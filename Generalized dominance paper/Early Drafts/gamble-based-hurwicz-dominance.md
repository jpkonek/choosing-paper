# Dominance for sets of gambles under commission–omission penalties

## 1. Setting

Let $\Omega$ be a finite set of worlds, $|\Omega| = n \ge 2$. A **gamble** is a vector $g \in G := \mathbb{R}^{\Omega} \setminus \{0\}$, with $g_\omega$ the payoff at world $\omega$. For a real number $x$ write $x^{+} = \max(x,0)$ and $x^{-} = \max(-x,0)$.

A **model** is a Borel set $D \subseteq G$, read as the set of gambles the agent accepts, i.e. strictly prefers to the zero gamble. No structural conditions are imposed on models: they need not be cones, convex, or coherent in any sense.

For each world $\omega$, the **ideal model** at $\omega$ is
$$
D_\omega := \{ g \in G : g_\omega > 0 \},
$$
the set of gambles that actually pay at $\omega$.

For a probability vector $\theta \in \Delta(\Omega)$ and a parameter $\lambda \in [\tfrac12, 1)$ with $\mu := 1 - \lambda \in (0, \tfrac12]$, define
$$
D_\theta := \{ g \in G : \mu\, \mathbb{E}_\theta[g^{+}] > \lambda\, \mathbb{E}_\theta[g^{-}] \}.
$$
$D_\theta$ is an open convex cone (see Lemma 2). For a point mass $\theta = \delta_\omega$, $D_{\delta_\omega} = D_\omega$.

## 2. The penalty

Fix a measure $\nu$ on $G$ and $\lambda \in [\tfrac12,1)$. For a model $D$ and world $\omega$,
$$
\mathrm{Pen}_\omega(D) := 2\lambda \int_{D \setminus D_\omega} |g_\omega| \, d\nu(g) \;+\; 2\mu \int_{D_\omega \setminus D} |g_\omega| \, d\nu(g).
$$
The first term charges **commission errors**: accepting a gamble that does not pay at $\omega$, weighted by what it loses there. The second charges **omission errors**: rejecting a gamble that pays at $\omega$, weighted by what it would have won. Since $D_\omega = \{g_\omega > 0\}$, equivalently
$$
\mathrm{Pen}_\omega(D) = 2\lambda \int_{D} g_\omega^{-}\, d\nu + 2\mu \int_{G \setminus D} g_\omega^{+}\, d\nu .
$$
Write $\mathrm{Pen}(D) := (\mathrm{Pen}_\omega(D))_{\omega \in \Omega} \in [0,\infty)^{\Omega}$.

**Dominance.** $D'$ *dominates* $D$ if $\mathrm{Pen}_\omega(D') \le \mathrm{Pen}_\omega(D)$ for all $\omega$, with $\mathrm{Pen}(D') \neq \mathrm{Pen}(D)$. $D$ is *undominated* if no model dominates it. Models that differ by a $\nu$-null set have the same penalty vector and are treated as equivalent.

**Standing hypotheses on $\nu$.**

- **(H1)** $\int_G |g_\omega| \, d\nu(g) < \infty$ for every $\omega$.
- **(H2)** $\nu$ is absolutely continuous with respect to Lebesgue measure on $\mathbb{R}^{\Omega}$.

(H2) is used only to guarantee that $\nu$ has no atoms and gives zero mass to the zero set of each nonzero piecewise-linear function considered below; any weaker hypothesis delivering these two facts suffices. For the identifiability statement in Remark 3 we also use

- **(H3)** $\nu(U) > 0$ for every nonempty open $U \subseteq G$.

### Additive form

Define $k : G \to \mathbb{R}^{\Omega}$ by
$$
k_\omega(g) := 2\lambda\, g_\omega^{-} - 2\mu\, g_\omega^{+},
$$
the change in the penalty vector caused by accepting $g$ rather than rejecting it. Then for every model $D$,
$$
\mathrm{Pen}(D) = \mathrm{Pen}(\varnothing) + \int_D k \, d\nu. \tag{1}
$$
Each gamble contributes independently; nothing is normalised by $D$.

**Remark 1 (why the weighting is needed).** Take $n = 2$ and a finite $\nu$, and penalise by the unweighted symmetric difference $\nu(D \,\triangle\, D_\omega)$. On gambles with one positive and one negative coordinate, $D_1$ is the complement of $D_0$, so every such gamble lies in exactly one of $D \triangle D_0$ and $D \triangle D_1$. Hence $\nu(D \triangle D_0) + \nu(D \triangle D_1)$ is constant on all models that accept the strictly positive gambles and reject the strictly negative ones. Every such model is then undominated, coherent or not. Weighting by the payoff $|g_\omega|$ removes this constant-sum structure.

## 3. Two worlds: the cones $D_\theta$ are interval cones and the penalty is a Hurwicz score

Take $\Omega = \{0,1\}$. Every gamble with mixed signs is, up to a positive scale $c = |g_0| + |g_1|$, of one of two forms, with **breakeven** $s \in (0,1)$:

- type A: $g = c\,(1-s, -s)$ (pays at world 0);
- type B: $g = c\,(-(1-s), s)$ (pays at world 1).

For a probability $t$ of world $0$, $t g_0 + (1-t) g_1 = c(t - s)$ for type A and $c(s - t)$ for type B. For $0 \le a \le b \le 1$ let
$$
D_{a,b} := \{ g : t g_0 + (1-t) g_1 > 0 \text{ for all } t \in [a,b] \},
$$
the set of gambles strictly desirable for every probability of world 0 in $[a,b]$. Gambles positive in both coordinates lie in every $D_{a,b}$; gambles negative in both lie in none. A type A gamble lies in $D_{a,b}$ iff $s < a$; a type B gamble iff $s > b$.

**Lemma 1.** For $\theta = (\theta_0,\theta_1)$ with $\theta_0,\theta_1 > 0$, $D_\theta = D_{a,b}$ where
$$
\frac{a}{1-a} = \frac{\theta_0}{\theta_1}\cdot\frac{\mu}{\lambda}, \qquad \frac{b}{1-b} = \frac{\theta_0}{\theta_1}\cdot\frac{\lambda}{\mu}.
$$
In particular $\dfrac{b/(1-b)}{a/(1-a)} = (\lambda/\mu)^2$, i.e. $\operatorname{logit} b - \operatorname{logit} a = 2 \operatorname{logit} \lambda$. Moreover $D_{(1,0)} = D_0 = D_{1,1}$ and $D_{(0,1)} = D_1 = D_{0,0}$.

*Proof.* For type A, $\mu\mathbb{E}_\theta[g^+] > \lambda \mathbb{E}_\theta[g^-]$ reads $\mu\theta_0(1-s) > \lambda\theta_1 s$, i.e. $s/(1-s) < (\theta_0/\theta_1)(\mu/\lambda)$, i.e. $s < a$. For type B it reads $\mu\theta_1 s > \lambda\theta_0(1-s)$, i.e. $s > b$. Gambles positive in both coordinates satisfy the inequality, gambles negative in both do not. The boundary cases are immediate. $\square$

**Proposition 1 (Hurwicz representation).** Suppose $\nu$ puts no mass on the coordinate axes, and for each type $\tau \in \{A,B\}$ the scale-weighted image of $\nu$ on breakeven points is a common measure $\rho$:
$$
\int_{\{g \text{ of type } \tau,\ s(g) \in B\}} c(g)\, d\nu(g) = \rho(B) \qquad (B \subseteq (0,1) \text{ Borel}).
$$
Define $S_0(t) := 2\int_{(t,1)} (1-s)\, d\rho(s)$ and $S_1(t) := 2\int_{(0,t)} s\, d\rho(s)$. Then for $0 \le a \le b \le 1$,
$$
\mathrm{Pen}_0(D_{a,b}) = \lambda S_0(b) + \mu S_0(a), \qquad \mathrm{Pen}_1(D_{a,b}) = \lambda S_1(a) + \mu S_1(b).
$$
Since $S_0$ is decreasing and $S_1$ increasing, each penalty is $\lambda\cdot(\text{best score on } [a,b]) + \mu\cdot(\text{worst score on } [a,b])$, a Hurwicz aggregation of the single-credence score $(S_0,S_1)$. When $\rho$ is Lebesgue measure, $S_0(t) = (1-t)^2$ and $S_1(t) = t^2$, the Brier score.

*Proof.* Only mixed gambles contribute, since $D_{a,b}$ and $D_\omega$ agree on gambles of constant sign. At world 0: the omission errors are the type A gambles with $s \ge a$, each with $|g_0| = c(1-s)$; the commission errors are the type B gambles with $s > b$, also with $|g_0| = c(1-s)$. Hence $\mathrm{Pen}_0 = 2\mu \int_{[a,1)}(1-s)\,d\rho + 2\lambda\int_{(b,1)}(1-s)\,d\rho$, which equals $\mu S_0(a) + \lambda S_0(b)$ up to the atoms of $\rho$, of which there are none, since $\nu$ puts no mass on rays. World 1 is symmetric, with $|g_1| = cs$, commission errors the type A gambles with $s < a$, and omission errors the type B gambles with $s \le b$. $\square$

## 4. Main result

**Lemma 2.** Let $\theta \in \Delta(\Omega)$ and $h_\theta(g) := \theta \cdot k(g) = 2\sum_\omega \theta_\omega(\lambda g_\omega^- - \mu g_\omega^+)$. Then:

1. $\{h_\theta < 0\} = D_\theta$.
2. $D_\theta$ is an open convex cone.
3. $\nu(\{h_\theta = 0\}) = 0$.

*Proof.*

1. Immediate from the definitions.
2. Using $\lambda x^- - \mu x^+ = -\mu x + (\lambda - \mu)x^-$, we get $h_\theta(g) = 2\big(-\mu\, \theta\cdot g + (\lambda-\mu)\,\theta\cdot g^{-}\big)$. This is continuous, positively homogeneous, and convex because $\lambda \ge \mu$ and $x \mapsto x^-$ is convex. So its strict sublevel set at $0$ is an open convex cone.
3. On each closed orthant, $h_\theta(g) = -2\sum_\omega \theta_\omega w_\omega g_\omega$ with $w_\omega \in \{\mu,\lambda\}$ fixed by the orthant. Since $\theta \ne 0$ and $w_\omega > 0$, this is a nonzero linear function, so its zero set within the orthant lies in a hyperplane. Hence $\{h_\theta = 0\}$ is Lebesgue-null, and $\nu$-null by (H2). $\square$

**Theorem 1.** Assume (H1) and (H2), and $\lambda \in [\tfrac12,1)$.

1. A model $D$ is undominated if and only if $D = D_\theta$ up to a $\nu$-null set, for some $\theta \in \Delta(\Omega)$.
2. Every model that is not undominated is dominated by some $D_\theta$.

*Proof.* Let $R := \{ \int_A k \, d\nu : A \subseteq G \text{ Borel} \} \subseteq \mathbb{R}^{\Omega}$. By (H1), $A \mapsto \int_A k\,d\nu$ is a finite $\mathbb{R}^\Omega$-valued measure ($|k_\omega| \le 2|g_\omega|$), and by (H2) it has no atoms. By Lyapunov's convexity theorem, $R$ is convex and compact. By (1), $D$ is undominated iff $z_D := \int_D k\,d\nu$ is a Pareto-minimal point of $R$.

*Undominated implies $D = D_\theta$ a.e.* Suppose $z_D$ is Pareto-minimal. Then $R$ is disjoint from the open convex set $z_D + (-\infty,0)^{\Omega}$. By the separating hyperplane theorem there is $\theta \ne 0$ with $\theta \cdot r \ge \theta \cdot q$ for all $r \in R$ and all $q \in z_D + (-\infty,0)^{\Omega}$. Letting coordinates of $q$ tend to $-\infty$ gives $\theta \ge 0$, so after normalising $\theta \in \Delta(\Omega)$. Letting $q \to z_D$ gives $\theta\cdot r \ge \theta \cdot z_D$ for all $r \in R$. So $D$ minimises $A \mapsto \int_A h_\theta \, d\nu$. Taking $A = D \cup \{h_\theta < 0\}$ and $A = D \setminus \{h_\theta > 0\}$ shows $\nu(\{h_\theta<0\} \setminus D) = 0$ and $\nu(D \cap \{h_\theta > 0\}) = 0$. By Lemma 2(3), $D = \{h_\theta < 0\} = D_\theta$ up to a $\nu$-null set.

*$D_\theta$ is undominated.* By the same argument, the minimisers of $A \mapsto \int_A h_\theta\,d\nu$ are exactly the models equal to $D_\theta$ $\nu$-a.e. Suppose $D'$ dominated $D_\theta$. Then $\theta \cdot \mathrm{Pen}(D') \le \theta\cdot \mathrm{Pen}(D_\theta)$, since $\theta \ge 0$, so $D'$ is also a minimiser. Hence $D' = D_\theta$ $\nu$-a.e., so $\mathrm{Pen}(D') = \mathrm{Pen}(D_\theta)$, contradicting dominance.

*Every other model is dominated by some $D_\theta$.* Let $z_D$ not be Pareto-minimal. The set $K := \{ r \in R : r \le z_D \}$ is compact and contains some $r \neq z_D$. Let $r^*$ minimise $\sum_\omega r_\omega$ over $K$. Then $r^*$ is Pareto-minimal in $R$: anything below it lies in $K$ with a smaller sum. Also $r^* \ne z_D$, since some $r \in K \setminus\{z_D\}$ has a strictly smaller sum than $z_D$. By Lyapunov, $r^* = z_{D^*}$ for some model $D^*$, which is undominated and hence equal to some $D_\theta$ a.e. by the first part. Then $D_\theta$ dominates $D$. $\square$

## 5. Consequences and remarks

**Corollary 1 (two worlds).** For $\Omega = \{0,1\}$ and $\tfrac12 < \lambda < 1$, the undominated models are, up to $\nu$-null sets, exactly
$$
D_{a,b} \text{ with } \operatorname{logit} b - \operatorname{logit} a = 2\operatorname{logit}\lambda,\ 0 < a < b < 1, \quad \text{together with } D_0 \text{ and } D_1 .
$$
Every other Borel set of gambles, convex or not, is dominated by one of them. Under the hypotheses of Proposition 1 with $\rho$ equal to Lebesgue measure, these are the intervals that are undominated for the Hurwicz–Brier score $\lambda \cdot \text{best} + \mu \cdot \text{worst}$ over credal intervals. *(Lemma 1 and Theorem 1.)*

**Remark 2 (coherence is derived).** The competing models are arbitrary Borel sets of gambles. The undominated ones are open convex cones that contain every gamble positive in all coordinates and no gamble negative in all coordinates. These coherence properties are consequences of the theorem, not assumptions.

**Remark 3 (credal reading of $D_\theta$).** Let
$$
C_\theta := \Big\{ p \in \Delta(\Omega) : p \text{ is supported in } \operatorname{supp}\theta,\ \ \frac{p_\omega/\theta_\omega}{p_{\omega'}/\theta_{\omega'}} \le \frac{\lambda}{\mu} \text{ for all } \omega,\omega' \in \operatorname{supp}\theta \Big\},
$$
the density-ratio (DeRobertis–Hartigan) neighbourhood of $\theta$ with ratio bound $\lambda/\mu$. Then
$$
D_\theta = \{ g : \mathbb{E}_p[g] > 0 \text{ for all } p \in C_\theta \}.
$$
*Proof.* Every $p\in C_\theta$ has the form $p_\omega \propto \theta_\omega z_\omega$ with $z_\omega \in [\mu,\lambda]$, and conversely: rescale $z = p/\theta$ so that $\max z = \lambda$. Minimising $\sum_\omega \theta_\omega z_\omega g_\omega$ over $z \in [\mu,\lambda]^{\Omega}$ sets $z_\omega = \mu$ where $g_\omega > 0$ and $z_\omega = \lambda$ where $g_\omega < 0$, giving $\mu\mathbb{E}_\theta[g^+] - \lambda\mathbb{E}_\theta[g^-]$. Positivity of the minimum does not depend on the normalisation. $\square$

So the undominated models are exactly the desirability cones of density-ratio neighbourhoods with the fixed ratio bound $\lambda/\mu$, centred anywhere in the simplex. For two worlds, $C_\theta$ is the interval $[a,b]$ of Lemma 1.

Under (H3), distinct $\theta$ give $\nu$-distinct models:

- The ratios $\theta_\omega/\theta_{\omega'}$ can be read off $C_\theta$: they are $\mu/\lambda$ times the maximal ratio $p_\omega/p_{\omega'}$ over $C_\theta$. So $\theta \ne \theta'$ gives $C_\theta \ne C_{\theta'}$.
- Take $p^* \in C_{\theta'}\setminus C_\theta$, say. Separating $p^*$ from the compact convex set $C_\theta$ and subtracting a constant gives a gamble $g$ with $\min_{C_\theta}\mathbb{E}_p g > 0 > \mathbb{E}_{p^*} g$. Both strict inequalities persist on a neighbourhood of $g$, which then lies in $D_\theta \setminus D_{\theta'}$ and has positive $\nu$-measure.

**Remark 4 (independence from $\nu$).** Which models are undominated does not depend on $\nu$, beyond (H1) and (H2). The measure $\nu$ affects the penalty values: by Proposition 1 it selects the single-credence scoring rule through $\rho$. It does not affect the undominated class, which is fixed by $\lambda$ alone. In particular, every scoring rule of the form in Proposition 1 gives the same undominated intervals in the two-world case.

**Remark 5 (the precise case).** At $\lambda = \tfrac12$, $C_\theta = \{\theta\}$ and $D_\theta = \{ g : \mathbb{E}_\theta[g] > 0\}$. The undominated models are exactly the strict desirability cones of single probability functions.

**Proposition 2 (graded models add nothing).** Let a *graded model* be a Borel $f : G \to [0,1]$ (degree of acceptance), with penalty $\mathrm{Pen}(f) := \mathrm{Pen}(\varnothing) + \int f\,k\,d\nu$, which extends (1). Under (H1) and (H2), $f$ is undominated among graded models iff $f = \mathbf{1}_{D_\theta}$ $\nu$-a.e. for some $\theta$.

*Proof.* $\{\int f k\,d\nu : f\}$ equals $R$: it contains $R$, and by Lyapunov's theorem (bang-bang form) every $\int f k \, d\nu$ is attained by an indicator. The proof of Theorem 1 then applies verbatim. A minimiser of $f \mapsto \int f h_\theta\,d\nu$ must equal $1$ a.e. on $\{h_\theta < 0\}$ and $0$ a.e. on $\{h_\theta > 0\}$, and $\{h_\theta = 0\}$ is null. $\square$

## 6. Open points

1. **$\lambda = 1$.** Then $\mu = 0$, omission errors cost nothing, $D_\theta = \varnothing$, and the uniqueness steps fail. The intended treatment of this case is unclear.
2. **Infinite $\Omega$.** Lyapunov's theorem fails in infinite dimensions, so the necessity half of Theorem 1 needs a different argument, or a closure, when $\Omega$ is infinite.
3. **Penalties nonlinear in the grade.** Proposition 2 shows that interior-sensitive (Choquet-type) aggregation cannot create new undominated models if the penalty is linear in a single acceptance grade. A version with separate grades for acceptance and rejection, which need not sum to one, is a different object and has not been analysed.
4. **Hurwicz representation for $n \ge 3$.** Proposition 1 is proved only for two worlds. Whether $\mathrm{Pen}(D_\theta)$ admits a comparable "best/worst over $C_\theta$" representation for $n \ge 3$ has not been checked.

## References

- R. DeRobertis and J. A. Hartigan, "Bayesian inference using intervals of measures", *Annals of Statistics* 9 (1981), 235–244.
- A. Lyapunov, "Sur les fonctions-vecteurs complètement additives", *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya* 4 (1940), 465–478.
- M. J. Schervish, "A general method for comparing probability assessors", *Annals of Statistics* 17 (1989), 1856–1879.
