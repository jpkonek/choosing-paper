# Referee report on Q1_notes.md Part I (Q1.20–Q1.26) and Q3_notes.md Part I (Q3.20–Q3.27), round 21

16 Oct 2026. This is an adversarial reading. Every PROVED item was re-derived line by line, against:
- R21_reduction.md;
- M2_notes + M23_referee, L4_notes + L4_referee, N1/N2 Part I + N12_referee, H1_notes + H12_referee, P1 Part I +
  P1_referee, F1_notes (F1.2), B1, K3 (K3.1);
- write-up §§2–3 (C_L = coherent undominated models; relevant comparisons; regular models), §7, §8.5–8.6.

Archived Parts II were not refereed.

**Numerics.** All reruns used `python3 -I -B`, and every one was byte-identical to its `.out`:
- `q1py/q1_fiber_return.py`, `q1py/q1_loops.py`, `q1py/q1_tc_linear.py`;
- `q3py/r21_kkm_check.py` (23 s).

My script is `q13ref_py/ref_loops_scaling.py` (+ `.out`). It reruns the rook loops of `q1_loops.py` while shrinking
the cell thickness:
- product-form ω: 1.0563 → 1.0277 → 1.0139 → 1.0071, i.e. → 1 linearly in the thickness;
- non-product ω (β = 0.5): one orientation 0.909 → 0.885 → 0.874 → 0.868, a limit near 0.863.

So the loop violation is not a discretisation artefact. No verdict below rests on numerics.

---

## 0. Verdicts

Nothing is WRONG. Both notes are substantive and, in their PROVED cores, correct.

### Q1 Part I

| Item | Verdict |
|---|---|
| **Q1.20** cut moves along the own edge chain, from competitiveness + (RL-2) | **CORRECT** |
| Q1.21 composition, ρ*-bookkeeping | **CORRECT** |
| **Q1.22** pinning, continuous w_j | **CORRECT**: (a) Π = 1 on alternating rook cycles, ω = ψ(x₃)/φ(x₂); (b) monotonicity; (c) uniqueness of σ-finite endorsers |
| Q1.22, measurable w_j ("CHECKED") | **GAP (fixable)**. Not written out, and the statement itself must change: fibres are null, φ and ψ may jump. Fix in §1.4. Until it is written, label it *sketch*, not CHECKED |
| **Q1.23** ρ*μ endorses every D-localized comparison; world 1 is (Loc) | **CORRECT**, with one **GAP (fixable)**: the order of quantifiers (η, h, P) is circular as written (§1.5) |
| (TC) | A clean, checkable hypothesis on the cover's **own** edge selection. Correctly kept as a hypothesis (§1.3) |
| **Q1.24** no cover (via H1.2) | **CORRECT**. All H1.2 hypotheses are met (checklist in §1.6). **Scope GAP (wording)**: §0 and Q1.25(d) say it "closes (V) origin II-a / origin I under (Nest_e) + (TC)". At PROVED level this needs *continuous* partner densities, and R21's partner densities are only measurable |
| Q1.25 (a), (b), (d) | **CORRECT** |
| Q1.25 (c) | CORRECT as a reading |
| Q1.25 (d), last bullet (p.f.a. partners, CHECKED) | Confirmed as CHECKED |
| **Q1.26** linear host satisfies (TC); ρ* = h\|g₁\| | **CORRECT**. The CHECKED item (π ~ Lebesgue) is a two-line proof (§1.7) and can be upgraded |

### Q3 Part I

| Item | Verdict |
|---|---|
| Q3.20 maximal (CA) density | **CORRECT**. Wording: ρ^ca_j is not unique; only its support is (§2.6) |
| **Q3.21** lsc of ψ_j(C_q) at (CA) worlds via the union test | **CORRECT**. This is the key new input, and it is right |
| Q3.22 M2.2–M2.3 with (CA) partners | **CORRECT** |
| **Q3.23** forced KKM with ψ-sublevel KKM sets; Gap ≡ 0; any n | **CORRECT** |
| **Q3.24** M2.6′ next to (CA⁺) partners | **CORRECT** at the status of M2.6′: PROVED except case (II), which is CHECKED |
| **Q3.25** universal fixed point, no hypothesis at any world | **CORRECT**. **GAP (wording)**: c♮ and Λ♮ depend on the choice of the (CA) densities, not only on their supports. Every statement holds for every choice; say so (§2.6) |
| **Q3.26** b♮ trichotomy | **CORRECT as a trichotomy** (except case (II)). **GAP (scope/wording)**: "(S) collapses / is no longer a separate leaf" overclaims (§2.7) |
| Q3.27 Pareto off the carriers for the universal tuple | **CORRECT** |
| §4 lead shape | §4.2 CORRECT. §4.3 is labelled CONJECTURE. One wording slip (§2.8) |
| §5, Q_S♮ | Well posed. It is the right replacement for Q_S |

---

## 1. Q1 Part I

### 1.1 Lemma Q1.20: CORRECT

- **The model.** Take C := C^j_t with c^j_t = {x_j < b} mod null. Such t exists for every b ∈ (0,1): chain-indexed
  edge models after the N12_referee §1.4 fix, with N0(iv) giving competitiveness at every interior b.
- **Error sets.** S ⊆ E₁C and T ∩ E₁C = ∅ hold mod null, so X := C △ (S ∪ T) has E₁X = (E₁C ∖ S) ∪ T (N1.0(c)).
  - On R_1j each advice errs at exactly one of 1, j.
  - Off R_1j nothing changes; C = P₁ there by N1.0(b).
- **The partner rejects.** ψ_j(X) − ψ_j(C) = w_j(S) − w_j(T) < 0. C ∈ C_L and X is regular, so this is a relevant
  comparison, and (RL-2) contraposed gives C ⋠_j X.
- **World 1 accepts.** Competitiveness on {1, j} gives C ⪯₁ X, with vector 1_T − 1_S.
- (RL-2) is exactly M2 §1's clause, "for every C ∈ C_L and regular X".
- The remark "in either direction along the level set" is right: the own coordinate must cross b upwards, the other
  coordinate is free.

### 1.2 Lemma Q1.21: CORRECT

- (IB) (Lemma vectorform) transports each accepted vector to the pair X_{i−1}, X_i. Transitivity does the rest.
- The bookkeeping inequality is immediate.

### 1.3 (TC)

(TC) is a hypothesis on the cover's own edge chains at e₁ and on the partners' densities, and it is kept as one.
The note never claims (TC) for a general cover; the "general hosts" remark is correctly labelled "no claim".

Two points a reader should see stated.
- **(TC1)'s openness of χ is the substantive clause.** Rook-connectivity (TC2) is automatic for open connected G:
  axis-parallel polygonal paths give rook sequences. (TC3) is a non-degeneracy condition at the sign classes Q₂, Q₃.
- **Continuity of x_j** depends only on the chain geometry and on w_jμ having no mass on level sets. It does not
  need continuity of w_j. So (TC1) is meaningful in the measurable case too.

### 1.4 Proposition Q1.22

**Continuous case: CORRECT.**

*The rook-cycle claim.* I re-derived the masses step by step.
- Start with M := w₂(S⁰), so w₃(S⁰) ≈ M/ω₀.
- After the first 13-step: w₃(T¹) = (1+η)M/ω₀, so w₂(T¹) ≈ (1+η)Mω₁/ω₀.
- After the following 12-step: w₂(T²) = (1+η)²Mω₁/ω₀, and so on.
- The closing 12-step deposits w₂(T^N) ≈ (1+η)^N·Π·M, with Π = ∏_{odd} ω(g^i) / ∏_{even, 0<i≤N} ω(g^i)
  (g^N = g⁰). This matches the note.

The geometric side checks too.
- The corner sets {target side of the incoming cut} ∩ {source side of the outgoing cut} ∩ V^i are non-null: χ(V^i) is
  open (TC1) and π ~ Leb.
- T^N ⊆ S⁰ is legal: S⁰ was vacated at step 1 and the current error set is T^{N−1}.
- The degenerate cycle (two preimages of one z) gives fibre-constancy.

*Product form.*
- Ω is continuous: Ω^{−1}(open) = χ(ω^{−1}(open)) with χ open.
- Cycles of the bipartite graph Γ are exactly alternating rook cycles, so the potential decomposition is standard.
- φ and ψ are continuous: φ(α) = ψ(β)/Ω(α, β) on an open α-interval.

*(b).* The across-cut step is ρ*-unfavourable by the factor φ(α′)/φ(α) < 1. The return along a rook path is
ρ*-neutral, and this uses the consistency of ρ* on Q₁ from (a). CORRECT.

*(c).*
- F1.2(b) runs per edge: world 1 has no errors off R_1j at C^j_t, so property (R) applies.
- D-localization is achieved by choosing targets off D_m.
- On Q₁, u(x₂) = v(x₃) π-a.e. So both are constant on boxes, and rook-connectivity glues the constants (overlapping
  α- or β-projections). CORRECT.

**Measurable case: GAP (fixable); not CHECKED as written.** The Remark is one sentence, and the statement it
"checks" is not the right statement. Write out the following.

1. **Restate (a) a.e.** Fibres of χ are null, and an exact rook cycle through chosen points is a null configuration.
   The correct claim: for π-a.e. z, ω is essentially constant on the fibre χ^{−1}(z) (via the disintegration of μ|_{Q₁}
   along χ); Ω(α, β)Ω(α′, β′) = Ω(α′, β)Ω(α, β′) for a.e. rook rectangle; hence log Ω = g(β) − f(α) a.e., by Fubini on
   boxes and gluing as in (c).
   - Proof device: replace points g^i by value bands A_i := {ω ∈ [a_i, a_i(1+η))}.
   - Use Lebesgue points z^i of the conditional laws P(ω ∈ band_i | χ = z). Their positivity makes the four corner
     sets around each cut-crossing non-null.
   - Only ω enters the conversions, never w₂ or w₃ separately. So no continuity of w_j is needed.
2. **(b)**: φ and ψ are a.e. nondecreasing, so they have nondecreasing versions, which may **jump**.
3. **Q1.23 with jumps.** The first and last steps "cut at the cell edge" are no longer neutral if φ jumps at the
   cut. Fix:
   - choose cell boundaries and route levels at continuity points of φ and ψ;
   - partition each compact level interval so that φ and ψ oscillate by ≤ 1+η on the open subintervals (monotone
     functions are regulated);
   - enter each Z₀-cell through a cut δ′ inside it, depositing only into the part beyond the cut, whose ρ*-mass is
     arbitrarily close to the cell's.

   Intermediate steps need only the oscillation of φ (12-steps) or ψ (13-steps) on the stop regions. w_j cancels,
   because each move conserves w_j-mass.

I believe this works. Until it is written, "Q1.22–Q1.24 for measurable densities" is a sketch, and the
measurable-density uses in §0 and Q1.25(d) should be relabelled accordingly (§1.6).

### 1.5 Theorem Q1.23: CORRECT, with one fixable GAP

**What I checked.**
- *Localizing family.*
  - D_m decreases: A_m, the strip widths 2^{−k−m}, the 1/m-collars and {ρ* > m} all do.
  - μ(D_m) → 0: Leb(⋃_k B_{k,m}) ≤ 4·2^{−m}, π ≪ Leb is finite, ⋂_m D_m is null, and ρ* < ∞.
  - H1.2 accepts any localizing family.
- *Shrinking Z.* X₀ ⪯₁ X by weak (G). The vector of (X₀, Y) is 1_W − 1_{Z₀}, transported by (IB) to X′, Y′ with
  E₁ ∩ M = Z₀ and W.
- *Free room.* W, Z₀ ⊆ M ∖ D_{m′}, and the stops lie in strip preimages ⊆ D_{m′}.
  - Pieces travel one at a time, so a stop is never occupied twice.
  - Deposits go into Z₀, which is disjoint from W.
  - Every move satisfies Q1.21's conditions S_i ⊆ E_{i−1}, T_i ∩ E_{i−1} = ∅.
- *Cell types.*
  - Q₂-cells leave through a 12-step into Q₁. (TC3) and the collar part of B_m guarantee levels just above the cell's
    sup in I₂. Q₃-cells are symmetric.
  - Q₁ cells in the other χ-component (D⁺ vs D⁻) are reached through G; preimages may be in either component.
- *Count.* The deposit into Z₀ ∩ K_l has ρ*-mass ≤ (1+ε)ρ*(W)·ρ*(Z₀ ∩ K_l)/ρ*(Z₀) < ρ*(Z₀ ∩ K_l). So Z₁ ⊊ Z₀ with
  non-null difference, and strict (G) is contradicted.
- *Degenerate case.* If ρ*(W) = 0, the accepted vector 1_∅ − 1_{Z₀} contradicts strict (G) directly.

**GAP (quantifier order).** The note:
1. fixes η, and h so that φ, ψ oscillate by ≤ 1+η on length-2h intervals;
2. builds cells from h and routes from the cells;
3. sets P := maximal route length;
4. "chooses η" with (1+η)^{3(P+1)} < 1+ε.

But h depends on η and P depends on h, so step 4 is circular.

**Fix.**
- **(i) Bound P first, uniformly in h.** G′ is compact and G is open and rook-connected.
  - Cover G′ by finitely many boxes B_r ⊆ G (any two points of a box are 2 rook steps apart inside it).
  - Fix routes between the box centres.
  - Then any two points of G′ are joined in ≤ P₀ := max(centre-route length) + 4 steps, independent of the cell size.
- **(ii) Then choose η** with (1+η)^{3(P₀+1)} < 1+ε, then h, then the cells.
- Alternatively, note that only the first and last steps see the cell width h. Intermediate steps see only the stop
  regions, which can be shrunk after the routes are fixed. The slack η per move can be chosen last.

Either fix is routine.

### 1.6 Corollary Q1.24: CORRECT. H1.2's hypotheses, one by one

| H1.2 hypothesis | Where it comes from in Q1 |
|---|---|
| (H_U) | assumed |
| Worlds 2, 3: integrable densities > 0 a.e. endorsing **all** relevant comparisons | (H_P) = (RL-2) with w_j ∈ L¹, w_j > 0. For integrable weights (E1) and (E2) coincide (H1 §1). Relevant = C ∈ C_L, X regular (write-up §2.7), as in M2 §1 |
| World 1: measurable ρ₁, 0 < ρ₁ < ∞ a.e. on M | ρ* = w₂φ(x₂) on R₁₂ and w₃ψ(x₃) on R₁₃: positive and finite, defined on all of M = Q₁ ∪ Q₂ ∪ Q₃ by (TC3) |
| A localizing family D_m ⊆ M | §4 of Q1, checked in §1.5 above |
| ρ₁μ (E2)-endorses every D-localized relevant comparison | Q1.23. It covers all regular pairs, so a fortiori relevant ones, and its localization ("W ∩ D_m = ∅") is H1.2's (δ ≤ 0 on D_m) |
| H1.2's internal D′_m = D_m ∪ {ρ₁ > m} | already contained (C_m). H1.1's integrability of ρ₁ on M ∖ D_m holds |

H1.2 is R1 (H12_referee). The deduction is correct.

**Scope GAP (wording), and it matters.** Q1.24 is PROVED only with *continuous* w₂, w₃ (Q1.22 at PROVED level).
- In R21's (V), origin II-a, the partners' (RL) densities are only measurable.
- Origin I's ρ*₂, ρ*₃ are only measurable too, and they qualify only when the partners are (RL-2), i.e. their
  endorsement is countably additive. The note does qualify that point correctly.

So §0 "(2) … This closes R21's (V), origin II-a … under (Nest_e) + (TC)" and Q1.25(d) should read:
- "PROVED for continuous partner densities"; and
- "for measurable densities, at the level of the §1.4 sketch".

The (TC) hypothesis is on the cover's own selection, so this closes a sub-branch of (V), not the branch. The note
says this in §6, but §0 reads more strongly.

### 1.7 Q1.25, Q1.26

**Q1.25.**
- (a) is immediate.
- (b) holds as stated: ρ* ∈ L¹ gives (S_int), and K3.1(e) gives Λ_∞ null.
  - The L2/P1-lift exclusion follows: Λ = M with a σ-finite endorser contradicts Q1.22(c), which forces the endorser
    to be c|g₁|, which is integrable for h ≡ 1.
  - This is consistent with P1.14 (σ-finite, non-integrable φ∘x in two worlds). In three worlds with two (RL-2)
    partners and transverse edges, the pinning removes the freedom P1.14 uses.
- (c) is a correct reading of Q1.22(c) and Q1.23.
- (d), last bullet (p.f.a. partners). Choosing *sources* off the partners' carriers D^{ν_j}_m makes π_j(S) = 0 exactly
  (as in M23_referee §3), and ν_j(T) ≥ ρ_j(T) > ρ_j(S) = ν_j(S) rejects at j. CHECKED is fair.
  - The note is also right that exclusion then needs a σ-finite H1.3, which is not proved.

**Q1.26: CORRECT.**
- (i): the sign analysis on R_1j gives {r_j < θ/(1−θ)} in both orientations.
- (ii): D^∓ are intersections of open half-planes.
  - D⁻ projects onto all s > 0 and all t > 0, since min_{K′} q₃ > 0.
  - D⁺ projects onto s < min q₁/q₂.
  - χ = (F₂(1/s), F₃(1/t)) is coordinatewise strictly monotone, so it is a homeomorphism of each chart region, constant
    on rays and open.
- (iii)–(v) check; ω = r₃/r₂ gives ρ* = h|g₁|.
- **Upgrade of the CHECKED item.**
  - F_j(r) = ∫_0^r f_j, where f_j > 0 is the w_j-flux through the level cone {r_j = r} ∩ R_1j. It is continuous,
    because w_j and the Gaussian density are, and positive, because every level cone meets U by (ii).
  - The chart map is therefore C¹ with Jacobian f₂(1/s)f₃(1/t)/(s²t²) > 0.
  - μ's cone density in the chart is C₁(1+s²+t²)^{−2} times a positive radial factor.
  - Hence π has a positive continuous density on G. This is PROVED.

---

## 2. Q3 Part I

### 2.1 Lemma Q3.20: CORRECT

- The (CA) condition is linear in ρ with bounded test functions, so 𝒞𝒜_j is closed in L¹.
- The series Σ2^{−n}ρ_n/(1 + ‖ρ_n‖₁) gives the maximal support.
- The (NC) clauses follow from K3.1(a), (c).
- C_L is by definition the set of coherent undominated models (write-up §2), so coherence of C_q is free; (C) is not
  needed.

### 2.2 Lemma Q3.21: CORRECT (priority 1)

- **Compactness.** Coherent models are D_K with K ⊇ K′ (H12_referee §1.1). Hausdorff compactness and R1 Prop. 3.1
  give a subsequence D_{K_m} → C in measure.
  - C is regular, as a limit of regular models in measure.
  - ψ_j(C) = L, because ψ_j is 1-Lipschitz for ρ_jμ(· △ ·) and ρ_j ∈ L¹.
  - A further subsequence has Σε_m < ∞.
- **The test model is legal.** E_jY_{m₀} := ⋃_{m≥m₀} E_jC_{q_m} ⊆ M, and Y_{m₀} = P_j △ (that union).
  - Y_{m₀} is regular: P_j is regular and only M is toggled.
  - Y_{m₀} ∈ M_U, as every measurable subset of U is.
- **Weak (G)** gives C_{q_m} ⪯_j Y_{m₀} for m ≥ m₀. The world-j section at Y_{m₀} is closed by (S) and contains the
  tail, so it contains q.
- **(CA) and the bound.** C_q ∈ C_L, so (CA) applies to C_q ⪯_j Y_{m₀}. The inclusion
  E_jC_{q_m} ⊆ E_jC ∪ (C_{q_m} △ C) gives ψ_j(C_q) ≤ L + Σ_{m≥m₀}ε_m → L.

This is a genuinely better device than M2.1: (G) does the work (RL-1) did. §5's diagnosis of why it fails for
p.f.a. endorsers is correct. π_j(⋃ tail) is not controlled, and the union test is not localized.

### 2.3 Proposition Q3.22: CORRECT (priority 3)

- M2.2 step 1 uses only (RL-2) contraposed.
- Step 3 is K2 (1.1) for any ρ_j ∈ L¹₊. Zero measures in ℳ are harmless: divisibility is vacuous for them.
- Step 4 needs exactly ψ_j(C_{q*}) ≤ L_j, which Q3.21 supplies.
- The remark that a zero-density partner forces nothing is right. Forced pairs then have S ∖ {1} inside the
  positive-density partners.

### 2.4 Theorem Q3.23: CORRECT (priority 2)

- **Closed sets.** F_j is a sublevel set of an lsc function, hence closed. F₁ := cl O is closed.
- **Covering.** The three-case analysis is exhaustive.
  - Case 1 ∉ supp q, with every j ∈ supp q above level ψ_j(B) + η: competitiveness of C_q on supp q gives
    i ∈ supp q with C_q ⪯_i B. (CA) then gives ψ_i(C_q) ≤ ψ_i(B), a contradiction. So this case is empty.
  - The face-wise KKM hypothesis holds.
- **The margin is built in.** On O, ψ_j(C_{q_m}) > ψ_j(B) + η, so L_j ≥ ψ_j(B) + η > ψ_j(B) strictly. That is why
  B± is no longer needed.
- **The limit pair.** The definition of a limit pair constrains only the approximating sequence (M23_referee §2), so
  1 ∉ supp q* is harmless.
- **Conclusion.** L4.0 is n-free (M23_referee §2).
- **No positivity** of ρ_j is used anywhere.

NUMERICS (A)–(C) reproduce.

### 2.5 Theorem Q3.24: CORRECT, at M2.6′'s status

The inputs check, and M2.6′ needs nothing beyond them (M23_referee §4: (B1) is field-level).
- (CA⁺) ⇒ ρ^ca_j > 0 a.e.
- Q3.25 gives (γ₀), admissibility and, through c♮ ≠ 0, coherence of every B_q.
- H1.1 step 4 uses only ρ₂, ρ₃ > 0.

(RL) ⇒ (CA⁺) strictly. A Pareto unanimity of densities is endorsed by each of its densities and fails (RL-1).

### 2.6 Theorem Q3.25: CORRECT; one wording GAP

- **(a)** is Q3.23.
- **(b) step 1.**
  - (T1, Y_W) is forced through Ω: T1 ∈ C_L, Lemma IC applies, and so does (CA).
  - π(δ_W) = 0 exactly, because W ⊆ M ∖ D_m ⊆ M ∖ D_{m′} for all m′ ≥ m.
- **(b) separation.** It needs no positivity. With a zero partner density, (b) may hold trivially at that vertex,
  which is correct and is precisely a degeneracy.
- **(c)** is L4.1.2 with c ≠ 0 a.e.

**GAP (wording).** "Let ρ^ca_2, ρ^ca_3 be *the* maximal (CA) densities" suggests uniqueness, but only the supports are
unique. The forced family 𝔉𝔏 depends on the values of ρ_j (forcedness is ψ_j(X) < ψ_j(C)). So φ*, ρ♮₁, Λ♮ and hence
b♮ depend on the choice.
- Every statement of Q3.25–Q3.27 holds for every choice, so nothing is lost.
- Say "for every choice of maximal-support (CA) densities", as R21 does for ν*.
- Λ^ca_j is choice-free (Q3.20).
- Whether Λ♮ is choice-free is not shown. A union of forced families over different ρ's would need a common ℳ for
  K2.1, so it is not obvious.

### 2.7 Corollary Q3.26: the trichotomy is CORRECT; the reading overclaims (GAP, scope)

**The proof.**
- **b♮ = 0.** All three densities are positive, so H1.1 step 4 forces p* ∈ Δ°. M0closed(a) applies.
- **b♮ = 1 at a partner k (say k = 2).**
  - ρ♮₁ > 0 and ρ^ca_3 > 0 a.e. Permuting H1.1 step 4 leaves p* ∈ Δ° or p* = e₂.
  - (B1), L4.6–L4.9, Prop. R and L4.7 are field statements (L4_referee §§4.1–4.2 re-read them as such). T1, u and K′
    are S₃-symmetric, and L4_referee §5(b) records the needed equivariance B^σ_q = σB_{σq}.
  - So A(c♮) = {e₂} and Λ^ca_2 ⊋ E₂(T1) ∩ M. This is CORRECT (case (II) CHECKED).
- **b♮ ≥ 2** is bookkeeping, and L4.3 is admissibility-only. CORRECT.

**The overclaim.** §0 item 4 says "(S) collapses … is no longer a separate leaf: it is (V) or a multi-blind
configuration of c♮". This conflates field-level configurations with R21's leaves.
- **b♮ = 1 at a partner e_j is not R21's (V).**
  - In R21's (V) the blind world's partners add up.
  - Here one partner of world j is the (NC)-failing world 1, which has only a forced-limit endorser. World j itself may
    have (NC) with p.f.a. endorsers.
  - R21's structure items (V2)–(V5) (N2.3′, N2.4, N2.5′; via M1.3/M1.6/M1.7) are not available. Q3 itself says
    N2.3–N2.6 are not re-derived.
- **b♮ ≥ 2 is not R21's (P0)/(PD)/(E)/(X).**
  - Those leaves carry ranking-level structure that needs (NC) at every world: N1.2's edge dichotomy and N1.3(c)
    rigidity.
  - R21 states (via M1.1′(c)) that (PD) cannot be closed by field questions without N1.2.
  - For c♮ only N2.1/N2.2/N2.2′ (Q3.27) are available.

**Requested restatement.** (S) splits as follows.
- **(S-CA⁺)**: both partners of the failing world are (CA⁺). It is closed into (V) origin II-a, whose definition is
  widened from (RL) to (CA⁺) (Q3.24).
- **(S♮)**: some partner has Λ^ca non-null. It is a new leaf, with structure "c♮ has (γ₀), T1 c♮-admissible,
  A(c♮) = {e_j} with Λ^ca_j ⊋ E_j(T1) ∩ M, or b♮ ≥ 2", and N2.1/N2.2/N2.2′ at every edge. Its open question is Q_S♮.

That is a real sharpening of R21: the defining cut moves from (RL) to (CA⁺), and a structure theorem appears where
there was none. It is not a collapse.

### 2.8 Q3.27 and §4

**Q3.27: CORRECT.**
- π(W′) = 0 exactly, by the same decreasing-carrier argument.
- The margins survive by absolute continuity (ρ♮₁, ρ^ca_j ∈ L¹).
- 1 ∉ S contradicts competitiveness. 1 ∈ S gives a forced pair, which φ* must endorse but which it ranks strictly
  worse.
- It is N2.1′ widened to (CA) partners and to arbitrary C ∈ C_L competitive on S.
- As N12_referee §2.1 notes for N2.1, w may be a vertex of Δ_S.

**§4.**
- §4.2 (Λ^ca = M for P1.10's world from P1.13) is CORRECT: P1.13 is refereed CORRECT in P1_referee.
- **Wording slip in §4.3.** "Here world 1 is not integrable, so H1.2 does not apply" should read: "a partner of the
  candidate exceptional world (world 2 of P1.10 type, or world 1 failing (NC)) has no integrable endorser of all its
  relevant comparisons, so H1.2 does not apply".
- §0 item 1, "(this is (RL-2) alone)", should read "(RL-2) without the positivity clause". M2's (RL) includes
  ρ_j > 0.

---

## 3. Cross-note consequence (for the integrator)

Q1.24 needs only (RL-2) = (CA⁺) partners. So it applies verbatim inside Q3.24's widened (V):
- every cover in which some world has two (CA⁺) partners and nested edges with (TC) at its vertex is excluded,
  whatever the (NC) status of that world;
- this is PROVED for continuous partner densities, and at sketch level for measurable ones (§1.4).

Combined with Q3.26:
- a surviving cover in (S) must have a partner without (CA⁺) (Q_S♮);
- a surviving cover in (V) with (CA⁺) partners must have a non-nested edge, or a comonotone part of Q₁, at the blind
  vertex (Q_Q1).

**Nearby result available.** Writing §1.4 upgrades Q1.24 to measurable densities. With that, "(V) with (CA⁺)
partners and (Nest_e) + (TC) at e₁" is closed outright. In particular the R21 (V) origin II-a sub-branch with
transverse nested edges is closed, with no continuity proviso.

---

## 4. Requested changes

1. Q1 §0, Q1.24, Q1.25(d): add "continuous partner densities" to every "closes (V)" claim, or write §1.4 of this
   report.
2. Q1.22 Remark (measurable): restate a.e., as in §1.4. Relabel it *sketch* until written.
3. Q1.23: fix the quantifier order (bound P₀ uniformly first; §1.5).
4. Q1.26: upgrade "π ~ Lebesgue" to PROVED, with the Jacobian argument of §1.7.
5. Q3.25–Q3.26: "for every choice of maximal-support (CA) densities". Λ♮ and b♮ are choice-dependent; Λ^ca_j is not.
6. Q3 §0 item 4 and Q3.26's last paragraph: replace "(S) collapses / is no longer a separate leaf" by the split
   (S-CA⁺) → (V) and (S♮), as in §2.7. Flag that b♮ = 1 at a partner is a field-level vertex configuration, not R21's
   (V).
7. Q3 §4.3 and §0 item 1: the two wording slips of §2.8.
8. R21 ledger: update II-a's definition to (CA⁺) partners (Q3.24). Record Q3.21 as the lsc input. Record Q1.24 as
   closing the (TC) sub-branch of (V) with (CA⁺) partners.

## 5. Files

`q13ref_py/ref_loops_scaling.py`, `q13ref_py/ref_loops_scaling.out`: shrinking-cell rerun of the Q1 rook loops
(imports `q1py/q1_loops.py` read-only).
