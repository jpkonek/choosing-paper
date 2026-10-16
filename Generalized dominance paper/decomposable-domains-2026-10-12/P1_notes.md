# P1. Case M0 on the U-domain: can atom chords of ψ rescue a cover of T1?

14 Oct 2026, BRIEF10 (round 11), construction side. Scripts: `p1py/`. Labels: **PROVED** (full proof here), **CHECKED**
(sketch, or proof imported from the write-up), **CONJECTURE**, **NUMERICS**. Nothing is assumed beyond the write-up's
framework. Notation as in "The Contamination Triangle" (§§2, 4, 7): U = D_{K′}, c(g) = ρ(g)⊙sign(g), B_q = {q·c > 0},
K♭_q (B_q = D_{K♭_q} a.e., for EVERY q, Thm Estructure(d)), E(ψ) = union of atom chords, p* the ψ-Bayes weighting of
T1, normalised p* = u, facet data x_k as in Prop T1.

---

## 0. Outcome

**No cover was constructed. No proof that M0 is impossible was found.** What was obtained:

1. **Reduction (CHECKED).** On M_U the three new routes (I1, I2, C2/short) are not the relevant obstruction. They are
   proofs for general decomposable domains, and their common input Cor TSalways(b) ("both acceptances in the advice range
   of a.e. mixed pair") is already contradictory on M_U. For a supporting assessment ψ on M_U, all of them reduce to the
   chain of §4 (Thm pivot → (PC), (NS) → corner equations + box). Every route enters through the facet data at p*.
   So a chord configuration defeats all three routes as soon as it defeats the facet-data algebra at p*.
2. **Straight levels survive every atom chord (PROVED, Lemma P1.2).** For every gamble h and level t, the sets
   {q : P_{K♭_q}(h) > t} and {q : P_{K♭_q}(h) < t} are half-planes ∩ int Δ, at every interior q. No continuity of K is
   needed. This removes one of the two "global" caveats in the write-up's localisation remark. Only PL2/nopin and
   evaluation at p* remain.
3. **One-sided holonomy (PROVED, Lemma P1.1).** The box bounds 1/κ ≤ x_k x_{k+1} ≤ κ and the corner relations weakened
   to *inequalities* x_k + 1/x_{k+1} ≥ κ+1 (k cyclic) have no positive solution. Here κ > 1.
4. **Atoms at corners cannot help (PROVED under hypothesis (HC), Thm P1.4).** An atom chord through p* whose atom sits
   at a corner of ∂D_{T1} turns (NS) at that corner into the *strict inequality* x_k + 1/x_{k+1} > κ+1, never the reverse
   (Lemma P1.3). By P1.1, any set of corner atoms through p* leaves the box contradiction intact. This covers R-a′(i)
   entirely (by Prop 4.3, a single atom at p* is a corner atom), and also the corner part of R-a′(ii), (iii).
5. **The escape that survives (NUMERICS, §4).** Atoms through p* whose arcs lie in the *middle* (+,+)-region of each
   facet ("split facets") give each facet two linear chart maps, of ratios a_k near one corner and b_k > a_k near the
   other. With (NS) at all three corners, b_k = κ+1 − 1/a_{k+1}, and the box admits solutions, for example
   a_k ≡ a ∈ (1/κ, 1). The semi-exact box search finds no certificate (log-margins −0.13 … −1.5 at ε = 0.1, 0.3, 0.6,
   0.9); the controls x_± give the known certificates. So the facet-data algebra at p* does **not** exclude M0.
   The configuration needs:
   - p* at a crossing of at least three atom chords, with a 2-dimensional face;
   - T1 intermediate in that face;
   - the mid-facet atoms *outside* cl D_{T1};
   - directional limits that drop vertices of T1.

   §4.3 gives proved constraints on it.
6. **Construction status.** Step (2) of the plan requires a global ψ (field c on U), and it is not achieved. Neither
   the split facet data nor any other configuration is known to extend from p* to the whole simplex with coherent B_q
   off E. Without ψ, the ordinal tie-breaking and the exact consistency test could not be run. §5 states the precise
   construction problem (CFJ) and what an obstruction would have to show.

---

## 1. What the additive proofs need from the Bayes family, and where atoms enter

**1.1 On M_U, I1/I2/C2 reduce to the §4 chain (CHECKED).**
- Thm gm's three routes start from §5.2 (Cor TSalways):
  - (b) a.e. mixed pair has both acceptances in its advice range;
  - (c) K_q → {e_b}, and edge confinement.

  On M_U no advice range contains both acceptances, so (b) already contradicts a cover. Edge confinement (K* ⊆ edge)
  is false on M_U in any case, because every K_q ⊇ K′.
- Cor TSalways rests on N21.4 items 1–5 and the localised N15 chain. So for ψ on M_U, the operative obstruction is
  Thm main, i.e. §4: Thm pivot, nosliding, PCNS, boxbridge, Prop T1.
- I1 then needs (PC) and the corner equation (x ≠ 1); I2 and C2 need the collar certificate, which uses x_+² > κ; the
  short route needs the collar. All of these come from the facet data at p*.

**1.2 Uses of the Bayes family in the §4 chain, and the effect of atom chords.**

| Step | Use of K | Atom chord through p* | Chord away from p* |
|---|---|---|---|
| Lemma chords/levels | joint continuity | harmless: Lemma P1.2 (K♭, every q) | harmless (P1.2) |
| Lemma UVN | q → e_l off E | harmless | harmless |
| Lemma PL2 in nopin (Step 1 of pivot) | clopen argument on int co(G ∪ V_l) | broken | broken if the chord separates G from V_l |
| Ψ(p*, τ) = 0 on [0,1] | K_{p*} = T1 | broken: P(p*, h) = P_{K♭}(h) may be < 0 (Thm pstarE) | harmless |
| Steps 3–5, nosliding, blow-up | continuity at p* | broken in the sectors cut by the chords | harmless if chords stay away from p* |
| Lemma edgebox | half-planes, E null | harmless (N26 §4.3) | harmless |
| boxbridge(c) | unique cluster lines of the witnesses | only through the facet data | harmless |

So the configurations that can defeat the chain are:
- (A) chords through p* (R-a′);
- (B) chords whose tie sets accumulate near a crossing ray of ∂D_{T1}, so that PL2 fails and a vertex may be pinned
  near p* (the write-up's Conj N26.R′; R-b′).

A **dense** family of chords enters only through (A) or (B).

---

## 2. Straight levels for K♭ at every weighting

**Lemma P1.2 (PROVED).** Let c be strictly signed on U, with B_q = D_{K♭_q} a.e. for every q ∈ int Δ. (This holds
for every supporting assessment: Thm Estructure(d).) For h ∈ ℝ³ put f(q) := P_{K♭_q}(h) and fix t. Then {f > t} is
int Δ ∩ (an open half-plane, ∅, or int Δ), and {f < t} is int Δ ∩ (a half-plane, possibly with part of its boundary,
∅, or int Δ).

*Proof.*
- *{f > t} is convex.* Let f(q₁), f(q₂) > t′ > t. On a ball O around h′ := h − t′𝟙, P_{K♭_{q_m}}(g) > 0 (continuity in
  g). For a.e. g ∈ O this gives g ∈ B_{q_m}, i.e. q_m·c(g) > 0, for m = 1, 2. By linearity, q·c(g) > 0 on [q₁, q₂].
  So for q ∈ [q₁, q₂], D_{K♭_q} contains a.e. point of O, hence all of O, since an open convex set containing a dense
  subset of a ball contains the ball. Thus P_{K♭_q}(h′) ≥ 0, i.e. f(q) ≥ t′ > t.
- *{f < t} is convex.* The same argument with P < 0 on O gives q_m·c(g) ≤ 0 on [q₁, q₂]. Then g ∉ B_q for a.e. g ∈ O,
  so O ∩ D_{K♭_q} is null and open, hence empty. So f(q) ≤ t′ < t.
- *Closing.* K♭ is upper semicontinuous (Estructure(d)), so f is lower semicontinuous and {f > t} is open. Also
  {f ≤ t} = ⋂_{t′>t} {f < t′} and {f ≥ t} = ⋂_{t′<t} {f > t′} are convex. Two complementary convex subsets of int Δ
  are separated by a line. ∎

*Consequence.* The write-up's localisation remark lists Lemma levels as surviving only off a null E (§7.2; N26_referee
§4.2). It holds verbatim at every interior weighting, for every field with (γ). Lemma sandwich holds wherever its
hypotheses at p* hold.

---

## 3. Corner atoms through p* do not help

**3.1 The algebra.**

**Lemma P1.1 (PROVED).** Let κ > 1, and let x₁, x₂, x₃ > 0 satisfy, for each k (indices mod 3),

 (C≥_k) x_k + 1/x_{k+1} ≥ κ+1,  (B_k) 1/κ ≤ x_k x_{k+1} ≤ κ.

This is impossible.

*Proof.* Fix k and put a = x_k, b = x_{k+1}.
- From ab ≤ κ: κ/b + 1/b ≥ a + 1/b ≥ κ+1, so b ≤ 1.
- From ab ≥ 1/κ: 1/b ≤ κa, so (1+κ)a ≥ κ+1, so a ≥ 1.

Applying this for k = 1, 2, 3 gives x_k ≥ 1 ≥ x_{k+1} for every k. Hence x₁ = x₂ = x₃ = 1, and then (C≥) reads
2 ≥ κ+1, a contradiction. ∎

(Sanity: `p1py/overlap_sympy.py`, 2·10⁵ random samples, none feasible.)

*Relation to Prop T1.* The six box bounds are those of Prop T1:
- x₁x₃ ≤ κ is the (1,2) certificate written with general facet data; the other two upper bounds are its cyclic images.
- The three lower bounds are the mirror certificates. For these, NUMERICS: the semi-exact search `p1py/box_exact.py`
  reproduces log(x₊²/κ) = 1.334 at ε = 0.3, and its binding certificates match log(1/(κ x_i x_j)) to 10⁻⁴. CHECKED
  through the transposition argument of Prop T1.

**Lemma P1.1 strengthens Prop T1.** The equality case is the corner equation. The box contradiction survives the
corners being only one-sided, in the "≥" direction.

**3.2 The sign of a corner atom.**

**Hypothesis (HC): the facet-data form of the chain with breaks.** For each facet F_k there are finitely many closed
arcs ("atom arcs"), each inside one sign-pattern region of F_k, such that:
- off the arcs, every facet gamble h has a unique oriented cluster line through p*;
- that line is given by a map Γ which is linear on each complementary piece of F_k;
- crossing rows hold on the pieces that contain crossings;
- on an atom arc the cluster line is the arc's atom chord (constant);
- the pivot normal is continuous along ∂D_{T1}, except at a corner without an atom, where (NS) holds;
- boxbridge(c) holds for witnesses off the arcs.

(HC) is what the §4 chain gives when no chord passes through p*, with no arcs. With chords through p*, (HC) is the
CONJECTURE that the chain runs sector by sector. It is not proved here, because PL2/nopin and Steps 3–5 of Thm pivot
would have to be redone in sectors with jumps.

**Lemma P1.3 (PROVED from (HC)).** Suppose an atom arc contains the corner r₃₁. Its pattern is that of r₃₁, (−,+,−),
and its chord cuts off e₂. Then x₃ + 1/x₁ > κ+1.

Here x₁ is the ratio of F₁'s piece next to r₃₁ and x₃ the ratio of F₃'s piece next to r₃₁. The same holds at every
corner, cyclically.

*Proof.*
- Parametrise the normals of pattern (−,+,−) by t := −b₁/(−b₁ − b₃) ∈ (0,1). Here t = 0 is the normal of lin(p*, e₁),
  i.e. (0,1,−1), the pivot of F₃'s 1-crossing; t = 1 is the normal of lin(p*, e₃), i.e. (−1,1,0), the pivot of F₁'s
  3-crossing.
- Γ₃ is linear, so t is strictly increasing along F₃ from its 1-crossing toward r₃₁. Γ₃ extended to r₃₁ gives
  t₃ = x₃/(κ+1).
- Likewise t increases along F₁ from r₃₁, where Γ₁ gives t₁ = 1 − 1/(x₁(κ+1)), to 1 at the 3-crossing.
- The arc has a single constant normal t_b, attained at its end h_b ∈ F₃ and its end h_a ∈ F₁, by continuity. So
  t₁ < t_b < t₃, strictly, since a non-null atom gives a non-degenerate arc.
- Finally t₃ − t₁ = (x₃ + 1/x₁ − (κ+1))/(κ+1) (sympy, `overlap_sympy.py`). ∎

*Reading.* In a realisation the pivot normal runs once round the circle with no overlap, and (NS) is the equality. An
atom can only produce an *overlap*: two facet pieces whose normal ranges overlap, joined by a constant arc. A *gap* is
what nosliding forbids, and an atom cannot fill it, because the arc's normal must be attained on both sides.

**Theorem P1.4 (PROVED from (HC)).** Assume (H_M0) and (HC), with all atom arcs at corners, and atoms through p* at any
subset of the three corners (R-a′(i), and the corner configurations of R-a′(ii), (iii)). Then no cover of T1 exists.

*Proof.*
- Without mid-facet arcs, each facet has one linear map. Its ratio x_k is shared by its two corners and by its boxes.
- Corners without atoms give equality by (NS), and corners with atoms give the strict inequality by Lemma P1.3. All
  satisfy (C≥).
- The box witnesses of Prop T1 lie arbitrarily near the crossings, which no atom arc contains (an arc lies in one
  pattern region), so (B_k) holds by boxbridge(c).
- Lemma P1.1 gives the contradiction. ∎

*NUMERICS cross-check.* With an atom only at r₃₁ and (NS) at r₁₂, r₂₃, the overlap condition holds on exactly two
branches: x₂ ∈ (1/(κ+1), x₋) and x₂ ∈ (x₊, κ+1). On the first all x_k < x₋; on the second all x_k > x₊. The
semi-exact search finds certificates on both branches at ε ∈ {0.02, 0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99}, with log
margins between 0.66 and 5.7, even after excluding the maximal possible r₃₁ arcs (`lower_branch.py`). The
general-subset run is `multi_atoms.py`. The point (κ, 1, 1/κ), with diagonal facet maps of weight (1, κ, 1), is
box-feasible with zero margin. There the r₃₁ defect is negative (a gap), so no atom can occur.

---

## 4. The surviving configuration: split facets

**4.1 Facet data with mid-facet arcs (PROVED from (HC)).** Let F₁ carry an atom arc inside its middle region
(h₂, h₃ > 0, pattern (−,+,+); the chord cuts off e₁). Write a₁ for the ratio of the piece next to r₃₁ (the piece
containing the 3-crossing) and b₁ for the piece next to r₁₂ (containing the 2-crossing). The normal parameter on the
middle region is u = ρ/(x + ρ), with ρ = h₃/h₂ increasing along F₁. Continuity across the arc gives
ρ_b/ρ_a = b₁/a₁, so **b₁ > a₁** (sympy). Cyclically on F₂ and F₃.

The pairings are then:
- corner r₁₂ ↔ (b₁, a₂), r₂₃ ↔ (b₂, a₃), r₃₁ ↔ (b₃, a₁);
- box (1,2) ↔ (b₁, a₃); the other boxes cyclically.

They are no longer the same pairs, which is why Lemma P1.1's argument does not close.

**4.2 Consistency (NUMERICS).** Take (NS) at all corners, b_k = κ+1 − 1/a_{k+1}, and a_k ≡ a ∈ (1/κ, 1). Then
b = κ+1 − 1/a > a, since 1/κ ∈ (x₋, x₊). Arcs were placed at the log-centre of each middle region, with ρ_b/ρ_a = b/a.
`split_facets.py` runs the semi-exact box search over all ordered pairs, all facet pairs and 600 edge priors, with the
arc gambles excluded or given the chord normal:

| ε | a | b | best log-margin |
|---|---|---|---|
| 0.1 | 0.81, 0.88, 0.94 | 1.10, 1.19, 1.27 | −0.42, −0.26, −0.13 |
| 0.3 | 0.58, 0.72, 0.86 | 1.56, 1.89, 2.12 | −0.76, −0.55, −0.25 |
| 0.6 | 0.39, 0.59, 0.80 | 3.91, 4.81, 5.24 | −1.34, −0.71, −0.32 |
| 0.9 | 0.28, 0.52, 0.76 | 25.4, 27.1, 27.7 | −1.47, −0.79, −0.37 |

The unsplit control x_± gives +0.83 … +1.95. **So corner equations plus box admit split solutions.** The algebra at p*
does not exclude atom chords through p* in the middle regions. (Only s is gridded, and the binding certificates sit at
the vertices; the margins are far from 0.)

**4.3 Necessary structure of a split configuration (PROVED, unconditional).** Let p* ∈ E(ψ), T1 a face model at p*,
and K any coherent face model, for example a directional limit B_{p*} ∪ (Z_{p*} ∩ {δ·c > 0}).

(a) On each facet, τ ↦ P_K(h(τ)) is concave. So O⁺_k(K) := {h ∈ relint F_k : P_K(h) > 0} is an interval, and
O⁻_k(K) := {P_K < 0} is a union of at most two end-intervals, each containing a corner.
- Gambles just outside D_{T1} near O⁺ lie in Z_{p*}, and so do gambles just inside near O⁻, since
  D_K △ D_{T1} ⊆ Z_{p*}.
- Hence tie gambles *inside* D_{T1} near a point h of a facet's middle region occur only together with tie gambles
  inside along a whole end-interval from h to a corner. That end-interval passes through a crossing, so two patterns
  and at least two atoms through p* are involved.
- So an isolated mid-facet arc consists of tie gambles **outside** cl D_{T1}. It needs a face model K with
  O⁺_k(K) ⊇ arc, hence v_k ∉ K.

(b) If K ⊊ T1 (D_K ⊋ D_{T1}), then K misses some v_k. Every h ∈ relint F_k then has P_K(h) > 0 (h·m > 0 on
T1 ∖ {v_k}). So Z_{p*} accumulates at every point of relint F_k from outside, with all three patterns of F_k (Prop 4.3's
argument).

(c) *Corollary.* Suppose the split configuration of 4.2 is realised with tie gambles only near the three mid-arcs. Then
T1 ≠ B_{p*}.
- If T1 = B_{p*}, every directional limit satisfies K_θ ⊆ T1.
- K_θ ≠ T1 for every θ: the three chord normals are the pivot normals of the three middle regions, which positively
  span the plane, so no direction rejects all three atoms.
- So each K_θ misses a vertex, and by (b) there are tie gambles along a whole facet, contradicting "only near the
  mid-arcs".

  Hence T1 is intermediate in a 2-dimensional face, its profile interior to the zonoid Σ_k[0, −∫_{G_k}c], with S ≠ ∅.
  By (a), its inside tie gambles run from the middle to corners, so the configuration must combine split facets with
  corner-to-crossing tie regions. The facet-data algebra for that combination is again feasible: the split solution
  satisfies the corner inequalities as equalities. So nothing local closes it.

---

## 5. What a construction must supply, and what an obstruction must show

**5.1 The construction problem (CFJ), precisely.** Find a measurable c : U → ℝ³ with:
- strict signs;
- B_q coherent for q ∉ E, where E is a countable union of atom chords and the atoms are as in Estructure(b);
- T1 = B_u ∪ S for some S ⊆ Z_u.

By §4, u must be a crossing of at least three chords, with split facet data. Then find preorders ⪯_i (strictly
monotone, cancellative qualitative probabilities on error sets: N9.4) such that each ψ_i endorses the relevant
comparisons, together with a selection C_p ∋ T1 with closed sections for every model. The ordinal part must:
- (i) dominate every incoherent model of the 2-dim face at u by a selected coherent model of equal ψ-profile, under
  (E_ψ) (Prop Epsi(a),(d)). This requires coherent face models B_u ∪ S realising a.e. profile of the 2-dim zonoid.
  Prop Epsi(d) (ideal tie-breaking) then forbids j-improvable selected realisers at area-a.e. profile;
- (ii) do the same along every other chord, with undominated splits independent of the point of the chord
  (Prop Epsi(e));
- (iii) avoid the N26 mechanisms: N26.5 (no 2-dim faces) and N26.7 use, per the N26 referee, (1) undominated ⇒ weakly
  ψ-Pareto, (2) R2 Thm 7, (3) the multiplier of an additive secondary, (4) the splice being a pointwise Lagrangian
  minimiser. A non-lexicographic ⪯_i must break (3)–(4). Within each ψ-fibre of the face, the comparison of a selected
  set with a competitor must not be a fixed-multiplier threshold rule shared by all three worlds. Otherwise the N26.4
  splice reappears.

None of (i)–(iii) can be checked before c exists. The exact consistency test (Thm closure) needs the family C_p and its
sections A_i(X), which depend on c.

**5.2 What remains open, and what an obstruction would have to show.**
- (O1) **(HC) in sectors.** Prove that the §4 chain runs in each sector at p* cut by atom chords: pivot lines through
  p*, linear pieces, crossing rows. Then Thm P1.4 becomes unconditional for corner atoms. The missing steps are PL2/nopin
  and continuity of pivot normals across sector boundaries, now with Lemma P1.2 available.
- (O2) **Split facets.** Exclude, or realise globally, the configuration of §4. An obstruction must use something
  beyond the facet data at p*, e.g.:
  - the global continuation of the mid-facet chords to the edges. Each chord's atom must be a shell D_{K⁺_t} ∖ D_{K⁻_t}
    at every point t of the chord (Estructure(e)), and K_t ⊇ K′ throughout;
  - a three-world multiplier argument for general (IB) preorders on the 2-dim face, generalising N26.5.
- (O3) **R-b′ (p* ∉ E).** Chords that cut PL2's set can let a vertex be pinned on a region accumulating at p*, bounded
  by chords. Lemma P1.2 shows that this, and evaluation at p*, are the only two places where chords enter the chain.

---

## 6. Status

| Claim | Status | Where |
|---|---|---|
| On M_U, I1/I2/C2 reduce to the §4 chain through facet data at p* | CHECKED | §1.1 |
| Straight levels for K♭ at every interior weighting, any field with (γ) | PROVED | Lemma P1.2 |
| Corner inequalities + box products infeasible | PROVED | Lemma P1.1 |
| Box bounds 1/κ ≤ x_k x_{k+1} ≤ κ (lower ones via the mirror certificate) | CHECKED / NUMERICS | §3.1 |
| Corner atom ⇒ strict inequality x_k + 1/x_{k+1} > κ+1 | PROVED from (HC) | Lemma P1.3 |
| No cover with only corner atoms through p* (incl. all of R-a′(i)) | PROVED from (HC) | Thm P1.4 |
| (HC) itself with chords through p* | CONJECTURE | §3.2, (O1) |
| Single corner atom: both overlap branches box-certified, ε ∈ [0.02, 0.99] | NUMERICS | §3.2 |
| Split facet data with (NS) at all corners is box-consistent | NUMERICS | §4.2 |
| Concavity/pattern constraints; split ⇒ T1 intermediate in a 2-dim face | PROVED | §4.3 |
| Global ψ, ordinal tie-breaking, closed sections | not achieved | §5 |

Scripts (NUMERICS only; no proof depends on them):
- `box_relax.py`: grid box search;
- `box_exact.py`: semi-exact box search;
- `relax_scan*.py`, `lower_branch.py`: corner-relaxed families;
- `relax_point.py`: the point (κ, 1, 1/κ);
- `multi_atoms.py`: atoms at several corners;
- `box_formula.py`: identification of the binding box bounds;
- `split_facets.py`: split facets;
- `overlap_sympy.py`: symbolic checks.
