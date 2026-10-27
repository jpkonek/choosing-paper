# Changes, rounds 14–15 (15 Oct 2026)

Backup of the round-13 file: `The Contamination Triangle pre-round14.tex` (2376 lines, a copy). The new file has 2738
lines. It compiles cleanly with `pdflatex` run twice (131 pages, previously 110). There are no errors, no undefined or
multiply defined references and no overfull boxes; the only warnings are underfull boxes. Line numbers refer to the
**new** file.

## Conventions

- No theorem names inside theorem environments. Source names (B1.3, C2.1, …) appear only in status lines.
- `\coloneqq` throughout; there is no `:=`.
- Every new statement has a `\status{...}` line with its source (`\src{}`) and its referee status.
- Where a referee repaired a note, the referee's version is used.
- The terminology check (`grep -niE 'menu|forced[- ]silen|accept-or-silence|available action|forced acceptance|forced advice'`)
  finds only line 252, the existing "Earlier terminology" paragraph, which is allowed.
- No earlier result of the write-up was marked wrong by the referees of this round, so no dated correction notes were
  needed. The statements the referees marked wrong or overstated were in the notes:
  - the B1 §0 headline;
  - B1.5(a)'s strictness step;
  - B3's "complete worlds in a cover are non-AR", "equivalently", "excluded outright" and the B3.4 scope remark;
  - B2.R without (LF), B2 Remark 5.3 "shorter", and the B2 §0 audit sentence;
  - C1's "no third case" headline, C1.8's non-strict fineness, C1.9's "supports must cross", and C2.4/C2.5/C2.8 wording.

  None of these was adopted. Each is recorded in the relevant status line in the referee's corrected form.
- **C12_referee.md appeared during the integration** (16:10). Its verdicts replace the provisional label "proved in a
  note, not yet refereed" for every C1/C2 item. Everything is CORRECT, with the small repairs listed in §4 below.

## Notation (renamed to avoid clashes; content unchanged)

| In the notes | In the write-up | Reason |
|---|---|---|
| C1's K_1, K_2 | 𝒦_ij, 𝒦_ik ("link cones") | K is used for credal sets |
| C1's G | Γ^gl ("glued credal set") | clashes with (G) and with the atom G |
| C1's ⪯_G | ⪯_Γ | follows from the line above |
| C1's ⊏⊏ | ⊏ | — |
| B3's top level ⪯ | ⊴ | ⪯ is used for model comparisons |
| B3.4's constant c | θ | c_p are sets |
| B2's 𝒲 (tangent hexagon) | 𝓗_T | 𝒲 is used for the walls of Thm TSalways |
| B2's residual "(R2)" | "full-atom residual" | (R2) is an item of §8.5(g) |
| B2's Prop B2.0 | "Claim B2.0" | it is not proved |

- B3's "complete" (in the sense of a total preorder) is written **total**, as B3_referee §1 requires. In §2.6,
  "complete" means a singleton credal set.
- (LD) is defined in the text, as C2 uses it.

## 1. Front matter and introduction

| Line | Change | Source |
|---|---|---|
| 42 | Date: "(rounds 14–15)". | — |
| 69 | "What is shown", item on §8.5: appended a paragraph "New in rounds 14–15" (B1.3/B1.4, B3.2, B3.5/B3.6, C1.1/C1.6, C2.1, C2.3, B2.1, with referee status). | all notes and referee reports |
| 73 | **"Summary for T1" rewritten.** See the list after this table. | B1_referee, B3_referee, C12_referee, B2_referee |
| 150 (table) | Q36 row: "(a′) proved (B1 Thm B1.3; confirmed, B1 referee)". | B1_referee (iv) |
| 180–199 (table) | New block "Rounds 14–15" with 19 rows: B1.0–B1.3; the referee counterexample; B1.4; B1.5; B3.1/B3.2; B3.3; B3.4; B3.5–B3.7; B3.C/R3/B3.C′; C1.1/C1.4; C1.6; C1.7–C1.9; C2.1; C2.3/C2.5; C2.6/C2.7; B2.1; B2.2/Prop 13; the referee's field; the audit. | — |
| 200 (table) | N17.B′ row: now points to §8.5(g). The reduction list adds Conj B3.C, Question C1.Q, Conj C2.C, other edge orders without a leading density, and case (i) of Thm R3. | — |

The rewritten "Summary for T1" (line 73) states:

- **What is excluded.** Additive rankings; adding-up rankings; (CP-a) rankings; and rankings all of whose worlds are (CP-a), leading-charge, total and AR, or glued credal.
- **What a cover needs.** A world that does not add up, which
  - (i) is not (CP-a) and has no leading charge;
  - (ii) has no leading density on some edge region (countably additive only; finitely additive gluing open);
  - (iii) is not glued credal (and, if it leads a credal pair, is not total and has a finite obstruction);
  - (iv) if total, is not AR and has a non-nested edge family.
- **What remains.** The remaining problems are listed, and what is open off the U-domain is stated (Claim B2.0 unwritten; the full-atom residual needs (LF); the p\* ∉ E branch is conditional; non-adding-up rankings are unexamined).

## 2. Edits to existing §8.1 and §8.5 text

| Line | Change | Source |
|---|---|---|
| 1566 | §8.1 summary: the reference "(f)" becomes "(g)". Added one sentence: rounds 14–15 sharpen the target (no leading density on some edge region; not glued credal), with a pointer to §8.5(g). | — |
| 1749 | §8.5 lead-in: "part (f)" becomes "part (g)" twice. Added a sentence describing the new part (f) and noting that the old (f) is now (g). | — |
| 1854 | **Theorem Q36: new item (a′)** (n = 3: positive integrable leading densities on both edge regions ⇒ a nonzero leading charge on M, so (a) applies). This is the referee's framing. | B1_referee (iv) |
| 1861 | Q36 proof sketch: "(a′) is Theorem B13". | — |
| 1863 | Q36 status: dated "Round 14" sentence. (a′) is B1.3, proved, one reader. Its only use of K′ is the linking step. Leading densities propagate; endorsing weights need not (Prop B1cex). | B1_referee (iv), §0 |
| 1871 | Cor Q37 status: dated "Rounds 14–15" sentence. Q36(a′) extends the leading-charge clause. By B3.1, "total and AR" is a special case of "leading charge", and B3.2 replaces the complete clause. Thm C16 adds glued credal worlds. | B1_referee (iv); B3_referee §2; C12_referee §3 |
| 1922 | Remark straighten status: dated "Round 14" sentence. After B3.2, straightening is one route to AR for total worlds, and Prop B34 shows that crossing can coexist with a world that is not fine. | B3_referee §§2, 4 |
| 2006, 2030 | "item (R3) of part (f)" becomes "part (g)" (reference update only). | — |

## 3. New part §8.5(f) "Rounds 14 and 15" (lines 2291–2594)

Every item below is labelled exactly as its referee assigns.

### Lead-in and notation

| Line | Item | Status |
|---|---|---|
| 2291 | Lead-in: what rounds 14–15 asked; no cover found; the B1 §1 reading of the additive contradiction as an exchange-rate cycle. | CHECKED, a reading |
| 2293–2299 | Sign classes Q_l; R_ij = Q_i ∪ Q_j; link class Q_i, non-null. Definition of a leading density (L1) and of additivity on S. | Includes the referee's cosmetic fix ("pairwise disjoint; union M up to null planes") |

### B1: the link class (B1_notes, B1_referee)

| Line | Item | Status |
|---|---|---|
| 2301 | **Lemma B10** (= B1.0), (L2). | Proved; confirmed, one reader. The positivity note is the referee's. |
| 2313 | **Lemma B11** (= B1.1, gluing) and the glued density. | Proved; confirmed (Sierpiński remark). |
| 2321 | **Lemma B12** (= B1.2, transfer chain). | Proved; confirmed, with the referee's added "common m" sentence. NUMERICS from both scripts. |
| 2329 | **Theorem B13** (= B1.3, edge leading densities propagate). Also added to Thm Q36 as (a′). | Proved; confirmed, one reader. Uses / not used; the t1_chain caveat. |
| 2342 | **Proposition B1cex**: the referee's counterexample (edge comparisons alone do not determine a world). | Proved in a referee report, one reader; NUMERICS. The B1 §0 headline is not included. |
| 2347 | **Corollary B14** (= B1.4), with the "every world that does not add up" form (contrapositive of B13). | At the status of M0closed(b); confirmed. |
| 2347 | B14 strengthening to integrable ρ ≥ 0 not a.e. zero, via S21. | CHECKED, with the referee's added sentence that L2 comes from B10. |
| 2347 | B14 scope remark: countably additive densities only; finitely additive gluing open. | — |
| 2355 | **Corollary B15** (= B1.5). (a) Corrected: the reversal contradicts the *second* claim of B13, and the hypothesis is stated precisely. (b) The referee's ordinal version: densities proportional on M, so every aggregate is ψ¹'s order. | Proved with the referee's corrections, one reader. |

### B3: total worlds (B3_notes, B3_referee)

| Line | Item | Status |
|---|---|---|
| 2367 | Definitions: total, AR, top level, leading top level (referee R2), cancellative, ⊴-null. | — |
| 2369 | **Lemma B31** (= B3.1). | Proved; confirmed. |
| 2374 | **Corollary B32** (= B3.2), with the wording repair "a total world of a cover *that does not add up*". | At the status of S21 and Q37. |
| 2379 | **Lemma B33** (= B3.3, order continuity on edges), with the "squeezed in ≤_i" gloss. | Proved; confirmed. |
| 2391 | **Proposition B34** (= B3.4, ultrafilter edge example). | Proved; confirmed with repairs. |
| 2403 | **Theorem B35** (= B3.5), stated for cancellative *leading* top levels, i.e. also for incomplete worlds (referee Remark R2). | Proved; confirmed; extension by R2, one reader. |
| 2411 | **Corollary B36** (= B3.6), with the IRWAS description repaired (two-tier and one-tier both covered). | Proved; confirmed; extended by R2. |
| 2416 | **Proposition B37** (= B3.7) for leading top levels. Narrative labelled HEURISTIC; the referee's §6.2 consequence included. | Proved; confirmed; extended by R2. |
| 2424 | **Conjecture B3C**, with the corrected implications. | Conjecture. |
| 2429 | **Proposition B3R3** (referee Prop R3: n = 2, the class chain is [0,1]). | Proved in a referee report, one reader. |
| 2440 | **Conjecture B3Cp** (= B3.C′), with the referee's remarks; the vector-measure sketch HEURISTIC and not claimed. | Conjecture. |

Further details for B3:

- **B34 repairs.** It needs the ultrafilter lemma (BPI). (K) holds trivially. (d) uses the referee's jump argument instead of the Savage import. Finitely additive leading charges are allowed in S21.
- **B34 scope remark, corrected.** S22 needs (C). Without (C) the world is realised in a two-world ranking (referee Prop R1, described in the status). Whether a third world can realise it is open.
- **B3C corrected implications.**
  - "Would follow from", not "equivalently".
  - "If true: every world of a cover that does not add up is not total; no all-total ranking covers", not "excluded outright".
  - (C) and the third world are unused, and B34 shows that straightening cannot be the general route.

### C1: glued credal worlds (C1_notes top; C12_referee §3)

| Line | Item | Status |
|---|---|---|
| 2445 | Definitions: Γ_ij, Γ_ik, (F), edge unanimity ⊑/⊏, glued closure, Γ-leading, link cones, Γ^gl, ⪯_Γ, Γ^gl-strict, (UI). | — |
| 2451 | **Theorem C11** (= C1.1, dichotomy). | Proved; confirmed, one reader (cosmetic repair; ref_c1 check). |
| 2462 | **Theorem C14** (= C1.3 + C1.4, the closure is Γ^gl-unanimity). | Proved; confirmed. NUMERICS caveat: the script checks only weak acceptance. |
| 2462 | C1.2/C1.5 ("gluing refines the edges") in the C14 status, with the referee's pointedness line. | — |
| 2462 | "Glue dichotomy" sentence, with the referee's **scope** restriction to Γ^gl-weak worlds; the band is open. | — |
| 2474 | **Theorem C16** (= C1.6). | Confirmed at the status of M0closed(b), with the scope remark. |
| 2482 | **Theorem C17** (= C1.7, Γ^gl-band). | Proved; confirmed. |
| 2487 | **Corollary C18** (= C1.8), with the referee's strict-fineness repair (S′ ⊊ S). | CHECKED (Savage); confirmed at CHECKED. |
| 2492 | **Proposition C19** (= C1.9). The "supports must cross" remark is marked HEURISTIC, as the referee requires. | Proved; confirmed. |
| 2497 | **Question C1.Q**, plus the referee's §4 remark (C1.Q and C2.C are the same residual) and the single proposed target. | Open. |

### C2: density unanimities and (LD) (C2_notes top; C12_referee §§1–2)

| Line | Item | Status |
|---|---|---|
| 2499 | Definition of (LD); the C2.1 setting. | — |
| 2503 | **Theorem C21** (= C2.1). | Proved; confirmed, one reader. |
| 2521 | Definition of density unanimity. | — |
| 2521 | **Theorem C23** (= C2.3). C2.4 is recorded in its status in the referee's wording: "necessary condition / sufficient condition", not "exact characterisation". | Proved; confirmed. |
| 2532 | **Corollary C25** (= C2.5). The last sentence is the referee's narrowed form: "an input outside this list: the third world, the link class, interior indices, or the shape of coherent edge models in R³". | Confirmed for the listed inputs. |
| 2537 | **Proposition C26** (= C2.6, link rigidity). | Proved; confirmed. |
| 2542 | **Corollary C27** (= C2.7) with the T1 consequence. Box densities were not re-checked by the referee. Remark C2.8: the identity is confirmed; its edge consequences are CHECKED (sketch), as the referee requires. | Proved; confirmed. |
| 2547 | **Conjecture C2C**. | Conjecture. |

Further details for C21:

- **Repairs.** Statement (5) now also covers leading densities that may vanish (G1). The proof sketch now has the endpoint cases s ∈ {0,1} (G2), uses only (P1) applied twice (G3), and gives the referee's S21-free closing.
- **Wording.** The status says that (St) is needed (the referee's §0 wording fix).
- **Remarks kept.** The worlds add up and so are no step towards T1; the envy form C2.2 is a special case.

### B2: general decomposable domains (B2_notes, B2_referee)

| Line | Item | Status |
|---|---|---|
| 2552 | Setting: A\*_x, face model at x, (γ), line ties and apex ties, the tangent hexagon 𝓗_T. | — |
| 2554 | **Theorem B21** (= B2.1), stated for every all-facing T, as the referee upgrades it. | Proved; confirmed with repairs, one reader. |
| 2568 | Paragraph on rankings that add up on a general domain, with **Claim B2.0** stated as **not proved**. The GAP and the steps still to write are listed. Everything about rankings below is marked "conditional on Claim B2.0". | — |
| 2570 | **Corollary B22** (= B2.2; no apex ties at p\*; the fan design is impossible). | Conditional on Claim B2.0. |
| 2575 | **Proposition B213** (= B2 Prop 13) with the referee's tie anatomy: at most three full corner c-atoms; a zonotope; "interior", not "centre". | Proved; confirmed with repairs. |
| 2585 | Full-atom residual (B2's "(R2)") and why Prop carrying(d) does not transfer. | — |
| 2587 | **Proposition B2ex**: the referee's field realising the residual without (LF). | Proved in a referee report, one reader. |
| 2587 | B2.R restated under (LF) (CONJECTURE), and the referee's nearby target (CONJECTURE), both in the B2ex status. | — |
| 2592 | **Corrected §6 audit.** Route I1 survives E with p\* ∉ cl E *conditionally* on (TS), edge confinement and K_q → {e_b}. The unaudited inputs are listed (TSalways, cuts/apex, vertexfree(i), every-q CF(⇒)). The overstated B2 sentence is not adopted. Lemma quasilin is unavailable on two-sided domains. | CHECKED (B2), corrected by B2_referee §7. |
| 2594 | Consequence for (M0) on general decomposable domains, conditional on Claim B2.0. | — |

Further details for B21:

- **Repairs.**
  - Lemma 9 step 3 uses the referee's argument (reject cone contains the short arc; Fubini; a.e. gamble; measurability).
  - Lemma 7: good levels with essential bounds, uniformity by chaining, "one type" of line tie.
  - D^i ∈ M follows from Remark advicerange.
- **Uses / not used.** It is the two-sided generalisation of crosspin and midarc.
- **B2 Remark 5.3 as corrected.** It is an alternative proof, not a shorter one. What is new on M_U is an alternative proof of Remark midarc.

## 4. §8.5(g) (formerly (f)), rewritten (lines 2596–2636)

| Line | Change |
|---|---|
| 2596–2604 | **New opening: "What a cover on M_U still needs."** See the list after this table. |
| 2606 | "Two worlds." prefix. Items (R1)–(R3) are unchanged, because they are cited throughout part (c). |
| 2611 | (R4): appended a "Round 14" sentence (after B32, nestedness is one route to AR for total worlds; B34). |
| 2617–2618 | Lifting bullets. First bullet: a "Round 14" sentence (B32; B3C would remove nestedness). Second bullet: a "Round 14" sentence (leading edge densities globalise, B13; edge comparisons alone do not, B1cex) and a "Round 15" sentence (for Γ-leading worlds the interior step is exactly Question C1.Q). |
| 2621–2629 | **New list "Three worlds: questions from rounds 14 and 15."** See the list after this table. |
| 2630–2635 | **New list "Off the U-domain."** See the list after this table. |
| 2636 | Status line extended: (R4) for total worlds; lifting via B13; the interior step is C1.Q for Γ-leading worlds; new open items listed. |

The new opening (lines 2596–2604) assumes (H_U) and says that every world of a cover that does not add up:

- is not (CP-a) and has no leading charge;
- lacks a leading density on one of its edge regions (B13/B14; ρ ≥ 0 version CHECKED; countably additive only, since finitely additive gluing is open);
- is not glued credal (C16), and if it is Γ-leading under (F), (UI), is not total (C18) and carries a finite Γ^gl-obstruction (C19);
- if total, is not AR (B32) and has a non-nested edge (Q36(c));
- has no cancellative leading top level with dense null sets and no small-κ value top level (B35–B37), total or not;
- under additive neighbours with density-unanimity edges, has a degenerate link-class law (C26/C27).

It also notes non-additive behaviour at T1 (Thm R3), the conclusion "fails to add up, no leading density on some edge region, not glued-credal", and that C21's world, the only known one without a leading density, adds up.

The new "Three worlds" list (lines 2621–2629) covers:

- finitely additive gluing;
- Conj B3C (first test B3Cp);
- Question C1.Q;
- Conj C2C;
- other edge orders without a leading density (the C25 restriction in the referee's wording);
- case (i) of Thm R3.

The new "Off the U-domain" list (lines 2630–2635) covers:

- additive rankings (Thm gm, Cor gmcharges);
- adding-up rankings: Claim B2.0 must be written; conditional on it, no apex ties; the full-atom residual needs (LF); the p\* ∉ E branch is conditional;
- (CP-a) beyond M_U: Conj U, Cor residual;
- non-adding-up rankings: unexamined;
- the world-level results stated on M_U only.

## 5. Sources (lines 2674–2731)

- Added BRIEF13.md, BRIEF14.md, B1/B2/B3 notes and referee reports, C12_referee.md, and *Independent Rankings Without
  Additive Structure.tex*.
- C1_notes.md and C2_notes.md entries now describe the round-15 content at the top of each file and mark the round-10
  content as the archive.
- The S34_referee entry's reference "(R3) item of §8.5(f)" became "(g)" (line 2724).

## 6. Not changed

- §§1–7 apart from the introduction and the status table.
- The statements of all earlier results, except the new item (a′) of Theorem Q36, which the B1 referee assigns.
- §8.5(a)–(e) (apart from the status sentences listed in §2).
- §8.6 and §9.
- Labels of existing environments.
