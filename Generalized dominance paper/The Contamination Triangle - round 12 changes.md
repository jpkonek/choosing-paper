# Changes, round 12 (15 Oct 2026)

Backup of the round-11 file: `The Contamination Triangle (pre-round12).tex` (1748 lines). The new file has 2047 lines
and compiles cleanly with `latexmk -pdf` (90 pages). There are no errors, no undefined or multiply defined
references and no overfull boxes; the only remaining warnings are a few underfull boxes. Line numbers refer to the
**new** file unless marked "old".

Conventions followed:
- no theorem names inside theorem environments;
- `\coloneqq` throughout;
- new terms are defined in plain words;
- every new statement carries a `\status{...}` line with its source and referee status (`\src{}`);
- where a referee repaired a note, the referee's version is used.

The terminology check (`grep -niE 'menu|forced[- ]silen|accept-or-silence|available action|forced acceptance|forced advice'`)
finds only line 212. That is the pre-existing "Earlier terminology" paragraph, which is allowed.

## 1. CPaU: Remark promoted to Corollary (sources: CPaU_referee.md §§1–9)

| Lines (new) | Change | Source |
|---|---|---|
| 1410–1427 (old 1391–1394) | Remark `rem:CPaU` replaced by **Corollary `cor:CPaU`**. A preamble defines the field c^P_i(g) := ρ_{P_i}(ḡ)(λ_i(ḡ,0) − λ_i(ḡ,a_g)) on U (R1). (a) is the statement with all the axioms (R4) and the scope: any bounded strictly rank-increasing λ_i, any weak-* closed convex set of null-invariant states, complete or not, purely finitely additive and atomic parts allowed. (b) excludes mixed systems in which each world is (CP-a) or adds up (Route B, R8). Proof of (a): P exists by Thm fullsupport (R2); strict signs of c^P; the translation of Thm integral (a), (c) into the hypotheses of thm:M0closed(a), via pointwise minimisers and E(P) = E(c^P) (R3); the statement that it does not pass through (U) and tolerates E(P) ≠ ∅ (R5). Proof of (b): Route B (CP-a ⇒ adds up on M_U). Status (R7): (a) proved; glue read once; inputs listed with their statuses; the "not used" list; subsumes Cors complete and DCA on M_U; scope CHECKED for every K′ and every all-facing triangle; "not established" list. (b) proved in a referee report, one reader. | CPaU_referee §§1–3, 5, 6, 8 |
| 1229 (old 1209–1210) | **LaTeX bug fixed.** `Remark~` + newline + `ef{rem:CPaU}` (the `\r` had been read as a line break) is replaced. The status of Conj U is rewritten with the corrected logic: open off M_U; on M_U the hypothesis is never met, so Conj U and Cor residual are vacuous there; the proved content is the equivalent form "no (CP-a) ranking covers T1"; (U) itself is a property of a system and is **not** shown. | CPaU_referee R5, R6, §4 |
| 1216 (old 1196) | rem:EPchords now says that thm:M0closed(a) applies to the strictly signed field c^P (R1) and cites the Corollary. It adds that "(U) fails exactly when …" and Prop Ucont are vacuous on M_U under (H), and that their content survives for systems without the coverage clause (R9). That last reading is the referee's and is marked as not re-checked step by step. | CPaU_referee §4, R9 |
| 66 (old 66) | Intro item 3 is reordered as the referee proposed: on M_U no (CP-a) ranking covers T1 (Cor CPaU, proved, glue refereed once); every (CP-a) world adds up; mixed systems are excluded; the other non-adjacent domains and (U) follow. The "CHECKED, not refereed" wording is dropped. | CPaU_referee §9 |
| 108–109 (old 106–107) | Status-table rows 106 and 107: "on M_U superseded by Cor CPaU"; Conj U "open on non-adjacent domains other than M_U; on M_U its hypothesis is never met". | CPaU_referee §9 |
| 122–123 (old 120) | The row is now bold: "No (CP-a) ranking covers T1 on M_U" (proved; glue refereed once; inputs). New row for Cor CPaU(b) (Route B). | CPaU_referee §9 |
| 1510 (old 1477) | §8.1 Q1 answer: "(Remark CPaU, CHECKED)" → "(Corollary CPaU, proved; glue refereed once)". | CPaU_referee §9 |
| 1520 (old 1487) | "The remaining target", first bullet: cross-reference to Route B (Cor CPaU(b)). | CPaU_referee §6, §9 |
| 1571 (old 1537) | §8.3 bullet "Rankings that do not add up": Remark → Corollary; adds a pointer to §8.5 and the narrowing under edge nestedness. | CPaU_referee §9; Q3_referee |

The list of what remains open for (CP-a) is in the Cor CPaU status and the Conj U status: (U) off M_U; (CP-a) on
general decomposable domains; the Walley-2000 variant with invisible desirability. Conj U now stays open only off
M_U.

## 2. New subsection §8.5 "Worlds that do not add up: the two-world core" (lines 1707–1964)

The subsection is inserted after §8.4 "Building ordinal rankings directly" and before "Other targets and more worlds"
(old 1673). Label `sec:open-core`.

| Lines | Content | Source / status recorded |
|---|---|---|
| 1707–1710 | Opening paragraph: the BRIEF11 question; no construction and no exclusion; list of sources. Notation paragraph: σ_i, P_i, M, N₊, the N9.4 order ≤_i, shadows, e_ij, R_ij, standing hypotheses (H_U). | BRIEF11; N9 |
| 1712–1721 | **(a)** Definition of ν^L and Q_L. **Prop Q31** (Q3 Lemma 2.1 + Prop Q3.1), the locality barrier, with the referee's precise meaning: an exclusion must use selection indices contained in no compact subset of Δ°. Global consequences of (S) count as using all indices. The "model space" extension is marked heuristic and not claimed. | Q3 §2; Q3_referee §1 (CONFIRMED, reading repaired) |
| 1723–1734 | **Prop Q32** (Q3.2 repaired: "at least one", integrable densities; plus Q3.3 for ν^L). Its status records: N17 Conj 5.2 false in its index reading (its model-space half is forced); the shadow-weight vs selection-index wording repair; and that Q3's "premise of P2.6 not forced" and "load-bearing reversals near T1 are not forced" are **WRONG**. | Q3 §3; Q3_referee §§2.1–2.3 |
| 1736–1750 | Definition of 𝒩_i. **Theorem R3** (the referee's corrected statement), with a proof sketch (bathtub closure, Prop R2 construction). Status: proved in a referee report, one reader; it replaces Q3 §6 item 3; the open point is the position of the dominators. | Q3_referee §2.4 |
| 1751–1757 | (LC_T1) defined. **Prop Q38** (Q3.8) with the wording repair: ¬(LC_T1) is a generalised (moving-dominator) form of (γ), not a sharpened one; this answers P2P3_referee §B6's "far" objection. | Q3 §5; Q3_referee §6 |
| 1758–1762 | Tie toggles. **Lemma Q39** (Q3.9) with repairs: finite unions only; Dynkin-type needs (c); (LC_T1) needed at every world for the N17.7 application. | Q3 §5; Q3_referee §6 |
| 1764–1774 | **(b)** **Lemma Q34** (edge complementarity: a.e. correct at i or j; complementary error sets on R_ij; edge test models), with proof. | Q3 Lemma Q3.4 = Q1 Lemma Q1.7; Q3_referee §3 |
| 1775–1788 | Definition of (Nest_e). **Prop Q35** (edge reduction: β, closed b-sections, (K), transfer of strict escape, DL, DR, Lemma T, E2, LF, IS, MP; E3 fineness step). Status: Q1.8 upgraded to PROVED; corrected form of Conj Q2.E; Q1.10 recorded; Lemma T stated in words. | Q3 Prop Q3.5; Q1 Prop Q1.8; Q3_referee §§4.1, 4.3, 8 |
| 1789–1802 | Leading charge on M defined. **Theorem Q36** (three-world transfer, any n ≥ 2; the linking step through R_ij ∩ R_ik). (c) is CHECKED (Savage). Status notes that positivity of edge comparisons does not globalise for general cones. | Q3 Thm Q3.6; Q1 Thm Q1.9; Q3_referee §4.2 |
| 1804–1810 | **Corollary Q37** with proof. Status: proved at the status of Thm M0closed(b), CHECKED with a complete world (E3 via Savage); the all-CP-a case is Cor CPaU; the contrapositive (E-a)/(E-b). | Q3 Cor Q3.7, §6 item 4; Q3_referee §5 |
| 1812–1822 | Remarks on (Nest_e). **Prop comonotone**, the referee's characterisation: on the edge models co(K′ ∪ [x,y]), (Nest_e) holds iff the endpoints are comonotone. | Q3_referee §4.4 (proved there, one reader) |
| 1824–1825 | **(c)** setting ((Nest) and (C)), cut pairs, 𝒱₁, 𝒱₂ (endorsing charges), μ̄; the drop lemmas DL and DR stated. | Q2 §1; P4B_referee §8.1 |
| 1826–1830 | **Lemma cutform** (Q1.0). | Q1 §1; Q12_referee §1.1 |
| 1831 | Symmetry; **Lemma T₂**; b₀(Z). | Q2 §1; Q12_referee §0 |
| 1833–1841 | **Theorem LF** (left-fineness) and its uniform form, with proof. | Q2 Thm LF; Q12_referee §2.1 |
| 1843–1851 | **Corollary IS** (null sets are initial segments), (i)–(iv), with the referee's precision (left mass at a\*). | Q2 Cor IS; Q12_referee §2.2 |
| 1853–1866 | Simple certificates defined. **Prop MP** in its sharp form: (a) needs no overlap; overlap is used only in the final step (b). Status records that this is also **Q1.4 corrected** (d_{1−h} ≤₂ A_j, not "≤₂ P_j"; summability superfluous and insufficient). | Q2 Prop MP; Q1 Thm Q1.4; Q12_referee §§1.4, 2.3, 3 |
| 1868–1876 | **Cor MP-loop**; **Cor MP′** (complete clause CHECKED). | Q2; Q12_referee §2.3 |
| 1878–1881 | **Prop NS** (repaired: b₀ = b₀(Z) explicit; t = b₀ in range); the N17.8 architecture is excluded; consistency with MP and with Prop Q13. | Q2 Prop NS; Q12_referee §2.3 |
| 1883–1886 | **Prop Q15** (Q1.5, Q1.6: no simple certificate next to an SP world; with a uniformly absolutely continuous partner, no vanishing-measure targets and no star certificates). | Q1 Cors Q1.5, Q1.6; Q12_referee §1.4 |
| 1888–1896 | **Prop N1** (MP sharp form; Cesàro-thin ⇔ simple, via Sion; the modulus next to an SP world). | Q12_referee §4 N1 (one reader) |
| 1898–1901 | **Prop N2** (closure of a mirrored pair: favourable-direction acceptance by both worlds; no contradiction from (U), (C), (K); a proof must use closedness quantitatively). | Q12_referee §4 N2 (one reader) |
| 1903 | "Shape of a surviving certificate": Q2 §4.1 (a)–(f) with the repaired wording of (b) (η(P,x) has no lower bound uniform in P), and §4.2(ii) (charges at 1⁻; a\* = 1 not excluded). | Q2 §§4.1–4.2; Q12_referee §2.4 |
| 1905 | "Ratio certificates" (N4). | Q12_referee §4 N4 |
| 1907–1928 | **(d)** **Prop lattice** (coherent error sets {σ < α} ∪ {τ ≤ β}); 1-D KKM; **Lemma G-SE**, whose status records what breaks without nestedness and the repair to Q2 §6 (interior vs edges); **Conjecture Q2N**. | Q2 §§5–6; Q12_referee §2.5; Q3_referee §4.3 |
| 1930–1946 | **(e)** The band-plus-exotic-cones construction. **Prop Q12** (Q1.1 + Q1.2) with the **referee's repair**: Fact 0 cannot be cited because the world-1 sections are not closed; the conclusion survives by the direct argument with b₂ = μ̄(A) − μ̄(N), clipped. **Prop Q13** (Q1.3) stated **exactly**: the section is [0, 0.5) in the dyadic family (a = 0.3, d = h = 0.1), with the referee's exact numerics. "Other designs": Q1 §§4–5 failure reports and the N3 exponential-tilt world. | Q1 §§2, 4, 5; Q12_referee §§1.2, 1.3, 4 N3 |
| 1948–1964 | **(f)** The precise remaining question (R1)–(R4), stated as in Q12_referee §6, with (R4) extended to (Nest_e) and comonotone endpoints; the constraints on any example. "How a positive two-world answer would lift to T1": (R4)-edge removes (Nest_e) from Thm Q36 and Cor Q37; N17.B′(2) applies on each R_ij but globalises only for leading charges and Savage measures, otherwise the interior step (Q1.C5) is needed; then case (i) of Thm R3 must be excluded, after which Prop Q38 applies. | Q12_referee §6; Q3_referee §§7–8; Q1 §6 |

## 3. Corrections elsewhere (§8.1, §8.3, §8.4(c))

| Lines | Change | Source |
|---|---|---|
| 1705 (old 1671) | **§8.4(c) "Three worlds" corrected.** "Nothing in the two-world results transfers as it stands" now applies only to comparisons out of *interior* selected models. An explicit "Correction (round 12)" says that on edges complementarity is automatic and the results transfer under (Nest_e). Status updated. | Q1 §5.2; Q3 §4; Q3_referee §§4.1–4.3 |
| 1507 (old 1474) | §8.1: pointer to §8.5 added. | — |
| 1522–1525 (old 1489–1491) | §8.1 "The remaining target". The two-world bullet adds initial segments and mirrored certificates. A new bullet covers the three-world restrictions under edge nestedness and Thm R3. The final paragraph is corrected (the old "strict escape needs a complementary world …, which crossing error sets do not supply" was too strong) and ends with the requested **Summary**: every ranking class examined is excluded except worlds that fail to add up; the decisive remaining problem is the two-world question (R1)–(R4) plus edge nestedness, with the two further steps named. | brief item 3; Q3_referee; Q12_referee §6 |

## 4. Introduction, date, status table, sources

| Lines | Change |
|---|---|
| 42 | Date "15 October 2026 (round 12)". |
| 69 | New intro item "Worlds that do not add up: the two-world core" (§8.5). |
| 73 | New paragraph "Summary for T1 on the U-domain" (brief item 3). It is worded so as not to overstate: for worlds outside the complete and leading-charge classes, a positive two-world answer controls only edge comparisons, and the interior step and Thm R3(i) remain. |
| 144–161 (old 141) | 17 new status rows for §8.5. The N17.B′ row is updated: "open; reduced to (R1)–(R4), edge nestedness, and the interior step". |
| 1999 | Sources: BRIEF11.md. |
| 2035–2040 | Sources: CPaU_referee.md, Q1_notes.md, Q2_notes.md, Q3_notes.md, Q3_referee.md, Q12_referee.md. |

## 5. Points for the author

1. **Cor CPaU (b) (Route B)** has had one reader (CPaU_referee §6), and the R9 reading in rem:EPchords is also the
   referee's alone. Both are labelled as such.
2. **Theorem R3, Prop comonotone and N1–N4** were proved in referee reports and have had one reader each.
3. **Q3's "load-bearing reversals near T1 are not forced" is recorded as WRONG**, following Q3_referee §2.3.
   Prop Q38 and Lemma Q39 are now read as acting on case (ii) of Theorem R3.
4. **The "Summary" deliberately names two further steps** beyond (R1)–(R4) and edge nestedness: the passage from
   edge comparisons to interior ones for general acceptance cones (Q1.C5), and case (i) of Theorem R3. The brief
   asked to call the remaining problem "a two-world question plus edge nestedness". That is accurate for complete and
   leading-charge worlds, but saying it without the caveat would overstate (Q3_referee §4.3: edge positivity does not
   globalise for general cones).
5. **A file was written outside the permitted location.** During editing, a scratch copy of the new §8.5 block was
   written to `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r12_block_core.tex`. That
   is outside `writeup/`. It was not deleted, per instructions, and can be removed.
