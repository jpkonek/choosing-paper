# IW66a: referee report on the infinite-world theorem (AUDIT_r66_extension §4) and the contamination cover (§5–6)

26 October 2026. Referee IW66a, working independently of IW66b; I have not read `IW66b_notes.md`. I re-derived every step by hand. Labels: PROVED / CHECKED (exact computation) / NUMERICS / CONJECTURE. Scripts are in `iw66a_py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file.

## Verdict at the top

**The theorem holds as stated.** It does not hold merely after repair. I found no mathematical error in Steps A–E. There are four expository gaps: two in the construction of μ, one in the description of the coherent class, and one in a citation inside Step D. The consequence for the simple safe-improvement ranking also holds as stated: the undominated models are exactly the coherent evaluable models, and every incoherent model is strictly dominated, with a uniform margin. **The contamination cover (§5) is correct** for (LF) read literally as in the binding framework. Its claim to be "the natural analogue" needs to be made precise; see §3 below. **§6 is accurate but incomplete.** One caveat is overcautious, and three scope points are missing.

**The hypotheses actually used:**

| Hypothesis | Where it is used |
|---|---|
| Ω is any nonempty set. E is a sup-norm-closed linear subspace of ℓ∞(Ω), with 1 ∈ E. | Everywhere. 1 ∈ E gives compactness of S, P_Q(h+t1) = P_Q(h)+t, Step C and Step E. |
| E is **separable**. | S is metrizable (Step A: closedness, and a dense sequence in Q_X). Bochner measurability of h ↦ h (Step B). The countable set Ω₀ (Step E). Existence of μ. |
| μ is a **finite** Borel measure on (E, ‖·‖) with **∫‖h‖ dμ < ∞**. | Step B: Bochner integrability and L∞ = (L¹)*. Step C: dominated convergence. |
| **μ{P_Q = 0} = 0** for every nonempty weak-* compact Q ⊆ S. | Step A, with Q = Q_X and Q = Q_B. Step B, with Q = {q}. Strict guidance, with Q = {δ_ω}. Step E, with Q = S. |
| K′ ⊆ S is nonempty, weak-* compact and convex, and U = D_{K′}. | Step C (an element k ∈ K′) and the coherent class. |
| **Full support of μ** | **Not used by the Theorem or by protection.** It is used only to show that the coherent representation D_Q is unique, that coherence on U means K′ ⊆ Q, and for the necessity half of (LF). |

## 0. Verdict table

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| **S1** | S is weak-* compact and metrizable | CORRECT | Positivity together with q(1) = 1 gives ‖q‖ = 1, because −‖h‖1 ≤ h ≤ ‖h‖1. So S is a weak-* closed subset of the unit ball (Banach–Alaoglu). Bounded sets in the dual of a separable space are weak-* metrizable. |
| S2 | inf_{q∈S} q(h) = inf_ω h(ω), and the minimum over S is attained | CORRECT | h − (inf h)1 ≥ 0, so q(h) ≥ inf h. The evaluations δ_ω lie in S. Attainment follows from compactness of S. |
| **S3** | Existence of μ via h = g + t1 | CORRECT, with **GAP (a)** and **GAP (b)** | (a) "Summably weighted atoms" must be read as Σ w_k(1 + ‖g_k‖) < ∞, or the first norm moment can be infinite. (b) Full support of the law of g + t1 is asserted, not argued. Repair: (g,t) ↦ g + t1 is a linear homeomorphism E₀ × ℝ → E, with inverse h ↦ (h − h(ω₀)1, h(ω₀)). A product of full-support measures on separable metric spaces has full support, since ν(V)·λ_t(W) > 0. The first moment holds because ‖g + t1‖ ≤ ‖g‖ + \|t\|. |
| **S4** | Null boundaries for **every** compact Q; whether ν's full support is enough; whether an atomic ν is acceptable | CORRECT | P_Q is 1-Lipschitz, hence Borel. By Fubini and independence, μ{P_Q = 0} = ∫ Prob(t = −P_Q(g)) ν(dg) = 0, because t is atomless. This holds for every nonempty Q ⊆ S, compact or not. Only the conditional law of t given g needs to be atomless. An atomic ν is acceptable: the t-variable makes μ atomless and makes every set {P_Q = 0} null, since such a set meets each line g_k + ℝ1 in exactly one point. Full support of ν is enough for full support of μ, given that t has full support on ℝ. |
| S5 | Measurability of D_Q, P_Q, q(h) and the models | CORRECT | D_Q is norm-open, P_Q is Lipschitz and each q is norm-continuous. Models are Borel sets. Completing μ changes nothing. |
| **S6** | Coherent class "D_Q with K′ ⊆ Q": does it equal "D_Q ⊆ U a.e."? Is Q unique? | CORRECT, **GAP (expository)** | This is not stated in the audit, and it needs full support. The finite Lemma D(c),(d) transfers: (d) an open O ⊆ D_Q a.e. gives O ⊆ D_Q (full support); (c) D_{Q₁} ⊆ D_{Q₂} gives Q₂ ⊆ Q₁, by weak-* separation, whose continuous functionals are the elements of E. |
| **A1** | Q_X is weak-* closed | CORRECT | For fixed h, q ↦ max(−q(h), 0) is weak-* continuous and bounded by ‖h‖, which is integrable. Dominated convergence along sequences suffices because S is metrizable. The finite proof also transfers: X ∩ {q < 0} ⊆ ∪_n X ∩ {q_n < 0}. |
| A2 | P_{Q_X} ≥ 0 a.e. on X, so X ⊆ G = D_{Q_X} a.e. | CORRECT | Q_X is compact and metrizable, hence separable. Off a countable union of null sets, q_j(h) ≥ 0 for all j, and weak-* limits extend this to all of Q_X. Then the null set {P_{Q_X} = 0} is removed. |
| A3 | hull(B) is the smallest coherent model containing B a.e. | CORRECT (needed in §2; not stated) | If B ⊆ D_Q a.e., then Q ⊆ Q_B, so D_{Q_B} ⊆ D_Q. |
| **B1** | {f : 0 ≤ f ≤ 1_G} is weak-* compact and convex in L∞(μ) | CORRECT | μ is finite, so L∞ = (L¹)*. The set is bounded and weak-* closed, as an intersection of the sets {f : ∫fφ ≥ 0} and {f : ∫(1_G − f)φ ≥ 0} for φ ≥ 0 in L¹. |
| **B2** | T is weak-*-to-norm continuous on this set | CORRECT | The identity is Bochner integrable: it is strongly measurable by Pettis, since E is separable, and ∫‖h‖ < ∞. Take simple s_n → id in L¹(μ;E). Each T_n f = Σ_k e_k ∫_{A_k} f dμ has finite rank and is weak-* continuous. Also ‖T f − T_n f‖ ≤ ‖f‖_∞ ‖id − s_n‖_{L¹(E)}, uniformly on the unit ball. A uniform limit of continuous maps is continuous. |
| B3 | Z_G is norm-compact and convex | CORRECT | It is the continuous linear image of a compact convex set. The audit rightly does not claim that the indicator range is convex. |
| **B4** | Minimax: which version, and are its hypotheses met? | CORRECT | Use Sion (1958), or Ky Fan's theorem for bilinear functions. The minimising variable q ranges over S, a compact convex subset of the locally convex space (E*, w*). The maximising variable z ranges over Z_G, a convex subset of (E, ‖·‖). For each z, q ↦ q(z − x) is affine and weak-* continuous; for each q, z ↦ q(z − x) is affine and norm-continuous. Attainment: z ↦ min_S q(z − x) = inf_ω(z − x)(ω) is 1-Lipschitz on the compact set Z_G, and q ↦ max_Z q(z − x) is weak-* lsc, as a supremum of continuous functions, on the compact set S. Joint continuity is true but unnecessary. |
| B5 | For each q the maximiser is unique: f = 1_{G∩{q>0}} | CORRECT | q commutes with the Bochner integral, so q(T f) = ∫ f(h) q(h) dμ. The maximiser equals 1 on G ∩ {q > 0} and 0 on G ∩ {q < 0}. The set {q = 0} = {P_{{q}} = 0} is null. The maximiser is D_{conv(Q_X ∪ {q})}, whose credal set is compact and contains K′. |
| B6 | v ≥ 0, and v = 0 forces X to be coherent, so v > 0 | CORRECT | x = T(1_X) ∈ Z_G because X ⊆ G a.e. If v = 0, then x maximises q\*(·) over Z_G, so 1_X maximises over the relaxed set, and uniqueness gives X = D_{conv(Q_X∪{q\*})} a.e. |
| **B7** | The saddle point gives an indicator, and z\* = m(N₀) | CORRECT | v = min_S q(z\* − x) ≤ q\*(z\* − x) ≤ max_Z q\*(z − x) = v. So z\* maximises q\*(·) over Z_G. Any preimage f\* ∈ T⁻¹(z\*) is a relaxed maximiser, so f\* = 1_{N₀} a.e. by B5, and z\* = m(N₀). Non-injectivity of T is harmless. |
| B8 | m(N₀) − m(X) ≥ v1 pointwise on Ω | CORRECT, and stronger | In fact q(m(N₀) − m(X)) ≥ v for **every state** q, including finitely additive ones. Evaluation at ω commutes with the Bochner integral, so the ω-coordinate is ∫_{N₀} h(ω) dμ − ∫_X h(ω) dμ. |
| **C1** | The shrink: P_{Q_τ} = (1−τ)P_{Q_X} + τ inf h; N_τ ↑ N₀; uniform margin | CORRECT | Q_τ is a weak-* continuous image of the compact set Q_X × S. Since P_{Q_X} ≥ inf h, P_{Q_τ} does not increase in τ. The bound ‖m(N_τ) − m(N₀)‖ ≤ ∫_{N₀∖N_τ} ‖h‖ → 0 along τ_n ↓ 0. |
| C2 | N_τ is coherent and its credal set contains K′ | CORRECT | N_τ = D_{conv(Q_X ∪ {q\*} ∪ Q_τ)}. The convex hull of three compact convex sets is compact. |
| C3 | The gained set is non-null | CORRECT | For k ∈ K′: k(m(N₀) − m(X)) ≥ v > 0, by B8. If N₀∖X were null, the same quantity would equal −∫_{X∖N₀} k(h) dμ ≤ 0. This uses only continuity and linearity of k, not countable additivity. Choose τ with μ(N₀∖N_τ) < μ(N₀∖X). |
| **D1** | The contraction lemma and the convergence of the iteration | CORRECT | Tᵏq′ = q + (c/(1+c))ᵏ(q′ − q). The convergence is in the **dual norm**, at rate 2(c/(1+c))ᵏ, so a fortiori weak-*. Q_X is weak-* closed by A1. |
| D2 | Hull invariance Q_{X∖N_τ} = Q_X | CORRECT, **GAP (expository)** | On X ∩ N_τ, q(h) ≥ inf h > −((1−τ)/τ)P(h), pointwise. On X∖N_τ, q(h) ≥ 0 ≥ −cP(h) a.e. This needs P ≥ 0 a.e. on X (A2), which the audit uses without citing it ("It also holds on the removed part"). Repair: cite Step A. |
| **E1** | A countable norming set Ω₀ | CORRECT | Take a dense sequence (h_j) in E and points ω_{j,n} with h_j(ω_{j,n}) < inf h_j + 1/n. Then inf_{Ω₀} h ≤ inf h + 2‖h − h_j‖ + 1/n. Infima suffice, because E = −E. |
| E2 | Guidance at every world forces the change to be trivial a.e. | CORRECT | Off a null set, every h in the added part A has h > 0 on Ω₀, so inf_Ω h ≥ 0. Removing the null set {P_S = 0} leaves A ⊆ D_S ⊆ D_Q a.e. for every coherent model, since Q ⊆ S. Every h in the removed part B has h ≤ 0, so k(h) ≤ 0 and h ∉ U. Hence B is null. |
| E3 | {P_S = 0} is null | CORRECT | Take Q = S in S4. |
| **T1** | §2 in this setting: a non-null guidance record has a strictly positive increment; (G) | CORRECT | This needs μ{h(ω) = 0} = 0, which is S4 with Q = {δ_ω}. |
| T2 | (TC) and finite-chain consistency | CORRECT | Every accepted non-null record strictly increases m_ω. The null record is guidance, so a.e.-equal models are tied. |
| T3 | (Add) | CORRECT | Guidance is closed under disjoint union. Safety is upward closed under adjoining a disjoint record. Increments add, and a guidance increment is ≥ 0. |
| T4 | Safe ⟺ μ(A ∩ hull(B)) > 0, including B null and Q_B = S | CORRECT | Uses A2 and A3 for B. If B is null, then Q_B = S and hull(B) = D_S. |
| T5 | Protection, dominance, (W), (GC), (C), (ID) | CORRECT | Protection is E2. Dominance: the Theorem gives the record (N∖X, X∖N), which is safe because A ⊆ N ⊆ hull(B). Its increment is ≥ v/2 at every ω. The reverse record has a negative increment and is non-null, so it is not accepted, and dominance is strict. |
| **K1** | The states of C(Ω) are the regular Borel probabilities | CORRECT | Riesz–Markov. On a compact metric space every finite Borel measure is regular. |
| K2 | P_K(h) = (1−ε)p(h) + ε min h | CORRECT | The minimum over a product is the sum of the minima, and min_S q(h) = min h. |
| K3 | Every nonzero boundary gamble has p(h) > 0, including for ε = 1 | CORRECT | 0 = P_K(h) ≤ p(h). If p(h) = 0, then min h = 0 (since ε > 0), so h ≥ 0, and full support with continuity gives h = 0. |
| **K4** | "The natural norm-topological analogue of (LF)" | CORRECT for literal (LF); **GAP (precision)** | The binding framework's (LF), read in the norm topology, holds with N = U. It also holds in the weak topology, because U = {p > 0} is weakly open. But (i) there is **no uniform conic margin** (CHECKED, `contamination_check.out`); (ii) p is **not** in the algebraic relative interior of K once Ω is infinite, so the finite characterization "K′ ⊆ relint K" does **not** transfer. The exact infinite-dimensional characterization is Proposition P1 below. Repair: name the condition met and cite P1. |
| K5 | D_K is undominated | CORRECT | The reason is protection (Step E), since K ⊇ K′ = {p}. It is not the Theorem itself; this is a wording point. |
| K6 | Hence a cover in the transplanted binding framework | CORRECT | (G) and (IB) by T1; (GC), (C), (ID) by T5; D_K ∈ M_U and undominated by K5; (LF) by K4. Conditional only on the transplanted definitions, which this report confirms. |
| **L1** | §6: separability, ℓ∞(Ω) nonseparable, no full-support measure on a nonseparable space | CORRECT | A nonseparable metric space has, for some r, an uncountable family of r-separated points. The disjoint r/2-balls would each need positive mass. |
| L2 | §6: finitely additive states | CORRECT | Example: on the space of convergent sequences, h ↦ lim h is a state that is not countably additive on ℕ. |
| L3 | §6: "non-Archimedean coherent sets are not automatically included" | **Overcautious** | Every coherent set of desirable gambles on E is μ-a.e. equal to some D_Q (P3). So **modulo null sets the coherent class is complete**. |
| L4 | §6: do not import "full-dimensional" | CORRECT | The correct replacement is P1 and P2: "full-dimensional" becomes K_⊥ = {0}, and "relint" becomes "strictly positive on C_K∖{0}". |
| L5 | §6: the measure and the null-set quotient are substantive choices | CORRECT but **incomplete** | See §4: there is no canonical null class, and admissible μ can be mutually singular. Every μ is carried by a meagre set. |
| L6 | Missing from §6 | **GAP** | (i) μ-relativity (§4). (ii) Every K with K_⊥ ≠ {0}, including **every finitely generated K when E is infinite-dimensional**, is uncoverable on one-sided domains (P2(c)). (iii) The hypothesis 1 ∈ E can be weakened to a strictly positive order unit (P4). |

**Score:** 42 items. ERROR: 0. Expository gaps: S3 (two), S6 and D2. Precision or scope repairs: K4, L3, L5 and L6. Every proof step in §4 and §5 is CORRECT.

## 1. Numerical replay with a measure the finite theorem does not cover (NUMERICS)

`iw66a_py/lines_check.py` → `lines_check.out`.

**Setup.** E = ℝ³, ω₀ = world 0, ν = finitely many atoms in E₀, t ~ N(0,1). Then μ lives on lines g_k + ℝ1 and is **singular to Lebesgue measure**. So the refereed finite theorem (μ ~ Lebesgue) does not apply, while the audit hypotheses (null boundaries and a first moment) do. On each line, D_Q is a half-line, so Steps A–D are computable exactly up to floating point.

**Rivals.** 300 random incoherent rivals: half-lines with holes, spikes and empty lines, with K′ a random singleton.

**Results.** All checks pass.

| Check | Result |
|---|---|
| min v | 1.14·10⁻⁴ |
| Saddle identity min_i(m(N₀) − m(X))_i = v | to 8·10⁻⁹ |
| Margin after the shrink | ≥ 0.501 v |
| μ(N_τ∖X) | > 0 in every case |
| Hull invariance: sup-difference of the support functions of Q_{X∖N_τ} and Q_X over 403 directions | ≤ 5·10⁻¹⁵ |

**Control.** Without the shrink (τ = 0), Q_{X∖N₀} ≠ Q_X in 219/300 cases. So the shrink is needed in this singular setting too.

**Consequence.** The infinite-world theorem, specialised to E = ℝⁿ, strictly extends the finite theorem's measure hypothesis.

## 2. Step B and the saddle point, written out (PROVED)

Let F_G = {f ∈ L∞ : 0 ≤ f ≤ 1_G}, Z_G = T(F_G) and x = T(1_X) ∈ Z_G. Put Φ(q, z) = q(z − x) on S × Z_G.

By B4 (Sion), v ≔ max_Z min_S Φ = min_S max_Z Φ, and both are attained, at z\* and q\*. Then

  v = min_S Φ(·, z\*) ≤ Φ(q\*, z\*) ≤ max_Z Φ(q\*, ·) = v.

So z\* ∈ argmax_Z q\*(·). For any f\* with T f\* = z\*, the following holds for all f ∈ F_G:

  ∫ f\* q\*(h) dμ = q\*(z\*) ≥ q\*(T f) = ∫ f q\*(h) dμ.

So f\* maximises f ↦ ∫ f q\*(h) dμ over F_G. Since μ{q\* = 0} = 0, this forces f\* = 1_{G∩{q\*>0}} a.e. Hence z\* = m(N₀), and

  q(m(N₀) − m(X)) ≥ v for every q ∈ S, in particular at every δ_ω.

Nothing here uses Lyapunov, atomlessness beyond the null hyperplanes, or countable additivity of states.

## 3. Local freedom in infinite dimensions: what is met, and what is natural (PROVED)

**Three candidate readings of (LF) at D_K on U = D_{K′}.** Write C_K = {P_K ≥ 0} and K_⊥ = {h : k(h) = 0 for all k ∈ K}.

- **(LF-norm)** There is a norm-open N ⊇ ∂D_K∖{0} such that every measurable X with X △ D_K ⊆ N a.e. lies in U a.e. This is the binding framework's wording.
- **(LF-weak)** The same, with N weakly open.
- **(LF-unif)** There is δ > 0 such that, for every h ∈ ∂D_K∖{0}, the ball B(h, δ‖h‖) lies in U.

In finite dimensions all three coincide, because the unit sphere is compact.

**Proposition P1.** Assume μ satisfies S3 (full support and null boundaries), and let K ⊆ S be compact and convex. The following are equivalent:
1. D_K ∈ M_U and (LF-norm) holds at D_K.
2. K′ ⊆ K, and every k ∈ K′ satisfies k(h) > 0 for all h ∈ C_K∖{0}.
3. K′ ⊆ K, K_⊥ = {0}, and for every k ∈ K′ the normal cone N_K(k) = {g ∈ E : k′(g) ≤ k(g) for all k′ ∈ K} equals ℝ1, that is, it is a linear subspace.

Condition 3 says that K′ lies in the quasi-relative interior of K for the weak-* topology, in the normal-cone form.

*Proof.*
- (2 ⇒ 1). D_K ⊆ D_{K′} = U. Since ∂D_K ⊆ {P_K = 0} ⊆ C_K, condition 2 and the compactness of K′ give ∂D_K∖{0} ⊆ U. Take N = U. Then X ⊆ D_K ∪ U = U.
- (1 ⇒ 2). From D_K ⊆ U a.e., Lemma D(d) (full support) gives D_K ⊆ U, and Lemma D(c) (weak-* separation) gives K′ ⊆ K. Now let k ∈ K′ and h ∈ C_K∖{0} with k(h) = 0. Then 0 ≤ P_K(h) ≤ k(h) = 0. Also h + t1 ∈ D_K for t > 0, so h ∈ ∂D_K∖{0}. Since D_K ∪ N ∈ M_U, we get N ⊆ U a.e., and since N is open, N ⊆ U by full support. Hence h ∈ U, contradicting k(h) = 0.
- (2 ⇔ 3). Take g ∈ N_K(k) and put h ≔ k(g)1 − g. Then h ∈ C_K and k(h) = 0. So condition 2 forces N_K(k) = ℝ1, and any h ∈ K_⊥ has k(±h) = 0 with ±h ∈ C_K, so h = 0. Conversely, let h ∈ C_K with k(h) = 0. Then −h ∈ N_K(k) = ℝ1, so h = c1 with c = k(h) = 0. ∎

**The contamination target in this light** (CHECKED, `contamination_check.out`).
- K_⊥ = {0}.
- N_K(p) = ℝ1: s(g) ≤ p(g) for all s forces max g ≤ p(g), so g is constant by full support.
- So P1 holds, and (LF-norm) holds. (LF-weak) also holds, since U = {p > 0} is weakly open.
- **The finite characterization does not transfer.** p + t(p − k) leaves K for every t > 0 when k = (1−ε)p + εδ_x and p{x} = 0. So p is not in the algebraic relative interior.
- **(LF-unif) fails.** Take the boundary gambles h_η = b_η − (1−ε)p(b_η)1, with b_η a tent of height 1 and width η. Their largest ball inside U has radius p(h_η) = εη/2, which tends to 0 relative to ‖h_η‖.

**Which reading is natural.** (LF-norm) is the right transplant. On E = C(Ω) with Ω infinite, (LF-unif) fails for **every** pair K′ ⊆ K (PROVED). For k ∈ K′, take bumps b at points where k puts little mass, and shift: h = b − P_K(b)1 ∈ ∂D_K. Then P_{K′}(h) ≤ k(b) → 0 while ‖h‖ → 1. A uniform reading would therefore make every target uncoverable. §5 should say: "(LF) in the binding framework's form, with the norm topology (equivalently, here, the weak topology); it holds iff P1(2)".

## 4. Nearby results the audit should state (PROVED unless marked)

**P2: infinite-world universal coverage on U.** Assume S3, with full support. Then the simple safe-improvement ranking on M_U, U = D_{K′}:
- **(a)** covers a compact convex K ⊆ S **iff** P1(2) holds, so it is a **universal cover on U**. The "only if" direction holds for every ranking on M_U, by P1.
- **(b)** Every K with K_⊥ = {0} is covered on some U. Take a weak-* dense sequence (k_j) in K and put k₀ ≔ Σ 2⁻ʲ k_j ∈ K. If h ∈ C_K and k₀(h) = 0, then k_j(h) = 0 for all j, so h ∈ K_⊥ = {0}. Hence K′ = {k₀} satisfies P1(2).
- **(c)** If K_⊥ ≠ {0}, then no ranking covers K on any one-sided domain V. The finite Lemma LF(c) transfers with full support: ±h ∈ ∂D_K∖{0}, and the ball B(h, r) lies in V ∩ (−V) a.e. **If E is infinite-dimensional, this excludes every finitely generated K and every precise target.** The contamination class escapes this exclusion because it contains a copy of the whole of S.

*Proof of (a).* This combines the Theorem, Step E and P1. ∎

This is the exact infinite-world counterpart of the finite Theorem main(e) and the corollaries on universal and every-target coverage: "full-dimensional" becomes K_⊥ = {0}, and "K′ ⊆ relint K" becomes P1(2).

**P3: the coherent class is complete modulo μ.** Let D ⊆ E be a coherent set of desirable gambles: a convex cone with 0 ∉ D that contains every gamble with inf h > 0. Then D = D_Q a.e., where Q ≔ {q ∈ S : q ≥ 0 on D}.

*Proof.*
- D ⊇ D_S, which is open, so int D ≠ ∅.
- Separating 0 from int D shows that the set of φ ∈ E* nonnegative on D is nonzero. Each such φ is positive on E, so φ(1) > 0 when φ ≠ 0, and therefore φ ∈ ℝ₊Q. So Q ≠ ∅.
- By the bipolar theorem, cl D = C_Q. Then int cl D = int D gives D_Q = int C_Q ⊆ D ⊆ C_Q.
- {P_Q = 0} is null. ∎

**Consequence for §6.** The "open versus non-Archimedean" caveat concerns identity, not identity a.e. Under a.e. identification, the theorem's coherent class (with K′ ⊆ Q) is all coherent sets of desirable gambles in M_U.

**P4: constants can be replaced by a strictly positive order unit.** Suppose e ∈ E satisfies e ≥ δ1 for some δ > 0, but 1 need not lie in E. Then h ↦ h/e is an order-isomorphism of E onto a closed separable subspace E′ ∋ 1. Under it:
- the signs h(ω) and h′(ω) agree, so the guidance sets correspond;
- the scores satisfy m_ω = e(ω)·m′_ω;
- null sets, safety and the coherent class are transported.

So the Theorem and the ranking results hold, with margin ≥ δv′. Without some order unit, S is not weak-* compact; for example, on c₀ the weak-* closure of the normalised positive functionals contains 0. So the hypothesis cannot simply be dropped.

**P5: dominance holds at states as well as worlds.** This is B8. The defender's margin is ≥ v/2 at every state, finitely additive or not. Enlarging the set of worlds to S changes nothing.

**Scope point missing from §6: μ-relativity (PROVED).**
- In finite dimensions, the null class was canonical (Lebesgue).
- Here, every finite Borel μ on an infinite-dimensional separable E is tight, so it is carried by a σ-compact set, which is meagre.
- Two admissible measures built from disjoint countable families of lines are **mutually singular**. Their model quotients M_U are then unrelated: a set that is coherent a.e. for μ can be incoherent a.e. for μ′.
- The Theorem holds for every admissible μ, but "incoherent", "undominated" and the ranking itself are relative to μ. A classical fact is relevant: there is no nonzero σ-finite Borel measure on an infinite-dimensional separable Banach space that is quasi-invariant under all translations. So this relativity cannot be removed by a better choice of μ.
- §6 should say this explicitly.

## 5. Attempts to break it

| Attempt | Outcome |
|---|---|
| Non-metrizable S, i.e. E nonseparable, e.g. C(Ω) for non-metrizable compact Ω, or ℓ∞(ℕ) | Outside the hypotheses. No full-support finite measure exists (L1). The Theorem applies to any separable E ∋ 1 even when Ω is wild, e.g. a separable subalgebra of C(βℕ). |
| E without constants | Breaks S-compactness, P_Q(h + t1), Step C and Step E. Repaired by P4 when E has an order unit bounded below. On c₀ there is no fix. |
| ε = 1 (K = S, D_K = D_S) | No failure. K3 and P1 hold. (LF-unif) fails, as it does for every target. |
| p without full support | The Theorem, protection and the undominatedness of D_K all survive. (LF) fails exactly. For ε ∈ (0,1], P1(2) ⟺ supp p = Ω: a bump b ≥ 0 with min b = 0, supported off supp p, lies in ∂D_K∖U. |
| ε = 0 (precise target) | K_⊥ ≠ {0} whenever dim E ≥ 2, so the target is uncoverable on one-sided domains (P2(c)). This is consistent with §5 excluding ε = 0. |
| Atomic ν, μ singular on lines | No failure. NUMERICS in §1. |
| X null; X ⊆ D_S; Q_X = S | Then N ⊆ D_S, and the record (N, ∅) is safe through hull(∅) = D_S. Consistent with the Theorem. |
| Non-compact Q in the definition of coherence | Harmless a.e.: D_Q = D_{cl Q} off {P_{cl Q} = 0}, which is null. |

## 6. Requested repairs (all minor)

1. **§4 measure:** require Σ w_k(1 + ‖g_k‖) < ∞, and add the one-line argument for full support (S3).
2. **§4 setting:** state the coherent-class lemma (K′ ⊆ Q ⟺ D_Q ⊆ U a.e.; Q unique), and note that it and (LF) are the only places where full support is used (S6).
3. **Step D:** cite Step A for P ≥ 0 a.e. on the removed part (D2).
4. **§5:** replace "natural norm-topological analogue" with the precise condition met, (LF-norm) ⟺ P1(2). Note that the finite relint characterization fails and that the uniform reading is unattainable (K4, §3). Attribute "D_K undominated" to Step E.
5. **§6:** soften the non-Archimedean caveat (P3). Add μ-relativity and the exclusion of finitely generated targets in infinite dimensions (P2(c)). Optionally add P2 as the infinite-world universal-coverage statement and P4.

## 7. Files (`iw66a_py/`)

| File | Content |
|---|---|
| `lines_check.py` / `.out` | Steps A–D replayed for μ = law(g + t1), ν atomic (singular to Lebesgue). 300 incoherent rivals; τ = 0 control. NUMERICS. |
| `contamination_check.py` / `.out` | Exact (rational) boundary gambles for K = (1−ε)p + εS on C[0,1]: P_K = 0, p > 0, and no uniform margin. Non-core computation. CHECKED. |
