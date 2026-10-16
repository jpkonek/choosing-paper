# N6: constructive attempt for T1 under PERMITTED negligible-stakes ties (BRIEF4)

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here.
- **CHECKED**: verified, proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Citations:
- R1 (Prop 2.1 table, Lemma 1.3(a), Lemma 1.4), R10a (Thm V, Thm M, Prop M′), R10b (Prop V, V1, Lemma FS, UVN, Lemma M, Thm PL), R15 (Thm 1, Lemma 6.1, Thm 6.2; refereed CORRECT in R18).
- N2 (Lemma 1 ray transport, Lemma 2 vertex pull, Thm B, Prop L; refereed in N4), N3 (Thm PL_θ, Thm CC_θ).

Scripts are in `n6py/`. Nothing was written outside this folder.

---

## 0. Outcome

**No construction. Every design of the kind BRIEF4 proposes fails, and the failure is a general theorem, not a design artefact.**

Under permitted NSI_θ, good~silence ties can never sit on the inner side of D_{T1}. Near ∂D_{T1} they can sit only in thin outer "horns" at the six coordinate crossings. So the mechanism BRIEF4 hoped for (inner-side ties near the crossings that relax the inputs of the strict no-gos) does not exist. The no-gos for T1 transfer from strict guidance to permitted ties.

Throughout:
- (H) means: an additive system on a decomposable domain under permitted NSI_θ; at every interior prior, a.e.-unique Bayes acts and coherent Bayes models B_q ≈ D_{K_q}; D_{T1} = B_{p\*} for some interior p\*; (LF) at D_{T1}.
- Θ_NT(T1) is the threshold defined in §1. Sup norm: Θ_NT = 1. Euclidean norm: Θ_NT = (κ+1)/√((κ+1)²+2), with κ = (1+2ε)/(1−ε). This lies in (√(2/3), 1); it is 0.9185 at ε = 0.3.

**N6.1 Domination Lemma DL (PROVED; any n, any target, any tie rule of good~silence type).** A tied orientation h (c_i(h) = 0, h_i > 0) cannot dominate coordinatewise a density point of the set of orientations, with acceptance in the advice range, that are strictly good at world i. The lemma needs only IBU and coherence at interior priors near e_i. It is the new mechanism.

**N6.2 Outer-tie Lemma OT (PROVED; T1, θ < Θ_NT, either norm).** Outer ties near ∂D_{T1} are null except in horns. The horns have depth ≥ (τ/2)·h_i at the crossing rays w_{ik}, for a constant τ > 0 fixed by the system. This verifies N2 Prop L away from the crossings, in density form. Directly at the crossings it is sharper than Prop L, which did not address those points.

**N6.3 Theorem NT (PROVED; T1, θ < Θ_NT, either norm).** Under (H):
- (a) inner ties are null on all of D_{T1}, at every world, not only near ∂D;
- (b) on a neighbourhood N′ of ∂D∖0, ties lie a.e. in the six outer horns Hor_{ik};
- (c) ties near ∂D accumulate only at the crossing rays, from outside, tangentially to {h_i = 0}.

So inner-side ties near the crossings, which are designs (a) and (b) of the task, are impossible for every θ ∈ (0, Θ_NT). N2 Prop L's "inner ties only add rigidity" is corrected: inner ties are impossible.

**N6.4 Vertex anchoring survives (Thm V′, PROVED).** Under (H) plus (LA), (S), every coherent e_i-Bayes model D_V has e_i ∈ V. The coordinator's claim in BRIEF4 is true. Its sketch, however, uses outer strictness at the crossings, which horns may violate; the proof here uses inner points only, which NT(a) makes strict. Hence R10b Cor V1 (gambles accepted by every evaluable model are nonnegative) and Lemma FS also hold.

**N6.5 Transfer (PROVED, by a line-by-line check of refereed proofs, §6).** For T1 under permitted NSI_θ:
- R15 Thm 6.2 holds with θ < Θ_NT. No realisation satisfies (DF), (ND), (NA_w). The same holds for R15 Lemma 6.1 (box), Thm 1(a)–(d) and Lemma 3.2.
- N3 Thm PL_θ (no plateau) holds with θ < θ_A (sup norm: θ_A = 1 for ε ≥ 1/4).

So permitted ties gain nothing in the class where strict guidance is already excluded.

**N6.6 Designs tried (NUMERICS, §7).**
- The strict 9-gon gauge system S0 passes every test.
- Inserting inner ties near its crossings (S1) breaks coherence near the vertices. Explicit DL certificates were found for 136 of 400 tied samples.
- A T1-exact all-model field with inner cevian ties (S2, B_u = D_{T1} exactly, permitted-(G) exact) fails badly: 3496 midpoint and 2194 upward violations summed over the 118 test priors, worst near the vertices and edges. DL certificates were found for 373 of 400 tied samples. Its strict analogue S2s fails too.
- Ties on all outer band points (S4) fail.
- Naive horn ties (S3) fail at a few priors with small genuine margins.

**N6.7 Thresholds (PROVED; NUMERICS agree to 6 digits, `theta1.py`).**
- Facet maxima: max_{cl F_k} h_i/‖h‖ for i ≠ k is 1 (sup) and √((κ²+1)/(κ²+2)) (Euclidean).
- Corner values: (κ+1)/‖(κ+1,−1,−1)‖, which is the binding constraint.
- h_k < 0 on all of F_k.

**N6.8 Residual (open).**
- (i) Horn ties: not excluded by DL/OT. CONJECTURE N6: they are impossible, or removable without loss. Even if they exist, they do not affect N6.5.
- (ii) θ ∈ [Θ_NT, 1) in the Euclidean norm (and θ ≥ 1): not treated.
- (iii) The strict residual of R15 §9 is unchanged: (E1) kinked facets, (E2) sliding edges, (E3) flat facets, (E4) adjacency at box witnesses. Plus the horn freedom.

**N6.9 Smallest θ / norm.** No design was found, so no θ is claimed for a construction. The obstruction holds for every θ ∈ (0, Θ_NT), for both norms; only Θ_NT depends on the norm. **Small θ is not a loophole.**

**N6.10 Nearby reachable results.**
- What remains true:
  - strict-guidance polygons converging to T1 (R10a Prop M′);
  - every positive result of the strict class (the permitted reading contains it).
- What would have to change for indifference to help a polytope target: DL + OT use only two inputs. One is strictly guided outer points cutting each facet contact, with acceptance in the advice range for large stakes; the other is "bad strictly worse than silence". An indifference rule helps only if it ties good~silence on the *whole* outer side of a facet's i-positive region, including large stakes. That conflicts with the author's "strict for non-negligible stakes" (§9, CHECKED).
- So for T1 the indifference route is closed under the brief's constraints. The live question is the strict residual (E1)/(E2) of R15.

---

## 1. Setting and notation

- n = 3. T = T1 = (1−ε)u + εΔ, with vertices v_k = (1−ε)u + εe_k and D = D_T.
- Facets: F_k = {h : v_k·h = 0, h_k < h_j (j ≠ k)}. Normalising h_k = −1, F_3 = {(t, κ−t, −1) : t ∈ (−1, κ+1)}.
- Corner rays: r_{kj} = cl F_k ∩ cl F_j. For example r_{31} = (−1, κ+1, −1); its only positive coordinate is 2.
- Crossings: w_{ik} ∝ v_k × e_i for i ≠ k. For example w_{13} = (0, κ, −1) and w_{23} = (κ, 0, −1).
- On F_k, h_k < 0 throughout (all-facing).
- φ_i(h) = h_i/‖h‖ (sup or Euclidean).

**Permitted NSI_θ (BRIEF4).** For an orientation h whose advice range contains + and 0, put c(h) = ℓ(0) − ℓ(acc h). Then:
- c_l(h) < 0 if h_l < 0;
- c_l(h) > 0 if h_l > 0 and (h is unanimous or h_l > θ‖h‖);
- c_l(h) ≥ 0 if h is band-l⁺ (mixed, 0 < h_l ≤ θ‖h‖).

Contradiction is worst. The tie and strict sets are:
- Θ_i = {h : h_i > 0, +, 0 ∈ A, c_i(h) = 0}. These points are band-i⁺ and mixed.
- S_i = {h : h_i > 0, + ∈ A, and accepting h is the unique best advice in the advice range at world i}.

If +, 0 ∈ A and c_i(h) > 0, then h ∈ S_i: if − is in the advice range, c′_i < 0 because accepting −h is bad at i.

**Standing hypotheses (H).**
- Additive penalties with integrable envelopes on a decomposable domain, satisfying permitted NSI_θ-(G).
- IBU: for every q ∈ int Δ the Bayes act is a.e. unique and B_q ≈ D_{K_q}.
- D ≈ B_{p\*} with p\* ∈ int Δ.
- (LF): an open cone N ⊇ ∂D∖0, shrunk as in R10a §1, so that N ∩ (−cl D) = ∅, N contains no h ≤ 0, and for a.e. h ∈ N the advice range of the choice represented by h contains accept-h and silence.

Nothing is assumed at boundary priors, except in N6.4 (vertex models), where (LA), (S) are used.

**Facts used** (all refereed):
- (F0) R(h) is the chart of h: the set of priors at which accepting h is the unique minimiser. It is relatively open in Δ and convex. If +, 0 ∈ A, then R(h) ⊆ {q : c(h)·q > 0}. If h ∈ S_i, then δ_i ∈ R(h).
- (F1) An open convex set containing a.e. point of an open set O contains O.
- (F2) Ray transport (N2 Lemma 1, N4 CORRECT). Let h ∈ Θ_i, p ∈ int Δ, q(s) = (1−s)δ_i + s·p.
  - (a) If h is accepted at p without a tie, h is accepted at q(s) for s ∈ (0,1].
  - (b) If neither h nor −h is accepted at p and there is no tie, then c(h)·p < 0, hence c(h)·q(s) = s·c(h)·p < 0 for every s > 0.
- (F3) Vertex pull (N2 Lemma 2). For non-null E ⊆ S_i there are a non-null E′ ⊆ E and r₀ > 0 such that, for interior q with |q − δ_i| < r₀, a.e. x ∈ E′ is accepted at q.

**Thresholds (N6.7; PROVED by calculus).**
- On F_3 with i = 1, maximise t/√(t² + (κ−t)² + 1). The critical point is t\* = (κ²+1)/κ ∈ (−1, κ+1), giving value √((κ²+1)/(κ²+2)). The sup-norm maximum is 1, attained near r_{32}.
- The corner value is φ_2(r_{31}) = (κ+1)/‖(κ+1,−1,−1)‖.
- Θ_NT(T1) := min over corner rays r and coordinates l with r_l > 0 of φ_l(r), together with the facet maxima. The corner value is smaller.
- So Θ_NT = 1 (sup) and (κ+1)/√((κ+1)²+2) (Euclidean). Values for ε = .05 / .1 / .3 / .5 / .6 / .9: 0.836 / 0.855 / 0.918 / 0.962 / 0.977 / 0.999.

For θ < Θ_NT:
- (T-i) every corner ray has a neighbourhood containing no band point;
- (T-ii) each F_k contains, for each i ≠ k, points with φ_i > θ.

---

## 2. The domination lemma

**Lemma DL (PROVED; any n ≥ 2, any target, any measurable good~silence tie rule).** Assume only IBU at interior priors. Let x⁰ be a Lebesgue density point of S_i. Then Θ_i ∩ (x⁰ + ℝⁿ_{≥0}) is null. Consequently Θ_i ∩ (S_i^♯ + int ℝⁿ_{≥0}) is null, where S_i^♯ denotes the density points of S_i.

*Proof.*

*Step 1: x⁰ ∈ D_{K_q} for all q ∈ V ∩ int Δ, for some relative neighbourhood V of δ_i.*
- Let B₀ = B(x⁰, ρ) with μ(B₀∖S_i) ≤ μ(B₀)/8.
- For x ∈ S_i ∩ B₀, R(x) is relatively open and contains δ_i (F0). So x ∈ B_q once |q − δ_i| < r(x).
- By dominated convergence along any sequence q_m → δ_i of interior priors, μ((S_i ∩ B₀) ∖ B_{q_m}) → 0. Since B_q ≈ D_{K_q}, μ(B₀ ∖ D_{K_q}) < μ(B₀)/4 for q close to δ_i. (Argue by contradiction with sequences to get a full neighbourhood V.)
- If x⁰ ∉ D_{K_q}, separate the open convex cone D_{K_q} from x⁰: D_{K_q} ⊆ {ν·h > 0} with ν·x⁰ ≤ 0. Then D_{K_q} misses the half-ball {h ∈ B₀ : ν·(h−x⁰) ≤ 0}, which has measure μ(B₀)/2. Contradiction.

*Step 2.* For h ≥ x⁰ and q ∈ V ∩ int Δ: m·h ≥ m·x⁰ > 0 for every m ∈ K_q ⊆ Δ. So h ∈ D_{K_q}.

*Step 3.*
- Suppose E = Θ_i ∩ (x⁰ + ℝⁿ_{≥0}) is non-null.
- Each h ∈ E is mixed, so h_k < 0 for some k. Accepting h is then bad at k, so c_k(h) < 0. Fix k on a non-null E₁ ⊆ E.
- For α, s ∈ (0,1), put q(s,α) = (1−s)δ_i + s((1−α)δ_k + αu). This prior is interior.
- Since c_i(h) = 0, c(h)·q(s,α) = s[(1−α)c_k(h) + α u·c(h)]. This is negative for α < α(h) := |c_k|/(|c_k| + |u·c| + 1).
- Choose α₀ with E₂ = {h ∈ E₁ : α(h) > α₀} non-null, and s with q := q(s,α₀) ∈ V.
- By (F0), a.e. h ∈ E₂ is not accepted at q, i.e. h ∉ B_q. By Step 2, h ∈ D_{K_q}. So E₂ ⊆ D_{K_q} ∖ B_q, which is null by IBU. Contradiction.

*Consequence.* Density points of S_i lie arbitrarily close to any density point. Take a countable dense subset of S_i^♯ and a countable union. ∎

*Reading.* A tie pins the chart line to δ_i, so the tied orientation is rejected at priors next to δ_i on the side of a negative world. Anything above a strictly guided point is accepted at **all** priors next to δ_i. Unlike N2 Thm B, the lemma needs no target, no (LF) and no contact geometry.

---

## 3. Outer ties near ∂D

**Lemma OT (PROVED).** Assume (H), T = T1, θ < Θ_NT. Fix k and i ≠ k, and a closed subcone A ⊂ relint F_k ∪ {0} with nonempty interior.
- Choose y\* ∈ relint F_k with φ_i(y\*) > θ (T-ii), and x\* = y\* − s\*𝟙 with s\* > 0 small. Choose a ball B\* ∋ x\* inside N ∩ {φ_i > θ} ∩ {v_k·x < −s\*/2} ∩ {h mixed}.
- Put τ := inf_{x∈B\*} |v_k·x|/x_i > 0.

Then there is an open cone W_A ⊇ A∖0 such that Θ_i ∩ W_A ∩ {h ∉ cl D : −v_k·h < (τ/2) h_i} is null.

*Proof.*
1. *The cutting point x.* B\* ⊆ S_i a.e.: the advice ranges of its points contain + and 0 (they lie in N), they are off-band, and c_i > 0 there. Vertex pull (F3) gives E′ ⊆ B\* and r₀. Fix q ∈ (δ_i, p\*) with |q − δ_i| < r₀; q is interior.
2. *Rejection on the cevian.* Let h ∉ cl D lie in N. Then −h ∉ cl D. By IBU at p\* and B_{p\*} ≈ D, a.e. such h is accepted at p\* in neither orientation and has no tie. If h ∈ Θ_i, (F2b) gives c(h)·q < 0, so h ∉ B_q.
3. *Inner acceptance.* Let G = {z ∈ D ∩ N : z_i > 0}, an open set. Take a.e. z ∈ G; then p\* ∈ R(z).
   - If c_i(z) > 0, then δ_i ∈ R(z) (F0), so q ∈ [δ_i, p\*] ⊆ R(z).
   - If c_i(z) = 0, (F2a) applies.

   So G ⊆ B_q a.e., hence G ⊆ D_{K_q} by (F1).
4. *x accepted.* E′ ∩ B_q is non-null (F3), so some x ∈ B\* lies in D_{K_q}.
5. *Hull.* Normalise ‖h‖ = ‖x‖ = 1 and write σ(h) = −v_k·h. Choose W_A so thin that for h ∈ W_A outside cl D:
   - σ(h) is small;
   - v_l·h > c_A > 0 for l ≠ k;
   - h ∈ N.

   For such h with σ(h) < (τ/2)h_i, put λ = 2σ/|v_k·x| and z = (h − λx)/(1−λ). Then λ < h_i/x_i, so z_i > 0. Also v_k·z = σ/(1−λ) > 0, and v_l·z > 0 for l ≠ k because λ is small. So z ∈ G ⊆ D_{K_q}, and h = (1−λ)z + λx ∈ D_{K_q}.

   These conditions are open in h. So a neighbourhood O of any density point h⁰ of the set in the statement lies in D_{K_q}.
6. *Contradiction.* O ∩ Θ_i is non-null; it lies in D_{K_q} and, by step 2, a.e. outside B_q. This contradicts IBU at q. ∎

*Remark (why the crossings are special).* The hull needs both z_i > 0 and v_k·z > 0. Since x_i > 0 and v_k·x < 0, this works only when σ(h)/h_i < |v_k·x|/x_i. Near a crossing ray h_i → 0, so outer points that are deep relative to h_i ("horns") escape. The design controls the advice ranges outside N, so it can make |v_k·x|/x_i small, i.e. horns fat relative to the scale of N. Away from the crossings (h_i bounded below near the facet point), the condition holds on a full exterior neighbourhood. That is N2 Prop L, now PROVED in density form.

---

## 4. No ties on the inside; horns only, near the boundary

**Theorem NT (PROVED).** Assume (H), T = T1, θ < Θ_NT (either norm). There is an open cone N′ ⊇ ∂D∖0 such that, for each world i:
- (a) Θ_i ∩ D is null;
- (b) Θ_i ∩ N′ ⊆ Hor_i a.e., where Hor_i = ∪_{k≠i} Hor_{ik}, and Hor_{ik} is the set of h ∉ cl D near the crossing ray w_{ik} with 0 < h_i ≤ (2/τ)(−v_k·h);
- (c) consequently the closure of Θ_i ∩ N′ meets ∂D∖0 only in the rays w_{ik}.

*Proof of (b).*
- By (T-i), small cone neighbourhoods C_r of the three corner rays contain no band point, hence no ties.
- Cover the rest of ∂D∖0 by finitely many W_{A_k}, with A_k = cl F_k minus those neighbourhoods (Lemma OT, for each i ≠ k). For i = k, F_k ⊆ {h_k < 0}, so there are no band-k⁺ points near A_k.
- Inside W_{A_k}, a tied h with h_i > 0 is one of three kinds:
  - inner: null by (a), which uses only Lemma OT (see below);
  - outer with σ < (τ/2)h_i: null by Lemma OT;
  - outer with h_i ≤ 2σ/τ: then h_i is small, because σ is small on W_{A_k}, so h is close to {h_i = 0} ∩ F_k, which is the crossing ray w_{ik}. This is Hor_{ik}.
- Take N′ = ∪ C_r ∪ ∪ W_{A_k}.

*Proof of (a).*
1. Let h⁰ be a density point of Θ_i ∩ D. Then a := h⁰_i > 0 and P₀ := P_T(h⁰) > 0. Put η = min(a, P₀)/4.
2. Choose d ≥ 0 with d_i = 0, d ≠ 0, generic. Along g(t) = h⁰ − η𝟙 − t d:
   - P_T is strictly decreasing (T ⊆ int Δ);
   - g(0) ∈ D;
   - g(t) leaves D at a point w″ with w″_i = a − η ≥ 3a/4.
   - For generic d, w″ lies in the relative interior of a facet F_k, or in some C_r. (Directions that hit a corner ray form a null set.)
3. Take x⁰ just beyond w″ on the path, at depth σ ≪ (τ/2)x⁰_i, with a ball B around x⁰ that lies in (W_{A_k} ∪ C_r) ∖ cl D and in the region σ < (τ/2)h_i.
   - On B, Θ_i is null: by Lemma OT, or because B ⊆ C_r.
   - The advice ranges of points of B contain + and 0 (they lie in N), and these points have h_i > 0.
   - So a.e. point of B lies in S_i, and (perturbing x⁰) x⁰ is a density point of S_i.
4. Every h ∈ B(h⁰, η/2) satisfies h ≥ x⁰, since x⁰ = h⁰ − η𝟙 − t′d.
5. Lemma DL then makes Θ_i ∩ B(h⁰, η/2) null, contradicting the choice of h⁰.

There is no circularity. Lemma OT uses inner acceptance of G for both tied and strict z (F2a, F0); it does not use (a). ∎

*Remarks.*
- (a) is global on D. A tie deep inside D is killed by the strict shallow exterior points below it, reached by lowering coordinates other than i.
- NT uses only interior priors on the cevian (δ_i, p\*) and near δ_i, plus the target prior. (S), (C), (IB) and boundary priors are not used.

---

## 5. Vertex anchoring

**Theorem V′ (PROVED).** Assume (H), T = T1, θ < Θ_NT, and let D_V be a coherent e_i-Bayes model. One exists under (LA), (S) by R1 Lemma 1.3(a). Then e_i ∈ V, i.e. D_V ⊆ {h_i > 0}.

*Proof.*
1. *Setup.* Fix k ≠ i and w = w_{ik}. Then w^⊥ ∩ aff Δ = line(e_i, v_k). Near w, inner points are a.e. untied (NT(a)), so:
   - for inner h near w with h_i > 0, accepting is the unique best advice in the advice range at e_i, so every e_i-Bayes model accepts h;
   - for inner h near w with h_i < 0, silence (in the advice range by (LF)) is strictly better, so every e_i-Bayes model rejects h.

   By (F1) and openness, D_V contains every inner h near w with h_i > 0 and no inner h near w with h_i < 0.
2. *Normal form.* Take n ⊥ e_i with v_k·n = 1. For c > v_{k,i} and small δ > 0, the point h_δ = w + cδ·n − δe_i is inner (P_T(h_δ) = cδ − δv_{k,i} > 0) and has (h_δ)_i = −δ < 0. So min_{m∈V} m·h_δ ≤ 0.
3. *Limit.* Divide by δ and let δ → 0 along a subsequence of minimisers m_δ → m\*. Since V ⊆ {m·w ≥ 0}, this gives m\*·w = 0 and c·m\*·n ≤ m\*_i.
4. *Parametrise the line.* Write m\* = (1−a)e_i + a·v_k with a ≥ 0 (points with a < 0 leave Δ). Then m\*·n = a and m\*_i = 1 − a + a·v_{k,i}, so a ≤ 1/(c + 1 − v_{k,i}).
5. *Conclusion.* Let c → ∞. Compactness of V gives e_i ∈ V. ∎

*Consequences.*
- R10b Cor V1 holds: gambles accepted by every evaluable model are (a.e.) nonnegative.
- R10b Lemma FS holds.
- R10a Thm V holds, with N replaced by its inner part.
- The coordinator's claim in BRIEF4 is **true**. Its sketch is **not** valid as written: "outer band points near a crossing with h_i > 0 are strict (by Prop L)" fails in the horns.

---

## 6. Transfer of the strict no-gos (PROVED by re-checking each use of strictness)

**Corollary TR.** For T1 under permitted NSI_θ with θ < Θ_NT, either norm:
- (i) R15 Thm 1(a)–(d), Lemma 3.2, Lemma 6.1 and Thm 6.2 hold verbatim. No realisation has (DF), (ND) and (NA_w) at p\*.
- (ii) N3 Thm PL_θ holds for θ < θ_A(T1): no plateau. Here θ_A = min{1, (1+2ε)/(2(1−ε))} (sup) or N3's Euclidean formula.

*Check of (i).* Each strictness input of R15 (R18 table), and how it survives:
- Lemma C and Thm 1(a), (b), (d) use no strictness. Weak signs suffice for Lemma C's non-constancy.
- Thm 1(c):
  - The crossing equation ĉ_i(w) = 0 needs only the weak signs from both sides.
  - λ_{ik} > 0 needs UVN(a) at one point of relint F_k off ker Γ_k with h_i > θ‖h‖. That point exists by (T-ii), since the off-band arc is open and ker Γ_k is at most a ray.
  - UVN(a) needs a strict ball B₀, which exists off-band in N.
- Lemma 3.2 uses the strict sign from (c), which is available.
- Lemma 6.1:
  - The Λ-signs are first-order: c_k(w)_a = λ_{ak}w_a with λ_{ak} > 0 from (c).
  - The witnesses are accepted via unique clusters plus (NA_w), with no strictness.
  - The forbidden-support step (Lemma FS) needs V1, which Theorem V′ supplies. Its own strictness is "bad is strictly worse than silence", which is unchanged.
- Thm 6.2 Steps 1–6 are algebra.
- Horns accumulate only at the crossing rays w, where the unique cluster is the cevian through e_i and p\* (ĉ·e_i = ĉ·p\* = 0), so they are consistent with Thm 1. Ties near other facet points are null (NT). Nothing else is affected.

*Check of (ii).* N3 PL_θ uses strictness only at off-band points (w₊ and the arc A, where j leads), plus "bad is strict". UVN(b) inside N does not need V1, because (LF) ensures that the evaluable models never all give the same advice there. Permitted ties are a subset of the forced ties N3 allowed for. ∎

*Remark (direct DF argument).* Even without NT, (DF) alone excludes ties accumulating at a facet point h with h_i ≠ 0 and Γ_k h ≠ 0. Tied clusters have ĉ_i = 0, while Γ_k h·(e_i − p\*) = λ_{ik}h_i ≠ 0, and the cluster is unique. NT is needed only for Theorem V′, i.e. inner strictness tangentially at the crossings.

---

## 7. Designs tried (NUMERICS; `n6py/designs.py`, `dl_certificate.py`, `horns*.py`)

**Common tests.** Chart fields c(h) with charts for advice range {+,0,−} (accept h iff c(h)·q > 0 and c(h)·q > c(−h)·q). Priors: 118 test priors (an interior grid, near vertices, near edges, cevians i–u), plus 48 tilted near-vertex priors in the horn runs. At each prior:
- (G)-sign check, permitted reading, sup norm;
- B_u versus the intended target;
- double acceptance;
- midpoint convexity;
- upward closure (x ∈ B_q, h = x + d with d ≥ 0, should give h ∈ B_q).

| design | idea | result |
|---|---|---|
| S0: R10a 9-gon (W = T1(.29), a/b = .01), strict | sanity | 0 violations, 0 ties |
| S1: S0 + inner ties near the crossings of K_u, value at u preserved (θ = .2) | design (a): ties on the inner side | B_u unchanged. 22 midpoint and 99 upward violations, concentrated at near-vertex priors. DL certificates: 136 of 400 tied samples, e.g. h = (.069, .912, −.405) tied at 1, x = h − d strict, q = (.99, .0002, .0098): x accepted, h rejected |
| S2: T1-exact field Ψ = (1−ε)h + ε·min h·𝟙; NAL sign violators: inner band → cevian tie (c_i = 0, deficit moved to a negative coordinate); others → strict repair; ε = .3, θ = .45 | design (a)/(b): exact target, all-model domain, ties exactly at the crossings, inner side | (G) exact, B_u = D_{T1} exactly. 3496 midpoint and 2194 upward violations; worst near vertices and near edges. DL certificates: 373 of 400 |
| S2s: S2 with strict repair everywhere | strict analogue | also fails (3241 / 1794) |
| S4: S0 + ties on all outer band points | outer ties | 30 midpoint violations in crossing-targeted tests (Lemma OT) |
| S3: S0 + ties only in outer horns (C = 1, 5) | the loophole left by NT | passes the cevian-ray tests. Fails at a few priors (12 midpoint violations, genuine margins 1.7e−3 to 8.4e−3, every violator tied; `horn_diag.py`) |

**Reading.**
- S1 and S2 fail exactly as Lemma DL predicts: the certificates are tied h ≥ strict x at tilted near-vertex priors.
- S2s shows that the T1-exact repair is hopeless with or without ties. The NAL obstruction is behind that, not ties.
- S3: naive horn surgery is incoherent. This is evidence, not proof, that horns are not freely usable.
- Random global sampling barely hits tie sets (S1: about 2·10³ tied entries in 9·10⁵). Crossing-targeted sampling is needed (`horns_targeted.py`).

**Thresholds.** `theta1.py` reproduces the facet maxima and corner values (N6.7) for ε ∈ {.05, .1, .3, .5, .6, .9}. It also confirms h_k < 0 on F_k (max φ_k ≈ −0.03 to −0.39) and that the corner rays lie on both facets.

---

## 8. Horns (the only residual tie freedom near ∂D)

What is known about horn ties Θ_i ∩ Hor_{ik}:
- (i) DL constrains them. Within N ∩ {x_i > 0}, everything below a horn tie must be tied or have its acceptance outside the advice range a.e. The horn shape {0 < h_i ≤ C·depth} is down-closed, so DL alone does not exclude horns. (CHECKED)
- (ii) Their charts are cevian half-planes {q_j/q_k > ρ(h)} with ρ(h) > p\*_j/p\*_k. As h → w_{ik}, these charts must converge to clusters consistent with Lemma C. Under (DF) the cluster at w_{ik} is exactly the cevian through e_i and p\*, so horns are consistent with first-order data. (CHECKED)
- (iii) They do not affect Theorem V′ or Corollary TR. (PROVED, §§5–6)
- (iv) A strict design can approximate a horn chart (c_i small and positive), so horns add at most an exact-pencil limit to the strict problem.

CONJECTURE N6: under (H), horn ties are null. Or at least, any realisation with horn ties can be replaced by one without them.

What I tried for the conjecture: tilted priors near δ_i (the DL mechanism), and upward closure from horn points to shallow strict points. Neither yields a contradiction, because horn points are only rejected on one side of a cevian and nothing forces their acceptance there.

---

## 9. Scope, other tie rules, other targets

- **Other good~silence tie rules (CHECKED).** DL, OT and NT never use the band's shape. They use:
  - (α) strictly guided points, with acceptance in the advice range, cutting each facet contact, at world i, near the i-positive part of every facet (here: off-band points);
  - (β) no tie-eligible points near corner rays;
  - (γ) bad is strictly worse than silence.

  Any rule of the form "good~silence permitted on a set R_i, strict elsewhere" with (α) and (β) gives NT for T1. For example the down-closed "negative-part band" {0 < h_i ≤ θ‖h⁻‖} does. To escape, a rule must permit ties on the whole outer side of a facet's i-positive region, large stakes included. That conflicts with strictness for non-negligible stakes.
- **Interior polytopes, n = 3 (CHECKED).** The same proofs work with Θ_NT(K) = the minimum, over corner rays r with r_l > 0, of φ_l(r), together with max_{cl F_v} φ_i over facets meeting {h_i > 0}. This is positive for every interior polytope. Theorem V′ needs a crossing of i on some facet whose inner side near it is untied; that holds by NT(a).
- **Smooth or curved targets.** Not claimed. OT's cutting point x needs a flat facet; for strictly convex boundaries the contact moves with w, and a thin N may leave no cutting point.
- **n ≥ 4.** DL is dimension-free. OT/NT need the corner analysis for lower-dimensional faces. Not claimed.
- **θ ≥ Θ_NT.** Not treated. Sup norm: only θ ≥ 1, where every mixed problem is band. Euclidean: the window [Θ_NT, 1).
- **Non-additive (IB) rankings.** Nothing claimed.
- **Closed choice.** Not reached. No design survived to the point where CCIBU or N3 Thm CC_θ would be needed.

---

## 10. Scripts (`n6py/`)

| file | content |
|---|---|
| `theta1.py` | Θ₁ / Θ_NT for T1, both norms: sampled, 1-d grid, and closed forms; checks on the corner rays |
| `designs.py` | chart-field framework; systems S0, S1, S2, S2s; (G), double-acceptance, midpoint and upward tests over 118 priors |
| `dl_certificate.py` | explicit Lemma DL certificates in S1 and S2 |
| `horns.py`, `horns_targeted.py`, `horns_allpriors.py`, `horn_diag.py`, `horns_allpriors.out` | horn designs S3 and S4; crossing-targeted tests; margin diagnostics |
