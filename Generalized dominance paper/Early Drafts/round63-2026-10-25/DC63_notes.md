# DC63: direction-continuous piecewise-linear charts and the reversed triangle (25 Oct 2026)

Labels: **PROVED** (full proof here, not yet refereed) / **CHECKED** (exact computation: sympy or `Fraction`) / **CONJECTURE** / **NUMERICS** (none used).
Scripts are in `dc63py/`, each with a `.out` file; run them with `python3 -I`.

---

## 0. Verdict

**Main result (Theorem DC, PROVED).** Direction-continuous piecewise-linear charts **cannot** meet the four-condition certificate for the reversed triangle K = {m_i ≤ 2/5}. This holds on every one-sided U = D_{K'} (any compact convex K' ⊆ relint K), for every finite fan, and for every choice of positive scalar per cell.

This closes the GAP that REF62 recorded against C62 Cor 4.5 for this class.

**How the proof works.** It redoes C62 Lemmas 4.2–4.4 and the corner system for directions only:
- **Lemma 4.2-D.** Its conclusion becomes automatic. In its place there is a strict-sign lemma: u·δ is nonzero off ∂D_K.
- **Lemma 4.3-D.** It holds in projective form: on each facet the direction of c is the direction of one linear map L_k. The proof has two parts:
  - (a) a **local rescaling lemma**, which reduces most facet points to REF62's repaired Lemma 4.3;
  - (b) a new **junction lemma**, with an exact witness, which handles the facet runs where rescaling is impossible.
- **Lemma 4.4-D.** The crossing rows go through, and all six λ are > 0.
- **Corner system.** Only proportionality at the corners is available. That is exactly C62's projective system, and it has no real solution (CHECKED again, by Gröbner basis): x = y = z with 2z² − 3z + 2 = 0.

**What the theorem needs and what it does not.** It uses (C1), (C4), and (C3) only for priors in a neighbourhood of u. It uses neither (C2) nor any prior on the segments (e_k, u]. This is weaker than what C62 Thm 4.1 needs. The reason is that direction continuity removes the vanishing ("pinned") branch, which is the only reason C62/REF62 needed priors far from u. REF62's pinned counterexample is not direction-continuous.

**Does unit normalisation reduce the problem to the continuous case?** Only partly (§2).
- Normalising c to unit length gives a continuous field with exactly the same Bayes sets. But that field is not piecewise linear, so C62 Thm 4.1 does not apply to it. General continuous fields are A62's open branch S1.
- Rescaling each cell by a constant works locally, at every boundary point except along "rank-1 facet runs" (stretches of a facet where the direction of c is constant).
- It can fail globally. The cross-section of the neighbourhood of ∂D_K is an annulus, so constants may have holonomy around it.
- Neither failure matters: the facet arguments are local, the rank-1 runs are excluded by the junction lemma, and the corner system is already the projective one.

**Precise remaining gap (stop point).** The class can be widened to allow direction jumps at finitely many isolated rays, either the three corner rays (A62 S3, "sliding edge") or the six crossing rays.
- If the jumps are only at the corner rays, everything up to Lemma 4.4-D still holds on the open facets.
- The missing step is then **corner proportionality** L_a r_j ∥₊ L_b r_j, derived from (C3) near u. That is A62's N5 step lemma for discontinuous PL fields, which is still a sketch (REF62: GAP).
- I do not attempt it. It is a local lemma about finitely many cells at one ray, not a new regularity conjecture, but it is unproved.
- Jumps across a whole facet are outside this task (C62 §6.1, A62-2).

---

## 1. Setting and named hypotheses

- Three worlds; K = {m ∈ Δ : m_i ≤ 2/5}; D_K = {h : v_k·h > 0, k = 1, 2, 3}, where v_1 = (1,2,2)/5 and the others are its permutations.
- Rays: r_j = 2·𝟙 − 5e_j. Facets: F_k = cone(r_i, r_j) ⊆ v_k^⊥.
- Each facet is crossed by both of the other coordinate planes: h_i = 0 on the crossing ray w_ik ∈ relint F_k, for i ≠ k.
- **(U)** U is an open convex cone with cl D_K∖0 ⊆ U and containing no h ≤ 0 (for example U = D_{K'}). One-sidedness is never used below; only cl D_K∖0 ⊆ U is.
- **(DC-PL), the class tested.** There are:
  - a finite polyhedral fan Σ covering a conic neighbourhood N of cl D_K∖0;
  - matrices M_σ, one per cell;
  - measurable positive functions s_σ;
  - a continuous direction field δ : N∖0 → S²,

  such that c = s_σ M_σ h a.e. on each cell σ, and M_σ h ∈ ℝ_{>0}·δ(h) on int σ.
  - Equivalently: the cell maps agree in direction across every wall, and the direction field extends continuously to the walls.
  - The scalars s_σ may be discontinuous across walls. This is exactly the brief's "c = s_σ(h) M_σ h, directions matching".
- **Certificate.**
  - (C1) sign(c_i) = sign(h_i) a.e. on U;
  - (C2) every tie set {π·c = 0} is null;
  - (C3) every B_π := U ∩ {π·c > 0} is a.e. equal to a coherent cone (equivalently, under (C1), a.e. convex: A62 Lemma 1.1);
  - (C4) B_{π*} = D_K a.e. for some π* > 0.
- **Normalisation.** Replacing c_i by π*_i c_i preserves (DC-PL), because a positive diagonal matrix preserves the continuity of directions, and it preserves (C1)–(C4). So π* = u = (1,1,1).
- **Direction invariance (REF62_R2 §2.3).** B_π = U ∩ {π·M_σ h > 0 on σ} does not depend on s_σ. So from now on s_σ ≡ 1. Then c = M_σ h is piecewise linear, but it may jump in magnitude across walls.

**Hypotheses actually used:** (DC-PL) near ∂D_K∖0; (C1); (C4) with π* = u; and (C3) for all π in some neighbourhood 𝒩 of u.

---

## 2. Unit normalisation: what it does and does not give

1. **Unit normalisation (PROVED, trivial).** c̃(h) := |h|·δ(h) is continuous, positively homogeneous and sign-equivalent to c. It has B_π(c̃) = B_π(c) for every π. So a DC-PL chart is the same certificate object as a continuous chart.
   - But c̃ is piecewise *projectively* linear, not piecewise linear.
   - C62 Thm 4.1 and REF62's repaired Lemma 4.3 use kink vectors M_σ − M_τ = d nᵀ, which need value-continuity of a PL field.
   - The general continuous case is A62's open branch S1 (variable kink ratio).
   - **So unit normalisation does not by itself reduce the problem to a proved case.**
2. **Constant rescaling per cell.** Let M_σ h ∥₊ M_τ h on a wall W.
   - If M_τ has rank 2 on span W, then M_σ = κ_W M_τ on span W with a constant κ_W > 0. Indeed, M_σ M_τ⁻¹ fixes every line of a plane, so it is scalar.
   - If M_τ has rank 1 on span W, then M_σ = a(·)p and M_τ = b(·)p on span W, with linear a, b. The ratio a/b is generally **not** constant.
3. **Two obstructions to making c value-continuous by constants t_σ > 0.**
   - (i) **Rank-1 walls.** Lemma 4.2-D excludes the transversal ones. The ones lying along a facet are the "rank-1 facet runs", which Lemma 4.3-D(b) excludes.
   - (ii) **Holonomy.** The product of the κ_W around a cycle of cells must be 1. Around a vertex ray w with M_σ w ≠ 0 it is automatically 1, since M_{σ_1} w = (Π κ) M_{σ_1} w. Around the annulus surrounding ∂D_K it need not be 1. That global holonomy is precisely the per-facet scale freedom that turns C62's rank-6 continuity system into the projective system of Cor 4.5.
4. **Example (CHECKED, `junction_witness.out` part 1).** The local field built there is direction-continuous on all four half-walls at a facet point w.
   - On the left facet run, the inner/outer ratio is (2ρ + s)/ρ, which is not constant.
   - So no constant rescaling makes it continuous: obstruction (i) is real.
   - The junction lemma then shows this field fails (C3) near u.

---

## 3. Lemma 4.2-D: strict signs of u·δ, and no vanishing cell maps at ∂D_K

**Lemma 4.2-D (PROVED).** Assume (DC-PL), (C1), (C4) and (C3) on 𝒩. Then:
- (a) u·δ = 0 on ∂D_K∖0;
- (b) u·δ > 0 on int D_K ∩ N;
- (c) u·δ < 0 on N∖cl D_K;
- (d) for every cell σ and every w ∈ cl σ ∩ ∂D_K∖0, M_σ w ≠ 0;
- (e) no transversal wall through a point of ∂D_K is rank-1.

*Proof.*

**(a)** By (C4), u·c > 0 a.e. on D_K and u·c < 0 a.e. on U∖cl D_K. The sign of u·c is the sign of u·δ, and δ is continuous. So u·δ ≥ 0 on cl D_K ∩ N and u·δ ≤ 0 on cl(U∖D_K) ∩ N. Both closures contain ∂D_K.

**(b) Interior.** Suppose u·δ(h₀) = 0 at some h₀ ∈ int D_K ∩ N.
- The zero set Z = {u·δ = 0} is closed. It is null, because u·δ > 0 a.e. on D_K.
- So for a.e. x near h₀, both x and h₀' := 2h₀ − x lie outside Z, hence u·δ > 0 at both.
- Choose δ' with δ'·δ(h₀) < 0 and set q = u + tδ'. For small t > 0, q ≥ 0 and q ∈ 𝒩.
- By continuity of δ, q·δ < 0 on a ball around h₀, and q·δ > 0 on balls around x and h₀'.
- By (C3), B_q is a.e. equal to an open convex C. An open convex set that contains a.e. point of a ball contains the ball. So C contains both balls, hence a neighbourhood of their midpoint h₀. But B_q misses a ball at h₀. Contradiction.

**(c) Exterior.** Suppose u·δ(h₀) = 0 at some h₀ ∈ N∖cl D_K.
- Choose δ' with δ'·δ(h₀) > 0. Then B_q, for q = u + tδ', contains a small ball around h₀.
- Pick a direction from h₀ pointing into int D_K. Pick x on that segment near h₀, outside cl D_K, with u·δ(x) < 0. A.e. point of a small open set of such x qualifies.
- Extend the segment from h₀ through x to a point d ∈ int D_K with u·δ(d) > 0.
- For small t, q·δ < 0 near x and q·δ > 0 near d. So C contains balls around h₀ and d, hence a neighbourhood of x ∈ (h₀, d), while B_q misses a ball at x. Contradiction.

**(d)** Two cases.
- *Rank of M_σ ≥ 2 and M_σ w = 0.* Then M_σ(w + x) = M_σ x on the tangent cone of σ at w. This tangent cone is open and 3-dimensional, so the direction of M_σ x is not constant on it. That contradicts continuity of δ at w.
- *Rank 1, M_σ = p aᵀ.* Then δ ≡ p̂ on σ, so δ(w) = p̂ and u·p = 0 by (a). That makes u·δ ≡ 0 on int σ, which meets int D_K or N∖cl D_K near w. This contradicts (b) or (c).

**(e)** Let W be a transversal wall through w ∈ ∂D_K, so that near w it lies in int D_K or in N∖cl D_K apart from w itself. If M_σ has rank 1 on span W, then M_σ = a(·)p there with a(w) ≠ 0 by (d). So δ ≡ p̂ on W near w, and u·p = 0 by (a), so u·δ = 0 on W∖w. This contradicts (b) or (c). ∎

This replaces C62 Lemma 4.2 ("c ≠ 0 on ∂D_K"). It needs no prior on the segments and no (C2). The reason is that the dangerous case, c ≡ 0 on a facet, is not direction-continuous: inner cells near the facet would have u·δ > 0 up to the facet, contradicting (a).

**Consequence.** For each cell σ meeting a relatively open facet segment, u·M_σ = α_σ v_k as a linear functional, with α_σ > 0. Indeed u·M_σ vanishes on the plane v_k^⊥ by (a), and its sign is that of v_k·h by (b)–(c).

---

## 4. Lemma 4.3-D: facet direction maps are projectively linear

Fix a facet F_k. The finitely many rays where walls meet relint F_k cut it into open runs I. On each run there is one inner and one outer cell, possibly a single cell straddling the facet. The direction there is that of L_I := M_σ|_{v_k^⊥}, where σ is the inner cell. A run is **rank 2** or **rank 1** according to the rank of L_I. By Lemma 4.2-D(d), L_I ≠ 0 on cl I.

**(a) Local rescaling at a rank-2 junction (PROVED).**

*Statement.* Let w ∈ relint F_k be a point where the runs on both sides are rank 2. Then L_left ∝₊ L_right.

*Proof.*
- Every wall at w is rank 2. Transversal walls are covered by Lemma 4.2-D(e). The facet half-walls are rank 2 by assumption, and the outer map equals a constant times the inner map on v_k^⊥.
- So each wall W_i between consecutive cells σ_i, σ_{i+1} around w carries a constant κ_i > 0 with M_{σ_{i+1}} = κ_i M_{σ_i} on span W_i.
- Since M_{σ_1} w ≠ 0 (Lemma 4.2-D(d)), Π κ_i = 1. So t_{σ_1} := 1, t_{σ_{i+1}} := t_{σ_i}/κ_i is consistent around w.
- The field c' := t_σ M_σ h is then **continuous** PL on a neighbourhood of w. It has c'(w) ≠ 0, the same Bayes sets as c, the same strict signs, and u·c' = 0 on the facet, > 0 inside and < 0 outside (Lemma 4.2-D).
- These are exactly the hypotheses of C62 Lemma 4.3 as repaired by REF62 §2, which is local at w and uses (C3) only near u.
  - (i) Inner half-wall kinks d_j satisfy u·d_j ≤ 0, by the kink test at q = u + tδ' with t → 0.
  - (ii) Applying u to M_{σ_1} − M_{σ_m} = Σ d_j n_jᵀ on side 1 of the facet gives u·d_j = 0.
  - (iii) Hence d_j = κ_j c'(w), and symmetrically d'_j = −κ'_j c'(w) for the outer half-walls.
  - (iv) Comparing the two facet sides gives κ = κ' = 0.
- So c' is linear on v_k^⊥ near w: t_left L_left = t_right L_right. ∎

**(b) Junction lemma: a rank-1 run cannot meet a rank-2 run (PROVED; exact instance CHECKED).**

*Statement.* Let w ∈ relint F_k separate a rank-1 run I_L (where L_L = a(·)p, so δ ≡ p̂ on I_L) from a rank-2 run I_R. Then (C3) fails at q = u + tω for every small t > 0, for a suitable ω.

*Proof.*
- **Coordinates.** Write facet points as y(s) = w + s e, with e ∈ v_k^⊥, s < 0 on I_L and s > 0 on I_R. Take n with v_k·n = 1, so h = y(s) + r n has v_k·h = r.
- **Choice of ω.** By continuity, L_R w ∝ p. Since L_R has rank 2, L_R e ∉ ℝp. Choose ω with ω·p = 0 and ω·L_R e > 0, and set q = u + tω.
- **Left of w** (inner cell σ_L, outer cell τ_L). There M y = a(y)p and ω·p = u·p = 0, so exactly
  - q·M_{σ_L}(y + rn) = r(α_L + tγ_L),
  - q·M_{τ_L}(y + rn) = r(β_L + tγ'_L),
  - with α_L, β_L > 0 (Consequence of §3).

  So near I_L the boundary of B_q is exactly the facet r = 0.
- **Right of w** (outer cell τ_R, whose map is κ_R L_R on v_k^⊥ with κ_R > 0). Exactly,
  - q·M_{τ_R}(y(s) + rn) = tκ_R s ω·L_R e + r(β_R + tγ_R).

  So the boundary is the line r = −c_t s, with c_t > 0 and c_t = O(t): outward, and growing linearly in s.
- **The boundary graph.** It is r = f(s), with f(s) = 0 for s < 0 and f(s) = −c_t s for s > 0. This has a concave corner, so the accepted region {r > f(s)} is not convex.
- **Explicit triple, at scale S small enough to stay in the four facet-adjacent sectors:**
  - P1 = y(−S) + (c_t S/4)n, accepted (in σ_L);
  - P2 = y(2S) − (3/2)c_t S n, accepted (in τ_R);
  - their midpoint y(S/2) − (5/8)c_t S n, rejected (in τ_R).

  All three are strict and lie at interior points of cells, so B_q is not a.e. convex.
- For small t, q ≥ 0 and q ∈ 𝒩. ∎

*CHECKED (`junction_witness.out`).* At w = (−1, −1/2, 3) ∈ relint F_3, with p = (−1,−1,2) and the facet part of L_R equal to 3ρp + s(1,−1,0):
- **The field is admissible locally.** It is direction-continuous on all four half-walls, with a non-constant ratio on the left facet run. On a 400-point grid near w, (C1) and (C4) hold with 0 failures.
- **Witness at t = 1/100.** At q = (101/100, 99/100, 1):
  - q·c(P1) = 1/3000 and q·c(P2) = 1/500;
  - q·c(P1 + P2) = −1/2000.
- **Symbolically in t > 0:** the three values are t/30, t/5 and −t/20.

**(c) Facet projective linearity (PROVED).** For each k there is a rank-2 linear map L_k : v_k^⊥ → ℝ³ with δ(h) ∝₊ L_k h on all of F_k∖0, the closed facet including the corner rays.
- *Two rank-1 runs.* Two adjacent rank-1 runs have the same p, by continuity of δ, so they form one constant-direction run.
- *A rank-1 run next to a rank-2 run.* Excluded by (b).
- *Every run rank 1.* Then relint F_k is connected, so δ would be constant (= p̂) on F_k. But δ_i(w_ik) = 0 for both crossing coordinates i (§5), and u·p = 0, so p = 0. Contradiction.
- *So every run is rank 2.* Then (a) at each junction makes all the L_I positively proportional. Continuity of M_σ up to the corner ray gives the closed facet. ∎

---

## 5. Lemma 4.4-D: crossing rows (PROVED)

**Statement.** On v_k^⊥, L_k h = Σ_{i≠k} λ_ik h_i (e_i − e_k), with both λ_ik > 0.

*Proof.*
- **Weak signs.** By (C1) and continuity of δ, δ_i has the weak sign of h_i on N.
- **Zeros at the crossings.** At the crossing ray w_ik, h_i changes sign along F_k, so δ_i(w_ik) = 0 and (L_k w_ik)_i = 0.
- **Rows i ≠ k.** A linear functional on v_k^⊥ that vanishes on ℝw_ik = v_k^⊥ ∩ e_i^⊥ is a multiple of h_i. So row i of L_k is λ_ik h_i, with λ_ik ≥ 0 by the weak signs.
- **Row k.** Since u·δ = 0 on F_k (Lemma 4.2-D(a)), row k is −Σ_{i≠k} λ_ik h_i.
- **Strict positivity.** If λ_ik = 0, then L_k = λ_jk h_j(e_j − e_k) vanishes on w_jk. That contradicts Lemma 4.2-D(d). ∎

The same holds for any interior π*, after the normalisation of §1.

---

## 6. Corner system and Theorem DC

**Corner proportionality (PROVED).** Let r_j be the corner ray in F_a ∩ F_b. Then δ is continuous at r_j, and L_a r_j, L_b r_j ≠ 0 (Lemma 4.2-D(d)). By Lemma 4.3-D(c), δ(r_j) ∝₊ L_a r_j and δ(r_j) ∝₊ L_b r_j. So L_a r_j ∥₊ L_b r_j.

**The system (CHECKED, `corner_dir.out`).** Both vectors lie in 𝟙^⊥, so parallelism at each corner is one scalar equation:
- r_1: 3λ12λ13 = 2λ12λ23 + 2λ13λ32;
- r_2: 3λ21λ23 = 2λ13λ21 + 2λ23λ31;
- r_3: 3λ31λ32 = 2λ12λ31 + 2λ21λ32.

Put a = λ23/λ13 (F_3), b = λ31/λ21 (F_1) and c = λ12/λ32 (F_2). The system becomes

  a + 1/c = 3/2,  b + 1/a = 3/2,  c + 1/b = 3/2.

So a = T³(a) with T(x) = 3/2 − 1/x, which is the elliptic Möbius map of C62/A62/REF62.
- The Gröbner basis is {x − z, y − z, 2z² − 3z + 2}, with discriminant −7. So the only solutions are 3/4 ± i√7/4, and there are **no real solutions**.
- All 26 degenerate patterns (some λ = 0, no facet map identically 0) also have no solution with the remaining λ nonzero. These are already excluded by §5, so this check is redundant.

**Theorem DC (PROVED, given REF62's repaired C62 Lemma 4.3, which REF62 rates CORRECT WITH REPAIR).**

*Statement.* No chart in the class (DC-PL) satisfies (C1), (C4), and (C3) for all π in a neighbourhood of u (or of π*), for the reversed triangle. This holds for any finite fan, any positive per-cell scalars s_σ, and any U ⊇ cl D_K∖0, in particular every one-sided U = D_{K'}. In particular no DC-PL chart carries the full four-condition certificate.

*Proof.* Sections 3–6: by them the corner system would need a real solution, and it has none. ∎

**Comparison with what was known.**
- *C62 Thm 4.1* is the special case where values are continuous. That proof needed (C2) and (C3) on the segments (e_k, u], because its Lemma 4.2 had to exclude c = 0 on ∂D_K.
- *Here* the vanishing branch is excluded by direction continuity itself (Lemma 4.2-D(d)). REF62's pinned counterexample (c ≡ 0 on ∂D_K, B_π = D_K near u) is consistent with this: it is not direction-continuous at ∂D_K.
- *REF62's remark* "if the field is a positive scalar times a continuous c̃, Cor 4.5 is contained in Thm 4.1" covers only fields that are continuous PL after a global constant rescaling. The class here is strictly larger: rank-1 facet runs (§2.4) and annulus holonomy. Neither changes the outcome.
- *Positive control.* Normalised boxes, rescaled per cell by arbitrary positive constants, are in (DC-PL) and pass the certificate (C62 §3, by direction invariance). The theorem does not touch them: box facets have no crossings, so §5 imposes nothing and the corner system is vacuous.

---

## 7. Scope and the precise gap

**Not covered by Theorem DC:**
1. **Directions jumping at the corner rays only** (A62 S3, "sliding edge").
   - What survives: §§3–5 on the open facets. Every relint facet point still has a DC neighbourhood. Only Lemma 4.2-D(d) at the corner rays themselves fails, and §4(c) gives L_k on relint F_k, extended by the cell limits.
   - **Gap:** derive L_a r_j ∥₊ L_b r_j from (C3) near u, for finitely many cells at r_j whose directions need not agree at r_j. This is A62 N5's "step lemma" for discontinuous PL fields, which REF62 marks as a sketch. If it holds, Theorem DC extends verbatim. I stop here as instructed. It needs no new regularity hypothesis, but it is unproved.
2. **Directions jumping at a crossing ray w_ik.** §5 then loses δ_i(w_ik) = 0. This is not treated here.
3. **Directions jumping across a facet** (C62 §6.1, A62-2). Outside the class.
4. **Non-PL directions** (A62 S1, S4). Outside the class. For general continuous charts, unit normalisation shows that only the direction field matters, but §4(a) uses PL.

---

## 8. Status table

| Item | Status |
|---|---|
| Unit normalisation: same Bayes sets, continuous, but not PL; does not by itself reduce to Thm 4.1 | PROVED (trivial) |
| Wall dichotomy: rank 2 ⇒ constant ratio; rank 1 ⇒ ratio may vary | PROVED |
| Holonomy around a vertex with M w ≠ 0 is 1; around the annulus it need not be | PROVED |
| Example: DC field whose cells cannot be rescaled to continuity (rank-1 facet run) | CHECKED |
| Lemma 4.2-D: u·δ = 0 on ∂D_K, strict off it; no cell map vanishes at ∂D_K; no rank-1 transversal walls | PROVED |
| Lemma 4.3-D(a): local rescaling ⇒ repaired C62 L4.3 at rank-2 junctions | PROVED (uses REF62 repair) |
| Lemma 4.3-D(b): junction lemma (rank-1 run next to rank-2 run violates (C3) near u) | PROVED; exact instance CHECKED |
| Lemma 4.3-D(c): facet directions = direction of one rank-2 linear L_k | PROVED |
| Lemma 4.4-D: crossing rows, all λ > 0 | PROVED |
| Corner proportionality from direction continuity | PROVED |
| Projective corner system: no real solution (Gröbner: 2z² − 3z + 2) | CHECKED |
| Degenerate λ patterns: no solutions | CHECKED (redundant) |
| **Theorem DC: no DC-PL chart, any fan/scalars/K′, meets (C1), (C3) near u, (C4) for the reversed triangle** | **PROVED** (refereeing needed) |
| (C2) and segment priors not needed under DC | PROVED (by the proof) |
| Extension to direction jumps at corner rays (N5 step lemma) | GAP (stated §7.1; not attempted) |
| Jumps at crossing rays, across facets, non-PL directions | not treated |

## 9. Files (`dc63py/`)

| File | Content |
|---|---|
| `corner_dir.py` / `.out` | projective corner system: equations, solve, Gröbner basis, degenerate patterns |
| `junction_witness.py` / `.out` | local DC-PL field with rank-1 facet run; wall direction checks; (C1)/(C4) grid; exact (C3) witness, also symbolic in t |
