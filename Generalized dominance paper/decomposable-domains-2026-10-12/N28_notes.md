# N28: competing acceptances on general (LF) decomposable domains. (E5a) is impossible; (E4′) shrinks to vertex caps

14 Oct 2026. This is BRIEF8's second question. Can an additive ranking cover T1 on a decomposable domain with (LF) when the
advice ranges near T1's cone are {accept g, accept −g, silence}, and the two acceptances may compete directly as best advice?

Labels: **PROVED** (full proof here, from the cited refereed inputs), **CHECKED** (verified, proof sketched),
**CONJECTURE**, **NUMERICS**, **REMARK** (heuristic). Scripts are in `n28py/`; the output is `n28py/checks.out`.

Terminology follows the Glossary of *START HERE* and the notation of *The Contamination Triangle.tex* §§2, 4, 5
(Ω = int Δ; P(q,g) = min_{K_q} m·g; for a facet F_k with gambles h(τ): A_τ, B_τ, Z_τ, H⁺_τ, λ_τ, n_τ; B₁ = B(p\*, r₁);
Γ_v, α_v, β_v and Z_v = {q ∈ Ω : K_q = {v}} as in R10b §1; d-face F(g)).

---

## 0. Outcome

The brief offered three outcomes: (a) close (E5a) and (E4′), (b) build a realisation, (c) reduce the question to a
geometric problem. Here (a) is done for (E5a) and for most of (E4′). What remains is one case of (E4′), stated
sharply, together with a reduction of type (c). No realisation was built. The only mechanism previously known to be
consistent at vertex scale, the identity cap of R4 §9, is now excluded.

1. **Two new convexity facts (§2, PROVED, every (LF) decomposable domain, every realisation).** Both follow from
   quasi-concavity (N21.1).
   - For every m₀ ∈ Δ, the wall Z_{m₀} = {q : K_q = {m₀}} is convex.
   - For every vertex e_b, C_b = {q : e_b ∉ K_q} is open and convex.
   - Also, by R4 Thm B: for a.e. pair g, the d-face cl F(g) ∩ Ω contains no prior whose credal set contains a fixed
     point m₀ with m₀·g ≠ 0.
   - A wall of one facet lies inside the positivity set of every relative-interior gamble of the other two facets
     (Lemma 2.4).
2. **Theorem 3.5 (PROVED): (TS) holds in every additive cover of T1** (and of every all-facing triangle in general
   position) on every (LF) decomposable domain. The pinning branch (II) of the dichotomy, i.e. residual (E5a), is empty. The
   proof is a cascade:
   - a pinned facet's wall forbids two-signedness on a second facet (Prop 3.1);
   - so that second facet must itself pin, and its walls face both remaining vertices (Lemma 3.3);
   - then two walls surround p\*, and this contradicts convexity of the third facet's positivity sets (Lemma 3.4).
3. **Corollary 3.6 (PROVED).** T1 has no additive cover on any (LF) decomposable domain on which, for a non-null set of mixed
   pairs, the advice range lacks acceptance of one orientation. Hence every cover has, for a.e. mixed pair, both acceptances in the advice range, precise vertex models
   K_{e_b} = {e_b}, edge-confined boundary limits, and the cut structure of N21.6 at every vertex. Earlier this needed
   the hypothesis (TS) (N21.8(b)).
4. **Theorem 4.1 (PROVED): the cut apexes go to the vertex.** In N21.6 the apex limit is always a\* = e_b. Competition
   between accepting g and accepting −g at a finite distance from ∂Δ is impossible. This settles the case
   "a\* ∈ Ω" that N23 §7.6 singled out.
5. **Proposition 4.3 (PROVED): vertex-free interiors and two-sided chords.** In every cover of T1:
   - no interior credal set contains a vertex of Δ;
   - on each crossing chord λ_b = line(p\*, e_b), every K_q meets both outer half-planes of the two tangent lines from
     e_b to T1, so it is never a singleton.
   Consequently no precise prior lies on a crossing chord. The precise identity cap of R4 §9 cannot be part of a cover
   (NUMERICS confirm the arithmetic, `checks.py` (3)). That cap was the evidence behind the claim that (E4′) is
   consistent at the scale of the vertices, so that claim no longer has support.
6. **Reduction (§5).**
   - **Prop 5.1 (CHECKED):** "T1 has an additive cover on some (LF) decomposable domain" ⇔ "the concurrent-chart family
     problem CF(T1) has a solution". CF(T1) is a purely geometric problem about Hausdorff-continuous credal families.
   - **Prop 5.2 (PROVED):** CF(T) is invariant under independent diagonal projective changes of priors and of
     probabilities.
   - The residual, **(E4″) vertex caps**, is stated in Def 5.3, together with every constraint now known.
   - **CONJECTURE N28:** (E4″) is empty. If so, T1 has no additive cover on any (LF) decomposable domain.
7. **The auditor's point on (LF) (Lemma 0, PROVED).** None of N21, N23 or this note needs a conic neighbourhood. A
   compact neighbourhood of the normalised facet gambles inside N suffices. For a.e. h in the whole cone over N,
   acceptance of h is in the advice range anyway.

**Status of BRIEF8's second question, in one sentence.** Direct competition between accepting g and accepting −g can
help an additive ranking cover T1 only inside neighbourhoods of the three vertices of Δ that shrink to the vertices.
There every crossing chord must carry non-precise credal sets right up to the vertex, and no interior credal set may
touch a vertex. Whether that can happen is the only open case.

Not addressed: the auditor's second repair (BRIEF8 (ii), permitted negligible-stakes ties in N15), and the M0 question.

---

## 1. Setting, inputs, and the (LF) neighbourhood

**Setting.** n = 3. T is T1 (any ε ∈ (0,1)) or, where stated, an all-facing triangle in general position. We have a
strictly guiding additive ranking (integral penalties, or bounded charges vanishing on null sets with interior
minimisers) on a decomposable domain 𝓜 with (LF) at D_T. It satisfies (LA), (S), (C) and covers T. By Prop necessary and
Prop reduction (Contamination Triangle §3) this gives:
- (BU) at every interior q, with K_q unique;
- q ↦ K_q Hausdorff-continuous on Ω;
- P jointly continuous;
- K_{p\*} = T for some p\* ∈ Ω.

**Refereed inputs used** (status as in the Contamination Triangle table):
- N21.1 (quasi-concavity, every g ∈ ℝ³) and N21.1′;
- N21.2 / Lemma B1 (ball B₁, half-plane charts of near-facet gambles on B₁);
- N21.4 items 1–5. Item 5 is the c-cluster sign: under (TS) at τ, n_τ·(e_l − p\*) ≤ 0 whenever h(τ)_l < 0;
- N21.6, N21.7, N21.9 (i)–(iii);
- Lemma R23.1, Cor R23.2 (second reading CORRECT);
- R10b: UVN, Lemmas D and M, Theorem PL;
- R4 Thm B;
- Lemma signs (Contamination Triangle Lemma 4.1).

**Lemma 0 (no conic neighbourhood is needed; PROVED).** Let N ⊇ ∂D_T ∖ 0 be any open set, as (LF) supplies. Fix
0 < ρ₁ < ρ₂. Put Φ := {h ∈ F₁ ∪ F₂ ∪ F₃ : ρ₁ ≤ |h| ≤ ρ₂}. This set is compact, and ρ₁, ρ₂ are chosen so that Φ contains
every facet gamble used below: the h(τ), τ ∈ [0,1], the crossings, and the box witnesses A_s, B_s at small s.
- (a) There is δ₀ > 0 such that N₀ := {h : dist(h, Φ) ≤ δ₀} satisfies N₀ ⊆ N and P_{K″} > 0 on N₀. On N₀ the advice ranges
  are {+,0} or {+,0,−} a.e. (up to the irrelevant ×).
- (b) For a.e. h in the open cone ℝ₊N, acceptance of h is in the advice range.
- (c) Every step of N21, N23 and this note that cites "N₀" uses only gambles in N₀. These are the facet gambles, their
  level shifts h − c𝟙 with |c| small, the box witnesses, the N21.6 test gambles w\* − δ𝟙 + ηe_b, and good gambles
  near all of these. Everything else is a statement about P(q,·), which is positively homogeneous, so the scale of a
  gamble never matters there.

*Proof.*
- (a) Φ is compact, Φ ⊆ ∂D_T ∖ 0 ⊆ N, and P_{K″} > 0 on Φ (N23 §1). N is open and P_{K″} is continuous. Note that
  the facets are cones: if a gamble at some other scale is needed, the scale can be moved into [ρ₁, ρ₂] before ρ₁, ρ₂
  are fixed.
- (b) By R10a Cor V2(c), N ⊆ Av a.e. and Av ≈ ∪_i D_{V_i} off the non-positive orthant. A union of open cones is an
  open cone, and the boundary of ∪_i D_{V_i} is null. So ℝ₊N ⊆ cl(∪_i D_{V_i}) ⊆ Av a.e.
- (c) By inspection of N21 §§1–6, N23 §§3–7 and §§2–4 below. N21 §1 lists exactly these gambles. N23's repair "levels
  must lie in int N₀" keeps |c| small. R10b and R23.1 use balls U ⊆ int N₀ around crossings. ∎

*Remark.* Silence may be missing from the advice range at scales outside N. That would give advice range {+,−}. Pairs with this advice range have the global
half-plane charts {d·q > 0} (R1 table) and are adjacent everywhere. None of the arguments below needs silence outside
N₀.

---

## 2. Convexity facts

Fix a realisation as in §1.

**Lemma 2.1 (walls are convex; PROVED).** For every m₀ ∈ Δ, Z_{m₀} := {q ∈ Ω : K_q = {m₀}} is convex and relatively
closed in Ω.

*Proof.*
- Z_{m₀} = ∩_{h : m₀·h > 0} {q : P(q,h) > 0}.
  - (⊆) If K_q = {m₀}, then P(q,h) = m₀·h.
  - (⊇) If K_q ∋ m ≠ m₀, take h := (m₀ − m) + t𝟙, choosing t so that m·h ≤ 0 < m₀·h. This is possible because
    (m₀ − m)·m₀ − (m₀ − m)·m = |m₀ − m|² > 0. Then P(q,h) ≤ m·h ≤ 0.
- Each set {P(·,h) > 0} is convex (N21.1). Closedness follows from Hausdorff continuity. ∎

**Lemma 2.2 (vertex-avoiding priors form a convex set; PROVED).** For each world b, C_b := {q ∈ Ω : e_b ∉ K_q} is open
and convex.

*Proof.* C_b = {q : P(q, 𝟙 − e_b) > 0}, since m·(𝟙 − e_b) = 1 − m_b vanishes on Δ only at e_b. Convexity is N21.1
(valid for every g ∈ ℝ³). Openness is continuity of P. ∎

**Lemma 2.3 (d-faces avoid fixed points; PROVED).** For a.e. pair g, for every m₀ ∈ Δ with m₀·g ≠ 0, the set
cl F(g) ∩ Ω contains no q with m₀ ∈ K_q. In particular:
- cl F(g) ∩ Ω ⊆ C_b for every b with g_b ≠ 0;
- cl F(g) ∩ Z_{m₀} = ∅.

*Proof.* R4 Thm B: for a.e. g, K_q ⊆ g^⊥ for every q ∈ cl F(g) ∩ Ω. ∎

**Lemma 2.4 (walls lie in the other facets' positivity sets; PROVED).** Let v_m be a vertex of T and i ≠ m. For every
τ ∈ (0,1), Z_{v_m} ⊆ A^i_τ := {q : P(q, h^i(τ)) > 0}. Moreover p\* ∉ A^i_τ, and A^i_τ is convex.

*Proof.*
- On Z_{v_m}, P(q, h^i(τ)) = v_m·h^i(τ). This is > 0, because relint F_i = {h : h·v_i = 0, h·v_j > 0 (j ≠ i)}.
- P(p\*, h^i(τ)) = 0, since h^i(τ) ∈ ∂D_T.
- Convexity is N21.1. ∎

---

## 3. (E5a) is impossible

Recall N21.9 (refereed, CORRECT). Suppose p\* ∉ cl A^m_{τ₀} for some facet F_m and some τ₀, i.e. A^m_{τ₀} ∩ B(p\*,ρ) = ∅.
Choose σ₁ < τ₀ < σ₂ such that:
- [σ₁,σ₂] contains a crossing τ_c of F_m;
- h(σ₁) and h(σ₂) share a positive coordinate l (l ≠ m, since h_m < 0 on F_m).

Put O := int(P_{σ₁} ∩ P_{σ₂}) ∩ B(p\*,ρ). Then:
- O is open and nonempty, and p\* ∈ cl O;
- v_m ∈ K_q on O, and O ⊆ Γ_{v_m};
- **every segment [o,v] with o ∈ O and v ∈ V_l ∩ Ω meets Z_{v_m}**. Here V_l is the UVN neighbourhood of e_l at
  w = h(τ_c).

Call this a **wall of F_m toward V_l, with pinned set O**.

**Which l occurs (Lemma signs).** Label the crossings of F_m as τ_x < τ_y, with sign pattern (h_x, h_y) = (−,+) on
[0,τ_x), (+,+) on (τ_x,τ_y), (+,−) on (τ_y,1]. There are two admissible choices of (σ₁,σ₂) (N15 Step 1):
- *Option 1* (when τ₀ < τ_y): σ₁ ∈ (0, min(τ₀,τ_x)), σ₂ ∈ (max(τ₀,τ_x), τ_y). The crossing is τ_x and l = y.
- *Option 2* (when τ₀ > τ_x): σ₁ ∈ (τ_x, min(τ₀,τ_y)), σ₂ ∈ (max(τ₀,τ_y), 1). The crossing is τ_y and l = x.

So an A-failure at τ₀ gives a wall:
- toward V_y if τ₀ ≤ τ_x;
- toward V_x if τ₀ ≥ τ_y;
- toward **both** V_x and V_y if τ₀ ∈ (τ_x, τ_y).

N21.9's proof applies verbatim to either option. It needs only τ₀ ∈ (σ₁,σ₂), a crossing in (σ₁,σ₂), and the shared
positive coordinate (for UVN).

**Proposition 3.1 (a wall forbids two-signedness elsewhere; PROVED).** Let F_m have a wall toward V_l with pinned set
O. Let i ≠ m and τ₁ ∈ (0,1) satisfy h^i(τ₁)_l < 0. Then (TS) fails at τ₁ on F_i, i.e. p\* ∉ cl A^i_{τ₁} ∩ cl B^i_{τ₁}.

*Proof.* Suppose (TS) holds at τ₁ on F_i.
1. *Half-plane confinement.* By local straight levels (N21.4 item 1, levels in N₀), A^i_{τ₁} ∩ B₁ and B^i_{τ₁} ∩ B₁
   are the two open half-discs of one line λ through p\*. Let H⁺ be the positive side and n its unit normal.
   N21.1′ gives A^i_{τ₁} ⊆ H⁺.
2. *Sign at e_l.* The c-cluster argument (N21.4 item 5) gives n·(e_l − p\*) ≤ 0, because h^i(τ₁)_l < 0. It needs both
   half-discs, i.e. (TS) at τ₁.
3. *A point v.* There is v ∈ V_l ∩ Ω with n·(v − p\*) =: −b < 0.
   - If n·(e_l − p\*) < 0, take v near e_l.
   - If n·(e_l − p\*) = 0, then e_l does not minimise n·x over Δ, because n·p\* = n·e_l with p\* interior and n ≠ 0 in
     𝟙^⊥. So points of Δ arbitrarily near e_l have n·(x − p\*) < 0.
4. *The wall is far from p\*.* d := dist(p\*, Z_{v_m}) > 0, since Z_{v_m} is relatively closed and K_{p\*} = T ≠ {v_m}.
5. *Estimate.* Take o ∈ O with |o − p\*| < δ (possible since p\* ∈ cl O). Suppose x = (1−t)o + tv satisfies
   n·(x − p\*) > 0. Then t < δ/(δ + b) ≤ δ/b, so |x − p\*| ≤ δ(1 + 2/b) (diam Δ ≤ √2 < 2).
6. *Contradiction.* By N21.9, [o,v] meets Z_{v_m} at some Q. By Lemma 2.4, Q ∈ A^i_{τ₁} ⊆ H⁺. So
   d ≤ |Q − p\*| ≤ δ(1 + 2/b), which fails for small δ. ∎

(`checks.py` (5): the estimate holds in 20 000 random configurations, with the ratio ≤ 0.51.)

**Lemma 3.2 (B-failures cannot straddle a crossing next to a pinned set; PROVED).** Let F_m have a pinned set O as
above, and let F_l be another facet (l ≠ m). There are no σ₁ < τ_c < σ₂ with τ_c a crossing of F_l and
p\* ∉ cl B^l_{σ₁}, p\* ∉ cl B^l_{σ₂}.

*Proof.*
- Otherwise Ψ^l(·,σ_i) ≥ 0 on B(p\*,ρ) for some ρ ≤ r₁.
- Lemma R23.1 gives v_l ∈ K_q and B(p\*,ρ) ⊆ Γ_{v_l} (R23.1 Step 1).
- O′ := O ∩ B(p\*,ρ) is open and nonempty (p\* ∈ cl O), with O′ ⊆ Γ_{v_m} ∩ Γ_{v_l} and v_m, v_l ∈ K_q on O′.
- This contradicts Theorem PL (R10b). The balls around the two crossings may be shrunk to meet PL's requirements;
  shrinking a ball enlarges Γ. ∎

**Lemma 3.3 (a facet that fails (TS) everywhere has walls toward both other vertices; PROVED).** Assume F_m has a pinned
set, and that (TS) fails at every τ ∈ (0,1) on another facet F_l. Let x, y be the two indices other than l. Then F_l
has a wall toward V_x and a wall toward V_y, each with a pinned set whose closure contains p\*.

*Proof.*
- Put β := {τ : p\* ∉ cl B^l_τ} and α := {τ : p\* ∉ cl A^l_τ}. By hypothesis α ∪ β = (0,1).
- By Lemma 3.2, β has no points on both sides of τ_x and none on both sides of τ_y. So β is contained in (0,τ_x],
  [τ_x,τ_y] or [τ_y,1). Therefore α contains:
  - (τ_x, 1) in the first case, which includes τ ∈ (τ_x,τ_y) and gives walls toward both V_x and V_y;
  - (0,τ_x) ∪ (τ_y,1) in the second case: Option 1 at τ < τ_x gives a wall toward V_y, and Option 2 at τ > τ_y gives
    a wall toward V_x;
  - (0,τ_y) in the third case, which again includes τ ∈ (τ_x,τ_y). ∎

**Lemma 3.4 (surround; PROVED).** Let Z, Z′ ⊆ Ω be relatively closed, with p\* ∉ Z ∪ Z′. Let {a,b,c} = {1,2,3}, and let
O₁, O₂, O₃ be sets with p\* in their closures. Suppose:
- Z meets every segment from O₁ to V_a ∩ Ω and every segment from O₂ to V_b ∩ Ω;
- Z′ meets every segment from O₃ to V_c ∩ Ω,

where each V_i is a relative neighbourhood of e_i in Δ. Then p\* ∈ conv(Z ∪ Z′).

*Proof.*
1. *Choices.* Let d := dist(p\*, Z ∪ Z′) > 0 and let δ be small. Pick o_i ∈ O_i and v_i ∈ V_i ∩ Ω within δ of p\* and
   of e_i. Let Q_i ∈ (Z or Z′) ∩ [o_i, v_i], and write Q_i = o_i + t_i(v_i − o_i).
2. *Each Q_i points roughly toward e_i.* Since |Q_i − p\*| ≥ d, we have t_i ≥ (d − δ)/2. Also
   Q_i − p\* = t_i(e_i − p\*) + ε_i with |ε_i| ≤ 2δ. So (Q_i − p\*)/t_i is within 4δ/(d − δ) of e_i − p\*.
3. *Openness.* 0 ∈ int conv{e_i − p\*} (in 𝟙^⊥), because p\* ∈ int Δ, and this condition is open under perturbation.
   So for small δ, 0 = Σ λ_i (Q_i − p\*)/t_i with λ_i ≥ 0 and Σλ_i = 1.
4. Then p\* is a convex combination of Q₁, Q₂, Q₃. ∎

(`checks.py` (4): 0 failures in 3000 random trials at δ/d ∈ {0.02, 0.1}. Failures appear at δ/d = 0.5 and 0.9, so the
smallness of δ is needed.)

**Theorem 3.5 ((TS) holds in every cover; PROVED).** Let T be T1 (any ε ∈ (0,1)), or any all-facing triangle in
general position. Let a strictly guiding additive ranking on a decomposable domain with (LF) cover T, with (BU) at every
interior prior and K_{p\*} = T. Then (TS) holds.

*Proof.*
1. Suppose (TS) fails. By Cor R23.2, (TS_A) fails on some facet F_m. N21.9 then gives a wall of F_m toward some V_l
   with pinned set O, with l ≠ m.
2. On F_l, h^l(τ)_l < 0 for every τ ∈ (0,1) (Lemma signs). By Prop 3.1 (with i = l), (TS) fails at every τ on F_l.
3. By Lemma 3.3, F_l has walls toward V_m and toward V_n, where n is the third index.
4. By Lemma 2.1 the walls Z_{v_l} and Z_{v_m} are relatively closed, and neither contains p\*. Apply Lemma 3.4:
   - with Z = Z_{v_l}, which meets the segments toward V_m and V_n;
   - with Z′ = Z_{v_m}, which meets the segments toward V_l.

   This gives p\* ∈ conv(Z_{v_l} ∪ Z_{v_m}).
5. Lemma 2.4 with i = n: Z_{v_l} ∪ Z_{v_m} ⊆ A^n_τ for every τ ∈ (0,1). A^n_τ is convex and does not contain p\*.
   This contradicts step 4. ∎

*Where general position and all-facing enter.* Every facet has two crossings, with the sign pattern of Lemma signs.
Every vertex of T has a crossing (needed for PL, UVN and Lemma M). R23.1/R23.2 hold for this class (N23 §8).

**Corollary 3.6 (PROVED).**
- (a) Branch (II) of the dichotomy (Contamination Triangle Thm 5.10), i.e. residual (E5a), never occurs. Every cover
  is in branch (I): (TS), (PC) and (NS) hold, and so do the conclusions of N21.6 and N21.7 at every world b with a
  failing box.
- (b) For T1 (failing box at every b, N23 §6): T1 has no additive cover on any (LF) decomposable domain on which, for a non-null
  set of mixed pairs, the advice range lacks acceptance of one of the two orientations. Examples:
  - any non-null set of mixed pairs with advice range ⊆ {+,0}, ⊆ {0,−}, or {0};
  - any open cone of mixed orientations h that no evaluable model accepts;
  - any domain on which every evaluable model gives no advice on a non-null set of mixed pairs.
- (c) In every cover of T1, K_{e_b} = {e_b} for all b. For every edge prior with support S, every limit of K_q as q
  approaches it through Ω lies in Δ_S.

*Proof.* (a) Theorem 3.5. (b) and (c): N21.7 and N21.8(b), whose only extra hypothesis was (TS). ∎

So the case BRIEF8 asks about, "acceptances of g and −g both in the advice range and competing near T1's cone", is not
just possible but necessary on almost every mixed pair.

---

## 4. (E4′): the apex goes to the vertex

Standing: a cover of T1, so branch (I) holds (Theorem 3.5). Fix a world b. Let a be the index with Λ_{ab} > 1 (N23 §6),
and c the third index. The two b-crossings are:
- w′ ∈ relint F_a, with w′_b = 0 and w′_a < 0 < w′_c;
- w ∈ relint F_c, with w_b = 0 and w_c < 0 < w_a.

For T1 with (a,b,c) = (1,2,3), w′ ∝ (−1,0,κ) and w ∝ (κ,0,−1). By Thm pivot (local, under (TS)) both crossing chords
are the same line, λ_b := line(p\*, e_b).
- For F_a's orientation, e_a lies strictly on the negative side and e_c on the positive side.
- For F_c's orientation, the sides are swapped.

The strict sign at e_a holds because λ_b ≠ line(p\*, e_a). (`checks.py` (2): 48/48 cases, both x₊ and x₋, four values
of ε.)

The tangent lines from e_b to T are ℓ′ := w′^⊥ ∩ aff Δ = line(e_b, v_a) and ℓ := w^⊥ ∩ aff Δ = line(e_b, v_c).

**Fact 4.0 (PROVED).** {m ∈ Δ : m·w′ ≤ 0, m·w ≤ 0} = {e_b}.

*Proof.* Write m = e_b + α(e_a − e_b) + γ(e_c − e_b) with α, γ ≥ 0. The two inequalities read
γw′_c ≤ α|w′_a| and αw_a ≤ γ|w_c|. An interior point of T satisfies both strictly reversed, so w′_c w_a > |w′_a||w_c|.
Hence αγ = 0, and then α = γ = 0. ∎
(`checks.py` (1): an LP gives max{1 − m_b} = 0 for all b and ε ∈ {.05, .3, .6, .9}.)

**Fact 4.0′ (PROVED).** For m on ℓ_{w\*} ∩ Δ, with ℓ_{w\*} ∈ {ℓ′, ℓ}, and w\*\* the other b-crossing:
m·w\*\* = t·(v_{k\*}·w\*\*) with t ≥ 0. Here v_{k\*}·w\*\* > 0, and t = 0 iff m = e_b.

*Proof.* Write m = (1−t)e_b + t v_{k\*}. Then t < 0 leaves Δ, w\*\*_b = 0, and w\*\* ∈ relint F_{k\*\*} with
k\*\* ≠ k\*. ∎
(`checks.py` (1): min v_{k\*}·w\*\* > 0.)

Recall N21.6 (refereed, CORRECT). There are good g_m with advice range {+,0,−} near one b-crossing w\* ∈ F_{k\*} with:
- d-faces F(g_m) ∩ Ω = (a_m, z_m);
- a_m → a\* ∈ [e_b, p\*] ∖ B₁ and z_m → z\* ∈ [e_b, e_a);
- K_q ⊆ ℓ_{w\*} for every q ∈ [a\*, z\*] ∩ Ω.

In the A-case w\* = w′ and z\* = e_b; in the B-case w\* = w. We may take the g_m in the co-null set where R4 Thm B holds
and (g_m)_b ≠ 0.

**Theorem 4.1 (apex at the vertex; PROVED).** a\* = e_b.

*Proof.* Suppose a\* ≠ e_b, so a\* ∈ Ω. Let w\*\* be the other b-crossing, on F_{k\*\*}, and let H⁺, H⁻ be the sides of
λ_b for F_{k\*\*}'s orientation.

*Step 1 (chord facts).*
- (TS) on F_{k\*\*} at the crossing gives Z ∩ B₁ = λ_b ∩ B₁ for P(·,w\*\*).
- N21.1′ gives {P(·,w\*\*) > 0} ⊆ H⁺, so P(·,w\*\*) ≤ 0 on Ω ∖ H⁺.
- {P(·,w\*\*) ≥ 0} is convex (N21.1).
- By Fact 4.0′, P(q,w\*\*) ≥ 0 for every q ∈ [a\*, z\*] ∩ Ω.

*Step 2 (B-case with z\* ≠ e_b).* Here w\* = w, k\*\* = a, w\*\* = w′.
- z\* ∈ (e_b, e_a) lies strictly on e_a's side of λ_b, which is H⁻.
- Pick q₁ ∈ (a\*, z\*) ⊆ Ω; it lies in the open set H⁻. Let I := λ_b ∩ B(p\*, r₁/2).
- On the triangle conv(I ∪ {q₁}) ⊆ cl H⁻, P(·,w′) ≥ 0 (convexity, Step 1) and P(·,w′) ≤ 0 (Step 1). So
  P(·,w′) = 0 there.
- But p\* + t(q₁ − p\*) lies in that triangle, in B₁ and off λ_b for small t > 0. This contradicts
  Z ∩ B₁ = λ_b ∩ B₁.

*Step 3 (z\* = e_b, A-case or B-case).*
- Fix x ∈ I. The segment [x, a\*] ⊆ λ_b ∩ Ω carries P(·,w\*\*) ≥ 0 (convexity, with P = 0 on I and P(a\*,w\*\*) ≥ 0)
  and P(·,w\*\*) ≤ 0 (λ_b ⊆ Ω ∖ H⁺). So P(a\*, w\*\*) = 0.
- By Fact 4.0′, some m ∈ K_{a\*} has t = 0, i.e. **e_b ∈ K_{a\*}**, so a\* ∉ C_b.
- C_b is open and convex (Lemma 2.2), and p\* ∈ C_b. Separate: there is an affine φ with φ(a\*) = 0 < φ on C_b. Then
  φ(p\*) > 0, so φ < 0 on (a\*, e_b].
- Fix y ∈ (a\*, e_b) ⊆ Ω and r > 0 with φ < 0 on B(y,r). Then B(y,r) ∩ Ω ⊆ Ω ∖ C_b.
- The segments (a_m, z_m) → [a\*, e_b] in the Hausdorff sense, so for large m some p_m ∈ F(g_m) lies in B(y,r).
- Then e_b ∈ K_{p_m}, against Lemma 2.3, since (g_m)_b ≠ 0. ∎

*Scope.* The proof uses N21.6 at b, (TS), the chord facts and Lemmas 2.2–2.3. So it holds for every all-facing T in
general position at every world b with a failing box.

**Proposition 4.3 (structure of every cover of T1 near the vertices; PROVED).**
- (i) **No interior credal set contains a vertex of Δ:** C_b = Ω for b = 1, 2, 3.
- (ii) **Chord–tangent duality.** For every facet F_k, every τ ∈ (0,1) and every q ∈ Ω ∖ H⁺_τ:
  K_q ∩ {m : m·h(τ) ≤ 0} ≠ ∅. That is, K_q is not inside the open inner side of the supporting line h(τ)^⊥ of T at
  v_k.
- (iii) **Two-sided chords.** For q ∈ λ_b ∩ Ω, K_q meets both {m·w′ ≤ 0} and {m·w ≤ 0}. So K_q contains two distinct
  points, one on or beyond ℓ′ and one on or beyond ℓ. In particular K_q is not a singleton. More generally:
  - on the closed e_a-side of λ_b, K_q meets {m·w′ ≤ 0};
  - on the closed e_c-side, K_q meets {m·w ≤ 0}.
- (iv) **No precise prior lies on a crossing chord.**
  - Consequently, no open precise region of R4 Prop D type (diagonal-projective or constant) meets any λ_b.
  - The identity cap K_q = {q} near e_b (R4 §9) is incompatible with every cover.
  - Under R4's continuity hypothesis (H1⁺), all d-faces are precise (R4 Thm C), hence disjoint from the three chords.

*Proof.*
- (i) Let y ∈ Ω with e_b ∈ K_y, so y ∉ C_b.
  - C_b contains points arbitrarily near e_a and e_c, because K_q → {e_a}, {e_c} at the vertices (Cor 3.6(c) with
    R10b V2).
  - Separate y from C_b: φ(y) = 0 < φ on C_b, so φ(e_a), φ(e_c) ≥ 0.
  - y is a strict convex combination of the vertices, and φ ≢ 0 on aff Δ. Hence φ(e_b) < 0, and φ < 0 on a relative
    neighbourhood V of e_b in Δ, with V ∩ Ω ⊆ Ω ∖ C_b.
  - By Theorem 4.1, the apexes a_m ∈ cl F(g_m) ∩ Ω converge to e_b. So some a_m lies in V. Then e_b ∈ K_{a_m}, against
    Lemma 2.3.
- (ii) N21.1′: {P(·,h(τ)) > 0} = A_τ ⊆ H⁺_τ. So P(q,h(τ)) ≤ 0 off H⁺_τ.
- (iii) λ_b is the boundary of both relevant half-planes, so (ii) applies to w′ and to w at τ_b. The points cannot
  coincide: by Fact 4.0 a common point would be e_b, which is excluded by (i). The one-sided versions are (ii) at τ_b.
- (iv) A singleton K_q = {σ} on λ_b would satisfy σ·w′ ≤ 0 and σ·w ≤ 0, so σ = e_b (Fact 4.0), against (i).
  - For a diagonal-projective σ, σ(q) ∈ Ω on chord points.
  - A constant σ ≡ m₀ forces m₀ = e_b.
  - For the identity cap, P(q,w′) = q·w′ = t·(p\*·w′) > 0 on the chord q = e_b + t(p\* − e_b).
  - (`checks.py` (3): at ε = 0.2, the case R4 §9 used, the identity cap gives max(q·w′, q·w) > 0 at every chord point
    for all three b. Among 2000 random diagonal-projective caps, none has both values ≤ 0.) ∎

*Remarks.*
- (ii) is a strict refinement near e_b. Choose δh := h′(τ_b) with δh_b > 0. Superadditivity of P(q,·) gives
  P(q,w′) ≤ −(τ − τ_b)P(q,δh) for q ∉ H⁺_τ, τ > τ_b. Near e_b, P(q,δh) ≈ δh_b > 0. So **P(·,w′) < 0 strictly on the
  open e_a-side of λ_b near e_b**: K_q pokes strictly beyond ℓ′ there (CHECKED). Symmetrically, P(·,w) < 0 on the
  open e_c-side.
- In the B-case with a\* = e_b and z\* ∈ (e_b, e_a), the d-faces converge to the edge segment [e_b, z\*]. Along them,
  K_q ⊆ g_m^⊥ → ℓ, and edge confinement forces K_q → ℓ ∩ [e_a, e_b] = {e_b} (CHECKED).

---

## 5. Reduction, invariance, and the residual

**Problem CF(T) (concurrent-chart family).** Find a Hausdorff-continuous map q ↦ K_q, from Ω to credal sets, with
K_{p\*} = T for some p\* ∈ Ω, such that for a.e. mixed g ∈ ℝ³ the following holds. There are c, c′ ∈ ℝ³ with
sign c_i = sign g_i = −sign c′_i (i = 1, 2, 3) and, for **every** q ∈ Ω:
- P_{K_q}(g) > 0 ⟺ c·q > max(0, c′·q);
- P_{K_q}(−g) > 0 ⟺ c′·q > max(0, c·q).

So the "accept g / accept −g / neither" partition of the prior triangle is the cell decomposition of max{0, c·q, c′·q}:
three concurrent lines, with R1's vertex signs.

**Proposition 5.1 (CHECKED).** T1 has an additive cover (integral penalties) on some decomposable domain with (LF) iff CF(T1)
has a solution. The prior p\* can then be chosen arbitrarily in Ω.

*Proof sketch.*
- (⇒) Prop necessary and Prop reduction give the family. By Cor 3.6(b), the advice range of a.e. mixed pair contains both
  acceptances, so advice ranges are {+,0,−} or {+,−} (× is never chosen).
  - For good g, R(±g) and {P(·,±g) > 0} are open, convex and a.e. equal, hence equal.
  - A {+,−} chart {d > 0}/{d < 0} is the cell decomposition, for advice range {+,0,−}, of (c, c′) = (λd + e₀𝟙, (λ−1)d + e₀𝟙) for
    0 < λ < 1 and small e₀ > 0. These data have the strict signs, and the silence cell is empty (as in N23's identity
    example).
- (⇐) Use the all-model domain: advice ranges {+,0,−}, which gives (LF).
  - Penalties come from R1 Prop 2.1 (converse), rescaled per pair to be integrable.
  - The admissible set {(g,c,c′)} is Borel. Equality of open convex sets is tested on a countable dense set of q.
    Jankov–von Neumann gives a measurable selection.
  - For each interior q, the tie set is ⊆ ∂D_{K_q}, which is null. So the Bayes model is D_{K_q} at **every**
    interior q.
  - Theorem CCIBU gives (LA), (S), (C).
- p\* is arbitrary by Prop 5.2(a). ∎

**Proposition 5.2 (invariance; PROVED).** Let D, D′ be positive diagonal matrices and ν the normalisation.
- (a) *Priors.* If K solves CF(T) at p\*, then K̃_{q̃} := K_{ν(D′^{-1}q̃)} solves CF(T) at ν(D′p\*), with chart data
  D′^{-1}c and D′^{-1}c′.
- (b) *Probabilities.* K′_q := ν(D^{-1}K_q) solves CF(ν(D^{-1}T)) at the same p\*, with data c′(Dg) := c(g).

*Proof.*
- (a) c·ν(D′^{-1}q̃) is a positive multiple of (D′^{-1}c)·q̃, and the signs are preserved.
- (b) m·g > 0 ⟺ (D^{-1}m/𝟙·D^{-1}m)·(Dg) > 0. Projective maps preserve convexity of credal sets and Hausdorff
  continuity. g ↦ Dg preserves sign patterns and null sets. ∎

(a) is Prop reduction (d). (b) seems not to have been recorded. It says that coverability of T depends only on the
orbit of T under diagonal projective maps of the probability simplex.

**REMARK (blow-up heuristics).** Take D_s^{-1} := diag with entries 1/s at a and c and 1 at b. This magnifies a
neighbourhood of e_b of size s to unit size. It maps T1 to thin triangles that converge, as s ↓ 0, to the segment
[π(v_a), π(v_c)] on the edge [e_a,e_c]. Here π is the central projection from e_b, so this segment is the shadow of T1
seen from e_b. The vertex-cap regime is therefore a statement about CF families for a sequence of targets in T1's
diagonal orbit that degenerates to a boundary segment target. These connect to the open segment and boundary targets
(T3, T4) of the Contamination Triangle §7.3. Nothing here is proved; it suggests where to look.

**Definition 5.3 (residual (E4″): vertex caps).** A solution of CF(T1) such that, at every vertex b (notation of §4):
1. (TS), (PC) and (NS) hold at p\*, with facet data x₊ or x₋ (Prop T1 corner equations). The box fails at (a, b).
2. K_{e_b} = {e_b}, with edge confinement at every edge prior.
3. The failing box is cut by d-faces F(g_m) ∩ Ω = (a_m, z_m) of good gambles g_m → w\* ∈ {w′, w}, with K_q ⊆ g_m^⊥ on
   them, **a_m → e_b**, and z_m → z\* ∈ [e_b, e_a). In the A-case z\* = e_b. If z\* ≠ e_b, then K_q → {e_b} along
   the d-faces near (e_b, z\*).
4. **No K_q (q ∈ Ω) contains a vertex of Δ.**
5. For every facet F_k and τ ∈ (0,1): A_τ ⊆ H⁺_τ, and K_q meets {m·h(τ) ≤ 0} for every q ∉ H⁺_τ.
6. **On λ_b ∩ Ω, K_q is non-precise and meets both outer half-planes of ℓ′ and ℓ.** Near e_b, K_q pokes strictly
   beyond ℓ′ on the open e_a-side of λ_b, and strictly beyond ℓ on the open e_c-side.
7. For a.e. pair, every d-face avoids every set {m₀ ∈ K_q} with m₀·g ≠ 0, and every wall Z_{m₀} is convex.

By §§3–4, every additive cover of T1 on an (LF) decomposable domain yields a solution of (E4″). Conversely (E4″) is a
sub-case of CF(T1). So:

**Theorem 5.4 (PROVED, from §§3–4 and Prop 5.1 (⇒)).** T1 has an additive cover on some (LF) decomposable domain only if
(E4″) has a solution.

**CONJECTURE N28.** (E4″) has no solution. Equivalently, T1 has no additive cover on any (LF) decomposable domain.

Evidence:
- the identity cap was the only known mechanism consistent at vertex scale, and it is excluded (Prop 4.3(iv));
- every precise or diagonal-projective local model is excluded on the chords;
- condition 6 forces non-precise credal sets that straddle the tangent wedge at e_b along a chord ending at e_b;
- condition 4 forbids them from reaching e_b at any interior prior.

What a construction would need is not known. A cap would need:
- non-precise credal sets along λ_b that shrink to e_b and avoid it;
- precise (under (H1⁺)) or segment d-faces in the two sectors between λ_b and the edges, cutting the box at scale s
  within O(s) of e_b;
- consistency of every concurrent chart for gambles with small h_b.

**Suggested next step.** Set up the blow-up at e_b of Remark 5.2 under a linear-scaling hypothesis
K_{e_b+sy} = e_b + sκ(y) + o(s), and test conditions 3–6 on the limit family κ. Two outcomes are possible:
- an inconsistency in the limit would prove CONJECTURE N28 under that hypothesis;
- a consistent limit would be a concrete local model to try to extend.

---

## 6. Answer to the brief's question

*Can an additive ranking cover T1 on an (LF) decomposable domain where the advice ranges near T1's cone are {accept g,
accept −g, silence} and the acceptances compete?*

- **It must.** In every cover, the advice range of a.e. mixed pair contains both acceptances (Cor 3.6(b)). Competition is forced at
  every vertex (N21.6 under (TS), now unconditional).
- **(E5a) is closed** (Theorem 3.5). No single-vertex pinning near p\*, ball-pinned or thin, exists in any cover.
- **(E4′) is closed except for vertex caps.**
  - Competition at a finite distance from ∂Δ is impossible: a\* = e_b (Theorem 4.1).
  - At vertex scale the only known consistent model (the precise identity cap) is excluded (Prop 4.3).
  - The remaining case (E4″) has the explicit constraints of Def 5.3.
- **No realisation was constructed.** Any realisation must satisfy Def 5.3 1–7. In particular it needs non-precise
  credal sets on the three crossing chords right up to the vertices, while no interior credal set touches a vertex.
- **Sharp reformulation:** CF(T1), modulo diagonal projective symmetries (Props 5.1, 5.2).

---

## 7. Status table, and what a second reader should check

| Result | Label | Depends on |
|---|---|---|
| Lemma 0 (no conic N₀ needed) | PROVED | R10a V2; inspection of N21/N23 |
| Lemma 2.1 (walls Z_{m₀} convex) | PROVED | N21.1 |
| Lemma 2.2 (C_b open convex) | PROVED | N21.1 |
| Lemma 2.3 (d-faces avoid fixed points) | PROVED | R4 Thm B |
| Lemma 2.4 (walls inside other facets' A-sets) | PROVED | N21.1 |
| Options 1/2 for N21.9 walls | PROVED | N21.9 proof, Lemma signs |
| Prop 3.1 (wall vs two-signedness) | PROVED | N21.4 items 1, 5; N21.1′; N21.9; UVN |
| Lemma 3.2 (no straddling B-failures) | PROVED | R23.1; R10b Thm PL |
| Lemma 3.3 (walls toward both vertices) | PROVED | Lemma 3.2; N21.9 |
| Lemma 3.4 (surround) | PROVED | elementary |
| **Theorem 3.5 ((TS) in every cover; (E5a) empty)** | **PROVED** | Cor R23.2 and the above |
| Cor 3.6 (advice ranges, precise vertices, edge confinement) | PROVED | Theorem 3.5; N21.7, N21.8 |
| Facts 4.0, 4.0′ | PROVED (NUMERICS confirm) | Lemma signs |
| **Theorem 4.1 (a\* = e_b)** | **PROVED** | N21.6; Thm pivot (local); N21.1, N21.1′; Lemmas 2.2–2.3 |
| Prop 4.3 (vertex-free interiors, chord duality, two-sided chords, no precise chord points) | PROVED | Theorem 4.1; Cor 3.6(c); R10b V2 |
| Remarks after Prop 4.3 | CHECKED | superadditivity of P; edge confinement |
| Prop 5.1 (CF equivalence) | CHECKED | Prop necessary, Prop reduction, R1 Prop 2.1, CCIBU, measurable selection |
| Prop 5.2 (diagonal invariance) | PROVED | |
| Blow-up remark | REMARK | |
| CONJECTURE N28 ((E4″) empty) | CONJECTURE | |

**Check first.**
1. *Theorem 3.5 step 4 and Lemma 3.4.* Do the walls supplied by N21.9 really meet **every** segment from the pinned
   set to V_l ∩ Ω? (N21.9(ii) via Lemma M on int conv(O ∪ V_l); refereed in N23 §7.4.) The surround lemma needs only
   that.
2. *Prop 3.1 step 2.* The c-cluster sign needs (TS) at τ₁ on F_i, with both half-discs. The conclusion of Prop 3.1 is
   that (TS) fails at τ₁, so there is no circularity.
3. *Lemma 3.2.* PL is applied to the open set O ∩ B(p\*, ρ), where Γ is taken with respect to two balls chosen in
   different arguments. PL tolerates shrinking the balls.
4. *Lemma 3.3.* Both options of N21.9 are available on (τ_x, τ_y). This is the only new use of N21.9.
5. *Theorem 4.1 step 3.* Lemma 2.3 is applied at d-face points p_m ∈ F(g_m) ∩ Ω for g_m in the Thm B co-null set.
   N21.6 picks g_m from a non-null set, so this is possible.

---

## 8. Files (`n28py/`)

| File | Content | Result |
|---|---|---|
| `checks.py` (1) | T1 crossing gambles (exact at ε = 3/10); LP for Fact 4.0; v_{k\*}·w\*\* > 0 (Fact 4.0′) | relint exact; max{1 − m_b} = 0 at ε ∈ {.05, .3, .6, .9}; min v_{k\*}·w\*\* > 0 |
| (2) | orientation of the b-crossing chords from the (PC) facet maps, x₊ and x₋ | 0/48 violations |
| (3) | identity cap and random diagonal-projective caps on the chord near e_b (ε = 0.2, as in R4 §9) | identity: max(q·w′, q·w) ≥ 2.5e−5 > 0 everywhere; 0 diagonal caps with both ≤ 0 |
| (4) | surround lemma, random configurations | 0/3000 failures at δ/d ≤ 0.1; failures at 0.5 and 0.9 |
| (5) | Prop 3.1 distance estimate | ratio ≤ 0.511 (bound 1) in 20 000 trials |
| (6) | quasi-concavity and vertex-free interiors in a genuine realisation (hexagon gauge mixture, R10a Thm M) | 0/4000 violations; max_K m_b ≤ 0.997 |
| `checks.out` | output | |

All NUMERICS are sanity checks. No proof above depends on them.
