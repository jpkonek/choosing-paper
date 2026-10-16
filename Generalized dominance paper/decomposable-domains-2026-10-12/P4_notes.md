# P4. The ordinal route for T1 on the U-domain: (A) rankings that add up survive almost nothing; (B) N17.B′ in the n = 2 nested case

14 Oct 2026, round 11, obstruction side. Labels: **PROVED** (full proof here, from the cited inputs), **CHECKED**
(verified, proof sketched), **CONJECTURE**, **NUMERICS** (scripts in `p4py/`; no proof depends on them).
Notation and terminology as in *The Contamination Triangle.tex* (writeup) and TERMFIX_RULES: decomposable domain,
advice range, U-domain M_U. Notes are cited by file name.

---

## 0. Outcome

**(A) Case M0 (every world adds up).** Fix ψ ∈ 𝒩 (a supporting additive assessment), its field
c_i(g) = ρ_i(g) sign(g_i), target weighting p\*, exceptional set E = E(ψ) = ⋃ atom chords.

- **Theorem A1 (PROVED). Residual R-b′ is closed: p\* ∈ E(ψ) for every ψ ∈ 𝒩.** The chain of writeup §4 runs for
  the canonical coherent family K^♭ (the strict Bayes sets B^s_q, coherent at every q) with no continuity hypothesis.
  Atom chords anywhere else, crossing or dense, do no harm. The new inputs are: quasi-linearity of every
  tie-breaking family in q (Lemma 2.1), a "ball lemma" for tie sets (Lemma 2.3), and a chord-robust Lemma PL2
  (Lemma 2.7). With p\* ∉ E, every line through p\* meets E in a countable set, and that is all the chain needs.
- **Theorem A2 (PROVED). Structure at p\* ∈ E.** T1 = B^s_{p\*} ∪ S with S ≠ ∅. S is carried by at most three
  *corner atoms*, one for each corner ray r_ij of D_{T1}, each lying on an atom chord through p\*. If some carrying
  atom is *full* (contained in D_{T1}), there is a contradiction, by a short argument that needs no blow-up (§4.3).
  Full carrying atoms are automatic when p\* lies on only one chord, and when at most two atoms carry S. They are also
  automatic when the normals of the carrying atoms lie in an open half-plane.
- **Theorem A3 (PROVED). Under (E_ψ), case M0 is closed.** (E_ψ) holds, for instance, when the endorsing weights are
  countably additive. Under it, no ranking on M_U that adds up and satisfies strict (G), (IB), (LA), (S), (C) has
  T1 ∈ C_L. (IB) transport (N25 Thm 8.2, extended here to crossing points) makes T1's split coherent along each chord
  through p\*, and the short argument then applies.
- **Exact residual of (A) (without (E_ψ)).** For every ψ ∈ 𝒩 the following must hold: (E_ψ) fails; p\* is a common
  point of at least three atom chords; T1's split is carried by three corner atoms G₁₂, G₂₃, G₃₁ on three distinct
  chords, with positively spanning normals; every one of them is *partial*, i.e. it straddles ∂D_{T1} along a whole
  boundary arc around its corner ray. Call this the **triple-point configuration (TP)**. It is neither excluded nor
  built here.

**(B) Conjecture N17.B′.**

- **n = 2, nested selection** (N19 §4 item 1):
  - PROVED: the section maximum is attained (Lemma B0).
  - PROVED: a new **strict-escape lemma** (Lemma B1). Adding any non-null set to an initial segment strictly raises
    its section maximum. It uses competitiveness and closed sections at the *other* world.
  - PROVED: N17.B′ for every world that is **lexicographic with countably many countably additive levels**
    (Theorem B3). Closed sections alone force the levels to be entered in order along the chain, and the density of
    the first positive level is then a strictly positive charge that endorses every relevant comparison. This is the
    first case in which (S) is shown to exclude mode (M2). Closed sections, not completeness, do the work.
  - PROVED: the jump-type purely finitely additive worlds have closed sections but fail SP, and strict escape
    excludes them (Prop B2). So competitiveness is needed in addition to closedness.
  - For general (non-lexicographic, incomplete) worlds, N17.B′ in n = 2 is **open**. §5.5 reduces it to a
    certificate statement.
- **n = 3 cyclic.**
  - PROVED: the n = 2 removal mechanism transfers as a lemma for every n (Lemma B4).
  - Where it stops: it needs selected models that approach from below in the first level. Strict escape needs a
    complementary world. In n = 3 neither is available along a cycle of crossing error sets. The n = 3 case is
    **open**, and §6 states what a construction must do.

**Net.** The ordinal route is **not** closed. What a positive construction must now do is narrow (§7):
- either some world fails to add up on the relevant comparisons, and then not by a countable lexicographic structure
  with countably additive levels in the n = 2 sense;
- or it adds up, with (E_ψ) failing for every ψ ∈ 𝒩 (so the endorsing weights carry purely finitely additive mass),
  in the triple-point configuration (TP).

---

## 1. Setting and imported facts

(H_M0) as in writeup §7.5:
- n = 3; the domain is M_U, with U = D_{K′}, K′ = u + s(T1 − u);
- the ranking satisfies strict (G), (IB), (LA), (S), (C), and T1 ∈ C_L;
- (M0) holds;
- ψ ∈ 𝒩, with p\* its target weighting.

Write:
- B^s_q := {g ∈ U : q·c(g) > 0} and Z_q := {q·c = 0};
- H(g) := {q : q·c(g) > 0}, a half-plane of aff Δ;
- *good* g: a.e. g, for which {q : P(q,g) > 0} = H(g) up to a null set of q (Fubini over Δ∖E).

Imported, all from (γ) alone unless stated:

| Fact | Source, status |
|---|---|
| (α) T1 is ψ-Bayes at an interior p\*, i.e. D_{T1} = B^s_{p\*} ∪ S with S ⊆ Z_{p\*} | writeup Prop M0; inputs refereed once |
| (γ) E null; B_q = D_{K_q} for q ∉ E | same |
| E = ⋃_k (ℓ_k ∩ Δ°); each ℓ_k is the common chart line of an oriented atom G_k ⊆ O_{σ_k}, b_k without zero coordinate, cutting off the vertex of the odd world; no fan points; E meets every non-chord line in a countable set | writeup Thm Estructure (N25 Thm 2.1, Cor 2.2, referee Prop F), one reader each |
| B^s_q = D_{K^♭_q} is coherent for **every** q ∈ Δ°; K^♭ is u.s.c., continuous exactly off E; for δ ∉ D_q the directional limit X_δ(q) := B^s_q ∪ (Z_q ∩ {δ·c > 0}) is coherent; countable intersections of coherent models are coherent | N25 Lemma 3.1, 3.2, Thm 3.3 (confirmed) |
| Atom anatomy: for q ∉ E, G_k ⊆ B_q on H⁺(ℓ_k) and G_k ∩ B_q = ∅ on H⁻ (mod null); at t ∈ ℓ_k° (points of ℓ_k on no other chord), Z_t = G_k ∪ G′_k, and B^s_t ∪ G_k = D_{K⁺(t)} is coherent; *frozen support*: on the 1-saturation Π_k of G_k, P_{K⁺(t)} =: π⁺ and P_{K^♭_t} =: π^♭ do not depend on t ∈ ℓ_k°, and G_k ∩ (g+ℝ𝟙) = {g − s𝟙 : π^♭(g) ≤ s < π⁺(g)} | N25 Thm 4.1 (confirmed) |
| Prop F step 2 and estimate (★): good points of Z_x on one fibre g+ℝ𝟙 share one oriented chart line through x; two good fibres with distinct lines through x, at sup-distance d, satisfy \|J(g)\| + \|J(g′)\| ≤ 2d, where J is the set of levels in Z_x | N25_referee §2 (one reader) |
| Lemma edgebox holds for every such field (no continuity) | N25 Prop 9.2 (confirmed) |
| (IB) transport of comparisons among splits along a chord; under (E_ψ), Lemma 1.2 (face points are profiles of selected models) and Thm 8.2 | N25 §§1.2, 8 (confirmed) |

---

## 2. Additive tools that survive atom chords

### 2.1 Tie-breaking families and quasi-linearity

For a measurable A ⊆ U put B^A_q := B^s_q ∪ (Z_q ∩ A). Then:
- A = ∅ gives K^♭;
- A = {δ·c > 0} gives the directional family K^δ, with B^A_q = X_δ(q).

The family is *admissible* if B^A_q is coherent for **every** q ∈ Δ°, say B^A_q = D_{K^A_q}. Write
P^A(q,g) := P_{K^A_q}(g).

**Lemma 2.1 (PROVED; quasi-linearity).** If A is admissible, then for every g ∈ ℝ³ the function q ↦ P^A(q,g) is
quasi-concave and quasi-convex on Δ°. So all its level sets {>t}, {≥t}, {<t}, {≤t} are convex.

*Proof.*
- For fixed g the acceptance region {q : g ∈ B^A_q} is the open half-plane {q·c(g) > 0} if g ∉ A, and the closed
  half-plane {q·c(g) ≥ 0} if g ∈ A. Each is convex with convex complement.
- Hence, for q ∈ [q₁,q₂], pointwise B^A_q ⊇ B^A_{q₁} ∩ B^A_{q₂} and B^A_q ⊆ B^A_{q₁} ∪ B^A_{q₂}.
- Mod null this gives D_{K_q} ⊇ D_{K_{q₁}} ∩ D_{K_{q₂}} = D_{co(K_{q₁}∪K_{q₂})} and D_{K_q} ⊆ D_{K_{q₁}} ∪ D_{K_{q₂}}.
- Suppose P_q(g₀) < min(P_{q₁}, P_{q₂})(g₀). Pick t strictly between. A neighbourhood of g₀ − t𝟙 lies in
  D_{K_{q₁}} ∩ D_{K_{q₂}} but outside D_{K_q}. That set is non-null, a contradiction. The max inequality is the
  same. ∎

So **Lemma levels holds for every admissible family, for every g and every level, with no continuity.** The proof
in writeup §4 needed cluster lines and joint continuity.

**Lemma 2.2 (PROVED; admissible families and their regularity).**
- (a) ∅ is admissible. So is {δ·c > 0} for every δ ∈ 𝟙^⊥ not parallel to an atom chord (a co-countable set of
  directions; N25 Lemma 3.1).
- (b) For admissible A: K^A_q = K_q for q ∉ E, and K^A is continuous at every q ∉ E. Moreover K^A_q → co(K′ ∪ {e_l})
  as q → e_l through all of Δ°. Hence Lemma UVN holds for P^A.
- (c) K^♭ is u.s.c. So P^♭(·,g) is l.s.c. for every g, and {P^♭(·,g) > t} is open.
- (d) Charts. For good g: {P^A(·,g) > 0} ⊇ H(g) ∩ Δ° and ⊆ cl H(g); {P^A(·,g) < 0} ⊇ Δ°∖cl H(g) and ⊆ Δ°∖H(g). The
  exceptional points lie in ∂H(g) ∩ E. For K^♭: {P^♭(·,g) > 0} = H(g) ∩ Δ° exactly.

*Proof.*
- (b) Fix q ∉ E and q_m → q. For a.e. g, q·c(g) ≠ 0, so eventually sign q_m·c(g) = sign q·c(g), and the tie rule is
  irrelevant. Hence 1_{B^A_{q_m}} → 1_{B_q} a.e. Coherent cones converging in measure have Hausdorff-converging
  credal sets (R1 Prop 3.1). For q → e_l, q·c(g) → c_l(g) ≠ 0 for every g. So B^A_q → U ∩ {g_l > 0} pointwise, and
  that cone is D_{co(K′∪e_l)}. UVN's proof uses only this convergence and upward closure of coherent cones.
- (c) is N25 Thm 3.3(c).
- (d) {P^A(·,g) > 0} is convex (Lemma 2.1) and a.e. equal to the open half-plane H(g) ∩ Δ°. A convex set has the
  same interior as its closure, so it contains H(g) ∩ Δ° and lies in cl H(g). The negative side is the same.
  - Suppose q ∉ E, q ∈ ∂H(g), and P^A(q,g) > 0. By (b), P^A(·,g) > 0 on a neighbourhood of q, and that neighbourhood
    meets Δ°∖cl H(g), where P^A < 0. Contradiction.
  - For K^♭ the set {P^♭ > 0} is open by (c), hence equal to H(g) ∩ Δ°. ∎

### 2.2 The ball lemma

**Lemma 2.3 (PROVED).** Let x ∈ Δ° and let O be an open ball with O ⊆ Z_x mod null. Then all good g ∈ O have c(g) in
one ray ℝ_{>0}b, so O lies (mod null) in a single open orthant O_{sign b}. In particular no ball centred on a
coordinate plane {g_c = 0} lies in Z_x mod null.

*Proof.*
- By Fubini, a.e. fibre g + ℝ𝟙 meeting the half-size ball O′ has good points of Z_x on a set of levels J(g) of
  length at least η > 0 (fixed by the radii).
- By Prop F step 2, each such fibre carries a single oriented line L(g) through x. By (★), two such fibres at
  sup-distance d < η with L ≠ L′ would give 2η ≤ 2d. So L is a.e. locally constant on the connected set of fibres
  through O′, hence a.e. constant.
- An oriented line determines c up to a positive factor, because aff Δ spans ℝ³. Strict signs then give the orthant.
- A ball centred on {g_c = 0} has non-null parts on both sides of that plane. ∎

### 2.3 Shell lemmas

Recall from writeup §4 the 6-cycle of sign patterns around ∂D_{T1}:
- the *middle arc* of F_k has pattern negative only at k;
- the *corner arc* around r_ij (between the crossings of F_i and F_j adjacent to r_ij) has the corner pattern,
  negative at i and j;
- the six crossing gambles w (with one zero coordinate) separate the arcs.

**Lemma 2.4 (PROVED).** Let x ∈ Δ° and let K be a credal set.
- (a) If K ⊊ T1, then the shell D_K∖D_{T1} is not contained in Z_x mod null.
- (b) If K ⊋ T1 and D_{T1}∖D_K ⊆ Z_x mod null, then the set A(K) := {h ∈ ∂D_{T1}∖0 : P_K(h) < 0} is a nonempty open
  subset of the 6-cycle containing no crossing gamble. Each component of A(K) is an open arc around a corner ray,
  contained in its corner arc, and there are at most three. Every point of the shell lies on a fibre
  {h + s𝟙 : 0 < s ≤ |P_K(h)|} with h ∈ A(K).

*Proof.*
- (a)
  - K misses some vertex v_k of T1. For h ∈ relint F_k, the minimum of h over T1 is attained only at v_k, so
    P_K(h) > 0.
  - Take the crossing w ∈ relint F_k with w_c = 0, and g₁ := w − s(𝟙 − e_c) for small s > 0. Then
    P_{T1}(g₁) ≤ −s(1 − v_{k,c}) < 0 < P_K(g₁), and (g₁)_c = 0.
  - A ball around g₁ lies in the shell. Lemma 2.3 then rules out shell ⊆ Z_x.
- (b)
  - A(K) is open (P_K is continuous) and nonempty: separate a point of K∖T1 from T1.
  - For h ∈ A(K) and 0 < s < |P_K(h)|, h + s𝟙 lies in the shell, with an open neighbourhood. If h = w were a
    crossing, the point w + s(𝟙 − e_c) would centre a ball in the shell on {g_c = 0}, against Lemma 2.3.
  - On relint F_k, {h : m·h < 0} is, for each m ∈ K, a sub-cone of F_k that contains a corner ray of F_k (m·h is
    linear on the 2-cone spanned by the corner rays). So every point of A(K) ∩ relint F_k is joined inside A(K) ∩ F_k
    to a corner ray. Since A(K) contains no crossing, each such sub-arc stays inside the corner arc.
  - Fibres: for g in the shell, h := g − P_{T1}(g)𝟙 has P_K(h) = P_K(g) − P_{T1}(g) < 0. ∎

**Lemma 2.5 (PROVED).** −σ is never a corner pattern when σ is one. So a chord's two oriented atoms G, G′ (patterns
±σ) cannot both have corner patterns. A chord whose atom has a corner pattern σ cuts off the vertex e_o of the
positive (odd) world o of σ.

*Proof.* Corner patterns have two negative coordinates and their negatives have one. The cut-off statement is writeup
Thm Estructure(b). ∎

NUMERICS (`p4py/shells.py`, ε = 0.3, 4·10⁵ sampled gambles; output in `p4py/shells.out`):
- 200 random K ⊊ T1 all have shells in ≥ 3 orthants;
- of 1735 random K = co(T1 ∪ {m}) ⊋ T1, the 164 whose shell lies in one orthant all have a corner pattern;
- −corner patterns are middle patterns;
- corner-pattern chords through u cut off the odd vertex.

### 2.4 PL2 and no-pinning across chords

Fix a vertex v = v_k with crossing w ∈ relint F_k, w_c = 0, and the ball 𝒰 of writeup §4.2, with 𝒰^± = 𝒰 ∩ D_{T1}
and 𝒰∖cl D_{T1}. Put:
- Γ := {q : D_{K^♭_q} ⊇ 𝒰⁺ mod null};
- α := {q ∈ Γ : v ∈ K^♭_q};
- β := Γ∖α.

For q ∈ Γ, K^♭_q lies in the wedge W at v. So q ∈ α iff P^♭(q,·) ≤ h·v < 0 on 𝒰⁻. And q ∈ β iff D_{K^♭_q}
contains an exterior collar of F_k ∩ 𝒰, which has points with g_c of both signs.

**Lemma 2.7 (PROVED; PL2 for K^♭, chords allowed).** If G ⊆ Γ is open and connected, then G ⊆ α or G ⊆ β.

*Proof.*
- β is relatively open in Γ, because K^♭ is u.s.c. and {v ∉ K} is open in the Hausdorff topology.
- Suppose Q ∈ G ∩ α ∩ cl β.
- **Step 1: every Hausdorff cluster value K\* of K^♭_q (q → Q, q ∈ G) contains v.**
  - K\* ⊆ W. If q·c(g) < 0 at Q then also at q near Q, so lim sup B^s_q ⊆ B^s_Q ∪ Z_Q, and
    D_{K\*} ⊆ D_{K^♭_Q} ∪ Z_Q mod null.
  - If v ∉ K\*, then D_{K\*} contains a collar of F_k near w, which misses D_{K^♭_Q} (v ∈ K^♭_Q). So the collar
    lies in Z_Q mod null.
  - The collar contains a ball centred on {g_c = 0}, against Lemma 2.3.
- **Step 2.** By Step 1 and Lipschitz continuity in g, P^♭(·,h) < 0 on a neighbourhood of Q, uniformly for h in
  compact subsets of 𝒰⁻. By Lemma 2.2(d), Q ∉ cl H(h) for good h ∈ 𝒰⁻.
- **Step 3.** The rest is the proof of writeup Lemma PL2 verbatim. It uses only:
  - openness of {P^♭ > 0} at the points s_m ∈ β (Lemma 2.2(c));
  - the a.e. half-plane charts;
  - the collar at points of β;
  - strict signs, and UVN (Lemma 2.2(b)).
  The two limit lines a_± through Q satisfy a₊ = λa₋ with λ > 0, (a₋)_c ≤ 0 and (a₊)_c > 0. Contradiction. ∎

**Lemma 2.8 (PROVED; no pinning, every admissible family).** Writeup Lemma nopin holds for P^A, with any admissible
A, on any nonempty open connected G ⊆ Δ°.

*Proof.*
- Under the hypotheses, P^A(q,w″) ≥ 0 on G for w″ ∈ F_k ∩ 𝒰̃, by concavity and homogeneity. So for good h ∈ 𝒰⁺,
  P^A(·,h) > 0 on G, hence G ⊆ H(h) (Lemma 2.2(d), G open). Also V_j ⊆ H(h), by UVN.
- So for **every** q ∈ int co(G ∪ V_j), a.e. h ∈ 𝒰⁺ has q·c(h) > 0, i.e. h ∈ B^s_q. Thus
  int co(G ∪ V_j) ⊆ Γ (for K^♭; no Fubini over q is needed).
- Lemma 2.7 and UVN at V_j put it in β: v_k ∉ K^♭_q. Since K^A_q ⊆ K^♭_q (B^A ⊇ B^s), also v_k ∉ K^A_q. The last
  step of nopin is then unchanged. ∎

---

## 3. R-b′ is closed

### 3.1 Why I1 and I2 are not the right routes on M_U

Routes I1, I2 and C2 of writeup §6 start from the structure of covers on *general* decomposable domains:
- (TS), (PC), (NS);
- both acceptances in the advice range of a.e. mixed pair (Cor TSalways(b));
- K_q → {e_b} at the vertices, and edge confinement (Cor TSalways(c));
- d-faces.

On M_U:
- K_q ⊇ K′ for every q, so edge confinement and K_q → {e_b} are false;
- no advice range contains both acceptances. Cor TSalways(b) *is* the contradiction there.

So for ψ on M_U the relevant impossibility argument is the chain of writeup §4 (Theorem main). I1's inputs at fixed
weightings are:
- the every-q chart form (Prop CF(⇒));
- vector clusters at p\* (Lemma veccluster);
- edge limits (Prop edgelimits);
- "no straddling" at every q with c_k(h)·q > 0 (Lemma nostraddle).

Their M_U analogues are Lemma 2.2(d), the robust cluster clause (§3.2, step "clusters"), and nothing, respectively:
the edge structure does not exist on M_U. I therefore rerun §4.

### 3.2 The chain for K^♭

**Theorem 3.1 (PROVED).** Let c be a strictly signed integrable field on M_U whose Bayes models are coherent at a.e.
weighting. Suppose p\* ∈ Δ°∖E and T1 = D_{K^♭_{p\*}}, which holds when T1 is ψ-Bayes at p\* ∉ E. (If p\* ∈ E,
then T1 = K^♭_{p\*} is impossible by Prop 4.1(i), which uses only Lemma 2.4(a).) Then the conclusions of writeup
Thms pivot and nosliding, Lemma rotation, Props regularity, blowup and boxbridge, and Cor PCNS hold for P^♭. Prop T1
then gives a contradiction. The same holds for every all-facing triangle in general position, through the R15
algebra.

*Proof: a step-by-step audit of writeup §4 with P = P^♭.*

Since p\* ∉ E, no line through p\* is an atom chord. So λ ∩ E is countable for every line λ through p\* (N25
Cor 2.2).

| §4 step | Original input | Replacement |
|---|---|---|
| Lemma chords (a) | continuity in q | Lemma 2.2(d): {P^♭ > 0} = H(g) ∩ Δ° exactly; {P^♭ < 0} = Δ°∖cl H(g) except points of ∂H(g) ∩ E |
| Lemma chords (b), cluster lines | joint continuity | not needed; replaced below |
| Lemma levels | (b) | Lemma 2.1, at every level and every g. {Ψ > t} is an open half-plane (l.s.c.); {Ψ < t} is a half-plane up to boundary points in E |
| Lemma sandwich | convexity | unchanged |
| Lemma caps (a), (b) | pointwise in q | unchanged |
| Lemma caps (c), used in Lemma rotation | joint continuity of Ψ | Ψ is jointly continuous at (q,τ) for every q ∉ E (Lemma 2.2(b) plus 1-Lipschitz in g). Each anchor q_τ(ξ) ∈ λ_τ is chosen with ξ such that q_τ(ξ) ∉ E, possible because λ_τ ∩ E is countable. Only countably many τ (a, b, c of Prop regularity(a)), or a single τ at a time (Prop regularity(b), (c)), need anchors |
| UVN | vertex limit | Lemma 2.2(b) |
| PL2, nopin | continuity on co(G ∪ V_l) | Lemmas 2.7, 2.8 |
| Pivot Step 0 | levels at 0, UVN | as above: A_τ is an open half-plane ∩ Δ°; B_τ ⊇ an open half-plane |
| Step 1 (p\* ∈ λ⁺_τ) | nopin, Ψ(p\*,·) = 0 | Lemma 2.8; Ψ(p\*,τ) = P_{T1}(h(τ)) = 0 |
| Step 2 (monotone pieces) | concavity in τ | unchanged (open half-planes through p\*) |
| Step 3 (continuity of n) | pointwise in q | unchanged: for q in the open wedges W, ±W, Ψ(q,τ) > 0 for τ > τ₀ and ≤ 0 for τ < τ₀, so Ψ(q,τ₀) = 0 by continuity in τ; the zero set is convex (Lemma 2.1) |
| Step 4 (no constancy) | Ψ(q,·) = 0 on [a,b] for q ∈ λ | For q ∈ λ∖E (co-countable): q ∉ A_τ, so Ψ ≤ 0. If Ψ(q,τ) < 0, continuity at q would put a neighbourhood of q, which meets A_τ, into B_τ. So Ψ(q,·) = 0 on [a,b], hence ≤ 0 on ℝ. Every A_τ, an open half-plane through p\*, misses λ∖E, so λ⁺_τ = λ for every τ. Contradiction as before |
| Step 5 (thin zero set) | pointwise | choose q ∈ (A_{τ₁} ∩ D⁻)∖E; otherwise verbatim. Afterwards Z_τ = λ_τ ∩ Δ° exactly: every q ∈ λ_τ∖{p\*} lies in A_σ for σ on one side of τ and outside A_σ on the other |
| Cluster clause | Lemma chords (b) | **robust form:** for good g_m → h(τ), q ∈ A_τ gives P^♭(q,g_m) > 0, hence q ∈ cl H(g_m), and q ∈ B_τ gives q ∉ H(g_m) for large m (1-Lipschitz in g, Lemma 2.2(d)). So every limit line separates the two open sides of λ_τ and equals λ_τ with its orientation. This also gives the vector form (Lemma veccluster) |
| Thm nosliding | convex zero set, caps (a) | unchanged (Lemma 2.1, pointwise caps) |
| Lemma rotation, Props regularity, blowup | sandwich, caps, joint continuity at anchors | as above |
| Lemma twoslope, Cor PCNS | pure analysis | unchanged |
| Lemma edgebox | — | N25 Prop 9.2 (E-robust) |
| Prop boxbridge (c) | cluster vectors | robust cluster clause |
| Prop T1, normalisations | algebra; p\* = u by κ⊙ψ; transposition | κ⊙ψ ∈ 𝒩 moves E and p\* together (writeup Prop generic(b)); the transposed field c^σ has the same properties |

So (PC), (NS), crossing rows, corner equations and the box hold, and Prop T1 contradicts them. ∎

**Theorem A1 (PROVED).** Under (H_M0), every ψ ∈ 𝒩 has p\* ∈ E(ψ): the target weighting lies on an atom chord.
Residual R-b′ of writeup §7.6 is closed. This uses only (α) and (γ): no (E_ψ), no ranking structure beyond Prop M0.

*Proof.* If p\* ∉ E, then S is null and T1 = K^♭_{p\*}. Apply Theorem 3.1. ∎

*Remark.* N25 Prop 9.3 (CHECKED) said that N15 *as written* needs continuity on sets covering Δ°. That remains true
of the text. The point here is that continuity is never needed: quasi-linearity replaces it everywhere, and the u.s.c.
family K^♭ replaces continuity at the single place (openness of A_τ) where a semicontinuity is needed.

---

## 4. p\* ∈ E: the split of T1

### 4.1 Where S lives

**Proposition 4.1 (PROVED).** Let p\* ∈ E and D_{T1} = B^s_{p\*} ∪ S.
- (i) S is non-null, i.e. T1 ≠ K^♭_{p\*}.
- (ii) S = D_{T1}∖D_{K^♭_{p\*}}, and A(K^♭_{p\*}) has at most three components α_ij, one around each corner ray
  r_ij. The fibres over α_ij lie in one oriented atom G_ij, which has the corner pattern of r_ij and lies on an atom
  chord ℓ_ij ∋ p\*. Call G_ij a *carrying atom*. S = ⋃ (S ∩ G_ij) mod null.
- (iii) If at most two atoms carry S, or the carrying normals b̄_ij (projections to 𝟙^⊥) lie in an open half-plane,
  then T1 = X_δ(p\*) for a generic δ, and every carrying atom is **full**: G_ij ⊆ D_{T1}. This holds in particular
  if p\* lies on a single chord.

*Proof.*
- (i)
  - If S is null, then for every generic δ, X_δ(p\*) ⊇ B^s = D_{T1}, so K_δ ⊆ T1, and the shell X_δ∖D_{T1} lies in
    Z_{p\*}. By Lemma 2.4(a), K_δ = T1.
  - Then X_δ = X_{−δ} = B^s, so Z_{p\*} ∩ {δ·c > 0} is null for all generic δ, and Z_{p\*} is null, against p\* ∈ E.
- (ii)
  - K^♭ ⊋ T1 and the shell S ⊆ Z_{p\*}, so Lemma 2.4(b) applies.
  - On each component α, |P^♭(h)| is continuous and positive, hence locally bounded below, and the fibre over h has
    level length |P^♭(h)|.
  - By (★), nearby fibres share one oriented line through p\*. By connectedness of α, all of them do, with
    c ∝ b_α. This set is non-null, so b_α is an atom of γ_\*μ, and its line is an atom chord through p\*.
  - The pattern of the fibre near h is the pattern of h, a corner pattern.
- (iii)
  - Two distinct chords through p\* have b̄'s that are not negatively proportional: b₁ + cb₂ ∝ 𝟙 with
    p\*·b₁ = p\*·b₂ = 0 forces b₁ = −cb₂, i.e. the same chord with opposite orientations, which is impossible for two
    corner patterns by Lemma 2.5.
  - So some δ, which may be taken generic, has δ·b_ij > 0 for every carrying atom. Then X_δ(p\*) ⊇ D_{T1}, and
    Lemma 2.4(a) gives equality, so the carrying atoms are full.
  - On a single chord, the opposite atom G′ has a middle pattern and carries nothing. ∎

### 4.2 Atom gambles force constant pivot lines

**Lemma 4.2 (PROVED).** Let G be a carrying atom on ℓ ∋ p\*, with arc α. For h ∈ α:
- π⁺(h) ≥ 0, with equality iff G's fibre through h does not extend below ∂D_{T1};
- for q ∈ H⁻(ℓ)∖E, P(q,h) ≤ π^♭(h) < 0;
- for q ∈ H⁺(ℓ)∖E, P(q,h) ≥ π⁺(h).

Hence, for **every** admissible family, B_h := {P^A(·,h) < 0} ⊇ H⁻(ℓ).

*Proof.*
- G ∩ (h + ℝ𝟙) = {h − s𝟙 : π^♭ ≤ s < π⁺} contains h + s′𝟙 for 0 < s′ < |P^♭_{p\*}(h)|. This gives π⁺ ≥ 0 and
  π^♭ ≤ −|P^♭_{p\*}(h)| < 0.
- The cliff is N25 Thm 4.1(f), with h ∈ Π (h is interior to Π, since the shell is open there).
- The last claim follows by convexity (Lemma 2.1), since H⁻∖E has convex hull H⁻. ∎

### 4.3 The short argument

**Theorem 4.3 (PROVED).** If some carrying atom G (on ℓ ∋ p\*, with arc α) admits an admissible family A whose
members at t ∈ ℓ° satisfy P^A(t,h) = 0 for all h ∈ α, there is a contradiction.

This is the case:
- with A = {δ·c > 0}, δ generic with δ·b > 0, when G is **full**. Then K^δ_t = K⁺(t) and
  P_{K⁺(t)}(h) = π⁺(h) = 0 (Lemma 4.2);
- with any admissible A such that A ∩ Z_{p\*} = S, for instance A = S when B^s_t ∪ (S ∩ G) is coherent for
  t ∈ ℓ° (§4.4). Then B^A_t = B^s_t ∪ (S ∩ G) on ℓ°. Its fibre over h is {s < π^♭} ∪ {π^♭ ≤ s < 0} = {s < 0},
  using frozen support and S ∩ G = G ∩ D_{T1}, so P = 0.

*Proof.*
- α is open around the corner ray r = r_kj, so it meets relint F_k in an interval h(J), J ⊆ (0,1) adjacent to the
  end of F_k at r.
- For t ∈ ℓ°, φ_t(τ) := P^A(t,h(τ)) is concave in τ (h is affine on the facet line) and vanishes on J. By writeup
  Lemma caps(a), φ_t ≤ 0 on ℝ.
- Take τ_m in the middle arc of F_k. Then h(τ_m) is positive at j and at the odd world o of σ = pattern(r). By
  Lemma 2.5, ℓ separates e_o from e_j.
- By UVN (Lemma 2.2(b)), {P^A(·,h(τ_m)) > 0} contains V_o ∩ Δ° and V_j ∩ Δ°. By Lemma 2.1 it is convex, so it
  contains segments from V_o to V_j. Their crossing points with ℓ fill an open interval of ℓ, which contains a point
  t ∈ ℓ° (co-countable). There φ_t(τ_m) > 0. Contradiction. ∎

**Corollary 4.4 (PROVED).** Under (H_M0) and for every ψ ∈ 𝒩, the target weighting p\* is a common point of at least
three atom chords. T1's split is carried by three corner atoms G₁₂, G₂₃, G₃₁ on three distinct chords, with
positively spanning normals b̄_ij. Each is *partial*: π⁺ > 0 on a dense open subset of the part of its arc lying in
relint F_k, for each facet F_k adjacent to its corner. Equivalently, G_ij straddles ∂D_{T1} there.

*Proof.*
- Theorem A1 gives p\* ∈ E.
- By Prop 4.1(iii) and Theorem 4.3 (full case), at most a configuration with three partial carrying atoms survives.
- If π⁺ vanished on an open sub-interval J of α ∩ relint F_k, Theorem 4.3 would apply with that J. So
  {π⁺ = 0} ∩ α ∩ relint F_k is nowhere dense, and {π⁺ > 0} is open by continuity of π⁺. ∎

*Forced features of (TP) (PROVED).*
- By Lemma 4.2, for each corner, every facet gamble in a dense open part of the arc has, for every admissible family,
  A_h ⊇ H⁺(ℓ_ij) and B_h ⊇ H⁻(ℓ_ij). Its pivot line is ℓ_ij, constant along the arc.
- **No admissible family passes through T1.**
  - If K^A_{p\*} = T1, then A ∩ Z_{p\*} = S, so A ∩ G_ij = S ∩ G_ij and A ∩ G′_ij = ∅.
  - Hence on ℓ_ij°, B^A_t = B^s_t ∪ (S ∩ G_ij), whose support at h ∈ α_ij is 0 by the fibre computation of
    Theorem 4.3.
  - Theorem 4.3 then applies.
- So in (TP) the chain cannot start, at p\* or anywhere: the obstruction is exactly the incoherence, along the
  chords, of T1's partial splits.

### 4.4 Under (E_ψ)

**Theorem A3 (PROVED).** Under (H_M0), suppose (E_ψ) holds for some ψ ∈ 𝒩, for instance because the endorsing
weights are countably additive. Then there is a contradiction: no ranking that adds up covers T1 on M_U.

*Proof.*
- By Theorem A1, p\* ∈ E. Let S_ij := S ∩ G_ij for the carrying atoms (Prop 4.1).
- **Claim:** for every t ∈ ℓ_ij°, B^s_t ∪ S_ij is undominated, hence coherent.
  - Suppose it is dominated. By Fact 0 and N25 Lemma 1.2 (which uses (E_ψ); B^s_t ∪ S_ij is t-Bayes and regular),
    some selected C dominates it with ψ(C) = ψ(B^s_t ∪ S_ij). So C = B^s_t ∪ S″ with S″ ⊆ G_ij ∪ G′_ij, the tie set
    at t ∈ ℓ_ij°.
  - Apply (IB) with A := (S″ △ S_ij) ∪ −(S″ △ S_ij), D = S″, E = S_ij, contexts F₁ := B^s_t ∪ (S″ ∩ S_ij) and
    F₂ := B^s_{p\*} ∪ (S∖(G_ij∪G′_ij)) ∪ (S″ ∩ S_ij).
  - Both contexts lie in A^c: B^s_{p\*} misses Z_{p\*}; the other carrying atoms have other directions; and
    U ∩ −U = ∅.
  - This transports the domination to B^s_{p\*} ∪ (S∖S_ij) ∪ S″ over D_{T1}, against T1 ∈ C_L.
  - Undominated models are tied with selected ones (Fact 0), so they are coherent by (C).
  - This is N25 Thm 8.2(a), (b), extended from ℓ° to splits of T1 at a crossing point.
- **A = S is admissible.**
  - At q off the chords through p\*: B^A_q = B^s_q.
  - At q ∈ ℓ_ij°: B^s_q ∪ S_ij, by the Claim.
  - At q ∈ ℓ_ij∖ℓ_ij°, q ≠ p\*: only ℓ_ij among the chords through p\* passes through q, so B^A_q = B^s_q ∪ S_ij.
    It is the intersection of the two limits along ℓ_ij from the two sides of q. Those limits are coherent (limits of
    the coherent B^s_{t′} ∪ S_ij, t′ ∈ ℓ_ij°), and they differ only in the atoms of the other chords through q, which
    satisfy u·c ≠ 0 for the direction u of ℓ_ij. By N25 Lemma 3.2 the intersection is coherent.
  - At p\*: D_{T1}.
- Theorem 4.3 (second case) now applies to any carrying atom. ∎

So **Q1 of writeup §8.1 is answered negatively whenever some supporting assessment endorses the relevant comparisons
itself**, in particular for countably additive endorsing weights. Without (E_ψ), only (TP) remains.

---

## 5. Part (B): N17.B′ in two worlds with a nested selection

### 5.1 Setting

This is N17.8, N19 §4. Map the mixed problems of U measure-preservingly onto I = [0,1], in the order in which they
enter world 1's error sets along the selection, so that E₁(C_b) = c_b := [0,b) for b ∈ [0,1], with C_L the path.
- On mixed problems E₂ = I∖E₁, so E₂(C_b) = d_b := [b,1).
- ≤₁ and ≤₂ are the induced cancellative, strictly monotone preorders on measurable subsets of I (N9.4).
- Every measurable A ⊆ I is E₁ of a regular model (accept the non-negative block).

Axioms used:
- (Cl): S₁(A) := {b : c_b ≤₁ A} and S₂(A′) := {b : d_b ≤₂ A′} are closed. They are an initial and a final segment
  of [0,1], by monotonicity along the chain.
- (K): for b ∈ (0,1) and every A, c_b ≤₁ A or d_b ≤₂ A^c (competitiveness of C_b on {1,2}).

SP^reg₁ means: there is a charge ν, positive on non-null sets, with ν(A) ≥ ν(c_b) whenever c_b ≤₁ A. By Lemma R1
(N19), the same as a charge ≥ 0 on 𝔚^reg₁ with countably additive part > 0 a.e.

### 5.2 Two lemmas

**Lemma B0 (PROVED).** S₁(A) = [0,φ₁(A)] with c_{φ₁(A)} ≤₁ A, and φ₁(c_b) = b. Likewise S₂(A′) = [φ₂(A′),1].
Condition (K) is equivalent to φ₁(A) ≥ φ₂(A^c) for all A.

*Proof.*
- Closedness, together with monotonicity along the chain (c_{b′} ⊆ c_b gives c_{b′} ≤₁ c_b).
- Strict (G) gives c_b <₁ c_{b′} for b < b′.
- (K): if φ₁(A) < b < φ₂(A^c), then both alternatives fail at b. ∎

**Lemma B1 (PROVED; strict escape).** If b ∈ (0,1) and A ⊋ c_b (non-null difference), then φ₁(A) > b. Dually, if
A′ ⊋ d_b, then φ₂(A′) < b. More generally, at b\* := φ₁(A) < 1, both c_{b\*} ≤₁ A and d_{b\*} ≤₂ A^c hold.

*Proof.*
- For b′ ∈ (φ₁(A),1), c_{b′} ≰₁ A, so d_{b′} ≤₂ A^c by (K). Closedness of S₂(A^c) gives d_{φ₁(A)} ≤₂ A^c.
- If A ⊋ c_b and φ₁(A) = b, then A^c ⊊ d_b, so A^c <₂ d_b by strict (G), against d_b ≤₂ A^c. ∎

### 5.3 Two kinds of non-Archimedean world

**Proposition B2 (PROVED).**
- (a) Let ν⁺ be a purely finitely additive "right density at x₀ ∈ (0,1)": a charge vanishing on null sets, with
  ν⁺((x₀,x₀+h)) = 1 for every h > 0, for instance a Banach limit of λ(·∩(x₀,x₀+h))/h. The lexicographic world
  ≤₁ = lex(ν⁺, λ) satisfies strict (G), (IB) and **all closed sections S₁**. It fails SP₁: c_{x₀} is 𝓜-null, because
  c_{x₀} <₁ A_j for infinitely many disjoint A_j with ν⁺(A_j) > 0.
- (b) No n = 2 nested system with (Cl), (K) and strict (G) has this world 1.

*Proof.*
- (a)
  - For b ≤ x₀, c_b ≤₁ A iff ν⁺(A) > 0, or ν⁺(A) = 0 and b ≤ λ(A). For b > x₀, ν⁺(c_b∖A) = 1 − ν⁺(A) and
    ν⁺(A∖c_b) = 0, so c_b ≤₁ A iff ν⁺(A) = 1 and b ≤ λ(A).
  - So S₁(A) is [0, min(x₀,λ(A))], [0,x₀] or [0, max(x₀,λ(A))] according as ν⁺(A) = 0, ∈ (0,1) or = 1. All are
    closed.
  - Disjoint A_j ⊆ (x₀,1) with ν⁺(A_j) = 2^{−j} exist. Every charge ≥ 0 on 𝔚 has ν(c_{x₀}) ≤ inf_j ν(A_j) = 0.
- (b) Take A := c_{x₀} ∪ D with D ⊆ (x₀,1) and 0 < ν⁺(D) < 1. Then φ₁(A) = x₀, against Lemma B1. ∎

So closedness alone does not give N17.B′: competitiveness through the other world is needed. The mirror world
lex(ν⁻, λ), with ν⁻ the left density, fails closedness. A diffuse purely finitely additive primary that vanishes on
an initial segment fails closedness by the mechanism of Theorem B3 (checked on one example).

### 5.4 Countable lexicographic worlds with countably additive levels

**Theorem B3 (PROVED).** Let world 1 be lexicographic with countably many countably additive levels w_k ≥ 0 (densities
w.r.t. λ): A ≤₁ B iff (π_k(1_B − 1_A))_k ≥_lex 0, with π_k := w_kλ. Strict (G) means that a.e. x has some w_k(x) > 0.
Put k(x) := min{k : w_k(x) > 0}. If every section S₁(A) is closed, then:
- (i) k is essentially nondecreasing along the chain: R_k := {k(x) = k} = [s_{k−1}, s_k) mod null, with
  0 = s₀ ≤ s₁ ≤ … ↑ 1;
- (ii) for any α_k > 0 with Σα_kπ_k(R_k) < ∞, ν := Σ_k α_k w_k 1_{R_k} λ is strictly positive and satisfies
  ν(A) ≥ ν(c_b) whenever c_b ≤₁ A. So SP^reg₁ holds, and N17.B′ holds at world 1.

No competitiveness is used.

*Proof.*
- (i)
  - Suppose some j and a have Z := {k ≥ j} ∩ [0,a) non-null and {k < j} ∩ (a,1) non-null.
  - Let b₀ ∈ (a,1) be a Lebesgue density point of {k < j} ∩ (a,1), and A := c_{b₀}∖Z. Then A ⊊ c_{b₀}, so
    b₀ ∉ S₁(A).
  - For b′ ∈ (a,b₀): c_{b′}∖A = Z and A∖c_{b′} = [b′,b₀). Now π_m(Z) = 0 for m < j, and [b′,b₀) has positive mass
    at some first level m < j. So v(Z) <_lex v([b′,b₀)), i.e. c_{b′} ≤₁ A.
  - So sup S₁(A) = b₀ is not attained, contradicting closedness.
  - Hence each {k ≥ j} is a final segment mod null. s_k ↑ 1 because k < ∞ a.e.
- (ii)
  - ν is positive on non-null sets, since w_k > 0 on R_k. Note that π_m vanishes on R_{>m}.
  - Let c_b ≤₁ A with b ∈ [s_{j−1}, s_j) (b = 1 forces A = I). Then A∖c_b ⊆ [b,1) ⊆ R_{≥j}, so π_m(A∖c_b) = 0 for
    m < j.
  - Inductively, lex-≤ forces π_m(c_b∖A) = 0 for m < j, hence (c_b∖A) ∩ R_m is null.
  - At level j: π_j(c_b∖A) ≤ π_j(A∖c_b). The left side is ν([s_{j−1},b)∖A)/α_j = ν(c_b∖A)/α_j. The right side is
    π_j(A ∩ [b,s_j)) = ν(A∩[b,s_j))/α_j ≤ ν(A∖c_b)/α_j.
  - Hence ν(c_b) ≤ ν(A). ∎

NUMERICS (`p4py/lex_n2.py`, exact rationals; output in `p4py/lex_n2.out`):
- out of order: the section of A = c_b∖(Z ∩ c_a) contains b − η for η = 10⁻²…10⁻⁷ but not b;
- in order: 9394 sampled comparisons c_b ≤₁ A, no violation of ν(A) ≥ ν(c_b).

*Reading.* Every (M2)-world of lexicographic type with countably additive levels must start its chain on its primary
level. A "secondary-first" chain makes the section of a slightly trimmed initial segment open at its right end. That
is the closedness phenomenon N19 §4 observed in one example, now a theorem for the whole class.

### 5.5 What is open in n = 2

Let 𝓜 := {probability charges ν ≥ 0 on 𝔚^reg₁}. It is nonempty: (NC⁺_𝔚) holds for nested chains (N17.3).

By N22 Lemma 1.1 / Thm 1.2 and Lemma R1 (PROVED there), SP₁ fails iff some non-null B is 𝓜-null. By separation in
L^∞ (PROVED, standard), that holds iff for every ε > 0 there are λ_k ≥ 0 and comparisons c_{a_k} ≤₁ A_k with

  1_B + Σ_k λ_k(1_{A_k} − 1_{c_{a_k}}) ≤ ε  a.e.

**CONJECTURE N17.B′(2).** In an n = 2 nested system, (Cl) at both worlds together with (K) excludes such
certificates.

Excluded so far:
- every certificate whose world 1 is of valuation type with countably additive levels (Theorem B3);
- jump-type purely finitely additive levels (Prop B2).

Not excluded: incomplete or non-valuation worlds. The minimal shape of a certificate is "c_a ≤₁ A_j for infinitely
many disjoint A_j". By Lemma B1 any such world must keep φ₁ strictly increasing under every non-null addition to
every initial segment.

---

## 6. n = 3 (cyclic)

**Lemma B4 (PROVED; removal lemma, any n).** Let world i be lexicographic with countably many countably additive
levels, with v = (π_k)_k. Suppose a selected C_{p₀} has a non-null part Z′ of E_i(C_{p₀}) on which the levels below j
vanish. Suppose also there are indices p_m → p₀ with v_{<j}(E_iC_{p_m}) <_lex v_{<j}(E_iC_{p₀}). Then (S) fails.

*Proof.*
- Let X be regular with E_i(X) = E_i(C_{p₀})∖Z′. Then X ≺_i C_{p₀}, so p₀ ∉ A_i(X).
- v(E_iX) agrees with v(E_iC_{p₀}) below level j. So v(E_iC_{p_m}) <_lex v(E_iX), i.e. C_{p_m} ⪯_i X by additivity
  of v on symmetric differences.
- So A_i(X) is not closed. ∎

*Why n = 2 does not transfer.* Theorem B3 used two things.
1. Approach from below at level 1, for free. It came from the totally ordered chain: every b₀ is approached by
   b′ < b₀ with strictly smaller error sets.
2. For Lemma B1, a complementary world: E₂ = I∖E₁.

In n = 3:
- the selection is two-dimensional;
- world-i error sets of selected models cross (N17.3: (M1) certificates *must* be cyclic with crossing error sets);
- a selected model can be a local minimum of the first-level valuation over the selection without being the
  world-i ideal, so (1) can fail;
- E_j ≠ U∖E_i, so (2) has no analogue.

Lemma B4 therefore excludes a lexicographic world i only at points where the selection improves world i's first level
from below. A cyclic (M1) certificate needs no such point.

**What an n = 3 counterexample to N17.B′ must do** (PROVED necessary conditions, from N17.3, Lemma B4 and
Theorem B3's mechanism):
- at the failing world i, either an (M1) certificate (≥ 4 comparisons out of members of C_L, overlapping gains,
  crossing error sets, cyclic), or an (M2) failure;
- if world i is lexicographic with countably additive levels, every selected model that errs on a deep-level set must
  be a local minimum of the shallow-level valuation along the selection;
- every section A_i(X) must be closed for **every** model, including the trimmed models of Lemma B4.

No such system is known. The n = 3 cyclic case of N17.B′ is **open**.

---

## 7. The resulting statement, and what a positive construction must do

**Theorem P4 (PROVED, assembling Theorems A1–A3, Cor 4.4).** Let a ranking on M_U satisfy strict (G), (IB), (LA), (S),
(C) and cover T1. Then one of the following holds.
- **(i)** Some world fails SP^reg: no charge ≥ 0 on its relevant comparisons is positive on mixed problems. This is
  mode (M1) or (M2), and it is not excluded.
- **(ii)** Every world adds up, and for **every** supporting assessment ψ ∈ 𝒩:
  - (E_ψ) fails, so in particular some endorsing weight has a non-trivial purely finitely additive part;
  - the target weighting is a common point of at least three atom chords;
  - T1's tie-split is carried by three corner atoms with positively spanning normals, each straddling ∂D_{T1}
    along its corner arc (configuration (TP)).

If (TP) were excluded and N17.B′ proved, the ordinal route for T1 on M_U would be closed (modulo charges, i.e. modulo
the purely finitely additive parts of endorsing weights in (ii)). Neither is done here.

**What a positive construction must do.**
- **Through M0:** build a strictly signed integral field ψ on M_U with a.e.-coherent Bayes models, in which:
  - T1 is a Bayes model at a triple point p\* of three atom chords;
  - the three corner atoms straddle ∂D_{T1};
  - no admissible tie-breaking family passes through T1.
  Then build the ordinal ranking. It must:
  - break the ties so that T1 ∈ C_L;
  - endorse the relevant comparisons only through charges with purely finitely additive parts, because (E_ψ) must
    fail;
  - fail to make the partial splits B^s_t ∪ (S ∩ G_ij) coherent along the chords (otherwise Theorem 4.3 applies).
  The two-world mechanism of N26.1 does not do this: in it (E_ψ) holds, and the tie is on one chord.
- **Through M1/M2:** some world must fail SP^reg.
  - In the n = 2 analogue this is impossible for countable lexicographic worlds with countably additive levels
    (Theorem B3).
  - Jump-type purely finitely additive levels are impossible (Prop B2), given competitiveness.
  - So a construction needs a non-valuation (incomplete) world with closed sections and strict escape (n = 2), or a
    cyclic arrangement of crossing error sets with no approach from below (n = 3).

---

## 8. Status table

| Claim | Status |
|---|---|
| Lemma 2.1 quasi-linearity of every tie-breaking family, for every g | PROVED |
| Lemma 2.2 admissible families: continuity off E, vertex limits, exact charts up to ∂H ∩ E | PROVED |
| Lemma 2.3 ball lemma (from Prop F's (★)) | PROVED (rests on N25_referee Prop F step 2 and (★), one reader) |
| Lemmas 2.4, 2.5 shell lemmas | PROVED; NUMERICS agree |
| Lemma 2.7 PL2 for K^♭ across chords; Lemma 2.8 nopin for admissible families | PROVED |
| Theorem 3.1 §4 chain for K^♭ (p\* ∉ E) | PROVED (step-by-step audit; a second reader should recheck Step 4 and the anchor choice in Lemma rotation) |
| **Theorem A1: p\* ∈ E(ψ) for every ψ ∈ 𝒩 (R-b′ closed)** | **PROVED** |
| Prop 4.1 carrying atoms; full in the single-chord, ≤ 2-atom and half-plane cases | PROVED |
| Lemma 4.2, Theorem 4.3 (short argument) | PROVED |
| Cor 4.4 residual (TP) | PROVED as a necessary condition |
| **Theorem A3: under (E_ψ) (e.g. countably additive weights) no M0 cover** | **PROVED** (uses N25 Lemma 1.2, Lemma 8.1, Fact 0, (C)) |
| (TP) without (E_ψ) | open |
| Lemma B0; **Lemma B1 (strict escape)** | PROVED |
| Prop B2 (closed but non-SP pfa world, excluded by strict escape) | PROVED |
| **Theorem B3 (N17.B′ for countable lexicographic worlds with countably additive levels, n = 2 nested)** | **PROVED** |
| N17.B′(2) in general; n = 3 cyclic | CONJECTURE / open |
| Lemma B4 removal lemma (any n) | PROVED |

**Hypotheses added: none.** (E_ψ) is used only in Theorem A3, where it is the hypothesis of the statement. Nestedness
in §5 is the hypothesis of the n = 2 case as stated in N19 §4.

## 9. Files (`p4py/`, run with `python3 -I`)

- `shells.py` (+ `.out`): Lemmas 2.4–2.5 sanity checks.
- `lex_n2.py` (+ `.out`): Theorem B3 sanity checks (non-closed section out of order; endorsement in order).
