# D1 — Corner atoms through p\* against (LF): the ordinal tie-breaking design cannot cover T1 (round 15)

Scripts: `d1py/` (`three_atom_example.py`, `geometry_checks.py`, with `.out` files; helper `t1geom.py`).
Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. "PROVED (D1)" means proved in this note and not yet refereed.
Notation as in the write-up §§2–7 and in B2_notes / B2_referee. Ω = int Δ.

---

## 0. Outcome

**No construction. The design breaks at step (4) of the plan, and the break is a theorem.**

**Theorem D1 (PROVED (D1)).** Let 𝓜 be a decomposable domain with (LF) at D_{T1}, for any ε ∈ (0,1). Let ψ be a
strictly guiding additive field on 𝓜 with integral penalties and integrable envelope, satisfying (γ). If D_{T1} is
ψ-Bayes at p\* ∈ Ω, then **p\* ∉ E(ψ)**: the ties at p\* are null, and D_{T1} is the a.e.-unique ψ-Bayes model at p\*.

What it says about the plan:
- By B2 Prop 13, p\* ∈ E would force at least one full corner c-atom through p\*. T1 can be intermediate only with
  three of them (B2_referee §5). Theorem D1 excludes **every** number of corner atoms, not just three.
- **Corollary D1.7 (at the status of Prop B2.0).** Take any ranking with strict (G), (IB), (LA), (S), (C) and
  T1 ∈ C_L, on a decomposable domain with (LF), in which every world adds up. Then every supporting assessment ψ has
  p\* ∉ E(ψ). So T1 is never among tied ψ-Bayes models. Ordinal tie-breaking at p\* has nothing to act on, and step (5)
  of the plan is vacuous.
- This proves Conjecture B2.R in the form the B2 referee asked for: under (LF), (R2) is empty. The referee's
  one-atom field, and its three-atom version in §2, show that (LF) cannot be dropped.

**The single obstruction: two-sided frozen support pins the vertices at p\*.**
1. Along the chord ℓ of a corner atom (corner r₁₂), the atom's ties are cut at their apexes. Even so, near p\* the
   face models on ℓ still vanish exactly on the atom's corner arcs. This is because coherence forces each shell to be
   tied or negated as a whole (Lemma D1.3).
2. So v₁ and v₂ lie in the face models at every chord point near p\*. The corner arcs' zeros, by concavity, force
   P ≤ 0 on all of F₁ and F₂ there.
3. (LF) gives vertex neighbourhoods on which the middle-arc gambles are accepted (UVN). By convexity of their charts,
   the middle-arc charts of F₁ and F₂ must then stay away from p\* altogether: (TS_A) fails on two facets (Lemma D1.4).
4. Failure of (TS_A) gives open pinned sets at three crossings (Lemma D1.5), and from them precise walls toward all
   three vertices. The walls are reached even across exceptional chords, by a sign-pattern argument (Lemma D1.6).
5. The surround lemma (N28 Lemma 3.4) then puts p\* in the convex positivity set of a facet-3 gamble, where every face
   model is ≤ 0. This is a contradiction.

"Design the atoms so that the corner equation binds only the K^i while T1 escapes it" fails before any corner
algebra is reached. The escape mechanism (ties at p\*) itself pins the vertices at p\*.

---

## 1. Setting and imports

**Standing data.**
- 𝓜, ψ, (γ) as in Theorem D1. Advice ranges A(g) and the vectors c, c′, d are as in B2 §1.
- E := {q ∈ Ω : ties at q non-null}. A\*_q(g) is the argmin of q·ℓ(g,·) over A(g).
- (LF) at D_{T1} holds with an open N ⊇ ∂D_{T1}∖0. For a.e. h ∈ N, "accept h" and silence are in A(h).

**Imported (statuses as recorded).**
- **B2.1 (B2; CORRECT, B2_referee).** Every p\*-face model K (a coherent D_K with a_{D_K}(g) ∈ A\*_{p\*}(g) a.e.)
  satisfies T1 ⊆ K ⊆ 𝒲. Ties at p\* are {+,0} c-ties only.
- **B2 Prop 13 (CORRECT, B2_referee §5).** If p\* ∈ E, there is a full corner atom. After relabelling it is at r₁₂:
  - an oriented c-atom G with c ∝₊ b, b of pattern (−,−,+), b·p\* = 0;
  - its chord ℓ := {b·q = 0} cuts off e₃;
  - G contains, mod null, the shells S_h := {h + s𝟙 : 0 < s < s_h}, s_h := −P_{K♭}(h) > 0, over an open arc
    α ⊂ ∂D_{T1} containing r₁₂, which meets relint F₁ and relint F₂;
  - Z_{p\*} ∩ (h + ℝ𝟙) equals S_h a.e., for h ∈ α.

  The other atoms at p\* (at most two) sit at r₂₃ and r₃₁. Their arcs lie in the corner portions next to those rays.
- **B2 §2 (CORRECT).** E ⊆ (countable union of atom lines) ∪ (countable set). Call a point t of an atom line ℓ′
  *generic* if it is not a fan point and lies on no other atom line. At generic t, Z_t consists, mod null, of the
  gambles that have one of their c-, c′-, d-lines equal to ℓ′.
- **R10b Lemma D, Lemma M (refereed R12; second reading TS_second_referee).** The notation Γ_v, α_v, β_v, U^±, W_v(U),
  U″ ⊂⊂ U′ ⊂⊂ U is that of write-up §4.2.
- **N28 Lemma 3.4 (surround; refereed twice).**
- **R4 Thm B, transferred off E (CHECKED).** For a.e. g and every q ∈ cl F(g) ∖ E, K_q ⊆ g^⊥. For good g, P(·,g) ≥ 0
  on cl R(g) ∖ E and P(·,−g) ≥ 0 on cl R(−g) ∖ E, by continuity of K at points off E (Lemma D1.1(a)).
- **Lemma signs; Lemma caps(a); B2 Lemma 3 (support).** Lemma 3: P_K = 0 on an open arc of lines through v implies
  v ∈ K.

---

## 2. Steps (1)–(3) of the plan

**Example D1.0 (PROVED; NUMERICS `three_atom_example.out`).** The referee's field extends to three atoms with the
symmetry of T1, without (LF).
- **Data.** Pick m_k ∈ int cap_k and put G_k := D_{T1} ∖ cl D_{co(T1∪{m_k})}.
- **Domain.** A = {+,0} on G_k, {0,−} on −G_k, and the singleton advice of D_{T1} elsewhere.
- **Penalties.** On G_k, c = b_k with b₁₂ = (−1,−1,2), b₂₃ = (2,−1,−1), b₃₁ = (−1,2,−1).

Then:
- each G_k has the corner pattern (E1: 0 violations);
- for every set S of atoms, D_{T1} ∖ ∪_{k∈S} G_k = D_{co(T1 ∪ {m_k : k∈S})} (E2: 0 mismatches in 8·20000 tests).

So every Bayes model at every q is coherent, E = ℓ₁₂ ∪ ℓ₂₃ ∪ ℓ₃₁, and the face at u is a zonotope with three
generators. Since Σ b_k = 0, T1 (accept all three atoms) is interior to it.

**Step (2): the world-i-best models.** K^i accepts G_k iff (e_i − p\*)·b_k > 0. Since b·p\* = 0 and the patterns are
fixed, K^i rejects exactly the two atoms at the corners adjacent to v_i (E4). So K^i = co(T1 ∪ bumps at the two edges
of T1 through v_i) ⊆ co(T1 ∪ {e_i}), in line with B2.1(a). The three K^i are vertices of the zonotope, and T1 (all
three atoms accepted) is an interior point of it. This holds in every three-atom configuration, by the sign argument.

What fails in Example D1.0 is exactly what D1 uses. The vertex model at e₂ contains v₁, so the middle-arc gamble of F₁
is not accepted near e₂ (E5: P = 0 to 10⁻¹⁷). UVN fails, and all K_q contain T1: everything is pinned, and without
(LF) nothing is contradictory.

**Step (3): where the routes of Theorem gm use uniqueness at p\*.** All three routes start from Thm TS / TSalways.
- **(i)** Ψ(p\*,τ) = 0 on [0,1] for every facet. This is used in Lemma levels at level 0 through p\*, in Step 1 of
  Thm pivot, and in "the α-point is p\*" in Lemma R23.1.
- **(ii)** (NS) at the corner rays, giving the corner equation, then the crossing rows, Lemma W/P/D (I1), and the box
  certificate feeding Thm collar (I2, C2, short route).
- **(iii)** K_{p\*} = T ≠ {v_m}, giving dist(p\*, 𝒵_{v_m}) > 0 (TSalways steps 4–5).
- **(iv)** P(p\*, h^i(τ)) = 0, giving p\* ∉ A^i_τ (N28 Lemma 2.4).

With corner atoms at p\*:
- (i) and (ii) survive only on the free arcs (where P_{K♭} = 0). At an atom corner, (NS) is replaced by a gluing
  condition. The facet chord images of the two facets must overlap, which needs x_k + 1/x_{k+1} > κ+1 (CHECKED in
  this round by the sector computation; it is P1's inequality). This was the intended escape: the corner equation
  binds only face models other than T1.
- (iii) and (iv) survive in face-model form. Every face model contains T1, so P^δ(p\*, h) ≤ 0 on ∂D_{T1} for every
  directional family (Lemma D1.1). That is all the surround step needs (§3, last step).

Theorem D1 shows the chain never reaches the corners. The atom forces (TS_A) to fail at p\*.

---

## 3. Theorem D1: proof

Assume p\* ∈ E and fix the atom G, its chord ℓ, its normal b, and the arcs α ⊂ F₁ and α′ ⊂ F₂, as in §1. All
constants below may shrink from line to line.

### Lemma D1.1 (directional families on two-sided domains; PROVED (D1))

Call δ ∈ 𝟙^⊥ **generic** if no atom line is parallel to δ, and the set of g having a c-, c′- or d-line parallel to
δ is null. All but countably many directions are generic.

For generic δ and **every** q ∈ Ω, let D^δ_q choose the lexicographic argmin of (q·ℓ, δ·ℓ) over A(g).

**(a) Coherence and continuity.**
- D^δ_q is a.e. well defined and coherent, D^δ_q = D_{K^δ_q}.
- It equals lim_{s↓0} Bayes(q + sδ) in measure.
- At q ∉ E, K^δ_q = K_q. The map q ↦ K_q is Hausdorff-continuous at every q ∉ E, whether or not E is closed.

**(b) Quasi-concavity.** For every g ∈ ℝ³, q ↦ P^δ(q,g) := P_{K^δ_q}(g) has convex sets {> t} and {≥ t}.

**(c) UVN under (LF).**
- As q → e_l through Ω, K^δ_q → K^{(l)}, the world-l-best (vertex) model.
- If x ∈ N has x_l > 0, there are a ball B ∋ x and a relative neighbourhood V_l of e_l with P^δ(q,h) > 0 for all
  q ∈ V_l ∩ Ω and h ∈ B.
- If x_l < 0, then P^δ(q,h) < 0 there.

**(d) One-sided limits at chord points.** Let t be a generic point of an atom line ℓ′ with normal b′, and let
δ·b′ ≠ 0. Then:
- K^δ_t depends only on sign(δ·b′). Call these sets K^±(t).
- K_q → K^±(t) (Hausdorff) as q → t inside the open side {±b′·(q−t) > 0}, q ∉ E.
- D_{K^+(t)} △ D_{K^−(t)} ⊆ Z_t. Every g there has pattern ±σ′, the strict sign pattern of b′.

**(e) Face models.** K^δ_{p\*} is a p\*-face model. Hence T1 ⊆ K^δ_{p\*} (B2.1), and P^δ(p\*, h) ≤ 0 for every
h ∈ ∂D_{T1}.

*Proof.*
- **(a)** For each g, A(g) is finite.
  - If q·ℓ ties two advices, δ·ℓ separates them unless their difference vector (a c, c′ or d) is orthogonal to both
    q and δ. Then its line is the line through q in direction δ, which is excluded for a.e. g.
  - E meets the ray q + ℝ₊δ in a countable set, since no atom line is parallel to δ.
  - So Bayes(q + s_mδ) is coherent along a sequence s_m ↓ 0 and converges pointwise a.e. to D^δ_q. Limits in measure
    of coherent cones are coherent (R1 Prop 3.1).
  - Off E the ties are null, so every family agrees with the Bayes model. For q′ → q ∉ E, every g not tied at q keeps
    its strict optimum, so the Bayes models converge in measure.
- **(b)** For fixed g and each competing advice a, the set of q at which + lex-beats a is an open half-plane, possibly
  with its boundary line added; the sign of δ·(ℓ(+) − ℓ(a)) on that line does not depend on q. So {q : g ∈ D^δ_q} is
  convex, and D^δ_{q₁} ∩ D^δ_{q₂} ⊆ D^δ_q for q ∈ [q₁,q₂]. Quasi-concavity then follows exactly as in write-up Lemma
  quasilin(a), first half (a ball around g − t𝟙).
- **(c)** For each g, the lex-argmin tends to the unique minimiser of ℓ_l (strict guidance). The limit model is
  coherent by (a).
  - For h near x ∈ N with x_l > 0, acceptance is available (LF) and world-l best, so a ball around x lies in
    D_{K^{(l)}}.
  - For x_l < 0, acceptance is never world-l best. If P_{K^{(l)}}(h₀) = 0, the gambles h₀ + s𝟙 would be accepted.
  - Hausdorff convergence then gives both claims.
- **(d)** At generic t, a gamble that is not tied keeps its strict optimum on a neighbourhood of t. A tied gamble has
  its tied advices differing by a vector ∝ ±b′, so q·(difference) has the sign of ±b′·(q−t) on each side. The third
  advice is strictly worse at t, hence nearby. This gives pointwise convergence a.e., hence Hausdorff convergence.
  The gambles accepted on one side and not on the other are c-ties or d-ties whose c or d is ∝ ±b′. Both vectors carry
  the strict pattern of g.
- **(e)** For a.e. g ∈ Z_{p\*}, − is strictly worse at p\*, so the lex-advice is + or 0. ∎

### Lemma D1.2 (face models near p\*; PROVED (D1))

There is r > 0 such that every Hausdorff cluster value of K_q, for q → p\* with q ∉ E, is a p\*-face model. Hence:
- K_q ⊄ B(m, η) for all m ∈ Δ, q ∈ B(p\*,r)∖E, and η < η₀ := ½ diam T1;
- the same holds for K^±(t) at generic t ∈ ℓ ∩ B(p\*,r);
- K^+(t) → a face model K^+_∗ and K^−(t) → a face model K^−_∗ as t → p\* along either half-ray of ℓ.

*Proof.* Off Z_{p\*}, the advice at q converges to the advice at p\*. On Z_{p\*} it lies in {+,0} eventually, since −
is strictly worse at p\*. A cluster value is therefore a face model, and contains T1. Along a half-ray of ℓ, the
advice on the other atoms' ties is fixed by the constant signs of b_k·(t − p\*). ∎

### Lemma D1.3 (two-sided frozen support; PROVED (D1))

There is r₀ > 0 such that for a.e. t ∈ ℓ ∩ B(p\*,r₀), with K^+(t) the limit from {b·q > 0}:

  **v₁, v₂ ∈ K^+(t), and P_{K^+(t)} ≤ 0 on F₁ ∪ F₂.**

*Proof.* Fix a compact subarc α₀ ⊂ α ∩ relint F₁ of positive length. Take t generic on ℓ, so that Z_t is the set of
line ties on ℓ (B2 §2). Put P^± := P_{K^±(t)}. On the fibre f_s = h + s𝟙 (h ∈ α₀), for a coherent D_K:
- f_s is accepted iff s > −P_K(h);
- f_s is negated iff s < −P̄_K(h);
- f_s is silent in between.

1. **Shell gambles are tied or negated.** For f_s ∈ S_h, c(f_s) ∝₊ b, so c(f_s)·t = 0.
   - If c′(f_s)·t < 0, f_s is a c-tie at t, accepted by K^+(t) and silent in K^−(t).
   - If c′(f_s)·t > 0, − is strictly optimal and both models negate f_s.
   - Apexes at t are null.

   So in K^+(t) every shell level is accepted or negated, never silent.
2. **Dichotomy.** By coherence, the accepted shell levels lie above the negated ones. If both kinds occur in
   (0, s_h), then −P^+(h) = −P̄^+(h), i.e. K^+(t) lies in a line {m·h = const}. By Lemma D1.2, K^+(t) has interior
   for t near p\*, so this never happens. Hence for a.e. h ∈ α₀, the shell S_h is **entirely accepted** (then
   P^+(h) ≥ 0) or **entirely negated** (then P̄^+(h) ≤ −s_h).
3. **Most shells are accepted.** For a.e. g ∈ G, c′(g)·p\* < 0, so g is tied at every t ∈ ℓ close enough to p\*.
   By dominated convergence, the h-measure of A_t := {h ∈ α₀ : S_h entirely accepted} tends to |α₀| as t → p\*.
4. **Exact zero.** Let h ∈ A_t, and suppose P^+(h) > 0.
   - The levels s ∈ (−ε, 0), with ε := min(P^+(h), c₁), are accepted by K^+(t). Here
     c₁ := ½ inf_{α₀} P̄_{T1} > 0.
   - They are not accepted by K^−(t): K^−(t) is silent on the shell above them, and accepted levels form an upper
     ray. So they lie in Z_t, as c-ties or d-ties on ℓ (Lemma D1.1(d)).
   - *c-tie with c ∝ b.* Then c·p\* = 0, so at p\* the gamble is c-tied (and in Z_{p\*}, hence in the shell, which is
     false: s < 0), or negated (which needs s < −P̄_{T1}(h) < −c₁, also false), or an apex (null).
   - *d-tie with d ∝ b.* Then K^−(t) negates it, so P̄^−(t,h) < −s < c₁. But K^−(t) → a face model K^−_∗ ⊇ T1, so
     P̄^−(t,h) ≥ P̄_{T1}(h) − o(1) ≥ 2c₁ − o(1), uniformly on α₀.

   So these levels are null, and P^+(h) ≤ 0. Hence **P^+(t,h) = 0 for every h ∈ A_t.**
5. **Concavity.** τ ↦ γ_t(τ) := P^+(t, h(τ)) is concave on ℝ, where h(τ) parametrises F₁. It vanishes on A_t, which
   has at least 3 points. By Lemma caps(a), γ_t ≤ 0 everywhere and γ_t = 0 on co(A_t), an interval. Lemma 3 (in v₁^⊥)
   gives v₁ ∈ K^+(t).
6. **Second arc.** The same argument on α′ ⊂ F₂ gives v₂ ∈ K^+(t) and P^+ ≤ 0 on F₂. ∎

*Remark.* The difference from Prop carrying (d) is in step 1. On two-sided domains a shell can leave the tie set
along ℓ (apexes). Coherence forces it to leave all at once, so near p\* the zero is still exact. No (LF) is used.

### Lemma D1.4 ((TS_A) fails on F₁ and F₂; PROVED (D1); uses (LF))

For every compact J in the open middle arc of F₁ there is r_J > 0 with P(q, h(τ)) ≤ 0 for all τ ∈ J and
q ∈ B(p\*, r_J) ∖ E. The same holds for F₂.

*Proof (F₁).*
- Put g := h(τ) with τ ∈ J, so g₂, g₃ > 0, and take generic δ with δ·b > 0. At generic t ∈ ℓ, K^δ_t = K^+(t).
- The set C := {P^δ(·, g) > 0} is convex (D1.1(b)) and contains V₂ ∩ Ω and V₃ ∩ Ω (D1.1(c)).
- ℓ meets relint[e₂,e₃] (b has pattern (−,−,+)). So its half-ray R⁺ from p\* toward that edge lies in the open wedge
  spanned by e₂ − p\* and e₃ − p\* (NUMERICS GA, `geometry_checks.out`).
- If x ∈ C has |x − p\*| < r₀/C₀, then co({x} ∪ V₂′ ∪ V₃′) ⊆ C contains an open interval of R⁺ ∩ B(p\*, r₀). Here
  C₀ is the hull constant of GB, finite for the fixed configuration.
- At a.e. point t of that interval, P^+(t, g) ≤ 0 (Lemma D1.3). Contradiction.
- Uniformity over compact J comes from the uniformity of UVN on compacts of gambles.

For F₂, use α′, middle gambles positive at worlds 1 and 3, and the other half-ray R⁻ toward relint[e₁,e₃]. ∎

### Lemma D1.5 (pinned sets at three crossings; PROVED (D1))

Let (F, w, v, l) be one of the following:
- (F₁, w₂₁ = (−1,0,κ), v₁, 3);
- (F₁, w₃₁ = (−1,κ,0), v₁, 2);
- (F₂, w₃₂ = (κ,−1,0), v₂, 1).

In each case l is the positive coordinate of w, and w ∈ relint F crosses one coordinate. Then there are:
- an open convex G with p\* ∈ cl G and V_l ∩ Ω ⊆ G;
- a small ball U around w inside N and inside the UVN balls at w, at w_±, and at the two worlds involved;
- r > 0;

such that:
- **(i)** D_{K_q} ⊇ U^+ (q ∈ Γ_v(U)) for every q ∈ G ∖ E;
- **(ii)** v ∈ K_q for every q ∈ O ∖ E, where O := G ∩ B(p\*, r) is open (E itself need not be closed).

*Proof.* Take σ₁ < τ_w < σ₂ on F around the crossing, with:
- one of them on the middle arc;
- the other on the adjacent corner portion;
- both h(σ_i) positive at world l (Lemma signs).

Choose a generic δ so that the face model K^δ_{p\*} accepts the corner atom whose arc contains σ_i, if there is one
(δ·b_k > 0). Then P^δ(p\*, h(σ_i)) = 0. Indeed K^δ_{p\*} ⊇ T1 gives ≤, and either the shells over h(σ_i) are accepted
or P_{K♭}(h(σ_i)) = 0, which gives ≥.

Put G := int{q : P^δ(q,h(σ₁)) ≥ 0, P^δ(q,h(σ₂)) ≥ 0}. This is convex (D1.1(b)) and contains p\* and V_l ∩ Ω (UVN).
So G ⊇ int co({p\*} ∪ V_l) ≠ ∅, and p\* ∈ cl G.

- **(i)** On G ∖ E, K_q ⊆ W := {m·h(σ₁) ≥ 0, m·h(σ₂) ≥ 0}, a wedge with apex v. Write h ∈ U^+ as w″ + (v·h)𝟙 with
  w″ ∈ F ∩ Ũ ⊆ ℝ₊h((σ₁,σ₂)). Then P(q,h) ≥ v·h > 0. This is the argument of write-up Lemma nopin.
- **(ii)** Choose τ_m ∈ J strictly between the middle-arc σ_i and τ_w, and r ≤ r_J (Lemma D1.4). For q ∈ O, the
  concave function Ψ(q,·) (q ∈ O ∖ E) is ≥ 0 at σ₁ and σ₂ and ≤ 0 at τ_m. So it vanishes identically on [σ₁,σ₂]: a concave
  function that is ≥ its non-negative chord and touches it at an interior point is that chord, which is then 0.
  Lemma 3 gives v ∈ K_q. ∎

### Lemma D1.6 (walls are reached across chords; PROVED (D1))

Fix one of the three cases of D1.5 and 0 < η < η₀. For a.e. (o, y) ∈ O × (V_l ∩ Ω), the segment [o,y] contains a point
q ∉ E with K_q ⊆ B(v, η).

*Proof.*
- **Setting up.** Let β := {q ∈ G∖E : D_{K_q} ∩ U^- ≠ ∅}. By Lemma D (R10b), points of β accept an exterior collar,
  and points of (G∖E)∖β have v ∈ K_q.
  - By D1.5(ii), β ∩ O = ∅ (β ⊆ Ω ∖ E). Since O is open, O ∩ cl β = ∅.
  - y ∈ β, by UVN at w for world l.
  - So the first point Q of cl β on [o,y] lies in (o, y].
- **Genericity.** For a.e. (o,y), the segment avoids the countably many non-generic points of E, is transversal to
  every atom line it meets, and meets E in a countable set.
- **Case Q ∉ E.** K is continuous at Q (D1.1(a)) and Q ∈ cl β ∖ β. Lemma M of R10b applies verbatim on the connected
  open set G, with G ∖ E ⊆ Γ_v (D1.5(i)). Every statement in its proof is about a.e. point of a ball, or about Q,
  so points of E in the ball do not matter. Hence K_Q = {v}.
- **Case Q ∈ E.** Then Q is a generic point of an atom line ℓ′.
  - Let K^s be the one-sided limit from the side of o, and K^o the other one (D1.1(d)). Points of (o,Q) are off cl β,
    so v ∈ K^s. Both limits lie in W_v(U), a closed condition.
  - **(A) D_{K^o} ∩ U^- ≠ ∅.** By Lemma D, D_{K^o} contains an exterior collar of F ∩ cl U″, while D_{K^s} ∩ U^- = ∅.
    So the collar lies in D_{K^o} ∖ D_{K^s} ⊆ Z_Q.
    - The collar contains a ball centred on {g_c = 0}, where c is the zero coordinate of w.
    - Its gambles have two patterns that differ only in coordinate c (NUMERICS GC; elementary). These are not of the
      form ±σ′.
    - This contradicts D1.1(d).
  - **(B) Otherwise.** Then v ∈ K^o as well.
    - If K^s = {v} or K^o = {v}, the segment points just before or after Q are off E, and K_q → {v}. So the segment
      meets {K_q ⊆ B(v,η)}.
    - If neither is {v}, run Lemma M's Steps 1–4 at Q with a full ball B(Q,r′):
      - **Step 1 (no d-faces of near-facet exterior good h in B ∖ E).** K_p stays outside B(v,ρ) by one-sided
        convergence, and R4 Thm B applies off E.
      - **Step 2.** P(·,h) < 0 near Q on both sides for fixed good h ∈ U^-, since v ∈ K^s ∩ K^o. So Q ∉ cl R(h).
        Points of β accumulate at Q, so the chart lines of exterior gambles close to the facet pass within 2η′ of Q.
      - **Steps 3–4.** These give a₊ ∝₊ a₋ against (a₋)_c ≤ 0 < (a₊)_c, where (a₊)_c > 0 is UVN at w₊ for world c.
      - This contradicts Q ∈ cl β. ∎

### Proof of Theorem D1

- Let 𝒵 := {q ∉ E : K_q ⊆ B(v₁,η)} and 𝒵′ := {q ∉ E : K_q ⊆ B(v₂,η)}. By Lemma D1.2, d := dist(p\*, 𝒵 ∪ 𝒵′) > 0.
- By Lemma D1.6:
  - 𝒵 meets a.e. segment from O(w₃₁) to V₂;
  - 𝒵 meets a.e. segment from O(w₂₁) to V₃;
  - 𝒵′ meets a.e. segment from O(w₃₂) to V₁.

  Each O has p\* in its closure.
- The proof of N28 Lemma 3.4 uses one segment per vertex for each small δ, so generic segments suffice. It gives
  p\* ∈ conv(𝒵 ∪ 𝒵′).
- Take h³ ∈ relint F₃ and generic δ. Then v₁·h³ > 0 and v₂·h³ > 0. So for small η, 𝒵 ∪ 𝒵′ ⊆ C₃ := {P^δ(·,h³) > 0},
  which is convex (D1.1(b)).
- Hence p\* ∈ C₃. But P^δ(p\*,h³) ≤ P_{T1}(h³) = 0 (D1.1(e)). Contradiction. ∎

**Where (LF) enters.** Only through UVN:
- at middle-arc gambles of F₁ and F₂ (D1.4, D1.5);
- at the three crossings w₂₁, w₃₁, w₃₂ (D1.5, D1.6).

(LF) near the corner rays, where the atoms sit, is never used. Example D1.0 shows (LF) cannot be dropped.

---

## 4. Consequences, and the nearby targets

**Corollary D1.7 (status of Prop B2.0).** As stated in §0. With B2.1 and Prop 13 it gives:

  **under (LF), the residual (R2) is empty (Conjecture B2.R, PROVED (D1)).**

It also gives the general-domain half of Thm M0closed(a)'s "p\* ∈ E" branch. On M_U that branch was closed by Prop
carrying (d). D1 is an independent route that does not need frozen support along the whole chord.

**What is left of case (M0) on general (LF) domains.** Only the branch p\* ∉ E(ψ) with E ≠ ∅. There, Theorem gm's
chain must survive exceptional chords away from p\*, possibly accumulating at p\*. That is B2 §6 with the referee's
conditional statement: (TS), edge confinement, K_q → {e_b}, vertex-free interiors for (γ)-fields.

**Nearby target.** The tools proved here are exactly what that audit lacked:
- directional families coherent at every q, with quasi-concavity on two-sided domains (D1.1);
- one-sided limits at chord points (D1.1(d));
- Lemma M across chords via sign patterns (D1.6).

TSalways's walls are the step the referee flagged as unaudited. D1.6 shows they cross every chord. I propose that next:
**prove TSalways, Thm cuts/apex and Prop vertexfree for (γ)-fields with p\* ∉ E.** That would close (M0) on every
decomposable domain with (LF) (CONJECTURE). On the construction side, any exact cover of T1 must then have a world
that does not add up (M1/M2), on general domains as on M_U.

---

## 5. Status

| Result | Status |
|---|---|
| Example D1.0 (three-atom (γ)-field, T1 interior to the face, no (LF)) | PROVED; NUMERICS E1–E5 |
| K^i structure (each rejects the two atoms adjacent to v_i) | PROVED (sign argument); NUMERICS E4 |
| Atom gluing needs x_k + 1/x_{k+1} > κ+1 (P1's inequality, general domain) | CHECKED; not used |
| Lemma D1.1 (directional families: coherence at every q, quasi-concavity, UVN with (LF), one-sided limits) | PROVED (D1) |
| Lemma D1.2 (cluster values near p\* are face models) | PROVED (D1) |
| **Lemma D1.3 (two-sided frozen support: v₁, v₂ ∈ K^+(t) near p\*)** | **PROVED (D1)**; no (LF) |
| Lemma D1.4 ((TS_A) fails on F₁, F₂) | PROVED (D1); NUMERICS GA, GB |
| Lemma D1.5 (pinned sets at three crossings) | PROVED (D1) |
| **Lemma D1.6 (walls reached across chords; Lemma M at chord points)** | **PROVED (D1)**; NUMERICS GC |
| **Theorem D1 (p\* ∉ E under (LF))**; Conjecture B2.R | **PROVED (D1)**, not refereed |
| Corollary D1.7 (no M0 cover with T1 among tied models; ordinal tie-breaking at p\* vacuous) | at the status of Prop B2.0 (B2_referee: GAP, documentation) |
| Construction | none; impossible by Theorem D1 |

**Referee priorities.**
1. **Lemma D1.3 steps 2 and 4.** The shell dichotomy, and the exclusion of d-ties with d ∝ b, which uses
   K^−(t) → face model ⊇ T1.
2. **Lemma D1.6 case (A).** The ball in the collar, and the claim that every gamble in D_{K^o} ∖ D_{K^s} at a generic
   chord point is a c-tie or d-tie on that chord, hence of pattern ±σ′.
3. **Lemma D1.1(a), (b) on two-sided domains.** Coherence of D^δ_q at every q, including q ∈ E; and convexity of the
   lex-accept sets.
4. **Lemma D1.5(ii).** The choice of δ per crossing, so that P^δ(p\*, h(σ_i)) = 0 when a corner atom covers σ_i.
5. **Transfer of R4 Thm B and R10b Lemma M to points off E** when E is not closed (continuity at q ∉ E, D1.1(a)).

---

## 6. Scripts (NUMERICS; no verdict rests on them)

- **`d1py/three_atom_example.py`** → `three_atom_example.out`. Example D1.0 at ε ∈ {.05, .2, .3, .6, .9}:
  - E1: corner patterns, 0 violations;
  - E2: coherence of all 8 Bayes-model types, 0 mismatches;
  - E3: b·u = 0, Σb = 0;
  - E4: each K^i rejects 2 atoms;
  - E5: UVN fails without (LF), P = O(10⁻¹⁸).
- **`d1py/geometry_checks.py`** → `geometry_checks.out`.
  - GA: corner chords meet the two edges at the odd vertex, and their half-rays lie in the vertex wedges. 4000 random
    (p\*, b), 0 failures.
  - GB: hull constant, max 721.7 over 19 942 samples (finite, configuration-dependent).
  - GC: facet signs, middle arcs, and two non-opposite patterns in every exterior ball at a crossing. 7 values of ε,
    0 failures. (A first version perturbed along 𝟙 instead of 𝟙 − e_c and reported spurious failures; corrected.)
- **`d1py/t1geom.py`**: helpers.
