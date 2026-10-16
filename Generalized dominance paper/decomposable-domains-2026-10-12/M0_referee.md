# M0 referee report: P4 Part A and P1 (case M0, every world adds up, on the U-domain)

14 Oct 2026, round 11. I am an independent referee and wrote neither note.
- Read: BRIEF10; writeup §§2–4 and §7; N25_notes (§§1–4, 8, 9) and N25_referee (Prop F); N26_referee; N26 Prop 4.3; N15 §6.
- Labels: **PROVED** (full proof here), **CHECKED** (verified, sketch), **CONJECTURE**, **NUMERICS**.
- Verdicts: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.
- Scripts:
  - rerun: `p1py/` (overlap_sympy, multi_atoms, split_facets) and `p4py/` (shells, lex_n2). All outputs reproduced: lex_n2 identical to `lex_n2.out`; shells reproduces the 164 single-orthant shells.
  - independent: `m0ref_py/` (transpose_box, tp_split, crossing_balls; outputs in `*.out`).
  - No proof below depends on numerics.

---

## 0. Headline

1. **P4 Part A is correct step by step.** Every PROVED claim checks, including the two items its author asked a second reader to recheck: Theorem 3.1 Step 4 and the anchor choice in Lemma rotation. A1 (p\* ∈ E for every ψ ∈ 𝒩) is CONFIRMED, so residual R-b′ is closed.
2. **P1's PROVED claims are correct.** P1.1 is correct, and its mirror bounds can be upgraded from CHECKED to PROVED. P1.2 and §4.3(a), (b) are correct. P1.3 and P1.4 are correct as conditionals on (HC), with one scope repair.
   - P1's "surviving escape" (split facets, NUMERICS) is **WRONG as an escape**. The facet algebra at p\* is indeed consistent; I reproduce this and extend it to strict corner inequalities. But the configuration is excluded by a local argument at the crossings (§5, Prop R.2).
3. **The two notes do not conflict.** They speak about different atoms:
   - P4's "at most three corner atoms" concerns atoms that **carry S**, i.e. tie gambles *inside* D_{T1};
   - P1's mid-facet atoms are tie gambles *outside* cl D_{T1}.
   P4's A2 does not exclude P1's atoms. **Both residuals are nevertheless empty.**
4. **New (PROVED here, one reader).**
   - *Crossing pinning (Prop R.1).* Apply P4's ball lemma to directional limits at the six crossings. Every coherent p\*-face model K then has P_K = 0 at the crossings, and so, by concavity, P_K ≤ 0 on the six corner portions of ∂D_{T1}.
   - Carrying atoms are forced to be partial by P4's Theorem 4.3. A partial carrying atom makes some directional limit positive on a corner portion, which is a contradiction. So P4's (TP) is empty.
   - **Theorem R: no ranking that adds up covers T1 on M_U.** No (E_ψ), no (HC), no P1.1/P1.3. Purely additive form: no strictly signed integrable field on M_U whose Bayes models are coherent at a.e. weighting has D_{T1} as a Bayes model at an interior weighting.
5. **(HC) is not supplied by P4**, and it is no longer needed (§4).

---

## 1. P4 Part A: verdicts

| Claim | Verdict | Note |
|---|---|---|
| Lemma 2.1 (quasi-linearity of every admissible family) | **CONFIRMED** | For each g the acceptance region in q is an open or closed half-plane with convex complement. The non-null-neighbourhood argument gives both min and max inequalities |
| Lemma 2.2 (a)–(d) | **CONFIRMED** | (b): K^A_q → K_q along *all* q_m → q ∉ E. Vertex limit is pointwise, so UVN transfers. (d): a convex set a.e. equal to an open half-plane H contains H and lies in cl H. Off-E boundary points are excluded by continuity at q |
| Lemma 2.3 (ball lemma) | **CONFIRMED** | Uses only Prop F steps 1–4: one line per fibre and (★). I re-derived both (§2.2). Prop F step 5 (no fans) is **not** used here, nor anywhere in Theorem R |
| Lemmas 2.4, 2.5 (shells) | **CONFIRMED** | (a): g₁ = w − s(𝟙−e_c) has g₁_c = 0 and P_{T1}(g₁) ≤ −s(1−v_{k,c}) < 0 < P_K(g₁). (b): the sub-cone {m·h < 0} ∩ F_k contains a corner ray. Crossings are excluded by the ball lemma. NUMERICS reproduced |
| Lemma 2.7 (PL2 for K^♭ across chords) | **CONFIRMED** | Step 1 makes rigorous the N25 referee's heuristic: a jump of α/β at Q puts a collar ball centred on {g_c = 0} into Z_Q. Step 2: dist(v, K^♭_q) → 0 gives P^♭(·,h) < 0 near Q *per h* (enough for PL2). Step 3: exact charts for K^♭ make the β-side statements exact |
| Lemma 2.8 (nopin, every admissible family) | **CONFIRMED** | int co(G ∪ V_j) ⊆ Γ directly, with no Fubini over q. K^A ⊆ K^♭ transfers v_k ∉ K |
| **Theorem 3.1** (§4 chain for K^♭, p\* ∉ E) | **CONFIRMED** | Step 4 and the anchors, §2.1 |
| **Theorem A1** (p\* ∈ E for every ψ ∈ 𝒩; R-b′ closed) | **CONFIRMED** | Uses only (α), (γ) |
| Prop 4.1 (i)–(iii) | **CONFIRMED** | (ii): fibre lengths are locally bounded below on each component, and (★) with connectedness gives one atom per component. (iii): two corner chords through p\* never have antiparallel b̄ (Lemma 2.5) |
| Lemma 4.2 | **CONFIRMED** | The fibre relation G ∩ (h+ℝ𝟙) = {π^♭ ≤ s < π⁺} is a property of G (computed at any t ∈ ℓ°), so p\* ∉ ℓ° is harmless |
| Theorem 4.3 | **CONFIRMED** | The proof needs φ_t = 0 only on *some* open interval of relint F_k. That is how Cor 4.4 uses it |
| Cor 4.4 (necessary conditions; residual (TP)) | **CONFIRMED** as a list of necessary conditions. **The residual is empty** (Theorem R) | — |
| "Forced features of (TP)" | **CONFIRMED** (vacuous) | — |
| Theorem A3 (under (E_ψ)) | **CONFIRMED**; **superseded** (E_ψ not needed) | The (IB) contexts lie in A^c (B^s ∩ Z = ∅, U ∩ −U = ∅). Admissibility of A = S at ℓ_ij ∖ ℓ_ij°: intersect the two one-sided limits (N25 Lemma 3.2). No Prop F needed |
| §3.1 (I1, I2, C2 are not the M_U route) | **CONFIRMED** (as a reading) | Agrees with P1 §1.1 |
| Theorem P4 (ii) / "exact residual of (A)" | **Superseded** | Alternative (ii) cannot occur. Theorem P4 now reads: a cover on M_U forces some world to fail SP^reg (M1 or M2) |
| Part B | not refereed (outside this brief) | — |

### 1.1 Theorem 3.1, Step 4 and the anchor choice (priority)

**Step 4.**
- Suppose n_τ is constant on [a,b], with line λ ∋ p\*. Since p\* ∉ E, λ is not an atom chord, so λ ∩ E is countable. This needs only N25 Thm 2.1 (chords ∪ countable F), not Prop F.
- For q ∈ λ ∖ E: q ∈ cl A_τ ∖ A_τ, so Ψ(q,τ) ≤ 0. If Ψ(q,τ) < 0, continuity of K^♭ at q (N25 Thm 3.3(c)) would put a neighbourhood of q, which meets A_τ, into {Ψ < 0}. So Ψ(q,·) = 0 on [a,b], hence ≤ 0 on ℝ (caps(a)).
- An open half-plane through p\* that misses a co-countable subset of λ has boundary λ. So λ⁺_τ = λ for every τ, and the sign contradiction runs as in the writeup.
- **CONFIRMED.**

**Anchors (Lemma rotation, Props regularity and blowup).**
- caps(c) is used only as upper semicontinuity of ∂⁻_τΨ at the *limit* point (q_{τ₁}(ξ), τ₁), and lower semicontinuity of ∂⁺ at the mirror anchor.
- ∂⁻Ψ(q,τ) = inf_s [Ψ(q,τ) − Ψ(q,τ−s)]/s is an infimum of functions continuous at (q,τ) whenever q ∉ E. K^♭ is continuous at q along every sequence, and P is Lipschitz in (K,h). That suffices.
- The approaching anchors q_{τ₀}(ξ) may lie in E: sandwich and caps(b) are pointwise.
- One ξ with p\* ± ξu_τ ∉ E is needed per τ used. That τ ranges over three points in regularity (a), and one τ at a time in (b), (c). Such ξ form a co-countable set.
- Blow-up (N15 §6, re-read): Arzelà–Ascoli in τ, (M), sweep and window are all pointwise in q.
- **CONFIRMED.**

Repair (wording only): the table entry "Ψ is jointly continuous at (q,τ) for every q ∉ E" is exactly what is used. No continuity at the approaching anchors is needed.

### 1.2 The ball lemma and Prop F (priority)

Re-derivation of the parts used.
- *Step 2.* For good h_t, h_{t′} ∈ Z_x with t < t′: a.e. q ∈ H(h_{t′}) has P(q,h_t) = P(q,h_{t′}) + (t′−t) > 0. So H(h_{t′}) ⊆ H(h_t). Nested open half-planes whose lines pass through the interior point x coincide.
- *(★).* Let b(g) = ess sup J and a(g) = ess inf J. Then P(q,g) ≥ b(g) a.e. on H(L) and ≤ a(g) a.e. on the opposite side. If L ≠ L′ (including L′ = −L), the sectors S₊₋ and S₋₊ are non-empty and open. 1-Lipschitz continuity in the sup norm gives (b−a)(g) + (b−a)(g′) ≤ 2d.
- *Ball lemma.* Fibres through the half-ball have tie spread ≥ η. (★) forces equal lines within distance < η. A chain argument on the disc of fibres gives one oriented line, which fixes c up to a positive factor (aff Δ spans ℝ³).

So the ball lemma rests on Prop F steps 1–4, now read twice (N25_referee and here). **Prop F step 5 (no fans) is not used in Theorem R.** Countability of E on non-chord lines comes from N25 Thm 2.1.

### 1.3 Does A2 exclude P1's mid-facet atoms? (priority)

**No.**
- Prop 4.1(ii) concerns S = D_{T1} ∖ D_{K^♭_{p\*}} ⊆ D_{T1}. P1's mid-facet atoms lie outside cl D_{T1} (P1 §4.3(a)), in Z_{p\*} ∖ S.
- Nothing in A1–A3 or in Cor 4.4 constrains non-carrying atoms through p\*. "p\* is a common point of at least three chords" is explicitly a lower bound.
- So neither note is in error on this point. P1's atoms are excluded only by the new Prop R.2 (§5), and P1's escape configurations are in any case covered by Theorem R.

---

## 2. P1: verdicts

| Claim | Verdict | Note |
|---|---|---|
| §1.1 (on M_U, I1, I2, C2 reduce to the §4 chain) | **CONFIRMED** (reading) | Same as P4 §3.1 |
| §1.2 table | **Superseded** | "PL2 broken across chords" is repaired by P4 Lemma 2.7. "R-b′ open" is closed by A1 |
| Lemma P1.2 (straight levels for K^♭ at every q) | **CONFIRMED** | Identical to P4 Lemma 2.1 with A = ∅ |
| Lemma P1.1 | **CONFIRMED** | b ≤ 1 from ab ≤ κ; a ≥ 1 from ab ≥ 1/κ; cyclically all x_k = 1, then 2 ≥ κ+1. Sympy and random checks rerun: 0 feasible |
| P1.1 box bounds (upper ones from the Prop T1 certificate; lower ones from the mirror) | **CONFIRMED WITH REPAIR**: upgrade the lower bounds to **PROVED** | Upper: the (1,2) certificate with general data gives x₁x₃ ≤ κ, then cyclic images. Lower: c^σ has facet data (1/x₂, 1/x₁, 1/x₃) (sympy, `m0ref_py/transpose_box.py`), so its upper bounds read x_kx_{k+1} ≥ 1/κ. NUMERICS: an own brute-force box search agrees in sign with the product criterion on 75/75 random data, to within 0.02 in log |
| Lemma P1.3 (corner atom ⇒ x_k + 1/x_{k+1} > κ+1) | **CONFIRMED WITH REPAIR**, conditional on (HC) | Algebra: t₃ = x₃/(κ+1), t₁ = 1 − 1/(x₁(κ+1)), t₃ − t₁ = (x₃ + 1/x₁ − κ − 1)/(κ+1); sympy rerun. Strictness needs only a non-degenerate arc, even one-sided. *Scope repair:* the argument needs the arc containing the corner to be the only arc in that corner region of both adjacent facets. A further constant arc, or a crossing-free linear piece, between it and the crossing piece breaks the comparison of t₁ with t₃ |
| Theorem P1.4 | **CONFIRMED** (conditional on (HC) and the scope repair); **superseded** by Theorem R | — |
| (HC) itself | **CONJECTURE**, correctly labelled. Moot | §4 |
| §4.1 split-facet algebra | **CONFIRMED WITH REPAIR** | The one-ratio parametrisation of a piece assumes both crossing rows on each piece. (HC) gives only one row on a piece containing one crossing, leaving 3 parameters per piece. Since this adds freedom, the consistency conclusion only gets stronger |
| §4.2 NUMERICS (split facets box-consistent) | **Reproduced.** As a statement about the facet algebra: correct. As a "surviving escape": **WRONG** | `m0ref_py/tp_split.py` extends it: with all three corners *strict* (as in (TP)) and every arc carrying its chord normal, margins are −0.09 … −1.39 for small overlaps at ε ∈ {0.1, 0.3, 0.6, 0.9}. Large overlaps with the corner normal near one end produce certificates. The configuration itself is impossible (Prop R.2) |
| §4.3 (a), (b) | **CONFIRMED** | (a) is a correct implication. Combined with the ball lemma it says inside tie gambles never sit over middle arcs |
| §4.3 (c) | **CONFIRMED** up to "T1 is intermediate, S ≠ ∅". **WRONG**: "nothing local closes it" | Closed locally at the crossings (Prop R.2). Also already closed by Theorem R |
| §0 item 1 and §6 "no proof that M0 is impossible" | **Superseded** | Theorem R |

---

## 3. Adjudication of the conflict

- **No PROVED statement of either note contradicts a PROVED statement of the other.**
- The apparent conflict ("P4: ≤ 3 corner atoms" vs "P1: mid-facet atoms") is a difference of objects. The facts are:
  - carrying atoms (inside D_{T1}) are corner atoms, one per corner ray, with arcs inside the corner arcs and never reaching a crossing (P4 2.4(b), 4.1(ii));
  - P1's escape needs non-carrying atoms outside cl D_{T1} adjacent to middle arcs.
- **P4's error** is one of omission: (TP) is listed as an open residual, but it is empty. P4 applied the ball lemma to K^♭ (Lemma 2.4(b)) and to K ⊊ T1 (2.4(a)), but not to the directional limits K_δ, which are neither.
- **P1's error** is the escape. It lacked the ball lemma, so it could not see that every face model is pinned at the crossings.
- Neither note made an invalid inference inside a PROVED proof.

---

## 4. Does P4 supply (HC)? (Task 3)

**No.**

What P4 does supply:
- (HC) needs straight levels at every q. These are given by P1.2 = P4 2.1.
- (HC) needs PL2/nopin across sector boundaries. These are given by P4 2.7, 2.8, valid for every open connected G, chords allowed.

What P4 does not supply:
- (HC) also needs the chain to start at p\* in each sector: Ψ(p\*,·) = 0 on the relevant facet pieces for the family used, and continuity at p\* for Steps 3–5, nosliding, rotation and blow-up. Theorem 3.1 has p\* ∉ E as a hypothesis.
- In (TP), P4 itself proves that no admissible family passes through T1.
- So P4 gives two of the three ingredients P1 lists under (O1), but not evaluation at p\*.

After Theorem R this question is moot.

---

## 5. New results (PROVED here; one reader)

### 5.1 Setting

Standing data:
- c is strictly signed and integrable on M_U, with B_q coherent for a.e. q ∈ int Δ (property (γ));
- p\* ∈ int Δ and D_{T1} = B^s_{p\*} ∪ S with S ⊆ Z_{p\*} (property (α)).

A **p\*-face model** is a credal set K with D_K = B^s_{p\*} ∪ R mod null for some R ⊆ Z_{p\*}, so that D_K △ D_{T1} ⊆ Z_{p\*} and D_K ⊆ U. Examples are K^♭_{p\*}, every directional limit K_δ (δ generic; N25 Lemma 3.1) and T1 itself.

On F_k write φ_K(τ) := P_K(h(τ)), with crossings at τ_i < τ_j. The *middle arc* is h((τ_i,τ_j)) and the *corner portions* are h([0,τ_i)) and h((τ_j,1]).

### 5.2 Prop R.1 (crossing pinning)

**Statement.** If p\* ∈ E, every p\*-face model K has P_K(w) = 0 at all six crossings w, and P_K ≤ 0 on all six corner portions.

**Proof.** Let w ∈ relint F_k with w_c = 0.
- *If P_K(w) > 0.* Put g₁ := w − s(𝟙 − e_c), with 0 < s < P_K(w).
  - Then (g₁)_c = 0 and P_{T1}(g₁) ≤ v_k·w − s(1 − v_{k,c}) < 0.
  - Also P_K(g₁) ≥ P_K(w) − s > 0.
  - So a ball centred at g₁ lies in D_K ∖ cl D_{T1} ⊆ Z_{p\*}, mod null.
- *If P_K(w) < 0.* Put g₂ := w + s(𝟙 − e_c).
  - Then (g₂)_c = 0, P_{T1}(g₂) ≥ s(1 − max_{T1} m_c) > 0, and P_K(g₂) < 0.
  - So a ball centred at g₂ lies in D_{T1} ∖ cl D_K ⊆ S ⊆ Z_{p\*}.
- Either case contradicts P4 Lemma 2.3 at x = p\*, since a ball centred on {g_c = 0} meets two orthants in non-null sets.
- So φ_K(τ_i) = φ_K(τ_j) = 0. φ_K is concave on ℝ, so it is ≤ 0 off (τ_i,τ_j) (write τ_i as a convex combination of τ < τ_i and τ_j). ∎

NUMERICS sanity (`crossing_balls.py`): 9600 crossing constructions, 0 failures; facet profiles concave.

### 5.3 Theorem R (no cover in case M0)

**Statement.** Under (α) and (γ) there is a contradiction. Hence, under (H_M0), with or without (E_ψ), no ranking covers T1 on M_U.

**Proof.**
1. p\* ∈ E: P4 Theorem A1, via Theorem 3.1.
2. S is non-null and carried by corner atoms: P4 Prop 4.1(i), (ii).
   - Take one, G, on a chord ℓ ∋ p\*, with arc α around a corner ray r = r_kj.
   - Then α ∩ relint F_k is a non-empty open interval inside a corner portion of F_k: α contains no crossing (P4 2.4(b)).
3. If π⁺ ≡ 0 on an open sub-interval of α ∩ relint F_k, P4 Theorem 4.3 (full case, A = {δ·c > 0} with δ·b > 0) gives a contradiction. So there is h ∈ α ∩ relint F_k with π⁺(h) > 0. Also π^♭(h) < 0 (P4 Lemma 4.2).
4. Take δ generic with δ·b > 0. Then G ⊆ Z_{p\*} ∩ {δ·c > 0} ⊆ X_δ(p\*) = D_{K_δ}.
   - For 0 < s < π⁺(h), the point h − s𝟙 lies in the open set {π^♭ < 0 < π⁺}. That set is contained in G mod null (N25 Thm 4.1(d)), hence in the open convex set D_{K_δ}.
   - So P_{K_δ}(h) > s > 0.
5. h lies in a corner portion, so Prop R.1 gives P_{K_δ}(h) ≤ 0. Contradiction. ∎

In particular P4's (TP) is empty, and so is every configuration of P1 §4 (all of them have p\* ∈ E and S ≠ ∅).

### 5.4 Prop R.2 (no face model is positive on a middle arc)

This is not needed for Theorem R. It is the direct reason P1's mid-facet arcs cannot exist.

**Statement.** If p\* ∈ E, every p\*-face model K has P_K ≡ 0 on every closed middle arc. Hence P_K ≤ P_{T1}, i.e. K ⊇ T1, and Z_{p\*} ⊆ D_{T1}, i.e. S = Z_{p\*}.

**Proof.** Suppose φ_K(τ₀) > 0 for some τ₀ ∈ (τ_i,τ_j).
- *Shape of φ_K.* By R.1 and concavity, φ_K > 0 on (τ_i,τ_j) and φ_K < 0 on (τ_j, 1].
- *Two atoms.* The outer shell {h − s𝟙 : 0 < s < φ_K(h)} over the middle arc M lies in Z_{p\*}, and so does the inner shell {h + s𝟙 : 0 < s < |φ_K(h)|} over the corner portion C beyond w := h(τ_j).
  - By (★) and connectedness, each shell lies in one atom: G_m (middle pattern) and G_c (corner pattern).
  - Both chords pass through p\*, and ℓ_m ≠ ℓ_c, since the patterns are neither equal nor opposite.
- *Fibre bounds.* The fibre relation gives:
  - on M: π^♭_m ≤ 0 < φ_K ≤ π⁺_m;
  - on C: π^♭_c ≤ φ_K < 0 ≤ π⁺_c.
- *Cliff (N25 Thm 4.1(f)).* For q ∉ E:
  - P(q,·) > 0 on M if q ∈ H⁺_m, and ≤ 0 on M if q ∈ H⁻_m;
  - P(q,·) ≥ 0 on C if q ∈ H⁺_c, and < 0 on C if q ∈ H⁻_c.
- *Values at w.* By concavity and homogeneity of P(q,·), and by 1-Lipschitz limits at w:
  - P(q,w) > 0 on the sector H⁺_m ∩ H⁺_c;
  - P(q,w) = 0 on the two opposite sectors H⁺_m ∩ H⁻_c and H⁻_m ∩ H⁺_c (all minus E).
- *Contradiction.* {P^♭(·,w) ≤ 0} is convex (P4 2.1 / P1.2). It contains the two opposite open sectors at p\* off a null set, so it contains points of H⁺_m ∩ H⁺_c ∖ E. Contradiction.
- *Consequences.* So φ_K ≤ 0 everywhere on ∂D_{T1}, and P_K ≤ P_{T1} by the 𝟙-shift. Applied to K_δ for a countable dense set of generic δ: Z_{p\*} ∩ {δ·c > 0} ⊆ D_{T1}, hence Z_{p\*} ⊆ S. ∎

Reading.
- Every face model at a target weighting on an atom chord contains T1. So T1 must be the accepting extreme in every direction, and every carrying atom is full.
- That is exactly the case P4's short argument (Theorem 4.3) kills.
- The single-chord fact of N26 Prop 4.3 ("T1 is the accepting extreme") holds at any crossing of chords.

---

## 6. Task 4: do P1.1 + P1.3 + (HC) exclude (TP)?

- **Within (HC):** only in the sub-case where the three corner arcs are the only arcs (one per corner region). With mid-facet arcs, the (HC)-algebra with strict corners is box-consistent (NUMERICS above). So the (HC) route alone would leave "(TP) + mid-facet arcs".
- **Unconditionally:** (TP) is excluded by Theorem R, which uses neither (HC) nor P1.1 nor P1.3. The (HC) route is not needed.

---

## 7. The established statement

**Theorem R (PROVED; this report, one reader).** Fix ε ∈ (0,1), 0 < s < 1, K′ = u + s(T1 − u), U = D_{K′}.

- (a) *Additive form.* No strictly signed integrable field c on M_U whose Bayes models are coherent at a.e. interior weighting has D_{T1} as a Bayes model at an interior weighting. This strengthens writeup Theorem main, which assumed (BU) at *every* interior q.
- (b) *Rankings.* No ranking on M_U with strict (G), (IB), (LA), (S), (C), T1 ∈ C_L, and every world adding up (case M0) exists. (E_ψ) is not needed.

**Corollaries.**
- Every ranking on M_U that covers T1 has a world failing SP^reg, i.e. mode (M1) or (M2).
- Q1 of writeup §8.1 is answered negatively on M_U.
- Residuals R-a′ and R-b′ of writeup §7.6 are both closed.
- No ranking in 𝓛₂ˢ covers T1 on M_U, since its primary endorses every comparison. Conjecture N26.R and Prop R1N26 are no longer needed for this.
- P4 Theorem A3 is a special case.

**Dependencies.**
- (D1) Writeup Prop M0 (α), (γ), without (E_ψ): N17 Prop 2.1 / N19 §2.2, N13 Prop B, N19 Prop R3(a). Only used for (b).
- (D2) N25 Thm 2.1 (E = chords ∪ countable set), Lemma 3.1 (directional limits coherent), Lemma 3.2, Thm 3.3 (K^♭ coherent and u.s.c., continuous off E), Thm 4.1 (b), (d), (e), (f) (atom anatomy, frozen fibres, cliff). Confirmed once (N25_referee).
- (D3) Prop F steps 1–4 (one line per fibre; (★)): N25_referee, re-derived here (§1.2). **Not** step 5.
- (D4) P4 Lemmas 2.1, 2.2, 2.3, 2.4(b), 2.7, 2.8 and Theorem 3.1. The latter is the writeup §4 chain, refereed twice, with E-robust edgebox (N25 Prop 9.2, confirmed), Prop T1 algebra, and the projective rescaling and transposition, which preserve (γ). Together these give Theorem A1.
- (D5) P4 Prop 4.1(i), (ii), Lemma 4.2 and Theorem 4.3 (full case, on sub-intervals).
- (D6) Prop R.1 (this report).
- **Not used:** (E_ψ); Prop F step 5; (HC); P1.1; P1.3; N26 results; Theorem ccibu; lexicographic structure; P4 Part B.

**Status and scope.**
- P4 Part A has now had one referee (this report). Prop R.1 and Theorem R have one reader. A second reading of Prop R.1 together with Theorem 3.1 would promote Theorem R to the writeup's "refereed once" standard.
- *Scope beyond T1* (CHECKED by reading, not written out): Prop R.1, Prop 4.1 and Theorem 4.3 use only Lemma signs, corner and middle patterns, and the odd-vertex cut. Theorem 3.1's general case rests on the R15 algebra. So the same proof should apply to every all-facing triangle in general position.

**What remains open for T1 on M_U:** only modes (M1) and (M2), i.e. conjecture N17.B′ in three worlds.
