# VER86: verification of the fixed countable-list argument (GUIDANCE86 §10)

29 October 2026. Verifier VER86. Sources: GUIDANCE86.md, AUDIT_fixed_countable.md, app_long.tex (Lemmas lem:states, lem:DQ, lem:identify, lem:hull, lem:guidedeverywhere, lem:contraction, lem:trim), ldg_short.tex (Lemma lem:kkm, Theorem thm:local, Definitions). I re-derived every step myself and did not rely on the audit's or R85b's verdicts.

Orientation used here: application convention Y ⪰_ω X ("Y at least as good as X"), which corresponds to LDG's Y ⪯_ω X. A = Y∖X is added and B = X∖Y is removed.

## Summary

| # | Item | Verdict |
|---|------|---------|
| 1 | Finite-inequality approximation, strict margins, P = S | OK |
| 2 | Homothetic neighbourhood and trimming | OK (one remark on the "technical correction") |
| 3 | Positive-gap lemma, both cases, dominated differentiation | OK |
| 4 | Hull-inclusion chain in §7 Step 2 | OK |
| 5 | Closedness of K_ω(X) | OK |
| 6 | Order of quantifiers | OK (two drafting points) |
| 7 | Finite-intersection step and universal tie clause | OK |
| 8 | U_L = C_L versus coherent undominated dominator | OK (one drafting point) |
| 9 | Identification of almost coherence | OK (wording fix in §7 Step 4) |
| 10 | Measure-existence lemma and infinite-world limits | OK |

There is no GAP or ERROR in the mathematics. The finite-world case is not needed as a fallback. The drafting points below are things the writers must state explicitly. None of them is a hole in the argument.

---

## 1. Finite-inequality approximation: OK

**Countability.** A listed set is fixed by a finite list of pairs (k_i, a_i) ∈ ℕ × ℚ, and only nonempty sets are kept. So the list is countable, and it depends only on E and (h_k). Each P_j is weak-* closed in S (an intersection of closed half-spaces), so it is compact and convex.

**Separation.** Let Q be a nonempty compact convex subset of S and q′ ∈ S∖Q. The continuous linear functionals on (E*, weak-*) are exactly the evaluations at h ∈ E. Strict Hahn–Banach separation of the compact convex set {q′} from the closed convex set Q gives h ∈ E with q′(h) < min_Q q(h). The minimum is attained because Q is compact. Let ε be the gap between these two values. Every state has norm 1, so |q(h) − q(h_k)| ≤ ‖h − h_k‖ uniformly on S. Choose h_k with ‖h − h_k‖ < ε/3. Then q′(h_k) < min_Q q(h_k), with a gap greater than ε/3, and there is a rational a strictly between them. The open set {q(h_k) < a} contains q′. The closed half-space {q(h_k) ≥ a} contains Q with **strict uniform margin** min_Q q(h_k) − a > 0.

**Finite list.** S∖U is compact, so finitely many such open sets cover it. The intersection P of the corresponding half-spaces is a listed set. P is nonempty because it contains Q. P ⊆ U, and every displayed inequality has a strict margin on Q. If U = S, the empty list gives P = S, and the margin requirement holds vacuously. **The case P = S is handled.**

**Decreasing sequence.** S is metrizable (Lemma lem:states(a)). Put U_n = {d(·,Q) < 1/n}. Then ⋂U_n = Q because Q is closed. Take P′_n ⊆ U_n as above and P_n := P′_1 ∩ … ∩ P′_n (concatenated lists). Each P_n is listed, decreasing, contains Q, and keeps strict margins on Q, and ⋂P_n = Q.

**Convergence.** If P_Q(g) > 0 but infinitely many P_n contain some q_n with q_n(g) ≤ 0, take a convergent subsequence q_n → q. Then q ∈ P_m for every m, so q ∈ Q, and q(g) ≤ 0. This is a contradiction. Hence D°_Q ⊆ ⋃_n D_{P_n}, and D_{P_n} ⊆ D_{P_{n+1}} ⊆ D_Q. So D_Q∖D_{P_n} ⊆ {P_Q = 0} ∪ (D°_Q∖D_{P_n}). The first set is null by (M2), and the second decreases to ∅. By (M1) and dominated convergence, ∫_{D_Q∖D_{P_n}} ‖g‖ dμ → 0.

## 2. Homothetic neighbourhood: OK

Let the listed P have inequalities q(h_i) ≥ a_i with margins c_i := min_Q q(h_i) − a_i > 0. For q ∈ Q and s ∈ S:

((1−λ)q + λs)(h_i) − a_i ≥ (1−λ)(a_i + c_i) − λ‖h_i‖ − a_i = c_i − λ(min_Q q(h_i) + ‖h_i‖) ≥ c_i − 2λ‖h_i‖.

So λ := min(1/2, min_i c_i/(1 + 2‖h_i‖)) ∈ (0,1) works uniformly over S. For P = S, any λ ∈ (0,1) works.

Then P_P ≤ P_{(1−λ)Q+λS} (the minimum is over a larger set), so D_P ⊆ D_{(1−λ)Q+λS}. Lemma lem:trim with X := Z, τ := λ and N := D_P gives Q_{Z∖D_P} = Q_Z.

I re-checked lem:trim and lem:contraction line by line. The null set where q(h) < −aP(h) does not depend on q′, so Ψ maps Q_X into Q_X. Also Ψ^k(q′) − q = (a/(1+a))^k (q′ − q), and Q_X is closed. Both are correct.

**Remark on the "technical correction" (GUIDANCE §6).** It is true that Q ⊆ int_S P does not give a positive margin for every displayed inequality: the inequality q(𝟙) ≥ 1 is tight on all of S. But Q ⊆ int_S P **does** give the homothetic inclusion, by the tube lemma. The map (q, s, λ) ↦ (1−λ)q + λs is continuous on Q × S × [0,1]. The preimage of int_S P is open and contains Q × S × {0}, and Q × S is compact. So the margin argument is sufficient but not necessary. The manuscript should not claim that interior containment is insufficient for the homothety. Either proof may be used; the margin proof is more elementary.

## 3. Positive-gap lemma: OK

Throughout, q(m(Y)) = ∫_Y q dμ, because bounded functionals commute with the Bochner integral.

**Consistent case (Z = X, Q = Q_X, G = D_Q).** X ⊆ G a.e. by lem:hull(b), which uses (M2). Hence

φ(q) := ∫_G q⁺ − ∫_X q = ∫_{G∖X} q⁺ + ∫_X q⁻ ≥ 0.

Since μ{q = 0} = 0 by (M2) applied to {q}, φ(q) = 0 forces X = G ∩ {q > 0} a.e. That set is a.e. equal to D_Q ∩ D_{{q}} = D_{conv(Q∪{q})}, which would make X almost coherent. So φ > 0 on S. φ is continuous: q_n → q weak-* gives q_n(g)⁺ → q(g)⁺ pointwise, with domination by ‖g‖ ∈ L¹ from (M1). Metrizability makes sequential continuity enough. Compactness of S then gives γ = min φ > 0.

**Inconsistent case.** h(q) = −∫_X q⁻ is continuous (as above) and negative, since h(q) = 0 iff q ∈ Q_X = ∅. Take a maximiser q₀. Put d = −h(q₀), Z = X ∩ {q₀ > 0} and L = X ∩ {q₀ ≤ 0}. Then q₀ ∈ Q_Z, so Z is consistent.

*Differentiation.* Fix ω and put q_t = (1−t)q₀ + tδ_ω ∈ S for t ∈ (0,1]. The difference quotients [min(q_t(g),0) − min(q₀(g),0)]/t are bounded by |g(ω) − q₀(g)| ≤ 2‖g‖, because min(·,0) is 1-Lipschitz. They converge to (g(ω) − q₀(g))·1_{q₀<0}(g) for every g ∉ {q₀ = 0}. On {q₀ = 0} the limit is min(g(ω),0), which is different, but that set is null by (M2), and it is **one null set, independent of ω**. Dominated convergence along any sequence t_n ↓ 0 gives the right derivative m(L)(ω) − q₀(m(L)), and maximality makes it ≤ 0.

So the argument runs one world at a time and never takes a union of null sets over Ω. It is valid for arbitrary Ω. Finally, q₀(m(L)) = ∫_X min(q₀,0) = −d exactly, so m(L) ≤ −d·𝟙 pointwise.

*Gap.* Z ⊆ G = H(Z) a.e. (M2), so ∫_G q⁺ ≥ ∫_Z q⁺ ≥ q(m(Z)). Also m(X) = m(Z) + m(L), and q(m(L)) ≤ −d by positivity and normalisation. So the gap is ≥ −q(m(L)) ≥ d =: γ.

## 4. Hull-inclusion chain: OK

Each link, with b := b^P_q ⊆ D_P:

- b∖X ⊆ D_P. This holds exactly.
- D_P ⊆ D_Q = G, since Q ⊆ P.
- G = H(Z∖D_P). Trimming (item 2) gives Q_{Z∖D_P} = Q ≠ ∅.
- H(Z∖D_P) ⊆ H(X∖D_P). Z ⊆ X gives Q_{X∖D_P} ⊆ Q_{Z∖D_P} by lem:hull(a). Then H(X∖D_P) is either D of a smaller credal set, hence larger, or E.
- H(X∖D_P) ⊆ H(X∖b), since X∖D_P ⊆ X∖b.

So A = b∖X ⊆ H(B) with B = X∖b, and this holds for every q. The degenerate case X∖b null forces Q = S, P = S and D_P = D_S, which is consistent with the chain.

Gap estimate: q(m(b)) = ∫_{D_P∩{q>0}} q ≥ ∫_{G∩{q>0}} q − ∫_{G∖D_P}‖g‖ = ∫_G q⁺ − e. So q(m(b) − m(X)) ≥ γ − e > γ/2. The estimate uses D_P ⊆ G and |q(g)| ≤ ‖g‖.

## 5. Closedness of K_ω(X): OK

Let q_n → q. For g ∉ {q = 0}, which is null by (M2) applied to the singleton {q}, 1_{q_n>0}(g) → 1_{q>0}(g). This covers every state, including extreme or boundary states such as δ_ω. Then ‖m(b^P_{q_n}) − m(b^P_q)‖ ≤ ∫ |1_{b_n} − 1_b| ‖g‖ dμ → 0 by dominated convergence. That is norm convergence in E, hence convergence at ω. So q ↦ m(b^P_q)(ω) is sequentially continuous on metrizable S, and K_ω(X) is closed.

Support coverage: t_F is weak-* continuous, so A^F_ω := t_F^{-1}(K_ω) is closed. At q = t_F(p), Σ_{ω∈F} p_ω[m(b)(ω) − m(X)(ω)] = q(m(b) − m(X)) > d. So some ω ∈ supp p has a gain > d, which puts t_F(p) in K_ω(X).

Comparison: a gain ≥ d > 0, together with the hull alternative from item 4, gives b ⪰_ω X.

## 6. Order of quantifiers: OK

The order is correct:

1. Fix (h_k), the list (P_j), Θ_j = S, b^j_q = D_{P_j} ∩ {q > 0}, and F(G) = G with t_F. None of these depends on X, on a target or on a dominator.
2. For each X, the following are chosen: Z, Q, γ, then j (from the decreasing sequence, so that e < γ/2 and margins are strict), then K_ω(X) and A^F_ω(X).

Two drafting points:

- **(6a)** The LDG theorem needs F_j(G) to be nonempty. The application must state F(∅) := {ω₀} for a fixed ω₀ (or any fixed singleton). Replacement text: "For nonempty finite G put F(G) := G; put F(∅) := {ω₀} for a fixed world ω₀."
- **(6b)** The LDG statement must require the assigned models b^j_θ to lie in M_L. Otherwise the comparisons are not defined. In the application every measurable model is evaluable, so this holds.

## 7. Finite-intersection step and tie clause: OK

I re-checked the KKM proof in ldg_short (Lemma lem:kkm). Every A_ω is nonempty by coverage at δ_ω. The map G is continuous into Δ_F. At a fixed point p_ω s = d_ω, and coverage at some ω ∈ supp p forces s = 0.

For finite {ω_1, …, ω_k}, take G equal to that set and F ⊇ G. Then ∩_i K_{ω_i} ⊇ t(∩_{ω∈F} A^F_ω) ≠ ∅. So the family K_ω has the finite-intersection property in compact Θ_j, and ⋂_{ω∈Ω} K_ω ≠ ∅. This needs no Hausdorff property. The argument uses **every** finite G, not a sequence of them.

The tie clause is universal over the intersection, as it must be. In the application it holds in a stronger form: at every common point the gain is ≥ d at every world, and there are no ties between distinct classes at any world. So b is not tied with X at any world.

The sufficient condition (assigned models in C_L, and C_L closed under ties) is also correct. A tie at every world would put X in C_L ⊆ C.

## 8. U_L = C_L: OK

(S_σ) and (T_σ) for I = M_L∖C give that every incoherent x ∈ M_L is dominated. Hence U_L ⊆ C, and so U_L = U_L ∩ C = C_L. This uses neither coherent assigned models nor (A). The stronger conclusion, that x has a dominator in C_L, needs the assignments to lie in C_L. The application has this, because every b^j_q is almost coherent and hence undominated.

**(8a) Drafting point.** The partition "permissible = C, irrational = complement of C" does not need (E). Incoherent models are irrational (possibly vacuously) and coherent ones are permissible by (A). (E) only makes the irrationality verdict non-vacuous, that is, it makes every incoherent model dominated under at least one ranking. ldg_short already says this. GUIDANCE §3.4's "Therefore" should not be read as making (E) necessary for the partition.

## 9. Identification of almost coherence: OK

I re-checked lem:identify(a),(b):

- Every ψ ≥ 0 on D is positive.
- Hahn–Banach separation of 0 from the open set int D gives K_D ≠ ∅.
- The bipolar theorem gives cl D = C_{K_D}.
- D°_{K_D} ⊆ int cl D = int D ⊆ D.
- Under (M2), D∖D_{K_D} ⊆ {P_{K_D} = 0} is null.
- D_Q∖D°_Q ⊆ {P_Q = 0}, so under (M2) the class of D_Q is the class of {P_Q > 0}.
- b^j_q = D_{P_j} ∩ {q > 0} is a.e. equal to D_{P_j} ∩ D_{{q}} = D_{conv(P_j∪{q})} (lem:states(c)).

**Wording fix.** b^j_q is in general **not** exactly coherent. It omits gambles g ⪈ 0 with q(g) = 0, so it violates (D2) whenever such gambles exist. GUIDANCE §7 Step 4 ("a coherent undominated dominator") and §1 must say "almost coherent" in the application. Replacement text: "to obtain an almost coherent, undominated model that dominates X". In LDG terms this is correct, provided C is defined as the class of almost coherent models.

## 10. Measure existence and limitations: OK

- μ = Σ w_k Law(f_k + T𝟙) is a Borel probability measure on E.
- (M1): ∫‖g‖ dμ ≤ Σ w_k‖f_k‖ + E|T| < ∞.
- (M2): μ{P_Q = 0} = Σ w_k P(T = −P_Q(f_k)) = 0. Here {P_Q = 0} is Borel because P_Q is 1-Lipschitz.
- Atomless: μ{h} ≤ Σ w_k P(T = h(ω₀) − f_k(ω₀)) = 0.
- Full support: a ball B(h, r) contains f_k + t𝟙 whenever ‖f_k − h‖ < r/2 and |t| < r/2, so μ(B) ≥ w_k P(|T| < r/2) > 0.
- The weights w_k ∝ 2^{-k}/(1 + ‖f_k‖) give Σ w_k‖f_k‖ < ∞.

Only absolute continuity of T and positivity of its law near 0 are used; continuity of the density is not needed.

Limitations: C(Ω) for compact metrizable Ω is separable and contains 𝟙. ℓ^∞(Ω) for infinite Ω is not separable: indicators of subsets of a countably infinite subset of Ω are at mutual distance 1. The new proof never uses full support or atomlessness, so the claim that (M3) is unnecessary is correct.

## Also checked

- **Admissibility (GUIDANCE §5).** Both branches are correct. Hull branch: A is null, so m(B) < 0 everywhere, while q > 0 a.e. on B. Guided branch: lem:guidedeverywhere uses the countable Ω₀ of lem:states(e), so no uncountable union of null sets occurs.
- **Elementary properties.** Strict guidance, independence, no ties between distinct classes, and the three-model and finite-chain conditions all hold.
- **The two LDG examples (§3.5).** One world forces F = {ω}, so each assignment contributes one model per rival. Two constant assignments cover two pairs, but one assignment cannot. Uncountably many pairs defeat any countable list.

No source file was modified.
