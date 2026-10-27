# PP18. Source fields: no selection can keep a correctness-protection set, and what survives

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full argument given here. CHECKED: exact rational computation on audit's cell model (ε = 3/10, c = 7/30, h = 7/60, d = 1/10, L = 5, the referee's PP17 instance). CONJECTURE / OPEN: as stated. No NUMERICS were needed.

**Scripts.** `r9/PP18_py/lib.py` (geometry, written independently of the audit's and the referee's code) and `s1_zones.py` → `s1_zones.out`. Run as `python3 -B s1_zones.py` inside the folder. Finite cells cannot test (S): an atom cannot carry the small fills that drive every result below. The cells only check the advice table and the record algebra.

**Inputs used.** Brief 44; `AUDIT_six_source.md` §§1–2, 9–15; `LEAD_selection_count.md`; `REFEREE_six_source.md` (PP17), including its §5 finding that T has no defence in audit's module against X* = T[A_1 ∪ A_2 → majority]; DESIGN_MEMO §8. Nothing is assumed beyond Brief 44's axioms. Where a result needs only some of them, it says which.

---

## 0. Verdict

The brief asked for a continuum version of audit's reciprocal-source mechanism that meets (S), or an obstruction for the whole class. The answer is an obstruction. It concerns the device that does the protecting, not any one choice of credal sets.

1. **What protects a source in audit's proofs.** Take a world w and a set R. A source-leaving record is safe at w if it moves the world-w rank on R from "correct" to "not correct", provided no accepted comparison ever moves it back. I call such an R a *correctness zone* at w. Audit's B_i (three-source) and R_i (six-source) are correctness zones at both worlds other than i. So are private witness sets (lead's Lemma D), sets shared by a group (the referee's repair of Lemma D), and every nested, sliding or rotating family of witness sets. The union of all of a world's zones is again a zone (§1).

2. **Theorem Z (PROVED).** In any ranking system with (IB) and strict (G) that has a selection meeting (S), with undominated selected models and direct (C), no world has a correctness zone of positive measure outside the unanimous problems. In fact the following holds at every world w and on every non-null set R of mixed problems. Some comparison C_p ⪯_w X, out of a selected model, makes advice correct at w on a non-null part of R. That comparison is a strict all-world domination of a "fill" (§3). The theorem uses neither (TC) nor T1. So no continuum reciprocal-source mechanism of this kind satisfies (S), whatever its witness geometry and however many sources share a witness.

3. **A finite form that needs no (S) (Lemma Z0, PROVED; CHECKED).** Suppose R_i stays a correctness zone at even one world j ≠ i and T stays undominated. Then *no* model dominates T with the majority answer on any non-null Q ⊆ R_i. So audit's "next boundary" (§15: release the R_i) cannot be crossed while the R_i keep protecting.

4. **T's own defences (target (b) for T; PROVED, CHECKED).** This part uses only T's competitiveness, with no KKM and no closed sections. In audit's pattern T has no defence, at any world that keeps its zones, against any of three explicit rivals:
   - Λ_T (T with the majority answer wherever it is silent);
   - the precise uniform model V_{c*};
   - Y_12 = T[R_1 ∪ R_2 → majority].

   Y_12 is the referee's X* moved from A_1 ∪ A_2 onto the protection sets. V_{c*} is coherent, so even an (S) restricted to coherent rivals breaks the pattern. An integrated version also holds: protection by a fixed charge on T's silence must be exactly balanced (Prop 4.3).

5. **What survives (§5).** There are three thresholds at which a pointwise protection set can act.
   - The correctness threshold (rank 1 → 0) is excluded by Theorem Z.
   - The contradiction threshold is useless between coherent models.
   - The **error threshold** ("no accepted comparison ever removes a world-w error on E") is *not* excluded by Theorem Z's argument.

   Error zones carry proved constraints:
   - every selected model has a "clean" world in its support;
   - comparisons at w must respect inclusion of error sets on E_w, so crossing sources cannot defend each other at a world whose error zone sees the crossing;
   - at T's clean world, every repair of a T-local rival is unprotected.

   Audit's W_ij are natural error zones (CHECKED). Whether error zones can carry a source field is a CONJECTURE.

**Single most important next step.** Decide whether *error-threshold* protection can carry a selection, at two worlds through error zones and at T's clean world through audit's composition control (a/b cancellation). The first test is the inclusion preorder of §5.2 against KKM. It is a 3-world key structure, so PP2 Thm 6 must be checked against it before any construction work.

---

## 1. Setting and the class of mechanisms

Brief 44's setting throughout:
- three worlds;
- problems are lines g ∈ R³ modulo sign, and only null sets of μ matter;
- full four-advice domain, models modulo null sets;
- ranks at world w: correct 0, silent 1, wrong 2, contradiction 3;
- T = D_M with M = c·1 + εΔ.

A coherent model is D_K for a nonempty closed convex K ⊆ Δ. It accepts g iff min_K m·g > 0, rejects g iff max_K m·g < 0, and is silent otherwise. Its accepted set C_K is an open convex cone, and C_K ∩ (−C_K) = ∅. Every coherent model is correct at every world on the unanimous problems U.

**Records.** A record is (D, a → b). Its world-w rank change at g ∈ D is r_w(b(g)) − r_w(a(g)). As the referee notes, this does not depend on the common context. "A ⪯_w B" means A is no worse than B, so its record runs from A to B.

**Definition 1.1 (threshold zone).** Fix a world w, a threshold ℓ ∈ {1, 2, 3} and a measurable set P. P is an *ℓ-zone at w* if no accepted comparison A ⪯_w B has r_w(A(g)) ≥ ℓ > r_w(B(g)) on a non-null subset of P. In words: no accepted comparison carries world-w advice back below level ℓ on P.
- A 1-zone is a *correctness zone*: no accepted comparison makes advice correct there.
- A 2-zone is an *error zone*: no accepted comparison removes an error there.

**Lemma 1.2 (what zones buy; PROVED).** Let P be an ℓ-zone at w. Suppose a record raises the world-w rank from below ℓ to at least ℓ on a non-null subset of P. Then no accepted 3-cycle at w contains a copy of it. In particular it is in no (TC) violation.

*Proof.* Around a cycle A ⪯ B ⪯ C ⪯ A the ranks at each g return to their start. Wherever the record crosses ℓ upward, one of the other two links crosses it downward. By pigeonhole one link does so on a non-null set, which is forbidden. A (TC) violation A ⪯ B ⪯ C ≺ A is such a cycle. ∎

**Every pointwise protection argument is of this form.** A pointwise protection argument says that a link worsens advice on R and no accepted link can undo that worsening. Any worsening at g crosses at least one threshold; undoing it means crossing back. So the argument is exactly Lemma 1.2 at that threshold.

Examples:
- **Audit's three-source proof (§11)** uses B_i as a 1-zone at w ≠ i.
- **Audit's six-source proof (§14)** uses R_i as a 1-zone at w ≠ i. The source-leaving records turn majority, which is correct at w, into silence. CHECKED: 0 of 21,040 installed records per world cross threshold 1 downward on R_i, i ≠ w (`s1` (a)).
- **The essential union of zones is a zone.** The essential union of any family of ℓ-zones at w (private, shared by groups, nested, sliding, rotating, of any cardinality) is again an ℓ-zone. It equals a countable sub-union, and the invariant is an a.e. statement.

**The class.** A *threshold-protected source mechanism* (at level ℓ) is any ranking system in which at least one strict source comparison or repair is protected at some world by an ℓ-zone, in the sense of Lemma 1.2. Audit's constructions, and every continuum version that shares witnesses in the way the brief suggests, are level-1 mechanisms.

---

## 2. Two lemmas

**Lemma Z0 (fill lemma; PROVED).** Uses only (IB) and reflexivity.
- Let N be undominated and P a 1-zone at w.
- Let Q ⊆ P be non-null, with N not correct at w a.e. on Q.
- Let X := N[Q → w-correct], meaning N with the world-w correct answer on Q.

If Z ⪯_v X at every world v, and X ⪯_v Z fails at some world, then N is dominated. So no model dominates X.

*Proof.*
1. Z ⪯_w X, and X has rank 0 on Q. Since P is a 1-zone, Z must have rank 0 a.e. on Q. The correct answer at w is unique a.e., so Z = X on Q.
2. Put D := {Z ≠ X}. Then D ∩ Q is null, and X = N off Q, so X = N on D.
3. The pair (Y, N), with Y := Z on D and N off D, has the same record as (Z, X).
4. By (IB): Y ⪯_v N at every v, and N ⪯_v Y fails where X ⪯_v Z fails.
5. Y ≠ N, since D is non-null (Z ≠ X by reflexivity and strictness). So Y dominates N. ∎

This is audit's §2 exposure necessity, forced by the zone.

**Corollary 2.1 (audit's boundary; PROVED, CHECKED).** In any extension of audit's six-source relation where T is undominated and R_i stays a 1-zone at even one world j ≠ i, no model dominates T[Q → majority] for non-null Q ⊆ R_i.

Audit §15 names R_1 ∪ R_2 ∪ R_3 as the next boundary. Corollary 2.1 says this boundary cannot be crossed by adding repairs while the R_i keep protecting.

CHECKED (`s1` (b)), for X = T[R_i → majority] and each of the seven sources:
- T and the four sources outside group i would have to make R_i correct at both worlds j ≠ i;
- C_i and F_i keep the zone, but their record copies onto (Y, T) with Y ≠ T.

**Lemma R (rigidity of coherent models; PROVED).** Let N = D_K be coherent and Q′ a non-null set on which N is not correct at w. Then there is a non-null Q ⊆ Q′ such that N[Q → w-correct] is not a.e. equal to any coherent model.

*Proof.*
1. **Choosing Q.** The boundaries of C_K and −C_K are null. So a.e. point of Q′ lies in one of two open sets: the open silence set Sil := complement of the closures of ±C_K, or the open answer set ±C_K. Take a density point g₀ of Q′ in one of these, with g₀,w ≠ 0. Orient g₀ so that the correct answer at w is "accept g₀". Let U be a small open cap around g₀, with the cap of twice the radius inside the same open set and g_w > 0 throughout. Put Q := Q′ ∩ U, which is non-null. Put X := N[Q → accept].
2. **Suppose X = D_{K′} a.e.** C_{K′} is open and convex and contains a.e. point of the open set C_K ∖ ±Ū. An open convex set containing a.e. point of an open set contains all of it, because each point is a convex combination of nearby points of the dense subset. So C_{K′} ⊇ C_K ∖ ±Ū. Also C_{K′} contains some q ∈ Q.
3. **Case U ⊆ Sil (N silent on U).** C_K ≠ ∅, since it contains the positive orthant. For c in a small ball B ⊆ C_K, the cone over the segments from c to q lies in C_{K′}. Each such segment runs from outside the double cap into U. So it crosses the annulus between radius r and 2r, which lies in Sil ∖ ±Ū. These crossing points form an open, hence non-null, set where D_{K′} accepts but X = N is silent. Contradiction.
4. **Case U ⊆ −C_K (N gives the wrong answer on U, i.e. accepts −g there).** Then C_K is an open convex cone containing the double cap around −g₀. Each point of −U is a midpoint of two points of C_K outside ±Ū, and these lie in C_{K′} by step 2. So −U ⊆ C_{K′}. Then q and −q both lie in C_{K′}, which is impossible for a coherent cone.

(Coherent models are never contradictory, and "not correct at w" means silent or wrong, so these two cases are exhaustive.) ∎

---

## 3. Theorem Z

**Theorem Z (PROVED).** Assume:
- (IB) and strict (G);
- a selection p ↦ C_p on Δ such that every C_p is coherent and undominated, competitive on supp p, with every section A_v(X) = {p : C_p ⪯_v X} closed;
- direct (C), in the form that no incoherent model is all-world tied with a selected model.

Then for every world w and every non-null set R of mixed problems there is a comparison C_p ⪯_w X, accepted, with C_p selected and X incoherent, such that:
- X has rank 0 at w on a non-null subset of R on which C_p has rank ≥ 1;
- C_p ⪯_v X at every world v, strictly at some.

Consequently every correctness zone at every world is contained in U, up to a null set.

*Proof.*
1. **Lemma B (lead's; refereed correct).** C_{e_j} = V_j, the precise vertex model. It is selected and undominated.
2. **Choosing a vertex.** For j ≠ w, V_j is not correct at w exactly on M_j ∪ M_w: it gives the minority-j answer on M_j and the majority answer on M_w. With k the third world, (M_j ∪ M_w) ∪ (M_k ∪ M_w) covers every mixed problem. So R meets {V_j not w-correct} in a non-null set Q′ for j or for k. Call that vertex N.
3. **The fill.** Lemma R gives a non-null Q ⊆ Q′ with X := N[Q → w-correct] incoherent, hence not selected.
4. **A dominator.** Competitiveness gives p ∈ ∪_{v ∈ supp p} A_v(X) for every p. With closed sections, the KKM lemma gives p with C_p ⪯_v X at every v. Since X is incoherent, direct (C) excludes an all-world tie, so the domination is strict at some v.
5. **The improvement.** If C_p had rank 0 a.e. on Q, then step 1 of Lemma Z0's proof would apply with P = Q, and N would be dominated. So C_p has rank ≥ 1 on a non-null part of Q, where X has rank 0.
6. **Zones lie in U.** Applied to R := P ∖ U for a 1-zone P, this gives a forbidden comparison unless P ∖ U is null. ∎

**Corollaries (PROVED).**

- **Z1: no continuum reciprocal-source mechanism of audit's kind satisfies (S).** By Lemma 1.2, the protection in such a mechanism is a 1-zone of positive measure inside the mixed problems. This holds for every witness geometry: private (Lemma D), shared by groups (PP17 repair), nested or sliding windows, rotating or crossing segments and their thickenings. It also holds for every number of sources. *Theorem Z bounds what protection can exist at all, not how many sources a fixed amount of protection can serve.* That is the sense in which it strengthens Lemma D.

- **Z2: restricting the invariant does not help.** The forbidden comparisons in Theorem Z have a *selected* better side and a *non-selected* worse side, and they are strict all-world dominations. So the invariant fails even if it is required only for comparisons out of selected models, or only for repairs.

- **Z3: it is not about T1.** The proof never uses T. With N = T (any selected interior T) and R ⊆ Sil(T), it shows that fills of T's silence on any part of any candidate zone are dominated at every world by selected models whose record makes advice correct there.

**Scope (stated exactly).**
- Theorem Z excludes the *invariant*, not (TC). A system may still satisfy (TC) if the source-leaving records and the forced correctness-making comparisons never compose into a triangle. That is *composition control*, which audit already uses at the label world: a/b cancellation on R_w.
- Composition between two copies needs matching advice on the overlap of their supports (PP17 §1). Records out of different coherent models usually have large, mismatched supports. So composition control is not excluded here.
- But it must now do *all* the work, at every world and on every set. No protection set can be held in reserve.

---

## 4. T's own defences (target (b) for T and every selected model)

The coordinator's PP17 finding is that T has no defence in audit's module against X* = T[A_1 ∪ A_2 → majority]. The results below show why that gap cannot be closed on the protection sets themselves. They need only competitiveness of the model concerned: no KKM, no closed sections, no rigidity.

**Proposition 4.1 (clean world for correctness zones; PROVED).** Let P_v be a 1-zone at each world v, and let N be competitive on a support I. Then N is correct a.e. on P_v for some v ∈ I.

*Proof.*
1. Otherwise, for each v ∈ I choose a non-null Q_v ⊆ P_v on which N is not v-correct. Make the Q_v pairwise disjoint, which is possible by atomless splitting.
2. Let X := N with the v-correct answer on Q_v, for every v ∈ I.
3. At each v ∈ I the record N → X makes advice v-correct on Q_v ⊆ P_v. So N ⪯_v X is refused at every v ∈ I, and N is not competitive. ∎

**Proposition 4.2 (three explicit rivals; PROVED; CHECKED in `s1` (c)).** In audit's six-source pattern, where R_i is a 1-zone at both worlds other than i, T has no defence at any world against each of the following rivals:
- (i) **Λ_T**, which is T with the majority answer wherever T is silent;
- (ii) the precise uniform model **V_{c*}**;
- (iii) **Y_12 := T[R_1 ∪ R_2 → majority]**.

*Why.* For (i) and (ii), on R_i (where c*·g = d > 0) the rival gives the majority answer, which is correct at both worlds other than i. Hence the record T → rival makes R_i correct at every w ≠ i, and every world contains such an i. For (iii), world 3 is refused by strict (G); world 1 makes R_2 correct, and world 2 makes R_1 correct.

Three remarks:
- (ii) is coherent, so the pattern fails even for an (S) that only asks for competitiveness against coherent rivals.
- (iii) is the referee's X* moved from the A cells onto the R cells. The referee's one-world target-reference fix passes the cells *because* its records are 0 on every R_i (PP17 §5). Proposition 4.2 (iii) says it cannot be extended to rivals that vary on R_i while the R_i protect.
- By Proposition 4.1 the same holds for every selected source in place of T. In a source field each selected model needs a clean world.

**Proposition 4.3 (integrated protection; PROVED).** Suppose that at each world w every accepted comparison is ν_w-nonimproving: ∫ (r_w(B) − r_w(A)) dν_w ≥ 0 whenever A ⪯_w B. Here the ν_w are finite measures absolutely continuous with respect to μ, with densities ρ_w.

- **(a)** If ν_w(M_w ∩ Sil(T)) = 0 and ν_w((M_i ∪ M_k) ∩ Sil(T)) > 0 for every w, then T is not competitive against Λ_T. This is the integrated form of audit's pattern.
- **(b)** In general, if T is competitive, there is λ ≥ 0, λ ≠ 0, with λ_i ρ_i = λ_j ρ_j + λ_k ρ_k a.e. on Sil(T) ∩ M_i, for each i. So protection by charges must be exactly balanced on T's silence.

*Proof.*
- **(a)** At w, Λ_T changes ν_w-weighted rank by −ν_w((M_i ∪ M_k) ∩ Sil(T)) < 0.
- **(b)**
  1. The set of vectors (∫ (r_w(X) − r_w(T)) dν_w)_w, over all models X, is convex. This follows from Lyapunov's theorem, applied to splice two rivals along a set carrying an α-fraction of every relevant integral.
  2. Competitiveness says this set misses the open negative orthant.
  3. A separating λ ≥ 0, λ ≠ 0, makes T minimise Σ_w λ_w ∫ r_w dν_w, and hence pointwise a.e.
  4. On Sil(T) ∩ M_i, silence costs a + b, the majority answer costs 2a and the minority answer costs 2b, where a = λ_i ρ_i and b = λ_j ρ_j + λ_k ρ_k. So a = b. ∎

---

## 5. What survives: error-threshold protection

- **Threshold 3.** Coherent models never contradict themselves. So no comparison between coherent models crosses threshold 3, and a 3-zone protects nothing a source field needs.
- **Threshold 2.** Let E_w be a 2-zone, an *error zone*, at w. Theorem Z's argument does not reach it. The dominator Z of a fill X = N[Q → w-correct] only has to avoid *wrong* answers on Q. It may be silent there, which keeps exposure, so Lemma Z0 does not fire.

  The same holds for the fill to silence: the dominator may be correct on part of Q. Vertex fills give no constraint either: V_j is clean at its own world j.

  So the argument of §3 says nothing about threshold 2. That is all that is claimed: error zones are not shown to be consistent with (S) (OPEN).

**Proven constraints on error zones (PROVED).**

- **5.1 Clean world.** Every model N competitive on support I has a world v ∈ I with no v-errors a.e. on E_v. The proof is that of Prop 4.1, with "fix errors" in place of "make correct".
- **5.2 Inclusion.** If A ⪯_w B is accepted, then err_w(A) ∩ E_w ⊆ err_w(B) up to a null set. Two consequences:
  - Two selected models whose error sets *cross* on E_w can be compared at w in neither direction. Crossing sources, such as rotating segments, must defend each other at worlds whose error zones do not see the crossing.
  - On each E_w, accepted comparisons respect a fixed inclusion preorder. This is a key-like structure, but on level-2 steps restricted to E_w, which PP2 Thm 6 (level-1 steps, a fixed key) does not literally cover. Whether a KKM argument in the style of PP2 excludes it is OPEN.
- **5.3 T's clean world is unprotected.** Let w_T be a clean world of T, as in 5.1. Any rival that agrees with T on E_{w_T} has no w_T-errors there. So no repair or source record into such a rival creates an error on E_{w_T}. At w_T, all T-local repairs must be made consistent by composition control alone. This is audit's a/b cancellation, but for *all* groups at once, not only group w_T.
- **5.4 Audit's W_ij are natural error zones (CHECKED, `s1` (d), (e)).** On W_ij, T gives the minority-k answer, which is wrong at i and j, while groups i and j are silent. So a source record S → T, with S in group i or j, creates an error there at worlds i and j.

  By 5.1 they cannot serve for T's errors at all three worlds. The rival T[all W → majority] removes T's errors at every world (`s1` (e)).

  The guard construction (DESIGN_MEMO §8.12) also protected through sets where T errs. Theorems B and O killed that architecture, not this threshold, but any design along these lines must show it escapes them.

**CONJECTURE (nearby target).** There is a source field whose source comparisons are protected at two worlds by error zones (5.2 ordered) and at T's clean world by composition control. Its selected models would have clean worlds that vary continuously with the index.

---

## 6. Status of the brief's targets for continuum reciprocal-source (level-1) mechanisms

| Target | Status |
|---|---|
| (a) coherent, undominated sources | Achievable in modules (audit). Not obstructed by itself. |
| (b) competitiveness against selected models | Compatible with zones only if each selected model is correct on some world's zone (Prop 4.1). |
| (b) against (IB)-created models and audit's six-set class | Cells: one-world t-records pass (PP17). Measurable proof OPEN. Possible only while the rivals avoid the zones. |
| (b) against fills inside a zone, Λ_T, V_{c*}, Y_12 | **Impossible** while the zone protects (Lemma Z0, Prop 4.2). |
| (c) closed sections | Not the issue. Theorem Z uses closedness only through KKM, and holds for every closed-section selection. |
| (d) audit's repairs with continuously varying sources | Possible on rivals avoiding the zones. Cannot reach rivals inside them (Cor 2.1). |
| full (S) | **Impossible** for every level-1 mechanism (Theorem Z). |

---

## 7. Next step

Test error-threshold protection, because it is the only pointwise protection level left.

1. Fix error zones E_1, E_2, E_3, for example thickenings of the W_ij that respect 5.1 (one world left clean for T).
2. Ask whether the inclusion preorder of 5.2 admits a closed-section selection meeting KKM. This is the analogue of PP2 Thm 6 for level-2 keys, and it should be settled first.
3. If it passes, combine it with audit's a/b cancellation at T's clean world (5.3), and with the referee's one-world target-reference records.

If it fails, the conclusion would be that protection must be fully compositional (no invariant of any pointwise kind), and the programme should study composition control directly.
