# R6: referee report on R1, R2 and R3 (round 9, 12 Oct 2026)

Scope: every item on the priority list was checked line by line against the brief's setting (decomposable domains, (G) and (IB) inside M_L, (LF) at the target only). Sources were opened and the cited labels were checked: GD v3, LDG, BA, CBOI, CCF, CANA; CPM v19b, NAL, DCE (staged copy), NOGO; the device copy of PB.

Verdict scale: CORRECT / CORRECT WITH REPAIR / GAP / FALSE.

---

## Summary table

| Item | Verdict |
|---|---|
| R1 Lemma 1.4 | CORRECT |
| R1 Lemma 1.5 | CORRECT |
| R1 Theorem 2.2 | (N), (S): CORRECT. (T): CORRECT WITH REPAIR |
| R1 Prop 2.4 | CORRECT (one measurability remark) |
| R1 Prop 2.5 | CORRECT (proof needs N shrunk). The follow-up slogan "domain shape gives no gain" is NOT established |
| R1 Prop 2.6 | CORRECT. Uncited rediscovery of the Audit §2 local face lemma |
| R1 Prop 2.7 | CORRECT |
| R1 Prop 3.1 | CORRECT |
| R1 Theorem 3.2 | CORRECT (clarifications in (iv)) |
| R1 Ex 3.3 | CORRECT WITH REPAIR (β formula; one unproved sentence) |
| R1 Ex 3.4 | CORRECT |
| R1 Lemma 3.5 | CORRECT WITH REPAIR (needs dim K = n−1; minor advice-range and Fubini points) |
| R1 Theorem 4.1 | CORRECT (NAL's bad set must be rebuilt for Ψ^w; this is routine) |
| R2 Lemma 1 | CORRECT |
| R2 Lemma 2 | CORRECT |
| R2 Lemma 3 | CORRECT (uses (LA), (S), (C) implicitly). The remark after it silently assumes the all-model domain |
| R2 Prop 4 | CORRECT |
| R2 Lemma U | CORRECT |
| R2 Theorem N | CORRECT WITH REPAIR (the sufficiency clause is FALSE as worded) |
| R2 Prop P | CORRECT |
| R2 Theorem R | CORRECT (Step 5 edge cases only sketched; they are fine) |
| R2 Prop 5 | CORRECT (minor decomposable-domain wording) |
| R2 Theorem 6 | CORRECT |
| R2 Theorem 7 | CORRECT ((C) is not needed) |
| R2 Prop 8 | CORRECT |
| R3 §2.1 + Cor 2.1a | CORRECT (2.1a's "in particular" needs K ≠ Δ) |
| R3 §2.3 | CORRECT |
| R3 §3 (P1, P2, P3) | CORRECT |
| R3 Theorem L | CORRECT. Hypotheses consistent. Step (3) wording imprecise |
| R3 §4 Remark (ii) (CHECKED, not on list) | GAP: "completely F-free" not justified |
| R3 §5.3 | CORRECT |
| R3 §5.4 (i), (ii) | CORRECT |

---

## R1

### Lemma 1.4: CORRECT
(i) LDG thm:kkm (GD "Loss Dominance Generalized v2.tex", l.164) is stated for an arbitrary M_L. It gives U_L = C_L under (LA), (S), (C). Combined with 1.3(c), it gives the claim.

(ii) Splitting E by pair of kinds of advice gives one non-null part. On it, the two kinds of advice differ in the acceptance of one orientation, so Z can be taken on one side of {g_1 = 0}. A ray θ with Z_θ non-null therefore never meets −Z. The polar-Fubini step needs only the direction "a.e. cone ⇒ radial sections null or co-null", and that direction is valid. In the (+,−) case, X_F also accepts −(Z∖F), but that set lies on the antipodal rays and does not affect the argument.

### Lemma 1.5: CORRECT
At e_i the objective is ℓ_i(g,·). This is injective on A(g) by Lemma 1.1, so the minimiser is unique and is the best advice in the advice range at i. Lemma 1.3(a) then makes the minimiser coherent. The DCE prop:ideal citation is accurate but not needed.

### Theorem 2.2
- **(N1)–(N4): CORRECT.** If the minimiser at p is unique with a positive gap, then p ∉ ∂R(h): when the minimiser accepts h, p ∈ R(h), which is open; otherwise the gap keeps a neighbourhood out of R(h).
- **(S): CORRECT.** v3 thm:general (GD v3 l.268–335) needs only that the comparisons and splices stay in M, an integrable envelope, and uniqueness at every p. The normalisation ℓ(good) = 0 is not used.
- **(T): CORRECT WITH REPAIR.**
  - ⇒ direction: Lemma 1.3(b) gives "D is p*-Bayes for some p*". It does not give D ≈ B_{p*} when p* is a boundary prior with ties on a non-null set (n ≥ 3, non-vertex faces).
  - ⇐ direction: for a boundary p*, a p*-Bayes model can be weakly dominated at a world outside supp p*. R1's own C1 says exactly this. B_{p*} need not even be a Bayes model there: at a +/− tie it is silent.
  - Repair: state (T) as two separate claims. (a) D ∈ C_L ⇒ D is p*-Bayes for some p*. (b) If p* is interior and D is p*-Bayes, then D ≈ B_{p*} ∈ C_L. Under Prop 2.6's hypotheses this is all that is used afterwards.

### Prop 2.4: CORRECT
- W is an uncountable union. Since every R(h) is relatively open, W = {h : R(h) ≠ ∅} = ⋃_{p rational} B_p (plus positives). So W is measurable, and "negatives are null" follows by countable union. This should be said.
- Vertex property: correct. At δ_i with h_i > 0, accepting h is good, so it is the unique minimiser. At δ_j with h_j < 0, some cheaper advice is in the advice range unless every evaluable model accepts h (× has been set aside). R(h) is an intersection of strict half-spaces.
- (ii): uses D_{K₁} ∩ D_{K₂} = D_{conv(K₁ ∪ K₂)}, which is correct.

### Prop 2.5: statement CORRECT; follow-up claim over-stated
- Proof:
  - "(LF) puts acceptance of h in the advice range" holds only after N is shrunk to a neighbourhood of ∂D∖0 that avoids −D and {h ≤ 0}. Shrinking is legitimate. On the precise boundary, −h ∈ ∂D is also inside N, so + (not only ×) is in the advice range.
  - The rest holds: N ⊆ int cl W^o; cl W^o ∖ W^o is null; the compactness step gives d_H(K', K) < η, where η = −max_{C} P_K on the complement C of the cone on the sphere. This works for K of any dimension.
- Over-claim: the sentences after the proposition ("the analysis can always be run on U'"; and in "Answer to task (2)", "Domain shape: no gain, by Prop 2.5") do not follow. Restricting the class of evaluable models to models inside U' removes "−" from the advice range of the pairs whose g lies in U'. That turns wedge charts {c>0, d>0} into half-planes {c>0}, and it changes the Bayes models: they could become incoherent. Prop 2.5 only says the original system's reach set contains a convex cone around cl D∖0. The phrase "charts of h ∈ U' are unchanged" is vacuous. Lemma 3.5 and Thm 4.2(H2) correctly keep the original advice ranges.

### Prop 2.6: CORRECT
The proof is sound: any p*-Bayes model accepts a.e. h with h_S > 0 whose acceptance is in the advice range, and (LF) puts the acceptance of such h in the advice range just outside cl D near g₀. This is the Bayes form of the **local face lemma** (Audit of Imported Assumptions, §2, item 1), which R1 does not cite. The brief asks for citation, not rediscovery.

### Prop 2.7: CORRECT
The sign facts behind it are correct: c_j < 0 and d_j < 0 for j ∈ N(g), and the same holds in the mirrored (−g) case.

### Prop 3.1: CORRECT
- Gap continuity plus dominated convergence give the L¹ claim.
- K ↦ 1_{D_K} is continuous and injective on the compact space of credal sets. Injectivity uses v19 lem:open-agree (CPM v19b l.1786–1792, cited as "line 1788": accurate) and the dual recovery of K. So it is a homeomorphism onto its image.

### Theorem 3.2: CORRECT
- (i) The zero set is closed in int Δ × ℝⁿ and every p-section is null; apply Fubini.
- (ii) Fubini.
- (iii) Pointwise convergence off a λ-null set, then dominated convergence.
- (iv) Two clarifications:
  - The "normal" is the vector c itself. An affine functional on aff Δ determines c uniquely, because aff Δ spans ℝⁿ. So ĉ = c/|c| is well defined.
  - "Continuous at every point" means continuous relative to the co-null set G of good h. Convergence of the normals uses that the limit line crosses int Δ. That holds because c has both signs on mixed h.

### Example 3.3: CORRECT WITH REPAIR
- {t : φ(t) > s} = (τ(s), 1], so α is right.
- But {t : φ(t) < s} = [0, σ(s)) with σ(s) = inf{t : φ(t) ≥ s}, so β should be σ(r/(1+w)), not τ(r/(1+w)). They differ exactly at the countably many r with r/(1+w) = s_k. The Bayes models still agree a.e. with D_{K_t}, so nothing downstream changes. State the formula with σ, or say "for r off a countable set".
- Checked:
  - realisation of any 0 < β < α < 1: + = (0, 1/(1−α)), 0 = (1,1), − = (1/β, 0), with strict (G) ranks, the stated rescaling, and the +/− comparison consistent;
  - α and β strictly increasing, so ties sit on one ray per prior;
  - Bad ⊇ the jump rays, because P_{K_t}(g) = 0 on a whole plateau interval of t.
- The sentence "Discontinuity of charts is equivalent to plateau-type persistence in n = 2" is unproved. Label it as a remark, not part of the PROVED example.

### Example 3.4: CORRECT
- Thresholds α = 3r/2 and β = (3r−1)/2 match D_{K_t}.
- The advice ranges are consistent: − is never needed for r ≤ 1/3, and + never for r ≥ 2/3.
- Uniqueness holds at every t, including the endpoints.
- W = D_{[2/3,1]} ∪ D_{[0,1/3]} with angular range (−63.43°, 153.43°).
- The witness pair and its negative midpoint check out.
- (LF) at [1/3, 2/3] holds with N a small neighbourhood of the rays (2,−1) and (−1,2).

### Lemma 3.5: CORRECT WITH REPAIR
- **Existence of Q''.** "K_q ∩ K' ≠ ∅ near p* by Hausdorff continuity, since K' ⊆ ri K" needs dim K = n−1.
  - If K is full-dimensional, a convex set Hausdorff-close to K contains points near every vertex of K, and hence contains K'.
  - If K is lower-dimensional (T3), a parallel translate of K is Hausdorff-close but misses K'. Prop 2.5 allows lower-dimensional K.
  - Repair: add dim K = n−1. This holds for T1 and T2.
- The passage from "for each q, for a.e. g" to "for a.e. g, R(−g) ∩ Q'' = ∅" needs Fubini plus openness of R(−g). This step is missing but routine.
- The conclusion R(g) ∩ Q'' = {c·q > 0} ∩ Q'' only makes sense when 0 ∈ A(g). For advice ranges {+,−} or {+}, state instead "R(g) ⊇ Q'' a.e.".
- A cleaner proof avoids the apex entirely. If q ∈ Q'' has c·q > 0 and d·q ≤ 0, then c'·q = c·q − d·q > 0, so q, or a nearby point of the open Q'', lies in the − sector. This works in every n; "apex" is a point only when n = 3.

### Theorem 4.1: CORRECT
- (w·q)·P_{K_q}(g) = q·(w⊙Ψ)(g): checked.
- R1 invokes "NAL's bad open set" (CPM NAL thm:obstruction, l.491–535), but NAL builds it for Ψ, not Ψ^w. The adaptation is routine and should be written out. Choose q̃⁰ ∈ U and run NAL's construction at q⁰ = σ(q̃⁰). Then q·Ψ^w(g*) = (w·q)·σ(q)·Ψ(g*) vanishes at q̃⁰. It is nonconstant on aff Δ, because Ψ^w_i(g*) < 0 while the value at q̃⁰ is 0. Take B to be a ball around q̃⁰ inside U.
- The chart-type case analysis is correct, including the wedge case. A full chord of {b = 0} inside B cannot be covered by two distinct lines, and the positive orientation of the multiplier follows from {b>0} ∩ B being non-null.
- No (LF), (S) or (C) is used: confirmed.

---

## R2

### Lemma 1: CORRECT
Transitivity through ties holds in a preorder. This is LDG thm:kkm / BA lem:complete-class(b), both valid on any M_L.

### Lemma 2: CORRECT
The penalty arithmetic was checked.
- Case a = +: the minimum difference is ≥ p(P) − 2η(1−p(P)) > p(P)² for η < p(P)/2.
- Case a = 0: the two differences are p(N) − ηp(P) and p(P) − ηp(N).
- The penalties are bounded and strictly rank-increasing.

### Lemma 3: CORRECT (with implicit hypotheses)
(LA) and (S) are needed for (i); (C) is needed through Lemma 1 for (ii). Please state them.

**Domain flag.** The sentence "These are exactly the hypotheses of the v3 three-vertex obstruction" silently assumes the all-model domain. v3 thm:additive-obstruction (GD v3 l.487) is stated for "a ranking of all measurable models". Its proof uses lem:bayes-necessary(c), which fails on decomposable domains (R1 C2). On a decomposable domain, Lemma 3 yields additive realisation, not the three-vertex obstruction.

### Prop 4: CORRECT
- Checked: L¹ is world-independent and weakly guiding; undominated ⇒ L¹ = 0; the sections are Δ or ℓ²-sections; (C) holds.
- Failure of (W_i): the "lightest piece" trick for charges is correct.
- CCF lem:cboi exists as cited (GD "Closed Choice Forces Fineness.tex", l.125, with (W_k) at l.121).

### Lemma U: CORRECT
Identical in substance to R1 Lemma 1.4(ii), with a different route to the contradiction. Both are fine.

### Theorem N: CORRECT WITH REPAIR (the sufficiency clause is FALSE as worded)
- The main argument is correct: the sign pattern σ* = −sign u on supp u, the support argument for interiority, and Lemma U.
- The final clause "The hypothesis holds whenever K_A ⊂ int K_B (interior relative to Δ)" is false when K_A meets ∂Δ.
  - Counterexample: n = 2, K_A = [0, 1/2], K_B = [0, 3/4]. K_A lies in the Δ-relative interior [0, 3/4) of K_B. A never accepts any g = (a, −b), since t = 0 gives −b < 0. So R_{(+,−)} is null.
  - Such a pair can sit on a monotone additive path (α equal, β increasing), so the conclusion genuinely fails, not just the proof.
- Repair: read "int" as the interior relative to aff Δ. Then K_A ⊆ int K_B ⊆ int Δ, so m(P), m(N) > 0 on K_A, and the ratio argument goes through.
- The T1-versus-u example is unaffected, since u ∈ int K.

### Prop P: CORRECT
- Monotonicity comes from the threshold inequality.
- Uniqueness at the endpoints holds because ranks are distinct at a vertex.
- Continuity in measure gives continuity of α and β via the interval homeomorphism.

### Theorem R: CORRECT
- Steps 1–4 checked:
  - no strict nesting ⇔ chain in ⪯_m;
  - the (G)-strict ordering at both worlds;
  - sections equal to order intervals;
  - the connectedness splits in Steps 2 and 3;
  - X = D_{[a',b']} ∈ M, because its advice is advice the u_k eventually give;
  - C_{e_1} ∈ R by the vertex lemma;
  - continuity in Step 4.
- Step 5 penalties checked:
  - +/0 tie at t = s₊, 0/− tie at t = s₋;
  - in the s₋ = s₊ case, silence is costlier for η < ½;
  - {s± = t} is a single r-value because α and β are continuous.
- The "zero gap" sentence is muddled but correct. A switch point at 0 or 1 with that advice in the advice range occurs only on single rays, or on pairs with a singleton advice range (every evaluable model gives the same advice), where the penalties are irrelevant.

### Prop 5: CORRECT
- BA's corollary (GD BA, unnumbered corollary after thm:extension) is stated for all models.
- On a decomposable domain, strict (G) only forces strictness of ℓ = Σc_kL^k on the advice in the advice range; that is all that is needed.
- The remaining steps are correct: equality of ℓ forces equality of every L^k_i, and then (C) applies.

### Theorem 6: CORRECT
All cases were checked:
- the supports exist (Aumann convexity plus weak Pareto minimality);
- t = 0 is excluded;
- case 1/1: t_A = t_B, the finite multiplier at an interior L¹-level, λ_A = λ_B, the tie on R1 ∪ R2, and undominatedness of the splice;
- cases 1/2 and 2/1: d₁ and e₁ positivity clash;
- case 2/2: dominators stay in 𝔐, and s* ∈ (0,1).

### Theorem 7: CORRECT
"With (C)" is unnecessary: Fact 0(b) and the definition of a lexicographic tie suffice.

### Prop 8: CORRECT
- Checked:
  - (G) for both lexicographic levels;
  - Neyman–Pearson sets are initial r-segments, unique because r has a density;
  - U is exactly the D_{[x,y]};
  - any selection is onto U;
  - every p is improvable at world 1 or at world 2;
  - countability against [α_B, α_A].
- M₀ is a decomposable domain (singleton advice ranges off R1 ∪ R2). (E) is not claimed.

---

## R3

### §2.1 and Corollary 2.1a: CORRECT
- Closed section ⇒ C_p ⪯_i C*; undominated ⇒ tie; vertex lemma plus strict (G) ⇒ contradiction. Completeness is not needed.
- 2.1a's z = e_k − ℓ_k(K)𝟙 is taken from v19 prop:target-two-sided's proof (CPM v19b l.2935ff). That proposition assumes K ⋐ int Δ, but the z computation is elementary and general.
- Two small points:
  - If ℓ_k(K) = u_k(K), D_K may give "−" rather than silence just outside D_K near z. The conclusion holds anyway, since neither is best at k.
  - "In particular the selection cannot equal the target on all of int Δ" needs some e_k ∉ K, i.e. K ≠ Δ.

### §2.3: CORRECT
- A weak dominator lies in 𝓜_T: error-only gives F ≥ 0. Its objective is no larger, so uniqueness applies.
- The KKM tie gives equal (F, S) and hence C = X.
- 𝓜_T is a decomposable domain because φ(silence) = 0 at every world.

### §3 (P1, P2, P3): CORRECT
- P1: the splice path gives an intermediate value strictly between sup_{m≥m₀} F_j(C_{q_m}) and F_j(C_p).
- P2: the lower boundary of a compact convex planar set is convex, so a finite subgradient exists at interior F-levels.
- P3: injectivity of v ↦ B_v holds, and strict sublevel sets are relatively closed because every point is a local minimum.
- Note: "not Lagrangian in the sense of P2" must include "not F_j-extremal". Theorem L checks all three conditions.

### Theorem L: CORRECT
- **Step (1).** V is open because of P1 and F ≥ 0. The silence-reduction strictly dominates at every world.
- **Step (2).**
  - The perturbation argument is valid; it needs F_j(Y) = c_j > 0 for the tight constraints, which holds.
  - KKT in image space: Aumann convexity of 𝓜_k's image, plus Slater via the F-free reduction.
  - "All optimal points share the multipliers" is correct in the form "every optimal point minimises the Lagrangian for every dual-optimal a" (complementary slackness).
  - (H3) gives uniqueness.
- **Step (3).**
  - "It is silent where the other advice in the advice range is bad at both k and j" is imprecise: C_q could choose advice good at k there.
  - The needed fact still holds. On that set, the only kinds of advice with φ_j > 0 are b and ×, which are bad or contradictory at k. Silence beats them in ψ_k + a·φ and is in A_k(g). So φ_j(C_q) = 0 < φ_j(b), and C_q is not F_j-maximal.
- **Steps (4)–(6).** Closedness of L_v via 2.1 holds: lexicographic ties force equal F. Sierpiński's theorem applies to [0,1]. Components of the open set V are open and path-connected. The final contradiction at e_j is correct.
- **Hypotheses.** (H1) depends only on (M, F); (H2) and (H3) are explicit. Nothing hidden is used beyond the vertex lemma, which holds on decomposable domains (DCE prop:ideal, staged copy l.49).

### §4 Remark (ii) (labelled CHECKED; not on the list): GAP
The remark claims that at least two of N₁, N₂, N₃ are "completely F-free". From failure of (H1), one only gets φ_j(accept h) = 0 for h ∈ N_j with j = l(k). Accepting −h on the same problem is bad at both worlds i ≠ j. It would need F_i to ignore acceptances in the advice range with positive j-coordinate for both i ≠ j, but l(j) is a single index. So the claim holds only where accepting −h is not in the advice range, as on the §5 domains. The residual reduction should be restated accordingly. [Correction, 14 October 2026: on a U-domain, accepting −h is outside the advice range only when −h ∉ U. For h ∉ U with −h ∈ U, accepting −h is in the advice range, so the remark does not hold there either. No theorem relies on this remark.]

### §5.3: CORRECT
- Geometry checked:
  - (a) v_k ∈ [v'_k, e_k];
  - (b) the ray from e_m exits K on the face {p_m = c} = [v_k, v_l];
  - (c) all three vertices lie in K''_k ∪ K''_l;
  - (F1)–(F5).
- (LF) with N = U holds: R △ D_K ⊆ U ⇒ R ⊆ U.
- The per-problem lexicographic minimisation was checked:
  - accept vs silence on D_K costs −r·h;
  - the shell is silent iff J ∩ supp r ≠ ∅;
  - the three prior cases give D_K ∩ D_r, D_r ∩ G_m and U ∩ D_k, all coherent;
  - D_K = B_r for r ∈ K.
- Uniqueness ⇒ undominated was checked for boundary r as well.

### §5.4: CORRECT
- **(i)** The minimiser X_a was rechecked:
  - D_K gambles accepted iff h_1 > 0;
  - J = {3} shell gambles accepted iff h_1 > a|h_3|;
  - J ∋ 1 shell gambles: no advice (required by F_1 = 0 on 𝓜_1);
  - J = {2} shell gambles accepted iff h_1 > 0.
  - Near the facet-middle crossing h_1 = a·c₀, the rejected set is an open convex wedge with angle < π. Its complement is non-convex: the midpoint witness lies in the wedge, with non-null neighbourhoods.
  - Ties are null, and 2.3 applies with T = {1}, a = (0, a), b = e_1.
- **(ii)** Theorem L's hypotheses were verified on this system:
  - (H1): B_k accepts G_m- and G_l-shell gambles with J = {m} and {l} by (F4).
  - (H2), first half: D_K problems.
  - (H2), second half: two-negative shell gambles with J = {k, j}. These exist non-null just outside D_K near the boundary point e_l − (c/(1−c))(e_k+e_j), perturbed by −δ𝟙, which leaves every G_m. Alternatively use J = {j}.
  - (H3): every tie functional has coefficient −1 on h_k.

---

## Citations: accuracy check

All cited labels exist and say what is claimed, with these exceptions:
1. **R2 §2 remark after Lemma 3:** the v3 three-vertex obstruction is an all-model theorem (see above).
2. **R1 Prop 2.6:** the Audit §2 local face lemma is not cited.
3. **R1 Thm 4.1:** "NAL's bad open set" is applied to Ψ^w, but NAL constructs it for Ψ (routine to adapt).
4. **R1 Ex 3.3:** v3 eq. (interval-family) and prop:bayes-interval are used correctly, but the β formula is slightly off (see above).

Verified:
- **v3:** lem:local-independence, thm:general, lem:bayes-necessary(a)–(c), lem:kkm, eq:independence.
- **LDG** thm:kkm (valid on any M_L).
- **BA:** lem:complete-class, thm:extension, the essential-union corollary, prop:lex, thm:finite-sample.
- **CBOI:** lem:dominator, thm:fa.
- **CCF** lem:cboi.
- **CANA** thm:closure.
- **DCE:** prop:ideal, prop:menu, thm:extension, the §4 cheap system C_p = {g ∈ U : p·g > 0}.
- **v19:** lem:open-agree (l.1786), prop:target-two-sided, prop:dimension-necessary.
- **NAL:** lem:additive, thm:belief, thm:obstruction.
- **NOGO:** §3 regularisation Ψ = dist(·, S̄)Φ/‖Φ‖.
- **PB** (device): Lemma 3.1, Thm 3.2, Thm 4.1.

## Domain flags (all-model domain silently assumed; (G)/(IB) outside M_L)
- R2 remark after Lemma 3 (above): all-model domain assumed.
- R2 Prop 5: BA's corollary is used "a.e." as on all models. On M only strictness on A(g) follows, which suffices.
- R1 "Answer to task (2), domain shape: no gain": implicitly replaces the advice ranges by those of the class of models inside U'. That is a different class of evaluable models, hence a different system (see Prop 2.5).
- No instance found of (G) or (IB) being applied to a model outside M_L.
  - Every splice, silence-reduction, model giving the best advice in the advice range, and limit model used (R2 Thm R Step 3's X; R3 Thm L's Y; R1 Lemma 1.1's X, Y) was checked to lie in the decomposable domain.
  - R1 Ex 3.3 and R2 Prop 4 use the all-model domain explicitly and legitimately.
