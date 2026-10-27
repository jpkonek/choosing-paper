# REF64_paper — Referee report on "Covering coherent sets of desirable gambles (draft)" (25 Oct 2026)

Referee: REF64_paper. Adversarial, journal standard. I wrote none of the paper and none of its sources.
I read the whole `.tex` (2825 lines; the PDF is 38 pages, built 22:03 from the 22:02 source; the log has no warnings, no undefined references and no overfull boxes). I checked every proof by hand. For the priority items I also checked the cited sources.

Labels: PROVED / CHECKED (exact computation) / CONJECTURE / NUMERICS.
Verdicts: CORRECT / CORRECT (minor) / GAP / ERROR.
- "CORRECT (minor)" means the mathematics is right but the text needs a wording or citation fix.

Scripts are in `ref64paper_py/` and were written independently of `w64py/`. They use integer and Fraction arithmetic only. Run each with `python3 -I <name>.py`.
- `polyhull.py`: an exact cone-hull routine. Facets come from signed maximal minors, vertices from the rank of the active facets, edges from the rank of common facets.
- `check_examples.py` → `check_examples.out` (≈4 s). It covers:
  - Remark 4.20(1);
  - Examples 5.11, 5.12, 6.13 and 6.16;
  - the Theorem F(c) facet map;
  - Corollary 6.12's facet;
  - the triangle in open problem (4).
- `check_n3.py` → `check_n3.out` (≈11 s). This is a randomized exact test of Theorem 6.8 and Lemma 6.6:
  - 300 random polygons L with at most one non-visible vertex;
  - four orthant-planar K₀: the cyclic triangle, the hexagon, a box, and a one-dimensional cevian segment.

---

## 0. Bottom line

1. **No mathematical ERROR was found in any numbered result.**
   - Every new write-up on the priority list is CORRECT: Lemma 5.4, Lemma 5.5, Lemma 6.6, Theorem 6.8, Proposition 6.14, Theorem 6.15 with Example 6.16, Proposition 7.17, and Theorem 6.11 with its hypothesis "no zero coordinate".
   - I checked each proof line by line. The computed examples reproduce exactly (§3).
2. **The framework section is sound.**
   - Lemma 2.6 is correct, and correctly scoped: (a) uses no order property, and (b) uses transitivity only.
   - Lemma 2.8, Theorem 2.9 and Proposition 2.10 use (G) only, and no (TC), (IB), transitivity or completeness.
   - No proof in §§2–6 silently uses completeness or transitivity outside the classes where Lemma 3.2 supplies them.
   - Every construction is correctly said to be complete and transitive and to give (W).
   - **Remark 2.7 is a GAP of wording.** Its three-model configuration satisfies neither (G) nor (IB) and does not live on 𝓜_U. So it does not show what the sentence "Without transitivity, (GC) does not imply (C)" says inside the framework.
3. **The three positive theorems match their refereed sources, with no scope drift.** Theorem 4.6/4.9/4.14, Theorem 5.7 and Theorem 6.3 were checked against REF61/W62, REF62_fd/REF62_R2 and RC63/REF63_comp respectively.
   - There is one small overreach in the introduction ("in three worlds, composition produces no new target inside the open simplex"). Theorem 6.8 proves this only for targets of the form L⋆K₀ with (L).
4. **§7 is honest in spirit, but §7.3 has scope drift in three items.** In each of these the paper states a broader domain or regularity class than the source proves:
   - **Item (2)** (E61 Cor 5.2) omits the hypothesis that the vetoes are convex and the gains concave *on an open convex set containing C_R∖{0}*.
   - **Item (6)** (IN63 Thm C) says "a one-sided domain with (LF)". IN63 proves it for an *open convex one-sided cone* U ⊇ C_R∖{0}.
   - **Items (4)–(5)** (C62, DC63) say "open convex one-sided domain". The sources need an open convex *cone* with no h ≤ 0.
   - Item (5) correctly carries (C2) at π\*, as REF63_neg requires. Items (1) and (3) match their sources. Item (3) cites the wrong result for "R is not orthant-planar".
   - All six items are stated as flat assertions without proof or a published citation. A journal version cannot keep them in this form.
5. **§7.5 and the introduction never suggest that pari-mutuel models are impermissible.** §7.5 says the opposite explicitly. The contamination exclusion (Proposition 7.17) is correctly scoped to centres with exactly one zero coordinate, and the text says that two or more zeros are untreated.
6. **Citations.**
   - Confirmed by external sources: Rockafellar Thm 11.6, Schrijver Cor 7.1a and Cor 7.1h.
   - Consistent with the book's numbering, but not confirmed by an external quotation: Rockafellar Thms 6.3, 11.3 and 13.2, and Schrijver §8.5.
   - The uses of all of them are correct (§5).
7. **Conventions.**
   - There are no names on theorem-like environments, \coloneqq is used, there is no commentary on earlier drafts, the dominance nomenclature is standard, and objects are called "models".
   - Three small lapses: "=:" at line 1198; the undefined terms "anti-visible" and "crossing" in Example 5.11; and the symbol F_x reused in the proof of Theorem 6.11.

---

## 1. Verdict per numbered result

### §2 Framework

| Result | Verdict | Notes |
|---|---|---|
| Lemma 2.1 (D_S) | CORRECT | (c) by strict separation from a compact convex S₁. |
| Lemma 2.2 | CORRECT | (d) uses Rockafellar 11.6 with D = {x}: correct. |
| Lemma 2.3 | CORRECT | Uses int cl C = int C for convex C with nonempty interior (Rockafellar 6.3). |
| Def 2.4 and the paragraph after it | CORRECT | "Weakly dominates but does not dominate ⇒ tied at every world" uses only the definition of ≺. Uniform dominance and strict dominance coincide for finitely many worlds: correct. |
| Def 2.5 (cover) | CORRECT | Matches BRIEF64 item by item: (G), (IB), (GC), (C), D_K a model and undominated, (ID), (LF). (G), (IB) and (LF) are verbatim from W62 §2. |
| **Lemma 2.6** | **CORRECT** | (a): if Y ∈ 𝒞\* weakly dominates an incoherent X but does not dominate it, they are tied at every world, and (C) makes X coherent. No order property is used. (b): uses transitivity twice and nothing else. This agrees with REF64_or's `w62dom` record system, which has (G), (IB) and (TC) on atoms, and in which X is tied with an undominated Y yet is dominated. |
| **Remark 2.7** | **GAP (wording)** | The configuration is a correct (TC) relation (I re-derived it: the only strict pair is Z ≺ X, and X ⪯ Z fails). But it has one world, three abstract models, and no (G), (IB) or 𝓜_U. So it shows only that "(TC) + (GC) ⇒ (C)" fails *for abstract relations*. Inside the framework the question is not settled by it. **Repair:** say "the derivation in (b) needs transitivity; for abstract relations with (TC) the implication fails, as this configuration shows. We do not know whether (G), (IB), (TC) and (GC) together imply (C). This is why (C) is listed as a requirement." Optionally add a record-level witness with (G), (IB) and (TC), as in REF64_or `w62dom.py`, labelled as a witness on atoms. |
| **Lemma 2.8** | **CORRECT** | Uses (G) at world i only. |
| **Theorem 2.9** | **CORRECT (minor)** | All five steps re-derived. (G) enters only through "for instance (GC)" via Lemma 2.8. The "exactly one" logic is compressed but complete. (i) If all pairs intersect, Step 5 gives that U is essentially one-sided. (ii) If some pair is disjoint, Step 4 gives Q_l = {e_l} for all l, hence U ⊇ {some h_l > 0} a.e. (iii) (b) contradicts (a). Suggest writing (i)–(iii) as three sentences. **Wording:** the introduction says "or the full domain", but (b) is "U contains every gamble that is not a sure loss". The abstract's "essentially the full domain" is acceptable if defined. |
| **Proposition 2.10** | **CORRECT (minor)** | The generalisation to any domain is fine. "The vector h is not ≥ 0 with all coordinates positive…" is garbled. What is needed is that h is neither strictly positive nor strictly negative, so it has one coordinate ≥ 0 and another ≤ 0, and every ball around it meets the open set M. Rewrite. |

### §3 Two-level integral rankings

| Result | Verdict | Notes |
|---|---|---|
| Def 3.1, Lemma 3.2 | CORRECT | Total preorders. (IB) by differences of integrals. (G) under (SC). |
| Lemma 3.3 (Lyapunov) | CORRECT | — |
| Lemma 3.4 (Zorn) | CORRECT | Re-derived the chain lower bound coordinate by coordinate. |
| Lemma 3.5 | CORRECT | Proper separation (Rockafellar 11.3) of the open cone P from E; β ≠ 0 argument correct. Remark: "J(X) = ∫_X g whenever X ⊆ N(W₀)" in fact holds for every X. Harmless. |
| Lemma 3.6, Theorem 3.7, Lemma 3.8 | CORRECT | (d): ties at every world give z(Y) = z(X) by antisymmetry of ≤_lex. (e): needs only Lemma 2.6(a); citing 2.6(b) as well is unnecessary. |

### §4 Veto–Brier (PROVED-ref; re-checked)

| Result | Verdict | Notes |
|---|---|---|
| Def 4.1, Lemmas 4.2, 4.3, Thm 4.4 | CORRECT | The max-of-sums identity for g, and {φ_ω = 0} = D_{Â_ω} a.e., are both correct. |
| Lemma 4.5, Thm 4.6, Rem 4.7, Cor 4.8, Thm 4.9, Rem 4.10 | CORRECT | — |
| Def 4.11, Lemmas 4.12, 4.13, Thm 4.14, Cor 4.15 | CORRECT | — |
| Lemma 4.16, Cors 4.17–4.19 | CORRECT | Cor 7.1h is used correctly (the right-hand side gives η₊ − η₋ ≥ 0). |
| Remark 4.20 | CORRECT | (1) CHECKED. Facets (−21,19,9), (0,1,−1), (14,−16,9). v has types TAC, and w = v + (v − e₁)/3. |
| Text on smooth sets (KL balls) | CORRECT (minor) | Say "G convex and differentiable on an open convex subset of aff Δ containing the set (for KL: relint Δ)". The argument is local, and "critical point ⇒ minimiser" needs a convex domain. |
| Props 4.21, 4.23, 4.24, Lemma 4.22, Cor 4.25, Prop 4.26, Cor 4.27, Prop 4.28, Prop 4.29 | CORRECT | Re-derived the TV computation δ + s(δ − p_j) and the supermodular telescoping. The constant-odds-ratio witness (1/5, 3/10, 1/2) is in the core and violates m₃ ≤ 2m₁. |

### §5 Orthant-planar targets

| Result | Verdict | Notes |
|---|---|---|
| Def 5.1, Lemma 5.2, Lemma 5.3 | CORRECT | Both inclusions of the closed-orthant identity, and the pure orthants in the pullback. |
| **Lemma 5.4 (ratio criterion)** | **CORRECT** | (a): with λ = min_P m_a/d_a, m·h ≥ λ d·h. (b): the ratio bound comes from h_δ = x e_a − e_b + δw ∈ σ (in σ for every δ > 0). The point m with m·h = 0 is forced to equal λd because h has no zero coordinate. λ > 0 uses K ⊆ relint Δ. The "hence" clause follows. |
| **Lemma 5.5 (obstruction)** | **CORRECT** | (a): C_K is a finite union of polyhedral cones, hence finitely generated (Schrijver 7.1a). K is recovered by Lemma 2.1(c). (b): d_σ·g = 0 because g ∈ cl(D_K∩σ) ∖ D_K. Then nesting of open half-spaces makes both minimisers proportional to d_σ. (c): faces are exposed, and H ∖ ⋃_l(H ∩ e_l^⊥) is nonempty because e_l ∉ span{a,b} exactly when the line ab misses e_l. (d): a facet has dimension n − 2 ≥ 1, and its normal is unique up to positive scale, so "no zero coordinate" is well defined. Neither (b) nor (c) uses full-dimensionality, which matters for §6. |
| Def 5.6, Theorem 5.7 | CORRECT | Null ties: {g = 0} ⊆ Z ∪ finitely many hyperplanes. (LF) needs K′ ⊆ relint K, which is stated (REF62_R2's repair is incorporated). |
| Cor 5.8 | CORRECT | — |
| Prop 5.9 | CORRECT | The paragraph after it ("two coordinates at upper bounds ⇒ not visible, tangential from those worlds") is correct by Lemma 6.10 and Lemma 4.16. It tacitly needs a coordinate at its lower bound and l_j < u_j. |
| **Theorem 5.10** | **CORRECT** | Sufficiency through log coordinates. The six roots e_a − e_b are 60° apart. f strictly between two adjacent roots has a unique maximiser, and that maximiser is locally constant, so it is constant on the connected cone Γ. Necessity is Lemma 5.5(c). |
| Example 5.11 | CORRECT (minor); CHECKED | Vertices, facets, all six deciding vertices, types ATC/CAT/TCA, and products 64 and 8, all as stated. "Anti-visible" and "crossing" are **undefined** in the paper: define them (F_x ⊆ {h_j ≥ 0}; both signs) or say "not weakly visible". |
| Example 5.12 | CORRECT; CHECKED | Six facets exactly as listed, all with a zero coordinate. Products 8 and 44/5. Exactly three vertices non-visible (ATT, TAT, TTA). |

### §6 Composition

| Result | Verdict | Notes |
|---|---|---|
| (L), Def 6.1, Lemma 6.2 | CORRECT | (a): the null sets of μ_c are checked orthant by orthant. (b): μ_c(Φ(X)) = μ(X∩O), since c⁻¹(c(X∩O)) misses Z. (c): the scores are identical. |
| Theorem 6.3 | CORRECT | Geometry: T_m(relint L) ⊆ relint K. Φ⁻¹(D_{K(W)}) = D_{K(W)⋆K₀} needs K(W) ⊇ L′, which is noted. The target comes through Theorem 4.9 under μ_c. Matches RC63/REF63_comp. |
| Lemma 6.4 | CORRECT | — |
| Lemma 6.5 | CORRECT | — |
| **Lemma 6.6 (three-world sector)** | **CORRECT** | Re-derived in full. The six rays ±ℝ₊g^{ij}_x are those of three distinct lines, so the six sectors each have angle < π. Crossing a ray flips exactly one sign, so the counts of positive coordinates alternate 1, 2. The closure of a 1-positive sector is cone{g^{ij}, g^{ik}}; the bounding rays are identified correctly. The (⇒) case analysis (0, 1, or ≥2 rays; a 2-positive sector forces a third ray) is complete, using pointedness (angle < π). Uniqueness comes from two distinct lines (they cannot both pass through e_j and e_k). Disjointness: M_i ∩ M_j makes m_i/m_j constant. CHECKED on 300 random polygons × 4 K₀: no failures. |
| Lemma 6.7 (decoupling) | CORRECT | — |
| **Theorem 6.8** | **CORRECT** | Route: N(L) ≤ 1 with equality iff π\* ∈ M_i(L). Lemma 5.4(b) gives w_i for K₀ of any dimension. Lemma 6.5 sends non-visible extreme points of K into ν(π\*⊙K₀). Lemmas 6.6 and 6.7 give equality. Uniformity uses finitely many points ν(π\*⊙w), w ∈ ext K₀. CHECKED by `check_n3.py`: N(L⋆K₀) = N(L) in all 1200 cases, including the one-dimensional cevian segment K₀. **Scope:** the theorem is about targets L⋆K₀ with (L). The introduction's "in three worlds composition produces no new target inside the open simplex" should say "no new target of the form of Theorem 6.3". An undominated (LF) model D_{Q⋆K₀} with Q = K(W₀,β,α) is reduced to the (L) form only partly, by the first lines of the proof of Proposition 7.14. That reduction does not prove L′ ⊆ relint Q. |
| Remark 6.9 | GAP (unsupported claim) | "An exact computation on an example shows that it is not necessary" gives neither the example nor a reference. Either give the example (CC63 §4.7; REF63_comp C14) with its data, or delete the clause. The same applies to open problem (5). |
| Lemma 6.10 (two-pair rule) | CORRECT | — |
| **Theorem 6.11** | **CORRECT** | (b): the chain w_j q_a m_a ≥ w_j q_j m_a ≥ q_j w_a m_j. Equality forces q = ū by (F), and y_a = α_a, y_j = β_j (the normalisation of y is harmless: y_j/β_j = y_a/α_a gives both = 1). ν is injective on {y_a = α_a} and segment-preserving, so extremality holds. The count is 2^{n−1} − n. (c): η′ = η ⊘ x\* is a facet normal with η's zero pattern, and dimension n − 2 is preserved by the homeomorphism T. Lemma 5.5(d) then applies (K ⊆ relint Δ since L ⊆ relint Δ). The hypothesis "no zero coordinate" is exactly what Lemma 5.5(d) needs. It is stronger than CC63's "≥ 3 nonzero coordinates", so the theorem is narrower than CC63, not broader. That is safe. CHECKED: every facet of L in Example 6.13 maps under η ↦ η ⊘ x\* to a facet of K. **Notation:** the face F_x in (b) clashes with the normal cone F_x. Rename it (e.g. G_x). |
| Corollary 6.12 | CORRECT; CHECKED | The ε-bound: v_{j,a} − v_{j,b} ≥ (1−ε)(p_a − p_b) − ε > 0 iff ε < (p_a − p_b)/(1 + p_a − p_b). The facet normal e_k − (1−ε)p_{0,k}𝟙 has no zero coordinate. For Example 6.13 the qualifying k are 3 and 4, and both normals are facets of L. |
| **Example 6.13** | **CORRECT; CHECKED independently** | v₁–v₄ as printed. 70 distinct generators. K has 32 vertices, 63 edges and 33 facets (Euler characteristic 2). Exactly five non-visible vertices, as listed: (1,2,2,2) ATTT, (2,1,2,2) TATT, (1,1,2,2) AATT, (1,2,1,2) ATAT, (1,2,2,1) ATTA, all tangential from two or three worlds. The first four are Theorem F(b)'s. Six facets have no zero coordinate, including (−19,−19,−19,362) and (134,−57,−57,94). Facets by number of nonzero coordinates: 12/15/6. The closing scope sentence ("we do not claim … outside every class with a veto level followed by a Brier-type level") is as AUDIT requires. |
| **Proposition 6.14 (face count)** | **CORRECT** | G = K\*∩Δ_S is a face, and ext G ⊆ T∩Δ_S. Points of K″ have full support, and points of Â_ω have full support or equal e_ω (support of size 1 < |S|). The W-points with support in S form a box. ν maps convex combinations of corners to convex combinations of their images. The support of a corner is supp β ∪ {ω ∈ M : T_ω > 0}, which determines the corner. |
| **Theorem 6.15 (BE)** | **CORRECT; (d) vacuous** | (b): L∩Δ_S = {π\*}, because points of L′ and A_i have full support or are e_i (excluded for i ∈ S). So K∩Δ_S = ν(π\*⊙K₀). It is not a point because ratios vary on the full-dimensional K₀. (c): Theorem 4.4, Lemma 2.3 and Proposition 6.14. No (LF) is needed. (d) "not orthant-planar, since it meets rbd Δ" is true by definition and carries no information. **Repair:** delete (d), or replace it by a remark, or by REF63_comp's argument that some edge line of K is non-cevian, stated with its hypothesis. The pentagon already shows three non-cevian edges. |
| **Example 6.16 (pentagon)** | **CORRECT; CHECKED independently** | L's facets are (−2,2,−1), (1,−1,2), (4,−1,−1), with vertex types CCS, CCC, ASC. (L) holds via Corollary 4.15. The five vertices and five facets of K are exactly as printed. The boundary edge is ν(π\*⊙K₀) = [(2/3,1/3,0), (1/5,4/5,0)]. Three facet normals have no zero coordinate. The only non-visible vertices are the two boundary ones (TAC, ATA), as BE(b) predicts. |

### §7 Exclusions

| Result | Verdict | Notes |
|---|---|---|
| Lemma 7.1 | CORRECT | Uses Rockafellar 13.2 and the bipolar theorem. Uses are correct. |
| Remark 7.2 | CORRECT | U = int cl U for open convex U (Rockafellar 6.3) is implicit. cl U ≠ ℝⁿ follows from U ∩ (−U) = ∅. |
| Theorem 7.3 | CORRECT | — |
| Cor 7.4, Cor 7.5 | CORRECT (minor) | 7.5(c) should say "full-dimensional", since the proof's first sentence assumes it. The abstract's "open convex one-sided domains" should read "open convex one-sided cones containing the positive orthant" (Remark 7.2). |
| Proposition 7.6 | CORRECT | Both cases re-derived. In the case |S| = 1, ν(w)₁ = (1−ε)/(1+ε) < 1 − ε. |
| Def 7.7, Lemmas 7.8–7.11 | CORRECT | Complete, transitive class. Lemma 7.11's spreading step is re-derived (r = λp + (1−λ)q, λ = t/(1+t)). The induction over the overlap graph is correct. |
| Theorem 7.12 | CORRECT (minor) | "A polytope K has at most one invisible vertex" needs K full-dimensional. That is forced by (LF) on a one-sided domain (Proposition 2.10), but say so. One-sidedness is not used elsewhere in the proof (W64 flag 2 is right), so keep it as a stated hypothesis matching O61. |
| Cor 7.13 | CORRECT | — |
| §7.3 preamble | CORRECT (minor) | (a) "In items (2)–(5) a chart is …" should be (3)–(5); item (2) has no chart. (b) Say π ∈ ℝ³₊∖{0} in (C2) and (C3). (c) "By Theorem 3.7 the certificate with (LF) suffices" is correct: (C1) is (SC), (C2) is null ties, (C3) gives coherent minimisers, (C4) gives the target. |
| §7.3 item (1) | CORRECT (unproved in paper) | Matches O61 Thm B (𝒱_conv; G ⊇ A) and the PMM upgrade (REF62_R2 row 24). |
| §7.3 item (2) | **GAP (scope drift)** | E61 Cor 5.2 needs φ_v convex and −σ_v concave *on an open convex set containing cl D_K∖0*. Its domain is a one-sided decomposable U with (LF). The paper's item omits where convexity and concavity hold. Without that, "concave" is undefined on non-convex U. **Repair:** add "on an open convex set containing C_R∖{0}". |
| §7.3 item (3) | CORRECT (minor) | The first part matches R15 (SH)+(DF)+(ND) and A62 Cor 2.3. The paper's chart is positively homogeneous, which narrows the source's class; that is safe. The second part matches REF62_fd Thm R1(a)–(b) as refereed by REF62_R2 (all-prior certificate). **Fixes:** (i) "with Theorem 2.9 and Corollary 7.15" should be "with Theorem 2.9 and Lemma 5.5(d)": R is not orthant-planar because its facet normals have no zero coordinate. Corollary 7.15 is about composed rankings. (ii) "Any two-sided domain" should be "any domain that is not essentially one-sided", which is Theorem 2.9's dichotomy. (iii) R1 uses (C3) at boundary priors π = e_i through Theorem 2.9's B_i. That is fine under the all-prior certificate. |
| §7.3 item (4) | **GAP (scope drift, small)** | C62 (U): an open convex *cone* containing cl D_K∖0 with no h ≤ 0. The paper says "open convex one-sided domain". **Repair:** add "cone". |
| §7.3 item (5) | CORRECT (minor) | (C2) at π\* is carried, as REF63_neg requires. Fix "domain" to "cone" as in item (4). DC63 allows *measurable positive* scalar functions s_σ per cell, not only constants. The paper's "positive scalar factor per cone" is narrower, which is safe, but could be stated at full strength. |
| §7.3 item (6) | **GAP (scope drift)** | IN63 Thm C is proved for an *open convex one-sided cone* U ⊇ cl D_K∖0 with no h ≤ 0 (IN63 §1), with concave gains on U. The paper says "a one-sided domain with (LF)". **Repair:** restrict to that cone. "Views jointly strictly guiding" should be defined as IN63's (SG). |
| §7.3 final paragraph | CORRECT (could be sharpened) | The (TP) step holds in these classes. OR64 (Prop 2.6; refereed by REF64_or) shows further that the priority regions used in items (1), (2) and (6) are *strong*, so (TP) is not needed at all. Optional: say so once REF64_or's verdict is final. |
| Proposition 7.14 | CORRECT | — |
| Cor 7.15 | CORRECT | PMM facet normals u_i𝟙 − e_i have no zero coordinate, so Lemma 5.5(d) applies. |
| Cor 7.16 | CORRECT | Opposite open angles are disjoint and miss every edge line. Two cevian edges pass through different vertices of Δ. Scoped to π\* ∈ relint Δ, as REF63_comp C11 requires. |
| **Proposition 7.17** | **CORRECT; scoped correctly; can be strengthened** | Dimension 0: n − 1 ≥ 2 distinct extreme points of L with support Ω∖{k} would all equal π\*. Dimension ≥ 2: every edge direction of T_q(K₀) at v_k is a positive multiple of v_k − e_k (verified: only v_k − e_k among ±(e_j − v_k) lies in the tangent cone, using n ≥ 3 and p_i > 0), contradicting the ≥ 2 independent edge directions at a vertex (Ziegler). Dimension 1: K₀ lies on a cevian line through e_k, the face over Ω∖{k} equals T_{m′}(L ∩ Δ_{Ω∖{k}}), and it collapses to at most one point. **Typo:** "{e_j : j ≠ k, e_j ∈ K}" should be "e_j ∈ L". The conclusion is the same, since e_j ∈ L ⇒ e_j ∈ K and no e_j lies in K. **Possible strengthening (PROVED here, sketch):** "D_K is not an undominated model of any composed ranking." Replace L by Q = K(W₀,β,α). The dimension-0 and dimension-1 cases then follow from Proposition 6.14, with K″ = L′ ⊆ relint Δ and S = Ω∖{k}, and the dimension ≥ 2 case is unchanged. This makes the statement parallel to Proposition 7.14 and Corollary 7.15. The authors' choice. |
| Text after 7.17; §7.5 | CORRECT | The two-or-more-zeros case is explicitly untreated. Nothing says that PMMs are impermissible. |

### §8 Open problems
- CORRECT as open problems.
- (4) is correct as stated, and its test triangle is CHECKED: one cevian edge, two non-visible vertices (CCC, CAT).
- Forward flag: PC64 (this round, **not refereed**) claims a cover of a different partially cevian triangle, which would answer (4) negatively. If its referee confirms the claim, (4) and the "two-cevian" test case must be revised. Until then the paper is right to omit it.
- (5) repeats the unsupported claim of Remark 6.9.

---

## 2. Required changes, ranked

1. **§7.3: fix the scope drift and the proof status.** Without these changes the section states more than the sources prove.
   - (a) Item (6): restrict to an open convex one-sided cone U ⊇ C_R∖{0} with no h ≤ 0, and define "jointly strictly guiding" as (SG).
   - (b) Item (2): add "convex/concave on an open convex set containing C_R∖{0}".
   - (c) Items (4)–(5): "domain" should be "cone".
   - (d) Item (3): replace "Corollary 7.15" by "Lemma 5.5(d)", and "two-sided" by "not essentially one-sided".
   - (e) The preamble: "items (2)–(5)" should be "(3)–(5)", and add π ∈ ℝ³₊∖{0}.
   - (f) For publication, every item needs a proof, an appendix or a citation to a published or preprint version. As it stands these are theorems without proofs. At minimum, head the section "Announced results (proofs in [refs])" and soften the abstract's "provably fail" for these items.
2. **Remark 2.7: reword** as in §1. Optionally add a record-level (G)+(IB)+(TC) witness. Do not claim that (C) is independent of the other requirements inside the framework.
3. **Remark 6.9 and open problem (5):** give the CC63 §4.7 example and its data, or delete "an exact computation on an example shows that it is not necessary".
4. **Theorem 6.15(d):** delete it, or replace it by a substantive statement with its hypothesis (REF63_comp's non-cevian-edge argument).
5. **Introduction scope sentences.**
   - (a) "In three worlds, composition produces no new target inside the open simplex" should be "… no new target of the form L⋆K₀ (Theorem 6.3)". Or add the reduction lemma for undominated (LF) models of composed rankings; this needs L′ ⊆ relint Q, which is not proved.
   - (b) Theorem 2.9's (b) should be described as "U contains every gamble that is not a sure loss", not "the full domain".
6. **(M) versus Lebesgue measure.** BRIEF64 takes μ to be Lebesgue measure or a measure with a positive density. (M) requires a finite measure with a first moment, so it excludes Lebesgue measure itself. Add one sentence: "The requirements depend on μ only through its null sets; (M) is used only to make the constructed scores finite. A ranking built with any μ satisfying (M) is a ranking in the sense of the framework for Lebesgue measure."
7. **Notation and definitions.**
   - Define "anti-visible" and "crossing" (Example 5.11), or avoid them.
   - Rename the box face F_x in the proof of Theorem 6.11.
   - Line 1198: "=:" should be \eqqcolon.
   - Proposition 7.17: "e_j ∈ K" should be "e_j ∈ L".
   - Proposition 2.10: rewrite the sentence "not ≥ 0 with all coordinates positive".
8. **Small hypotheses to make explicit.**
   - Cor 7.5(c): full-dimensional.
   - Theorem 7.12, last sentence: full-dimensional (forced by (LF)).
   - Abstract: "open convex one-sided cones containing the positive orthant".
   - KL-ball paragraph: name the open convex set on which G is convex and differentiable.
9. **Optional strengthening:** Proposition 7.17 for every composed ranking, via Proposition 6.14 (§1, row 7.17).
10. **Optional:** the closing paragraph of §7.3 can note that the regions used are strong priority regions, so (TP) is not needed there (OR64 Prop 2.6, subject to REF64_or).
11. **Non-mathematical:** the title page names a second author, carried over from W62. Confirm co-authorship with her before the draft circulates.

---

## 3. Exact re-verification (CHECKED; `ref64paper_py/*.out`)

- Remark 4.20(1): as stated.
- Example 5.11: vertices (1,4,2)/7, (2,1,4)/7, (4,2,1)/7.
  - Facets (−1,2,0), (0,−1,2), (2,0,−1).
  - Deciding vertices w₁, w₂, w₃, w₂, w₁, w₃ for P = {1}, {2}, {3}, {1,2}, {1,3}, {2,3}.
  - Products 64 and 8. No vertex visible.
- Example 5.12: six facets as listed, all cevian. Products 8 and 44/5. Three non-visible vertices.
- Example 6.13 / Theorem F:
  - v_j as printed; ε bound 1/11; (F) holds.
  - 70 distinct generators; 32 vertices, 63 edges, 33 facets.
  - Five non-visible vertices, with the types listed in §1.
  - Six facets with no zero coordinate; split 12/15/6.
  - The four Theorem F(b) corners are among the non-visible vertices.
  - Every no-zero facet of L maps to a facet of K under η ↦ η ⊘ x\*.
- Corollary 6.12: the qualifying k are {3, 4}, and both normals are facets of L.
- Example 6.16: L's facets and vertex types as stated; K's vertices and facets as stated; three non-cevian edges; the boundary edge is ν(π\*⊙K₀).
- Theorem 6.8 and Lemma 6.6: 300 random polygons × 4 orthant-planar K₀ (including a one-dimensional K₀). No failures.
- Open problem (4) triangle: facets (−1,−1,7), (−1,6,0), (17,3,−35); one cevian edge; vertex types SCA, CCC, CAT.

---

## 4. Framework audit (priority 2)

- **Completeness and transitivity.**
  - Neither is used in §2 except in Lemma 2.6(b), which names transitivity.
  - §3 obtains both from Lemma 3.2.
  - §§4–6 inherit them through Theorem 3.7.
  - §7.1–7.2 and §7.4 work inside complete, transitive classes and say so in the opening of §7.
  - The unanimity items (2) and (6) are transitive, and §7's opening paragraph says so.
- **Constructions.** Each is stated to be complete and transitive and to give (W):
  - Theorem 4.4;
  - Theorems 4.6 and 4.9 (W only; completeness and transitivity are inherited from 4.4);
  - Theorem 5.7;
  - Theorem 6.3 (and hence 6.11(a) and 6.15(a)).
  - The paragraph after Theorem 3.7 says this for all of them. Each is a two-level integral ranking with (SC), null ties and coherent minimisers. I verified this for the VB ranking (Lemma 4.3), the chart ranking (proof of Theorem 5.7) and the composed ranking (Lemma 6.2: the scores are transported, so (SC), null ties and coherent minimisers transfer).
- **(G), (IB) and (LF)** are verbatim from W62 §2. The cover definition lists exactly the BRIEF64 requirements. (W), (S), (B), transitivity, completeness, etc. are listed as not required.

---

## 5. Citations (priority 5)

| Citation | Use in paper | Status |
|---|---|---|
| Rockafellar Thm 6.3 (cl ri C = cl C; ri cl C = ri C) | Lemma 2.3: int cl D_S = D_S | Use correct. Number consistent with the book (§6: 6.1 line segment principle, 6.2 ri ≠ ∅, 6.3; arXiv:1101.3098 cites 6.5 and 6.6 for adjacent results). **Not externally quoted.** |
| Rockafellar Thm 11.3 (proper separation iff ri C₁ ∩ ri C₂ = ∅) | Lemma 3.5; Lemma 4.13 (in aff Δ) | Use correct (P open; open ray relatively open). Number consistent with the book. **Not externally quoted.** |
| Rockafellar Thm 11.6 (non-trivial supporting hyperplane containing D iff D ∩ ri C = ∅) | Lemma 2.2(d) | **Confirmed**: arXiv:1101.3098 (proof of Lemma 2.15) cites 11.6 for a supporting hyperplane, and W64 cites arXiv:1905.08157. Use correct. |
| Rockafellar Thm 13.2 (support functions = closed proper positively homogeneous convex functions) | Lemma 7.1 | Use correct (a finite sublinear function is closed). Number consistent (arXiv:1101.3098 cites 13.1 for the adjacent result). **Not externally quoted.** |
| Schrijver Cor 7.1a (cone polyhedral iff finitely generated) | §2 facts; Lemma 5.5(a) | **Confirmed**: Schrijver's own MPRI notes (lix.polytechnique.fr/~vjost/mpri/prelimILP.pdf) cite "Corollary 7.1a" for exactly this. Use correct. |
| Schrijver Cor 7.1h (affine Farkas) | Lemma 4.16 | **Confirmed** by the same notes ("Corollary 7.1h … affine variant of Farkas' lemma"). Use correct (the feasibility hypothesis holds: K ≠ ∅). |
| Schrijver §8.5 ("Minimal faces and vertices") | Cor 7.5 (vertex iff the active constraints and 𝟙 span ℝⁿ) | Use correct. The same notes cite §8.2 (dimension) and §8.3 (faces), consistent with §8.5 being minimal faces and vertices. **Not externally quoted.** |
| Ziegler (no number) | Proposition 7.17: a vertex of a d-polytope has ≥ d edges with spanning directions | The fact is standard and correct. Give a precise location if possible (e.g. the vertex figure, Lectures on Polytopes §2.1). |

Search results used: arXiv:1101.3098; lix.polytechnique.fr/~vjost/mpri/prelimILP.pdf. Several other arXiv papers were searched; none quoted 6.3, 11.3 or 13.2 by number.

---

## 6. Conventions (priority 6)

- No optional names on any theorem-like environment (checked by grep). ✓
- \coloneqq is used throughout. Exception: line 1198 "=:" (use \eqqcolon). ✓/minor
- No commentary comparing drafts, rounds or notes in the text. "W62" does not occur; the date line "Draft" is fine. ✓
- Dominance nomenclature: weak dominance, dominance, strict dominance, uniform dominance (Def 2.4 and the paragraph after it). ✓
- Objects are called "models" throughout. ✓
- Status labels: §7.3 is explicitly "recorded without proof". Examples 5.12 and 6.13 say "(Exact computation.)" and "An exact computation…". Remark 6.9 and open problem (5) do not give theirs (required change 3).
