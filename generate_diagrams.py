import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

fig_dir = r"d:\ML project\REPORT"
os.makedirs(fig_dir, exist_ok=True)

# 1. Architecture Diagram
fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title
ax.text(50, 96, "TRAVELMATE AI - Multi-Agent System Architecture", fontsize=16, fontweight='bold', ha='center', color='#0f172a')

# Boxes styling
def draw_box(x, y, w, h, title, items, bg_color='#f8fafc', border_color='#0284c7'):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.5", ec=border_color, fc=bg_color, lw=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 4, title, fontsize=12, fontweight='bold', ha='center', color='#0f172a')
    for idx, item in enumerate(items):
        ax.text(x + 4, y + h - 9 - (idx * 3.8), f"• {item}", fontsize=9.5, color='#334155')

# Layer 1: Client UI Layer
draw_box(5, 78, 90, 14, "Layer 1: Interactive Client UI & Presentation (React 19 + TypeScript + Tailwind)", [
    "Trip Customization Engine (Duration, Budget, Pace, Cold-Start Star Ratings)",
    "Pareto Front Explorer (2D Interactive Recharts Trade-Off Scatter Plot & Knee Point)",
    "Day-by-Day Timeline & Leaflet Route Map (Numbered Waypoints & Transit Legs)",
    "Trip Copilot Conversational Assistant & What-If Scenario Replanner Panel"
], bg_color='#f0fdf4', border_color='#16a34a')

# Layer 2: API Gateway & Orchestrator
draw_box(5, 59, 90, 14, "Layer 2: FastAPI Gateway & TripContext Orchestrator (Python 3.10+)", [
    "Asynchronous REST API Endpoints (Destinations, Places, Weather, Predictions, Optimizer, Chat)",
    "Immutable TripContext Pipeline State Coordinator & Session Memory Manager",
    "Pydantic v2 Request/Response Validation & OpenAPI Automated Documentation",
    "Rule-Based Intent Routing & LLM Fallback Integration (Gemini 1.5 / Groq)"
], bg_color='#eff6ff', border_color='#2563eb')

# Layer 3: Recommender & Predictive Core
draw_box(5, 38, 43, 17, "Layer 3A: Hybrid ML Recommender", [
    "TF-IDF Content Similarity over Tags & Categories",
    "SVD Collaborative Filtering (20 Latent Factors)",
    "Cold-Start Folding-In Seed Projection",
    "LightGBM GBDT Blender ([0, 1] Match Score)",
    "SHAP TreeExplainer Local Attribution Cards"
], bg_color='#fdf4ff', border_color='#9333ea')

draw_box(52, 38, 43, 17, "Layer 3B: Predictive Analytics Engine", [
    "LightGBM Crowd Density Regressor (R² = 0.950)",
    "GradientBoosting Cost Estimator (R² = 0.784)",
    "LightGBM Disruption Classifier (Acc = 99.4%)",
    "Open-Meteo Weather Suitability Scoring",
    "Composite Trip Feasibility KPI Formula"
], bg_color='#fffbeb', border_color='#d97706')

# Layer 4: Multi-Objective Optimizer & Dynamic Replanner
draw_box(5, 17, 90, 17, "Layer 4: Multi-Objective Optimizer & Dynamic Scenario Replanner", [
    "Team Orienteering Problem with Time Windows (TOPTW) Mathematical Formulation",
    "NSGA-II Genetic Solver (35 Population, 30 Generations, Evaluated over 5 Objectives)",
    "Domain Repair Operator (Strict Enforcement of Time Windows, Budget Caps, and Pace Limits)",
    "Automated Knee Point Selection via TOPSIS / Normalized Euclidean Distance",
    "Dynamic Replanning Engine for Weather Rain Shocks, Crowd Surges, and Budget Reductions"
], bg_color='#f0fdfa', border_color='#0d9488')

# Layer 5: Data & Storage Layer
draw_box(5, 2, 90, 11, "Layer 5: Data Ingestion & Persistence Layer", [
    "Synthetic Benchmark Catalogs (300 Places, 1,000 Users, 31,408 Ratings across 15 Cities)",
    "Spatial Distance & Transit Matrices (Haversine Distance + 35 km/h Urban Velocity Model)",
    "SQLAlchemy ORM Database (16 Tables supporting SQLite / MySQL 8.0)",
    "Real Data Ingestion Adapter (OpenTripMap, Foursquare, Kaggle API Compatible)"
], bg_color='#f8fafc', border_color='#64748b')

plt.tight_layout()
arch_path = os.path.join(fig_dir, "travelmate_architecture.png")
plt.savefig(arch_path, bbox_inches='tight')
plt.close()
print("Saved:", arch_path)

# 2. Data Flow Diagram (DFD)
fig, ax = plt.subplots(figsize=(12, 10), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 96, "TRAVELMATE AI - Level-1 Data Flow Diagram (DFD)", fontsize=16, fontweight='bold', ha='center', color='#0f172a')

# Entities & Processes
def draw_process(x, y, r, p_num, p_title, bg='#f0fdfa', ec='#0d9488'):
    circle = patches.Circle((x, y), r, ec=ec, fc=bg, lw=2)
    ax.add_patch(circle)
    ax.text(x, y + 2, p_num, fontsize=11, fontweight='bold', ha='center', color='#0f172a')
    ax.text(x, y - 2.5, p_title, fontsize=8.5, ha='center', color='#1e293b')

def draw_entity(x, y, w, h, title, bg='#f1f5f9', ec='#334155'):
    rect = patches.Rectangle((x, y), w, h, ec=ec, fc=bg, lw=2)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, title, fontsize=11, fontweight='bold', ha='center', va='center', color='#0f172a')

def draw_datastore(x, y, w, h, ds_id, title):
    rect = patches.Rectangle((x, y), w, h, ec='#0284c7', fc='#f0f9ff', lw=1.5)
    ax.add_patch(rect)
    ax.plot([x, x+w], [y, y], color='#0284c7', lw=2)
    ax.plot([x, x+w], [y+h, y+h], color='#0284c7', lw=2)
    ax.text(x + 3, y + h/2, ds_id, fontsize=10, fontweight='bold', va='center', color='#0284c7')
    ax.text(x + 18, y + h/2, title, fontsize=9.5, va='center', color='#0f172a')

# External Entities
draw_entity(4, 76, 16, 10, "Traveler\n(User UI)")
draw_entity(4, 18, 16, 10, "External\nWeather API")

# Data Stores
draw_datastore(40, 84, 52, 6, "D1", "Destination & Places Catalog (300 POIs)")
draw_datastore(40, 52, 52, 6, "D2", "Distance & Travel Time Matrices")
draw_datastore(40, 20, 52, 6, "D3", "Trained ML Models & Scalers (.joblib)")
draw_datastore(40, 2, 52, 6, "D4", "Trip History & Pareto Versions DB")

# Processes
draw_process(32, 70, 7.5, "1.0", "Destination &\nPlace Ingestion")
draw_process(65, 70, 7.5, "2.0", "Hybrid ML\nScoring")
draw_process(82, 40, 7.5, "3.0", "NSGA-II TOPTW\nOptimization")
draw_process(32, 38, 7.5, "4.0", "Weather & Risk\nAssessment")
draw_process(55, 38, 7.5, "5.0", "Dynamic Replan\n& Copilot")

# Connecting lines & annotations
ax.annotate("", xy=(24.5, 70), xytext=(20, 76), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(17, 72, "Preferences", fontsize=8, color='#0284c7')

ax.annotate("", xy=(57.5, 70), xytext=(39.5, 70), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(44, 72, "Candidate POIs", fontsize=8, color='#0284c7')

ax.annotate("", xy=(82, 47.5), xytext=(72.5, 70), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(78, 60, "Personalized Scores", fontsize=8, color='#0284c7')

ax.annotate("", xy=(62.5, 38), xytext=(74.5, 40), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(64, 43, "Pareto Front", fontsize=8, color='#0284c7')

ax.annotate("", xy=(20, 26), xytext=(24.5, 38), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(14, 34, "Forecasts", fontsize=8, color='#0284c7')

ax.annotate("", xy=(12, 76), xytext=(47.5, 38), arrowprops=dict(arrowstyle="->", lw=1.5, color='#0284c7'))
ax.text(26, 52, "Synthesized Itinerary & Explanations", fontsize=8.5, fontweight='bold', color='#0f172a', rotation=38)

plt.tight_layout()
dfd_path = os.path.join(fig_dir, "travelmate_dfd.png")
plt.savefig(dfd_path, bbox_inches='tight')
plt.close()
print("Saved:", dfd_path)
