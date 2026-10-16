# N28 referee report (14 Oct 2026)

I did not write N28, and I treated nothing in it as correct until I had re-derived it.

**Read.**
- BRIEF8 and the Glossary of *START HERE*; BRIEF5–BRIEF7; writeup *The Contamination Triangle.tex* (all of it).
- N28 in full, and `n28py/` (rerun: the output is identical to `checks.out`).
- Sources:
  - N21 in full;
  - N23 §§0–1 and §7 (Lemma R23.1, Cor R23.2, §7.4 on N21.9, §7.6);
  - R4 in full (Thms A–C, Lemma C2, Props D, F, G1, G2, §9);
  - R10a §§1–2 (Thm V, Cor V1, V2);
  - R10b in full (Prop V, V2, UVN, Lemmas D, M, P, Thm PL, Cor PL2);
  - N27 §§0–1 (Repair 27.1, Lemma 27.2, Cor 27.3).
- R1 Prop 2.1 and N15 I used only as quoted in the writeup, R4 and R10b. "R23.1" is Lemma R23.1 of the N23 referee report; its second reading is recorded in `writeup/CHECK_REPORT.md`.

**Verdict scale.** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.

**Scripts.** All in `n28ref_py/`, with outputs `*.out` (§8). Labels for my own additions: PROVED, CHECKED, NUMERICS, as in the briefs.

---

## 0. Summary

| Claim | Verdict | Reason in one line |
|---|---|---|
| Lemma 0 (no conic N₀ needed) | **CONFIRMED WITH REPAIR** | Agrees with N27 Repair 27.1. It omits N27's two quantitative conditions (c₀ < η/√3; shrink r₁ so that \|Ψ\| < c₀ on B₁ × [0,1]). (b) is right: R10a V2(c) uses N only through openness |
| Lemma 2.1 (walls Z_{m₀} convex, relatively closed) | **CONFIRMED** | Intersection of the convex sets {P(·,h) > 0}, m₀·h > 0. The separating gamble is right |
| Lemma 2.2 (C_b open, convex) | **CONFIRMED** | N21.1 applies to 𝟙 − e_b: its level shifts are mixed and good gambles are dense |
| Lemma 2.3 (d-faces avoid fixed points) | **CONFIRMED** | R4 Thm B (closure clause) |
| Lemma 2.4 (walls inside the other facets' A-sets) | **CONFIRMED** | v_m·h > 0 on relint F_i for m ≠ i |
| N21.1 as used in §2 | **CONFIRMED** | Valid for every g ∈ ℝ³ at every level. It needs only (BU) at every interior q, (1.1) for good gambles (which holds without convexity of {P > 0}), density, and convexity of every chart |
| Options 1/2 for N21.9 walls | **CONFIRMED** | Sign bookkeeping re-derived |
| **N21.9(ii) as used in the surround step** | **CONFIRMED** | N21.9(ii) gives exactly "every segment [o,v] with o ∈ O and v ∈ V_j ∩ Ω meets Z_{v_k}". The segment lies in int conv(O ∪ V_j) ⊆ Γ, which is open and connected; o ∈ α and v ∈ β; Lemma M applies at the first point of cl β (§3.1) |
| Prop 3.1 | **CONFIRMED** | Not circular. The estimate is correct |
| Lemma 3.2 | **CONFIRMED** | R23.1 plus Thm PL on O ∩ B(p\*,ρ). Ball-shrinking is harmless |
| Lemma 3.3 | **CONFIRMED** | Case analysis re-derived |
| Lemma 3.4 (surround) | **CONFIRMED** | Elementary. The constants check (t_i ≥ (d−δ)/√2) |
| **Theorem 3.5 ((TS) in every cover; (E5a) empty)** | **CONFIRMED** | Every step re-derived. Inputs: N21.9, Lemma R23.1 / Cor R23.2 (one referee plus a second reading), Thm PL (one referee) |
| Cor 3.6 | **CONFIRMED** | (a) Theorem 3.5. (b), (c) N21.7, N21.8(b), whose only extra hypothesis was (TS) |
| Facts 4.0, 4.0′ | **CONFIRMED** | Re-derived by hand; valid for every all-facing T |
| **Theorem 4.1 (a\* = e_b)** | **CONFIRMED** | Both steps re-derived. Step 2's triangle argument gives a stronger, global statement (Lemma R1 below) |
| **Prop 4.3 (i)–(iv)** | **CONFIRMED** | (ii) and (iii) strengthen to strict inequalities on whole open half-planes (Lemma R1) |
| Remark after 4.3 ("strictly beyond ℓ′ near e_b") | **CONFIRMED, superseded** | Lemma R1 gives it on the whole open e_a-side of λ_b, PROVED |
| "The identity cap of R4 §9 cannot be part of a cover" | **CONFIRMED** (full-neighbourhood cap) | Any precise point on λ_b is excluded |
| "**That cap was the evidence … that claim no longer has support**" (§0.5, Conj. evidence, §6) | **WRONG** | Counterexample C1: the identity restricted to a vertex sector adjacent to the failing edge passes every constraint N28 derives, Lemma R1 included, and carries the cuts (NUMERICS, §4.3). R4 §9's cut mechanism never used the chord |
| Prop 5.1 (CF equivalence) | **CONFIRMED WITH REPAIR** | Re-derived. (1) The Borel/selection sketch is mis-stated: {P(·,g) > 0} is not known to be convex for an arbitrary candidate, so "test on a countable dense set" is not a valid test. Repaired in §5.1. (2) (⇐) inherits the status of Thm CCIBU (author-checked, no formal referee). (3) (⇒) needs both orientations a.e., so it is specific to T1 |
| Prop 5.2 (a), (b) | **CONFIRMED** | (b) is right. It is in fact a symmetry of the whole axiomatic framework for **arbitrary** rankings (Prop R3) |
| "Coverability depends only on the diagonal orbit" | **CONFIRMED WITH REPAIR** | As derived through Prop 5.1 it covers only T1. Prop R3 gives it directly for every T and every transport-closed class |
| Def 5.3 (E4″) | **CONFIRMED WITH REPAIR** | Each listed item holds in every cover. But (E4″) **equals** CF(T1): every CF(T1) solution satisfies 1–7 via Prop 5.1(⇐). Further repairs: boundary items must be read as limits; facet data are stated after normalising p\* = u; items 5–6 strengthen (Lemma R1); the list is not exhaustive |
| Theorem 5.4 | **CONFIRMED** | Uses only Prop 5.1(⇒) |
| CONJECTURE N28 | **CONFIRMED WITH REPAIR** (as a statement) | It is the statement "CF(T1) has no solution". "Equivalently, no additive cover" uses Prop 5.1(⇐), hence CCIBU. Its first evidence bullet is wrong (C1) |

**Overall.** The proved chain of N28 is sound. **(E5a) is empty**, **the cut apexes go to the vertices**, **no interior credal set contains a vertex of Δ**, and **no prior on a crossing chord is precise**. I found no gap in Theorem 3.5. The surround step uses N21.9(ii) exactly as N21.9 proves it.

One inference is wrong. The residual (E4″) is not stripped of its known local model: a *sector* identity cap survives. Two strengthenings are new here: Lemma R1 (PROVED) and Prop R3 (PROVED). One numerical structure result is new: precise priors near e_b can occur only on the failing-edge half of the vertex neighbourhood (NUMERICS N1).

---

## 1. Lemma 0 and N27 Repair 27.1

- **(a)** Correct. Φ is compact and lies in ∂D_T∖0 ⊆ N. P_{K″} > 0 on Φ, so a δ₀-collar exists.
  - The R10b §1 shrinking (N₀ ∩ (−cl D_T) = ∅, no h ≤ 0) makes the advice ranges {+,0} or {+,0,−}.
  - This is N27's construction with Σ replaced by a slightly larger compact set of facet gambles. The two are compatible.
- **(b)** Correct. R10a's §1 shrinks N to an open cone, but the proofs of Thm V and Cor V2(c) use only openness of N:
  - h⁰ ∈ N;
  - h⁰ ± δe_i ∈ N and h^θ ∈ N for small parameters;
  - N ∩ D_i open.

  So N ⊆ Av a.e., and Av∖{h ≤ 0} ≈ ∪D_{V_i}, a union of open cones with null boundary. Hence ℝ₊N ⊆ Av a.e. The same follows from N27 Cor 27.3(a) (ray transfer of Av).
- **(c) Repair.** "Level shifts h − c𝟙 with |c| small" must be made quantitative, as in N27 §1.2:
  - c₀ < δ₀/√3, so that h(τ) − c𝟙 ∈ int N₀ for |c| ≤ c₀;
  - r₁ shrunk so that |Ψ_k(q,τ)| < c₀ on B(p\*,r₁) × [0,1], so that the levels used in local straight levels and in the sandwich lemma stay below c₀.

  Neither condition affects anything else.
- **N28's new uses.**
  - Lemmas 2.1–2.2 use arbitrary gambles (m₀ − m + t𝟙, 𝟙 − e_b). That is legitimate because N21.1 holds for every g and needs no N₀.
  - Lemma 2.3 and Thm 4.1 use R4 Thm B (a.e. g, no N₀) and the N21.6 gambles, which lie in N₀.
- **Verdict:** CONFIRMED WITH REPAIR. Cite N27 Repair 27.1 for the quantitative choice.

---

## 2. Lemmas 2.1–2.4 and the applicability of N21.1

N21.1's proof needs:
- (BU) at every interior q (B_q ≈ D_{K_q});
- property (1.1) for good gambles;
- density of good gambles, and joint continuity of P;
- convexity of every chart in R1's table.

(1.1) does not need convexity of {P > 0}:
- {P(·,h) > 0} is open and a.e. inside R(h), hence inside cl R(h);
- R(h) is a.e. inside {P > 0}, hence P ≥ 0 on cl R(h).

All charts ({α > 0, d > 0}, {d > 0}, {c·q > 0}, ∅, Ω) are convex. So N21.1 holds for every g ∈ ℝ³ and every level, including:
- nonnegative g (the shifted gamble g − c′𝟙 is mixed);
- gambles on whose choice every evaluable model gives the same advice.

- **Lemma 2.1.** Checked.
  - (⊇): for m ∈ K_q with m ≠ m₀, take h = (m₀ − m) − ((m₀ − m)·m)𝟙. Then m·h = 0 and m₀·h = |m₀ − m|² > 0.
  - An arbitrary intersection of convex sets is convex. Closedness follows from Hausdorff continuity.
- **Lemma 2.2.** min over K_q of (1 − m_b) is > 0 iff e_b ∉ K_q, by compactness.
- **Lemma 2.3.** R4 Thm B states the closure clause (K_p ⊆ g^⊥ on cl F(g) ∩ Ω, for a.e. g).
- **Lemma 2.4.** On Z_{v_m}, P = v_m·h^i(τ) > 0 because τ ∈ (0,1) puts h^i(τ) in relint F_i. P(p\*, h^i(τ)) = 0.

**Verdict:** all CONFIRMED.

---

## 3. Theorem 3.5: the cascade

### 3.1 What N21.9(ii) gives (the surround input)

N21.9 is applied after an A-failure A^m_{τ₀} ∩ B(p\*,ρ) = ∅ with σ₁ < τ₀ < σ₂ chosen as in N15 Step 1.

- *Setup.*
  - G = int(P_{σ₁} ∩ P_{σ₂}) is convex (N21.1). It is nonempty (it contains V_l(σ₁) ∩ V_l(σ₂) ∩ Ω) and p\* ∈ cl G (a convex set with interior has every point in the closure of its interior). Put O = G ∩ B(p\*,ρ).
  - On O, concavity forces Ψ(q,·) ≡ 0 on [σ₁,σ₂], so v_m ∈ K_q (wedge argument), i.e. O ⊆ Γ ∩ α.
  - UVN(a) at the crossing w = h(τ_c), for the coordinate j with w_j > 0, gives V_j ∩ Ω ⊆ Γ ∩ β.
- *The wall.* Fix o ∈ O and v ∈ V_j ∩ Ω.
  - [o,v] lies in G′ := int conv(O ∪ V_j), because both endpoints have open neighbourhoods in the hull.
  - G′ ⊆ Γ, because charts of good h ∈ U⁺ are convex and contain O ∪ V_j (containment of the open set O needs no convexity: B ⊆ O a.e. inside R gives B ⊆ int cl R = R).
  - G′ is open and connected, so Lemma M applies in G′.
  - Let t\* be the first parameter with q(t\*) ∈ cl β. If q(t\*) ∈ β, then t\* = 0 is impossible (o ∈ α) and t\* > 0 contradicts openness of β. So q(t\*) ∈ ∂_{G′}β, and K_{q(t\*)} = {v_m}.
- *Match.* The wall points are points of the **single global** set Z_{v_m}, whatever the pinned set. Lemma 3.4 needs exactly this.

So N21.9(ii) gives what Theorem 3.5 step 4 uses. The match of j with N28's l is correct:
- Option 1: the crossing is τ_x, w_y > 0, the shared positive coordinate is y;
- Option 2: the crossing is τ_y and the shared coordinate is x.

N23 §7.4 refereed N21.9(i)–(iii) as CORRECT. Its caveat concerns only the heuristic paragraph after it, which N28 does not use.

### 3.2 Prop 3.1

1. *(TS) at τ₁ only.*
   - Local straight levels on B₁ (N21.2 ⇒ N21.4 item 1, at level 0 for h^i(τ₁) ∈ Φ) give two non-crossing lines.
   - (TS) at τ₁ puts p\* on both, so they coincide.
   - Then N21.1′ applies.
2. *c-cluster sign.* Item 5 of N21.4 needs both half-discs, i.e. (TS) at τ₁, and c(g_m)_l < 0 from strict (G). The conclusion is n·(e_l − p\*) ≤ 0. There is no circularity: the hypothesis is refuted.
3. *Choice of v.* The degenerate case n·(e_l − p\*) = 0 is handled correctly.
4. *Estimate.* n·(x − p\*) ≤ (1−t)δ − tb, so t < δ/(δ+b) and |x − p\*| ≤ δ + 2t ≤ δ(1 + 2/b). Then d ≤ δ(1 + 2/b) fails for small δ.

**Verdict:** CONFIRMED.

### 3.3 Lemmas 3.2–3.4

- **Lemma 3.2.**
  - R23.1 needs a crossing of F_l in (σ₁,σ₂) and ρ ≤ r₁. It gives B(p\*,ρ) ⊆ Γ_{v_l} ∩ α_{v_l}.
  - O′ = O ∩ B(p\*,ρ) is then open and nonempty, lies in Γ_{v_m} ∩ Γ_{v_l}, and has v_m, v_l ∈ K_q, so it is not in Z_{v_m} ∪ Z_{v_l}.
  - Thm PL needs vertices with crossings (true in general position) and admits any sufficiently small balls (smaller U⁺ gives larger Γ).
  - CONFIRMED.
- **Lemma 3.3.** "No straddle of τ_x" and "no straddle of τ_y" put β in (0,τ_x], [τ_x,τ_y] or [τ_y,1). The complement statements and the Option choices check, including the endpoint cases τ₀ = τ_x (Option 1) and τ₀ = τ_y (Option 2). CONFIRMED.
- **Lemma 3.4.**
  - |Q_i − p\*| ≤ δ + t_i√2, so t_i ≥ (d−δ)/√2.
  - Q_i − p\* = t_i(e_i − p\*) + (1−t_i)(o_i − p\*) + t_i(v_i − e_i), with error ≤ 2δ.
  - 0 ∈ int conv{e_i − p\*} is an open condition, and the weights λ_i/t_i give p\* as a convex combination.
  - CONFIRMED. `checks.py` (4) correctly shows that the smallness of δ/d matters.

### 3.4 Theorem 3.5 and Cor 3.6

- *Step 1.* Cor R23.2 turns a (TS)-failure on a facet into an A-failure on the same facet.
- *Step 2.* h^l_l < 0 on F_l (Lemma signs), and l ≠ m.
- *Step 4.* In Lemma 3.4, take (a,b,c) = (m,n,l):
  - Z = Z_{v_l} meets the segments toward V_m and toward V_n (two pinned sets, from Lemma 3.3);
  - Z′ = Z_{v_m} meets the segments toward V_l.
- *Step 5.* Lemma 2.4 with i = n (l, m ≠ n). Then conv(Z ∪ Z′) ⊆ A^n_τ ∌ p\*, which contradicts step 4.
- *Scope.* Every ingredient holds for all-facing triangles in general position.

Cor 3.6(a) follows. (b) and (c) are N21.7 and N21.8(b) (refereed in N23), whose only extra hypothesis was (TS).

**Verdict:** CONFIRMED.

*Dependency note.* Theorem 3.5 rests on several once-refereed inputs: N21.9 and N21.4 (N23); Thm PL, UVN and Lemma M (R12); Lemma R23.1 and Cor R23.2 (N23, with a second reading). The writeup should say so in its status line.

---

## 4. Theorem 4.1, Prop 4.3, and the identity cap

### 4.1 Theorem 4.1

**Facts 4.0, 4.0′.** Re-derived:
- an interior point of T has α, γ > 0 with both strict reversals, which gives w′_c w_a > |w′_a||w_c|;
- t < 0 gives m_b > 1.

**Step 2 (B-case, z\* ≠ e_b).**
- q₁ ∈ (a\*, z\*) lies in Ω and in the open H⁻ (z\* is strictly on e_a's side, e_a ∉ λ_b).
- P(q₁,w′) ≥ 0, from K_{q₁} ⊆ line(e_b,v_c) and Fact 4.0′.
- The triangle conv(I ∪ {q₁}) gives a fat zero set in B₁. Correct.

**Step 3.**
- [x, a\*] ⊆ λ_b ∩ Ω, so P(a\*,w\*\*) = 0, so e_b ∈ K_{a\*}.
- Separation from the open convex C_b ∋ p\* gives φ < 0 on (a\*, e_b].
- The d-faces (a_m, z_m) → [a\*, e_b] pass through B(y,r), and Lemma 2.3 applies (a.e. g_m, (g_m)_b ≠ 0).

Correct. **Verdict:** CONFIRMED.

### 4.2 Lemma R1 (new; PROVED): global one-sidedness of every chord

**Lemma R1.** In every cover of an all-facing T in general position on an (LF) decomposable domain, for every facet F_k and every τ ∈ (0,1):

  {q ∈ Ω : P(q, h(τ)) ≥ 0} ⊆ cl H⁺_τ, i.e. Ω ∩ (open H⁻_τ) ⊆ B_τ.

Together with N21.1′ (A_τ ⊆ H⁺_τ), the chord line λ_τ separates Ω globally. P(·,h(τ)) is > 0 only on the open positive side, < 0 on the whole open negative side, and ≤ 0 on λ_τ.

*Proof.*
1. By Theorem 3.5, (TS) holds, so Z_τ ∩ B₁ = λ_τ ∩ B₁ (writeup Thm TS).
2. Suppose q₁ ∈ Ω lies on the open negative side and P(q₁,h(τ)) ≥ 0. Let I := λ_τ ∩ B(p\*, r₁/2) ⊆ Z_τ.
3. {P(·,h(τ)) ≥ 0} is convex (N21.1), so it contains the non-degenerate triangle conv(I ∪ {q₁}) ⊆ Ω ∖ H⁺_τ.
4. There P ≤ 0 (N21.1′), so P = 0 on the triangle.
5. The triangle contains p\* + t(q₁ − p\*) ∈ B₁ ∖ λ_τ for small t > 0. This contradicts step 1. ∎

**Consequences.** These replace the CHECKED Remark after Prop 4.3.
- Prop 4.3(ii) becomes strict: K_q meets {m·h(τ) < 0} for every q in the open negative side.
- Prop 4.3(iii) becomes strict: on the **whole** open e_a-side of λ_b, K_q meets {m·w′ < 0}; on the whole open e_c-side, K_q meets {m·w < 0}.

Theorem 4.1 Step 2 is a special case.

### 4.3 Prop 4.3 and the identity cap: what is and is not excluded

- (i)–(iv) are CONFIRMED. In (i):
  - C_b ≠ ∅ because K_{p\*} = T;
  - φ(e_a), φ(e_c) ≥ 0 by limits (K_q → {e_a} at e_a, Cor 3.6(c) with V2);
  - φ(e_b) < 0, else φ ≡ 0 on aff Δ;
  - the apexes a_m ∈ cl F(g_m) ∩ Ω → e_b (Thm 4.1), and Lemma 2.3 applies.
- In (iv), the explicit identity computation P(q,w′) = t·p\*·w′ > 0 presumes p\*·w′ > 0 (true at p\* = u). It is redundant: the general singleton argument (σ = e_b) covers every p\*.
- A precise cap on a **full** neighbourhood of e_b is excluded. So is every diagonal-projective cap meeting λ_b.

**The wrong inference.** The step from "the identity cap is excluded" to "the evidence that (E4′) is consistent at vertex scale no longer has support" does not hold. R4 §9 used the cap only where the cut d-faces live. Those d-faces run from the apex to the failing edge and never reach λ_b (`r4cap_position.out`: 0 crossings of λ₁).

**Counterexample C1 (NUMERICS; `sector_cap_counterexample.out`, `sector_caps2.out`, `cut_in_writeup_coords.out`).**

*Setting.* Writeup conventions, PC data at p\* = u with x ∈ {x₊, x₋}. The failing edge at each b was recomputed from Prop 4.22(c) in `failing_edge.out`: x₊ fails at (a,b) = (1,2), (2,3), (3,1); x₋ at (2,1), (3,2), (1,3).

*Constraints tested.* For every facet and every τ ∈ (0,1), the precise identity must satisfy:
- (A) N21.1′: q·h(τ) > 0 ⇒ c_k(h(τ))·q > 0;
- (B) Lemma R1: c_k(h(τ))·q < 0 ⇒ q·h(τ) < 0.

The test is exact in τ: both sides are affine in τ, so the endpoints and both sides of both roots suffice.

*Results.*
- Near every vertex the identity passes (A) and (B) for all three facets on a sector S_b = {φ ≤ φ_max} adjacent to the **failing** edge. Here φ is the angular parameter from the failing edge (φ = ½ is λ_b). φ_max ≈ 0.367 / 0.196 / 0.127 / 0.026 at ε = .05 / .2 / .3 / .6, and the sector is very thin at ε = .9.
- The identity cut d-faces of box witnesses near the b-crossing of F_a lie in S_b at every sampled point (45/45 at every (ε, x, b)). Their apexes are at distance ≈ 5η from e_b, and they lie on the boundary ray of S_b. This is expected: the boundary of the admissible set is where q·h = 0 = c(h)·q, i.e. the apex locus.
- A sector cap is convex, so it also passes R4 Prop F's one-sidedness test.
- It also respects Def 5.3 items 2–4 and 7 at vertex scale:
  - K_q = {q} never contains a vertex for q ∈ Ω;
  - the d-faces are precise and inside g^⊥;
  - the cap is edge-confined;
  - the apexes go to e_b.

So the R4 §9 mechanism survives in sector form. What N28 adds is that the sector cannot be extended across λ_b, and that λ_b (and, by N1 below, the whole non-failing half) must carry non-precise credal sets.

*Caveat.* R4 §9's own numbers (apex at φ ≈ 0.43 from its edge) were computed with NOGO-coordinate facet maps. In the writeup's normalisation they are **not** admissible beyond φ_max. The admissible cuts are those of `cut_in_writeup_coords.py`.

**NUMERICS N1 (precise priors near a vertex; first-order blow-up; `precise_blowup_eps0*.out`).**
- *Set-up.* Prior q = e_b + ρ·(direction φ), image σ = e_b + ρz with z on a log grid over [10⁻³,10³]², ρ = 10⁻⁷, constraints (A) and (B).
- *Results, ε ∈ {.2, .3, .6}, x₊ and x₋, all b:*
  - no admissible precise image exists for any prior direction φ ≥ ½, i.e. on the closed half toward the **non-failing** edge;
  - for φ < ½, admissible images exist, confined to an image sector near the failing edge;
  - |z| → 0 as φ ↑ ½.
- *Reading.* This extends Prop 4.3(iv) from the chord to a half-neighbourhood, at the level of first-order asymptotics. CONJECTURE (referee): every precise prior near e_b lies strictly on the failing side of λ_b. It is probably a short linear-algebra lemma in the blow-up variables.

---

## 5. Reduction and symmetry

### 5.1 Prop 5.1

**(⇒)** Re-derived.
- K_q comes from Prop necessary (a), and Hausdorff continuity from R1 Prop 3.1.
- For good g, R(±g) and {P(·,±g) > 0} are open and convex (N21.1), and a.e. equal, hence equal.
- The {+,−} data (λd + e₀𝟙, (λ−1)d + e₀𝟙) give:
  - c − c′ = d;
  - R(g) = {d·q > 0} and R(−g) = {d·q < 0};
  - an empty silence cell;
  - strict signs once e₀ < λ min|d_i| and e₀ < (1−λ) min|d_i|.

  Correct.
- Cor 3.6(b) is essential. A {+,0} pair cannot be written in CF form, because c′ would have to be positive at e_l for g_l < 0, so R(−g) would contain points near e_l. So **(⇒) holds for T1 and for any target whose covers have both acceptances in the advice range a.e.**, not for every T.

**(⇐)** Re-derived.
- Penalties come from R1 Prop 2.1 (converse). Unanimous pairs get c > 0 > c′; × gets a large penalty.
- Per-pair positive rescaling gives integrability.
- At each interior q, ties lie in ∂D_{K_q} ∪ (−∂D_{K_q}), which is null.
- So the Bayes model D_{K_q} is unique and coherent, CCIBU applies, and T1 = D_{K_{p\*}} is the unique p\*-Bayes model, hence undominated.
- The status is that of CCIBU (author-checked).

**Repair (selection).** "Equality of open convex sets is tested on a countable dense set of q" is valid only once both sets are known to be open and convex, and {P(·,g) > 0} is not known to be convex for an arbitrary candidate (g,c,c′). Use instead, with C ranging over closed rational polygons in Ω:
- [C ⊆ R(c,c′) ⇒ min_C P(·,g) > 0] (this gives {P > 0} ⊇ R);
- [min_C P(·,g) > 0 ⇒ C ⊆ R(c,c′)] (this gives {P > 0} ⊆ R).

Each is Borel in (g,c,c′), since min_C P is jointly continuous and "C ⊆ R" is Borel in (c,c′). Then:
- the admissible set is Borel;
- its projection is analytic and co-null;
- Jankov–von Neumann gives a universally measurable selection, equal a.e. to a Borel one.

**Verdict:** CONFIRMED WITH REPAIR.

### 5.2 Prop 5.2, and a ranking-level version

(a) and (b) re-derived:
- ν(D′⁻¹q̃) is a projective homeomorphism of Ω;
- m·g > 0 ⟺ ν(D⁻¹m)·(Dg) > 0;
- projective maps with denominators positive on Δ preserve convexity and Hausdorff continuity;
- the sign patterns are those of g.

CONFIRMED. The notation c′(Dg) := c(g) clashes with the second chart vector c′. Write (c̃, c̃′)(Dg) := (c, c′)(g).

**Prop R3 (new; PROVED).** Let D be positive diagonal. The map X ↦ DX on models (and A(g) ↦ A(D⁻¹·) on advice ranges) preserves:
- decomposable domains, splicing and convergence in measure;
- null sets;
- world-wise guidance ranks (sign patterns);
- (IB) (A = −A is preserved);
- coherence (D·D_K = D_{ν(D⁻¹K)});
- (LF) (D·N is open and contains ∂(D·D_T)∖0).

Hence a ranking L covers D_T iff its transport covers D_{ν(D⁻¹T)}. For additive rankings, multiply the penalties by the Radon–Nikodym factor d(D_\*μ)/dμ. This is positive per pair, so it preserves charts and integrability.

So **coverability of T by any transport-closed class of rankings depends only on T's orbit under diagonal projective maps**. This holds for every T, without Prop 5.1 or CCIBU. N28's sentence after 5.2 should cite this instead.

---

## 6. Definition 5.3 and Conjecture N28

**Correctness.** Every item holds in every cover (§§3–4). Item 3's z\* ≠ e_b clause: limits along d-faces lie in ℓ ∩ [e_a,e_b] = {e_b} (edge confinement plus K ⊆ g_m^⊥ → ℓ). That is CHECKED, as labelled.

**Repairs.**
1. **(E4″) = CF(T1), not a proper sub-case.** Every CF(T1) solution comes from a cover by Prop 5.1(⇐), and so satisfies items 1–7. Either say so, or present Def 5.3 as "CF(T1), together with the following necessary conditions".
2. **Boundary items.** CF lives on Ω. "K_{e_b} = {e_b}" and edge confinement must be read as Hausdorff limits q → ∂Δ. These exist by R10b V2 once the solution is realised as a cover.
3. **Facet data.** x₊ or x₋ refer to the normalisation p\* = u (Prop 5.2(a)). For general p\* they are the transported data.
4. **Items 5–6.** Replace with Lemma R1: P(·,h(τ)) < 0 on the whole open H⁻_τ. On the open e_a-side of λ_b, K_q pokes strictly beyond ℓ′; on the open e_c-side, strictly beyond ℓ. This holds globally, not only near e_b.
5. **Optional item 8 (NUMERICS N1).** Near e_b, precise priors occur only strictly on the failing side of λ_b.
6. **Not exhaustive.** The list omits constraints that are now known: quasi-concavity of every P(·,g) (N21.1); Thm PL and Lemma M; Lemma C2 and Props D and F of R4 (precise regions); and, under (H1⁺), R4 Thm C (precise d-faces). Since the definition starts from CF(T1), nothing is lost, but the sentence "together with every constraint now known" should be dropped.

**CONJECTURE N28** is correctly stated as "CF(T1) has no solution". The two directions of "Equivalently" stand differently:
- "no additive cover ⇒ (E4″) empty" uses Prop 5.1(⇐), i.e. CCIBU's status;
- "(E4″) empty ⇒ no additive cover" uses only Theorem 5.4.

Evidence bullets:
- bullet 1 is **wrong** (C1);
- bullet 2 holds on the chords, and by N1 numerically on the non-failing half;
- bullets 3 and 4 stand.

**Where a construction would now have to live (referee summary).**
- Precise (sector) caps adjacent to the failing edge at each vertex carry the cuts.
- A non-precise layer along λ_b and the whole non-failing half-neighbourhood straddles the tangent wedge at e_b without touching e_b. On the open e_c-side it pokes strictly beyond ℓ, and on the chord beyond both ℓ and ℓ′.
- The precise sectors and the non-precise layer must be glued to the core under every concurrent chart.

The gluing across the sector boundary (precise ↔ non-precise; compare R4 Prop F and Lemma C2) is the natural next test.

---

## 7. What is established (exact statement)

Let T be T1 (any ε ∈ (0,1)). Parts (A)–(C) also hold for any all-facing triangle in general position, with (B) at every world b that has a failing box. Consider a strictly guiding additive ranking with integrable envelopes on a decomposable domain with (LF) at D_T, satisfying (LA), (S), (C) and covering D_T. Write K_q for its interior Bayes credal sets, and p\* for a prior with K_{p\*} = T. Then:

**(A) (TS), (PC), (NS) hold** (Theorem 3.5, N21.4). In particular there is no single-vertex pinning near p\* ((E5a) is empty). For every facet F_k and τ ∈ (0,1):
- {P(·,h(τ)) > 0} ⊆ H⁺_τ;
- Ω ∩ open H⁻_τ ⊆ {P(·,h(τ)) < 0} (N21.1′, Lemma R1).

**(B) Cuts reach the vertex.** At every b, the failing-box cuts of N21.6 have apexes a_m → e_b (Theorem 4.1).

**(C) Structural consequences.**
- No K_q (q ∈ Ω) contains a vertex of Δ.
- Every wall Z_{m₀} and every set {q : e_b ∉ K_q} is convex.
- For a.e. g, d-faces avoid {q : m₀ ∈ K_q} whenever m₀·g ≠ 0.

**(D) Chords (T1).**
- On each crossing chord λ_b ∩ Ω, K_q contains a point with m·w′ ≤ 0 and a different point with m·w ≤ 0, so it is non-precise.
- On the open e_a-side, K_q meets {m·w′ < 0}; on the open e_c-side, it meets {m·w < 0}.

**(E) Domain consequences (T1).**
- the advice range of a.e. mixed pair contains both acceptances;
- lim_{q→e_b} K_q = {e_b};
- edge confinement holds.

Hence T1 has no additive cover on any (LF) decomposable domain on which, for a non-null set of mixed pairs, the advice range lacks acceptance of one orientation.

**(F) Reduction (T1).** The following are equivalent:
1. T1 has such a cover on some (LF) decomposable domain;
2. CF(T1) has a solution;
3. (E4″) has a solution.

Here 1 ⇒ 2 is PROVED, and 2 ⇒ 1 holds at CCIBU's status.

**(G) Symmetry.** Coverability (any transport-closed class) is invariant under T ↦ ν(D⁻¹T), D positive diagonal (Prop R3). CF(T) is also invariant under diagonal reindexing of priors (Prop 5.2(a)).

**Open.** Whether CF(T1) has a solution.
- The full-neighbourhood vertex cap is excluded.
- Sector caps at the failing edges are not excluded (C1).
- By N1 (NUMERICS), the non-failing half-neighbourhood of each vertex must be non-precise.

---

## 8. Requested edits to N28

1. §0 item 5, Conjecture evidence bullet 1, §6 "(E4′) is closed except for vertex caps … only known consistent model excluded": replace with "the full-neighbourhood identity cap is excluded; the identity on a sector adjacent to the failing edge passes every constraint derived here and carries the cuts (referee C1)".
2. Prop 4.3(ii)/(iii) and the Remark: insert Lemma R1 (strict, global).
3. Lemma 0(c): add N27's c₀/r₁ conditions and cite Repair 27.1.
4. Prop 5.1: replace the selection sentence (§5.1 above). State that (⇒) needs both orientations a.e. (T1-specific). Status of (⇐): CCIBU.
5. The sentence after Prop 5.2: cite Prop R3 (ranking-level, every T). Fix the c′ notation clash.
6. Def 5.3: apply repairs 1–6 of §6. Theorem 3.5's status line: list its once-refereed inputs.

---

## 9. Scripts (`n28ref_py/`)

| File | Content | Result |
|---|---|---|
| `n28_checks_rerun.out` | rerun of `n28py/checks.py` | identical to `checks.out` |
| `failing_edge.py/.out` | failing box per vertex from Prop 4.22(c) with the PC data | x₊: (1,2), (2,3), (3,1); x₋: (2,1), (3,2), (1,3), at ε = .2, .3, .6 |
| `sector_caps2.py/.out` | exact-in-τ test of constraints (A), (B) for the identity along arcs around each vertex | admissible only on a sector adjacent to the failing edge; the chord always fails |
| `cut_in_writeup_coords.py/.out` | identity cuts of box witnesses in writeup conventions | apex ≈ 5η from e_b; 25/25 d-face points admissible |
| `sector_cap_counterexample.py/.out` | C1 for ε ∈ {.05, .2, .3, .6, .9}, x±, all b | φ_max as in §4.3; 45/45 cut points admissible everywhere |
| `precise_blowup.py`, `precise_blowup_eps02.out`, `precise_blowup_eps03.out` | N1: admissible precise images per prior direction | none for φ ≥ ½; images exist for φ < ½ |
| `r4cap_position.py/.out` | R4 §9 cuts in R4's own coordinates | the d-faces never cross λ₁ |

All numerics are sanity checks or exploratory (C1 and N1 are labelled NUMERICS). The verdicts in §§1–6 rest on the hand derivations. Lemma R1 and Prop R3 are proved in the text.
