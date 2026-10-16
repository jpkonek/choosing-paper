# R3 notes: non-additive (lexicographic / incomplete) coverage attempts on decomposable domains

12 Oct 2026. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof sketched),
**CONJECTURE**. Nothing here has been refereed. Scripts: `r9/r3py/geom.py` (numerical check of two
polygon containments, later proved by hand in §5.2).

## 0. Outcome in one paragraph

No covering construction for T1, T3 or T4 was found. What was found:

1. For T1 there is a complete, strictly guiding (G), (IB)-additive-componentwise **lexicographic** system on a
   decomposable domain with (LF) at the target whose **lexicographic Bayes model is coherent at every prior**, and
   the target is one of them (§5). So for lexicographic rankings the bottleneck is **not** coherence of the
   Bayes family (the CPM bottleneck for additive rankings). It is closed choice (S).
2. That system fails (S), and the failure is general. Closed sections force the primary profile along the
   selection to be a lower-semicontinuous **staircase**: countably many values, every point a local
   minimum (§3). For an *error-only* primary (the natural Σ_T-style primary: it ties good advice with
   silence and penalises only errors), this staircase is incompatible with (S) as soon as some vertex
   model pays the primary at every other world (Theorem L, §4). The proof uses only (G), (IB), (S), the decomposable
   domain, and two genericity conditions. It is target-independent.
3. Smaller general facts: the selection cannot be constant on any set whose closure contains a point
   with a different model up to ties (§2.1). Unanimity (multi-loss Pareto) rankings make competitiveness
   strictly harder (§2.4). Lexicographic coverage requires every *partial-lexicographic* undominated model
   to be coherent (§2.3). In the T1 system this already fails at an explicit model (§5.4).

## 1. Conventions

Problems g ∈ H, Gaussian μ, models modulo null sets, decomposable domain M with advice ranges A(g)
(the class of evaluable models is restricted to models whose advice on the choice represented by g lies in A(g)). A **lex ranking** at world j:

 X ⪯_j Y ⇔ F_j(X) < F_j(Y), or [F_j(X) = F_j(Y) and S_j(X) ≤ S_j(Y)],

with F_j(X) = ∫φ_j(g,a_X(g))dμ and S_j(X) = ∫ψ_j(g,a_X(g))dμ. Here φ_j, ψ_j are measurable, |φ_j|, |ψ_j| ≤ integrable
h_j, φ_j is weakly increasing along the guidance order at j (ties allowed anywhere), and ψ_j is strictly
increasing along it. Such a ranking is complete and satisfies strict (G). It also satisfies (IB) for
**every** quadruple of models: both F_j and S_j differences cancel common advice. Call F the **primary**.
F is **error-only** if φ_j(g,a) = 0 whenever a is good or silent at j (so φ_j ≥ 0 penalises only bad or
contradictory advice at j).

Standing facts used (from the brief, rechecked):
- (V) Vertex lemma (Domain Closure prop:ideal): under strict (G) at k, C_{e_k} gives, pointwise, the best advice in the advice range at k.
- (KKM) Every X ∈ M is weakly dominated at every world by some selected C_q (LDG simplex argument; CANA
  thm:closure proof). Hence every undominated X is tied at every world with a selected model (complete case).
- (Au) For finitely many additive functionals on a decomposable domain the range {(Φ_1(X),…,Φ_r(X)) : X ∈ M} is
  convex and compact (Aumann/Lyapunov: integrals of measurable selections of a measurable finite-valued
  correspondence over an atomless space). Splicing along a nested family A_t gives continuous paths in
  this range, so intermediate values are attained by splices.

## 2. General lemmas

### 2.1 Constant-level lemma (PROVED)
If C_q = C* for all q in a set Q, then for every p ∈ cl Q and every world i, C_p ⪯_i C*. If C* is
undominated, then C_p is tied with C* at every world. If moreover the ranking is complete and strictly
guiding at k, and C_p = C_{e_k} differs from C* on a non-null set where C*'s advice is not the best in the advice range at
k, this is impossible.

*Proof.* The section {q : C_q ⪯_i C*} contains Q by reflexivity and is closed, so it contains p. If C_p were
strictly better at some world, C* would be dominated. For the last clause, C_{e_k} is pointwise weakly
better at k and strictly better on a non-null set, so C_{e_k} ≺_k C* by strict (G). ∎

**Corollary 2.1a (PROVED).** Let K ∌ e_k, with (LF) at D_K and strict (G) at k. Then e_k ∉ cl{q : C_q = D_K}. In
particular the selection cannot equal the target on all of int Δ.
*Proof.* z = e_k − ℓ_k(K)𝟙 ∈ ∂D_K with z_k > 0 (v19 prop:target-two-sided). Near z, (LF) puts + in the advice range on
gambles just outside D_K with g_k > 0. There D_K is silent and + is good at k. Apply 2.1. ∎

### 2.2 Weak additive extensions transfer the Bayes condition (CHECKED; extends v3 lem:bayes-necessary)
Suppose at each world X ⪯_i Y ⇒ F_i(X) ≤ F_i(Y) for an additive F_i that is merely weakly guiding.
Then for every prior r some selected model is F-r-Bayes in M. So wherever the F-r-Bayes model is unique,
it is coherent and selected. The target, being competitive on Ω, is F-w-Bayes for some w ∈ Δ (separation
using (Au)). For lex rankings with a strictly guiding secondary, at interior r the KKM dominator is
lexicographically r-Bayes, so **every lexicographic r-Bayes model at interior r must be coherent** (when
unique). Lex rankings thus pose a non-Archimedean version of the measurable CPM problem: per-problem
charts are lexicographic half-spaces (Φ_g·r, Ψ_g·r) >_lex 0, with Φ_g only *weakly* sign-respecting.

*Vector-additive remark (PROVED under its hypothesis).* If X ⪯_i Y ⇔ L⃗_i(X) − L⃗_i(Y) ∈ P_i, with L⃗_i a finite
vector of additive losses and P_i an additive monoid (transitivity and reflexivity are equivalent to
P_i + P_i ⊆ P_i and 0 ∈ P_i), then the comparisons depend only on these difference vectors. Assume P_i ⊇ −C for a
nonempty open convex cone C in V = span of the differences (for instance, strict-improvement differences
fill such a cone). Then either all models are mutually ⪯_i-comparable both ways (which contradicts strict (G)), or some
nonzero λ ∈ C* gives a weakly guiding weak extension λ·L⃗_i that is not constant on M.
*Proof.* If cone(P_i) ≠ V, separate. If cone(P_i) = V, then some integer combination of points of P_i lies in C, so P_i
meets C at some c. For any x ∈ V and large m, mc − x ∈ C, so x = mc − (mc − x) ∈ P_i + (−C) ⊆ P_i. ∎
So vector-additive rankings always fall under 2.2 with some weakly guiding F. Lex rankings are the case
P = lex cone.

### 2.3 Partial-lexicographic undominated models must be coherent (PROVED)
Lex system, F error-only. For ∅ ≠ T ⊆ Ω, let 𝓜_T = {X ∈ M : F_j(X) = 0 ∀ j ∈ T} (a decomposable domain if 0 ∈ A(g) a.e.).
For a ∈ [0,∞)^{Ω∖T} and b ∈ Δ_T, let X be a minimiser of Σ_{j∉T} a_jF_j + Σ_{j∈T} b_jS_j over 𝓜_T that is unique
modulo null sets. Then X is undominated. Under (S) it is a selected model, hence coherent.
*Proof.* A weak dominator Y has F_j(Y) = 0 and S_j(Y) ≤ S_j(X) for j ∈ T, and F_j(Y) ≤ F_j(X) for j ∉ T. So its
objective is no larger, and uniqueness gives Y = X. By (KKM) X is tied at every world with a selected C. Ties in a lex
ranking mean equal F_j and S_j for all j, so C is also a minimiser, and C = X. ∎
(No appeal to (C) is needed.)

### 2.4 Unanimity rankings do not help competitiveness (CHECKED)
X ⪯_i Y ⇔ L^θ_i(X) ≤ L^θ_i(Y) ∀θ ∈ Θ_i (strict additive L^θ). This satisfies (G), (IB), and closed sections whenever each
q ↦ L^θ_i(C_q) is lsc. But "∀X ∃i ∀θ" implies, for every choice θ(·), "∀X ∃i" for the single-loss system.
So the selection must be competitive for every additive choice system simultaneously. Coverage by such a
system therefore yields competitiveness in each component additive system. Incompleteness of this kind
relaxes only undominatedness, not the Bayes structure.

## 3. Closed sections at primary ties: the staircase

Lex system as in §1, decomposable domain, selection with closed sections. These lemmas use only the two
properties of a primary: F_j(X) < F_j(Y) ⇒ X ≺_j Y, and X ⪯_j Y ⇒ F_j(X) ≤ F_j(Y).

**Lemma P1 (lsc; PROVED).** For every j, q ↦ F_j(C_q) is lower semicontinuous on Δ.
*Proof.* Suppose q_m → p and F_j(C_{q_m}) → f < F_j(C_p). Splice C_{q_m} (m large) into C_p along balls of
growing radius. By (Au) this yields X ∈ M with f < F_j(X) < F_j(C_p). Eventually F_j(C_{q_m}) < F_j(X), so
C_{q_m} ≺_j X and q_m lies in the section of X. That section is closed, so C_p ⪯_j X, giving
F_j(C_p) ≤ F_j(X), a contradiction. ∎

**Lemma P2 (Lagrangian condition; PROVED).** If p ∈ cl{q : F_j(C_q) < F_j(C_p)}, then either C_p is F_j-minimal or
F_j-maximal on M, or there is λ ∈ ℝ such that C_p minimises S_j + λF_j over M. Equivalently, a.e. C_p's advice
minimises ψ_j + λφ_j over A(g).
*Proof.* For X with F_j(X) = F_j(C_p), the approximating C_q satisfy C_q ≺_j X, so C_p ⪯_j X, i.e.
S_j(C_p) ≤ S_j(X). Hence (F_j(C_p), S_j(C_p)) is the lowest point of the compact convex range (Au) on its
vertical line. A supporting line there is either vertical (F_j extremal) or of finite slope −λ. ∎

**Corollary P3 (staircase; PROVED).** Let O ⊆ Δ be open, and suppose that at no q ∈ O is C_q Lagrangian at
world j in the sense of P2. Then every q ∈ O is a local minimum of F_j∘C, and F_j∘C takes only countably
many values on O. Each strict sublevel set {F_j∘C < c} ∩ O is relatively closed.
*Proof.* Local minimality is the contrapositive of P2. For each value v choose q_v with F_j(C_{q_v}) = v and a
rational ball B_v ∋ q_v inside O on which F_j∘C ≥ v. If v ≠ v' had the same ball, each value would dominate
the other. So v ↦ B_v is injective into a countable set. ∎

**Answer to the brief's lexicographic question.** Ties are harmless only where the primary profile is a
staircase. Wherever F_j∘C varies through non-minimal points, C_q must be a *single-world* Lagrangian
model (best for S_j + λF_j at world j alone). With three worlds varying simultaneously, this forces the
selection into the intersection of three one-parameter families. The design must therefore keep the
primary locally constant along the selection, letting it change only by lsc jumps. §4 shows that, for
error-only primaries, even that fails.

## 4. Theorem L: error-only primaries cannot give (S)

**Setting.** Decomposable domain M with 0 ∈ A(g) a.e. Lex rankings with error-only primary F and strictly
guiding additive secondary S (§1). Fix a world k.
- (H1) *Vertex payment.* F_j(B_k) > 0 for every j ≠ k, where B_k is the model giving, pointwise, the best advice in the advice range at k.
  This is a property of (M, F) alone: φ_j penalises, on a non-null set, acceptances in the advice range that are good at k.
- (H2) *Free trade-off.* For each j ≠ k, a non-null set of problems is F-free (φ_i(g,a) = 0 for all i and all
  a ∈ A(g)) and has best advice in the advice range at k different from that at j. A non-null set of problems also
  has in its advice range an advice that is bad at both k and j with φ_j > 0.
- (H3) *Genericity.* For every a ∈ [0,∞)^{Ω∖{k}}, a.e. problem has a unique minimiser of
  ψ_k + Σ_{j≠k} a_jφ_j over A_k(g) = {a ∈ A(g) : φ_k(g,a) = 0}.

**Theorem L (PROVED).** Under (H1)–(H3), no selection satisfies (S). This holds for any target, any (LF),
and any number of worlds n ≥ 2.

*Proof.* Suppose C satisfies (S). By (V), C_{e_k} = B_k.

(1) *The open region V.* Put V = {q : F_j(C_q) > 0 ∀ j ≠ k}. By P1 each {F_j∘C = 0} = {F_j∘C ≤ 0} is closed,
so V is open, and e_k ∈ V by (H1). For q ∈ V, F_k(C_q) = 0. Otherwise every F_i(C_q) > 0, and the model Y
obtained by replacing every F-penalised advice of C_q by silence lies in M with F_i(Y) = 0 for all i. Then
Y ≺_i C_q at every world, so C_q would be dominated.

(2) *Uniqueness given the profile.* Let q ∈ V and c_j = F_j(C_q) > 0 (j ≠ k). Let
A = {Y ∈ 𝓜_k : F_j(Y) ≤ c_j ∀ j ≠ k}, where 𝓜_k = {F_k = 0} is a decomposable domain with advice ranges A_k(g).
- C_q minimises S_k on A. If Y ∈ A had S_k(Y) < S_k(C_q), splice Y towards its F-free reduction (penalised
  advice replaced by silence) on a small set. This lowers every F_j (j ≠ k) strictly below c_j, keeps F_k = 0,
  and keeps S_k < S_k(C_q). The result strictly dominates C_q (via F at j ≠ k and via S at k).
- By (Au) and Slater (the F-free reduction has F = 0 < c), KKT gives a ≥ 0 such that C_q minimises
  S_k + a·F over 𝓜_k. All optimal points of a convex programme share the multipliers, so any two
  undominated models in V with the same profile c minimise the same objective. By (H3) they coincide.
  Thus on V the model C_q is a function of the profile (F_j(C_q))_{j≠k} alone.

(3) *Staircase on V.* For q ∈ V, C_q's advice on F-free problems is the best in the advice range at k (by (2)). If C_q
were Lagrangian at world j ≠ k, it would be best at j there, contradicting the first half of (H2). It is not
F_j-minimal (F_j(C_q) > 0). It is not F_j-maximal either: it is silent where the other advice in the advice range is bad at both k and j
(both the S_k and the F terms prefer silence), contradicting the second half of (H2). By P3, the profile
q ↦ (F_j(C_q))_{j≠k} is countable-valued on V.

(4) *Level sets are closed.* Let L_v = {q ∈ V : profile = v}, on which C ≡ C*_v by (2). If p ∈ cl L_v, then by
2.1 C_p is tied with C*_v at every world. Lex ties give equal F and S, so p ∈ V with profile v, and C_p = C*_v by (2).
Hence L_v is closed in Δ.

(5) *Sierpiński.* For any path γ : [0,1] → V, the sets γ⁻¹(L_v) are countably many, disjoint, closed,
and cover [0,1]. By Sierpiński's theorem only one is nonempty, so C is constant along γ. V is open in Δ, so
its components are path-connected. The component Q ∋ e_k lies in a single L_v, so cl Q ⊆ L_v ⊆ V. Since
cl Q is connected, cl Q = Q, so Q is open and closed in Δ, hence Q = Δ.

(6) *Contradiction.* For j ≠ k, C_{e_j} = B_j gives silence or good advice at j wherever possible (0 is
in every advice range), so F_j(C_{e_j}) = 0 and e_j ∉ V = Δ. ∎

**Remarks.** (i) The theorem covers the Σ_T-flavoured lexicographic evaluator "shun error first (at
designated worlds, on designated problems), then seek truth". (ii) It does not cover primaries that also
reward truth (φ_j(good) < φ_j(silence)). It also does not cover error-only primaries violating (H1) at
every vertex. For n = 3, failure of (H1) at every vertex means: for each k there is l(k) ≠ k such that
F_{l(k)} never penalises an acceptance in the advice range of a gamble with positive k-coordinate. Since |image(l)| ≥ 2, at least
two of the three single-negative sign patterns N_j = {h_j < 0 < h_i, i ≠ j} are then completely F-free
(CHECKED). On F-free problems the target must be S-w'-Bayes for one prior w'. This holds because modifications of D_K
confined to F-free problems leave every F_j unchanged, and competitiveness plus (Au) separation does the
rest. At every interior r the lex-r-Bayes models, coherent by 2.2, follow strict additive charts there.
So the residual case contains the measurable additive CPM problem near the middles of at least two facets
of D_K (for T1). Status of that residual: open. (iii) Replacing the secondary S by the *pointwise* order
⊴_j (incomplete) keeps (G), (IB) and closedness, but makes competitiveness fail on F-free problems: a
modification improving at every world on different parts is ⪯_i-comparable at no world. So that
variant needs F-free problems to be null, which returns F to the role of a full additive system (CHECKED, sketch).

## 5. T1: a lexicographic system whose Bayes models are all coherent

### 5.1 Data
n = 3, u = 𝟙/3, 0 < ε < 1, c = (1−ε)/3. K = (1−ε)u + εΔ = {m ∈ Δ : m_j ≥ c ∀j}, with vertices
v_j = (1−ε)u + εe_j. Fix 0 < s < 1 and K' = u + s(K − u) ⊆ relint K. Put U = D_{K'}.
- U is a coherent open cone with cl D_K∖{0} ⊆ U: for g not a multiple of 𝟙, the minimum of m·g over K is attained only on
  the relative boundary of K, so P_{K'}(g) > P_K(g).
- **U-domain:** the evaluable models are the measurable subsets X of U, so M = {X : X ⊆ U a.e.}, a decomposable domain.
  Advice ranges: on {g,−g}, + is in the advice range iff g ∈ U; − iff −g ∈ U; 0 always; × never (U never contains
  both g and −g, so no evaluable model gives contradictory advice). (LF) holds at D_K with N = U, and (G) and (IB) are not vacuous on M.
- For m ∈ Ω with {k,l} = Ω∖{m}: K''_m = K ∩ conv(K' ∪ {e_k,e_l}) and G_m = D_{K''_m}.
- Shell S = U∖D_K. For h ∈ S put J(h) = {m} if h ∈ G_m∖D_K, and J(h) = {j : h_j < 0} otherwise.

### 5.2 Geometry (PROVED)
(a) [v_k,v_l] ⊆ conv(K'∪{e_k,e_l}): v_k lies on the segment from v'_k = u + sε(e_k−u) to e_k. Hence [v_k,v_l] ⊆ K''_m.
(b) K ⊆ conv(K''_m ∪ {e_m}). The ray from e_m through x ∈ K decreases the m-coordinate and increases the
other two proportionally. Since K = {p_j ≥ c}, it leaves K where p_m = c, i.e. on [v_k,v_l] ⊆ K''_m.
(c) K ⊆ conv(K''_k ∪ K''_l) for k ≠ l: by (a) the right side contains all three vertices of K.
Consequences (all modulo the null boundary sets):
- (F1) D_K ⊆ G_m ⊆ U.
- (F2) G_m∖D_K ⊆ {h_m < 0}. If h_m ≥ 0 and h > 0 on K'', then by (b) h > 0 on K∖{e_m} = K.
- (F3) The sets G_m∖D_K are pairwise disjoint, by (c).
- (F4) U ∩ {h_k > 0, h_l > 0} ⊆ G_m, since h > 0 on K' ∪ {e_k,e_l}.
- (F5) Every h ∈ S is mixed. J(h) ⊆ {j : h_j < 0} is nonempty, and |J(h)| = 2 unless J(h) = {m} with h ∈ G_m∖D_K.
  (If h is in no G_m∖D_K, then by (F4) it has at most one positive coordinate, hence two negative ones.)
(`r3py/geom.py` also confirms (b) and (c) numerically for ε ∈ {.05,.2,.5,.9} and s ∈ {.99,.9,.5,.1}.)

### 5.3 The system and its Bayes models (PROVED)
- Secondary: S_j uses penalties 0, |g_j|, 2|g_j|, 4|g_j| (good, silence, bad, contradictory).
- Primary (error-only): F_j(X) = ∫ |h_j| dμ over the problems on which X accepts an orientation h ∈ S
  with j ∈ J(h).
- Lex rankings as in §1, complete, with strict (G) and full (IB).

Lexicographic r-Bayes model B_r (minimise r·F, then r·S). Per problem:
- For h ∈ D_K: F-free, so accept iff r·h > 0 (since E_r(+) − E_r(0) = −r·h).
- For h ∈ S: silence if J(h) ∩ supp r ≠ ∅; otherwise accept iff r·h > 0.
- Ties lie on {r·h = 0}, which is null, so B_r is unique and hence undominated.

Hence:
- r interior: B_r = D_K ∩ D_r.
- r ∈ relint Δ_{kl}: B_r = D_r ∩ G_m (with the positive orthant adjoined), by (F5).
- r = e_k: B_r = U ∩ D_k = D_{conv(K'∪{e_k})}.

**All are coherent.** D_K = B_r for every r ∈ K. So the target is undominated, (LA) holds, and
**every lexicographic Bayes model at every prior is coherent**. The NAL/CONTAMINATION-style "Bayes map must be
a CPM" obstruction therefore has no analogue here. Note the contrast with additive rankings on the same
domain: there the r-Bayes model would be U ∩ D_r ≠ D_K.

### 5.4 Failure of (S) (PROVED, two independent ways)
(i) **An incoherent undominated model.** Take T = {1} and the objective S_1 + aF_3 on 𝓜_1 = {F_1 = 0}. On facet F_3
of D_K, normalised by Σh = 1, we have h_3 = −(1−ε)/(3ε) =: −c_0 and h_1 + h_2 = 1 + c_0. The middle part
{h_1,h_2 > 0} has an outer shell inside G_3∖D_K with J = {3} (F4). The minimiser X_a accepts:
- D_K-gambles iff h_1 > 0;
- G_3-shell gambles iff h_1 > a|h_3|.

For a ∈ (0, (1+c_0)/c_0) the threshold falls inside the middle part. Near that point X_a contains inside
points on both sides of the threshold, but outside points on one side only. So its boundary contains a
2-dimensional piece of the plane h_1 + ah_3 = 0, while it has points on both sides of that plane. Hence X_a
is not convex modulo null sets (explicit midpoint witness: an outside point with h_1 + ah_3 > 0 and an
inside point with h_1 + ah_3 < 0, both close to the facet). X_a is the unique minimiser (ties null), hence
undominated by 2.3. By 2.3, (S) would make it coherent. Contradiction.

(ii) **Theorem L applies.**
- (H1): B_k = U ∩ D_k accepts G_m-shell gambles with J = {m} (from U ∩ R_{kl}) and G_l-shell gambles with J = {l}.
- (H2): D_K-problems are F-free and contain gambles with h_k > 0 > h_j for every pair. Two-negative shell gambles are bad at both
  negative worlds and penalised by φ.
- (H3): ties lie on finitely many cones.

**Diagnosis.** The Bayes family is fine. What breaks is the intermediate partial-lexicographic models,
i.e. the selection near vertices and edges. Near e_k the selection must pay F_l, F_m at least as much as
C_{e_k} (P1). Those models are forced by undominatedness to be S_k + a·F minimisers, and then by P3 to be
constant on closed level sets. Changing the primary penalty to vanish at ∂D_K (φ_j(h) = −P_K(h) in place of |h_j|) removes
the particular notch in (i). If the weights on the two other worlds are equal and every shell gamble had the
same number of penalising worlds, X_a would be {h_1 + a'·min(P_K,0) > 0}, a concave superlevel set. In general
the J-classes give different thresholds, and coherence of all partial-lexicographic models is unchecked.
This does not matter: Theorem L still applies, so the selection fails anyway.

## 6. T3 (interior segment) and T4 (conv{e_1,u})

What transfers (target-independent): §2.1, §2.3, Lemmas P1–P3, Theorem L. In particular **no error-only
lexicographic system satisfying (H1)–(H3) covers T3 or T4**.

What does not transfer: the §5 domain. For dim K < 2, both z and −z lie in ∂D_K for z ⊥ span K
(v19 prop:dimension-necessary). So (LF) needs a neighbourhood N of the line ℝz, with advice range {+,0,−,×} there.
No convex cone U ⊇ cl D_K∖{0} exists. The interior lexicographic Bayes models D_K ∩ D_r (primary
penalising every acceptance outside D_K) are still coherent. But the vertex models must give the best advice in the advice range
on a decomposable domain whose advice ranges are not conic, and the edge models must be redesigned. Not attempted to completion.
For T4 the local face lemma (Audit §2) forces the realising prior to be interior: K ⊄ any proper face.
Nothing beyond these remarks is claimed: **T3 and T4 status: open.**

## 7. Summary of claims and status

| # | Claim | Status |
|---|---|---|
| 2.1 | Constant-level lemma; selection never equals D_K near a vertex e_k ∉ K | PROVED |
| 2.2 | Weakly guiding additive weak extension ⇒ F-Bayes condition; vector-additive ⇒ such F exists (open-cone hypothesis) | CHECKED / PROVED |
| 2.3 | Lex + (S): every unique partial-lexicographic minimiser is selected, hence coherent | PROVED |
| 2.4 | Unanimity rankings make competitiveness harder | CHECKED |
| P1–P3 | Primary along a closed selection is lsc; Lagrangian at non-minimal points; staircase on open sets | PROVED |
| L | Error-only primary + (H1)–(H3) ⇒ (S) impossible (any target, any n) | PROVED |
| 5.3 | T1: lex system on the U-domain, U = D_{K'}, (LF), strict (G), full (IB), all lexicographic Bayes models coherent, target undominated | PROVED |
| 5.4 | That system fails (S) (explicit incoherent undominated model; and by L) | PROVED |
| 4(ii) | Residual for error-only primaries (n = 3): two single-negative sign patterns F-free ⇒ measurable additive CPM problem near two facet middles of D_K | CHECKED (reduction); residual open |
| — | Covering T1/T3/T4 by any non-additive system | open; no construction |

## 8. Where a construction could still live
1. Primaries that **reward truth** at some worlds (φ_j(good) < φ_j(silence) on some problems), so that (H1)–(H3) and the
   "removal lowers F" step fail. P1–P3 still impose the staircase.
2. Error-only primaries violating (H1) at every vertex (§4 remark ii). Here the open problem is the measurable
   (discontinuous) additive realisation near two facet middles. A CONTAMINATION_NOGO-style facet-flatness argument for
   measurable charts would close it.
3. Rankings with no additive weak extension at all (IRWAS-type ultrafilter orders). Closed sections look hopeless there:
   such orders are not continuous in any topology the selection can use. This is a heuristic, not a theorem.
4. Genuinely partial secondaries between "complete additive" and "pointwise ⊴" (§4 remark iii): an
   incomplete additive-unanimity secondary inside F-ties. Unexamined.
