# N25 referee report (exceptional-tie case M0: structure of E(ψ), what (S) forces, what is left)

14 Oct 2026. I am an independent referee and did not write N25. I re-derived every PROVED claim against its sources:
N13 Prop B; N19 §2.2 (the M0 form of (W)); N22 Thm 2.1, Cor 2.3, Remarks 3.3, Prop 4.1 and §4; N24 §§2, 4, 6;
N15 / writeup §4; R2 Thm 7; R7; N9. I read the glossary, BRIEF5–8 and the writeup first.
- Verdict scale: CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.
- New results here are labelled PROVED (full proof given) or NUMERICS.
- Script: `n25ref_py/patterns.py` (NUMERICS only). It lists the sign patterns around ∂D_{T1} at ε = 0.3 and finds the
  6-cycle −+−, −++, −−+, +−+, +−−, ++−. No verdict rests on it.

---

## 0. Headline

1. **Claim 1 is correct, but fans never occur.** Prop F (§2, PROVED) shows that **no ψ with strict signs on M_U whose
   Bayes models are coherent at a.e. weighting has a fan point.** Only (γ) is used: no (E_ψ), no (S), no lexicographic
   structure. So E(ψ) = ⋃_k(ℓ_k ∩ int Δ), a countable union of atom chords.
2. **Consequences.**
   - A cover forces *every* supporting assessment to have atom chords: a(ψ) > 0 for every ψ ∈ 𝒩, so a\* > 0.
   - Residual R-c is closed, and so is the fan half of R-a.
   - CONJECTURE N25.L is vacuous: a countable E is empty.
3. **(E_ψ).** It is stated correctly and is genuinely needed for Claims 6–9. N22 and N24 do **not** supply it. It is
   the countably additive case of M0, the M0 analogue of the hypothesis of N22 Prop 4.1.
4. **Consistency with N26.**
   - N26.5's proof and N26.7's proof use the lexicographic class essentially. They do not transfer to N25's setting.
   - N26.5's *conclusion* "no isolated exceptional points" does hold in N25's setting, by Prop F (an independent,
     purely additive proof).
   - N26.5's other conclusion, "no 2-dimensional interior face", is not established in general. Crossings of two atom
     chords are not excluded.
   - N26.7 (p\* ∉ E) is not established in general. R-a survives in its atom form.

---

## 1. Verdict table

| Claim | Verdict | Note |
|---|---|---|
| N25.1 (Thm 2.1, Cor 2.2) | **CONFIRMED**, strengthened | Every step re-derived. Prop F adds F = ∅, so E = ⋃ atom chords. Every atom chord cuts off one vertex: b has no zero coordinate, so ℓ misses the vertices (Thm 4.1(a)) |
| N25.2 (Lemma 3.1, 3.2, Thm 3.3) | **CONFIRMED** | Rays avoiding D_q meet E countably; {q·c = 0 = δ·c} is the atom set of the line through q in direction δ; the boundary of a cone with interior is null; Straszewicz plus compactness |
| N25.3 (Thm 4.1) | **CONFIRMED** | Frozen support (e) holds on the support of μ\|Π. The cliff (f) uses only density points of G. (g) checks by Fubini on U × ℓ° |
| N25.4 (Thm 5.1) | **CONFIRMED but VACUOUS** | Prop F: fan points do not exist |
| N25.5(a) (Lemma 6.1) | **CONFIRMED** | The triple-overlap count and the affine-in-s argument check, including the case b₁ ∥ b₃ |
| N25.5(b) (Thm 6.2, Cor 6.3) | **CONFIRMED WITH REPAIR** | Normalise the *charges* (‖ν_k‖ ≤ 1), not ∫\|c_k\| ≤ 1, so that Σw_kν_k converges and its CA part is ψ^w. Under (E_ψ) nothing changes. With Prop F, a\* = 0 gives E(ψ\*) = ∅, which is impossible for a cover (§3) |
| N25.5(c) (Prop 6.4) | **CONFIRMED**; (c) vacuous | Rescaling invariance and fixed-x countability check |
| Lemma 1.1, Lemma 1.2 | **CONFIRMED** | Lemma 1.1 also uses (E_ψ), although §0 says (E_ψ) is used "only in §§1.2, 7–9". Pointwise minimisers at any w ≠ 0 are regular |
| N25.6 (Lemmas 7.1, 7.2, Cor 7.3) | **CONFIRMED** (needs (E_ψ)) | The tail-worsened X_M is regular and is ⪰_i every tail model by (G). Closed sections then apply. ∫_{S_M}ρ_i → 0 needs ψ integral |
| N25.7 (Lemma 7.4) | **CONFIRMED** | — |
| N25.8 (Thm 7.5, Cor 7.6) | **CONFIRMED** | Same-ball classes are strict antichains, and \|λ\| ≤ max\|w_i\| gives the Lipschitz graphs. (a) has no fans to apply to, but it applies verbatim to 2-dimensional faces at crossings of atom chords. In (c) the word "regular" can be dropped (regularise Z) |
| N25.9 (Lemma 8.1, Thm 8.2) | **CONFIRMED** | The (IB) contexts lie in A^c because B^s_t ∩ Z_t = ∅ and U ∩ −U = ∅. In (c), θ' ↑ θ gives the strict increase at i ≠ j, Lemma 7.4 gives C_{p̄} = B^s_t ∪ S_θ, and ∫_{S'}\|c\| ≥ ∫_{S_θ}\|c\| ⇔ no worse at i ≠ j |
| N25.10 (Thm 9.1) | **CONFIRMED WITH REPAIR** | "q ↦ P(q,h) has no limit at p\*" is not proved; read it as "does not converge to P_{T1}(h) = 0". This is all N15 needs. Location claims: CONFIRMED (6-cycle; σ and −σ are antipodal on it) |
| N25.11, Prop 9.2 (edgebox E-robust) | **CONFIRMED** | Agrees with N26 §4.3 |
| N25.11, Prop 9.3 (CHECKED: no localisation) | **CONFIRMED as a reading of the proof as written**, with a caveat (§5) | — |
| CONJ N25.L | **Vacuous** | Countable E means E = ∅ by Prop F. Replace it by the chord version (§5) |
| N25.12 | **CONFIRMED** | — |
| §10 residual table | **Superseded** | See §6 |

No step is WRONG. There is no GAP in any PROVED claim beyond the two local repairs.

---

## 2. Claim 1 and fan points (priority 1)

**Claim 1 as stated.**
- §2.1: silence minus acceptance equals t·c(g). The formula Φ′(t;δ) + Φ′(t;−δ) = ∫_{Z_t}|δ·c| holds by dominated
  convergence, since ρ_i ∈ L¹.
- c ∝ 𝟙 on Z_t would force c = 0. So V is differentiable along aff Δ exactly off E. Danskin gives the face.
- §2.2: μ(Z_q) = m(Π_q), and two great circles Π_q, Π_{q′} meet in two antipodal points. Hence F is countable.
- Corollary 2.2 follows.
- All correct.

**Prop F (PROVED). No fan points.** Let c be a strictly signed integrable field on M_U such that, for a.e. q ∈ int Δ,
B_q = D_{K_q} a.e. Then m_c(Π_x) = 0 for every x ∈ int Δ, so F = ∅ and E = ⋃_k(ℓ_k ∩ int Δ).

*Proof.*
1. **Good gambles.** By Fubini on (q,g), for a.e. g: [q·c(g) > 0] ⇔ [P(q,g) > 0] for a.e. q. Call such g good. For
   a.e. g, a.e. point of the fibre g + ℝ𝟙 is good.
2. **One line per fibre.** Let h_t := g − t𝟙 and h_{t′} with t < t′ be good. For a.e. q ∈ H(h_{t′}),
   P(q,h_t) = P(q,h_{t′}) + (t′ − t) > 0, so q·c(h_t) > 0. Hence H(h_{t′}) ⊆ cl H(h_t) a.e., and so
   H(h_{t′}) ∩ int Δ ⊆ H(h_t).
   - If both h_t and h_{t′} lie in Z_x, both boundary lines pass through x ∈ int Δ. Nested half-planes whose lines
     share an interior point coincide.
   - So all good points of Z_x on one fibre share one oriented line L(g) through x.
3. **Cliff.** Put J(g) := {t : h_t good, h_t ∈ Z_x}, a(g) := ess inf J and b(g) := ess sup J. Using a countable dense
   set of good t ∈ J:
   - P(q,g) ≥ b(g) for a.e. q ∈ H(L(g));
   - P(q,g) ≤ a(g) for a.e. q in the open opposite side.
4. **Two fibres.** Let g, g′ be good fibres, with representatives at sup-distance d, and with oriented lines L ≠ L′,
   both through x.
   - The sectors S₊₋ = H(L) ∖ cl H(L′) and S₋₊ are non-empty open sets. If L′ = −L, take S₊₋ = H(L).
   - Since P(q,·) is 1-Lipschitz in sup-norm: on S₊₋, b(g) ≤ P(q,g) ≤ P(q,g′) + d ≤ a(g′) + d; on S₋₊,
     b(g′) ≤ a(g) + d.
   - Adding: |J(g)| + |J(g′)| ≤ 2d. (★)
5. **Contradiction.** Suppose m_c(Π_x) > 0, and let Z^c_x be the part of Z_x whose directions are not atoms of m.
   - Fubini gives η > 0 and a set A_η of good fibres, of positive 2-measure in 𝟙^⊥, with |J| > η and non-atomic
     direction.
   - For fixed φ, the fibres of A_η carrying the line L(φ) lie in γ^{−1}(γ(φ)) ∩ Z^c_x, which has μ-measure
     m_c({γ(φ)}) = 0. So they form a 2-null set, and a.e. pair in A_η × A_η has distinct lines.
   - At a density point of A_η, pick such a pair within distance η/2. Then (★) gives 2η < η. ∎

*Remarks.*
- Prop F uses only (γ). It therefore holds for every member of 𝒩, under M0 with or without (E_ψ).
- (★) also constrains atoms. Two atom chords crossing at an interior point, or G and G′ on one chord, must have
  𝟙-saturations separated in the quantitative sense of (★). That is not a contradiction, and crossings of atom chords
  remain possible as far as I can tell. At such a crossing the face is a 2-dimensional parallelogram.
- N22 §4's unverified sketch ("nested open half-circles … hence equal") is the one-fibre version of step 2. Steps 3–5
  are what turn it into an exclusion.

**Answer to priority (1).** The structure claim is correct, and fan points are **not** possible for any ψ arising on
M_U with n = 3. Thm 5.1, Remark 5.2 ("a fan at p\* is the natural escape"), Prop 6.4(c) and Cor 7.6(a)-for-fans are
vacuous.

---

## 3. The hypothesis (E_ψ) (priority 2)

**Stated?** Yes, explicitly, in the standing hypotheses. It is used in:
- Lemma 1.1 (§1.1, not listed in §0);
- Lemma 1.2;
- §7 throughout;
- §8.

**Needed?** Yes.
- **Lemma 7.1.** With charges, ν_i(S_M) need not tend to 0. This is exactly the failure N22 Remarks 3.3 diagnosed.
- **Lemma 1.2.** Endorsement by ν gives ψ_i(C) + ν^s_i(E_iC) ≤ ψ_i(Y) + ν^s_i(E_iY), with the singular parts
  uncontrolled. So the brief's premise (N25.12) fails to follow.
- **Thm 7.5** itself goes through without (E_ψ) for the *charge* profile φ = ν∘E. Every inequality in its proof is an
  endorsement inequality. But Cor 7.6 and §8 need it on ψ-faces, so (E_ψ) is needed there.

**Supplied by N22/N24?** No.
- N22 Thm 2.1, as refereed in N24 §2.1, gives only (α)–(δ) for the CA part. Only (W) for the *full* charges is used.
- N22 Prop 4.1 is the exact (CP-a) analogue of N25 §§1.2/8, and it *assumes* that P consists of countably additive
  members.
- N24 Prop R2 produces a detecting member under (CD), but that member is still a charge.
- In M0 form, (E_ψ) is the CA case of N19 §2.2 (Prop 2.1). That source is the one that shows (W) is needed only against
  regular X.

So the import of (α)–(δ) for M0 should cite N19 §2.2 together with N13 Prop B, rather than N22 Thm 2.1 alone, which is
stated for (CP-a).

**Consequence (PROVED, without (E_ψ)).** Under (H25) + (M0), every ψ ∈ 𝒩 satisfies (α)–(δ).
- If E(ψ) = ∅, ψ would be a realisation of T1 at p\*(ψ), contradicting Thm main (the N22 Cor 2.3 / N24 §2.2 argument).
- So E(ψ) ≠ ∅, and by Prop F it contains an atom chord.
- Hence a(ψ) > 0 for every ψ ∈ 𝒩, and so a\* > 0. Thm 6.2 is not needed for this, although it adds the universal
  atom set A\*.

---

## 4. Claims 7 and 9 (priority 3)

**Claim 7 (Thm 7.5, Cor 7.6).** CONFIRMED.
- The countable base gives, for each p ∈ I_j, a ball B(p) on which competitiveness and (E_ψ) give
  ψ_i(C_q) ≤ ψ_i(Z_p) ≤ ψ_i(C_p) for some i ≠ j.
- Within one ball class the projected profiles form a strict antichain.
- An antichain in ℝ² for the strict order is a 1-Lipschitz graph over 𝟙^⊥.
- (b): the odd world's projection of an atom face is strictly monotone, since the two other coordinates of b share a
  sign. So it meets each antichain at most once.
- (a) applies to every 2-dimensional face. After Prop F, the only such faces are at crossings of atom chords.

**Claim 9 (N25.10 / Thm 9.1: p\* ∈ E blocks the N15 chain).** CONFIRMED WITH REPAIR.
- X_δ and X_{−δ} differ exactly on Z_{p\*}, so one of K_{±δ} differs from T1.
- The shift h₀ = g₀ − P_{T1}(g₀)𝟙 lands on ∂D_{T1}, and K_{p\*+s_mδ} → K_δ.
- What is proved is that P(·,h) does not tend to 0 = P_{T1}(h) along the ray. "No limit" needs two directions with
  different values, which is not shown. The repaired statement is what N15 Step 1 and Lemma levels at p\* need, so the
  blocking conclusion stands.
- If p\* ∈ ℓ°, the affected h lie in cl(G ∪ G′) ⊆ cl(O_σ ∪ O_{−σ}). On the 6-cycle, σ and −σ are antipodal. So the
  affected h are one middle arc and the opposite corner region, as stated.

**Addition (CHECKED).** N26 Prop 4.3 is stated for *any* strictly guiding error-weight field. Its proof uses only Lemma
signs, the face-extreme sandwich and the single-pattern hypothesis. So it transfers to N25:
- if p\* ∈ ℓ°, G′ is null and no other chord passes through p\*, then T1 must be the accepting extreme B^s ∪ G;
- the rejecting extreme D_{K^♭} = T1 ∖ R has R near a single corner ray, so σ is a corner pattern.
This narrows R-a but does not close it.

---

## 5. Localisation (priority 4)

Prop 9.3 is an accurate account of where the proof **as written** uses Hausdorff continuity: Lemma levels, Thm pivot
Steps 0–5, and Lemma nopin/PL2 on co(G ∪ V_l). Those sets sweep int Δ. The label CHECKED, as a statement about the
proof, is right. Two caveats.

- **(i) Many global steps are E-robust when run on int Δ ∖ E.**
  - K is Hausdorff-continuous relative to int Δ ∖ E (N24 R1(a)), and E is null.
  - Straight levels hold for a.e. g by step 2 of Prop F, with no continuity.
  - Lemma chords transfers by the density argument of §2.
  - So "needs continuity on all of int Δ" overstates the genuine dependence. What really crosses an atom chord is:
    - Lemma PL2's clopen argument for α_v/β_v on co(G ∪ V_l). Vertex pinning could switch across a chord.
    - Evaluation at p\* when p\* ∈ E.
  - A heuristic worth testing: a jump of α/β across ℓ at a crossing w would put collar gambles of both signs of w_c
    into the atom on ℓ, while an atom has a single sign pattern. I have not made this rigorous. Label: CONJECTURE.
- **(ii) N25.L is vacuous.** Its hypothesis "E countable" forces E = ∅. The right target is the chord version, the
  general-ψ form of N26.R: N15's conclusions survive a non-empty countable union of atom chords at positive distance
  from p\* (and, for R-a, chords through p\*).

---

## 6. Consistency with N26

| N26 claim | Ingredients of its proof | Transfers to N25's setting? |
|---|---|---|
| N26.5, Thm 3.1 (no 2-dimensional interior face) | Fact 3.0 (lexicographic minimum of the secondaries), Lemma 2.2 (Lagrangian normal form for an *additive* secondary S_i via the Lyapunov joint range of (ψ_i, S_i)), (T7) = R2 Thm 7 (lexicographic staircase), Lemma 2.3 (the splice is undominated because Y ⪯_i X ⇒ ψ_i(Y) ≤ ψ_i(X) for **all** Y, together with the S_i + λ_iψ_i bookkeeping) | **No.** Every ingredient is specific to the lexicographic class 𝓛₂ˢ. A general (IB) preorder has no real-valued secondary and no multiplier |
| N26.5, "isolated exceptional points impossible" | Cor 3.2, from Thm 3.1 | The proof does not transfer, but **the conclusion holds** by Prop F (additive, (γ) only) |
| N26.5 / Cor 3.2(c), "chords do not meet" | Thm 3.1 | **No.** In general, crossings of atom chords, with 2-dimensional faces, are not excluded. Cor 7.6(a) (ideal tie-breaking a.e.) is all that is known there |
| N26.6 (rigidity) | Lemmas 2.2, 2.3 | **No.** In general only N25 Thm 4.1(g) holds: gambles in Π∖G never switch along ℓ |
| Cor 3.4(b), "vertex-cutting" | Rigidity | The conclusion **holds in general**: b has no zero coordinate (Thm 4.1(a)) |
| N26.7 (p\* ∉ E, dist(p\*, E) > 0) | Thm 3.3 rigidity + Cor 3.4(c) | **No.** Only the transferred Prop 4.3 constraint holds (§4) |

**Precise verdict.**
- N26.5's and N26.7's proofs depend on the lexicographic class, so they do not close N25's residuals.
- N25's fan points and residual R-c are closed independently, by Prop F.
- N25's R-a in its atom form (p\* on an atom chord) remains open in the general setting.
- There is no contradiction between N25 and N26: N26 is a subclass, and in it the extra exclusions hold.

---

## 7. Corrected residual configurations

Under (H25) + (M0), without (E_ψ), a cover of T1 forces:
- for **every** ψ ∈ 𝒩, E(ψ) to be a non-empty countable union of open atom chords;
- no fan points;
- each chord to cut off the vertex of its odd world.

With ψ\* generic (Thm 6.2), a\* > 0 and A\* ⊆ A(ψ′) for all ψ′.

| | Configuration | Status |
|---|---|---|
| **R-a′** | p\* ∈ E(ψ\*): p\* lies on an atom chord. Sub-cases: (i) p\* ∈ ℓ°, single pattern (G′ null); (ii) p\* ∈ ℓ° with G, G′ both non-null; (iii) p\* at a crossing of two or more chords, with a 2-dimensional face | Open. N15 cannot start (Thm 9.1, repaired). In (i), T1 = B^s ∪ G is the accepting extreme and σ is a corner pattern (N26 Prop 4.3). Under (E_ψ): N25.8(b), N25.9; in (iii) also Cor 7.6(a) |
| **R-b′** | p\* ∉ E(ψ\*), with E(ψ\*) a non-empty countable union of atom chords, possibly crossing and possibly dense | Open. Needs the chord form of localisation (§5(ii)). Under (E_ψ): Thms 4.1, 8.2, Cor 7.6(b), (c) |
| R-c (fans, a\* = 0) | — | **Closed** (Prop F + §3) |
| Fan at p\* (half of R-a) | — | **Closed** (Prop F) |

Without (E_ψ), N25's §§7–8 constraints are unavailable. What remains is the additive structure (Prop F, Thms 3.3, 4.1)
plus R-a′/R-b′.

**Suggested next steps.**
1. The chord form of N15, starting with PL2 across a single chord, using the single-pattern heuristic of §5(i).
2. R-a′(i), using T1 = B^s ∪ G: a one-sided N15 on H⁺.
3. Whether crossing atom chords are compatible with (γ) and (★).
