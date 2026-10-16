# Q3 referee report: T1 on the U-domain, exclusion side (Q3_notes.md), with Q1.7–Q1.10 and Q2 §6

15 Oct 2026, round 12. Independent, adversarial referee; I wrote none of Q1, Q2, Q3.
- **Read:** BRIEF11; termfix/TERMFIX_RULES; write-up §§2–3, §7.5–7.7 (Prop M0, Thm M0closed, Cor M0closed,
  Rem CPaU), §8.4; N17 §§1–2, 5–6; P2 §5 and P2P3_referee §§B3, B6; P4 §§5–6; P4B_referee (all); R10b Prop L
  (via the round report); Q3_notes (all) and `q3py/`; Q1_notes §§0, 1, 3, 5–7; Q2_notes §§0–3, 6–7.
- **Verdicts:** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG. New statements of my own are labelled
  PROVED / CHECKED / NUMERICS and kept apart from the verdicts (§2.4, §4.4, §8).
- **Scripts:** `q3ref_py/shadow_family.py` (output `shadow_family.out`), run with `python3 -I`. I re-ran
  `q3py/propL_shadow.py`; it reproduces. No verdict rests on numerics alone.

---

## 0. Summary

| Item | Verdict | One-line reason |
|---|---|---|
| Q3.1 locality barrier (ranking form) | **CONFIRMED** (reading repaired) | Lemma 2.1 re-derived by hand. The conclusion follows in the precise sense of §1: an exclusion must use facts about selected models at indices outside every compact Q ⊂ int Δ (or global consequences of (S) such as Fact 0). The extension to "local in model space" is heuristic, and §2.4 shows that in model space it is false for the shadow argument. |
| Q3.2 dichotomy for shadows | **CONFIRMED WITH REPAIR** | "Exactly one" must be "at least one": (b) concerns ν only, (a) the cover; both can hold. The densities must be integrable (Lyapunov, N17 Prop 2.1). |
| Q3.3 two-valued shadows ν^L | **CONFIRMED** (mathematics) | Lemma 2.1(a), (b), the threshold 1/(L+1) and η₀ = min μ(S_k) are right. Weights with min t = 1/(L+1) have non-null ties, so they are not in I_ν; no gap. |
| "N17 Conjecture 5.2 is false" | **CONFIRMED WITH REPAIR** | False in its universal reading ("for every shadow the forced incoherent B_t can be taken with t → π, B_t → T"). Its model-space half ("B_t → T") is in fact *forced* whenever some shadow endorses T1's out-comparisons (§2.4). |
| "The premise of P2.6 is not forced by any shadow argument" / §6 item 3 "load-bearing reversals near T1 are not forced" | **WRONG** | One shadow (ν^L) is not the shadow argument. A cover must meet Q3.2's disjunction for *every* shadow at once. The endorsing shadows form a cone closed under T1-favouring reweightings (Lemma R1), and such reweightings produce incoherent Bayes models arbitrarily close to T1 (Prop R2). Correct statement: Theorem R3. |
| "forced reversals at indices in a collar of ∂Δ" (§0, §6 item 3) | **CONFIRMED WITH REPAIR** (wording) | The t of Q3.3 is a *shadow weight*, not a selection index; the dominator C of Lemma 5.1 is selected at an unconstrained index. Per-world rescaling of ν^L moves the collar projectively. The invariant content: I_ν avoids a neighbourhood of the weight at which T1 is ν-Bayes. Q3.1 (selection indices) and Q3.3 (shadow weights) do not combine into one "boundary" statement. |
| Q3.4 edge complementarity | **CONFIRMED** | Re-derived. Uses only strict (G) and competitiveness on supp p ⊆ {i,j}; neither coherence nor (C). |
| Q3.5 edge reduction (N0, B0, B1, N1, DL, DR, T, E2; E3 first step) | **CONFIRMED** | Every hypothesis of P4B §§1–2, 8 is available on R_ij under (Nest_e): chain (hypothesis), complementary world (Q3.4), (K) at edge test models (competitiveness of open-edge models), closed b-sections (from (S) and continuity of β), strict (G), cancellation. PROVED label justified (E3 part CHECKED). |
| Q3.6 (a) leading charge, (b) lexicographic, (d) | **CONFIRMED** | Linking through R_ij ∩ R_ik is correct and is what makes positivity all-or-nothing. |
| Q3.6 (c) complete worlds | **CONFIRMED** (CHECKED) | One import, Savage's theorem, as in P4B §8.4. |
| Q3.7 corollary | **CONFIRMED** | Status as stated: at the status of Thm M0closed(b); CHECKED when a complete world is involved. The all-CP-a case is already Remark CPaU; the mixed and edge-nested cases are new. |
| Q3.8 far dominators ⇒ far tie partner or ¬(LC_T1) | **CONFIRMED WITH REPAIR** (wording) | Proof correct. ¬(LC_T1) is a *weaker* (more general) failure than P2.6's (γ), not a "sharpened form". The result also justifies the word "far" in P2.6(β), which P2P3_referee had found unjustified, under (LC_T1). |
| Q3.9 tie toggles | **CONFIRMED WITH REPAIR** | (a) only finite disjoint unions and relative differences ("Dynkin-type" needs (c) for countable unions). "For N17.7's world Q3.8 applies" needs (LC_T1) at **every** world, not only at the N17.7 world. |
| Q3.10 / §6 list | **CONFIRMED WITH REPAIR** | Item 3 must be replaced by Theorem R3. Items 1, 2, 4–7 stand. |
| Q1.7 | **CONFIRMED** | = Q3.4. |
| Q1.8 | **CONFIRMED** (can be labelled PROVED) | Same as Q3.5. |
| Q1.9 | **CONFIRMED** | = Q3.6(b), (c); (b) CHECKED (Savage). |
| Q1.10 | **CONFIRMED**, conditional on Q1.4 (not refereed here) | A global SP^reg_j charge endorses the world-j edge cut comparisons, which are relevant comparisons. |
| Q1 vs Q2 §6 | **Both correct, different scopes; Q2 §6 needs a repair** | §4.3 below. Q2's "breaks" concern comparisons out of *interior* selected models; Q1/Q3's transfers concern edge comparisons, and E2/E3 globalise only because a leading charge or Savage measure endorses everything. Q2's "absence of a complementary world" is false on edges. CONJECTURE Q2.E is mis-stated (wrong restriction set, missing (Nest_e)); its corrected form is PROVED under (Nest_e) (§4.3). |

**Net.** The edge machinery (Q3.4–Q3.7, Q1.7–Q1.10) is sound and is the main positive content of the round on the
exclusion side. It is conditional on (Nest_e), which I could not derive. On the coherent edge models of the form
co(K′ ∪ segment of the edge), (Nest_e) is exactly a comonotonicity condition (§4.4), the edge form of Q2.N. The
locality part is correct as mathematics but overstated in its reading. The shadow argument *does* force reversals
against incoherent models arbitrarily close to T1, unless some world's comparisons out of T1 admit no strictly
positive endorsing shadow (Theorem R3). This restores a version of P2.6's premise and redirects Q3.8–Q3.9 to it.

---

## 1. Q3.1, the locality barrier

**Lemma 2.1: CONFIRMED.** I re-derived it by hand.
- On D_{T1}, w = L on the positive coordinates and 1 on the negative ones, so t·c^L = L t(P) − t(N) ≥ (L+1)t(P) − 1.
  Off cl D_{T1} the roles swap.
- On S_k, t·c^L = (L+1)t_k − 1.
- S_k is open and nonempty: w0 = (−1, −1, κ+3) ∈ S_3, since v_1·w0 = 2c0 > 0, using c0(κ−1) = ε.
- `shadow_family.py` (1): 0 violations of (a) or (b) over 300 weights × 3·10⁵ gambles.

**Prop Q3.1: CONFIRMED.** It is R10b Prop L lifted to rankings; Q3 says so.

**What "every axiom instance at those indices" means.** The premises satisfied by (ψ^L, C_q ≡ T1 on Q) are:
- global strict (G), (IB) and (LA);
- T1 ∈ C_L (coherent and undominated), and hence Lemma IC;
- for q ∈ Q: competitiveness of C_q on Ω, relative closedness in Q of the sections {q ∈ Q : C_q ⪯_i X} (trivial for a
  constant map), and (C) for models tied with T1.

What is *not* satisfied is any statement that needs the selection off Q. That includes every use of Fact 0
(Theorem kkm), which consumes (S) on all of Δ.

**Does "any exclusion must use indices approaching ∂Δ" follow?** Yes, in this precise form. Suppose a derivation of a
contradiction uses only the premises listed above, for selection indices in a fixed compact Q ⊂ int Δ. Then ψ^L with
Q ⊆ Q_L is a model of those premises, so the derivation cannot exist.
- Because L depends on Q, the correct quantifier is: the set of selection indices that an exclusion uses is contained
  in **no** compact subset of int Δ. Boundary indices themselves (vertex models) count; the write-up's chain uses
  them (§5.2, vertex neighbourhoods).
- Global consequences of (S), such as Fact 0, count as using all indices.

**Reading paragraph: CONFIRMED WITH REPAIR.**
- The P2P3 localisation GAP "cannot be proved by local means": correct for *index*-local arguments.
- "It applies equally to arguments local in model space" is heuristic. "Local in model space" is not formalised.
  Moreover, §2.4 shows that the shadow argument does produce forced behaviour against models arbitrarily close to T1
  in measure (at shadow weights near ∂Δ). Delete the sentence or label it heuristic.

---

## 2. Q3.2, Q3.3 and their consequences

### 2.1 Q3.2: CONFIRMED WITH REPAIR

- **Repair 1.** "Exactly one of (a), (b)" should be "**at least one**". (b)'s hypothesis, "T1 is ν-Bayes at an interior
  weight", depends on ν alone; (a) depends on the cover. For ν^L, (b) holds whatever the cover is, and a cover with an
  unendorsed comparison out of T1 satisfies both. The proof shows ¬(a) ⇒ (b), which is all that is used.
- **Repair 2.** ν_i = ρ_i μ needs ρ_i ∈ L¹(μ). Lyapunov and the separation in N17 Prop 2.1(α) need finite measures.
  Bounded densities, as in ν^L, are fine.
- **Rest verified.**
  - N17 Prop 2.1(α) uses only regular X: replace X by X ∪ N₊, which is weakly better at every world.
  - Thm M0closed(a) applies to c = ρσ, which is strictly signed. Its negation gives a non-null set of interior
    weights at which the strict Bayes set is incoherent. Tonelli gives null ties off a null set.
  - Lemma 5.1 is Fact 0 plus null ties.
  - The comparisons are relevant: C is selected, and B_t is regular because c > 0 on N₊.

### 2.2 Q3.3: CONFIRMED (mathematics)

- T1 = B_u. Q_L ∩ I_{ν^L} = ∅ by Lemma 2.1(a).
- At min t = 1/(L+1) the tie set contains S_argmin, which is non-null, so those weights are not in I.
- For min t < 1/(L+1), μ(B_t △ T1) ≥ μ(S_k) ≥ η₀.

### 2.3 Consequences drawn in Q3 §3, §0 and §6

- **N17 Conjecture 5.2 "false": CONFIRMED WITH REPAIR.**
  - The universal reading is refuted by ν^L. That reading is: for the shadow at hand, the incoherent B_t can be taken
    with t → π and B_t → T in measure. The statement about N12's proof ("uses only Bayes models at q → p\*") is also
    refuted, since ν^L has (BU) on Q_L and (TP).
  - But the conjecture has two halves. The **index half** (t → π) is not forced. The **model-space half**
    (B_t → T1) **is forced** in every cover with some endorsing shadow (Prop R2 below), at weights away from π.
- **"Indices in a collar of ∂Δ": CONFIRMED WITH REPAIR.**
  - The t of Q3.2–Q3.3 is the weight of the *shadow*. The forced comparison is C ⪯_j B_t with C = C_p selected at an
    index p about which Q3.2 says nothing.
  - Rescaling worlds, ν_i := λ_iν^L_i, gives a shadow with the same Bayes models relabelled by t ↦ t⊙λ/(t·λ). Its
    T1-weight is ∝ u/λ, and its "collar" can contain any compact subset of int Δ.
  - Invariant content: I_ν avoids a neighbourhood of the weight at which T1 is ν-Bayes, and that neighbourhood
    contains the projective image of Q_L.
  - Q3.1 concerns selection indices. Q3 §6 item 1 links the two. That link is not established.
- **"The premise of P2.6 is not forced by any shadow argument"; §6 item 3 "Load-bearing reversals near T1 are not
  forced": WRONG.** See §2.4.

### 2.4 New results (PROVED): what the shadow argument forces near T1

Notation. A *shadow* is ν = (ρ_iμ), with ρ_i ∈ L¹(μ) and ρ_i > 0 a.e. For a cover (standing hypotheses (H) of Q3),
let 𝒩_i be the set of world-i shadows that endorse every comparison T1 ⪯_i X with X regular, and put 𝒩 := Π_i 𝒩_i.
So ν ∈ 𝒩 iff Q3.2(a) fails for ν.

**Lemma R1 (bathtub closure; PROVED).** If ν_i ∈ 𝒩_i, λ > 0, and f ≥ 0 is measurable and bounded on bounded sets
with f ≤ λ on E_i(T1) and f ≥ λ off E_i(T1), and fν_i is a shadow, then fν_i ∈ 𝒩_i. The same holds for arbitrary X,
not only regular X.

[Correction, 15 October 2026: the hypothesis "bounded on bounded sets" is not used in the proof, and Prop R2's normalisation step (f = max(1, 1/ρ_i) off E_iT1) violates it wherever ρ_i has no positive lower bound on bounded sets. It should be deleted; the construction needs only that fν_i is a shadow, which holds. The write-up states the lemma without it.]

*Proof.* Put A = E_iT1 and E = E_iX. Then
∫_{E∖A} f dν − ∫_{A∖E} f dν ≥ λ(ν(E∖A) − ν(A∖E)) ≥ 0. ∎

(Conversely, when the cover's out-comparisons at world i are exactly those of ψ^L, 𝒩_i is exactly this bathtub
family of ν^L_i: A must minimise ν over {E : ν^L(E) ≥ ν^L(A)}.)

**Proposition R2 (PROVED).** Assume (H) and 𝒩 ≠ ∅. For every η > 0 there are:
- ν′ ∈ 𝒩, with ν′ = fν for some ν ∈ 𝒩;
- an interior weight t with null ties at which the ν′-Bayes model B′_t is incoherent and μ(B′_t △ T1) < η.

Hence, by Lemma 5.1, there are a selected C ≠ T1 and a world j such that:
- C ⪯_k B′_t at every k;
- ν′_j(E_jC) > ν′_j(E_jB′_t);
- C ⪯_j B′_t is a relevant comparison that ν′ does not endorse, against an incoherent model within η of T1.

*Proof.* Take ν ∈ 𝒩.
1. **Normalise.** Put ρ¹_i := min(ρ_i, 1) on E_iT1 and max(ρ_i, 1) off it. This is Lemma R1 with λ = 1, so it lies in
   𝒩. Errors of T1 now weigh ≤ 1 and correct points weigh ≥ 1.
2. **Choose a cone and a weight.**
   - Fix a mixed ray w ∈ D_{T1} and a closed circular cone C_η around it with cl C_η ⊂ D_{T1}∖{0}, so narrow that
     μ(C_η) < η and every point of C_η is a midpoint of two points of D_{T1}∖C_η.
   - Pick j with w_j < 0. For interior t → e_j and a.e. g ∈ C_η, t·c¹(g) → −ρ¹_j(g) < 0. So for some interior t near
     e_j (chosen off a null set of weights, by Fubini, so that ties in C_η are null), C′ := {g ∈ C_η : t·c¹(g) < 0}
     has μ(C′) ≥ ½μ(C_η).
3. **Inflate.** Put M := 2/min_i t_i + 1. Multiply ρ¹_i by M at every point where world i is correct for T1, except
   on C_η, where the factor is 1. By Lemma R1 the result ν′ is in 𝒩, and its densities are bounded by M·max(ρ, 1),
   which is integrable.
4. **Compute B′_t.**
   - For mixed g ∈ T1∖C_η: t·c′ ≥ M min t − 1 > 0.
   - For mixed g ∈ U∖T1: t·c′ ≤ 1 − M min t < 0.
   - Non-negative g are accepted.
   - On C_η, c′ = c¹.
   So B′_t = T1∖C′ a.e., and ties are null.
5. **Incoherence.** Suppose B′_t = D_K a.e. The open set D_{T1}∖C_η lies a.e. in D_K, so it lies in
   int cl D_K = D_K. Convexity then gives D_K ⊇ D_{T1} ⊇ C′, which is non-null and disjoint from B′_t: a
   contradiction.
6. **C ≠ T1.** C ⪯_k B′_t would be an out-of-T1 comparison, and ν′ endorses those. ∎

For ν^L itself there is a fully explicit version.
- Take f_3 = 1 + ζ on S_3, where ζ is the angle to w0 divided by α₀, capped at 1. Take f_3 = 2 at the other points
  correct at world 3, and f = 1 elsewhere.
- Take t = ((1−t_3)/2, (1−t_3)/2, t_3) with t_3 = 1/(L+1) − δ.
- Then B′_t = T1 minus the cone {ζ ≤ θ(δ) − 1} ⊂ S_3, with θ(δ) = (1−t_3)/(Lt_3) ↓ 1.
- NUMERICS (`shadow_family.py` (3)): the removed set equals the predicted cone exactly; there are no additions and no
  ties; μ(B′_t△T1)/μ(U) = 1.4·10⁻³, 9·10⁻⁵, 10⁻⁵, … as δ ↓ 0; midpoint incoherence witnesses are found in every case.
- (4) runs the general recipe on the facet-switching shadow. The removed set lies inside C_η, with no other changes.
- (2): 10⁴ ν^L-endorsed out-of-T1 comparisons, and no ν′-violation.

**Theorem R3 (PROVED; replaces Q3 §6 item 3).** Assume (H). Exactly one of the following holds.
- **(i)** Some world i has 𝒩_i = ∅. Then for every shadow, Q3.2(a) holds at that world: some comparison T1 ⪯_i X out
  of T1 itself is unendorsed.
- **(ii)** 𝒩 ≠ ∅. Then for every η > 0 the cover contains a relevant comparison C ⪯_j X with C selected, C ≠ T1, X
  incoherent, μ(X △ T1) < η, and C ⪯_k X at every world k. This comparison is unendorsed by some ν′ ∈ 𝒩.

So the shadow argument always forces non-additive behaviour *at T1*: either in T1's own out-comparisons, or against
incoherent models converging to T1. What remains open is the **position of the dominators**: near T1, or far. Far
dominators are what P2.6 and Q3.8 address.

*Reading for P2.6.* In case (ii) there are incoherent X_k → T1 with selected weak dominators and unendorsed
comparisons, as P2.6 needs. Two differences remain:
- the endorsing shadow ν′_k varies with k, while P2.6's flexible/rigid template fixes one ν per world;
- the dominators may approach T1.

If they stay at distance ≥ η along a subsequence, Q3.8 applies verbatim. So the correct trichotomy for case (ii) is:
- dominators approaching T1 (near unendorsed comparisons, against a k-dependent shadow);
- a far tie partner of T1;
- ¬(LC_T1).

---

## 3. Q3.4, edge complementarity: CONFIRMED

- Toggling A := {τ^C_i = τ^C_j = −1} gives X = C △ A ∈ M_U (A ⊆ U). It has E_i(X) = E_i(C)∖A and
  E_j(X) = E_j(C)∖A, so X ≺_i C and X ≺_j C when A is non-null.
- That contradicts competitiveness on supp p ⊆ {i,j}. A vertex p = e_i is included, since competitive on {i} implies
  competitive on {i,j}.
- Off R_ij the two worlds agree on the correctness of each advice; on R_ij exactly one world is correct.
- The edge test model X^{ij}_A is regular: N₊ lies off R_ij and has h_i > 0 a.e.
- Neither (C) nor coherence is used, as Q3 claims.
- `shadow_family.py` (5): coherent models co(K′ ∪ [x,y]·edge) agree with P_1 off R_12 (0 disagreements).

---

## 4. Q3.5–Q3.6 and Q1.7–Q1.10: edge transfer

### 4.1 Q3.5: CONFIRMED

I checked each hypothesis of P4B on the edge system (≤_i, ≤_j restricted to subsets of R_ij, with selection
p ∈ e_ij).
- **Chain.** This is (Nest_e). It is a chain at world i iff at world j, since E_j = R_ij∖E_i. The countable-subchain
  union in "no missing value" is legitimate in a separable measure algebra.
- **Vertex values.** β(e_i) = 0 by competitiveness on {i} against P_i. β(e_j) = 1 by Q3.4 at e_j.
- **No missing value and continuity.**
  - The sections at X^{ij}_A, with A the essential union below t, meet e_ij exactly in {β < t}: weak (G) below,
    strict (G) above (both error sets lie in R_ij).
  - Dually, world j at A′ gives {β > t}.
  - Two disjoint nonempty closed sets cannot cover the edge.
  - {β ≤ b} and {β ≥ b} are sections, so β is continuous. Models with equal β agree on R_ij (equal measure in a
    chain), and off R_ij by Q3.4.
- **b-sections.** S_i(A) = β({p ∈ e_ij : C_p ⪯_i X^{ij}_A}) is the continuous image of a compact set. The p-section is
  β⁻¹(S_i(A)) because C_p depends on β(p) only.
- **(K).** For b ∈ (0,1), β⁻¹(b) lies in the open edge, so supp p = {i,j}. Competitiveness at X^{ij}_A gives
  c_b ≤_i A or d_b ≤_j R_ij∖A. P4B uses (K) only at test models whose E_1 ⊆ M, which here are exactly the
  X^{ij}_A.
- **The proofs.**
  - B1, N1: (K), closedness of world-j sections at X^{ij}_A, strict (G) at j (R_ij∖A ⊊ R_ij).
  - DL, DR, T: chain slabs [s,t) = c_t∖c_s are non-null for s < t (μ(c_t∖c_s) = (t−s)μ(R_ij)), and arbitrary
    measurable sets are handled by cancellation as in P4B.
  - E2: the test sets c_β∖([b,β)∖Z_m) and c₁∖c_{s/2} lie in R_ij; c₁ = R_ij = E_i(C_{e_j}).
  - N0(ii) (C_L = path) is never used. E2 needs no such fact, because a leading charge endorses everything.
- **E3 first step.** Lemma T (m = 1), completeness and compactness of [0,1] give a fine ≤_i on R_ij.

The label PROVED is justified, at the standard of P4B §8 (one reader) plus this check. E3 remains CHECKED.

### 4.2 Q3.6: CONFIRMED; (c) at CHECKED

- (a) M = ∪_{j≠i} R_ij: a mixed h has h_i ≠ 0 a.e., and some coordinate of the opposite sign. R_ij ∩ R_ik contains a
  neighbourhood of e_i − η(e_j + e_k), which lies in U because K′ ⊆ int Δ is compact. So the all-or-nothing
  propagation is valid for every n ≥ 3. For n = 2 it is E2.
- (b) The first level nonzero on M is a leading charge on M.
- (c) The pieces of the finite covers of R_ij and R_ik, made disjoint, partition M into pieces ≤_i Z. Savage (fine ⇒
  unique almost-agreeing finitely additive P) is the one import. Positivity follows from fineness, and nullity on null
  sets from strict (G).
- (d) is Q3.5(4).

### 4.3 Q1.7–Q1.10, and Q1 against Q2 §6

- **Q1.7: CONFIRMED** (= Q3.4).
- **Q1.8: CONFIRMED.** Its "Check" is exactly §4.1. It can be labelled PROVED.
- **Q1.9: CONFIRMED** (= Q3.6(b), (c)). (b) is CHECKED.
- **Q1.10: CONFIRMED, conditional on Q1.4.** I did not referee Q1.4 (outside the remit). The transfer is valid:
  - world-j cut comparisons on R_ij are relevant comparisons (C_p ∈ C_L, X^{ij}_A regular);
  - a global SP^reg_j charge endorses them and is positive on R_ij;
  - Q1.4(b) on R_ij then contradicts its positivity.

**Decision on the Q1/Q2 conflict.** They do not contradict each other.
- Q1 (and Q3) claim the following. On each edge, under (Nest_e), the full nested two-world machinery holds for edge
  comparisons. E2 and E3 then *globalise* to every n, because a leading charge or a Savage measure that is positive on
  one R_ij is positive on all of them and endorses every comparison. All of this is correct.
- Q2 §6 claims that LF, IS and MP "break" in n = 3, from "the absence of a complementary world along a cut". This is
  correct for comparisons out of **interior** selected models, whose error sets cross. It is **false on edges**:
  Q3.4 supplies the complementary world there automatically.
- On each R_ij, under (Nest_e), LF, IS and MP hold for the edge comparisons, by Q3.5 plus Q2's own proofs, which use
  only P4B's inputs. But for a general acceptance cone they do not globalise. An edge-restricted endorsing charge need
  not endorse interior comparisons.
- **Repair to Q2 §6.** Replace "What breaks, all from one cause" by "what breaks for comparisons out of interior
  selected models". Add that on edges the complementary world exists, and that the n = 2 results hold there under
  (Nest_e).
- **CONJECTURE Q2.E is mis-stated.**
  - Its restriction set, "problems on which the third world's error is unchanged along the edge", is U∖(variation
    set) ⊇ U∖R_ij. There all edge models agree, so the restriction is vacuous.
  - It also omits nestedness, which n = 2 needs too.
  - Corrected form (PROVED, from Q3.4, Q3.5 and Q2 §§2–3): under (Nest_e) on e_ij, the restriction of
    (≤_i, ≤_j, edge selection) to R_ij satisfies the hypotheses of Q2 §1. Hence LF, IS and MP hold for edge
    comparisons at both i and j.
  - The open part is the interior, as Q2 says.

### 4.4 New observation (PROVED): (Nest_e) on the edge models co(K′ ∪ [x,y])

Let n = 3 and edge e_12. For 0 ≤ x ≤ y ≤ 1 put M_{x,y} := co(K′ ∪ {(a, 1−a, 0) : a ∈ [x,y]}).

**(i)** D_{M_{x,y}} agrees with P_1 off R_12.

*Proof.*
- On {h_1, h_2 > 0} the edge points give a h_1 + (1−a) h_2 > 0, so D_M = D_{K′} = U there.
- On {h_1, h_2 < 0} the edge points give values < 0.

**(ii)** On R_12, the world-1 error set of M_{x,y} is
{h_1 > 0 > h_2 : min(P_{K′}(h), x h_1 + (1−x) h_2) ≤ 0} ∪ {h_1 < 0 < h_2 : min(P_{K′}(h), y h_1 + (1−y) h_2) > 0}.
The first part increases as x decreases, the second as y decreases, and both changes are strict on non-null sets.
Hence two such models are nested at world 1 iff (x, y) and (x′, y′) are comonotone.

NUMERICS: `shadow_family.py` (5) gives a comonotone pair nested and a crossing pair not nested (1.3·10⁴ and 1.1·10⁴
sample points in the two differences).

So on this family (Nest_e) is exactly the two-parameter comonotonicity question that Q2.N poses in n = 2 for
X_{α,β}. Edge-selected models must touch the edge (N17.4(c)'s compactness argument applies to any edge model, by
Q3.4). Whether every edge model is of this form, and whether (S) forces comonotone endpoints, is open.

---

## 5. Q3.7: CONFIRMED

- CP-a worlds have SP^reg by Theorem fullsupport (refereed once).
- Edge-nested worlds with a nonzero leading charge on M, or complete, have SP^reg by Q3.6.
- Then every world adds up (N19 Lemma R1), which is (M0), and Thm M0closed(b) applies.

Status as Q3 states:
- at the status of Thm M0closed(b), whose imports N13 Prop B and N19 Prop R3(a) have been read once;
- plus Theorem fullsupport;
- plus P4B §8 (one reader) and this report;
- CHECKED when a complete world is involved (Savage).

The all-CP-a case duplicates Remark CPaU. The mixed and edge-nested cases are new.

---

## 6. Q3.8, Q3.9

**Q3.8: CONFIRMED WITH REPAIR (wording).**
- The proof is correct: (LC_T1) ⇒ C^∞ ⪯_j T1 at every j; undominatedness then gives T1 ⪯_j C^∞; (C) gives
  C^∞ ∈ C_L; and C^∞ is coherent as a limit in measure of coherent subsets of U.
- The distance identity holds: |μ(C_k△X_k) − μ(C^∞△T1)| ≤ μ(C_k△C^∞) + μ(X_k△T1).
- **Repair.** (γ) of P2.6 is the failure of (LC_T1) with C_k ≡ C fixed. So ¬(LC_T1) is *implied by* (γ) and is
  weaker. Call it "a generalised (moving-dominator) form of (iii)", not a "sharpened form".
- The content is real: P2.6 allows (α) ∧ ¬(β) ∧ ¬(γ); Q3.8 shows that this configuration needs ¬(LC_T1) along moving
  dominators.
- Bonus: under (LC_T1) the partner in (β) is at distance ≥ η, which answers P2P3_referee §B6's wording objection.

**Q3.9: CONFIRMED WITH REPAIR.**
- (a), (b) and (c) are correct, but (a) gives only *finite* disjoint unions and relative differences. A
  Dynkin-type class (countable increasing unions) needs (c).
- I checked that the N17.7 world is L¹-closed:
  - G_θ = {μ(δ⁻) ≤ θμ(δ⁺)}, and δ_k → δ in L¹ within 𝒞 forces δ_k^± → δ^± in measure;
  - W_i is L¹-continuous.
- But "for it Q3.8 applies" needs (LC_T1) at **every** world. Reword: "if every world is closed in measure (for
  instance, of N17.7 type), far dominators force a far tie partner".
- The symbol Δ for a toggle in "{∅, Δ}" clashes with the simplex.
- The remarks on (ii) (Lyapunov splitting in additive rankings) and (iii) (Villegas) are fine at CHECKED level.
  - Villegas needs monotone continuity, given by closedness, and qualitative atomlessness, given by strict (G) on
    an atomless algebra.

---

## 7. Q3.10 (§6) and §7

- Items 1, 2, 4–7: **CONFIRMED.**
  - Item 1 must be read with selection indices (§1).
  - Item 4's (E-a)/(E-b) is the exact contrapositive of Q3.6–Q3.7.
- Item 3: **replace by Theorem R3**. Keep the first sentence of Q3.2 (with "at least one").
- §7 "Proposed shift of aim": CONFIRMED. Two nearby reachable targets are, in my view, sharper than "E2 without
  (Nest)":
  1. **(Nest_e) as comonotonicity** (§4.4). Classify coherent edge models (they touch the edge and agree with P_i off
     R_ij), then show that (S) on the edge forces comonotone endpoint data. This is the edge version of Q2.N, and it
     would remove the hypothesis from Q3.6–Q3.7 in one stroke.
  2. **Case (i) of Theorem R3.** It is a statement purely about T1's out-comparisons at one world: non-endorsable by
     any positive CA shadow. Lemma IC and Lemma R1's bathtub structure are the natural tools. Excluding (i) would
     put every T1 cover in case (ii), so that unendorsed relevant comparisons against incoherent X_k → T1 are always
     present. Q3.8 then makes far dominators cost a far tie partner or ¬(LC_T1).

---

## 8. Exact established statements (after this report)

1. (Q3.1, PROVED) For every compact Q ⊂ int Δ there is an additive strictly guiding ranking on M_U (ψ^L) in which T1
   is the a.e.-unique q-Bayes model for every q ∈ Q. Hence no contradiction follows from global (G), (IB), (LA),
   T1 ∈ C_L, and (S)/(C) facts about selected models at indices in Q. An exclusion of T1 covers must use selection
   indices not contained in any compact subset of int Δ.
2. (Q3.2, PROVED) For every shadow ν with integrable densities, at least one holds: (a) some T1 ⪯_i X (X regular) is
   not ν-endorsed; (b) T1 is ν-Bayes at an interior weight, I_ν is not Lebesgue-null, and at each t ∈ I_ν some
   selected C and world j have C ⪯_j B_t with ν_j(E_jC) > ν_j(E_jB_t).
3. (Q3.3, PROVED) For ν^L, I_ν ∩ Q_L = ∅, and every B_t with t ∈ I_ν has μ(B_t△T1) ≥ min_k μ(S_k). N17 Conj 5.2 is
   false in its universal (index) reading.
4. (Lemma R1, Prop R2, Thm R3; PROVED here) Either some world's out-of-T1 comparisons admit no endorsing shadow, or
   for every η > 0 a selected C ≠ T1 weakly dominates at every world an incoherent X with μ(X△T1) < η, through a
   comparison unendorsed by some endorsing shadow.
5. (Q3.4, PROVED) Selected models on e_ij are a.e. correct at i or at j; their error sets lie in R_ij and are
   complementary there.
6. (Q3.5, PROVED; E3 step CHECKED) Under (Nest_e) on e_ij: Lemma N0(i), (iii), B0, B1, N1, DL, DR, T and E2 hold on
   R_ij for ≤_i, ≤_j. So do LF, IS and MP (Q2), and Q1.4 (as stated in Q1).
7. (Q3.6, PROVED; (c) CHECKED) Under (Nest_e) on all edges at e_i, in any n ≥ 2: a leading charge of world i is 0 on M
   or a.e. positive on M. Lexicographic worlds with charge levels and (CHECKED) complete worlds satisfy SP^reg_i.
8. (Q3.7) No T1 cover on M_U in which every world is CP-a, or is edge-nested with a nonzero leading charge on M or
   complete. Status: that of Thm M0closed(b); CHECKED with a complete world.
9. (Q3.8, PROVED) Weak dominators C_k → C^∞ of X_k → T1 with (LC_T1) at every world give C^∞ ~ T1, C^∞ ∈ C_L, and
   μ(C^∞△T1) = lim μ(C_k△X_k).
10. (§4.4, PROVED) On edge models co(K′ ∪ [x,y]), (Nest_e) ⟺ comonotone (x,y).

Not established: (Nest_e) from (S); N17.B′ for the open class (n = 2 or edges); any statement about interior
comparisons for general acceptance cones; the position of dominators in Theorem R3(ii).

---

## 9. Files (`q3ref_py/`, run with `python3 -I`)

`shadow_family.py` (+ `shadow_family.out`):
- (1) Lemma 2.1 check;
- (2) bathtub closure spot check;
- (3) explicit ν^L reweighting: thin-cone B′_t, distances, incoherence witnesses;
- (4) the general recipe of Prop R2 on the facet-switching shadow;
- (5) edge models: agreement with P_1 off R_12, and the nestedness ⟺ comonotonicity check.
