# N79 report: Nielsen (2023), "Accuracy and probabilism in infinite domains", Mind 132

## Results first

| Condition | Verdict | Label |
|---|---|---|
| (E) evaluability | HOLDS: every ranking evaluates every credence function | PROVED |
| (A) coherent admissibility | HOLDS: every finitely additive probability is undominated under *every* admissible J | PROVED |
| (S) selection | HOLDS via thm:bayes-infinite (so via thm:local), for the whole admissible class | PROVED |
| (T) closure under ties | HOLDS for the whole admissible class | PROVED |

Every condition follows from quasi-strict propriety (QSP) together with lower semicontinuity (lsc) of q ↦ J(q,w) on P at each world. Nielsen's "continuity on P" implies that lsc (take p = v_w). So all four conditions hold for every measure Nielsen calls admissible. They also hold for LDG's larger class (QSP + lsc), with or without local boundedness. No subclass fails.

**thm:nielsen is correct** (CHECKED line by line, §3 below). The claim that it "removes a boundedness assumption of Nielsen for ordinary dominance" is correct. It needs two qualifications.
- Nielsen's §4.2.1 question concerns his Theorem 1, whose conclusion is *strict* dominance. Both of his normative premisses also use strict dominance. So LDG answers a weakened question.
- Nielsen's Theorem 2 (no probability is dominated) already dropped local boundedness (his note 27). What is new is weak domination of every incoherent credence, and hence dominance, without local boundedness.

**One sentence in LDG §8 is wrong:** "Whether strict dominance holds without local boundedness remains open." Under thm:nielsen's own hypotheses (QSP + lsc), the answer is negative even on two worlds: SSK Example 2 (ex:ssk-sharp) lifts to Nielsen's setting (§5, item C). Under Nielsen's continuity hypothesis, the answer is positive on finite domains, by prop:strict(b), and it even gives uniform dominance. The question remains open only for infinite domains under continuity (UNCLEAR).

**LDG does not improve on Nielsen's conclusion.** Nielsen's proof of Theorem 1 already gives uniform dominance, with margin D_J(c,p*) = min_q D_J(c,q), although he states only strict dominance (his eq. (9)). What LDG gains is in the hypotheses:
- lsc at each world replaces continuity of q ↦ E_p J(q) for every p;
- local boundedness is not needed for ordinary dominance.

---

## 1. Nielsen's setting, precisely

- **Worlds.** W is an arbitrary nonempty set. Propositions are all subsets, 2^W. There are no measurability restrictions; note 13 says an algebra could be handled, but this is not done.
- **Models.** Credence functions c: 2^W → [0,1]. The set is C = [0,1]^{2^W}, with the product topology (note 20).
- **Coherent class.** P is the set of "probabilistic" credence functions: c(W) = 1 and finite additivity on disjoint pairs. These are exactly the finitely additive probabilities on the full power set (note 14: "This is finite additivity"). P is compact (note 20).
- **Inaccuracy measures.** J: C × W → [0,∞]. Extended values are allowed.
  - No additivity or separability across propositions is assumed: J is an arbitrary function, and Nielsen notes he follows Pettigrew 2022 in dropping additivity (note 17).
  - Not bounded. Only *local boundedness on P* is assumed: sup_w J(p,w) < ∞ for each p ∈ P. There is no uniform bound over P (note 23), and incoherent credences may have infinite inaccuracy.
  - Expectation: E_p f = sup{E_p h : h bounded, h ≤ f} for f ≥ 0 (Appendix A, eq. (1)).
- **Admissible** (§3.1.2): QSP + continuity on P + local boundedness on P.
  - *QSP*: "E_p(J(p)) ≤ E_p(J(c)) for all p ∈ P and all c ∈ C, with strict inequality if c ∈ C\P."
  - *Continuity on P*: for every p ∈ P, q ↦ E_p(J(q)) is continuous on P. This is continuity in the *evaluated* credence, restricted to P, as a [0,∞]-valued map.
- **Dominance notions** (§3.1.3, §4.1).
  - "Accuracy-dominance": J(c,w) < J(c',w) for all w. This is LDG *strict* dominance.
  - "Weak accuracy-dominance": ≤ everywhere and < somewhere. This is LDG *dominance*.
- **Theorem 1** (§3.2, proof in App. C): if J is admissible and c is non-probabilistic, some probabilistic credence function accuracy-dominates c (strictly, at every world).
- **Theorem 2** (§4.1, proof in App. D): if J is admissible and p ∈ P, no credence function weakly accuracy-dominates p. Note 27 says local boundedness is not used, so the theorem holds under QSP + continuity on P alone.
- **Argument 1**: admissibility + "Normative Premiss for Probabilism" (accuracy-dominated, i.e. strictly, under every admissible measure ⇒ irrational) + Theorem 1.
- **Argument 2**: admissibility + "Weak Normative Premiss" + Theorems 1 and 2. The Weak Normative Premiss reads: strictly dominated under every admissible measure, by a c' that is not weakly accuracy-dominated, ⇒ irrational.
- **Side results.**
  - Note 24: admissible measures exist, including a nontrivial one due to Pruss.
  - §4.2.1: an example (1) that is QSP and not locally bounded, for which Theorem 1's conclusion holds but continuity and Theorem 2 fail.
  - §4.2.2: no strictly proper J exists when W is infinite (a cardinality argument).
  - §4.2.1: the open question "whether Theorem 1 can be generalized by relaxing local boundedness on P."

## 2. Translation into LDG

- Ω = W. M = C = [0,1]^{2^Ω}. The coherent class (LDG's C) = P, the finitely additive probabilities.
- 𝔏 = {loss rankings generated by J : J admissible}. For each L ∈ 𝔏, M_L = M, and m ⪯_ω m' iff J(m,ω) ≤ J(m',ω).
- For LDG's thm:nielsen, the family is the larger class {J : QSP, and q ↦ J(q,ω) lsc on P for every ω}. All verdicts below hold for this larger class as well.

**Continuity implies lsc (PROVED).** For f ≥ 0, E_{v_w} f = f(w), including the case f(w) = ∞ (use h = min(f,n)). So continuity on P with p = v_w gives continuity of q ↦ J(q,w) on P, hence lsc.

## 3. The conditions

### (E) HOLDS (PROVED)
Each ranking has M_L = M. 𝔏 is nonempty: J = 0 on P×W and J = 1 off P is admissible (Nielsen, note 24). It is also lsc on P.

### (A) HOLDS (PROVED)
Under every admissible J, and indeed under every QSP + lsc J, every q ∈ P is undominated, so C_L = C. I checked LDG's proof line by line.
- **Finite expected loss.** E_q L(q) is finite: QSP gives E_q L(q) < E_q L(0), where 0 is the zero credence function, which is incoherent and evaluable. A strict inequality in [0,∞] forces the left side to be finite.
- **Equality and finiteness.** If L(m) ≤ L(q) with L(m,w) < L(q,w), then monotonicity of E_q and QSP give E_q L(m) = E_q L(q). Also L(m,w) is finite.
- **Mixing.** Put q_n = (1/n)δ_w + (1−1/n)q. Linearity of E in the probability holds for [0,∞]-valued f with the sup definition: ≤ is immediate, and ≥ follows by taking h1 ∨ h2.
- **The chain.** It gives (1/n)L(q_n,w) + (1−1/n)E_q L(q_n) ≤ (1/n)L(m,w) + (1−1/n)E_q L(q). The right side is finite, so every term on the left is finite. QSP at q then gives L(q_n,w) ≤ L(m,w).
- **Limit.** q_n → q pointwise on subsets, and lsc at w gives L(q,w) ≤ L(m,w), a contradiction.

This is exactly Nielsen's proof of Theorem 2 (App. D, eqs. (10)–(14)). Nielsen's step (13)→(14) uses continuity only through liminf J(p_n,w) ≥ J(p,w), that is, lsc at one world.

Failure without lsc: in Nielsen's example (1), §4.2.1, which is QSP but not continuous, p' is dominated by every p ≠ p'. So lsc is doing real work for (A).

### (S) HOLDS (PROVED), route: thm:bayes-infinite
This is an instance of thm:local via the remark after it, with K_ω(m) = {θ : L(c_θ,ω) ≤ L(m,ω)} and θ_F = σ_F.
- **Compact family.** Θ = P with the product topology. P is closed in [0,1]^{2^Ω}, since normalisation and each additivity equation involve finitely many coordinates. By Tychonoff it is compact (and Hausdorff, though this is not needed). Put c_θ = θ.
- **(i) lsc.** θ ↦ L(θ,ω) is lsc on P. This is the hypothesis of thm:nielsen, and it is implied by Nielsen's continuity on P (§2).
- **Linked sets.** Every finite nonempty F is linked. Every world lies in one, and finite unions are finite.
- **Continuous σ_F.** σ_F(p) = the finitely supported probability p, viewed in P. It is continuous because each coordinate A ↦ Σ_{ω∈F∩A} p_ω is linear in p.
- **Bayes choice and competitiveness.** For finitely supported p and f ≥ 0, E_p f = Σ_{ω∈supp p} p_ω f(ω), the same convention as LDG's π·L. So QSP gives p·L(p) ≤ p·L(m) for every m, and p is a Bayes model for itself; its prior has support supp p. Lemma bayes-competitive then gives competitiveness on supp p, which is the serving condition.
- **Closed guarantee sets.** K_ω(m) is closed by lsc, and it is all of Θ when L(m,ω) = ∞. Its preimage under σ_F is closed.
- **Assigned models are undominated and coherent.** By (A), C_L = C.

Conclusion: every credence function is weakly dominated by a finitely additive probability. Local boundedness is never used.

### (T) HOLDS (PROVED)
If L(m) = L(q) with q ∈ P, then E_q L(m) = E_q L(q), so m ∈ P by the strict clause of QSP. Since C_L = C, m ∈ C_L.

When W is infinite, Nielsen's cardinality argument (§4.2.2) shows that distinct probabilities with identical profiles always exist. That is harmless here, because ties stay inside C_L.

**Conclusion of thm:argument for this family:** U_L = C_L = P for each admissible J, and every incoherent credence is dominated by an undominated probability. CHECKED.

## 4. What Nielsen proves beyond LDG's conclusion, and whether §5 recovers it

1. **Strict dominance (Theorem 1), and in fact uniform dominance.** Nielsen's eq. (9) reads J(p*,w) ≤ J(c,w) − D_J(c,p*) at every w with J(c,w) < ∞. Local boundedness gives J(p*,·) finite. So his proof yields LDG's *uniform* dominance with margin min_q D_J(c,q) > 0, though he states only strict dominance (PROVED, by reading his App. C).
   - Recovery: LDG recovers this in thm:nielsen ("Uniform dominance") with QSP + lsc + local boundedness. It uses thm:margin (§5) plus a separate argument that D is lsc on P, which is Nielsen's Lemmas 2–4. §5 alone does not suffice: prop:strict is finite-Ω only.
   - Gain: LDG's hypotheses are weaker. It needs lsc at each world rather than continuity of q ↦ E_p J(q) for all p. Nielsen uses the latter at p = p* in passing from (8) to (9).
2. **Dominators are undominated coherent models (Theorem 2).** LDG recovers this, with lsc in place of continuity (CHECKED).
3. **Normative premisses.** Both of Nielsen's premisses are stated with *strict* dominance. LDG's dominance principle uses ordinary dominance, so its normative premiss is stronger: it declares more models irrational. Without local boundedness, LDG's ordinary-dominance result does not feed either of Nielsen's premisses.
4. **Side results with no LDG counterpart, and none needed:** existence of nontrivial admissible J (note 24), non-existence of strictly proper J on infinite W (§4.2.2), and example (1).

### The strict-dominance question (the "nearby result")
- **lsc only, local boundedness dropped: strict dominance FAILS, even on two worlds** (PROVED; numerically sanity-checked).
  - Take W = {1,2}, write a = c({1}) and b = c({2}), and put
    L(c,1) = (1−a)² + g0(b) + c(∅)² + (1−c(W))²,
    L(c,2) = a² + g1(b) + c(∅)² + (1−c(W))²,
    with g0, g1 as in ex:ssk-sharp.
  - The expected loss separates into three parts, each with a unique minimiser at q, and V is finite. So the loss is strictly proper, hence QSP. It is lsc along P and not locally bounded: L(δ_1,2) = ∞.
  - Take m with a = 1/2, b = 0, c(∅) = 0, c(W) = 1. Then L(m) = (1/4, ∞).
  - Any c' with L(c',1) < 1/4 has b' = 0, so L(c',2) = ∞. Hence no model strictly dominates m. δ_1 dominates it, as thm:nielsen says.
- **Continuity at each world, finite W, local boundedness dropped: uniform dominance HOLDS** (PROVED). prop:strict(b) applies with c_p = p, because V(p) = E_p L(p) is finite by QSP, p is Bayes for itself, and the losses along p are continuous. Incoherent m is Bayes for no prior, by strict QSP. This answers Nielsen's §4.2.1 question positively for finite domains.
- **Continuity at each world (or Nielsen's continuity on P), infinite W, local boundedness dropped: UNCLEAR.** The obstacles are two.
  - Without bounded L(q'), q ↦ E_q L(q) need not be upper semicontinuous on P.
  - thm:margin with x = K on Ω_∞ would demand a uniform bound on the worlds where L(m) = ∞, which is more than strict dominance needs.

## 5. Is LDG §8 still accurate under the current axioms? Sentences to change

The proof of thm:nielsen is correct under the current axioms. It verifies (A), (S) (via thm:bayes-infinite), and (T) in exactly the current form, and it needs no change. The following text does need changes.

**A.** Line 704: "Nielsen's Theorem~1~\cite{Nielsen} concludes strict dominance, assuming in addition continuity of $q\mapsto E_pL(q,\cdot)$ for every $p\in\C$ and local boundedness, $\sup_\omega L(q,\omega)<\infty$ for every $q\in\C$."
- Problems:
  - "in addition" suggests Nielsen also assumes LDG's lsc.
  - The sentence omits that his proof yields uniform dominance.
  - It omits that his Theorem 2 already lacks local boundedness.
- Replace with:
  > Nielsen's Theorem~1~\cite{Nielsen} assumes quasi-strict propriety, continuity of $q\mapsto E_pL(q,\cdot)$ on $\C$ for every $p\in\C$ (with $p=\delta_\omega$ this includes continuity of $q\mapsto L(q,\omega)$), and local boundedness, $\sup_\omega L(q,\omega)<\infty$ for every $q\in\C$. It states strict dominance by a probability; its proof gives uniform dominance, with margin $\min_{q\in\C}D(q)$, as here. His Theorem~2, that no probability is dominated (``weakly accuracy-dominated'' in his terms), does not use local boundedness~\cite[note~27]{Nielsen}, and its proof uses continuity only through lower semicontinuity at one world; the first step of the proof above is that argument.

**B.** Line 704: "Theorem~\ref{thm:nielsen} needs only lower semicontinuity at each world, and drops local boundedness for ordinary dominance, which answers the question of~\cite[\S4.2.1]{Nielsen} for that conclusion."
- Problem: the sentence is correct, but it overstates the reach of the answer. Nielsen's question and both of his premisses concern strict dominance.
- Replace with:
  > Theorem~\ref{thm:nielsen} replaces continuity of expectations by lower semicontinuity at each world, and drops local boundedness for ordinary dominance, which Nielsen calls weak accuracy-dominance. This answers the question of~\cite[\S4.2.1]{Nielsen} for ordinary dominance; his question concerns his Theorem~1, whose conclusion is strict dominance, and both of his normative premisses are stated with strict dominance.

**C.** Line 704: "Whether strict dominance holds without local boundedness remains open." The sentence is FALSE as stated under thm:nielsen's hypotheses. Replace with:
> For strict dominance, local boundedness cannot simply be dropped under the hypotheses of Theorem~\ref{thm:nielsen}, even on two worlds. In Example~\ref{ex:ssk-sharp}, read $f=(c(\{1\}),c(\{2\}))$ for a credence function $c$ on the subsets of $\{1,2\}$ and add $c(\varnothing)^2+(1-c(\Omega))^2$ to the loss at each world. The result is quasi-strictly proper and lower semicontinuous along the probabilities, and the credence function with $c(\{1\})=\frac12$, $c(\{2\})=0$, $c(\varnothing)=0$ and $c(\Omega)=1$ is dominated by $\delta_1$ but strictly dominated by no model. If instead each $q\mapsto L(q,\omega)$ is continuous on $\C$, as Nielsen assumes, and $\Omega$ is finite, then Proposition~\ref{prop:strict}(b) gives uniform dominance of every incoherent model by a probability without local boundedness: $V(p)=E_pL(p,\cdot)$ is finite, each $p$ is a Bayes model for itself, and no incoherent model is a Bayes model. Whether strict dominance holds without local boundedness on infinite domains, under continuity, remains open.

**D.** Intro, line 55: "Probabilism on arbitrary domains holds under quasi-strict propriety and lower semicontinuity of the loss at each world, which removes a boundedness assumption of Nielsen~\cite{Nielsen} for ordinary dominance." This is accurate. An optional sharpening:
> ..., which weakens Nielsen's continuity assumption~\cite{Nielsen} and, for ordinary dominance, removes his boundedness assumption.

**E.** Optional, footnote to def:dominance: add
> Nielsen~\cite{Nielsen} calls our dominance ``weak accuracy-dominance'' and our strict dominance ``accuracy-dominance''.

**F.** Optional, in the "Uniform dominance" paragraph: credit the argument that D is lsc and attains a positive minimum to Nielsen's Lemmas 2–4. At present it cites "Lemmas 1 and 3".

Check files: /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r79/n79chk/chk.py (numerical sanity check of the item C example).
