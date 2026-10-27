# Non-additive rankings for T1: what has been explored, what has not, what to read

16 October 2026. A hand-off for audit. Plain English throughout; technical names are given in brackets so that the reader can find them in the notes.

**Statuses**
- **refereed once:** checked by one independent referee.
- **unrefereed:** proved in a note, not checked.
- **CHECKED:** verified by inspection, not fully proved.

**Where files are**
- "Notes" are in `decomposable-domains-2026-10-12/`.
- The write-up is `The Contamination Triangle.tex/.pdf` (236 pp.). It covers rounds up to 22; rounds 23–25 are in the notes only.
- Two of the files below are project documents (claude.ai project "CCT"), not files in this folder.

---

## 1. The question and the framing

- **Setting.** Three worlds. T1 is the ε-contamination of the uniform distribution. A **cover** of T1 is a ranking — one preorder per world on the evaluable models of a decomposable domain with (LF) at T1 — satisfying:
  - strict (G), (IB) and (LA);
  - (S): a coherent selection p ↦ C_p, closed sections for every evaluable model, and competitiveness on supp p;
  - (C);
  - T1 undominated.
- **What is settled.**
  - Additive covers are impossible on every such domain (Theorem gm).
  - The question is whether some non-additive ranking covers T1.
- **The main working domain.** Most work is on the U-domain M_U: the evaluable models are the subsets of a cone U slightly larger than T1's cone, so a model can accept or stay silent but never accept −f near the target.
  - On M_U, (G) together with (IB) means each world is an ordering of its *error sets* satisfying de Finetti cancellation (N9.4).
  - So a world is a comparative-probability-like order on sets of problems.

## 2. What has been explored

### 2a. Exclusions (classes of non-additive ranking shown not to cover T1)

1. **Rankings a single bounded weighting can summarise ("adds up", case M0).**
   - **What this means.** At every world, some bounded weight, positive on every non-null set of mixed problems, endorses every relevant comparison.
   - **What the class includes:**
     - credal unanimity (CP-a);
     - lexicographic orders with additive tie-breakers;
     - additive orders with ties broken ordinally;
     - glued credal worlds (C1);
     - intersections of additive rankings.
   - **Status:**
     - On M_U: Theorem M0closed. A second proof is L4.2 (refereed once).
     - On every (LF) decomposable domain: Q4.1–Q4.2 (refereed once, at the CHECKED status of M3.9).
     - Intersections of additive rankings have a separate short proof on every (LF) domain: project doc *Intersections of Additive Rankings* (one reading).
2. **Complete worlds.**
   - With three complete worlds, the vacuous model is always dominated, so full coverage needs incomparability (*Three Complete Rankings Cannot Cover*; *Complete Rankings for Any Number of Worlds*).
   - For T1: a complete world in a cover that fails to add up is not "almost representable" (B3, refereed). Ruling such worlds out entirely is Conjecture B3.C.
3. **Veto and lexicographic designs.**
   - The ordinal limit of additive near-covers is the "veto–Brier" ranking VB (L3). It satisfies every axiom except closed sections, which fail only at boundary weightings.
   - "Vetoes cannot be paid" (L3.4, refereed): this failure is forced for any design that ranks a world's own wrong acceptances first.
4. **Decorations of an additive base.**
   - **What a decoration is.** An additive or tail-dominance base, with extra or reversed trades protected at "ends" of edge chains (D2 type).
   - **Which are excluded:**
     - whenever the failure to add up is confined to small sets (H1.2);
     - whenever protection sits at ends that T1 handles correctly (E1.4, H2.3, J1, K1);
     - whenever all worlds have unbounded but locally finite endorsers and the edges are straight-line ("linear-host") families (U1, refereed).
5. **Structure any cover must have.**
   - **Hahn–Banach fixed point (L4, refereed; Q3.25, refereed).** The endorsers of any ranking form an undefeated field. So a cover forces that field to be **degenerate**: some world gives zero ordinary weight to a non-null region (a "blind set").
   - **Excluded within that requirement:**
     - one blind world at an interior weighting (L1, refereed);
     - the "T1-shadow" pattern, and any "blind target" (N1, N2, refereed).
   - **What remains:** the reduction theorem R21 (assembled; inputs refereed) lists the surviving configurations. All of them need two or more worlds without strictly positive integrable endorsers, or the vertex configuration (V). (V) with well-behaved partners and nested, transverse edges is closed (Q1, T1n, refereed).
6. **Splicing at a pair-indexed weighting (the author's proposal; project doc).**
   - **The construction.** Compare D and D′ by replacing their common advice with the advice of a coherent C_p, where p is chosen from their disagreement vector, and then applying a fixed base ranking.
   - **Gives (G) and (IB) for any base with (G).**
   - **Not transitive.** With the homothetic ordinal base, a three-model cycle appears already in two worlds.
   - **The two repairs by intersection both fail (S):**
     - closing under substitution collapses the ranking to the background order;
     - intersecting over contexts that include the two vertex contexts destroys competitiveness.
   - **What remains open.** A base that is not independent but whose spliced comparisons are transitive. That class has not been searched systematically.

### 2b. Constructions (non-additive worlds that actually exist)

All of these are **full two-world systems on M_U** satisfying every axiom:

| System | What it shows | Note | Status |
|---|---|---|---|
| D2 | First world that fails to add up | D2_notes | two referees |
| D2′ | Same, with protection at ∂U | F1 | refereed |
| C2.1 | A world with no leading density (Pareto unanimity of two densities) | C2 | refereed |
| L2 | Non-null blind set; refutes K3.C | L2 | refereed |
| P1 | Totally blind world | P1 | refereed |
| H2.4 | Neither world adds up | H2 | refereed |
| T2n.1 | Both worlds totally blind | T2n | refereed |

Every one of them is built by **the same recipe**:
- a dominance ("tail") cone along a one-dimensional chain of coherent models;
- plus countably many thin "generator" trades, whose targets are laid out by finite projective planes so that any two targets overlap near the chain end.

Every one of them also has an **unbounded but ordinary (σ-finite) endorsing density** that grows toward the chain end (property (Loc)). Next to well-behaved partners, that is exactly what the exclusions use.

**Near-miss in three worlds:** VB (item 3 above).

## 3. What has not been explored, or only in a limited way

1. **Construction technique.** Only the recipe of §2b has been used. Ideas never tried as constructions:
   - orders defined from credal-set geometry or threshold statistics. The homothetic ordinal rankings of v2 are of this kind; they fail (IB) (v3 §2), and the splicing note shows one way of restoring (IB) gives cycles;
   - non-Archimedean or ultrafilter-valued orders other than the one lexicographic limit VB;
   - orders defined directly through the exact consistency test (*Coverage after Neutral Abstention* §3) with a non-additive selection. This has never been executed, except to reproduce additive systems.
2. **Three worlds.**
   - **No non-additive three-world construction exists,** for any target.
   - **Where every attempt broke:** in defining a world's verdicts on comparisons *out of interior selected models*, whose error sets cross instead of nesting (B1, T2n, U1, V1).
   - **What is missing:** a general method for this step.
3. **Two-sided domains** (a model may also accept −f near the target).
   - What exists: reductions only (M3, Q4) and a few two-grade designs (L3.6).
   - Missing: non-additive constructions that treat silence and wrong acceptance differently.
4. **Worlds with no unbounded ordinary endorser either (non-(Loc)).**
   - Never built, in any number of worlds.
   - In two worlds next to an additive world they are conjectured impossible (L2.C). P1 proves the fixed-window half.
   - In three worlds, the natural mechanism (incompatible edge endorsers on the shared strip) is impossible under the conditions of Q1 and T1n.
5. **Worlds violating the uniform condition (NC)** — some combination of accepted comparisons is negative everywhere.
   - Never built.
   - Q3 shows they are harmless next to well-behaved partners.
6. **Finite-certificate (M1) worlds.**
   - Never built.
   - Every certificate must contain a rigid comparison that no axiom forces (K2.1). The natural scheme is empty over Brier-type bases (K2.6).
7. **The one surviving positive blueprint (U1.5 / V1).**
   - **The blueprint:** edge chains made of "segment hosts", with an explicit σ-finite field under which T1 is exactly the best model at the uniform weighting. No known theorem excludes it.
   - **What V1 (unrefereed) shows a cover built on it would need:**
     - a discontinuous jump of the selection inside the simplex;
     - two blind worlds jointly sheltering that jump.
   - **Already excluded:** the "far end first" way of doing this (V1.6).
   - **Open:** Question Q_V1.

## 4. What to read, in order

1. `START HERE -- Coverage Status.md`: the dated sections from 15–16 October.
2. `decomposable-domains-2026-10-12/R21_reduction.md`: the reduction theorem and its open questions. Then T1n_notes, T2n_notes, U1_notes (with U1_referee), V1_notes, which update it.
3. The write-up §8.6, "The fixed-point reduction", and the Summary for T1 in the introduction.
4. **The constructions:**
   - D2_notes (§§2–3);
   - P1_notes, Part I (P1.10–P1.14);
   - T2n_notes, T2n.1 (doubly blind system).
   - Read these for the one recipe we have.
5. **The near-miss:** L3_notes (VB, L3.3–L3.4) with L23_referee.
6. **The author's splicing proposal, and the intersection theorem:** project docs *Splicing at a Pair-Indexed Weighting* and *Intersections of Additive Rankings*.
7. **Background on independence and coverage:**
   - *Full Coverage by Homothetic Credal Families v3* (two-world coverage by additive penalties; why the v2 ordinal recipe fails (IB));
   - *Three Complete Rankings Cannot Cover*;
   - *Coverage after Neutral Abstention* §3 (the exact consistency test).
8. **Round history:** `Coverage on Decomposable Domains - Round Report 2026-10-12.md`, addenda for rounds 14–25.

## 5. Questions on which audit's advice would help

1. Is there a construction technique, beyond §2b's recipe, that could produce a three-world non-additive world? In particular, one that handles comparisons between models whose error sets cross.
2. Is the splicing idea worth pursuing with a different base: a non-independent base whose spliced comparisons are transitive? If so, what properties should the base have?
3. Should the positive search move to two-sided domains, where the non-additive theory is much thinner?
4. Is the exact consistency test, run computationally on fine finite approximations of T1, a sensible way to look for candidate covers? Or do the continuum features (atomlessness, closed sections) make finite searches uninformative?
5. Given §2a, does audit see an impossibility argument that would cover everything at once — for example, by attacking the blind-set requirement directly?
