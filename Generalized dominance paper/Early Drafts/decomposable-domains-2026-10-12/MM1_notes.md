# MM1 (round 41, BRIEF33). Strict quorum competitiveness (QS): what the judges must look like, and why the natural geometries fail

18 Oct 2026. Rules of BRIEF13 and BRIEF33. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named, with their recorded status.
- **CHECKED**: exact rational (or exact symbolic) computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: marked as such.

Scripts are in `mm1py/`. Run `python3 -I <script>.py` from inside that folder. Outputs are in `*.out`. Each ends with `ALL CHECKS PASSED`.
- `mincell_check.py` → `mincell_check.out` (Fractions; ε ∈ {1/10, 3/10, 1/2});
- `helly_check.py` → `helly_check.out` (Fractions; exhaustive 1D part, random exact 3D part);
- `covariance_check.py` → `covariance_check.out` (sympy identity, plus Fractions).

Setting: the write-up §2, AUDIT_LL and BRIEF33. Three worlds; the full four-advice domain (so (LF) at T1 is automatic); μ standard Gaussian; T1 = D_K, K = (1−ε)u + εΔ, c₀ = (1−ε)/3, v_k = c₀𝟙 + εe_k. At each world i there are n = 4 strictly guiding integrable additive judges ℓ_iv, quorum q = 3. A branch at p is a choice F = (F_i)_{i∈supp p} of a pair F_i of judges at each active world. No assumption is added. Every extra hypothesis is a hypothesis of the result that states it.

---

## 0. Outcome

**No cover of T1 was constructed.** I did not find judges and a coherent family satisfying (QS), and I prove that the natural judge geometries cannot work. The single mechanism behind every exclusion is the same. Two **disjoint** blocking pairs exist at every world. When the representations of a selected model are rigid, these disjoint pairs force two judges at each world to coincide, and the quorum then behaves like one field. The condition 3q > 2n always produces disjoint blocking sets (Remark 3.3), so this mechanism is not an artefact of n = 4.

What is PROVED (all PROVED results are written out in §§1–5):

1. **Exact sign form (§1).**
   - The certificate is a pointwise sign problem in the judges' accept/silence switch values σ_iv(g), where g is an oriented gamble and σ_iv(g) has the strict sign of g_i (Lemma 1.1).
   - Every family of such switch values is realised by strictly guiding integrable judges.
   - (QS) at p implies, in every branch, that C_p is a pointwise **weak** Bayes model of a nonnegative mixture of that branch (Lemma 1.2; the η = 0 case of LL2 Lemma 2.1).
   - Vertex models are forced to be W_i = {g_i > 0}, and they pass (Lemma 1.3). T1 can be selected only at interior indices (Lemma 1.4).
2. **Kinks forbid analytic judges (§2).**
   - At a corner ray of a selected model, no branch mixture with real-analytic switch values can certify the model. Under weak Bayes, such a mixture must vanish identically near the ray (Proposition 2.1).
   - The plain posterior family moves its kinks over every direction of the open two-negative orthants (CHECKED). So, for every branch, its judges are non-analytic on a dense set there (Corollary 2.2).
   - **Monomial judges** make certification invariant under the posterior (coordinate-scaling) action. They would transport one certified model to its whole posterior orbit (Lemma 2.3). But they are analytic, so they never certify T1 (Corollary 2.4).
3. **Pair-Helly rigidity (§3).** Suppose the representations of a model are linear in a parameter d and each branch pair gives a two-generator cone in d-space. If all 216 triples of cones meet, then:
   - at every world the four judges are coplanar, with a **doubled** middle ray;
   - the doubled rays of the three worlds coincide (Lemma 3.1; 1D part CHECKED exhaustively, 3D part CHECKED on random exact instances).
4. **Doubled judges kill (QS) (Proposition 3.2; PROVED modulo FF2 Thm 4.1's import chain).** If every world has two judges with proportional penalty differences, (QS) fails for every coherent selection that is continuous in measure and passes through T1. So **some world must have four pairwise non-proportional judges.**
5. **Cellwise-linear judges (§4).**
   - On any finite fan, at a selected model where all 216 branches are weakly Bayes, the quorum reduces on the pinned cells to a **single field** made of the doubled judges (Theorem 4.1).
   - **Theorem 4.2 (self-contained, no imports):** suppose the switch values are linear on the three min-cells M_k = {g_k minimal} near ∂D_{T1}. This is the class that contains T1's own canonical field. Then (QS) fails for **every** coherent selection that is continuous in measure and passes through T1.
   - In that class, T1 **alone** satisfies (QS) against every X, with heterogeneous judges and all 216 branches certified (CHECKED, Part A). Every neighbouring triangle model fails some branch (CHECKED, Part B).
   - For a general fan, every selected model near T1 coincides, on the cells pinned by T1, with one plain-posterior model C_μ (Corollary 4.3).
6. **Rank-2 worlds (§5).** Suppose each world's switch values span a 2-dimensional space. Then each interior selected model C needs a relation space R(C) of dimension at least 2 on ∂C (Proposition 5.1).

**Cycles.** For n = 4, q = 3 the Nakamura number is 4 (LL3 Theorem A, imported).
- (TC) holds, so there are no strict 3-cycles.
- Strict k-cycles of distinct models can occur for every k ≥ 4.
- No construction was obtained, so no cycle is exhibited here.

**Single most important open point.** Does any measurable judge geometry escape the Helly rigidity of §3? Such a geometry must give each selected model C_p a representation set that is not a one-parameter (per-world ray) family. Concretely, the restrictions of the branch switch values to ∂C_p must satisfy enough linear relations: dim R(C_p) ≥ 2 in rank-2 designs, with every world's projection injective. The judges must also be non-analytic at every selected kink, and not cellwise linear near T1. No such design is known. Whether one exists decides (QS) for T1.

---

## 1. The sign form, the necessary weak-Bayes condition, vertices

### 1.1 Switch values

For an oriented gamble g (off the coordinate planes) and a judge (i,v), put

  σ_iv(g) := ℓ_iv(pair of g, silence) − ℓ_iv(pair of g, "accept g only").

On H this is c_iv(g) in the write-up's notation. On −H it is c′_iv(−g). By strict guidance, σ_iv(g) has the strict sign of g_i.

**Realisation (PROVED).** Let σ_iv be bounded measurable functions with sgn σ_iv(g) = sgn g_i a.e. Define, for h ∈ H:
- ℓ(h,0) := 0;
- ℓ(h,+) := −σ(h);
- ℓ(h,−) := −σ(−h);
- ℓ(h,×) := max(−σ(h), −σ(−h)) + |h_i| + 1.

This penalty is strictly increasing in world-i rank. Where h_i > 0 the order is + < 0 < − < ×; where h_i < 0 it is − < 0 < + < ×. Its envelope is integrable for the Gaussian μ. So every such family σ is a judge field.

**Lemma 1.1 (sign form; PROVED).** Let C = D_K with K a credal set, and let α ≥ 0 be nonzero on the judges of a branch. Write Σσ := Σ α_iv σ_iv.

(a) C is the unique pointwise minimiser of the mixture (the certificate of BRIEF33) iff, for a.e. oriented g:
- if C accepts g: Σσ(g) > 0 and Σσ(g) − Σσ(−g) > 0;
- if C is silent on {g, −g}: Σσ(g) < 0 and Σσ(−g) < 0.

(b) In particular, **sgn Σσ(g) = sgn P_K(g) for a.e. g** suffices.

(c) C is a pointwise **weak** minimiser iff the same holds with ≥ and ≤ in place of > and <.

*Proof.*
- × is strictly worst for every judge, so it is never a minimiser of a nonzero nonnegative mixture.
- On {+, 0, −} the three comparisons are exactly the displayed differences (write-up §2.4: charts via c, c′, d = c − c′).
- For (b): if P_K(g) > 0 then P_K(−g) < 0. So Σσ(g) > 0 > Σσ(−g), which gives both accept conditions. A silent pair has P_K(±g) ≤ 0, which is < 0 a.e. ∎

So the certificate problem is purely a problem about signed functions: find, for each p and branch F, α ≥ 0 on F with Σ_F α σ ≍ P_{K_p} in sign. The weights may depend on (p, F) but not on g.

### 1.2 The necessary condition

**Lemma 1.2 (PROVED; LL2 Lemma 2.1 and Prop 8.3 with η = 0).** If (QS) holds at p, then for every branch F at p, C_p is a pointwise weak Bayes model of some nonnegative nonzero mixture of the judges of F.

*Proof.*
1. The attainable set Z := {(N_iv(C_p, X))_{(i,v)∈F} : X a model} is convex by Lyapunov. This is FF2 Step 1, refereed in GG3 §8.1. It contains 0.
2. Suppose some X had N_iv < 0 for all (i,v) ∈ F. Then X ≠ C_p. At each active world at most 4 − 2 = 2 < q judges would strictly prefer C_p, contradicting (QS). So Z misses the open negative orthant.
3. Separation gives α ≥ 0, α ≠ 0, with α·z ≥ 0 on Z.
4. Switching C_p to a better advice on a non-null set would make α·z < 0. So the weak inequality holds pointwise. ∎

### 1.3 Vertices and the position of T1

**Lemma 1.3 (PROVED).**
- (QS) at e_i forces C_{e_i} = W_i := {g : g_i > 0}, which is D_{{e_i}} and hence coherent.
- Conversely, W_i satisfies (QS) at e_i, and any single world-i judge certifies it.

*Proof.* If C ≠ W_i, every world-i judge strictly prefers W_i to C, because W_i is pointwise world-i best and strictly better on a non-null set. Then no world-i judge strictly prefers C, and (QS) fails against X = W_i. The converse is the same observation read in reverse. ∎

**Lemma 1.4 (PROVED).** If (QS) holds at p and C_p = T1, then p ∈ int Δ.

*Proof.*
- At an edge index, say supp p = {1,2}, Lemma 1.2 gives a weak Bayes mixture of world-1 and world-2 judges only.
- Gambles near (1,1,−t), with t slightly above 2c₀/(c₀+ε), form an open set outside cl D_{T1}, where T1 is silent.
- There "accept" is strictly better at worlds 1 and 2 for every judge. So the mixture strictly prefers acceptance, which contradicts weak Bayes.
- At a vertex, Lemma 1.3 gives C = W_i ≠ T1. ∎

---

## 2. Kinks forbid analytic judges; posterior covariance cannot start at T1

**Proposition 2.1 (PROVED).** Let C = D_K be selected at p, with K two-dimensional. Let r be a corner ray of D_K, where two facets with normals n₁ ≠ n₂ in K meet. Let F be a branch whose switch values σ_iv ((i,v) ∈ F) are real-analytic on a neighbourhood of r in ℝ³∖{0}. Then:
- (a) no mixture of F certifies C;
- (b) if a mixture α of F makes C a weak Bayes model, then Σ α σ ≡ 0 on a neighbourhood of r.

*Proof.*
1. **Local picture.** Near x₀ ∈ r, D_K = x₀ + W with W := {y : n₁·y > 0, n₂·y > 0}, an open dihedral wedge of angle < π.
   - Outside cl D_K near x₀ the pair is silent. Indeed −g ∉ D_K there, because \bar P_K(x₀) > 0 = P_K(x₀) when K is two-dimensional.
   - Put Φ := Σ α σ, which is analytic near x₀.
   - Certification gives Φ > 0 on x₀ + W and Φ < 0 on the open complement (Lemma 1.1(a)). Weak Bayes gives ≥ and ≤ (Lemma 1.1(c)).
2. **Leading term.** Suppose Φ ≢ 0 near x₀ (this is automatic in (a)). Let P_k be the lowest nonzero homogeneous term of its Taylor expansion at x₀. Then P_k ≥ 0 on W and P_k ≤ 0 on the complement.
   - **k even.** −W lies in the complement, so P_k ≤ 0 there. But P_k(−y) = P_k(y) ≥ 0. Hence P_k = 0 on the open set −W.
   - **k odd.** S := {n₁·y > 0 > n₂·y} and −S both lie in the complement, so P_k ≤ 0 on both. Oddness then gives P_k = 0 on S.
   - In both cases the polynomial P_k vanishes on an open set, so P_k ≡ 0. This is a contradiction.
3. Hence Φ ≡ 0 near x₀. That contradicts the strict signs in (a), and it is the claim in (b). ∎

**Corollary 2.2 (PROVED; sweep CHECKED, `covariance_check.out` (b)).** Consider the plain posterior family C_p = {g : p⊙g ∈ D_{T1}}.
- Its corner rays p^{−1}⊙r_kj, as p ranges over int Δ, cover every direction of the three open two-negative orthants. For r_12 = (−1, −1, κ+1) the target (−a, −b, c) is reached at p ∝ (1/a, 1/b, (κ+1)/c).
- So, if this family satisfies the certificate at all interior p, then for every branch F and every open set U of two-negative directions, some judge of F has a switch value that is not analytic on U.
- Under (QS) alone (weak Bayes), suppose a branch's judges are analytic on U. Then the branch's mixture at every C_p with a kink in U vanishes identically near that kink.

**Lemma 2.3 (monomial judges are posterior-covariant; PROVED; identity CHECKED, `covariance_check.out` (a)).**
- **The class.** Let each switch value have the form σ_iv(g) = sgn(g_i) · a_iv(sgn g) · Π_j |g_j|^{e_ivj}, where:
  - Σ_j e_ivj = 1, which makes σ_iv homogeneous of degree 1;
  - e_ivj > −1, for integrability;
  - a_iv(·) > 0 is constant on each orthant;
  - the same exponents are used for g and for −g.
- **Covariance.** Then σ_iv(p⊙g) = (Π_j p_j^{e_ivj}) σ_iv(g) for every p > 0.
- **Consequence.** Suppose α certifies C in branch F (or makes it weakly Bayes). Then α^p_iv := α_iv Π_j p_j^{e_ivj} does the same for C^{(p)} := {g : p⊙g ∈ C} = D_{ν(p⊙K)} (EE2 Prop 2.3a). So the set of models certified in a branch is invariant under the posterior action.

*Proof.* The scaling identity is immediate; both σ(g) and σ(−g) scale by the same factor. Then Lemma 1.1 applies to the rescaled mixture, pointwise in g. ∎

**Corollary 2.4 (PROVED).** Monomial judges are real-analytic on every open orthant. T1 has its corner rays r_kj inside the open two-negative orthants. So, by Proposition 2.1, no branch of monomial judges certifies T1 or any model in its posterior orbit.

The covariance mechanism would turn **one** all-branch certificate into a whole family over the open simplex. It is blocked exactly at T1, and only by T1's kinks.

---

## 3. The pair-Helly lemma, and why doubled judges are fatal

**Lemma 3.1 (pair-Helly rigidity; PROVED; CHECKED in `helly_check.out`).**
- **Setting.** Let m ≥ 2. For each i ∈ {1,2,3}, let a_i1, …, a_i4 ∈ ℝ^m∖{0} lie in an open half-space H_i. For a pair P = {v,w} put σ_i^P := cone(a_iv, a_iw).
- **Hypothesis.** For every choice (P₁, P₂, P₃) of pairs, σ₁^{P₁} ∩ σ₂^{P₂} ∩ σ₃^{P₃} ≠ {0}.
- **Conclusion.**
  - (a) For each i, the four a_iv span at most a plane.
  - (b) Ordered by angle in that plane, the second and third are positively proportional. Call their common ray z_i, the *doubled ray*.
  - (c) z₁ = z₂ = z₃.

*Proof.*

**Step 1 (each world's six cones share a ray).** Suppose world 3's six cones have no common nonzero point. Take any P₁, P₂ and put X := σ₁^{P₁} ∩ σ₂^{P₂}.
- If X were a single ray ρ, it would contain every triple intersection, so ρ would lie in every σ₃^{P₃}. That is a contradiction.
- So X ≠ {0} is not a ray. Hence σ₁^{P₁} and σ₂^{P₂} are both two-dimensional and span one plane L. This holds for all pairs, so all a_1v and a_2v lie in L, inside the open half-plane L ∩ H.
- Order the rays in L by angle: x(1) ≤ … ≤ x(4) for world 1 and y(1) ≤ … ≤ y(4) for world 2. Two-dimensional overlaps are nondegenerate interval overlaps. So [x(1),x(2)] ∩ [y(3),y(4)] gives y(3) < x(2), and [x(3),x(4)] ∩ [y(1),y(2)] gives x(3) < y(2).
- Then x(3) < y(2) ≤ y(3) < x(2) ≤ x(3), which is a contradiction.
- By symmetry every world's six cones share a nonzero point z_i.

**Step 2 (coplanar, doubled).**
- Suppose three of the a_iv are independent, say a₁, a₂, a₃. Then z_i ∈ cone(a₁,a₂) ∩ cone(a₁,a₃) ⊆ ℝa₁, so z_i = s·a₁ with s > 0. Also z_i ∈ span(a₂,a₃), so a₁ ∈ span(a₂,a₃). This is a contradiction.
- So the rank is at most 2. In the plane, a common point of all six angular intervals [x(v), x(w)] needs x(3) ≤ x(2), hence x(2) = x(3).
- The intersection of the six intervals is then exactly that ray.

**Step 3 (common).** The branch P_i = {(2),(3)} at every world has the rays z_i as its cones. They must meet, so z₁ = z₂ = z₃. ∎

*Checks.*
- 1D, exhaustively: for two worlds with four points each in {0,…,5}, all pair-intervals intersect across worlds iff x(2) = x(3) = y(2) = y(3). The same holds for three worlds. These are 15 876 and 74 088 configurations.
- 3D, random exact instances (40 of each kind): the 216-branch condition fails for generic, for coplanar-undoubled and for doubled-with-distinct-rays configurations. It holds for doubled-with-common-ray configurations.

**Proposition 3.2 (PROVED modulo FF2 Theorem 4.1 Steps 2–6 and their import chain: D1, BB2 Thm 6.1, M3.7–3.8; FF2 refereed in GG3 with the Cor 4.3 repair).**
- **Hypothesis.** At every world i there are two judges v_i ≠ w_i with proportional penalty differences: ℓ_{iw_i}(h,a) − ℓ_{iw_i}(h,b) = ρ_i (ℓ_{iv_i}(h,a) − ℓ_{iv_i}(h,b)) for a constant ρ_i > 0, for all advices and a.e. h.
- **Conclusion.** No coherent selection that is continuous in measure on Δ and passes through T1 satisfies (QS).

*Proof.*
1. Take the branch F* := ({v_i, w_i})_i. By Lemma 1.2, at every p the model C_p is a pointwise weak Bayes model of a mixture of F* supported on supp p.
2. Up to terms constant in the advice, that mixture is Σ_i (α_{iv_i} + ρ_i α_{iw_i}) ℓ_{iv_i}. So C_p is a weak Bayes model of the fixed, integrable, strictly guiding field ℓ* := (ℓ_{1v₁}, ℓ_{2v₂}, ℓ_{3v₃}) at a weight in Δ_{supp p}.
3. This is exactly the output of FF2 Theorem 4.1, Step 1. Steps 2–6 use only that output, continuity in measure, T1 selected, and (H2) for ℓ*. They give a contradiction. ∎

Hence **(QS) needs at least one world whose four judges are pairwise non-proportional.** The same argument excludes any (n, q) design in which every world has n−q+1 mutually proportional judges.

**Remark 3.3 (PROVED).** Under 3q > 2n with n ≥ 2, every world has two disjoint blocking sets of size n−q+1, since 2(n−q+1) ≤ n.
- For n ≤ 5 this follows by inspecting q = ⌊2n/3⌋+1: (2,2), (3,3), (4,3), (5,4).
- For n ≥ 6, 2q > 4n/3 ≥ n+2.

Lemma 3.1 is the n = 4, q = 3 instance. The same proof works for q = n−1 and any n ≥ 4: replace x(2) = x(3) by x(2) = … = x(n−1). I do not claim the version for blocking sets of size ≥ 3.

---

## 4. Cellwise-linear judges

**Setting.**
- 𝒜 is a finite family of disjoint open polyhedral cones (cells) whose union is co-null. N is an open cone.
- A judge is *cellwise linear on N* if σ_iv(g) = κ_iv(Q) g_i for g ∈ Q ∩ N, with constants κ_iv(Q) > 0.
- For a selected model C = D_K, a cell Q is *pinned* if ∂D_K ∩ Q ∩ N contains a relatively open two-dimensional piece. Write P(C) for the set of pinned cells.

**Theorem 4.1 (PROVED).**
- **Hypotheses.** Let C = D_K with K ⊆ int Δ two-dimensional, ∂D_K∖{0} ⊆ N, and suppose that in all 216 branches C is a weak Bayes model of a branch mixture.
- **Conclusion.**
  - (a) For each world i, the vectors κ_iv|_{P(C)} ∈ ℝ^{P(C)} (v = 1, …, 4) are coplanar with a doubled middle ray z_i. Two judges at world i are proportional on the pinned cells.
  - (b) There are λ ∈ ℝ³_{>0} and d ∈ ℝ^{P(C)}_{>0} with n^Q_i d_Q = λ_i z_i(Q) for every Q ∈ P(C) and every i, where n^Q ∈ K is the normal of ∂D_K in Q.
- **In words.** On its pinned cells, C is the Bayes model, at world weights λ, of the single cellwise-linear field formed by the doubled judges.

*Proof.*
1. **The mixture on one cell.** Fix a branch and its weak Bayes mixture α. On Q ∩ N the mixture's switch value is Σασ(g) = ω^Q·g with ω^Q_i = Σ_{v∈F_i} α_iv κ_iv(Q).
2. **Weak Bayes near the boundary.** Near ∂D_K, C is silent outside cl D_K, because K is two-dimensional (proof of Proposition 2.1). So weak Bayes reads ω^Q·g ≥ 0 inside and ≤ 0 outside (Lemma 1.1(c)).
3. **Every world is used.** Suppose some world had α_i· = 0. Then ω^Q_i = 0 for every Q, while the normal n^Q ∈ K ⊆ int Δ has n^Q_i > 0. So the weak Bayes signs fail near a pinned piece. Hence every ω^Q has all coordinates > 0.
4. **Normals.** On a pinned piece, ω^Q·g = 0 by continuity from both sides. The piece spans its plane, so ω^Q = d_Q n^Q with d_Q > 0. Here n^Q ∈ K is the facet normal: a planar boundary piece of D_K has an exposed point of K as its normal.
5. **Reduction to Lemma 3.1.**
   - Row i of the matrix (ω^Q_i) is Ω_i = A_i d, with A_i := diag(n^Q_i)_{Q∈P(C)} invertible and positive.
   - Ω_i ∈ cone(κ_{iF_i}|_{P(C)}). So, for every branch, d ∈ ∩_i A_i^{−1} cone(κ_{iF_i}|_P), and d > 0.
   - The generators A_i^{−1} κ_iv|_P are positive vectors, so they lie in an open half-space.
6. **Conclusion.**
   - Lemma 3.1 applies in ℝ^{P(C)}. The linear bijection A_i^{−1} preserves coplanarity and the angular order up to reversal, which gives (a).
   - It also gives a common ray d* ∝ A_i^{−1} z_i for all i, i.e. A_i d* = λ_i z_i, which is (b). ∎

**Theorem 4.2 (PROVED; self-contained).**
- **Hypotheses.** Use the three min-cells M_k := {g : g_k < g_j for j ≠ k}. Suppose every judge is cellwise linear on these cells on some open cone N ⊇ ∂D_{T1}∖{0}. Away from N the judges are arbitrary strictly guiding integrable judges.
- **Conclusion.** No coherent selection p ↦ C_p, continuous in measure on Δ with T1 = C_{p₀}, satisfies (QS). The weaker per-branch weak Bayes condition of Lemma 1.2 already fails.

This class contains T1's own canonical field: P_{T1}(g) = v_k·g on M_k (CHECKED, Part 0).

*Proof.*

**1. Classification near T1.** Let C = D_K with K Hausdorff-close to T1. (Measure-closeness of coherent cones is equivalent to Hausdorff closeness of credal sets; write-up Prop reduction(b), R1 Prop 3.1.) Then:
- K ⊆ int Δ is two-dimensional, and ∂D_K∖{0} ⊆ N.
- All three min-cells are pinned.
- If C is weak Bayes in some branch, then by Theorem 4.1 Steps 1–4, ∂D_K ∩ M_k lies in the plane (n^k)^⊥ for some n^k ∈ K.
- No two-dimensional piece of ∂D_K lies in a wall {g_k = g_j}: its normal would be ∝ e_k − e_j ∉ ℝ_+ K.
- So ∂D_K ⊆ ∪_k (n^k)^⊥, and K = co{n¹, n², n³}.
- The facet of n^k lies in cl M_k. So the corner ray ∝ n^k × n^j lies in {g_k = g_j}, which means the side [n^k, n^j] is parallel to e_k − e_j.
- Near T1 the n^k are distinct and near v_k. This forces K = {m ≥ c} with c > 0, t := 1 − Σc > 0 and n^k = c + t e_k. (The equalities n¹₃ = n²₃, n¹₂ = n³₂ and n²₁ = n³₁ define c, and normalisation gives a common t.)

**2. All-branch weak Bayes forces the doubled field.** If C is weak Bayes in all 216 branches, Theorem 4.1 gives z_i ∈ ℝ³_{>0}, the doubled ray of world i. Here P = all three cells, so z_i depends on the judges only. It also gives λ, d > 0 with (c_i + t δ_ik) d_k = λ_i z_i(k).

**3. That system has at most one solution c.**
- For k ≠ i: c_i d_k = λ_i z_i(k). This fixes d up to scale (d₂/d₃ = z₁(2)/z₁(3), d₁/d₃ = z₂(1)/z₂(3)).
- For k = i: t = λ_i (z_i(i)/d_i − z_i(k)/d_k). This fixes λ_i/t, hence c_i/t = β_i.
- Then t = 1/(1 + Σβ_i). So c is unique.

**4. Clopen argument.** Let E := {p : C_p = T1}. It is closed, by continuity, and nonempty.
- Let p₀ ∈ E. By Lemma 1.4, p₀ ∈ int Δ. For p near p₀, C_p is close to T1 and p has full support.
- (QS) and Lemma 1.2 make C_p weak Bayes in all 216 branches.
- By Steps 1–3, C_p is the unique triangle model of the doubled field. So is T1 = C_{p₀}, by the same steps with the same z_i. So C_p = T1.
- Hence E is open. Δ is connected, so E = Δ, which contradicts Lemma 1.3 at e₁. ∎

*Checks (`mincell_check.out`; ε ∈ {1/10, 3/10, 1/2}).*
- **Part 0.** P_{T1} = v_k·g on M_k, on 2000 exact samples.
- **Part A, (QS) at T1 alone, PROVED for an explicit heterogeneous design.**
  - Judges at world i: κ*_i := (c₀ + εδ_ik)_k, then κ*_i ± δτ_i (δ = c₀/2, τ_i = e_{i+1} − e_{i+2}), and 2κ*_i.
  - With d = (1,1,1), T1 is **certified in all 216 branches** (exact). By Lemma 1.1(b) this proves (QS) at T1 against every X, since sgn Σασ = sgn P_{T1} holds strictly on every min-cell.
  - The pair-normal system has rank 2, so d is unique.
- **Part B, the neighbours.** For 400 rational d ≠ 𝟙, the triangle model c(d) on the common-plane surface **fails at least one branch** (exact).
- **Part C, generic judges.** For 200 random generic min-cell judge sets, T1 itself fails at least one branch.
- **Part D, uniqueness.** The doubled field's unique triangle model is T1.

**Corollary 4.3 (PROVED; general fans near T1).** Take cellwise-linear judges on any finite fan, with N ⊇ ∂D_{T1}∖{0}, and suppose (QS) holds at an interior p₀ with C_{p₀} = T1. Then, for p near p₀, there is μ = μ(p) ∈ ℝ³_{>0} such that, on every cell pinned by T1, ∂C_p is the boundary plane of the plain posterior C_μ = {g : μ⊙g ∈ D_{T1}}.

*Proof.*
1. **Pinned cells persist.** For p near p₀, P(C_p) ⊇ P(T1). A cell containing a two-dimensional piece of ∂D_{T1} also contains one of ∂D_{K_p} when K_p is Hausdorff-close.
2. **Restricting to P(T1).** Apply Theorem 4.1 to C_p and restrict to P(T1). Coordinate projection keeps the doubled pair proportional.
3. **The same middle ray.** Lemma 3.1 at T1 says the configuration on P(T1) has x(2) = x(3), with at most one entry on each side. So the only ray carried by two judges there is the middle ray. Both C_p and T1 therefore use the same z_i on P(T1).
4. **The posterior.** Hence n^Q(C_p) ∝ λ⊙z^Q and n^Q(T1) ∝ λ*⊙z^Q, so n^Q(C_p) ∝ μ⊙n^Q(T1) with μ = λ/λ*. These are the facet normals ν(μ⊙v_k) of C_μ. ∎

So, near T1, cellwise-linear quorum designs have exactly the rigidity of a single field: the plain-posterior rigidity that FF1 and FF2 studied. The quorum's heterogeneity is invisible on every cell that T1 pins. I have not settled whether a general fan also fails globally. Near each corner it would need μ(p)^{−1}⊙r_kj on a wall, or extra small facets on cells not pinned by T1.

---

## 5. Rank-2 worlds: the representation space must be large

**Setting.**
- Suppose each world's switch values lie in a two-dimensional space of continuous functions: σ_iv = x_iv b_i1 + y_iv b_i2 on all of ℝ³∖{0}, with constants (x_iv, y_iv). Put V_i := span(b_i1, b_i2).
- For an interior selected C = D_K with K ⊆ int Δ two-dimensional, put R(C) := {(w₁, w₂, w₃) ∈ V₁ × V₂ × V₃ : Σ_i w_i = 0 on ∂C∖{0}}.

**Proposition 5.1 (PROVED; second part modulo the Proposition 3.2 imports).**
- (a) If (QS) holds at an interior p with C = C_p, then every branch has (u_i) ∈ R(C) with u_i ∈ cone(σ_{iF_i}) and u_i ≠ 0 at every world.
- (b) If dim R(C) ≤ 1 at some such p, then (QS) fails for every coherent selection that is continuous in measure and passes through T1.

*Proof.*
- **(a).**
  - Lemma 1.2 gives a weak Bayes mixture. Its world components u_i ∈ cone(σ_{iF_i}) satisfy Σu_i ≥ 0 inside D_K and ≤ 0 outside near ∂C. By continuity Σu_i = 0 on ∂C.
  - Suppose u_i = 0 for some world. ∂D_K meets the orthant where g_i < 0 < g_j, g_k, because P_K(−a, 1, 1) changes sign in a. There the other two components have strict positive sign unless they vanish. So all three would vanish, and α = 0, which is excluded.
- **(b).**
  - If R(C) = span(r), each branch uses ±r. Each world's cone is pointed, so the sign is the same for all branches.
  - So the ray of π_i(r) lies in all six pair cones of the two-dimensional, pointed V_i. By the 1D Helly step, two judges at world i are proportional, as elements of V_i and hence globally.
  - That holds at every world, and Proposition 3.2 applies. ∎

*Remark (not a claim).* Suppose dim R(C) = 2 and at least two of the projections π_i : R(C) → V_i are injective. Then the 1D argument of Lemma 3.1 Step 1, run inside R(C), again doubles those worlds. A rank-2 design therefore needs, on **every** interior selected boundary, a relation space of dimension ≥ 2 that is not of this kind, or of dimension ≥ 3. That means at least three independent linear relations among six fixed functions restricted to ∂C_p. The family {∂C_p} sweeps an open set of directions, and through a given direction the boundaries pass in varying tangent directions (for the plain posterior family, by Corollary 2.2). So a ratio σ_iw/σ_iv that is constant along every ∂C_p is locally constant, and the judges would be proportional. These relations must therefore come from a genuinely non-proportional coincidence structure, and none is known.

---

## 6. What a construction would need, and the nearby results

**Necessary features (PROVED above).** A coherent family through T1 with (QS) needs judges such that:
1. Some world has four pairwise non-proportional judges (Proposition 3.2).
2. The judges are not cellwise linear on the min-cells near ∂D_{T1} (Theorem 4.2). On a general fan they are single-field-rigid near T1 (Corollary 4.3).
3. The judges are not analytic near any kink of any selected model (Proposition 2.1). For the plain posterior family they must be non-analytic on a dense set of two-negative directions in every branch (Corollary 2.2). In particular the posterior-covariant monomial judges cannot be used (Corollary 2.4).
4. In rank-2 designs, the relation space on every interior boundary has dimension ≥ 2 (Proposition 5.1), and in effect ≥ 3 (Remark).
5. Every branch passes the exact nonstrict test of AUDIT_LL. This contains, for each branch, the weak-Bayes condition of Lemma 1.2.

**Structural reading.** In every geometry above, the set of representations of a selected model is linear in a parameter, with one ray per world per branch pair. Lemma 3.1 then turns the two disjoint blocking pairs into a doubled judge at each world, and the quorum collapses to one field. For a single field, the additive exclusions apply: Theorem gm, FF2 Theorem 4.1, and Theorem 4.2 here, which is self-contained in its class. An escape needs representation sets with at least two independent parameters per world at **every** selected model, including along every moving kink, which requires non-analytic judges there.

**Nearby results that are available.**
- (QS) at T1 alone, against every competitor, with heterogeneous judges and all 216 branches certified: PROVED (Theorem 4.2's Part A design). The compactness step of AUDIT_LL's lifting lemma, run at the single index p₀, then gives a positive margin function that makes T1 alone competitive. It is **not** a family, and Theorem 4.2 shows that no family extends it inside its class.
- Posterior families of **kink-free** base models are exactly where covariance works (Lemma 2.3). One all-branch certificate of a smooth coherent model C* would give certificates along its whole interior posterior orbit. I have not built such a heterogeneous certificate, and it would not reach T1.
- Additive covers of polygons arbitrarily close to T1 already exist (R10a Thm M). The quorum adds nothing to them in the geometries analysed here.

**Lifting lemma.** No family satisfying (QS) was found, so AUDIT_LL's lifting lemma (pending referee) is not invoked for a cover.

**Cycles.** These are imported from LL3 Theorem A.
- For n = 4, q = 3 the Nakamura number is ⌈n/(n−q)⌉ = 4. So there are no strict 3-cycles ((TC)), and strict k-cycles of distinct models are possible for every k ≥ 4.
- None is exhibited here, since there is no construction.

---

## 7. Status table

| Item | Statement | Label |
|---|---|---|
| 1.1 | certificate ⇔ pointwise sign conditions on switch values; sgn Σασ = sgn P_K suffices; realisation of any signed switch field | PROVED |
| 1.2 | (QS) ⇒ weak Bayes in every branch | PROVED (η = 0 case of LL2 2.1) |
| 1.3, 1.4 | vertex models forced and certified; T1 selectable only at interior indices | PROVED |
| 2.1 | no analytic branch mixture certifies a model at a kink; weak Bayes forces Σασ ≡ 0 there | PROVED |
| 2.2 | plain posterior kinks sweep the two-negative orthants; dense non-analyticity needed | PROVED; sweep CHECKED |
| 2.3, 2.4 | monomial judges are posterior-covariant, but never certify T1 | PROVED; identity CHECKED |
| 3.1 | pair-Helly rigidity | PROVED; CHECKED (1D exhaustive, 3D random exact) |
| 3.2 | a proportional pair at every world ⇒ (QS) fails | PROVED modulo FF2 Thm 4.1 Steps 2–6 imports |
| 3.3 | 3q > 2n ⇒ disjoint blocking sets | PROVED |
| 4.1 | cellwise-linear: all-branch weak Bayes ⇒ single doubled field on pinned cells | PROVED |
| 4.2 | min-cell judges: (QS) fails for every continuous coherent selection through T1 | PROVED (self-contained) |
| 4.2 Part A | (QS) at T1 alone, 216/216 branches certified | CHECKED (exact), hence PROVED |
| 4.3 | general fans: near T1 the selected models are plain posteriors on T1-pinned cells | PROVED |
| 5.1 | rank-2 worlds: dim R(C) ≤ 1 anywhere ⇒ (QS) fails | PROVED (part (b) modulo 3.2 imports) |
| — | (QS) for some family through T1, with any judges | open |
