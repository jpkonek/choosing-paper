# REF64_pc — referee report on PC64 (one partially cevian triangle) — 25 Oct 2026

Labels: CORRECT / GAP (true, or true once re-scoped, but the argument or wording needs a repair) / ERROR (a false statement).
Binding inputs used: `BRIEF64.md`, `AUDIT_r64_decisions.md` §3; background `W62_note.tex`, `P61_notes.md`, `O61_notes.md`, `C62_notes.md`, `FD62_notes.md`, `REF62_fd_notes.md`, `REF63_comp_notes.md`, `ROUND61–63_report.md`.

Referee scripts are in `r64/ref64pc_py/`. They were written independently of `pc64py/` and use Fractions/sympy only. Run each with `python3 -I <name>.py`; each writes `<name>.out`.

| script | what it checks |
|---|---|
| `rg.py` | own helpers. Strict visibility is tested from the **definition** (barycentric direction of v − e_j), not from generator signs |
| `t_cover.py` | geometry of T; data of the construction; the chart identity (symbolic); 𝟙-monotonicity; (G); (LF) and margin; the target identity |
| `t_family.py` | every kind of admissible triple (406 triples, incl. boundary priors, β₃ = 0, formal W₀): g = max over W, X\* = D_K(triple), closure under addition, strict 𝟙-decrease. Also a control with a *convex* world-1 chart |
| `t_scope.py` | concave-chart ray system; PL value system for several π\*; a direct 𝒱_B exclusion for T (exact witness); the forced-face system vs O61 Thm B; class of the paper's test triangle |
| `t_pl_sym.py`, `t_pl_null.py` | PL corner value system with symbolic π\* (determinant); null vectors when π\* has a zero |
| `t_bx3.py` | Cor BX3 ⇐ on 2 000 class-X triangles (exact hypotheses + exact hull); "normalised boxes are never triangles" (3 000 exact boxes); class-X structure; an independent recount of the small-integer census |

---

## Verdict table

| # | Item | Verdict | Repair / comment |
|---|---|---|---|
| 1 | T: one cevian edge [p,s] (line m₂ = m₃ through e₁); types ACC / CAS / TCC; bad vertices p, s; not orthant-planar; not VB-type | **CORRECT** | Re-derived exactly (`t_cover.out` §1). The definition test agrees with the sign test. |
| 2a | Cover: strict (G) and (IB); each ⪯_j a total preorder (so reflexive and (TC)) | **CORRECT** | q = (10/11)k + (1/11)e₃ exactly, so φ₃ = 0 on U ∩ {h₃ ≥ 0}. Charts are sign-correct (exact). |
| 2b | Existence of undominated weak dominators | **CORRECT** | W62 `lem:lyap`/`lem:zorn` verbatim. The integrand is (φ, −c) with \|c_j\| ≤ u_j\|h_j\|, and μ satisfies (M). The Gaussian is allowed by the binding "positive density" clause. |
| 2c | Every undominated model is coherent; exact family (W₀ = Ω, β ≠ 0 arbitrary) ∪ (W₀ = {1,2}, β₃ = 0, α₃ ≥ 0); boundary priors; π₃ = 0 | **CORRECT** | W₀ ⊇ {1,2} always, since worlds 1 and 2 have no veto. `t_family`: 406 triples (6 hand-picked boundary ones), 0 failures of g = max_W(−w·h), of X\* = D_K(triple), of closure on 24 360 pairs, and of strict decrease. Control: with c₁ = max(h₁, 6h₁), which is sign-correct but convex, the Bayes set at β = (1,1,0), W₀ = {1,2} is not convex (exact witness). So concavity is genuinely used. |
| 2d | D_T is a model and is undominated; unique minimiser at (Ω, β = (1,2,2), ∅) | **CORRECT** | Σc = min(5p·h, 10s·h) holds symbolically on both branches. So ν(β⊙R) = [p,s], and N(Ω) ∩ {Σc > 0} = D_k ∩ D_q ∩ D_p ∩ D_s = D_T a.e. (k = p/10 + 3q/5 + 3s/10). Role of the identity: it is exactly ν(W) = [p,s]. |
| 2e | Direct (C); incoherent-model dominance | **CORRECT** | Family (d), "tied ⇒ a.e. equal", gives direct (C). W62 `lem:dominance` uses completeness, which these rankings have. |
| 2f | (LF) at D_T; U one-sided; margin | **CORRECT** | k·r = 3/250, 3/125, 1/250 at the extreme rays; angular margin ≈ 0.0236. |
| 3 | Lemmas BX1–BX4, BX-family, **Theorem BX** (degenerate boxes, β on ∂Δ, any n) | **CORRECT** | Checked line by line (§B). The only new steps are BX1(c)–(d), BX3 and BX4, and all hold. The plain-English reason "convex vetoes + concave chart" is incomplete: coherence also needs W ⊆ ℝⁿ₊ with 𝟙·w ≥ β·l > 0. That is in BX4's statement, so the theorem is fine. |
| 4 | **Cor BX3** (veto–box reach on interior triangles = V ∪ X), both directions | **CORRECT** (scoped to VBox on M_{D_{K′}}) | ⇒ re-proved (§C). Step 4 verified exactly: 3 000 boxes give hull vertex counts 6/4/2/1 for 0/1/2/3 degenerate coordinates, never 3, and every edge is cevian. ⇐: 2 000 class-X triangles, all hypotheses of Thm BX and the hull identity exact, 0 failures. |
| 4′ | The 200-case check (`x_class.py`) | **GAP (label)** | It checks the *construction instances* (sign, veto guidance, and the target identity sampled on rational gambles). It does not check the criterion's ⇒ direction. Being sampled, it is NUMERICS-grade; the exact proof is Thm BX. Replace it by the exact hypothesis check (as in `t_bx3`). |
| 4″ | Census | **CORRECT** / **GAP (wording)** | Small-integer census reproduced exactly with an independent classifier (82 284 triangles; class X = 9 216 + 2 892 = 12 108; V, N, 3 match). The random-sample shares (16.8%, 31.4%) depend on the sampler, and partially cevian triangles are a null family. Strike "class X is about a sixth to a third of all partially cevian triangles" (§4.1) or say "under the stated sampler". |
| 5 | Proposed characterisation (VB ∪ orthant-planar) is false | **CORRECT** | From 1 and 2. |
| 6a | Exclusions: VB-type, R2 charts, composition | **CORRECT** | Cited refereed results (P61 V6, REF62_R2 §4, CC63 N3 / REF63 C1, C11); applicability checked. |
| 6b | No single-level concave chart | **CORRECT** | Steps re-derived. Ray determinant 1/625 (5 for integer rays). Every world with r_j ≠ 0 crosses on an adjacent facet; c₁(r_ps) = 0 by sign. π\* ≥ 0 with zeros is handled. Only "D_T undominated" plus (LF) is used, not global coherence. |
| 6c | No continuous PL single chart, "modulo C62 L4.2–4.4" | **GAP (scope)** | The "modulo" label is honest, but the object excluded is the **four-condition certificate** ((C2) null ties and (C3) near π\* included), not coverage under the binding framework. §0 item 6 and §6.2 ("never cover") overstate this. Referee addition: the value system has det = π₁π₂π₃/15625 (`t_pl_sym`), so it is nonsingular for **every** π\* ≫ 0. At π\* with one zero it has nullity 1 (`t_pl_null`), so the step "π\* ≫ 0" is needed. That step is forced: D_T contains −Σ_{i≠j}e_i + Me_j for large M, and strict sign-correctness then forces π\*_j > 0 (O61 Lemma 2 argument). State it. |
| 6d | No 𝒱_B ranking (measurable vetoes, then a Brier-type level with one common weight), "conditional on O61 Cor A(d)" | **CORRECT as labelled; upgradable** | The referee gives a direct proof for T (§D, exact witness in `t_scope` (3)). The exclusion can be labelled PROVED (referee; second check advised). The record on Cor A(d) itself is still inconsistent: O61 calls it a sketch, ROUND61 says "repaired for n = 3", and REF62_fd asked for this to be reconciled. |
| 7 | Lemma CM (corner mismatch) | **CORRECT** as linear algebra; **GAP (scope)** | (i) "What it excludes" must carry π\* ≫ 0. (ii) "(FL),(F) are C62 Lemmas 4.3–4.4 (refereed)": they are refereed for the reversed triangle only, so for N33 targets this is the same transfer as 6c. (iii) For direction-continuous charts, (FL) is DC63's lemma, with its hypothesis (C2) at u; name it. (iv) The paper's test triangle is class N∖N33 (types CCC, CAT, SCA; the second bad facet has forced coordinates {1,3} only), so CM does not reach it. |
| 8 | Replacement conjecture | **CORRECT label; GAP (scope)** | Its "only if" half contains non-coverage of the reversed triangle under the binding framework, the project's central open question. So it is strictly stronger than that question and must be stated so. Nearby **PROVED** statement (from BX3, REF62_R2 §4, CC63 N3): *the targets reached by every known architecture (VB, veto–box, R2 charts, composition) among interior triangles are exactly V ∪ X ∪ {all three edges cevian}.* |
| 9 | §5 "Consistency with O61 Thm B" and the §7 "For the paper" bullet ("vetoes then convex error must stay restricted to targets with an all-crossing non-visible vertex, such as the reversed triangle and the interior pari-mutuel triangles") | **ERROR (scope statement)** | The reversed triangle and the interior pari-mutuel triangles have **no** all-crossing vertex: every vertex is ACC. The correct scope (as in FD62 #6 / REF62_fd §3 and paper item (1)) is: (a) R and the interior PM triangles, whose three faces are all forced and whose ray system is nonsingular; (b) any target with ≥ 2 CCC vertices (Thm B general form). Also "s is outside Lemma 4" is the wrong reason. Collar forcing *does* reach F_s (§D; in the cover N ⊇ balls around relint F_s). The cover survives because the forced-face system on F_p ∪ F_s is solvable (x₂ = x₃; Γ = −min(5p·h, 10s·h)) and F_q is not forced (q is strictly visible, and q·h = 0 on F_q is the veto boundary). |
| 10 | (f) Does the cover contradict an earlier refereed theorem? | **No** | See §F. O61 Thm A, Cor A(d) and Thm B are all consistent. Only an unproved summary sentence (O61 §7, already corrected in ROUND61 by FD62 #6) and coverage-map status lines (ROUND62 §3, ROUND63 §5) are superseded. |

**Overall.** The cover of T is correct under the binding framework, and the proposed characterisation is refuted. Theorem BX and Corollary BX3 are correct. The repairs needed are to scope statements (6c, 7, 8, 9) and labels (4′, 4″). 6d can be upgraded.

---

## A. The cover of T: independent verification

- **Data (exact).**
  - bary(k) = (1/10, 3/5, 3/10).
  - q = (10/11)k + (1/11)e₃.
  - ν(1,2,2) = p and ν(6,2,2) = s.
  - The hull of {k, q, p, s} is T.
- **Chart.**
  - c = (min(h₁, 6h₁), 2h₂, 2h₃).
  - Sign-correct, including c_j = 0 at h_j = 0.
  - c(h + t𝟙) ≥ c(h) + t(1,2,2) for t ≥ 0, by superadditivity of a concave homogeneous function.
  - 𝟙·c = min(5p·h, 10s·h) (sympy, both branches; difference 5h₁).
- **Every requirement of the binding framework.** All are verified: (G); (IB); reflexive/(TC); Zorn; global coherence; target undominated; direct (C); incoherent-model dominance; (LF); one-sidedness. Each goes through W62 `thm:family` with the integrand changed. The changed steps are exactly BX1(c)–(d), BX3 and BX4 (§B).
- **No hidden hypothesis.** μ must be finite with a first moment (W62 (M)), so that the scores are finite. Lebesgue measure itself is not usable; a Gaussian is. PC64 states this. Completeness/transitivity are properties of the construction, not assumptions.

## B. Theorem BX: the proof re-checked

1. **Lemma sep.** It carries over verbatim. The separation uses only that J is linear in the score vector, and J(X) = ∫_X g with g = Σ_{ω∉W₀}α_ωφ_ω − Σβ_jc_j. Only the b-integrand changes. γ = 0 off W₀ and β ≠ 0 are unchanged.
2. **Uniqueness (BX3).**
   - g is continuous.
   - g(h + t𝟙) ≤ g(h) − tβ·l, using φ(h + t𝟙) ≤ φ(h) and BX1(c).
   - β·l > 0 because l ≫ 0 and β ≥ 0, β ≠ 0. This is where l ≫ 0 is needed, and degenerate l_j = u_j is harmless.
   - W62 `lem:fubini` then gives a null tie set, and the bathtub argument gives an a.e.-unique minimiser.
   - Boundary priors (zeros in β) are covered, because only β·l > 0 is used.
3. **Coherence (BX4).**
   - −β_jc_j(h) = max_{ρ_j∈[l_j,u_j]}(−β_jρ_jh_j), because β_j ≥ 0.
   - Independent maxima add, so g(h) = max_{w∈W}(−w·h) with W = β⊙R + Σ_{ω∉W₀}α_ωB_ω compact.
   - W ⊆ ℝⁿ₊ and 𝟙·w ≥ β·l > 0, so {g < 0} = D_{ν(W)} with ν(W) ⊆ Δ compact.
   - N(W₀) = D_{K′} ∩ ⋂_{W₀}D_{Â_ω} a.e. (W62 `lem:coh`).
   - Hence X\* = D_{K(W₀,β,α)} a.e.
   - The second level being concave rather than linear changes nothing, because the box chart is still a minimum of linear functionals with non-negative coefficient vectors.
4. **Converse and ties.** W62 `thm:family` (c) converse and (d) carry over verbatim.
5. **Target.** For the triple (Ω, β, ∅), K = conv(K′ ∪ ⋃conv A_i ∪ ν(β⊙R)). W62 `lem:LF`(a) gives (LF).
6. **Remarks.**
   - Every cevian segment in relint Δ is a degenerate box: re-derived, and checked exactly on 2 000 cases.
   - ν(R) in relint Δ₃ is the polygon cut by the six cevian half-planes l_jy_i ≤ u_iy_j.
   - The pair (i,j) is redundant iff l_k = u_k. Both constraints of a pair drop together, so the polygon has 6, 4, 2 or 1 "sides" (hexagon, quadrilateral, segment, point) and is never a triangle.

## C. Corollary BX3

- **⇐ (V).** This is W62 `thm:exempt`, with K′ the hull of the points v + ε(v − e_{j_v}) for the good vertices v.
- **⇐ (X).** As in PC64, with all hypotheses verified exactly on 2 000 triangles.
- **⇒.** Steps 1–5 are correct.
  - Step 2: W₀ = Ω, because ν(β⊙l) ∈ T ⊆ relint Δ forces supp β = Ω.
  - Step 3: x ∈ Â_ω ⊆ conv(K′ ∪ e_ω) with x extreme gives x − e_ω ∝ k − x, so x is strictly visible from ω.
  - Step 4: never a triangle (see B6).
  - Step 5: the supporting-line argument.
- **"Exactly" is justified in both directions within the class VBox(K′, B, R) on M_{D_{K′}}**, with B any veto profile over K′.
- **Referee lemma (structure of class X; PROVED).** Let b = (1−τ)a + τe_l, τ ∈ (0,1), be the bad endpoint nearer e_l. Then a − b ∝ b − e_l, so (b − e_l)·h ≥ 0 on F_b. Hence h_l ≤ 0 on F_b, and b is tangential from l.
  - So **no class-X triangle has two O61-strong non-visible vertices.** CHECKED: 2 000 of 2 000.
  - Hence no veto–box target has two strongly non-visible vertices.

## D. A direct 𝒱_B exclusion for T (replaces the appeal to O61 Cor A(d))

Hypotheses: those of O61 Thm A. These are a 𝒱_B ranking, a one-sided (LF) domain A, D_T undominated, and the X_{kj} coherent.

1. O61 Lemma 2 gives D_T ⊆ N.
2. Thm A steps 1–2 give π ∈ T with D_T = N ∩ {π·h > 0} a.e.
3. **At p.** p is strongly non-visible (ACC). Lemma 4 and step 3 give π ⊥ F_p, so π = p.
4. **At s (world 1 tangential; worlds 2, 3 crossing).**
   - Lemma 4's induction, run for k ∈ {2,3} only, puts balls around relint F_s into Z₂ ∩ Z₃. It needs only P₂ ∪ P₃ = relint F_s, and connectivity.
   - X₁₃ = Z₁ ∩ A ∩ {h₃ > 0} is coherent, = A ∩ D_Q. It contains A ∩ {h₁ > 0, h₃ > 0} (Lemma 1) and D_T ∩ {h₃ > 0}.
   - Witness, with r = (0,−1,1):
     - p′ = r + γe₁ − δ𝟙, with γ = 1/10, δ = 2/25 (s₁γ < δ < γ). It has h₁ = 1/50 > 0 and h₃ > 0.
     - q′ = r′ + ζ𝟙 ∈ D_T, with r′ = r + ½(−1,4,−1) ∈ relint F_s and ζ = 1/1000.
     - h\* = p′/10 + 9q′/10 has s·h\* = −11/10000 < 0 and p·h\* = 4449/10000 > 0 (exact).
   - Since D_Q is open and convex, it contains a ball around h\*. Scaling γ, δ, ζ, λ down keeps every point in the (LF) neighbourhood, because the inequalities are homogeneous.
   - So a ball around h\* lies a.e. in Z₁ ∩ Z₂ ∩ Z₃ = N, inside {p·h > 0} and outside cl D_T. That contradicts step 2. ∎
5. So T is outside 𝒱_B without citing Cor A(d) (PROVED by referee).
6. **Why the box cover escapes.** Its world-1 weight is 1 or 6 according to the sign of h₁, not common with worlds 2 and 3. A single nonatomic integral order fixes its integrand up to a positive constant, so no rescaling puts the ranking in 𝒱_B.

## E. Scoped exclusions and the conjecture: required wording

- **6c.** "No continuous piecewise-linear single chart meets the four-condition certificate (C1)–(C4) for T, with (C2), (C3) at priors near π\* and on [e_k, π\*]." Mark it PROVED modulo writing out C62 Lemmas 4.2–4.4 for T. Add the referee's π\* ≫ 0 step and the determinant π₁π₂π₃/15625.
- **7 (Lemma CM).** Add π\* ≫ 0. Write "modulo transfer" for the C62 lemmas. Name DC63's (C2)-at-u for direction-continuous charts.
- **8.** State the conjecture as a statement about coverage under the binding framework that implies the reversed-triangle impossibility. Put the proved "reach of known architectures" statement next to it.

## F. Consistency (item f)

- **O61 Thm A** (𝒱_B; ≥ 2 strongly non-visible vertices excluded): not contradicted.
  - T has one strongly non-visible vertex (p), and the cover is not 𝒱_B (§D6).
- **O61 Cor A(d)** (𝒱_B; one-world-tangential corners count as non-visible): not contradicted.
  - §D re-proves it for T. The step "π = s" needs a *linear* Γ, which the box chart does not have.
- **O61 Thm B** (convex error): not contradicted.
  - For R and the PM triangles all three faces are forced and the ray matrix is nonsingular. For T only F_p and F_s are forced, and that system is solvable. The general form needs ≥ 2 CCC vertices, and T has none.
- **O61 §7 sentence** "Theorems A and B then show that a cover of a polytope with two or more non-visible vertices must use … R1 (an error level neither Brier-type nor convex) …": the convex half was **never proved**.
  - Thm B's general form needs all-crossing vertices. The mixed case is O61's own CONJECTURE.
  - In the strong sense T does not contradict it (one strongly non-visible vertex), and by §C no veto–box target does.
  - Under the weak reading ("not strictly visible", or counting one-world tangency as in Cor A(d)), T is a counterexample.
  - ROUND61 §3 ("Convex error levels do not help") was already corrected to "cannot cover the reversed triangle" by FD62 #6, refereed in REF62_fd.
  - **Error located:** O61 §7 generalises Thm B beyond what its proof gives, namely beyond the all-three-faces-forced ray system or two CCC vertices.
- **Status lines now superseded (not theorems):**
  - ROUND62 §3: "not covered by any construction yet: triangles with one or two edges through simplex vertices".
  - ROUND63 §5: "every target with at least two corners that are not uniformly visible and not orthant-planar".
  - The class-X triangles, with one or two cevian edges, are now covered.
- **Unaffected:** ROUND63 "a triangle with two cevian edges is never a composed target". It concerns composition only.
- **Paper (W64), for the writer.**
  - Open problem (7)'s test triangle conv{(1,6,1)/8, (6,1,3)/10, (6,1,1)/8} is class **N∖N33**, not X. It stays open, and Lemma CM does not apply to it.
  - The characterisation question itself is answered negatively by T, so (7) must be rewritten.
  - The scoped convex-error item (1) is already correctly restricted to R and the PM triangles.
  - Theorem BX belongs with the positive theorems once it has been refereed a second time.
