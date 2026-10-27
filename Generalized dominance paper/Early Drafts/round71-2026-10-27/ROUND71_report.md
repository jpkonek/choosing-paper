# Round 71 report: maximal rankings, additivity and the role of condition (3)

27 October 2026. This round was a research round; the manuscripts are unchanged.

The round had three parts:
- **REF71**: an independent referee of the auditor's note and the lead's claims;
- **ADD71**: disjoint additivity;
- **PHIL71**: justification.

Full reports are in this folder.

Notation:
- A change r = (A, B) adds A and removes B.
- d_w(r) is its score increment at world w.
- A change is *dangerous* if some coherent model could make it and it improves the score at every world. This is internal shorthand only.

The **four conditions** are:
1. guidance;
2. independence;
3. strict score consistency;
4. every coherent model is undominated under the ranking.

## 1. Verdicts on the auditor's note (REF71)

- **Exact protection condition: PROVED.** Under independence, reflexivity and strict score consistency, every coherent model is undominated iff every change some coherent model could make is refused at some world.
- **Characterisation of the maximal rankings, and their existence for any set of worlds: PROVED.**
  - Everything is well defined on a.e.-classes of changes.
  - It needs the condition μ{P_S = 0} = 0, a separable gamble space and an order unit. It needs neither (M1) nor (M3).
  - The reason the characterisation is easy: the four conditions each constrain one change at a time, so the maximal rankings are maximal change by change.
- **Coverage for every maximal ranking: PROVED.** Every clause of "covers K" holds under (M1)–(M2).
- **Restricted domains closed under coherent hulls: PROVED.** Everything carries over. Each such ranking covers K exactly when D_K ⊆ U a.e. and local freedom holds, which is the answer of Cor 7.1(d).

## 2. New results

### (a) Exact coverage criterion (PROVED)

Consider any ranking with guidance, independence and strict score consistency. Its undominated models are exactly the coherent ones, and every incoherent model is dominated by a coherent one, iff both of these hold:
- every change some coherent model could make is refused at some world;
- every incoherent model has, to some coherent model, a change accepted at every world.

By the repair theorem, the second clause holds whenever the ranking satisfies (5′): it accepts every change that no coherent model could make, at every world where that change improves the score.

**Class theorem.** Every ranking satisfying the four conditions and (5′) covers every credal set.
- These rankings are exactly the independent relations between R0 and some maximal ranking.
- R0 is the smallest of them.
- Condition (3) of Prop 6.3 is therefore not needed for coverage. It only selects the smallest member.

### (b) Canonical intersection R∩ (PROVED)

R∩ is the intersection of all maximal rankings. It accepts a change wherever it improves the score, with one exception: a dangerous change is accepted only where it is guided.
- It is the largest relation satisfying (3′): a change some coherent model could make, and that improves the score at every world, is accepted only where it is guided.
- Equivalently, it is the largest ranking satisfying the four conditions together with neutrality: a dangerous change refused at one non-guided world is refused at all non-guided worlds.
- R0 ⊊ R∩.

### (c) Sharper guidance-protection lemma (PROVED, any Ω)

A non-null change that a coherent model could make is unguided at two or more worlds, or its score does not improve everywhere. Equivalently, every dangerous change is non-guided at two or more worlds.

### (d) Maximality is incompatible with disjoint additivity (PROVED)

The example has three worlds and the vacuous model. Take six small balls, one about each vector with one coordinate equal to 1, one equal to −1 and one equal to 10. Adding all six is dangerous and is guided at no world.

For each world x, split the change into two halves, each made of three whole balls:
- one half has increments (10, −1, 21);
- the other has increments (10, 21, −1).

Coordinates are listed in the order (x, y, z). Both halves improve at x, and each fails somewhere.

So every maximal ranking accepts both halves at the world where it refuses the whole change. R∩ fails disjoint additivity too; a four-ball example shows this.

### (e) The additive landscape (ADD71: PROVED unless marked)

- **Two worlds.** No dangerous change is guided anywhere. R∩ is disjointly additive, and it is the largest neutral additive ranking.
- **Three or more worlds.**
  - There is **no largest** additive ranking satisfying the four conditions, with or without neutrality.
  - R0 is **not** maximal among additive rankings.
  - The intersection R^c of the maximal neutral additive rankings is explicit and needs no choice. It lies strictly between R0 and R∩, and it covers. But its definition quantifies over completions of changes, and it is not elegant.
  - No additive ranking can decide changes by their score vectors alone.
- **Unanimity over truth-directed reweightings** is automatically additive and never mentions the coherent class.
  - Protection forces the weight ratios to spread without bound.
  - In the limit the ranking accepts only guidance, which covers nothing.
  - CONJECTURE: no family gives both protection and coverage. Earlier notes (r9) do not settle this under the present axioms.

## 3. Justification (PHIL71; lead concurs)

- **Maximality with an arbitrary refusing world: reject.** Every change that must be refused improves at every world. The paper's scores are invariant under rescaling each world separately, so no score-based rule can pick the refusing world. The arbitrariness is built in.
- **R∩: a legitimate alternative, not a replacement.**
  - It makes no arbitrary choice.
  - It has a perverse dependence on other worlds. A change with increments (1, −2) is accepted at world a. Make it better at world b, so its increments are (1, ε), and it is refused at a.
  - It loses disjoint additivity.
- **(5′) with protection: recommended.** It is weaker than condition (3), contains R0, and gives the class theorem.
  - The coherent class enters in exactly two places:
    - as a premise, that coherent models are undominated;
    - in (5′), "no coherent model could make it".
  - So the paper's verdict stands: the ranking represents coherence and does not derive it from accuracy alone.
  - For R0, protection is proved from (3). For the class, protection is a premise.

## 4. Recommendation for the application paper (not yet made)

Replace the role of Prop 6.3 with the class theorem (a). Keep R0 as the concrete ranking, described as the smallest covering ranking of this kind and the one that keeps disjoint additivity. The additions would be:
- the exact criterion;
- a remark on R∩ and on maximal rankings, with the additivity counterexample;
- the sharper protection lemma.

Estimated length: about 1–1.5 pages.

LDG Prop 7.1(c) has an abstract analogue of the exact criterion, which needs only strict score consistency and independence. It could be stated there in two lines.

## 5. Open

- The largest additive rankings in three or more worlds: there is no explicit form, and possibly none exists.
- Unanimity over reweightings: protection together with coverage (conjectured impossible).
- Whether any principle that never mentions the coherent class gives coverage. This is the real open problem behind "represents, does not derive".
