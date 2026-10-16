# B2 — Exceptional ties at the target weighting on general decomposable domains (round 14)

Scripts: `b2py/geom_checks.py` (+ `.out`), `b2py/random_triangles.py` (+ `.out`).
Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. "PROVED (B2)" means proved in this note, not yet refereed.

---

## 0. Outcome

**No construction.** This is the failure report.

**The plan.** Cover T1 on a two-sided decomposable domain with a ranking whose worlds add up (M0). Its supporting additive assessment ψ would have exceptional ties at the target weighting p\*. The ranking would break those ties ordinally, as in N26.1, with T1 an intermediate face model. On M_U this is excluded by Theorem M0closed. That proof needs the ball lemma at p\*, and the ball lemma fails on two-sided domains for exactly one new kind of tie: the **apex (fan) tie**, where accept, silence and reject are all optimal at p\* (§2). So the natural design was a fan at p\*. Its apex ties would let the directional face models escape crossing pinning, and the routes of Theorem gm would then never start (§3).

**Where it broke: at p\* itself.** Theorem B2.1 below (PROVED (B2)) holds on every decomposable domain containing D_{T1}, with or without (LF). Let ψ be a strictly guiding integral field with (γ) whose Bayes models at p\* include D_{T1}. Then:
- **crossing pinning holds for every coherent p\*-Bayes model K** (P_K = 0 at the six crossings);
- **every such K contains T1**, so T1 is the most decisive face model;
- **p\* carries no apex (fan) tie and no accept-versus-reject tie.**

**The single obstruction** is the mechanism behind B2.1: the *lexicographic vertex limits* (the world-i-best p\*-Bayes models) K^1, K^2, K^3.
- K^c is pinned at the c-crossings, by a two-line argument that needs no ball lemma.
- Any face model that escapes pinning forces e_c ∈ K^c. That propagates to K^a = {e_a} for every a, which is impossible (Lemmas 5–9).

So the fan design is dead. The only ties left at p\* are U-domain-type c-atoms of corner pattern ("full" ones: they never straddle ∂D_{T1}).

**What remains open.** I could not close it, and say exactly where the U-domain argument stops transferring:
- **(R2) Full corner c-atoms through p\*.** On M_U this is closed by Prop carrying (d), which uses that an atom's ties persist along its whole chord. On two-sided domains the chord of a c-atom is cut at the apexes of its gambles, and d-atoms on the same line can add tied levels (§5). Only when there is one such atom at each of the three corners can T1 be an intermediate face model. That is the only place an N26.1-type ordinal tie-breaking could still matter.
- **(p\* ∉ E)** Theorem gm with (BU) only off a null set E ∌ p\*. Route I1 survives every exceptional set that stays away from p\* (CHECKED audit, §6). It is open only if E accumulates at p\*, or if (TS) or edge confinement fail for (γ)-fields.

On M_U, B2.1 gives a new, short proof of the "p\* ∈ E" half of Theorem M0closed(a), up to (R2), which Prop carrying (d) closes there (Remark 5.3).

---

## 1. Setting; the M0 reduction on decomposable domains

n = 3, ε ∈ (0,1), T1 as in the write-up.
- **Domain:** M is a decomposable domain with D_{T1} ∈ M. (LF) is used only in §5.
- **Penalties:** ℓ_i(g,a), a ∈ A(g), with an integrable envelope, strictly increasing in world-i rank on A(g) for a.e. g (strict guidance, R1 Lemma 1.1).
- **Optimal advice:** for x ∈ Δ°, A\*_x(g) := argmin_{a∈A(g)} x·ℓ(g,a).
- **Face model at x:** a coherent D_K ∈ M with a_{D_K}(g) ∈ A\*_x(g) for a.e. g.
- **Penalty vectors** (for a pair whose range contains {+,0,−}): c := ℓ(0) − ℓ(+), c′ := ℓ(0) − ℓ(−), d := c − c′. They carry the strict sign patterns of g, −g and g.
- **Ranks:** for g with g_i ≠ 0, ≺_i is good ≺ silence ≺ bad ≺ ×.

**(γ)** For a.e. q ∈ Δ° the q-Bayes model is a.e. unique and coherent.

**(α\*)** D_{T1} is ψ-Bayes at some x = p\* ∈ Δ°.

**Prop B2.0 (CHECKED; transfer of imports).**
- *Definition.* On a general domain, world i *adds up* if some bounded strictly guiding penalty λ_i and some finitely additive ν_i, positive on non-null sets of problems with non-singleton advice range, satisfy ν_i(λ_i(·,a_B)) ≤ ν_i(λ_i(·,a_X)) for every relevant comparison B ⪯_i X (B ∈ C_L, X regular). On M_U with the error indicator this is write-up Def. addup.
- *Supporting assessment.* ψ_i := ∫ λ_i ρ_i dμ, where ρ_i is the density of the countably additive part of ν_i.
- *Claim.* Under strict (G), (IB), (LA), (S), (C), T1 ∈ C_L and (M0), ψ satisfies (α\*), (β), (γ), (δ).
- *Status.* This is the status of N13 Prop B, which is stated for decomposable domains, together with N19 Prop R3(a), the restriction to relevant comparisons. Its proof uses only regularity, which is domain-free.

---

## 2. Tie anatomy on two-sided domains

The new phenomenon is entirely in point 2.

1. **Line ties (PROVED (B2), Lemma 7 below).** A tie at x is a *line tie* when exactly two advices are optimal:
   - **c-tie:** c·x = 0 > c′·x;
   - **c′-tie:** c′·x = 0 > c·x;
   - **d-tie:** d·x = 0 < c·x = c′·x.

   Near x the two regions are separated by one line through x. Prop F steps 1–4 (N25_referee §2; three readings) transfer verbatim to line ties. Two nearby fibres with long tie intervals share their line. Since a line through x separates the vertices exactly as the sign pattern of g does, **no ball centred on a coordinate plane is filled with line ties.**
2. **Apex ties.** Here c·x = c′·x = 0 with c ∦ c′: all of +, 0, − are optimal at x.
   - The three cells are sectors with common apex x. Along a fibre the nested wedges share the apex but not their boundary lines, so step 2 of Prop F ("nested half-planes through x coincide") fails.
   - This is the **only** tie type that escapes the ball lemma, and so the only way crossing pinning (write-up Prop crosspin) could fail at p\*.
   - Each g has at most one apex. So the *fan points* {x : apex ties at x non-null} are countable (PROVED (B2)).
   - E ⊆ (countable union of lines) ∪ (countable set) (PROVED (B2)):
     - pencils through distinct points share one line;
     - the non-atomic part of the push-forward of μ to lines charges only countably many pencils;
     - atoms of that push-forward give atom lines.
3. **Vertex-segment rule (PROVED (B2)).** If g has an apex tie or a d-tie at x, then on the whole open segment (x, e_a) the Bayes advice on g is e_a's advice (accept iff g_a > 0).
   - *Apex tie:* c·(x + s(e_a − x)) = s·c_a.
   - *d-tie:* (1−s)c·x + s·c_a > 0 when g_a > 0, and (1−s)c′·x + s·c′_a > 0 when g_a < 0.

---

## 3. The construction attempted (design)

**Design.**
- **Place ties at p\*:** a non-null set O of apex ties at p\*, containing a ball around each crossing-ball centre w ∓ s(𝟙 − e_c).
- **Directional face models:** let K(θ) be the limit of the Bayes models along the ray p\* + sθ. Then each K(θ) may have P_{K(θ)}(w) ≠ 0. This blocks the chain of §4 at p\*, which blocks (TS), (PC), (NS), and with them all three routes of Theorem gm, which start from them.
- **Target:** T1 sits inside the ψ-face as an intermediate model.
- **Ordinal tie-breaking:** done N26.1-style, choosing comparisons through the exact test with (R5).

**Structure such a fan must have** (PROVED (B2)):
- by the vertex-segment rule, the ray towards e_a carries e_a's advice on O;
- along d-rays of the continuous part of the fan, K is a single boundary point of Δ;
- a fan with all mixed gambles apex-tied would need a boundary curve that a.e. line through Δ° meets exactly once.

**Why it fails:** Lemmas 5–9 show that a fan escaping crossing pinning leads to that last situation, which is impossible (Lemma 9).

---

## 4. Theorem B2.1 and its proof

**Theorem B2.1 (PROVED (B2)).**

*Hypotheses.*
- M is a decomposable domain with D_{T1} ∈ M; ψ is a strictly guiding additive field with integral penalties on M.
- (γ) holds, and D_{T1} is ψ-Bayes at x ∈ Δ°.
- Let 𝒲 := {m ∈ Δ : m·w ≥ 0 for the six crossings w}. This is the *tangent hexagon*: T1 together with three caps cap_ij = co(v_i, v_j, o_ij) beyond the edges of T1 (CHECKED; NUMERICS G3).

*Conclusions.*
- **(a) Lexicographic vertex limits.** For each i, the model D^i that picks the world-i-best element of A\*_x(g) is coherent, D^i = D_{K^i}, and T1 ⊆ K^i ⊆ co(T1 ∪ {e_i}).
- **(b) Crossing pinning.** Every face model K at x has P_K(w) = 0 at the six crossings. Hence K ⊆ 𝒲, and K touches the six tangent lines.
- **(c) Containment.** Every face model at x contains T1. So D_{T1} accepts, and rejects, every gamble that some face model accepts, or rejects.
- **(d) Tie types.** For a.e. g, A\*_x(g) ∈ {{+}, {0}, {−}, {+,0}, {0,−}}. There are no apex ties (x is not a fan point) and no d-ties at x.

The same holds for every all-facing triangle in general position: CHECKED. The geometric facts used are G1, G2, G4–G7, rerun on 300 random all-facing triangles with no failure (NUMERICS, `random_triangles.out`).

### Proof

Crossings: w^k_c ∈ relint F_k has (w^k_c)_c = 0, and ℓ_{w^k_c} = line(v_k, e_c) is a tangent line from e_c (G2). Put C_i := co(T1 ∪ {e_i}).

**Lemma 1 (lexicographic limits).**
- For θ ∈ 𝟙^⊥∖0, let D^θ choose argmin_{a ∈ A\*_x(g)} θ·ℓ(g,a). For a.e. θ, D^θ is coherent and is the limit in measure of the Bayes models at x + sθ.
- The model D^i := D^{e_i − x} is coherent. Its advice is the world-i-best element of A\*_x(g). Hence a_{D^i}(g) ⪯_i a_X(g) a.e., for every x-Bayes X.

*Proof.*
- For each g, x + sθ has the same minimisers as the pair (x·ℓ, θ·ℓ) ordered lexicographically, for s < s_0(g).
- For fixed g, ties in θ·ℓ on A\*_x(g) occur along at most three directions. So for a.e. (θ, g) the lexicographic minimiser is unique.
- By (γ) and Fubini in polar coordinates at x, for a.e. θ the Bayes models at x + s_mθ are coherent along some s_m ↓ 0. They converge a.e. to D^θ, and limits in measure of coherent cones are coherent (R1 Prop 3.1).
- At θ_i := e_i − x we have θ_i·ℓ = ℓ_i − x·ℓ, which is ℓ_i up to a constant on A\*_x. By strict guidance its minimiser is unique and is the world-i best. So D^θ → D^i a.e. as θ → θ_i, and D^i is coherent.
- D^i ∈ M, because M is closed in measure. ∎

**Lemma 2 (betweenness).**
- (K1) K^i ⊆ C_i.
- (K2) If T1 is silent on g (it straddles or touches ℓ_g), then K^i does not reject g when g_i > 0, and does not accept g when g_i < 0.

*Proof.* Lemma 1 with X = D_{T1}. For (K1): K^i accepts D_{T1} ∩ {g_i > 0} = D_{C_i}. ∎

**Lemma 3 (support).** If a credal set K has P_K = 0 on a relatively open subset of e_c^⊥, then e_c ∈ K.

*Proof.* Let m_0 ∈ K be a minimiser at a point g_0 of the open set. Then m_0·g ≥ 0 on an open cone of e_c^⊥, with equality at its interior point g_0. So m_0 vanishes on e_c^⊥, and m_0 = e_c. ∎

**Lemma 4 (own-vertex pinning).** P_{K^c}(w) = 0 at both c-crossings.

*Proof.*
- **Case P_{K^c}(w) > 0.**
  - On a small ball B around g_1 := w − s(𝟙 − e_c), K^c accepts and T1 is silent:
    - P_{T1}(g_1) ≤ −s(1 − m_c) < 0, where m ∈ T1 attains P_{T1}(w);
    - P̄_{T1}(g_1) > 0, since P̄_{T1}(w) > 0.
  - So {+, 0} ⊆ A\* a.e. on B.
  - B is centred on {g_c = 0}. On B ∩ {g_c < 0} the world-c best element of A\* is 0 or −, never +. This contradicts K^c accepting.
- **Case P_{K^c}(w) < 0.** On a ball around w + s(𝟙 − e_c), T1 accepts and K^c does not. On its part with g_c > 0, + is world-c best and lies in A\*, so K^c would accept. Contradiction. ∎

**Lemma 5 (escape forces the vertex).** If some face model K has P_K(w) ≠ 0 at a c-crossing w, then e_c ∈ K^c.

*Proof.* Take the ball B of Lemma 4 for K: on it, {+, a_K} ⊆ A\* with a_K ≠ + (if P_K < 0), or {+, 0} ⊆ A\* (if P_K > 0).
- On B ∩ {g_c > 0}, D^c accepts.
- On B ∩ {g_c < 0}, D^c does not accept.
- By continuity, P_{K^c} = 0 on B ∩ e_c^⊥. Lemma 3 gives e_c ∈ K^c. ∎

**Lemma 6 (propagation).** If e_c ∈ K^c, then e_a ∈ K^a for all a.

*Proof.*
- If T1 accepts g and g_c < 0, then K^c (∋ e_c) does not accept g. So g is tied at x, since untied gambles get the same advice from every face model.
- Take a ball B_a ⊆ D_{T1} ∩ {g_c < 0} centred on {g_a = 0}. It exists (G7): e.g. g_0 = (g_a = 0, g_b ≫ 0, g_c = −1).
- On B_a, + ∈ A\* and |A\*| ≥ 2. So D^a accepts iff g_a > 0.
- Lemma 3 gives e_a ∈ K^a. ∎

**Lemma 7 (★ for line ties; PROVED (B2), transfer of Prop F steps 1–4).**
- *Setting.* Let B be a ball of gambles in which a.e. g has a c-tie at x.
- *Fibre lines.* Fix n. On fibres g − t𝟙, take the tied levels t at which d(g − t𝟙) > 0 on B(x, 1/n). There the + region is the half-plane {c(g − t𝟙)·q > 0} near x. Nested half-planes through x coincide, so all such levels share one oriented line L(g).
- *Inequalities.* P(q, g) ≥ b_n(g) on one side of L(g) and ≤ a_n(g) on the other, for a.e. q near x.
- *Estimate.* Two fibres with L ≠ L′ at sup-distance d satisfy |J_n(g)| + |J_n(g′)| ≤ 2d.
- *Conclusion.* For every n the sets J_n exhaust J, so fibres with long tie intervals that are close have the same oriented line.
- *Consequence.* The oriented line {c·q = 0} separates the vertices exactly as sign(g) does. So no ball centred on a coordinate plane consists of c-ties. The same holds for c′-ties and d-ties. ∎

**Lemma 8 (collapse).** If e_i ∈ K^i, then K^i = {e_i}.

*Proof.*
- Suppose m\* ∈ K^i ∖ {e_i}. By (K1), m\* ∈ C_i ∖ {e_i} ⊆ Δ°, because C_i ∩ ∂Δ = {e_i} (all-facing; G4).
- On the open set S of gambles whose line strictly separates e_i from co(T1 ∪ {m\*}), oriented T1-positive:
  - T1 accepts, so + ∈ A\*;
  - K^i straddles (e_i negative, m\* positive), so D^i is silent;
  - by Lemma 1, 0 is world-i best in A\*, so − ∉ A\* (since g_i < 0), and A\* = {+, 0}: a c-tie.
- S contains a ball centred on {g_j = 0}, for j ≠ i: lines through e_j cutting the edge [e_i, e_k] near e_i (G7). Lemma 7 then gives a contradiction. ∎

**Lemma 9 (no vertex collapse).** The case K^a = {e_a} for a = 1, 2, 3 is impossible.

*Proof.*
1. *Both acceptances are optimal.* By Lemma 1, for a.e. mixed g both + and − lie in A\*. So g has a d-tie or an apex tie at x.
2. *Direction cells.* For generic θ, D^θ(g) is +, 0 or − according to the cone cells of g in 𝟙^⊥ (both tie types):
   - R₋(g) is an open convex cone of angle ≤ π containing θ_b exactly when g_b < 0;
   - S(g) (silence) is empty (d-tie) or a closed convex cone of angle < π containing no vertex direction θ_a := e_a − x.
3. *The arcs.* Let A_a := {θ generic : e_a ∈ K(θ)}. Take gambles g near the corner line {m_a = 1 − ε/2}, oriented e_a-positive. They give:
   - {θ : K(θ) ⊆ {m_a < 1 − ε}} ⊆ R₋(g_ε) mod null, for one good g_ε (Fubini);
   - the left side increases as ε ↓ 0, so |A_a| ≥ π;
   - R₋(g_ε) ∋ θ_b, θ_c, so A_a misses the gap G_bc and neighbourhoods of θ_b and θ_c.
4. *Overlaps.* Hence |A_a ∪ A_b| < 2π and |A_a ∩ A_b| > 0, and A_a ∩ A_b ⊆ G_ab (the open gap between θ_a and θ_b).
5. *Contradiction.* Take g with g_a, g_c > 0 > g_b (a non-null set).
   - On A_a ∩ A_b, K(θ) contains e_a and e_b, so it straddles ℓ_g and θ ∈ S(g).
   - The same holds on A_b ∩ A_c ⊆ G_bc.
   - So S(g) meets two different gaps in positive measure. But a convex cone that avoids the three vertex directions lies in a single gap. ∎

**Prop 10 (= B2.1(b)).** If (b) failed, Lemmas 5, 6 and 8 would give K^a = {e_a} for every a, which Lemma 9 excludes.
- On each facet, P_K(h(τ)) is concave in τ and vanishes at both crossings. So it is ≥ 0 on the middle arc and ≤ 0 on the corner portions, and K lies on the T1-side of all six tangent lines, i.e. K ⊆ 𝒲. ∎

**Lemma 11 (= the containment in (a)).** K^i ⊇ T1.

*Proof.*
- **The vertices v_k with k ≠ i.** F_k has a corner portion on which h_i > 0 (G6).
  - There P_{K^i}(h) ≥ P_{C_i}(h) = min(0, h_i) = 0 by (K1), and P_{K^i}(h) ≤ 0 by Prop 10.
  - Concavity then gives P_{K^i}(h(τ)) = 0 on [τ_i, 1], an interval of lines through v_k. So v_k ∈ K^i.
- **The vertex v_i.**
  - By Prop 10, K^i ⊆ W_i, the wedge at v_i bounded by line(v_i, e_j) and line(v_i, e_k). W_i is pointed, and e_i lies strictly in the opposite wedge (G5).
  - If v_i ∉ K^i, take a line through v_i that supports W_i only at v_i, and shift it slightly into T1. The resulting lines straddle T1 and strictly separate K^i from e_i: a non-null set of gambles violating (K2).
- **Why this step is needed.** C_i ∩ W_i ⊋ T1 (NUMERICS G10), so (K1) and pinning alone do not suffice. ∎

**Prop 12 (= B2.1(c), (d)).**
- **Containment.** Suppose a face model K lies strictly on the positive side of a line ℓ_g through int T1. Pick i with g_i > 0. Lemma 1 forces D^i to accept g. But K^i ⊇ T1 straddles ℓ_g. Contradiction. So every line through int T1 meets K, and T1 ⊆ K.
- **No ±-ties.** If + and − were both in A\*, then K^i (with g_i > 0) would accept and K^j (with g_j < 0) would reject, and T1 ⊆ K^i ∩ K^j would do both. ∎

---

## 5. Consequences, the residual (R2), and where the U-domain proof stops transferring

**Corollary B2.2 (PROVED (B2), at the status of Prop B2.0 for rankings).** In every ranking on a decomposable domain that adds up at every world and has T1 ∈ C_L, the supporting assessment ψ satisfies:
- the ties at p\* are c-ties only (orienting each pair T1-positive), and D_{T1} accepts all of them;
- every face model lies between T1 and 𝒲.
- In particular p\* is not a fan point, and the fan design of §3 is impossible on every decomposable domain.

**Prop 13 (reduction to (R2); PROVED (B2), using (LF) only for "UVN" below).** Suppose p\* ∈ E. Then:
- **(i) The strict-Bayes model.** D♭ picks the unique optimum, and silence otherwise. It is a coherent face model: by Prop 12 silence is always optimal at a tie, and D♭ is the intersection of countably many generic D^θ.
- **(ii) A cap.** K♭ ⊋ T1 and K♭ ⊆ 𝒲, so K♭ has a point m beyond an edge of T1; say m ∈ cap_12. Then m·r_12 < 0.
- **(iii) The atom.** Take a small ball around r_12 + s𝟙, 0 < s < |P_{K♭}(r_12)|. On it T1 accepts and K♭ is silent, so it consists of c-ties. Lemma 7 makes it part of one oriented c-atom G:
  - c ∝ b on G, with b·p\* = 0 and b of pattern (−,−,+) (G8, G9);
  - G carries the shells h + s𝟙 over corner arcs α ⊂ F_1 and α′ ⊂ F_2 at r_12.
- **(iv) The atom is full.** Every face model accepting G (for example D^θ with θ·b > 0) has P_K ≥ 0 on α ∪ α′ because of the shells, and P_K ≤ 0 by Prop 12. So π⁺ := P_K ≡ 0 there: the atom never straddles ∂D_{T1}.

**Residual (R2).** p\* lies on full corner c-atoms of this kind.
- T1 accepts all of them.
- T1 is an intermediate face model, so that ordinal tie-breaking would matter, **only if there is one at each of the three corners.** Then the normals b positively span 𝟙^⊥ and the face is a zonotope with T1 at its centre. This is P4's triple-point configuration, with full atoms.

**Where the U-domain closing step stops transferring.** On M_U, (R2) is closed by Prop carrying (d), the full-atom case:
- by frozen support (N25 Thm 4.1(e)), for every t on the whole chord L the δ-broken model satisfies P = π⁺ = 0 on α;
- concavity then gives P ≤ 0 on F_1;
- but for t near L ∩ [e_2, e_3], the convex superlevel set of a middle-arc gamble of F_1 (which contains vertex neighbourhoods of e_2 and e_3, by UVN) gives P > 0.

On a two-sided domain this fails at two points:
1. **The chord is cut.** A gamble g ∈ G is a c-tie at q ∈ L only while c′(g)·q < 0. So its tie stops at the apex a_g = L ∩ {c′(g) = 0} and g is strictly rejected beyond it. M_U has no c′, which is why there the tie persists along the whole chord.
2. **Extra tied levels.** d-atoms on the same line L (d ∝ ±b, tied beyond their apexes) can add tied levels to the fibres over α at points t ≠ p\*. That moves the δ-broken lower previsions there.

The argument can be rerun on F_2 at the other end of L, so a construction would have to arrange both:
- the gambles over α have their apexes between p\* and L ∩ [e_2, e_3];
- the gambles over α′ have their apexes between p\* and L ∩ [e_1, e_3].

**Conjecture B2.R (CONJECTURE).** (R2) is empty.

**Remark 5.3 (M_U).** On M_U, Lemma 9 is not needed:
- crossing pinning for K^c (Lemma 4) needs no ball lemma;
- an escape from pinning fails at once: Lemmas 5, 6 and 8 would force K^a = {e_a}, while every model on M_U has K ⊇ K′, and Lemma 7 is the known ball lemma there;
- so Lemmas 1–8, Lemma 11, Prop 12 and Prop 13, followed by Prop carrying (d), give a shorter proof of the p\* ∈ E half of Theorem M0closed(a).

This agrees with the proved theorem, which is a consistency check on Theorem B2.1.

---

## 6. Branch p\* ∉ E: the routes of Theorem gm against an exceptional set

The question is which steps use (BU) at specific weightings. The table is my reading (CHECKED), not refereed.

| Step (write-up) | Where (BU)/coherence is used | Robust to null E with p\* ∉ cl E? |
|---|---|---|
| Thm TS (local chain on B_1), Lemma veccluster, corner equation | every q ∈ B_1 | yes if E ∩ B_1 = ∅. If E accumulates at p\*: open on two-sided domains (on M_U, Prop chainchords; its two-sided analogue would need Lemma 7 at chord points off the countable fan set) |
| Thm TSalways (walls along segments to V_l) | K_Q at points of segments | **not audited**: chords can cut the segments |
| Edge confinement (Cor TSalways(c)) | limits at edge priors | yes, by a direct proof, if + is available for a.e. g with g_i, g_j > 0 near the edge; otherwise via cuts (not audited) |
| Prop edgelimits, Prop clines | every limit of K_q (q ∉ E) at an edge prior; S(g) and R(g) are penalty cells | yes |
| Lemma forcedlines, Lemma window, first proof | P(q,g) = 0 at q ∉ E on segments; joint continuity at one window point q ∉ E | yes |
| Collars (Thm collar), Thm D/T/A (routes I2, C2, short) | precise priors off E; points y ∉ E on crossing chords; vertexfree(iv) | collar ∖ E splits into components, each σ_w or constant; Thm A uses y off E. vertexfree(i) rests on Thm apex/cuts: **not audited** |

**Reading.** Exceptional chords and fans *away from p\** cannot break route I1 once (TS), (PC), (NS) hold at p\* and edge confinement holds. The design the brief suggested (chords breaking all routes simultaneously) can therefore succeed only by breaking those common inputs: (TS) through walls, or the local chain through E accumulating at p\*. I did not find a configuration that does either while keeping (γ). I state none.

---

## 7. Status

| Result | Status |
|---|---|
| Prop B2.0 (M0 reduction on decomposable domains) | CHECKED (status of N13 Prop B + N19 Prop R3(a)) |
| §2: tie types; fan points countable; E ⊆ lines ∪ countable set; vertex-segment rule | PROVED (B2) |
| Lemma 7 (★ for line ties) | PROVED (B2); transfer of Prop F steps 1–4 (three readings) |
| Lemmas 1–6, 8, 9; Props 10, 12; Lemma 11 = **Theorem B2.1** | **PROVED (B2)**, new, not yet refereed; geometric inputs NUMERICS G1–G10 for 10 values of ε |
| B2.1 for every all-facing triangle in general position | CHECKED (NUMERICS: 300 random triangles) |
| Corollary B2.2 (no fan, no ±-tie at p\*; T1 most decisive) | PROVED (B2), at the status of Prop B2.0 |
| Prop 13 (p\* ∈ E ⇒ (R2)) | PROVED (B2) |
| Conjecture B2.R ((R2) empty) | CONJECTURE |
| §6 audit (route I1 robust off p\*) | CHECKED |
| Remark 5.3 (short proof on M_U, modulo Prop carrying (d)) | CHECKED |
| Construction | none |

**Referee priorities:**
1. Lemma 9 (the arcs A_a), and the "generic θ" bookkeeping in Lemma 1.
2. Lemma 7, in particular the uniformity in n.
3. The (K2) step at v_i in Lemma 11.

---

## 8. Scripts (NUMERICS; no verdict rests on them)

**`b2py/geom_checks.py` (output `geom_checks.out`).** For ε ∈ {0.01, 0.05, 1/7, 0.2, 0.3, 0.5, 0.6, 0.8, 0.9, 0.99}:
- G1: facet signs.
- G2: crossings are the tangent lines from the vertices.
- G3: 𝒲 = T1 ∪ 3 caps (200 000 samples).
- G4: C_i ∩ ∂Δ = {e_i}; caps ⊆ C_i.
- G5: pointed wedges W_i, with e_i in the opposite wedge.
- G6: corner portion with h_i > 0, where P_{C_i} = 0.
- G7: witnesses for Lemmas 6 and 8.
- G8: a cap point is negative near r_12; middle arcs are positive.

Also:
- G9: separating lines from cap_12 have pattern (−,−,+), and lines through a vertex and a point of 𝒲 meet T1.
- G10: C_1 ∩ W_1 ⊋ T1.

All pass. The first run reported two spurious failures at ε = 0.99, from sampling windows; the windows were corrected and the corrected tests pass.

**`b2py/random_triangles.py` (output `random_triangles.out`).** G1, G2 and G4–G7 on 300 random all-facing triangles in general position: no failure.
