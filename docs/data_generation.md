# Synthetic Data Generation & Data Adapter Specification

**Project Title:** TRAVELMATE AI — *An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization*

---

## 1. Academic Disclaimer & Synthetic Labeling

> [!IMPORTANT]
> **Synthetic Data Disclosure**: In compliance with rigorous research reporting standards, all datasets located in `data/` (`places.csv`, `users.csv`, `ratings.csv`, `distance_matrix.csv`, `travel_time_matrix.csv`, and mock catalogs) are **SYNTHETIC BENCHMARKS** generated deterministically using seed `42`. They simulate realistic tourist behavioral patterns, spatial distributions, crowd dynamics, and seasonal factors across India.
>
> A production-grade adapter is provided in `data/real_data_adapter.py` that allows immediate ingestion of real-world datasets (OpenTripMap, Foursquare, Kaggle, or state tourism boards) without changing any machine learning or optimization code.

---

## 2. Generative Methodology

### A. Places Dataset (`data/places.csv`)
- **Total Entities:** 300 tourist destinations and attractions across South and North India.
- **Regions:** Tamil Nadu, Kerala, Karnataka, Rajasthan, Goa, Uttar Pradesh.
- **Attributes:**
  - `id`: Unique identifier (`PLC_0001` to `PLC_0300`).
  - `name`: Attraction name (e.g., *City Palace*, *Meenakshi Amman Temple*, *Periyar Wildlife Sanctuary*).
  - `city`: Host city / destination.
  - `lat`, `lon`: True or clustered geospatial coordinates.
  - `category`: Heritage, Nature, Temple, Adventure, Food, Shopping, Museum, Wildlife, Hill Station, Beach.
  - `avg_cost_inr`: Uniformly sampled entry fee & activity cost (₹0 to ₹1,800).
  - `avg_visit_duration_min`: Realistic duration bounds based on category (30 mins to 240 mins).
  - `rating`: Base historical rating on [1.0, 5.0] scale drawn from $\mathcal{N}(4.2, 0.4)$ truncated at 3.0 and 5.0.
  - `popularity`: Frequency percentile rank in $[0.05, 1.0]$.
  - `crowd_level`: Baseline tourist congestion factor $[0.1, 1.0]$.
  - `open_time`, `close_time`: Operating hours (e.g., `09:00` to `18:00`).
  - `best_season`: Winter, Monsoon, Summer, All-Year.
  - `tags`: Semicolon-delimited descriptive semantic tags (e.g., `palace; royal; mewar; architecture`).

### B. User Profiles (`data/users.csv`)
- **Total Users:** 1,000 synthetic travelers.
- **Attributes:**
  - `user_id`: `USR_0001` to `USR_1000`.
  - `latent_preferences`: 10-dimensional category affinity vector generated via Dirichlet distribution $\text{Dir}(\alpha)$ ensuring natural interest clustering (e.g., history buffs, wildlife enthusiasts, foodies).
  - `budget_tier`: `budget`, `medium`, `luxury`.
  - `pace`: `relaxed` (2-3 stops/day), `moderate` (3-4 stops/day), `packed` (5-6 stops/day).

### C. Ratings Interaction Matrix (`data/ratings.csv`)
- **Total Observations:** 31,408 user-item ratings.
- **Interaction Model:**
  $$\text{Rating}_{u, p} = 1.0 + 4.0 \cdot \left( 0.50 \cdot (\mathbf{u}_{\text{pref}} \cdot \mathbf{p}_{\text{cat}}) + 0.25 \cdot \text{Popularity}_p + 0.15 \cdot \text{Rating}_p + \epsilon \right)$$
  where $\epsilon \sim \mathcal{N}(0, 0.12)$ represents observational noise.
- **Sparsity:** Realistic density of ~10.4% with power-law distribution over popular items.
- **Cold-Start Partition:** 100 dedicated new users with $\le 2$ ratings to evaluate cold-start blending dynamics.

### D. Spatial Distance & Travel Time Matrices
- **Distance Matrix (`data/distance_matrix.csv`):** Pairwise Haversine great-circle distance:
  $$d = 2 R \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)}\right)$$
- **Travel Time Matrix (`data/travel_time_matrix.csv`):** Modeled using an urban road tortuosity factor $\tau = 1.35$ and average urban velocity $v = 32\text{ km/h}$, with a fixed 5-minute parking/transit buffer:
  $$t_{\text{transit}} = \left( \frac{d \cdot 1.35}{32} \times 60 \right) + 5 \text{ minutes}$$

---

## 3. Real Data Adapter (`data/real_data_adapter.py`)

The real data adapter decouples external datasets from the downstream machine learning models and optimization solvers.

### Ingestion Interface:
```python
from data.real_data_adapter import RealDataAdapter

# Ingest external OpenTripMap or Kaggle CSV
adapter = RealDataAdapter()
df_places = adapter.load_and_validate_places("path/to/raw_places.csv")
df_ratings = adapter.load_and_validate_ratings("path/to/raw_ratings.csv")

# Computes distance & travel time matrices automatically
distance_matrix, travel_time_matrix = adapter.build_spatial_matrices(df_places)
```

### Validation Guarantees:
1. **Schema Integrity:** Verifies required fields (`id`, `name`, `lat`, `lon`, `category`, `avg_cost_inr`, `avg_visit_duration_min`, `open_time`, `close_time`).
2. **Boundary Validation:** Asserts coordinates fall within Indian bounding box (or configured geography) and hours follow `HH:MM` 24h format.
3. **Missing Value Imputation:** Imputes missing duration by category medians and missing costs by regional baselines.

