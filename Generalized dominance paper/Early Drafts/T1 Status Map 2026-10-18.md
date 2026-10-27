# T1 coverage: current status map (rounds 33–39), 18 October 2026

**Objective:** EXACT coverage of T1. That means an accuracy ranking with:
- strict (G), (IB), (LA), (S) (every selected model undominated, competitive on supp p, closed sections for every model), direct (C);
- T1 undominated;
- a decomposable domain with (LF) at T1.

Approximate coverage (additive gauge covers of hexagons and 9-gons arbitrarily close to T1) is a recorded side result, not the objective. Nothing below shows that the axioms themselves exclude T1.

**Labels.** "Refereed" = one independent referee, unless stated otherwise. Notes are in `decomposable-domains-2026-10-12/`.

## 1. Settled or verified

| Result | Status | Notes |
|---|---|---|
| ccibu (closed choice from interior Bayes uniqueness, n = 3), as stated | PROVED in full, one reader | KK2_ccibu.tex, KK2_notes |
| Lifting theorem: a protected weak-additive design on any decomposable (LF) domain lifts to a full (FC) cover; any n, any target | refereed (one repair) | II1 Thm 4.1, II2 Cor 2.4, JJ1 |
| No protected weak-additive design through T1, full domain or (LF)+(Av) | refereed; modulo gm in "family form" (CHECKED reading); no ccibu | JJ3 Thm 5.1 + KK1 repair; JJ2 Thm 7.4 independent on the full domain |
| Domain dichotomy: every decomposable domain with coherent vertex models has either precise vertices and (Av), or is one-sided | PROVED, one reader | KK3 |
| No protected design through T1 on ANY decomposable (LF) domain | PROVED modulo the above, one reader | KK3 |
| Dominance theorem without transitivity (model-level KKM, direct (C)) | PROVED | HH1 |
| Barriers that survive dropping transitivity: Q4.2, L4, L3.4, FF2 Thm 4.1, GG2 Thm B | survive, some with repair | HH1 |
| Plain posterior family passes audit's selected-tie test | refereed | FF1 Thm 5.1–5.2, GG3 |
| NA-credal representation theorem; classification of known constructions | PROVED, one reader | GG3 |

## 2. Excluded classes (beyond earlier rounds)
- Additive covers (gm); intersections of additive rankings; worlds that all add up (Q4.2).
- Non-additivity only at the simplex edges, for selections continuous in measure (FF2 Thm 4.1).
- NA-credal designs with a shared leading layer; edge-first lexicographic designs (GG2).
- Credal repairs of VB (GG1).
- Record-local arrow rules (HH2).
- Protected weak-additive rate designs (section 1).

## 3. Open, in order of concreteness
1. **Non-protected rate designs** (KK4). Every rate cover of T1 on the full domain is in branch (CT) (concurrent interior leading ties) or branch (BT) (visible best-ties), PROVED modulo the JJ2 chain. Most concrete open point: does JJ2 Thm 7.2 survive the (BT)-specific weakening of strict-best on the forced collar near a vertex?
2. **Clone route** (II3): T1 tied with a selected model but not itself selected. Needs a leading map that is non-additive on the disagreement set; feasibility unknown.
3. **General (FC) rankings** that do not start from additive lexicographic levels or continuous selections.
4. **Transitive NA-credal question** (GG2/GG3): under closed choice, must every NA-credal world add up?
5. **Worlds with finite obstructions** (CC1 seeds, type α) and worlds refusing forced comparisons (type β: D2, P1, T2n.1).

## 4. Proof hygiene still owed
- A second reading of gm in "family form" (KK1 follow-up). If it holds, Cor CFnone also drops ccibu.
- A referee for KK3 (dichotomy and extension) and for KK4.
- The write-up integrates rounds up to 22 only.
