# Brief, round 20 (16 Oct 2026, 08:30): settle T1, boldly

## Author's directive (verbatim intent)
Settle the T1 question: either prove a genuine impossibility result, or be more bold and creative about settling it positively. The author's sense is that a positive answer is possible, and that we have not been clever enough in how we construct the accuracy rankings.

## Critical diagnosis (read this before anything else)
**1. Every positive design so far was "additive base plus decoration" on M_U.** Examples: protected ends (D2), glued credal worlds (C1), reversed or extra comparisons (B1), and the M1 scheme over additive bases (K2.5).
- The exclusions (M0closed, H1, H2, J1, K1, K3 patch theorem) all work the same way. They exhibit ONE admissible shadow ν and show it is not "defeated".
- **Admissible shadow:** positive densities with T1 Bayes at an interior weight.
- **Defeated at t:** the KKM dominator C ⪯_k B^ν_t of the incoherent Bayes model B^ν_t is unendorsed by ν_k at some world k.
- Decorations of additive bases always leave the base's own density (suitably reweighted) undefeated.
- **So a cover must defeat EVERY admissible shadow,** including ones adapted to the ranking.

**2. The non-additive analysis is confined to M_U.**
- On a two-sided decomposable domain, a model can accept f, accept −f, or stay silent near the target. So each world has two grades of error (silent; wrong). None of the ordinal machinery below has a two-sided version: N9.4 normal form, B1, D2, H1, K3.
- On two-sided domains, only ADDITIVE covers are excluded (Theorem gm, all three routes).
- Rankings that add up are nearly excluded there (D1: no ties at p*). The branch E ≠ ∅ with p* ∉ E is open.
- Gauge-mixture covers (R10a Thm M) of polygons arbitrarily close to T1 exist on two-sided domains. They degenerate in the limit only because the (LF) margin is O(a).

**3. Weak fields were never tested.**
- K3.1 classification: a world with no finite certificate either has a localizable endorser or a non-null blind set Λ_∞, on which every endorser's countably additive part vanishes.
- K3.7: Λ_∞ is rigid. On each edge region it is the error set of a coherent model between P₁ and P_j.
- K3 referee: the step of M0closed(a) that fails for such a "weakly signed" field is exactly the one about chart lines through the vertex e₁ for atoms in Λ.
- **So Question Q_A is concrete additive geometry:** does M0closed(a) hold for fields with one weakly signed component?

## Read first
- BRIEF13.md (rules).
- Write-up §§2–3, §4 (corner equation and box), §5 ((TS), walls, CF(T)), §6 (Theorem gm and routes I1/I2/C2), §7 (Prop M0, Theorem M0closed, Theorem kkm), §8.5 (all, including (f″) and (g)).
- Notes: K3_notes.md, K3_referee.md, K2_notes.md, K2_referee.md, K1_notes.md, K1_referee.md, H1_notes.md, D2_notes.md, F1_notes.md, Q12_referee.md (the tilted world), R10a_notes.md (Thm M gauge mixtures), B2_notes.md, D1_notes.md (+ referees), P3_notes.md (exact consistency test with R5).

## RULES
- As in BRIEF13. A construction counts only when every axiom is verified, including closed sections for EVERY evaluable model, (C), (LF) at T1, and T1 ∈ C_L.
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Add no assumptions.
- Write only your own note, plus scripts in a subfolder named after it, in this folder.
- Deliver a construction, a theorem, or one precise single obstruction. Do not deliver lists.
