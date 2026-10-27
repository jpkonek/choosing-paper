# Brief, round 29 (17 Oct 2026): a construction on the WHOLE simplex

Method: the joint two-sided construction (BRIEF18–20). Read FIRST:
- AUDIT_Z123_loop.md: audit's assessment, plus its additive posterior LOOP T1 → D1 → D2 → T1 on [u,e1] ∪ [e1,e2] ∪ [e2,u], every axiom on the loop. Script: audit_loopcheck/check.py.

## Corrections adopted
- **"The difficulty is loops" is withdrawn.** Audit's loop is additive.
- **Z1's three-point obstruction is specific.** It concerns the posterior family on the full three-arm star plus an edge, with Bayes weights equal to the indices. It is not about all coherent families, and not about loops.
- **Z2's isolation theorem holds only under its own hypotheses.** Z2.C (every additive field with a coherent boundary isolates T1) is a conjecture.
- **Star and tripod do not cover every finite collection of paths.**
- **Successively larger path diagrams are no longer the principal target.**

## Standing necessary conditions (refereed results; any whole-simplex cover must meet them)
- **No additive cover** on any (LF) decomposable domain (Theorem gm). So the construction must be non-additive SOMEWHERE.
- **No cover whose worlds all add up.** This holds on every (LF) domain (M0closed; Q4.2). So some world must fail to admit a bounded strictly positive endorsing weight.
- **Fixed-point theorem** (L4, Q3.25; M3 on two-sided domains). The Hahn–Banach endorser field of any cover is degenerate: some world is blind (its endorsers have zero countably additive weight) on a non-null set. This constrains weights, not the ranking.
- **Vertex models are precise** on two-sided domains (L3.1). Edge selections use credal sets on the edge (X3.2). Vetoes cannot be paid (L3.4).

## Obligations (audit)
1. **Global orders first.** Define GLOBAL transition-record orders without fixing an additive primary or a prescribed posterior family. Then DETERMINE which coherent models those orders make competitive. T1 must be among them; the rest of the selection should emerge.
2. **An extension principle.** Prove a genuine extension principle that fills a two-dimensional parameter region while preserving closed sections, with independently verifiable hypotheses.
   - Neither convex-cone amalgamation nor "every finite fragment of the completed theory is satisfiable" counts.
3. **Intermediate test.** The ENTIRE boundary plus a path from T1 to it, inside the global attempt. It is not known whether this needs non-additivity.

## Read
- AUDIT_Z123_loop.md, AUDIT_Y123.md, AUDIT_X123.md, AUDIT_nonlinear_programme.md.
- Z1/Z2 notes and Z3_referee.md; Y1–Y3 notes; X1, X2 notes and X12_referee.md.
- Writeup §2, §8.6.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it.
