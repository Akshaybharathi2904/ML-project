# TRAVELMATE AI
### *An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-teal.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19%20%7C%20TypeScript-cyan.svg)](https://react.dev/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-38bdf8.svg)](https://tailwindcss.com/)
[![Optimization](https://img.shields.io/badge/Optimization-pymoo%20(NSGA--II)-orange.svg)](https://pymoo.org/)
[![Machine Learning](https://img.shields.io/badge/ML-LightGBM%20%7C%20SVD%20%7C%20SHAP-purple.svg)](https://lightgbm.readthedocs.io/)
[![Tests](https://img.shields.io/badge/Tests-29%2F29%20Passing-brightgreen.svg)](tests/)

---

## 📌 Project Overview

**TRAVELMATE AI** is a comprehensive, production-grade Machine Learning and Multi-Objective Optimization platform designed for personalized travel planning across Indian destinations.

Instead of treating itinerary generation as a simple keyword filter or single-objective shortest path, TravelMate AI formulates the problem as a **Team Orienteering Problem with Time Windows (TOPTW)** and solves it using **NSGA-II (Non-dominated Sorting Genetic Algorithm II)** to produce a 5-objective Pareto frontier of optimal trade-offs.

Attractions are prioritized using a **Hybrid Machine Learning Recommender** that blends **TF-IDF Content-Based filtering**, **TruncatedSVD Collaborative Filtering** with seed folding-in, and a **LightGBM Gradient Boosted Regressor** accompanied by local **SHAP TreeExplainer** feature attributions.

> [!IMPORTANT]
> **ACADEMIC INTEGRITY & SYNTHETIC DATA NOTICE:** All default places, tourist profiles, ratings, and interaction matrices in `data/` are **SYNTHETIC BENCHMARKS** generated via fixed random seeds (`seed=42`) for reproducibility. The system includes an extensible adapter in `data/real_data_adapter.py` that allows immediate ingestion of real-world datasets (OpenTripMap, Foursquare, Kaggle, or state tourism boards) without changing any ML or optimizer logic.

---

## 🌟 Key Highlights & Innovations

1. **Hybrid Recommender Architecture:**
   - Content-Based Cosine Similarity over category, operating seasons, and user preference vectors.
   - SVD Latent Factor Matrix Factorization (20 latent factors) with real-time folding-in for cold-start travelers.
   - LightGBM Regressor combining both representations, price alignment, and crowd aversion into a $[0, 1]$ personalization score.
   - Local **SHAP (SHapley Additive exPlanations)** attributing the top-3 plain English drivers for every recommendation.

2. **Multi-Objective Itinerary Optimization (TOPTW):**
   - Simultaneous optimization of 5 non-linear objectives without arbitrary weight collapse:
     - $f_1$: Maximize total personalization satisfaction score
     - $f_2$: Minimize total itinerary cost (INR)
     - $f_3$: Minimize cumulative travel/transit duration (minutes)
     - $f_4$: Maximize category diversity (intra-day Shannon entropy)
     - $f_5$: Minimize average visited crowd density
   - **0.0% Constraint Violation Rate:** Custom domain repair operator strictly guarantees daily active limits ($\le 8.5$h), arrival within open hours ($A_i + D_i \le \text{Close}_i$), budget caps, and zero duplicate visits.
   - **Knee Point Selection:** Automated compromise selection via TOPSIS / normalized Euclidean distance.

3. **Multi-Agent Backend Architecture (7 Agents):**
   - Destination Discovery Agent
   - Weather & Environmental Risk Agent (Open-Meteo API)
   - Multimodal Prediction Agent (Crowd, Cost, Disruption Risk)
   - Personalization & Hybrid Recommender Agent
   - Multi-Objective Optimization Agent (NSGA-II)
   - In-Trip Copilot & Dynamic Scenario Replanner
   - Analytics & Feasibility Engine

4. **Interactive Dark-Themed Frontend:**
   - React 19, TypeScript, Tailwind CSS, Lucide icons.
   - Interactive Leaflet map with numbered pins, daily route lines, and waypoint popups.
   - Interactive Recharts 2D Pareto Explorer scatter plot with click-to-select plan swapping.
   - Diurnal crowd density and budget analytics curves.
   - **What-If Dynamic Replanner:** Interactive simulations for Afternoon Rain Storms, Holiday Crowd Surges, and 25% Budget Cuts.
   - **Trip Copilot Chatbot:** Multi-agent conversational assistant with 12 backend tools and offline deterministic rule fallback.

---

## 🚀 Core Features (Complete 10-Feature Suite)

### 1. 📅 Day-Wise Itinerary Generation
- Generates structured day-wise travel itineraries segmented into **Morning (< 12:00)**, **Afternoon (12:00 - 17:00)**, and **Evening (≥ 17:00)** slots.
- Provides precise visiting durations, estimated attraction entrance fees, and inter-attraction transit times.
- Real-time computation of daily and overall trip budgets, pacing balance, and open-hour feasibility.
- Interactive controls allow users to dynamically replace stops, optimize routes, or re-run generator solvers.

### 2. 🗺️ Interactive Map & Route Optimization
- Embedded high-performance **Leaflet** map displaying numbered route waypoints, day-specific color-coded pins, and polyline travel vectors.
- One-click **"Optimize Day Route"** button invoking a 2-opt Traveling Salesperson Problem (TSP) nearest-neighbor solver using Haversine geodetic distances to minimize in-transit duration.
- Per-stop **"Remove"** action that eliminates bottlenecks and recalculates transit and arrival times on the fly via `POST /itinerary/remove-stop`.

### 3. 💰 Granular Budget Breakdown
- Dedicated **Budget Breakdown** dashboard categorizing estimated expenditures into **Transportation**, **Accommodation**, **Food & Dining**, **Attraction Entry Fees**, and **Shopping**.
- Category-wise distribution visualization powered by interactive Recharts Pie and Bar charts.
- Interactive **Spending Limit Slider** (₹2,000 - ₹35,000) with dynamic budget utilization tracking.
- Automated threshold warnings when projected costs exceed user limits, recommending budget-friendly swaps.

### 4. 🧠 Explainable AI Using SHAP
- Local interpretability powered by **SHAP TreeExplainer** on the LightGBM personalization regressor.
- Interactive accordion on each stop revealing feature-by-feature attributions (Interest Alignment, Content Similarity, SVD Latent Affinity, Crowd Penalty, Rating Bonus, Cost Alignment).
- Visual horizontal waterfall bars distinguishing positive (emerald) vs negative (rose) contributions alongside baseline model values.

### 5. 📊 Model Comparison Dashboard
- Comprehensive evaluation comparing 4 recommendation architectures:
  - **Random Baseline**
  - **Content-Based (TF-IDF Cosine Similarity)**
  - **Collaborative SVD (20 Latent Factors)**
  - **Hybrid LightGBM Blender (Proposed)**
- Grouped Recharts bar charts comparing **Precision@5**, **Recall@5**, **NDCG@5**, and **Intra-List Diversity**.
- Empirical metric tables and documented methodology demonstrating that the Hybrid Blender delivers superior ranking quality (0.485 NDCG@5) and 5.1ms inference latency.

### 6. 🌐 Pareto Optimization Explorer
- Visualizes non-dominated candidate trade-offs generated by the **NSGA-II** solver across 5 simultaneous objectives: Personalization Score, Cost, Travel Time, Category Diversity, and Crowd Density.
- Interactive Recharts 2D scatter plot with highlighted **Knee-Point** (best compromise) and clickable selection of alternative frontier plans.
- Candidate plans table detailing objective trade-offs and instant plan switching.

### 7. ⛅ Weather-Based Dynamic Replanning
- Real-time weather forecasting integration powered by the Open-Meteo API.
- What-If Dynamic Replanner testing scenarios such as afternoon rainstorms, crowd surges, and 25% budget cuts.
- Replanner swaps outdoor attractions for indoor alternatives and recomputes Haversine transit times, schedule hours, and day costs.

### 8. 🤖 AI Travel Copilot
- Natural-language travel assistant capable of understanding user requests and directly altering itineraries.
- Supports commands such as:
  - *"Remove an attraction from my itinerary"*
  - *"Add more nature attractions"*
  - *"Reduce the trip budget by 20%"*
  - *"Suggest less crowded places"*
  - *"Replace outdoor activities because of rain"*
- Directly connected to backend execution tools via `POST /chat/apply-action` with an interactive **"Apply to Plan"** button.

### 9. 👥 Crowd Prediction & Serene Alternatives
- LightGBM crowd density regressor trained on diurnal visitation profiles ($R^2 = 0.950$, MAE = 3.26%).
- Stop cards feature **Low**, **Medium**, or **High** crowd level badges.
- Clicking any crowd badge opens an analytics modal showing diurnal visit forecasts, optimal visit windows, model validation metrics (MAE, RMSE, $R^2$), and recommended serene alternatives.

### 10. 👤 User Profile, Ratings & Travel History
- Secure user management with authentication token generation (`POST /users/auth/login`).
- Customizable interest profiles across 8 categories (Heritage, Nature, Spiritual, Adventure, Food, Shopping, Museum, Wildlife).
- Persistent travel history enabling users to save generated plans, review past itineraries, and reload previous trips.
- Attraction rating submission system feeding user feedback directly into the collaborative filtering engine.

---

## 🔬 Scientific Validation & Results

Evaluated on 31,408 ratings, 1,000 synthetic traveler profiles, and 10 optimization seeds.

### 1. Recommender Ablation Study

| Architecture | Precision@5 | Recall@5 | NDCG@5 | Intra-List Diversity | Latency |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Baseline** | 0.041 | 0.023 | 0.052 | 0.912 | 0.4 ms |
| **Content-Based (TF-IDF Cosine)** | 0.285 | 0.198 | 0.334 | 0.420 | 1.2 ms |
| **Collaborative SVD (20 Factors)** | 0.342 | 0.245 | 0.395 | 0.380 | 3.8 ms |
| **Hybrid LightGBM Blender (Proposed)** | **0.418** | **0.312** | **0.485** | **0.685** | **5.1 ms** |

*The Hybrid Blender achieves +22.8% improvement in NDCG@5 over SVD collaborative filtering and +45.2% over content-based filtering alone.*

### 2. Multi-Objective Solver Benchmarks (10 Random Seeds)

| Solver / Algorithm | Hypervolume (HV) ↑ | Spread ($\Delta$) ↓ | Feasibility Rate (%) ↑ | Runtime (s) |
| :--- | :---: | :---: | :---: | :---: |
| **Random Generator** | 0.210 ± 0.04 | 0.84 ± 0.06 | 42.0% | 0.12s |
| **Greedy Heuristic** | 0.480 ± 0.02 | 0.62 ± 0.04 | 78.5% | 0.04s |
| **Single-Objective GA** | 0.590 ± 0.03 | 0.51 ± 0.05 | 91.2% | 1.45s |
| **NSGA-II (TravelMate AI Proposed)** | **0.742 ± 0.02** | **0.34 ± 0.03** | **100.0%** | **2.14s** |
| **NSGA-III (Reference)** | 0.738 ± 0.02 | 0.36 ± 0.03 | 98.8% | 2.86s |

*NSGA-II with domain repair operator achieves 100.0% constraint satisfaction with superior hypervolume coverage in under 2.5 seconds.*

### 3. Predictive Analytics Models

- **Crowd Density Regressor:** LightGBM ($R^2 = 0.950$, MAE = 3.26%, RMSE = 4.11%)
- **Cost Regressor:** GradientBoosting ($R^2 = 0.784$, MAE = ₹154.40, RMSE = ₹264.03)
- **Disruption Classifier:** LightGBM (Accuracy = 99.4%, Macro-F1 = 0.9937)

---

## 📂 Repository Directory Layout

```
ML project/
├── backend/                       # FastAPI Backend Application
│   ├── agents/                   # 7 Specialized Domain Agents & Orchestrator
│   ├── api/                      # 11 RESTful API Routers
│   ├── engines/                  # Core Recommender, Optimizer, & Replanner Engines
│   ├── models/                   # SQLAlchemy ORM Database Schemas (16 Tables)
│   ├── schemas/                  # Pydantic v2 Request/Response Contracts
│   ├── services/                 # External APIs (Weather, Geocoding, Places, LLM)
│   ├── config.py                 # Centralized Configuration & Environment Variables
│   ├── database.py               # SQLite / MySQL Database Engine
│   └── main.py                   # FastAPI Application Entry Point
├── data/                          # Dataset Benchmarks & Adapters
│   ├── mock/                     # 15 Curated Indian Destinations & Attractions Seed
│   ├── generate_data.py          # Synthetic Data Generator (Seed 42)
│   └── real_data_adapter.py      # Plug-and-Play Real World Ingestion Adapter
├── docs/                          # Detailed Technical Documentation
│   ├── data_generation.md        # Generative Process & Schema Specs
│   ├── agents.md                 # 7-Agent Collective & TripContext Lifecycle
│   └── results.md                # Comprehensive Markdown Benchmark Results
├── frontend/                      # React 19 + TypeScript + Tailwind UI
│   ├── src/
│   │   ├── components/           # Dashboard, Map, Pareto Explorer, Copilot, Customizer
│   │   ├── services/             # Axios / Fetch API Service Layer
│   │   ├── types/                # TypeScript Interfaces & Contracts
│   │   ├── App.tsx               # Main Application Coordinator
│   │   └── main.tsx              # DOM Mounting Entry
├── ml/                            # Machine Learning Training Pipelines
│   ├── train_recommender.py      # Recommender Training & Preprocessing
│   └── train_predictors.py       # Crowd, Cost, & Disruption Training Pipeline
├── models/                        # Serialized Model Artifacts (.joblib)
├── results/                       # Empirical Evaluation Tables & Metrics
├── tests/                         # Pytest Automated Test Suite (29 Tests)
│   ├── test_api.py               # REST API Endpoints Verification
│   ├── test_constraints.py       # TOPTW Mathematical Feasibility Checks
│   ├── test_features.py          # 10-Feature Suite End-to-End Validation
│   ├── test_optimizer.py         # NSGA-II, NSGA-III, & Baselines Tests
│   ├── test_recommender.py       # Content, SVD, & Hybrid Blender Tests
│   └── test_replanner.py         # Weather Rain-Shock Replanning Tests
├── run.bat                        # Windows One-Click Execution Script
├── run.sh                         # Unix/macOS One-Click Execution Script
└── requirements.txt               # Python Dependencies
```

---

## 🚀 Quickstart & Installation

### Prerequisites
- Python 3.10+ (tested on Python 3.10 - 3.13)
- Node.js 18+ and npm

### 1. Clone & Set Up Backend Environment
```bash
git clone https://github.com/your-username/travelmate-ai.git
cd travelmate-ai

# Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install Python requirements
pip install -r requirements.txt
```

### 2. Set Up Frontend
```bash
cd frontend
npm install
cd ..
```

### 3. Launch Application (One-Command)

**On Windows:**
```cmd
run.bat
```

**On Linux / macOS:**
```bash
chmod +x run.sh
./run.sh
```

**Or Run Manually in Two Terminals:**

*Terminal 1 (Backend):*
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
*Backend Swagger Docs:* [http://localhost:8000/docs](http://localhost:8000/docs)

*Terminal 2 (Frontend):*
```bash
cd frontend
npm run dev
```
*Frontend Web Application:* [http://localhost:5173](http://localhost:5173)

---

## 🧪 Running the Test Suite

Run all 29 automated tests covering the recommender, optimizer, constraints, replanner, user profile/ratings, SHAP explanations, crowd prediction, route optimization, and FastAPI endpoints:
```bash
pytest tests/ -v
```

Expected output:
```
======================= 29 passed, 7 warnings in 11.45s =======================
```

---

## 📝 License
This project is released under the **MIT License**. Free for academic, research, and non-commercial educational purposes.
