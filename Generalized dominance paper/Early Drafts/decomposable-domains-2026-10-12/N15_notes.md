# N15: the (DD) gap closed on non-adjacent domains — straight levels, caps, and a two-stage blow-up

13 Oct 2026. Task: BRIEF7, proof side. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof
sketched), **CONJECTURE**, **NUMERICS**. Refereed inputs used, with their status:
- N12.1 reduction, Lemma 2.1 (weak chords / clusters), Theorem 3.1 ((PC)+(NS) ⇒ contradiction), Lemma 4.3 (concavity ⇒
  projectivity for two-slope data): all CORRECT in N14.
- R10b Lemma UVN, Lemma M, Cor PL2: CORRECT in R12.
- N14 §3(iv) (non-adjacent domains reduce to the N12.1 setting), N14 Thm C2 (charges): PROVED in N14.

Scripts: `n15py/`. Nothing else in this note is imported.

---

## 0. Outcome

**Verdict.** The gap of N14 §6 is closed. No hypothesis (DD) is needed.
- On the U-domain (the evaluable models are the measurable subsets of U = D_{K′}) **T1 has no realisation**, for every ε ∈ (0,1) (PROVED, N15.8).
- The same holds on every decomposable domain whose pairs meeting U′ are non-adjacent (CHECKED, N15.9(a)).
- In both cases the conclusion extends to every all-facing triangle in general position, in particular every
  ε-contamination of an interior baseline, at every interior p\*.
- The new arguments are unrefereed; §8 lists where a referee should look first.

How the three failure modes die:
- (F2) direction-discontinuity is impossible outright (N15.6(d)).
- (F3) in its zero-set forms is impossible at every facet gamble: pinning, half-pinning, fat zero sets (N15.3). In its
  first-order form, the profile is bi-Lipschitz at almost every facet gamble (N15.6).
- (F1) oscillation is **not** excluded as a phenomenon by the local structure. Slow (log-log type) oscillation of
  P(p\*+tδ,h)/t is compatible with everything in §§2–5. It is made harmless: the argument passes to a blow-up along a
  common subsequence, proves that every blow-up profile is concave, and zooms once more to get exact two-slope data.
  N12 Lemma 4.3 then gives projectivity of the **chord map**. The chord map does not depend on the subsequence.

The proof uses exactly the two structural facts the brief singled out:
- the level shift P(q, h − c𝟙) = P(q,h) − c, which makes every superlevel set an exact half-plane (§2);
- concavity of P(q,·) in h, which turns each sign change along a facet into a nonzero one-sided slope (§3).

The new ingredient that makes the zero-set statements unconditional is R10b Cor PL2, applied at finite distance from
p\* (N15.2).

**Numbered claims.**

**N15.1 (PROVED) Exact straight levels.** Let g ∈ U and let c be an interior point of the interval of levels for which
g − c𝟙 ∈ U is mixed. Then on Ω = int Δ:
- {P(·,g) > c} and {P(·,g) < c} are each Ω ∩ (open half-plane), or ∅, or Ω;
- {P(·,g) = c} is Ω ∩ (closed strip between two lines that do not cross inside Ω).

This repairs N14's "possibly fat level set" remark into an exact description. Consequences:
- profiles of P(·,h) along any line are monotone;
- **parallel-level sandwich** (Lemma 2.3): near a zero chord, P(·,h) is a ridge up to a relative distortion
  |y|/(r₀ ∓ |y|) in the transverse argument, where r₀ = dist(p\*, ∂Δ).

**N15.2 (PROVED from refereed R10b Cor PL2) No partial pinning across a crossing.** Let τ_i be a crossing parameter on
the facet F_k, with σ₁ < τ_i < σ₂. Let G ⊆ Ω be nonempty, open and connected, with P(q,h(τ)) ≥ 0 for all q ∈ G and
τ ∈ [σ₁,σ₂]. Then P(q,h(τ)) > 0 on G × (σ₁,σ₂).
- G may lie anywhere in Ω; it need not contain p\*.
- The hypothesis needs only the two endpoint values (concavity).

**N15.3 (PROVED) Pivot chord theorem.** Let T be all-facing in general position (T1 included). For every facet F_k and
every h ∈ relint F_k:
- {q ∈ Ω : P(q,h) = 0} is exactly λ_h ∩ Ω, for one line λ_h through p\*;
- P(·,h) > 0 on one open side of λ_h and < 0 on the other;
- every cluster chord of h equals λ_h, with the same orientation. So clusters are unique.
- The chord map h ↦ λ_h is continuous and strictly monotone on relint F_k (a homeomorphism onto an open arc of the pencil
  at p\*);
- at the crossings it takes the values line(p\*, e_i).

This excludes (G1) pinning on every arc, not only on crossing arcs (N14 §5.2); (G2) non-unique clusters; jumps; and every
zero-set form of (F3). It also repairs the GAP in N12 Prop 2.6 (monotonicity).

**N15.4 (PROVED) No sliding edges.** At each corner ray r = r_{kj} the one-sided chord limits from F_k and from F_j
coincide, with the same orientation. With N15.7 this is (NS).

**N15.5 (PROVED) Profile–rotation inequalities.** Fix τ₁ ∈ (0,1) and a small ξ > 0. Let θ be the angle of the chord
normal, and L_\*, L^\* its lower and upper left Dini derivatives at τ₁. Let S^±(ξ) be the one-sided h-slopes of
P(q,h(·)) at τ₁, at the anchor q = p\* + ξ(unit vector along λ_{τ₁}). These are finite and nonzero (concavity). Then:

  S⁺(ξ)(r₀−ξ)/(r₀ ξ L^\*) ≤ liminf_{x↓0} D⁺(x)/x ≤ limsup_{x↓0} D⁺(x)/x ≤ S⁻(ξ)(r₀+ξ)/(r₀ ξ L_\*),

where D⁺ is the transverse profile of P(·,h(τ₁)) at p\*. The same holds on the negative side. So:
- the magnitude of P at p\* (an infinitesimal q-quantity) is controlled by the contact geometry at finite distance (an
  h-derivative);
- the controlling quantity is the rotation speed of the chords.

**N15.6 (PROVED) Regularity for free.**
- (a) For every compact J ⊂ relint F_k: |P(p\*+δ, h)| ≤ C_J|δ||h| near p\*. This is Lipschitz control of K_q at p\*
  in the facet directions, the compactness input N14 C1′ asked for.
- (b) θ′ exists and lies in (0, ∞) for a.e. τ.
- (c) At a.e. τ the transverse profiles are bi-Lipschitz at 0.
- (d) If the derivative along ±n_h exists, then the full directional derivative exists for every δ and has the two-slope
  form. So (F2) cannot occur.

**N15.7 (PROVED) Projectivity, i.e. (PC).**
- (a) Along a common subsequence t_m ↓ 0, P(p\*+t_mδ, h(τ))/t_m converges for all (δ, τ) to G(δ,τ). The limit G is
  concave in τ.
- (b) For a.e. τ, G(·,τ) = φ_τ(n_τ·δ) with φ_τ **continuous and concave on ℝ**. The proof is a sweep along rotating
  chords, then a window rescaling.
- (c) The second zoom G₂ = lim_{ε↓0} G(εδ,τ)/ε is exact two-slope data α_τ[n_τ·δ]₊ − β_τ[n_τ·δ]₋ for every τ, with
  α, β > 0, concave in τ.
- (d) N12 Lemma 4.3 applies to G₂. So τ ↦ α_τ n_τ is affine, and the chord map is projective: n_h ∝₊ Γ_k h with Γ_k
  linear and nonsingular.

**N15.8 (PROVED) Main theorem.** Assume:
- the U-domain;
- (R1): every interior Bayes model is a.e. unique and coherent;
- (R2): T is the Bayes model at some p\* ∈ int Δ;
- (LF) at T.

Then T is not all-facing in general position. In particular **no realisation of T1 exists**, for any ε, without (DD),
(DF), (ND), (NA_w) or any regularity of q ↦ K_q beyond its automatic Hausdorff continuity.

**N15.9 Scope.**
- (a) (CHECKED) The theorem holds on every decomposable domain with (LF) on which a.e. pair meeting U′ is non-adjacent, e.g.
  under (FD). Route: N14 §3(iv), plus Cor PL2's no-d-face hypothesis, which non-adjacency supplies.
- (b) (PROVED, given N14 Thm C2) The penalties may be bounded charges vanishing on null sets, provided interior Bayes
  minimisers exist. Existence remains a part-(A) question.
- (c) Adjacent domains: unchanged. The box bridge still needs (NA_w), i.e. N14's (E4).
- (d) n > 3 and non-all-facing triangles: not addressed. N15.3 needs a crossing and a shared positive coordinate on each
  facet; Theorem 3.1 needs all-facing.

**N15.10 (NUMERICS)** On the gauge-mixture realisation of N14 §2.3: N15.3, N15.4 and the inequalities of N15.5 hold,
with the bounds bracketing the true slope (`n15py/gauge_sanity.py`). This is a sanity check of orientations only; that
family is (DF)-regular.

**Status of (F1)–(F3).**

| Failure mode | Status after N15 |
|---|---|
| (G1) pinning, (G2) non-unique clusters, chord jumps, fat/half-zero sets | impossible (N15.3) |
| sliding edges | impossible (N15.4) |
| (F2) direction-discontinuity | impossible (N15.6(d)) |
| (F3) first-order flat or steep profile | impossible at a.e. facet gamble (N15.6(c)); harmless elsewhere |
| (F1) oscillation of P(p\*+tδ,h)/t | not excluded locally; made irrelevant by the blow-up (N15.7) |
| non-projective chord map | impossible (N15.7) |

**Risk points for the referee (§8).**
- The use of Cor PL2 at sets G away from p\*.
- The parallel-level sandwich.
- The semicontinuity directions in N15.5.
- The sweep and window steps of N15.7(b).

---

## 1. Setting and standing facts

**Setting** (N12 §1 with the N14 repairs).
- U = D_{K′} with K′ = u + s(T − u), 0 < s < 1.
- q ↦ K_q (q ∈ Ω := int Δ) is Hausdorff-continuous, with K_q ⊇ K′ and K_{p\*} = T.
- P(q,g) = min_{m∈K_q} m·g is jointly continuous. It is concave and positively homogeneous in g, and
  P(q, g + c𝟙) = P(q,g) + c.
- For a.e. g ∈ U, {P(·,g) > 0} = H(g) ∩ Ω a.e., with H(g) an open half-plane respecting vertex signs (N12.1, (★)).
- On non-adjacent domains replace K_q by K̂_q = conv(K_q ∪ K′) (N14 §3(iv)).

**Notation.**
- r₀ := dist(p\*, ∂Δ) > 0 in the Euclidean metric of the plane aff Δ. Then B(p\*, r₀) ⊆ Ω.
- Unit normals live in 𝟙^⊥.
- Facets F_k = cone{r, r′} with corner rays r, r′; h(τ) := (1−τ)r + τr′, so relint F_k ↔ τ ∈ (0,1).
- Ψ(q,τ) := P(q, h(τ)). For each q, g_q(τ) := Ψ(q,τ) is **concave on all of ℝ** (P(q,·) is concave and h is affine).

**Facet sign structure for all-facing T** (R15 §6, R18 §6). On F_k:
- h_k < 0;
- the other two coordinates i, j each cross zero once in relint F_k, at τ_i < τ_j (after relabelling);
- (h_i, h_j) has signs (−,+) on [0,τ_i), (+,+) on (τ_i,τ_j), (+,−) on (τ_j,1].

So h_j > 0 on [0,τ_j) and h_i > 0 on (τ_i,1]. (Proof for T1: at a crossing of one coordinate the other must be positive,
since h·v_k = 0 with v_k > 0 and h_k < 0.)

**Imported tools.**
- (L2.1) N12 Lemma 2.1(b). For every mixed g ∈ U there is at least one cluster chord ℓ. With its limiting orientation,
  P(·,g) ≥ 0 on the closed positive side and ≤ 0 on the closed negative side (∩Ω). The line is genuine: the normal is a
  unit vector not ∝ 𝟙.
- (UVN) R10b. Let x ∈ N be mixed.
  - If x_l > 0, there are a ball B₁ ∋ x and a relative neighbourhood V_l of e_l with P(q,h) > 0 for all q ∈ V_l ∩ Ω and
    h ∈ B₁.
  - If x_l < 0, the same holds with P < 0.
- (PL2) R10b Cor PL2; used in §4.1.
- (L4.3) N12 Lemma 4.3; used in §6.
- (T3.1) N12 Theorem 3.1; used in §7.

---

## 2. Straight levels (N15.1)

**Lemma 2.1 (exact half-planes; PROVED).**
- *Statement.* Let g ∈ ℝ³, and let I_g := {c : g − c𝟙 ∈ U and mixed}, an open interval. Put f := P(·,g) on Ω. For every
  c ∈ I_g:
  - {f > c} is Ω ∩ H⁺_c for an open half-plane H⁺_c, or is ∅ or Ω;
  - {f < c} is Ω ∩ H⁻_c similarly;
  - {f = c} is Ω ∩ (a closed strip bounded by ∂H⁺_c and ∂H⁻_c). When both half-planes are proper, these two lines do not
    cross inside Ω.
- *Proof.*
  1. For c′ ∈ I_g, (L2.1) applied to g − c′𝟙 gives a line ℓ_{c′} with closed sides Π^±_{c′}. On Π⁺_{c′} ∩ Ω, f ≥ c′,
     and on Π⁻_{c′} ∩ Ω, f ≤ c′.
  2. {f > c} is convex. Let q₁, q₂ ∈ {f > c} and pick c′ ∈ I_g with c < c′ < min f(q_i). Then q_i ∉ Π⁻_{c′}, so
     q_i ∈ int Π⁺_{c′}. The segment [q₁,q₂] lies in int Π⁺_{c′} ∩ Ω ⊆ {f ≥ c′} ⊆ {f > c}.
  3. {f ≤ c} is convex. It equals ∩_{c′∈(c,c+η)} (Π⁻_{c′} ∩ Ω) for small η > 0:
     - "⊆": f(q) < c′ implies q ∉ Π⁺_{c′};
     - "⊇": q in every Π⁻_{c′} gives f(q) ≤ c′ for all c′ > c.
  4. {f > c} is open and convex, and its complement in the convex set Ω is convex. If both are nonempty, separate them by a
     line L. Then {f > c} ⊆ int L⁺, and Ω ∩ int L⁺ cannot meet {f ≤ c} ⊆ L⁻. So {f > c} = Ω ∩ int L⁺.
  5. The case {f < c} is symmetric.
  6. If the two boundary lines crossed at x ∈ Ω, the two disjoint open half-planes would both contain a wedge with apex
     x, and that wedge meets Ω. ∎

**Lemma 2.2 (monotone profiles; PROVED).**
- *Statement.* Suppose f(p\*) = 0 and A := {f > 0} = Ω ∩ {n·(q−p\*) > 0} for a unit normal n (zero chord through p\*).
  Then s ↦ D⁺(s) := f(p\* + s n) is nondecreasing on [0, r₀) wherever its values lie in I_g. Likewise for D⁻(s) :=
  −f(p\* − sn).
- *Proof.* For c > 0 in I_g, {f > c} is a half-plane ∩ Ω inside A that does not contain p\*. Its trace on the ray
  {p\* + sn} is therefore a terminal sub-ray. ∎

**Lemma 2.3 (parallel-level sandwich; PROVED).**
- *Statement.* In the setting of Lemma 2.2, suppose the zero set of f is exactly λ ∩ Ω with λ = p\* + ℝu (u ⊥ n). Let
  q = p\* + yu + xn with |y| ≤ r₀/2 and x > 0, with f(q) ∈ I_g. Then

    D⁺( x r₀/(r₀+|y|) ) ≤ f(q) ≤ D⁺( x r₀/(r₀−|y|) ).

  The mirror statement holds for x < 0 with D⁻.
- *Proof.* Put c := f(q) > 0.
  - *Lower bound.* Let s₂ := x r₀/(r₀+|y|) and suppose D⁺(s₂) > c.
    1. Then p\* + s₂n lies in H := {f > c}, an open half-plane ∩ Ω inside A.
    2. Its boundary L does not meet λ ∩ Ω. If it met λ at z ∈ Ω, then H ⊆ A near z would force ∂H = λ near z. Then f > c
       on A near z, which contradicts f(z) = 0 and continuity.
    3. So L meets the line λ, if at all, at p\* + y₀u with |y₀| ≥ r₀ (B(p\*,r₀) ⊆ Ω).
    4. L crosses the normal ray at some height s_c < s₂. Over |y′| < r₀ it is the graph s = s_c(1 − y′/y₀), and H is the
       side above it.
    5. At y′ = y its height is < s₂(1 + |y|/r₀) = x. So q ∈ H, which contradicts f(q) = c.
  - *Upper bound.* Suppose D⁺(s₁′) < c for some s₁′ > x r₀/(r₀−|y|).
    1. H′ := {f < c} is an open half-plane ∩ Ω containing p\* + s₁′n and the whole chord λ ∩ Ω.
    2. Its boundary is a line above λ meeting it only at |y₀| ≥ r₀.
    3. Its height at y′ is ≥ s′(1 − |y′|/r₀) with s′ > s₁′. At y′ = y this is > x, so q ∈ H′. Contradiction.
    4. Hence D⁺ ≥ c on (x r₀/(r₀−|y|), r₀), and continuity gives the bound. ∎

**Uniformity.** For the facet family, {h(τ) − c𝟙 : τ ∈ [0,1], |c| ≤ c₀} ⊆ U consists of mixed gambles for some c₀ > 0
(compactness). All levels used below are smaller than c₀, by continuity of Ψ near (p\*, [0,1]).

---

## 3. Concavity in h: caps (pure convex analysis)

**Lemma 3.1 (cap lemma; PROVED).** Let γ : ℝ → ℝ be concave.
- (a) {γ > 0} is an open interval and {γ ≥ 0} a closed interval.
- (b) If {γ > 0} ≠ ∅, then {γ = 0} = ∂{γ > 0} (at most two points), and γ < 0 off cl{γ > 0}. In particular, if γ
  vanishes on a nondegenerate interval, then γ ≤ 0 everywhere.
- (c) Suppose γ(τ₀) = 0 and γ > 0 on (τ₀, τ₀+η). Then:
  - γ(τ)/(τ−τ₀) is nonincreasing on ℝ∖{τ₀};
  - γ′₊(τ₀) ≥ γ(τ₀+η)/η > 0 and γ′₋(τ₀) ≥ γ′₊(τ₀), both finite;
  - for τ₀ < τ₁ < τ₂: γ(τ₂)/(τ₂−τ₀) ≤ γ(τ₁)/(τ₁−τ₀) ≤ γ′₊(τ₀).
- (d) The mirror statements hold when γ > 0 on (τ₀−η, τ₀).
- (e) (Semicontinuity.) For a jointly continuous family Γ(q,τ), concave in τ:
  - (q,τ) ↦ ∂⁻_τΓ = inf_{s>0}(Γ(q,τ) − Γ(q,τ−s))/s is upper semicontinuous;
  - (q,τ) ↦ ∂⁺_τΓ = sup_{s>0}(Γ(q,τ+s) − Γ(q,τ))/s is lower semicontinuous.

*Proof.* Standard. For (b): if γ(a) = 0 with a interior to {γ ≥ 0} and γ(d) > 0, concavity on [b, d] (b on the other
side of a, γ(b) ≥ 0) gives γ(a) > 0. ∎

---

## 4. Zero chords

### 4.1 No partial pinning across a crossing (N15.2)

**Lemma 4.1 (PROVED, from refereed R10b Cor PL2).** Let τ_i ∈ (σ₁,σ₂) ⊆ [0,1] be a crossing of F_k, so w = h(τ_i) has
w_c = 0 for a world c. Let G ⊆ Ω be nonempty, open and connected, with Ψ(·,σ₁) ≥ 0 and Ψ(·,σ₂) ≥ 0 on G. Then
Ψ > 0 on G × (σ₁,σ₂).

*Proof.*
1. *Concavity.* By concavity of g_q, Ψ ≥ 0 on G × [σ₁,σ₂].
2. *Choice of ball.* Choose the R10b ball U_w around w (§5 of R10b: inside N, inside the UVN balls at w for a world j
   with w_j > 0 and at points w_± with (w_±)_c ≷ 0) so small that the concentric enlargement Ũ has F_k ∩ cl Ũ ⊆
   h([σ₁,σ₂])·ℝ₊.
3. *G ⊆ Γ_{v_k}.* By homogeneity, Ψ ≥ 0 on [σ₁,σ₂] gives m·w″ ≥ 0 for all m ∈ K_q and w″ ∈ F_k ∩ cl Ũ, i.e.
   K_q ⊆ W_{v_k}(Ũ). By R10b §1 this gives q ∈ Γ_{v_k}.
4. *Dichotomy.* On the U-domain the advice ranges near ∂T are {+,0}, so no d-faces exist (on non-adjacent
   domains, by hypothesis). Cor PL2 gives G ⊆ α_{v_k} or G ⊆ β_{v_k}.
5. *α is excluded.* The second alternative of Cor PL2 ("in particular") excludes G ⊆ α_{v_k} for open G:
   - UVN(a) at w for j gives V_j ⊆ Γ ∩ β;
   - chart convexity gives int conv(G ∪ V_j) ⊆ Γ;
   - that set is connected and meets both α and β, contradicting the dichotomy.
6. *Positivity.* So G ⊆ β_{v_k}, i.e. v_k ∉ K_q for q ∈ G.
   - K_q lies in the wedge W := {m : m·h(σ₁) ≥ 0, m·h(σ₂) ≥ 0}, with apex v_k. The two linear parts are independent.
   - For τ ∈ (σ₁,σ₂), h(τ) is a strictly positive combination of h(σ₁) and h(σ₂). So m·h(τ) > 0 on W∖{v_k}.
   - Compactness of K_q gives Ψ(q,τ) > 0. ∎

*Remark.* G need not contain p\*. Only the two endpoint values enter.

### 4.2 The pivot chord theorem (N15.3)

**Notation.** For τ ∈ [0,1]: A_τ := {Ψ(·,τ) > 0}, B_τ := {Ψ(·,τ) < 0}, Z_τ := {Ψ(·,τ) = 0},
P_τ := Ω∖B_τ = {Ψ ≥ 0}, N_τ := Ω∖A_τ = {Ψ ≤ 0}.

**Step 0 (half-planes; PROVED).**
- Ψ(p\*,τ) = P_T(h(τ)) = 0, so p\* ∈ Z_τ.
- UVN at the mixed gamble h(τ): A_τ ⊇ V_l ∩ Ω for every l with h(τ)_l > 0, and B_τ ⊇ V_k ∩ Ω (h_k < 0).
- By Lemma 2.1, A_τ and B_τ are nonempty proper open half-planes ∩ Ω. Write λ^±_τ for their boundary lines, so that
  Z_τ is the closed strip between λ⁺_τ and λ⁻_τ.

**Step 1 (λ⁺_τ passes through p\*, for every τ ∈ (0,1); PROVED).**
1. *Choice of σ₁, σ₂.* Choose them according to the position of τ:
   - if τ < τ_j: take σ₁ ∈ (0, min(τ,τ_i)) and σ₂ ∈ (max(τ,τ_i), τ_j);
   - if τ ≥ τ_j: take σ₁ ∈ (τ_i, min(τ,τ_j)) and σ₂ ∈ (max(τ,τ_j), 1).

   In both cases σ₁ < τ < σ₂, there is a crossing in (σ₁,σ₂), and h(σ₁), h(σ₂) share a positive coordinate l (j in the
   first case, i in the second).
2. *G is nonempty.* So A_{σ₁} ∩ A_{σ₂} ⊇ V_l(σ₁) ∩ V_l(σ₂) ∩ Ω ≠ ∅.
3. *Positivity on G.* Let G := int(P_{σ₁} ∩ P_{σ₂}). This is open, convex and nonempty, with p\* ∈ cl G (a closed convex
   set with nonempty interior is the closure of its interior). Lemma 4.1 gives G ⊆ A_τ.
4. *Conclusion.* Hence p\* ∈ cl A_τ ∖ A_τ = λ⁺_τ ∩ Ω. ∎

Let n_τ be the unit normal of λ⁺_τ pointing into A_τ, so A_τ = Ω ∩ {n_τ·(q−p\*) > 0}.
- For τ ∈ (0,τ_j), n_τ·(e_j − p\*) > 0. The value 0 is excluded, because a line through p\* and e_j would cut
  V_j ∩ Ω ⊆ A_τ.
- For τ ∈ (τ_i,1), n_τ·(e_i − p\*) > 0.

**Step 2 (monotone; PROVED).**
1. *Betweenness.* Let σ < τ < σ′ with A_σ ∩ A_{σ′} ≠ ∅. Concavity gives A_σ ∩ A_{σ′} ⊆ A_τ.
   - Near p\* this is the inclusion of the open wedge {n_σ·δ > 0, n_{σ′}·δ > 0} (nonempty, so n_σ ≠ −n_{σ′}) in
     {n_τ·δ > 0}.
   - By 2-dimensional Farkas, n_τ ∈ cone(n_σ, n_{σ′}).
2. *Monotone angle.* On (0,τ_j) all A_τ contain points near e_j, so they pairwise intersect, and the n_τ lie in one open
   half-circle. A betweenness-preserving map into an open half-circle is a monotone angle function. The same holds on
   (τ_i,1), and the two intervals overlap.
3. Hence there is an angle θ(τ) of n_τ, monotone on (0,1). ∎

**Step 3 (continuous; PROVED).**
1. *Setup.* Suppose the one-sided limits n(τ₀±) differ at some τ₀ ∈ (0,1). By Step 2, n_{τ₀} lies between them.
2. *The jump wedge.* Let W := {δ : n(τ₀+)·δ > 0 > n(τ₀−)·δ}, a nonempty open wedge. For small δ ∈ W:
   - p\* + δ ∈ A_τ for τ ↓ τ₀;
   - p\* + δ ∈ N_τ for τ ↑ τ₀;
   - so Ψ(p\* + δ, τ₀) = 0 by continuity in τ.
   - The same holds on −W.
3. *Contradiction.* Z_{τ₀} is convex, so it contains conv((p\*+W) ∪ (p\*−W)) near p\*, which is a neighbourhood of p\*.
   Then A_{τ₀} misses a neighbourhood of p\*, contradicting Step 1. ∎

**Step 4 (strictly monotone; values at crossings; PROVED).**
1. *No constancy.* Suppose n_τ is constant on [a,b] ⊆ (0,1), a < b, with boundary line λ.
   - Every q ∈ λ ∩ Ω lies in cl A_τ ∖ A_τ ⊆ P_τ ∩ N_τ, so g_q = 0 on [a,b].
   - Lemma 3.1(b) gives g_q ≤ 0 everywhere, so λ ∩ Ω ⊆ N_τ for every τ ∈ (0,1).
   - A closed half-plane whose boundary contains p\* contains the line λ through p\* only if λ is that boundary. So λ⁺_τ
     = λ for all τ.
2. *The crossing contradicts this.*
   - For τ on the side of τ_i where h_i > 0: V_i ∩ Ω ⊆ A_τ, so n_τ·(e_i−p\*) > 0.
   - For τ on the other side: V_i ∩ Ω ⊆ B_τ, which is disjoint from λ⁺_τ ∪ A_τ (since λ⁺_τ ∩ Ω ⊆ P_τ). So
     n_τ·(e_i−p\*) < 0.
   - So n is not constant. By continuity, n_{τ_i}·(e_i − p\*) = 0, i.e. λ⁺_{τ_i} = line(p\*, e_i). ∎

**Step 5 (thin zero sets; PROVED).**
1. *Setup.* Suppose λ⁻_{τ₀} ≠ λ⁺_{τ₀}. They cannot both pass through p\* ∈ Ω (they would cross there). So λ⁻_{τ₀} stays
   at positive distance from p\*, and for small ρ the open half-disc D⁻ := B(p\*,ρ) ∩ {n_{τ₀}·(q−p\*) < 0} lies in
   int Z_{τ₀}.
2. *A test point.* Pick τ₁ ≠ τ₀ near τ₀ and q ∈ A_{τ₁} ∩ D⁻. Such q exist: two distinct half-planes through p\* differ
   on a wedge at p\*.
3. *Contradiction.*
   - g_q(τ₁) > 0 and g_q(τ₀) = 0. By Lemma 3.1(b), τ₀ ∈ ∂J⁺(q), where J⁺(q) := {g_q > 0}.
   - So q ∈ A_τ for τ → τ₀ from one side. Continuity of n gives n_{τ₀}·(q−p\*) ≥ 0, contradicting q ∈ D⁻. ∎

**Theorem 4.2 (pivot chord theorem; PROVED).** For every τ ∈ (0,1), Z_τ = λ_τ ∩ Ω with λ_τ := λ⁺_τ = λ⁻_τ ∋ p\*.
Moreover:
- A_τ and B_τ are the two open sides;
- τ ↦ λ_τ is continuous and strictly monotone;
- λ_{τ_i} = line(p\*, e_i) and λ_{τ_j} = line(p\*, e_j);
- every cluster chord of h(τ) is λ_τ with the same orientation.

*Proof of the last clause.* By (L2.1), a cluster's closed positive side has Ψ ≥ 0, hence misses B_τ, hence lies in
cl A_τ. So the cluster's boundary is λ_τ. ∎

### 4.3 No sliding edges (N15.4)

Let r be the common corner of F_k and F_j. Parametrise each facet so that the corner is at τ = 0. By Steps 2–4 the
limits n^k(0+) and n^j(0+) exist. Joint continuity then gives P(·,r) ≥ 0 on {n^k(0+)·(q−p\*) ≥ 0} and ≤ 0 on the
complement, and the same for j.

**Theorem 4.3 (PROVED).** n^k(0+) = n^j(0+).

*Proof.*
1. *The sliding-edge picture.* If not, then on the nonempty open set O := {n^k·δ > 0 > n^j·δ} ∪ {n^j·δ > 0 > n^k·δ}
   (near p\*), P(·,r) is both ≥ 0 and ≤ 0. The zero set of P(·,r) is convex (Lemma 2.1; r is mixed and lies in U). So
   P(·,r) ≡ 0 on a neighbourhood B of p\*. This is exactly the sliding edge of R15 (E2).
2. *A test point.* Strict monotonicity on F_k gives n^k_τ ≠ n^k(0+) for τ ∈ (0,1). So there is q ∈ B with
   n^k(0+)·(q−p\*) < 0 and q ∈ A^k_τ for some τ ∈ (0,1).
3. *Contradiction.*
   - By continuity at 0+, q ∉ A^k_σ for σ ∈ (0,ε).
   - J⁺(q) is an interval that contains τ and misses (0,ε). Hence 0 ∉ cl J⁺(q).
   - Lemma 3.1(b) then gives g^k_q(0) = P(q,r) < 0. Contradiction. ∎

The orientations agree, since the normals are oriented by positivity on both facets.

---

## 5. Magnitudes from rotation (N15.5, N15.6)

**Normalisation.** Fix a facet. Reparametrising τ ↦ 1−τ if necessary (affine, so it preserves concavity), let
θ : (0,1) → ℝ be a continuous strictly increasing angle of n_τ.
- n_τ = (cos θ_τ, sin θ_τ) and u_τ := (−sin θ_τ, cos θ_τ) in an orthonormal frame of 𝟙^⊥.
- D^±_τ are the transverse profiles of Ψ(·,τ) at p\* (Lemma 2.2).
- Left Dini derivatives: L_\*(τ₁) := liminf_{τ↑τ₁}(θ_{τ₁}−θ_τ)/(τ₁−τ) and L^\*(τ₁) := limsup of the same quotient.

**Anchors.** For τ₀ ∈ (0,1) and 0 < ξ < r₀/2, put q_{τ₀}(ξ) := p\* + ξu_{τ₀} ∈ λ_{τ₀}.
- Since n_τ·u_{τ₀} = sin(θ_τ − θ_{τ₀}), q_{τ₀}(ξ) lies in A_τ for τ > τ₀ (near) and in B_τ for τ < τ₀ ("right cap").
- Likewise q′_{τ₀}(ξ) := p\* − ξu_{τ₀} has a left cap.

**Lemma 5.1 (profile–rotation inequalities; PROVED).** Let τ₁ ∈ (0,1) and 0 < ξ < r₀/2. Put
S⁺ := ∂⁺_τΨ(q_{τ₁}(ξ),τ₁) and S⁻ := ∂⁻_τΨ(q_{τ₁}(ξ),τ₁). Then 0 < S⁺ ≤ S⁻ < ∞, and

  (S⁺/L^\*)·(r₀−ξ)/(r₀ξ) ≤ liminf_{x↓0} D⁺_{τ₁}(x)/x ≤ limsup_{x↓0} D⁺_{τ₁}(x)/x ≤ (S⁻/L_\*)·(r₀+ξ)/(r₀ξ),

with 1/0 = ∞ and 1/∞ = 0. The same holds for D⁻_{τ₁}, with |∂⁻_τΨ(q′,τ₁)| on the left and |∂⁺_τΨ(q′,τ₁)| on the right,
where q′ := q′_{τ₁}(ξ).

*Proof (D⁺).*
1. *Anchor coordinates.* Let τ₀ < τ₁ near τ₁, Δ := θ_{τ₁} − θ_{τ₀} > 0 and q := q_{τ₀}(ξ). Relative to λ_{τ₁}, q has
   transverse coordinate ξ sinΔ > 0 and tangential coordinate ξcosΔ ∈ (0,ξ].
2. *Sandwich.* Lemma 2.3 and monotonicity of D⁺ give

     D⁺(ξ sinΔ·r₀/(r₀+ξ)) ≤ Ψ(q,τ₁) ≤ D⁺(ξ sinΔ·r₀/(r₀−ξ)).

3. *Cap.* Lemma 3.1(c) applies to g_q (right cap at τ₀). For τ₂ > τ₁:

     (τ₁−τ₀)Ψ(q,τ₂)/(τ₂−τ₀) ≤ Ψ(q,τ₁) ≤ (τ₁−τ₀)∂⁺_τΨ(q,τ₀).

4. *Small x covers all small τ₀.* As τ₀ ↑ τ₁, Δ ↓ 0 continuously and strictly. So every small x has the form
   ξ sinΔ·r₀/(r₀±ξ) for some τ₀ → τ₁. Also (τ₁−τ₀)/sinΔ has limsup 1/L_\* and liminf 1/L^\*.
5. *Upper bound.* ∂⁺_τΨ(q_{τ₀}(ξ),τ₀) ≤ ∂⁻_τΨ(q_{τ₀}(ξ),τ₀), and the latter is usc (Lemma 3.1(e)), with
   q_{τ₀}(ξ) → q_{τ₁}(ξ). So limsup_{τ₀↑τ₁} ∂⁺_τΨ(q_{τ₀},τ₀) ≤ S⁻.
6. *Lower bound.* Ψ(q_{τ₀},τ₂) → Ψ(q_{τ₁},τ₂). Then take sup over τ₂ ↓ τ₁ of Ψ(q_{τ₁},τ₂)/(τ₂−τ₁), which is S⁺.
7. *Finiteness and positivity.* S⁺ > 0 and S⁻ < ∞ by Lemma 3.1(c).

*Proof (D⁻).* Use q′_{τ₀}(ξ) (transverse coordinate −ξ sinΔ, left cap at τ₀). Lemma 3.1(c),(d) give

  (τ₁−τ₀)|∂⁺_τΨ(q′,τ₀)| ≤ −Ψ(q′,τ₁) ≤ (τ₁−τ₀)|Ψ(q′,τ₂)|/(τ₂−τ₀).

The semicontinuity now runs the other way: |∂⁺| ≥ |∂⁻|, and −∂⁻ is lsc. That gives the stated left constant; the inf over
τ₂ ↓ τ₁ gives the right one. Positivity: g_{q′} > 0 to the left of τ₁, so ∂⁻ < 0. ∎

**Lemma 5.2 (rising sun; PROVED).** Let θ be continuous and strictly increasing on [a,b]. Then there is τ ∈ (a,b] with
L_\*(τ) > 0.

*Proof.*
1. Fix 0 < ε′ < (θ(b)−θ(a))/(b−a) and suppose L_\* < ε′ on (a,b]. Put f := θ − ε′·id, so f(b) > f(a).
2. Every τ ∈ (a,b] has arbitrarily small s > 0 with f(τ−s) > f(τ). So a maximiser of f on [a,b] cannot lie in (a,b].
3. Hence f(a) > f(b). Contradiction. ∎

**Proposition 5.3 (regularity for free; PROVED).**
- (a) (Uniform Lipschitz.) For every compact J ⊂ (0,1) there are C, t₀ with |Ψ(p\*+δ,τ)| ≤ C|δ| for τ ∈ J and
  |δ| ≤ t₀.
- (b) θ′(τ) exists and lies in (0,∞) for a.e. τ ∈ (0,1). Write E′ for this full-measure set.
- (c) For τ ∈ E′, c_τ x ≤ D^±_τ(x) ≤ C x for small x, with c_τ > 0.
- (d) If lim_{x↓0} D^±_τ(x)/x exist (for both signs), then D(δ,τ) := lim_{t↓0} Ψ(p\*+tδ,τ)/t exists for every δ and
  equals α[n_τ·δ]₊ − β[n_τ·δ]₋. So direction-discontinuity (F2) cannot occur.

*Proof.*
- (a) Lemma 5.2 gives points a < b < min J and c > max J (in (0,1)) with L_\* > 0.
  - At those points, Lemma 5.1 gives D^±(x) ≤ C′x for small x.
  - Lemma 2.3 then gives |Ψ(p\*+δ,σ)| ≤ D^±_σ(2|δ|) ≤ 2C′|δ| for σ ∈ {a,b,c}.
  - For τ ∈ J, concavity of g_q gives:
    - g(τ) ≤ g(b) + (τ−b)(g(b)−g(a))/(b−a) (extrapolation from the left);
    - g(τ) ≥ min(g(b),g(c)).
- (b) By Lebesgue's theorem θ′ exists and is finite a.e. If θ′(τ) = 0 then L^\*(τ) = 0, and Lemma 5.1 gives
  D⁺_τ(x)/x → ∞, contradicting (a).
- (c) Lemma 5.1 with L^\* = θ′ ∈ (0,∞), together with (a).
- (d) Lemma 2.3 at scale t:
  - Ψ(p\*+t(yu+xn),τ)/t lies between D⁺_τ(tx r₀/(r₀±t|y|))/t;
  - both bounds tend to αx when D⁺_τ(s)/s → α.
  - The negative side is the same. ∎

**Remark (what is and is not excluded locally).**
- At a.e. τ: no first-order flatness, no steepness.
- The quotient D⁺_τ(x)/x may still oscillate inside [c_τ, C]. For example x(2 + sin log log(1/x)) is not excluded by
  anything in §§2–5.
- §6 shows such oscillation is irrelevant.

---

## 6. Projectivity via a two-stage blow-up (N15.7)

Fix compact intervals J₁ ⋐ J ⋐ J′ ⋐ (0,1). By Prop 5.3(a) on J′, Ψ_t(δ,τ) := Ψ(p\*+tδ,τ)/t satisfies
|Ψ_t| ≤ C|δ| for τ ∈ J′ and |δ| ≤ t₀/t.
- Ψ_t(δ,·) is concave on J′, hence Lipschitz on J with constant L|δ|, L := 2C/dist(J,∂J′), uniformly in t.
- (M) (Monotonicity, Lemma 2.3.) For fixed τ and fixed δ, δ′ with n_τ·δ < n_τ·δ′: Ψ_t(δ,τ) ≤ Ψ_t(δ′,τ) for all small t.
  (Mixed signs use Thm 4.2's strict signs.)

**Step 1 (first blow-up; PROVED).**
1. *Diagonal.* Let Q ⊂ ℝ² be countable and dense. Arzelà–Ascoli in τ for each δ ∈ Q, plus a diagonal argument, give
   t_m ↓ 0 with Ψ_{t_m}(δ,·) → G(δ,·) uniformly on J for all δ ∈ Q.
2. *Properties on Q.* G is concave and L|δ|-Lipschitz in τ. By (M), for each τ ∈ J and δ,δ′ ∈ Q:
   n_τ·δ < n_τ·δ′ ⇒ G(δ,τ) ≤ G(δ′,τ).

**Step 2 (continuity of the profile by sweeping; PROVED).** Fix τ₀ ∈ E′ ∩ J and write ϑ := θ′(τ₀) ∈ (0,∞),
n₀ := n_{τ₀}, u₀ := u_{τ₀}. Define

  φ⁻(x) := sup{G(δ,τ₀) : δ ∈ Q, n₀·δ < x},  φ⁺(x) := inf{G(δ,τ₀) : δ ∈ Q, n₀·δ > x}.

Claim: φ⁻ = φ⁺.

1. *Setup.* Suppose φ⁺(x₀) − φ⁻(x₀) = 𝒥 > 0. Fix ε > 0.
   - Pick δ′, δ″ ∈ Q with |u₀·δ′|, |u₀·δ″| ≤ 1, n₀·δ′ ∈ (x₀, x₀+ε) and n₀·δ″ ∈ (x₀−ε, x₀).
   - For large Y pick δ ∈ Q with |δ − (Yu₀ + x₀n₀)| < ε/10.
   - Use n_σ = cosΔ·n₀ + sinΔ·u₀, Δ = θ_σ − θ_{τ₀}.
2. *Sweep forward.* Choose σ₊ > τ₀ with sinΔ = 3ε/Y.
   - For large Y: n_{σ₊}·δ ≥ x₀ + 2.5ε > x₀ + 1.5ε ≥ n_{σ₊}·δ′.
   - So G(δ,σ₊) ≥ G(δ′,σ₊) ≥ φ⁺(x₀) − L₁|σ₊−τ₀|, where L₁ := L(|x₀|+2).
3. *Sweep backward.* Symmetrically, choose σ₋ < τ₀ with sin(−Δ) = 3ε/Y. Then G(δ,σ₋) ≤ φ⁻(x₀) + L₁|σ₋−τ₀|.
4. *Lipschitz bound.* Since θ′(τ₀) = ϑ, |σ_± − τ₀| = (3ε/(Yϑ))(1+o(1)) as Y → ∞. So

     𝒥 − o(1) ≤ G(δ,σ₊) − G(δ,σ₋) ≤ L|δ||σ₊−σ₋| → 12Cε/(ϑ·dist(J,∂J′)).

5. Letting ε → 0 gives 𝒥 = 0. ∎

**Consequences.**
- φ_{τ₀} := φ⁻ = φ⁺ is continuous and nondecreasing, with |φ_{τ₀}(x)| ≤ C|x|.
- G(δ,τ₀) = φ_{τ₀}(n₀·δ) on Q.
- Squeezing with (M) shows Ψ_{t_m}(δ,τ₀) → φ_{τ₀}(n₀·δ) for **every** δ ∈ ℝ².
- For every δ, Ψ_{t_m}(δ,·) is equi-Lipschitz on J and converges on the dense set E′ ∩ J, hence uniformly on J.
- So **G(δ,τ) exists for all (δ,τ) ∈ ℝ² × J**. It is concave and L|δ|-Lipschitz in τ, and G(·,τ) = φ_τ(n_τ·δ) for
  τ ∈ E′ ∩ J.

**Step 3 (window: profiles are concave; PROVED).** Let τ₀ ∈ E′ ∩ J, x₀ ∈ ℝ, r > 0. Put δ_Y := Yu₀ + x₀n₀ and

  h_Y(s) := G(δ_Y, τ₀ + s/(Yϑ)),  |s| ≤ r.

h_Y is concave in s. For σ = τ₀ + s/(Yϑ) ∈ E′:
- G(δ_Y,σ) = φ_σ(z), with z := n_σ·δ_Y = Y sinΔ + x₀cosΔ → x₀ + s uniformly (Δ = (s/Y)(1+o(1)), since θ′(τ₀) = ϑ);
- φ_σ(z) = G(zn_σ, σ) = G(zn_σ, τ₀) + O(L|z||σ−τ₀|) = φ_{τ₀}(z cosΔ) + O(1/Y).

By uniform continuity of φ_{τ₀} on compacts, h_Y(s) = φ_{τ₀}(x₀+s) + o(1) uniformly on the full-measure set of such s, and
hence on [−r,r] (both sides are continuous). A uniform limit of concave functions is concave. So **φ_{τ₀} is concave on
ℝ**. ∎

**Step 4 (second zoom; PROVED).**
1. *At τ₀ ∈ E′.* φ_{τ₀} is concave with φ(0) = 0. So α_{τ₀} := φ′(0+) and β_{τ₀} := φ′(0−) exist, with
   c_{τ₀} ≤ α ≤ β ≤ C (lower bound by Prop 5.3(c)). Hence G(εδ,τ₀)/ε → α[n·δ]₊ − β[n·δ]₋ as ε ↓ 0.
2. *At every τ.* G(εδ,·)/ε is concave and bounded by C|δ| on J, hence equi-Lipschitz on J₁. It converges on E′ ∩ J₁,
   hence everywhere on J₁. Call the limit G₂.
3. *Two-slope form everywhere.* For τ ∉ E′, take σ → τ in E′:
   - α_σ cos(θ_σ−θ_τ) → G₂(n_τ,τ) =: α_τ, and likewise β;
   - so G₂(·,τ) = α_τ[n_τ·δ]₊ − β_τ[n_τ·δ]₋ for every τ ∈ J₁;
   - α and β are continuous.
4. *Positivity.* α > 0 on int J₁. If α(τ₁) = 0, take δ = n_{τ₁}. Then G₂(δ,·) = α·(n·δ) is concave, ≥ 0 near τ₁ and
   zero at τ₁, so it is ≡ 0 near τ₁. That contradicts α > 0 on E′. Finally β ≥ α > 0. ∎

**Step 5 (projectivity; PROVED).** G₂ satisfies the hypotheses used in the proof of N12 Lemma 4.3 (refereed CORRECT;
N14 notes that Step 2 needs only α > 0):
- two-slope data with continuous n and α, β > 0;
- f_δ(τ) := G₂(δ,τ) concave in τ for every δ;
- n not constant (Thm 4.2).

Hence τ ↦ a(τ) := α_τn_τ is affine on int J₁, and β/α is constant.
- The direction field n_τ is the zero-chord field of Ψ. It does not depend on the subsequence or on J₁.
- So the pencil map τ ↦ [n_τ] is projective on every compact subinterval, hence on (0,1).
- Choosing one normalisation and extending a affinely, define Γ_k on v_k^⊥ = span{r, r′} by Γ_k h(τ) := a(τ). This
  is linear, Γ_k h ∝₊ n_h on relint F_k, and Γ_k has rank 2 because the direction is not constant.
- With Thm 4.2 this is (PC). ∎

---

## 7. Main theorem (N15.8, N15.9)

**Theorem 7.1 (PROVED).** On the U-domain, let (R1), (R2) hold with T all-facing in general position.
Then (PC) and (NS) hold at p\* on all three facets. By N12 Theorem 3.1 this is a contradiction. Hence **T1 is not
realisable**, for any ε ∈ (0,1) and any interior p\*, and neither is any interior ε-contamination triangle.

*Proof.*
1. (PC) is §6 Step 5.
2. (NS): Γ_k r = a(0) ≠ 0 by rank 2, and a(τ) ∝₊ n_τ, so Γ_k r ∝₊ n^k(0+). Theorem 4.3 gives n^k(0+) = n^j(0+),
   i.e. Γ_k r ∝₊ Γ_j r.
3. Theorem 3.1's box step needs uniqueness of clusters at the witnesses (Thm 4.2), so that good A′ near A have chords
   uniformly near λ_A. Its remaining steps use only (PC), (NS) and N12 Thm 2.4. ∎

**Corollary 7.2 (CHECKED).** The same holds on every decomposable domain with (LF) on which a.e. pair meeting U′ is non-adjacent.
- Apply everything to K̂_q = conv(K_q ∪ K′) (N14 §3(iv)).
- Ψ̂ = min(Ψ, P_{K′}(h)) agrees with Ψ at the small levels used.
- Lemma 4.1's appeal to Cor PL2 needs exactly the no-d-face hypothesis, which non-adjacency gives.

**Corollary 7.3 (PROVED given N14 Thm C2).** With bounded charges vanishing on null sets as penalties, and existence of
interior Bayes minimisers, the same conclusion holds.

**What is not covered.**
- Adjacent domains: the box bridge still needs (NA_w) (N14 (E4)).
- Existence of minimisers for charges (part (A)).
- Non-all-facing triangles, i.e. CONJECTURE R15 classes (1,2,3) and non-facing (2,2,2). §§2–6 apply facet by facet
  wherever a facet has a crossing with a shared positive coordinate. Theorem 3.1's pinching is all-facing-specific.
- n > 3.

---

## 8. Points a referee should check first

1. **Lemma 4.1 (Cor PL2 away from p\*).** Γ_v is defined from a fixed small ball U around the crossing. Our hypothesis
   gives K_q ⊆ W_{v}(Ũ) for the enlarged ball, which R10b §1 shows implies Γ_v. G need not contain p\*: Cor PL2 is
   stated for any open connected G ⊆ Γ_v. The relative-openness repair of R12 (β_v open in Γ_v) is all that is used.
2. **Lemma 2.3.** This is the only place where "level lines do not cross inside Ω" is converted into quantitative ridge
   structure. The distortion is relative and tends to 1 with |y|/r₀.
3. **Lemma 5.1 semicontinuity.** The usc/lsc directions are chosen so that only S⁻ (finite) and S⁺ (positive) appear. No
   continuity of contact points is assumed.
4. **§6 Steps 2–3.** These need θ′(τ₀) ∈ (0,∞) at τ₀; Prop 5.3(b) supplies it a.e. The comparison of φ_σ with φ_{τ₀}
   uses only the τ-Lipschitz bound at bounded |δ|.
5. **Use of N12 Lemma 4.3 for G₂.** Its proof uses the two-slope form and concavity of f_δ. Here concavity of f_δ is
   built in, not derived from a limit of P/t.

**No silent regularity.**
- Hausdorff continuity of K_q (N12.1) is the only regularity input.
- Lipschitz control at p\* (Prop 5.3(a)) is derived.
- No boundary-prior coherence is used. Vertex coherence is automatic on this domain and is forced in general.
- No Bayes-at-index selection is assumed.
- Fubini appears only inside the imported Lemma 2.1(b) and UVN.

---

## 9. Numerics (`n15py/`)

| File | What | Result |
|---|---|---|
| `gauge_sanity.py` | Gauge mixture M_i = [e_i,(1−γ)e_i+γu], γ = 0.6, p\* = u; target K_u a hexagon. On each facet: zero set of Ψ(·,τ) on a circle of radius 0.02 (4000 angles, 25 τ's); chord angle monotonicity (200 τ's); Lemma 5.1 at τ₁ = 0.5 with ξ ∈ {0.01, 0.03, 0.06}; corner matching | zero sets are lines through p\* with strict signs on all 6 facets; angles strictly monotone; Lemma 5.1 bounds bracket the true slope α (e.g. facet 0: 0.04779 ≤ 0.04899 ≤ 0.05019 at ξ = 0.01, bracket shrinking as ξ → 0); corner normals agree to 1.5e−6 |

NUMERICS only, on a (DF)-regular family; this checks orientations and constants, not the theorem.
