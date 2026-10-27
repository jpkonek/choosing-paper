# Q4. Mixed domains: one cut cell makes every vertex precise, so rankings that add up cannot cover T1 on any (LF) domain

16 Oct 2026, round 21 (BRIEF13 rules). Labels: **PROVED** (full proof here, from results that the write-up or refereed
notes mark proved, each named), **CHECKED** (a step-by-step reading, not a re-derivation), **CONJECTURE**, **NUMERICS**
(`q4py/`, run `python3 -I q4_checks.py` inside it; no proof rests on it). No assumption is added. Notation: write-up
§§2, 5, 6; R10a §2; R10b §§2–3; M3 §§1, 3, 5–7; D1 §3; R21. T = T1, n = 3, Ω = Δ°. A *(γ₀)-field* is an integral ladder
field ψ with integrable envelope that has a coherent Bayes model at every t ∈ Δ (M3.4.2). It is *non-degenerate* if it is
strictly guiding, i.e. every ladder density is > 0 a.e. E = E(ψ) is its exceptional set (non-null ties). K_q is the
credal set of the unique Bayes model at q ∈ Ω ∖ E. V_b is the credal set of the e_b-Bayes model.

---

## 0. Outcome

**No construction exists on the adding-up route. The obstruction is a short theorem, and it closes (GnAv-nd).**

The brief asked for a cover of T1 on a mixed (LF) domain, by a ranking whose worlds add up or by a degenerate ladder
field. Any such cover with a non-(Av) layout needs an **imprecise vertex model** at some vertex b (§4). The obstruction is
that the facet structure at p\* forbids this.

> **Theorem Q4.1 (one cut cell; PROVED, new).** Let ψ be a non-degenerate (γ₀)-field on a decomposable domain 𝓜 with
> (LF) at D_{T1}. Let D_{T1} be the unique ψ-Bayes model at some p\* ∈ Ω, and let (C2), (C3) hold at p\*: (PC), (NS),
> with facet data x ∈ {x₊, x₋}, and the cluster clause (Lemma veccluster). Then for every world b:
> - **V_b = {e_b}**: the e_b-Bayes model is D_{e_b} = {g_b > 0} ∪ {g ≥ 0};
> - acceptance is in the advice range for a.e. g with g_b > 0.
>
> Hence **(Av)** holds, and edge confinement holds too (M3.7(d)).

The proof uses only the following:
- **Step 1 of Thm N21.6**, the box giving a cut: one witness family is two-sided, with q₀ ∉ R(g).
- **One open cell R(−g)** next to the edge prior q₀, where K_q ⊆ {m·g < 0}.
- **Continuity at the vertex.** At e_b the field's minimiser is unique and has a margin, so continuity there holds for
  every field. E plays no role.
- **The test gambles of N21.6(iv).**

It needs **no** apex, **no** R4 Thm B, **no** Hausdorff limits along [a\*, z\*], and **no** edge confinement. These are
exactly the steps that Conjecture M3.C said needed off-E replacements.

> **Corollary Q4.2 (status: that of Prop. M3.9, i.e. CHECKED with M23_referee GAP (ii); plus Q4.1 and Lemma Q4.3, new).**
> On **every** decomposable domain with (LF) at D_{T1}, take a ranking with strict (G), (IB), (LA), (S) (closed sections
> for every model), (C), T1 ∈ C_L and (NC) at every world. Then every endorser tuple has a degenerate ladder field.
> In particular:
> - branch **(GnAv-nd) of R21 is empty**;
> - **no ranking whose worlds all add up covers T1 on any (LF) decomposable domain**. This is M3.10′ without (Av), and
>   it closes the exception flagged in R21 §0 item 9 and in §5 item 6.

**Which input a mixed layout would have to break (the question of the brief).** A non-degenerate field on a non-(Av)
domain needs, at some b, an imprecise vertex model V_b (§4). The other inputs are downstream of that:
- edge confinement (M3.7(d)) and precise vertex limits are *equivalent* to (Av) at that b;
- the cuts are not needed.

Q4.1 derives V_b = {e_b} from the *local* facet data at p\* alone. So the only input left to break is (TS)/(PC)/(NS) at
p\*. M3.6 and M3.9 prove these for every non-degenerate field **whatever the layout**. Lemma Q4.3 removes the single
place where M3.9's reading cited (Av). So no mixed layout can host a ranking that adds up.

For **degenerate** fields, Prop. Q4.4 (PROVED) says where the blindness must sit, at every vertex b where availability
fails. One of three things holds:
- (i) world b is ladder-blind in every neighbourhood of a b-crossing;
- (ii) worlds a and b are jointly blind on the box combinations in J_c, the joint T1-error set of a and b;
- (iii) there is no box-witness structure at e_b. This is automatic if p\* is not interior, or if (PC) fails at p\*.

So (GnAv-d) remains open, now with this localisation.

| | Statement | Label |
|---|---|---|
| Q4.1 | box witnesses at e_b ⇒ V_b = {e_b} ⇒ (Av) | PROVED, new |
| Q4.2 | (GnAv-nd) empty; M3.10, M3.10′ on every (LF) domain | at the status of M3.9 (CHECKED) |
| Q4.3 | UVN for K^♭ and for every tie-breaking family, without (Av) | PROVED, new (D1.1(c) argument) |
| Q4.4 | degenerate fields: availability at b unless (i), (ii) or (iii) | PROVED, new |
| Q4.5 | Q4.1 reproves Cor. N21.7(a)–(c) for additive covers without Thm cuts Steps 3–7 or Thm apex | PROVED (special case) |
| q4py | box witnesses (ε ∈ {.05, .3, .6, .9}); LP for step 7; fat W_b versus one cut cell; step-5 geometry; layout search | NUMERICS |

---

## 1. Setting and imports

**Standing data.** As in Q4.1: 𝓜, (LF) with open N ⊇ ∂D_{T1} ∖ 0, compact collar N₀ ⊆ N (write-up §5), ψ, p\*.

**Imports.**
- **M3.4 [R1].** The maximal ladder field of a ranking with (NC) everywhere is a (γ₀)-field with T1 Bayes at some p\*.
  If it is non-degenerate then p\* ∈ Ω. The proof works on every decomposable domain and uses no (Av).
- **M3.1, last clause [R1].** A world that adds up has null blind set. So a ranking whose worlds all add up has a
  non-degenerate maximal field (M3.5 [R1]).
- **D1 [R1].** p\* ∉ E. It uses no (Av); its UVN is D1.1(c), under (LF) only.
- **M3.6 [R1, M23_referee §6.7].** Local one-sidedness on B₁. No (Av).
- **M3.7(a) [R1].** For good g and q ∉ E: R(±g) = {P(·, ±g) > 0} at q.
- **M3.9 [CHECKED, M23_referee §6.10, GAP (ii)].** (C2), (C3) at p\*, i.e. Thm TS's conclusions with the cluster clause,
  for non-degenerate (γ)-fields.
- **Prop. T1 [R2 chain].** Crossing rows, the corner equation x + 1/x = κ + 1, and the box certificate.
- **Lemma edgebox, in the chart form of Lemma FS [R10b, R12].**
- **Prop. V and Cor. V1 [R10b; R10a Thm V].** Vertex confinement, and no forced acceptance of mixed gambles.
- **R1 Prop. 3.1.** K ↦ 1_{D_K} is a homeomorphism onto its image.
- **Normalisations p\* = u and x = x₊** (Prop. diag(a); transposition of coordinates 1, 2). These preserve
  (γ₀), strict guidance, (LF), the domain, the vertex models and the advice ranges.

**Lemma Q4.0 (field versions of V2, V and V1; PROVED).** Let ψ be any integral (γ₀)-field on an (LF) domain. Let world b
have positive ladder density a.e. on a set G ⊆ M.
- (a) *Vertex margin.* For a.e. g ∈ G the e_b-optimal advice over A′(g) is unique, with margin m_b(g) > 0. If G = M,
  then every q-Bayes model X_q (any q ∈ Δ, any tie-breaking), and the strict-Bayes set D♭_q, satisfy
  μ(X_q △ X_{e_b}) ≤ μ{g : m_b(g) ≤ 4 env(g)|q − e_b|₁} → 0 as q → e_b. So the credal sets of coherent q-Bayes models
  converge to V_b in the Hausdorff metric.
- (b) *Prop. V.* Suppose G contains a ball around some b-crossing w (w ∈ ∂D_{T1}, w_b = 0, w mixed). Then every
  coherent e_b-Bayes model D_K has D_K ⊆ {h_b > 0}, so e_b ∈ K.
- (c) *V1.* Under (b), for a.e. mixed h with h_b < 0, the advice range A(h) contains 0 or −.
- (d) *Any limit.* For any field with integrable envelope, take q_m → t and q_m-Bayes models X_m with X_m → X in
  measure. Then X is t-Bayes. If the X_m are coherent, so is X, and its credal set is the Hausdorff limit.

*Proof.*
- **(a)** World-b penalties strictly increase in rank on A′(g), and the ranks are distinct, so the e_b-optimum is
  unique with margin m_b(g) > 0 a.e. on G. For q ∈ Δ:
  q·(ℓ(g,a) − ℓ(g,a_b)) ≥ q_b m_b(g) − (1 − q_b)·2env(g),
  which is positive off the stated set. That set decreases to a null set, because m_b > 0 and env < ∞ a.e. The same
  bound holds for D♭_q, which agrees with the unique optimum wherever the optimum is unique. Hausdorff convergence then
  follows from R1 Prop. 3.1.
- **(b)** This is R10b Prop. V verbatim. On a ball B ⊆ N ∩ G around w, accept and silence are both available (LF),
  and the e_b-advice is unique, so D_K ∩ B = {h_b > 0} ∩ B. The convexity argument of Prop. V then gives
  D_K ⊆ {h_b > 0}.
- **(c)** If A(h) ⊆ {+, ×} on a non-null set, every coherent model of 𝓜 accepts h there. This includes a coherent
  e_b-Bayes model, which exists by (γ₀). That contradicts (b), since h_b < 0.
- **(d)** ψ^{q_m}(X_m) = min ψ^{q_m} → min ψ^t, since |ψ^q − ψ^t| ≤ |q − t|₁∫env uniformly. ψ^t(X_m) → ψ^t(X) by
  dominated convergence. Coherence passes to the limit (R1 Prop. 3.1, with compactness of credal sets). ∎

---

## 2. Theorem Q4.1: proof

Normalise p\* = u and x = x₊. Fix a failing pair (a, b) ∈ {(1,2), (2,3), (3,1)}, with c the third index. Every world b
occurs (Prop. T1; failing pairs per vertex, N21 §5). Let w′ ∈ relint F_a and w ∈ relint F_c be the two b-crossings, and
q₀(s) := (1 − s)e_b + s e_a.

**Step 1 (box witnesses).** By Prop. T1's certificate (cyclic images of its (1,2) case), for small s > 0 there are
A(s) ∈ relint F_a and B(s) ∈ relint F_c with:
- signs A_a < 0 < A_b and B_b < 0 < B_a;
- ratio A_bB_a < |A_a||B_b|;
- c_a(A)·q₀ > 0 and c_c(B)·q₀ > 0;
- A(s) → w′ and B(s) → w (normalised) as s → 0.

NUMERICS (1) confirms all of these at ε ∈ {.05, .3, .6, .9} and every failing pair (for ε = 0.9 at s ≤ 10⁻⁴; s₀ shrinks
as ε → 1). The distance to the crossings is O(s).

**Step 2 (uniform chart signs).** By (C3) (Lemma veccluster, applied at q₀ ∈ aff Δ), there are δ = δ(s) > 0 and balls
𝒜 := B(A, δ) and ℬ := B(B, δ) inside cone(int N₀) on which:
- the sign and ratio conditions hold for every pair (A′, B′) ∈ 𝒜 × ℬ;
- c(g)·q₀ > 0 for every good g ∈ 𝒜 ∪ ℬ.

**Step 3 (edge box with E allowed).** *Claim:* for a.e. (A′, B′) ∈ 𝒜 × ℬ, q₀ ∉ R(A′) ∩ R(B′).

*Proof of the claim.* Suppose q₀ lies in both charts, with A′ and B′ good.
- The charts are open cells of aff Δ, so O := R(A′) ∩ R(B′) ∩ Ω accumulates at q₀.
- At q ∈ O ∖ E, M3.7(a) gives P(q, A′) > 0 and P(q, B′) > 0. Fix λ > 0 with z′ := A′ + λB′ having z′_a, z′_b < 0, which
  the ratio condition allows. Concavity gives P(q, z′) > 0.
- Then z′ + (0, r)³ ⊆ D_{K_q}, a set of fixed positive measure inside B(z′, 2r).
- By Q4.0(c) (world b is non-degenerate), a.e. h ∈ B(z′, 2r) has 0 or − available. Either alternative is strictly
  better than + at both worlds a and b. So + is strictly q₀-suboptimal with a gap.
- So for each such h, no q-Bayes model accepts h once |q − q₀| < r(h). Dominated convergence then gives
  μ(B(z′, 2r) ∩ D_{K_q}) → 0 as q → q₀ through O ∖ E.
- This is a contradiction.

By Fubini, one of the two balls (call it G) has q₀ ∉ R(g) for a.e. g ∈ G.

**Step 4 (two-sidedness at the witnesses).** Take g ∈ G good, with + and 0 in A(g) (by (LF), since G ⊆ N). If − ∉ A(g),
then R(g) = {c·q > 0} ∋ q₀, a contradiction. So {+, 0, −} ⊆ A(g), and R(g) = {c·q > 0, d·q > 0}. From c·q₀ > 0 and
q₀ ∉ R(g) we get d·q₀ ≤ 0, hence c′·q₀ = c·q₀ − d·q₀ > 0.

On a mixed domain this is the first place where the layout bites: **near one of the two b-crossings the domain must be
two-sided a.e.** On M_U it fails here, which is Prop. T1's contradiction.

**Step 5 (one cut cell).** If d·q₀ < 0, then q₀ lies in the open cell R(−g) = {c′·q > 0, d·q < 0} of aff Δ. If
d·q₀ = 0, then d is non-constant on the edge line, because d_a and d_b have the strict signs of g_a and g_b, which are
opposite. Moving q₀ an arbitrarily small distance along the edge gives a point of the open cell.

Either way there is a non-empty open set of q ∈ Ω ∖ E within any prescribed distance of q₀ lying in R(−g). At each such
q, M3.7(a) for −g gives P(q, −g) > 0, i.e. **K_q ⊆ {m : m·g < 0}**.

NUMERICS (4): 438 random strict-sign instances, 0 failures to find such a q within 10⁻⁶.

**Step 6 (vertex continuity).** Take s_m ↓ 0, and g_m and q_m as in Steps 4–5 with |q_m − q₀(s_m)| < s_m. Pass to a
subsequence on which G is always the 𝒜-family or always the ℬ-family. Then:
- g_m → w\* ∈ {w′, w};
- |q_m − e_b| = O(s_m);
- K_{q_m} → V_b by Q4.0(a), with world b non-degenerate on all of M.

So **V_b ⊆ {m : m·w\* ≤ 0}**.

**Step 7 (test gambles).** Take h := w\* − δ𝟙 + ηe_b with 0 < δ < η small. Then h ∈ N, and h_b = η − δ > 0. For a.e. h′
near h, accept is available and world-b-correct, so it is the strict e_b-optimum, and D_{V_b} ∋ h′. Hence
V_b ⊆ {m·h ≥ 0}. Combined with Step 6:

  η m_b ≥ δ − m·w\* ≥ δ, so m_b ≥ δ/η, for every 0 < δ < η.

Letting δ/η → 1 gives **V_b = {e_b}**. NUMERICS (2): the LP value of max(1 − m_b) equals 1 − δ/η to within 10⁻¹³ at every
b-crossing and ε ∈ {.05, .3, .9}.

**Step 8 (availability).** The e_b-Bayes model is D_{e_b}, and it lies in 𝓜. So + ∈ A(g) for a.e. g with g_b > 0. This
holds for every b. Every mixed g and −g has a positive coordinate, so (Av) holds. Then M3.7(d) gives edge confinement and
K_q → {e_b}. ∎

**Remarks.**
- **Q4.5.** For additive covers (E = ∅), Q4.1 is a shorter proof of Cor. N21.7(a)–(c) and Cor. TSalways(b), (c). Of Thm
  cuts it uses only Step 1, and it needs neither Thm apex nor R4 Thm B.
- **It does not prove too much.**
  - It needs a failing box at b, and that is specific to the triangle: it comes from the corner equation via Prop. T1.
  - R10a Thm M's gauge-mixture covers of hexagons and 9-gons near T1 live on non-(Av) domains (Av = ∪ D_{V_i}, with V_i
    imprecise). They have no box witnesses with c > 0 at q₀ → e_b: Lemma edgebox forbids such witnesses, because
    K_{q₀} meets the edge.
  - On M_U the witnesses are one-sided, and Step 4 is already Prop. T1's contradiction.

---

## 3. M3.9 without (Av), and the corollary

**Lemma Q4.3 (UVN for every tie-breaking family; PROVED).** Let ψ be a non-degenerate (γ₀)-field on an (LF) domain,
x ∈ N mixed, and l a world.
- If x_l > 0, there are a ball B ∋ x and a relative neighbourhood V_l of e_l with P(q, h) > 0 for every q ∈ V_l ∩ Ω,
  every h ∈ B and every coherent tie-breaking. This includes K^♭, directional families, and K_q off E.
- If x_l < 0, the same holds with P(q, h) < 0.

*Proof.* By Q4.0(a), every family converges to V_l in Hausdorff as q → e_l. For x_l > 0, D_{V_l} contains a ball around
x, because acceptance is available and world-l-strictly best. So P_{V_l}(x⁻) > 0 for some x⁻ < x close to x. For
x_l < 0, D_{V_l} misses a ball around x, so P_{V_l}(x + δ𝟙) ≤ 0 and P_{V_l}(x) ≤ −δ. Uniform convergence of P on bounded
sets gives both claims. This is D1.1(c)'s argument; it uses no (Av). ∎

**Where M3.9 touched (Av).**
- M23_referee §6.10 found **no** use of (Av) in M3.9 except one. In checklist item (i) the reading obtained UVN for K^♭
  "from M3.7(d), since K^♭_q → {e_l} under (Av)". Q4.3 replaces this.
- Its other non-local inputs use no (Av). These are: quasi-concavity (D1.1(b), M3.7(a)); D1.6's walls across chords;
  N21.9(i)–(ii) (UVN, Lemma M); and TSalways steps (i)–(iv) (c-cluster signs, Lemma walls, surround).
- Edge confinement (M3.7(d)) is used only in M3.8, and is now supplied by Q4.1.

CHECKED (my reading of M3 §6 and M23_referee §6.10 for occurrences of "(Av)", "available", "advice range"). I did not
re-derive M3.9 itself.

**Proof of Corollary Q4.2.** Let ν be an endorser tuple whose field ψ := ψ^ν is non-degenerate.
- By M3.4, (γ₀) holds and T1 is Bayes at some p\* ∈ Ω.
- By D1, p\* ∉ E.
- By M3.6, M3.9 and Q4.3, (C2) and (C3) hold at p\*.
- By Q4.1, (Av) holds.
- So 𝓜 is an (Av)-domain, and M3.10 (M3.8 with M3.7(d)) gives a contradiction.

For rankings whose worlds all add up, M3.1's last clause makes ψ^{ν\*} non-degenerate. ∎

*Status.* This is that of M3.9, CHECKED. The open GAP is (ii) of M23_referee: Thm PL with approximate walls, generic o and
A. Q4.1 and Q4.3 have one reading (this note); D1, M3.4, M3.6–M3.8 have one reading each.

**Effect on R21.**
- Part B: (GnAv-nd) ✗ at this status. The configurations left are (GS), (GL) and (GnAv-d).
- §0 item 9 and §5 item 6: on off-M_U domains without (Av), rankings that add up are now excluded as well.

---

## 4. What a mixed layout would have to break, and what the computation shows

**Layouts, exactly.** Take any field with coherent vertex models. By R10a Thm V and Cor. V2(a) (whose proof needs only
vertex uniqueness and coherence, i.e. Q4.0), Av ∩ {g_b > 0} ≈ D_{V_b} with e_b ∈ V_b. So:
- (Av) fails at b ⇔ V_b ≠ {e_b};
- a non-(Av) layout is the same thing as an imprecise vertex model somewhere.

(LF) alone permits a fat V_b: V_b ⊆ W_b(N) := {m : m·h ≥ 0 for all h ∈ N with h_b > 0}. NUMERICS (3): at ε = 0.3,
W_b(ρ-tube) reaches distance ≈ 0.94–0.96 from e_b, for ρ ∈ {0.05, 0.01}. That is the U-domain's freedom.

**What breaks it.** One cut cell adds V_b ⊆ {m·w\* ≤ 0}. Then W_b(N) ∩ {m·w\* ≤ 0} = {e_b}. NUMERICS (3): extent
1.3·10⁻³, the test-gamble resolution used.

So the four inputs named in the brief stand as follows:

| input | needed by a non-(Av) cover broken? | status after Q4 |
|---|---|---|
| precise vertex limits | yes, at some b (equivalent to non-(Av) at b) | forced by Q4.1 from (PC) + cluster clause at p\* |
| edge confinement | follows from (Av) (M3.7(d)) | forced |
| cuts (Thm N21.6 Steps 3–7, Thm apex) | not needed by anyone | irrelevant |
| (TS), (PC), (NS) at p\* | the only input left to break | proved for every non-degenerate field, layout-free (M3.6, M3.9 + Q4.3) |

**Search (NUMERICS (5)).** Layouts were sampled through their exact parametrisation, imprecise V_b ⊆ W_b(ρ). For each
of 900 sampled imprecise vertex models at each ρ ∈ {0.05, 0.01}, I tested Q4.1's Step-6 conclusion: is V_b ⊆ {m·w\* ≤ 0}
for some b-crossing w\*? **0 survivors.**

A search over penalty fields was not run. Q4.1 makes it moot. Any non-degenerate field that has T1 as a Bayes model at an
interior p\* produces the box witnesses of Step 1 at every vertex, and (1) confirms these at every ε tested. Its vertex
models are then precise, whatever the layout and whatever E is.

**Exceptional chords (the mechanism the brief proposed).** Chords off p\* with coexisting coherent and incoherent
minimisers do not help. Steps 3 and 5 use only priors off E, and E is null. Step 6 uses the vertex margin, which no tie
at an interior or edge prior affects. The ordinal tie-break of N26.1 acts on E. Q4.1 never evaluates the ranking on E.

---

## 5. Degenerate fields: where the blindness must sit

**Proposition Q4.4 (PROVED).** Let ψ be an integral (γ₀)-field on an (LF) domain, possibly degenerate, with (γ) on Ω.
Fix b and an edge [e_a, e_b]. Assume:
- **[W_b] (box-witness structure at e_b).** For a sequence s_m ↓ 0 there are non-null 𝒜_m, ℬ_m ⊆ N in the sign
  classes {g_a < 0 < g_b} and {g_b < 0 < g_a}, converging to the b-crossings w′ and w respectively. Every pair satisfies
  the box ratio. Moreover c(g)·q₀(s_m) > 0 for a.e. g ∈ 𝒜_m ∪ ℬ_m (c = ℓ(0) − ℓ(+)).
- **[B_b].** World b's ladder density is > 0 a.e. on some neighbourhood of {w′, w}.
- **[G_ab].** For a.e. mixed h with h_a, h_b < 0 near the box combinations A′ + λB′, at least one of worlds a, b strictly
  penalises + relative to every available alternative.

Then some coherent e_b-Bayes model is D_{e_b}. So + ∈ A(g) for a.e. g with g_b > 0.

*Proof.* Steps 3–8 of §2, with three changes.
- Step 3 uses [G_ab] for the gap, and Q4.0(b), (c) with G a neighbourhood of a crossing, from [B_b].
- Step 5 uses [B_b]: d_b = ±(s_b + w_b) ≠ 0, so d is non-constant on the edge.
- Step 6 replaces vertex continuity by Q4.0(d). Some subsequence of the q_m-Bayes models converges to a coherent
  e_b-Bayes model X\*, with credal set K\* ⊆ {m·w\* ≤ 0}.
- Step 7 is unchanged, using s_b > 0 at the test gambles (from [B_b]): K\* = {e_b}. ∎

**Consequence for (GnAv-d).** At every vertex b where (Av) fails, a degenerate cover must violate [W_b], [B_b] or
[G_ab]:
1. **[B_b] fails:** world b is blind on some step for gambles in every neighbourhood of a b-crossing. That is
   silence-blindness at the target's boundary, the M3.11 / L4 configuration-(I) mechanism moved to the crossings.
2. **[G_ab] fails:** worlds a and b are jointly blind on a non-null set of the joint T1-error set J_c near the segment
   (w′, w). This is the joint blindness that M3.4.4 forces when p\* ∈ (e_a, e_b); compare configuration (E).
3. **[W_b] fails.** With a non-degenerate restriction near p\*, [W_b] comes from (PC), so failure needs one of:
   - p\* ∈ ∂Δ;
   - blindness on near-facet gambles that destroys (C2)/(C3);
   - (TS) failing for a degenerate field.

CONJECTURE (not attempted): each of 1–3 is the general-domain image of an M_U configuration (V), (E) or (X). If so, the
M_U open questions Q_N2⁽³⁾, Q_V+ and Q_N1 govern (GnAv-d) too.

No degenerate construction was attempted to completion. No full three-world system with a ladder-blind world is known on
any domain (R21 §2), and Q4.4 says only where such a world's blindness would have to be.

---

## 6. Ledger and referee priorities

**New, unrefereed, in order of risk.**
1. Q4.1 Step 3: the edge box with E ≠ ∅ on a general domain. The inputs are M3.7(a) at q ∉ E, Lemma FS by dominated
   convergence, and V1 via Q4.0(b), (c).
2. Q4.1 Step 6 / Q4.0(a): vertex continuity for every tie-breaking family. It is the R10b V2 / D1.1(c) argument, with
   E irrelevant.
3. Q4.3, and the CHECKED claim that M3.9 uses (Av) nowhere else.
4. Q4.4: the bookkeeping of the hypotheses [B_b] and [G_ab].

**Corrections to earlier notes.**
- M3 §7 / Conjecture M3.C: its reduction is now complete. The availability half needs only Step 1 of N21.6. The apex, Thm
  B and Hausdorff limits along [a\*, z\*] are not needed. With M23_referee's fix (M3.9 without (Av), §3 above), M3.C's
  purpose is served at the status of M3.9.
- R21 Part B: (GnAv-nd) is closed at that status.

---

## 7. Files (`q4py/`)

- `q4_checks.py` (+ `q4_checks.out`), five checks:
  1. Box witnesses for every failing pair at ε ∈ {.05, .3, .6, .9}: membership, signs, chart values, ratio, and
     convergence to the b-crossings. The c-values for (1,2) are exact in sympy.
  2. LP for Step 7: max(1 − m_b) = 1 − δ/η within 10⁻¹³.
  3. W_b(ρ) is fat (≈ 0.94–0.96); it collapses to 1.3·10⁻³ after one cut cell.
  4. Step-5 geometry: 438 instances, 0 failures.
  5. Layout search: 1800 imprecise LF-compatible vertex models, 0 survivors.
