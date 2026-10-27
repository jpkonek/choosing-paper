# Referee report on C2_notes.md and C1_notes.md (round 10, 14 Oct 2026)

Independent adversarial referee. I read BRIEF9.md and the write-up (*The Contamination Triangle.tex*, cited WU) §§2–5,
then C2_notes.md, C1_notes.md, and N28_referee.md where it matters.
- Reran: c2py/pin_symbolic, pin_general, edge_check, two_caps, glue_conics (ε = 3/10), cap_R1 (0.3), pencil_tests (0.3),
  and c1py/thmA_cap_geometry, gauge_layer. All outputs reproduce. cap_R1_eps03.out is a truncated copy of the full
  run (2 of 6 vertex/data cases), and the rerun agrees on all 6.
- My own checks are in `c2ref_py/`: conics.py, conicsI.py, elim_allx.py, capsign.py and witnesses.py, each with a `.out`.

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Verdicts: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.
Notation is WU's. Ω = int Δ. A "cover" means a strictly guiding additive ranking with integral penalties on a
decomposable domain with (LF) that covers T1. K_q are its interior Bayes credal sets.

---

## 0. Summary

1. **C2's chain is correct up to two repairs, and with them Theorem 5.1 holds for every ε ∈ (0,1).**
   - **Repair 1 (a gap in C2).** C2 cites R4 Prop D in its unrepaired form. R8 marked "non-constant ⇒ injective" as a
     GAP, and C2 needs exactly that step. I prove it here, from the CF chart structure alone, as Proposition P (§3):
     on a connected open set of precise priors, σ is constant or injective. That closes R4 Prop D's gap for covers.
   - **Repair 2 (Prop 4.3 misdescribes candidate (I)).** The two conics never coincide for w > 0. At
     W = (x,1,1/x) they share the line x²q₁ − (x²+1)q₂ + q₃ = 0 (for b = 2), and that line does **not** pass through
     e_b. The accumulation argument therefore excludes (I) directly, and the Lemma R1 sign test is not needed. That
     test is nevertheless correct, and N21.1′ alone already violates it.
   - **The exceptional set is empty.** I solve the common-line system through e_b by hand for every x > 1. The only
     positive solution is W = (κ,1,κ), with slope r = 1/x. So the exceptional finite set of ε disappears.
2. **C1 Theorem A is CONFIRMED.** One measurability repair is needed in step 5.
3. **C1 Theorem A and C2/I2's forced caps do not conflict. Together they give a second impossibility proof.**
   - C2 Thm 4.1 forces an open precise set O′_b at every vertex.
   - By Prop P, σ is constant or injective on it. The constant case is ruled out by vertexfree (i).
   - Theorem A forbids the injective case.
   - Hence no cover exists, for every ε ∈ (0,1). This route uses no Bezout argument, no conic algebra and no
     Prop 5.2 (§5).
4. **C1 Theorem B is CONFIRMED WITH REPAIR**, but it is now subsumed: no solution from a cover exists at all. Prop P
   also makes P_wild = ∅ and Prop 6.1 unconditional: every open precise region is a wall.
5. **Chord adjudication: C2 is right and the write-up is wrong.**
   - On λ_b (minus p*), K_q ⊆ W_b, and it touches both ℓ′ and ℓ.
   - The write-up's "on the chord beyond both ℓ and ℓ′" comes from a summary bullet in N28_referee (§4 end), not from
     any NUMERICS. Prop vertexfree (iii) gives only weak inequalities on the chord.
   - The strict poking holds only on the open sides of λ_b (Lemma R1).

**Net statement established (§6, Theorem R).** For every ε ∈ (0,1), T1 has no additive cover with integral
penalties on any decomposable domain with (LF), at any interior target prior. Hence CF(T1) has no solution that
comes from a cover. At the status of CCIBU (Prop CF ⇐), CF(T1) has no solution, i.e. WU Conjecture N21 holds at that
status. This rests on once-refereed inputs; see the dependency list in §6.

---

## 1. C2, §3: no straddling on the positive side

### Lemma 3.1 — CONFIRMED (PROVED)

All four steps re-derived.

**Step 1.** For good g, CF holds at **every** q (Prop CF ⇒, via the equality of open convex sets that agree a.e.).
Near Σ the advice range contains 0 by (LF), so the chart vector c is the genuine penalty vector. Then c·q > 0 puts q
in exactly one of three places:
- in R(g), if d > 0;
- in R(−g), if d < 0, since then c′ = c − d > c > 0;
- on the d-face, if d = 0, where P(q,±g) = 0 by continuity and P(q,g) + P(q,−g) ≤ 0.

**Step 2.** The three straddling witnesses (h, h ∓ t𝟙, h + tn) are correct. The straddling set S is open, so S has
positive measure in every ball around h.

**Step 4 (the brief's priority: c-vector cluster convergence on general domains).** Take good g_m → h, chosen in the
cone over int N₀, which is possible because S is open. Lemma B1 / raytransfer (c) give R(g_m) ∩ B₁ =
{c(g_m)·q > 0} ∩ B₁. Then:
- Every limit c∞ of c(g_m)/|c(g_m)| in ℝ³ defines an affine function on aff Δ whose zero line meets B₁. Otherwise
  P(·,h) would be one-signed on B₁, against the pivot structure of Thm TS.
- By the cluster clause of (PC) near Σ (Thm TS / TSalways), that line is λ_τ, with its orientation.
- An affine function on aff Δ determines its vector in ℝ³, so c∞ = c_k(h)/|c_k(h)|.

So c(g_m)·q → (positive)·c_k(h)·q > 0 at **every** q ∈ Ω, not only on B₁. Homogeneity (P(q,th) = tP(q,h)) handles
any h ∈ relint F_k off Σ.

### Corollary 3.2 and the "first alternative near e_b" — CONFIRMED (PROVED)

{Φ > 0} and {Ψ > 0} are disjoint open subsets of the interval I⁺ and, by Lemma 3.1, they cover it.

Near e_b, take τ₁ with h(τ₁)_b > 0. The crossing row (Prop boxbridge (a)) gives χ_q(τ₁) → λ_{bk}h(τ₁)_b > 0, and
K_q → {e_b} gives Φ_q(τ₁) → h(τ₁)_b > 0. So the alternative Φ > 0 holds on a fixed neighbourhood V of e_b, for
k ∈ {a,c}.

Touching: Φ ≤ 0 on I⁻ by N21.1′, so Φ(τ*) = 0. Here τ*(q) → τ_b ∈ (0,1).

### Corollary 3.3 (chord) — CONFIRMED (PROVED)

It holds on the whole λ_b ∩ Ω minus p*, on both sides of p*.

- Strict straddle of ℓ′ persists to I⁺ and is excluded by Lemma 3.1, since the singleton case is excluded by
  vertexfree (iv).
- N21.1′ gives P(q,w′), P(q,w) ≤ 0.
- Fact 4.0 and vertexfree (i) exclude the other side combinations.

**Adjudication against N28_referee.** The write-up's §5.3 sentence "on the chord beyond both ℓ and ℓ′" is **WRONG**.
- On the chord, K_q ⊆ W_b and it touches both ℓ′ and ℓ.
- N28_referee's NUMERICS (C1, N1) concern precise priors off the chord and contain no test of the chord claim. The
  sentence is N28_referee's summary bullet, which over-read vertexfree (iii): (iii) has only "≤" on the chord.
- What survives is the strict version on the open e_a- and e_c-sides (Lemma R1).
- C2's per-prior MILP (rerun, identical output) agrees.

---

## 2. C2, §4: the forced cap

### Theorem 4.1 — CONFIRMED (PROVED from the inputs)

**Witnesses.** The Prop T1 witnesses A ∈ relint F_a and B ∈ relint F_c (exact facet gambles, so no a.e. issue) satisfy
c_a(A)·q₀ > 0, c_c(B)·q₀ > 0 and the ratio condition, because x₊² > κ. `witnesses.py` checks membership, both
signs, the ratio, and a nonempty λ-window for A + λB < 0 in coordinates a and b. The check covers
ε ∈ {.01, .05, .3, .6, .9, .99}. Note that s₀ shrinks as ε → 1 (s ≤ 10⁻⁵ is needed at ε = 0.9).

**Contradiction at a non-precise prior.** For non-precise q in V near q₀(s):
- Cor 3.2 gives P(q,A), P(q,B) > 0, hence P(q,A+λB) > 0 by superadditivity;
- edge confinement (Cor TSalways (c)) gives P(q,A+λB) < 0.

So every prior near q₀(s) is precise.

**Connectedness.** The union of the balls B(q₀(s), r(s)) ∩ Ω is connected. Each ball contains interior points just
above every edge point within r(s) of q₀(s), so the index sets of any two-colouring are open in (0,s₀).

### R4 Prop D as used by C2 — GAP, repaired by Proposition P (§3)

C2 says: "By R4 Prop D (CHECKED), σ_b is constant or ν(W_b·)." In that form Prop D is the unrepaired statement. R8
marked "non-constant ⇒ injective" as a **GAP**, and Consolidated Statements §R4 records the GAP.

C2 needs exactly this case, because nothing in Thm 4.1 makes σ injective. Proposition P below fills the gap. After it,
C2's use of Prop D is legitimate.

The constant case is excluded as C2 says: O′_b accumulates at e_b and K_q → {e_b}, so the constant would be e_b,
against vertexfree (i).

### Lemma 4.2 — CONFIRMED (given Prop P)

The three ingredients all hold:
- **Boundary points are limits of non-precise priors.** Otherwise they would lie in int(precise) ∩ cl O_b ⊆ O_b.
- **The precise set is closed**, since diam K_q is continuous.
- **The limits are the right ones.** σ extends continuously to the boundary as ν(Wq), and the touching points pass to
  the limit.

The arc from the failing edge (in O′_b) to λ_b (non-precise) at radius r < s₀ meets ∂O_b inside the open sector.

### Proposition 4.3 — CONFIRMED WITH REPAIR; the exceptional set is eliminated

My derivation is independent of C2's (`conics.py`). I write H_k(q) = v_k × (C_kᵀq), where c_k(h) = C_k h, so
Q^k(q) = det(Wq, v_k, C_kᵀq). For b = 2 (a = 1, c = 3), W = diag(w_a, 1, w_c) and x > 1:

- **The forms are never proportional.** Q^a has q₁²-coefficient w_a·x(x−1) ≠ 0 and q₃²-coefficient 0. Q^c has
  q₁²-coefficient 0 and q₃²-coefficient w_c·x(x−1) ≠ 0. So no irreducible common component exists. By the real
  Nullstellensatz for real conics with infinitely many points, a common component must be a line. The common zeros
  accumulate at e_b, so that line passes through e_b.
- **Common line through e_b and (1,0,r).** The system is E1–E4 of `conics.out`.
  - The case r = 0 is inconsistent.
  - For r ≠ 0, E1 and E3 are linear in (w_a, w_c), with determinant −r·x(x−1)²(x²+1) ≠ 0. They give
    w_a = (1−r)s/(x−1) and w_c = (1−r)s/(r·x(x−1)), where s = x² − x + 1.
  - Then E2 and E4 both reduce to (r−1)(rx−1)·s = 0 (`elim_allx.out`).
  - Positivity forces 0 < r < 1, hence r = 1/x and w_a = w_c = s/x = κ.

  This is PROVED by hand for **every** x > 1, so for every ε ∈ (0,1). The finite exceptional set of C2's Theorem 5.1
  is empty.
- **Candidate (I), W = (x,1,1/x): WRONG as described.** It is not "the conics coincide". `conicsI.out` gives
  Q^a = (x−1)·q₁·L and Q^c = (x−1)·q₃·L, with L = x²q₁ − (x²+1)q₂ + q₃ and L(e₂) = −(x²+1) ≠ 0. So the common zeros
  near e_b reduce to {e_b}, and (I) is excluded by Lemma 4.2's accumulation argument alone. C2's resultant R ≡ 0
  records that the *second* intersections coincide, not that the conics do.
- **The sign question.** C2's R1 test of (I) has the correct (violating) sign. `capsign.py` finds violations of both
  N21.1′ and Lemma R1 at every sampled direction, for ε ∈ {.05, .3, .6} and ρ ∈ {10⁻², 10⁻³}. So the one-reader Lemma
  R1 is not needed, and in fact no sign test is needed at all.
- **W_II passes** both conditions on a sector next to the failing edge, consistent with cap_R1.
- **Other vertices and data.** The other vertices follow by cyclic symmetry and x₋ by the transposition (1 2).

The status table's line "Lemma R1 is not needed" is therefore true, but it was contradicted by C2's own exclusion of
(I). That exclusion is now unnecessary.

## 3. Proposition P (new; PROVED here) — precise regions are constant or injective

**Statement.** In every cover, let O ⊆ Ω be open and connected with K_q = {σ(q)} on O. Then σ is constant on O or
injective on O. If it is injective, σ = ν(w⊙·) with w > 0, by Lemma 5.0 of C1, i.e. R4 Prop D in its injective case
as repaired by R8, using the classical local fundamental theorem of projective geometry (CHECKED, classical).

**Proof.** Only CF charts at every q (Prop CF ⇒) and continuity of σ are used.

**(a) Sign identity.** For a.e. g, the silence wedge {c ≤ 0, c′ ≤ 0} has interior disjoint from O. If a ball B_j ⊆ O
lies in it, then σ·g ≡ 0 on B_j, so g ∈ (span σ(B_j))^⊥. That is a null set of g, and a countable base suffices.
- If the wedge is non-degenerate (or a strip), it misses O entirely.
- If it is degenerate (c′ = −μc), it equals the d-line.

So for a.e. g and **every** q ∈ O: sign(σ(q)·g) = sign(d_g·q).

**(b) Segments go to segments, monotonically.** Let q, q′ ∈ O with [q,q′] ⊆ O, and let r ∈ [q,q′]. For a.e.
g ∈ G₊ := {g : σ(q)·g > 0, σ(q′)·g > 0}, (a) gives d_g·q, d_g·q′ > 0, hence d_g·r > 0, hence σ(r)·g > 0. By
continuity σ(r)·g ≥ 0 on cl G₊ = cone(σ(q),σ(q′))*. So σ(r) ∈ [σ(q), σ(q′)]. If σ(q) = σ(q′), (a) applied directly
to d_g gives σ ≡ σ(q) on [q,q′] ∩ O even when the segment leaves O.

**(c) No one-dimensional pieces.** Let U ⊆ O be open and connected, with σ(U) = J inside a line Λ and σ not constant
on U.
- For good g with g^⊥ ∩ Λ = {m} ⊂ relint J, σ·g changes sign on U, so the zero set of σ·g in U is L_g ∩ U ≠ ∅, by
  (a).
- That zero set is σ^{-1}(m) ∩ U, so L_g depends only on m.
- By Fubini along the submersion g ↦ m, for a.e. m ∈ relint J, a.e. g in the plane m^⊥ is good.
- For m ∈ Δ not a vertex, m^⊥ contains open cones of two sign classes not related by ±, while d_g ∥ d_{g′} forces
  sign g = ±sign g′. This is a contradiction.

This is C1's Lemma 4.5 argument with the regularity removed.

**(d) Non-injective implies locally constant.** If σ(q₁) = σ(q₂) = m, then by (b) σ ≡ m on a segment C′ inside a ball
B ⊆ O around q₁. For q₃ ∈ B, (b) applied to segments parallel to C′ maps the triangle co(C′, q₃) into [m, σ(q₃)]. If
σ(q₃) ≠ m, the interior of the triangle contradicts (c). So σ ≡ m on B.

**(e) Locally constant implies constant.** The set E where σ is locally constant is open. It is also closed in O: if
q₀ ∈ cl E, take a convex ball B around q₀ and a plateau ball inside B, and apply (d)'s triangle argument to every point
of B. Since O is connected, E = O and σ is constant. ∎

**Consequences.**
- R4 Prop D's GAP is closed for covers, and for CF solutions in general: (a)–(e) use only the CF form.
- In C1, P_wild = ∅, and Prop 5.2, Cor A′ and Prop 6.1 hold without (LD) or C¹ hypotheses: every open precise region
  is a wall.

## 4. C2, §5 and the remaining claims

**Prop 5.2 — CONFIRMED (PROVED, given Prop P).**
- Images of injective σ are open (invariance of domain), so the set of good mixed g whose line g^⊥ meets both
  images is open and nonempty.
- On O, S = {q·Wg = 0} ∩ O is a nondegenerate segment lying in cl R(g) ∩ cl R(−g) ⊆ {c = c′ ≥ 0}. So d_g = λWg with
  λ > 0.
- Likewise d_g = λ′W′g. Then W′W^{-1} has an eigenvector Wg off the coordinate axes, which is impossible for generic g
  unless W ∝ W′.
- W₁ = diag(1,κ,κ) and W₂ = diag(κ,1,κ) are not proportional, since κ ≠ 1. `two_caps` reruns identically.

**Theorem 5.1 — CONFIRMED WITH REPAIR, and upgraded to every ε ∈ (0,1)** (Prop P, plus §2's elimination).

**Other claims.**
- **§§1–2 (DCF, DCF+, NUMERICS).** Prop 1.1 (a) and (c) are correct and elementary. I did not re-derive (b)'s
  |S| ≤ 3 claim; nothing depends on it. The reading "finite systems are feasible, artefacts only" is fair.
- **§5.4 "finite core".** This is a heuristic remark, not a theorem. It is harmless.
- **§6 "C1 itself is not part of any cover".** CONFIRMED: the identity is W = I, not (κ,1,κ). C1's Theorem A also
  excludes it.

## 5. C1

**Lemma 2.1 (gauge mixtures split) — CONFIRMED.** By concavity and homogeneity, f(g) + f(−g) ≤ 2f(0) = 0.

**Lemma 2.2 — CHECKED/NUMERICS.** It reproduces. It was not refereed in depth because nothing depends on it.

**Lemmas 4.0–4.5 — CONFIRMED.** Lemma 4.0 uses (I2): WU Thm main together with N14 §3(iv). Lemma 4.1 holds for every
good g, because CF holds at every q.

**Lemma 5.0 — CONFIRMED (CHECKED; classical input).**

**Theorem A — CONFIRMED WITH REPAIR (PROVED).**
- **Step 1.** (I1) holds on the whole chord line λ_b ∩ Ω, on both sides of p*. Vertexfree (iii) and (iv) use only
  (ii) in its weak form (N21.1′), Fact 4.0 and (i), all valid for every q ∉ H⁺_τ. So the chamber decomposition is
  legitimate.
- **Steps 2–4.** CONFIRMED. A line crossing both open chord sides of the chamber cannot exit through [e_b, f] in
  between, so the half-line face J_g, which contains L_g ∩ O, contains y₁ or y₂. `witnesses.out` checks the geometry
  for W_II-cap points.
- **Step 5 (the fibration; the brief's priority). Repair.** "Fubini" needs measurability of G_i and of their images.
  - Replace G_i by G′_i := {g ∈ G* : P(y_i(g), g) = 0 = P(y_i(g), −g)}. This set is Borel, since P is continuous and G*
    is a Borel co-null set of good g. It contains G_i, and on it K_{y_i} ⊆ ℓ_g directly.
  - Φ: g ↦ (y₁, θ) is a submersion, so Φ(G′₁) is analytic, hence measurable, and of positive measure.
  - A measurable set all of whose sections are single points is null, so some y has two directions.

  With this repair the step is valid, and with Lemma 4.3 it gives a precise point on a chord.

**Theorem A against the forced caps (the brief's last question).** Both hold, and together they give an independent
impossibility proof (§6, route B). There is no inconsistency between the notes: C1 excluded the cap as a construction
ingredient, and C2/I2 showed it is compulsory.

**Prop 5.2, Cor 5.3, Cor 5.4 — CONFIRMED.** Superseded by Prop P: P_wild = ∅.

**Theorem B — CONFIRMED WITH REPAIR.** Three repairs:
1. "Good" is not definable from (LD), which is local on compacts. Use "CF chart on int Q_n" (first-order over the
   Q_n-structure) in Step 0. Everything after Step 0 is local to Q, except Prop 6.1, which is now unconditional.
2. Dimensions must be counted on projective classes of g (dim G = 2, dim I = 3).
3. Case k = 1: replace "finitely many intersections" with the correct fact that a definable set of dimension ≤ 1
   contains segments on only finitely many lines. Hence ⋃ O_L has interior.

Theorem B is now strictly weaker than Theorem R. **§7 (wild solutions, Cantor fans)** is moot.

## 6. Exact statements established

**Theorem R (PROVED, at the status of the inputs below).** For every ε ∈ (0,1) and every interior target prior, no
strictly guiding additive ranking with integral penalties on a decomposable domain with (LF) covers T1. The same holds
for bounded-charge penalties, provided the interior minimisers exist (as in WU Cor charges). Consequently CF(T1) has
no solution that comes from a cover, and, at the status of CCIBU (Prop CF ⇐), no solution at all.

**Route A (C2, repaired).** Lemma 3.1 → Cor 3.2 → Thm 4.1 → Prop P (+ Lemma 5.0) → Lemma 4.2 → Prop 4.3 (hand
elimination, all x > 1) → Prop 5.2.

**Route B (C1 + C2).** Thm 4.1 → Prop P → C1 Theorem A. This route uses no conic algebra and no Bezout argument.

**Dependencies, common to both routes:**
- Prop CF (⇒), with Prop necessary and Prop reduction: once refereed, with repair.
- Thm TS and Thm TSalways, giving (TS), (PC) cluster clause near Σ, (NS) and x ∈ {x±}: one referee each. Cor TSalways
  (c), K_q → {e_b} and edge confinement: one referee.
- Prop boxbridge (a) (crossing rows) and Prop T1 (box witnesses, x₊² > κ): refereed.
- N21.1′ (Lemma quasiconcave): one referee. **Lemma R1 is not used.**
- Prop vertexfree (i) and (iv), with Fact 4.0, Thm apex and Lemma walls (c) (= R4 Thm B): one referee.
- The classical local fundamental theorem of projective geometry: CHECKED.
- Proposition P: PROVED in this report, not yet second-read.

**Route B only:** C1 Theorem A, CONFIRMED here.

**Route A only:** Lemma 4.2, Prop 4.3 and Prop 5.2, all CONFIRMED here.

**Not used anywhere:** CCIBU (except for the CF converse), R4 Prop D's non-injective clause (replaced by Prop P),
regularity, and the finite set of ε.

**Other statements established:**
- **Forced precise collar** (C2 Thm 4.1 = I2 Thm 3). In every cover, at every vertex b, a relative neighbourhood of the
  failing edge near e_b consists of precise priors, σ_b = ν(W_b·) with W_b = κ off b and 1 at b, bounded near e_b by
  the line of slope 1/x. These statements are all vacuous, since no cover exists, but they are the content of the
  proof.
- **Chord structure** (C2 Cor 3.3). This corrects WU §5.3.

## 7. Recommended edits to the write-up

1. §5.3 "Where a solution … would have to live" and Conjecture N21: replace them with Theorem R, its two routes, the
   dependencies above, and Prop P as a new lemma.
2. Prop vertexfree: add "(iii′) on λ_b, K_q ⊆ W_b and touches ℓ′ and ℓ", and delete "beyond both on the chord".
3. Prop 4.3 of C2: describe (I) as a shared line not through e_b, and drop the R1 exclusion.
4. A second reading of Prop P and of C2 Lemma 3.1 / Thm 4.1 should precede any change of status from "one referee".
