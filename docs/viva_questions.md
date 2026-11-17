# Viva Voce & Technical Defense Guide
## 25 Comprehensive Questions & High-Scoring Answers

---

### Q1: What is the core problem addressed by this project, and why is single-objective optimization insufficient?
**Answer:**
Standard travel planning problems are traditionally formulated as Orienteering Problems (OP) or Traveling Salesperson Problems (TSP) optimizing a single objective, such as maximizing tourist score or minimizing distance. However, in reality, travel decisions involve inherently conflicting criteria: maximizing personalization, minimizing financial cost, minimizing transit fatigue, maximizing theme diversity, and minimizing crowd density. 
Single-objective scalarization (e.g., $J = \sum w_i f_i$) suffers from three major flaws: (1) it forces the user to choose arbitrary weights *before* understanding the trade-off landscape, (2) it cannot find solutions on non-convex regions of the Pareto front, and (3) it outputs a single fragile itinerary. Our multi-objective approach returns a true Pareto optimal frontier of mutually non-dominated options, empowering the user to make informed trade-offs.

---

### Q2: What is the Team Orienteering Problem with Time Windows (TOPTW)?
**Answer:**
The Team Orienteering Problem (TOP) models a set of $D$ vehicles (or days) that must select and sequence a subset of candidate points of interest (POIs) to collect cumulative rewards within daily budget allowances. The Time Windows extension (TOPTW) introduces arrival intervals $[t_{\text{open}}, t_{\text{close}}]$ for each POI. It is an NP-hard combinatorial optimization problem combining the Knapsack Problem (selecting the most rewarding places) with the Vehicle Routing Problem with Time Windows (scheduling valid, cost-effective routes).

---

### Q3: Explain the hybrid recommender architecture. Why combine Content-Based and Collaborative Filtering?
**Answer:**
Content-based filtering relies on place features (categories, tags, cost bands) and cosine similarity to user interest vectors. While effective at cold-start scenarios, it suffers from over-specialization and cannot capture serendipity or latent tourist acclaim. 
Collaborative Filtering (TruncatedSVD) uncovers latent interaction patterns across users, capturing crowd consensus, but suffers from severe cold-start degradation on unseen users or places. 
Our LightGBM hybrid model fuses both signals alongside contextual trip constraints (proximity to starting city, seasonal match, budget tier compatibility). LightGBM learns the non-linear interaction terms and dynamic weight shifts between content and collaborative modalities.

---

### Q4: How does your system address the cold-start problem for a new user?
**Answer:**
We employ a two-level defense:
1. **Zero-rating cold start:** If a user has no prior interaction history, the system dynamically relies on the Content-Based engine derived from explicit category preferences and budget sliders.
2. **Interactive folding-in:** If a new user rates even 1 to 5 seed landmarks in the UI, the collaborative filtering module uses the SVD item basis matrix $\mathbf{V}_k$ to fold in a pseudo-latent vector: $\mathbf{u}_{\text{new}} = (\mathbf{r}_{\text{seed}} - \bar{r})\mathbf{V}_k \mathbf{\Sigma}_k^{-1}$. The LightGBM feature weights dynamically scale the collaborative contribution with $\alpha = \min(1.0, m/5)$.

---

### Q5: How is matrix factorization formulated in your collaborative filtering model?
**Answer:**
We employ mean-centered SVD. Let $\mathbf{R} \in \mathbb{R}^{U \times P}$ be the sparse rating matrix. We compute user biases $\mu_u$ and center the matrix: $\tilde{R}_{u, p} = R_{u, p} - \mu_u$, imputing unobserved entries with 0 (representing the user's neutral mean). TruncatedSVD factorizes $\tilde{\mathbf{R}} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$. The predicted rating is:
$$\hat{R}(u, p) = \mu_u + \mathbf{U}_k(u) \cdot (\mathbf{\Sigma}_k \mathbf{V}_k^T)(p)$$
This separates global user optimism/pessimism from latent category affinities.

---

### Q6: Why did you choose LightGBM over Deep Learning (e.g., NeuMF or Two-Tower Networks) for the hybrid ranker?
**Answer:**
1. **Data Efficiency & Sparsity:** Gradient Boosted Decision Trees (GBDTs) consistently outperform neural networks on heterogeneous tabular data featuring mixed categorical, continuous, and physical distance variables.
2. **Inference Latency:** LightGBM scores 300 places in less than 5 milliseconds, critical for responsive web interaction in Streamlit.
3. **Native Explainability:** TreeSHAP computes exact Shapley values in polynomial time $\mathcal{O}(T L D^2)$, whereas neural network explainers (like Integrated Gradients or KernelSHAP) require sampling approximations and significant compute overhead.

---

### Q7: How does SHAP work in this system, and how are explanations generated?
**Answer:**
SHAP (SHapley Additive exPlanations) is based on cooperative game theory. It calculates the unique marginal contribution $\phi_j$ of each feature to the difference between the model's prediction $f(\mathbf{x})$ and the expected baseline prediction $\mathbb{E}[f(\mathbf{x})]$. 
In `src/recommender/explain.py`, TreeExplainer calculates $\phi_j$ for all 11 features per recommendation. The top 3 positive contributors are mapped to human-readable narratives (e.g., high $\phi_{\text{category\_match}}$ maps to "Matches your strong preference for Heritage experiences").

---

### Q8: What are the 5 objectives optimized in Stage 2?
**Answer:**
1. $\max f_1$: Total Personalization Score ($\sum_{p} \text{Score}_{\text{pers}}(u, p)$)
2. $\min f_2$: Total Monetary Cost ($\sum_{p} \text{Cost}(p)$ in INR)
3. $\min f_3$: Total Travel Transit Time ($\sum t_{\text{travel}}$ in minutes)
4. $\max f_4$: Category Diversity, quantified using Shannon Entropy:
   $$H = -\sum_{c \in \mathcal{C}} p_c \ln(p_c + \epsilon)$$
5. $\min f_5$: Average Crowd Level ($\frac{1}{N} \sum \text{Crowd}(p) \in [0, 1]$)

---

### Q9: Define Pareto dominance mathematically.
**Answer:**
For a multi-objective minimization problem with objective vector $\mathbf{F}(\mathbf{x}) = [F_1(\mathbf{x}), \dots, F_m(\mathbf{x})]$, a solution $\mathbf{x}_1$ dominates $\mathbf{x}_2$ ($\mathbf{x}_1 \prec \mathbf{x}_2$) if and only if:
1. $\forall i \in \{1, \dots, m\}, \quad F_i(\mathbf{x}_1) \le F_i(\mathbf{x}_2)$ (it is no worse in all objectives)
2. $\exists j \in \{1, \dots, m\}, \quad F_j(\mathbf{x}_1) < F_j(\mathbf{x}_2)$ (it is strictly better in at least one objective)
The Pareto front $\mathcal{PF}^*$ is the set of all non-dominated feasible solutions in objective space.

---

### Q10: How does NSGA-II work? Explain its two key selection operators.
**Answer:**
NSGA-II (Non-dominated Sorting Genetic Algorithm II) operates via:
1. **Fast Non-Dominated Sorting:** Partitions the combined parent and offspring population ($2N$) into hierarchical Pareto fronts ($\mathcal{F}_1, \mathcal{F}_2, \dots$) in $\mathcal{O}(M N^2)$ time.
2. **Crowding Distance Assignment:** Measures the density of solutions surrounding each individual in objective space to preserve diversity along the front without requiring user-specified sharing parameters.
3. **Elitist Selection:** Individuals from higher-ranked fronts are selected first; within the border front, individuals with highest crowding distances are retained.

---

### Q11: Why did you test NSGA-III / MOEA/D alongside NSGA-II? What did the empirical results show?
**Answer:**
NSGA-II is celebrated for 2-3 objective problems, but can encounter "dominance resistance" in many-objective spaces ($M \ge 4$), where almost all random solutions become non-dominated. NSGA-III addresses this using structured reference directions (Das-Dennis simplex-lattice).
In our 10-seed empirical evaluation on the travel problem:
- **NSGA-II** achieved a higher Hypervolume ($0.538 \pm 0.107$) and maintained $31.7 \pm 1.0$ diverse Pareto solutions in $1.69\text{ s}$.
- **NSGA-III** achieved Hypervolume $0.264 \pm 0.093$ with $7.8 \pm 1.6$ solutions in $3.01\text{ s}$.
Because our specialized permutation-decoder enforces dense feasibility, NSGA-II's crowding distance metric was more effective at expanding the boundary solutions than reference lines that fell into sparse combinatorial regions.

---

### Q12: How do you encode chromosomes in pymoo to ensure constraint satisfaction?
**Answer:**
Instead of binary adjacency matrices which frequently produce disconnected or invalid itineraries, we utilize a **continuous priority encoding** $\mathbf{X} \in [0, 1]^{|\mathcal{P}_{\text{cand}}|}$. 
A deterministic decoder traverses places in priority order $\arg\sort(-\mathbf{X})$ and packs places into Day 1 through Day $D$. Each candidate is appended only if it satisfies:
(1) remaining daily time allowance, (2) open/close operating hours, (3) total budget cap, and (4) pace capacity. Unvisited or invalid places are bypassed. This guarantees a **0.0% constraint violation rate**.

---

### Q13: What does the custom Repair operator do?
**Answer:**
The `ItineraryRepair` class acts as a domain-aware genetic operator:
- When an individual's budget approaches the cap ($>85\%$), the repair operator dampens the priorities of high-cost items ($\mathbf{X}_{i, \text{cost}} \times 0.85$).
- When an itinerary is under-scheduled due to scattered travel times, it boosts top personalization candidates located within proximate spatial clusters. This drives evolutionary search toward high-density, high-reward clusters.

---

### Q14: How is the Knee Point calculated?
**Answer:**
The Knee Point is the compromise solution representing the best balance across all 5 objectives without extreme sacrifice in any dimension. We use Compromise Programming / TOPSIS:
1. Objectives are normalized using the ideal point $\mathbf{z}^*$ and nadir point $\mathbf{z}^{\text{nad}}$ of the Pareto front: $\bar{F}_{k, j} \in [0, 1]$.
2. The knee point minimizes the Euclidean $L_2$ distance to the normalized ideal point $(0, 0, 0, 0, 0)$:
   $$k^* = \arg\min_k \sqrt{\sum_{j=1}^5 \bar{F}_{k, j}^2}$$

---

### Q15: If the user adjusts priority sliders in the UI, does it re-run the genetic algorithm?
**Answer:**
No! That is a central design strength of our system. The genetic algorithm performs the heavy computational search once (~1.7 s) to discover the entire 5D Pareto front. The user's sliders simply apply preference weights $w_j$ to the normalized distance function to immediately pick a different point already on the front in $<1\text{ ms}$.

---

### Q16: How do you measure category diversity? Why use Shannon Entropy?
**Answer:**
Category diversity is formulated as the Shannon Entropy of category proportions:
$$H(\mathcal{C}) = -\sum_{c \in \mathcal{C}, p_c > 0} p_c \ln(p_c)$$
If an itinerary visits only temples, $p_{\text{temple}} = 1.0$, resulting in $H = 0.0$ (monotonous). If an itinerary balances 5 distinct categories evenly ($p_c = 0.2$), entropy reaches $\ln(5) \approx 1.61$. Entropy rewards diverse exposure while penalizing repetitive theme burnout.

---

### Q17: What is the Hypervolume (HV) indicator, and why is it the gold standard in MOO?
**Answer:**
Hypervolume measures the volume of objective space enclosed between a non-dominated Pareto front and a pre-defined reference point $\mathbf{r}_{\text{ref}}$. It is the only unary metric that is **strictly Pareto-compliant**: if front $A$ dominates front $B$, then $\text{HV}(A) > \text{HV}(B)$. It simultaneously captures both convergence (closeness to the true front) and diversity (extent of coverage).

---

### Q18: What is the Spacing metric?
**Answer:**
The Spacing metric $S$ measures the uniformity of solution spread across the front:
$$S = \sqrt{\frac{1}{N} \sum_{i=1}^N (d_i - \bar{d})^2}$$
where $d_i = \min_{j \ne i} \|\mathbf{F}_i - \mathbf{F}_j\|_1$. A lower spacing value indicates an evenly distributed continuum of trade-offs rather than clustered islands.

---

### Q19: What were the quantitative findings of your recommender ablation study?
**Answer:**
Evaluated on 6,282 test interactions:
- **Hybrid (LightGBM):** Achieved the highest ranking performance with **NDCG@10 = 0.9563** and **NDCG@5 = 0.9298**, and lowest error (MAE = 0.7568).
- **Content-Only:** Achieved NDCG@10 = 0.9420, but suffered higher error (RMSE = 1.5672) due to inability to calibrate user rating baselines.
- **Collaborative-Only (SVD):** Achieved RMSE = 0.8282, but lower ranking fidelity (NDCG@10 = 0.8466).
On held-out cold-start users, Hybrid maintained **NDCG@10 = 0.9544**, outperforming Collaborative SVD (0.8044) by 18.6%.

---

### Q20: How did NSGA-II compare against the 4 baselines?
**Answer:**
- **Random Itineraries:** Produced scattered solutions with poor Hypervolume (0.398).
- **Greedy by Score:** Produced an itinerary with high personalization score, but resulted in excessive travel time and cost, collapsing to only 1 solution.
- **Greedy by Score/Cost:** Selected cheap places but failed to respect travel geometry.
- **Single-Objective Weighted-Sum GA:** Produced 1 rigid solution ($0.86\text{ s}$).
- **NSGA-II:** Discovered **31.7 non-dominated solutions** across 10 seeds with Hypervolume **0.538**, Spacing **87.26**, and **0.0% constraint violation rate**.

---

### Q21: What were the results of the End-to-End User Satisfaction experiment?
**Answer:**
Simulating 20 diverse travelers with varying paces and budgets:
- Random: 36.64% ± 4.81%
- Greedy Score: 34.69% ± 5.26%
- Greedy Score/Cost: 36.12% ± 6.18%
- Weighted-Sum GA: 51.02% ± 9.66%
- **Hybrid + NSGA-II (Knee Point):** **49.25% ± 5.68%**
While Single-Objective GA optimized exclusively for the fixed simulated weighting formula, NSGA-II produced a comparable satisfaction score while offering 30+ alternative trade-offs allowing real travelers to customize according to personal preference.

---

### Q22: How is travel time between attractions computed?
**Answer:**
We calculate the great-circle Haversine distance between coordinates:
$$d = 2 R \arcsin\left(\sqrt{\sin^2(\Delta \phi / 2) + \cos(\phi_1)\cos(\phi_2)\sin^2(\Delta \lambda / 2)}\right)$$
This is converted to travel time using an average speed model of $42.0\text{ km/h}$, a road winding and traffic factor of $1.15$, and a base boarding/parking buffer of $15\text{ minutes}$. Pairwise calculations are cached in a symmetric $(300 \times 300)$ matrix for instantaneous lookup.

---

### Q23: How does the "Replace this place" feature work?
**Answer:**
When a user clicks "Replace this place" on any stop in the UI, that place ID is added to the session's exclusion set. The candidate pool filters out the place, and NSGA-II re-optimizes the itinerary in under 2 seconds, re-allocating time to the next best geographic and thematic substitute while preserving all constraints.

---

### Q24: How would the system ingest real-world data like OpenTripMap or Kaggle?
**Answer:**
Via `data/real_data_adapter.py`. The abstract base class `BaseDataAdapter` defines standard ingestion methods (`fetch_places`, `fetch_ratings`) and a strict schema validator. The `KaggleTourismDataAdapter` maps external CSV headers to our canonical fields, and `OpenTripMapAdapter` parses GeoJSON FeatureCollections, meaning no changes to recommender or optimizer code are required.

---

### Q25: What are the primary limitations of the current implementation and directions for future research?
**Answer:**
1. **Live Traffic Fluctuations:** The current travel model uses a fixed speed heuristic; future work can integrate Google Maps Directions or OpenRouteService API for time-dependent traffic matrices.
2. **Dynamic In-Trip Re-planning:** Disruptions such as rain or unexpected closures could be handled dynamically using Deep Reinforcement Learning (e.g., PPO or contextual bandits).
3. **Group Travel Consensus:** Travel with family or friends involves multi-agent preference aggregation (e.g., Nash bargaining or Pareto group consensus).
4. **Multi-Modal Transit:** Incorporating metro, walking, and bus timetables alongside driving.

