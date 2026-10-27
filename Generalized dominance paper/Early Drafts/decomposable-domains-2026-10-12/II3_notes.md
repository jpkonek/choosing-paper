# II3 (round 37, BRIEF29, second track). A non-transitive cover attempt with T1 tied but not selected: the barrier map, a vacuity in HH2 Theorem 2.1 and its repair, and a clone theorem that reduces the cover to one defence map

18 Oct 2026. Rules of BRIEF13 and BRIEF28/29. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports keep their recorded status.
- **CHECKED**: a step-by-step reading of a recorded proof, or an exact rational computation in `ii3py/checks.py`
  (run `python3 -I checks.py` inside `ii3py/`; output `checks.out`).
- **CONJECTURE**, **NUMERICS**: none is used below.

Setting: the full four-advice domain (every measurable model is evaluable), three worlds, T1 the ε-contamination of u,
ε ∈ (0,1); notation of the write-up §2 and HH2 §1 (records rec(X,Y), realisations, record sets 𝒜_i). Each ≼_i is
reflexive; (FC) as in BRIEF28. Strict (G), (IB) in record form, (LA), (S) (closed sections for every model,
competitiveness on supp p), direct (C), (LF) at T1, T1 undominated. Nothing is assumed beyond these. Every extra
condition below is a hypothesis of the result that states it.

---

## 0. Outcome

**No cover of T1 was obtained.** I pursued lead (A) (T1 tied with a selected C_{p\*} but not selected). Lead (B)
(a jumping selection) turned out to be subsumed: the construction below never uses continuity of the selection.
What I proved:

1. **Barrier map for an unselected T1 (§1; CHECKED/PROVED).**
   - The adding-up barriers **still bind** when T1 is only tied. These are Q4.2, M3.10′ and M0closed(b), together
     with L4.1/L4.2. Their single ranking-level step (M3.4.3 = H1.1 step 1) needs T1 ∈ C_L and T1 ≈ C_p, not
     T1 = C_p. So every cover of type (A) still needs a world that does not add up.
   - FF2 Thm 4.1, HH2 Thm 5.1/Cor 5.3, Q3.25 and CC2 Cor 5.7 need T1 **selected** (or competitive). They do not bind
     an unselected T1, except through HH1's strengthened Thm 4.1″.
   - L3.4 and the vertex lemma (HH2 3.1) constrain the selection and bind regardless.
2. **Rigidity of the tie (§2; PROVED).**
   - The tie record t\* = rec(C_{p\*}, T1) is mixed at every world.
   - It is a tie in every ordering extension, at every realisation.
   - T1 and C_{p\*} have **identical** verdicts on every record supported off S := supp t\*. So T1 is competitive
     on supp p\* against every model that agrees with T1 on S, and the whole escape must happen inside S.
   - Splitting S yields a "piece calculus" (Lemma 2.4). Together with direct (C) and a conic-twin argument, it gives
     a precise constraint on how sub-records of t\* may be accepted (Prop 2.5).
3. **HH2 Theorem 2.1 is vacuous on the full domain (Prop 3.1; PROVED, CHECKED).**
   - Its hypothesis (M), applied to the worsening records from the vertex models to the all-contradictory model,
     forces w(that model) = 0 ∉ Δ. So no defence map w satisfies (M).
   - Its hypothesis (E), exact sections, fails on the same model (Prop 3.1′).
   - **Repair (Theorem 3.2; PROVED).**
     - Separate the defence point w̄(X) ∈ Δ, which gives the cap sets, from a uniform slack c(X) ≥ 0 in the leading
       level c(X) − w̄_i(X).
     - Replace exactness (E) by closedness (E″).
     - All conclusions of HH2 2.1 survive except exactness of sections, and both vacuities disappear (CHECKED).
4. **The clone theorem (Theorem 4.1; PROVED).** Take the repaired generator scheme with an injective coherent
   selection that need not pass through T1 and need not be continuous. Attach T1 as an unselected clone of C_{p\*}:
   - set w̄(T1) = p\*, c(T1) = 0 and τ(T1) = 0;
   - accept t\* and t\*⁻¹ at every world;
   - use a strictly guiding additive tie-break G_i with G_i(t\*) = 0.

   **Every axiom then follows from two conditions on (w̄, c): (M′) and (E″).**
   - (M′) is monotonicity of the generators along all their realisations, together with invariance of (w̄, c) under
     the t\*-swap in every context.
   - (E″) is closedness of the sections, a condition on the points the caps do not supply.

   The axioms so obtained are reflexivity, (IB), strict (G), (FC), closed sections, competitiveness, (LA) with
   C_L = Σ ∪ {T1}, direct (C), (LF) and T1 undominated.
   - No barrier in §1 excludes the design, because Theorem 5.1, FF2 4.1, Q3.25 and CC2 5.7 need T1 selected.
   - Q4.2 still applies: in any such cover some world has only degenerate endorsers, or fails (NC). Every endorser
     must vanish on the clone record (Prop 4.3). So the clone tie is a natural carrier of the non-additivity Q4.2
     demands.
5. **Where it stops (§5).** I could not construct (w̄, c) with (M′) and (E″) for any selection.
   - **Equivalent form (§5.1).** Three leading functions f_i = c − w̄_i, with f(C_p) = −p, Σf ≥ −1, and an
     argmax-increment cap rule. The one hard requirement is context transport (CT) of caps.
   - **A necessary sandwich condition** on the selection alone (Prop 5.2).
   - **The additive sub-ansatz (Prop 5.3).** With additive f, (M′) reduces to an explicit list (A1)–(A5).
   - **One PROVED obstruction (Prop 5.4).** For the clone, additive f and G are impossible. A Lyapunov half of t\*
     has zero additive increments at every level, yet competitiveness forces some world to accept it strictly.
     So the clone needs a leading level that is **non-additive inside S = C △ T1**.

**Single most important open point.** Is there a leading level f = c − w̄, necessarily non-additive inside S, that
satisfies swap invariance and context transport (CT) of argmax-increment caps (§5.4)? A yes, with closed sections
(E″), is a full (FC) cover of T1 with T1 unselected, by Theorem 4.1.

---

## 1. Which barriers need T1 selected

Throughout §1, T1 ∈ C_L and T1 ≈ C_{p\*} for a selected C_{p\*} ≠ T1. Proposition 1(b) of HH1 forces such a p\* in
every cover (KKM; no transitivity).

**Proposition 1.1 (CHECKED: reading of M3 §3 and HH1 §2.2; the repair step is PROVED).** The ranking-level step of
M3.4.3, which is the only place where Q4.2 and M3.10′ touch the ranking beyond Proposition 1(a), needs only the tie
T1 ≈ C_{p\*}. The same holds for L4.1.3, the same step on error indicators.

*Proof.*
1. **The step.** Fix an endorser ν_k of all relevant comparisons at world k. Let Y = T1 off D_m be regular, and let
   C_p ≼_k Y with C_p selected and tied with T1. One needs ν_k(λ_kY − λ_kT1) ≥ 0.
2. **Both inequalities come from relevant comparisons.** T1 ∈ C_L and C_p is regular, so T1 ≼_k C_p is relevant
   and gives ν_k(λC_p − λT1) ≥ 0. C_p ∈ C_L and Y is regular, so C_p ≼_k Y is relevant and gives
   ν_k(λY − λC_p) ≥ 0.
3. **Add.** By linearity, ν_k(λY − λT1) ≥ 0. This is HH1 Lemma 2.1.
4. **What is not used.** The world k is supplied by competitiveness of C_p (KKM), not of T1. Nothing uses T1 = C_p.
   The remaining steps (localisation, Lyapunov, separation, limit) are field-level. ∎

**Consequence (PROVED from 1.1 and Q4.2 at its recorded status).** Every cover in which T1 is tied but not selected
has a world that fails (NC) or does not add up. So lead (A) does **not** evade the adding-up barrier. It can only
supply the non-additivity that the barrier demands.

**Proposition 1.2 (CHECKED).** The following need T1 selected, or a substitute for it.
- **FF2 Thm 4.1 and HH2 Thm 5.1/Cor 5.3.** Step 5 (= Step 1 run for T1) uses competitiveness of T1 on supp q₀. With
  T1 only tied, (FC) gives weak competitiveness (HH1 Prop 2). The step then needs HH1's strengthened (H3), which
  endorses non-reversals (Thm 4.1″, stated under (TC)).
- **Q3.25 step (b)1 and CC2 Cor 5.7.** These are HH1's two gaps, verbatim.

**Proposition 1.3 (CHECKED).** L3.4 and HH2 Lemma 3.1/Prop 3.2 are statements about the selection and single
comparisons. They bind whether or not T1 is selected.

**Reading.** Lead (A) removes exactly the local-field barriers. It keeps the global adding-up barrier. A design of
type (A) must therefore have three properties:
- (i) its selected layer need not be pointwise Bayes for any fixed strictly guiding field near T1;
- (ii) the selection may even be a Bayes family of an additive ranking (FF2's Steps 1–4 then hold harmlessly, and
  Steps 5–6 have nothing to act on);
- (iii) some world's relevant comparisons, T1's tie included, admit no strictly positive endorser.

Proposition 4.3 shows that a clone tie produces (iii) automatically.

---

## 2. Rigidity of an unselected tie

Write C := C_{p\*}, t\* := rec(C, T1) and S := supp t\* = C △ T1, which is non-null.
- For Z any model, put Z_B := Z ⊕ C|S (Z off S, C on S) and Z_T := Z ⊕ T1|S.
- For E ⊆ S, write t\*|_E for t\* restricted to E (ι elsewhere).
- Write S⁺_i ⊆ S for the set where T1's advice is strictly better than C's at world i, and S⁻_i for the set where it
  is strictly worse.

**Lemma 2.1 (PROVED).** Assume (IB) and strict (G), with T1 ≈ C at every world.
- (a) t\* and t\*⁻¹ lie in every 𝒜_i. Hence Z_B ~_i Z_T for every Z and every i.
- (b) S = S⁺_i ∪ S⁻_i a.e., and both parts are non-null, for every i.
- (c) S contains no non-null set on which T1 is worse than C at all three worlds, nor one on which it is better at
  all three.

*Proof.*
- (a) T1 ≼_i C and C ≼_i T1 give t\*⁻¹, t\* ∈ 𝒜_i. (IB) transports both to every realisation.
- (b) On S the two advices differ. Distinct advices have distinct world-i ranks off null coordinate hyperplanes, so
  S = S⁺_i ∪ S⁻_i a.e.
  - If S⁺_i were null, t\* would be a non-null i-worsening record. Then t\*⁻¹ is improving, and strict (G) rejects
    it, contradicting (a).
  - If S⁻_i were null, t\* itself would be improving.
- (c) Both models are coherent. On unanimous pairs both accept the positive orientation and neither gives ×, so S
  consists of mixed pairs where each gives one of +, 0, −. Moving between two distinct members of {+, 0, −} on a
  mixed pair is better at the worlds where one sign of h holds and worse where the other holds. Both sign sets are
  nonempty. ∎

CHECKED (`checks.py` (5)). For C = C_u = {g : Σg > 0} and each ε ∈ {1/20, 3/10, 1/2, 9/10}, there are exact rational
pairs at which C_u accepts, T1 is silent, and h_i has either sign, for each i. Openness makes the corresponding sets
non-null. So Lemma 2.1(b) is satisfiable for the clone of C_u.

**Lemma 2.2 (PROVED).** Assume (FC) and (IB). Every ordering extension R_i of ≼_i (Suzumura; HH2 Prop 1.3) has
Z_B ~_{R_i} Z_T for every Z. In particular, a real potential Φ_i representing R_i is invariant under the S-swap in every
context.

*Proof.* R_i contains ≼_i, and both Z_B ≼_i Z_T and Z_T ≼_i Z_B hold by Lemma 2.1(a). ∎

**Proposition 2.3 (off-S rigidity; PROVED).** Assume (IB). Let r be a record with supp r ∩ S null and with from-advice
equal to T1's on supp r. Then r is also a record out of C, and:
- T1 ≼_i T1 ⊕ r ⟺ C ≼_i C ⊕ r, and T1 ⊕ r ≼_i T1 ⟺ C ⊕ r ≼_i C;
- consequently T1 is competitive on supp p\* against every model that agrees with T1 a.e. on S;
- suppose world k endorses, by a field ℓ_k with integrable envelope, every accepted comparison of C against models
  equal to C off H_n (FF2's (H3) at q₀ = p\*), and C is competitive. Then T1 is pointwise weakly w-Bayes for ℓ
  a.e. on H_n ∖ S, for the same w ∈ Δ_{supp p\*} that FF2 Step 1 gives for C.

*Proof.*
- **Same record.** C = T1 off S, so rec(T1, T1 ⊕ r) = r = rec(C, C ⊕ r) as records. (IB) gives the first line.
- **Competitiveness.** If X = T1 a.e. on S, then rec(T1, X) is supported off S and equals rec(C, C ⊕ (X off S)).
  Competitiveness of C gives a world in supp p\* accepting it.
- **Weak Bayes.** FF2 Step 1, run for C on H_n, gives w with C pointwise weakly w-Bayes a.e. on H_n. T1 = C off S. ∎

*Reading.*
- Every barrier whose test models agree with T1 on S binds T1 exactly as if it were selected.
- The escape from FF2 lives **inside S = C △ T1**, a non-null set of mixed pairs, a union of conic wedges between
  ∂D_{K\*} and ∂D_{T1}, where K\* is C's credal set.
- If K\* ⊆ int T1, then S contains the whole outer side of ∂D_{T1} (C accepts, T1 is silent). FF2-type tests near
  ∂D_{T1} that add acceptances just outside it are then records out of T1 that are **not** records out of C. That is
  where T1 can be incomparable to its own perturbations.

**Lemma 2.4 (piece calculus; PROVED).** Assume (IB) and (FC). Let E₁, …, E_m partition S, and suppose all the
records t\*|_{E_1}, …, t\*|_{E_m} lie in 𝒜_i. Then each of them is an i-tie, i.e. its inverse also lies in 𝒜_i.

*Proof.* Fix Z, and put A₀ := Z_B and A_s := A_{s−1} ⊕ T1|E_s. Then rec(A_{s−1}, A_s) = t\*|_{E_s}, because on
E_s the from-advice is C's, whatever was done on the other pieces. So A₀ ≼_i A₁ ≼_i ⋯ ≼_i A_m = Z_T. Lemma 2.1(a)
adds Z_T ≼_i Z_B. In this cycle, (FC) forbids every strict step, so every step is a tie. ∎

Write 𝒜(E) := {i : t\*|_E ∈ 𝒜_i}. The axioms give three further constraints:
- **competitiveness of C** against C ⊕ T1|E: 𝒜(E) ∩ supp p\* ≠ ∅;
- **strict (G):** i ∈ 𝒜(E) strictly when E ⊆ S⁻_i, and i ∉ 𝒜(E) when E ⊆ S⁺_i;
- **undominatedness of T1:** Y_E := T1 ⊕ C|E has rec(Y_E, T1) = t\*|_E. So 𝒜(E) = Ω forces t\*|_E to be a tie at
  every world (else Y_E dominates T1), and then direct (C) needs Y_E ∈ C_L.

**Proposition 2.5 (conic twins; PROVED).** Assume (IB), (FC), direct (C) and T1 ≈ C. Let v be a finite vector of
finite non-atomic signed measures on S. Suppose that at every world the verdict on t\*|_E, for E ⊆ S, is a function
of v(E) alone ("statistics-determined pieces"). Then, writing E_½ for any set with v(E_½) = v(S)/2:
- the set 𝒜_½ := 𝒜(E_½) is the same for all such sets;
- 𝒜_½ ∩ supp p\* ≠ ∅, and every world of 𝒜_½ treats every half-piece as a tie;
- 𝒜_½ ≠ Ω.

*Proof.*
1. **Independence of the choice.** 𝒜(E) depends on v(E) only. Also v(S∖E_½) = v(S)/2, so 𝒜(S∖E_½) = 𝒜_½.
2. **Non-empty on supp p\*, and ties.** Competitiveness gives a world j ∈ 𝒜_½ ∩ supp p\*. At any j ∈ 𝒜_½ both
   pieces of the partition {E_½, S∖E_½} are accepted, so Lemma 2.4 makes both ties at j.
3. **Not every world.** Suppose 𝒜_½ = Ω. Then for every half-set E, t\*|_E is a tie at all worlds, so Y_E ≈ T1.
   - Since T1 ∈ C_L, direct (C) puts Y_E in C_L. So Y_E is coherent, and in particular a cone mod null.
   - **Choose twins.** Let B be the open unit ball. By Lyapunov there are E_a ⊆ S ∩ B and E_b ⊆ S ∖ B with
     v(E_a) = v(S ∩ B)/2 and v(E_b) = v(S ∖ B)/2. Then E := E_a ∪ E_b and E′ := E_a ∪ ((S ∖ B) ∖ E_b) are both
     half-sets.
   - Y_E and Y_{E′} agree on B. A cone is determined by its trace on B, so if both were cones they would agree a.e.
   - They would then give E_b = (S ∖ B) ∖ E_b a.e. That forces S ∖ B to be null. But S is a non-null cone (both
     models are cones), so S ∖ B is non-null.
   - So one of Y_E, Y_{E′} is incoherent, a contradiction. ∎

*Reading.* Any statistics-determined acceptance of the pieces of t\* has the same three features:
- a fixed proper nonempty set of worlds treats all v-proportional half-pieces as ties;
- the other worlds reject them;
- incoherent models Y_E are tied with T1 only at some worlds.

This is not a contradiction. It is consistent with Lemma 2.4. But it shows that the clone tie must be supported by
**non-additive** structure inside S at the worlds in 𝒜_½: a potential invariant under all v-half swaps at those
worlds, yet strictly monotone under pointwise worsening. Section 4 builds a potential of exactly this kind from a
defence map, with tie-breaking by τ and by a strictly guiding G_i with G_i(t\*) = 0.

---

## 3. HH2 Theorem 2.1 is vacuous on the full domain, and its repair

Recall HH2 §2:
- the defence map is w : models → Δ, with w(C_p) = p;
- τ(X) := 0 for X ∈ Σ, and 1 otherwise;
- the potential is Ψ_i(X) := (−w_i(X), τ(X), G_i(X)), ordered lexicographically, smaller being better;
- caps K_i := {rec(C_p, X) : X ≠ C_p, p − w(X) ∈ Γ_i};
- (M): every non-identity record of W_i ∪ K_i strictly increases Ψ_i along every realisation.

**Proposition 3.1 (PROVED; CHECKED `checks.py` (1)).** On the full domain no defence map satisfies (M).

*Proof.*
1. **The test model.** Let X_× be the model giving contradictory advice × on every pair. Every C_p is coherent, so it
   gives × on a null set only, and × has the worst rank at every world. Hence rec(C_p, X_×) is a non-null
   i-worsening record, for every i and p. It lies in W_i.
2. **Apply (M) at p = e_k, i ≠ k.** At the realisation (C_{e_k}, X_×), (M) needs
   (0, 0, G_i(C_{e_k})) <_lex (−w_i(X_×), 1, G_i(X_×)).
   Since w_i ≥ 0, this forces w_i(X_×) = 0.
3. **Conclude.** Letting k range over the worlds other than i gives w_i(X_×) = 0 for every i. So w(X_×) = 0 ∉ Δ. ∎

The same argument applies on every domain containing a model that is strictly worse, at each world i, than the vertex
models C_{e_k} with k ≠ i. Pointedness of the cones plays no role.

**Proposition 3.1′ (PROVED).** HH2's hypothesis (E) is also unsatisfiable on the full domain, for any map into Δ and
any cones with Γ₁ ∩ Γ₂ ∩ Γ₃ = {0}, the argmax cones included.

*Proof.* rec(C_p, X_×) ∈ W_i for every p and i, as above. So (E) gives p − w(X_×) ∈ Γ₁ ∩ Γ₂ ∩ Γ₃ = {0} for every
p ∈ Δ. That is, w(X_×) = p for all p, which is impossible. ∎

*Reading.* (E) asks that the sections be **exactly** the cap sets. The axiom only asks that they be closed, and
F_i(X_×) = Δ is closed. So (E) is replaced below by closedness itself, restricted to the part of each section that the
caps do not already supply.

**Theorem 3.2 (repaired generator scheme; PROVED).**

*Data.*
- An injective selection p ↦ C_p of coherent models (no continuity assumed), with Σ := {C_p}.
- A defence point w̄ : models → Δ and a slack c : models → [0, ∞), with w̄(C_p) = p and c(C_p) = 0.
- τ as above, and strictly guiding additive G_i with integrable envelope.
- The potential Ψ_i(X) := (c(X) − w̄_i(X), τ(X), G_i(X)), lexicographic.
- The argmax cones Γ_i := {x ∈ T : x_i ≥ x_k ∀k}, with T := {Σx = 0}.
- Generators W_i (the i-worsening records, ι included) and K_i := {rec(C_p, X) : X ≠ C_p, p − w̄(X) ∈ Γ_i}.
- The relation 𝒜_i := W_i ∪ K_i, with no closure taken.

*Hypotheses.*
- **(M)** Every non-identity record of W_i ∪ K_i strictly increases Ψ_i along every realisation.
- **(E″)** For every model X and world i, the section F_i(X) = {p : rec(C_p, X) ∈ 𝒜_i} is closed. It always contains
  the closed cap set Cap_i(X) := {p : p − w̄(X) ∈ Γ_i}, for X ∉ Σ. So (E″) is a condition on the *extra* points:
  those p ∉ Cap_i(X) at which rec(C_p, X) is worsening, or is a cap issued by another selected model. Every limit of
  extra points must lie in F_i(X).

*Conclusions.* Reflexivity, (IB), strict (G), (FC), closed sections, competitiveness, every C_p undominated, every
X ∉ Σ dominated by C_{w̄(X)}, C_L = Σ, no non-trivial ties (hence (C)), and (LF) on the full domain.

*Proof.* HH2's proof is used verbatim except at four points.
1. **Covering.** The cap sets depend only on w̄ ∈ Δ, so (K3) for the argmax cones holds as in HH2. CHECKED exactly
   on Δ ∩ (1/12)ℤ³, `checks.py` (3): 8281 pairs, 0 failures. Since Cap_i(X) ⊆ F_i(X), every C_p is competitive.
   Closedness is (E″).
2. **Protection.** Let Y ≠ C_p with Y ≼_i C_p at every i. By (M), Ψ_i(Y) < Ψ_i(C_p), so c(Y) − w̄_i(Y) ≤ −p_i for
   every i. Summing over i gives 3c(Y) − 1 ≤ −1, so c(Y) = 0 and w̄_i(Y) ≥ p_i for all i. Both points lie in Δ, so
   w̄(Y) = p. The second coordinate then gives τ(Y) = 0, so Y = C_q with q = w̄(Y) = p, a contradiction.
3. **Domination.** For X ∉ Σ put q := w̄(X). Then q − w̄(X) = 0 lies in every Γ_i, so C_q ≼_i X at every world via a
   cap. If X ≼_i C_q were accepted, (M) would give Ψ_i(X) < Ψ_i(C_q). But
   Ψ_i(C_q) = (−q_i, 0, ·) <_lex (c(X) − q_i, 1, ·) = Ψ_i(X). So the cap is strict. CHECKED `checks.py` (4): the only
   point in all three cap sets is w̄(X).
4. **Where (E) was used.** In HH2, (E) served only to identify the sections. Protection, domination, (FC) and strict
   (G) use (M) alone. ∎

*Both vacuities are gone.* Put w̄(X_×) := u and c(X_×) := 1.
- (M) at (C_p, X_×) reads (−p_i, 0) <_lex (2/3, 1), which is true for every p and i. CHECKED `checks.py` (2) on
  Δ ∩ (1/24)ℤ³.
- F_i(X_×) = Δ is closed.

Whether the repaired scheme is non-vacuous **in full** (all realisations of all generators) is open (§5). It is the
same open question as for HH2 2.1, now without the trivial obstruction.

---

## 4. The clone theorem: T1 tied with a selected model, not selected

**Data.**
- The data of Theorem 3.2: an injective coherent selection, Σ, w̄, c, strictly guiding G_i, the argmax cones Γ_i,
  W_i and caps K_i. Caps are issued against every model X, T1 included.
- T1 ∉ Σ, a point p\* ∈ Δ, C := C_{p\*}, t\* := rec(C, T1), S := supp t\*, and Z_B, Z_T as in §2.
- **Clone values:** w̄(T1) := p\*, c(T1) := 0, and τ(X) := 0 for X ∈ Σ ∪ {T1}, τ(X) := 1 otherwise.
- **Relations:** K_i° := K_i ∖ {t\*}, N := {t\*, t\*⁻¹}, and 𝒜_i := W_i ∪ K_i° ∪ N. No closure is taken.
- The potential Ψ_i(X) := (c(X) − w̄_i(X), τ(X), G_i(X)), lexicographic.

**Hypotheses.**
- **(H_inj)** No C_q with q ≠ p\* agrees a.e. on S with C, or with T1.
- **(Mix)** t\* is mixed at every world: S⁺_i and S⁻_i are non-null for every i.
- **(G0)** G_i(t\*) = 0 for every i.
- **(M′)**
  - (i) Every non-identity record of W_i ∪ K_i° strictly increases Ψ_i along every realisation.
  - (ii) w̄(Z_B) = w̄(Z_T) and c(Z_B) = c(Z_T) for every model Z.
- **(E″)** Every section F_i(X) = {p : rec(C_p, X) ∈ 𝒜_i} is closed.

**Lemma 4.0 (PROVED).** Under (Mix), strictly guiding additive G_i with integrable envelope and (G0) exist.

*Proof.* Start from any strictly guiding additive G⁰_i with integrable envelope. Write P > 0 for the contribution of
S⁻_i to G⁰_i(t\*), and −N < 0 for that of S⁺_i. Multiply the penalty G⁰_i(h, ·) by N/P for h in S⁻_i, and leave it
unchanged elsewhere. Positive pairwise rescaling keeps strict guidance and the envelope, and the new value of t\* is
(N/P)P − N = 0. ∎

(Mix) holds for C = C_u, for every ε tested (`checks.py` (5); §2). It is forced in any cover where T1 ≈ C
(Lemma 2.1(b)).

**Theorem 4.1 (clone theorem; PROVED).** Under (H_inj), (Mix), (G0), (M′) and (E″), the system (𝒜_i) satisfies
reflexivity, (IB), strict (G), (FC), (S) (closed sections; every C_p competitive on supp p), (LA) with
C_L = Σ ∪ {T1}, direct (C) and (LF) at T1. T1 is undominated, T1 ≈ C, and T1 is not selected.

*Proof.*
1. **The three generator families are disjoint off ι.**
   - t\* and t\*⁻¹ are mixed, so neither lies in W_i.
   - A cap equal to t\* has from-advice C on S. By (H_inj) it is issued by C itself, against X = T1, and it is
     removed from K_i°.
   - A cap equal to t\*⁻¹ would be issued by a selected model agreeing with T1 on S, which (H_inj) excludes.
2. **N is Ψ-neutral.** Fix Z.
   - **First coordinate:** equal, by (M′)(ii).
   - **τ.** Z_B ∈ Σ ∪ {T1} forces Z_B = C, by (H_inj) and since T1 ≠ C on S. Likewise Z_T ∈ Σ ∪ {T1} forces
     Z_T = T1. Both happen exactly when Z = C off S, because C = T1 off S. So τ(Z_B) = τ(Z_T).
   - **G_i:** equal, by additivity and (G0).
3. **(IB), reflexivity.** 𝒜_i is a record set containing ι.
4. **(FC).**
   - Every non-identity record of W_i ∪ K_i° strictly increases Ψ_i at every realisation. Its inverse cannot also
     lie in W_i ∪ K_i°, and by step 1 it does not lie in N, so it is strict.
   - The only ties are N, and they are Ψ-neutral.
   - So the lexicographic preorder of Ψ_i is an ordering extension that keeps strict parts. HH2 Prop 1.3 (converse)
     gives (FC).
5. **Strict (G).** W_i ⊆ 𝒜_i. A non-null improving record is not in N (Mix). If it were in K_i°, then (M′)(i) for
   it and for its worsening inverse would give contradictory strict inequalities (HH2's argument).
6. **Sections and competitiveness.**
   - For X ∉ Σ, Cap_i(X) ⊆ F_i(X). For X = T1 and p = p\*, the cap t\* was removed, but t\* ∈ N, so still
     p\* ∈ F_i(T1).
   - By the argmax covering (Theorem 3.2, step 1), every C_p is competitive on supp p.
   - For X = C_q, reflexivity puts q in F_i(C_q), and the caps of other p cover the rest.
   - Closedness is (E″).
7. **Protection.** Let Y ≠ D with Y ≼_i D at every i, where D ∈ Σ ∪ {T1}. Every accepted comparison weakly
   increases Ψ_i, strictly off N. So c(Y) − w̄_i(Y) ≤ c(D) − w̄_i(D) = −w̄_i(D) for every i.
   - Summing gives c(Y) = 0 and w̄(Y) = w̄(D).
   - At equal first coordinates τ(Y) ≤ τ(D) = 0, so Y ∈ Σ ∪ {T1}.
   - By injectivity and w̄(T1) = p\*, the only possibility is {Y, D} = {C, T1}. That pair is tied at every world, not
     a domination.
   - So every C_p and T1 are undominated.
8. **Domination of the rest.** Let X ∉ Σ ∪ {T1} and q := w̄(X). The caps rec(C_q, X) lie in K_i° at every world (they
   are not t\*, since X ≠ T1), so C_q ≼_i X everywhere.
   - If X ≼_i C_q were accepted through W_i ∪ K_i°, then Ψ_i(X) < Ψ_i(C_q). But Ψ_i(C_q) = (−q_i, 0, ·) <_lex
     (c(X) − q_i, 1, ·) = Ψ_i(X).
   - If it were accepted through N, then rec(X, C_q) = t\*⁻¹ would force C_q = C and X = T1, which is excluded.
     rec(X, C_q) = t\* would make C_q agree with T1 on S, which (H_inj) excludes.
   - So C_q dominates X. Hence C_L = Σ ∪ {T1} (T1 is coherent), and (LA) holds.
9. **Direct (C).** By step 4 the only non-trivial ties are realisations of N. Let X ≈ D with D ∈ C_L and X ≠ D. Then
   rec(X, D) ∈ N. By step 2's τ analysis this forces {X, D} = {C, T1} ⊆ C_L.
10. **(LF)** holds on the full domain. ∎

**Proposition 4.2 (what the clone escapes; PROVED from §1).** In a system given by Theorem 4.1:
- the hypotheses "T1 = C_{q₀}" of FF2 Thm 4.1, HH2 Thm 5.1 and Cor 5.3, Q3.25 (b)1 and CC2 Cor 5.7 all fail;
- no continuity in measure of the selection is used anywhere, so lead (B) is covered by the same theorem;
- the vertex lemma (HH2 3.1) and L3.4 still constrain the selection. They are hypotheses-level checks on w̄ via (E″).

**Proposition 4.3 (the clone carries the non-additivity; PROVED).** In a system given by Theorem 4.1:
- every endorser ν_i of the relevant comparisons at world i satisfies ν_i(λ_iC − λ_iT1) = 0, because T1 ≼_i C and
  C ≼_i T1 are both relevant;
- by Prop 1.1 and Q4.2, at least one world has only degenerate endorsers, or fails (NC).

So in particular no world of such a system may be endorsed by an integrable strictly guiding field φ with
φ(t\*) ≠ 0 at that world. Hence the leading levels must be blind, jointly, along the clone. In the additive form of
§5.3 this is the requirement Δf(t\*) = 0.

---

## 5. Where the construction stops

### 5.1 An equivalent form, and the one hard requirement

**Lemma 5.1 (PROVED).** Put f_i := c − w̄_i. Then (w̄, c) ↦ f = (f_1, f_2, f_3) is a bijection onto the maps
f : models → ℝ³ satisfying three conditions:
- (a) Σ_i f_i ≥ −1;
- (b) 3f_i ≤ 1 + Σ_j f_j for every i;
- (c) f(C_p) = −p for every p, and f(T1) = −p\* in the clone version.

The inverse is c = (1 + Σf)/3 and w̄_i = c − f_i. Under it:
- the leading level of Ψ_i is f_i;
- c(X) = 0 iff Σf(X) = −1;
- **the cap rule becomes an argmax-increment rule:** rec(C_p, X) ∈ K_i iff f_i(X) − f_i(C_p) = max_j (f_j(X) − f_j(C_p)).

*Proof.*
- **Bijection.** Σw̄ = 1 gives 3c − Σf = 1. Then c ≥ 0 is (a), and w̄_i ≥ 0 is (b). On selected models c = 0 and
  w̄ = p.
- **Cap rule.** p_i − w̄_i(X) = p_i − c(X) + f_i(X) = f_i(X) − f_i(C_p) − c(X). ∎

So (M′)(i) asks two things:
- **(W-mon)** Each f_i is weakly increasing along every realisation of every i-worsening record, with the τ/G
  tie-break when the increment is zero.
- **(CT) context transport.** For every cap rec(C_p, X) at world i, the increment of f_i is ≥ 0 at **every**
  realisation (Z, Z ⊕ X|_D), D := supp, again with the tie-break when it is zero. At the base realisation (C_p, X)
  the increment is max_j Δ_j ≥ (1/3)Σ_jΔ_j = c(X) ≥ 0 automatically.

(CT) is where non-additive f fail: an increment that is maximal at the base realisation must stay non-negative in every
context. (M′)(ii) asks f(Z_B) = f(Z_T) for all Z.

### 5.2 A necessary condition on the selection alone

**Proposition 5.2 (sandwich; PROVED).** Suppose (M′)(i) holds. Let Y ∉ Σ ∪ {T1}, and let a¹, a², a³ ∈ Δ be such that,
for each i, C_{a^i} is pointwise weakly i-worse than Y and strictly on a non-null set. Then a¹₁ + a²₂ + a³₃ < 1. For
Y = T1 (clone version) the same holds with ≤.

*Proof.*
1. rec(Y, C_{a^i}) is i-worsening. At its realisation (Y, C_{a^i}), (M′)(i) gives
   (f_i(Y), 1, ·) <_lex (−a^i_i, 0, ·).
2. So f_i(Y) < −a^i_i for each i.
3. Sum and use Lemma 5.1(a): −1 ≤ Σf(Y) < −Σ_i a^i_i.
4. For T1, τ(T1) = 0 only gives ≤. ∎

*Reading.*
- With a¹ = a² = a³ the hypothesis is never met. Each C_a is pointwise Pareto-optimal on mixed pairs, so a Y
  pointwise weakly better than C_a at every world equals C_a.
- The condition bites only for triples tilted **towards** their own world, and only when there is a Y that beats each
  of them at its own world.
- A family whose advice on each mixed pair moves monotonically with the weights (more weight on i, better at i) meets
  it: tilted triples then disagree on some pair in incompatible directions, so no such Y exists. I have not proved
  this for the plain posterior family. It is a finite check per pair-type, and I flag it as the first test for any
  candidate selection.

### 5.3 The additive sub-ansatz

Let f_i(X) = κ + ∫ φ_i(h, X(h)) dμ(h), with measurable φ_i having an integrable envelope (κ fixed so that (c) can hold).
This is the one place where an additive level enters. It is a candidate *leading level* inside the generator scheme,
paired with the non-additive τ and the argmax-increment acceptance rule. It is not a starting lexicographic base:
acceptance is not "Φ ≥ 0".

**Proposition 5.3 (PROVED reduction).** With additive f, hypotheses (M′) and Lemma 5.1(a)–(c) hold iff all of the
following hold.
- **(A1)** Each φ_i is weakly guiding. Moreover, for each D ∈ Σ ∪ {T1}, φ_i(h, D(h)) > φ_i(h, b) for a.e. h and
  every advice b strictly better than D(h) at world i.
  - The first clause is (W-mon).
  - The second makes a zero-increment worsening record never end at D, so τ cannot drop.
- **(A2)** Σ_iφ_i(h, ·) is minimised at D(h) for a.e. h and every D ∈ Σ ∪ {T1}. That is, every selected model and T1
  are u-Bayes for the weakly guiding field Σf. Also Σf(D) = −1.
- **(A3)** f(C_p) = −p, f(T1) = −p\*, and 2f_i − f_j − f_k ≤ 1 for all models.
- **(A4)** (CT) reduces to its zero-increment case. Let r ≠ t\* be a non-null record out of some C_p with
  Δ(r) := f(C_p ⊕ r) − f(C_p) = 0. All three worlds accept r as a cap, since every increment is maximal. Then
  - **(A4a)** G_i(r) > 0 at every world i.
  - **(A4b)** If D ∈ Σ ∪ {T1} carries r's to-advice on supp r, then D with C_p's advice restored on supp r also
    lies in Σ ∪ {T1}.

  *Why these are exactly the zero-increment cases of (CT).* At a realisation (Z, Z′) the first coordinates are equal.
  - (A4b) says τ(Z) = 1 > τ(Z′) = 0 never happens.
  - When τ(Z) = τ(Z′), (A4a) gives strict increase. Realisations with τ(Z) = τ(Z′) = 1 always exist (put X_× on a
    non-null set off supp r), so (A4a) is also necessary.
- **(A5)** The clone is f-blind: Δf(t\*) = 0, i.e. f(T1) = f(C).

*Proof.*
- **Context-free increments.** With additive f, increments do not depend on the context, so (CT) at the base
  realisation implies it everywhere.
- **Positive maximal increment.** If Δ_i = max_j Δ_j > 0, the increment is positive at every realisation.
- **Zero maximal increment.** If max_j Δ_j = 0, then Σ_jΔ_j = 3c(C_p ⊕ r) ≥ 0 forces Δ = 0. The lexicographic
  tie-break is then (A4).
- **(W-mon)** is the first clause of (A1).
- **Zero-increment worsening.** A worsening record with zero increment needs τ(Z) ≤ τ(Z′), and G handles equal τ.
  The second clause of (A1) is exactly the statement that no such record ends at a model of τ = 0 starting from τ = 1.
  - Ending at D ∈ Σ ∪ {T1}: Z is i-better than D on supp r, and a zero φ_i-increment there would contradict the
    strict separation.
  - Ending at another model of τ = 0: these are the same set.
- **(A2) and (A3).** Lemma 5.1(a) with equality on Σ ∪ {T1} gives (A2): Σf is minimised at −1 exactly there, and by
  additivity pointwise. (A3) is Lemma 5.1(b),(c).
- **(A5)** is (M′)(ii) for additive f. ∎

*What the sub-ansatz would achieve.* (For the clone, Prop 5.4 below closes it.)
- **Every barrier in §1 is compatible with it.**
  - The field Σf is weakly guiding and degenerate. Theorem gm and M3 need strict guidance, and Q4.2 in fact demands
    degeneracy.
  - T1 is not selected, so FF2 and Theorem 5.1 do not apply.
- **The selected layer is an f-parametrised family of Σf-minimisers.** By (A2), C_p and C_q can differ only on the
  Σφ-tie set. There the increment vectors of rec(C_p, C_q) lie in the plane {Σ = 0} and integrate to
  f(C_q) − f(C_p) = p − q.
- **The hard point is (A4).** For interior p, the records out of C_p supported on the tie set have increment vectors
  spanning the plane {Σ = 0}: they must integrate to p − q for every q.
  - So zero-increment records r out of C_p (Δ(r) = 0, r ≠ ι) will typically exist.
  - (A4) needs every such r to have **positive G-integral at all three worlds**. Equivalently, on the cone of
    f-null modifications of each C_p, the strictly guiding tie-break G must increase at every world.
  - Here G is ours to choose, subject only to (G0).

  I could not decide this. Lyapunov makes zero sums easy to produce whenever the increment directions out of C_p
  positively span the plane, and they do in aggregate. But a zero sum needs the pieces to be **compatible advices on
  disjoint sets**, which is a genuine restriction.

  This is the sharpest form I can give of the remaining question for the sub-ansatz.

**Proposition 5.4 (the clone excludes additive levels; PROVED).** In the scheme of Theorem 4.1, suppose
X ↦ f(X) and X ↦ G(X) are additive with integrable envelopes, at least for records supported in S. Then (M′)(i)
fails. Hence in any system obtained from Theorem 4.1, at some world i the leading level f_i = c − w̄_i is
**not** additive on the sub-records of t\*.

*Proof.*
1. **A half-record.** Apply Lyapunov to the non-atomic vector measure E ↦ (μ(E), Δf(t\*|_E), ΔG(t\*|_E)) on S, which
   has seven components. It gives E ⊆ S with value half that of S. By (A5) and (G0), Δf(t\*) = 0 and ΔG(t\*) = 0, so
   r := t\*|_E has Δf(r) = 0 and ΔG(r) = 0. Moreover μ(E) = μ(S)/2, so r ≠ ι and r ≠ t\*.
2. **r is accepted somewhere.** Competitiveness of C against C ⊕ T1|E gives some world i with r ∈ 𝒜_i. Here r ∉ N,
   since r ≠ t\* and r has from-advice C on its support. So r ∈ W_i ∪ K_i°, and (M′)(i) applies to it. (In fact
   r ∉ W_i, because G_i is strictly guiding and ΔG_i(r) = 0. It is a cap at every world, since all its f-increments
   are equal.)
3. **(M′)(i) fails at a context with τ = 1.** Let Z be C on E and X_× on S ∖ E (non-null), arbitrary elsewhere, and
   put Z′ := Z ⊕ T1|E. Neither Z nor Z′ is coherent, since each gives × on a non-null set. So τ(Z) = τ(Z′) = 1.
   - f and G are additive, so Ψ_i(Z′) − Ψ_i(Z) = (Δf_i(r), 0, ΔG_i(r)) = (0, 0, 0).
   - So r does not strictly increase Ψ_i at this realisation, contradicting (M′)(i). ∎

*Reading.*
- This is the scheme-level counterpart of Prop 2.5. The clone tie forces a world whose leading level is non-additive
  **inside S**.
- It closes the additive sub-ansatz of §5.3 *for the clone*. Conditions (A1)–(A4) remain a live reduction for the
  version with **T1 selected**, where (A5) and (G0) are absent. That version is not lead (A), and HH2 Thm 5.1 binds it
  if the selection is continuous in measure.
- The half-record is the obstruction of Lemma 2.4 seen through Ψ. Both halves of t\* have zero additive increment, so
  only a non-additive level can make the acceptance of one half strict while the whole stays a tie.

### 5.4 Failure report

- **Where the global attempt broke.** Not at an axiom. Theorem 4.1 delivers every axiom from (M′) and (E″). It broke at
  constructing f = c − w̄ with context transport (CT) and swap invariance.
- **Additive f.** Prop 5.4 closes this case for the clone. (The case with T1 selected reduces to (A4).)
- **Non-additive f.** f must be non-additive on the sub-records of t\* at some world, and context-uniformly monotone
  along argmax-selected caps (CT). I found no such f, and I proved no obstruction to it.
- **No PROVED obstruction to lead (A) as such.** What is proved:
  - two obstructions to HH2's *statement* (Props 3.1, 3.1′), both removed by the repair;
  - one obstruction to the additive version of the clone scheme (Prop 5.4).

---

## 6. Status

| # | Statement | Label |
|---|---|---|
| 1.1 | Q4.2 / M3.10′ / M0closed(b) / L4.1–2 need only T1 ≈ C_p, not T1 selected | CHECKED (reading); repair step PROVED |
| 1.2–1.3 | FF2 4.1, HH2 5.1/5.3, Q3.25, CC2 5.7 need T1 selected; L3.4 and vertex lemma bind regardless | CHECKED |
| 2.1 | the tie record t\* is mixed at every world, and contains no all-better or all-worse part | PROVED; (5) CHECKED for C_u |
| 2.2 | t\* is a tie in every ordering extension, in every context | PROVED |
| 2.3 | off-S rigidity: T1 and C have the same verdicts off S; T1 competitive against models agreeing with T1 on S | PROVED |
| 2.4 | piece calculus: a partition of S all accepted at one world consists of ties | PROVED |
| 2.5 | conic twins: statistics-determined pieces have 𝒜_½ ≠ Ω, nonempty on supp p\*, with ties | PROVED |
| 3.1, 3.1′ | HH2 Thm 2.1's (M) and (E) are each unsatisfiable on the full domain (all-× model) | PROVED; (1) CHECKED |
| 3.2 | repaired generator scheme: slack c, defence point w̄, closedness (E″) | PROVED; (2)–(4) CHECKED |
| 4.0 | G_i with G_i(t\*) = 0 exist under (Mix) | PROVED |
| **4.1** | **clone theorem: (H_inj), (Mix), (G0), (M′), (E″) ⇒ every axiom, T1 ∈ C_L tied and unselected** | **PROVED** |
| 4.2–4.3 | barriers escaped; every endorser vanishes on the clone; Q4.2 ⇒ some world degenerate | PROVED (4.3 at Q4.2's status) |
| 5.1 | equivalent form: f = c − w̄, f(C_p) = −p, Σf ≥ −1, argmax-increment caps | PROVED |
| 5.2 | sandwich: necessary condition on the selection | PROVED |
| 5.3 | additive leading level: (M′) ⇔ (A1)–(A5) | PROVED |
| 5.4 | clone + additive f, G ⇒ (M′) fails; some world's f non-additive inside S | PROVED |
| — | existence of (w̄, c) with (M′), (E″) | open |
| — | cover of T1 | **not obtained** |

**Referee priorities.**
1. Theorem 4.1 step 2 (τ-neutrality of N), and step 7 (protection with weak inequalities, the case {Y, D} = {C, T1}).
2. Prop 3.1′: that (E) is required at worsening realisations from selected models. It is stated so in HH2 §2.
3. Prop 5.4 step 3: the choice of a context Z with τ = 1 on both sides.
4. Prop 1.1: that M3.4.3 is the only ranking-level use of tie transfer in Q4.2's chain (HH1 §2.2 says so; I re-read M3
   §3 only).

**Single most important open point.** Is there a non-additive leading level f : models → ℝ³ satisfying all of the
following?
- f(C_p) = −p, f(T1) = −p\*, Σf ≥ −1 and 3f_i ≤ 1 + Σf;
- f is invariant under the T1/C swap on S in every context;
- f is weakly monotone under pointwise world-i worsening;
- it is context-uniformly non-decreasing along every argmax-increment cap (CT).

By Prop 5.4 it must be non-additive inside S = C △ T1. A yes, with closed sections (E″), is a full (FC) cover of T1
with T1 unselected (Theorem 4.1).

## 7. Files

`ii3py/checks.py` (exact `fractions` arithmetic), output `ii3py/checks.out`:
- (1) the forced bounds w(X_×) ≤ 0 (Prop 3.1);
- (2) the repaired (M) at (C_p, X_×) on Δ ∩ (1/24)ℤ³;
- (3) argmax covering on Δ ∩ (1/12)ℤ³ (8281 pairs, 0 failures);
- (4) the KKM-point characterisation;
- (5) rational pairs where C_u accepts and T1 is silent with each sign of each coordinate, for four ε (Lemma 2.1(b)).
