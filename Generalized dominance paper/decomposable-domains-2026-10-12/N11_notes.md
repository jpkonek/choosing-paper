# N11. BRIEF6 part (A): the reduction for coherent-preference rankings

13 Oct 2026. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof sketched or imported with its source),
**CONJECTURE**, **NUMERICS**. Script: `n11py/checks.py` (NUMERICS only; no proof depends on it).

Standing hypotheses (H): n worlds (n = 3 only where CCIBU is invoked); decomposable domain M (SC + closed in measure); strict (G),
(IB), (LA), (S) in LDG's preorder sense, (C), (E); T = T1 = D_K, K = (1−ε)u + εΔ ⊆ int Δ, T ∈ C_L, (LF) at T.
Fact 0 = R2 Fact 0 / LDG thm:kkm (valid for preorders): (a) every X ∈ M has a selected C with C ⪯_i X at every i;
(b) every undominated X is tied at every world with a selected model. Lemma IC = R11 Lemma IC (refereed C in R13):
T is competitive on Ω. Vertex lemma = DCE prop:ideal: C_{e_i} = W_i(M), the a.e.-unique world-i-best member of M.

Notation. Λ_i X := λ_i(·, a_X(·)) ∈ L^∞(H, μ) (the loss gamble; λ_i bounded, measurable, strictly increasing in world-i
rank on each advice range). A *state* is a positive normalised linear functional on L^∞(μ) (= a finitely additive probability
vanishing on μ-null sets). For a state P, Yosida–Hewitt: P = P^c + P^p with P^c = ρ_P μ (ρ_P ∈ L¹₊) and P^p purely
finitely additive. Stone picture: L^∞(μ) = C(K) (K hyperstonean), states = Radon probabilities on K, P^c = the normal
part, P^p = the singular part (carried by a meagre set); P^p itself splits into a non-atomic part and an atomic part
Σ a_j δ_{k_j} (point evaluations at points k_j ∈ K, i.e. {0,1}-valued "ultrafilter" charges).

Variants of the hypothesis (CP).
- **(CP-a)** (main): M_i a weak-* closed convex set of states; X ⪯_i Y ⇔ P(Λ_iY − Λ_iX) ≥ 0 for all P ∈ M_i.
- **(CP-s)** (Walley 1991 §3.7.7–3.7.9, strict preference): X ⪯_i Y ⇔ X = Y or [P̲_i(Λ_iY − Λ_iX) > 0, or
  Λ_iY − Λ_iX ≥ 0 a.e. and ≠ 0].
- **(CP-b)** (Walley 2000 §6): D_i a coherent set of desirable gambles on L^∞(μ) (D1–D4, "X > 0" read as ≥ 0 a.e.,
  > 0 on a non-null set); X ⪯_i Y ⇔ Λ_iY − Λ_iX ∈ D_i ∪ {0}.
(CP-s) is the special case D_i = {P̲_i > 0} ∪ {nonzero nonnegative} of (CP-b) (Walley 2000 eq. (8)).

---

## 0. Outcome

**Verdict.** The reduction is PROVED in a precisely delimited class, and the two gaps of BRIEF6 are resolved in the
sense that each is shown to be (i) closable under an explicit hypothesis that is automatic in the natural sub-cases and
(ii) not closable by the R11/R13 mechanism in general (explicit counterexamples at ranking level). The two gaps pull in
opposite directions: detection (gap 1) needs the purely finitely additive parts *kept* (only then does the aggregate
respect the ranking, (W)); separation (gap 2) needs them *tamed* (non-atomic) or *discarded*. The precise residual is
the atomic part of the singular charges.

**N11.1 (PROVED) Normal form of (CP-a).** (IB) and weak (G) hold automatically. Strict (G) holds iff P̄_i(f) > 0 for every
guidance-improvement difference f (f ≥ 0, f > 0 on a non-null set). Strict part: X ≺_i Y ⇔ P(f) ≥ 0 ∀P ∈ M_i and
P(f) > 0 for some P ∈ M_i (f = Λ_iY − Λ_iX). Every P ∈ M_i satisfies (W): X ⪯_i Y ⇒ P(Λ_iX) ≤ P(Λ_iY).

**N11.2 (PROVED) Integral reduction under countably additive detection.** Assume (H), (CP-a) and
 (D^CA) for each i, whenever X ≺_i Y some *countably additive* Q ∈ M_i has Q(Λ_iY − Λ_iX) > 0.
Then there is an integral, strictly guiding additive field ψ_i(X) = ∫ λ_i(g, a_X(g)) ρ_i(g) dμ, ρ_i ∈ L¹ (ρ_i > 0 a.e. on
problems whose advice range has ≥ 2 elements), on the **same** domain M, with ψ_i = Σ_k c_k Q_{i,k}∘Λ_i, Q_{i,k} ∈ M_i, such that:
(a) at every interior p the ψ-Bayes model is a.e. unique, coherent and in C_L; (b) B_{e_i} = W_i(M) = C_{e_i} is
coherent; (c) every boundary p has a coherent (selected) ψ-Bayes model; (d) T1 = B_{p_T} for some p_T ∈ int Δ.
For n = 3, CCIBU then makes ψ itself satisfy (LA), (S), (C) and vindicate T1 with (LF) on M. (D^CA) holds in
**Case CA** (every member of M_i countably additive), in particular for every M_i that is a closed convex set of
densities, and whenever M_i ∩ CA is weak-* dense in M_i in the detection sense.

**N11.3 (PROVED) Splice lemma: what survives with arbitrary charges.** Under (H) + (CP-a) only: for any choice P_i ∈ M_i
(one per world) let ψ^c_i(X) = P_i^c(Λ_iX) = ∫ Λ_iX ρ_{P_i} dμ. If C is L-competitive on S then no X has
ψ^c_i(X) < ψ^c_i(C) for all i ∈ S; hence C is ψ^c-Bayes at some π ∈ Δ_S. Consequently:
- every selected C_q makes a **Bayes choice** for the integral parts (supp π(q) ⊆ supp q), for every member choice;
- L-competitiveness on S implies competitiveness on S for L^c, the unanimity ranking of {P^c : P ∈ M_i};
- T1 is ψ^c-Bayes at some p_T ∈ Δ, and p_T ∈ int Δ whenever every ρ_{P_i} > 0 a.e. (possible iff
  (FS^c): the essential union of {ρ_P > 0}, P ∈ M_i, is a.e. all of the problems with a non-singleton advice range).
So the purely finitely additive parts can be **discarded in the separation step** (gap 2 is closed for T1 itself).

**N11.4 (PROVED) But they cannot be discarded in the coherence step.** (W) fails for integral parts in general: there is a
(CP-a) system satisfying all of (G), (IB), (LA), (S), (C) (CBOI Prop. example, M_i = {ν}, ν = μ/2 + η/2) and models
X ⪯_i Y with ν^c(Λ_iY − Λ_iX) < 0. Lemma K's step "C ⪯ B ⇒ ψ(C) ≤ ψ(B)" therefore needs the full charges.

**N11.5 (PROVED) Gap 1: countable detection.** (i) If M_i is weak-* separable (e.g. M_i ⊆ CA; M_i the closed convex hull
of a norm-separable set; M_i finitely generated) then a countable {P_{i,k}} ⊆ M_i detects every strict comparison at i
(condition (CD)). (ii) (CD) is NOT implied by (CP-a) + strict (G) + (IB): an explicit M_i (almost-disjoint family of
ultrafilter charges plus μ) on the U-domain (evaluable models: the measurable subsets of U = D_{K′}) has strict comparisons X ≺_i Y invisible to every countable
subfamily (and to every single member: no "relative interior" point exists). Whether (S) + (LA) + (C) + coverage force
(CD) is OPEN.

**N11.6 (PROVED) Gap 2: convexity for charges.** If the charges P_{i,k} are strongly non-atomic (no atomic part in the
Stone picture; condition (SN)), the closure of the attainable set R = {ψ(X) : X ∈ M} is convex (finitely additive
Lyapunov via Shapley–Folkman rounding; NUMERICS check). Atomic singular parts can make R nonconvex, and then the
separation step fails as a proof step: a weakly Pareto profile need not be Bayes (NUMERICS toy, N11.7).

**N11.7 (PROVED) Finitely additive reduction.** Assume (H), (CP-a), (CD) and (SN). Then ψ_i(X) := P*_i(Λ_iX),
P*_i = Σ_k c_k P_{i,k} ∈ M_i (a charge-valued additive field, one per world) is strictly guiding and:
(a′) every *attained* minimiser of p·ψ at interior p is a.e. unique, coherent and in C_L;
(b) the vertex minimiser W_i(M) is attained, unique, coherent;
(d) T1 is the (attained, unique) minimiser at some p_T ∈ int Δ.
NOT proved: attainment of inf p·ψ at other interior p (there is a structural reason it can fail: §5.4). CCIBU's converse
(ψ itself satisfies (S)) is not available for charges (it uses continuity in measure).

**N11.8 (the class that part (B) must exclude).** By N11.2/N11.7 part (B) must exclude:
- integral fields (when (D^CA) holds) — the class of R15, N5–N7, CONTAMINATION_NOGO;
- otherwise, **genuinely finitely additive fields** ψ_i = P*_i∘Λ_i with P*_i strongly non-atomic states on L^∞(μ),
  possibly with singular (purely finitely additive) parts concentrated on μ-small sets near ∂T1, and with the property
  (a′) only for attained minimisers (non-attainment at some interior weights must be allowed in (B)).
Fields with atomic singular parts are not reached by the reduction (the separation step fails), so for them the
reduction itself is incomplete, not (B).

**N11.9 (PROVED) Strict-preference variant (CP-s): clean integral reduction.** Under (H) + (CP-s) + (FS₁): some
countably additive Q_i ∈ M_i has density ρ_i > 0 a.e. on problems with a non-singleton advice range. Then the **single** member ψ_i = Q_i∘Λ_i
gives (a)–(d) of N11.2 (and, n = 3, CCIBU vindication), with no detection or convexity hypothesis and without using (C)
in Lemma K. Incomparabilities on the boundary {P̲_i = 0} are harmless. With a strictly positive strongly non-atomic
charge in place of Q_i, the N11.7 conclusions hold.

**N11.10 Walley-2000 variant (CP-b).** (PROVED) (G) strict and (IB) are automatic; M_i := {states ≥ 0 on D_i} is
non-empty and D_i ⊇ {P̲_i > 0}, so (CP-b) sits between (CP-s) and (CP-a) and every P ∈ M_i satisfies (W). Let
D_i^0 := D_i ∩ {f : P(f) = 0 ∀P ∈ M_i} ("invisible desirability").
- (PROVED) If D_i^0 = ∅ and countably many members of M_i strictly separate D_i (condition (CS); automatic from
  D_i^0 = ∅ + weak-* separability), the reduction holds: integral ψ if the separating family is countably additive
  (N11.2 conclusions), charge-valued under (SN) (N11.7 conclusions). Lemma K then needs no (C).
- If D_i^0 ≠ ∅ the ranking is genuinely non-Archimedean and no real additive field with (W) detects it. Under the
  representation hypothesis (LEX_m) (D_i lexicographic with m countably additive levels) the system is in R11's class
  𝓛_m: interior lex-Bayes models are unique, coherent, in C_L (R11 Prop LX = N9.5 for m = 2, PROVED there), vertices as
  usual. **Blocked** exactly at "T1 is lex-Bayes at some (non-standard) interior prior": lexicographic separation of a
  competitive point of the convex attainable set in ℝ^{nm}, which fails for undominated points in general (R5 Ex 4.3) and
  is rescued by (S) only on faces with I_v = Ω (R11 SF_n); this is R11 §5's CONJECTURE and N10's GAP on N9.9. Without
  (LEX_m), blocked earlier: a coherent D_i on L^∞(μ) need not have a finite lexicographic representation.

**N11.11 (PROVED) The user's worry (disagreement among complete additive rankings).** Harmless for the reduction
direction. The reduction never uses undominatedness that comes from disagreement: (S), Fact 0 and Lemma IC deliver
*competitiveness* and *unanimous* weak dominance (C ⪯_i X at a world i means every P ∈ M_i agrees), and every single
member P ∈ M_i respects unanimous comparisons (W). Models undominated only through disagreement are, by Fact 0(b), tied
at every world with a selected (competitive) model, so they add no new profiles. The single place where disagreement
enters is detection (whether ψ sees a strict comparison) — that is gap 1, not a protection mechanism for T1.
Disagreement can enlarge U_L but cannot put T1 in C_L for a reason the aggregate misses (§7).

---
## 1. Normal form and imported facts

**Prop 1.1 (N11.1; PROVED).** Under (CP-a):
- (i) ⪯_i is a preorder; (IB) holds; weak (G) holds.
- (ii) Strict part: X ≺_i Y iff, with f = Λ_iY − Λ_iX, P(f) ≥ 0 for all P ∈ M_i and P(f) > 0 for some P ∈ M_i.
- (iii) Strict (G) at i holds iff sup_{P∈M_i} P(f) > 0 for every f of the form Λ_iY − Λ_iX with Y pointwise
  (weakly) worse than X at i and strictly worse on a non-null set.
- (iv) (W) for every member: X ⪯_i Y ⇒ P(Λ_iX) ≤ P(Λ_iY) for every P ∈ M_i.

*Proof.* (i) Reflexive: f = 0. Transitive: P(Λ_iZ − Λ_iX) = P(Λ_iZ − Λ_iY) + P(Λ_iY − Λ_iX) by linearity. (IB): replacing
the common advice of X and Y on any set leaves f unchanged pointwise. Weak (G): if X is pointwise at least as good as Y
at i then f ≥ 0 a.e. (penalties increasing in rank), so P(f) ≥ 0 for every state P. (ii) "not Y ⪯_i X" means some P has
P(−f) < 0. (iii) Under the stated hypothesis f ≥ 0, so X ⪯_i Y; strictness is "some P(f) > 0" by (ii). (iv) is the
definition. ∎

**Fact 1.2 (Yosida–Hewitt with concentration; CHECKED, imported from CBOI lem:split and Pennanen–Perkkiö Thm 1).**
Every state P on L^∞(μ) is uniquely P = P^c + P^p with P^c countably additive, hence P^c = ρ_P μ (ρ_P ∈ L¹₊, Radon–
Nikodym, since P vanishes on μ-null sets), and P^p ≥ 0 purely finitely additive; and there are measurable Z_m with
μ(Z_m) → 0 and P^p(H ∖ Z_m) = 0. For countably many states P_k there is one common sequence: choose Z^k_m with
μ(Z^k_m) < 2^{−m−k} and P_k^p(H∖Z^k_m) = 0, and put Z_m = ∪_k Z^k_m (then μ(Z_m) ≤ 2^{−m} and
P_k^p(H∖Z_m) ≤ P_k^p(H∖Z^k_m) = 0). Replacing Z_m by ∩_{j≤m} Z_j makes the sequence decreasing (a finite intersection of
concentration sets is a concentration set).

Consequence used below: if h ∈ L^∞ then P^p(1_{H∖Z_m} h) = 0, because |P^p(1_A h)| ≤ ‖h‖_∞ P^p(A).

**Fact 1.3 (Lyapunov for integrals; CHECKED, R2 §1, CCIBU §1).** For finitely many finite measures ρ_iμ (ρ_i ∈ L¹₊) and
bounded λ_i, the set {(∫Λ_iX ρ_i dμ)_i : X ∈ M} is convex and compact.

---

## 2. Integral reduction under countably additive detection (N11.2)

**Theorem 2.1 (PROVED).** Assume (H), (CP-a) and (D^CA). Then the conclusions (a)–(d) of N11.2 hold; for n = 3 the field
ψ vindicates T1 on M with (LF).

*Proof.*
1. *Countable CA detecting family.* Let 𝒬_i = M_i ∩ CA, identified with a subset of L¹(μ) via Q ↦ ρ_Q. L¹(μ) is norm-
   separable (μ is a finite Borel measure on ℝ^n), so 𝒬_i has a countable norm-dense subset {Q_{i,k}}. For bounded f,
   |Q(f) − Q_{i,k}(f)| ≤ ‖f‖_∞ ‖ρ_Q − ρ_{i,k}‖_1. Hence, by (D^CA), whenever X ≺_i Y some Q_{i,k} has
   Q_{i,k}(Λ_iY − Λ_iX) > 0. This is R11's (R). R11's (W) holds for every Q_{i,k} ∈ M_i by Prop 1.1(iv).
2. *Aggregate.* ψ_i := Σ_k 2^{−k} Q_{i,k}∘Λ_i, i.e. ψ_i(X) = ∫ λ_i(g, a_X(g)) ρ_i(g) dμ with ρ_i = Σ 2^{−k} ρ_{i,k}
   (norm-convergent in L¹, ‖ρ_{i,k}‖_1 = 1). Envelope ‖λ_i‖_∞ ρ_i ∈ L¹.
3. *Strict guidance.* Let Q be a non-null set of problems whose advice ranges have ≥ 2 elements, and suppose ρ_i = 0 a.e. on Q.
   Let Y be W_i(M) with strictly worse advice from the advice range substituted on Q (measurable choice). Then W_i(M) ≺_i Y by strict
   (G), so step 1 gives some Q_{i,k}(Λ_iY − Λ_iW_i) > 0; but Λ_iY − Λ_iW_i vanishes off Q and ρ_{i,k} ≤ 2^k ρ_i vanishes on
   Q: contradiction. So ρ_i > 0 a.e. on problems with a non-singleton advice range and ψ_i has a strictly rank-increasing local penalty ρ_iλ_i.
4. The members Q_{i,k} need not be strictly guiding individually; R11's proofs of Lemma K and Theorem W (a)–(d) use only
   (W), (R), positivity of the weights, strict guidance of the aggregate, Fact 0, (C), Lemma IC and Lyapunov (Fact 1.3)
   (R13 §2.1–2.3, verdict CORRECT; R13 §2.4 for the weakly-guiding-members remark). They therefore apply verbatim and give
   (a)–(d) on the same domain M.
5. For n = 3, (a), (b) and K ⊆ int Δ are the hypotheses of CCIBU Thm 1 (integrable envelopes, a.e.-strict rank increase,
   unique coherent interior Bayes models), which gives (LA), (S), (C) for ψ; T1 = B_{p_T} with p_T interior, hence
   T1 ∈ C_ψ; M is unchanged, so (LF) is kept (CCIBU Cor. 5 argument). ∎

**Remarks 2.2.**
- *Case CA* (every member of M_i countably additive) satisfies (D^CA) trivially. This includes every credal set of
  densities that is weak-* closed (equivalently weakly compact, i.e. uniformly integrable, in L¹).
- Theorem 2.1 is R11 Thm W + R13 Prop S applied to the family M_i ∩ CA; the only new point is that (CP-a) worlds are
  sandwiched by their CA members exactly when (D^CA) holds.
- (D^CA) says that purely finitely additive members never decide a strict comparison alone. It fails in the CBOI
  example (M_i = {ν}, ν not CA), where nevertheless the integral field with costs ℓ_i and measure μ has the same Bayes
  models D_{{p}} (§4). So (D^CA) is sufficient, not necessary, for an integral reduction.

---

## 3. The splice lemma: what survives with arbitrary charges (N11.3)

**Lemma 3.1 (PROVED).** Assume (CP-a) on a decomposable domain. Let S ⊆ Ω be non-empty, C ∈ M competitive on S for L, and for each
i ∈ S let P_i ∈ M_i be arbitrary, with ψ^c_i(X) := P_i^c(Λ_iX) = ∫ Λ_iX ρ_{P_i} dμ. Then there is no X ∈ M with
ψ^c_i(X) < ψ^c_i(C) for every i ∈ S.

*Proof.* Suppose X is such a model. Take a common concentration sequence Z_m for the finitely many P_i^p (Fact 1.2).
Let X_m be C on Z_m and X off Z_m; X_m ∈ M since M is closed under splicing. Then Λ_iX_m − Λ_iC = 1_{H∖Z_m}(Λ_iX − Λ_iC),
so for i ∈ S
 P_i(Λ_iX_m − Λ_iC) = ∫_{H∖Z_m} (Λ_iX − Λ_iC) ρ_{P_i} dμ + P_i^p(1_{H∖Z_m}(Λ_iX − Λ_iC))
 = ∫_{H∖Z_m} (Λ_iX − Λ_iC) ρ_{P_i} dμ → ψ^c_i(X) − ψ^c_i(C) < 0
(the second term vanishes by Fact 1.2; dominated convergence with envelope 2‖λ_i‖_∞ρ_{P_i}). Fix m so large that all
|S| limits are negative. Then for every i ∈ S, P_i(Λ_iX_m − Λ_iC) < 0, so C ⪯_i X_m fails. This contradicts
competitiveness of C on S. ∎

**Corollary 3.2 (PROVED).**
- (a) C competitive on S ⇒ C is ψ^c-Bayes at some π ∈ Δ_S (π·ψ^c(C) ≤ π·ψ^c(X) for every X ∈ M).
- (b) Every selected C_q makes a Bayes choice for ψ^c (LDG §B, "makes Bayes choices"): π(q) can be taken with
  supp π(q) ⊆ supp q. This holds for **every** choice of members P_i ∈ M_i.
- (c) C competitive on S for L ⇒ C competitive on S for L^c, where X ⪯^c_i Y :⇔ P^c(Λ_iY − Λ_iX) ≥ 0 ∀P ∈ M_i.
- (d) T1 is ψ^c-Bayes at some p_T ∈ Δ; if ρ_{P_i} > 0 a.e. for every i, then p_T ∈ int Δ. Members with ρ_{P_i} > 0 a.e.
  exist iff (FS^c) holds (take P_i = Σ_k 2^{−k}P_{i,k} for countably many members whose supports {ρ > 0} have
  essential union equal to the problems with a non-singleton advice range; such a countable family exists because the measure algebra of μ
  satisfies the countable chain condition; the sum lies in M_i, a norm-closed convex set).

*Proof.* (a) Restrict to the coordinates in S. By Fact 1.3 the set R^c_S = {ψ^c_S(X)} is convex; by Lemma 3.1 it does not meet
the open convex set ψ^c_S(C) − (0,∞)^S. Separation gives π ≥ 0, π ≠ 0, with π·x ≥ π·ψ^c_S(C) on R^c_S; normalise.
(b) Selected models are competitive on supp q by (S). (c) If C ⪯^c_i X failed for every i ∈ S, pick P_i ∈ M_i with
P_i^c(Λ_iX − Λ_iC) < 0 and apply Lemma 3.1 to these finitely many members. (d) Lemma IC makes T1 competitive on Ω; apply (a).
If S = supp p_T ≠ Ω, the model X of Lemma IC for this S (valid for any proper non-empty S since K ⊆ int Δ; R13 §1.2) is
pointwise strictly better than T1 at every i ∈ S on a non-null V′ ⊆ N and equal elsewhere; ρ_{P_i} > 0 a.e. gives
ψ^c_i(X) < ψ^c_i(T1) for i ∈ S, so p_T·ψ^c(X) < p_T·ψ^c(T1): contradiction. ∎

**Reading.** In the separation step the purely finitely additive parts can be discarded: competitiveness is
robust under the splice, because a finite set of members always has a common μ-small concentration set. This closes gap
(2) *for T1 and for each selected model individually*. It does not give coherence of the interior ψ^c-Bayes family:
Corollary 3.2(b) says each selected model is ψ^c-Bayes somewhere, not that each ψ^c-Bayes model is selected. That converse
is Lemma K, which needs (W) (§4). Also (d) is close to vacuous on its own (R11 Lemma V: T1 is Bayes for *some* field
anyway); its value is that the field is built from L.

---
## 4. The pure parts cannot be discarded in the coherence step (N11.4)

**Prop 4.1 (PROVED).** There is a (CP-a) system satisfying (G) strict, (IB), (LA), (S), (C) on the all-model domain (any
n ≥ 2), with M_i = {ν} for every i, and models X, Y with Y ⪯_i X (indeed Y ≺_i X) but ν^c(Λ_iX − Λ_iY) < 0.

*Proof.* CBOI Prop. prop:example: g = Rθ, t = F(R) uniform and independent of θ; η(A) = lim_{m→𝒰} m μ(A ∩ {t < 1/m}) for a
non-principal ultrafilter 𝒰; ν = μ/2 + η/2; costs ℓ_i(g, ·) = (0, ¾b_i, b_i, 2b_i) on (good, silent, bad, contradictory),
b_i = |g_i|/‖g‖. CBOI proves (G), (IB), (LA), (S), (C) with C_p = D_{{p}}. This is (CP-a) with M_i = {ν}, λ_i = ℓ_i
(bounded). Here ν^c = μ/2 (η is purely finitely additive: it gives mass 1 to every {t < 1/m}), and η agrees with μ on
functions of θ alone.
Let D_i be the world-i ideal, Q a non-null mixed cone, and put a := (3/8)∫_Q b_i dμ > 0.
- X := D_i silenced on Q ∩ {t < 1/m}. Then Λ_iX − Λ_iD_i = ¾ b_i 1_{Q∩{t<1/m}}, and
  ν(Λ_iX − Λ_iD_i) ≥ ½ η(¾ b_i 1_Q 1_{t<1/m}) = ½ η(¾ b_i 1_Q) = a (η is concentrated on {t < 1/m}; b_i1_Q depends on θ).
- Y := D_i silenced on S ⊆ Q ∩ {t > 1/2} with 0 < (3/8)∫_S b_i dμ < a. Then η(S) = 0 and ν(Λ_iY − Λ_iD_i) = (3/8)∫_S b_i dμ < a.
So ν(Λ_iX − Λ_iY) > 0, i.e. Y ≺_i X. But ν^c(Λ_iX − Λ_iY) = (3/8)[∫_{Q∩{t<1/m}} b_i dμ − ∫_S b_i dμ] < 0 once
m is large. ∎

**Consequence.** R11 Lemma K's first step (Fact 0(a) C ⪯ B, then (W) gives ψ(C) ≤ ψ(B)) is unavailable for an integral
field built from the CA parts: Fact 0 delivers *L*-weak dominance, which bounds the full charges, not their CA parts. With
ψ^c alone the argument shows only: some selected C is ψ^c-competitive (Cor 3.2), not that a given ψ^c-Bayes model B is
L-tied to a selected one. A ψ^c-Bayes model B is fixed μ-a.e. by pointwise minimisation, while the pure parts evaluate B
"at μ-small concentration sets", where B may be L-improvable at no ψ^c-cost; so B may be L-dominated, and then
nothing makes it coherent. (In the CBOI system itself this does not happen: the ψ^c-Bayes models are again D_{{p}}, because
the cost and coherent models depend on θ only. The failure is of the mechanism, not a counterexample to the reduction.)

So: **to run Lemma K one must keep the full charges** (§5); **to run the separation step one may drop them** (§3). A
reduction producing *one* field must reconcile the two.

---

## 5. Charge-valued fields: detection, convexity, the finitely additive reduction

### 5.1 Gap 1: countable detection (N11.5)

**Condition (CD) at world i.** There are countably many P_{i,k} ∈ M_i such that X ≺_i Y implies P_{i,k}(Λ_iY − Λ_iX) > 0 for
some k. (Only the pairs (selected C, attained minimiser B) are used in Lemma K; we state it for all pairs.)

**Prop 5.1 (PROVED).** If M_i is weak-* separable then (CD) holds at i. M_i is weak-* separable in each of the cases:
M_i ⊆ CA; M_i is the weak-* closure of a norm-separable set (e.g. the closed convex hull of countably many states, or of a
set of densities together with countably many charges); M_i finitely generated.

*Proof.* Let {P_k} be weak-* dense in M_i. If X ≺_i Y then some P ∈ M_i has P(f) > 0, f = Λ_iY − Λ_iX ∈ L^∞; the set
{P′ ∈ M_i : P′(f) > 0} is weak-* open in M_i and non-empty, so it contains some P_k. Cases: a norm-dense subset is
weak-* dense; L¹(μ) is norm-separable and every subset of a separable metric space is separable; rational convex
combinations of a countable generating set are weak-* dense in its closed convex hull (closed convex hull = weak-* closure
of the convex hull). ∎

**Prop 5.2 (PROVED). (CD) is not implied by (CP-a) + strict (G) + (IB).** On the U-domain M_U
(U = D_{K′}, error-indicator encoding Λ_iX = 1_{E_i(X)}, BRIEF6) there is a weak-* closed convex set M_i of states such that
strict (G) holds at i, and for every countable {P_k} ⊆ M_i there are X ≺_i Y with P_k(Λ_iY − Λ_iX) = 0 for all k. In
particular no single member of M_i detects every strict comparison (no "relative-interior" point exists).

*Proof.* Partition U ∩ P_i into non-null measurable sets B_1, B_2, … with μ(B_1) > ½μ(U ∩ P_i), where P_i = U ∩ {h_i > 0}
(world-i ideal; an error on h ∈ P_i is silence). Let {A_α : α < 𝔠} be an almost-disjoint family of infinite subsets of
{2, 3, …}, choose free ultrafilters 𝒰_α ∋ A_α, and set
 P_α(f) := lim_{n→𝒰_α} μ(B_n)^{−1} ∫_{B_n} f dμ.
Each P_α is a state on L^∞(μ), P_α(1_{B_n}) = 0 for every n, and with Y_β := ∪_{n∈A_β} B_n: P_β(Y_β) = 1, and
P_α(Y_β) = 0 for α ≠ β (A_α ∩ A_β is finite, so A_β ∉ 𝒰_α). Let C_0 be the weak-* closed convex hull of {P_α} and
M_i := conv({μ̄} ∪ C_0), μ̄ = μ/μ(H) (convex hull of two weak-* compact convex sets: compact, convex, closed).
- Strict (G): μ̄ ∈ M_i detects every pointwise improvement.
- Every Q ∈ C_0 vanishes on every B_n (closed under convex combinations and weak-* limits), hence on finite unions; so
  Q(Y_β ∩ Y_γ) = 0 for β ≠ γ, and finite additivity gives Σ_{β∈F} Q(Y_β) ≤ 1 for finite F. Hence {β : Q(Y_β) > 0} is
  countable.
- Given P_k = t_kμ̄ + (1−t_k)Q_k (k ∈ ℕ), choose β with Q_k(Y_β) = 0 for all k. Let G ⊆ Y_β have μ(G ∩ B_n) = ½μ(B_n) for
  n ∈ A_β, and W ⊆ B_1 with μ(W) = μ(G) (possible since μ(G) ≤ ½μ(U∩P_i) < μ(B_1)). Let X have error set exactly W
  (silence on W, ideal elsewhere) and Y have error set exactly G. Both lie in M_U. f := Λ_iY − Λ_iX = 1_G − 1_W.
- For every P = tμ̄ + (1−t)Q ∈ M_i: μ̄(f) = 0 and Q(f) = Q(G) − Q(W) = Q(G) ≥ 0, so X ⪯_i Y; and P_β(f) = P_β(G) = ½ > 0
  (averages of 1_G over B_n equal ½ for n ∈ A_β ∈ 𝒰_β). So X ≺_i Y.
- P_k(f) = t_k·0 + (1−t_k)(Q_k(G) − Q_k(W)) = 0, since Q_k(G) ≤ Q_k(Y_β) = 0 and Q_k(W) ≤ Q_k(B_1) = 0. ∎

*Scope.* Prop 5.2 is a statement about single-world rankings. I have not checked whether such an M_i can occur in a system
with (S), (LA), (C) covering T1. **CONJECTURE N11.A (open):** (S) + (C) + coverage force (CD) on the pairs used by Lemma K.
(Heuristic for: CBOI thm:blind shows that closed choice punishes criteria that live on arbitrarily small sets; the
undetectable comparisons in Prop 5.2 are carried by such criteria.)

### 5.2 Gap 2: convexity of the attainable set for charges (N11.6)

**Definition.** A state P is *strongly non-atomic* (SN) if for every ε > 0 there is a finite measurable partition of H into
sets A_j with P(1_{A_j}) < ε. CA states are SN (μ atomless, single ρ ∈ L¹ uniformly integrable). Point-evaluation
(ultrafilter, {0,1}-valued) states are not. (CHECKED, sketch: SN ⇔ the Radon representative on the Stone space K has no
atoms; compactness and zero-dimensionality of K give one direction, an atom gives the other.)

**Prop 5.3 (PROVED).** Let ψ_i = P*_i∘Λ_i with each P*_i SN (i = 1..n). Then cl R, R = {ψ(X) : X ∈ M}, is convex.

*Proof.* Let X, Y ∈ M, t ∈ (0,1). For measurable A let X_A be X on A and Y off A (X_A ∈ M) and
m(A) := ψ(X_A) − ψ(Y) = (P*_i(1_A(Λ_iX − Λ_iY)))_i, a bounded ℝ^n-valued charge. Let c := max_i‖Λ_iX − Λ_iY‖_∞ and ε > 0.
By SN (common refinement of n partitions) choose a partition A_1..A_N with P*_i(A_j) < ε for all i, j, so ‖m(A_j)‖_∞ < cε.
The set F = {s ∈ [0,1]^N : Σ_j s_j m(A_j) = t m(H)} contains s = (t,…,t), so it is a non-empty polytope; let s* be a vertex.
At most n coordinates of s* lie in (0,1): otherwise the vectors m(A_j) with fractional s*_j are linearly dependent in ℝ^n,
and moving s* along a dependency in both directions stays in F, contradicting extremality. Let A = ∪{A_j : s*_j = 1}. Then
‖m(A) − t m(H)‖_∞ ≤ n c ε. Hence tψ(X) + (1−t)ψ(Y) = ψ(Y) + t m(H) ∈ cl R. So cl R contains every convex combination
of two points of R, and by approximation of two points of cl R by points of R, cl R is convex. ∎ (NUMERICS: `n11py/checks.py`
(1) confirms ≤ n fractional coordinates and the rounding bound.)

**Remark 5.4 (atoms; PROVED as stated).** If some P*_i has an atomic part a·δ_k (k ∈ K, a > 0), splicing cannot split it:
for every A, δ_k(1_A) ∈ {0, 1}. The attainable set then has the form cl R = cl R^{na} + R^{at}, with R^{na} convex (the
non-atomic parts, Prop 5.3) and R^{at} a set of "atom choices" (one kind of advice from the advice range per atom), which can be non-convex.
A profile can then be weakly Pareto in R and not minimise p·x over R for any p ∈ Δ. NUMERICS (toy, `n11py/checks.py` (2)):
R = disc((2,2),1) + {(0,0), (1.5,−1)}; the point (1.000, 1.996) is weakly Pareto and unsupported. So for atomic charges the
separation step of R11 Thm W(d) fails as a proof step. (Whether T1 can actually be in this situation in a system satisfying
all axioms is not settled.)

### 5.3 The finitely additive reduction (N11.7)

**Theorem 5.5 (PROVED).** Assume (H), (CP-a), (CD) with members P_{i,k}, and (SN) for each P_{i,k}. Let
P*_i := Σ_k 2^{−k}P_{i,k} (∈ M_i; SN) and ψ_i := P*_i∘Λ_i. Then:
- (0) ψ_i is strictly guiding: Λ_iX ≤ Λ_iY a.e. with strict inequality on a non-null set ⇒ ψ_i(X) < ψ_i(Y); and (W) holds.
- (a′) if p ∈ int Δ and B ∈ M attains inf_M p·ψ, then B is coherent and in C_L, and every other attaining model equals B a.e.
- (b) for each i, W_i(M) uniquely attains min ψ_i, and W_i(M) = C_{e_i} is coherent.
- (c) if B attains inf p·ψ at a boundary p, some selected (coherent) C also attains it, with ψ(C) ≤ ψ(B).
- (d) T1 attains inf p_T·ψ for some p_T ∈ int Δ, and is the unique such model.

*Proof.* (0) Strict (G) of L gives X ≺_i Y, and (CD) gives some P_{i,k}(Λ_iY − Λ_iX) > 0; all other terms are ≥ 0. (W) for
each P_{i,k} (Prop 1.1(iv)) sums to (W) for ψ_i (norm-convergent series).
(a′) *Lemma K for charges.* Fact 0(a) gives a selected C with C ⪯_i B at every i. By (W), ψ_i(C) ≤ ψ_i(B); since B attains
the infimum and p is interior, ψ_i(C) = ψ_i(B) for every i. With f_i := Λ_iB − Λ_iC, every P_{i,k}(f_i) ≥ 0 and
Σ_k 2^{−k}P_{i,k}(f_i) = 0, so every P_{i,k}(f_i) = 0. By (CD), C ≺_i B fails; with C ⪯_i B this gives C ~_i B. (C) puts B in
C_L; B is coherent.
*Uniqueness.* Let B, B′ attain, differing on a non-null Z. Both are coherent, so Z is a cone mod null sets. For any
measurable A let E_A be B′ on A, B off A, and E′_A the complementary splice. Pointwise Λ_iE_A + Λ_iE′_A = Λ_iB + Λ_iB′,
so by linearity p·ψ(E_A) + p·ψ(E′_A) = 2 inf; both are ≥ inf, so both attain. Take A = Z ∩ {|g| < 1}: E_A attains, hence is
coherent by the previous step, but it is not a.e. a cone (R2 Lemma U / R1 Lemma 1.4(ii)): contradiction.
(b) Λ_iW_i ≤ Λ_iX pointwise for every X ∈ M, so W_i attains min ψ_i; any X ≠ W_i on a non-null set has ψ_i(X) > ψ_i(W_i)
by (0). Coherence: the vertex lemma (strict (G) + (S)) gives C_{e_i} = W_i(M).
(c) Fact 0(a) and (W).
(d) Lemma IC: T1 is competitive on Ω. With (W): for every X some i has ψ_i(T1) ≤ ψ_i(X), so R misses ψ(T1) − (0,∞)^n,
and so does cl R (an open set meeting cl R meets R). By Prop 5.3 cl R is convex; separation gives p_T ∈ Δ with
p_T·ψ(T1) ≤ p_T·x on cl R, so T1 attains. If S = supp p_T ≠ Ω, the Lemma-IC model X for S satisfies X ≺_i T1 at each i ∈ S
(strict (G)), so ψ_i(X) < ψ_i(T1) for i ∈ S by (0), and p_T·ψ(X) < p_T·ψ(T1): contradiction. Uniqueness by (a′). ∎

### 5.4 Attainment at other interior weights (why (a′) is the honest statement)

**Prop 5.6 (PROVED).** Let ψ_i = P*_i∘Λ_i, p ∈ int Δ, and write P*_i = ρ_iμ + π_i (Fact 1.2) with a common concentration
sequence Z_m for π_1..π_n. Let a := min_X Σ_i p_i∫Λ_iXρ_i dμ, attained exactly by the pointwise minimisers of
Σ_i p_iρ_i(g)λ_i(g,·), and b := inf_X Σ_i p_i π_i(Λ_iX). Then inf_M p·ψ = a + b, and it is attained iff some pointwise
minimiser B^c of the CA part also satisfies Σ_i p_iπ_i(Λ_iB^c) = b.

*Proof.* "≥" is termwise. For "≤": take A_m with pure value < b + 1/m and let X_m be A_m on Z_m and B^c off Z_m; the pure
value of X_m equals that of A_m (π_i(H∖Z_m) = 0), and its CA value tends to a. Attainment: X attains a + b iff it attains
both a and b; attaining a forces X to be a pointwise CA-minimiser a.e. (where Σp_iρ_i > 0, i.e. a.e. if ρ_i > 0), and
π_i(Λ_iX) depends only on X mod null sets. ∎

So for genuinely finitely additive ψ, attainment at p requires the CA-optimal advice to be also optimal for the singular
parts, which are evaluated "at the concentration sets". Nothing in L's axioms (as far as I can see) forces this at every
interior p; Fact 0 only gives selected models with p·ψ(C) arbitrarily close to the infimum. Theorem 5.5 secures attainment
where it is needed for T1 (p_T) and at the vertices. **Consequence for part (B):** the class to be excluded is "charge-valued,
strictly guiding fields with SN members such that every attained interior minimiser is unique and coherent, the vertex
minimisers are the coherent ideals, and T1 is the attained minimiser at an interior weight". When ψ is integral (π_i = 0),
attainment is automatic and this is BRIEF2's single-target additive problem.

### 5.5 What kind of penalties ψ must be allowed (N11.8)

- If (D^CA) holds: ψ integral (ordinary densities ρ_i > 0 a.e.). Part (B) for integral fields suffices.
- If only (CD) + (SN) hold: ψ_i = P*_i∘Λ_i with P*_i a strongly non-atomic state on L^∞(μ), possibly with a singular part
  π_i concentrated on μ-small sets (e.g. near ∂T1, near the coordinate crossings, or "at radius 0 or ∞"). On coherent models
  (cones) a singular part concentrated at radius 0 or ∞ acts like an ordinary density on directions (CBOI); one concentrated
  near a ray or a boundary arc acts like a lower-dimensional measure on directions (a non-integrable "kink" weight). Part (B)
  must therefore exclude these as well; R15's (DF)/(ND) failures and BRIEF6's "kink mimicking" are exactly where such
  weights would enter.
- Atomic singular parts are not reached: Theorem 5.5(d) fails as a proof (Remark 5.4). For L with such members the reduction
  is open, independently of (B). **CONJECTURE N11.B:** under (H), atomic singular parts of members of M_i are inessential
  (removable without changing the strict comparisons used by Lemma K and IC), by a CBOI thm:blind-type argument.

---
## 6. Walley's other variants

### 6.1 Strict preference (CP-s) (N11.9)

Write D^+_i := {f : P̲_i(f) > 0} ∪ {f ≥ 0 a.e., f ≠ 0}, P̲_i(f) = min_{P∈M_i} P(f) (attained: M_i weak-* compact).

**Prop 6.1 (PROVED).** Under (CP-s): ⪯_i is a partial order (ties are equalities mod null on problems with a non-singleton advice range); (IB) and
strict (G) are automatic; every P ∈ M_i satisfies (W).

*Proof.* D^+_i is a convex cone: P̲ is superadditive and positively homogeneous; P̲(f) > 0 and g ≥ 0 give P̲(f+g) > 0; two
non-zero non-negative gambles sum to one. It contains no pair f, −f: P̲(f) + P̲(−f) ≤ 0; f ≥ 0, f ≠ 0 gives P̲(−f) ≤ 0
and −f ∉ {≥ 0}. So D^+_i ∪ {0} is a pointed convex cone, which makes ⪯_i reflexive, transitive and antisymmetric
(Λ_iX = Λ_iY a.e. iff X = Y a.e. on problems with a non-singleton advice range, by strict rank increase). (IB): the relation depends on f only.
Strict (G): a pointwise improvement gives f ≥ 0, f ≠ 0, so f ∈ D^+_i and −f ∉ D^+_i ∪ {0}. (W): f ∈ D^+_i ⇒ P(f) ≥ P̲(f) > 0
or f ≥ 0. ∎

**Theorem 6.2 (PROVED).** Assume (H), (CP-s) and (FS₁): some countably additive Q_i ∈ M_i has density ρ_i > 0 a.e. on
problems with a non-singleton advice range. (Equivalently, the CA members of M_i have essential union of supports equal to the problems
with a non-singleton advice range: then a countable combination Σ2^{−k}Q_{i,k} ∈ M_i works.) Then ψ_i := Q_i∘Λ_i (one member per world, integral)
satisfies (a)–(d) of N11.2, and for n = 3 vindicates T1 on M with (LF).

*Proof.* (W) by Prop 6.1; strict guidance by ρ_i > 0. *Lemma K without detection or (C).* Let p be interior and B
ψ-p-Bayes (a pointwise minimiser; exists since ψ is integral). Fact 0(a) gives a selected C with C ⪯_i B for all i, so
f_i := Λ_iB − Λ_iC ∈ D^+_i ∪ {0}. (W) gives ψ_i(C) ≤ ψ_i(B), and p interior gives equality, i.e. Q_i(f_i) = 0. If
P̲_i(f_i) > 0 then Q_i(f_i) > 0; if f_i ≥ 0, f_i ≠ 0, then Q_i(f_i) = ∫f_iρ_i > 0. So f_i = 0 and B = C a.e.: B is a selected
model, hence coherent. Uniqueness: all interior p-Bayes models are pointwise minimisers, splices of two of them are
again minimisers, all are coherent, and R2 Lemma U gives the contradiction as in R11 Thm W(a). (b): W_i(M) is the unique
ψ_i-minimiser (strict guidance) and equals C_{e_i}. (c): Fact 0(a) and (W). (d): Lemma IC + (W) + Lyapunov (Fact 1.3) +
separation, and the IC push to the interior as in Cor 3.2(d). For n = 3, CCIBU as in Theorem 2.1 step 5. ∎

*Reading.* Under (CP-s) the boundary gambles {P̲_i = 0} are *incomparable*, not tied, so no detection problem arises:
Fact 0 can only deliver weak dominators that are either equal or strictly better for every member of M_i. The massive
incomparability of (CP-s) enlarges U_L but is invisible to the reduction (§7). If no CA member has full support but a
strictly positive SN charge Q_i ∈ M_i exists, the same proof gives the conclusions of Theorem 5.5 (with attainment as in
§5.4).

### 6.2 Walley 2000: coherent sets of desirable gambles (CP-b) (N11.10)

**Prop 6.3 (PROVED).** Let D_i be coherent (D1–D4) on L^∞(μ), and M_i := {states P : P(f) ≥ 0 ∀f ∈ D_i}. Then:
- (i) (IB) and strict (G) hold for (CP-b); ⪯_i is a partial order.
- (ii) M_i ≠ ∅, cl D_i = {f : P(f) ≥ 0 ∀P ∈ M_i}, and D_i ⊇ {f : P̲_i(f) > 0}. Hence every P ∈ M_i satisfies (W), and
  (CP-s) ⊆ (CP-b) ⊆ (CP-a)-weak in the sense: X ⪯^{(CP-s)}_i Y ⇒ X ⪯^{(CP-b)}_i Y ⇒ X ⪯^{(CP-a)}_i Y for the same M_i.

*Proof.* (i) As in Prop 6.1, using D3–D4 (convex cone), D1 (0 ∉ D_i, so f, −f ∈ D_i is impossible) and D2.
(ii) Suppose f ∈ D_i with ess sup f ≤ −δ < 0 and put g := −f − δ·1 ≥ 0. If g ≠ 0 then g ∈ D_i (D2), δ·1 ∈ D_i (D2),
and 0 = f + δ·1 + g ∈ D_i (D4), contradicting D1; if g = 0 then 0 = f + δ·1 ∈ D_i, the same contradiction. So the convex
cone D_i misses the non-empty open convex cone {ess sup < 0}. Hahn–Banach gives φ ∈ (L^∞)*, φ ≠ 0, with φ ≥ 0 on D_i and
φ ≤ 0 on {ess sup < 0}; the latter makes φ positive, so φ(1) > 0 and φ/φ(1) ∈ M_i. The bipolar theorem for the
norm-closed convex cone cl D_i (whose dual cone consists of positive functionals, since cl D_i ⊇ L^∞_+) gives
cl D_i = {f : P(f) ≥ 0 ∀P ∈ M_i}. If P̲_i(f) = δ > 0 then the ball of radius δ around f lies in cl D_i, so
f ∈ int cl D_i = int D_i (D_i is convex with non-empty interior ⊇ {ess inf > 0}), so f ∈ D_i. The chain of inclusions
follows: D^+_i ⊆ D_i ⊆ {P̲_i ≥ 0}. ∎

Define the *invisible part* D^0_i := {f ∈ D_i : P(f) = 0 ∀P ∈ M_i}.

**Theorem 6.4 (PROVED).** Assume (H), (CP-b), and (CS): there are countably many P_{i,k} ∈ M_i such that every f ∈ D_i has
P_{i,k}(f) > 0 for some k. Let ψ_i := Σ2^{−k}P_{i,k}∘Λ_i.
- If all P_{i,k} are countably additive, (a)–(d) of N11.2 hold (n = 3: CCIBU vindication).
- If all P_{i,k} are SN, the conclusions of Theorem 5.5 hold.
(CS) implies D^0_i = ∅, and conversely D^0_i = ∅ + weak-* separability of M_i imply (CS) (Prop 5.1's argument).

*Proof.* As Theorem 6.2 / Theorem 5.5, with this Lemma K: C ⪯_i B gives f_i ∈ D_i ∪ {0}; ψ-equality gives
P_{i,k}(f_i) = 0 for every k; by (CS), f_i ∉ D_i, so f_i = 0 and B = C. Strict guidance: non-negative non-zero gambles lie
in D_i, so they are detected. ∎

**When D^0_i ≠ ∅ (genuinely non-Archimedean).** No functional that is non-negative on D_i sees f ∈ D^0_i (such functionals are
multiples of members of M_i). So no real additive field obeying (W) can carry the comparisons "f ∈ D^0_i"; Lemma K for any
such field can yield ψ-ties C, B with C ≺_i B, and B need not be coherent. The natural reduction target is lexicographic.

(LEX_m): there are countably additive states Q^1_i, …, Q^m_i with D_i = {f : (Q^1_i(f), …, Q^m_i(f)) >_lex 0}, the union of
the supports of the densities being all problems with a non-singleton advice range (so D2 holds; the set is a coherent D_i).

**Prop 6.5 (PROVED, restricted class).** Under (H), (CP-b), (LEX_m): for every real p ∈ int Δ, the pointwise lex minimiser B_p
of (p·Q^1∘Λ, …, p·Q^m∘Λ) is a.e. unique, coherent and selected; vertices as usual.

*Proof.* R11 Prop LX's proof (refereed C, R13 §4.2), with one simplification: Fact 0(a) gives a selected C ⪯ B_p, hence
Λ_iB_p − Λ_iC ∈ D_i ∪ {0}; minimality and p ≫ 0 force all levels equal; a gamble in D_i has a positive lex vector, so the
difference is 0 and C = B_p. Uniqueness by the splice argument at every level. ∎

**Where the 2000 reduction is blocked (precise).**
1. *Representation.* A coherent D_i on L^∞(μ) need not satisfy (LEX_m) for any m: Walley 2000 Example 7 (D_1 ≠ D_2 with the same M)
   shows that D carries boundary information beyond M; on finite spaces a coherent D is in general only an *intersection* of
   lexicographic ones (the maximal coherent sets; literature result, not re-proved here), and on L^∞(μ) the levels of a
   lexicographic piece need be neither finitely many nor countably additive. For intersections, one needs a
   lexicographic analogue of R13 Prop S (countable detection at every level, with a common face structure); I have none.
2. *T1 in the lex family.* Under (LEX_m) the separation step must produce a non-standard interior prior q = t + εu + … at
   which T1 is lex-Bayes. Lemma IC gives competitiveness; level 1 separates (Lyapunov) and gives t ∈ Δ with T1 ∈ argmin
   t·Q^1∘Λ; but the push to int Δ uses strict guidance of level 1, which (LEX_m) does not give (a level-1 member may be blind
   on the IC set), and the level-2 separation inside the face is the lexicographic separation problem of R11 §5 (CONJECTURE
   there), which fails for undominated points in general (R5 Ex 4.3) and is rescued by (S) only on interior faces with
   I_v = Ω (R11 Lemma SF_n). This is exactly N10's GAP on N9.9 (T on a primary face decided by the secondary).
3. *Tools that do apply.* N9.5 (lex-IBU) = Prop 6.5 for m = 2; N9.6 (FC) applies verbatim to (LEX_2) systems and kills any
   design in which a secondary trades off against another world's primary on a primary-optimal face at a continuum of rates.

---

## 7. The user's worry: disagreement among complete additive rankings (N11.11)

*Worry.* Under (CP-a) each world's ranking is the unanimity of many complete additive rankings P∘Λ_i, P ∈ M_i. A coherent model
can be undominated merely because the members disagree (X beats it for some P, loses for another), so U_L can be far larger than
any single additive field's Bayes family. Could T1 be covered by L "through disagreement" while no single additive field has
T1 in an all-coherent interior Bayes family?

*Answer (PROVED, for the reduction direction).* No use of disagreement is ever made, for three reasons.
1. *T1's status comes from competitiveness, not undominatedness.* T1 ∈ C_L gives only undominatedness, but Fact 0(b) ties T1 to a
   selected model and Lemma IC upgrades this to competitiveness on Ω: for every X there is a world i with T1 ⪯_i X, i.e. **every**
   P ∈ M_i weakly prefers T1. (This is why LDG's (S) demands competitiveness: ex:incomparable shows that mere non-domination is not
   enough for KKM.) Hence for **any** choice of one member per world, T1 is not strictly beaten (Prop 1.1(iv); and Lemma 3.1 for
   the CA parts). Disagreement-based protection would be a world where some members prefer X; competitiveness never relies on
   such a world.
2. *Fact 0 gives unanimous weak dominators.* The coherence of the interior ψ-family (Lemma K) starts from a selected C with
   C ⪯_i B at every world — unanimously in M_i — so every member, and every positive aggregate of members, ranks C weakly better.
3. *Disagreement-protected models add no profiles.* If X is L-undominated only because of incomparabilities, Fact 0(b) still
   gives a selected C with C ~_i X at every world; so U_L consists of tie-copies of selected (competitive) models. The
   aggregate ψ's interior family is a subfamily of U_L (R11 Cor W1), and the reduction needs nothing about the rest of U_L.

The only place where the plurality of M_i matters is *detection*: whether the aggregate ψ registers a strict comparison C ≺_i B
(gap 1, §5.1). Failure of detection does not protect T1; it would make some ψ-Bayes model B L-dominated (possibly incoherent),
i.e. it would spoil the ψ-family, not create coverage. Under (CP-s) and (CP-b) with (CS), detection is automatic for a single
member or a countable aggregate (Thms 6.2, 6.4), and the vast incomparability of those variants is entirely harmless.

*What disagreement can do (for the record).* It can enlarge U_L (e.g. CBOI-type and ex:incomparable-type models), and it can make
the selection non-Bayes for every *fixed* member choice; Cor 3.2(b) shows that each selected model is nevertheless Bayes for the
integral parts of every member choice, at a weight that depends on the choice. None of this enters the reduction.

---

## 8. Status

| Claim | Status | Hypotheses beyond (H) + (CP-a) |
|---|---|---|
| N11.1 normal form (IB, weak G automatic; strict G ⇔ detection by P̄; (W) for members) | PROVED | — |
| N11.2 integral reduction, (a)–(d); n = 3 vindication by ψ (CCIBU) | PROVED | (D^CA) (e.g. Case CA) |
| N11.3 splice lemma; competitive ⇒ Bayes for CA parts; T1 ψ^c-Bayes; L-comp ⇒ L^c-comp | PROVED | interior p_T needs (FS^c) |
| N11.4 (W) fails for CA parts in a system satisfying all axioms (CBOI example) | PROVED | — |
| N11.5(i) weak-* separability ⇒ (CD) | PROVED | — |
| N11.5(ii) (CD) not implied by (CP-a) + strict (G) + (IB) | PROVED | ranking-level only |
| Conj. N11.A: (S) + (C) + coverage force (CD) on Lemma-K pairs | CONJECTURE | — |
| N11.6 SN charges ⇒ cl R convex | PROVED | (SN) |
| Remark 5.4: atomic parts ⇒ separation step can fail | PROVED (as proof-step failure); NUMERICS toy | — |
| N11.7 finitely additive reduction (a′), (b), (c), (d) | PROVED | (CD) + (SN) |
| Prop 5.6 attainment criterion; non-attainment possible in principle | PROVED (criterion) | — |
| Conj. N11.B: atomic singular parts inessential under (H) | CONJECTURE | — |
| N11.9 (CP-s): single CA member gives full integral reduction | PROVED | (FS₁) |
| N11.10 (CP-b): structure; reduction under (CS); lex under (LEX_m) | PROVED (as stated) | (CS) / (LEX_m) |
| (CP-b): T1 in the lex family; general representation | OPEN (blocked as in §6.2) | — |
| N11.11 the disagreement worry is harmless for the reduction direction | PROVED | — |
| SN ⇔ no atoms on the Stone space | CHECKED (sketch) | — |
| Fact 1.2 (Yosida–Hewitt with concentration) | CHECKED (imported: CBOI lem:split, PP Thm 1) | — |

**For part (B).** The reduction lands in: integral fields under (D^CA) or (CP-s)+(FS₁) or (CP-b)+(CS) with CA separators;
otherwise strongly non-atomic charge-valued fields with attained-minimiser uniqueness (§5.4–5.5). Atomic singular parts and the
non-Archimedean (D^0 ≠ ∅) part of (CP-b) are not reached by any proved reduction.
