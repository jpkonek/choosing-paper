# N5: permitted ties near the crossings of T1 — the structural side

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here, or a line-by-line transfer of a refereed proof with every changed step written out.
- **CHECKED**: verified, proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Read: BRIEF–BRIEF4, R15 + R18, N2 (§§0–3, 7), N3 (§§1, 2, 5), N4, R10a (Thm V), R10b (Prop V, Lemma FS, UVN, (1.1)), R1 (§§1–3), R14 (Thm A), CCIBU, N1 (Prop 2.3, Thm 2.4).
Scripts: `n5py/` (`thetax.py`, `tie_system.py`, `geom_check.py`, with `.out` files).

---

## 0. Outcome

**Short answer.** Permitted ties near the crossings do **not** remove the R15 Thm 6.2 mechanism. They cannot even be placed where that mechanism reads its data.

- Ties next to a facet near a crossing are impossible, in every configuration (inner only, outer only, both sides):
  - unconditionally (no regularity hypothesis) for θ < θ_x(T1);
  - under (DF)+(ND), for every θ.
- R15 Thm 1(a)–(d), Lemma 6.1 and Thm 6.2 hold verbatim in the permitted-tie class, for **every θ > 0**, in both norms, for every ε ∈ (0,1) and every interior p\*.
- The corner system, the box and the contradiction are literally the same as in the strict case.

The threshold θ_x(T1) is:
- sup norm: θ_x = 1, so every θ ∈ (0,1) is covered;
- Euclidean norm: θ_x = √((κ²+1)/(κ²+2)), with κ = (1+2ε)/(1−ε). This is 0.928 at ε = 0.3, and θ_x > √(2/3) ≈ 0.816 for every ε.

**Standing hypotheses (SH_θ), used throughout.**
- n = 3.
- Additive penalties with integrable envelopes on a decomposable domain (SC, closed in measure).
- Permitted-tie (G) of BRIEF4, any θ > 0, sup or Euclidean norm: r_i ≥ 0 on band-i problems, r_i > 0 off the band, bad strictly worse than silence, unanimous problems strict.
- (IBU): every interior Bayes model is a.e. unique and coherent, B_q ≈ D_{K_q}.
  - This is requirement (i) of the BRIEF2 single-target problem.
  - BRIEF4 records that (C) forces it for θ < 1 (sup) and θ < 1/√3 (Euclidean). For larger θ it is assumed.
- T = T1, or more generally an all-facing general-position triangle (R15 §6).
- D_T = B_{p\*} with p\* ∈ int Δ. Interiority is in fact forced for every θ by N1 Prop 2.3, which uses only strict badness.
- (LF) at D_T, with N an open cone ⊇ ∂D_T∖0, N ∩ (−cl D_T) = ∅.

(S), (LA), (C) are **not** used in the no-go statements. They are discussed only in Claim 1(c). (DF), (ND), (NA_w) are exactly R15's hypotheses, with R18's precise readings. **(X_ik)** is defined in §3.

### Claims

**1. The three "known constraints" of BRIEF4.**

**(a) N2 Prop L: CORRECT WITH REPAIR, and superseded by a stronger result.**
- What is provable is a *collar* exclusion (Prop 3.2, PROVED under (X_ik)). At a facet point w with w_i > 0 the collar is a slab, as N2 says. At a crossing (w_i = 0) it is only a wedge, {h_i > 0, −c′h_i < v_k·h < 0}.
- Outer ties beyond the collar are not excluded by any argument here. They live in a thin horn along the bad half-plane {h_i = 0, v_k·h < 0}, and they are harmless (§3.3).
- N2's second sentence ("inner ties only add rigidity") is the wrong picture. **Inner ties near a crossing are impossible whenever the outer side just across the facet is strict** (Lemma 3.1 "VT", PROVED, every θ, no (X), no regularity).
- Together (Thm 3.3, PROVED under (X), i.e. for θ < θ_x): the world-i tie set cannot accumulate at any point of ∂D_T with h_i > 0, from either side.

**(b) The coordinator's claim (Thm V survives inner-side-only ties): TRUE (PROVED), with two repairs.**
- The argument needs the outer side strict on a *full* outer quarter-ball at one i-crossing. Prop L cannot supply this: it gives only the collar, and the collar's tangent cone admits the non-anchored contact ν(v_k + c′e_i) (NUMERICS `geom_check.py` (d)).
- Its hypothesis forces the inner side to be strict as well (Lemma 3.1). So "inner-side-only ties" cannot actually occur there.
- Correct general form (Prop 3.5, PROVED): every coherent world-i-optimal model is anchored (e_i ∈ V_i). This covers C_{e_i} and every directional vertex limit of the K_q. It holds under (X_ik) or under (DF)+(ND), via an inner-disc argument.
- What fails is R10b Cor V2: Hausdorff continuity of K_q at the vertices. Vertex limits are directional. R15 never uses it.

**(c) N3's blow-up closed choice under permitted ties: CHECKED, works verbatim** (Prop 3.7).
- Only R14 Thm A (IBU only), CCIBU's interior and edge lsc arguments, and strict convexity of G_r on the face F_i are used. None of them uses strictness or forced ties.
- N1 Thm 3.1 (Chebyshev selection, any guidance order) is an independent route.

**2. R15's first-order calculus with ties (§4).**

**(a) Thm 1(a), 1(b), 1(d): PROVED unchanged.** They use only concavity in h, (DF), Lemma C, (1.1) and weak signs.

**(b) Thm 1(c): PROVED for every θ, with λ_{ik} > 0 still.**
- The vanishing of the crossing functional at w_{ik} uses only two-sided *weak* signs.
- Positivity no longer comes from UVN(a). It comes from a sign–rank argument (Lemma 4.2):
  - weak signs give λ ≥ 0;
  - if λ_{ik} = 0, then on F_k the bad coordinate gives c_k = −μ_{jk}h_j/p\*_k, which has the wrong sign where h_j < 0;
  - so Γ_k = 0, contradicting (ND).
- Lemma 3.2 (nonsingularity) holds.

**(c) What happens to the crossing rows if c_i = 0 inside and c_i > 0 outside?**
- The configuration does not exist (Lemma 3.1).
- Formally, under (DF), it would force λ_{ik} = 0 and hence Γ_k = 0 (Prop 4.3). So ties touching a facet would force (DF) or (ND) to fail: a kink (E1) or a flat facet (E3).
- The kinked version has **no** solution: Lemma 3.1 is pointwise and needs no derivative (Prop 4.4).
- So permitted ties never force a kink in any consistent system.

**(d) Lemma 6.1 (vertex-limit box): PROVED unchanged.**
- Strict signs of Λ come from the line(p\*, e_b) route for both signs.
- Lemma FS comes from anchoring (Prop 3.5).
- **The box does not loosen.**

**(e) N3 Cor ST2** becomes moot: one-sided ties are excluded (Lemma 3.1, Prop 3.2), and two-sided ties are excluded (N2 Thm B tie version, or N3 Thm ST + N4). It stays relevant only in the open regime of Claim 3(b).

**3. Answer to the question.**

**(a) Thm 5.1 (PROVED).** Under (SH_θ), (DF), (ND), (NA_w) are inconsistent:
- for every θ > 0 and both norms;
- for T1 at every ε ∈ (0,1) and every interior ε-contamination triangle;
- for every all-facing general-position triangle;
- at every interior p\*.

The tie-version first-order system for T1 *is* the strict system:
- the same two solutions x± with x + 1/x = κ + 1;
- the same box 1/κ ≤ x² ≤ κ;
- the same violation, Λ_max = x₊²/κ = 3.80 at ε = 0.3 (NUMERICS `tie_system.py`, reproducing R15).

Permitted tying near crossings leaves the mechanism **intact** and adds no new contradiction for T1 itself. The only "new contradiction" is local: a system that actually places ties next to a crossing is inconsistent outright.

**(b) Not settled.**
- *Euclidean θ ≥ θ_x(T1) without (DF).* There, (X) can fail, and outer-and-inner ties along a facet are not excluded unconditionally. They would force a kink, which is R15's escape (E1) in a new guise. Status: CONJECTURE/open. This regime needs θ > 0.816.
- *The R15 escapes.* (E1)–(E4) (failure of (DF), (ND) or (NA_w)) remain exactly as open as in the strict case. Ties do not touch them, by Thm 3.3 and Prop 4.3.

---

## 1. Notation

- Charts: R1 Prop 2.1. For an orientation h with + and 0 in its advice range, write c(h) = ℓ(0) − ℓ(accept h), and c′, d when acceptance of −h is in the advice range. R(h) ⊆ {c(h)·q > 0} always, and R(h) = {c·q > 0} for advice range {+,0}.
- **Weak signs (Lemma 2.1 below).** For accepting h:
  - c_l(h) ≥ 0 if h_l > 0 (= 0 exactly on the permitted tie set τ_l, which lies in the band);
  - c_l(h) > 0 off the band;
  - c_l(h) < 0 if h_l < 0.
- The tie set τ_i is the set of h with h_i > 0, mixed, + and 0 in the advice range, and c_i(h) = 0. It is defined a.e.
- T1: v_k = a𝟙 + εe_k, a = (1−ε)/3, κ = (1+2ε)/(1−ε).
  - F_k = {v_k·h = 0, h_k < h_l (l ≠ k)}. Here h_k < 0, and C_k = {i ≠ k}.
  - In coordinates (i, j, k), the i-crossing of F_k is w_{ik} = (0, κ, −1).
  - The corner ray r_{kj} has i as its only positive coordinate.
- Inner side: D = D_T. Outer side: the complement of cl D.
- K_q are the interior Bayes credal sets, and P(q,h) = min_{K_q} m·h is jointly continuous on int Δ × ℝ³ (R1 Prop 3.1, IBU only).
- **Good h:** R10b (1.1) holds, i.e. P(·,h) ≥ 0 on cl R(h) ∩ int Δ and ≤ 0 off it. Good h are co-null.
- **Cluster set** Cl(h): as in R15 §1.

## 2. Tools valid under permitted ties

**Lemma 2.1 (weak signs). PROVED.** Under permitted-tie (G), for a.e. g and the kinds of advice in its advice range:
- ℓ_i is weakly increasing in the four-rank order;
- ℓ_i is strictly increasing across the classes bad < silence < contradictory and between good and silence off the band (and wherever the ranking does not tie).

*Proof.* R1 Lemma 1.1 verbatim for the strict pairs. The weak part is the definition. ∎

Consequences:
- R1 Lemma 3.5 (half-plane charts near p\* for pairs in N) and Lemma C of R15 hold. Lemma C's non-constancy needs only weak mixed signs: ĉ_l ≥ 0 on P(h), ĉ_l ≤ 0 on N(h), so ĉ ∝ 𝟙 forces ĉ = 0.
- R10b (1.1) and N2 Lemma 1 (transport along (δ_i, p\*] for tied h) hold; they use IBU only.
- N1 Prop 2.3 holds.

R1 Lemma 3.5 needs only that K_q ∩ K′ ≠ ∅ near p\* (Hausdorff continuity plus K′ ⊆ ri K) and the three-sector geometry. No vertex uniqueness is needed: R1 Prop 2.4(ii) is not needed for pairs in N.

**Lemma 2.2 (vertex-uniform acceptance; the UVN step). PROVED.** Let B₀ ⊆ N ∩ {h_i > 0} be a ball such that, for a.e. g ∈ B₀, accepting g is in the advice range and c_i(g) > 0. Then:
- there is a relative neighbourhood V of e_i in Δ with x ∈ D_{K_q} for every centre-ball point x of B₀ (in particular its centre) and every q ∈ V ∩ int Δ;
- consequently, every h > x (strictly, coordinatewise) satisfies P(q,h) ≥ P(q,x) + min_l (h − x)_l > 0 for q ∈ V ∩ int Δ.

*Proof.* R10b UVN(a), with the ball given directly.
- For a.e. g ∈ B₀, accepting g is the unique world-i optimum: it beats silence since c_i > 0, beats −g since −g is bad at i, and beats ×.
- So it is the q-minimiser for |q − e_i| < r(g). Dominated convergence gives μ(B₀∖D_{K_q}) → 0.
- An open convex cone that misses the centre misses a half-ball. ∎

Define **A_i° := {h : h > x for some centre x of a ball as in Lemma 2.2}**. It is open, upward closed, and conic.

## 3. Item 1: where ties can go

### 3.1 Inner ties above a strict point are impossible

**Lemma 3.1 (VT). PROVED (every θ, both norms, no regularity, no (X)).** Under (SH_θ), for a.e. h ∈ A_i° that is mixed and has + and 0 in its advice range, c_i(h) > 0. That is, τ_i ∩ A_i° is null.

*Proof.*
1. Fix h₀ ∈ A_i° with h₀ > x, where x is a centre as in Lemma 2.2. Take a ball B₁ ∋ h₀ inside {h > x}.
2. By Lemma 2.2, B₁ ⊆ D_{K_q} for every q ∈ V ∩ int Δ.
3. Since B_q ≈ D_{K_q}, Fubini on B₁ × (V ∩ int Δ) gives: for a.e. h ∈ B₁, a.e. q ∈ V ∩ int Δ lies in R(h) ⊆ {c(h)·q > 0}.
4. Suppose h ∈ τ_i is mixed. Then c_i(h) = 0, and c_l(h) < 0 for some l with h_l < 0 (bad is strict).
5. For q = (1−s−t)e_i + s e_l + t e_m with 0 < t < s|c_l|/max(c_m, 1) and s small, c·q = s c_l + t c_m < 0. These q form a set of positive measure in V ∩ int Δ. Contradiction. ∎

(Equivalently: a tied chart is contained in a half-plane bounded by a cevian through e_i, which never contains a vertex neighbourhood.)

**Application at a crossing.** Let w = w_{ik}, and suppose the outer side is strict, i.e. c_i > 0 a.e. on O⁻ = B(w,δ) ∩ {h_i > 0} ∖ cl D.

Every inner h ∈ B(w, δ/3) ∩ D ∩ {h_i > 0} lies in A_i°:
- Take x⁻ = h − d with d = (τh_i, s, s) in (i, j, k) coordinates, τ small.
- Choose s so that v_k·x⁻ < 0.
- Then x⁻ ∈ O⁻, x⁻_i > 0, and |d| = O(v_k·h + τh_i) is small.

So the inner side near w is strict a.e. (NUMERICS `geom_check.py` (b): 6137 random inner points, 0 failures.)

**The brief's configuration** ("c_i = 0 on the inner side, c_i > 0 on the outer side, near a crossing") **has no realisation under (SH_θ).**

### 3.2 The outer side: a collar, not a slab

**Hypothesis (X_ik).** There is a non-null set of mixed x, with acceptance of x in the advice range, such that c_i(x) > 0 and v_k·x < 0.

For T1 this holds automatically when θ < θ_x := sup_{h∈cl F_k∖0} h_i/‖h‖. Take x = h̄ − s𝟙 ∈ N near a facet point h̄ with h_i > θ‖h‖. Such x is off-band, hence strict.

Values of θ_x:
- sup norm: θ_x = 1, attained at r_{kj};
- Euclidean norm: θ_x = √((κ²+1)/(κ²+2)), attained at (κ + 1/κ, −1/κ, −1) (this is N4's θ₀). Values: 0.837, 0.857, 0.928, 0.984, 0.9994 at ε = .05, .1, .3, .6, .9 (`thetax.py`).

**Proposition 3.2 (outer collar; repaired N2 Prop L). PROVED.** Assume (SH_θ) and (X_ik). Let w ∈ relint F_k with w_i ≥ 0, and U = B(w,δ) ⊆ N meeting no other facet. Then there are c′, ρ > 0 such that c_i > 0 a.e. on
- W = {y ∈ B(w,ρ) : y_i > 0, −c′y_i < v_k·y < 0} when w_i = 0;
- the slab {y ∈ B(w,ρ) : −c′ < v_k·y < 0} when w_i > 0.

*Proof.*
1. N2 Lemma 2 (vertex pull; d_i = c_i − c′_i > 0) gives a non-null E′ and r₀.
2. Fix q ∈ (δ_i, p\*] with |q − δ_i| < r₀. Pick x₀ ∈ E′ ∩ D_{K_q}.
3. *Inner points are accepted at q.* For a.e. h ∈ U⁺_i := U ∩ D ∩ {h_i > 0}:
   - if h ∈ τ_i, N2 Lemma 1(a) puts q ∈ R(h);
   - otherwise c_i(h) > 0, so δ_i ∈ R(h) (vertex property, d_i > 0) and p\* ∈ R(h), and convexity puts q ∈ R(h).
   So D_{K_q} ⊇ U⁺_i (open convex), hence D_{K_q} ⊇ conv(U⁺_i ∪ {x₀}).
4. *The hull contains W.* For y ∈ W with v_k·y = −σ, put λ = 2σ/|v_k·x₀| and z = (y − λx₀)/(1−λ). Then:
   - v_k·z = σ/(1−λ) > 0;
   - with c′ := |v_k·x₀|/(4x₀_i), z_i ≥ (y_i/2)/(1−λ) > 0;
   - |z − w| ≤ (1 + Cc′)ρ < δ.
   So z ∈ U⁺_i and y ∈ (z, x₀). The slab case is the same with y_i ≈ w_i > 0.
5. *Tied points of W are rejected at q.* For a.e. h ∈ τ_i ∩ W: h ∉ cl D and −h ∉ cl D, so there is no tie at p\* and N2 Lemma 1(b) gives h ∉ B_q.
6. Since W ⊆ D_{K_q} ≈ B_q, the set τ_i ∩ W is null. ∎

(NUMERICS `geom_check.py` (a): 0 failures of the hull containment.)

The collar's thickness c′y_i degenerates at the crossing. Outer points with v_k·y < −c′y_i (a thin horn along {h_i = 0, v_k·h < 0}) are not excluded by Prop 3.2, nor by Lemma 3.1, since they dominate no strict point near w.

### 3.3 No ties at the boundary

**Theorem 3.3 (NT). PROVED** under (SH_θ) and (X_ik) for every crossing pair (i, k); for T1 this means θ < θ_x. For every world i, τ_i does not accumulate (essentially) at any h ∈ ∂D_T∖0 with h_i > 0, from either side. Precisely: every such h has a neighbourhood B with c_i > 0 a.e. on B ∩ {h_i > 0}.

At crossing rays (h_i = 0), τ_i can accumulate only through the outer horn of §3.2.

*Proof.* Three kinds of boundary points.
- **Facet points of F_k with h_i > 0** (i ∈ C_k): Prop 3.2 gives a strict slab; Lemma 3.1 (inner h dominates slab points h − σ𝟙 − small) gives the inner side. Outer points of B within the slab are covered by Prop 3.2.
- **Corner rays r with r_i > 0** (for T1, r = r_{kj} with i ∉ {k, j}):
  - inner points near r have i as their only positive coordinate, so c_i > 0 by positivity (a tied h would have c ≤ 0 with a negative entry, hence be rejected at p\*);
  - the outer side is covered by the hull argument of Prop 3.2 with x₀ = r − s𝟙, since v_k·x₀ = v_j·x₀ = −s.
- **Facets where h_i < 0** contain no points with h_i > 0. ∎

**Corollary 3.4 (inner ties are deep). PROVED** under the hypotheses of Thm 3.3. For a.e. mixed h ∈ D with + and 0 in its advice range and h_i > min_k v_k·h, c_i(h) > 0.

*Proof.*
- b = h − t𝟙 with t = min_k v_k·h lies in ∂D, and b_i > 0.
- By Thm 3.3, x = b − σ𝟙 is a strict collar centre.
- h − x = (t + σ)𝟙 ≫ 0, so h ∈ A_i°. Apply Lemma 3.1. ∎

So inner ties survive only where the world-i stake is below the acceptance margin, away from ∂D_T. Example: h = (0.1, 2, −0.3) for T1 at ε = 0.3.

### 3.4 Vertex anchoring

Call a coherent model D_W **world-i-optimal on N** if:
- (α) it contains a.e. h ∈ N with acceptance of h in the advice range, h_i > 0 and c_i(h) > 0;
- (β) it contains no non-null set of h ∈ N with h_i < 0.

Two kinds of model qualify:
- C_{e_i} from (S): competitive on {i} means pointwise world-i optimal, as in DCE prop:ideal, with good and silence both world-i optimal on τ_i;
- every directional limit W = lim K_{q_n} with q_n → e_i interior. For these, (α) holds even in the stronger form "D_W ⊇ A_i°" (Lemma 2.2: P_W(h) ≥ min(h − x) > 0). (β) holds because for a.e. such h silence beats acceptance at e_i with a gap, so μ(D_{K_{q_n}} ∩ ·) → 0. M_L is closed in measure, so D_W ∈ M_L.

**Proposition 3.5 (anchoring). PROVED.** Assume (SH_θ) and either (X_ik) for some k with i ∈ C_k, or (DF)+(ND) (with Thm 4.1 below). Then e_i ∈ W for every world-i-optimal coherent D_W.

*Proof.*
1. Let w = w_{ik} and h₀ = w + t(e_j + e_k) in (i, j, k) coordinates, with t small. Then h₀ ∈ D ∩ N and (h₀)_i = 0.
2. *Every h ∈ B(h₀, ρ) with h_i > 0 lies in A_i°* (ρ ≪ t). Take y = w + αf − β v_k/|v_k|², with f ∈ v_k^⊥, such that y_i = h_i/2 and −c′y_i < v_k·y < 0. Then h − y ≫ 0, and y is a strict centre:
   - under (X): by Prop 3.2 (`geom_check.py` (c): 10010 points, 0 failures);
   - under (DF)+(ND): take y ∈ relint F_k with y_i = h_i/2. Its unique cluster has ĉ_i ∝ λ_{ik} y_i > 0 (Thm 4.1(c)), so good points in a small ball around y have c_i > 0.
3. By Lemma 3.1 (for C_{e_i}) or Lemma 2.2 (for limits), D_W ⊇ B(h₀,ρ) ∩ {h_i > 0}. By (β), D_W ∩ B(h₀,ρ) ∩ {h_i < 0} = ∅.
4. So D_W ∩ B = B ∩ {h_i > 0}. Take m ∈ W with m·h₀ = 0. Then m·d ≥ 0 for every d with d_i > 0, so m ∝ e_i, i.e. m = e_i. ∎

Consequences:
- R10a Cor V1 holds: gambles accepted by every evaluable model are (a.e.) nonnegative (a set accepted by every evaluable model is accepted by every model in M_L, including an anchored D_W).
- Hence R10b Lemma FS holds verbatim: its other ingredient is strict badness.

**Verdict on the coordinator's sketch.**
- Under its hypothesis (outer side strict on the full quarter-ball O⁻), the tangent cone {d_i ≥ 0, v_k·d ≤ 0} gives a dual cone{e_i, −v_k} ∩ Δ = {e_i}. CORRECT.
- The cited source "(by Prop L)" is wrong. Prop L gives only W, whose tangent cone {d_i ≥ 0, v_k·d + c′d_i ≥ 0} has dual cone{e_i, v_k + c′e_i}. That dual contains the probability m = ν(v_k + c′e_i) with m·w = 0 (`geom_check.py` (d): m = (0.238, 0.232, 0.530)).
- The repair is step 2 above (an inner disc instead of the outer wedge).

### 3.5 Closed choice

**Proposition 3.7. CHECKED.** N3 Thm CC_θ holds under permitted ties.

Re-reading its proof:
- (C) and coherence of efficient profiles come from R14 Thm A, which uses IBU and admissible lexicographic sequences only (N1 Thm 2.4(N3_θ) uses (e_i, (0, α, β))).
- The vertex face F_i = argmin_R y_i is compact and convex, of any dimension ≤ 2.
- x̂(e_i, r) = argmin_{F_i} G_r is a unique profile, because G_r is strictly convex in (y_j, y_k) and y_i is constant on F_i.
- It is efficient: an improvement stays in F_i and lowers G_r.
- The endpoint rule is lexicographic.
- The lsc arguments at arc points use only G_{r_m}(x_m) ≤ G_{r_m}(y\*) and closedness.
- CCIBU's interior and edge lsc lemmas use strictness only at vertices; R14 says so, and its edge-uniqueness step is replaced by R14 Thm A.
- σ = ψ∘ρ is continuous with supp σ(p) ⊆ supp p.

Whether the ties are forced or permitted only changes the shape of F_i, and the proof is shape-free. N1 Thm 3.1 (Chebyshev) is an independent route. Neither is needed for the no-go.

## 4. Item 2: the first-order calculus with ties

**Theorem 4.1 (R15 Thm 1 under permitted ties). PROVED**, assuming (SH_θ), (DF), (ND), any θ, either norm.
- **(a) and (b)** are R15's proofs verbatim. (a) uses concavity in h and two-sided (DF). (b) uses Lemma C, which holds by §2.
- **(c)** For i ∈ C_k, Γ_k h·(e_i − p\*) = λ_{ik}h_i with **λ_{ik} > 0**.
  - Vanishing at w_{ik} (when Γ_k w ≠ 0): good sequences from {h_i > 0} give ĉ_i ≥ 0 (weak, ties allowed), and sequences from {h_i < 0} give ĉ_i ≤ 0. The cluster is unique, so ĉ·e_i = 0.
  - Positivity comes from Lemma 4.2, not from UVN(a).
- **(d)** Corner proportionality is R15's proof verbatim. It uses concavity in h, Lemma C and (DF) on the adjacent facets, and no signs.

**Lemma 4.2 (sign–rank positivity). PROVED.** Let F_k have C_k = {i, j}, with the third coordinate k strictly negative on relint F_k (all-facing; T1). Under (DF) and (ND), λ_{ik}, λ_{jk} > 0, and Γ_k is nonsingular.

*Proof.*
1. c_k(h)·p\* = 0 gives p\*_k c_k(h)_k = −(μ_{ik}h_i + μ_{jk}h_j), with μ = p\*λ.
2. *Weak signs give μ ≥ 0.* At h ∈ relint F_k with h_i > 0 and Γ_k h ≠ 0, ĉ_k(h) ∝₊ c_k(h), so λ_{ik}h_i ≥ 0.
3. *Suppose μ_{ik} = 0.* Then c_k(h)_k = −μ_{jk}h_j/p\*_k. Since j ∈ C_k, relint F_k contains points with h_j < 0, and there Γ_k h ≠ 0 when μ_{jk} > 0. But h_k < 0 forces ĉ_k ≤ 0 there (bad is strict). So μ_{jk} = 0, hence c_k ≡ 0 and Γ_k = 0, contradicting (ND).
4. Nonsingularity is then R15 Lemma 3.2, whose kernel case uses exactly this positivity. ∎

(`tie_system.py` (1): every zero pattern on a facet violates the weak signs unless Γ = 0.)

**Proposition 4.3 (ties cannot touch facets; they would force a kink). PROVED, every θ.** Under (SH_θ), (DF), (ND), no open G ⊆ relint F_k ∩ {h_i > 0} can have every point be a limit of good points of τ_i.

*Proof.*
- Such limits give clusters with ĉ_i = 0. The cluster is unique, so c_k(h)_i = λ_{ik}h_i = 0 on G, i.e. λ_{ik} = 0, contradicting Lemma 4.2.
- Read the other way: ties accumulating on a facet piece (inner, outer, or both) force failure of (DF) (a kink, (E1)) or of (ND) (a first-order flat facet, (E3)). ∎

**Proposition 4.4 (the kinked version has no solution). PROVED where its hypothesis is that of the brief.**
- Suppose (DF) is dropped and the brief's configuration holds: inner side tied, outer side strict near w_{ik}. Lemma 3.1 already excludes it, and Lemma 3.1 is pointwise: it uses no derivative and no cluster.
- So there is no kinked solution with this tie pattern, whatever the one-sided derivatives are.
- Cluster-level arguments alone would not suffice here. An inner tied cluster can degenerate to ĉ = e_j, whose half-plane contains int Δ. Lemma 3.1 works with the strict c_l(h) < 0 of each individual tied h.
- If instead the outer side near w is tied as well, then:
  - two-sided ties are excluded by N2 Thm B (tie version, refereed in N4) under (X_ik);
  - the outer-only case is excluded on the collar by Prop 3.2.

**Lemma 4.5 (R15 Lemma 6.1 under ties). PROVED**, assuming (SH_θ), (DF), (ND), (NA_w), any θ.
- *Strict signs of Λ_{ab}.* Γ_k w ≠ 0 by Lemma 4.2. The cluster at the b-crossing w has ĉ·e_b = 0 (two-sided weak signs) and ĉ·p\* = 0, so its zero line is line(p\*, e_b), which misses e_a. The weak sign ĉ_a ≥ 0 (w_a > 0), or ĉ_a ≤ 0 (w′_a < 0), is therefore strict. This is R18's hypothesis-free route, now used for **both** signs, with no strictness at world a.
- *Steps 1–4* use the first-order chart c_{k′}(A)·q₀ = s c_a + (1−s)λ_{bk′}A_b with λ_{bk′} > 0 (Lemma 4.2), together with (b) and (NA_w). They are unchanged.
- *Step 5* is Lemma FS, available by Prop 3.5.
- **The box Λ_{ab} ≤ 1 is identical: it does not loosen.**

**Remark (N3 Cor ST2).** Its tie hypothesis (ties on both sides of a facet piece next to a y-crossing) is excluded:
- under (X), by N2 Thm B tie version, or by N3 Thm ST strengthened as in N4 (Π_U contains the whole cevian through e_y and p\*; strict exterior w₊ then contradicts it near e_y);
- under (DF)+(ND), by Prop 4.3.

One-sided versions are excluded by Lemma 3.1 and Prop 3.2. So Cor ST2 plays no role at θ < θ_x. It survives only as a constraint in the open regime of §6.

**Remark (reversed orientations).** Ties c′_i = 0 for accept(−h) on pairs with h_i < 0 enter only charts for advice range {+,0,−}. Those are absent near p\* (R1 Lemma 3.5) and at the witnesses (NA_w). They never enter Thm 4.1, Lemma 4.5 or Lemma FS: there −h is at least as good as silence at the worlds of S, which is strictly better than +.

## 5. Item 3: the conclusion

**Theorem 5.1 (R15 Thm 6.2 in the permitted-tie class). PROVED** (line-by-line transfer; changed steps are Thm 4.1(c), Lemma 4.2, Lemma 4.5 and Prop 3.5).

Let T be an all-facing general-position triangle, p\* ∈ int Δ, θ > 0 arbitrary, with either norm. Then (SH_θ), (DF), (ND), (NA_w) are inconsistent.

In particular this holds for T1 at every ε ∈ (0,1), and for every ε-contamination of an interior baseline.

*Proof.* R15 Thm 6.2, steps 1–6. The only inputs are:
- facet linearity, unique clusters, crossing rows with μ > 0, nonsingular Γ_k, corner proportionality (Thm 4.1, Lemma 4.2);
- Lemma 4.1 of R15 (pure algebra);
- the box (Lemma 4.5).

None of these uses strict good-vs-silence. ∎

**For T1 explicitly.** The weak-sign first-order system has exactly R15's solution set:
- a = b = c ∈ {x₊, x₋}, with x + 1/x = κ + 1;
- the non-crossing sign condition becomes 1/(κ+1) ≤ a ≤ κ+1, which x± satisfy strictly;
- zero patterns are excluded by Lemma 4.2.

The box 1/κ ≤ x² ≤ κ is violated. At ε = 0.3: Λ_max = 3.7978, and the six Λ lie in [0.0504, 3.7978] (`tie_system.py`, matching R15's 3.80).

**Answer for every θ > 0 and both norms.**

| Question | sup norm | Euclidean norm |
|---|---|---|
| Thm 6.2 mechanism, under (DF), (ND), (NA_w) | intact, every θ (PROVED) | intact, every θ (PROVED) |
| Ties next to crossings, unconditionally | impossible for θ < 1 (PROVED, Thm 3.3); θ ≥ 1: see §6 | impossible for θ < √((κ²+1)/(κ²+2)) (PROVED); above: open |
| Inner-only ties with strict outer side | impossible, every θ (PROVED, Lemma 3.1) | same |
| Box | unchanged | unchanged |
| Forced kink? | no: ties cannot sit on facets (Thm 3.3 / Prop 4.3) | same |

**Net.** Ties are a usable freedom only:
- away from ∂D_T: inner points with h_i ≤ min_k v_k·h (Cor 3.4), and the outer horns along the bad half-planes at crossing rays;
- on reversed orientations.

Neither feeds R15's first-order data, which live at facet points with h_i > 0, at the b-crossings' clusters, and at the box witnesses. So the T1 status in the permitted-tie class equals its strict status as far as R15's mechanism is concerned: conditionally excluded, with the same escapes (E1)–(E4).

## 6. The main open gap

1. **(E1)–(E4) themselves**, unchanged from R15 §9 and R18:
   - deriving (DF) (oddness in δ), (ND) and (NA_w) from the axioms;
   - otherwise, handling kinked or flat facets, sliding edges, and adjacency at box witnesses.

   This is the decisive open problem for T1, with or without ties. Nothing here suggests that ties make any of these escapes easier: they cannot reach the facets. It is not proved, though, that ties far from ∂D_T (Cor 3.4 region, outer horns) cannot help *produce* a (DF)-failing realisation. CONJECTURE: they cannot.
2. **Euclidean θ ≥ θ_x(T1)** (> 0.816 for every ε), and **sup θ ≥ 1**, without (DF).
   - Here (X_ik) can fail: no strict x with v_k·x < 0 whose acceptance is in the advice range. Then outer-and-inner ties along F_k are excluded only via (DF)+(ND) (Prop 4.3).
   - A realisation in this regime would have to be kinked or flat on F_k, and anchoring at e_i would need another source.
   - N3 Thm ST then still gives the cevian rigidity: Π_U contains the whole chord through e_y and p\*.
   - Status: open. This is far from "negligible stakes".

## 7. Scripts (`n5py/`, evidence only)

| file | content |
|---|---|
| `thetax.py` | θ_x(T1) in both norms against the closed forms (5 values of ε) |
| `tie_system.py` (`.out`) | weak-sign first-order system for T1: zero patterns infeasible unless Γ = 0; x± reproduced; Λ ∈ [0.0504, 3.7978]; box violated |
| `geom_check.py` (`.out`) | T1, ε = .3: (a) collar ⊆ hull (0 failures); (b) inner points dominate collar points (0/6137); (c) disc points dominate collar points (0/10010); (d) non-anchored contact ν(v_k + c′e_i) with m·w = 0 consistent with collar-only strictness |
