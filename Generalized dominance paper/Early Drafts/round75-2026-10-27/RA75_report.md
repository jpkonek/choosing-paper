# RA75: referee report on `app_revised.tex` (application paper, round 75)

Compared: `app_revised.tex` against `app_device.tex` (round 74). Requirements: `BRIEF75_APP.md`, `AUDIT_1352.md` §§1–4, `REFL75_report.md`.

Compile check: I compiled it myself in `RA75_build/` with three pdflatex passes. Result: 17 pages, no errors, no warnings, no undefined references, no overfull or underfull boxes.

## Verdict

**Minor revision. The mathematics is sound. The text has two outright false sentences, two inaccurate glosses, and some form problems.**

- Every new formal claim I re-derived is correct:
  - (M4);
  - Proposition `prop:advice`;
  - the corrected unordered-choice identity;
  - the symmetric existence measure;
  - both grouping measures;
  - the two overlap consequences stated in the paper;
  - Corollary 4.10.
- Two sentences are false as written:
  - "A coherent model never gives contradictory advice". The paper's own Example 1.12 contradicts it.
  - "No result is claimed for every finite Borel measure". Several results, Proposition `prop:advice` among them, hold for every finite Borel measure.
- Two glosses are inaccurate:
  - (M2) as "exactly indifferent";
  - "in these cases it is demanding" in the (A4) overlap bullet. A counterexample is given below.
- One definitional sentence about what μ(B) weighs is inconsistent with "f and −f represent the same choice".
- On form, the two Remarks should become definitions and an unnamed lemma. A stray unused result in Definition 1.4 and a result stated inside the (A4) explanation should go.

## 1. Re-derivation of the new or changed claims

| Claim | Status |
|---|---|
| (∗): {α_X ≠ α_Y} = N ∪ (−N), with N = X△Y | Correct. α_X(f) = (𝟙_X(f), 𝟙_X(−f)). |
| Prop. `prop:advice` (a)⇒(c)⇒(b)⇒(d)⇒(a) | Correct. In (d)⇒(a), X := −B is a model because −B is Borel. The (⇐) half of (d), applied to X = −B and Y = ∅, gives μ(−B) = 0. |
| Bijection under (M4) | Correct. (M4) makes −X measurable, so α_X is measurable. Injectivity: X△Y ⊆ {α_X ≠ α_Y}. Surjectivity: for f ∉ Z, −f ∈ X ⟺ α(f) ∈ {against, contradictory}. Well-definedness on classes is (a)⇒(b), but the proof does not say so (optional item O2). |
| "Well defined iff μ and μ̌ have the same null sets" | Correct: (a)⇔(b). |
| Def. 1.4: (M2) and (M4) give μ{max_Q q = 0} = 0 | Correct, since {max_Q q(h) = 0} = −{P_Q = 0} and the latter is closed and null. However, nothing uses it (fix 8). |
| μ_π(B) = ½π(B∪−B) + ½π(B∩−B) | Correct. 𝟙_B + 𝟙_{−B} = 𝟙_{B∪−B} + 𝟙_{B∩−B}, and both sets are symmetric. The reading "half weight for choices touched once, full weight for choices touched twice" is also correct, since this equals ½π((B∪−B)∖(B∩−B)) + π(B∩−B). WA75's correction of REFL75's "μ(B∪−B) = 2μ_π(B)" is right. |
| μ_π is the unique symmetric extension of π | Correct. For symmetric μ, μ(B) = ∫½(𝟙_B(f)+𝟙_B(−f))dμ, and the integrand is measurable for the symmetric σ-algebra. The Remark asserts this without proof (fix 9). |
| μ_π(B) ≤ μ(B∪−B) ≤ 2μ_π(B); same null sets ⟺ (M4); (μ+μ̌)/2 = μ_π | Correct. Note that π = μ restricted to the symmetric sets. |
| Symmetric score m_ω(X) = ½∫(𝟙_X(f) − 𝟙_X(−f))f(ω)dμ | Correct: average the identity ∫g(f)dμ = ∫g(−f)dμ applied to g(f) = 𝟙_X(f)f(ω). The per-choice reading (strict ±½\|f(ω)\| per unit weight; silence and contradiction score 0) is correct. |
| Example 1.12, μ₀ + δ_𝟙 | Correct. P_Q(𝟙) = 1, so (M2) holds. μ_c = μ₀, so (M3′) holds. {−𝟙} is null and {𝟙} has mass 1. |
| Symmetric existence measure, ν = Σ(w_k/2)(δ_{g_k} + δ_{−g_k}) | Correct. It is a probability measure with full support (every g_k is an atom of ν), and ∫‖g‖dν = Σw_k‖g_k‖ < ∞. The proofs of (M1), (M2) (Fubini; λ atomless), (M3) and atomlessness are unchanged. Φ(−g,−t) = −Φ(g,t) and ν⊗λ is reflection-invariant, so μ is symmetric and (M4) holds. So it keeps (M1), (M2), (M3) = (M3′), is atomless, and satisfies (M4). |
| Sum grouping μ\|G₁⊗μ\|G₂⊗μ\|G₃/m² | Correct. Mass m³/m² = m. First marginal: μ\|G₁(A)·m·m/m² = μ\|G₁(A), and likewise for the others. Each group satisfies z ≥ x + y + κ. |
| Midpoint grouping μ\|G₁⊗μ\|G₂⊗μ\|G₃⊗μ\|G₃/(4m³) | Correct. Mass m·m·2m·2m/(4m³) = m. The marginals on G₁ and G₂ are μ\|G₁ and μ\|G₂. Each G₃ marginal is μ\|G₃·m·m·2m/(4m³) = ½μ\|G₃. Adding z ≥ (x+y)/2 + κ to z′ ≥ (x+y)/2 + κ gives z + z′ ≥ x + y + 2κ. |
| "Grouping does not matter" | Correct. For any grouping γ, ∫(replacement − withdrawn)dγ = m_ω(G₃) − m_ω(G₁) − m_ω(G₂), and the integrand meets the bound pointwise. |
| z, −z ∈ G₃ ⇒ x + y ≤ −cκ𝟙 | Correct. Add the two margin inequalities: 0 ≥ 2(x+y)/c + 2κ. |
| x ∈ G₁, −x ∈ G₂ ⇒ z ≥ κ𝟙 | Correct: z ≥ (x − x)/c + κ. The advice changes from contradictory to silence. |
| −z ∈ G₁, z ∈ G₃ reverses the advice | Correct a.e. Before: −z ∈ W and z ∉ W. After: z ∈ W′ and −z ∉ W′. The unstated consequence in WA75's notes, z ≥ (y + cκ𝟙)/(c+1), and the x, −x ∈ G₁ consequence z ≥ (\|x\| + y)/c + κ are also correct. |
| "No coherent W satisfies the hypotheses; no condition on μ is used" | Correct. The argument in Prop. 5.5 uses only μ(G₁), μ(G₂), μ(G₃) > 0 and Lemma 1.3(c). It is still a result stated inside the explanation (fix 7). |
| Corollary 4.10(a) | Correct, and it says exactly what the brief requires: under (M2), (M3′) and (A1)–(A4), with (A5) for 𝒦, every member of 𝒦 is undominated while every incoherent model is dominated. The first clause is (A5) itself; the second is Theorem 4.1. |
| Corollary 4.10(b) | Correct: it is (a) for the family of all coherent models, plus the fact that coherent and incoherent models are complementary. |
| Theorem 4.1 | Unchanged; its hypotheses are (M2), (M3′) and (A1)–(A4). |

Table of conditions against results (Remark 1.6):
- **(M1):** correct.
- **(M2):** the "used by" column is correct, including that Proposition 5.5 needs only μ{P_S = 0} = 0 and only for (A5). The plain-English gloss is wrong (fix 4).
- **(M3):** correct.
- **(M3′):** correct. "Not Sections 5 or 6" is slightly loose, because Corollary 5.6 asserts (M3′) of its measure (optional item O1).
- **(M4):** correct. Only Proposition `prop:advice` uses it, and no theorem's proof uses reflection.

## 2. Required fixes

**1. False claim about coherent models (Definition 1.9, last sentence).**
- Current text: "A coherent model never gives contradictory advice, since $D_Q\cap(-D_Q)=\emptyset$."
- Why it is wrong: models are identified a.e. In Example 1.12, the model D_S ∪ {−𝟙} equals D_S a.e., so it is coherent. Yet it gives contradictory advice on {𝟙}, a choice of measure 1. In general, if X = D_Q ∪ N with N null, X gives contradictory advice exactly on a subset of N ∪ (−N). That set is null under (M4), but not otherwise.
- Replace with:
  > The model $D_Q$ never gives contradictory advice, since $D_Q\cap(-D_Q)=\emptyset$. Under (M4), a model equal a.e.\ to $D_Q$ gives contradictory advice only on a null set (Proposition~\ref{prop:advice}).

**2. False claim about every finite Borel measure (Remark 1.6, second paragraph).**
- Current text: "No result is claimed for every finite Borel measure: the conditions are substantive assumptions, and (M2) and (M3$'$) are hypotheses of Theorem~\ref{thm:dominance}."
- Why it is wrong: Proposition `prop:advice`, Lemmas 1.3, 1.14(a)–(c), 1.15, 1.17(a)(c), 4.2, 4.3 and 4.5 all hold for every finite Borel measure.
- Replace with:
  > The main results are not claimed for every finite Borel measure: Theorem~\ref{thm:dominance} and Corollary~\ref{cor:admissible} assume (M2) and (M3$'$), and the results of Sections~\ref{sec:integral} and~\ref{sec:repair} assume (M1) and (M2). These conditions are substantive assumptions.

**3. What μ(B) weighs (Remark 1.6, first paragraph).**
- Current text: "$\mu(B)$ is the weight of the opportunities represented by the gambles in $B$."
- Why it is unclear: by Definition 1.9, B and −B represent the same choices, yet μ(B) ≠ μ(−B) in general. Even for symmetric μ, if B ∩ −B = ∅ then B and B ∪ −B represent the same choices but μ(B ∪ −B) = 2μ(B). The (A4) explanation already counts in single judgements ("Judgements, not whole choices"), so the definition must say so too.
- Replace the first paragraph with:
  > Each gamble $f$ represents a binary choice, and a model judges $f$ and $-f$ separately (Definition~\ref{def:advice}); each choice therefore offers two opportunities to give a judgement, one for each way round. The measure $\mu$ gives the relative frequency or importance of these opportunities: $\mu(B)$ is the weight of the opportunities to judge the gambles in $B$.

  (Fix 9 moves this text into Definition 1.4.)

**4. Wrong gloss of (M2) (table, row (M2)).**
- Current text: "the choices on which $Q$ is exactly indifferent, those with $P_Q(h)=0$".
- Why it is wrong: P_Q(h) = 0 does not mean Q is indifferent. The upper prevision of h may be positive. The set is the boundary of D_Q: gambles on which D_Q is silent but which lie at the edge of acceptance.
- Replace with:
  > the gambles on the boundary of what $D_Q$ accepts, those with $P_Q(h)=0$, carry no weight.

**5. Definition of the grouping misstates the midpoint marginals ((A4) Explanation, item "What the masses supply").**
- Current text: "a measure on matched groups of opportunities drawn from the three parts, whose marginals are the restricted measures."
- Why it is wrong: in the midpoint form, the two G₃ marginals are each ½μ|_{G₃}, not the restricted measure.
- Replace with:
  > a finite measure on $G_1\times G_2\times G_3$ (sum triples) or on $G_1\times G_2\times G_3\times G_3$ (midpoint triples) whose marginals on the first two factors are $\mu|_{G_1}$ and $\mu|_{G_2}$ and whose marginals on the remaining factors add up to $\mu|_{G_3}$.

**6. Overlap bullet ((A4) Explanation, item "Judgements, not whole choices").** It has three problems:
- (i) "one choice contributes a judgement to two of the parts" is wrong when i = j. For example, z, −z ∈ G₃ is G₃ ∩ −G₃, a case the bullet itself treats.
- (ii) "no further assumption is involved" is unclear.
- (iii) "in these cases it is demanding" is **false** in general. Counterexample with c = 1 and κ = 1:
  - G₁ is a small ball around 𝟙, G₂ a small ball around −10·𝟙, and G₃ a small ball around −𝟙 (radius 1 suffices; worst case −2 ≥ 2 − 9 + 1).
  - G₁ meets −G₃.
  - The consolidation turns correct strict advice for sure gains into strict advice for sure losses, and pays for this by withdrawing the sure-loss judgements near −10𝟙.
  - The payoff inequality is not demanding here. This is exactly the compensation commitment.
- Replace the whole bullet with:
  > \item \emph{Judgements, not whole choices.} The grouped units are single judgements, each the acceptance of one gamble, weighted by $\mu$; a choice offers two of them, one for each way round (Definition~\ref{def:measure}). When some $G_i$ meets $-G_j$ (possibly with $i=j$), both judgements on one choice fall in the parts, in opposite orientations. For instance, if $-z\in G_1$ and $z\in G_3$, the consolidation reverses the advice on that choice. The payoff inequality still compares single judgements, so these cases need no separate treatment. Two of them have direct consequences. If $z$ and $-z$ both lie in $G_3$, then $x+y\le-c\kappa\one$ for all $x\in G_1$ and $y\in G_2$: contradictory advice is supplied only in place of withdrawn pairs that lose at least $c\kappa$ at every world. If $x\in G_1$ and $-x\in G_2$, so that contradictory advice is withdrawn, then $z\ge\kappa\one$ for every $z\in G_3$.

**7. A result stated inside the (A4) explanation (item "The remaining commitment", last sentence).**
- Current text: "No coherent model satisfies the hypotheses on $W$; the argument in the proof of Proposition~\ref{prop:axioms} uses no condition on $\mu$."
- Why it must change: this is a lemma stated in prose with a pointer into another proof, which the brief does not allow.
- **Step 1.** Insert the following after Definition `def:consolidation`:
  > ```latex
  > \begin{lemma}\label{lem:Wincoherent}
  > Let $(G_1,G_2,G_3)$ be a margin triple. No coherent model $W$ satisfies $G_1\cup G_2\subseteq W$
  > a.e.\ and $W\cap G_3$ null.
  > \end{lemma}
  > \begin{proof}
  > Suppose $W=D_Q$ a.e.\ does. As $G_1$ and $G_2$ are non-null, there are $x\in G_1\cap D_Q$ and
  > $y\in G_2\cap D_Q$. For every $z\in G_3$, $z\ge(x+y)/c+\kappa\one$, so by
  > Lemma~\ref{lem:states}(c), $P_Q(z)\ge(P_Q(x)+P_Q(y))/c+\kappa>0$. So $G_3\subseteq D_Q$; as $G_3$
  > is non-null, $G_3\cap W$ is not null, a contradiction.
  > \end{proof}
  > ```
- **Step 2.** Replace the sentence in the explanation with:
  > By Lemma~\ref{lem:Wincoherent}, (A4) constrains the comparison only for incoherent $W$.
- **Step 3.** In the proof of Proposition 5.5, replace the paragraph "\emph{No coherent model could make this change.} ... a contradiction." with:
  > \emph{No coherent model could make this change}, by Lemma~\ref{lem:Wincoherent}.

**8. Remove an unused result from Definition 1.4.**
- Current text: "Under (M4), $-X$ is null whenever $X$ is null; and (M2) then also gives $\mu\{h:\max_{q\in Q}q(h)=0\}=0$ for every credal set $Q$, because this set is $-\{P_Q=0\}$."
- Why: nothing uses the second clause.
- Replace with:
  > Under (M4), $-X$ is null whenever $X$ is null.

**9. Remarks become definitions and an unnamed lemma.** The author forbade remarks, and `app_device.tex` had none. Neither Remark is purely definitional: Remark 1.6 contains a claim about the results, and Remark 1.11 contains five unproved claims.
- (a) **Delete Remark 1.6** (`rem:measure`). Then:
  - Insert the fix-3 paragraph into Definition 1.4, after "outside a null set.".
  - Append the fix-2 paragraph, preceded by "Each result below holds uniformly over every $\mu$ that satisfies the conditions the result states; beyond those conditions, no particular distribution of advice opportunities is assumed.", to the end of Definition 1.5 (`def:atoms`). Follow it with the table, with fix 4 applied. That is where the old "uses" paragraph was, and (M3′) is defined there.
  - Change `Remark~\ref{rem:measure}` in the (A4) explanation to `Definition~\ref{def:measure}`.
  - Delete the sentence "Remark~\ref{rem:unordered} shows how a distribution over unordered choices yields such a measure."
- (b) **Replace Remark 1.11** (`rem:unordered`) with the following:
  ```latex
  \begin{definition}[Unordered choices]\label{def:unordered}
  A set $B\subseteq E$ with $B=-B$ is \emph{symmetric}; it represents a set of unordered choices.
  The symmetric Borel sets form a $\sigma$-algebra $\mathcal S$. A \emph{distribution over
  unordered choices} is a finite measure $\pi$ on $\mathcal S$. Its \emph{equal split} is
  \[
    \mu_\pi(B)\coloneqq\int\tfrac12\bigl(\one_B(f)+\one_B(-f)\bigr)\,d\pi(f)\qquad(B\text{ Borel}),
  \]
  which gives each way round of a choice half the weight of the choice.
  \end{definition}

  \begin{lemma}\label{lem:unordered}
  Let $\pi$ be a distribution over unordered choices.
  \begin{enumerate}[label=(\alph*)]
    \item $\mu_\pi$ is the only symmetric Borel measure that agrees with $\pi$ on $\mathcal S$, and
    $\mu_\pi(B)=\tfrac12\pi(B\cup(-B))+\tfrac12\pi(B\cap(-B))$ for every Borel $B$.
    \item Let $\mu$ be a Borel measure that agrees with $\pi$ on $\mathcal S$. Then
    $(\mu+\check\mu)/2=\mu_\pi$, and $\mu$ has the same null sets as $\mu_\pi$ if and only if $\mu$
    satisfies (M4).
    \item If $\mu$ is symmetric and satisfies (M1), then $m_\omega(X)=\tfrac12\int\bigl(\one_X(f)-
    \one_X(-f)\bigr)f(\omega)\,d\mu(f)$ for every model $X$ and world $\omega$.
  \end{enumerate}
  \end{lemma}

  \begin{proof}
  For Borel $B$, $f\mapsto\one_B(f)+\one_B(-f)$ equals $\one_{B\cup(-B)}+\one_{B\cap(-B)}$, so it
  is $\mathcal S$-measurable. Hence $\mu_\pi$ is a Borel measure (by monotone convergence), it is
  symmetric, it agrees with $\pi$ on $\mathcal S$, and the formula in (a) holds. If $\mu$ agrees
  with $\pi$ on $\mathcal S$, then, as the integrand is $\mathcal S$-measurable,
  $\tfrac12(\mu(B)+\mu(-B))=\int\tfrac12(\one_B(f)+\one_B(-f))\,d\mu(f)=\mu_\pi(B)$; this is the
  first claim of (b), and for symmetric $\mu$ it gives $\mu=\mu_\pi$, the uniqueness in (a). By
  (a), $\mu_\pi(B)\le\pi(B\cup(-B))=\mu(B\cup(-B))\le2\mu_\pi(B)$, so $\mu_\pi(B)=0$ if and only
  if $\mu(B\cup(-B))=0$. Under (M4), $\mu(B)=0$ if and only if $\mu(B\cup(-B))=0$; conversely,
  the null sets of the symmetric measure $\mu_\pi$ are closed under reflection. (c) For symmetric
  $\mu$, $\int g(f)\,d\mu(f)=\int g(-f)\,d\mu(f)$ for integrable $g$; apply this to
  $g(f)\coloneqq\one_X(f)f(\omega)$ and average.
  \end{proof}
  ```
- Follow-up edits for (b):
  - Change `(Remark~\ref{rem:unordered})` in the (A4) explanation to `(Definition~\ref{def:measure})`.
  - If the author wants the reading of (c) (strict advice ±½|f(ω)| per unit weight; silence and contradictory advice score 0), it belongs in the gloss on the score, not here. It is not needed for the formal core.
  - Example 1.12 may stay. It explains why (M4) is stated separately.

**10. Garbled condition in the bijection clause (statement of Proposition `prop:advice`).**
- Current text: "with $\alpha(-f)=\alpha(f)$ with ``for'' and ``against'' exchanged, for a.e.\ $f$".
- Why it must change: the displayed equation α(−f) = α(f) is false as written.
- Replace with:
  > such that, for a.e.\ $f$, $\alpha(-f)$ is $\alpha(f)$ with ``for'' and ``against'' exchanged.

## 3. Form check (brief items 1–5)

- **Named definitions:** all 18 definitions are named.
- **Axiom names:** the axioms have names.
- **Unnamed results:** no lemma, theorem, proposition or corollary is named.
- **Notation:** `\coloneqq` is used throughout, and there is no `:=`.
- **Wording:** none of the jargon words appear. There is no introduction, summary, discussion, literature or version commentary.
- **Remark 1.6:** this is the only sentence that summarises results (now fix 2). The brief mandates it, so it stays, as a definitional paragraph.
- **(A4) explanation:** it stays within "explaining the axiom", apart from the item fixed in fix 7. It is longer than "compact" (≈45 lines; see O3).
- **Advice states:** brief item 2 is met.
- **Two conclusions:** brief item 5 is met.
- **Integral ranking and repair:** brief item 6 is met. Sections 5–6 are unchanged apart from (M4) in Corollary 5.6 and the symmetric measure.

## 4. Optional suggestions

- **O1.** Table, row (M3′): replace "not Sections~\ref{sec:integral} or~\ref{sec:repair}" with "no result in Sections~\ref{sec:integral} or~\ref{sec:repair} assumes it".
- **O2.** Proof of Proposition `prop:advice`, start of "Bijection.": add "By (b), $\alpha_X$ depends only on the class of $X$."
- **O3.** (A4) explanation: shorten the "Every context" item to its first and last sentences. The four state transitions follow from Definition 1.9.
- **O4.** Item "The two forms": "judgement ... paying at least κ more" should be "the gamble in each supplied judgement pays at least κ more". Judgements do not pay.
- **O5.** Item 7 of the brief: WA75's answer (no change to the axiom; units are judgements) is mathematically sound. The counterexample in fix 6 shows that in the overlap case −z ∈ G₁, z ∈ G₃, (A4) can endorse reversing correct strict advice on sure-gain choices. That is an instance of the compensation commitment, which the text already states. The authors may want to know this case exists. Nothing in the formal core needs to change.
