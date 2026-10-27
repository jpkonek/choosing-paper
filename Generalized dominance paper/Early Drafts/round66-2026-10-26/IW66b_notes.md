# IW66b: referee report on the infinite-world theorem (AUDIT_r66_extension §4) and the contamination cover (§5–6)

26 October 2026. Referee IW66b, working independently of IW66a (I have not read `IW66a_notes.md`). I checked every step by hand. Labels: PROVED / CHECKED (exact computation) / NUMERICS. Scripts are in `iw66b_py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file.

## Verdict at the top

**The theorem of §4 holds as stated.** Steps A–E are correct. I found no mathematical error in §4 or §5. The consequence also holds: in this setting, the simple safe-improvement ranking makes the undominated models exactly the coherent models on U, and it strictly (indeed uniformly) dominates every incoherent model. I re-derived every clause of §2's proof in this setting. Each transfers.

**The contamination cover of §5 holds** for every ε ∈ (0,1], including ε = 1, when p has full support. The (LF) that is met is the literal one: a norm-open neighbourhood N of ∂D_K∖{0}. Here N = U, which is also weakly open. If p lacks full support, (LF) fails on U = {p > 0}, so D_K is not covered there. It is covered on a nearby domain (§6.4).

**The hypotheses that are actually used:**
1. Ω is any nonempty set. E is a closed, separable linear subspace of ℓ^∞(Ω) with the sup norm, and 𝟙 ∈ E. An order unit e (an element with inf_Ω e > 0) is enough; see §7.1. **Without an order unit the ranking conclusion can fail**: there is an explicit counterexample in §7.1.
2. K′ ⊆ S is nonempty, weak-* compact and convex, and U = D_{K′}.
3. μ is a finite Borel measure on E with ∫‖h‖ dμ < ∞.
4. Null boundaries: μ{q(h) = 0} = 0 for each q ∈ S; μ{P_S = 0} = 0; and μ{P_Q = 0} = 0 for every weak-* closed convex Q ⊇ K′. This is implied by the audit's "every nonempty compact Q". **μ{P_S = 0} = 0 is essential for protection.** Without it, pure guidance strictly dominates a coherent model (§4.3).
5. μ has full support. This is used only to identify models: Q is unique, a coherent model lies in U iff K′ ⊆ Q, and (LF) can be characterized. The existence of the defender N (Steps A–D) does not use it.

**Expository gaps that need repair** (none affects the truth of the theorem):
- the infinite-dimensional domain lemma is not stated (§1.5);
- the hull of an arbitrary removed set needs the Step A argument, for the safety test (§3.1);
- the minimax theorem is not named (§2.4);
- atomic ν needs moment-weighted atoms (§1.3);
- "the theorem supplies (LF)" is a wording slip (§6.3);
- §6 omits six scope items (§8).

## 0. Verdict table

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| S1 | S is weak-* compact and metrizable | CORRECT | Banach–Alaoglu; the unit ball of E* is weak-* metrizable because E is separable. Converse (PROVED, §1.1): with 𝟙 ∈ E, S is metrizable **iff** E is separable. |
| S2 | inf_S q(h) = inf_Ω h(ω) | CORRECT | Positivity applied to h − (inf h)𝟙 ∈ E. Moreover S is the weak-* closed convex hull of the evaluations (PROVED, §1.2). |
| S3 | A μ with full support, a finite first moment and null boundaries exists via g + t𝟙 | CORRECT | Fubini on E₀ × ℝ. For null boundaries t needs only an atomless law; for full support, ν and the law of t need full support. A continuous density is unnecessary. **GAP:** "summably weighted atoms" must satisfy Σ w_k‖g_k‖ < ∞. With atomic ν, μ lives on countably many lines g_k + ℝ𝟙. This is legitimate (identification stays injective), but it should be said (§1.3). |
| S4 | Measurability of D_Q, of models and of hull(X) | CORRECT | P_Q is 1-Lipschitz, so D_Q, hull(X), N₀ and N_τ are norm-open. Each {h(ω) > 0} and {q(h) > 0} is open. (q,h) ↦ q(h) is jointly continuous on S × E. The identity map is Bochner integrable. Details in §1.4. |
| S5 | Coherent models on U are exactly the D_Q with K′ ⊆ Q, and Q is unique | **GAP** (unstated) | Needs infinite-dimensional analogues of Lemma D(c),(d): weak-* separation, and full support. Proof supplied in §1.5. |
| A1 | Q_X is weak-* closed | CORRECT | Dominated convergence along sequences (S is metrizable), with dominating function ‖h‖. |
| A2 | X ⊆ D_{Q_X} a.e. | CORRECT | A countable dense subset of Q_X, then the null boundary {P_{Q_X} = 0}. |
| B1 | {0 ≤ f ≤ 1_G} is weak-* compact in L^∞(μ) | CORRECT | μ is finite, so L^∞ = (L¹)*. The set is weak-* closed and bounded. |
| B2 | T is weak-*-to-norm continuous | CORRECT | A uniform limit, on the ball, of finite-rank weak-*-continuous maps. Works for nets. |
| B3 | Z_G is norm compact and convex | CORRECT | Continuous linear image of a compact convex set. |
| B4 | Minimax | CORRECT; GAP (citation) | Sion's theorem (or Ky Fan's) for an affine–affine, separately continuous payoff on two compact convex sets. The payoff is in fact jointly continuous, so both optima are attained. |
| B5 | For each q, the maximizer is unique a.e. | CORRECT | Uses μ{q(h) = 0} = 0, i.e. the null boundary for Q = {q}. |
| B6 | v > 0 | CORRECT | x ∈ Z_G gives v ≥ 0. If v = 0, uniqueness makes X = G ∩ {q* > 0} a.e., which is coherent. |
| B7 | The saddle point is attained by the indicator 1_{N₀} | CORRECT | Every f with T(f) = z* maximizes ∫ f q*(h) dμ, so f = 1_{N₀} a.e. |
| B8 | m(N₀) − m(X) ≥ v𝟙 at every ω ∈ Ω | CORRECT | Evaluate the minimum over S at δ_ω. Evaluation commutes with the Bochner integral. |
| C1 | The shrink keeps a uniform margin | CORRECT | The margin survives because convergence is in **sup norm**: ‖m(N_τ) − m(N₀)‖ ≤ ∫_{N₀∖N_τ}‖h‖ dμ → 0. |
| C2 | N_τ is coherent with credal set ⊇ K′ | CORRECT | Credal set conv(Q_X ∪ {q*} ∪ Q_τ). Its compactness is checked in §2.5. |
| C3 | The gained set is non-null | CORRECT | Apply k ∈ K′. Choosing τ small also preserves μ(N_τ∖X) > 0. |
| D | The contraction lemma | CORRECT | The iterates converge in the **norm** of E*, hence weak-*. Q_X is weak-* closed (A1). |
| E1 | A countable norming set Ω₀ exists | CORRECT | ε-minimizers for a countable dense set; |inf h − inf h′| ≤ ‖h − h′‖. |
| E2 | Pure guidance at every world is trivial, a.e. | CORRECT; **load-bearing hypothesis** | Needs μ{P_S = 0} = 0. Counterexample without it in §4.3. |
| E3 | "§2's ranking proof applies unchanged" | CORRECT | Reflexivity, a.e. ties, strict (G), (IB), (TC), finite-chain consistency, (Add), protection, dominance, (GC), direct (C) and (W) are each re-derived in §3. |
| F1 | Safe ⟺ μ(A ∩ hull(B)) > 0 | CORRECT | Needs A2 for an arbitrary B ⊆ U. The test is the same whether "coherent" means coherent on U or any D_Q (§3.1). |
| F2 | Strict (G) at uncountably many worlds versus null sets | CORRECT | (G) is a requirement at each world separately. Only "guidance at **every** world" needs a countable reduction, which is E1 plus E2. |
| F3 | Is dominance over Ω the same as over Ω₀? | **No, as relations; yes, for the undominated set** | Guidance at every world of Ω₀ equals guidance at every world of Ω, a.e. A safe record positive on Ω₀ need only be nonnegative on Ω. The undominated set is the same for Ω, for Ω₀ and for the compactification Ω̂ (§4.2). |
| G1 | The states of C(Ω) are the regular Borel probabilities | CORRECT | Riesz representation. On a compact metric space every finite Borel measure is regular. |
| G2 | P_K(h) = (1−ε)p(h) + ε min h | CORRECT | Minimum of a sum over a Minkowski sum; min h is attained because Ω is compact and h continuous. |
| G3 | The local-freedom analogue | CORRECT for the literal (LF) with a norm-open N; GAP (wording) | It holds with N = U, also in the weak topology. (LF) ⟺ C_K∖{0} ⊆ D_{K′} ⟺ the normal cone of K at each k′ ∈ K′ consists of constants (§6.2). A **uniform** version, a tube of fixed relative width, fails for every infinite Ω (CHECKED, §6.3). "The theorem supplies (LF)" should read "a direct boundary computation gives (LF)". |
| G4 | D_K is undominated | CORRECT | D_K is coherent, K′ ⊆ K, and Step E applies. This is protection, not the theorem. |
| G5 | Hence a cover in the binding sense | CORRECT | All six clauses of the cover definition, checked in §6.1. |
| G6 | ε = 1 | CORRECT | P_K = min h. The same proof works, since min h = 0 forces h ≥ 0. |
| G7 | p without full support | Not covered on U = {p > 0}: **(LF) fails** (PROVED, §6.4) | The audit does not claim this case. Nearby result (PROVED): for every p and every ε ∈ (0,1], K is covered on U′ = D_{{k′}} with k′ = (1−ε)p + εr, r of full support. |
| G8 | Contamination in a general separable E | Needs "p strictly positive on E₊∖{0}", not "full support" | PROVED, §6.5: (LF) at D_K on {p > 0} holds iff p is strictly positive. Such p always exist in a separable E. |
| H | §6 scope limits | Accurate; GAP (six omissions) | §8 lists the omissions: the order unit; the null set {P_S = 0} as the hidden boundary choice; the Ω̂ representation, which is countably additive; the dependence of the identification on μ; uniform versus literal (LF); the general (LF) characterization. |
| V1 | E without constants | **The theorem fails without an order unit** | (a) A dead world makes every model undominated (PROVED, §7.1). (b) If E has an order unit, the result transfers exactly by a change of numéraire (PROVED). (c) In c₀ a uniform margin is impossible; a pointwise version is OPEN. |
| V2 | Non-metrizable state space | Outside the theorem; the audit is correct | S is non-metrizable iff E is nonseparable, and then no finite full-support Borel measure exists (§7.2). |
| V3 | Ω compact but not metrizable | C(Ω) is outside the theorem; every separable unital E ⊆ C(Ω) is inside | The metrizability of Ω is irrelevant; only that of Ω̂ ⊆ S matters (§7.3). |
| N | Curved-state-space replay | NUMERICS | Ω = [0,1], E = span{1, ω, ω²}, and S curved, with a continuum of extreme points. Steps A–D are replayed on 3 rivals. A uniform margin holds at every ω ∈ [0,1]. Hull invariance holds after the shrink and fails without it, in all 3. See §9. |

---

## 1. The setting

### 1.1 The state space (S1)
- **Positivity forces continuity.** For q positive with q(𝟙) = 1 we have −‖h‖𝟙 ≤ h ≤ ‖h‖𝟙. Hence |q(h)| ≤ ‖h‖ and ‖q‖ = 1.
- **Compactness and metrizability.** S is weak-* closed in the unit ball of E*: positivity and normalization are pointwise conditions. So S is compact (Banach–Alaoglu) and metrizable (E is separable).
- **Converse (PROVED).** The map h ↦ ĥ, with ĥ(s) := s(h), is a linear isometry of E into C(S), since sup_S |q(h)| = ‖h‖. If S is metrizable, then C(S) is separable, and so is E. Hence, given 𝟙 ∈ E, **S is metrizable iff E is separable.** "Non-metrizable state space" and "nonseparable E" are the same case.

### 1.2 The inf identity and the hull of the evaluations (S2)
- The evaluations δ_ω lie in S. So inf_S ≤ inf_Ω.
- Conversely, h − (inf_Ω h)𝟙 ∈ E is pointwise nonnegative. Hence q(h) ≥ inf_Ω h.
- **S = the weak-* closed convex hull of {δ_ω} (PROVED).** Suppose q ∈ S lies outside it. Separation in (E*, weak-*), whose dual is E, gives h with q(h) < c ≤ h(ω) for all ω. Then q(h) < inf_Ω h, which contradicts the inf identity.

### 1.3 The measure (S3)
- **The decomposition.** E = E₀ ⊕ ℝ𝟙 via h ↦ (h − h(ω₀)𝟙, h(ω₀)), a bounded isomorphism. μ is the image of ν ⊗ λ_t under the continuous map (g,t) ↦ g + t𝟙. The Borel σ-algebra of E₀ × ℝ is the product σ-algebra, by separability.
- **Null boundaries.** Take any Q ⊆ S (P_Q is upper semicontinuous, hence Borel). Then {P_Q = 0} = {(g,t) : t = −P_Q(g)}. By Fubini, μ{P_Q = 0} = ∫ λ_t{−P_Q(g)} dν(g) = 0 whenever the law λ_t has no atoms. **A continuous density is not needed**, nor is compactness of Q.
- **Full support.** A ball B(g + t𝟙, r) contains B_{E₀}(g, r/2) + (t − r/2, t + r/2)𝟙. So full support of ν on E₀ and of λ_t on ℝ suffices. "Is ν's full support enough?": yes, together with full support of the law of t.
- **Finite first moment.** ‖g + t𝟙‖ ≤ ‖g‖ + |t|.
- **Atomic ν (GAP).** ν = Σ w_k δ_{g_k} with {g_k} dense in E₀ is acceptable, provided Σ w_k‖g_k‖ < ∞. Take, for example, w_k ∝ 2^{−k}/(1 + ‖g_k‖). "Summably weighted" alone does not give the first moment.
  - μ is then concentrated on the countably many lines L_k = g_k + ℝ𝟙. On each line, D_Q is the half-line {t > −P_Q(g_k)}.
  - The identification of coherent models stays injective: the thresholds determine P_Q on a dense set, hence everywhere, hence Q (§1.5).
  - The null boundaries are carried entirely by t, as the audit says.
  - Models differing only off ∪L_k are identified. This is a substantive modelling choice; it should be stated beside §6's remark on the null-set quotient.

### 1.4 Measurability (S4; question (i))
- **The envelope is Lipschitz.** P_Q(h) = min_{q∈Q} q(h) is 1-Lipschitz in sup norm, because each q has norm 1. So D_Q = {P_Q > 0} is norm-open, hence Borel.
- **The same holds for every set used in the proof.** hull(X) = D_{Q_X}, N₀ = D_{Q_X} ∩ {q* > 0} and N_τ are open. {h(ω) > 0} and {q(h) > 0} are open: h ↦ h(ω) and h ↦ q(h) are continuous linear.
- **Models.** Models are Borel (or μ-measurable) subsets of the open set U, modulo μ-null sets. Nothing more is needed.
- **Joint continuity.** (q,h) ↦ q(h) is jointly continuous on (S, weak-*) × (E, norm): |q(h) − q′(h′)| ≤ |q(h) − q′(h)| + ‖h − h′‖. Both factors are separable and metrizable, so its Borel σ-algebra is the product σ-algebra.
- **Bochner integrability.** E is separable, so the identity map is strongly measurable (Pettis); ∫‖h‖ dμ < ∞ makes it Bochner integrable. Bounded linear functionals commute with the integral. So m(X)(ω) = ∫_X h(ω) dμ and q(m(X)) = ∫_X q(h) dμ.

### 1.5 The domain lemma in infinite dimensions (S5; GAP, PROVED here)
The audit defines coherent models on U as D_Q with K′ ⊆ Q. To match the finite paper, where X is coherent if X = D_Q a.e. for some Q, and to make Q unique, one needs the following.
- **(c∞)** If Q₁, Q₂ ⊆ S are weak-* compact and convex and D_{Q₁} ⊆ D_{Q₂}, then Q₂ ⊆ Q₁.
  *Proof.* Take k ∈ Q₂∖Q₁. Separation in (E*, weak-*) gives g ∈ E and c with q(g) > c > k(g) on Q₁. Put h = g − c𝟙. The minimum over the compact set Q₁ is attained, so P_{Q₁}(h) > 0, while k(h) < 0. So h ∈ D_{Q₁}∖D_{Q₂}.
- **(d∞)** If O is norm-open and O ⊆ D_Q a.e., then O ⊆ D_Q.
  *Proof.* The set O ∩ {P_Q < 0} is open and null, hence empty by full support. For h ∈ O, h − η𝟙 ∈ O for small η > 0, so P_Q(h) ≥ η > 0.
- **Consequences.**
  - D_Q ⊆ U a.e. ⟹ D_Q ⊆ U ⟹ K′ ⊆ Q.
  - D_{Q₁} = D_{Q₂} a.e. ⟹ Q₁ = Q₂.
  - So C_U = {D_Q : K′ ⊆ Q ⊆ S compact convex}, with Q unique.
- **Robustness.** If Q is convex but not closed, then D_Q ∖ D_{cl Q} ⊆ {P_{cl Q} = 0}, which is null. So strict desirability sets with non-closed credal sets add nothing modulo μ.

## 2. Steps A–D

### 2.1 Step A (A1, A2)
- **Closedness.** F(q) := ∫_X max(−q(h), 0) dμ is continuous along weak-* convergent sequences, by dominated convergence with dominating function ‖h‖. Sequences suffice because S is metrizable. So Q_X = F^{−1}(0) is closed. It is convex, and it contains K′ because k(h) > 0 on U ⊇ X.
- **X ⊆ G a.e.** Let {q_j} be dense in Q_X (a compact metric space is separable). For a.e. h ∈ X, q_j(h) ≥ 0 for all j. By weak-* continuity of q ↦ q(h), q(h) ≥ 0 for all q ∈ Q_X. So P_{Q_X} ≥ 0 a.e. on X. Since μ{P_{Q_X} = 0} = 0, X ⊆ G a.e.
- **The same argument applies to any measurable B ⊆ U.** It is needed in §3.1.

### 2.2 Step B: compactness (B1–B3)
- **The relaxed choices are compact.** μ is finite, so L^∞(μ) = L¹(μ)*. The set F_G = {f : 0 ≤ f ≤ 1_G} is weak-* closed: 0 ≤ ∫fφ ≤ ∫_Gφ for every φ ≥ 0 in L¹ forces the bounds a.e. It is also bounded, hence weak-* compact, and convex.
- **T is weak-*-to-norm continuous.**
  - Choose simple φ_n = Σ_i x_i 1_{E_i} with ∫‖h − φ_n‖ dμ < 1/n.
  - T_n(f) = Σ_i x_i ∫_{E_i} f dμ is finite-rank and weak-* continuous, since 1_{E_i} ∈ L¹.
  - ‖T(f) − T_n(f)‖ ≤ ‖f‖_∞ / n.
  - So T is a uniform limit of continuous maps on F_G, hence continuous. This holds for nets, so metrizability of the weak-* topology is not needed (though L¹(μ) is in fact separable).
- **Z_G = T(F_G) is norm compact and convex.** The audit correctly avoids claiming that the range of indicator choices {m(Y)} is convex. In infinite dimensions Lyapunov's theorem fails, and that range need be neither convex nor closed. The proof only needs the maximizers to be indicators.

### 2.3 Step B: maximizers, the value and the saddle point (B5–B8)
- **Uniqueness of the maximizer (B5).** q(T(f)) = ∫ f(h) q(h) dμ ≤ ∫_{G∩{q>0}} q(h) dμ. Equality holds iff f = 1 a.e. on G ∩ {q > 0} and f = 0 a.e. on G ∩ {q < 0}. Since μ{q = 0} = 0, f = 1_{G∩{q>0}} a.e. That set is D_{Q_X ∪ {q}} = D_{conv(Q_X ∪ {q})}, which is coherent; its credal set is compact and contains K′.
- **v > 0 (B6).**
  - 1_X ∈ F_G by A2, so x ∈ Z_G and v ≥ 0.
  - Suppose v = 0. Then min_q max_z q(z − x) = 0 is attained at some q*. So q*(x) ≥ q*(z) for every z ∈ Z_G.
  - Then 1_X is a maximizer, and B5 gives X = G ∩ {q* > 0} a.e. That set is coherent: a contradiction.
- **The saddle point is an indicator (B7).**
  - Let q* attain the outer minimum and z* the outer maximum.
  - Then v = min_q q(z* − x) ≤ q*(z* − x) ≤ max_z q*(z − x) = v. So z* maximizes q* over Z_G.
  - Write z* = T(f*). Then f* maximizes ∫ f q*(h) dμ, so f* = 1_{N₀} a.e. by B5.
  - Hence z* = m(N₀). This is the indicator, not merely a relaxed choice.
- **The margin holds at every world (B8).** For ω ∈ Ω, (m(N₀) − m(X))(ω) = δ_ω(z* − x) ≥ min_S q(z* − x) = v. Evaluation at ω is continuous and linear, so it commutes with the Bochner integral. The inequality is pointwise at **every** ω, with no exceptional set.

### 2.4 The minimax theorem (B4)
- **The payoff.** f(q, z) = q(z − x) on S × Z_G. Both sets are compact convex subsets of locally convex Hausdorff spaces: (E*, weak-*) and (E, norm). f is affine in each variable, and jointly continuous because ‖q‖ = 1.
- **The theorem.** Sion's theorem (Pacific J. Math. 1958) needs only one compact set. Here both are compact, so the inner extrema are semicontinuous and both outer extrema are attained. Ky Fan's minimax theorem would also do.
- **Repair.** The audit should name the theorem it uses.

### 2.5 Step C (C1–C3)
- **The shrunk credal set.** Q_τ = (1−τ)Q_X + τS is weak-* compact (a continuous image of Q_X × S) and convex, and contained in S.
- **Its envelope.** P_{Q_τ} = (1−τ)P + τP_S with P_S(h) = inf_Ω h, by §1.2.
- **N_τ is coherent.** N_τ = D_{conv(Q_X ∪ {q*} ∪ Q_τ)}. The convex hull of finitely many compact convex sets is compact. This credal set contains K′.
- **Monotonicity.** P ≥ P_S, so P_{Q_τ}(h) = P(h) − τ(P(h) − P_S(h)) is non-increasing in τ. For h ∈ N₀ we have P(h) > 0, so h ∈ D_{Q_τ} for small τ. Hence N_τ ↑ N₀ as τ ↓ 0.
- **Convergence.** ‖m(N_τ) − m(N₀)‖ ≤ ∫_{N₀∖N_τ}‖h‖ dμ → 0, by dominated convergence.
- **Why the sup norm matters.** It turns "norm-close" into "uniformly close at uncountably many worlds". Hence inf_Ω(m(N_τ) − m(X)) ≥ v − ‖m(N_τ) − m(N₀)‖ ≥ v/2 for small τ.
- **The gain is non-null.** If N₀∖X were null, then for k ∈ K′, k(m(N₀) − m(X)) = −∫_{X∖N₀} k(h) dμ ≤ 0. But k ∈ S gives k(z* − x) ≥ v > 0. So μ(N₀∖X) > 0, and μ(N₀∖N_τ) → 0 keeps μ(N_τ∖X) > 0.

### 2.6 Step D (D)
- **The contraction.** Suppose q ∈ S and q(h) ≥ −cP(h) a.e. on X. For q′ ∈ Q_X, T(q′) = (q + cq′)/(1+c) ∈ Q_X, because (q + cq′)(h) ≥ q(h) + cP(h) ≥ 0 a.e. on X.
- **The limit.** T^k(q′) − q = (c/(1+c))^k (q′ − q), with ‖q′ − q‖ ≤ 2. So the iterates converge in the norm of E*, hence weak-*. Q_X is weak-* closed and nonempty (it contains K′), so q ∈ Q_X.
- **Hull invariance.** Let c = (1−τ)/τ.
  - On X ∩ N_τ, pointwise: q(h) ≥ inf h > −cP(h).
  - On X∖N_τ, a.e.: q(h) ≥ 0 ≥ −cP(h), using P ≥ 0 a.e. on X (A2). This is the infinite form of the finite referee's d3 point.
  - So Q_{X∖N_τ} = Q_X and hull(X∖N_τ) = hull(X) ⊇ N₀ ⊇ N_τ.
- **The witness mass.** μ((N_τ∖X) ∩ hull(X∖N_τ)) = μ(N_τ∖X) > 0.

## 3. The simple ranking in this setting (E3, F1)

Write φ_ω(X) := m(X)(ω) = ∫_X h(ω) dμ. This is finite, since |h(ω)| ≤ ‖h‖. For a record r = (A,B), d_ω(r) = φ_ω-increment = m(A)(ω) − m(B)(ω).

### 3.1 Safe ⟺ hull test (PROVED in this setting)
- **hull(B) is the smallest coherent model containing B.** For measurable B ⊆ U, Q_B ⊇ K′ is closed and convex (A1), and B ⊆ hull(B) a.e. (A2). If B ⊆ D_Q a.e., then Q ⊆ Q_B, so hull(B) ⊆ D_Q.
- **(⟸)** If μ(A ∩ hull(B)) = 0, then hull(B) is a coherent model that contains B a.e. and misses A a.e. So the record is unsafe.
- **(⟹)** If some D_Q contains B a.e. and misses A a.e., then hull(B) ⊆ D_Q, so A ∩ hull(B) is null.
- **Robustness.** The argument never uses K′ ⊆ Q for the attacked model. So the test is the same whether "coherent" means coherent on U or any D_Q with Q ⊆ S. Hence the reading is immaterial.
- **Edge cases.** For B null, Q_B = S and hull(B) = D_S. Then safe ⟺ μ(A ∩ D_S) > 0, consistent with D_S being contained in every coherent model.

### 3.2 Each clause of the Proposition
1. **Every accepted non-null record strictly raises φ_ω.**
   - Guidance at ω with A ∪ B non-null gives ∫_A h(ω) > 0 or −∫_B h(ω) > 0, with the other term ≥ 0.
   - A safe accepted record has d_ω > 0 by definition.
   - So X ⪯_ω Y implies either X = Y a.e., or φ_ω(X) > φ_ω(Y). The deletion lemma with φ = −φ_ω gives (TC), finite-chain consistency and no nontrivial ties.
2. **Reflexivity, a.e. ties and (IB).** The rule is a function of the record modulo null sets, and the null record is guidance.
3. **Strict (G).** A non-null guidance record r at ω is accepted. Its inverse has d_ω < 0, so it is neither safe-accepted nor guidance (guidance would force d_ω(r⁻¹) > 0).
4. **(Add).**
   - If both records are guidance, so is their union.
   - Otherwise one record, say r₁, is safe, and r₁ ⊔ r₂ is safe: a coherent C attacked by the union is attacked by r₁.
   - d_ω is additive, with d_ω(r₂) ≥ 0, so d_ω(r₁ ⊔ r₂) > 0.
5. **Protection.** r(Y, C) attacks C, so it is unsafe. If it is accepted at every ω, it is guidance at every ω, and then it is null by §4.1.
6. **Dominance.**
   - The theorem gives N with inf_Ω d_ω(r(N,X)) ≥ v/2 > 0 and r(N,X) safe. So N ⪯_ω X at every ω.
   - The reverse record has d_ω < 0. So N ≺_ω X at every ω.
   - Only pointwise positivity of d_ω is needed; uniformity is a bonus.
7. **(GC), direct (C) in the strong form ("tied everywhere with a coherent model ⟹ equal to it") and (W)** follow exactly as in the finite note.

## 4. The binding framework with uncountably many worlds (question (ii))

### 4.1 Step E (E1, E2)
- **A countable norming set exists.** Let {h_k} be dense in E. Choose ω_{k,j} with h_k(ω_{k,j}) < inf h_k + 1/j, and let Ω₀ be the set of all ω_{k,j}. If ‖h − h_k‖ < η, then inf_{Ω₀} h ≤ inf h_k + η ≤ inf h + 2η. So inf_{Ω₀} h = inf_Ω h for all h ∈ E. Applying this to −h gives the same for suprema.
- **Pure guidance at every world is trivial.** Let r = (A,B) be guidance at every ω ∈ Ω₀. Removing countably many null sets:
  - a.e. h ∈ A satisfies inf_Ω h = inf_{Ω₀} h ≥ 0, and, off the null set {P_S = 0}, inf h > 0. Then P_Q(h) ≥ P_S(h) > 0, so h lies in every D_Q.
  - a.e. h ∈ B satisfies sup_Ω h ≤ 0. Then k(h) ≤ 0 for k ∈ K′, so h ∉ U, and B is null.
  - If r attacks a coherent C = D_Q a.e., then A ⊆ C a.e. and A ∩ C is null, so A is null. **So r is null.**

### 4.2 Strict guidance and null sets; Ω versus Ω₀ (F2, F3)
- **Strict guidance needs no countable reduction.** (G) is a requirement at each world separately. The null sets in "A ⊆ {h(ω) > 0} a.e." may depend on ω, and that is harmless: d_ω and the acceptance rule are evaluated world by world. Only "guidance at every world" requires the countable reduction, and §4.1 supplies it.
- **Guidance at every world (PROVED).** A record is guidance at every ω ∈ Ω iff it is guidance at every ω ∈ Ω₀. The proof of §4.1 shows that guidance on Ω₀ forces the record to be a.e. of the form (A, ∅) with inf h > 0 on A, which is guidance at every ω ∈ Ω.
- **Safe records: the relations differ.** d_ω(r) = m(r)(ω) with m(r) ∈ E. Positivity on Ω₀ gives only inf_Ω m(r) ≥ 0, not > 0.
  - For example, in C[0,1] with Ω₀ = ℚ ∩ [0,1], an element such as (ω − 1/√2)² is positive on Ω₀ but vanishes at 1/√2.
  - So weak dominance over Ω₀ is a weaker relation than weak dominance over Ω.
- **The undominated set does not change (PROVED).** Protection uses only Ω₀ (§4.1). The defender's margin is uniform: inf_Ω = inf_{Ω₀} ≥ v/2. So with world set Ω₀ the undominated models are again exactly the coherent models. The same holds with world set Ω̂ (§5): continuity extends the uniform margin to the closure.
- **The answer to (ii).** Dominance over Ω and over Ω₀ is not the same relation. It has the same undominated set, and that is all the theorem needs.

### 4.3 The null set {P_S = 0} is essential (PROVED counterexample)
This is where uncountably many worlds and null sets interact in a way that matters.
- **The setting.**
  - Ω = (0,1]. E = {a + bω} is two-dimensional, closed, separable, contains 𝟙, and consists of bounded continuous functions.
  - S ≅ [0,1] by the mean m. The state m = 0 is the "limit at 0". It is **not** an evaluation.
  - P_S(h) = min(a, a+b). K′ = {m = 1/2}, so U = {a + b/2 > 0}.
- **The measure.** μ = (a standard Gaussian on (a,b)) + (the law of (0, β) with β ~ Exp(1)). This μ is finite, has full support and a first moment. It violates the hypothesis: μ{P_S = 0} ≥ μ(R) > 0 for the ray R = {a = 0, b > 0}.
- **The coherent model.** C = D_Q with Q = [0, 1/2] ∋ 1/2. Then C = {a > 0, a + b/2 > 0}, and R ∩ C = ∅.
- **The dominator.** Y = C ∪ R ∈ M_U, and r(Y,C) = (R, ∅). Every h = bω in R is strictly positive at every world, so the record is guidance at **every** ω ∈ Ω, and it is non-null. Hence Y ≺_ω C for all ω: **pure guidance strictly dominates a coherent model.** The same applies to D_S.
- **What this shows.** Pointwise-positive gambles with inf h = 0 exist as soon as the infimum is not attained. Strict guidance at each world then sees a gain that no single world's null set hides. The hypothesis μ{P_S = 0} = 0 is exactly what makes such gambles negligible.
- **A hidden boundary choice.** Y = C ∪ R is a coherent set of desirable gambles in Walley's sense, with a boundary choice. So the hypothesis is also what makes the "non-Archimedean boundary choices" of §6 invisible. It deserves an explicit sentence in §6.

## 5. Bounded, discontinuous gambles; general E versus C(Ω) (question (iii))

All definitions go through E. Ω carries no topology or σ-algebra, and the measure lives on E, not on Ω. The following reduction (PROVED) explains why nothing depends on Ω's cardinality or topology.
- **The compactification.** Let Ω̂ be the weak-* closure of {δ_ω} in S. It is compact and metrizable.
- **The embedding.** h ↦ ĥ|_Ω̂ embeds E isometrically, in an order-preserving and unital way, into C(Ω̂). Indeed sup_Ω̂ |ĥ| = sup_Ω |h|, and h ≥ 0 on Ω iff ĥ ≥ 0 on Ω̂.
- **States are countably additive on Ω̂.** Every q ∈ S extends to a positive normalized functional on C(Ω̂): use Hahn–Banach with the sublinear functional max f, which dominates q on E because q is positive and normalized. By Riesz, q is then given by a regular Borel probability on Ω̂. So **every state of a general separable E is countably additive on the metrizable compactum Ω̂**, though in general not on Ω, and not uniquely.
- **The points of Ω̂∖Ω** are "ideal worlds", such as the limit at 0 in §4.3. The ranking can be extended to them, and the theorem's uniform margin persists there.
- **Bounded, discontinuous gambles are fine.** For example, Ω = [0,1] with E the closed span of C[0,1] and 1_{[0,1/2]}. The definitions, Steps A–E and the ranking need only E's sup norm and its pointwise order. The only new phenomenon is that infima need not be attained. That is handled by μ{P_S = 0} = 0 (§4.3).
- **The difference for C(Ω), Ω compact metric:** Ω̂ = Ω, the infimum is attained, and states are regular Borel probabilities on Ω itself.

## 6. Contamination (question (iv))

### 6.1 The cover (G1–G6)
- **Clauses.**
  - (G), (IB), (GC), direct (C) and (ID) hold by §3.
  - D_K ∈ M_U, since p ∈ K gives D_K ⊆ D_{{p}}.
  - D_K is coherent, so it is undominated, by protection (§4.1). This is not a consequence of the theorem: it is Step E together with μ{P_S = 0} = 0.
  - (LF) is checked in §6.2.
- **The envelope.** P_K = (1−ε)p + ε min. Hence ∂D_K = {P_K = 0}: points with P_K > 0 are interior, points with P_K < 0 are exterior, and if P_K(h) = 0 then h + t𝟙 ∈ D_K for t > 0.
- **The boundary computation.** Let h ≠ 0 with P_K(h) = 0. Then 0 ≤ (1−ε)p(h) + εp(h) = p(h). If p(h) = 0, then ε > 0 forces min h = 0, so h ≥ 0, and p(h) = 0 with full support and continuity forces h = 0. So p(h) > 0 and h ∈ U.
- **ε = 1 (G6).** P_K = min h, and the same argument applies. **ε = 1 is covered.** The case ε = 0 is the precise model {p}: (LF) fails on any one-sided domain, as in the finite case.

### 6.2 Which (LF), and whether it is natural (G3)
- **The definition met.** (LF∞): there is a **norm-open** N ⊆ E with ∂D_K∖{0} ⊆ N (norm boundary) such that every Borel X with X △ D_K ⊆ N a.e. satisfies X ⊆ U a.e. This is the finite (LF) word for word, with "open" read in the norm topology. Since U = {p > 0} is also weakly open, the stronger weak-topology version holds too.
- **General characterization (PROVED, given full support).** For compact convex K ⊆ S and U = D_{K′}, the following are equivalent.
  - (a) D_K ∈ M_U and (LF∞) holds at D_K.
  - (b) K′ ⊆ K and C_K∖{0} ⊆ D_{K′}, where C_K = {P_K ≥ 0}.
  - (c) K′ ⊆ K, and for every k′ ∈ K′ the normal cone N_K(k′) = {h : q(h) ≤ k′(h) for all q ∈ K} is ℝ𝟙.

  *Proof.*
  - **(a)⟹(b):** K′ ⊆ K by (c∞),(d∞). The model D_K ∪ N lies in M_U, so N ⊆ U a.e., so N ⊆ U by (d∞). Moreover C_K = D_K ∪ ∂D_K.
  - **(b)⟹(a):** take N = U.
  - **(b)⟺(c):** h ∈ N_K(k′) iff g := k′(h)𝟙 − h ∈ C_K with k′(g) = 0. Also k′(g) ≥ 0 on C_K because k′ ∈ K. So (b) says such g must be 0, i.e. h is constant. The minimum over the compact K′ is attained, so pointwise positivity gives P_{K′}(g) > 0.
- **Finite case.** There, (c) is exactly "K is full-dimensional and K′ ⊆ relint K" (Lemma LF(b),(c)).
- **Consequence: universality in infinite dimensions.** The simple ranking on D_{K′} covers K iff K satisfies (b). Any ranking covering K on D_{K′} must satisfy (b), so **the simple ranking is a universal cover on D_{K′}** in this setting (PROVED, given the audit theorem). This is the right replacement for "full-dimensional": as the audit says, "relint K" should not be imported.
  - For example, (1−ε)p + εS does not contain p in its norm-relative interior: a small signed perturbation with a negative atom where p has none leaves S. Yet (LF∞) holds.
- **Natural?** Yes, as the literal analogue, and the characterization (c) shows it is the intrinsic one. But it is strictly weaker than finite-dimensional (LF) in one respect, recorded in §6.3.

### 6.3 No uniform tube (CHECKED, `no_uniform_tube.py`)
- **The finite case.** In finite dimensions, the compactness of ∂D_K ∩ (unit sphere) makes (LF) uniform: a tube of fixed relative width around the boundary lies in U.
- **The infinite case.** On Ω = [0,1], E = C[0,1], p = Lebesgue, take tents h_j of height 1 and half-width 2^{−j}. Put g_j = h_j − P_K(h_j)𝟙. Then:
  - P_K(g_j) = 0 and g_j ≠ 0;
  - dist(g_j, E∖U) ≤ p(g_j) = ε·2^{−j}, while ‖g_j‖ → 1.
- **Checked exactly** for ε = 1/2 and ε = 1. The relative distance falls from 1/3 to 4.9·10⁻⁴ for ε = 1/2, and from 1/2 to 9.8·10⁻⁴ for ε = 1.
- **The general fact (PROVED).** For every infinite compact metric Ω and every p, there are disjoint balls of p-mass tending to 0, with spikes on them. So **no target K ∋ p has uniform (LF) on {p > 0}.**
- **Consequence.** Only the literal (pointwise-open) (LF) is attainable. The audit's "natural norm-topological analogue" is right, but the paper should say that the finite-dimensional uniformity is lost.

### 6.4 p without full support (G7)
- **(LF) fails on U = {p > 0} (PROVED).**
  - Take a nonzero continuous h ≥ 0 supported in the open p-null set Ω∖supp p (Urysohn). Then p(h) = 0 and min h = 0, because h vanishes on supp p ≠ ∅.
  - So P_K(h) = 0, and h ∈ ∂D_K∖{0} lies outside U.
  - By (d∞), any open N in (LF) lies in U. So (LF) fails, and D_K is **not covered on {p > 0}**, for every ε ∈ [0,1].
  - This is the analogue of K′ meeting the relative boundary of Δ in the finite case.
- **Nearby result (PROVED).** Let ε ∈ (0,1] and let r be any full-support probability. Put k′ = (1−ε)p + εr ∈ K and U′ = D_{{k′}}. For g ∈ C_K∖{0}:
  - k′(g) = (1−ε)p(g) + εr(g) ≥ ε(r(g) − min g) ≥ 0;
  - equality forces g to equal min g on supp r = Ω, i.e. g is constant, and then P_K(g) = k′(g) = 0 gives g = 0.
  - So (b) of §6.2 holds, and **every contamination target with ε > 0 is covered on a suitable one-sided domain, whatever the support of p.**

### 6.5 General separable E (G8)
- **The characterization (PROVED).** Take K = (1−ε){p} + εS with ε ∈ (0,1] and U = {p > 0}. Then (LF∞) at D_K holds iff p is strictly positive: h ≥ 0 and h ≠ 0 imply p(h) > 0.
  - (⟸) is §6.1, with inf in place of min.
  - (⟹) Suppose h ≥ 0, h ≠ 0 and p(h) = 0. Then inf h ≤ p(h) = 0 forces inf h = 0. So h ∈ ∂D_K∖{0} lies outside U.
- **Full support is the special case.** In C(Ω), "strictly positive" is "full support". For indicator-type gambles it is not: for example, with p Lebesgue and 1_{{ω₁}} ∈ E, (LF) fails.
- **Strictly positive states always exist.** p = Σ 2^{−k} δ_{ω_k} over a norming sequence Ω₀ is one, since sup h > 0 implies h(ω_k) > 0 for some k. The nearby result of §6.4 then holds in every separable E, with r strictly positive.

## 7. Adversarial cases (question (v))

### 7.1 E without constants (V1)
- **(a) Counterexample (PROVED).**
  - Ω = {1,2} and E = {(t, 0)}. E is closed and separable, and 𝟙 ∉ E.
  - At world 2 every gamble pays 0. So d₂ ≡ 0, and the only guidance record at world 2 is the null record.
  - Under the simple ranking, ⪯₂ is a.e. equality. No model weakly dominates another, every model is undominated, and (GC) fails. For instance, X = {0 < t < 1} is incoherent and undominated.
  - The same happens whenever some ω has h(ω) = 0 for all h ∈ E.
- **(b) An order unit suffices (PROVED).** Suppose some e ∈ E has inf_Ω e > 0. Put Φ(h) = h/e.
  - Ẽ = Φ(E) ⊆ ℓ^∞(Ω) is closed, separable and contains 𝟙.
  - States normalized by q(e) = 1 correspond to states of Ẽ via q̃(h̃) = q(e·h̃). Then D_Q ↦ D_{Q̃}, and μ̃ = Φ_*μ inherits full support, the first moment and null boundaries.
  - The pointwise signs of gambles are unchanged, so guidance and safety are unchanged. Also d̃_ω = d_ω / e(ω) has the same sign as d_ω.
  - So the ranking is literally the transported one. The margin transfers: m(N) − m(X) ≥ (inf e)·ṽ 𝟙.
  - Hence "𝟙 ∈ E" can be weakened to "E contains an order unit".
- **(c) No order unit and no dead world, e.g. E = c₀ on Ω = ℕ.**
  - Every element of c₀ has inf ≤ 0. So the theorem's uniform conclusion inf_Ω(m(N) − m(X)) > 0 is **impossible**.
  - The state set {q ∈ ℓ¹₊ : ‖q‖ = 1} is not weak-* compact, so Step B's minimax loses its compact side.
  - Whether a pointwise version holds (strict dominance at every world, without uniformity) is **OPEN**. A natural attempt normalizes by a strictly positive e ∈ c₀. That gives an unbounded state set. Sion's theorem still applies, since Z_G is compact, but v = 0 no longer yields an attaining q*: mass can escape.

### 7.2 Non-metrizable state space (V2)
- By §1.1, S is non-metrizable iff E is nonseparable.
- Then no finite Borel measure has full support. Some ε gives an uncountable ε-separated set; otherwise maximal 1/n-separated sets would give a countable dense set. The disjoint ε/2-balls would each need positive mass. **The audit's claim in §6 is correct.**
- If full support is dropped, a finite Borel measure for which h ↦ h is Bochner integrable is concentrated on a separable subspace E₁. Models then live in E₁ modulo null sets, and the theorem reduces to E₁ (if 𝟙 ∈ E₁).
- The metrizability uses in Steps A and E (sequential dominated convergence, a countable dense subset of Q_X, the countable norming set) all fail without separability. But they are moot, since the measure hypothesis already fails.

### 7.3 Ω compact but not metrizable (V3)
- **E = C(Ω) is excluded.** C(Ω) is separable iff Ω is metrizable (Ω compact Hausdorff). So C(Ω) is outside the theorem, and so is the contamination example of §5. Examples: βℕ, where C(βℕ) ≅ ℓ^∞; and [0,1]^{[0,1]}.
- **Separable unital subspaces are included.** Any separable unital E ⊆ C(Ω) is inside the theorem: E is closed, separable and contains 𝟙, and Ω's topology plays no role. The effective world space is the metrizable Ω̂ ⊆ S of §5. For example, take E generated by countably many coordinate functions on [0,1]^{[0,1]}.
- **Contamination there** works with S = S(E), provided p is strictly positive on E₊∖{0} (§6.5).

## 8. Scope limits (§6 of the audit)

The five bullets of §6 are accurate. Six items should be added.
1. **An order unit is needed.** "𝟙 ∈ E" can be weakened to "an order unit e ∈ E" (§7.1(b)), but not dropped (§7.1(a)). For spaces such as c₀ the uniform conclusion is false and the pointwise question is open.
2. **The hidden boundary choice.** μ{P_S = 0} = 0 makes Walley-type boundary choices, such as pointwise-positive gambles with inf 0, invisible. Without it, protection fails (§4.3). The hypothesis is load-bearing, not technical.
3. **Countable additivity.** For general E, every state is a countably additive regular probability on the metrizable compactum Ω̂ ⊇ image(Ω) (§5). "Finitely additive" is a statement about Ω, not an intrinsic feature of the setting.
4. **Dependence on μ.** The theorem holds for every admissible μ, but "model" means "class modulo μ".
   - The coherent classes do not depend on μ: Q ↦ [D_Q] is injective for every full-support μ.
   - The incoherent classes, and hence the ranking, do depend on μ's null ideal. For example, atomic ν puts all mass on countably many lines (§1.3).
5. **(LF) is literal, not uniform** (§6.3).
6. **Universality.** The general (LF) characterization (§6.2(b),(c)) gives universality on each D_{K′}. It replaces "full-dimensional with K′ ⊆ relint K", and it should be stated if §5 is written up.

Minor wording repairs:
- §5: "the theorem makes D_K undominated" should read "protection (Step E) makes D_K undominated".
- §5: "it also supplies the natural analogue of (LF)" should read "a direct boundary computation gives (LF∞)".
- §4: name the minimax theorem (§2.4).
- §4: "summably weighted atoms" should read "atoms with Σ w_k‖g_k‖ < ∞".
- The positive continuous density of t can be weakened to an atomless law of full support.

## 9. Numerics: a curved state space with a continuum of worlds (`curved_states.py` → `curved_states.out`)

**What it tests.** Ω = [0,1] and E = span{1, ω, ω²} ≅ ℝ³. This E is finite-dimensional, but it has uncountably many worlds and a **curved** S = {(m₁, m₂) : m₁² ≤ m₂ ≤ m₁}. The extreme points of S are the evaluations, a continuum. This exercises P_S = inf over [0,1] (computed exactly for quadratics), the shrink by (1−τ)Q_X + τS with S non-polyhedral, and the uniform margin over a continuum.

**The setup.**
- K′ = {p}, with p Lebesgue, at (1/2, 1/3).
- μ = N(0, I₃) on the coefficients. Integrals are taken against a fixed empirical sample (n = 4·10⁵), so the results are exact for that discrete measure and NUMERICS for μ.
- q* is found by convex minimization over S, as in REF65_hA's Step 1′.
- τ is halved from 0.3 until half the margin survives.
- Hull invariance is tested on an 81×81 grid of states: q ∈ Q_{X∖N} iff no removed gamble has q(h) < 0.

**Results.**

| Rival | Q_X | v (minimax) | inf_{ω∈[0,1]} margin of N₀ | τ | inf_ω margin of N_τ | min # removed gambles with q(h) < 0, for q at distance ≥ 0.02 / 0.05 / 0.1 from Q_X: after shrink; **τ = 0 control** |
|---|---|---|---|---|---|---|
| R1: D_{[p,δ₀]} ∪ D_{[p,δ₁]} | {p} | 8.0·10⁻⁵ | 8.0·10⁻⁵ | 4.7·10⁻³ | 3.9·10⁻⁵ | 110 / 114 / 216; **0 / 0 / 139** |
| R2: two triangles sharing [p, δ_{1/2}] | [p, δ_{1/2}] | 8.0·10⁻⁵ | 7·10⁻⁵ | 5.9·10⁻⁴ | 5.2·10⁻⁵ | 2 / 9 / 120; **0 / 0 / 111** |
| R3: U minus a ball | {p} | 0.0190 | 0.0190 | 0.15 | 0.0119 | 832 / 1592 / 2888; **0 / 0 / 0** |

**Findings.**
- The minimax value equals the infimum of the margin over the continuum of worlds, as §1.2 predicts: S is the closed convex hull of the evaluations.
- N_τ ⊆ hull(X) in every case.
- After the shrink, every tested state outside Q_X is violated by some removed gamble. Without the shrink, states far from Q_X survive in all three rivals. So the shrink is genuinely needed here too, as in the finite case (REF65_hA, rivals E1b and E9).
- In R2, the smallest count near Q_X (2) reflects sampling resolution near the boundary of Q_X, not a failure.

## 10. Repairs requested (summary)
1. State the infinite-dimensional domain lemma, (c∞) and (d∞), and its consequences (§1.5).
2. State that A2 holds for every measurable B ⊆ U, and derive the safety ⟺ hull test from it (§3.1).
3. Name the minimax theorem (§2.4).
4. Atomic ν: require Σ w_k‖g_k‖ < ∞, and note the concentration on countably many lines (§1.3).
5. Flag μ{P_S = 0} = 0 as essential for protection, with the example of §4.3.
6. Weaken "𝟙 ∈ E" to "E has an order unit"; record the dead-world counterexample and the open c₀ case (§7.1).
7. In §5: say (LF∞) explicitly, i.e. the literal (LF) with norm-open N, and note that uniformity is lost (§6.3). Add the characterization of §6.2 and the universality it gives. For general E, replace "full support" by "strictly positive".
8. Record the nearby result for p without full support (§6.4).
9. Add §8's six items to the scope section.

## 11. Files (`iw66b_py/`)
| File | Content | Label |
|---|---|---|
| `curved_states.py` / `.out` | Steps A–D replayed on Ω = [0,1], E = span{1, ω, ω²}; 3 rivals; τ = 0 controls | NUMERICS |
| `no_uniform_tube.py` / `.out` | Exact rational check that the contamination boundary has no uniform tube inside U (ε = 1/2 and ε = 1) | CHECKED |
