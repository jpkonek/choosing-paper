# R16. Ordinal vindication ⇒ additive vindication beyond sandwiched worlds (n = 3)

13 October 2026, round 16. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof
sketched, or resting on a cited external theorem not re-proved here), **CONJECTURE**.
Setting: BRIEF.md, BRIEF2.md (with the 13 Oct update), CCIBU.tex. Repairs of R6, R8, R9, R13
are in force. Throughout: n = 3; L satisfies strict (G), (IB), (LA), (S), (C) on a decomposable domain M,
and **vindicates** T = D_K, K ⊆ int Δ, with (LF) on an open N ⊇ ∂T∖{0}. Standing facts used:
Fact 0 and R2 Lemma 1 (U_L = C_L ⊆ coherent), pointwise Bayes (PB) on decomposable domains, Aumann
convexity of attainable sets, R11 Lemma IC (T is competitive on Ω), the radial-splice
argument (R1 Lemma 1.4(ii) / R2 Lemma U), R13 Prop S, CCIBU Theorem 1 and its Remark.

## 0. Summary

1. **Theorem A (face-anchored transport; PROVED).** The reduction holds whenever there is a
   decomposable subdomain 𝔇 ⊆ M that keeps target-local freedom at T, contains every selected model
   that weakly dominates one of its members, and carries a strictly guiding additive ψ that
   represents each ⪯_i *strictly* on comparisons anchored at C_L ∩ 𝔇. Theorem W + CCIBU is the
   case 𝔇 = M. Nothing is assumed about the boundary (CCIBU handles it).
2. **Lexicographic worlds, positive (Theorem LV; PROVED).** If T sits on an *additive face*
   of the upper levels (the upper-level profile is constant on a face exposed by strictly
   positive weights) and the upper levels are blind near ∂T, the last level vindicates T.
   This holds for any finite number of levels and for mixtures with sandwiched worlds. It
   covers the auditor's error-only system.
3. **Lexicographic worlds, the target is in the lex family (Prop P; PROVED).** In the
   SF_n-regular position (interior primary support t, π(T) ∈ relint F_t, all primaries vary)
   T is the unique lex-Bayes model at an interior **Puiseux-series** prior. This settles R11
   §5's open item "T in the lex family" there. A degree-one prior t + εμ is not enough in
   general; the infinite tail fixes every deeper level.
   At additive vertex fibres T is in the lex family **iff** the face-supports of T meet the
   normal cone of π(T) (Prop V; PROVED). So "T in the lex family" can fail there, and Theorem LV
   is then the relevant route.
4. **Lexicographic worlds: the reproduction route is blocked in the SF_n-regular case.**
   (a) Lemma NG (PROVED): the natural face fields S_i − λ_i·P are never strictly guiding where
   the face keeps freedom near ∂T. So Theorem A cannot be run on T's own face.
   (b) Prop J (PROVED): the interior Bayes family of any real additive field with unique
   interior Bayes models is continuous in measure. If dim F_t ≥ 1, the lex family is
   discontinuous at T's own support t. So no reindexing that is continuous at t reproduces it.
   (c) Prop RG (CHECKED; uses the local fundamental theorem of projective geometry and stated
   richness hypotheses): no blow-up reindexing works either. A real field whose interior
   family contains the lex family near an isolated interior tie point, or near a tie segment,
   is impossible when the lex chart lines near it are dense. **R11 §5's "interior hyperplane
   blow-up" CONJECTURE is therefore false as a reproduction statement under richness.**
   A proof of the reduction in this case must use an additive field whose interior family is
   *not* L's family near T. The constant-δ field ψ^δ = L¹ + δL² is not a candidate (§2.7).
5. **General (IB) preorders.**
   (a) A counterexample to the reduction must contain a proof that T is additively
   unvindicable on every decomposable domain with (LF). No such no-go is known for any interior
   target, so no example can currently be certified (Remark 3.1).
   (b) The M-wide form of Theorem A needs an *anchored Archimedean* property (AA). (AA) is
   **not** derivable from the axioms: the auditor's error-only lex system satisfies all of them
   and violates (AA), yet the reduction holds there (Prop 3.3, PROVED). Any derivable
   structural property must therefore be *face-local*, as in Theorem A.
   (c) Complete preorders that are continuous in measure: additive by a Vind-type
   representation theorem, hence covered by Theorem W (CONJECTURE: the transfer to decomposable
   domains is unchecked).

**Net.** The reduction is now PROVED for lex/sandwiched mixtures whenever T sits on a
blind additive face (Thm LV). It is OPEN in the SF_n-regular lex case and for general (IB)
preorders. In the SF_n-regular case the lex family's own geometry rules out the
reproduction strategy (Props J, RG). No counterexample is possible without an additive no-go.

---

## 1. A general transport theorem

**Theorem A (PROVED).** Let L vindicate T as in the setting. Suppose there are a decomposable domain
𝔇 ⊆ M, an open N′ ⊆ N with N′ ⊇ ∂T∖{0}, and finite additive losses
ψ_i(X) = ∫ ψ_i(g, a_X(g)) dμ on 𝔇 (integrable envelopes), with each ψ_i strictly guiding at
world i on the advice ranges of 𝔇 a.e., such that:
- (T0) every measurable R with R △ T ⊆ N′ (a.e.) lies in 𝔇;
- (A1) if C ∈ C_L, X ∈ 𝔇 and C ⪯_i X for every i, then C ∈ 𝔇;
- (A2) for C ∈ C_L ∩ 𝔇, X ∈ 𝔇 and each i: C ⪯_i X ⇒ ψ_i(C) ≤ ψ_i(X), and
  C ≺_i X ⇒ ψ_i(C) < ψ_i(X).

Then ψ on 𝔇 satisfies strict (G), (IB), (LA), (S), (C), and vindicates T with (LF) at T
(neighbourhood N′).

*Proof.*
1. *Every interior ψ-Bayes model over 𝔇 lies in C_L.*
   - Let w ∈ int Δ and let B minimise w·ψ over 𝔇.
   - Fact 0(a) (L on M) gives a selected C ∈ C_L with C ⪯_i B for all i. By (A1), C ∈ 𝔇.
   - By (A2), ψ_i(C) ≤ ψ_i(B) for all i. Since C ∈ 𝔇 and B is w-Bayes there,
     w·ψ(C) ≥ w·ψ(B). Because w_i > 0, ψ(C) = ψ(B).
   - If C ≺_i B for some i, (A2) gives ψ_i(C) < ψ_i(B), which is impossible. Hence B ⪯_i C,
     so C ~_i B at every world.
   - (C) gives B ∈ C_L. In particular B is coherent.
2. *Uniqueness.*
   - Let B ≠ B′ be w-Bayes over 𝔇. Both are coherent, so Z = {a_B ≠ a_B′} is a non-null cone
     mod null sets.
   - The splice E = B′ on Z ∩ {|g| < 1}, B elsewhere, lies in 𝔇 (decomposable domain) and is a
     pointwise w-minimiser. By (PB) on 𝔇 it is w-Bayes, so by Step 1 it is coherent.
   - E's advice changes along a positive-measure set of rays of Z, so it is not a.e. a cone.
     Contradiction.
3. *T is ψ-Bayes at an interior weight.*
   - T ∈ C_L ∩ 𝔇 by (T0). By Lemma IC, T is competitive on Ω against M ⊇ 𝔇.
   - If X ∈ 𝔇 had ψ_i(X) < ψ_i(T) for every i, the contrapositive of (A2) (with C = T) would
     give "not T ⪯_i X" for every i. That contradicts competitiveness.
   - The attainable set {ψ(X) : X ∈ 𝔇} is convex (Aumann). Separation gives w_T ∈ Δ with T
     w_T-Bayes over 𝔇.
   - Suppose S = supp w_T ≠ Ω. Build Lemma IC's model X with its ball V ⊆ N′ (and −V ⊆ N′ if
     −g_0 ∈ ∂T). Then X △ T ⊆ N′, so X ∈ 𝔇 by (T0). X is pointwise strictly better than T at
     every world of S on a non-null set, and equal elsewhere. Strict guidance of ψ_i on the
     advice ranges of 𝔇 gives ψ_i(X) < ψ_i(T) for i ∈ S, so w_T·ψ(X) < w_T·ψ(T). Contradiction.
   - So w_T ∈ int Δ, and T is the unique w_T-Bayes model (Step 2).
4. *Closed choice.*
   - CCIBU Theorem 1 applies to ψ on the decomposable domain 𝔇: three worlds, strictly guiding,
     integrable envelopes, interior Bayes models unique and coherent (Steps 1–2). It gives
     (LA), (S), (C).
   - CCIBU's Remark (every interior Bayes model is selected) puts T in C_ψ.
   - Strict (G) and (IB) hold for strictly guiding additive losses on 𝔇.
   - (LF) at T within 𝔇 is (T0). ∎

**Remarks.**
- (i) *Instance 𝔇 = M.* (T0) and (A1) are trivial. (A2) is the condition
  - (AR) C ∈ C_L, X ∈ M: C ⪯_i X ⇒ ψ_i(C) ≤ ψ_i(X), and C ≺_i X ⇒ ψ_i(C) < ψ_i(X).

  For sandwiched worlds, R13 Prop S plus aggregation gives (AR). So Theorem A contains the
  CCIBU corollary. (AR) is also equivalent to "anchored sandwiching": families satisfying
  (W), (R) only for pairs whose smaller member lies in C_L. Prop S's separability argument
  works verbatim for anchored pairs, so countability is again automatic.
- (ii) *What Theorem A does not need.* It needs no representation of L off C_L, nothing at
  boundary weights, and no relation between ψ's interior family and L's selection beyond
  Step 1.
- (iii) *Where the strength lies.* 𝔇 may be much smaller than M, provided it keeps (T0).
  Shrinking 𝔇 is what makes lexicographic levels tractable (§2.1). (A1) is the closure
  property that replaces Lemma F.

## 2. Lexicographic worlds (with possible sandwiched worlds)

**Setting of §2.** Worlds split as Ω = Ω_ℓ ∪ Ω_s.
- A world j ∈ Ω_ℓ ranks by lex(L¹_j, …, L^m_j). The levels are additive, with integrable
  envelopes, and the composite is strictly guiding: for rank_j(a) < rank_j(b), the level
  vector of a is lexicographically below that of b, a.e. Pad with zero levels so that all lex
  worlds have m levels.
- A world i ∈ Ω_s is sandwiched (R5/R11; any cardinality, by Prop S).

For m = 2, write P = (L¹_j)_j and S = (L²_j)_j. Write φ¹, φ² for the local penalties, 𝔅_t for
the decomposable domain of pointwise t·φ¹-minimisers, F_t = π(𝔅_t), 𝒫 = π(M), and N(x) for the normal
cone of 𝒫 at x intersected with Δ.

### 2.1 Theorem LV: blind additive faces (PROVED)

**Definition.** T sits on a *blind additive face* if there are weights τ¹, …, τ^{m−1} ∈
(0,∞)^{Ω_ℓ} with the following properties. Let 𝔇 be the decomposable domain of successive pointwise
minimisers over A(g): first of τ¹·ℓ¹_{Ω_ℓ}(g,·), then of τ²·ℓ²_{Ω_ℓ}, …, then of
τ^{m−1}·ℓ^{m−1}_{Ω_ℓ}. Then:
- (F1) T ∈ 𝔇, and for k < m and j ∈ Ω_ℓ, ℓ^k_j(g,·) is a.e. constant on the advice ranges of 𝔇.
  Equivalently, the upper profile (L¹_j, …, L^{m−1}_j)_{j∈Ω_ℓ} is constant on 𝔇: if it were
  not constant on the advice ranges on a non-null set, pointwise min and max selections would give
  different integrals.
- (F2) For some open N′ ⊇ ∂T∖{0} with N′ ⊆ N, and a.e. pair meeting N′ ∪ (−N′), the upper
  levels ℓ^k_j(g,·) (k < m, j ∈ Ω_ℓ) are constant on A(g). ("Blind near ∂T.")

For m = 2, (F1) says exactly: π(T) is an exposed point of 𝒫, exposed by some τ ∈ int Δ
(restricted to Ω_ℓ), and 𝔇 = 𝔅_τ.

**Theorem LV (PROVED).** If T sits on a blind additive face, then T is vindicated with (LF) by
the additive system on 𝔇 given by
- ψ_j = L^m_j for j ∈ Ω_ℓ;
- ψ_i = Σ_k c_k L^{θ_{i,k}} for i ∈ Ω_s, aggregated over a countable dense subfamily of Θ_i
  (R13 Prop S), with c_k as in R11.

*Proof.* We check the hypotheses of Theorem A.
- **(T0).** Let R △ T ⊆ N′. Then R ∈ M by (LF). On pairs meeting N′ ∪ (−N′), every kind of advice in
  A(g) is a successive minimiser by (F2). Elsewhere R = T ∈ 𝔇. So R ∈ 𝔇.
- **(A1).** Let C ∈ C_L, X ∈ 𝔇, with C ⪯_j X at all worlds.
  - At j ∈ Ω_ℓ, lexicographic ≤ gives L¹_j(C) ≤ L¹_j(X). So τ¹·L¹(C) ≤ τ¹·L¹(X), and the
    right side is the minimum over M. Equality follows, and with τ¹ > 0, L¹_j(C) = L¹_j(X)
    for each j. So C lies in the first-stage domain (PB).
  - Lexicographic ≤ now gives L²_j(C) ≤ L²_j(X). The same argument on the first-stage domain
    puts C in the second stage with equal L²_j.
  - Iterating to stage m − 1 gives C ∈ 𝔇.
- **(A2).** Let C ∈ C_L ∩ 𝔇 and X ∈ 𝔇.
  - At j ∈ Ω_ℓ the upper profiles of C and X coincide by (F1). So C ⪯_j X ⇔ L^m_j(C) ≤ L^m_j(X),
    and strictly likewise.
  - At i ∈ Ω_s, (W) gives the weak inequality term by term. (R) for the dense subfamily, with
    positive c_k, gives the strict one.
- **Strict guidance on the advice ranges of 𝔇.**
  - j ∈ Ω_ℓ: the upper levels are constant on the advice ranges of 𝔇, so composite strictness makes
    ℓ^m_j(g,·) strictly increasing in world-j rank there.
  - i ∈ Ω_s: the aggregate is strictly guiding on the advice ranges of M, hence on those of 𝔇.
- Theorem A applies. ∎

**Examples.**
1. *The auditor's error-only system* (AUDIT_ASSESSMENT.md). Here m = 2 and every primary is
   F(X) = μ{g ∈ Q : X errs on g}, so 𝒫 = {(f,f,f)}. τ = u exposes 0, 𝔇 = 𝔅_u is "no errors on
   Q", and F is blind on mixed problems, hence near ∂T. Theorem LV recovers the known
   reduction there.
2. *Any additive or sandwiched system* (Ω_ℓ = ∅) is the case 𝔇 = M.

**Remark (multi-level faces need positive weights at every depth).** The τ^k must be
strictly positive on Ω_ℓ. Boundary weights at some depth break the equality step in (A1),
which is Lemma F(ii)'s loss of P_2. Faces exposed only by boundary weights are not covered.

### 2.2 Prop P: the target is lex-Bayes at an interior Puiseux prior (PROVED)

Let F = ℝ{{ε}} be the field of real Puiseux series. It is real closed, contains ℝ(ε) and the
formal power series ℝ[[ε]], and is ordered with ε > 0 infinitesimal.

**Prop P (PROVED, m = 2, any n).** Let X ∈ U_L, t ∈ int Δ with X ∈ 𝔅_t, and suppose X is
*multi-Lagrangian*: there are λ_1, …, λ_n ∈ ℝ^n with X minimising S_i − λ_i·P over 𝔅_t for
every i. By SF_n this holds whenever π(X) ∈ relint F_t and I_v(t) = Ω.

Then there is p = Σ_{k≥0} ε^k p_k ∈ F^n with p_0 = t and Σ_i p_{k,i} = 0 for k ≥ 1 (so p_i > 0
and Σp = 1), such that X is the a.e.-unique F-p-Bayes (lex-Bayes) model. In particular X
belongs to Prop LX's family.

*Proof.*
- **Expansion.** Λ = P + εS, so p·Λ = Σ_{k≥0} ε^k (p_k·P + p_{k−1}·S), with p_{−1} := 0.
- **Successive domains.** Let 𝔅^{(0)} = M and let 𝔅^{(k+1)} be the decomposable domain of pointwise
  minimisers of the level-k objective o_k = p_k·φ¹ + p_{k−1}·φ² over the advice ranges of 𝔅^{(k)}. We
  choose the p_k inductively so that X ∈ 𝔅^{(k)} for all k.
- **Level 0.** o_0 = t·φ¹, and X ∈ 𝔅_t = 𝔅^{(1)}.
- **Level 1.** Take p_1 = μ := −Σ_i t_i λ_i. Summing t_i(S_i − λ_i·P) shows that X minimises
  t·S + μ·P over 𝔅_t. So X ∈ 𝔅^{(2)}. On 𝔅^{(2)}, t·S + μ·P ≡ c_1 is constant.
- **Level k ≥ 2.** Given p_{k−1}, choose α_k ≥ 0 with c^{(k)} := p_{k−1} + α_k t ≥ 0. This is
  possible because t is interior.
  - On 𝔅^{(2)} ⊇ 𝔅^{(k)}: p_{k−1}·S = c^{(k)}·S − α_k t·S = c^{(k)}·S + α_k μ·P − α_k c_1.
  - Put p_k := −α_k μ − Σ_i c^{(k)}_i λ_i. Then on 𝔅^{(k)} the level-k objective equals
    Σ_i c^{(k)}_i (S_i − λ_i·P) + const.
  - X minimises each bracket over 𝔅_t, and the weights c^{(k)}_i are ≥ 0. So X minimises the
    sum over 𝔅^{(k)} ∋ X. By (PB) on 𝔅^{(k)}, X ∈ 𝔅^{(k+1)}.
- **Normalisation.** Adding βt to p_k (k ≥ 1) changes o_k by βt·φ¹, which is constant on the
  advice ranges of 𝔅_t. So Σ_i p_{k,i} = 0 can be imposed without changing any 𝔅^{(k)}.
- **X is pointwise F-optimal.** a_X(g) lies in every 𝔅^{(k)}(g). For any other b ∈ A(g),
  either b is in every 𝔅^{(k)}(g) (all coefficients tie) or there is a first k with
  b ∉ 𝔅^{(k+1)}(g); then the coefficients below ε^k agree and the ε^k coefficient is larger.
  So a_X(g) minimises p·Λ(g,·) in F.
- **Integration.** R5 Lemma 4.1 applies, since p·ℓ involves only the 2n coefficients p_i and
  εp_i. So X is F-p-Bayes.
- **Uniqueness.** Prop LX's F-prior clause gives uniqueness (its proof uses only p_i > 0 in an
  ordered field, Fact 0(a), (C) and the radial splice). ∎

**Remark.** R11 §5 stopped at the degree-one prior t + εμ, whose third level μ·S is
uncontrolled. The tail p_2, p_3, … fixes every level, using two facts: X minimises *each*
Lagrangian, and t·S is affine in P on 𝔅^{(2)}. This is why a real closed field containing
power series is used. I do not claim that a finite-degree prior suffices.

### 2.3 Prop V: vertex fibres decide membership in the lex family (PROVED)

Let m = 2. Suppose π_0 := π(T) is exposed by some t ∈ int Δ (F_t = {π_0}), and put
𝔅^0 := 𝔅_t = {X : π(X) = π_0}. This domain is the same for every exposing weight. On 𝔅^0 the
secondaries form a strictly guiding additive system (as in R7 "endpoint fibres"). Let
Σ_T = {β ∈ Δ : T minimises β·S over 𝔅^0}.

**Prop V.**
- (i) If Σ_T ∩ N(π_0) = ∅, then T is not F-p-Bayes for any real closed F ⊇ ℝ(ε) and any
  F-prior p (no positivity needed).
- (ii) If some β ∈ Σ_T ∩ int Δ exposes π_0, then T is the lex-Bayes model at the *real* prior β.

*Proof.*
- (i)
  - Comparing T with arbitrary Y ∈ M, the leading (standard) part of p·Λ(Y) − p·Λ(T) is
    st(p)·(P(Y) − P(T)). So st(p) ∈ N(π_0).
  - For Y ∈ 𝔅^0, P(Y) = P(T). So p·Λ(Y) − p·Λ(T) = ε p·(S(Y) − S(T)) ≥ 0, hence
    p·(S(Y) − S(T)) ≥ 0.
  - If st(p)·(S(Y) − S(T)) were a negative real, adding the infinitesimal η·(S(Y) − S(T))
    would keep it negative. So st(p) ∈ Σ_T.
  - Hence st(p) ∈ Σ_T ∩ N(π_0) = ∅. Contradiction.
- (ii) β ∈ N(π_0) makes T β·P-minimal. Since β exposes π_0, 𝔅_β = 𝔅^0, where T minimises β·S.
  So T is a pointwise lexicographic minimiser of (β·φ¹, β·φ²). ∎

*Reading.* T ∈ U_L only requires Σ_T ∩ int Δ ≠ ∅ (Lemma F(i): undominatedness is decided
inside 𝔅^0). So case (i) is the n = 3 form of R7 §5.6's "additive Bayes paths at vertices":
undominated members that are in no lex-Bayes family.
- If the primary is blind near ∂T, Theorem LV still gives the reduction for such T.
- If it is not blind, case (i) is OPEN.
- I have not checked whether case (i) actually occurs in an (LA),(S),(C) system with an
  interior target. A naive construction fails: an "R-restricted precise primary" makes Prop
  LX's lex-Bayes model at β incoherent (it removes an open piece from T's interior).

### 2.4 Lemma NG: face fields cannot be strictly guiding in the regular position (PROVED)

**Lemma NG.** Let T be multi-Lagrangian on 𝔅_t, with t ∈ int Δ (Prop P's hypothesis). Let
ψ_i = S_i − λ_i·P. Suppose that on a non-null set G of mixed problems the advice range of 𝔅_t contains
two kinds of advice. Then on G no choice of the λ_i makes all three ψ_i(g,·) strictly guiding.

In particular:
- If 𝔅_t keeps (LF) at T, the face 𝔅_t with these fields never satisfies Theorem A's strict
  guidance.
- If the primaries are all blind near ∂T, T cannot be multi-Lagrangian with advice ranges of 𝔅_t
  containing two kinds of advice there. So under blindness the SF_n-regular position is impossible.

*Proof.* By (PB) on 𝔅_t, T's advice minimises every ψ_i(g,·) over the advice range of 𝔅_t a.e. If every
ψ_i were strictly guiding, T's advice would be world-i-best for every i. On a mixed problem,
two distinct kinds of advice are ranked in opposite orders by some pair of worlds, so this is
impossible. ∎

### 2.5 Prop J: real families are continuous; lex families jump at T's support (PROVED)

**Prop J.**
- (a) Let ψ be any additive field on a decomposable domain with integrable envelope whose w-Bayes
  model B^ψ_w is a.e. unique for every w ∈ int Δ. Then w ↦ B^ψ_w is continuous in measure on
  int Δ.
- (b) Let m = 2, t ∈ int Δ, and suppose F_t contains two points. For each real interior p let
  B^lex_p be Prop LX's lex-Bayes model. Then there is a tangent direction θ (Σθ = 0) such that
  the profiles π(B^lex_{t+rθ}) and π(B^lex_{t−rθ}) have disjoint sets of limit points as
  r ↓ 0. So p ↦ B^lex_p has no limit in measure at t.
- (c) Consequently, there is no field ψ as in (a), on any decomposable domain, together with a map
  Φ from a neighbourhood of t in int Δ into int Δ, continuous at t, such that
  B^ψ_{Φ(p)} = B^lex_p on the two rays.

*Proof.*
- (a) Fix w_0 and g off a null set, with a unique w_0-minimiser, gap γ(g) > 0 and envelope
  H(g) < ∞. If 2|w − w_0|_1 H(g) < γ(g), the minimiser at w is the same. So B^ψ_w → B^ψ_{w_0}
  pointwise a.e., hence in measure.
- (b)
  - Let d be a direction of aff F_t, so t·d = 0. The map θ ↦ θ|_{t^⊥} from {Σθ = 0} to
    (t^⊥)* is injective (its kernel is spanned by t, and Σt = 1 ≠ 0), hence onto. So choose
    θ with θ·d ≠ 0.
  - B^lex_p minimises p·P over M. Let π_r := π(B^lex_{t+rθ}) and y ∈ F_t. Then
    (t+rθ)·π_r ≤ (t+rθ)·y and t·π_r ≥ t·y, so θ·π_r ≤ θ·y.
  - Hence every limit point of π_r lies in F_t ∩ argmin_{F_t} θ, and every limit point of
    π_{−r} lies in argmin_{F_t}(−θ).
  - These two faces of F_t are disjoint because θ is non-constant on F_t.
  - P is continuous in measure, so the two ray families cannot converge to a common model.
- (c) If they did, (a) and continuity of Φ at t would make both rays converge to B^ψ_{Φ(t)}.
  This contradicts (b). ∎

**Application.** In Prop P's regular position with dim F_t ≥ 1, t is T's own primary support.
So the lex family is discontinuous exactly at the place where T sits: T is an F-model
"inside" the jump. Hence any real field whose family contains the real lex models near t
must reindex discontinuously there (a blow-up). In n = 2 this is R2 Thm R's interval
insertion. In n = 3 it is R11 §5's "interior hyperplane blow-up".

### 2.6 Prop RG: blow-ups cannot be straightened under richness (CHECKED)

**Prop RG (CHECKED).** Let m = 2 and U ⊆ int Δ open, with singular set P* ∩ U equal to either
- (point case) {t}, where t is an isolated interior tie point as in Prop J(b), or
- (segment case) ℓ ∩ U, a segment of a line ℓ across which the lex family jumps on a non-null
  set G_ℓ (as happens when dim F_t = 1: the normal segment of an edge of 𝒫).

Suppose:
- (R1) ψ is a strictly guiding real field with a.e.-unique interior Bayes models, and its
  interior family contains B^lex_p for every p ∈ U∖P*;
- (R2) w ↦ B^ψ_w is injective, and Φ := (B^ψ)^{-1}∘B^lex maps U∖P* into a compact subset of
  int Δ;
- (R3) richness: the lex chart lines H_g = {p : p·Δ¹(g) = 0} (g in a co-null set, outside the
  pencil or G_ℓ) are dense in the space of lines meeting U, and the ψ chart lines are dense
  in the space of lines meeting Φ(U∖P*).

Then (R1)–(R3) are contradictory.

*Proof sketch (checked).*
1. *Φ is continuous.* B^lex is continuous on U∖P*, by the gap argument, since the primary
   minimiser is unique there. B^ψ is a continuous injection on compacta, hence an embedding
   there.
2. *Φ maps chart lines into chart lines.*
   - For a.e. g, the lex chart and Φ^{-1}(ψ chart) are open subsets of U∖P* agreeing up to a
     λ-null set (Fubini over (p, g)).
   - An open null set is empty. So A ∩ Φ^{-1}(L_g^−) = ∅, where A is the lex chart and L_g^−
     the opposite open half-plane of ψ, and symmetrically.
   - A point of H_g mapped into the open ψ half-plane would have a neighbourhood meeting the
     opposite lex half-plane. Hence Φ(H_g ∩ (U∖P*)) ⊆ L_g, a line.
   - By (R3) and continuity, Φ maps every segment in U∖P* into a line.
3. *Local projectivity.* Each connected component of U∖P* is mapped into lines by a
   continuous injection. By the local fundamental theorem of projective geometry (a map of a
   connected open subset of the plane taking segments into lines is the restriction of a
   projective transformation; see e.g. B. Shiffman, Enseign. Math. 1995; **cited, not
   re-proved here**), Φ is projective on each component.
4. *Point case.* U∖{t} is connected, so Φ is one projective map and extends continuously to
   t. This contradicts Prop J(c).
5. *Segment case.*
   - The two sides of ℓ give projective maps π_L and π_R.
   - A lex chart line H_g crossing ℓ (g ∉ G_ℓ) has a single ψ chart line L_g containing both
     π_L(H_g) and π_R(H_g). So σ := π_R^{-1}∘π_L maps a dense open set of lines to
     themselves, and σ = id.
   - Then π_L = π_R on ℓ, so the left and right limit models at each q ∈ ℓ coincide. They
     differ on G_ℓ. Contradiction. ∎

**Status and scope.**
- The argument is complete modulo the cited theorem and the hypotheses (R2), (R3). (R3) is
  genuinely needed: if all chart lines pass through a few points, projective rigidity is
  unavailable.
- n = 2 contrast: in one dimension every injective map "preserves lines" (points), which is
  why R2 Thm R's insertion works.
- **Consequence for R11 §5.** Under (R2)–(R3), R11's CONJECTURE that "the interior blow-up can
  always be done" is false as a statement about *reproducing the lex family*.
- What remains possible is a real field whose interior family differs from L's family near t
  but still passes through T. Coverage needs only that. Theorem A's Step 1 is the only known
  mechanism that makes a real family coherent, and Lemma NG blocks it on T's face.
- I have **not** verified that a full (LA),(S),(C) lex system with an interior target in the
  regular position and (R3) exists. In n = 2 the analogue (Lagrangian ramps on interior
  faces, R7 §5.6) does exist structurally. So the obstruction is to a proof *strategy*, not
  to the reduction.

### 2.7 The constant-δ field and "supporting-functional" fields

- *ψ^δ = L¹ + δL² (constant δ > 0).*
  - Strict guidance holds for some δ iff the ratio d¹/|d²| is essentially bounded below. Here
    d¹ is the primary gap and d² the opposing secondary difference, over pairs of kinds of advice where
    the primary is strict and the secondary opposes it. Otherwise ψ^δ is not strictly guiding
    for any δ.
  - When it is strictly guiding, Prop J(a) makes its family continuous. So it cannot contain
    the lex family near t in the regular position.
  - Nothing makes its Bayes models L-undominated. Fact 0's C ⪯_i B gives L¹_i(C) ≤ L¹_i(B) but
    not ψ^δ_i(C) ≤ ψ^δ_i(B), so Theorem A's Step 1 is unavailable.
  - The auditor's example is a case where ψ^δ does work: there the primary is blind off Q.
    That is an instance of Theorem LV, not a general mechanism. **No claim either way in
    general.**
- *Fields from the levels' supporting functionals* (ψ_i = S_i − λ_i·P on 𝔅_t, or the Puiseux
  objective's real shadows): not strictly guiding where they would need freedom (Lemma NG).

### 2.8 The case without interior primary ties (PROVED, with a residual)

Suppose that for every w ∈ int Δ the pointwise w·φ¹-minimiser is a.e. unique (P* ∩ int Δ = ∅).
Then:
- 𝔅_w = {B_w} is a singleton, and B_w equals Prop LX's lex-Bayes model, so it is coherent.
  It is unique, and continuous by Prop J(a).
- If T ∈ 𝔅_t for some t ∈ int Δ, then T = B_t.
- If moreover φ¹ is strictly guiding a.e., then CCIBU applies to the primary itself, and the
  primary system vindicates T on M. **The reduction holds (PROVED).**

In general φ¹ is only weakly guiding. A tie of φ¹_i between a and b at g means that the line
{w : w·(φ¹(g,a) − φ¹(g,b)) = 0} passes through e_i. (Blindness, Δ ≡ 0, is excluded here,
since it would make every w a tie point.) A strictly guiding field's tie lines avoid all
vertices. So the primary family can be reproduced by a strictly guiding field only after
modification near the vertices met by such lines. **Residual: "vertex strictification"
(OPEN).** CCIBU does not address it, because it assumes strict guidance.

### 2.9 Status for lexicographic worlds

| Position of T (m = 2 unless stated) | Status |
|---|---|
| Blind additive face, any m, mixed with sandwiched worlds | **Reduction PROVED** (Thm LV) |
| No interior primary ties, primary strictly guiding | **Reduction PROVED** (§2.8) |
| No interior primary ties, primary weakly guiding | OPEN (vertex strictification) |
| SF_n-regular (t interior, π(T) ∈ relint F_t, I_v = Ω) | T ∈ lex family PROVED (Prop P); face transport impossible (NG); lex family discontinuous at t (J); reproduction impossible under (R3) (RG, CHECKED). Reduction OPEN |
| Vertex fibre, Σ_T ∩ N(π_0) = ∅, primary not blind near ∂T | T ∉ lex family (Prop V); reduction OPEN |
| Primary support only on ∂Δ; mixed faces ∅ ≠ I_v ≠ Ω; π(T) ∈ relbd F_t; m ≥ 3 outside Thm LV | OPEN (not attempted) |

## 3. General (IB) preorders

### 3.1 What a counterexample must contain (Remark; PROVED, elementary)

The question is whether some additive system, on some decomposable domain with (LF), vindicates T. A
counterexample is therefore an ordinal L vindicating T together with a **proof that T admits
no additive vindication on any decomposable domain with target-local freedom.**
- For every target already known to be additively covered (precise targets, and the other
  positive cases recorded in BRIEF.md where they satisfy (LF) on a decomposable domain), the reduction is
  trivially true.
- None of the known additive no-gos applies to decomposable domains with target-only (LF) and
  arbitrary measurable penalties (BRIEF.md, "Negative known").

So at present no counterexample can be certified, whatever the ordinal construction. The
search for one is equivalent to the open additive problem for T (T1–T3) plus an ordinal
construction. Conversely, a positive solution of the additive problem for T makes the
reduction trivial for T.

### 3.2 The structural property that suffices: anchored representation

By Theorem A with 𝔇 = M, it suffices that every world satisfies (AR) (§1 Remark (i)): an
additive strictly guiding ψ_i that is weakly and strictly monotone on comparisons C vs X with
C ∈ C_L. By Prop S this is the same as an anchored sandwich of any cardinality. It is weaker
than R5's sandwiching, since nothing is asked of comparisons whose smaller member is outside
C_L.

**Necessary condition for (AR): anchored Archimedeanity.**
- (AA) There are no C, C′ ∈ C_L and world i with C′ ≺_i C such that C′ is a limit in measure of
  models X_s with C ≺_i X_s.

*Proof that (AR) ⇒ (AA).* ψ_i is continuous in measure (dominated convergence, finite advice ranges).
From C ≺_i X_s we get ψ_i(C) < ψ_i(X_s) → ψ_i(C′). From C′ ≺_i C we get ψ_i(C′) < ψ_i(C).
Contradiction. ∎

### 3.3 Prop 3.3: (AA) is not derivable from the axioms, and not necessary (PROVED)

Take the auditor's error-only system: world i ranks by lex(F, L_i), with L_i the penalties
(0, |g_i|, 2|g_i|, 4|g_i|) on all models. It satisfies strict (G), (IB), (LA), (S), (C),
(LF), (E) (AUDIT_ASSESSMENT.md), and C_L = {D_p : p ∈ Δ} (precise family).
- Take p ≠ p′ interior with L_1(D_{p′}) < L_1(D_p); for instance p′ closer to e_1. Then
  D_{p′} ≺_1 D_p.
- Let X_s be D_{p′} with bad advice on a subset of Q of measure s ↓ 0. Then F(X_s) = s > 0 =
  F(D_p), so D_p ≺_1 X_s, and X_s → D_{p′} in measure.
- So (AA) fails at world 1 (and likewise at every world). By §3.2, no world admits (AR).
- Yet the reduction holds: L_i itself, and Theorem LV, vindicate every target L does.

**Consequences.**
1. No M-wide anchored-Archimedean or "local exchange rate" property follows from (G), (IB),
   (LA), (S), (C). Closedness of (S)-sections in the index p does not give any closedness of
   ⪯_i in M × M.
2. The property that should be sought must be **face-local**: Archimedean behaviour on a
   decomposable subdomain 𝔇 that keeps (T0) and (A1). That is exactly the shape of Theorem A.
3. In §2's terms, for lex worlds the non-Archimedean jumps live in the upper levels.
   Theorem LV succeeds when T's face kills them without destroying target-local freedom.
   §2.4–2.6 show that in the regular position no face does both.

### 3.4 Candidate face-local properties (CONJECTURES)

- **Conjecture C (complete Archimedean worlds).** If ⪯_i is complete, satisfies (IB) and strict
  (G), and is closed in M × M under convergence in measure, then ⪯_i is represented by a
  strictly guiding additive loss on M. This is expected from Vind-type theorems on independent
  continuous preferences over measurable functions on atomless spaces (K. Vind, J. Math. Econ.
  1991). Their transfer to decomposable domains with finite advice ranges and Gaussian μ is **not
  checked here**. If true, such worlds are sandwiched and Theorem W/CCIBU applies, including
  mixtures with lex worlds via Theorem LV.
- **Conjecture F (face-local Archimedean property).** For every L vindicating an interior T in
  three worlds, there are a decomposable subdomain 𝔇 satisfying (T0), (A1) and a strictly guiding
  additive ψ on 𝔇 satisfying (A2). By Theorem A this implies the reduction. By Prop 3.3 the
  restriction to a face cannot be dropped. In the lexicographic regular position (§2.4) it
  would require a 𝔇 that is *not* an upper-level face. Neither the regular-position lex case
  nor KPS/IRWAS-type complete non-Archimedean orders give any evidence on whether it holds.

## 4. Status

| Claim | Status |
|---|---|
| Thm A: face-anchored transport ⇒ additive vindication (n = 3, K ⊆ int Δ) | PROVED |
| (AR) ⇔ anchored sandwich; countability automatic | PROVED (Prop S argument) |
| Thm LV: blind additive faces (any m, mixed with sandwiched worlds) | PROVED |
| Auditor's error-only system is an instance of Thm LV | PROVED |
| Prop P: regular position ⇒ T is lex-Bayes at an interior Puiseux prior | PROVED |
| Prop V: vertex fibres; T ∈ lex family iff Σ_T meets N(π_0) (⇐ with the exposure condition) | PROVED |
| Occurrence of Prop V(i) in a full (LA),(S),(C) system with interior T | not established |
| Lemma NG: multi-Lagrangian face fields never strictly guiding where freedom remains | PROVED |
| Prop J: real interior families continuous; lex family jumps at T's support | PROVED |
| Prop RG: no blow-up reindexing reproduces the lex family under (R2)–(R3) | CHECKED (cites local FTPG) |
| R11 §5 "interior blow-up always possible" (as reproduction) | FALSE under (R2)–(R3), modulo RG |
| §2.8: no interior primary ties + strictly guiding primary ⇒ reduction | PROVED |
| Vertex strictification for weakly guiding primaries | OPEN |
| Reduction in the regular lex position | OPEN |
| Counterexample requires an additive no-go for T on all decomposable domains | PROVED (elementary) |
| (AR) ⇒ (AA); (AA) fails in an axiom-satisfying system where the reduction holds | PROVED |
| Conjecture C (complete continuous (IB) ⇒ additive) | CONJECTURE |
| Conjecture F (face-local Archimedean property) ⇒ reduction | implication PROVED (Thm A); property CONJECTURE |

**Suggested edits to R11.**
- §5 "Missing for lex systems: T in the lex family": now PROVED in the regular position
  (Prop P). It is false in general at vertex fibres (Prop V(i)), where Theorem LV takes over
  if the primary is blind.
- §5 (M3) CONJECTURE "the blow-up can always be done": replace by Props J and RG. The
  reproduction is impossible under richness; only non-reproducing fields remain possible.
