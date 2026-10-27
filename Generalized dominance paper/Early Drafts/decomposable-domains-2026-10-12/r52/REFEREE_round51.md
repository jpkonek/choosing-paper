# Referee report, round 51: PP45, PP46, PP47, AUDIT_posterior_pairs

23 October 2026. Independent referee. Setting: BRIEF51 (and BRIEF52 for the posterior family). Cautions read: AUDIT_round52, AUDIT_posterior_pairs §5. Background used: PP42 §§1–3, REFEREE_round50 §1 (Thm 3.1(c) without the agreement region, Thm R1, Lemma S), AUDIT_completion (direct (C)), and the ℓ^T of REFEREE_PP32 §3.2 as coded in `PP45_py/tripod_exact.py`.

**Labels.** PROVED: argument checked line by line here, or given here. CHECKED: exact rational computation (authors' scripts re-run, or mine in `r9/PP54_py/`). NUMERICS: floating point or sampled patterns. CONJECTURE / OPEN: as stated.

**Re-runs.** Every author script named in the three notes was re-run from a copy in `PP54_py/rerun/`. All outputs are byte-identical to the stored `.out` files, and every CHECKED script ends ALL PASS (§6). Two PP45 scripts need `../PP42_py` on the path; I symlinked it.

---

## 0. Verdicts

| Note | Claim | Verdict |
|---|---|---|
| PP45 | Lemma 2.1 (type lemma) | correct |
| PP45 | Lemma 2.3 (own Bayes forced; interior weights) | correct |
| PP45 | Thm 3.1 (T + combined cut) | correct; hidden hypotheses named (H1, H2) |
| PP45 | Cor 3.2 (≤ 1 up, ≤ 1 down; tripod; no rectangle or C¹ surface) | correct |
| PP45 | Cor 3.3 (refinements missing two vertices) | correct |
| PP45 | Thm 5.1 (tripod fields) | correct (independently CHECKED); it is a literal single-field realisation (§2.6) |
| PP45 | Prop 5.6 (pointwise estimate) | correct |
| PP46 | Lemma A0 | correct (exact equivalence CHECKED) |
| PP46 | Thm A | correct; T's uniqueness is an unstated hypothesis |
| PP46 | Thm B (pair criterion, "iff") | correct with repair: the sufficiency proof is a sketch (§3.3) |
| PP46 | Cor B1 | correct (CHECKED); its CONJECTURE is partly proved by PP45 Cor 3.2(c) |
| PP46 | Prop C | correct, and slightly more general than stated |
| PP46 | Thm D (star fields) | correct; also a single-field realisation (§3.6) |
| PP46 | Prop E | correct with repair: partially overlapping caps at v are omitted; one-line fix (§3.7) |
| PP47 | Thm 2.5 | correct |
| PP47 | Prop 2.6 | (a) correct in outline; **(b) wrong as stated** (counterexamples, §4.2); (c) correct |
| PP47 | Thm 2.7 | correct; the weak case needs N undominated |
| PP47 | Cor 2.3 | correct with repair (two hypotheses to state) |
| PP47 | Lemma 2.4 | correct under (U); small bookkeeping repair |
| PP47 | Cor 3.3 | **wrong as stated**; correct for rivals that agree with T off a bounded set; OPEN for bounded modifications of a single cap (§4.5) |
| PP47 | Thm 4.1 ((R0) test) | correct as a conditional theorem; the headline omits its hypothesis, and two proof steps need repair (§4.6) |
| AUDIT | Family facts (compactness, continuity, boundary, injectivity) | correct; injectivity holds on the whole closed simplex |
| AUDIT | Pair-ordering theorem | correct for all disagreement types; extends to boundary pairs (§5.2, PROVED and CHECKED here) |

**Main points for the coordinator.**
1. The combined-cut obstruction (PP45 Thm 3.1 = PP46 Thm A, completed by PP47 Thm 2.5) is sound. It is a theorem about the gate-union architecture with universally competitive gated members. It says nothing about the axioms.
2. PP47's "cannot dominate **any** rival" (Prop 2.6(b), Cor 3.3) is false. Beyond the audit's always-contradictory model there is a bounded counterexample: a retreat of the combined cut on unanimous problems. The correct statement is restricted to rivals that agree with T off a bounded set. For those rivals it is actually stronger: the domination is refused at **every** world.
3. The tripod (PP45) and the star (PP46) are not merely "witnessed". Each member is exactly the Bayes model of one fixed field at a weight along a path. That is the excluded CPM-type route. Both notes say this; I make the field explicit.
4. The posterior pair theorem is right. Its certificate D^{ab} = log a − log b is a **coboundary**. So the type test, at the pair, triple and family level, can never be what creates "no global prices" on this family. BRIEF52's target must come from the magnitudes (pair intervals), not from the orders (§5.3).

---

## 1. Hidden assumptions used across the notes

- **H1. Universal competitiveness of every gated member.** Own-Bayes (Lemma 2.3 / 1.2) is derived from it. It is a binding design requirement of BRIEF51 item 5, not an axiom. It is used for the combined cut in PP45 Thm 3.1 (stated), and for the carrying realiser in PP47 Cor 3.3 (not stated). Without it the type lemma has no input, though CG2 necessity remains.
- **H2. T a.e.-uniquely own-Bayes.** This is used in PP45 Thm 3.1, Cor 3.2 and Cor 3.3, in PP46 Lemma A0 and Thm A, and in PP47 Lemma 2.4. PP47 Thm 2.5 removes it under (R0), at the price that the contradiction is with **direct (C)**, not with (TC). Under (R) it is removed only at the four-model checkpoint.
- **H3. Coherent (conic) models.** The realiser-inheritance step ("M agrees with N off a bounded set, hence on the whole cone") needs both models conic. This is true for the D_K models used.
- **H4. Strict CG2 a.e. under (R0).** PP47 Lemma 1.3 needs it, and through it Cor 2.3 (weak branch) and Thm 4.1.
- **H5. A region where the relevant gated members equal T and T is not w-correct.** It is used by PP45 §3.2 and PP47 Prop 2.2(b) and Cor 2.3: off-band Sil(T).
  - For the multicap family it holds globally.
  - For the posterior family it holds only locally. Deep in Sil(T) (planes through the middle of M), every C_a with a near u is silent. Away from u, and in boundary limits, it has to be re-checked.
  - Where it fails, use REFEREE_round50's placement of the improvement inside D.
- **H6. Interior supporting weights.** These are forced for refinements of T, because they repeat T's minority answers on Ans(T) (PP45 remark after Lemma 2.3). Posterior members are not refinements, so this must be re-proved for them.

---

## 2. PP45

### 2.1 Lemma 2.1: correct (PROVED)
I checked the reduction a_w = λ^N_w|e^N_w|, b_w = λ^M_w|e^M_w|, and the CG2 sandwich in the form b_w ≥ e^{−D_w}a_w on W and b_r ≤ e^{−D_r}a_r on R. I also checked the finiteness of D on the relevant sides (κ = ∞ is impossible on W, κ = 0 is impossible on R) and the choice of a finite m.

Two remarks:
- If R(g) = ∅, the hypotheses are inconsistent, because M's weak preference fails with interior λ^M. So (★)'s "min over ∅" never arises.
- Only one of the two preferences needs to be strict. That is what makes PP47 Thm 2.5 a clean extension.

### 2.2 Lemma 2.3: correct (PROVED)
- **(a)** This is the Lyapunov–separation "⇒" direction (REFEREE_round50 §1.1). The shell is a full radial shell, so it meets every cone. Every gated member is conic (H3), so N is the only realiser.
- **(b)** Correct.
- **The interior-weight remark** is correct. With λ_w = 0, T's minority answer (right only at w) is strictly worse than silence at the other two worlds, which carry all of λ's weight. This needs minority answers on non-null subsets of every class M_w, which T has.

### 2.3 Theorem 3.1: correct (PROVED; CHECKED by re-run)
- Lemma 1.1 is correct. I re-derived the corner parametrisation, the edge crossings at λ_j and λ_k, h > 0, and the sign criterion for g_j. The threshold rule τ = ε·max(λ_j, λ_k) < t is exact, because the cut corner is the triangle with edge fractions t/ε.
- Band 1 supplies B_2 and B_3, and band 2 supplies B_1. By Lemma 2.2 ("r not top") no world can be the maximum of D.
- The appeal to Thm 3.1(c) without the agreement region is valid under (R) and under (R0).
- §3.2's explicit triangle is valid: F lies off the bands, where AB = T. That is H5.
- **Hidden hypotheses:** H1 for AB (stated) and H2 for T (stated, and later removed by PP47).
- **Overstatement (harmless):** §3.4's "Thm R1 makes the whole interval test exact here" holds under (R) only. The obstruction uses only pair necessity, which holds under both rules.

### 2.4 Corollary 3.2: correct (PROVED; CHECKED)
- **Two ups.** There are three "not top" constraints, which is impossible.
- **One up i, one down j.** Applying Lemma 2.1 with N = C_s and the swapped readings gives i on top and j at the bottom. That is consistent.
- **(c), the rectangle.** A diagonal pair has two ups (or two downs).
- **(c), the C¹ surface.** The tangent plane must lie in the union of the coordinate planes, hence in one of them, and that plane contains a direction with two positive entries.

This **proves** the part of PP46 Cor B1's CONJECTURE ("compatible subfamilies are at most one-dimensional") that concerns C¹ surfaces and axis rectangles. A non-smooth or totally disconnected 2-dimensional compatible set is not excluded by the argument as written.

### 2.5 Corollary 3.3: correct (PROVED)
- K is closed, so every sufficiently shallow corner at a missed vertex misses K.
- The sign of D_K's answer is the positive side of the plane, which contains K. So u ∈ K is not needed.
- In the limit τ → 0 at a fixed edge ratio ρ, the condition for g_j > 0 tends to ρ > κ₀/(1 + 2κ₀). So A, B_k and B_j all occur at arbitrarily small depth.
- The remark that refinements missing exactly one vertex pass the test is also right. If K contains m_j and m_k, every plane that misses K but meets M cuts off m_i alone.

### 2.6 Theorem 5.1, the tripod: correct (PROVED; CHECKED independently), but a single-field realisation

**Lemma 5.2.**
- On band i: Σn̂ = 1 − q = φ(τ) for every family, and Σ|n̂| = 2.
- So n̂·μ^{i,t} = φ(τ) − φ(t), and the cost difference is n·μ ± c·m̂·Σ_w |n_w|μ_w. This gives the margin (1 − 2c)m̂|g| ≥ (3/8)m̂|g|.
- Caps at other vertices are S-sayers: on B_k the bound is φ(τ)(1 − φ(t′)/2) ≥ (3/4)φ(τ).
- −σ is strictly worse because R(g) ≠ ∅ on bands, and contradiction is never optimal.

**Lemma 5.3 (strict CG2).** The scaled magnitudes are |n_w|·H, so the inequality depends only on who says σ. The pair bounds are right.

**(BR).** The sharp range is [25/78, 78/25], inside the stated [3/10, 10/3], because m̂ ≤ 7/8.

**Lemma 5.4.** At the switch, H = 1 from both sides. At t → 0 each cap's field tends to T's field. So (S1)–(S2) hold on the compact tripod.

**(iv) and (vi).** Thm 3.2(a), (b) apply. The selection is continuous (all t_i vanish when the argmax changes) and reaches every member once K₀r ≥ δ.

**CHECKED (`tripod_indep.py`, 110,240 exact checks, ALL PASS).** I re-implemented the design without the authors' library:
- band points are planes through two random edge points;
- each member's advice is computed from the vertices of its own hexagon, with no union lemma;
- δ goes up to 0.33ε.

The script verifies:
- the threshold rule;
- strict own u-Bayes over all four advice values, with the 3/8 margin;
- strict CG2 with constants 1/μ for every ordered pair and world;
- continuity at the switch.

**The caveat, made explicit (PROVED; CHECKED in the same script, check (4)).** Let U be the field with U_w(σ) − U_w(S) = n_w(g) on the bands.
- For every member s and its own move between σ and S: c^s_w(ℓ^s_w(b) − ℓ^s_w(a)) ≤ U_w(b) − U_w(a).
- Every member is exactly the U-Bayes model at weight μ^s/|μ^s|_1, because sign(n·μ^s) is the member's advice.

So the tripod is literally the Bayes selection of one field along a path of weights. This is stronger than "admits a global witness" (where Thm 2.1 gives only "⇒"). PP45 §6 classifies the construction correctly as the excluded route. It settles cube compatibility. It does not supply a continuation.

### 2.7 Proposition 5.6: correct (PROVED; CHECKED by re-run)
- **σ against silence.** On B_j points of H_v, g_v < g_k < 0, since g_k − g_v = h/λ_k > 0 in Lemma 1.1's parametrisation. ℓ^T has β_w = |g_j|F(|g_w|/|g_j|) on M_j with F non-decreasing, so β_k ≤ β_v.
- **−σ against silence.** G(s) = 1/F(1/s) is non-decreasing, so α_k ≤ α_v.
- **Positivity.** Both inequalities follow, using u·d > 0 and u·d′ > 0 (T silent at u, strictly). So θ(s) > 0 and the step 3(1 − η)u·d ≤ 3θd_v is legitimate.
- The constant 3 is right.

---

## 3. PP46

### 3.1 Lemma A0: correct (PROVED; CHECKED)
- Steps 1–3 combine CG2 for the move z → a with the two Bayes inequalities, giving p·e^z < 0 < q·e^z.
- The two-case elimination (|C| = 1 or |W| = 1) is right.

**CHECKED (`pair_criterion_indep.py` (A)).** The statement "the pointwise system is solvable iff ∃ c ∈ C, w ∈ W with p_c q_w > p_w q_c" holds exactly on 120,000 random (piece, p, q). Solvability is decided by an exact 2-D cone test, not by LP.

**Small correction to §3.4.** "Goes through unchanged with p·e ≤ 0" needs p_c > 0 in case C = {c}, and p_w > 0 in case W = {w}. This holds with interior weights and positive constants, which is the case here.

### 3.2 Theorem A: correct (PROVED)
- Every world beats some other world, a finite relation has a cycle, and 2- and 3-cycles are impossible.
- With boundary weights, zero entries do not rescue a 3-cycle: the left-hand product must be positive.
- Every world is two-signed on D_{T,R} under the hypothesis, so the CG2 constants lie in (0, ∞).
- **Unstated:** T must be gated and a.e.-unique own-Bayes (H2). The statement names only R.

### 3.3 Theorem B: correct with repair
- **Necessity** is correct. On an "up" band, A0 says ψ_v is the strict minimum; on a "down" band, the strict maximum.
- **Sufficiency** ("choose ψ, then concentrate increments") is a sketch. It must also say:
  - (i) the CG2 constraint concerns D_st only, so each member's field elsewhere (Ans(T), the other bands, off-band Sil(T)) can be chosen independently to make it own-Bayes at its weight;
  - (ii) on D_st the −σ and contradiction entries are set large at the worlds where they are wrong, which keeps σ/S optimal (interior weights);
  - (iii) piece-constant multiples of |g| give (BR) and an envelope.

  With these the converse is PROVED. It is a statement about a pair in isolation, as the note says.

### 3.4 Corollary B1: correct (CHECKED)
`pair_criterion_indep.py` (B) reproduces the ten incompatible pairs and the eight maximal compatible subfamilies (two stars and six triangles). The order enumeration from Lemma 2.2's readings agrees with Thm B on all 28 pairs. On the CONJECTURE, see §2.4.

### 3.5 Proposition C: correct (PROVED)
The hypothesis "Y answers σ on A" can be weakened. Y need not equal T off A:
- every realiser must answer σ on A, so Thm A excludes it;
- guidance fails at every world on A alone.

### 3.6 Theorem D, the star: correct (PROVED; NUMERICS re-run)
I checked (a), steps 1–8. The key identities are:
- π^{v,s}·e = θ(τ) − θ(s) on the own band;
- θ(1 − κθ_s/θ_δ) ≥ θ(1 − κ) on the v-wrong piece of another band;
- the humility bound η < 1/(2 + 2κ);
- the Ans(T) bounds with ρ_A < 1/3 and θ_δ < 1/6.

(b) holds because the answerer carries the only humility at each disagreement point. (c)–(e) hold as stated.

**Same caveat as §2.6, made explicit.** Each star member is exactly the Bayes model of the *base* field at weight π^N: the own-band value is θ(τ) − θ(s), and the other bands' values are positive. So the star is a single-field realisation along a weight path. This is stronger than §4.4's "global witness".

The open-interval failure (§4.3) is correct and forced. It is useful evidence: (TC) under (R0) holds here with degenerate pair intervals, because CG2 is strict pointwise. This bears on PP47 Thm 4.1 (§4.6).

### 3.7 Proposition E: correct with repair (PROVED here)
- (i) is correct.
- (ii) checks out, including through every realiser's gate. The realisers are caps C^{v,s′} with s′ ≥ s. Humility makes their per-world values no larger than the base values, and per-world rescaling does not affect signs.

**Gap.** (ii) treats caps at v *disjoint from* G. Two cases are missing:
- **Caps at v containing G.** These are excluded at once: rec(C, X) = (H_v(s) ∖ G : σ → S) is a pure v-improvement.
- **Caps at v meeting G partially** (G = G_in ⊔ G_out, with G_in ⊆ H_v(s)). The v-condition gives Φ_v(G_out) ≥ Φ_v(C) − Φ_v(G_in). Write θ* := sup θ on G, which is < 1/2. The c-condition, with |Φ_c(C)| ≤ Φ_v(C)/2, gives (1 − θ*)(Φ_v(G_out) + Φ_v(G_in)) ≤ Φ_v(C)/2. Together these force 1 − θ* ≤ 1/2, which is impossible.

With this, §0 item 4's summary ("no star member dominates") is correct.

---

## 4. PP47

### 4.1 Theorem 2.5: correct (PROVED; CHECKED by re-run)
**(a)** With T weak, take a family point where (★) fails; one must exist, because the three B-families exclude every top. Equality throughout the chain then forces:
- max_W D = min_R D = m;
- D_w = m at all three worlds (a_w > 0 everywhere).

Since D is global, every point of D_{T,AB} is then tight. This gives λ_T·e^T = 0 and e^AB = γ⊙e^T.

**(b)** The three one-negative sign patterns occupy alternate sectors of λ_T^⊥. Opposite sectors are negatives of each other, so v_3 ∈ −cone(v_1, v_2). Hence 0 is a positive combination, and Lyapunov gives a bounded E with ∫_E e^T = 0 ∈ R³. X = T[E ↦ AB] is not conic, hence incoherent. Both gate values are 0, so (R0) gives an all-world tie, and **direct (C)** fails for the coherent undominated T (AUDIT_completion line 70).

**(c)** Correct as stated: only at the four-model checkpoint, since a larger family may contain another gated model silent on E.

### 4.2 Proposition 2.6: (a) correct in outline; (b) wrong as stated; (c) correct
**(b) counterexamples (PROVED).** Let N = AB, or any N agreeing with AB off a bounded set.

- **The audit's example.** X ≡ contradiction. N ⪯_w X by guidance at every w, and the reverse has no coherent realiser and is a pure improvement.
- **A bounded retreat of N itself.** Take a bounded non-null F ⊆ U (unanimous problems) and X := N[F ↦ S].
  - rec(N, X) is a weak worsening at every world, so guidance accepts N ⪯_w X at all w.
  - The reverse is a pure improvement. No coherent model is silent on unanimous problems, so it has no realiser.
  - So N **strictly dominates** X.

  This also refutes the first bullet of the proof, "a two-valued rival never makes N pointwise better at all three worlds". X takes only N's values and silence.
- **Second bullet of the proof.** "A gated realiser M must agree with N off a bounded set" holds only if {N ≠ X} contains N's cones off a bounded set. For X = N[F ↦ ·] the record has bounded support, and T itself can be the realiser.

**Repair (PROVED).** Restrict to rivals X with X = T off a bounded set G, that is, fills of T, including the two-corner rival.
- Then {N ≠ X} ⊇ {N ≠ T} ∖ G.
- At every world w this set contains non-null points where σ is w-wrong: band w if w is one of N's vertices, and a B-family of the other world otherwise. So guidance refuses at every w.
- Every realiser M agrees with N on {N ≠ T} (H3), so it answers σ on refinement cones at two vertices. It cannot be gated beside T: H1 is needed for M, and H2, or Thm 2.5 under (R0), for T.

Hence **N ⪯_w X is refused at every world**. That is stronger than non-domination.

### 4.3 Theorem 2.7: correct (PROVED; CHECKED by re-run)
- The per-band criterion "r_b > min(r_j, r_k)" is A0 with W = {b}, p = μ and q = λ_N.
- The weak case reduces as claimed: the three one-positive A-patterns also occupy alternate sectors.
- **Missing hypothesis:** for general N, the direct-(C) contradiction needs N to be coherent and undominated. This is automatic for N = T.

### 4.4 Corollary 2.3 and Lemma 2.4
**Cor 2.3: correct with repair.** I checked:
- the shrinking-F argument of Prop 2.2(b), which uses closed sections at p_0 and the common envelope;
- the (S2) limit;
- the unique case.

Two things should be stated:
- (i) the weak branch uses strict CG2 a.e. (Lemma 1.3, strict case; H4);
- (ii) the argument needs a bounded F on which the members near T equal T and T is not w-correct (H5). That is available here, and only locally in the posterior family.

**Lemma 2.4: correct under (U).** The guidance-carried worlds of step 1 give the bound ∫_{G_n} env^T, not the realiser bound. So κ_n should include the term w ↦ ∫_{G_n} env^T. Conicity of N_n is not needed: without it, the extra terms on G_n are again bounded by envelopes.

### 4.5 Corollary 3.3: wrong as stated; correct for fills of T; OPEN for modifications of a single cap
- **"Any rival" is refuted** by both examples of §4.2.
- **The repaired statement is §4.2's**, for rivals that agree with T off a bounded set. It needs H1 for the realiser, which the statement should name.
- **What the proof does not reach.** Take bounded modifications of a single cap, for example X = C_1[G ↦ S] with G ⊆ H_1. A realiser carrying N = AB ⪯_w X need only answer σ on band 2 and on the cone of G. It need not carry two full corners.
  - If that cone carries only A_1 (or only B_3), the type test against T is **passable** at the order level (`pair_criterion_indep.py` (C), CHECKED).
  - If it carries B_2, the test fails.
  - Every *refinement* realising such a cone misses m_1, so it fails by PP45 Cor 3.3. A non-refinement realiser would be PP47's own aim (ii) (Prop 5.1, CONJECTURE).

  So for this class the claim is OPEN, not proved.

### 4.6 Theorem 4.1: correct as a conditional theorem; three repairs
**Scope (the audit's caution).**
- The theorem assumes two-valuedness, (BR) and strict CG2 a.e. for every pair.
- §0 item 3 and the "Answer" paragraph state the equivalence without the strict-CG2 hypothesis. That must be restored.
- The parenthetical "which (R0) needs anyway" is not a theorem. Thm 3.2(c) needs strictness only for strict dominations, and a design could live without it.
- Nothing here licenses a claim about all (R0) systems satisfying (TC).

**Proof step 4.** "Unless a pair interval is degenerate, which strict pair CG2 excludes" is false. PP46's star has pointwise-strict CG2 with every two-sided interval a single point (§3.6, re-run). The step survives: for a degenerate pair, strictness at its unique constant is exactly the hypothesis, and the other pairs sit in their open intervals.

**Proof step 5.** The ray argument covers triangles whose three links are gate links on the referee's three point patterns. A complete proof must also exclude triangles that use guidance links, or other patterns of (X, Y, Z) ∈ {σ, S}³. The fix works (PROVED here):
1. Build the Lemma 3.0 potential with slack on every edge except the pinned σ/S edges of the attained sets. All other cycles are strictly negative: gate edges into −σ or contradiction have no return edge, and strict guidance makes each σ/S edge strict.
2. U is then strictly increasing in rank. So a guidance link with 𝒰 = 0 is trivial.
3. A gate link with 𝒰 = 0 lives on the pinned set, where the pointwise link vectors are multiples of (1, −1, 0), (0, 1, −1) and (−1, 0, 1) in scaled coordinates.
4. With at most two pinned pairs in the tight orientation, no nontrivial nonnegative combination is zero, which is step 5's conclusion.

**CHECKED.** Ex1–Ex3 re-run identically. They are atomic toy instances, not fields on the geometry; that is adequate for showing the attained-tight case is a genuine failure.

---

## 5. AUDIT_posterior_pairs

### 5.1 Family facts: correct (PROVED; CHECKED where computable)
- **Compactness and convexity.** a·p ≥ min p_i > 0, and the projective map sends segments to segments.
- **Continuity.** It is Hausdorff-continuous in a, uniformly.
- **Special indices.** M_u = M and M_{e_i} = {e_i}. A boundary index gives a set in the *relative interior* of its face.
- **Continuity in measure.** For polytope M the vertices v_k(a) ∝ a⊙m_k move continuously, and the planes {v_k(a)·g = 0} are null. This includes limits at vertices and edges.
- **Equivariance.** C_a(g) = T(a⊙g), which is worth stating: the family is the rescaling orbit of T. As the audit says, round 42's results concern rescaling-invariant *rankings* and do not apply to the family as such.
- **Injectivity.** max_{q∈M_a} q_i/q_j = (a_i/a_j)·max_{p∈M} p_i/p_j holds exactly (CHECKED, 300 random polytopes). Boundary indices are also separated, by their face and by their ratios inside it. So a ↦ M_a is injective on the **closed** simplex, and a homeomorphism onto its image there, not only on compact subsets of the interior. D_K determines a closed convex K, so the models are injective too.

### 5.2 The pair-ordering theorem: correct (PROVED; CHECKED)
**All three cases check.**
- Silence → answer: the k-sandwich with k ≥ 0.
- Answer → silence: k > 0.
- Opposite answers: the first case applied to the newly accepted answer. The old model cannot accept both h and −h.

**Null and empty cases.** Coordinate-zero problems are null. W and R are never empty, which the proof should say:
- silence → answer: C_a not accepting h needs some h_i < 0, and C_b accepting needs some h_i > 0;
- answer → silence: symmetric.

**CHECKED (`posterior_pairs.py`, ALL PASS).** The inequality holds on every disagreement in:
- 21,076 disagreements on T1 (ε = 1/10, 3/10);
- 9,933 on random interior polytopes with n = 3;
- 11,064 with n = 4.

All six (C_a, C_b) kinds occur.

**Extension to the boundary (PROVED here; CHECKED on 19,466 boundary disagreements).** Let a, b ∈ Δ be arbitrary. Put r_i = b_i/a_i ∈ [0, ∞], and drop the worlds with a_i = b_i = 0. Then min_W r < max_R r still holds, and both sides are non-empty after dropping.
- The only new cases are infinite r. For example, if max_R r = ∞ = min_W r, then supp a ⊆ R, so C_a cannot accept h in the answer → silence case.
- Where k is forced to 0, supp b ⊆ W, and C_b would accept h.

This settles the **geometric** certificate at the boundary. It does not settle boundary *gates*, where the supporting weights can be boundary weights and D can be infinite. The audit is right to keep that separate.

### 5.3 What the certificate implies (PROVED; NUMERICS)
- **It is a coboundary.** D^{ab} = log a − log b. Within any triple that passes the closed triangle test with common constants, the type vectors built as in PP45 Lemma 2.1 satisfy D^{ab} + D^{bc} + D^{ca} = 0, since constants and weights cancel. That is a necessary triple-level type condition under (R) (Thm R1), and under (R0) given strict CG2 (PP47 Thm 4.1(a)).
  - The posterior certificate meets it, and the analogous family-level condition, automatically.
  - **Consequence:** the order data of this family cannot obstruct global prices. BRIEF52's "feasible on triples, infeasible globally" must come from the *magnitudes* of the pair intervals.
  - This agrees with the audit's warning against installing a_i/b_i as constants, and sharpens it: the orders already admit global prices, so any non-globality has to be engineered in the magnitudes.
- **The orders are nearly rigid (NUMERICS, `posterior_orders.py`).** I sampled 4,000 problems per pair.
  - In 232 of 293 pairs with distinct ratios, the order of log(a/b) is the *only* admissible strict order.
  - The others admit 2–3 orders, probably because patterns were missed in sampling.
  - So the freedom left to fields is in the values of D within one order cone, not in the order.

### 5.4 The audit's other cautions
- I agree on PP47 Prop 2.6(b) and Cor 3.3 (see §4.2, which adds a bounded counterexample).
- I agree on Thm 4.1 (§4.6).
- "A global witness is allowed as an intermediate construction" is fair. But the tripod and the star are more than witnessed: they are single-field Bayes selections (§§2.6, 3.6).

---

## 6. Scripts (`r9/PP54_py/`)

Run each with `python3 -I -B <script> > <script>.out` inside the folder.

| Script | Content | Label | Result |
|---|---|---|---|
| `tripod_indep.py` | PP45 Thm 5.1 re-implemented from credal-set vertices: threshold rule, own Bayes with margin, strict CG2 with constants 1/μ, single-field realisation U, switch continuity; 110,240 checks | CHECKED | ALL PASS |
| `posterior_pairs.py` | pair theorem: interior pairs (T1, random polytopes, n = 3, 4), boundary pairs, injectivity identity | CHECKED | ALL PASS |
| `posterior_orders.py` | admissible strict orders per posterior pair | NUMERICS | §5.3 |
| `pair_criterion_indep.py` | A0 exact equivalence (120,000), box graph and maximal cliques, Cor 3.3 retreat loophole at the order level | CHECKED | ALL PASS |
| `rerun/` | copies of all PP45/PP46/PP47 scripts, re-run; `runall.log` | — | see below |

**Re-run status** (all outputs byte-identical to the stored `.out` files):
- **PP45:** `types_exact`, `pair_obstruction_exact` and `tripod_exact` are CHECKED, ALL PASS. `forbidden_triangle_mc`, `tripod_repairs_mc` and `edge_types_mc` are NUMERICS, identical.
- **PP47:** `geom47`, `fullcut47` and `tc_r0_47`, ALL PASS.
- **PP46:** `geometry_check` and `pair_criterion` are CHECKED, ALL PASS. `star_check` (NUMERICS) ends ALL PASS (sections 1–4) and reproduces the degenerate intervals and the §6.3 discount certificate. `repairs` and `fan_types` are NUMERICS, identical. Run times: `star_check` 670 s, `repairs` 1,303 s, `fan_types` 455 s.
- **Log.** The first two PP45 entries in `runall.log` (exit 1) are the missing `../PP42_py` path. After symlinking, both were re-run by hand and match.
