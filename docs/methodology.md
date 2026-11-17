# Research Methodology & Mathematical Formulation

## 1. Executive Summary & Problem Motivation
Traditional travel planning systems rely either on rigid pre-packaged tour itineraries or single-objective heuristic recommenders (e.g., maximizing popularity). However, real-world travel planning is inherently **multi-criteria, constrained, and personalized**:
1. **User Heterogeneity:** Travelers possess starkly varied latent preferences across culture, nature, gastronomy, budget tolerance, and pace.
2. **Conflicting Objectives:** Maximizing tourist enjoyment typically conflicts with minimizing expenditure and travel fatigue.
3. **Complex Spatiotemporal Constraints:** Sightseeing occurs within tight daily time windows, opening/closing hours, transport times across road networks, and physical endurance caps.

To solve this, our system introduces a two-tier paradigm:
- **Tier 1 (Personalization):** A **Hybrid Machine Learning Recommender** that fuses Content-Based semantics, SVD Collaborative Filtering, and trip context via LightGBM, explained through SHAP feature attribution.
- **Tier 2 (Itinerary Synthesis):** A **Multi-Objective Team Orienteering Problem with Time Windows (TOPTW)** solved via **NSGA-II**, returning a mathematically non-dominated Pareto front of trade-offs rather than collapsing the search into a single arbitrary plan.

---

## 2. Stage 1: Hybrid Recommender Formulation

### 2.1 Content-Based Modeling
Each attraction $p \in \mathcal{P}$ is characterized by:
- Category $\mathbf{c}_p \in \{0, 1\}^{|\mathcal{C}|}$ over canonical categories $\mathcal{C}$
- Textual tags vectorized via Term Frequency–Inverse Document Frequency (TF-IDF):
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \ln\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
- Historical quality rating $r_p \in [1, 5]$ normalized to $[0, 1]$

For a user profile with category preference weights $\mathbf{w}_u$ and budget band $b_u$, the user query vector $\mathbf{q}_u$ is matched against place vector $\mathbf{v}_p$ using cosine similarity:
$$\text{Score}_{\text{CB}}(u, p) = \frac{\mathbf{q}_u \cdot \mathbf{v}_p}{\|\mathbf{q}_u\|_2 \|\mathbf{v}_p\|_2} \in [0, 1]$$

### 2.2 SVD Matrix Factorization Collaborative Filtering
Given a sparse user-item interaction matrix $\mathbf{R} \in \mathbb{R}^{|\mathcal{U}| \times |\mathcal{P}|}$, we subtract user baseline means to eliminate rating scale bias:
$$\tilde{R}_{u, p} = R_{u, p} - \mu_u$$

Truncated Singular Value Decomposition (SVD) factorizes the centered matrix into $k$ latent dimensions:
$$\tilde{\mathbf{R}} \approx \mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$$
Predicted rating for user $u$ on place $p$:
$$\hat{R}_{\text{CF}}(u, p) = \mu_u + \mathbf{u}_u \cdot \mathbf{v}_p$$
Normalized to collaborative score:
$$\text{Score}_{\text{CF}}(u, p) = \frac{\text{clip}(\hat{R}_{\text{CF}}(u, p), 1.0, 5.0) - 1.0}{4.0} \in [0, 1]$$

### 2.3 Cold-Start Folding-In
For novel users who supply $m$ interactive seed ratings $\mathcal{R}_{\text{seed}} = \{(p_i, r_i)\}_{i=1}^m$:
$$\mathbf{u}_{\text{new}} = \left(\mathbf{r}_{\text{seed}} - \bar{r}\right) \mathbf{V}_k \mathbf{\Sigma}_k^{-1}$$
The system smoothly transitions weight from content to collaborative representation as interaction count $m$ grows:
$$\alpha_{\text{CF}} = \min\left(1.0, \frac{m}{5}\right)$$

### 2.4 LightGBM Hybrid Regressor & SHAP Attribution
The hybrid model predicts the final user enjoyment rating $\hat{y}_{u, p}$ using a gradient boosted decision tree (LightGBM) trained on feature vector $\mathbf{x}_{u, p}$:
$$\mathbf{x}_{u, p} = \left[\text{Score}_{\text{CB}}, \text{Score}_{\text{CF}}, \text{Rating}_p, \text{Pop}_p, \text{Crowd}_p, \text{CostMatch}_{u,p}, \text{Dist}_{u,p}, \text{SeasonMatch}_{p}, \text{BudgetTier}_u, \text{Pace}_u, \text{CatMatch}_{u,p}\right]$$
The personalization score used by the optimizer is:
$$\text{Score}_{\text{pers}}(u, p) = \frac{\hat{y}_{u, p} - 1.0}{4.0} \in [0, 1]$$

SHAP (SHapley Additive exPlanations) computes exact additive feature attribution via TreeSHAP:
$$\hat{y}_{u, p} = \phi_0 + \sum_{j=1}^M \phi_j(u, p)$$
The top 3 features with highest positive Shapley values $\phi_j > 0$ are converted into user-facing narrative explanations ("Why this place?").

---

## 3. Stage 2: Multi-Objective Itinerary Formulation (TOPTW)

### 3.1 Decision Variables
Let $D \in \{1, \dots, 7\}$ be the trip duration.
Let $S_d = [p_{d, 1}, p_{d, 2}, \dots, p_{d, K_d}]$ denote the ordered sequence of visited attractions on Day $d$, where $K_d \le K_{\max}$.
Total places visited across all days: $\mathcal{V} = \bigcup_{d=1}^D S_d$.

### 3.2 Objective Functions
All five objectives are returned simultaneously without premature scalarization:

1. **Maximize Total Personalization Score ($f_1$):**
   $$\max f_1 = \sum_{p \in \mathcal{V}} \text{Score}_{\text{pers}}(u, p) \implies \min F_1 = -f_1$$

2. **Minimize Total Cost ($f_2$):**
   $$\min f_2 = \sum_{p \in \mathcal{V}} \text{Cost}(p)$$

3. **Minimize Total Travel Time ($f_3$):**
   $$\min f_3 = \sum_{d=1}^D \left( t_{\text{travel}}(\text{Start}_d, p_{d, 1}) + \sum_{k=1}^{K_d - 1} t_{\text{travel}}(p_{d, k}, p_{d, k+1}) \right)$$

4. **Maximize Category Diversity ($f_4$):**
   Measured via Shannon Entropy over selected attraction categories $\mathcal{C}$:
   $$p(c) = \frac{\sum_{p \in \mathcal{V}} \mathbb{I}(\text{cat}(p) = c)}{|\mathcal{V}|}$$
   $$\max f_4 = H(\mathcal{C}) = -\sum_{c \in \mathcal{C}, p(c) > 0} p(c) \ln(p(c)) \implies \min F_4 = -f_4$$

5. **Minimize Average Crowd Level ($f_5$):**
   $$\min f_5 = \frac{1}{|\mathcal{V}|} \sum_{p \in \mathcal{V}} \text{Crowd}(p)$$

---

### 3.3 Constraints & Feasibility
Every candidate solution must strictly satisfy:

1. **No Repeated Visits:**
   $$S_{d_1} \cap S_{d_2} = \emptyset, \quad \forall d_1 \neq d_2$$
   $$p_{d, i} \neq p_{d, j}, \quad \forall i \neq j$$

2. **Daily Time Budget Limit:**
   For each day $d$:
   $$T_d = \sum_{k=1}^{K_d} \text{Duration}(p_{d, k}) + T_{\text{travel}, d} \le T_{\text{daily\_cap}}$$
   where $T_{\text{daily\_cap}} \in \{480, 600, 720\}$ minutes depending on user pace (Relaxed, Moderate, Packed).

3. **Total Budget Cap:**
   $$f_2 = \sum_{p \in \mathcal{V}} \text{Cost}(p) \le B_{\text{total\_cap}}$$

4. **Opening and Closing Time Windows:**
   Let $t_{\text{arr}}(p)$ be arrival time and $t_{\text{dept}}(p) = \max(t_{\text{arr}}(p), t_{\text{open}}(p)) + \text{Duration}(p)$.
   $$t_{\text{dept}}(p) \le t_{\text{close}}(p) + 30\text{ min buffer}$$

5. **Pace-based Daily Capacity:**
   $$|S_d| \le K_{\max}, \quad K_{\max} \in \{3, 5, 7\}$$

---

## 4. Multi-Objective Solver: NSGA-II & Repair Operator

### 4.1 Permutation-Decoder Architecture
Rather than naive binary selection which frequently violates routing feasibility, we employ a continuous priority-chromosome encoding:
$$\mathbf{X} \in [0, 1]^{|\mathcal{P}_{\text{cand}}|}$$
A specialized **Decoder and Repair Operator** sequences attractions:
- Candidates are evaluated in descending order of gene priority $\arg\sort(-\mathbf{X})$.
- Each candidate is scheduled only if it satisfies the remaining daily time allowance, opening hours window, and total budget cap.
- If total expenditure exceeds 85% of budget, high-cost nodes have their priorities dampened dynamically during crossover/mutation.

### 4.2 Non-Dominated Sorting & Crowding Distance
Solutions are ranked into Pareto fronts:
$$\mathcal{F}_1 \prec \mathcal{F}_2 \prec \dots \prec \mathcal{F}_k$$
where solution $A$ dominates $B$ ($A \prec B$) if:
$$\forall j \in \{1,\dots,5\}, F_j(A) \le F_j(B) \quad \text{and} \quad \exists j, F_j(A) < F_j(B)$$

### 4.3 Knee Point Extraction (Compromise Programming)
Across the extracted non-dominated Pareto front $\mathcal{P}^*$, ideal $\mathbf{z}^*$ and nadir $\mathbf{z}^{\text{nad}}$ vectors normalize each objective:
$$\bar{F}_{k, j} = \begin{cases} 
\frac{F_{k, j} - z_j^*}{z_j^{\text{nad}} - z_j^* + \epsilon} & \text{if minimizing} \\
\frac{z_j^* - F_{k, j}}{z_j^* - z_j^{\text{nad}} + \epsilon} & \text{if maximizing}
\end{cases}$$
The **Knee Point** minimizes normalized Euclidean distance to the ideal point:
$$k^* = \arg\min_{k} \sqrt{\sum_{j=1}^5 \bar{F}_{k, j}^2}$$
User-selected priority sliders in the UI simply adjust weights $w_j$ in post-processing without biasing the evolutionary search.

