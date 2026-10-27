# MM2 (round 41, BRIEF33). Attack on (QS): refined mirror swaps reduce (QS) exactly to a boundary-alignment condition; it is violated by generic and by world-separable judges at T1, and on every edge it becomes a selection-independent identity on the judges

18 Oct 2026. Rules of BRIEF13 and BRIEF33; the corrections of AUDIT_LL.md are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script in `mm2py/`.
- **NUMERICS**: none used.
- **CONJECTURE**: marked where offered.

Scripts: `mm2py/t1_separable.py`, `branch_comb.py`, `generic_t1.py`, `edge_ratio.py`, each with a `.out`. Run
`python3 -I <script>.py` from inside `mm2py/`. All verdicts use `fractions.Fraction` or exact sympy rationals. Nothing in
a proof rests on a script.

Setting: three worlds, μ the standard Gaussian, T1 = D_K with K = (1−ε)u + εΔ, any ε ∈ (0,1), c₀ := (1−ε)/3, vertices
v_k = c₀𝟙 + εe_k, corner rays r_12, r_23, r_31 (write-up §2.3). No assumption is added. Every extra hypothesis below is a
hypothesis of the stated result and is named there.

---

## 0. Outcome

**No complete obstruction to (QS) is proved.** What is proved is an exact reduction of the local adversary, a
selection-independent rigidity on every edge, and two precisely described classes of judges for which (QS) fails through
T1. The reduction is stated in §7.

1. **(QS) is one protection condition per branch (Lemma 1.1, PROVED).** (QS) at p holds iff, for each of the
   C(n, n−q+1)^{|supp p|} branches F, the selected model C_p is the only model with L_iv(X) ≤ L_iv(C_p) for every
   (i,v) ∈ F. This is the audit's nonstrict test, written as a protection condition for each branch.
2. **Refined mirror swaps give exactly a boundary-alignment condition (Theorem 3.1 and Propositions 4.1, 4.3; PROVED).**
   - Call y a *common essential value* at a boundary of C_p if the judges' switch map across that boundary takes values
     arbitrarily near y on non-null sets on both sides.
   - (QS) at p forces, for every branch F, a nonnegative nonzero weight w_F on F that annihilates **every** common
     essential value at **every** boundary of C_p (one w_F for all boundaries).
   - Conversely, if for some branch no such w_F exists, an explicit multi-site swap defeats (QS). It uses judge-dependent
     masses on both sides of several boundary points, and every increment in the branch is strictly negative.
   - If w_F exists and is strictly signed off the boundary on each side, no local record defeats F.
   - So the brief's idea (1), done exactly, yields this alignment condition and nothing more. The second-order density
     terms help the adversary only when alignment fails.
3. **Rigidity at each p (Lemmas 3.2–3.3; PROVED, combinatorics CHECKED).**
   - Every w_F meets worlds of both signs of every common essential value. At T1 with continuous judges, it meets all
     three worlds.
   - If q ≥ 3 and two or more worlds are active, the annihilator of the common essential values has dimension ≥ 3.
     Equivalently, these values span at most 9 of the 12 dimensions at full support (n = 4, q = 3).
4. **Generic judges fail at T1 (Corollary 4.2, PROVED; illustration CHECKED).**
   - (QS) fails at T1's index whenever, for some branch, the switch values on ∂D_{T1} span a subspace of ℝ^F containing a
     strictly negative vector. In particular it fails whenever they span ℝ^F.
   - For twelve explicit heterogeneous polynomial judges, all 216 branches have rank 6 at twelve facet points of T1, with
     an explicit defeating combination (`generic_t1.out`).
5. **World-separable judges are excluded (Theorem 5.1, PROVED; algebra CHECKED).**
   - Suppose that near ∂D_{T1} each judge's accept-versus-silence switch has the form θ(g)·φ_iv(g_i): a common positive
     factor times a function of that world's own payoff. Then T1 is not a pointwise weak Bayes model of **any** nonzero
     nonnegative mixture of the judges.
   - Hence (QS) fails through T1, in every branch, on the full domain and on every decomposable domain with (LF) at T1.
     The proof is a local Pexider equation on each facet piece, plus slope matching across facets, which is impossible
     because ε > 0.
6. **Edges: a selection-independent identity (Theorem 6.4, PROVED, full domain; no regularity of the judges).**
   - On the open edge (e_i, e_j), C_p = D_{K_p} with K_p inside the edge, and its acceptance boundary sweeps every plane
     Π_s = {(1−s)g_i + s g_j = 0}, s ∈ (0,1), each containing the whole g_k-axis direction.
   - Hence, for a.e. s and every one of the 36 branches (F_i, F_j), some w ≥ 0 gives
     Σ_{v∈F_i} w_iv|y_iv(g)| = Σ_{u∈F_j} w_ju|y_ju(g)| at a.e. point of Π_s, **for every value of the off-edge payoff
     g_k**. Here y is the approximate value of the relevant switch map.
   - Corollary 6.5: (QS) fails whenever, on a positive-measure set of such planes, every world-i/world-j magnitude ratio
     varies strictly monotonically with g_k along a segment (`edge_ratio.out`).
7. **The global route of idea (2) is not available (§8).** (QS) gives per-branch weak Bayes weights, not unique Bayes models.
   The per-branch KKM argument of JJ3 Theorem 2.1 fails, and the reason is identified exactly. So gm and JJ3 cannot be
   imported. I do not assume that Bayes models of mixtures are coherent.

**Use of (IB), (TC), closed sections.**
- None is used anywhere.
- 3q > 2n is not used. Only |F_i| = n − q + 1 is used, and q ≥ 3 in Lemma 3.3.
- Continuity in measure of the selection is used only in §6 (the edge sweep).
- Theorems 3.1, 5.1 and Corollary 4.2 use only (QS) at the single index of T1.

**Single most important open point.** Is the *alignment realisation problem* (§7, (R1)–(R5)) solvable? We need twelve
strictly guiding integrable judges and a coherent family p ↦ C_p, continuous in measure and through T1, such that:
- for every p and every branch F, some w_F(p) ≥ 0 annihilates all common essential switch values on ∂C_p, with the strict
  side conditions;
- on every edge, the identities of Theorem 6.4 hold on every plane Π_s for all values of the off-edge payoff.

Generic and world-separable judges fail; heterogeneity must be confined to directions that the boundaries of the selected
models do not see.

---

## 1. Setting and the branch reformulation

**Domain.** Either the full four-advice domain, or a decomposable domain M with advice range A(h). Pairs are indexed by
f ∈ H = {f_1 > 0}; advice +, 0, −, ×; world ranks good < silence < bad < contradiction (write-up §2).

**Judges.** At each world i there are n judges v ∈ J_i with measurable penalties ℓ_iv(h, a), a ∈ A(h). They are strictly
increasing in world-i rank for a.e. h, with integrable envelopes. Write:
- L_iv(X) := ∫ ℓ_iv(h, a_X(h)) dμ;
- Δ_iv(p, X) := L_iv(X) − L_iv(C_p).

Here p ↦ C_p is a selection of coherent models.

**(QS) at p.** For every evaluable X ≠ C_p (mod null sets) there is i ∈ supp p with at least q judges v ∈ J_i having
Δ_iv(p, X) > 0.

**Branches.** A branch at p is F = ⊔_{i∈supp p} F_i with F_i ⊆ J_i and |F_i| = n − q + 1. For n = 4, q = 3 at full
support there are 6³ = 216.

**Lemma 1.1 (PROVED).** (QS) holds at p iff, for every branch F:

  (NT_F) if X is evaluable and Δ_iv(p, X) ≤ 0 for every (i,v) ∈ F, then X = C_p a.e.

*Proof.*
- **(QS) ⇒ (NT_F).** Let X ≠ C_p. Some active i has a set Q of at least q judges with Δ > 0. Since
  |Q| + |F_i| ≥ q + n − q + 1 > n, Q meets F_i. So some (i,v) ∈ F has Δ_iv > 0.
- **(NT_F) for all F ⇒ (QS).** If (QS) fails for X ≠ C_p, then at every active i at most q − 1 judges have Δ > 0, so at
  least n − q + 1 have Δ ≤ 0. Choosing F_i among them gives a branch violating (NT_F). ∎

So each branch is a *six-pseudo-world* additive system: pseudo-world (i,v) ranks by L_iv. The selected model must be
protected by the pseudo-worlds of F in the sense of JJ3's (NT), although the selection is indexed by the 3-world simplex,
not by the simplex of F (§8).

**Switch maps and common essential values.** Fix a model C and advices a ≠ b. Put A := {a_C = a} and B := {a_C = b}. The
switch map is f^{ab}(h) := (ℓ_iv(h,b) − ℓ_iv(h,a))_{i,v}, defined for a.e. h with a, b ∈ A(h). By strict guidance every
entry is nonzero a.e., and the entries of one world share a sign.

For a measurable set E, the essential range R(f|E) is the set of y such that E ∩ (f)^{−1}(B(y,r)) is non-null for every
r > 0 (LL1 §1).

A **common essential value** of C (of type (a,b)) is any y ∈ R(f^{ab}|A′) ∩ R(f^{ab}|B′), where A′ ⊆ A and B′ ⊆ B are the
parts on which b, respectively a, lies in A(h). Let N(C) ⊆ ℝ^{3n} be the set of all common essential values of C, over all
types (a,b). For p fixed and an index set I, write y_I for the restriction of y to I.

**The basic source of common essential values (PROVED).** Let h₀ be a point at which the switch map f^{ab} is
approximately continuous, with approximate value y. Suppose A′ and B′ both have positive upper density at h₀. Then
y ∈ N(C).

*Proof.* The set {|f^{ab} − y| > r} has density 0 at h₀. Since A′ has positive upper density at h₀, the part of A′ inside
f^{−1}(B(y,r)) is non-null near h₀, for every r. The same holds for B′. ∎

Examples:
- T1 at relative-interior facet points g ∉ coordinate planes, with A = accept g and B = silence. Locally the two sides are
  half-spaces of density 1/2. The domain needs accept and silence near ∂D_{T1}, which (LF) gives.
- The edge planes of §6.

---

## 2. Weak Bayes in every branch (η = 0)

**Lemma 2.1 (PROVED; the η = 0 case of LL2 Lemma 2.1 and Prop 8.3).** Suppose (QS) holds at p, and let F be a branch.
Then there is w ∈ ℝ^F, w ≥ 0, w ≠ 0, such that for a.e. h and every b ∈ A(h):

  Σ_{(i,v)∈F} w_iv [ℓ_iv(h,b) − ℓ_iv(h, a_{C_p}(h))] ≥ 0.   (WB_F)

*Proof.*
1. **Convexity.** Z := {(Δ_iv(p,X))_{(i,v)∈F} : X ∈ M} is convex, by Lyapunov's theorem for the atomless vector measure
   with integrable densities and by decomposability (FF2 Step 1, refereed in GG3 §8.1).
2. **No strictly negative point.** If z(X) < 0 componentwise, then X ≠ C_p and X violates (NT_F). So Z misses the open
   negative orthant.
3. **Separation.** Separation gives a nonzero w with w·z ≥ 0 on Z and w ≥ 0, as in LL2 Lemma 2.1 step 3.
4. **Pointwise form.** If (WB_F) failed on a non-null set P, switching C_p to a measurable violating advice on P would give
   w·z < 0. ∎

Lemma 2.1 is necessary only (BRIEF33 correction 3). Exactness needs the nonstrict test of Lemma 1.1.

---

## 3. Boundary alignment and its rigidity

**Theorem 3.1 (alignment; PROVED).** Suppose (QS) holds at p. For every branch F, the weight w = w_F of Lemma 2.1 satisfies

  w · y_F = 0 for every y ∈ N(C_p).

In particular, the linear span of {y_F : y ∈ N(C_p)} contains no vector that is strictly negative on F.

*Proof.*
1. **One side.** Let y ∈ N(C_p) be of type (a,b), and let r > 0. On a non-null subset of A′ we have |f^{ab} − y| < r, and
   (WB_F) at advice b gives w·f^{ab}_F ≥ 0 there. So w·y_F ≥ −r Σw.
2. **The other side.** On a non-null subset of B′ we also have |f^{ab} − y| < r. There the switch to a is f^{ba} = −f^{ab},
   so (WB_F) gives −w·f^{ab}_F ≥ 0. Hence w·y_F ≤ r Σw.
3. **Conclusion.** Let r → 0. The second statement follows: a strictly negative z = Σλ_j y^j_F would give
   0 = w·z < 0, since w ≥ 0 and w ≠ 0. ∎

The point is that **one** w_F serves every boundary type and every boundary point of C_p simultaneously. By Gordan's
alternative, the second statement is equivalent to the existence of such a w for the finitely many values that span
⟨N(C_p)_F⟩.

**Lemma 3.2 (sign support; PROVED).** Let y ∈ N(C_p), and let s_i be the common sign of the world-i entries of y. Then for
every branch F, the support of w_F contains a judge at a world with s_i = + and a judge at a world with s_i = −. If N(C_p)
contains values of three sign patterns of which each world is the unique odd world in one, then supp w_F meets every
world. This happens, for instance, at T1 when the judges' accept/silence switch is approximately continuous at one point
of each of the nine facet pieces of §5.

*Proof.* w·y_F = Σ_i s_i Σ_{v∈F_i} w_iv|y_iv| = 0 with every |y_iv| > 0. For the second claim, suppose the pattern with
unique odd world o has sign σ_o at o, opposite to the other two worlds. Then supp w_F must contain world o. The facet
pieces are listed in §5 (CHECKED `t1_separable.out`): all six mixed patterns occur. ∎

**Lemma 3.3 (dimension; PROVED, combinatorics also CHECKED `branch_comb.out`).** Assume q ≥ 3 and |supp p| ≥ 2, and let
(QS) hold at p. Put J_S := ⊔_{i∈supp p} J_i, and let W_p ⊆ ℝ^{J_S} be the annihilator of {y_{J_S} : y ∈ N(C_p)}. Then
dim W_p ≥ 3. Equivalently, the common essential values span at most |J_S| − 3 dimensions: 9 at full support for n = 4,
q = 3.

*Proof.*
1. **What W_p must contain.** By Theorem 3.1, W_p contains, for each branch F, a nonzero w ≥ 0 supported in F.
2. **Small W_p.** Suppose dim W_p ≤ 2. The cone W_p ∩ ℝ^{J_S}_+ lies in the pointed orthant, so it is pointed. A pointed
   closed convex cone in a space of dimension ≤ 2 is generated by at most two rays r_1, r_2. Every nonzero member is
   a r_1 + b r_2 with a, b ≥ 0 not both 0, so its support contains supp r_1 or supp r_2.
3. **Two supports can be avoided.** Given nonempty S_1 = supp r_1 and S_2 = supp r_2, choose a ∈ S_1 ∩ J_i and
   b ∈ S_2 ∩ J_j.
   - If i ≠ j, choose F_i ∌ a and F_j ∌ b. This is possible since n − q + 1 ≤ n − 1.
   - If i = j, choose F_i ⊆ J_i ∖ {a, b}. This is possible since n − q + 1 ≤ n − 2, i.e. q ≥ 3.
   - Choose the other F_k arbitrarily.
4. **Contradiction.** The branch F so chosen contains neither S_1 nor S_2, so W_p has no nonzero nonnegative vector
   supported in F. ∎

*Remarks.*
- **Tightness.** The bound 3 is combinatorially tight if signs are ignored: three singleton supports at one world meet
  every branch (CHECKED). But by Lemma 3.2, singletons are excluded as soon as N(C_p) ≠ ∅.
- **Supports at T1.** With the T1 sign condition, every support meets all three worlds with at most two judges per
  world. Such a support lies in at most 3·3·3 = 27 branches. So W_p ∩ ℝ_+ has at least ⌈216/27⌉ = 8 distinct extreme
  supports (PROVED by counting; CHECKED).
  - The 27 transversals T × T × T with |T| = 3 at each world do suffice combinatorially (CHECKED).
  - Whether a subspace of dimension 3 can carry the needed supports is not settled here.
- **Strength.** Lemma 3.3 says that, at every index with at least two active worlds, the judges restricted to the boundary
  of the selected model must satisfy at least three independent linear identities. At least one is nonnegative in every
  branch. Generic judges violate this (Corollary 4.2).

---

## 4. Refined mirror swaps: the constructive adversary, and why it can do no more

**Proposition 4.1 (multi-site swap; PROVED).** Let C = C_p, and let F be a branch at p. Suppose y^1, …, y^k ∈ N(C), of
types (a_j, b_j), and λ ∈ ℝ^k satisfy z := Σ_j λ_j y^j_F < 0 componentwise. Then there is an evaluable X ≠ C with
Δ_iv(p, X) < 0 for every (i,v) ∈ F. So (NT_F) and (QS) fail at p.

*Proof.*
1. **Constants.** Put ζ := min_F |z_iv| > 0 and Λ := Σ_j |λ_j| > 0, and choose r with 0 < r < ζ/(2Λ).
2. **The sets.** For each j, let A_j ⊆ A′_j be a non-null set on which |f^{a_jb_j} − y^j| < r, and B_j ⊆ B′_j similarly.
   - These exist by the definition of N(C), and f^{a_jb_j} is bounded on them.
   - Choose 0 < m < min_j min(μ(A_j), μ(B_j))/(2Λ).
   - Choose the sets E_j one after another, using atomlessness: E_j ⊆ A_j of measure mλ_j when λ_j > 0, and E_j ⊆ B_j
     of measure m|λ_j| when λ_j < 0, in each case avoiding the earlier E_l. This is possible because the earlier sets
     have total measure < mΛ < μ(A_j)/2 (resp. μ(B_j)/2). The E_j are pairwise disjoint.
3. **The record.** Let X switch C from a_j to b_j on E_j ⊆ A_j, and from b_j to a_j on E_j ⊆ B_j. Then X is evaluable
   (decomposability, and the advices lie in A(h) on A′_j, B′_j), and X ≠ C.
4. **Increments.** For each (i,v) ∈ F, Δ_iv = Σ_j sgn(λ_j) ∫_{E_j} f^{a_jb_j}_iv. So |Δ_iv − m z_iv| ≤ m r Λ < mζ/2, and
   Δ_iv < 0. ∎

This is the brief's idea (1) made exact:
- **Free masses.** Judge-dependent effects are produced by free masses on both sides of several boundary points, with
  signs λ_j of either sign.
- **What the adversary achieves.** The adversary reaches every direction in the span of the common essential values, to
  first order.
- **Equivalence with alignment.** By Gordan's alternative, Proposition 4.1 applies exactly when the alignment of
  Theorem 3.1 fails. So Theorem 3.1 and Proposition 4.1 are two faces of one statement:

  **(QS) at p ⟹ for every branch F, ⟨N(C_p)_F⟩ ∩ ℝ^F_{<0} = ∅; and if this intersection is nonempty, an explicit swap
  record defeats F.**

**Corollary 4.2 (generic judges fail at T1; PROVED).** Let T1 = C_{p*}, on the full domain or on a decomposable domain with
(LF) at T1. Suppose that for some branch F at p*, the accept/silence switch values c_F(g) at points g ∈ ∂D_{T1}∖{0} where
the switch map is approximately continuous span a subspace of ℝ^F that contains a strictly negative vector. This holds in
particular if they span ℝ^F. Then (QS) fails at p*, so no family through T1 satisfies (QS) with these judges.

*Proof.* Such values are common essential values (§1). Apply Proposition 4.1. ∎

**CHECKED (`generic_t1.out`).** The setting is ε = 3/10, with twelve judges c_iv(g) = g_i(1 + A_iv g_1² + B_iv g_2² +
C_iv g_3²) and twelve different rational coefficient triples. Twelve rational relative-interior facet points of T1 are
used, four per facet, all off the coordinate planes.
- All 216 branches have rank-6 switch matrices.
- For each branch, an explicit λ with Σλ_j c_F(g^j) = −𝟙 was computed and verified exactly.

So these smooth, heterogeneous, strictly guiding judges cannot carry T1 in any (QS) family.

**Proposition 4.3 (exhaustion of local swaps; PROVED).** Let w ≥ 0 on F, and let O be a measurable set of problems.
Suppose that for a.e. h ∈ O and every b ∈ A(h) ∖ {a_C(h)}:

  Σ_{(i,v)∈F} w_iv [ℓ_iv(h,b) − ℓ_iv(h, a_C(h))] > 0   (strict branch-Bayes on O).

Then no record X ≠ C supported in O has Δ_F(X) ≤ 0.

*Proof.* w·Δ_F(X) is the integral, over the non-null change set, of a strictly positive function. So it is positive, and
some coordinate of Δ_F is positive. ∎

So the second-order variation of the judges' densities across a boundary, which the brief hoped the adversary could
exploit, gives nothing once an aligned w_F has strict signs on both sides. For continuous judges this is the generic
situation: w_F·c(h) vanishes on the boundary and changes sign across it. The local method is therefore exhausted by
Theorem 3.1. Any further obstruction must use the *global* family: how ∂C_p moves with p while the judges stay fixed. §6
does this on the edges.

---

## 5. World-separable judges

**Class (WS).** There are an open N ⊇ ∂D_{T1}∖{0}, a function θ : N → (0,∞), and functions φ_iv on ℝ∖{0}, each continuous
on (0,∞) and on (−∞,0) with sgn φ_iv(t) = sgn t, such that:

  c_iv(g) := ℓ_iv(g, silence) − ℓ_iv(g, accept g) = θ(g) φ_iv(g_i)

for every g ∈ N off the coordinate planes, every world i and every judge v. Here "accept g" means advice + on the pair if
g ∈ H, and − if −g ∈ H, and θ is continuous on N.

In words: near T1's boundary, each judge scores accepting a gamble by a function of what that gamble pays at the judge's
own world. A positive factor common to all judges and worlds is allowed. Heterogeneity between judges is unrestricted
within that form. The sign condition is strict guidance.

**Theorem 5.1 (PROVED; algebra CHECKED `t1_separable.out`).** Let the domain be the full domain or decomposable with (LF)
at T1, and let the judges satisfy (WS). Then T1 is not a pointwise weak Bayes model of any nonzero nonnegative combination
Σ w_iv ℓ_iv of the judges. Consequently:
- (WB_F) fails at T1 for every branch F;
- (QS) fails at T1's index, whatever the index;
- no family through T1 satisfies (QS).

*Proof.*
1. **Alignment along the facets.** Let w ≥ 0 be nonzero, and suppose T1 is weakly w-Bayes. Each g ∈ relint F_k off the
   coordinate planes is a continuity point of the switch map c, with accept g on one side and silence on the other, and
   both sides are half-spaces locally. So c(g) ∈ N(T1), and Theorem 3.1's argument, which uses only (WB), gives
   w·c(g) = 0. Dividing by θ(g):

     B_1(g_1) + B_2(g_2) + B_3(g_3) = 0,  B_i(t) := Σ_v w_iv φ_iv(t),   (5.1)

   for every such g. Write B_i^± for B_i on ±(0,∞). They are continuous, with B_i^+ ≥ 0 ≥ B_i^-.
2. **Facet pieces (CHECKED for six values of ε, proved in general below).** On F_k, write h = a r + b r′ with a, b > 0,
   where r, r′ are its two corner rays.
   - On F_1, h_1 = −(a+b) < 0, h_2 = −a + (κ+1)b and h_3 = (κ+1)a − b.
   - The open pieces of relint F_1 off the coordinate planes are the three open convex cones with patterns (−,+,+),
     (−,−,+) and (−,+,−). The pattern (−,−,−) would need (κ+1)b < a and (κ+1)a < b, which is impossible.
   - F_2 and F_3 follow cyclically. Every piece is an open convex cone of the plane v_k^⊥.
   - So on a piece each coordinate ranges over a full open half-line.
3. **Affine on each piece.** By Lemma 5.2 below, on each piece of F_k there are λ (depending on the piece) and constants
   with B_i^{σ_i}(t) = λ (v_k)_i t + b_i on the whole half-line.
   - The three pieces of F_1 all use B_1^-, whose slope λ(c₀+ε) is then common. So F_1 has a single λ_1, and likewise F_2
     and F_3 have λ_2, λ_3.
4. **Slope matching across facets.**
   - B_1^- is used on F_1 with slope λ_1(c₀+ε), and on the piece of F_2 with h_1 < 0 with slope λ_2c₀.
   - B_2^- is used on F_2 with slope λ_2(c₀+ε), and on the piece (−,−,+) of F_1 with slope λ_1c₀.
   - Hence λ_1(c₀+ε) = λ_2c₀ and λ_2(c₀+ε) = λ_1c₀. Multiplying, λ_1λ_2[(c₀+ε)² − c₀²] = 0, so λ_1λ_2 = 0, and then both
     vanish.
   - B_3^- is used on F_3 with slope λ_3(c₀+ε), and on piece (−,+,−) of F_1 with slope λ_1c₀ = 0. So λ_3 = 0.
   - (The script confirms that the full slope system has rank 3.)
5. **Constants.** Every B_i^± is therefore constant, β_i^± say, with β^+ ≥ 0 ≥ β^-. On F_1, the pieces give
   - β_1^- + β_2^+ + β_3^+ = 0;
   - β_1^- + β_2^- + β_3^+ = 0;
   - β_1^- + β_2^+ + β_3^- = 0.

   Subtracting, β_2^+ − β_2^- = 0 and β_3^+ − β_3^- = 0. By the signs, β_2^± = β_3^± = 0, and then β_1^- = 0. The
   pattern (+,−,+) on F_2 gives β_1^+ = 0.
6. **Contradiction.** So B_i ≡ 0 on ℝ∖{0} for every i. Since every φ_iv is strictly signed and w ≥ 0, this forces w = 0. ∎

**Lemma 5.2 (local Pexider; PROVED).** Let Ω be a nonempty open convex subset of the plane P = {x ∈ ℝ³ : v·x = 0}, with
all v_i ≠ 0. Let B_i be continuous on open intervals containing π_i(Ω), with B_1(x_1) + B_2(x_2) + B_3(x_3) = 0 on Ω.
Then there are λ and b_1, b_2, b_3 with Σb_i = 0 and B_i(t) = λv_it + b_i on π_i(Ω).

*Proof.*
1. **Local affinity of B_1.** Let u := (v_2, −v_1, 0) ∈ P. For x ∈ Ω and small t, x + tu ∈ Ω, and
   B_1(x_1 + tv_2) − B_1(x_1) = −[B_2(x_2 − tv_1) − B_2(x_2)].
   - Since v_3 ≠ 0, (x_1, x_2) are coordinates on P, so near a point of Ω they vary independently.
   - The left side therefore does not depend on x_1 locally. Call it D(t).
   - Then D(s+t) = D(s) + D(t) for small s, t, and D is continuous, so D(t) = μt.
   - Hence B_1 is affine near every point of π_1(Ω). This interval is connected, so B_1 is affine on it.
2. **The other two.** The same argument with (0, v_3, −v_2) and (v_3, 0, −v_1) shows that B_2 and B_3 are affine.
3. **Matching.** Write B_i(t) = μ_it + b_i. Then μ·x = −Σb_i on the open set Ω ⊆ P. So μ annihilates the directions of
   P, μ = λv, and then μ·x = 0 on P gives Σb_i = 0. ∎

*Remarks.*
- **What (WS) excludes.** Theorem 5.1 excludes, at once, every (QS) family, every single-field cover through T1, and
  every exchange-rate or quorum design built from (WS) judges.
- **Why the facets force it.** T1's acceptance boundary has three flat facets whose normals differ, and only (ε > 0)
  makes them differ. Separable fields can produce a flat zero set only with one slope ratio per world, and the facets
  demand two incompatible ratios.
- **Which hypotheses are used.** The proof uses no continuity of the selection, no edge or vertex information, and no
  (IB), (TC) or closed sections. It uses neither n nor q.
- **An extension, recorded as CONJECTURE 5.3.** The same conclusion holds for D_K with any non-singleton polygonal K in
  the interior of Δ. The slope matching uses only two facets sharing a negative half-line with different normal
  coordinates.

---

## 6. Vertices and edges: the boundaries sweep, the judges do not move

Throughout this section the domain is the **full** four-advice domain. Write W_i for the world-i-perfect model: on the
pair of g it accepts the orientation that is positive at world i.

**Lemma 6.1 (vertices; PROVED).** If (QS) holds at e_i, then C_{e_i} = W_i = D_{{e_i}} a.e. In particular, the vertex
condition of BRIEF33 idea (3) is satisfied by the world-optimal model and only by it.

*Proof.*
- **Only W_i.** If C ≠ W_i on a non-null set, then X = W_i is a pointwise world-i improvement there, strict on that set.
  So every world-i judge has Δ_iv(e_i, X) < 0, and no judge strictly prefers C. So (QS) fails.
- **W_i passes.** Every X ≠ W_i is a strict world-i worsening on its change set, so all n judges have Δ > 0.
- **Identification.** W_i = D_{{e_i}} a.e. is immediate. ∎

**Lemma 6.2 (edge confinement; PROVED).** If p lies in the open edge (e_i, e_j) and (QS) holds at p, then C_p = D_{K_p}
with K_p ⊆ Δ_ij := co{e_i, e_j}.

*Proof.*
1. **Two-positive gambles are accepted.** Let E be the set of g with g_i, g_j > 0 on which C_p does not accept g (alone).
   If E is non-null, let X be C_p with "accept g" on E. At worlds i and j this is the strictly best advice. So every judge
   at both active worlds has Δ < 0, and (QS) fails.
2. **Confinement.** So D_{K_p} accepts a.e. g with g_i, g_j > 0. If some m ∈ K_p had m_k > 0, the gambles near
   (t, t, −N) (in coordinates (i, j, k)) with N > t(m_i + m_j)/m_k would have P_{K_p} < 0 on an open set, a
   contradiction. ∎

**Lemma 6.3 (ratio monotonicity; PROVED; CHECKED `edge_ratio.out`).** Let a_v, a′_v > 0 (v ∈ F_i) and b_u, b′_u > 0
(u ∈ F_j) satisfy a′_v/b′_u > a_v/b_u for all v, u. Let w ≥ 0 have nonzero restrictions to F_i and to F_j. Put
A := Σ w_v a_v, B := Σ w_u b_u, and A′, B′ likewise. Then A′/B′ > A/B.

*Proof.* Put λ_u := b′_u/b_u and Λ := max{λ_u : w_u > 0}.
- The hypothesis gives a′_v > λ_u a_v for every u, so a′_v > Λ a_v. Hence A′ > ΛA, strictly, since some w_v > 0.
- Also B′ = Σ w_uλ_u b_u ≤ ΛB.
- So A′/B′ > ΛA/(ΛB) = A/B. ∎

**Theorem 6.4 (edge identities; PROVED).** Let p ↦ C_p be a coherent selection, continuous in measure on the closed edge
[e_i, e_j], with (QS) at every point of that edge. Write coordinates (i, j, k).

(a) **The sweep.**
- K_p = {(1−x)e_i + xe_j : x ∈ [α_p, β_p]}, where α_p ≤ β_p depend continuously on p.
- β = α = 0 at e_i, and β = α = 1 at e_j.
- Hence for every s ∈ (0,1) some p_s in the open edge has β_{p_s} = s.

(b) **The boundary plane.** For g with g_i > 0 > g_j:
- P_{K_p}(g) = (1−β_p)g_i + β_p g_j and P̄_{K_p}(g) = (1−α_p)g_i + α_p g_j. Neither depends on g_k.
- So C_{p_s} accepts g iff (1−s)g_i + s g_j > 0. Its acceptance boundary in Q_ij := {g_i > 0 > g_j, g_k ≠ 0} is the
  half-plane Π_s := {(1−s)g_i + s g_j = 0} ∩ Q_ij, which contains every value of the off-edge payoff g_k.
- Across Π_s the advice changes from "accept g" to silence if α_{p_s} < s, and to "accept −g" if α_{p_s} = s.
- Let τ_s denote the corresponding switch map: c(g) = ℓ(g, silence) − ℓ(g, accept g), or
  d(g) = ℓ(g, accept −g) − ℓ(g, accept g).

(c) **The identities.** Let N ⊆ Q_ij be the null set where c or d fails to be approximately continuous, and write τ(g) for
the approximate value. For a.e. s ∈ (0,1), the slice N ∩ Π_s is null for 2-dimensional measure. For every branch
(F_i, F_j) at p_s there is a weight w ≥ 0, with nonzero restrictions to F_i and to F_j, such that

  Σ_{v∈F_i} w_iv |τ_{s,iv}(g)| = Σ_{u∈F_j} w_ju |τ_{s,ju}(g)|  for every g ∈ Π_s ∖ N.   (6.1)

*Proof.*
1. **Continuity of K_p.** The map K ↦ D_K is continuous from credal sets (Hausdorff metric) to models (measure metric),
   by LL1 Lemma 4.2a, and it is injective (write-up §2). Credal sets form a compact space, so the map is a homeomorphism
   onto its image. Hence p ↦ K_p is Hausdorff-continuous, and so are α_p and β_p (the extreme x-coordinates).
2. **Endpoints.** Lemma 6.2 gives K_p ⊆ Δ_ij in the open edge. Lemma 6.1 and injectivity give K_{e_i} = {e_i} and
   K_{e_j} = {e_j}. The intermediate value theorem then gives (a).
3. **(b).** m·g = (1−x)g_i + xg_j decreases in x when g_i > 0 > g_j. Its minimum is at x = β and its maximum at x = α.
   Near a point g ∈ Π_s with g_i > 0, the other plane {(1−α)g_i + αg_j = 0} (if α < s) is at positive distance. So
   locally the model is "accept g" on one open half-space and τ_s's alternative on the other.
4. **Slices.** The map (s, g_i, g_k) ↦ (g_i, −(1−s)g_i/s, g_k) is a diffeomorphism of (0,1) × (0,∞) × (ℝ∖0) onto Q_ij,
   with nonvanishing Jacobian. N is null, so by Fubini a.e. slice N ∩ Π_s is 2-null.
5. **Identities.** At g ∈ Π_s ∖ N, τ_s(g) is a common essential value of C_{p_s} (§1). Theorem 3.1 at p_s gives
   w·τ_s(g)_F = 0.
   - At world i, g_i > 0, so "accept g" is the best advice, and τ_{s,iv}(g) > 0.
   - At world j, the alternative is better, and τ_{s,ju}(g) < 0.
   - This is (6.1).
   - If w vanished on F_i (or on F_j), (6.1) would force w = 0. ∎

**Reading.** Each plane Π_s carries every value of the off-edge payoff g_k, and world k's judges are absent. So for
almost every s and every one of the 36 branches, some nonnegative mixture of the branch's world-i judges equals some
nonnegative mixture of its world-j judges along the whole plane, as functions of two variables. The planes are fixed by
the geometry of the simplex, not by the designer: whatever the selection, its edge boundaries are exactly these planes.
So (6.1) is a **selection-independent** necessary condition on the judges, for a.e. s and with the switch type τ_s ∈ {c, d}.
The designer can choose the type, but must choose one per plane.

**Corollary 6.5 (PROVED).** Suppose that for some edge {i,j} there is an open set U ⊆ Q_ij on which c and d are
continuous, and on which, for each τ ∈ {c, d} and all v ∈ J_i, u ∈ J_j, the ratio |τ_iv(g)|/|τ_ju(g)| is strictly
increasing in g_k (with g_i, g_j fixed). Then no coherent selection that is continuous in measure on Δ satisfies (QS)
everywhere on the full domain. This holds whether or not the family passes through T1.

*Proof.*
1. **Planes meeting U.** For s in a nonempty open interval, Π_s ∩ U is a nonempty open subset of Π_s.
2. **Two points on one line.** Pick such an s at which (6.1) holds (a.e. s qualifies), and two points g, g′ of Π_s ∩ U
   on one line parallel to the g_k-axis, with g_k < g′_k. By continuity N ∩ U = ∅.
3. **Contradiction.** By Lemma 6.3 the ratio of the two sides of (6.1) is strictly larger at g′ than at g, so it cannot
   equal 1 at both. ∎

An instance: world-i judges whose switch magnitudes do not depend on g_k near U, while every world-j judge's magnitude
strictly decreases in g_k there. In words, one world's judges discount accuracy when the third world's stake grows, and
the other's do not.

*Remark.* §6 needs the full domain for three things:
- availability of "accept g" for g_i, g_j > 0 (Lemma 6.2);
- the vertex models (Lemma 6.1);
- the switches along Π_s.

On a decomposable domain these hold, for instance, in case (A) of KK3 Theorem 2.4 (two-sided domains). That
extension is not checked here.

---

## 7. The proved reduction: what a (QS) family through T1 must look like

**Theorem 7.1 (PROVED; the union of Lemma 1.1, Theorem 3.1, Lemmas 3.2–3.3, 6.1–6.2, Theorem 6.4, Corollaries 4.2 and
6.5, Theorem 5.1).** Let n = 4 and q = 3 (more generally q ≥ 3), and let the domain be the full domain. Suppose twelve
strictly guiding integrable judges and a coherent selection, continuous in measure and through T1, satisfy (QS).
Then:
- **(R0) Corners and edges.** C_{e_i} = W_i, and on each open edge K_p lies in the edge (Lemmas 6.1–6.2).
- **(R1) Per-branch weights.** For every p and each of the C(4,2)^{|supp p|} branches F, there is w_F(p) ≥ 0, nonzero,
  supported in F, with C_p pointwise weakly w_F(p)-Bayes (Lemma 2.1).
- **(R2) Alignment.** w_F(p) annihilates every common essential switch value at every boundary of C_p. Its support meets
  worlds of both signs of each such value (all three worlds at T1 for judges continuous at one point of each facet piece).
  The common essential values span at most 9 dimensions at full support, and at most 5 on an edge (Theorem 3.1,
  Lemmas 3.2–3.3).
- **(R3) At T1.** For no branch do the facet switch values contain, in their span, a vector strictly negative on the
  branch (Corollary 4.2). In particular the judges are not of class (WS) (Theorem 5.1).
- **(R4) On each edge.** For a.e. s ∈ (0,1) and every branch of the two edge worlds, the identity (6.1) holds along Π_s
  for every value of the off-edge payoff (Theorem 6.4). In particular, the hypothesis of Corollary 6.5 fails on every
  edge.
- **(R5) Exactness.** (R1)–(R4) are necessary only. The exact condition is (NT_F) for every F at every p (Lemma 1.1),
  i.e. the audit's nonstrict test.
  - The gap between (R1)–(R2) and (NT_F) consists exactly of records whose change set lies in the tie set
    {h : w_F·(ℓ(h,b) − ℓ(h,a_{C_p}(h))) = 0} for every admissible certificate w_F.
  - In particular, if each w_F(p) can be taken strictly branch-Bayes off a null set, then (QS) holds at p
    (Proposition 4.3 with O = H; this is the audit's sufficient certificate).

So the surviving configurations are exactly those satisfying (R0)–(R5).
- **Fixed judges.** The judges are fixed. At every p, the switch values on ∂C_p lie in a subspace of codimension ≥ 3 whose
  annihilator contains nonnegative vectors inside each of the 216 branches.
- **Edges.** Along every edge plane, the two edge worlds' judges balance identically in the third world's payoff.
- **What a cover needs.** Neither generic smooth judges (Corollary 4.2, CHECKED instance) nor world-separable judges
  (Theorem 5.1) pass. A cover needs judges whose heterogeneity is invisible on every selected boundary, yet large enough
  to escape the single-field barriers (FF2 Thm 4.1, gm).

---

## 8. The global route (BRIEF33 idea (2)), and why it is not available from (QS)

Could (QS) force, for some branch F, a continuous choice of unique-Bayes mixtures, rigid enough for gm or JJ3? I find no
derivation, and I can name where the route breaks.

- **JJ3 Theorem 2.1** (unique, coherent interior Bayes models at every interior weight) comes from KKM applied to a fixed
  ranking whose selection is competitive on every face of *its own* weight simplex.
  - For the six-pseudo-world system of a branch F, the weight simplex is Δ_F. A sub-support σ ⊆ F that omits a judge of
    some F_i would need protection by σ alone.
  - (QS) gives protection only by complete branches (Lemma 1.1). A record with Δ ≤ 0 for every judge of σ but Δ > 0 for an
    omitted judge of F_i is not excluded by (QS). The omitted judge may be the only member of F_i who strictly prefers
    C_p.
  - So the KKM step has no counterpart, and "every Bayes model of every mixture is selected" is **not** derived. This is
    in line with AUDIT_LL and BRIEF33.
- **Lemma 2.1 gives existence of w_F(p) only.** It does not give uniqueness, continuity in p, or a single within-world
  ratio. JJ3 needs (NT) for one fixed field; FF2 Thm 4.1 needs one fixed endorsing field. Neither is available.
- **The remaining global information** is the sweep of boundaries against fixed judges (§6). It is used here only on the
  edges, where the boundaries are forced. In the interior the boundaries ∂C_p are chosen by the designer. The analogue of
  (6.1) at interior p constrains the judges only jointly with the unknown family. Exploiting it (for example near the
  corner rays of T1, where three facets' alignment weights must be compatible) is the natural next step. I have not
  carried it out.

---

## 9. What is used, status, files

| Result | Uses | Does not use |
|---|---|---|
| 1.1 | (QS), \|F_i\| = n−q+1 | everything else |
| 2.1 | Lyapunov (atomless μ, integrable envelopes), decomposability | continuity, coherence, (IB), (TC), closed sections |
| 3.1, 3.2 | (WB_F), the definition of common essential values | continuity of the selection |
| 3.3 | 3.1, q ≥ 3, ≥ 2 active worlds | 3q > 2n |
| 4.1 | atomlessness, decomposability | Lyapunov, separation |
| 4.2 | 4.1, (LF) at T1 | continuity of the selection |
| 5.1 | (WB) at T1 for one mixture, (LF), (WS) | n, q, continuity of the selection, edges |
| 6.1–6.4, 6.5 | (QS) on vertices and edges, coherence, continuity in measure on the edge, full domain | interior p, T1, (IB), (TC), closed sections |

**(IB), (TC), closed sections:** none is used anywhere. Nor is 3q > 2n, nor the absence of ties.

| Item | Statement | Label |
|---|---|---|
| 1.1 | (QS) ⟺ (NT_F) for every branch | PROVED |
| 2.1 | weak Bayes for some nonnegative mixture in every branch | PROVED (η = 0 case of LL2 2.1/8.3) |
| 3.1 | one w_F annihilates all common essential values of all boundaries of C_p | PROVED |
| 3.2 | sign support; all three worlds at T1 for judges continuous at a point of each facet piece | PROVED; patterns CHECKED |
| 3.3 | annihilator dimension ≥ 3 (q ≥ 3); bound tight without signs; ≥ 8 extreme supports at T1 | PROVED; CHECKED (`branch_comb.out`) |
| 4.1 | multi-site swap with free masses defeats (QS) when alignment fails | PROVED |
| 4.2 | generic judges fail at T1; explicit 12-judge instance, all 216 branches | PROVED; CHECKED (`generic_t1.out`) |
| 4.3 | strict branch-Bayes defeats every local record (exhaustion of idea (1)) | PROVED |
| 5.1, 5.2 | world-separable judges: T1 is weak Bayes for no mixture; (QS) fails through T1 | PROVED; CHECKED (`t1_separable.out`, six ε) |
| 5.3 | same for every non-singleton polygonal interior K | CONJECTURE |
| 6.1, 6.2 | vertex models; edge confinement | PROVED |
| 6.3 | ratio monotonicity | PROVED; CHECKED (`edge_ratio.out`) |
| 6.4 | edge sweep; selection-independent identities (6.1) on a.e. plane Π_s | PROVED (full domain) |
| 6.5 | monotone off-edge ratios ⇒ no continuous (QS) family at all | PROVED |
| 7.1 | surviving configurations (R0)–(R5) | PROVED (reduction) |
| — | (QS) fails for every configuration | **open** |

**Files (`mm2py/`).**
- `t1_separable.py` → `t1_separable.out`: facet pieces and sign patterns of ∂D_{T1}, the slope-matching system (rank 3)
  and the constant system, for ε ∈ {1/100, 1/10, 3/10, 1/2, 9/10, 99/100}.
- `branch_comb.py` → `branch_comb.out`: Lemma 3.3 combinatorics.
  - No support lies in all 216 branches.
  - Every pair of supports (885 115 pairs) is avoided by some branch.
  - Three singletons cover all branches.
  - Full-world supports cover at most 27 branches each; the 27 transversals cover all.
  - Greedy search is a diagnostic only.
- `generic_t1.py` → `generic_t1.out`: rank-6 switch matrices for all 216 branches at twelve facet points (ε = 3/10),
  with exact defeating combinations.
- `edge_ratio.py` → `edge_ratio.out`: segment previsions on an edge, and 20 000 exact instances of Lemma 6.3.
