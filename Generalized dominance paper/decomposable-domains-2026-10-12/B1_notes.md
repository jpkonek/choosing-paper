# B1. A non-additive cover of T1 on M_U absorbing the corner holonomy: attempt and failure report

15 Oct 2026, round 14 (BRIEF13). Labels: **PROVED** (full proof here), **CHECKED** (verified, proof sketched or
read off a cited proof), **CONJECTURE**, **NUMERICS** (scripts in `b1py/`, run with `python3 -I`; no proof
depends on them). Standing setting: n = 3, ε ∈ (0,1), K′ = u + s(T1 − u), U = D_{K′}, the U-domain M_U.
Notation as in the write-up, §8.5 "Notation": P_i, E_i(X) = X △ P_i, M (mixed gambles of U), N_+, R_ij = {h ∈ U :
h_i h_j < 0}. New notation:

- **Sign classes.** Q_l := {h ∈ U : h_l has the opposite sign to both other coordinates}, l = 1, 2, 3. So
  Q_1 = (+,−,−) ∪ (−,+,+), Q_2 = (−,+,−) ∪ (+,−,+), Q_3 = (−,−,+) ∪ (+,+,−) (intersected with U).
- Then **R_ij = Q_i ∪ Q_j**, **M = Q_1 ∪ Q_2 ∪ Q_3** (disjoint up to null sets), and for world i the two edge
  regions R_ij, R_ik overlap exactly in the **link class Q_i = R_ij ∩ R_ik**. Each Q_l is non-null: it contains a
  neighbourhood of a corner ray of D_{T1} (r_23 ∈ Q_1, r_31 ∈ Q_2, r_12 ∈ Q_3), and cl D_{T1} ∖ 0 ⊆ U.

---

## 0. Outcome

**No cover was constructed. The global attempt broke at step (2), the design of the world orders, and it broke for
a structural reason that applies to every world separately, before any selection is chosen.**

**Where it broke.** The design asked to keep each world additive (or at least adding up) on comparisons
between subsets of each edge region R_ij, so that all edge results hold, and to put the non-additivity only into
comparisons out of interior selected models, whose error sets cross. It was to keep each link of the cycle the
cover needs and drop the link that closes it. That cannot be done: **a world's comparisons inside its two edge
regions determine all of its comparisons on M**, by transitivity through the link class Q_i. The cycle-closing
comparison is therefore never free. It is re-derived as a finite chain of edge comparisons (Lemma B1.2). Precisely:

- **Theorem B1.3 (PROVED).** Suppose world i is a preorder, satisfies strict (G), and on each of its two edge regions
  R_ij, R_ik has a *leading density*, i.e. a positive integrable ρ such that every ρ-strict improvement inside that
  region is accepted. Then the two densities agree on Q_i up to a factor. The glued density ρ_i is leading for
  **all** comparisons of world i between regular models, and it endorses every such comparison. So world i adds up.
  Additive edge restrictions are the special case.
- **Corollary B1.4 (PROVED at the status of Theorem M0closed(b)).** In every ranking on M_U with strict (G), (IB),
  (LA), (S), (C) and T1 ∈ C_L, some world i has an edge region R_ij on which it has no leading density.
- **Corollary B1.5 (PROVED).** Both concrete mechanisms of the brief collapse:
  - "additive base ψ plus extra or reversed interior comparisons, keeping the edges": every extra comparison is
    already decided by ψ, and every reversal closes a strict cycle Y ≺_i Y;
  - "min/max of several additive scores that agree on edge regions but differ on interior crossing sets": such
    scores coincide on all of M.

**The single obstruction revealed: transitivity through the link class.** In three worlds each world sees M as two
overlapping two-world regions. Once a world's exchange rates are a potential on each region, they are a potential
on M. So the holonomy of the corner cycle (§1) cannot be absorbed by interior comparisons alone. It can only be
absorbed at a world whose order on a **single edge region** R_ij has no leading density: an incomplete or otherwise
non-Archimedean two-world comparison structure on R_ij. That is the object of the open two-world core (§8.5(f) of
the write-up), now required *inside the edge restriction of a world*, not only in its interior comparisons. No such
world is known in a full system for any target. I did not find one, so steps (3)–(4) were not reached.

**Correction to the brief.** The brief says that nothing constrains a world's comparisons out of interior selected
models. That is true of the edge *theorems*, which do not force edge additivity. It is false for any *design* that
makes the edges tame: tame edges constrain the interior completely.

Scripts: `b1py/transfer_chain.py` (exact check of the chain of Lemma B1.2 on 4000 random atomless-cell instances,
half of them with no room in the link class), `b1py/t1_chain.py` (the chain on a sampled T1 instance between a
coherent model and a Theorem-R3-type incoherent model near T1, at each world).

---

## 1. Step (1): the cyclic family the additive chain closes (CHECKED, a reading of write-up §4 and §6.3)

The additive contradiction is a closed cycle of exchange-rate links. For each link I name the selected models and
the gambles whose comparisons it uses. Here c_k(h) is the chart vector on facet F_k, and x_k is the facet rate.

1. **Facet links (three; one per facet).** These are comparisons out of the C_q with q in every neighbourhood of p*:
   C_q against C_q with the advice on a small ball around h ∈ relint F_k toggled.
   - The chart {q : C_q accepts h} is a pencil line through p* (Thm pivot).
   - Its normal is linear in h (Prop blowup, Lemma twoslope): c_k(h) = Γ_k h.
   - In rate form, on F_k the relative world weights are x_k := (ρ_{k+1}/|h_{k+1}|) / (ρ_{k+2}/|h_{k+2}|), constant
     along the facet.
   - The crossing rows (charts of w_{ik} pass through e_i) fix the other two entries.
   - Each facet arc runs corner portion → crossing → middle arc → crossing → corner portion, through all three sign
     classes. On F_1 these are Q_2 (near r_31), Q_1 (middle arc), Q_3 (near r_12).
2. **Corner links (three).** At r_{k,k+1} the chart from F_k equals the chart from F_{k+1} (Thm nosliding, (NS)).
   The corner gamble is a single point, so its rates are single-valued. With p*·c = 0 this gives
   x_k + 1/x_{k+1} = κ + 1. Going round the corners composes the Möbius map φ(t) = κ + 1 − 1/t three times. The
   holonomy condition is x_1 = φ³(x_1); φ is hyperbolic, so x_1 = x_2 = x_3 = x_±.
3. **Edge (box) links (three, with mirrors).** These are comparisons out of edge models C_{q0}, q0 ∈ e_ab, near e_b,
   for two gambles near the crossings of coordinate b: A ∈ F_k and B ∈ F_{k′}. Since A_a < 0 < A_b and
   B_b < 0 < B_a, while the third coordinates have opposite signs, both lie in Q_a ⊆ R_ab (for T1 and (a,b) = (1,2):
   A ≈ (−β, 0⁺, 1), B ≈ (1, 0⁻, −β), both in Q_1). An edge model is competitive on {a,b} and coherent, so it cannot accept both when
   A + λB < 0 at a and b (Lemma edgebox). In rates: x_k x_{k′} ≤ κ, and the mirror gives ≥ 1/κ. These are
   incompatible with x_± (Prop T1; one-sided form Lemma P1box).

So the cycle is: three facet-rate links (near T1), three corner identifications (near T1), and three edge pinnings
(at the edges). Two remarks:

- **It is not a finite family of comparisons.** The facet links come from blow-ups at p* (limits over q → p* and over
  balls shrinking to h). What a non-additive world would have to break is the *single-valuedness and linearity of
  rates*: the rate at which world i trades a ball near one boundary gamble against a ball near another.
- **Every such trade at world i is a trade between sign classes.** If the two balls lie in Q_i ∪ Q_j it is an R_ij
  comparison; if they lie in Q_j and Q_k it is an *interior* comparison for world i, the kind the brief proposed to
  make non-additive. §2 shows that the second kind is decided by the first.

---

## 2. Step (2): the design, and why it collapses

**Design D.** For each world i, fix positive integrable densities ρ^{ij} on R_ij and ρ^{ik} on R_ik:

- world i compares models differing inside one edge region additively (or at least accepts every ρ-strict
  improvement there), so every edge result holds;
- on comparisons whose difference meets both Q_j and Q_k, world i is free;
- there the cyclic M1 exchanges are to be placed around the corners.

The definitions below concern **regular** models only, i.e. models that accept a.e. h ∈ N_+. For regular models
Y, Z, Y △ Z = E_iY △ E_iZ ⊆ M. Every relevant comparison is between regular models.

**Definition.** Let S ⊆ M be measurable and non-null. A positive integrable ρ on S is a **leading density of world i
on S** if, for all regular Y, Z with Y △ Z ⊆ S:

- (L1) ρ(E_iZ ∖ E_iY) > ρ(E_iY ∖ E_iZ) ⇒ Y ⪯_i Z.

It is **additive on S** if moreover Y ⪯_i Z ⇔ ρ(E_iZ ∖ E_iY) ≥ ρ(E_iY ∖ E_iZ).

**Lemma B1.0 (PROVED).** If world i is a preorder with strict (G) and ρ satisfies (L1) on S, then also

- (L2) Y ⪯_i Z ⇒ ρ(E_iZ ∖ E_iY) ≥ ρ(E_iY ∖ E_iZ), for regular Y, Z with Y △ Z ⊆ S.

So ρμ|_S endorses every comparison of world i between regular models that differ inside S.

*Proof.*
- Suppose Y ⪯_i Z and g := ρ(E_iY ∖ E_iZ) − ρ(E_iZ ∖ E_iY) > 0.
- Then S ∖ E_iZ is non-null. Otherwise Y △ Z ⊆ S ⊆ E_iZ gives E_iY ∖ E_iZ = ∅ and g ≤ 0.
- Take a non-null e ⊆ S ∖ E_iZ with ρ(e) < g/2 (ρμ is atomless) and put Z′ := Z △ e. Then E_iZ′ = E_iZ ∪ e, so
  Z ≺_i Z′ by strict (G).
- Z′ is regular and Z′ △ Y ⊆ S. Moreover ρ(E_iY ∖ E_iZ′) − ρ(E_iZ′ ∖ E_iY) ≥ g − 2ρ(e) > 0, so (L1) gives
  Z′ ⪯_i Y.
- Hence Z ≺_i Z′ ⪯_i Y ⪯_i Z, i.e. Z ≺_i Z, a contradiction. ∎

**Lemma B1.1 (gluing; PROVED).** Let world i be a preorder with strict (G), with leading densities ρ^{ij} on R_ij
and ρ^{ik} on R_ik. Then ρ^{ik} = c ρ^{ij} a.e. on Q_i for a constant c > 0.

*Proof.*
- Let f := dρ^{ik}/dρ^{ij} on Q_i, and suppose ess inf f < ess sup f. Choose a, δ so that S_− := {f < a − δ} and
  S_+ := {f > a + δ} are both non-null.
- By Lyapunov take B ⊆ S_+ with ρ^{ij}(B) = b > 0 small, and A ⊆ S_− with ρ^{ij}(A) = (1+η)b, where
  (a − δ)(1 + η) < a + δ.
- Then ρ^{ik}(A) ≤ (a − δ)(1+η)b < (a + δ)b ≤ ρ^{ik}(B).
- Choose regular Y, Z that agree off A ∪ B, with E_iZ ∖ E_iY = A and E_iY ∖ E_iZ = B (fix the advice on A ∪ B
  accordingly). Then Y △ Z = A ∪ B ⊆ Q_i ⊆ R_ij ∩ R_ik.
- (L1) for ρ^{ij} gives Y ⪯_i Z, since ρ^{ij}(A) > ρ^{ij}(B).
- (L2) for ρ^{ik} (Lemma B1.0) then gives ρ^{ik}(A) ≥ ρ^{ik}(B), a contradiction. ∎

Rescale ρ^{ik} by 1/c and define the **glued density** ρ_i := ρ^{ij} on R_ij and ρ^{ik}/c on R_ik. It is
well defined, positive and integrable on M, and leading on R_ij and on R_ik.

**Lemma B1.2 (transfer chain; PROVED).** Let ρ be a positive integrable density on M. Let C, X be regular models
with D := C △ X, and put Δ := ρ(E_iX) − ρ(E_iC) = ρ(D ∖ E_iC) − ρ(D ∩ E_iC). If Δ ≥ 0, there is a finite chain
of regular models C = Z_0, Z_1, …, Z_N = X such that, for every t:

- Z_t △ Z_{t+1} ⊆ R_ij or Z_t △ Z_{t+1} ⊆ R_ik;
- ρ(E_iZ_{t+1}) − ρ(E_iZ_t) = Δ/N ≥ 0, the same for every step (so > 0 when Δ > 0).

*Proof.* For a set S toggled out of a model Z, write s_Z(S) := ρ(S ∖ E_iZ) − ρ(S ∩ E_iZ), the change in ρ-error.
Put D_l := D ∩ Q_l, s_a := s_C(D_i) + s_C(D_j) and s_b := s_C(D_k). Then s_a + s_b = Δ.

*Case 1: Q_i ∖ D is non-null.*
- **Room.** Q_i ∖ D splits into R⁺ (where C, and X, are correct at world i) and R⁻ (where they err). At least one is
  non-null. Toggling c ⊆ R⁺ changes the ρ-error by +ρ(c); toggling c ⊆ R⁻ changes it by −ρ(c); toggling back undoes
  the change.
- **Pieces.** For m ∈ ℕ, split each of D_i, D_j, D_k by Lyapunov into m pieces. Each piece of D_l carries 1/m of
  both ρ(D_l ∩ E_iC) and ρ(D_l ∖ E_iC), hence net change s_C(D_l)/m. This holds whatever has been toggled elsewhere,
  because the pieces are disjoint.
- **One round** has two steps:
  - step a toggles a piece of D_i and a piece of D_j, a subset of R_ij;
  - step b toggles a piece of D_k, a subset of R_ik.
- **Transfer.** Put τ := Δ/(2m) − s_a/m. Add a set c of ρ-measure |τ|, with c ⊆ R⁺ or c ⊆ R⁻; it is toggled in the
  first step of the round and toggled back in the second.
  - With order (a, b): step a changes by s_a/m + τ, if c ⊆ R⁺ and τ ≥ 0, or c ⊆ R⁻ and τ ≤ 0.
  - With order (b, a): the same, if c ⊆ R⁻ and τ ≥ 0, or c ⊆ R⁺ and τ ≤ 0.
  - So whichever of R⁺, R⁻ is non-null, both signs of τ are available. Since |τ| ≤ (|s_a| + Δ)/m, for m large the
    set c fits.
- **Changes.** Each step changes the ρ-error by exactly Δ/(2m) ≥ 0 (this also covers Δ = 0, where τ = −s_a/m):
  - step a: s_a/m + τ = Δ/(2m);
  - step b: s_b/m − τ = Δ/m − Δ/(2m) = Δ/(2m).
- **Region control.** c ⊆ Q_i lies in both regions. So every step toggles a subset of R_ij or of R_ik.
- **End point.** After m rounds every piece of D is toggled once and c is restored, so Z_{2m} = X. All toggles lie in
  M, so all intermediate models are regular.

*Case 2: Q_i ⊆ D a.e.*
- By Lyapunov split D = D′ ⊔ D″ so that each of the six numbers ρ(D_l ∩ E_iC), ρ(D_l ∖ E_iC) is halved.
- Go from C to Z := C △ D′ and then from Z to X. Each leg has net change Δ/2 ≥ 0, and both legs use the same m,
  so all 4m steps have change Δ/(4m).
- In both cases N = 2m or N = 4m, and every step has change Δ/N.
- Each leg has room in the link class: Q_i ∖ D′ ⊇ D″ ∩ Q_i, of ρ-measure ρ(Q_i)/2 > 0, and symmetrically for the
  second leg. Apply Case 1 to each leg. ∎

NUMERICS. `b1py/transfer_chain.py` runs exact rational arithmetic on atomless cells: 4000 instances with Δ > 0, 2000
of them with no room. Every chain has steps inside one edge region, all with the same positive change, summing to
Δ. In the worked example with s_J = −5, s_K = +6 and room 1/100, the chain has 2048 steps of change 1/2048.
`b1py/t1_chain.py` takes ε = 0.3, s = 0.9, C = D_{conv(T1 ∪ {q})} and X = T1 minus a thin cone around
w = (−0.5, 1, 1). At each world, with a non-constant density, the chain uses only R_ij and R_ik steps, and it
derives the strict comparison that ρ_i favours (world 1: X ≺_1 C; world 2: C ≺_2 X; world 3: X ≺_3 C). See
`t1_chain.out`.

**Theorem B1.3 (edge leading densities propagate; PROVED).** Let world i of a ranking on M_U be a preorder with
strict (G), with leading densities on R_ij and on R_ik, and let ρ_i be the glued density. Then for all regular
C, X:

- ρ_i(E_iX) > ρ_i(E_iC) ⇒ C ⪯_i X;
- C ⪯_i X ⇒ ρ_i(E_iX) ≥ ρ_i(E_iC).

Hence ν_i := ρ_i μ|_M + μ|_{N_+} is positive on non-null sets and endorses every relevant comparison of world i, so
world i adds up. If both edge restrictions are additive, world i is additive on regular models with density ρ_i.

*Proof.*
- **First claim.** Lemma B1.2 gives a chain whose steps lie in R_ij or R_ik and strictly increase the ρ_i-error.
  ρ_i is leading on each region, so (L1) gives Z_t ⪯_i Z_{t+1} at every step; transitivity gives C ⪯_i X.
- **Second claim.** Apply Lemma B1.0 with S = M, using the first claim as (L1) on M.
- **Additive case.** If ρ_i(E_iX) ≥ ρ_i(E_iC), Lemma B1.2 gives a chain of edge steps, each with change ≥ 0. Each
  step is accepted by the additive edge representation, so C ⪯_i X. The converse is the second claim. ∎

*Uses:* transitivity of ⪯_i, strict (G) at world i, regular models, Lyapunov. *Not used:* (IB), (S), (C), (LA),
completeness, any other world, any selection.

*Relation to known results.* Theorem S21 (leading charge on M ⇒ strictly positive) and the Q3 referee's remark
("an edge-restricted endorsing charge need not endorse interior comparisons") are consistent with B1.3:

- an *endorsing* edge weight (which is what "adds up on R_ij" means) does not propagate;
- a *leading* edge density does.

**Corollary B1.4 (PROVED, at the status of Theorem M0closed(b)).** Assume (H_U): strict (G), (IB), (LA), (S), (C) on
M_U, with T1 ∈ C_L. Then some world i and some j ≠ i are such that no positive integrable density on R_ij is
leading for world i. In particular some world is not additive on comparisons between subsets of one of its edge
regions.

*Proof.* Otherwise B1.3 makes every world add up (case (M0)), which Theorem M0closed(b) excludes. ∎

*Strengthening (CHECKED, by inspection of the proof of Theorem S21).* That proof uses the leading property only for
the edge test models X^{ij}_A, together with competitiveness and closed sections at edge indices of e_ij. It shows
that a leading charge of world i on R_ij that is nonzero on R_ij is strictly positive on R_ij. So "positive" in B1.4
may be weakened to "nonnegative and not a.e. zero".

**Corollary B1.5 (the brief's two mechanisms; PROVED).**

- **(a) Additive base plus extra or reversed interior comparisons.** Let world i contain the comparisons of an
  additive ψ_i (density ρ_i) on both edge regions.
  - By B1.3, world i then contains every ψ_i-strict comparison between regular models, and only comparisons that
    ψ_i endorses.
  - An "extra" comparison is therefore already present or a ψ_i-tie.
  - A "reversed" comparison C ⪯_i X with ψ_i(C) > ψ_i(X) gives X ≺_i C ⪯_i X, a strict cycle.
  - "Keep each link and drop the one that closes the cycle" is impossible: the closing link is the chain of
    Lemma B1.2.
- **(b) min/max of several additive scores agreeing on edge regions.** Let ν, ν′ be measures on M that agree on all
  measurable subsets of R_ij and of R_ik.
  - Every S ⊆ M is the disjoint union of S ∩ R_ij and S ∖ R_ij ⊆ R_ik.
  - So ν(S) = ν′(S), and the scores coincide on M; no "interior crossing set" separates them.

---

## 3. Steps (3)–(4): not reached; what is left

The selection and the axiom checks were not attempted, because no admissible world order survived step (2). The
surviving designs are exactly those in which some world i has, on some edge region R_ij, **no** leading density
(Corollary B1.4). The order on R_ij must be:

- incomplete in an essential way (for example, unanimity over several non-proportional densities, which is (CP-a) on
  R_ij and adds up there but has no leading density); or
- complete but without a countably additive almost-agreeing representation with positive density.

In the first case the interior comparisons are no longer generated: a step of Lemma B1.2 is accepted only if every
member of the edge credal set accepts it. Room for non-additive interior comparisons then exists. But the cycle of
§1 must be broken by a world whose *edge* order is already non-tame. On the edges, Theorem Q36 and Corollary Q37
exclude:

- complete worlds under (Nest_e);
- worlds with a nonzero leading charge;
- (CP-a) worlds globally.

So the escape needs a two-world edge structure of exactly the type studied in the open two-world core: an
incomplete world without leading charge, with strict escape and closed sections along a possibly non-nested edge
selection. No full system with such a world is known for any target (write-up §8.5 summary), and I found none.

Theorem R3 does not help here. Its reversals against near-T1 incoherent models must sit at a world that lacks a
leading density on some edge region. For the shadow ν = (ρ_1, ρ_2, ρ_3) built from glued leading densities, B1.3
makes every world endorse every relevant comparison.

**Honest bottom line.** The holonomy of the corner cycle cannot be absorbed by non-additive *interior* comparisons in
any world whose edge orders are tame. Transitivity through the link class Q_i = R_ij ∩ R_ik turns tame edge exchange
rates into a global potential (B1.3), and then (M0) closes the case. A positive answer for T1 on M_U now requires,
as a sub-structure, a two-world order on an edge region with no leading density inside a full three-world system.
That is the single obstruction this attempt reveals.

---

## 4. Files (`b1py/`, run with `python3 -I`)

- `transfer_chain.py` (+ `.out`): exact check of Lemma B1.2 on random atomless-cell instances, with and without room
  in the link class; worked example.
- `t1_chain.py` (+ `.out`): the chain on a sampled T1 instance (ε = 0.3, s = 0.9) between a coherent C and a
  Theorem-R3-type incoherent X near T1, at each world.
