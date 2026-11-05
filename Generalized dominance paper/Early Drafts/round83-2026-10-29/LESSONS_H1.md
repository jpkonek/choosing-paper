# LESSONS_H1: the foundations, 25 September to 8 October 2026

Reader H1. Access note: the Projects tool was not available to me. I read the device originals of the same documents instead:
- `~/mnt/CPMs/outputs/complete-class-research/`: kkm-calibration v1 to v7, kkm-benchmark-draft, realization-and-coherence.md, kkm-calibration-v7-audit.md, and "Loss Dominance Generalized (old).tex" (30 Sep, the KCM axioms);
- `~/mnt/CPMs/CHANGES_v19.md` and LSP_CPMs_v19a.tex, in place of `cpm-v19-split.md`;
- nonadditive_losses.tex and truth_directed_losses.tex;
- local copies of loss-relations-sdg, loss-relations-credal-families and full-coverage-homothetic-v2.

`bayes-profiles/` contains no .md files, only figures, scripts and the kkm-explainer TeX. I peeked at one document from 9 October (homothetic v3, "Independent Rankings of Binary Advice") because it states directly why the 8 October construction fails independence.

**Naming warning.** The labels collide across documents.
- In loss-relations-credal-families, **(G)** is a *gluing* condition on family orders. From v3 (9 Oct) on, (G) means world-by-world *guidance*.
- In kkm v6 and v7, **(C)** is lower semicontinuity of the conditional block losses. In the KCM and loss-relations notes, (C) means that C_L is closed under equal profiles.
- **(IB)**, independence, appears **nowhere in this slice**. Its first statement is 9 October.
- Guidance appears here as truth-directedness (TD), that is, weak monotonicity in error-set inclusion, or as (B1)/(B2) (strict respect for the background order).

---

## 1. Chronological list of attempts

**A0. Calibration conditions (calibration-and-complete-classes, abstract-calibration; around 25 Sep).**
- *Aim:* get coherent dominance from Bayes structure.
- *Assumptions:* local coherent continuation, convex coherent ties, differentiable Bayes risk, optimizability, compactness.
- *Outcome:* PROVED under those hypotheses, then **abandoned**.
- *Mechanism:* kkm v1, Example "rescaled quadratic", shows that none of these conditions is invariant under world-wise increasing rescaling. The target conclusion is invariant. With f(t)=t^{1/4}, convex ties and smoothness fail. With a jump rescaling, optimizability fails. Lesson: premises must be ordinal.

**A1. Realization theorem and the finite-error no-go (realization-and-coherence.md, 25 Sep).**
- *Aim:* get undominated equals coherent from realization conditions.
- *Theorem (PROVED):* assume Bayes optima are attained, B (the union of Bayes profiles) is pointwise compact, and Bayes faces satisfy the Bayes-convexity condition (BC). Then R↑=B↑, this set is closed and convex, and U_R ⊆ B.
- *No-go (PROVED):* three-state finite-error losses with Lebesgue-equivalent densities built on three boxes A_1, A_2, A_3. These satisfy every realization hypothesis, compactness of the coherent profile class, and strict error-inclusion monotonicity, yet D*=A_1∪A_2 has undominated profile (1,1,4) while every coherent profile has third coordinate ≤3. An everywhere-positive version keeps a gap of 0.75.
- *Mechanism:* the sum of any gamble in A_i and any gamble in A_j is strictly negative, so no coherent cone meets two boxes. Additive Bayes structure says nothing about coherence; coherence of the Bayes sets must be imposed separately.
- *Positive bit:* with densities a_i|g_i|r(g), the Bayes set at p is D_q with q ∝ (a_i p_i). Coherence identification need not be "proper" at the indexing prior.

**A2. The KKM calibration theorem (kkm-calibration v1, 25 Sep, through v7, 30 Sep).**
- *Aim:* an ordinal dominance theorem for arbitrary model sets.
- *Assumptions:*
  - (A): no coherent model is dominated.
  - (S): a choice p↦c_p of coherent models, not strictly dominated on supp p, with p↦L(c_p,ω) lower semicontinuous.
  - For infinitely many worlds, (T) a compact family plus (S∞) continuous σ_F on finite simplices.
  - Or (B): lsc bounds Q_F(p) met by some family member and not strictly dominated on supp p.
- *Outcome:* PROVED. (A)+(S) gives every model a weak dominator c_{p*} that is undominated, so U_R=K. If C is closed under equal profiles, U=C. The proof is one KKM application.
- *Extras (all PROVED):*
  - the margins theorem for Bayes choices (uniform dominance iff expected-loss excess ≥ ε at every finitely supported prior);
  - Nielsen's Theorems 1 and 2 recovered, with local boundedness removed for ordinary dominance;
  - Predd et al. and Pettigrew recovered as special cases;
  - conditional systems with null-event freedom, via a continuous section lemma;
  - vertex tie-breaking models M_{i,r};
  - a countable Brier example with K not closed;
  - a counterexample to Joyce's 2009 partition theorem. A softmax loss with penalty is truth-directed and continuous and satisfies (A) with no ties, yet x*=(1,1,0) is weakly dominated by no coherent credence.
- *Mechanism:* the competitor m defines closed sets A_ω={p: L(c_p,ω)≤L(m,ω)}. (S) is exactly the KKM covering condition. Only the boundary of Δ constrains the choice, because by (A) interior points are automatic. At the vertices, (S) demands coherent *ideal* models (I).

**A3. What (S) amounts to (kkm v2–v5, Sec. "Finitely many worlds").**
For compact K, (S) holds iff there is a continuous P:Δ→K with P(p) ∈ K^{supp p}, where K^S is the set of coherent profiles not strictly dominated on S.
- Two worlds: (S) holds iff K is connected and has ideal points (PROVED).
- Three worlds: (S) holds iff the edge paths exist and the loop they form fills (PROVED).
- Convex three-world problems and polyhedral problems: (S) can be met, via Peleg retraction and Hoffman's lemma (PROVED).
- **Three-world counterexample** (FAILS): K is connected, (A) and (I) hold, but K^{12} splits into two pieces at t≤0.48 and t≥0.52.
- **Four-world counterexample** (FAILS): a convex problem with K compact, yet K^{12} contains a sin(1/t)-type zigzag, so no path exists.
- Lower semicontinuity cannot be dropped: three coherent models (0,1,1), (1,0,1), (1,1,0) against a fourth model (½,½,½).
- *Mechanism:* (S) is a path-connectedness and topology condition on the sets K^S over the faces of the simplex.

**A4. Benchmarks and bounds (kkm-benchmark-draft 28 Sep, folded into v6 as (B)).**
- *Aim:* a condition that is also necessary.
- *Outcome:* PROVED. For finitely many worlds and compact K, (T)+(B) holds iff every model is weakly dominated by a coherent one, using ray bounds Q^ray.
- *Mechanism and caveat:* v7, Remark "elementary", admits that (B) with ray bounds is close to a restatement of the conclusion. The real content is that *any* lsc bounds work. Bayes bounds (Lemma bayesbounds) do not always exist: they fail on the three-world edge, by a connectedness argument.

**A5. The rational-permissibility argument (v6 and v7, Sec. 2.4; KCM "old", 30 Sep).**
- Axioms (E), (LA), (A), (S)/(T)/(B), plus the identification clause.
- In v6 the identification clause was "C_L-profile implies coherent". In v7 it became "equivalent to C_L", reflecting the shift to equivalence classes.
- *Outcome:* PROVED (Prop. "permissible"). This is bookkeeping once each loss meets the single-loss hypotheses.

**A6. CPM error losses (v7 Sec. "ignored region", v8, the v7 audit, CPM v18/v19a).**
- *Aim:* make every coherent set of desirable gambles (SDG) admissible for some error loss of a coherence-preserving map (CPM).
- *Assumptions:* CPM (continuous, homogeneous, exactly sign-preserving, every q-contraction convex) on an open cone V ⊇ ℝⁿ≥0∖{0}.
  - v7: the loss ignores Z=N_mix∖V.
  - v8 and v18/19: the loss **evaluates only rules D⊆V up to null sets**.
- *Outcomes (PROVED):*
  - **Bayes bridge:** q·L(D)−q·L(C_q) = ∫_{D△C_q} W|q·Φ|.
  - **Dominance (thm:dominance):** admissible = Bayes = contractions, up to null sets. (LA), (S) and (C) hold.
  - **Realisation (thm:realise):** every parallel body K=L+rB_H ⋐ int Δ is realised non-tangentially by an explicit LP map at any q ∈ relint K.
- *Failures (PROVED):*
  - lower-dimensional interior targets have no LP realiser;
  - exact realisability is not closed under limits;
  - **cor:boundary-support:** a credal set containing two boundary points with different supports is never a contraction of *any* CPM at *any* prior. So the vacuous set is admissible for no CPM error loss and is uniformly dominated whenever it is evaluated.
- The ε-contamination no-go for n=3 is announced but UNPROVED (Rem. "contamination").
- *Why the domain was restricted (Rem. "extension"):* with zero density off V, C∪B ties C for a ball B ⊂ N_mix∖V, which breaks (C). Restricting to M_L removes those ties. This is a **domain restriction to subsets of V**, the kind now banned.
- Two-state picture (cor:two-states, PROVED): concave CPMs cover every coherent set except the vacuous one.

**A7. Write-in, omission-blind losses (truth_directed_losses, 4 Oct). I read this note only.**
- *Aim:* restore coverage with truth-directed (TD) losses on all rules.
- *Vertex obstruction (PROVED, thm:obstruction):* suppose L is TD, its exchange rates vanish at (i,j) and (j,i), and the domain is closed under adding the thin cones A_ij(δ) near e_i. Then any coherent D whose credal set has boundary points with *incomparable* supports is dominated by D∪A_ij∪A_ji. This includes the vacuous set.
- Vanishing exchange rates hold for CPM error losses, bi-Lipschitz transforms, worst-case and best-case aggregates, and nonnegative combinations.
- *Restoration (PROVED, thm:coverage):* the omission-blind loss uses the identity map on V := int D and charges only shortfalls off V. It covers every coherent set, and the family satisfies (E), (LA), (A), (S) and (C).
- *Why rejected (Rem. writein, Prop. price):*
  - The domain *is the target's interior*: the trivial tangential realisation of CPM Rem. 1.4. The target is written into the loss.
  - Prop. price (a): the vacuous set is vindicated at a full-support prior only by a loss under which its counted error is zero at every world.
  - Prop. price (b): boundary targets are vindicated only by losses whose domain omits a vertex on the target's boundary.
- Strict guidance also fails: wrong rejections off V cost nothing.

**A8. Non-additive losses (nonadditive_losses, 5 Oct).**
- *Aim:* reach ε-contamination with a natural TD loss.
- *Aggregation theorem (PROVED):* combine TD error losses world by world through G_i that are convex or concave, or differentiable or concave. Every rule that is not strictly dominated is then a Bayes rule at *one* prior of a single additive TD loss with map Ξ_i=Σ_k s_ik Φ^k_i.
  - With concave ingredients nothing new is vindicated.
  - On all of ℝⁿ, concave TD maps are two-slope, so **only normalised boxes** (cor:all-gambles).
- *Belief-function losses L_m = (1−ε)L^0 + Σ m_S L^S (PROVED):* additive, evaluated on all rules, satisfying (LA), (S) and (C). Their Bayes set at q is D_{K_q} with K_q=(1−ε)q+Σ m_S Δ_S. This gives ε-contamination and every belief function with positive singleton mass.
  - **But L_m rewards wrong rejections:** gambles with g_i>0 whose gain is less than ε/(1−ε) times their worst loss. So it is not TD.
- *Obstruction (PROVED, thm:obstruction):* for n≥3, no TD additive loss has the ε-contamination of q as its Bayes rule for all q in an open set. The field is forced to be proportional to Ψ, which has the wrong sign on an open set.
- *World-constant TD loss (PROVED):* such a loss ignores every contingent gamble.

**A9. Loss relations from credal families (loss-relations-sdg and loss-relations-credal-families, about 6–7 Oct).**
- *Aim:* replace losses by rankings built from a family p↦K_p.
- *Construction:* the extension ranking X ⪯^s_i Y iff P_i(Y) ⊆ ↑_i P_i(X), where P_i(X) = {p : E_i(X) ⊆ E_i(D_p)} is the set of family members that *cover* X at world i.
- *Conditions:* (G) gluing, (FC), (ND), (Cl); in particular the level orders under (U): p_i>q_i implies Ū_p(i)>Ū_q(i).
- *Outcomes (PROVED):*
  - (LA), (S) and (C) hold, and (B1) holds, but **(B2) fails** (Prop. noclosed).
  - The lexicographic refinement ⪯^L satisfies (B1) and (B2), but **no selection satisfies (S)** (Prop. noselection; σ is forced to be locally constant).
  - The numerical loss L_η(X,i) = inf over covers of [1−p_i−η·μ(errors avoided)] satisfies (B1), (B2), (LA), (S) and (C) under (U), (Lip) and (Dom).
  - Coverage: every credal set M ⊂ int Δ.
- *Failure (PROVED, Rem. "class"):* (U)+(F) exclude every vertex-containing credal set other than {e_i}.
- *Mechanism:* a budget argument. Gluing of covers at two worlds gives p^j_k ≥ p^k_k, so the cover levels sum to at most 1, and competitiveness follows without any Bayes structure.

**A10. Homothetic families (full-coverage-homothetic-v2, 8 Oct).**
- *Aim:* full coverage, including the vacuous set.
- *Construction:* K_p = p + θ(p)(M − r), with anchor r = (1−λ)ℓ + λu, λ = (1−L)/(U−L), and θ the largest factor ≤1 that keeps the copy inside Δ. Replace (U) by **(CC)** (compatibility of covers), which comes from the endpoint identity (1−λ)lo + λhi = p_i.
- *Outcome:* PROVED. Ordinal and numerical (L_η) rankings on all measurable models give (E), (LA), (A), (S), (C) and strict background respect.
- Also PROVED (Prop. ustar): an upper-probability-only condition (U*) cannot contain a vertex-containing set with support of size ≥3. The proof uses invariance of domain.
- *Independence:* **FAILS.** This is not examined in v2. The 9 October v3, §2, proves that the ordinal benchmark recipe of v2 violates (IB). Adding the same contradictory or strictly negative acceptances to two models leaves *no cover anywhere*, so both fall back to the default comparison and an earlier strict comparison is erased.
- Also, L_η(D_{K_p},i)=1−p_i is an **imposed exact profile**, and the family is built through the target M. Both are now on the "cheap tricks" list.

---

## 2. Recurring obstructions

1. **Realisation, or coverage, is the bottleneck.** For any additive (integral) loss, the Bayes set at q is {q·φ>0} (Lemma additive(b), CPM Bayes bridge). So the vindicated models are exactly the sign sets of q-combinations of the per-world fields. Coverage of a target class becomes a realisation problem. Appears in: realization-and-coherence §3; CPM v19a thm:dominance and cor:covering; nonadditive cor:all-gambles; TDL §1.

2. **The vertex or boundary-support obstruction, the "tangency at the vacuous model".** Three forms:
   - (a) CPM: every m ∈ Q_p has supp m ⊇ supp p. So two boundary points with different supports never occur, and the vacuous set is never a contraction (v19a cor:boundary-support).
   - (b) A TD loss that is continuous at the vertices (vanishing exchange rates), on a domain closed under thin near-vertex cones, dominates every target with incomparable-support boundary points (TDL thm:obstruction).
   - (c) The nested-support case is excluded for additive losses (CPM Prop. 11.6) and is **open** for non-additive losses (TDL Rem. nested).

   *Mechanism:* near e_i, a gamble that gains almost its whole size at ω_i and loses δ at ω_j can be accepted. A vanishing exchange rate makes that trade profitable at both worlds.

3. **Domain restriction is needed for identification.** Zero density off V lets incoherent sets tie coherent ones, which breaks (C). Every fix in this period restricted the evaluation domain: D⊆V in v8 and in CPM M_L, and V=int D in the write-in losses. See v7-audit, top note; v19a Rem. extension; TDL Rem. designs.

4. **Two-slope rigidity on the full domain.** A concave, homogeneous, TD map on ℝⁿ has coordinates α_i g_i⁺ − β_i g_i⁻. So with all rules evaluated, the reach is the normalised boxes (CPM Prop. 2.4; nonadditive Prop. average(iii), cor:all-gambles). This is exactly the "audit's positive baseline". It was already a theorem by 5 October.

5. **Topological obstructions to (S).**
   - Gaps in K^S (three-world example), a non-path-connected K^S (four-world zigzag), and connectedness blocking Bayes choices (rescaled quadratic, v7 Rem. bayeschoice; Bayes bounds on the three-world edge).
   - The closedness clause of (S) is incompatible with strict refinements of cover rankings (credal-families Prop. noclosed and Prop. noselection).
   - An infinite penalty makes p↦L(u_p,ω_j) jump to +∞ on a face, so no selection satisfies (S) in n=2 (TDL Rem. unsettled).

6. **Truth-directedness against contamination.**
   - Contamination and other belief functions need rewarded wrong rejections (nonadditive thm:obstruction, n≥3).
   - Monotone non-additive aggregation collapses to one additive loss at one prior (thm:aggregation).
   - The smallest repair that restores TD destroys closure under addition (Rem. repair).

7. **Guidance plus (A) does not give dominance.** Joyce counterexample (v7); finite-error box no-go (realization note); v1 Prop. "(S) cannot be weakened to coherent admissibility". Some selection or calibration premise is logically needed.

8. **Whole-model covers against independence.** Any ranking that compares models through "which family member covers the whole model at ω_i" is non-local. Shared contradictory advice can remove all covers (homothetic v3 §2, on v2). This is the Round 82 failure, already diagnosed on 9 October.

---

## 3. Positive mechanisms and their exact scope

- **KKM selection theorem.** (A)+(S) ⇒ an undominated coherent weak dominator. Arbitrary model sets, no topology on models; for infinitely many worlds add (T)+(S∞), or (B).
  *Scope:* fully general and sound. All the difficulty is pushed into building (S).
- **Additive loss with null indifference sets and coherent Bayes sets ⇒ (LA), (S) with continuous Bayes choices, and (C), plus uniform dominance of non-Bayes rules** (nonadditive Lemma additive(d); CPM thm:dominance).
  *Scope:* any integral loss on any domain. **This mechanism is independent by construction.** The only remaining question is whether the Bayes sets are coherent at every prior, including boundary priors, and which sets they reach.
- **Certifying prior ≠ index prior.** Conditional block section lemma; vertex tie-breaking via M_{i,r}; the a_i-rescaling in realization §4.
  *Scope:* handles null events and ties at boundary priors without discontinuity.
- **LP realisation.** Every parallel body is realised exactly, non-tangentially, with a closed-form denominator. Every credal set is a limit of realised ones.
  *Scope:* only on proper domains V. So it depends on the domain restriction.
- **Belief-function additive losses.** Full domain, additive (so independent), Bayes sets coherent at every q.
  *Scope:* covers belief functions with positive singleton mass, including ε-contamination. Not TD.
- **Budget plus gluing, or (CC).** Covers of one model at different worlds glue, so the cover levels sum to at most 1. This gives competitiveness and strict dominance without Bayes structure.
  *Scope:* the homothetic family covers every credal set, including the vacuous one. It is intrinsically non-local and fails (IB).
- **Floor loss (TDL Rem. floor).**
  - *Field:* Φ^κ_j(g) = g_j − κ‖g‖ if g_j<0, and g_j otherwise.
  - *Properties:* positive density wherever g_j≠0, so strict guidance; additive, so independent; full domain.
  - *Result:* vindicates the vacuous set at interior priors when κ ≥ max(p_1/p_2, p_2/p_1).
  - *Scope:* n=2 only. In 3 states its Bayes sets are numerically non-convex.

---

## 4. Assumptions dropped or changed, and why

- **Calibration conditions** (continuation, convex ties, smooth risk, optimizability) were dropped in v1 because they are not ordinal.
- **(T)+(S) became (S) alone for finitely many worlds** (v7), because no topology on models was needed. (B) was added because (S) is not necessary.
- **Real losses became [0,∞]** (v7), to cover Nielsen's setting.
- **"Each C_q coherent" became "coherent up to null sets"** (v7 audit). At point-mass priors, C_{δ_i} omits e_j.
- **Identification clause:** "has an L-profile in C_L ⇒ coherent" became "⇒ equivalent to a member of C_L" (v6 to v7). Null-set ties are unavoidable.
- **The ignored region Z became the evaluation domain D⊆V** (v8, at the user's request; CPM v18). This was needed for (C). It is now banned.
- **CPM domain ℝⁿ≥0∖{0} ⊆ V was relaxed to ℝⁿ>0 ⊆ V** (TDL), to escape the vertex obstruction. It works only by omitting vertices on the target boundary: tangential, write-in.
- **(U) became (CC)** (homothetic v2). (U)+(F) cannot hold of vertex-containing targets, and (CC) uses actual common covers.
- **Truth-directedness was the candidate guidance axiom**, and it was shown incompatible with additive contamination. On 9 October, v3 replaced it with (G) guidance over an advice order (good, silence, bad, contradictory) together with (IB).
- **"A single loss vindicates all coherent models" became "a family jointly does"** (Premise 2 / (A)). This was necessary because one CPM loss vindicates only its contractions.

---

## 5. Top five lessons

1. **Under independence, a full domain and strict guidance, the problem *is* a field-realisation problem, and its crux is the boundary of the simplex.** *(Confidence: high.)* Independence pushes toward local, additive penalties. Additive losses give Bayes sets {q·φ>0}, and (LA), (S) and (C) then come for free (Lemma additive(d)). So what remains is a classification: which global sign-preserving fields have coherent q-sign-sets at every q, and which credal sets they reach. Concave homogeneous fields reach only the normalised boxes. Any field that is continuous at the vertices hits the vertex obstruction, so the vacuous set and every incomparable-support boundary target are lost. Effort should go into fields whose wrong-acceptance cost does **not** vanish near the almost-sure gains: non-concave, floor-type fields.

2. **Every full-coverage success in this period encoded the target.** *(Confidence: high.)* The write-in loss uses V=int D. The homothetic and L_η losses use a family through M and impose the profile 1−p_i. The CPM losses restrict the domain to V. Each of these devices is now banned. Coverage results should be judged first by whether the loss class is defined independently of the target.

3. **Cover-based, whole-model rankings cannot satisfy (IB).** *(Confidence: high.)* This was diagnosed on 9 October (v3 §2). Round 82 re-ran the same mechanism with a different family. The budget and gluing argument is a good competitiveness tool, but it needs whole-model covers. If it is to be kept, it needs a local analogue, such as covers of each binary problem separately. I do not know whether such an analogue exists.

4. **(S) is a topological condition, but for additive losses with null indifference sets it is automatic.** *(Confidence: medium-high.)* The long kkm v2–v5 analysis (paths in K^S, loop filling, the zigzag) matters only for non-additive rankings. Under an additive design the remaining risk in (S) is at the boundary priors: indifference sets that are not null at the vertices, as in the n=2 contamination field of nonadditive Rem. n2, and infinite penalties. Lexicographic vertex tie-breaking (M_{i,r}) is the tested repair.

5. **Monotone non-additivity buys nothing, and every reach beyond boxes so far gives up some guidance.** *(Confidence: medium.)* Aggregating TD error losses collapses, at each surviving rule, to one additive TD loss at one prior. Contamination needs rewarded wrong rejections (n≥3). The omission-blind and Jamesian losses give up strict guidance by assigning zero cost to some wrong rejections. A next step should therefore say exactly which strict-guidance instances must be given up for which targets, and should test whether the "floor on wrong-acceptance cost" route keeps all of them.

---

## 6. Leads dropped too early or never tested

- **Floor-type global fields in n≥3** (TDL Rem. floor). These are strictly guided, additive and full-domain, and they escape the vanishing-exchange-rate hypothesis. Only one formula was tried, and it was rejected on numerical non-convexity alone. Nobody searched for other non-concave, homogeneous, sign-preserving global fields with convex q-sign-sets. CPM v19a notes that the two-slope rigidity is a result about *concave* global maps only. **Caveat:** v3 (9 Oct) announces that no additive per-binary-problem construction of its kind gives full coverage for n≥3, because the vacuous set is forced to be strictly dominated. A reader of the later slice should check whether that proof covers floor-type fields or only its four-penalty scheme.
- **The Jamesian mixed omission-blind loss** (TDL Ex. jamesian). It is target-independent, additive and on all rules, and its admissible sets have credal sets with incomparable-support boundary points. (S) at boundary priors and coverage of the family were never checked. It fails strict guidance at the shun-error worlds.
- **Belief-function losses as one component of a family.** They are additive, independent and full-domain, and they cover all belief functions with positive singleton mass. The only defect is TD. Whether a strict-guidance variant exists, perhaps by mixing in a floor, was not tested.
- **Bounds (B) in place of (S)** were never used in the gamble application. They allow the coherent witness to jump.
- **Largest-error (ess-sup) losses:** their admissible sets were not determined (TDL Rem. unsettled).
- **Nested supports for non-additive TD losses:** open (TDL Rem. nested).
- **The realization-note calibration subclass** (densities a_i|g_i|r(g)). This shows that the vindicated prior can differ from the index prior by a fixed rescaling q ∝ (a_i p_i). The analogous freedom in the CPM and gamble setting was not exploited systematically.
