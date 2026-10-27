# BB2. Proposition M3.9 in full: (TS), (PC), (NS) for non-degenerate (γ)-fields on every (LF) decomposable domain, exceptional chords allowed to accumulate

17 Oct 2026, round 30 (BRIEF22, Task B; BRIEF13 rules). Labels:
- **PROVED**: full proof written here, from results that the write-up or refereed notes mark proved, each named;
- **CHECKED**: a step-by-step reading, not a re-derivation;
- **CONJECTURE**;
- **NUMERICS**: `bb2py/`, run `python3 -I bb2_checks.py` inside it. No proof rests on it.

No assumption is added. Notation follows the write-up (§§2, 4, 5, 7.7), M3 §§1, 5–6, D1 §1 and Q4 §1:
- T = T1 with ε ∈ (0,1), n = 3, Ω = int Δ (relative interior in aff Δ);
- for a credal set K, P_K(g) = min_{m∈K} m·g and D_K = {P_K > 0} ∪ {g ≥ 0, g ≠ 0};
- "pair" means {g, −g}, "orientation" means one of g, −g, and "accept g" is the advice that accepts g only.

---

## 0. Outcome

**M3.9 is PROVED, with no gap left, under exactly the hypotheses of the reduction. That includes fields whose
exceptional chords accumulate at p\*, or are dense. (Av) is not used. GAP (ii) of M23_referee is closed, and the
checklist items (i) and (iii) are re-derived rather than read.** No counterexample exists to construct.

> **Theorem 6.1 (= M3.9; PROVED).** Let ψ be a strictly guiding additive field with measurable penalties on a
> decomposable domain 𝓜 with (LF) at D_{T1}. Assume that for a.e. q ∈ Ω the q-Bayes model is a.e. unique and
> coherent ((γ)). Assume also that D_{T1} is the a.e.-unique ψ-Bayes model at some p\* ∈ Ω. Then:
> - (TS) holds on every facet at every τ ∈ (0,1);
> - every conclusion of Thm TS holds on a ball B around p\* for the strict-Bayes family K♭, equivalently for K_q at
>   q ∉ E. These conclusions are: pivot chords with thin zero sets, the strictly monotone continuous chord map,
>   crossing values, no sliding, Lemma rotation, Props regularity and blow-up, (PC) with rank-2 Γ_k, (NS), crossing
>   rows, and the facet data x ∈ {x₊, x₋};
> - the cluster clause holds in vector form (Lemma veccluster).
>
> Hence (C2) and (C3) of M3 §6 hold. Integrability, (γ₀) at boundary weights and (Av) are not used.

**How the three risky transfers are closed.**

| Flagged risk (M3 §6, M23_referee §6.10, Q24_referee §2.4) | Where | Status |
|---|---|---|
| (i) the local chain with chords accumulating at p\*: every use of K is through near-facet levels | §§2.5–2.6 and §3. The chain runs on the lower semicontinuous family P♭ = P_{K♭}, which is exactly quasi-linear on B (Lemma 2.6). Thin zero sets hold at **every** point of B, points of E included (Lemma 3.3). Continuity is used only at anchors chosen off E (Prop 3.1(P5), (P6)) | PROVED |
| (ii) Thm PL with approximate walls and generic segment endpoints | §4. The approximate walls are replaced by the **closed cluster walls** Ẑ_v (Def 4.0). The proof runs on **one** generic segment: two "first points" and a sign-pattern lemma, with no second endpoint A and no nearest point (Thm 4.2) | PROVED |
| (iii) R23.1 for K♭ with chords in the ball | Lemma 4.3. The dichotomy α♭/β♭ is proved clopen directly with K♭, using exact half-plane charts in B | PROVED |
| walls crossing chords (D1.6) | Lemma 4.1, re-derived with the D1_referee open-chart repair | PROVED |
| the chainchords audit transfer | not used as a black box. Its local items are re-derived in §3, and its global item (nopin) is replaced by (TS), as in N21.4 | PROVED |

**Consequence for the premise "every cover of T1 needs a world that does not add up" (Q4.2 / M3.10 / M3.10′).**

| Domain | Status of the premise after BB2 |
|---|---|
| M_U | holds, by Thm M0closed(b) [R2], independently of BB2 |
| (Av)-domains, e.g. every domain two-sided near ∂D_{T1} | holds: **M3.10 and M3.10′ are PROVED.** The inputs are M3.1, M3.4, M3.5, M3.6–M3.8 and D1, each refereed once (R1), plus this note (unrefereed, one reading) |
| every decomposable domain with (LF) | holds: **Q4.2 is PROVED**, at the same status plus Q4.1 and Q4.3 [R1, Q24_referee] |

In each case the stronger statement holds: every endorser tuple of a ranking with (NC) at every world has a degenerate
(ladder-blind) field. The open branches of R21 Part B are therefore (GS), (GL) and (GnAv-d) only. Branches (G0) and
(GnAv-nd) are closed at PROVED status, no longer [CH].

**Corrections to the record found on the way** (none affects a conclusion; §8):
1. M3.6(c) as stated needs silence in the advice range. On the cone over N₀ outside N it can be missing, and then
   accepting is strictly optimal on all of B. The fix is harmless and is made in Lemma 2.5(c).
2. M3 §6's reading of Lemma 3.2 says that in case Q ∈ E, "D1.6 case (B) gives v′ in both one-sided limits". That is
   not the mechanism. The contradiction is the pattern Lemma 2.8(a): a limit {v} next to a limit containing v′ differs
   on an open cone that meets two non-opposite orthants.
3. "Every line through p\* meets E in a countable set" is false globally on two-sided domains. An atom whose ties are
   realised only far from p\* can have its line through p\*. It is true inside B (Lemma 2.6(b)), and that is all that
   is used.

| | Statement | Label |
|---|---|---|
| 2.1 | tie anatomy: E ⊆ ∪ atom lines ∪ countable set; generic points; one-sided limits; patterns ±σ′ | PROVED |
| 2.2 | families K^δ, K♭: coherent at every q; K♭ maximal and upper semicontinuous; continuity off E; quasi-concavity for every g | PROVED |
| 2.3 | exact charts for good gambles, for K♭ at every q | PROVED |
| 2.4 | vertex continuity and UVN for every family, with no (Av) | PROVED |
| 2.5 | local one-sidedness (M3.6), with the silence caveat | PROVED |
| 2.6 | the ball B: exact quasi-linearity of P♭; E ∩ B is a union of frozen near-facet chords and a countable set; lines through p\* meet E ∩ B countably | PROVED |
| 2.7 | wedges, Lemma D for credal sets, chart convexity | PROVED |
| 2.8 | pattern lemmas | PROVED; NUMERICS |
| 3.2 | Theorem TS for (γ)-fields (the local chain under (TS)) | PROVED (analytic lemmas of write-up §4 imported, R2) |
| 3.4 | crossing rows, corner equation, x ∈ {x₊, x₋}, vector cluster clause | PROVED |
| 4.1 | Lemma M across chords at first points of generic segments | PROVED |
| 4.2 | Theorem PL across chords (GAP (ii)) | PROVED |
| 4.3 | R23.1 for K♭ with chords in the ball (checklist (iii)) | PROVED |
| 5.1–5.7 | R23.2, N21.9, N28 Prop 3.1, Lemmas 3.2–3.4, Thm 3.5 for (γ)-fields | PROVED |
| 6.1 | M3.9 | PROVED |
| 7.1 | M3.10, M3.10′, Q4.2 upgraded from [CH] | PROVED at the stated input status |

---

## 1. Hypotheses, notation, imports

**Standing hypotheses (H).** These are exactly M3 §5's standing data, which M3.10 and Q4.2 hand to M3.9. In M3.10 and
Q4.2 they hold for ψ = ψ^ν, a non-degenerate fixed-point field: (γ₀) is M3.4.2, strict guidance is non-degeneracy, and
p\* ∉ E is Theorem D1.
- **(H1)** 𝓜 is a decomposable domain with advice range A(g) (Remark advicerange). (LF) holds at D_{T1} with an open
  N ⊇ ∂D_{T1} ∖ 0. For a.e. pair with an orientation h ∈ N, the advice range contains "accept h" and silence.
- **(H2)** ψ has measurable penalties ℓ_k(g, a), a ∈ A(g), with env(g) := max_{k,a} |ℓ_k(g,a)| < ∞ a.e.
  - It is **strictly guiding**: for a.e. g and every k, ℓ_k(g,·) is strictly increasing in world-k rank on A(g),
    with × strictly last.
  - Bayes models are pointwise minimisers (R1 Lemma 1.2).
  - Integrability is never used below.
- **(H3)** (γ): for a.e. q ∈ Ω the q-Bayes model is a.e. unique and coherent.
- **(H4)** D_{T1} is the a.e.-unique ψ-Bayes model at p\* ∈ Ω.

**Tie vectors.** For a mixed orientation g whose advice range contains the relevant advices, put:
- c(g) := ℓ(silence) − ℓ(accept g);
- c′(g) := ℓ(silence) − ℓ(accept −g) = c(−g);
- d(g) := c(g) − c′(g) = ℓ(accept −g) − ℓ(accept g).

By (H2), c(g) and d(g) have the strict sign pattern σ(g), and c′(g) has the pattern −σ(g). The check: at a world with
g_k > 0 the order is accept g ≺ silence ≺ accept −g. The same holds within any two-element advice range. A tie vector
therefore has mixed strict signs, is not in ℝ𝟙, and its zero line in aff Δ meets Ω and misses the vertices.

**Charts.** R(g) := {q ∈ aff Δ : accepting g is the unique minimiser of q·ℓ(g,·) over A(g)}. It is a finite
intersection of open half-planes, so it is open and convex (R1 Prop 2.1). Unanimous pairs are never tied, because the
correct advice is strictly best at every world.

**Facet data.** These are as in write-up §§2.3, 4.1, 5:
- the facets F_k, corner rays r_kj, crossings w_ck (coordinate c vanishes on relint F_k);
- h^k(τ) = (1 − τ)r + τr′ on F_k, between the normalised corner rays;
- the compact set Σ of facet segments, crossings and limit witnesses;
- the compact collar N₀ = {dist(·, Σ) ≤ η} ⊆ N, with a compact K″ ⊆ int T1 and P_{K″} > 0 on N₀;
- the level bound c̄ < η/√3 (N1).

Put **𝒞 := ℝ₊·int N₀**, an open cone that contains ∂D_{T1} ∖ 0. P_{K″} > 0 on 𝒞 by homogeneity.

**Lemma signs** (write-up Lemma 4.1, R2). On F_k ∖ 0, h_k < 0. On F_k the other two coordinates i, j cross once each,
at τ_i < τ_j, with patterns (h_i, h_j) = (−,+), (+,+), (+,−) on the three arcs.

**Imports, used as stated** (statuses from the write-up and the referee reports):
- [I1] **Remark advicerange.** Every measurable selection of A is a model of 𝓜.
- [I2] **R1 Prop 3.1.** K ↦ 1_{D_K} is a homeomorphism from credal sets (Hausdorff) onto a closed subset of L¹(μ). So
  limits in measure of coherent models are coherent, and their credal sets converge.
- [I3] **R1 Lemma 1.2.** Bayes models are pointwise minimisers.
- [I4] **Lemma signs; Lemma caps; Lemma sandwich; Lemma rotation; Lemma risingsun; Prop regularity; Prop blowup;
  Lemma twoslope; Cor PCNS; Prop boxbridge(a), (b); the corner algebra of Prop T1.** These are all R2 except boxbridge
  (R1). They are used only through the properties (P1)–(P8) of Prop 3.1. The table in §3.3 records where each property
  enters.
- [I5] **B2 Lemma 3 (support).** Re-proved in Lemma 2.7(d).

**Not used:**
- (Av), edge confinement (M3.7(d));
- Theorem gm, Thm ccibu, Prop chainchords as a black box;
- R4 Thm B (replaced by D1_referee's open-chart argument);
- Thm cuts, Thm apex;
- integrability of env;
- (γ₀) at boundary weights.

---

## 2. Foundations

### 2.1 Tie anatomy

Let Z_q be the set of mixed pairs with at least two q-optimal advices, and E := {q ∈ Ω : μ(Z_q) > 0}. For each
two-element subset {a, b} of advices, the map g ↦ (ℓ(g,a) − ℓ(g,b))/|·| pushes μ (restricted to the pairs with
a, b ∈ A(g)) forward to S². Let m be the sum of these push-forwards, m = m_a + m_c its atomic and non-atomic parts,
and {±b_k} the atoms.
- Each b_k has strict mixed signs. Its **atom line** is ℓ_k := {q ∈ aff Δ : b_k·q = 0}.
- C₀ := {q ∈ Ω : m_c(q^⊥) > 0}, where q^⊥ is a great circle.
- C_E := C₀ ∪ {pairwise intersections of distinct atom lines}.
- A point t ∈ Ω ∖ C_E is **generic**.

**Lemma 2.1 (PROVED).**
- (a) C₀ and C_E are countable. E ⊆ C₀ ∪ ⋃_k ℓ_k, so E is Lebesgue-null. E is Borel.
- (b) If t is generic and lies on no atom line, then t ∉ E.
- (c) If t ∈ E is generic, it lies on exactly one atom line ℓ′ = {b′·q = 0}. There is ρ > 0 with ℓ′ ∩ B(t,ρ) ⊆ E.
  For a.e. pair g ∈ Z_t, every difference of two t-optimal advices is a nonzero multiple of b′.
- (d) (one-sided limits) Let t ∈ E be generic and H^±_t := {q ∈ aff Δ : ±b′·q > 0}. There are credal sets K^±(t)
  with the following property. Take any q_n → t in H^±_t, and any coherent models X_n = D_{K_n} that agree a.e. with
  the q_n-optimum wherever it is unique. This includes D♭_{q_n}, D^δ_{q_n} (§2.2) and the Bayes model at q_n ∉ E. Then
  K_n → K^±(t). If t ∉ E is generic, the same holds with the single limit K_t.
- (e) In (d), D_{K⁺(t)} △ D_{K⁻(t)} consists, up to a null set, of gambles of strict pattern σ′ or −σ′, where σ′ is
  the pattern of b′.

*Proof.*
- **(a)** Two distinct great circles meet in two points, which are m_c-null. So the great circles of positive m_c-mass
  are countably many. Since q ↦ q^⊥ is injective on Ω, C₀ is countable.
  - For q ∈ Ω, μ(Z_q) ≤ m(q^⊥). This is positive only if q ∈ C₀ or q ⊥ b_k for some k.
  - The set of (q, g) with g ∈ Z_q is Borel, so q ↦ μ(Z_q) is Borel by Tonelli.
- **(b)** If t lies on no atom line and t ∉ C₀, then m(t^⊥) = 0.
- **(c)** t ∈ E ∖ C₀, so some atom lies on t^⊥. By genericity only ±b′ does.
  - The gambles of Z_t with a tied difference vector of any other direction have μ-measure at most
    m_c(t^⊥) + m_a(t^⊥ ∖ {±b′}) = 0.
  - For a.e. g ∈ Z_t, the advices that are not t-optimal are worse by a margin μ_t(g) > 0. The tied differences
    vanish on all of ℓ′.
  - So for q ∈ ℓ′, Z_q ⊇ {g ∈ Z_t : μ_t(g) > 2|q − t| env(g)}, whose measure tends to μ(Z_t) > 0 as q → t.
- **(d)** Fix a.e. g.
  - If g ∉ Z_t, the t-optimal advice is unique with a margin, and it stays the unique optimum near t.
  - If g ∈ Z_t, then by (c), for t-optimal a, a′ we have ℓ(a) − ℓ(a′) = κ_{aa′}b′ with κ_{aa′} ≠ 0. So
    q·(ℓ(a) − ℓ(a′)) = κ_{aa′}(b′·q), because b′·t = 0. On each open side the t-optimal advices have pairwise
    distinct values, so there is a unique minimiser a^±(g), constant on the side. The advices that are not t-optimal
    remain worse near t.
  - Hence along q_n → t in H^±_t the q_n-optimal advice is eventually unique and equal to a^±(g). So the advice of
    X_n at g is eventually a^±(g), whatever X_n does at ties. The models converge pointwise a.e., hence in measure, to
    X^± := {g : a^±(g) = accept}.
  - By [I2], X^± = D_{K^±(t)} is coherent and K_n → K^±(t).
  - The case t ∉ E is the same with Z_t null.
- **(e)** A gamble in the symmetric difference has its pair in Z_t. By (c) its tied vector is one of ±c, ±c′, ±d,
  and each of these carries the pattern ±σ(g). So σ(g) = ±σ′. ∎

### 2.2 Tie-breaking families

Call δ ∈ 𝟙^⊥ ∖ 0 **generic** if:
- b_k·δ ≠ 0 for every atom (no atom line is parallel to δ);
- μ{g : some difference vector v of g has v·δ = 0} = 0.

Each g lies in the bad set of at most six directions up to sign, so all but countably many directions are generic.
- For generic δ, D^δ_q chooses on each pair the lexicographic minimiser of (q·ℓ, δ·ℓ) over A(g). It is a.e. unique.
- D♭_q accepts g iff accepting g is the unique q-optimum, i.e. iff q ∈ R(g).
- At q ∉ E, write K_q for the credal set of the unique Bayes model.

**Lemma 2.2 (PROVED).**
- (a) For generic δ and **every** q ∈ Ω, D^δ_q is a coherent q-Bayes model, D^δ_q = D_{K^δ_q} a.e.
- (b) For every q ∈ Ω, D♭_q is coherent, D♭_q = D_{K♭_q} a.e., and K♭_q ⊇ K for every coherent model D_K that agrees
  a.e. with the q-optimum wherever it is unique. In particular K♭_q ⊇ K^δ_q, and K♭_q = K^δ_q = K_q for q ∉ E.
- (c) (upper semicontinuity) If q_n → q in Ω and K♭_{q_n} → K\*, then K\* ⊆ K♭_q. Hence q ↦ P♭(q,g) := P_{K♭_q}(g)
  is lower semicontinuous, and {P♭(·,g) > t} is open.
- (d) (continuity off E) If q ∉ E, q_n → q, and K_n is K♭_{q_n}, K^δ_{q_n} or the credal set of any coherent model
  agreeing with the q_n-optimum wherever it is unique, then K_n → K_q. Consequently
  |P♭(q′, g′) − P(q,g)| ≤ |g′ − g| + |g|·d_H(K♭_{q′}, K_q) → 0 as (q′, g′) → (q, g).
- (e) (quasi-concavity) For every g₀ ∈ ℝ³, q ↦ P♭(q, g₀) and q ↦ P^δ(q, g₀) are quasi-concave on Ω: {> t} and
  {≥ t} are convex for every t ∈ ℝ.

*Proof.*
- **(a)** The ray q + ℝ₊δ is contained in no atom line, so by Lemma 2.1(a) it meets E in a countable set. Take
  s_m ↓ 0 with q_m := q + s_mδ ∈ Ω ∖ E.
  - For a.e. g, either the q-optimum is unique (and persists near q), or the tied vectors v satisfy v·q = 0 and
    v·δ ≠ 0.
  - Then v·q_m = s_m(v·δ). So the q_m-optimum is eventually the lexicographic minimiser, and the other advices remain
    worse.
  - So Bayes(q_m) → D^δ_q pointwise a.e. These Bayes models are coherent by (H3), so D^δ_q is coherent by [I2]. It is
    a q-Bayes model, and it lies in 𝓜 by [I1].
- **(b)** Let Θ be a countable dense set of generic directions. For a.e. g:
  - if accepting g is the unique optimum, every D^θ_q accepts g;
  - if accepting g is tied with an advice a, the set of θ preferring a is an open half-circle (or contains one, for a
    triple tie), so some θ ∈ Θ rejects g;
  - otherwise no D^θ_q accepts g.

  So D♭_q = ⋂_{θ∈Θ} D^θ_q a.e. Now ⋂_θ D_{K^θ} differs from D_{K♭} with K♭ := cl co ⋃_θ K^θ only on
  {P_{K♭} = 0}, a null cone boundary. So D♭_q is coherent.
  - If D_K agrees with the unique optimum wherever it exists, then D♭_q ⊆ D_K a.e., hence K ⊆ K♭_q.
  - At q ∉ E all three models agree a.e.
- **(c)** For a.e. g ∈ D♭_q the unique q-optimum persists near q, so g ∈ D♭_{q_n} eventually. Then
  1_{D_{K\*}} = lim 1_{D♭_{q_n}} ≥ 1_{D♭_q} a.e., using [I2] for the limit. So D_{K\*} ⊇ D_{K♭_q} a.e., i.e.
  K\* ⊆ K♭_q.
  - Then liminf P♭(q_n, g) ≥ P♭(q, g): a minimum over the smaller limit set is at least the minimum over K♭_q.
- **(d)** At q ∉ E, a.e. g has a unique q-optimum, which persists near q. Every listed model eventually agrees with it.
  This gives convergence in measure, and then [I2]. The estimate uses |m|₂ ≤ 1 on Δ.
- **(e)** For a.e. mixed orientation g, the set {q : g ∈ D^F_q} is convex:
  - for F = ♭ it is R(g) ∩ Ω;
  - for F = δ it is an intersection of half-planes {q·v_a > 0}, closed when δ·v_a > 0 and open when δ·v_a < 0, with
    v_a = ℓ(a) − ℓ(accept g).

  Let P^F(q_i, g₀) > t (i = 1,2), q ∈ [q₁, q₂], and t′ ∈ (t, min_i P^F(q_i, g₀)). A ball B′ around g₀ − t′𝟙 lies in
  D_{K^F_{q₁}} ∩ D_{K^F_{q₂}}.
  - So a.e. g ∈ B′ has q₁, q₂ in its convex accept set, hence q too, so g ∈ D^F_q.
  - Then B′ ⊆ cl D_{K^F_q}, so P^F(q, g₀) ≥ t′ > t.
  - {≥ t} = ⋂_{t′<t} {> t′}. ∎

### 2.3 Exact charts

**Lemma 2.3 (good gambles; PROVED).** For a.e. mixed orientation g the following hold for g and for −g. Call such g
**good**. From §2.5 on, "good" also includes, for g ∈ 𝒞, the a.e. property of Lemma 2.5(c), and the countably many
other a.e. properties used later (strict signs, no zero coordinate).
- R(g) ∩ Ω = {q ∈ Ω : P♭(q, g) > 0} **exactly**;
- R(g) ∩ Ω ⊆ {P^δ(·, g) > 0} ⊆ cl R(g) for every generic δ.

In particular, for good g and every q ∈ Ω, g ∈ D_{K♭_q} ⟺ q ∈ R(g) ⟺ g ∈ D♭_q.

*Proof.*
- For q ∉ E the unique Bayes model is D_{K_q} a.e., and K_q = K♭_q. So {g : [q ∈ R(g)] ≠ [P♭(q,g) > 0]} is null.
  - The map (q, g) ↦ P♭(q, g) is Borel: lower semicontinuous in q and 1-Lipschitz in g. So by Fubini, for a.e. g the
    two open convex sets R(g) ∩ Ω and {P♭(·, g) > 0} (Lemma 2.2(c), (e)) agree up to a null set of q.
  - Two open convex planar sets that agree a.e. are equal: each lies in the closure of the other, and an open convex
    set equals the interior of its closure.
- For δ, the set C = {P^δ(·, g) > 0} is convex and agrees a.e. with R(g) (it equals P♭ off E). So R(g) ⊆ C ⊆ cl R(g). ∎

### 2.4 Vertex continuity and UVN for every family

**Lemma 2.4 (PROVED; = Q4.0(a) and Q4.3, re-derived; no (Av)).**
- (a) For each world l the e_l-optimum is a.e. unique, with margin m_l(g) > 0. The model X_{e_l} it defines is coherent,
  say X_{e_l} = D_{V_l}. As q → e_l in Δ, every model that agrees with the q-optimum wherever it is unique (in
  particular D♭_q, D^δ_q, and D_{K_q} off E) converges in measure to X_{e_l}, and its credal set converges to V_l.
- (b) Let x ∈ N be mixed, and l a world.
  - If x_l > 0, there are a ball B_x ∋ x and a convex relative neighbourhood V_l of e_l with P^F(q, h) > 0 for all
    q ∈ V_l ∩ Ω, h ∈ B_x and F ∈ {♭, δ}. For good h ∈ B_x, R(h) ⊇ V_l ∩ Ω.
  - If x_l < 0, the same holds with P^F(q, h) < 0 and R(h) ∩ V_l = ∅.

*Proof.*
- **(a)** Strict guidance gives distinct world-l ranks, so the minimiser is unique with margin m_l > 0 a.e. For
  q_l ≥ ½, the bound q·(ℓ(a) − ℓ(a_l)) ≥ q_l m_l − (1 − q_l)·2env makes a_l the unique q-optimum off
  {m_l ≤ 4env|q − e_l|₁}. That set decreases to a null set.
  - Hence the listed models converge in measure to X_{e_l}. They are coherent, so X_{e_l} is coherent by [I2], and the
    credal sets converge.
- **(b)** Suppose x_l > 0. By (LF), accepting is available near x and is world-l strictly best. So X_{e_l} accepts a.e.
  gamble of a ball around x, and D_{V_l} contains that ball (an open convex cone).
  - Hence P_{V_l} ≥ 2r₀ on some B(x, r₀).
  - Hausdorff convergence is uniform on bounded sets, so P^F(q, ·) > r₀ on B(x, r₀) for q near e_l.
  - For good h, Lemma 2.3 gives R(h) ⊇ (V_l ∩ Ω) ∖ E. An open convex set containing a dense subset of the open convex
    set V_l ∩ Ω contains it.
  - The case x_l < 0 is symmetric: silence is available by (LF) and world-l better than accepting, so D_{V_l} misses a
    ball around x. ∎

### 2.5 Local one-sidedness at p\*

**Lemma 2.5 (PROVED; = M3.6(a)–(d), re-derived, with one caveat).**
- (0) For a.e. h ∈ ℝ₊N, in particular a.e. h ∈ 𝒞, accepting h is in the advice range.
- (a) For every η > 0 there is r > 0 such that every model agreeing with the q-optimum wherever it is unique, with
  |q − p\*| < r, is η-close to D_{T1} in measure.
- (b) For every η > 0 there is r > 0 with d_H(K, T1) < η for every q ∈ B(p\*, r) and every coherent such model D_K.
  This covers K♭_q, K^δ_q and K_q. Hence there is r₁ > 0 with K♭_q ⊇ K″, and every such K ⊇ K″, for q ∈ B(p\*, r₁).
- (c) For a.e. pair with an orientation h ∈ 𝒞 and **every** q ∈ B(p\*, r₁), accepting −h is not weakly q-optimal.
  Hence:
  - if silence ∈ A(h), accepting h is the unique q-optimum iff c(h)·q > 0, and the only possible tie is "accept h"
    vs silence, on {c(h)·q = 0};
  - if silence ∉ A(h), accepting h is the unique q-optimum at every q ∈ B(p\*, r₁).

  *(Caveat to M3.6(c): silence is guaranteed by (LF) only on N, not on all of 𝒞. Nothing downstream needs it outside N.)*
- (d) There is r₂ ∈ (0, r₁] such that for every q ∈ B(p\*, r₂), Z_q consists, up to a null set, of pairs with an
  orientation in 𝒞.

*Proof.*
- **(0)** By Lemma 2.4(a), X_{e_i} accepts g iff accepting is available and g_i > 0. So D_{V_i} ⊇ N ∩ {g_i > 0} a.e.,
  and D_{V_i} is a cone. Every mixed h ∈ N has a positive coordinate.
- **(a)** By (H4), the p\*-optimum is a.e. unique with margin μ\*(g) > 0. For |q − p\*|₁ < r it stays the unique
  optimum off G_r := {μ\* ≤ 2r env}, and G_r decreases to a null set.
- **(b)** Apply [I2]: the inverse of K ↦ 1_{D_K} is uniformly continuous on the compact space of credal sets. For the
  containment: if d_H(K, T1) < η < dist(K″, ∂T1) and x ∈ K″ ∖ K, separate x from K. The point of T1 at distance η
  beyond the separating line is at distance ≥ η from K, which is a contradiction.
- **(c)**
  - Fix q ∈ B(p\*, r₁). Suppose accepting −h were weakly optimal on a non-null set G′ of such pairs. If it is the
    unique optimum there, every D^δ_q accepts −h. If it is tied, the directions δ preferring it form an open half-circle
    (or contain one), and Fubini over δ gives a generic δ for which D^δ_q accepts −h on a non-null set.
  - But K^δ_q ⊇ K″, so P_{K^δ_q}(−h) ≤ −P_{K″}(h) < 0. This is a contradiction. So for each q, the set of such pairs
    is null.
  - By Tonelli, for a.e. h the closed convex set W(h) of q at which accepting −h is weakly optimal meets B(p\*, r₁) in
    a null set. W(h) is {c′·q ≥ 0, d·q ≤ 0}, or {d·q ≤ 0} if silence is unavailable.
  - W(h) cannot be a nonempty set with empty interior: that would need c′ − λd ∈ ℝ𝟙 with λ > 0, but c′ − λd has the
    strict mixed pattern −σ(h).
  - So W(h) ∩ B(p\*, r₁) = ∅: a point of it would be the limit of interior points.
  - The two bullets of (c) follow, because × is never optimal.
- **(d)**
  - Let ω(r) := 2 sup{d_H(K, T1)}, over q ∈ B(p\*, r) and K ∈ {K♭_q, K^δ_q}. By (b), ω(r) → 0.
  - Take a pair g with min(|P_{T1}(g)|, |P_{T1}(−g)|) > ω|g|. Every K with d_H(K, T1) ≤ ω/2 gives T1's advice
    a_T(g) on g, since |P_K − P_{T1}| ≤ d_H|·|.
  - If such pairs formed a non-null part Z′ of Z_q, then for a.e. g ∈ Z′ the directions δ for which D^δ_q picks an
    advice other than a_T(g) form a set of positive measure. Fubini gives a generic δ with D^δ_q ≠ a_T on a non-null
    subset of Z′, which is a contradiction.
  - The remaining unit vectors decrease, as ω ↓ 0, to S² ∩ (∂D_{T1} ∪ −∂D_{T1}). That set is compact and inside the
    open set 𝒞 ∪ −𝒞. So for small r the remaining pairs have an orientation in 𝒞. ∎

### 2.6 The ball B

Fix r ∈ (0, r₂] so small that (N2) holds: |P♭(q, h^k(τ))| < c̄ for q ∈ B := B(p\*, r), τ ∈ [0,1], k = 1,2,3. This
is possible by Lemma 2.5(b), since P_{T1}(h^k(τ)) = 0.

**Lemma 2.6 (PROVED).**
- (a) (exact local charts) For good g ∈ 𝒞 and every q ∈ B:
  - g ∈ D_{K♭_q} ⟺ [silence ∉ A(g) or c(g)·q > 0];
  - g ∈ D_{K^δ_q} ⟺ [silence ∉ A(g), or c(g)·q > 0, or (c(g)·q = 0 and δ·c(g) > 0)].
- (b) (E inside B) Let m_𝒞 be the push-forward of μ, restricted to the good g ∈ 𝒞 with silence ∈ A(g), under
  g ↦ c(g)/|c(g)|. Then:
  - for q ∈ B, μ(Z_q) = m_𝒞(q^⊥);
  - each atom b of m_𝒞 has its whole chord ℓ_b ∩ B inside E (frozen ties);
  - no atom chord of m_𝒞 passes through p\*;
  - E ∩ B ⊆ ⋃_b ℓ_b ∪ (a countable set);
  - every line through p\* meets E ∩ B in a countable set.
- (c) (exact quasi-linearity) Let g₀ ∈ ℝ³ and t ∈ ℝ with g₀ − t𝟙 ∈ 𝒞. For q₁, q₂ ∈ B and q ∈ [q₁, q₂]:
  - if P♭(q_i, g₀) > t for i = 1,2, then P♭(q, g₀) > t;
  - if P♭(q_i, g₀) < t for i = 1,2, then P♭(q, g₀) < t.

  Hence for such t the four sets {P♭(·, g₀) ⋛ t} ∩ B are convex. This holds for g₀ = h^k(τ), τ ∈ [0,1], and |t| ≤ c̄,
  by (N1).

*Proof.*
- **(a)** Lemma 2.3 together with Lemma 2.5(c).
- **(b)**
  - By Lemma 2.5(d) the ties at q ∈ B are, up to a null set, those of (a): {c(g)·q = 0}.
  - An atom b with chord through q ∈ B has all its gambles tied along ℓ_b ∩ B. If ℓ_b ∋ p\*, then p\* ∈ E, against
    (H4).
  - The non-atomic part charges only countably many great circles, as in Lemma 2.1(a).
  - A line λ ∋ p\* meets each ℓ_b in at most one point, since λ ≠ ℓ_b.
- **(c)**
  - First claim: suppose P♭(q, g₀) ≤ t. Choose t′ ∈ (t, min_i P♭(q_i, g₀)) with g₀ − t′𝟙 ∈ 𝒞 (𝒞 is open). Take a
    ball B′ ⊆ 𝒞 around g₀ − t′𝟙, inside D_{K♭_{q₁}} ∩ D_{K♭_{q₂}} and outside cl D_{K♭_q} (P♭(q, g₀ − t′𝟙) < 0).
    For good g ∈ B′, (a) gives [silence ∉ A(g) or c(g)·q_i > 0] for i = 1,2, and [silence ∈ A(g) and c(g)·q ≤ 0].
    This is impossible for an affine function.
  - The second claim is the mirror argument.
  - The level sets {≥ t}, {≤ t} are intersections of the strict ones, using the openness of 𝒞. ∎

### 2.7 Wedges, Lemma D, chart convexity

Fix a vertex v = v_k of T1 and a crossing w ∈ relint F_k with w_c = 0. Let j be the third index, so w_k < 0 < w_j.
Fix:
- w₊, w₋ ∈ F_k with (w₊)_c > 0 > (w₋)_c;
- concentric balls U″ ⊂⊂ U′ ⊂⊂ U ⊂⊂ Ũ around w, inside int N₀, bounded away from 0, meeting no other facet, with
  w_± ∈ U″. Take rad Ũ ≥ (1 + √3)·rad U, so that h − (v·h)𝟙 ∈ Ũ for h ∈ U;
- U inside the UVN balls (Lemma 2.4(b)) at w for world j, at w₊ for world c, and at w₋ for world c.

Put:
- U^± := U ∩ D_{T1}, resp. U ∖ cl D_{T1};
- W_v(U) := {m ∈ aff Δ : m·w″ ≥ 0 ∀ w″ ∈ F_k ∩ cl U};
- **Γ_v := {q ∈ Ω : D_{K♭_q} ⊇ U⁺}**.

For q ∈ Γ_v ∖ E:
- q ∈ α_v if v ∈ K_q;
- q ∈ β_v if v ∉ K_q.

**Lemma 2.7 (PROVED; R10b §1, Lemma D, written for credal sets).**
- (W1) There is c₀ > 0 with m·w′ ≥ c₀|m − v| for m ∈ W_v(U) and w′ ∈ F_k ∩ cl U′.
- (W2) K ⊆ W_v(U) whenever D_K ⊇ U⁺. Conversely, K ⊆ W_v(Ũ) implies D_K ⊇ U⁺. Also K ⊆ B(v′, η) implies
  K ⊆ W_v(Ũ) ∖ {v} for every other vertex v′ of T1 and small η.
- (W3) (Lemma D) Let K ⊆ W_v(U).
  - If v ∈ K, then P_K(h) ≤ v·h < 0 for every h ∈ U⁻.
  - If v ∉ K, then D_K contains the exterior collar {h ∈ U⁻ : dist(h, F_k ∩ cl U″) < δ_K} for some δ_K > 0.
- (W4) (chart convexity) If W₁, W₂ ⊆ Ω are open and D_{K♭_q} ⊇ U⁺ for q ∈ (W₁ ∪ W₂) ∖ E, then
  co(W₁ ∪ W₂) ⊆ Γ_v. The same holds with U⁺ replaced by U.
- (W5) (support) If P_K(h^k(τ)) = 0 for all τ in a nondegenerate interval, then v_k ∈ K.

*Proof.*
- **(W1)** Write y = m − v ∈ 𝟙^⊥. For z ∈ v^⊥ with |z| small, w′ + z ∈ F_k ∩ cl U. So y·(w′ + z) ≥ 0, i.e.
  y·w′ ≥ ρ|Proj_{v^⊥}y| ≥ ρc|y|, because 𝟙^⊥ ∩ ℝv = 0.
- **(W2)**
  - First claim: by continuity on the facet points of cl U⁺.
  - Second claim: h ∈ U⁺ equals w″ + (v·h)𝟙 with w″ ∈ v^⊥ ∩ Ũ ⊆ F_k (relint F_k is open in v^⊥). So
    m·h = m·w″ + v·h > 0.
  - Third claim: v′·w″ > 0 on the compact F_k ∩ cl Ũ, because only v is active on relint F_k.
- **(W3)**
  - Near w, P_{T1} = v·(·), so v·h < 0 on U⁻.
  - If v ∉ K, then min_K m·w′ ≥ c₀ dist(v, K) > 0 on F_k ∩ cl U′, by (W1). The collar follows by compactness.
- **(W4)** For good h ∈ U⁺, Lemma 2.3 gives R(h) ⊇ (W₁ ∪ W₂) ∖ E, a dense subset of the open set W₁ ∪ W₂. So the open
  convex R(h) contains W₁ ∪ W₂ and its convex hull. At q ∈ co(W₁ ∪ W₂), a.e. h ∈ U⁺ lies in D_{K♭_q}, and D_{K♭_q} is
  an open convex cone.
- **(W5)** K lies in the wedge {m·h(σ) ≥ 0} over the interval. For an interior τ, a point m ∈ K with m·h(τ) = 0 has
  m·h(σ₁) = m·h(σ₂) = 0, because h(τ) is a strictly positive combination of h(σ₁) and h(σ₂). The lines h(σ_i)^⊥ meet
  in aff Δ only at v_k. ∎

### 2.8 Two pattern facts

**Lemma 2.8 (PROVED; NUMERICS (1), (2), (5)).**
- (a) Let v ≠ v′ ∈ Δ and let K be a credal set with v′ ∈ K. Then the open cone W := {g : v·g > 0 > v′·g} lies in
  D_{{v}} ∖ cl D_K. Moreover W ⊄ cl O_σ ∪ cl O_{−σ} for every sign pattern σ. So W contains a non-null open set of
  gambles whose pattern is not ±σ.
- (b) For the crossing w of §2.7 and small s > 0, a small ball around w − s(𝟙 − e_c) lies in U⁻ and in every collar
  of (W3) of width > 2s. Its two halves {g_c > 0} and {g_c < 0} are non-null, with patterns σ₁ and σ₂ that differ
  exactly in coordinate c. Hence σ₂ ∉ {σ₁, −σ₁}.

*Proof.*
- **(a)**
  - Membership: v·g > 0 gives g ∈ D_{{v}}, and P_K(g) ≤ v′·g < 0.
  - v and v′ are nonnegative, distinct and both sum to 1, so they are linearly independent. Hence n := v × v′ ≠ 0,
    W is nonempty, and W + ℝn = W.
  - If W ⊆ cl O_σ ∪ cl O_{−σ}: these closed sets meet only at 0 ∉ W, and W is connected, so W ⊆ cl O_σ, say.
    Then (g + sn)/|s| ∈ cl O_σ for all s, so ±n ∈ cl O_σ and n = 0, a contradiction.
  - W ∖ (cl O_σ ∪ cl O_{−σ}) is then open and nonempty.
- **(b)**
  - P_{T1}(w − s(𝟙 − e_c)) = −s(1 − v_c) < 0, so the point is exterior.
  - Its distance to w is s√2.
  - Its c-coordinate is 0, and its other coordinates have the strict signs of w. ∎

---

## 3. The local chain under (TS): Theorem TS for (γ)-fields

### 3.1 Definitions

For a facet F_k, put Ψ(q, τ) := P♭(q, h^k(τ)) for q ∈ Ω and τ ∈ ℝ. Define:
- A_τ := {Ψ(·, τ) > 0};
- B_τ := {Ψ(·, τ) < 0};
- Z_τ := {Ψ(·, τ) = 0};

all as subsets of Ω. **(TS)** at (F_k, τ) means p\* ∈ cl A_τ ∩ cl B_τ. **(TS_A)** means p\* ∈ cl A_τ.

*Robustness.* (TS) does not depend on the family. A_τ ∩ B is an open half-disc or empty (Lemma 3.3). B_τ ∩ B is empty
or has dense interior. E is null, and P♭ = P = P^δ off E. So the same closures arise from {q ∉ E : P(q, h(τ)) ⋛ 0},
and from P^δ.

### 3.2 The properties used

**Proposition 3.1 (PROVED).** For each facet, Ψ satisfies:
- (P1) Ψ(q, ·) is concave on ℝ for every q.
- (P2) Ψ(p\*, τ) = 0 for τ ∈ [0,1], since K♭_{p\*} = K_{p\*} = T1 by (H4).
- (P3) A_τ is open and convex, and {Ψ(·, τ) ≥ t} is convex for all t (Lemma 2.2(c), (e)).
- (P4) For τ ∈ [0,1] and |t| ≤ c̄, the four level sets {Ψ(·, τ) ⋛ t} ∩ B are convex, and |Ψ| < c̄ on B × [0,1]
  (Lemma 2.6(c), (N2)).
- (P5) Ψ is jointly continuous at (q, τ) for every q ∈ Ω ∖ E (Lemma 2.2(d)).
- (P6) Every line through p\* meets E ∩ B in a countable set (Lemma 2.6(b)).
- (P7) If h(τ)_l > 0 then V_l ∩ Ω ⊆ A_τ, and if h(τ)_l < 0 then V_l ∩ Ω ⊆ B_τ. Here V_l is a relative neighbourhood of
  e_l, uniform for τ in compact subsets of (0,1) (Lemma 2.4(b); h(τ) ∈ Σ ⊆ N).
- (P8) For good g ∈ 𝒞 near h(τ) with silence ∈ A(g), and every q ∈ B: g ∈ D_{K♭_q} ⟺ c(g)·q > 0 (Lemma 2.6(a)).

### 3.3 Half-planes, thin zero sets, and the theorem

**Lemma 3.3 (half-planes and thin zero sets; PROVED).** Fix τ ∈ [0,1].
- (a) A_τ ∩ B is ∅, B, or H⁺ ∩ B for an open half-plane H⁺. If p\* ∈ cl A_τ, the last case holds with p\* on
  λ⁺ := ∂H⁺, and then A_τ ⊆ H⁺ on all of Ω.
- (b) B_τ ∩ B is empty or has nonempty interior H⁻ ∩ B, with H⁻ an open half-plane and B_τ ∩ B ⊆ cl H⁻. If
  p\* ∈ cl B_τ, then p\* ∈ λ⁻ := ∂H⁻.
- (c) If (TS) holds at τ, then λ⁺ = λ⁻ =: λ_τ ∋ p\*, H⁻ is the opposite open side, and **Z_τ ∩ B = λ_τ ∩ B
  exactly, at every point, points of E included.**

*Proof.*
- **(a)** A_τ ∩ B is open and convex, and its complement in B is convex (P4). Separate them by a line L. The open set
  A_τ ∩ B lies in the open side, and the complement lies in the other closed side. So A_τ ∩ B is the open side ∩ B.
  - p\* ∉ A_τ (P2), so p\* ∈ cl A_τ ∖ A_τ lies on L.
  - Global containment: if x ∈ A_τ ∖ H⁺, the convex set A_τ (P3) contains co({x} ∪ (H⁺ ∩ B)), which meets
    B ∖ cl H⁺ near p\*. This is a contradiction.
- **(b)** Suppose B_τ ∩ B is nonempty but lies in a line L′. Then {Ψ ≥ 0} ∩ B ⊇ B ∖ L′, whose convex hull is B. That
  contradicts (P4). So B_τ ∩ B has interior, and the separation argument of (a) applies.
- **(c)**
  - Two lines through p\* bound disjoint open half-planes H⁺ and H⁻ only if they coincide and the sides are opposite.
    So B = (H⁺ ∩ B) ⊔ (λ_τ ∩ B) ⊔ (H⁻ ∩ B), with Z_τ ∩ B ⊆ λ_τ.
  - On λ_τ: at q ∈ λ_τ ∩ B ∖ E, Ψ(q, τ) is a limit of values > 0 and of values < 0 (P5), hence 0.
  - So B_τ ∩ λ_τ ∩ B is a convex subset (P4) of the countable set E ∩ λ_τ ∩ B (P6), i.e. at most one point x. Its
    complement in the open interval λ_τ ∩ B is Z_τ ∩ λ_τ ∩ B, which is convex ((P3) with t = 0 and (P4)).
  - An open interval minus one interior point is not convex. So B_τ ∩ λ_τ ∩ B = ∅. ∎

**Lemma 3.4 (c-clusters at one τ; PROVED).** Let (TS) hold at τ ∈ (0,1) and h = s·h(τ) with s > 0. Let good g_m → h
in 𝒞 with silence ∈ A(g_m), and let ĉ be a limit point of c(g_m)/|c(g_m)|. Then:
- {q ∈ aff Δ : ĉ·q > 0} = H⁺_τ, so ĉ·q = κ n_τ·(q − p\*) with κ > 0, where n_τ is the unit normal of λ_τ pointing
  into H⁺_τ;
- in particular n_τ·(e_i − p\*) ≤ 0 whenever h(τ)_i < 0.

Only (TS) at this single τ is used. If only p\* ∈ cl A_τ and p\* ∈ cl B_τ are known, the same proof applies, with
int(B_τ ∩ B) in place of H⁻ ∩ B.

*Proof.*
- If q ∈ A_τ ∩ B, then P♭(q, h) = sΨ(q, τ) > 0. So a ball around h lies in D_{K♭_q}, and for large m, g_m ∈ D_{K♭_q}.
  By (P8), c(g_m)·q > 0, so ĉ·q ≥ 0.
- Likewise ĉ·q ≤ 0 on int(B_τ ∩ B).
- ĉ is not ∝ 𝟙: otherwise it is a constant ≠ 0 on aff Δ, which violates one of the two inequalities.
- So the affine function ĉ is ≥ 0 on H⁺ ∩ B and ≤ 0 on an open set accumulating at p\*. Hence ĉ·p\* = 0, and the open
  half-plane {ĉ < 0}, whose boundary passes through p\*, misses H⁺ ∩ B. So {ĉ > 0} = H⁺_τ.
- c(g_m)_i < 0 when h(τ)_i < 0, so ĉ_i ≤ 0, and hence n_τ·(e_i − p\*) = ĉ·e_i/κ ≤ 0. ∎

**Theorem 3.2 (Theorem TS for (γ)-fields; PROVED).** Assume (H) and (TS) on F_k at every τ ∈ (0,1). Then, on B:
- (i) (**pivot**) for τ ∈ (0,1):
  - Z_τ ∩ B = λ_τ ∩ B with λ_τ ∋ p\*;
  - A_τ ∩ B = H⁺_τ ∩ B and B_τ ∩ B = H⁻_τ ∩ B;
  - A_τ ⊆ H⁺_τ;
  - n_τ is continuous and strictly monotone in angle;
  - n_τ·(e_l − p\*) > 0 when h(τ)_l > 0;
  - λ_{τ_i} = lin(p\*, e_i) at each crossing.
- (ii) (**cluster clause**) Lemma 3.4 holds for every τ ∈ (0,1).
- (iii) (**no sliding**) At a corner ray shared with F_j (parametrised so that r = h(0) on both facets),
  n^k(0+) = n^j(0+), provided (TS) holds on F_j as well.
- (iv) Lemma rotation, with r₀ replaced by r and with limit anchors q_{τ₁}(ξ) ∉ E; Prop regularity; Prop blowup.
- (v) (**(PC)**) There is a linear Γ_k : v_k^⊥ → 𝟙^⊥ of rank 2 with Γ_k h ∝₊ n_τ for h ∝₊ h(τ), τ ∈ [0,1]. With (iii)
  on all three facets this gives **(NS)**.

*Proof.* Steps 1–6 are the steps of write-up Thm pivot and Thm nosliding, rewritten as N21.4 does with (TS). Each is
re-derived for P♭ with chords allowed. Step 7 imports the analytic lemmas and checks their inputs.

1. *Half-planes and vertex signs.* Lemma 3.3 gives everything in (i) up to and including "A_τ ⊆ H⁺_τ". By (P7),
   V_l ∩ Ω ⊆ A_τ ⊆ H⁺_τ when h(τ)_l > 0. A line through p\* and e_l would cut V_l ∩ Ω, so n_τ·(e_l − p\*) > 0.
2. *Cluster clause and negative signs.* Lemma 3.4.
3. *Monotone pieces.* Let σ < τ < σ′.
   - Concavity (P1) gives A_σ ∩ A_{σ′} ⊆ A_τ pointwise.
   - The intersection is nonempty: it contains (V_j(σ) ∩ V_j(σ′)) ∩ Ω if σ′ < τ_j, by (P7), and likewise with i on
     (τ_i, 1). With A ⊆ H⁺ this gives n_σ ≠ −n_{σ′}.
   - Near p\* the inclusion reads H⁺_σ ∩ H⁺_{σ′} ∩ B ⊆ H⁺_τ ∩ B, an inclusion of wedges. By Farkas,
     n_τ ∈ cone(n_σ, n_{σ′}).
   - On (0, τ_j) all n_τ lie in the open half-circle {n·(e_j − p\*) > 0} (Step 1), so the angle is monotone there.
     The same holds on (τ_i, 1).
4. *Continuity.* Suppose n(τ₀+) ≠ n(τ₀−). On the wedge W := {n(τ₀+)·δ > 0 > n(τ₀−)·δ} and on −W, small δ give
   Ψ(p\* + δ, τ₀) ≥ 0 (limit of points of A_τ, τ ↓ τ₀) and ≤ 0 (outside H⁺_τ, τ ↑ τ₀, using (P1) for continuity in τ).
   - By (P4) the sets {Ψ(·, τ₀) ≥ 0} ∩ B and {≤ 0} ∩ B are convex. Each contains W ∪ −W near p\*, hence a disc
     around p\*.
   - So Ψ(·, τ₀) ≡ 0 near p\*, against (TS_A) at τ₀.
   - Only the A-half was used in Steps 3–4.
5. *Non-constancy; crossing values.* Suppose n_τ ≡ n on [a, b] with line λ.
   - By Lemma 3.3(c), Ψ(q, ·) = 0 on [a, b] for **every** q ∈ λ ∩ B. By Lemma caps(a), Ψ(q, ·) ≤ 0 on ℝ.
   - So λ ∩ B ⊆ B ∖ H⁺_τ for every τ. Both lines pass through p\*, so λ_τ = λ for all τ ∈ (0,1). With continuity, n
     is constant on (0,1).
   - This contradicts Step 1 (> 0 on one side of τ_i) and Step 2 (≤ 0 on the other).
   - So the two monotone pieces glue into one strictly monotone continuous angle. The sign change at τ_i gives
     λ_{τ_i} = lin(p\*, e_i).
6. *No sliding.* Let r = h(0) be a normalised corner ray in Σ.
   - For q with n^k(0+)·(q − p\*) > 0 we have q ∈ A^k_τ for small τ > 0, so Ψ(q, 0) ≥ 0 by continuity in τ. On the
     opposite side Ψ(q, 0) ≤ 0. The same holds for F_j.
   - If n^k(0+) ≠ n^j(0+), then P♭(·, r) = 0 on a double wedge at p\*. By (P4) (r ∈ Σ) both {≥ 0} ∩ B and {≤ 0} ∩ B
     are convex, so P♭(·, r) ≡ 0 on a disc B′ around p\*.
   - Strict monotonicity gives q ∈ B′ with n^k(0+)·(q − p\*) < 0 and q ∈ A^k_τ for some τ ∈ (0,1). Also q ∉ A^k_σ for
     σ ∈ (0, η).
   - Then {Ψ^k(q, ·) > 0} is an interval missing (0, η), and Lemma caps(a) gives Ψ^k(q, 0) < 0. Contradiction.
   - Every step is pointwise in q.
7. *Analytic part.* Lemmas sandwich, caps, rotation and risingsun, Props regularity and blowup, Lemma twoslope and
   Cor PCNS [I4] use Ψ only through the following:

| lemma | what it needs of Ψ | available |
|---|---|---|
| sandwich (radius r) | {f > 0} ∩ B a half-disc; f ≤ 0 on λ ∩ B; convexity of {f < t}, {f ≤ t} ∩ B | (P4), Lemma 3.3(c) |
| caps (a), (b) | concavity in τ | (P1) |
| caps (c) | joint continuity of Γ(q, τ) at the point where semicontinuity is taken | (P5) at q ∉ E |
| rotation | sandwich; caps(b) at the approaching anchors q_{τ₀}(ξ), pointwise (any q); caps(c) **only at the limit anchor** q_{τ₁}(ξ) | choose ξ with q_{τ₁}(ξ) ∉ E: λ_{τ₁} ∩ E ∩ B is countable (P6) |
| risingsun, twoslope | none (real analysis) | — |
| regularity (a)–(d) | rotation at countably many τ (a, b, c, and every τ ∈ E′ used); sandwich; concavity | as above, one anchor off E per τ |
| blowup | regularity(a), concavity (Lipschitz in τ), property (M) from sandwich, Arzelà–Ascoli, sweep and window (pointwise in q) | yes |
| PCNS | blowup, twoslope, non-constancy (Step 5), no sliding (Step 6) | yes |

   The limit anchors are the only points at which continuity in q is used. The write-up's chainchords proof makes the
   same observation for the U-domain (its "joint continuity is used only at the limit anchor"). The approaching
   anchors q_{τ₀}(ξ) lie on λ_{τ₀}, where Ψ(·, τ₀) = 0 **at every point** (Lemma 3.3(c)). That is the only property
   rotation uses there.
8. *(PC), (NS).* Cor PCNS. The direction field n_τ is the zero-chord field of Step 5, independent of subsequences. ∎

**Corollary 3.5 (crossing rows, corner equation, cluster clause in vector form; PROVED).** If (TS) holds on all three
facets, then:
- (a) for each crossing coordinate i of F_k, c_k(h)_i = λ_ik h_i with λ_ik > 0 (Prop boxbridge(a));
- (b) c_k(r) ∝₊ c_j(r) at each corner (boxbridge(b));
- (c) for T1, x₁ = x₂ = x₃ = x ∈ {x₊, x₋} with x + 1/x = κ + 1 (corner algebra of Prop T1);
- (d) (Lemma veccluster) for h on an open facet segment h^k((0,1)) ⊆ Σ, and good g_m → h,
  c(g_m)/|c(g_m)| → c_k(h)/|c_k(h)| in ℝ³. Uniformly: if c_k(h)·q₀ ≠ 0 at some q₀ ∈ aff Δ, then c(g)·q has that sign
  for good g near h and q near q₀. At other scales s·h(τ) the same holds for good g_m with silence ∈ A(g_m). This is
  all that M3.8 and Q4.1 use: their facet gambles are normalised into Σ, and their box witnesses converge to
  crossings in Σ.

*Proof.*
- (a), (b) and (c) use only unique c-clusters at p\*, (PC) and (NS), and algebra. Those are Theorem 3.2 (ii) and (v).
- (d): by Lemma 3.4 every limit point has the same zero line and orientation as c_k(h). An affine function on aff Δ
  determines its coefficient vector, since aff Δ spans ℝ³. Uniformity follows by contradiction along a subsequence.
- Near Σ ⊆ int N₀ ⊆ N, silence is in the advice range by (LF), so c(g_m) is defined. Off N it may not be, which is why
  the last sentence of (d) carries the silence clause. ∎

---

## 4. Lemma M and Theorem PL across chords (GAP (ii)); R23.1 for K♭ (checklist (iii))

**Definition 4.0 (cluster walls).** For v ∈ Δ, let Ẑ_v be the set of Q ∈ Ω such that K_{q_n} → {v} (Hausdorff) for some
q_n ∈ Ω ∖ E with q_n → Q.

Properties (PROVED):
- (a) Ẑ_v is relatively closed in Ω (diagonal argument).
- (b) Ẑ_v ∖ E = {q ∉ E : K_q = {v}} (Lemma 2.2(d)).
- (c) If Q is generic, Ẑ_v ∋ Q iff K_Q = {v} (Q ∉ E), or K⁺(Q) = {v}, or K⁻(Q) = {v} (Q ∈ E). This is Lemma 2.1(d):
  near a generic Q ∈ E the off-E points lie on the open sides.
- (d) dist(p\*, Ẑ_v) > 0, because K is continuous at p\* ∉ E with K_{p\*} = T1 ≠ {v}.
- (e) For v ≠ v′ vertices of T1: if Q ∈ Ẑ_v, then Q ∈ cl β_{v′} (by (W2)).
- (f) Ẑ_v ⊆ cl 𝒵_v(η) for every η > 0, where 𝒵_v(η) := {q ∉ E : K_q ⊆ B(v, η)}.

A segment S = [o, y] ⊆ Ω is **generic** if S ∩ C_E = ∅ and S lies in no atom line. Then S is transversal to every atom
line it meets, and every point of S is generic. Fix two open sets O₁, O₂ ⊆ Ω. For a.e. (o, y) ∈ O₁ × O₂ the segment
[o, y] is generic: the pairs whose segment passes through a given point, or lies in a given line, form a null set,
and there are countably many of each.

**Lemma 4.1 (Lemma M across chords; PROVED).** In the setting of §2.7, let G ⊆ Ω be open with G ⊆ Γ_v, and let
S = [o, y] ⊆ G be generic. Suppose o ∉ cl β_v and S ∩ cl β_v ≠ ∅, and let Q be the first point of cl β_v on S. Then
**Q ∈ Ẑ_v.**

*Proof.* The points of [o, Q) ∖ E lie in G ∖ E ⊆ Γ_v and not in β_v, so they lie in α_v: v ∈ K_q.

**Case Q ∉ E.**
- β_v is relatively open in Ω ∖ E near Q, by continuity at Q (a collar point of D_{K_Q} persists). So Q ∉ β_v,
  otherwise off-E points of [o, Q) near Q would lie in β_v. Hence Q ∈ α_v.
- Suppose K_Q ≠ {v}. Run Steps 1–4 below with K_p ⊄ B(v, ρ) on B(Q, r′) ∖ E, which holds by continuity at Q. The
  conclusion contradicts Q ∈ cl β_v. So K_Q = {v}.

**Case Q ∈ E.** Q is a generic point of one atom line ℓ′, S crosses ℓ′ transversally at Q, and ℓ′ ∩ B(Q, ρ) ⊆ E
(Lemma 2.1(c)). Let K^s and K^o be the one-sided limits from o's side and from the other side.
- Since v ∈ K_q on [o, Q) ∖ E, v ∈ K^s.
- Both K^s and K^o lie in W_v(U), a closed condition that holds on G ∖ E.
- **(A) v ∉ K^o.** By (W3), D_{K^o} contains a collar, while D_{K^s} ∩ U⁻ = ∅. So the collar lies in
  D_{K^o} ∖ D_{K^s}, which by Lemma 2.1(e) has patterns ±σ′ only. The collar ball of Lemma 2.8(b) has two non-null
  halves with patterns not of the form ±σ′ simultaneously. Contradiction.
- **(B) v ∈ K^o.** If K^s = {v} or K^o = {v}, then Q ∈ Ẑ_v. Otherwise both contain v and a point at distance ≥ 2ρ
  from v. Run Steps 1–4 on B(Q, r′) ⊆ G, with K_p ⊄ B(v, ρ) for p ∈ B(Q, r′) ∖ E. This holds because such p lie on
  an open side and K_p → K^±.

**Steps 1–4** (R10b Lemma M, with D1_referee §5's open-chart Step 1). Put B° := B(Q, r′).

1. *(no reject cell)* Let h ∈ U⁻ be good with nearest facet point w′ ∈ F_k ∩ cl U′ and |h − w′| < c₀ρ.
   - If R(−h) ∩ B° ≠ ∅, this open set contains a point q ∉ E, and Lemma 2.3 gives P(q, −h) > 0.
   - Then K_q ⊆ {m·h < 0} ∩ W_v(U). For m ∈ K_q, (W1) gives c₀|m − v| ≤ m·w′ ≤ m·h + |w′ − h| < |w′ − h|, so
     K_q ⊆ B(v, ρ). Contradiction.
   - So R(−h) ∩ B° = ∅. Then {c(h) > 0} ∩ B° ⊆ {d(h) ≥ 0}: if c·q > 0 > d·q then c′·q > 0 and q ∈ R(−h).
   - An open set inside a closed half-plane lies in the open half-plane, so R(h) ∩ B° = {c(h)·q > 0} ∩ B°.
2. *(chart lines through Q)*
   - For fixed good h ∈ U⁻, P(q, h) < 0 for q ∉ E near Q. Indeed v ∈ K_Q in case Q ∉ E, and v ∈ K^s ∩ K^o in case (B),
     so P_{K}(h) ≤ v·h < 0 for these limit sets. By Lemma 2.3, R(h) misses a neighbourhood of Q, so c(h)·Q ≤ 0.
   - Points s ∈ β_v ∖ E accumulate at Q. Each has a collar of width δ(s) (W3), and by continuity at s its gambles are
     accepted near s.
   - So for good h ∈ U⁻ within δ(s) of the facet, R(h) meets every neighbourhood of s. Hence the line {c(h) = 0}
     separates Q from points arbitrarily near s.
3. *(the two clusters agree)* Take s_n ∈ β_v ∖ E with |s_n − Q| < 1/n, and good h±ⁿ ∈ U⁻ within δ(s_n) of the facet,
   with h±ⁿ → w_±. Then their chart lines pass within 1/n of Q. Pass to normalised limits a_± of c(h±ⁿ). Then
   a_±·Q = 0, and a_± ∉ ℝ𝟙 because Q ∈ Ω.
   - (i) If a₊·q > 0 with q ∈ B°, then a neighbourhood of q lies in R(h₊ⁿ) for large n. Its off-E points accept
     h₊ⁿ ∈ U⁻ (Lemma 2.3), so they lie in β_v. Hence {a₊ > 0} ∩ B° ⊆ cl β_v.
   - (ii) If q ∈ β_v ∩ B°, then for large n, h₋ⁿ lies in q's collar. So P(q, h₋ⁿ) > 0, q ∈ R(h₋ⁿ), and
     c(h₋ⁿ)·q > 0. Hence a₋ ≥ 0 on β_v ∩ B°, and therefore on cl β_v ∩ B°.
   - So {a₊ > 0} ∩ B° ⊆ {a₋ ≥ 0}. Both lines pass through Q, so a₊ = λa₋ with λ > 0.
4. *(signs)*
   - (a₋)_c ≤ 0, because c(h₋ⁿ)_c < 0.
   - By UVN at w₊ for world c (Lemma 2.4(b)), {c(h₊ⁿ)·q > 0} ⊇ R(h₊ⁿ) ⊇ V_c ∩ Ω. So a₊ ≥ 0 on V_c ∩ Ω. Since its
     zero line passes through Q ∈ Ω, it cannot pass through e_c, so (a₊)_c > 0.
   - Contradiction. ∎

**Theorem 4.2 (PL across chords; PROVED).** Let v ≠ v′ be vertices of T1, each with crossing data as in §2.7. There is
no nonempty open O ⊆ Ω with O ⊆ Γ_v ∩ Γ_{v′} and v, v′ ∈ K_q for all q ∈ O ∖ E.

*Proof.* Suppose O exists.
- Let w be v's crossing with w_j > 0, and V_j the UVN neighbourhood at w for world j.
  - Then D_{K♭_q} ⊇ U_v (all of U_v) for q ∈ V_j ∩ Ω, so V_j ∩ Ω ⊆ Γ_v and (V_j ∩ Ω) ∖ E ⊆ β_v.
  - By (W4), G := int co(O ∪ (V_j ∩ Ω)) ⊆ Γ_v.
- Pick a generic S = [o, y] with o ∈ O and y ∈ V_j ∩ Ω.
  - O is open and O ∖ E ⊆ α_v ∩ α_{v′}, so O ∩ cl β_v = O ∩ cl β_{v′} = ∅.
  - y ∈ cl β_v.
  - Let Q₁ be the first point of cl β_v on S. By Lemma 4.1, **Q₁ ∈ Ẑ_v.**
- Take q_n ∉ E with q_n → Q₁ and K_{q_n} → {v}. By continuity at q_n and (W2), there are balls B(q_n, r_n) on which
  D_{K♭_q} ⊇ U⁺_{v′} and v′ ∉ K_q off E.
  - By (W4), G′ := int co(O ∪ ⋃_n B(q_n, r_n)) ⊆ Γ_{v′}.
  - [o, Q₁) ⊆ G′: (1 − t)o + tQ₁ is within t|Q₁ − q_n| of (1 − t)o + tq_n, which is the centre of the ball
    (1 − t)B(o, ε) + tq_n ⊆ G′ of radius (1 − t)ε.
  - Q₁ ∈ cl β_{v′} (4.0(e)). Let Q₂ be the first point of cl β_{v′} on [o, Q₁]. Then Q₂ ∈ (o, Q₁].
- **Q₂ < Q₁.** Lemma 4.1 for v′ on the generic segment [o, Q₂] ⊆ G′ gives Q₂ ∈ Ẑ_{v′}. By 4.0(e), Q₂ ∈ cl β_v, which
  contradicts the choice of Q₁.
- **Q₂ = Q₁.** Then the points of [o, Q₁) ∖ E lie in α_v ∩ α_{v′}, so v, v′ ∈ K_q there.
  - If Q₁ ∉ E, then K_{Q₁} ∋ v′ by continuity, but K_{Q₁} = {v} (4.0(b)). Contradiction.
  - If Q₁ ∈ E, then K^s(Q₁) ∋ v, v′. Since Q₁ ∈ Ẑ_v and K^s ≠ {v}, 4.0(c) gives K^o(Q₁) = {v}. By Lemma 2.8(a),
    D_{K^o} ∖ D_{K^s} contains a non-null open set of gambles whose pattern is not ±σ′. This contradicts
    Lemma 2.1(e). ∎

*Remark (why this closes GAP (ii)).* The original proof took the nearest point of the closed set Z_v ∪ Z_{v′} and
applied Lemma P along [o, A]. Approximate walls {q ∉ E : K_q ⊆ B(v, η)} are not closed. The closed cluster walls Ẑ_v
replace them, and the second first-point search runs on a subsegment of the **same** generic segment. So no specific
endpoint A must be generic. The only new ingredient is Lemma 2.8(a). It is what makes Ẑ_v ∩ Ẑ_{v′} ∩ S empty, and what
excludes the one-sided configuration K^o = {v}, K^s ∋ v′.

**Lemma 4.3 (R23.1 for K♭, chords in the ball; PROVED).** Let F_k have a crossing τ_c ∈ (σ₁, σ₂) and 0 < ρ ≤ r. Suppose
Ψ(·, σ₁) ≥ 0 and Ψ(·, σ₂) ≥ 0 on B_ρ := B(p\*, ρ). Then for every q ∈ B_ρ:
- v_k ∈ K♭_q;
- Ψ(q, ·) ≡ 0 on [σ₁, σ₂] and Ψ(q, ·) ≤ 0 on [0,1];
- B_ρ ⊆ Γ_{v_k} for balls U around w = h(τ_c) with F_k ∩ cl Ũ ⊆ cone h([σ₁, σ₂]).

*Proof.*
- **Γ.** Concavity gives Ψ ≥ 0 on B_ρ × [σ₁, σ₂]. So K♭_q ⊆ W_{v_k}(Ũ), and (W2) gives D_{K♭_q} ⊇ U⁺.
- **The sets α♭, β♭.** Put β♭ := {q ∈ B_ρ : v_k ∉ K♭_q} and α♭ := B_ρ ∖ β♭.
  - β♭ is open, by upper semicontinuity (Lemma 2.2(c)).
  - p\* ∈ α♭, since K♭_{p\*} = T1.
- **α♭ is open.** Suppose Q ∈ α♭ ∩ cl β♭. Every gamble of U⁻ is in 𝒞, and Lemma 2.6(a) holds at **every** q ∈ B_ρ. So:
  - Q ∈ α♭ gives P♭(Q, h) < 0 on U⁻, hence c(h)·Q ≤ 0 for good h ∈ U⁻;
  - s ∈ β♭ gives a collar of width δ(s) in D_{K♭_s} (W3), hence c(h)·s > 0 for good collar gambles.

  Steps 3–4 of Lemma 4.1 now run verbatim with K♭ in place of K, and with no exceptional points:
  - in (i), **every** q′ ∈ R(h₊ⁿ) ∩ B_ρ has h₊ⁿ ∈ D_{K♭_{q′}} by the exact charts of Lemma 2.3, hence q′ ∈ β♭;
  - in (ii), q ∈ β♭ puts h₋ⁿ in D_{K♭_q} for large n, so q ∈ R(h₋ⁿ) and c(h₋ⁿ)·q > 0 (Lemma 2.6(a)).

  This contradicts UVN at w₊.
- **Conclusion.** B_ρ is connected, so B_ρ = α♭. Then Ψ(q, τ) ≤ v_k·h(τ) = 0 on [0,1], with equality on [σ₁, σ₂]. ∎

---

## 5. (TS) holds: TSalways for (γ)-fields

**Lemma 5.1 (R23.2: B-failure alone is impossible; PROVED).** If p\* ∈ cl A_τ for every τ ∈ (0,1) on F_k, then
p\* ∈ cl B_τ for every τ.

*Proof.*
- Steps 3–4 of Theorem 3.2 used only (TS_A). So A_τ ∩ B = H⁺_τ ∩ B, A_τ ⊆ H⁺_τ, and n_τ is monotone on the two pieces
  and continuous.
- Suppose p\* ∉ cl B_{τ₀}. Then D⁻ := B(p\*, ρ₀) ∩ {n_{τ₀}·(q − p\*) < 0} lies in Z_{τ₀}.
- **n is constant.** If n_{τ₁} ≠ n_{τ₀}, pick q ∈ A_{τ₁} ∩ D⁻. Concavity gives Ψ(q, τ) > 0 strictly between τ₀ and
  τ₁, so n_τ·(q − p\*) > 0 there. Continuity at τ₀ then contradicts q ∈ D⁻.
- **B fails outside [τ_i, τ_j].** Let τ < τ_i. If p\* ∈ cl B_τ, Lemma 3.4 (second form) gives n·(e_i − p\*) ≤ 0. But
  V_i ∩ Ω ⊆ A_{τ′} ⊆ H⁺ for τ′ > τ_i gives n·(e_i − p\*) > 0. The case τ > τ_j is symmetric.
- **Contradiction.** Take τ′ < τ_i and τ‴ > τ_j. Then Ψ(·, τ′) ≥ 0 and Ψ(·, τ‴) ≥ 0 on some B(p\*, ρ) with ρ ≤ r.
  Lemma 4.3 with crossing τ_i gives A_{τ_i} ∩ B(p\*, ρ) = ∅, against p\* ∈ cl A_{τ_i}. ∎

**Proposition 5.2 (N21.9: pinned set and wall; PROVED).** Suppose A_{τ₀} ∩ B(p\*, ρ) = ∅ on F_m, with ρ ≤ r.
- Choose σ₁ < τ₀ < σ₂ whose interval contains a crossing τ_c and such that h(σ₁), h(σ₂) share a positive coordinate l.
  This is Option 1 or 2 of N28 §3, by Lemma signs.
- Put G := int{q ∈ Ω : Ψ(q, σ₁) ≥ 0, Ψ(q, σ₂) ≥ 0} and O := G ∩ B(p\*, ρ).

Then:
- (i) G is open and convex, G ⊇ V_l ∩ Ω, O ≠ ∅, and p\* ∈ cl O;
- (ii) for q ∈ O: Ψ(q, ·) ≡ 0 on [σ₁, σ₂] and v_m ∈ K♭_q; and G ⊆ Γ_{v_m};
- (iii) (**wall toward V_l**) for a.e. (o, y) ∈ O × (V_l ∩ Ω), the segment [o, y] meets Ẑ_{v_m}.

*Proof.*
- **(i)** Each {Ψ(·, σ_i) ≥ 0} is convex (P3) and contains p\* (P2) and V_l ∩ Ω (P7). So their intersection contains
  co({p\*} ∪ (V_l ∩ Ω)), whose interior has p\* in its closure.
- **(ii)**
  - On O, Ψ(·, τ₀) ≤ 0 and Ψ(·, σ_i) ≥ 0. A concave function that is ≥ 0 at both ends and ≤ 0 at an interior point
    vanishes on the interval.
  - (W5) gives v_m ∈ K♭_q.
  - G ⊆ Γ_{v_m} as in Lemma 4.3.
- **(iii)**
  - G is convex, contains O and V_l ∩ Ω, and lies in Γ_{v_m}.
  - O ∖ E ⊆ α_{v_m}, so O ∩ cl β = ∅.
  - (V_l ∩ Ω) ∖ E ⊆ β, by UVN at w = h(τ_c) for world l, where w_l > 0.
  - For generic (o, y), Lemma 4.1 applies to the first point of cl β on [o, y]. ∎

**Proposition 5.3 (N28 Prop 3.1: a wall forbids two-signedness; PROVED).** Let F_m have a wall toward V_l with pinned
set O, as in 5.2. Let i ≠ m and τ₁ ∈ (0,1) with h^i(τ₁)_l < 0. Then (TS) fails at τ₁ on F_i.

*Proof.* Suppose (TS) holds there, with normal n.
- Lemma 3.4 gives n·(e_l − p\*) ≤ 0, so some y₀ ∈ V_l ∩ Ω has n·(y₀ − p\*) < 0. Fix b > 0 and an open set
  Y ⊆ V_l ∩ Ω with n·(y − p\*) < −b on Y.
- d := dist(p\*, Ẑ_{v_m}) > 0 by 4.0(d).
- For δ > 0, pick a generic (o, y) ∈ (O ∩ B(p\*, δ)) × Y. This pair set has positive measure. The segment meets Ẑ_{v_m}
  at some Q.
- By 4.0(f), Q is a limit of q_n ∉ E with P(q_n, h^i(τ₁)) → v_m·h^i(τ₁) > 0. So q_n ∈ A^i_{τ₁} ⊆ H⁺, and
  n·(Q − p\*) ≥ 0.
- A point (1 − t)o + ty with n·(· − p\*) ≥ 0 has t ≤ δ/(δ + b). So d ≤ |Q − p\*| ≤ δ(1 + 2/b), which fails for small δ. ∎

**Lemma 5.4 (N28 Lemma 3.2; PROVED).** Let F_m have a pinned set O as in 5.2, and let l ≠ m. Then there are no
σ₁ < τ_c < σ₂ with τ_c a crossing of F_l and p\* ∉ cl B^l_{σ₁} ∪ cl B^l_{σ₂}.

*Proof.* Otherwise Ψ^l(·, σ_i) ≥ 0 on some B(p\*, ρ) with ρ ≤ r. Lemma 4.3 gives v_l ∈ K♭_q and B(p\*, ρ) ⊆ Γ_{v_l}.
Then O′ := O ∩ B(p\*, ρ) is open and nonempty, O′ ⊆ Γ_{v_m} ∩ Γ_{v_l}, and v_m, v_l ∈ K_q on O′ ∖ E. This contradicts
Theorem 4.2. The crossing balls may be shrunk to meet §2.7, and shrinking a ball enlarges Γ. ∎

**Lemma 5.5 (N28 Lemma 3.3; PROVED, combinatorics).** Suppose F_m has a pinned set and (TS) fails at every τ ∈ (0,1) on
F_l. Then F_l has walls toward V_x and toward V_y, where {x, y} are the indices other than l. Each wall has a pinned set
whose closure contains p\*.

*Proof.* N28's case analysis, with Lemma 5.4 in place of its Lemma 3.2, Lemma 5.1 in place of R23.2, and
Proposition 5.2 in place of N21.9. ∎

**Lemma 5.6 (surround, robust form; PROVED; NUMERICS (4)).** Let 𝒵 ⊆ Ω with d := dist(p\*, 𝒵) > 0. Suppose that for each
i ∈ {1, 2, 3} and every δ > 0 there are o_i ∈ B(p\*, δ), y_i ∈ B(e_i, δ) ∩ Ω and a point of cl 𝒵 on [o_i, y_i]. Then
p\* ∈ co 𝒵.

*Proof.* N28 Lemma 3.4, with the wall point replaced by a point of 𝒵 within δ of it. Then Q_i − p\* = t_i(e_i − p\*) + ε_i
with |ε_i| ≤ 3δ and t_i ≥ (d − δ)/2. The condition 0 ∈ int co{e_i − p\*} is open. ∎

**Theorem 5.7 ((TS) always; PROVED).** Under (H), (TS) holds on every facet at every τ ∈ (0,1).

*Proof.* Suppose not.
1. By Lemma 5.1, (TS_A) fails on some F_m at some τ₀. By Proposition 5.2, F_m has a wall toward some V_l with l ≠ m.
2. By Lemma signs, h^l(τ)_l < 0 on F_l for all τ. By Proposition 5.3, (TS) fails at every τ on F_l.
3. By Lemma 5.5, F_l has walls toward V_m and V_n, where n is the third index.
4. Fix η small and put 𝒵 := 𝒵_{v_l}(η) ∪ 𝒵_{v_m}(η).
   - d := dist(p\*, 𝒵) > 0, by continuity at p\*.
   - The three walls give, for each vertex and each δ, segments as in Lemma 5.6 that meet Ẑ_{v_l} ∪ Ẑ_{v_m}
     ⊆ cl 𝒵 (4.0(f)). This uses that generic pairs exist in every pair of open sets.
   - Lemma 5.6 gives p\* ∈ co 𝒵.
5. For q ∈ 𝒵 and any τ ∈ (0,1), P(q, h^n(τ)) ≥ min(v_l, v_m)·h^n(τ) − η|h^n(τ)| > 0 for small η, so 𝒵 ⊆ A^n_τ.
   - A^n_τ is convex (P3), so p\* ∈ A^n_τ.
   - But Ψ^n(p\*, τ) = 0 (P2). Contradiction. ∎

---

## 6. M3.9 assembled

**Theorem 6.1 (= M3.9; PROVED).** Under (H):
- (a) (TS) holds on every facet at every τ ∈ (0,1) (Theorem 5.7). It is family-independent (§3.1).
- (b) The conclusions of Theorem 3.2 hold on every facet. These are: pivot chords with thin zero sets on B at every
  point; the strictly monotone continuous chord map; crossing values; no sliding; rotation, regularity and blow-up;
  (PC) with rank-2 Γ_k; and (NS). They hold for P♭, and for P at q ∉ E, where P = P♭.
- (c) Crossing rows λ_ik > 0, the corner equation, and x ∈ {x₊, x₋} (Corollary 3.5(a)–(c)).
- (d) The cluster clause in vector form (Corollary 3.5(d)).

Hence (C2) and (C3) of M3 §6 hold. The normalisations p\* = u and x = x₊ used by M3.8 and Q4.1 are diagonal rescalings
and the transposition σ. They preserve (H) and move E projectively.

**Hypotheses actually used.** (H1)–(H4). Not used:
- (Av) or edge confinement, which answers M23_referee §6.10 and §6.13 affirmatively;
- integrability;
- (γ₀) at boundary weights;
- R4 Thm B.

---

## 7. Consequences for the premise "every cover of T1 needs a world that does not add up"

**Corollary 7.1 (PROVED at the input status listed).** Let 𝓜 be a decomposable domain with (LF) at D_{T1}. Take a
ranking with strict (G), (IB), (LA), (S) (closed sections for every model), (C) and T1 ∈ C_L, with (NC) at every world.
Then every endorser tuple ν has a degenerate ladder field ψ^ν: some world has a non-null ladder-blind set. In
particular **no ranking whose worlds all add up covers T1 on any (LF) decomposable domain.**

*Proof.* This is Q4.2's chain, with M3.9 now proved.
- **M3.4** [R1]: ψ := ψ^ν is a (γ₀)-field with T1 Bayes at some p\*. If ψ is non-degenerate, p\* ∈ Ω.
- **D1** [R1, after repairs]: p\* ∉ E.
- So (H) holds, and Theorem 6.1 gives (C2) and (C3).
- **Q4.1** [R1]: (Av) holds. On M_U, Q4.1's Step 4 is already a contradiction (Prop T1).
- **M3.8** [R1] with M3.7(d) [R1]: contradiction.
- If all worlds add up, M3.1's last clause [R1] makes ψ^{ν\*} non-degenerate. ∎

| Domain class | Premise | Weakest inputs |
|---|---|---|
| M_U | holds (Thm M0closed(b)) | R2 (independent of BB2) |
| (Av)-domains, e.g. two-sided near ∂D_{T1} (L3.1(a) [R1]) | holds (M3.10, M3.10′) | M3.1, M3.4, M3.5, M3.8, D1 (each R1); BB2 (one reading, unrefereed) |
| all (LF) decomposable domains | holds (Q4.2) | the above plus Q4.1, Q4.3 (R1) |

R21 Part B is affected as follows:
- **(G0)** and **(GnAv-nd)** are closed at PROVED status, no longer [CH].
- What remains open on general domains is **(GS)**, **(GL)** and **(GnAv-d)**: the degenerate or (NC)-failing
  configurations, unchanged.

Rankings that add up are excluded everywhere (LF) holds. A positive answer to the T1 question must use a world that does
not add up, as on M_U: a strongly (M1) world, or a world with a non-null ladder-blind set.

---

## 8. Checklist answers and corrections to the record

**M3 checklist (M23_referee §6.10).**
- **(i) Chords accumulating at p\*.** Every use of K in the local chain is through P♭(·, g₀) with g₀ − t𝟙 ∈ 𝒞, i.e. a
  near-facet level.
  - On B, P♭ is exactly quasi-linear at such levels (Lemma 2.6(c)), with no continuity.
  - Thin zero sets hold at **every** point of B (Lemma 3.3(c)). The proof combines lower semicontinuity and
    quasi-linearity with "lines through p\* meet E ∩ B countably" (Lemma 2.6(b)).
  - Continuity is used only at limit anchors chosen off E (§3.3 Step 7).
  - **Re-derived**, not read.
- **(ii) Thm PL with approximate walls.** Theorem 4.2, on one generic segment with closed cluster walls. The two parts
  of the GAP as M23 stated it:
  - (a) "Lemma P along specific segments [o, A]" is not needed;
  - (b) "case Q ∈ E restated toward A" is replaced by the Q₂ = Q₁ case, closed by Lemma 2.8(a).
- **(iii) R23.1 for K♭ with chords in the ball.** Lemma 4.3. It is a direct clopen argument for K♭, using the exact
  local half-plane charts at every q ∈ B (Lemma 2.6(a)). There is no d-face issue: inside B no near-facet pair has a
  reject cell.

**Q24_referee §2.4 ("M3.9 uses (Av) nowhere else", CHECKED).** Confirmed by the full proof: the only vertex inputs are
Lemma 2.4 (UVN for every family), which uses (LF) only.

**Corrections** (none changes a conclusion):
1. **M3.6(c).** "Accept h iff c(h)·q > 0" needs silence in A(h). On 𝒞 ∖ N it can be missing (A(h) = {+, −}), and then
   accepting is the strict optimum on all of B. Stated correctly in Lemma 2.5(c). Every gamble the chain uses lies in
   int N₀ ⊆ N, where silence is available.
2. **M3 §6, M3.9 reading, item 2 (Lemma 3.2, case Q ∈ E).** "D1.6 case (B) gives v′ in both one-sided limits" is not
   the operative step. What is needed, and now proved, is Lemma 2.8(a): a one-sided limit {v} next to one containing
   v′ differs on an open cone that meets two non-opposite orthants.
3. **"Lines through p\* meet E in a countable set"** (chainchords on M_U). On two-sided domains this is false outside B:
   - a {+,−} or wedge-chart atom tied only far from p\* may have its line through p\*;
   - only the local statement (Lemma 2.6(b)) holds, and only it is used.

   On M_U the global statement is correct, since all ties there are c-ties on their whole chord.
4. **M3.4.2's "D♭_q is coherent at every q" (M23_referee §6.4).** Correct. The proof needs K♭ := cl co ⋃_θ K^θ and the
   remark that a countable intersection of coherent cones is coherent up to the null boundary {P_{K♭} = 0}
   (Lemma 2.2(b)).

**Referee priorities for BB2, in order of risk.**
1. Lemma 2.1(c)–(e): one-sided limits at generic chord points for every tie-breaking, and the pattern bookkeeping.
2. Theorem 4.2, case Q₂ = Q₁ with Q₁ ∈ E.
3. Lemma 3.3(c): thin zero sets at points of E on λ_τ.
4. Lemma 4.3: the clopen argument for K♭ via Lemma 2.3.
5. Lemma 2.5(d): the tie localisation, and Lemma 2.6(b)'s "no near-facet atom chord through p\*".

---

## 9. Files (`bb2py/`)

`bb2_checks.py`, with output `bb2_checks.out`. Run `python3 -I bb2_checks.py` inside the folder. These are NUMERICS
only:
- (1) Lemma 2.8(a): 2000 random (v, v′, K ∋ v′). The cone {v·g > 0 > v′·g} misses cl D_K and shows two non-opposite
  patterns. 0 failures.
- (2) Lemma 2.8(b): the six crossings of T1 at ε ∈ {.05, .2, .3, .6, .9}. Exterior point, ball outside cl D_{T1},
  halves differing exactly in coordinate c. 0 failures.
- (3) (W1): the sampled wedge constant min m·w′/|m − v| is positive (0.019–0.048) at ε ∈ {.05, .3, .6, .9}.
- (4) Lemma 5.6: 0 failures in 3000 trials at δ/d ≤ 0.05 (p\* with min coordinate ≥ 0.15). Failures appear at
  δ/d = 0.1 (8), 0.5 (709) and 0.9 (1345), so the smallness of δ is needed.
- (5) Lemma 2.8(a) for the ordered vertex pairs of T1 actually used in Theorem 4.2: 480 cases, 0 failures.
