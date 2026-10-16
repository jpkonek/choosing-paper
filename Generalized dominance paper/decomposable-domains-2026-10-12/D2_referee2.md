# Referee report (second, independent) on D2_notes.md: Theorem D2.1

15 Oct 2026. Adversarial reading of D2_notes.md against the write-up (§§2–3, §8.4–8.5), C2_notes (top), N17, N19_referee,
P4B_referee, Q1 and the round-13 results quoted in the write-up (Lemma T₁, Cor. IS, Props MP, Q15, S32, S33).
I did not read D2_referee.md and did not run or read the author's `d2py/`. My own scripts are in `d2ref2_py/`, run
with `python3 -I`. They use exact integer or rational arithmetic, and no verdict depends on them.

## 0. Verdict

**Theorem D2.1 is CORRECT** as stated, with weights read as real-valued finitely additive set functions (the
write-up's and N19's convention: bounded charges). I tried to break every axiom: strict (G) under R⁺, transitivity,
cancellation, closed sections, (K), and (C). I found no counterexample. Every step re-derives. There are two small
GAPs in the presentation, both fixable in a line, and one **substantive scoping remark** (§3):

> World 1 *does* add up if the endorsing weight may be σ-finite with infinite total mass. The measure
> ν = ρλ, with ρ(x) = 1/(1−x) on M and ρ = 1 on N₊, is countably additive, strictly positive on non-null sets, and
> endorses **every** world-1 comparison between regular models, relevant ones included. Its Bayes sets are exactly
> the chain C_b. So the failure of SP^reg in D2 is **exactly** a failure of integrability of the endorsing density
> at the protected end x = 1.

This does not affect the refutation of N17.B′, N17.B′(2) and Q1.C1, or the negative answer to (R2). All of these
are stated for bounded charges. It does affect how §0/§5 should describe the T1 situation. The nearby open
statement that D2 does **not** refute is "SP^reg with a locally integrable (σ-finite) density". It is the natural
next target (§3.3).

| Item | Verdict |
|---|---|
| §1 coordinates (C2.1 path, x pushes λ\|_M to Lebesgue, c_b = {x<b}, E₂C_b = d_b) | CORRECT |
| Lemma D2.2 (designs exist) | CORRECT; NUMERICS confirm incidence and bounds for n = 1, 2, 3 |
| Lemma D2.3 (preorder, strict (G), (IB)) | CORRECT |
| Lemma D2.4(i) (non-regular sections) | CORRECT |
| Lemma D2.4(ii) (regular sections) | CORRECT |
| D2.1 step 2 ((K) for every model) | CORRECT |
| D2.1 step 3 (closed sections, both worlds) | CORRECT |
| D2.1 step 4 (no weak domination of C_b) | CORRECT; GAP (cosmetic) at b = 1, see §2.4 |
| D2.1 step 5 (C_L, (C), (LA)) | CORRECT; a direct proof without Theorem kkm is given in §2.5 |
| D2.1 step 6 ((LF)) | CORRECT |
| D2.1 step 7 (no bounded endorsing charge positive on c_a) | CORRECT for every real-valued finitely additive ν ≥ 0; **false for σ-finite weights** (§3). Statement should say "finite" |
| Remark "Mode (M2)" | CORRECT; a direct proof is in §3.2 (no appeal to N17.3) |
| Remark "Consistency with the corpus" (Lemma T₁, QC₁, SR₁, rate) | CORRECT (§2.7) |
| Remarks "Why R⁺" and "Why the protected end" | Heuristic. Not precise enough to be labelled PROVED; relabel them as remarks. No result depends on them |
| §0 consequences: N17.B′, N17.B′(2), Q1.C1 refuted; (R2) negative | CORRECT (bounded-charge formulation, which is the corpus's) |
| §0/§5 "the positive route for T1 is open again" | Fair, but should mention §3: the D2 mechanism is σ-finitely additive |

## 1. Setting checks

- **Vector form.** On M_U, X ⪯₁ Y depends only on δ = 1_{E₁Y} − 1_{E₁X}, so (IB) and de Finetti cancellation
  (A ≤ B ⟺ A∖B ≤ B∖A) are automatic.
  - Every pair δ₁, δ₂ with ternary sum is realised by a triple of models. Pick e_Y := 1 where δ₁ = 1 or δ₂ = −1, and 0
    where δ₁ = −1 or δ₂ = 1. These choices conflict only when |δ₁ + δ₂| = 2.
  - So transitivity of ⪯₁ is **equivalent** to closure of 𝒜₁ under ternary sums. Lemma D2.3 proves exactly that.
- **Null-invariance.** Every clause of R⁻/R⁺/R⁰ is an integral or an a.e. condition, so it is invariant under null
  changes.
- **Chain.** For K = [l, r] (m = weight on world 2), a mixed h with h₁ > 0 > h₂ is in E₁D_K iff θ(h) ≤ r, and one with
  h₁ < 0 < h₂ is in E₁D_K iff θ(h) < l, where θ(h) = h₁/(h₁ − h₂). Both endpoints of K_s = [α′s, β′ + (1−β′)s] increase
  in s, so the c_s are nested. The law of θ is continuous with full support on the relevant ranges. The reindexing
  b = λ(c_s) is therefore a homeomorphism and x is uniform. The interior K_s contain K′ in their relative interior,
  so ∂C_s ∖ 0 ⊆ U and (LF) holds with N = U. ✓

## 2. Line-by-line

### 2.1 Lemma D2.2 (designs)

- (D1) ✓.
- (D2): same level, distinct lines meet in exactly one point, so Leb(Ŷ ∩ Ŷ′) = 1/Π_n. For the same line it is
  (q+1)/Π_n. Across levels the coordinates are independent, so it is (q_n+1)(q_{n′}+1)/(Π_nΠ_{n′}). Each block B_m
  contributes λ(B_m)·Leb(·) > 0, and every {x ≥ t}, t < 1, contains a block. ✓
- (D3) ✓.
- (D4): each strip carries L_n generators, so Σ1_P/L_n = 1_{c_a} exactly (pointwise, not only a.e.). Each v has v_n in
  exactly one J_{n,π}, so Σ1_Q/L_n ≤ (q_n+1)/L_n **everywhere**. The bound 2(q+1)2ⁿ/q² needs L_n ≥ Π_n/2^{n+1},
  i.e. Π_n ≥ 2^{n+1}. This holds. ✓
- ι is defined everywhere (terminating expansions), measurable and measure-preserving. ✓

NUMERICS (`design_check.py` → `design_check.out`; PG(2,q) for q = 5, 17, 67, the least primes ≥ 4ⁿ):
- all line pairs meet in exactly 1 point and every point is on q+1 lines;
- maximal multiplicity of assigned lines = q+1;
- (q+1)/L_n = 2/5, 9/38, 68/569, each below the note's bound (0.96, 0.498, 0.242);
- digit-splitting by 2-adic valuation is uniform on all 64 joint cylinders of depth 12;
- 0 failures.

### 2.2 Lemma D2.3 (strict (G), transitivity)

Every case re-derived.
- **Fact (F).** For t ≥ a, P_g ∩ {x ≥ t} = ∅ and g_* = 0 on N₊, so τ_{g_*}(t) = λ(Q_g ∩ {x ≥ t}) ≥ 0.
- **Near-one lemma.** On {x ≥ max(b*, a)}, g_* = 1_{Q_g} (the note says 1 − h₀; a suffices).
- **Strict (G) under R⁺.** R⁺ needs D > 0, so no δ ≤ 0 reaches it. For δ ≥ 0, −δ has D ≤ 0.
  - If D(−δ) = 0, then δ = 0 on N₊.
  - −δ ∈ 𝒦₀ forces ∫δ ≤ 0, so δ = 0.
  - −δ − g_* ∈ 𝒦₀ forces −δ ≥ 1_{Q_g} near 1, which is impossible.
- **Sums.** D is additive and R⁻ makes D ≥ 0 on 𝒜₁.
  - Mixed R⁺/R⁰ sums use (F).
  - The decisive case: two generator-type summands force σ ≥ 2 on Q_g ∩ Q_{g′} ∩ {x ≥ t*}, which is non-null by
    (D2). So **no two exotic comparisons ever chain**, and transitivity never has to accept a sum that would separate
    targets.

I searched for a transitivity failure along the obvious adversarial lines:
- X = C_a, Y = X_g, Z = Y with a second disjoint source P_{g′} traded for Q_{g′}. Then
  δ_{YZ} = 1_{Q_{g′}∖Q_g} − 1_{P_{g′}}, and δ_{YZ} − g′_* = −1 on Q_g ∩ Q_{g′} near 1, so Y ⋠₁ Z. Hence the hypothesis
  of transitivity fails and there is nothing to check.
- R⁺ chains through non-regular intermediates: R⁺ tails on [a, 1] are additive.

No failure. ✓

### 2.3 Lemma D2.4 (sections)

**(i)** τ_{δ_b}(t) = ψ(t) − b for t < b, with ψ(t) = t + λ(N_X) + λ(A ∩ {x ≥ t}), which is nondecreasing. On [a, 1]
the binding point is t = a. Since ψ(a) ≥ a, S₁ = [0, min(1, ψ(a))]. ✓

**(ii)**
- **B₀.** φ(t) = t + λ(A ∩ {x ≥ t}) is nondecreasing, so the binding tail is t = 0, which gives b ≤ λ(A). For b = 1,
  −1_{M∖A} ∈ 𝒦₀ iff A = M. ✓
- **B_g.**
  - b = 1 is excluded by the near-one clause and (D2). ✓
  - Eligibility is independent of b. ✓
  - The initial-segment argument is correct. ✓
  - Closedness is a pointwise limit and does not need continuity of u_g. ✓
  - Bounds: the t = 0 bound is β_g ≤ λ(A) + λ(P_g) − λ(Q_g). The t = a bound for b > a gives b ≤ 1 − λ(Q_g) < 1. ✓
- **Union.** Every g with β_g > (s + β₀)/2 has λ(P_g) > (s − β₀)/2. By (D3) there are finitely many, and they include
  the g's that approach s, so s is attained. ✓

This is exactly where an adversary would look: sources shrinking with targets near 1. The thin sources make all but
finitely many generators irrelevant to the top of any section, and **(D3), not (D2), is what does it**. ✓

On "sequences of models converging in measure whose comparisons flip in the limit": these exist, but no axiom
forbids them. (S) asks for closedness in p for each fixed X, not continuity in X. Example: A = ∅ with
λ(N_{X_k}) = η_k ↓ 0 gives C_a ⪯₁ X_k for all k (S₁(X_k) = [0, a + η_k]), but X_k → C_0 and C_a ⋠₁ C_0. This is the
N19 Prop R3 priority on unanimous errors, which the note correctly says touches no relevant comparison. The
generator models X_g also converge to C_a as the level n → ∞, with C_a ⪯₁ X_g for every g. That is harmless too.

### 2.4 Theorem D2.1 steps 2–4, 6, 7

- **Step 2 ((K)).** Re-derived for both λ(N_X) > 0 (R⁺) and N_X null (𝒦₀ with b* = b). Vertices by (G). ✓
- **Step 3.** World 2: C_b ⪯₂ X ⟺ b ≥ λ(A) − λ(N_X), which is closed. World 1 by D2.4. Composition with the continuous
  p ↦ p₂. ✓
- **Step 4.** Correct conclusion, one cosmetic **GAP**. At b = 1 we have c_1 = M, P = M∖A and Q = ∅, so
  δ′ = 1_{M∖A} − 1_{N_X}. If N_X is null, δ′ = 1_{M∖A} ≥ 0. Then "δ′ − g_* ≤ −1 on Q_g near 1" is **false** when
  Q_g ⊆ M∖A near 1. The conclusion survives because Q = A ∖ c_1 = ∅ trivially. *Fix:* treat b = 1 separately (Q = ∅;
  X ⪯₂ C_1 forces λ(M∖A) = 0) or restrict the generator sentence to b < 1, where δ′ = −1_Q ≤ 0 on {x ≥ b}.
- **Step 6.** ✓
- **Step 7.** X_g is regular, C_a ∈ C_L, and 1_{E₁X_g} − 1_{c_a} = g_* exactly, so the comparison is relevant and
  accepted. For a **real-valued** finitely additive ν ≥ 0: ν(c_a) = Σw_gν(P_g) ≤ ∫Σw_g1_{Q_g}dν ≤ εν(M). This uses
  pointwise identities, so it holds even without null-invariance. ✓
  - A real-valued finitely additive ν ≥ 0 is automatically bounded by ν(U), so "finitely additive" in the statement
    should read "**finitely additive, real-valued**" (or "bounded charge"). See §3 for why this word matters.
  - Complement: ν = λ|_{d_a} endorses every relevant comparison (base cone: τ_δ(a) ≥ 0; generators: (F)). So in
    Cor. IS terms **a\* = a exactly**: every bounded endorsing charge kills c_a, and some kills nothing else.

### 2.5 Step 5: a direct proof of U_L = {C_b} (suggested replacement for the appeal to Theorem kkm)

Every X ≠ C_b is strictly dominated by an explicit selected model.
- **X regular.** Take b := λ(A).
  - C_b ⪯₂ X holds with equality.
  - C_b ⪯₁ X holds by B₀.
  - If also X ⪯₁ C_b, step 4 (with X ⪯₂ C_b by equality) gives X = C_b.
  - So X ≠ C_b is strictly worse at world 1.
- **X non-regular.** Take b := max(0, λ(A) − λ(N_X)).
  - C_b ⪯₂ X holds.
  - b ≤ λ(A) ≤ a + λ(A ∩ {x ≥ a}) ≤ ψ(a), so C_b ⪯₁ X by D2.4(i).
  - X ⋠₁ C_b by R⁻.

So (C), (LA) and C_L = {C_b} follow without the KKM theorem for preorders. Nothing is wrong with citing it, but the
direct argument is one paragraph and removes a dependency.

### 2.6 Strict (G) / (C) for non-regular models under R⁺

- R⁺ is never used against a regular model: X ⪯₁ (regular) requires D ≤ 0, and with N_X non-null that is rejected
  by R⁻.
- Non-regular models can be *very* badly ranked at world 1 (e.g. C_a ⪯₁ X for E₁X = N_X of tiny measure). This is
  permitted by (G), because δ is not ≥ 0.
- No incoherent model is undominated (§2.5).

### 2.7 Corpus consistency

I checked that D2 contradicts no proved result quoted in the write-up.
- **Lemma T₁ at 1.** Z ≤₁ Q with Q ⊆ d_{1−η} needs λ(Q) ≥ λ(Z) (base) or λ(Q) ≥ λ(Z) − λ(P_g) + λ(Q_g) together with
  Q ⊇ Q_g near 1. Hence η₁(Z, 1) ≥ min(λ(Z)/2, min{λ(Q_g) : λ(P_g) ≥ λ(Z)/2}) > 0, a finite minimum by (D3). This
  bound depends only on λ(Z), so the qualitative rate (Cor. SR) holds, as it must next to an additive world 2.
- **Rate.** For level-n sources, P_g ≤₁ Q_g ≤₁ [1 − λ(Q_g), 1) (the base cone right-packs, Prop. S33(c)). So
  η₁(P_g, 1) ≤ λ(Q_g) = h₀(q_n+1)/Π_n ≈ h₀/q_n ≤ h₀4^{−n} ≈ (h₀/a²)·λ(P_g)², quadratic and so superlinear as
  claimed. This is consistent with Props LIN and ExA.
- **(QC₁)-type bound.** κ₁(Z) := inf{λ(A) : Z ≤₁ A} ≥ min(λ(Z)/2, min_{finitely many g} λ(Q_g)) > 0. At t = a,
  generator acceptance forces λ(A ∩ {x ≥ a}) ≥ λ(Q_g).
- **Prop. Q15.** There is no simple, vanishing-target or fixed-source star certificate. Each fixed source can use only
  finitely many generators with λ(P_g) bounded below.
- **Prop. S32(d).** "inf over the family of target measures > 0" refers to families attached to a *fixed* source
  window. Here inf_g λ(Q_g) = 0, but S32 is stated for worlds band ∪ ⋃𝒢(F) with targets F ⊆ d_a used against
  *all* sources. In D2, generator g is usable only by sets containing its own source P_g (the tails at t = 0 and the
  near-one clause tie it). The D2.4(ii) bound β_g ≤ β₀ + λ(P_g) is what replaces S32's hypothesis. There is no
  conflict, but a sentence in the note explaining why S32 does not apply would help readers.

## 3. Substantive remark: σ-finite additivity of world 1

### 3.1 Statement (PROVED here)

Let ρ(x) := 1/(1−x) on M (any nondecreasing ρ > 0 with ∫_{Q_g} ρ dλ = ∞ for all g will do, e.g. 2^m on B_m) and
ρ := 1 on N₊. Put ν := ρλ.

Then ν is countably additive and σ-finite, positive exactly on non-null sets, and finite on every c_b, b < 1. It
endorses every comparison X ⪯₁ Y between regular models, i.e. ν(E₁X) ≤ ν(E₁Y) in [0, ∞], and so every relevant
comparison.

*Proof.* Let δ = 1_{E₁Y} − 1_{E₁X} be accepted with D(δ) = 0. In both R⁰ branches δ = 0 on N₊.
- **Base branch (δ ∈ 𝒦₀).** δ ≥ 0 on {x ≥ b*}, so δ⁻ ⊆ {x < b*} and ∫δ⁻ρ < ∞. Tonelli applied to δ⁺ and δ⁻
  separately gives ∫δρ = ρ(0)τ_δ(0) + ∫₀¹ρ′(s)τ_δ(s)ds ≥ 0, because τ_δ ≥ 0 and ρ′ ≥ 0.
- **Generator branch (δ − g_* ∈ 𝒦₀).** δ ≥ 1_{Q_g} on {x ≥ t*}, so ∫δ⁺ρ ≥ ∫_{Q_g ∩ {x ≥ t*}}ρ = ∞, while
  ∫δ⁻ρ < ∞.
- For ρ = 1/(1−x): ρ ∈ [2^m, 2^{m+1}] on B_m and λ(Q_g ∩ B_m) = 2^{−m−1}Leb(Ŷ_g), so each block contributes at
  least Leb(Ŷ_g)/2. The sum diverges, and it diverges on every tail {x ≥ t*}. ∎

Moreover:
- The pointwise "Bayes sets" {q·c > 0} of the extended assessment (ψ₁ = ∫_{E₁}ρ dλ, ψ₂ = λ(E₂)) are exactly the
  chain C_b, with b = ρ^{−1}(q₂/q₁).
- On P₁ ∩ M, h is rejected iff q₁ρ(x) ≤ q₂; on P₂ ∩ M, h is accepted iff ρ(x) < q₂/q₁. Both are initial segments
  in x.

So D2 is an (M0)-type system **in the σ-finite sense**: world 1 is a sub-relation of an additive order with a
strictly positive density that is integrable on every compact part of the chain and non-integrable only at the
protected end. In the write-up's phrase (§8.5, tilt-world paragraph), D2's world 1 is "a weight infinitely heavy on
spread thin sets". That weight exists here as a genuine σ-finite measure.

NUMERICS (`cell_model.py` §6): with ρ nondecreasing on the cells and huge on the proxy near-one block, all 5672
accepted relevant comparisons in the pool are endorsed (0 failures).

### 3.2 Consequence: a direct proof that the mode is (M2)

Let Σ_k c_kδ_k ≤ 0 a.e. with c_k > 0 and δ_k relevant. Each δ_k⁻ ⊆ c_{b_k} with b_k < 1 (C_1 ⪯₁ X forces X = C_1),
so every ∫δ_k⁻ρ is finite and ∫(Σc_kδ_k)ρ = Σc_k∫δ_kρ ≥ 0. With Σc_kδ_k ≤ 0 and ρ > 0 this gives Σc_kδ_k = 0 a.e.
So there is no finite obstruction. This is self-contained and replaces the appeal to N17.3 in the "Mode" remark.

### 3.3 What this means for the claims in §0/§5, and the nearby target

- **Still correct.** N17.B′, N17.B′(2) and Q1.C1 are false, and (R2) has a negative answer. All of these are about
  bounded charges (N19 §3, "Let ν be a bounded charge"; write-up Def. addup via the Yosida–Hewitt countably additive
  part, which presupposes boundedness).
- **Should be added to §0/§5.** The D2 mechanism is "additive with a non-integrable density at the protected end".
  The natural weakened conjecture, which D2 does **not** refute, is:
  - **N17.B′_σ (suggested CONJECTURE).** In a full system, each world has a countably additive endorsing measure
    ρ_iμ with ρ_i > 0 a.e. and ρ_i locally integrable on U. In D2, ρ blows up only as x → 1, i.e. near the boundary
    ray of U on the e₂ side, and is bounded on every closed subcone of U.
  - For T1, the relevant question is whether Prop. M0 survives for such σ-finite supporting assessments. The
    write-up states that the closing argument of M0closed "uses no integrability", so the gap would be confined to
    Prop. M0 (α)–(γ), which use the Lyapunov range and finite Bayes risks. If Prop. M0 localises, i.e. it is applied
    to models that differ only on a set where ρ is integrable (for instance a neighbourhood of ∂D_{T1}, which lies
    inside U), then the D2-type failure would be excluded at T1 by the same route.
  - Not attempted; recorded as the nearby reachable target suggested by D2.
- **CONJECTURE D2.C** (installing the D2 world on an edge region in three worlds) would, if carried out with the same
  design, again be σ-finitely additive near the vertex end. So it would refute the bounded N17.B′ in three worlds,
  not N17.B′_σ.

## 4. Independent NUMERICS (`d2ref2_py/`)

**`design_check.py` → `design_check.out`:** see §2.1. 0 failures.

**`cell_model.py` → `cell_model.out`:** a finite exact-integer proxy, with a different design from the author's:
- levels with PG(2,3) and PG(2,5);
- targets are product sub-cells (π₁, π₂) in two near-one blocks, and the last block is the proxy for "near 1";
- source strips of sizes 1/4 and 1/8;
- N₊ split into 4 sub-cells.

| Test | Count | Failures |
|---|---|---|
| generator comparisons accepted | 40 | 0 |
| pairwise target meeting in the last block | 820 | 0 |
| strict (G), random δ ≥ 0 including non-regular | 400 + 400 | 0 |
| −1_Q rejected | 40 | 0 |
| transitivity triples on a 59-model adversarial pool (C_b, X_g, two-generator chains with overlapping targets, packing moves, non-regular and randomly perturbed models) | 4758 | 0 |
| sections are initial segments | 59 | 0 |
| D2.4(i) formula | 10 | 0 |
| D2.4(ii) union formula, cuts below the proxy block | 49 | 0 |
| (K) at cuts below the proxy block | 24 249 | 0 |
| no weak domination of C_b | 47 958 | 0 |
| ρ-endorsement | 5672 | 0 |

The 687 (K) failures at cuts *inside* the proxy near-one block are a proxy artefact and are reported separately in the
output. A finite model cannot let b* approach 1 beyond b. In the continuum, every b < 1 leaves a non-null {x ≥ b},
and step 2's proof applies verbatim.

## 5. Requested changes

1. **Step 7 / Theorem statement.** Say "finitely additive, real-valued (bounded)". Add the σ-finite remark of §3.1,
   and qualify §0/§5 accordingly. Suggest N17.B′_σ as the surviving target.
2. **Step 4.** Treat b = 1 separately (cosmetic).
3. **Step 5.** Optionally replace the appeal to Theorem kkm by the direct domination argument of §2.5.
4. **"Mode" remark.** Use the direct argument of §3.2.
5. **Relabel** "Why R⁺" and "Why the protected end" as heuristics (not PROVED). The non-closed section formula
   [0, a + r + η − κ) depends on an unspecified alternative rule.
6. **Add one sentence** on why Prop. S32(d) does not apply (§2.7).
