# R1: additive rankings on decomposable domains (notes, 12 Oct 2026)

Labels: **PROVED** (full proof given here), **CHECKED** (verified, proof sketched or delegated to a cited proof whose steps were re-read for the new setting), **CONDITIONAL** (proved from a cited result that I did not fully re-verify), **CONJECTURE**.

Citations: v3 = *Full Coverage by Homothetic Credal Families v3*; LDG = *Loss Dominance Generalized v2*; NAL = *nonadditive_losses.tex*; DCE = *Domain Closure and Extendability*; NOGO = *CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md*; PB = *TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md* (device, CPM folder; read for §4 only); v19 = *LSP_CPMs_v19b.tex*.

---

## 0. Setting and two corrections to the brief's summary

Setting as in the brief. $H=\{g_1>0\}$, Gaussian $\mu$, $P(g)=\{i:g_i>0\}$, $N(g)=\{i:g_i<0\}$. A pair is *mixed* if $P,N\neq\varnothing$. A pair $g\in H$ stands for the binary choice represented by $g$. The kinds of advice a model gives on it are: $+$ (it accepts $g$ and not $-g$), $0$ (no advice, or silence: it accepts neither), $-$ (it accepts $-g$ and not $g$), $\times$ (contradictory advice: it accepts both). For an orientation $h\in\{g,-g\}$, "accepting $h$" means $+$ if $h=g$ and $-$ if $h=-g$.

An **additive ranking on a decomposable domain**: a measurable **advice range** $A(g)\neq\varnothing$ at each pair $g$, i.e. the kinds of advice that evaluable models give on the choice represented by $g$; the class of evaluable models $\mathcal M$ is the set of all measurable models whose advice at (a.e.) $g$ lies in $A(g)$. This class is closed under splicing and under convergence in measure, so it is a decomposable domain. The restriction concerns only which models are evaluated; the choices themselves are unchanged. Measurable penalties $\ell_i(g,a)$, $a\in A(g)$; $L_i(X)=\int_H\ell_i(g,a_X(g))\,d\mu$, assumed finite for every $X\in\mathcal M$ (equivalently $\max_{a\in A(g)}|\ell_i(g,a)|$ integrable; take the evaluable model whose advice is pointwise worst).

Corrections (both checked against v3 lem:bayes-necessary and LDG thm:kkm):

* **C1.** "Every $p$-Bayes model is coherent for every $p\in\Delta$" is *not* forced at boundary priors. What is forced: at interior priors every Bayes model is coherent and Bayes advice is a.e. unique (Lemma 1.4); at every prior a coherent Bayes model exists (Lemma 1.3(a)); at vertices the Bayes advice is unique (Lemma 1.5). A boundary $p$-Bayes model can be incoherent if another $p$-Bayes model beats it at a world outside $\operatorname{supp}p$.
* **C2.** v3 lem:bayes-necessary(c) ($M\subseteq\Delta_{\operatorname{supp}p}$) does **not** transfer verbatim to decomposable domains. Its proof needs $+$ to be in the advice range at every $g$ with $g_S>0$. The correct version on decomposable domains: a $p$-Bayes model accepts a.e. $h$ with $h_S>0$ *whose acceptance is in the advice range*. Under (LF), this still forces the target's prior to be interior (Prop. 2.6).
* NAL lem:additive is a field model with *two kinds of advice per gamble* (accept it or not): $g$ and $-g$ are accepted independently, with additive costs. It covers the advice range $\{+,0\}$ only. The advice range $\{+,0,-\}$ falls outside its form, and so does the four-rank order's coupling of $g$ and $-g$. v3 thm:general is the right template.

---

## 1. Bayes structure on decomposable domains

**Lemma 1.1 ((G) on decomposable domains). PROVED.** Under the strict four-rank order, (G) holds on $\mathcal M$ iff for each $i$ and a.e. $g$ (off the coordinate hyperplanes), $a\mapsto\ell_i(g,a)$ is strictly increasing in guidance rank at world $i$ on $A(g)$.

*Proof.* If: a pointwise rank improvement lowers the integrand pointwise, and strictly on a non-null set when the improvement is strict. Only if: suppose $E$ is non-null, $a,b\in A(g)$ on $E$ (measurably chosen), $a$ is better than $b$ at $i$, and $\ell_i(g,a)\ge\ell_i(g,b)$ on $E$. Take $X,Y\in\mathcal M$ that agree off $E$ and choose $a$, respectively $b$, on $E$; both are in $\mathcal M$ because the domain is decomposable (closed under splicing). Then $X$ is a strict guidance improvement on $Y$ at $i$, but $L_i(X)\ge L_i(Y)$. A finite partition into the pairs $(a,b)$ makes the selection measurable. $\square$

Since the four ranks are distinct at every world, the restriction of $\ell_i(g,\cdot)$ to $A(g)$ is injective.

**Lemma 1.2. PROVED.** $X\in\mathcal M$ is $p$-Bayes iff $a_X(g)\in\arg\min_{a\in A(g)}p\cdot\ell(g,a)$ for a.e. $g$. A measurable pointwise minimiser exists (finitely many kinds of advice; fixed tie-break order), and it lies in $\mathcal M$.

*Proof.* As in v3 thm:general: integrate the nonnegative difference from the pointwise minimum. $\square$

**Lemma 1.3 (v3 lem:bayes-necessary on decomposable domains). PROVED.**
(a) Under (LA) and (S), a coherent $p$-Bayes model exists for every $p\in\Delta$.
(b) A model in $\mathcal M$ that is not strictly dominated within $\mathcal M$ is $p$-Bayes for some $p$.
(c) For interior $p$, every $p$-Bayes model is undominated within $\mathcal M$.

*Proof.* (a) is v3's proof verbatim. Its auxiliary model $B$ is the pointwise minimiser, which is in $\mathcal M$ by Lemma 1.2. KKM is applied to $A_i=\{q:C_q\preceq_iB\}$. (b) is v3's proof. The splices used to show that the closure of the attainable loss set is convex are measurable models whose advice lies in the advice ranges, so they lie in $\mathcal M$. Alternatively, use Lyapunov as in NAL lem:additive(c), applied to the vector measure of loss differences on the decomposable domain. (c) If $Y$ weakly dominates $X$, strictly at $j$, then $p\cdot L(Y)<p\cdot L(X)$ because $p_j>0$. $\square$

**Lemma 1.4 (interior priors). PROVED.** Assume (LA), (S), (C). For every interior $p$:
(i) every $p$-Bayes model is coherent (a.e.);
(ii) the minimiser in Lemma 1.2 is unique for a.e. $g$.

*Proof.* (i) LDG thm:kkm gives $\mathcal U_L=\mathcal C_L$ under (LA), (S), (C). By 1.3(c), a $p$-Bayes model is undominated, hence coherent.

(ii) Suppose two distinct kinds of advice $a,b$ both minimise on a non-null $E$. Distinct kinds of advice differ in the acceptance of $g$ or of $-g$. Hence there is a non-null set $Z\subseteq\mathbb R^n$ of orientations on which, as $F\subseteq Z$ varies, the models $X_F$ ("accept $h\in F$, reject $h\in Z\setminus F$, fixed minimiser elsewhere") are all $p$-Bayes. By (i) they are all a.e. cones.

A measurable set is a.e. a cone iff, for a.e. $\theta\in S^{n-1}$, its radial section is null or co-null in $(0,\infty)$. This is polar Fubini. Let $\Theta=\{\theta:Z_\theta\text{ non-null}\}$; it has positive measure. For a.e. $\theta\in\Theta$:

* $(X_\varnothing)_\theta$ misses $Z_\theta$, so it is null.
* $(X_Z)_\theta=(X_\varnothing)_\theta\cup Z_\theta$ is co-null, so $Z_\theta$ is co-null.
* Then $(X_{Z\cap\{|h|<1\}})_\theta$ agrees a.e. with $(0,1)$, which is neither null nor co-null.

This is a contradiction. $\square$

**Lemma 1.5 (vertices). PROVED.** At $e_i$ the minimiser is a.e. unique (Lemma 1.1). It is the best advice in the advice range at world $i$ (DCE prop:ideal for general rankings). Under (LA), (S) it is coherent: by 1.3(a) a coherent $e_i$-Bayes model exists, and the minimiser is unique.

---

## 2. Charts

For a pair $g$ and an orientation $h\in\{g,-g\}$, let the **chart**
$$R(h)=\{p\in\Delta:\text{accepting }h\text{ is the unique minimiser of }p\cdot\ell(g,\cdot)\text{ over }A(g)\}.$$
It is relatively open in $\Delta$, since it is defined by finitely many strict affine inequalities. Write $\ell(a)=\ell(g,a)$.

**Proposition 2.1 (table of charts for each advice range). PROVED.** For the charts, $\times$ can be ignored in any advice range that contains other advice: it has the worst rank at every world, so it is never a minimiser at any prior. A non-null set with $A(g)=\{\times\}$ (every evaluable model gives contradictory advice there) makes every evaluable model incoherent, so (LA) fails. For the remaining advice ranges $A\subseteq\{+,0,-\}$, put
$$c=\ell(0)-\ell(+),\qquad c'=\ell(0)-\ell(-),\qquad d=\ell(-)-\ell(+)=c-c'.$$
By Lemma 1.1, wherever the relevant advice is in the advice range:

* $c_i,d_i$ have the sign of $g_i$;
* $c'_i$ has the sign of $-g_i$;
* $|d_i|>|c_i|$ for $i\in N(g)$, and $|d_i|>|c'_i|$ for $i\in P(g)$.

The charts are as follows.

| advice range | $R(g)$ | $R(-g)$ |
|---|---|---|
| $\{+\}$ (every evaluable model accepts $g$) | $\Delta$ | $\varnothing$ |
| $\{0\}$ | $\varnothing$ | $\varnothing$ |
| $\{+,0\}$ | $\{c\cdot p>0\}$ | $\varnothing$ |
| $\{+,-\}$ | $\{d\cdot p>0\}$ | $\{d\cdot p<0\}$ |
| $\{+,0,-\}$ | $\{c\cdot p>0,\ d\cdot p>0\}$ | $\{c'\cdot p>0,\ d\cdot p<0\}$ |

Mirror images give $\{-\}$ and $\{0,-\}$. For the advice range $\{+,0,-\}$ the silence region is $\{c\cdot p\le0,\ c'\cdot p\le0\}$, and the three lines $\{c=0\},\{c'=0\},\{d=0\}$ are concurrent (projectively), because $d=c-c'$. The three regions are the sectors of a three-piece minimisation diagram. $R(g)$ and $R(-g)$ are adjacent across the $d$-ray. This is the "two-slope coupling".

**Vertex property.** Whenever accepting $h$ is in the advice range but not every evaluable model accepts $h$, $R(h)$ is convex, contains $\delta_i$ for every $i\in P(h)$, and contains no $\delta_j$ with $j\in N(h)$.

**Converse. PROVED.** Any measurable sign-preserving data $c$ (for $\{+,0\}$), $d$ (for $\{+,-\}$), or $(c,c')$ with these signs (for $\{+,0,-\}$) come from (G)-penalties. For $i\in P$ take $\ell_i(+)=0$, $\ell_i(0)=c_i$, $\ell_i(-)=c_i-c'_i$. For $i\in N$ take $\ell_i(-)=0$, $\ell_i(0)=c'_i$, $\ell_i(+)=c'_i-c_i$. Give $\times$ a strictly larger value, and multiply the penalty vector at $g$ by a positive weight making all of them integrable. Charts are invariant under that rescaling.

Call the region where a chart is the intersection of two genuinely different half-planes a **wedge**: advice range $\{+,0,-\}$ with the apex of the concurrent lines in $\operatorname{int}\Delta$, and both constraints active.

For a prior $p$, let $B_p=\{h:p\in R(h)\}$ (orientations), with unanimous positive gambles included. At interior $p$, $B_p$ is a.e. the unique Bayes model (Lemma 1.4(ii)).

**Theorem 2.2 (chart characterisation). PROVED** (sufficiency CHECKED).
Let $L$ be an additive ranking on a decomposable domain satisfying (G).

**(N) Necessity.** If (LA), (S), (C) hold, then:
* (N1) for every interior $p$, $\{g:p\in\partial R(g)\cup\partial R(-g)\}$ is null;
* (N2) for every interior $p$, $B_p$ agrees a.e. with a coherent $D_{K_p}$;
* (N3) at every vertex, $B_{e_i}$ is a.e. "accept $h$ iff accepting $h$ is the best advice in the advice range at world $i$", and it is coherent;
* (N4) at every boundary $p$, some coherent $p$-Bayes model exists.

**(S) Sufficiency.** If, for every $p\in\Delta$ including the boundary, the minimiser is a.e. unique and $B_p$ is a.e. coherent, then (LA), (S), (C), (G), (IB) all hold on $\mathcal M$ (v3 thm:general on decomposable domains). Every model in $\mathcal M$ outside $\{C_p\}$ is strictly dominated at every world by some $C_q$.

**(T) Targets.** Assume (N). A coherent $D$ belongs to $\mathcal C_L$ iff $D$ is $p^*$-Bayes for some $p^*$ at which (writing $\approx$ for a.e. equality) $D\approx B_{p^*}$. If $p^*$ is interior, this is automatic. See Prop. 2.6 for when interiority is forced.

*Proof.* (N1)–(N2) are Lemma 1.4, (N3) is Lemma 1.5, and (N4) is Lemma 1.3(a). For (S), v3's proof is re-read on decomposable domains:
* the unique Bayes model is undominated;
* the gap argument plus dominated convergence give continuity of $p\mapsto L_i(C_p)$, which yields closedness;
* (c) uses KKM;
* (C) uses uniqueness;
* (IB) is v3 lem:local-independence applied to models in $\mathcal M$: the common contribution cancels.

Every step only compares models in $\mathcal M$. For (T): $D\in\mathcal C_L$ means $D$ is undominated, so by 1.3(b) it is $p^*$-Bayes for some $p^*$. Conversely, an interior Bayes model is undominated (1.3(c)) and coherent. $\square$

**Remark 2.3 (boundary ties). CHECKED.** Between (N) and (S) the only gap is ties at boundary priors. One exact version reads as follows. Under (N1)–(N2), the axioms (LA), (S), (C) hold iff there are coherent, undominated models $C_p$ for $p\in\partial\Delta$, each competitive on $\operatorname{supp}p$, such that:
* $p\mapsto L_i(C_p)$ is lower semicontinuous on $\Delta$ for each $i$ (on the interior, $C_p$ is the unique Bayes model and the map is continuous);
* every $X\in\mathcal M$ whose loss profile equals that of some boundary $C_p$ is coherent.

Lower semicontinuity is equivalent to closedness of the sections, because the attainable values of $L_i$ form the interval between the values at the evaluable models with pointwise-best and pointwise-worst advice (splicing). Competitiveness depends on $p$ only through $\operatorname{supp}p$, so $C_p$ need not be $p$-Bayes.

**Proposition 2.4 (reach set). PROVED.** Assume (N). Let $W=\bigcup_{p\in\operatorname{int}\Delta}B_p$, and let $\mathrm{Av}$ be the set of orientations whose acceptance is in the advice range.
(i) $W\approx\mathrm{Av}\setminus\{h\le0\}$.
(ii) $W\cap D_i\approx B_{e_i}\cap D_i=D_{V^i}$, where $V^i=\operatorname{conv}(K_{e_i}\cup\{e_i\})\ni e_i$. So $W$ is a.e. a finite union of open convex cones $D_{V^i}$, with $D_{V^i}\cap D_j\approx D_{V^j}\cap D_i$. In particular $W$ is a.e. a cone.

*Proof.* (i) $W\subseteq\mathrm{Av}$ is trivial, and coherence of interior $B_p$ excludes negative gambles. Conversely, if $h\in\mathrm{Av}$ and $h_i>0$, then $\delta_i\in R(h)$ (vertex property, or $R(h)=\Delta$ if every evaluable model accepts $h$). $R(h)$ is relatively open, so it contains interior priors. (ii) By (i), $W\cap D_i\approx\mathrm{Av}\cap D_i$, and $B_{e_i}\cap D_i\approx\mathrm{Av}\cap D_i$ (Lemma 1.5). Also $B_{e_i}\cap D_i=D_{K_{e_i}}\cap D_{\{e_i\}}=D_{\operatorname{conv}(K_{e_i}\cup e_i)}$. Finally, $W$ minus negatives is covered by $\bigcup_i(W\cap D_i)$. $\square$

**Proposition 2.5 (a convex-cone subdomain). PROVED.** Assume (N), let $D=D_K\in\mathcal C_L$ with $K\subseteq\operatorname{int}\Delta$, assume (LF) at $D$, and let $p^*$ be interior (Prop. 2.6). Then there is a credal $K'\subseteq\operatorname{ri}K$ with $U':=D_{K'}\subseteq W$ a.e. For every interior $p$, $B_p\cap U'\approx D_{\operatorname{conv}(K_p\cup K')}$ is coherent, and the charts of $h\in U'$ are unchanged.

*Proof.* Take the open representative $W^o=\bigcup_iD_{V^i}$. Since $B_{p^*}\approx D$, we have $D\subseteq W^o$ a.e. (LF) puts acceptance of $h$ in the advice range for $h$ in an open $N\supseteq\partial D\setminus0$. By Prop. 2.4(i), $N\subseteq W^o$ a.e., so $N\subseteq\operatorname{int}\overline{W^o}$. For a finite union of open convex sets, $\overline{W^o}\setminus W^o\subseteq\bigcup\partial D_{V^i}$ is null. So $W^o\supseteq\operatorname{int}\overline{W^o}$ a.e., and the latter is an open cone containing $D\cup(\partial D\setminus0)$. By compactness on the sphere it contains $D_{K'}$ for some $K'\subseteq\operatorname{ri}K$ close to $K$. Intersections of coherent cones are coherent. $\square$

So **a non-conic or non-convex $\mathrm{Av}$ gives nothing beyond a convex cone domain** for coverage arguments: the analysis can always be run on $U'$.

**Proposition 2.6 (interior target prior). PROVED.** Under (N), if $D_K\in\mathcal C_L$ with $K\subseteq\operatorname{int}\Delta$ and (LF) holds at $D_K$, every $p^*$ at which $D_K$ is Bayes is interior.

*Proof.* Let $S=\operatorname{supp}p^*\neq\Omega$. The gamble $g(t)=\mathbf 1_S-t\mathbf 1_{S^c}$ has $P_K(g(0))>0$ and $P_K(g(t))<0$ for large $t$, because $m(S^c)>0$ on $K$. So some $g_0=g(t_0)\in\partial D\setminus0$ has $(g_0)_S>0$. Near $g_0$, (LF) puts $+$ and $0$ in the advice range. Accepting is good at every world of $S$, hence the unique minimiser at $p^*$. So the $p^*$-Bayes model accepts a.e. $h$ near $g_0$ with $h_S>0$, including a non-null set outside $\overline D$. That contradicts $D\approx$ Bayes. $\square$

**Proposition 2.7 (acceptance propagation). PROVED.** Assume (N) and that $D$ is $p^*$-Bayes, $p^*$ interior. For a.e. $h\in D$, $R(h)\supseteq\operatorname{conv}(\{p^*\}\cup\{\delta_i:i\in P(h)\})$. For a.e. $h\notin\overline D$, $R(h)\cap\operatorname{conv}(\{p^*\}\cup\{\delta_j:j\in N(h)\})=\varnothing$.

*Proof.* The first holds because $R(h)$ is convex. For the second, consider each chart type in 2.1:
* a half-plane: the complement is convex;
* a wedge $\{c>0,d>0\}$: $p^*$ fails one inequality, say $c\cdot p^*\le0$, and $c_j<0$ for $j\in N$, so the whole hull lies in $\{c\le0\}$;
* the case in which every evaluable model accepts $h$ is excluded a.e. because $D\approx B_{p^*}$. $\square$

The constant selection $K_q\equiv K$ satisfies 2.7 at every prior. So 2.7 cannot obstruct a plateau by itself. What does obstruct $K_q\equiv K$ near $\partial\Delta$ is the following.

**Proposition 2.8 (edge forcing). PROVED.** If $E\subseteq\mathrm{Av}\cap D_i\cap D_j$ is non-null, there are a non-null $E'\subseteq E$ and an open neighbourhood $O$ of the closed edge $[\delta_i,\delta_j]$ with $E'\subseteq B_q$ for every interior $q\in O$.

*Proof.* $R(h)$ is convex and contains $\delta_i,\delta_j$, so it contains the closed edge. Being open, it contains $O_m=\{\operatorname{dist}(\cdot,[\delta_i,\delta_j])<1/m\}$ for some $m=m(h)$. Take $E'=\{h\in E:m(h)\le m_0\}$ with $m_0$ large. $\square$

For T1 with (LF): $\mathrm{Av}\cap D_1\cap D_2\supseteq N\cap\{h_1,h_2>0\}\not\subseteq\overline D$. So near every edge, $B_q\not\subseteq D$, and $K_q\not\supseteq K$. Any plateau must be interior.

---

## 3. Regularity: what measurability and advice ranges add

**Proposition 3.1 (the selection is continuous). PROVED.** Under (N1)–(N2), $p\mapsto B_p$ is continuous from $\operatorname{int}\Delta$ to $L^1(\mu)$, and $p\mapsto K_p$ is Hausdorff-continuous on $\operatorname{int}\Delta$.

*Proof.* At a.e. $g$, the unique minimiser at $p$ has a positive gap, so it is eventually the minimiser at $p_k$; dominated convergence gives the $L^1$ claim. The map $K\mapsto\mathbf 1_{D_K}$, from credal sets (Hausdorff, compact) to $L^1(\mu)$, is:
* continuous: $P_{K_k}\to P_K$ uniformly on bounded sets, and $\{P_K=0\}$ is null;
* injective: two a.e.-equal open convex sets are equal (v19, line 1788), and $K=\{m\in\Delta:m\cdot h\ge0\ \forall h\in D_K\}$.

So it is a homeomorphism onto its image. $\square$

Consequently $(p,h)\mapsto P_{K_p}(h)$ is jointly continuous on $\operatorname{int}\Delta\times\mathbb R^n$. Define the **regularised chart** $\tilde R(h)=\{p\in\operatorname{int}\Delta:P_{K_p}(h)>0\}$, which is open for every $h$, and the **persistent-boundary set**
$$\mathrm{Bad}=\{h:\lambda\{p\in\operatorname{int}\Delta:P_{K_p}(h)=0\}>0\}.$$

**Theorem 3.2 (charts are continuous almost everywhere). PROVED.**
(i) $\mathrm{Bad}$ is null.
(ii) For a.e. $h$, $\tilde R(h)\approx R(h)\cap\operatorname{int}\Delta$.
(iii) For every $h_0\notin\mathrm{Bad}$ and every sequence $h_k\to h_0$, $\lambda(\tilde R(h_k)\triangle\tilde R(h_0))\to0$.
(iv) If $\tilde R(h)$ is a.e. an open half-plane $H(h)$ (all pairs with advice range $\{+,0\}$, and all half-plane charts), then $\tilde R(h)\subseteq H(h)$ and $H(h)\setminus\tilde R(h)$ is relatively closed and null. On the co-null set where this holds and $h\notin\mathrm{Bad}$, the unit normal $\hat c(h)$ is continuous at every point. That is, discontinuities of the chart lie in $\mathrm{Bad}$.

*Proof.* (i) is Fubini: each $\{h:P_{K_p}(h)=0\}$ is null. (ii) is Fubini applied to $B_p\approx D_{K_p}$. (iii) Off the null set $\{p:P_{K_p}(h_0)=0\}$, joint continuity gives pointwise convergence of indicators; dominated convergence finishes. (iv) $\tilde R(h)\setminus\overline{H}$ is open and null, hence empty; an open subset of $\overline H$ lies in $H$. Convergence in measure of half-planes whose boundary lines cross $\operatorname{int}\Delta$ (they separate vertices) gives convergence of the normals. $\square$

**Example 3.3 (genuinely discontinuous charts, $n=2$). PROVED.** Let $\varphi:[0,1]\to[0,1]$ be continuous, nondecreasing and onto, constant on each of countably many disjoint intervals whose plateau values $\{s_k\}$ are dense, and strictly increasing elsewhere (for instance, the inverse of a strictly increasing function with jumps at a dense countable set). Take v3's family $K^w_s=[l_w(s),u_w(s)]$ with $0<w<1$, and set $K_t:=K^w_{\varphi(t)}$.

At $g=(a,-b)$ with $r=b/(a+b)$, the selection accepts $g$ iff $t>\alpha(r)$ and accepts $-g$ iff $t<\beta(r)$, where
$$\alpha(r)=\tau\Big(\frac{r+w}{1+w}\Big),\qquad\beta(r)=\tau\Big(\frac r{1+w}\Big),\qquad\tau(s)=\sup\{t:\varphi(t)\le s\}.$$
Here $\tau$ is strictly increasing (since $\varphi$ is continuous) and jumps exactly at the $s_k$. Any $0<\beta<\alpha<1$ is realised by (G)-penalties: $+=(0,x)$, $0=(1,1)$, $-=(y,0)$ with $x=1/(1-\alpha)$ and $y=1/\beta$, rescaled by $(1-\alpha)\beta|g|$. Then:
* ties at each prior lie on a null set of $r$;
* thm:general applies on the all-model domain, so (LF) holds at every selected target;
* the charts $\alpha,\beta$ jump on a countable dense set of rays, so $\mathrm{Bad}\supseteq$ those rays;
* the selection has plateaus ($K_t$ constant on each $\varphi$-interval).

So coherence does not force continuous charts. Discontinuity of charts is equivalent to plateau-type persistence in $n=2$. In general, the brief's statement "the selection's profile is continuous modulo ties" is right at the level of $p\mapsto K_p$ (Prop. 3.1); it is the charts, as functions of $h$, that can jump.

**Example 3.4 (non-convex reach set, $n=2$). PROVED.** $K_t=[2t/3,\ 2t/3+1/3]$. Advice ranges at $g=(a,-b)$:
* $\{0,-\}$ if $a/b\le1/2$;
* $\{+,0\}$ if $a/b\ge2$;
* $\{+,0,-\}$ otherwise.

The thresholds are $\alpha=\tfrac32/(1+a/b)$ wherever $+$ is in the advice range and $\beta=\tfrac32/(1+a/b)-\tfrac12$ wherever $-$ is in the advice range; both are in $(0,1)$ with $\beta<\alpha$, and they are realised as above. Then:
* $W=D_{[2/3,1]}\cup D_{[0,1/3]}$ has angular range $(-63.4^\circ,153.4^\circ)$, which is more than $180^\circ$;
* $(1,-1.5),(-1.5,1)\in W$, but their midpoint is negative;
* (LF) holds at, for example, $K_{1/2}=[1/3,2/3]$.

So $W$ can be non-convex. With only one-orientation advice ranges ($\mathrm{Av}\cap-\mathrm{Av}=\varnothing$), $W$ is convex when $n=2$ (angle $\le180^\circ$); for $n\ge3$ I have not decided this (open).

**Answer to task (2).**
* *Domain shape*: no gain, by Prop. 2.5.
* *Discontinuity*: the selection $p\mapsto K_p$ is always continuous, and charts are continuous off the null set $\mathrm{Bad}$. Charts can still be genuinely discontinuous on a dense null set (Ex. 3.3).

  If the discontinuities lie in a **closed** null cone (finitely many seams, including target facets), NOGO §3's regularisation $\Psi=\operatorname{dist}(\cdot,\bar S)\,\Phi/\|\Phi\|$ turns a realisation with advice range $\{+,0\}$ into a continuous weak-sign map. That map has the same closures: they are convex, because an open set a.e. equal to an open convex $O$ off a closed null set has closure $\bar O$. So finite-seam discontinuity gains nothing over continuous CPMs.
* *Advice range $\{+,0,-\}$*: genuinely outside single-map CPMs. Charts can a priori be wedges. I do not know whether wedges with apex in $\operatorname{int}\Delta$ are compatible with (N2) for $n\ge3$ (**open**). They do occur structurally whenever the apex of the concurrent lines lies inside the simplex.

**Lemma 3.5 (no wedges near the target prior). PROVED.** Under Prop. 2.5, let $Q''$ be a convex neighbourhood of $p^*$ on which $K_q\cap K'\neq\varnothing$; it exists by Hausdorff continuity, since $K'\subseteq\operatorname{ri}K$. For a.e. $g\in U'$, $R(g)\cap Q''=\{c(g)\cdot q>0\}\cap Q''$.

*Proof.* If $K_q\cap K'\ni m$, then $h\in D_{K_q}\Rightarrow m\cdot h>0$, so $-g\notin B_q$ for $g\in U'$. Hence $Q''$ misses the $-$ sector, and therefore the apex. An open convex set missing the $-$ sector cannot contain a point of the $d$-ray in its interior, and it meets the line $\{c=0\}$ only along the $+|0$ ray. $\square$

Wedges can therefore matter only at priors away from $p^*$. Near the vertices, PB's Lemma 3.1 negative case is exactly where they matter (§4.3).

---

## 4. Test target T1: $K=(1-\varepsilon)u+\varepsilon\Delta$, $n=3$

### 4.1 Status

**Not settled.** No realisation was found, and no unconditional impossibility proof. The following is established.

### 4.2 Unconditional results

**(a)** Reductions from §§2–3. Any realisation has an interior target prior (2.6), a convex-cone subdomain $U'=D_{K'}$ with $K'\subseteq\operatorname{ri}K$ (2.5), a Hausdorff-continuous selection (3.1), charts continuous off $\mathrm{Bad}$ (3.2), and half-plane charts near $p^*$ (3.5). The selection is not $\equiv K$ near $\partial\Delta$ (2.8). PROVED.

**(b) Theorem 4.1 (NAL thm:obstruction on decomposable domains). PROVED.** Let $n\ge3$ and $0<\varepsilon<1$, and let $U\subseteq\operatorname{int}\Delta$ be open. There is no additive ranking on any decomposable domain satisfying (G) whose unique Bayes model at every $q\in U$ is $D_{K_q}$ with
$$K_q=(1-\varepsilon)\sigma(q)+\textstyle\sum_Sm_S\Delta_S,\qquad\sigma(q)=w\odot q/(w\cdot q),\ w>0.$$
This includes $\varepsilon$-contamination of $q$ or of any diagonal reindexing of it. No (LF), (S) or coverage hypothesis is needed.

*Proof.* We have $(w\cdot q)P_{K_q}(g)=q\cdot\Psi^w(g)$ with $\Psi^w=w\odot\Psi$ and $\Psi$ as in NAL thm:belief. So $\Psi^w$ has the sign pattern of $\Psi$.

By Fubini, for a.e. $g$ and a.e. $q\in U$: $q\in R(g)\iff q\cdot\Psi^w(g)>0$. NAL's bad open set $N$ satisfies:
* for $g\in N$, $b(q)=q\cdot\Psi^w(g)$ is nonconstant and vanishes inside a ball $B\subseteq U$;
* $g_i>0>\Psi_i(g)$;
* $N\subseteq D_{K_{q^+}}$, so accepting $g$ is in the advice range.

On $B$, the convex open chart $R(g)$ agrees a.e. with the half-plane $\{b>0\}$. Going through the chart types of 2.1:
* the chart $R(g)=\Delta$ (every evaluable model accepts $g$) is impossible;
* for a half-plane $\{c>0\}$ or $\{d>0\}$, the boundary lines coincide on $B$;
* for a wedge, the boundary inside $B$ is straight, so exactly one of $\{c=0\},\{d=0\}$ is the line $\{b=0\}$ there.

In every case a sign-preserving vector ($c$ or $d$) is a positive multiple of $\Psi^w(g)$, as an affine function on $\operatorname{aff}\Delta\ni e_i$. That contradicts $\Psi^w_i(g)<0<g_i$ by Lemma 1.1. $\square$

New relative to NAL: decomposable domains, the advice range $\{+,0,-\}$ and advice ranges $\{+\}$, $\{-\}$, (G) in place of truth-directedness, and the diagonal reindexing.

**(c) Plateaus are compatible with every local constraint at $p^*$.** A selection constant ($=K$) on a neighbourhood $W_0$ of $p^*$ is not excluded by NAL thm:obstruction (its proportionality step needs $q\mapsto q\cdot\Psi(g)$ nonconstant on the set of indices). It is also not excluded by Prop. 2.7.

For such a plateau, every chart line of $h$ near $\partial D$ avoids $W_0$. At every facet point, the inside cluster $c^+$ satisfies $c^+\cdot q\ge0$ on $W_0$ and the outside cluster $c^-$ satisfies $c^-\cdot q\le0$ on $W_0$. So the one-sided projective limits differ, and $\partial D\subseteq\mathrm{Bad}$. PROVED. Plateaus with $\mathrm{Bad}\supseteq\partial D$ do exist in $n=3$ *without* (LF): DCE §4's cheap system has $C_p=D_K\cap D_p$, constant on $K$. With (LF) I know of none.

### 4.3 Conditional impossibility

**Theorem 4.2. CONDITIONAL** on NOGO + PB + the fixed-anchor note. Suppose a realisation of T1 satisfies:
* (H1) there is a closed null cone $S$ such that the a.e.-defined unit chart normal $\hat c$ agrees a.e. on $U'\setminus S$ with a continuous function. Its zero-coordinate set is then relatively closed and null, so it can be added to $S$;
* (H2) for a.e. $g\in U'$, accepting $-g$ is not in the advice range (equivalently, each $V^j$ meets $K'$).

Then no such realisation exists.

*Proof.* By (H2), charts on $U'$ are single half-planes, so the realisation restricts to a map $c$ on $U'$ with $B_p\cap U'\approx\{p\cdot c>0\}$. By (H1) and NOGO §3, the regularisation $\Psi$ is continuous, positively homogeneous (take the normal of $\tilde R(h)$, which is degree-$0$ in $h$) and weak-sign, with strict signs off a closed null set. Its contraction closures are convex for all interior $q$, and $\operatorname{int}C_{p^*}\cap U'=D$. $U'$ is an open convex cone containing $\overline D\setminus0$ and the nonzero nonnegative orthant. These are NOGO §1's hypotheses, and NOGO §1–2 gives no realiser at any interior prior. $\square$

**Spot-check of the plateau case.** I re-read PB Lemma 3.1, Thm 3.2, the exterior-ratio law (4.2) and Thm 4.1. For a plateau $W_0\ni p^*$, the exterior ratio constant $d_{F,j}$ is at least the largest $s$ with $q^*+se_j\in W_0$, which is positive. PB Thm 4.1 derives a contradiction from $d>0$ using only:
* priors near $Q=q^*+de_j$;
* the strict cluster signs of Thm 3.2;
* convexity and closures.

I found no step that fails for a $\Psi$ vanishing on the facets. So plateaus are excluded under (H1)–(H2) (CHECKED as far as these steps go).

**Where (H2) is needed.** PB Lemma 3.1, negative case, infers acceptance at priors near $e_i$ from $q_s\cdot u>0$ for a cluster $u$ of $c$. With a wedge, acceptance also needs $d\cdot q_s>0$. So without (H2) the strict-sign theorem 3.2 is unproved, and Thm 4.1 with it.

(H2) fails on all-model domains, where $V^j=\{e_j\}$. **So T1 is open even for additive rankings on the all-model domain.** v3 thm:additive-obstruction needs three vertices in $K$.

**Conjecture 4.3.** (H1) can be removed by running PB's arguments on the regularised chart $\tilde R$, which is open for every $h$ and equals $H(h)$ minus a closed null set off $\mathrm{Bad}$ (Thm 3.2(iv)). Every PB contradiction of the form "an accepted point lies in the closure of a rejected open set" survives with $\tilde R$ in place of continuity of $\Phi$. Not verified.

**Precise residual for T1.** If NOGO is correct and Conjecture 4.3 holds, a T1 realisation must use wedge charts on $U'$ at priors away from $p^*$. That means advice range $\{+,0,-\}$ at pairs near $\partial D$, with $-g$ in the advice range and accepted near the vertices of $N(g)$.

### 4.4 T2 (generic interior triangle)

Everything in §§2–3, 4.2(a),(c) and Thm 4.2's reduction applies verbatim. Thm 4.1 does not apply: it is specific to contamination and belief functions. Under (H1)–(H2) the question reduces to the continuous single-map problem, for which TRIANGLE_STATUS reports only **numerical** evidence of a no-go for random triangles (its §"rigid", item on general triangles). Status: open; conditional status is "numerically negative".

---

## 5. What is new here versus the cited files

* **Theorem 2.2 / Prop. 2.1**: an exact table of charts for each advice range on decomposable domains, including the ranges $\{+\}$, $\{-\}$, $\{+,-\}$ and concurrency. Corrections C1–C2 to the brief/v3 transfer.
* **Props 2.4–2.6, 2.8**: the reach set is a finite union of vertex cones; there is a convex-cone subdomain; the target prior is interior; edge forcing.
* **Prop. 3.1, Thm 3.2**: Hausdorff continuity of the selection; a.e.-continuity of charts with discontinuities in $\mathrm{Bad}$; the regularised chart.
* **Examples 3.3, 3.4**: dense chart discontinuities; a non-convex $W$.
* **Lemma 3.5, Thm 4.1**: no wedges near $p^*$; the decomposable-domain version of NAL thm:obstruction.
* **Thm 4.2 (conditional), with (H2) identified as the precise gap**, and the observation that T1 is open even on all-model additive domains.

Not new: NOGO's continuous theorem and regularisation; NAL's bad-set construction; v3's sufficiency proof.
