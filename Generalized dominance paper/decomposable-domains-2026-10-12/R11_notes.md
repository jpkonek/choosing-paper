# R11. The weaker (single-target) reduction: ordinal vindication ⇒ additive vindication?

12 October 2026, round 11. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof
sketched), **CONJECTURE**. Setting as in BRIEF.md and BRIEF2.md; repairs of R6, R8, R9 are
in force (in particular "int" in nesting statements is relative to aff Δ; R7 Lemma A carries
the constant-primary hypothesis). "L vindicates T" means: L satisfies strict (G), (IB), (LA),
(S), (C) on a decomposable domain M, T = D_K ∈ C_L, and (LF) holds at T. Fact 0, Lemma 1 are R2's;
R1 Thm 2.2 is the additive chart characterisation (refereed in R6).

**Question (R11).** If some L vindicates T, does some *additive* strictly guiding L′ on some
decomposable domain M′ vindicate T (with (LF) at T)?

## 0. Summary

1. **The per-target part is vacuous (Lemma V, PROVED).** Every coherent T is already the
   unique Bayes model of some strictly guiding additive loss at an interior prior (R2 Lemma 2).
   So "extract additive criteria under which T is Bayes" proves nothing. The whole content
   of the reduction is the *global* requirement on L′: all interior Bayes models a.e. unique
   and coherent, coherent vertex models, and a boundary selection with closed sections.
   Any proof must transport a *family* from L to L′.
2. **Ordinal local face lemma (Lemma IC, PROVED, any preorders).** If L vindicates T = D_K
   with K ⊆ int Δ, then every selected model tied with T has full support, so T is
   competitive on Ω. (Ordinal form of R1 Prop 2.6 / the Audit's local face lemma.)
3. **Restriction lemma (Lemma RS, PROVED).** Restricting L to any decomposable subdomain that contains
   the range of a selection preserves all axioms. So domains can be shrunk freely as long as
   the selection and the (LF) neighbourhood stay inside.
4. **Main positive result (Theorem W, any n).** If every world of L is *countably
   sandwiched* (a countable family of strictly guiding additive losses that weakly respects
   ⪯_i and detects its strict comparisons; this includes all countable Pareto/unanimity
   rankings, R2 Prop 5's class via R8's repair, and additive rankings), then the aggregated
   additive system ψ on the **same** domain M satisfies all of R1 Thm 2.2's necessary
   conditions (N1)–(N4): unique coherent Bayes models at every interior prior (all of them in
   U_L), the world-ideal coherent models at the vertices, and a coherent Bayes model at every
   boundary prior. T is the ψ-Bayes model at an interior prior (PROVED). If in addition
   ψ has no non-null Bayes ties at non-vertex boundary priors (hypothesis (BT)), ψ vindicates
   T with (LF) at T, on M (PROVED). So for countably sandwiched systems the single-target
   reduction is reduced to **exactly the boundary-tie gap that already exists for additive
   systems** (R1 Remark 2.3).
5. **The boundary-tie gap is real for the natural selection (Lemma BT, PROVED).** If ψ has a
   non-null tie at a non-vertex boundary prior, then no selection that equals the Bayes
   model at every interior prior satisfies (S). Only a reindexed selection (which (S) allows;
   auditor's point 2) can survive. A "directional blow-up" reindexing is sketched for an
   isolated tie point (§4.3, CHECKED for one point; general case CONJECTURE).
6. **Transfer corollary (Cor T, PROVED as an implication).** Every obstruction to additive
   T1 that uses only (N1)–(N4) (R1 Thm 4.1, R4 Thms A–C, the conditional NOGO/PB/FA chain;
   all evaluate charts only at interior priors and vertices) applies verbatim to every
   countably sandwiched ordinal system. In BRIEF2's terms: a countably sandwiched system
   vindicating T delivers an additive penalty field satisfying (i), (ii), (iv) on the same
   decomposable domain; only (iii) (boundary) is not delivered.
7. **Non-Archimedean mechanism, single-target form (§5).** (a) R7 Lemma SF generalises to n
   worlds (Lemma SF_n, PROVED, via Baire): on an interior primary face, (S) forces ideal
   fibres in all worlds whose primary is non-constant on the face. (b) For finite lex with
   additive levels, every standard interior prior has a unique coherent lex-Bayes model in
   U_L (Prop LX, PROVED). (c) Its charts are "half-closed" half-spaces; a real additive field
   must reproduce them up to a reparametrisation that blows up primary-tie hyperplanes. In
   n = 2 this is R2 Thm R's countable blow-up; in n ≥ 3 it is the exact missing step
   (CONJECTURE that it can always be done). Ex 4.3's non-Bayes undominatedness is
   irrelevant at the target itself (Lemma V) and is killed by SF_n on interior faces.
8. **Uncountable sandwiches.** Theorem W's proof uses (R) only on pairs (selected C, E) with
   C ⪯_i E; a countable detecting subfamily for those pairs suffices. Without one, the
   aggregate's ties need not be L-ties: exact missing step (§3.4).
9. **n = 2**: trivial (v3). **n = 3**: Theorem W applies; (BT) concerns the three open edges;
   Cor T makes every interior/vertex additive obstruction to T1 an obstruction for all
   countably sandwiched systems. No counterexample to the reduction was found; I believe it
   true for all sandwiched and finite-lex systems (CONJECTURE), and the residual is the same
   boundary/reparametrisation issue in both classes.

## 1. What the reduction requires, and three general lemmas

**What additive vindication needs.** By R1 Thm 2.2 (N) (refereed), an additive strictly
guiding L′ on M′ vindicates T only if: (N1)–(N2) at every interior p the Bayes model B_p is
a.e. unique and coherent; (N3) at each vertex B_{e_i} is the world-i-best evaluable model and
is coherent; (N4) at each boundary p a coherent Bayes model exists; and T = B_{p*} for some
p* (interior if K ⊆ int Δ, R1 Prop 2.6). Sufficiency (R1 Thm 2.2 (S)) needs, in addition,
uniqueness at every boundary prior, or the boundary selection of R1 Remark 2.3.

**Lemma V (vacuity of per-target extraction; PROVED).** Let T = D_K be coherent and p ∈ int Δ.
There is a strictly guiding additive loss on any decomposable domain containing T for which T is the
a.e. unique p-Bayes model.
*Proof.* R2 Lemma 2 (refereed, R6). ∎
*Consequence.* Any argument of the form "from L vindicating T, find additive criteria under
which T is Bayes at an interior prior" establishes nothing beyond Lemma V. In particular
R5 Thm UN's Steps 1–2 (each pairing makes T Bayes at an interior prior), applied to a single
target, are vacuous for the reduction. The reduction is equivalent to: *some* family of
coherent models through T is the interior Bayes family of an additive field (with vertex and
boundary conditions). This is a statement about a family, which only L's selection can
supply.

**Lemma IC (ordinal local face lemma; PROVED, any preorders).** Let L vindicate T = D_K
with K ⊆ int Δ (every m ∈ K has all m_i > 0). If T is tied at every world with a selected
C_a, then supp a = Ω. Hence T is competitive on Ω: for every X ∈ M some i has T ⪯_i X.
*Proof.* T ∈ U_L, so by R2 Lemma 1 it is tied with some selected C_a, and ties transfer
competitiveness (R5 N1): T is competitive on S := supp a. Suppose S ≠ Ω. Put
g(t) = 1_S − t·1_{S^c}. Then min_K m·g(0) = min_K m(S) > 0 and min_K m·g(t) → −∞, since
m(S^c) > 0 on K. So some g_0 = g(t_0) lies in ∂T∖{0}, with (g_0)_i > 0 for i ∈ S and < 0
otherwise. Take a ball V around g_0 on which every h has h_i > 0 (i ∈ S), h_i < 0 (i ∉ S),
with V ⊆ N (the (LF) neighbourhood). Shrink V so that also −V ⊆ N whenever −g_0 ∈ ∂T. Note
−g_0 ∉ T: −g_0 ∈ T would mean max_K m·g_0 < 0, contradicting min_K m·g_0 = 0. So −V ∩ T is
null or −g_0 ∈ ∂T, after shrinking. Let V′ = V ∖ cl T. V′ is non-null, since g_0 is a
boundary point of the open convex cone T. Define X: on pairs with orientation h ∈ V′, X
accepts h and does not accept −h (advice "accept h"); elsewhere X = T. Then X △ T ⊆
V′ ∪ (−V′ ∩ T) ⊆ N, so X ∈ M by (LF). On V′ the orientation h is good at every world of S.
T's advice on these pairs is silence or acceptance of −h (bad at every i ∈ S), since h ∉ T.
So X is pointwise strictly better than T at every i ∈ S on the non-null V′, and equal
elsewhere. Strict (G) gives X ≺_i T for all i ∈ S, contradicting competitiveness on S. ∎
*Remarks.* (i) No additivity, completeness or (IB) is used. (ii) For boundary targets (T4)
the same argument shows only that supp a ⊇ every S with K ∩ Δ_{S^c} = ∅ and K ⊄ Δ_S.

**Lemma RS (restriction; PROVED).** Let L satisfy strict (G), (IB), (LA), (S), (C) on M with
selection p ↦ C_p. Let M′ ⊆ M be a decomposable domain with C_p ∈ M′ for all p. Then L restricted
to M′ satisfies the same axioms with the same selection, and C_{L|M′} = {X ∈ M′ : X tied at
every world with some C_p}. If M′ also contains every R with R △ T ⊆ N, then (LF) at T is
kept.
*Proof.* (G), (IB) are universal statements about models of the domain; restricting the
domain weakens them. (S): C_p is competitive against M ⊇ M′; sections {p : C_p ⪯_i X} for
X ∈ M′ are sections for L. C_p is undominated in M′ (fewer competitors) and coherent, so
(LA). Fact 0 (KKM) now runs on M′ and shows every undominated member of M′ is tied with some
C_p. (C): if X ∈ M′ is tied with Y ∈ C_{L|M′}, then Y is tied with some C_p, so X is tied
with C_p ∈ C_L; L's (C) makes X coherent, and X is undominated in M′ by transitivity. ∎
*Use.* The domain may be shrunk to anything containing a selection's range plus the (LF)
neighbourhood of T. It may **not** be shrunk below that: the vertex lemma (DCE prop:ideal)
forces the world-i-best member W_i(M′) to be coherent for every domain carrying an (S)
system, ordinal or additive. This constraint on domains is common to both sides of the
reduction, so it never separates them.

## 2. Is the reduction plausible? Where could ordinal freedom help?

An ordinal system can beat additive ones only by producing a selected family through T that
no additive field reproduces. Lemma V rules out any gain *at T itself*. Candidate mechanisms:

* **(M1) Non-Archimedean undominatedness (R5 Ex 4.3).** It produces undominated models with no
  supporting (even non-standard) prior. At the target this buys nothing (Lemma V: T is
  additive-Bayes anyway). In the family it is killed on interior primary faces by (S): R7
  Lemma SF for n = 2, and Lemma SF_n below for any n (§5.1). What survives is the weaker
  phenomenon (M3).
* **(M2) Ties invisible to every countable additive aggregate** (uncountable sandwiches): two
  models tied by every member of a countable aggregate but strictly ordered by the preorder.
  This is the only way an aggregate's interior Bayes set can contain incoherent splices
  (Theorem W's proof). Missing step: §3.4.
* **(M3) Half-closed charts (finite lex).** Lex-Bayes models at standard priors are unique and
  coherent (Prop LX), but their per-problem charts are half-spaces plus part of the boundary
  hyperplane. A real field reproduces the family only after a reparametrisation of Δ that
  inflates these hyperplanes (§5.3).
* **(M4) Boundary selection.** (S) needs a selection on ∂Δ with closed sections. An ordinal
  system can have one where the natural additive aggregate does not (Lemma BT). This is also
  a gap *within* additive theory (R1 Remark 2.3), not specific to ordinal systems.

(S) is what kills (M1) (via the countable-staircase lemma R2 Thm 7 / R7 Lemma 7′), and (C)
plus Fact 0 is what kills (M2) for countable families (Theorem W). None of (M2)–(M4) is known
to actually occur in an (S) system vindicating a target that no additive system vindicates.

## 3. Countably sandwiched systems: Theorem W

**Definition.** World i is *countably sandwiched* if there is a countable family
Θ_i = {θ_{i,1}, θ_{i,2}, …} of additive losses L^{θ}(X) = ∫ ℓ^θ(g, a_X(g)) dμ, each strictly
guiding at world i on the advice ranges with an integrable envelope h_{i,k}, such that
 (W) X ⪯_i Y ⇒ L^θ(X) ≤ L^θ(Y) for all θ ∈ Θ_i;
 (R) X ≺_i Y ⇒ L^θ(X) < L^θ(Y) for some θ ∈ Θ_i.
Examples: additive rankings (|Θ_i| = 1); Pareto/unanimity of countably many strictly guiding
additive losses; R2 Prop 5's countable unanimity of *weakly* guiding losses, after R8's
repair (Θ′_i = {θ + ψ_i}, ψ_i a strictly guiding countable aggregate; still countable).
Put c_k = 2^{-k}/(1 + ∫h_{i,k}) and ψ_i = Σ_k c_k L^{θ_{i,k}}. Each ψ_i is a finite,
strictly guiding additive loss (any one strictly guiding summand makes the sum strict; the
others are weakly guiding by strictness). Call ψ = (ψ_1, …, ψ_n) the *aggregate* system on M.
For p ∈ Δ, "p-Bayes" means minimising p·ψ over M; by R2 (PB) this is pointwise.

**Key step (Lemma K; PROVED).** Let p ∈ Δ and let B be p-Bayes for ψ. Then there is a
selected C (of L) that is also p-Bayes with ψ_i(C) ≤ ψ_i(B) for all i. If p ∈ int Δ, or more
generally if ψ_i(C) = ψ_i(B) for all i, then C ~_i B at every world, and B is coherent and
in C_L.
*Proof.* Fact 0(a) (valid on M under (LA), (S)) gives a selected C with C ⪯_i B for all i.
By (W), L^θ(C) ≤ L^θ(B) for all θ ∈ Θ_i, so ψ_i(C) ≤ ψ_i(B) and C is p-Bayes. If p is
interior, p·ψ(C) = p·ψ(B) with every coordinate ≤ forces ψ_i(C) = ψ_i(B) for all i.
Then, since every term c_k L^{θ_{i,k}} is ≤ and the weighted sums agree,
L^{θ}(C) = L^{θ}(B) for every θ ∈ Θ_i. If B ⪯_i C failed, then C ≺_i B (as C ⪯_i B), and (R)
gives some θ ∈ Θ_i with L^θ(C) < L^θ(B): contradiction. So C ~_i B for all i. (C) puts B in
C_L; in particular B is coherent. ∎

**Theorem W (PROVED for (a)–(d); (e) under (BT)).** Let L satisfy strict (G), (IB), (LA),
(S), (C) on a decomposable domain M, with every world countably sandwiched, and let ψ be the
aggregate. Then:
(a) for every p ∈ int Δ the ψ-p-Bayes model B_p is a.e. unique, coherent, and tied at every
    world with a selected model of L; so {B_p : p ∈ int Δ} ⊆ C_L;
(b) at each vertex, B_{e_i} is a.e. unique and equals W_i(M) = C_{e_i}, which is coherent;
(c) at every boundary p some ψ-p-Bayes model is coherent (indeed selected);
(d) if L vindicates T = D_K with K ⊆ int Δ, then T = B_{p_T} for some p_T ∈ int Δ;
    for general K, T is ψ-Bayes at some p_T ∈ Δ;
(e) if moreover (BT) holds — for every non-vertex p ∈ ∂Δ the minimiser of p·ψ(g,·) over
    A(g) is a.e. unique — then ψ (with selection p ↦ B_p) satisfies (G), (IB), (LA), (S),
    (C) on M and vindicates T, with (LF) at T on the same domain. This holds for every K.

*Proof.*
(a) By Lemma K every interior p-Bayes model is coherent and tied with a selected model.
Uniqueness: let B ≠ B′ be p-Bayes, differing on a non-null set. Both are coherent, so the
difference set Z is a cone mod null sets. The splice E = B′ on Z ∩ {|g| < 1}, B elsewhere, is
in M (decomposable domain) and is a pointwise p-minimiser, hence p-Bayes, hence coherent by Lemma K.
But E's advice changes along the radius on a positive-measure set of rays of Z, so E is not
a.e. a cone (R1 Lemma 1.4(ii), R2 Lemma U): contradiction.
(b) At e_i the objective is ψ_i, strictly guiding, so its pointwise minimiser is a.e. unique
and is the world-i-best advice in the advice range, i.e. W_i(M). Lemma K gives a selected e_i-Bayes C;
uniqueness gives C = B_{e_i}, so B_{e_i} is coherent. (By the vertex lemma C_{e_i} = W_i(M)
as well.)
(c) Lemma K.
(d) By Lemma IC, T is competitive on Ω. If some X had ψ_i(X) < ψ_i(T) for all i, then by (W)
(contrapositive) T ⪯_i X would fail at every i, contradicting competitiveness. The
attainable set {ψ(X) : X ∈ M} is convex and compact (Aumann/Lyapunov, R2 §1), so separation
gives p_T ∈ Δ with T p_T-Bayes. If S = supp p_T ≠ Ω, the model X built in the proof of Lemma
IC is pointwise strictly better than T at every world of S on a non-null set and equal
elsewhere; strict guidance of ψ_i gives ψ_i(X) < ψ_i(T) for i ∈ S, so p_T·ψ(X) < p_T·ψ(T):
contradiction. Hence p_T is interior and T = B_{p_T} by (a). For general K, T is competitive
on supp a (R5 N1), and the same separation in ℝ^{supp a} gives a prior supported in supp a.
(e) Under (BT) the minimiser is a.e. unique at every p ∈ Δ (interior by (a), vertices by
(b), the rest by (BT)), and it is coherent at every p (Lemma K: the selected p-Bayes C equals
the unique minimiser). This is the hypothesis of R1 Thm 2.2 (S) (= v3 thm:general on decomposable
domains; refereed in R6), which yields (G), (IB), (LA), (S), (C) for ψ on M with
U_ψ = {B_p : p ∈ Δ}. T is p_T-Bayes and the minimiser at p_T is unique, so T = B_{p_T} ∈ C_ψ.
(LF) at T is a property of the domain M, which is unchanged. ∎

**Corollary W1 (PROVED).** Under the hypotheses of Theorem W, U_ψ-interior ⊆ U_L: the interior
Bayes family of the aggregate is a sub-family of L's undominated set, it is Hausdorff
continuous on int Δ (R1 Prop 3.1), and its charts are continuous off a null set (R1 Thm 3.2).
Every member of U_L that is competitive on Ω and supported (in the sense of (d)) by an interior
prior is in it.

**Corollary T (transfer of additive obstructions; PROVED as an implication).** Let 𝒪 be any
theorem of the form "no strictly guiding additive penalty field on a decomposable domain with
(LF) at T has a.e.-unique coherent Bayes models at all interior priors, coherent world-ideal
models at the vertices, coherent Bayes models at boundary priors, and T among its interior
Bayes models" (possibly with extra hypotheses on the domain or penalties, such as R4's (H0),
(H1)). Then, under 𝒪's extra hypotheses applied to ψ, no countably sandwiched system
vindicates T. *Proof.* Theorem W (a)–(d) supplies such a field (ψ, on the same domain). ∎
Instances: R1 Thm 4.1 (no (S) used at all), R4 Thms A–C and the conditional chain Cor B2/C3
(R8 confirms the NOGO/PB/FA arguments evaluate maps only at interior priors). In BRIEF2's
terms, Theorem W delivers (i), (ii), (iv) of the single-target additive problem on the same
decomposable domain; only (iii) (the boundary) is not delivered. **So for countably sandwiched
rankings, the single-target additive problem for T1 is the whole problem: if additive T1 is
impossible for a reason not involving the boundary, ordinal (countably sandwiched) T1 is
impossible too.**

### 3.4 Uncountable families: the exact missing step
The proof of Lemma K uses (R) only for pairs (C, B) with C selected, C ⪯_i B, and B
ψ-Bayes. So Theorem W holds whenever each world has a countable subfamily Θ′_i ⊆ Θ_i,
containing a strictly guiding member, with
 (R_c) C ∈ C_L, X ∈ M, C ≺_i X ⇒ L^θ(C) < L^θ(X) for some θ ∈ Θ′_i.
(W) is inherited by subfamilies. **Missing step:** for a general sandwiched world (R5's
definition, arbitrary cardinality), find a countable Θ′_i satisfying (R_c). Without it, the
aggregate of any countable subfamily can tie an incoherent splice E with a selected C while
⪯_i separates them via an unused θ; then E is a ψ-Bayes model outside U_L and (a) fails.
This is mechanism (M2). R5 Thm UN avoided aggregation by working pairing by pairing, which is
enough for no-nesting (a pairwise statement) but not for producing *one* additive field whose
whole interior family is coherent: for a single pairing θ, interior θ-Bayes sets can be
non-singletons (Lemma K gives only θ-ties with selected models), and the argument of (a)
breaks exactly there.

## 4. The boundary: what (BT) costs

### 4.1 Lemma BT (natural selection fails at a non-null boundary tie; PROVED)
Let ψ be any strictly guiding additive system on a decomposable domain M whose interior Bayes models
are a.e. unique (e.g. the aggregate of Theorem W). Let p ∈ ∂Δ be a non-vertex prior,
S = supp p (|S| ≥ 2), and suppose G = {g : the p-minimiser over A(g) is not unique} is
non-null. Then no selection C′ with C′_q = B_q for every q ∈ int Δ satisfies (S).
*Proof.* Off G the p-minimiser is unique; on G pick measurably two tied kinds of advice a ≠ b
(finite partition), and put w(g) = ψ(g,a) − ψ(g,b), so p·w = 0 on G. Strict guidance makes
every w_i ≠ 0 on mixed g (a, b have different ranks at every world), and p·w = 0 with
p_S > 0 forces w to take both signs on S. (Unanimous g have a unique best advice, so G is
a.e. mixed.) For j ∈ S let X_j be the model equal to the p-minimiser off G and, on G, the
world-j-best advice among the p-minimisers at g (a.e. unique by strict guidance). For
q_s = p + s(e_j − p): q_s·ψ(g,·) = (1−s) p·ψ(g,·) + s ψ_j(g,·), so for a.e. g and all small s
(gap argument) B_{q_s} picks, on G, the world-j-best p-minimiser, and off G the unique
p-minimiser. By dominated convergence ψ(B_{q_s}) → ψ(X_j) as s ↓ 0.
Closed sections force lower semicontinuity: the attainable values of ψ_j form an interval
(splicing), so {q : ψ_j(C′_q) ≤ c} closed for every attainable c gives
ψ_j(C′_p) ≤ liminf_s ψ_j(B_{q_s}) = ψ_j(X_j) (if ψ_j(X_j) is the maximum attainable value
the inequality is trivial). Hence p·ψ(C′_p) ≤ Σ_{j∈S} p_j ψ_j(X_j). All X_j agree off G, and
pointwise on G, Σ_{j∈S} p_j ψ_j(g, x_j(g)) ≤ Σ_{j∈S} p_j ψ_j(g, a) = min p·ψ(g,·) termwise
(x_j is world-j-best among minimisers, a is one of them), with strict inequality at every g ∈ G
because some j ∈ S has w_j > 0 there (b strictly better than a at j). So p·ψ(C′_p) < min_M p·ψ: impossible. ∎
*Reading.* Any additive vindication with a non-null boundary tie must use a *reindexed*
selection near that boundary point (allowed by (S): the auditor's C_t = B_{t²}). Lemma BT is
the precise form of R1 C1/Remark 2.3's gap, and it applies equally to additive L.

### 4.2 Does an ordinal L help at the boundary?
L's own selection is ψ-competitive on supp p (if X had ψ_i(X) < ψ_i(C_p) for all i ∈ supp p,
then C_p ⪯_i X fails at every i ∈ supp p by (W)). But neither ψ-undominatedness of C_p nor
closedness of the ψ-sections {q : ψ_i(C_q) ≤ ψ_i(X)} follows from L's (S): L's sections are
{q : C_q ⪯_i X}, and (W) only gives one inclusion. So L's boundary selection cannot simply be
reused. This is the exact point where Theorem W stops.

### 4.3 Directional blow-up of an isolated tie point (CHECKED for one point, n = 3)
Suppose n = 3, the only non-null boundary tie is at one point p on the edge [e_1, e_2], and
the tie set G involves two kinds of advice. For a direction v in the closed tangent cone of Δ at p
(an arc from v_1 = e_1 − p through e_3 − p to v_2 = e_2 − p), let X_v = p-minimiser off G and
the v·ψ-minimiser of {a, b} on G. Then: X_v = lim_{s↓0} B_{p+sv} (on G exactly, since
(p+sv)·w = s·v·w), hence X_v is coherent (Hausdorff limit of D_{K_q}, R1 Prop 3.1); X_v is
p-Bayes, hence ψ-competitive on S = {1,2}; X_{v_j} = X_j picks the world-j-better advice on
G, and is ψ-undominated (a weak dominator is p-Bayes, agrees off G, and on G cannot have
ψ_j ≤ without picking the same advice); X_v with v_3 > 0 is ψ-undominated (a weak dominator Y
strictly better only at world 3 would give, spliced with B_{p+sv} off G, a model with
(p+sv)-value smaller by s·v_3·(ψ_3(X_v) − ψ_3(Y)) > 0, contradicting Bayes optimality of
B_{p+sv}). If for each v the set {g ∈ G : v·w(g) = 0} is null, v ↦ X_v is continuous in
measure. Reparametrise: replace p on the edge by a short sub-segment of the edge carrying the
arc v_1 → v_2, and push the interior near p accordingly (polar coordinates around p). The
selection is then continuous at the inserted segment from both sides, and l.s.c. of the
profiles holds. I have checked this for one isolated point; it is the n = 3 analogue of the
interval insertion in R2 Thm R Step 2–4.
**CONJECTURE (boundary blow-up).** For the aggregate ψ of Theorem W (or any additive field
satisfying (N1)–(N4)), a face-preserving reindexing of Δ exists that yields a selection
satisfying (S). If true, Theorem W holds without (BT). For a continuum of tie points along an
edge (a 2-parameter family (p, v) to be packed into a 1-dimensional edge) the construction
above does not apply as it stands; this is the hardest case and I have not resolved it.

## 5. Lexicographic systems in n worlds: what (S) kills and what survives

Class 𝓛₂ⁿ: world i ranks by lex(P_i, S_i) with additive levels, P_i weakly guiding, the
composite strictly guiding (R7 §1, any n). For t ∈ int Δ, 𝔅_t = pointwise minimisers of
t·φ, F_t = π(𝔅_t) ⊆ ℝ^n (π = primary vector), fibre Φ(x) = {X ∈ 𝔅_t : π(X) = x}.
R7 Lemma F(i) holds verbatim for t ∈ int Δ (all t_i > 0): a weak dominator of X ∈ 𝔅_t lies
in 𝔅_t with the same π. Let I_v(t) = {i : x ↦ x_i is non-constant on F_t}.

**Lemma SF_n (PROVED, any n).** Under (LA), (S) and class 𝓛₂ⁿ, for every t ∈ int Δ and every
x ∈ relint F_t there is an undominated X ∈ Φ(x) with S_i(X) = g_i(x) := min_{Φ(x)} S_i for
every i ∈ I_v(t). If I_v(t) = Ω, every member of U_L in Φ(x) attains all n minima and is a
multi-Lagrangian: it minimises S_i − λ_i·P over 𝔅_t for each i, for suitable λ_i.
*Proof.* 𝒦 = {(π, S)(X) : X ∈ 𝔅_t} is convex and compact (Aumann). Each g_i is convex and
finite on F_t, hence continuous on relint F_t. The set of x ∈ relint F_t admitting a fibre
member with S_{I_v} = g_{I_v}(x) is the preimage of the closed projection of 𝒦 under the
continuous map x ↦ (x, g_{I_v}(x)); so its complement N is relatively open. For x ∈ N let Z
be the lexicographic minimiser over Φ(x) of the secondaries, I_v first, then the rest (exists
by compactness). Z is undominated: a weak dominator lies in Φ(x) (Lemma F(i)) and is
lexicographically ≤, hence equal in every S_i. Since x ∈ N, some i ∈ I_v has S_i(Z) > g_i(x);
a fibre member attaining g_i(x) has the same P_i, so Z is improvable at world i, and
x_i ∈ C_i := {P_i(X) : X ∈ U_L improvable at i}, countable by R2 Thm 7 (U_L form; R6: (C) not
needed; it holds for any n). So N ⊆ ⋃_{i∈I_v} {x : x_i ∈ C_i}. For i ∈ I_v each level set
{x_i = c} ∩ relint F_t is relatively closed and nowhere dense (x_i is a non-constant affine
function on aff F_t). relint F_t is a Baire space and N is open in it, so N = ∅.
If I_v = Ω and X ∈ U_L ∩ Φ(x), then X is Pareto in its fibre (R7 (F*), same proof); an ideal
point exists, so X attains every g_i(x). A finite subgradient of g_i at the relative interior
point x gives λ_i with S_i(Y) − λ_i·π(Y) ≥ S_i(X) − λ_i·x for all Y ∈ 𝔅_t (as R7 SF-L). ∎
*Reading.* R5 Ex 4.3's configuration (every fibre non-ideal) cannot occur on any interior
face with I_v = Ω, in any number of worlds. When some primaries are constant on a face
(I_v ≠ Ω, possible only for n ≥ 3), the worlds in Ω∖I_v keep the Ex 4.3 freedom on that face;
but on such a face those worlds' primaries are constant, so their secondaries act there as
additive strictly guiding losses. A full n ≥ 3 analogue of R7 Theorem 1′₂ would have to
handle these mixed faces; not attempted.

**Proposition LX (lex-Bayes families are coherent; PROVED, any n, any finite number of
additive levels).** Let world i rank by lex(L^1_i, …, L^m_i), additive levels, composite
strictly guiding, and assume (LA), (S), (C). For p ∈ int Δ (real), let B_p be a pointwise
lexicographic minimiser of (p·φ^1(g,·), …, p·φ^m(g,·)) over A(g). Then B_p is a.e. unique,
coherent, and tied at every world with a selected model, so B_p ∈ C_L. The same holds for
any F-prior with all coordinates > 0 in F ⊇ ℝ(ε).
*Proof.* Λ_i = Σ_k ε^{k−1} L^k_i ∈ ℝ(ε) represents ⪯_i exactly (R5 §4), and B_p minimises
p·Λ over M (R5 Lemma 4.1). Fact 0(a) gives a selected C with C ⪯_i B_p, so Λ_i(C) ≤ Λ_i(B_p)
for all i; minimality and p_i > 0 force Λ_i(C) = Λ_i(B_p), i.e. lexicographic ties at every
world; (C) makes B_p coherent. Uniqueness: two distinct minimisers are coherent; their radial
splice is again a minimiser, hence coherent, but it is not a cone (as in Thm W (a)). ∎
This is the lexicographic analogue of Theorem W (a): (M1) does not prevent a coherent interior
family. Vertices: B_{e_i} = W_i(M) as before.

**The residual (M3): half-closed charts (CHECKED as stated; reproduction CONJECTURE).**
For a problem g with advice range {+, 0}, put Δ^k(g) = φ^k(g,0) − φ^k(g,+) ∈ ℝ^n. B_p accepts g iff
(p·Δ^1, p·Δ^2, …) >_lex 0. When Δ^1(g) ≠ 0, the chart is the open half-space
{p·Δ^1(g) > 0} together with a subset of its boundary hyperplane H_g. A real strictly guiding
field with the same interior Bayes models must have open half-space charts (R1 Prop 2.1).
By Fubini, Z(p) = {g : p ∈ H_g} is null for a.e. p, but it can be non-null on a λ-null set
P* of priors (a pencil of hyperplanes H_g through a common point or line for a non-null set of
g). At p ∈ P* the lex family "jumps" in a way no real field reproduces at the same index:
- n = 2: P* is countable and R2 Thm R inserts intervals of limit models (which are in U_L by
  (S)); the family becomes a continuous monotone path and is additive. So for n = 2 the lex
  family is additively reproducible (PROVED there, R2 Thm R + R7).
- n ≥ 3: P* can contain lines in int Δ; a real reproduction requires a reparametrisation of Δ
  that blows each such line up into a strip, compatibly with the closed sections. This is the
  same operation as §4.3, now in the interior. **Missing step; CONJECTURE that it is always
  possible.**
Also missing for lex systems: that the target T itself lies in the lex-Bayes family (or its
blow-up). Lemma SF_n shows that, if T sits at a relatively interior primary level of an
interior face with I_v = Ω, T minimises t·S + μ·P over 𝔅_t (μ = −Σ t_i λ_i); i.e. T solves the
first two levels of an F-prior t + εu. The third level is not controlled, so "T is F-Bayes"
remains CONJECTURE (Ex 4.3 shows it can fail for undominated models in general, though not
for an interior-face configuration that survives SF_n).

## 6. n = 2 and n = 3

**n = 2.** Every coherent target is vindicated by an additive system on the all-model domain
(v3 thm:general), which has (LF) everywhere. So the reduction holds trivially, independently of
L. (R2 Thm R, R5 UN2 and R7 1′₂ give more: the same *family* on the same domain, for the
classes covered.)

**n = 3.** What is now known about the single-target reduction:
- Countably sandwiched L (including countable Pareto rankings and additive L): Theorem W gives
  an additive field on the same domain with (N1)–(N4) and T among its interior Bayes models.
  Non-vertex boundary priors are the three open edges; (BT) asks that ψ have no non-null Bayes
  tie at any edge prior. Under (BT) the reduction holds (PROVED). Without it, Lemma BT shows a
  reindexing near the tied edge points is unavoidable; for isolated tie points it exists (§4.3),
  in general CONJECTURE.
- For T1 specifically (K = (1−ε)u + εΔ): Cor T. Any obstruction to additive T1 using only
  interior and vertex data (R1 Thm 4.1 for prescribed families; R4 Thms A–C; the conditional
  R4 Cor B2/C3 chain with its (H0), (H1)) is an obstruction for countably sandwiched ordinal
  systems too. Conversely an ordinal countably sandwiched vindication of T1 would hand us an
  additive field solving BRIEF2 (i), (ii), (iv): so **ordinal T1 for this class is at least as
  hard as additive T1 minus the boundary condition**.
- Two-level lex in three worlds: Lemma SF_n and Prop LX hold; T's membership in the lex family
  and the interior blow-up (§5) are open.
- General (IB) preorders (IRWAS/KPS type): nothing beyond Lemmas V, IC, RS.

## 7. Answers to the R11 brief, item by item

1. *Plausibility.* The only route by which an ordinal system could vindicate a target no
   additive system can is through the family, never at T (Lemma V). Ex 4.3's mechanism is
   killed by (S) on interior faces in any n when all primaries vary (SF_n). For countably
   sandwiched systems (S)+(C) kill the remaining interior freedom (Theorem W (a)). What is left
   is reindexing (boundary ties, Lemma BT; interior primary-tie hyperplanes for lex, §5) and
   uncountable/non-representable preorders. I found no counterexample and expect none for
   sandwiched or finite-lex systems (CONJECTURE).
2. *Proof for known-rigid classes, one target, any n.* Done for countably sandwiched systems
   modulo (BT) (Theorem W). The construction is *not* "one criterion per world from a pairing"
   (that is vacuous at the target and can have incoherent interior ties); it is the countable
   aggregate, whose interior Bayes models are forced coherent and unique by Fact 0(a) + (W) +
   (R) + (C) (Lemma K). The domain need not shrink: the additive system lives on L's own decomposable
   domain, so (LF) is inherited.
3. *Exact missing steps.* (i) (BT), or a face-preserving reindexing at boundary tie points
   (Lemma BT shows the identity indexing fails); (ii) a countable subfamily with (R_c) for
   uncountable sandwiches (§3.4); (iii) for lex systems: T in the lex family, and an interior
   blow-up of primary-tie hyperplanes (§5).
4. *n = 2 trivial; n = 3 as in §6.*

## 8. Status

| Claim | Status |
|---|---|
| Lemma V: per-target extraction is vacuous | PROVED (R2 Lemma 2) |
| Lemma IC: ordinal local face lemma (K ⊆ int Δ ⇒ T competitive on Ω) | PROVED |
| Lemma RS: restriction to subdomains containing a selection | PROVED |
| Lemma K: aggregate-Bayes models are L-tied with selected models | PROVED |
| Theorem W (a)–(d): countably sandwiched ⇒ additive field with (N1)–(N4), T interior Bayes | PROVED |
| Theorem W (e): under (BT), additive vindication of T on the same domain with (LF) | PROVED (via R1 Thm 2.2(S), refereed) |
| Cor W1, Cor T (transfer of interior/vertex additive obstructions) | PROVED |
| Lemma BT: non-null boundary tie ⇒ identity-indexed selection fails (S) | PROVED |
| §4.3 blow-up of one isolated boundary tie point (n = 3) | CHECKED (sketch) |
| Boundary blow-up in general (Theorem W without (BT)) | CONJECTURE |
| Uncountable sandwiches: countable (R_c) subfamily | OPEN (exact missing step) |
| Lemma SF_n (interior faces, Baire) | PROVED |
| Prop LX (lex-Bayes interior family unique, coherent, in U_L) | PROVED |
| Lex: T in the lex family; interior hyperplane blow-up for n ≥ 3 | CONJECTURE |
| Weak reduction for all (IB) systems | CONJECTURE (no counterexample found) |
