# Consolidated Statements: Decomposable Domains, 12 October 2026

This document restates every numbered result in the round-9 notes R1, R2, R3, R4, R5 and R7 (folder `r9/`) in corrected form. Every repair from the referee reports R6 (on R1–R3), R8 (on R4–R5) and R9 (on R7) is built in, as is every correction in AUDIT_ASSESSMENT.md. It is meant to be usable without the referee reports. It contains no new results. Where a referee supplied a corrected statement or a short missing argument, that is said explicitly and attributed.

Order of precedence where sources disagree: (1) the audit, (2) the referee reports, (3) the author notes. Summary sentences in the notes and in the round report are superseded by §0.3 and the final section.

---

## 0. How to read this document

### 0.1 Status labels

| Label | Meaning |
|---|---|
| REFEREED-CORRECT | A referee checked statement and proof and found them correct. The referee's remarks were cosmetic or clarifying, and any clarification is recorded. |
| REFEREED-REPAIRED | A referee found a defect in the statement or the proof and supplied a repair. The statement given here is the repaired one. |
| GAP | The proof has an unfilled step, so the statement as originally given is not established. A weaker established version is given where one exists. |
| FALSE-AS-STATED | The original wording is false. A corrected version is given where one exists, with its own status. |
| CONDITIONAL | Proved from named premises that have not themselves been verified (for example the CPM-folder no-go chain), or from extra hypotheses that are not known to hold. |
| CONJECTURE | Not proved. |
| NOT-REFEREED | The author labelled it PROVED or CHECKED, but no referee examined it. Use with care. The author's own label is given in brackets. |

All "proofs" here are AI-written, and all referee passes were AI passes. No human check has been made. The audit is a direct assessment of the main arguments; it is not a line-by-line re-certification of the external CPM no-go chain (NOGO, PB, FA).

### 0.2 Setting and conventions (from BRIEF.md, used throughout)

- **Worlds and priors.** Ω = {1, …, n}, n ≥ 2. Δ is the probability simplex with vertices e_i (also written δ_i when viewed as priors). **int Δ** and **∂Δ** are taken relative to aff Δ. For a credal set K ⊆ Δ, **int_aff K** is the interior of K relative to aff Δ, and **ri K** is the relative interior of K in its own affine hull. When dim K = n − 1 the two coincide.
- **Problems.** A gamble g represents the binary choice {g, 0}, equivalently {a, b} for any gambles a, b with g = a − b. The gambles g and −g represent the same choice, the pair {g, −g}, which is indexed by its member in H = {g_1 > 0}. μ is a Gaussian measure. P(g) = {i : g_i > 0} and N(g) = {i : g_i < 0}. A problem is *mixed* if both are nonempty.
- **Models.** A model is a measurable acceptance set, taken modulo μ-null sets. On a pair it gives one of four kinds of advice: + (accept g), − (accept −g), 0 (silence), × (both).
- **Guidance order at world i.** good < silence < bad < contradictory. "Good" is the orientation that pays at ω_i.
- **Coherent models.** D_K = {g : P_K(g) > 0} ∪ {g ≥ 0, g ≠ 0}, where K is a credal set and P_K(g) = min_{m∈K} m·g. D_p = D_{{p}}.
- **Decomposable domain.** A measurable advice range A(g) ⊆ {+, 0, −, ×}, nonempty, is fixed on each pair: the kinds of advice that evaluable models give on the choice represented by g. M = M_L, the class of evaluable models, is the set of all measurable models whose advice lies a.e. in the advice ranges. M is closed under splicing and under convergence in measure. This restricts only which models are evaluated; no decision problem is removed or altered. (Earlier notes call these *menu domains* and A(g) the *menu*.)
- **Ranking system L.** A preorder ⪯_i on M at each world. (G): weak and strict guidance improvement inside M. (IB): independence across binary problems inside M.
- **Undominated and selected models.** U_L is the set of undominated members of M: no Y ∈ M has Y ⪯_i X at every i with Y ≺_j X at some j. C_L is the set of coherent members of U_L.
- **The axioms.**
  - (LA): C_L ≠ ∅.
  - (S): a selection p ↦ C_p ∈ C_L. Each C_p is competitive on supp p against M: for every X ∈ M some i ∈ supp p has C_p ⪯_i X. The section {p : C_p ⪯_i X} is closed for every i and every X ∈ M.
  - (C): closure of C_L under equal profiles, modulo null sets.
  - (E): every model is evaluated by some ranking in the class.
  - (LF) at a target D: there is an open N ⊇ ∂D ∖ {0} such that every measurable R with R △ D ⊆ N lies in M_L.
- **Additive losses.**
  - An additive loss is L_i(X) = ∫_H ℓ_i(g, a_X(g)) dμ, with an integrable envelope on the advice ranges.
  - It is *strictly guiding at i* if ℓ_i(g, ·) is strictly increasing in world-i rank on A(g) for a.e. g. It is *weakly guiding* if it is weakly increasing.
  - An *additive system* ranks world i by L_i.
  - A model X is *p-Bayes* if it minimises p·L over M.
  - A *lexicographic (lex) ranking* with additive levels compares level vectors lexicographically.
- **Charts (R1).** For a pair g and an orientation h ∈ {g, −g}, R(h) = {p ∈ Δ : accepting h is the unique minimiser of p·ℓ(g, ·) over A(g)}. For a prior p, B_p = {h : p ∈ R(h)}, with unanimous positive gambles included. For interior p, K_p is the credal set with B_p ≈ D_{K_p}. Here ≈ means agreement modulo null sets.
- **Nesting.**
  - For coherent A = D_{K_A} and B = D_{K_B} and a mixed sign pattern σ, put R_σ(A, B) = {h : sign h = σ, A accepts h, B silent on {h, −h}}.
  - **(Nest):** R_σ(A, B) is non-null for every mixed σ.
  - In n = 2 a coherent model is D_{[α,β]} in the coordinate r = −g_2/(g_1 − g_2). A pair is **strictly nested** if α_B < α_A ≤ β_A < β_B, which is equivalent to K_A ⊂ int_aff K_B. Then R1 = {α_B < r < α_A} (A: +, B: 0) and R2 = {β_A < r < β_B} (A: −, B: 0).
- **Test targets (n = 3).**
  - T1: K = (1 − ε)u + εΔ, with u the uniform prior.
  - T2: a generic triangle in int Δ.
  - T3: a segment in int Δ.
  - T4: conv{e_1, u}.
- **Cited files.**
  - GD folder: v3 = *Full Coverage by Homothetic Credal Families v3*; LDG = *Loss Dominance Generalized v2*; BA, CBOI, CCF = *Closed Choice Forces Fineness*; CANA; Audit = *Audit of Imported Assumptions 2026-10-12*.
  - CPM folder: v19 = *LSP_CPMs_v19b*; NAL = *nonadditive_losses*; DCE = *Domain Closure and Extendability*; NOGO = *CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md*.
  - Device-only CPM notes: PB = *TRIANGLE_A0_A1_PROJECTIVE_BOUNDARY.md*; FA = *TRIANGLE_A0_A1_NOGO_FIXED_ANCHORS.md*.

### 0.3 Global corrections (apply everywhere below)

1. **Bayes uniqueness is not selection uniqueness.**
   - For a fixed additive system satisfying the axioms, each interior weighted objective p·L has an a.e.-unique Bayes minimiser on M.
   - The axioms do not require an (S) selection to assign that minimiser to index p. Selections can be reindexed (Example AUD-1).
   - Wherever a note calls p ↦ B_p "the selection", read it as "the interior Bayes map".
2. **Nesting uses interior relative to aff Δ.**
   - Every sufficient condition for (Nest) written as "K_A ⊂ int K_B" means K_A ⊂ int_aff K_B.
   - With the topology of Δ instead, the claim is false. Counterexample (R6): n = 2, K_A = [0, ½], K_B = [0, ¾].
3. **Family rigidity is stronger than coverage.**
   - Reproducing an entire undominated family is stronger than vindicating one target.
   - Covering a target needs only *some* system that vindicates it. That system need not vindicate anything else in particular.
   - So no-nesting results do not by themselves exclude any imprecise target.
4. **Representing rankings is not reproducing families.** A system can have an additive undominated family while its rankings have no additive extension (R2 Prop 4).
5. **Excluding a prescribed family is not excluding a target.** R1 Thm 4.1 excludes the prescribed Bayes family K_q = (1 − ε)σ(q) + εΔ (and its belief-function generalisation) on an open set of priors. It does not exclude an additive family that passes through one contamination target but has a different shape, or a different (nonlinear) parametrisation, at nearby priors.
6. **Strict-guidance results do not automatically apply to Σ_T systems or to the D_Δ exception.** The no-nesting proofs use strictly signed local differences.
7. **Withdrawn slogans (not established):**
   - R1's "domain shape gives no gain" and "the analysis can always be run on U′";
   - "measurability and advice ranges add only a little" (originally phrased with "menus");
   - R2's "avoidable exactly when" (only necessity is proved);
   - R7's "staircase only at vertices / edge endpoints" (false in general; see the R9 version);
   - the round report's "only diagonal-projective caps remain" (the reduction is conditional and not exhaustive);
   - "T1 reduces to one exotic remaining construction".
8. **Extra regularity and advice-range hypotheses are extra.**
   - (H0), (H1) and (H1⁺) do not follow from measurability, the advice ranges or (LF).
   - Continuity relative to a co-null set does not supply a continuous representative off a closed null set. R1 Ex 3.3 is densely discontinuous.
   - (LF) does not imply (H0).
9. **n = 3 is not silently extended to n > 3.** The contamination no-go results are stated for n = 3, except R1 Thm 4.1, which holds for n ≥ 3.

---
## 1. R1: additive rankings on decomposable domains (R1_notes.md)

**Standing hypotheses for R1 §§1–3.**
- L is an additive ranking on a decomposable domain. The advice ranges A(g) ≠ ∅ are measurable, and M is the set of all measurable models whose advice lies in them.
- The penalties ℓ_i(g, a) are measurable, and L_i(X) = ∫_H ℓ_i(g, a_X(g)) dμ is finite on M. Equivalently, max_{a∈A(g)} |ℓ_i(g, a)| is integrable.
- The guidance order is the strict four-rank order.
- "(N)" abbreviates: (G) holds, and (LA), (S), (C) hold. By Theorem 2.2(N) these imply (N1)–(N4).

### R1 Correction C1 (§0)
- **Status:** NOT-REFEREED as a separate item. R6's check of Thm 2.2(T) relies on it and agrees.
- **Statement:** Under (N) it is *not* forced that every p-Bayes model is coherent at boundary priors. What is forced:
  - at interior p, every Bayes model is coherent and the Bayes advice is a.e. unique (Lemma 1.4);
  - at every p ∈ Δ, a coherent Bayes model exists (Lemma 1.3(a));
  - at vertices, the Bayes advice is unique (Lemma 1.5).

  A boundary p-Bayes model can be incoherent if another p-Bayes model beats it at a world outside supp p.
- **Used for:** separating the necessary conditions (N) from the sufficient conditions (S) in Thm 2.2.

### R1 Correction C2 (§0)
- **Status:** NOT-REFEREED as a separate item. R6 accepts it and uses it (domain flag on R2 Lemma 3).
- **Statement:**
  - v3 lem:bayes-necessary(c) (a Bayes model's credal set lies in Δ_{supp p}) does not transfer verbatim to decomposable domains. The correct version for decomposable domains: a p-Bayes model accepts a.e. h with h_S > 0 whose acceptance is in the advice range, where S = supp p.
  - NAL lem:additive has two kinds of advice per gamble, so it covers advice ranges {+, 0} only.
- **Used for:** Prop 2.6. Also explains why v3's three-vertex obstruction is an all-model result.

### R1 Lemma 1.1 ((G) on decomposable domains)
- **Status:** NOT-REFEREED [author: PROVED].
- **Statement:** Under the strict four-rank order, (G) (weak and strict) holds on M iff, for each i and a.e. g, a ↦ ℓ_i(g, a) is strictly increasing in world-i guidance rank on A(g). Consequently ℓ_i(g, ·) is injective on A(g).
- **Used for:** turning (G) into sign conditions on chart data (Prop 2.1). Used throughout R1–R5.

### R1 Lemma 1.2 (pointwise Bayes)
- **Status:** NOT-REFEREED [author: PROVED].
- **Statement:** X ∈ M is p-Bayes iff a_X(g) ∈ argmin_{a∈A(g)} p·ℓ(g, a) for a.e. g. A measurable pointwise minimiser exists (fixed tie-break order), and it lies in M.
- **Used for:** reducing Bayes questions to per-problem minimisation.

### R1 Lemma 1.3 (v3 lem:bayes-necessary on decomposable domains)
- **Status:** NOT-REFEREED [author: PROVED].
- **Statement:**
  - (a) Under (LA) and (S), a coherent p-Bayes model exists for every p ∈ Δ.
  - (b) If X ∈ M and no Y ∈ M has L_i(Y) < L_i(X) for every i, then X is p-Bayes for some p ∈ Δ. The proof uses convexity of the attainable loss set, via splicing or Lyapunov.
  - (c) For interior p, every p-Bayes model is undominated within M.
- **Used for:** Lemma 1.4, Thm 2.2, Prop 2.6. R2 §1 ("pointwise Bayes on decomposable domains") restates (b) with an Aumann/Lyapunov proof.

### R1 Lemma 1.4 (interior priors)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Assume (N). For every p ∈ int Δ:
  - (i) every p-Bayes model in M is a.e. coherent;
  - (ii) the pointwise minimiser of p·ℓ(g, ·) over A(g) is unique for a.e. g. Hence the p-Bayes model is unique modulo null sets.
- **Clarification (§0.3.1):** this is uniqueness of the Bayes minimiser for each interior weighting. It is not uniqueness of the (S) selection, which may be reindexed (Example AUD-1).
- **Used for:** the basic rigidity of additive closed choice. It is identical in substance to R2 Lemma U.

### R1 Lemma 1.5 (vertices)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** At e_i the minimiser of ℓ_i(g, ·) over A(g) is a.e. unique. It is the best advice in the advice range at world i. Under (LA) and (S) it is coherent. (The DCE prop:ideal citation is accurate but not needed.)
- **Used for:** (N3); reach-set and vertex arguments.

### R1 Proposition 2.1 (table of charts for each advice range), vertex property, and converse
- **Status:** NOT-REFEREED [author: PROVED]. The sign facts were confirmed in passing by R6 (in the check of Prop 2.7) and by R8 (R4 §1 notation).
- **Statement.**
  - **× and singleton advice ranges.** × can be deleted from any advice range containing another kind of advice, because it is never a minimiser. A non-null set with A(g) = {×} violates (LA).
  - **Chart data.** For A(g) ⊆ {+, 0, −} put c = ℓ(0) − ℓ(+), c′ = ℓ(0) − ℓ(−) and d = c − c′ (vectors over worlds). Wherever the kinds of advice concerned are in the advice range, (G) gives:
    - c and d have the strict sign pattern of g;
    - c′ has the strict sign pattern of −g;
    - |d_i| > |c_i| for i ∈ N(g), and |d_i| > |c′_i| for i ∈ P(g).
    - For advice range {+, 0, −}, R8 records |d_i| > max(|c_i|, |c′_i|) for every i.
  - **Charts.**

    | Advice range | R(g) | R(−g) |
    |---|---|---|
    | {+} (every evaluable model accepts g) | Δ | ∅ |
    | {0} | ∅ | ∅ |
    | {+, 0} | {c·p > 0} | ∅ |
    | {+, −} | {d·p > 0} | {d·p < 0} |
    | {+, 0, −} | {c·p > 0, d·p > 0} | {c′·p > 0, d·p < 0} |

    The advice ranges {−} and {0, −} are the mirror images. For {+, 0, −} the silence region is {c·p ≤ 0, c′·p ≤ 0}, and the three lines are projectively concurrent.
  - **Vertex property.** If accepting h is in the advice range and not every evaluable model accepts h, then R(h) is relatively open and convex, contains δ_i for every i ∈ P(h), and contains no δ_j with j ∈ N(h).
  - **Converse.** Any measurable data c (for {+, 0}), d (for {+, −}) or (c, c′) (for {+, 0, −}) with these signs arise from (G)-penalties:
    - for i ∈ P: ℓ_i(+) = 0, ℓ_i(0) = c_i, ℓ_i(−) = c_i − c′_i;
    - for i ∈ N: ℓ_i(−) = 0, ℓ_i(0) = c′_i, ℓ_i(+) = c′_i − c_i;
    - × gets a strictly larger value;
    - the penalties are rescaled by a positive weight at each g to make them integrable. Charts are invariant under this rescaling.
- **Used for:** the whole chart calculus in R1, R4 and R5 (Theorem R_n).

### R1 Theorem 2.2 (chart characterisation)
Hypothesis: L is an additive ranking on a decomposable domain satisfying (G).

**(N) Necessity.**
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** If (LA), (S), (C) hold, then:
  - (N1) for every interior p, {g : p ∈ ∂R(g) ∪ ∂R(−g)} is null;
  - (N2) for every interior p, B_p agrees a.e. with a coherent D_{K_p};
  - (N3) at every vertex, B_{e_i} is a.e. "accept h iff accepting h is the best advice in the advice range at world i", and it is coherent;
  - (N4) at every boundary p, some coherent p-Bayes model exists.

**(S) Sufficiency.**
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Suppose that for every p ∈ Δ, boundary included, the minimiser is a.e. unique and B_p is a.e. coherent. Then (LA), (S), (C), (G), (IB) all hold on M (v3 thm:general, re-read on decomposable domains), with C_p = B_p. Every model in M outside {C_p} is strictly dominated at every world by some C_q.
- **Note (audit):** this sufficient condition (uniqueness at every prior) is strictly stronger than the necessary conditions (N). The difference is ties at non-vertex boundary priors (Remark 2.3). The chart description is therefore not an unconditional iff, and boundary choices remain part of the problem.

**(T) Targets.**
- **Status:** REFEREED-REPAIRED (R6). The original "D ∈ C_L iff D ≈ B_{p*} for some p* at which D is Bayes" is split, because both directions can fail at boundary p*.
- **Statement:** Assume (N).
  - (T-a) If D ∈ C_L, then D is p*-Bayes for some p* ∈ Δ.
  - (T-b) If p* ∈ int Δ and a coherent D is p*-Bayes, then D ≈ B_{p*} and D ∈ C_L.
  - Nothing is claimed for boundary p*. There D ≈ B_{p*} can fail under ties, and a p*-Bayes model can be weakly dominated at a world outside supp p*.
- **Used for:** under the hypotheses of Prop 2.6 the target prior is interior, so (T-b) is all that is used later.

### R1 Remark 2.3 (boundary ties)
- **Status:** NOT-REFEREED [author: CHECKED].
- **Statement:** Under (N1)–(N2), the axioms (LA), (S), (C) hold iff there are coherent undominated models C_p for p ∈ ∂Δ, each competitive on supp p, such that:
  - p ↦ L_i(C_p) is lower semicontinuous on Δ for each i, where on int Δ, C_p is the unique Bayes model; and
  - every X ∈ M whose loss profile equals that of some boundary C_p is coherent.

  Lower semicontinuity is equivalent to closedness of sections, because attainable values of L_i form an interval (splicing). A boundary C_p need not be p-Bayes.
- **Caution:** on int Δ the remark fixes C_p to be the Bayes map. Since (S) selections can be reindexed (§0.3.1), the "only if" direction has not been checked against a selection that differs from the Bayes map.
- **Used for:** locating the exact gap between Thm 2.2(N) and 2.2(S).

### R1 Proposition 2.4 (reach set)
- **Status:** REFEREED-CORRECT (R6, with a measurability remark).
- **Statement:** Assume (N). Let W = ⋃_{p∈int Δ} B_p, and let Av be the set of orientations whose acceptance is in the advice range.
  - (i) W ≈ Av ∖ {h ≤ 0}.
  - (ii) Write D_i = {h : h_i > 0}. Then W ∩ D_i ≈ B_{e_i} ∩ D_i = D_{V^i}, where V^i = conv(K_{e_i} ∪ {e_i}). So W is a.e. a finite union of open convex cones D_{V^i}, with D_{V^i} ∩ D_j ≈ D_{V^j} ∩ D_i. In particular W is a.e. a cone.
  - **Measurability (R6):** W = ⋃_{p rational} B_p together with the positive gambles, because every R(h) is relatively open.
- **Used for:** Prop 2.5; R4 Remark B3 repair.

### R1 Proposition 2.5 (a convex-cone subdomain of the reach set)
- **Status:** REFEREED-CORRECT (R6). The proof needs N shrunk to a neighbourhood of ∂D ∖ 0 that avoids −D and {h ≤ 0}. The clause "the charts of h ∈ U′ are unchanged" is deleted as vacuous.
- **Statement:** Assume (N). Let D = D_K ∈ C_L with K ⊆ int Δ, assume (LF) at D, and let p* be interior (Prop 2.6). Then there is a credal set K′ ⊆ ri K with U′ := D_{K′} ⊆ W a.e. For every interior p, B_p ∩ U′ ≈ D_{conv(K_p ∪ K′)}, which is coherent.
- **Used for:** fixing the cone U′ on which R1 Lemma 3.5, R1 Thm 4.2 and R4 work.

### R1 "Domain shape gives no gain" (sentence after Prop 2.5, and "Answer to task (2)")
- **Status:** GAP. Withdrawn: not established (R6, audit).
- **Original claim:** non-conic or non-convex sets of orientations whose acceptance is in the advice range give nothing beyond a convex-cone domain, and "the analysis can always be run on U′".
- **Why it fails:** restricting the evaluable models to those inside U′ removes "−" from the advice range of pairs with g ∈ U′. That turns wedge charts {c > 0, d > 0} into half-planes and changes the Bayes models, which could become incoherent.
- **What does hold:** Prop 2.5 only says the *original* system's reach set contains a convex cone around cl D ∖ 0. Later arguments (Lemma 3.5, Thm 4.2, R4) correctly keep the original advice ranges.

### R1 Proposition 2.6 (interior target prior)
- **Status:** REFEREED-CORRECT (R6). It is the Bayes form of the local face lemma (Audit §2, item 1), which should be cited.
- **Statement:** Assume (N). If D_K ∈ C_L with K ⊆ int Δ and (LF) holds at D_K, then every p* at which D_K is Bayes is interior.
- **Used for:** applying Thm 2.2(T-b); Prop 2.5.

### R1 Proposition 2.7 (acceptance propagation)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Assume (N) and that D is p*-Bayes with p* interior.
  - For a.e. h ∈ D, R(h) ⊇ conv({p*} ∪ {δ_i : i ∈ P(h)}).
  - For a.e. h ∉ cl D, R(h) ∩ conv({p*} ∪ {δ_j : j ∈ N(h)}) = ∅.
- **Remark:** a constant Bayes map K_q ≡ K satisfies these conditions, so 2.7 alone cannot exclude plateaus.
- **Used for:** constraints on any realisation of a target.

### R1 Proposition 2.8 (edge forcing)
- **Status:** NOT-REFEREED [author: PROVED].
- **Statement:** Under the standing hypotheses, suppose E ⊆ Av ∩ D_i ∩ D_j is non-null. Then there are a non-null E′ ⊆ E and an open neighbourhood O of the closed edge [δ_i, δ_j] with E′ ⊆ B_q for every interior q ∈ O.
- **Consequence for T1 under (LF):** near every edge, B_q ⊄ D, so K_q ⊉ K. Any plateau K_q ≡ K must stay away from the edges.
- **Used for:** excluding the constant Bayes map near ∂Δ.

### R1 Proposition 3.1 (continuity of the interior Bayes map)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Under (N1)–(N2), the following hold:
  - p ↦ B_p is continuous from int Δ to L¹(μ);
  - p ↦ K_p is Hausdorff-continuous on int Δ;
  - (p, h) ↦ P_{K_p}(h) is jointly continuous on int Δ × ℝⁿ.
- **Reading:** R1 calls this "the selection is continuous". Per §0.3.1 it is the interior *Bayes map* that is continuous.
- **Used for:** Thm 3.2; R4 throughout.

### R1 Theorem 3.2 (charts are continuous almost everywhere)
- **Status:** REFEREED-CORRECT (R6, with clarifications in (iv)).
- **Definitions:** R̃(h) = {p ∈ int Δ : P_{K_p}(h) > 0}, and Bad = {h : λ{p ∈ int Δ : P_{K_p}(h) = 0} > 0}.
- **Statement:** Under (N1)–(N2):
  - (i) Bad is null.
  - (ii) For a.e. h, R̃(h) ≈ R(h) ∩ int Δ.
  - (iii) For every h_0 ∉ Bad and every sequence h_k → h_0, λ(R̃(h_k) △ R̃(h_0)) → 0.
  - (iv) Suppose R̃(h) is a.e. an open half-plane H(h). Then R̃(h) ⊆ H(h), and H(h) ∖ R̃(h) is relatively closed and null. Let G be the co-null set of h for which this holds and h ∉ Bad. The unit normal ĉ = c/|c| is well defined, because an affine functional on aff Δ determines c and aff Δ spans ℝⁿ. On G, ĉ is continuous *relative to G*.
- **Note (audit):** this does not give a continuous representative off a closed null set. That is why (H1) in Thm 4.2 is an extra hypothesis.
- **Used for:** the regularised chart R̃; R4 §8 (K1).

### R1 Example 3.3 (genuinely discontinuous charts, n = 2)
- **Status:** REFEREED-REPAIRED (R6).
- **Statement:**
  - **Construction.** Let φ : [0, 1] → [0, 1] be continuous, nondecreasing and onto, constant on countably many disjoint intervals whose plateau values s_k are dense, and strictly increasing elsewhere. Take v3's interval family K^w_s with 0 < w < 1, and set K_t := K^w_{φ(t)}.
  - **Thresholds.** At g = (a, −b) with r = b/(a + b), the Bayes model accepts g iff t > α(r) := τ((r + w)/(1 + w)), where τ(s) = sup{t : φ(t) ≤ s}. It accepts −g iff t < β(r) := τ₋(r/(1 + w)), where τ₋(s) = inf{t : φ(t) ≥ s}.
    - The repair replaces R1's τ by τ₋ in β.
    - The two differ only at countably many r, so the Bayes models still agree a.e. with D_{K_t}.
  - **Realisation.** Any 0 < β < α < 1 is realised by (G)-penalties: + = (0, 1/(1 − α)), 0 = (1, 1), − = (1/β, 0), rescaled.
  - **Properties.** Ties at each prior are null. v3 thm:general applies on the all-model domain, so (LF) holds at every selected target. The charts jump on a countable dense set of rays, all of which lie in Bad. The family has plateaus.
- **Demoted:** the sentence "discontinuity of charts is equivalent to plateau-type persistence in n = 2" is an unproved remark, not part of the example.
- **Used for:** showing that coherence and (S) do not force continuous charts. This is why (H1) is a genuine extra hypothesis.

### R1 Example 3.4 (non-convex reach set, n = 2)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Take K_t = [2t/3, 2t/3 + 1/3]. Advice ranges at g = (a, −b):
  - {0, −} if a/b ≤ ½;
  - {+, 0} if a/b ≥ 2;
  - {+, 0, −} otherwise.

  These are realised with (G)-penalties. Then W = D_{[2/3,1]} ∪ D_{[0,1/3]} has angular range (−63.4°, 153.4°), which exceeds 180°. (1, −1.5) and (−1.5, 1) lie in W, but their midpoint is negative. (LF) holds at K_{1/2} = [1/3, 2/3].
- **Attached open question:** if every advice range contains the acceptance of at most one orientation, W is convex when n = 2. For n ≥ 3 this is OPEN.
- **Used for:** showing that the reach set can be non-convex.

### R1 Lemma 3.5 (no wedges near the target prior)
- **Status:** REFEREED-REPAIRED (R6).
- **Statement:** Assume the hypotheses of Prop 2.5 **and dim K = n − 1**. Let Q″ be a convex neighbourhood of p* on which K_q ∩ K′ ≠ ∅. It exists by Hausdorff continuity because K is full-dimensional; this holds for T1 and T2.
  - For a.e. g ∈ U′ with 0 ∈ A(g): R(g) ∩ Q″ = {c(g)·q > 0} ∩ Q″.
  - For a.e. g ∈ U′ whose advice range lacks 0 ({+, −} or {+}): R(g) ⊇ Q″.
- **Repairs:**
  - Passing from "for each q, a.e. g" to "for a.e. g, R(−g) ∩ Q″ = ∅" uses Fubini and the openness of R(−g).
  - R6's apex-free proof works in every n: if q ∈ Q″ has c·q > 0 ≥ d·q, then c′·q > 0, which puts q or a nearby point in the − sector.
  - Without dim K = n − 1 the lemma fails: for lower-dimensional K (T3), a parallel translate of K is Hausdorff-close to K but misses K′.
- **Used for:** half-plane charts near p* for T1 and T2.

### R1 finite-seam regularisation ("Answer to task (2)", second bullet; unnumbered)
- **Status:** NOT-REFEREED.
- **Statement:** Suppose the chart discontinuities of a realisation with advice ranges {+, 0} lie in a *closed* null cone (finitely many seams). Then NOGO §3's regularisation Ψ = dist(·, S̄)Φ/‖Φ‖ yields a continuous weak-sign map with the same, convex, closures. So finite-seam discontinuity gains nothing over continuous CPMs.
- **Used for:** motivating (H1).

### R1 Theorem 4.1 (NAL thm:obstruction on decomposable domains)
- **Status:** REFEREED-CORRECT (R6). NAL builds its "bad open set" for Ψ, not for Ψ^w; R6 records the routine adaptation. Choose q̃⁰ ∈ U and run NAL's construction at q⁰ = σ(q̃⁰). Then q·Ψ^w(g*) = (w·q)σ(q)·Ψ(g*) vanishes at q̃⁰ and is nonconstant on aff Δ. Take the ball B around q̃⁰ inside U.
- **Statement:** Let n ≥ 3, 0 < ε < 1, and let U ⊆ int Δ be open. There is no additive ranking on any decomposable domain satisfying (G) whose unique Bayes model at every q ∈ U is D_{K_q} with
  K_q = (1 − ε)σ(q) + Σ_S m_S Δ_S,  σ(q) = w⊙q/(w·q), w > 0,
  where the masses m_S are those of NAL thm:belief. The case m_Ω = ε is ε-contamination of σ(q). The theorem includes ε-contamination of q and of any diagonal reindexing of q. No (LF), (S) or (C) is used.
- **Scope (audit; §0.3.5):** this excludes the *prescribed* family on an open set. The sign argument uses the affine dependence on q in exactly this family. It does not exclude a single contamination target lying on an additive Bayes family of different shape at nearby priors, nor a nonlinear reparametrisation.
- **Used for:** the fixed-family obstruction for T1-type families.

### R1 §4.2(c) (plateaus)
- **Status:** NOT-REFEREED [author: PROVED].
- **Statement:**
  - A Bayes map constant (= K) on a neighbourhood W_0 of p* is not excluded by NAL thm:obstruction or by Prop 2.7.
  - For such a plateau, every chart line of h near ∂D avoids W_0, the one-sided limits of the chart normals differ at facet points, and ∂D ⊆ Bad.
  - Plateaus with ∂D ⊆ Bad exist in n = 3 *without* (LF): DCE §4's cheap system C_p = D_K ∩ D_p is constant on K. None is known with (LF).
- **Used for:** showing that plateaus must be handled separately (Thm 4.2 spot-check).

### R1 Theorem 4.2 (conditional impossibility for T1)
- **Status:** CONDITIONAL. It rests on NOGO §§1–3; PB Lemma 3.1, Thm 3.2, Thm 4.1 and the exterior-ratio law; and FA (the fixed-anchor note). None of these was re-verified line by line. It also rests on the extra hypotheses below. The hypothesis (H0)_{U′} is added per R4 Remark B3, confirmed by R8.
- **Statement:** Consider an additive realisation of T1: an additive ranking on a decomposable domain with (G), (LA), (S), (C), (LF) at D_K and D_K ∈ C_L, with p* and U′ = D_{K′} as in Props 2.5–2.6. Suppose:
  - (H0)_{U′}: for a.e. h ∈ U′, both accepting h and silence are in the advice range of its pair;
  - (H1): there is a closed null cone S such that the a.e.-defined unit chart normal ĉ agrees a.e. on U′ ∖ S with a continuous function (its zero-coordinate set can then be added to S);
  - (H2): for a.e. g ∈ U′, accepting −g is not in the advice range.

  Then no such realisation exists.
- **Strengthening:** R4 Cor B2 replaces (H2) by the weaker (H2″)_{U′}: a.e. pair meeting U′ is non-adjacent.
- **Plateau spot-check:** author CHECKED, not refereed. PB Thm 4.1's contradiction from d > 0 survives a Ψ that vanishes on the facets.
- **Notes:**
  - (H1) is not implied by measurability (Ex 3.3; audit).
  - (H2) fails on the all-model domain. **T1 is open even for additive rankings on the all-model domain.** v3 thm:additive-obstruction needs "three vertices in K", in R1's wording.
- **Used for:** the conditional no-go for T1; superseded in scope by R4 Cor B2 / C3.

### R1 Conjecture 4.3
- **Status:** CONJECTURE.
- **Statement:** (H1) can be removed by running PB's arguments on the regularised chart R̃.
- **Progress:** R4 §8 transfers some steps, (K1)–(K4). The rest is R4 Conjecture 4.3′.

### R1 §4.4 (T2)
- **Status:** open. This is not a result.
- **Content:** everything in §§2–3, §4.2(a) and (c), and Thm 4.2's reduction applies to T2 verbatim. Thm 4.1 does not apply. Under (H1)–(H2), plus (H0) per R4 Remark B3, the question reduces to the continuous single-map problem, for which only numerical evidence of a no-go exists.

---
## 2. R2: do the axioms force additive behaviour? (R2_notes.md)

Conventions: ranks at world i are good 0, silence 1, bad 2, contradiction 3. An "additive strictly guiding loss" is as in §0.2.

### R2 Fact 0 (BA lem:complete-class, imported)
- **Status:** REFEREED-CORRECT. R6 verified the citation, and LDG thm:kkm / BA lem:complete-class are valid on any M_L.
- **Statement:** Assume (LA) and (S) on M.
  - (a) Every X ∈ M has a selected C_p with C_p ⪯_i X for all i.
  - (b) Every X ∈ U_L is tied at every world with some selected C_p.
- **Used for:** the KKM step behind Lemma 1, Lemma 3, R3 (KKM) and R7 (L1).

### R2 Lemma 1
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Under (LA), (S), (C), U_L = C_L ⊆ coherent. Moreover U_L is exactly the set of models tied at every world with a selected model.
- **Used for:** the standard lever in R2–R7. An incoherent undominated model contradicts (LA) + (S) + (C).

### R2 Fact (exchanges)
- **Status:** NOT-REFEREED [author: CHECKED, elementary].
- **Statement:** By (IB), whether X ⪯_i Y depends only on (Z, a_X|_Z, a_Y|_Z), where Z = {a_X ≠ a_Y}. Weakly favourable exchanges on disjoint supports sum to a weakly favourable exchange, by passing through the intermediate splice, which lies in M. (G) makes guidance-improving exchanges strictly favourable.
- **Used for:** background for Lemma X (R5).

### R2 "Pointwise Bayes on decomposable domains" (§1, unnumbered)
- **Status:** NOT-REFEREED as a separate item. The Aumann/Lyapunov convexity step it uses was checked repeatedly (R8 on Thm UN Step 1; R9 §1).
- **Statement:**
  - For an additive loss and a prior p, a model is p-Bayes on M iff a.e. it picks a minimiser of Σ p_i ℓ_i(g, a) over A(g).
  - The attainable set {(L_i(X))_i : X ∈ M} is convex and compact.
  - Hence every X ∈ M not strictly dominated at every world is Bayes at some p ∈ Δ.
- **Used for:** R1 Lemma 1.3(b) and the Bayes reductions throughout.

### R2 Lemma 2 (per-model representation is trivial)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Let D ∈ M be coherent and p ∈ int Δ. There are bounded local penalties, strictly increasing in rank at each world, for which D's advice is the a.e.-unique minimiser of p·ℓ(g, ·) over A(g). So D is the unique p-Bayes model.
- **Used for:** showing that the substantive question is a *single* system realising a whole family.

### R2 Lemma 3 (extension implies weak additive realisation)
- **Status:** REFEREED-REPAIRED (R6). The hypotheses were implicit and are now stated; a domain flag was added.
- **Statement:** Assume (LA), (S) and, for (ii), (C). Suppose each world k has an additive strictly guiding ℓ_k with
  (W_k): B ∈ C_L, X ∈ M, B ⪯_k X ⇒ ℓ_k(B) ≤ ℓ_k(X).
  Then:
  - (i) every ℓ-Bayes model B, at any prior p, has a selected coherent C with ℓ(C) ≤ ℓ(B) coordinatewise. Hence C is p-Bayes, and ℓ(C) = ℓ(B) if p is interior;
  - (ii) every D ∈ U_L is ℓ-Bayes at some prior.
- **Domain flag:** R2's sentence "these are exactly the hypotheses of the v3 three-vertex obstruction" holds only on the all-model domain. v3 thm:additive-obstruction is an all-model theorem, and its proof uses lem:bayes-necessary(c), which fails on decomposable domains (R1 C2). On a decomposable domain, Lemma 3 yields weak additive realisation, not the obstruction.
- **Used for:** the "trap": extension properties reduce coverage to additive realisation.

### R2 Proposition 4 (one-sided extension fails, yet the family is additive)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Let ℓ² be any additive loss satisfying v3 thm:general on the all-model domain M. Put L¹_i(X) = μ{g unanimous : a_X(g) ≠ +}, with local penalties 0, 1, 1, 1. Rank each world lexicographically by (L¹_i, L²_i). Then:
  1. strict and weak (G), (IB) and (E) hold;
  2. U = {C_p}, the ℓ²-Bayes family, and (LA), (S), (C) hold with the same selection;
  3. at every world i there is no strictly guiding additive ℓ_i satisfying (W_i), and no finitely additive one of CBOI's positive form.
- **Used for:** showing that extension is sufficient but not necessary for additivity of the family. It is the audit's distinction 1 (§0.3.4).

### R2 Lemma U (uniqueness of interior Bayes models)
- **Status:** REFEREED-CORRECT (R6). Same content as R1 Lemma 1.4(ii), by a different route.
- **Statement:** Consider an additive strictly guiding system on a decomposable domain M with (LA), (S), (C). For every p ∈ int Δ, any two p-Bayes models in M agree a.e. Equivalently, the pointwise minimiser of p·ℓ(g, ·) over A(g) is a.e. unique.
- **Consequences stated in R2:**
  - The uniqueness hypothesis of v3 thm:general is necessary at interior priors.
  - Distinct members of U_add have disjoint sets of interior Bayes priors.
- **Clarification (§0.3.1):** this concerns the Bayes minimiser per interior weighting. It does not say that an (S) selection maps p to the p-Bayes model (Example AUD-1).
- **Used for:** Theorem N, Prop P, R5 Theorem PC.

### R2 Theorem N (no interior nesting for additive systems; any n ≥ 2)
- **Status:** REFEREED-REPAIRED (R6). The main argument is correct. The sufficiency clause "(interior relative to Δ)" is FALSE as worded and is replaced by interior relative to aff Δ.
- **Statement:** Work in the setting of Lemma U. Let D_{K_A}, D_{K_B} ∈ M satisfy (Nest): R_σ(A, B) is non-null for every mixed σ. Then A and B are not both undominated. (Nest) holds whenever K_A ⊂ int_aff K_B, which forces K_A ⊆ int Δ.
- **Counterexample to the original wording (R6):** n = 2, K_A = [0, ½], K_B = [0, ¾]. Here K_A lies in the Δ-relative interior of K_B, but R_{(+,−)} is null. Such a pair can lie on one monotone additive path.
- **Scope (audit):** this does not exclude any individual imprecise target. A target can have its own system, which need not also vindicate a model nested inside it. Example: an ε-contamination target T1 and the uniform precise model are never *both* in U_add.
- **Used for:** the additive rigidity behind Theorem R, R5 UN and PC, and R7.

### R2 Proposition N2 (n = 2 form)
- **Status:** REFEREED-CORRECT. Not listed separately by R6. R9 checked that R7 Lemma A (repaired), applied with φ ≡ 0, yields it, and that strict nesting α_B < α_A ≤ β_A < β_B is equivalent to K_A ⊂ int_aff K_B.
- **Statement:** In n = 2, under Lemma U's hypotheses, U_add contains no strictly nested pair. Here R1 and R2 are the two mixed patterns.
- **Used for:** the (⇒) direction of Theorem R.

### R2 Proposition P (n = 2: the additive undominated set is a continuous monotone path)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** Let n = 2, under Lemma U's hypotheses. Then U_add = {B_t : t ∈ [0, 1]}, where:
  - B_t is the unique t-Bayes model, including at t = 0 and t = 1, because ranks are distinct at a vertex;
  - the endpoints α(t), β(t) are non-decreasing and continuous;
  - B_0 and B_1 are the world-2-best and world-1-best evaluable models.
- **Clarification:** an (S) selection may traverse this path with a different parametrisation (Example AUD-1).
- **Used for:** Theorem R, R5 Cor UN2, R7 Cor 4.1.

### R2 Theorem R (two-world reduction)
- **Status:** REFEREED-CORRECT (R6; the Step 5 edge cases are only sketched, and R6 found them fine).
- **Statement:** Let n = 2 and let L be any ranking system on a decomposable domain M with (G), (IB), (LA), (S), (C). Then U_L is the undominated set of some additive strictly guiding (LA), (S), (C) system on M iff U_L contains no strictly nested pair.
- **Scope (audit; §0.3.3):** this is equivalence of whole undominated families. It is stronger than needed for coverage of one target. For n = 2 every target is already covered (v3).
- **Used for:** the reduction of two-world rigidity to no-nesting (R5 Cor UN2, R7 Cor 4.1).

### R2 Proposition 5 (countable unanimity; any n)
- **Status:** REFEREED-CORRECT (R6). Minor decomposable-domain wording: strict (G) forces strictness of ℓ = Σ c_k L^k only on the advice in the advice ranges, and that suffices.
- **Statement:** Let X ⪯_i Y ⇔ L^k_i(X) ≤ L^k_i(Y) for all k ∈ ℕ. Each L^k_i is an integral of weakly ordered local penalties (good ≤ silent ≤ bad ≤ ×) with integrable envelope h_k. Suppose the combined ranking has strict (G), (IB), (LA), (S), (C). Then U_L contains no pair satisfying (Nest).
- **Used for:** no-nesting beyond additivity. It is superseded by R5 Thm UN with R8's extra step.

### R2 Theorem 6 (one lexicographic world, one additive world; n = 2)
- **Status:** REFEREED-CORRECT (R6). It is re-proved and generalised by R7 Thm 1′₂, case (b).
- **Statement:** Let n = 2, with a decomposable domain M and (LA), (S), (C).
  - World 2 is additive and strictly guiding.
  - World 1 ranks lexicographically by (L¹_1, L²_1). The levels are additive, L¹_1 is weakly guiding, and L²_1 is weakly guiding and strict where L¹_1's local differences vanish.

  Then U_L has no strictly nested pair, so by Theorem R it is additively realisable. The same holds with the worlds swapped. The class contains rankings with no additive one-sided extension (world 1 of Prop 4).
- **Used for:** a non-Archimedean case of Conjecture 1.

### R2 Theorem 7 (local minimum / countability at lexicographic worlds; any n)
- **Status:** REFEREED-CORRECT (R6). (C) is not needed.
- **Statement:** Suppose world i ranks by lex(L¹_i, L²_i) with real-valued levels, which need not be additive, and (S) holds. Let f_i(q) = L¹_i(C_q).
  - If some Z ∈ M has L¹_i(Z) = f_i(p) and L²_i(Z) < L²_i(C_p) ("p is improvable at i"), then p is a local minimum of f_i.
  - Hence {f_i(p) : p improvable at i} is countable.
  - Under (LA) and (S), via Fact 0(b), the set {L¹_i(X) : X ∈ U_L improvable at i} is also countable.
- **Used for:** R3 P1–P3, R7 (T7), Lemma SF and Lemma 7′.

### R2 "avoidable exactly when" (sentence after Theorem 7)
- **Status:** GAP. Only necessity is proved (audit).
- **Corrected statement:** if (S) holds, the improvable members of U_L occupy only countably many primary levels at each lexicographic world. Countability is a necessary condition for (S). It has not been shown to be sufficient.

### R2 Proposition 8 (decoupled lexicographic rankings: nesting in U, failure of (S); n = 2)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:**
  - **Domain.** Fix nested A = D_{[α_A,β_A]} and B = D_{[α_B,β_B]} with R1 and R2 as in §0.2. M₀ consists of the models agreeing with A off R1 ∪ R2, with advice ranges {+, 0} on R1 and {0, −} on R2 (on every other pair every evaluable model gives A's advice). Write a model as (S, T), where S is its +-part of R1 and T is its silent part of R2.
  - **Rankings.** World 1 is ranked by lex(ν₁(R1 ∖ S), ν′₁(R2 ∖ T)) and world 2 by lex(ν₂(S), ν′₂(T)). On R1, ν₁ = (1 − r)μ and ν₂ = rμ; on R2, ν′₁ = (1 − r)μ and ν′₂ = rμ.
  - **Conclusion.** (G), (IB), (LA), (C) hold, and U = {all D_{[x,y]} : x ∈ [α_B, α_A], y ∈ [β_A, β_B]}. This is a 2-parameter family containing the nested pair. Every incoherent model is dominated, but no selection satisfies (S). (E) is not claimed.
- **Used for:** showing that lexicographic independence can enlarge undominated sets, and that (S) kills this through Theorem 7.

### R2 Conjecture 1 and Conjecture 1′; Q1 for n ≥ 3
- **Status:** CONJECTURE / OPEN.
- **Statements:**
  - **Conjecture 1.** In n = 2, every (G), (IB), (LA), (S), (C) system on a decomposable domain has no strictly nested pair.
  - **Conjecture 1′.** The same for two-level lex rankings at both worlds.
  - **Q1 for n ≥ 3** is open.
- **Current status:**
  - Conjecture 1 is proved for additive systems (R2), sandwiched systems (R5 Cor UN2), one-lex-plus-additive systems (R2 Thm 6) and class 𝓛₂ (R7 Thm 1′₂). Otherwise it is open.
  - Conjecture 1′ for two levels with additive levels is now a theorem (R7 Thm 1′₂). For three or more levels it is open (R7 Conjecture 1′_m).

---

## 3. R3: non-additive (lexicographic / incomplete) coverage attempts (R3_notes.md)

**Conventions.**
- A **lex ranking** at world j: X ⪯_j Y ⇔ F_j(X) < F_j(Y), or [F_j(X) = F_j(Y) and S_j(X) ≤ S_j(Y)].
- F_j = ∫ φ_j and S_j = ∫ ψ_j, with integrable envelopes.
- φ_j is weakly increasing along the world-j guidance order, and ψ_j is strictly increasing.
- Such a ranking is complete and satisfies strict (G) and (IB).
- F is **error-only** if φ_j(g, a) = 0 whenever a is good or silent at j.

### R3 §2.1 Constant-level lemma
- **Status:** REFEREED-CORRECT (R6). Completeness is not needed.
- **Statement:** Assume (S). If C_q = C* for all q in a set Q, then for every p ∈ cl Q and every world i, C_p ⪯_i C*. If C* is undominated, C_p is tied with C* at every world. Suppose moreover that (G) is strict at k, p = e_k, and C_{e_k} differs from C* on a non-null set where C*'s advice is not the best advice in the advice range at k. That situation is impossible.
- **Used for:** Cor 2.1a; Theorem L Step (4); R5 Lemma TJ "use".

### R3 Corollary 2.1a
- **Status:** REFEREED-REPAIRED (R6). The "in particular" clause needs K ≠ Δ.
- **Statement:** Let e_k ∉ K, with (LF) at D_K, strict (G) at k, and (S). Then e_k ∉ cl{q : C_q = D_K}. In particular, if K ≠ Δ, the selection cannot equal the target on all of int Δ.
- **Note:** if ℓ_k(K) = u_k(K), D_K may give "−" rather than silence just outside D_K near z = e_k − ℓ_k(K)𝟙. Neither is best at k, so the conclusion stands.
- **Used for:** ruling out the constant selection.

### R3 §2.2 (weak additive extensions transfer the Bayes condition)
- **Status:** NOT-REFEREED [author: CHECKED].
- **Statement:** Assume (LA) and (S), and suppose that at each world X ⪯_i Y ⇒ F_i(X) ≤ F_i(Y) for an additive, merely weakly guiding F_i.
  - For every prior r some selected model is F-r-Bayes.
  - Wherever the F-r-Bayes model is unique, it is coherent and selected.
  - The target, being competitive on Ω, is F-w-Bayes for some w ∈ Δ.
  - For lex rankings with a strictly guiding secondary, every lexicographic r-Bayes model at interior r is coherent when it is unique.
- **Used for:** recasting lex rankings as a non-Archimedean measurable CPM problem.

### R3 §2.2 vector-additive remark
- **Status:** NOT-REFEREED [author: PROVED under its hypothesis].
- **Statement:** Suppose X ⪯_i Y ⇔ L⃗_i(X) − L⃗_i(Y) ∈ P_i, where L⃗_i is a finite vector of additive losses and P_i is an additive monoid containing 0. Suppose P_i ⊇ −C for a nonempty open convex cone C in the span V of the differences. Then either all models are mutually ⪯_i-comparable both ways, which contradicts strict (G), or some nonzero λ ∈ C* gives a weakly guiding weak extension λ·L⃗_i that is not constant on M.
- **Used for:** placing vector-additive rankings under §2.2.

### R3 §2.3 (partial-lexicographic undominated models must be coherent)
- **Status:** REFEREED-CORRECT (R6). (C) is not needed.
- **Statement:** Take a lex system with error-only F and 0 ∈ A(g) a.e. For ∅ ≠ T ⊆ Ω let 𝓜_T = {X ∈ M : F_j(X) = 0 for all j ∈ T}; this is a decomposable domain. Let a ∈ [0, ∞)^{Ω∖T} and b ∈ Δ_T. Suppose X is the a.e.-unique minimiser over 𝓜_T of
  Σ_{j∉T} a_j F_j + Σ_{j∈T} b_j S_j.
  Then X is undominated. Under (S) it is tied with, hence equal to, a selected model, so it is coherent.
- **Used for:** R3 §5.4(i).

### R3 §2.4 (unanimity rankings do not help competitiveness)
- **Status:** NOT-REFEREED [author: CHECKED].
- **Statement:** Let X ⪯_i Y ⇔ L^θ_i(X) ≤ L^θ_i(Y) for all θ ∈ Θ_i, where each L^θ_i is strictly guiding additive.
  - This satisfies (G) and (IB). Its sections are closed whenever each q ↦ L^θ_i(C_q) is lower semicontinuous.
  - A selection competitive for this system is competitive for every single-loss system obtained by choosing one θ at each world.
  - So incompleteness of this kind relaxes undominatedness only, not the Bayes structure.
- **Used for:** motivation for R5 Thm UN, which proves the corresponding no-nesting statement.

### R3 Lemma P1 (lower semicontinuity)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** For a lex system with additive levels (primary F_j) and a selection with closed sections, q ↦ F_j(C_q) is lower semicontinuous on Δ for every j.
- **Used for:** Theorem L Step (1).

### R3 Lemma P2 (Lagrangian condition)
- **Status:** REFEREED-CORRECT (R6).
- **Statement:** In the same setting, suppose p ∈ cl{q : F_j(C_q) < F_j(C_p)}. Then one of the following holds:
  - C_p is F_j-minimal on M;
  - C_p is F_j-maximal on M;
  - there is λ ∈ ℝ such that C_p minimises S_j + λF_j over M, equivalently its advice is a.e. a pointwise minimiser of ψ_j + λφ_j over A(g).
- **Used for:** Cor P3.

### R3 Corollary P3 (staircase)
- **Status:** REFEREED-CORRECT (R6). "Not Lagrangian" must include "not F_j-extremal".
- **Statement:** Let O ⊆ Δ be open, and suppose that at no q ∈ O is C_q Lagrangian at j in the sense of P2, extremal cases included. Then:
  - every q ∈ O is a local minimum of F_j ∘ C;
  - F_j ∘ C takes only countably many values on O;
  - every strict sublevel set {F_j ∘ C < c} ∩ O is relatively closed.
- **Used for:** Theorem L Step (3).

### R3 Theorem L (error-only primaries cannot give (S))
- **Status:** REFEREED-CORRECT (R6), with the Step (3) wording repaired. Per the audit, **(H1)–(H3) must be kept in every statement and summary.** Example AUD-2 shows that (H1) cannot be dropped.
- **Setting:** a decomposable domain M with 0 ∈ A(g) a.e. At each world there is a lex ranking with error-only additive primary F and strictly guiding additive secondary S. Fix a world k, and let B_k be the model that gives, pointwise, the best advice in the advice range at k.
- **Hypotheses:**
  - **(H1) Vertex payment.** F_j(B_k) > 0 for every j ≠ k.
  - **(H2) Free trade-off.** For each j ≠ k:
    - a non-null set of problems is F-free (φ_i(g, a) = 0 for all i and all a ∈ A(g)) and has different best advice in the advice range at k and at j;
    - a non-null set of problems has, in its advice range, advice that is bad at both k and j and has φ_j > 0.
  - **(H3) Genericity.** For every a ∈ [0, ∞)^{Ω∖{k}}, a.e. problem has a unique minimiser of ψ_k + Σ_{j≠k} a_j φ_j over A_k(g) = {a ∈ A(g) : φ_k(g, a) = 0}.
- **Statement:** Under (H1)–(H3) no selection satisfies (S). This holds for any target, any (LF), and any n ≥ 2.
- **Step (3) repair (R6):** on the set in (H2), second half, the only kinds of advice with φ_j > 0 are bad or contradictory at k. Silence beats them in ψ_k + a·φ and lies in A_k(g). So φ_j(C_q) is zero there, and C_q is not F_j-maximal.
- **Scope:**
  - R3 Remark (i) says the theorem "covers the Σ_T-flavoured evaluator". Read it as covering lex rankings with an error-only primary and a *strictly guiding* secondary. These satisfy strict (G).
  - They are not Σ_T systems in the brief's sense, where good ~ silence at T-worlds. Per §0.3.6, conclusions do not automatically transfer to Σ_T.
  - Remark (ii): the theorem does not cover primaries that reward truth (φ_j(good) < φ_j(silence)).
- **Used for:** excluding a natural class of non-additive designs for every target.

### R3 §4 Remark (ii) (residual when (H1) fails at every vertex, n = 3)
- **Status:** GAP (R6).
- **Original claim:** if (H1) fails at every vertex, at least two of the single-negative sign patterns N_j are completely F-free. So the residual contains the measurable additive CPM problem near the middles of two facets of D_K.
- **What is established:** failure of (H1) gives φ_j(accept h) = 0 for h ∈ N_j with j = l(k) only. Accepting −h on the same problem is not controlled.
- **Corrected scope:** the claim holds where accepting −h is not in the advice range on N_j, as on the §5 domains. In general it is not established.

### R3 §4 Remark (iii) (pointwise secondary)
- **Status:** NOT-REFEREED [author: CHECKED, sketch].
- **Statement:** Replacing S by the pointwise order ⊴_j keeps (G), (IB) and closedness, but breaks competitiveness on F-free problems. That variant therefore needs F-free problems to be null.

### R3 §5.2 (geometry of the T1 lex system)
- **Status:** REFEREED-CORRECT (R6).
- **Data:** n = 3, u = 𝟙/3, c = (1 − ε)/3, K = {m ∈ Δ : m_j ≥ c for all j}, with vertices v_j = (1 − ε)u + εe_j. Fix 0 < s < 1 and put K′ = u + s(K − u) ⊆ ri K and U = D_{K′}.
  - For m with {k, l} = Ω ∖ {m}: K″_m = K ∩ conv(K′ ∪ {e_k, e_l}) and G_m = D_{K″_m}.
  - The shell is S = U ∖ D_K. For h ∈ S, J(h) = {m} if h ∈ G_m ∖ D_K, and J(h) = {j : h_j < 0} otherwise.
- **Statement:**
  - (a) [v_k, v_l] ⊆ K″_m.
  - (b) K ⊆ conv(K″_m ∪ {e_m}).
  - (c) K ⊆ conv(K″_k ∪ K″_l) for k ≠ l.
  - Consequences, modulo null sets:
    - (F1) D_K ⊆ G_m ⊆ U.
    - (F2) G_m ∖ D_K ⊆ {h_m < 0}.
    - (F3) the sets G_m ∖ D_K are pairwise disjoint.
    - (F4) U ∩ {h_k > 0, h_l > 0} ⊆ G_m.
    - (F5) every h ∈ S is mixed, ∅ ≠ J(h) ⊆ {j : h_j < 0}, and |J(h)| = 2 unless J(h) = {m} with h ∈ G_m ∖ D_K.
  - Also cl D_K ∖ {0} ⊆ U.
- **Used for:** §5.3–5.4.

### R3 §5.3 (a lex system for T1 whose lexicographic Bayes models are all coherent)
- **Status:** REFEREED-CORRECT (R6).
- **Statement.**
  - **Advice ranges.** The advice range of the pair {g, −g} contains + iff g ∈ U and − iff −g ∈ U; it always contains 0 and never ×. So M = {X : X ⊆ U a.e.} (the U-domain: the evaluable models are the measurable subsets of U), every evaluable model gives no advice on pairs {g, −g} with g ∉ U and −g ∉ U, and (LF) holds at D_K with N = U.
  - **Rankings.**
    - Secondary S_j: penalties 0, |g_j|, 2|g_j|, 4|g_j| for good, silent, bad, contradictory advice.
    - Primary (error-only): F_j(X) = ∫ |h_j| dμ over the problems on which X accepts an orientation h ∈ S with j ∈ J(h).
    - World j is ranked by lex(F_j, S_j). The rankings are complete, with strict (G) and full (IB).
  - **Lexicographic r-Bayes model B_r (minimise r·F, then r·S).** It is unique. Its form depends on r:
    - r interior: B_r = D_K ∩ D_r;
    - r ∈ relint Δ_{kl}: B_r = D_r ∩ G_m, with the positive orthant adjoined;
    - r = e_k: B_r = U ∩ D_k = D_{conv(K′ ∪ {e_k})}.

    All of these are coherent, and D_K = B_r for every r ∈ K. So the target is undominated and (LA) holds.
  - **Contrast.** For additive rankings on the same domain, the r-Bayes model would be U ∩ D_r ≠ D_K.
- **Used for:** showing that for lex rankings, coherence of the Bayes family is not the bottleneck.

### R3 §5.4 (that system fails (S))
- **Status:** REFEREED-CORRECT (R6), both parts.
- **Statement:** The §5.3 system admits no selection satisfying (S).
  - **(i)** Take T = {1} and the objective S_1 + aF_3 on 𝓜_1, with a ∈ (0, (1 + c_0)/c_0) and c_0 = (1 − ε)/(3ε). Its unique minimiser X_a is undominated by §2.3, yet not convex modulo null sets.
  - **(ii)** Theorem L applies. For (H2), second half, R6 supplies witnesses: two-negative shell gambles near e_l − (c/(1 − c))(e_k + e_j), perturbed by −δ𝟙.
- **Note:** the "Diagnosis" paragraph after §5.4 is a set of unverified remarks. In particular, coherence of all partial-lexicographic models for the modified primary φ_j(h) = −P_K(h) is unchecked.
- **Used for:** concrete failure of the lex route for T1.

### R3 §6 (T3, T4)
- **Status:** open. These are remarks, not results.
- **What transfers:** §2.1, §2.3, P1–P3 and Theorem L are target-independent. So no error-only lex system satisfying (H1)–(H3) covers T3 or T4.
- **What does not transfer:** the §5 domain. For dim K < 2, both z and −z lie in ∂D_K for z ⊥ span K, so (LF) needs advice ranges {+, 0, −, ×} near the line ℝz, and no convex cone U ⊇ cl D_K ∖ 0 exists.
- **T4:** the realising prior must be interior (local face lemma).

---
## 4. R4: charts for the advice range {+, 0, −} and the residual case of T1 (R4_notes.md)

**Notation.** Take a pair g with advice range ⊇ {+, 0, −}.
- **Chart data.** c = ℓ(g, 0) − ℓ(g, +), c′ = ℓ(g, 0) − ℓ(g, −), d = c − c′. Write α_g(p) = c·p and β_g(p) = c′·p.
- **Chart regions.**
  - R(g) = {α > 0, α > β};
  - R(−g) = {β > 0, β > α};
  - the silence region is S(g) = {α ≤ 0, β ≤ 0}.
- **d-face.** F(g) = {p ∈ Δ : α_g(p) = β_g(p) > 0}. For the advice range {+, −}, F(g) = {d·p = 0} ∩ Δ instead.
- **Credal sets and lower previsions.** K_p is the interior credal set of R1 Thm 2.2(N2). P(p, h) = P_{K_p}(h) is jointly continuous (R1 Prop 3.1).
- **Lower-dimensional and precise priors.** Z = {p ∈ int Δ : dim K_p ≤ n − 2} and Z_pt = {p ∈ int Δ : K_p is a singleton}.
- **Lines.** ℓ_g = g^⊥ ∩ aff Δ.
- **Standing hypotheses.** R4 works with an additive system with (G) and (LA), (S), (C). Statements about U′ refer to a realisation of a target with (LF), with U′ from R1 Prop 2.5. Unless said otherwise, n = 3.

### R4 Theorem A (adjacency dichotomy)
- **Status:** REFEREED-CORRECT (R8). The dichotomy (i)/(ii) holds for any n; the wedge clause is an n = 3 notion.
- **Statement:** Let g be mixed with advice range {+, 0, −}. Exactly one of the following holds.
  - (i) **Adjacent:** F(g) ∩ int Δ ≠ ∅.
  - (ii) **Split:** R(g) ∩ int Δ = {α_g > 0} ∩ int Δ, R(−g) ∩ int Δ = {β_g > 0} ∩ int Δ, and {α_g > 0} ∩ {β_g > 0} ∩ int Δ = ∅.

  A pair with advice range {+, −} and g mixed is always adjacent. For n = 3, R1's "wedge" (apex of the concurrent lines in int Δ) is adjacent.
- **Used for:** replacing "wedge" by "adjacency" as the relevant invariant.

### R4 Theorem B (adjacency forces degenerate credal sets)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Assume (N1)–(N2), i.e. (LA), (S), (C). For a.e. pair g with advice range {+, 0, −} or {+, −}, K_p ⊆ g^⊥ for every p ∈ cl F(g) ∩ int Δ. In particular dim K_p ≤ n − 2 on F(g) ∩ int Δ.
- **Scope (audit):** this restricts the selected sets on such boundaries, but does not make adjacency inadmissible. Target-only (LF) allows other selections to be tangent or lower-dimensional.
- **Used for:** Cor B1–B2 and Thm C.

### R4 Corollary B1 (single-map form)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Let V be a set of orientations, and assume:
  - (H0)_V: for a.e. h ∈ V, both accepting h and silence are in the advice range;
  - (H2″)_V: a.e. pair meeting V, as g or −g, is non-adjacent.

  Then for a.e. h ∈ V, R(h) ∩ int Δ = {p·c(h) > 0} ∩ int Δ, with c(h) strictly sign-preserving. Hence for every interior q, B_q ∩ V ≈ {h ∈ V : q·c(h) > 0}; the exceptional set does not depend on q. (H2″)_V holds for every V if dim K_q = n − 1 for all q ∈ int Δ.
- **Used for:** Cor B2.

### R4 Corollary B2 (T1 without (H2))
- **Status:** CONDITIONAL on NOGO + PB + FA, exactly as R1 Thm 4.2. R8 found the reduction step correct.
- **Statement:** R1 Thm 4.2 remains true with (H2) replaced by (H0)_{U′} + (H2″)_{U′}; (H1) is still assumed. In particular, no additive realisation of T1 on the all-model domain satisfies (H1) and has full-dimensional K_q at every interior q. On that domain (H0) is automatic.
- **Remark (R8):** charts are identified only on int Δ. This is harmless, because NOGO, PB and FA evaluate maps only at interior priors.
- **Used for:** the conditional no-go for full-dimensional interior selections.

### R4 Remark B3 (a gap in R1 Thm 4.2)
- **Status:** REFEREED-REPAIRED (R8). The parenthetical "(and {0} on U′ ∖ cl D)" is deleted.
- **Statement:**
  - R1's (H2) still allows the advice range {+} (every evaluable model accepts h) on U′. Their charts (Δ) are not sign-preserving half-planes, so NOGO's weak-sign axiom fails there.
  - (LF) excludes singleton advice ranges near ∂D ∖ 0. But FA §10.1's forbidden-support step uses strict signs at z′ ≈ a + λb, generically in int D, and the advice range {+} near z′ (every evaluable model accepts) voids that step. Hence R1 Thm 4.2 needs (H0)_{U′}.
  - The advice range {0} cannot occur on a non-null subset of U′, since acceptance is in the advice range a.e. on U′ (R1 Props 2.4–2.5).
  - **Open (audit):** acceptance by every evaluable model inside D (all K_q avoiding a fixed region) is a separate potential escape on general decomposable domains. (LF) does not imply (H0), and excluding advice that every evaluable model gives there would be a new domain assumption.
- **Used for:** adding (H0) to the conditional no-go.

### R4 Lemma S (disjoint segments carry a null set of lines)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Let 𝒥 be any family of pairwise disjoint non-degenerate segments in ℝ². The set of lines that contain a member of 𝒥 has Lebesgue measure 0 in the (θ, r)-parametrisation of lines.
- **Used for:** Thm C.

### R4 Hypothesis (H1⁺); openness of N′; extension of Thm B
- **Status:** REFEREED-CORRECT (R8). Degree-0 homogeneity is used tacitly; it holds a.e. because interior Bayes models are cones, and everywhere on U′ ∖ S by continuity.
- **Definition (H1⁺):** there is a relatively closed null cone S ⊂ U′ such that, a.e. on U′ ∖ S:
  - advice ranges are {+, 0, −};
  - the normalised chart data (c_g, c′_g)/‖(c_g, c′_g)‖ agree with a function continuous on U′ ∖ S.
- **Statement:** under (H1⁺), N′ := {g ∈ U′ ∖ S : F(g) ∩ int Δ ≠ ∅} is open, and the conclusion of Thm B holds for *every* g ∈ N′.
- **Note (audit):** (H1⁺), like (H1), is an extra regularity hypothesis.

### R4 Theorem C (under continuity, adjacency forces precise d-faces)
- **Status:** REFEREED-CORRECT (R8), as a theorem with hypothesis (H1⁺).
- **Statement:** Let n = 3. Assume (LA), (S), (C) and (H1⁺). For every g ∈ N′ and every p ∈ F(g) ∩ int Δ, K_p is a singleton; that is, F(g) ∩ int Δ ⊆ Z_pt.
- **Used for:** Cor C3.

### R4 Lemma C2 (precise points avoid silence)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** For a.e. pair g, λ(Z_pt ∩ int S(g)) = 0. Hence for a.e. adjacent pair whose silence cell has positive angle, the apex, if interior, is not a Lebesgue density point of Z_pt.
- **Used for:** constraints on the residual configuration.

### R4 Corollary C3
- **Status:** CONDITIONAL on NOGO + PB + FA, as in Cor B2. R8 found it correct as a conditional.
- **Statement:** Under (H0)_{U′} and (H1⁺), a T1 realisation must have a nonempty open set N′ ⊆ U′ of adjacent pairs, and every d-face of a pair in N′ consists of precise priors. In particular, if Z_pt contains no non-degenerate segment, T1 has no realisation.
- **Used for:** locating the residual: precise d-faces.

### R4 Proposition D (open precise regions)
- **Status as stated:** GAP (R8). Original: if K_p = {σ(p)} on an open connected O ⊆ int Δ, then σ is constant on O or diagonal-projective. The step "non-constant ⇒ injective" is supported only by one example. Non-constant, non-injective σ (one-dimensional image, folds, partial plateaus) is not excluded.
- **Corrected statement (REFEREED-REPAIRED by R8; author CHECKED; relies on the classical local fundamental theorem of projective geometry):** Let O ⊆ int Δ be open and connected with K_p = {σ(p)} on O, and **assume σ is injective on O (or a local homeomorphism)**. Then σ(p) = w⊙p/(w·p) on O for some w > 0.
  - The proof needs one step written out: invariance of domain gives σ(R(h) ∩ O) ⊆ {m·h > 0}, hence σ⁻¹(ℓ_h) ∩ O ⊆ L_h up to the silence set.
  - The diagonal step (det(e_i, x, Ae_i) = 0 on an open set of x ⇒ Ae_i ∥ e_i) is correct.
- **Open:** "non-constant ⇒ injective" is a CONJECTURE. R8 notes that the pattern argument can be made to work in the special case where σ(O) is a curve whose fibres are segments, but this is not written out.
- **Used for:** the "caps" picture, which is therefore conditional (§0.3.7).

### R4 Proposition F (one-sidedness)
- **Status:** CONDITIONAL on Prop D's projective form, so it inherits the injectivity / local-homeomorphism hypothesis. R8 found the argument correct given that form.
- **Statement:** Let O be as in corrected Prop D (σ injective on O, hence diagonal-projective), and let p_f ∈ int Δ with K_{p_f} not a singleton. Then no line through p_f meets O on both sides of p_f.
- **Consequence:** "no precise boundary ring around a full-dimensional core" holds only for such non-constant (here injective) σ. A constant precise region (K_p ≡ {m₀}) is untouched by F.
- **Used for:** constraining precise caps; the evidence for CONJECTURE R4.

### R4 Proposition G1 (ray equations)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Let κ = 1 + 3ε/(1 − ε). The ray equations FA (10.3), x₃ + 1/x₂ = x₁ + 1/x₃ = x₂ + 1/x₁ = κ + 1, have exactly two positive solutions:
  - x₁ = x₂ = x₃ = x₊, where x₊ + 1/x₊ = κ + 1 and x₊ > 1;
  - x₁ = x₂ = x₃ = x₋ = 1/x₊.

  Moreover x₊² > κ and x₋² < 1/κ, so both violate the box 1/κ ≤ x_i x_j ≤ κ (FA (10.2)) at every pair of vertices.
- **Numerical note (R8):** ray_box_cap.py's grid scan finds only x₊ for ε ≥ 0.2, because its filter discards x₋. R4's sentence "only x₊ and x₋ solve T³x = x (grid scan)" overstates the scan. The theorem is proved independently of the scan.
- **Used for:** Prop G2.

### R4 Proposition G2 (where adjacency would have to act)
- **Status:** CONDITIONAL on the conclusions of PB §§3–6 and FA §§3–9 (facet maps (10.1) and ray matching) holding for the realisation. R8 found it correct as a conditional. Its near-q* chain also uses B1, which adjacent pairs near the vertices could in principle disturb.
- **Statement:** For every vertex e_k and all small t > 0:
  - every neighbourhood of the FA §10.1 witness a(t), or of b(t), contains a non-null set of adjacent pairs;
  - each of these separates the witness prior q_η ≈ e_k + O(t) from part of its own accept-region, although α_h(q_η) > 0.

  Under (H1⁺) these pairs form an open set with precise d-faces (Thm C).
- **Used for:** describing the residual near the vertices.

### R4 §9 item 4 (edge blow-up)
- **Status:** REFEREED-CORRECT (R8 recomputed it) [author: CHECKED]. Its relevance is conditional on the facet-map framework of G2.
- **Statement:** At first order in t, a precise edge model σ(q₀) ∝ (1, ωt, 0) is compatible with the facet α's iff ω ∈ [κ/x₂, x₃]. This interval is nonempty iff x₂x₃ ≥ κ, that is, iff the upper box fails. Such an edge model then rejects both FA witnesses.
- **Numerical companion (§9 item 3, "identity cap" at e₁):** evidence only. Apex distance from e₁ ≈ 8.6·t; d-rays pairwise disjoint.
- **Used for:** showing that no contradiction arises locally at a vertex.

### R4 Example E (kinked contamination)
- **Status:** FALSE-AS-STATED (R8). The headline "(G) holds only if f ≡ 0" is false: f = (−1, −1, −1) gives the precise identity model, which is (G)-realisable. R4's second bullet (h_i → 0⁻ ⇒ f_i ≥ 0) is an invalid deduction, because c_i for i ∈ N(h) is invisible in the chart.
- **Correct parts:** let f ∈ ℝ³ and K_p = (1 − ε(p))p + ε(p)Δ with ε/(1 − ε) = (f·p)⁺. For mixed h, with m = min h < 0 < M = max h, P_{K_p}(h) ∝ p·h + (f·p)⁺m. The charts are exactly concurrent three-sector diagrams:
  - α = M p·(h + mf), β = −|m| p·(h + Mf), and d = (M + |m|) p·h;
  - the lines meet at {p·h = 0 = f·p};
  - the d-face lies in the precise layer {f·p < 0}.
- **Corrected statement (REFEREED-REPAIRED; proof by R8):** the family is (G)-realisable iff f ≤ 0, iff (f·p)⁺ ≡ 0 on Δ, iff K_p ≡ {p}.
  - Proof: the vertex property needs R(h) ⊇ a neighbourhood of δ_i for i ∈ P(h). Near δ_i, P ∝ h_i + f_i⁺m, which is negative for 0 < h_i < f_i|m| if f_i > 0.
  - Moral (unchanged): this natural exact-wedge mechanism realises only the precise model.
- **Used for:** evidence that wedges do not come for free.

### R4 §8 (K1) (essential chart normals)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Assume (H0) and non-adjacency on U′, so that ĉ = c/‖c‖ is defined a.e. on U′.
  - For every h ∉ Bad, R̃(h) = {P(·, h) > 0} is a.e. a half-plane H(h).
  - ĉ is continuous on U′ ∖ Bad in the relative topology.
  - P(·, h) ≥ 0 on cl H(h) and ≤ 0 on int Δ ∖ H(h).
- **Used for:** (K2)–(K3).

### R4 §8 (K2) (essential clusters)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Put U(w) = ⋂_r cl{ĉ(h) : h ∈ B(w, r) ∖ Bad}.
  - (Forward) If w ∈ D_{K_q}, every v ∈ U(w) has q·v > 0.
  - (Converse) If q·v > 0 for all v ∈ U(w), then w ∈ D_{K_q}.
- **Used for:** transferring PB's interior-margin lemma B2 without (H1).

### R4 §8 (K3) (transfer of PB Lemma 3.1 / Thm 3.2, "B1")
- **Status:** REFEREED-REPAIRED (R8).
- **Statement:** assume (H0), or the all-model domain, for acceptance near x⁻. Then PB's strict-sign theorem (B1) transfers without (H1):
  - **Positive case:** valid even with adjacent pairs.
  - **Negative case:** valid on split pairs.
- **Repair:** "x⁻ is accepted near e_i" holds as follows. For a small ball N around x⁻, dominated convergence gives μ(N ∖ D_{K_q}) → 0 as q → e_i. A convex cone containing all but a small fraction of a ball contains its centre. The negative case uses P(q, x⁺ + δ𝟙) = P(q, x⁺) + δ.
- **Used for:** partial removal of (H1).

### R4 §8 (K4) (forbidden support)
- **Status:** REFEREED-CORRECT (R8), on the all-model domain. On a decomposable domain it needs + in the advice range for a.e. h with h_S > 0.
- **Statement:** let q_η → q₀ with supp q₀ = S. Every Hausdorff limit point K* of K_{q_η} satisfies K* ⊆ Δ_S. Hence, for z′ with z′_S < 0, max_{K_{q_η}} m·z′ < 0 uniformly near z′ for small η. This replaces NOGO's use of strict signs of Φ in FA §10.1, without (H1).

### R4 Conjecture 4.3′
- **Status:** CONJECTURE.
- **Statement:** the remaining NOGO steps transfer with Φ-clusters replaced by essential clusters U(·). These are PB §§4–6 (exterior ratio law, unique facet trace, interior clusters) and FA §§3–9 (anchors, seeds, pinning, pencil test).

### R4 CONJECTURE R4 and "Residual R4"
- **Status:** CONJECTURE. The residual is an open problem.
- **Conjecture:** under (H0), a.e. pair meeting U′ is non-adjacent in any additive realisation of T1. Equivalently, no realisation has the residual structure below.
- **Residual (as corrected).** Under (H0) and (H1⁺), with the vertex statements conditional on the near-q* chain, any T1 realisation must have:
  - a full-dimensional core around p* with split charts;
  - an open set N′ ⊆ U′ of adjacent pairs with precise d-faces;
  - d-faces cutting the FA witnesses near each vertex.

  The description "open precise regions are diagonal-projective caps" holds **only for injective σ** (Prop D gap).
- **Not exhaustive (audit).** The following escapes are outside this residual and remain open:
  - advice that every evaluable model gives, away from the target boundary ((LF) does not imply (H0); Remark B3);
  - merely measurable charts ((H1)/(H1⁺) are extra);
  - non-injective precise regions (Prop D);
  - the conditional status of the NOGO/PB/FA chain itself.

---

## 5. R5: does closed competitive choice force additive undominated sets? (R5_notes.md)

Under (LA), (S), (C), U_L = C_L ⊆ coherent (R2 Lemma 1). (Nest) and R_σ are as in §0.2.

### R5 Lemma N1 (a nested pair may be taken selected, at interior priors)
- **Status:** REFEREED-CORRECT (R8). For b, use the mirror pattern: σ = + exactly on supp b, and switch B to A's acceptance.
- **Statement:** Assume strict (G), (IB), (LA), (S), (C), and let A, B ∈ U_L satisfy (Nest). Then either A and B are tied at every world, or there is a selection C′ satisfying (S), with the same C_L, and points a ≠ b in int Δ with C′_a = A and C′_b = B.
- **Used for:** Thm UN Step 0.

### R5 Lemma TJ (tie-midpoint)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Assume (C). Suppose that at each world i finitely many additive functionals Φ_i = (Φ_i^1, …, Φ_i^{m_i}) cut out the ties: X ~_i Y ⇔ Φ_i(X) = Φ_i(Y). Examples: additive rankings, finite-level lex rankings with additive levels, finite unanimity. Then two distinct members of C_L are never tied at every world.
- **Consequence stated in R5:** in these classes a nested pair cannot arise by a "tie-jump", and every member of U_L is itself selected.
- **Used for:** constraints on any counterexample to Conjecture 1.

### R5 Definition (sandwiched world)
- **Status:** REFEREED-CORRECT (R8; consistent, and covers unanimity of strictly guiding losses).
- **Definition:** world i is sandwiched by a nonempty family Θ_i of additive losses, each strictly guiding at i on M, if:
  - (W) X ⪯_i Y ⇒ L^θ(X) ≤ L^θ(Y) for every θ ∈ Θ_i;
  - (R) X ≺_i Y ⇒ L^θ(X) < L^θ(Y) for some θ ∈ Θ_i.

  No cardinality, measurability in θ, or completeness is assumed.

### R5 Theorem UN (sandwiched systems carry no nested pair; any n ≥ 2)
- **Status:** REFEREED-REPAIRED (R8), with two repairs. (IB) is not used in the proof; strict (G) is used in Step 0.
- **Statement:** Let n ≥ 2, with a decomposable domain M and strict (G), (IB), (LA), (S), (C), and every world sandwiched. Then U_L contains no pair satisfying (Nest). In particular:
  - there are no D_{K_A}, D_{K_B} ∈ U_L with K_A ⊂ int_aff K_B (Repair 1: aff-Δ interior, §0.3.2);
  - in n = 2, there is no strictly nested pair.
- **Repair 2 (unanimity of merely weakly guiding losses, R2 Prop 5's setting, any cardinality).** UN applies only after one extra step (R8):
  - By the essential-union argument, strict (G) of the unanimity ranking yields a countable subfamily whose weighted sum ψ_i = Σ c_k L^{θ_k} is strictly guiding on the advice in the advice ranges.
  - Then Θ′_i = {θ + ψ_i : θ ∈ Θ_i} sandwiches ⪯_i, and every member is strictly guiding.
  - With this step written out, UN covers R2's open uncountable case.
- **Used for:** two-world rigidity (Cor UN2) and the n ≥ 3 pairwise shadow.

### R5 Corollary UN2 (n = 2)
- **Status:** REFEREED-CORRECT. It combines UN with R2 Thm R and Prop P; R9 confirmed its use in R7 Cor 4.2.
- **Statement:** For every sandwiched system on a decomposable domain with strict (G), (IB), (LA), (S), (C), U_L is the undominated set of an additive strictly guiding (LA), (S), (C) system on the same domain, namely a continuous monotone path.
- **Scope:** family equivalence (§0.3.3).

### R5 Lemma X (cross-competitiveness; n = 2, any preorders)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Under (G), (IB), (LA), (S), (C), let A, B ∈ U_L be strictly nested, with R1, R2 and region preorders q1, q2 on R = R1 ∪ R2 defined via X_Z as in R5 §3. For all measurable U ⊆ R1 and W ⊆ R2:
  - (★A) W ⪯_{q1} U or U ⪯_{q2} W;
  - (★B) U ⪯_{q1} W or W ⪯_{q2} U.

  For complete rankings, the two worlds never strictly disagree on a cross pair.
- **Used for:** Prop X2 and Lemma 4.4.

### R5 Proposition X2 (proportional Archimedean parts)
- **Status:** REFEREED-CORRECT (R8) [author: CHECKED]. It is conditional on its own hypotheses, completeness and fineness, which are not free in n = 2.
- **Statement:** In addition to Lemma X, suppose both rankings are complete and q1, q2 are fine on R (CCF §5). Let P1 and P2 be the Savage–Wakker finitely additive probabilities almost agreeing with q1 and q2. Then there is κ > 0 with P2 = κP1 on the measurable subsets of R.
- **Used for:** locating the residual of Conjecture 1 in the non-Archimedean part.

### R5 Lemma 4.1 (integration over ordered fields)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Let F ⊇ ℝ(ε) be real-closed and p an F-prior. If p·ℓ(g, a_X(g)) ≤ p·ℓ(g, a_Y(g)) in F for a.e. g, then p·L(X) ≤ p·L(Y). If moreover the inequality is strict on a non-null set, the conclusion is strict. Hence "pointwise F-p-minimiser a.e." ⇔ F-p-Bayes.

### R5 Proposition 4.2 (conditional no-nesting for finite lex)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Suppose every world has a finite-level lex ranking with additive levels and a strictly guiding composite, for any n, with strict (G), (IB), (LA), (S), (C). If every member of U_L that is competitive on Ω is F-p-Bayes for some F-prior p, then U_L has no pair satisfying (Nest).

### R5 Example 4.3 (undominated, not F-Bayes)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Take two worlds and two lex levels, with x = (½ − 2ε, −½ + ε), y = (−½ − 2ε, ½ + ε) ∈ ℝ(ε)², and K = {λx + λ′y : λ, λ′ ∈ [0, 1] real}. K is the attainable change set of a decomposable domain with two-element advice ranges on two disjoint regions, with legitimate guidance signs. Then:
  - 0 (the base model) is undominated and competitive;
  - no F-prior supports K at 0.
- **Comments:**
  - No full (S)/(C) system is built around this configuration.
  - Per R7/R9, no (LA), (S), (C) system of class 𝓛₂ can have this configuration as a face 𝔅_t with t ∈ (0, 1) (see R7 Remark 3).
- **Used for:** showing that the separation step "competitive ⇒ F-Bayes" fails for lex rankings.

### R5 "Region-only domain" claim (§4)
- **Status:** CONJECTURE (labelled so by the author; heuristic).
- **Statement:** no finite-lex nested counterexample lives on a domain with non-singleton advice ranges only on R.

### R5 Lemma 4.4 (standard parts proportional)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Let n = 2, with finite lex rankings with additive levels at both worlds, and A, B ∈ U_L strictly nested. Suppose the standard parts of the exchange values γ_l(U) and δ_l(W) are positive on every non-null U ⊆ R1 and W ⊆ R2. Then st(γ_2/γ_1) and st(δ_2/δ_1) take one common constant value κ on all non-null U and W. Only standard parts are forced.

### R5 Theorem PC (pattern compatibility for additive systems; any n)
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Take an additive strictly guiding (LA), (S), (C) system on a decomposable domain with A ≠ B ∈ U_add, Bayes at p_A and p_B. For every realised mixed pattern τ = (P, N) ∈ T(A, B), there are i ∈ P and j ∈ N with p_{A,i} p_{B,j} ≥ p_{A,j} p_{B,i}. In particular T(A, B) is never the set of all mixed patterns.
- **Used for:** intrinsic necessary conditions for additive representability in n ≥ 3.

### R5 Theorem UN′
- **Status:** REFEREED-CORRECT (R8).
- **Statement:** Theorem UN holds with (Nest) replaced by (AllPat): T(A, B) is the set of all mixed patterns. The splice is taken on Z′ ∩ {|g| < 1} for a non-null cone Z′ ⊆ {a_A ≠ a_B}.
- **Used for:** the n ≥ 3 pairwise shadow of rigidity for sandwiched systems.

### R5 Theorem R_n (additive representability vs chart parametrisation)
- **Status:** REFEREED-REPAIRED (R8). The diagram reformulation needs per-prior quantifiers. The boundary-tie gap remains, so this is **not** an unconditional iff (audit).
- **Statement:** Let L satisfy strict (G), (IB), (LA), (S), (C) on a decomposable domain M.
  - **(a)** Suppose there are:
    - an onto map π : Δ → U_L;
    - a measurable penalty field ℓ(g, a) ∈ ℝⁿ (a ∈ A(g)), with coordinate i strictly increasing in world-i rank and an integrable envelope;

    such that for **every** p ∈ Δ the minimiser of p·ℓ(g, ·) over A(g) is a.e. unique and a.e. equal to π(p)'s advice. Then U_L = U_add for ℓ, and that additive system satisfies (LA), (S), (C).
  - **(b)** Conversely, suppose U_L = U_add for some strictly guiding additive (LA), (S), (C) system. Then the Bayes minimiser is a.e. unique and coherent at every interior p and at every vertex.
    - At non-vertex boundary priors uniqueness can fail (R1 C1).
    - Members of U_L that are Bayes only at tied boundary priors may be missed by the Bayes map. The exact boundary condition is R1 Remark 2.3.
- **Repair (R8):** R5's "Equivalently, for a.e. g the partition p ↦ a_{π(p)}(g) is a vertex-respecting diagram" is ill-posed, because a_{π(p)}(g) is defined only modulo null sets, separately for each p. The condition must be stated per prior, as in (a). Its converse also needs a measurable choice of (c, c′) where a boundary line is invisible in Δ.
- **Used for:** framing Conjecture R_n.

### R5 Conjectures
- **Status:** CONJECTURE.
- **Conjecture 1 (n = 2) and Conjecture 1′:** see the R2 entry.
- **"One two-level lex world + additive others, n ≥ 3, no AllPat":** CONJECTURE.
- **"Pairwise conditions are insufficient for n ≥ 3" (Remark 5.4, heuristic):** CONJECTURE.
- **Conjecture R_n:** under strict (G), (IB), (LA), (S), (C) on a decomposable domain, U_L admits a chart parametrisation. For n = 3 it would reduce T1–T4 coverage by any (IB) system to additive realisation restricted to the advice ranges, which is itself open.
- **Remark 2(c):** charges in place of integrals are not covered by UN.

---
## 6. R7: two-level lexicographic systems in two worlds (R7_notes.md)

n = 2 throughout. Strictly nested means α_B < α_A ≤ β_A < β_B, equivalently K_A ⊂ int_aff K_B (consistent with R6's repair).

**Class 𝓛₂.** At world i, X ⪯_i Y ⇔ P_i(X) < P_i(Y), or [P_i(X) = P_i(Y) and S_i(X) ≤ S_i(Y)].
- P_i = ∫ φ_i and S_i = ∫ ψ_i, measurable, with an integrable envelope on the advice ranges.
- For a.e. g and all a, b ∈ A(g) with rank_i(a) < rank_i(b):
  - φ_i(g, a) ≤ φ_i(g, b) (weak guidance of the primary);
  - (φ_i, ψ_i)(g, a) <_lex (φ_i, ψ_i)(g, b) (strict guidance of the composite).
- ψ_i is unrestricted where φ_i is strict. Additive worlds are the case φ_i ≡ 0.

**Faces and fibres.**
- 𝒫 = {(P_1, P_2)(X) : X ∈ M} is the primary range.
- T_X is the set of t ∈ [0, 1] at which π(X) = (P_1, P_2)(X) minimises tP_1 + (1 − t)P_2 over 𝒫.
- 𝔅_t is the decomposable domain of pointwise minimisers of tφ_1 + (1 − t)φ_2, and X ∈ 𝔅_t ⇔ t ∈ T_X.
- J_t is the range of P_1 on 𝔅_t. F_t(x) = {X ∈ 𝔅_t : P_1(X) = x} is the fibre at level x.
- A level x is *ideal* if one fibre member minimises both S_1 and S_2 on the fibre.

### R7 §1 class 𝓛₂ and standing facts (L1), (Au), (PB), (Sp), (T7)
- **Status:** REFEREED-CORRECT (R9).
- **Statement:**
  - Each ⪯_i is a complete preorder satisfying strict (G), weak (G) and (IB).
  - (L1) = R2 Lemma 1.
  - (Au): finitely many additive functionals have a convex compact range on a decomposable domain.
  - (PB): minimising a real additive functional over a decomposable domain ⇔ minimising pointwise a.e.
  - (Sp): the splice "A on R1 ∩ {|g| < 1}, B elsewhere" is incoherent.
  - (T7) = R2 Thm 7 in U_L form; (C) is not needed, but (LA) and (S) are.
  - T_X is a nonempty closed interval for X ∈ U_L.
  - Endpoint fibres 𝔅_t^± (t ∈ (0, 1)) are decomposable domains on which φ_1 and φ_2 are a.e. constant. So (S_1, S_2) is an additive strictly guiding two-world system there.

### R7 Lemma F (faces are closed under domination)
- **Status:** REFEREED-CORRECT (R9).
- **Statement:**
  - (i) Let t ∈ (0, 1), X ∈ 𝔅_t, and let Y weakly dominate X. Then Y ∈ 𝔅_t and π(Y) = π(X).
  - (ii) If X ∈ 𝔅_1 and Y weakly dominates X, then Y ∈ 𝔅_1. Symmetrically for 𝔅_0; P_2 need not be preserved.
- **Consequence (F*), REFEREED-CORRECT:** for t ∈ (0, 1), X ∈ 𝔅_t is undominated ⇔ (S_1, S_2)(X) is Pareto-minimal in (S_1, S_2)(F_t(P_1(X))).

### R7 Lemma A (additive faces carry no nested pair)
- **Status:** REFEREED-REPAIRED (R9). The constant-primary hypothesis was missing and is added. Every application satisfies it.
- **Statement:** Assume (LA), (S), (C), so that (L1) is available. Let 𝔇 ⊆ M be a decomposable domain such that:
  - **φ_1 and φ_2 are a.e. constant on the advice ranges of 𝔇**, so P_1 and P_2 are constant on 𝔇 (the added hypothesis);
  - (S_1, S_2) is strictly guiding additive on 𝔇;
  - every weak dominator of a member of 𝔇 lies in 𝔇 and has the same primaries.

  Then 𝔇 ∩ U_L contains no strictly nested pair.
- **Applications:**
  - case (a0): 𝔇 = 𝔅_{t₀} with J a point;
  - case (a1) (min,min) and (max,max): 𝔇 = 𝔅^∓;
  - case (b), θ₀ = 0: 𝔇 = argmin_𝔐 φ_2.
- **Attribution (R9):** "no nesting on additive faces" should cite Lemma A, not R2 Thm N. Thm N would need (LA), (S), (C) for the face system, and these are unavailable.
- **Used for:** Theorem 1′₂.

### R7 Lemma SF (closed choice forces ideal fibres)
- **Status:** REFEREED-CORRECT (R9).
- **Statement:** Assume (LA), (S), (C) and class 𝓛₂. Then for every t ∈ (0, 1), every x ∈ int J_t is ideal.
  - The non-ideal set is relatively open in int J_t by convexity alone.
  - It is countable by (T7), which uses (S).
- **Used for:** Theorem 1′₂; it is the key new ingredient.

### R7 Corollary SF-L (two-sided Lagrangian at interior levels)
- **Status:** REFEREED-CORRECT (R9). The multipliers need not be unique; every argument works for any choice from the subdifferential.
- **Statement:** Let t ∈ (0, 1) and X ∈ U_L ∩ 𝔅_t with P_1(X) ∈ int J_t. Then there are λ, μ ∈ ℝ such that X minimises both S_1 + λP_1 and S_2 + μP_1 over 𝔅_t. Equivalently, its advice is a.e. a pointwise minimiser of both ψ_1 + λφ_1 and ψ_2 + μφ_1 over the advice ranges of 𝔅_t.

### R7 Lemma BWC (blind choice kills interior levels)
- **Status:** REFEREED-CORRECT (R9).
- **Statement:** Let t ∈ (0, 1). Suppose that on a non-null set Q of mixed problems:
  - the advice range of 𝔅_t contains two distinct kinds of advice a, b ∈ {+, 0, −} with φ_1(a) = φ_1(b);
  - every kind of advice in {+, 0, −} that lies in the advice range of 𝔅_t has that same φ_1.

  Then int J_t = ∅.

### R7 Lemma 7′ (depth-k staircase)
- **Status:** REFEREED-CORRECT (R9). It holds for any n and uses only (S) and Fact 0, hence (LA).
- **Statement:** Let world i rank by lex(L¹_i, …, L^m_i) with real-valued levels, and assume (S). Call X *improvable at depth k* at i if some Z ∈ M has L^j_i(Z) = L^j_i(X) for j < k and L^k_i(Z) < L^k_i(X). Then {(L¹_i, …, L^{k−1}_i)(X) : X ∈ U_L improvable at depth k} is countable.
- **Used for:** the m ≥ 3 sketch (§6).

### R7 Theorem 1′₂ (main result)
- **Status:** REFEREED-REPAIRED (R9). The statement is unchanged. The proof repairs:
  - use the repaired Lemma A;
  - case (c) Step 3: replace the "equal P_2" sentence by the two-line optimality argument;
  - mark the branch t_A = 1 as redundant, since Step 5 covers it;
  - Remark 1 should read "(S) enters through (L1) and (T7); (C) only through (L1)".

  R9: none of the defects touches the logic of the proof.
- **Statement:** Let n = 2, M any decomposable domain, class 𝓛₂ at both worlds, and assume (LA), (S), (C). Then U_L contains no strictly nested pair. Consequently, by R2 Theorem R, U_L is the undominated set of an additive strictly guiding (LA), (S), (C) system on M, and it is a continuous monotone path.
- **Scope:**
  - It contains the additive case (R2 Prop N2) and R2 Theorem 6. Case (b) re-proves Theorem 6 without requiring S to be guiding where φ is strict.
  - It covers R5 Example 4.3's class.
  - It is family equivalence (§0.3.3). It does not say the rankings themselves are additive.
- **Used for:** settling Conjecture 1′ for two additive levels.

### R7 Corollary 4.1
- **Status:** REFEREED-CORRECT (R9).
- **Statement:** For n = 2 and any decomposable domain, every (G), (IB), (LA), (S), (C) system in class 𝓛₂ has the same undominated set as some additive strictly guiding (LA), (S), (C) system on the same domain. In particular such systems cover exactly the targets that additive systems cover with the same advice ranges. Since every two-world target is already covered (v3), the content is structural, not a coverage gain.

### R7 Corollary 4.2
- **Status:** REFEREED-CORRECT (R9).
- **Statement:** In n = 2, Conjecture 1 holds for every system whose two worlds are both sandwiched (R5 Cor UN2), and for every system whose two worlds are both of class 𝓛₂ (Thm 1′₂). The mixed case, one world of each kind, is open.

### R7 Remark 3 / §5.1 (Example 4.3's face is incompatible with (S))
- **Status:** REFEREED-REPAIRED (R9). The hypothesis is made precise.
- **Statement:** No (LA), (S), (C) system of class 𝓛₂ has the R5 Example 4.3 configuration as a face 𝔅_t with t ∈ (0, 1). In that face every interior level is non-ideal, contradicting Lemma SF. (S) fails only jointly with (LA), because (T7) uses Fact 0.
- **Scope:** a system in which the 4.3 set sits inside M but is not a face is not addressed by SF. As far as nesting goes, it is addressed by Theorem 1′₂.

### R7 §5.2 (a single exceptional non-ideal level is impossible)
- **Status:** REFEREED-CORRECT (R9). It is pure convexity; (S) is not needed.
- **Statement:** for t ∈ (0, 1), the non-ideal set in int J_t is relatively open, so it cannot be a single point.

### R7 §5.3 (pair at the two ends of an edge)
- **Status:** REFEREED-CORRECT (R9). It is case (a1), (min,max), of Thm 1′₂.

### R7 §5.4 and §0 item 3 ("the countable staircase lives only at vertices of the primary range and at endpoints of primary edges")
- **Status:** FALSE-AS-STATED (R9). It is not used in Theorem 1′₂.
- **Counterexample (R9):**
  - Take an additive strictly guiding (LA), (S), (C) system with B_0 ≠ B_1, written in class 𝓛₂ as world 1 = lex(0, ℓ_1) and world 2 = lex(ℓ_2, 0).
  - Then 𝒫 = {0} × [a, b] with a < b, and F_1 = 𝒫.
  - Every B_s with s ∈ (0, 1) sits at an interior point of this edge and is improvable at world 1 by B_1.
  - So a continuum of improvable members fills the interior of a boundary primary edge, all sharing the world-1 primary level 0.
- **Corrected statement (supplied and proved by R9; not separately re-refereed):** let t ∈ (0, 1).
  - No member of U_L at an interior level x ∈ int J_t is improvable at either world.
  - Hence, on interior faces, improvable members occur only at endpoints of J_t and on faces where J_t is a point (vertices of 𝒫).
  - On the boundary faces F_0 and F_1, improvable members can fill the whole face, sharing one primary level of the corresponding world.
  - Proof sketch (R9): m(x) = min{S_1(Z) : P_1(Z) = x} and g_1 are convex, hence continuous on int J_t. So {x : m(x) < g_1(x)} is open, and by (T7) it is countable, hence empty. The same holds at world 2 via P_2 = c_t − κ_tP_1.
- **Attribution:** "no nesting at those points" should cite Lemma A, not R2 Thm N.

### R7 §5.5 (pair on two different faces)
- **Status:** REFEREED-CORRECT (R9), as a summary of case (c). BWC flattens every face with t ∈ (0, t_A), not only those strictly between T_B and T_A.

### R7 §5.6 (structure of U_L for 𝓛₂)
- **Status:** NOT-REFEREED (author: "a sketch, not verified in full, and not used"). It describes U_L as additive Bayes paths at vertices and edge endpoints, joined by Lagrangian ramps along interior edges.
- **Caution:** read it with the R9 correction above. Boundary faces F_0 and F_1 can carry continua of improvable members.

### R7 §6 (three or more levels)
- **Status:** CHECKED as a sketch only, NOT-REFEREED, for branch (a). Cases (b) and (c) at depth ≥ 2 are not done.
- **Conjecture 1′_m (CONJECTURE):** Theorem 1′₂ holds for every finite number of additive lexicographic levels. Countably many levels have not been sketched.

---

## 7. The auditor's examples (AUDIT_ASSESSMENT.md)

These two examples are the auditor's own direct arguments. BRIEF2 accepts them. No separate referee was commissioned for them.

### Example AUD-1 (Bayes uniqueness is not uniqueness of the (S) selection)
- **Status:** NOT-REFEREED (auditor's direct argument; accepted in BRIEF2).
- **Construction:**
  - n = 2, all measurable models, local penalties at world i of (0, |g_i|, 2|g_i|, 4|g_i|) for good, silent, bad, contradictory advice.
  - The t-Bayes model is a.e. unique: B_t = D_{(t, 1−t)}, the precise model. Accepting g beats silence iff (t, 1 − t)·g > 0.
- **Statement:** the reindexed selection C_t := B_{t²}, t ∈ [0, 1], also satisfies (S):
  - its profiles t ↦ L_i(C_t) are continuous, so the sections are closed;
  - its endpoints C_0 = B_0 and C_1 = B_1 are the appropriate world ideals;
  - at every interior index C_t is undominated in complete rankings, hence competitive on both worlds.

  Yet C_t is generally not Bayes for the weight t.
- **Consequence (the precise uniqueness statement):** for a fixed additive system satisfying the axioms, each interior weighted objective has a unique Bayes minimiser modulo null sets. The axioms do not require an admissible selection to assign that minimiser to the same index.
- **Used for:** the reading of R1 Lemma 1.4, R1 Prop 3.1, R2 Lemma U and R2 Prop P (§0.3.1), and the caution on R1 Remark 2.3.

### Example AUD-2 (an error-only primary compatible with closed choice)
- **Status:** NOT-REFEREED (auditor's direct argument; accepted in BRIEF2). It is a counterexample to an *unconditional* reading of R3 Theorem L, not to Theorem L with (H1)–(H3).
- **Construction:**
  - **Domain and secondary.** All measurable models. L_i is the ordinary additive guidance loss with penalties (0, |g_i|, 2|g_i|, 4|g_i|).
  - **Primary.** Let Q = {g ∈ H : every coordinate is positive}, the unanimous problems. At every world the primary is the same:
    F(X) = μ{g ∈ Q : X gives bad or contradictory advice at g}.
    It is error-only: good advice and silence cost 0.
  - **Rankings.** World i is ranked by lex(F(X), L_i(X)).
- **Statement:**
  - Both levels are additive; the primary is weakly guiding and the secondary strictly guiding. So strict (G) and (IB) hold.
  - Every coherent precise B_p has F(B_p) = 0.
  - If F(X) > 0, replacing the erroneous unanimous advice by good advice strictly dominates X at every world.
  - If F(X) = 0, comparisons with the B_p reduce to the ordinary secondary comparisons. Uniqueness then gives exactly the ordinary undominated family {B_p}.
  - The section for X is all of Δ when F(X) > 0, and the ordinary additive closed section when F(X) = 0. So (S) holds with the ordinary selection, and competitiveness follows as in the additive case.
  - Equal profiles give equal secondary profiles, so secondary Bayes uniqueness gives (C). The all-model domain supplies (LF) at every target it covers, and (E).

  So this nonzero error-only primary is compatible with (LA), (S), (C), strict (G) and (IB). It violates R3's (H1), because its coherent vertex models pay zero primary loss everywhere.
- **Used for:** showing that (H1)–(H3) cannot be dropped from Theorem L.

---

## 8. What is and is not established

Adapted from the audit's suggested replacement summary.

**In plain terms.** Closed competitive choice, axiom (S), rules out several natural ways in which non-additive rankings might select more models than additive rankings can.
- In two worlds this gives a clean result for two broad classes:
  - rankings sandwiched by families of additive losses;
  - rankings that are lexicographic with two additive levels.

  For these, the set of undominated models is exactly the set an additive system would select.
- In three worlds, new geometric restrictions sharpen the obstruction to *prescribed* contamination constructions.
- Additive coverage of a *single* contamination target remains open, with several unresolved possibilities.
- Coverage by arbitrary ordinal rankings is also open.
- The results make rigidity a reasonable research conjecture. They do not show that full coverage fails under the accepted decomposable-domain axioms. Nor do they show that such a failure, if it exists, would extend to the accepted weakened guidance orders (Σ_T systems, the D_Δ exception).

**Established, refereed, possibly after repair.**
- **Additive systems on decomposable domains.**
  - The Bayes minimiser at each interior weighting is a.e. unique and coherent (R1 Lemma 1.4 = R2 Lemma U). The (S) selection itself is not unique (AUD-1).
  - No additive system selects two models with one credal set strictly inside the other, interior relative to aff Δ (R2 Thm N).
  - Pairwise pattern compatibility (R5 Thm PC).
  - Chart necessity conditions (R1 Thm 2.2(N)), and sufficiency under uniqueness at *every* prior (R1 Thm 2.2(S)). These are not an unconditional iff, because the boundary-tie gap remains.
- **Two worlds.** U_L is additively representable iff it has no strictly nested pair (R2 Thm R). No nesting holds for:
  - sandwiched systems of any cardinality (R5 Thm UN, with R8's step for weakly guiding unanimity families);
  - two-level lexicographic systems with additive levels (R7 Thm 1′₂).

  These are equalities of whole undominated families. They are not representations of the rankings, and they are stronger than coverage needs.
- **Any n, sandwiched systems.** No (Nest) or (AllPat) pair in U_L (R5 Thm UN, UN′). This is only a necessary, pairwise shadow of rigidity.
- **Lexicographic structure.**
  - Closed sections force lower semicontinuous, countable "staircases" of improvable primary levels (R2 Thm 7, R3 P1–P3, R7 Lemma 7′). Countability is necessary for (S), not sufficient.
  - Error-only primaries cannot give (S) **under (H1)–(H3)** (R3 Thm L). AUD-2 shows (H1) cannot be dropped.
  - On interior primary faces of an 𝓛₂ system, interior levels carry no improvable members (R9). Boundary faces can carry continua of them.
- **Three worlds, contamination.**
  - The prescribed diagonal-projective contamination (and belief-function) family cannot be the Bayes family on any open set of priors, on any decomposable domain, for any n ≥ 3 (R1 Thm 4.1). One target is not excluded.
  - Adjacency of accept and reject regions forces degenerate selected credal sets on the shared face (R4 Thm B). Under the extra continuity hypothesis (H1⁺) it forces precise ones (R4 Thm C).
  - The lex T1 system of R3 §5 has coherent Bayes models at every prior but fails (S).

**Conditional only.**
- No additive realisation of T1 with full-dimensional interior selections (R1 Thm 4.2, R4 Cor B2/C3). This depends on:
  - the unrefereed CPM-folder chain NOGO/PB/FA;
  - the extra hypotheses (H0) and (H1) (or (H1⁺)), which (LF) and measurability do not supply.
- The diagonal-projective "caps" picture (R4 Prop D, F). It needs σ to be injective or a local homeomorphism.
- R4 Prop G2 (conditional on PB/FA conclusions).

**Not established or withdrawn.**
- "Domain shape gives no gain" (R1).
- "Measurability and advice ranges add only a little" (originally phrased with "menus").
- "Avoidable exactly when" (R2).
- "Only diagonal-projective caps remain", and any claim that the T1 residual is exhaustive.
- "The staircase lives only at vertices and edge endpoints" (R7). Only the interior-face version holds.
- R4 Example E's "f ≡ 0". The correct statement is f ≤ 0, i.e. only the precise family.
- R3 Remark (ii)'s "completely F-free".

**Open (principal items).**
- **The single-target additive problem (BRIEF2).** Is there one additive decomposable-domain system with target-only (LF) that covers the interior contamination triangle T1, or a generic interior triangle T2, in n = 3? Advice that every evaluable model gives, away from the target boundary, and merely measurable penalties are both allowed.
- **Weaker reduction goal.** Is each target covered by an ordinal system also covered by some additive system with the required domain freedom?
- **Rigidity for arbitrary (IB) rankings.**
  - Conjecture 1 in n = 2 beyond sandwiched and 𝓛₂ systems: mixed sandwiched/𝓛₂ worlds, three or more lex levels, IRWAS/KPS-type orders.
  - Conjecture R_n in n ≥ 3.
- **Acceptance by every evaluable model** inside the target on general decomposable domains (R4 Remark B3).
- **Removal of (H1) / (H1⁺)** (Conjectures 4.3, 4.3′).
- **Non-injective precise regions** (Prop D).
- **T3, T4.**
- **Transfer to Σ_T systems.**
- **n > 3.** No reduction from n = 3 preserving advice ranges, null-set identification, (LF) and closed competitive choice is known.

---
## Appendix: status index

| Source | Item | Status |
|---|---|---|
| R1 | C1 (boundary Bayes models need not be coherent) | NOT-REFEREED (accepted by R6) |
| R1 | C2 (decomposable-domain form of lem:bayes-necessary(c)) | NOT-REFEREED (accepted by R6) |
| R1 | Lemma 1.1, 1.2, 1.3 | NOT-REFEREED |
| R1 | Lemma 1.4, 1.5 | REFEREED-CORRECT |
| R1 | Prop 2.1 (table of charts for each advice range, vertex property, converse) | NOT-REFEREED (sign facts confirmed in passing) |
| R1 | Thm 2.2 (N), (S) | REFEREED-CORRECT |
| R1 | Thm 2.2 (T) | REFEREED-REPAIRED (split into T-a, T-b) |
| R1 | Remark 2.3 | NOT-REFEREED |
| R1 | Prop 2.4, 2.5, 2.6, 2.7 | REFEREED-CORRECT (2.5: N shrunk; "charts unchanged" deleted) |
| R1 | "Domain shape gives no gain" | GAP (withdrawn) |
| R1 | Prop 2.8 | NOT-REFEREED |
| R1 | Prop 3.1, Thm 3.2 | REFEREED-CORRECT |
| R1 | Ex 3.3 | REFEREED-REPAIRED (β uses τ₋) |
| R1 | Ex 3.4 | REFEREED-CORRECT (convexity of W for n ≥ 3 open) |
| R1 | Lemma 3.5 | REFEREED-REPAIRED (dim K = n − 1) |
| R1 | Finite-seam regularisation | NOT-REFEREED |
| R1 | Thm 4.1 | REFEREED-CORRECT (excludes a prescribed family, not a target) |
| R1 | §4.2(c) plateaus | NOT-REFEREED |
| R1 | Thm 4.2 | CONDITIONAL (NOGO/PB/FA; (H0), (H1), (H2)) |
| R1 | Conjecture 4.3 | CONJECTURE |
| R2 | Fact 0 | REFEREED-CORRECT (citation) |
| R2 | Lemma 1, Lemma 2 | REFEREED-CORRECT |
| R2 | Fact (exchanges); pointwise Bayes | NOT-REFEREED |
| R2 | Lemma 3 | REFEREED-REPAIRED (hypotheses stated; all-model flag) |
| R2 | Prop 4, Lemma U | REFEREED-CORRECT |
| R2 | Thm N | REFEREED-REPAIRED (aff-Δ interior) |
| R2 | Prop N2, Prop P, Thm R | REFEREED-CORRECT |
| R2 | Prop 5, Thm 6, Thm 7, Prop 8 | REFEREED-CORRECT |
| R2 | "Avoidable exactly when" | GAP (necessity only) |
| R2 | Conjectures 1, 1′; Q1 for n ≥ 3 | CONJECTURE / OPEN (1′ for two levels now proved by R7) |
| R3 | §2.1 constant-level lemma | REFEREED-CORRECT |
| R3 | Cor 2.1a | REFEREED-REPAIRED (K ≠ Δ) |
| R3 | §2.2 and vector-additive remark; §2.4 | NOT-REFEREED |
| R3 | §2.3 | REFEREED-CORRECT |
| R3 | P1, P2, P3 | REFEREED-CORRECT |
| R3 | Thm L | REFEREED-CORRECT (only with (H1)–(H3); Step 3 wording repaired) |
| R3 | §4 Remark (ii) | GAP |
| R3 | §4 Remark (iii) | NOT-REFEREED |
| R3 | §5.2, §5.3, §5.4 | REFEREED-CORRECT |
| R3 | §6 (T3, T4) | open (remarks) |
| R4 | Thm A, Thm B, Cor B1 | REFEREED-CORRECT |
| R4 | Cor B2, Cor C3 | CONDITIONAL (NOGO/PB/FA) |
| R4 | Remark B3 | REFEREED-REPAIRED |
| R4 | Lemma S; (H1⁺) extension; Thm C; Lemma C2 | REFEREED-CORRECT (Thm C assumes (H1⁺)) |
| R4 | Prop D | GAP; injective version REFEREED-REPAIRED; "non-constant ⇒ injective" CONJECTURE |
| R4 | Prop F | CONDITIONAL (inherits Prop D's injectivity) |
| R4 | Prop G1 | REFEREED-CORRECT |
| R4 | Prop G2 | CONDITIONAL |
| R4 | §9 item 4 | REFEREED-CORRECT (context conditional) |
| R4 | Example E | FALSE-AS-STATED; corrected (f ≤ 0 ⇔ precise) REFEREED-REPAIRED |
| R4 | (K1), (K2), (K4) | REFEREED-CORRECT ((K4) all-model) |
| R4 | (K3) | REFEREED-REPAIRED |
| R4 | Conjecture 4.3′; CONJECTURE R4 | CONJECTURE |
| R5 | Lemma N1, Lemma TJ, sandwiched definition | REFEREED-CORRECT |
| R5 | Thm UN | REFEREED-REPAIRED (aff-Δ interior; weak-unanimity step) |
| R5 | Cor UN2 | REFEREED-CORRECT |
| R5 | Lemma X, Prop X2, Lemma 4.1, Prop 4.2, Ex 4.3, Lemma 4.4 | REFEREED-CORRECT |
| R5 | Thm PC, Thm UN′ | REFEREED-CORRECT |
| R5 | Thm R_n | REFEREED-REPAIRED (per-prior form; boundary-tie gap; not an unconditional iff) |
| R5 | Region-only claim; Conjecture R_n; n ≥ 3 lex conjecture; pairwise insufficiency | CONJECTURE |
| R7 | Class 𝓛₂ and standing facts; Lemma F; (F*) | REFEREED-CORRECT |
| R7 | Lemma A | REFEREED-REPAIRED (constant primaries) |
| R7 | Lemma SF, Cor SF-L, Lemma BWC, Lemma 7′ | REFEREED-CORRECT |
| R7 | Thm 1′₂ | REFEREED-REPAIRED (proof repairs only) |
| R7 | Cor 4.1, Cor 4.2 | REFEREED-CORRECT |
| R7 | Remark 3 / §5.1 | REFEREED-REPAIRED (face 𝔅_t, t ∈ (0, 1)) |
| R7 | §5.2, §5.3, §5.5 | REFEREED-CORRECT |
| R7 | §5.4 / §0 item 3 staircase claim | FALSE-AS-STATED; interior-face version proved by R9 |
| R7 | §5.6 structure sketch | NOT-REFEREED |
| R7 | §6 (m ≥ 3); Conjecture 1′_m | NOT-REFEREED sketch; CONJECTURE |
| Audit | Example AUD-1, Example AUD-2 | NOT-REFEREED (auditor's direct arguments; accepted in BRIEF2) |
