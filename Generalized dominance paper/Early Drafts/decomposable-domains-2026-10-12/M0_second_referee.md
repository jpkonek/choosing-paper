# M0 second referee report: Prop R.1, Prop R.2, Theorem R (case M0 on the U-domain)

14 Oct 2026, round 11. I am an independent second referee (convex analysis, measure theory). I wrote none of P1, P4, N25, N25_referee or M0_referee.
- Read: BRIEF10; writeup §§2–4 and §7 (also §§8–9 for task 4); N25_notes §§0–5; N25_referee (all, especially Prop F); P4_notes Part A (§§0–4); P1_notes (all); M0_referee (all); "Conditional Shunning of Error" (project copy, for task 4).
- Verdicts: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG. Labels for my own additions: PROVED / CHECKED / NUMERICS.
- Scripts: `m0ref2_py/` (`geometry_check.py`, `hexagon_check.py`, outputs `*.out`; run with `python3 -I`). I also reran the first referee's `m0ref_py/crossing_balls.py` and `transpose_box.py`: outputs identical (`m0ref2_py/rerun_*.out`). No verdict rests on numerics.

---

## 0. Headline

1. **Prop R.1 is correct, and more general than stated.** Its only external input is the ball lemma (P4 Lemma 2.3), applied at x = p\* to the tie set Z_{p\*} of the *field*. The face model K enters only through the identity D_K △ D_{T1} ⊆ Z_{p\*}. No hypothesis of the ball lemma concerns K, so it makes no difference that a directional limit K_δ is only a limit in measure of Bayes models.
   - The hypothesis "p\* ∈ E" is not needed.
   - The argument works at every gamble w ∈ ∂D_T∖0 with a zero coordinate, for any interior target T.
2. **Theorem R is correct.** The case p\* ∈ E is a two-line consequence of R.1, P4 Prop 4.1(i)–(ii), Lemma 4.2 and Theorem 4.3. I re-derived each of these, and each is correct. The case p\* ∉ E is P4 Theorem 3.1. I audited it step by step against writeup §4 and found no gap: every place where §4 used continuity of q ↦ K_q is replaced correctly.
3. **Prop R.2 is correct** (not needed for Theorem R). (TP) is empty, and P1's mid-facet escape is excluded.
4. **The additive form conflicts with no known positive result.** Two places single out T1, one for each branch of the proof:
   - p\* ∉ E: the corner-equation/box algebra (Prop T1, or R15 pinching);
   - p\* ∈ E: Lemma signs, i.e. two relative-interior crossings on every facet and every corner ray in a two-negative orthant.

   Neither holds for normalised boxes, hexagons or other gauge-mixture polygons. Those are covered with E = ∅ in any case. In n = 2 there are no crossings, so N26.1 (a target Bayes at an exceptional weighting) is consistent with R.1.
5. **Status.** Theorem R(a), the additive form, is PROVED. Its new parts have now had two independent readings. Theorem R(b), the ranking form, is PROVED at the status of its imports, writeup Prop M0 (α), (γ) without (E_ψ). Those imports rest on N13 Prop B and N19 Prop R3(a), each proved in a referee report and read once.

Verdict on M0_referee's new results: **R.1 CONFIRMED WITH REPAIR** (the repair strengthens it: drop "p\* ∈ E", and state it for all zero-coordinate boundary gambles). **R.2 CONFIRMED.** **Theorem R CONFIRMED.** Dependency list: **CONFIRMED WITH REPAIR** (some items are missing; see §6).

---

## 1. Verdict table

| Item | Verdict | Note |
|---|---|---|
| Ball lemma (P4 2.3), with Prop F steps 1–4 | **CONFIRMED** | Re-derived (§2.1). Third reading of Prop F steps 1–4. Step 5 (no fans) is not used |
| Prop R.1 (crossing pinning) | **CONFIRMED WITH REPAIR** (strengthening) | §2.2. Holds without p\* ∈ E and for any interior target at any zero-coordinate boundary gamble |
| Prop R.2 (no face model positive on a middle arc) | **CONFIRMED** | §2.4. Strictness at w and the hull-of-opposite-sectors step are checked |
| Theorem R, steps 1–5 | **CONFIRMED** | §2.3. The dichotomy in step 3 is exhaustive, since π⁺ ≥ 0 on α |
| (TP) empty; mid-facet atoms excluded | **CONFIRMED** | §3 |
| P4 Lemma 2.1 (quasi-linearity) | **CONFIRMED** | Pointwise sandwich B^A_{q₁} ∩ B^A_{q₂} ⊆ B^A_q ⊆ B^A_{q₁} ∪ B^A_{q₂} |
| P4 Lemma 2.2 (a), (b), (d) | **CONFIRMED** | (d): a convex set a.e. equal to an open half-plane H contains H and lies in cl H, by the interior-of-closure argument |
| P4 Lemma 2.4 (a), (b) | **CONFIRMED** | (b): the negative set of a linear functional on a 2-cone is an end sub-cone; no crossing, by the R.1 ball |
| P4 Lemma 2.5 | **CONFIRMED** | — |
| P4 Lemma 2.7 (PL2 for K^♭) | **CONFIRMED** | §4.2. Step 1 is the only new idea, and it is sound |
| P4 Lemma 2.8 (nopin) | **CONFIRMED** | §4.2 |
| **P4 Theorem 3.1 / A1** | **CONFIRMED** | §4.1, step-by-step table |
| P4 Prop 4.1 (i), (ii) | **CONFIRMED** | — |
| P4 Lemma 4.2 | **CONFIRMED** | — |
| **P4 Theorem 4.3** | **CONFIRMED** | §4.3. Needs φ_t = 0 only on a sub-interval J |
| N25 Thm 2.1, Lemmas 3.1–3.2, Thm 3.3, Thm 4.1 (a), (b), (d), (e), (f) | **CONFIRMED** (re-read) | — |
| Writeup Prop M0 (α), (γ) without (E_ψ) | **not re-derived** (imported) | It sets the status of Theorem R(b) (§7) |
| Theorem R(a), additive form, "no conflict with positive results" | **CONFIRMED** | §5 |
| Corollaries in M0_referee §7 | **CONFIRMED** | ¬M0 ⇔ some world fails SP^reg, by N19 Lemma R1 in one direction and trivially in the other |
| Scope claim "every all-facing triangle in general position" (CHECKED there) | **CONFIRMED at CHECKED level** | §5.3. Inputs verified on 2000 random all-facing triangles (NUMERICS) |

---

## 2. Re-derivations

Standing data:
- c is strictly signed on U, and B_q = D_{K_q} for a.e. q ∈ Δ° (property (γ); E is then null by Tonelli);
- p\* ∈ Δ°, and D_{T1} = B^s_{p\*} ∪ S with S ⊆ Z_{p\*};
- a *p\*-face model* is a coherent D_K = B^s_{p\*} ∪ R mod null, with R ⊆ Z_{p\*}. It satisfies D_K ⊆ U, because an open convex set that lies in the open convex set U up to a null set lies in U (separate a point outside U from U).

### 2.1 Ball lemma (and Prop F steps 1–4)

- **Good gambles.** By Fubini on {(q,g) : 1[q·c(g) > 0] ≠ 1[P(q,g) > 0]}, a.e. g is good. Only q ∉ E are involved, so x ∈ E costs nothing.
- **One line per fibre.** Take t < t′ with h_t, h_{t′} good.
  - P(q,h_t) = P(q,h_{t′}) + (t′ − t), so H(h_{t′}) ⊆ cl H(h_t) up to null sets, hence H(h_{t′}) ⊆ cl H(h_t).
  - If both lie in Z_x, both boundary lines pass through x ∈ Δ°. An open half-plane inside a closed one, with both boundaries through an interior point, forces the same line with the same orientation.
- **(★).**
  - Cliff: P(q,g) ≥ b(g) a.e. on H(L), and P(q,g) ≤ a(g) a.e. on the open opposite side.
  - On the sector S₊₋, b(g) ≤ P(q,g) ≤ P(q,g′) + d ≤ a(g′) + d. Symmetrically on S₋₊.
  - If L′ = −L, take S₊₋ = H(L).
  - Adding gives |J(g)| + |J(g′)| ≤ 2d.
- **Ball.**
  - The fibres through a smaller concentric ball meet O in intervals of length ≥ η, and a.e. such fibre is a.e. good and tied.
  - (★) forces equal lines for fibres within distance < η. The essential line is locally constant on a disc, hence constant.
  - aff Δ spans ℝ³, so an oriented line through x fixes c up to a positive factor. Strict signs then give a single orthant.

**CONFIRMED.**

### 2.2 Prop R.1

Let w ∈ ∂D_{T1}∖0 with w_c = 0. Put P_{T1}(w) = 0, and let m_w ∈ T1 attain it.
- *g₁ = w − s(𝟙 − e_c).*
  - (g₁)_c = 0 and P_{T1}(g₁) ≤ m_w·g₁ = −s(1 − m_{w,c}) < 0.
  - P_K(g₁) ≥ P_K(w) − s, because min_K m·(𝟙 − e_c) ≤ 1.
  - If P_K(w) > 0, a ball around g₁ lies in D_K ∖ cl D_{T1} ⊆ D_K △ D_{T1} ⊆ Z_{p\*}.
- *g₂ = w + s(𝟙 − e_c).*
  - P_{T1}(g₂) ≥ s(1 − max_{T1} m_c) > 0, and P_K(g₂) ≤ P_K(w) + s.
  - If P_K(w) < 0, a ball around g₂ lies in D_{T1} ∖ cl D_K ⊆ S ⊆ Z_{p\*}.
- *Contradiction.* Either ball is centred on {g_c = 0}, so it has non-null parts in two orthants, against the ball lemma at p\*.
- *Concavity.* With zeros at τ_i < τ_j: for τ < τ_i, 0 = φ(τ_i) ≥ λφ(τ) + (1−λ)φ(τ_j) = λφ(τ) with λ > 0, so φ(τ) ≤ 0. Likewise for τ > τ_j. Moreover φ ≥ 0 on [τ_i, τ_j].

On the hypotheses at directional limits:
- The ball lemma is a statement about Z_{p\*}, a set of gambles defined by the field.
- K_δ is used only through D_{K_δ} = X_δ(p\*) = B^s ∪ (Z ∩ {δ·c > 0}) a.e. That identity is N25 Lemma 3.1, whose coherence claim is exactly the limit-in-measure statement.
- So nothing about K_δ beyond coherence is needed, and coherence is supplied.

**Repair (strengthening; PROVED by the argument above).**
- "If p\* ∈ E" can be dropped. If Z_{p\*} is null, no ball lies in it.
- The proof never uses that w lies in relint F_k, nor that T is a triangle. For any interior T, every p\*-face model K has P_K = 0 at every zero-coordinate gamble of ∂D_T∖0.
- What is T1-specific is the *location* of these gambles: two in the relative interior of each facet. That location is what produces "≤ 0 on the corner portions" (§5).

NUMERICS (`geometry_check.py` §4): 450 crossing constructions at 25 values of ε, with 0 failures of (g₁)_c = 0, P_{T1}(g₁) < 0, (g₂)_c = 0 and P_{T1}(g₂) > 0.

### 2.3 Theorem R

1. *p\* ∉ E is impossible.* P4 Theorem 3.1 (§4.1).
2. *p\* ∈ E.*
   - S is non-null (Prop 4.1(i)). If it were null, every generic K_δ would satisfy K_δ ⊆ T1. A proper subset misses a vertex v_k and is positive on all of relint F_k, crossings included, which contradicts R.1. So K_δ = K_{−δ} = T1, and Z_{p\*} is null.
   - K^♭ := K^♭_{p\*} ⊋ T1, and D_{T1} ∖ D_{K^♭} = S ⊆ Z_{p\*}. By Lemma 2.4(b), A(K^♭) is a union of at most three open arcs, each around a corner ray and free of crossings.
   - Over each arc α the shell {h + s𝟙 : 0 < s < |P^♭(h)|} is open, connected and contained in Z_{p\*}. By the ball lemma it lies in a single atom G with c ∝ b. Since G ⊆ Z_{p\*}, p\*·b = 0. So G lies on a chord ℓ through p\* and has a corner pattern.
3. *h ∈ α ∩ relint F_k (a non-empty open interval of a corner portion).*
   - Lemma 4.2 gives π⁺(h) ≥ 0 and π^♭(h) ≤ −|P^♭(h)| < 0. Here π⁺ = P_{K⁺(t)} and π^♭ = P_{K^♭_t}, frozen for t ∈ ℓ°. They are well defined at h because the fibre through h meets G in the non-null set {h + s𝟙 : 0 < s < |P^♭(h)|}.
   - Since π⁺ ≥ 0 and is continuous, either π⁺ ≡ 0 on the open interval α ∩ relint F_k or π⁺(h) > 0 at some h there. The first alternative is killed by Theorem 4.3.
4. *If π⁺(h) > 0.* Fix t ∈ ℓ° and a generic δ with δ·b > 0. For 0 < s < π⁺(h):
   - P_{K⁺(t)}(h − s𝟙) > 0 > P_{K^♭_t}(h − s𝟙). So h − s𝟙 has a neighbourhood N ⊆ D_{K⁺(t)} ∖ cl D_{K^♭_t}, and N ⊆ G mod null (N25 Thm 4.1(d)).
   - G ⊆ Z_{p\*} ∩ {δ·c > 0} ⊆ D_{K_δ}. An open convex set containing a.e. point of the open set N contains N.
   - Hence P_{K_δ}(h) > s > 0.
5. h lies in a corner portion, so R.1 gives P_{K_δ}(h) ≤ 0. Contradiction.

**CONFIRMED.**

### 2.4 Prop R.2

Suppose φ_K(τ₀) > 0 with τ₀ ∈ (τ_i, τ_j).
- *Shape of φ_K.* By concavity, φ_K > 0 on (τ_i, τ_j) and φ_K < 0 on (τ_j, 1]: τ_j lies between τ₀ and τ, and φ(τ₀) > 0.
- *Two atoms.*
  - The outer shell over M is contained in D_K ∖ cl D_{T1} ⊆ Z_{p\*}, and the inner shell over C in D_{T1} ∖ cl D_K ⊆ Z_{p\*}. Both are open and connected, and the ball lemma gives atoms G_m and G_c.
  - Their patterns, (−_k, +, +) and (−_k, +_i, −_j), are neither equal nor opposite, so the chords are distinct lines through p\*.
- *Fibre bounds and cliff (N25 Thm 4.1(f)).*
  - For q ∉ E: P(q,·) > 0 on M on H⁺_m, and ≤ 0 on M on H⁻_m.
  - P(q,·) ≥ 0 on C on H⁺_c, and < 0 on C on H⁻_c.
- *Values at w = h(τ_j).*
  - On H⁺_m ∩ H⁺_c: concavity gives φ_q(τ_j) ≥ λφ_q(τ_a) + (1−λ)φ_q(τ_b) with φ_q(τ_a) > 0, φ_q(τ_b) ≥ 0 and λ > 0. So φ_q(τ_j) > 0, **strictly** (checked).
  - On the two opposite sectors the one-sided limits give φ_q(τ_j) = 0.
- *Contradiction.*
  - {P^♭(·,w) ≤ 0} is convex (P4 Lemma 2.1 with A = ∅) and contains (opposite sectors) ∖ E.
  - A convex set containing co-null subsets of two vertically opposite open sectors contains a point of the third sector off E. For z = λa + (1−λ)b, perturb a and set b′ = (z − λa′)/(1−λ); this is an affine bijection, so a.e. a′ has a′, b′ ∉ E.
  - At that point P(q,w) > 0. Contradiction.
- *Consequences.*
  - P_K ≤ 0 on ∂D_{T1}∖0 = ⋃F_k. Since g − P_{T1}(g)𝟙 ∈ ⋃F_k, this gives P_K ≤ P_{T1}, i.e. K ⊇ T1.
  - Over a countable dense set of generic δ: Z_{p\*} ⊆ D_{T1}, i.e. S = Z_{p\*}.

**CONFIRMED.** NUMERICS for the sector-hull step: 20000 random line pairs, 0 failures (`geometry_check.py` §5).

---

## 3. (TP) and mid-facet atoms

- **(TP) is empty.**
  - (TP) requires partial carrying atoms (P4 Cor 4.4), i.e. π⁺ > 0 somewhere on the corner-portion part of the arc.
  - Steps 4–5 of §2.3 turn any such point into a face model K_δ positive on a corner portion, against R.1.
  - Full atoms are killed by Theorem 4.3.
  - This uses neither (E_ψ), nor (HC), nor P1.1/P1.3. **CONFIRMED.**
- **Mid-facet atoms.**
  - From inside: an atom of tie gambles inside D_{T1} over a middle-arc point h needs a face model with P_K(h) < 0. R.1 already excludes this, since φ_K ≥ 0 on [τ_i, τ_j] by concavity.
  - From outside: P1's escape, tie gambles outside cl D_{T1} over a middle arc, needs K_δ with δ·b′ > 0 and P_{K_δ} > 0 there. This is excluded by R.2.
  - So P1 §4.2's "surviving escape" is impossible. Its NUMERICS concern the facet algebra only, and remain correct as such. **CONFIRMED** (agreeing with M0_referee §2).

---

## 4. The dependency chain, especially P4 Theorems 3.1 and 4.3

### 4.1 Theorem 3.1 (the §4 chain for K^♭ when p\* ∉ E)

The chain uses the following facts:
- K^♭ is coherent at every q, u.s.c., and continuous exactly off E;
- P^♭ = P off E;
- lines through p\* are not chords, so each meets E countably (N25 Cor 2.2; with Prop F step 5 or without it, since a non-chord line meets each chord at most once and F is countable).

| §4 step | Where §4 used continuity | Replacement checked |
|---|---|---|
| Lemma chords (a) | continuity in q | {P^♭(·,g) > 0} = H(g) ∩ Δ° *exactly* for good g. It is convex (2.1), a.e. equal to H, and open (l.s.c.), so it contains H and lies in int cl H = H. ✓ |
| Lemma levels | cluster lines | Lemma 2.1 at every level. {Ψ > t} is an open half-plane; {Ψ < t} is a half-plane plus boundary points. ✓ |
| UVN | vertex limit | B^A_q → U ∩ {g_l > 0} pointwise as q → e_l along any sequence, hence in measure and in Hausdorff distance. ✓ |
| PL2, nopin | continuity on co(G ∪ V_l) | Lemmas 2.7, 2.8 (§4.2). ✓ |
| Step 1 | nopin, Ψ(p\*,·) = 0 | p\* lies in the convex set P_{σ₁} ∩ P_{σ₂}, whose interior is non-empty, hence p\* ∈ cl G. ✓ |
| Step 3 | — | Purely pointwise in q. The zero set is convex, by 2.1. ✓ |
| Step 4 | Ψ(q,·) = 0 on [a,b] for q ∈ λ | Only for q ∈ λ∖E. Continuity at such q excludes Ψ < 0, since a neighbourhood would otherwise meet A_τ. An open half-plane through p\* missing a co-countable part of λ has boundary λ. ✓ |
| Step 5 | — | Pointwise. The added "Z_τ = λ_τ ∩ Δ° exactly" follows from strict monotonicity and continuity in τ. ✓ |
| Cluster clause | Lemma chords (b) | Robust: for good g_m → h(τ), q ∈ A_τ gives q ∈ H(g_m), and q ∈ B_τ gives q ∉ H(g_m) for large m. Exact charts for K^♭ make this two-sided. ✓ |
| Nosliding | — | Pointwise. The wedges W₁ and −W₁ give P = 0, the convex zero set gives a ball, and caps(a) gives the contradiction. ✓ |
| Rotation, regularity, blow-up | joint continuity at anchors | Only at the *limit* anchor q_{τ₁}(ξ) ∉ E. ∂⁻Ψ is an infimum of functions each continuous at that point, hence u.s.c. there. The approaching anchors are used only pointwise: they lie on λ_{τ₀} = Z_{τ₀}, and caps(b) applies. For each τ used, a co-countable set of ξ is available. Blow-up, sweep, window and twoslope are pointwise or pure analysis. ✓ |
| Edgebox, boxbridge (c) | — | N25 Prop 9.2 needs only a.e. q. Boxbridge uses the robust cluster vectors. ✓ |
| Prop T1 | p\* = u; transposition | p\*⊙c preserves (γ) and moves E with p\*. c^σ(g) := σc(σg) gives B^σ_q = σB_{σq}, which preserves (γ), fixes U (K′ is σ-symmetric) and fixes D_{T1} at u. ✓ |

**CONFIRMED.** A1 follows: if p\* ∉ E then S is null and T1 = K^♭_{p\*}.

### 4.2 Lemmas 2.7 and 2.8

**Lemma 2.7.**
- *β is relatively open.* By u.s.c., v ∈ K^♭_{q_m} → K ⊆ K^♭_q, so v ∈ K^♭_q.
- *Step 1.*
  - lim sup 1_{B^s_{q_m}} ≤ 1_{B^s_Q ∪ Z_Q}, and Hausdorff convergence gives convergence in measure, so D_{K\*} ⊆ D_{K^♭_Q} ∪ Z_Q mod null.
  - If v ∉ K\*, then m·w > 0 on W∖{v}. The only m ∈ W with m·w = 0 is v, because w is interior to the facet piece and m·𝟙 = 1. So D_{K\*} contains a neighbourhood of w.
  - Its exterior part avoids D_{K^♭_Q}, because h·v < 0 there, and so lies in Z_Q. The ball lemma at Q gives the contradiction.
- *Step 2.* Joint Lipschitz continuity of (K,h) ↦ P_K(h) gives P^♭ < 0 near Q, uniformly in h.
- *Step 3.*
  - Points q with a₊·q > 0 near Q lie in H(h⁺_m) for large m, so v ∉ K^♭_q and q ∈ β. This is in fact stronger than "∈ cl β".
  - Points of β have P^♭(q, w₋) > 0, hence a₋·q ≥ 0.
  - Then (a₊)_c > 0 ≥ λ(a₋)_c gives the contradiction.
- ✓

**Lemma 2.8.**
- P^A(q,h) = P^A(q,w″) + v_k·h > 0 on G for h ∈ 𝒰⁺. With exact charts this gives G ⊆ int cl H(h) = H(h), and int co(G ∪ V_j) ⊆ H(h) for every good h ∈ 𝒰⁺.
- So D_{K^♭_q} ⊇ 𝒰⁺. An open convex set containing a dense subset of an open set contains it.
- K^A ⊆ K^♭ transfers v_k ∉ K.
- ✓

### 4.3 Theorem 4.3

- *Setup.* At t ∈ ℓ° (co-countable in ℓ ∩ Δ°), Z_t = G ∪ G′. For generic δ with δ·b > 0, B^δ_t = B^s_t ∪ G, so P^δ(t,h) = π⁺(h) = 0 on J.
- *Concavity.* By caps(a), φ_t ≤ 0 on ℝ. Here φ_t is concave on the whole facet line.
- *Middle arc.*
  - Points of the middle arc of F_k are positive at j and at o, where the corner r_{kj} has pattern (−_k, −_j, +_o).
  - The chord, with normal b of corner sign, has e_o ∈ H⁺ and e_j ∈ H⁻.
  - UVN for P^δ and convexity (2.1) give segments from V_o to V_j inside {P^δ(·,h(τ_m)) > 0}. Their crossings with ℓ form a non-empty open subset of ℓ ∩ Δ°, which meets ℓ°.
- *Admissibility.* {δ·c > 0} needs δ ∉ D_q at every q, i.e. δ parallel to no chord. Since there are countably many chords, a co-countable set of directions qualifies, and δ·b > 0 is open.
- **CONFIRMED.** NUMERICS (`geometry_check.py` §4): for T1 at 25 values of ε, every corner of every facet satisfies "middle arc positive at j and o". 20 random corner-sign normals through random interior points at each corner all separate e_o from e_j.

### 4.4 Other links

- **N25 Lemma 3.1.**
  - {q·c = 0 = δ·c} is the atom of the line through q in direction δ. It is null for δ ∉ D_q.
  - Rays meet E countably.
  - The limit is coherent.
- **Lemma 3.2.** The boundary of a closed convex cone with interior is null.
- **Thm 3.3(a).** For g ∈ Z_q, some δ ∈ Q has δ·c(g) < 0, because c(g) ∝ 𝟙 is impossible.
- **Thm 4.1(e).** The interval G ∩ (g + ℝ𝟙) is independent of t mod null, so its endpoints agree. Continuity in g then extends this to supp μ|Π.
- **Thm 4.1(f).** It uses density points only.
- **Prop 4.1(i), (ii) and Lemma 4.2.** As in §2.3.
- **All CONFIRMED.**

---

## 5. Task 4: what singles out T1; no conflict with positive results

### 5.1 The two branches use different T1-specific inputs

- **Branch p\* ∉ E** (Theorem 3.1).
  - Everything up to (PC), (NS), crossing rows and the box holds for *any* interior target whose facets carry crossings with a shared positive coordinate.
  - The contradiction is the corner-equation/box algebra: Prop T1 for T1, and the R15 pinching for all-facing triangles in general position.
  - This is the step that fails for covered targets. Gauge mixtures, normalised boxes, the hexagon around u and the 9-gons all have unique Bayes models at every interior weighting (E = ∅), so only this branch is relevant to them. For them the algebra is consistent (R10a Thm M; "Conditional Shunning of Error" Prop bayes(a), Lemma Q(b)). No gauge mixture covers a triangle in general position (R10a Thm R), in agreement.
- **Branch p\* ∈ E** (R.1 + 4.1 + 4.3). R.1 itself is general (§2.2). The T1-specific inputs are those of Lemma signs (all-facing):
  - (i) each facet has **two** crossings in its relative interior, so that concavity yields "≤ 0 on the corner portions";
  - (ii) each corner ray lies in a **two-negative** orthant, so carrying atoms have corner pattern (Lemma 2.4(b));
  - (iii) the middle arc of F_k is positive at j and at o, which the corner-pattern chord separates (Theorem 4.3).

  A counting fact shows these characterise triangles. The boundary cycle of D_K, for K ⊆ Δ°, meets each plane {g_c = 0} exactly twice, so it has 6 crossings in all. "Two relative-interior crossings per facet" therefore forces exactly three facets.

  NUMERICS (`geometry_check.py`, `hexagon_check.py`):
  - all 2000 random all-facing triangles satisfy (i)–(iii);
  - among 591 random interior polygons whose hull has ≥ 4 vertices, every one fails (i), 582 also fail (ii), and none satisfies both;
  - a regular hexagon around u has 1 or 0 relative-interior crossings per facet, and corners in one-negative orthants;
  - a **normalised box has all six crossings at its corner rays**, since its edges lie on lines m_b = ρm_a whose normals have a zero coordinate. There, generalised R.1 says that every face model vanishes at the six corners, and concavity then gives P_K ≥ 0 on every facet, i.e. K ⊆ box. This is the *opposite* inclusion to T1's, and it yields no contradiction.

### 5.2 Exceptional targets that are realised

- **N26.1** (n = 2) exhibits exactly what Theorem R forbids for T1: a target that is a coherent Bayes model at an exceptional weighting, with an intermediate split.
  - In n = 2 the boundary rays of D_K have no zero coordinate (`geometry_check.py` §6: (0.75, −0.25) and (0.375, −0.625)). So R.1 is vacuous and nothing is contradicted.
  - Crossings exist only for n ≥ 3, and the bite comes from where they sit.
- **"Conditional Shunning" systems Σ_T with T ≠ ∅.** These have ties (c_i = 0 when g_i > 0 and i ∈ T), so they are not strictly signed and lie outside the hypothesis of Theorem R(a). Their exceptional priors lie in Δ_T ⊆ ∂Δ, not in Δ°.
- **No n = 3 strictly signed field with (γ)** is known with a target at an interior exceptional weighting. Theorem R(a) contradicts nothing established.

### 5.3 Scope beyond T1

For all-facing triangles in general position:
- (i)–(iii) hold by Lemma signs (general proof in the writeup);
- Lemma 2.5 is general;
- the R15 algebra replaces Prop T1, and it needs no transposition.

I agree with M0_referee's CHECKED scope claim: Theorem R(a) holds for every all-facing triangle in general position, on every U-domain of it. This is CHECKED, not written out.

---

## 6. Repairs (none affects the conclusions)

1. **R.1:** drop "If p\* ∈ E". State it for every zero-coordinate gamble of ∂D_T∖0 and any interior target T. Keep the corner-portion clause for T1 (or for all-facing triangles).
2. **Dependencies (M0_referee §7).** Add the following to (D4)/(D5):
   - P4 Lemma 2.4(a) (in Prop 4.1(i));
   - Lemma 2.5 and Thm Estructure(b) "cuts off the odd vertex", i.e. N25 Thm 4.1(a) (in Thm 4.3);
   - Lemmas 2.1 and 2.2(a), (b) (admissibility of {δ·c > 0}, and UVN for P^δ, in Thm 4.3);
   - N25 Lemma 3.1 (coherence of K_δ, in Theorem R step 4 and in R.1's application);
   - Lemma signs (all-facing structure).

   N25 Cor 2.2 is used in the form "a non-chord line meets E countably". With Prop F step 5 this is immediate. Without it, it still holds: F is countable, and each chord meets the line at most once.
3. **M0_referee, P4 Lemma 2.7 Step 3.** The points with a₊·q > 0 near Q lie in β itself, not merely in cl β. This is harmless.
4. **Theorem R(a) wording.** "Bayes models coherent at a.e. interior weighting" is (γ). Nullity of E then follows by Tonelli and need not be assumed. Integrability is not used by the proof; it is harmless.

---

## 7. What is established, and its status

**Theorem R(a) (additive form). PROVED; new parts read independently twice (M0_referee and this report).**
- *Setting.* ε ∈ (0,1); M_U a U-domain of T1, with K′ = u + s(T1 − u), 0 < s < 1. (By §5.3, CHECKED, every K′ ⊆ relint T1 works.)
- *Statement.* No strictly signed field c on U with B_q coherent for a.e. q ∈ Δ° has D_{T1} = B^s_{p\*} ∪ S, with S ⊆ Z_{p\*}, at any p\* ∈ Δ°.
- *Strength.* This strictly strengthens writeup Theorem main, which assumes (BU) at every q.
- *Reading counts of its inputs:*
  - P4 Part A: now two referees;
  - N25 Thm 2.1/3.3/4.1: N25_referee, M0_referee, and this report for the parts used;
  - Prop F steps 1–4: three readings;
  - writeup §4 chain: refereed twice, and its chord-tolerant audit (P4 Theorem 3.1) has now been read twice.

**Theorem R(b) (ranking form). PROVED at the status of writeup Prop M0 (α), (γ) without (E_ψ).**
- *Statement.* On M_U there is no ranking with strict (G), (IB), (LA), (S), (C) and T1 ∈ C_L in which every world adds up on the relevant comparisons. This holds with or without (E_ψ).
- *Status of the imports.* For general (finitely additive) weights these are N13 Prop B and N19 Prop R3(a), each proved in a referee report and read once. For countably additive weights they rest on N17 Prop 2.1, refereed in N19. I did not re-derive them. A second reading of N13 Prop B (α), (γ) and N19 Prop R3(a) would put (b) at the same standard as (a).

**Consequences (CONFIRMED):**
- Q1 of writeup §8.1 is answered negatively on M_U;
- residuals R-a′ and R-b′ are closed;
- P4's (TP) is empty, and P1's split-facet escape is impossible;
- no 𝓛₂ˢ ranking covers T1 on M_U;
- P4 Theorem A3 is a special case;
- a cover of T1 on M_U must have a world in mode (M1) or (M2), i.e. failing SP^reg: Conjecture N17.B′ in three worlds is the only remaining route on M_U.

**Not established:**
- the same for general decomposable domains (two-sided advice ranges);
- targets other than all-facing triangles;
- n ≥ 4.

---

## 8. Files

`m0ref2_py/`:
- `geometry_check.py` / `.out`:
  - facet structure and Lemma-signs inputs for T1 (6 values of ε) and for 2000 random all-facing triangles;
  - normalised boxes;
  - the R.1 constructions;
  - Theorem 4.3 separation;
  - the R.2 sector hull;
  - n = 2 boundary rays.
- `hexagon_check.py` / `.out`: hexagons around u and random interior polygons.
- `rerun_crossing_balls.out`, `rerun_transpose_box.out`: reruns of M0_referee's scripts, identical to the originals.
