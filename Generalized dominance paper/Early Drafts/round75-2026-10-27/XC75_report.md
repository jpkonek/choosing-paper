# XC75: cross-check of app_final.tex against ldg_full_final.tex and ldg_short_final.tex

The files in r75/ are identical to the copies in FA75_build/ and FL75_build/. The numbering below comes from FA75_build/app_final.aux.

## Verdict: no required mismatches.

## 1. Statements about the companion paper

There are 13 KCM citations: full lines 51, 53 (two), 518, 624 (six) and 795; short line 180 (two). All of them were checked.

### Numbers

Every cited number matches the application paper exactly:

| Cited as | Label in app | What it is |
|---|---|---|
| Thm 4.1 | thm:dominance | (M2), (M3′) and (A1)–(A4) give: every incoherent model is dominated |
| Cor 4.10 | cor:admissible | (a): with (A5) for 𝒦, members of 𝒦 are undominated and incoherent models are dominated |
| Prop 5.5 | prop:axioms | Under (M1), the integral ranking satisfies (A1)–(A4). Under μ{P_S=0}=0, and in particular under (M2), it satisfies (A5) for all coherent models |
| Thm 6.8 | thm:repair | Under (M1) and (M2): a coherent N, a uniform margin η, and a change no coherent model could make |
| Cor 6.9 | cor:repair | Under (M1) and (M2): strict domination by an undominated coherent model |

### Labels and glosses

- **(A1)–(A5).** The names match: guidance, three-model condition, transitivity through ties, consolidation, admissibility of 𝒦. The LDG gloss of (A1), "non-null change guided at every world ⇒ strictly better at every world", matches. So does the gloss of (A5), "every member of a family of coherent models is undominated".
- **(M1), (M2), (M3′).** The names match: finite first moment; null indifference boundaries; full support of the diffuse part, glossed as "positive measure once the atoms are removed", which is μ_c. "Separable gamble space containing the constants" matches Definition 1.1. "Identified up to null sets" matches Definition 1.7.

### Conclusions

- **Axiomatic class.** It is credited with ordinary dominance only, at full lines 51, 518 and 624 and short line 180. Each of these says explicitly that the theorem does not give undominated coherent dominators.
- **Undominated coherent dominators.** These are credited only to the integral ranking under (M1) and (M2), via Theorem 6.8 and Corollary 6.9, at full lines 53 and 624. Correct.
- **"Under (M2) it also leaves every coherent model undominated" (Prop 5.5).** This is true. The application paper needs only the instance μ{P_S=0}=0, so the LDG statement is weaker than what is proved, but not wrong.

### Integral ranking as an instance of LDG Definition (construction)

This is correct:

- **Score.** It is real-valued under (M1).
- **Null change.** It is guided, and a null change means equality a.e.
- **"Available to no coherent model".** The LDG wording (no coherent z whose change to some z′ is that change) is equivalent to the application's wording (B ⊆ Z a.e. and A∩Z null). Take Z′ = (Z∖B)∪A.
- **"Guided changes improve the score".** This is Lemma 5.3(b), under (M1).
- **"Guidance protects coherent models".** This is Lemma 5.4, under μ{P_S=0}=0.
- **"Closed under ties".** This holds because distinct models are never tied (Lemma 5.3(b)).
- **"Score increment the same at every occurrence of a change" (full line 584).** This holds because m_ω(X)−m_ω(Y)=m_ω(A)−m_ω(B).

## 2. Shared definitions and conventions

**Orientation.** In LDG, m ⪯_ω m′ reads "m performs at least as well as m′". In the application, X ⪰_ω Y reads "X is at least as good as Y". So LDG ⪯ corresponds to application ⪰, and LDG ≺ to application ≻. Both papers define the strict relation as "the relation holds and its converse does not". Ties are mutual comparison in both.

**Notions that match under this translation:**
- **Dominance.** The LDG full version, the LDG short version ("weakly dominates and not tied at every world") and application Definition 2.2 are equivalent.
- **Strict dominance** and **undominated** also match.
- **LDG's three-model no-reversal condition** is exactly application (A2).
- **LDG Definition (construction).** "m ⪯_ω m′ iff the change from m′ to m is guided at ω, or available to no coherent model and φ_ω(m) > φ_ω(m′)". This matches application Definition 5.2 with m = X and m′ = Y. Higher scores are better in both.

**Lower-is-better losses.** These appear only in LDG's loss rankings and are never applied to the companion paper.

**No symbol is transcribed across the papers,** so nothing is conflated.

**Other terms:**
- **Irrational and permissible.** These appear only in LDG.
- **"Admissible".** The application uses it as a synonym for undominated. LDG's "coherent admissibility" is a property of a family. LDG describes (A5) in words, as "every member … is undominated", and never equates it with coherent admissibility. No conflation.

## 3. The family premise against Theorem 4.1

LDG premise (i) reads: "every incoherent model is dominated under every ranking in 𝓛 that evaluates it".

The application's rankings are relations on all models (Definition 2.1). Axioms (A1) and (A4) quantify over all models, so a ranking that satisfies (A1)–(A4) has M_L = M, the set of all models (classes a.e.). Each such ranking therefore evaluates every model, and "evaluates" imposes no restriction.

With C equal to the application's coherent models, Theorem 4.1 gives dominance by some model in M_L under each ranking in the family. That is exactly premise (i). Evaluability is then automatic for a nonempty family. LDG claims only premise (i) from Theorem 4.1, and not premise (ii), coherent admissibility. Consistent.

## Optional (not mismatches)

**O1. Full, line 620.** The text reads "the cycle property of Proposition~\ref{prop:construct}(a) is not used elsewhere in this paper; it is stated for comparison with the companion paper." The companion paper states no cycle property, and none of the application versions mentions cycles or chains. The analogous fact there is Lemma 5.3(b). Possible fix: replace "it is stated for comparison with the companion paper" with "it is stated for comparison with the companion paper, whose integral ranking accepts a comparison between distinct models only when it raises the score, so that distinct models are never tied~\cite[Lemma~5.3(b)]{KCM}."

**O2. Full, line 518, and short, line 180.** The fact that the KCM rankings evaluate every model is implicit. To make it explicit, after "satisfy its axioms (A1)--(A4)" add ", which are defined on all models, so that each evaluates every model," (in the short version, after "(A1)--(A4) of~\cite{KCM}").
