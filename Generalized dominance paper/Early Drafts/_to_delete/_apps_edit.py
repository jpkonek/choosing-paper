import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()

def rep(old, new):
    global s
    n = s.count(old)
    assert n == 1, (n, old[:80])
    s = s.replace(old, new)

R = r"{\color{red}"

# preamble
if r"\usepackage{xcolor}" not in s:
    rep(r"\usepackage{lmodern,microtype,amsmath,amssymb,amsthm,mathtools,enumitem}",
        r"\usepackage{lmodern,microtype,amsmath,amssymb,amsthm,mathtools,enumitem}" + "\n" + r"\usepackage{xcolor}")

# R1 intro of the applications section
rep(r"Improvement at every world is a stronger conclusion.",
    r"Improvement at every world is a stronger conclusion. " + R +
    r" For a finitely supported prior $p$, write $E_pL(m)\coloneqq\sum_{\omega\in\supp p}p_\omega L(m,\omega)$. Each proof below verifies selection (S) and closure under ties (T) for the ranking at hand, and then applies Corollary~\ref{cor:coherent-assigned}(c).}")

# R2 proper scores proposition and proof
rep(r"""Let $\Omega$ be finite, $\C=\Delta\subseteq\M_L$, and suppose each $p\in\Delta$ is the unique Bayes model for $p$. If $p\mapsto L(p,\omega)$ is lower semicontinuous for every world, then the undominated models are exactly the probabilities, and every other model is dominated by a probability.
\end{proposition}
\begin{proof}
A weak dominator of $p$ is also Bayes for $p$, hence equals $p$. Thus probabilities are undominated and no other model is tied with one. Bayes optimality gives, for each $m$, a world in $\supp p$ where $L(p,\omega)\le L(m,\omega)$; lower semicontinuity makes these comparison sets closed. Apply Corollaries~\ref{cor:closed-choice} and~\ref{cor:coherent-assigned}.
\end{proof}""",
    R + r"""Let $\Omega$ be finite and $\C\subseteq\M_L$. Suppose that $p\mapsto c_p$ maps $\Delta$ onto $\C$, that each $c_p$ is the unique Bayes model for $p$, and that $p\mapsto L(c_p,\omega)$ is lower semicontinuous for every world $\omega$. Then the undominated models are exactly the coherent models, and every other model is dominated by a coherent model. In particular, if $\C=\Delta$, each $p\in\Delta$ is the unique Bayes model for $p$, and $p\mapsto L(p,\omega)$ is lower semicontinuous for every world, then the undominated models are exactly the probabilities, and every other model is dominated by a probability.}
\end{proposition}
\begin{proof}
""" + R + r"""If $E_pL(c_p)=\infty$ for some $p$, every model is a Bayes model for $p$, so $\M_L=\{c_p\}$ and the claims are trivial. Assume otherwise.

\emph{Closure under ties.} If $m$ weakly dominates $c_p$, then $E_pL(m)\le E_pL(c_p)$, so $m$ is a Bayes model for $p$, and $m=c_p$. So every coherent model is undominated, $\C_L=\C$, and the only model tied at every world with $c_p$ is $c_p$ itself: (T) holds.

\emph{Selection.} If some $m$ had $L(m,\omega)<L(c_p,\omega)$ at every $\omega\in\supp p$, then $E_pL(m)<E_pL(c_p)$, as $E_pL(c_p)$ is finite; this contradicts Bayes optimality. So every model $m$ has some $\omega\in\supp p$ with $c_p\preceq_\omega m$. Each set $\{p:L(c_p,\omega)\le L(m,\omega)\}$ is $\Delta$ if $L(m,\omega)=\infty$, and closed by lower semicontinuity otherwise. So the hypotheses of Corollary~\ref{cor:closed-choice} hold with every $c_p\in\C_L$: (S) holds. Corollary~\ref{cor:coherent-assigned}(c) completes the proof.}
\end{proof}""")

# R3 event forecasts and merely proper scores
rep(r"It also applies to finitely many event forecasts on arbitrary $\Omega$: replace worlds by their finitely many truth-value patterns and assign each prior its vector of event probabilities. Continuous, strictly proper component scores give the unique Bayes forecasts, recovering",
    R + r"It also applies to finitely many event forecasts on arbitrary $\Omega$: replace worlds by their finitely many truth-value patterns $w$, with truth-value vectors $v_w$, and put $c_p\coloneqq\sum_wp_wv_w$; the coherent forecasts are exactly these vectors. Continuous, strictly proper component scores make $c_p$ the unique Bayes forecast for $p$, recovering}")
rep(r"incoherent forecasts can share coherent loss profiles and remain undominated~\cite{SSK2009}. This is precisely",
    r"incoherent forecasts can share coherent loss profiles and remain undominated~\cite{SSK2009}" + R + r"; then (T) fails}. This is precisely")

# R4 probabilism on arbitrary domains
rep(r"""Hence $L(q_n,w)\le L(m,w)$, contradicting lower semicontinuity at $q$. So probabilities are undominated. Quasi-strict propriety also excludes an incoherent model tied with a probability.""",
    r"""Hence $L(q_n,w)\le L(m,w)$, contradicting lower semicontinuity at $q$. So probabilities are undominated""" + R + r""", and $\C_L=\C$. If an incoherent $m$ were tied at every world with $q\in\C$, then $E_qL(m,\cdot)=E_qL(q,\cdot)$, contradicting quasi-strict propriety. So (T) holds.}""")
rep(r"""Apply Theorem~\ref{thm:local} with the compact space $\Theta=\C$, $c_q=q$, $K_\omega(m)=\{q:L(q,\omega)\le L(m,\omega)\}$, and $\theta_F(p)=p$. The finite-support Bayes inequalities supply condition~2(b), and lower semicontinuity supplies closedness. Corollary~\ref{cor:coherent-assigned} completes the proof.""",
    R + r"""For (S), apply Theorem~\ref{thm:local} with the compact space $\Theta\coloneqq\C$, which is closed in $[0,1]^{2^\Omega}$, $c_q\coloneqq q\in\C_L$, and $K_\omega(m)\coloneqq\{q:L(q,\omega)\le L(m,\omega)\}$, which is closed by lower semicontinuity. Given a finite set $G$ of worlds, let $F\coloneqq G$, or a single world if $G=\varnothing$, let $\theta_F(p)\coloneqq p$, viewed as a finitely supported probability, which is continuous, and let $A^F_\omega(m)\coloneqq\theta_F^{-1}(K_\omega(m))$, which is closed. Then condition~2(a) holds by definition. For condition~2(b), let $p\in\Delta_F$. Quasi-strict propriety gives $E_pL(p,\cdot)<E_pL(m',\cdot)$ for an incoherent $m'$, such as the zero credence function, so $E_pL(p,\cdot)$ is finite, and $E_pL(p,\cdot)\le E_pL(m,\cdot)$. If $L(m,\omega)<L(p,\omega)$ at every $\omega\in\supp p$, then $E_pL(m,\cdot)<E_pL(p,\cdot)$, a contradiction. So (S) holds, and Corollary~\ref{cor:coherent-assigned}(c) completes the proof.}""")

# R5 remove the earlier copy of the chance-dominance paragraph
i = s.index(r"\emph{Chance dominance.} Pettigrew's")
assert s.count(r"\emph{Chance dominance.} Pettigrew's") == 1
j = s.index("\n", i)
s = s[:i] + s[j+1:]

# R6 conditional updating
rep(r"So coherent strategies are undominated and closed under ties.",
    r"So coherent strategies are undominated" + R + r", $\C_L=\C$, and (T) holds}.")
rep(r"Its losses are lower semicontinuous, so Corollary~\ref{cor:closed-choice} applies.",
    r"Its losses are lower semicontinuous" + R + r" in $p$, since $J$ is lower semicontinuous on probabilities and $q$ and the $r_j$ are continuous in $p$. So the hypotheses of Corollary~\ref{cor:closed-choice} hold with every assigned strategy in $\C_L$: (S) holds, and Corollary~\ref{cor:coherent-assigned}(c) completes the proof}.")

# R7 Joyce
rep(r"Here selection holds with $c_p=p$, but closure under ties fails.",
    R + r"Here (S) holds: $E_pL(x)=p_1(1-d)^2+p_2(1+d)^2$ is minimised at $d=p_1-p_2$, so each $p$ is a Bayes model for itself, hence competitive on $\supp p$; the losses are continuous; and $\C_L=\Delta$, since no model is dominated. So Corollary~\ref{cor:closed-choice} applies with $c_p=p$. But (T) fails: every incoherent $x$ is tied at every world with a probability.}")

# R8 final chance-dominance subsection
i = s.index(r"\subsection{Chance dominance.}")
j = s.index(r"\bibliographystyle{plain}")
new = R + r"""
\subsection{Chance dominance}\label{sec:chance}
Pettigrew's~\cite[Chapter~10]{Pettigrew2016} chance-dominance argument compares expected rather than actual accuracy. Let $W$ be a finite nonempty set of worlds, $\mathcal F$ a set of propositions (subsets of $W$), and $\M_L\coloneqq[0,1]^{\mathcal F}$ the credence functions. Each probability $\theta$ on $W$ induces the credence function $X\mapsto\sum_{w\in X}\theta(w)$, also written $\theta$. Let $\mathcal K$ be a nonempty set of probabilities on $W$: the possible current chance functions, conditional on the agent's total evidence. Let $\C$ consist of the credence functions induced by the closed convex hull $\operatorname{cl}\operatorname{conv}\mathcal K$; these are the credence functions satisfying Probabilism and Pettigrew's ETP$^+$. Let $I:\M_L\times W\to[0,\infty)$ be a finite inaccuracy measure such that, for every probability $\theta$ on $W$, $\theta$ is the unique minimiser of $c\mapsto E_\theta I(c)\coloneqq\sum_w\theta(w)I(c,w)$ over $\M_L$, and $c\mapsto I(c,w)$ is lower semicontinuous on the credence functions induced by probabilities, for every $w$. The worlds of the ranking are the members of $\mathcal K$, and $c\preceq_{\mathrm{ch}}d$ exactly when $E_{\mathrm{ch}}I(c)\le E_{\mathrm{ch}}I(d)$.
\begin{proposition}\label{prop:short-chance}
The undominated credence functions are exactly the members of $\C$, and every other credence function is dominated by a member of $\C$.
\end{proposition}
\begin{proof}
\emph{Closure under ties.} Let $\theta\in\operatorname{cl}\operatorname{conv}\mathcal K$, and let $m$ weakly dominate $\theta$: $E_{\mathrm{ch}}I(m)\le E_{\mathrm{ch}}I(\theta)$ for every $\mathrm{ch}\in\mathcal K$. Since $W$ is finite and $I$ is finite, $\rho\mapsto E_\rho I(m)-E_\rho I(\theta)$ is affine and continuous on the probabilities on $W$. It is nonpositive on $\mathcal K$, hence on $\operatorname{cl}\operatorname{conv}\mathcal K$, and in particular at $\rho=\theta$. So $E_\theta I(m)\le E_\theta I(\theta)$, and $m=\theta$ by strict propriety. Hence every member of $\C$ is undominated, $\C_L=\C$, and the only model tied at every world with a member $\theta$ of $\C$ is $\theta$: (T) holds.

\emph{Selection.} Apply Theorem~\ref{thm:local} with the compact space $\Theta\coloneqq\operatorname{cl}\operatorname{conv}\mathcal K$, $c_\theta\coloneqq\theta\in\C_L$, and $K_{\mathrm{ch}}(m)\coloneqq\{\theta\in\Theta:E_{\mathrm{ch}}I(\theta)\le E_{\mathrm{ch}}I(m)\}$, which is closed since $\theta\mapsto E_{\mathrm{ch}}I(\theta)=\sum_w\mathrm{ch}(w)I(\theta,w)$ is lower semicontinuous. Given a finite $G\subseteq\mathcal K$, let $F\coloneqq G$, or a single member of $\mathcal K$ if $G=\varnothing$; let $\theta_F(p)\coloneqq\sum_{\mathrm{ch}\in F}p_{\mathrm{ch}}\,\mathrm{ch}$, which is continuous; and let $A^F_{\mathrm{ch}}(m)\coloneqq\theta_F^{-1}(K_{\mathrm{ch}}(m))$, which is closed. Condition~2(a) holds by definition. For condition~2(b), note that $\sum_{\mathrm{ch}\in F}p_{\mathrm{ch}}E_{\mathrm{ch}}I(c)=E_{\theta_F(p)}I(c)$ for every $c$, which is minimised at $c=\theta_F(p)$. If $E_{\mathrm{ch}}I(m)<E_{\mathrm{ch}}I(\theta_F(p))$ for every $\mathrm{ch}\in\supp p$, then $E_{\theta_F(p)}I(m)<E_{\theta_F(p)}I(\theta_F(p))$, a contradiction. So (S) holds, and Corollary~\ref{cor:coherent-assigned}(c) completes the proof.
\end{proof}
The set $\mathcal K$ may be infinite. Pettigrew's additive Bregman divergences meet the hypotheses whenever they are finite and lower semicontinuous, in particular the Brier score, which he endorses; additivity and the Bregman form are not needed. His Theorem~10.1.1 gives more: improvement under every possible chance function, by a dominator that is not even moderately modest. The proposition gives ordinary chance dominance by an undominated member of $\C$. Either way, the argument requires a normative principle concerning chance dominance, not actual-loss dominance.}

"""
s = s[:i] + new + s[j:]
open(dst, "w").write(s)
print("ok")
