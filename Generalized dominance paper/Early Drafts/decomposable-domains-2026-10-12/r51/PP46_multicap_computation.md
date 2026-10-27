# PP46. Fields on the multicap family: computation on the common checkpoint

23 October 2026. Task PP46 of Brief 51. One reader (me); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exact rational or exhaustive integer computation in `r9/PP46_py/` (ALL PASS). NUMERICS: floating-point evaluation of exact pointwise formulas at sampled problems, or verdicts computed on an empirical measure; no proof depends on them. CONJECTURE / OPEN as stated.

**Exact versus discretised.** Every Bayes condition and every CG2 condition below is **pointwise** (the referee's item 3), and is either proved for all problems or checked exactly. Only two things are discretised: the essential sup/inf in the interval tables of §4 (taken over samples, and used only as illustration), and the domination verdicts of §6 (computed on an empirical measure).

**Inputs.** BRIEF51, AUDIT_multicap, AUDIT_round51(_answers), PP42 and its scripts, and the coordinator's relay of REFEREE_round50. From that relay I use:
- Thm R1: for two-valued families the interval/cycle test is *exact* for (TC) in the gate-union design;
- Thm 3.1(c) without the agreement-region hypothesis: a failed pair sandwich gives a (TC) failure;
- Lemma S for sections;
- pointwise Bayes bounds.

---

## 0. Verdict

1. **The four-model checkpoint is infeasible, for every choice of fields and every choice of supporting weights (Thm A, PROVED; CHECKED).** Here "infeasible" covers interior and boundary weights, and both the strict and the closed versions of the test. The failing pair is (T, combined cut). The failure is pairwise, so it does not involve CG3 at all.
   - The infeasibility certificate is a 3-cycle. The combined cut answers on three kinds of problem at which exactly one world gains, and one of each kind exists for every world.
   - By Thm R1 and the referee's Thm 3.1(c), this is a genuine (TC) failure of the gate-union architecture with own-Bayes gates. It is not a weakness of the sufficient test.
   - I have not shown that it is a failure of the axioms. Whether some non-additive ranking could register both models is OPEN.
2. **Exact pair criterion (Thm B, PROVED; CHECKED).** Two box members can be gated together iff *each answers beyond the other on at most one corner band*.
   - In the eight-model box, 10 of the 28 pairs fail.
   - Every compatible subfamily containing T lies in the **star**: T plus the single caps at the three vertices.
   - Combined cuts are not just ungateable. In any such design they are **not competitive against T** (Prop C), so they cannot be selected.
3. **Nearby result that is available: the star (Thm D, PROVED; NUMERICS confirm).** I give a closed-form, continuous-in-s field family on the whole star {T} ∪ {C^v_s : v = 1, 2, 3, 0 < s ≤ δ}, valid for all ε ∈ (0, 1) and all δ < ε/3. It gives:
   - pointwise unique own-Bayes for every member;
   - pointwise-strict CG2 for every pair;
   - the closed triple test for every triple;
   - (BR), an envelope, and L¹-continuity in s.

   It **passes the pointwise-strict test**, which is what PP42 Thm 3.1(b) and (R0) use. It **fails the stronger open-interval test**, because its two-sided intervals are single points. It admits globally consistent constants, and so a global witness: flagged in §4.4.
4. **The star with this field family is repair-poor (Prop E, PROVED; NUMERICS).** In this design, no star member dominates T's generation-2 fills by the caps' own answer on the "one world gains" pieces. The two-corner rival T[G_i ↦ σ, G_j ↦ σ] is mostly undominated: about 11% of sampled rivals are dominated. Cap retreats on arbitrary sets are almost never dominated (§6.2).
   - PP42's remedy, a cap discounting its own v-errors, buys these dominations. But the computation shows it breaks the *cross-vertex pairs* at the cut world. That is PP42 Prop 4.4(b), now confirmed as a genuine (TC) failure by Thm R1.
   - Fixing it needs cross-vertex intervals of width at least log(1/b) at the cut world (§6.3). This is the concrete target for the next field design.

| Item | Result | Label |
|---|---|---|
| Band boundaries, depth, pieces, measures | §2 | PROVED; CHECKED |
| (T, combined cut) incompatible for all fields and weights | Thm A | PROVED; CHECKED |
| Pair criterion; box graph; T-cliques = star | Thm B, Cor B1 | PROVED; CHECKED |
| Combined cuts not competitive against T in own-Bayes gate unions | Prop C | PROVED |
| Agreement with PP45 Lemma 2.1, Thm 3.1, Cor 3.2; fan passes the pair test | §3.4 | CHECKED; NUMERICS |
| Closed-form star fields | Thm D | PROVED; NUMERICS |
| Index map from a 2-D patch onto the star | §5 | PROVED (given Lemma S) |
| Star design misses generation-2 single-correct fills | Prop E | PROVED |
| Coverage tables; PP42 discount breaks cross pairs | §6 | NUMERICS |

---

## 1. Setting and notation

- M = c·1 + εΔ with c = (1−ε)/3, vertices m_v = c·1 + εe_v, centre u.
- The cut at v of size t has new vertices p_{v,o}(t) = m_v + (t/ε)(m_o − m_v).
- On the bands, members answer σ(g) = sign(g_1 + g_2 + g_3) = sign(u·g). This holds because all cuts are at most δ < ε/3 ≤ 2ε/3 (referee item 4). The union lemma is exact because s_i + s_j ≤ 2δ < ε.
- For a field ℓ and advice a, write e_w(g) := ℓ_w(g, σ) − ℓ_w(g, S): negative where σ is w-correct, positive where σ is w-wrong.
- **Normalisation (PROVED).** Rescaling world w of member N's field by κ_w > 0 changes neither its gate verdicts nor the CG2 inequalities, once c^N_w is replaced by c^N_w/κ_w. It moves N's Bayes weight from λ to λ⊙κ. So for interior weights I take every member to be u-Bayes for its own field, with free constants. Equivalently, take all constants equal to 1 and let the member's weight be π^N = λ^N/c^N. Boundary weights correspond to π^N_w = 0, and are kept throughout §3.

---

## 2. Geometry (PROVED; CHECKED in `geometry_check.out`)

Let S := g_1 + g_2 + g_3. All formulas below are exact.

- **Band.** H_v(t) is the set of g for which cS + εg_v has the opposite sign to both
  cS + (ε − t)g_v + t g_j and cS + (ε − t)g_v + t g_k.

  Its boundary lines in problem space are three planes:
  - L_0 := {cS + εg_v = 0}, which is the arc Γ_v of ∂Sil(T);
  - L_j(t) and L_k(t), each pivoting about a fixed ray on L_0.
- **Rays.** Mod sign, H_v(t) is the cone over a thin spherical triangle. It has two fixed base rays on Γ_v, m_v × m_j and m_v × m_k, and a moving apex p_{v,j}(t) × p_{v,k}(t). For v = 1, the base rays are ∝ (−c, −c, 2c+ε) (class M_3) and (−c, 2c+ε, −c) (class M_2).
- **Depth.** For g ∈ Sil(T), exactly one vertex m_v is separated from the other two by g's plane. Put

    τ_v(g) = ε·|m_v·g| / (|m_v·g| + min_{o≠v} |m_o·g|),

  with m_w·g = cS + εg_w. Then H_v(t) = {τ_v < t}, and Sil(T) is the disjoint union of the full bands H_v(ε) (up to null sets).
- **Pieces.** H_v ∩ M_r with r ∈ {v, j, k}. The correctness pattern of σ on each piece is:

  | piece | σ is | where it lies |
  |---|---|---|
  | (v, v) | wrong only at v | the large middle part |
  | (v, j) | correct only at j | at the base corner m_v × m_k |
  | (v, k) | correct only at k | at the base corner m_v × m_j |

  I call (v, j) and (v, k) the **single-correct pieces**. Their correct worlds are the two worlds other than v.
- **Measures.** These come from exact cones and the solid-angle formula, agree with Monte Carlo to 5 s.e., and are μ(piece) for the band H_v(t):

  | ε | t | (v,v) | (v,j) = (v,k) |
  |---|---|---|---|
  | 0.1 | 0.0323 | 9.89e-3 | 1.26e-3 |
  | 0.1 | 0.0081 | 2.48e-3 | 3.01e-4 |
  | 0.3 | 0.097 | 2.93e-2 | 1.80e-3 |
  | 0.3 | 0.024 | 7.03e-3 | 3.96e-4 |

  Because |g| is independent of direction, ∫_A |g| dμ = μ(A)·E|g| for every cone A. So fields of the form (constant)·|g| on pieces have exact integrals.
- **Annuli.** Every annulus piece (H_v(t) ∖ H_v(s)) ∩ M_r with s < t is non-null. It contains a neighbourhood of a fixed base ray inside the wedge between L_o(s) and L_o(t).
- **Where members differ.** For s, t in the box,

    D_{st} = ⊔_v { min(s_v, t_v) ≤ τ_v < max(s_v, t_v) }.

  On each of these annuli the larger cut answers σ and the other is silent, so every pair and triple of members is two-valued.
- **CHECKED (A):** 34,878 exact rational problems, with ε ∈ {1/10, 3/10, 1/2} and random s, half of them near vertex planes. On all of them the union-lemma advice equals D_{K_s}, and H_v(t) = {τ_v < t}.

---

## 3. The obstruction

### 3.1 The key lemma

**Lemma A0 (one piece; PROVED).** Consider a piece with gain worlds C and loss worlds W. Let a be a member answering σ there and z a member silent there, both a.e.-unique own-Bayes. Suppose CG2 holds for the pair at all three worlds, with constants c^a, c^z. Put p := λ^a ⊙ (c^z/c^a) and q := λ^z.

Then, at a.e. point of the piece, there exist c ∈ C and w ∈ W with p_c·q_w > p_w·q_c.

*Proof.*
1. CG2 for the move z → a says c^z_w e^z_w ≤ c^a_w e^a_w at every world w.
2. Own-Bayes gives λ^a·e^a < 0 < λ^z·e^z.
3. Steps 1 and 2 combine to p·e^z < 0 < q·e^z. Here e^z is negative exactly on C, by strict guidance.
4. Every piece has |C| = 1 or |W| = 1.
5. If C = {c}: q_c·(p·e^z) − p_c·(q·e^z) = Σ_{w∈W} (q_c p_w − p_c q_w)·e^z_w must be < 0. So some w ∈ W has p_c q_w > p_w q_c.
6. If W = {w}: q_w·(p·e^z) − p_w·(q·e^z) = Σ_{c∈C} (p_w q_c − q_w p_c)·|e^z_c| must be < 0. So some c has p_c q_w > p_w q_c.
7. If p and q both vanish at the relevant world, step 3 already fails. ∎

The dual multipliers are (q_c, p_c) (or (q_w, p_w)) on the two Bayes rows and λ^a_w on the CG2 rows. This is the LP certificate that `pair_criterion.py` (b) verifies on 1,061 infeasible random pieces.

Under the referee's sandwich form, zero constants do not help on a two-signed move. The ess sup and ess inf of a positive finite ratio over non-null sets lie in (0, ∞).

### 3.2 The combined cut

**Theorem A (PROVED; CHECKED).** Let R be any gated, a.e.-unique own-Bayes model. Suppose that on the set where T is silent and R answers σ, R meets non-null single-correct points of all three types (correct world 1, 2 and 3). Then CG2(T, R) fails at some world, for every choice of fields and weights.

In particular this holds for **every** combined cut C_s with two positive coordinates: the bands i and j contribute the correct worlds {j, k} and {i, k}.

*Proof.*
1. Write x ≻ y when p_x q_y > p_y q_x. Lemma A0 says that every world beats some other world.
2. A finite relation in which every element beats another contains a cycle.
3. No 2-cycle exists: p_x q_y > p_y q_x and p_y q_x > p_x q_y cannot both hold.
4. No 3-cycle exists: multiplying x ≻ y ≻ z ≻ x gives P > P, where both sides equal p_x p_y p_z q_x q_y q_z (if some entry is 0, the left side would have to be > 0, forcing all entries positive). ∎

**Theorem B (exact pair criterion; PROVED; CHECKED (a) exhaustively).** Let s ≠ t be box members. They can be given own-Bayes fields satisfying CG2 at all worlds iff

  #{v : t_v > s_v} ≤ 1  and  #{v : s_v > t_v} ≤ 1.

*Proof.*
1. Put ψ = log p − log q, allowing ±∞.
2. On a band where the second member answers, Lemma A0 over the three pieces says exactly that ψ_v is the strict minimum. Where the first member answers, ψ_v is the strict maximum.
3. Hence the condition is necessary.
4. Conversely, choose ψ, then each piece's increments concentrated on the witnessing (c, w). ∎

`pair_criterion.py` (a) checks this over all 26 band configurations × 3,969 weight pairs, boundary weights included.

**Corollary B1 (CHECKED).**
- **Box.** In the 8-model box the incompatible pairs are T with each of 110, 101, 011, 111; 001 with 110 and 111; 010 with 101 and 111; 100 with 011 and 111. That is 10 of 28.
- **Maximal compatible subfamilies (in the box).** The bottom star {000, 100, 010, 001}, the top star {111, 011, 101, 110}, and six triangles such as {100, 110, 010}.
- **27-model grid.** The unique maximal compatible family containing T is the star.
- **In general:** any compatible family containing T lies in the star, since every other member must have at most one positive cut. No two compatible members can differ in all three coordinates. CONJECTURE: every compatible subfamily of the cube is at most one-dimensional.

### 3.3 Combined cuts are not competitive against T

**Proposition C (PROVED).** Work in a gate-union design in which:
- T is gated;
- every gated member is a.e.-unique own-Bayes;
- (TC) holds.

Let Y answer σ where T is silent, on a set A that meets all three single-correct types; for example, any combined cut. Then Y ⪯_w T is refused at every world w. So Y is not competitive against T, and it cannot be selected or registered.

*Proof.*
1. **Guidance refuses.** rec(Y, T) = (A: σ → S). At each w, A contains points where σ is w-wrong, so the record is not a weak w-worsening.
2. **No gate accepts.** A realiser R would be gated and equal σ on A. (TC) forces the sandwich for (R, T) at every world (referee, Thm 3.1(c) without the agreement region). Theorem A excludes this. ∎

**Classification.** This answers the brief's three-way question:
- **Not the sufficient test.** Thm R1 makes the test exact, and the failure is pairwise.
- **The gate-union architecture with own-Bayes gates.** This is where the obstruction sits, together with the requirement that T be gated.
- **The axioms: OPEN.** What remains open is whether a non-additive ranking could make T and a combined cut both universally competitive. The 3-cycle of Theorem A is a Condorcet-type pattern of the three single-correct piece types. Any ranking that rates the move T → C_s by world-wise additive values meets it.

### 3.4 Cross-check with PP45 (coordinator's request; `fan_types.out`)

**No disagreement.** PP45 Lemma 2.1 is Lemma A0 with PP45's D = −ψ. Its condition "max over worse worlds of D > min over better worlds of D" is my condition "∃ c ∈ C, w ∈ W with p_c q_w > p_w q_c". PP45 Thm 3.1 is Theorem A, and PP45 Cor 3.2 is Theorem B and Cor B1.

The two proofs differ only in their hypotheses, and each covers something the other does not:
- PP45 needs only *weak* own-Bayes for the combined cut. Lemma A0 goes through unchanged with p·e ≤ 0.
- PP46 also allows boundary weights. PP45 shows these cannot occur for multicap members anyway.

My solver finds the (T, AB) pair **infeasible**. It gives:
- 0 of 3,969 weight pairs feasible (exact integer enumeration);
- 1,061 LP Farkas certificates on random pieces;
- in `fan_types.out` (A), the type test is EMPTY for (T, AB), (T, ABC), (A, ABC) and (B, ABC), and feasible for the other six box pairs at both ε.

**PP45's fan (NUMERICS).** Tilted single-vertex cuts: 40 random cuts, tilt ratio t_1/t_2 ∈ [1/50, 50], sizes in [δ/50, δ], at ε ∈ {0.1, 0.3}. These pass the pair type test:
- with T: 80/80;
- at one vertex, nested and crossing: 500/500;
- at different vertices: 1,060/1,060.

Refinements missing two vertices fail against T in 60/60 cases, as PP45 Cor 3.3 predicts. Type occurrence is sampled (types seen at ≥ 10 points), so this is NUMERICS. The order test itself is exact enumeration.

For a single pair the type test is also sufficient (Thm B, converse direction). For the fan as a *family*, joint fields with shared values are still needed; §4's construction extends verbatim to any family whose members' answer regions on each band are nested in one depth function. Tilted cuts are not nested, so the fan needs a new joint design. OPEN.

---

## 4. The star: a closed-form compatible family (Thm D)

### 4.1 The fields

All values below are multiples of |g|. Fix TH ∈ (0, 1/2], κ ∈ (0, 1), η ∈ (0, 1/(2+2κ)) and ρ_A ∈ (0, 1/3). Put:
- θ(τ) := TH·τ/ε;
- θ_δ := θ(δ);
- ρ(τ) := κθ(τ)/θ_δ.

**Base field on Sil(T).** At a problem in band v at depth τ, with e_w := ℓ_w(σ) − ℓ_w(S):
- piece (v, v): e_v = 1 and e_j = e_k = −(1 − θ)/2;
- piece (v, j): e_v = 1, e_k = ρ and e_j = −(1 + ρ − θ); piece (v, k) is symmetric.

So Σ_w e_w = θ(τ) exactly. The remaining entries:
- at σ-correct worlds, β = 2(1 + ρ);
- at σ-wrong worlds, α = e_w/2;
- γ = 1.

**Base field on Ans(T).** Writing a for T's answer:
- α = 1 and β = 2 at a-correct worlds;
- β = ρ_A and α = ρ_A/2 at a-wrong worlds;
- γ = 1.

**Members.**
- **Weights.** π^T = (1, 1, 1) and π^{v,s} = (1, 1, 1) − θ(s)·e_v.
- **Fields.** Each member's own field is ℓ^N := π^N ⊙ (base with humility). For T the humility factor is 1, so ℓ^T := π^T ⊙ base.
- **Humility.** On the cap's own region {band v, τ < s} only, multiply its σ-wrong β by 1 + ηh and its σ-correct α by 1 − ηh, where h := θ(s) − θ(τ) > 0.
- **Normalisation.** N is u-Bayes for ℓ^N. The constants are c^N_w = 1/π^N_w.

### 4.2 The theorem

**Theorem D (PROVED).** For every ε ∈ (0, 1), δ < ε/3, and parameters as in §4.1:
- **(a) Own-Bayes.** Every star member is the a.e.-unique u-Bayes model of its own field, pointwise.
- **(b) Strict pairs.** Every pair satisfies CG2 pointwise strictly a.e. with the global constants 1/π.
- **(c) Triples.** Every triple passes the closed triple test with positive constants. Hence:
  - (TC) holds under (R) and (R0), by Thm R1(iii) and by PP42 Thm 3.1(b) with measurable a.e.-positive slack (the strictness is pointwise, as the referee checked);
  - Thm 3.2's conclusions hold: universal competitiveness against every measurable rival, undominatedness, no ties, direct (C), inert closure.
- **(d) Continuity.** The fields are continuous in s at every problem, with an integrable envelope (bounded by a constant times |g|, since ρ ≤ κε/δ). So the advice-cost differences are L¹-continuous (S2), and (BR) holds.
- **(e) Sections.** By Lemma S with zero acceptance, fixed-rival sections are closed on the star, for every measurable rival.

*Proof of (a).*
1. **Own band, answer against silence.** On band v at depth τ, π^{v,s}·e = Σe − θ(s)e_v = θ(τ) − θ(s). This is negative iff τ < s; the boundary is null.
2. **Humility.** On its own region the cap's value becomes (θ_s − θ)(η π·|e| − 1). Since π·|e| ≤ 2 + 2κ there, this stays negative.
3. **Other bands.** A cap at v is silent on band v′ ≠ v:
   - if σ is v-correct there, Σe − θ_s e_v > 0 trivially;
   - on the piece where σ is v-wrong, e_v = ρ, and Σe − θ_s ρ = θ(1 − κθ_s/θ_δ) ≥ θ(1 − κ) > 0.
4. **T** is silent on Sil(T), since Σe = θ > 0.
5. **Silence against −σ.** The value is ≥ 2(1+ρ)(1 − θ_δ) − (1+ρ)/2 > 0, because θ_δ < TH/3 ≤ 1/6.
6. **σ against −σ.** This matters only on the member's own region, where its weight is 1 at every σ-correct world. The value is ≤ (1.5 + η)(1+ρ) − 2(1+ρ) < 0, because η < 1/2.
7. **Ans(T).**
   - Answer against silence: ≤ −(1 − θ_δ) + 2ρ_A < 0 at the one-correct points, and all values are negative on U.
   - Answer against the opposite answer: 1.5ρ_A·Σπ − 3π_c < 0.
8. **Contradiction** is never optimal: β + γ > 0 at every world.

*Proof of (b).*
1. With constants 1/π, the rescaled increments of every member are the base increments, except on its own region.
2. There, the answerer's losses are multiplied by 1 + ηh > 1 and its gains by 1 − ηh < 1.
3. At a point of D_NM, exactly one of the two answers. So c^N f^N < c^M f^M strictly wherever h > 0, which is a.e.

*Proof of (c).* Global constants satisfy every pair inequality, and so every cycle.

*(d) and (e).* (d) can be read off the formulas. (e) is Lemma S, applied to a compact gated family with L¹-continuous fields. ∎

**NUMERICS (`star_check.out`).** ε ∈ {0.1, 0.3, 0.5}, 2.1·10⁶ problems each (about 300,000 in the bands), 10 members:
- every member is the strict own optimum at every sample (min margin/|g| ≈ 2·10⁻⁸; the margin vanishes at the thresholds, as it must);
- pointwise strict CG2 holds at all ≈ 1.8·10⁷ (pair, point, world) instances;
- all 360 (triple, world) closed tests pass.

### 4.3 Strict versus open (both versions computed, referee item 2)

- **Pointwise-strict version: holds.**
- **Open-interval version: fails.** All 117 two-sided pair-world intervals are single points (widths < 0.02 on samples, and exactly zero in the limit). Example: (T, C^1) at world 2 is [0, 0]. The one-sided intervals are open: (T, C^1) at world 1 is (−∞, −0.172].

The degeneracy is forced in this design. The humility factor must vanish at the threshold, because the answerer's own Bayes margin θ_s − θ(τ) vanishes there. So the strict sufficient condition that this design meets is the pointwise one, and the stronger open test is the one that fails.

Whether some continuous star design has open two-sided intervals is OPEN. It would need fields that jump at each member's own threshold.

### 4.4 Flag: a global witness

The constants 1/π are globally consistent. By Lemma 3.0 applied to all gates, a single field U dominates every gate on its own records. By PP42 Thm 2.1, the star members are then U-Bayes, possibly non-uniquely.

So this design is a **local** witnessed design. It is not a realisation of a full coherent selection: U's Bayes models at other weights are unconstrained. But it is the "one witness" commitment that PP42 §2 classifies. Whether that counts as equivalent to the excluded CPM route is a call for the audit.

Prop E shows that this design is also exactly what blocks the generation-2 repairs. So I treat it as a **compatibility baseline**, not a final design.

---

## 5. An explicit index map onto the star (PROVED, given Lemma S)

Let p_T be T's index and take a small disc P around it in int Δ. Write p − p_T = d, with Σ d_w = 0. Order the coordinates as d_(1) ≤ d_(2) ≤ d_(3), and let v(p) be the world attaining d_(1). Put

  sel(p) := C^{v(p)}_{φ(d_(2) − d_(1))},  with φ continuous, increasing, φ(0) = 0 and φ ≤ δ.

Properties:
- **Continuity.** sel is continuous into the star in measure. Where the two smallest coordinates tie, the argument of φ is 0 and sel(p) = T. So T's fibre is the Y-shaped set of those ties.
- **Supports.** Every index is interior. The members' supporting weights π^{v,s} are interior and are unrelated to p, as the audit requires.
- **Direction.** The choice "lowest coordinate gives the cut vertex" is a convention. The mirror rule using d_(3) works equally well.
- **Sections.** Lemma S gives closed fixed-rival sections in member space. Their preimages under the continuous map sel are closed in P.
- **Undominated class.** Every star member is undominated (Thm 3.2(b)), and all of them are selected by sel. By Prop C, the combined cuts are not competitive against T in this architecture. So no cube member outside the star belongs to the selected class here.

  Whether combined cuts are *dominated* is a separate question. In the design of §4 they are not (§6), and that stays visible.

---

## 6. Repairs

### 6.1 Limits of the base design

**Proposition E (PROVED).** Let X = T[G ↦ σ] with G a non-null subset of a single-correct piece (v, c) of band v. Write k for the third world.
- **(i) Any own-Bayes design.** X is dominated neither by T nor by any cap at c. For T, the record (G: S → σ) is a strict c-improvement. For a cap at c, the record adds (H_c(t): σ → S), and σ is c-wrong on band c, so that part is a strict c-improvement too. Every field rates a strict c-improvement negative, and guidance refuses it.
- **(ii) The design of §4.** X is also dominated by no cap at v disjoint from G, and by no cap at k. The argument needs θ ≤ 1/2 on G, which always holds because TH ≤ 1/2.

  Below, Φ_w(C) := Φ^base_w(T → C), the base value of the cap C relative to T at world w. The bounds hold through every realiser's gate, because humility only worsens them.
  - **Cap C at v.** By the j ↔ k symmetry and Σe ≥ 0, |Φ_c(C)| ≤ Φ_v(C)/2, while |Φ_c(G)| ≥ (1 − θ)Φ_v(G). Domination needs Φ_v(C) < Φ_v(G) at world v and |Φ_c(C)| > |Φ_c(G)| at world c. Together these give 1 − θ < 1/2, which is impossible.
  - **Cap at k.** Domination needs ∫_G ρ > Φ_k(C^k) at world k, and Φ_k(C^k)/2 ≥ |Φ_c(C^k)| > ∫_G (1 + ρ − θ) at world c. Together these give ∫_G (2 + ρ − 2θ) < 0, which is impossible. ∎

These generation-2 fills are exactly the fills PP42 left uncovered. The single-base design cannot repair them. What is needed is a cap whose own-region c-gain to v-loss ratio exceeds about 1 − θ. PP42's discount b < 1/2 of the cap's own v-penalties on its own region provides this; the same inequalities then hold with Φ_v(C) replaced by bΦ_v(C).

### 6.2 Coverage numerics (`repairs.out`; NUMERICS, empirical measure, 150 rivals per class)

In each row a design is fixed. Members are T and 20 cap sizes per vertex in [δ/60, δ]. Acceptance is through any realiser's gate or through guidance. G is a random thinned subset of one depth-layer atom, with sizes log-uniform over two decades. Each cell shows how many of 150 rivals were dominated.

| design | R1: generation-2 σ-fills | R2: two-corner | R3: cap retreats | R4: vertex fills |
|---|---|---|---|---|
| ε = 0.3, κ = 0.1 | 30 | 17 | 1 | 54 |
| ε = 0.3, κ = 0.5 | 21 | 18 | 0 | 55 |
| ε = 0.3, κ = 0.9 | 27 | 14 | 0 | 56 |
| ε = 0.1, κ = 0.1 | 23 | 16 | 0 | 52 |
| ε = 0.3, κ = 0.1, own-region discount b = 0.4 (violates CG2; diagnostic) | 88 | 87 | 20 | 88 |

Readings:
- **Dominators used.** In R1–R3 they were essentially always caps at the band's own vertex. Of the 68 dominated R2 rivals in the four compatible designs, one used T. In R4 the dominators were mainly caps at another vertex. These counts do not record piece types. They are consistent with Prop E: in the compatible designs, the single-correct pieces are where the fills stay undominated.
- **κ has little effect.** The compatible designs dominate about 15% of generation-2 fills, about 11% of two-corner rivals, essentially no cap retreats, and about 36% of vertex fills.
- **The discount helps but does not finish the job.** It triples or quadruples coverage, yet still leaves about 40% of fills and most retreats undominated, and it is not CG2-compatible (§6.3).
- **Cap retreats** C^v_s[G ↦ S] are almost never dominated by a star member, even with the discount. Removing σ on G ⊆ (v, v) improves world v and worsens both other worlds, and no star member is better at all three worlds. So retreats on arbitrary G look like a separate obstruction for the star. Their exact status is OPEN; Prop E's method should apply.

### 6.3 The PP42 discount breaks the cross pairs: certificate and redesign target

`star_check.out` (6) computes the case ε = 0.3, b = 1/2, with A = C^1_{δ/2}, A′ = C^1_δ, B = C^2_{δ/2}.
- The **pair** (A′, B) at world 2 has the empty interval [−0.082, −0.776].
- The triple (A, A′, B) fails at worlds 1 and 2 (sum L = +0.693 > 0 > sum U = −0.693 at world 2). Its certificate is the cycle with multipliers (1, 1, 1).

The mechanism:
- On cap B's own band 2, at world 2, the move is one-signed. A's world-2 field is undiscounted there, B's is discounted by b, so U drops by log(1/b).
- On A's band 1, at world 2, the move is two-signed, and in this design the interval is a single point.

**Redesign requirement (PROVED for designs of this class, whose cross intervals come from rescaled common shapes).** Consider every cap at v with own-region discount b. For each cross-vertex cap C^j_t, the pair (C^v_s, C^j_t) needs a two-sided interval at world v (from band j) of width at least log(1/b), positioned to meet the one-sided bound from band v. Nested caps at v also need, in the triple (C^v_s, C^v_{s′}, C^j_t), the bound

  inf I(s, t) − sup I(s′, t) ≤ log b + log(π^{v,s′}_v / π^{v,s}_v)  for all s < s′.

Width is **necessary**. If every cross interval were a single point, this bound would force an offset o(s) with o(s′) ≥ o(s) + log(1/b) for all s < s′. That is impossible on a continuum, which is the mechanism of PP42 Thm 4.3(c).

The two naive ways of creating width both fail at the threshold or at the arc. I checked this by hand; it is not proved in general:
- discounting the silent v-cap's v-loss on piece (j, k) leaves the interval pinned by band v;
- scaling the j-cap's whole band-v field moves the conflict to world k.

So the next field family must use fields that **jump at their own thresholds** (allowed by (S2)) or **non-base shapes on the single-correct pieces**. I state this as the target. It is not solved here.

---

## 7. Status, scripts, next step

| Result | Label |
|---|---|
| §2 geometry: formulas, depth, pieces, measures, annuli | PROVED; CHECKED |
| Lemma A0, Thm A, Thm B, Cor B1 (box graph, T-cliques = star) | PROVED; CHECKED |
| Prop C (combined cuts not competitive against T in own-Bayes gate unions) | PROVED |
| Thm D (closed-form star fields; pointwise-strict, closed-triple, continuous) | PROVED; NUMERICS |
| Open-interval version for the star | fails in this design (forced); OPEN for jump designs |
| §5 index map | PROVED given Lemma S |
| Prop E (base design misses generation-2 single-correct fills) | PROVED |
| §6.2 coverage; §6.3 cross-pair certificate | NUMERICS |
| Axiom-level status of (T, combined cut); compatible families are 1-dimensional | OPEN; CONJECTURE |

**Scripts** (`r9/PP46_py/`; run `python3 -I -B <script> > <script>.out` inside the folder):

| Script | Content | Label |
|---|---|---|
| `geom.py` | exact geometry library | library |
| `geometry_check.py` | §2: union/depth identity (34,878 exact problems), ray equations, exact piece clipping, solid angles against MC, annuli | CHECKED, ALL PASS |
| `pair_criterion.py` | Thm B exhaustive; LP and Farkas cross-check; box and grid cliques | CHECKED, ALL PASS |
| `star.py` | the field family of §4 | library |
| `star_check.py` | Thm D pointwise at 6.3·10⁶ problems; intervals; triples; (6) the discount certificate | NUMERICS, ALL PASS (sections 1–4) |
| `repairs.py` | §6.2 coverage (run with NRIV=150) | NUMERICS |
| `fan_types.py` | §3.4: pair type test on the box, PP45's fan, and two-vertex refinements | NUMERICS (order test exact) |

**Most important next step.** Pose the generation-2 repair as the LP of §6.3. On the star checkpoint {T, C^i_s, C^i_{s′}, C^j_t}, take as unknowns piecewise-constant fields on the nine piece types times two depth layers (inside and outside each member's threshold), with jumps allowed at each threshold. The constraints are:
- pointwise own-Bayes;
- strict CG2 and the CG3 cycles;
- domination of the single-correct generation-2 fills by the cap at v with discount b.

All coefficients are exact (solid angles times E|g|). Then extend the solution to the star continuum by letting the layers follow s. If this LP is infeasible, its dual is the next obstruction to report. It would then place the failure in the star with the gate-union architecture. It would not be a failure of the multicap geometry.
