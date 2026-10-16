# R13. Referee report on R11_notes.md (single-target reduction)

12 October 2026. Independent referee. I did not write R11. I checked it against BRIEF.md, BRIEF2.md,
AUDIT_ASSESSMENT.md, R2, R5, R7, the R6/R8/R9 reports and the Consolidated Statements. Every step
was re-derived; nothing was taken on trust. Verdicts: **CORRECT**, **CORRECT WITH REPAIR** (the
statement stands once a local fix is made), **GAP** (a step is missing and not supplied here),
**FALSE** (as worded).

## 0. Verdict table

| Item | Verdict | One-line reason |
|---|---|---|
| Lemma V (per-target extraction is vacuous) | CORRECT | Direct restatement of R2 Lemma 2 (refereed). The commentary in §2 (M1) and §0 item 7 claiming it makes Ex 4.3 "irrelevant at T" overreaches (§1.1 below) |
| Lemma IC, main statement (K ⊆ int Δ) | CORRECT | Every step checked; uses only (LF), strict (G), R2 Lemma 1 |
| Lemma IC, Remark (ii) (boundary targets) | FALSE as worded | The argument shows supp a ∉ 𝒮; it does not show supp a ⊇ every S ∈ 𝒮 (T4 example below) |
| Lemma RS (restriction) | CORRECT | (G), (IB) are universal statements; Fact 0 reruns on M′; (C) via L's (C) |
| Fact 0 (imported) | CORRECT | Valid on any decomposable domain, including M′ in Lemma RS, since (LA), (S) hold there |
| Definition "countably sandwiched" | CORRECT, but **the countability is automatic** | Any R5-sandwiching family of L¹ penalties has a countable dense subfamily that still satisfies (W) and (R) (Prop S below) |
| Aggregation ψ_i = Σ c_k L^{θ_{i,k}} | CORRECT | Absolutely convergent, integrable envelope Σ c_k h_k (∫ ≤ 1), strictly increasing a.e. (countable union of null exceptions) |
| Lemma K | CORRECT | Fact 0(a) + (W) + positivity of c_k + (R) + (C) |
| Theorem W (a) | CORRECT | Lemma K + R2 Lemma U radial-splice argument |
| Theorem W (b) | CORRECT | Strictness of ψ_i at e_i; Lemma K gives a selected e_i-Bayes model; uniqueness |
| Theorem W (c) | CORRECT | Lemma K |
| Theorem W (d) | CORRECT | (W)-contrapositive + separation + IC's model X excludes boundary p_T |
| Theorem W (e) | CORRECT | Exactly the hypothesis of R1 Thm 2.2(S) (refereed); domain unchanged, so (LF) kept |
| Corollary W1 | CORRECT (wording) | "charts continuous off a null set" must be read as R1 Thm 3.2(iii), not as (H1) |
| Corollary T (implication) | CORRECT | Theorem W(a)–(d) supplies exactly the field 𝒪 quantifies over |
| Corollary T (instance list) | CORRECT WITH REPAIR | R1 Thm 4.1 is not of the form 𝒪 (prescribed family, audit point 3). The other instances need a recorded check that they use only (N1)–(N4) |
| Lemma BT | CORRECT WITH REPAIR | The approach path q_s = p + s(e_j − p) stays in the face of p, where C′ is not constrained. Approach from the interior instead (repair below). Conclusion unchanged and in fact stronger |
| §4.3 reindexing sketch (n = 3, one point) | UNVERIFIED (plausible) | Key estimates hold (checked below); the reindexing homeomorphism, (C) for inserted models and degenerate directions are not written. "CHECKED" is too strong |
| §4.3 "continuum of tie points along an edge" | Case is VACUOUS for n = 3 | Non-null boundary ties occur at only countably many points of each edge (Prop E below) |
| Lemma SF_n (Baire) | CORRECT | Every step checked. Two cosmetic fixes |
| Prop LX | CORRECT | Including the F-prior clause (R5 Lemma 4.1) |
| (M3) half-closed charts | CORRECT as a description; reproduction is CONJECTURE as labelled | |
| (R_c) and §3.4 "exact missing step" | (R_c) CORRECT as a sufficient condition; the "missing step" is **not missing** | Separability of L¹ gives a countable subfamily satisfying full (R) (Prop S) |

No silent all-model assumption was found. Every model to which (G), (IB), Bayes optimality or
(S) is applied lies in the decomposable domain: IC's X by (LF); BT's X_j and §4.3's X_v as measurable
choices within the advice ranges; Lemma K's C by Fact 0 on M. The single all-model citation, v3
thm:general for n = 2 in §6, is explicit and harmless.

Bayes uniqueness and selection uniqueness are kept apart correctly throughout (Theorem W(b) uses
the vertex lemma, not Bayes uniqueness, to identify C_{e_i}). One imprecision: the Reading after
Lemma BT cites the auditor's C_t = B_{t²} as the kind of reindexing that rescues (S). A
homeomorphic reindexing cannot help at a boundary tie. Only non-open "blow-up" reindexings can
(§3.3 below).

---

## 1. The general lemmas

### 1.1 Lemma V: CORRECT

R2 Lemma 2 builds bounded penalties, strictly increasing in rank, that depend measurably on
(sign pattern of g, a_T(g)). They are therefore defined on any decomposable domain containing T, with a
bounded (hence integrable) envelope. Nothing more is needed.

**Commentary that overreaches.** §2 (M1) says "At the target this buys nothing (Lemma V: T is
additive-Bayes anyway)", and §0 item 7 says "Ex 4.3's non-Bayes undominatedness is irrelevant at
the target itself (Lemma V)". Lemma V makes T Bayes for *some* additive loss, unrelated to L. The
reduction needs T inside a family transported from L. For lexicographic L, that family is Prop
LX's lex-Bayes family, and Ex 4.3-type undominatedness at T is exactly what would keep T out of
it. §5 concedes this ("T in the lex family ... remains CONJECTURE"). Delete "irrelevant at T" from
§0 item 7 and §2 (M1), or restrict it to the sandwiched case, where Theorem W(d) puts T in the
family by a separate argument.

### 1.2 Lemma IC: main statement CORRECT; Remark (ii) FALSE as worded

Checked step by step:
- T ∈ C_L ⊆ U_L. R2 Lemma 1 ties T to a selected C_a. Transitivity transfers competitiveness on
  S = supp a.
- g(t) = 1_S − t·1_{S^c}. Then min_K m·g(0) = min_K m(S) > 0 and min_K m·g(t) → −∞, because K is
  compact in int Δ. Continuity gives g_0 with min_K m·g_0 = 0. g_0 is mixed, hence not ≥ 0, so
  g_0 ∈ ∂T ∖ {0}.
- For K ⊆ int Δ, T is an open convex cone: the orthant part is already contained in
  {min_K m·g > 0}. So a supporting half-space at g_0 shows that V ∖ cl T contains a non-empty open
  set, which is non-null.
- −g_0 ∉ T is correctly argued. −g_0 ∈ ∂T happens only if K ⊆ g_0^⊥ (lower-dimensional K, e.g.
  T3), and that case is handled by putting −V inside N.
- X △ T ⊆ V′ ∪ (−V′ ∩ T) ⊆ N, so X ∈ M by (LF). On V′, T's advice is silence or "accept −h", both
  worse than good at every i ∈ S. Strict (G) inside M gives X ≺_i T for all i ∈ S, contradicting
  competitiveness.

No completeness, additivity or (IB) is used, as claimed.

**Remark (ii) is misstated.** Let 𝒮 = {S : K ∩ Δ_{S^c} = ∅ and K ⊄ Δ_S}. The argument needs
min_K m(S) > 0, which holds iff K ∩ Δ_{S^c} = ∅. It needs min_K m·g(t) → −∞, which holds iff
K ⊄ Δ_S. Run with S = supp a, it shows **supp a ∉ 𝒮**. It does not show supp a ⊇ ⋃𝒮.

Counterexample to the inference, T4 (K = conv{e_1, u}, n = 3):
- 𝒮 = {{1}, {1,2}, {1,3}}.
- The remark as worded would force supp a = Ω.
- The argument excludes only {1}, {1,2}, {1,3}. It leaves {2}, {3}, {2,3} open.
- For S = {2,3} the construction cannot even start: every g with g_1 < 0 has min_K m·g ≤ g_1 < 0,
  so no boundary point of T has the required sign pattern.

Replace the remark by "supp a ∉ 𝒮".

### 1.3 Lemma RS: CORRECT

- (G) and (IB) restrict.
- Sections for X ∈ M′ are sections for L.
- C_p is undominated in M′ and coherent, which gives (LA).
- Fact 0 on M′ needs only (LA) and (S) there.
- The description C_{L|M′} = {X ∈ M′ tied with some C_p} uses L's (C) to get coherence, as
  written.
- (C) for the restriction follows.

The "Use" paragraph (W_i(M′) must be coherent) is right.

### 1.4 Fact 0: CORRECT

Imported from R2 (BA lem:complete-class), refereed in R6. It is valid on any decomposable domain M under
(LA) and (S), and so on M′ in Lemma RS.

---

## 2. Theorem W

### 2.1 Definition and aggregation: CORRECT

**Envelope.** With c_k = 2^{−k}/(1 + ∫h_{i,k}):
- |c_k L^{θ_k}(X)| < 2^{−k};
- the local series Σ c_k ℓ^{θ_k}(g, a) has the integrable envelope Σ c_k h_k (∫ ≤ 1), so it
  converges a.e. and term-by-term integration is justified by dominated convergence.

**Strictness.** Each ℓ^{θ_k}(g, ·) is strictly increasing in world-i rank off a null set N_k. Off
⋃N_k (null), the positive combination is strictly increasing. So ψ_i is a strictly guiding
additive loss in the sense of §0.2 of the Consolidated Statements.

**(W) and (R).** (W) for ψ_i is immediate. (R) is not inherited by ψ_i, and it is not needed: it
is used only inside Lemma K.

### 2.2 Lemma K: CORRECT

- Fact 0(a) and (W) give ψ_i(C) ≤ ψ_i(B) for every i, so C is p-Bayes.
- At interior p, equality of the weighted sums forces ψ_i(C) = ψ_i(B). Since c_k > 0 and each term
  is ≤, every L^{θ}(C) = L^{θ}(B).
- (R) applied to C ≺_i B would give a strict inequality, which is impossible. So C ~_i B, and
  L's (C) puts B in C_L.

### 2.3 Parts (a)–(e)

**(a) CORRECT.**
- Two interior p-Bayes models are coherent (Lemma K), so their difference set Z is a cone mod
  null sets.
- The radial splice is a pointwise p-minimiser in M, hence coherent by Lemma K.
- But the splice is not a.e. a cone: contradiction.
- The uniqueness obtained is uniqueness of the **Bayes minimiser** of ψ at p. It is not a claim
  about L's selection at p, and R11 never claims that.

**(b) CORRECT.** At e_i the objective is ψ_i alone. Its pointwise minimiser is the a.e.-unique
world-i-best advice in the advice range, i.e. W_i(M). Lemma K provides a selected e_i-Bayes model, and
uniqueness identifies it with W_i(M). The identification with C_{e_i} uses the vertex lemma, as
it should.

**(c) CORRECT.** Directly from Lemma K.

**(d) CORRECT.**
- Competitiveness of T on Ω (Lemma IC) plus (W)-contrapositive: no X has ψ(X) < ψ(T)
  coordinatewise.
- Convexity of the attainable set suffices for the separation. Compactness is not needed.
- If S = supp p_T ≠ Ω, IC's X (constructed for that S, legitimately since K ⊆ int Δ) strictly
  lowers ψ_i for i ∈ S and leaves p_T·ψ affected only through S, so p_T·ψ(X) < p_T·ψ(T).
- The general-K clause also checks: separation in ℝ^{supp a}.

**(e) CORRECT.** R1 Thm 2.2(S) requires, at every p ∈ Δ, an a.e.-unique minimiser that is a.e.
coherent. Theorem W supplies:
- uniqueness at interior priors by (a), at vertices by (b), and at the remaining boundary priors
  by (BT);
- coherence everywhere, because Lemma K's selected p-Bayes model must equal the unique minimiser.

T is p_T-Bayes, so T = B_{p_T} ∈ C_ψ. M is unchanged, so (LF) at T is kept.

**Remark (not an error).** (BT) is a property of the aggregate, not of L. The weights c_k are
arbitrary positive summable weights, and Θ may be enlarged by any further losses satisfying (W)
and (R). Different aggregates have different boundary tie sets, and every aggregate satisfies
(a)–(d). For multi-member families this is a free parameter that might be used to achieve (BT).
I have not tried to prove that it always can be.

### 2.4 Prop S (new; resolves §3.4): every sandwiched world is countably sandwiched

**Proposition S (PROVED here).** Let world i be sandwiched in R5's sense: Θ_i is any family of
additive losses with measurable penalties on the advice ranges, integrable envelopes, and strict guidance
at i, satisfying (W) and (R). Then some countable Θ′_i ⊆ Θ_i satisfies (W) and (R).

*Proof.*
1. Put d(θ, θ′) = ∫ max_{a∈A(g)} |ℓ^θ(g, a) − ℓ^{θ′}(g, a)| dμ. This is the norm of L¹ of
   μ ⊗ counting on the graph of A. That space is separable, because μ is a finite Borel measure
   on a countably generated σ-algebra.
2. Every subset of a separable metric space is separable. So Θ_i has a countable d-dense subset
   Θ′_i.
3. (W) passes to subfamilies.
4. For (R): if X ≺_i Y, pick θ with δ := L^θ(Y) − L^θ(X) > 0, and θ′ ∈ Θ′_i with d(θ, θ′) < δ/2.
   Since |L^θ(Z) − L^{θ′}(Z)| ≤ d(θ, θ′) for every Z ∈ M, we get L^{θ′}(Y) − L^{θ′}(X) > 0. ∎

**Consequences.**
- Theorem W (a)–(e), Corollary W1 and Corollary T hold for **every sandwiched system**, of any
  cardinality.
- §3.4's "exact missing step", item (ii) of §7.3, the OPEN row of §8, and mechanism (M2) for
  sandwiched worlds all disappear.
- (M2) can only occur at worlds that are not sandwiched by L¹ losses at all.
- R5 Remark (a)'s statement that aggregation "loses ties for uncountable families" is moot.
- R2 Prop 5's uncountable case is closed directly. R8's essential-union step is not needed:
  apply Prop S to the weakly guiding family. Then show, from strict (G), (R) for the countable
  subfamily and weak guidance of each member, that the countable aggregate is strictly guiding:
  a non-null tie set of the aggregate is a common tie set of every member, which contradicts (R)
  applied to the guidance-improving swap.

### 2.5 Corollary W1: CORRECT, with a wording fix

- U_ψ^{int} ⊆ U_L follows from (a).
- Continuity of the interior Bayes map follows from R1 Prop 3.1.
- "Its charts are continuous off a null set" must be read as R1 Thm 3.2(iii): continuity in
  measure at each h ∉ Bad. It is **not** a continuous representative off a closed null set. The
  audit's warning applies, and (H1) remains an extra hypothesis.

### 2.6 Corollary T: implication CORRECT; instance list needs repair

**The implication.** It is valid as stated: ψ on M has (LF) at T, (N1)–(N4), and T among its
interior Bayes models.

**Instances.**
- **R1 Thm 4.1 is not an instance of 𝒪.** It excludes the *prescribed* family
  K_q = (1−ε)σ(q) + εΔ on an open set (audit point 3; Consolidated §0.3.5). Its transfer says
  only that the aggregate ψ does not have that family, with that affine parametrisation, on an
  open set. That places no constraint on a sandwiched L vindicating T1. ψ's interior family is a
  subfamily of U_L, parametrised by ψ's own priors, possibly nonlinearly relative to any
  parametrisation one might impose on L.
  - Delete R1 Thm 4.1 from the instance lists in §0 item 6, the Cor T proof paragraph, and §6.
  - Equivalently, keep it only as "excludes aggregates with the prescribed family".
- **R4 Thms A–C, Cor B2/C3 and R1 Thm 4.2** are stated under (N) := (G) + (LA) + (S) + (C) for
  the additive ranking. ψ need not satisfy (S) (that is (BT)). The transfer therefore needs a
  recorded check that each proof uses only (N1)–(N4), (LF) and its extra hypotheses.
  - R8 confirms this for NOGO, PB and FA ("evaluate maps only at interior priors").
  - The proofs of R1 Props 2.4–2.8, 3.1, 3.2, Lemma 3.5 and R4 Thms B and C visibly use only
    (N1)–(N4).
  - This should be stated, not assumed.
- **Extra hypotheses are not intrinsic to L.** (H1)/(H1⁺) are chart-regularity hypotheses on ψ,
  and ψ depends on the weights. The conditional transfer reads: "no sandwiched L has an aggregate
  satisfying (H1) ...". (H0) is a domain property and transfers intrinsically.

The bold sentence ("if additive T1 is impossible for a reason not involving the boundary, ordinal
(countably sandwiched) T1 is impossible too") is correct. With Prop S, "countably" can be dropped.

---

## 3. The boundary

### 3.1 Lemma BT: CORRECT WITH REPAIR

**Defect.** The hypothesis constrains C′ only on int Δ. But q_s = p + s(e_j − p) has
supp q_s = supp p = S ≠ Ω (p is a non-vertex *boundary* prior), so q_s stays in p's face. There
C′_{q_s} = B_{q_s} is not assumed, and B_{q_s} need not even be unique. As written, the
liminf step uses values of C′ that the hypothesis does not control.

**Repair.**
1. Let v_δ = (1−δ)e_j + δu and q_k = (1−s_k)p + s_k v_δk, with s_k, δ_k ↓ 0. Each q_k is
   interior, so C′_{q_k} = B_{q_k}.
2. Fix g outside a null set (countably many k).
   - Let γ(g) > 0 be the p·ψ-gap between argmin and the other kinds of advice, and H(g) an envelope.
   - For s_k < γ/(γ + 4H), every q_k-minimiser lies in argmin p·ψ(g, ·), uniformly in δ.
   - Within argmin, q_k·ψ = s_k v_δk·ψ + const. For g ∈ G, w_j ≠ 0 between any two tied kinds of advice
     (strict guidance), so for δ_k < δ_0(g) the q_k-minimiser is the world-j-best tied advice.
3. Hence B_{q_k}(g) = X_j(g) for all large k, and dominated convergence gives
   ψ(B_{q_k}) → ψ(X_j).
4. The rest of the proof is unchanged and correct:
   - lower semicontinuity from closed sections, using that the attainable values of ψ_j form an
     interval;
   - the pointwise strict inequality on G, via a j ∈ S with w_j > 0;
   - integration, giving p·ψ(C′_p) < min_M p·ψ.

I verified the remaining steps:
- Unanimous problems carry no ties.
- On mixed g every pair of distinct kinds of advice has w_i ≠ 0 at every world.
- p·w = 0 with p_S > 0 forces both signs on S.

**Strengthening.**
- The proof is local. It suffices that C′_q = B_q for interior q in some neighbourhood of p.
- It is invariant under homeomorphic reindexing: if C′_x = B_{Φ(x)} on int Δ, with Φ continuous
  at x_0, Φ(x_0) = p, and Φ mapping every neighbourhood of x_0 in int Δ onto a neighbourhood of p
  in int Δ, then (S) fails at x_0. The contradiction p·ψ(C′) < min_M p·ψ involves values only,
  not indices.
- So the auditor's C_t = B_{t²} kind of reindexing cannot rescue a boundary tie. Only non-open
  ("blow-up") reindexings can, as in §4.3. The Reading after Lemma BT should say so.

### 3.2 §4.3 directional blow-up (n = 3, one point): UNVERIFIED as written; plausible

What I checked (under §4.3's assumptions: one tie point p, uniqueness at all other non-vertex
boundary priors, two tied kinds of advice, and for every v in the arc, {g ∈ G : v·w = 0} null):

1. **Uniform convergence in polar coordinates.** The gap threshold s_0(g) does not depend on v,
   so |ψ(B_{p+sv}) − ψ(X_v)| ≤ ∫_{s_0(g) ≤ s} 2H dμ → 0 uniformly in v. Together with continuity
   in measure of v ↦ X_v, the profile is continuous on the oriented blow-up.
2. **Edge directions.** The endpoints v_1, v_2 point along the edge, so X_{v_j} as a limit along
   p + s v_j again uses edge priors. This is legitimate under the "unique elsewhere on the edge"
   assumption. Alternatively, define X_{v_j} as the limit of X_v as v → v_j: v_1·w = w_1 ≠ 0.
3. **Coherence of X_v.** Limits in measure of D_{K_k} are a.e. D_K for any Hausdorff limit point
   K, since ∂D_K is null. R1 Prop 3.1, cited in the notes, covers only interior priors, but this
   argument suffices.
4. **Undominatedness.** For v_3 > 0 there is a shorter proof than the splice: a weak dominator Y
   is p-Bayes, so ψ_1 and ψ_2 are equal, so v·(ψ(Y) − ψ(X_v)) = v_3(ψ_3(Y) − ψ_3(X_v)) < 0.
   But pointwise v·ψ(Y) ≥ v·ψ(X_v): contradiction.
5. **(C) for the inserted models.** ψ(Y) = ψ(X_v) forces Y = X_v a.e., by v·w ≠ 0 a.e. on G.
   This is needed and not stated in the notes.

Not written:
- the face-preserving reindexing map (a Joukowski-type map from the half-disc minus a boundary
  slit onto the half-disc minus a point works);
- (LA)/(S)/(C) for the new selection, in full;
- the **degenerate directions**: the sets {v·w = 0} are disjoint for distinct rays v of the open
  arc, so at most countably many v are degenerate. At those, X_v is not unique and a second,
  nested insertion is needed, as in R2 Thm R Step 2–4.

Label: sketch, plausible, not CHECKED.

### 3.3 Prop E (new): in n = 3 boundary ties occur at only countably many points per edge

Let p = (p_1, p_2, 0) be on the edge [e_1, e_2] and (a, b) a pair of kinds of advice at g. A tie
p·(ψ(g,a) − ψ(g,b)) = 0 with w_1, w_2 ≠ 0 (strict guidance) determines p_1/p_2 = −w_2/w_1
uniquely, or has no solution. So each (g, pair) ties at most at one point of each edge. The sets
G_p are therefore disjoint up to multiplicity 6, and Σ_p μ(G_p) ≤ 6μ(H) < ∞. Only countably many
edge points carry a non-null tie.

**Consequence.** The "continuum of tie points along an edge" that §4.3 calls the hardest case
cannot occur for n = 3. The general n = 3 case is countably many (possibly dense) tie points.
That is structurally the same as R2 Thm R's countable insertion, which makes the boundary blow-up
conjecture considerably more plausible for n = 3. For n ≥ 4 the faces have dimension ≥ 2, tie
loci are hyperplane sections, and continua do occur. There the conjecture stands as stated.

### 3.4 §4.2: CORRECT

L's boundary selection is ψ-competitive on supp p. Neither ψ-undominatedness nor closed ψ-sections
follow, since (W) gives only one inclusion.

---

## 4. Lexicographic part

### 4.1 Lemma SF_n: CORRECT

Checked:
- Lemma F(i) for t ∈ int Δ: a weak dominator has every P_i ≤, and t·P is minimal, so all are
  equal.
- 𝒦 ⊂ ℝ^{2n} is convex and compact (Aumann).
- Each g_i is convex and finite on F_t, hence continuous on relint F_t.
- The "good" set is the preimage of the compact projection of 𝒦 under the continuous map
  x ↦ (x, g_{I_v}(x)), so N is relatively open.
- For x ∈ N, the lexicographic minimiser Z (I_v first) is undominated: a weak dominator lies in
  the fibre with all S_i ≤, so successive minimality forces equality in every coordinate. Z is
  improvable at some i ∈ I_v by a fibre member with the same P_i.
- R2 Thm 7 (U_L form, any n; (C) not needed per R6) makes C_i countable.
- For i ∈ I_v, x_i is non-constant affine on aff F_t, so its level sets are nowhere dense in
  relint F_t, which is a Baire space. Hence N = ∅.
- Multi-Lagrangian part: Pareto-minimality in the fibre plus an ideal point gives S(X) = g(x). A
  subgradient of g_i at the relative-interior point x gives S_i − λ_i·π minimised at X over 𝔅_t.

Cosmetic fixes:
1. The existence claim for x ∉ N needs one sentence. The lexicographic minimiser with I_v first
   attains every g_i (i ∈ I_v), because an ideal member exists, and it is undominated by the
   argument above. The proof only shows N = ∅.
2. In the Reading, "I_v ≠ Ω, possible only for n ≥ 3" should be "∅ ≠ I_v ≠ Ω". I_v = ∅ (a point
   face) occurs for n = 2. In n = 2, F_t lies on a line, so I_v ∈ {∅, Ω}.

The summary's "(S) kills (M1) on interior faces in any n" holds only on faces with I_v = Ω, as
the Reading says. Mixed faces are not covered.

### 4.2 Prop LX: CORRECT

- Λ_i = Σ ε^{k−1}L^k_i represents ⪯_i exactly.
- The pointwise lex minimiser minimises p·Λ over M: successive pointwise minimisation, R5
  Lemma 4.1.
- Fact 0(a) gives Λ_i(C) ≤ Λ_i(B_p). Since p_i > 0 in an ordered field, every Λ_i(C) = Λ_i(B_p),
  i.e. lex ties.
- (C) gives coherence. Uniqueness follows by the radial splice, which is again a pointwise lex
  minimiser.
- The F-prior clause holds: Lemma 4.1 covers F-coefficients, because finitely many real integrals
  with lex-nonnegative pointwise combinations integrate to lex-nonnegative values.

### 4.3 (M3) and "T solves two levels of t + εu": CORRECT (with a detail)

- The chart description is right.
- The Fubini claim is right: Z(p) is null for λ-a.e. p.
- n = 2: P* is countable, by the disjointness argument of §3.3.
- On the passage from the multi-Lagrangian to an F-prior: μ = −Σ t_iλ_i is determined modulo
  multiples of t on 𝔅_t, so it can be normalised to Σμ = 0. Then t + εμ is an F-prior and level 2
  of its objective is t·S + μ·P on 𝔅_t. The note should say "u := μ normalised". As written,
  "t + εu" leaves u unrelated to μ.

---

## 5. (R_c) for uncountable families

**As a sufficient condition: CORRECT.** Lemma K uses (R) only for (selected C, ψ-Bayes B) with
C ⪯_i B, and (R_c) covers this.

**The "missing step" is not missing.** By Prop S (§2.4), every R5-sandwiching family has a
countable subfamily satisfying full (R), so (R_c) holds. The scenario described in §3.4 (an
incoherent ψ-Bayes splice separated from C only by an unused θ) cannot occur for any countable
dense subfamily.

---

## 6. Recommended changes to R11's summary and status table

1. Replace "countably sandwiched" by "sandwiched" throughout, citing Prop S. Change the row
   "Uncountable sandwiches: OPEN" to "closed (separability of L¹; R13 Prop S)". Remove (M2) for
   sandwiched worlds.
2. Lemma IC Remark (ii): replace with "supp a ∉ 𝒮".
3. Lemma BT: approach p from int Δ (repair §3.1). Add the locality and homeomorphic-reindexing
   strengthening, and correct the Reading: C_t = B_{t²}-type reindexings do not help, only
   blow-ups do.
4. §4.3: relabel "sketch (plausible), not CHECKED". Add (C) for inserted models and the
   degenerate-direction issue. Replace the "continuum along an edge" paragraph by Prop E: for
   n = 3, only countably many tie points per edge.
5. Corollary T: drop R1 Thm 4.1 from the instance list, or restate it as a statement about
   aggregates with the prescribed family. Record that the other instances use only (N1)–(N4).
   Note that (H1)-type hypotheses are on ψ, not on L.
6. Corollary W1: "continuous off a null set" should read "in the sense of R1 Thm 3.2(iii)".
7. Remove "irrelevant at the target (Lemma V)" from §0 item 7 and §2 (M1).
8. SF_n: add the one-line existence step and fix "I_v ≠ Ω ⇒ n ≥ 3".

## 7. Net assessment

The central result stands: Theorem W (a)–(d) is correct, and (e) under (BT). With Prop S it
applies to every sandwiched system, not only countable ones. So the single-target reduction for
sandwiched L (any cardinality, any n) is proved modulo boundary ties of the aggregate.

For n = 3 those ties sit at countably many edge points (Prop E). The residual is then a countable
blow-up problem of R2-Thm-R type, whose one-point case (§4.3) is plausible but unwritten.

The lexicographic results (SF_n, LX) are correct. The open lex steps (T in the family; interior
blow-up) are correctly labelled CONJECTURE.

No result in R11 bears on general (IB) preorders beyond Lemmas V, IC and RS, as the note itself
says.
