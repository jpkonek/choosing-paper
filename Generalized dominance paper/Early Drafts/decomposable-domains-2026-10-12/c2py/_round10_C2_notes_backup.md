# C2: a faithful discretisation of CF(T1), and the impossibility it led to (14 Oct 2026)

Construction side, round 10. Scripts and outputs: `c2py/`. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
Terminology as in TERMFIX_RULES (decomposable domain, advice range, U-domain). Notation as in the write-up
(*The Contamination Triangle*, §§2–5): T1 = (1−ε)u + εΔ, κ = (1+2ε)/(1−ε), p* = u (WLOG, Prop. reduction (d)),
facet data x ∈ {x₊, x₋}, x + 1/x = κ + 1, PC vectors c_k(h) (§4.6), h_k(τ) = (1−τ)r₀ + τr₁ on F_k.
For a world b with failing pair (a,b) and third index c: crossings w′ ∈ F_a, w ∈ F_c, chord λ_b = line(u,e_b),
tangent lines ℓ′ = w′^⊥, ℓ = w^⊥ from e_b, tangent wedge W_b := {m ∈ Δ : m·w′ ≥ 0, m·w ≥ 0}.

---

## 0. Outcome

**(b), but not by a finite certificate alone.** The discretisation did not produce a solution. Its per-prior
part pointed to one new constraint, and that constraint, pushed through the continuum, gives an impossibility.

**Theorem 5.1 (PROVED here, conditional on the cited inputs listed in §5.3; single author, not yet refereed).**
For ε ∈ {1/20, 1/10, 1/5, 3/10, 1/2, 3/5, 9/10}, and for every ε ∈ (0,1) outside a finite set (possibly empty), T1
has no additive cover with integral penalties on any decomposable domain with (LF). Hence CF(T1) has no solution
that comes from a cover. Every solution comes from a cover at the status of CCIBU, so at that status CF(T1) has no
solution. This settles Conjecture N21/N28 at these statuses.

The chain has six steps.
1. **Lemma 3.1 (no straddling on the positive side of a chord), new.** If c_k(h)·q > 0 for an exact facet gamble h,
   then K_q strictly accepts h or −h, unless K_q is a single point on h^⊥.
2. **Uniformity (Cor. 3.2).** Near a vertex, a non-precise K_q has half-plane charts for every facet gamble of the
   two facets crossing b. There are no cuts at non-precise priors.
3. **Forced precise caps (Thm 4.1).** The failing box then forces K_q to be a singleton on a relative neighbourhood
   of the failing edge near each vertex. So the sector caps of the referee's C1 are not merely allowed, they are
   *required*. By R4 Prop. D the cap map is diagonal-projective, σ_b(q) = ν(W_b q).
4. **Gluing (Lemma 4.2).** At every boundary point of the cap near e_b, σ_b(q) lies on both pencil lines L^a(q) and
   L^c(q), which the PC data fix. Infinitely many such points accumulate at e_b. So two explicit conics in q share
   a component (Bezout).
5. **Pinning (Prop. 4.3, exact algebra).** Only two W_b allow a shared component. One of them violates (R1) next to
   the edge. What remains is **W_b = κ off b and 1 at b**, with the cap bounded by the line through e_b of slope 1/x.
   In blow-up coordinates the apexes of all cut facet gambles lie on that line.
6. **Two caps cannot coexist (Prop. 5.2).** A gamble whose line meets the images of two caps would need its d-line
   to be both (W₁g)^⊥ and (W₂g)^⊥. Since W₁ = diag(1,κ,κ) and W₂ = diag(κ,1,κ) are not proportional, this is
   impossible.

**Finite core and continuum inputs** (as the brief asked, §5.4). The finite core is:
- the two box witnesses A, B and one combination A + λB at each vertex;
- one prior on each crossing chord;
- one double-cap gamble g.

The continuum inputs are:
- (PC) cluster limits at exact facet gambles;
- Hausdorff continuity;
- a.e. goodness of gambles;
- Prop. D (precise regions are projective);
- the arc/Bezout argument on infinitely many interface points.

No finite family of gambles and priors that is blind to these can be inconsistent. §2 explains why the plain
discretisation stays feasible.

**Discretisation results (NUMERICS).**
- DCF(G,F) is exactly necessary (Prop. 1.1, PROVED).
- Generic instances are feasible at ε = 0.3 and 0.6.
- DCF+ (adding the facet-pencil constraints) is feasible at ε = 0.3 and 0.6 (δ* = 0.0053, 0.0032; cells and charts re-verified).
  The solutions exploit the finite τ-grid and are wildly discontinuous, so they are artefacts and not constructions.
- The per-prior pencil MILP CHECKS several facts:
  - C1's identity sector, φ_max = 0.125 at ε = 0.3 and 0.025 at ε = 0.6;
  - the referee's N1;
  - the new chord statement (Cor. 3.3): on λ_b, K_q ⊂ W_b and touches both ℓ′ and ℓ. **It does not poke beyond
    them.** This corrects the write-up's §5.3 description.

---

## 1. The discretisation

**Definition 1 (DCF(G,F)).** Fix a finite set of interior priors G ∋ u and a finite family F of mixed gambles. The
unknowns are a cell z(q,g) ∈ {+,0,−} for q ∈ G, g ∈ F. The requirements are as follows.
- **(CH)** For each g, the column z(·,g) is the cell pattern of max{0, c·q, c′·q} for some c, c′ with
  sign c_i = sign g_i = −sign c′_i. Once z is fixed this is an LP in (c,c′). It is homogeneous, so margin 1 is
  exact.
- **(DC)** For each q, put Acc(q) = {g : z = +} ∪ {−g : z = −}. There is a credal set K with P_K > 0 on Acc(q) and
  P_K ≤ 0 on the rejected members of ±F.
- **(TP)** z(u,·) is the pattern of T1.

**Proposition 1.1 (PROVED).**
- (a) (DC) holds iff C(q) := {m ∈ Δ : m·a > 0 ∀a ∈ Acc(q)} ≠ ∅ and C(q) ∩ {m·h ≤ 0} ≠ ∅ for every rejected h.
- (b) Equivalently, Acc(q) satisfies the q-independent Horn clauses "S ⇒ h": no rejected h lies in
  posi(S) + ℝ³_{≥0}, for S ⊆ Acc(q). It also contains no S with 0 ∈ posi(S) + ℝ³_{≥0} (no sure loss). Minimal S have
  |S| ≤ 3 (Carathéodory in ℝ³).
- (c) **Faithfulness.** If CF(T1) has a solution and every g ∈ F is good (its CF chart holds at every q), then DCF(G,F)
  is feasible for every G. A.e. g is good, so for every nominal F₀ and η > 0 there is a feasible F within η of F₀.
  Infeasibility for *all* η-perturbations of F₀ therefore proves that CF(T1) has no solution.

*Proof.*
- (a) Take K = conv of one witness per rejected h. It lies in the open convex set C(q).
- (b) Farkas on cl C(q). Strictness holds because rejected gambles are mixed.
- (c) Restrict K_q and the chart data to G × F. ∎

**Witness form (used in the code).** Each prior gets one witness point per rejection requirement. All witnesses
satisfy every acceptance, with a common margin δ that is maximised. The problem is feasible iff δ* > 0. This form is
exact and imposes no shape on K_q (`dcfplus.py`). The lazy Horn-clause form (`dcf.py`, `horn.py`) is equivalent but
converges slowly: 116 905 clauses with |S| ≤ 2 for 66 gambles; ~1 600 lazily generated clauses after 18 rounds.

**DCF+ (`dcfplus.py`).** This adds per prior the facet-pencil constraints below, for facet gambles h_k(τ) on a τ-grid
refined around the chord root τ*_k(q).
- **(R1)** If c_k(h)·q < 0, some witness has m·h ≤ 0 (writeup Lemma R1, relaxed to ≤).
- **(C)** If c_k(h)·q > 0, all witnesses lie on one closed side of h^⊥ (the weak form of Lemma 3.1).

Every constraint is necessary for a cover with data x. There are three artefacts:
- the vertex margin dv = 10⁻³ (vertex-freeness is an open condition in the continuum);
- the bound |c|, |c′| ≤ 10³;
- the finite τ-grid.

**What a finite system cannot see.** Hausdorff continuity is not encoded: no modulus is known, and imposing one would
be an added assumption. Nor are the limit statements:
- (PC) cluster uniqueness at exact facet gambles, which are a null set;
- Prop. D;
- accumulation at vertices.

§§3–5 show that the obstruction lives exactly there.

## 2. Computations (NUMERICS unless stated)

| run | ε | size | result |
|---|---|---|---|
| lazy Horn DCF (`run2.py`) | 0.3, 0.6 | 60 gambles × 14 priors | every round feasible. Still adding ~100 clauses per round after 13/18 rounds (stopped) |
| witness DCF, no pencil (`run_plus.py … nopencil`) | 0.3 | 36 × 16 | feasible, δ* = 0.0080 |
| DCF+ (`run_plus.py`) | 0.3 | 36 × 16; 6 304 vars, 162 088 rows | feasible, δ* = 0.0053 |
| DCF+ | 0.6 | 36 × 16 | feasible, δ* = 0.0032 (0 cell mismatches, 36/36 charts, 1 188 fine-grid violations: the same artefact) |

Independent check of the ε = 0.3 DCF+ solution (`verify_plus.py`, `verify_plus_e03.out`):
- 0 cell mismatches when P_{K_q}(±g) is recomputed from the witness hulls;
- 36/36 charts realisable from scratch;
- **658 violations of (R1)/(C) on a 2 000-point τ-grid.**

So the solution lives in the gaps of the τ-grid. Its K_q are far from T1 next to u (Hausdorff distance up to 1.1 on
the ring of radius 0.04) and have no continuity. **Reading:** finite unstructured systems are feasible, and their
"solutions" carry no structure that could become an exact family. This is the expected failure mode.

**Per-prior pencil MILP (`pencil.py`, `pencil_tests.py`, CHECKED; `pencil_tests_eps03.out`).** For a single prior, is
there a vertex-free K satisfying (R1) and (C) for all three facets?
- On λ_b at t ∈ {.02, .1, .3, .6, .9}:
  - an admissible K exists;
  - none pokes beyond ℓ′ or ℓ by 10⁻³t (infeasible);
  - no precise K exists.
- On arcs around e_b (ρ = .05, .01):
  - precise K exists only for φ < ½, on the failing side (the referee's N1);
  - the identity is admissible exactly for φ ≤ 0.125 (C1: 0.127).

(The first run of this script had a big-M sign bug and a vertex-tolerance problem; both are fixed. The outputs
quoted are from the corrected code.)

## 3. No straddling on the positive side of a chord

Standing hypotheses for §§3–5: a strictly guiding additive ranking with integral penalties covers T1 on a
decomposable domain with (LF), and K_q are its interior Bayes credal sets. So (Cor. TSalways):
- (TS), (PC) and (NS) hold, with x ∈ {x₊, x₋};
- K_q → {e_b} at the vertices;
- edge confinement holds;
- the charts are those of CF(T1) for a.e. g, at every q (Prop. CF ⇒).

Nothing else is assumed.

**Lemma 3.1 (PROVED).** Let h ∈ relint F_k and q ∈ int Δ with c_k(h)·q > 0. Then P(q,h) > 0, or P(q,−h) > 0, or K_q
is a singleton contained in h^⊥.

*Proof.*
1. **The CF cells.** For good g, the cell {c·q > 0} misses the silence wedge {c ≤ 0, c′ ≤ 0}. So every q with
   c(g)·q > 0 lies in A(g) ∪ A(−g) ∪ {c = c′ > 0}. On the d-ray, P(q,±g) = 0 by continuity, since q lies in the
   closure of both open cells.
2. **Straddling gambles near h.** Suppose the conclusion fails. Then K_q is not a singleton and meets both closed
   sides of h^⊥. The set of g with min_K m·g < 0 < max_K m·g is open. It has points arbitrarily close to h:
   - h itself, if K_q straddles strictly;
   - h ∓ t𝟙, if K_q touches h^⊥ from one side;
   - h + tn, with n separating two points of K_q, if K_q ⊂ h^⊥.
3. **The chart of such a g.** For a good g in that set, P(q,g) < 0 and P(q,−g) < 0. By step 1, c(g)·q ≤ 0.
4. **The PC limit.** Take good g_m → h in the set. By (PC) (Thm TS, every cluster line of h is the PC line with
   its positive side), c(g_m)/|c(g_m)| → c_k(h)/|c_k(h)|. Hence c(g_m)·q > 0 for large m, a contradiction. ∎

Fix q and a facet k. Put χ_q(τ) := c_k(h_k(τ))·q. It is affine in τ, with root τ*_k(q) (which exists unless q = u).
Put I⁺ := {χ_q > 0} ∩ (0,1), Φ(τ) := P(q,h(τ)) and Ψ(τ) := P(q,−h(τ)).

**Corollary 3.2 (uniformity; PROVED).** If K_q is not a singleton, then either Φ > 0 on all of I⁺ or Ψ > 0 on all
of I⁺.

*Proof.* {Φ > 0} and {Ψ > 0} are disjoint (Φ + Ψ ≤ 0) and open, and by Lemma 3.1 they cover the interval I⁺. ∎

Near e_b the first alternative holds, for k ∈ {a,c}. Some τ₁ has h(τ₁)_b > 0. Then:
- χ_q(τ₁) → λ_{bk} h(τ₁)_b > 0 (crossing rows, Prop. boxbridge (a));
- Φ_q(τ₁) → h(τ₁)_b > 0 (K_q → {e_b}).

Hence, near e_b:
- **a non-precise prior is never cut by a facet gamble of F_a or F_c;**
- **K_q touches the pencil line L^k(q) := {m : m·H_k(q) = 0}**, where H_k(q) := (c_k(r₁)·q) r₀ − (c_k(r₀)·q) r₁
  ∝ h_k(τ*_k(q)). Indeed Φ > 0 on I⁺, and Φ ≤ 0 on I⁻ by N21.1′, so Φ(τ*) = 0.

**Corollary 3.3 (chord; PROVED).** For q ∈ λ_b ∩ int Δ, q ≠ u: K_q ⊂ W_b, P(q,w′) = P(q,w) = 0, and K_q meets ℓ′
and ℓ at points other than e_b.

*Proof.*
1. On λ_b, χ for F_a vanishes at τ_b with nonzero slope. A strict straddle of ℓ′ would persist to τ ∈ I⁺ near τ_b,
   which Lemma 3.1 forbids (q ∉ ℓ′'s singleton case, Prop. vertexfree (iv)). So K_q lies on one closed side of ℓ′,
   and likewise of ℓ.
2. N21.1′ gives P(q,w′), P(q,w) ≤ 0.
3. Every other combination of sides puts e_b ∈ K_q, by Fact 4.0, against Prop. vertexfree (i). ∎

This corrects the write-up's §5.3 bullet "poking strictly beyond ℓ … beyond both ℓ and ℓ′ on the chord". On the chord,
K_q touches the tangent lines and stays inside the tangent wedge. It pokes beyond ℓ′ only off the chord, on the
e_a-side (N28 Remark). CHECKED numerically (§2).

## 4. Forced precise caps and their pinning

WLOG x = x₊ (transposition; `pin_caps.py` also runs x₋). The failing pairs are (a,b) = (1,2), (2,3), (3,1).

**Theorem 4.1 (forced caps; PROVED).** For each b there are s₀ > 0 and a connected open O′_b ⊂ int Δ such that:
- O′_b contains a relative neighbourhood of every edge prior q₀(s) = (1−s)e_b + s e_a, for 0 < s < s₀;
- K_q is a singleton for every q ∈ O′_b.

*Proof.*
1. **Witnesses.** For small s there are box witnesses A ∈ relint F_a and B ∈ relint F_c with
   c_a(A)·q₀ > 0 < c_c(B)·q₀ and A_b B_a < |A_a||B_b|. This is the write-up's Prop. T1 computation, valid
   because x² > κ.
2. **A non-precise prior near q₀ would accept both.** The positivities persist near q₀. For a non-precise q close to
   e_b, Cor. 3.2 gives P(q,A) > 0 and P(q,B) > 0, since τ_A ∈ I⁺_a(q) and τ_B ∈ I⁺_c(q).
3. **Contradiction with the edge.** Then P(q, A+λB) > 0, where A + λB < 0 in coordinates a and b. But K_q is close to
   the edge [e_a,e_b] (edge confinement), where m·(A+λB) < 0.
4. **Connectedness.** Let O′_b be the union of these neighbourhoods; it is connected. ∎

Let O_b be the component of int{q : K_q singleton} containing O′_b.
- By R4 Prop. D (CHECKED), σ_b := the point of K_q is constant or σ_b(q) = ν(W_b q) on O_b, with W_b positive
  diagonal.
- A constant map is excluded: it would have to be e_b, against Prop. vertexfree (i).

**Lemma 4.2 (gluing; PROVED).** Every q ∈ ∂O_b ∩ int Δ close to e_b satisfies Q^a(q) = 0 and Q^c(q) = 0, where
Q^k(q) := (W_b q)·H_k(q). Such points exist at every small distance r from e_b, inside the sector between the failing
edge and λ_b.

*Proof.*
1. **Boundary points are limits of non-precise priors.** Otherwise a precise neighbourhood would join O_b.
2. **Touching passes to the limit.** Non-precise priors near e_b touch L^a(q) and L^c(q) (after Cor. 3.2).
   Hausdorff continuity carries the touching points to the singleton σ_b(q), and H_k is continuous.
3. **Arc argument.** The arc of radius r from the failing edge (which is in O′_b) to λ_b (whose points are
   non-precise, Prop. vertexfree (iv)) crosses ∂O_b. ∎

**Proposition 4.3 (pinning; PROVED by exact algebra, CHECKED numerically).** Infinitely many common zeros accumulate at
e_b, so by Bezout the conics {Q^a = 0} and {Q^c = 0} (both through e_b; neither form vanishes identically for any w > 0: if one did, R ≡ 0 and w would lie in the solution set of (I) below, at which both forms are nonzero — `pin_symbolic.out`) share a
component through e_b. With w_b = 1 there are exactly two possibilities.
- **(I) The conics coincide.** Then (w_a, w_b, w_c) = (x₊, 1, 1/x₊).
- **(II) A common line.** Then (w_a, w_b, w_c) = (κ, 1, κ), and the common line through e_b has direction
  d_c/d_a = 1/x₊ (for both data x₊ and x₋, with a the failing index).

Evidence for the classification:
- Gröbner bases over ℚ(x) (`pin_general.py`): (I) is {w_a − x²w_c, w_c(xw_c − 1)}. (II) is the ideal generated by
  (r−1)(rx−1) together with two linear relations; the branch r = 1 forces w = 0.
- Exact sympy solves at ε ∈ {1/20, 1/10, 1/5, 3/10, 1/2, 3/5, 9/10}, all three vertices, x₊ and x₋, confirm this
  (`glue_conics*.out`, `pin_caps_eps0*.out`).
- Multistart numerics find nothing else.

**Excluding (I).** On the failing edge, F := Q^c vanishes identically and ∂F/∂η ≠ 0 with the violating sign
(`edge_check.out`). So every interior point of the cap next to the edge violates (R1) for pencil c. The exact τ-test
in `cap_R1.py` gives 0 admissible directions out of 120, at ρ = 10⁻², 10⁻³ and ε = .3, .6. The blow-up margin is
y_c(x²κ − 1)/x > 0 (`pin_symbolic.out`).

**What (II) gives.**
- (II) satisfies (R1) exactly on the sector up to slope 1/x, and fails beyond it (`cap_R1`: φ_max = 0.25 against the
  prediction 0.2534 at ε = .3; 0.135 against 0.1362 at ε = .6).
- In the blow-up, the apexes of the cut facet gambles of both pencils lie on the cap boundary. This is exact:
  κ(−y_a + κy_c) = (κ/x)(y_c − y_a) ⟺ y_c/y_a = 1/x, and the same for pencil c.

So **the vertex structure of any cover is forced:**
- σ_b = ν(W_b ·), with W_b = κ off b and 1 at b, on a cap bounded near e_b by the line of slope 1/x;
- non-precise K_q touching both pencil lines beyond it;
- inside W_b on λ_b.

## 5. The contradiction

**Proposition 5.2 (PROVED).** Two open precise regions O, O′ with σ = ν(W·) and σ′ = ν(W′·), W and W′ not proportional,
cannot both exist.

*Proof.*
1. **Choose g.** Let I = σ(O) and I′ = σ′(O′). The set of g whose line g^⊥ meets both I and I′ is open and nonempty,
   so it contains good, mixed g with all g_i ≠ 0.
2. **The d-line through O.** On O, A(g) = {(Wg)·q > 0}. The segment S = {(Wg)·q = 0} ∩ O lies in
   cl A(g) ∩ cl A(−g) ⊂ {c = c′ ≥ 0} ⊂ {d·q = 0}. So the d-line of g is {(Wg)·q = 0}, i.e. d ∝ Wg.
3. **The d-line through O′.** Likewise d ∝ W′g.
4. **Conclusion.** Wg ∥ W′g with W′W⁻¹ having distinct diagonal entries forces g onto a coordinate axis. ∎

**Theorem 5.1 (PROVED, at the status of §5.3).** Apply Prop. 5.2 to O₁ and O₂. By Prop. 4.3, W₁ = diag(1,κ,κ) and
W₂ = diag(κ,1,κ), and W₂W₁⁻¹ = diag(κ, 1/κ, 1) has distinct entries since κ > 1.

`two_caps.py`: over 2 000 double-cap gambles, the angle between W₁g and W₂g is ≥ 0.03° (ε = .3) and ≥ 0.12°
(ε = .6). It is nonzero, as it must be.

**5.3 Inputs and their status.**

| input | status |
|---|---|
| Prop. CF (⇒), Prop. necessary, reduction | proved; once refereed with repair |
| Thm TSalways ⇒ (TS), (PC) clusters near Σ, (NS), x ∈ {x±}; Cor. TSalways (c) | one referee |
| crossing rows (Prop. boxbridge (a)); box witnesses (Prop. T1) | refereed |
| N21.1′ (A_τ ⊆ H⁺_τ) | refereed once. Lemma R1 is *not* needed |
| Prop. vertexfree (i), (iv); Fact 4.0 | one referee |
| R4 Prop. D (precise regions are diagonal-projective) | CHECKED (local fundamental theorem of projective geometry). **The weakest link.** |
| Lemma 3.1, Cor. 3.2, 3.3, Thm 4.1, Lemma 4.2, Prop. 5.2 | PROVED here, unrefereed |
| Prop. 4.3 | exact algebra: Gröbner over ℚ(x) (generic ε) plus exact solves at 7 values of ε. Uniqueness at finitely many exceptional ε is not checked |

No regularity is assumed: no smoothness, no continuity of chart data, no linear scaling at the vertices. The blow-up
(linear-scaling) computations in §4 are used only as corroboration. Steps 4–5 use the exact conics.

**5.4 The finite core.** At one vertex pair (b, b′) the following finite system is jointly inconsistent:
- box witnesses A, B and A + λB near q₀(s);
- one point of λ_b on each small arc;
- one double-cap gamble g.

This holds *given* three continuum facts:
- (i) the PC cluster limit at the exact facet gambles A, B and h(τ₁);
- (ii) Prop. D on the cap;
- (iii) infinitely many interface points (Hausdorff continuity and connectedness), needed for Bezout.

Without (iii) the cap map is not pinned. Without (i), Lemma 3.1 fails. This is why DCF, which sees only finitely many
good gambles and no continuity, stays feasible.

## 6. Effect on the write-up, and what a referee should check

- §5.3 "Where a solution of CF(T1) would have to live" is superseded.
  - C1's identity caps are *forced to be* caps, but with W_b = κ-diag, not the identity. So C1 itself is not part of
    any cover.
  - The chord layer lies inside the tangent wedge (Cor. 3.3).
- Conjecture N21 becomes Theorem 5.1, at the status above. Corollary: no additive cover of T1 on any (LF)
  decomposable domain (integral penalties). The charge version needs the existence proviso, as in Cor. charges.
- A referee should check, in order:
  1. Lemma 3.1, step 4: cluster convergence of the *c*-vectors on general domains, which Thm TS states for h near Σ;
  2. Prop. D (re-derive it; the diagonal step uses the strict signs of d);
  3. Lemma 4.2 (the limit of touching points; that the arc crossing lies near e_b);
  4. the exclusion of (I) (the orientation of the violating sign);
  5. Prop. 5.2.
- Possible generalisation (CONJECTURE): the same chain should work for every all-facing triangle in general position.
  The pinning algebra would then use the R15 pinched ratios.

## 7. Files (`c2py/`)

`dcf.py`, `horn.py`, `families.py`, `run1.py`, `run2.py`, `count.py` (lazy Horn DCF); `dcfplus.py`, `run_plus.py`,
`verify_plus.py` (witness DCF / DCF+); `pencil.py`, `pencil_tests.py` (per-prior MILP); `glue_conics.py`,
`pin_caps.py`, `pin_general.py`, `pin_symbolic.py`, `edge_check.py`, `cap_R1.py`, `two_caps.py` (§§4–5);
outputs `*.out`, `plus_e03.pkl`.
