# Changes, audit of 15 October 2026 (audit16)

Backup: `The Contamination Triangle pre-audit16.tex` (2931 lines, a copy of the file before this audit). The new file has
3046 lines. It compiles cleanly with `pdflatex` run twice: 156 pages (previously 146). There are no errors, no undefined
or multiply defined references and no overfull boxes. The only warnings are 7 underfull boxes, as before. Line numbers
below refer to the **new** file.

Inputs: F1_notes.md, F2_notes.md, F12_referee.md. Statuses are as F12_referee assigns. Every repair the referee lists
(§6, items 1–9) is applied where it touches the write-up.

## Conventions

- Theorem environments carry no names. Note numbers (F1.3, F2.4, ...) appear only in status lines.
- `\coloneqq` is used throughout; `grep ':='` finds nothing.
- The terminology check (TERMFIX_RULES.md) finds only the existing "Earlier terminology" paragraph. One old use of
  "forced trades" (in the status of Lemma E13) was removed with the sentence that contained it.
- No new mathematics. New statements are F1/F2 results as refereed, with the referee's repairs included.
- Credit for the refutation is given as "observed by an external auditor; proved in note F1".

## 1. Conjecture conj:sigmaB refuted (F1.2, F1.3, F2.4; refereed once)

- **Line 2378 (lead-in).** "The nearby statement that Theorem D21 does not refute is the following" now reads: proposed in
  round 16; **false** (Theorem F13); kept and marked as refuted because the notes refer to it.
- **Conjecture conj:sigmaB (line 2379).** The statement is unchanged and not deleted.
- **Its status (line 2382), rewritten:**
  - It is now headed "REFUTED (15 October 2026)". The counterexample is D21, under the total-cost and cancellation
    readings, proved in F1 and by a second route in F2 Prop. F2.4. The credit line is included.
  - The false round-16 sentence "blows up only as x→1, … near the boundary ray of U on the side of e₂, and is bounded on
    every closed subcone of U" is quoted and corrected. The end also contains R₊(1,0), which is interior to U. The same
    slip is noted in D2_referee2 §3.3.
  - Added: whether the conclusion holds depends on the selection (it holds in D2′_B).
  - Added: pointers to the repairs.
  - The "For T₁" localisation paragraph is kept and redirected to Conj. F1Cp, subject to its caveat.
  - The final clause "…not this conjecture" is removed, since the conjecture is now false in two worlds.
- **Prop. D2sigma "Reading" (status, line 2377).** Both end rays are now named, as F12 §6 item 9 asks: R₊(1,0) (interior,
  approached from M⁺) and R₊(−α′,1−α′) (∂U, approached from M⁻). Added: ρ is integrable on compact subsets of M but not
  near R₊(1,0). The statement of the proposition is unchanged, because it is correct.
- **New block after the conjecture (lines 2384–2472)**, "Audit of 15 October: Conjecture sigmaB is false, and nearby
  systems". It contains:
  - The two hosts (A = path of Thm C21; B = the two-phase path).
  - The readings of endorsement: total cost and cancellation, and property (R). The both-finite reading is trivial via
    |h|⁻² and is therefore not the conjecture's reading.
  - **Lemma lem:F11** (F1.1): the geometry of the end; 1/(1−x) is not locally integrable on U; host B's end lies on ∂U only.
  - **Theorem thm:F12** (F1.2): next to an additive world, every σ-finite endorser is a nondecreasing function φ(x).
  - **Theorem thm:F13** (F1.3): in D21, σ-finite endorsers have ∫^1φ = ∞. None is finite on compact subsets of U.
    σ-finite endorsers exist, and so do non-σ-finite ones. Hence conj:sigmaB is false for n = 2.

## 2. F1.4, Cor. F1.5, and the systems D2′_A, D2′_B (refereed once)

- **Theorem thm:F14** (F1.4): with sources and targets in a fixed c_{b₀}, certificates cost at least θ > 0 next to an
  additive world. The scope is stated: it uses Cor. SR at world 2, and the case where both worlds are non-additive is open.
- **Corollary cor:F15** (F1.5): targets in a compact K ⊂ U with h₂ ≤ −c|h| on K ∩ M⁺ carry no certificate.
  - The status marks the last sentence (accumulation at R₊(1,0)) as **a necessary condition only**, per F12 §3.
  - Host-B chains admit no certificate with targets in a compact subset at all.
  - F1.9 is mentioned together with the referee's repair of its finiteness step.
- **Definition paragraph for D2′_H** (before Thm F16). It ends with the referee's wording point: only the generators and
  the protected set W are confined, and world 1's base order acts on all of M.
- **Theorem thm:F16** (F1.5′, F1.6a/b, F1.6): D2′_A and D2′_B are full systems in which world 1 fails SP^reg, of type
  (M2). The confinement clause reads "every generator source and target, and the protected set W" (F12 §4.4, §6 item 3).
- **Theorem thm:F18** (F1.7, F1.8):
  - Bounded endorsers do not exist.
  - σ-finite endorsers blow up exactly at the chain's far end. On host A no endorser is finite on compact subsets of U;
    host B satisfies the conclusion of conj:sigmaB.
  - σ-finite and non-σ-finite endorsers both exist.
  - The status drops F1's unproved parenthetical (F12 §4.5, §6 item 2).
- **Conjecture conj:F1Cp** (F1.C′, local integrability on M). Its status:
  - lists what satisfies it;
  - gives the two-world equivalence with σ-finiteness, and F1.C;
  - carries the **referee's caveat** (F12 §4.7, §6 item 4): the evidence is two-world only, and its use for T₁ depends on
    a location result for ends, i.e. on (Nest_e).
- **"The a.e.-finite target"** paragraph (F2 §2.3) carries the **referee's remark on the reading** (F12 §5.2): read
  endorsement in the cancellation form, or require finite cost of the left-hand model. Otherwise endorsement can be
  vacuous (∞ ≤ ∞).

## 3. Scope of E1 (per F2 and F12 §5)

- **E1 block header in (f) (line ~2701).** "not yet refereed" is replaced by: proved in E1, audited in F2 (exact
  hypotheses, corrected scope), audit refereed once. It notes that Prop. F21 is proved in F2.
- **Thm E11 status.**
  - Hypotheses added: (a) uses no integrability; (b) uses finite ψ.
  - The "which worlds" remark is corrected. Putting every failure at the third world needs an admissible completion
    (ν_i, aρ_j, bρ_k), which is not automatic (F2 §1.3, F12 §5.1).
- **Thm E12 status.** Re-derived and confirmed; it needs no hypothesis on any world beyond (H_U).
- **Lemma E13 status, rewritten.**
  - Hypotheses: (a) uses only the comparisons out of T₁. The a.e.-finite relaxation is valid only with the cancellation
    reading or finite ρ_kμ(E_kT₁) (F12 §5.2, §6 item 6).
  - The false sentence "an end … can sit only … at limits of near-unanimous problems" is replaced by what is proved: ends
    are eventually T₁-correct at the protected world. A collar of ∂U ∩ {h₁ < 0} is T₁-correct (F2.1). Under (Nest_e) on
    both edges, ends lie at the near-unanimous boundary or at ∂U ∩ {h₁ < 0} (F2.3).
  - The two-world corroboration is noted (the D21 end contains a ∂U ray; D2′_B has its protection at ∂U).
- **New Proposition prop:F21** (F2.1, F2.2, F2.3), after Lemma E13.
  - (a) The ∂U collar, automatic for ends in a collar inside {h_i < 0}.
  - (b) The location of ends under (Nest_e) on both edges, with all of F2.2's hypotheses written out (positive, a.e.
    finite densities at worlds 2 and 3 endorsing the edge comparisons, with the reading repair), as F12 §5.6 requires.
  - The status records: the Hausdorff-convergence import is CHECKED; an end approaching ∂U ∩ {h_i = 0} is not covered;
    and what is not excluded without (Nest_e).
- **Lemma E14 status.** It is location-free and automatic at ∂U ∩ {h_i < 0} (F2.1). Moving protection to ∂U does not make
  it visible (F2 §2.1). The ∂U ∩ {h_i > 0} case is excluded by E13(a) or F21(b). NUMERICS from f2py were added.
- **Thm E15 status.**
  - Exact hypotheses: (h) is joint, not a property of world i alone; admissibility is proved in step (1); the theorem is
    location-free, does not use E13, and uses integrability.
  - It excludes exactly the covers in which every world is an end-protected decoration with integrable, jointly
    end-heavy base densities. When it does not apply is stated.
  - E1's "unconditional general form" holds only when every end is eventually T₁-correct.
  - "Additive near-cover plus modifications falls under this theorem" is qualified: when (b) and (h) hold jointly.
  - Wording note: the brief said "jointly admissible". Admissibility of the triple is a conclusion of step (1), not a
    hypothesis, so the text says "integrable, jointly end-heavy base densities".
- **Prop E16 status.** It is two-world only. F13 concerns base and generators together, while E15 needs a base endorser
  only, so F13 does not touch E15 (F2 §2.3).
- **"The obstruction: protection and visibility exclude each other"**, renamed "Protection and visibility", and rewritten:
  - "it cannot be moved off the near-unanimous limits" is replaced by the proved location statements.
  - The supersession of D2 §5 is restricted to covers meeting E15's hypotheses.
  - "Conjecture D2.C does not bear on T₁" and "every installation … is excluded or inert" are marked as overstated (F2
    §1.2).
- **"What a cover still needs" (end of (f)), rewritten** per F12 §5.7:
  - The unendorsed comparison is at *some* world, which may depend on ν and t, and it is automatic under (H_U).
  - At an end-protected world with T₁-correct ends, after reweighting, any unendorsed comparison there is a base
    comparison.
- **§8.5(f) heading paragraph.** "the mechanism … cannot carry a cover of T₁" is restricted to covers by end-protected
  decorations with integrable, jointly end-heavy base densities. The audit status is added.
- **Part (e) "Consequences" (end).** "Part (f) shows … the mechanism cannot carry a cover" is restricted in the same way,
  and "other installations are not excluded" is added.

## 4. B3

- The write-up already stated B3.2 correctly. Cor. B32, the status of Conj. B3C, and the (g) bullet "Total worlds" were
  all conditional. The overstated sentence is in the roundreport, which is not edited here.
- To guard against the overstatement, two clauses were added:
  - Summary for T₁, item (iv): "that it cannot be total at all would follow from Conjecture B3C, which is open".
  - (g) bullet "If it is total…": "Only this is proved; that such a world cannot be total at all would follow from
    Conjecture B3C, which is open."

## 5. §8.5(g) "What a cover on M_U still needs" (F2 §4.3 as corrected by F12 §5.7)

- **Intro sentence.** It now says that D21's end contains R₊(1,0), so no endorser is finite on compact subsets of U
  (Thm F13), and that Thm F16 gives two more examples.
- **The per-world list.**
  - The E1 bullet ("not of the type of Theorem D21 …; its ends … sit only at near-unanimous limits") was removed from
    the per-world list, because E15 is a statement about the whole cover.
  - It was replaced by a new paragraph, **"The cover as a whole"**:
    - E15 with its exact scope;
    - E11(a),(b): for every admissible ν, an unendorsed dominator comparison at *some* world j (which may depend on ν
      and t), automatic under (H_U), so not a restriction on one world;
    - the constraint on an end-protected world with T₁-correct ends: base comparisons not all ν′-endorsed, a constraint
      only when the failures must sit there.
- **New paragraph "The open route".** It gives (R-a) and (R-b) with their labels and what is not covered. It adds the
  CONJECTURE nearby target, with the referee's added condition that E1.1(b)'s cost differences on C △ B_t be finite.
- **(R2) item.** "that form is Conjecture sigmaB" is replaced by: false (Thm F13); the M-form is Conj. F1Cp.
- **Lifting list, second bullet.** The σ-finite analogue is false. The M-analogue is open. The E15 exclusion is
  restricted. "Not yet refereed" is updated.
- **Lifting list, third bullet.** The E12 status is updated.
- **Three-world bullet "σ-finite endorsement", rewritten.** It covers: sigmaB false; F1Cp open with the (Nest_e)
  caveat; the a.e.-finite target with the reading remark; F1.C; and the extension of E11/E15 needed for T₁.
- **Three-world bullet "Unprotected certificates".** It is renamed "Unprotected failures and the open route" and points
  to (R-a), (R-b). "By Theorem E15 it [D2.C] does not bear on T₁" is replaced by the conditional statement.
- **Closing status line of (g).** "Conjecture sigmaB … open" is removed. The E1 status and an audit summary are added.

## 6. Introduction, Summary for T₁, table, other places

- **Line 42.** The date line now adds "audit of 15 October".
- **Line 69 (Intro, item "Worlds that do not add up").**
  - "so the σ-finite form of N17.B′ is open (Conj. sigmaB)" is replaced by the refutation, with credit, and Conj. F1Cp.
  - One sentence on F12, F14/F15, F16/F18 was added.
  - "so that mechanism cannot carry a cover of T₁" is replaced by the exact E11/E14/E15 content and the audit status.
- **Line 73 (Summary for T₁).**
  - "σ-finite form … open (Conj. sigmaB)" is replaced by the refutation.
  - Item (iv) gains the B3 clause.
  - Item (v) is rewritten: the joint E15 scope, and "no result shows a three-world installation does".
  - "The protected ends … can sit only at near-unanimous limits (Lemma E13)" is replaced by the proved location
    statements (E13(a); F21(a) automatic at the ∂U collar inside {h_i < 0}; F21(b) under (Nest_e)).
  - "What a cover still needs" now says *some world* and "follows from (H_U)".
  - Remaining problems: Conj. sigmaB is replaced by Conj. F1Cp and the a.e.-finite target. "Whether unendorsed dominator
    comparisons that are not end-positive can occur" is replaced by the open route of (g).
- **Status table (lines ~204–215).**
  - D2sigma row: the interior ray is noted and Lem. F11 cited.
  - A new sub-header "Audit of 15 October" with 4 new rows: sigmaB refuted with F12/F13; F1Cp; F14/F15; F16/F18.
  - The two E1 rows are updated to "audited (F2); audit confirmed (F12 referee)". The second row adds Prop. F21 and its
    scope is narrowed.
  - N17.B′ row: sigmaB is false; F1Cp and the open route are added to the remaining items.
- **Line ~1582 (§8.1 "precise target").** "invisible … and cannot carry a cover of T₁" is restricted to the proved
  scope.
- **Line 1760 (§8.4(c)).** "that form is Conjecture sigmaB" is replaced by: false (Thm F13), with the M-form being F1Cp.
- **Line 1765 (§8.5 intro).** "with the consequence that the two-world mechanism cannot carry a cover of T₁ … E1 has not
  yet been refereed" is restricted. A sentence lists where the audit results sit.
- **§8.5(a) status of Thm R3 (line ~1805).** The E12 status is updated.
- **Sources.**
  - New entries for F1_notes.md, F2_notes.md and F12_referee.md.
  - The E1 entry now says "audited in F2; the audit refereed once".
  - The D2_referee2 entry marks the suggested σ-finite conjecture "false as written".

## Not changed

- No statement of an existing theorem, lemma or proposition was changed. Conj. sigmaB keeps its wording, and Lemma E13
  keeps its hypotheses as stated in the write-up (integrable densities, as in the Notation).
- D2_referee2.md and the roundreport/starthere files contain the same false sentences, but they are outside the
  write-up and were not edited ("write nowhere else"). F12 §6 item 9 asks for D2_referee2 §3.3 to be corrected; the
  write-up records the slip in the status of conj:sigmaB.
