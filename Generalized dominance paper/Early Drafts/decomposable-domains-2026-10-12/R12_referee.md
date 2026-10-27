# R12: referee report on R10a and R10b (12 Oct 2026)

**Scope.** Every PROVED or CHECKED item in R10a_notes.md and R10b_notes.md was checked line by line against the following:
- the setting of BRIEF.md, BRIEF2.md and AUDIT_ASSESSMENT.md;
- the repaired statements of R1 and R4, using R6, R8 and "Consolidated Statements - Decomposable Domains 2026-10-12.md".

I did not write these notes, and nothing in them was assumed correct.

**Sources opened:**
- CPM v19b (LSP_CPMs_v19b.tex): §§1–3 (def:cpm, prop:contraction, lem:concave-cpm, lem:indiff-null, prop:diagonal-majorant, prop:global-concave), §4 (LP maps, thm:lsp-cpm, lem:nontangent), §5 (prop:concave-envelope, prop:concave-converse), §13 (ex:box-realisation, ex:lp-hexagon, cor:approx, cor:approx-all) and §14 (lem:hs-reduce, lem:hs-slices, thm:hs-nogo);
- NAL (nonadditive_losses.tex): thm:aggregation, cor:concave-ingredients, lem:twoslope, cor:all-gambles, lem:support, **prop:average**, thm:belief and rem:nogo;
- NOGO (CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md), in full.

PB and FA (device-only) were not reopened. Every R10 statement that depends on them is treated as conditional, as the authors themselves label it.

**Scripts.**
- `r10py/mixture_check.py` and `r10bpy/crossings.py` were rerun. Both reproduce every number reported in the notes, including:
  - hexagon: 6 vertices;
  - 9-gons: Hausdorff distances 0.0186 / 0.0053 / 0.0035;
  - 0 (G)-sign violations, 0 mismatches, 0 ties;
  - T1: 3 crossing vertices; 0 of 20 000 random triangles with fewer than 2 crossing vertices;
  - the non-box cevian hexagon: 6 vertices, no crossings, cyclic products 12 vs 6;
  - the normalised box: no crossings.
- One referee script was added: `r12py/mprime_check.py`. It confirms that K_u ⊇ W and that d_H(K_u, W) ≈ 0.5–0.65·(a/b), for ε′ ∈ {0.2, 0.28}.

Verdict scale: CORRECT / CORRECT WITH REPAIR / GAP / FALSE.

---

## Summary table

| Item | Verdict |
|---|---|
| R10a §1 / R10b §1, shrinking N | CORRECT WITH REPAIR (the stated shrink is impossible for lower-dimensional K; a repaired shrink is given below) |
| R10a Thm V (vertex anchoring) | CORRECT (needs strict (G) at world i; lower-dimensional K needs the §1 repair) |
| R10a Cor V1 | CORRECT (count advice range {+,×} as acceptance by every evaluable model) |
| R10a Cor V2 (a)–(d) | CORRECT |
| R10a Cor V3 ((H0) automatic) | CORRECT WITH REPAIR (false on the nonnegative orthant as worded; harmless) |
| R10a Prop V4 | CORRECT WITH REPAIR (necessity is V2; the "converse" does not cover a prescribed D; the third bullet is not a characterisation) |
| R10a Lemma E | CORRECT as stated |
| R10a Remark after E, "(K4) replaced by Lemma E" | CORRECT WITH REPAIR (FA uses interior q_η → q₀, not charts at q₀; a one-line limit step, or R10b Lemma FS, is needed) |
| R10a Cor C (B2, C3, G2 without (H0)) | CORRECT WITH REPAIR (as a conditional; same two repairs) |
| R10a Thm M (gauge mixtures), all steps | CORRECT. Novelty is limited: see the overlap section |
| R10a Thm M examples | CORRECT. The affine-contamination non-example is CORRECT WITH REPAIR (the condition is "for each ordered pair i ≠ j, λ_i = 0 or λ_j = 1") |
| R10a Prop M′ | CORRECT (constant 3a/(bδ′) should carry diam Δ = √2). K_u ⊇ W is verified analytically and numerically |
| R10a Thm R (ray lemma) | CORRECT. It holds for every p* ∈ Δ, not only interior p* |
| R10a Cor R1, first bullet | CORRECT |
| R10a Cor R1, second bullet | CORRECT WITH REPAIR (strict signs on ∂D_K must be derived, not assumed) |
| R10a Thm P (no plateau, measurable charts) | CORRECT under (Sp) and R4 (K1), (K3) as repaired by R8. Superseded by R10b Thm PL / PL2 |
| R10a Thm O, "plateaus are excluded measurably" listed as unconditional | FALSE as labelled (Thm P needs (Sp)). The claim itself is true by R10b Thm PL |
| R10a §6 PB Thm 5.2 sketch, §7 last paragraph | Not verified (sketch / "direct computation" not shown) |
| R10b Prop V | CORRECT |
| R10b Cor V1 | CORRECT ("E ⊆ ∩_i{h_i>0}" should read E ⊆ {h ≥ 0}) |
| R10b Cor V2 | CORRECT (read "q → e_i through int Δ") |
| R10b Remark V3 | CORRECT |
| R10b Cor V4 | CORRECT |
| R10b Lemma FS | CORRECT |
| R10b Lemma UVN (a), (b) | CORRECT |
| R10b Prop L (locality barrier) | CORRECT |
| R10b Lemma D | CORRECT WITH REPAIR ("β_v is open" should read "relatively open in Γ_v") |
| R10b Lemma M (main local lemma) | CORRECT |
| R10b Lemma P | CORRECT |
| R10b Theorem PL and its corollary (no plateau) | CORRECT (segments need the §1 repair) |
| R10b Corollary PL2 | CORRECT |
| R10b crossing criterion: "vertex has a crossing iff its edge normals have opposite signs in some coordinate" | CORRECT |
| R10b "every interior triangle has ≥ 2 crossing vertices" | CORRECT WITH REPAIR (the "rays k and k+3 are opposite / arc spans 4 gaps" argument is invalid as written; a correct counting proof is below) |
| R10b: T1 has 3 crossing vertices; normalised boxes have none; cevian hexagon example | CORRECT (box: when all six ratio constraints are edges, which is the generic case) |
| R10b n > 3 transfer of items 1–6 | CORRECT (Lemma M Steps 3–4 work with hyperplanes) |
| R10b §8 remaining case | CORRECT as a statement of what is proved |
| R10b §9 corrections to earlier notes | CORRECT (the (K3) item is a chart-level statement; the c-cluster version of (K3) still needs split pairs) |

No use of (G) or (IB) outside M_L was found, and no silent all-model assumption. Every model built in either note is a choice within the advice ranges or a splice. Prop L uses the all-model domain explicitly and legitimately.

---

## R10a

### §1 and R10b §1: shrinking N. CORRECT WITH REPAIR
R10a argues that ∂D ∩ (−cl D) = {0} "since K spans ℝⁿ". This holds only when dim K = n−1.

For a lower-dimensional K, such as T3 or a segment, every h ⊥ K has h, −h ∈ ∂D∖0. So no open N ⊇ ∂D∖0 can satisfy N ∩ (−cl D) = ∅, and R10b §1's shrink is impossible.

**Repair.** Take N′ := (N ∖ −cl D) ∪ (N ∩ −N). This set is open and contains ∂D∖0, because a boundary point in −cl D is ⊥ K and so lies in N ∩ −N. For a.e. h ∈ N′, either −h ∉ D, so the advice range contains {acc h, 0}, or both orientations can be toggled, so all four kinds of advice are in the advice range. Hence "accept h and silence are in the advice range a.e. on N′" holds for every K. Nothing downstream changes.

This matters for:
- Thm V as stated (only e_i ∉ K is assumed);
- R10b Prop V for "every interior target";
- the segment case of the PL corollary.

### Theorem V (vertex anchoring). CORRECT
Every step was checked:
- prop:ideal gives the best advice in the advice range at world i, so a.e. on N, C_{e_i} accepts h iff h_i > 0. Accepting h is the unique best advice when h_i > 0; when h_i < 0, silence (or accepting −h) beats it.
- An open set that is a.e. contained in an open convex set is contained in it, and an open null set is empty.
- The boundary gamble h⁰ exists: e_i ∉ K gives m_i < 1 on K, so P_K changes sign on the connected sphere of {h_i = 0} (n ≥ 3). h⁰ ∈ ∂D because h⁰ ± δ𝟙 lie on either side of D, and h⁰ is not ≥ 0.
- The two-sided limit gives w ∈ V_i with w·h⁰ = 0.
- If w ≠ e_i, the vector k (k·w = 0, k_i = 1) gives h^θ ∈ N ∩ D_i with w·h^θ = 0, which contradicts h^θ ∈ D_{V_i}.

Scope: strict (G) is needed at each world i used. The theorem says nothing at worlds where guidance is weakened (Σ_T systems, the D_Δ exception; audit correction 6). The note should say so.

This refines audit correction 8. (LF) alone does not imply (H0), but (LF) + (S) + (LA) + strict (G) exclude acceptance by every evaluable model of any gamble with a negative coordinate. R4 Remark B3's escape is closed.

### Cor V1. CORRECT
The proof also covers advice range {+,×}: every model accepts h there too. "Accepted by every evaluable model" should be read to include them (R10b's "in effect").

### Cor V2. CORRECT
- (a) Best advice in the advice range at i, plus V1.
- (b) D_{V_j} ∩ D_i = D_{conv(V_j ∪ e_i)}. Cones that are nested a.e. are nested. Duality reverses the inclusion.
- (c), (d) D ∈ M_L, D is coherent so it never contains both orientations, and (LF) holds.

### Cor V3. CORRECT WITH REPAIR
On the nonnegative orthant (which is inside D for K ⊆ int Δ), the advice ranges {+} and {+,×} are consistent with V1. So "(H0) on D ∪ N except on pairs with advice range {+,−}" is false as worded.

Repair: state it for a.e. mixed h, and add R10b Cor V4's observation. A nonnegative h accepted by every evaluable model has chart Δ = {𝟙·q > 0}, which is sign-preserving, so NOGO's weak-sign hypothesis still holds.

The compactness step "D_{K′}∖D ⊆ N for K′ close to K" is correct. On the compact set of unit vectors outside N ∪ D we have P_K < 0, because P_K = 0 forces membership of ∂D ⊆ N.

### Prop V4. CORRECT WITH REPAIR
The necessity half is Cor V2.

The stated converse ("every compatible tuple is the vertex structure of a full additive system, Thm M with M_i = V_i") is true. But that system covers the targets Σ_i p_i V_i, which is NAL prop:average(ii), not a prescribed D with D ∪ N ⊆ ∪ D_{V_i}. So V4 does not characterise the advice-range structures compatible with covering a given target.

The third bullet ("advice ranges that contain acceptance of h for each h ∈ Av, and contain silence wherever they contain no other kind of advice; every evaluable model gives no advice on the remaining pairs") is not a characterisation. Advice ranges {+,−}, {+,0,−} and advice ranges containing × are all possible.

Correct statement: (i) in any system satisfying Thm V's hypotheses, Av off {h ≤ 0} is ≈ ∪ D_{V_i} for a compatible tuple with e_i ∈ V_i and D ∪ N ⊆ ∪ D_{V_i}; (ii) conversely, on any advice-range structure with that Av, every strictly guiding ranking has coherent vertex models D_{V_i}.

### Lemma E. CORRECT as stated
- Bayes models contain C(p₀) a.e.
- On {h_S < 0}, not every evaluable model accepts (V1), so the advice range contains a cheaper advice at every world of S.
- Separation gives K* ∩ Δ_S ≠ ∅.
- The density-point argument holds because P(z + δ𝟙) = P(z) + δ.

### Remark after Lemma E, and "(K4) replaced by Lemma E". CORRECT WITH REPAIR
FA §10.1 has a and b accepted at **interior** priors q_η → q₀, through facet maps evaluated only at interior priors (R8, FA §10.1). It does not give q₀ ∈ R(h) for h near a, b: charts are open, so q₀ may lie on their boundary. So "it needs only that the charts of the two facet witnesses contain the edge prior" does not match FA's input.

Repair (one line): let K* be any Hausdorff limit point of K_{q_η}.
- D_{K_{q_η}} → D_{K*} in L¹, M_L is closed under convergence in measure, and each L_i is L¹-continuous (integrable envelope). So D_{K*} is a coherent q₀-Bayes model.
- Lemma E then gives K* ∩ Δ_S ≠ ∅, hence P_{K*}(z′) < 0, hence P_{K_{q_η}}(z′) < 0 for small η.

This is exactly R10b Lemma FS, which is the right citation.

### Cor C (R4 Cor B2, Cor C3, Prop G2 without (H0)). CORRECT WITH REPAIR, still CONDITIONAL
With the Cor V3 repair (nonnegatives) and the limit step above:
- (H0)_{U′} reduces to non-adjacency.
- R8's advice-range flags are discharged: x⁻ ∈ U′ ⊆ D ∪ N ⊆ Av; z′ ∈ D.
- (K4) is replaced by Lemma FS.

The resulting no-go remains conditional on NOGO + PB + FA and on (H1) (respectively (H1⁺)), as R10a says.

### Theorem M (gauge mixtures). CORRECT
Every step was checked.
- **Signs.** f_i(h) > 0 ⟺ h ∈ D_{V_i}, since m = (𝟙·m)ν(m). For h ∈ Av:
  - h_i < 0 ⇒ f_i(h) ≤ a_i h_i < 0 (M1);
  - h_i > 0 and h ∈ D_{V_j} ⇒ h > 0 on conv(V_j ∪ e_i) ⊇ V_i (M2);
  - h_i = 0 gives f_i(h) = 0 exactly (both bounds). So the signs are exact.
- **Charts.** F_p(h) = min over S_p = Σ p_i M_i (Minkowski). S_p is compact, convex and nonnegative; it excludes 0 because each M_i ⊆ ℝⁿ_{≥0}∖0. Superadditivity gives F_p(g) + F_p(−g) ≤ 0, so p·c > 0 ⇒ p·c′ < 0 ⇒ p·d > 0. This puts the chart for advice range {+,0,−} in exactly the form claimed.
- **Uniqueness.** Ties occur only on {F_p(±g) = 0}, the boundary of a convex cone, which is null. A +/− tie with p·c > 0 would force p·c′ > 0, which is impossible.
- **Coherence.** F_p(h) > 0 ⇒ h ∈ Av. Nonnegative h with F_p(h) = 0 form a null set. This holds at every p, including the boundary and the vertices (K_{e_i} = V_i).
- **(G).** R1's converse applies to the advice ranges {+,0}, {0,−} and {+,0,−}. Rescaling for integrability leaves charts unchanged.
- **(LF).** If every f_i(h) ≤ 0 on ∂D_{K_{p*}}, then every f_i(h) = 0 (p* interior), hence h ≥ 0, which contradicts S_{p*} ⊆ open orthant. So ∂D∖0 ⊆ Av, which is open. R ∈ M_L because D = B_{p*} ∈ M_L.
- **(LA), (S), (C), (IB)** follow from R1 Thm 2.2(S), which R6 found CORRECT.

Examples:
- Common-W: ν maps hulls to hulls, so (M2) holds trivially.
- Hexagon: S_u is the zonotope with generators (u − e_i)/3 and is already normalised. Its vertices are u ± (e_i − u)/3, with coordinates 5/9, 2/9 and 1/9, 4/9, so it is interior.
- Precise identity: K_p = {p}.

Non-example: (M1) forces y_i = e_i when λ_i < 1. The edge argument shows that (M2) for the ordered pair (i, j) holds iff λ_i = 0 or λ_j = 1. Over all ordered pairs this means all λ = 0 (precise) or all λ = 1 (vacuous), which is what "λ_i ∈ {0,1}" should say. This is the decomposable-domain counterpart of NAL thm:belief's "rewards some wrong rejections when ε > 0" (see the overlap section).

### Prop M′. CORRECT
- Every point of S_u normalises to λw̄ + (1−λ)t/Σt, with w̄ ∈ W and 1−λ ≤ aΣt/(bΣ(1−t)).
- Case Σ(1−t) ≥ δ′: the distance is ≤ (1−λ)·√2. The note's 3a/(bδ′) lacks the √2; immaterial.
- Case Σ(1−t) < δ′: t/Σt ∈ B(u, Cδ′) ⊆ W when δ′ ≲ inradius(W). The convex combination is then in W.
- K_u ⊇ W: take t = 0 and w_1 = w_2 = w_3.

`r12py/mprime_check.py` confirms containment and a linear rate d_H ≈ 0.5–0.65·(a/b).

Shape of the approximants: the 9-gons keep three long edges parallel to T1's edges. Each vertex of W is replaced by a small "tent" of three vertices (two short edges) leaning toward e_i. In D_K terms, each facet of D_W is replaced by three facets.

### Theorem R (ray lemma). CORRECT
- **Step 1.** The crossing ⇔ tangent-from-e_i equivalence holds, since h ∝ v_k × e_i. An external point has two tangent lines touching distinct single vertices, by general position. Edge rays have r_i = det(v_k, v_j, e_i) ≠ 0.
- **Step 2.** A positive combination of concave functions that equals a linear function forces equality in each concavity inequality. Affinity and homogeneity give linearity. Continuity holds up to the closed facets because cl F_k∖0 ⊆ U, which is open.
- **Step 3.** Two linear functionals on v_k^⊥ with the same strict signs on an open sector that the zero line of h_i crosses are positively proportional.
- **Step 4.** Two facets of a simplicial 3-cone share a ray.
- **Step 5.** Each coordinate has one non-crossing facet, so every edge ray lies on a crossing facet of every coordinate.
- **Step 6.** Three independent rays force p*_i α_i = 0.

Remark: Steps 2–5 are needed only for i ∈ supp p*, and Step 6 already gives a contradiction if one p*_i > 0. So Thm R holds for **every p* ∈ Δ**.

### Cor R1. First bullet CORRECT; second bullet CORRECT WITH REPAIR
First bullet: f_i is concave on all of ℝⁿ and strictly sign-preserving on Av ⊇ ∂D∖0. Boundary p* is irrelevant: for p* ∈ ∂Δ, K_{p*} ∋ ν(Σ_{supp} p_i a_i e_i) ∈ ∂Δ, and in any case Thm R holds for every p*.

Second bullet: a concave representative of an a.e. strictly signed field only has *weak* signs on the null set ∂D_K. Thm R needs α_{ik} > 0.

Repair. Suppose α_{ik} = 0, so f_i ≡ 0 on F_k. Pick h ∈ relint F_k with h_i > 0 and points h ± sν on both sides of the facet, where the representative is strictly positive (a.e. choice). Concavity gives 0 = f_i(h) ≥ ½(f_i(h+sν) + f_i(h−sν)) > 0, a contradiction. So strictness on ∂D follows from a.e. strictness plus concavity, and the bullet holds.

### Theorem P. CORRECT under (Sp) and R4 (K1), (K3) as repaired by R8
- **d < 1 and monotonicity.** The vertex property gives δ_j ∈ R(x) for x ∈ Av with x_j > 0. Convexity of R(x) carries this along the segment.
- **Step 1.** The lower bound Q·ĉ ≥ d·c₀ (the note's constant differs; immaterial). The ball R and (K1) then give D∩U ⊆ D_{K_q}.
- **Step 2.**
  - s < d: exterior points are rejected, so P < 0 and Q_s·ĉ < 0.
  - s > d: write w′ = (z + ηx)/(1+η) with z ∈ D ∩ {h_j > 0} ⊆ D_{K_{Q_s}}. That inclusion holds because R(h) ⊇ [p*, δ_j] a.e.
- **Step 3.** An interior point plus a closure point gives an interior point.
- **Step 4.** Two half-planes through the centre Q, one inside the other's closure, coincide. The clusters at points with w′_i ≷ 0 have opposite i-signs by (K3).

Theorem P is therefore PB Thm 4.1 for measurable charts, but only under non-adjacency (Sp) and (K3). R10b Thm PL removes (Sp) for the no-plateau conclusion. R10b Cor PL2 gives Thm P's "exterior acceptance for all s ∈ (0,1)" conclusion from non-adjacency alone, without (K3): the open segment (p*, δ_j) lies in C = int conv({p*} ∪ V_j) ⊆ β_v.

### Theorem O, "Unconditional parts". FALSE as labelled
"Plateaus are excluded measurably (Thm P)" is listed among the unconditional parts, but Thm P assumes (Sp). The statement is nonetheless true unconditionally, by R10b Thm PL, for targets with two crossing vertices (T1 among them).

---

## R10b

### Prop V. CORRECT
- {h_i = 0}∖0 is connected and contains e_j ∈ D and −e_j ∉ cl D. The resulting boundary point w is mixed because K ⊆ int Δ.
- On a ball B ⊆ N around w, the vertex Bayes model equals {h_i > 0} a.e. (Lemma 1.5), hence exactly (open convex sets).
- The convex-combination step λ(w + δe_i) + (1−λ)y: choose λ first so that the point stays in B, then δ < (1−λ)|y_i|/λ.
- Separation gives e_i ∈ K_{e_i}. D_K ⊆ {h_i > 0} ⟺ e_i ∈ K is a correct equivalence.

This is the additive form of R10a Thm V. R10a's version is more general (any ranking, only e_i ∉ K).

### Cor V1, Cor V2, Remark V3, Cor V4. CORRECT
- V1: the conclusion is E ⊆ {h ≥ 0} a.e. The displayed "∩{h_i > 0}" is a slip.
- V2: for interior q → e_i, the gap at e_i gives L¹ convergence. R1 Prop 3.1's homeomorphism onto the image of the compact space of credal sets gives Hausdorff convergence.
- V3: |h_i|/|h| ≤ |e_i − m_n| with m_n ∈ K_{p_n} ⊆ h_n^⊥ and m_n → e_i.
- V4 handles the nonnegative orthant correctly (chart Δ = {𝟙·q > 0}).

### Lemma FS. CORRECT
- For a.e. h ∈ B ⊆ {h_S < 0}, acceptance is not in the advice range or is strictly beaten at every world of S.
- So 1_{B_q}(h) → 0 as q → q₀, and dominated convergence applies.
- z′ ∈ cl D_{K_q} ⇒ z′ + open orthant ⊆ D_{K_q}, which occupies a fixed fraction of B.

This is the correct decomposable-domain replacement for R4 (K4) and for FA §10.1's strict-sign step, without (H0). It is also the repair R10a's Lemma E remark needs.

### Lemma UVN. CORRECT
- (a): dominated convergence; an open convex cone missing x⁻ misses a half-ball. Upward closure gives P(q, h) ≥ P(q, x⁻) + min(h − x⁻). An open convex chart containing a.e. point of an open convex set contains the whole set.
- (b): the mirror argument via V1 and downward closure.

Neither part uses continuity or non-adjacency. This is a genuine improvement on R4 (K3), whose negative case worked with c-clusters and so needed split pairs.

### Prop L (locality barrier). CORRECT
Q ⊂ int Δ is compact, so q_i ≥ η > 0 on Q, and scaling the positive or negative coordinates makes c·q, c′·q of the required sign on all of Q. The three-sector chart then gives acceptance of g exactly when g ∈ D.

The proposition does not claim (S) or (LA). Its content is the meta-statement that any obstruction must use priors accumulating at ∂Δ (or on it). That is correct, and it sharpens R1 §4.2(c).

### Lemma D. CORRECT WITH REPAIR
- The collar argument holds: z = w′ + ε(w′ − x) has v·z = −εv·x > 0.
- (α) ⇔ v ∈ K_q: locally cl D_{K_q} coincides with {v·h ≥ 0} near w, so v^⊥ supports D_{K_q}.
- Γ ⇔ K_q ⊆ W_v holds with the enlarged ball: h = w″ + (v·h)𝟙 with v·𝟙 = 1.

Repair: β_v = Γ_v ∩ {∃x ∈ U⁻: P(q, x) > 0} is open **relative to Γ_v**, not in int Δ. Points near q may fail to keep U⁺, which is not compactly contained in D_{K_q}. Every later use (Lemma M, Lemma P, Thm PL) works inside an open G ⊆ Γ_v, where relative openness suffices.

Notation: the concentric balls "U″ ⊂⊂ U′ ⊂⊂ U" reuse the symbol U′ of R1 Prop 2.5. Rename them.

### Lemma M. CORRECT
This is the key new argument, and it was checked in detail.
- **Step 1.** For m ∈ W_v(U) and w′ ∈ F_v ∩ cl U′: m·w′ ≥ r|P_{v^⊥}(m − v)| ≥ rc|m − v|, because 𝟙^⊥ ∩ ℝv = 0. Hence ℓ_h ∩ W_v(U) ⊆ B(v, |h − w′|/c₀). R4 Thm B then puts every d-face point p ∈ B of a thin-collar adjacent pair at K_p ⊆ B(v, ρ), contradicting the choice of B. On B ∩ {c > 0}, d has one sign, so R(h) ∩ B ∈ {∅, B, {c > 0} ∩ B}.
- **Step 2.** Q ∈ α_v ⇒ P(Q, h) < 0 ⇒ Q ∉ cl R(h), by (1.1). Points s ∈ β_v near Q put R(h) ∩ B(s, η) ≠ ∅. Hence the line {c = 0} passes within 2η of Q.
- **Step 3.**
  - Limits a± satisfy a±·Q = 0 and a± ∉ ℝ𝟙.
  - (i) For good h, a.e. q ∈ R(h) has h ∈ D_{K_q}, so it lies in β_v.
  - (ii) P(q, h) > 0 ⇒ q ∈ cl R(h), by (1.1).
  - Half-planes through Q, one contained in the other's closure, coincide. Since aff Δ spans ℝⁿ, a₊ = λa₋ as vectors.
- **Step 4.** (a₋)_c ≤ 0 by strict (G) at c. UVN(a) gives R(h₊ⁿ) ⊇ V_c ∩ int Δ. Since R(h) ⊆ {c(h) > 0} globally, a₊ ≥ 0 on V_c, and a₊·e_c = 0 would put the line through e_c and Q across V_c. So (a₊)_c > 0, a contradiction.

The only hypotheses used are (LA), (S), (C), strict (G) at c, (LF) near the facet, R4 Thm B, R1 Prop 3.1 and UVN(a). There is no (H0), (H1), (Sp) or NOGO.

### Lemma P. CORRECT
- Near A (K_A = {v}), uniform positivity of v on cl U_{v′} gives a ball B_A ⊆ Γ_{v′} ∩ β_{v′}.
- For a.e. h ∈ U⁺_{v′}, R(h) contains the open set O ∪ B_A. By the open-convex fact it then contains the convex hull, so G′ ⊆ Γ_{v′}.
- On the segment [o, A], the first parameter t with q(t) ∈ cl β_{v′} is positive (Lemma M applied at o, and O ∩ Z_{v′} = ∅) and less than 1 (relative openness at A). At that point Lemma M gives K = {v′}.

### Theorem PL and the no-plateau corollary. CORRECT
- O ⊆ (Γ ∩ α ∖ Z) for both vertices, and UVN(a) gives V_j ⊆ Γ_v ∩ β_v.
- The first exit along [o, e′] lies in Z_v.
- The nearest point A₁ of the relatively closed set Z_v ∪ Z_{v′} on [o, A] leads to a contradiction by Lemma P, applied in either order.
- The Baire remark for q-dependent balls is correct.
- Corollary: a plateau satisfies the hypotheses trivially.

Scope of the corollary:
- T1 (all ε) and every interior triangle: each has ≥ 2 crossing vertices; see the next item.
- Interior segments: crossings at both endpoints in every coordinate c whose vertex e_c is not on the segment's line. The §1 repair is needed here.
- ε-contamination of an interior baseline, n ≥ 3: the crossing h_k = −1, h_x = 0, other coordinates t > 0, with t solving v_k·h = 0, is in relint F_k.

The result is genuinely unconditional: no (H0), (H1), (Sp), NOGO, PB or FA. It closes R1 §4.2(c) and the plateau escape that the audit listed under "Regularity".

### Cor PL2. CORRECT
Without d-faces meeting G, Step 1 of Lemma M holds for every h ∈ U⁻, and K_Q ≠ {v} is not needed. So ∂_G β_v = ∅, and connectedness gives G ⊆ α_v or G ⊆ β_v. Both sufficient conditions are correct: advice ranges {+,0}, or dim K_q = n−1 together with Thm B.

### Crossing criterion (§7)
- **"Crossing iff the two edge normals have strictly opposite signs in some coordinate": CORRECT.** h_c is linear on the 2-dimensional cone spanned by the two rays.
- **"Every interior triangle has ≥ 2 crossing vertices": CORRECT WITH REPAIR.**
  - The six "wall transitions" are correct: each plane {h_c = 0} meets int D_K (it contains e_j), so it meets ∂D_K in exactly two rays, each crossing transversally.
  - So is "at most 3 transitions at edges".
  - But "rays k and k+3 are opposite" is false. The two rays of {h_c = 0} ∩ ∂D_K are not antipodal. The two corresponding outward-normal directions of K bound the arc of K's boundary visible from e_c, which has length < π, not π. The "arc spans 4 gaps > π" step is therefore unjustified.
  - Correct argument: the two tangent lines from e_c are distinct, so one vertex hosts at most one transition per coordinate, hence at most 3. If one vertex v₁ hosted all ≥ 3 vertex transitions, each e_c would have its other tangent along an edge not containing v₁ (a tangent edge through v₁ would coincide with the line e_c v₁). So all three e_c would lie on the line through v₂v₃, which is impossible: at most one vertex of Δ lies on an interior edge line.
  - The script's 20 000 random triangles agree.
- **T1 has 3 crossing vertices, each with 2: CORRECT.** No edge of T1 lies on a cevian.
- **Normalised boxes have no crossings: CORRECT** when all six ratio constraints are edges (the generic case). The two tangents from e_c are then the two cevian edges through e_c. If a constraint is active only at a vertex, that vertex has a crossing.
- **Non-box cevian hexagon: CORRECT.** Cyclic products are box invariants (u₁u₂u₃/(l₁l₂l₃) both ways). The ratios are intrinsic once all six constraints are edges.
- **"Coverage open" for these classes:** not checked against Thm M. Heuristically, gauge mixtures with all-axis-parallel M_i give only boxes, so the claim is plausible.

### n > 3. CORRECT
- Lemma M Step 3: one half-space through Q inside another forces equal hyperplanes.
- Lemma M Step 4: a hyperplane through e_c and the interior point Q contains [e_c, Q] and so cuts V_c ∩ int Δ.
- Thm B, UVN, FS and Lemma P are dimension-free.
- Prop V needs n ≥ 3.

The FA box/ray system is correctly not claimed for n > 3.

### §9 corrections to earlier notes. CORRECT
- R1 §4.2(c) and R4 Remark B3: closed by Thm PL and V1.
- R4 Cor B2: drop (H0), with V4's nonnegative remark.
- R4 Prop G2: its decomposable-domain branch now rests on Lemma FS.
- Prop L: correct.
- On (K3): UVN(b) is the chart-level negative case for adjacent pairs. The **c-cluster** statement (K3) itself still needs split pairs, as R4 said. The note should say "chart-level replacement", not "(K3) holds for adjacent pairs".

---

## Consistency between R10a and R10b (new observation)

R10a's covered polygons have crossing vertices. The hexagon u ± (e_i − u)/3 has no cevian edge (det[(5,2,2),(4,4,1), e_c] ∈ {−6, 3, 12}), so all six tangencies from the e_c are vertex tangencies. Theorem PL therefore applies to it: no plateau, which is consistent, since its K_q varies.

The gauge-mixture systems have full-dimensional K_q at all interior q. So Cor PL2 puts them in the **zero-exterior-ratio regime** that R10b §8 leaves open for T1.

Hence that regime is inhabited by genuinely covered polygonal targets, including 9-gons Hausdorff-close to T1. Consequences:
- No argument confined to facet crossings (PB §§4–6 type, Lemma M type) can close T1.
- Any T1 no-go must use triangle-specific corner/ray structure, as Thm R (concave case) and FA §10.2 (ray matching) do.
- R10b's Conjecture R10b is consistent with this, since its programme ends in FA's ray system. It should say explicitly that the chart-level PB §§5–6 statements must not imply non-coverage on their own.

---

## Overlap check with v19, NAL and NOGO

### Theorem M
**At the level of covered targets, Theorem M is known machinery.**
1. **The formula is NAL prop:average.** NAL prop:average(i)–(ii) (nonadditive_losses.tex, §"Concave maps on all gambles") already has q·Ψ = min over M_q = Σ q_i A_i, {q·Ψ > 0} = D_{K_q} with K_q = ν(M_q), and K_q = Σ_i q_i K_{e_i} when A_i ⊆ Δ ("the best credal set at q is the q-mixture of the credal sets of the ideal models"). Thm M(b) is this formula with M_i = A_i. Prop V4's converse (K_p = Σ p_i V_i) is prop:average(ii) verbatim. R10a cites neither.
2. **(M1) is NAL prop:average(iii)'s condition** for never rewarding a wrong acceptance (A_i contains a positive multiple of e_i). NAL shows that on **all** gambles, full truth-directedness forces A_i ⊆ (0, ∞)e_i, i.e. normalised boxes (also NAL cor:all-gambles, v19 prop:global-concave). The affine-contamination non-example is the decomposable-domain shadow of NAL thm:belief ("rewards some wrong rejections when ε > 0").
3. **Every Thm M target is a v19 concave-CPM target.** Restrict f to the convex cone V = D_{K′} with K′ ⊆ ri K_{p*} close to K_{p*}, so that cl D_{K_{p*}}∖0 ⊆ V ⊆ Av (compactness). Then f is a concave CPM on V = {P_{K′} > 0} in v19's sense (app:concave):
   - by v19 prop:concave-envelope its supergradient sets lie in cone(e_i ∪ K′), and v19 prop:concave-converse is the converse;
   - its q-contractions are D_{K_q} ∩ V, coherent for every q ∈ Δ (prop:contraction, lem:indiff-null);
   - it realises D_{K_{p*}} non-tangentially.
   On the U-domain with U = V (the evaluable models are the measurable subsets of V; V ∩ −V = ∅, so the advice range is {+,0} on the choice represented by g ∈ V, {−,0} on the choice represented by g with −g ∈ V, and every evaluable model gives no advice on pairs {g, −g} with g ∉ V and −g ∉ V), this is a full coverage system (R1 Thm 2.2(S); v19 Bayes bridge §9). So the non-convex domain Av is **not needed** for coverage. Coverage of these targets therefore follows from v19 + NAL.
4. **What is new in Thm M:**
   - (a) the compatibility condition (M2), shown to be exactly what makes the NAL mixture strictly sign-preserving on the **maximal** Av = ∪ D_{V_i};
   - (b) its link to Thm V / Cor V2. Every system's Av has the union form ∪ D_{V_i}, so gauge mixtures are the canonical additive systems with prescribed vertex models;
   - (c) explicit advice ranges {+,0,−} on Av ∩ −Av.
   The hexagon u ± (e_i − u)/3 is a new instance of the class v19 already exhibits (ex:lp-hexagon realises the D₃-symmetric hexagon u − (e_i − u)/5, u + 2(e_i − u)/11 with an LP map; ex:box-realisation gives box hexagons).

So "Theorem M is v19's concave CPM realisation, written as NAL's mixture of ideals, on a non-convex union-of-cones domain" is an accurate description. The union-of-cones packaging and (M2) are the new parts.

### Prop M′
**"Covered targets arbitrarily close to T1" is already implied by v19.** v19 cor:approx-all realises, for **every** compact convex L (T1 included), the parallel bodies K_t = (1−t)L + tq₀ + taB_H ⋐ int Δ exactly by LP maps. They are non-tangential at full-support priors (lem:nontangent), so they are covered with (LF), and d_H(K_t, L) = O(t). NOGO §§5–6 says the same ("Approximate the target: already solved by (5.1)"). R10a's own sentence ("complements the parallel-body approximations") concedes this, but §0 calls M′ a new positive construction.

What is new: the approximants are **polygons** (9-gons with three long edges parallel to T1's and tents at T1's vertices), realised by concave maps, and they contain T1(ε′). NOGO §4 already notes that "other polygonal targets have positive results". M′ adds polygonal targets *arbitrarily close to T1*. Together with Thm R, this locates the obstruction for concave charts precisely in the triangle's three corner rays and two-crossings-per-coordinate combinatorics, not in flat facets.

### Theorem R
- **Not implied by v19 thm:hs-nogo.** That theorem concerns concave CPMs on **halfspace** domains D_p, where coordinates have the separable perspective form G(t) = Σ g_i(t_i) (lem:hs-reduce). Its targets are **parallel bodies** (rounded segments; rounded bodies with one flat face), and it works through singular points on coordinate slices (lem:hs-slices). Thm R allows any convex domain (in fact any neighbourhood of cl D_K∖0) and non-separable concave coordinates, and its targets are triangles. Neither theorem implies the other. For n = 3 and a triangle, lem:hs-slices only forces the three edge rays to be covered by pairs sharing a coordinate value, which generic p need not violate.
- **Not implied by v19 prop:global-concave / NAL cor:all-gambles** (concave CPMs on all of ℝⁿ realise exactly normalised boxes, so no triangle) except in the special case where the domain is ℝⁿ. Thm R extends that exclusion to arbitrary domains.
- **NOGO implies the contamination case.** Gauge mixtures restricted to V = D_{K′} (above) are continuous weak-sign maps on an open convex conic domain containing the nonnegative orthant and the closed target cone, with convex contractions. These are exactly NOGO §1's hypotheses. So NOGO (n = 3, every interior contamination baseline, §2) already excludes Cor R1 for T1.
- **The mechanism is NOGO §4's** (facet linearity, crossing rows, ray matching). Concavity forces the facet factors ξ ≡ 1, so (2.4) fails without the box, exactly as R10a's "Comparison with NOGO" says.
- **What is new:**
  - the extension from contamination triangles to **every triangle in general position** (NOGO §1 explicitly does not cover general triangles; the TRIANGLE_STATUS evidence there is numerical);
  - no use of boundary priors (box);
  - a self-contained one-page proof;
  - validity for every p* ∈ Δ and for concavity only near ∂D_K.
- **Possible strengthening:** combined with NAL cor:concave-ingredients, Thm R also excludes general-position triangles for nondegenerate monotone aggregations of strictly sign-preserving concave error losses on a convex domain. In that case the surviving rule is the Bayes set of one concave map Ξ with strict signs.

---

## What the round establishes (corrected summary)

**Unconditional**, under the BRIEF2 axioms: additive or (for Thm V) arbitrary rankings, strict (G), (LF) at an interior target.
- **Vertex anchoring** (R10a Thm V, R10b Prop V). Acceptance by every evaluable model is confined to nonnegative gambles, and Av off {h ≤ 0} is a union ∪ D_{V_i} with e_i ∈ V_i, compatible tuple. This closes R4 Remark B3. (H0)_{U′} reduces to non-adjacency.
- **Box step on decomposable domains** (R10b Lemma FS; R10a Lemma E plus the limit step). It no longer needs (K4) or (H0).
- **No plateau** at any target with two crossing vertices (R10b Thm PL), for merely measurable charts and with adjacency allowed. This covers T1 (all ε), every interior triangle, interior segments, and contamination in every n ≥ 3. Single-vertex pinning is also excluded when there are no adjacent exterior pairs (Cor PL2).
- **Gauge mixtures** (R10a Thm M) are complete additive systems on decomposable domains. As a class of covered targets they coincide with contractions of v19 concave CPMs (NAL prop:average formula). They cover polygons arbitrarily close to T1, but no triangle in general position (Thm R).

**Conditional (unchanged):** the T1 no-go of R1 Thm 4.2 / R4 Cor B2–C3, now without (H0), still conditional on NOGO + PB + FA and (H1) / (H1⁺).

**Open (unchanged in kind):** T1 in the zero-exterior-ratio regime, where covered polygons near T1 also live, with adjacency allowed away from p*. Any closure must exploit the triangle's corner rays.

---

## Requested edits, in priority order
1. R10a Theorem O: move "plateaus are excluded" out of the unconditional list, or cite R10b Thm PL for it.
2. R10a Lemma E remark / Cor C: replace "(K4) replaced by Lemma E" with R10b Lemma FS, or add the Hausdorff-limit step.
3. R10a §0 and §4: cite NAL prop:average (formula, (M1), K_p = Σ p_i V_i) and v19 app:concave / cor:approx-all. Describe Thm M's novelty as (M2) plus the maximal-Av packaging, and M′'s novelty as "polygonal approximants".
4. R10a Cor V3: add "mixed h", plus R10b V4's remark on nonnegative gambles accepted by every evaluable model.
5. R10a Prop V4: restate as necessity plus the vertex-coherence converse; delete "exactly" and the third bullet.
6. R10b §7: replace the "opposite rays / > π" argument with the tangent-counting proof above.
7. R10a §1 / R10b §1: use the repaired shrink N′ for lower-dimensional K.
8. R10b Lemma D: "relatively open in Γ_v"; rename the concentric balls.
9. R10a Cor R1, second bullet: add the concavity argument for strict boundary signs. Note that Thm R holds for all p* ∈ Δ.
10. R10a/R10b: state that Thm V / Prop V use strict (G) and do not transfer to Σ_T systems or the D_Δ exception.
