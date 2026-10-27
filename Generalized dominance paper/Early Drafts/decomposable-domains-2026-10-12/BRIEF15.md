# Brief, round 17 (15 Oct 2026, 20:30): an ambitious positive attempt for T1, built on the lessons of rounds 14–16

## Author's directive
Use the lessons below to make the next ambitious attempt at a positive answer for T1: an exact cover of T1. The rules of BRIEF13.md apply.
- The deliverable is a complete construction with every axiom verified.
- If it fails, give one honest failure report: where the attempt broke, and the single obstruction (proved, if it is a theorem).
- Do not produce catalogues of necessary conditions.

## Read first
- BRIEF13.md (rules).
- B1_notes.md + B1_referee.md.
- C1/C2 top notes + C12_referee.md.
- D2_notes.md + D2_referee.md + D2_referee2.md.
- E1_notes.md.
- F1_notes.md + F2_notes.md + F12_referee.md.
- writeup/"The Contamination Triangle.tex":
  - §4: the holonomy, i.e. the corner equation x + 1/x = κ + 1 against the box;
  - §7.7: Prop M0 and Theorem M0closed;
  - §8.5.

## The lessons (statuses as refereed)
- **L1 (M0closed).** Any cover of T1 on M_U has a world that does not add up.
- **L2 (D2, two referees).** Worlds that fail to add up exist in full two-world systems.
  - Mechanism: protection at an "end" plus ratio certificates of generators. Each generator trades a thin source strip for a target spread so that any two targets meet near the end at every scale.
  - Protection may sit at ∂U, with all non-additive trades in a region whose payoffs are bounded away from zero (D2′_A, D2′_B; F1, refereed).
  - Every endorsing measure of D2's world 1 must have infinite mass near R₊(1,0), which is interior to U. Conjecture σB is false (F1/F2, refereed).
- **L3 (E1, refereed via F2).** The argument for Theorem M0closed needs only one admissible shadow ν: positive densities making T1 Bayes at an interior weighting. Such shadows always exist (ν^L, Prop Q31).
  - For a.e. t in a non-null set I_ν where the ν-Bayes model B^ν_t is incoherent, KKM gives a selected C with C ⪯_k B^ν_t at every k.
  - A cover needs, for EVERY admissible ν, some world k at which such a comparison is not endorsed by ν_k.
- **L4 (E1.4).** Protected comparisons are invisible.
  - Take an end on which T1 is eventually correct at the protected world. This holds automatically at ∂U ∩ {h_i < 0} (F2.1).
  - Any admissible ν can be reweighted to be heavy there and stays admissible.
  - Its Bayes models are then correct deep in the end, so no dominator comparison into them is protected-positive.
  - So the unendorsed comparisons L3 requires must be **base (unprotected) comparisons, or comparisons at another world**.
- **L5 (E1.5, hypotheses per F2).** E1.5 excludes covers in which every world is an end-protected decoration whose base has an integrable endorsing density, with those densities jointly admissible and heavy at the ends.
  - **Open:** a protected world whose base has no such density; or two or more worlds that fail to add up.
- **L6 (B1).** A world with leading densities on both of its edge regions has a global leading density, and adds up. So the non-adding-up world lacks a leading density on some edge region.
- **L7 (C1).** Glued credal worlds add up. Complete worlds that do not add up are not almost representable (B3; "must be incomplete" is Conjecture B3.C).

## The design target these lessons point to
T1's competitiveness against the "holonomy dominators" must be supplied by comparisons that no admissible shadow endorses. These are the models that beat T1 under every tuple of base densities, because the corner equation conflicts with the box.
- By L4 these cannot be protected comparisons alone, because those are invisible after reweighting.
- So the bases themselves must have endorsing families G_i with no admissible tuple in ∏G_i, even after end reweighting.
- Yet each base must remain consistent with protection (strict (G), (IB), transitivity, closed sections).

The holonomy must be moved into the COMPATIBILITY of the worlds' endorsing weights.

**Warning (heuristic, unproved).** If a protected world's base is "end-light" (its endorsers cannot be heavy at the end) and is additive on its core, then generator plus base chains may produce an accepted δ ≤ 0, i.e. a collapse. Check this. If true, it is a theorem that forces the core to be incomplete or non-additive, or it closes this route.

## RULES
- As in BRIEF13.
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Add no assumptions.
- Write only your own note, plus scripts in a subfolder named after it, in this folder.
