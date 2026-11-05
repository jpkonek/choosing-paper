# FAP80: ldg_full_final80.tex (concise §8, referee option C plus fixes)

Files in `r79/`:
- `ldg_full_final80.tex` and `ldg_full_final80.pdf`: the final paper.
- `fap80_edit.py`: every edit made after option C, as exact old/new pairs.
- `fap80/`: the build directory.

The build starts from `rap80/ldg_appC.tex`. Option D was not applied.

## Result

pdflatex was run three times, and references settled. The log shows:
- no errors;
- no undefined references;
- no overfull or underfull boxes;
- no LaTeX warnings.

| Part | Pages |
|---|---|
| §8 (42% down p. 24 to 80% down p. 30) | about **6.4 pp** (r80: about 9.3) |
| Appendix A (60% down p. 31 to 9% down p. 34) | about **2.5 pp** |
| Total | **34 pp** (r80: 35) |

## 1. Verifying option C against ldg_full_r80.tex

The check ran in three steps.

**Option A (r80 to ldg_cut2).** I re-ran `rap80/cuts.py` and then `cuts2.py` on `ldg_full_r80.tex`. The output is byte-identical to `rap80/ldg_cut2.tex`. All 25 "new" texts in RAP80 §3 appear verbatim in the result, and Cuts 11 and 13 are deletions, as described. Two cuts are overwritten by later ones:
- Cut 7 by Cut 22 (the report says so);
- Cut 17 by Cut 24 (the report does not say so, but this is harmless).

**Option B (ldg_cut2 to ldg_app).** The six proofs were moved with byte-identical bodies, and each was replaced by "The proof is in Appendix~\ref{app:proofs}.". There is **one undescribed change.** In §8.1 "Proper scores", `so (E) and (A) hold` became `so (A) holds`. This drops the (E) verdict, which ROUND79 and RAP80's Cut 21 both state. **I restored it.**

**Option C (ldg_app to ldg_appC).** Four things moved:
- the statement of lem:section;
- the proof of prop:joyce-repair;
- the two footnote proofs (Example 4, log score).

All moved bodies are byte-identical. Nothing else changed.

**Global check (r80 to appC).**
- No `\label` was lost. Only `app:proofs` was added.
- No theorem-like environment was lost.
- Every bibitem is still cited.
- Every citation that was lost has a described cause. `[Example~4]` and `[Example~5]` were absorbed into `[Examples~4--6]` (Cuts 8 and 9). `Assumption~3 of~\cite{SSK09}` became `\cite[Assumption~3]{SSK09}` (Cut 22).
- Every `\ref` that was lost is accounted for by a described cut:
  - ex:conditional by Cut 13;
  - ex:ssk-sharp by Cut 10;
  - thm:bayes-finite by Cut 6;
  - three references to thm:argument by Cuts 1, 5 and 6.

## 2. Correctness fixes (exact texts from RAP80 §2)

- **F1** was already in option C (Cut 8): `Without continuity, (A), (S) and (T) can each fail~\cite[Examples~4--6]{SSK09}.`
- **F2** was already in option C (Cut 19): `it covers Joyce's continuous strictly proper scores~\cite[p.~276]{Joyce},`
- **F3** was already in option C (Cut 12): `and Corollary~\ref{cor:updating} and its proof contain his Theorems~3 and~4~\cite{Nielsen21}.`
- **F4** was applied: `The failure needs $N\ge3$.` became `The failure of (S) needs $N\ge3$.`
- **F6** was applied, since it removes the conjunctive misreading: in Scope, Open questions, the sentence now reads `while strict propriety does, and so does face coherent admissibility (Proposition~\ref{prop:joyce-repair}).`
- F5 and F8 were already in the cuts. **F7 was not applied** (not requested). It is still recommended: `$(\frac12,\frac12,0)$` should become `$(\frac12,\frac12,0,\dots,0)$` in "Both counterexamples violate it at …".

## 3. Other edits

1. **(E) restored** in §8.1 "Proper scores", as described in §1.
2. **Dangling reference.** Option B left the phrase "by the bounds above" after prop:joyce, but those bounds are now in the appendix. It now reads `by the bounds in the proof of Proposition~\ref{prop:joyce}`.
3. **Appendix reordered to follow the order of statements:**
   1. Example 4 of SSK09 (§8.1);
   2. thm:nielsen;
   3. a one-line lead-in, then lem:section and its proof;
   4. prop:blocks;
   5. cor:updating;
   6. the log-score claim (§8.3);
   7. prop:countable;
   8. prop:joyce;
   9. prop:joyce-repair.
4. **The two footnote proofs are now proof environments.** Each is headed `Proof for Example~4 of~\cite{SSK09} in Section~\ref{sec:proper}` or `Proof for the logarithmic score in Section~\ref{sec:conditional}`, and opens with one sentence saying what is shown. This replaces option C's `\paragraph{Example 4 of [SSK09].}` and `\paragraph{… in Section 8.3.}`, which hard-coded the citation and the section number. In the log-score proof, "such an $x$" became "a Bayes model $x=(c,a_1,\dots,a_k)$", since the footnote's antecedent is gone.
5. **Lead-in for lem:section:** "The proof of Proposition~\ref{prop:blocks} uses the following lemma, in the setting of Definition~\ref{def:conditional-systems}."
6. **The 1.1 pt overfull vbox (p. 26) is fixed.** Its cause was the `\footnote{See Appendix…}` stub that falls under the Γ display. The two footnote stubs are now in-text pointers: `…is undominated; the proof is in Appendix~\ref{app:proofs}.` and `…whenever $c(E_j)>0$; the proof is in Appendix~\ref{app:proofs}.` So every moved proof is referenced from its claim.
7. **Leftover blank lines** where lem:section stood were removed.

## Side effect

lem:section is now Lemma A.1. The later §8 statements are renumbered (e.g. prop:blocks is 8.8, cor:updating 8.10). All references use `\ref`, and the source has no hard-coded internal numbers.
