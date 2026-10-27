# REF64_bx: second referee report on the new sections of the covering paper (25 Oct 2026)

**Labels.**
- **CORRECT**: the statement is true and the proof is complete.
- **GAP**: true, or true once re-scoped, but the proof or the wording needs a repair.
- **ERROR**: a sentence that is false as written.

**What was refereed.** `Covering coherent sets of desirable gambles (draft).tex` and its PDF (43 pages, compiles cleanly), in its revised form; see `W64_changes.md` §§R1–R7. The binding framework is the one in `BRIEF64.md`.

**Sources checked against.**
- `PC64_notes.md` and `REF64_pc_notes.md`;
- `O61_notes.md` §§3–5 (Lemmas 1–4, Theorems A and B, and the general form of B);
- `REF62_R2_notes.md` row 24 (the pari-mutuel upgrade);
- `FD62_notes.md` item 6.

**Scripts.** My own exact scripts are in `r64/ref64bx_py/`. They use Fractions and sympy only and were written independently of `pc64py/`, `ref64pc_py/` and `w64py/`. Run each with `python3 -I <name>.py`; each writes `<name>.out`.

| script | what it checks |
|---|---|
| `g3.py` | Helpers: exact 2-D hull in aff Δ₃, inward facet normals, world types via Lemma 4.16, and visibility tested from Definition 4.11(a) directly |
| `ex67.py` | Example 6.7 in full: geometry, data identities, (LF) margins, the second-level identity (symbolic), sign condition (SC), 𝟙-monotonicity, and the target identity on 20 000 rational gambles. Lemma 6.3 on 288 admissible triples (8 648 tests), including boundary priors and every formal W₀. A convex-chart control |
| `geom_checks.py` | Lemma 6.5(a)–(c) on 3 000 exact boxes and (b) on 2 000 cevian segments; Corollary 6.6 (⇐) on 400 exact class-X triangles; the two test triangles of open problem (4); Example 7.17; Theorem 7.16(d) on 299 random pairs (L, K₀) |
| `ccc_check.py` | Consistency of §8.3 item (1) with Corollaries 6.6 and 7.9: the number of all-crossing (CCC) vertices by triangle class, on 6 000 triangles |

I also re-ran the author's `w64py/t_check.py`. It agrees with my scripts.

---

## Verdict table

| # | Item | Verdict | Repair (details in the sections below) |
|---|---|---|---|
| 1a | Lemma 6.2 (box chart) and Lemma 6.3 ((SC), null ties, coherent minimisers) | **CORRECT** | Optional: the sentence after Lemma 6.3 should also say "compact" (§1.1) |
| 1b | Theorem 6.4 (veto–box: one exempt normalised box, possibly degenerate, β possibly on ∂Δ, any n) | **CORRECT** | Optional wording on the case where β has zero coordinates (§1.2) |
| 1c | Lemma 6.5 (box geometry) | **CORRECT** | — |
| 1d | Corollary 6.6 (veto–box targets among interior triangles = V ∪ X) | **CORRECT** | One misattributed reason in the proof (§1.4) |
| 1e | Example 6.7 (the cover of T) | **CORRECT** | Every requirement of Definition 2.5 verified; optional strengthening of the last sentence (§1.5) |
| 2 | Corollary 7.9 (reach of the paper's constructions on interior triangles) | **GAP** | The chart-ranking step cites Theorem 5.7 outside its hypotheses. The claim holds on *every* domain, and a three-line argument is given in §2. The composition clause is correctly scoped, but paraphrases elsewhere drop the scope |
| 3 | Theorem 7.16(d) | **CORRECT** | Optional: note that K is a polygon whenever L is |
| 4 | Proposition 8.17 (strengthened) | **CORRECT** | Optional: the symbol T is used for the tangent cone and also for the maps T_q, T_{m′} (§4) |
| 5a | §8.3 item (1): scope against O61 Theorem B as corrected in REF64_pc | **ERROR (missing hypothesis)** | The class omits (G), and without (G) the sentence is false (explicit counterexample in §5.1). Add (G), or replace "has D_K undominated and all undominated models coherent" by "covers K". The scope is otherwise exactly right |
| 5b | §8 against Example 6.7 | **CORRECT** (no contradiction) | — |
| 5c | §8.5, "would have to lie outside every class above" and "reached by none of the constructions examined" | **GAP (scope)** | Overstated for pari-mutuel models other than R. A short corollary (proof in §5.3) closes the veto–box and chart cases in every n |
| 6a | Open problem (4): the caveat | **GAP (wording)** | "Strictly stronger" is not established. Say that the conjecture would settle the reversed-triangle case negatively. Say that its "if" half is Corollary 7.9. Carry Corollary 7.9's L⋆K₀ qualifier (§6) |
| 6b | Open problem (4): the two test triangles | **CORRECT** | Both are exactly as described: two bad vertices joined by a non-cevian edge, outside class X, with one and two cevian edges respectively |
| 7a | Global: introduction, item (3) | **ERROR (wording)** | "two non-visible vertices" must read "exactly two non-visible vertices". As written, "exactly these" includes triangles with three bad vertices that are not veto–box targets (§7) |
| 7b | Global: conventions (no names on theorem-like environments, \coloneqq, no draft commentary, "models") | **CORRECT** | grep-checked: no `\begin{…}[…]`, no `:=` or `=:`, no references to earlier drafts or notes |
| 7c | Global: numbered results contradicting each other | **CORRECT** (none found) | — |

---

## 1. Section 6

### 1.1 Lemmas 6.2 and 6.3, and the concave second level

Every step was checked by hand. The concave box chart enters the route of §3 in exactly two places.

**(a) Uniqueness (null ties).**
- g = Σ_{ω∉W₀} α_ω φ_ω − Σ_j β_j c_j.
- φ_ω(h + t𝟙) ≤ φ_ω(h), because v·𝟙 ≥ 0 on B_ω (Lemma 4.2(c)).
- c_j(h + t𝟙) ≥ c_j(h) + t l_j. The chart is concave and positively homogeneous in one variable, hence superadditive, and c_j(t) = l_j t for t ≥ 0.
- So g(h + t𝟙) ≤ g(h) − t β·l.
- Applied at h + s𝟙, this makes t ↦ g(h + t𝟙) strictly decreasing on all of ℝ, which is what Lemma 3.8 needs. g is continuous on ℝⁿ.
- Only β·l > 0 is used, and this holds for every β ∈ ℝⁿ₊∖{0} because l ≫ 0. So boundary priors and degenerate coordinates (l_j = u_j) are covered.
- CHECKED: 0 failures of g(h + t𝟙) ≤ g(h) − t β·l over 288 triples, including β = e₁, e₂, e₃, (1,1,0), (0,1,1) and (1,0,1).

**(b) Coherence.**
- For β_j ≥ 0, β_j c_j(h) = min over ρ_j ∈ [l_j, u_j] of β_j ρ_j h_j. So −Σ β_j c_j = max_{ρ∈R} (−(β⊙ρ)·h).
- With α ≥ 0, a sum of maxima over independent choices is the maximum of the sums. So g = max_{w∈W} (−w·h), where W = β⊙R + Σ α_ω B_ω is compact and lies in ℝⁿ₊, with 𝟙·w ≥ β·l > 0.
- Hence {g < 0} = D_{ν(W)}. Then N(W₀) = D_{K′} ∩ ⋂_{W₀} D_{Â_ω} a.e. (proof of Lemma 4.3), so X\* = D_{K(W₀,β,α)} globally, not merely on U.
- CHECKED on Example 6.7's ranking:
  - 0 failures of g = max_W (−w·h);
  - 0 failures of X\* = D_{K(triple)}, over 8 648 tests, every formal W₀ ⊆ Ω with supp β ⊆ W₀, and α₃ ∈ {0, 1, random}.
- Control: with the convex chart max(h₁, 6h₁) at world 1, the Bayes set at β = (1,1,0), W₀ = {1,2}, is not convex. An exact witness is in `ex67.out`. So concavity is genuinely used: it is what turns the second level into a maximum of linear functionals.

**Optional wording.** The sentence after Lemma 6.3 says that coherence uses only that the combined integrand "is a maximum of linear functionals −w·h with w ≥ 0 and 𝟙·w > 0". It should read "…over a compact set W ⊆ ℝⁿ₊ with 𝟙·w > 0 on W". Compactness gives an attained maximum and a compact ν(W). Without it, {sup < 0} and D_{cl ν(W)} can differ.

### 1.2 Theorem 6.4

Correct as stated.
- (Ω, β, ∅) is admissible, W = β⊙R, and Â_ω = conv A_ω. So K(Ω,β,∅) = K.
- Theorem 3.7(c) gives that D_K is undominated.
- Lemma 4.5(a) gives D_K ∈ 𝓜_U and (LF).
- Theorem 3.7 with Lemma 6.3 gives the rest: (G), (IB), (GC), (C), (ID), (W), the exact family and ties.
- Nothing uses n = 3.

The remarks after the theorem are right:
- R = {𝟙} with β = p recovers Theorem 4.9 for every p ∈ Δ.
- R = {r} induces the same order as VB(K′,B).
- A = ∅ and β = 𝟙 recovers the one-sided case of Proposition 5.9.

*Optional.* "The exempt set ν(β⊙R) is a normalised box" holds literally only when β ≫ 0. When β has zeros, it is a normalised box of the face Δ_{supp β}, and a vertex e_j when |supp β| = 1. Say so in one clause.

### 1.3 Lemma 6.5

- **(a)** Both inclusions are correct, including the step that excludes m_i = 0.
- **(b)** Correct, including the reduction to τ ∈ (0,1) and the parametrisation ν(a + te_l) = (1−τ′)a + τ′e_l. CHECKED: 0 failures on 2 000 random cevian segments.
- **(c)** Correct.
  - Dimension count: no degenerate coordinate gives a hexagon, one gives a quadrilateral, two give a segment, three give a point.
  - Edges lie on the six cevian lines.
  - Never a triangle. In log coordinates the three normals of a putative triangle must be the alternating triple e₂−e₁, e₃−e₂, e₁−e₃ (or its negative), since the six candidates are 60° apart and must positively span H. Each vertex then forces one coordinate to be degenerate.
  - CHECKED on 3 000 exact boxes: hull sizes 6/4/2/1 for 0/1/2/3 degenerate coordinates, 750 each; never 3; 0 non-cevian edges; (a) membership 0 mismatches.

### 1.4 Corollary 6.6

Both directions are correct.
- **(iii)⇒(ii).** Case (V) is Corollary 4.17, and VB = VBox with R = {𝟙}. In case (X): c = (k + εe_j)/(1+ε); the box of Lemma 6.5(b) gives ν(R) = [a,b]; and conv{k, c, a, b} = T. CHECKED exactly on 400 random class-X triangles: hull identity, membership of A_j, and k ∈ relint T; 0 failures.
- **(i)⇒(iii).**
  - Lemma 4.5(b) gives K′ ⊆ relint T, and Theorem 3.7(c) with Lemma 2.3 gives T = K(W₀,β,α).
  - Taking v_ω = 0 ∈ B_ω gives ν(β⊙ρ) ∈ T ⊆ relint Δ, so supp β = Ω = W₀.
  - Vertices in Â_ω are visible. So bad vertices lie in E.
  - Three bad vertices would give T = E, which Lemma 6.5(c) forbids.
  - With two bad vertices, the supporting line meets E in a face with two points, so it is cevian.

*Wording.* "here t ≠ 0, t ≠ 1 because e_ω ∉ relint Δ": that reason gives only t ≠ 1 (x ∈ T ⊆ relint Δ). Here t ≠ 0 follows from the previous sentence (x ∉ K′), and it is not needed anyway, since Lemma 4.12(a) allows t ∈ [0,1). Write "here t < 1, because x ∈ relint Δ".

### 1.5 Example 6.7: every requirement of Definition 2.5

Data CHECKED exactly (`ex67.out`):

| item | result |
|---|---|
| Facet normals | (2,2,−3) [p,q], non-cevian; (−1,4,−1) [q,s], non-cevian; (0,−1,1) [p,s], cevian through e₁ |
| World types | p ACC, q CAS, s TCC |
| Visibility (from Definition 4.11(a)) | p none; q world 3 only; s none |
| Barycentric coordinates of k | (1/10, 3/5, 3/10) |
| Identities | q = (10/11)k + (1/11)e₃; ν(1,2,2) = p; ν(6,2,2) = s; hull{k,q,p,s} = T |
| k·r at the extreme rays of C_T (integer rays) | 3/10, 1/10, 3/25 > 0. These equal the text's 3/250, 3/125, 1/250 at rays scaled by 1/25 |
| Second level | Σc = min(5p·h, 10s·h), symbolically on both branches; the difference is 5h₁ |

| requirement (Definition 2.5) | where it comes from | verdict |
|---|---|---|
| (i) strict (G), (IB) | Lemma 3.2 with (SC): φ₃ = max(0, −q·h) vanishes on U ∩ {h₃ ≥ 0}, because q ∈ conv(K′ ∪ e₃) (Lemma 4.2(b)); c_j has the sign of h_j | CORRECT. 0 failures on 20 000 gambles |
| reflexive, a.e. ties, (TC) | total preorders (Lemma 3.2) | CORRECT |
| (ii) global coherence | Lemma 6.3 with Theorem 3.7(e); X\* = D_{K(triple)} with K(triple) ⊇ K′, globally | CORRECT. 0 failures over 288 triples |
| (iii) direct (C) | Theorem 3.7(d): tied at every world ⇒ a.e. equal | CORRECT |
| (iv) D_T ∈ 𝓜_U and undominated | k ∈ T gives D_T ⊆ U; triple (Ω, 𝟙, ∅) with the factor-2 chart; N(Ω) ∩ {Σc > 0} = D_k ∩ D_q ∩ D_p ∩ D_s = D_T a.e. | CORRECT. Target identity: 0 mismatches on 20 000 gambles |
| (v) incoherent-model dominance | Lemma 2.6(a): (W) together with (C) | CORRECT |
| (vi) (LF) | Lemma 4.5(a), k ∈ relint T | CORRECT |
| Domain conditions | U = D_{k} is an open half-space, one-sided; 𝓜_U is decomposable by construction; T is full-dimensional; μ satisfies (M), with the Lebesgue clause after (M) | CORRECT |

**Boundary priors and degenerate boxes in the example.**
- R is degenerate in coordinates 2 and 3.
- W₀ ⊇ {1,2} for every undominated model, since worlds 1 and 2 have no veto.
- Formal triples with W₀ = {3} give D_{conv(k,e₃)} = U ∩ {h₃ > 0}, the world-best model. It is coherent, as Theorem 2.9 requires.
- All of these were tested.

**Scoped exclusions stated in the example.**
- Not orthant-planar (Theorem 5.10): correct, since it has a non-cevian edge.
- Not a VB target (Corollary 8.4): correct, since it has two non-visible vertices.
- "Not L⋆K₀ with π\* ∈ relint Δ" (Theorem 7.8): correct.
- *Optional:* since T ⊆ relint Δ forces π\* ∈ relint Δ (as in the proof of Corollary 7.9), the example can say "not of the form L⋆K₀ at all".

---

## 2. Corollary 7.9

**(⇐)** Correct. Classes V and X come from Corollary 6.6. All-cevian triangles are orthant-planar by Theorem 5.10 and covered by Theorem 5.7.

**(⇒)** The veto–Brier and veto–box cases are correct: both are VBox rankings on 𝓜_{D_{K′}}, so Corollary 6.6 (i)⇒(iii) applies. The composition case is correct as scoped: T = L⋆K₀ ⊆ relint Δ forces π\* ∈ relint Δ, and Theorem 7.8 then applies.

**GAP: the chart-ranking case.**
- The proof treats chart rankings on ℝ³ or on D_{K′} and cites Theorem 5.7 for the undominated family.
- Theorem 5.7 assumes K′ ⊆ relint K₀. The corollary needs arbitrary K′, since K₀ need not be the target.
- The family formula itself holds for every domain. Its proof uses only Theorem 3.7(c) and Lemma 5.3.
- The step "T = conv(K′ ∪ ν(π⊙K₀)) ⇒ T = ν(π⊙K₀)" is fine, but it is special to D_{K′}.

**Repair.** The following argument holds on every domain U, so the statement can say "a chart ranking of an orthant-planar credal set, on any domain":
- By Theorem 3.7(c) and Lemma 5.3, D_T = U ∩ D_E a.e., where E := ν(π⊙K₀) and π ≠ 0. By Lemma 2.3, E ⊆ T.
- Suppose a vertex x of T lies outside E. Choose h with min_T m·h = 0 attained only at x. Then h ∈ ∂D_T∖{0}, and h ∈ D_E, because m·h > 0 on T∖{x} ⊇ E and E is compact.
- (LF) puts a ball around h a.e. inside U. D_E is open, so a smaller ball lies a.e. in U ∩ D_E = D_T. But every ball around h ∈ ∂D_T contains a non-null open set outside cl D_T.
- So ext T ⊆ E, and T = E. The rest of the proof (π ≫ 0, deciding vectors d_σ⊙π, Theorem 5.10) is unchanged.

**Scope.** The statement correctly restricts the composition clause to "a composed ranking with a target of the form L⋆K₀ of Theorem 7.3". Two places paraphrase the corollary without that qualifier:
- open problem (4) ("the ones covered by the constructions of this paper");
- introduction item (3) (which cites only Corollary 6.6, so that one is fine).

Either add "in the sense of Corollary 7.9" to open problem (4), or prove the extension: an interior triangle that is any undominated (LF) model of a composed ranking. I did not find a complete short proof of the extension. When Q = K(Ω,β,∅) is not full-dimensional, Theorem 7.8 does not apply verbatim. So keep the qualifier.

**Equivalence with open problem (4)'s formulation.** "Every edge joining two non-visible vertices is cevian" is equivalent to "V ∪ X ∪ all-cevian":
- with 0 or 1 bad vertex the condition is vacuous;
- with 2, it is (X);
- with 3, it says all edges are cevian.

So the two formulations agree.

---

## 3. Theorem 7.16(d)

Checked line by line. **CORRECT.**
- n = 3 and S = {a,b}.
- By (b), K ∩ Δ_S = ν(π\*⊙K₀) is a nondegenerate segment [x⁻, x⁺] on {m_c = 0}, and it is an edge of K. The ratio m_a/m_b runs over [ρ⁻, ρ⁺] with ρ± = (π\*_a/π\*_b)θ±, where θ⁻ < θ⁺ because K₀ is full-dimensional.
- Suppose every edge line is cevian. The second edge at x⁺ cannot pass through e_a or e_b (that line is {m_c = 0}, which carries only one edge). So it lies on {m_a = ρ⁺m_b}, and K ⊆ {m_a ≤ ρ⁺m_b}, since x⁻ is on the strict side. Likewise K ⊆ {m_a ≥ ρ⁻m_b}.
- Full-dimensionality of L gives q ∈ relint L with q_a/q_b ≠ π\*_a/π\*_b. Then ν(q⊙m±) violates one of the two bounds.
- The hypothesis "e_i ∉ L for i ∈ S" enters through (b).

CHECKED:
- Example 7.17 is exactly as stated: five vertices, normals (16,−1,−2), (4,0,−1), (−4,8,−1), (0,0,1), (4,−1,4), three of them non-cevian. L has types CCS, CCC, ASC.
- On 299 random pairs (L with π\* ∈ relint Δ_{12}; K₀ a random 2-D box or a random cyclic-type triangle), 0 cases had all edge lines cevian.

*Optional.* Add "(this holds whenever L is a polygon, since K₀ is a polytope by Lemma 5.5(a) and Lemma 7.4 applies)".

---

## 4. Proposition 8.17 (strengthened)

Checked line by line. **CORRECT.** No (LF) is used. The scope is exactly one zero coordinate, and the text says so.
- **Setup.** By Theorem 7.3 and Lemma 2.3, K = Q⋆K₀ with Q = K(W₀,β,α) of VB(L′,A). Since L′ ⊆ relint L ⊆ relint Δ, Proposition 7.15 applies with K″ = L′. The face K ∩ Δ_S = conv{v_i : i ∈ S} has n − 1 ≥ 2 extreme points of support exactly S.
- **dim K₀ = 0.** T_{p₀} is a support-preserving bijection of Δ that preserves extreme points both ways. So Q ∩ Δ_S has n − 1 ≥ 2 extreme points of support S. This contradicts Proposition 7.15.
- **dim K₀ ≥ 1.** The tangent cone of K at v_k is cone{e_i − e_k}. Among ±(e_j − v_k) only v_k − e_k lies in it; this uses n ≥ 3 and p_i > 0 for i ≠ k, and each case was checked. The copy T_q(K₀) has v_k as a vertex, and its edges are cevian by Lemma 5.5(c).
  - Lemma 5.5(b)–(c) hold for orthant-planar K₀ of any dimension. Re-checked: the proof of (b) uses only openness of σ and orthant-planarity. For dim K₀ = 1, K₀ is itself its unique edge, and (c) applies.
  - So every edge direction at v_k is a positive multiple of v_k − e_k.
  - dim ≥ 2: a vertex lies on two edges with independent directions, which is impossible.
  - dim 1: K₀ lies on a line through e_k. The generators of K ∩ Δ_S do not depend on m′. So Q ∩ Δ_S = T_{m′}⁻¹(K ∩ Δ_S), which again contradicts Proposition 7.15.
- **"In particular K ≠ L⋆K₀."** Correct, via Theorem 7.3.

*Notation (optional).* The proof uses T for the tangent cone, alongside the maps T_q, T_{m′}, T_{p₀}, and Proposition 7.15 uses T for a generating set. Rename the cone (e.g. 𝒯 or T_K(v_k)).

---

## 5. §8.3 item (1) and §8 against Example 6.7

### 5.1 ERROR: (G) is missing from item (1)

Item (1)'s class has:
- finitely many non-negative measurable veto levels;
- then an error level that is nonzero a.e. on its veto-free set and convex on an open convex G;
- then any further levels;
- on a one-sided U ⊆ G with (LF).

Strict guidance is never required. O61's standing hypotheses for Lemmas 1–4 and for Theorem B include (G), and Definition 8.7 (𝒱_B) states it explicitly. Without (G) the sentence is false:

**Counterexample (in the literal class, K = R).**
- Fix p ∈ relint R and take U = D_{K′} with K′ ⊆ relint R.
- At *every* world, use the same two levels:
  - the veto ∫_X max(0, −min_{m∈R} m·h) dμ;
  - the error level ∫_X (−p·h) dμ, which is linear (hence convex on G = ℝ³) and nonzero a.e.
- All worlds share one total preorder, so the undominated models are its minimisers.
  - Veto 0 forces X ⊆ C_R a.e.
  - The error then forces X = U ∩ C_R ∩ {p·h > 0} = D_R a.e.
- So D_R is the unique undominated model: it is coherent, and D_R is undominated. (G) fails.

**Repair.** In item (1), write "…then any further levels, and that satisfy (G), on a one-sided domain…". Alternatively, replace "No such ranking has D_K undominated and all undominated models coherent" by "No such ranking covers K". (G) is part of covering, and O61 needs only D_K undominated and the X_kj coherent.

*Optional.* "The collar mechanism of Lemma 8.11" refers to a lemma stated for 𝒱_B. Its proof uses only Lemmas 8.8–8.10, which hold for any vetoes-then-strict-error ranking with (G). Say so in a clause.

### 5.2 Scope against O61 Theorem B as corrected in REF64_pc: matches

- (a) R and every pari-mutuel triangle in relint Δ₃.
  - All three vertices are invisible, of type ACC, so the collar reaches all three faces.
  - The ray system has det = u₁ + u₂ + u₃ − 1 = δ ≠ 0 (O61 Theorem B; REF62_R2 row 24).
- (b) Every polytope in relint Δ₃ with at least two all-crossing (CCC) vertices: O61's general form. A CCC vertex is automatically invisible.
- The text no longer calls the pari-mutuel vertices "all-crossing". This is exactly REF64_pc item 9's corrected scope.

### 5.3 No contradiction from Example 6.7

- Example 6.7's ranking *is* in item (1)'s class. It has one veto at world 3, then error levels −c_j:
  - −c₁ = max(−h₁, −6h₁) is convex;
  - −2h₂ and −2h₃ are linear.
- T has no CCC vertex (types ACC, CAS, TCC) and is not pari-mutuel. Its facet (0,−1,1), i.e. m₃ ≥ m₂, is not an upper-bound constraint. So item (1) does not apply.
- Theorem 8.12 (𝒱_B): the cover is not in 𝒱_B. On N_v world 1's weight is 1 or 6 according to the sign of h₁, against a constant weight at worlds 2 and 3. T also has only one invisible vertex (p), since s is tangential from world 1.
- Corollary 8.16 (two cevian edges): T has one.
- Proposition 8.14: q is visible.
- Theorem 8.3 and Corollary 8.4: consistent (two non-visible vertices).
- CHECKED (`ccc_check.out`, 6 000 triangles): class X had 0 CCC vertices in every case, and class V at most 1. All-cevian triangles have none, since a zero coordinate in a normal kills crossing at that world. So no target in Corollary 7.9's reach meets item (1)'s second clause. Class N triangles have up to 2 CCC vertices, consistent with the conjecture.

### 5.4 GAP: §8.5 overstates the scope for pari-mutuel models other than R

- "A ranking covering them would have to lie outside every class above": items (2)–(6) concern R only, and item (1) concerns n = 3 only. So for other pari-mutuel models, and for n ≥ 4, the sentence claims more than is proved.
- "Reached by none of the constructions examined": true for R, by Corollaries 6.6, 8.4 and 8.15, item (1), and the non-orthant-planarity of R. For n ≥ 4 the paper's own veto–box and chart constructions are not addressed.

**Repair.** Add the following short corollary (proof checked), and reword §8.5 as "a ranking covering R would have to lie outside every class above; for the other pari-mutuel models, outside the classes whose exclusions apply to them".

*Corollary.* For n ≥ 3, no pari-mutuel model K ⊆ relint Δ is an undominated (LF) target of a veto–box ranking on some 𝓜_{D_{K′}}, or of a chart ranking of an orthant-planar credal set on any domain.

*Proof.*
- Veto–box. As in Corollary 6.6 (i)⇒(iii), whose steps 1–3 do not use n = 3: supp β = Ω, and every non-visible vertex lies in E = ν(β⊙R). All vertices of K are non-visible (Corollary 8.5(a)). So K = E, a normalised box, which is orthant-planar (Proposition 5.9). That contradicts Lemma 5.5(d), since the facet normals u_i𝟙 − e_i have no zero coordinate.
- Chart. By §2's repair, K = ν(π⊙K₀) with π ≫ 0, which is orthant-planar. The same contradiction follows. ∎

---

## 6. Open problem (4)

**The test triangles: CORRECT** (`geom_checks.out`).

| triangle | types | facet normals | cevian edges | bad vertices | edge joining them | class |
|---|---|---|---|---|---|---|
| conv{(1,6,1)/8, (6,1,3)/10, (6,1,1)/8} | CCC, CAT, SCA | (17,3,−35), (−1,6,0), (−1,−1,7) | 1 | (1,6,1)/8 and (6,1,3)/10 | non-cevian | N (not X) |
| conv{(6,4,1)/11, (6,1,3)/10, (6,1,1)/8} | CTC, CCT, SAA | (11,−12,−18), (−1,6,0), (−1,0,6) | 2 | (6,4,1)/11 and (6,1,3)/10 | non-cevian | N (not X) |

Both are interior, have exactly two bad vertices joined by an edge on no cevian line, and are outside class X, as the text says.

**The caveat: GAP (wording).**
- The "only if" half does imply that the reversed triangle is not covered: R has three bad vertices and no cevian edge. Correct.
- But "so the conjecture is strictly stronger than the open case of problem (1)" asserts a non-implication that is not proved, and cannot be while both are open.
- **Repair:** "…implies that the reversed triangle is not covered. So proving the conjecture would settle the simplest open case of problem (1), negatively."
- Also add: "The 'if' half holds by Corollary 7.9, so the content of the conjecture is its 'only if' half."
- Write the sentence before it as "the ones covered by the constructions of this paper, in the sense of Corollary 7.9, are exactly…" (see §2).

---

## 7. Global consistency pass

1. **Introduction, item (3): ERROR (wording).**
   - The text reads: "in three worlds this covers every interior triangle with two non-visible vertices joined by such an edge, and among interior triangles the veto–box targets are exactly these and the veto–Brier targets (Corollary 6.6)".
   - Triangles with *three* non-visible vertices, two of them joined by a cevian edge, exist: PC64's census has hundreds with one or two cevian edges. They are not veto–box targets by Corollary 6.6, unless all three edges are cevian. In the latter case they are chart targets, but still not veto–box targets, since T = E is impossible.
   - **Repair:** "every interior triangle with exactly two non-visible vertices, joined by such an edge".
2. **Abstract.** "in three worlds this covers triangles that lie in neither of the first two classes": correct.
3. **Remark after Corollary 8.16** (a two-cevian triangle whose bad pair is joined by a cevian edge is a veto–box target): correct. It is consistent with Corollary 8.16, which excludes only VB, orthant-planar and interior composed targets.
4. **Remark 7.10 and open problem (5)** no longer assert non-necessity in n ≥ 4: consistent.
5. **The sentence after Theorem 3.7** says every ranking of §§4–7 is a two-level integral ranking with (SC), null ties and coherent minimisers. This includes §6 via Lemma 6.3: consistent.
6. **Remark 4.20(3)** ("K ⊆ relint Δ is used only in Corollary 4.18 and in the exclusions of Section 8") is scoped to §4. Corollaries 6.6 and 7.9 also assume relint Δ, but they state it.
7. **Conventions.**
   - No theorem-like environment carries an optional name.
   - No `:=` or `=:` appears (`\eqqcolon` is used once, correctly).
   - There is no reference to earlier drafts, rounds or notes.
   - Objects are called "models" throughout.
   - Dominance nomenclature (weak, dominance, strict, uniform) is as in Definition 2.4.
8. **No numbered result contradicts another.** I checked §6 against Theorems 4.9 and 8.3, Corollaries 8.4 and 8.16, Theorem 8.12, item (1), and Theorems 7.8 and 7.16.

---

## Ranked list of required changes

1. **§8.3 item (1): add (G)** (or say "covers K"). As written the sentence is false (§5.1).
2. **Introduction, item (3): "two non-visible vertices" → "exactly two non-visible vertices"**. As written, "exactly these" is false (§7.1).
3. **Corollary 7.9, chart-ranking step: replace the appeal to Theorem 5.7** by the general-domain argument of §2, valid on any domain. Then the statement can say "on any domain" for chart rankings.
4. **Open problem (4).**
   - Replace "strictly stronger" by "would settle the reversed-triangle case of problem (1) negatively".
   - Note that the "if" half is Corollary 7.9.
   - Add "in the sense of Corollary 7.9" (the L⋆K₀ qualifier) to the reach sentence.
5. **§8.5: re-scope** "would have to lie outside every class above" to R, and state the classes that apply to other pari-mutuel models. Optionally add the short corollary of §5.4 (no pari-mutuel model is a veto–box or chart target, any n ≥ 3).
6. **Minor (optional).**
   - (a) After Lemma 6.3: "maximum over a compact W ⊆ ℝⁿ₊ with 𝟙·w > 0".
   - (b) After Theorem 6.4: when β has zeros, ν(β⊙R) is a normalised box of the face Δ_{supp β}.
   - (c) Proof of Corollary 6.6: "here t < 1 because x ∈ relint Δ".
   - (d) Example 6.7, last sentence: "not of the form L⋆K₀ at all", since π\* must be interior.
   - (e) Theorem 7.16(d): "K is a polygon whenever L is".
   - (f) Proposition 8.17: rename the tangent cone T.
   - (g) §8.3 item (1): note that Lemma 8.11's proof applies to any vetoes-then-strict-error ranking with (G).

**Overall.**
- The new positive material is correct under the binding framework: Theorem 6.4, Lemmas 6.2, 6.3 and 6.5, Corollary 6.6 and Example 6.7.
- The concave second level is handled correctly: uniqueness uses only β·l > 0, and coherence uses only the max-of-linear-functionals form over a compact subset of ℝⁿ₊.
- Theorem 7.16(d) and the strengthened Proposition 8.17 are correct.
- What remains is one false sentence (item 1, missing (G)), one wording error in the introduction, one citation gap with an easy general repair (Corollary 7.9), and scope wording in §8.5 and open problem (4).
