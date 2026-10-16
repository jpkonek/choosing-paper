# N19. Referee report on N17_notes.md ("Rankings that do not add up")

13 Oct 2026. I am an independent referee and did not write N17. Every step was re-derived against BRIEF5, BRIEF6,
N9 (N9.2, N9.4, Cor 3.3), N10, N11 §§0–3 (Fact 1.2, Lemma 3.1, Cor 3.2), N13 (Prop B), IRC ("Incomplete Rankings and
Coverage.tex": §NCsetup, Lemma accept, Thm NC, Cor NCext, Lemma smallcanc, Ex. K4, Ex. half5, Thm/Cor twoNC, §EXT) and
LDG v2 §§1–3 (definitions of C_L, (S), Thm kkm).
- Verdicts: **CORRECT**, **CORRECT WITH REPAIR**, **GAP**, **FALSE**.
- New statements here are labelled PROVED (full proof below) or NUMERICS.
- Scripts are in `n19py/`; run them with `python3 -I`. I also re-ran N17's scripts in `n17py/`, and they reproduce.

## 0. Summary table

| Item | Verdict | One-line reason |
|---|---|---|
| N17.1(a) normal form | CORRECT | Sum-closure under 𝒞-valued sums is exactly transitivity in one layer (pointwise realisation checks). |
| N17.1(b) chaining, no money pump | CORRECT | — |
| N17.1(c) charges ⇔ (NC_𝔊); strict positivity from covers; (NC)⇔(NC⁺) under 𝔉 | CORRECT | IRC Thm NC(a)–(c) in one layer; the cover computation checks. |
| N17.1(d) ≥ 5 exchanges for an (NC) violation | CORRECT | This is for certificates ≤ −1. For certificates ≤ 0, ≠ 0 (the kind Lemma 3.1 treats) the bound is **4** (smallcanc; K4 attains it). |
| N17.2 Prop 2.1 (CA charges) | CORRECT | (α), (β), (γ) check. (W) is used only on 𝔚, and in fact only against *regular* X (§3.3). |
| N17.2 general charges (via N13 Prop B) | CORRECT WITH REPAIR | (W) is indeed used only on 𝔚. But with pure parts, the a.e.-unique Bayes models are only shown *coherent*, not *selected*. |
| N17.2 "equivalently (NC_{𝔚∪𝔉})" | CORRECT WITH REPAIR | Only one direction holds: (NC_{𝔚∪𝔉}) ⇒ a strictly positive weak charge on 𝔚 (SP). The converse is not shown. |
| N17.2 trichotomy (i)/(ii)/(iii) | CORRECT WITH REPAIR | (ii) is **empty**: a strictly positive charge has a CA part > 0 a.e. (Lemma R1). The real dichotomy is SP_i vs ¬SP_i. |
| N17.2 choice of 𝔚 (all X ∈ M_U) | CORRECT WITH REPAIR (substantive) | With unrestricted 𝔚, ¬SP can be produced in *any* system by a trivial "unanimous-error-first" lexicographic modification (Prop R3). The meaningful object is 𝔚^reg (X correct on non-negative problems). Prop 2.1 needs only 𝔚^reg. |
| N17.3 Lemma 3.1 | CORRECT | Both bullets and the chain induction check. |
| N17.3 "shape of a useful cancellation" | GAP | Lemma 3.1 constrains only certificates *inside* 𝔚 ((NC⁺_𝔚) failures). A world can lack SP while (NC⁺) holds on all of 𝒜 (Prop R2, lexicographic). For that mode no shape constraint is known. |
| N17.4(a) edge Bayes models selected | CORRECT | — |
| N17.4(b) exchange-rate condition | CORRECT | — |
| N17.4(c) edge model with K's ratio range | CORRECT | One unstated step (D_M meets {h_3 = 0}) is supplied in §2.4. For the facet-switching field the interval is degenerate, {1}, so (c) does not apply to it. |
| N17.4 "converse" (ρ_3 exists) | CORRECT | — |
| N17.5 Lemma 5.1 | CORRECT | Immediate from Fact 0. |
| N17.5 / §0 / §7 "must reverse a continuum of near-T comparisons" | GAP | "Continuum" needs (γ)-failure on a set of weights of positive measure, and "near T" is CONJECTURE 5.2. The no-go (N14 §6) only negates uniqueness *at every* weight. NUMERICS reproduce. A crossing search found no witnesses, so the evidence is for corner rays only. |
| N17.6 finite atoms contradict (S) | CORRECT | Finitely many closed fibres partition a connected edge. |
| N17.7 fine (NC)-violating world (single layer) | CORRECT | Every inequality re-derived. Exact cell-level LPs confirm closure for θ < 1/25 (n19py). |
| N17.7 two-layer version; answer to the IRC §EXT remark | CORRECT | Sum-closure in IRC's 𝒞 is inherited. Covers, SI pair and weakly AC pair come from G_θ. It answers the remark at the order level only, as N17 says. |
| N17.8(a) full n = 2 system | CORRECT WITH REPAIR | All claims check on I. With the non-negative block, θ = 10⁻⁷ is **too large** if the block has its μ-length p₀ ≥ 1 (and p₀ ≥ 1 for every K′): an explicit admissible pair s ∈ 𝒢_4, s′ ∈ 𝒢_5 with s + s′ ∉ 𝒜 breaks transitivity (n19py). Repair: θ < (1−θ)min_k(m_k − 3R_k)/(3(1+p₀)), or give the block a small length in world 1's coordinate. The target for (LF) should also be named. |
| N17.8(b) (NC) on 𝔚_1 with e^{Mx} | CORRECT | All three cases re-derived. Valid with the block. |
| N17.8(c) nested ⇒ (NC⁺_{𝔚_1}) | CORRECT WITH REPAIR | Nestedness is needed for {E_1(C) : C ∈ C_L}, not just for selected models. It holds in N17.8 because C_L is the path. It gives (NC⁺_𝔚), not SP. |
| N17.9 "n = 2 cannot host a useful violation" | GAP | Lemma 3.1 gives (NC⁺_𝔚) only. In SP form the claim is false for unrestricted 𝔚 (Prop R3, an n = 2 system satisfying all the axioms) and open for 𝔚^reg. |
| §7 "Equivalently, by N17.1(c): no strictly positive weak charge on 𝔚_i" ⇔ "(NC⁺) fails on 𝔚_i" | FALSE | ⇐ holds (IRC Thm NC(c)); ⇒ fails (Prop R2). |
| CONJECTURE N17.B as stated ((S) ⇒ (NC⁺_{𝔚_i})) | Insufficient | Even if true, it would not give Prop 2.1's hypothesis. The needed statement is N17.B′ (§4). |
| CONJECTURE N17.A | Open, well posed | Two (W)-worlds in N17.4's sense; no contradiction found. |
| Overall verdict "route not closed, no evidence it is open" | CORRECT | The sharp question must be restated (§4). |

---

## 1. Net assessment

N17's mathematics is sound line by line. I found no false proof step in N17.1, Lemma 3.1, N17.4, N17.6 or N17.7, nor
in the main body of N17.8.

The problems are in how the results are assembled into the reduction of the route.

1. **The quantity that matters is SP, not (NC⁺) on 𝔚.**
   - Define SP_i: some charge ν_i with ν_i ≥ 0 on 𝔚_i and CA part > 0 a.e.
   - Prop 2.1 needs SP_i at every world. A cover outside the additive class therefore needs ¬SP_i at some world.
   - ¬SP_i is *implied by* the failure of (NC⁺_{𝔚_i}). It does not imply that failure: a lexicographic world has
     (NC⁺) on all of 𝒜 and no strictly positive weak charge (Prop R2).
   - So N17.3's shape constraints (cyclic, crossing, overlapping) cover only one of two modes. N17.B as stated would not
     close the route.
2. **Alternative (ii) of N17.2 is empty** (Lemma R1).
3. **𝔚 must be restricted to regular X.** With N17's 𝔚, an error on a non-negative (unanimous) problem can be made
   lexicographically worse than every mixed-problem error. This modification preserves every axiom, (S) included. It
   destroys SP, and it does so in the n = 2 setting too (Prop R3). So ¬SP on the unrestricted 𝔚 says nothing about
   whether rankings add up.
   - Prop 2.1's proof uses (W) only against regular X. With 𝔚^reg the reduction is unchanged and the necessary
     condition becomes informative.
4. **N17.8 parameter slip.** It is harmless and easy to repair, but as stated the world-1 relation with the block is
   not transitive (explicit witness).
5. **The location claims are partly conjectural.** "Continuum" and "near T" are not established. NUMERICS support
   corner-ray localisation for the one shadow tested.

---

## 2. Claim by claim

### 2.1 N17.1

**(a) CORRECT.**
- Sum-closure: N17 realises δ = 1_B − 1_A and δ′ = 1_C − 1_B pointwise. I checked all six cases (δ ∈ {±1, 0} against
  the admissible δ′).
- The realisation of δ is irrelevant by cancellation: A ≤ B depends only on (A∖B, B∖A), and these are read off δ.
- The converse checks.
- Inherited imprecision: N9 Prop 1.1 writes strict monotonicity as "B∖A non-null ⇒ ¬(B ≤ A)", which needs A ⊆ B. The
  vector form used here ("no δ ≤ 0, δ ≠ 0 in 𝒜") is the correct statement.

**(b) CORRECT.**
- Partial sums stay in 𝒞 because positive parts are pairwise disjoint and negative parts are pairwise disjoint.
- In the money pump, the J_k are disjoint because J_k ⊆ I_{k+1}. The sum is −Σ1_{I_{k+1}∖J_k}.

**(c) CORRECT.**
- The minimax and Tychonoff argument of IRC Thm NC(a) uses nothing about rankings.
- Strict positivity: ν(Q_k) ≤ ν(A), so 1 ≤ qν(A).
- (NC⁺) from (NC): the cover vectors must have yardstick S, and they are in 𝔊 ⊇ 𝔉.
- On M_U only one layer exists, so IRC's pairs, which exclude a massless layer, are not needed.

**(d) CORRECT, but note the scope.**
- For a violation of (NC) (sum ≤ −1, rational weights cleared), smallcanc gives a non-null set where two summands are
  +1. There the sum ≤ −1 needs three −1's, so m ≥ 5.
- One layer of half5 attains 5.
- For certificates with sum ≤ 0 and ≠ 0, which is what Lemma 3.1 and N17.B are about, smallcanc gives only m ≥ 4, and
  K4 attains 4 at a non-fine world. §7 item 2's "at least 5 exchanges out of selected models" should read:
  - ≥ 4 for an (NC⁺_𝔚) certificate;
  - ≥ 5 in total for a ≤ −1 certificate in 𝔚 ∪ 𝔉, of which an unknown number come from 𝔚.

### 2.2 N17.2

**Prop 2.1, CA case: CORRECT.**
- C_L: by LDG (LA), C_L is the set of coherent undominated models, and (S) maps into C_L. So selected models are in
  C_L and their comparisons lie in 𝔚.
- (α):
  - Lemma IC puts 1_{E_iX} − 1_{E_iT} in 𝔚_i for some i.
  - Lyapunov applies, since ν_i is finite.
  - Separation against the open orthant gives π ∈ Δ.
  - Interiority: if π_3 = 0, silencing T on T ∩ {h_1 < 0, h_2 < 0} lowers ψ_1 and ψ_2 strictly. At a vertex T = P_i,
    which is false.
- (β): the tie sets are hyperplane sections of Δ, and Fubini applies. Fact 0(a) and (W) on 𝔚 make C t-Bayes, so C = B_t.
- (γ): trivial.
- Not stated but immediate: at **every** t, any pointwise minimiser B is weakly dominated by a selected C, and (W) makes
  C a coherent t-Bayes model. This is the "coherent Bayes models at every weight" that the summary quotes.

**General charges: CORRECT WITH REPAIR.**
- I checked N11 Lemma 3.1 and Cor 3.2(d), the source of (α). The only comparison used is T ⪯_i X_m, with X_m a splice;
  that lies in 𝔚.
- N13 Prop B(β) uses C_m ⪯_i X_m with C_m selected, which is also in 𝔚.
- So "(W) only on 𝔚" is right.
- The conclusion "a.e.-unique and **selected**" holds only for CA ν. With pure parts, Prop B gives a coherent limit
  C_∞ of selected models, which need not be in C_L (N13 Prop B, Reading). The summary bullet should say "coherent".

**"Equivalently, by N17.1(c), (NC_{𝔚_i ∪ 𝔉_i})": CORRECT WITH REPAIR.**
- N17.1(c) gives (NC_{𝔚∪𝔉}) ⇒ a charge ≥ 0 on 𝔚 ∪ 𝔉, and such a charge is strictly positive. Hence SP_i, by Lemma R1.
- The converse would need a strictly positive charge ≥ 0 on 𝔚 to be ≥ 0 on some admissible 𝔉 as well, and nothing
  gives that.
- The direction actually used in the trichotomy is ¬SP_i ⇒ (NC_{𝔚_i∪𝔉_i}) fails for **every** admissible 𝔉_i. That
  direction is valid.

**Trichotomy: CORRECT WITH REPAIR.**
- Case (ii) cannot occur (Lemma R1, §3.1). The correct statement is:
  > modulo the exclusion of Prop B's class, every T1 cover has a world i with ¬SP_i. At a fine world this forces
  > (NC_{𝔚_i∪𝔉_i}) to fail for every admissible 𝔉_i, hence (NC) to fail.
- The "must" is doubly conditional, as N17 says:
  - N14 §6 needs (DD) and unique coherent Bayes models at **every** interior weight;
  - Prop 2.1/Prop B give uniqueness only at a.e. weight.
- After §3.3 the statement should use 𝔚^reg.

**The TAW/twoNC paragraph: CORRECT.** It is an accurate account of which IRC steps transfer.

### 2.3 N17.3

**Lemma 3.1: CORRECT.**
- At a point of δ_k⁺ some δ_l equals −1. That point lies in E(B_l). Necessarily B_l ≠ B_k, since δ_k⁺ ∩ E(B_k) = ∅.
- If E(B_{k₀}) contains all the other error sets, δ_{k₀}⁺ is null. Then δ_{k₀} ≤ 0 is accepted, so δ_{k₀} = 0 by
  strict (G).
- The chain induction then removes zero vectors.
- The coherent-model inclusion criterion is right (§3 Reading). Nestedness is needed for **all of C_L**; see N17.8(c).

**"Shape of a useful cancellation": GAP.**
- The lemma constrains Σλδ ≤ 0, ≠ 0 with all δ ∈ 𝔚, i.e. failures of (NC⁺_𝔚).
- A world can fail SP with (NC⁺_𝔚) intact:
  - abstractly, 𝔚 ⊇ {1_{D_k} − 1_A} with D_k disjoint and A ⊆ E(C) for a single base C. This is a chain, and any
    weak charge has ν(A) ≤ inf ν(D_k) = 0;
  - concretely at ranking level, the lexicographic world of Prop R2.
- In that mode there is no cycle and no crossing; one base suffices.
- So "a useful violation needs at least two undominated models with crossing error sets, arranged cyclically" is
  established only for the in-𝔚 cancellation mode.
- At a fine world the second mode necessarily involves cover vectors from 𝔉 in its certificate. Fineness then forces
  (NC) to fail.

### 2.4 N17.4

**(a) CORRECT.**
- The tie sets Z_s are disjoint across s, so at most countably many are non-null.
- Pointwise minimisation, Fact 0(a) and (W) at worlds 1 and 2 give C = B_s a.e.
- World 3 and (C) are not used.

**(b) CORRECT.**
- Labels:
  - R_a: adding (+,−,+) and removing (−,+,−) both carry τ = (+,−,+);
  - R_b: τ = (−,+,+).
- Choose B small first, then η, then A with ν_1(A) = (1+η)ν_1(B), by Lyapunov.
- ν_2(A) < cν_1(A) strictly because r < c on the non-null A. And ν_2(B) > cν_1(B).
- Strict (G) at world 3 excludes j = 3. (W) on 𝔚 at the base T ∈ C_L excludes j = 1, 2.
- X is regular.

**(c) CORRECT.**
- The four acceptance/rejection statements follow from κ* lying strictly inside the interval.
- μ has full support, so "open set a.e. inside T" becomes "inside cl T".
- The plane-trace computation is right: on Q₊₋, m·g > 0 ⟺ |h_2|/h_1 < m_1/m_2. The cl T trace is |h_2|/h_1 ≤ c0/(c0+ε).
- The Rockafellar step cl(C) ∩ L = cl(C ∩ L) needs D_M ∩ {h_3 = 0} ≠ ∅. That is unstated, but true:
  - if e_3 ∈ M, then D_M ⊆ {h_3 > 0}, which contradicts T ∩ (+,−,−) ⊆ cl D_M;
  - so e_3 ∉ M, and then (1,1,0) ∈ D_M by compactness.
- The edge point comes from (−1,−1,L) ∈ U for large L.
- Values: 0.4375 and 2.2857 are right.

**Remark (NUMERICS, n19py/t1_check.py (A)).** For the facet-switching field, Σ_i u_iρ_iσ_i = (1/3)min_j v_j·h. On
∂T ∩ (+,−,+) this gives ρ_2 = ρ_1 + ρ_3, i.e. r = 1 + ρ_3/ρ_1 → 1 as h_3 → 0. Measured: 1.0787, 1.0224, 1.0074,
1.0022 at h_3 = 0.1, 0.03, 0.01, 0.003. So inf_{R_a} r = 1 = sup_{R_b} r exactly. N17's 1.004 and 0.9985 are sampling
bounds. The interval of (c) is degenerate and (c) does not apply to this field. Brier converges to 0.4375, as predicted.

**Converse: CORRECT.** T is π-Bayes iff Σ_iπ_iρ_iτ_i ≤ 0 pointwise. World-3 gain points need an upper bound on ρ_3,
which is positive exactly under (b) with null ties at c*. World-3 loss points need a lower bound. Every problem carries
one label, and integrability is clear.

### 2.5 N17.5

**Lemma 5.1: CORRECT.**

**Location claims as stated in §0 and §7: GAP.**
- Lemma 5.1 needs, for the shadow ν, weights t with null ties at which B_t is incoherent.
- The additive no-go is N14 §6, conditional on (DD). It refutes "unique coherent Bayes models at **every** interior
  weight". Its negation can be met at a single weight, or at a λ-null set (Prop B's class allows exactly that).
- So "a continuum of reversals" is not implied for a general shadow. "Near T" is CONJECTURE 5.2, correctly labelled in
  §5 but stated as a "must" in §0 and §7 item 4.
- For the facet-switching shadow, N17's NUMERICS do show incoherent B_t for t in an open set near u. I re-ran them and
  they reproduce.

**Additional NUMERICS (n19py/t1_check.py (B)).**
- A targeted search near all six crossings of ∂D_T, using three directions t − u and 300 000 pairs each, found **no**
  non-convexity witnesses.
- N17 searched only near corner rays, so "all witnesses sit there" was tautological. With this search, the evidence
  supports localisation at the corner rays, not at the crossings, for this shadow.

### 2.6 N17.6: CORRECT

- The vertex step uses strict monotonicity on atoms.
- The fibres u^{-1}[C] are closed (N9 Lemma 3.1, which uses only closed sections and C undominated). They are
  pairwise disjoint and finitely many, so the connected edge lies in one fibre. But P_1 ≺_1 P_2.
- The target plays no role.

### 2.7 N17.7: CORRECT

**Single layer.** I re-derived each step:
- G_θ + G_θ: the negative part b + b′ − x − y ≤ θ(a + a′ − x − y), using θ < 1;
- W_i under G_θ-steps: δW ≤ (1+κ)μ(t⁻) − κμ(t⁺) ≤ μ(t⁺)(θ(1+κ) − κ) = 0;
- 𝒢_i + 𝒢_j ∉ 𝒞: R_{ij} has measure 0.1 − 2.4κ > 0, and C_i has 0.4 − 2.4κ > 0;
- sign conditions: W_i ≥ 0.4 > 1.2κ on non-positive vectors;
- generators: W_i(g_i) ≤ 1.2κ;
- Σg_i = −1;
- fineness: covers by A and pieces Q of U∖A with μ(Q) ≤ θμ(A).

**NUMERICS (n19py/fine_world_milp.py).**
- Inside a cell only the measures of the 7 admissible value combinations of (s,t) matter. So cell-level LPs are exact
  for the atomless problem, not discretisations.
- For θ ∈ {0.01, 0.03, 0.039, 0.0399} I found:
  - max (G+G excess) ≤ 0;
  - max W_i(s+t) − 1.2κ ≤ 0;
  - no feasible 𝒢_i + 𝒢_j pair.
- The pair exclusion survives up to θ = 0.06 and fails at θ = 0.1, so θ < 1/25 is sufficient, not sharp.

**Two layers.**
- In IRC's 𝒞, a sum of two members that lies in 𝒞 is {−1,0,1}-valued on Ω′. Single-layer closure on Ω′ then gives
  transitivity of X ⪯ Y :⇔ δ(X,Y) ∈ 𝒜′, and (IB′) holds because the relation depends only on δ.
- Debt and credit covers come from G_θ.
- SI pair: (1_Z, −1_D) ∈ G_θ iff μ(D) ≤ θμ(Z). Its reverse lies in neither G_θ nor any 𝒢_i, because C_i × {1} carries
  μ′-mass 0.2 outside D × {2}.
- Weakly AC pair: μ(Z′) ≤ θμ(D′).
- So Cor NCext(i) applies.

**On the IRC §EXT remark.** "We know no fine world with (IB) that violates (NC)" is answered at the level of the order
axioms. N17 states correctly that (S), (T1o) and (EP) are untouched.

### 2.8 N17.8

**(a) CORRECT on I.** I re-derived Claims 1–4:
- 𝒢_i + 𝒢_j at x_k needs (1−θ)(m_k − 3R_k) > 3θ;
- in (ii′), with a ≤ x* or a > x*, the bound T^θ_{x*}(δ) ≤ 0 contradicts c*_i > 0;
- closedness holds because T^θ_x(1_A − 1_{[0,a)}) is continuous in a for each x;
- competitiveness holds because λ(A ∩ [x,1]) ≥ λ(A) − x;
- C_L equals the path, ties are trivial, and (C) holds;
- min_k(m_k − 3R_k) = m_10 = 4.096·10⁻⁷, so θ = 10⁻⁷ works **without** the block.

**Repair 1: the block.**
- With the non-negative block [−p₀, 0), T_0 becomes T_{−p₀}, whose range on 𝒞 is [−(1+p₀), 1+p₀]. The pair
  inequality becomes (1−θ)(m_k − 3R_k) > 3θ(1+p₀). With θ = 10⁻⁷ this needs p₀ < 0.365.
- If the block has its μ-length relative to L ∪ R, then p₀ ≥ 1 for every K′: the non-negative quadrant carries half of
  H's mass, and L ∪ R lies in the other half. Examples: p₀ = 1.336 for K′ = [0.4, 0.6] and 3.21 for [0.2, 0.8]
  (n19py/n2_block.py).
- The failure is real, not a weakness of the proof. n19py/n2_block_witness.py gives exact step functions, checked
  exactly at every breakpoint, with θ = 10⁻⁷ and p₀ = 4/3:
  - s ∈ 𝒢_4 and s′ ∈ 𝒢_5, with min slacks 6.2·10⁻⁸ and 2.5·10⁻⁸;
  - s + s′ admissible, but not in 𝒜_band or in any 𝒢_i.
- So world 1 is not transitive.
- Repair: take θ = 10⁻⁸ (valid for p₀ ≤ 3; the LP confirms no feasible pair), or give the block a small length in world
  1's coordinate. Only null sets matter for (G), so world 1's measure need not be μ, and the Remark's proofs use the
  block only through θ-terms.
- With the repaired θ, Claims 1–5 hold with T_{−p₀}, e*_i = (c*_i − θ(1+p₀))/(1−θ) > 0. I re-derived the Remark's
  competitiveness and undominatedness computations, including λ(B_I) ≥ a + λ(N_B).

**Repair 2: the target.** (LF) is at whichever coherent target T with cl T∖0 ⊆ U the monotone path is chosen to pass
through. This should be said.

**(b) CORRECT.** All three cases are re-derived; e*_i > 0 because 3θ < (1−θ)(m − 3R). The block only adds non-negative
terms, since δ ≥ 0 on the block for δ ∈ 𝔚.

**(c) CORRECT WITH REPAIR.** As in §2.3, nestedness is needed for {E_1(C) : C ∈ C_L}. Tied members of C_L are not
interchangeable inside a certificate: replacing B by a tied selected model changes the vector. In N17.8, C_L is the
path, so the hypothesis holds.

**Reading "n = 2 cannot host a useful violation": GAP.** Lemma 3.1 gives (NC⁺_{𝔚_1}), not SP_1. For unrestricted 𝔚 the
SP version is false (Prop R3, n = 2, all axioms). For 𝔚^reg it is open; §4 has a suggestion.

### 2.9 N17.9 and §7

- (a) CORRECT.
- (b) and §7 item 2: GAP, as in §2.3 and §2.1(d).
- (c) is heuristic and should be labelled so. The additive contradiction of N12 is a limiting argument, not a finite
  certificate, so "write the T1 certificate with disjoint supports" has no precise meaning yet.
- The sharp question as posed ("(NC⁺) fails on 𝔚_i; equivalently no strictly positive weak charge"): FALSE as an
  equivalence (Prop R2). §4 restates it.

---

## 3. New results

### 3.1 Lemma R1 (PROVED). Strict positivity forces an a.e.-positive CA part

Let ν be a bounded charge on the measurable subsets of U that vanishes on μ-null sets. Suppose ν(A) > 0 for every
non-null A. Then the CA part ν^c = ρμ of ν has ρ > 0 μ-a.e.

*Proof.*
- Yosida–Hewitt with concentration (N11 Fact 1.2, refereed in N13) gives ν = ρμ + ν^p, with ν^p ≥ 0 purely finitely
  additive and sets Z_m with μ(Z_m) → 0 and ν^p(U∖Z_m) = 0.
- If S = {ρ = 0} is non-null, choose m with μ(Z_m) < μ(S). Then S∖Z_m is non-null and
  ν(S∖Z_m) = ∫_{S∖Z_m} ρ dμ + ν^p(S∖Z_m) = 0. Contradiction. ∎

*Consequences.*
- N17.2(ii) is empty.
- "Strictly positive weak charge" and "weak charge with CA part > 0 a.e." are the same property, SP_i.
- At a fine world, (NC_{𝔚∪𝔉}) ⇒ SP_i ⇒ (NC⁺_𝔚). Neither converse is established, and the second is false in general
  (Prop R2).

### 3.2 Prop R2 (PROVED). (NC⁺) everywhere without a strictly positive weak charge

Setting:
- Partition U into non-null V and A_0.
- Let 𝒜 = {δ ∈ 𝒞 : μ(δ1_V) > 0, or μ(δ1_V) = 0 and μ(δ1_{A_0}) ≥ 0}. This is the lexicographic ranking with primary
  error measure on V and secondary on A_0.

Claims:
- (i) 𝒜 satisfies N17.1(a), so it is a ranking with strict (G) and (IB).
- (ii) (NC⁺_𝒜) holds.
- (iii) No strictly positive charge is ≥ 0 even on the subfamily {1_D − 1_A : A ⊆ A_0, D ⊆ V non-null}.

*Proof.*
- (i):
  - δ ≥ 0 is accepted.
  - δ ≤ 0, δ ≠ 0: either μ(δ1_V) < 0, or δ = 0 a.e. on V and then μ(δ1_{A_0}) < 0.
  - The lexicographic order of two linear functionals is a convex cone, hence sum-closed.
- (ii): let c = Σλ_kδ_k ≤ 0. Then μ(c1_V) ≥ 0, so μ(c1_V) = 0, so every μ(δ_k1_V) = 0 and c = 0 a.e. on V. Then every
  μ(δ_k1_{A_0}) ≥ 0, so μ(c1_{A_0}) ≥ 0, so c = 0.
- (iii): for non-null A ⊆ A_0 and pairwise disjoint non-null D_1, D_2, … ⊆ V, every 1_{D_k} − 1_A is accepted. Then
  ν(A) ≤ ν(D_k) for all k, while Σ_kν(D_k) ≤ ν(U) < ∞. So ν(A) = 0. ∎

The world is not fine. It is an order-level counterexample to the §7 equivalence, and it shows that N17.B as stated
does not deliver Prop 2.1's hypothesis. Whether a fine world in a system with (S) can have SP fail while (NC⁺_𝔚) holds
is open. By §2.3 it would need cover vectors in its certificate.

### 3.3 Prop R3 (PROVED). With unrestricted 𝔚, ¬SP is free; the reduction only needs 𝔚^reg

Call X ∈ M_U *regular* if it accepts every non-negative problem of U, and let N(X) be its set of silenced non-negative
problems. Put
𝔚^reg_i = {1_{E_iX} − 1_{E_iC} : C ∈ C_L, X regular, C ⪯_i X}.

**(a) The reduction needs only 𝔚^reg.** Suppose each world has a CA weak charge on 𝔚^reg_i whose density is > 0 a.e.
on the *mixed* problems of U. Then Prop 2.1 (α)–(γ) hold for the field
ψ_i(X) = ∫_{E_iX ∖ Nn} ρ_i dμ + μ(E_iX ∩ Nn), where Nn is the set of non-negative problems.

*Proof.*
- For non-regular X, its regularisation X′ = X ∪ N(X) has ψ(X′) ≤ ψ(X) coordinatewise. So the separation step in (α)
  needs T ⪯_i X only for regular X, where it gives ψ_i(T) ≤ ψ_i(X) through 𝔚^reg.
- Interiority uses a mixed-problem silencing.
- In (β), B_t is regular: non-negative problems are strictly accepted, since the block penalty is μ. Fact 0 gives
  comparisons into 𝔚^reg.
- The general-charge version (splices of regular models are regular) is the same. ∎

**(b) The modification.** Take any system satisfying (G), (IB), (LA), (S), (C), (E), (LF) on M_U, and a world i. Define
⪯′_i by:
- X ⪯′_i Y iff μ(N(X)) < μ(N(Y)), or μ(N(X)) = μ(N(Y)) and N(X) = N(Y) a.e. and X ⪯_i Y;
- in single-layer terms: the lexicographic order with the non-negative errors first (additively), then ≤_i applied to
  the mixed part.

Then:
- (i) ⪯′_i is a ranking with strict (G) and (IB).
- (ii) The modified system satisfies every axiom, with the same selection, the same C_L, and the same covered target.
- (iii) Under ⪯′_i, 𝔚′_i contains 1_N − 1_{E_iC} for every C ∈ C_L and every non-null N ⊆ Nn. So every weak charge
  ν′ ≥ 0 on 𝔚′_i has ν′(E_iC) = 0 for all C ∈ C_L. In particular ¬SP_i.

*Proof.*
- (i):
  - The acceptance set is {δ : μ(δ1_{Nn}) > 0, or δ = 0 on Nn and δ1_{Mx} ∈ 𝒜_i}.
  - Sum-closure: if both summands have δ = 0 on Nn, use 𝒜_i's closure. Otherwise the Nn-mass of the sum is positive.
    It is non-negative because each summand has Nn-mass ≥ 0, and > 0 because at least one summand has Nn-mass > 0.
  - Sign conditions: as in Prop R2.
- (ii):
  - Selected models are coherent, hence regular.
  - For regular X the comparisons with selected models are unchanged. For X with μ(N(X)) > 0, u_p ≺′_i X at every p.
    So every section {p : u_p ⪯′_i X} is either unchanged or all of Δ, hence closed, and competitiveness is preserved.
  - A model weakly dominating C ∈ C_L under ⪯′ is regular at world i and therefore compares as before. So C_L, ties,
    (C) and (LF) are unchanged.
- (iii): the vector is accepted because its Nn-mass is μ(N) > 0. Then ν′(E_iC) ≤ inf over disjoint N_k of ν′(N_k), and
  that infimum is 0. ∎

**(c) Example in n = 2.** Apply the modification to world 1 of the system "world 1 additive with increasing density f
on I, world 2 = λ(E_2)" along N17.8's path. The result is an n = 2 system with nested error sets that satisfies every
axiom, and world 1 has ¬SP for N17's 𝔚_1. It is additive on 𝔚^reg.

*Consequences.*
- With N17's 𝔚, the necessary condition "some world fails SP" is satisfied by trivial modifications. So it cannot by
  itself indicate rankings that genuinely fail to add up.
- The SP version of N17.B is false for unrestricted 𝔚.
- N17.2, N17.3 and N17.4 all go through verbatim for 𝔚^reg; every comparison they use is against a regular X. The
  route should be stated with 𝔚^reg and positivity on mixed problems.

---

## 4. Justified status of the "rankings that don't add up" route for T1

**What is proved** (after the repairs, under (H), and conditional on the exclusion of N13 Prop B's class — which is
itself conditional on N14 §6's (DD) and on uniqueness at every weight):

> Every T1 cover on M_U has a world i with **¬SP^reg_i**: there is no charge ν ≥ 0 on 𝔚^reg_i (comparisons from
> coherent undominated models against regular models) whose CA part is > 0 a.e. on mixed problems; by Lemma R1,
> equivalently, no such charge strictly positive on mixed problems.

At a fine world this forces (NC_{𝔚^reg∪𝔉}) to fail for every admissible 𝔉, so (NC) fails.

¬SP^reg can arise in two ways.

- **(M1) Cancellation inside 𝔚^reg**, i.e. (NC⁺_{𝔚^reg}) fails. Such a certificate:
  - uses ≥ 4 accepted exchanges out of members of C_L (≥ 5 if its sum is ≤ −1);
  - has gains overlapping on a non-null set;
  - has no member whose world-i error set contains all the others. So it is cyclic, with crossing error sets
    (N17.3, CORRECT). Crossing is generic in n = 3.
- **(M2) Non-Archimedean failure:** (NC⁺_{𝔚^reg}) holds but no strictly positive charge exists. One base model suffices
  and no cycle is needed (§2.3, Prop R2).
  - At fine worlds the certificate must use cover vectors.
  - At non-fine worlds this is the lexicographic or blind-region class. N9.5–N9.8 exclude specific designs in that
    class, not the class.

**What is known about existence.**
- At the order level, fine (NC)-violating worlds exist (N17.7).
- Exotic acceptances *outside* 𝔚 are compatible with (S) (N17.8, after the θ repair).
- Not a single system is known, for **any** target and any n, in which (M1) or (M2) occurs on 𝔚^reg together with
  (S). Prop R3 shows that occurrence on the unrestricted 𝔚 is trivial and proves nothing.
- Two additive worlds pin down the edge structure (N17.4) without contradiction. N17.A is open.
- The additive no-go is itself conditional (N14 (DD); uniqueness at every weight versus a.e.). So even the necessary
  condition above is conditional.

**Verdict.** The route is **open, neither closed nor shown viable**. It is sharply posed after restatement.
- N17's "honest bottom line" stands in spirit.
- Its sharp question and N17.B must be replaced by:

> **CONJECTURE N17.B′.** On M_U, (S) (with strict (G), (IB), (LA), (C)) forces, at every world i, a charge ≥ 0 on
> 𝔚^reg_i that is strictly positive on mixed problems.

- N17.B′ together with the Prop B-class no-go would close the route.
- N17.B as stated would not close it, because of mode (M2).

**Nearby reachable results** (suggested next steps, in increasing difficulty).
1. **N17.B′ for n = 2, nested C_L.**
   - Along a nested path E_1(u_a) = [0,a), the section S(A) = {a : [0,a) ≤_1 A} is a closed initial segment
     [0, a*(A)] with a*(A) ≥ λ(A). This follows from competitiveness, closedness and monotonicity.
   - SP^reg_1 is the existence of a strictly positive ν with ν(A) ≥ ν([0, a*(A))) for all A.
   - The natural lexicographic (M2)-world on part of I violates closedness: its section is [0, a*) without its endpoint
     (I checked one such world). This suggests a provable lemma that closed sections force the Archimedean property
     along the path.
   - It would be the first case in which (S) is shown to exclude (M2). Closed sections, not completeness, would do the
     work.
2. **N17's "easy target" test, restated with 𝔚^reg.** In an n = 3 system with a precise target, put exotic acceptances
   *inside* 𝔚^reg, in mode (M1) (cyclic and crossing) or (M2), and test (S). N17.8 tested only outside 𝔚.
3. **N17.A** (two additive worlds exclude T1). N17.4(c) supplies the edge model with K's ratio range. A contradiction
   would have to use (S) at selected models other than T (N17.4 converse), presumably via the edge sweep of N17.4(a)
   and the closed fibres of N9.2.

---

## 5. Files (`n19py/`, run with `python3 -I`)

- `fine_world_milp.py` (+ `.out`): exact cell-level LPs for N17.7. Checks G+G closure, 𝒢_i + G_θ ⊆ 𝒢_i and 𝒢_i + 𝒢_j
  infeasibility across θ, and Σg_i = −1.
- `n2_block.py` (+ `.out`): p₀ ≥ 1 for N17.8's block; the sufficient condition with the block; LP pair test at θ = 10⁻⁷
  and 10⁻⁸.
- `n2_block_witness.py` (+ `.out`): an explicit exact pair s ∈ 𝒢_4, s′ ∈ 𝒢_5 with admissible s + s′ ∉ 𝒜 at θ = 10⁻⁷,
  p₀ = 4/3, showing a transitivity failure.
- `t1_check.py` (+ `.out`): the facet-switching exchange rate tends to 1 at the crossings (degenerate interval in
  N17.4(c)); Brier tends to 0.4375; no non-convexity witnesses near the crossings of ∂D_T.
- N17's own scripts (`n17py/`) were re-run. The outputs, saved as `n19py/rerun_*.txt`, are identical to their `.out`
  files.
