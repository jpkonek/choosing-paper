# OUT67: proof outline for the application paper

26 October 2026. Role: OUT67 (BRIEF67). Revision 3, after the RF67a, RF67b and REF67_out reports. REF67_out re-derived the whole chain and finds it mathematically sound. This is a mathematical skeleton, not a manuscript. It follows the binding decisions in `AUDIT_r67_message2.md`.

## Status labels

- **[refereed: …]** The proof has been checked by the named referees. RF67a and RF67b independently found the full-domain theorem correct, with no mathematical error. Their repairs are made below.
- **[new here]** The proof is mine alone and has not been refereed. The appendix lists every such item.

## The chain in one paragraph

Part 1 fixes the setting and separates sets from classes. Part 2 proves one minimax lemma, used twice: to optimise inside a coherent hull, and to locate a uniformly losing part. Part 3 proves the trimming lemma, which only the consistent case needs. It also proves a lemma saying that N ⊆ hull(X∖N), together with a strict score gain at every world, makes a change impossible for any coherent model. Part 4 proves the repair theorem **directly on the full space E**. Part 5 derives the ranking. Part 6 derives the restricted-domain results from the repair theorem's location clause.

The one-sided theorem (Theorem 7.7 of the note) is **not** an ingredient. Its proof is contained in the consistent case below, and its only step that used K′ is replaced by Lemma 3.3. The one-sided dominance result is therefore a genuine restriction of Theorem 4.1.

```
Part 1 (setting; hull lemma; sets vs classes)
 ├─ Lemma 2.1 (minimax) ─┬─ Cor 2.2 (consistent case: optimise in hull(X))
 │                       └─ Cor 2.3 (uniformly losing part)
 ├─ Lemmas 3.1–3.2 (contraction, trimming)   [consistent case only]
 └─ Lemma 3.3 (hull inclusion + strict gain ⇒ no coherent model can make the change)
Theorem 4.1 (repair on E, with location clause) ← 2.1–2.3, 3.2, 3.3
Lemma 5.4 (changes guided at every world, on E) ← countable norming set
Theorem 5.7 (ranking; coverage of every target) ← 4.1, 3.3, 5.4
Part 6 (hull-closed and one-sided domains; finite worlds) ← location clause of 4.1, 5.7
```

---

## Part 1. Setting

### 1.1 Worlds, gambles, states

- **Worlds.** Ω is any nonempty set. It carries no topology and no σ-algebra.
- **Gambles.** The gamble space E is a linear subspace of ℓ∞(Ω) with the sup norm ‖h‖ = sup_Ω |h| and the pointwise order. We assume that E is closed, separable, and contains 𝟙. Remark 1.6 weakens the last condition to a gamble e with inf_Ω e > 0. With finitely many worlds, Ω = {1,…,n} and E = ℝⁿ.
- **States.** A *state* is a linear q: E → ℝ that is positive (h ≥ 0 ⇒ q(h) ≥ 0) and normalised (q(𝟙) = 1). S is the set of states, with the weak-* topology; δ_ω(h) = h(ω) is a state.
  - A *credal set* is a nonempty, weak-* closed, convex Q ⊆ S, hence compact.
  - With finitely many worlds, S = Δ.
- **Coherent sets.** For nonempty compact Q ⊆ S:
  - P_Q(h) := min_{q∈Q} q(h);
  - D_Q := {P_Q > 0};
  - C_Q := {P_Q ≥ 0}.
- **Convention.** D_∅ := E. This is the literal reading: "q(h) > 0 for all q ∈ ∅" holds for every h.

**Lemma 1.1 (states and lower expectations)** [refereed: IW66a, IW66b, REF66_iw].

- (a) Every state has norm 1. S is convex, weak-* compact and metrizable.
- (b) P_S(h) = inf_Ω h. In particular q(h) ≤ sup_Ω h for every state q.
- (c) P_Q is 1-Lipschitz, concave and positively homogeneous, and P_Q(h + t𝟙) = P_Q(h) + t. Consequently:
  - D_Q is an open convex cone;
  - D_S ⊆ D_Q;
  - D_Q contains no h with sup_Ω h ≤ 0;
  - D_{Q₁} ∩ D_{Q₂} = D_{conv(Q₁∪Q₂)}.
- (d) (1−τ)Q + τS is a credal set for 0 ≤ τ ≤ 1, and P_{(1−τ)Q+τS} = (1−τ)P_Q + τP_S.
- (e) For credal sets Q₁ and Q₂: if D_{Q₁} ⊆ D_{Q₂}, then Q₂ ⊆ Q₁. Convexity is needed here, since D_{Q₁} = D_{conv Q₁}.
- (f) **Countable norming set.** There is a countable Ω₀ ⊆ Ω with inf_{Ω₀} h = inf_Ω h and sup_{Ω₀} h = sup_Ω h for all h ∈ E. Every Ω′ ⊆ Ω that norms infima contains such an Ω₀.

*Proof.*
- (a) We have −‖h‖𝟙 ≤ h ≤ ‖h‖𝟙. So S is a weak-* closed subset of the dual unit ball. Apply Banach–Alaoglu. The dual ball of a separable space is metrizable.
- (b) Since δ_ω ∈ S, P_S(h) ≤ inf h. Also h − (inf h)𝟙 ≥ 0. Apply this to −h for the sup.
- (c) Each q has norm 1, so P_Q is 1-Lipschitz. The rest follows from (b), together with the fact that a linear map has the same minimum over Q₁ ∪ Q₂ as over its convex hull.
- (d) The set is a continuous image of Q × S. The minimum over a Minkowski sum is the sum of the minima.
- (e) Take k ∈ Q₂∖Q₁. Weak-* separation gives g ∈ E and c with q(g) > c > k(g) on Q₁. Put h := g − c𝟙.
- (f) Take a dense sequence (h_j) and points ω_{j,l} ∈ Ω′ with h_j(ω_{j,l}) < inf h_j + 1/l. Do the same for −h_j. ∎

### 1.2 The measure and the score

μ is a finite Borel measure on (E, ‖·‖). It may satisfy three conditions:

- **(M1) Finite first moment:** ∫‖h‖ dμ < ∞.
- **(M2) Null indifference boundaries:** μ{P_Q = 0} = 0 for every credal set Q. The instances used are Q = {q} (including δ_ω), Q = S, Q = Q_B, and convex hulls of finitely many credal sets.
- **(M3) Full support:** nonempty open sets have positive measure.

**Only (M1) and (M2) are used for the repair theorem, protection, the ranking and coverage on E.** (M3) serves only to identify models (Lemma 1.3(a)) and in the one-sided (LF) characterisation [refereed: RF67a S4, RF67b G4].

**Lemma 1.2 (existence)** [refereed: IW66a, IW66b, REF66_iw]. Fix ω₀ and put E₀ := {g : g(ω₀) = 0}. Let ν be a full-support Borel probability on E₀ with ∫‖g‖ dν < ∞; for example ν = Σ w_k δ_{g_k} with (g_k) dense and Σ w_k(1 + ‖g_k‖) < ∞. Let λ be an atomless full-support probability on ℝ with a first moment. Then the law of g + t𝟙 under ν ⊗ λ satisfies (M1)–(M3).

*Proof.* The map (g,t) ↦ g + t𝟙 is a linear homeomorphism. For each condition:
- Full support transfers to the product measure.
- ‖g + t𝟙‖ ≤ ‖g‖ + |t| gives (M1).
- {P_Q = 0} pulls back to {t = −P_Q(g)}, which is null by Fubini. This gives (M2). ∎

**Integrated payoff.** Under (M1), the identity is Bochner integrable. Put m(X) := ∫_X h dμ ∈ E. Every ℓ ∈ E* commutes with the integral, so m(X)(ω) = ∫_X h(ω) dμ and q(m(X)) = ∫_X q(h) dμ. The score of X at ω is m_ω(X) := m(X)(ω), and higher is better.

*Accuracy reading.* Put c_ω := ∫_{h(ω)>0} h(ω) dμ. Then c_ω − m_ω(X) is the payoff-weighted measure of X's wrong acceptances plus its silences on gambles that pay off at ω.

### 1.3 Models, coherent models, and sets versus classes

**Models.** A model is a Borel X ⊆ E, the gambles it accepts. Models that agree up to a μ-null set are identified. A model is **coherent** if it equals some D_Q a.e., with Q a credal set.

**Sets versus classes** [refereed: RF67a S1, RF67b row 16]. The following points make the distinction explicit.

1. **Class-invariance.** Every notion below depends only on μ-classes: m, Q_B, hull, the changes of Part 3 and their tests, guidance, and the ranking. For a fixed minimiser q*, the sets L and X₊ of Cor 2.3 depend on the representative of X only up to null sets.
2. **Coherence is a property of classes, not of raw sets.** A raw set can be literally incoherent yet coherent modulo μ. Two examples: D_Q together with any null set; or, for μ carried by lines g_k + ℝ𝟙, any set that agrees with D_Q on those lines.
3. **The classification depends on μ.** Mutually singular admissible measures classify the same raw set differently (Part 7).
4. **Representatives are always literal sets.** Every repair in Theorem 4.1 is a literal open set D_Q. Every target is the literal open set D_K. The inclusions N ⊆ hull(X∖N) and N ⊆ hull(X) or N ⊆ {q* > 0} in Theorem 4.1 hold as inclusions of sets.
5. **Coherent sets of desirable gambles (weak sense, Lemma 1.3(b)).** These are measurable only for the completion of μ. They enter as models through their Borel versions D_{Q_D}.

**Lemma 1.3 (identification)** [refereed: IW66a, IW66b, REF66_iw].
- (a) Assume (M3). If O is open and O ⊆ D_Q a.e., then O ⊆ D_Q. If D_{Q₁} = D_{Q₂} a.e., then Q₁ = Q₂. Without (M3) this can fail. For instance, if μ is carried by D_S ∪ (−D_S), then all D_Q are a.e. equal (RF67b row 19).
- (b) Assume (M2). Let D be a convex cone with 0 ∉ D that contains every h with inf h > 0. Call such a D a coherent set of desirable gambles *in the weak sense*. Walley's coherent sets, which must contain every nonzero h ≥ 0, form a strict subclass: D_{{e₁}} = {h₁ > 0} on ℝ² is weakly coherent but not Walley-coherent. Then:
  - Q_D := {q : q ≥ 0 on D} is a credal set;
  - D_{Q_D} ⊆ D ⊆ C_{Q_D};
  - so D = D_{Q_D} a.e., and boundary choices are invisible modulo μ.

  Conversely, every D_Q is a.e. equal to the Walley-coherent set D_Q ∪ {h ≥ 0, h ≠ 0}, since the difference lies in {P_Q = 0}. **Modulo μ, the weak and the Walley notions give the same classes.**

*Proof.*
- (a) O ∩ {P_Q < 0} is open and null, hence empty. Also h − η𝟙 ∈ O for small η > 0. Then apply Lemma 1.1(e).
- (b) This is the note's Prop "cdg":
  - D ⊇ D_S, so int D ≠ ∅;
  - the nonnegative functionals on D are multiples of states, and there is at least one, by Hahn–Banach;
  - by the bipolar theorem, cl D = C_{Q_D};
  - int cl D = int D;
  - {P_{Q_D} = 0} is null. ∎

### 1.4 Supporting states and the hull

For Borel B put Q_B := {q ∈ S : q(h) ≥ 0 for μ-a.e. h ∈ B}. These are the *supporting states* of B, and there may be none. Put hull(B) := D_{Q_B}. **A set with no supporting state has hull equal to E.** For null B, Q_B = S and hull(B) = D_S.

**Lemma 1.4 (hull lemma)** [refereed: IW66a A1–A3, IW66b §3.1; on E with possibly empty Q_B: RF67a S5, RF67b row 1 and §3.3].

- (a) Q_B is weak-* closed and convex. If B ⊆ B′ a.e., then Q_{B′} ⊆ Q_B.
- (b) If Q_B ≠ ∅, then P_{Q_B} ≥ 0 a.e. on B. Under (M2), B ⊆ hull(B) a.e.
- (c) For a credal set Q: B ⊆ D_Q a.e. ⇒ Q ⊆ Q_B ⇒ hull(B) ⊆ D_Q. Under (M2) the converse implications also hold, so hull(B) is the smallest coherent model containing B a.e., whenever some coherent model contains B a.e. The converses fail without (M2): take B ⊆ {q = 0} and Q = {q}.
- (d) "No coherent model contains B a.e." ⇒ Q_B = ∅ needs no condition. The converse uses (M2). When Q_B = ∅, hull(B) = E. E is not coherent, so in this case hull(B) is not "the smallest coherent model containing B".
- (e) If some Borel L ⊆ B a.e. has m(L) ≤ −η𝟙 for some η > 0, then Q_B = ∅.
- (f) Assume (M2). If some non-null Borel L ⊆ B a.e. has m_ω(L) ≤ 0 at every world, then Q_B = ∅.

*Proof.*
- (a) If q_j → q in Q_B and q(h) < 0, then q_j(h) < 0 for large j. Use sequences, since S is metrizable.
- (b) Take a dense sequence in Q_B. Then remove the null set {P_{Q_B} = 0}.
- (c) If q ∈ Q, then q(h) ≥ P_Q(h) > 0 on D_Q. Also Q ⊆ Q_B gives P_{Q_B} ≤ P_Q. For the converse, use B ⊆ hull(B) a.e., which is (b) under (M2).
- (d) If Q_B ≠ ∅, then under (M2) hull(B) is a coherent model containing B a.e. Conversely, a coherent D_Q ⊇ B a.e. gives ∅ ≠ Q ⊆ Q_B.
- (e) For q ∈ Q_L, we have q(m(L)) = ∫_L q dμ ≥ 0. But q(m(L)) ≤ sup_Ω m(L) < 0. Then use (a).
- (f) Let q ∈ Q_L. Then q ≥ 0 a.e. on L, and {q = 0} is null, so q > 0 a.e. on L. Hence q(m(L)) > 0, since L is non-null. But q is positive and m(L) ≤ 0, so q(m(L)) ≤ 0. ∎

### 1.5 Finite worlds as a special case

Take E = ℝⁿ, so S = Δ. Every finite μ with Lebesgue's null sets and ∫|h| dμ < ∞ satisfies (M1)–(M3). Lebesgue-measurable sets are a.e. Borel. Measures singular to Lebesgue measure and carried by lines g_k + ℝ𝟙 also qualify.

TS66's full-domain finite results are therefore the case E = ℝⁿ of Parts 4–5 [refereed: RF67a C1, RF67b row 21]. Lyapunov's theorem becomes a historical remark.

The following finite statements are **not** special cases, because they are domain or Carathéodory computations: (LF) on V₀, n = 2 sectors, and the density-point form of the test (Cor 6.3).

**Remark 1.5 (reweighting)** [refereed: REF67_out U1]. Let w: E → (0,∞) be Borel with ∫ w(1 + ‖h‖) dμ < ∞. Then ∫_X w(h)h(ω) dμ is the integrated payoff under μ_w := w·μ. This measure is finite, has μ's null sets, and satisfies (M1)–(M3). So positive common reweightings need no new construction.

Multiplying the score at each world ω by a constant c_ω > 0 leaves the ranking unchanged, because the ranking uses only signs of score differences. For the rescaled score, the *uniform* margin of Theorem 4.1 survives if inf_ω c_ω > 0. **No claim is made that other scores fail.**

**Remark 1.6 (order unit)** [refereed: IW66b §7.1, REF66_iw W5; on E: RF67a H2, RF67b row 22]. Suppose instead that some e ∈ E has inf_Ω e > 0. Then h ↦ h/e transports everything:
- the signs at each world;
- the states (normalised by q(e) = 1);
- the sets D_Q;
- the conditions (M1)–(M3);
- the coherent class.

Scores transform as m_ω = e(ω)·m̃_ω, and margins are multiplied by inf e. A world at which every gamble pays 0 makes every model undominated. The case c₀ remains open.

---

## Part 2. The minimax lemma

For Borel G let F_G := {f ∈ L∞(μ) : 0 ≤ f ≤ 𝟙_G a.e.}. These are the *weighted acceptance choices* inside G. Put T(f) := ∫ f(h) h dμ(h), so that T(𝟙_Y) = m(Y).

**Lemma 2.1 (minimax over weighted acceptance choices)** [refereed: IW66a B1–B8, IW66b §2.2–2.4 (for G = hull(X)); RF67a P1–P4, RF67b rows 2–3 and §2.2 (any Borel G and any x ∈ E)]. Assume (M1)–(M2). Let G be Borel and x ∈ E, and put

  v := max_{f∈F_G} min_{q∈S} q(T f − x) = min_{q∈S} ( ∫_G q(h)⁺ dμ − q(x) ).

- (a) Both optima exist, and they are equal.
- (b) For each state q, the maximiser of q(T f) over F_G is unique a.e. and equals 𝟙_{G∩{q>0}}. **The optimal weighted choice is an ordinary set.**
- (c) Let q* attain the minimum, and put N* := G ∩ {q* > 0}. Then every maximiser f equals 𝟙_{N*} a.e. Also q(m(N*) − x) ≥ v for every state q, and in particular at every world.

*Proof.*
1. **Compactness.** F_G is weak-* compact and convex in L∞ = (L¹)*, because μ is finite.
2. **Continuity.** T is weak-*-to-norm continuous, as a uniform limit of finite-rank maps T_n f = ∫ f s_n dμ with ∫‖h − s_n‖ dμ < 1/n. So Z := T(F_G) is norm-compact and convex.
3. **Minimax.** Sion's theorem applies to Φ(q,z) := q(z − x) on S × Z.
4. **Attainment.**
   - z ↦ inf_Ω(z − x) is 1-Lipschitz on the compact set Z.
   - q ↦ max_Z Φ(q,·) is lower semicontinuous on the compact set S.
5. **The formula.** q(T f) = ∫ f q dμ ≤ ∫_G q⁺ dμ. Equality holds iff f = 𝟙 a.e. on G ∩ {q > 0} and f = 0 a.e. on G ∩ {q < 0}. The set {q = 0} is null. This proves (b) and the formula for v.
6. **The saddle point.** Let f* be a maximiser and z* = T f*. Then

   v = min_q Φ(q, z*) ≤ Φ(q*, z*) ≤ max_z Φ(q*, z) = v.

   So f* maximises q*(T·), and f* = 𝟙_{N*} by (b). Hence q(m(N*) − x) ≥ min_q Φ(q, z*) = v. ∎

**Corollary 2.2 (consistent case)** [refereed: IW66a/b; on E: RF67a T1, RF67b row 7]. Let Q_X ≠ ∅, and take G := hull(X) and x := m(X). Then:
- X ⊆ G a.e., so v ≥ 0;
- v > 0 iff X is incoherent;
- for every minimiser q*, N₀ := hull(X) ∩ {q* > 0} = D_{conv(Q_X ∪ {q*})} is coherent, and q(m(N₀) − m(X)) ≥ v for all q.

*Proof.*
- If v = 0, then 𝟙_X maximises q*(T·). So X = G ∩ {q* > 0} a.e., which is coherent.
- If X = D_Q a.e., then G = X a.e. by Lemma 1.4(c). So the bracket in the formula for v vanishes at any q ∈ Q_X. ∎

**Corollary 2.3 (the uniformly losing part)** [refereed: RF67a P1–P6, RF67b rows 2–4, §2.1, §3.3; finite form: TS66 Lemma E, REF66_ts]. Assume (M1)–(M2), and let X be a model.

- (a) v := min_{q∈S} ∫_X q(h)⁻ dμ is attained, and v > 0 ⟺ Q_X = ∅.
- (b) Suppose Q_X = ∅, and let q* be any minimiser. Put L := X ∩ {q* < 0} and X₊ := X ∩ {q* > 0}. Then:
  - m(X₊) − m(X) = −m(L);
  - q(m(L)) ≤ −v for **every state** q, equivalently m_ω(L) ≤ −v at every world;
  - q* ∈ Q_{X₊};
  - Q_L = ∅.
- (c) The following are equivalent:
  - Q_X = ∅;
  - some non-null Borel L ⊆ X has m_ω(L) ≤ 0 at every world;
  - some Borel L ⊆ X has m(L) ≤ −η𝟙 for some η > 0.

A set of commitments is **inconsistent** (has no supporting state) exactly when part of it loses in integrated payoff at every world.

*Proof.*
- (a) Apply Lemma 2.1 with G := X and x := m(X). The bracket is ∫_X q⁻ dμ, which vanishes iff q ∈ Q_X.
- (b) By Lemma 2.1(c), N* = X₊. The set X ∩ {q* = 0} is null, so m(X₊) − m(X) = −m(L).
  - The bound at worlds is the case q = δ_ω. It is equivalent to the bound at every state, by Lemma 1.1(b).
  - q* > 0 pointwise on X₊, so q* ∈ Q_{X₊}.
  - Q_L = ∅ by Lemma 1.4(e): a state applied to the Bochner integral m(L) would be both ≥ 0 and ≤ −v.
- (c) The first implies the third by (b). The third implies the second trivially. The second implies the first by Lemma 1.4(f). ∎

*Remarks.*
- Any minimiser q* works. q* need not be an evaluation. For X = E on E = {a + bω} over (0,1], q* is the "limit at 0" state (RF67b row 23).
- Any state q with sup_Ω m(X ∩ {q < 0}) < 0 can serve in place of q* (REF66_ts G2).
- No Lyapunov theorem and no non-atomicity are used.

---

## Part 3. Trimming, and when a change is closed to coherent models

**Lemma 3.1 (contraction)** [refereed: REF65_hA Lemma S; IW66a D1; IW66b §2.6]. Let Q_X ≠ ∅ and P := P_{Q_X}. If q ∈ S, c ≥ 0 and q(h) ≥ −c·P(h) for a.e. h ∈ X, then q ∈ Q_X.

*Proof.*
- Put T(q′) := (q + cq′)/(1 + c). It maps the closed set Q_X into itself, because (q + cq′)(h) ≥ q(h) + cP(h) ≥ 0 a.e. on X.
- Tᵏq′ − q = (c/(1+c))ᵏ(q′ − q) → 0 in norm. ∎

**Lemma 3.2 (trimming)** [refereed: REF65_hA Cor S; IW66a D2; IW66b §2.6]. Let Q_X ≠ ∅, 0 < τ < 1, and Q_τ := (1−τ)Q_X + τS. For every Borel N ⊆ D_{Q_τ}, Q_{X∖N} = Q_X, and so hull(X∖N) = hull(X).

*Proof.* Let q ∈ Q_{X∖N} and c := (1−τ)/τ.
- On X ∩ N: P_{Q_τ}(h) > 0 gives q(h) ≥ P_S(h) > −cP(h).
- On X∖N, a.e.: q(h) ≥ 0 ≥ −cP(h), because P ≥ 0 a.e. on X (Lemma 1.4(b)).

Then apply Lemma 3.1. ∎

Cutting from X only gambles that lie well inside its hull leaves the hull unchanged. **Only the consistent case uses Lemmas 3.1–3.2.**

**Definition (changes).** The *change from Y to X* adds A := X∖Y and removes B := Y∖X.
- It is **open to** a model Z if B ⊆ Z a.e. and A ∩ Z is null. Then Z can make the change, with result (Z∖B) ∪ A.
- It is **closed to coherent models** if it is open to no coherent model.

**Lemma 3.3 (hull inclusion plus a strict gain)** [refereed: RF67b Prop R and §3.3 (part (a)); RF67a §2.2 (parts (b)–(c)); first stated here as (b)]. Let X and N be models with N ⊆ hull(X∖N) a.e., where hull(B) = E when Q_B = ∅. N need not be coherent.

- (a) Assume (M2). If m_ω(N) > m_ω(X) at **every** world, the change from X to N is closed to coherent models.
- (b) Without (M2), the same holds if the gain is uniform, that is, m(N) − m(X) ≥ η𝟙 for some η > 0. (M1) is still needed, so that m is defined.
- (c) Assume (M2). If the change is closed and Q_{X∖N} ≠ ∅, then μ(N∖X) > 0.

*Proof.*
1. Put A := N∖X and B := X∖N. Suppose the change is open to D_Q.
2. Then Q ⊆ Q_B, so Q_B ≠ ∅, and N ⊆ hull(B) ⊆ D_Q a.e. Hence A ⊆ D_Q a.e. Since A ∩ D_Q is null, A is null. So m(N) − m(X) = −m(B).
3. For (a): m(B) < 0 at every world, so B is non-null. Lemma 1.4(f) then gives Q_B = ∅, a contradiction.
4. For (b): take q ∈ Q. Then q(m(B)) = ∫_B q dμ ≥ 0, but positivity gives q(m(B)) ≤ −η.
5. For (c): if A were null with Q_B ≠ ∅, the change would be open to hull(B). That set is coherent and contains B a.e. (Lemma 1.4(b)). ∎

*Which version to keep.* Under the standing assumption (M2), (a) is the weakest hypothesis that has been proved: a strict gain at every world, not necessarily uniform. RF67a remarks that a pointwise margin does not suffice "for this argument". That remark concerns (b), which does not use (M2). RF67b's argument through Lemma 1.4(f) needs (M2). There is no conflict. The repairs of Theorem 4.1 satisfy both versions.

**Remark 3.4 (neither hypothesis can be dropped).**
- **The gain alone is not enough** [refereed: REF65_hA E1b, E9; REF66_ts §3.3]. The untrimmed N₀ of Cor 2.2 improves uniformly, yet on exact examples its change is open to the coherent model hull(X∖N₀).
- **The hull inclusion alone is not enough** [refereed: REF67_out U2–U3 and §2.1; CHECKED numerically]. The general family:
  - Take X = D_Q ∪ B and N = D_Q, with B Borel, non-null, disjoint from D_Q, and ∅ ≠ Q_B ⊆ Q.
  - Then N = D_Q ⊆ D_{Q_B} = hull(B) = hull(X∖N), literally, by Lemma 1.1(e).
  - The change (∅, B) is open to the coherent model hull(B).
  - This is the precise condition. If instead Q ⊆ Q_B, then (M2) gives B ⊆ D_Q a.e., so B would be null. In particular Q_B = Q is impossible, and the inclusion Q ⊆ Q_B in RF67b §3.2 is reversed. (This corrects revision 2's flag.)
- **An incoherent instance** [refereed: REF67_out §2.1, CHECKED]. Take n = 2, any μ with full support (say Gaussian), Q = Δ and N = int ℝ²₊. Put B′ := {h₁ + h₂ > 0, min(h₁,h₂) ≤ 0, |h| > 1} and X′ := N ∪ B′.
  - B′ contains neighbourhoods of (−t, t + s) and (t + s, −t) for all large t, so Q_{B′} = {(½,½)} ⊆ Δ.
  - So hull(X′∖N) = {h₁ + h₂ > 0} ⊇ N.
  - X′ is incoherent: its hull is {h₁ + h₂ > 0}, but it misses the non-null set {h₁ + h₂ > 0, min(h₁,h₂) ≤ 0, |h| ≤ 1}.
  - The change (∅, B′) is open to the coherent model {h₁ + h₂ > 0}.
  - Its gain −m(B′) is negative at both worlds, since (½,½)·m(B′) > 0.
  - Dropping |h| > 1 gives the coherent case X = {h₁ + h₂ > 0}, where the change is trivially open to X itself.

This is the precise sense in which the score gain is essential (AUDIT_r67_message2 §2).

---

## Part 4. The repair theorem

**Theorem 4.1 (repair)** [refereed: RF67a (Theorem; T1–T11; §2.2–§2.3), RF67b (rows 5–12, 20; §2.2; §3.5), REF67_out C17–C19. The consistent-case proof is the note's refereed Thm 7.7, run on E with its Step C replaced by Lemma 3.3(c); RF67a §2.2 records that replacement]. Assume (M1)–(M2). Let X be an incoherent model. Then there are a credal set Q and η > 0 such that the literal open set N := D_Q satisfies the following.

1. **Uniform improvement.** q(m(N) − m(X)) ≥ η for every state q. In particular m_ω(N) ≥ m_ω(X) + η at every world.
2. **All of N follows from what is abandoned.** N ⊆ hull(X∖N), as sets: every gamble of N, not only the newly accepted ones. Here hull(X∖N) = E when X∖N has no supporting state.
   - In the consistent case this inclusion carries content: everything N accepts is implied, under coherence, by commitments that X abandons.
   - In the inconsistent case it holds *because* the abandoned commitments are inconsistent: hull(X∖N) = E. The informative facts there are Q_{X∖N} = ∅ and the location N ⊆ hull(X₊).
3. **Location.**
   - If Q_X ≠ ∅: N ⊆ hull(X), hull(X∖N) = hull(X), and μ(N∖X) > 0.
   - If Q_X = ∅: N ⊆ hull(X₊) ⊆ {q* > 0}, with q*, X₊ and L as in Cor 2.3. Moreover L ⊆ X∖N, Q_{X∖N} = ∅, hull(X∖N) = E, and η ≥ v.
4. **No coherent model can make this change.** The change from X to N is closed to coherent models. This follows from 1, 2 and Lemma 3.3.

*Proof, consistent case (Q_X ≠ ∅): optimise within the hull, then trim.*
1. **Region of optimisation.** G := hull(X) = D_{Q_X}. This is the one-sided domain D_{K′} with K′ := Q_X, but no element of K′ is needed below. By Lemma 1.4(b), X ⊆ G a.e. and P := P_{Q_X} ≥ 0 a.e. on X.
2. Cor 2.2 gives v > 0, q*, and N₀ := D_{conv(Q_X∪{q*})} ⊆ G, with q(m(N₀) − m(X)) ≥ v.
3. Put N_τ := N₀ ∩ D_{Q_τ} = D_{conv(Q_X ∪ {q*} ∪ Q_τ)}.
4. P_{Q_τ} = P − τ(P − P_S) is non-increasing in τ, and P > 0 on N₀. So N_τ ↑ N₀ as τ ↓ 0.
5. By dominated convergence, ‖m(N₀) − m(N_τ)‖ ≤ ∫_{N₀∖N_τ}‖h‖ dμ → 0. Fix τ with this at most v/2, and put N := N_τ. Then q(m(N) − m(X)) ≥ v/2 =: η, which is item 1.
6. Lemma 3.2 gives hull(X∖N) = hull(X) = G ⊇ N₀ ⊇ N, as sets. This is items 2 and 3.
7. μ(N∖X) > 0 follows from Lemma 3.3(c), since Q_{X∖N} = Q_X ≠ ∅.

One could instead invoke Thm 7.7 with K′ := Q_X and U′ := hull(X), or with K′ := {q₀} and U′ := D_{q₀} for some q₀ ∈ Q_X, applied to X ∩ U′ [RF67a T1; RF67b row 7]. The direct proof makes this unnecessary.

*Proof, inconsistent case (Q_X = ∅): remove the uniformly losing part, using Lemma 2.1 once more.* [refereed: RF67a §2.3–2.4 (CHECKED 48/48), RF67b §2.2 and §3.5, REF67_out C18; finite form: TS66 Thm 3.4, REF66_ts]
1. Cor 2.3 gives q*, v > 0, L and X₊, with q(m(X₊) − m(X)) ≥ v for all q, and q* ∈ Q_{X₊}.
2. **Region of optimisation.** G₁ := hull(X₊) = D_{Q_{X₊}}.
   - Since q* ∈ Q_{X₊}, G₁ ⊆ D_{q*} = {q* > 0}.
   - By Lemma 1.4(b), X₊ ⊆ G₁ a.e.
   - If X₊ is null, then G₁ = D_S.
3. **Apply Lemma 2.1** with G := G₁ and x := m(X). Note that x need not lie in T(F_{G₁}).
   - Since 𝟙_{X₊} ∈ F_{G₁}, the value satisfies v₁ ≥ min_q q(m(X₊) − m(X)) ≥ v > 0.
   - Let π* attain the minimum, and put N := G₁ ∩ {π* > 0} = D_{conv(Q_{X₊}∪{π*})}. This set is coherent and literally open.
   - q(m(N) − m(X)) ≥ v₁ =: η ≥ v for every state q. This is item 1.
4. **The losing part is removed.** N ⊆ G₁ ⊆ {q* > 0}, so N ∩ L = ∅ and L ⊆ X∖N, literally. By Lemma 1.4(a),(e), Q_{X∖N} ⊆ Q_L = ∅. Hence hull(X∖N) = E ⊇ N, which is item 2.
5. **Location.** N ⊆ G₁ = hull(X₊), which is item 3. ∎

*Remark (a half-space instead of hull(X₊))* [refereed: RF67a §2.3; RF67b §2.2]. On E one may instead take G₁ := D_{q*} = {q* > 0}, the one-sided domain with K′ := {q*}.
- Steps 1–4 hold verbatim, with X₊ ⊆ G₁ literally.
- The repair is the **two-prior** model N = D_{conv{q*,π*}}.
- The location clause weakens to N ⊆ {q* > 0}. N ⊆ hull(X₊) can fail here, because it would need Q_{X₊} ⊆ conv{q*,π*} (REF67_out C18).
- So this choice serves on E, but not for Cor 6.1.

*What this proof buys.*
- It needs no trimming and no contraction lemma.
- It needs no split on whether X₊ is coherent, incoherent or null.
- The repair is explicit, and the margin is at least the losing margin v directly.
- The architecture becomes literally "one minimax lemma, two uses".
- The audit's argument is also correct [RF67a T3–T10; RF67b rows 5–6, §2.2]: take N := hull(X₊) if X₊ is coherent, else repair X₊ by the consistent case. Its only extra yield is μ(N∖X) > 0 when X₊ is incoherent, which nothing uses.

*Remarks.*
- **Degenerate cases** [refereed: RF67a T6, B4; RF67b row 5; REF67_out C19].
  - X₊ null: N ⊆ G₁ = D_S.
  - N∖X null: the change only removes, and it is closed because Q_{X∖N} = ∅.
  - X containing both h and −h, for example X = E: then N = hull({q* > 0}), which is D_{q*} under (M3) and a.e. equal to it otherwise. The change is (∅, {q* < 0}) up to null sets [RF67a B1; RF67b row 23].
- **Countable unions of thin pieces** [RF67b row 24]. If X = ⋃_n X_n, then Q_X = ⋂_n Q_{X₁∪…∪X_n}, a decreasing intersection of compact sets. So Q_X = ∅ is already witnessed by a finite sub-union. However thinly the sure loss is spread, v > 0 comes from Cor 2.3(a).
- **The obvious one-step repair can fail** [refereed: REF66_ts §3.3, G8]. At the minimax prior, the full-domain Brier-optimal half-space can give a change that is open to a coherent model. So the case distinction does real work.
- **The two cases reflect a real distinction.**
  - Consistent case: the change replaces part of X by consequences of what it gives up.
  - Inconsistent case: the change discards commitments that already lose at every world.

---

## Part 5. The ranking (corollary)

**Lemma 5.1 (test for closedness)** [refereed: SR66 S1, IW66b §3.1; on E: RF67a S5, RF67b G1]. Assume (M2). The change adding A and removing B is closed to coherent models iff

  Q_B = ∅, or μ(A ∩ hull(B)) > 0.

The convention hull = E alone would misclassify the change (∅, B) when Q_B = ∅; that change is closed. Joining a closed change to a change with disjoint support gives a closed change.

*Proof.*
- If Q_B = ∅, no coherent model contains B a.e.
- Otherwise, hull(B) is coherent and contains B a.e. If the change is open to D_Q, then hull(B) ⊆ D_Q.
- Joining: if the joined change is open to Z, so is each of its parts. ∎

**Definition 5.2 (the ranking).** At world ω, X ⪯_ω Y iff the change from Y to X either:
- is **guided by ω**, meaning that it adds only gambles with h(ω) > 0 and removes only gambles with h(ω) < 0, a.e.; or
- is **closed to coherent models** and m_ω(X) > m_ω(Y).

**Accept guidance, or a strictly score-improving change that no coherent model can make.**

**Proposition 5.3 (structure)** [refereed: SR66 P1–P5, IW66a T1–T3, IW66b §3.2; on E: RF67a E5–E6, RF67b row 15].
- (a) Reflexivity. A.e.-equal models are tied. **Independence:** X ⪯_ω Y depends only on (X∖Y, Y∖X) modulo null sets.
- (b) If X ⪯_ω Y and X ≠ Y a.e., then m_ω(X) > m_ω(Y). Hence:
  - distinct models are never tied;
  - **no strict reversal of a two-step chain (TC)**: A ⪯ B ⪯ C never gives C ≺ A;
  - **acyclicity (finite-chain consistency)**: no finite chain A₀ ⪯ … ⪯ A_k gives A_k ≺ A₀, and every cycle consists of a.e.-equal models;
  - **strict guidance**.
- (c) **Disjoint additivity.**
- (d) **The ranking is not transitive** (Example 5.9).

*Proof.*
- (a) The null change is guided.
- (b) A non-null change guided by ω has increment ∫_A |h(ω)| + ∫_B |h(ω)| > 0. The integrand is positive a.e. on the non-null set A ∪ B, by the strict inequalities in "guided". A closed change is accepted only with a positive increment. Chains then telescope.
- (c) Guided changes join to guided changes. A closed change joined with another change stays closed (Lemma 5.1), and the increments add, one of them positive and the other nonnegative. ∎

**Lemma 5.4 (changes guided at every world, on E)** [refereed: RF67a E1–E4, RF67b §3.1]. Assume (M2), and let Ω′ ⊆ Ω norm infima. Suppose the change (A,B) is guided by every ω ∈ Ω′. Then:
- A ⊆ D_S a.e.;
- B ⊆ {h : sup_Ω h ≤ 0} a.e.;
- the change is guided by every ω ∈ Ω;
- if the change is non-null, it is closed to coherent models.

On E, **B may be non-null.**

*Proof.*
1. **Reduce to countably many worlds.** Take a countable Ω₀ ⊆ Ω′ norming infima and suprema (Lemma 1.1(f)). Off countably many null sets, h ∈ A has inf_Ω h ≥ 0, and h ∈ B has sup_Ω h ≤ 0.
2. **The added part.** Remove the null set {P_S = 0}.
3. **Guidance at every world.** A ⊆ D_S ⊆ {h(ω) > 0}. Also B ∩ {h(ω) ≥ 0} ⊆ {h(ω) = 0}, which is null.
4. **Closedness.**
   - If B is non-null, no D_Q contains B a.e., because D_Q contains no h with sup h ≤ 0.
   - If B is null, then A ⊆ D_S ⊆ D_Q is non-null. ∎

*The protection sentence, corrected* [RF67a E3; RF67b P2]. A change guided at every world adds gambles with inf h > 0 a.e., by μ{P_S = 0} = 0. It removes gambles that are **nowhere positive**, with sup h ≤ 0. Every coherent model contains the former and excludes the latter.

The removed gambles **need not be uniformly negative a.e.** Counterexample: take E = C[0,1] and μ := μ_std + the law of −(ω − s)², with s uniform. This μ satisfies (M1)–(M3), yet μ{sup h = 0} ≥ 1. Removing all these gambles is guided at every world, and harmless.

μ{P_S = 0} = 0 is essential: without it, guidance alone strictly dominates a coherent model (the note's Example "PS").

**Proposition 5.5 (protection)** [refereed: RF67a E1–E2, RF67b §3.1]. No coherent model has a weak dominator other than itself.

*Proof.*
1. Let C = D_Q a.e., and let Y weakly dominate C. The change from C to Y is open to C, so it is accepted at every world only as guidance.
2. By Lemma 5.4, Y∖C ⊆ D_S ⊆ D_Q a.e. Since Y∖C misses C, it is null.
3. Also C∖Y ⊆ D_Q ∩ {sup h ≤ 0} = ∅ a.e. ∎

**Proposition 5.6 (dominance is always strict)** [refereed: REF66_un Prop 3.6, SR66 X2; on E: RF67a (Theorem), RF67b row 15]. For Y ≠ X a.e., the following are equivalent:
- (i) Y weakly dominates X;
- (ii) Y dominates X;
- (iii) Y ≺_ω X at every ω;
- (iv) the change from X to Y is closed to coherent models, and m_ω(Y) > m_ω(X) at every ω.

*Proof.*
- (iii) ⇒ (ii) ⇒ (i): immediate from the definitions.
- (i) ⇒ (iv): every increment is positive by Prop 5.3(b). If the change were open to some coherent model, it would be accepted everywhere only as guidance, and then Lemma 5.4 makes it closed.
- (iv) ⇒ (iii): the reverse change has negative increments. ∎

**Theorem 5.7 (main application theorem)** [refereed: RF67a (Theorem; S2–S4), RF67b (rows 15, 17–19)]. Assume **(M1)–(M2) only**. On all models of E, the ranking has the following properties.

- (a) The undominated models are exactly the coherent models.
- (b) Every incoherent X is strictly dominated by an undominated coherent N = D_Q. This N improves on X uniformly, at every state, and satisfies N ⊆ hull(X∖N).
- (c) Every model is weakly dominated by an undominated coherent one (W). Every undominated model is coherent (GC). Every incoherent model is dominated by an undominated coherent one (ID).
- (d) Strong closure under ties (C): a model tied with a coherent model at one world equals it.
- (e) **Literal (LF) at every target:** the open set E contains ∂D_K∖{0}, and every Borel X is a model of E.
- (f) For **every** credal set K, the ranking covers D_K. This includes precise targets (even states that are not evaluations), finitely generated targets, lower-dimensional targets, boundary targets, and K = S. **One ranking covers them all.**

*Proof.*
- (b): Theorem 4.1, Prop 5.6 and Prop 5.5.
- (a): Prop 5.5 together with (b).
- (c) and (d): from (a), (b) and Prop 5.3(b).
- (e): trivial.
- (f): D_K is a model and undominated by Prop 5.5. ∎

**Full support.** Adding (M3) makes distinct credal sets give distinct models, so the undominated classes correspond bijectively to credal sets. It adds nothing to (a)–(f).

**World sets** [refereed: REF66_iw §2.3]. Lemma 5.4 and Prop 5.5 allow any set of worlds Ω′ that norms infima. So the undominated set is the same for Ω and for a countable norming Ω₀. The dominance relation itself can differ. On E = span{1, ω, ω²} over [0,1], with ω* ∉ Ω₀, some closed change has m(r) = β(ω − ω*)². It is strictly improving at every world of Ω₀, but not at ω*.

**Example 5.8 (dominance need not be uniform)** [refereed: REF66_iw §2.1; on E: RF67a]. Take Ω = (0,1], E = {a + bω}, and μ Gaussian on the coefficients. Then some closed change has m(r) = βω. The resulting dominance is strict at every world, with infimum gain 0. Every *repair* of Theorem 4.1 is nonetheless uniform.

**Example 5.9 (not transitive, on the full domain ℝ²)** [refereed: RF67b row 15; CHECKED numerically, `rf67b_py/intransitive_full.out`]. Take E = ℝ² with Gaussian μ. Let A be the ball of radius 0.1 about (1,−1). Let A′ := A₁ ∪ A₂, with A₁ the ball of radius 0.3 about (1.5,−0.5) and A₂ the ball of radius 0.1 about (−1,−0.5). At world 1:

- **A′ ⪯₁ A.** The change adds A′ and removes A. It is closed to coherent models, because A₁ ⊆ hull(A). Its increment is m₁(A′) − m₁(A) ≈ 0.0145 > 0.
- **A ⪯₁ ∅.** This is guided.
- **A′ ⪯₁ ∅ fails.** A₂ has h₁ < 0, so the change is not guided. It is open to the coherent model D_{e₂} = {h₂ > 0}, which misses A′.

---

## Part 6. Corollaries for restricted domains

The restricted-domain results below are **restrictions** of Theorem 4.1 through its location clause.

A domain is a Borel U ⊆ E.
- Models on U are the Borel X ⊆ U modulo μ.
- The coherent models on U are the coherent D_Q with D_Q ⊆ U a.e.
- The ranking on U uses "closed to coherent models on U".
- U is **closed under coherent hulls** if hull(B) ⊆ U a.e. for every Borel B ⊆ U with Q_B ≠ ∅. Taking B = ∅ shows that D_S ⊆ U a.e.
- **One-sided** (the single definition used throughout, in finite and in infinite dimensions): V is one-sided if no nonempty open O has both O ⊆ V a.e. and −O ⊆ V a.e. This depends only on the μ-class of V. Every D_{K′} is one-sided under (M3), since D_{K′} ∩ (−D_{K′}) = ∅. In finite dimensions with Lebesgue null sets, this is implied by "V ∩ (−V) is null", and it is strictly weaker [refereed: REF66_iw §3].

**Corollary 6.1 (domains closed under coherent hulls)** [refereed: RF67a C3, §2.4; RF67b §3.5; finite: TS66 §3–5, REF66_ts]. Assume (M1)–(M2), and let U be closed under coherent hulls. Then:

- (a) For changes between models on U, closed to coherent models on U ⟺ closed to all coherent models.
- (b) Every incoherent model X on U has a repair N as in Theorem 4.1 with N ⊆ U a.e. As a model on U, use N ∩ U, which is a.e. equal to N.
- (c) All of Part 5 holds on U, with "coherent on U" in place of "coherent". In particular, the undominated models are the coherent models on U.
- (d) The ranking covers K ⟺ D_K ⊆ U a.e. and (LF) holds at D_K. Equivalently, some open O ⊇ ∂D_K∖{0} has O ⊆ U a.e. Every ranking that covers K needs both conditions, so **this ranking is a universal cover on U.**

*Proof.*
- (a) Suppose the change is open to D_Q. Then Q_B ≠ ∅, and the change is open to hull(B). That set is coherent, lies in U a.e., and contains B a.e.
- (b) By the location clause:
  - if Q_X ≠ ∅, then N ⊆ hull(X) ⊆ U a.e.;
  - if Q_X = ∅, then N ⊆ hull(X₊) ⊆ U a.e., because X₊ ⊆ U and q* ∈ Q_{X₊}. This includes X₊ null, where hull(∅) = D_S ⊆ U.
- (c) Lemma 5.4 and Prop 5.5 do not use the domain.
- (d) For "⇒", test (LF) with D_K ∪ O. Neither direction needs (M3). ∎

*Examples.*
- E; D_{K′}; and every U ⊇ {h : sup_Ω h > 0} a.e., since D_Q lies there [refereed: RF67a C3, RF67b §3.5].
- D_{K′} ∪ F with F Borel and F ⊆ {sup h ≤ 0} [refereed: REF67_out U4; infinite-dimensional form of the refereed TS66 Prop 3.2(b), REF66_ts 7b]. *Proof.*
  1. Let B ⊆ U be Borel with Q_B ∋ q.
  2. Then q ≥ 0 a.e. on B, while q(h) ≤ sup h ≤ 0 on F. So q = 0 a.e. on B ∩ F.
  3. By (M2), {q = 0} is null, so B ∩ F is null and B ⊆ D_{K′} a.e.
  4. Hence K′ ⊆ Q_B, and hull(B) = D_{Q_B} ⊆ D_{K′} ⊆ U.
- For n = 2, every domain admitting a ranking with strict guidance and global coherence [refereed: REF66_ts 7c].
- Exact (LF) conditions on general domains closed under coherent hulls in infinite dimensions have **not** been checked (RF67a C3).

**Corollary 6.2 (one-sided domains D_{K′})** [dominance part: a restriction of Theorem 4.1, refereed: RF67a C2, RF67b row 20; (LF) part: refereed: IW66a P1–P2, IW66b §6.2, REF66_iw]. Let U := D_{K′}. Every model on U has Q_X ⊇ K′ ≠ ∅, so only the consistent case arises, and N ⊆ hull(X) ⊆ U. The refereed Theorem 7.9 of the note is thereby recovered.

The (LF) characterisation is a separate domain statement and uses (M3).

- **(a) Exact (LF), any E.** D_K ∈ M_U and (LF) at D_K ⟺ K′ ⊆ K and every k ∈ K′ has k(h) > 0 for all h ∈ C_K∖{0}. The ranking covers exactly these K, and it is a universal cover on U.
- **(b) Finite worlds.** The condition reads: K full-dimensional and K′ ⊆ relint K.
- **(c) Infinite dimensions.** Write K_⊥ := {h : k(h) = 0 ∀k ∈ K}.
  - If K_⊥ ≠ {0}, (LF) fails on every one-sided domain.
  - So when E is infinite-dimensional, every precise and finitely generated K is excluded.
  - If K_⊥ = {0}, K is covered on D_{{k₀}} with k₀ := Σ2⁻ʲk_j, for (k_j) dense in K.
- **(d) Example.** On C(Ω), Ω infinite compact metric, the contamination (1−ε){p} + εS (0 < ε ≤ 1) is covered on {p > 0} when p has full support. For any p, it is covered on D_{{(1−ε)p+εr}} with r of full support.

*Proof of (a).*
- **"⇐".** ∂D_K ⊆ C_K, and the minimum over K′ is attained. So ∂D_K∖{0} ⊆ U, and we take the open set U.
- **"⇒".** Lemmas 1.3(a) and 1.1(e) give K′ ⊆ K, and testing (LF) gives N ⊆ U. Suppose k(h) = 0 for some k ∈ K′ and h ∈ C_K∖{0}. Then h ∈ ∂D_K ⊆ U, a contradiction.

*Proof of (b)* [refereed: note Lemma "LF"(b); covering paper Lemma "fulldim"(c),(d)]. For finite n we show that "k(h) > 0 for all h ∈ C_K∖{0}" ⟺ "K is full-dimensional and k ∈ relint K".
- **"⇐".** Let k ∈ relint K, h ∈ C_K∖{0}, and suppose k·h = 0. Moving k in every direction d with 𝟙·d = 0 stays in K, so d·h = 0 for all such d. Hence h = c𝟙 with c = k·h = 0, a contradiction.
- **"⇒".** If K is not full-dimensional, some h ≠ 0 has k·h = 0 on K. If k ∈ rbd K, a supporting hyperplane at k gives h ∈ C_K∖{0} with k·h = 0.

*Proof of (c).* Each 0 ≠ h ∈ K_⊥ gives ±h ∈ ∂D_K, so (LF) puts balls about both h and −h into V a.e. ∎

**Corollary 6.3 (finite worlds)** [refereed: TS66, REF66_ts, SR66; (a) as the case E = ℝⁿ of Thm 5.7: RF67a C1, RF67b row 21; hypotheses and (e): REF67_out C31, U6, §2.3]. Let E = ℝⁿ.
- **(a)** needs only (M1)–(M2).
- **(b)–(e)** assume that μ is finite, has the null sets of Lebesgue measure, and has ∫|h| dμ < ∞; this implies (M1)–(M3). Parts (b)–(d) are (LF) characterisations, which need full support. Part (e) uses Lebesgue density points.
- "One-sided" in (d) is the single definition of Part 6.

- (a) On ℝⁿ, one ranking covers every credal set.
- (b) On V₀ = ℝⁿ∖(−ℝⁿ₊), it covers exactly the K that meet relint Δ.
- (c) On D_{K′}, it covers exactly the full-dimensional K with K′ ⊆ relint K.
- (d) Lower-dimensional K are covered on no one-sided domain.
- (e) **Geometric form of the test** [refereed pieces: note Cor "witness"; TS66 Lemma 2.1(b),(c), REF66_ts 4e]. A change is closed iff one of the following holds:
  - some nonnegative combination of at most n density points of B is ≪ 0; or
  - some density point a of A has a − Σ_{j≤n} t_j b_j ≫ 0, with b_j density points of B and t_j ≥ 0.

  So a change is closed exactly when what it removes is a sure loss in combination, or when some added gamble beats a combination of removed ones at every world.

  *Proof of (e)* [REF67_out §2.3].
  1. Q_B = {q ∈ Δ : q·b ≥ 0 for all density points b of B}.
  2. Q_B = ∅ ⟺ cone(B_d) meets the open cone −ℝⁿ₊₊. For "⇐": if they are disjoint, a separating q ≠ 0 satisfies q ≥ 0 and q ≥ 0 on B_d, so q/(𝟙·q) ∈ Q_B. Conic Carathéodory gives at most n points. This is the first disjunct.
  3. When Q_B ≠ ∅, hull(B) = cone(B_d) + ℝⁿ₊₊, by the note's hull formula; its proof does not use the domain. This set is open. So μ(A ∩ hull B) > 0 ⟺ some density point a of A lies in it ⟺ the second disjunct, by Carathéodory again.
  4. Lemma 5.1 then assembles the two. When Q_B = ∅, the second disjunct is subsumed by the first. ∎

(b), (d) and (e) are finite domain statements, not special cases of Thm 5.7.

---

## Part 7. Scope statement (about half a page)

**Worlds versus gambles.**
- Ω is arbitrary.
- E must be a separable, sup-norm-closed space of bounded gambles containing some e with inf_Ω e > 0. Separable unital subspaces of larger spaces are covered.
- The theorem is **not** proved for all bounded gambles on an infinite Ω, and the reason is not existence.
  - ℓ∞(Ω) and C(Ω) for non-metrizable compact Ω are nonseparable.
  - **Nonseparable remark** [sketch, not refereed: REF67_out §2.4]. Let F ⊆ ℓ∞(Ω) be closed with 𝟙 ∈ F, possibly nonseparable. Suppose μ is concentrated on a separable closed subspace E ∋ 𝟙, and satisfies (M1) and (M2) on F. Then restricting states from F to E transfers Theorems 4.1 and 5.7(a)–(f) to F. By the Marczewski–Sikorski theorem, the concentration hypothesis holds for every finite Borel μ, unless the density character of F is real-valued measurable.
  - **What is lost there.** First, credal sets on F can no longer be told apart: two of them with the same restrictions to E give the same model, and (M3) must fail, since no finite measure on a nonseparable metric space has full support. Second, the result says nothing about gambles outside the separable support E: they are μ-null, so no model is judged by them.

**Order unit.**
- Some such condition is needed: a world at which every gamble pays 0 makes every model undominated.
- c₀ is open.

**Coherence modulo μ.**
- Models are classes. "Coherent" means "a.e. equal to some D_Q".
- Coherent sets of desirable gambles in the weak sense, and Walley's coherent sets, give the same classes modulo μ (Lemma 1.3(b)). Boundary choices are invisible.
- A literally incoherent set can be coherent modulo μ.
- Which classes are incoherent, and so the ranking, depends on μ. Admissible measures can be mutually singular, for example measures on disjoint countable families of lines. No measure is canonical in infinite dimensions.
- **Hypotheses.**
  - (M1)–(M2) carry every existence and dominance claim, and coverage on E.
  - (M3) serves only to identify distinct credal sets with distinct models, and in the (LF) characterisations of Cor 6.2 and Cor 6.3(b)–(d).
  - μ{P_S = 0} = 0 is essential for protection.
  - μ{sup h = 0} = 0 is neither assumed nor needed.

**Finite-world parts.** Cor 6.3(b)–(e) and Part 8 assume finitely many worlds and a μ with Lebesgue's null sets. Part 8 also works only on one-sided domains D_{K′}.

**The score.**
- The results hold for integrated payoff under **every** μ satisfying (M1)–(M2).
- Positive common reweightings are absorbed into μ (Remark 1.5).
- **No claim is made about other scores.** The orthant and box constructions show that other transformations can also give coherent optima.

**Strict versus uniform improvement.**
- In the ranking, dominance means strict improvement at every world.
- With infinitely many worlds, this need not be uniform (Ex. 5.8). Every repair is uniform, at every state.
- With finitely many worlds, strict and uniform coincide.
- The dominance relation depends on the world set (Ω versus a countable norming Ω₀). The undominated set does not (Part 5, "World sets"; REF66_iw §2.3).

**Interpretation.** The ranking refers to the coherent class through its test "no coherent model can make this change". It *represents* coherence as undominatedness. It does not derive coherence from accuracy considerations stated independently. The mathematical work is the existence of the repairs.

**Open.**
- Nonseparable spaces. Existence and dominance transfer by the remark above (once refereed). What is open is identification: some natural replacement for (M3).
- Spaces without an order unit bounded below.
- Domains not closed under coherent hulls: finite n ≥ 3, and the infinite case.
- Exact (LF) conditions on domains closed under coherent hulls in infinite dimensions.
- **Uniform local freedom.** Say (LF) holds *uniformly* at D_K on U if some δ > 0 makes the ball of radius δ‖h‖ about every h ∈ ∂D_K∖{0} lie in U. It is automatic in finite dimensions. It fails on C(Ω) for infinite Ω (the note's Prop "tube"). It can hold in other infinite-dimensional spaces (REF66_iw §2.2). Its general characterisation is open.
- Which other scores admit such results.

---

## Part 8. One representative structured construction: veto–Brier rankings

**Why include it.** The universal ranking is incomplete and intransitive by design. A veto–Brier ranking shows what is achievable when more structure is demanded. It gives **complete, transitive, score-based** world rankings that assess each acceptance intelligibly: first a veto charge for acceptances that look wrong from world i's side, then a payoff-weighted error. It covers many genuinely imprecise targets.

Its formula is built from points of K, so it encodes the target. It should **not** be advertised as an independent justification of coherence without an examination of why its scoring rule is apt.

**Setting.** Finitely many worlds, n ≥ 2. μ is finite, has Lebesgue's null sets, and has ∫|h| dμ < ∞.

**Theorem 8.1 (veto–Brier coverage)** [covering paper Thms "family" and "cover", Lemma "coh"; refereed in round 61 (VB_dominance_note, REF61)]. Let K be a full-dimensional credal set. Let K′ ⊆ relint K be nonempty, compact and convex. Let A₁,…,A_n be compact, possibly empty, with A_i ⊆ conv(K′ ∪ {e_i}), and

  K = conv(K′ ∪ A₁ ∪ … ∪ A_n).

On U := D_{K′}, rank X at world i by the pair

  a_i(X) := ∫_X max(0, max_{v∈A_i}(−v·h)) dμ,  b_i(X) := −∫_X h_i dμ,

compared lexicographically, lower first.
- a_i charges each accepted gamble by how far its expectation falls below zero under the least favourable member of A_i.
- b_i is the payoff-weighted error at world i, up to a constant.

Then:
- each relation is complete and transitive;
- the ranking satisfies strict guidance and independence;
- only coherent models are undominated;
- it satisfies closure under ties, (ID) and (W);
- D_K is undominated, and (LF) holds at D_K.

So it **covers K**. Its undominated models are exactly the coherent models D_{K(W₀,β,α)} of Lemma "coh".

**Worked instance** [covering paper Cor "contam"]. Let p ∈ relint Δ and 0 < ε ≤ 1, and put K := (1−ε)p + εΔ, with vertices v_i := (1−ε)p + εe_i. Take K′ := {p} and A_i := {v_i}. Then K = conv(K′ ∪ ⋃A_i), and p ∈ relint K.

So Theorem 8.1 applies on {p·h > 0}. At world i the ranking compares

  ( ∫_X [−(1−ε)p·h − εh_i]⁺ dμ, −∫_X h_i dμ )

lexicographically. For ε = 1 this is the vacuous model.

**Which targets are covered: the visibility class** [covering paper Thm "vis", Cor "exemptvis"; round 61].
- **The condition.** Put K_δ := {k ∈ K : the δ-ball about k in aff Δ lies in K}. Hypotheses of the form in Theorem 8.1 exist iff ext K is *uniformly visible*: for some δ > 0, every extreme point lies in some conv(K_δ ∪ {e_j}). Then K′ := K_δ and A_j := K ∩ conv(K_δ ∪ {e_j}) work.
- **An equivalent form.** Uniform visibility holds iff both:
  - every point of cl(ext K) other than a vertex of Δ is visible, that is, for some j, the ray from e_j through it continues into relint K; and
  - no vertex of Δ in K is a limit of other extreme points.
- **Examples.** The class includes:
  - smooth credal sets in relint Δ (Cor "smooth");
  - every full-dimensional credal set for n = 2 (Cor "n2");
  - interior ε-contaminations, with p ∈ relint Δ (Cor "contam");
  - total-variation neighbourhoods {m : ½Σ|m_i − p_i| ≤ δ} with p ∈ relint Δ and 0 < δ < min_j p_j (Prop "tv").

  One exceptional extreme point may be exempt (Thm "exempt").

**Proof sketch.**
1. It is a two-level integral ranking. It satisfies a sign condition: the veto vanishes on gambles in U that are correct at i. Its ties are null, by Fubini along 𝟙-lines. So each relation is a total preorder satisfying strict guidance and independence.
2. Lyapunov's theorem makes the range of score vectors compact and convex.
3. Zorn's lemma together with compactness gives every model an undominated weak dominator.
4. Separation shows that each undominated model minimises an admissible weighted combination over the region where the active vetoes vanish. Each such minimiser is a.e. the intersection of half-spaces D_{K(W₀,β,α)}, which is coherent.
5. **The target.** Take the admissible triple (Ω, p, ∅) with p ∈ K′: every veto is forced to zero, and the error terms are weighted by p. It gives K(Ω,p,∅) = conv(K′ ∪ ⋃_i conv A_i ∪ {p}) = K, so D_K is undominated. (LF) holds with neighbourhood U because K′ ⊆ relint K.

Pointer: covering paper §3 (main theorem on two-level integral rankings; Lemmas "lyap", "zorn", "sep", "unique") and §4 (Lemma "coh", Thms "family", "cover", "vis", Cor "contam").

---

## Part 9. Cut list

### 9.1 Universal note

| Item | Decision | Role in the application |
|---|---|---|
| Abstract, §1 | Rewrite | Lead with Thm 4.1; the ranking is a corollary. |
| §2 framework: rankings, dominance, requirements, Def "cover" | **Essential**, in words | Part 5. Drop (FCC), "record", "safe". |
| §2 Lemmas "D", "hull" (finite) | Drop | Subsumed by Lemmas 1.1, 1.4. |
| §2 Lemma "LF" | Keep | Cor 6.2(b), 6.3(c),(d). |
| §3 records, Lemmas "record", "safe" | **Essential**, renamed | Definition of changes; Lemma 5.1. |
| §3 Def "SI", Lemma "increment", Props "structure", "dominance", Cor "protect" | **Essential** | Part 5, with the general proofs. |
| §3 Lemma "hullformula", Cor "witness" | Keep as a remark | Cor 6.3(e). |
| §4 Lemma "contraction", Prop "shrink" | **Essential** | Lemmas 3.1–3.2. Consistent case only. |
| §4 Thm "H" (Lyapunov) | Drop | Finite case of Thm 4.1; Lyapunov becomes a historical remark. |
| §4 Remark "H" (b),(c),(d) | Remarks / one sentence | Part 4 remarks; Remark 3.4. |
| §5 Thm "main", Cors "universal", "every", Prop "lowdim" | Keep the statements | Cors 6.2–6.3. |
| §6 abstract construction lemma | Drop from the application | Short remark in LDG. Keep one paragraph on why the test must depend only on the change (REF66_un R1). |
| §7.1 Lemmas "states", "envelopes" | **Essential** | Lemma 1.1. "states"(c) becomes a scope remark. |
| §7.2 (M1)–(M3), Lemma "measure", "where conditions are used" | **Essential** | §1.2. Update: coverage needs only (M1)–(M2). |
| §7.2 Example "PS" | Keep as an example | Part 7; Lemma 5.4 note. |
| §7.3 Lemmas "inf-hull", "inf-safe" | **Essential**, generalised to Q_B = ∅ | Lemmas 1.4, 5.1. |
| §7.4 Thm "Hinf", Steps A–D | **Essential**, run on E | Lemma 2.1 (Step B), Lemma 3.2 (Step D), consistent case of Thm 4.1 (Steps A, C). Step C's K′-based non-null gain is replaced by Lemma 3.3(c). The one-sided theorem is no longer cited, only restricted to (Cor 6.2). |
| §7.5 Lemma "normingE"(a),(b) | **Essential** | Lemma 1.1(f); Prop 5.3. |
| §7.5 Lemma "normingE"(c), (A2)/(A5) step | **Replace** | By Lemma 5.4 (full-domain version; B may be non-null). |
| §7.5 Thm "inf-main" | **Essential**, moved to E | Props 5.5–5.6, Thm 5.7. |
| §7.5 "Worlds and norming sets" | Keep as a remark | Part 7. |
| Remarks "finite-special", "orderunit" | **Essential** | §1.5; Remark 1.6. |
| §7.6 one-sidedness, Prop "inf-LF", Thm "inf-cover" | Keep | Cor 6.2. |
| Prop "tube"; §7.7 contamination | Keep as remark / example | Part 7; Cor 6.2(d). |
| Prop "cdg" | **Essential** | Lemma 1.3(b). |
| §8.1 Example "tr" (one-sided) | Replace | By RF67b's full-domain Example 5.9. |
| §8.2 relation to Brier; lexicographic variant | One sentence; drop the variant | — |
| §9 scope | Rewrite | Part 7. |

**Import from round-66/67 notes:**
- TS66 Lemma E → Cor 2.3.
- Domains closed under coherent hulls → Cor 6.1.
- (LF) on V₀ → Cor 6.3(b).
- Plain Brier on ℝⁿ covers exactly the precise sets: one remark.
- The naive repair can fail: one remark.
- From RF67: the inconsistent case by one more use of Lemma 2.1; Lemma 3.3 (Prop R); the −(ω−s)² counterexample; the ℝ² intransitivity example.
- REF66_iw §2.3: world-set dependence of the dominance relation (Part 5, "World sets").
- The note's Lemma "LF"(b), or the covering paper's Lemma "fulldim"(c),(d): the proof of Cor 6.2(b).
- From REF67_out: the incoherent example in Remark 3.4; the nonseparable remark (Part 7), after it is refereed.

**Manuscript convention** (REF67_out J5): theorem environments carry no names. The parenthetical names used here, such as "(repair)", become prose before each statement. Referee tags and file names are stripped.

### 9.2 Covering paper

| Item | Decision | Role |
|---|---|---|
| §2.1–2.4 framework; Lemmas "D", "fulldim", "open"; Def "cover" | **Essential**, already absorbed | Parts 1, 5. |
| Lemma "dominance"(b) (transitivity and global coherence give closure under ties) | Keep | Part 8. |
| Remark "TC" | Footnote | Why closure under ties is a separate requirement. |
| Lemma "worldbest", Thm "dichotomy" | Drop (preserve separately) | — |
| Prop "lowdim" (first part) | Keep | Cor 6.3(d). |
| §3 two-level integral rankings (main theorem of §3) | Keep as an example | Part 8 proof sketch. |
| §4.1–4.3 veto–Brier: Def "vb", Lemmas "veto", "coh", Thms "family", "cover", Cor "contam" | Keep as an example | Part 8. |
| Def "vis", Lemma "V1", Thm "vis", Remark "qual"(1) | Keep as example and **figure** | Part 8. Figure: a triangle in Δ₃ with one visible and one tangential vertex. |
| Thm "exempt", Cors "exemptvis", "poly", "smooth", "n2", Prop "tv" | One-sentence mention | Part 8 (visibility class). |
| §4.4 examples; §4.5 dense approximation | Drop (preserve) | At most one line. |
| §5 orthant-planar; §6 veto–box; §7 composition | Drop (preserve) | One mention in Part 7 that other scores can give coherent optima. |
| §8 scoped exclusions; "what the exclusions show" | Drop (preserve) | Historical catalogue. |
| §9 open problems | Replace | Part 7. Problem (1) is solved by Thm 5.7. |
| Appendix (Thm "PL") | Drop (preserve) | — |

---

## Part 10. Glossary

| Current term | Plain replacement |
|---|---|
| record r(X,Y) = (A,B) | the change from Y to X: what it adds (A) and removes (B) |
| record applies to / attacks Z | the change is open to Z (Z can make it) |
| safe / unsafe | closed to coherent models ("no coherent model can make this change") / open to some coherent model |
| safe-improvement ranking, simple ranking | the ranking: "accept guidance, or a strictly improving change no coherent model can make" |
| defender, safe repair | the repair N (Thm 4.1) |
| two-prior defender D_{[q*,π*]} | the two-prior repair D_{conv{q*,π*}} |
| auxiliary K′ / domain U′ | region of optimisation (hull(X), hull(X₊) or {q* > 0}) |
| rival | a model / an incoherent model |
| Theorem H, H.1, Thm "Hinf" | the repair theorem (consistent case) |
| relative minimax, Step 1/1′, Step B | the minimax lemma (Lemma 2.1) |
| relaxed choice | weighted acceptance choice |
| hull-preserving shrink, shrink, N_τ | trimming (Lemma 3.2) |
| Lemma S / Cor S | contraction lemma / trimming lemma |
| Lemma E, net sure loss | the uniformly losing part (Cor 2.3) |
| Proposition R | Lemma 3.3 |
| Case 1 / Case 2 | consistent / inconsistent commitments |
| Q_B; hull(B) | supporting states of B; coherent hull (E if there is no supporting state) |
| witness mass | dropped (use μ(N∖X)) |
| guidance, G_ω | guided by the truth at ω |
| Brier score m_ω, Brier increment | integrated payoff at ω; score difference |
| uniformly dominates in Brier loss | improves uniformly at every world |
| evaluable model | a model on U |
| hull-closed domain | domain closed under coherent hulls |
| norming set Ω₀ | a countable set of worlds that determines infima and suprema |
| Ω̂ | closure of the worlds among the states (remark only) |
| K_⊥ | gambles to which every member of K assigns expectation 0 |
| (M), (M1), (M2), (M3) | finite first moment; null indifference boundaries; full support |
| (G), (IB) | strict guidance; independence |
| (TC); (FCC) | no strict reversal of a two-step chain; acyclicity (finite-chain consistency) |
| (Add) | disjoint additivity |
| (GC); (ID); (C); (W) | only coherent models undominated; every incoherent model dominated by an undominated coherent one; closure under ties; every model weakly dominated by an undominated coherent one |
| (LF), (LF∞) | local freedom (literal, norm-open neighbourhood); "uniform local freedom" is defined in Part 7 |
| coherent set of desirable gambles (note's Prop "cdg") | coherent set of desirable gambles in the weak sense (Walley's sets are a subclass; same classes mod μ) |
| (A1)–(A5), (R0)–(R5) | dropped from the application |
| (GI), (GP), (SI), (RS), (TG), (TS) [LDG] | guided changes improve; guidance cannot dominate a coherent model; every incoherent model has a strictly improving closed repair; comparisons depend only on the change; guided changes combine; closedness survives joining |
| route A / B / C [LDG] | dropped; name the result |
| certificate, realiser, (B1)–(B3) [LDG] | guarantees on finite sets of worlds; the guaranteeing model |
| (LA), (E), (A) [LDG] | each ranking has undominated coherent models; every model is evaluated by some ranking; every coherent model is undominated for some ranking |
| veto profile, VB(K′,A) | veto sets; the veto–Brier ranking |
| visible, uniformly visible, tangential | unchanged (defined in Part 8) |

---

## Appendix: status after RF67 and REF67_out, and what is still unrefereed

**Refereed by RF67a and RF67b** (all items formerly pending):
- Cor 2.2 on E and Cor 2.3;
- Thm 4.1 in both cases, including the location clause and the inconsistent case by one more use of Lemma 2.1;
- Lemma 3.3(a)–(c) and Lemma 1.4 on E;
- Lemma 5.1, Lemma 5.4 with its protection note, and Props 5.5–5.6;
- Thm 5.7 under (M1)–(M2), and Example 5.9;
- Cor 6.1 for E, D_{K′} and U ⊇ {sup h > 0}; Cor 6.2 as a restriction; Cor 6.3(a);
- the paragraph on sets versus classes.

**Refereed by REF67_out** (it re-derived the whole chain and accepts it as sound):
- the direct consistent-case proof (C17, U5);
- Remark 1.5 (U1);
- Remark 3.4, including the n = 2 examples (U2, §2.1);
- D_{K′} ∪ F (U4);
- Cor 6.3(e) (U6, §2.3).

**Changes made from REF67_out (items 1–10, the minor items, and the wording):**
1. Remark 3.4: the family is now ∅ ≠ Q_B ⊆ Q, with B non-null and disjoint from D_Q. My "Q_B = Q" flag is withdrawn.
2. Part 8: the general Thm "cover" form, refereed in round 61; the contamination case as a real instance; visibility as the description of the class; "full-dimensional" for n = 2; "interior" contaminations; δ < min p_j; step 5 rewritten.
3. Cor 6.3(b)–(e) assume Lebesgue's null sets. One definition of "one-sided", stated in Part 6.
4. Scope:
   - the nonseparable remark (a sketch, not refereed), saying what is lost: credal sets cannot be told apart, and gambles outside the separable support are unconstrained;
   - the (LF) uses of (M3);
   - world-set dependence, citing REF66_iw §2.3;
   - uniform (LF) defined;
   - the finite and one-sided scope of Part 8 and Cor 6.3(b)–(e).
5. Thm 4.1: inconsistent case proved with region hull(X₊); the half-space D_{q*} moved to a remark, with its weaker location clause; one sentence on what the hull inclusion means in each case.
6. Lemma 1.3(b): "coherent in the weak sense", which strictly contains Walley's class; the two give the same classes modulo μ.
7. Incoherent n = 2 variant added (Remark 3.4).
8. Proofs completed: D_{K′} ∪ F (K′ ⊆ Q_B) and Cor 6.2(b). The proof of Cor 6.3(e) is also added.
9. Hypotheses:
   - Lemma 1.1(e) for credal sets;
   - Lemma 1.4(c),(d) converses need (M2);
   - Lemma 3.3(b) is stated "without (M2)" (it still needs (M1)).
10. Glossary: (TC) is "no strict reversal of a two-step chain", and (FCC) is "acyclicity", also in Prop 5.3(b); "weak sense" coherence added.
- **Minor items:**
  - countable-union remark;
  - "at the minimax prior";
  - the null-set appeal dropped from Prop 5.3(b);
  - (iii)⇒(ii)⇒(i) listed in Prop 5.6;
  - "for a fixed minimiser q*";
  - the c_ω nit in Remark 1.5.
- **Wording:** "route(s)" and "relaxed minimax" are removed from headings and remarks. They survive only as old terms in the glossary and as LDG terminology.

**Still unrefereed:**
1. **The nonseparable remark in Part 7.** It is REF67_out's sketch and needs an independent referee before it is stated as a theorem. It is marked as such.
2. **My new text in this revision.** It consists of the rewordings above, the one-sidedness paragraph in Part 6 (assembled from REF66_iw §3 and the note), and the proof write-ups of Cor 6.2(b) and 6.3(e), which follow REF67_out and the note.

No mathematical claim of mine alone remains unrefereed.
