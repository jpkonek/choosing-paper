# PP62. A record-based refusal allocation, and what openness forces on any such allocation

23 October 2026. Constructor, Brief 54. One author; not refereed. Takes in the coordinator's relay of REFEREE_round53 (§3.3, §6.3–6.4, §7). No axiom is added; extra hypotheses are named where they enter.

**Labels.** PROVED: complete argument here, or a cited result used within its stated hypotheses. CHECKED: exact integer computation in `r9/PP62_py/` (ends ALL PASS). NUMERICS: Monte Carlo, used only where said. CONJECTURE / OPEN: as stated.

---

## DRAFT RULE (posted first for PP63; unchanged in the final version)

u¹ is PP56's balanced field (§1.2 below fixes the family it is built from). For an ordered record r = rec(X, Y):

  V_w(r) := ∫_{X≠Y} [u¹_w(g, Y(g)) − u¹_w(g, X(g))] dμ,  w = 1, 2, 3.

Fix the world w₀ := 2.

**Rule R₀.**
- r null: R₀(r) = ∅.
- V(r) ≠ 0: R₀(r) = {w : V_w(r) < 0}.
- r non-null and V(r) = 0 (a **null record**): R₀(r) = {w₀}.

X ⪯_w Y iff w ∉ R₀(rec(X, Y)). On a null record both directions are refused at w₀ (single-world incomparability) and both are accepted at worlds 1 and 3 (ties). Every ordered record of measurable four-advice models receives a verdict: **nothing is unassigned.**

---

## 0. Verdict

1. **The hint's candidate, built exactly (Theorem R; PROVED, CHECKED).** R₀ is the balanced first level of Λ with no tie-breaks. Its null records are made single-world incomparable at w₀ and tied elsewhere.
   - It satisfies, on **every** triangle of measurable models: reflexivity, (IB), strict (G) and (TC).
   - It gives every member of the family defence, exact undominatedness and direct (C) against **every** measurable rival.
   - On each balanced swap, the forward and reverse records are refused at the same world. That pattern has the α-certificate α = (1, 1), so **no common q certifies it**, and by the referee's Prop A″ no reweighted Λ_q has these refusals open.
2. **Where its sections fail, exactly (Theorem P; PROVED).** For a fixed rival X, the refusal set {a : w ∈ R₀(rec(C_a, X))} is open at every source except one kind of point: a source a whose record with X is a non-null null record, at world w₀, where members arbitrarily close to a, outside that fibre, are at least as good as C_a at w₀ under u¹ (condition (★) of §3.1 fails). For each X these points form the fibre {a : Φ(C_a) = Φ(X)}. At every interior source of the family this fibre is non-empty for many X.
3. **A two-dimensional module on which everything holds, including openness, and weights fail (Theorem M; PROVED).** Take a compact family N with interior, made of two lobes around u and B. Each lobe is cut so that its centre strictly minimises Φ_{w₀}. On N, R₀ satisfies every clause in scope, including open refusals:
   - all of PP57's overlapping balanced swaps between u and B (any measurable F⁺ ⊆ Ep, F⁻ ⊆ Em of equal mass);
   - their reverses;
   - all common-context copies and all triangles;
   - every rival that is not an h/S-variant of a non-centre member with the same Φ.

   Those balanced swaps carry inverse refusals at the same world, so this is the audit's outcome **(W¬R): weights fail, the relation survives.**
4. **The limitation is real, and it is not Theorem Q (Theorem E; PROVED at a = u, NUMERICS elsewhere).** Take any allocation whose acceptances out of members are **endorsed by u¹** (accepted ⇒ V_w ≥ 0). R₀ is one; so is every "Λ₀ + refusal penalty" rule. Such an allocation cannot have closed sections at an interior member that has a balanced member swap.
   - The proof uses only (IB), direct (C), defence, openness and pure-shift geometry. It uses no (TC) and no (G).
   - Theorem Q excludes the *lower* envelope ({V_w > 0} ⊆ Acc). Theorem E excludes the *upper* envelope (Acc ⊆ {V_w ≥ 0}).
   - A splitting lemma (Lemma S; PROVED) ties the two together under (TC).
   - **Consequence (Cor E.2, axiom-level given the geometry).** Any allocation with closed sections near u must contain *u¹-unfavourable acceptances* out of shifted members. For every one of them it must also refuse a u¹-favourable split of its reverse, or accept the reverses of both halves of that split.
   - So the interior target is not reachable by any rule of R₀'s kind. **The block is an artefact of endorsement, not an axiom-level obstruction.**
5. **Status of the audit's target.**
   - Reached on the extremal module: compact, 2-D, overlapping measurable balanced swaps, open refusals, defence/protection/(TC)/(IB) everywhere, α-certificate.
   - **Not reached** for balanced swaps out of *interior* members. Theorem E says which rules cannot reach it, and Cor E.2 specifies, as germ literals at u, what a rule that does must contain.

| Item | Result | Label |
|---|---|---|
| Direction lemma: monotone answer regions; signs of the record vector by world order | Lemma 1.1 | PROVED |
| Balanced member swaps live on the middle world's points | Cor 1.2 | PROVED |
| Pure-shift layer formula; Γ(u, u_t^w) ∈ O_w exactly | Lemma 1.3 | PROVED (symmetry); NUMERICS at B, D and a₁ |
| R₀: (IB), reflexivity, strict (G), (TC) on all triangles; defence, undominatedness, direct (C) for all members against all rivals | Thm R | PROVED; CHECKED (`r0_check.out`) |
| Exact location of R₀'s non-closed sections | Thm P | PROVED |
| Extremal module: all clauses including openness; α = (1, 1) | Thm M | PROVED |
| Endorsement obstruction | Thm E | PROVED at u; general form under (H_Γ) |
| Splitting lemma | Lemma S | PROVED |
| What an interior solution must contain | Cor E.2 | PROVED (given Lemma 1.3) |
| A rule with open refusals for balanced swaps out of interior members | — | OPEN |

---

## 1. Setting, notation, and three geometric facts

### 1.1 Records

The setting is Brief 54's: three worlds; Gaussian μ; four advice values; ranks 0 < 1 < 2 < 3; ε = 3/10; C_a = D_{M_a}, with index = likelihood.

The index region where (2V) holds is 𝒢 = {a : normalise(1/a) ≥ c coordinatewise} (REFEREE_round53 1a). u and B lie in its interior. Fix η > 0 so small that u and B are interior to 𝒮₀ := {a : normalise(1/a) ≥ c + η}. Throughout:
- u¹ is PP56 §4.1's level-0 field for the family 𝒮₀;
- R := R(𝒮₀) is its disagreement region;
- h(g) is the common answer (the sign of g₁ + g₂ + g₃ under (2V)).

Every family N used below is a subset of 𝒮₀.

The properties of u¹ used (PP56 Thm L proof; REFEREE_round53 1b):
- **(U1)** |u¹| ≤ K|g| and u¹_w is strictly increasing in the w-rank, at every g and over all four values;
- **(U2)** every member is pointwise λ-Bayes with λ = (1, 1, 1): λ·[u¹(g, x) − u¹(g, C_a(g))] ≥ 0;
- **(U3)** equality in (U2) holds exactly for g ∈ R and x ∈ {h, S}.

Put Φ(Y) := ∫ u¹(g, Y(g)) dμ ∈ R³, which is finite by (U1). Then V(rec(X, Y)) = Φ(Y) − Φ(X).

Write H for the set of models that equal the common advice off R and lie in {h, S} on R. The H-records are the records between members of H.

**Odd worlds.** Each g ∈ R has mixed signs. So h is correct at exactly one world, or wrong at exactly one; call that world the **odd world** o(g).
- On an H-record, changing the advice at g moves the u¹-loss vector by ±|g|ε_{o(g)}, where ε_i := (1, 1, 1) − 3e_i. This is PP57's (−2, 1, 1) / (2, −1, −1).
- The sign is + when the new side *improves* its odd world: it answers a point with Cor = {o}, or silences a point with Wr = {o}.
- Let c_i(r) be the |g|-mass of the changed odd-world-i points that improve world i, minus the mass of those that worsen it. Then

  V(r) = Σ_i c_i(r) ε_i,  so V(r) = 0 ⇔ c_1(r) = c_2(r) = c_3(r).   (1.1)

### 1.2 Lemma 1.1 (direction lemma; PROVED)

Let a, b ∈ 𝒮₀ and d := log(b/a) (defined modulo (1, 1, 1)).
- (i) If d_o ≥ d_i for all i, then on {C_a ≠ C_b} every odd-world-o point has C_b improving world o relative to C_a. So c_o(rec(C_a, C_b)) ≥ 0, and every non-null piece contributes strictly.
- (ii) If d_o ≤ d_i for all i, every odd-world-o point has C_b worsening world o, and c_o ≤ 0.

*Proof.* C_a answers h at g iff s_v(a) := Σ_i a_i m_{v,i} h_i > 0 for all three vertices v (PP50 library; under (2V) no member answers −h).
- **Points with Cor = {o}.** Here h_o > 0 and h_i < 0 for i ≠ o. In case (i), s_v(b) ∝ e^{d_o}a_o m_{v,o}h_o + Σ_{i≠o} e^{d_i}a_i m_{v,i}h_i ≥ e^{d_o}s_v(a), because each negative term is multiplied by e^{d_i} ≤ e^{d_o}.
  - So C_b answers wherever C_a answers among these points: they can only be **gained**, and answering a Cor = {o} point improves o.
- **Points with Wr = {o}.** Here h_o < 0 and the other two coordinates are positive. The same estimate with −d shows that the answer region is up-closed under directions whose o-coordinate is minimal. So in case (i) these points can only be **lost**, and silencing a Wr = {o} point improves o.
- Case (ii) is symmetric. ∎

**Corollary 1.2 (PROVED).** Let F ⊆ {C_a ≠ C_b} be non-null with V(F : C_a → C_b) = 0. Then, a.e., F consists of odd-world-m points, where m is the strictly middle coordinate of d, with c_m(F) = 0. If d has no strictly middle coordinate (two coordinates tie as max or as min), no such F exists.

*Proof.* By (1.1), c_1 = c_2 = c_3 = γ. Lemma 1.1 gives c_max ≥ 0 ≥ c_min, so γ = 0. Each of c_max and c_min is a sum of same-signed contributions, so the max-world and min-world parts of F are null. ∎

For u → B, d ∝ (log 406, log 421, log 373): the max is world 2, the min world 3, the middle world 1. PP57's balanced swaps F = F⁺ ∪ F⁻ (F⁺ ⊆ Ep, Wr = {1}; F⁻ ⊆ Em, Cor = {1}; equal |g|-mass) are of exactly this kind. Pure shifts u → u∘(1 + te_w) have tied min coordinates, so **pure-shift pairs have no balanced swaps.**

### 1.3 Lemma 1.3 (pure-shift layers; PROVED at u, NUMERICS elsewhere)

For interior a, w ∈ {1, 2, 3} and t > 0, put a_t := a∘(1 + te_w) (normalised), and

  Γ(a, a_t) := V(rec(C_{a_t}, C_a)) = Φ(C_a) − Φ(C_{a_t}).

Let α be the |g|-mass of the odd-world-w points of the layer {C_a ≠ C_{a_t}}, and β_v the mass of its odd-world-v points (v ≠ w). Write w′, w″ for the two other worlds.

(a) **(PROVED.)**

  Γ_w = 2α + β_{w′} + β_{w″} > 0,  Γ_{w′} = −α − 2β_{w′} + β_{w″},  Γ_{w″} = −α − 2β_{w″} + β_{w′}.

(b) **(PROVED.)** At a = u, Γ(u, u_t) ∈ O_w := {x : x_{w′} < 0 and x_{w″} < 0} for every w and every t > 0.

(c) **(NUMERICS, `gamma62.out`.)** At a = u, B, D and a₁ = (0.34, 0.335, 0.325), for all six pure shifts: Γ/t ≈ 0.2·(3e_w − 1) for shifts toward e_w, which lies in O_w with margin about 0.3. The map a ↦ Φ(C_a) has Jacobian rank 2, with singular values about 0.9 and 0.5.

*Proof.*
- **(a).** d = e_w has max world w and the other two tied at the min. By Lemma 1.1, c_w(rec(C_a, C_{a_t})) = α and c_v = −β_v for v ≠ w. Apply Γ = −Σ_i c_i ε_i. The layer is non-null (Lemma 4.1, with the referee's repaired wording) and lies in R. So α + β_{w′} + β_{w″} > 0 and Γ_w > 0.
- **(b).** Take w = 1, and let τ swap the coordinates 2 and 3 of g.
  - τ preserves μ and |g|.
  - It permutes the vertices of M, and it fixes the indices u and u_t = u∘(1 + te₁).
  - So the layer is τ-invariant, and τ maps odd-world-2 layer points to odd-world-3 layer points. Hence β₂ = β₃ =: β.
  - By (a), Γ₂ = Γ₃ = −α − β < 0.

  Worlds 2 and 3 are handled with the transpositions (1 3) and (1 2). ∎

---

## 2. Theorem R: R₀ satisfies every non-section clause, on all records

**Theorem R (PROVED).** Let N ⊆ 𝒮₀. Then R₀ satisfies:
- (IB) and reflexivity;
- strict (G) on every record at every world;
- (TC) for every triangle of measurable models (hence for every reverse record, every mixed triangle and every common-context copy);
- for every a ∈ N and every measurable X ≠ C_a:
  - **defence:** R₀(rec(C_a, X)) ≠ {1, 2, 3};
  - **protection:** R₀(rec(X, C_a)) ≠ ∅.

  So exact undominatedness holds vacuously, and direct (C) holds for coherent and incoherent X alike.

*Proof.*
1. **(IB) and reflexivity.** R₀ is a function of the record. Null records receive ∅.
2. **Null records are mixed at every world.** On a non-null record the two sides differ at every point of the support, and ranks are injective in the advice. So at each world each support point is strictly better or strictly worse for the new side. If the new side were pointwise worse at w, (U1) would give V_w > 0.

   Hence a non-null record with V = 0 is mixed at every world, and (G) never applies to it.
3. **Strict (G).** Suppose the new side is pointwise weakly w-worse on a non-null record. Then it is strictly worse on the whole support (step 2), so V_w > 0. Then V ≠ 0 and w ∉ R₀, so the comparison is accepted. The reverse has V_w < 0, so it is refused.
4. **(TC).** Let X ⪯_w Y, Y ⪯_w Z, Z ⪯_w X with records r₁, r₂, r₃. Then V(r₁) + V(r₂) + V(r₃) = Φ(Y) − Φ(X) + Φ(Z) − Φ(Y) + Φ(X) − Φ(Z) = 0.
   - An accepted link has V_w ≥ 0: either V ≠ 0 and w ∉ {V_w < 0}, or V = 0.
   - Three non-negative numbers sum to zero, so every V_w(r_k) = 0.
   - The reverse r_k⁻ has V(r_k⁻) = −V(r_k).
     - If V(r_k) ≠ 0, then V_w(r_k⁻) = 0 is not negative, so the reverse is accepted.
     - If V(r_k) = 0 and r_k is non-null, acceptance of r_k at w means w ≠ w₀. Since R₀(r_k⁻) = {w₀} as well, the reverse is accepted.
     - Null links are trivial.
5. **Defence and protection.** Let r = rec(C_a, X), non-null. By (U2), Σ_w V_w(r) = ∫ λ·[u¹(X) − u¹(C_a)] ≥ 0.
   - **If V(r) ≠ 0.** Some coordinate is ≥ 0, so r is accepted there (defence). Some coordinate is > 0: otherwise all are ≤ 0 with a non-negative sum, so all vanish. At that world V_w(r⁻) < 0, so the reverse is refused (protection).
   - **If V(r) = 0.** r is accepted at 1 and 3, and R₀(r⁻) = {w₀}. ∎

**Remarks.**
1. **Which records are null.** By (U2)–(U3), a record out of a member has V = 0 only if it is an H-record: the rival equals the common advice off R and lies in {h, S} on R. So for every rival X ∉ H, R₀ coincides with Λ₀ (the u¹-sign rule) on the records out of members.
2. **Derived clauses.** Every SAFE clause of PP59 (PP19 Thms 1, 4(a)(b), 5; Prop S; PP30 Thm 3.1; PP33; Prop K and K^S) is derived from reflexivity, (G), (IB), (TC) and members' defence. So R₀ satisfies all of them, for the same reason as PP56 Cor 4.3.
3. **(LA)** holds because T = C_u is a member and is protected, as in Theorem L. I have not re-derived it separately.

**CHECKED (`PP62_py/r0_check.py`, `r0_check.out`, exact integers, ALL PASS).** The instances are PP56's actual kink cells, with m(above) = m(below) so that balanced records occur:
- [I1] 18 cells with values {h, S}, 2¹⁸ rivals: defence and protection for A and the proxies A^B, A^D.
- [I2], [I3], [I4] (six pieces with {h, S}; three pieces with four values; all masses equal). Exhaustively checked:
  - reflexivity, strict (G) on every pair at every world, and (IB) on 729 or 2,197 record classes;
  - (TC) on every ordered triple at every world;
  - the members' obligations.
- Single-world incomparabilities occur only on null records, and only at w₀: 16, 48, 16, 9, 4, 4 and 141 incomparable pairs across the seven instances. Ties occur.
- [α] On A → A[Ep ∪ Em ↦ S]: R₀ refuses both directions at w₀ = 2, and the pointwise sum of the two refusal increments is 0.

---

## 3. Openness

### 3.1 Theorem P (exact location of non-closed sections; PROVED)

Fix a measurable rival X and a world w. Let Z_X := {a ∈ N : C_a ≠ X, V(rec(C_a, X)) = 0}. The set Ref := {a ∈ N : w ∈ R₀(rec(C_a, X))} is relatively open in N at every point except the points a ∈ Z_X with w = w₀ that fail

  (★) some neighbourhood U of a in N has Φ_{w₀}(C_{a′}) > Φ_{w₀}(C_a) for every a′ ∈ U ∖ Z_X.

At every **interior** point of N lying in Z_X, (★) fails.

*Proof.* The map a ↦ V(rec(C_a, X)) = Φ(X) − Φ(C_a) is continuous, by continuity in measure of a ↦ C_a and the envelope K|g| (dominated convergence, as in the robust refusal lemma).
- **Case V(rec(C_a, X)) ≠ 0 and w ∈ Ref.** Then V_w < 0 at a, and also near a; there V ≠ 0, so w ∈ R₀.
- **Case a ∈ Z_X.** Then w ∈ Ref iff w = w₀. For a′ near a, either a′ ∈ Z_X (refused at w₀), or V_{w₀}(rec(C_{a′}, X)) = Φ_{w₀}(C_a) − Φ_{w₀}(C_{a′}), which is refused iff it is negative. That is (★).
- **Interior points.** Take a′ = a∘(1 + te_{w₀}). Lemma 4.1 and (U1) give Φ_{w₀}(C_{a′}) < Φ_{w₀}(C_a). So a′ ∉ Z_X (its Φ differs from Φ(X) = Φ(C_a)), and it accepts at w₀. ∎

So R₀'s section failures are exactly the **non-null null records out of members that are not strict local minimisers of Φ_{w₀}**. For a given X, they sit on the single Φ-fibre over Φ(X). Compare Λ (PP56 Prop 5.1): Λ also fails on rivals with V_w = 0 and V ≠ 0, through its tie-breaks. R₀ accepts both directions there and is open.

### 3.2 The extremal family and Theorem M (the module)

**Construction.** For c ∈ {u, B} and constants ρ, κ > 0, put

  N_c := {a ∈ 𝒮₀ : |a − c| ≤ ρ,  Φ₂(C_a) − Φ₂(C_c) ≥ κ|a − c|},  N := N_u ∪ N_B.

**Lemma 3.1 (PROVED).** For small ρ and κ:
- (i) N is compact and each lobe has non-empty interior;
- (ii) c is the unique minimiser of Φ₂ on N_c, and (★) holds at u and at B for every X;
- (iii) Φ(N_u) ∩ Φ(N_B) = ∅.

*Proof.*
- **(i).** N_c is closed (Φ is continuous) and bounded. Let a₁ := c∘(1 − se₂), normalised, with s small. Then c is a pure 2-shift of a₁, so C_c is pointwise better at world 2 than C_{a₁}, strictly on a non-null set. By (U1), δ := Φ₂(C_{a₁}) − Φ₂(C_c) > 0. Take κ < δ/(2|a₁ − c|) and ρ > |a₁ − c|. By continuity, a neighbourhood of a₁ satisfies the defining inequality strictly.
- **(ii).** For a ≠ c in N_c, Φ₂(C_a) ≥ Φ₂(C_c) + κ|a − c| > Φ₂(C_c). This gives (★) at c, since the other lobe is at positive distance once (iii) holds.
- **(iii).** It suffices that Φ(C_u) ≠ Φ(C_B), and then to take ρ small.
  - {C_u ≠ C_B} contains odd-world-3 cells: for instance the cells with sign (−1, −1, 1) and advice (P, S, ·) or (S, M, ·) (`PP56_py/cells56.out`).
  - World 3 is the min coordinate of log(B/u). By Lemma 1.1(ii), c₃ < 0 strictly, while c₂ ≥ 0. So c is not a multiple of (1, 1, 1), and V ≠ 0 by (1.1). ∎

**Theorem M (PROVED).** On N, with w₀ = 2, rule R₀ satisfies every clause of the module on the following scope.
- **Sources:** all a ∈ N. This is a compact family with non-empty interior, containing T = C_u and B.
- **Rivals:** every measurable X with Z_X ⊆ {u, B}. These include:
  - (a) every X ∉ H;
  - (b) **every balanced rival of u or B**. In particular, the overlapping measurable swap family X_F := C_u[F ↦ C_B] and the reverses Y_F := C_B[F ↦ C_u], for every F = F⁺ ∪ F⁻ with F⁺ ⊆ Ep and F⁻ ⊆ Em measurable and m(F⁺) = m(F⁻) > 0. These F are non-conic as soon as they are not a.e. cones, and they overlap and share pieces arbitrarily;
  - (c) every H-rival X with Φ(X) ∉ Φ(N ∖ {u, B}). This includes every unbalanced X_F whose Φ-value leaves Φ(N).
- **Records:** every record between any two measurable models, so every reverse, every mixed triangle and every common-context copy.

On this scope the following hold:
- reflexivity, (IB), strict (G) and (TC) (Thm R, on all triangles);
- defence, exact undominatedness and direct (C) for every source (Thm R);
- open refusal sets for every fixed rival in scope and every world (Thm P with Lemma 3.1(ii)). In particular, C_u ⋠₂ X_F holds for all a in a neighbourhood of u, for every balanced F, and likewise C_B ⋠₂ Y_F near B.

**Prescribed refusals and their α-certificate (PROVED).** For each balanced F, R₀ prescribes:
- C_u ⋠₂ X_F, with increment d_F := u¹₂(X_F) − u¹₂(C_u);
- C_B ⋠₂ Y_F, with increment d′_F := u¹₂(Y_F) − u¹₂(C_B).

By (IB), rec(C_B, Y_F) is the reverse of rec(C_u, X_F), so d′_F = −d_F pointwise. Hence α = (1, 1) gives d_F + d′_F = 0 ≥ 0 a.e., and by the alternative theorem (REFEREE_round53 Thm A) **no bounded q ≥ δ > 0 gives both ∫ q d_F < 0 and ∫ q d′_F < 0**.

For a compact parameterised family F_s, the certificate is the measure ν = δ_{(s, fwd)} + δ_{(s, rev)} for any single s. No sampling is involved (cf. the referee's §6.4).

By the referee's Prop A″, no reweighted relation Λ_q, with any tie-breaks, has these two refusals open. In the referee's world table (§6.1) the assignment (w, v) = (2, 2) is an α-cell. **This is outcome (W¬R).**

**Unassigned records: none.** All records are assigned. The scope excludes only rival–source pairs, and only for the openness clause: pairs (a, X) with a ∈ N ∖ {u, B}, X ≠ C_a and Φ(X) = Φ(C_a). For interior a this exclusion is unavoidable for R₀ (Thm P), and §4 shows it is unavoidable for every u¹-endorsed rule whenever the null record is a balanced member swap.

**Why this is not a killed architecture, and what the escape really is.**
- **Not a gate union.** Acceptances are not realiser-gated.
- **Not the kernel ℓ^T.**
- **Not lexicographic.** There are no later levels.
- **Locally endorsed by u¹, so M0-type.** The referee's §7 says no *local* exclusion of M0 was established. Theorem E below now gives one for interior modules. A full cover would still have to escape the full-cover theorems (M0closed, Q4.1–Q4.2, L4/R21).
- **R₀ does satisfy (L0⁺) for u¹, so Theorem Q applies to it.** Theorem Q(ii) needs Q(i) at all three worlds, including w₀ = 2, and Q(i) at w₀ uses the pure shifts u∘(1 + te₂). In N those shifts do not exist: by construction they lower Φ₂ and so leave N_u. At worlds 1 and 3, Q(i) asks only that C_u ⪯ X_F, and R₀ grants that as a tie.

  **So the module escapes Theorem Q through the shape of the family, not through the relation.** I state this plainly: Theorem M is a genuine 2-D module with overlapping balanced swaps and a q-infeasible refusal pattern. Its balanced swaps sit at the two Φ₂-extremal members, not at interior ones.

---

## 4. Theorem E: openness forces non-endorsed acceptances

**Hypothesis (H_Γ) for an endorsing field ψ** (an integrable field with world components ψ_w, and Γ^ψ defined from it as Γ is from u¹). At the interior member a, for each w and all small t > 0, Γ^ψ(a, a∘(1 + te_w)) ∈ O_w.

For ψ = u¹ and a = u this is Lemma 1.3(b) (PROVED). At B, D and a₁ it is NUMERICS (Lemma 1.3(c)).

**Theorem E (PROVED under (H_Γ); unconditional for ψ = u¹ at a = u).** Let a be interior to N, b ∈ N, and F ⊆ {C_a ≠ C_b} non-conic with Ψ(F : C_a → C_b) = 0 at all three worlds. Put X := C_a[F ↦ C_b] and Y := C_b[F ↦ C_a].

There is no allocation satisfying all of the following at once:
- (IB) on rec(Y, C_b) = rec(C_a, X);
- direct (C) for C_b against Y;
- defence of the members a∘(1 + te_w) against X;
- closed fixed-rival sections at a for X;
- **endorsement**: C_{a′} ⪯_v X ⇒ Ψ_v(rec(C_{a′}, X)) ≥ 0, for a′ near a.

*Proof.*
1. Y differs from the coherent C_b on the non-conic F, so Y is incoherent (Lemma H). Direct (C) then gives a world w with Y ⋠_w C_b. By (IB), C_a ⋠_w X.
2. Openness gives C_{a_t} ⋠_w X for a_t = a∘(1 + te_w) and all small t (a is interior, so a_t ∈ N).
3. Defence of C_{a_t} gives some v ≠ w with C_{a_t} ⪯_v X. By endorsement, Ψ_v(rec(C_{a_t}, X)) ≥ 0.
4. But by additivity, Ψ(rec(C_{a_t}, X)) = Ψ(rec(C_{a_t}, C_a)) + Ψ(rec(C_a, X)) = Γ^ψ(a, a_t) + 0.
5. (H_Γ) makes both coordinates v ≠ w negative. Contradiction. ∎

No (TC), no (G), no completeness and no single-world-tie assumption is used.

**Corollary E.1 (PROVED).** Take any module on a closed 2-D neighbourhood containing u in its interior and B (for instance PP57's N_u), with PP57's balanced swap X = C_u[F ↦ C_B]. No allocation on it whose acceptances out of members near u are u¹-endorsed has closed sections at u.

This covers:
- R₀;
- every rule of the form "accept iff V_w ≥ ρ_w" with ρ ≥ 0, which was my first design (§5);
- Λ₀ with any tie treatment;
- every intersection of additive rankings that contains u¹ as one of its rankings.

So **M0 with the endorser u¹ is excluded locally.** This complements the referee's §7.

**Lemma S (splitting; PROVED).** Let X ⪯_w Y be accepted with V_w(rec(X, Y)) < 0. Choose E ⊆ supp rec(X, Y) such that, with Z := X[E ↦ Y], both V_w(rec(Y, Z)) and V_w(rec(Z, X)) are positive. Such an E exists by Lyapunov, because the two values sum to −V_w(rec(X, Y)) > 0.

Then (TC) forces: either Y ⪯_w Z or Z ⪯_w X is refused, or both Z ⪯_w Y and X ⪯_w Z (each with V_w < 0) are accepted.

*Proof.* The triangle X → Y → Z → X has records summing to zero. If all three links are accepted, (TC) demands the three reverses. ∎

Consequently a relation that accepts every record with V_w > 0 (the global form of (L0⁺)) has all its acceptances at w endorsed by u¹. Theorem E then applies. This gives a second route to Q-type failures, and shows the two envelopes are linked.

**Corollary E.2 (what any interior solution must contain; PROVED given Lemma 1.3(b)).** Suppose an allocation satisfies (IB), defence, direct (C) and (TC), with closed sections at u, on a module containing u in its interior, B, X = C_u[F ↦ C_B] and the records out of the pure shifts u_t^w = u∘(1 + te_w). Let w be a world refusing C_u ⪯ X (one exists by C_B's direct (C)). Then for every small t > 0:
- **(i)** C_{u_t^w} ⋠_w X, and C_{u_t^w} ⪯_v X for some v ≠ w, although V_v = Γ_v(u, u_t^w) = −(α_t + β_t) < 0. This is a **u¹-unfavourable acceptance**, a germ literal γ(u, X, v, e_w) along the pure shift.
- **(ii)** For each such acceptance and each split E as in Lemma S, the allocation refuses a u¹-favourable split comparison at v, or accepts two more u¹-unfavourable comparisons.

So a solution must leave both envelopes of u¹ at the worlds v ≠ w, near u. This is the precise sense in which "Theorem Q needs refusals of favourable comparisons" (PP57 §5) must be complemented by *acceptances of unfavourable ones*.

**Is the block axiom-level?** No, as far as anything shown here goes. Theorem E needs endorsement, which is a property of the rule. Cor E.2 lists forced literals but derives no contradiction from them. The natural non-endorsed escape from Cor E.2(i) at world v is a tie X ~_v C_u combined with C_u ⪯_v C_{u_t^w}.
- (TC) then demands C_{u_t^w} ⪯_v C_u, which is again u¹-unfavourable.
- Lemma S then propagates the change into the splits of member–member records.

I could not close this cascade into a rule with a global (TC) proof. It is the concrete OPEN step.

---

## 5. Hints evaluated, and coordinator items

**Hint 1: single-world incomparability on inverse records.**
- Correct as a q-escape: α = (1, 1).
- It is relationally consistent with defence, protection, (G) and (TC) when built symmetrically: incomparable at w₀ and tied elsewhere (Thm R). The symmetry is essential for (TC) (step 4 of Thm R).
- (TC) on reverses of accepted 3-cycles is never violated, because every accepted cycle has all V_w = 0.
- The obstruction is **openness at interior sources** (Thm E), not (TC), defence or (G).

**Hint 2: refusals as strict inequalities of continuous functionals.**
- My first design was "accept iff V_w ≥ ρ_w(r)", with ρ ≥ 0 symmetric and lower semicontinuous, zero on guidance records.
- It has automatic (TC) and automatic openness: any accepted cycle has all V_w = ρ_w = 0.
- Protection on null records reduces to ρ ≠ 0 there; defence reduces to: some w with V_w ≥ ρ_w.
- It is u¹-endorsed, so Thm E kills it at u. The adversary should not need to attack it.
- It is not PP38's kernel, which is fixed to ℓ^T and complete, and not a gate union. It is killed by the new Theorem E, not by those.

**Hint 3: modify Λ only where Theorem Q bites.** R₀ is exactly that, with Λ's tie-breaks removed:
- Λ's verdicts are kept wherever V ≠ 0;
- ties at V_w = 0 with V ≠ 0 are made two-way;
- null records are made incomparable at w₀.

The modification preserves (TC), (G) and protection (Thm R). Its sections fail exactly on the null fibres (Thm P), which by Thm E is unavoidable for this class.

**Hint 4: germ literals.** Cor E.2(i) is an exact germ statement along pure shifts. No neighbour heuristic is used, and Lemma 1.3(b) is exact.

**Coordinator items.**
- **(1) Ledger.** As used above: M0 and intersections were locally unexcluded before this note. Theorem E excludes the u¹-endorsed ones for interior modules.
- **(2) Prop A″** is used for the "no Λ_q" claim in Thm M.
- **(3) Compact families.** No sampling enters: the certificate is pointwise.
- **(4) Straddling.** (2, 2) is in the α-cell of the referee's table.
- **(5) SR(c) cofinite coupling.** On the module, R₀ has closed sections at every rival–source pair in scope, so every such restriction is met. Theorem E is itself an instance of the referee's pattern:
  - openness forces C_{u_t} ⋠_w X for all small t;
  - defence then forces "⪯_v for some v ≠ w" cofinitely;
  - endorsement makes every such literal false.

---

## 6. Open gaps

1. **Interior balanced swaps (main gap; OPEN).** A rule with open refusals for X = C_a[F ↦ C_b] at interior a. By Cor E.2 it must accept, at v ≠ w, comparisons out of w-shifted members that u¹ disfavours by Θ(t), and must handle their splits. Two candidate mechanisms:
   - a world-v tie class containing C_a, X and the members in O_w-directions from a. These are mixed at v, so strict (G) allows it; but by the tie–pad lemma it must meet each e_v-ray at most once;
   - refusing u¹-favourable splits through protection refusals of the shifted members, since rec(Z_E, C_{a_t}) is a protection record of a_t.

   Neither has a global (TC) proof yet.
2. **(H_Γ) away from u.** NUMERICS only. An exact proof needs the boundary integrals of the layer, or a symmetry argument as at u.
3. **Endorsers other than u¹.** Theorem E applies to q·u¹ once the family contains a q-balanced member swap and (H_Γ) holds for q·u¹. For general ψ it is conditional on Cor 4.4's strict (K2) and on (H_Γ).
4. **Full covers.** Theorem M is a module. A full cover must also escape M0closed, Q4.1–Q4.2 and L4/R21.

---

## 7. Scripts (`r9/PP62_py/`; run `python3 -I -B <script>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `r0_check.py` | R₀ on PP56's exact kink cells (imports PP56's `instance56`, `cells56`, `lex56` unchanged). [I1]: 2¹⁸ rivals, member obligations. [I2]–[I4]: exhaustive reflexivity, strict (G), (IB), (TC) on all triples, member obligations, incomparability only on null records at w₀. [α]: same-world inverse refusals with α = (1, 1). | CHECKED, ALL PASS (about 45 s) |
| `gamma62.py` | Γ(a, a∘(1 ± te_w))/t for a ∈ {u, B, D, a₁}; layer masses by odd world; membership in O_w; Jacobian of a ↦ Φ(C_a). 4·10⁶ Gaussian samples. | NUMERICS |

**Most important next step.** Attack Cor E.2 directly with germ literals at u. Variables: the verdicts of C_{u_t^w} against X, against C_u, and against the split models Z_E, at the two worlds v ≠ w, for the six pure-shift germs. Constraints: (TC) on the triangles {C_{u_t}, X, C_u} and {C_{u_t}, X, Z_E}, strict (G) along the e_v-rays (tie–pad), and the members' defence. If this finite germ system is UNSAT, it would be the first axiom-level section obstruction. If it is SAT, its solution is the local shape of the interior rule.
