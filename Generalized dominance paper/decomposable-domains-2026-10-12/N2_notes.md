# N2: construction attempt under negligible-stakes indifference NSI_θ

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here.
- **CHECKED**: verified, with the proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Citations:
- R1 (Lemma 1.1, Prop 2.1, Lemma 1.4, Prop 3.1), R10a (Thm M, Prop M′, Thm R, Thm V), R10b (Lemma UVN, Lemma M, Thm PL), all with the repairs in R6/R8/R12.
- CSE = *Conditional Shunning of Error*; CCIBU.

Scripts are in `n2py/`.

---

## 0. Outcome

**No construction exists. The task's target is provably out of reach, and so is most of its neighbourhood.** Under NSI_θ as BRIEF3 defines it, the band ties are *forced*, not merely permitted. Forced ties create a new rigidity that kills additive coverage:

1. **T1 is never covered.** For every θ > 0, every ε ∈ (0,1), and either norm (sup or Euclidean), there is no additive system on a decomposable domain with:
   - NSI_θ-(G);
   - a.e. unique, coherent interior Bayes models;
   - (LF) at T1;
   - T1 as the Bayes model at an interior prior.

   This is Cor C1. It holds for ε-contamination of **every** interior baseline, in every n ≥ 3.
2. **No interior full-dimensional target is covered for small θ.** For θ < θ_cap(K) (defined in §1), no interior full-dimensional target K is covered (Thm Z). Here θ_cap(K) > 0 depends only on the distance of K from the vertices of Δ. So the author's ideal ("every θ > 0") fails for **every** interior full-dimensional target. Small θ is the *worst* regime, not the best.
3. **Triangles.**
   - Every interior triangle in general position with an edge ray of D_K having a single positive coordinate is excluded for **every** θ (Cor C2). These are the "upright" triangles, including T1; about 87% of random triangles (vertices sampled Dirichlet(3,3,3)) are of this kind.
   - The remaining ("inverted") triangles are excluded for θ < θ_cap(K). Above θ_cap(K) only an exceptional coincidence configuration remains (Prop C3, CHECKED).
4. **The mechanism (Thm B, PROVED, any n ≥ 3).**
   - On a band problem at world i, the chart is a pencil through δ_i. So acceptance at the target prior p\* is transported unchanged along the whole ray (δ_i, p\*].
   - Near δ_i, strictly guided non-band gambles must be accepted.
   - Convexity of the Bayes cone then forces acceptance of band gambles that are rejected at p\*.

   Corollary: whenever a supporting functional (contact point) m ∈ K of a band-i boundary gamble is cut by a non-band-i gamble whose acceptance is in the advice range, the system fails.
5. **What survives (nearby results).**
   - (a) Under the *lenient* reading ("ties permitted, not forced"), all strict-(G) results stand: R10a Thm M polygons converge to T1. Thm B then shows that ties are forbidden on the exterior band collar of the target, so they buy nothing there (§7).
   - (b) The lesson for the definition: **partial (stake-limited) indifference at a world, with strictness elsewhere at the same world, is harmful.** The obstruction needs a strict/tie interface at world i. Σ_T (total indifference at a world) has none, which is why CSE covers boxes.
   - (c) Precise targets, two-world targets, and targets meeting the caps escape these arguments. Their status is open.

**Numerics** (§9) exhibit the Thm B witness explicitly in a band-surgered R10a 9-gon system.

---

## 1. Setting, conventions, and what NSI_θ-(G) forces

The setting is that of BRIEF.md, BRIEF2.md and BRIEF3.md. Additive rankings L_i(X) = ∫ ℓ_i(g, a_X(g)) dμ on a decomposable domain.

Notation:
* φ_i(h) = h_i/‖h‖, for either norm. The results hold for both norms, and §§2–5 hold for any norm unless stated.
* An orientation h is *band-i⁺* if it is mixed and 0 < h_i ≤ θ‖h‖.
* C_θ(i) = {h : h_i > θ‖h‖}. This is an open convex cone, because h ↦ h_i − θ‖h‖ is concave and positively homogeneous. Its elements are mixed or unanimous gambles with a *non-negligible* positive world-i stake.
* **cap_θ(i)** = {m ∈ Δ : m·h ≥ 0 for all h ∈ C_θ(i)}, the dual cap. It is a neighbourhood of e_i in Δ:
  * Euclidean norm: cap_θ(i) = {m : ∠(m, e_i) ≤ arcsin θ}, the dual of a round cone of half-angle arccos θ;
  * sup norm: cap_θ(i) = {m : m_i ≥ 1/(1+θ)}, obtained by dualising the generators (θ, ±1, ±1) of C_θ(i).
* θ_cap(K) = sup{θ : K ∩ cap_θ(i) = ∅ for all i}. This is positive for K ⊆ int Δ:
  * Euclidean: min_i sin(min_{m∈K} ∠(m, e_i));
  * sup: min_i (1/max_K m_i − 1).
  * For T1, the sup-norm value is 2(1−ε)/(1+2ε), and the Euclidean value is 0.77 / 0.53 / 0.25 / 0.05 at ε = .05 / .3 / .6 / .9 (`geometry.py`).

**Standing hypotheses (H).**
* We have an additive system on a decomposable domain with NSI_θ-(G).
* For every interior q the Bayes act is a.e. unique and the Bayes model B_q is a.e. coherent, B_q ≈ D_{K_q}. Under (LA), (S), (C) this is R1 Lemma 1.4; the task also requires it directly.
* D = D_K is B_{p\*} for an interior p\*.
* (LF) holds at D with an open N ⊇ ∂D∖0. So for a.e. h ∈ N, the advice range of the choice represented by h contains both "accept h" and silence.

**Nothing at boundary priors is used anywhere below.** No (S), no CCIBU, and no vertex coherence is needed, so the vertex step of CCIBU that BRIEF3 flags is irrelevant to these results.

**Lemma 0 (penalty form of NSI_θ-(G)). PROVED.** For each i and a.e. g, on the kinds of advice in the advice range A(g):
* on band problems (mixed, |g_i| ≤ θ‖g‖), ℓ_i(good) = ℓ_i(silence) < ℓ_i(bad) < ℓ_i(contradictory);
* elsewhere ℓ_i is strictly increasing in the four-rank order.

Hence, for an orientation h with accept-h and silence in its advice range, the vector c(h) = ℓ(0) − ℓ(accept h) has:
* c_i > 0 if h_i > θ‖h‖, or if h is unanimous positive;
* **c_i = 0 if h is band-i⁺**;
* c_i < 0 if h_i < 0.

*Proof.* This is the splicing argument of R1 Lemma 1.1. On a band problem, changing good to silence is a weak improvement in the coarser order, and so is changing silence to good. So (G) makes each change weakly improve L_i, and the two penalties are equal. The strict claims are R1 Lemma 1.1 verbatim. ∎

*Remark.* The ties are **forced**. So the strict systems of R10a (Thm M, Prop M′) and the Σ_T systems of CSE (zero reward for all positive stakes at worlds of T) are **not** NSI_θ systems. Under BRIEF3's definition no earlier positive result transfers automatically. The task's phrase "f_i may vanish (but not be negative)" describes the lenient reading, which §7 treats separately.

Charts are as in R1 Prop 2.1. For an orientation h whose advice range contains + and 0, with c′ = ℓ(0) − ℓ(accept −h) when acceptance of −h is in the advice range, h is accepted at q iff c·q > 0 and (if − is in the advice range) c·q > c′·q. Contradiction is never optimal.

---

## 2. The band pencil and ray transport

**Lemma 1 (ray transport). PROVED.** Let h be band-i⁺ with + and 0 in its advice range. Let p ∈ int Δ, and q(s) = (1−s)δ_i + s p for s ∈ (0, 1].
* (a) If h is accepted at p (strictly, with no tie), then h is accepted at every q(s).
* (b) If neither h nor −h is accepted at p, and there is no tie at p, then h is accepted at no q(s).

*Proof.* We have c_i = 0, so c·q(s) = s·c·p. If acceptance of −h is in the advice range, c′_i < 0, because (−h)_i < 0 makes accepting −h bad at world i.
* (a) Here c·p > 0 and c·p > c′·p. Then c·q(s) = s c·p > 0, and
  c′·q(s) = (1−s)c′_i + s c′·p < s c′·p < s c·p = c·q(s).
* (b) If c·p > 0, then either c·p > c′·p and h is accepted, or c′·p > c·p > 0 and −h is accepted; equality is a tie. So c·p ≤ 0, and c·p = 0 is a tie, so c·p < 0. Hence c·q(s) < 0. ∎

So **a band-i⁺ chart is a union of rays from δ_i.** For fixed q, Lemma 1 holds for a.e. h, because ties at p are null.

**Lemma 2 (vertex pull). PROVED.** Let x ∈ C_θ(i) be a mixed orientation with + in its advice range. Then the chart R(x) contains a relative neighbourhood of δ_i in Δ.

Consequently, for every non-null set E of such x there are a non-null E′ ⊆ E and r₀ > 0 such that, for every interior q with |q − δ_i| < r₀, a.e. x ∈ E′ is accepted at q.

*Proof.*
* We have c_i(x) > 0 by Lemma 0. If acceptance of −x is in the advice range, (c − c′)_i > 0, because accepting −x is bad at world i.
* So δ_i satisfies the finitely many strict affine inequalities defining R(x); advice range {+} (every evaluable model accepts x) gives R(x) = Δ.
* Let r(x) > 0 be measurable with B(δ_i, r(x)) ∩ Δ ⊆ R(x), and take E′ = {x ∈ E : r(x) ≥ r₀}. ∎

---

## 3. The band–hull obstruction

**Theorem B. PROVED (any n ≥ 3, any norm).** Assume (H). Let:
* w ∈ ∂D∖0 with 0 < w_i < θ‖w‖ and −w ∉ cl D;
* m ∈ K with m·w = 0 (a contact point of w).

Then the set of mixed orientations x ∈ C_θ(i) with m·x < 0 whose acceptance is in the advice range is null. In particular N ∩ C_θ(i) ∩ {m·x < 0} = ∅.

*Proof.* Suppose E is a non-null set of such x.

*Step 0 (a neighbourhood of w).* Choose an open ball U ∋ w such that:
* U ⊆ N;
* every h ∈ U is mixed with 0 < φ_i(h) < θ;
* (−U) ∩ cl D = ∅, which is possible because −w ∉ cl D.

*Step 1 (transport).*
* Lemma 2 gives E′ and r₀. Fix q on (δ_i, p\*] with |q − δ_i| < r₀; q is interior.
* For a.e. h ∈ D ∩ U: h is accepted at p\* without a tie, and its advice range contains + and 0 by (LF). Lemma 1(a) gives h ∈ B_q.
* For a.e. h ∈ U∖cl D: h ∉ B_{p\*}, and −h ∉ B_{p\*} because −h ∉ D. Lemma 1(b) gives h ∉ B_q.
* So **B_q ∩ U ≈ D ∩ U.**

*Step 2 (convexity).*
* B_q ≈ D_{K_q}, an open convex cone.
* An open convex set that contains a.e. point of an open set O contains O. (Each y ∈ O is the midpoint of y ± v with both points in the set, for a.e. small v.)
* Hence D ∩ U ⊆ D_{K_q}. Also some x ∈ E′ lies in D_{K_q}.

*Step 3 (hull).*
* Take z ∈ D ∩ U close to w, and y = (1−λ)z + λx with λ = λ₀ small.
* Since m·w = 0, we can choose |z − w| small enough that y ∈ U and m·z < λ₀|m·x|/2. Then
  m·y < λ₀|m·x|/2 − λ₀|m·x| < 0,
  so y ∉ cl D ⊆ {m·h ≥ 0}.
* Thus D_{K_q} ∩ U∖cl D is a nonempty open set, hence non-null, and it lies a.e. in B_q. This contradicts Step 1. ∎

**Corollary B1 (same-face form). PROVED.** Assume (H). Suppose an exposed face F_m = {h ∈ cl D∖0 : m·h = 0} (m ∈ K) contains:
* a point w with 0 < φ_i(w) < θ and −w ∉ cl D, and
* a point w′ with φ_i(w′) > θ.

Then (H) fails.

*Proof.* We have w′ ∈ ∂D∖0 ⊆ N. The points x = w′ − s𝟙 with s > 0 small form an open subset of N ∩ C_θ(i) with m·x = −s < 0. Apply Thm B. ∎

*Remark (why strict (G) escapes).* With strict (G), c_i(h) > 0 is merely small on near-band h, so the chart tilts and transport along (δ_i, p\*] holds only on one side. NSI_θ pins the chart line to δ_i. That is the whole difference.

---

## 4. Facet crossings: T1 for every θ

**Theorem C. PROVED (n ≥ 3; Euclidean or sup norm; any θ ∈ (0, 1)).** Assume (H). Let F_m (m ∈ K, m ≫ 0) be an (n−1)-dimensional exposed face of D. Write relint for the relative interior in m^⊥. Assume −h ∉ cl D on relint F_m, which is automatic if K is full-dimensional. If relint F_m contains
* (a) a point at which i is the only positive coordinate, and
* (b) a point with h_i < 0,

then (H) fails.

For θ ≥ 1 every mixed orientation is band at every positive world. Every mixed chart is then empty at interior priors, and (H) fails trivially, since ∂D∖0 is mixed.

*Proof.* Let S = {h ∈ relint F_m : h_j < 0 for all j ≠ i}. By (a), S is nonempty and relatively open. On S, h_i > 0: otherwise m·h < 0 for m ≫ 0. The set relint F_m is connected, and φ_i takes a negative value there by (b). There are three cases.
1. *Some s ∈ S has φ_i(s) > θ.* By connectedness φ_i takes a value in (0, θ) on relint F_m. Apply Cor B1.
2. *Some s ∈ S has φ_i(s) < θ.*
   * Points h ∈ D near s are band-i⁺ and have all other coordinates negative.
   * So c(h) has c_i = 0 and c_j < 0 for j ≠ i, and c·q < 0 at every interior q.
   * Their advice ranges contain silence by (LF), so a.e. such h is rejected at p\*.
   * But D near s is a non-null set of h accepted at p\*. Contradiction.
3. *φ_i ≡ θ on S.*
   * Euclidean norm: the quadratic form (1−θ²)h_i² − θ²Σ_{j≠i}h_j² vanishes on an open subset of the hyperplane m^⊥, hence on all of m^⊥. But m^⊥ ∩ e_i^⊥ ∋ h ≠ 0 (n ≥ 3), where the form is −θ²|h|² < 0.
   * Sup norm: on S, ‖h‖ = −min_{j≠i}h_j. On an open S′ ⊆ S where a single j₀ attains the minimum, h_i + θh_{j₀} = 0. This linear identity on an open part of m^⊥ forces m ∝ e_i + θe_{j₀}, contradicting m ≫ 0 for n ≥ 3. ∎

**Corollary C1 (contamination; T1). PROVED.** Let n ≥ 3, p ∈ int Δ, ε ∈ (0,1), and K = (1−ε)p + εΔ. Then (H) fails for every θ > 0 and either norm. In particular **T1 (p = u, n = 3) is covered under NSI_θ for no θ and no ε.**

*Proof.* Let v_k = (1−ε)p + εe_k. Then v_j·h − v_k·h = ε(h_j − h_k), so
relint F_k = {h : (1−ε)p·h + εh_k = 0, h_k < h_j for all j ≠ k}.
Fix i ≠ k.
* *(a)* Take h_k = −1, h_j = −1+η for j ∉ {i,k}, and
  h_i = β = [ε/(1−ε) + p_k + (1−p_i−p_k)(1−η)]/p_i > 0.
  This point lies in relint F_k, and i is its only positive coordinate.
* *(b)* Take h_k = −1, h_i = −½, and h_j = M for j ∉ {i,k} (such j exist since n ≥ 3), with
  M = (ε/(1−ε) + p_k + p_i/2)/(1 − p_i − p_k) > 0.
  This point lies in relint F_k and has h_i < 0.
* K is full-dimensional and v_k ≫ 0. Apply Thm C. ∎

For T1 this is visible in `geometry.py`:
* On F_3, h(s) = (−1+s, b−s, −1) with b = (2+ε)/(1−ε). Here φ_2 runs from about −0.39…−0.03 up to φ_2(r₃₁).
* Sup norm: φ_2 ≡ 1 near r₃₁.
* Euclidean norm: φ_2(r₃₁) = 0.836…0.999, and the maximum lies strictly inside F_3 (case 1 for θ below the maximum; case 2 above it).

**Corollary C2 (upright triangles). PROVED (n = 3).** Let K ⊆ int Δ be a triangle in general position (no edge line through a vertex of Δ). If some edge ray of D_K has exactly one positive coordinate, (H) fails for every θ.

*Proof.*
* The edge ray r_e of edge e = [v_k, v_j] has positive coordinates exactly at the vertices of Δ on K's side of line(e). General position makes every coordinate of every edge ray nonzero.
* Let r_e have single positive coordinate i. If i were positive on the other edge rays of both F_k and F_j, then e_i would lie on K's side of all three edge lines, so e_i ∈ K, which is impossible.
* So on F_k (say) coordinate i changes sign, giving (b). Near r_e, relint F_k has the sign pattern of r_e, giving (a). Apply Thm C. ∎

**Proposition C3 (inverted triangles above θ_cap). CHECKED (sketch).** Suppose every edge ray of a general-position triangle has two positive coordinates. Then (H) can hold only in an exceptional configuration, which requires all of the following.
* At each edge ray r = cl F ∩ cl F′ with positive coordinates {i, j}:
  * i crosses on F only and j on F′ only;
  * φ_i(r) = φ_j(r) = θ, with the same θ at all three edge rays;
  * the contact vertex of F lies in cap_θ(i), and that of F′ lies in cap_θ(j).

*Sketch.*
* Each positive coordinate crosses on an adjacent facet (the C2 argument), so Cor B1 gives φ ≤ θ on that facet.
* Positivity near r (case 2 of Thm C, with two positive coordinates) forces the rest.
* The cap condition comes from the Thm Z step 2 perturbation at w₀ = r.

For the symmetric inverted triangles this is excluded by θ_inv < θ_cap at ε = .1, .3, .6, .9 (`geometry.py`).

---

## 5. Every interior full-dimensional target, for small θ

**Theorem Z. PROVED (any n ≥ 3, any norm).** Assume (H) with K ⊆ int Δ full-dimensional and K ∩ cap_θ(i) = ∅ for every i (that is, θ < θ_cap(K)). Contradiction.

*Proof.*

*Step 1 (positivity).* For a.e. h ∈ D ∩ N, some l has h_l > θ‖h‖. Otherwise c(h) ≤ 0 with a negative entry (h is mixed), so c·p\* < 0 and h is rejected at p\*, as in case 2 of Thm C.

*Step 2 (φ_i ≤ θ on ∂D∖0, for every i).*
* ∂D∖0 is connected (n ≥ 3).
* φ_i is negative somewhere on it. Separate e_i from K by a gamble g, then subtract the constant min_K g·m, which keeps g_i < 0.
* Suppose φ_i(w′) > θ somewhere. Along a path from a negative value to w′, there are band-i⁺ points w_k → w₀ with φ_i(w₀) = θ. Take t₁ = the first time φ_i ≥ θ, and t₀ = the last time before t₁ with φ_i ≤ 0.
* Choose contacts m_k ∈ K with m_k·w_k = 0, and a subsequence m_k → m\* ∈ K. Then m\*·w₀ = 0.
* Since m\* ∉ cap_θ(i), there is h ∈ C_θ(i) with m\*·h < 0. Put x = w₀ + s h. By the triangle inequality,
  x_i − θ‖x‖ ≥ s(h_i − θ‖h‖) > 0.
  Also m\*·x = s m\*·h < 0, and x ∈ N for small s.
* For large k, m_k·x < 0 on an open neighbourhood of x in N ∩ C_θ(i). Theorem B with (w_k, m_k) gives a contradiction. Note −w_k ∉ cl D because K is full-dimensional.

*Step 3.*
* Fix w ∈ ∂D∖0 and a contact μ ∈ K (μ·w = 0). Take small balls B ∋ w inside N.
* By Step 2, each convex C_θ(l) ∩ B misses ∂D, so it lies in D or misses cl D.
* By Step 1, D ∩ B is a.e. covered by those C_θ(l) ∩ B that lie in D. Since w ∈ cl(D ∩ B) for every B and there are finitely many l, some l has w ∈ cl C_θ(l) and C_θ(l) ∩ B ⊆ D ⊆ {μ·y > 0}.
* *Local to global:* suppose y′ ∈ C_θ(l) had μ·y′ < 0. Take c ∈ C_θ(l) ∩ B near w with μ·c small. Then points of [c, y′] near c lie in C_θ(l) ∩ B with μ < 0.
* So μ·y ≥ 0 on C_θ(l), i.e. μ ∈ cap_θ(l) ∩ K = ∅. Contradiction. ∎

*Reading.* At small θ, the band edge {φ_i = θ} lies close to the hyperplane {h_i = 0}, so it meets the target boundary. There Thm B forces K to contain only points of the cap. For **every** interior full-dimensional target the admissible θ (if any) satisfy θ ≥ θ_cap(K). The answer to BRIEF3 question (2) is therefore the reverse of the hoped-for one.

---

## 6. Other targets, and n ≥ 4

* **Interior segments (T3).**
  * Let K = [a, b] in general position. The face F_a = {a·h = 0, b·h > 0} is an open half-plane.
  * Pick i, j with b_i/a_i > b_j/a_j. Then h = e_i − (a_i/a_j)e_j ∈ relint F_a.
  * Band points h = z + t(e_i − (a_i/a_j)e_j) also lie in relint F_a, where z spans a^⊥ ∩ e_i^⊥ and b·z > 0.
  * −h ∉ cl D on relint F_a. So Cor B1 excludes T3 for all θ < sup_{relint F_a} φ_i (PROVED for that range). The full range is open.
* **T4 = conv{e₁, u}, a boundary-touching segment, with an interior target prior.**
  * The face F_u = {u·h = 0, h₁ > 0} contains (2, −1, −1), with φ₁ = 2/√6 ≈ 0.816 (Euclidean) or 1 (sup).
  * It also contains band points (t, 1, −1−t).
  * −h ∉ cl D because cl D ⊆ {h₁ ≥ 0}.
  * Cor B1 excludes T4 for θ < 0.816 (Euclidean) and θ < 1 (sup). PROVED.
* **Boundary-touching full-dimensional targets.**
  * Thm B and Cor B1 apply unchanged.
  * Thm Z needs K ∩ caps = ∅, which fails for targets containing vertices. Such targets, with K near e_i where it meets cap_θ(i), are not excluded by these arguments. Open.
* **Precise targets** {p\*}. Every boundary gamble has −w ∈ ∂D, so Lemma 1(b) fails: exterior band gambles may switch from −h to +h along the ray. Thm B does not apply. **Open**; no construction was attempted.
* **n = 2.**
  * Faces are rays and ∂D∖0 is disconnected, so Thm B, C and Z have no content.
  * Case 2 of Thm C still gives a necessary condition. For K = {m₁ ∈ [a, b]}, the boundary rays must be non-band at their positive coordinate, e.g. (1−a)/‖(1−a, −a)‖ > θ. Sufficiency is open.
* **n ≥ 4.** Lemmas 0–2, Thm B, Cor B1, Thm C, Cor C1 and Thm Z are written dimension-free (n ≥ 3). The contamination no-go holds for every θ in every n ≥ 3.

---

## 7. Lenient reading and the general tie-region principle

* **Lenient NSI_θ** ("good ⪯ silence allowed on band problems, strictness elsewhere"; the task's "may vanish"). This class contains every strictly guiding system. So R10a Thm M and Prop M′ (polygons converging to T1 in Hausdorff distance), CSE boxes, precise targets and all earlier positive results stand.

  **Proposition L. CHECKED.** Under the lenient reading, with (H) otherwise, Thm B's proof shows that for w, m, x as in Thm B, c_i > 0 a.e. on an exterior slab {y near w : −c < m·y < 0}. The hull of x and D near w contains that slab when w is in the relative interior of a facet. Interior-side ties add rigidity only: Lemma 1(a) transports from p\* *away* from δ_i as well. So ties cannot help near the target boundary.

  CONJECTURE: under the lenient reading, T1's status equals its strict status (open; R10b Thm PL plausibly survives, because Lemma M uses exterior strictness only).
* **General tie regions.** Replace the band by any measurable cone R_i of orientations with h_i > 0 on which good ~ silence at world i, with strictness on {h_i > 0}∖R_i. The proof of Thm B goes through verbatim. It obstructs whenever a target boundary gamble in int R_i has a contact m cut by a gamble in int({h_i > 0}∖R_i) whose acceptance is in the advice range with m·x < 0.
  * Σ_T has R_i = {h_i > 0}, with no strict side. Hence no obstruction, consistent with CSE.
  * **Partial indifference at a world (a strict/tie interface at that world) is the harmful structure.** A weakening that is to help coverage must avoid such interfaces near target boundaries. A target-independent band cannot do that.
* **Scope.** Thm B uses additivity (charts are affine minimisation diagrams). For non-additive (IB) preorders under NSI_θ nothing is claimed.

---

## 8. Designs tried, and where each fails

| design | fate | reason |
|---|---|---|
| band surgery of gauge mixtures (f_i := 0 on band-i⁺) | incoherent B_q near δ_i | Thm B; explicit witness in §9 |
| plateau K_q ≡ T1 near p\* (R10b PL crossing argument broken by NSI) | impossible | Thm B uses p\* alone, no plateau needed |
| imprecise vertex models (caps) | allowed at vertices | Thm Z: the target's band contacts must lie in caps |
| Σ_T-type zero lower slope inside bands only | not an NSI system unless ties are exact; with exact ties | Thm B / C |
| large θ for T1 | impossible | Thm C cases 1–3 cover all θ ∈ (0,1); θ ≥ 1 trivial |

---

## 9. Numerics (`n2py/`, evidence only)

* `geometry.py`:
  * T1 facet data, both norms. The Euclidean maximum of φ_2 on F_3 is interior, and φ_2 is negative near r₃₂.
  * θ_cap for T1 (the sup-norm formula is confirmed).
  * 20000 random triangles: 87% have a single-positive edge ray (Cor C2), 13% are inverted.
  * Symmetric inverted triangles: θ_inv < θ_cap, so Thm Z excludes θ_inv.
* `surgery_check.py`, `hull_check.py`, `hull_check2.py`: random midpoint and dual-hull tests of band-surgered R10a systems (hexagon, 9-gon).
  * Hexagon: defects of mass up to 0.6% at θ = .2.
  * 9-gon: about 0. This is because Thm B's failure region is a thin exterior collar, so random tests are insensitive. Not evidence of coherence.
* `witness2.py` (9-gon, θ = .05, Euclidean): constructs Thm B's objects:
  * a band-1⁺ boundary gamble w of B_u, with φ₁ = 0.025;
  * its contact m\* = (0.234, 0.531, 0.234);
  * a non-band x whose acceptance is in the advice range, with m\*·x = −0.0044.

  At q = (1−s)e₁ + s u with s ≤ 0.002: x and z (inside, near w) are accepted, while y ∈ [z, x] (beyond the facet plane, φ₁ = 0.026, rejected at u) is rejected. So B_q is non-convex exactly as predicted. For s ≥ 0.02, x is not yet accepted, consistent with Lemma 2's r₀.

  The surgered B_u itself shows a reflex kink where its facet meets the band edge (a boundary gamble with m\*·w′ < 0).

---

## 10. Recommendation (spirit of the project)

* NSI_θ as defined (forced ties) does not deliver coverage of T1 for any θ. It excludes every interior full-dimensional target for θ < θ_cap(K), and every upright triangle and every contamination class for all θ.
* The reachable nearby results are:
  * (i) the lenient reading, which keeps all strict-(G) coverage, including the R10a polygons converging to T1, but adds nothing near target boundaries (Prop L);
  * (ii) the general tie-region principle (§7), which says any acceptable indifference weakening must be *total at a world* (Σ_T-like) rather than stake-limited.
* The author should decide between:
  * (a) dropping the forced-tie clause (lenient reading), in which case T1 stays exactly the strict problem; or
  * (b) seeking a weakening without strict/tie interfaces at a single world (for instance indifference indexed by events rather than by stake size).

  Option (b) is the only route this analysis leaves open for contamination targets.
