# N13. Referee report on N11_notes.md (BRIEF6 part (A): reduction for coherent-preference rankings)

13 Oct 2026. Independent referee; I did not write N11. Every step was re-derived against BRIEF–BRIEF6, R11 (Lemma IC,
Lemma K, Thm W), R13 (Prop S), CCIBU.tex, N9 (N9.5, N9.6), N10, CBOI ("Closed Choice Beyond Ordinary Integrals"), LDG v2
§§1–2, and the Walley extracts (w1991.txt 8200–8600 = Walley 1991 §§3.7–3.8; w2000.txt 575–720 = Walley 2000 §6).
Script: `n13py/checks.py` (NUMERICS only). Verdicts: **CORRECT**, **CORRECT WITH REPAIR**, **GAP**, **FALSE**.
New results here are labelled PROVED (full proof below).

## 0. Summary table

| Item | Verdict | One-line reason |
|---|---|---|
| Formulation of (CP-a) vs Walley 1991 §3.7.5–3.7.6, Thm 3.8.1 | CORRECT | Almost-preference R0–R5 ⇔ P̲(X−Y) ≥ 0 ⇔ unanimity of a weak-* compact convex set of states; losses enter as −Λ; null-set reading = L^∞(μ) |
| Formulation of (CP-s) vs Walley 1991 §3.7.7–3.7.9, Thm 3.8.1(5) | CORRECT (as mathematics) | ≻ ⇔ P̲(f) > 0 or f ≥ 0 a.e., f ≠ 0. In LDG's preorder framework it must be ≻ ∪ = ; see Prop A for what this costs |
| Formulation of (CP-b) vs Walley 2000 §6 (D1–D4, P1–P5, eqs (4),(8),(9)) | CORRECT | D5 (conglomerability) is omitted; this only enlarges the class. Walley's own "weak preference" (§6(f)) is (CP-a)'s relation |
| N11.1 normal form | CORRECT | (IB), weak (G) automatic; strict (G) ⇔ P̄(f) > 0; (W) for members |
| Fact 1.2 (Yosida–Hewitt with concentration) | CORRECT | Matches CBOI lem:split / Pennanen–Perkkiö Thm 1; the common-sequence and decreasing-refinement steps check |
| N11.2 integral reduction under (D^CA) | CORRECT | R11 Thm W + R13 Prop S applied to M_i ∩ CA; strict guidance of the aggregate from strict (G) is correctly derived. Relies on CCIBU (unrefereed; spot-checked, no error found) for n = 3 |
| N11.3 splice lemma, Cor 3.2 | CORRECT | Finite families of pure parts have a common μ-small concentration set; splicing kills them |
| N11.4 CBOI counterexample to (W) for CA parts | CORRECT | Computation re-done; CBOI Prop prop:example checked for (G), (IB), (LA), (S), (C) |
| N11.5(i) weak-* separability ⇒ (CD) | CORRECT | {P : P(f) > 0} is weak-* open |
| N11.5(ii) ultrafilter M_i: (CD) not implied by (CP-a)+(G)+(IB) | CORRECT | Every step checked (almost-disjoint family, Bonferroni bound, choice of β, G, W) |
| N11.6 / Prop 5.3 Shapley–Folkman rounding under (SN) | CORRECT | Vertex of {s ∈ [0,1]^N : Σ s_j m(A_j) = t m(H)} has ≤ n fractional coordinates |
| SN ⇔ no atoms on the Stone space | CORRECT (sketch adequate) | Regularity + clopen base + compactness |
| Remark 5.4 (atoms break separation) | CORRECT WITH REPAIR | Conclusion stands. The formula cl R = cl R^na + R^at is asserted, not proved (state as cl R = cl(R^na + R^at) or drop it). The NUMERICS witness (1.000, 1.996) is **wrong** (grid artefact: it is supported by p ≈ (0.996, 0.004)); a correct witness is (1.658, 1.060) (n13py (1)) |
| N11.7 / Thm 5.5 finitely additive reduction | CORRECT | Lemma K for charges, uniqueness by complementary splices + linearity, separation via cl R |
| Prop 5.6 attainment criterion | CORRECT | |
| N11.8 class for part (B) | CORRECT WITH REPAIR | Must record that ψ's local penalties ρ_iλ_i are integrable, not bounded; add the weaker integral class reached without (D^CA) (Prop B below) |
| N11.9 (CP-s) integral reduction | CORRECT as a conditional; **"no extra hypotheses" is FALSE** | (FS₁) is a genuine hypothesis: strict (G) is automatic under (CP-s) for every M_i (Walley D6), so it supplies nothing, and the encoding is irrelevant to M_i. Worse: Prop A shows (S) fails for every (CP-s) system that is Case CA with strictly positive members at two disagreeing worlds, including the additive instance. The theorem's hypothesis class may be empty |
| N11.10 Prop 6.3, Thm 6.4 | CORRECT | Hahn–Banach / bipolar / int cl D = int D all check |
| N11.10 (LEX_m) definition | CORRECT WITH REPAIR | D2 needs the union of level supports to be all of H a.e. (not only problems with a non-singleton advice range); append μ̄ as a last level |
| N11.10 Prop 6.5; "where blocked" | CORRECT | Same proof as R11 Prop LX, with (C) replaced by detection. N9.6 (FC) applies only under its hypotheses FC1–FC3 |
| N11.10 (CP-b) as a hypothesis class | Same caveat as N11.9 | For D_i = D⁺_i (the (CP-s) case, including the additive instance) Prop A applies |
| N11.11 the disagreement worry | CORRECT | Every proof step uses competitiveness and unanimous weak dominance only |
| BRIEF6 "additive rankings are instances of every variant" | FALSE for (CP-s), (CP-b); TRUE for (CP-a) | The strict-or-equal version of an additive ranking turns ties into incomparabilities and violates (S) (Prop A) |

**Net.** N11's mathematics is sound. I found no false proof step. The corrections are (i) one NUMERICS witness, (ii) one
definitional slip in (LEX_m), and (iii) a substantive scope problem for the strict-preference variants: they are close to
inconsistent with closed competitive choice (Prop A). (CP-a) is therefore the only Walley variant for which the reduction is
both proved and known to be non-vacuous, and for which "impossibility ⊇ additive impossibility" holds. I also give a
nearby result (Prop B) that removes N11's detection and convexity hypotheses for (CP-a), at the price of Bayes uniqueness
holding only at almost every weight.

---

## 1. Walley's models: are the formulations right?

**(CP-a).** Walley 1991 §3.7.5 defines X ≽ Y iff X − Y is almost-desirable; R0–R5 (§3.7.6) characterise the coherent
ones; Thm 3.8.1 gives X ≽ Y ⇔ P̲(X − Y) ≥ 0; §3.8.4 gives the credal set ℳ(≽) = {P : P(X) ≥ P(Y) whenever X ≽ Y}. With
gambles −Λ_iX (losses are penalties), "X at least as good as Y at i" is P̲_i(Λ_iY − Λ_iX) ≥ 0, i.e. N11's (CP-a). On
L^∞(μ), Walley's linear previsions are exactly the states (they vanish on null classes automatically), and coherent lower
previsions ↔ weak-* compact convex sets of states (lower envelope theorem). The null-set modification ("X ≥ 0" as ≥ 0 a.e.)
is exactly what passing to L^∞(μ) does. CORRECT.

**(CP-s).** Walley 1991 §3.7.8–3.7.9: D2, D3, D5–D7 / R2, R3, R5–R8; Thm 3.8.1: X ≻ Y ⇔ P̲(X − Y) > 0, or X ≥ Y and
X ≠ Y. N11's D⁺_i matches, with "≥" a.e. and "≠" off a null set. Walley's ≻ is irreflexive (R6 with X = Y), so the only
LDG preorder whose strict part is ≻ and which adds no further ties is ≻ ∪ =. N11 uses exactly that. The formulation is
right. Its consequences for (S) are the subject of Prop A.

**(CP-b).** Walley 2000 §6: D1 (0 ∉ D), D2 (X > 0 ⇒ X ∈ D, where X > 0 means X ≥ 0 and X ≠ 0), D3 (c > 0 ⇒ cX ∈ D; the
extract drops "> 0"), D4 (sums); P1–P5 with X ≻ Y ⇔ X − Y ∈ D (eq. 4); eq. (8) gives N11's embedding of (CP-s); eq. (9)
gives M = {P : P ≥ 0 on D}, as in Prop 6.3. Walley also mentions D5 (conglomerability, from his 1991 book) and sets it aside
for finite spaces. N11 omits D5 on L^∞(μ). That is a weaker hypothesis, so every reduction proved under (CP-b) holds a
fortiori for D5-coherent sets. CORRECT.

**Observation (used in Prop A).** Walley 2000 §6(f): "weak preference for X over Y iff X − Y + ε ∈ D for all ε > 0", that is,
f ∈ cl D = {P̲ ≥ 0}. So Walley's own pairing is *strict* preference from D⁺ or D together with *weak* preference from the
closure, which is (CP-a)'s relation. LDG's framework uses a single preorder per world, and the strict part of (CP-a)'s
preorder is not Walley's ≻. One must choose between the two. The closure axiom D4/R4 is what makes closed sections possible.
The openness axiom D7/R8 of strict preference works against them (Prop A).

---

## 2. Claim-by-claim

### N11.1 (Prop 1.1): CORRECT
- Preorder: linearity.
- (IB): f is unchanged pointwise when common advice is replaced (CBOI's form of (IB)).
- Weak (G): f ≥ 0 a.e. ⇒ P(f) ≥ 0.
- Strict part, (iii) and (iv) are immediate.
- Strict (G) is **not** automatic under (CP-a). N11 correctly keeps it in (H).

### Fact 1.2: CORRECT
- This is Rockafellar's characterisation of singular functionals on L^∞ (= PP Thm 1, used identically in CBOI lem:split).
- Common sequence: μ(∪_k Z^k_m) ≤ 2^{−m}, and P_k^p(H∖Z_m) ≤ P_k^p(H∖Z^k_m) = 0.
- Finite intersections stay concentration sets, since P^p(H∖(A∩B)) ≤ P^p(H∖A) + P^p(H∖B).
- Because Z_m decreases with μ(Z_m) → 0, 1_{Z_m} → 0 a.e. This is the form needed for dominated convergence in Lemma 3.1.

### N11.2 (Thm 2.1): CORRECT
- **Step 1.** M_i ∩ CA ⊆ L¹(μ), and L¹ of a Gaussian on ℝⁿ is separable. Then |Q(f) − Q_k(f)| ≤ ‖f‖_∞‖ρ_Q − ρ_k‖_1.
  Since strict (G) produces strict comparisons, (D^CA) forces M_i ∩ CA ≠ ∅.
- **Step 3** (strict guidance of the aggregate) is right: the swap Y = W_i with worse advice on Q is a measurable model
  whose advice lies in the advice ranges, and ρ_{i,k} ≤ 2^k ρ_i.
- **Step 4.** R11 Thm W's proof uses (W), (R), positive weights, an integrable envelope, strict guidance of ψ, Fact 0, (C),
  IC and Lyapunov. The members Q_{i,k}∘Λ_i need not be strictly guiding; R13 §2.4 (last bullet) covers this.
  Envelope: ‖λ_i‖_∞ρ_{i,k}.
- **Step 5.** CCIBU Thm 1's hypotheses are met (integrable envelope, a.e.-strict increase, unique coherent interior Bayes
  models). CCIBU is author-checked, not refereed. I re-derived Lemmas 2–4: the direction lemma, the edge case via a
  subgradient of the convex h with v = (−λ, 0, 1), and l.s.c. of x(p). I found no error.
- **Remark 2.2.** "Weak-* closed set of densities ⇔ weakly compact ⇔ uniformly integrable" is right: σ((L^∞)*, L^∞)
  restricted to L¹ is σ(L¹, L^∞), and Dunford–Pettis applies.
- **Strengthening worth recording.** (D^CA) holds whenever M_i is the weak-* closure of its CA members, because CA members
  are then weak-* dense and {P(f) > 0} is weak-* open. So every credal set *generated* by densities qualifies, even when its
  closure contains singular charges.

### N11.3 (Lemma 3.1, Cor 3.2): CORRECT
- Every step checks: X_m ∈ M by splicing; the pure term vanishes; dominated convergence uses envelope 2‖λ_i‖ρ_{P_i}.
- (c): pick, per world, a member witnessing failure of ⪯^c, then apply 3.1. Correct.
- (d): (FS^c) and the countable-combination argument are right. The ccc of the measure algebra gives a countable family
  attaining the essential union. The band projection onto L¹ is linear and norm-continuous, so ρ_{ΣcₖPₖ} = Σcₖρ_{Pₖ}. The
  norm limit lies in M_i.
- The "Reading" is accurate: this closes the separation step only.

### N11.4 (Prop 4.1): CORRECT
- η is purely finitely additive: η({t ≥ 1/m}) = 0 for all m forces η^c({t ≥ 1/m}) = 0. Then
  η^c(H) = lim η^c({t < 1/m}) = η^c({t = 0}) = 0.
- η = μ on functions of θ (independence of t and θ).
- ν(Λ_iX − Λ_iD_i) ≥ ½η(¾b_i1_Q) = (3/8)∫_Q b_i dμ = a. ν(Λ_iY − Λ_iD_i) = (3/8)∫_S b_i dμ < a. ν^c-difference < 0 for large m.
- CBOI prop:example is (CP-a) with M_i = {ν}, λ_i = ℓ_i bounded, and (G), (IB), (LA), (S), (C) hold there (CBOI's proof
  checked: uniqueness of the Bayes model, continuity of L_i(C_p) via direction-only costs, (C) via uniqueness).
- The "Consequence" paragraph correctly limits the claim to the mechanism.

### N11.5: CORRECT
- (i) Each listed case is weak-* separable. Remark: the whole state space of L^∞(μ) is weak-* separable (L¹ densities are
  weak-* dense, and L¹ is separable), but weak-* separability is not hereditary. That is what Prop 5.2 exploits.
- (ii) Checked line by line:
  - P_α(1_{B_n}) = 0 for every n;
  - P_α(Y_β) = δ_{αβ}, since A_α ∈ 𝒰_α and A_α ∩ A_β is finite;
  - C_0 vanishes on every B_n (a weak-* closed convex condition);
  - finite unions of the Y_β have overlaps of Q-measure 0, so Σ_F Q(Y_β) ≤ 1 by Bonferroni, and {β : Q(Y_β) > 0} is
    countable;
  - since 1 ∉ A_β, B_1 ∩ Y_β = ∅, and μ(G) ≤ ½μ(U ∩ P_i) < μ(B_1) makes W available;
  - μ̄(f) = 0, Q(f) = Q(G) ≥ 0, P_β(f) = ½, P_k(f) = 0.
- Scope (ranking-level only) and CONJECTURE N11.A are correctly labelled.

### N11.6 (Prop 5.3; SN): CORRECT
- A countable convex combination of SN states is SN (tail < ε/2 plus a common refinement).
- The rounding argument is the standard Shapley–Folkman / Lyapunov-by-LP argument. NUMERICS reproduce ≤ n fractional
  coordinates.

### Remark 5.4: CORRECT WITH REPAIR
- What is proved: an atom δ_k (k in the Stone space) evaluates a model through its advice "along the ultrafilter k", a
  finite choice, so R can be a non-convex Minkowski-type sum. A weakly Pareto, unsupported profile then breaks the
  separation step. This conclusion stands.
- What is not proved: the equality cl R = cl R^na + R^at. Splicing the atom choices independently of the non-atomic part
  needs a set in k of small non-atomic mass for each of countably many atoms. That holds, but the note does not show it, and
  the right-hand side need not be closed. Replace the formula by "R ⊆ R^na + R^at ⊆ cl R", or drop it.
- **The NUMERICS witness is wrong.** (1.00000771, 1.99607204) lies at angle 180.23° on D1 and is supported by
  p = (0.99609, 0.00391). The script's p-grid (step 0.0025) cannot hit it. n13py (1) checks support exactly: the unsupported
  weakly Pareto points of D1 form the arc 236.3°–270°, e.g. (1.658, 1.060).

### N11.7 (Thm 5.5): CORRECT
- (0): strict (G) plus (CD); every other term is ≥ 0.
- (a′): Fact 0(a), then (W) gives ψ_i(C) ≤ ψ_i(B). Interior p plus attainment gives equality; every term ≥ 0 with zero sum
  gives each P_{i,k}(f_i) = 0; (CD) excludes C ≺_i B; (C) finishes.
- Uniqueness: the complementary-splice identity Λ_iE_A + Λ_iE′_A = Λ_iB + Λ_iB′ plus linearity makes both splices attain,
  with no pointwise minimisation needed. Then R2 Lemma U applies. Correct and neat.
- (d): competitiveness plus (W) shows R misses ψ(T1) − (0,∞)ⁿ. An open set missing R misses cl R. Separation, then the IC
  push to the interior.

### Prop 5.6: CORRECT
The CA value of X_m converges because ∫_{Z_m} Σp_iρ_i‖λ_i‖ → 0. Attainment of a + b forces attainment of both a and b.

### N11.8: CORRECT WITH REPAIR
- Add that ψ_i(g, a) = ρ_i(g)λ_i(g, a) has an **integrable, possibly unbounded** envelope.
- On M_U with the error encoding, ψ_i(X) = ν_i(E_i(X)) with ν_i = ρ_iμ.
- Add the class reached without (D^CA) under only (FS^c) (Prop B).
- Otherwise the description (integral under (D^CA); SN-charge fields, attained minimisers only, under (CD)+(SN); atoms not
  reached) is accurate.

### N11.9 (Prop 6.1, Thm 6.2): CORRECT as a conditional; the summary overstates it
- **Prop 6.1** checks: D⁺ is a pointed convex cone, using superadditivity of P̲ and P̲ ≥ 0 on nonnegative gambles.
- **Thm 6.2's proof** checks, including the step "Q_i(f_i) = 0 and f_i ∈ D⁺ ∪ {0} ⇒ f_i = 0":
  - if P̲(f) > 0 then Q(f) > 0;
  - if f ≥ 0 and f ≠ 0 then ∫fρ > 0, because f vanishes on problems with a singleton advice range;
  - Λ_iB = Λ_iC a.e. at one world gives B = C a.e., because distinct kinds of advice have distinct ranks a.e.
- **What is assumed: (FS₁)**, a countably additive member with a.e.-positive density on problems with a non-singleton advice range.
  - It is **not** supplied by strict (G). Under (CP-s), strict (G) holds for *every* M_i (D6 builds it in).
  - It is not supplied by the encoding, which constrains Λ, not M_i.
  - It is not supplied by (IB).
  - Counter-instances satisfying (CP-s) + strict (G) + (IB): M_i = {η} (CBOI's pure charge); M_i = {Q} with ρ_Q = 0 on a
    non-null region; N11's ultrafilter set C_0 together with μ̄|_R for a proper region R.
  - So "integral reduction with no extra hypotheses" is FALSE as a summary. The theorem itself states (FS₁), and N11 §0
    says "Under (H) + (CP-s) + (FS₁)". The overstatement is in BRIEF6's paraphrase, not in N11's text.
- **Remark on the "strictly positive SN charge" variant.** CBOI lem:split shows that any strictly positive state has a CA
  part with a.e.-positive density. The normalised CA part need not lie in M_i, though, and (W) needs the full member. So
  that variant is not subsumed by (FS₁), and N11's remark stands.
- **Without (FS₁), a nearby result is available** (PROVED here). For any P ∈ M_i, the two-level lexicographic field
  (P∘Λ_i, μ̄∘Λ_i) satisfies lex-(W) and lex-detection of every strict (CP-s) comparison:
  - P̲(f) > 0 ⇒ P(f) > 0;
  - f ≥ 0, f ≠ 0 ⇒ P(f) ≥ 0 and μ̄(f) > 0.

  If M_i has a CA member Q_i (of any support), both levels are integrals. Then Prop 6.5's proof gives:
  - interior lex-Bayes models a.e. unique, equal to selected models, coherent;
  - vertices as usual;
  - T1's membership is exactly N11.10's blocked lex-separation step.

  So (FS₁) is what collapses the lex field to a single integral.
- **Scope problem.** See Prop A in §3. Every (CP-s) system that is Case CA with strictly positive members at two
  disagreeing worlds violates (S). Thm 6.2's hypothesis class is therefore at most the systems where every such pair has a
  blind or non-uniformly-integrable member, and it may be empty (CONJECTURE N13.A).

### N11.10: CORRECT, with one repair
- **Prop 6.3** (i) checks.
- **Prop 6.3** (ii) checks:
  - the case split g ≠ 0 / g = 0 for D ∩ {ess sup < 0} = ∅;
  - the separating φ is positive with φ(1) = ‖φ‖ > 0;
  - bipolar for the norm-closed cone cl D ⊇ L^∞₊;
  - P̲(f) = δ > 0 ⇒ B(f, δ) ⊆ cl D ⇒ f ∈ int cl D = int D (int D ⊇ {ess inf > 0} ≠ ∅).
- **Thm 6.4** checks. The converse ("D⁰ = ∅ + weak-* separability ⇒ (CS)") is right.
- "No real additive field obeying (W) can carry D⁰": right for fields of the form φ∘Λ_i with φ ≥ 0 on D_i, whose dual cone
  is cone(M_i). For general penalty fields, (W) is only required on realised differences. Read the sentence with that
  qualifier.
- **(LEX_m): REPAIR.** {f : (Q¹(f), …, Q^m(f)) >_lex 0} satisfies D2 only if the union of the level supports is all of H
  a.e. A nonnegative f supported on problems with a singleton advice range would otherwise be lex-zero. Append μ̄ as a final level. Comparisons of
  loss differences are unchanged, since those vanish on problems with a singleton advice range.
- **Prop 6.5** checks. Lex ties at every world plus lex-detection give f_i = 0, so no (C) is needed.
- **"Where blocked"** (representation; T1 in the lex family; tools) is accurate. The citation of N9.6 should carry FC's
  hypotheses FC1–FC3 (a.e. uniqueness of Y_λ, uncountably many F_j-levels, improvability at j). With them, FC applies to
  (LEX_2) systems with CA levels as stated.
- **Scope.** For D_i = D⁺_i, (CP-b) is (CP-s) and Prop A applies. For D_i with boundary desirability, Prop A's key step
  (C_p ≺_ω C* ⇒ P̲_ω(·) > 0) fails, and consistency with (S) is open. My heuristic for the (LEX_m) case is the primary-level
  version of Prop A: level-1-strict improvements are excluded near p0, and FC/R2 Thm 7 bound the level-2 moves. Not proved.

### N11.11: CORRECT
- (1) Lemma IC gives competitiveness on Ω. For any member choice P_i ∈ M_i, ψ_i(X) < ψ_i(T1) ∀i would make T1 ⪯_i X fail at
  every i.
- (2) Fact 0(a) is unanimous.
- (3) Fact 0(b) ties every undominated model to a selected one.
- So no step uses non-domination that rests on disagreement. The plurality of M_i matters only for detection (gap 1),
  which is invisibility (all chosen members tie), not disagreement. Under (CP-s)/(CP-b) the "incomparabilities" are boundary
  indecision, also harmless to the proofs.
- Caveat for the record: the worry is harmless *for the proofs*. Whether disagreement can be exploited when (CD) fails is
  exactly CONJECTURE N11.A.

---

## 3. New results

### Prop A (PROVED). Strict-preference worlds are incompatible with closed competitive choice

**Setting.**
- Domain: the U-domain M_U (evaluable models: the measurable subsets of U = D_{K′}), with error indicators
  Λ_iX = 1_{E_i(X)}. Any decomposable domain works whose advice ranges contain, at every selected model, all-worlds-worse
  advice on a non-null set of unanimous problems and ω-improving advice wherever the model errs at ω.
- Worlds ω ≠ j follow (CP-s), with M_ω, M_j weak-* compact sets of CA states whose densities are > 0 a.e. ("Case CA,
  strictly positive"). Uniform integrability is then automatic.
- W_ω ≠ W_j on a non-null set.

**Claim.** No selection u : Δ → C satisfies (S), even without (LA), (C), (G) or any target.

*Proof.*

1. **Preliminaries.**
   - For p on the edge E = [e_ω, e_j], (S) makes C_p competitive on supp p ⊆ {ω, j}.
   - C_{e_ω} = W_ω, since C_{e_ω} ⪯_ω W_ω forces equality: nothing is strictly better than W_ω at ω. Likewise C_{e_j} = W_j.
   - Under strict positivity and compactness, g ≥ 0 a.e. with g ≠ 0 gives P̲_ω(g) > 0. Hence, at ω and j,
     Y ≺ Z ⇔ P̲(Λ Z − Λ Y) > 0.

2. **Witness.** Let C* = C_{p0} with C* ≠ W_ω.
   - Take a non-null B ⊆ E_ω(C*) of small measure. Let A = C* ∩ (positive orthant) ∩ U, which is non-null since C* is
     coherent. A is disjoint from E_ω(C*).
   - For an increasing family A_t ⊆ A, continuous in measure, with A_0 = ∅ and A_1 = A, let X_t be C* corrected on B and
     silenced on A_t. Then f_t := Λ_ωX_t − Λ_ωC* = 1_{A_t} − 1_B.
   - t ↦ P̲_ω(f_t) is continuous (uniform integrability).
   - P̲_ω(f_0) = −P̄_ω(B) < 0, and P̲_ω(f_1) ≥ P̲_ω(A) − P̄_ω(B) > 0 once μ(B) is small (again uniform integrability).
   - So P̲_ω(f_{t*}) = 0 for some t* > 0. Put X := X_{t*}.
   - X is incoherent (silent on part of the orthant), so X ≠ C_p for every p.
   - C* ⊀_ω X, since P̲(f) = 0 and f is not ≥ 0. Hence p0 ∉ A_ω(X).

3. **Local exclusion.** If C_p ≺_ω C*, then P̲_ω(Λ_ωX − Λ_ωC_p) ≥ P̲_ω(f) + P̲_ω(Λ_ωC* − Λ_ωC_p) > 0. So p ∈ A_ω(X).
   A_ω(X) is closed and misses p0, so some neighbourhood N_ω of p0 contains no p with C_p ≺_ω C*. The same holds at j when
   C* ≠ W_j.

4. **Local constancy.**
   - If C* ∉ {W_ω, W_j}: for p ∈ E ∩ N_ω ∩ N_j, competitiveness of C_p against C* gives C_p = C* or C_p ≺_{ω or j} C*.
     Both strict options are excluded, so C_p = C*.
   - If C* = W_ω: nothing is ≺_ω W_ω, and the j-witness exists because E_j(W_ω) = P_ω △ P_j is non-null. So C_p = W_ω near
     p0. The case C* = W_j is symmetric.

5. **Conclusion.** p ↦ C_p is locally constant on the connected edge E, hence constant. Then W_ω = C_{e_ω} = C_{e_j} = W_j,
   a contradiction. ∎

**Corollary A1 (PROVED).** The additive instance M_i = {Q_i}, Q_i CA with positive density, of (CP-s), and of (CP-b) with
D = D⁺, never satisfies (S) once two worlds' ideals differ. So BRIEF6's statement "additive rankings are instances of
every variant" is false for (CP-s) and (CP-b). For (CP-a) it is true: X ⪯ Y ⇔ Q(ΛY − ΛX) ≥ 0 is the additive ranking.

The mechanism is Walley's openness axiom (D7/R8): the upper sets {Y : C ≺ Y} are open. Closed sections then force
local minima of the selection everywhere, the same mechanism as CBOI thm:blind and R2 Thm 7.

n13py (2) illustrates the half-open section for a two-world additive instance: {t : ψ_1(C_t) < c} = [0, t*).

**CONJECTURE N13.A.** (CP-s) + (S) is inconsistent whenever two worlds' ideals differ, for every M_i. The gap in the proof
above: with a member blind on a region R, a selected C_p can be strictly better than C* only through pointwise improvement
on R, with P̲ = 0. Step 3 then gives no exclusion.

### Prop B (PROVED). Weak integral reduction for (CP-a) without detection or convexity hypotheses

**Hypotheses.**
- (H), (CP-a), and (FS^c): some P_i ∈ M_i has a CA part with density ρ_i > 0 a.e. on problems with a non-singleton advice range.
- Note: any strictly positive member qualifies (CBOI lem:split); (CD) and (SN) are not assumed.

**Field.** ψ^c_i(X) := ∫ λ_i(g, a_X(g)) ρ_i(g) dμ.

**Claim.** ψ^c is a strictly guiding integral field on M with:
- (α) T1 is ψ^c-Bayes at some p_T ∈ int Δ;
- (β) for **every** p ∈ Δ some ψ^c-p-Bayes model in M is coherent;
- (γ) for λ-almost every p ∈ Δ the ψ^c-p-Bayes model is a.e. unique, hence coherent;
- (δ) at each vertex the Bayes model is W_i(M) = C_{e_i}, coherent.

*Proof.*

- **(α)** is N11 Cor 3.2(d).
- **(β)** follows CBOI's proof of Thm fa, transplanted.
  - Fix p. Put a := min Σp_iψ^c_i (attained by pointwise minimisers B) and b := inf_M Σp_iπ_i(Λ_i·), with π_i = P_i^p.
  - Choose A_m with pure value < b + 1/m, and let X_m be A_m on Z_m and B off Z_m (common concentration sets, Fact 1.2).
    Then p·P(Λ X_m) → a + b.
  - Fact 0(a) gives a selected C_m ⪯_i X_m at every i. (W) for the full member P_i gives
    a ≤ Σp_iψ^c_i(C_m) ≤ p·P(ΛX_m) − Σp_iπ_i(Λ_iC_m) ≤ p·P(ΛX_m) − b → a.
  - Coherent models are sequentially compact in measure (CBOI lem:compact; R1 Prop 3.1), and M is closed in measure.
    ψ^c is continuous in measure (integrable envelope).
  - So a subsequence converges to a coherent C_∞ ∈ M with p·ψ^c(C_∞) = a.
- **(γ)** Fubini on H × Δ.
  - For a.e. g and any two distinct kinds of advice a, b, w = ψ^c(g,a) − ψ^c(g,b) has all coordinates ≠ 0 (ρ_i > 0, strict rank
    increase). A tie in Δ therefore lies on the hyperplane p·w = 0, which is λ-null.
  - So for λ-a.e. p the tie set is μ-null, and the pointwise minimiser is a.e. unique. It equals the coherent C_∞ of (β).
- **(δ)** By strict guidance and the vertex lemma. ∎

**Reading.**
- This is strictly weaker than N11.2's (a): ties are allowed at a λ-null set of interior weights, and the Bayes models
  need not lie in C_L. It needs neither (CD) nor (SN), and it covers the CBOI example (ν^c = μ/2).
- It is the integral class part (B) must exclude when nothing beyond (FS^c) is known.
- Whether R15-type exclusions survive "uniqueness at a.e. interior weight" is open. At a tie weight p0, a coherent
  minimiser exists, but other (incoherent) minimisers are not excluded by anything above.

---

## 4. Justified overall conclusion

**Reduction to an additive field, as BRIEF6 (A) asks, is PROVED for:**

1. **(CP-a) + (D^CA).** (D^CA) includes Case CA and every M_i that is the weak-* closure of its CA members.
   - The field is integral: ψ_i = ∫ρ_iλ_i dμ, with ρ_i ∈ L¹ and ρ_i > 0 a.e. on problems with a non-singleton advice range, on the **same** decomposable
     domain.
   - At every interior weight the Bayes model is a.e. unique, coherent and in C_L.
   - Vertices: W_i = C_{e_i}. Boundary: coherent Bayes models exist.
   - T1 = B_{p_T} with p_T ∈ int Δ.
   - For n = 3, ψ vindicates T1 with (LF) (CCIBU). This is the clean case.
2. **(CP-a) + (CD) + (SN).** A charge-valued field P*_i∘Λ_i with SN states; uniqueness and coherence only for **attained**
   interior minimisers (N11.7).
3. **(CP-a) + (FS^c).** An integral field with properties (α)–(δ) of Prop B: a.e.-unique coherent Bayes models at almost
   every weight, a coherent Bayes model at every weight, and T1 interior-Bayes. Weaker conclusions, minimal hypotheses.
4. **(CP-s) + (FS₁)** and **(CP-b) + (CS) with CA separators.** Integral conclusions as in item 1, *but* Prop A shows (S)
   fails for every Case-CA strictly positive instance, including the additive one. These variants are not known to contain
   any system satisfying the axioms. Here "impossibility ⊇ additive impossibility" fails, because the additive rankings are
   not instances.

**Not reached:**
- (CP-a) with atomic singular parts, or with detection only by uncountable singular families (N11.A/B open);
- (CP-b) with invisible desirability D⁰ ≠ 0 (lexicographic; the T1-in-family step is open, as in R11 §5 and N10 on N9.9).

**Part (B) must exclude** (for the clean case, item 1): strictly guiding **integral** additive fields
X ↦ (∫ ρ_i(g)λ_i(g, a_X(g)) dμ)_i on the given decomposable domain M with (LF) at T1, satisfying:
- (N1)–(N2): a.e.-unique coherent Bayes models at **every** interior weight;
- (N3): coherent world-ideal vertex models;
- (N4): coherent Bayes models at boundary weights;
- T1 Bayes at an interior weight.

Penalties are integrable (ρ_i ∈ L¹), not necessarily bounded. On M_U with the canonical encoding, the fields are
ν_i(E_i(X)) with ν_i ≪ μ, ν_i ~ μ on U. The Bayes rule there is: accept h iff Σ_{h_i>0} p_iρ_i(h) > Σ_{h_i<0} p_iρ_i(h).
For n = 3 this is equivalent to "no additive integral vindication of T1 on a decomposable domain with (LF)" (CCIBU), i.e.
BRIEF2's single-target additive problem.

Finitely additive penalties enter part (B) only if one wants items 2–3:
- SN charge fields with attained-only uniqueness;
- or integral fields with a.e.-only uniqueness.

Purely atomic and ultrafilter-type penalties are not part of (B). For those, the *reduction* is what is incomplete.
