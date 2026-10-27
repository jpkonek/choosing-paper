# Z2 — Connection: T1 joins the precise vertex models freely; the boundary is free; what fails is joining T1 to a coherent boundary

17 Oct 2026, round 28 (BRIEF20, milestone 2 "connection"; it also settles milestone 1). Labels:
- **PROVED**: full proof here, not refereed;
- **CHECKED**: exact rational arithmetic on stated samples;
- **CONJECTURE**;
- **NUMERICS**: floating-point sampling; nothing depends on it.

Scripts are in `z2py/`. Run each with `python3 -I z2py/<script>`; outputs are in the matching `.out` files. No assumption is added: every hypothesis beyond the §2 axioms is a hypothesis of the result that states it.

**Read:** BRIEF20, AUDIT_Y123 (Props 1–5, §5: trivial isolated interior subsystem), AUDIT_X123, Y1, Y2 (§6: Y2.11, Y2.12), Y3 (Y3.1–Y3.8, Y3.C), X1, write-up §2, §6 (Thm gm, route I1) and §8.6 (Thm L4.1, Prop L4.3).

**Domain and notation.** The full two-sided domain: every measurable model is evaluable, so (LF) at T1 is automatic. As in the write-up:
- c₀ = (1−ε)/3, λ = ε/c₀, A = 1+λ = κ, and b := 1/(2+λ);
- v_k = c₀(𝟙+λe_k), u = 𝟙/3;
- E_k := {g : g_k > 0} is the precise vertex model at e_k.

For an additive field in acceptance-vector form (Y3 §1), take n(g) = m(g)⊙g with m > 0 bounded. The losses are ℓ(h,S) = 0, ℓ(h,M) = −n(h), ℓ(h,O) = −n(−h), and a large contradictory penalty. By Lemma Y3.1:
- such a field is strictly guiding, with integrable envelope;
- its w-Bayes advice on the pair {h,−h} is M iff w·n(h) > max(0, w·n(−h)), and symmetrically for O.

Write G(Ψ) := {w ∈ Δ : Ψ has a coherent w-Bayes model}.

---

## 0. Outcome

**1. Option (b) of the milestone is false: there is no connection obstruction between T1 and the precise vertex models (Thm Z2.4, PROVED; CHECKED).**

One strictly guiding additive field Ψ^Y on the full domain carries a closed selection on a connected index set S_Y. S_Y consists of:
- a closed plateau W ∋ u where C_p = T1;
- three legs from W to the three vertices, along which C_p = (1−s)T1 + s e_k;
- closed neighbourhoods N_k of the vertices, edge pieces included, where C_p = E_k.

The selection satisfies, against every measurable competitor:
- competitiveness on supp p;
- protection (T1 ∈ C_L);
- no (C)-ties;
- closed sections, strict (G), (IB) and transitivity.

So the transition from T1 to all three precise vertex models carries no obstruction, simultaneously at all three vertices, with one triple of complete additive orders. A fortiori it carries none for independent preorders.

**2. The whole boundary together with T1 is also free (Thm Z2.5, PROVED; CHECKED).** A second strictly positive additive field Ψ^∂ has:
- T1 as its a.e.-unique u-Bayes model;
- coherent, a.e.-unique, edge-supported Bayes models at every weight of ∂Δ;
- precise vertex models.

Its selection on ∂Δ ∪ N₁ ∪ N₂ ∪ N₃ ∪ W satisfies every axiom. Consequences:
- **BRIEF20 milestone 1 holds in strong form:** three vertex neighbourhoods, all three edges and T1, in one additive system.
- **Y3's Conjecture Y3.C is false as stated.** Already the vertex plateaus of Lemma Z2.1 refute it in Y3's own field.
- **Y2.11 and Y2.12 do not extend beyond their scope.** The edges of Ψ^∂ are neither precise nor posterior. Near e_i the edge odds interval is [2r/(2+λ), A·r]; at the midpoint it is [1/A, A], which is T1's shadow, as route I1 of Thm gm forces.

**3. What actually fails: connecting T1 to a coherent boundary (Thm Z2.6, Prop Z2.7, PROVED; CHECKED; NUMERICS).**
- **Thm Z2.6 (additive rankings).** Suppose T1's weight u is an isolated point of G(Ψ). Then every closed selection on a connected index set through T1 is constant, equal to T1, and stays in Δ°. T1 is then disconnected from everything else in the system.
- **Prop Z2.7.** For Ψ^∂, u is isolated in G(Ψ^∂). There is an explicit non-convexity certificate at every q ≠ u near u (exact certificates at 216 weights).
- So the additive pieces exist separately: Ψ^Y connects T1 but has an incoherent boundary, and Ψ^∂ has a coherent boundary but isolates T1.
- **CONJECTURE Z2.C.** Every additive field with coherent boundary Bayes models and T1 ∈ C_L isolates T1's weight. With Z2.6, this would be an additive *connection obstruction*: it would localise Thm gm from a 2-cell to a single path from T1 to ∂Δ. Evidence is in §5.

**4. Where the forced comparisons are, and where earlier obstructions live (§2, PROVED).**
- At a plateau boundary the forced comparisons are "veto inheritance" (Lemma Z2.3). Suppose X beats T1 at two worlds. Then every zone model near the plateau is no worse than X at the third world. These comparisons are satisfiable: the tripod satisfies them.
- A plateau's model must be competitive on the support of each of its limit indices (Lemma Z2.2). So the T1 plateau never reaches ∂Δ, and the zone must separate it from the boundary.
- L3.4, X2.9 and Y3.7 do not live in the T1→vertex transition, which is free. They also do not exclude "boundary + T1", which is free.
- The new, sharper constraint is the coupling between T1 and a coherent boundary. In additive form it reads: the zone models next to the plateau must be Bayes at weights converging to u (proof of Z2.6), and Ψ^∂ has no coherent Bayes models there.

**Nearby result (project preference).** The literal target was a closed selection on all of Δ through T1, with non-additive orders. It is not reached. The proposed impossibility (b) is refuted, not proved. The reachable statements are 1–3 above. They move the T1 question to one precise place: a path from the T1 plateau to a coherent boundary system.
- In additive rankings this is the isolation phenomenon (Z2.6, Z2.7, Z2.C).
- A non-additive escape must break exactly one step of Z2.6: "competitive ⇒ Bayes for some weighting of the world losses", for zone models next to T1 (§6, Q_Z2).

---

## 1. Plateaus, ties and competitiveness

**Lemma Z2.1 (vertex plateaus are free; PROVED).** Take any ranking on the full domain with strict (G), and any k.
- (a) E_k ≺_k X for every model X ≠ E_k a.e.
- (b) For every closed N ⊆ {p : p_k > 0}, the constant selection C_p := E_k on N has these properties:
  - competitive on supp p;
  - undominated;
  - tied at every world with no other model;
  - its sections, relative to N, are N or ∅, hence closed.
- (c) Suppose the orders are complete and T1 is competitive on Ω (e.g. T1 is an a.e.-unique w-Bayes model of an additive ranking). Then for every closed W ⊆ Δ°, the constant selection C_p := T1 on W satisfies the same clauses relative to W.

*Proof.*
- (a) E_k gives world-k-good advice on every pair. Any X ≠ E_k gives worse world-k advice on a non-null set and better on none, so (G) applies.
- (b) By (a), E_k ⪯_k X for every X, and k ∈ supp p.
- (c) supp p = Ω on W. ∎

*Consequences.*
- **Y3.C is false as stated.** Y3.C reads: "no additive field with T1 ∈ C_L has closed competitive coherent selections near two vertices". Take Y3's field Ψ⁽¹⁾ (T1 ∈ C_L) with C_p = E₁ on N₁ and C_p = E₂ on N₂. What Y3.7(b) actually excludes is box selections that are Bayes at their own index.
- **BRIEF20 milestone 1, without the boundary, is trivial in the same way.**

**Lemma Z2.2 (plateau limits; PROVED).** Take any ranking satisfying the axioms on an index set S (sections closed relative to S, C_p ∈ C_L). Let p_n → p in S with C_{p_n} ~_i M at every world i, for a fixed M ∈ C_L. Then C_p ~_i M at every world, and M is competitive on supp p.

*Proof.*
- C_{p_n} ⪯_i M, so closedness gives C_p ⪯_i M at every i.
- If C_p ≺_j M for some j, then M is dominated, which is impossible. Hence C_p ~_i M at every i.
- Competitiveness of C_p on supp p transfers to M by transitivity. ∎

**Corollary Z2.2′ (PROVED).** The set {p ∈ S : C_p ~ T1 at every world} is closed in S and contained in Δ°.

*Proof.* T1 is not competitive on any S′ ⊊ Ω. For example, on {1,2}: accept the gambles with g₁, g₂ > 0 > g₃ that T1 rejects. This set is non-null, and the change is a strict improvement at worlds 1 and 2 by (G). ∎

So a T1 plateau is compact in Δ°, and every closed selection on Δ through T1 has a transition zone that separates it from ∂Δ.

**Lemma Z2.3 (veto inheritance: the forced comparisons in the zone; PROVED).** Take p_n → p in S with C_p ⋠_i X for all i in some set I. Then for all large n:
- C_{p_n} ⋠_i X for every i ∈ I;
- C_{p_n} ⪯_j X for some j ∈ supp p_n ∖ I.

*Proof.* The first item is closedness, in contrapositive form. The second is competitiveness of C_{p_n}. ∎

For a T1 plateau with complete orders, at p ∈ ∂W, define for each world l (with {i,j,l} = Ω)

  Φ_l := {X : X ≺_i T1 and X ≺_j T1}.

Then every X ∈ Φ_l has C_q ⪯_l X for zone indices q near p. The neighbourhood depends on X.
- For additive rankings this says limsup L_l(C_q) ≤ inf_{Φ_l} L_l. With lower semicontinuity it gives L(C_q) → L(T1).
- These are exactly the comparisons the brief asked about. They are satisfiable: Thm Z2.4 satisfies them, by continuity in measure.

---

## 2. The tripod: T1 joined to all three precise vertex models

**Construction of Ψ^Y.** Fix an interior a ∈ Δ° (we take a = u). The leg families are

  K_k(s) := (1−s)T1 + s e_k,  s ∈ [0,1],

and P_{K_k(s)}(g) = (1−s)P_{T1}(g) + s g_k is affine in s. The leg weights are w_k(s) := (1−s)a + s e_k.

For a gamble g with P₀ := P_{T1}(g) ≠ 0, put σ := sign P₀, and let J be the set of legs on which g's acceptance changes:

  J := {j : sign g_j = −σ},  with |J| ≤ 2.

For j ∈ J, the root of the leg family is s_j := P₀/(P₀ − g_j) ∈ (0,1), and the crossing weight is x_j := w_j(s_j). Define n(g) as follows:
- **|J| = 0:** n := g.
- **|J| = 2, J = {j,k}:** n ∝ x_j × x_k, oriented so that sign(n·a) = σ.
- **|J| = 1, J = {j}:** n := σ(α(e_k + e_l) − βe_j) with α = 1 and β = (1−s_j)(a_k + a_l)/((1−s_j)a_j + s_j). This is the line through x_j with e_k, e_l and a on one side.

Finally, normalise n so that |n|_∞ = |g|_∞.

**Lemma Z2.4a (PROVED; CHECKED).**
- (i) n(g) has the strict sign pattern of g.
- (ii) For every k, every s ∈ [0,1] and a.e. pair h, the Bayes advice of Ψ^Y at w_k(s) is that of D_{K_k(s)}.
- (iii) At s = 0 that advice is T1's; at s = 1 it is E_k's.

*Proof.*
- **The line ℓ_g.** By construction, ℓ_g := {w : w·n(g) = 0} meets the tripod exactly at the crossing points x_j (j ∈ J), and it has a on the σ side.
- **|J| = 2.** A line through x_j and x_k (on legs j and k) separates a from e_j and e_k. It cannot also cross leg l: if it did, a would lie on one side and all of e₁, e₂, e₃ on the other, contradicting a ∈ int Δ. So e_l is on a's side.
- **|J| = 1.** Here n·e_k = n·e_l = σ, n·e_j = −σβ, and n·x_j = 0 by the choice of β. Substituting β gives n·a = σα(a_k + a_l)·s_j/((1−s_j)a_j + s_j), which has the sign σ.
- **(i).** In both cases n·e_m has the sign of the side of e_m, and that is the sign of g_m: legs in J have g_m = −σ, the others have g_m = σ.
- **(ii).** Along leg k, w_k(s)·n(g) is affine in s. It has the sign σ at s = 0, and its only root is at s_k if k ∈ J, with none otherwise. P_{K_k(s)}(g) is affine with the same root and the same sign at 0. So the two have the same sign on [0,1]. Apply this to n(h) and n(−h). Since D_{K_k(s)} is coherent, at most one of them is positive, and the Bayes advice is the D_K advice.
- **Ties** occur only where some P_{K_k(s)}(±h) = 0, a finite union of hyperplane pieces in h. These are null.
- **(iii)** is (ii) at the end points. ∎

CHECKED (`z2_tripod.out`):
- ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5}, 1500 pairs each;
- random gambles, gambles within 10⁻⁴ of T1's boundary, and gambles near the coordinate planes;
- s random, at 0 and 1, and within 10⁻⁶ of each pair's crossing;
- about 20 000 leg checks per ε: **0** sign-pattern failures, **0** leg mismatches, **0** endpoint failures.

The first run flagged 14–37 "mismatches" per ε. All of them were gambles sampled exactly on ∂D_{T1} (P_{T1} = 0, a null set) by a shift of 0. They are excluded in the run reported.

**Theorem Z2.4 (tripod connection; PROVED).** Fix small ρ, ρ′ > 0. Define:
- W := {p : |p−u| ≤ ρ};
- N_k := {p ∈ Δ : p_k ≥ 1−ρ′};
- Λ_k := the segment of [u, e_k] between ∂W and ∂N_k;
- S_Y := W ∪ ⋃Λ_k ∪ ⋃N_k, which is closed and connected.

Let φ : S_Y → Δ be continuous, with:
- φ ≡ u on W;
- φ ≡ e_k on N_k;
- φ mapping Λ_k affinely onto [u, e_k].

Put C_p := the Ψ^Y-Bayes model at φ(p). On W this is T1, on Λ_k it is D_{K_k(s)}, and on N_k it is E_k. Then:
- **(a)** Ψ^Y is additive, strictly guiding, with integrable envelope; it satisfies (G) and (IB). T1 is its a.e.-unique u-Bayes model, so T1 ∈ C_L, (LA) holds, and (LF) holds.
- **(b)** For every p ∈ S_Y and every measurable X:
  - C_p is coherent and competitive on supp p;
  - C_p is undominated;
  - every model tied with C_p at every world equals C_p (Csel);
  - {p ∈ S_Y : C_p ⪯_i X} is closed.

*Proof.*
- **(a)** Lemmas Y3.1 and Z2.4a.
- **(b), coherence and competitiveness.**
  - On W ∪ Λ_k, supp p = Ω. A w-Bayes model of a complete additive ranking is beaten at all three worlds by no X, since otherwise w·L(X) < w·L(C).
  - On N_k use Lemma Z2.1.
- **(b), uniqueness.** C_p is the a.e.-unique φ(p)-Bayes model. Any model tied with it is also φ(p)-Bayes, hence equal to it.
- **(b), closedness.** p ↦ C_p is continuous in measure on S_Y: the Bayes models along a leg move with null ties, and φ is continuous. By dominated convergence p ↦ L_i(C_p) is continuous. ∎

**Global (C).** It also holds, in the following sense (PROVED). Every coherent undominated model is w-Bayes for some w, by Aumann convexity (Y3.7, Step 0). At every w the Bayes model of Ψ^Y is a.e. unique. On each of the finitely many rational pieces of n, the functions w·n(h) and w·(n(h) − n(−h)) are real-analytic and non-constant in h, so their zero sets are null.

**Corollary Z2.4′ (no connection obstruction; PROVED).** Option (b) of the milestone is false: closed selections through T1 can be joined to the precise vertex models under all the axioms. A single additive ranking does it at all three vertices at once. Any exclusion of T1 must use indices on the open edges, that is, two-world competitiveness away from the vertex plateaus.

---

## 3. The boundary together with T1

**Edge pinning (PROVED, elementary).** Suppose an additive field's Bayes models on the edge {i,j} are coherent and a.e. unique at every edge weight. Then, for g_i > 0 > g_j with ratio x := g_i/|g_j|, the switching odds w_j/w_i depend on x alone. Call them s_ij(x); the function s_ij is increasing.

Equivalently, m_i/m_j = s_ij(x)/x on every mixed gamble. Every mixed gamble has exactly two opposite-sign coordinate pairs, so **the boundary families determine n(g) up to scale for every mixed g.**

The edge model is coherent iff s_ij(x)·s_ji(1/x) ≤ 1 for all x. Its credal segment has odds of world j over world i in

  [1/s_ji⁻¹(1/r), s_ij⁻¹(r)],  where r = w_j/w_i.

**T1 at u.** Write S_ij(v) := 1/s_ij(1/v). Then u-Bayes = T1 is equivalent to two families of equations:
- **(E1)** on (i,k|j) gambles (x, y, −1): s_ij(x) + s_kj(y) > 1 ⟺ x + y > A;
- **(E2)** on (i|j,k) gambles (1, −y, −z): S_ij(y) + S_ik(z) < 1 ⟺ y + z + λ·max(y,z) < 1.

Each is a single level set of a separable function, so each is satisfiable.

**Construction of Ψ^∂ (S₃-symmetric).** Take one function s for all six ordered pairs, built from S(v) := 1/s(1/v):
- S(v) = (2+λ)v/2 on [0, b];
- S(v) = 1 − (2+λ)(1−Av)/2 on [b, 1/A];
- S(v) = Av on [1/A, ∞).

So s(x) = x/A on (0, A].

**Theorem Z2.5 (PROVED; CHECKED).** Ψ^∂ is a strictly guiding additive ranking on the full domain with integrable envelope, and:
- **(a)** T1 is its a.e.-unique u-Bayes model, and T1 is w-Bayes for no w ≠ u.
- **(b)** At every boundary weight the Bayes model is coherent, edge-supported and a.e. unique. At e_k it is E_k. On the edge {i,j} at odds r = w_j/w_i, the credal odds of j over i form the interval [1/s⁻¹(1/r), s⁻¹(r)]. In particular:
  - for r ≤ 1/2 the interval is [2r/(2+λ), Ar];
  - at the midpoint (r = 1) it is [1/A, A], which is T1's shadow from the opposite vertex.
- **(c)** Let S_∂ := ∂Δ ∪ N₁ ∪ N₂ ∪ N₃ ∪ W, with W ⊆ Δ° closed and N_k as in Z2.4. Define the selection by:
  - C_p := E_k on N_k;
  - C_p := T1 on W;
  - C_p := the Bayes model at ψ(p) on ∂Δ ∖ ⋃N_k, where ψ is a continuous reparametrisation of each edge that is ≡ e_k on N_k.

  This selection satisfies, against every measurable X: competitiveness on supp p, undominatedness, Csel, and closed sections relative to S_∂. Global (C) holds by the argument of §2.

*Proof.*
- **Sign pattern and guidance.** m > 0 is bounded after normalisation.
- **(a): (E1).** With s = t = x/A on (0, A), s(x) + s(y) = 1 exactly on x + y = A. For x ≥ A, s(x) ≥ 1, which gives acceptance, as T1 gives.
- **(a): (E2).** S(y) + S(z) = 1 exactly on T1's broken line. For y ≥ z the line has z = 1 − Ay ≤ b, so S(y) = 1 − S(z), by the middle formula. Beyond y = 1/A, S(y) > 1, which gives rejection, as T1 gives. Strict monotonicity yields the open sets.
- **(a): other patterns** follow by S₃ symmetry; unanimous gambles are trivial.
- **(a): ties** lie on level curves of strictly increasing separable functions, which are null.
- **(a): "only at u".** Suppose T1 is w-Bayes. Letting y → 0 in (E1) at w gives w₃ = w₁; letting x → 0 gives w₃ = w₂. At boundary weights some open set of mixed gambles is accepted with all sign patterns allowed, so boundary weights are excluded. (NUMERICS in `z2_t1only.out`: on a 30-grid, the disagreement with T1 is 0 only at u and ≥ 0.9% elsewhere.)
- **(b): product condition.**
  - For x ∈ (1/A, A): s(x)s(1/x) = 1/A² < 1.
  - For x ≤ 1/A: s(x)s(1/x) = x/(A·S(x)) ≤ 1, since S(x) ≥ x/A on [0, 1/A].
  - For x ≥ A the case is symmetric.
- **(b): coherence and vertex limits.** Since s is strictly increasing, the edge model accepts a cone that depends on (g_i, g_j) only. As r → 0 it converges in measure to E_i.
- **(c)** Lemma Z2.1, Lemma Y3.1(d),(e), and continuity in measure on each component. W is disjoint from ∂Δ ∪ ⋃N_k. ∎

CHECKED (`z2_boundary.out`), exact, ε ∈ {1/20, 1/10, 3/10, 1/2, 4/5}:
- s⁻¹∘s = id and monotonicity: 0 failures;
- product condition: 0 failures;
- sign patterns: 0 failures;
- u-Bayes vs T1 on 3000 pairs (half within 3·10⁻⁵ of ∂D_{T1}): **0** mismatches;
- edge Bayes advice vs the explicit credal segment, 12 000 checks including gambles at relative distance 10⁻⁵ from the switching ratios: **0** mismatches;
- vertices: 0 failures.

**Remarks.**
1. **Y2.11 and Y2.12 do not apply.** Y2.12 says precise edges, a strictly positive endorser and T1 at u are inconsistent. Y2.11 says posterior edges force half-edge blindness. Ψ^∂ is itself a strictly positive endorser, and its edges are of a third kind.
2. **Route I1 is consistent with this.** The cover-forced midpoint limit (Prop edgelimits: parameters (1−ε)/(2+ε) and (1+2ε)/(2+ε), i.e. odds 1/A and A) is reproduced. Route I1's contradiction needs coherent Bayes models in a two-dimensional neighbourhood of u, and Ψ^∂ has none (§4).

---

## 4. Connection in additive rankings: isolation

**Theorem Z2.6 (isolation ⇒ no connection; PROVED).** Let Ψ be an additive, strictly guiding ranking with integrable envelope on the full domain. Assume:
- (i) T1 is the a.e.-unique u-Bayes model and is w-Bayes for no w ≠ u;
- (ii) u is an isolated point of G(Ψ).

Let S ⊆ Δ be connected, and let p ↦ C_p ∈ C_L be competitive on supp p with sections closed relative to S. If C_{p₀} ~ T1 at every world for some p₀ ∈ S, then:
- C_p = T1 a.e. for every p ∈ S;
- S ⊆ Δ°.

*Proof.* Let W := {p ∈ S : C_p ~ T1 at every world}. By Lemma Z2.2, W is closed in S.

*W is open in S.* Let p ∈ W and p_n → p in S, and suppose p_n ∉ W for infinitely many n.
- **Step 1 (Bayes weights).** C_{p_n} is competitive on supp p_n. The range {L(X) − L(C_{p_n})} is convex (Aumann; Y3.7, Step 0). So C_{p_n} is w_n-Bayes for some w_n ∈ Δ. Since C_{p_n} is coherent, w_n ∈ G(Ψ).
- **Step 2 (limits).** Coherent models are compact in measure (write-up, proof of Lemma H10(a)), and L is continuous in measure. So along a subsequence:
  - w_n → w*;
  - C_{p_n} → C* in measure, with C* coherent and w*-Bayes.
- **Step 3 (semicontinuity).** Closedness gives L_i(C_p) ≤ L_i(C*) for each i. The range of L_i is an interval (Lyapunov), so every level c is realised by some X. Hence L(T1) = L(C_p) ≤ L(C*) coordinatewise.
- **Step 4 (the limit weight is u).** Since C* is w*-Bayes, w*·L(C*) ≤ w*·L(T1). Hence T1 is w*-Bayes, and by (i), w* = u.
- **Step 5 (contradiction).** So w_n → u with w_n ∈ G(Ψ). By (ii), w_n = u for large n, so C_{p_n} = T1 and p_n ∈ W. This is a contradiction.

S is connected, so W = S. A model tied with T1 is u-Bayes, hence equal to T1. Finally, S ⊆ Δ° by Corollary Z2.2′. ∎

*Reading.* In an additive ranking, the zone models adjacent to a T1 plateau must be coherent Bayes models at weights converging to u. This is the additive content of the brief's "forced comparisons persist into the zone". The proof uses three additive facts:
- (A1) competitive ⇒ Bayes for a weighting;
- (A2) compactness;
- (A3) uniqueness at u.

**Proposition Z2.7 (Ψ^∂ isolates T1; PROVED; CHECKED).** Let q ∈ Δ°, and suppose there are distinct i, j with 0 < q_i − q_j < q_k/2, where k is the third index. Then Ψ^∂'s Bayes model at q (which is a.e. unique) is not coherent. In particular, u is isolated in G(Ψ^∂), and Thm Z2.6 applies: **in Ψ^∂ no closed selection on a connected set joins T1 to any other model, in particular not to the boundary system of Z2.5.**

*Proof.*
- **The slice.** Take the slice g_i = 1, g_j = −y, g_k = −z. Acceptance at q is q_j·S(y) + q_k·S(z) < q_i, that is, y < y(z), with y(·) decreasing. The accepted slice is convex iff y(·) is concave.
- **The kink point.** Put k_S := (2+λ)/2 > 1 and z* := (q_i − q_j)/(k_S q_k) ∈ (0, b).
  - For z < z*: S(y) > 1, so y = (q_i − q_k k_S z)/(A q_j), with slope −q_k k_S/(A q_j).
  - For z > z*: S(y) ∈ (1/2, 1), so y = (1 − (1 − S(y))/k_S)/A, with slope −q_k/(A q_j).
- **The kink is convex.** The slope increases across z* (since k_S > 1). The chord between z* ± h lies above the curve by h·q_k(k_S−1)/(2A q_j) at z*.
- **Certificate.** The gambles g± on the curve, pushed slightly inside, are accepted, and g₊ + g₋ is rejected. The defect is an open condition, so no D_K agrees with the Bayes model a.e.
- **Isolation.** Near u, every q ≠ u has such a pair (i, j), so u is isolated in G(Ψ^∂).
- **Uniqueness of the Bayes model** follows from Theorem Z2.5(a); hypothesis (i) of Thm Z2.6 is Theorem Z2.5(a). ∎

CHECKED (`z2_isolation.out`): exact certificates (g₊, g₋ accepted, g₊ + g₋ rejected) at q = u + r·d for ε ∈ {1/10, 3/10, 3/5}, r ∈ {10⁻², 10⁻³, 10⁻⁵}, and 24 directions d: **72 of 72** per ε.

NUMERICS:
- `z2_scan.out`: on grids with spacings 1/10 and 1/12, every interior weight except u has an incoherent Bayes model.
- `z2_scan_near_u.out`: circles of radius 0.05, 0.01 and 0.002, 24 directions each: all incoherent.

**CONJECTURE Z2.C (additive connection obstruction).** Suppose an additive strictly guiding field has coherent, a.e.-unique Bayes models at every boundary weight and T1 as an a.e.-unique Bayes model at some interior weight. Then that weight is isolated in G.

By Thm Z2.6 (after the rescaling of Prop diag(a), which moves T1's weight to u), Z2.C would give the following: **no additive ranking carries a closed selection on ∂Δ ∪ γ, with γ any path from a T1 index to ∂Δ.** That would localise Thm gm to a 1-dimensional connection.

*Evidence (not a proof).*
- (a) Prop Z2.7.
- (b) **A first-order analysis at u (heuristic).** Coherence of the Bayes model at u + δ reduces to local conditions at the places where T1's boundary is assembled from the edge functions:
  - at the six coordinate crossings, the junction slopes S_ik′(0) versus 1;
  - at the three corners, slope ratios at b within [1/A, A];
  - on the facet pieces, curvature conditions linear in δ, of the form (δ_i − δ_j)·(1/S_ik′)″ + (δ_j − δ_k)·(S_ik/S_ik′)″ ≤ 0.

  For S₃-symmetric fields the three curvature vectors of a cyclic triple sum to zero. That forces linear pieces, hence the kink of Prop Z2.7. For the vertex directions, with regular slopes, the conditions conflict: one needs (S/S′)″ ≥ 0 on one function, which caps S(b) ≤ b, while the partner function needs S(b) ≥ 1 − b with (1−S)/S′ convex and T′(0) ≥ −1. This forces ∫₀ᵇ 1/T ≤ −ln(1−b) < −ln b. I re-derived parts of this list twice during the round (corner and crossing conditions were found only from numerics), so it should not be relied on as complete.
- (c) **NUMERICS.** Three non-symmetric designs aimed at a leg toward e₃ (`z2_asym.out`, `z2_asym2.out`, `z2_asym3.out`) keep T1 at u (0 mismatches) and edge coherence. Each fails at first order (defect ∝ t) along legs toward e₃, e₁ and the midpoint of [e₁,e₂]:
  - the first at T1's corners;
  - the second and third at the coordinate crossings next to e₂ (`z2_diag3.out`).

---

## 5. What this means for T1

1. **Where obstructions do not live.**
   - The plateau-to-vertex transition: Thm Z2.4.
   - The boundary taken together with T1: Thm Z2.5.
   - Vertex neighbourhoods: Lemma Z2.1.
   - L3.4 (vetoes), X2.9 (vertex symmetry of local orders) and Y3.7 (box rigidity of Bayes-at-index vertex plans) are not triggered by any of these components.
2. **Where it must live.** In the coupling between T1 and a coherent boundary through the zone.
   - Topologically, the zone must separate W from ∂Δ (Cor. Z2.2′).
   - Additively, zone models next to W are coherent Bayes models at weights converging to T1's weight (Thm Z2.6). That is a real restriction: Ψ^∂ has none.
   - Globally, Theorem kkm together with (C) gives the familiar global form: every undominated model is coherent.
3. **The precise non-additive target.**

   > **Q_Z2.** Is there a triple of independent preorders that carries a coherent boundary selection on ∂Δ (e.g. that of Ψ^∂, whose boundary comparisons are fixed by (IB) on boundary-realisable records) and a closed selection on a path γ from a T1 plateau to ∂Δ?
   >
   > Such a triple must violate (A1) for the zone models adjacent to W: those models must be competitive on Ω without being Bayes for any weighting of the world losses. For complete orders this means a non-convex weak-Pareto frontier near L(T1).

   Unlike the T1→vertex link, this is a genuinely coupled one-dimensional problem. By Z2.6–Z2.7 it already fails in the boundary ranking Ψ^∂ itself, and (if Z2.C holds) in every additive ranking.
4. **Settling T1 negatively** would need Q_Z2 answered negatively for all independent preorders. Neither direction is established here.

---

## 6. Status

| Item | Status |
|---|---|
| Z2.1 vertex plateaus free for every strictly guiding ranking; T1 plateau free; Y3.C false as stated | PROVED |
| Z2.2 plateau limits; Z2.2′ T1-tie set closed and interior | PROVED |
| Z2.3 veto inheritance (forced comparisons in the zone) | PROVED |
| Z2.4a tripod field realises the three contamination legs | PROVED; CHECKED (≈10⁵ exact checks, 0 failures) |
| **Z2.4 tripod connection: T1 plateau joined to E₁, E₂, E₃ in one additive system, all axioms** | **PROVED** |
| Z2.4′ option (b) of the milestone false | PROVED |
| **Z2.5 boundary + vertex neighbourhoods + T1 in one strictly positive additive system** | **PROVED; CHECKED** |
| **Z2.6 isolation of T1's weight in G ⇒ no closed connection through T1 (additive)** | **PROVED** |
| **Z2.7 Ψ^∂ isolates T1 (explicit certificate)** | **PROVED; CHECKED (216/216 exact certificates)**; NUMERICS (grids) |
| Z2.C every coherent-boundary additive field isolates T1 (additive connection obstruction) | CONJECTURE (heuristic first-order analysis; NUMERICS) |
| Q_Z2 non-additive connection of T1 to a coherent boundary | open |
| Closed selection on all of Δ through T1 (the milestone's literal target) | not obtained |

**Referee priorities.**
1. Lemma Z2.4a, case |J| = 1: the sign of n·a and the side of e_k, e_l.
2. Thm Z2.5(a): the "only at u" step, and the (E2) branch bookkeeping on [b, 1/A].
3. Thm Z2.6, Step 3: lower semicontinuity of L_i ∘ C from closed sections, which uses that the range of L_i is an interval.
4. Prop Z2.7: the slope computation on both sides of z*.

## 7. Files (`z2py/`)

- `z2common.py`: exact helpers.
- `z2_tripod.py` / `.out`: Lemma Z2.4a (CHECKED).
- `z2_boundary.py` / `.out`: Thm Z2.5 (CHECKED).
- `z2_isolation.py` / `.out`: Prop Z2.7 certificates (CHECKED).
- `z2_scan.py` / `.out`, `z2_scan_near_u.py` / `.out`: coherence maps of Ψ^∂ (NUMERICS).
- `z2_t1only.py` / `.out`: T1 is Bayes only at u in Ψ^∂ (NUMERICS).
- `z2_diag.py` / `.out`: location of the Ψ^∂ defect near u (NUMERICS).
- `z2_leg.py` / `.out`, `z2_diag2.py` / `.out`: symmetric variants of S_low (NUMERICS).
- `z2_asym.py`, `z2_asym2.py`, `z2_asym3.py` / `.out`, `z2_diag3.py` / `.out`: non-symmetric designs for a leg toward e₃ (NUMERICS for Z2.C).
