import sys
from pathlib import Path

# Ensure project root is in sys.path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

from src.utils.config import load_config, get_project_root
from src.recommender.hybrid import HybridRecommender, FEATURE_COLUMNS
from src.recommender.explain import RecommendationExplainer
from src.optimizer.problem import TravelPlanningProblem, ItinerarySolution, ItineraryStop
from src.optimizer.solve import solve_itinerary_optimization, OptimizerResult
from src.optimizer.selection import ParetoSelector

# Page Configuration
st.set_page_config(
    page_title="AI Travel Planner | Hybrid ML & Pareto MOO",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1f77b4, #00b4d8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .day-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 12px;
        font-weight: bold;
        color: white;
        margin-right: 8px;
    }
    .tag-badge {
        display: inline-block;
        background-color: #e2e8f0;
        color: #2d3748;
        padding: 2px 8px;
        border-radius: 8px;
        font-size: 0.8rem;
        margin-right: 4px;
    }
    .why-badge {
        background-color: #ecfdf5;
        border-left: 4px solid #10b981;
        padding: 8px 12px;
        border-radius: 4px;
        font-size: 0.85rem;
        color: #065f46;
        margin-top: 6px;
    }
    .footer-text {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_and_train_recommender():
    """Load datasets and train the hybrid recommender engine once."""
    root = get_project_root()
    cfg = load_config()
    places_df = pd.read_csv(root / cfg["data"]["places_csv"])
    users_df = pd.read_csv(root / cfg["data"]["users_csv"])
    ratings_df = pd.read_csv(root / cfg["data"]["ratings_csv"])
    time_mat = pd.read_csv(root / cfg["data"]["travel_time_matrix_csv"], index_col=0)

    model = HybridRecommender()
    model.fit(places_df, users_df, ratings_df)
    explainer = RecommendationExplainer(model)
    return cfg, places_df, users_df, time_mat, model, explainer


config, places_df, users_df, time_mat, recommender, explainer = load_and_train_recommender()

# Session State Initialization
if "optimizer_result" not in st.session_state:
    st.session_state.optimizer_result = None
if "selected_solution_idx" not in st.session_state:
    st.session_state.selected_solution_idx = 0
if "excluded_places" not in st.session_state:
    st.session_state.excluded_places = set()
if "last_query_params" not in st.session_state:
    st.session_state.last_query_params = None

# Top Title Header
st.markdown('<div class="main-header">🧭 Intelligent & Personalized Travel Planning System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Hybrid Machine Learning Recommendation & Multi-Objective Pareto Optimization (NSGA-II)</div>', unsafe_allow_html=True)

# SIDEBAR CONTROLS
st.sidebar.header("🎯 Travel Preferences")

region_name = config.get("region", {}).get("name", "South India")
st.sidebar.info(f"📍 **Target Region:** {region_name} (Tamil Nadu, Kerala, Karnataka)")

start_cities = config.get("region", {}).get("cities", ["Bengaluru", "Chennai", "Kochi", "Mysuru"])
start_city = st.sidebar.selectbox("Starting Hub City", start_cities, index=0)

col_days, col_pace = st.sidebar.columns(2)
with col_days:
    num_days = st.slider("Trip Duration (Days)", min_value=1, max_value=7, value=3)
with col_pace:
    pace = st.selectbox("Travel Pace", ["relaxed", "moderate", "packed"], index=1)

budget_cap = st.sidebar.slider("Total Budget (INR)", min_value=2000, max_value=40000, value=12000, step=1000)
season = st.sidebar.selectbox("Travel Season", ["winter", "monsoon", "summer", "all"], index=0)

# Interest Weight Sliders
with st.sidebar.expander("🎨 Destination Category Interests", expanded=True):
    st.caption("Adjust sliders to customize your personal taste profile:")
    all_categories = [
        "heritage", "nature", "beach", "temple", "adventure",
        "food", "shopping", "museum", "wildlife", "hill_station"
    ]
    interest_weights = {}
    default_vals = {
        "heritage": 0.8, "nature": 0.9, "beach": 0.5, "temple": 0.6, "adventure": 0.4,
        "food": 0.7, "shopping": 0.4, "museum": 0.5, "wildlife": 0.6, "hill_station": 0.7
    }
    for cat in all_categories:
        interest_weights[cat] = st.slider(f"{cat.capitalize()}", 0.0, 1.0, default_vals.get(cat, 0.5), 0.1)

# Interactive Seed Ratings for Collaborative Folding
with st.sidebar.expander("⭐ Seed Ratings (Cold-Start Adaptation)", expanded=False):
    st.caption("Rate a few well-known landmarks to activate collaborative matrix factorization folding:")
    seed_places = [
        ("P001", "Bangalore Palace"),
        ("P009", "Mysore Palace"),
        ("P037", "Meenakshi Temple"),
        ("P055", "Fort Kochi"),
        ("P064", "Alleppey Houseboat"),
    ]
    user_seed_ratings = {}
    for pid, pname in seed_places:
        r = st.slider(f"{pname}", 0, 5, 0, 1, key=f"seed_{pid}", help="Set to 0 if not visited/unrated")
        if r > 0:
            user_seed_ratings[pid] = float(r)

# Excluded Places Management
if st.session_state.excluded_places:
    with st.sidebar.expander(f"🚫 Excluded Places ({len(st.session_state.excluded_places)})", expanded=False):
        for ep in list(st.session_state.excluded_places):
            c1, c2 = st.columns([3, 1])
            c1.write(ep)
            if c2.button("Remove", key=f"unex_{ep}"):
                st.session_state.excluded_places.remove(ep)
                st.rerun()
        if st.button("Clear All Exclusions"):
            st.session_state.excluded_places.clear()
            st.rerun()

generate_btn = st.sidebar.button("🚀 Optimize Itinerary", type="primary", use_container_width=True)


def execute_planner(user_weights, budget, days, user_pace, start_c, travel_s, seed_rats, excluded):
    """Run Stage 1 Scoring + Stage 2 Optimization."""
    with st.spinner("1/2: Calculating Hybrid Personalization Scores & SHAP attributions..."):
        # Map budget and pace
        b_tier = "low" if budget <= 6000 else ("medium" if budget <= 18000 else "luxury")
        user_prof = {
            "budget_level": b_tier,
            "pace": user_pace,
            **{f"pref_{cat}": w for cat, w in user_weights.items()}
        }

        scored_places, feat_matrix = recommender.predict_personalization_scores(
            user_profile=user_prof,
            start_city=start_c,
            travel_season=travel_s,
            user_seed_ratings=seed_rats
        )

        # Filter out excluded places
        if excluded:
            scored_places = scored_places[~scored_places["name"].isin(excluded)].copy()

        # Pre-filter top candidates (top 45 places by personalization score + nearby attractions)
        candidates = scored_places.sort_values(by="personalization_score", ascending=False).head(45).copy().reset_index(drop=True)

    with st.spinner("2/2: Exploring Pareto Front via NSGA-II Multi-Objective Optimization..."):
        # Pace limits
        pace_limits = config.get("pace_limits", {}).get(user_pace, {"max_places_per_day": 4, "daily_time_budget_min": 600.0})
        max_p = pace_limits["max_places_per_day"]
        day_time_limit = pace_limits["daily_time_budget_min"]

        # City coords
        start_coord = recommender.city_coords.get(start_c, (12.9716, 77.5946))

        problem = TravelPlanningProblem(
            candidate_places=candidates,
            travel_time_matrix=time_mat,
            num_days=days,
            daily_time_budget_min=day_time_limit,
            total_budget_cap=budget,
            max_places_per_day=max_p,
            start_lat=start_coord[0],
            start_lon=start_coord[1],
            start_city=start_c,
            day_start_time_str="08:30"
        )

        res = solve_itinerary_optimization(
            problem=problem,
            algorithm_name="nsga2",
            pop_size=35,
            generations=30,
            seed=42
        )

    return res, scored_places, feat_matrix


# Trigger Run if button pressed or if not yet run
if generate_btn or st.session_state.optimizer_result is None:
    opt_res, scored_df, feat_mat = execute_planner(
        interest_weights, budget_cap, num_days, pace, start_city, season, user_seed_ratings, st.session_state.excluded_places
    )
    st.session_state.optimizer_result = opt_res
    st.session_state.scored_places = scored_df
    st.session_state.feat_matrix = feat_mat
    st.session_state.selected_solution_idx = opt_res.knee_index

# Fetch Current Session State
opt_res: OptimizerResult = st.session_state.optimizer_result
scored_df: pd.DataFrame = st.session_state.scored_places
feat_mat: pd.DataFrame = st.session_state.feat_matrix
pareto_sols = opt_res.pareto_solutions

# TABS NAVIGATION
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📅 Itinerary",
    "📊 Pareto Explorer",
    "🗺️ Interactive Map",
    "💡 Model Insights & SHAP",
    "📈 Evaluation & Metrics",
    "⚖️ Side-by-Side Compare"
])

# ----------------------------------------------------
# TAB 1: ITINERARY TIMELINE & EXPLANATIONS
# ----------------------------------------------------
with tab1:
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.subheader("Selected Day-by-Day Itinerary Plan")
    with col_t2:
        sol_options = [f"Plan #{i+1} {'(⭐ Knee Point)' if i == opt_res.knee_index else ''}" for i in range(len(pareto_sols))]
        chosen_opt = st.selectbox(
            "Select Pareto Plan",
            options=range(len(pareto_sols)),
            format_func=lambda i: sol_options[i],
            index=st.session_state.selected_solution_idx
        )
        st.session_state.selected_solution_idx = chosen_opt

    active_sol: ItinerarySolution = pareto_sols[st.session_state.selected_solution_idx]

    # Metrics Summary Row
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    m1.metric("Satisfaction Score", f"{active_sol.total_personalization_score:.2f}")
    m2.metric("Total Cost", f"₹{active_sol.total_cost:,.0f}", delta=f"Budget: ₹{budget_cap:,.0f}")
    m3.metric("Total Travel Time", f"{int(active_sol.total_travel_time // 60)}h {int(active_sol.total_travel_time % 60)}m")
    m4.metric("Category Entropy", f"{active_sol.category_diversity:.2f}")
    m5.metric("Avg Crowd Level", f"{active_sol.avg_crowd_level:.2f}")
    total_stops = sum(len(d.stops) for d in active_sol.days)
    m6.metric("Total Stops", f"{total_stops} places")

    st.markdown("---")

    # Render Day Schedules
    DAY_COLORS = ["#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899", "#06b6d4", "#14b8a6"]

    def format_time_min(min_val):
        h = int(min_val // 60)
        m = int(min_val % 60)
        suffix = "AM" if h < 12 else "PM"
        display_h = h if 1 <= h <= 12 else (h - 12 if h > 12 else 12)
        return f"{display_h:02d}:{m:02d} {suffix}"

    for day in active_sol.days:
        day_color = DAY_COLORS[(day.day_number - 1) % len(DAY_COLORS)]
        with st.expander(f"📍 Day {day.day_number} — {len(day.stops)} Stops | Travel: {int(day.total_travel_time_min)} min | Cost: ₹{day.total_cost_inr:,.0f}", expanded=True):
            if not day.stops:
                st.info("Rest or free exploration day.")
                continue

            for s_idx, stop in enumerate(day.stops):
                st.markdown(f"""
                <div style="border-left: 3px solid {day_color}; padding-left: 12px; margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: bold; font-size: 1.1rem;">
                            <span class="day-badge" style="background-color: {day_color};">Stop {s_idx + 1}</span>
                            {stop.place_name} ({stop.city})
                        </span>
                        <span>
                            <span class="tag-badge">Category: {stop.category.capitalize()}</span>
                            <span class="tag-badge">Cost: ₹{stop.cost_inr:,.0f}</span>
                            <span class="tag-badge">Crowd: {int(stop.crowd_level * 100)}%</span>
                        </span>
                    </div>
                    <div style="color: #555; font-size: 0.9rem; margin-top: 4px;">
                        ⏰ <b>Schedule:</b> {format_time_min(stop.arrival_time_min)} - {format_time_min(stop.departure_time_min)} 
                        (Duration: {int(stop.visit_duration_min)} min | Transit: {int(stop.travel_time_from_prev_min)} min)
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # SHAP Explainability Reasons
                exp_dict = explainer.explain_place(stop.place_id, scored_df, feat_mat)
                reasons_html = "".join([f"<li>{r}</li>" for r in exp_dict["reasons"]])
                st.markdown(f"""
                <div class="why-badge">
                    <b>💡 Why this place?</b>
                    <ul style="margin: 2px 0 0 15px; padding: 0;">
                        {reasons_html}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

                # Replace this place button
                c_rep, _ = st.columns([2, 5])
                if c_rep.button(f"🔄 Replace '{stop.place_name}'", key=f"rep_{stop.place_id}_{day.day_number}"):
                    st.session_state.excluded_places.add(stop.place_name)
                    st.rerun()

    # Export Section
    st.markdown("### 📥 Export Your Itinerary")
    e_col1, e_col2 = st.columns(2)

    # 1. CSV Export
    csv_rows = []
    for d in active_sol.days:
        for s in d.stops:
            csv_rows.append({
                "Day": d.day_number,
                "Place": s.place_name,
                "City": s.city,
                "Category": s.category,
                "Arrival": format_time_min(s.arrival_time_min),
                "Departure": format_time_min(s.departure_time_min),
                "Duration_Min": s.visit_duration_min,
                "Travel_From_Prev_Min": s.travel_time_from_prev_min,
                "Cost_INR": s.cost_inr,
                "Personalization_Score": s.personalization_score,
            })
    csv_df = pd.DataFrame(csv_rows)
    csv_bytes = csv_df.to_csv(index=False).encode("utf-8")
    e_col1.download_button("📄 Download as CSV", data=csv_bytes, file_name="itinerary.csv", mime="text/csv")

    # 2. Markdown Export
    md_content = f"# Personalized Travel Itinerary - {region_name}\n\n"
    md_content += f"- **Days:** {num_days}\n- **Budget:** ₹{active_sol.total_cost:,.0f} / ₹{budget_cap:,.0f}\n"
    md_content += f"- **Total Travel Time:** {int(active_sol.total_travel_time)} minutes\n- **Personalization Score:** {active_sol.total_personalization_score:.2f}\n\n"
    for d in active_sol.days:
        md_content += f"## Day {d.day_number}\n"
        for s in d.stops:
            md_content += f"- **{format_time_min(s.arrival_time_min)} - {format_time_min(s.departure_time_min)}**: {s.place_name} ({s.category}) | Cost: ₹{s.cost_inr:.0f}\n"
    e_col2.download_button("📝 Download as Markdown", data=md_content, file_name="itinerary.md", mime="text/markdown")


# ----------------------------------------------------
# TAB 2: PARETO EXPLORER
# ----------------------------------------------------
with tab2:
    st.subheader("Interactive Pareto Optimal Trade-Off Surface")
    st.write(
        "Multi-Objective optimization via **NSGA-II** returns a diverse Pareto front representing mathematically non-dominated compromises."
    )

    pareto_df = opt_res.selector.to_dataframe()

    # Interactive Preference Sliders to navigate the front
    st.markdown("##### 🎛️ Dynamic Trade-off Weights (Picks from Pareto Front without re-running GA)")
    w_c1, w_c2, w_c3, w_c4, w_c5 = st.columns(5)
    w_sc = w_c1.slider("Satisfaction", 0.1, 5.0, 1.0, 0.1)
    w_co = w_c2.slider("Budget Thrift", 0.1, 5.0, 1.0, 0.1)
    w_ti = w_c3.slider("Travel Brevity", 0.1, 5.0, 1.0, 0.1)
    w_di = w_c4.slider("Diversity", 0.1, 5.0, 1.0, 0.1)
    w_cr = w_c5.slider("Crowd Avoidance", 0.1, 5.0, 1.0, 0.1)

    picked_idx, _ = opt_res.selector.select_by_weights(w_sc, w_co, w_ti, w_di, w_cr)
    if st.button("Apply Selected Trade-off Plan"):
        st.session_state.selected_solution_idx = picked_idx
        st.rerun()

    # 3D Scatter Plot
    fig_3d = px.scatter_3d(
        pareto_df,
        x="total_cost_inr",
        y="total_travel_time_min",
        z="total_score",
        color="category_diversity",
        size="total_places",
        hover_data=["solution_index", "avg_crowd_level"],
        title="Pareto Front (Cost vs Travel Time vs Personalization)",
        labels={
            "total_cost_inr": "Total Cost (INR)",
            "total_travel_time_min": "Travel Time (min)",
            "total_score": "Personalization Score",
            "category_diversity": "Diversity (Entropy)"
        },
        color_continuous_scale="Viridis",
        height=500,
    )
    # Highlight Knee Point and Selected Point
    knee_row = pareto_df.iloc[opt_res.knee_index]
    fig_3d.add_trace(go.Scatter3d(
        x=[knee_row["total_cost_inr"]],
        y=[knee_row["total_travel_time_min"]],
        z=[knee_row["total_score"]],
        mode="markers+text",
        marker=dict(size=12, color="gold", symbol="diamond"),
        text=["⭐ Knee Point"],
        textposition="top center",
        name="Knee Point"
    ))
    st.plotly_chart(fig_3d, use_container_width=True)

    # Pareto Table
    st.markdown("##### Complete Pareto Front Solutions")
    st.dataframe(pareto_df, use_container_width=True)


# ----------------------------------------------------
# TAB 3: INTERACTIVE FOLIUM MAP
# ----------------------------------------------------
with tab3:
    st.subheader("Geographic Route & Numbered Stops")
    active_sol: ItinerarySolution = pareto_sols[st.session_state.selected_solution_idx]

    # Compute center of itinerary
    all_stops = [s for d in active_sol.days for s in d.stops]
    if all_stops:
        center_lat = np.mean([s.lat for s in all_stops])
        center_lon = np.mean([s.lon for s in all_stops])
    else:
        center_lat, center_lon = 12.9716, 77.5946

    m = folium.Map(location=[center_lat, center_lon], zoom_start=8, tiles="CartoDB positron")

    DAY_MARKER_COLORS = ["blue", "green", "orange", "purple", "red", "cadetblue", "darkgreen"]

    for d in active_sol.days:
        day_color = DAY_MARKER_COLORS[(d.day_number - 1) % len(DAY_MARKER_COLORS)]
        day_coords = []

        for stop_idx, stop in enumerate(d.stops):
            coord = [stop.lat, stop.lon]
            day_coords.append(coord)

            popup_html = f"""
            <b>Day {d.day_number} - Stop #{stop_idx + 1}</b><br>
            <b>{stop.place_name}</b><br>
            City: {stop.city}<br>
            Category: {stop.category.capitalize()}<br>
            Arrival: {format_time_min(stop.arrival_time_min)}<br>
            Cost: ₹{stop.cost_inr:.0f}
            """

            folium.Marker(
                location=coord,
                popup=folium.Popup(popup_html, max_width=250),
                tooltip=f"Day {d.day_number}: {stop.place_name}",
                icon=folium.Icon(color=day_color, icon="info-sign")
            ).add_to(m)

        # Draw route polyline
        if len(day_coords) > 1:
            folium.PolyLine(
                locations=day_coords,
                color=day_color,
                weight=3.5,
                opacity=0.8,
                dash_array="5, 10" if d.day_number % 2 == 0 else None,
                tooltip=f"Day {d.day_number} Transit Route"
            ).add_to(m)

    st_folium(m, width="100%", height=550)


# ----------------------------------------------------
# TAB 4: MODEL INSIGHTS & SHAP
# ----------------------------------------------------
with tab4:
    st.subheader("Recommendation Model Explainability & Feature Insights")

    col_ins1, col_ins2 = st.columns([1, 1])

    with col_ins1:
        st.markdown("##### 🔍 Local SHAP Feature Attribution")
        st.write("Inspect how the LightGBM model scored any candidate place:")
        place_names = scored_df["name"].tolist()
        ins_place_name = st.selectbox("Select Place to Inspect", place_names, index=0)
        ins_pid = scored_df[scored_df["name"] == ins_place_name].iloc[0]["id"]

        shap_fig = explainer.generate_shap_waterfall_fig(ins_pid, scored_df, feat_mat)
        st.plotly_chart(shap_fig, use_container_width=True)

    with col_ins2:
        st.markdown("##### ⚖️ Hybrid vs Content vs Collaborative Breakdown")
        top_candidates = scored_df.sort_values(by="personalization_score", ascending=False).head(12)
        breakdown_fig = go.Figure()
        breakdown_fig.add_trace(go.Bar(
            x=top_candidates["name"],
            y=top_candidates["content_score"],
            name="Content-Based Score",
            marker_color="#3498db"
        ))
        breakdown_fig.add_trace(go.Bar(
            x=top_candidates["name"],
            y=top_candidates["collab_score"],
            name="Collaborative SVD Score",
            marker_color="#e67e22"
        ))
        breakdown_fig.add_trace(go.Scatter(
            x=top_candidates["name"],
            y=top_candidates["personalization_score"],
            name="Hybrid LightGBM Score",
            mode="lines+markers",
            marker=dict(size=8, color="#2ecc71"),
            line=dict(width=3)
        ))
        breakdown_fig.update_layout(
            title="Score Component Breakdown for Top Candidate Places",
            xaxis_tickangle=-45,
            yaxis_title="Normalized Score [0, 1]",
            barmode="group",
            height=380,
            margin=dict(l=20, r=20, t=40, b=80),
            template="plotly_white"
        )
        st.plotly_chart(breakdown_fig, use_container_width=True)

    st.markdown("##### 🧠 Global Model Feature Importance")
    if recommender.model is not None:
        importances = recommender.model.feature_importances_
        imp_df = pd.DataFrame({
            "Feature": [FEATURE_COLUMNS[i] for i in range(len(FEATURE_COLUMNS))],
            "Importance": importances
        }).sort_values(by="Importance", ascending=True)

        fig_imp = px.bar(
            imp_df,
            x="Importance",
            y="Feature",
            orientation="h",
            color="Importance",
            color_continuous_scale="Teal",
            title="LightGBM Global Feature Importance (Gain/Splits)",
            height=320
        )
        st.plotly_chart(fig_imp, use_container_width=True)


# ----------------------------------------------------
# TAB 5: EVALUATION BENCHMARKS
# ----------------------------------------------------
with tab5:
    st.subheader("Empirical Evaluation & Baseline Comparisons")
    st.write(
        "All metrics below were computed from the empirical offline evaluation suite (`src/evaluation/run_experiments.py`)."
    )

    t_ev1, t_ev2, t_ev3 = st.tabs(["Recommender Ablation", "Optimizer Benchmarks (10 Seeds)", "End-to-End Satisfaction"])

    with t_ev1:
        st.markdown("#### Recommender Ablation & Cold-Start Results")
        try:
            ab_df = pd.read_csv("results/tables/recommender_ablation.csv")
            st.dataframe(ab_df, use_container_width=True)
            st.image("results/figures/fig1_recommender_ablation.png", caption="Recommender Ablation: RMSE & NDCG@10")
        except Exception as e:
            st.warning(f"Results table loading: {e}")

    with t_ev2:
        st.markdown("#### Multi-Objective Optimizer 10-Seed Benchmarks")
        try:
            opt_bench_df = pd.read_csv("results/tables/optimizer_benchmark.csv")
            st.dataframe(opt_bench_df, use_container_width=True)
            st.image("results/figures/fig2_hypervolume_comparison.png", caption="Hypervolume Indicator across 10 Seeds")
        except Exception as e:
            st.warning(f"Optimizer benchmark loading: {e}")

    with t_ev3:
        st.markdown("#### End-to-End Simulated User Satisfaction")
        try:
            sat_bench_df = pd.read_csv("results/tables/end_to_end_satisfaction.csv")
            st.dataframe(sat_bench_df, use_container_width=True)
            st.image("results/figures/fig3_end_to_end_satisfaction.png", caption="User Satisfaction across 20 Travelers")
        except Exception as e:
            st.warning(f"Satisfaction table loading: {e}")


# ----------------------------------------------------
# TAB 6: SIDE-BY-SIDE COMPARE
# ----------------------------------------------------
with tab6:
    st.subheader("Side-by-Side Itinerary Comparison")
    st.write("Compare two distinct Pareto solutions or trade-offs:")

    col_cmp1, col_cmp2 = st.columns(2)
    with col_cmp1:
        idx_a = st.selectbox("Plan A", range(len(pareto_sols)), index=0, format_func=lambda i: f"Plan #{i+1} {'(⭐ Knee)' if i == opt_res.knee_index else ''}", key="cmp_a")
    with col_cmp2:
        default_b = min(1, len(pareto_sols) - 1)
        idx_b = st.selectbox("Plan B", range(len(pareto_sols)), index=default_b, format_func=lambda i: f"Plan #{i+1} {'(⭐ Knee)' if i == opt_res.knee_index else ''}", key="cmp_b")

    sol_a = pareto_sols[idx_a]
    sol_b = pareto_sols[idx_b]

    # Metrics comparison table
    comp_metrics = pd.DataFrame([
        {
            "Metric": "Personalization Score",
            "Plan A": f"{sol_a.total_personalization_score:.2f}",
            "Plan B": f"{sol_b.total_personalization_score:.2f}",
            "Winner": "Plan A" if sol_a.total_personalization_score > sol_b.total_personalization_score else "Plan B",
        },
        {
            "Metric": "Total Cost (INR)",
            "Plan A": f"₹{sol_a.total_cost:,.0f}",
            "Plan B": f"₹{sol_b.total_cost:,.0f}",
            "Winner": "Plan A" if sol_a.total_cost < sol_b.total_cost else "Plan B",
        },
        {
            "Metric": "Total Travel Time",
            "Plan A": f"{int(sol_a.total_travel_time)} min",
            "Plan B": f"{int(sol_b.total_travel_time)} min",
            "Winner": "Plan A" if sol_a.total_travel_time < sol_b.total_travel_time else "Plan B",
        },
        {
            "Metric": "Category Diversity (Entropy)",
            "Plan A": f"{sol_a.category_diversity:.2f}",
            "Plan B": f"{sol_b.category_diversity:.2f}",
            "Winner": "Plan A" if sol_a.category_diversity > sol_b.category_diversity else "Plan B",
        },
        {
            "Metric": "Avg Crowd Factor",
            "Plan A": f"{sol_a.avg_crowd_level:.2f}",
            "Plan B": f"{sol_b.avg_crowd_level:.2f}",
            "Winner": "Plan A" if sol_a.avg_crowd_level < sol_b.avg_crowd_level else "Plan B",
        },
    ])
    st.dataframe(comp_metrics, use_container_width=True)

    # Detailed stop comparison
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"#### Stops in Plan A (#{idx_a+1})")
        for d in sol_a.days:
            st.markdown(f"**Day {d.day_number}** ({len(d.stops)} stops)")
            for s in d.stops:
                st.write(f"- {s.place_name} ({s.category}) | ₹{s.cost_inr:.0f}")

    with col_p2:
        st.markdown(f"#### Stops in Plan B (#{idx_b+1})")
        for d in sol_b.days:
            st.markdown(f"**Day {d.day_number}** ({len(d.stops)} stops)")
            for s in d.stops:
                st.write(f"- {s.place_name} ({s.category}) | ₹{s.cost_inr:.0f}")


# FOOTER (Mandatory Synthetic Data Notice)
st.markdown("""
<div class="footer-text">
    ⚠️ <b>DATASET NOTICE:</b> All tourist places, user latent profiles, and interaction ratings utilized in this project are 
    <b>SYNTHETIC</b>, engineered with realistic geospatial distributions across South India (Tamil Nadu, Kerala, Karnataka) for academic evaluation. 
    Plug-and-play real datasets (OpenTripMap, Foursquare, Kaggle) are supported via <code>data/real_data_adapter.py</code>.
    <br><br>
    Built with <b>Streamlit</b>, <b>Pymoo (NSGA-II)</b>, <b>LightGBM</b>, <b>SHAP</b>, and <b>Folium</b>.
</div>
""", unsafe_allow_html=True)

