# Q3. T1 on the U-domain, exclusion side: what a cover in the remaining case must look like

15 Oct 2026 (round 12, task Q3). Brief: BRIEF11.md. Terminology: termfix/TERMFIX_RULES.md.
Labels: **PROVED** (complete proof here, or a verbatim transfer of a cited proof whose every step is checked here),
**CHECKED** (verified; one imported theorem or a sketched step), **CONJECTURE**, **NUMERICS** (scripts in `q3py/`, run
with `python3 -I`; no proof depends on them). No assumption is added to the framework. Where a result needs an extra
hypothesis, the hypothesis is named in the statement and is not claimed to follow from the axioms.

**Standing hypotheses (H).** n = 3; T1 = (1−ε)u + εΔ, ε ∈ (0,1); K′ = u + s(T1 − u), 0 < s < 1; U = D_{K′};
M_U = measurable subsets of U. A ranking with strict (G), (IB), (LA), (S) (selection p ↦ C_p ∈ C_L, competitive on
supp p, every section A_i(X) = {p : C_p ⪯_i X} closed), (C), and T1 ∈ C_L. Notation as in the write-up §§2–3 and
N17/N19/P2: P_i = U ∩ {h_i > 0}, E_i(X) = X △ P_i, σ_i = sign h_i, 𝒜_i the acceptance set (N17.1(a)), 𝔚^reg_i the
relevant comparisons, SP^reg_i, (M0)/(M1)/(M2). M := the mixed problems of U; U = M ∪ N₊ mod null, with N₊ the
non-negative gambles of U (U contains no non-zero h ≤ 0). R_ij := {h ∈ U : h_i h_j < 0}. e_ij := the edge [e_i, e_j]
of Δ. For a model C, τ^C(h) := σ(h) if h ∈ C and −σ(h) if h ∉ C, so that toggling a set A changes world-i errors by
τ^C_i 1_A: C ⪯_i C △ A iff τ^C_i 1_A ∈ 𝒜_i.

---

## 0. Outcome

**The target was not reached.** I did not prove that no ranking covers T1 on M_U in the remaining case (some world
with ¬SP^reg). What I did:

1. I show that the task's strategy, "work locally at T1", has no input to work with. The axiom instances at indices in
   any compact subset of int Δ are jointly satisfied by an additive ranking that selects T1 at every such index (Q3.1).
   The reversals that N17.5 derives from an additive shadow can all be placed against models at a fixed positive
   measure distance from T1, at indices in an arbitrarily thin collar of ∂Δ (Q3.2, Q3.3). So N17's CONJECTURE 5.2 is
   **false**, and the premise of P2.6 (load-bearing reversals against near-T1 incoherent models) is **not forced** by
   any shadow argument.
2. The information that excludes T1 lives at indices near ∂Δ. On the **edges** of Δ the two-world machinery does
   transfer. Edge-selected models have complementary error sets on R_ij (Q3.4). Under an edge-nestedness hypothesis
   (Nest_e), which is the exact analogue of the two-world (Nest), the two-world results of P4B (strict escape, Lemma T,
   Theorem E2, Theorem E3) hold on every R_ij. Positivity then propagates from one edge to the next through
   R_ij ∩ R_ik (Q3.5, Q3.6).
   Consequence (Q3.7): no T1 cover on M_U exists in which every world is (CP-a), or is edge-nested and either has a
   leading charge nonzero on mixed problems (for instance, lexicographic with charge levels) or is complete. This is
   PROVED, except that it is CHECKED when a complete world is involved.
3. On P2.6's three alternatives: (i), discontinuity of the selection at the target fibre, is **not an independent
   escape** (Q3.8). Far dominators of near-T1 models force either a far tie partner (ii) or a failure of *lower
   closedness at T1*, a sharpened form of (iii); closed sections are not even needed for this. Alternatives (ii) and
   (iii) are **not refuted**. Their exact residual content is stated in Q3.9 and §6.

| # | Result | Status |
|---|---|---|
| Q3.1 | Locality barrier, ranking form: for every compact Q ⊂ int Δ there is an additive ranking with T1 the unique Bayes model at every q ∈ Q; every axiom instance at indices in Q holds with C_q ≡ T1 | PROVED |
| Q3.2 | For every strictly positive CA shadow ν: either some comparison out of T1 is not ν-endorsed, or the weights at which the cover must reverse ν against an incoherent ν-Bayes model form a non-null set | PROVED |
| Q3.3 | Two-valued shadows ν^L: B_t = T1 iff min t_i > 1/(L+1), and otherwise μ(B_t △ T1) ≥ η₀ > 0 with η₀ independent of L. Hence all forced reversals are against far models at indices in a collar of ∂Δ of width 1/(L+1). N17 CONJECTURE 5.2 is false | PROVED; NUMERICS |
| Q3.4 | Edge complementarity: for p ∈ e_ij, E_i(C_p) ∪ E_j(C_p) ⊆ R_ij and E_j(C_p) = R_ij ∖ E_i(C_p) | PROVED |
| Q3.5 | Edge reduction: under (Nest_e) on e_ij at world i, P4B Lemma N0, B0, B1, Cor N1, DL, DR, Lemma T, Theorem E2 hold for ≤_i on subsets of R_ij, and E3 under completeness | PROVED (E3: CHECKED) |
| Q3.6 | Three-world transfer, any n ≥ 2: with (Nest_e) at world i on every edge at e_i, a leading charge of world i on M is 0 on M or strictly positive on M; lexicographic charge-level worlds and (CHECKED) complete worlds satisfy SP^reg_i | PROVED / CHECKED |
| Q3.7 | Corollary for T1: no cover with every world (CP-a), or edge-nested and (leading charge or complete) | PROVED at the status of Thm M0closed(b); CHECKED with a complete world |
| Q3.8 | Far dominators of near-T1 models ⇒ a far tie partner, or failure of lower closedness at T1. Selection discontinuity is not an independent escape | PROVED |
| Q3.9 | Tie toggles of T1 form a Dynkin-type class of coherent toggles; N17.7's rigid world is closed in measure, so for it far dominators force a far tie partner | PROVED |
| Q3.10 | Exact list of what a T1 cover in the remaining case must have (§6) | assembled; labels per item |

**Verdict.** The remaining case is not closed. The task assumed that a cover must carry load-bearing reversals near
T1. That premise is false as a consequence of the shadow argument: the forced non-additive work can sit at the
boundary of the simplex, against models far from T1. Near the boundary, edge structure reduces three-world positivity
to two-world questions on the sets R_ij. Those questions are open: (Nest) without nestedness, and the incomplete class
without a leading charge. A T1 cover in the remaining case must therefore either have a non-nested edge family at its
failing world, or have a failing world in the open two-world class on every edge (§6).

---

## 1. Imported facts used

- Thm M0closed(a) (write-up): no strictly signed measurable field c on U whose Bayes models are coherent at a.e.
  interior weight has D_{T1} as a Bayes model at an interior weight. Integrability is not used. Proved; new parts read
  twice.
- Thm M0closed(b): no (M0) cover of T1 on M_U. Status: that of Prop M0, which imports N13 Prop B and N19 Prop R3(a),
  each read once.
- N17 Lemma 5.1 (CORRECT, N19): Fact 0 gives, for an incoherent ν-t-Bayes B_t with null ties, a selected C and a world
  j with C ⪯_j B_t and ν_j(E_jC) > ν_j(E_jB_t).
- N17 Prop 2.1(α) (CORRECT, N19, only regular X used): if a CA ν with densities > 0 a.e. endorses T1's comparisons,
  then T1 is ν-Bayes at an interior weight. It uses Lemma IC (T1 competitive on Ω), Lyapunov, separation, and a
  silencing step for interiority.
- P4B §§1–2, 8 (Lemma N0, B0, B1, Cor N1, DL, DR, Lemma T, Theorem E2 PROVED; E3 CHECKED via Savage), stated for
  n = 2 under (Nest).
- Theorem fullsupport (write-up; N22/N24): a (CP-a) world with strict (G) has a member with an a.e.-positive CA part,
  hence SP^reg.
- Coherent models are sequentially compact in measure, and limits in measure of coherent models are coherent
  (R1 Prop 3.1; CBOI lem:compact).

---

## 2. The locality barrier, ranking form (Q3.1, PROVED)

**Two-valued shadows.** For L > 2 define, for g ∈ U, w_i(g) := L if (g ∈ D_{T1} and g_i > 0) or (g ∉ D_{T1} and
g_i < 0), and w_i(g) := 1 otherwise. Put c^L_i(g) := σ_i(g) w_i(g), ν^L_i := w_i μ, ψ^L_i(X) := ν^L_i(E_iX). This is a
strictly guiding additive ranking on M_U with bounded densities in {1, L}. Its t-Bayes model is
B_t = {g ∈ U : t·c^L(g) > 0}.

**Lemma 2.1 (PROVED).** Let Q_L := {t ∈ Δ : min_i t_i > 1/(L+1)}. This is an open triangle containing u, and every
compact Q ⊂ int Δ lies in Q_L once L is large.
- (a) For t ∈ Q_L the tie set {t·c^L = 0} is null and B_t = D_{T1} a.e.
- (b) If t_k = min_i t_i < 1/(L+1), then B_t ∩ S_k = ∅, where S_k := D_{T1} ∩ {g_k > 0 > g_i, g_j} (i, j ≠ k).
  Hence μ(B_t △ T1) ≥ η₀ := min_k μ(S_k) > 0, and η₀ does not depend on L.

*Proof.*
- (a) Let g ∈ U be mixed, with positive coordinate set P and negative set N, both nonempty, and write t(P) := Σ_{i∈P} t_i.
  - If g ∈ D_{T1}, then t·c^L(g) = L t(P) − t(N) ≥ L t(P) − (1 − t(P)). This is > 0 because t(P) ≥ min t > 1/(L+1).
  - If g ∉ cl D_{T1}, then t·c^L(g) = t(P) − L t(N) < 0 by the same computation with t(N).
  - For g > 0, c^L(g) > 0, and g ∈ D_{T1}.
  - ∂D_{T1} and the coordinate planes are null.
- (b) For g ∈ S_k ⊆ D_{T1}, t·c^L(g) = L t_k − (1 − t_k) < 0. S_k is open and nonempty (it contains gambles near the
  corner ray of D_{T1} whose positive coordinate is k, e.g. r_12 for k = 3), so μ(S_k) > 0. ∎

**Proposition Q3.1 (PROVED).** For every compact Q ⊂ int Δ there are an additive, strictly guiding ranking on M_U
(ψ^L with Q ⊆ Q_L) and the constant map C_q :≡ T1 (q ∈ Q) such that, for every q ∈ Q:
- C_q is coherent, undominated and competitive on Ω = supp q;
- every section {q ∈ Q : C_q ⪯_i X} is ∅ or Q, so it is relatively closed;
- every model tied with T1 at every world equals T1 a.e.

Hence every instance of (G), (IB), (LA), of (S) at indices in Q, and of (C) for models tied with the C_q, holds.

*Proof.*
- T1 is the a.e.-unique q-Bayes model of ψ^L with q interior (Lemma 2.1(a)).
- If X were weakly better at every world and strictly better at one, then q·ψ^L(X) < q·ψ^L(T1), a contradiction. For
  the same reason, for every X some i has ψ^L_i(T1) ≤ ψ^L_i(X).
- A tie at every world means ψ^L(X) = ψ^L(T1), so X is q-Bayes and X = T1 a.e. ∎

*Reading.* Every argument that excludes T1 must use selected models at indices that leave every compact subset of
int Δ. This is R10b Prop L at the level of rankings, with a field that is constant and two-valued on cells. It applies
equally to arguments "local in model space": in this ranking every comparison among models near T1 is additive and
consistent. The localisation that P2P3_referee §B3 flags as a GAP ("a cover must avoid a straight-chart family near T1
on one facet arc") therefore cannot be proved by local means. It would have to come from boundary information.

---

## 3. Reversals: always a continuum, never necessarily near T1 (Q3.2, Q3.3)

**Proposition Q3.2 (PROVED).** Assume (H). Let ν = (ρ_i μ) with ρ_i > 0 a.e. (a "shadow"), ψ_i = ν_i ∘ E_i,
c_i = ρ_i σ_i, and B_t the ν-t-Bayes model. Then exactly one of the following holds.
- (a) Some comparison T1 ⪯_i X with X regular has ν_i(E_iT1) > ν_i(E_iX).
- (b) T1 is ν-Bayes at an interior weight. In that case the set I_ν of t ∈ int Δ with a null tie set and B_t
  incoherent is not Lebesgue-null. At every t ∈ I_ν some selected C and some world j have C ⪯_j B_t and
  ν_j(E_jC) > ν_j(E_jB_t). These are relevant comparisons, since B_t is regular.

*Proof.*
- If (a) fails, N17 Prop 2.1(α) makes T1 ν-Bayes at an interior weight.
- Then Thm M0closed(a), applied to the strictly signed field c, says that the Bayes models are not coherent at a.e.
  interior weight.
- Tie sets are null off a Lebesgue-null set of weights (Tonelli: each mixed g has a line of tie weights). So I_ν is
  not null.
- At t ∈ I_ν apply N17 Lemma 5.1. ∎

This closes N19's GAP on "continuum" (N19 §0, row N17.5): no hypothesis beyond Thm M0closed(a) is needed.

**Proposition Q3.3 (PROVED).** For every L > 2 the shadow ν^L of §2 is in case (b) of Q3.2. Every weight in I_{ν^L}
has min_i t_i ≤ 1/(L+1), and every model against which Q3.2 forces a reversal has μ(B_t △ T1) ≥ η₀.

*Proof.* T1 = B_u (Lemma 2.1(a)), and Q3.2 applies. Lemma 2.1(a) excludes Q_L from I_{ν^L}, and Lemma 2.1(b) gives
the distance bound. ∎

**Consequences.**
- N17's **CONJECTURE 5.2 is false.** That conjecture said the forced reversals can be taken against B_t with t → π,
  B_t → T1, differing from coherent models only near corner rays and crossings. For ν^L no forced reversal is against
  a model within η₀ of T1, and none is at an index in Q_L.
- The NUMERICS of N17.5 and N19 locate the incoherence of *one* shadow, the facet-switching field. They are correct
  for that shadow. The geography of reversals depends on the shadow and is not a property of the cover.
- The premise of P2.6 (Prop rigid(b) in the write-up) is a hypothesis about the cover, not a consequence of ¬SP. It
  reads: "incoherent X_k → T1 whose selected weak dominators use rigid acceptances". The intrinsic statement of
  ¬SP^reg_i is this: some non-null B ⊆ M has, for every ε > 0, relevant comparisons C_k ⪯_i X_k and λ_k > 0 with
  1_B + Σλ_k(1_{E_iX_k} − 1_{E_iC_k}) ≤ ε a.e. This follows from Theorem fullsupport's key lemma and separation in
  L^∞, as in P4 §5.5; it is PROVED there for n = 2, and the proof uses no n = 2 fact. Nothing in it says where the
  C_k and X_k lie.

**NUMERICS** (`q3py/propL_shadow.py`, output `propL_shadow.out`; ε = 0.3, s = 0.9, L = 21):
- (A) 200 weights in {min t ≥ 0.1} against 2·10⁵ gambles: B_t = D_{T1} with no disagreement.
- (B) 151 of 400 collar weights have a robust convexity failure of B_t (g, g′ ∈ B_t and g + g′ ∈ U ∖ B_t, stable
  under perturbation). All have min t_i ≤ 0.0454 ≈ 1/(L+1).
- (D) Over 3000 weights: B_t ≠ D_{T1} never occurs with min t > 1/(L+1). B_t never meets S_argmin when
  min t < 1/(L+1). The minimum observed μ(B_t △ T1)/μ(U) there is 0.037, against μ(S_k)/μ(U) ≈ 0.027.

---

## 4. Edges: the two-world machinery transfers, conditionally on edge-nestedness

### 4.1 Complementarity on edges (Q3.4, PROVED; any n)

**Lemma Q3.4.** Let C ∈ M_U be competitive on {i, j}, for instance C = C_p with p ∈ e_ij. Then, a.e., C is correct at
world i or at world j. Consequently:
- E_i(C) ∪ E_j(C) ⊆ R_ij;
- on U ∖ R_ij, C accepts h iff h_i > 0 (iff h_j > 0);
- E_j(C) = R_ij ∖ E_i(C).

*Proof.*
- Let A := {h : τ^C_i(h) = τ^C_j(h) = −1}. If A is non-null, then X := C △ A has E_i(X) = E_i(C) ∖ A and
  E_j(X) = E_j(C) ∖ A. Strict (G) gives X ≺_i C and X ≺_j C, so neither C ⪯_i X nor C ⪯_j X, which contradicts
  competitiveness.
- Off R_ij the signs of h_i and h_j agree (coordinate planes are null), so correctness at i and at j coincide there.
- On R_ij exactly one of the two worlds is correct. ∎

Coherence is not used. For every A ⊆ R_ij the **edge test model** X^{ij}_A, which agrees with P_i off R_ij and has
E_i = A on R_ij, is regular and satisfies E_i(X^{ij}_A) = A and E_j(X^{ij}_A) = R_ij ∖ A.

So on each edge the selected models form a two-world system on the measure space R_ij: worlds i and j have
complementary error sets, exactly as E₂ = M ∖ E₁ in n = 2. The write-up §8.4(c) says that "strict escape needs a
complementary world along a chain, which crossing error sets do not supply". That remark concerns interior indices. On
edges complementarity holds automatically, and what remains is the chain.

### 4.2 Edge reduction (Q3.5)

**(Nest_e) at world i on e_ij.** For the given selection, {E_i(C_p) : p ∈ e_ij} is a chain mod null.

**Proposition Q3.5 (PROVED; E3 part CHECKED).** Assume (Nest_e) at world i on e_ij. Put
β(p) := μ(E_iC_p)/μ(R_ij) for p ∈ e_ij. Then:
1. β is continuous from e_ij onto [0,1], with β(e_i) = 0 and β(e_j) = 1. The models C_p with β(p) = b agree a.e.;
   write c_b := E_i(C_p) and d_b := R_ij ∖ c_b = E_j(C_p).
2. For A ⊆ R_ij the b-sections S_i(A) = {b : c_b ≤_i A} and S_j(A′) = {b : d_b ≤_j A′} are closed.
3. **(K)** For every b ∈ (0,1) and every A ⊆ R_ij: c_b ≤_i A or d_b ≤_j R_ij ∖ A.
4. Consequently P4B Lemma B0, Lemma B1 (strict escape), Cor N1, Lemmas DL, DR, Lemma T and Theorem E2 hold verbatim
   for ≤_i, ≤_j restricted to measurable subsets of R_ij, with M replaced by R_ij and worlds (1, 2) by (i, j).
5. If ≤_i is complete, ≤_i restricted to subsets of R_ij is fine in Savage's sense (E3's first step).

*Proof.*
- **Vertex values.** C_{e_i} is competitive on {i}, so C_{e_i} ⪯_i P_i, and E_i(C_{e_i}) is null by strict (G). By
  Q3.4 at e_j, E_j(C_{e_j}) = ∅ forces E_i(C_{e_j}) = R_ij.
- **No missing value** (as in N0). Suppose t ∈ (0,1) is not a value of β.
  - Let A := ess ∪{E_i(C_p) : p ∈ e_ij, β(p) < t}, which is the union of a countable subchain; the set is nonempty
    because β(e_i) = 0. Then {p ∈ e_ij : C_p ⪯_i X^{ij}_A} =
    {β < t}. If β(p) < t, then E_i(C_p) ⊆ A. If β(p) > t, then E_i(C_p) ⊋ A with non-null difference, and strict (G)
    applies.
  - This section is closed by (S).
  - Dually, with A′ := ess ∪{d : β(p) > t} and world j, the test model with E_j = A′ gives the closed section
    {β > t}. This uses E_j = R_ij ∖ E_i (Q3.4).
  - Two disjoint nonempty closed sets would then cover the connected edge.
- **Continuity.** {β ≤ b} and {β ≥ b} are sections at chain test models, hence closed.
- **Item 2.** β is a continuous surjection of a compact space, so p-sections and b-sections correspond (N0(iii)).
- **Item 3.** Competitiveness of C_p, β(p) = b ∈ (0,1), is applied to X^{ij}_A. Every such p lies in the open edge,
  since β(e_i) = 0 and β(e_j) = 1.
- **Item 4.** Every step of P4B §§2, 8.1–8.3 uses only the following:
  - the chain c_b on the underlying space;
  - closed b-sections at worlds 1 and 2 for subsets of that space;
  - (K);
  - strict (G), cancellation and finite additivity of the charge.
  
  In particular E2 step 1 uses the test set A = c_β ∖ ([b,β) ∖ Z_m) ⊆ R_ij, step 2 uses strict escape, and step 3
  uses A = c₁ ∖ c_{s/2}. All of these are subsets of R_ij, and all of them are edge test models. N0(ii)
  (C_L = the path) is not used anywhere.
- **Item 5** is the first half of E3: Lemma T with m = 1 and completeness, followed by compactness of [0,1]. ∎

### 4.3 Three-world transfer (Q3.6)

A charge π ≥ 0 on U, bounded and vanishing on null sets, is a **leading charge of world i on M** if, for all
measurable A, B ⊆ M:

  π(B ∖ A) > π(A ∖ B) ⇒ A ≤_i B ⇒ π(B ∖ A) ≥ π(A ∖ B).

**Theorem Q3.6.** Let n ≥ 2, let K′ ⊆ int Δ be any credal set, and let a ranking on M_U have strict (G), (IB) and
(S). Fix world i and assume (Nest_e) at world i on every edge e_ij, j ≠ i.
- (a) **(PROVED)** Every leading charge π of world i on M satisfies π|_M = 0, or π has a countably additive density
  ρ > 0 a.e. on M. In the second case π endorses every comparison of world i between subsets of M, so SP^reg_i holds.
- (b) **(PROVED)** If world i is lexicographic with countably many bounded charge levels π_k ≥ 0 vanishing on null
  sets (countably additive, purely finitely additive or mixed), then SP^reg_i holds.
- (c) **(CHECKED)** If ≤_i is complete, SP^reg_i holds.
- (d) **(PROVED)** On each R_ij, strict escape and Lemma T hold for ≤_i. In particular no non-null Z ⊆ R_ij is ≤_i
  every member of a sequence of non-null sets shrinking, in the chain parameter of e_ij, to finitely many cuts.

*Proof.*
- **Relevant comparisons live on M.** A regular X and a coherent B both accept a.e. h ∈ N₊, so
  E_i(X), E_i(B) ⊆ M. By cancellation, B ⪯_i X iff E_iB ≤_i E_iX as subsets of M.
- **(a)**
  - The restriction of π to subsets of R_ij is a leading charge for ≤_i on R_ij. Q3.5(4) with Theorem E2 gives
    π|_{R_ij} = 0, or ρ > 0 a.e. on R_ij.
  - **Linking.** M = ∪_{j≠i} R_ij: a mixed h has h_i ≠ 0 a.e. and some coordinate of the opposite sign. For
    j ≠ k (both ≠ i), R_ij ∩ R_ik ⊇ U ∩ {h_i > 0, h_j < 0, h_k < 0}. This is open and nonempty, since
    (1, −η, −η, 0, …) ∈ U for small η because K′ ⊆ int Δ, so it is non-null.
  - If π|_M ≠ 0, finite additivity gives some j with π|_{R_ij} ≠ 0, hence ρ > 0 a.e. on R_ij, in particular on
    R_ij ∩ R_ik. Then π|_{R_ik} ≠ 0, so ρ > 0 a.e. on R_ik, and this holds for every k.
  - Then π(D) ≥ ∫_D ρ > 0 for non-null D ⊆ M. By the second implication, E_iB ≤_i E_iX gives π(E_iX) ≥ π(E_iB).
    Adding μ on N₊ gives a weight positive on every non-null set of U that endorses 𝔚^reg_i.
- **(b)** Strict (G) on subsets of M forces some level to be nonzero on M. The first such level is a leading charge
  on M: lower levels vanish on subsets of M. Apply (a).
- **(c)**
  - Fix a non-null Z ⊆ M. Pick j with Z′ := Z ∩ R_ij non-null. Q3.5(5) gives a finite partition of R_ij into pieces
    ≤_i Z′.
  - For k ∉ {i, j}, one of these pieces meets R_ij ∩ R_ik in a non-null set Z″, and Z″ ≤_i Z′ by monotonicity.
    Q3.5(5) on e_ik gives a finite partition of R_ik into pieces ≤_i Z″ ≤_i Z′.
  - The common refinement of these partitions partitions M into finitely many pieces ≤_i Z. So ≤_i on subsets of M is
    a complete, fine qualitative probability (de Finetti cancellation is N9.4).
  - Savage (1954 §3.3; Fishburn 1986 §3) gives a finitely additive P on the measure algebra of M that almost agrees
    with it.
  - With N pieces ≤_i Z, 1 ≤ N·P(Z), so P is strictly positive. Null sets tie with ∅, so P vanishes on them. P
    endorses every comparison.
  - The only import is Savage's theorem, whose proof is Boolean, as in P4B §8.4. Hence the label CHECKED.
- **(d)** Q3.5(4). ∎

For n = 2, Q3.6 is P4B's Theorem E2 and E3: one edge, R_12 = M. The new content for n ≥ 3 is complementarity on
edges (Q3.4) together with the linking through R_ij ∩ R_ik.

### 4.4 Corollary for T1 (Q3.7)

**Corollary Q3.7.** Assume (H). Suppose that for some selection satisfying (S), every world i is either (CP-a), or
satisfies (Nest_e) on both edges at e_i and has a leading charge nonzero on M (in particular, is lexicographic with
charge levels) or is complete. Then T1 is not covered.

Status: **PROVED** when no complete world is involved; **CHECKED** otherwise. In both cases the status is at most that
of Thm M0closed(b).

*Proof.*
- A (CP-a) world has SP^reg by Theorem fullsupport, via the endorsing charge A ↦ P(κ1_A) with κ > 0 the penalty gap.
- The other worlds have SP^reg by Q3.6.
- So every world adds up, which is (M0), and Thm M0closed(b) applies. ∎

*Reading.*
- In three worlds the "two-world evidence" of the brief now holds for T1 covers, conditionally on edge-nestedness.
  A failing world must be incomplete, not (CP-a), without a leading charge on M, and with ¬SP certificates spread out
  on every edge in the sense of Lemma T, **or** it must have a non-nested edge family.
- The second alternative is a two-world phenomenon on R_ij: it is the open case "N17.B′(2) without (Nest)". The first
  is the open class of P4B §8.5.
- Positivity for these canonical objects is all-or-nothing on M by linking. This is why edge information suffices
  for leading charges and Savage measures. For a general acceptance cone, positivity of edge comparisons would not
  globalise. That is the precise reason Q3.6 stops at these classes.
- (Nest_e) is a genuine restriction. It holds for additive edge families with null ties, which are nested threshold
  families. It can fail at exceptional edge weights where a non-null tie set is split in crossing ways. It is not
  derived here.

---

## 5. P2.6's three alternatives at T1 (Q3.8, Q3.9)

P2.6 (write-up Prop rigid(b)) is stated as follows. Incoherent X_k → T1 have selected weak dominators C_{p_k} at
measure distance ≥ η, with p_k → p̄. Then one of the following holds:
- (α) C_{p̄} ~ T1, and the selection is discontinuous at the target fibre;
- (β) some coherent C ≠ T1 is tied with T1 at every world (a far tie partner);
- (γ) some world j is non-Archimedean at T1: there is a fixed C with C ⪯_j Y_m, Y_m → T1, but not C ⪯_j T1.

**Lower closedness at T1, (LC_T1) at world j.** Whenever C_k ⪯_j X_k, C_k → C and X_k → T1 in measure, C ⪯_j T1.

**Proposition Q3.8 (PROVED).** Assume (H). Let X_k → T1 in measure, and let C_k be weak dominators of X_k at every
world. The C_k may be any coherent models; they need not be selected, and no index is used. Let C_k → C^∞ in measure,
which holds along a subsequence by compactness. If (LC_T1) holds at every world along (C_k, X_k), then:
- C^∞ ~ T1 at every world;
- C^∞ ∈ C_L;
- μ(C^∞ △ T1) = lim μ(C_k △ X_k), the limit taken along the convergent subsequence.

Hence, if the dominators stay at distance ≥ η, (β) holds with a partner at distance ≥ η. In particular, (α) without
(β) forces (LC_T1) to fail at some world.

*Proof.*
- (LC_T1) gives C^∞ ⪯_j T1 for every j.
- T1 is undominated. So for each j it is not the case that C^∞ ≺_j T1, and since C^∞ ⪯_j T1 this means T1 ⪯_j C^∞.
- So C^∞ ~ T1 at every world, and (C) gives C^∞ ∈ C_L. C^∞ is coherent as a limit of coherent models.
- The distance identity is the triangle inequality with X_k → T1. ∎

So alternative (i) of the brief, discontinuity at the target fibre, is **not an independent escape**: it requires
(β) or the failure of (LC_T1). (LC_T1) is weaker than full closedness of ⪯_j. Its failure is the precise form of
alternative (iii). The proof uses neither closed sections nor the indices.

**Lemma Q3.9 (PROVED).** Let 𝒵 := {A ⊆ U : τ^{T1}_i 1_A ∈ 𝒜_i and −τ^{T1}_i 1_A ∈ 𝒜_i for every i}, the tie toggles
of T1. Then:
- (a) 𝒵 contains ∅ and is closed under disjoint unions and under proper differences B ∖ A (A ⊆ B, both in 𝒵);
- (b) by (C), T1 △ A ∈ C_L, and in particular T1 △ A is coherent, for every A ∈ 𝒵;
- (c) if every ⪯_i is closed in measure, 𝒵 is closed in measure.

N17.7's fine (NC)-violating world 𝒜 = G_θ ∪ 𝒢_1 ∪ … ∪ 𝒢_5 is closed in measure (each defining inequality is
continuous on 𝒞 for the L¹ metric). So for it Q3.8 applies: far dominators of near-T1 models force a far tie partner.

*Proof.*
- (a) The sums τ1_A + τ1_B (disjoint) and τ1_B − τ1_A (A ⊆ B) stay in 𝒞, so sum-closure (N17.1(a)) applies to them
  and to their negatives.
- (b) T1 △ A is tied with T1 at every world.
- (c) Ties are intersections of closed relations. ∎

*Status of the alternatives.*
- (i) Reduced: not independent (Q3.8).
- (ii) **Open.** In an additive ranking, Lyapunov splits any tie toggle Δ into pieces with zero vector value, so an
  incoherent model tied with T1 exists and (C) excludes (β). For general orders, 𝒵 can be as small as {∅, Δ}: a
  rigid tie. Nothing in the axioms supplies a split. The analogue of crossing pinning (write-up Prop crosspin) would
  need pointwise ties, which a non-additive order lacks.
- (iii) **Open.** (LC_T1) is not implied by closed sections: sections are closed in the index, not in the model.
  N13 Prop A shows that Walley openness is incompatible with (S). The converse question, whether (S) forces
  lower closedness, is open. A complete world that is closed in measure is represented by a countably additive
  probability (Villegas 1964: closedness gives monotone continuity, and strict (G) on the atomless measure algebra
  gives qualitative atomlessness; CHECKED, one import). Such a world adds up. So a failure of (LC_T1) at a complete
  world falls under the write-up's Conjecture villegas.

Even if (ii) and (iii) were refuted, P2.6 would exclude only covers whose load-bearing reversals sit against near-T1
models and use rigid acceptances. By §3 such reversals are not forced, so refuting (i)–(iii) would not close the
remaining case.

---

## 6. What a T1 cover in the remaining case must have (Q3.10)

Assume (H), and that some world fails SP^reg (Cor M0closed(a): this is forced). Then:
1. **(PROVED, Q3.1)** No contradiction is available from indices in a compact subset of int Δ. The cover's
   non-additive behaviour must be detectable only through selected models at indices accumulating at ∂Δ.
2. **(PROVED, N9 Cor 3.3, Lemma IC)** T1 is competitive on Ω only. Near its fibre, the selected models are
   competitive on no edge.
3. **(PROVED, Q3.2)** For every strictly positive CA shadow ν: either some comparison out of T1 is unendorsed, or a
   non-null set of weights carries unendorsed relevant comparisons C ⪯_j B_t against incoherent ν-Bayes models.
   **(PROVED, Q3.3)** For the shadows ν^L, all of these are at measure distance ≥ η₀ from T1 and at indices with
   min t_i ≤ 1/(L+1). Load-bearing reversals near T1 are not forced.
4. **(PROVED/CHECKED, Q3.6–Q3.7)** At each failing world i, one of the following holds:
   - (E-a) some edge family at e_i is not nested at world i, for the selection used; this is a two-world phenomenon
     on R_ij;
   - (E-b) all edge families at e_i are nested at world i, and world i is incomplete, is not (CP-a), has no leading
     charge nonzero on M, and on every R_ij satisfies strict escape and Lemma T (¬SP certificates spread out, as in
     P4B §8.5).
5. **(PROVED, N17.3 / N19)** If the failure is of type (M1), its certificate uses ≥ 4 relevant comparisons with
   overlapping gains and cyclic crossing world-i error sets. Otherwise it is (M2).
6. **(PROVED, Q3.8)** Suppose some incoherent X_k → T1 have weak dominators at distance ≥ η. Then either T1 has a far
   tie partner, which is coherent, in C_L and at distance ≥ η, or some world fails lower closedness at T1. The tie
   toggles of T1 form a Dynkin-type class of coherent toggles (Q3.9).
7. **(PROVED, Q3.4)** Every selected model on e_ij is pointwise Pareto-correct for {i, j}, and its error sets at i and
   j are complementary on R_ij.

No system with these properties is known for any target. Items 4 and 6 are where an exclusion proof would have to
act. Item 4 requires two-world-type results on R_ij that are open even for n = 2.

---

## 7. What would close it, and nearby reachable results

- **Close the leading-charge and complete classes outright.** The missing step is (Nest_e). One route is to show that
  some selection satisfying (S) can be chosen edge-nested. Another is to prove E2/E3 on an edge without (Nest), which
  is the two-world question N17.B′(2) without nestedness. Either would remove the hypothesis from Q3.6 and Q3.7.
- **Globalising edge positivity for general cones.** For a world in the open class with nested edges, the edges give,
  at best, charges that endorse the edge-chain comparisons on each R_ij. Theorem E2's proof uses leading charges
  because they endorse *all* comparisons. A three-world proof for the open class needs a mechanism that transports
  interior comparisons to the edges. The candidate is the KKM weak dominators of edge-near incoherent models, which
  is where Q3.3 places the forced reversals. I could not make this work: the dominators of an edge-near model need
  not be edge models.
- **(β) for T1.** A splitting lemma for tie toggles under (S) would refute (ii): from a non-null A ∈ 𝒵, produce a
  non-null proper A′ ⊆ A in 𝒵 with T1 △ A′ incoherent. Closed fibres (N9 Lemma 3.1) and Q3.9(a) are the available
  tools. No splitting principle was found.
- **Proposed shift of aim** (in the spirit of the project, since the stated target is not reached). The nearest
  established statement is Q3.7: T1 has no ordinal cover on M_U whose worlds are coherent almost-preferences,
  lexicographic with charge levels, or complete, provided the selection is edge-nested. The next reachable step is
  the two-world statement "E2 without (Nest)". By Q3.4–Q3.6 it would lift to three worlds and to T1 at once.

---

## 8. Files (`q3py/`, run with `python3 -I`)

- `propL_shadow.py` (+ `propL_shadow.out`): the two-valued shadow ν^L (L = 21) for T1 at ε = 0.3, s = 0.9.
  - (A) B_t = D_{T1} on {min t ≥ 0.1}.
  - (B), (C) Robust incoherence witnesses, all at min t_i ≤ 1/(L+1).
  - (D) The exact threshold 1/(L+1) and the distance bound μ(B_t △ T1) ≥ μ(S_k).
