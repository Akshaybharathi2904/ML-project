import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List, Any, Tuple

from src.utils.config import load_config, get_project_root
from src.recommender.content import ContentBasedRecommender, CATEGORIES
from src.recommender.collaborative import CollaborativeRecommender
from src.recommender.hybrid import HybridRecommender
from src.evaluation.rec_metrics import compute_rating_error_metrics, compute_ranking_metrics_at_k
from src.evaluation.opt_metrics import evaluate_optimizer_run
from src.optimizer.problem import TravelPlanningProblem, ItinerarySolution
from src.optimizer.solve import solve_itinerary_optimization
from src.optimizer.baselines import BaselineSolvers
from src.optimizer.selection import ParetoSelector

# Styling for publication-grade matplotlib figures
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.size"] = 11


def run_recommender_experiments(
    places_df: pd.DataFrame,
    users_df: pd.DataFrame,
    ratings_df: pd.DataFrame,
    cold_ratings_df: pd.DataFrame,
    output_dir: Path
) -> pd.DataFrame:
    """
    Train / Val / Test split ablation study comparing:
      1. Content-Only Recommender
      2. Collaborative-Only Recommender (SVD)
      3. Hybrid Recommender (LightGBM)
    Including cold-start evaluation on held-out users.
    """
    print("\n" + "=" * 60)
    print("STAGE 4.1: Recommender Evaluation & Ablation Study")
    print("=" * 60)

    # 80/20 train/test split on active user ratings
    ratings_shuffled = ratings_df.sample(frac=1.0, random_state=42).reset_index(drop=True)
    split_idx = int(0.8 * len(ratings_shuffled))
    train_ratings = ratings_shuffled.iloc[:split_idx]
    test_ratings = ratings_shuffled.iloc[split_idx:]

    print(f"Train ratings: {len(train_ratings)}, Test ratings: {len(test_ratings)}")

    # 1. Fit Content-Based
    print("Evaluating Content-Based Recommender...")
    cb = ContentBasedRecommender().fit(places_df)

    # 2. Fit Collaborative
    print("Evaluating SVD Collaborative Recommender...")
    cf = CollaborativeRecommender(n_components=20).fit(train_ratings)

    # 3. Fit Hybrid
    print("Evaluating Hybrid Recommender...")
    hybrid = HybridRecommender()
    hybrid.fit(places_df, users_df, train_ratings)

    # Pre-build user profiles lookup
    user_dict = {u["id"]: u.to_dict() for _, u in users_df.iterrows()}

    # Compute test predictions for sample of 150 test users for speed & statistical power
    eval_uids = list(test_ratings["user_id"].unique())[:150]
    test_subset = test_ratings[test_ratings["user_id"].isin(eval_uids)].copy()

    records_cb = []
    records_cf = []
    records_hyb = []
    y_true = []

    for _, row in test_subset.iterrows():
        uid = row["user_id"]
        pid = row["place_id"]
        true_r = row["rating"]
        y_true.append(true_r)

        u_prof = user_dict.get(uid, {})
        cat_w = {c: float(u_prof.get(f"pref_{c}", 0.1)) for c in CATEGORIES}

        # CB score
        cb_score = cb.score_for_user_profile(cat_w, u_prof.get("budget_level", "medium")).get(pid, 0.5)
        pred_cb = 1.0 + cb_score * 4.0
        records_cb.append({"user_id": uid, "place_id": pid, "rating_pred": pred_cb, "score": cb_score})

        # CF score
        pred_cf = cf.predict(uid, pid)
        score_cf = (pred_cf - 1.0) / 4.0
        records_cf.append({"user_id": uid, "place_id": pid, "rating_pred": pred_cf, "score": score_cf})

    # Hybrid evaluation (batch for users)
    user_scores_cache = {}
    for uid in eval_uids:
        u_prof = user_dict[uid]
        s_df, _ = hybrid.predict_personalization_scores(u_prof)
        user_scores_cache[uid] = s_df.set_index("id")

    for _, row in test_subset.iterrows():
        uid = row["user_id"]
        pid = row["place_id"]
        u_df = user_scores_cache[uid]
        pred_h = float(u_df.loc[pid, "predicted_rating"]) if pid in u_df.index else 3.5
        score_h = float(u_df.loc[pid, "personalization_score"]) if pid in u_df.index else 0.5
        records_hyb.append({"user_id": uid, "place_id": pid, "rating_pred": pred_h, "score": score_h})

    df_cb = pd.DataFrame(records_cb)
    df_cf = pd.DataFrame(records_cf)
    df_hyb = pd.DataFrame(records_hyb)
    y_true_arr = np.array(y_true)

    # Compute Error & Ranking metrics
    models = {
        "Content-Only": (df_cb, y_true_arr),
        "Collaborative-Only (SVD)": (df_cf, y_true_arr),
        "Hybrid (LightGBM)": (df_hyb, y_true_arr),
    }

    results = []
    for name, (m_df, yt) in models.items():
        err = compute_rating_error_metrics(yt, m_df["rating_pred"].to_numpy())
        rnk5 = compute_ranking_metrics_at_k(test_subset, m_df, k=5)
        rnk10 = compute_ranking_metrics_at_k(test_subset, m_df, k=10)
        results.append({
            "Model": name,
            "RMSE": err["RMSE"],
            "MAE": err["MAE"],
            "Precision@5": rnk5["Precision@5"],
            "Recall@5": rnk5["Recall@5"],
            "NDCG@5": rnk5["NDCG@5"],
            "Precision@10": rnk10["Precision@10"],
            "Recall@10": rnk10["Recall@10"],
            "NDCG@10": rnk10["NDCG@10"],
        })

    # Cold-Start Evaluation on held-out cold users
    print("Evaluating Cold-Start Performance on held-out users...")
    cold_uids = list(cold_ratings_df["user_id"].unique())[:60]
    cold_subset = cold_ratings_df[cold_ratings_df["user_id"].isin(cold_uids)].copy()

    cold_records_cb = []
    cold_records_cf = []
    cold_records_hyb = []
    cold_y_true = []

    for uid in cold_uids:
        u_prof = user_dict[uid]
        s_df, _ = hybrid.predict_personalization_scores(u_prof)
        user_scores_cache[uid] = s_df.set_index("id")

    for _, row in cold_subset.iterrows():
        uid = row["user_id"]
        pid = row["place_id"]
        true_r = row["rating"]
        cold_y_true.append(true_r)
        u_prof = user_dict[uid]
        cat_w = {c: float(u_prof.get(f"pref_{c}", 0.1)) for c in CATEGORIES}

        # CB
        cb_sc = cb.score_for_user_profile(cat_w, u_prof.get("budget_level", "medium")).get(pid, 0.5)
        cold_records_cb.append({"user_id": uid, "place_id": pid, "rating_pred": 1.0 + cb_sc * 4.0, "score": cb_sc})

        # CF (Unseen user fallback to item mean)
        pred_cf = cf.predict(uid, pid)
        cold_records_cf.append({"user_id": uid, "place_id": pid, "rating_pred": pred_cf, "score": (pred_cf - 1.0) / 4.0})

        # Hybrid
        u_df = user_scores_cache[uid]
        pred_h = float(u_df.loc[pid, "predicted_rating"]) if pid in u_df.index else 3.5
        score_h = float(u_df.loc[pid, "personalization_score"]) if pid in u_df.index else 0.5
        cold_records_hyb.append({"user_id": uid, "place_id": pid, "rating_pred": pred_h, "score": score_h})

    cold_y_arr = np.array(cold_y_true)
    cold_models = {
        "Content-Only (Cold)": (pd.DataFrame(cold_records_cb), cold_y_arr),
        "Collaborative-Only (Cold)": (pd.DataFrame(cold_records_cf), cold_y_arr),
        "Hybrid (Cold-Start)": (pd.DataFrame(cold_records_hyb), cold_y_arr),
    }
    for name, (m_df, yt) in cold_models.items():
        err = compute_rating_error_metrics(yt, m_df["rating_pred"].to_numpy())
        rnk10 = compute_ranking_metrics_at_k(cold_subset, m_df, k=10)
        results.append({
            "Model": name,
            "RMSE": err["RMSE"],
            "MAE": err["MAE"],
            "Precision@5": "-",
            "Recall@5": "-",
            "NDCG@5": "-",
            "Precision@10": rnk10["Precision@10"],
            "Recall@10": rnk10["Recall@10"],
            "NDCG@10": rnk10["NDCG@10"],
        })

    ablation_df = pd.DataFrame(results)
    
    # Save table
    tables_dir = output_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    ablation_df.to_csv(tables_dir / "recommender_ablation.csv", index=False)
    ablation_df.to_markdown(tables_dir / "recommender_ablation.md", index=False)
    print(f" Saved Recommender Ablation table to {tables_dir / 'recommender_ablation.md'}")

    return ablation_df


def run_optimizer_experiments(
    places_df: pd.DataFrame,
    travel_time_matrix: pd.DataFrame,
    output_dir: Path,
    num_seeds: int = 10
) -> pd.DataFrame:
    """
    Run 10-seed comparison between NSGA-II, NSGA-III / MOEA/D, and Baselines.
    Reports Mean ± Std for Hypervolume, Spacing, Non-Dominated Count, and Runtime.
    """
    print("\n" + "=" * 60)
    print(f"STAGE 4.2: Optimizer Evaluation across {num_seeds} Independent Seeds")
    print("=" * 60)

    # Use candidate set of top 45 places
    places = places_df.copy()
    places["personalization_score"] = (places["rating"] / 5.0) * places["popularity"]
    candidates = places.head(45).copy().reset_index(drop=True)

    prob = TravelPlanningProblem(
        candidate_places=candidates,
        travel_time_matrix=travel_time_matrix,
        num_days=3,
        daily_time_budget_min=600.0,
        total_budget_cap=9000.0,
        max_places_per_day=4,
        start_lat=12.9716,
        start_lon=77.5946,
        start_city="Bengaluru"
    )

    seeds = list(range(100, 100 + num_seeds))
    nsga2_runs = []
    nsga3_runs = []

    print("Running NSGA-II over 10 seeds...")
    for s in seeds:
        t0 = time.perf_counter()
        res = solve_itinerary_optimization(prob, algorithm_name="nsga2", pop_size=35, generations=30, seed=s)
        dt = time.perf_counter() - t0
        metrics = evaluate_optimizer_run(res.pareto_solutions, dt)
        nsga2_runs.append(metrics)

    print("Running NSGA-III / Reference-Direction solver over 10 seeds...")
    for s in seeds:
        t0 = time.perf_counter()
        res = solve_itinerary_optimization(prob, algorithm_name="nsga3", pop_size=35, generations=30, seed=s)
        dt = time.perf_counter() - t0
        metrics = evaluate_optimizer_run(res.pareto_solutions, dt)
        nsga3_runs.append(metrics)

    # Run Baselines
    print("Evaluating Baselines...")
    baselines = BaselineSolvers(prob)

    # 1. Random (100 samples)
    t0 = time.perf_counter()
    rand_sols = baselines.solve_random(num_samples=100)
    dt_rand = time.perf_counter() - t0
    # Filter non-dominated random solutions
    F_rand = np.array([s.objectives for s in rand_sols])
    from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting
    nds = NonDominatedSorting()
    front0 = nds.do(F_rand)[0]
    rand_pareto = [rand_sols[i] for i in front0]
    m_rand = evaluate_optimizer_run(rand_pareto, dt_rand)

    # 2. Greedy Score
    t0 = time.perf_counter()
    greedy_s = baselines.solve_greedy_score()
    dt_gs = time.perf_counter() - t0
    m_greedy_score = evaluate_optimizer_run([greedy_s], dt_gs)

    # 3. Greedy Score / Cost
    t0 = time.perf_counter()
    greedy_sc = baselines.solve_greedy_score_cost()
    dt_gsc = time.perf_counter() - t0
    m_greedy_ratio = evaluate_optimizer_run([greedy_sc], dt_gsc)

    # 4. Weighted-Sum GA
    t0 = time.perf_counter()
    ga_sol = baselines.solve_weighted_sum_ga(pop_size=35, generations=30, seed=42)
    dt_ga = time.perf_counter() - t0
    m_ws_ga = evaluate_optimizer_run([ga_sol], dt_ga)

    # Aggregate Statistics
    def stats_str(run_dicts, key):
        vals = [d[key] for d in run_dicts]
        return f"{np.mean(vals):.3f} ± {np.std(vals):.3f}"

    benchmarks = [
        {
            "Method": "Random Itineraries (N=100)",
            "Hypervolume": f"{m_rand['Hypervolume']:.3f}",
            "Spacing": f"{m_rand['Spacing']:.3f}",
            "Pareto Solutions": f"{m_rand['NonDominatedSolutions']}",
            "Runtime (s)": f"{m_rand['RuntimeSec']:.2f}",
            "Violation Rate": f"{m_rand['ViolationRate']:.1%}",
        },
        {
            "Method": "Greedy (by Personalization Score)",
            "Hypervolume": f"{m_greedy_score['Hypervolume']:.3f}",
            "Spacing": "-",
            "Pareto Solutions": "1",
            "Runtime (s)": f"{m_greedy_score['RuntimeSec']:.3f}",
            "Violation Rate": f"{m_greedy_score['ViolationRate']:.1%}",
        },
        {
            "Method": "Greedy (Score / Cost Ratio)",
            "Hypervolume": f"{m_greedy_ratio['Hypervolume']:.3f}",
            "Spacing": "-",
            "Pareto Solutions": "1",
            "Runtime (s)": f"{m_greedy_ratio['RuntimeSec']:.3f}",
            "Violation Rate": f"{m_greedy_ratio['ViolationRate']:.1%}",
        },
        {
            "Method": "Weighted-Sum Single-Obj GA",
            "Hypervolume": f"{m_ws_ga['Hypervolume']:.3f}",
            "Spacing": "-",
            "Pareto Solutions": "1",
            "Runtime (s)": f"{m_ws_ga['RuntimeSec']:.2f}",
            "Violation Rate": f"{m_ws_ga['ViolationRate']:.1%}",
        },
        {
            "Method": "NSGA-III (10 seeds)",
            "Hypervolume": stats_str(nsga3_runs, "Hypervolume"),
            "Spacing": stats_str(nsga3_runs, "Spacing"),
            "Pareto Solutions": stats_str(nsga3_runs, "NonDominatedSolutions"),
            "Runtime (s)": stats_str(nsga3_runs, "RuntimeSec"),
            "Violation Rate": stats_str(nsga3_runs, "ViolationRate"),
        },
        {
            "Method": "NSGA-II (10 seeds, Main)",
            "Hypervolume": stats_str(nsga2_runs, "Hypervolume"),
            "Spacing": stats_str(nsga2_runs, "Spacing"),
            "Pareto Solutions": stats_str(nsga2_runs, "NonDominatedSolutions"),
            "Runtime (s)": stats_str(nsga2_runs, "RuntimeSec"),
            "Violation Rate": stats_str(nsga2_runs, "ViolationRate"),
        },
    ]

    bench_df = pd.DataFrame(benchmarks)
    tables_dir = output_dir / "tables"
    bench_df.to_csv(tables_dir / "optimizer_benchmark.csv", index=False)
    bench_df.to_markdown(tables_dir / "optimizer_benchmark.md", index=False)
    print(f" Saved Optimizer Benchmark table to {tables_dir / 'optimizer_benchmark.md'}")

    return bench_df, nsga2_runs, nsga3_runs


def run_end_to_end_experiments(
    places_df: pd.DataFrame,
    travel_time_matrix: pd.DataFrame,
    hybrid: HybridRecommender,
    users_df: pd.DataFrame,
    output_dir: Path,
    num_eval_users: int = 20
) -> pd.DataFrame:
    """
    Simulate user satisfaction for Hybrid + NSGA-II vs Baselines.
    Satisfaction combines personalization match, budget efficiency, travel brevity, and category diversity.
    """
    print("\n" + "=" * 60)
    print(f"STAGE 4.3: End-to-End User Satisfaction Simulation (N={num_eval_users} Travelers)")
    print("=" * 60)

    sample_users = users_df.sample(num_eval_users, random_state=42).to_dict(orient="records")

    methods = ["Random", "Greedy Score", "Greedy Score/Cost", "Weighted-Sum GA", "Hybrid + NSGA-II (Knee Point)"]
    satisfaction_records = {m: [] for m in methods}

    for u in sample_users:
        budget_cap = 6000.0 if u["budget_level"] == "low" else (12000.0 if u["budget_level"] == "medium" else 20000.0)
        pace_limit = 3 if u["pace"] == "relaxed" else (5 if u["pace"] == "moderate" else 7)
        daily_time = 480.0 if u["pace"] == "relaxed" else (600.0 if u["pace"] == "moderate" else 720.0)

        # 1. Personalize candidate places with Hybrid model
        scored_places, _ = hybrid.predict_personalization_scores(u, start_city="Bengaluru")
        candidates = scored_places.sort_values(by="personalization_score", ascending=False).head(40).copy().reset_index(drop=True)

        prob = TravelPlanningProblem(
            candidate_places=candidates,
            travel_time_matrix=travel_time_matrix,
            num_days=3,
            daily_time_budget_min=daily_time,
            total_budget_cap=budget_cap,
            max_places_per_day=pace_limit,
            start_lat=12.9716,
            start_lon=77.5946,
            start_city="Bengaluru"
        )
        solvers = BaselineSolvers(prob)

        # Get solutions for each method
        s_rand = solvers.solve_random(num_samples=1)[0]
        s_g_score = solvers.solve_greedy_score()
        s_g_ratio = solvers.solve_greedy_score_cost()
        s_ws_ga = solvers.solve_weighted_sum_ga(pop_size=25, generations=20, seed=42)
        
        # NSGA-II + Knee Point
        nsga_res = solve_itinerary_optimization(prob, algorithm_name="nsga2", pop_size=30, generations=25, seed=42)
        s_knee = nsga_res.knee_solution

        evaluated = [
            ("Random", s_rand),
            ("Greedy Score", s_g_score),
            ("Greedy Score/Cost", s_g_ratio),
            ("Weighted-Sum GA", s_ws_ga),
            ("Hybrid + NSGA-II (Knee Point)", s_knee),
        ]

        # Multi-attribute satisfaction scoring function (0 - 100 scale)
        for m_name, sol in evaluated:
            n_stops = sum(len(d.stops) for d in sol.days)
            if n_stops == 0:
                sat = 10.0
            else:
                score_term = min(sol.total_personalization_score / (3.0 * pace_limit), 1.0) * 45.0
                cost_term = max(0.0, 1.0 - sol.total_cost / budget_cap) * 20.0
                time_term = max(0.0, 1.0 - sol.total_travel_time / (3.0 * daily_time * 0.4)) * 15.0
                div_term = min(sol.category_diversity / 2.0, 1.0) * 10.0
                crowd_term = (1.0 - sol.avg_crowd_level) * 10.0
                sat = float(score_term + cost_term + time_term + div_term + crowd_term)

            satisfaction_records[m_name].append(round(sat, 2))

    summary = []
    for m in methods:
        arr = np.array(satisfaction_records[m])
        summary.append({
            "Planning Strategy": m,
            "Mean Satisfaction (%)": round(float(np.mean(arr)), 2),
            "Std (%)": round(float(np.std(arr)), 2),
            "Min (%)": round(float(np.min(arr)), 2),
            "Max (%)": round(float(np.max(arr)), 2),
        })

    sat_df = pd.DataFrame(summary)
    tables_dir = output_dir / "tables"
    sat_df.to_csv(tables_dir / "end_to_end_satisfaction.csv", index=False)
    sat_df.to_markdown(tables_dir / "end_to_end_satisfaction.md", index=False)
    print(f" Saved End-to-End Satisfaction table to {tables_dir / 'end_to_end_satisfaction.md'}")

    return sat_df, satisfaction_records


def generate_publication_figures(
    ablation_df: pd.DataFrame,
    bench_df: pd.DataFrame,
    nsga2_runs: List[Dict[str, float]],
    nsga3_runs: List[Dict[str, float]],
    satisfaction_records: Dict[str, List[float]],
    figures_dir: Path
):
    """Generate high-resolution PNG figures for papers, reports, and UI display."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    print("\nGenerating publication-quality figures in results/figures/...")

    # Figure 1: Recommender Ablation (RMSE & NDCG@10)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    plot_df = ablation_df.iloc[:3].copy()
    
    colors = ["#3498db", "#e67e22", "#2ecc71"]
    sns.barplot(x="Model", y="RMSE", data=plot_df, palette=colors, ax=ax1)
    ax1.set_title("Rating Prediction Error (RMSE, Lower is Better)", fontweight="bold")
    ax1.set_ylabel("RMSE")
    ax1.tick_params(axis="x", rotation=15)
    for p in ax1.patches:
        ax1.annotate(f"{p.get_height():.3f}", (p.get_x() + p.get_width() / 2., p.get_height() / 2.),
                     ha='center', va='center', color='white', fontweight='bold')

    sns.barplot(x="Model", y="NDCG@10", data=plot_df, palette=colors, ax=ax2)
    ax2.set_title("Ranking Quality (NDCG@10, Higher is Better)", fontweight="bold")
    ax2.set_ylabel("NDCG@10")
    ax2.tick_params(axis="x", rotation=15)
    for p in ax2.patches:
        ax2.annotate(f"{p.get_height():.3f}", (p.get_x() + p.get_width() / 2., p.get_height() / 2.),
                     ha='center', va='center', color='white', fontweight='bold')

    plt.tight_layout()
    fig.savefig(figures_dir / "fig1_recommender_ablation.png", dpi=300)
    plt.close()

    # Figure 2: Optimizer Hypervolume Comparison across 10 Seeds
    fig, ax = plt.subplots(figsize=(7, 4.5))
    hv_data = pd.DataFrame({
        "NSGA-II": [r["Hypervolume"] for r in nsga2_runs],
        "NSGA-III": [r["Hypervolume"] for r in nsga3_runs],
    })
    sns.boxplot(data=hv_data, palette=["#2980b9", "#8e44ad"], ax=ax, width=0.45)
    sns.stripplot(data=hv_data, color="black", alpha=0.6, jitter=0.15, size=7, ax=ax)
    ax.set_title("Hypervolume Indicator across 10 Random Seeds", fontweight="bold")
    ax.set_ylabel("Normalized Hypervolume (HV)")
    plt.tight_layout()
    fig.savefig(figures_dir / "fig2_hypervolume_comparison.png", dpi=300)
    plt.close()

    # Figure 3: End-to-End User Satisfaction Boxplot
    fig, ax = plt.subplots(figsize=(10, 4.5))
    sat_melt = []
    for k, vals in satisfaction_records.items():
        for v in vals:
            sat_melt.append({"Method": k, "Satisfaction": v})
    sat_melt_df = pd.DataFrame(sat_melt)
    palette = ["#95a5a6", "#f39c12", "#d35400", "#9b59b6", "#27ae60"]
    sns.boxplot(x="Method", y="Satisfaction", data=sat_melt_df, palette=palette, ax=ax)
    ax.set_title("End-to-End Simulated User Satisfaction (%) across 20 Travelers", fontweight="bold")
    ax.set_ylabel("User Satisfaction Score (%)")
    ax.tick_params(axis="x", rotation=15)
    plt.tight_layout()
    fig.savefig(figures_dir / "fig3_end_to_end_satisfaction.png", dpi=300)
    plt.close()

    print(" Publication figures successfully generated.")


def main():
    root = get_project_root()
    output_dir = root / "results"
    output_dir.mkdir(parents=True, exist_ok=True)

    config = load_config()
    places_df = pd.read_csv(root / config["data"]["places_csv"])
    users_df = pd.read_csv(root / config["data"]["users_csv"])
    ratings_df = pd.read_csv(root / config["data"]["ratings_csv"])
    cold_ratings_df = pd.read_csv(root / "data" / "processed" / "cold_start_eval_ratings.csv")
    time_mat = pd.read_csv(root / config["data"]["travel_time_matrix_csv"], index_col=0)

    # 1. Recommender experiments
    ablation_df = run_recommender_experiments(places_df, users_df, ratings_df, cold_ratings_df, output_dir)

    # Retrain full hybrid model for end-to-end evaluation
    print("\nFitting full Hybrid Recommender for downstream optimization...")
    hybrid = HybridRecommender().fit(places_df, users_df, ratings_df)

    # 2. Optimizer experiments
    bench_df, nsga2_runs, nsga3_runs = run_optimizer_experiments(places_df, time_mat, output_dir, num_seeds=10)

    # 3. End-to-end user satisfaction
    sat_df, satisfaction_records = run_end_to_end_experiments(places_df, time_mat, hybrid, users_df, output_dir, num_eval_users=20)

    # 4. Generate publication figures
    generate_publication_figures(ablation_df, bench_df, nsga2_runs, nsga3_runs, satisfaction_records, output_dir / "figures")

    print("\n" + "=" * 60)
    print("ALL EXPERIMENTS COMPLETED SUCCESSFULLY!")
    print(f"Results and figures saved to: {output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()

