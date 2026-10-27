# Changes, rounds 20–22 (16 Oct 2026): the fixed-point reduction

Backup: `The Contamination Triangle pre-round20.tex`, a copy of the file before this round (3705 lines). The new file has
4469 lines. It compiles cleanly with `pdflatex` run twice: 236 pages (was 197). There are no errors, no undefined or
multiply defined references, no overfull boxes and no LaTeX warnings; the only warnings are the 7 underfull boxes, as
before. Line numbers below refer to the **new** file.

Inputs, with statuses exactly as refereed:
- L1_notes + L1_referee; L2_notes, L3_notes + L23_referee; L4_notes + L4_referee (incl. Proposition R);
- M1_notes + M1_referee; M2_notes, M3_notes + M23_referee (incl. the sharper M2.6′);
- N1_notes (round-20 top part) and N2_notes Part I + N12_referee;
- R21_reduction.md (round 21, integrator's note), with its [U] tags for N1/N2 updated to "refereed once".
- P1_notes round-22 part: **not used**, except the single sentence "A totally blind two-world world has been announced
  (P1, round 22, under review)" at Question Q_N2 (§8.6(j)), and a Sources note saying the file now begins with that
  note.

## Conventions

- Theorem environments carry no names; note numbers (L4.1, M2.6′, ...) appear only in status lines and prose.
- `\coloneqq` throughout; `grep ':='` finds nothing.
- TERMFIX_RULES.md check: the only hit of the grep is line 321, the existing "Earlier terminology" paragraph (allowed).
  "Forced pair", "forced KKM", "forced endorser", "forced cone" mean forced by competitiveness (logical use).
  "available" (L3, M3 notes) was reworded to "in the advice range"; one "availability result" reworded.
- Statuses: "proved (note); confirmed (referee), one reader", every requested repair incorporated. Marked as proved in
  a referee report (one reader): Prop. L4R (L4_referee "Proposition R"), Cor. L4V, Lemma L17z (L1.7⁰), the sharp
  second sentence of Thm. M26 (M2.6′), the charge form of Thm. M19, Cor. M19p(b), the M1_referee §4.3 rigidity
  remark, Cor. N26(d) (the three-vertex nearby result), the restricted strong form and weak inequality of Prop. M32.
  CHECKED: case (II) audit, Lemma L17, Thm. L1C, Prop. M39 (with fixable gap (ii)). R21's four inferences ((RL)⇒(NC),
  location trichotomy, interval ⇒ joint blindness in E, two-sided shadow sketch) are "proved in R21, unrefereed".
- No new mathematics; no assumption added. Notes, referee reports and scripts were not edited.

## Notation (renamed to avoid clashes; content unchanged)

| In the notes | In the write-up | Reason |
|---|---|---|
| L4's (B1) | (OB) | (B1) is a note name |
| L4's D_m, D^ν; 𝒩_k | Θ_m, Θ^ν; 𝔑_k | as in round 19 (K3 block) |
| L4/N1/N2's Λ_k | Λ_k = Λ_∅ of world k (Thm K31(c)) | consistent with round 19 |
| K3_referee's (Q1) | Prop. KQA(a) | (Q1) is a question in §8.1 |
| L4's w₂, w₃ | w₁₂, w₁₃ (write-up crossing names) | §2.3 convention |
| L3's hypothesis (V) | (Pay) | (V) clashes with configuration V |
| L3's (N) in L3.5 | (N_∞) | (N) is K3's class |
| L3's VB with Ψ̃ (referee) | VB′ | referee's repair |
| M1's (W1)–(W4) | (Sh1)–(Sh4) | (W1)–(W4) used in §8.4(b) |
| M1's R⁰_k | M ∖ E_k(T1) | R⁰_i is the improvement region of part (f′) |
| M1.10's e_θ | f_θ | e_θ is N2's edge field |
| M2's 𝔉𝔏 | 𝔚^f_1 | 𝔉 used elsewhere |
| N1's (R), (D) | (rig), (dbl) | (R), (D) used elsewhere |
| M3's Γ_k (ladder), s_k, w_k | Ld_k, r^s_k, r^w_k | Γ used for credal pairs; s is the K′ parameter |
| M3's (C2), (C3) | (TS), (PC), (NS) and the cluster clause | named directly |
| R21's (S), (V0), (V+), (P0), (PD), (E), (X), (GS), (GL), (GnAv-nd), (GnAv-d), (G0); (int), (edge), (vtx) | sans-serif \cfg{S}, \cfg{V0}, ... (macro `\cfg`, line 39) | (S), (E) are axioms |
| R21's θ(A*) | I* = {p_i/(p_i+p_j) : p ∈ A*} | θ(q) is L1's q₂/(q₂+q₃) |

## 1. New §8.6 "The fixed-point reduction" (lines 3612–4329)

Introduction (3612) and Notation (3614): rounds 20–22, the eleven notes, six referee reports, R21; citation convention
for N1/N2 (round-20 parts); P1 not used; notation list (J_l, W_l, c^{ij}_T, Y_l, 𝔚_k, 𝔑_k, (NC), strongly (M1),
maximal endorser, Λ_k, V_k, generalised shadow, c^ν, Gap_t, d_t, (γ₀), A(c), edge models, e_θ, E^{θ,±}, joint blind set).

- **(a) Hahn–Banach fixed point (3631):** Lemma L40; **Thm. L41** with the referee's hypothesis c ≠ 0 a.e. for the
  every-B_q clause and the counterexample without it; the withdrawn "iff/exactly when" overstatements; **Cor. L42**
  (second proof of M0closed(b); status K31 + H11, each read once; fullsupport needed for the CPaU(b) remark);
  Props. L43, L44 (item (c) moved to a reading), L45.
- **(b) One blind world (3688):** (OB); Lemma L46; Prop. L47; Lemma L48 with the strengthened hypothesis S∩N null;
  Thm. L49 with (I₂)/(I₃) in the strengthened form; **Prop. L4R (Proposition R)** excluding configuration (I), with the
  withdrawn "single obstruction" and "first computation"; case (II): what it looks like and the CHECKED audit with the
  referee's additions (a)–(d); **Cor. L4V** (only p* = e₁, Λ₁ ⊋ E₁(T1) ∩ M).
- **(c) Forced fixed point (3739):** (RL), forced/limit pairs; Lemma M21 (wording fix); Thm. M24; Prop. M25;
  **Thm. M26 with the sharper M2.6′** (only configuration V); corrections of "L4.9 unrefereed" and "Q_M2 answered
  no"; Prop. M27 with the "two places, not one" correction.
- **(d) Weak fields (3774):** **Thm. L1** (Q_A: No, modulo L1.7 and L1.C); Bayes structure ("when", not "exactly
  when"); Prop. L12; Lemmas L13, L16; Thm. L1A ((a) proved; (b) on F₁ modulo L1.7, two repairs); **Lemma L17z
  (L1.7⁰)**; Lemma L17 (gap and fix); Cor. L1B relabelled "modulo L1.7", sharpened; Thm. L1C (CHECKED, row repairs);
  cross-check with (I); Conj. L1D with the "verbatim" gap.
- **(e) T1-shadow (3847):** Thm. M11; Cor. M11′ ("strict signs exactly in UVN" corrected; "CA field alone"; headline
  restricted); Prop. M12 (K₁ ∩ [e₁,e₂] = {e₂}); Lemma M110; Prop. M111 (reading corrected); Lemmas M13, M14;
  Cor. M15 (wording fix); Lemma M16 (local form); **Thm. M17** with scope; Cor. M18 (+ referee's second route);
  Thm. M19 + charge form; Cor. M19′ with the referee's interval dichotomy replacing the "two-sided tie shell";
  (Sh1)–(Sh4) and the attempts (readings labelled); **Q_M1 answered No**, "equivalently" not an equivalence.
- **(f) N1, N2 (3952):** Thm. N21 (vertex-of-face and totally-blind caveat; M2 setting); Cors. N22, N22′;
  Lemmas N10, N11 (strict (G) not used); Thm. N23; Cor. N23′; **Thm. N12 (edge dichotomy)**; Cor. N13;
  Thm. N24 (only the source forced blind in (int_i)); Thm. N25 ((a) wording; (b) one facet per side);
  Lemma N25′; **Cor. N26 with N2.6(a)'s "equivalently" removed as wrong and the nearby result (d)**; Thm. N27
  ((c) one-sided); Lemma N14 (reindexed by the chain), Thm. N15, Cor. N16, Thm. N17; **Conj. N1C: N1.C false as
  stated, the counterexample K = co(K′ ∪ {e₁, (v₁+v₂)/2}) recorded, restricted form conjectured**; Question Q_N1
  ("failing (NC)", strengthenings).
- **(g) L2 (4113):** **Thm. L21, Thm. L24 (K3.C false; Q_K3 Yes in two worlds)**; Prop. L25 ((Loc), not (N));
  Cor. L26; Conj. L2C; three-world analysis and Q_L2; consistency with N1/N2; L2's non-refinement via L3.4 + N2.2.
- **(h) L3 (4142):** Prop. L31 (NUMERICS of c(ε) corrected to ≤ 0.0068, 0.029, 0.031, 0.011); Prop. L32;
  **Thm. L33 for VB and VB′** ((a) repaired; open-edge clause of (c) removed); **Thm. L34 (vetoes cannot be paid)**
  and its VB application; remark on (Imp) on M_U; Thm. L35 with the two hypotheses; Prop. L36 with R″; nearby result.
- **(i) M3 (4191):** ladders and "regular" flagged as a definition; Lemma M30; Prop. M32 (witness, restricted strong
  form, weak inequality; strict form vacuous on (Av)-domains); Thm. M34; **Cor. M35 (Claim B2.0 proved, with the
  identification)**; gm audit (CHECKED, not load-bearing); Lemma M36 (stronger step 3); Lemma M37; Prop. M38;
  Prop. M39 (CHECKED, gap (ii), (Av) apparently unused); **Thm. M310, Cor. M310′**; Lemma M311 restated with the
  doubly-blind hypothesis; Conj. M3C with the completion; Q_M3; the referee's ladder conjecture.
- **(j) Reduction theorem (4261):** in words; case variables; **Theorem R21 (thm:R21, line 4267)**, Part A
  (S, V0, V+, P0, PD, E, X) and Part B (GS, GL, GnAv-nd, GnAv-d; G0 closed); proof sketch (case tree);
  status (weakest inputs; N1/N2 inputs now refereed once); per-configuration structure, single open question and
  effect of each answer (Q_S; Q_N2 / Q^(3)_N2 with the flag; Q_V+; Conj. L1D rigid form; Q_N1 restricted;
  Q_GS; Q_M3(a); Conj. M3C; GnAv-d unaddressed); how earlier questions sit in the tree; unaddressed branches,
  fixable gaps, unproved reductions. The P1 sentence is here.

## 2. Summary for T1 (line 75) — rewritten

Now organised around Theorem R21: what is excluded; the fixed point and blind sets; the seven configurations with
their questions; what is closed; the T1-shadow and the ranking-level tools; Q_A answered No; L2 and VB; statuses;
the earlier necessary conditions (rounds 13–19) compressed, with a pointer to §8.5(g) and the remark that they are not
separate configurations; off the U-domain (gm; M3.10/M3.10′; Claim B2.0 proved; Part B configurations).

## 3. §8.5(g) "What a cover still needs" (line 3531) — rewritten to match R21

- The numbered list is now: (1) a world that does not add up (+ L21/L24 example); (2) exactly one of the seven
  configurations, with what is closed; (3) one open question per configuration and what the answers do; (4) how the
  round-19 classification fits (certificates, Λ_∞ with L24/L25/Cor L26 and Q_A No, localizable worlds: the
  "if Q_K3 = No" exclusion of minority mass is void; sheltering/ends are not separate leaves).
- Property bullets: new "Rounds 20–22" bullet. Cover-as-a-whole: new round 20–22 exclusions bullet. Known examples:
  L21, VB, the shadow. Three-world questions: header "14 to 22"; Q_K3/Q_A bullet updated; new bullet with the R21
  questions and the other open items (N1C restricted, L2C, L3.6(b) residual, L3.5 without (N_∞), Prop. M27 residual).
  Off the U-domain: Claim B2.0 proved; (Av)-domains closed for adding-up rankings (CHECKED); the p* ∉ E branch closed
  on (Av)-domains; the general-domain configurations. Case (D) bullet: minority-mass exclusion marked unavailable.
  Status paragraph extended.

## 4. Other edits

| Line | Change |
|---|---|
| 39 | `\cfg` macro |
| 43 | Date: rounds 14–22 |
| 69 | Introduction item 6: round-19 sentence on the second kind updated (L24) |
| 71 | Introduction: new item "The fixed-point reduction" |
| 122 (table) | M0closed(b) row: second proof Cor. L42 |
| 199, 213 (table) | Cor. B22, Cor. D17 rows: Claim B2.0 proved |
| 231, 234, 235 (table) | patch theorem row (Q_K3 Yes); K3C false; Q_K3/Q_A answered |
| 244–268 (table) | new "Rounds 20–22" block (24 rows) |
| 269 (table) | N17.B′ row: residual list updated |
| 1508 | Thm. M0closed status: round-20 second proof |
| 1637 | §8.1 remaining target: round 20–22 sentence |
| 1820 | §8.5 intro: rounds 20–22 sentence |
| 2811, 2849 | Cor. B22, Cor. D17 statuses: Claim B2.0 proved (Cor. M35) |
| 3262 (Cor. K35p status) | sharpening: hypothesis false (Q_K3 Yes) |
| 3300, 3328, 3330 | Q_A answered No; K3C false; Q_K3 Yes in two worlds |
| Sources | BRIEF17; P1 note on the round-22 part; L1, L1 ref, L2, L3, L23 ref, L4, L4 ref, M1, M1 ref, M2, M3, M23 ref, N1 (round 20), N2 (round 20), N12 ref, R21 |

## Not changed

- No statement of an existing result was changed; only statuses and pointers (Q_A, Q_K3, K3C, Claim B2.0, B22, D17,
  K35p sharpening, M0closed(b)) were updated where a refereed round-20 result bears on them.
- Notes, referee reports, scripts and P1 were not edited. Only the write-up, its backup copy and this file were written
  (plus pdflatex's own output files in writeup/).
