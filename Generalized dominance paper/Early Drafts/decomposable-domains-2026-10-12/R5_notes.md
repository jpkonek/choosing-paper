# R5. Structure theorem: does closed competitive choice force additive undominated sets?

12 October 2026, round 9. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof
sketched or delegated to a cited proof re-read for this setting), **CONJECTURE**.
Setting and notation as in BRIEF.md and R2_notes.md: decomposable domain M, models mod null sets,
U_L = undominated members of M, C_L = coherent undominated members. Under (LA),(S),(C):
U_L = C_L ⊆ coherent, and every member of U_L is tied at every world with a selected model
(R2 Lemma 1). For coherent A = D_{K_A}, B = D_{K_B} ∈ M and a mixed sign pattern σ, put
R_σ(A,B) = {h : sign h = σ, A accepts h, B silent on {h,−h}} (a cone, since A and B are).
Hypothesis (Nest): R_σ(A,B) is non-null for every mixed σ. It holds when K_A ⊂ int K_B
(R2 Thm N), and in n = 2 exactly when the pair is strictly nested (R2 Prop N2).
Decomposable domains throughout; the all-model domain is not assumed.

## 0. Summary

1. **Theorem UN (PROVED, any n ≥ 2).** Suppose each world's preorder ⪯_i is *sandwiched*
   by some nonempty family Θ_i (any cardinality) of strictly guiding additive losses on M:
   (W) X ⪯_i Y ⇒ L^θ(X) ≤ L^θ(Y) for all θ ∈ Θ_i, and (R) X ≺_i Y ⇒ L^θ(X) < L^θ(Y) for
   some θ ∈ Θ_i. With strict (G), (IB), (LA), (S), (C), U_L contains no pair satisfying
   (Nest). This covers every unanimity (Pareto) ranking of additive strictly guiding losses,
   with no countability (it closes R2's "uncountable unanimity" case), and every incomplete
   ranking whose strict comparisons are witnessed by its strictly guiding additive weak
   extensions. With R2 Theorem R: **in n = 2 every sandwiched system has an additively
   representable U_L.** The proof is new: competitiveness is pushed into every *pairing*
   (one loss per world) separately, and the incoherent splice is undominated for all pairings
   at once.
2. **Lemma N1 (PROVED)**: a nested pair in U_L may be assumed selected, at interior priors.
   **Lemma TJ (PROVED, any n)**: if every world's tie relation is cut out by finitely many
   additive functionals (additive rankings, finite-level lexicographic rankings with
   additive levels, finite unanimity), distinct members of C_L are never tied at all
   worlds. Hence "tie-jumps" (a selection switching between A and B with A ~ B) cannot
   produce nesting in these classes.
3. **Lemma X (cross-competitiveness, PROVED, n = 2, any preorders)**: if A, B ∈ U_L are strictly nested, then the region comparisons at the two worlds satisfy an exchange condition
   (★). Under completeness plus fineness of the region orders (CCF sense), (★) forces the
   Savage–Wakker probabilities of the two worlds to be proportional on the region
   (Prop X2, CHECKED). What survives is purely non-Archimedean: infinitesimal deviations of
   the cross-ratio. This is the precise residual of Conjecture 1 for complete rankings.
4. **Conjecture 1 (n = 2, every (IB) system)**: still **CONJECTURE**. Not proved, no
   counterexample. Proved now for: additive (R2), sandwiched systems of any cardinality
   (UN), one lex world + one additive world (R2 Thm 6). Not covered: both worlds
   non-Archimedean (finite lex at both worlds, Conjecture 1′), and complete orders without
   any strictly guiding additive weak extension (IRWAS / KPS-type). For finite lex, §4 shows
   that every step of the additive proof transfers to ℝ(ε)-valued losses (Prop 4.2) **except**
   "undominated ⇒ (non-standard) Bayes", and **Example 4.3 shows that step is false**: an
   undominated point of an ℝ-convex attainable set in ℝ(ε)² with no F-supporting prior. This is
   the precise non-Archimedean gap; standard parts are forced proportional (Lemma 4.4), only
   ε-parts are free.
5. **n ≥ 3 (§5)**: Theorem R_n (CHECKED): U_L is additively representable iff it admits a
   parametrisation by Δ whose per-problem charts are vertex-respecting affine minimisation
   diagrams with null boundaries (the "affine-chart property"). Intrinsic necessary
   conditions: no (Nest) pair (R2 Thm N), and a stronger pairwise *pattern compatibility*
   (Prop PC, PROVED). Theorem UN gives no-(Nest) for sandwiched systems in every n. Whether
   no-(Nest) (or pattern compatibility) plus (S) suffices for n ≥ 3 is **OPEN**; I explain
   why it is not a pairwise question in n ≥ 3 (Remark 5.4).

## 1. Normalisation lemmas

**Lemma N1 (PROVED, any n).** Assume strict (G), (IB), (LA), (S), (C). Let A, B ∈ U_L satisfy
(Nest). Then either A and B are tied at every world, or there is a selection C' satisfying
(S) (same C_L) with C'_a = A, C'_b = B for some a ≠ b, both in int Δ.

*Proof.* By R2 Lemma 1, A is tied at every world with some selected C_a, and B with some C_b.
If a = b (or more generally C_a ~ C_b at every world) then A ~ B at every world. Otherwise
put C'_a = A, C'_b = B, C'_p = C_p elsewhere. A ∈ C_L (Lemma 1). Ties transfer
competitiveness: C_a ⪯_i X and A ~_i C_a give A ⪯_i X. Sections are unchanged:
{p : C'_p ⪯_i X} = {p : C_p ⪯_i X}, since C'_a ~_i C_a. So C' satisfies (S).
Interiority: let S = supp a ≠ Ω. Pick the mixed σ with σ_i = − exactly for i ∈ S. On
R_σ(A,B) (non-null), A accepts an orientation that is bad at every world of S, and silence
is in the advice range (B gives it). Silencing A there gives X ∈ M that is pointwise better at every
world of S, strictly on a non-null set, so X ≺_i A for all i ∈ S by strict (G). Then A is not
competitive on S, though it inherits competitiveness on S from C_a. Same for b. ∎

**Lemma TJ (tie-midpoint; PROVED, any n).** Assume (C), and suppose at each world i there are
finitely many additive functionals Φ_i = (Φ_i^1, …, Φ_i^{m_i}), Φ_i^k(X) = ∫ φ_i^k(g, a_X(g)) dμ
(φ measurable, integrable envelope on the advice ranges), with X ~_i Y ⇔ Φ_i(X) = Φ_i(Y). Then two
distinct members of C_L are never tied at every world.
Examples: additive rankings; lexicographic rankings with finitely many additive levels
(lex ties are equalities of all levels); unanimity of finitely many additive losses.

*Proof.* Let A ≠ B ∈ C_L be tied at every world. Z = {g ∈ H : a_A(g) ≠ a_B(g)} is non-null and,
A and B being coherent, a cone mod null sets. For S ⊆ Z let E_S = A on S, B elsewhere;
E_S ∈ M. Then Φ(E_S) = Φ(B) + m(S), where m(S) = ∫_S (φ(g,a_A) − φ(g,a_B)) dμ is a finite
non-atomic vector measure (all worlds and levels stacked), and m(Z) = Φ(A) − Φ(B) = 0.
Split Z^< = Z ∩ {|g| < 1}, Z^≥ = Z ∖ Z^<. Lyapunov gives H1 ⊆ Z^<, H2 ⊆ Z^≥ with
m(H1) = ½m(Z^<), m(H2) = ½m(Z^≥). Put S0 = H1 ∪ H2 and S1 = H1 ∪ (Z^≥∖H2). Then
m(S0) = m(S1) = ½m(Z) = 0, so E_{S0}, E_{S1} are tied at every world with A, and (C) puts
both in C_L; both are coherent.
A coherent model's advice is a function of the direction of g, so by polar Fubini, for a.e.
ray ρ in Z, S0 ∩ ρ and S1 ∩ ρ are each null or co-null in ρ. On ρ^≥ = ρ ∩ Z^≥ the sets S0, S1
are complementary, and both ρ^< and ρ^≥ are non-null (the radial density of μ is positive).
If S0∩ρ is co-null, then S1∩ρ^≥ is null, so S1∩ρ is null, so H1∩ρ^< is null, contradicting
S0∩ρ co-null. If S0∩ρ is null, then H2∩ρ^≥ is null, so S1 ⊇ ρ^≥, so S1∩ρ is co-null and H1∩ρ^<
is co-null, contradicting S0∩ρ null. Z has a positive-measure set of rays. ∎

*Use.* In these classes a nested pair cannot arise by a "tie-jump" (a selection equal to B on
one side of a point and to A on the other: by R3 Lemma 2.1 that forces A ~ B at all worlds).
Together with N1: in these classes every member of U_L is itself selected (U_L = {C_p : p ∈ Δ}
exactly), and a nested pair is selected at two distinct interior priors.

## 2. Sandwiched rankings: no nesting in any number of worlds

A loss L(X) = ∫_H ℓ(g, a_X(g)) dμ on M is *strictly guiding at i* if ℓ(g,·) is strictly
increasing in world-i rank on A(g) for a.e. g, with an integrable envelope (R1 Lemma 1.1).
World i is **sandwiched** by a nonempty family Θ_i of such losses if
 (W) X ⪯_i Y ⇒ L^θ(X) ≤ L^θ(Y) for every θ ∈ Θ_i, and
 (R) X ≺_i Y ⇒ L^θ(X) < L^θ(Y) for some θ ∈ Θ_i.
No cardinality, measurability in θ, or completeness is assumed. The unanimity ranking
X ⪯_i Y ⇔ ∀θ L^θ(X) ≤ L^θ(Y) is sandwiched by Θ_i; so is every preorder lying between it and
a coarser relation with the same strict part. Unanimity rankings satisfy (IB) and strict (G).

**Theorem UN (PROVED).** n ≥ 2, decomposable domain M, strict (G), (IB), (LA), (S), (C), every world
sandwiched. Then U_L contains no pair A, B satisfying (Nest). In particular no
D_{K_A}, D_{K_B} ∈ U_L with K_A ⊂ int K_B; in n = 2, no strictly nested pair.

*Proof.* Suppose A, B ∈ U_L satisfy (Nest).

*Step 0 (competitiveness).* By Lemma N1 (or directly: A is tied with a selected C_a and
ties transfer competitiveness), A is competitive on Ω: for every X ∈ M some i has A ⪯_i X.
Lemma N1's interiority argument gives supp a = Ω; if N1's first alternative occurs (A ~ B)
the same holds, since then A and B inherit competitiveness from one selected model whose
support must be Ω by the same argument. Likewise for B.

*Step 1 (each pairing is Bayes).* Fix a pairing θ = (θ_i)_{i∈Ω}, θ_i ∈ Θ_i, and write
L^θ(X) = (L^{θ_i}(X))_i ∈ ℝ^n. If some X had L^θ_i(X) < L^θ_i(A) for every i, then by (W)
(contrapositive) A ⪯_i X fails at every i, contradicting Step 0. The attainable set
K_θ = {L^θ(X) : X ∈ M} is convex and compact (Aumann/Lyapunov; R2 §1), so K_θ − L^θ(A) misses
the open negative orthant, and a separating nonzero functional is nonnegative. Normalising
gives p^θ_A ∈ Δ with p^θ_A·L^θ(A) ≤ p^θ_A·L^θ(X) for all X ∈ M. Thus A is p^θ_A-Bayes for the
additive system θ, and its advice is a.e. a pointwise minimiser of p^θ_A·ℓ^θ(g,·) over A(g)
(R2, pointwise Bayes). Likewise B at p^θ_B.

*Step 2 (common interior prior).* This is R2 Theorem N, run inside the pairing. On R_σ(A,B)
both acceptance (A's advice) and silence (B's) are in the advice range. Let
c(h) = (ℓ^{θ_i}(h,silence) − ℓ^{θ_i}(h,accept h))_i. Strict guidance gives sign c(h) = σ
on R_σ. Pointwise optimality gives p^θ_A·c ≥ 0 ≥ p^θ_B·c a.e. on R_σ. If u = p^θ_A − p^θ_B ≠ 0,
u has both signs (Σu = 0); for the mixed σ* with σ*_i = −sign u_i on supp u, c·u < 0 on the
non-null R_{σ*}: contradiction. So p^θ_A = p^θ_B =: p^θ. If p^θ_j = 0 for some j, take σ with
σ_i = + exactly on supp p^θ (mixed). On R_σ, B's silence needs p^θ·c ≤ 0, but
p^θ·c = Σ_{supp p^θ} p^θ_i c_i > 0. So p^θ ∈ int Δ. Note p^θ depends on θ.

*Step 3 (one splice for all pairings).* Fix a mixed σ0 and let S = R_{σ0}(A,B) ∩ {|h| < 1}
(as a set of problems). Let E = A on S, B elsewhere; E ∈ M. The set S does not depend on θ.
For every pairing θ, E's advice is a.e. a pointwise p^θ-minimiser (A's advice on S, B's
elsewhere, both minimisers at the common prior p^θ). So E is p^θ-Bayes for θ, with p^θ interior.

*Step 4 (E is undominated).* Suppose Y ⪯_i E at every world and Y ≺_j E. By (R) choose
θ*_j ∈ Θ_j with L^{θ*_j}(Y) < L^{θ*_j}(E). Complete θ* arbitrarily at the other worlds. By (W),
L^{θ*}_i(Y) ≤ L^{θ*}_i(E) for all i. Since p^{θ*}_j > 0, p^{θ*}·L^{θ*}(Y) < p^{θ*}·L^{θ*}(E),
contradicting Step 3. So E ∈ U_L.

*Step 5 (E is incoherent).* On the cone R_{σ0}, B is silent and E accepts exactly on
{|h| < 1}. A coherent model's acceptance set is a cone, and R_{σ0} is a non-null cone, so E is
not a.e. equal to a coherent model. This contradicts U_L ⊆ coherent (R2 Lemma 1). ∎

**Corollary UN2 (PROVED, n = 2).** For every sandwiched system on a decomposable domain with strict
(G), (IB), (LA), (S), (C), U_L is the undominated set of an additive strictly guiding
(LA),(S),(C) system on the same domain, namely a continuous monotone path (R2 Theorem R
and Prop P).

*Remarks.*
(a) The proof never aggregates the family (R2 Prop 5 aggregated a countable family into one
weighted sum, which loses ties for uncountable families). Pairing world-by-world avoids
aggregation: competitiveness holds in every pairing, and the splice is Bayes in every pairing
at a pairing-dependent but always interior prior.
(b) Which (IB) rankings fall outside? Exactly those with a strict comparison X ≺_i Y that no
strictly guiding additive weak extension of ⪯_i separates. R2 Prop 4 (lexicographic) and IRWAS
(ultrafilter/KPS) are of this kind; for the latter, no additive weak extension exists at all.
So **any counterexample to Conjecture 1 must use a world whose strict part is not witnessed by
its additive weak extensions**, i.e. a genuinely non-Archimedean or non-representable world.
(c) Charges in place of integrals (CBOI's finitely additive form) are not covered: Step 1 needs
convexity of the attainable set, which I have not checked for vector charges. Not claimed.

## 3. Complete rankings in two worlds: what competitiveness of a nested pair forces

n = 2. A = D_{[α_A,β_A]}, B = D_{[α_B,β_B]} ∈ U_L strictly nested; R1 = {α_B < r < α_A}
(A: +, B: 0), R2 = {β_A < r < β_B} (A: −, B: 0), R = R1 ∪ R2. For Z ⊆ R let X_Z be the model
equal to A = B off R, with + on Z∩R1, 0 on R1∖Z, 0 on Z∩R2, − on R2∖Z. So X_{R1} = A, X_{R2} = B,
X_Z ∈ M, and enlarging Z is a pointwise improvement at world 1 and a pointwise worsening at
world 2. By (IB), V ⪯_{q1} V' :⇔ X_{V'} ⪯_1 X_V, and V ⪯_{q2} V' :⇔ X_V ⪯_2 X_{V'}, define
"comparative-probability" preorders on the measure algebra of R (de Finetti additivity is
(IB); monotonicity and strict monotonicity are (G)), independent of the context used.

**Lemma X (cross-competitiveness; PROVED, any preorders).** Under (G), (IB), (LA), (S), (C),
for all measurable U ⊆ R1, W ⊆ R2:
 (★A) W ⪯_{q1} U or U ⪯_{q2} W (i.e. A ⪯_1 or ⪯_2 the model "A moved to B on U ∪ W"),
 (★B) U ⪯_{q1} W or W ⪯_{q2} U.
For complete rankings: the two worlds never *strictly disagree* on a cross pair (U ⊆ R1,
W ⊆ R2): never q1(U) ≻ q1(W) with q2(U) ≺ q2(W), and never the reverse.

*Proof.* A and B are competitive on Ω (Step 0 of Theorem UN; it used only (Nest)).
Let Y = A with silence on U ∪ W. Then Y and A differ exactly on U ∪ W, where A has (+ on U,
− on W) and Y is silent. By (IB) the comparison of
Y with A is the comparison of X_{C∪U} with X_{C∪W} for the common context C = (the Z-set of
A) ∖ U; so A ⪯_1 Y ⇔ X_{C∪U} ⪯_1 X_{C∪W} ⇔ W ⪯_{q1} U, and A ⪯_2 Y ⇔ U ⪯_{q2} W. Competitiveness of A against Y gives (★A). For (★B) use B and B with
A's advice on U ∪ W. ∎

**Proposition X2 (proportional Archimedean parts; CHECKED).** Suppose in addition that both
rankings are complete and that q1 and q2 are *fine* on R (CCF §5: every non-null V ⊆ R admits
a finite partition of R into sets ⪯ V). Let P1, P2 be the Savage–Wakker finitely additive
probabilities almost agreeing with q1, q2 (CCF Thm SW). Then there is κ > 0 with P2 = κ P1 on
the measurable subsets of R.

*Proof.* CCF Lemma Pd applies verbatim on R: (i) P(V) < P(V') ⇒ V ≺ V' (completeness);
(ii) P(V) > 0 iff V non-null; (iv) simultaneous θ-splitting for (P1, P2) within any η.
Let ρ(V) = P2(V)/P1(V) for non-null V. Suppose ρ(U) < ρ(W), U ⊆ R1, W ⊆ R2 non-null. Put
a = P2(U)/P2(W) < b = P1(U)/P1(W). If a < 1 pick θ ∈ (a, min(b,1)) and replace W by
W_θ ⊆ W with P_l(W_θ) within η of θP_l(W) (l = 1,2); for small η, P1(W_θ) < P1(U) and
P2(W_θ) > P2(U). If a ≥ 1 pick θ' ∈ (1/b, 1/a) ⊆ (0,1] and shrink U instead. Either way
(i) gives q1(U') ≻ q1(W') and q2(U') ≺ q2(W'), contradicting (★B). The reverse inequality
is excluded by (★A) symmetrically. So ρ is constant on non-null subsets of R1 and of R2,
with one common value κ; finite additivity gives P2 = κP1 on R. ∎

*What remains (the residual of Conjecture 1 for complete rankings).* In the additive case
P_l = q_l exactly, and κ-proportionality is the Theorem N tie; Theorem UN then exhibits an
incoherent undominated splice. Under Prop X2 only almost-agreement is available: the two
worlds agree on the region **up to the non-Archimedean part of the orders**, i.e. up to the
comparisons P_l cannot see (ties of P_l broken by q_l). A counterexample must therefore live
entirely in that part. Two further obstacles any such counterexample must pass:
- (C) with Lemma TJ: if the tie relations are finitely additive-generated, A and B cannot be
  tied, so the nested pair must be connected through the selection by a continuum of
  undominated models;
- R2 Theorem 7 / R3 P1–P3: at a lexicographic world the improvable members of U_L occupy only
  countably many primary levels.
*Fineness is not free in n = 2.* CCF derives fineness from edge selections with the endpoint
property; in n = 2 the relevant selections (interior intervals) do not have it. So Prop X2 is
conditional on fineness. Without fineness, q_l need not have any almost-agreeing probability
(IRWAS), and Lemma X is the only general consequence I can prove.

## 4. Finitely many additive lexicographic levels (Conjecture 1′): what transfers, what breaks

A lexicographic ranking with additive levels L^1_i, …, L^m_i is exactly the order of the single
additive loss L_i = Σ_k ε^{k−1} L^k_i with values in the ordered field ℝ(ε) (ε > 0
infinitesimal): lex comparison of level vectors = sign of the leading coefficient. Local
penalties ℓ_i(g,·) = Σ_k ε^{k−1} ℓ^k_i(g,·) ∈ ℝ[ε]; strict guidance = strictly increasing in rank
in the field order. Fix a real-closed ordered field F ⊇ ℝ(ε) (any; saturation is irrelevant
below). An *F-prior* is p ∈ F^n, p ≥ 0, Σp = 1; *interior* if all p_i > 0. X is *F-p-Bayes* if
p·L(X) ≤ p·L(Y) for all Y ∈ M.

**Lemma 4.1 (integration over F; PROVED).** If p·ℓ(g, a_X(g)) ≤ p·ℓ(g, a_Y(g)) in F for a.e. g,
then p·L(X) ≤ p·L(Y); if moreover the inequality is strict on a non-null set, it is strict.
*Proof.* f(g) = p·(ℓ(g,a_Y) − ℓ(g,a_X)) = Σ_r c_r f_r(g), c_r ∈ F, f_r real integrable. The
ℝ-span V of the c_r is a finite-dimensional ordered real vector space, hence (Hahn, finite
dimension) has a basis b_1 ≫ … ≫ b_s in which the order is lexicographic. Rewrite
f = Σ_t b_t h_t, h_t real. f ≥ 0 a.e. means (h_1,…,h_s)(g) ≥_lex 0 a.e. Then ∫h_1 ≥ 0; if
∫h_1 = 0 then h_1 = 0 a.e. and h_2 ≥ 0 a.e.; and so on. So (∫h_t)_t ≥_lex 0, i.e.
∫f ≥ 0. Strictness: the first t with h_t ≠ 0 on a non-null set has ∫h_t > 0. ∎
Hence "pointwise F-p-minimiser a.e." ⇔ F-p-Bayes, as in the real case.

**Proposition 4.2 (conditional no-nesting; PROVED).** Finite-level lex with additive levels
(strictly guiding composite) at every world, any n, strict (G), (IB), (LA), (S), (C). If every
member of U_L that is competitive on Ω is F-p-Bayes for some F-prior p, then U_L has no pair
satisfying (Nest).
*Proof.* Theorem UN, Steps 2–5, with Θ_i = {L_i} (one F-valued loss; (W) and (R) hold
exactly, since ⪯_i is the order of L_i). Step 2 is algebra in the ordered field F (the sign
argument and the boundary argument use only signs and positivity). Step 3 uses Lemma 4.1.
Step 4: Y weakly dominating E with Y ≺_j E gives p·L(Y) < p·L(E) because p_j > 0 in F.
Step 5 is unchanged. ∎

So for finite lex the **only** missing step is the separation "competitive (even undominated)
⇒ F-Bayes". It is false in general:

**Example 4.3 (undominated, not F-Bayes; PROVED).** Two worlds, two lex levels. Let
x = (½ − 2ε, −½ + ε), y = (−½ − 2ε, ½ + ε) ∈ ℝ(ε)², and K = {λx + λ′y : λ, λ′ ∈ [0,1] real},
the attainable change set of a decomposable domain with two kinds of advice in the advice range on two disjoint regions P_x, P_y with
constant local differences (switch on a λ-fraction of P_x and a λ′-fraction of P_y). The guidance
signs are legitimate: on P_x the switch is worse at world 1 and better at world 2, on P_y the
reverse. Then 0 (the base model A) is undominated: for real λ ≠ λ′ the standard parts
(½(λ−λ′), −½(λ−λ′)) have opposite signs; for λ = λ′ = s > 0 the point is (−4εs, 2εs), better
at 1, worse at 2. But no F-prior (t, 1−t) supports K at 0: x forces t ≥ (½−ε)/(1−3ε) > ½ and
y forces t ≤ (½+ε)/(1+3ε) < ½. (In F the segment from x to y crosses the open negative
quadrant on an infinitesimal λ-interval around ½ that contains no real λ.) ∎

*Consequence.* Theorem N's mechanism genuinely fails for lexicographic rankings: an
undominated selected model need not carry any (even non-standard) prior. Conjecture 1′
therefore cannot be proved by transfer of the additive argument, and Example 4.3 is the
non-Archimedean seed from which a counterexample would have to grow. What such a counterexample
still has to defeat:
- Lemma 4.4 below: the standard parts of the two worlds must be proportional across the
  region (in Example 4.3 the standard parts on P_x, P_y are (½,−½) and (−½,½): proportional,
  κ = 1);
- Lemma TJ: A and B are not tied, so they are joined in U_L through a continuum of selected
  models;
- R2 Thm 7 / R3 P1–P3: improvable members of U_L occupy countably many primary levels at each
  world; on an open set of priors where the primary varies, the selection is single-world
  Lagrangian (R3 P2). Because the standard parts are proportional on the region (X2), all
  region splices with the same standard mass share a primary level (when the primaries see
  the whole region); a nested pair in U_L must
  therefore sit on **one** primary level at each world, or be connected through
  non-improvable (single-world Lagrangian) models.
I did not succeed in assembling a full system (with closed sections for every X ∈ M and (C))
around Example 4.3, nor in excluding one. **Conjecture 1′: CONJECTURE (open).** My current
belief is weakly in favour of a counterexample existing for finite lex at both worlds, on a
domain larger than the region-only domain, because Example 4.3 removes the only rigidity
lemma; I have no construction.

*Region-only domain (CONJECTURE, with a heuristic argument).* If M has non-singleton advice ranges only on R (so M ≅ subsets
of R), then with finite lex additive levels and X2-proportional standard parts, the undominated
region sets at a common standard mass m form the Pareto set of a two-objective additive problem
under a mass constraint. Generically it is a continuum for every m, which (S) forbids
(R2 Thm 7). Making it a singleton for all m but one forces, by Hausdorff continuity of the
slices of the zonoid range, either an incoherent tie plateau or a chain. So no counterexample
lives on the region-only domain; any counterexample must use non-singleton advice ranges outside R. (Heuristic only:
the "singleton for all m ≠ m*" step is not proved; I label the whole paragraph CONJECTURE.)

**Lemma 4.4 (standard parts proportional; PROVED).** n = 2, finite lex with additive levels at
both worlds, A, B ∈ U_L strictly nested, with region R = R1 ∪ R2 as in §3. Let γ_l(U), δ_l(W) ∈
ℝ[ε] be the world-l values of the exchanges "credit on U ⊆ R1" and "debt on W ⊆ R2" (as in
Lemma X), and suppose their standard parts are positive on every non-null U, W (the primaries
see the whole region). Then st(γ_2/γ_1) and st(δ_2/δ_1) take one common constant value κ on all
non-null U ⊆ R1, W ⊆ R2.
*Proof.* Lemma X in field form: no U, W with γ_1(U) > δ_1(W) and γ_2(U) < δ_2(W), nor the
reverse. All coefficient measures are finitely many real non-atomic measures, so Lyapunov gives
W_θ ⊆ W with δ_l(W_θ) = θ δ_l(W) exactly, for any real θ ∈ [0,1] (and likewise U_θ). If
st ρ(U) < st ρ(W) with ρ = (world-2 value)/(world-1 value), the interval
(γ_2(U)/δ_2(W), γ_1(U)/δ_1(W)) of F has standard endpoints differing by a standard amount, so it
contains a real θ (or the inverted interval for shrinking U does, as in Prop X2). The
corresponding real splitting violates (★B). The reverse inequality violates (★A). ∎
Only standard parts are forced: Example 4.3 shows the ε-parts are free.

## 5. n ≥ 3: the right analogue of Theorem R

### 5.1 Patterns
For A ≠ B ∈ M and a non-null set where A gives a and B gives b ≠ a, the change B → A has
*pattern* τ ∈ {+,−}^n, τ_i = + iff a is better than b at world i (ranks are distinct at every
world off null sets). If B is undominated, τ ≡ + is not realised (switching B to a there
would improve B at every world, strictly by (G)); if A is undominated, τ ≡ − is not. Let T(A,B) be the
set of mixed patterns realised on non-null sets. In n = 2, for coherent A, B:
T(A,B) = both mixed patterns ⇔ strictly nested. (Nest) ⇒ T(A,B) = all mixed patterns.

**Theorem PC (pattern compatibility for additive systems; PROVED, any n).** Let an additive
strictly guiding (LA),(S),(C) system on a decomposable domain have A ≠ B ∈ U_add, Bayes at p_A, p_B.
Then for every realised τ = (P,N) ∈ T(A,B) there are i ∈ P, j ∈ N with
p_A,i p_B,j ≥ p_A,j p_B,i. In particular T(A,B) is never the set of all mixed patterns.
*Proof.* On the realising set, w = ℓ(g,b) − ℓ(g,a) has sign pattern τ and p_A·w ≥ 0 ≥ p_B·w.
If p_A,i p_B,j < p_A,j p_B,i for all i ∈ P, j ∈ N, then p_B,i > 0 (i ∈ P) and p_A,j > 0
(j ∈ N), and with r_k = p_A,k/p_B,k ∈ [0,∞] we get max_P r < min_N r; pick c > 0 strictly
between. Then (p_A − c p_B)_i < 0 on P and > 0 on N, so (p_A − c p_B)·w < 0, contradicting
p_A·w ≥ 0 ≥ c p_B·w. For the last claim run R2 Theorem N with general pairs of kinds of advice: if all
mixed patterns occur, the u-pattern argument gives p_A = p_B = p; if p_j = 0, the realised
pattern with P = supp p makes B's advice strictly p-worse than A's; so p is interior, and
Lemma U gives A = B. ∎

**Theorem UN′ (PROVED, any n).** Theorem UN holds with (Nest) replaced by
(AllPat): T(A,B) = all mixed patterns.
*Proof.* Identical, with c(h) = ℓ^θ(g,b) − ℓ^θ(g,a) on each realising set and the splice on
Z′ ∩ {|g| < 1} for a non-null cone Z′ ⊆ {a_A ≠ a_B} (A, B coherent, so the difference set is a
cone); E's advice then changes along a.e. ray of Z′, so E is incoherent. ∎

### 5.2 Characterisation (the structure statement)
A **chart parametrisation** of a family 𝒰 ⊆ M is an onto map π : Δ → 𝒰 together with a
measurable penalty field ℓ(g,a) ∈ ℝ^n (a ∈ A(g)), coordinate i strictly increasing in world-i
rank, integrable envelope, such that for every p ∈ Δ the minimiser of p·ℓ(g,·) over A(g) is
a.e. unique and equals π(p)'s advice. Equivalently (R1 Prop 2.1 and its converse): for a.e. g
the partition p ↦ a_{π(p)}(g) of Δ is a vertex-respecting minimisation diagram of ≤ 3 affine
functions (half-planes for two-element advice ranges, three concurrent sectors for {+,0,−}), whose
cell boundaries are null in g for each fixed p.

**Theorem R_n (CHECKED).** Let L satisfy strict (G), (IB), (LA), (S), (C) on a decomposable domain M.
(a) If U_L admits a chart parametrisation, then U_L = U_add for the additive system ℓ, and that
system satisfies (LA), (S), (C) (v3 thm:general on decomposable domains, R1 Thm 2.2(S)).
(b) Conversely, if U_L = U_add for some strictly guiding additive (LA),(S),(C) system, then the
Bayes map satisfies the chart condition at every interior p (Lemma U; R1 Lemma 1.4, Thm 2.2(N)),
and at the vertices (R1 Lemma 1.5). At non-vertex boundary priors uniqueness can fail (R1
correction C1); the exact boundary condition is R1 Remark 2.3.
So, up to R1's boundary-tie gap, **"U_L is additively representable" ⇔ "U_L admits a chart
parametrisation"**. In n = 2 a chart parametrisation is exactly a continuous monotone path, and
R2 Theorem R shows that under (S) this is equivalent to the intrinsic, prior-free condition
"no strictly nested pair" = "no pair with T(A,B) = all mixed patterns".

### 5.3 What is proved for n ≥ 3
- Intrinsic necessary conditions on U_L for additive representability: Theorem PC (pairwise
  prior-compatibility of realised patterns), hence no (AllPat) pair, hence no (Nest) pair.
- For every sandwiched system (Theorem UN′), in every n: U_L has no (AllPat) pair. So the
  first intrinsic obstruction to additive representability is absent for all sandwiched
  systems, whatever the cardinality of the families.
- For finite lex at every world: no (AllPat) pair provided nested members are F-Bayes
  (Prop 4.2); Example 4.3 shows that proviso can fail for undominated models.
- "Additive at all but one world": if the exceptional world is sandwiched, Theorem UN′ applies.
  If it is a two-level lex world: R2 Theorem 6 (n = 2 only). For n ≥ 3 I expect R2 Theorem 6's
  iterated-support argument to give F-Bayes (only one world carries ε-terms, which is exactly
  what Example 4.3 needs to avoid), but I have not written it: CONJECTURE.

### 5.4 Why the n ≥ 3 analogue is not pairwise (remark; heuristic, not a theorem)
In n = 2 every pairwise-consistent family is a monotone path, and Theorem R's Step 5 builds the
penalties problem by problem from two switch points. In n ≥ 3 a chart parametrisation needs,
for each problem g, the *whole* set {p : π(p) gives a at g} to be a half-plane (or a sector of
three concurrent lines). This couples a continuum of members at once; R1 Thm 4.1 / NAL
thm:obstruction is an example of a failure of exactly this kind (ε-contamination with the
diagonal parametrisation) that no pairwise test sees: translates of one triangle are never
nested. I have not shown that some family satisfies all pairwise conditions (PC) yet admits no
chart parametrisation under *any* π, so "pairwise conditions are insufficient for n ≥ 3" is a
CONJECTURE. The honest n ≥ 3 target is therefore:

**Conjecture R_n.** Under strict (G), (IB), (LA), (S), (C) on a decomposable domain, U_L admits a chart
parametrisation. (For n = 2 this is Conjecture 1 via Theorem R; it is proved for additive and
sandwiched systems in n = 2, and for n ≥ 3 only its pairwise shadow (no AllPat pair) is proved
for sandwiched systems.)
Note: Conjecture R_n for n = 3 would reduce T1–T4 coverage by *any* (IB) system to additive
(measurable CPM) realisation, which is itself open (R1 §4).

## 6. Status

| Claim | Status |
|---|---|
| N1: nested members of U_L may be taken selected, at interior priors | PROVED |
| TJ: finitely-additive-generated ties ⇒ distinct members of C_L never tied at all worlds | PROVED |
| UN: sandwiched worlds (any families) ⇒ no (Nest) pair, any n | PROVED |
| UN′: same with (AllPat) | PROVED |
| UN2: n = 2, sandwiched ⇒ U_L additively representable | PROVED (with R2 Thm R) |
| X: cross-competitiveness (★) for a nested pair, any preorders, n = 2 | PROVED |
| X2: complete + fine region orders ⇒ Savage–Wakker probabilities proportional on R | CHECKED |
| 4.1: integration over ordered fields | PROVED |
| 4.2: finite lex, nested members F-Bayes ⇒ contradiction | PROVED |
| 4.3: undominated but not F-Bayes (two lex worlds, two-element advice ranges) | PROVED |
| 4.4: finite lex, nested pair ⇒ standard parts proportional on R | PROVED |
| Region-only domain admits no finite-lex nested counterexample | CONJECTURE |
| PC: realised patterns of two members of U_add are prior-compatible; no AllPat pair | PROVED |
| R_n: additive representability ⇔ chart parametrisation (boundary-tie gap as in R1 Rem 2.3) | CHECKED |
| Conjecture 1 (all (IB) systems, n = 2) | CONJECTURE (open) |
| Conjecture 1′ (finite lex both worlds, n = 2) | CONJECTURE (open; Example 4.3 removes the natural proof) |
| One two-level lex world + additive others, n ≥ 3, no AllPat | CONJECTURE |
| Pairwise conditions insufficient for n ≥ 3 | CONJECTURE |
| Conjecture R_n | CONJECTURE |

**Where a counterexample to Conjecture 1 must live (n = 2), combining R2, R3 and this note.**
At least one world is not sandwiched (UN), so it has a strict comparison invisible to all its
strictly guiding additive weak extensions. If the worlds are finite lex: both worlds carry
non-trivial ε-parts on the region (R2 Thm 6), the standard parts are proportional there
(Lemma 4.4), the nested pair is joined by a continuum of selected models (TJ), improvable
members sit on countably many primary levels (R2 Thm 7), and non-singleton advice ranges outside R1 ∪ R2 must be used
(conjectural region-only exclusion). The seed configuration is Example 4.3. For IRWAS/KPS-type
complete orders nothing beyond Lemma X is known.
