# PP70. Adversary for round 57: what the axioms force along a non-isolated family of distinct selected models, and attacks on the two-direction construction

24 October 2026. Adversary task of Brief 57. One author; not refereed. Final. §1 is independent of PP69; §2 attacks PP69 (final version) and answers the coordinator's relays of REFEREE_round56 and of PP69.

Read: BRIEF57_two_direction and its binding audits (AUDIT_round57, AUDIT_round57_two_direction, AUDIT_round57_answers); PP67 and PP68 with the corrections at the end of DESIGN_MEMO §8.25; PP64 §1–2; REFEREE_round55 §2.4, §4, §5; AUDIT_completion (rules I–IV); LEAD_selection_count.

**Labels.**
- PROVED: complete argument here, or a cited result used within its hypotheses.
- CHECKED: exact rational geometry, or exact SAT on a finite cell sub-universe, in `r9/PP70_py/`. Every SAT clause is an axiom instance on the sub-universe (`lib70.py`, my own encoding), so UNSAT is a full-domain fact; SAT is evidence only.
- NUMERICS / CONJECTURE / OPEN: as stated.

No axiom is added. Conventions: X ⪯_w Y means "X is at least as good as Y at w"; X ⊵_w Y means X is pointwise weakly w-better; a record is accepted at w when its old side is at least as good. Coherent models are conic (Lemma H), so a model differing from a coherent one exactly on a non-conic set is incoherent.

---

## 0. Verdict

1. **No axiom-level conflict** was found (§3). Every conflict below is with a particular choice.
2. **Forced structure along a non-isolated family (§1; PROVED unless marked).**
   - **Guidance is tame along the curve (Thm 1.2).** For every fixed rival and world, guidance acceptances form a closed interval of indices and guidance refusals form an interval. So guidance never makes the defending world alternate, and never produces a limit conflict. Any accumulation trap needs non-guidance commitments.
   - **The fill's class fixes the direction of repair (Prop 1.3).**
     - Class-3 fills can be repaired only by later members.
     - Class-1 and class-2 fills can be repaired only by earlier members, or off the curve.
     - T's other-class fills can be repaired by no curve member.
     - The class-k and class-k′ repairers of one source are distinct.
     - PP67's (C3) stops T from repairing either kind of other-class fill of N.
   - **Thin rivals force repairs to accumulate (Prop 1.5)** at the source (fills), at u (splices) and at N (other-class). So fixed reservation balls are impossible, not merely costly.
   - **World-by-world windows (Props 1.6, 1.7).**
     - Fill repairs are mixed at every world exactly when the repair is silent on part of E. Otherwise strict (G) alone refuses them.
     - The audit's splice window is necessary but not sufficient; there are new world-1 and world-2 exclusions. Some splice repairs are guidance acceptances.
     - REFEREE_round56's world-2 example is an instance.
   - **(IB) coincidences (Prop 1.8).**
     - A repair record equal to a member–member record is inadmissible; two-band splices are an example (CHECKED).
     - T itself carries the R-repairs of other-class fills inside its silence.
   - **The generalised trap transfers (Prop 1.9; CHECKED)** to every later member that is A on an earlier fill set.
3. **PP69 (§2).** Its 𝒲 is one total additive relation realising the arc by Bayes acts. The finitary attacks all fail against it on the arc: mixed triangles, (IB) copies, the generalised trap, accumulation on the arc. The repair lemma and Props 5.2–5.3 are correct; 5.3(a) needs a repair. **What fails:**
   - **(a) An error at the endpoint (Prop 2.1).** The tube radius at θ = 1 is unbounded when A_w(X) = ∅ (X = V₁, w = 1). Then (I8) fails at e₁, and Σ is not extendible (Lemma B).
   - **(b) After the obvious cap, an edge squeeze (Prop 2.2).**
     - Every future edge model has min(Φ₁, Φ₂) ≤ Φ₁(D\*).
     - No swap-invariant edge model other than D\* is ever selected.
     - Wide edge models (K ⊋ M₀ at both ends) are banned.
     - Any radius at h₁₂ bounded below forces a D\*-level plateau on the edge.
   - **(c) Scope (Props 2.3, 2.4).**
     - The referee's non-vacuous Prop 7.1 family contains **no** swap-invariant H, so PP69's remark that it is repaired is vacuous. These splices are N's other-class fills, unrepaired.
     - Result: class-3 fills only, which is narrower than either partial target of the brief.
   - **(d) A mis-checked import (Prop 2.5).** Dominator sets are intervals, so three nested fills share a member. PP68's carrier exclusion therefore applies to a continuum of records.
   - **(e) Bequests.**
     - Transverse tube rate (Prop 2.6).
     - Off-arc Bayes acts of 𝒲 are incoherent (NUMERICS), as Theorem gm requires. So every extension must leave 𝒲 on records that no arc member carries.
     - One-sided retreats and T's other-class fills are dominated by no member (Prop 2.7, PROVED for PP69's field).

---

## 1. Forced structure along a non-isolated family

### 1.1 The curve

Index the brief's curve by s ∈ [0, 3]:
- C_s = R_s for s ∈ [0, 1];
- C_s = J_{s−1} for s ∈ [1, 2];
- C_s = F_{s−2} for s ∈ [2, 3].

So C_0 = T, C_1 = N, C_2 = L₀ and C_3 = D\*.

**Lemma 1.1 (PROVED; CHECKED in `geom70.py`, `thr70.py`).**
- **(a) 3-descending.** For r < s, C_r ⊵₃ C_s. The R-segment withdraws only T's answers on L = {T ≠ N}, which are 3-correct. The J- and F-segments add only 3-wrong answers.
- **(b) At most two changes per problem.** Each problem g changes advice at most once on [0, 1], and only if g ∈ L, from T's answer to S at σ(g). It changes at most once on [1, 3], from S to an answer, at a threshold β(g) or τ(g). If both happen, the second answer is the opposite of T's. Hence, for every g and every world w, s ↦ rank_w C_s(g) is **monotone** (non-decreasing or non-increasing, depending on g and w).
- **(c) Continuity.** C_{s_n} → C_s a.e. whenever s_n → s.
- **(d) Change types.**
  - On R: (class 3, B → S) on R_B, and (class k, A → S) on L ∩ M_k for k = 1, 2.
  - On J: only (class k, S → B) for k = 1, 2. J_β = N on class 3.
  - On F: (class 3, S → A), and (class k, S → B) for k = 1, 2.

  For every region and every one of 12 equal sub-intervals of its segment, a change of that type occurs (CHECKED, exact thresholds). So every band {C_s ≠ C_t} with s < t has class-1 and class-2 parts of positive measure.
- **(e) R_B is answered late.** On R_B the F-threshold satisfies τ ≥ 9/16, and 9/16 is the infimum. Hence F_t is silent on all of R_B for t ≤ 9/16.

*Proof.*
- **(a), first half.** M ⊆ K_α ⊆ K_N, with K_α increasing in α. If k = (1−α)m + αk′, write it as (1−α′)m + α′k″ with k″ := (α/α′)k′ + (1 − α/α′)m ∈ K_N. So the answers of R_α are T's answers minus some on L, and those are 3-correct.
- **(a), second half.** K_{J_β} decreases in β by the same identity. The new answers of J lie among L₀'s new answers, which are B on M₁ ∪ M₂ (PP68 Prop 4.5(iii)). For F: conv(v_t, M₀) decreases in t, because v_t ∈ [v_s, h₁₂] ⊆ conv(v_s, M₀). F_t's answers are among D\*'s, and D\* ⊴₃ T (PP64 Lemma 4.2). So D\* gives no 3-correct answer where N, hence L₀, is silent.
- **(b).** Minimum over a Minkowski combination is the combination of minima. So R_α answers T's answer iff (1−α)a + αb > 0, with a > 0 ≥ b on L; this gives the single threshold σ = a/(a − b). The same holds for J and, by linearity of t ↦ v_t·g, for F. Answers only grow on [1, 3].
  - Monotonicity: T's answer, then S, then the opposite answer have ranks (0, 1, 2) or (2, 1, 0) at every world. A single change is trivially monotone.
- **(c).** The set where a threshold equals s is contained in a quadric cone, which is null.
- **(e).** On R_B take g = (−a, −b, h) with a, b > 0. Then T says + exactly when 16a + 7b ≤ 7h and 7a + 16b ≤ 7h (vertices v₁, v₂; v₃ is then automatic). Also τ = v₃·g / (v₃·g + (a + b)/2), and v₃·g = (16h − 7(a + b))/30.
  - τ increases with h/(a + b).
  - The constraints give h ≥ 23(a + b)/14, with equality iff a = b.
  - At equality, v₃·g/(a + b) = 9/14, so τ = 9/16.
  - Sampled minimum: 0.5695. ∎

### 1.2 Guidance along the curve is tame

**Theorem 1.2 (PROVED).** Fix a measurable X and a world w. Put
- G⁺ := {s : C_s ⊵_w X} (guidance acceptance of X);
- G⁻ := {s : X ⊵_w C_s strictly} (guidance refusal).

Then:
- G⁺ is a closed interval;
- G⁻ ∪ {s : C_s = X} is an interval;
- the two sets are disjoint.

Consequently:
- (i) No fixed rival is ever forced by guidance to be accepted at w on a set accumulating at a guidance refusal of w, or to have its defending world alternate along the curve.
- (ii) No member is guidance-refused against X at all three worlds. On a mixed problem no advice is weakly better at all three worlds, and coherent models are correct on unanimous problems.

*Proof.*
- **Convexity.** Let r < s < t. By Lemma 1.1(b), rank_w C_s(g) lies between rank_w C_r(g) and rank_w C_t(g).
  - If both are ≤ rank_w X(g), so is the middle one.
  - If both are ≥ rank_w X(g), so is the middle one.
- **Closedness of G⁺.** Lemma 1.1(c): an a.e. limit of pointwise inequalities is a pointwise inequality.
- **Disjointness.** By strictness. ∎

**Reading.** Along this family, the only unit literals that are rival-level and world-specific are:
- the guidance literals (tame by Theorem 1.2);
- the **spread** of each refusal to an open neighbourhood (closed sections, reservation (I6)–(I7));
- whatever the construction commits.

An accumulation trap of REFEREE_round55 §5.3 type therefore needs non-guidance commitments: repairs, their (TC) consequences, and their (IB) copies. That is where §2 attacks.

### 1.3 The forced directions of repair

**Prop 1.3 (direction lemma; PROVED; CHECKED K1, K2).** Let C be selected at an interior index. Let Y = C[E ↦ A_k] be a class-k fill, with E ⊆ Sil(C) ∩ M_k non-null. Let B be any model with B ⪯_i Y at both worlds i ≠ k. Then C ⋠_i B for both i ≠ k, and therefore C ⪯_k B.

*Proof.* Y is strictly i-better than C for i ≠ k, so Y ⪯_i C (guidance) and C ⋠_i Y (strict (G)). If C ⪯_i B, then C ⪯_i B ⪯_i Y ⪯_i C is an accepted triangle with a refused reverse. C's competitiveness then leaves world k. ∎

**Corollaries (PROVED).**
- **(a) Distinct dominators for distinct classes.** If B dominates a class-k fill and B′ dominates a class-k′ fill of the same interior source, with k ≠ k′, then B ≠ B′. Otherwise C refuses B at {i ≠ k} ∪ {i ≠ k′} = W.
- **(b) Directions along a weakly 3-descending family.**
  - A class-3 fill of C_s can be repaired only by a member C_t with C_s ⋠₁ C_t and C_s ⋠₂ C_t. It cannot be repaired by a 3-better member, which would contradict C_s ⪯₃ C_t (PP68 Lemma 4.2(a)). So the repair is later.
  - A class-1 or class-2 fill of C_s cannot be repaired by any later member, since C_s ⪯₃ C_t is guidance while the lemma demands C_s ⋠₃ C_t. So the repair is earlier, or off the curve.
- **(c) The root.** Every curve member is weakly 3-worse than T. So T's class-1 and class-2 fills are repaired by **no** member of the curve. They need off-curve models such as PP67's N₁ and N₂, whose own fills start further families.
- **(d) N's other-class fills.**
  - Within the curve, only T or some R_α (α < 1) can repair them.
  - T can repair a class-1 fill of N only if N ⋠₂ T, and a class-2 fill only if N ⋠₁ T. **PP67's (C3) commits N ⪯₁ T and N ⪯₂ T, which excludes T for both classes.**
  - Since N ⋠₃ T, N must defend against T at 1 or 2 (PP68 Prop 2.2). So T can serve at most one of the two classes.

**Reading.** The audit's two directions (fill repairs moving forward, splice repairs moving back toward T) are not the only forced split. The class of the fill already fixes the direction. A "repeatable step at every source in all three classes" needs, at every source, repairs on **both** sides of it, and at the root T it needs off-curve models.

### 1.4 A fixed fill rival along the family

Let Y = C_s[E ↦ A] be a class-3 fill of a member C_s at an interior index. Write τ_max(E) for the essential supremum of the curve thresholds on E (Lemma 1.1(b); on the J-segment class 3 does not change, so thresholds on E lie in the F-segment).

**Prop 1.4 (PROVED).** In any selection with closed sections:
- **(a) Refusal neighbourhood.** There is an open neighbourhood V(Y) of p_s in which every selected model refuses Y at 1 and at 2, and so accepts it at 3.
- **(b) Late members cannot accept at 3.** Every member C_x with x ≥ τ_max(E) has C_x = A a.e. on E. So Y ⊵₃ C_x strictly, C_x ⋠₃ Y, and C_x accepts Y at 1 or 2. More generally, this holds for every selected B with B ⊴₃ Y strictly.
- **(c) The switch.** σ\*(Y) := inf{x > s : C_x ⪯₁ Y or C_x ⪯₂ Y} lies in (s, τ_max(E)]. It is attained: C_{σ\*} ⪯_i Y for some i ∈ {1, 2}, and also C_{σ\*} ⪯₃ Y when σ\* < τ_max.
- **(d) Non-guidance literals before the switch.** Each x ∈ (s, σ\*) has C_x ⪯₃ Y, and this literal is **not** guidance: the record carries a 3-gain on the band and a 3-loss on E ∩ {threshold > x}.
- **(e) Earlier members.** For each x < s, C_s defends against C_x at some i(x) ∈ {1, 2}, since C_s ⋠₃ C_x. Then C_x ⋠_{i(x)} Y, by the triangle C_x → Y → C_s → C_x.

*Proof.*
- (a): strict (G) at s, closed sections, and competitiveness.
- (b): Lemma 1.1(a), together with C_x = A on E.
- (c): A₁(Y) ∪ A₂(Y) is closed, misses V(Y), and contains [τ_max, 3) by (b).
- (d): direct.
- (e): C_s ⪯_i C_x, C_x ⪯_i Y and Y ⪯_i C_s (guidance) form an accepted triangle whose reverse C_s ⪯_i Y is refused. ∎

**Collision test.** The question is whether switch points of different rivals can be forced together.
- By Theorem 1.2, guidance cannot do it.
- By (d), the literals between s and σ\*(Y) are non-guidance.
- Two such literals at the same index for different rivals interact only through (TC) and (IB), i.e. through the construction's commitments.
- I found no collision forced by the axioms alone. §2 tests PP69's commitments.

### 1.5 Forced accumulation of repairs, and the end of fixed balls

**Prop 1.5 (PROVED).**
- **(a) Class-3 fills, thin near the source.** Let E ⊆ Sil(C_s) ∩ M₃ have its thresholds in (s, s + η).
  - Any in-family repair C_t has s < t < s + η: later by Prop 1.3(b), and t < τ_max(E) by Prop 1.4(b).
  - So the in-family repairs of the thin fills of every source **accumulate at that source from above**.
  - On the J-segment this applies only to sources in F, and to L₀ itself (fills of L₀ in Sil(L₀) ∩ M₃). N's class-3 fills may be repaired uniformly by J-members, which are silent on all of Sil(N) ∩ M₃ (PP68 Prop 4.5).
- **(b) Thin splices near T.** Let Z_H = T[H ↦ S] with H ⊆ L and σ < η on H. Any repair R_α has α < η, because α ≥ ess sup σ|_H gives H ⊆ L_α, and then Z_H ⊵₃ R_α strictly. **In-family splice repairs accumulate at u.**
- **(c) N's other-class fills, thin near N.** Let E ⊆ L ∩ M₁ have σ > 1 − η on E. Any R_α repairing N[E ↦ T] has α > ess inf σ|_E ≥ 1 − η (Prop 1.7(b)). **These repairs accumulate at N from below.**
- **(d) Reservations must shrink.** Suppose C_t repairs a class-3 fill of C_s. Then C_s ⋠₁ C_t and C_s ⋠₂ C_t (Prop 1.3). Each refusal needs a reservation U ∋ p_s with every assigned q ∈ U refusing C_t at that world. Since C_t ⪯_w C_t, p_t ∉ U.
  - So U has radius below |p_s − p_t|. By (a) this tends to 0.
  - No fixed ball at a source can carry the reservations of all refusals its repairs force.
  - The same holds at u for splice repairs: T ⋠₁ R_α whenever Z_H is strictly 1-better than T and R_α repairs it.

*Proof.* As stated; (b) and (c) use Prop 1.7. ∎

So PP68 Prop 2.1 (fixed balls force tie plateaus) is superseded. In-family repairs of thin rivals make fixed balls **impossible**, not merely costly. Rival-dependent reservation neighbourhoods are forced.

### 1.6 Fill windows, world by world

**Prop 1.6 (PROVED).** Let Y = C_s[E ↦ A] be a class-3 fill and C_t a later member, t in the J- or F-segment. Then

  ρ := rec(C_t, Y) = (B∖E : C_t → C_s) ⊔ (E ∩ Sil(C_t) : S → A),  with B := {C_s ≠ C_t}.

- **Worlds 1 and 2: always mixed.**
  - On the class-1 band, C_t = B is 1-correct and 2-wrong.
  - On the class-2 band, the reverse.
  - Both bands are non-null (Lemma 1.1(d)).
  - When s lies in R, the L-part (C_t = S → T's answer) is also mixed at 1 and 2.
- **World 3.**
  - Mixed iff E ∩ Sil(C_t) is non-null.
  - Otherwise the new side Y is strictly 3-better than C_t, and C_t ⋠₃ Y by **strict (G)**.

  This gives the audit's path obstruction without protection or (C). Protection is needed only for the stronger form with (IB).

So the audit's claim "mixed at every world" holds for class-3 fill repairs **exactly** on the window "C_t silent on part of E". The quartile window is inside it.

### 1.7 Splice windows, world by world

**Prop 1.7 (PROVED).** Let Z_H = T[H ↦ S] with H ⊆ L, and write L_α := {σ ≤ α}. Then

  rec(R_α, Z_H) = (L_α ∖ H : S → T) ⊔ (H ∖ L_α : T → S).

**(a) Exclusions.** R_α cannot dominate Z_H if any of the following holds.
- (i) H ⊆ L_α. The new side is strictly 3-better: strict (G).
- (ii) L_α ⊆ H with H ∖ L_α non-conic. The record equals rec(W, N) with W = N[H ∖ L_α ↦ T]. N's protection and (C) then make W ≈ N, but W is non-conic.
- (iii) L_α ∖ H ⊆ M₂ and H ∖ L_α ⊆ R_B ∪ M₁. Z_H is strictly 1-better: strict (G) at 1.
- (iv) The mirror of (iii) at world 2: L_α ∖ H ⊆ M₁ and H ∖ L_α ⊆ R_B ∪ M₂.

(i) and (ii) are the audit's window. (iii) and (iv) are new.

**(b) Other-class fills of N are splices.** For E ⊆ L ∩ M₁, N[E ↦ T] = Z_{L∖E} is a class-1 fill of N. Here (i)–(iv) read:
- α > ess inf σ|_E;
- α < ess sup σ on (L ∩ M₁) ∖ E.

The second condition is (iv): R_α must keep T's A₁ somewhere on L ∩ M₁ outside E.

**(c) "Every repair is mixed at every world" fails for splices.**
- If H ⊆ L ∩ M₂ and H ⊇ L_α ∩ M₂, then R_α ⪯₁ Z_H is a **guidance** acceptance. Such guidance links take part in (TC) kills that mixed links do not.
- **Example where only a short window survives.** H := ((R_B ∪ M₁) ∩ L ∖ K) ∪ (M₂ ∩ L_{α₀}), with K ⊆ L ∩ M₁ non-conic and σ|_K ⊆ (1 − η, 1).
  - α ≤ α₀ is excluded by (ii).
  - α ∈ (α₀, 1 − η] is excluded by (iii).
  - So the R-window is contained in (1 − η, 1), and these repairs accumulate at N.

*Proof.* Compute the record cell by cell, using T's answer B on R_B (wrong at 1, 2), A₁ on L ∩ M₁ (wrong at 1) and A₂ on L ∩ M₂ (wrong at 2). The identity in (ii) holds because the new side of the record is S, which is N, on its whole support. ∎

### 1.8 (IB) coincidences inside the family

**Prop 1.8 (PROVED; (a) CHECKED K3).**
- **(a) Member–member records are forbidden as repair records.**
  - Distinct curve members are never all-world tied: strict (G) at 3.
  - So if rec(B, Y) = rec(C′, C″) for distinct members, B cannot dominate Y. Otherwise C′ dominates C″, and C″'s protection forces a tie.
  - **Example: two-band splices.** H = L_α ∪ (L_x ∖ L_{α′}) with α < α′ < x gives rec(R_α, Z_H) = rec(R_{α′}, R_x). So the inner member R_α can never repair this conic splice. Its repairs must come from (α, α′) or (α′, x), where the record has two opposite parts.
- **(b) Family carriers of fill-repair records.** Let ρ = rec(C_t, Y), Y = C_s[E ↦ A] (§1.6).
  - A member C_{t′} ≠ C_t carries ρ iff t′ > t and E has no thresholds in (t, t′].
  - The copy is then: C_{t′} dominates Y[(t, t′]-band ↦ C_{t′}].
  - No copy of ρ has a member on its new side. Copies of ρ⁻¹ end at a member exactly at the carriers just listed: rec(C_{t′} ⊕ ρ, C_{t′}) = ρ⁻¹. So the strictness of the repair (Y ⋠_w C_t at some w) is inherited by every gap carrier.
- **(c) Family carriers of splice-repair records.** R_{α′} carries rec(R_α, Z_H) iff σ ≤ α′ on L_α ∖ H and σ > α′ on H ∖ L_α. The copy is a domination of Z_{H′}, with H′ = H ∪ (L_{α′} ∖ L_α) for α′ > α. If H′ is a threshold set, (a) applies.
- **(d) T carries R-repairs of other-class fills inside its silence.**
  - Let R_x repair a class-1 fill Y = R_α[E ↦ A₁] with E ⊆ Q₁ = Sil(T) ∩ M₁ and x < α (Prop 1.3(b)).
  - Then rec(R_x, Y) = (L_α ∖ L_x : T → S) ⊔ (E : S → A₁), and T carries it.
  - So **T must dominate V := T[L_α ∖ L_x ↦ S, E ↦ A₁] at every world.** This is a continuum of non-guidance acceptances at the root, one per (α, E). The same holds for class 2.

*Proof.*
- (a) as stated.
- (b): a carrier must equal C_t on B ∖ E and be S on E ∩ Sil(C_t). Members before t are silent on part of B ∖ E, because the class-1 band is non-null. Members after t answer on E ∩ (t, t′].
- (c), (d): direct record computations. ∎

### 1.9 The generalised trap, transferred along the family

**Prop 1.9 (PROVED; CHECKED K4).** Let s < t, and let E ⊆ Sil(C_s) ∩ M₃ be non-null with C_t = A on E.
- By Prop 1.4(b), C_t must defend against Y = C_s[E ↦ A] at 1 or 2.
- Let G₁ ⊇ E with G₁ ∖ E a non-null proper part of the class-2 band; define G₂ symmetrically with the class-1 band.
- Put Z_w := C_s[G_w ↦ C_t] and r_w := rec(Z_w, C_t).

Then:
- each r_w is mixed at 1 and 2;
- r₁ ∈ Acc₁ together with r₂ ∈ Acc₂ leaves C_t undefended against Y;
- for s ≥ 1, r_w is carried by C_s and by every member C_x with 1 ≤ x ≤ s (they are silent wherever C_s is), and also by T and the R_α when the band avoids L.

*Proof.* REFEREE_round55 Prop G with (T, D, X_E) replaced by (C_s, C_t, Y). That proof uses only strict (G), (TC) and C_t's defence on {1, 2}. Here C_t ⋠₃ Y by Prop 1.4(b), which replaces "supp D = {1, 2}". ∎

**Consequence.** For every pair (C_t, Y) with C_t = A on E, the construction must refuse, at C_t's chosen defending world, a whole continuum of records (one per admissible G_w). These records are carried by the source and **all earlier members**, and each refusal is reserved around every carrier, which is an open set containing an interval of the family (Prop 1.5(d)). In particular the defending world of C_t against Y must be **committed** at installation, as REFEREE_round55 recommends for edge defenders.

---

## 2. Attacks on PP69 (final version of 10:02)

PP69 builds one total relation 𝒲, additive at every world, from a field for which every member C_θ of the curve (indices p(θ) on [u, h₁₂], endpoint D\* included) is the unique pointwise Bayes act of p(θ)·f. It commits every record out of every member. It repairs each rival X with Φ₁(X) = Φ₂(X) by C_θ′, the first member with Φ₁(C_θ′) = Φ₁(X). Refusals are reserved on tubes. Because 𝒲 is total and satisfies every finitary axiom, the finitary attacks of the brief (mixed fill/splice triangles, (IB) copies, the generalised trap, (TC) among repairs, REFEREE_round55-type accumulation **on the arc**) all fail against it, and I confirm this below. The successful attacks concern the endpoint, the scope, one mis-checked import, and what the committed rows bequeath to the rest of Δ.

### 2.1 What I confirm (PROVED, independently)

- **Thm 3.1 and Thm 3.3 are correct.** For the repair lemma there is a one-line proof. Apply Bayes at p(θ′) to X: since Φ₁ = Φ₂ for both, p₃(θ′)(Φ₃(C_θ′) − Φ₃(X)) ≤ 0, with equality only if X = C_θ′. This needs **no** knapsack argument and no structure of X beyond Φ₁(X) = Φ₂(X). So every swap-balanced rival with Φ₁(X) ∈ [Φ₁(D\*), Φ₁(T)] is strictly dominated.
- **Exact criterion for asymmetric rivals (PROVED).** Let m(X) := min(Φ₁(X), Φ₂(X)). A member dominates X iff Φ₃(C_θm) ≤ Φ₃(X), where θ_m is the first θ with Φ₁(C_θ) ≤ m(X) (θ_m = 0 if m(X) ≥ Φ₁(T)). Indeed Φ₁(C_θ) decreases and Φ₃(C_θ) increases along the arc (PP69 Lemma 3.2). Bayes at θ_m bounds the failure: Φ₃(C_θm) − Φ₃(X) ≤ (p₁/p₃)(θ_m)·|Φ₁(X) − Φ₂(X)|.
- **Finitary attacks fail on the arc.** Every committed literal is a 𝒲-verdict, and 𝒲 satisfies (TC), (IB) and strict (G) on all measurable models. So:
  - mixed fill/splice triangles, all (IB) copies (including those ending at members), and the transferred generalised trap (Prop 1.9) are satisfied;
  - the two-band splices of Prop 1.8(a) receive repairs strictly inside the band, never at the inner member, because Φ₁(Z_H) < Φ₁(R_α);
  - accumulation on the arc cannot produce a contradiction, because the limit literals are 𝒲's (θ ↦ Φ(C_θ) is continuous).
- **Referee's relay (1), the σ-lemma at world 2.** Within PP69's scope the trap cannot occur. If C_θ′ were pointwise strictly 2-worse than Z, strict monotonicity of f₂ would give Φ₂(C_θ′) > Φ₂(Z), contradicting the tie at world 2. The referee's example H = (L ∩ (M₂ ∪ M₃)) ∪ B₁ is outside the scope: Z_H = N[(L ∩ M₁) ∖ B₁ ↦ T] is a **class-1 fill of N** (§2.3), which no member can repair.
- **Splice windows.** PP69's choice satisfies Prop 1.7(iii)–(iv) automatically, for the same reason.

### 2.2 The endpoint: Theorem 3.7(a) fails as stated, and the repair forces an edge plateau

**Prop 2.1 (PROVED).** PP69's tube radius at θ = 1 is r(1) = ½·dist(h₁₂, p(A_w(X))), with no second term. Take X = V₁, the precise vertex model at e₁, which is correct at world 1 on every problem, and take w = 1.
- f₁ is strictly rank-monotone, so Φ₁(V₁) < Φ₁(C_θ) for every θ. Hence A₁(V₁) = ∅.
- Then r(1) = +∞, and U₁(V₁) = Δ.
- So Rz_{e₁}(V₁) ⊇ {1} = supp e₁, and **(I8) fails at e₁**.
- Moreover, every extension to D = Δ must put V₁ at e₁ (LEAD Lemma B), which then refuses itself. So Σ is not extendible.

The same happens for every X with Φ_w(X) < Φ_w(D\*), w ∈ {1, 2}. The (I8) argument in PP69 (edge points "lie only in tubes around θ = 1, where D\* defends at 1 or 2") covers the open edge {1, 2} only.

**Repair, and its price.** Cap r(1) at ½·dist(h₁₂, ∂Δ ∖ (e₁, e₂)) =: ρ₀, or at any radius bounded below independently of X. Then (I8) holds. But the following still holds.

**Prop 2.2 (edge squeeze; PROVED; CHECKED K6, K7).** In any extension of PP69's Σ to a system satisfying the axioms:
- **(a)** Every selected model D at an open-edge index of {1, 2} satisfies min(Φ₁(D), Φ₂(D)) ≤ Φ₁(D\*).
  - *Proof.* D must defend, at 1 or 2, against a class-3 fill of each C_θ, θ < 1. If Φ₁(C_θ) ≤ Φ₁(D) and Φ₂(C_θ) ≤ Φ₂(D), the committed row of C_θ accepts C_θ ⪯₁ D and C_θ ⪯₂ D. Then D is undefended (Kill-A with an edge model; REFEREE_round55 §4).
  - Hence min(Φ₁(D), Φ₂(D)) < Φ₁(C_θ) for every θ < 1, and Φ₁(C_θ) ↓ Φ₁(D\*).
  - In particular **no swap-invariant edge model other than D\* is ever selected**, since for those min = mean > Φ₁(D\*). This includes PP65's precise D_{(½,½,0)}.
- **(b)** Suppose the tube radii at θ = 1 are bounded below by ρ > 0 on the rivals X with Φ_w(X) < Φ_w(D\*). Then every selected model C_q with |q − h₁₂| < ρ has Φ₁(C_q) ≥ Φ₁(D\*) and Φ₂(C_q) ≥ Φ₁(D\*).
  - *Proof.* Otherwise X := C_q with a small w-worsening added still has Φ_w(X) < Φ_w(D\*). Guidance (I1) accepts C_q ⪯_w X, while q ∈ U_w(X) refuses it.
- **(c)** Combining (a) and (b): on the edge within ρ of h₁₂, every selected model has min(Φ₁, Φ₂) = Φ₁(D\*) exactly.
  - Every 𝒲-Bayes edge model at an index q ≠ h₁₂ has min < Φ₁(D\*), so it is excluded.
  - So the selection is forced onto a **plateau** of D\* (or of exact Φ₁(D\*)-level models). This is PP68 Prop 2.1 reappearing at the endpoint.
- **(d)** Every edge model D_K with K ⊆ [e₁, e₂] extending strictly beyond **both** endpoints of M₀ is never selected anywhere on the edge.
  - *Proof.* Such a D_K is silent on non-null parts of both the class-1 and class-2 F-bands near D\*'s boundary, where L₀ is silent. Choose P in those parts, with masses such that Φ₁ and Φ₂ both strictly decrease under P : S → B. This is possible because each switch lowers φ₁ + φ₂ (PP69 Lemma 2.2(c)).
  - L₀'s committed row refuses L₀[P ↦ B] at 1 and 2. By (IB), D_K refuses D_K[P ↦ B] at 1 and 2, which are its whole support.

**Verdict on the endpoint.** PP69's "sections checked at the endpoint" holds **along the arc**. Sections at h₁₂ in Δ involve the edge, and there the committed rows impose (a) and (d) on every future edge model. Any radius rule at θ = 1 that does not shrink with the future edge index forces (c). The endpoint is consistent as a module, with the cap. As a starting point for (S) on the edge it is a design commitment with an explicit price. The honest label is **interior construction plus a constrained endpoint**.

### 2.3 Scope: the referee's non-vacuous Prop 7.1 family is not covered, and PP69's remark on it is vacuous

**Prop 2.3 (PROVED).** Let w ∈ {1, 2}, P_w ⊆ H ⊆ L, with L ∖ H non-null and H non-conic (REFEREE_round56 §1.7).
- **(a) No such H is swap-invariant on M₁ ∪ M₂.** We have P₁ = R_B ∪ (L ∩ M₁). If H ∩ (M₁ ∪ M₂) is swap-invariant and contains L ∩ M₁, it contains σ(L ∩ M₁) = L ∩ M₂, so H = L.
  - So PP69 §3.2's remark that these splices "**are** repaired here whenever H is swap-invariant on M₁ ∪ M₂" applies to **no** splice.
- **(b) Every such Z_H is a class-w′ fill of N** (w′ the other edge world): Z_H = N[L ∖ H ↦ T], with L ∖ H ⊆ L ∩ M_{w′} and T = A_{w′} there.
- **(c)** By Prop 1.3, no member later than N repairs it, in any relation. By PP69 Prop 5.2, no member repairs it in 𝒲. So the whole non-vacuous family is **unrepaired**, as are the referee's B6 example (§2.1) and, more generally, every T/N splice whose restored set lies inside one class M_k, k = 1, 2.

**Prop 2.4 (PROVED; what PP69 reaches, against the brief's criterion).**
- Class-3 majority fills of every source on a non-isolated family: **yes** (PP69 Cor 3.4).
- "Fills alone" in the brief's sense (N's fills in all three classes, and the analogues for every source): **no**.
  - In any relation, no curve member repairs a class-1 or class-2 fill of T (Prop 1.3(c)).
  - In 𝒲, no member repairs one of any source (PP69 Prop 5.2).
- "Splices alone" (all measurable T/N splices): **no**. Swap-invariant ones only, and by (a) none of the referee's.

So the round's result is a **class-3 partial theorem**, which is weaker than either partial target of the brief. PP69's §0 says the milestone is not reached; the partial target should be described as narrowed in the same way.

### 2.4 A mis-checked import: sharing applies after all

PP69 §4 dismisses PP68 Prop 1.3 because "nested fills have distinct repairs". But PP69 commits every member's **whole row**, and in 𝒲 the dominator set of a fill is the interval Dom(Y_E) = [θ′(E), θ₃(E)], with θ₃ defined by Φ₃(C_θ₃) = Φ₃(Y_E).

**Prop 2.5 (PROVED).** Let θ lie in the interior of Dom(Y_E), i.e. with strict inequalities at all worlds.
- Then θ ∈ Dom(Y_{E″}) ∩ Dom(Y_E) ∩ Dom(Y_{E′}) for nested E″ ⊊ E ⊊ E′ close to E in measure. Φ is continuous in measure.
- PP68 Thm 1.1(iii) needs only these three nested fills, not every subset of E₀. It refuses rec(Y_E, C_θ) at all three worlds, by the **axioms**.
- So **no selected model at any index may carry rec(Y_E, C_θ)**: it would refuse its own copy at every world.

This is the carrier exclusion of PP68 Prop 1.3(b), for a continuum of (E, θ). It is a bequest to every future assignment. It is not a conflict inside the module.

### 2.5 The transverse tube condition for future interior models

**Prop 2.6 (PROVED).** Let q be an interior index off the arc, p(θ\*) its nearest arc point and d := |q − p(θ\*)|. Let C_q be the model eventually placed at q. Suppose, for some w, Φ_w(C_q) < Φ_w(C_θ\*), and let θ_w be the arc index where Φ_w(C_θ) = Φ_w(C_q). Then PP69's tubes require

  d ≥ ½·min{|p(θ\*) − p(θ_w)|, dist(p(θ\*), ∂Δ)} − o(1).

*Proof.* Use the guidance argument of Prop 2.2(b), with rivals X → C_q worsened at w. ∎

So future models near the arc must approach the arc's Φ-values at a rate fixed by PP69's factor ½. A rule with radius o(margin) removes this constraint at first order. **The radius rule must be revised before any extension near the arc is attempted.**

### 2.6 Other items checked

- **Theorem Q.** PP69's stated reason ("(L0⁺) fails here") is inaccurate: 𝒲 accepts every strictly Φ-positive record out of a member, which is (L0⁺) for members. Q is harmless for the right reason, which PP69 also gives: a strict Bayes member has no Φ-balanced swap. Q(i)'s conclusion is already a 𝒲-verdict.
- **Prop 5.2 (no symmetric repair of other-class fills)** agrees with Prop 1.3, and is correct.
- **Prop 5.3(b)** rests on PP38 Thm 3.1(ii), which I did not re-check.
- **Option A of PP69 §6** (σ-breaking on M₁ ∪ M₂). By Prop 1.3(a), the class-1 and class-2 repairers of one source must be different earlier models. By Prop 2.2(a), any σ-breaking must also keep every future edge model inside min(Φ₁, Φ₂) ≤ Φ₁(D\*), unless the committed rows of members near the edge are revised.

### 2.7 Coordinator's checks: off-arc Bayes acts, Theorem gm, Props 5.2–5.3, the rule, one-sided splices

**(a) What a single additive field gives, and what it cannot.**
- 𝒲 is total, so it satisfies every finitary axiom. Every member is the unique p(θ)-Bayes act, which gives defence, protection and direct (C). θ ↦ Φ(C_θ) is continuous, which gives closed sections on the arc. That is all PP69 claims, and it holds.
- What 𝒲 cannot be is the **final** relation. At a weight λ off the arc, the pointwise argmin X_λ of λ·f exists and is undominated in 𝒲. NUMERICS (`offarc70`, own implementation of PP69's tables):
  - X_λ is **incoherent** at (0.40, 0.30, 0.30), (0.45, 0.35, 0.20), (0.6, 0.2, 0.2) and (0.5, 0.1, 0.4) (LP certificate on a 500-problem sample);
  - the three on-arc controls pass;
  - at offsets 0.02 from the arc the test finds incoherence at θ = 0.15 and 0.85, but not at 0.5; at offset 0.005 it is mostly inconclusive (`offarc70b`).
- So 𝒲 has incoherent undominated models, and global (C) fails **in 𝒲**. That is Theorem gm's conclusion (no additive ranking covers T1 on the full simplex) seen concretely.
- **Why this does not contradict PP69.** Theorem gm needs (S) on the whole simplex. Its proof uses neighbourhoods of several vertices (Y3 §4). PP69 claims only the module on the arc: defence, protection, (C⁺) for P = 𝔽, and sections along the arc. Each holds in 𝒲 regardless of gm.
- **What it implies for extension.** Any extension to D = Δ must **deviate from 𝒲** on some record out of some future selected model. By (IB), every record carried by an arc member keeps its 𝒲-verdict at every future carrier. So the deviation must sit on records that **no arc member carries**: future models must be non-additive exactly off their agreement sets with the arc.
- A 2-D additive sheet around the arc (PP69 Option B / Prop 5.3) is not excluded by gm itself, which needs vertices. But it would have to avoid PP50 Thm K, PP51's kink certificate and PP63 Thm J. Those were proved for posterior or kernel families and are not known in general.
- Prop 2.1 above is the first concrete instance: V₁ at e₁ is incompatible with PP69's uncapped tube.

**(b) Props 5.2, 5.3 and the repair lemma.**
- **Repair lemma: correct** (§2.1, with the one-line proof).
- **Prop 5.2: correct.** Swap-invariance of the relation, with C∘σ = C and B∘σ = B, maps C ⋠₂ B to C ⋠₁ B. Prop 1.3 supplies C ⋠₂ B and C ⋠₃ B.
- **Prop 5.3(a): correct with repair.** The convergence in measure needs the pointwise margin e(g) := min_{a ≠ C_s(g)} λ_s·(f(g, a) − f(g, C_s(g))), which is > 0 a.e. Then

  μ{B_n ≠ C_s} ≤ μ{e ≤ δ} + δ⁻¹·(λ_s·Φ(B_n) − λ_s·Φ(C_s)).

  "Excess > δ" alone does not suffice.
- **Prop 5.3(b): correct.** Lyapunov convexity of the risk set, and a supporting hyperplane at a point that is not strictly dominated.
- **Prop 5.3(c): correct.** The "two-dimensional sheet" is a reading. What is proved is that the weights λ_n are off the arc (on the arc, uniqueness gives B_n = C_θ, which is swap-invariant) and accumulate at weights where C_s is weakly Bayes.
- **CONJECTURE.** In 𝒲 itself the B_n would have to be the unique X_{λ_n}. If those are incoherent near the arc, as (a) suggests at moderate offsets, then no coherent model at all repairs thin other-class fills **in 𝒲**, and 𝒲 must be revised, not merely extended.

**(c) The rule and the arc sections.**
- θ′ is well defined. Φ₁(C_θ) is continuous and **strictly** decreasing, since every band carries switches that lower φ₁ + φ₂ (thresholds cover every subinterval: `thr70` CHECKED; PP69 Cor 3.4(d)). So θ′ is the unique solution, and "earliest" is redundant.
- X ↦ θ′(X) is continuous in Φ₁, so there are no tie pathologies. The world-1 and world-2 ties are exact 𝒲-ties, consistent with every axiom.
- Rivals with Φ₁(X) = Φ₂(X) > Φ₁(T) are outside the rule. Only T can dominate them, and only if Φ₃(T) ≤ Φ₃(X).
- Defence and sections along the arc: correct.
- At the endpoint: Prop 2.1 (error) and Prop 2.2 (price).

**(d) One-sided splices out of T (PP69 T5 made rigorous, for PP69's field).**

**Prop 2.7 (PROVED).** Every switch along the curve lowers Φ₁ = Φ₂ by at most half of what it raises Φ₃ (PP69's tables).
- R-part pairs: δ(τ₁) per 2.
- R_B: (1 − τ₁) per (2 + τ₁).
- J/F pairs: δ(τ₂) per 2.
- F on M₃: (1 − τ₂) per (2 + τ₂).

So Φ₃(C_θ) − Φ₃(T) ≥ 2(Φ₁(T) − Φ₁(C_θ)) for every θ. Hence **no member dominates any rival Z with**

  Φ₃(Z) − Φ₃(T) < 2·max_{w∈{1,2}}(Φ_w(T) − Φ_w(Z)).

This covers:
- every one-sided retreat T[H ↦ S] with H ⊆ L ∩ M₁ (or ⊆ L ∩ M₂). Its world-1 gain is ∫_H (1 + δ)|g| ≥ (11/7)∫_H |g|, while its world-3 loss is ∫_H |g|;
- every class-1 or class-2 fill of T, whose world-3 change is negative.

Whether an axiom-level version holds for every symmetric relation is OPEN.

---

## 3. Conflicts: axiom-level versus choice-level

**Axiom-level: none.** Every clause below is derived from the axioms, but each needs a choice in order to bite.

| Conflict | What it hits | Level |
|---|---|---|
| Later members never repair other-class fills; T's are repaired by no curve member | any 3-descending family (Prop 1.3) | axiom-level **given the family**; avoidable only off the curve |
| A dominator of a class-k fill differs from one of a class-k′ fill (k ≠ k′) of the same interior source | any construction | axiom-level, but costs only distinctness |
| Thin rivals force repairs to accumulate at the source (fills), at u (splices) and at N (other-class) | any in-family repair rule (Prop 1.5) | axiom-level given in-family repairs; kills fixed balls |
| (I8) failure at e₁; non-extendibility | PP69's r(1) | choice (Prop 2.1) |
| Edge squeeze; plateau; wide-K edge ban | PP69's committed rows + any X-independent radius at h₁₂ | choice (Prop 2.2) |
| Carrier exclusion for rec(Y_E, C_θ) | PP69's committed rows (interval dominator sets) | choice (Prop 2.5) |
| Transverse tube rate | PP69's factor ½ | choice (Prop 2.6) |
| N's class-1/2 fills, one-sided splices (including the referee's Prop 7.1 family) unrepaired | 𝒲's symmetry (PP69 Prop 5.2) | choice |

**What would be axiom-level, and was not found.** It would be a fixed rival whose sections along a non-isolated family are forced, by guidance alone, to alternate between worlds, or to accumulate at a guidance refusal. Theorem 1.2 rules this out along the curve. Any such conflict must run through commitments, and PP69's 𝒲 shows that commitments chosen as one total additive relation never produce it on the arc.

---

## 4. Scripts (`r9/PP70_py/`; run `python3 -I -B <script>` in that folder)

| Script → output | Content | Label |
|---|---|---|
| `geom70.py` → `geom70.out` | exact advice along the curve on a 1/48 grid: 3-monotonicity; change census; at most two changes; J = N on class 3 | CHECKED (the G3 line reports sparse J samples on the grid; superseded by `thr70`) |
| `thr70.py` → `thr70.out` | exact thresholds σ, β, τ per region; 12-bin coverage of every region, including targeted J samples; τ ≥ 0.5695 on R_B | CHECKED |
| `lib70.py` | own SAT encoding (guidance, strict (G), (IB) by record variables, (TC) on all triples, competitiveness, rule III, direct (C)) | — |
| `checks70.py` → `checks70.out` | K1 direction lemma; K2 distinct other-class dominators; K3 two-band splice; K4 transferred generalised trap; K5 Kill-A; K6 edge model undefended under C ⪯₁ D, C ⪯₂ D; K7 member record refused at 1, 2 bans edge carriers | CHECKED, ALL PASS |
| `offarc70.py`, `offarc70b.py` → `.out` | own implementation of PP69's field; Bayes acts at off-arc weights; LP coherence test; on-arc controls pass | NUMERICS |
