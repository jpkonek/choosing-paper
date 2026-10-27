# X12 referee report: X1_notes.md and X2_notes.md (round 26)

16 October 2026. Adversarial refereeing of X1 and X2, read against AUDIT_X123.md, AUDIT_nonlinear_programme.md, BRIEF18.md and write-up §2. I also verify the audit's interior-locality lemma.

**Scripts.**
- Every script cited by X1 and X2 was rerun with `python3 -I`, on copies in `x12ref_py/x1/` and `x12ref_py/x2/`. Outputs are the `*.rerun` files.
- My own checks are `x12ref_py/x29_eps_scan.py` and `x12ref_py/audit_locality_check.py`, with matching `.out` files.

**Verdict scale.** CORRECT / GAP (fixable; the fix is given) / WRONG.

---

## 0. Summary

| Item | Verdict |
|---|---|
| X1.1.1 / X1.1.2 transition lemma, full domain and advice-range domains | **CORRECT** |
| X1.3.1 finitarity | GAP (cosmetic). Csel has 6 literals, not ≤ 4; finitarity is unaffected |
| X1.3.2 finitary consistency for fixed (C, V) | **CORRECT** (propositional compactness) |
| X1.3.3 plan extension theorem (a)–(e) | **CORRECT as stated**. As a compactness criterion it is exact but close to tautological. It is not an existence result, and the brief's extension lemma is not supplied (§1.2) |
| X1.3.4 automatic plans | CORRECT, once the hypothesis is read as literals in L |
| X1.3.5 ultralimit corollary | CORRECT. "Precise condition" overstates a sufficient condition |
| X1.3.6 finitary form of T1 | CORRECT (WLOG T1 = C_{p*} by tie-replacement) |
| X1.5.1 dead crossing triple, parts (1)–(5) | **CORRECT** (independently re-proved) |
| X1.5.2 90 minimal models, all exactly common-density witnessed | **CORRECT** (CHECKED; reproduced bit-for-bit; enumeration algorithm complete) |
| X1.5.3 non-witnessed model | CHECKED (reproduced) |
| X1.5.4 S4: clean in Γ, (K) unmeetable by real derivations | **CORRECT** (each derivation re-done by hand). The dichotomy (α)/(β) is a tautology |
| X1.5.5 Φ′ certificates; S4 has none | **CORRECT** (re-derived) |
| X1 NUMERICS (greedy) | Reproduced (0 stuck). `greedy_stuck.out` is stale: it predates the script, and its mean-length line differs |
| X2.1 record form of the full domain | CORRECT |
| X2.2 (a)–(d) constraints forced on every selection | **CORRECT**. In (d), edge priors need one extra sentence |
| X2.3 / X2.4 double-improvement lemma; at most one W-first and at most one N-first world | **CORRECT**. It does sharpen L3.6(b) |
| X2.5 posterior selection: properties | CORRECT |
| X2.5 uniqueness under rescaling | **GAP**. Uniqueness holds on int Δ only; on the open edges other equivariant selections exist. Harmless for X2.9 |
| X2.6 attribution form | CORRECT (re-derived; 20 000/20 000 reproduced) |
| X2.7a reduction to u | CORRECT |
| X2.7 local extension theorem | **GAP** at ×: as written, guidance fails for moves to ×; fixed by a weight > 4 on σ_×. Otherwise CORRECT within its scope (local records only; no (S); no nonlocal (K)) |
| X2.8 whole-piece interior fragments satisfiable | CORRECT. NUMERICS reproduced (seed 1: 10/10 SAT) |
| X2.9 no G′-invariant local A_k with closed choice at e_k | **CORRECT, with GAP in the geometry.** The box size and E₁ must depend on ε; with ε-dependent choices it is verified exactly for ε ∈ [10⁻⁴, 0.999] |
| X2 "the difficulty is the ends corresponding to ∂Δ" | **WRONG** as an interpretation (audit lemma, §3) |
| Audit interior-locality lemma and its corollary | **CORRECT** (re-proved; exact check) |
| New referee observation R1: X2.7's rules fail closed choice at every vertex, for every selection with imprecise near-vertex models, by a level-0 mass count | PROVED here (§2.8) |

---

## 1. X1

### 1.1 Transition lemma (Thm X1.1.1, Lemma X1.1.2): CORRECT

**(i) Record invariance.** Suppose (X, Y) and (X′, Y′) have the same record r. Let A := supp r ∪ −supp r. Then X ∩ A = X′ ∩ A, Y ∩ A = Y′ ∩ A, X ∖ A = Y ∖ A =: F and X′ ∖ A = Y′ ∖ A =: G. This is literally an (IB) instance with F, G ⊆ Aᶜ, and all four models are the given evaluable ones. Correct.

**(ii) Joint realisation.** The values used at f all occur in a realizable record at f, so they lie in A(f). The filler on {r = s = ι} is the "first available value" selection, which is measurable. By Remark advicerange the three models are evaluable.

The audit's proviso, that every composition must be realizable, is therefore automatic, as X1 says.

**(iii) and the converse.** Both are fine. The transitivity-to-composition direction uses (i) to pass from "some pair with record r" to "every such pair". Injectivity of rk_i(f, ·) off {f_i = 0} makes condition 4 exactly strict (G).

X1's wording correction to the audit is right: condition 3 comes from weak (G), not from reflexivity.

**U-domain remark.** On the U-domain the advice range is {+, 0}. Records are ternary, and composability is "σ + τ ternary". This recovers P3's (P), (N), (Σ). Correct.

### 1.2 Theorem X1.3.3 (plan extension theorem): CORRECT as a theorem; it is a compactness criterion, not an existence result

**Checks.**

- *The plan clause.* ¬x_{i,r_q^X} ∨ x_{i,r_p^X} for q ∈ V(p, i, X) reads "accepted at some q ∈ V ⇒ accepted at p". It forces V(p, i, X) ∩ A_i(X) = ∅ whenever p ∉ A_i(X). So every section has open complement. Correct.
- *(a) and (c)* are immediate once INV holds. (a) follows because INV already gives a full model by compactness; (c) because a finite subset of a chain union lies in one member.
- *(d)* is correct.
  - Maximal L equals a model.
  - Thm X1.1.1 gives the preorders.
  - (R4) gives undominated selected models.
  - Closed sections come from the plan.
  - (C): KKM ties any B ∈ C_L to some C_p. A model tied with B is tied with C_p, so (Csel) makes it coherent. It is undominated by transitivity.
- *(e)* is correct. Put V(p, i, X) := Δ ∖ A_i(X) when the comparison is rejected, and Δ otherwise.
- *X1.3.6.* T1 ∈ C_L ties some C_p. Replacing C_p by T1 at p changes neither competitiveness nor any section, by transitivity. So T1 = C_{p*} is WLOG. Correct.

**What it gives and what it does not.** I agree with the audit, and add the following precision.

- INV(L; V) is equivalent, by Prop X1.3.2, to: *there is a successful system for C that contains L and respects V*.
- Hence (a)–(c) are not consequences of an invariant one could check independently; they restate existence. (e) shows the criterion is exact, but the plan in (e) is read off the solution. So "∃V: Θ_C ∪ Plan(V) finitely satisfiable" is equivalent to "a successful system for C exists".
- The theorem therefore supplies:
  - a correct finitary normal form;
  - finite refutation certificates for a **fixed** (C, V).

  It does **not** supply existence, and it gives no procedure for finding V.
- This is P3 Thm 4.1 (compactness of everything but (Cl)), with (Cl) replaced by a fixed plan. P3 §8.4 already says that a "global commitment that controls R5" is what is missing. X1.3.3 names that commitment V; it does not produce it.
- The "Outcome" sentences "It is the extension lemma requested in the brief" and "explicit" should be withdrawn. Replace them with: "a plan-relative compactness criterion; constructing a plan through T1 is the open problem".

**Removal of R5.** This is legitimate only in the sense just described. Plan(V) implies R5, since the sections become closed. Conversely, R5 together with closed sections does not determine V before the solution exists. The quantifier order "∃V ∀ fragments" cannot be weakened to "∀ fragments ∃V". The audit's point stands: V may depend on (p, i, X), but it must be the same across all fragment witnesses.

**Minor.**
- X1.3.1's "≤ 4 literals" is false for (Csel), which has 6 literals with three worlds (`fullfrag.py`, `horn()`). Finitarity is unaffected.
- X1.3.4: the hypothesis "C_p ⪯_i C_q for q ∈ W" must be literals in L (or in the theory) for the plan clause to be a *consequence*. Otherwise it is only an instance of (Σ) with one literal still open.

### 1.3 Ultralimit corollary X1.3.5: CORRECT

Each S_α satisfies Θ_C ∪ Plan(V). For accepting triples this is trivial; for rejecting triples it follows from uniform rejection. A finite clause true for every α has a literal true on a 𝒰-large set, so the ultralimit satisfies it.

The partial-assignment version is also correct. If ¬x is true on a 𝒰-large set, then {α : x^α true} ∉ 𝒰, because the two sets are disjoint.

The hyperreal remark (Łoś) and its no-(M1)-certificate consequence are correct.

**Overstatement.** "Uniform rejection is the precise condition under which such gluing keeps closed sections" claims necessity; only sufficiency is proved.

Note also that each S_α is already a model of the same theory. The corollary produces *new* systems from a shared plan; it does not help find a plan.

### 1.4 Dead crossing triple, Thm X1.5.1: CORRECT

I re-proved every part.

- **(1)** With exact piece weights, ρ_j is accepted at world j iff a·m_{j+1} ≥ m_j. All three together force a³ ≥ 1. The stated masses (a², a, 1) accept two of them, with equality.
- **(2)** I checked closure of G_j = B_j ∪ R_j under composition.
  - B∘R and R∘B stay in R: the start rank is ≤ 1 and the end rank ≥ 2 on π_{j+1}.
  - R∘R is never composable: it ends in {+, ×} and would have to start in {−, 0} on the non-null set π_{j+1}.
  - G_j contains no nontrivial improvement and no pair r ≠ ι with r⁻¹ also in G_j.
  - Sections are closed: they are finite sums of μ(E ∩ {C_q = a}) = 0 conditions, and these are continuous in q when C is continuous in measure.

  So E_{1,2,5}(L) ⊆ G is clean.
- **(3)–(5)** τ⁻¹ = ρ_j ∘ (0→+ on π_{j+2}), and the second factor is j-worsening. τ ∉ G_j. And τ ∘ ρ_j = (+→0 on π_{j+2}), a strict j-improvement.

The conclusion holds for every coherent selection with C_u at + a.e. on Π. Continuity in measure is needed only for (2). `fullfrag.rerun` reproduces it: inconsistent with H; consistent without R4, but τ is then unmeetable.

### 1.5 Crossing fragment Γ: X1.5.2–X1.5.5

**Reproduction.** `fullfrag`, `exact_witness`, `cegar_full`, `s4_certificate`, `trace`, `maximal_states`, `stuck_minimise`, `pareto_witness` (both conventions), `horn_states`, `crossing_fragment` and `crossing_minimal` all reproduce their `.out` files byte for byte. `greedy_stuck` reproduces "stuck 0" for both conventions, but its stored `.out` predates the current script (mtimes 17:18 and 17:19), and the "mean number of choices" line differs (10.5 rerun, against 92.9 and 129.9 stored). Regenerate the `.out` file.

**X1.5.2 (90 minimal models): CORRECT.**
- The enumeration is complete. Each model is shrunk to a minimal one, and every superset of it is then blocked. At termination every model contains a found minimal model.
- The exact LP rationalisation verifies a positive margin at a = 1/20, 1/5, 3/10, 9/20.
- The inference "M ⊆ Ψ^{ρ_m}, hence INV(M; V_m)" is right. ∫_{π_k} (m_k/φ)|h_j| dμ = m_k·vol·|h^{(k)}_j|, with a common density for all worlds, so Ψ^{ρ_m} is a successful system covering the precise targets.

The audit's caution is apt: this concerns the precise selection. It says nothing T1-specific.

**X1.5.4 (S4): CORRECT.** I redid each real derivation by hand.

- *World 1:* r is a strict 1-improvement.
- *World 0:* r∘g = [., +>0, .], which is a strict 0-improvement.
- *World 2:* c₃ ∘ (r∘c₂) = [., 0>+, 0>+]. Composing with c₄ gives [0>+, ., 0>+] = r⁻¹.
- r⁻¹ = [., 0>+, .] ∘ g is accepted at world 0 (the first factor is background there), and r⁻¹ is background at world 1.
- So (R4) puts r at world 1, which (N) forbids.

All compositions are composable and realizable. The "exact dichotomy (α)/(β)" is a tautology, since (β) is the negation of (α). It should not be labelled a theorem.

**X1.5.5 (Φ′): CORRECT.**
- R4 reduces to a.e.-unique minimisation of q₀Φ₀ + q₂Φ₂ among models that are at least as good as D_q at world 1. On π₀ where D_q = +, this needs q₀κ₀(0)h₀ > q₂κ₂(0)|h₂|. That follows from q·h > 0 and κ₀(0) ≥ κ₂(0). The other cases are as stated.
- "No certificate for S4" re-derived. c₂ + c₃ with κ₂(1) ≤ κ₂(0) give κ₂(2) ≤ aκ₂(0). On the other side, κ₂(2) ≥ κ₀(2) > κ₀(0)/a ≥ κ₂(0)/a > aκ₂(0). Contradiction. Confirmed by the LP rerun.

---

## 2. X2

### 2.1 X2.2: constraints forced on every selection — CORRECT

**(a)** If C_p is not at M on a non-null part of Q_l, correcting it is strictly better at both i and j. Coherence of C_p and letting h_l → −∞ then give m_l = 0 on K_p.

**(b)** B^k is the strict world-k optimum.

**(c)** I checked every step.
- e_k ∉ {p : C_p ⪯_j X_P}, because X_P ≺_j B^k = C_{e_k}.
- The k-worsening X_P → X_P^F identifies X_P^F = C_p[F → correct, P → S].
- The incoherence argument is sound. If D_K contained a.e. of {h_k > 0} ∖ (−P), then by convexity of the open cone {P_K > 0} it would contain the whole open half-space. That contradicts the non-null hole.

**(d)** Correct for interior p. For p on an edge (e_k, e_j) near e_k, use competitiveness on {k, j}: world l is excluded by the same section, so (c) still applies. Add this sentence.

### 2.2 Double-improvement lemma X2.3 and Cor X2.4: CORRECT; it tightens L3.6(b)

On Q_i ∪ Q_j, O→S and S→M improve world k strictly, so competitiveness leaves i or j.

T1 can replace its tied selected model. Its prior is interior: an edge prior would force T1 to be at M on Q_l, by X2.2(a)'s argument applied to T1 through the tie. That argument works on any (LF) domain, using corrections near ∂D_{T1}. A vertex prior would force T1 = B^k.

**(a)** On A ⊆ O_j(T1), the change O→S removes i-wrong advice. On B ⊆ O_i(T1), O is i-correct and S is not wrong. So W_i drops by W_i(A) > 0, and symmetrically for j. Two W-refining worlds would therefore make X dominate T1.

L3.6(b) concluded "at most two" from T1 ⋠_m R. X2.4(a) gives "at most one". This is a genuine sharpening, under the hypotheses (S), (LF) at T1, T1 ∈ C_L, and W_i a bounded charge positive on non-null sets.

**(b)** The same argument, with the non-correct charge N_i. Correct.

(LF) supplies S and M near ∂D_{T1}, as claimed: for the O-cases, use orientation −h ∈ N.

### 2.3 Posterior selection (X2.5) and uniqueness: properties CORRECT; uniqueness GAP

**Checks.**
- h ∈ C_p ⟺ p⊙h ∈ D_{T1}, because p·m > 0.
- d*C_p = C_{ν(d⊙p)}.
- K_{e_k} = {e_k}, the edge statements and Hausdorff continuity: all correct.

**Gap.** Equivariance with C_u = D_{T1} determines C_p only for p ∈ int Δ, since d⊙u reaches only the interior. On an open edge, the stabiliser (s, s, t) fixes every D_K with K ⊆ that edge, and it acts transitively along the edge. So the edge values may be *any* equivariant orbit of edge credal sets. For example, the precise edge selection C_p = D_p, p ∈ (e_i, e_j), satisfies d*D_p = D_{ν(d⊙p)}. At the vertices, equivariance alone forces nothing; X2.2(b) forces B^k.

**Fix.** State: "unique on int Δ; unique on Δ among Hausdorff-continuous equivariant selections." The axioms do not require Hausdorff continuity; (S) concerns sections only.

The gap is harmless for X2.9. That proof uses only interior near-vertex priors and C_{e_k} = B^k, which X2.2(b) forces anyway. So "no equivariant system" stands.

**Minor.** The phrase "every constraint that the full domain forces on any selection" should read "the constraints of Prop X2.2". The audit lemma (§3) exhibits a further compatibility constraint, which X2.2 does not list.

### 2.4 X2.6 attribution: CORRECT

The minimum over vertices of (p⊙v_m)·h ∝ p·h + λ p_m h_m is attained at m = o, and the maximum at argmax_{j≠o} p_j h_j.

The field: Σ p_i F_i(M) = −(p·h + λ p_o h_o) and Σ p_i F_i(O) = p·h + λ p_a h_a, with M and O never both better than S. The per-world orders are M < S < O for majority worlds and O < S < M for the odd world, so the field is strictly guiding for every attribution.

`attribution_check.rerun`: 20 000 pairs, 0 mismatches.

### 2.5 Theorem X2.7 (local extension theorem): GAP at ×; otherwise CORRECT within its stated scope

**The × gap.** Composition-additivity forces the record vector to be a coboundary: σ(a→b) = pos(b) − pos(a) for one world-independent embedding pos of {M, S, O, ×}. Write pos(×) = (α, β, 1) in the coordinates (step A, step B, σ_×). With the stated coefficient 1 on ∫σ_×, the level-0 value of × relative to M on Q_c is:
- α + β + 1 for a majority world (weight w = 1, sign +). Guidance needs this to exceed O's value 2, so α + β > 1.
- −2(α + β) + 1 for the odd world (w = 2, sign −). Guidance needs this to exceed M's value 0, so α + β < ½.

These requirements are incompatible. So for some move to ×, X2.7(a)'s claims "contains every weak i-worsening and no non-null i-improvement" fail.

**Fix.** Give σ_× a weight γ > 4 at every world, with pos(×) = (1, 1, 1); γ > 2 suffices with pos(×) = (0, 0, 1). The balance becomes Σ_i m_i = 3∫σ_U + 3γ∫σ_× ≥ 0 out of coherent C, and (b) and (c) are unchanged. X2.8 and the X1/X3 fragments never use ×, so they are unaffected.

**Other parts: correct.**
- *(a)* Lex-≥0 of a sequence of linear functionals is a positive cone of a group order, so it is closed under addition. Weak worsenings have m_i > 0 and improvements m_i < 0.
- *(b)* Translation changes the (α, m) moment by moments (β, m) with β < α, all earlier in the |α| + m enumeration. By induction, the first non-zero level and its value are invariant.
- *(c)* Out of a coherent C, σ_U, σ_× ≥ 0. If all m_i = 0, then σ_U = σ_× = 0.
  - {ω^α e^{−mc}} is a point-separating unital algebra on K × [0, ∞]. So, by Stone–Weierstrass, it determines σ_{cs}·ν, a finite signed measure.
  - Since the signs (+, +, −) are not all equal, some world accepts strictly.

**Scope.**
- The theorem's conclusions do not include (S). They include no (K) for non-local competitors and no boundary priors.
- With the audit lemma, the scope is narrower than the "Reading" suggests. For each fixed X, rec(C_p, X) is local for at most one interior p. So X2.7 says nothing about any section {p : C_p ⪯_i X}.

### 2.6 Corollary X2.8: CORRECT

Whole-piece records on cones bounded away from the planes are local. Their acceptance under X2.7 depends only on the record, so the variables are selection-independent as in X1. (K), (U), (T) and (G±) then follow from X2.7(a) and (c).

`run_frag.py 4 10 1` reproduces the stored output exactly: 10/10 SAT.

**Scope caveat.** X2.8 covers only interior priors and local records. It does not cover X1's Γ with S = Plus(s), nor fragments containing comparisons C_p vs C_q at distinct priors, which are nonlocal by §3.

### 2.7 Theorem X2.9: CORRECT, with a GAP in the stated geometry

**The logic, re-checked.**
- *Step 1.* ρ_p(F) ∈ A_k for local F ⊆ E_k(C_p), by X2.2(c). C_p is at O on all of P near e_k, by compactness of P̄ in the open region.
- *Step 2.* For p ∝ (t, 1, 1), C_p = (1/t, 1, 1)⊙D_{T1}. Transport is by a G′ element, and normalisation is harmless because all models involved are cones. It yields ρ(F, t) for every local F ⊆ E_k(T1).
- *Step 3.* Π₂ = g⊙P_{t₂} is centred at (−1, 1/(t₁t₂), 1), and g⁻¹⊙Π₁ at (−1, 1, 1/(t₁t₂)). Both lie in S_k(T1). The model g⊙D_{T1} is at S on Π₁ and at O on Π₂.
- *Step 4.* ρ₁ = (Π₁: O→S, Π₂: S→O, E₁: M→O) and ρ₂ = (Π₁: S→O, Π₂: O→S) are composable, with matching middles. The composite is E₁: M→O, a non-null strict k-improvement, contradicting strict (G).

Hypotheses used: strict (G), (IB), competitiveness on Ω near e_k, two closed sections at e_k, C_{e_k} = B^k, and the posterior on the interior. Not used: (C), (LA), T1 ∈ C_L. As stated.

**Geometry gap.** The note fixes "a box within 3%" (the script uses 1%) and E₁ around (−1, 3, 3).
- The strip is (β, A) = (c₀/(c₀+ε), 1 + ε/c₀), which shrinks to {1} as ε → 0. So no fixed box works for all ε.
- (−1, 3, 3) ∈ M_k(T1) iff 5c₀ > ε, i.e. ε < 5/8.

`x12ref_py/x29_eps_scan.out` shows the failures exactly:
- the 1% box fails for ε ≤ 1/1000, and the 3% box for ε ≤ 1/100;
- E₁ at (−1, 3, 3) fails for ε ≥ 5/8.

**Fix (verified).** Take:
- half-width η = (A − 1)/(8A), which gives (1+η)/(1−η) < A and (1−η)/(1+η) > β;
- E₁ around (−1, R, R) with R = 2 + ε/c₀;
- t₀ > 4 + 4ε/c₀ + 1/η.

With these, all piece positions (O, O, S, S, M) are certified exactly on the boxes, for ε ∈ {10⁻⁴, 10⁻³, 10⁻², 0.1, 0.3, 0.5, 5/8, 0.7, 0.9, 0.99, 0.999} and four (t₁, t₂) combinations each. The analytic argument works for every ε ∈ (0, 1).

**Reading.** Agreed with the audit: this obstructs G′-invariant local accepted sets with the posterior (equivalently, any equivariant) selection. It is not a theorem against the posterior selection with non-invariant orders.

### 2.8 Referee observation R1 (PROVED here): X2.7's rules fail at a vertex for essentially every selection

X2.9's "in particular" (X2.7's rules are not the local part of any such ranking) follows much more simply, and it does not need the posterior selection or invariance.

**Claim.** Let a ranking on the full domain have strict (G), competitiveness on Ω at interior priors near e_k, closed sections at e_k for the models X_P, and any coherent selection with C_{e_k} = B^k. Suppose some interior p ∈ N_P has K_p ≠ {e_k}. Then world k's local part is not X2.7's A_k. This holds even with the × fix and with any higher levels.

**Proof.**
- Take m ∈ K_p with, say, m_l > 0. On Q_k, h = (−1, eˣ, eʸ) with eʸ > m_k/m_l is not at O for C_p. Such h is k-wrong. Its ω-image contains a half-plane, so ν(E_k(C_p) ∩ Q_k) = ∞.
- Choose a local F ⊆ E_k(C_p) ∩ Q_k, disjoint from P, with ν(F) > ν(P).
- In ρ_p(F), the part on P is O→S or less, and on Q_k (world k odd, weight 2) this contributes at most +2ν(P). Each unit of F contributes at most −2.
- So m_k(ρ_p(F)) ≤ 2ν(P) − 2ν(F) < 0, and X2.7 rejects ρ_p(F) at level 0. But X2.2(c) forces ρ_p(F) ∈ A_k. ∎

**Nearby positive pointer** (in the project's "nearby result" spirit). Near e_k, X2.2(c) forces world k to rate the silence cost on a fixed far piece P above *every* local correction of C_p's errors. Any level-0 additive local rule with weight ν_k therefore needs sup_F ν_k(F) ≲ ν_k(P) over local F ⊆ E_k(C_p). In other words, ν_k(E_k(C_p)) must be bounded relative to ν_k(P) as p → e_k. A Haar-type (infinite, invariant) weight cannot meet this, while finite, plane-decaying weights can. This is the precise non-invariance that a local rule must have. It is consistent with X2.9 Remark (iii) and with V1's bounded-endorser shadow.

### 2.9 Interpretive claim: WRONG

X2 §0 and §6 locate the cover problem at "the 'ends' that correspond to ∂Δ". By the audit lemma (§3), selected models at *any two distinct interior* priors already differ on cones reaching the coordinate planes. Gamble-space approach to the planes is therefore not the same thing as parameter-space approach to ∂Δ.

Replace the claim with the audit's sentence: bounded-support fragments admit the rules; nonlocal comparisons and closed sections remain open, already for varying interior priors; vertex closedness separately excludes full rescaling invariance.

---

## 3. The audit's interior-locality lemma: CORRECT

**Proof check.**
- For h = (h_i = −1, h_j = t, h_k = s), the vertex minimum of v_m·(p⊙h) is c₀ p·h − ε p_i. So h ∈ C_p ⟺ p_j t + p_k s > A p_i with A = (c₀+ε)/c₀. As s ↓ 0 the t-threshold tends to A p_i/p_j.
- If p_i/p_j ≠ q_i/q_j, then for t strictly between the two limits and all small s > 0, exactly one of C_p, C_q is at M. So the records differ.
- The disagreement set is a cone over a region whose log|h_k/h_i| is unbounded below. Every tail of it has positive measure, so deleting a null set cannot make it local.

**Corollary check.** supp rec(C_p, C_q) ⊆ supp rec(C_p, X) ∪ supp rec(X, C_q), and a finite union of local sets is local. Correct.

**Exact check** (`x12ref_py/audit_locality_check.out`):
- the acceptance formula: 5 000 random rational instances, 0 mismatches;
- 300 random distinct pairs (p, q) with random ε, a grid of 9 t-values in the middle half of the interval and s = 10⁻¹, …, 10⁻¹²: disagreement at every point.

**Consequence I endorse.** X2.7 gives no information on closed sections, even on a compact interior J. In an equivariant system, {p : C_p ⪯_i X} involves nonlocal records at all but at most one interior p.

---

## 4. Requested corrections

1. **X1 §0.3 and §3.** Call X1.3.3 a "plan-relative compactness criterion". Say explicitly that INV(L; V) is equivalent to existence of a solution through L respecting V, and that no plan through T1 is constructed. Credit P3 Thm 4.1 and §8.4.
2. **X1.3.1.** The Csel clause has 6 literals.
3. **X1.3.4.** State the hypothesis as literals.
4. **X1.3.5.** Replace "precise condition" by "sufficient condition".
5. **X1.5.4.** Label the (α)/(β) dichotomy as trivially exhaustive, not as a theorem.
6. **`greedy_stuck.out`.** Regenerate it; it is stale.
7. **X2.5.** Make uniqueness interior-only, or add continuity.
8. **X2.2(d).** Add the edge-prior sentence.
9. **X2.7.** Give σ_× a weight γ > 4, or γ > 2 with pos(×) = (0, 0, 1). State the coboundary encoding of × explicitly.
10. **X2.9.** Use the ε-dependent η, R and t₀ of §2.7, and extend `cycle_check.py` over ε, as in `x29_eps_scan.py`.
11. **X2 §0 and §6.** Replace the ∂Δ-ends reading with the audit's formulation, and add R1 (§2.8) as the simple reason X2.7's rules cannot be extended.
