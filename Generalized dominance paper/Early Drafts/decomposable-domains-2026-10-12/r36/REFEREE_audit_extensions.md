# Referee report: "Two extensions found by audit" (Separation-Gated Evaluators, §4)

This is an adversarial reading of §`sec:audit` (lines 464–524 of `Separation-Gated-Evaluators.tex`). I read it against `REFEREE_gate2d.md` and `weakgate.py`. I did not edit the note. New files, all in `gate2d/`:
- `referee_audit_ext.py` and `referee_audit_ext_out.txt`: an independent exact-arithmetic checker for both gates and both verdicts. It does not import `check.py`.
- `referee_audit_controls.py`: negative controls for that checker.
- `referee_three_world_count.py` and `referee_three_world_count_out.txt`: the three-world step count.
- `referee_fixed_model_endorse.py` and `referee_fixed_model_endorse_out.txt`: endorsement out of one fixed selected model, plus the two record ratios.

## Summary

| Item | Verdict |
|---|---|
| 1a. Coordinated verdict satisfies (V1)–(V3), and Φ₂ = −Φ₁ on regular changes | **CONFIRMED** |
| 1b. The two indispensable-defence examples | **CONFIRMED** (arithmetic, side of t = ½, out of C_{1/2}). There is a wording caveat on what "indispensable" means: see 1d. |
| 1c. Non-endorsement at both worlds, including finitely additive charges | **CONFIRMED WITH REPAIR**. Prop 5(b)'s records have mass ratio 2. Under the coordinated verdict these give Φ₁ = Φ₂ = 0, so they are *not* indispensable defences. Use a ratio in (1,2), for example 3/2. Also, the argument runs across a dense set of selected models, not out of the target alone. Out of the target alone, a positive field *does* endorse. |
| 1d. Framing ("redundant" vs "indispensable") | **CONFIRMED WITH REPAIR** (wording) |
| 2a. Weak gate: no cycles, using only β_j < γ_j | **CONFIRMED** |
| 2b. Weak gate: Lemma 3, undominatedness, sections, direct (C), domination of the rest, strict (G) | **CONFIRMED**. There is no new failure of strict (G). One typo: the world-2 threshold is 1 − p. |
| 2c. Weak gate: "Prop 6's rival passes the weak gate everywhere" | **CONFIRMED WITH REPAIR**: this needs the key convention that contradiction and unanimous steps have the lowest keys. Prop 6 allows arbitrary keys. |
| 3. Three-world count Σ off_i ≤ 2 Σ on_i, and "some verdict is nonnegative" | **CONFIRMED WITH REPAIR**: the count is **WRONG** for "a model with regular advice" as written. It is true for a model that is regular on mixed problems and *correct on unanimous problems*, for example any coherent model. The bound is sharp. The sentence about the "three-world task" omits undominatedness. |
| 4. Finite checks | No failure in 100 configurations (2 gates × 2 verdicts × 25), plus 6 targeted layouts. The controls are caught. The three-world count is enumerated exhaustively. |

Nothing here breaks Theorem 4 or its weak-gate version. The substantive repairs are 1c (ratio and scope) and 3 (the hypothesis on unanimous problems).

---

## 1. The coordinated verdict

**Definitions.**
- α = 2 on mixed problems with t < ½, α = ½ on mixed problems with t > ½, and α = 1 on unanimous problems. On a mixed problem the (g,3) steps carry α(t). The value at t = ½ is irrelevant, since that set is null.
- Φ₁ = ∫_{T^on₁} α dν − ν(T^off₁).
- Φ₂ = ν(T^on₂) − ∫_{T^off₂} α dν.

### 1a. (V1)–(V3): CONFIRMED

**(IB).** α is a fixed bounded function of the problem, and T^on, T^off are determined by the advice on the difference set. So Φ_i depends only on that advice.

**(V1).**
- α ≤ 2.
- Passing from C_p to C_q changes T^on_i and T^off_i only over the problems where C_p and C_q differ, by at most 3 steps per problem.
- So |Φ_i(C_q,X) − Φ_i(C_p,X)| ≤ 6 μ(C_p △ C_q) → 0.
- The discontinuity of α at t = ½ is in the *problem* variable, not in the index p. It plays no role in (V1).
- Nor does it play a role anywhere in Theorem 4, which needs only that Φ_i is real-valued, satisfies (IB) and satisfies (V1)–(V3).

**(V2).**
- If T^on is null and T^off is non-null: Φ₁ = −ν(T^off₁) < 0, and Φ₂ = −∫_{T^off₂} α < 0, because α ≥ ½ > 0.
- If T^off is null: Φ_i ≥ 0.

**(V3).** I checked the change at a single mixed problem, out of C_p. The world-1 rank is r ∈ {0,1,2} and the world-2 rank is 2 − r.
- *Regular change r → r'.* Let δ = r' − r.
  - If δ > 0, world 1 adds δ steps and world 2 removes δ steps at the same problem. The contributions are α·δ to Φ₁ and −α·δ to Φ₂.
  - If δ < 0, the contributions are −|δ| to Φ₁ and +|δ| to Φ₂.
  - This covers the two-step changes P ↔ M (|δ| = 2). The contributions cancel exactly, because the same problem carries the same α at both worlds.
- *Into contradiction.* World 1 adds 3 − r steps, contributing α(3 − r) ≥ 0. World 2 adds 1 + r steps, contributing 1 + r > 0. Nothing is removed, because C_p is never contradictory.
- *Unanimous problems.* C_p is correct there, with ranks (0,0). Every change adds the same number of steps at both worlds, and α = 1.
- So Φ₁ + Φ₂ = ∫_{c₁} α dν + ν(c₂) ≥ 0, where c₁ and c₂ are the world-1 and world-2 steps of the second kind. (V3) follows, in fact at every p and not just interior p.

The checker tests this exactly. It found no case of Φ₁ + Φ₂ < 0, and no case of Φ₁ + Φ₂ ≠ 0 on rivals that differ from C_p only by regular mixed changes, over all models × all critical indices × 25 + 3 layouts.

### 1b. The two examples: CONFIRMED

The target is C_{1/2} = 𝒟_{[1/3, 2/3]}.

**Near t = 1/3.**
- The rival is silent on Q just below 1/3. This changes P to S: world-1 rank 0 → 1 (an added (g,1) step, α = 2), and world-2 rank 2 → 1 (a removed step, α = 2).
- It accepts g on R just above 1/3, with μ(R) = 3/2·μ(Q). This changes S to P: world-1 rank 1 → 0 (removed), and world-2 rank 1 → 2 (added, unweighted).
- Φ₁ = 2m − 3/2 m = m/2.
- Φ₂ = 3/2 m − 2m = −m/2.
- Uniform additive at world 1: on − off = −m/2 < 0, so it favours the rival. ✓

**Near t = 2/3.**
- The rival is silent just above 2/3. World-2 rank 0 → 1 (an added step, unweighted mass m). World-1 rank 2 → 1 (removed, mass m).
- It accepts −g just below 2/3, with mass 3/2 m. World-2 rank 1 → 0 (removed, weighted ½·3/2 m). World-1 rank 1 → 2 (added, weighted ½·3/2 m).
- Φ₂ = m − 3/4 m = m/4.
- Φ₁ = 3/4 m − m = −m/4.
- Uniform additive at world 2: m − 3/2 m < 0, so it favours the rival. ✓

**Side of t = ½ and origin of the records.** For small ε every step lies in (1/3 − ε, 1/3 + 3ε) ⊂ {t < ½}, or in (2/3 − 3ε, 2/3 + ε) ⊂ {t > ½}. Both records are modifications of C_{1/2}, and both stay inside the band where C_{1/2} is silent, on the correct side. ✓

**Finite cells.** `indispensable()` lists, out of C_{1/2}, the rivals defended at exactly one world whose additive evaluator at that world refuses. They exist in 14 of the 28 layouts:
- world 1: 2 to 18 rivals per layout;
- world 2: 2 rivals in one random layout, and 1 in the layout with cells straddling 2/3.

### 1c. Non-endorsement: CONFIRMED WITH REPAIR

**(i) The ratio.** Prop 5(b)'s world-1 record has μ(R) = 2μ(Q).
- Under the coordinated verdict at t₀ = l(p) < ½, this gives Φ₁ = 2m − 2m = 0.
- Because Φ₂ = −Φ₁ on regular records, it also gives Φ₂ = 0. So *world 2 also accepts it*. Its world-2 additive balance is 2m − m > 0.
- That record is therefore not an indispensable defence. At world 2, Prop 5(b)'s record (ratio 2, weight ½ on removals) likewise gives Φ₂ = 0 = Φ₁.

**Repair.** Use any ratio r ∈ (1,2), for example the note's own 3/2.
- World 1: Φ₁ = (2 − r)m > 0 > Φ₂. Endorsement requires ∫_R f ≤ ∫_Q f. At a Lebesgue point this gives r·f(g₀) ≤ f(g₀), a contradiction.
- World 2, at t₀ = u(p) > ½: Φ₂ = (1 − r/2)m > 0 > Φ₁. The same estimate contradicts endorsement.
- Both computations are in `referee_fixed_model_endorse_out.txt`: ratio 2 gives Φ₁ = Φ₂ = 0, and ratio 3/2 gives ½ and −½.
- The l(p) = u(p) variant needs the same tweak. Use μ(R) = (1 − η)μ(Q), which gives Φ₁ = 2ηm > 0 > Φ₂. Endorsement then needs (1 − η)f₂ ≤ η f₁ at g₀; choose η < f₂/(f₁ + f₂) at g₀. This case does not arise for the note's family, where l < u on (0,1).

**(ii) Scope.** The sentence "Out of the target, a rival … The Lebesgue-point argument … shows that no … field … endorses these indispensable defences" reads as if the non-endorsement concerned defences out of C_{1/2}. It does not, and cannot.
- For any *fixed* selected model C, the following positive two-valued field endorses every accepted comparison out of C:
  - world 1: f = 1 on U₁(C) and f = α off it;
  - world 2: f = α on U₂(C) and f = 1 off it.
- The reason: acceptance says ν(T^off₁) ≤ ∫_{T^on₁} α, and the gate puts T^off₁ inside U₁(C) and T^on₁ outside it. World 2 is the same.
- `referee_fixed_model_endorse.py` checked this on 233,064 accepted comparisons out of 16 selected models per layout: 0 failures.
- The same field, with α replaced by 2, works for the sticky instance. So the "fixed boundary point" caveat in Prop 5(b) is understated: one positive field endorses *everything* out of any one fixed selected model.
- The Lebesgue argument needs C_p with p = l⁻¹(t₀) for a.e. t₀ < ½ (world 1), or p = u⁻¹(t₀) for a.e. t₀ > ½ (world 2). For the note's family these are dense subsets of p < 5/8 (since l(5/8) = ½) and of p > 3/8 (since u(3/8) = ½).

**Repair (wording).** Say "no strictly positive integrable field … endorses the indispensable defences out of the selected models C_p, p in a dense set; out of the target alone, a positive field endorses all of them".

**(iii) Finitely additive charges.**
- The Yosida–Hewitt carrier argument of Prop 5(b) transfers unchanged once the ratio is r ∈ (1,2).
- One step behind "carried by a set Z with ν(Z) < η" deserves a line. A positive purely finitely additive π_p that vanishes on null sets gives, for each n, a set E_n with ν(E_n) < η2⁻ⁿ and π_p(E_nᶜ) < 1/n. Then Z = ⋃E_n has ν(Z) < η and π_p(Zᶜ) = 0. So exact carriers exist.
- Wording: "positive bounded finitely additive charge" should read "a bounded charge vanishing on null sets and positive on non-null sets", as in Prop 5.

### 1d. Framing: CONFIRMED WITH REPAIR (wording)

The paragraph calls the sticky instance's extra defences "redundant", on the ground that "world 2 already defends additively".

In that sense, redundancy is *unavoidable for every two-world instance*:
- on regular mixed records, ν(T^on₁) = ν(T^off₂) and ν(T^off₁) = ν(T^on₂);
- so the two uniform additive balances are exact negatives of each other;
- so whenever world 1's additive evaluator refuses, world 2's accepts.

The coordinated repair makes the defences indispensable in a different sense: *world 2's own verdict* refuses. In every indispensable case found on finite cells, the other world's uniform additive evaluator defends the rival (the `indisp_*_other_world_additive_defends` counts equal the `indisp_*` counts in every layout).

Both senses are legitimate. The paragraph should say which one it delivers: "only one world *of the system* defends, …". It should also add that the in-system sense is the only one available in two worlds.

## 2. The weak gate

The weak gate is: T^on_i non-null, and essinf_{T^on} k_i < essinf_{T^off} k_i (vacuous when T^off is null).

### 2a. No cycles: CONFIRMED

I re-read the proof of Lemma 2.
- With β_j = essinf T^on_j and γ_j = essinf T^off_j (+∞ for a guidance step), it uses:
  - (a) β_j < γ_j for every nontrivial step;
  - (b) T^off_j ⊆ {k ≥ γ_j} a.e., which holds by definition of essinf;
  - (c) T^on_{j*} ∩ {β* < k < γ} is non-null, which follows from essinf = β*, β* < γ and a null level set.
- The strong-gate chain β_j < esssup ≤ γ_j was only a route to (a). The weak gate gives (a) directly.
- Guidance steps still have T^on non-null, because ranks determine the advice.
- In finite cells the window should be [β*, γ), since the level set of β* is an atom. The checker's topological sort confirms acyclicity with the weak gate in every configuration.

### 2b. Lemma 3, undominatedness and the rest of Theorem 4: CONFIRMED

**Lemma 3.**
- Out of C_p, T^on ⊆ {k ≤ p}. Non-null, with null level sets, gives essinf < p ≤ essinf T^off.
- At world 2 the threshold is 1 − p. The note writes p for both worlds: a typo.
- More simply, the weak gate contains the strong gate whenever T^on is non-null (β < esssup ≤ γ). So Lemma 3 for the weak gate follows from Lemma 3. The checker confirms the containment as relations: 0 failures.

**Undominatedness.**
- Into C_p, T^on ⊆ {k ≥ p}, so essinf T^on ≥ p.
- A non-null T^off ⊆ {k ≤ p} has essinf < p. So the weak gate fails unless T^off is null.
- The rank-pair argument then applies unchanged.

**The rest.**
- The section identity uses the same four cases, with Lemma 3 (weak). Closedness follows from (V1). Competitiveness follows from (V3) and the vertices.
- Direct (C) and "domination of the rest" use only antisymmetry and closedness, both of which still hold.
- The checker confirms the section identity, competitiveness at all critical indices and undominatedness, for both verdicts.

**Strict (G).**
- The weak gate still requires T^on non-null. So a strict pointwise improvement, which has T^on null and T^off non-null, is rejected.
- Guidance is unchanged.
- The checker finds 0 strict-(G) failures over all pairs.
- There is no new failure.

**Not claimed, not checked.** The note claims only Theorem 4 for the weak gate.
- Prop 5 transfers, since out of selected models both gates pass and the relations coincide there.
- The leading-charge argument of Remark 7 does *not* transfer verbatim. It needs essinf P ≥ essinf D, so D must be the bottom of S in key. For a charge concentrated at the bottom of the key order the split may then fail. Nobody should cite Remark 7 for the weak gate without a new argument.

### 2c. The three-world sentence: CONFIRMED WITH REPAIR

"Contradiction … adds steps with the lowest keys at every world" holds under §1's convention, where j = 3 and unanimous steps have keys in (−2, −1), below all regular mixed steps. Prop 6 is stated for *arbitrary* keys k_i.

**Repair.** "…for keys that, as in Section 1, put contradiction and unanimous steps lowest."

Two further observations for the authors:
- Under that convention, *every* rival that adds a contradiction step or makes a unanimous change passes the weak gate at every world. The weak gate restricts only rivals made purely of regular mixed changes.
- The escape of Prop 6's particular rival is therefore not evidence that the weak gate gives (S) in three worlds.
  - An analogue of Prop 6 for the weak gate would use regular rivals only: replace C_p by D_i's advice on low-key world-i steps b_i, which must lie below every world-i step added by the changes at b_{i'}, i' ≠ i.
  - I have not examined it.

The sentence "Proposition 6 is a statement about the strong gate only" is correct.

## 3. The three-world count

### Is Σ off_i ≤ 2 Σ on_i true? CONFIRMED WITH REPAIR

**Hypothesis as written.** "Out of a model with regular advice" is **WRONG** as stated. On a unanimous problem, a regular but non-correct advice can be improved, and that change removes steps at every world and adds none:
- S → P: off = 3, on = 0;
- M → P: off = 6, on = 0;
- M → S: off = 3, on = 0.

The sentence "unanimous changes only add" holds only if the model is correct on unanimous problems.

**Repair.** "Out of a model that is regular on mixed problems and correct on unanimous problems (for example any coherent model, in particular every selected model)". Coherent models are correct on unanimous problems because m·g has the sign of g for every probability m.

**Under the repair.** Exhaustive enumeration over all 8 sign patterns, all regular A and all B ≠ A, including the two-step changes P ↔ M and changes into C (`referee_three_world_count_out.txt`):
- *Mixed problems.* The maximum ratio of off to on is exactly 2. It is attained at S → P, M → P and M → S on the pattern (+,+,−), and at their images under g ↔ −g. Example: M → P on (+,+,−) has ranks (2,2,0) → (0,0,2), so off = 4 and on = 2.
- *Changes into contradiction.* These only add.
- *Unanimous problems with correct A.* The ratio is 0.
- *Many problems.* The count is additive over problems, so it integrates.
- A random test of 3,000 coherent models (credal hulls of 1–4 random points) against random rivals on 1–6 weighted problems found 0 failures.

**Sharpness.** The constant 2 is sharp. A sticky factor κ < 2 would break the conclusion. In n worlds the same pattern (+,…,+,−) gives a ratio n − 1, so the analogous argument needs κ ≥ n − 1.

### Does "some verdict is nonnegative at an interior index" follow? CONFIRMED

Σ_i (2on_i − off_i) = 2Σon − Σoff ≥ 0, so max_i Φ_i ≥ 0.

This holds at every index, interior or not, and indeed for every coherent model, not just selected ones. "Interior" is not needed.

### The "three-world task" sentence: incomplete

The paragraph says that the remaining task is to make that world pass its gate, with closed sections. That is not the whole of (S): it also needs *undominatedness*.

In two worlds undominatedness came free from the threshold property in the *into* direction (Theorem 4). In three worlds a selected model that is not a threshold set at world i can admit gated comparisons X ⪯_i C_p with T^off non-null. This holds for either gate.

**Repair.** "…pass its gate, with closed sections, while keeping every selected model undominated".

## 4. Finite checks

**The independent checker** (`referee_audit_ext.py`) uses exact integers: masses are integers and verdicts are scaled by 2. It checks for key ties and found none.
- Configurations:
  - layouts (mixed, unanimous) ∈ {(3,1), (4,0), (2,2), (1,3), (3,2)} × 5 seeds;
  - gates: strong and weak;
  - verdicts: coordinated and sticky;
  - 100 configurations in all, up to 1024 models;
  - plus 3 targeted layouts with cells straddling 1/3, ½ and 2/3, under both gates.
- Tests:
  - full acyclicity of each world (Kahn's algorithm on the whole accepted relation);
  - strict (G) on all pairs;
  - at every critical index (all l⁻¹(t), u⁻¹(t), midpoints between them, and a 65-point grid), against every model:
    - competitiveness;
    - no dominated selected model;
    - the section identity;
    - (V2) and (V3);
    - Lemma 3 for the gate in use;
    - for the coordinated verdict, Φ₁ + Φ₂ ≥ 0, with equality on regular-only rivals;
  - for the weak gate, that it contains the strong-gate relation.
- **Result: every failure counter is 0, in every configuration** (`referee_audit_ext_out.txt`).

**Controls** (`referee_audit_controls.py`), all caught:
- a verdict violating (V3): 828 (V3) and competitiveness failures;
- the sticky verdict with no gate: 2 cyclic worlds and 555 dominated selected models;
- a reversed weak gate: Lemma-3, section-identity and competitiveness failures.

**Shipped `weakgate.py`.** Reproduced: 0 / 0 / 0 on its 8 runs. Its limitations, which my checker covers:
- it tests only the coordinated verdict;
- it uses only the 65-point grid, not the cell breakpoints;
- it does not test strict (G) or the section identity.

**The "domination of the rest" step** is still not finitely checkable, because of atoms (see `REFEREE_gate2d.md` §3). It was not tested.

## Requested repairs, in one list

1. **Indispensable defences, non-endorsement.**
   - Use records with mass ratio r ∈ (1,2), for example 3/2, not Prop 5(b)'s ratio 2, which gives Φ₁ = Φ₂ = 0.
   - Say that the argument runs over a dense set of selected models C_p, not out of the target. Out of any one fixed selected model, the positive field "1 on U_i(C), α off it" (worlds swapped appropriately) endorses everything.
   - Say "charge vanishing on null sets and positive on non-null sets".
2. **Indispensable defences, framing.** State that indispensability is in-system: the other world's own verdict refuses, while its uniform additive evaluator does defend. Note that additive redundancy is unavoidable on regular records in two worlds.
3. **Weak gate.**
   - Replace "p" by "1 − p" at world 2 in the Lemma-3 sentence (typo).
   - Qualify "lowest keys at every world" by the §1 key convention.
   - Optionally note that the escape of Prop 6's rival says nothing yet about (S) under the weak gate in three worlds, and that Remark 7's leading-charge argument has not been re-proved for the weak gate.
4. **Three-world count.**
   - Replace "a model with regular advice" by "a model regular on mixed problems and correct on unanimous ones (e.g. coherent)".
   - Note that the constant 2 is sharp, and that the conclusion holds at every index.
   - Add undominatedness to the "three-world task".
