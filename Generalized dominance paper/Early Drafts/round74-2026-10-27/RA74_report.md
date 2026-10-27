# RA74: referee report on core.tex (round 74), with the ldg.tex cross-reference check

27 Oct 2026. Independent referee. Everything was checked by hand. I recompiled both files in a separate folder (`r74/ra74build/`).
- `core.tex`: 14 pages. No warnings, undefined references or overfull boxes. The text is identical to the supplied core.pdf.
- `ldg.tex`: 25 pages, also clean.

## Verdict: MINOR FIXES

I re-derived every proof in core.tex. **There is no mathematical error and no gap.** Theorem 4.1, Corollary 4.10, Proposition 5.5, Corollary 5.6, Theorem 6.8 and Corollary 6.9 are all correct under the hypotheses stated.

The required fixes are of four kinds:
- one wrong sentence about which results use which measure conditions (R1);
- hypotheses missing from the statements of the Section 6 results (R2);
- a one-line consequence that ldg.tex now relies on but core.tex does not state (R3);
- notation and terminology clean-ups (R4–R7).

In ldg.tex:
- one of the four edits under-states its hypotheses (R8);
- two sentences outside the edited lines still rest on the intransitivity example, which has been cut from the companion (R9).

---

## Required fixes

**R1. Definition 1.5 (core.tex l.127–130): the statement of which results use which conditions is wrong.**
- The text says Sections 5 and 6 use "neither (M3) nor (M3′)".
- But Corollary 5.6, `cor:existence`, assumes (M3′) and uses it: its last clause is proved through Corollary 4.10(b), and so through Theorem 4.1.
- The text also overstates what Proposition 5.5 needs: (A1)–(A4) need (M1) only.

Replace "Theorem~\ref{thm:dominance} uses (M2) and (M3$'$), and not (M1). Sections~\ref{sec:integral} and~\ref{sec:repair} use (M1) and (M2), and neither (M3) nor (M3$'$)." with:

> Theorem~\ref{thm:dominance} and Corollary~\ref{cor:admissible} use (M2) and (M3$'$), and not (M1). Proposition~\ref{prop:axioms} uses (M1), and for (A5) the instance $\mu\{P_S=0\}=0$ of (M2). Corollary~\ref{cor:existence} uses (M1), (M2) and (M3$'$). Section~\ref{sec:repair} uses (M1) and (M2), and neither (M3) nor (M3$'$).

If R3 is adopted, Corollary 5.6's last clause can instead cite Corollary 6.9 and then needs only (M1) and (M2). Adjust the sentence to match.

**R2. Theorem 6.8 and Corollary 6.9: state the hypotheses in the statements.**
- Both use (M1), for m, and (M2), through Lemma 1.12(b), Lemma 6.2, Lemma 6.7 and Proposition 5.5's (A5) part.
- At present the hypotheses appear only in the sentence "Throughout this section…".
- Corollary 6.9 opens "Under the integral ranking", which hides the use of (M2). Every other headline result (Theorem 4.1, Corollary 4.10, Proposition 5.5, Corollary 5.6) names its conditions.

Fix:
- Theorem 6.8: begin "Assume (M1) and (M2). Let $X$ be an incoherent model. …"
- Corollary 6.9: begin "Assume (M1) and (M2). Under the integral ranking, …"
- Optional: state "Assume (M2)" in Lemmas 6.2, 6.7 and Corollaries 6.3, 6.4. These are the results that use it; Lemmas 6.5 and 6.6 use neither condition. The sentence covering the whole section can then go.

**R3. Corollary 6.9: add the characterisation under (M1) and (M2).**
- Under (M1) and (M2) alone, two results already give that the undominated models are exactly the coherent ones:
  - Proposition 5.5 (A5): every coherent model is undominated;
  - Corollary 6.9: every incoherent model is dominated.
- The paper never states this. Its only statement of "undominated ⟺ coherent" for the integral ranking is Corollary 5.6, which adds (M3′).
- ldg.tex l.518 relies on the (M1)+(M2) version. It says the companion's ranking "still ha[s] exactly the coherent models as its undominated models", in a passage whose measure is described by "a finite-moment and a null-boundary condition".

Fix:
- Append to the statement of Corollary 6.9: "In particular, a model is undominated if and only if it is coherent."
- Append to its proof: "Coherent models are undominated by Proposition~\ref{prop:axioms}."

**R4. Proof of Proposition 5.5, (A4) (l.638–646): the letter m is used for two things.**
- "put $m\coloneqq\mu(G_1)$" is followed by "$m_\omega(G_3)\ge\gamma\,cm$", so m is a mass and $m_\omega$ is the score in the same display.

Fix:
- Rename the mass to $t$ in this proof: "put $t\coloneqq\mu(G_1)$"; then $m_\omega(G_3)\ge\gamma\,ct\ge(\alpha+\beta)t+c\kappa t\ge m_\omega(G_1)+m_\omega(G_2)+c\kappa t$.
- For uniformity, do the same in the proofs of Lemmas 4.6 and 4.9 (l.378–384, l.494–499). There the clash is only with notation defined later.

**R5. Definition 6.1 (l.679–680): delete the unused term.**
- Delete "An element of $F_H$ is a \emph{weighted acceptance choice} inside $H$."
- The term is never used again, and the brief forbids extra terminology and exposition.

**R6. Define "$X\ne Y$ a.e." before it is used.**
- The notation is used in (A1), Lemma 5.3(b), Proposition 5.5 and Corollary 6.9.
- It can be misread as "X and Y differ at almost every gamble".

Fix: in Definition 1.7, after "models that are equal a.e.\ are identified", add "We write $X\ne Y$ a.e.\ if $X$ and $Y$ are not equal a.e."

**R7. Gloss of (A4) (l.286–287): "rejects" is not defined.**
- Replace "rejects those in $G_3$" with "accepts none of those in $G_3$".

**R8. ldg.tex l.518, new sentence: the measure hypotheses are missing.**

The sentence reads: "The companion paper also proves, without any score, that every incoherent set of desirable gambles is dominated under every ranking that satisfies four conditions …".
- The preceding sentence fixes the measure by "a finite-moment and a null-boundary condition".
- Read in that context, the new sentence claims the theorem under those conditions. That is false:
  - Theorem 4.1 needs (M2) and full support of the diffuse part (M3′);
  - (M3) cannot be dropped (REF73b §4);
  - (M1) is not needed.
- "Every incoherent set of desirable gambles" should be "every incoherent model", since models are a.e.-classes.

Replace the sentence with:

> The companion paper also proves, without any score, that when the measure satisfies the null-boundary condition and its atomless part gives positive measure to every nonempty open set of gambles, every incoherent model is dominated under every ranking that satisfies four conditions on comparisons: guidance for changes guided at every world, the three-model condition, transitivity through ties, and a consolidation condition.

The following sentence ("Its constructed ranking satisfies these conditions and leaves every coherent model undominated.") is accurate (Proposition 5.5) and can stay.

**R9. ldg.tex l.44 and l.451: "the rankings constructed in Section~\ref{sec:construct} need not be transitive" has lost its support.**
- "Need not be" asserts that intransitive instances exist.
- The only support was the companion's intransitivity example. The l.514 edit correctly removed that citation, and core.tex no longer contains the example.
- ldg's own `ex:intransitive` (l.460) is an abstract three-model relation, not a ranking built in Section 6.

Fix:
- l.44: replace "need not be transitive" with "are not assumed to be transitive".
- l.451: make the same replacement ("This matters because the rankings constructed in Section~\ref{sec:construct} are not assumed to be transitive.").

---

## Check of the four ldg.tex edits (task 4)

| Line | Edit | Verdict |
|---|---|---|
| 514 | "In general the ranking is not transitive, and the companion paper gives an example…" → "Transitivity is not part of the construction." | Correct; it removes the citation of cut material. See R9 for the two sentences that still depend on it. |
| 518 | Maximality characterisation ("largest relation …") replaced by the four-condition sentence | The maximality claim is correctly removed. The new sentence is under-hypothesised (R8). The neighbouring claims hold, under these conditions: repair theorem (Theorem 6.8); coherent models undominated (Proposition 5.5); strict improvement at every world (Corollary 6.9); closure under ties in ldg's sense (Lemma 5.3(b) together with Proposition 5.5); "exactly the coherent models" (needs R3). The four conditions named match (A1)–(A4) of Definition 3.1, and the names "three-model condition" and "transitivity through ties" are identical. |
| 660 | Zorn construction citation removed | Correct |
| 662 | Open question about the guidance-only clause "preserving the companion paper's results" removed | Correct. It referred to the maximality characterisation. |

Search of the rest of ldg.tex for:
- **veto, Brier, maximal, largest relation, Zorn, one-sided, restricted domain, covers:** no citation of the companion remains. The "Brier" at l.617 is ldg's own example.
- **The remaining `\cite{KCM}` sites (l.52, 429, 514, 518, 654):** consistent with core.tex, apart from R8, R9 and the dependence on R3.
- **l.654**, "Section~\ref{sec:construct} and the companion paper address [coherent admissibility]": accurate, because Proposition 5.5 gives one ranking under which every coherent model is undominated.

---

## Proofs re-derived (task 1)

- **Setting lemmas.**
  - Lemma 1.3 (a)–(e): correct. Each part is used.
  - Lemma 1.6: correct, and the measure is atomless (point masses factor as ν{·}·λ{·} = 0).
  - Lemma 1.9:
    - (a) correct;
    - (b) correct: the no-atom argument by shrinking balls of radius 1/n, then Sierpiński;
    - (c) correct: Lindelöf;
    - (d) correct: a state on the segment between the inf and sup states takes the value 0 at the atom, which contradicts (M2) for {q}.
  - Lemma 1.10 (identification): correct. The steps are the interior of D, positivity of the separating functionals, Hahn–Banach, the bipolar theorem, and int cl D = int D.
  - Lemma 1.12 (a)–(c): correct.
- **Tie lemma and Lemma 4.3:** correct. Lemma 4.3 uses (A4), and then (A3) and (A2) through Lemma 4.2.
- **Lemma 4.5 (U1):** correct.
- **Lemma 4.6 (sum triple):** correct.
  - Margin: inf(z′−x′−y′) ≥ 2δ − 3δ/2 = δ/2 = κ.
  - G₂ can be chosen disjoint from G₁ because m < ½μ_c(B(d,ρ)), and (U1) puts B(d,ρ) inside X up to μ_c-null sets.
- **Corollary 4.7:** correct.
- **Lemma 4.8 (a)–(e):** correct.
  - The dyadic density step holds: v′ − v = (λ−λ′)(w−v)/(1−λ′).
  - The cone step holds: λv = λ(v−η𝟙) + (1−λ)ε𝟙 with ε = λη/(1−λ).
  - Atoms are handled exactly by Lemma 1.9(d). Atoms in D_S lie in both X and D_K; atoms in −D_S lie in neither.
- **Lemma 4.9 (gap ⇒ triple of order c breaking (U2)):** correct.
  - Margins: 5η/8 for c = 1 and η/4 for c = 2, so κ = η/4 works for both.
  - J₀ lies in B(v₁, 3η/2) ⊆ V and misses B(v₁′, r); x − w has infimum greater than r.
  - The case v₁ = v₂ is covered.
- **Theorem 4.1 and Corollary 4.10:** correct.
- **Lemma 5.3:** correct.
- **Lemma 5.4:** correct.
- **Proposition 5.5:**
  - (A1), (A2) and (A3): correct.
  - (A4): correct. The unavailability step uses monotonicity, translation, superadditivity and homogeneity of P_Q. The score step uses sup/inf bounds that are finite because the sets are nonempty, and gives a gain of at least cκμ(G₁) > 0.
  - (A5): correct, via Lemma 5.4 ("protection").
- **Corollary 5.6:** correct, and it does not claim the class is nonempty for every fixed μ.
- **Lemma 6.2 (minimax):** correct. It uses weak-∗ compactness of F_H, uniform approximation of T by simple functions, Sion, and the saddle-point identification.
- **Corollaries 6.3 and 6.4, Lemmas 6.5, 6.6 and 6.7, Theorem 6.8:** correct, in both the consistent and the inconsistent case.
- **Corollary 6.9:** correct.

## Hypotheses and claims (task 2)

- **(M1):** used only in Sections 5–6. Not used by Theorem 4.1.
- **(M2):** used in Lemma 1.9(d), Lemma 1.12(b), Lemma 4.8(e) and Section 6. Lemma 5.4 and (A5) use only μ{P_S=0}=0.
- **(M3′):** used in Lemmas 4.6, 4.8 and 4.9, Corollary 4.7 and Theorem 4.1.
- **Separability and 𝟙 ∈ E:** global, fixed in Definition 1.1.
- **Remaining issues:** only R1 and R2.
- **Statements to avoid:** "Cannot be consolidated" does not appear. Nonemptiness for every μ allowed by Theorem 4.1 is not claimed.

## Form (task 3)

- No remarks, no names on theorem environments, no forbidden words.
- `\coloneqq` throughout; no `:=`.
- "Models" is used throughout. "Set of desirable gambles" appears only in the title.
- Every listed notion has a numbered definition. The axiom list (A1)–(A5) is complete for every result: (U1), (U2) and (M1)–(M3′) appear in the statements that use them.
- **Prose outside the glosses:**
  - the conditions sentence in Definition 1.5 (needed by the brief; fix per R1);
  - "The proof is in Section 4.4";
  - the clarifying sentence in Definition 1.14;
  - the unused term in Definition 6.1 (R5).

---

## Optional suggestions

1. Definition 1.14: name κ ("κ is a *margin* of the triple"). The proof of Proposition 5.5 says "with margin κ".
2. Lemma 6.2: rename Z ≔ T(F_H). The letter Z is a model in Definitions 1.13 and 3.1. Φ is also reused (the proof of Lemma 1.6 and Lemma 6.2).
3. Definition 5.1 states several facts inside a definition: Bochner integrability, functionals commuting with the integral, the norm bound and additivity. Consider a one-line lemma citing Diestel–Uhl.
4. After R1 and R2, "Each result below states the conditions it uses" is redundant.
5. Corollary 6.9 could also record that every model X has an undominated coherent N with N ⪰_ω X at every ω. For coherent X, take N = X (Lemma 5.3(a)). This is ldg's "dominance property" verbatim, which ldg l.52 and l.518 attribute to the companion.
6. ldg l.518: "guidance at every world" could be misread as strict guidance at each world. "Guidance for changes guided at every world" matches (A1); it is already used in the R8 text.
7. ldg l.514: "recorded for comparison with the companion paper" could become "…with the companion paper's integral ranking, in which distinct models are never tied". The cycle property itself is no longer stated in core.tex.
8. The letter B is used both for balls B(h,r) and for models. This is harmless but could be avoided.
