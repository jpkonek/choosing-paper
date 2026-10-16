# P2. Non-additive covers of T1 through "holonomy": the attempt, three reductions, and the exact point of failure

14 Oct 2026 (round 11, construction side). Brief: BRIEF10.md.
Labels: **PROVED** (complete proof here), **CHECKED** (verified, proof sketched or a reading of a cited proof),
**CONJECTURE**, **NUMERICS** (scripts in `p2py/`, run with `python3 -I`; no proof depends on them).
Standing: n = 3; T1 = (1−ε)u + εΔ; the U-domain M_U (U = D_{K'}, K' = u + s(T1 − u)); P_i = U ∩ {h_i > 0};
E_i(X) = X △ P_i; σ_i(h) = sign h_i; 𝒞 = measurable {−1,0,1}-valued functions on U mod null sets;
𝒜_i = acceptance set of world i (N17.1(a)); 𝔚_i, 𝔚^reg_i as in N17/N19; (M0)/(M1)/(M2) as in the write-up §2.5.
Terminology follows termfix/TERMFIX_RULES.md (decomposable domain, advice range, U-domain).

---

## 0. Outcome

**No cover of T1 was constructed.** The holonomy idea was made exact, and it points to one precise target. Of the
mechanisms I could put behind that target:
- the flexible ones are ruled out by closed sections, except one that collapses into the (M0) residual R-a′;
- the rigid ones need a far-dominator structure (Prop 5.3) that I could neither build nor refute.

What remains open, and what an obstruction would have to prove, is stated in §8.

| # | Result | Status |
|---|---|---|
| P2.1 | Vector form of the exact consistency test on M_U: C ⪯_i X ⟺ σ_i(1_C − 1_X) ∈ 𝒜_i | PROVED |
| P2.2 | **Holonomy, made exact.** The constraint system that the additive chain produces (strict chart signs, crossing rows, no sliding at corners, monotone rotation, edge box) is inconsistent when all three facet maps are linear (write-up Prop. 4.22). It becomes **consistent** as soon as **one** facet map has **one kink between its two crossings** (ε = 0.05, 0.3, 0.6; with one kink per facet at ε = 0.9). A kink at a corner sector does not help | NUMERICS |
| P2.3 | Linearity of facet maps is **not** an additivity input: it is forced by coherence of the selected models plus straight (half-plane) charts of the selected family. So the "potential" in the holonomy is carried by the coherent selected family, not by the world orders | CHECKED (reading of write-up §4.1–4.5) |
| P2.4 | **Flexible worlds.** If a world's acceptance depends only on cellwise masses and is divisible, it has no finite obstruction (no M1, for any family of comparisons); if it is moreover cell-fine it adds up on everything; otherwise it is endorsed by a lexicographic hierarchy of additive levels | PROVED (a)–(d); (e) CHECKED |
| P2.5 | **Theorem LX.** For two-level lexicographic rankings with additive levels and *weakly signed* primary on M_U with (LA), (S), (C): on every open disk of weights that avoids the exceptional set and on which the lex-Bayes map is injective, there is a sub-disk on whose moving problems every world is single-level additive (secondary ∝ primary, or a free set) | PROVED |
| P2.6 | Rigid acceptances (N17.7/N17.8 type) cannot act between nearby models; a cover using them for near-T1 reversals needs far dominators, hence a discontinuous selection at the target fibre, a far tie partner of T1, or a non-Archimedean world | PROVED (template lemma); CHECKED (trichotomy) |
| P2.7 | n = 2 versus n = 3: world-i error sets of coherent models are nested iff the credal sets have the same two tangent lines from e_i and are radially ordered; nested pairs are codimension 2 in n = 3. But crossing is **not** what escapes the n = 2 Archimedean lemma: Theorem LX recovers its conclusion in n = 3 without nestedness | PROVED (criterion); NUMERICS |
| P2.8 | Design attempts D1–D3 and their exact failure points; statement an obstruction must prove | — |

**One-paragraph verdict.**
- The additive contradiction for T1 is a holonomy of *linear facet maps* around the three corners, closed by the edge box.
  Breaking linearity on a single facet, by one kink between its crossings, removes the contradiction at the level of
  chart data (P2.2).
- But linearity comes from coherence once the selected family has straight charts (P2.3). So a cover must keep U_L
  near T1 from containing a straight-chart family on at least one facet arc. That means at least one world must compare
  errors on the two halves of that arc non-additively.
- Flexible (rearrangement-invariant, divisible) worlds cannot do this except by lexicographic layering (P2.4), and
  layering is neutralised by closed sections wherever the Bayes family moves two-dimensionally (P2.5).
- The only flexible survivor is a *degenerate* kink: a flat sector of one facet map, which is an atom chord through
  the target weighting, i.e. configuration R-a′ of the (M0) residual. It is chart-consistent (NUMERICS), but it is
  not an M1/M2 mechanism.
- Non-flexible (rigid) acceptances act only between far-apart models (P2.6). Using them needs a far-dominator
  structure for which I have neither a construction nor a contradiction.

---

## 1. The exact consistency test in vector form (P2.1, PROVED)

**Lemma 1.1.** For X, C ∈ M_U and every world i: 1_{E_i X} − 1_{E_i C} = σ_i·(1_C − 1_X).

*Proof.* On C∖X, X is silent and C accepts. X errs at i iff h_i > 0, C errs iff h_i < 0, so the left side is
[h_i>0] − [h_i<0] = σ_i. On X∖C the roles swap and the left side is −σ_i. Elsewhere both sides vanish. ∎

Hence C ⪯_i X ⟺ σ_i(1_C − 1_X) ∈ 𝒜_i, and the exact test of "Coverage after Neutral Abstention" (Thm closure) reads:
- choose the coherent family (C_p) and the closed sets A_i(X), subject to the covering condition (5);
- the generators are G_i = {σ_i(1_{C_p} − 1_X) : p ∈ A_i(X)};
- rules 1–3 produce the 𝒞-sum-closure of G_i ∪ 𝒞_{≥0} (N17.1(a));
- rule 4 adds σ_i(1_{C_p} − 1_X) at every world whenever σ_i(1_X − 1_{C_p}) is generated at every world;
- forbidden outcomes:
  - (a) a nonzero δ ≤ 0 is generated;
  - (b) σ_i(1_{C_p} − 1_X) is generated with p ∉ A_i(X);
  - (c) a rule-4 tie with an incoherent X.

Equivalently, choose acceptance sets 𝒜_i satisfying N17.1(a) and put A_i(X) := {p : σ_i(1_{C_p} − 1_X) ∈ 𝒜_i}.
Then (b) is automatic, and what must be checked is:
- these sets are closed;
- (5) holds;
- the rule-4 closure stays inside 𝒜_i;
- (c).

All failures below are given as derivations of a forbidden outcome in this form.

---

## 2. Holonomy, made exact (P2.2 NUMERICS; P2.3 CHECKED)

### 2.1 The constraint system

The additive chain (write-up §4) produces, for each facet F_k, a facet map c_k : F_k → 𝟙^⊥ (cluster-line normals at p* = u).
It has the following properties:
- **(sign)** c_k(h) has the strict sign pattern of h on relint F_k;
- **(cross)** c_k(w_{ik})_i = 0 at each crossing;
- **(NS)** c_k(r) ∝_+ c_j(r) at each corner ray r = F_k ∩ F_j;
- **(rot)** the direction of c_k(h(τ)) rotates strictly monotonically along the facet;
- **(box)** write-up Prop 4.21(c): for all ordered pairs (a,b), all A ∈ relint F_k and B ∈ relint F_{k'} with A_a<0<A_b,
  B_b<0<B_a and A_bB_a<|A_a||B_b|, and all q₀ ∈ [e_a,e_b], one has c_k(A)·q₀ ≤ 0 or c_{k'}(B)·q₀ ≤ 0;
- **(LIN)** each c_k is linear on span F_k (write-up Cor 4.19).

The write-up shows that (sign)+(cross)+(NS)+(box)+(LIN) is inconsistent for every ε (Prop 4.22: Möbius corner equations
give x = x_±, and the box gives κ^{−1} ≤ x² ≤ κ).

**Exact box test used in the scripts.**
- Put s_A = c_b/(c_b − c_a) and s_B = −c_b/(c_a − c_b), where c = c_k(A) or c_{k'}(B).
- Put ρ_A = A_b/|A_a| and σ_B = |B_b|/B_a.
- Then (box) holds iff s_A ≤ s_B whenever ρ_A < σ_B.

(Indeed c(A)·(s e_a + (1−s)e_b) > 0 ⟺ s < s_A, and c(B)·(…) > 0 ⟺ s > s_B.) The scripts evaluate
min (s_B − s_A) over admissible sampled pairs. They sample facet points on uniform grids and on grids refined
geometrically down to 10⁻⁹ around every crossing and corner, and they include an independent brute-force check over
q₀.

### 2.2 One kink suffices (NUMERICS)

**Linear sanity check.** With (LIN) the box margin is −0.143 at ε = 0.3, and x²/κ = 3.798 as in the write-up. It is
negative on every grid and at every ε tested (0.05, 0.3, 0.6, 0.9).

**One kink on F_1 between its crossings w_21 and w_31; F_2 and F_3 linear (ε = 0.3).**
- Exact NS: residual 4.5·10⁻¹⁷ after fsolve.
- Strict signs: margin 4.7·10⁻⁴, taken at |h_l| ≥ 10⁻³|h|.
- Monotone rotation: all sector determinants > 0.
- Box margin ≥ 1.1·10⁻⁹ on the refined grid (8 397 points per facet). The minimum sits at the degenerate ends
  ρ → 0 or ∞, where s → 0 or 1.
- No violation among 120 000 brute-force pairs (max of min(c_A·q, c_B·q) = −7.7·10⁻³).
- Data (facet map of F_1, sector A ∋ w_21: c_2 = 1.368565 h_2, c_3 = 0.09583 h_2 + 0.540421 h_3; sector B ∋ w_31:
  c_3 = 0.568784 h_3, c_2 = 0.307991 h_2 + 0.313897 h_3; break at τ = 0.355134; F_2, F_3 linear with rates
  x_2 = 1.642451, x_3 = 0.608545):
  `p2py/holonomy_onekink_F1_eps0.3.npy`, `holonomy_onekink_eps0.3.out`, `holonomy_refine.out`.

**Other cases.**
- The same holds with the kink on F_2. By the cyclic symmetry of T1 and of the system, it holds on F_3 as well.
- At ε = 0.05 and 0.6 one kink on F_1 also works.
- At ε = 0.9 the search found a solution with one kink on **each** facet (margin ≥ 1.45·10⁻⁹ on the refined grid,
  no brute-force violations), but none with a single kink. That is a search failure, not a claim.

**Corner sector frozen.** If instead the kink is a *frozen corner sector* (c_1 of constant direction on [r_12, b] with b
before the first crossing, the rest linear), every solution of NS violates the box: 76/76 configurations, margins
≤ −0.146 (`holonomy_flat.out`). The kink has to separate the two crossing rows of one facet.

**Frozen sector in the middle of F_1.** A *flat middle sector* (constant direction on [b_1, b_2] with
w_21 < b_1 < b_2 < w_31) is chart-consistent for widths up to 60 % of the middle arc. In each case NS is exact, signs are
strict, rotation is weakly monotone, and the box margin on the refined grid is ≥ 3·10⁻⁹ (`holonomy_flatmid.out`).

**Reading (heuristic, supported by the numerics).** The additive contradiction is a *cyclic rigidity*:
- three linear facet maps, each transporting a crossing-row rate from one crossing to the other;
- three corner gluings (NS);
- closed by the box at the edges.

Remove the transport on one facet and the system is consistent. This is the precise form of the brief's
"cyclic exchange-rate condition around the three corners".

### 2.3 Where linearity comes from (P2.3, CHECKED)

The write-up derives (LIN) as follows:
- Prop 4.18 (blow-up) and Lemma 4.17 (two slopes) give a(τ) = α_τ n_τ affine;
- concavity of τ ↦ Ψ(q,τ) = P(q, h(τ)) is coherence of each K_q (P(q,·) is a lower prevision);
- the two-slope form of the second blow-up needs the half-plane level structure (Lemmas 4.6 → 4.7),
  which comes from half-plane charts and Hausdorff continuity (Lemma 4.5);
- pivot chords (Thm 4.12) use Lemmas 4.11, 4.10 and 4.9 (no pinning, PL2, UVN), i.e. straight charts together with the behaviour of the family
  near the vertices.

Additivity of the *world orders* enters only to make the selected family a Bayes family with straight charts. So:

> **P2.3.** Any Hausdorff-continuous family of coherent models through T1 whose charts are half-planes (coherent at every
> interior weight, with UVN), whatever produced it, has linear facet maps; P2.2 then gives the contradiction.
> A non-additive cover must therefore keep U_L near T1 from containing such a family on at least one facet arc. The
> world orders "need not carry a potential" (brief), but the potential that matters, the linear facet map, is carried by
> the coherent selected models themselves.

In ranking terms the minimal design target is a **kink**:
- on one facet F_k there are two sub-arcs, one around each crossing;
- the local exchanges at the selected models near T1 are supported by weights that are *not* projectively related
  between the two sub-arcs;
- so at least one world must price errors on the two sub-arcs against each other non-additively.

---

## 3. Flexible worlds (P2.4)

Fix a finite partition 𝒬 = (Q_1,…,Q_N) of U into non-null measurable cells and a finite non-atomic measure ν ~ μ on U.
For δ ∈ 𝒞 put a_c(δ) = ν(δ⁺ ∩ Q_c), b_c(δ) = ν(δ⁻ ∩ Q_c), m(δ) = (a,b) ∈ ℝ^{2N}_{≥0} and π(a,b) = a − b ∈ ℝ^N.
A world is **(𝒬,ν)-flexible** if:
- **(F1) invariance:** m(δ) = m(δ′) implies (δ ∈ 𝒜 ⟺ δ′ ∈ 𝒜);
- **(F2) divisibility:** if δ ∈ 𝒜, s ∈ (0,1] and m(δ′) = s·m(δ), then δ′ ∈ 𝒜.

Let 𝔄 = m(𝒜) and let Cap = {(a,b) ≥ 0 : a_c + b_c ≤ ν(Q_c) ∀c}.
Additive worlds with cellwise-constant densities, and lexicographic worlds whose levels have cellwise-constant
densities, are flexible. N17.7 is (F1) but not (F2): g_i ∈ 𝒢_i, while the half-mass version (mass 0.2 on the C_i
cells, 0.3 elsewhere) lies neither in G_θ (0.3 > 0.2θ) nor in any 𝒢_j (its positive part cannot nearly fill a C_j).

**Lemma 3.1 (PROVED).**
- (a) cone(𝔄) = {s·m : m ∈ 𝔄, s > 0} is a convex cone, and 𝔄 = cone(𝔄) ∩ Cap.
- (b) π(𝔄) ∩ (−ℝ^N_{≥0}) = {0}.
- (c) There is w ∈ ℝ^N_{≥0}∖{0} such that ν_w := Σ_c w_c ν|_{Q_c} satisfies ν_w(δ) ≥ 0 for every δ ∈ 𝒜. In
  particular a flexible world has **no finite obstruction** (no M1), for any family of its comparisons.
- (d) Suppose the world is **cell-fine**: for all c ≠ c′ there is ε > 0 such that, for all small s > 0, gaining mass s in
  Q_c against losing mass εs in Q_{c′} is accepted (the vector with a = s e_c, b = εs e_{c′} lies in 𝔄). Then w can be
  taken with all w_c > 0, so the world adds up on **all** comparisons.
- (e) (CHECKED) In general there are w¹,…,w^r ∈ ℝ^N with the following properties:
  - every accepted δ has (w¹·πm(δ), …, w^r·πm(δ)) ≥_lex 0;
  - for every cell c, the first nonzero w^k_c is positive.

  So the world is endorsed by a lexicographic hierarchy of additive levels with cellwise-constant densities.

*Proof.*
- (a) Disjointly supported accepted vectors sum, inside 𝒞, to an accepted vector (N17.1(a)), and m is additive on
  disjoint supports. For m, m′ ∈ 𝔄, (F2) gives m/2, m′/2 ∈ 𝔄. These are realisable with disjoint supports because
  (m+m′)/2 ∈ Cap and ν is atomless, so (m+m′)/2 ∈ 𝔄. Scaling up within Cap is repeated disjoint addition. So 𝔄 is the
  trace on Cap of a convex cone.
- (b) Let m = (a,b) ∈ 𝔄 with a ≤ b cellwise and a ≠ b.
  - By (F2), assume ν(Q_c) ≥ 2b_c + a_c, and realise δ.
  - Choose δ′ with the same masses, δ′⁺ ⊆ δ⁻ (possible since a_c ≤ b_c), and δ′⁻ = δ⁺ ∪ R with R ∩ supp δ = ∅ and
    ν(R ∩ Q_c) = b_c − a_c.
  - By (F1), δ′ ∈ 𝒜. Positive parts are disjoint and negative parts are disjoint, so δ + δ′ ∈ 𝒞 is accepted.
  - But δ + δ′ = −1_{δ⁻∖δ′⁺} − 1_R ≤ 0 and is nonzero. This contradicts strict (G).
- (c) K := π(𝔄) is a convex cone missing the open negative orthant. Separate them, and note
  ν_w(δ) = w·π(m(δ)) ≥ 0.

  For "no M1": a finite certificate Σλ_kδ_k ≤ 0 (nonzero) would give Σλ_k π m(δ_k) ≤ 0 and nonzero, which is an
  element of K by (a), contradicting (b).
- (d) Suppose no w > 0 exists. By Stiemke's lemma for the closed cone cl K there is v ∈ cl K with v ≤ 0 and v ≠ 0.
  - Let v^{(m)} ∈ K converge to v. Put P = {c : v_c = 0} and pick c″ with v_{c″} < 0.
  - For each c ∈ P with p_c := v^{(m)}_c > 0, add (p_c/ε)(e_{c″} − ε e_c) ∈ K (cell-fineness).
  - The sum lies in K. It is ≤ 0 on P, and its c″-coordinate is v^{(m)}_{c″} + Σ p_c/ε → v_{c″} < 0. The other negative
    coordinates stay negative for large m.
  - This contradicts (b).
- (e) Lexicographic separation of the disjoint convex sets K and −ℝ^N_{≥0}∖{0} (Martínez-Legaz & Singer,
  *Lexicographical separation in ℝⁿ*, LAA 1987). Applied to −e_c, it gives the positivity of the first nonzero level. ∎

**Consequence.** A flexible world that does not add up on 𝔚^reg is not cell-fine, and its non-additivity is
*lexicographic layering* (M2). M1 is impossible for flexible worlds. This turns N17's heuristic "flexible violations
restore additivity" into a theorem, with the one exception of layering.

---

## 4. Lexicographic layering and closed sections: Theorem LX (P2.5, PROVED)

**Class.** World i ranks lexicographically by (F_i, S_i), with:
- F_i(X) = ∫_U φ_i(h, a_X(h)) dμ and S_i(X) = ∫_U ψ_i(h, a_X(h)) dμ, integrable envelopes;
- c^F_i(h) := φ_i(h,0) − φ_i(h,+) **weakly** signed (zeros allowed, both good~silence and bad~silence);
- c^S_i := ψ_i(h,0) − ψ_i(h,+) strictly signed;
- strict (G) and (IB) on M_U, with (LA), (S), (C).

This is N10 (F4)'s class. It contains the open zero-pattern residual (C-i) and the class 𝓛₂^s of the write-up §7.

**Notation.**
- For t ∈ Δ°, B_t is the lex-t-Bayes model: accept h iff (t·c^F(h), t·c^S(h)) >_lex 0.
- E is the set of t at which μ{h : c^F(h) ≠ 0, t·c^F(h) = 0} > 0 or μ{h : c^F(h) = 0, t·c^S(h) = 0} > 0. It is
  contained in a countable union of lines and points (atoms and fan points of the chart directions, as in N25).
- On an open set avoiding E, t ↦ B_t is a.e.-unique and continuous in measure.
- B_t is undominated and coherent, and it equals a selected model (N9 Lemma 4.1; the proof uses only uniqueness and the
  lexicographic form, so weak signs are allowed).

**Facts used.**
1. **(R2 Thm 7.)** The set V_i := {F_i(X) : X ∈ U_L improvable at i} is countable. Here *improvable* means some Z has
   F_i(Z) = F_i(X) and S_i(Z) < S_i(X).

   In test form: if p were not a local minimum of q ↦ F_i(C_q), then the indices q_m → p with C_{q_m} ≺_i Z (by the
   primary) put q_m ∈ A_i(Z). Closedness puts p ∈ A_i(Z), so C_p ⪯_i Z ≺_i C_p, a forbidden outcome.
2. **Non-improvable implies Lagrangian.** If X is non-improvable and F_i(X) is not extremal, then X minimises
   ψ_i + λφ_i pointwise for some λ ∈ ℝ: the (F_i,S_i)-range is convex and compact (Aumann), and X is the lowest point of
   its vertical line.

   Computation:
   - λ ≥ 0 gives P_i;
   - for λ < 0, X accepts h with h_i > 0 iff r(h) < λ, and h with h_i < 0 iff r(h) > λ, where r = −c^S_i/c^F_i < 0
     on {c^F_i ≠ 0};
   - on {c^F_i = 0}, X is world-i-optimal.

   So the Lagrangian models at world i, together with the end model λ = −∞, form a closed set 𝓛_i. It is a *chain* for
   world-i error inclusion, except at the countably many "atoms" λ with T_λ := {c^F_i ≠ 0, c^S_i + λc^F_i = 0}
   non-null; there 𝓛_i contains all splices on T_λ. The functional φ(X) := ν(E_i(X) ∩ {c^F_i ≠ 0}) is continuous,
   monotone along the chain, and injective off the atom splice families.

**Theorem LX (PROVED).** Let W ⊆ Δ° be an open disk with W ∩ E = ∅ on which t ↦ B_t is injective. Then there is an open
disk W″ ⊆ W with the following property. Let M″ be the set of problems on which t ↦ a_{B_t}(h) is not constant on W″.
Then either:
- (i) for every world i there is a constant α_i > 0 with c^S_i = α_i c^F_i a.e. on M″, so that c^F_i is strictly
  signed there; or
- (ii) c^F = 0 a.e. on M″ (M″ is a free set), and B_t restricted to M″ is the secondary-t-Bayes model.

In either case, for models that differ only on M″, every world's order is the additive order of one strictly signed
field (c^F_i in (i), c^S_i in (ii)). No comparison supported in M″ is non-Archimedean.

*Proof.*

*Step 1 (one world).* Fix i, and let V be the countable set V_i ∪ {min F_i, max F_i}.
- Put L := {t ∈ W : B_t ∈ 𝓛_i} and Z_v := {t ∈ W : F_i(B_t) = v}.
- By Facts 1–2, W = L ∪ ⋃_{v∈V} Z_v. Each Z_v is closed in W, by continuity.

*Case 1: some Z_v has interior.* Take a disk W_1 ⊆ Z_v.
- V(t) := min_X t·F(X) = Σ_i t_i∫φ_i(h,0)dμ − ∫[t·c^F(h)]₊dμ(h) is concave and 1-homogeneous, with ∇V(t) = F(B_t).
- So ∂_iV ≡ v on the cone over W_1, and hence ∂_i²V = 0 there as a distribution.
- But ∂_i²V = −∫ δ(t·c^F(h)) c^F_i(h)² dμ(h). Testing against φ ≥ 0, positive on the cone, gives
  ∫ c^F_i(h)² (∫φ(t)δ(t·c^F(h))dt) dμ(h) = 0.
- So **c^F_i = 0 a.e. on the problems whose primary chart line meets W_1.** Call this (a_i).

*Case 2: no Z_v has interior.* Then ⋃Z_v is meagre (W is a Baire space).
- L is comeagre, hence dense. 𝓛_i is closed and B is continuous, so B_t ∈ 𝓛_i for **all** t ∈ W.
- The function f := φ∘B is continuous on the disk W, so its image I is an interval.
- If an interior point y of I were a non-atom position of the chain, then f⁻¹(y) would be a single point, by injectivity.
  It would also separate W into {f<y} and {f>y}, both nonempty and open. That is impossible: a disk minus a point is
  connected.
- So every interior point of I lies in the open interval (φ⁻(a), φ⁺(a)) of some atom a. (A position outside all these
  open intervals, endpoints included, carries a unique model of 𝓛_i.) These open intervals are pairwise disjoint and
  int I is connected, so int I lies in a single one.
- Hence all B_t (t ∈ W) are splices of a single atom T_a: they agree off T_a and vary only on T_a. (If I were a single
  non-atom point, B would be constant, which contradicts injectivity.)
- So **every problem whose decision varies on W lies in T_a, where c^S_i = |a| c^F_i, c^F_i strictly signed, and no free
  problem varies.** Call this (b_i).

*Step 2 (all worlds).* Apply Step 1 successively for i = 1, 2, 3 to nested disks, to get W″ on which each world is in
case (a_i) or (b_i). Let A be the set of worlds in case (a).
- **A = ∅:** this is (i).
- **A = Ω:** no problem has a primary chart line through W″, so the moving problems are free. This is (ii).
- **A = {i}:** a world in case (b) forbids moving free problems, so every moving problem has c^F ≠ 0 and c^F_i = 0. Its
  chart line passes through e_i. Then B_t = B_{t′} whenever t, t′ ∈ W″ lie on one line through e_i, which contradicts
  injectivity.
- **|A| = 2, say A = {i,j}:** moving problems have c^F = (0,0,c^F_k) up to order, so t·c^F does not change sign on Δ°.
  Nothing moves, B is constant on W″, which contradicts injectivity. ∎

**Corollary LX.1 (CHECKED).**
- Under the hypotheses of LX, the good sub-disks are dense in W.
- Two good sub-disks that share a non-null set of moving problems are in the same case, with the same constants α_i.
- If the good sub-disks of W are linked by such chains (a mild richness condition on the chart lines through W), then
  every world is additive (one strictly signed density) on all problems whose lex charts cross W.
- So the lexicographic second level can do non-additive work only on problems whose charts avoid every injective,
  E-free region: thin (non-injective) regions, a dense exceptional set E, or "fixed" problems whose lex decision is
  the same at every interior weight.
- In case (ii) the moving set is a free set, and Prop 4.5 of N9 (decoupling) applies to it.

**Significance.**
- Theorem 7 (R2) and the face-continuum theorem (N9.6) kill particular lexicographic designs. LX says more: wherever a
  layered world's Bayes family moves two-dimensionally, closed sections force its two levels to be proportional.
- For the zero-pattern residual (C-i) of N10 (F4) this means: bad~silence or good~silence zeros of the primary cannot
  sit on problems whose charts cross an injective E-free region, unless the whole primary vanishes there (free set).

---

## 5. Rigid acceptances act only at a distance (P2.6)

**Template.** Write 𝒜_j = 𝒜^flex ∪ 𝒜^rig, where:
- 𝒜^flex is endorsed by a strictly positive ν_j;
- every δ ∈ 𝒜^rig has ‖δ‖_{L¹(μ)} ≥ η > 0 ("η-rigid").

**Lemma 5.1 (PROVED, immediate).** Every comparison C ⪯_j X with μ(C △ X) < η is endorsed by ν_j.

**Lemma 5.2 (PROVED).** N17.7 and N17.8 are η-rigid:
- in N17.7, δ ∈ 𝒢_i forces μ(C_i∖δ⁺) ≤ 1.2κ, so ‖δ‖ ≥ 0.4 − 1.2κ;
- in N17.8, δ ∈ 𝒢_i forces T^θ_{x*}(δ) ≥ c*_i, so ‖δ‖ ≥ e*_i > 0.

Every cancellation certificate built from them involves comparisons between models at distance at least η.

**Proposition 5.3 (CHECKED).** Let X_k → T1 in measure be incoherent near-T1 models (for instance incoherent Bayes models
B_t of a shadow, N17.5) whose selected weak dominators C_{p_k} use a rigid acceptance, so that μ(C_{p_k} △ X_k) ≥ η.
Pass to p_k → p̄. For each world j:
- put Y_{m,j} := the model with E_j(Y_{m,j}) = ⋃_{k≥m} E_j(X_k);
- then C_{p_k} ⪯_j X_k ⪯_j Y_{m,j} for k ≥ m, so closedness gives C_{p̄} ⪯_j Y_{m,j};
- passing first to a subsequence with Σ_k μ(X_k △ T1) < ∞, one gets Y_{m,j} → T1 in measure as m → ∞.

Hence one of the following holds:
- (α) C_{p̄} = T1 up to ties, so the selection is discontinuous at the target fibre: indices arbitrarily close to P_T
  carry models at distance ≥ η/2 from T1;
- (β) some coherent C* ≠ T1 is tied with T1 at every world (a far tie partner);
- (γ) some world j is non-Archimedean at T1: some C has C ⪯_j Y_m for a sequence Y_m → T1 in measure, but not
  C ⪯_j T1.

(If (γ) fails at every world, then C_{p̄} ⪯_j T1 for all j, so C_{p̄} ~ T1, because T1 is undominated; this gives (α) or
(β).)

---

## 6. n = 2 versus n = 3 (P2.7)

**Lemma 6.1 (PROVED).** Let M, M′ be credal sets containing K′, with e_i ∉ M. Then
E_i(D_M) ⊆ E_i(D_{M′}) (mod null) ⟺ M ⊆ conv(M′ ∪ {e_i}) and M′ ⊆ Sh_i(M) := Δ ∩ (cone M − ℝ₊e_i).
Equivalently, M and M′ have the same two tangent lines from e_i, and on every ray from e_i both the near and the far
boundary point of M′ lie beyond those of M.

*Proof.*
- The inclusion means (1) D_{M′} ∩ {h_i>0} ⊆ D_M and (2) D_M ∩ {h_i<0} ⊆ D_{M′}.
- Since D_{M′} ∩ {h_i>0} = D_{conv(M′∪e_i)}, condition (1) says M ⊆ conv(M′ ∪ e_i).
- The dual cone of the open cone D_M ∩ {h_i<0} is cl(cone M − ℝ₊e_i), so (2) says M′ ⊆ Sh_i(M).
- In polar coordinates about e_i: (1) gives equal-or-larger angular extent and farther far points; (2) gives
  equal-or-smaller extent and farther near points. ∎

NUMERICS (`nested_criterion.py`): Monte Carlo agrees with the criterion in all 7 test cases (radial pushes nested;
homotheties, translations not). Among a 7×7 grid of translates of T1, **0 of 2352** ordered pairs are nested at world 1.

**Where n = 3 escapes, and where it does not.**
- In n = 2 every monotone path is nested, so sections at a world are down-sets of a chain. Along a strictly increasing
  primary, closedness forces the Lagrangian property (R3 Lemma P2). This is the mechanism of the "nearby lemma".
- In n = 3, Lemma 6.1 shows that nestedness is lost generically, and the chain argument has nothing to act on.
- But **Theorem LX recovers the conclusion without nestedness.** Wherever the Bayes family is locally 2-dimensional, it
  uses Baire category and the concavity Hessian, plus the topological fact that a point does not separate a disk.
- So crossing (cyclic) error sets are **not** by themselves an escape. In n = 3, closed sections kill flexible M2 in
  every injective, E-free region of weights.
- What escapes is exactly:
  - (T) thin regions: a locally non-injective Bayes map, i.e. chart lines locally forming a pencil (in particular atom
    chords);
  - (D) a dense exceptional set;
  - (F) free sets and fixed blind problems (decoupling and FC territory, N9.6–N9.8, R3 Thm L);
  - (R) non-flexible (rigid or ultrafilter-type) acceptances.

---

## 7. Design attempts and the exact points of failure

**D1. Kink by layering (flexible).**
- *Design.* Take worlds additive within regions R_A, R_B (neighbourhoods of the two sub-arcs of F_1 around w_21 and
  w_31) and on the rest of ∂T1. World 1 makes R_B a lower lexicographic level relative to R_A, so that the supporting
  weights of the selected models on R_A and R_B can differ non-projectively (P2.3's kink).
- *Selection.* The lex-Bayes family, which N9 Lemma 4.1 forces into U_L.
- *Exact failure.* The kink needs world 1's two levels to be non-proportional on problems near both sub-arcs, and the
  lex charts of those problems pass arbitrarily close to the target weight t*.
  - On every E-free disk near t* on which the lex-Bayes map is injective, Theorem LX gives a sub-disk on which the two
    levels are proportional on the moving problems, so the supporting weights there are projectively related.
  - Hence the kink survives only if every disk near t* is thin (non-injective) or meets E. That is configuration D2
    below, or a dense exceptional set.
  - In the test: off the Lagrangian set, the improvable models B_t would occupy a continuum of primary levels. Fact 1
    makes each such index a local minimum, and the countability of V_1 then produces C_p ⪯_1 Z ≺_1 C_p, a forbidden
    outcome (b)/(a).

**D2. Degenerate kink (flat sector).**
- *Design.* Freeze the direction of one facet map on a middle sub-arc of F_1. The facet gambles of that sub-arc then
  share one chart line ℓ ∋ p* of sign pattern (−,+,+); ℓ cuts off e_1, as write-up Thm 7.14(b) requires. This escapes LX,
  because the map is not injective along ℓ.
- *Chart level.* Consistent (§2.2, widths up to 60 %).
- *Exact failure, as a P2 construction.* It is not M1/M2. Gambles with one chart line and a non-null tie set form an atom
  chord through the target weighting, so p* ∈ E(ψ). This is **configuration R-a′** of the (M0) residual, with T1
  splitting the atom (inside accepted, outside rejected), and write-up Thm 7.15 says the additive chain cannot start there.
  - In 𝓛₂^s it is excluded by write-up Thm 7.19(e) (p* ∉ E).
  - With weak-sign primaries, or for general (M0) rankings, it is open.
  - So the holonomy idea, pushed through flexible worlds, lands exactly on question (Q1) of the write-up §8.1, not on
    (M1)/(M2).

**D3. Rigid corner exchanges (M1).**
- *Design.* World j = 𝒦_j ∪ ⋃_k (g_k + 𝒦_j), where 𝒦_j is a band (unanimity) cone and the g_k are exotic generators. Each
  g_k has a heavy set H_k, positive part ≈ H_k and negative part N_k. The g_k are placed on 𝔚^reg_j so that
  Σλ_k g_k ≤ 0 (a cyclic, crossing certificate, as N17.3 requires) and so that they reverse ψ-comparisons against the
  incoherent near-corner Bayes models of a shadow.
- *Constraints derived in the test (PROVED for the template).*
  1. Each H_k lies in the world-j-correct region of every selected model that uses g_k.
  2. No selected model's world-j error set contains most of any H_k. Otherwise a reverse exotic acceptance X ⪯_j C_p
     appears, and together with additive worlds j′ ≠ j it makes C_p dominated (rule 4, outcome (b)).
  3. The H_k must overlap pairwise in positive measure, or cross-sums are generated.
  4. By Lemma 3.1 of N17, each H_k lies in the union of the other bases' world-j error sets. With (2): each H_k is
     covered by several selected error sets, but mostly by none of them.
  5. 𝒦_j must be strictly smaller than a half-space (otherwise any exotic δ₀ with ν(δ₀) < 0 plus a half-space vector
     yields −1_E, which is outcome (a)). So competitiveness must survive with an incomplete band. Where the exotic
     generators do not carry it, R3 §2.4 applies: the selection must be Bayes for every member of the band.
- Constraints 1–4 are jointly satisfiable at the level of sets (crossing makes room).
- *Exact failure.* Lemma 5.1. The reversals the cover needs are C ⪯_j B_t with B_t → T1 as t → p*: a continuum of
  near-T1 comparisons (N17.5 and CONJECTURE 5.2 there).
  - When the dominator C is within η of B_t, the reversal lies in 𝒦_j and is endorsed by ν_j.
  - So rigid acceptances can only supply dominators at distance ≥ η, and Prop 5.3 applies.
- With finitely many generators (needed for closed sections: an infinite union of closed sections need not be closed),
  I could not realise (α), (β) or (γ) of Prop 5.3, nor derive a forbidden outcome from them. This is the open point of
  the M1 route.

---

## 8. What an obstruction would have to prove

The route "rankings that do not add up" (write-up §8, N19 Conj N17.B′) is now reduced as follows.

1. **Flexible worlds.**
   - **M1 is impossible** (Lemma 3.1(c)).
   - **M2 is lexicographic layering** (3.1(e)).
   - Layering is single-level wherever the Bayes family is injective and E-free (Theorem LX).
2. **Therefore** a cover of T1 outside (M0) needs, at some world, non-additive load on one of the following:
   - (T) a thin region: chart lines locally a pencil, in particular an atom chord through p*, which is D2 = R-a′;
   - (D) a dense exceptional set;
   - (F) free sets or fixed blind problems;
   - (R) rigid or other non-flexible acceptances, which act only between far-apart models and need (α), (β) or (γ) of
     Prop 5.3.

**Statement an obstruction must prove** (each part is necessary for closing the route; together with the (M0)
residuals R-a′ and R-b′ they would close it):
- **(Ob-R)** In every ranking on M_U that covers T1 with strict (G), (IB), (LA), (S), (C):
  - (α′) the selection of the cover satisfies C_q → T1 in measure as q → P_T (plateau selections, N9.1, satisfy this);
  - (β′) no coherent C ≠ T1 is tied with T1 at every world;
  - (γ′) every world is Archimedean at T1: C ⪯_j Y_m with Y_m → T1 in measure implies C ⪯_j T1.

  By Prop 5.3, (α′)–(γ′) force the dominators of near-T1 incoherent models to be near, and then by Lemma 5.1 rigid
  acceptances carry no load on them.
- **(Ob-T)** Excluding (T), (D) and (F): the world orders are additive on the moving problems of a neighbourhood of the
  target weighting, in the sense of LX(i)/(ii). This holds for flexible worlds on injective E-free regions (LX), so what
  must be shown is that a cover cannot live on thin regions or a dense E. Thin at p* means an atom chord through p*,
  which is the (M0) question R-a′.
- Both are parts of N19's **N17.B′ for covers of T1**, which this note reduces to the cases (T), (D), (F), (R) above.

**Nearby reachable results** (proposed shifts of aim, in increasing difficulty).
1. **LX for multi-level lexicographic worlds**, which by 3.1(e) is every flexible world. Induct on levels with the same
   Baire/Hessian argument. This would give: flexible M2 is locally M0 wherever U_L is locally two-dimensional.
2. **The degenerate kink D2**, i.e. R-a′ with a middle-arc atom split by T1. Decide whether an ordinal tie-breaking at
   p* (as in N26.1) can coexist with (S) in three worlds. This is exactly where the holonomy idea lands. Write-up Thm 7.19(e)
   already excludes it for strict primaries, and LX shows that weak-sign primaries cannot avoid it by adding zeros on
   injective regions.
3. **(β′) for T1 (no far tie partner).** It is a statement about two coherent models tied at all three worlds under
   (IB) and closed sections, and is plausibly provable with the splice and fibre lemmas of N9 §3.

---

## 9. Files (`p2py/`, run with `python3 -I`)

- `holonomy_pl.py [eps] [ntrials]`: the constraint system of §2.1 and the exact box reduction. It runs the linear
  check, then searches for facet maps with one kink per facet. Output: `holonomy_linear.out`, `holonomy_eps09.out`;
  solutions in `holonomy_pl_best*.npy`.
- `holonomy_onekink.py eps m ntrials`: one kink on facet F_{m+1}, the others linear. Outputs: `holonomy_onekink_eps0.3.out`
  and `holonomy_onekink_eps.out` (ε = 0.05, 0.6, 0.9); solutions in `holonomy_onekink_F*_eps*.npy`.
- `holonomy_check.py eps file mode n`: independent brute force over admissible (A,B) pairs and q₀ on the closed edge;
  output `holonomy_check.out`.
- `holonomy_refine.py eps file mode`: box margin on grids refined to 10⁻⁹ around crossings and corners; output
  `holonomy_refine.out`.
- `holonomy_signs.py`: strict-sign margins of the saved solutions.
- `holonomy_flat.py eps`: frozen corner sector (76/76 configurations violate the box); output `holonomy_flat.out`.
- `holonomy_flatmid.py eps ntrials` (env `FLATW` = width): frozen middle sector, chart-consistent; output
  `holonomy_flatmid.out`.
- `nested_criterion.py`: Lemma 6.1 by Monte Carlo; output `nested_criterion.out`.
