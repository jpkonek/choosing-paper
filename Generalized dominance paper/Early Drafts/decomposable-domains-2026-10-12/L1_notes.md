# L1. Question Q_A for T1: weak fields do not cover T1

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here from results the write-up
or K3/K3_referee mark proved, each named), **CHECKED** (verified step by step, not written out in full),
**CONJECTURE**, **NUMERICS** (scripts in `l1py/`, run with `python3 -I` from inside `l1py/`; no proof depends
on them). No assumption is added. Notation: write-up §§2–4, §7.5–7.7; K3_notes §§5–6; K3_referee §7.
Facets of D_{T1} are parametrised as in write-up §4.1: F1 from r12 (τ = 0) to r31 (τ = 1), F2 from r12 to r23,
F3 from r23 to r31. Pinned crossings are crossings of coordinates 2 or 3; coordinate-1 crossings are w12 ∈ F2
(between (−,−,+) and (+,−,+)) and w13 ∈ F3 (between (−,+,−) and (+,+,−)).

---

## 0. Outcome

**Q_A has answer NO. Theorem M0closed(a) holds for weak fields: a weak field with property (γ) never has D_{T1}
as a Bayes model at an interior weighting.** Status: the new parts (A, B below) are PROVED, except that case (b2) uses Lemma L1.7 (Steps 1 and 3 of
Thm. pivot on F1 for weak fields), which is CHECKED. The final assembly (Part C: the existing §4/§7.7 chain run
on a field whose blind set touches ∂D_{T1} on at most finitely many rays) is CHECKED. With K3.7 this closes the blind-set route for T1: next to two integrable
worlds that endorse all their relevant comparisons, the third world of a cover is (M1) or has
Λ_∞ ⊇ E₁(T1) ∩ M (the boundary case p* = e₁ of K3.7(γ)).

**Theorem L1.** Let c = (ρ₁σ₁, ρ₂σ₂, ρ₃σ₃) be measurable on U, with ρ₂, ρ₃ > 0 a.e., ρ₁ > 0 a.e. on M ∖ Λ and
ρ₁ = 0 on a non-null Λ ⊆ M. Suppose B_t is coherent for a.e. t ∈ Δ° (property (γ)). Then there is no p* ∈ Δ°
with D_{T1} = B_{p*} ∪ S, S ⊆ Z_{p*}. (Integrability is not used.)

Why this is not routine (and why the answer is not decided by the old algebra):

1. **Blind sets can defeat the corner/box algebra** (Prop. L1.2; PROVED as algebra, NUMERICS for the
   non-crossing boxes). If Λ contains conic neighbourhoods of the two coordinate-1 crossings w12 and w13, the
   facet chords there are pinned to the *vertex chord* R* := line(e₁, p*) (§1.4). This deletes the corner
   equations at r12 and r31 and moves the coordinate-1 crossing rows to "virtual crossings". The resulting
   corner + box system is **consistent for every ε ∈ (0,1)**. So Q_A is genuinely beyond M0closed(a), as the K3
   referee said, and any proof must use something other than x + 1/x = κ + 1 against the box.
2. **What kills it is frozenness along the vertex chord** (Lemma L1.6, Theorem L1.A). On Λ the Bayes sets
   depend on t only through θ = t₂/(t₂+t₃). So along R*, and along nearby rays from e₁, the Bayes model is
   frozen on Λ all the way up to the vertex e₁. Concavity along the facet then carries a zero (or a two-sided
   small value) from the blind arc to the whole facet. But the facet also contains a gamble that world 1 (on
   F2, F3: the (+,−,−) corner portion near r23) or worlds 2 and 3 (on F1: the middle arc) force to be accepted
   on every ray. Ties on R* ("vertex atoms") are handled by face models and crosspin at the pinned crossings.
3. **Consequence (Corollary L1.B, PROVED).** Near ∂D_{T1} the blind set lies inside E₁(T1), contains no facet
   arc and is adjacent to none; it can touch ∂D_{T1} only on finitely many rays. On such fields the chain of
   write-up §4 and §7.7 needs world-1 strictness only at generic facet points and at "good halves" of
   crossing balls, which are available (Part C).

| | Statement | Label |
|---|---|---|
| L1.1 | Bayes models, vertex fan at e₁, vertex chords; necessary conditions (N1)–(N4) | PROVED |
| L1.2 | corner + box algebra with R*-arcs at w12 and w13 is consistent for every ε | PROVED (algebra); NUMERICS (all boxes, ε = 0.3) |
| L1.3 | crossing-box formula (Box_{a,b}); recovers 1/κ ≤ x_k x_{k+1} ≤ κ | PROVED |
| L1.4 | tools for weak fields: every B_q coherent; face models; weak ball lemma; crosspin at pinned crossings; local UVN at e₁ | PROVED (from cited results) |
| L1.5 | facet classification of Λ by concavity of P_{K*} | PROVED |
| L1.6 | frozen-along-R* and frozen-along-rays lemma | PROVED |
| L1.7 | Steps 1, 3 of Thm. pivot on F1 for P♭ of a weak field | CHECKED |
| L1.A | (a) no facet arc lies in int Λ; (b) no facet arc is one-sidedly adjacent to Λ | (a) PROVED; (b) PROVED, (b2) modulo L1.7 |
| L1.B | Λ touches ∂D_{T1} on finitely many rays; half-collar Λ ⊆ E₁(T1) near ∂D_{T1} | PROVED |
| L1.C | §4 + §7.7 chain for fields with finitely many touching rays | CHECKED (audit table §5) |
| L1 | Q_A: no | PROVED modulo L1.7 and L1.C (both CHECKED) |
| L1.D | several blind sets Λ₁, Λ₂, Λ₃ | necessary conditions PROVED; exclusion CONJECTURE (§6.3) |

---

## 1. Bayes models of weak fields and what changes in the chart geometry

Standing data: c as in Theorem L1, with (γ) and (TB): D_{T1} = B_{p*} ∪ S, S ⊆ Z_{p*}, p* ∈ Δ°. By
Prop. reduction(d) (rescaling p* ⊙ c, which keeps ρ₁ = 0 exactly on Λ and fixes the vertices) we may take
p* = u whenever convenient; nothing below depends on that except §§1.5–1.6 (algebra). Write
θ(q) := q₂/(q₂+q₃) ∈ (0,1) and θ* := θ(p*).

### 1.1 Bayes models (PROVED, elementary)

For q ∈ Δ°: B_q = {g ∈ U : q₁ρ₁σ₁·1_{M∖Λ} + q₂ρ₂σ₂ + q₃ρ₃σ₃ > 0} (and B_q ⊇ N₊).
- **On Λ the advice depends on q only through θ(q):** q·c(g) = (q₂+q₃)(θρ₂σ₂ + (1−θ)ρ₃σ₃).
- On Λ ∩ {σ₂ = σ₃}, i.e. Λ ∩ ((+,−,−) ∪ (−,+,+)), the advice is constant in q: (+,−,−) is never accepted, (−,+,+)
  always.
- On Λ ∩ R₂₃ the advice is monotone in θ: increasing on (·,+,−), decreasing on (·,−,+).
- Ties of Λ-gambles: Z_q ∩ Λ = {ρ₃/ρ₂ = θ/(1−θ)} ∩ R₂₃ — they have c ∝ ±b_v(θ), b_v(θ) := (0, 1−θ, −θ).

### 1.2 Charts and the vertex fan (PROVED)

- For g ∈ Λ ∩ R₂₃ the chart H(g) = {q·c(g) > 0} is a half-plane whose boundary passes through **e₁**: a *vertex
  chord*. Its sides are θ-sectors {θ < θ_g} or {θ > θ_g}. For g ∈ Λ ∩ {σ₂ = σ₃}, H(g) is ∅ or Δ°.
- Lemma UVN at e₁ (write-up Lemma UVN) holds at a mixed x exactly when some ball around x meets Λ in a null
  set (the proof is dominated convergence of q·c(g) → c₁(g) as q → e₁, which needs c₁ ≠ 0 on the ball). At
  e₂, e₃ it holds everywhere (ρ₂, ρ₃ > 0).
- **No single vertex model at e₁.** As q → e₁ along the ray {θ = θ₀}, B_q → S_{θ₀} in measure, where S_θ = P₁ on
  M ∖ Λ and G_θ := {θρ₂σ₂ + (1−θ)ρ₃σ₃ > 0} on Λ (K3.7(β)). S_θ is coherent for a.e. θ (K3.7(β)). So
  Prop. reduction(c) fails at e₁ unless Λ ∩ R₂₃ is null, and q ↦ K_q has a *fan* of limits at e₁.
- **Atoms.** An oriented atom inside Λ has normal b with b₁ = 0, so its chord passes through e₁ (a *vertex atom*;
  K3_referee (Q3)). This is the failure of Thm. Estructure(b) ("ℓ_k misses the vertices"). A vertex atom at p*
  lies on R* := {θ = θ*}, the line through e₁ and p*.

### 1.3 Necessary conditions (PROVED; the list the brief asks for)

- **(N1) Rigidity** (K3.7(β′); its proof uses only (γ) and ρ₂, ρ₃ > 0): Λ ∩ R₁ⱼ = E₁(C₁ⱼ) ∩ R₁ⱼ for coherent
  C₁₂ = D_{K₁}, C₁₃ = D_{K₀} with K₁ ∩ [e₁,e₂] ≠ ∅, K₁ ⊆ co(K′ ∪ [e₁,e₂]), K₀ ∩ [e₁,e₃] ≠ ∅,
  K₀ ⊆ co(K′ ∪ [e₁,e₃]); D_{K₁} = D_{K₀} on (+,−,−) ∪ (−,+,+). In an orthant O with g₁ > 0, Λ ∩ O = O ∖ D_{K*}; with
  g₁ < 0, Λ ∩ O = D_{K*} ∩ O (K* = K₁ on R₁₂-orthants, K₀ on R₁₃-orthants). In particular Λ is a union of cones.
- **(N2)** (K3_referee (Q1)) Λ ∩ (+,−,−) ⊆ U ∖ D_{T1} and Λ ∩ (−,+,+) ⊆ D_{T1}.
- **(N3)** (K3_referee (Q2)) a coherent C* equal to P₁ on M ∖ Λ and to T1 on Λ ∖ Z_{p*}. Then K* ⊆ co(T1 ∪ {e₁})
  and D_{K*} ∩ {g₁ < 0} ⊆ D_{T1} (because E₁(C*) ⊆ E₁(T1)).
- **(N4) Exclusions from "between".** v₃ ∉ co(K′ ∪ [e₁,e₂]) ⊇ K₁ and v₂ ∉ co(K′ ∪ [e₁,e₃]) ⊇ K₀: the third coordinate
  (resp. second) of v₃ (resp. v₂) is c₀ + ε, which exceeds its maximum 1/3 + s(c₀ + ε − 1/3) over K′ and its
  value 0 on the edge.
- **(N5)–(N6)** (new, from Part B): Λ contains no facet arc in its interior and is adjacent to no facet arc; near
  ∂D_{T1} it lies inside E₁(T1) and touches ∂D_{T1} on finitely many rays (Corollary L1.B).

Theorem L1 says that (N1)–(N6) together with (γ) are inconsistent. **So the brief's Stage-B question ("what a
world-1 order must do on Λ: strict (G) with zero exchange rate") has no instance to serve.**

### 1.4 R*-arcs, virtual crossings, and the corner equation (PROVED)

Call an open facet arc J an **R*-arc** if some conic neighbourhood N of J satisfies N ⊆ Λ (mod null). By §1.1,
for h ∈ J, P(q, h) near level 0 is determined by B_q ∩ N, hence by θ(q). So every chart line of every level
near 0 passes through e₁. If the facet chain of §4 held at J, its chord would be R*, its zero set R* (or a
θ-wedge), and its two-slope data would have constant direction.
- **Virtual crossing.** If a rotating piece of the facet ends at an endpoint a of an R*-arc and the chord is
  continuous there (Thm. pivot Step 3), then its coordinate-1 row vanishes at h(a). It no longer vanishes at the
  true coordinate-1 crossing.
- **Corner equations.** A corner ray inside an R*-arc carries no corner equation. A piece without any true
  crossing of a coordinate has that row free, subject only to sign.
- **Boxes.** The edge box (write-up Lemma edgebox) survives on the half-open edges: if a = 1 or b = 1 and
  A + λB ∈ Λ, then c(A+λB) is ≤ 0 on [e_a, e_b] with equality only at e₁. With A ∈ U ∖ Λ and B ∈ Λ it reproduces the
  "between" condition K₁ ∩ [e₁,e₂] ≠ ∅ of K3.7′ and nothing new.

**Which placements of R*-arcs are combinatorially possible** (from (N1)–(N2)):
- they never contain a pinned crossing: one side would be (+,−,−) or (−,+,+), where (N2) forbids int-Λ facet
  points;
- on F1 they lie in a corner portion;
- on F2 and F3 they lie in R₂₃-portions, around or beside w12, w13.

---
### 1.5 The crossing boxes (Lemma L1.3; PROVED)

Let b be a coordinate and a ≠ b. Let w_A and w_B be crossings of coordinate b on rotating facet pieces, with
w_{A,a} < 0 < w_{B,a}. Write the facet data near each as c_b(h) = λ h_b (pinned row) and c_a(w) for the a-row at
the crossing. Then Prop. boxbridge(c) holds for all pairs near (w_A, w_B) iff

  **(Box_{a,b})**  λ_B · |c_a(w_A)| · w_{B,a}  ≥  λ_A · c_a(w_B) · |w_{A,a}| .

*Proof.*
- Take A on the facet near w_A with A_b = η > 0 and B near w_B with B_b = −ζ < 0, and put q₀ = (1−s)e_b + s e_a.
- Then c(A)·q₀ = (1−s)λ_Aη + s c_a(A), positive iff s/(1−s) < λ_Aη/|c_a(A)|.
- Likewise c(B)·q₀ = −(1−s)λ_Bζ + s c_a(B), positive iff s/(1−s) > λ_Bζ/c_a(B).
- The ratio condition A_bB_a < |A_a||B_b| reads η/ζ < |A_a|/B_a.
- So a violating pair exists for small η, ζ iff (λ_B/c_a(w_B))·(|c_a(w_A)|/λ_A) < |w_{A,a}|/w_{B,a} (all quantities
  are continuous at the crossings).
- The normalisations of the two facets cancel. ∎

*Check.* In the strict case (write-up Prop. T1 normalisation) the six instances are exactly x_k x_{k+1} ≤ κ and
x_k x_{k+1} ≥ 1/κ, i.e. Lemma P1box's six bounds.
- E.g. b = 3, a = 2: w_A = w32 = (κ,−1,0), w_B = w31 = (−1,κ,0), λ_A = x₂, c₂(w32) = −κ, λ_B = 1, c₂(w31) = x₁κ.
  This gives 1·κ·κ ≥ x₂·x₁κ·1, i.e. x₁x₂ ≤ κ.

*NUMERICS caveat.* Grid checks of the boxes systematically miss these crossing limits. `l1py/verify_F3J.py`: a
configuration with x₁x₂ = 2.44 > κ passed a 60×100 grid and failed only weakly (+0.002) on 150×400. So every
feasibility claim below uses (Box_{a,b}) exactly, and grids are used only for the boxes away from crossings.

### 1.6 Two R*-arcs defeat the algebra (Prop. L1.2; PROVED as algebra)

**Configuration.** R*-arcs J ∋ w12 on F2 and J′ ∋ w13 on F3 (orientations: chord R* with e₃ on the positive
side on J, and e₂ on J′). F1 is strict. F2 has rotating pieces [0, a) and (b, 1]; F3 has [0, a′) and (b′, 1].
Facet data:
- F1: c = (−(x₁h₂ + h₃), x₁h₂, h₃).
- F2 on (b,1]: c₁ = (κ+2)(τ−b)/(1−b), c₃ = x₂h₃.
- F3 on [0,a′): c₂ = h₂, c₁ = N(a′−τ)/a′.
- The pieces of F2 on [0,a) and F3 on (b′,1] are free affine fields with the strict signs, ending on (0,−1,1) and
  (0,1,−1) at the arc ends and parallel to F1's data at r12 and r31.

**Constraints.**
- Corner r23: x₂ = (κ+2)(1 − 1/N).
- Crossing boxes, with m₃ := (κ+2)(τ₃−b)/(1−b) and M := N(a′−τ₂)/a′:
  - b = 2: 1 ≤ x₁M ≤ κ²;
  - b = 3: m₃/κ² ≤ x₁x₂ ≤ m₃;
  - b = 1: involves only R*-arc gambles, whose charts on the edges [e₁,e₂], [e₁,e₃] are one-signed. There is no
    constraint.
- Corner signs at r12 and r31: 1/(κ+1) < x₁ < κ+1.

**Claim: for every κ > 1 these are simultaneously satisfiable.**
- Let b ↓ τ₁ and N → ∞. Then x₂ → κ+2 and m₃ → κ(κ+2)/(κ+1).
- So the b = 3 boxes allow every x₁ ∈ [1/(κ(κ+1)), κ/(κ+1)] (with slack). This meets the corner window
  (1/(κ+1), κ/(κ+1)).
- M ranges over (0, N(1 − τ₂/τ₁)) as a′ varies, so x₁M ∈ [1, κ²] is attainable for N large. ∎

At ε = 0.3, `l1py/explicit_twoarc.py` takes x₁ = 0.5, b = τ₁ + 0.02, a′ = τ₁ − 0.02, N = 5 (so x₂ = 3.43). It
checks:
- all strict signs on all pieces;
- corner r23 to 10⁻³²;
- the four crossing boxes exactly;
- every sampled box on 200×600 grids (worst value −0.0012 ≤ 0).

So **no contradiction can come from corner equations and boxes alone** once Λ holds neighbourhoods of w12 and
w13. Single arcs do not suffice:
- the configurations "corner r12 (or r31) inside an R*-arc" (F1 + F2, or F1 + F3) violate the boxes at
  ε = 0.1, 0.3, 0.6 (`facet_algebra.py`, `run_r12end_J0_strict.out`, `run_r31end_strict_J1.out`: worst box
  ≥ 0.046);
- a single arc at w13 (F2 strict at w12) is already inconsistent with (N1): it forces P_{K₁}(w13) > 0 and
  P_{K₁}(w12) ≥ 0, and K₁ ∩ [e₁,e₂] = {e₁} then contradicts P_{K₁}(w13) > 0.

---

## 2. NUMERICS (guidance only)

- **Random weak fields** (`field_search.py`): six homogeneous weak fields.
  - Construction: rigid Λ from K₁ = co(K′ ∪ {e₁, m₁}), K₀ = co(K′ ∪ {e₁, m₀}); live densities exp(linear); world-1
    density solved so that T1 is exactly Bayes at u.
  - Midpoint-convexity violations in B_t occur at 67–82% of the grid weightings, with mean rate 0.008–0.024,
    against a coherent baseline of 0.0000.
  - Diagnosis: such fields are nowhere near realisations, with or without Λ, so random search is uninformative.
    The informative object is the facet algebra.
- **Facet algebra.**
  - `facet_algebra.py` reproduces the strict contradiction (both corner solutions x± violate a box, at ε = 0.1,
    0.3, 0.6) and the failure of "corner r12 in an R*-arc".
  - `facet_configs.py` / `run_one.py` scan R*-arc placements. Grid artifacts are noted in §1.5.
  - `explicit_twoarc.py` gives the consistent two-arc solution of Prop. L1.2.
- **Lesson used in the proof.** The two-arc configuration survives every algebraic test. So the obstruction must
  be non-algebraic: it is the vertex-e₁ positivity along R* (Lemma L1.6, Theorem L1.A).

---

## 3. Tools for weak fields

**Lemma L1.4 (PROVED).** Under the standing data:
- **(a)** For every q ∈ Δ°, B_q is coherent, B_q = D_{K♭_q}, and q ↦ K♭_q is upper semicontinuous.
  - For generic δ ∈ 𝟙^⊥, B_q ∪ (Z_q ∩ {δ·c > 0}) =: D_{K^δ_q} is coherent.
  - At q = p* these directional limits K_δ are **p*-face models**: D_{K_δ} △ D_{T1} ⊆ Z_{p*}.
  - *Proof:* write-up Thm. Estructure(d) and N25 Lemma 3.1. They use only (γ), Fubini in polar coordinates
    around q, and c(g) ∦ 𝟙 on mixed g. The last holds for weak fields: (0, ρ₂σ₂, ρ₃σ₃) ∦ 𝟙.
- **(b)** (Quasi-linearity; write-up Lemma quasilin(a) with A = ∅.) For every g, q ↦ P♭(q,g) has convex level sets.
  {P♭(·,g) > 0} is open, since P♭ is lower semicontinuous by (a). The proof uses only that {q : g ∈ B_q} is an
  open half-plane, ∅ or Δ°.
- **(c)** (Local UVN.) If a ball B(x, r) ⊆ U meets Λ in a null set and x₁ > 0 (resp. < 0), then
  P♭(q, x) > t > 0 (resp. < −t) for all q ∈ Δ° near e₁, in every direction.
  - At e₂ and e₃ this holds for every x with x₂ ≠ 0 (resp. x₃ ≠ 0).
  - *Proof:* q·c(g) → c₁(g) pointwise on the ball as q → e₁. So B_q ∩ B(x,r) → B(x,r) ∩ {g₁ > 0} in measure, and an
    open convex cone containing all but a small part of a ball contains a smaller concentric ball.
- **(d)** (Weak ball lemma.) If O ⊆ U is open and connected and O ⊆ Z_x mod null for some x ∈ Δ°, then c(g), g ∈ O,
  are a.e. positive multiples of one vector b.
  - Hence O cannot contain non-null parts of both Λ (where b₁ = 0) and M ∖ Λ (where c₁ ≠ 0).
  - Nor can it straddle {g_c = 0} for c ∈ {2,3} (c_c changes sign).
  - *Proof:* write-up Lemma ball, steps 1–4 of Prop. F (N25_referee §2), which use only (γ), the half-plane charts
    and the 1-Lipschitz dependence of P on g. Local constancy on a connected set gives one vector. Only the final
    "strict signs give the orthant" sentence is signed, and it is replaced by the two consequences stated.
- **(e)** (Crosspin at pinned crossings.) Every p*-face model K has P_K(w) = 0 at every pinned crossing w (w_c = 0,
  c ∈ {2,3}).
  - At a coordinate-1 crossing w the same holds unless, for every small s, the ball used in write-up
    Prop. crosspin lies in Λ mod null.
  - *Proof:* the crosspin construction gives a ball in Z_{p*} centred on {g_c = 0}, against (d).

**Lemma L1.5 (facet classification; PROVED).** Fix a facet F_k and an open orthant O. On the arc F_k ∩ O put
f(τ) := P_{K*}(h(τ)) (K* from (N1)); f is concave. For a facet point h = h(τ) in O:
- g₁ > 0 on O: f(τ) < 0 ⇒ h is an **int-Λ point** (a conic neighbourhood lies in Λ); f(τ) > 0 ⇒ h is **strict** (a
  neighbourhood misses Λ); f(τ) = 0 ⇒ near h, Λ is the part of O outside D_{K*}.
- g₁ < 0: the same with the signs of f reversed (Λ ∩ O = D_{K*} ∩ O).
- If f ≡ 0 on an open interval, then v_k ∈ K* and K* lies in the polar wedge of that interval. Locally
  D_{K*} = D_{T1}, and Λ is **one-sidedly adjacent** to the arc: outside T1 if g₁ > 0, inside if g₁ < 0.
- By (N2), f ≥ 0 on (+,−,−)-arcs and f ≤ 0 on (−,+,+)-arcs. By (N4), f ≢ 0 on any interval of:
  - F2 ∩ (−,−,+) (needs v₂ ∈ K₀);
  - F3 ∩ (−,+,−) (needs v₃ ∈ K₁);
  - F2 ∩ (+,−,−) and F3 ∩ (+,−,−) (K₁ = K₀ there, which would need v₂ ∈ K₀ or v₃ ∈ K₁).
- Hence, in particular, (+,−,−)-arcs have no int-Λ points and at most two non-strict points per arc.

*Proof.*
- Rigidity gives the orthant description, and D_{K*} is open convex with continuous P_{K*}.
- f ≡ 0 on an interval: K* ⊆ {m·h ≥ 0 for h in the interval}, a wedge with apex v_k, and the minimum is attained
  only at v_k for interior h. So v_k ∈ K* and P_{K*}(g) = v_k·g near the arc.
- A concave f ≥ 0 vanishing at three points vanishes on an interval. ∎

**Lemma L1.6 (frozen along rays from e₁; PROVED).** Let N be a conic neighbourhood of a compact facet arc J₀ with
N ⊆ Λ. Then for q, q′ ∈ Δ° with θ(q) = θ(q′): B_q ∩ N = B_{q′} ∩ N and Z_q ∩ N = Z_{q′} ∩ N. So for h ∈ J₀,
P♭(q, h) (when |P♭| < s₀, where h ± s₀𝟙 ∈ N) is a function of θ(q) alone. In particular, on R* ∩ Δ° it equals
P♭(p*, h).
*Proof.* §1.1: on Λ, q·c(g) = (q₂+q₃)·(θρ₂σ₂ + (1−θ)ρ₃σ₃). Local determination: P_K(h) = sup{s : h − s𝟙 ∈ D_K}. ∎

---
## 4. The blind set cannot reach the target boundary along an arc

**Auxiliary positive gambles (PROVED, from L1.4(b),(c), L1.5).** For each facet there are h₀ on the facet line
(the line through its two corner rays), t > 0 and an open W ⊆ Δ° meeting **every** ray {θ = const} from e₁,
such that P♭(q, h₀) ≥ t on W:
- **F1:** h₀ any middle-arc point. UVN at e₂, e₃ gives P♭ ≥ t on V₂ ∪ V₃. By quasi-concavity this extends to
  W := conv(V₂ ∪ V₃) ∩ Δ°, a strip along the open edge (e₂, e₃).
- **F2, F3:** h₀ a strict point of the (+,−,−) arc. UVN at e₁ gives W := V₁ ∩ Δ°.

On F1 the auxiliary gamble is forced positive by worlds 2 and 3 near the opposite edge. On F2 and F3 it is
forced positive by world 1 near its own vertex.

**Lemma L1.7 (Steps 1 and 3 of Thm. pivot on F1, for P♭; CHECKED).** For every τ ∈ (0,1),
A_τ := {P♭(·, h(τ)) > 0} is Δ° ∩ an open half-plane with p* on its boundary line λ_τ, and τ ↦ λ_τ is continuous.

*Check.*
- Step 1 is Lemma nopin applied to a bracket around w21 (shared positive coordinate 3) or w31 (shared positive
  coordinate 2). Its inputs:
  - UVN at e₂, e₃ (L1.4(c));
  - Lemma PL2 at a crossing of coordinate c ∈ {2,3}, which uses UVN at e_c and sign(c_c(h)) = sign(h_c) for
    h ∈ U⁻ — true also on Λ;
  - "pick j with w_j > 0" with j ∈ {2,3};
  - the chainchords version of PL2 for K♭, which uses the ball lemma on a ball centred on {g_c = 0}, c ∈ {2,3}
    (L1.4(d)).
- Step 3 uses only Step 1 and convexity of zero sets (L1.4(b)). No input involves world 1.

**Theorem L1.A.**
- **(a) (PROVED)** No facet point of D_{T1} is an int-Λ point.
- **(b) (PROVED; (b2) uses L1.7)** No open facet arc is one-sidedly adjacent to Λ.

*Proof of (a).*
- Suppose h(τ₀) ∈ F_k is an int-Λ point. By L1.5 there are a compact arc J₀ ∋ τ₀ of int-Λ points inside one
  open orthant O with σ₂ ≠ σ₃ on O, and a conic neighbourhood N ⊆ Λ of J₀ inside O. On N:
  - Z_{p*} ∩ N = {c ∝ ε b_v}, with b_v := b_v(θ*) and ε = ±1 fixed by O.
  - For generic δ, K_δ restricted to N is L₊ := B_{p*} ∩ N if εδ·b_v < 0, and L₋ := (B_{p*} ∪ Z_{p*}) ∩ N if
    εδ·b_v > 0.
  - Both are face models (L1.4(a)), so P_{L₊} ≤ 0 ≤ P_{L₋} on J₀.
- **Case 1: P_{L₋} ≡ 0 on a subarc J₁.**
  - Let θ → θ* from the side on which Λ-ties are accepted. By §1.1 the sets G_θ ∩ N decrease monotonically to
    L₋, in measure.
  - By L1.6, for every q on the ray {θ}, P♭(q, h) = f_θ(h) for h ∈ J₁, and f_θ → P_{L₋} = 0 pointwise. These
    are concave functions of τ, so the convergence is uniform on a compact J₂ ⊂ J₁.
  - Concavity along the whole facet line gives P♭(q, h(τ)) ≤ η(1 + 2 dist(τ, J₂)/|J₂|) ≤ Cη for τ ∈ [0,1], where
    η := sup_{J₂}|f_θ|.
  - Take q ∈ W ∩ {θ} and the auxiliary h₀: then t ≤ P♭(q, h₀) ≤ Cη, false for θ close to θ*.
  - (This contains the tie-free case L₊ = L₋.)
- **Case 2: P_{L₋}(h(τ_R)) > 0 at some τ_R ∈ J₀.** Take a generic δ on the L₋ side.
  - **F1.** J₀ lies in a corner portion, outside [τ₂, τ₃]. P_{K_δ}∘h is concave with zeros at τ₂, τ₃ (L1.4(e)), so
    it is ≤ 0 outside [τ₂, τ₃]. This contradicts P_{K_δ}(h(τ_R)) > 0.
  - **F2.** J₀ ⊆ (0, τ₃), and P_{K_δ} vanishes at τ₃ and is > 0 at τ_R. By concavity P_{K_δ} < 0 on (τ₃, 1].
    - Choose a compact arc I ⊆ (τ₃, 1) of strict points (L1.5) and the shell
      Sh := {h + s𝟙 : h ∈ I, 0 < s < s₁}, with s₁ small. Sh is open, connected, contained in
      (+,−,−) ∩ D_{T1} ∖ D_{K_δ} ⊆ Z_{p*}, and disjoint from Λ (by (N2)).
    - By L1.4(d), c ∝₊ b on Sh, with b strictly signed.
    - Take a generic δ′ with δ′·b > 0 and εδ′·b_v > 0. This is possible, since b₁ ≠ 0 = (b_v)₁, so b ≠ −λb_v.
    - Then D_{K_{δ′}} ⊇ Sh, so P_{K_{δ′}} ≥ 0 on I. Also P_{K_{δ′}} = P_{L₋} > 0 at τ_R, and P_{K_{δ′}} = 0 at τ₃,
      with τ_R < τ₃ < I. This is impossible for a concave function.
  - **F3.** The same argument with τ₂ and the arc [0, τ₂). ∎

*Proof of (b).* By L1.5 the possible adjacency arcs are:
- F2's middle arc ((+,−,+); Λ outside T1);
- F3's middle arc ((+,+,−); Λ outside);
- arcs of F1 (Λ inside).

**(b1) F2 middle; F3 by the transposition (2 3), which fixes e₁, T1 and the weak world.**
- Let J₀ be a compact adjacency subarc, N its neighbourhood, Λ ∩ N the outside part. Let q = (1−λ)p* + λe₁ with
  λ ∈ (0,1).
- An inside gamble g ∈ N ∩ D_{T1} is strict with g₁ > 0, and p*·c(g) ≥ 0 because D_{T1} ⊆ B_{p*} ∪ Z_{p*}. So
  q·c(g) = (1−λ) p*·c(g) + λ ρ₁(g) > 0.
- An outside gamble g ∈ N is in Λ, so c₁(g) = 0 and q·c(g) = (1−λ) p*·c(g) ≤ 0.
- Hence B_q ∩ N = D_{T1} ∩ N mod null, and P♭(q, ·) = 0 on J₀. **Ties play no role here.**
- Concavity gives P♭(q, ·) ≤ 0 on the facet line. For λ near 1, q ∈ V₁, against P♭(q, h₀) ≥ t. ∎(b1)

**(b2) F1.** Let J₀ ⊆ O ∈ {(−,−,+), (−,+,+), (−,+,−)} be a compact adjacency arc, with Λ inside and the outside
strict.
- *Reduction to no inside ties.* If the Λ-ties near J₀ are non-null, the L₊-side face model K_δ has
  P_{K_δ}(h(τ_L)) < 0 at some τ_L ∈ J₀. (Otherwise D_{K_δ} shares the facet near J₀, and so contains D_{T1}
  near it.) This forces O to be a corner orthant, since (−,+,+) ∩ Λ is never tied (§1.1). Say τ_L < τ₂.
  - Concavity and the zeros at τ₂, τ₃ give P_{K_δ} < 0 on [0, τ_L], including r12.
  - Take an open arc I of strict facet points on which P_{K_δ} < 0, accumulating either at a point of [0, τ_L)
    or at r12 from the F2 side. By L1.5 such arcs exist on F1 ∩ [0, τ_L), unless that arc is all adjacency.
    In that case use F2 ∩ (−,−,+) near r12, where L1.5 and (a) leave at most one non-strict point.
  - The shell over I is strict, open and connected, in Z_{p*}, so it lies in one strict atom b (L1.4(d)).
  - With δ′ on the L₊ side and δ′·b > 0, P_{K_{δ′}} ≥ 0 on I, hence (by continuity) at its end. But
    P_{K_{δ′}} < 0 on [0, τ_L] by the same concavity. This contradicts either concavity on F1 (pattern ≥ 0, < 0,
    = 0) or the value at r12.
  - So we may shrink N until the inside ties are null.
- *No inside ties.* For h = h(τ), τ ∈ J₀:
  - P♭(q, h) ≥ 0 iff the inside Λ-gambles near h are in B_q. That depends only on θ(q) (L1.6), so
    Θ_τ := {P♭(·, h) ≥ 0} is a closed convex union of rays from e₁, i.e. a sector.
  - Θ_τ contains R* (as P♭(p*, h) = 0) and A_τ.
  - By L1.7, A_τ is an open half-plane at p*.
  - If λ_τ ≠ R*, then Θ_τ ⊇ conv(A_τ ∪ R*), which contains an open wedge at p* between λ_τ and R* on the non-A
    side. So the zero set Z_τ = Θ_τ ∖ A_τ is fat at p*.
- *Step-5 argument.* Suppose λ rotates at τ₀ (fat zero set). Take τ₁ near τ₀ and q in A_{τ₁} ∩ (the fat wedge).
  Then P♭(q, τ₁) > 0 = P♭(q, τ₀), so by concavity q ∈ A_τ for τ ∈ (τ₀, τ₁]. Continuity (L1.7) then gives
  n_{τ₀}·(q − p*) ≥ 0, which is false.
  - So λ is locally constant on {λ ≠ R*}, an open set by continuity.
  - Hence either λ_τ ≡ R* on J₀, or λ_τ ≡ λ ≠ R* on J₀.
- *λ ≡ R*.* Then Z_τ ⊇ R* ∩ Δ° and P♭(q, ·) = 0 on J₀ for every q ∈ R*. So P♭(q, ·) ≤ 0 on F1 by concavity.
  But R* meets the strip W, where P♭(·, h₀) ≥ t.
- *λ ≡ λ ≠ R*, middle orthant (−,+,+).*
  - Here A ⊇ V₂ ∪ V₃. The convex union of rays Θ_τ then contains rays with θ near 0 and near 1, so Θ_τ = Δ°.
  - Hence Z := Δ° ∖ A, a closed half-plane, is the zero set for every τ ∈ J₀. (The Step-5 argument applies here
    even when λ = R*.)
  - For q ∈ Z, P♭(q, ·) = 0 on J₀, so P♭(q, ·) ≤ 0 on F1. Hence A_{τ′} ∩ Z = ∅ for every τ′ ∈ (0,1). By L1.7 each
    A_{τ′} is an open half-plane at p*, so A_{τ′} = A for every τ′.
  - But A ⊇ V₂, while A_{τ′} ∩ V₂ = ∅ for τ′ ∈ (0, τ₂), where h₂ < 0 and UVN at e₂ holds.
- *λ ≡ λ ≠ R*, corner orthant* (say (−,−,+); (−,+,−) is symmetric).
  - A := A_τ contains V₃ and misses V₂ and V₁: V₁ because strict outside gambles are rejected near e₁. So λ
    meets the edge [e₂, e₃] at a point y with A on the e₃ side.
  - Θ_τ = {θ ≤ θ_b(τ)} with θ_b(τ) ≥ θ(y), since A ⊆ Θ_τ. Also θ_b(τ) > θ*: if θ_b = θ*, then A ⊆ {θ ≤ θ*}
    forces λ = R*.
  - Hence, for any three τ ∈ J₀, the set ⋂ Z_τ ⊇ {θ ≤ θ(y)} ∩ (non-A side of λ). This is a nondegenerate wedge
    with apex y on the edge, since λ ≠ line(e₁, y): p* ∉ line(e₁, y) because θ(y) > θ*. So it meets the strip W.
  - At q in that intersection, P♭(q, ·) vanishes at three points of J₀, hence on an interval, hence
    P♭(q, ·) ≤ 0 on F1. This contradicts q ∈ W.
  - (θ(y) > θ*: y lies on the e₂ side of R*, since λ ≠ R* passes through p* and has e₁ on its non-A side.) ∎(b2)

**Corollary L1.B (PROVED).** Under the standing data:
- **(i)** The set Θ_Λ of facet rays h such that every conic neighbourhood of h meets Λ non-nully is **finite**:
  - at most 2 per facet-orthant arc with g₁ > 0;
  - at most 1 per arc with g₁ < 0;
  - plus possibly the crossings w12, w13.
- **(ii) Half-collar.** Near every h ∈ Θ_Λ, Λ lies in E₁(T1): inside D_{T1} if g₁ < 0, outside if g₁ > 0.
- **(iii)** Every pinned crossing, every corner ray and every point of the (+,−,−) arcs has a neighbourhood in which
  Λ is contained in E₁(T1), and the half of a crossing ball on the T1-correct side is strict.

*Proof.*
- By L1.A, on each facet-orthant arc f has the good sign except at its zeros. f is concave and not ≡ 0 on any
  interval, so: if f ≥ 0, at most 2 zeros; if f ≤ 0, its zero set is a convex set of maxima, i.e. at most 1 point.
  At a crossing, int-Λ from one side would be an int-Λ arc.
- (ii): for g₁ > 0, f ≥ 0 near h gives P_{K*}(h′ + s𝟙) ≥ s > 0, so inside gambles are not in Λ. Symmetrically
  for g₁ < 0. ∎

---

## 5. Assembly (Part C; Theorem L1.C, CHECKED)

**Theorem L1.C (CHECKED).** The proof of Theorem M0closed(a) — Props. crosspin, chainchords, carrying and the
chain of write-up §4 — runs for the standing data. Hence Theorem L1.

**Audit.** Each place where §4 or §7.7 uses strict signs of world 1, and why it survives (Cor. L1.B):

| Step | use of world 1 | why it survives |
|---|---|---|
| Lemma UVN at e₁ (Thm. pivot Steps 0, 1, 4; Lemma nopin; Prop. carrying(d)) | facet gambles h(τ), crossing half-balls U^±, middle-arc gambles | at every τ with h(τ) ∉ Θ_Λ (all but finitely many), by L1.4(c). At the finitely many exceptional τ, the needed facts are limits: A_τ ⊇ A_{τ−η} ∩ A_{τ+η} by concavity; Step 4's sign of n_τ·(e₁ − p*) by continuity of n. In nopin at w32 and w23 (j = 1), U⁺ lies in the T1-correct half, which is strict (L1.B(ii)) |
| Lemma PL2 at w12, w13 (crossing coordinate 1) | UVN at e₁ at w_± | w_± are generic facet points near the crossing; choose them outside Θ_Λ. c₁(h^±_m) ≤ 0 still holds on Λ |
| Lemma ball, "strict signs give the orthant" (crosspin; carrying(b)) | balls centred on {g_c = 0} | c ∈ {2,3}: L1.4(d),(e). c = 1, crosspin at w12, w13: if P_K(w) ≠ 0 for a face model K, the open connected shell {P_K < 0 < P_{T1}} (or the outside analogue) near w contains strict parts near the facet points beside w (finitely many exceptions) and, by assumption, Λ-balls. This contradicts L1.4(d) |
| Thm. Estructure(b): chords miss vertices, cut off the odd vertex (chainchords' countability; carrying(b),(d)) | atom chords | vertex atoms (chords through e₁) lie in Λ. (1) Every line ≠ R* through p* meets each of them at most once, so countability survives. (2) Face models agree with T1 on Λ: a Λ-part of D_{K_δ} △ D_{T1} is joined to a facet point outside Θ_Λ by a segment inside D_{K_δ} ∖ cl D_{T1} (resp. D_{T1} ∖ cl D_{K_δ}), whose end is strict. This contradicts L1.4(d). So carrying atoms are strict (they meet strict near-facet gambles) and keep b₁ ≠ 0 |
| Lemma edgebox | c(A+λB) < 0 on the closed edge | ≤ 0 on [e_a, e_b], < 0 off e₁ (§1.4). Every application uses q₀ ≠ e₁ (Prop. T1: q₀ = (s, 1−s, 0), s > 0) |
| Prop. T1, transposition σ = (1 2) | c^σ is a field of the same kind | c^σ is weak at world 2. Parts A–B hold for any one weak world by the S₃-symmetry of T1 and K′. Rescaling p* ⊙ c keeps Λ |
| p* ∈ E branch (Prop. carrying(a)) | S null ⇒ Z_{p*} null | crosspin (above) gives K_δ = T1 for all generic δ. Then Z_{p*} ∩ {δ·c ≠ 0} is null for two independent generic δ, and c ∦ 𝟙 on Λ |

*Status note.* For blind sets with Θ_Λ = ∅ (a full collar: Λ null near ∂D_{T1} ∖ 0) the exceptional-τ entries are
void. The audit is then a line-by-line check that every world-1 sign used concerns a gamble with a strict
neighbourhood. Its two-reader standard has not been met: one reading, here.

---

## 6. Consequences, scope, and what is left

### 6.1 For T1 and the ranking programme (PROVED from L1 and K3.7)
- In the setting of K3.7 (worlds 2, 3 with integrable endorsing densities; world 1 not (M1)), the weak field
  (ρ_∞σ₁, ρ₂σ₂, ρ₃σ₃) has (γ). If moreover Λ_∞ ⊉ E₁(T1) ∩ M, then T1 is Bayes at an interior weight (K3.7(γ)).
  Theorem L1 forbids this.
- **So the third world of a cover is (M1), or Λ_∞ ⊇ E₁(T1) ∩ M.**
- The second alternative makes T1 Bayes only at e₁. It is the residual of K3.7(γ) and is not a Q_A question.
- The blind-set route of BRIEF17 §3 is closed at this level. A Stage-B construction of a world-1 order on Λ
  ("strict (G) with zero exchange rate") would produce a field excluded by L1.

### 6.2 What the proof shows about where non-additivity must live
- The weak field may break the corner equations (Prop. L1.2) but not coherence along the vertex chord.
- So a world that is blind (purely finitely additive) on part of its error region cannot help unless it is blind on
  **all** of E₁(T1) ∩ M, or carries finite certificates ((M1)). Combined with K3, the remaining T1 questions on
  M_U are therefore:
  - Q_K3 (non-localizable blind sets in full systems);
  - (M1) worlds;
  - the sheltering residual of K3.5′.

### 6.3 Several blind sets (Λ₁, Λ₂, Λ₃) — necessary conditions PROVED; exclusion CONJECTURE
Let ρ_k = 0 exactly on Λ_k, with c ≠ 0 a.e. (so Λ₁ ∩ Λ₂ ∩ Λ₃ is null).
- (γ) plus the K3.7(β) argument at each vertex e_k gives **rigidity** of Λ_k ∖ (Λ_i ∪ Λ_j) relative to world k
  (two "between" models C_{ki}, C_{kj}). It needs ρ_i, ρ_j > 0 on Λ_k, i.e. Λ_k ∩ (Λ_i ∪ Λ_j) null.
- On Λ_i ∩ Λ_j only one coordinate is live: its chart is ∅ or Δ°. By (TB), Λ_i ∩ Λ_j must lie in
  D_{T1} ∩ {g_k > 0} or in (U ∖ D_{T1}) ∩ {g_k < 0}.
- The analogues of (N2), (N3) hold world by world.
- Parts A–B use, for world k, auxiliary gambles that are strict at the other worlds. If the closures of the Λ_k
  meet ∂D_{T1} in pairwise disjoint sets of rays, the arguments go through verbatim (CHECKED). I have not
  excluded two blind sets touching the same facet arc. **CONJECTURE L1.D:** Theorem L1 holds for every field with
  pairwise-null blind-set intersections.

### 6.4 Not done
- Part C (L1.C) and Lemma L1.7 are CHECKED, not written out to the write-up's standard.
- L1.D is open.
- Nothing here bears on general (two-sided) decomposable domains.
- Not refereed.

---

## 7. Dependencies and files

**Used (all marked proved in the write-up, K3 or K3_referee):**
- write-up Lemmas signs, chords, levels, caps, UVN, PL2, nopin, quasilin, ball (steps 1–4 of Prop. F),
  edgebox;
- Thms. pivot, nosliding, Estructure(a),(c),(d),(e);
- Props. reduction(d), crosspin, chainchords, carrying, T1, P1box;
- N25 Lemma 3.1;
- K3.7(β),(β′) and Lemma K3.7′;
- K3_referee §7 (Q1)–(Q3).

**Not used:** integrability of ρ_k; (E_ψ); Prop. F step 5; ranking axioms beyond K3.7.

`l1py/` (run each with `python3 -I` from inside `l1py/`):
- `facet_algebra.py` (+ `.out`): strict contradiction and the r12-corner arc configuration at ε = 0.1, 0.3, 0.6.
- `facet_configs.py`, `run_one.py` (+ `run_*.out`, `best_*.npy`): penalty search over R*-arc placements on grids.
  Superseded where it conflicts with the exact crossing boxes (§1.5).
- `verify_F3J.py` (+ `.out`): shows the grid artifact (x₁x₂ > κ passing coarse grids).
- `explicit_twoarc.py` (+ `.out`): the consistent two-arc solution of Prop. L1.2 at ε = 0.3, with exact crossing
  boxes and fine-grid boxes.
- `field_search.py` (+ `.out`): random homogeneous weak fields with T1 exactly Bayes at u; coherence tests and
  baseline.
