# Changes, round 19 (16 Oct 2026): J1 referee, K1, K2, K3 and their referee reports

Backup: `The Contamination Triangle pre-round19.tex`, a copy of the file before this round (3274 lines). The new file has
3705 lines. It compiles cleanly with `pdflatex` run twice: 197 pages. There are no errors, no undefined or multiply
defined references, no overfull boxes and no LaTeX warnings; the only warnings are the 7 underfull boxes, as before.
Line numbers below refer to the **new** file.

Inputs, each refereed once, with statuses exactly as refereed:
- J1_referee.md (on J1_notes.md, already in the write-up);
- K1_notes.md + K1_referee.md;
- K2_notes.md + K2_referee.md;
- K3_notes.md + K3_referee.md.

## Conventions

- Theorem environments carry no names. Note numbers (K3.1, R.2, ...) appear only in status lines and prose.
- `\coloneqq` throughout; `grep ':='` finds nothing.
- TERMFIX_RULES.md check: the only hit is line 294, the existing "Earlier terminology" paragraph (allowed). "Forced
  comparison" and "forced vector" (K2) mean forced by competitiveness, a logical use.
- Statuses: note results "proved (note); confirmed (referee), one reader", with every requested repair incorporated.
  Results first proved in a referee report are marked so: Theorem R.2, Corollary R.3 (J1_referee), Proposition R6.2
  (K2_referee), the necessary conditions for Q_A (K3_referee), the K3.4 extensions, the sharpening under Q_K3 = No.
  CHECKED and NUMERICS as labelled by the notes and referees.
- No new mathematics; no assumption added. The notes and referee reports were not edited.

## Notation (renamed to avoid clashes; content unchanged)

| In the notes | In the write-up | Reason |
|---|---|---|
| K3's class (S), (S_int) | (Loc), (Loc_int) | (S) is the axiom of closed choice (referee's request) |
| K3.7 items (α), (β), (β′), (γ) | (a), (b), (b′), (c) | (γ) is the property in item (a) (referee's request) |
| K3's (E_b) | (EP_b) | (E) is an axiom in §2 |
| K3's patch conditions (P1)–(P3) | (Y1)–(Y3) | P1 etc. are note names |
| K3's 𝔚, 𝒩 | 𝔚, 𝔑 | 𝒩 is used for shadow families |
| K3's localizing families D, D^ν, D^∞, D̂; blind sets Λ, Λ_D | Θ, Θ^ν, Θ^∞, Θ̂; Λ_∅, Λ_Θ | Θ as in round 17; Λ = Λ_Θ for the empty family |
| K1's T(Y), m_t | Cost_t(Y), Cost_t underlined | T is the target; m is a depth |
| K1's Π^k(a), D(a) | 𝓔^k(a), 𝓔(a) | as for J1 in round 17 |
| K2's 𝒞, Ψ, C, 𝒦, (1.1) | 𝒞_±, 𝒴, coefficient vectors a, 𝒦_𝒴, (K2) | 𝒞/C/Ψ are used elsewhere |
| K2's (E), (P), (Cert) | (endorse), (pair), (cert) | (E), (P) are used elsewhere |
| K2's SPREAD gap δ, trade ratio η | η, η′ | δ denotes vectors |
| J1_referee's Γ, Γ_mis, (F), (B) | H⃗, H⃗_mis, conditions (a), (b) of Thm. JR2 | as in round 17 |
| K3's class (N), K3.C, Q_A, Q_K3; K1's (EP∞), (Al∞), J1.Q′∞ | unchanged | no clash |

## 1. Part (f′): the J1 block corrected (J1_referee)

- **Line 2914**, (f′) introduction: J1 now refereed once; what the referee found.
- **J1 header** and every J1 status (lem:J1C, lem:J10, J1.1, thm:J12, cor:J13, prop:J15): "proved in a note, not yet
  refereed" → "proved (J1); confirmed (J1_referee §…), one reader". J1C status adds the referee's remark on the
  uniform bound.
- **Cor. J13(a)**: the referee's stronger form (any finite 𝒮₂); "for any t ∈ I_ψ" → "the configuration is inconsistent
  with (EP)"; proof of (a) written out (§4.1).
- **Cor. J13(c)**: one-line gap closed in the proof (T1-correct S at i is case (i)); status records it, defines
  "shadowed" for (b), and notes "for every t" adds nothing.
- **Example J1.4**: radii caveat (θ₀ small enough to lie in U ∩ O and a region of constant T1 advice); "escapes J12"
  holds when 𝒮_l = ∅ and W is the only end; NUMERICS j1ref_geometry.
- **Prop. J15**: same one-line gap closed in the proof; consequence (i → j misaligned); the referee's (γ) by-product.
- **Question J1.Q (line 3102)**: wording corrected ("every tuple of integrable base endorsers, every t, every large m";
  "l incident to no arrow" for 𝒮_l = ∅). Explicit corrections (1)–(4): the too-broad ψ; the replacement of 𝒮_l = ∅;
  **the closure claim is unproved: a negative answer closes only case (R-i)**; J1 §0's "no cycle survives one aligned
  arrow" proved only for (R-i) and pure 3-cycles. Scope limits: pointer to K1's countable forms.
- **New block (line 3104)**: definition of aligned/misaligned arrows; **Theorem JR2** (R.2, thm:JR2, 3106);
  **Corollary JR3** (R.3, cor:JR3, 3119) (a)–(c), NUMERICS j1ref_orders (10 digraphs); **the residual (R-i)–(R-iii)**
  (3132), with (R-ii) CHECKED; **Question J1.Q′** (3138).
- **"What survives round 17", case (B)**: round-19 sentence (countable ends: only cyclic non-aligned configurations,
  K14/K15; finite: (R-i)–(R-iii); general sheltering is the patch-theorem residual). Case (A′): round-19 parenthesis
  (by K31(c)–(e) every world that adds up is (Loc_int), so (A′) = certificate or (N)).

## 2. New part (f″) of §8.5 (lines 3148–3502), before (g)

Introduction (3148): BRIEF16, three notes, four referee reports, statuses, order of the blocks (K3, K2, K1, the order
of the argument of (g)).

**K3 (3150–3303)**: setting (bounded endorsers, Yosida–Hewitt, per-world modes, (NC), (Loc), (Loc_int), (EP_b), (N),
ratio certificates); **Thm. K31** with (NC_𝔚) explicit for (c)–(f), "only Λ_∞ canonical; Θ̂, ρ_∞ not", the referee's
observation that (N) ⊆ {Λ_∞ non-null} may be strict, and the reading; **Prop. K32**; **Thm. K33** (tilt world, every
axiom but closed world-1 sections; **credited as Q12_referee N3 completed**; NUMERICS); **Lemma K34** with the referee's
extensions and the **wording fix** (only the contrapositive of (b) is stated; the "not pairwise meeting" and "pairwise
disjoint small targets" readings withdrawn); **Thm. K35** (patch theorem), **Cor. K35′** ("bounds", not "is"; residual
sheltering / infinite minority mass; **referee's sharpening: under Q_K3 = No, a cover needs an (M1) world or
sheltering**); **Lemma K36**; **Lemma K37′** (NUMERICS with the referee's corrected diagnosis); **Thm. K37** (items
relabelled); **Question Q_A**; **Prop. KQA** (referee's necessary conditions (a)–(c); where M0closed(a) breaks, a
reading); **Prop. K38**; **Conjecture K3C** with placement and **the F1.4 gap** (F14 does not exclude chain-free ratio
certificates; only those with g bounded below on a fixed set); **Question Q_K3**, with the note that settling (M2) for
T1 also needs Q_A for one exceptional world.

**K2 (3305–3423)**: setting and (K2); divisibility; **Thm. K21**; forced comparisons; **Prop. K22**; **Cor. K22′ in
ρ_j form**; remarks (D2 remark not re-derived by the referee); **Thm. K23** with the referee's precisions; **Thm. K24**
with **the crossing-needs-interleaving fix**, the H1 case (A) inference replaced by H12, and (e) read through (pair);
**Thm. K25** (scheme; every axiom; referee's small-trade addition; interior indices); (SPREAD)/(ADJ); **Thm. K26**;
**Prop. K26a** (**only SPREAD proved for Brier; ADJ numerical**); **Prop. KR62** (R6.2, proved in a referee report,
consequences (i)–(iii)); **Conjecture K26′** with the referee's nearby target; **Lemma K27**; "What K2 gives for T1"
with the **overstatements removed** (the general "single obstruction in words" and "what a T1 cover must do" are
stated as holding only for K25-type decorations / conditional on K26′ and are not asserted); Question Q-K2.

**K1 (3425–3502)**: class (EP∞) with **the purely-finitely-additive wording fix**; standing facts; **Lemma K10**
(K1.0, K1.0′); **Lemma K11** (K1.1, K1.1′); **Thm. K12** (attribution of K14/K15 corrected); canonical triple; **Cor.
K13** (hypothesis at a₀; "some depth vs every depth" gain withdrawn); **Thm. K14**; (Al∞); **Thm. K15** with **the
uniform-depth fix to the sufficient condition** (pairwise reading false; J1.3(b) and R.2 case 4 need the uniform
reading; R.2/R.3 not extended); **the referee's countable-conflict configuration without arrows** (CHECKED);
**Thm. K16** (a)–(c) as **necessary condition and exclusion test; the status states plainly that the "iff" with K1.Q
is tautological and K1.Q is the class question restated**; the referee's untested selection-level test; failed
repairs; **Question J1.Q′∞** (3502), the residual.

## 3. §8.5(g) rewritten (from line 3504)

- **"What a cover on M_U still needs"** now states, in order, as a numbered list: (1) a cover needs a world that does
  not add up (with the known examples); (2) by K31 such a world carries a certificate, or has a non-null Λ_∞, or is
  (Loc_int); (3) certificate: rigid, unforced comparison (K21, K22, K22′), the Brier-type scheme empty (K25, K26, R6.2),
  two-world link to Q2N (K23), Q-K2, K26′; (4) non-null Λ_∞: open (Q_K3), not excluded without closed sections (K33),
  rigid shape and Q_A next to two integrable worlds (K37), K3C in two worlds; (5) localizable: by the patch theorem a
  cover needs sheltering or infinite minority mass, the latter excluded if Q_K3 = No (referee); sheltering by ends is
  J1.Q′∞ (countable) and J1.Q′ / (R-i)–(R-iii) (finite). The property bullets follow unchanged.
- **The cover as a whole**: J12 bullet updated (refereed; JR2, JR3); three new excluded-cover bullets (countable ends;
  patch; forced-only certificates).
- **The precise residual** → "of the end-protected classes": item (3) rewritten with (R-i)–(R-iii) and J1.Q′; new
  paragraph on class (EP∞) (K14, K15, K13, K16; J1.Q′∞).
- **Outside class (EP)**: case (D) bullet gains the patch theorem; countably-many-ends bullet narrowed per K1_referee
  §9; failures-not-of-end-protected-form bullet: K32, (A′) = certificate or (N), adding-up worlds are (Loc_int).
- Known examples (+K33); "rounds 14 to 17/16" → "14 to 19"; σ-finite bullet (+K35); conflict-cycle bullet rewritten
  (J1.Q, J1.Q′, J1.Q′∞; closure claim unproved); new bullet with Q_K3, K3C, Q_A, Q-K2, K26′; closing status extended.

## 4. Summary for T1 (line 73)

- After "So a cover needs a world that does not add up": the round-19 chain, in the same order as (g): K31's three
  kinds; certificates (K21, K22′, K25, K26, R6.2); non-null Λ_∞ (Q_K3, K33, Q_A); localizable (patch theorem: sheltering,
  i.e. J1.Q′ / J1.Q′∞ for ends, or infinite minority mass, excluded if Q_K3 = No). Status parenthesis.
- (viii) updated (R-i)–(R-iii), J1.Q′; new (ix) (K14, K15, J1.Q′∞); J1 statuses updated.
- Remaining problems: the old residual sentence replaced by the round-19 questions.

## 5. Other edits

| Line | Change |
|---|---|
| 42 | Date: 16 October 2026, rounds 14–19 |
| 69 | Introduction: J1 refereed; "New in round 19" passage |
| 223–243 | Status table: J1 row updated; new "Round 19" block (18 rows); questions row J1.Q/J1.Q′/J1.Q′∞; N17.B′ row residual updated; Round 17 header shortened (to fit the line) |
| 219, 3020 | "J1 (not yet refereed)" → refereed once in round 19 |
| §8.1, §8.5 intro, (f) heading, end of (f) | one round-19 sentence or pointer each |
| Sources | BRIEF16, J1_referee, K1_notes, K1_referee, K2_notes, K2_referee, K3_notes, K3_referee; J1_notes entry updated |

## Not changed

- No statement of an existing result was changed except where a referee's repair applies to it (Cor. J13(a), its
  proof, and the proofs of J13(c) and J15), as the status-convention paragraph of the write-up requires.
- Notes, referee reports and scripts were not edited. Only the write-up, its backup copy and this file were written
  (plus pdflatex's own output files in writeup/).
