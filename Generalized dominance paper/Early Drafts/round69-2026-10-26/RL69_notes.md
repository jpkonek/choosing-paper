# RL69: referee report on the restructured *Coherence and Dominance under General Rankings*

26 October 2026. Independent referee. I read the current `.tex` and PDF in full and compared them against `build/LDG_before_PR69b.tex` (before the copy edit and the restructure) and `build/LDG_before_restructure.tex`. I compared every theorem-like environment and every proof by label, and word-diffed the restructure. I also rebuilt the paper from scratch in `rl69work/`, the only other thing I wrote in this folder.

**Overall verdict.** The restructure succeeds. Nowhere is dominance presented as an assumption of the argument. The general finite theorem is correctly described as a weakening of the selection argument. No mathematical statement changed in substance, every cross-reference resolves to the right result, and the paper compiles cleanly. The required changes below are small presentation repairs. The most useful one is a model-level lemma in §2.1. It removes the forward references to Prop 6.1 without stating anything conditional on the dominance property before the theorems.

---

## 1. Is dominance anywhere presented as an assumption?

**Verdict: no.** Two wording points remain (items R2 and R5 below).

- **Abstract.** The abstract defines the dominance property and immediately says the main results *derive* it "from hypotheses that can be checked without knowing it". The consequences come afterwards: "We next record what the dominance property gives once it is established". A first-time reader gets the right order.
  - Two flaws. "The classical selection argument" is introduced with no source (R3). "Served at some world it charges" uses two terms that are defined only in the body (R3).
- **§1.**
  - ¶2 defines the property as the target.
  - ¶3–4 present the deriving theorems.
  - ¶5 ("What the dominance property gives") is explicitly labelled as consequences.
  - The one overstatement is "We never assume it." Props 6.1, 6.3 and 6.5 and Rem 4.7 do take it as an explicit hypothesis of conditional statements, so a careful reader will object. See R5.
- **§2.1.** The dominance property is defined in a displayed item and then called "a claim to be established, not an assumption". The old "Four conditions will be used" list is gone. Closure under ties is defined here, which is right because Thms 3.2, 4.1(c) and 4.6 use it in their statements. Evaluability and coherent admissibility moved to §6.3, where they are used.
- **§§3–4 come first.** §3 opens: "This section and the next contain the main results … derive the dominance property". Thm 3.2 now states "in particular, the ranking has the dominance property". Thms 3.3, 4.1 and 4.6 do not have the parallel clause (R4).
- **Prop 6.1.** It is introduced by "The following is a purely logical observation." Part (a) is conditional ("If L has the dominance property, then …"). §6 opens by saying that nothing in it is a reason to assume the property. This is correct.
- **Prop 6.5.** The hypothesis "… or has had the dominance property established by other means" is not a mathematical condition. A hypothesis cannot depend on how a fact was established. As written, the disjunction is equivalent to "has the dominance property", and the proof's opening "By those theorems, or by assumption" says exactly that. A referee would flag this phrasing (R2).
- **Section ranges disagree.**
  - §2.1 says "Sections 3 and 4 derive it".
  - §3 opens "This section and the next contain the main results".
  - §1 ¶3 says "Sections 3–5 contain the main results".
  - §6 opens "Sections 3–5 derive the dominance property".

  §5 does not derive the property; it refines it for losses (margins, Bayes models, strict dominance). See R6.

## 2. Is the general finite theorem correctly described as a weakening?

**Verdict: yes, accurate.**

Checked against the statements:
- **Corollary 4.2 (the selection argument).** It assumes:
  - c_p ∈ C_L;
  - competitiveness on supp p;
  - every full comparison set {p : c_p ⪯_ω m} closed.
- **Theorem 4.1.** It assumes c_p ∈ C_L and closed sets A_ω(m) with:
  - (i) A_ω(m) ⊆ {p : c_p ⪯_ω m};
  - (ii) every p lies in some A_ω(m) with ω ∈ supp p.

Cor 4.2 is the case where A_ω(m) is the whole comparison set, as its proof shows. Example 4.4 shows the inclusion between the hypotheses is strict.

One point the text gets right and should keep: Thm 4.1 does **not** drop competitiveness. Condition (ii), together with A_ω(m) ⊆ full set, implies that c_p is competitive on supp p. The weakening is only in closedness: closed *subsets* replace closed *full sets*. The abstract, §1 ¶4 and the new §4.1 paragraph all say this correctly ("provided these subsets still serve every prior at some world it charges"). KKM applies to the subsets unchanged, and Thm 4.6 adds compactness. All of this is stated accurately.

**Problem: the word "classical".** It appears five times: abstract, §1 ¶4 twice (once in the italic heading), §1 ¶5, §4.1, §7. No source is cited. I know of no published proof of an accuracy-dominance or complete-class result that uses exactly this KKM selection with closed comparison sets. The standard proofs use separating hyperplanes, Bregman projections or fixed points of a different kind. So a referee will ask "classical according to whom?".

There is also a clash with the companion paper. Its §(veto–Brier) calls a *different* argument "the classical argument from undominatedness to coherence": Zorn, then separation, which is LDG's "Other methods" in §9. The two papers therefore use "classical" for two different arguments. See R3.

## 3. Forward references to Prop 6.1

**Not circular.** The proof of Prop 6.1(a) uses only the definitions of weak dominance, dominance, ties, C_L and closure under ties. It cites no theorem, so the proofs of Thms 3.2, 4.1 and 4.6, which cite it, are logically sound.

**Recommendation: replace the citation with a short model-level lemma in §2.1, and do not move Prop 6.1(a) itself.** Reasons:
- Inlining would have to be done twice, in Thm 3.2 and Thm 4.1, because Thm 3.2 comes first and cannot cite Thm 4.1 without another forward reference.
- Moving Prop 6.1(a) to §2 would put a statement whose hypothesis is "L has the dominance property" before the theorems. That partly undoes the restructure.
- The step the theorems actually use is a fact about **one model and one weak dominator**. It mentions no dominance property and presupposes no weak dominators. It fits naturally right after the definition of closure under ties, and Prop 6.1(a) then becomes a one-line corollary.

Replacement text is in R1 below.

## 4. Unchanged mathematics; cross-references

**Verdict: confirmed.** No statement changed in substance.

I compared every theorem, lemma, proposition, corollary, example and remark by label, and every proof. All differences are of four kinds:
- **Terminology.** "dominance conclusion holds/fails" became "has/lacks the dominance property". "closure under ties holds" became "L is closed under ties". Both define the same property: the old and new definitions of the dominance property and of closure under ties match word for word.
- **Thm 3.2.** It adds "in particular, the ranking has the dominance property". This is an immediate restatement, since the assigned models are in C_L.
- **Proofs of Thms 3.2 and 4.1, and of Prop 6.5.** Only connective sentences were added: "So L has the dominance property", "purely logical", and "By those theorems, or by assumption".
- **Prop 6.5's hypothesis.** It changed from "every ranking satisfies the dominance conclusion" to "meets the hypotheses of Thm 4.1 or 4.6 … or has had the dominance property established by other means". Since those theorems imply the property, and the second disjunct *is* the property, the hypotheses are equivalent. This is the same mathematics, but badly phrased (R2).

Rem 4.7 (both items), Rem 4.8, Rem 4.9, the "guarantees on finite sets" paragraph, Examples 3.4, 4.4 and 6.2, and §7 differ only in the terminology above, plus framing sentences.

**Cross-references.** In a fresh three-pass build there are no undefined or multiply defined labels. Every hard-coded number in the text is an external citation (SSK09 Ex 2/4, Pettigrew Thm 1, and so on). I checked each renumbered internal reference in context:
- Prop 6.1, 6.3, 6.5; Ex 6.2, 6.4;
- Thm 3.2, 3.3, 4.1, 4.6; Cor 4.2; Ex 3.4, 4.4; Rem 4.7, 4.8, 4.9;
- Prop 7.1(a)/(c);
- §7's "(Proposition 6.1, and Proposition 6.5 except part (c))", where PR69b's notes still say 3.1/3.5;
- §9's lists.

All point to the intended result.

## 5. Section 7

**Verdict: accurate.** Two small wording points.

- **Prop 7.1(c).** I re-checked the proof. Given the two guidance conditions, (i) ⇔ (ii) holds as stated, and (i) is the dominance property (with "model" meaning a member of M_L). The new paragraph after the proof says this correctly: "Part (c) does not assume the dominance property. It is an equivalence … reduces the dominance property to the existence of improvements of a specific kind, which must then be proved."
- **The companion.** It is described as proving the dominance property directly: coherent models cannot be dominated, plus a repair theorem giving a replacement accepted at every world. The text says it bypasses the selection argument and Theorems 4.1 and 4.6, and that it does not assume dominance. This matches the companion's abstract ("As a consequence, and without assuming any dominance property, one ranking has exactly the coherent sets as its undominated members …"). §9 "Other methods" (Zorn's lemma, used by the companion "for one structured construction") is also consistent with the companion's veto–Brier theorem.
- **Wording 1.** §7's first paragraph says "build a ranking, and derive the dominance property for it directly". Prop 7.1 does not derive it; it reduces it. This sentence contradicts the careful paragraph after the proof (R7).
- **Wording 2.** §1 ¶6 says "for such a ranking, the dominance property is equivalent to …" and omits the two guidance conditions (R7).
- **Cross-paper item (not LDG).** The companion's line 1237 still describes LDG in the old order: "studies … what follows once coherent undominated replacements exist, and conditions under which they do". See R9(e).

## 6. Compile and conventions

- **Compile.** The fresh pdflatex ×3 build has no warnings, no undefined references, and no overfull or underfull boxes; it runs to 23 pages. The shipped PDF's text is identical to the fresh build (pdftotext diff empty), and I spot-checked pp. 1 and 14 visually.
- **`\coloneqq`.** It is used throughout, with no `:=` anywhere.
- **Theorem names.** No theorem-like environment has an optional name.
- **No comments, TODOs or internal codes** in the source.
- **Jargon.**
  - "classical selection argument" (uncited; R3);
  - "served … charges" in the abstract (R3);
  - "bookkeeping" (§1 ¶5, §6 opening), which is informal and slightly dismissive in a journal paper (R9(c));
  - "evaluable model", used in the definition of the dominance property and in Props 6.1, 6.3 and 6.5 but never defined (R9(a)). This predates the restructure.
- **Abstract length.** The abstract is 321 words, up from 250 before the restructure, and many journals cap abstracts at 200–250 (R9(b)).

---

## Required changes, ranked

### R1. Replace the forward citations of Prop 6.1(a) with a model-level lemma in §2.1
Insert at the end of §2.1, after the paragraph defining closure under ties:

```latex
\begin{lemma}\label{lem:ties}
Let $c\in\C_L$ weakly dominate a model $m$.
\begin{enumerate}[label=(\alph*)]
\item If $m$ is undominated, then $m$ and $c$ are tied at every world.
\item If $L$ is closed under ties and $m\notin\C_L$, then $c$ dominates $m$.
\end{enumerate}
\end{lemma}
\begin{proof}
(a) If $m$ did not weakly dominate $c$, then $c$ would dominate $m$. (b) By closure under ties, $m$ is not tied at every world with $c$. Since $c$ weakly dominates $m$, $m$ does not weakly dominate $c$, so $c$ dominates $m$.
\end{proof}
The lemma concerns one model and one weak dominator; it does not presuppose that weak dominators exist.
```

**Thm 3.2 proof.** Replace "…so the additional hypothesis is closure under ties, and the purely logical Proposition~\ref{prop:conclusion}(a) in Section~\ref{sec:conclusion} applies." with:

> …so the additional hypothesis is closure under ties. Let $m$ be any model and $c$ an assigned model weakly dominating it. If $m$ is undominated, Lemma~\ref{lem:ties}(a) ties it to $c$, so $m\in\C_L$ by closure under ties; and if $m\notin\C_L$, then $c$ dominates $m$ by Lemma~\ref{lem:ties}(b).

**Thm 4.1 proof.** Replace "So $L$ has the dominance property, and parts (b) and (c) follow by the purely logical Proposition~\ref{prop:conclusion}(a)." with:

> (b) and (c) Let $c\in\C_L$ weakly dominate $m$, by (a). If $m$ is undominated, Lemma~\ref{lem:ties}(a) ties it to $c$, which gives (b); under closure under ties it follows that $m\in\C_L$, so $\U_L\subseteq\C_L\subseteq\U_L$. If $m\notin\C_L$, then $c$ dominates $m$ by Lemma~\ref{lem:ties}(b).

**Thm 4.6 proof.** Replace "The rest is Proposition~\ref{prop:conclusion}(a)." with:

> Conclusions (b) and (c) follow from Lemma~\ref{lem:ties} as in the proof of Theorem~\ref{thm:finite}.

**Prop 6.1(a) proof.** Replace it with:

> (a) Apply Lemma~\ref{lem:ties} to each model and an undominated coherent model weakly dominating it. By part (a) of the lemma every undominated model is tied with a member of $\C_L$, and so, under closure under ties, lies in $\C_L$; hence $\U_L\subseteq\C_L\subseteq\U_L$, and part (b) of the lemma gives the last claim.

**Optional.** In §9 "What depends only on the ranking", list "Lemma~\ref{lem:ties}" before Proposition 6.1.

**Numbering.** The new lemma becomes Lemma 2.4. Nothing else renumbers, because the counter is per section.

### R2. Restate Prop 6.5's hypothesis as a mathematical condition
Replace "Suppose that each ranking in $\Lf$ meets the hypotheses of Theorem~\ref{thm:finite} or~\ref{thm:local} (in particular, of Theorem~\ref{thm:bayes-finite} or~\ref{thm:bayes-infinite}), or has had the dominance property established by other means. Then for each $L\in\Lf$:" with:

> Suppose that each ranking in $\Lf$ has the dominance property (for instance, because it meets the hypotheses of Theorem~\ref{thm:finite} or~\ref{thm:local}). Then for each $L\in\Lf$:

In the proof, delete "By those theorems, or by assumption, every ranking in $\Lf$ has the dominance property." and the following "then". This is mathematically identical to the current statement. If the author prefers not to write "has the dominance property" in a hypothesis, the alternative is "meets the hypotheses of Theorem 4.1 or 4.6, or is a ranking as in Proposition 7.1 satisfying (c)(ii) under its two conditions". That version is *narrower*, so it would change the mathematics. I do not recommend it.

### R3. Remove the uncited "classical", and define "served" in the abstract
Unless the author has a source to cite for this exact argument, change:
- **Abstract.** "which weaken the classical selection argument. That argument requires … ; we require only closed subsets of these sets, large enough that every prior is served at some world it charges." becomes:
  > which weaken the selection argument behind these results. That argument requires the priors at which an assigned model does at least as well as a given rival at a given world to form a closed set; we require only closed subsets of these sets, provided every prior belongs to the subset for some world to which it gives positive probability.
- **§1 ¶4 heading.** "The general theorems weaken the classical argument." becomes "The general theorems weaken the selection argument."
- **§1 ¶4.** "The classical selection argument assigns" becomes "The selection argument behind Theorem~\ref{thm:bayes-finite} assigns".
- **§1 ¶6 and §7.** "the classical selection argument and its weakening" becomes "the selection argument and its weakening".
- **§4.1.** "\emph{A weakening of the classical selection argument.} The classical argument is Corollary~\ref{cor:closed-choice} below." becomes "\emph{A weakening of the selection argument.} The selection argument behind Theorem~\ref{thm:bayes-finite}, stated for arbitrary rankings, is Corollary~\ref{cor:closed-choice} below."

If "classical" is kept, it needs a citation, and the companion's different use of "the classical argument from undominatedness to coherence" should be renamed.

### R4. State the dominance property in every deriving theorem, not only Thm 3.2
- **Thm 3.3.** "Then every model is weakly dominated by some $c_\theta$." becomes "Then every model is weakly dominated by some $c_\theta$; in particular, the ranking has the dominance property."
- **Thm 4.1(a).** Append "; in particular, $L$ has the dominance property".
- **Thm 4.6.** "Then every model is weakly dominated by some $c_\theta$, and conclusions…" becomes "Then every model is weakly dominated by some $c_\theta$, so $L$ has the dominance property, and conclusions…"

These are restatements, because every $c_\theta$ or $c_p$ is in $\C_L$. They make the paper's central claim visible in the statements of its main theorems.

### R5. Make "We never assume it" precise (§1 ¶2)
Replace "We never assume it. The main results derive it from hypotheses stated without reference to it; only afterwards do we record what follows from it." with:

> It is never a standing assumption. The main results derive it from hypotheses stated without reference to it; the consequences recorded afterwards are stated conditionally on it.

### R6. Make the section ranges consistent
- §1 ¶3: "Sections~\ref{sec:bayes}--\ref{sec:margins} contain the main results." becomes "Sections~\ref{sec:bayes} and~\ref{sec:general} contain the main results, and Section~\ref{sec:margins} refines them for losses." Then delete the now-redundant "(Section~\ref{sec:margins})" at the end of that paragraph, or keep it; either is fine.
- §6 opening: "Sections~\ref{sec:bayes}--\ref{sec:margins} derive the dominance property" becomes "Sections~\ref{sec:bayes} and~\ref{sec:general} derive the dominance property".

### R7. Section 7 and §1: "reduce", not "derive"
- §7 first paragraph: "build a ranking, and derive the dominance property for it directly." becomes "build a ranking, and reduce the dominance property for it to the existence of improvements of a specific kind."
- §1 ¶6: "it shows that, for such a ranking, the dominance property is equivalent to" becomes "it shows that, for such a ranking and under two conditions on the guidance, the dominance property is equivalent to".

### R8. §4.1: remove the duplication the inserted paragraph created
The new "A weakening…" paragraph introduces Cor 4.2 and Ex 4.4. It is followed by the older paragraph ending "A simpler special case takes every comparison of the assigned model to be guaranteed", which introduces Cor 4.2 again. The fix:
- Move the paragraph "We read $A_\omega(m)$ as … (Remark~\ref{rem:collapse})." so that it comes directly after "The proof uses no property of the relations…".
- Delete its last sentence, "A simpler special case takes every comparison of the assigned model to be guaranteed."
- Let the "A weakening…" paragraph, with the R3 wording, lead straight into Corollary 4.2.

### R9. Optional
- **(a) Define "evaluable" once.** In §2, change "its \emph{evaluation domain}," to "its \emph{evaluation domain}, whose members are the models \emph{evaluable} by $L$,".
- **(b) Shorten the abstract.** It is now 321 words. The R3 sentence is shorter. Cutting "under lower semicontinuity at each world" from the applications list, and "and an example shows that this cannot be dropped", would bring it to about 280 words.
- **(c) Replace "bookkeeping".** §1 ¶5 "records, as bookkeeping, the consequences" becomes "records the logical consequences". §6 opening "records, as bookkeeping, what follows" becomes "records what follows".
- **(d) Say whether evaluability is used.** It is listed as a condition "that will be used", but no proof uses it: Prop 6.5 and the closing sentence hold without it, because an unevaluated model is vacuously irrational and not permissible. Either add a clause saying it excludes vacuous verdicts, or drop "will be used". This predates the restructure.
- **(e) Companion, line 1237 (for PR69a or the lead, not LDG).** "studies, for arbitrary models and rankings, what follows once coherent undominated replacements exist, and conditions under which they do" becomes:
  > derives, for arbitrary models and rankings, the property that every model is weakly dominated by an undominated coherent model from conditions stated without reference to it, and records what follows from it

  This matches LDG's new order.
- **(f) Intro ¶5, the permissibility sentence.** It still omits "and every ranking in the family is closed under ties", which the exact identification in Prop 6.5 needs (PR69b §3.3).
