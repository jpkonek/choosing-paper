# PP20. Completion on the joint class: a clean measurable extension, full competitiveness of T, and where the difficulty goes

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact finite computation on cells. Cells check record bookkeeping only and say nothing about (S). CONJECTURE / OPEN: as stated. NUMERICS: none in the claims. A scipy LP lists candidate coherent patterns for §6, and every pattern used is then certified exactly.

**Scripts** (`r9/PP20_py/`; run `python3 -B <script>` inside the folder; outputs in the `.out` files):

| Script | Content |
|---|---|
| `reclevel.py` | record-level closure engine (rules I–IV) |
| `cells.py` | dense model-level engine: all copies, guidance, rules I–IV |
| `coarsen_check.py`, `coarsen_check2.py`, `coarsen_dense.py` | Theorem 3.2 on cells |
| `coarsen_allT.py`, `coarsen_dense_allT.py` | Theorem 4.3 on cells |
| `zfill_check.py`, `isolate6.py` | §6 checks |
| `geom_coarsen.py` | Lemma 3.1, exact |
| `oldpattern.py` | §2; imports `../PP17_py/records.py` |
| `greedy.py`, `verify.py`, `radial.py`, `run_radial.py`, `single.py`, `geom6.py`, `full6.py`, `full6_reuse.py`, `family6.py`, `verify_full6.py`, `certify6.py`, `search.py` | §6 explorations |

**Inputs.** Brief 45; AUDIT_completion (rules I–IV, F1/F2); PP18; PP19; REFEREE_Z_PP19 (Lemma H, Prop S, §5); AUDIT_six_source; REFEREE_six_source; LEAD_selection_count; DESIGN_MEMO §§8.12–8.13. Only Brief 45's axioms are used.

---

## 0. Verdict

1. **A clean measurable extension for the joint class, and more (Theorem 3.2, PROVED).**
   - *Construction.* Take three coherent **coarsenings** C_1, C_2, C_3 of T (credal sets K_w ⊋ M; Lemma 3.1 gives them explicitly for every ε). Install T ⪯_w C_w. For every rival X that agrees with T on the footprints F_w := {C_w ≠ T}, install C_{w(X)} ⪯_u X at all worlds u, where w(X) is any world at which X worsens T somewhere.
   - *Closure.* The least closure under rules I–IV has no F1, no F2, no completed triangle and no tie at any world. T and the C_w stay coherent and undominated. Every such rival is strictly dominated **at every world**.
   - *Scope.* The rival class contains every model equal to T off its silent mixed set D. That covers all majority, minority, mixed and contradictory fills on arbitrary measurable sets, including the old A_i, B_i and R_i, and X*, Y_12, Λ_T and V_{c*}. It also covers every change of T's *answers* that avoids the footprints.
   - *No protection.* No region is protected and no strict verdict is stipulated.

2. **T is competitive against every model (Theorem 4.3, PROVED).** Add T ⪯_σ Y for **every** model Y outside {T, C_1, C_2, C_3}, at one "safe" world σ(Y), which always exists (Lemma 4.2). The closure stays clean. This settles T's whole defence clause of (S), apart from sections, including the four rivals of the brief at any world where they are not strict improvements. The cascades of point 3 occur exactly in PP19's Lemma-5.0 form, and the safe world dodges them.

3. **Completion is never used, and it could not do more (Lemma 1.3, PROVED).** A triangle containing a guidance link is degenerate or F1. So rule II only ever ties all-mixed triangles. Every kill in PP18, PP19 and Prop S is of the F1 type. Theorems 3.2 and 4.3 avoid those kills by placing defenders, not by completion.

4. **T's old defences (point 1, CHECKED).** In audit's six-source module (PP17 cells), T ⪯_w Y for Y ∈ {Λ_T, V_{c*}, Y_12, X*} can be added at every non-improving world, singly and in all 36 joint choices, with no completion and no F1. PP18 Prop 4.2 is a failure of the zone invariant, not of the closure.

5. **Where the difficulty went (Prop 5.1, PROVED).** No accepted *domination* makes advice correct on the defenders' compensation sets N_w at the two other worlds. By PP18 Theorem Z, any (S)-extension must therefore dominate incoherent rivals that change T **on the footprints**. That is exactly where PP19 Lemma 5.0, Theorems 5–6 and Prop S live, and where the no-triangle argument stops working (§5). The brief's joint class never reaches that territory, because its compensation can be put on T's answered region, which the class does not touch.

6. **Most important next step.** Dominate the incoherent rivals that touch the footprints, starting with the Theorem-Z fills T[Q → u-correct], Q ⊆ N_w. On 6-line geometric cells, with general coherent defenders, there is a clean closure in which T is competitive against all 729 models and every incoherent model is strictly dominated by an undominated coherent one. This is CHECKED and re-verified from scratch (§6), and supports Conjecture 6.1. Do this before attempting selections or sections.

---

## 1. Two closure facts

Setting of Brief 45: three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets; ranks correct 0 < silent 1 < wrong 2 < contradictory 3; T = D_M, M = c·𝟙 + εΔ. Write
- D for the mixed problems on which T is silent,
- Ans for the problems on which T answers,
- Err_u for the problems on which T's answer is wrong at u.

A **record** r = (supp r, old, new). Its rank change at w, δ_w(r), is independent of the context. Call r, at world w:
- of kind **W** if δ_w ≥ 0 everywhere (weak guidance, including the trivial record);
- of kind **I** if δ_w ≤ 0 everywhere and r is nontrivial;
- of kind **M** otherwise.

**Lemma 1.1 (PROVED).** At every problem and world, the four values have distinct ranks. No value is no worse than a coherent model's value at all three worlds, except that value itself.

*Proof.* On a mixed problem the rank vectors over (majority, majority, minority) worlds are A (0,0,2), S (1,1,1), B (2,2,0), X (3,3,3). On U they are (0,0,0), (1,1,1), (2,2,2), (3,3,3), and a coherent model takes the value with vector (0,0,0). No vector of A, S, B is coordinatewise ≤ another. ∎

**Composition.** Copies (P, Q) of r1 and (Q, R) of r2 exist iff new₁ = old₂ a.e. on supp r1 ∩ supp r2. Then r1·r2 := rec(P, R) is: old₁ → new₁ off supp r2; old₂ → new₂ off supp r1; old₁ → new₂ on the overlap. An accepted triangle P ⪯_w Q ⪯_w R ⪯_w P is the same thing as accepted r1, r2, r3 with r3 = (r1·r2)⁻¹. Any two of its records are cyclically adjacent, and adjacent records compose.

**Lemma 1.2 (PROVED).** If one of r1, r2 is of kind W at w and the other of kind M, then r1·r2 has a strict worsening point at w.

*Proof.* At a strict worsening point g of the M record, the W record's change (if any) is weakly upward. So the net change at g is strictly upward, in either order. ∎

**Lemma 1.3 (triangle trichotomy; PROVED).** Suppose the accepted relation at w contains weak guidance and no record of kind I.
- (a) Two accepted records compose to a record of kind I only if both are of kind M.
- (b) A non-degenerate accepted triangle containing a record of kind W is F1.
- (c) Rule II installs only reverses of M records.
- (d) F1 arises in the closure iff one of the following happens:
  - an installed record is of kind I;
  - two accepted M records compose to a record of kind I;
  - rule III reverses an all-world weak domination of a member of P that is of kind W somewhere.

*Proof.* (a) follows from Lemma 1.2 and W·W = W. For (b), rotate so that r3 is of kind W. Then r1·r2 = r3⁻¹ is trivial (a degenerate triangle) or of kind I. In the second case r1 and r2 are both M by (a), and rule II installs r1·r2, the reverse of the strict guidance record r3. (c) and (d) follow. ∎

**Consequence.** Completion can only tie the three records of an all-mixed triangle. PP19 Lemma 0.2, Lemma 5.0, Theorems 4(b), 5, 6 and Prop S each exhibit two M records that compose to a strict improvement. Each is therefore F1 in the closure, as REFEREE_Z_PP19 §5.2 says. In both constructions below, no all-mixed triangle ever arises.

---

## 2. Point 1 in the old pattern (CHECKED)

PP18 Prop 4.2 shows that in audit's six-source module T has no defence **that keeps the zones R_i** against Λ_T, V_{c*} and Y_12. PP17 shows the same for X*. Without the zone requirement, `oldpattern.py` adds T ⪯_w Y to the module on the PP17 cells (21,040 installed records per world) and runs the closure incrementally. Every new triangle or F1 pair must contain a new record, since the module has none (PP17).

**Result.**
- Each of Λ_T, V_{c*}, Y_12 and X* is clean at every world where it is not a strict improvement: worlds 1–3 for Λ_T and V_{c*}, worlds 1–2 for Y_12 and X*.
- All 36 joint world choices are also clean.
- In every case there are 0 completions, 0 F1 and no source dominated.

The full-support rivals Λ_T and V_{c*} compose with module records only where advice matches on whole supports, and that happens nowhere. So Prop 4.2 is a failure of the zone invariant, not of the closure.

**CONJECTURE:** the same holds measurably. I do not pursue it, because §§3–4 replace the module. The cells omit sub-cell rivals and the conic/bounded distinction of Lemma H.

---

## 3. Coarsening defenders (points 2 and 4)

A **coarsening** of T is a coherent C = D_K with K ⊋ M, closed and convex. Wherever T is silent, C is silent. Wherever C answers, it gives T's answer. Its **footprint** F_C := {C ≠ T} lies in Ans, and C is silent there.

**Lemma 3.1 (explicit triple; PROVED; centre inequalities CHECKED exactly at 16 values of ε by `geom_coarsen.py`).** Fix 0 < s < t < c. For each world w put

  q_w := s·e_w + ((1 − s)/2)(𝟙 − e_w),  K_w := conv(M ∪ {q_w}),  C_w := D_{K_w},  g^w := e_w − t𝟙.

There is a non-null open cone N_w around ±g^w on which:
- (i) T answers, C_w is silent, and every C_{w′} with w′ ≠ w agrees with T;
- (ii) T's answer is correct at w and wrong at both other worlds.

Hence N_w ⊆ F_w := F_{C_w}, N_w ⊆ Err_u for u ≠ w, and N_w ∩ F_{w′} = ∅ for w′ ≠ w.

*Proof.* m·g^w = m_w − t.
- On M, m_w ≥ c > t, so T accepts g^w.
- q_w·g^w = s − t < 0, so K_w straddles g^w and C_w is silent.
- For w′ ≠ w, q_{w′}·g^w = (1 − s)/2 − t > 0, because t < c < 1/3 < (1 − s)/2. So all of K_{w′} accepts g^w.

These are strict inequalities on compact sets, so they persist on a neighbourhood. Accepting g^w is correct exactly at the one world with a positive coordinate, namely w. ∎

### Theorem 3.2

Let C_1, C_2, C_3 be any coarsenings with sets N_w as in Lemma 3.1, and put F := F_1 ∪ F_2 ∪ F_3. Let

  𝓛 := {X : X = T a.e. on F}.

𝓛 contains every model equal to T off D. For X ≠ T let W(X) := {w : X is strictly worse than T at w on a non-null set}. W(X) is nonempty by Lemma 1.1.

**Installation.** Choose 𝓛_0, 𝓛_1 ⊆ 𝓛 ∖ {T}, a world w(X) ∈ W(X) for each X ∈ 𝓛_0, and a nonempty W_1(X) ⊆ W(X) for each X ∈ 𝓛_1. Install, with all copies:
- (a) a_w := rec(T, C_w) at world w;
- (b) b_X := rec(C_{w(X)}, X) at every world, for X ∈ 𝓛_0;
- (t) t_X := rec(T, X) at every w ∈ W_1(X), for X ∈ 𝓛_1.

Register P_0 := {T, C_1, C_2, C_3}.

**Theorem 3.2 (PROVED).** The closure under rules I–IV consists of the weak guidance records and the copies of the installed records, with P = P_0. Hence:
1. There is no F1, no F2, no completed triangle, and no tie at any world.
2. Strict (G), (IB) and (TC) hold. T and the C_w are coherent and undominated. Direct (C) holds for P, and (LA) holds.
3. Each X ∈ 𝓛_0 is strictly dominated at every world by C_{w(X)}.
4. T ⪯_w X for each X ∈ 𝓛_1 and w ∈ W_1(X), and T ⪯_w C_w.

This holds for every choice of 𝓛_0, 𝓛_1, w(·) and W_1(·), with arbitrary measurable (bounded or conic) supports.

*Proof.* Supports:
- supp a_w = F_w: old T, new S.
- supp b_X = F_{w(X)} ∪ supp X (disjoint): on F_{w(X)}, S → T; on supp X, T → X.
- supp t_X = supp X: T → X.

Call a and t **T-out**: their old side is T. The new side of every b equals T on F.

*Step 0 (no installed record is of kind I).*
- a_w worsens at w on N_w.
- t_X worsens at w ∈ W(X).
- b_X worsens at w(X) on supp X.
- At u ≠ v := w(X), b_X turns S into T's u-wrong answer on N_v.

So **every b worsens somewhere at every world.**

*Step 1 (no F1 pair).* By Lemma 1.3, check pairs of installed M records at a world w.
- **(t_Y, t_{Y′}):** composable only if supp Y ∩ supp Y′ is null; the composite is the union and keeps a worsening point.
- **(a_w, a_w):** not composable (S ≠ T on F_w).
- **(a_w, t_Y), either order:** disjoint supports; the union worsens on N_w.
- **(t_Y, b_X):** composability needs Y = C_{w(X)} = T on supp Y ∩ supp X. So the supports are disjoint and the composite is the union.
- **(b_X, t_Y):** composability needs X = T on supp X ∩ supp Y. Again disjoint, union.
- **(b_X, b_{X′}):** composability needs T = S on F_{w(X)} ∩ F_{w(X′)} and X = T on supp X ∩ supp X′. So both overlaps are null and the composite is the union. Each b worsens at every world.
- **(a_w, b_X) and (b_X, a_w), with v = w(X):** always composable. Both C_w and C_v are silent on F_w ∩ F_v, and X = T there. In both orders the composite is T → S on F_w ∖ F_v, S → T on F_v ∖ F_w, and T → X on supp X.
  - If v = w, this is t_X, which worsens at w.
  - If v ≠ w, N_w ⊆ F_w ∖ F_v and T is w-correct there, so T → S worsens.

*Step 2 (no triangle).* By Lemma 1.3(b), a non-degenerate triangle would consist of three installed M records.
- **All three T-out:** after the first one acts at g, the advice is no longer T(g), and the other two cannot act at g.
- **Exactly one b, say b_X:** at g ∈ supp X it moves T(g) to X(g) ≠ T(g), and the two T-out records cannot act at g.
- **At least two b:** two of them are adjacent, so by Step 1 they compose to a disjoint union. The closing record is the inverse of that union. Its old side is X ≠ T on supp X, so it is not T-out. Its new side is S on F_{w(X)}, so it is not a b.

So rule II is idle.

*Step 3 (rule III idle).*
- **N = T.** No installed record has new side T throughout its support. So an all-world dominator X of T would satisfy X ≤ T pointwise at every world, hence X = T by Lemma 1.1.
- **N = C_w.**
  - A copy of a_{w′} ends at C_w only if F_{w′} ⊆ F_w. That is excluded for w′ ≠ w by N_{w′} ∩ F_w = ∅. For w′ = w the record is a_w, which is accepted only at w: at u ≠ w it is not guidance, because of N_w.
  - No t or b ends at C_w, since their new side is a rival ≠ T on its support, where C_w = T.
  - Pure guidance at all worlds gives X = C_w.

Rule IV adds nothing.

*Conclusions.*
- Items 1, 2 and 4 follow.
- For item 3: b_X⁻¹ is never accepted.
  - It is not guidance, by Step 0.
  - Its old side X ≠ T on supp X excludes a and t.
  - Its new side S on F_{w(X)} excludes b.

So X ⪯_u C_{w(X)} fails at every u. ∎

**CHECKED (bookkeeping).** `coarsen_check.py` (up to 728 rivals, 1,330 records per world, with contradiction values), `coarsen_check2.py` (rivals also changing T's answers off F; all-world t; source records C_w ⪯_u T) and `coarsen_dense.py` (729 models, every copy, model-level rules) all report ALL PASS: 0 F1, 0 completions, P unchanged.

**Remarks.**
- **PP19 is respected.** T defends C_w only at w, as in Theorem 4(b). Theorem 5's compensation set for class-w fills is N_w. Theorem 6(b) holds on N_w, where C_w is silent and the other defenders give T's answer.
- **The PP17 all-worlds rule now works.** With W_1 = W, T ⪯_w X holds at every world where X is not a strict improvement. No t copy can end at a defender, because t's support avoids F.
- **Not additive in disguise (PROVED).** With W_1 = W, no finite, finitely additive rank-step charge that is positive on non-null sets (PP17's class R3) weakly endorses the world-1 comparisons out of T.

  *Proof.* For non-null E_1 ⊆ D ∩ M_1 and E_2 ⊆ D ∩ M_2, the fill T[E_1 ∪ E_2 → A] worsens at 1, so T ⪯_1 it is accepted, and endorsement gives ν₂(E_1) ≥ ν₁(E_2). Fix E_2 = D ∩ M_2. Splitting D ∩ M_1 into n non-null pieces gives one piece with ν₂ ≤ ν₂(D ∩ M_1)/n < ν₁(E_2) for large n. Every world is symmetric. ∎

---

## 4. Point 1 for every model, and the shape of cascades (point 3)

Every rival in Theorem 3.2 avoids F. Now let T defend against **every** model.

**Lemma 4.1 (cross-pair kills; PROVED).** Let Y ≠ T be any model, and let b_X be installed with defender C_w and X ∈ 𝓛. If one of the composites t_Y·b_X or b_X·t_Y exists and is of kind I at u, then:
- (i) u ≠ w;
- (ii) Y ≤_u T a.e. on supp Y ∖ F_w;
- (iii) Y ≤_u S a.e. on supp Y ∩ F_w;
- (iv) N_w ⊆ supp Y a.e.

*Proof.* Both composites need supp X ∩ supp Y null. When defined they consist of:
- T → X on supp X;
- T → Y on supp Y ∖ F_w;
- S → T on F_w ∖ supp Y;
- on supp Y ∩ F_w: the identity (for t·b, which forces Y = S there), or S → Y (for b·t).

Kind I needs each part to be ≤_u 0.
- From the first part: X ≤_u T on supp X, so u ∉ W(X) ∋ w = w(X), which gives (i).
- The second and fourth parts give (ii) and (iii).
- The third part needs T to be u-correct a.e. on F_w ∖ supp Y. Since N_w ⊆ Err_u for u ≠ w, this gives (iv). ∎

This is PP19 Lemma 5.0, written for a coarsening defender. It is the general shape of a cascade here: a T-defence whose record touches a footprint, composed with a domination out of that footprint's defender.

**Lemma 4.2 (a safe world always exists; PROVED).** For each Y ≠ T (in particular each Y ∉ P_0), call u ∈ W(Y) *safe* if no installed b_X makes t_Y·b_X or b_X·t_Y of kind I at u. Every Y ≠ T has a safe world.

*Proof.* Take u₀ ∈ W(Y). If u₀ is not safe, Lemma 4.1 gives w ≠ u₀ with N_w ⊆ supp Y and Y ≤_{u₀} S on N_w. So on N_w, Y is silent or gives the u₀-correct answer. T is w-correct on N_w and u₀-wrong there. So both of Y's possible values are strictly w-worse than T, and w ∈ W(Y).

Suppose w is not safe. Then Lemma 4.1 at world w gives w′ ≠ w with Y ≤_w T a.e. on supp Y ∖ F_{w′}. But N_w ⊆ supp Y ∖ F_{w′}, because N_w ∩ F_{w′} = ∅, and Y is strictly w-worse than T on N_w. This is a contradiction, so w is safe. ∎

**Theorem 4.3 (PROVED).** To Theorem 3.2's installation add t_Y at one safe world σ(Y), for **every** model Y ∉ P_0. (T is already defended against C_w by a_w. Adding t_{C_w} at a second world could create a tie.) The conclusions of Theorem 3.2 still hold: closure = guidance plus copies, P = P_0, no F1, F2, triangle or tie. In addition, **T is competitive against every model.**

*Proof.* The new records are T-out and installed at worlds in W(Y). So Step 0 holds, and Step 2 goes through verbatim.

Step 1 changes only in two places:
- **(a_w, t_Y):** composable only when F_w ∩ supp Y is null (S ≠ T, resp. Y ≠ T, on the overlap), and then the composite is the union.
- **(t_Y, b_X), (b_X, t_Y):** handled by safety.

Step 3 changes only for t copies ending at some C_w. Such a copy needs supp Y ⊆ F_w and Y = S there. Y ≠ C_w here, since Y ∉ P_0, so the record t_Y differs from a_w and is installed only at σ(Y). For it to be accepted at all three worlds, it would have to be guidance at the two worlds other than σ(Y). Then T would be correct at those two worlds throughout supp Y. A mixed answer is right at most at two worlds, so T would be wrong at σ(Y) throughout supp Y, and Y would be strictly better there. That contradicts σ(Y) ∈ W(Y).

No t record ends at T. Finally, b_X⁻¹ is not a t record, because its old side is X ≠ T on supp X. ∎

**CHECKED.**
- `coarsen_allT.py` (record level): 8 cells, all 6,561 models defended by T, 242 dominated rivals, safe worlds chosen by the recipe of Lemma 4.2. ALL PASS: 0 F1, 0 completions, P unchanged.
- `coarsen_dense_allT.py` (model level): 6 cells, all copies. T is defended against all 729 models with no tie at any world and P unchanged.

**The general shape of cascades, and how the design avoids them.** By Lemma 1.3, a cascade needs an all-mixed triangle, or two accepted M records composing to a strict improvement.

The design meets two conditions:
- **(R1)** defenders equal T on every rival's support;
- **(R2)** every rival differs from T somewhere (exposure).

These two conditions remove every triangle, because T-out records cannot follow a b record on a rival's support. They also remove every bad pair except two kinds:
- the (a, b) cross pairs, which reduce to one geometric condition per pair of defenders: C_w must lose to T at w somewhere outside F_v (Lemma 3.1(i)–(ii));
- T-defences touching a footprint, which are cascades of Lemma 4.1 type. Lemma 4.2 always finds a world that dodges them, because a kill at u through C_w forces Y to be strictly worse than T on N_w, where no other defender is present.

The audit §1 pattern (T ⪯_i C ⪯_i X ≺^G_i T) is the (a, b) pair with v = w. It is avoided by assigning to C_w only rivals that worsen at w.

---

## 5. What is secured, and what remains (point 4)

**Secured (PROVED).**
- T is coherent, undominated, and competitive against **every** model.
- Three coherent undominated defenders exist.
- Strict (G), (IB), (TC), (LA), and direct (C) for P all hold.
- Every model that agrees with T on the footprints is strictly dominated at every world.
- No region is reserved, and no completion or tie is needed.

**Not secured.**
1. Domination of incoherent models that change T on the footprints.
2. The defenders' own competitiveness, and any selection p ↦ C_p, beyond the three defenders.
3. Closed sections, which are not finitary (AUDIT_completion §6).

Item 1 is forced:

**Proposition 5.1 (residual zone for dominations; PROVED).** In the closure of Theorem 4.3, fix u and w ≠ u. No accepted comparison of the form "member of P ⪯_u X at every world" makes advice u-correct on a non-null part of N_w. Hence any system satisfying (S), (IB), strict (G) and direct (C) that contains this closure must also dominate, out of a selected model, an incoherent rival that makes advice u-correct on part of N_w (PP18 Theorem Z with R = N_w). Such a rival changes T on F_w.

*Proof.* A record accepted at all three worlds out of a member of P is one of the following:
- **Guidance at the world in question.** Guidance changes advice only upward in rank (Lemma 1.1), so it never reaches rank 0 from rank ≥ 1.
- **A copy of a b record.** On N_w these act only through defender C_w, as S → T's answer, which is u-wrong.
- **A copy of a_w.** This is accepted only at w.
- **A copy of t_Y, installed at σ(Y) and guidance at the other two worlds.** If σ(Y) ≠ u, the record is guidance at u, and the first case applies. If σ(Y) = u, the only u-correct value at a point of N_w is the answer opposite to T's. That answer is also correct at the third world, so the record improves there and is not guidance there.

The t records are not all-world dominations. They do make advice correct on N_w, which is why T is competitive, and why PP18 Prop 4.1 is not violated. ∎

**Why the old no-triangle argument stops working there.** Once a dominated rival Z touches F_w, its b record can end with silence on a footprint. Then the closing record in Step 2 can be a b record, and triangles become possible. Rivals that touch footprints are also where Lemma 5.0, Theorems 5–6 and Prop S constrain *dominators* rather than T. The joint class of Brief 45 is a weaker test than intended. Its compensation can always sit on T's answered region, which none of its rivals touch.

---

## 6. Toward rivals on the footprints (CHECKED on cells; CONJECTURE)

**Silent-set cells.**
- *Conic cells.* On 6 conic silent cells with *refinement* defenders only (`greedy.py`, `verify.py` → `greedy_verify.out`), a greedy co-design (seed 0) finds a clean closure. It has:
  - all 106 incoherent majority and minority fills strictly dominated by registered refinement defenders;
  - T defended against all 126 fills and against X*, Y_12, Λ_T and V_{c*};
  - every registered model undominated;
  - no tie at any world and no completion.
- *Radial halves.* Splitting each silent line into two radial halves models Lemma H (`radial.py`, `run_radial.py`). Then a half-cell majority fill has **no** clean refinement defender when there is only one silent line per class (`single.py`). In this coarse geometry, every coherent refinement that beats T at both majority worlds off the fill says A on the fill's whole line, so it is not exposed (`single.out`). Coarsenings escape this, because their compensation is off D.

**The full cell domain** (`geom6.py`, `full6.py`).
- *Model.* One silent line and one footprint line per class, with general coherent K ⊆ Δ.
- *Coherent patterns.* An LP with a margin lists 141 coherent patterns. All 141 are certified exactly by rational convex hulls (`certify6.py` → `certify6.out`). The other 588 patterns are treated as incoherent. If any of them were coherent, dominating it would be harmless.
- *Seed.* Theorem 3.2.
- *T's defences.* T is defended against all 729 models.
- *Domination.* Dominators for every incoherent model, including those that change T on the footprint lines, were searched for by greedy co-design (`full6.py`, each step a full closure).
  - **Random order.** Every run with a random order (three runs) left between one and five leftovers. They come from one structured family: a two-class majority fill on D, plus silencing of one of those classes' footprints and flipping of the other's (e.g. AASSAB, ASAABS, SAABSA). Each leftover has 12–46 clean dominators on the Theorem 3.2 seed alone, and the whole family has a joint repair (`family6.py`, backtracking, found at once). So these were failures of the greedy order.
  - **Family first.** Processing that family first gives a complete result (`full6_success.out`). It was re-verified from scratch, not incrementally, by `verify_full6.py` → `verify_full6.out`:
    - T is competitive against all 729 models;
    - all 588 incoherent models are strictly dominated by registered coherent models (63 defenders besides T);
    - every registered model is undominated;
    - there is no F1, no F2, and no tie at any world, so no completion was ever needed.

  This is the cell version of "(S) at T, without a selection and without sections": T's defences, plus domination of every incoherent model by an undominated coherent one. The cells omit sub-cell rivals, Lemma H, and every infinite family. They are evidence about record algebra only.

**Theorem-Z fills on a footprint.** Let Z = T[Q → u-correct] with Q ⊆ N_w and u ≠ w. Then Z worsens only at w, so W(Z) = {w}. By Lemma 0.2, its dominator must be one that T defends at w.

- **Part of the footprint (CHECKED).** The defender C_w itself works when Q leaves part of F_w ∩ Err_u and of F_w ∩ Err_v outside Q. Then rec(C_w, Z) worsens at every world. This was checked by `zfill_check.py`, with footprints split into two cells: on top of Theorems 3.2 and 4.3 there were 0 F1 and 0 completions.
- **The whole of C_w's errors (PROVED).** If Q ⊇ F_w ∩ (Err_u ∪ Err_v), then rec(C_w, Z) is a strict improvement at u. On F_w ∖ Q it turns S into T's u-correct answer, and on Q it turns S into the u-correct answer. So C_w cannot serve Z. A *second* defender that T defends at w is needed, for example a coarsening whose footprint is disjoint from F_w.

**CONJECTURE 6.1.** There is a clean closure under rules I–IV, containing that of Theorem 4.3, in which every incoherent model is strictly dominated by a registered, undominated coherent model. Its dominators for footprint rivals vary with the rival.

The measurable evidence comes in two parts.
- *What is proved.* Theorem 4.3 covers T's side completely. Footprint rivals that leave part of a footprint's errors untouched can be served by that footprint's own defender (above).
- *What is checked on cells.* The 6-line cells give the full statement.

The first measurable case to prove is the following: rivals that touch only F_w and worsen at some w′ with F_{w′} ∩ supp Z = ∅, served by C_{w′}. Every pair condition of §3 survives there. What remains is the b·b compositions in which S on a footprint meets Z, and the triangles that such compositions could close. These are exactly the records that Step 2 of Theorem 3.2 excluded by the hypothesis that rivals avoid F. The cell leftovers show which rivals need co-design first: two-class majority fills combined with silencing one footprint and flipping another.

**Most important next step.** Prove Conjecture 6.1 measurably. Start with the rivals that Prop 5.1 forces:
- the whole-footprint Theorem-Z fills T[Q → u-correct] with Q ⊇ F_w ∩ Err_u, which need a second defender that T defends at w;
- the Lemma-5.0 rivals T[F_w ∩ Err_u → S].

The concrete design question is whether a second coarsening triple, with footprints disjoint from the first and chosen depending on the rival, keeps the cross-pair condition of §4. That condition is "each defender loses to T at its own world outside the other footprints". A finite measure admits only countably many pairwise-disjoint non-null footprints (the counting behind the lead's Lemma D), so the triples must share footprints, and that sharing is the point to test. Only after this does the next layer begin: the defenders' own competitiveness (a selection), and then sections.
