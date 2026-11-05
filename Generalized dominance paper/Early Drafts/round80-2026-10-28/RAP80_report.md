# RAP80: referee report on ldg_full_r80.tex (new §8 "Applications")

Referee files are in `rap80/`:
- `rap80/ldg_full_r80.{tex,pdf}`: my own compile;
- `rap80/cuts.py` and `rap80/cuts2.py`: the concision cuts as exact old/new pairs, applied in order;
- `rap80/ldg_cut2.{tex,pdf}`: Option A applied;
- `rap80/ldg_app.tex` and `rap80/ldg_appC.{tex,pdf}`: the appendix variants B and C;
- `rap80/cuts_listing.md`: the generated list of cuts below.

## Verdict

**Mathematically sound, with four small required fixes. Not yet concise enough.**

**Correctness.** Every new claim checks out, either by my own re-derivation or against the paper texts:
- every new proposition, corollary and example;
- every literature claim;
- every page and theorem number;
- every (E)/(A)/(S)/(T) verdict, which matches ROUND79/REF79a/REF79b.

The four required fixes (F1–F4) are small overstatements or ambiguities. None changes a verdict.

**Concision.** By page fractions, §8 is about **9.3 pp**: from 45% down p. 24 to 77% down p. 33. That is not 8.5 as WAP80 reports. The old §8 was about 5.6 pp.

The pre-existing material alone fills about 5.6 pp:
- thm:nielsen and its proof;
- the §8.3 machinery and ex:conditional;
- prop:countable;
- prop:joyce.

So the target of 5–6 pp **cannot be met by trimming the literature discussion alone**. My in-section cuts (Option A, all exact text below) bring §8 to about **8.5 pp** with no result or verdict lost. Reaching 5–6 pp needs one structural step: moving proofs to an appendix. I measured this by compiling each option:

| Option | What it does | §8 length |
|---|---|---|
| B | A, plus the six long proofs moved to an appendix | about **6.9 pp** |
| C | B, plus lem:section, the proof of prop:joyce-repair and the two long footnote proofs moved too | about **6.4 pp** (one 1.1 pt overfull vbox, trivial) |
| D | C, plus ex:conditional replaced by a short remark | about **6.0 pp** (estimate) |

The six proofs in B are those of thm:nielsen, lem:section, prop:blocks, cor:updating, prop:countable and prop:joyce.

**Compilation.** My own pdflatex compile (`rap80/`) gives 35 pp, with no errors, no undefined references, and no overfull or underfull boxes.

**Edits outside §8** (intro, Scope, bibliography, prop:strict(b), §6.1, rem:closed-comparisons) are accurate and acceptably minimal. One wording fix is in F6 (optional).

## 1. Correctness: what I checked (all OK unless listed in §2)

### Pettigrew (2022)
- I : C×W→[0,∞]; Continuity, Strict Propriety and Theorem 1 at p. 135 of the text; the enhanced log score L*(c,i) = Σ[−w(X) log c(X) + c(X)]. All match the text.
- The gap example, recomputed:
  - L*(c) = (∞, 1.5+ln 2);
  - the divergence minimiser is δ₂, with L*(δ₂,1) = ∞;
  - prop:strict(b) applies, since continuity is used only on supp p.

### Predd et al. (IEEE)
- Definition 2: s:{0,1}×[0,1]→[0,∞], uniqueness in (a), sequential continuity in (b).
- Theorem 1(a),(b).
- §VII.A: one score per event.
- §VII.B.1 "Non-Uniqueness … Proposition 2 also holds in this generalized case".
- Proposition 2: φ(x) = −x s(1,x) − (1−x)s(0,x) is "bounded, continuous, and strictly convex". I checked this on the PDF image, p. 4788.
- For the example, φ = −∞ on (0,1). So the "false" claim is correct, and SSK Lemma 3 (max{g0,g1} = ∞ everywhere) is cited correctly.

### SSK (TR 865 file)
- Theorem 2 / Conclusion 3: it requires Assumptions 1 and 3, Assumption 2 for merely proper scores, and continuity. This matches "finite on (0,1), continuous".
- Lemma 5, Lemma 3, Assumption 3 (p. 260 of the txt), Theorem 1 (coherence₁ ⇔ coherence₃, the latter defined by strict dominance) and §6 (the (0.9, 0.7) remark and the conjecture wording): all correct.
- Example 4:
  - g0 = x² + ½·1{x>½} and g1 = (1−x)² + ½·1{x≤½}.
  - f = (½, 0.3) has profile (0.84, 1.24).
  - The footnote proof is correct: the jumps contribute exactly ½ per coordinate over the two worlds, so the sum of the Brier parts is ≤ 0.08, which gives the radius 1/5 circle. Each step (y>½ ⇒ L1 > 0.84; x>½ ⇒ L2 > 1.5; then y ≤ 0.3, which forces f) re-derived.
- Example 5:
  - (½, 0.7) has profile (7/4, 1/4) and is Bayes for (½, ½) with V = 1.
  - Coherent profile requires r₁ = ½ and r₂ > ½.
  - (0, 0.7) and (0, 1) are tied at (5/2, 0), and the loss-0 argument is correct.
  - Note: SSK's own d₁, d₂ are printed swapped; LDG does not repeat them, which is fine.
- Example 6:
  - g1(½) is undefined in SSK; reading it as ¼ gives losses (1,1,1,1) against (1,½,½,1).
  - (½,½,½) is coherent via R(C1) = R(C4) = ½.
- Flat score: G′ = (y−t)·1_supp λ; s ≡ 1/18 on [⅓,⅔]; the tie is at (1/9, 1/9). Checked.

### Nielsen (2023)
Checked against the text:
- quasi-strict propriety, continuity on P, local boundedness, product topology (n. 20);
- Theorem 1 (strict "accuracy-dominance");
- Theorem 2 (weak accuracy-dominance = our dominance);
- note 27;
- §4.2.1, which asks whether Theorem 1 holds without local boundedness.

The lifted ex:ssk-sharp is correct:
- r(c) is minimised only at c(∅) = 0, c(Ω) = 1;
- g0 ≥ 1 on (0,1] forces c({2}) = 0, and then g1(0) = ∞.

"Open only for infinite Ω" is correct: prop:strict(b) applies under Nielsen's [0,∞]-continuity, with V finite by quasi-strict propriety.

### Nielsen (2021) and Briggs–Pettigrew
- Checked against the text:
  - Separability, Continuity, Extensionality, Strict Propriety, Temporal Separability (α, β in n. 3);
  - B&P's Theorem 1 (I)–(III), p. 171;
  - Nielsen's Theorems 3 and 4.
- cor:updating:
  - statement and proof re-derived;
  - Bayes models for π: c = π, and a_j = π(·|E_j) on cells π charges;
  - ρ(Γ) is the set of coherent strategies.
- The claim "contains his Theorems 3 and 4" holds only with the proof (F3).
- Log score:
  - strictly proper under 0·∞ = 0;
  - J(c,ω) = ∞ iff c({ω}) = 0 is in effect;
  - the footnote proof is correct, and so is the failure of Theorem 4(a).
- The necessity paragraph ("Bayes prior must differ") is correct under continuity. I re-derived the limit argument.

### SSK conditional forecasts
- The Brier numbers are correct: 0.5, 0.9, 1.3 against 0.32, 0.72, 0.52.
- The R-characterisation is SSK's Lemma 11, not their definition (Definition 1 is the no-book definition). I suggest citing Lemma 11; see Cut 15.

### Joyce (2009)
Checked against the text:
- Theorem 2 (pp. 287–288): hypotheses TD, CA, finite and continuous; (i) "dominated", strict by p. 267;
- n. 9, p. 271;
- CA, p. 280;
- PROPRIETY, p. 276, where the log score is called strictly proper;
- the log score excluded, p. 288;
- Lemmas 2 / 2* (pp. 295 / 296): the "all zero" case is mishandled;
- Lemma 1* (p. 295) and the bᵐ construction (b³ = (½,½,0) for c = (1,1,0)).

Results:
- **prop:joyce symmetry line**: s_{σ(i)}(x∘σ⁻¹) = s_i(x). Checked.
- **Two-cell tie example**: checked, including that c_p = p is Bayes, since the minimiser is d = p₁−p₂.
- **ex:joyce-additive**:
  - derivative 6x+2−(2N+6)p;
  - the prior (6b+2)/(2N+6) sums to 1;
  - t = min{(N+1)/6, 1} ≥ ⅔;
  - uniqueness even for p without full support, by coordinatewise strict convexity;
  - tie loss 2N+1−9/(4N) for the constants 1/(2N) and 3/(2N), checked algebraically;
  - violation of face CA at (½,½,0,…) for all N, since the minimiser of the convex f(a) is (N+1)/6 ≠ ½.
- **Face CA**:
  - automatic at vertices (TD) and at interior p (CA), hence for N = 2;
  - prop:joyce-repair(b) re-derived: completeness gives competitiveness on supp p (lem:competitive), lsc gives closed comparison sets, and cor:closed-choice and cor:coherent-assigned(c) do the rest.

### Verdict table
All (E)/(A)/(S)/(T) statements in §8 agree with ROUND79's table as corrected by REF79a/b. This includes:
- Ex4: A ✓, S ✗, T ✓;
- Ex5: S ✗, T ✗;
- Ex6: A ✗;
- Joyce: S ✗ for N ≥ 3, T ✗;
- B&P: A ✗;
- log score: T ✗;
- SSK conditional: A ✗.

### Scripts
WAP80's scripts (`wap80/check_proper.py` and `wap80/check_other.py`) re-run and pass.

## 2. Required correctness fixes (exact text)

**F1 (§8.1, Discontinuous scores).** (E) cannot fail here; "each condition" is wrong.
- Old: `Without continuity each condition can fail, as three examples of Schervish, Seidenfeld and Kadane show~\cite[Examples~4--6]{SSK09}.`
- New: `Without continuity, (A), (S) and (T) can each fail~\cite[Examples~4--6]{SSK09}.`
- Cut 8 below already includes this.

**F2 (§8.5, paragraph after prop:joyce-repair).** "it covers Joyce's strictly proper scores" is wrong without a continuity or lsc qualifier: SSK's Example 4 is strictly proper and (S) fails there.
- Old: `it covers Joyce's strictly proper scores~\cite[p.~276]{Joyce},`
- New: `it covers Joyce's continuous strictly proper scores~\cite[p.~276]{Joyce},`
- Cut 19 below already includes this.

**F3 (§8.3, after cor:updating).** Nielsen's Theorem 3(c)(2) (no non-conditionalizing strategy weakly dominates a probabilistic conditionalizing one) is not in the corollary's statement. It follows from its proof, since a weak dominator of a Bayes model for c is one.
- Old: `and Corollary~\ref{cor:updating} contains his Theorems~3 and~4~\cite{Nielsen21}.`
- New: `and Corollary~\ref{cor:updating} and its proof contain his Theorems~3 and~4~\cite{Nielsen21}.`
- Cut 12 below already includes this.

**F4 (§8.5, after ex:joyce-additive).** "The failure needs $N\ge3$." is wrong as read, because Joyce's theorem already fails for N = 2 (the tie example). Only the failure of (S) needs N ≥ 3.
- Old: `The failure needs $N\ge3$.`
- New: `The failure of (S) needs $N\ge3$.`

**Optional accuracy and clarity fixes:**
- **F5 (§8.1, Credence functions).** Old: `This is~\cite[Theorem~1]{Pettigrew};`. New: `This contains~\cite[Theorem~1]{Pettigrew};`. LDG proves uniform dominance and more. Cut 5 includes this.
- **F6 (Scope, Open questions).** Old: `while strict propriety and face coherent admissibility do (Proposition~\ref{prop:joyce-repair}).` New: `while strict propriety does, and so does face coherent admissibility (Proposition~\ref{prop:joyce-repair}).` The old wording can be read as the conjunction.
- **F7 (§8.5).** Old: `Both counterexamples violate it at $(\frac12,\frac12,0)$.` New: `Both counterexamples violate it at $(\frac12,\frac12,0,\dots,0)$.`
- **F8 (§8.3, Conditional forecasts).** Cite `\cite[Lemma~11]{SSK09}` for the R-characterisation of coherence₁. Cut 15 includes this.

## 3. Concision cuts

### Option A: in-section cuts (exact text; apply in order)

Cuts 1–19 are `rap80/cuts.py`, applied to ldg_full_r80.tex. Cuts 20–25 are `rap80/cuts2.py`, applied to the result. The result is `rap80/ldg_cut2.tex`: it compiles cleanly to 34 pp, and §8 is about 8.5 pp.

No result or condition verdict is lost. What Option A changes:
- **Cut 1** states once that Theorem 6.4 applies to every family of such losses, so the four repetitions go.
- **Cuts 2–4** remove the inline restatements of def:propriety, def:quasi-propriety and def:block-propriety inside prop:proper, thm:nielsen and prop:blocks. The definitions stay.
- **Cut 10** replaces the display of the lifted SSK Example 2 by a sentence pointing to ex:ssk-sharp.
- **Cut 13** deletes the paragraph that proves the Bayes prior must differ in cor:updating's setting. ex:conditional already makes this point and is what §3 cites.

Cut 7 is superseded by Cut 22. F4, F6 and F7 are not part of the cuts and must be applied separately. Long old passages are given by their exact first and last words ("…" marks the elided middle). The full old strings are in the scripts.

**Cut 1.** Replace the text `where a condition fails, it says so and why.`

with:

```latex
where a condition fails, it says so and why. When all four hold for each loss in a class, Theorem~\ref{thm:argument} applies to every family of such losses; we do not repeat this.
```

**Cut 2.** Replace the text `and $L$ is \emph{strictly proper relative to $\M_L$}: each $p$ is a Bayes model for $p$, and every Bayes model …  every Bayes model for $p$ has the profile $L(p)$. Then every coherent`

with:

```latex
and $L$ is strictly proper relative to $\M_L$ (Definition~\ref{def:propriety}). Then every coherent
```

**Cut 3.** Replace the text `Assume \emph{quasi-strict propriety}: $E_qL(q,\cdot)\le E_qL(m,\cdot)$ for every $q\in\C$ and $m\in\M_L$, stri … L$, strictly when $m\notin\C$. Assume also that $q\mapsto L(q,\omega)$`

with:

```latex
Let $L$ be quasi-strictly proper (Definition~\ref{def:quasi-propriety}), and assume that $q\mapsto L(q,\omega)$
```

**Cut 4.** Replace the text `Assume \emph{block propriety}: for each $j$ and $q\in\PP(F_j)$, the report $\rho_j(q)$ minimises $x\mapsto q(S … psto L(\rho(\gamma),\omega)$ is lower semicontinuous on $\Gamma$. Then`

with:

```latex
Assume block propriety and lower semicontinuity along coherent systems (Definition~\ref{def:block-propriety}). Then
```

**Cut 5.** Replace the text `\emph{Credence functions.} Pettigrew~\cite{Pettigrew} takes as models the credence functions on all subsets of … $ does. The theorem remains true, by Proposition~\ref{prop:strict}(b).`

with:

```latex
\emph{Credence functions.} Pettigrew~\cite{Pettigrew} takes as models the credence functions on all subsets of a finite $\Omega$, as coherent models the probabilities, and losses that need not be additive, are continuous as maps into $[0,\infty]$, and are strictly proper with $0\cdot\infty=0$. Proposition~\ref{prop:proper} applies with unique Bayes models, and (E) is trivial; so every incoherent credence function is uniformly dominated by a probability, which contains~\cite[Theorem~1]{Pettigrew}. His proof does not cover infinite losses: for his enhanced logarithmic score $I(c,\omega)\coloneqq-\sum_{A\ni\omega}\log c(A)+\sum_Ac(A)$, two worlds and $(c(\varnothing),c(\{1\}),c(\{2\}),c(\Omega))\coloneqq(0,0,\frac12,1)$, the probability his proof selects, which minimises his divergence from $c$, is $\delta_2$, and it has infinite loss at world~$1$, as $c$ does. The theorem remains true, by Proposition~\ref{prop:strict}(b).
```

**Cut 6.** Replace the text `\emph{Strictly proper continuous scores.} Let each $s_i$ be strictly proper and continuous as a map into $[0,\ … ~1]{Predd}, also with one score per event~\cite[Section~VII.A]{Predd}.`

with:

```latex
\emph{Strictly proper continuous scores.} Let each $s_i$ be strictly proper and continuous as a map into $[0,\infty]$, as in~\cite[Definition~2]{Predd}. Each $G^i_t$ has a finite minimum, since otherwise every $y$ would minimise it; so $c_p$ is the unique Bayes model for $p$, $V$ is finite, and, as in Proposition~\ref{prop:proper}, (A), with $\C_L=\C$, and (T) hold. The losses along $c_p$ are continuous, so Theorem~\ref{thm:bayes-infinite}, with $\Theta\coloneqq\Delta_{\tau(\Omega)}$, $c_\theta\coloneqq(\theta(E_i))_i$, every finite set linked and $\sigma_F(p)$ the image of $p$ under $\tau$, gives (S), and Proposition~\ref{prop:strict}(b) shows that every incoherent forecast is uniformly dominated by a coherent one. This is~\cite[Theorem~1]{Predd}, also with one score per event~\cite[Section~VII.A]{Predd}.
```

**Cut 7.** Replace the text `\emph{Scores infinite inside $(0,1)$.} The finiteness condition matters: without it coherent admissibility can fail. With one event`

with:

```latex
\emph{Scores infinite inside $(0,1)$.} Without the finiteness condition, (A) can fail. With one event
```

**Cut 8.** Replace the text `\emph{Discontinuous scores.} Without continuity each condition can fail, as three examples of Schervish, Seide … neqq(\frac12,\frac3{10})$, with profile $(0.84,1.24)$, is undominated.`

with:

```latex
\emph{Discontinuous scores.} Without continuity, (A), (S) and (T) can each fail~\cite[Examples~4--6]{SSK09}. Example~4 uses two complementary events and a strictly proper score with jumps at $\frac12$ (Figure~\ref{fig:profiles}(b) shows a variant). Strict propriety gives (A) and (T), but no coherent forecast weakly dominates $(0.6,0.7)$, so (S) fails, and the incoherent $f\coloneqq(\frac12,\frac3{10})$, with profile $(0.84,1.24)$, is undominated.
```

**Cut 9.** Replace the text `In their Example~5, a merely proper score with a jump, the incoherent forecast $(\frac12,0.7)$ is a Bayes mode … ssk-sharp}, where all four conditions hold but strict dominance fails.`

with:

```latex
In Example~5, a merely proper score with jumps, the incoherent $(\frac12,0.7)$ is a Bayes model for the prior $(\frac12,\frac12)$ with $V$ finite, hence undominated, and no coherent forecast has its profile, so (S) fails; the incoherent $(0,0.7)$ is tied, at $(\frac52,0)$, with the coherent $(0,1)$, which is undominated since every forecast with loss $0$ at the second world has loss $\frac52$ at the first, so (T) fails. In Example~6, reading $g_1(\frac12)$ as $\frac14$, the coherent $(\frac12,\frac12,\frac12)$ has loss $1$ at all four worlds and is dominated by $(0,0,0)$, with losses $(1,\frac12,\frac12,1)$, so (A) fails. Example~2 is Example~\ref{ex:ssk-sharp}: all four conditions hold, but strict dominance fails.
```

**Cut 10.** Replace the text `The proof gives (A), with $\C_L=\C$, (S), by Theorem~\ref{thm:bayes-infinite}, and (T), for each such loss; (E …  Bayes model. So the question remains open only for infinite $\Omega$.`

with:

```latex
The proof gives (A), with $\C_L=\C$, (S), by Theorem~\ref{thm:bayes-infinite}, and (T); (E) is trivial. Nielsen's admissible measures~\cite{Nielsen} lie in this class: they are quasi-strictly proper, and his continuity of $q\mapsto E_pL(q,\cdot)$ on $\C$ gives, at $p=\delta_\omega$, continuity of $q\mapsto L(q,\omega)$. He also assumes local boundedness, $\sup_\omega L(q,\omega)<\infty$ for $q\in\C$, concludes strict dominance~\cite[Theorem~1]{Nielsen}, and asks whether local boundedness can be relaxed~\cite[\S4.2.1]{Nielsen}; his Theorem~2, that no probability is dominated, already does without it~\cite[note~27]{Nielsen}. Theorem~\ref{thm:nielsen} drops it for the dominance of incoherent models. Strict dominance can fail under its hypotheses: Example~\ref{ex:ssk-sharp}, with $f\coloneqq(c(\{1\}),c(\{2\}))$ and $c(\varnothing)^2+(1-c(\Omega))^2$ added at each world, is quasi-strictly proper, since each probability is its own unique Bayes model with $V$ finite, and lower semicontinuous along the probabilities; the incoherent $(c(\varnothing),c(\{1\}),c(\{2\}),c(\Omega))=(0,\frac12,0,1)$ is dominated by $\delta_1$ but, as there, not strictly dominated. This loss is not continuous at $\delta_1$. Under Nielsen's continuity with $\Omega$ finite, Proposition~\ref{prop:strict}(b) gives uniform dominance without local boundedness, since $V$ is finite, each $p$ is a Bayes model for itself and no incoherent model is a Bayes model. So his question remains open only for infinite $\Omega$.
```

**Cut 11.** Replace the text `A null cell is treated like any other: on $E_j$ the comparison is made against $q_j$, not $q_0$.`

with:

```latex
(delete)
```

**Cut 12.** Replace the text `For each such $J$, (E) is trivial and the proof of Proposition~\ref{prop:blocks} gives (A), (S) and (T); so Th … g}. Nielsen's counterexample to (III)~\cite{Nielsen21} is an instance.`

with:

```latex
For each such $J$, (E) is trivial and the proof of Proposition~\ref{prop:blocks} gives (A), (S) and (T). Nielsen's finite-valued measures, which are moreover additive, extensional and continuous, are among them, and Corollary~\ref{cor:updating} and its proof contain his Theorems~3 and~4~\cite{Nielsen21}. The strategies that are dominated but not strictly dominated are the incoherent Bayes models: on some cell $E_j$ with $c(E_j)=0$ they plan a credence function that is not a probability, or a probability with $a_j(E_j)<1$. Briggs and Pettigrew claim that no probabilistic conditionalizing strategy is dominated~\cite[Theorem~1(III)]{BP20}. With these strategies as the coherent class, this claim is (A), and it fails when $k\ge2$: strategies of the second kind belong to the class and are dominated under every $J$ satisfying the hypotheses of Corollary~\ref{cor:updating}. Nielsen's counterexample to (III)~\cite{Nielsen21} is an instance.
```

**Cut 13.** Replace the text `As in Example~\ref{ex:conditional}, the Bayes prior must be allowed to differ from $p$ when $J$ is continuous  … delta_{\omega_1}$ by strict propriety; likewise $x=\delta_{\omega_2}$.`

with:

```latex
(delete)
```

**Cut 14.** Replace the text `Finiteness of $J$ matters, and Proposition~\ref{prop:blocks}, which needs finite block losses, does not cover  … cores, and under $0\cdot\infty=0$ his Theorem~4(a) fails for this one.`

with:

```latex
Finiteness of $J$ matters. The logarithmic score $J(b,\omega)\coloneqq-\sum_{A\ni\omega}\log b(A)-\sum_{A\not\ni\omega}\log(1-b(A))$ is strictly proper with $0\cdot\infty=0$, but $J(c,\omega)=\infty$ whenever $c(\{\omega\})=0$; so Proposition~\ref{prop:blocks}, which needs finite block losses, does not apply, and strategies that differ only on cells of probability zero are tied at every world. By Theorem~\ref{thm:bayes-finite} directly, the undominated strategies are exactly the Bayes models, those with $c$ a probability and $a_j=c(\cdot\mid E_j)$ whenever $c(E_j)>0$.\footnote{A weak dominator $y$ of such an $x$ has $c$-expected loss at most that of $x$, which is finite; by strict propriety, applied to the prior and to the cells that $c$ charges, $y$ has the same prior and the same plans on those cells, so $L(y)=L(x)$, the losses being infinite off $\supp c$. Conversely, the strategies with prior $p$, plans $p(\cdot\mid E_j)$ when $p(E_j)>0$ and fixed plans otherwise are Bayes models for $p$, with losses continuous as maps into $[0,\infty]$, since $J(p,\omega)\to\infty$ as $p(\{\omega\})\to0$. By Theorem~\ref{thm:bayes-finite} each strategy is weakly dominated by one of them, so an undominated strategy is tied with a Bayes model and, by the first step, is one.} So for $k\ge2$ the coherent class of Corollary~\ref{cor:updating} is not closed under ties, and the conclusion of Theorem~\ref{thm:argument} fails for it; Nielsen's assumptions allow this score, and under $0\cdot\infty=0$ his Theorem~4(a) fails for it.
```

**Cut 15.** Replace the text `and call forecasts coherent if some finitely additive probability $R$ has $R(B)P(A\mid B)=R(A\cap B)$ for ever … nce survives because it uses strict dominance~\cite[Theorem~1]{SSK09}.`

with:

```latex
and call forecasts coherent if some finitely additive probability $R$ has $R(B)P(A\mid B)=R(A\cap B)$ for every pair~\cite[Lemma~11]{SSK09}, so that forecasts given an $R$-null event are unconstrained. This class violates (A) already under the Brier score. For disjoint $A_1,A_2$ meeting $B\ne\Omega$, the forecasts $0.9$ and $0.7$ for $A_1$ and $A_2$ given $B$ are coherent~\cite[Section~6]{SSK09}, but $0.6$ and $0.4$ dominate them: at the worlds of $A_1\cap B$, $A_2\cap B$ and $B\setminus(A_1\cup A_2)$ they lose $0.32$, $0.72$ and $0.52$, against $0.5$, $0.9$ and $1.3$, and both lose $0$ outside $B$. Their equivalence of coherence with the absence of dominance~\cite[Theorem~1]{SSK09} survives because it uses strict dominance.
```

**Cut 16.** Replace the text `\emph{Credences that sum to more than one.} Joyce's Lemma~$1^*$~\cite[p.~295]{Joyce} asserts a sign that truth … rectedness does not supply for such credences, and selection can fail.`

with:

```latex
\emph{Credences that sum to more than one.} Here selection can fail.
```

**Cut 17.** Replace the text `This is where Lemma~$1^*$ goes wrong.`

with:

```latex
This is where Joyce's Lemma~$1^*$~\cite[p.~295]{Joyce} goes wrong.
```

**Cut 18.** Replace the text `\item If each $p\in\Delta$ is the unique Bayes model for $p$, then (A), (S) and (T) hold for $L$, and every in … e or continuous as a map into $[0,\infty]$, it is uniformly dominated.`

with:

```latex
\item If each $p\in\Delta$ is the unique Bayes model for $p$, then (A), (S) and (T) hold.
```

**Cut 19.** Replace the text `So truth-directedness and coherent admissibility give (E) and (A), and, for two cells, (S); but in general the … rm dominance for them. Part~(b) gives dominance, not strict dominance.`

with:

```latex
So truth-directedness and coherent admissibility give (E) and (A), and with two cells (S), so that every credence is weakly dominated by a coherent one; in general they give neither (S) nor (T). Part~(a) needs neither truth-directedness nor finiteness; it covers Joyce's continuous strictly proper scores~\cite[p.~276]{Joyce}, including the logarithmic score, which his theorem excludes~\cite[p.~288]{Joyce}, and Proposition~\ref{prop:proper} gives uniform dominance for them. Part~(b) gives dominance, not strict dominance.
```

**Cut 20.** Replace the text `\emph{Event forecasts.} Predd et al.~\cite{Predd} and Schervish, Seidenfeld and Kadane~\cite{SSK09} fix events … sed at $t$, and \emph{strictly proper} if $t$ is its unique minimiser.`

with:

```latex
\emph{Event forecasts.} Predd et al.~\cite{Predd} and Schervish, Seidenfeld and Kadane~\cite{SSK09} fix events $E_1,\dots,E_n$ in a nonempty set $\Omega$ and scores $s_i:\{0,1\}\times[0,1]\to[0,\infty]$; a forecast $f\in[0,1]^n=\M_L$ has loss $L(f,\omega)\coloneqq\sum_is_i(\one_{E_i}(\omega),f_i)$ and is coherent if $f=(\pi(E_i))_i$ for a probability $\pi$. The loss depends on $\omega$ only through $\tau(\omega)\coloneqq(\one_{E_i}(\omega))_i$, so loss profiles and dominance on $\Omega$ and on the finite set $\tau(\Omega)$ correspond. To a prior $p$ on $\tau(\Omega)$ assign the coherent forecast $c_p\coloneqq(p(E_i))_i$. With $0\cdot\infty=0$, the $p$-expected loss of $f$ is $\sum_iG^i_{p(E_i)}(f_i)$, where $G^i_t(y)\coloneqq ts_i(1,y)+(1-t)s_i(0,y)$; $s_i$ is \emph{proper} if each $G^i_t$ is minimised at $t$, and \emph{strictly proper} if uniquely.
```

**Cut 21.** Replace the text `\emph{Proper scores.} Let each $s_i$ be continuous and proper, not necessarily strictly, with $s_i(0,y)<\infty … ny unconditional events this is~\cite[Theorem~2, Conclusion~3]{SSK09}.`

with:

```latex
\emph{Proper scores.} Let each $s_i$ be continuous and proper, with $s_i(0,y)<\infty$ for $y<1$, $s_i(1,y)<\infty$ for $y>0$ and $s_i(0,0)=s_i(1,1)=0$. Then $c_p$ is a Bayes model for $p$, $V$ is finite, and every Bayes model for $p$ has the profile of $c_p$~\cite[Lemma~5]{SSK09}; so (E) and (A) hold, with $\C_L=\C$, and (S) as before. By Propositions~\ref{prop:profiles} and~\ref{prop:strict}(b), the undominated forecasts are those with a coherent loss profile, and a forecast that is a Bayes model for no prior is uniformly dominated by a coherent one; for unconditional events this is~\cite[Theorem~2, Conclusion~3]{SSK09}. But (T) can fail, and with it the conclusion of Theorem~\ref{thm:argument}. Score $E_1\ne\varnothing,\Omega$ and $E_2\coloneqq\Omega\setminus E_1$ by $s(1,x)\coloneqq\int_{[x,1)}(1-q)\,\lambda(dq)$ and $s(0,x)\coloneqq\int_{[0,x)}q\,\lambda(dq)$, with $\lambda$ Lebesgue measure on $[0,\frac13]\cup[\frac23,1]$. Then $G_t'(y)=(y-t)\one_{\supp\lambda}(y)$, so $s$ is proper; it is continuous, finite and normalised, and $s(0,\cdot)=s(1,\cdot)=\frac1{18}$ on $[\frac13,\frac23]$. So the incoherent $(0.4,0.4)$ is tied with the coherent $(0.4,0.6)$, at $(\frac19,\frac19)$, and is undominated.
```

**Cut 22.** Replace the text `\emph{Scores infinite inside $(0,1)$.} Without the finiteness condition, (A) can fail. With one event $E\ne\va … lse, and it needs Assumption~3 of~\cite{SSK09}, finiteness on $(0,1)$.`

with:

```latex
\emph{Scores infinite inside $(0,1)$.} Without the finiteness condition, (A) can fail. With one event $E\ne\varnothing,\Omega$, let $s(0,y)\coloneqq y/(\frac12-y)$ for $y<\frac12$, $s(1,y)\coloneqq(1-y)/(y-\frac12)$ for $y>\frac12$, and both be $\infty$ elsewhere. This score is continuous as a map into $[0,\infty]$, and proper, since $s(0,0)=s(1,1)=0$ and $G_t\equiv\infty$ for $0<t<1$. Every forecast is coherent, and $0$, with profile $(\infty,0)$ on $(E,\Omega\setminus E)$, dominates $0.3$, with profile $(\infty,\frac32)$. The score meets~\cite[Definition~2]{Predd} without uniqueness, as in~\cite[Section~VII.B.1]{Predd}, which asserts that Proposition~2 still holds. It does not: $\varphi(x)\coloneqq-xs(1,x)-(1-x)s(0,x)$, there asserted to be bounded, is $-\infty$ on $(0,1)$, as for every proper score infinite somewhere in $(0,1)$~\cite[Lemma~3]{SSK09}; the assertion needs~\cite[Assumption~3]{SSK09}.
```

**Cut 23.** Replace the text `\emph{Ties.} In Lemmas~2 and~$2^*$~\cite[pp.~295--296]{Joyce}, a fixed point at which every difference $S(p,\n … election holds, with $c_p\coloneqq p$, which is a Bayes model for $p$.`

with:

```latex
\emph{Ties.} In Lemmas~2 and~$2^*$~\cite[pp.~295--296]{Joyce}, a fixed point at which every difference $S(p,\nu_n)-S(c,\nu_n)$ vanishes is a tie, which coherent admissibility does not exclude; and ties occur. With two cells, let $L_1(x)\coloneqq(1-x_1+x_2)^2$ and $L_2(x)\coloneqq(1+x_1-x_2)^2$. The bases are nonnegative, so the loss is truth-directed, and it has Joyce's other properties. With $d\coloneqq x_1-x_2$, the profile of $x$ is $((1-d)^2,(1+d)^2)$; so profiles are pairwise incomparable, and $x$ is tied with the coherent $(\frac{1+d}2,\frac{1-d}2)$. Hence (A) holds, and (S) with $c_p\coloneqq p$, a Bayes model for $p$; but (T) fails, and no credence, not even $(0,0)$, is dominated.
```

**Cut 24.** Replace the text `Here (E), (A) and (T) hold, and (S) fails, since no coherent credence weakly dominates $x^*$. With $c_p\colone … t needs $L_i(b^3)<L_i(c)$ for $i=1,2$; both inequalities are reversed.`

with:

```latex
Here (E), (A) and (T) hold and (S) fails. With $c_p\coloneqq p$, the comparison sets of Corollary~\ref{cor:closed-choice} are closed, but competitiveness fails at $p=(\frac12,\frac12,0)$: by the bounds above, $x^*$ is strictly better than $p$ at worlds~$1$ and~$2$. This is where Joyce's Lemma~$1^*$~\cite[p.~295]{Joyce} goes wrong: from $c=x^*$ his construction forms the coherent $b^3=(\frac12,\frac12,0)$ and needs $L_i(b^3)<L_i(c)$ for $i=1,2$; both are reversed.
```

**Cut 25.** Replace the text `Additivity, extensionality and strict convexity do not repair the theorem. Let $N\ge3$, $s(b,1)\coloneqq3(1-b) … rac9{4N}$ at every world, but no credence is tied with a coherent one.`

with:

```latex
Additivity, extensionality and strict convexity do not repair the theorem. Let $N\ge3$, $s(b,1)\coloneqq3(1-b)^2+2(N-1)(1-b)$, $s(b,0)\coloneqq3b^2+2b$ and $L(x,\omega)\coloneqq\sum_ns(x_n,\one\{n=\omega\})$. This loss is finite, continuous, truth-directed (as $s(\cdot,1)$ strictly decreases and $s(\cdot,0)$ strictly increases), additive, extensional, strictly convex and permutation-invariant; Joyce's factor $1/N$ changes no ranking. The $n$th term of the $p$-expected loss is strictly convex in $x_n$ with derivative $6x_n+2-(2N+6)p_n$, so the unique Bayes model for $p$ has $x_n=\min\{\max\{((2N+6)p_n-2)/6,0\},1\}$. Each coherent $b$ is the unique Bayes model for the prior $(6b+2\one)/(2N+6)$, which charges every world; so a weak dominator of $b$ equals $b$, and (A) and (T) hold. The unique Bayes model for $(\frac12,\frac12,0,\dots,0)$ is $(t,t,0,\dots,0)$ with $t\coloneqq\min\{(N+1)/6,1\}\ge\frac23$; it is incoherent and, for the same reason, weakly dominated by nothing else, so (S) fails. There are ties, for instance between the constant credences $\frac1{2N}$ and $\frac3{2N}$, with loss $2N+1-\frac9{4N}$ at every world, but none with a coherent credence.
```


### Options B–D: structural (needed for 5–6 pp)

**B (measured: §8 about 6.9 pp).** On top of A:
1. Replace each of these six proofs by `The proof is in Appendix~\ref{app:proofs}.`: thm:nielsen, lem:section, prop:blocks, cor:updating, prop:countable and prop:joyce.
2. Insert before the bibliography:
```latex
\appendix
\section{Proofs for Section~\ref{sec:apps}}\label{app:proofs}
\begin{proof}[Proof of Theorem~\ref{thm:nielsen}] ...unchanged body... \end{proof}
```
   and likewise for the other five proofs, with their bodies unchanged.
- File: `rap80/ldg_app.tex`.

**C (measured: about 6.4 pp).** On top of B, move into the appendix:
- the statement of lem:section (it is used only in the proof of prop:blocks);
- the proof of prop:joyce-repair;
- the bodies of the Example 4 and log-score footnotes. Each footnote becomes `\footnote{See Appendix~\ref{app:proofs}.}`.
- File: `rap80/ldg_appC.tex`. It has one 1.1 pt overfull vbox, which needs a manual fix.

**D (estimate: about 6.0 pp).** On top of C:
1. Delete ex:conditional, together with the sentence that introduces it: `Nothing requires every Bayes model to be coherent, nor every assigned model to be a Bayes model for the prior to which it is assigned:`
2. Restore the paragraph that Cut 13 deletes, as `\begin{remark}\label{rem:bayes-prior}…\end{remark}`, starting "In the setting of Corollary~\ref{cor:updating}, the Bayes prior must be allowed to differ from $p$ when …". Its text is unchanged otherwise.
3. In §3 (line 230), change `Example~\ref{ex:conditional} shows that this freedom is needed` to `Remark~\ref{rem:bayes-prior} shows that this freedom is needed`.
4. Dominated Bayes models are already shown by the "dominated but not strictly dominated" sentence after cor:updating.

## 4. Edits outside §8

- **Intro (§1).** The literature sentence and the applications paragraph are accurate. Every claim is backed in §8, including "drops a boundedness assumption … for the dominance, though not the strict dominance, of incoherent models". This is fine and minimal enough. Optional: the abstract could add "conditionalization".
- **prop:strict(b)** ("continuous as a map into [0,∞]"): correct. The proof uses continuity only on supp p.
- **§6.1** (after def:argument-assumptions): correct and necessary. The old sentence became false once §8.1 contained (S)-failures (SSK Examples 4 and 5).
- **rem:closed-comparisons**: correct. prop:joyce-repair(b) uses closed sections with Θ = Δ through cor:closed-choice. The infinite-inside example, whose (S) needs thm:finite, is excluded by "in which we verify the hypotheses".
- **Scope**: correct. Apply F6.
- **Bibliography**:
  - BP20: Noûs 54 (2020) 162–181. Correct.
  - Nielsen21: Philos. Stud. 178 (2021) 3217–3236. Correct.
  - The keys are consistent: `Nielsen` is the 2023 Mind paper.

## 5. Compilation

In `rap80/`, three pdflatex passes give 35 pp, with:
- no errors;
- no undefined references;
- no overfull or underfull boxes;
- no LaTeX warnings.

Option A (`rap80/ldg_cut2.tex`) also compiles cleanly, to 34 pp.
