# Changes, round 17 (15 Oct 2026): H1, H2, H12_referee, J1

Backup: `The Contamination Triangle pre-round17.tex`. It is a copy of the file before this round, 3046 lines. The new file
has 3274 lines. It compiles cleanly with `pdflatex` run twice: 170 pages (previously 156). There are no errors, no
undefined or multiply defined references, no overfull boxes and no LaTeX warnings. The only warnings are 7 underfull
boxes, as before. Line numbers below refer to the **new** file.

Inputs:
- H1_notes.md and H2_notes.md, with the verdicts of H12_referee.md (refereed once);
- J1_notes.md (not refereed).

## Conventions

- Theorem environments carry no names. Note numbers (H1.2, J1.3, ...) appear only in status lines and prose.
- `\coloneqq` is used throughout; `grep ':='` finds nothing.
- The terminology check of TERMFIX_RULES.md finds only line 276, the existing "Earlier terminology" paragraph, which is
  allowed.
- Statuses:
  - H1 and H2 items: "proved (H1/H2); confirmed (H12 referee), one reader", with the referee's repairs.
  - Prop. R.1: "proved in a referee report (H12 referee), one reader". It was also proved independently in J1
    (Thm. J1.1), which is not yet refereed.
  - J1 items: "proved in a note, not yet refereed". Example J1.4 is CHECKED.
- No new mathematics. No existing statement was changed. Superseded passages were extended in place with a
  "Round 17" marker.

## Notation (renamed to avoid clashes; content unchanged)

| In the notes | In the write-up | Reason |
|---|---|---|
| localizing family D_m | Θ = (Θ_m) | D_K denotes coherent models |
| d_t (H1.0) | Φ*_t | d_b is the chain complement |
| Φ(Y) | Φ_t(Y) | t-dependence made explicit |
| readings (E1), (E2) | "total-cost", "cancellation" form (as in part (e)) | E1 is a note name |
| conflict digraph Γ | $\vec{\mathcal H}$ | Γ denotes credal pairs (C1) |
| J1's Π^k_m, D_m | 𝓔^k_m, 𝓔_m | Π is used locally elsewhere |
| J1's conflict sets B^s_m | Ξ^s_m | B denotes Bayes models |
| J1's hypothesis (J) / referee's class 𝒞 | hypothesis (EP), "class (EP)" | J1 is a note name; (C) is an axiom |
| depth index M (H2, J1) | n, d | M is the set of mixed problems |
| W(g), worlds where T1 errs | Ω⁻(g) | W denotes ends |
| H1 §6 cases (A), (B), (C) | referee's (A′), (B), (D) | (C) is an axiom |

## 1. New part (f′) of §8.5, after the E1/F1/F2 material (lines 2896–3092)

Heading: "(f′) Round 17: localized failures are invisible, the conflict digraph, and pattern switching". Part (g) keeps
its label.

**Introduction and setting.** The paragraph states:
- what BRIEF15 asked;
- that there are three notes and no cover;
- the statuses.

The setting paragraph gives:
- densities (a.e. finite, not necessarily integrable);
- the two readings of endorsement, with property (R);
- localizing families, Θ-localized and (Θ, T1)-localized comparisons;
- the deep ends, and why base endorsement implies Θ-localized endorsement;
- Φ_t and Φ*_t.

**H1 (refereed once).**

| Item | Where | Notes |
|---|---|---|
| Lemma H1.0 | lem:H10 (2907) | (b) carries the **referee's missing line** Φ_t(Y) ≤ Σ t_k ρ_kμ(E_kY) < ∞ (H12 §1.2). The status says so. NUMERICS from h1py and h12ref_py |
| Lemma H1.1 | lem:H11 (2920) | The status gives the consequence that the BRIEF15 target (no admissible tuple) is unattainable, and that countably many ends are needed |
| Theorem H1.2 | thm:H12 (2928) | The status adds the referee's c/\|c\| justification of M0closed(a) without integrability (H12 §1.4). It records that (R) suffices and gives the H1.4 consequences as scoped (H12 §1.5): the D2sigma density endorses in the cancellation form; the warning is moot within this setting; F2's nearby target is proved for one non-integrable world |
| Theorem H1.3 | thm:H13 (2936) | The status records: localized endorsement is stronger than base endorsement at T1-wrong ends; T1-correct sets are automatically compatible; a σ-finite version for ≥ 2 worlds is not proved |

- **Line 2944, "What replaces the heaviness hypothesis of Theorem E15".** This is the referee's narrowed statement
  (H12 §1.6), quoted in substance:
  - (h) can be replaced by eventual T1-correctness of every end (H1.3), which (h) implies, with the referee's
    one-line derivation;
  - for finite families, (h) can be dropped unless the conflict digraph has a directed cycle (H2.3 with Prop. R.1).

  H1's own claim, "E1.5 holds without (h)", is reported as not what is proved.

**H2 (refereed once).**

| Item | Where | Notes |
|---|---|---|
| Definitions | 2946 | T1-correct and T1-wrong ends, orthants |
| Lemma H2.0 | lem:H20 (2948) | |
| V(W), improvement regions R⁰_i | 2956 | |
| Lemma H2.1 (a), (b) | lem:H21 (2958) | In (b), endorsement is in the **cancellation form or with ρ_jμ(E_jT1) < ∞** (the referee's repair, H12 §2.2). The status records the referee's corollary (ρ_j(W_m) = ∞ when V(W) = {j}; one reader) and H2's remarks |
| Prop. H2.2 | prop:H22 (2973) | The status says that joint reweighting is already in Lemma E14 and that the new content is (h′) (H12 §2.3). It is not needed after Prop. R.1 |
| Definition of the conflict digraph | def:conflict (2984) | |
| Theorem H2.3 | thm:H23 (2988) | With (b) and (h′). The status gives the arrow-depth adjustment and where finiteness is used |
| Prop. R.1 | prop:HR1 (2996) | (h′) is unnecessary, via the near-Bayes models X_m. Status: proved in a referee report, one reader; independently J1.1 |
| Corollary H2.3′, corrected | cor:H23p (3004) | The statement is the referee's (H12 §2.5): two worlds with T1-wrong ends; two worlds without an integrable full endorser (via H1.2); "two worlds fail to add up" only with singleton V(W). The status quotes the referee's counterexample to the note's deduction |
| H2 §5 | 3012 | The template (CHECKED). What a shadow with (b) and (h′) forces, with the **two §5.2 corrections**: "for every admissible shadow (E1.1)" is deleted, and the citation is corrected to end-protection plus H2.1(a). §5.3, where the design broke. H2.Q as restated by the referee (without (h′), with X_m) |
| Theorem H2.4 | thm:H24 (3014) | The full two-world system in which neither world adds up. The status says every axiom was re-derived by the referee, gives the exact-rational (K) check and the b = 1 wording repair, the NUMERICS, and "not a conflict cycle" |

**J1 (not refereed; header at line 3022).**

| Item | Where | Notes |
|---|---|---|
| Hypothesis (EP) | 3022 | |
| The near-Bayes tool | lem:J1C (3024) | J1 §1, Steps A–C |
| Closure lemma J1.0 | lem:J10 (3034) | |
| J1.1 | 3042 | Recorded as Prop. R.1, proved independently |
| Pattern switching, (Al) | 3042 | |
| Theorem J1.2 | thm:J12 (3048) | The status contains the pairwise sufficient condition (i)–(iii) |
| Cor. J1.3 (a)–(c) | cor:J13 (3056) | |
| "What survives pattern switching" | 3069 | Defines doubly misaligned cycles. Example J1.4, labelled CHECKED |
| Prop. J1.5 | prop:J15 (3071) | The status covers why pattern switching stops and the three failed repairs |
| Question J1.Q | 3084 | Open, with no conjecture. Also gives the scope limits: countably many ends; non-integrable base endorsers; installation not reached; no scripts |

**Line 3086, "What survives round 17".** This is H1 §6 as corrected by H12 §§1.7, 3. H1's "exactly one of (A), (B),
finitely additive" is reported as neither exclusive nor exhaustive. The text replaces it with "at least one of" the
following:
- (A′), which subsumes the finitely additive case;
- (B), narrowed: within finite ends and integrable bases, only along a directed cycle;
- the **new case (D)**: non-integrable endorsers at two or more worlds, or one non-integrable endorser with only
  localized integrable endorsers elsewhere, together with the referee's reason why this is a genuine obstacle.

## 2. §8.5(g), "What a cover on M_U still needs" (lines 3094–3158)

- **Line 3094.** The intro now says the text was rewritten in round 17, and Thm. H24 is added to the list of known
  worlds that do not add up.
- **"The cover as a whole" (3102), rewritten.**
  - E11/E12 are kept.
  - It adds the robust form (H10(c)).
  - It gives the list of excluded covers: E15 as a special case of H13; H12, including the installation of the D21
    world; H13; H23 with R.1; J12 (not refereed).
- **"The precise residual" (3111), new.** Class (EP) as in H12 §3. A cover in this class needs:
  1. a 2- or 3-cycle, with the consequences of Cor. H23p;
  2. the germ exchanges at X_m;
  3. per J1, no aligned order of the worlds. For a 2-cycle next to a world without ends this means that the cycle is
     doubly misaligned, with shell exchanges (J15) and Question J1.Q.

  The text states explicitly that for 3-cycles, and for 2-cycles whose third world has ends, J1 leaves "no aligned
  order" and does not analyse it further.
- **"Outside class (EP)" (3118), new.** It replaces the old (R-a)/(R-b) "open route" and the old "nearby target"
  CONJECTURE. The cases are:
  - non-integrable endorsers at two or more worlds (case (D)). The nearby target is proved for one non-integrable
    world (H12) and is otherwise open, with F12 §5.7's added condition kept;
  - countably many ends;
  - failures not of end-protected form: protection not given by ends, and non-localizable failures (A′), which include
    purely finitely additive weights.

  The "known examples" sentence gains H24, and "rounds 14 to 16" becomes "rounds 14 to 17".
- **Line 3138, lifting list, second bullet.** Added: "round 17 removes the heaviness and excludes more".
- **Line 3149, σ-finite bullet.** The extension to shadows that are non-integrable at ends is proved for one world
  (H12). It is open for two or more worlds (case (D)).
- **Line 3150, "Unprotected failures and the open route".** Replaced by "Conflict cycles, and the cases outside class
  (EP)". It covers J1.Q and the generalised question. **Precision:** J1 says that a negative answer to J1.Q would
  exclude every cover in the class. The text notes that this also needs the configurations with no aligned order
  that J1 does not analyse. It also covers the cases outside the class, and D2.C: an installation keeping an a.e.-finite
  cancellation endorser is excluded by H12, without heaviness or compatibility.
- **Line 3158, closing status.** "the open route (R-a), (R-b) are open" is replaced by the round-17 statuses and the
  new open items.

## 3. Summary for T1 (line 73)

- After item (v), three new items, with a status parenthesis:
  - **(vi)** H12;
  - **(vii)** H13, with (h) replaced by T1-correctness;
  - **(viii)** H23 + R.1, Cor. H23p, and J12/J13, leaving the doubly misaligned cycles of J1.Q.
- Added: H24 exists (refereed once).
- After "carried by base comparisons or by comparisons at another world": the robust form (Lemma H10).
- Remaining problems. "the open route … two or more worlds that fail to add up" is replaced by the residual of (g):
  - within the class, conflict cycles with no aligned order (doubly misaligned 2-cycles, J1.Q);
  - outside it, non-integrable endorsers at two or more worlds, countably many ends, and failures not of
    end-protected form.

## 4. Status table (lines 213–224)

- The E1 row now ends with "heaviness in Thm. E15 removed in round 17 (Thm. H13, Prop. HR1)".
- New block "Round 17" with 9 rows:
  - H10/H11;
  - H12 (bold);
  - H13;
  - H20/H21/H22;
  - H23/HR1 (bold);
  - Cor. H23p;
  - H24 (bold);
  - J1C/J10/J12/J13/J15 (not refereed);
  - Question J1.Q (open).
- N17.B′ row: "the open route of §8.5(g)" is replaced by "the residual of §8.5(g) (Question J1.Q and the cases outside
  the class of finitely many end-protected worlds with integrable base endorsers)".

## 5. Small consistency edits elsewhere in the file

These point to (f′) and keep earlier text from contradicting the new results.

| Line | Change |
|---|---|
| 42 | Date: "rounds 14--17". |
| 69 | Introduction, item "Worlds that do not add up": one "New in round 17" passage (H12, H13, H23/R.1, H24, J1). |
| 1592 | §8.1: one sentence on round 17. |
| 1775 | §8.5 introduction: one sentence listing round 17 and part (f′). |
| 2484 | (f) heading paragraph: "Round 17 follows in part (f′)." |
| 2877 | Status of Thm. E15: a "Round 17" note (H13, R.1, H12). |
| 2892 | "Protection and visibility": a parenthesis saying heaviness and compatibility are not needed (H12, H11). |
| 2894 | End of (f), "What a cover still needs": "round 17 narrows it (part (f′))". |
| Sources (3198, 3263–3266) | New entries for BRIEF15.md, H1_notes.md, H2_notes.md, H12_referee.md, J1_notes.md. |

## Not changed

- No statement of an existing theorem, lemma, proposition or conjecture was changed. Theorem E15 keeps its
  hypotheses. Its supersession by H13 is recorded in its status and in (f′), not by rewriting it.
- The notes and the referee report were not edited. Only the write-up and this file were written. The backup is a
  copy.
