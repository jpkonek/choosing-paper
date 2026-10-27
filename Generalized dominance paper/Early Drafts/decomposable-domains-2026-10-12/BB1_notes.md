# BB1 (round 30, Task A). A three-world system with a non-adding-up world: the link class pins prices. Two incompatibility theorems, and what any construction must therefore do

17 Oct 2026 (BRIEF22, Task A; rules of BRIEF13). Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: a step-by-step reading or an exact finite computation;
- **NUMERICS**: sampling or floating-point computation; nothing depends on it;
- **CONJECTURE**.

Scripts: `bb1py/` (run `python3 -I <script>.py` from inside it; outputs in `*.out`). No assumption is added. Every
extra hypothesis below is a hypothesis of a stated result, and is named where it is used.

**Domain: the U-domain M_U.** The notions this task tests are posed on M_U: relevant comparisons, adding up and the
(M0)/(M1)/(M2) division are defined there (write-up Def. addup), and M_U is the domain on which "every world adds up"
is excluded for T1 (Thm M0closed). The results below use only models that differ from an **edge-selected** model
inside the link class Q_1 ⊆ M_U. Every such model is also a model of the full four-advice domain. The transfer of the
statements to the full domain (ladder steps, contradictory advice) is **not claimed**.

---

## 0. Outcome

**The requested construction was not obtained.** The positive attempt (§5) failed. Its failure is explained by two
theorems, proved here. They hold next to any two partner worlds whose comparisons out of edge models are endorsed by
continuous densities (for example additive partners), when the edges at e_1 are of Brier type. They use only strict
(G), (IB), transitivity at world 1 and competitiveness at edge indices; (LA), (C), closed sections and the interior
selection are not used.

1. **Pump theorem (Thm BB1.A; PROVED).** On the link class Q_1, world 1 must accept two families of forced moves:
   - moves out of the 12-edge models, which lower the 12-chain coordinate x and raise ρ_2-mass;
   - moves out of the 13-edge models, which lower the 13-chain coordinate y and raise ρ_3-mass.

   Unless the partners' exchange rate is **separable**, i.e. ρ_3/ρ_2 = e^{f(x)+g(y)} with f nonincreasing and g
   nondecreasing, finitely many forced moves chain to a nonzero nonpositive accepted vector. That contradicts strict
   (G). This is an explicit, axiom-level incompatibility. It kills the design of §5: there, world 1 was to inherit
   non-additivity from a mismatch of its partners' exchange rates on its link class.
2. **Saturation theorem (Thm BB1.B; PROVED).** If the rate is separable, put φ := ρ_2 e^{f(x)} = ρ_3 e^{−g(y)}. Then
   **every** accepted world-1 vector supported over a compact (x,y)-region of the link class has ∫ δφ ≥ 0. This covers
   forced and unforced vectors, rigid or divisible, out of selected models or not. The proof routes mass through
   two-move zigzags (one 13-move, then one 12-move), whose φ-cost tends to 1.
   - Consequently world 1 has **no finite certificate** and **no infinitary certificate confined to a fixed region**
     of its link class away from the coordinate planes. Both certificate types were the ones the brief preferred.
   - This proves the link-class form of K2's Conjecture K26′ (Brier edges, continuous partners). It supplies the step
     K2_referee said was missing: passing from the weak-* closed convex hull of the forced cone to the acceptance set
     itself.
3. **Where a construction can still live (§6).** A world whose non-adding-up is witnessed in a fixed region of its
   link class needs one of the following:
   - (i) a **partner that is itself not continuously endorsable** on its comparisons out of edge models into the link
     class (a "blind partner", the T2n direction);
   - (ii) edges at e_1 that are not of Brier type. I conjecture this does not help (Prop BB1.6: coherent edge families
     are always transverse on Q_1);
   - (iii) a certificate that escapes every compact region. That is an end device, which the brief excludes.

   So in a construction of the kind requested, at least **two** worlds must fail continuous endorsement near the
   link class of the non-additive one.
4. **Why the obvious protected-region repair is an end device (Prop BB1.5; PROVED).** On Q_1, every coherent model's
   world-1 error set is an up-set in the edge coordinates (x,y). So a region that no forcing selected model gets wrong
   at world 1 can only shrink to the corner (x,y) → (0,0), which is the coordinate axis R_+e_1. D2's protected end is
   of this kind.

**Aimed at T1.** The corner ray r_23 = (κ+1, −1, −1) of D_{T1} lies in Q_1^+, at (x,y) = (1/(κ+1), 1/(κ+1)), inside a
compact region away from the coordinate planes; cyclically, r_31 ∈ Q_2 and r_12 ∈ Q_3. So Thm BB1.B speaks exactly
where T1's corner holonomy sits.

*Reading* (not a theorem): in a T1 cover with Brier-type edges, a world can absorb the corner cycle at its own link
class only if one of its partners is not continuously endorsable there.

The positive design of §5 was chosen with T1 in mind, by putting the holonomy defect (a non-separable exchange rate)
into the link class. BB1.A shows that this placement is a pump.

**Plain-English status.**
- No full three-world system with a non-adding-up world was built.
- The design I tried was the natural one: two ordinary (additive) partner worlds whose exchange rates do not fit
  together on the region where both meet the third world. That design is provably impossible: it forces the third
  world to prefer a strictly worse model.
- When the exchange rates do fit together, the third world is forced to have a genuine price on that region. Then no
  certificate of the kind the brief asked for can exist there.
- So a successful construction must make at least one partner world itself non-additive on that region, or push the
  certificate to an end of the simplex. The brief rules out the second option.

| | Statement | Label |
|---|---|---|
| BB1.0 | link-class coordinates; Brier-type edges (TH); partner endorsement (E2), (E3) | definitions |
| BB1.1 | forced edge moves on Q_1 (12: x↓, ρ_2↑; 13: y↓, ρ_3↑, other coordinate free) | PROVED |
| BB1.2 | a positive cycle of the move graph is realised by sets and contradicts strict (G) | PROVED; NUMERICS (A), (B) |
| BB1.3 | no positive cycle ⇒ log(ρ_3/ρ_2) = f(x)+g(y), f↓, g↑ (potential argument) | PROVED |
| BB1.A | pump theorem (incompatibility for non-separable partner rates) | PROVED |
| BB1.B | saturation: separable ⇒ φ endorses every accepted vector over compact link regions | PROVED; NUMERICS (C) |
| BB1.C | no finite / fixed-region certificate on the link class next to such partners; local K26′ | PROVED |
| BB1.5 | coherent error sets on Q_1 are up-sets; protected regions shrink to the axis R_+e_1 | PROVED |
| BB1.6 | 12- and 13-edge boundary families of coherent edge models are transverse on Q_1^+ (singleton K′) | PROVED |
| BB1.7 | (TH) can be replaced by "coherent edge selections with (S)" | CONJECTURE |
| BB1.8 | extension of BB1.B from Q_1 to compact parts of R_12 ∪ R_13 | sketch; not PROVED |

---

## 1. Setting (BB1.0)

n = 3, U = D_{K′}, K′ ⊆ Δ° a credal set, M_U, and the notation of write-up §8.6:
- P_i, E_i, σ_i, M, N_+, R_ij;
- Q_l, the sign class in which world l has the odd sign;
- the **link class** of world 1, Q_1 = R_12 ∩ R_13 (worlds 2 and 3 agree there, against world 1).

World i is identified with its acceptance set 𝒜_i of ternary vectors δ = 1_{E_iY} − 1_{E_iX} (X ⪯_i Y). By N17.1(a)
such a set comes from a preorder with strict (G) and (IB) iff it:
- contains every δ ≥ 0;
- contains no δ ≤ 0 with δ ≠ 0;
- is closed under pairwise sums that stay ternary.

The chaining lemma N17.1(b) is used repeatedly.

**Coordinates on the link class.** Q_1^+ := {h ∈ U : h_1 > 0 > h_2, h_3}. Write h = r(1, −x, −y) with r > 0 and
x, y > 0. Let Ω_U ⊆ (0,∞)² be the (x,y)-projection of Q_1^+. It is the open set {(x,y) : k_1 > k_2x + k_3y for every
k ∈ K′}. Under h ↦ (x,y,r), μ has the positive continuous density (2π)^{−3/2} r² e^{−r²(1+x²+y²)/2}.

A **cell** is the cone over a small closed square in (x,y), intersected if wished with a radial interval. A **box** is
Ω = (x_0,x_1) × (y_0,y_1) with cl Ω ⊆ Ω_U. The results also hold on Q_1^− = {h_1 < 0 < h_2, h_3}, with
h = r(−1, x, y), by the same proofs; only Q_1^+ is written out.

**Hypotheses** (named where used; none is a new axiom of the ranking):
- **(H1)** World 1 is a preorder with strict (G) and (IB). For every q on the open edges (e_1, e_2] and (e_1, e_3],
  the selected C_q is competitive on supp q.

  (H1) follows from (S). Closed sections, (LA) and (C) are not used.
- **(TH) Brier-type edges at e_1.**
  - For every θ in an open interval J_x ⊇ [x_0, x_1] there is q on the edge (e_1, e_2] with
    E_1(C_q) ∩ Q_1^+ = {x ≥ θ} a.e.
  - For every θ in an open interval J_y ⊇ [y_0, y_1] there is q on (e_1, e_3] with E_1(C_q) ∩ Q_1^+ = {y ≥ θ} a.e.

  For C_q = U ∩ {q·h > 0} (for instance K2.5's selection, or any selection that is Brier on the two edges at e_1):
  E_1(C_q) ∩ Q_1^+ = {x ≥ q_1/q_2} on the 12-edge and {y ≥ q_1/q_3} on the 13-edge. So (TH) holds with
  J_x = J_y = (0,∞). The interior selection is arbitrary.
- **(E2) Partner endorsement on the 12-edge.** There is a continuous ρ_2 > 0 on the cone over cl Ω, integrable
  there, such that for every q on (e_1, e_2] and every X with X △ C_q ⊆ Q_1^+ over Ω:
  C_q ⪯_2 X ⇒ ρ_2(E_2C_q) ≤ ρ_2(E_2X).

  **(E3)** is the same for world 3, ρ_3 and the 13-edge.

  (E2) holds if world 2 is additive with a continuous density. It also holds if world 2 has a continuous leading
  density on R_12 (Lemma B10), and more generally if world 2 adds up on these particular comparisons with a continuous
  density. Put w := ρ_3/ρ_2 and v := log w, both continuous on the cone over cl Ω.

---

## 2. Forced edge moves (Lemma BB1.1; PROVED)

**Lemma BB1.1.** Assume (H1), (TH), (E2), (E3).
- **(a) 12-moves.** Let θ ∈ J_x. Let B, B′ be measurable subsets of the cone over Ω with B ⊆ {x ≥ θ}, B′ ⊆ {x < θ},
  and ρ_2(B′) > ρ_2(B). Then 1_{B′} − 1_B ∈ 𝒜_1.
- **(b) 13-moves.** The same holds with y, J_y and ρ_3 in place of x, J_x and ρ_2.

In words, world 1 accepts moving a world-1 error:
- downward in x by a 12-move, with y and r free, whenever ρ_2-mass increases;
- downward in y by a 13-move, with x and r free, whenever ρ_3-mass increases.

*Proof.* (a) Take q on (e_1, e_2] with E_1(C_q) ∩ Q_1^+ = {x ≥ θ} (TH). Then B ⊆ E_1(C_q) and
B′ ∩ E_1(C_q) = ∅. Let X be the model with E_1X = (E_1C_q ∖ B) ∪ B′, i.e. X := C_q △ (B ∪ B′); then
X △ C_q = B ∪ B′ ⊆ Q_1^+.

On Q_1 ⊆ R_12, worlds 1 and 2 have opposite signs. So toggling world-1 error status toggles world-2 status the other
way: E_2X = (E_2C_q ∪ B) ∖ B′. Hence

  ρ_2(E_2X) − ρ_2(E_2C_q) = ρ_2(B) − ρ_2(B′) < 0.

By (E2), not C_q ⪯_2 X. Since supp q = {1,2} and C_q is competitive on it (H1), C_q ⪯_1 X. Its vector is
1_{E_1X} − 1_{E_1C_q} = 1_{B′} − 1_B. (b) is the same argument on the 13-edge, using Q_1 ⊆ R_13 and (E3). ∎

These are relevant comparisons: C_q ∈ C_L by (S), and X is regular because it agrees with C_q off Q_1.

---

## 3. The pump theorem

**The move graph.** Let G_Ω be the directed graph on the points P = (x,y,r) ∈ Ω × (0,∞):
- a **12-edge** P → P′ exists iff x′ < x, with weight 0;
- a **13-edge** P → P′ exists iff y′ < y, with weight v(P′) − v(P).

When both kinds apply, take the larger weight. A **positive cycle** is a finite closed walk of positive total weight.

**Lemma BB1.2 (positive cycle ⇒ violation of strict (G); PROVED).** Assume (H1), (TH), (E2), (E3). If G_Ω has a
positive cycle, then 𝒜_1 contains a nonzero vector ≤ 0. That is impossible.

*Proof.* Let P_0 → P_1 → … → P_N = P_0 be a cycle of total weight c > 0, all steps strict. Choose τ > 0 and a
half-width η > 0 such that:
- consecutive points of each step are separated by more than 2η in the coordinate that the step lowers (x for a
  12-step, y for a 13-step);
- the oscillation of v on the η-cell Γ_k around each P_k (a box in (x,y,r)) is at most ω, with
  (1+τ)^N e^{2Nω − c} < 1.

Continuity of v on the compact closure makes this possible. The sets are chosen inductively; they are pairwise disjoint
except that S_N will be chosen inside S_0. Put W_k := ρ_3(S_k)/ρ_2(S_k).
- **Start.** Take a non-null S_0 ⊆ Γ_0 so small that every set required below fits into its cell.
- **12-step.** Take S_{k+1} ⊆ Γ_{k+1} with ρ_2(S_{k+1}) = (1+τ)ρ_2(S_k). Choose a threshold θ ∈ J_x between the
  x-ranges of Γ_k and Γ_{k+1}; Lemma BB1.1(a) gives 1_{S_{k+1}} − 1_{S_k} ∈ 𝒜_1.
- **13-step.** Take S_{k+1} with ρ_3(S_{k+1}) = (1+τ)ρ_3(S_k); Lemma BB1.1(b) gives the same conclusion. Since
  W_k ∈ [e^{v(P_k)−ω}, e^{v(P_k)+ω}], this gives

    ρ_2(S_{k+1}) = (1+τ) ρ_2(S_k) W_k / W_{k+1} ≤ (1+τ) e^{−(v(P_{k+1}) − v(P_k)) + 2ω} ρ_2(S_k).

Multiplying over the cycle gives ρ_2(S_N) ≤ (1+τ)^N e^{2Nω − c} ρ_2(S_0) < ρ_2(S_0). So S_N can be taken as a subset
of S_0 with S_0 ∖ S_N non-null; it is disjoint from S_{N−1}, which lies in another cell. (A cell visited twice by the
cycle receives disjoint sets, which is possible since the masses are small.)

The vectors 1_{S_{k+1}} − 1_{S_k} have:
- pairwise disjoint positive parts S_1, …, S_N;
- pairwise disjoint negative parts S_0, …, S_{N−1}.

By the chaining lemma their sum 1_{S_N} − 1_{S_0} = −1_{S_0 ∖ S_N} lies in 𝒜_1. It is nonzero and ≤ 0, against
strict (G). ∎

Concretely: let W be the common rest of the world-1 error set, and let X_k be the regular model with
E_1X_k = S_k ∪ W. Then (IB) and transitivity give X_0 ⪯_1 X_N, while E_1X_N ⊊ E_1X_0 gives X_N ≺_1 X_0.

**Lemma BB1.3 (no positive cycle ⇒ separable rate; PROVED).** If G_Ω has no positive cycle, then
v(x,y,r) = f(x) + g(y) on Ω × (0,∞), with f continuous and nonincreasing and g continuous and nondecreasing. In
particular w does not depend on r.

*Proof.*
- **Reachability.** Any P reaches any P′ in at most two steps.
  - If x′ < x, one 12-step suffices; if y′ < y, one 13-step suffices.
  - Otherwise go first by a 13-step to (x′+ε, y−ε, r′), which lies in Ω for small ε since Ω is open, and then by a
    12-step to P′.
- **The potential.** Fix P_*. Let Φ(P) be the supremum of the weights of walks from P_* to P.
  - Φ(P) > −∞ by reachability.
  - Φ(P) < ∞: otherwise append a fixed walk from P to P_* and obtain a positive cycle.
  - For every 12-edge P → P′, Φ(P′) ≥ Φ(P).
  - For every 13-edge, Φ(P′) ≥ Φ(P) + v(P′) − v(P); so Ψ := Φ − v satisfies Ψ(P′) ≥ Ψ(P).
- **Φ depends only on x.** Put F(x) := sup Φ(x,·,·) and F̲(x) := inf Φ(x,·,·).
  - The 12-inequality says that every value at x′ < x is ≥ every value at x, so F̲(x′) ≥ F(x). Hence F is
    nonincreasing and F̲(x) ≥ F(x+).
  - At every continuity point of F, F̲(x) = F(x), so Φ(x,·,·) is constant there.
  - F has countably many discontinuities.
- **Ψ depends only on y.** In the same way Ψ(·,y,·) = G(y) for all but countably many y, with G nonincreasing.
- **Conclusion.** v = Φ − Ψ = F(x) − G(y) on a dense set. Since v is continuous, F and G extend continuously from the
  good points, preserving monotonicity, and the identity holds everywhere. Put f := F and g := −G. ∎

**Theorem BB1.A (pump theorem; PROVED).** Assume (H1), (TH), (E2), (E3) on a box Ω. Then ρ_3/ρ_2 = e^{f(x)+g(y)} on
the cone over Ω, with f nonincreasing and g nondecreasing. Equivalently: if the partners' exchange rate on the link
class is not of this form, then no world 1 satisfies strict (G), (IB) and transitivity next to them. This holds
whatever the interior selection, and whatever world 1 does elsewhere.

*Proof.* BB1.2 and BB1.3. ∎

**Remarks.**
- The two-step cycle P →12→ P′ →13→ P with P′ strictly up-left of P already forces w(P′) ≥ w(P). So w is
  nonincreasing in x, nondecreasing in y, and independent of r.
- Monotonicity is **not** enough. NUMERICS (A) (`pump_grid.py`, a 21 × 21 grid on [0.2,0.4]², exact longest-path
  search) found the following:
  - for w = (y/x)(1 + 1_{y>x}), which is monotone but not separable, a positive 14-step cycle, which crosses the
    diagonal upward by 13-steps and back by 12-steps;
  - for w = (y/x)(1 + bump), a positive 4-step cycle;
  - for the separable rates y/x and e^{−3x+2y}, no positive cycle.
- NUMERICS (B) (`pump_masses.py`) realises the 4-step cycle with Gaussian cell masses and worst-case density ratios
  (half-width 0.003, τ = 10^{−3}). Every set fits in its cell, and ρ_2(S_N)/ρ_2(S_0) ≤ 0.627 < 1. All cells lie in U
  for K′ = u + 0.1(T1 − u), ε = 0.3.
- **Relation to known results.**
  - K2.1 shows that forced (divisible) comparisons can never form a certificate **inside a consistent world**.
  - BB1.A is the converse direction for edge-forced moves: when the forced moves themselves admit a positive
    combination ≤ 0 (here, a chain), no consistent world exists.
  - The separability condition is the link-class gluing condition of Lemma B11 and Prop KR62, now derived from the
    partners rather than assumed of world 1.

---

## 4. The saturation theorem

**Theorem BB1.B (PROVED).** Assume (H1), (TH), (E2), (E3) on a box Ω, so that ρ_3/ρ_2 = e^{f(x)+g(y)} by BB1.A.
Put

  φ := ρ_2 e^{f(x)} = ρ_3 e^{−g(y)}   (continuous and > 0 on the cone over cl Ω),

and let Ω′ be a box with cl Ω′ ⊆ Ω. Then for all disjoint measurable P, Q contained in the cone over Ω′:

  1_Q − 1_P ∈ 𝒜_1 ⟹ φ(Q) ≥ φ(P).

Hence every accepted vector δ of world 1 supported in the cone over Ω′ has ∫δφ dμ ≥ 0. This holds for forced or
unforced vectors, divisible or rigid, and for comparisons out of selected models or not.

*Proof.* **Step 1 (two-move routes).** Let S, T be disjoint, non-null and contained in the cone over Ω′, with
φ(T) > φ(S). We show 1_T − 1_S ∈ 𝒜_1.

*Choice of constants.*
- Choose η > 0 with (1+η)φ(S) < φ(T).
- By uniform continuity of f and g on cl Ω, choose ε > 0 such that:
  - the 2ε-neighbourhood of Ω′ lies in Ω;
  - |f(x) − f(x′)| and |g(y) − g(y′)| are at most λ := log(1+η)/16 whenever the arguments differ by at most 2ε.
- Put d := ε/4, and choose τ > 0 with (1+τ)² ≤ e^{λ}.

*Matching.* Partition the cone over Ω′ into finitely many cells (cones over squares of side ≤ d). Since
φμ is atomless and Σ(1+η)^{1/2}φ(pieces of S) < φ(T), we can split S and T into finitely many pieces with:
- pairwise disjoint pieces s_m ⊆ S covering S, each inside one cell;
- pairwise disjoint pieces t_m ⊆ T, each inside one cell;
- φ(t_m) = (1+η)^{1/2}φ(s_m) for every m.

The pieces may be split further, so all masses are as small as we like.

*Route for one pair.* Fix a pair (s, t) = (s_m, t_m). Let a = (x_a, y_a) be the centre of s's square, b = (x_b, y_b)
the centre of t's square, and c := (x_b + ε, y_a − ε) ∈ Ω.
- **13-move s → I.** Take I inside the cone over the d-square around c, with ρ_3(I) = (1+τ)ρ_3(s). The threshold
  θ′ := y_a − ε/2 lies strictly between the y-ranges of s and I. By Lemma BB1.1(b), 1_I − 1_s ∈ 𝒜_1.
- **12-move I → t″.** The threshold θ := x_b + ε/2 lies strictly between the x-ranges of I and t. We need
  t″ ⊆ t with ρ_2(t″) = (1+τ)ρ_2(I). Writing min/max over the relevant cells, this is available:
  - required: (1+τ)ρ_2(I) ≤ (1+τ)e^{−min_c f}φ(I) ≤ (1+τ)²e^{−min_c f − min_c g + max_a g}φ(s);
  - available: ρ_2(t) ≥ e^{−max_b f}φ(t) = e^{−max_b f}(1+η)^{1/2}φ(s).

  Cells b and c differ by at most 2ε in x, and cells a and c by at most 2ε in y. So the required mass is at most
  e^{3λ − max_b f}φ(s), which is less than the available mass. By Lemma BB1.1(a), 1_{t″} − 1_I ∈ 𝒜_1.
- **Assemble.** The sum (1_I − 1_s) + (1_{t″} − 1_I) = 1_{t″} − 1_s is ternary, since s ∩ t″ = ∅, so it is
  accepted. Adding the nonnegative vector 1_{t∖t″}, whose support is disjoint from s and t″, gives
  1_t − 1_s ∈ 𝒜_1.

*All pairs.* The vectors 1_{t_m} − 1_{s_m} have pairwise disjoint positive parts and pairwise disjoint negative parts.
By the chaining lemma their sum 1_{∪t_m} − 1_S is accepted. Adding 1_{T ∖ ∪t_m} gives 1_T − 1_S ∈ 𝒜_1. (Different
pairs may use overlapping intermediate sets I; each pair's vector is formed on its own, so this does not matter.)

**Step 2.** Suppose 1_Q − 1_P ∈ 𝒜_1 with φ(Q) < φ(P).
- If Q is null, then −1_P ∈ 𝒜_1, against strict (G).
- Otherwise choose P′ ⊆ P with φ(Q) < φ(P′) < φ(P). Step 1 gives 1_{P′} − 1_Q ∈ 𝒜_1. The sum
  (1_Q − 1_P) + (1_{P′} − 1_Q) = −1_{P∖P′} is ternary, nonzero and ≤ 0, but accepted. That contradicts strict (G).

The last sentence of the theorem is the case P = δ^−, Q = δ^+. ∎

**Corollary BB1.C (PROVED).** Under the hypotheses of BB1.B:
- (a) World 1 has no finite certificate (mode (M1) family) all of whose comparison vectors are supported in the cone
  over Ω′.
- (b) Let ν := φμ on the cone over Ω′ and μ elsewhere. Then ν is bounded (φ is integrable there, since ρ_2 is and
  e^{f} is bounded), it is positive on non-null sets, and it endorses every comparison of world 1 between models that
  differ only inside the cone over Ω′. So no family of relevant comparisons supported there is an infinitary
  obstruction either.
- (c) (Local K26′.) The hypotheses cover two Brier-additive partners (ρ_l = |h_l|) with the Brier selection on the two
  edges at e_1, which is K2's frontier and decoration setting. There f = −log x, g = log y and φ = |h_1|. So on every
  compact link-class box, world 1 is endorsed by the Brier density of world 1 itself, whatever its other comparisons
  and whatever the interior selection.
  - This is the passage from the closed convex hull of the forced cone (KR62) to the acceptance set, on the link class.
  - K2's referee located the missing step of Conjecture K26′ exactly there.
  - The zigzag routes are what close the gap: sums of forced moves never need convexity, because each two-move route
    is itself a ternary sum.

NUMERICS (C) (`saturation_routes.py`, Brier partners): the worst two-move route factor over 20 000 random pairs in
[0.2,0.4]² is 1.350, 1.078, 1.015 and 1.003 for ε = 0.02, 0.005, 0.001 and 0.0002.

**Sketch BB1.8 (not PROVED): from Q_1 to compact parts of R_12 ∪ R_13.** A piece of Q_2 (inside R_12 only) at
12-coordinate x can be routed:
- by a 12-move into Q_1 at a slightly smaller x;
- through Q_1 by zigzags;
- by a 12-move back into Q_2.

If the needed x-values are covered by Q_1^+ ∪ Q_1^−, this gives the conclusion of BB1.B for vectors supported in
compact parts of R_12 ∪ R_13, with φ extended by ρ_2e^{f(x)} on R_12 and ρ_3e^{−g(y)} on R_13. I have not checked:
- the coverage of x-ranges (Q_1^+ has bounded x, Q_1^− unbounded);
- the consistency of the two halves Q_1^±, which have separate f, g.

---

## 5. The positive attempt and where it broke

**Design D (aimed at T1 from the outset).** T1's additive contradiction is a holonomy: exchange rates around the three
corners of D_{T1} that do not compose to 1 (the corner equation x + 1/x = κ + 1 against the box, write-up §8.6(f)
reading of B1 §1). An additive cover fails because one potential cannot carry a non-trivial holonomy. So I tried to
build a world 1 whose acceptance set carries a holonomy defect, located where the T1 corner ray r_23 sits, in the link
class Q_1, by letting its two partners disagree there:
- worlds 2 and 3 additive, with ρ_2 = |h_2| and ρ_3 = |h_3|(1 + κ b(x,y)) on Q_1^+, where b is a continuous bump
  supported in a compact box around (1/(κ+1), 1/(κ+1)), and ρ_3 = |h_3| elsewhere;
- on R_23 the partners are Brier, so the (2,3)-edge Bayes models are the coherent Brier models (Q_1 does not affect
  them, since 2 and 3 agree there), and competitiveness and closed sections on [e_2, e_3] hold;
- selection p ↦ C_p = U ∩ {p·h > 0} on all of Δ (coherent and continuous in measure);
- world 1 the **least** acceptance set making every selected model competitive: the closure under ternary sums of
  the weakly forced vectors and the nonnegative vectors (strict (G) for this set was to come from the divisibility of
  forced vectors, K2.2 and K2.1).

**Intended mechanism.** Every L¹ endorser of the edge-forced moves of world 1 has the form ρ_2H(x) on R_12 and
ρ_3H_3(y) on R_13 (KR62 step (1)). With the bump these two forms cannot agree on the bump region of Q_1. So every
endorser vanishes there, world 1 does not add up, and the obstruction is confined to a fixed compact region of Q_1
away from the coordinate planes: exactly the certificate type the brief prefers.

The infinitary certificate was to have the audit's form 1_{A_n} − 1_{B_0}:
- B_0 fixed in the bump region;
- A_n thin, disjoint, and accumulating at a level set inside the region, not at an end;
- each comparison realised out of a selected edge model by chaining forced moves, hence relevant.

**Where it broke (Theorem BB1.A).** The rate (y/x)(1 + κb) is not separable. So the forced moves themselves pump:
- NUMERICS (A) finds a 4-move cycle of weight 0.55 for κ = 1;
- NUMERICS (B) realises it with genuine sets, with mass ratio ≤ 0.627.

The least acceptance set therefore contains a nonzero nonpositive vector. **No world 1 exists next to these partners
and this edge selection, at all.**
- The divisibility route to strict (G) fails here: K2.1 presupposes a consistent world and only excludes certificates
  inside it.
- The failure does not depend on the recipe for world 1: every world 1 must contain the forced moves (Lemma BB1.1).
- It does not depend on the interior selection either: only edge indices are used.

**Repairs considered, and why each is blocked.**
1. *Make the partners' rate separable but not Brier,* for example ρ_3/ρ_2 = e^{−3x+2y}. Theorem BB1.B then pins
   world 1 to the price φ on every compact link box. There is no room for a certificate there.
2. *Keep a separable rate and add rigid, unforced generators* g_k = 1_{Q_k} − 1_{P_k} out of interior selected
   models, protected as in K2.5 or D2. By BB1.B every such generator supported in a compact link box has φ(Q_k) ≥
   φ(P_k). So the generators are φ-endorsed, and a family of them is never a certificate. Rigidity (K2.1) is
   necessary for a certificate but cannot help on a pinned region.
3. *Protect a region by keeping the forced negative parts out of it* (D2's mechanism: the base cone never moves error
   out of the protected end). This needs a region that the late edge models do not get wrong at world 1. Prop BB1.5
   below shows that such regions retreat to the coordinate planes {h_2 = 0} ∪ {h_3 = 0}: an end device.
4. *Use edge selections whose 12- and 13-error families on Q_1 are not transverse,* so that both families lower the
   same coordinate and the forced moves are acyclic. Then a non-separable rate would give non-adding-up without a
   pump. Prop BB1.6 below shows that coherent edge models make this impossible when K′ is a singleton. I conjecture
   the same for every K′ (BB1.7).

**Proposition BB1.5 (PROVED).** For every coherent model C ∈ M_U, E_1(C) ∩ Q_1^+ is, modulo null sets, the cone over
an up-set of (x,y), independent of r; the same holds on Q_1^−.

Consequently, let (S) hold and p_m → e_2 along the open edge (e_1, e_2) (the same holds at e_3). Then for every box
Ω ⋐ Ω_U, E_1(C_{p_m}) contains the cone over Ω up to a null set for all large m. So any region left free of world-1
errors by the late edge models lies in every neighbourhood of the coordinate planes inside Q_1^+.

*Proof.*
- **Up-set.** C = D_K for a credal set K. Then h = r(1,−x,−y) ∈ Q_1^+ is rejected, which is an error at world 1, iff
  m_1 ≤ m_2x + m_3y for some m ∈ K (boundary null). Since m ≥ 0, increasing x or y preserves this, and r plays no
  role.
- **Q_1^−.** For h = r(−1,x,y), the error is acceptance, iff m_2x + m_3y > m_1 for every m ∈ K. This is again an
  up-set.
- **Late edge models.** Suppose the cone over Ω were not contained in E_1(C_{p_m}) for infinitely many m. The free
  set D_m := Q_1^+ ∖ E_1(C_{p_m}) is the cone over a down-set. If it meets the cone over Ω = (x_0,x_1) × (y_0,y_1) in
  a non-null set, it contains a point (x′, y′) with x′ > x_0 and y′ > y_0, hence the whole cone over
  (0, x_0] × (0, y_0], intersected with Q_1^+.
- That set A is fixed and non-null. Along that subsequence, A ∩ E_1(C_{p_m}) = ∅ for all m, which contradicts Lemma
  K2.7 (proved, refereed once: write-up Lemma K27) applied to the subsequence, since A ⊆ Q_1 ⊆ R_12. ∎

So D2-type protection at world 1, the only known way to block sums of rigid generators, lives at the coordinate planes.
D2's own protected end contains the axis ray R_+(1,0) (Lemma F11 in the write-up).

**Proposition BB1.6 (PROVED; K′ = {k} a singleton in Δ°).** Let C = D_K be a coherent edge-(1,2) model, i.e. by Lemma
Q34 correct at worlds 1 and 2 off R_12. Then:
- every m ∈ K whose boundary line {m_1 = m_2x + m_3y} meets Ω_U has normal (m_2, m_3) with m_2/m_3 > k_2/k_3;
- for every coherent edge-(1,3) model the corresponding ratio is < k_2/k_3.

So on Q_1^+ the error-set boundaries of the two edge families are strictly transverse.

*Proof.* C accepts every h ∈ U with h_1, h_2 > 0 > h_3. So each m ∈ K lies in the dual of
cl U ∩ {h_1 ≥ 0, h_2 ≥ 0, h_3 ≤ 0}, which is cl(cone{k} + cone{e_1, e_2, −e_3}) (bipolar theorem). Write
m ∝ αk + βe_1 + γe_2 − δe_3 with α, β, γ, δ ≥ 0 and m_3 = αk_3 − δ ≥ 0. Then the ratio is

  m_2/m_3 = (αk_2 + γ)/(αk_3 − δ) ≥ k_2/k_3,

with equality iff γ = δ = 0. In that case m ∈ co{k, e_1}, and m·h = αk·h + βh_1 > 0 on Q_1^+ ∩ U, so its line does not
meet Ω_U. The 13-edge case is the mirror. ∎

With a singleton K′, non-transverse edge families are therefore unavailable, and BB1.A or BB1.B applies whenever (TH)
is replaced by the actual coherent families. That replacement is **CONJECTURE BB1.7**: the zigzag of BB1.B needs
only two transverse families of up-set boundaries sweeping the box, together with closed sections and strict (G) on the
edges (which give the sweep, as in Prop Q35(1) under nesting). I have not written the curvilinear version, and
nesting of the edge families is not automatic.

---

## 6. What any construction of the requested kind must do, and the proposed shift of aim

**Theorem BB1.D (PROVED, from BB1.A–C).** Let a ranking on M_U satisfy (S) and strict (G), (IB) at world 1. Let the
selection be of Brier type on the two edges at e_1 (TH). Suppose world 1 has a certificate, finite or infinitary,
confined to a compact box of its link class away from the coordinate planes. Then at least one partner world, 2 or 3,
violates (E2) or (E3) on that box: its comparisons out of its edge models into models that differ from them inside the
box are endorsed by no continuous positive density.

In particular, the system needs at least **two** worlds that are not continuously endorsable near Q_1: world 1 itself,
and one partner.

*Proof.* Otherwise BB1.A gives a separable rate and BB1.C(a), (b) exclude the certificate. ∎

**Readings for T1** (CHECKED as readings, not theorems).
- **Location.** The corner ray r_23 lies in Q_1^+ at (x,y) = (1/(κ+1), 1/(κ+1)), inside Ω_U for every K′ ⊆ relint
  T1, away from the coordinate planes. Cyclically, r_31 ∈ Q_2 and r_12 ∈ Q_3.
- **Consequence for absorption.** In a T1 cover whose selection is Brier-type on the edges at e_i, world i can carry a
  non-additive comparison near its own corner ray only if a partner of world i is not continuously endorsable there.
- **Where T1's cycle can be absorbed.** The holonomy cannot be absorbed by one non-additive world between two
  continuously endorsable partners: BB1.A forbids a holonomy defect between such partners, and BB1.B forbids
  non-additive comparisons in the link class. This matches, from the construction side, T2n.3's finding that
  sheltering sits on the pair of non-(CA⁺) worlds.
- **Hypotheses.** These readings need (TH) at the relevant vertex; T1 covers are not known to have Brier-type edges
  (CONJECTURE BB1.7 would remove this).

**Why the competitive coherent family could still admit T1 in a construction that escapes BB1.D.** Nothing here
constrains the interior selection: BB1.A–C use only edge indices. A system escaping BB1.D has a partner, say world 2,
whose comparisons out of 12-edge models are not continuously endorsable on the box. Its edge and interior selections
are then not tied to the Bayes family of any continuous field. That is the freedom AA2 identified as necessary for
filling prescribed boundary data, and the freedom T1 needs: Theorem gm excludes T1 from every additive Bayes family.

**Proposed shift of aim (the nearby reachable target).** The requested three-world construction reduces, at a link
box, to a **two-world edge question**:

> **Q_box.** On an edge region R_12 (two worlds; the third world additive and continuous, supplying the 13-moves of
> world 1), is there a full edge system in which, on a fixed compact box B ⊆ Q_1 away from the chain ends:
> - world 2's comparisons out of edge models into B are not continuously endorsable, and
> - world 1's are not either,
> while competitiveness and closed sections hold on the edge?

All known non-endorsable two-world systems put their failure at the chain ends:
- D2;
- P1 ⊕ mirror (T2n.1);
- by Prop D2sigma, D2 has a σ-finite endorsing density, continuous on every compact part of M away from the end.

So they satisfy (E2) on every compact box, and Q_box is genuinely new. My recommendation for the next round:
- **Positive side:** attack Q_box with the transition-record language of AUDIT_nonlinear_programme. The box is where
  both worlds must refuse the zigzag. BB1.B shows that one refusing world is not enough.
- **Negative side:** attempt the curvilinear BB1.7. Together with a negative answer to Q_box, it would show that every
  non-adding-up world of a full three-world system on M_U is an end device. Combined with M0closed, that would put
  every T1 cover's non-additivity at ends.

**Not reached.** No closed-section verification was attempted (exact consistency test, X1 plans), because the
obstruction found is upstream of closed sections: it already lives in strict (G), (IB) and competitiveness at edge
indices.

---

## 7. Status, dependencies, what a referee should check, files

**Dependencies (all proved earlier, with their reading counts):**
- N17.1(a),(b): the acceptance-set normal form and the chaining lemma;
- write-up Lemma Q34 (edge models are correct at one of the two edge worlds);
- write-up Lemma K27 (= K2.7; refereed once);
- Lemma B10, only for the remark that leading densities give (E2).

BB1.A–C use no other result.

**Referee targets.**
1. Lemma BB1.1: the sign bookkeeping on Q_1 (worlds 2 and 3 both opposite to world 1), and that X agrees with C_q off
   Q_1.
2. Lemma BB1.2: the choice of disjoint sets when the cycle revisits a cell, and the worst-case mass bound in 13-steps.
3. Lemma BB1.3: the reachability step inside the open box, and the extension of f, g from the co-countable good sets
   (continuity of v is used here).
4. Theorem BB1.B Step 1: the inequality "required ≤ available" in the 12-move, and that all intermediate cells stay in
   Ω.
5. Prop BB1.5: the down-set step "meets the cone over Ω non-nullly ⇒ contains the cone over (0,x_0] × (0,y_0]".
6. Scope: (TH) is a hypothesis on the selection; continuity of ρ_2, ρ_3 is a hypothesis on the partners. The
   measurable-density version of BB1.A/B is open (I expect it from Lebesgue density points, but it is **not
   claimed**).

**Files (`bb1py/`, run with `python3 -I`).**
- `pump_grid.py` → `pump_grid.out`: NUMERICS (A), exact longest-path search for positive cycles of the move graph on a
  21 × 21 grid. It finds no cycle for the separable rates and a positive cycle for the two non-separable ones. It
  takes about 90 seconds.
- `pump_masses.py` → `pump_masses.out`: NUMERICS (B), realising the 4-move pump with Gaussian cell masses and
  worst-case density ratios, and checking that all cells lie in U for K′ = u + 0.1(T1 − u), ε = 0.3.
- `saturation_routes.py` → `saturation_routes.out`: NUMERICS (C), two-move route factors for Brier partners, tending
  to 1.
