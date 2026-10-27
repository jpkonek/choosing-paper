# FA75: changes from `app_revised.tex` to `app_final.tex`

`app_revised.tex` is untouched. The edits were applied by `FA75_build/apply.py`, which checks that each target string occurs exactly once, plus two small follow-up edits listed at the end.

Build: three pdflatex passes in `FA75_build/`. Result: **17 pages**, no errors, no warnings, no undefined references, no overfull or underfull boxes. Every `\ref` was checked against the `.aux` file and resolves to the intended item. The new numbering is:
- Definition 1.4: the measure
- Definition 1.5: atoms, plus the conditions table
- Lemma 1.6: the existence measure
- Definition 1.8: advice
- Proposition 1.9: `prop:advice`
- Definition 1.10 and Lemma 1.11: unordered choices
- Example 1.12
- Lemma 1.21: `lem:Wincoherent`
- Theorem 4.1 and Corollary 4.10
- Proposition 5.5: `prop:axioms`
- Definition 5.1: the score

The PDF has been copied to `app_final.pdf`.

## Required fixes

1. **Coherent models and contradictory advice (Definition 1.8).** Replaced with the referee's exact text, ending "...only on a null set (Proposition~\ref{prop:advice})."
2. **Every finite Borel measure.** The referee's text was used with one change. "the results of Sections 5 and 6 assume (M1) and (M2)" became "...assume (M1), (M2) or both". The verbatim wording would be false for some results:
   - Lemma 5.3 and the (A1)–(A4) part of Proposition 5.5 assume only (M1);
   - Lemma 5.4 assumes only the instance μ{P_S=0}=0.

   The table itself records this correctly. The paragraph now sits in Definition 1.5 (see fix 9a).
3. **What μ(B) weighs.** The referee's paragraph was inserted verbatim into Definition 1.4, after "outside a null set." and before "We consider the following conditions".
4. **(M2) gloss in the table.** Replaced with the exact text: "the gambles on the boundary of what $D_Q$ accepts, those with $P_Q(h)=0$, carry no weight."
5. **Grouping definition ((A4) explanation, "What the masses supply").** Replaced with the exact text: a finite measure on G₁×G₂×G₃ or on G₁×G₂×G₃×G₃, with the marginal conditions as given.
6. **Overlap bullet ("Judgements, not whole choices").** The whole bullet was replaced with the referee's exact text, including "(possibly with $i=j$)" and "these cases need no separate treatment". The false "it is demanding" is gone.
7. **Result inside the (A4) explanation.**
   - Step 1: `lem:Wincoherent` was inserted after Definition `def:consolidation` (it is Lemma 1.21) and is unnamed. Its proof is the referee's. One addition to the statement: "of order $c$, and let $\kappa$ be as in Definition~\ref{def:triple}(ii)". The proof uses c and κ, and nothing else introduces them.
   - Step 2: the sentence was replaced with "By Lemma~\ref{lem:Wincoherent}, (A4) constrains the comparison only for incoherent $W$."
   - Step 3: in the proof of Proposition 5.5, the paragraph was replaced with "\emph{No coherent model could make this change}, by Lemma~\ref{lem:Wincoherent}." The rest of that proof does not use the x, y of the deleted paragraph.
8. **Unused clause in Definition 1.4.** Replaced with "Under (M4), $-X$ is null whenever $X$ is null."
9. **Remarks removed.**
   - (a) Remark `rem:measure` was deleted:
     - its first paragraph was replaced by the fix-3 paragraph in Definition 1.4;
     - "Each result below holds uniformly ... is assumed.", the fix-2 paragraph, the lead-in "They say the following." and the table (with fix 4 and O1 applied) were appended to the end of Definition 1.5;
     - `Remark~\ref{rem:measure}` in the (A4) explanation became a reference to `def:measure`. It was then merged with the preceding reference as "Definitions~\ref{def:advice} and~\ref{def:measure}";
     - the `rem:unordered` pointer sentence was deleted.
   - (b) Remark `rem:unordered` was replaced by Definition `def:unordered` [Unordered choices] (1.10) and the unnamed Lemma `lem:unordered` (1.11) with its proof, verbatim, with one exception. Clause (c) reads "then the score of Definition~\ref{def:score} satisfies $m_\omega(X)=\dots$". The score is defined later (Definition 5.1), so it needed a pointer.
   - Follow-up edits for (b):
     - the `(Remark~\ref{rem:unordered})` in the overlap bullet became `(Definition~\ref{def:measure})`, through the fix-6 text;
     - the per-choice reading of the score was dropped;
     - Example 1.12 was kept.
   - The unused `remark` theorem declaration was removed. No Remark environments remain.
10. **Bijection clause (Proposition 1.9).** Replaced with the exact text "such that, for a.e. $f$, $\alpha(-f)$ is $\alpha(f)$ with ``for'' and ``against'' exchanged."

## Optional suggestions

- **O1 (applied).** Table, row (M3′): "no result in Sections~\ref{sec:integral} or~\ref{sec:repair} assumes it."
- **O2 (applied).** The proof of Proposition 1.9 now opens its "Bijection." paragraph with "Assume (M4). By (b), $\alpha_X$ depends, up to null sets, only on the class of $X$. Also, ..." "Assume (M4)" was already implicit in "Under (M4)", which this replaces.
- **O3 (applied).** The "Every context" item was cut to its first and last sentences. The four state transitions were removed.
- **O4 (applied).** Both forms now say "the gamble in each supplied judgement pays at least κ more than the sum/average of the gambles in any withdrawn pair". This makes the sum form consistent with the midpoint form.
- **O5.** No change, as the referee advised.

## Form check

- Definitions carry short names. Lemmas, propositions and theorems are unnamed. No Remark environments remain.
- The only non-definitional prose is:
  - the axiom glosses and the (A4) explanation;
  - the plain-English material on μ, inside Definitions 1.4 and 1.5.

  The "used by" column and the fix-2 paragraph are the condition-to-result statements that the brief requires.
- There is no summary of results, introduction or discussion.

## Notes, not changed

- (M2) is still named "Null indifference boundaries". Given fix 4, a name such as "Null acceptance boundaries" may read better. That was not requested, so the name is unchanged.
- The conditions table is unbreakable, so it moves to the top of page 3 and leaves about a third of page 2 blank. `app_revised` had the same layout. It is not an overfull box.
