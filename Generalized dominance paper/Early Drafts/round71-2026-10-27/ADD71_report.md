# ADD71 report: the best disjointly additive ranking (round 71, 27 Oct 2026)

Notation follows AUDITOR_note.md and LEAD_claims.md. A change is r=(A,B) with A∩B=∅, and supp r = A∪B. Write 𝒜 for the changes available to some coherent model; 𝒜 is closed under sub-changes (Lemma join). 𝒟 ⊆ 𝒜 is the set of dangerous changes (available to a coherent model, with P(r)=Ω). For a fixed world w, 𝒢_w is the set of changes guided at w, and 𝒫_w = {r : d_w(r)>0} together with the null changes. A ranking given by independence is a choice, for each w, of a family 𝒱_w of changes (those accepted at w). "Additive" means disjoint additivity: if r1,r2 ∈ 𝒱_w and supp r1 ∩ supp r2 is null, then r1⊔r2 ∈ 𝒱_w. Under independence this is exactly Prop 6.2(c), because any two changes with disjoint supports can be chained (Z=B1∪B2, Y=(Z∖B2)∪A2, X=(Y∖B1)∪A1). Axioms 1–4 are (G) 𝒢_w ⊆ 𝒱_w, (S) 𝒱_w ⊆ 𝒫_w, independence, and (Prot) ∩_w 𝒱_w contains no non-null change in 𝒜. "Neutral" is the lead's neutrality. Given protection it is equivalent to (3′): 𝒱_w ∩ 𝒟 ⊆ 𝒢_w for every w.

## Results (one line each)

- **R1 PROVED.** With |Ω|=2, no dangerous change is guided at any world. So R∩ refuses every dangerous change at both worlds.
- **R2 PROVED.** With |Ω|=2, R∩ is disjointly additive. It is the largest ranking satisfying 1–4 and neutrality, so it is the largest neutral additive ranking. R0 ⊊ R∩.
- **R3 PROVED (any Ω, using only μ{P_S=0}=0 and μ{h_w=0}=0).** Every dangerous change is non-guided at two or more worlds. This sharpens the guidance-protection lemma (Lemma 6.5).
- **R4 PROVED.** Under neutrality the axioms decouple world by world. A ranking satisfies 1–4, neutrality and additivity iff each 𝒱_w is ⊔-closed with 𝒢_w ⊆ 𝒱_w ⊆ 𝒫_w and 𝒱_w ∩ 𝒟 ⊆ 𝒢_w. Adding 𝒫_w∖𝒜 keeps all of these, so maximal such rankings contain R0 and cover. This holds for arbitrary Ω.
- **R5 PROVED (explicit canonical ranking).** Define the w-safe changes as safe_w = {s ∈ 𝒫_w : s⊔g ∉ 𝒟∖𝒢_w for every g ∈ 𝒢_w∪{∅} disjoint from s}. Then define R^c_w = {r ∈ 𝒫_w : r⊔s ∉ 𝒟∖𝒢_w for every s ∈ safe_w∪{∅} disjoint from r}.
  - R^c satisfies 1–4, neutrality and additivity, and the proof needs no choice.
  - R0 ⊆ R^c ⊆ R∩, and R^c covers.
  - Using Zorn, R^c is exactly the intersection of all maximal neutral additive rankings.
  - When |Ω|=2, R^c = R∩.
- **R6 PROVED.** R0 is not maximal among additive rankings satisfying 1–4 (or 1–4 with neutrality). R^c ⊋ R0 in 2 worlds (the lead's example) and in 3 worlds. The 3-world witness is a change whose removed set has a singleton credal hull; such changes are "robust".
- **R7 PROVED (point masses with margin 1; LP check is NUMERICS, py/add71_safe.py).** In 3 worlds there are two x-safe changes s and t whose disjoint union is dangerous and non-guided at x. So **there is no largest neutral additive ranking**, and R^c is strictly below every maximal one. The same four atoms also give a smaller counterexample to additivity of R∩ than L4 does.
- **R8 PROVED.** Without neutrality there is also no largest additive ranking.
  - For any world w0, take 𝒱_{w0} = 𝒫_{w0} (pure score), with any neutral additive families at the other worlds. This "one-free-world" ranking satisfies 1–4 and additivity, by R3.
  - It strictly contains R^c and is not symmetric across worlds.
  - In 3 worlds two worlds cannot both be free.
- **R9 PROVED.** With |Ω|=2, for each c ∈ [0,∞] the cone rule is a maximal additive ranking satisfying 1–4. The rule refuses a dangerous r at world 1 iff d_1(r) ≤ c·d_2(r), and refuses it at world 2 otherwise. c ∈ {0,∞} gives the two dictator rankings.
  - The swap-symmetric strict version accepts dangerous r at w iff d_w > d_{w′}. It is additive and lies strictly between R∩ and the c=1 rule.
  - It is not maximal. It compares scores across worlds, so it is not invariant under rescaling one world's score.
- **R10 PROVED (sketch).** When |Ω| ≥ 3, no ranking with 1–4 and additivity can decide 𝒜-changes at each world as a function of d(r) alone. So any explicit form must use the sets involved, not just the score vector, and the 2-world cone rules do not extend.
- **R11 PROVED.** The proposed rule satisfies 1–4 and additivity: accept at w iff guided at w, or d_w>0 and r is not a sub-change of a dangerous change non-guided at w. But it is contained in R^c, strictly when |Ω|=2, so it is not maximal.
- **R12 (iii) PROVED / CONJECTURE.** Unanimity over reweightings g is automatically additive, guided and score consistent (if 1∈𝒢).
  - PROVED: to protect D_S in two worlds, the ratios g(b)/g(a) must be spread without bound, for a in quadrant IV and b in quadrant II.
  - PROVED: in the limit (all positive g) the rule is guidance only. That protects, but it covers nothing.
  - CONJECTURE: no 𝒢 gives both protection and coverage.
  - What the earlier notes already settle is summarised below. They do not settle (iii) under the present axioms.
- **Check of L4: CHECKED** (cx.py output reproduced: all six splits "ok"; atoms each have a negative coordinate, so the change is available to D_S; H(r)=∅ because every world has atoms negative there).

**Bottom line.** "The best additive ranking" has no single answer: no largest one exists, with or without neutrality. The natural canonical, choice-free and permutation-equivariant object is R^c, the intersection of the maximal neutral additive rankings. It is explicit, strictly larger than R0, equal to R∩ in two worlds, and covers. In three or more worlds it is strictly below every maximal ranking, and it depends on magnitudes (bounded vector-measure ranges), not only on signs.

---

## Proofs

### R1 (two worlds, Ω={1,2}; dangerous changes are never guided)
Let r=(A,B) be non-null, guided at world 1, and available to D_Q.
- On A: h_1>0 and A∩D_Q is null. Gambles with h_1>0 and h_2>0 lie in D_S ⊆ D_Q, and {h_2=0} is null. So h_2<0 a.e. on A.
- On B: h_1<0 and B ⊆ D_Q. A gamble with h_1<0 and h_2≤0 is not in D_Q. So h_2>0 a.e. on B.

Hence d_2(r) = ∫_A h_2 − ∫_B h_2 < 0, and r is not dangerous. The case of world 2 is symmetric. So H(r)=∅ for every dangerous r, and R∩ gives V(r)=∅ there.

### R2 (two worlds: R∩ is additive; largest neutral ranking)
Let r=r1⊔r2 with w ∈ V(r1)∩V(r2). If r ∉ 𝒟, then V(r)=P(r) ∋ w, since d_w(r) = d_w(r1)+d_w(r2) > 0 (null parts contribute 0).

If r ∈ 𝒟, both parts are in 𝒜. If either part were non-null and dangerous, its V would be ∅ by R1, so neither is. So for each part, V(r_i) = P(r_i) ∋ w and P(r_i) ≠ Ω. Hence d_{w′}(r_i) ≤ 0 for both, so d_{w′}(r) ≤ 0, which contradicts r ∈ 𝒟. So the case cannot occur.

Neutrality with protection forces V(r) ⊆ H(r) = ∅ on 𝒟, so every neutral ranking satisfying 1–4 is contained in R∩. For R0 ⊊ R∩, take the lead's example: add A near (2,−1) and (−1,−1), so d≈(1,−2). The change is available to D_S, refused at world 1 by R0 and accepted there by R∩.

### R3 (dangerous changes are non-guided at two or more worlds)
Suppose r=(A,B) is non-null, available to D_Q, and guided at every world except w.
- On A, h_v>0 for all v≠w. If also h_w>0, then inf h ≥ 0, so h ∈ D_S ⊆ D_Q after discarding the null set {P_S=0}. For infinite Ω, use the countable Ω_0 of Lemma 2.1(f) as in Lemma 6.5. Since A∩D_Q is null, h_w<0 a.e. on A.
- On B, h_v<0 for all v≠w and h ∈ D_Q, so h_w>0. (Otherwise sup h ≤ 0, and such gambles are not in D_Q.)

So d_w(r)<0, and r is not dangerous. ∎

Consequence: when |Ω|=2, H(r)=∅ on 𝒟 (which is R1 again).

### R4 (decoupling under neutrality)
Conditions (G), (S) and additivity each concern a single world. Given protection, neutrality is equivalent to (3′) (lead L3).

Conversely, (3′) implies protection. A non-dangerous 𝒜-change is refused wherever d_w ≤ 0. A dangerous change is accepted only where it is guided, and by R3 it is non-guided somewhere.

Adding 𝒫_w∖𝒜 to 𝒱_w preserves everything:
- a disjoint union with a non-𝒜 part is non-𝒜, because 𝒜 is closed under sub-changes, and has d_w>0;
- non-𝒜 changes are never dangerous.

So maximal rankings contain R0. Coverage then follows from L2(b) (the repair theorem) and protection. No finiteness of Ω is used.

### R5 (R^c)
(a) *Validity without choice.*
- 𝒢_w ⊆ safe_w, and safe_w is closed under ⊔ with 𝒢_w.
- R^c_w ⊆ safe_w: take s=g ∈ 𝒢_w.
- 𝒢_w ⊆ R^c_w: if r is guided and s is safe, r⊔s = s⊔r ∉ 𝒟∖𝒢_w.
- 𝒫_w∖𝒜 ⊆ R^c_w trivially.
- R^c_w ∩ 𝒟 ⊆ 𝒢_w: take s=∅.

For ⊔-closure, let r1, r2 ∈ R^c_w be disjoint and s ∈ safe_w∪{∅} be disjoint from both.
- First, r2⊔s ∈ safe_w. For guided g, s⊔g is safe, and r2 ∈ R^c_w gives r2⊔(s⊔g) ∉ 𝒟∖𝒢_w. If r2 is guided or non-𝒜, this is direct.
- Then r1⊔(r2⊔s) ∉ 𝒟∖𝒢_w, because r1 ∈ R^c_w.
- So r1⊔r2 ∈ R^c_w.

(b) *Intersection of the maximal rankings.* A valid world-w family (as in R4) containing s exists iff s ∈ safe_w. For "if", the family 𝒢_w ∪ (𝒫_w∖𝒜) ∪ {s⊔g : g ∈ 𝒢_w∪(𝒫_w∖𝒜)∪{∅}} is valid. For "only if", every valid family contains 𝒢_w and is ⊔-closed.
- If r ∈ R^c_w and 𝒱 is maximal, then 𝒱 ∪ {r⊔s : s ∈ 𝒱∪{∅}} is valid, because members of 𝒱 are safe. By maximality, r ∈ 𝒱.
- If r ∉ R^c_w, some safe s has r⊔s ∈ 𝒟∖𝒢_w. Extend a valid family containing s to a maximal one by Zorn; the conditions are finitary, so chains have valid unions. That maximal family cannot contain r.

(c) *Comparisons.* R^c ⊆ R∩ because R∩_w = 𝒢_w ∪ (𝒫_w∖𝒟) when |Ω|=2, and R∩ satisfies (3′) in general. In two worlds, safe_w = 𝒫_w∖𝒟 by the R1 argument, and R^c_w = 𝒫_w∖𝒟 = R∩_w. (A non-dangerous 𝒜-change with d_w>0 has d_{w′} ≤ 0, so it cannot complete a non-dangerous safe s to a dangerous change.)

Reading of R^c: accept r at w unless some change that w could consistently be made to accept would complete r to a dangerous change not guided at w.

### R6 (R^c ⊋ R0 in three worlds)
Take E=ℝ³, μ ≈ Lebesgue, and q=(⅓,⅓,⅓). Let B = {h : 0 < Σh < δ‖h‖, 1 < ‖h‖ < 1+κ}.

First, Q_B = {q}. Let q′≠q and u=q−q′, which lies in the plane Σ=0. Take h0 = c·u/‖u‖ with c ∈ (1,1+κ), and h = h0 + τ𝟏 with small τ>0. Then h ∈ B and q′·h = −c‖u‖₂²/‖u‖ + τ < 0 on an open set. So q′ ∉ Q_B.

Let r remove B and add a small ball A around (5,−1,−5). Then Σ<0 on A, so A misses D_q = hull(B), and r ∈ 𝒜. For δ and κ small, d_x(r) ≈ 5μ(A) − O(μ(B)) > 0. B removes gambles with h_x>0, so r is not guided at x. So R0 refuses r at x.

Any extension r⊔s ∈ 𝒜 is available only to D_Q with Q ⊆ Q_B = {q}, so q·d(r⊔s) < 0, and no extension is dangerous. So r ∈ R^c_x.

### R7 (no largest neutral additive ranking in three worlds)
Use coordinates (x,y,z). Place unit point masses (in reality small balls, plus a background density of total first moment < 1) at σ1=(−1,−1,5), σ2=(4,−1,1), τ1=(−1,5,−1), τ2=(4,1,−1). All four lie outside D_S.

Let s add σ1 and σ2, and let t add τ1 and τ2. Then:
- d(s)=(3,−2,6), d(t)=(3,6,−2), d(s⊔t)=(6,4,4).
- s⊔t is available to D_S, so it is dangerous. It is not guided at x, since σ1 and τ1 have h_x<0.
- s is x-safe. The only x-guided resources disjoint from s are adding τ2 and removing τ1 (removal is over-approximated as always allowed), plus background < 1. The LP maximum of min_k d_k(s⊔g) is −1 (py/add71_safe.py). The same holds for t.

By R5(b), one maximal world-x family contains s and another contains t, and none contains both. So maximal neutral additive rankings are not unique, and R^c_x contains neither s nor t. R∩ accepts both s and t at x (they are non-dangerous with d_x>0) but refuses s⊔t there. That is a 4-atom failure of additivity for R∩.

### R8 (one free world)
𝒫_{w0} is ⊔-closed and contains 𝒢_{w0}. For dangerous r, R3 gives a non-guided world v≠w0, and the neutral family at v refuses r. So protection holds, and the ranking covers (it contains R0 after the R4 enlargement).

It accepts dangerous non-guided changes at w0 (they exist; see Remark 5.4), so it is strictly larger than R^c.

Two free worlds y and z fail in three worlds. Take r adding balls near (1,10,−1) and (1,−1,10): then d≈(2,9,9) and H(r)={x}, so r is accepted at x by guidance and at y and z by score, which breaks protection.

### R9 (two-world cone rules)
For r ∈ 𝒜, 𝒱_1 accepts r iff d_1>0 and d_1 > c·d_2, and 𝒱_2 accepts r iff d_2>0 and c·d_2 ≥ d_1. Non-dangerous 𝒜-changes with d_1>0 have d_2 ≤ 0, so they satisfy the world-1 test, and symmetrically for world 2.
- Both 𝒜-parts are convex cones in d, so they are ⊔-closed within 𝒜. Unions with non-𝒜 parts are non-𝒜.
- Guided 𝒜-changes are in the right cone (R1 gives d_{w′}<0).
- The two cones are disjoint on ℝ²₊₊, so every dangerous change is refused at exactly one world. That makes the rule auditor-maximal, hence maximal among additive rankings.

Whether every maximal additive ranking in two worlds is a cone rule, and whether R∩ is the intersection of all of them: **unclear**. The intersection is ⊆ R∩, by the two dictators.

### R10 (no rule based on d alone when |Ω| ≥ 3; sketch)
Gambles with h_x>0 and some other coordinate negative lie outside D_S, and their directions generate the open half-space {d_x>0}. By Lyapunov, the x-guided changes available to D_S realise every sufficiently small v ∈ ℝ³₊₊.

Let r be the L4 change, with H(r)=∅, scaled down by proportional subsets. Its subsets realise an open set of small vectors in ℝ³₊₊, so some v is realised both by r′ ⊆ r and, at each x, by an x-guided change. If acceptance at x depended on d alone, guidance would force r′ to be accepted at every x, which breaks protection. ∎

### R11 (the proposed rule)
Additivity: if r1 is accepted by the second clause and r1⊔r2 ⊆ ρ with ρ ∈ 𝒟∖𝒢_w, then r1 ⊆ ρ, a contradiction. Guided ⊔ guided is guided.

Protection: a dangerous r is a sub-change of itself, so it is accepted only where guided, and R3 applies.

Its extra acceptances are changes with no dangerous extension at all. These are robust, so they lie in R^c. When |Ω|=2 the lead's d≈(1,−2) change can be extended to a dangerous one by adding mass near (−0.1,3). So R∩ accepts it and this rule does not, and the inclusion is strict.

### R12 ((iii), brief)
Rule: accept at w iff ∫_A h_w g dμ − ∫_B h_w g dμ > 0 for all g ∈ 𝒢 (with 1 ∈ 𝒢). Guided changes pass automatically. Additivity holds because sums of positive numbers are positive.

Protection of D_S with Ω={1,2}: let F add small pieces of masses α near a=(M,−1) and β near b=(−1,M), with ρ_g = g(b)/g(a). F is accepted at both worlds iff ρ_g ∈ (α/(Mβ), Mα/β) for every g ∈ 𝒢. So protection requires, for every k>0, some g with ρ_g outside (k/M, kM). The ratio spread of 𝒢 must therefore be at least M² for every M, i.e. unbounded.

In the limit where 𝒢 is all bounded positive g, the rule is guidance only. Then X = D_S ∪ (a ball near (−1,M)) is incoherent and undominated (an everywhere-guided change can add only D_S and remove only nowhere-positive gambles). So that rule does not cover.

**CONJECTURE:** no intermediate 𝒢 achieves both protection and coverage.

What the earlier project notes already settle (r9/INTERSECTIONS_additive.md, AUDIT_quorum.md, EXPLORATION_MAP_2026-10-16.md, T1n_notes.md; not redone here):
- Unanimity over a family of strictly guiding integral rankings transfers every strict comparison to a single mixture ψ = Σ c_k L^k, using a countable dense subfamily. Such intersections are "adds-up" (M0) rankings.
- Under the old axiom package ((LA), (S), (C), closed sections, (LF) decomposable domains, target T1), they cover no target that a single additive ranking fails to cover, and so they do not cover T1.
- Quorum rankings were a non-additive alternative there. They give up finite-chain consistency, and no cover was built.
- Those results use (S)/closed sections and the old four-advice framework. They do **not** settle protection plus coverage for the present application's axioms, which have no (S). The transfer lemma does apply verbatim: R_𝒢 ⊆ R_ψ for strict comparisons.

## Open
- Explicit description of maximal additive rankings without neutrality when |Ω| ≥ 3. They are set-dependent (R10) and non-unique (R8).
- Whether R^c is strictly larger than R0 ∪ (robust changes).
- Whether every maximal additive ranking contains R^c, so that R^c would be the intersection of all maximal additive rankings, not just the neutral ones.
- (iii) as conjectured above.
