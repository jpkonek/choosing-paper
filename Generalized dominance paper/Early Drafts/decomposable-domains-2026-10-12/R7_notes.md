# R7. Conjecture 1 in two worlds: two-level lexicographic systems

12 October 2026, round 9. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof
sketched), **CONJECTURE**. Setting, notation and standing results are those of BRIEF.md,
R2_notes.md, R3_notes.md and R5_notes.md, with R6's repairs. n = 2 throughout. A mixed problem
g (g_1 > 0 > g_2) has r = −g_2/(g_1 − g_2) ∈ (0,1). A coherent D_{[α,β]} gives + if r < α,
0 if α < r < β, and − if r > β. A pair A = D_{[α_A,β_A]}, B = D_{[α_B,β_B]} is **strictly
nested** if α_B < α_A ≤ β_A < β_B. Equivalently, K_A ⊂ int K_B with the interior taken relative
to aff Δ (R6's repair of R2 Thm N). Then R1 = {α_B < r < α_A} (A: +, B: 0) and
R2 = {β_A < r < β_B} (A: −, B: 0) are non-null cones.

## 0. Outcome

**(B) succeeded for two-level lexicographic systems. (A) failed, and the failure has an exact
reason.**

1. **Theorem 1′₂ (PROVED).** Take n = 2 and any decomposable domain. Let each world rank
   lexicographically by two additive levels (P_i, S_i), with P_i weakly guiding and (P_i, S_i)
   strictly guiding (§1; S_i is otherwise unrestricted, in particular not required to be guiding
   where P_i is strict). Assume (LA), (S), (C). Then U_L contains no strictly nested pair.
   With R2 Theorem R, U_L is then the undominated set of an additive strictly guiding
   (LA),(S),(C) system on the same domain, namely a continuous monotone path.
   This settles Conjecture 1′ for two levels. It contains the additive case (R2 Thm N) and
   R2 Theorem 6 (one world additive) as special cases, and it covers R5 Example 4.3's class
   (two lexicographic worlds) completely.
2. The new ingredient is **Lemma SF (staircase forces ideal fibres; PROVED)**. Take any
   interior primary support t ∈ (0,1) and let 𝔅_t be its face. Then on every *interior*
   primary level of 𝔅_t, the two secondaries are minimised **simultaneously** by one model.
   The reason: the set of non-ideal levels is relatively open, and by (S) (R2 Thm 7) it is
   countable, so it is empty. This is where (S) enters. R5 Example 4.3 is exactly a face
   whose fibres are non-ideal at *every* level, so it can never be completed to an (S) system.
3. **Why the suggested construction fails (§5).** The countable staircase that (S) allows
   lives only at *vertices* of the primary range and at *endpoints* of primary edges. There
   the relevant subdomain is a decomposable domain on which both primaries are constant, so the
   secondaries form an additive system, and R2 Thm N forbids nesting. Along the interior of an
   edge, every undominated model is a two-sided Lagrangian (an ideal point), and two
   Lagrangian models cannot be strictly nested. For two levels nothing is left over.
4. **Three or more levels: CONJECTURE (open).** Two pieces carry over. The depth-k version of
   R2 Thm 7 is PROVED (Lemma 7′). The common-interior-support branch of the proof iterates
   (sketch, §6). The branches with deeper blind regions (cases (b) and (c) at depth ≥ 2) are
   not done. A counterexample to Conjecture 1 must now use either at least three lexicographic
   levels or an order that is neither sandwiched nor lexicographic with additive levels
   (IRWAS/KPS type).

## 1. The class 𝓛₂ and standing facts

**Class 𝓛₂.** We are given a decomposable domain M with advice ranges A(g). At world i,
 X ⪯_i Y ⇔ P_i(X) < P_i(Y), or [P_i(X) = P_i(Y) and S_i(X) ≤ S_i(Y)],
where P_i(X) = ∫ φ_i(g, a_X(g)) dμ and S_i(X) = ∫ ψ_i(g, a_X(g)) dμ. Here φ_i and ψ_i are
measurable with an integrable envelope on the advice ranges. For a.e. g and all a, b ∈ A(g) with
rank_i(a) < rank_i(b), we require φ_i(g,a) ≤ φ_i(g,b) (weak guidance of the primary), and that
(φ_i, ψ_i)(g,a) <_lex (φ_i, ψ_i)(g,b) (strict guidance of the composite). Consequences:
- Wherever φ_i ties two kinds of advice, ψ_i strictly prefers the world-i-better one.
- Where φ_i is strict, ψ_i is unrestricted.
- Each ⪯_i is a complete preorder satisfying strict (G) and (IB) for all quadruples (both
  levels are integrals).
- Additive worlds are the case φ_i ≡ 0.
On mixed problems the two worlds rank +, 0, − in opposite orders, and × is worst at both.

**Standing facts used.**
- (L1) R2 Lemma 1: under (LA), (S), (C), U_L = C_L ⊆ coherent.
- (Au) Aumann/Lyapunov: for finitely many additive functionals on a decomposable domain, the range is
  convex and compact.
- (PB) Pointwise Bayes: X minimises a real additive functional over a decomposable domain iff its
  advice is a.e. a pointwise minimiser.
- (Sp) R5 Thm UN Step 5: a splice "A on R1 ∩ {|g|<1}, B elsewhere" is incoherent.
- (T7) R2 Theorem 7, U_L form (R6: (C) not needed): the set
  {P_i(X) : X ∈ U_L, X improvable at i} is countable. Here "improvable at i" means some
  Z ∈ M has P_i(Z) = P_i(X) and S_i(Z) < S_i(X).

**Primary supports.** 𝒫 = {(P_1, P_2)(X) : X ∈ M} ⊂ ℝ² is convex and compact (Au). If X ∈ U_L,
then no Y has P_1(Y) < P_1(X) and P_2(Y) < P_2(X) (such a Y dominates X). So π(X) = (P_1,P_2)(X)
is weakly Pareto-minimal, and the set
 T_X = {t ∈ [0,1] : t P_1(X) + (1−t) P_2(X) = min_𝒫 (t P_1 + (1−t) P_2)}
is a nonempty closed interval: the normal cone of 𝒫 at π(X), intersected with Δ. For t ∈ [0,1]
let 𝔅_t be the decomposable domain of pointwise minimisers of t φ_1 + (1−t) φ_2. By (PB), X ∈ 𝔅_t ⇔
t ∈ T_X. The t-face of 𝒫 is F_t = π(𝔅_t).

**Lemma F (faces are closed under domination; PROVED).**
(i) Let t ∈ (0,1), X ∈ 𝔅_t, and let Y weakly dominate X (Y ⪯_i X for both i). Then Y ∈ 𝔅_t
and π(Y) = π(X).
(ii) Let X ∈ 𝔅_1 and let Y weakly dominate X. Then Y ∈ 𝔅_1. Symmetrically for 𝔅_0.
*Proof.* (i) Y ⪯_i X gives P_i(Y) ≤ P_i(X) for both i. So tP_1(Y) + (1−t)P_2(Y) is at most the
minimum, hence equal to it, and both inequalities are equalities because t, 1−t > 0.
(ii) P_1(Y) ≤ P_1(X) = min P_1. ∎

So for t ∈ (0,1), undominatedness of a member of 𝔅_t is decided inside 𝔅_t, among models with
the same primaries. On 𝔅_t we have P_2 = c_t − κ_t P_1 with κ_t = t/(1−t) > 0. Write J_t for the
range of P_1 on 𝔅_t (a compact interval) and F_t(x) = {X ∈ 𝔅_t : P_1(X) = x} for the
**fibre** at level x. By Lemma F(i):

 (F*) X ∈ 𝔅_t is undominated ⇔ (S_1, S_2)(X) is Pareto-minimal in (S_1, S_2)(F_t(P_1(X))).

**Endpoint fibres are additive.** Put 𝔅_t^− = F_t(min J_t) and 𝔅_t^+ = F_t(max J_t). These are
decomposable domains: the pointwise φ_1-minimisers (respectively maximisers) within the advice ranges of 𝔅_t. On their
advice ranges φ_1 and φ_2 are constant a.e. (P_1 is constant on 𝔅_t^±, and the t-primary is constant
on 𝔅_t). So ψ_1 and ψ_2 are strictly guiding there, and (S_1, S_2) is an additive strictly
guiding two-world system on 𝔅_t^±. If J_t is a single point, then 𝔅_t itself is such a
domain.

**Lemma A (additive faces carry no nested pair; PROVED).** Let 𝔇 be a decomposable domain on which
(S_1, S_2) is strictly guiding additive. Suppose every weak dominator of a member of 𝔇 lies in
𝔇 and has the same primaries. Then 𝔇 ∩ U_L contains no strictly nested pair.
*Proof.* By (F*)-type reasoning, A, B ∈ 𝔇 ∩ U_L are (S_1,S_2)-Pareto in 𝔇. By (Au) and
separation they are Bayes at s_A and s_B ∈ [0,1], and by (PB) pointwise. Both A's and B's
advice lies in the advice ranges of 𝔇 on R. On R1, c = (ψ_1(0) − ψ_1(+), ψ_2(0) − ψ_2(+)) has signs (+, −).
On R2, c' = (ψ_1(0) − ψ_1(−), ψ_2(0) − ψ_2(−)) has signs (−, +). A's advice gives
s_A c_1 + (1−s_A) c_2 ≥ 0 on R1 and s_A c'_1 + (1−s_A) c'_2 ≥ 0 on R2. B's give ≤ 0 on both.
- On R1: (1−s_B)/s_B ≥ c_1/|c_2| ≥ (1−s_A)/s_A, so s_B ≤ s_A.
- On R2: (1−s_A)/s_A ≥ |c'_1|/c'_2 ≥ (1−s_B)/s_B, so s_A ≤ s_B.
- s = 1 fails for A on R2 (it would need c'_1 ≥ 0), and s = 0 fails for A on R1 (it would need
  c_2 ≥ 0).
Hence s_A = s_B = s* ∈ (0,1), with ties on R1 ∪ R2. Then
the splice E of (Sp) is s*-Bayes on 𝔇. A weak dominator Y lies in 𝔇 with the same primaries,
and strictness would lower the s*-sum. So E ∈ U_L is incoherent, contradicting (L1). ∎

## 2. Closed choice forces ideal fibres

Fix t ∈ (0,1) and write 𝔅 = 𝔅_t, J = J_t. Let 𝒦 = {(P_1, S_1, S_2)(X) : X ∈ 𝔅} ⊂ ℝ³, which is
convex and compact (Au). For x ∈ J put g_l(x) = min{S_l : (x, S_1, S_2) ∈ 𝒦} (l = 1, 2). Each g_l
is convex on J, hence continuous on int J. Level x is **ideal** if some X ∈ F_t(x) has
S_1(X) = g_1(x) and S_2(X) = g_2(x), i.e. one fibre member minimises both secondaries.

**Lemma SF (PROVED).** Under (LA), (S), (C) and class 𝓛₂, every x ∈ int J_t is ideal, for every
t ∈ (0,1).
*Proof.*
- *The non-ideal set is open.* The ideal set is {x ∈ int J : (x, g_1(x), g_2(x)) ∈ 𝒦}. This is
  closed in int J, because 𝒦 is closed and g_1, g_2 are continuous there. So the non-ideal set
  N is relatively open in int J.
- *Each non-ideal level yields an improvable undominated model.* Let x ∈ N. Choose Z_1 ∈ F_t(x)
  lexicographically minimising (S_1, S_2), and Z_2 ∈ F_t(x) lexicographically minimising
  (S_2, S_1). Both exist by compactness of 𝒦 ∩ {P_1 = x}. Non-ideal means S_1(Z_2) > S_1(Z_1).
  - Z_2 is undominated. A weak dominator Y lies in F_t(x) (Lemma F(i)). It has
    S_2(Y) ≤ S_2(Z_2) = g_2(x), hence S_2(Y) = g_2(x), and then S_1(Y) ≥ S_1(Z_2) by the
    lexicographic choice of Z_2. So it is not strict.
  - Z_2 is improvable at world 1: Z_1 ∈ M has P_1(Z_1) = x = P_1(Z_2) and S_1(Z_1) < S_1(Z_2).
  So x ∈ {P_1(X) : X ∈ U_L improvable at 1}, which is countable by (T7).
- *Conclusion.* N is open and countable, hence empty. ∎

**Corollary SF-L (two-sided Lagrangian at interior levels; PROVED).** Let t ∈ (0,1), and let
X ∈ U_L ∩ 𝔅_t with P_1(X) ∈ int J_t. Then there are λ, μ ∈ ℝ such that X minimises both
S_1 + λP_1 and S_2 + μP_1 over 𝔅_t. By (PB), X's advice is a.e. a pointwise minimiser of both
ψ_1 + λφ_1 and ψ_2 + μφ_1 over the advice ranges of 𝔅_t.
*Proof.* The level is ideal (SF). By (F*), X is Pareto in its fibre, so it attains both
minima. The lower boundary g_1 of the convex compact set {(P_1, S_1)} over 𝔅_t has a finite
subgradient −λ at the interior point P_1(X). So S_1 − (−λ)P_1 is minimised at X. The same holds
for S_2. ∎

**Lemma BWC (blind choice kills interior levels; PROVED).** Let t ∈ (0,1). Suppose that on a
non-null set Q of mixed problems the advice range of 𝔅_t contains two distinct kinds of advice a, b ∈ {+, 0, −}
with φ_1(a) = φ_1(b). Suppose also that every kind of advice in {+, 0, −} that lies in the advice range of 𝔅_t has the
same φ_1 as a and b. Then int J_t = ∅.
*Proof.* Suppose x ∈ int J_t. By SF there is an ideal I ∈ F_t(x), Pareto in its fibre, hence
undominated (F*), hence in U_L. By SF-L it pointwise minimises ψ_1 + λφ_1 and ψ_2 + μφ_1.
- On Q every kind of advice in {+, 0, −} in the advice range has the same φ_1. So the first Lagrangian picks the
  world-1-best of them, and the second picks the world-2-best (ψ_l is strict where φ_l
  ties).
- × is not a candidate. Its t-primary is minimal only if φ_1(×) and φ_2(×) equal the common
  values, and then ψ_1 and ψ_2 rank it last.
- On mixed problems the world-1-best and world-2-best of two or more kinds of advice in {+, 0, −}
  differ. Contradiction. ∎
(Its use below is always with Q = R2 and {a, b} = {−, 0}. There the third kind of advice +, if
present, is φ-tied as well; this is verified case by case.)

**Lemma 7′ (depth-k staircase; PROVED, any n, any finite number of real levels).** Let world i
rank by lex(L¹_i, …, L^m_i) with real-valued levels, and assume (S). Call X *improvable at depth
k* at i if some Z ∈ M has L^j_i(Z) = L^j_i(X) for j < k and L^k_i(Z) < L^k_i(X). Then
{(L¹_i, …, L^{k−1}_i)(X) : X ∈ U_L improvable at depth k} is countable.
*Proof.* As R2 Thm 7. Let X be tied (equal levels) with a selected C_p. Then p ∉ A_i(Z), which is
closed, so some neighbourhood V of p misses A_i(Z). For q ∈ V, C_q ⪯_i Z fails. Hence
(L¹,…,L^{k−1})(C_q) ≥_lex (L¹,…,L^{k−1})(C_p); otherwise C_q ≺_i Z. So the lexicographic profile
has a local minimum at p. Distinct minimum values v ≠ v′ get distinct basic open sets from a
countable base: on a common one, each would be ≥_lex the other. ∎
(Used only in §6.)

## 3. Theorem 1′₂ and its proof

**Theorem 1′₂ (PROVED).** n = 2, decomposable domain M, class 𝓛₂ at both worlds, (LA), (S), (C). Then
U_L contains no strictly nested pair. Consequently (R2 Theorem R) U_L is the undominated set of
an additive strictly guiding (LA),(S),(C) system on M, and it is a continuous monotone path.

*Notation.* Let A, B ∈ U_L be strictly nested, with R1 and R2 as above. On R1 (A: +, B: 0) put
 d_1 = φ_1(0) − φ_1(+) ≥ 0,  d_2 = φ_2(+) − φ_2(0) ≥ 0.
On R2 (A: −, B: 0) put
 e_1 = φ_1(−) − φ_1(0) ≥ 0,  e_2 = φ_2(0) − φ_2(−) ≥ 0.
For t ∈ T_A, (PB) gives a.e.
 (A1) (1−t) d_2 ≤ t d_1 on R1,  (A2) t e_1 ≤ (1−t) e_2 on R2.
For t ∈ T_B:
 (B1) t d_1 ≤ (1−t) d_2 on R1,  (B2) (1−t) e_2 ≤ t e_1 on R2.

T_A and T_B are closed intervals. Exactly one of the following holds:
(a) T_A ∩ T_B meets (0,1);
(b) T_A ∩ T_B ⊆ {0, 1} and is nonempty;
(c) T_A ∩ T_B = ∅.

### Case (a): a common interior support t₀.
Put 𝔅 = 𝔅_{t₀} and J = J_{t₀}. Then A, B ∈ 𝔅, so on R the advice of both lies in the advice ranges of 𝔅. (A1) and
(B1) at t₀ give d_2 = κ d_1 on R1, and (A2), (B2) give e_2 = κ e_1 on R2 (κ = κ_{t₀}). Split
R = R⁺ ∪ R⁰, where R⁰ is the set on which A's and B's advice has equal φ_1, hence equal φ_2.

*(a0) int J = ∅.* Then 𝔅 is an additive face (§1), and Lemma A applies with 𝔇 = 𝔅 (Lemma F(i)).
Contradiction.

*(a1) int J ≠ ∅.* First, where A and B can sit.
- *A at an interior level.* By SF-L, A pointwise minimises ψ_1 + λ_Aφ_1 and ψ_2 + μ_Aφ_1.
  - On R⁰ ∩ R1, + and 0 are φ-tied and ψ_2(0) < ψ_2(+), so the second Lagrangian rejects A's +.
  - On R⁰ ∩ R2, ψ_1(0) < ψ_1(−) rejects A's −.
  Hence R⁰ is null.
- *B at an interior level.* Symmetrically: on R⁰ ∩ R1, ψ_1 rejects B's 0; on R⁰ ∩ R2, ψ_2
  rejects B's 0. Hence R⁰ is null.
- *A at min J* (pointwise φ_1-minimal in 𝔅): on R2⁺, 0 has smaller φ_1 than A's −, so R2⁺ is
  null.
- *A at max J:* R1⁺ is null.
- *B at min J:* R1⁺ is null.
- *B at max J:* R2⁺ is null.

*Sub-case R⁰ null.* Then R1 = R1⁺ and R2 = R2⁺ are both non-null. So neither A nor B is at an
endpoint, and both are at interior levels. By SF-L:
- On R1, with σ_1 = ψ_1(0) − ψ_1(+), A gives σ_1 + λ_A d_1 ≥ 0 and B gives σ_1 + λ_B d_1 ≤ 0.
  Since d_1 > 0 on R1, λ_A ≥ λ_B.
- On R2, with τ_1 = ψ_1(−) − ψ_1(0), A gives τ_1 + λ_A e_1 ≤ 0 and B gives τ_1 + λ_B e_1 ≥ 0.
  Since e_1 > 0, λ_B ≥ λ_A.
- So λ_A = λ_B = λ*, with equality in both relations on R. Identically, μ_A = μ_B = μ*.
- Every splice E of A and B on R therefore pointwise minimises both ψ_1 + λ*φ_1 and
  ψ_2 + μ*φ_1 over the advice ranges of 𝔅, and E ∈ 𝔅.
- E is undominated. A weak dominator Y lies in 𝔅 with P_1(Y) = P_1(E) (Lemma F(i)). Then
  S_l(Y) ≥ S_l(E) by Lagrangian optimality, so it is not strict.
Take E as in (Sp): it is incoherent and in U_L, contradicting (L1).

*Sub-case R⁰ non-null.* Then neither A nor B is at an interior level, so both are at endpoints
of J.
- (min, min): R2⁺ and R1⁺ are null, so A, B ∈ 𝔅^− (P_1 = min J, an additive face). Lemma A
  applies with 𝔇 = 𝔅^−: weak dominators of members of 𝔅^− lie in 𝔅 at the same P_1 level,
  hence in 𝔅^−. Contradiction.
- (max, max): the same with 𝔅^+.
- (A at min, B at max): R2⁺ is null, so R2 = R2⁰. Take any x ∈ int J and the ideal I ∈ F(x)
  (SF), and let c be I's advice on R2⁰.
  - The two Lagrangians of SF-L exclude c = 0 (ψ_2 prefers the φ-tied −) and c = − (ψ_1
    prefers the φ-tied 0).
  - They exclude c = ×: if × is in the advice range of 𝔅 it is φ-tied with − and 0, and ψ_1 ranks it
    worse than 0.
  - So c = + is in the advice range of 𝔅 a.e. on R2⁰, with φ_1(+) ≠ φ_1(−). If φ_1(+) = φ_1(−), ψ_2 would
    prefer −. With weak guidance, φ_1(+) < φ_1(0) = φ_1(−).
  - But A ∈ 𝔅^− is pointwise φ_1-minimal in the advice ranges of 𝔅 and picks − on R2⁰. Contradiction.
- (A at max, B at min): R1 = R1⁰. Symmetrically, the ideal I picks − on R1⁰ with
  φ_1(−) > φ_1(0) = φ_1(+), contradicting A ∈ 𝔅^+ picking +.

### Case (b): a common support t ∈ {0, 1}, none in (0,1).
By the world-swap symmetry (below), take t = 1, so A, B ∈ 𝔐 := 𝔅_1. By Lemma F(ii), weak
dominators of members of 𝔐 lie in 𝔐. On the advice ranges of 𝔐, φ_1 is constant, so ψ_1 is strictly guiding
there. World 1 is thus the additive S_1, and world 2 is lex(P_2, S_2).
- A and B are weakly Pareto in (S_1, P_2) over 𝔐: a Y ∈ 𝔐 strictly lower in both would
  dominate. So they have supports θ ∈ Θ_A, Θ_B ⊆ [0,1], and (PB) applies to
  θψ_1 + (1−θ)φ_2 over the advice ranges of 𝔐.
- On R1 put σ = ψ_1(0) − ψ_1(+) > 0 (φ_1 is tied, so ψ_1 is strict) and d_2 as before. On R2
  put τ = ψ_1(−) − ψ_1(0) > 0 and e_2 as before. Then:
  A: (1−θ)d_2 ≤ θσ on R1 and θτ ≤ (1−θ)e_2 on R2.
  B: θσ ≤ (1−θ)d_2 and (1−θ)e_2 ≤ θτ.
- θ = 1 is impossible for A (it needs τ ≤ 0) and for B (it needs σ ≤ 0).
- *No common θ.* If all of Θ_A lies below all of Θ_B: take θ_A < θ_B < 1. Then
  d_2/σ ≥ θ_B/(1−θ_B) > θ_A/(1−θ_A) ≥ d_2/σ, impossible. If all of Θ_B lies below Θ_A: R2 gives
  e_2/τ ≥ θ_A/(1−θ_A) > θ_B/(1−θ_B) ≥ e_2/τ, impossible.
- *Common θ₀ = 0.* A and B both pointwise minimise φ_2 over the advice ranges of 𝔐. A's + on R1 forces
  d_2 = 0, and B's 0 on R2 forces e_2 = 0. Then 𝔅'' = argmin_𝔐 φ_2 (pointwise) is an additive
  face: φ_1 and φ_2 are constant on its advice ranges. It is closed under weak domination with equal
  primaries (Lemma F(ii), then P_2 ≤ min). Lemma A gives a contradiction.
- *Common θ₀ ∈ (0,1).*
  - The two inequalities at θ₀ become equalities. So d_2 = θ₀σ/(1−θ₀) > 0 on R1 and e_2 > 0
    on R2.
  - Let 𝔅' be the decomposable domain of pointwise minimisers of θ₀ψ_1 + (1−θ₀)φ_2 in 𝔐. Weak
    dominators of members of 𝔅' lie in 𝔅' with equal S_1 and P_2 (as in Lemma F(i)). So
    X ∈ 𝔅' is undominated iff it minimises S_2 on its P_2-fibre; there is a single objective,
    so no SF is needed.
  - A is at an interior P_2-level of 𝔅'. The P_2-minimum would pick 0 on R1 (d_2 > 0), and the
    P_2-maximum would pick 0 on R2 (e_2 > 0).
  - B is interior too. The minimum would pick − on R2, and the maximum would pick + on R1.
  - Hence finite multipliers exist: A and B pointwise minimise ψ_2 + ν_Aφ_2 and ψ_2 + ν_Bφ_2
    over the advice ranges of 𝔅'. R1 gives (ψ_2(+) − ψ_2(0)) + ν d_2 ≤ 0 for A and ≥ 0 for B, so ν_A ≤ ν_B.
    R2 gives (ψ_2(−) − ψ_2(0)) − ν e_2 ≤ 0 for A and ≥ 0 for B, so ν_A ≥ ν_B.
  - So ties hold on R. The (Sp) splice minimises S_2 + ν*P_2 over 𝔅', so it is undominated
    and incoherent. Contradiction.
(This re-proves R2 Theorem 6 without needing S_2 to be guiding where φ_2 is strict.)

### Case (c): T_A ∩ T_B = ∅.
**World-swap symmetry.** Relabel the worlds and represent each pair by g′ = (−g_2, −g_1). This
maps + ↔ −, R1 ↔ R2, D_{[α,β]} ↦ D_{[1−β, 1−α]} (nesting preserved), T ↦ 1 − T, and every
axiom to itself. So we may assume every element of T_B is below every element of T_A.

**Step 0 (R2 is primary-blind).** Take t_B ∈ T_B and t_A ∈ T_A, with t_B < t_A.
- If t_A < 1: (A2) and (B2) give κ_A e_1 ≤ e_2 ≤ κ_B e_1 with κ_B < κ_A. So e_1 = 0, then e_2 = 0
  (if t_B = 0, (B2) gives e_2 ≤ 0 directly).
- If t_A = 1: (A2) gives e_1 = 0, and (B2) with t_B < 1 gives e_2 = 0.
So on R2, − and 0 have identical (φ_1, φ_2). Put t_A := min T_A > 0.

**Step 1.** For t ∈ (0, t_A), the advice range of 𝔅_t on R2 contains − and 0, and its elements of
{+, 0, −} are all φ-tied.
- − is a t_A-minimiser on R2 (A ∈ 𝔅_{t_A}).
- Let f(t) = t(φ_1(+) − φ_1(−)) + (1−t)(φ_2(+) − φ_2(−)) = −ta + (1−t)b, with a, b ≥ 0. Then
  f(t) = f(t_A) + (t_A − t)(a + b) ≥ 0, with equality only if a = b = 0.
- × is never t-cheaper than −. And 0 is φ-tied with −.

**Step 2.** For t ∈ (0, t_A), Lemma BWC (Q = R2) gives int J_t = ∅. So F_t = {π_t} is a single
point, and 𝔅_t is an additive face.

**Step 3 (π_t is constant).**
- For t ∈ (0, t_A), the additive system (S_1, S_2) on 𝔅_t has distinct Pareto end points. Its
  S_2-minimiser picks − on R2 and its S_1-minimiser does not.
- The lexicographic (S_2, S_1)-minimiser W_t is undominated, by Lemma F(i) and the same
  argument as for Z_2 in SF. It is improvable at world 1, by the S_1-minimiser at the same
  primaries.
- By (T7), {P_1(π_t) : t ∈ (0, t_A)} is countable.
- t ↦ F_t is upper hemicontinuous and singleton-valued on (0, t_A), hence continuous, so
  t ↦ P_1(π_t) is continuous with countable range, hence constant. Points of F_t with equal
  P_1 and t < 1 also have equal P_2.
- So π_t = π* for all t ∈ (0, t_A), and by closedness T_{π*} ⊇ [0, t_A].

**Step 4.** If some t ∈ T_B lies in (0, t_A), then π(B) ∈ F_t = {π*}, so T_B = T_{π*} ∋ t_A ∈ T_A.
This contradicts (c). Hence T_B = {0} and π(B) ≠ π*.

**Step 5.** Both π(B) and π* lie in the 0-face {P_2 = min}, and π* is its P_1-minimal point (it
lies in F_t for small t > 0). So P_1(B) > P_1(π*).
- B ∈ 𝔅_0. Within 𝔅_0, P_2 is constant. If Y ∈ 𝔅_0 had P_1(Y) < P_1(B) and S_2(Y) < S_2(B), it
  would dominate B. So B is weakly Pareto in (P_1, S_2) over 𝔅_0, and some θ ∈ [0,1] makes B a
  pointwise minimiser of θφ_1 + (1−θ)ψ_2 over the advice ranges of 𝔅_0.
- θ = 1 is impossible: models with primaries π* lie in 𝔅_0 (0 ∈ T_{π*}) and have smaller P_1.
- θ < 1 is impossible: on R2, − and 0 are both in the advice ranges of 𝔅_0 (B's 0 is φ_2-minimal, and − is
  tied with it) and are φ_1-tied, while ψ_2(−) < ψ_2(0). So B's 0 is not a minimiser on the
  non-null R2. Contradiction.

**Branch t_A = 1 (T_A = {1}).** Steps 1–3 run on (0,1), so T_{π*} = [0,1] and π* minimises both
P_1 and P_2. If π(A) ≠ π*, then P_1(A) = P_1(π*) and P_2(A) > P_2(π*). Inside 𝔐 = 𝔅_1, A is
weakly Pareto in (S_1, P_2), with support θ:
- θ = 0 would give P_2(A) ≤ P_2(π*);
- θ > 0 fails on R2, where 0 is φ-tied with − and ψ_1(0) < ψ_1(−).
So π(A) = π*, and T_A = [0,1] ⊇ T_B. Contradiction. ∎

**Remarks on the proof.**
1. (S) enters only through (T7), used in SF and Step 3. (C) enters only through (L1). (LA)
   enters through (L1)'s KKM step. Everything else is convex analysis in ℝ² and ℝ³ plus
   pointwise comparisons on R1 and R2.
2. Hypotheses actually used on the levels: integrability; weak guidance of φ_i; strict
   lexicographic guidance of (φ_i, ψ_i). No sign condition on ψ_i where φ_i is strict. This is
   exactly the freedom R5 Example 4.3 exploits, so the theorem covers that class.
3. Which (S)-consequence is decisive? In Example 4.3 (κ = 1, t₀ = ½), every fibre of 𝔅_{1/2}
   is a segment along which S_1 decreases and S_2 increases. So every level is non-ideal, and
   SF shows that no system containing that face can satisfy (S). This answers R5's question of
   whether 4.3 can be completed: not with two levels.

## 4. Consequences

**Corollary 4.1 (PROVED).** For n = 2 and any decomposable domain, every (G),(IB),(LA),(S),(C) system
in class 𝓛₂ has the same undominated set as some additive strictly guiding (LA),(S),(C) system
on the same domain (Theorem 1′₂ + R2 Theorem R). In particular, such systems cover exactly the
targets that additive systems cover with the same advice ranges. For n = 2 every target is already
covered (v3), so there is no coverage gain to look for there. The point is structural:
**two-level lexicographic (IB) rankings do not enlarge what closed choice can select in two
worlds.**

**Corollary 4.2 (PROVED).** In n = 2, Conjecture 1 holds for every system whose two worlds are
both sandwiched (R5 Cor UN2), and for every system whose two worlds are both of class 𝓛₂
(Theorem 1′₂). The mixed case, with one world of each kind, is open (§7).

## 5. Part (A): the constructions tried, and why each fails

The brief asked for a construction that combines R5 Example 4.3 with a countable staircase.
Theorem 1′₂ shows that no such construction exists with two additive levels. It is still worth
recording exactly where each natural design dies, because §6 needs this.

**5.1 The 4.3 face alone.** Example 4.3 lives in the face 𝔅_{1/2}, with proportional primaries
on R. All its fibres are non-ideal. SF says the non-ideal levels of an interior face are empty.
Dead: (S) fails at uncountably many primary levels (R2 Thm 7 / T7).

**5.2 4.3 at a single exceptional level.** Make the fibres ideal except at one level x*, and put
the nested pair in F(x*). Impossible: ideal levels form a relatively closed subset of int J. So
the non-ideal set is open, and a single interior level cannot be non-ideal. Dead (SF).

**5.3 Pair at the ends of an edge.** Put A at min J and B at max J of one primary edge (case
(a1), (min, max)). Then R2 must be primary-blind. The ideal points in the middle of the edge are
required to accept on R2 with a φ_1-cheaper +, which contradicts A's φ_1-minimality. Dead.

**5.4 Pair at a vertex, or at the ends of a primary edge.** At a vertex π_v of 𝒫 (or at an
endpoint of an edge) the fibre is a decomposable domain with constant primaries, i.e. an additive
(S_1,S_2) system. This is the only place the countable staircase allowed by (T7) can carry
improvable members, and Lemma A forbids nesting there. Dead.

**5.5 Pair on two different faces.** Disjoint T_A, T_B (case (c)). The primaries must be blind on
one of the two regions (Step 0). The blind region then makes every face strictly between the two
an additive face (BWC), and these faces have improvable members. By (T7) they all collapse onto
one kink point π*. The far member is then on a flat face through π*, where the blind region
contradicts its Pareto support. Dead.

**5.6 Remark: structure of U_L for class 𝓛₂ (a sketch, not verified in full, and not used in
the theorem).** U_L is the union of:
- for each t ∈ (0,1) with int J_t ≠ ∅, the chain of ideal points {I_x : x ∈ int J_t}. Each is a
  two-sided Lagrangian, and per problem it is monotone in x, because without blind choice
  φ_1 strictly orders the kinds of advice in {+, 0, −} that lie in the advice range;
- at the countably many vertices of 𝒫 and the edge endpoints, additive Bayes paths of the
  faces 𝔅_t^±;
- the analogous pieces inside 𝔅_0 and 𝔅_1, each of the (one additive world, one lex world)
  type.
This is the "countable staircase": additive steps at vertices joined by Lagrangian ramps along
edges. Every piece is a ⪯_m-chain, and Theorem 1′₂ says the pieces never interleave into a
nested pair.

## 6. Three or more levels: what carries over (sketch; CONJECTURE)

World i = lex(L¹_i, …, L^m_i), additive levels, L¹_i weakly guiding, composite strictly guiding.

*What iterates (CHECKED as a sketch, not written in full).* Take the common-interior-support
branch (a).
- At depth 2, Lemma 7′ with k = 2 gives SF verbatim, with "ideal" meaning that the depth-2
  secondaries (L²_1, L²_2) are simultaneously minimised on the fibre. Every interior level is
  depth-2-ideal.
- So members at interior levels lie in 𝔅^{λ,μ}, the decomposable domain of joint pointwise minimisers
  of ψ²_1 + λφ_1 and ψ²_2 + μφ_1. On 𝔅^{λ,μ} all depth ≤ 2 quantities are affine in P_1.
- If A and B are both at interior levels, the multiplier argument of (a1) forces a common
  (λ*, μ*). (On the doubly blind part of R, depth-2 ties are forced instead of contradictions.)
  So A, B ∈ 𝔅^{λ*,μ*}.
- Inside 𝔅^{λ*,μ*}, domination again requires equal P_1. The depth-3 levels then play the role
  of S, and Lemma 7′ with k = 3 gives SF at depth 3, because ideal levels within the P_1-range
  of the fixed domain 𝔅^{λ*,μ*} are again relatively closed.
- One iterates down to an additive face (Lemma A) or a two-sided Lagrangian contradiction.
- Key point: at each depth the exceptional (non-ideal) levels are confined to the endpoints of
  the P_1-range of a decomposable domain, where all higher levels are constant. That is an additive
  face at the next depth.

*What is not done.* Cases (b) and (c) at depth ≥ 2. These are configurations in which a region
is blind at depth 1 and depth 2 for some kinds of advice but not others. The world-swap and
Step 0–5 arguments must be redone with the "first level that sees R1, R2" varying across
sub-regions. I see no mechanism for a counterexample there, but I have not excluded one.

**Conjecture 1′_m (CONJECTURE).** Theorem 1′₂ holds for every finite number of additive
lexicographic levels. Countably many levels (lex over ℕ): not even sketched. Theorem 7's
countable-base argument works for any well-ordered lexicographic profile with real
coordinates, but SF's closedness step uses finitely many objectives.

## 7. Status

| Claim | Status |
|---|---|
| Lemma F (faces closed under domination) | PROVED |
| Lemma A (additive faces carry no nested pair) | PROVED |
| Lemma SF (interior levels of interior primary faces are ideal, under (S)) | PROVED |
| Corollary SF-L (two-sided Lagrangian at interior levels) | PROVED |
| Lemma BWC (blind choice on a non-null set ⇒ the face's P_1-range is a point) | PROVED |
| Lemma 7′ (depth-k staircase, any n, finitely many real levels) | PROVED |
| **Theorem 1′₂: n = 2, two-level lex (additive levels) at both worlds, (LA),(S),(C) ⇒ no strictly nested pair in U_L** | **PROVED** |
| Corollary 4.1: such U_L is additively representable (monotone path) | PROVED (with R2 Thm R) |
| Case (b) re-proves R2 Thm 6 without guidance of S where φ is strict | PROVED |
| R5 Ex. 4.3's face cannot occur in any (S) system with two levels | PROVED (SF) |
| §5.6 structure of U_L for 𝓛₂ | remark, unverified sketch |
| m ≥ 3 levels, branch (a) | CHECKED as sketch only |
| Conjecture 1′_m (m ≥ 3, finite) | CONJECTURE |
| Conjecture 1 (all (IB) systems, n = 2) | CONJECTURE (open) |

**Where a counterexample to Conjecture 1 (n = 2) can still live.**
1. At least one world is neither sandwiched (R5 UN) nor of class 𝓛₂. The mixed case "one world
   sandwiched, the other 𝓛₂" is not covered by either proof. It is probably closable by running
   §3 with the sandwiching family's pairings in place of the 𝓛₂ primary at that world, but I
   have not checked this.
2. Lexicographic orders with three or more additive levels, in cases (b) or (c) at depth ≥ 2.
3. Orders with no additive structure at any level (IRWAS/KPS ultrafilter type). Nothing beyond
   R5 Lemma X is known there.

**Answer to R7.** No counterexample was found with two-level lexicographic worlds (additive
levels), and none exists: Theorem 1′₂. Combining Example 4.3's mechanism with a countable
staircase fails for a precise reason, Lemma SF. Closed sections make the set of non-ideal
primary levels countable, convexity makes it relatively open, so it is empty. That leaves room
for non-additive secondary behaviour only on additive faces, where R2 Theorem N already forbids
nesting.
