# Referee report on N1_notes.md (round 20/22 part, top of file) and N2_notes.md Part I

16 Oct 2026. This is an adversarial reading against the following:
- M1_notes + M1_referee, L4_notes + L4_referee, L2_notes + L23_referee, L3_notes (L3.4), K3_notes + K3_referee
  (K3.1, K3.7′), S1/S2 notes, P4B_referee (Lemma N0), M2_notes + M23_referee;
- the write-up §§2–3 (axioms, competitiveness, relevant comparisons, regular models).

Every item labelled PROVED was re-derived line by line. Archived Parts (N1 "ARCHIVE", N2 Part II) were not refereed.

**Numerics** (all reruns with `python3 -I -B`):
- `n1py/n1b_edge_check.py`: byte-identical to `n1b_edge_check.out` (rerun in `n12ref_py/n1b_edge_rerun.out`).
- `n2py/r20/n2_checks.py`: byte-identical to `n2_checks.out` (rerun in `n12ref_py/n2_checks_rerun.out`). The body
  of `n2_geo.py` is identical to `m1py/m1_common.py`.
- My scripts are in `n12ref_py/`:
  - `n1c_probe*.py`: a search for counterexamples to N1.C. It finds them; see §1.8.
  - `l2_consistency.py`: an exact cell check that N2.1(c) and N2.3 hold in L2.

None of my verdicts rests on numerics except the refutation of N1.C, and that one is also proved by hand in §1.8.

---

## 0. Verdicts

### N1 (round-20 note, lines 1–426)

| Item | Verdict |
|---|---|
| N1.0(a) π-null pieces; (b) edge-selected = P_i on Q_k; (c) swap vectors | **CORRECT** |
| **N1.1** swap lemma | **CORRECT.** Remark (i) overstates what is used: N1.0(b) is not needed, so strict (G) is not used at all (§1.1). Interior version (ii) and remark (iii): CORRECT |
| M1.3 re-proof (face KKM on an edge) | CORRECT (M1.3 is now also refereed CORRECT in M1_referee) |
| **N1.2** edge dichotomy | **CORRECT**, including the vertex cases. It is the contrapositive of N2.3′(a) with extra information in (D) (§3) |
| **N1.3(a)** no shadow; Q_M1 = No | **CORRECT**, for Q_M1 read as Λ_k = E_k(T1) ∩ M. The weaker "admissible at all three vertices" reading is **not** settled; see §2.6 for the nearby result |
| N1.3(b) the M1.7 exchange; (W2) impossible | CORRECT |
| N1.3(c) pairwise-null blind sets are rigid, with selected edge models | CORRECT ((NC) at every world is implicit) |
| **N1.4** no jumps; strict escape | **GAP (fixable).** "By (Nest), c_t is nondecreasing in t" does not follow: (Nest) only says that C_L is a chain. Fix: index by the chain via Lemma N0 (§1.4). With that fix, CORRECT, including τ = 1 and τ = 0 |
| **N1.5** CA-blind sets are initial segments, whatever the partner | **CORRECT** after the N1.4 fix. Steps 1–3 re-derived, including the sup argument |
| N1.6(a)–(d) | CORRECT. (c) rests on L2.1/L2.4, refereed CORRECT |
| §4 two-world reduction (non-nested C_L, failure of (MC_sel), partner null) | CORRECT as a list of necessary conditions (it relies on S1 §4) |
| **N1.7** gluing fails at competitiveness of the edge witness | **CORRECT.** It is N1.3(b) with an explicit swap |
| **N1.C** "every coherent between model other than P_i, P_j crosses T1 on R_ij" | **WRONG as stated.** There is an explicit counterexample with K ∩ [e_i, e_j] = {e_i} (§1.8). Restricted to K meeting the open edge it remains a plausible CONJECTURE. The "consequence" sentence must be restricted in the same way |
| §6 independence from L3.4 | CORRECT as a reading |
| **Q_N1** | Well posed. "No" ⇒ no cover with (NC) at every world: CORRECT. Wording GAP: "(M1) world" should read "a world failing (NC)". Two strengthenings are recommended (§1.9) |

### N2 Part I

| Item | Verdict |
|---|---|
| **N2.1(a)** carrier argument; (b) Lyapunov separation; (c) edge form; elementary proof | **CORRECT.** w may be a vertex of Δ_S; what this gives is in §2.1 |
| N2.1′ (M2 setting) | CORRECT |
| **N2.2** no blind target with a visible source; N2.2′ crossings live on ties, (Nest_e) criterion | **CORRECT** |
| **N2.3** every extreme edge θ-Bayes model is selected (null joint blindness) | **CORRECT.** All four inclusions and both vertex cases check. Its input M1.3 is now refereed CORRECT |
| N2.3′(a)–(d) | CORRECT |
| **N2.4** (vis)/(int_i)/(int_j) | Trichotomy CORRECT. **GAP (wording):** in (int_i) only the *source* is forced i-blind. The target F_i is unconstrained, so "both i-blind" and "carried by π_i alone" are not proved (§2.4) |
| N2.5 trichotomy, (c) | CORRECT |
| N2.5(a) | The statement is CORRECT. **GAP (wording):** "M1.9 for arbitrary endorsers" overstates. M1.9 allows ties on one side, whereas N2.5(a) needs the whole tie set Z_{θ₀} null (§2.5) |
| **N2.5(b)** two-sided tie shell for f.a. endorsers | **GAP (inherited from M1.9′(b), fixable).** One facet per side, and the local form of M1.6(a) is needed (§2.5) |
| N2.5′ T1 is (i,j)-Bayes on J_i ∪ J_j | CORRECT |
| **N2.6** Q_M1 = No | **CORRECT.** But "(a) Equivalently (M1.1(b)), no cover has T1 admissible at all three vertices" is **WRONG**: it is not proved, and it repeats the error M1_referee §6.5 flagged. The nearby result that is PROVED is in §2.6. (b), (c) CORRECT. (d) is mislabelled: it is not M1.11 |
| N2.7(a), (b) | CORRECT |
| N2.7(c) | **GAP (inherited).** The hypothesis must be one-sided (§2.5) |
| **N2.7(d)** vertex case with a refined veto, via L3.4 | **CORRECT.** L3.4's (V) and (Imp) were verified (§2.7) |
| §6 (V1)–(V5) | CORRECT |
| §6 (V6) | CORRECT (the last sentence is at the standard of H1.2 and K3.7) |
| §6 (V+) handover | Correct as a description. "L2's world 1 does not refine its veto (PROVED)" is true, but the proof is L3.4 + N2.2 and not anything in L2; cite it so. "(ii) … so the partners would need pfa parts" is conditional on Conjecture L2.C. **GAP (wording)** |
| §6 (V0) / **Q_N2** | Q_N2 is well posed. "(V0) reduces to a two-world question" is an overstatement: Q_N2 is a first test, not a reduction |
| §6 "T1 is not edge-Bayes on R_ij for p* ∈ Δ°" | unproved; it is a reading, so label it |
| §5 status lines "M1 unrefereed" | out of date. M1.2, M1.3, M1.6, M1.7 are now refereed CORRECT, and M1.9′(b) has a GAP |
| numerics | Reruns identical. Docstring of (B): "Thm N2.4" should be N2.3/N2.6 |

**Net.**
- Both notes are mathematically sound in their main lines.
- The swap/carrier mechanism, which is partial trades off the purely finitely additive carriers, is right, and so is
  everything built on it: N1.1, N1.2, N1.5, N1.7, N2.1–N2.3 and N2.6. It is a genuinely new tool, and it needs no
  closed sections (N1.1, N2.1, N2.2).
- **Q_M1 has answer No** (Λ_k = E_k(T1) ∩ M reading), proved twice and independently.
- One statement is false: Conjecture N1.C as worded.
- Two notes repeat M1's earlier overstatements: the three-vertex "equivalently", and the two-sided shell.
- The two notes are **consistent with each other and with L2** (§3).

---

## 1. N1

### 1.1 N1.0, N1.1 — CORRECT
- **N1.0(a).** μ(Q) ≥ μ(B) − Σ_{k≥1}2^{−k−1}μ(B) = μ(B)/2, and π(Q) ≤ π(M ∖ E_k) < 1/k.
- **N1.0(b).** On Q_k worlds i and j agree. A joint error set Z gives C △ Z ≺_i C and ≺_j C, against
  competitiveness on {i, j}.
- **N1.0(c).** On R_ij, for either advice exactly one of i, j errs. So δ_j = −δ_i on R_ij, and δ = 0 elsewhere.
- **N1.1.**
  - The world-i vector 1_Q − 1_{P′} is ≤ 0 on D_m, since Q ∩ D_m = ∅. So it is D^ν-localized, and K3.1(b) (refereed
    CORRECT) gives ρ(Q) ≥ ρ(P′) > 0, which contradicts ρ = 0 on Q.
  - So C ⪯_j X_n for each of countably many disjoint non-null P′_n ⊆ P. Every ν_j ∈ 𝒩_j then has
    ν_j(Q) ≤ ν_j(P′_n), and Σ_n ν_j(P′_n) ≤ 1 by finite additivity. Hence ν_j(Q) = 0.
  - The partner's own carrier plays no role, because world j's comparison is endorsed in full, not localized. That
    is why N1.1 reaches the purely finitely additive part π_j. N2.2 does not reach it.
- **Remark (i).** The swap sits inside R_ij, so δ_i, δ_j do not depend on C off R_ij. N1.0(b) is not needed for
  N1.1, and N1.1 uses no strict (G) at all, only competitiveness and K3.1(b). Correct the remark.
- **(ii).** On Q_i, δ_j = δ_k = −δ_i. Pigeonhole over n gives the world l.
- **(iii).** ν(δ_i) = −ν(P′) < 0 directly.

### 1.2 N1.2 — CORRECT
- **Setup.** X_Λ has E_iX_Λ = Λ_i ∩ R_ij, and it is correct at both i and j on Q_k.
- **Errors.** In the non-(R) case, F_i = (Λ_i ∖ E_iC) ∩ R_ij and F_j = (E_iC ∖ Λ_i) ∩ R_ij. Here X_Λ has no world-j
  errors off R_ij, because P_i = P_j is correct at j on Q_k.
- **Vertices.** C_{e_i} ⪯_i P_i forces C_{e_i} = P_i by strict (G), and then F_j = ∅. The case e_j is the mirror.
- **Z_ij ⊆ E_iC.** This is N1.1 with P = F_j (visible at i) and Q = Z_ij ∖ E_iC ∖ D_m. It contradicts
  ν*_j ≥ ρ*_jμ with ρ*_j > 0 on V_j.
- **(D).** Its remaining clauses follow from the same lemma.
- **Inputs.** N1.2 uses (S) through the face KKM, and (NC) at i and j. Both are in the statement.

### 1.3 N1.3 — CORRECT
- **(a).** On R_ij, E_i(T1) ∩ E_j(T1) = ∅. So the joint blind set lies in E_i(T1) ∩ Λ_j, which is null. Hence (R)
  holds, X_Λ = Y_k is coherent, and that contradicts M1.6(b) (refereed CORRECT).
  - For c^T, V_j = R⁰_j ⊇ E_i(T1) ∩ R_ij.
  - The script check (1) confirms the set algebra.
  - This settles Q_M1 in the reading M1_referee §6.5 required (Λ_k = E_k(T1) ∩ M). The three-vertex reading is
    treated in §2.6.
- **(b).** P = F_j ∩ V_i ⊆ E_iC ∩ R_ij and Q = F_i ∩ Λ_i ∖ D_m ⊆ R_ij ∖ E_iC. Then N1.1 applies. The witness C of M1.7
  is C_p with p in the open edge, since F_i and F_j are non-null.
- **(c).** M = R_ij ∪ R_ik, and the two descriptions agree on Q_i.

### 1.4 N1.4 — GAP (fixable), then CORRECT
**The gap.** §4 says "by (Nest), c_t is nondecreasing". (Nest) (P4B_referee §1; Q1/Q3 for (Nest_e)) only says that
{E_i(C) : C ∈ C_L} is a chain.
- Lemma N0 gives continuity and surjectivity of β(p) = μ(E₁C_p). It does not give monotonicity of p ↦ c_p, and
  P4B_referee deliberately avoids assuming it.

**Fix.** Index by the chain itself: c_b with μ(c_b) = bμ(R), as in P4B and Q3.5 on edges. Lemma N0(iii) gives closed
b-sections, and N0(iv) gives competitiveness on {i, j} at every interior b. Every step of N1.4 and N1.5 then runs
verbatim.

**Checks after the fix.**
- **(a), left.** s < τ gives c_s ⊆ c_τ ∖ N″, so C_s ⪯_i X by (G). Closedness gives C_τ ⪯_i X, which contradicts
  X ≺_i C_τ.
  - At τ = 1, c_1 = R, and the section at the vertex is closed by (S).
- **(a), right.** This is the mirror at j. At τ = 0 it gives P_i ⪯_j X with E_jX ⊊ R, a contradiction.
- **(b).** X ≺_j C_t. S_j(X) is closed and misses t, and the nearby t′ > t are interior, hence competitive on {i, j}.

### 1.5 N1.5, N1.6 — CORRECT (after §1.4)
- **Step 1.** The strict-escape vector is 1_{D∖c_{t′}} − 1_{c_{t′}∖(c_t∪D)}. Its positive part lies in D, which
  misses D^ν_m, so it is D^ν-localized. K3.1(b) gives ρ = 0 on c_{t′} ∖ c_t.
- **Step 2.** S is an initial interval. τ ∈ S by left no-jump; this is a countable union along s_n ↑ τ, because the
  family is monotone. τ < t₀ contradicts Step 1 at τ ∈ T.
- **Step 3.** c_g = ⋂_{t>g} c_t gives Λ_ν ∖ c_g null. The case g = 1 uses left continuity at 1. The case T = ∅ is
  trivial.
- **N1.6(a).** Q ⊄ c_t and Q ∩ c_g ≠ ∅ give g > t, so P ⊆ c_t ⊆ c_g. Every member of C_L is a chain model by
  N0(ii).
- **N1.6(b).** Choose the blind piece off both D^ν_m and the given family's D_m. The comparison then lies in 𝔚_D and
  is D^ν-localized.
- **N1.6(d).** M1.7 places F_i ⊆ R ∖ c_t and F_j ⊆ c_t.
- **Scope.** N1.5 places no hypothesis on world j, and it is strictly more than K3.8. This is the strongest
  two-world structural statement now available for nested systems.

### 1.6 §4 reduction and §6 — CORRECT as stated
The necessary conditions for a non-nested two-world blind-target system all follow from cited results:
- a rigid or tied crossing, and failure of (MC_sel) at both worlds (S1 §4);
- partner nullness on the target (N1.1).

"I do not conjecture that one exists" is appropriately cautious. §6 is a correct reading: N1.1 uses no veto, no
(Imp) and no closedness.

### 1.7 N1.7 — CORRECT
- C ⪯_i X fails: the comparison is D-localized, ρ*_i(Q) = 0 and ρ*_i(P′) > 0.
- C ⪯_j X fails: ν*_j(Q) ≥ ρ*_j(Q) > ρ*_j(P′) = ν*_j(P′), using π*_j(P′) = 0 (N1.0(a)) and a small P′ (absolute
  continuity).
- Only ρ*_i(F_j) > 0 is used from (W2). "Violates (S)" is right, because C = C_p is (S)'s competitive selection.

### 1.8 N1.C — WRONG as stated
**Counterexample** (i = 1, j = 2). Let q ∈ T1 ∩ co(K′ ∪ [e₁, e₂]) with q ∉ co(K′ ∪ {e₁}), for instance
q = (v₁ + v₂)/2 at (ε, s) = (0.3, 0.5) or (0.6, 0.5). Put K := co(K′ ∪ {e₁, q}) and C := D_K = P₁ ∩ {q·g > 0}.
- **C is a between model.** K ∩ [e₁, e₂] ∋ e₁, and K ⊆ co(K′ ∪ [e₁, e₂]).
- **C is not P₁.** By separation of q from co(K′ ∪ {e₁}), there is an open set of g ∈ U with g₁ > 0 and q·g < 0, and
  it meets R₁₂.
- **C is not P₂.** Indeed C ⊆ P₁.
- **Its world-1 errors on R₁₂.** They are the g ∈ R₁₂ with g₁ > 0 and q·g ≤ 0. Since q ∈ T1, these are rejected by
  D_{T1} too. So E₁C ∩ R₁₂ ⊆ E₁(T1) ∩ R₁₂: C does **not** cross T1.

`n12ref_py/n1c_probe3.out` confirms this. On 400 000 samples, |C △ P₁| on R₁₂ is 53 and 528 samples, and the crossing
pieces are (132 910, 0) and (132 786, 0). `n1c_probe.out` and `n1c_probe2.out` find many such non-crossers, all with K
containing e_i or e_j. The note's script never tested such K: its edge point is m with t ∈ [0.02, 0.98].

**Restricted form.** With K meeting the **open** edge, every model sampled crossed T1. This includes K = co(K′ ∪ {m_t, q})
with m_t → e_i: the smaller crossing piece decays like O(t) but is non-null (`n1c_probe4.out`).

**Repair.**
- Restate N1.C as: "every coherent between model D_K with K ∩ (e_i, e_j) ≠ ∅ crosses T1 on R_ij".
- Restate the consequence: N1.1 forbids those edge-selected models under the shadow hypotheses.
- Note that open-edge-selected models can have K ∩ [e_i, e_j] at a vertex (K3.7′ gives only K ∩ [e_i, e_j] ≠ ∅). The
  consequence therefore does not cover every intermediate edge-selected model, even if the restricted N1.C holds.

### 1.9 Q_N1
**The "No" direction is correct.**
- The maximal endorser tuple satisfies the first three properties (L4.1).
- It satisfies (N1.2) by N1.2(R)/(D), with K3.7′ for the between form.
- M0closed(a), via L4.1.4, removes the case where every Λ_k is null: strictly positive fields force p* ∈ Δ°.

**Wording.** "T1 on M_U would then reduce to covers with an (M1) world" should read "with a world failing (NC)".
- (M1) worlds satisfying (NC) are inside Q_N1.
- Next to two (RL) partners even those are covered by M2.6 and M23_referee.

**Recommended strengthenings.** Each is PROVED and makes the question sharper.
- Replace the rigid alternative by N2.3′(d). Whenever Λ_i ∩ Λ_j ∩ R_ij is null, **every** extreme edge θ-Bayes
  model of (ρ*_i, ρ*_j), θ ∈ [0, 1], is coherent. This is an edge (γ₀) for both tie-breaks, and much stronger than
  rigidity of Λ_i alone.
- In alternative (D), add N1.2's extra clause: the partner is totally null (π included) on a non-null part of the
  joint blind set. This is not field-level, but it constrains any realisation.

---

## 2. N2 Part I

### 2.1 N2.1 — CORRECT; vertices of the face
**(a) The carrier argument.**
- One carrier E serves π = Σπ_k. Apply Step 1 to each π_k and take the union.
- X = C △ (W ∖ E) ⊆ U is regular, so every C ⪯_k X is relevant.
- The CA change is < −2η at every k ∈ S, and the π change is < η. So every endorser strictly prefers X, which
  contradicts competitiveness.

**(b).** The range of the vector measure is convex and compact (Lyapunov) and misses the open negative orthant.
Separating from a cone forces w ≥ 0 and w·v ≥ 0 on the range. The set {Σ w_kχ_kρ_k < 0} is then null.

**(c).**
- On Q_k, χ_i = χ_j = +1.
- On R_ij, χ_j = −χ_i, which gives the two threshold conditions.
- The elementary proof also checks: monotone unions give a(θ_a) = 0 = b(θ_b), αβ < 1, and the two strict
  inequalities.
- NUMERICS (A) agree in 4000/4000 cases. The LP and the breakpoint test are both correct implementations.

**The face may include vertices.** w ∈ Δ_S may be a vertex e_i of Δ_S. Then the conclusion is only χ_iρ_i ≥ 0: every
world-i error of C lies in {ρ_i = 0}. Nothing is said about C's correct advice or about the other worlds. On an edge:
- θ = 1 is exactly "E_i(C) ∩ R_ij ⊆ {ρ_i = 0}", and θ = 0 is its mirror;
- if ρ_i ≡ 0 on R_ij (a totally CA-blind world), every edge model is 1-Bayes, so N2.1 is **vacuous** there.

This is not a defect. It is what makes N2.1 consistent with L2 (the θ = 1 phase b < a) and with (V0). But it means
that every downstream result is empty at a totally blind world. N2's own §6 says so for (V0) ("all its edge models
are θ = 1 models"). §0 item 1 should add a sentence on this.

**N2.1′ (M2 setting).** The perturbed X is a forced pair:
- C is competitive on S ∋ 1, and ψ_j(X) < ψ_j(C) for j ∈ S ∖ {1}, so (RL-2) gives C ⋠_j X;
- so C ⪯₁ X, and φ ∈ 𝒩(𝔉𝔏) endorses it.

CORRECT.

### 2.2 N2.2, N2.2′ — CORRECT
- **N2.2.** On the given non-null set, e_θ = −(1−θ)ρ_j ≥ 0 forces θ = 1, and then E_iC ∩ R_ij ⊆ {ρ_i = 0}.
- **Relation to N1.1.**
  - N2.2 gives N1.1's conclusion at the level of CA parts, for all of C's errors at once.
  - N1.1 gives in addition ν_j(Q) = 0, including the partner's pfa part, but only pair by pair.
  - The two are complementary, and consistent.
- **N2.2′.** Off the joint blind set, e_θ < e_θ′. Then {e_θ′ ≤ 0} ⊆ L_θ ∪ joint ⊆ E_iC ∪ joint. The (Nest_e)
  criterion follows.

### 2.3 N2.3 — CORRECT (flagged priority)
- **The four inclusions.** For X = E^{θ,−}: θ′ ≤ θ gives c ⊇ L_θ (with no hypothesis), and θ′ > θ gives c ⊆ L_θ
  (null joint blind set used). For X = E^{θ,+}: θ′ < θ gives c ⊇ U_θ (null joint blind set used), and θ′ ≥ θ gives
  c ⊆ U_θ (with no hypothesis).
- **Conclusion.** C ⪯_i X with c ⊇ A forces c = A, by strict (G) at i. C ⪯_j X with c ⊆ A forces c = A, by strict
  (G) at j. Both are edge models, so X = C.
- **Vertices.** These are as stated.
- **The hypothesis is sharp in the proof.** Without null joint blindness, two of the four cases fail, and nothing
  else rescues them (§2.5).
- **Check in L2** (`l2_consistency.out`, exact). For (λ|_{d_a}, λ), every E^{θ,±} on a 201-point θ-grid is a path
  model C_b, and every C_b is θ-Bayes. Here θ ∈ (½, 1] gives C_a, θ = ½ gives C_a and C_1, θ < ½ gives P₂, and θ = 1
  gives P₁ and C_a.
- **N2.3′.** This is correct.
  - (b) needs K3.7′ and H12_referee §1.1, as cited.
  - (c): the replacement of M1.5(a) on edges is exactly E^{θ,−} = T^i_θ.

### 2.4 N2.4 — trichotomy CORRECT; GAP (wording) in (int_i)
- **What is proved.** C = C_p with p interior and θ*-Bayes; F_i ⊆ {e_θ* ≥ 0} and F_j ⊆ {e_θ* ≤ 0}. This gives (vis)
  as stated, and in (int_i) gives E_i(C) ∩ R_ij ⊆ Λ_i. So the **source** of world i's trade (E_iC ∖ E_iY_k ⊇ F_j) is
  i-blind.
- **What is not proved.** At θ* = 1 the condition on F_i is vacuous (e_1 = ρ_i ≥ 0). F_i may be CA-visible at i, and
  then ν_i(F_i) ≥ ν_i(F_j) = π_i(F_j) is carried partly by ρ_i(F_i).
- **The claims to change.** Three claims overstate:
  - §0.4 "(int_i) … so source and target of world i's trade are both i-blind";
  - §3 "in (int_i), at world i by π_i alone";
  - §0.8 and §6 "world i trades errors inside its own blind set against errors inside its own blind set".
- **When the claims hold.** They hold when Λ_i ⊇ c_T^{ij}, for instance at p* = e_i (N2.5(c)), and so in
  configuration (V) ((V4) is right).
- **Fix.** "(int_i): the source is i-blind; the target is i-blind as well when Λ_i ⊇ E_i(T1) ∩ R_ij, in particular
  at p* = e_i."

### 2.5 N2.5, N2.5′ — mostly CORRECT; two GAPs
- **Trichotomy.**
  - θ* < θ₀: on F_i, 0 ≤ e_θ* ≤ e_θ₀ ≤ 0, so (θ₀ − θ*)(ρ_i + ρ_j) = 0.
  - θ* > θ₀: the mirror on F_j.
  - θ* = θ₀: both lie in Z_θ₀.
  - (a) and (c) are correct. In (c), the p* of L4.1.3 belongs to the same endorser tuple; state this.
- **GAP (wording): "M1.9 for arbitrary endorsers".**
  - M1.9's hypothesis allows ties (including joint blindness) on E_j(T1) ∩ R_ij, and is strict only on E_i(T1) ∩ R_ij.
  - With arbitrary endorsers, N2.5 then leaves the branch θ* > θ₀ with F_j ⊆ {ρ_i = ρ_j = 0} ∖ c_T. N2.3 cannot close
    that branch, since joint blindness is not null.
  - So N2.5(a) generalises M1.9 in its endorsers but **strengthens** its tie hypothesis to "Z_θ₀ null on both sides".
  - Say so, and correct the bullet "CA endorsers removed from M1.9" in §5.
  - The charge-form M1.9 of M1_referee §5.1 is the correct arbitrary-endorser version.
- **GAP (inherited): N2.5(b).** What the argument proves is the following.
  - Null joint blindness gives θ* = θ₀, so Z ∩ c_T and Z ∖ c_T are both non-null.
  - E^{θ₀,−} = Y_k △ (Z ∩ c_T) is coherent, and the *local* facet-plane lemma (M1_referee §3.4) gives a facet F_m along
    every point of every R_ij-arc of which Z ∩ c_T accumulates.
  - E^{θ₀,+} gives a facet F_{m′} for Z ∖ c_T. It may differ from F_m.

  So "two-sided … of some facet", and "shell" (as opposed to accumulation), are not proved. Replace them by M1_referee
  §5.2's one-sided-per-side statement. (Under null joint blindness the ties are indeed a frozen ratio.)
- **N2.7(c)** must then read: "for one side (Z ∩ c_T or Z ∖ c_T), accumulation fails along the R_ij-arcs of every
  facet".
- **N2.5′ — CORRECT.**
  - Every W ⊆ J_i ∪ J_j makes T1 △ W ≺_k T1, so competitiveness passes to {i, j}.
  - The carrier modification keeps W′ inside J_i ∪ J_j.
  - The separation is then the restricted N2.1(b).

### 2.6 N2.6 — CORRECT; one WRONG sentence; the nearby result
- **The proof.** The joint blind set is Λ_j ∩ c_T, which is null. N2.3′(a) puts X_ij = Y_k ∈ C_L, against M1.6(b).
  NUMERICS (B) confirm X₁₂ = Y₃ for the shadow and its midpoint failures.
- **WRONG: "(a) Equivalently (M1.1(b)), no cover has T1 admissible at all three vertices."**
  - Three-vertex admissibility of the maximal field means Λ_k ⊇ E_k(T1) ∩ M, not equality (M1_referee §6.5).
  - N2.6 needs Λ_j ∩ c_T^{ij} null, and enlarged Λ_j can violate this.
- **The nearby result (PROVED here from N2.3′ and N2.6).** If T1 is admissible at all three vertices for the maximal
  field, then **Λ_i ∩ Λ_j ∩ R_ij is non-null on every edge**.
  - Proof: on R_ij, Λ_i ⊇ c_T and Λ_j ⊇ R_ij ∖ c_T. If the joint blind set were null, then Λ_i ∩ R_ij = c_T exactly
    and Λ_j ∩ c_T = ∅ (mod null), and N2.6 applies.
  - By N1.2(D), world j is moreover totally null (π included) on a non-null part of that joint blind set, off the
    carrier of ν*_i.
  - Replace the "equivalently" sentence by this.
- **(b), (c).** These are correct. In (c), (B1) gives ρ₂ > 0, hence the null joint blind set.
- **(d) is mislabelled.** M1.11's hypothesis is ρ_k > 0 on J_j ∪ J_k. N2.6 needs the partner to see
  c_T^{ij} = W_i ∪ J_j. Neither statement implies the other. Call (d) "the ranking-level analogue", not "M1.11 at the
  ranking level".

### 2.7 N2.7 — (a), (b), (d) CORRECT; (c) GAP (§2.5)
I verified (d) in full.

**The veto.** Φ₁(X) = ∫_{X∩V₁} ρ*₁ is an L3.4 veto:
- ω(g, accept) = ρ*₁1_{V₁}, which charges only world-1-wrong acceptances, because V₁ ⊆ {g₁ < 0} (M1.2, refereed
  CORRECT);
- Φ₁(B¹) = Φ₁(P₁) = 0.

**(V).** Φ₁(P_j) = ρ*₁(V₁ ∩ {g_j > 0}) = ρ*₁(V₁ ∩ R_{1j}) > 0 for some j.

**(Imp).**
- At an interior q, C_q is competitive on {1, j} and is an edge model.
- If Φ₁(C_q) > 0, C_q has a visible world-1 error. N2.2(a′), with the partner density ρ_j > 0 a.e., then gives
  E₁(C_q) ⊇ Λ₁ ∩ R_{1j}.
- That set is non-null, since it contains M ∩ {g₁ > 0} ∩ R_{1j} (M1.2(ii)).
- Removing a piece of it does not change Φ₁, since the piece is disjoint from V₁, and it is strictly better at world 1.
- At q = e_j the same removal works. L3.4 only uses (Imp) at an interior t_c anyway.

**The setting.** "The configuration is (V)" is right: p* ∈ Δ° is excluded by L4.9 + Prop. R (L4_referee), and
configuration (I) is excluded by Prop. R.

### 2.8 §6 — (V1)–(V6) CORRECT; wording elsewhere
- **(V1).** A(c*) = {e₁}. p* in an open edge would force joint blindness with world 2 or 3 on some J_l (L4.3),
  contradicting ρ₂, ρ₃ > 0. p* = e₂ or e₃ is impossible for the same reason.
- **(V2)** is N2.3′, since ρ₂, ρ₃ > 0.
- **(V3).** θ = 1 gives c ⊆ Λ₁. θ < 1 gives e_θ = −(1−θ)ρ_j < 0 on Λ₁, so c ⊇ Λ₁^R. The two closed sections S₁, S₂
  are as stated, and they meet exactly in {c = Λ₁^R}.
- **(V4).** θ₀ = 1, and θ* < 1 would put F₁ inside the joint blind set, which is null. So θ* = 1. c = Λ₁^R would give
  F₁ = c_T ∖ Λ₁ = ∅, so c ⊊ Λ₁^R, and here both F's lie in Λ₁.
- **(V5)** is N2.5′.
- **(V6)** follows from N2.7(d).
- **"L2's world 1 does not refine its veto λ|_{d_a} (PROVED)".**
  - It is true. λ|_{d_a} is an L3.4 veto paid at e₂, and (Imp) holds by N2.2: C_b with visible errors has b > a and
    contains c_a, and fixing a piece of c_a is neutral.
  - L2 has closed sections, so L3.4 forbids refinement.
  - The proof is this, not anything in L2_notes; cite it.
- **"(ii) … contradicts Conjecture L2.C …, so the partners would need endorsers with nonzero pfa parts".** This holds
  only if L2.C is true. Write "if L2.C holds".
- **Q_N2 is well posed and is a good first test.** "(V0) reduces to a two-world question" overstates. An edge system
  inside a three-world cover need not be a full two-world system (S1.9), and conversely.
- **"T1 is not edge-Bayes on R_ij for p* ∈ Δ°"** is an unproved reading. Label it.

---

## 3. Consistency of N1, N2 and L2

| Pair | Relation | Consistent? |
|---|---|---|
| N1.2 ↔ N2.3′(a) | N1.2 is the contrapositive of "null joint blindness ⇒ X_ij selected", plus partner-nullness in (D). N2.3 is stronger in giving every θ | yes |
| N1.3(a) ↔ N2.6 | the same theorem (Q_M1 = No), by two independent routes (swap lemma vs. Pareto off the carriers) | yes |
| N1.1 ↔ N2.2 | the same mechanism. N1.1 also kills the partner's pfa part; N2.2 constrains all errors at once | yes |
| N1.5 ↔ N2.2 | N1.5: nested chain, any partner, blind set = c_g. N2.2: any C_L, partner visible. Both forbid blind targets with visible sources | yes |
| N1.6(d) ↔ N2.4/N2.5(c) | on a nested edge the M1.7 exchange is visible or blind–blind; at p* = e_i it is internal | yes |
| N1, N2 ↔ L2 | L2 is nested, with Λ = c_a = E₁(C_a) (N1.5 shape, N2.3′ rigidity). Its path is θ = 1 for b < a and θ = ½ for b > a (N2.1(c)). All E^{θ,±} are path models (N2.3). Its comparisons have blind sources and visible targets (N1.6(c), N2.2). Its veto is not refined (L3.4 + N2.2). Checked exactly in `l2_consistency.out` | yes |
| N1 §0 item 5 ↔ N2 §6 | both place a two-world blind-target system in non-nested C_L with partner-null (hence jointly blind) targets | yes |

No contradiction was found. The two notes duplicate each other on Q_M1, so one proof should be kept as the main one:
- N2.6 via N2.3 is shorter and gives more;
- N1.2(D)'s partner-nullness should be kept as a complement.

## 4. Requested changes (minimal)
1. N1 §4: reindex by the chain (Lemma N0; Q3.5 on edges) instead of "c_t nondecreasing by (Nest)".
2. N1.C: restrict to K ∩ (e_i, e_j) ≠ ∅, and restrict the consequence (§1.8). Record the counterexample.
3. N1.1 remark (i): strict (G) is not used.
4. N2.4, §0.4, §0.8, §6: in (int_i) only the source is forced blind (§2.4).
5. N2.5(a) and §5: M1.9's one-sided ties are not covered. N2.5(b) and N2.7(c): one facet per side (§2.5).
6. N2.6(a): delete "Equivalently …", and add the three-vertex nearby result (§2.6). N2.6(d): relabel.
7. Q_N1: "failing (NC)" instead of "(M1)". Add N2.3′(d) and N1.2(D)'s partner-nullness.
8. Status lines: M1.2, M1.3, M1.6 and M1.7 are refereed CORRECT. Cite L3.4 + N2.2 for L2's non-refinement. Make (V+)(ii)
   conditional on L2.C. Change "reduces" to "first test" for Q_N2. Fix the docstring in `n2_checks.py` (B).

## 5. Files (`n12ref_py/`)
- `n1b_edge_rerun.out` and `n2_checks_rerun.out`: identical reruns.
- `n1b_common_copy.py`: a copy of `n1py/n1b_common.py`, so that nothing is imported across folders.
- `n1c_probe.py`/`.out`, `n1c_probe2.py`/`.out`: random search; non-crossing between models with K ∋ e_i or e_j.
- `n1c_probe3.py`/`.out`: the explicit counterexample K = co(K′ ∪ {e₁, (v₁+v₂)/2}); open-edge search.
- `n1c_probe4.py`/`.out`: the open-edge family m_t → e_i; the crossing piece is O(t) but non-null.
- `l2_consistency.py`/`.out`: an exact check of N2.1(c) and N2.3 on L2's path.
