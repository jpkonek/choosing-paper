# NN1 (round 42, BRIEF34). Five-of-seven committees: the three-generator escape exists only where a third world absorbs; on every edge the committee collapses to one judge, for every quota with 2q > n

19 Oct 2026. Rules of BRIEF13 and BRIEF34; all scope corrections of AUDIT_MM are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named, with their recorded status.
- **CHECKED**: exact integer or rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: marked as such.

Scripts are in `nn1py/`. Run `python3 -I <script>.py` from inside that folder. Each `.out` ends with `ALL CHECKS PASSED`.
- `median_check.py` → `median_check.out` (exhaustive one-dimensional check of Lemma 2.1 for (n,k) = (4,2), (5,2), (5,3), (7,3); exact random checks in ℝ³ for (7,3));
- `escape_check.py` → `escape_check.out` (Example 5.1: all 42 875 branches, exact).

Setting: the write-up §2, AUDIT_LL, BRIEF34. Three worlds, μ standard Gaussian, T1 = D_K with K = (1−ε)u + εΔ. At each world i there are n = 7 strictly guiding integrable additive judges ℓ_iv (v ∈ J_i, |J_i| = 7), quorum q = 5, blocking size k := n − q + 1 = 3. No assumption is added. Every extra hypothesis is a hypothesis of the result that states it.

---

## 0. Outcome

**No cover of T1 was constructed, and no five-of-seven (QS) family through T1 was found.** What is proved is where the extra freedom of three-judge blocking sets can and cannot act. The answer is sharp.

1. **Two-colour median coincidence (Lemma 2.1, PROVED; CHECKED).** This is the three-generator (indeed k-generator) version of MM1's pair-Helly lemma, in any finite dimension and with no planarity step. Take n positive vectors of each of two colours. Suppose every cone spanned by k vectors of the first colour meets every cone spanned by k vectors of the second colour away from 0, with 2k ≤ n + 1. Then, after normalisation, **n − 2k + 2 vectors of each colour coincide, at one common point**. For (n,q) = (7,5) this is 3 = k: a whole blocking set is proportional, with a common profile in both colours.
   - The brief's proposed structural design, "any 3 of the 7 judges positively span a fixed cone", is a special case (Corollary 2.2). It forces three proportional judges.
2. **Edge collapse (Theorem 3.2, PROVED; any measurable judges, any decomposable domain).**
   - At every edge index p where (QS) holds, every common essential switch value of C_p has opposite signs at the two active worlds.
   - On the set of these values, three world-i judges and three world-j judges are proportional to one common signed function.
   - On the full domain this holds on almost every edge plane Π_s of MM2 Theorem 6.4, whose edge identities are re-derived for branch size 3 (Proposition 3.1).
   - So **on edges the five-of-seven committee acts as a single judge**, plane by plane.
   - This holds for every quota with 2q > n: the coincident set has 2q − n members. It contains a full blocking set exactly when 3q > 2n, that is, exactly under (TC). Enlarging the committee therefore **never** helps on edges.
3. **Interior collapse under a balancing normalisation (Theorem 4.1, PROVED).** At an interior index the alignment condition is "some positive mixture of each branch sums to zero on the boundary over three worlds". Suppose the boundary admits world-wise positive normalisations that can be shifted independently in the two directions θ₁ + θ₂ + θ₃ = 0 (hypothesis (B)). Then again 2q − n judges per world coincide, and the three coincident profiles satisfy one relation: the committee is one field on ∂C_p.
   - **Corollary 4.2 (PROVED).** Cellwise-linear judges on any fan satisfy the shared-parameter form of this. So MM1 Theorem 4.1 holds for five-of-seven with a **tripled** middle ray.
   - **Corollary 4.3 (PROVED).** MM1 Theorem 4.2 also extends verbatim: with judges cellwise linear on the three min-cells near ∂D_{T1}, no coherent selection continuous in measure through T1 satisfies (QS) for five-of-seven.
4. **The escape is real, but only through the third world (Example 5.1, CHECKED; Proposition 5.2, PROVED).**
   - There are 21 pairwise non-proportional vectors, the judges' values at two boundary points with the mixed patterns (+,−,+) and (+,+,−), for which **all 42 875 branches** have a strictly positive exact relation using all three worlds. Every one of the 3 × 1225 two-world branches has none.
   - So three-generator cones can intersect in genuinely varying directions, as BRIEF34 hoped. This happens only when (B) fails: each world's judges must have relative magnitudes that change between the sign-pattern arcs of the boundary.

**Single most important open point.** Can strictly guiding judges realise Example 5.1's slack along every boundary of a continuous coherent family through T1? Hypothesis (B) must fail at every interior index, which means region-dependent relative magnitudes on every boundary ∂C_p. The family must also be glued to edges where the committee is forced to be a single judge plane by plane (Theorem 3.2). The strict sign conditions off the boundaries must hold too. §6 states the realisation problem precisely.

**What the brief asked for, item by item.**
- Branch-supporting mixtures with several independent directions, varying with index and branch: they exist in the finite model (Example 5.1). They are impossible at every edge index (Theorem 3.2), and impossible under (B) (Theorem 4.1).
- Edge identities for branch size 3: re-derived (Proposition 3.1). Their consequence is Theorem 3.2.
- Guidance signs: built into every statement.
- A structural certificate covering all branches: Example 5.1's transversal certificate. Every branch contains a transversal, and every transversal has a positive relation. This is the "Helly in reverse" design. It works with three colours and fails with two (Lemma 2.1).
- (QS) proved for a family: **not achieved.** The lifting lemma is therefore not invoked, and no cover is claimed. Vertices, edges and (LF) are not verified, because there is no construction to verify.

---

## 1. Setting and the exact branch form

Notation is that of MM2 §1.
- Δ_iv(p,X) := L_iv(X) − L_iv(C_p).
- A **branch** at p is F = ⊔_{i∈supp p} F_i with F_i ⊆ J_i and |F_i| = k = 3. There are 35^{|supp p|} branches: 42 875 at full support, 1225 on an edge.

**Lemma 1.1 (PROVED; MM2 Lemma 1.1, whose proof uses only |F_i| = n − q + 1).** (QS) holds at p iff, for every branch F, every evaluable X with Δ_iv(p,X) ≤ 0 for all (i,v) ∈ F equals C_p a.e.

**Common essential values.** The set N(C_p) ⊆ ℝ^{21} and its basic source (approximate-continuity points with both sides of positive upper density) are as in MM2 §1. MM2 Theorem 3.1 is proved there for an arbitrary branch, using only Lemma 2.1 of MM2 (the η = 0 weak-Bayes lemma) and the definition of N. Its conclusion for branch size 3:

**Lemma 1.2 (alignment; PROVED, MM2 Thm 3.1).** If (QS) holds at p, then for every branch F there is w_F ≥ 0, w_F ≠ 0, supported in F, with w_F · y_F = 0 for every y ∈ N(C_p).

Conversely, if for some branch F the span of {y_F : y ∈ N(C_p)} contains a vector that is strictly negative on F, an explicit multi-site swap defeats (QS) (MM2 Prop 4.1, proof independent of branch size).

Alignment is necessary only. The exact condition is Lemma 1.1, the audit's nonstrict test. A strict branch-Bayes weight on a co-null set is sufficient (MM2 Prop 4.3).

---

## 2. Two-colour median coincidence

**Lemma 2.1 (PROVED; CHECKED `median_check.out`).**
- **Setting.** Let V be a finite-dimensional real vector space and ψ ∈ V*. Let a_1, …, a_n and b_1, …, b_n be vectors in V with ψ(a_v) > 0 and ψ(b_u) > 0. Let k ≥ 1 with 2k ≤ n + 1.
- **Hypothesis.** For all k-subsets A, B ⊆ {1,…,n}, cone{a_v : v ∈ A} ∩ cone{b_u : u ∈ B} ≠ {0}.
- **Normalisation.** Put â_v := a_v/ψ(a_v) and b̂_u := b_u/ψ(b_u).
- **Conclusion.** There is z ∈ V with ψ(z) = 1 such that #{v : â_v = z} ≥ n − 2k + 2 and #{u : b̂_u = z} ≥ n − 2k + 2.
  - For a φ ∈ V* that is injective on the finite set {â_v} ∪ {b̂_u}, the sorted positions k, …, n−k+1 of both lists (φ(â_v))_v and (φ(b̂_u))_u are occupied by φ(z).
  - Hence z is unique.

*Proof.*
1. **Separation excludes a branch.** Suppose φ ∈ V* has φ(a_v) > 0 for v ∈ A and φ(b_u) < 0 for u ∈ B. Let x be a nonzero common point, x = Σ_A λ_v a_v = Σ_B μ_u b_u with λ, μ ≥ 0. Since x ≠ 0, neither λ nor μ is zero. Then φ(x) = Σ λ_v φ(a_v) > 0 and φ(x) = Σ μ_u φ(b_u) < 0, a contradiction. So for no branch (A, B) does such a φ exist.
2. **Order statistics.** Fix φ ∈ V* and θ ∈ ℝ. Apply step 1 to φ − θψ. It is positive on â_v iff φ(â_v) > θ, and the same holds for a_v since ψ(a_v) > 0.
   - Let α_1 ≤ … ≤ α_n be the sorted values φ(â_v), and β_1 ≤ … ≤ β_n the sorted values φ(b̂_u).
   - "Some k of the a's exceed θ" means α_{n−k+1} > θ. "Some k of the b's are below θ" means β_k < θ.
   - Step 1 forbids both at once, for every θ. Hence α_{n−k+1} ≤ β_k.
   - Applying this to −φ, whose sorted values are −α_n ≤ … ≤ −α_1, gives β_{n−k+1} ≤ α_k.
3. **Chain.** Since k ≤ n − k + 1:
   α_k ≤ α_{n−k+1} ≤ β_k ≤ β_{n−k+1} ≤ α_k.
   So all these numbers are equal: α_k = … = α_{n−k+1} = β_k = … = β_{n−k+1}.
4. **Coincidence.** Choose φ injective on the finite set {â_v} ∪ {b̂_u}. This is possible: avoid the finitely many hyperplanes {φ : φ(d) = 0} for the nonzero differences d.
   - Equal values at positions k, …, n−k+1 then mean equal vectors. So n − 2k + 2 of the â's equal one vector z, and n − 2k + 2 of the b̂'s equal one vector z′.
   - φ(z) = φ(z′) and injectivity give z′ = z.
   - **Uniqueness when 3k ≤ n + 2 (in particular for (7,3), and for every quota with (TC)).** Suppose a second point z″ ≠ z had multiplicity ≥ n − 2k + 2 among the â's. For an injective φ, its copies carry one value, so they are contiguous in sorted order. They lie entirely below position k or entirely above position n−k+1. Either side has only k − 1 slots, and n − 2k + 2 > k − 1. This is impossible. ∎

*Remarks.*
- **Dimension-free.** Unlike MM1 Lemma 3.1, there is no step "a non-ray intersection forces a common plane". The order-statistic chain works in any dimension. So three-generator cones of **two** colours collapse exactly as two-generator cones did.
- **The CHECKED part.**
  - The one-dimensional form (all k-subset intervals meet ⟺ α_{n−k+1} ≤ β_k and β_{n−k+1} ≤ α_k) and the coincidence were verified exhaustively on value grids for (n,k) = (4,2), (5,2), (5,3), (7,3).
  - In ℝ³, exact random instances for (7,3) were checked. Generic configurations and tripled configurations with distinct rays always fail some branch pair. Tripled configurations with a common ray and two opposite pairs of other points pass all 1225 branch pairs.
- **Quotas.** With k = n − q + 1, the multiplicity is n − 2k + 2 = 2q − n.
  - It is positive iff 2q > n, which is exactly the no-ties condition of LL3 Theorem A.
  - It is at least k iff 3q ≥ 2n + 1, which is exactly (TC).
  - For (4,3) it is 2 (MM1's doubled ray). For (7,5) it is 3. For (5,4) it is 3 > k = 2.

**Corollary 2.2 (fixed-cone designs; PROVED).** Let a_1, …, a_7 ∈ V with ψ(a_v) > 0, and let z ≠ 0 with ψ(z) > 0. Suppose z lies in cone{a_v : v ∈ A} for every 3-subset A. Then at least three of the a_v are positive multiples of z.

*Proof.* Apply Lemma 2.1 with b_u := z for all u. ∎

So "judges arranged so that any 3 of them positively span a fixed cone of trade-offs" is possible only with a proportional blocking set. Then MM1 Proposition 3.2 (in its stated generality: n − q + 1 mutually proportional judges at every world; PROVED modulo FF2 Thm 4.1 imports) excludes the design whenever it is used at every world.

---

## 3. Edges: re-derived identities, and the committee collapses to one judge

**Proposition 3.1 (edge identities for branch size 3; PROVED; MM2 Thm 6.4 re-derived).**
- **Hypotheses.** Use the full four-advice domain. Let p ↦ C_p be a coherent selection, continuous in measure on the closed edge [e_i, e_j], with (QS) at every point of that edge. Use coordinates (i, j, k).
- **Conclusion.** Statements (a) and (b) of MM2 Theorem 6.4 hold verbatim: the sweep, the boundary plane Π_s, and the switch type τ_s ∈ {c, d}. Statement (c) holds as follows. For a.e. s ∈ (0,1), and for every one of the 35² = 1225 branches (F_i, F_j) with |F_i| = |F_j| = 3, there is w ≥ 0 with nonzero restrictions to F_i and to F_j such that
  Σ_{v∈F_i} w_v |τ_{s,iv}(g)| = Σ_{u∈F_j} w_u |τ_{s,ju}(g)| for a.e. g ∈ Π_s.  (3.1)
- **In the precise case** (α_{p_s} = β_{p_s} = s), the same w satisfies (3.1) on both halves Π_s ∩ Q_ij and Π_s ∩ Q_ji.

*Proof.* MM2's proof uses the following, none of which depends on the branch size:
- Lemma 6.2 (edge confinement: every judge at both active worlds strictly prefers accepting two-positive gambles);
- Lemma 6.1 (vertex models);
- Hausdorff continuity of K_p;
- the Fubini slice argument;
- Theorem 3.1 at p_s (here Lemma 1.2).

The only place the branch enters is the existence of w ≥ 0 on F with w·τ_s(g)_F = 0, and Lemma 1.2 supplies it for |F_i| = 3.

For the precise case, at p_s both halves of Π_s are boundaries of C_{p_s}, because the minimum and maximum of m·g over K_{p_s} = {point} coincide. Lemma 1.2 gives one w for all common essential values at once. ∎

**Theorem 3.2 (edge collapse; PROVED; any measurable strictly guiding judges, any decomposable domain).**
- **Hypotheses.** Let p lie in the open edge (e_i, e_j), and let (QS) hold at p for the five-of-seven committee. Suppose N(C_p) ≠ ∅, and write N := N(C_p).
- **Conclusion (a).** Every y ∈ N has opposite signs at the two active worlds: the world-i entries y_iv share a sign s(y), and the world-j entries have sign −s(y).
- **Conclusion (b).** There are:
  - sets Z_i ⊆ J_i and Z_j ⊆ J_j with |Z_i|, |Z_j| ≥ 3;
  - constants λ_v > 0 (v ∈ Z_i ∪ Z_j);
  - a function ζ : N → ℝ∖{0},

  such that
  y_iv = λ_v ζ(y) (v ∈ Z_i),  y_ju = −λ_u ζ(y) (u ∈ Z_j)  for every y ∈ N.
- **In words.** On everything that the boundary of C_p exposes, three world-i judges and three world-j judges are one judge with a fixed exchange rate.

*Proof.*
1. **(a).** By strict guidance every entry y_iv is nonzero and the entries of one world share a sign. If both active worlds had the same sign s at some y ∈ N, then any w ≥ 0 nonzero on a branch F would give w·y_F = s Σ_F w_iv |y_iv| ≠ 0, contradicting Lemma 1.2.
2. **Functions on N.** Put a_v(y) := |y_iv| (v ∈ J_i) and b_u(y) := |y_ju| (u ∈ J_j). These are positive functions on N. By (a), w·y_F = s(y) (Σ_{F_i} w_v a_v(y) − Σ_{F_j} w_u b_u(y)).
3. **Lemma 2.1's hypothesis.** By Lemma 1.2, for every branch (F_i, F_j) some w ≥ 0, w ≠ 0, has Σ_{F_i} w_v a_v = Σ_{F_j} w_u b_u as functions on N.
   - If w vanished on F_j, the left side would be a nonzero sum of positive functions equal to 0, which is impossible. Likewise for F_i.
   - So cone(a_{F_i}) ∩ cone(b_{F_j}) ≠ {0} in the finite-dimensional space V := span{a_v, b_u} ⊆ ℝ^N.
4. **Apply Lemma 2.1.** Use n = 7, k = 3 and ψ := evaluation at a fixed y⁰ ∈ N, which is positive on all a_v, b_u.
   - It gives Z_i, Z_j of size ≥ 3 and z with a_v = a_v(y⁰) z (v ∈ Z_i) and b_u = b_u(y⁰) z (u ∈ Z_j).
   - Put λ_v := a_v(y⁰), λ_u := b_u(y⁰) and ζ := s·z, and use (a) for the signs. ∎

**Corollary 3.3 (planewise single judge; PROVED).** Under the hypotheses of Proposition 3.1, for a.e. s ∈ (0,1) there are Z_i(s), Z_j(s) of size ≥ 3, constants λ_v(s) > 0 and a function ζ_s on Π_s such that, for a.e. g ∈ Π_s ∩ Q_ij (and also on Π_s ∩ Q_ji in the precise case):
- |τ_{s,iv}(g)| = λ_v(s) ζ_s(g) for v ∈ Z_i(s);
- |τ_{s,ju}(g)| = λ_u(s) ζ_s(g) for u ∈ Z_j(s).

*Proof.* Approximate values at the full-measure set of approximate-continuity points of Π_s are common essential values of C_{p_s} (MM2 §1). Apply Theorem 3.2 at p_s, restricted to these values. ∎

*Scope (AUDIT_MM correction 5 respected).*
- The sets Z, the rates λ and the profile ζ may depend on s, and so may the switch type.
- So Corollary 3.3 does **not** identify one field across planes. It says that on each edge plane the edge worlds' judges contain a proportional blocking set with a common profile.
- **Every quota.** The proof uses only 2k ≤ n + 1. For a general q-of-n quota the coincident sets have size 2q − n. They contain a full blocking set iff 3q > 2n.
- **Hence**, for every quota satisfying (TC), each edge branch built from the coincident sets reduces on Π_s to a single pair of judges at one exchange rate. No choice of n or q with (TC) escapes on edges.

---

## 4. Interior: when the third world cannot absorb

Fix an interior p with (QS), and write N := N(C_p).
- For each world i, let V_i ⊆ ℝ^N be the span of the functions x_iv : y ↦ y_iv (v ∈ J_i). Put Σ := V_1 + V_2 + V_3.
- Let R := {(r_1, r_2, r_3) ∈ V_1 × V_2 × V_3 : r_1 + r_2 + r_3 = 0}.
- Since R is the kernel of the sum map, its annihilator is R^⊥ = {(φ|V_1, φ|V_2, φ|V_3) : φ ∈ Σ*} (finite-dimensional linear algebra).

**Hypothesis (B) (balancing normalisations).** There are ψ_i ∈ V_i* with ψ_i(x_iv) > 0 for all v, such that for every θ ∈ ℝ³ with θ_1 + θ_2 + θ_3 = 0, the triple (θ_1ψ_1, θ_2ψ_2, θ_3ψ_3) lies in R^⊥. Equivalently, there are two functionals on Σ that restrict to (ψ_1, −ψ_2, 0) and (0, ψ_2, −ψ_3).

**Theorem 4.1 (PROVED).** Let (QS) hold at an interior p, and suppose (B) holds at C_p. Then:
- at each world i, at least 2q − n = 3 of the normalised functions x̂_iv := x_iv/ψ_i(x_iv) coincide, with a common function z_i;
- z_1 + z_2 + z_3 = 0 on N.

So on N(C_p) the committee contains, at every world, a proportional blocking set, and these three blocking sets form a single aligned field.

*Proof.*
1. **(★) from alignment.** Let u ∈ R^⊥. Some world i has at most k − 1 = 2 judges with u_i(x_iv) > 0.
   - Otherwise choose F_i ⊆ {v : u_i(x_iv) > 0} with |F_i| = 3 at every world, and take w_F from Lemma 1.2.
   - Then (Σ_{F_i} w_v x_iv)_i ∈ R, because Σ_i Σ_{F_i} w_v y_iv = w·y_F = 0 on N.
   - Applying u gives 0 = Σ_{(i,v)∈F} w_iv u_i(x_iv) > 0, a contradiction.
2. **Order statistics.** For u ∈ R^⊥, let m_i(u) be the (n−k+1)-th smallest of u_i(x̂_iv) (the third largest), and l_i(u) the k-th smallest (the third smallest).
   - (★) says min_i m_i(u) ≤ 0.
   - By (B), u + (θ_iψ_i)_i ∈ R^⊥, and m_i(u + θψ) = m_i(u) + θ_i.
   - Take θ_i := M/3 − m_i(u), with M := Σ_j m_j(u). Then (★) gives M ≤ 0, that is, Σ_i m_i(u) ≤ 0 for all u ∈ R^⊥.
   - Applying this to −u gives Σ_i l_i(u) ≥ 0.
   - Since l_i ≤ m_i termwise, l_i(u) = m_i(u) for every i and every u ∈ R^⊥.
3. **Coincidence.** Choose φ ∈ Σ* injective on each finite set {x̂_iv : v ∈ J_i} (avoid finitely many hyperplanes), and put u := (φ|V_i)_i ∈ R^⊥. Then l_i = m_i means positions k, …, n−k+1 carry one vector z_i, with multiplicity ≥ n − 2k + 2 = 2q − n.
4. **The relation.** For such generic u, m_i(u) = u_i(z_i), so Σ_i u_i(z_i) = 0.
   - Generic φ are dense in Σ*, and u ↦ Σ_i u_i(z_i) is linear, so Σ_i u_i(z_i) = 0 on all of R^⊥.
   - Hence (z_i) ∈ R^⊥⊥ = R. ∎

*The edge case is a special case.* At an edge index, (B) holds automatically (with two worlds and θ_i + θ_j = 0): evaluation at one y⁰ ∈ N restricts to s(y⁰)ψ_i on V_i and −s(y⁰)ψ_j on V_j, with ψ = |ev_{y⁰}|. That is Theorem 3.2 again.

**Corollary 4.2 (cellwise-linear judges on any fan; PROVED).**
- **Hypotheses.** These are those of MM1 Theorem 4.1, but for five-of-seven: C = D_K with K ⊆ int Δ two-dimensional, judges cellwise linear on an open cone N ⊇ ∂D_K∖{0}, and C weak Bayes in all 42 875 branches.
- **Conclusion (a).** For each world i, at least three of the vectors κ_iv|_{P(C)} are positively proportional, to a common ray z_i.
- **Conclusion (b).** There are λ ∈ ℝ³_{>0} and d ∈ ℝ^{P(C)}_{>0} with n^Q_i d_Q = λ_i z_i(Q) for all Q ∈ P(C) and all i.

*Proof.*
1. **MM1's steps.** MM1 Theorem 4.1 Steps 1–5 are independent of the branch size. They give, for every branch, a vector d > 0 with d ∈ ∩_i A_i^{−1} cone(κ_{iF_i}|_P), where A_i = diag(n^Q_i)_Q.
2. **Pairs of worlds.** In particular, for every pair of worlds (i, j) and all 3-subsets F_i, F_j, the cones A_i^{−1}cone(κ_{iF_i}|_P) and A_j^{−1}cone(κ_{jF_j}|_P) meet away from 0. Their generators are positive vectors, and ψ := the sum of coordinates is positive on them.
3. **Lemma 2.1 for each pair.** For (1,2) it gives a common normalised point z of multiplicity ≥ 3 in both worlds. For (1,3) it gives z′, the unique median point of world 1 by Lemma 2.1's uniqueness clause. So z′ = z, and similarly for world 3.
4. **Back to the original coordinates.** Undoing A_i, which is diagonal and positive and so preserves positive proportionality, gives (a) with z_i ∝ A_i z. Then d* := z satisfies A_i d* = λ_i z_i, which is (b). ∎

**Corollary 4.3 (min-cell judges, five-of-seven; PROVED, self-contained modulo MM1's written steps).** Suppose every judge is cellwise linear on the three min-cells M_k on some open cone N ⊇ ∂D_{T1}∖{0}, and arbitrary strictly guiding integrable elsewhere. Then no coherent selection, continuous in measure on Δ with T1 = C_{p₀}, satisfies (QS) for the five-of-seven committee.

*Proof.* This is MM1 Theorem 4.2's proof word for word, with Corollary 4.2 in place of MM1 Theorem 4.1.
- Step 1 (classification near T1) uses only weak Bayes in one branch.
- Step 2 uses the tripled ray z_i. It depends on the judges only:
  - all three cells are pinned, and A_i is a positive diagonal bijection, so "three judges with proportional κ_iv" is a property of the judges;
  - by the uniqueness clause of Lemma 2.1 (3k ≤ n + 2), once all branches are weak Bayes at T1, world i has exactly one ray carried by at least three judges;
  - so every nearby C_p uses the same z_i as T1.
- Step 3 is the same linear algebra, so c is unique.
- Step 4 uses Lemma 1.4 of MM1, which is independent of the branch size, and the clopen argument. ∎

So the five-of-seven committee is exactly as rigid as the four-judge committee in every shared-parameter geometry: cellwise linear on any fan, or with fixed per-world cones.

---

## 5. What escapes, and why it needs the third world

**Example 5.1 (CHECKED `escape_check.out`; exact integers).**
- **The setting.** Let N consist of two points A, B. They are the values at two boundary points, with sign patterns A = (+,−,+) and B = (+,+,−); both are mixed. A judge's restriction is a vector (value at A, value at B) ∈ ℝ².
- **World 1:** (10,10), (10,11), (11,10), (10,12), (12,10), (11,12), (12,11). These lie near 45°.
- **World 2:** (−26,7), (−26,8), (−25,7), (−27,7), (−26,6), (−25,8), (−27,6). These lie near 165°.
- **World 3:** (7,−26), (8,−26), (7,−25), (7,−27), (6,−26), (8,−25), (6,−27). These lie near 285°.

The script checks the following, all exactly.
1. **Signs.** Every vector has the strict sign of its world at A and at B (strict guidance).
2. **Non-proportionality.** No two of the 21 vectors are proportional.
3. **Transversals.** For each of the 343 transversals (a, b, c), one vector per world, the identity det(b,c)·a + det(c,a)·b + det(a,b)·c = 0 holds with all three coefficients strictly positive.
   - Every branch (three judges per world) contains a transversal.
   - So **all 42 875 branches** have a strictly positive relation using all three worlds.
4. **Two worlds fail.** For each pair of worlds, all 1225 two-world branches have cones meeting only at 0.

*Reading.*
- The structural certificate is the transversal one. The three world sectors are about 120° apart, so any three vectors, one per world, positively span 0. The supporting mixture changes with the branch, because it uses the branch's own transversal.
- (B) fails here, as it must by Theorem 4.1: no proportional triple exists. The reason is that the A-to-B ratio of each world's judges varies across the judges and is not shared across worlds.
- The two-world failure is Lemma 2.1 in action.

**Proposition 5.2 (necessary features of an escape; PROVED from Theorems 3.2, 4.1 and Corollary 4.2).** Suppose a five-of-seven (QS) family through T1 exists, continuous in measure on Δ. Then:
1. **Edges.** At every edge index with N(C_p) ≠ ∅, the edge worlds contain proportional blocking sets with a common profile on N(C_p) (Theorem 3.2). On the full domain this holds plane by plane on a.e. Π_s (Corollary 3.3).
2. **(B) fails at interior indices.** At every interior index where some world has no three judges proportional on N(C_p), hypothesis (B) fails.
   - In particular, near any interior selected model whose boundary has a pinned cell structure, the judges are not cellwise linear on all pinned cells unless they are tripled there (Corollary 4.2).
   - The judges are not of shared-parameter type (Corollary 2.2).
3. **Region-dependent magnitudes.** For (B) to fail, the world-wise positive functionals available as restrictions of one functional on Σ must not be shiftable independently. In practice:
   - the ratios σ_iv/σ_iv′ restricted to ∂C_p must take different values on different sign-pattern arcs of ∂C_p;
   - they must differ between worlds in an uncorrelated way, as A-to-B ratios do in Example 5.1.
   - Nothing in the axioms requires continuity of σ_iv across the coordinate planes, so the ratios may jump there.

Point 3 is a description of how (B) can fail, not a theorem. Points 1–2 are proved.

*Remark (heterogeneity that the boundary does not see is no escape).*
- **T1 alone.** T1 alone passes (QS) with seven pairwise non-proportional judges per world. Take σ_iv(g) = g_i[a_iv κ*_i(g) + (P_{T1}(g)/|g|) Σ_{j≠i} β_ivj g_j/|g|] with |β| small relative to a, where κ*_i is the canonical min-cell factor (κ*_i = (v_k)_i on M_k).
  - Choosing α with Σ_{F_i} α_iv a_iv = 1 at each world gives Σασ = P_{T1}(g)(1 + E(g)) with |E| < 1.
  - So every branch is strictly certified (MM1 Lemma 1.1(b)). This is PROVED by the displayed identity Σ_i κ*_i g_i = P_{T1}.
- **Why it does not help.** On ∂D_{T1} all seven judges of a world are proportional, so (B) holds there trivially and Theorem 4.1's conclusion is met. This heterogeneity is invisible on the boundary and cannot be transported to a moving family. It is recorded only to separate "heterogeneous judges" from "heterogeneous boundary restrictions"; only the latter can escape.

---

## 6. The precise remaining obstacle

A five-of-seven cover of T1 through the lifting lemma needs strictly guiding integrable judges σ_iv, and a coherent family p ↦ C_p continuous in measure through T1, with the following properties.
- **(E) Edges.** Planewise single-judge behaviour on N(C_p) at every edge index. This is forced (Theorem 3.2) and must be built in, for example by making the switch values in each region {g_ig_j < 0} proportional within a blocking set along every edge plane, with s-dependent rates.
- **(I) Interior.** At every interior p, the restrictions to N(C_p) must violate (B) and satisfy the transversal-type alignment of Example 5.1, with slack. "With slack" means a strictly positive relation for every branch.
- **(S) Strictness.** The aligned mixtures must have the strict signs of Lemma 1.1(a) of MM1 off ∂C_p, or at least pass the exact nonstrict test of Lemma 1.1. Alignment on the boundary alone is not (QS) (AUDIT_LL; MM2 §7 (R5)).
- **(G) Gluing.** (I) must persist as p tends to an edge index, where (B) becomes automatic and the committee collapses (E). The third world's absorption must vanish in a way compatible with Corollary 3.3.

The difficulty is that every point g of the mixed region lies on the boundaries of a one-parameter set of selected models. So the "region-dependent magnitudes" of (I) must be consistent along all of them at once. Meanwhile (E) fixes the judges' structure along the edge planes, which foliate each region {g_ig_j < 0}. I have no construction, and no proof that (E), (I) and (G) are incompatible.

**CONJECTURE 6.1 (offered as the sharpest open alternative).** Either (E) and (I) are compatible along a continuous family, or the edge foliations force (B) at interior indices sufficiently close to every edge. In the second case, Theorem 4.1 and the clopen mechanism of Corollary 4.3 would exclude (QS) for every quota with (TC). I have proved neither.

---

## 7. Cycles, imports, status

**Cycles.** For n = 7, q = 5 the Nakamura number is ⌈7/2⌉ = 4 (LL3 Theorem A, imported). So (TC) holds and strict k-cycles of distinct models are possible for k ≥ 4. No construction was obtained, so none is exhibited.

**Imports.**
- MM2 Lemma 1.1, Lemma 2.1, Theorem 3.1, Proposition 4.1 and Theorem 6.4. Their proofs are independent of branch size, as checked line by line here. MM2 is author-proved and refereed in MM3.
- MM1 Theorems 4.1–4.2 (Steps 1–5 of 4.1; Steps 1, 3, 4 of 4.2) and Lemma 1.4. Also MM1 Proposition 3.2, with FF2 Thm 4.1 imports, used only in the comment after Corollary 2.2.
- The lifting lemma (AUDIT_LL, refereed in MM3) is not used, since no (QS) family is claimed.

| Item | Statement | Label |
|---|---|---|
| 1.1, 1.2 | branch form (35^{\|supp p\|} branches); alignment w_F for branch size 3 | PROVED (imports, size-independent) |
| 2.1 | two-colour median coincidence: n−2k+2 normalised vectors coincide at one common point, any dimension | PROVED; CHECKED (1D exhaustive, 3D exact random) |
| 2.2 | "any 3 of 7 span a fixed direction" ⇒ three proportional judges | PROVED |
| 3.1 | edge identities (3.1) for all 1225 edge branches, a.e. plane; both halves when precise | PROVED |
| 3.2 | edge collapse at every edge index, any domain: opposite signs; 3+3 judges proportional to one profile on N(C_p) | PROVED |
| 3.3 | planewise single judge on a.e. Π_s (full domain); any quota: 2q−n coincide, a blocking set iff (TC) | PROVED |
| 4.1 | under (B): 2q−n coincide per world and the three profiles form one aligned field | PROVED |
| 4.2 | cellwise-linear on any fan: tripled middle ray, common d | PROVED |
| 4.3 | min-cell judges: no five-of-seven (QS) family through T1 | PROVED (MM1 steps) |
| 5.1 | 21 non-proportional vectors; all 42 875 branches strictly aligned; all two-world branches fail | CHECKED (exact) |
| 5.2 | necessary features of an escape | PROVED (items 1–2); item 3 descriptive |
| 5 Remark | T1 alone passes with seven pairwise non-proportional judges per world, invisible on ∂T1 | PROVED |
| 6.1 | (E),(I) compatible, or edges force (B) near the boundary of Δ | CONJECTURE |
| — | five-of-seven (QS) family through T1; cover of T1 | open |
