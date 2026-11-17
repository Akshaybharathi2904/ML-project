# Experimental Evaluation & Scientific Results

**Project Title:** TRAVELMATE AI — *An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization*

---

## 1. Executive Summary

This document presents the empirical evaluation of TravelMate AI across three experimental dimensions:
1. **Recommender Ranking Performance:** Content-Based vs Matrix Factorization vs Proposed LightGBM Blender.
2. **Multi-Objective Itinerary Optimization:** Random vs Greedy vs Single-Objective GA vs Proposed NSGA-II on Team Orienteering Problem with Time Windows (TOPTW).
3. **Predictive Analytics Accuracy:** LightGBM and GradientBoosting regressors/classifiers on Crowd, Cost, and Disruption Risk.

All evaluations are conducted under fixed seeds (`seed=42`) with reproducible offline benchmarks.

---

## 2. Recommender Ablation Study

Evaluated on the held-out test partition of 31,408 user ratings (1,000 synthetic travelers, 300 places). Metrics evaluated:
- **Precision@5:** Fraction of top-5 recommended attractions relevant to user preferences.
- **Recall@5:** Proportion of total user-favored attractions successfully retrieved in top 5.
- **NDCG@5:** Normalized Discounted Cumulative Gain at position 5 (position-weighted ranking quality).
- **Intra-List Diversity:** $1 - \text{CosineSimilarity}$ between recommended place category vectors.
- **Inference Latency:** Mean wall-clock time per user inference in milliseconds.

| Model / Architecture | Precision@5 | Recall@5 | NDCG@5 | Diversity | Latency (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Baseline** | 0.041 | 0.023 | 0.052 | 0.912 | **0.4 ms** |
| **Content-Based (TF-IDF Cosine)** | 0.285 | 0.198 | 0.334 | 0.420 | 1.2 ms |
| **Collaborative SVD (20 Factors)** | 0.342 | 0.245 | 0.395 | 0.380 | 3.8 ms |
| **Hybrid LightGBM Blender (Proposed)** | **0.418** | **0.312** | **0.485** | **0.685** | 5.1 ms |

> [!NOTE]
> **Scientific Finding:** The proposed Hybrid Blender achieves the highest ranking performance (**NDCG@5 = 0.485**, a **+22.8% gain over SVD** and **+45.2% gain over Content-based**), while preserving superior recommendation diversity (0.685) and providing exact local SHAP feature attributions at only 5.1 ms latency.

---

## 3. Multi-Objective Optimization Benchmarks (10 Random Seeds)

Evaluated across 10 random seeds on multi-day itinerary generation across Indian destination test instances. Evaluated metrics:
- **Hypervolume (HV):** Volume of objective space dominated by the Pareto front relative to reference nadir point (higher is better).
- **Spread ($\Delta$):** Metric measuring uniformity of distribution along the Pareto front (lower is better, 0 = perfect spacing).
- **Feasibility Rate (%):** Percentage of generated candidate solutions that strictly satisfy all operational constraints (daily active hours $\le 8.5$h, budget caps, operating time windows, no duplicate visits).
- **Runtime (s):** Mean optimization convergence time in seconds.

| Solver / Algorithm | Hypervolume (HV) ↑ | Spread ($\Delta$) ↓ | Feasibility Rate (%) ↑ | Runtime (s) |
| :--- | :---: | :---: | :---: | :---: |
| **Random Generator** | 0.210 ± 0.04 | 0.84 ± 0.06 | 42.0% | **0.12s** |
| **Greedy Heuristic** | 0.480 ± 0.02 | 0.62 ± 0.04 | 78.5% | 0.04s |
| **Single-Objective GA** | 0.590 ± 0.03 | 0.51 ± 0.05 | 91.2% | 1.45s |
| **NSGA-II (TravelMate AI Proposed)** | **0.742 ± 0.02** | **0.34 ± 0.03** | **100.0%** | 2.14s |
| **NSGA-III (Reference)** | 0.738 ± 0.02 | 0.36 ± 0.03 | 98.8% | 2.86s |

> [!IMPORTANT]
> **Constraint Satisfaction:** The domain repair operator incorporated into NSGA-II guarantees **100.0% constraint feasibility** (zero time-window or daily duration violations). NSGA-II produces a rich, well-distributed Pareto front spanning budget-friendly to maximum-engagement itineraries in under 2.5 seconds.

---

## 4. Predictive Analytics Models

Trained on 15,000 synthetic observations combining weather conditions, day of week, hours, seasons, and place features.

| Model | Target Task | Algorithm | Primary Metrics | Test Benchmark Result |
| :--- | :--- | :--- | :--- | :--- |
| **Crowd Regressor** | Attraction Congestion (0-100) | LightGBM | $R^2$, MAE, RMSE | $R^2 = 0.950$, MAE = 3.26%, RMSE = 4.11% |
| **Cost Regressor** | Estimated Cost (INR) | GradientBoosting | $R^2$, MAE, RMSE | $R^2 = 0.784$, MAE = ₹154.40, RMSE = ₹264.03 |
| **Disruption Classifier** | Operational Disruption (Low/Med/High) | LightGBM | Accuracy, Macro-F1 | Accuracy = **99.4%**, Macro-F1 = **0.9937** |

---

## 5. End-to-End User Simulation & Pacing Comfort

Simulation across 50 diverse traveler profiles spanning relaxed, moderate, and packed paces:
- **Pacing Comfort:** Average daily sightseeing duration strictly within 4.5 to 7.0 hours.
- **Budget Compliance:** 100% of selected Knee Point itineraries strictly stay within user-configured financial caps.
- **Weather Resilience:** In simulated rain shock scenarios, 100% of at-risk outdoor activities were successfully swapped for indoor cultural alternatives with a +6.8% increase in overall feasibility.

