# Changes, round 11 (14 Oct 2026): "the positive ordinal attempt"

Target: `writeup/The Contamination Triangle.tex`. The backup made before any edit is
`writeup/The Contamination Triangle (pre-round11).tex` (identical to the round-10 version, 1446 lines).
Line numbers refer to the **new** file (1748 lines). It compiles cleanly with `latexmk -pdf`: no errors, no undefined
references or citations, no overfull boxes, 75 pages. The only messages are five underfull hboxes in narrow table cells.

Sources used: BRIEF10; P1_notes, P2_notes, P3_notes, P4_notes; M0_referee, M0_second_referee, P2P3_referee,
P4B_referee. The refereed or repaired version of each statement is the one used. Terminology follows
termfix/TERMFIX_RULES.md (grep of all added lines for menu / forced silence / accept-or-silence / available /
offered / forced acceptance / forced advice: 0 hits). No theorem environment has a name; definitions use `\coloneqq`;
every new statement has a `\status{...}` line naming its source and referee status with `\src{}`.

Numbering. A new §7.7 is inserted (old §7.7 on the lexicographic class becomes §7.8), and a new §8.4 is inserted (old
§8.4 "Other targets" becomes §8.5). No existing label was changed.

## 1. Case M0 closed on the U-domain (§7, items 1 of the brief)

- **§7.6 `sec:M0-residual` (1295–1303).**
  - Intro sentence: both residuals are now closed.
  - R-a′ and R-b′ statuses changed from "open" to **CLOSED**, each with the result that closes it.
  - "Closed:" becomes "Closed earlier:".
  - The localisation paragraph is marked "superseded in round 11", and a closing sentence says how each failure point
    was resolved (quasi-linearity, ball lemma / PL2 across chords, crossing pinning).
  - Sources: P4 §§2–3, M0_referee, M0_second_referee.
- **New §7.7 `sec:M0-closed`, "Case (M0) is closed on the U-domain" (1305–1420).**
  - 1305–1311: introduction; standing data (field with (γ), E null by Tonelli, integrability unused, good gambles);
    tie-breaking families B^A_q and admissibility, with A = ∅ (K^♭) and the generic directional families.
  - **Lemma 7.18 `lem:quasilin`** (1313–1325): quasi-linearity of every admissible family; continuity off E and vertex
    limits (UVN); exact charts for K^♭. Status: P4 Lemmas 2.1–2.2, confirmed by both M0 referees; P1 Lemma P1.2 is the
    case A = ∅.
  - **Lemma 7.19 `lem:ball`** (1326–1334): the ball lemma. Status: P4 Lemma 2.3, confirmed twice; Prop F steps 1–4 now
    have three readings; step 5 is not used.
  - Face models (1334) are defined in plain words.
  - **Proposition 7.20 `prop:crosspin`** (1336–1343): crossing pinning, in the **second referee's strengthened form**
    (any interior target, no "p* ∈ E", every zero-coordinate boundary gamble), with the T1 sign consequences. Status:
    M0_referee Prop R.1, strengthened and confirmed in M0_second_referee §2.2; two readers; NUMERICS.
  - **Proposition 7.21 `prop:chainchords`** (1344–1352): the §4 chain survives atom chords away from p*, hence
    p* ∈ E. The proof sketch is the step-by-step replacement table: quasi-linearity, PL2 for K^♭ via the ball lemma,
    nopin, Step 4 on λ∖E, anchors off E, robust cluster clause, edgebox, normalisations. Status: P4 Thm 3.1 / A1,
    confirmed by both referees (wording repair on anchors incorporated). R-b′ is closed. The all-facing extension is
    CHECKED.
  - **Proposition 7.22 `prop:carrying`** (1353–1367): at p* ∈ E, (a) S is non-null; (b) carrying corner atoms;
    (c) frozen bounds π⁺ ≥ 0 > π^♭; (d) the short argument. Status: P4 Prop 4.1(i), (ii), Lemmas 2.4, 2.5, 4.2,
    Thm 4.3, confirmed twice; the second referee's proof of (a) via Prop 7.20 is noted.
  - **Theorem 7.23 `thm:M0closed`** (1368–1379): (a) additive form; (b) ranking form, with or without (E_ψ). Proof:
    Prop 7.21 when p* ∉ E; Props 7.22 and 7.20 with a directional limit when p* ∈ E. Status: (a) new parts read by two
    referees; (b) at the status of Prop M0 (α), (γ) without (E_ψ), whose imports are N13 Prop B and N19 Prop R3(a), each
    read once. The status also gives the list of what is not used, the completed dependency list (M0_second_referee §6),
    the scope (all-facing triangles and every K′: CHECKED only) and the domain caveat.
  - **Corollary 7.24 `cor:M0closed`** (1380–1390): (a) a cover needs a world failing SP^reg ((M1)/(M2)); (b) R-a′,
    R-b′, P4's triple-point configuration and P1's split facets are empty; (c) no 𝓛₂ˢ ranking covers T1; (d) Q1 is
    answered on M_U. Status: M0_referee §7, confirmed in M0_second_referee §7. P4 Thm A3 is a special case.
  - **Remark 7.25 `rem:CPaU`** (1391–1395): **no (CP-a) ranking covers T1 on M_U**, by applying Thm 7.23(a) to the
    field ψ^P of Thm integral. This is an editor's observation that is not in the sources. It is labelled CHECKED,
    not refereed. See "Points for the author" below.
  - Paragraph "How the residuals were closed" (1396–1397): P4's triple-point configuration. It is named so as not to
    clash with condition (TP) of Def. realisation. Full atoms are handled by P4 Prop 4.1(iii); the M0 referee's
    observation about directional limits is recorded.
  - **Remark 7.26 `rem:midarc`** (1398–1402): Prop R.2 (no face model is positive on a middle arc). It is
    proved in M0_referee and confirmed by the second referee, and is marked as not needed (its hypotheses are never met).
  - Paragraph "The results of P1" (1403–1414), including **Lemma 7.27 `lem:P1box`** (P1 Lemma P1.1, confirmed). Its
    status records that the mirror (lower) box bounds were **upgraded to PROVED** by M0_referee. The paragraph also
    covers:
    - Lemma P1.2, which is Lemma 7.18 with A = ∅;
    - P1.3 / P1.4, which are conditional on (HC), carry a scope repair and are superseded;
    - the split-facet configuration: its algebra is consistent (NUMERICS, reproduced), but it is wrong as an escape;
    - P1 §4.3(c), "nothing local closes it", which is wrong.
  - Paragraph "What singles out T1" (1415–1420), from task 4 of the second referee:
    - the two branches and the inputs specific to T1 in each;
    - the six-crossing counting fact;
    - the normalised-box contrast;
    - why n = 2 (N26.1) is consistent with the result;
    - NUMERICS;
    - the extension to every all-facing triangle, which is **CHECKED only**.
- **§7.8 (lexicographic class)**:
  - status of Thm Ltwo (1451): the "consequently" clause is now vacuous for T1;
  - Prop R1N26 (1459): superseded as a route;
  - **Conjecture N26.R (1464): superseded for coverage** by Cor 7.24(c), while still open as stated.
- **§7.5**: the status of Thm Estructure (1262) records three readings of Prop F steps 1–4 and one of step 5.
- **§7.3**:
  - Remark EPchords (1196) gains a pointer to Rem 7.25;
  - the status of Conj U (1209–1210) says it holds vacuously on M_U (CHECKED) and remains open on other non-adjacent
    domains.
- **§2.5** (292): one sentence says that on M_U a cover must fall under (M1) or (M2).

## 2. New §8.4 `sec:open-ordinal`, "Building ordinal rankings directly" (1540–1672; item 2 of the brief)

- 1540–1541: introduction, with the objective of BRIEF10. No cover was constructed.
- **(a) Exact test and the limit rule (1543–1583).**
  - Recalls Thm closure of *Coverage after Neutral Abstention*: four rules, three forbidden outcomes.
  - Defines successful systems, choices, the limit rule R5 and Cl₅(κ).
  - **Theorem 8.3 `thm:R5`** (P3 Thm 3.1; CONFIRMED in both directions, P2P3_referee A2). It is "exact but formal",
    and compactness (P3 Thm 4.1, confirmed) is noted in its status.
  - Exchange transport and exchange transversality (P3 Lemma 2.1, Cor 2.2, §5), with the general-domain formula repair
    R-P3a.
  - The extension lemma as posed in *Vacuous Targets* §5.
  - **Proposition 8.4 `prop:extcounter`**, the two counterexamples (P3 Examples 1, 2; confirmed). The status gives
    **the referee's narrowing**: they are not obstructions for T1; what (b) proves is non-preservation of
    extendability and cleanliness under ω-unions (R-P3b); EL* is open.
  - **Theorem 8.5 `thm:witness`**, the positive lemma with an additive witness (P3 Thm 7.1; confirmed, "close to
    tautological"). Its status covers:
    - its scope (reproduced covers, and the V clause restricted per R-P3c);
    - witnessed T1 covers, which are excluded by Thm 7.23;
    - pre-systems, which are also excluded through R-P3d (an editor's observation, CHECKED, not refereed).
  - **Conjecture 8.6 `conj:villegas`** (P3.C1), with the referee's remarks R-P3e (non-generic nesting; the target
    "exact representability by a state").
- **(b) Exchange rates and layering (1585–1630), from P2.**
  - **Lemma 8.7 `lem:vectorform`** (P2.1; confirmed).
  - **Proposition 8.8 `prop:flexible`** (P2.4: (a)–(c) proved, (d) CHECKED; with its scope).
  - **Theorem 8.9 `thm:LX`**: two-level lexicographic worlds with a **weakly signed primary**, stated in the
    referee's class repair R-P2c (**α_i ∈ ℝ**; covers 𝓛₂ˢ); two levels only.
  - **Proposition 8.10 `prop:rigid`** (P2.6; the "far" wording repair).
  - **Lemma 8.11 `lem:nested`** (P2.7; crossing is "not an escape" only for the two-level class).
  - **Proposition 8.12 `prop:P23`**: the exact statement replacing P2.3 (P2P3_referee B3). It says that the
    selection of any T1 cover by any ranking fails Hausdorff continuity on Δ° or vertex-respecting straight charts.
    Its status records that the localisation to one facet arc is a **GAP**.
  - Paragraph "Holonomy (NUMERICS)" (1630) records P2.2 only as showing that the chain needs linearity on all three
    facets. A kink is excluded by coherence via Lemma twoslope. The frozen middle sector is R-a′, now closed.
- **(c) Two worlds with a nested selection, and the step to three (1632–1671), from P4 Part B and P4B_referee.**
  - Setting (Nest), with Lemma N0 of the referee, and N17.B′ stated.
  - **Proposition 8.13 `prop:strictescape`**: strict escape, including the referee's b = 0 case.
  - **Theorem 8.14 `thm:E2`**: leading charges and lexicographic worlds with charge levels, finitely or countably
    additive (referee Thm E2 / Cor E2′; one reader). It subsumes P4 Thm B3 (recorded with the referee's remarks).
  - **Theorem 8.15 `thm:E3`**: complete worlds, CHECKED via Savage's theorem, with Lemma T.
  - **Proposition 8.16 `prop:B2`**: the repaired Prop B2. It adds a hypothesis for "fails SP", gives the {0,1}-valued
    counterexample, and supplies a new witness D = (x₀+h,1).
  - "The precise open class in two worlds": incomplete, not CP-a, no leading charge, spread-out certificates, and what
    blocks a proof.
  - "Three worlds": the removal lemma (credited to R2 Thm 7), the n = 3 necessary conditions, why nothing transfers,
    and the attribution correction.

## 3. §8.1, introduction, status table (item 3 of the brief)

- **§8.1 `sec:two-questions`** (1468–1492):
  - The title is now "Two concrete questions, both now answered, and the remaining target".
  - 1474: the first escape is ruled out on M_U. Non-additive rankings, including rankings that add up, are unexamined
    on two-sided domains.
  - 1476–1477: Q1 is marked "Answered on M_U: no", with an **Answer** paragraph covering:
    - Thm 7.23 and Cor 7.24;
    - the fact that tie-breaking cannot help, by the additive form;
    - the status;
    - why N26.1 does not transfer;
    - CP-a (Rem 7.25);
    - the **domain caveat**: proved on M_U only; on general decomposable domains only the additive Thm 6.1 is proved.
  - 1485–1491: new paragraph **"The remaining target"**. The only remaining route on M_U is a world that does not add
    up ((M1)/(M2)). What is known (not CP-a; flexible/LX; 𝓛₂ˢ excluded; and, in the n = 2 nested analogue,
    incomplete, no leading charge, spread certificates) is stated with its scope. The precise target is a three-world
    world that is incomplete, non-lexicographic, without a leading charge and not CP-a, i.e. a counterexample to
    N17.B′ in three worlds. Whether the n = 2 restrictions hold in n = 3 is open.
- **§8.3** (1535–1537): the 𝓛₂ˢ bullet, the M0 bullet (Q1 answered) and the M1/M2 bullet (the only route left;
  pointer to §8.4; N17.B′ narrowed in two worlds) are updated.
- **Introduction**:
  - 42: date "round 11";
  - 66: CP-a item (Rem 7.25);
  - 67: rankings-that-add-up item, rewritten with the round-11 theorem and its reading status;
  - 68: new item "Building ordinal rankings directly";
  - 70: §8 item (both questions answered; the remaining route).
- **Status table**:
  - 107: (U) row;
  - 112–123: residuals row → closed, plus 11 new rows (Lemmas 7.18–7.19, Props 7.20–7.22, Thm 7.23(a), (b), the
    all-facing extension CHECKED, Rem 7.25, Rem 7.26, Lemma 7.27, split facets);
  - 126–127: Prop R1N26 superseded, and a new row "No 𝓛₂ˢ ranking covers T1";
  - 129–141: 13 new rows for §8.4.

## 4. Sources and bibliography (item 4 of the brief)

- Bibliography (1694–1697): Savage 1954; Fishburn 1986; Villegas 1964; Martínez-Legaz & Singer 1987.
- Sources (1706–1709): BRIEF10.md; *Coverage after Neutral Abstention.tex*; *Vacuous Targets and Transfinite
  Construction.tex*; *Three Complete Rankings Cannot Cover.tex* and *Complete Rankings for Any Number of Worlds.tex*.
- Sources (1734–1741): P1_notes, P2_notes, P3_notes, P4_notes, M0_referee, M0_second_referee, P2P3_referee,
  P4B_referee.

## 5. Points for the author

1. **Remark 7.25 (CP-a on M_U)** and the **pre-system remark** in the status of Thm 8.5 are the editor's
   consequences of Thm 7.23(a), not in any source.
   - Remark 7.25 is Thm integral (a), (c) with Thm 7.23(a), exactly as Remark EPchords applies Thm Estructure.
   - The pre-system remark is (γ) by KKM plus the referee's (α) derivation R-P3d.
   - Both are labelled CHECKED, not refereed. If correct, Remark 7.25 settles Conjecture U on M_U, so it deserves a
     referee.
2. Thm 7.23(b) is only as strong as N13 Prop B and N19 Prop R3(a), each read once. Both M0 referees recommend a
   second reading.
3. A scratch copy of the inserted §7.7 block was written to
   `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r11_block_M0.tex` during editing.
   This is outside the permitted locations. It is not deleted, per instructions, and can be removed.
