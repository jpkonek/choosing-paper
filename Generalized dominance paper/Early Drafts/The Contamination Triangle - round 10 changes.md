# Changes, round 10 (14 Oct 2026)

Target: `writeup/The Contamination Triangle.tex`. The backup made before any edit is
`writeup/The Contamination Triangle (pre-round10).tex` (identical to the round-9 version).
Line numbers refer to the **new** file (1446 lines). It compiles cleanly with `latexmk -pdf`: no errors, no undefined
references, no overfull boxes, 58 pages. The only messages are four underfull hboxes in narrow table cells.

Sources used: BRIEF9; I1_notes, I1_referee; I2_notes, I2_referee; C2_notes, C1_notes, C1C2_referee; PropD_notes;
TS_second_referee. The repaired version of every statement is the one used (referee versions over note versions).

Section numbering. A new Section 6 is inserted. Old §6 (coherent almost-preferences) becomes §7, old §7 (what is
excluded and open) becomes §8, and old §8 (positive results) becomes §9. "Two concrete open questions" is now §8.1.
No existing label was changed.

## 1. New Section 6, "No additive cover on general decomposable domains" (lines 812–1091)

- **§6 preamble (812–814).** Defines "cover" for the section and notes that "in every cover" statements are vacuous
  proof steps.
- **§6.1 (816–842).**
  - **Theorem 6.1 `thm:gm`.** For every ε ∈ (0,1), and at every interior target weighting, no strictly guiding
    additive ranking with integral penalties covers T1 on any (LF) decomposable domain.
    - Its status names the three routes and their referees (I1_referee; I2_referee §8 with Prop D*;
      C1C2_referee §6, Theorem R with Prop P, empty exceptional set).
    - It states that the box inequality is not used in I1's own steps, but that box witnesses enter through
      Thm cuts / Cor TSalways (I1_referee R7, TS_second_referee §2).
  - **Corollary 6.2 `cor:CFnone`.** CF(T1) has no solution, at the status of Thm ccibu. The status explains why: the
    converse direction of Prop CF is needed.
  - **Corollary 6.3 `cor:gmcharges`** (charges, given interior minimisers). The referees disagree on scope, and this is
    reconciled as follows:
    - it is proved along route I2 only (I2_referee §8, via N14 Thm C2);
    - I1's charge clause is CHECKED only;
    - Theorem D has not been checked for charges (PropD Lemma 1.1(c));
    - so the short route and route C2 are recorded for integral penalties only.
  - A paragraph summarising the three routes.
- **§6.2 Common inputs (844–860).**
  - The normalisations p* = u (world reweighting) and x = x₊ (transposition).
  - The chart cells, with the CF every-q form and the silence cell S(g).
  - **Lemma 6.4 `lem:veccluster`**: vector cluster convergence, with the corner-ray caveat.
- **§6.3 First proof, route I1 (862–937).**
  - Edge maps, Z_o and the non-failing set N_E are defined.
  - **Lemma 6.5** (strict vertex signs, edge maps; repair R2, no fold-back at corners).
  - **Prop 6.6** (exact edge limits = Prop E; repair R3, corner rays at t = c₀, 1−c₀ excluded harmlessly).
  - **Prop 6.7** (pinned c-lines = Thm R).
  - **Lemma 6.8** (forced supporting lines = Lemma S).
  - **Lemma 6.9** (window, projectivity at e₁, three-line determinant = Lemmas W, P, D). It carries repair R5 (the
    window points are fixed before U is shrunk) and repair R6 (the projective reading at ε = 1/7).
  - The first proof of Thm 6.1 (I1 Thm I1).
  - A paragraph "Where the contradiction lives": (Diag), i.e. the facet maps are diagonal iff x = 1, against the
    corner equation.
- **§6.4 Precise collars and precise regions (939–1018).**
  - **Lemma 6.10** (no straddling; I2 Lemma 1 with repair R1, and C2 Lemma 3.1).
  - **Cor 6.11 `cor:chord`** (C2 Cor 3.3: on λ_b, K_q lies in the tangent wedge and touches ℓ′ and ℓ).
  - **Thm 6.12 `thm:collar`** (I2 Thms 2–3 = C2 Cor 3.2 + Thm 4.1). The collar may be a horn.
  - The condition **(DL)** ("d-line condition"). It is renamed from PropD's "(C)" to avoid a clash with axiom (C).
  - **Lemma 6.13** (who satisfies (DL); PropD Lemma 1.1).
  - **Thm 6.14 `thm:D`** (Theorem D). Its status: proved, not refereed. The dichotomy has independent one-reader proofs
    (Prop P, Prop D*). It replaces R4 Prop D, whose status CHECKED is withdrawn (GAP per R8).
  - **Thm 6.15 `thm:T`** (Theorem T, transport). Its status: proved, not refereed; the same content was refereed in
    I2 Prop 4(b),(c) and C2 Prop 5.2.
  - **Thm 6.16 `thm:A`** (C1 Thm A, with the Borel-set repair through P(y,±g) = 0).
  - **Cor 6.17 `cor:nocap`** (C1 Cor 5.1: the sector-cap example C1 and every diagonal-projective precise region are
    part of no cover).
  - **Remark 6.18 `rem:B`** (C1 Thm B, no o-minimal solution; marked superseded).
- **§6.5 Second and third proofs (1020–1043).**
  - Route I2: collar, then Thm D, then Thm T, then transition points, then blow-up, giving w₁ = w₂ = w₃ against
    v₁ − v₃ = κ.
  - Route C2: gluing conics, then hand elimination, giving W = κ off b and 1 at b, with the exceptional set EMPTY.
    Candidate (I) is a shared line not through e_b. Then the two caps contradict Thm T(c) / C2 Prop 5.2.
  - Short route: collar, then Thm D, then Thm A. It uses no Bezout or conic algebra.
  - Each route has its own status line.
- **§6.6 Dependencies (1045–1091).** Table 2 `tab:gmdeps`.
  - Imported inputs with two readings (TS_second_referee): Thm TSalways and its inputs, Cor TSalways(b)(c), Thm cuts,
    Thm apex (with repair), Lemma R1, Prop vertexfree, Prop CF(⇒) every-q form (with repair), Lemmas quasiconcave,
    B1 and walls.
  - Imported inputs with one reading: Prop necessary with R1 Prop 3.1, R4 Thm B, and the crossing-row/box assembly.
  - New steps, one reading each: I1; I2; C2/C1.
  - Theorem D and Theorem T: none yet.
  - The closing paragraph names the next test (a second reading of one complete route).

## 2. Corrections required by the referees

- **(a) "Competition … at a positive distance from ∂Δ is impossible"** (TS_second_referee §3.3).
  - Thm apex statement (742–744): the sentence is replaced by "the cut d-faces (a_m, z_m) converge into ∂Δ, to
    [e_b, z*], with apexes → e_b".
  - Its status (748) records the second reading, the repair and the reason.
  - The introduction (65) is rewritten.
  - §5.4 (E4′) (806) states what is proved and that the old sentence is unproved and unused.
  - No other occurrence remains. Grep for "positive distance"/"finite distance" finds only:
    - the two repair notes that quote the old sentence (748, 806);
    - unrelated uses (206, 1305, 1318).
- **(b) The §5.3 chord bullet** "poking strictly beyond ℓ … beyond both ℓ and ℓ′ on the chord" is replaced (806–808).
  The new bullet records:
  - what Prop vertexfree proves (weak inequalities on the chord; strict inequalities only on the open sides);
  - the correction by Cor 6.11 (C2 Cor 3.3, confirmed in C1C2_referee §1; TS_second_referee §4.3);
  - the origin of the error (a summary bullet in N28_referee §4).
- **(c) The sector-cap example C1** (807, and 1011–1013). It is now said explicitly to be part of no cover and of no
  CF(T1) solution (Cor 6.17 / C1 Thm A). Along route C2 the forced caps have w = (κ off b, 1 at b), not the identity.
- **(d) Prop CF(⇒) repairs** (proof 786; status 788), from TS_second_referee §5:
  - R1 Prop 3.1 is cited for Hausdorff continuity, replacing Prop reduction;
  - the good set is symmetric (the intersection of the co-null sets for g and −g);
  - joint measurability of (q,g) ↦ 1[q ∈ R(g)] for Fubini;
  - the explicit every-q argument;
  - the note that CF data are not unique.

## 3. Status updates from TS_second_referee (second readings)

| Lines | Item | Update |
|---|---|---|
| 404 | Lemma UVN | second reading recorded |
| 420 | Lemma PL2 | second reading recorded |
| 644 | Lemma quasiconcave | second reading recorded |
| 649 | Lemma B1 | second reading recorded |
| 656 | Thm TS | second reading: items 1–5 re-derived, items 6–8 spot-checked |
| 663 | Thm cuts | second reading, plus the cosmetic hypothesis repair; Step 1 uses the chart-form edge box |
| 668 | Cor availability | second reading recorded |
| 721 | Lemma walls | second reading recorded |
| 729 | Thm TSalways | independent second reading; its inputs re-derived |
| 738 | Cor TSalways | second reading of (b), (c), with a dependency note |
| 756 | Lemma R1 | now two readers (was "one reader only") |
| 770 | Prop vertexfree | second reading. The weak forms suffice for (i), (iv), which hold on both sides of p*. Points to Cor 6.11 and Thm 6.16 |

**R4 Prop D.** The write-up never cited R4 Prop D by name. Its old status (CHECKED in R4; GAP in R8) is withdrawn in
the status of Thm 6.14. Every use now goes through Thm D, Prop P or Prop D*, combined with the CHECKED injective case
(C1 Lemma 5.0).

## 4. Introduction, summaries, §5.4, §8, §9, sources

- **Date line (42).** Now "round 10".
- **Introduction item 2 (65).** Rewritten: the new main theorem, the CF corollary at CCIBU status, the three routes,
  and the charge clause. The overclaim is removed.
- **Introduction item 6 (69).** Q2 is answered.
- **Status table (89–100).**
  - Rows for TSalways, apex/vertexfree, Lemma R1 and Prop CF are updated to two readings.
  - The row "CF(T1) open; sector cap passes" is replaced by seven rows: Thm 6.1; Cor 6.3; Cor 6.2;
    Lemma 6.10 / Thm 6.12 / Cor 6.11; Thms D and T; Thm A; Rem B.
- **§5 closing paragraph (800).** Points to §6.
- **§5.4 (802–810).**
  - Retitled "What was open on general decomposable domains".
  - (E5a) unchanged.
  - (E4′) is closed, and correction (a) is applied.
  - The sector-cap bullet takes correction (c).
  - The chord bullet takes correction (b).
  - Conjecture N21/N28 is replaced by a pointer to Cor 6.2 and Thm 6.1. The `conjecture` environment and its label
    `conj:N21` are removed, and the only reference to them (old Q2) is rewritten.
- **§8.1 (1324–1340).**
  - Retitled "Two concrete questions, one now answered".
  - The opening sentence now cites Thm 6.1.
  - "General two-sided domains are a separate open route" is replaced: there is no additive escape, and non-additive
    rankings on two-sided domains have not been examined.
  - **Q2 is answered "no"** (1333–1338). What remains is listed: the converse/CF form at CCIBU status; integral versus
    charge (existence of minimisers; one route only); readings.
  - The closing sentence is limited to non-additive rankings.
- **§9 (1400).** The continuous-map bullet now says the general-domain question is answered negatively (Thm 6.1).
- **Sources (1414–1440).** New entries: BRIEF9.md; TS_second_referee.md; I1_notes/I1_referee; I2_notes/I2_referee;
  C2_notes; C1_notes; C1C2_referee; PropD_notes.

## 5. Conventions checked

- No theorem names inside theorem environments (no optional arguments).
- `\coloneqq` throughout. New terms are defined in words on first use: edge map, non-failing, forced supporting line,
  tangent wedge, precise/precise region, diagonal-projective, precise collar, (DL), transition point.
- Every new statement has a `\status{}` with `\src{}` sources and referee status.
- Terminology grep (`menu|forced[- ]silen|accept-or-silence|available action|forced acceptance|forced advice`): one
  hit only, the pre-existing "Earlier terminology" paragraph (line 166), which is allowed.

## 6. Housekeeping

- A temporary draft of §6, `writeup/sec_gm_draft.tex`, was created by mistake in `writeup/` during editing. It was
  moved to the session scratchpad (`scratchpad/r10_tmp/`). No pre-existing file was deleted or modified apart from the
  target `.tex` and its LaTeX build products.
