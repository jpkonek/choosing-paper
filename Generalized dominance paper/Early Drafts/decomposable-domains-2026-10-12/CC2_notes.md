# CC2 (round 31, BRIEF23). Target-side design: a corner seed, a layered invariant, and a rigidity theorem that excludes the design

17 Oct 2026. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact finite computation, or a step-by-step reading of a cited result;
- **CONJECTURE**;
- **NUMERICS**: sampling; nothing depends on it.

Scripts: `cc2py/` (run `python3 -I <script>.py` inside it; outputs in `*.out`). No assumption is added. Every extra
hypothesis below is a hypothesis of a stated result and is named where it is used.

**Domain.** Unless stated otherwise, the full four-advice domain 𝓜 (every measurable model is evaluable; (LF) holds
at every target). This is the setting of AUDIT_BB §3 and AUDIT_AA's Task A. The main theorem (§5) is a full-domain
theorem: it uses gambles at "chart infinity" (§1), which the U-domain does not contain.

---

## 0. Outcome

**No full system covering T1 was obtained. The design CC2 was asked to take is excluded by a theorem (§5). The
theorem identifies exactly what a layered construction would have to do instead.**

The brief prescribed a target-side seed at T1's corners, plus a layered invariant: each world is a "core" outside a
region W, plus the seed and its interactions inside W. Five results.

1. **The target-side core (§2; PROVED, CHECKED by script).** Take the rank-weighted Brier field 𝔑_κ. Its penalties
   are 0, λ₁, λ₂, λ₃ times |h_k| for good, silent, bad and contradictory advice, with κ := (λ₂−λ₁)/λ₁. Take
   κ = κ(ε) = (1+2ε)/(1−ε).
   - **What it is.** 𝔑_κ is a successful full system on all of Δ. Its q-Bayes model is D_{R(q)}, where R(q) is the
     density-ratio class of q.
   - **Boundary.** On ∂Δ its selected family is exactly T1's posterior family ν(q⊙T1).
   - **At u.** R(u) is a hexagon containing T1. And D_{T1} ∖ D_{R(u)} is the union of three **corner wedges** Γ_l.
     Γ_l is the cone spanned by a corner ray of D_{T1} and its two adjacent crossing rays.

   So the core agrees with T1 everywhere except on cones that contain exactly the gambles the additive no-go uses:
   the corner rays and the crossings.
2. **The seed (§3; PROVED, CHECKED).**
   - **Single-base lemma (any decomposable domain).** Comparisons out of one base never form a certificate. So a
     target-side seed needs bases that differ from T1 on the seed's support.
   - **An explicit corner seed.** It consists of five comparisons at world 3, out of five coherent models contained
     in D_{T1}, supported on ten small cells inside Γ₃. Σ_k g_k = −1 cell by cell. Every two gains overlap, so in
     isolation the seed is composition-clean: there is no genuine composition (exhaustive closure on the cell
     algebra; proof for the real algebra).
3. **Invariant and extension theorem (§4; PROVED).**
   - **Valued worlds.** World k accepts a record r iff V_k(r) ≥ 0, where V_k is superadditive along composition and
     strictly guiding.
   - **The theorem.** A selection that is strictly p-Bayes for (V_k), coherent and upper semicontinuous gives a
     successful system. Every extension step of the brief is then automatic: competitors, composition, closed
     sections, protection, (C)-ties and unions.
   - **The layered invariant** is the case V_k(r) = ℓ_k(r|W^c) + v_k(r|W). Lemma 4.3: this separable form is not a
     restriction. It is forced as soon as the worlds agree with the core on records supported off W. The value v_k is
     then the **shadow price** of a W-record.
4. **Main result: local rigidity (§5, Theorem 5.6; PROVED).** Assume the following.
   - **(H1)** The worlds agree with a rank-weighted Brier core on every record supported off W.
   - W is bounded in the sign-class charts.
   - **(H3)** Shadow prices of small W-records are small: no vetoes.
   - **(H4)** No non-null part of W is infinitesimal at all three worlds.
   - The edges carry competitive selections with closed sections.

   Then **every model competitive on Ω whose core boundary is somewhere visible off W is a core Bayes model.**
   Whatever the worlds do inside W, they cannot change it.
   - **Corollary 5.7.** If W misses a non-null open piece of one middle arc of one facet of D_{T1}, then T1 is not
     competitive on Ω. Hence T1 ∉ C_L. Every target-side seed placed at the corners, in a W of this kind, is
     therefore excluded, whatever its structure.
   - **Mechanism: an ordinal corner/box contradiction.** On the full domain the edge-selected models are exactly the
     core's strip models (Lemma 5.2), and every edge weight is attained (Lemma 5.3, connectedness). So the two edges
     at e₃ pin the shadow exchange rates at every point h₀ = (x, y) of the sign class Q₃⁺ (Lemma 5.5):
     - a₃ ≤ τ|a₁| and a₃ ≤ σ|a₂|, with τ = 1/(κx) and σ = 1/(κy);
     - at u this gives u·a ≤ a₃(1 − κ(x+y))/3;
     - on Γ₃ we have x + y > 1/κ, so this is < 0 (symbolic check: `geometry.py` (D)).

     So silencing T1's corner-wedge acceptances is profitable in shadow prices. Any exchange off W near T1's boundary
     cashes the profit in, and T1 stops being competitive.
5. **What survives (§6). A layered construction must do one of the following:**
   - **(L1)** let W surround essentially all of ∂D_{T1}, not only the corners, so that no exchange near T1's
     boundary is available off W;
   - **(L2)** give W-records unbounded shadow prices at small scales (vetoes, as in VB, so L3.4 and S21 territory);
   - **(L3)** make a non-null part of W infinitesimal at all three worlds (a lexicographic second level; on M_U,
     S21 excludes the total version);
   - **(L4)** let W reach chart infinity, i.e. the planes where a sign class's odd coordinate vanishes. These are the
     ends of the edge sweeps, where D2-type end devices live;
   - **(L5)** drop the additive core off W altogether.

   The corner seed of item 2 fits none of these, so on its own it is dead. The next target-side question is (L1) or
   (L2) (§6).

**Plain-English status.** I tried to build T1 from an additive system that already agrees with T1 everywhere except
at its three corners, changing the rankings only near the corners. A theorem shows this cannot work, for any change of
that kind with no vetoes. The two edges of the simplex next to each corner fix the "exchange rates" there. Those rates
make T1's corner acceptances a losing trade, and the unchanged region around T1's sides lets every competitor exploit
it. A working construction must change the rankings around the whole boundary of T1, or use vetoes, or exploit the
ends of the edges.

| | Statement | Label |
|---|---|---|
| 2.1 | 𝔑_κ: Bayes models D_{R(q)} (κ ≥ 1); full successful system on Δ | PROVED; CHECKED (`geometry.py` (A)) |
| 2.2 | R(q) = ν(q⊙T1) on ∂Δ for κ = κ(ε); ν(q⊙T1) ⊆ R(q) inside | PROVED; CHECKED ((B)) |
| 2.3 | T1 ⊆ R(u); D_T1 ∖ D_R(u) = Γ₁∪Γ₂∪Γ₃, Γ₃ = cone{r₁₂, w₂₁, w₁₂′} ⊆ cl Q₃⁺; chart formula | PROVED; CHECKED ((C)) |
| 3.1 | single-base lemma (any decomposable domain, ladder encoding) | PROVED |
| 3.2 | explicit corner seed: five coherent bases ⊆ D_T1, ten cells in Γ₃, Σg = −1 | CHECKED (`seed.py`) |
| 3.3 | pairwise overlapping gains ⇒ composition-clean in isolation | PROVED; CHECKED ((v)) |
| 3.4 | no certificate of comparisons each strictly rejected by one fixed positive density at another world | PROVED |
| 4.1 | valued-world extension theorem | PROVED |
| 4.3 | agreement with the core off W ⇒ separable shadow prices | PROVED |
| 5.1–5.5 | off-W Bayes; edge rigidity; edge weights attained; paraboloid exchange lemma; corner chain | PROVED |
| **5.6** | **local rigidity of rank-weighted Brier cores** | **PROVED** |
| **5.7** | **no layered design with chart-bounded W missing a piece of a middle arc has T1 competitive** | **PROVED** |
| 6 | loopholes (L1)–(L5); (L3) total version on M_U is S21 | reading; partly CHECKED |

---

## 1. Setting and notation

- n = 3, ε ∈ (0,1), c₀ = (1−ε)/3, κ(ε) = (1+2ε)/(1−ε) > 1, and T1 = conv{v_k}, v_k = c₀𝟙 + εe_k.
- Records, composition, A_k and the transition lemma are as in X1 §1 (Thm X1.1.1). A world is a set A_k of records
  satisfying the four conditions there (strict (G), (IB) and transitivity are then automatic). This is **(R0)**.
- **Sign half-classes.** For l ∈ {1,2,3}, Q_l⁺ := {h : h_l > 0 > h_j for j ≠ l}. Every mixed pair has exactly one
  orientation in Q⁺ := Q₁⁺ ∪ Q₂⁺ ∪ Q₃⁺, and is indexed by it. Its advice is + (accept h), 0, − (accept −h) or ×.
  Q_l⁺ is the half-class of the sign class Q_l of B1, in which world l has the odd sign.
- **Chart.** On Q₃⁺, χ(h) := (x, y) := (|h₁|/h₃, |h₂|/h₃) ∈ (0,∞)². Q₁⁺ and Q₂⁺ are charted in the same way, by the
  ratios of the two negative coordinates to the positive one. Chart infinity in Q_l⁺ means that h_l is small compared
  with the other coordinates.
- A symmetric measurable set W is **chart-bounded** if χ(W ∩ Q_l⁺) is bounded for each l. A W-record is a record
  supported in W; an off-W record is a record supported in W^c.
- A coherent model D_K accepts h ∈ Q₃⁺ iff χ(h) lies in the open convex down-set {m₃ − m₁x − m₂y > 0 ∀ m ∈ K}. It
  accepts −h iff χ(h) lies in the open convex up-set {m₁x + m₂y − m₃ > 0 ∀ m ∈ K}.
- **Core.** ℓ_k(h, a) := λ_{rk_k(h,a)}|h_k| with 0 = λ₀ < λ₁ < λ₂ < λ₃ (a "rank-weighted Brier" field), and
  κ := (λ₂−λ₁)/λ₁. For a record r, ℓ_k(r) := ∫_{supp r}(ℓ_k(h, y(h)) − ℓ_k(h, x(h))) dμ, where r(h) = (x(h) → y(h)).
  B_q denotes the a.e.-unique q-Bayes model (Thm 2.1).
- On Q₃⁺, write the value of silencing an accepted h, and of moving from silence to −h, as

  g(h) := ℓ(h,0) − ℓ(h,+) = λ₁h₃(−κx, −κy, 1),  g′(h) := ℓ(h,−) − ℓ(h,0) = λ₁h₃(−x, −y, κ).   (1.1)

---

## 2. The target-side core 𝔑_κ

**Theorem 2.1 (PROVED; CHECKED, `geometry.py` (A), 15 937 exact tests, 0 mismatches).** Let κ ≥ 1. For every q ∈ Δ,
the pointwise q-Bayes advice of ℓ is a.e. unique, and it is the advice of D_{R(q)}, where

R(q) := conv{ν(q⊙t) : t ∈ {1,κ}³} = {m ∈ Δ : m_i q_j ≤ κ m_j q_i for all i, j}.

With the selection C_q := B_q the system is successful on all of Δ: strict (G), (IB), (LA), competitiveness on
supp q, closed sections for every model, and (C) with C_L = {B_q}.

*Proof.*
- **Bayes advice.** The q-costs of +, 0, − are λ₂ q·h⁻, λ₁ q·|h| and λ₂ q·h⁺; × costs more than 0.
  - + is optimal iff (λ₂−λ₁) q·h⁻ < λ₁ q·h⁺, that is, q·h⁺ − κ q·h⁻ > 0.
  - Since κ ≥ 1, that condition also gives λ₂q·h⁻ < λ₂q·h⁺.
  - q·h⁺ − κ q·h⁻ = min_{t∈{1,κ}³} (q⊙t)·h, so + is optimal iff P_{R(q)}(h) > 0. The case of − is symmetric.
  - Ties lie on finitely many hyperplane pieces of the sign classes, so they are null for every q.
- **Successful system.** Uniqueness gives undominatedness and (C), as in AUDIT_BB §3. Competitiveness on supp q is
  Bayes optimality. Continuity in measure of q ↦ B_q and dominated convergence give continuous p ↦ ℓ_k(B_p), hence
  closed sections. (C): by Thm kkm every undominated model is tied with a selected B_p, and then it is p-Bayes, hence
  equal to B_p. ∎

**Proposition 2.2 (PROVED; CHECKED (B)).** Let κ = κ(ε).
- On ∂Δ, R(q) = ν(q⊙T1).
- For q ∈ int Δ, ν(q⊙T1) ⊆ R(q), and the inclusion is strict (in the samples, D_{ν(q⊙T1)} is strictly larger).

*Proof.*
- For m ∈ T1 the ratios m_i/m_j lie in [1/κ, κ], with the extremes attained at the vertices: v_{ii}/v_{ij} =
  (c₀+ε)/c₀ = κ.
- So ν(q⊙m) satisfies the ratio constraints of R(q), which gives the inclusion.
- On an edge, say q₃ = 0, both sets are the segment {m₁/m₂ ∈ [q₁/(κq₂), κq₁/q₂], m₃ = 0}, since the ratio m₁/m₂ over
  T1 fills [1/κ, κ]. At vertices both are {e_i}. ∎

So **𝔑_{κ(ε)} realises T1's posterior family on the whole boundary of Δ, Bayes at identity**, and fills the interior
with hexagons.

**Proposition 2.3 (corner wedges; PROVED; CHECKED (C)).** Let κ = κ(ε) and H := R(u).
- **(a) Inclusion.** T1 ⊆ H. The hexagon H = {m : m_i/m_j ≤ κ} has the vertices v_k ∝ (κ,1,1) (cyclically) and
  w₃ ∝ (κ,κ,1), w₁ ∝ (1,κ,κ), w₂ ∝ (κ,1,κ).
- **(b) The wedges.** D_{T1} ∖ cl D_H = Γ₁ ∪ Γ₂ ∪ Γ₃, with Γ₃ := {h ∈ D_{T1} : w₃·h ≤ 0}, and cyclically.
  - Γ₃ is the cone spanned by the corner ray r₁₂ = (−1,−1,κ+1) and the two crossing rays adjacent to it: w₂₁ =
    (−1,0,κ) on F₁ and w′₁₂ = (0,−1,κ) on F₂.
  - So Γ₃ ⊆ cl Q₃⁺, and in the chart

    χ(Γ₃) = {x + y ≥ 1/κ, κ max(x,y) + min(x,y) < 1}.

    This is the triangle with vertices (1/κ,0), (0,1/κ) and (1/(κ+1), 1/(κ+1)), the last being χ(r₁₂).
- **(c) Agreement elsewhere.** Off the three wedges, D_{T1} and D_H agree. In particular they share the middle arcs
  of the three facets of D_{T1}.

*Proof.*
- (a) By 2.2 at q = u, together with the vertex list of R(u).
- (b), the faces. v₁ × w₃ ∝ (1−κ, 0, κ²−κ) ∝ (−1,0,κ) = w₂₁, and v₂ × w₃ ∝ (0,−1,κ).
- (b), the chart. On Q₃⁺ with h = h₃(−x,−y,1), the minimum of m·h over the vertices of H is 1 − κ(x+y), attained at
  w₃. So χ(D_H ∩ Q₃⁺) = {x+y < 1/κ}. T1's conditions read c₀(1−x−y) − εx > 0 and c₀(1−x−y) − εy > 0, i.e.
  κ max + min < 1.
- (c) The other three facets of H are the three facets of D_{T1}, restricted to their middle parts. ∎

*Reading.* The hexagon "cuts T1's corners" exactly along the planes through consecutive crossing rays. Every gamble
the additive contradiction uses lies in the closure of the wedges:
- the corner rays (corner equations);
- the crossing rays (crossing rows, box gambles A ≈ (−1/κ,0⁺,1), B ≈ (1,0⁻,−1/κ); write-up Prop T1).

This agrees with N17 Conj. 5.2's numerics: incoherent shadow Bayes models sit at the corner rays.

---

## 3. The seed

**Lemma 3.1 (single-base lemma; PROVED; any decomposable domain).** Encode comparisons by ladder vectors: at (h, s),
s ∈ {1,2,3}, the record (a → b) contributes +1 if rk(a) < s ≤ rk(b) and −1 if rk(b) < s ≤ rk(a). Then no finite
family of comparisons B ⪯_i X_k out of **one** base B is a certificate.

*Proof.*
- At each (h, s) every δ_k(h,s) lies in {0, σ(h,s)}: σ = +1 if s > rk_i(h, a_B(h)), and −1 otherwise.
- If Σλ_kδ_k ≤ 0, then every positive coordinate vanishes, so every δ_k ≤ 0.
- Strict (G) then gives δ_k = 0. ∎

On M_U this is the observation that a record out of a fixed base has a fixed sign at each point. So a seed out of T1
alone is impossible; a seed needs further bases that differ from T1 on its support. The natural partner of T1 is
D_{R(u)}, and the two differ exactly on the wedges (Prop 2.3).

**Proposition 3.2 (explicit corner seed; CHECKED, `seed.py`; ε = 3/10, κ = 16/7).**
- **Cells.** Ten cell centres P_S, indexed by the 2-subsets S of {0,…,4}, lie on the circle arc of radius 37/100
  about 0. Their angles run from 27° to 63°, and they are exact rational points. All of them lie in the interior of
  χ(Γ₃).
- **Bases.** For k = 0,…,4, put K_k := conv(T1 ∪ N_k). Here N_k consists of the normals of the chords between
  consecutive centres of C_k := {S : k ∈ S}, plus two end cuts of slopes −κ and −1/κ, all pushed out by the factor
  1 + 10⁻⁵.
  - B_k := D_{K_k} is coherent, and B_k ⊆ D_{T1}.
  - The trace of B_k on the ten centres is exactly C_k. The minimal margin is 2·10⁻⁶, so cells of chart radius below
    5·10⁻⁷ have the same trace.
  - The cut normals are *not* inside R(u), so the B_k are not sandwiched between D_{R(u)} and D_{T1}.
- **Comparisons.** At world 3, B_k ⪯₃ X_k, where X_k is B_k with the four C_k-cells silenced and the six other cells
  accepted. In Q₃⁺ silencing is bad and accepting is good at world 3, so the world-3 error vector is g_k = +1 on C_k
  and −1 on the other six cells.
- **Certificate.** Σ_k g_k = −1 on every cell (each cell lies in exactly two C_k).

**Lemma 3.3 (PROVED; CHECKED (v)).** If the positive parts of g₁,…,g_m pairwise overlap on non-null sets, then the
composition closure of {g_k} ∪ {all δ ≥ 0} contains no nonzero δ ≤ 0. In particular the seed of 3.2 is clean in
isolation: no genuine composition closes it.

*Proof.*
- A ternary sum g_k + e with e ≥ 0 keeps g_k's positive part, since e must vanish there.
- A further g_l cannot be added, because the positive parts would add to 2 on g_k⁺ ∩ g_l⁺.
- So the closure consists of the nonnegative vectors and the vectors g_k + e. None of these is nonpositive and
  nonzero. ∎

(`seed.py` (v) computes the closure on the ten-cell algebra exhaustively: 4169 vectors, none nonzero and nonpositive.)

**Lemma 3.4 (PROVED).** Let ρ > 0 be integrable. No world-3 certificate Σλ_kδ_k ≤ 0, ≠ 0 (δ_k = 1_{E₃X_k} −
1_{E₃B_k}, supported in Q₃) consists of comparisons in each of which X_k is strictly ρ-better than B_k at world 1,
i.e. ρ(E₁X_k) < ρ(E₁B_k) for every k.

*Proof.* On Q₃ the world-1 error change of a record is the negative of its world-3 change (Q₃ ⊆ R₁₃).
- So ρ(E₁X_k) < ρ(E₁B_k) means ∫δ_kρ > 0.
- Integrating the certificate against ρ gives Σλ_k∫δ_kρ ≤ 0, a contradiction. ∎

So the seed's comparisons can be "needed" only if worlds 1 and 2 are themselves non-additive on the seed's region.
This is the K2.2/BB1 message in its simplest form.

---

## 4. The invariant and the extension theorem

**Definition 4.0 (valued worlds).** A *valuation* at world k is a map V_k from realizable records to [−∞, ∞) with:
- (V0) V_k(ι) = 0;
- (V1) V_k(r∘s) ≥ V_k(r) + V_k(s) for composable r, s;
- (V2) V_k(r) ≥ 0 for k-worsening r, and V_k(r) < 0 for nontrivial k-improving r.

Put A_k := {V_k ≥ 0}. Then A_k is a world (transition lemma): (V0) gives identity, (V1) composition, and (V2) weak and
strict (G). Conversely every world arises this way, with V_k = 0 on A_k and −∞ off it.

**Theorem 4.1 (valued-world extension theorem; PROVED).** Let V = (V_k) be valuations, and let p ↦ C_p be a coherent
selection on Δ such that:
- **(B)** C_p is *strictly p-Bayes*: for all X ≠ C_p, Σ_{k∈supp p} p_k V_k(rec(C_p,X)) > 0, all terms finite;
- **(U)** p ↦ V_k(rec(C_p,X)) is upper semicontinuous on Δ, for every k and X.

Then the system is successful: strict (G), (IB), (LA), competitiveness on supp p, closed sections for every model,
undominatedness, and (C) with C_L = {C_p}.

*Proof.*
- **Competitiveness.** If V_k(rec(C_p,X)) < 0 for every k ∈ supp p, the p-weighted sum is negative.
- **Undominatedness and no ties.** Suppose X ⪯_k C_p at every k. By (V1), V_k(rec(C_p,X)) ≤ V_k(ι) −
  V_k(rec(X,C_p)) ≤ 0. If X ≠ C_p this contradicts (B).
- **Closed sections.** {p : V_k(rec(C_p,X)) ≥ 0} is closed by (U).
- **(C).** By Thm kkm every undominated model is tied at every world with some C_p, hence equals it. ∎

*How this answers the brief's request for an invariant.*
- The invariant is (V0)–(V2) + (B) + (U). Each is checkable independently, and none restates finite
  satisfiability.
- Every extension step is automatic:
  - competitors are handled by (B);
  - composition by (V1);
  - closed sections by (U);
  - protection and (C)-ties by strictness in (B);
  - unions do not arise.
- Additive fields with a.e.-unique coherent Bayes models (CCIBU, Thm 2.1) are the case V_k = ℓ_k.
- The brief's **layered invariant** is

  V_k(r) = ℓ_k(r|W^c) + v_k(r|W),   (4.2)

  where the core ℓ acts off W and a superadditive v_k acts on W-records (the seed and its interactions).

**Lemma 4.3 (shadow prices; PROVED).** Let worlds satisfy (R0) and **(H1)**: for every off-W record o,
o ∈ A_k ⟺ ℓ_k(o) ≥ 0. For a W-record w and an off-W region Z, put

θ_k(w | Z) := inf{ℓ_k(o) : o off-W record supported in Z, w∘o ∈ A_k}.

Then:
- (a) ℓ_k(o) < θ_k(w|Z) ⇒ w∘o ∉ A_k. This is the definition.
- (b) If Z ∩ Z′ = ∅, then θ_k(w|Z) + θ_k(w⁻¹|Z′) ≥ 0.
- (c) If Z, Z′ are disjoint and *rich* (the ℓ_k-values of records supported in each fill [−m, m]), and |θ_k(w|Z)| <
  m, then θ_k(w|Z′) = θ_k(w|Z). So small shadow prices are intrinsic; write θ_k(w).
- (d) If w is strictly k-improving, θ_k(w) ≥ 0. If w is k-worsening, θ_k(w) ≤ 0.

*Proof.*
- (b) Take w∘o ∈ A_k (o in Z) and w⁻¹∘o′ ∈ A_k (o′ in Z′). These are composable: they match on supp w and are
  disjoint elsewhere. The composite is the off-W record o ∪ o′, so ℓ_k(o) + ℓ_k(o′) ≥ 0 by (H1).
- (c) Let w∘o ∈ A_k with o in Z and ℓ_k(o) = t. Let o′ be in Z′ with ℓ_k(o′) ≥ t.
  - o⁻¹∘o′ is an off-W record of value ≥ 0, so it lies in A_k.
  - (w∘o)∘(o⁻¹∘o′) = w∘o′ is composable, since the supports of o, o′ are disjoint.
  - Hence θ(w|Z′) ≤ t. The reverse inequality is symmetric.
- (d) Suppose w is strictly k-improving and w∘o ∈ A_k with ℓ_k(o) < 0. Then o⁻¹ ∈ A_k, and (w∘o)∘o⁻¹ = w ∈ A_k,
  contradicting strict (G). The second clause is weak (G) with o = ι. ∎

*Consequence.* Under (H1), the acceptance of w∘o is determined by ℓ(o) and the threshold vector θ(w), up to the
boundary value. So (4.2) is not an extra restriction on layered designs: it is forced, with v_k = −θ_k.

---

## 5. The incompatibility: local rigidity of the core

**Standing hypotheses of §5.**
- (R0); a rank-weighted Brier core with κ > 1; W symmetric and chart-bounded; (H1).
- **(H3) (no vetoes).** There is ω(δ) → 0 such that, for every W-record w with μ(supp w) < δ and every off-W record
  o: ℓ_k(o) ≥ ω(δ) ⇒ w∘o ∈ A_k, and ℓ_k(o) ≤ −ω(δ) ⇒ w∘o ∉ A_k.
- **(H4) (no infinitesimal sets).** For every non-null B ⊆ W ∩ Q_l⁺ and every pair α ≠ β of neighbouring advices
  ({+,0} or {0,−}), the record "α → β on B" has θ(w) ≠ (0,0,0).
- **(S∂).** Each edge [e_i,e_j] carries selected models competitive on their supports, with closed sections at worlds
  i and j. Each vertex carries the world-best model.

**Lemma 5.1 (off-W Bayes; PROVED).** If C is competitive on S ⊆ Ω, there is q ∈ Δ with supp q ⊆ S and C = B_q a.e.
off W.

*Proof.*
- The values ℓ(rec(C,X)), for X agreeing with C on W, form a convex set (Lyapunov–Aumann; the envelope λ₃|h| is
  integrable).
- By (H1) and competitiveness, this set misses {z_k < 0 ∀ k ∈ S}.
- Separation gives q ≥ 0, supported in S, nonnegative on the set. So C's advice is pointwise q-optimal a.e. off W.
- Uniqueness (Thm 2.1) gives C = B_q off W. ∎

**Lemma 5.2 (edge rigidity; PROVED).** Let q ∈ ∂Δ, and let D_K be coherent with D_K = B_q a.e. off W (W
chart-bounded). Then D_K = B_q. In particular every edge-selected model equals a core edge or vertex model, by
Lemma 5.1.

*Proof.* Say q₂ = 0.
- **Interior edge weight.** If q is interior to the edge [e₁,e₃], then B_q accepts h ∈ Q₃⁺ iff x < c := q₃/(κq₁),
  for **every** y.
  - Off W this includes points with y arbitrarily large.
  - Open sets that agree a.e. agree up to closure, so m₃ − m₁x − m₂y ≥ 0 for all m ∈ K, all x < c and all large y.
  - Hence m₂ = 0, and K lies on the edge face.
  - A credal set on that face is determined by its interval of ratios m₃/m₁. That interval can be read off the
    strips {x < min m₃/m₁} (accept h) and {x > max m₃/m₁} (accept −h) at large y, so it equals B_q's interval.
- **Vertex weight.** If q = e₁, B_q accepts h ∈ Q₁⁺ at every chart point. Any m ∈ K with m₂ > 0 or m₃ > 0 makes D_K
  reject h at chart infinity of Q₁⁺, which lies off W. So K = {e₁}. ∎

**Lemma 5.3 (all edge weights are attained; PROVED).** On each edge, every weight q* is the core weight of some
selected model.

*Proof.* Take the edge [e₁,e₃], and write E_t = B_{q(t)} (Lemma 5.2).
- **Monotonicity.** The core edge family is pointwise monotone. On R₁₃ the advice moves along good₁ → silent → good₃
  as q₁/q₃ decreases (single crossing of affine costs); elsewhere it is constant.
- **Test model.** Suppose q* is not attained, and let Y := B_{q*}.
  - S₁ := {t : E_t ⪯₁ Y} is exactly {t : q(t) on the e₁-side of q*}, by weak and strict (G).
  - S₃ := {t : E_t ⪯₃ Y} is exactly {t : q(t) on the e₃-side of q*}.
- **Contradiction.** By (S∂) both sets are closed. They are disjoint, they cover the edge, and they are nonempty (the
  vertices). This contradicts connectedness. ∎

**Lemma 5.4 (paraboloid exchange lemma; PROVED).** Let S ⊆ Ω with |S| ≥ 2 and q ∈ relint face(S). Let C be a model,
and Z ⊆ W^c an open set with C = B_q a.e. on Z. Suppose Z meets the accept/silent (or silent/−) boundary surface Σ of
B_q in one sign class, off the coordinate planes, and the values g_S (or g′_S) on Σ ∩ Z span q^⊥ ∩ ℝ^S. Let
O := {ℓ_S(o) : o a record out of C supported in Z}. Then there are K, r₀ > 0 with

O ⊇ {z ∈ ℝ^S : q·z ≥ K|z|², |z| ≤ r₀}.

*Proof.*
- **Convexity.** O is convex and contains 0 (Lyapunov).
- **Shells.** On a sign class, g is linear and φ := q·g is linear with nonzero gradient. Pick σ₁, σ₂ ∈ Σ∩Z with
  independent g_⊥(σ_i), where ⊥ denotes projection onto q^⊥; one point suffices if |S| = 2.
  - Silencing the inner shell N_i ∩ {0 < φ < t}, or accepting the outer shell N_i ∩ {−t < φ < 0}, has value ±m(t)
    g(σ_i)(1+O(η)).
  - Its q-component is O(t·m(t)) = O(m(t)²), since m(t) ≍ t (coarea formula; bounded Gaussian density).
  - This gives four curves in O, with ⊥-parts near ±g_⊥(σ_i) and q·z ≤ K₀|z|².
- **Disc.** At each small scale the convex hull of their ⊥-parts contains a disc of comparable radius, so every small
  z_⊥ is attained with q·z ≤ K₁|z_⊥|².
- **Lifting.** Mixing two opposite shells gives a point (0, s₀) ∈ O with s₀ > 0. Convex combinations with it fill
  K₁|z_⊥|² ≤ q·z ≤ s₀/2 at fixed z_⊥, by the intermediate value theorem.
- For small z, q·z ≥ K|z|² implies q·z ≥ K|z_⊥|². ∎

**Lemma 5.5 (corner chain; PROVED).** Assume the standing hypotheses. Let C be competitive on Ω with C = B_q off W,
q ∈ int Δ, and let Lemma 5.4 apply to (C, q) on an off-W region Z_C. Let h₀ ∈ W ∩ Q₃⁺ be a density point of
{C = α}, where the core's advice at h₀ is strictly q-better than α. Then a contradiction follows.

*Proof*, for α = + with the core strictly preferring 0 at h₀, i.e. q·g(h₀) < 0 ⟺ κ(q₁x₀ + q₂y₀) > q₃. By discrete
convexity of the costs along + ~ 0 ~ − when κ ≥ 1, the only other cases are (0→+), (0→−) and (−→0); see the end of
the proof.

1. **Edge models.** By Lemma 5.3 choose a selected E = B_{q^E} on [e₁,e₃] with strip position c_E ∈ (x₀(1−η), x₀),
   and F = B_{q^F} on [e₂,e₃] with c_F ∈ (y₀(1−η), y₀). Then τ := q^E₁/q^E₃ = 1/(κc_E) and σ := q^F₂/q^F₃ =
   1/(κc_F).
   - For a small chart ball B around h₀, E and F are silent on B, since c < x < κ²c.
   - Let B′ := B ∩ {C = +}, which is non-null.
   - Order of choices: first η (so that the bracket in step 6 exceeds δ₀/2 for small ε₁), then E and F, which fixes
     τ, σ, K_E, K_F; then B small enough for the smallness used in steps 4–6. The constants K and C_q for C are fixed
     by Z_C.
2. **Records.** Put w := (+→0) on B′, w′ := w⁻¹, a := −θ(w), b^E := −θ(w′) = b^F.
   - Choose disjoint rich exchange regions:
     - Z_C near Σ off W, from Lemma 5.4;
     - Z_E near E's strip boundary at large y in Q₃⁺;
     - Z_F near F's strip boundary at large x in Q₃⁺.

     Lemma 5.4 applies to E and F on Z_E and Z_F (|S| = 2), because g restricted to {1,3} is constant in direction
     along x = c, and nonzero.
   - By (H3), |a|, |b| ≤ ω(μ(B)) → 0 as B shrinks.
3. **Signs.** By Lemma 4.3(d): a₁, a₂ ≤ 0 ≤ a₃ and b₁, b₂ ≥ 0 ≥ b₃.
4. **C-step.** If q·(−a) > K|a|², Lemma 5.4 gives a record o out of C in Z_C with ℓ(o) < −a in every coordinate.
   Then X := C∘w∘o is rejected at all three worlds, by Lemma 4.3(a). Hence

   q₃a₃ ≥ q₁|a₁| + q₂|a₂| − K|a|².   (5.1)

5. **E-step.** In the same way, q^E₃|b₃| ≤ q^E₁b₁ + K_E|b|². By Lemma 4.3(b), b ≤ −a, so b₁ ≤ |a₁| and |b₃| ≥ a₃.
   For |b| small this gives a₃ ≤ τ(1+ε₁)|a₁|, with ε₁ → 0 as |b| → 0. Likewise a₃ ≤ σ(1+ε₁)|a₂|.
6. **Algebra.** Insert into (5.1):

   [κ(q₁c_E + q₂c_F)/(1+ε₁) − q₃]·a₃ ≤ K|a|².

   - The bracket tends to δ₀ := κ(q₁x₀ + q₂y₀) − q₃ > 0.
   - From (5.1), |a| ≤ 2C_q a₃ once |a| is small.
   - So δ₀a₃/2 ≤ 2KC_q a₃|a|, which forces a₃ = 0, hence a = 0.
   - This contradicts (H4) for B′.

*Other cases.* Each is the same computation with the edge model chosen to carry the end advice β of w on B, and with
g replaced as listed.
- (0→+) (core strictly prefers +): E accepts on B, with c_E slightly above x₀.
- (0→−) and (−→0): use g′ and the −h strips {x > κq₃/q₁}, with τ′ = q^E₁/q^E₃ = κ/c′_E.
- The contradiction condition is in each case exactly the core's strict preference at h₀. ∎

**Theorem 5.6 (local rigidity; PROVED).** Under the standing hypotheses of §5, let C be competitive on Ω, and let q
be its off-W weight (Lemma 5.1).
- (a) If q ∈ ∂Δ, then C = B_q (Lemma 5.2).
- (b) If q ∈ int Δ and W^c contains, up to a null set, an open set meeting the accept/silent or silent/− boundary of
  B_q in some sign class off the coordinate planes, then C = B_q a.e.

So the only models competitive on Ω, in particular every member of C_L, are core Bayes models.

*Proof of (b).* Fix a sign class Q_l⁺; for l = 1, 2 use the two edges at e_l.
- Lemma 5.4 applies at (C, q): g is linear and injective on the class, so the values over any open piece of the
  boundary plane fill an open cone in q^⊥, and ± give a spanning set.
- If C ≠ B_q on a non-null part of W ∩ Q_l⁺, then a.e. point of the difference set (ties are null) is a density point
  as in Lemma 5.5, which yields a contradiction.
- On unanimous pairs, any model competitive on Ω gives the correct advice, and so does B_q. ∎

**Corollary 5.7 (T1; PROVED).** Assume (R0), (H1) for some rank-weighted Brier core (any κ), (H3), (H4) and (S∂),
with W chart-bounded and W^c containing, up to a null set, an open set G meeting the relative interior of the middle
arc of some facet F_k of D_{T1}. Then T1 is not competitive on Ω. Hence T1 ∉ C_L for any such ranking with (LA)
and (S).

*Proof.*
- **Off-W weight.** By Lemma 5.1, T1 = B_q off W for some q ∈ Δ. (Lemma 5.1 uses only (R0), (H1) and a.e.
  uniqueness of the core's Bayes advice, which holds for every κ.)
- **κ ≤ 1.** Then every B_q is precise (D_q): it is silent only on a null set. But T1 is silent on the outer side of
  F_k inside G, a non-null set off W. Contradiction. From here on κ > 1.
- **q is interior.** If q ∈ ∂Δ, Lemma 5.2 makes T1 an edge or vertex model, which it is not. So q is interior.
- **Matching facet.** On G, T1 accepts on one side of F_k and is silent on the other. So B_q's accept/silent boundary
  contains an open piece of F_k. In the class of the middle arc that boundary is the plane (κq_k, q_j, q_l)·h = 0.
  Matching v_k ∝ (κ(ε),1,1) gives q_j = q_l and κq_k/q_j = κ(ε).
- **Rigidity.** Theorem 5.6(b) applies with this G, and gives T1 = D_{R_κ(q)} a.e.
- **Contradiction.** R_κ(q) with κ > 1 and q interior is a hexagon. Its cone has six facets, while D_{T1} has three.
  (For κ = κ(ε), q = u, they differ exactly on the wedges, Prop 2.3.) ∎

*Remarks.*
- The proof never uses (C), protection, or any property of the orders inside W beyond (H3), (H4) and transitivity.
  So the seed's structure, the seed itself and any composition rule on W are irrelevant to the exclusion.
- The edges enter only through Lemmas 5.2–5.3. That is, edge-selected models are pinned by gambles at chart
  infinity, where the core is untouched.

---

## 6. What survives, aimed at T1

Lemma 5.5 has an informative form that does not need the C-step. For B ⊆ Γ₃ and w = silence B, the two edges at e₃
force:

a₃ ≤ |a₁|/(κx₀) and a₃ ≤ |a₂|/(κy₀),  so  u·a ≤ a₃(1 − κ(x₀+y₀))/3 < 0.

That is, **in shadow prices, T1's corner-wedge acceptances are always a losing trade at u.** T1 survives only if no
competitor can cash this in. The routes out are exactly the following.

- **(L1) Stiff exchange medium.** W contains, up to null sets, a neighbourhood of *every* point of ∂D_{T1}, so that
  every off-W toggle out of T1 costs a fixed positive multiple of its size in u-value.
  - Then (5.1) holds only with a linear error.
  - Heuristically, T1 then survives at points of Γ₃ where κ(x+y) − 1 is below a multiple of the stiffness constant.
  - This requires a modification surrounding the whole boundary of T1, not a corner seed.
  - Status: open. Interior selected models whose off-W core boundary escapes W are rigid (Thm 5.6), so the selection
    must stay inside the "free" index set {q : ∂B_q ∩ W^c null} and glue to rigid models across its boundary with
    closed sections. That gluing is the precise next problem.
- **(L2) Vetoes.** (H3) fails: some small W-records have unbounded shadow prices. VB (L3 Thm L3.3) is of this type
  and fails exactly at boundary priors; Thm L3.4 and Thm S21 kill lexicographic refinements of a veto paid at a
  vertex.
  - Status: non-lexicographic vetoes are open. One sketch (unproved, not used): at an edge, a model that pays two
    worlds' vetoes is dominated (silence a little of each). So veto-type absorption forces each edge selection to
    pass through models paying neither veto, and then L3.4's mechanism reappears.
- **(L3) Infinitesimal sets.** (H4) fails. If all of W is infinitesimal at all worlds, the core-off-W charge is a
  nonzero leading charge vanishing on W.
  - On M_U this contradicts Thm S21. On the full domain I have not checked S21's transfer.
  - Partial infinitesimality is open.
- **(L4) Ends.** W is not chart-bounded: it reaches the planes where the odd coordinate of a sign class vanishes.
  - Lemma 5.2 then fails, and edge models can bend at chart infinity.
  - These are the ends of the edge sweeps, where D2/F-type end devices live (write-up §8.6(e)–(f)). So a non-veto
    layered design for T1 needs ends in at least one sign class, against the brief's preference.
- **(L5) No additive core off W.** For example, all three worlds are non-additive everywhere, as the brief's item 1
  suggests. Theorem 5.6 says nothing there.

**Recommendation.** The corner seed should not be pursued as a local decoration of any rank-weighted Brier core.
Theorem 5.6 makes every such decoration inert. Two target-side questions remain sharp.
1. **(L1) gluing.** Is there a valuation on a neighbourhood W of all of ∂D_{T1}, with T1 strictly u-Bayes and with
   closed sections across the boundary of the free index set?
2. **(L2) at an edge.** Can a non-lexicographic veto at world 3 on Γ₃ be paid continuously along [e₁,e₃] and
   [e₂,e₃]? L3.4's (Imp) must fail at every paying edge model, so the paying models would have to be
   "veto-saturated". Lemma 5.2's chart-infinity rigidity suggests not, but this is not proved.

---

## 7. Status table

| Item | Statement | Label |
|---|---|---|
| Thm 2.1 | rank-weighted Brier core: Bayes model D_{R(q)} (κ ≥ 1), successful system on Δ | PROVED; CHECKED |
| Prop 2.2 | boundary family = T1's posterior (κ = κ(ε)) | PROVED; CHECKED |
| Prop 2.3 | hexagon H ⊇ T1; corner wedges Γ_l = cone(corner ray, two crossing rays); chart formula | PROVED; CHECKED |
| Lemma 3.1 | single-base lemma (any decomposable domain) | PROVED |
| Prop 3.2 | explicit five-base corner seed in Γ₃ | CHECKED |
| Lemma 3.3 | pairwise-overlapping gains ⇒ clean in isolation | PROVED; CHECKED |
| Lemma 3.4 | no certificate of comparisons strictly rejected by a fixed density at another world | PROVED |
| Thm 4.1 | valued-world extension theorem | PROVED |
| Lemma 4.3 | (H1) ⇒ separable shadow prices, intrinsic for small values | PROVED |
| Lemmas 5.1–5.5 | off-W Bayes; edge rigidity; attained edge weights; paraboloid; corner chain | PROVED |
| **Thm 5.6** | **local rigidity: Ω-competitive ⇒ core Bayes model** | **PROVED** |
| **Cor 5.7** | **T1 excluded for chart-bounded W missing a piece of one middle arc** | **PROVED** |
| §6 (L1)–(L5) | surviving routes | (L3) on M_U by S21 (CHECKED reading); rest open |
| two-veto sketch | veto-paying edge models are dominated | sketch only, unproved |

## 8. Files (`cc2py/`)

- `geometry.py`, `geometry.out`: Thm 2.1, Props 2.2–2.3 (exact rationals, ε ∈ {1/10, 3/10, 1/2, 4/5}), and the
  symbolic identity (1/(κx)−1)(1/(κy)−1) − 1 = −(κx+κy−1)/(κ²xy).
- `seed.py`, `seed.out`: Prop 3.2 and Lemma 3.3 (exhaustive closure).
