# PP25. Adversary on local defences: the local layer cannot carry an obstruction, and what is left is a dominator-only problem

22 October 2026. One author (the adversary); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exhaustive exact integer computation on finite cells (diagnostic only). NUMERICS: Monte Carlo. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP25_py/`; run `python3 -B <script>` inside the folder):
- `common.py`: shared cell code.
- `local_rule.py` → `local_rule.out`: Theorem A on cells.
- `decouple.py` → `decouple.out`: Theorem B, Prop D and the control for Lemma 5, with inner and outer radial pieces.
- `psi_scores.py` → `psi_scores.out`: angular scores of coherent models, for §6.

Finite cells are diagnostics only. Nothing in them is evidence about (S).

---

## 0. Verdict

I tried to prove that (a) and (b) are incompatible. I could not, and I can say exactly why.

1. **(a) costs nothing, for every coherent model at once (Theorem A, PROVED).** There is a record-based rule on bounded records with the following properties:
   - it satisfies strict (G), (IB) and (TC);
   - every model that is correct on U and never contradictory, and in particular every coherent model, is *strictly* competitive against every bounded rival;
   - no such model is dominated by a bounded rival;
   - there are no ties, even at a single world.

   The rule is a lexicographic additive score whose first level makes all advice on mixed problems exactly indifferent at the uniform weight. Audit's Prop 1 rival, the brief's departure/retreat pump and the forced retreats of point 4.1 are all absorbed, because the rule is a potential at each world.

2. **Local defences and dominations do not interact, provided each dominator carries compensation at every world (Theorem B, PROVED).** Compensation here means that C beats N somewhere at every world, on the cone where they differ. Every triangle with exactly one bounded edge is then not accepted. A (TC) failure has to consist of three unbounded links, two of them domination records. This is a precise form of the brief's last lever (Lemma H): the dominator's record crosses N's local defences, but its conic far part cannot be cancelled by a bounded link.

3. **Reduction (Theorem C, PROVED).** Use the rule of Theorem A on bounded records and accept on unbounded records only guidance plus the chosen domination records. Suppose the domination records satisfy:
   - compensation at every world;
   - no inverse far parts;
   - an exposure/landing condition.

   Then (a) holds for every coherent model, every domination is strict at all three worlds, members and dominators are undominated, direct (C) holds trivially (no all-world ties), and (TC) holds **iff** a condition (GG) holds that involves only pairs of domination records. A sufficient condition for (GG) is an angular additive certificate (Prop D).

4. **Consequence for the adversarial task.** At the stated scope, an obstruction to the extension principle cannot use local defences at all. It must be one of two things:
   - an obstruction to (b) inside the dominator layer alone, which is a coverage question involving no bounded records; or
   - a proof that every dominator system for (b) must use dominators that lack compensation at some world. Only that case brings local refusals in (Lemma 5).

   Neither is proved. Lemma 5 explains PP21's corner tightenings: by Lemma Q they lack compensation at world k, so they are exactly the dominators that *do* create local refusals.

5. **The freedom that escapes, stated exactly.**
   - **(F1) A single common interior witness weight.** (a) concerns an interior family only, with no face-supported competitiveness and no continuity in the index. So all members can share the witness λ = (1/3, 1/3, 1/3), and PP18 Prop 4.3(b)'s balance condition can be met once and for all by the weights.
   - **(F2) Conic compensation.** The compensation of a dominator lives on a cone, and bounded rivals cannot reach it.

   (F1) is a scope freedom. Once a continuous-in-measure selection must also cover the faces, FF2 Thm 4.1 / Cor 4.3 excludes the rule of Theorem A, because its first level is an integrable, strictly guiding endorser. So the local layer must become non-additive exactly when (S) is added. That is beyond (a)+(b), which is the real location of the difficulty.

6. **Simplest rule exploiting this:** "indifference-lexicographic on bounded records; guidance plus compensated, certified dominations on unbounded records". §6 states the remaining existence question for the dominations.
   - NUMERICS: with a uniform angular certificate, tightenings toward the centre of a member's credal set are certified.
   - Corner tilts and loosenings are not certified, and these would be needed as dominators of rivals near the edges of the member's silence band or inside its answered region. OPEN.

---

## 1. Scope and conventions

**Setting.** Brief 46's setting throughout:
- three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain;
- advice codes accept, reject, silent, contradiction; ranks 0 < 1 < 2 < 3;
- mixed regions M_k, where world k is the minority sign; U is the unanimous set.

Write X ≤_w Y for "pointwise no worse at w", and X ⪯_w Y for the ranking. rec(A, B) = (D, a → b) with D = {A ≠ B}. δ_w(g) := r_w(b(g)) − r_w(a(g)).

**Axioms used.** Reflexivity, strict (G), (IB), (TC) ("A ⪯ B ⪯ C implies not C ≺ A"; equivalently, every accepted triangle has all three reverses). Direct (C) is reported, never assumed. No transitivity is assumed. Single-world ties and triangle completion are allowed, and defenders may depend on the rival.

**Bounded, far part.**
- A record is *bounded* if D lies, modulo null sets, in a bounded set.
- For an unbounded record r, its *far part* is r restricted to D ∖ B for a bounded B. Statements "the far part is (not) a weak w-improvement" mean: for every bounded B.
- Triangle lemma (brief, point 2): in any triangle the number of unbounded edges is 0, 2 or 3. If exactly one edge (A, B) is bounded, then A = B off a bounded set, so the far parts of the other two links are mutual inverses.

**The family and the requirements.**
- F is any set of coherent models. Theorem A even allows F = all coherent models. The brief's examples (every D_K with K a small triangle near T's credal set, or a one-parameter chain such as K_r = u + r(Δ − u), r ∈ [r_0, r_1]) are special cases.
- (a): for every N ∈ F and every Y with rec(N, Y) bounded, N ⪯_w Y at some w.
- (b): for every N ∈ F and every incoherent Y = N[E → y] with E bounded, there is a coherent undominated C with C ⪯_v Y at all v and Y ⋠_v C at some v.
- (H_U) (used only in Lemma 2): members are undominated.

---

## 2. What the levers give (PROVED)

**Lemma 1 (dominators of improving rivals are other models).** If Y is a weak w-improvement of N with strictness somewhere, then N ⋠_w Y. So C = N cannot serve in (b).

By Lemma H, any other coherent C has {C ≠ N} a.e. conic and non-null, hence not bounded. So rec(C, Y) is unbounded, with far part rec(C, N) restricted to a cone.

**Lemma 2 (exposure; PP18 Z0 localised).** Under (H_U), a dominator C of Y = N[E → y] differs from y on a non-null part of E.

*Proof.* If C = y a.e. on E, then Y = N on D := {C ≠ Y}. So (N[D → C], N) is a copy of rec(C, Y), and N[D → C] would dominate N. ∎

**Lemma 3 (pump, exact form).** Suppose that at world w a record d and a record ρ are accepted, that their copies compose (the new advice of d equals the old advice of ρ on the overlap), and that the composite is a weak w-improvement with strictness somewhere. Then (TC) fails. Brief point 4's departure–retreat pair is the case where d is silent → answer on G ∪ H and ρ is answer → silent on G ∪ H ∪ F.

*Proof.* A ⪯ A∘d ⪯ (A∘d)∘ρ ≺ A, the last link by strict (G). ∎

**Lemma 4 (Prop 1 rival needs a non-guidance local defence).** This is audit's Cor 4, restated so that it applies to every N ∈ F: the rival correcting N at i on E_i, for i = 1, 2, 3, is refused by guidance at every world.

**Lemma 5 (the only local consequence of a dominator; localised PP19 Lemma 5.0).** Let C dominate Y = N[E → y], and let C have **no compensation at v**: N ≤_v C a.e. on {C ≠ N}. Put W := N[E → C] (C on E, N elsewhere), a bounded rival of N. Then:
- W ≺_v C by strict (G);
- the bounded record rec(Y, W) = (E ∩ {y ≠ c}: y → c) is refused at v, together with all its (IB) copies;
- Y ≺_v W is also excluded.

*Proof.* W = C on E. Off E, W = N ≤_v C, strictly on the non-null cone {C ≠ N} ∖ E. So W ≺_v C. Hence C ⪯_v Y ⪯_v W ≺_v C would violate (TC). Also W ⪯_v C ⪯_v Y forbids Y ≺_v W. ∎

Two remarks on Lemma 5:
- A coherent C ≠ N cannot lack compensation at all three worlds, because N would then dominate C by guidance. So Lemma 5 refuses a local record at one or two worlds.
- PP21 Lemma Q's k-corner tightenings lack compensation at world k. They are exactly the dominators that create these refusals.

**Classification.** Lemma 5 is a failure from a *chosen geometry* (uncompensated dominators). It does not follow from the axioms plus (a) and (b).

---

## 3. Theorem A: the local layer is free

**Weights.**
- On a mixed problem g ∈ M_i, put ρ_i(g) = 2 and ρ_j(g) = ρ_k(g) = 1. On U put ρ_w = 1. These are bounded and positive.
- The point is uniform-λ indifference on mixed problems. At g ∈ M_i:
  - silent → majority changes ranks by (+1, −1, −1);
  - silent → minority by (−1, +1, +1);
  - majority → minority by (−2, +2, +2).

  So Σ_w ρ_w δ_w = 0 for every change among {accept, reject, silent} on a mixed problem.
- Changes away from the correct answer on U, and changes to contradiction, have Σ_w ρ_w δ_w > 0.

**Rule L.** Fix a countable family {B_n} of bounded Borel sets generating the Borel σ-algebra (for example, rational boxes). For a bounded record r and world w, define

  Φ_w(r) := ( ∫ ρ_w δ_w dμ ,  ∫_{B_1} ρ_w δ_w dμ ,  ∫_{B_2} ρ_w δ_w dμ , … ),

and accept r at w iff Φ_w(r) ≥ 0 in the lexicographic order.

**Theorem A (PROVED).** On bounded records, L satisfies the following.
1. (IB), and strict (G).
2. (TC): no violation among bounded links.
3. If Φ_w(r) = 0 for some w, then r is trivial. Hence there are no single-world ties between distinct models across a bounded record.
4. Every model N that is correct on U and never contradictory satisfies N ≺_w Y at some w, for every bounded rival Y ≠ N. In particular every coherent model is strictly competitive against every bounded rival.
5. No such N is dominated across a bounded record.

*Proof.*
1. Φ depends only on the record. For strict (G): a weak worsening has every component ≥ 0, so it is accepted. A non-trivial weak improvement has first component < 0, because ρ > 0. So it is refused.
2. At each world, Φ_w is additive under composition of copies, with values in the ordered group R^ℕ (lexicographic order). Around an accepted triangle, Φ_w sums to 0, and each term is ≥ 0, so each term is 0. Then each reverse also has Φ_w ≥ 0.
3. Φ_w(r) = 0 gives ∫_{B_n} ρ_w δ_w = 0 for all n. So δ_w = 0 a.e. Since the rank at a single world is injective on the four advice values, r is trivial.
4. Let r = rec(N, Y) ≠ trivial. Let n* be the first level at which the vector (Φ_w^{(n*)})_w is non-zero; it exists by item 3. Pointwise, Σ_w ρ_w δ_w ≥ 0 for records out of N: it is 0 on mixed changes among coherent-type advice, and > 0 when U-correctness is lost or a contradiction is added. So Σ_w Φ_w^{(n*)} ≥ 0. As the vector is non-zero, some component is > 0. At that w, r is accepted and its inverse is refused.
5. For a record B → N, the same pointwise sum is ≤ 0. Acceptance at all three worlds with strictness somewhere would make the sum > 0 at level n*. ∎

**CHECKED** (`local_rule.out`). The cells use three mixed directions (one per M_k), a second radial piece, and a U cell, giving all 4⁵ models. The second run, `pump4`, uses a configuration containing brief point 4's pump. Results in both:
- 0 (TC) violations at every world;
- 0 single-world ties;
- strict (G) holds;
- all 81 (respectively 27) models that are U-correct and non-contradictory are strictly competitive against every model and dominated by none.

**What it does to the levers.**
- *Prop 1 rival.* It is defended at the world where Φ first turns positive.
- *Pump.* L is a potential, so Lemma 3's composite can never be accepted together with both of its links.
- *Brief point 4.1.* The retreat rival Z (silence on majority pieces of M_1, M_2, M_3) is answered at a world where its Φ is positive. The departure Z → N is accepted exactly where the retreat is refused, and no asymmetry needs designing.
- *Departure rule of brief point 3.* It is superseded. L accepts some departures and some retreats at each world, and the split is set by one potential.

**What it is not.**
- It is not a CPM realisation and not a proper ℓ^m. No prior selects a model: at the uniform weight, every U-correct non-contradictory model is optimal on bounded changes. It is maximally improper on mixed problems.
- It does not decide any unbounded record (§4).
- **Caveat (PROVED by citation).** Its first level is an integrable, strictly guiding additive endorser of every accepted bounded comparison. That is FF2's (H3). So L cannot be the local layer of any selection that is continuous in measure, competitive on supp q at every q ∈ Δ and passes through T1 (FF2 Thm 4.1, Cor 4.3).

  The step L escapes is FF2 Step 3, which needs competitiveness of face-indexed models with restricted support. Requirement (a) concerns interior members, so a single interior witness serves all of them. This is freedom (F1). It disappears at the scope of (S), not at the scope of (a)+(b).

---

## 4. Theorem B: decoupling

**Hypotheses.** At world v, the accepted records are:
- the bounded records in L_v, which contains guidance on bounded records and satisfies (TC) among bounded links (Theorem A's rule, or any other such rule);
- the unbounded records in Guid_v ∪ G_v,

where:
- **(B1) compensation:** no r ∈ G_v has a far part that is a weak v-improvement;
- **(B2) no far inverses:** there are no r, s ∈ G_v whose far parts are mutually inverse.

**Theorem B (PROVED).** Every accepted triangle at v that misses a reverse consists of three unbounded links, at least two of them in G_v.

*Proof.* Use the triangle lemma.
- *0 unbounded edges:* (TC) holds by hypothesis on L_v.
- *2 unbounded edges* ℓ_2, ℓ_3 (exactly one bounded edge): their far parts are mutually inverse.
  - Both in Guid: each far part and its inverse are weak worsenings, so the far part is trivial. That contradicts unboundedness.
  - One in G_v, the other in Guid: the G far part would be the inverse of a weak worsening, hence a weak improvement. That contradicts (B1).
  - Both in G_v: excluded by (B2).

  So no triangle with exactly one bounded edge is accepted at all.
- *3 unbounded edges* with at most one G link: if there are none, guidance alone satisfies (TC). If there is one, the other two links are weak worsenings whose sum is minus the G link, so the G link is a weak improvement on its whole support. That contradicts (B1). ∎

**Proposition D (angular certificate; PROVED).** Fix a world v and a positive density τ_v on the sphere. For a record whose rank change is conic off a bounded set, put

  Ψ_v(r) := ∫_{S²} δ_v^∞(θ) τ_v(θ) dθ,

where δ_v^∞ is the angular profile of the far part. Suppose every r ∈ G_v has Ψ_v(r) > 0. Then (B1) and (B2) hold, and no accepted triangle at v contains a G_v link.

*Proof.*
- Ψ_v > 0 rules out a weak improvement (where Ψ_v ≤ 0), and it rules out mutually inverse far parts (whose Ψ values have opposite signs).
- In a triangle whose links are all unbounded, if two links have conic far parts then so does the third (minus their sum), and Ψ_v sums to 0.
- Guidance links have Ψ_v ≥ 0, and G links have Ψ_v > 0. So no accepted triangle contains a G link. ∎

**CHECKED** (`decouple.out`). The cells are three mixed directions × {inner, outer} pieces, giving 4096 models. L acts on inner-only records. G consists of random records rec(C, Y), with C and N constant across the two pieces and Y = N changed on inner pieces.

| G drawn with | runs | (TC)-violating pairs | triangle types found |
|---|---|---|---|
| compensation at all worlds, no far inverses | 4 | 3, 0, 3, 24 | only **GGg** (two G links and one guidance link) |
| Ψ > 0 at all worlds (τ uniform) | 4 | 0, 0, 0, 0 | none |
| no compensation at world 1 (control), strict (G) kept | 3 | 1924, 942, 1911 | only **GLg** (Lemma 5) |

Exactly as Theorem B predicts, a triangle with one bounded edge appears only when compensation is missing.

The printed GGg witness at world 3 has outer pieces A: (A, A, S), B: (S, S, A), Z: (R, S, R). The new side of one G link equals the old side of the other on a shared outer cell. That is a *shadow* (Lemma 6 below).

---

## 5. Theorem C: reduction of (a)+(b) to a dominator-only problem

For each local rival Y = N[E → y] in (b), choose a coherent C(Y) and put rec(C(Y), Y) into G_v at all three worlds. Let 𝒟 be the set of chosen dominators, and write S := {C ≠ N} and X := E ∩ {C ≠ y}. Assume:
- **(C1)** compensation: C beats N on a non-null set at each world;
- **(C2)** no far inverses in G;
- **(C3)** exposure and no landing: X is non-null, and there is no model C° ∈ F ∪ 𝒟 with C° = N on S ∖ E and C° = y on X.

Two sufficient conditions for (C3):
- X ∩ S is non-null; or
- y is pointwise impossible for coherent models on X ∖ S (wrong or silent on U, or contradictory).

If Y is a pointwise worsening of N at every world (for example, it only damages U or adds contradictions), take C = N. Then (b) holds by guidance and no G record is needed.

**Theorem C (PROVED).** With L on bounded records and Guid ∪ G on unbounded records:
1. (IB) and strict (G) hold.
2. (a) holds for every coherent model.
3. Each chosen domination is strict at **all three** worlds.
4. Every model in F ∪ 𝒟 is undominated.
5. There are no ties at any world between distinct models, so direct (C) holds.
6. (TC) holds iff (GG): no accepted triangle consists of three unbounded links with at least two in G.

*Proof.*
- **Strict (G).** Bounded records are covered by Theorem A. G links are not weak improvements, by (C1). Unbounded pure improvements are in neither Guid nor G.
- **(a).** This is Theorem A.
- **Strictness.** inv rec(C, Y) is unbounded. It is not guidance, by (C1), and not in G, by (C2).
- **Undominated.** Let B dominate C° ∈ F ∪ 𝒟, and consider the single record rec(B, C°).
  - If it is bounded, Theorem A(5) applies.
  - If it is unbounded and accepted by guidance at all three worlds, it would be a Pareto worsening at every problem. That is impossible, because every change between coherent-type advice worsens some world.
  - If at some world it is a copy of some rec(C, Y), then C° equals Y's advice on {C ≠ Y} = (S ∖ E) ∪ X. That is excluded by (C3). (When X ∩ S is non-null: C° = N on S ∖ E with S conic forces C° = N on S, which contradicts C° = y ≠ n on X ∩ S.)
- **Ties.** Bounded ties are excluded by Theorem A(3). Unbounded ties would need a record and its inverse both in Guid ∪ G, which (C1) and (C2) exclude.
- **(TC).** This is Theorem B. ∎

**Lemma 6 (shape of GG failures; PROVED).** Every GG triangle contains two G links r = rec(C_1, Y_1) and s = rec(C_2, Y_2) (as copies) whose far supports S_1, S_2 overlap in a non-null set on which the new far advice of one equals the old far advice of the other. In other words, N_1 = C_2 a.e. on S_1 ∩ S_2: a **shadow**. The composite then cancels on the shadow, and (TC) fails exactly when the cancelled part held all of one pair's compensation at the triangle's world.

*Proof.* Rank changes sum to 0 around a triangle, so a.e. far point lies in at least two far supports. Adjacent copies compose only where their advice matches. If the two G far supports met only in a null set, then:
- a third link in Guid would make each far part a weak improvement, which contradicts (C1);
- a third link in G would need its old far advice to equal N_1 on S_1, which is a shadow between it and r. ∎

So the residual is the global layer's own version of PP19 Prop S and PP21's cross-exposure. It is stated purely in terms of cones and pairs (C, N). No bounded record and no local defence enters it.

---

## 6. The residual question, and how far the simplest certificate reaches

By Theorem C and Prop D, (a)+(b) holds for a family F if the following is satisfied:

**(Π)** There are densities τ_1, τ_2, τ_3 > 0 such that, for each N ∈ F and each bounded incoherent rival Y = N[E → y] that is not a pointwise worsening, there is a coherent C with:
- s_τ(C) < s_τ(N) componentwise, where s_{τ,v}(X) = ∫ r_v(X(θ)) τ_v(θ) dθ is the angular score (equivalently Ψ_v(rec(C, N)) > 0 for all v);
- (C3) for C and Y.

(Π) is purely a question about angular scores of coherent models.

Note: s_τ(C) < s_τ(N) is **not** a domination of N in our relation, because rec(C, N) is never accepted. It is only a certificate that the records rec(C, Y) do not close triangles. So (Π) does not conflict with N being undominated.

**What uniform τ certifies** (NUMERICS, `psi_scores.out`, N = D_K with K = u + 0.15(Δ − u), 4·10⁵ directions):

| C | Ψ(C → N) | certified |
|---|---|---|
| precise centre u | (+0.016, +0.015, +0.016) | yes |
| half-size triangle | (+0.010, +0.009, +0.010) | yes |
| a vertex of K | (+0.149, −0.058, −0.057) | no |
| e_1-tilts | negative at worlds 2 and 3 | no |
| loosening u + 0.25(Δ − u) | negative at all worlds | no |

On Sil(N) the centre gives the majority answer on 63.5% of directions.

So uniform τ certifies dominators for rivals on N's silence whose hyperplanes pass near the centre of K, in both orientations, using slightly displaced tightenings. It does **not** certify:
- the opposite-orientation dominator for silence points near the edge of N's silence band (this needs a corner tilt);
- dominators for flips and retreats inside N's answered region (these need loosenings, or far credal sets).

For these, the alternative (C3) route, exposure with X ∩ S null, can sometimes be used. One case is PROVED: if S ⊇ Sil(N) and y = reject on part of N's accept region, then no coherent C° can land, because silence on all of Sil(N) forces K° ⊇ K (separation argument). Retreats y = silent can land on loosenings of N. **So a nested family that contains loosenings of its own members is a geometric hazard for retreat rivals** (classification: chosen geometry).

**OPEN.** Whether (Π), or (GG) by any other means, can be met for a one-parameter family. This is the exact remaining content of (a)+(b).

**CONJECTURE.** (GG) can be met with dominators whose far parts are pairwise shadow-free on their compensation sets, chosen per rival (non-uniform τ, or no global certificate).

---

## 7. Status of each lever, classified

| Lever | Outcome | Classification |
|---|---|---|
| Audit Prop 1 rival | Answered by L at the first world where Φ turns positive (Theorem A). | No obstruction. |
| Departure–retreat pump (brief 4) | Impossible under a potential (Lemma 3 + Theorem A). The forced retreat acceptances of 4.1 are met. | No obstruction. Brief 3's departure rule was a *chosen rule*, not forced. |
| Theorem Z vertex fill | Needs selected vertex models and KKM over Δ (closed sections). Neither is in (a)+(b). Its conclusion, no correctness zones, holds: L accepts correctness-making records. | Outside scope. Becomes live only with (S). |
| PP19 Thm 5 / Prop S | Their killing rivals change N on {C <_w N} ∖ E, which is conic, so they are not bounded rivals. The localised version is Lemma 5, which bites only at worlds where the dominator lacks compensation. | Chosen geometry (uncompensated dominators, e.g. corner tightenings). |
| Lemma H crossing (one bounded edge) | Vacuous under compensation (Theorem B). CHECKED: GLg appears only in the uncompensated control. | Chosen geometry. |
| G–G shadows | GGg triangles occur for random compensated choices and never for Ψ-certified ones (CHECKED). | Global layer: dominator geometry, not local defences. OPEN whether avoidable for every rival (§6). |
| FF2 Thm 4.1 | Excludes L once a continuous selection must be competitive on faces. | Scope of (S), beyond (a)+(b). |

No failure found follows from the axioms plus (a) and (b) alone.

---

## 8. What this means for audit's extension principle

- **The local half of the principle holds trivially at this scope.** Every coherent candidate receives its own local defence from one rule, uniformly, with no co-design and no reassignment of worlds. Defence of a family against bounded rivals is not the bottleneck.
- **The co-design that matters is between dominators.** Dominators should be chosen with every-world compensation (to avoid Lemma 5) and shadow-free far parts (Lemma 6). This argues *against* PP21 §8.2's corner tightenings as dominators of local rivals: their lack of compensation at k is exactly what creates local refusals.
- **The real tension appears only with (S).** Competitiveness on faces forces a non-additive local layer (FF2), and closed sections enter. So an adversary seeking a genuine obstruction should take the scope to be (a)+(b) plus competitiveness of edge-supported models against bounded rivals. That is where (F1) is lost, and where Theorem A's indifference cannot be used.

**Suggested next tests.**
1. Settle (Π) or (GG) for the chain K_r, including corner rivals near the band edges.
2. Replace L by a non-additive local layer that survives FF2 Step 3, and recheck Theorem B. Theorem B needs only (TC) among bounded links, so it transfers verbatim.
