# Changes, round 13 (15 Oct 2026)

Backup of the round-12 file: `The Contamination Triangle (pre-round13).tex` (2047 lines). The new file has 2376 lines
and compiles cleanly with `latexmk -pdf` (110 pages). There are no errors, no undefined or multiply defined references
and no overfull boxes; the only warnings are a few underfull boxes. Line numbers refer to the **new** file unless marked
"old".

Conventions followed:
- no theorem names inside theorem environments (names such as "Level Lemma", "parallelogram lemma" and "packing lemma"
  appear only in status lines, as source names);
- `\coloneqq` throughout (and `\eqqcolon` where the defined symbol is on the right); no `:=`;
- new terms are defined in plain words: generic level, double ties, splices, segment pair, pattern, rigid crossing,
  tied crossing, monotone continuity (MC_i), (MC_sel)_1, (MC_sel)_2, edge family, (EU_ij), nested edge family,
  straightening, concentrates at x, doubly-light sequence, t_Z, η₁(Z,1), κ₁, κ₂, (QC₁), (QC₂), (R1′), uniform escape,
  right-packing, bounded splices;
- every new statement carries a `\status{...}` line with its source (`\src{}`) and referee status;
- where a referee repaired a note, the referee's version is used;
- the existing qualifications are kept: the finer edge results under (Nest_e) concern comparisons between subsets of a
  single R_ij, and nothing transfers automatically to comparisons out of interior selected models (§8.1 bullet,
  line 1543; Q36 status; Remark straighten; lift paragraph, lines 2278–2283).

Notation renamed to avoid clashes (the content is unchanged): S4's τ(Z) is written t_Z (τ is the M⁺ coordinate of
part (d)); S4's S(t) is written T*(t); S1's quotient 𝓛 and map π are written 𝔏 and ϖ (π is the leading charge).

The terminology check (`grep -niE 'menu|forced[- ]silen|accept-or-silence|available action|forced acceptance|forced advice'`)
finds only line 231, the pre-existing "Earlier terminology" paragraph, which is allowed.

## 1. S2.1: leading charges without nestedness, and its consequences (item 1)

| Lines (new) | Change | Source |
|---|---|---|
| 1810–1818 (inserted before old 1790) | Lead-in paragraph, then **Theorem `thm:S21`** (any n ≥ 2, M_U, K′ ⊆ Δ°; strict (G), (IB), (S); a leading charge is 0 on M or strictly positive on every non-null subset of M; then ρ > 0 a.e., endorsement, SP^reg_i; no nestedness). Proof sketch with the referee's simplifications (small sets by splitting, no carrier lemma; one generic index), and linking for n ≥ 3. Status: two readers; inputs and "not used" list; consistency with the locality barrier and with B2, N26.1, B3. | S2 §4; S2_referee §1 |
| 1820–1827 | **Corollary `cor:S21`**: (a) Thm E2 and its lexicographic clause (E2′) without (Nest), (K) or the chain; (b) Prop B2(b) restated without chain coordinates (B2(b′)); (c) the referee's observation on Thm LX's class (primary zero a.e. on M or nowhere). | S2 Cor S2.1′(a); S2_referee §§2.1, 2.2, 2.5 |
| 1829–1841 (old 1790–1802) | **Theorem `thm:Q36` restated.** (a), (b) now without (Nest_e); (c) (complete worlds) and (d) (strict escape, Lemma T on R_ij) keep (Nest_e) as explicit hypotheses. The proof of (a) cites Thm S21 and keeps the old proof as the (Nest_e) case. Status: the old version is recorded as the special case; (c), (d) may use any nested edge family (Remark straighten). | S2 Cor S2.1′(b); S2_referee §2.3; S1_referee §6 |
| 1843–1851 (old 1804–1810) | **Corollary `cor:Q37` restated**: every world is (CP-a), or has a leading charge nonzero on M, or is complete and edge-nested. Proof updated. Status: adds Thm S21; the old version is the special case; the contrapositive (E-a′)/(E-b′) replaces (E-a)/(E-b). | S2 Cor S2.1′(c); S2_referee §2.4 |
| 1704 (old 1684) | Thm E2 status: "Round 13: (Nest) is not needed …; the statement under (Nest) is the special case." | S2_referee §§1, 2.1 |
| 1721 (old 1701) | Prop B2 status: (b) holds without nesting, in the chain-free form Cor S21(b). | S2_referee §2.2 |
| 1661 (old 1641) | Thm LX status: the class is narrower (pointer to Cor S21(c)). | S2_referee §2.5 |
| 1723 (old 1703) | "Precise open class in two worlds": leading-charge clause needs no (Nest); a leading-charge or monotonely continuous partner makes (Nest) automatic. | S2_referee §§2.1, 3.4; S1_referee §5 |
| 1725 (old 1705) | Three-world status sentence: N17.B′ proved for leading-charge worlds with no nestedness; complete worlds CHECKED under edge nestedness. | S2_referee §7 item 10 |

## 2. S2.2 and Lemma PL (item 2)

| Lines (new) | Change | Source |
|---|---|---|
| 1853–1856 | **Lemma `lem:PL`** (parallelogram lemma, any n) with the referee's repair: X′ ∈ C_L from F ∈ C_L; X ∈ C_L only if also C ∈ C_L. NUMERICS of both scripts. | S2 §3; S2_referee §3.1 |
| 2105–2113 | Lead-in "Round 13: nestedness in two worlds"; **Theorem `thm:S22`** (n = 2, every axiom, a nonzero leading charge at either world ⇒ C_L is a chain, members fixed by π-level, (Nest) holds). Proof sketch (generic levels, bounded balanced exchange, PL, fans collapse). Status: confirmed; consequence that all of part (c) applies unconditionally in the leading-charge class (Prop Q15 example); cross-agreement as a special case; recorded failures; S2's half-vanishing "anatomy" not cited. | S2 Thm S2.2, §§3, 5; S2_referee §§3.2, 3.4, 6 |

## 3. The tie remark, S2.0 and Prop R-S2.A (item 3)

| Lines (new) | Change | Source |
|---|---|---|
| 1858 (old 1812) | The sentence that (Nest_e) "can fail at exceptional edge weights where a non-null tie set is split in crossing ways" is **replaced** by the referee's corrected text (§4.4), with its scope restriction (n = 3: integral penalties only), pointers to Prop plateau and Prop R7.1, and a marked correction note. | S2 §2; S2_referee §4.4 |
| 1860–1870 | **Proposition `prop:S20`**: (a) on one edge or n = 2, additive Bayes error sets are nested for every tie-break (wording repair: not "any n", not "strictly"); (b) n = 2, every axiom ⇒ null tie sets at interior weights. Proof sketch and status. | S2 S2.0(a), (b); S2_referee §4.1 |
| 1872–1883 | **Proposition `prop:RS2A`** (n = 3; strict (G), (IB), (S), (C); edge worlds additive with integral penalties): (a) complete third world ⇒ (Nest_e) on e_ij, all-additive case included; (b) crossings need incomparability at k for every bounded balanced exchange; (c) proportionality and sign conditions when world k has a leading charge. Proof by bounded splices + PL. Status: repaired S2.0(c) (GAP in the Lyapunov half-splice) as special case; NUMERICS fan_search; S2.4 item 5 strengthened; S2.4 items 2–4 GAP noted. | S2 S2.0(c), S2.4; S2_referee §§4.2, 4.3, 5 |
| 1885 | "On a natural family … comonotonicity" sentence kept as the lead-in to Prop comonotone. | (unchanged content) |

## 4. S1 (item 4)

| Lines (new) | Change | Source |
|---|---|---|
| 1895 (old 1822) | Prop comonotone status: round-13 pointers (edge inputs do not force it; nor Q35's hypotheses without (C); proved in the R-S2.A cases; pairwise straightening). | S1 §5.7; S1_referee §§7, 8; S2_referee §4.3 |
| 1897–1900 | **Remark `rem:straighten`** (S1.8 as repaired): Q35(1)–(5), Q36(c), (d) and Q37's complete clause need only a nested edge family with (K) and closed sections; straightening is the right target; after S2.1 its payoff is Q36(c); relevant-comparison reading of LF/IS/MP needs (i,j)-ties with C_L. | S1 Remark S1.8; S1_referee §6 |
| 1902–1905 | **Proposition `prop:plateau`** (Example S1.9): the edge inputs do not force (Nest_e); status with the referee's caveats. | S1 Example S1.9; S1_referee §7 |
| 2103 (old 1923) | Lemma GSE status: pointers to strict escape without nestedness and to the two chain criteria. | S1 Cor S1.2(d); S1_referee §2 |
| 2115–2121 | **Lemma `lem:level`** (Level Lemma S1.1, with the referee's strengthening: a selected C_q tied with both). | S1 Lemma S1.1; S1_referee §1 |
| 2123–2132 | **Corollary `cor:continuum`** (S1.2 (a)–(d); (e) inclusion closedness in the status). | S1 Cor S1.2; S1_referee §2 |
| 2134–2137 | **Proposition `prop:S13`** (nested selection ⟺ nested class representatives). | S1 Prop S1.3; S1_referee §2 |
| 2139–2144 | Definitions (crossing, splices, segment pair, pattern, rigid/tied crossing) and **Lemma `lem:rigid`** (S1.4/S1.5 strengthened: only (<,<), (>,>), (~,~), and (~,~) only at the corner pairs). | S1 Lemma S1.4, Thm S1.5; S1_referee §3 (S1.5(ii)′) |
| 2146–2154 | Definition of (MC_i) and of the two halves of (MC_sel); **Theorem `thm:MC`** (S1.6′: either half alone forces a chain), proof sketch from (MC_sel)₁; status with the repair of S1.6, clause equivalence (R4.1), and the repaired "necessary shape". | S1 Thm S1.6, §4; S1_referee §§4.1–4.3, 5 |
| 2156–2163 | **Corollary `cor:MC`**: (a) additive and countably additive (CP-a) worlds are monotonely continuous (S1.7); (b) the **combined two-world statement**: a non-nested system needs both worlds to fail monotone continuity and to lack a nonzero leading charge. Independence of the two criteria noted. | S1 Cor S1.7; S1_referee §§5, 10; S2 S2.3 |
| 2165–2171 | **Proposition `prop:R71`**: the referee's full two-world ranking on M_U with strict (G), (IB), (LA), (S) and a crossing coherent undominated selection; only (C) fails, so (C) is what must force nestedness. | S1_referee §7 |
| 2173–2176 (old 1925–1928) | Conj Q2N kept; status extended: proved in the leading-charge and (MC_sel) classes, open only when both worlds lack both, (C) necessary, Prop S13 consequence, failed lattice-join route consistent with rigid crossings, reduced form. | S1 §§3–4, 6; S1_referee §§9, 11; S2_referee §7 |
| 2178–2181 | **Conjecture `conj:S1R`** (S1.R as reduced to one half of (MC_sel) at the crossing pair), with "where the proof stops". | S1 Conj S1.R, §4; S1_referee §9 |
| 2183–2209 | "Edges in three worlds": edge family; **Lemma `lem:weakedge`** (S1.10); definition of (EU_ij) and its additive case; **Prop `prop:S111`** (S1.11, conditional; referee's added step; "only non-nested possibility not excluded"); **Prop `prop:S112`** (S1.12, pairwise straightening, coherent on D_{M_{x,y}}); **Conjecture `conj:S113`** (global straightening; payoff Q36(c); where the maximal-chain argument stops, with the referee's filled gap). | S1 §5; S1_referee §§8–10 |

## 5. S3 and S4 (item 5)

| Lines (new) | Change | Source |
|---|---|---|
| 1990–2003 | "Round 13: rates …": definitions of φ₂, concentration, (SR_i), (R3_i), (R3_i^u), doubly-light sequence; **Theorem `thm:RATE`** with proof sketch; status (inputs; duality with mirrored pairs; §2.4 rider marked heuristic; rates per system). | S4 Thm RATE, §2; S34_referee §6 |
| 2005–2008 | **Conjecture `conj:NDL`** (S4.1: no doubly-light sequences; the restated (R3); linear form false). | S4 Conj S4.1; S34_referee §§10.1, 12 |
| 2010–2016 | **Corollary `cor:SR`** with proof sketch; status (scope; does not imply (R2)). | S4 Cor SR; S34_referee §7 |
| 2018–2033 | Definitions t_Z, η₁(Z,1), κ₁, κ₂, 𝒰₂; **Proposition `prop:MPsharp`** (MP♯ (a)–(c); (d) with the **repaired bounds** ν(d_{t_Z}) ≤ inf ≤ lim_{t↑t_Z}; (e) the referee identity η₁ = 1 − t_Z and κ₁ = η₁ next to μ̄); proof; status ((W-a) with repaired modulus; N1(c) sharpened). | S4 Prop MP♯, §5.4; S34_referee §§8.1, 10.1 |
| 2035–2044 | **Lemma `lem:loop`** (repaired: (a) c_s ≤₁ d_t or d_t ≤₂ c_s for all s, t; (b) the inclusions and T*(t) ≤ s); status records the gap (t ∈ (T(s), s] occurs in Example A). | S4 Loop lemma; S34_referee §8.2 |
| 2046–2049 | **Lemma `lem:block`** and the **blocking effect** (world-2 half of a mirrored pair satisfies (K) by itself); S4 §5.2 reading corrected; S4 §5.1 relabelled as an observation (GAP, overlabelled). | S34_referee §§10.1, 10.2; S4 §5 |
| 2051–2064 | Definitions (QC₁), (QC₂), (R1′); **Proposition `prop:QCJ`** (the referee's equivalence; inequalities; QC ⇒ no mirrored pair; ¬QC mirrored and weaker than R1); **Conjecture `conj:QC`** (S3.C1) with evidence. Wording "a priori stronger". | S3 §6; S34_referee §5 |
| 2066–2069 | **Lemma `lem:UE`** with its consequences (inconclusive, thin residue). | S4 Lemma UE, §5.3; S34_referee §10.1 |
| 2071–2077 | **Proposition `prop:ExA`** (Example A: every axiom, both worlds additive, η₁(P_m,1) ≤ m²/2; variants with the referee's "any q > 1"). | S4 Example A; S34_referee §9.1 |
| 2079–2085 | **Proposition `prop:LIN`** (stated for world 2 = μ̄, as repaired; general ν₂ noted in status). | S4 Prop LIN; S34_referee §9.2 |
| 1969 (old 1886) | Prop Q15 status: the "both worlds non-additive" gloss restricted to the Q15 types and now holds without (Nest). | S1_referee §5; S2_referee §3.4 |
| 1979 (old 1896) | Prop N1 status: modulus sharpened by MP♯. | S4 §3.2; S34_referee §8.1 |
| 1984 (old 1901) | Prop N2 status: the "rate in Lemma T" reading qualified; Loop lemma, blocking lemma and Prop S31 cited. | S34_referee §§8.2, 9.3, 10.2; S3 §2 |
| 2227 (old 1946) | "Other designs": the ping-pong is now realised without closed sections at both worlds. | S3 Prop S3.1 |
| 2229–2265 | "Round 13: mirrored pairs from the construction side": mirrored world-2 definitions; **Prop `prop:S31`** (S3.1, with the referee's simpler witness of non-closed sections, wording repair "C_L is the chain"); **Prop `prop:S32`** (S3.2 as repaired: half-open also when inf > 0 not attained; inf > 0 rather than min; **necessary, not sufficient**, with the referee's counterexample; compact profiles impossible for thin families); **Prop `prop:S33`** (packing lemma, with the b ≤ s case); **Prop `prop:S34`** (fibrewise route fails (K), general form; other designs as failure reports). | S3 §§2–5; S34_referee §§1–4 |

## 6. Part (f) corrections (item 6)

| Lines (new) | Change | Source |
|---|---|---|
| 2271 (old 1950) | (R1) restated: initial-segment form, MP♯ consequence, Loop lemma, S3.1; **weaker target (R1′) = ¬QC**; known constraints on a construction; what any exclusion must obtain. | S34_referee §12; S3; S4 |
| 2272 (old 1951) | (R2): round-13 sentence (qualitative rate available; linear rate needed and not a consequence of the axioms). | S34_referee §12; S4 §4 |
| 2273 (old 1952) | **(R3) replaced** by the referee's corrected text (§9.3). Deleted: "the missing lemma common to (R1) and (R2)", "This would give Q1.C1", and the Vitali clause; a marked correction note explains why. (R3) is restated as Conjecture NDL (S4.1); the linear form is false. | S4 §4.3; S34_referee §§9.3, 12 |
| 2274 (old 1953) | **(R4) updated**: true when one world has a leading charge or is monotonely continuous; open only when both lack both; (C) necessary; reduced form; strict escape survives; edge form: R-S2.A cases, not implied by edge inputs, straightening (pairwise proved, global conjectured); after S2.1 relevant only to complete worlds and general cones. | S1, S2; S1_referee §11; S2_referee §7 |
| 2276 (old 1955) | Closing paragraph: the Q13 "compact family of target profiles" clause replaced by the referee's text (closed world-1 sections force inf μ̄(F) > 0, hence (QC) and no mirrored pair), with a correction note. | S34_referee §9.3 |
| 2278–2283 (old 1957–1962) | **Lift paragraph**: any nested edge family will do; first bullet rewritten (leading-charge worlds no longer need (Nest_e); complete worlds still do, so (R4)/straightening would remove it from Q36(c) and Q37's complete clause); second bullet notes leading charges without (Nest_e). | S2 Cor S2.1′(d); S1_referee §6 |
| 2284 (old 1963) | Status line of (f) rewritten for the new state of (R1)–(R4). | S1_referee §11; S2_referee §7; S34_referee §12 |

## 7. Introduction, §8.1, §8.3, §8.5 lead-in, status table (item 7)

| Lines (new) | Change | Source |
|---|---|---|
| 42 | Date line: round 13. | — |
| 68 (old 68) | Intro item "Building ordinal rankings directly": leading-charge clause no longer needs nesting. | S2 |
| 69 (old 69) | Intro item for §8.5 rewritten: round-13 results (Thm S21 and the new Cor Q37; S22 and MC; R7.1; RATE/SR and Example A; S3.1). | S1–S4 and referees |
| 73 (old 73) | "Summary for T₁": leading-charge worlds excluded outright; complete worlds when edge-nested; remaining problem (R1), (R2), (R4), Conj NDL, edge nestedness or straightening for complete worlds. | S2_referee §7; S34_referee §12 |
| 1541–1545 (old 1522–1525) | §8.1 "The remaining target": new bullet (no leading charge, unconditionally); two-world bullet (automatic nesting next to a leading-charge or monotonely continuous world); three-world bullet now only adds incompleteness under (Nest_e); the qualification about interior comparisons kept, adjusted to "none of these finer restrictions transfers" (line 1543); "precise target" and "Summary" sentences updated. | S2_referee §2.4; S1_referee §10 |
| 1591 (old 1571) | §8.3 "Rankings that do not add up" status: narrowed in two worlds also by §8.5(d); in three worlds for leading charges unconditionally. | S2 |
| 1728 (old 1708) | §8.5 opening paragraph: round-13 summary and sources. | BRIEF12; S1–S4; referees |
| 141, 143, 150, 153, 180 (old 141, 143, 150, 151, 161) | Rows updated: Thm E2 (no (Nest) needed), Prop B2 (chain-free form), Thm Q36 (new form), Cor Q37 (new form, bold), N17.B′ (new reduction). | S2_referee; S34_referee |
| 151–152, 155–156, 163–171, 173–179 | New rows: Thm S21/Cor S21 (bold); Lemma PL; S20 and R-S2.A; Remark straighten and Prop plateau; Thm S22; Level Lemma/continuum/S13; Lemma rigid; Thm MC/Cor MC; Prop R71; Conj Q2N row extended; Conj S1R; edge results S1.10–S1.12; Conj S113; Prop S31; Props S32–S34; RATE/SR; Conj NDL; MP♯/loop/block/UE; QC-J/Conj QC; Example A/LIN. | as in §§1–5 |

## 8. Sources (item 8)

| Lines (new) | Change |
|---|---|
| 2321 | New entry BRIEF12.md. |
| 2363–2369 | New entries S1_notes.md, S1_referee.md, S2_notes.md, S2_referee.md, S3_notes.md, S4_notes.md, S34_referee.md. |

## Not incorporated, and why

- S2 §5(c) "forced anatomy" of a half-vanishing leading charge: superseded by Thm S21 and not re-checked
  (S2_referee §6); mentioned only as not cited.
- S2.4 items 2–4 (fans): derived only for additive edge worlds; item 4 is a GAP (heuristic). Only item 5 (strengthened)
  is stated, inside the status of Prop R-S2.A.
- S4 §6 (pointer to fibre-direction non-additive worlds): heuristic, not claimed; not reproduced.
- S3 §5 other designs: failure reports; recorded in one sentence of the Prop S34 status.
