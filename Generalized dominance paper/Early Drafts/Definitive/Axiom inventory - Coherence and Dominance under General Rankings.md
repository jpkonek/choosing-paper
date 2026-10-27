# AX70L: Axiom inventory for "Coherence and Dominance under General Rankings" (LDG)

**Audited text:** `r69/Coherence and Dominance under General Rankings.tex` (670 lines). Numbering was checked against `r69/build/...aux` and the PDF text, and all three agree. "l.N" means line N of the .tex.

**Method.** Each item below was checked against the theorem statements and also against the proofs. A "uses" entry means the proof actually invokes the item. Where a statement assumes more than its proof uses, this is recorded.

**Status vocabulary.**
- **Definition:** names something and asserts nothing.
- **Assumed:** a hypothesis, standing or local.
- **Constructed:** an object built in the text.
- **Proved:** derived in the text.
- **Imported:** a result proved elsewhere.

**Scope vocabulary.**
- **World:** one relation ⪯_ω.
- **Ranking:** one L, all worlds.
- **Family:** a family 𝔏 of rankings.
- **Model space:** Ω, 𝓜, 𝒞, or background mathematics.

No new axioms are introduced. Everything listed occurs in the manuscript, or (for B4 and B5) is named in the binding guidance and shown here to be absent from the manuscript.

---

## 0. Verdict on the preliminary list (`Axioms_in_each_paper.md`, LDG part)

| # | Claim in preliminary list | Verdict | Correction |
|---|---|---|---|
| 0.1 | A: worlds and models are unstructured, ranking = domain + one relation per world, no property assumed, 𝒞 fixed in advance | Correct (l.58, l.99) | Add three things. M_L is nonempty. C_L is a name, not an assertion (l.99–103). The dominance notions are relative to one ranking (l.60). |
| 0.2 | B1 Closure under ties "Used in: Thm 3.2 (last claim), Thm 4.1(c), Prop 6.1(a), Prop 6.5(b)" | Incomplete | The operative use is **Lemma 2.4(b)**. All the listed uses go through it. Also used in: Thm 3.3 (last claim), Thm 4.6 (conclusion (c)), Cor 4.2 (via 4.1(c)), and Prop 6.5 (its "iff" claim, as one alternative, and its final claim). It is **proved** and then used in Prop 8.1, Thm 8.2, Prop 8.4 and Prop 8.6. It is proved in Prop 7.1, Prop 8.7 and Examples 3.4, 4.4, 4.5, 5.4. In Thms 3.2/3.3 it is stated in loss-profile form, and the proof (l.184) shows the equivalence. Besides "identifying the undominated models exactly", it is also what upgrades weak domination to **domination** for models outside C_L. |
| 0.3 | B2 "Preorder (reflexive and transitive). Used only in Prop 6.3 and Prop 6.5(c)" | Partly wrong | The proofs use **only transitivity**. Reflexivity is stated but never used (l.444; see B1). Transitivity is also used downstream through Prop 6.3: in the "iff" claim of Prop 6.5, in Prop 8.1, Prop 8.4 and the merely-proper paragraph of §8.1 (l.525). In addition, numerical transitivity of ≤ is used in the proof of the last claim of Thm 3.2 (l.184). |
| 0.4 | B3 "Completeness. Used only through loss rankings (Lemma 2.1 converse, Lemma 2.3)" | Correct | Add: it is used through Lemma 2.3 in Thm 3.2 and Thm 3.3, and hence in all of §8 except Prop 8.7. Thm 5.1 does **not** use it, because it argues numerically. |
| 0.5 | C Thm 3.2 hypotheses | Correct | Add the support relation explicitly: the Bayes prior π may differ from the index p, needs only supp π ⊆ supp p, and need not vary continuously (l.187). |
| 0.6 | C Thm 3.3 "(ii) on cofinally many finite sets ... continuous maps ... that make Bayes choices" | Correct but loose | Exact form: every finite set of worlds lies in a nonempty finite linked F with continuous σ_F: Δ_F → Θ, such that each c_{σ_F(p)} is a Bayes model for some prior π with supp π ⊆ supp p. |
| 0.7 | C Thm 4.1, Cor 4.2 | Correct | — |
| 0.8 | C Thm 4.6 "(a) local ⊆ global" | Loose | Exact form: θ_F(p) ∈ K_ω(m) whenever p ∈ A^F_ω(m), i.e. θ_F(A^F_ω(m)) ⊆ K_ω(m). |
| 0.9 | §5 "These use the hypotheses of Thm 3.3. Prop 5.3 adds usc of V ..." | Correct | Add: Prop 5.3 is for finite Ω under Thm 3.2's hypotheses. Thm 5.1 and Cor 5.2 never use the undominatedness or coherence of the c_θ (see §3, check 1). |
| 0.10 | C′ Prop 7.1 "Data: ... 'available to z' ..." | Wrong | "Available to z" is **defined** from the change assignment (l.478). It is not separate data. |
| 0.11 | C′ "Part (c) ... assumes neither" | Wrong as written | (c) **assumes both** guidance conditions ("Assume both conditions", l.488). It assumes neither side of the equivalence. Also, closure under ties follows from protection (b) alone, not from (c) (proof l.501). |
| 0.12 | C″ "Each ranking is closed under ties, or is a preorder" | Conflates two claims | "Closed under ties **or** transitive" suffices only for "undominated under no ranking ⇔ irrational". "Permissible = coherent" needs **closure under ties for every ranking** (l.467, l.470). The preorder alternative gives only "permissible = models tied with a coherent undominated model". |
| 0.13 | C″ Coherent admissibility "Every coherent model is an undominated coherent model of some ranking" | Correct | Add: by itself it gives "every coherent model is permissible" (l.470), with no dominance property needed. It is in fact equivalent to that statement (see A2). |
| 0.14 | C‴ Prop 8.1 "Finite losses or continuity give uniform dominance" | Incomplete | Uniform dominance **also** needs uniqueness of Bayes models ("If moreover", l.517). The proof uses "no incoherent model is a Bayes model" (l.520). |
| 0.15 | C‴ Prop 8.7 "coherent admissibility holds but dominance fails" | Misuse of term | What holds is undominatedness of every coherent credence under **this single loss** (C ⊆ C_L). That is coherent admissibility only for the one-member family {L}. See check 4. |
| 0.16 | D "The dominance property ... Proved, never assumed" | Overstated | It is never a **standing** assumption. It **is** a hypothesis of Prop 6.1(a), Prop 6.3, Prop 6.5 and Remark 4.7, all of which are conditional consequences. Add Cor 4.2 to the list of results that derive it. D also omits the other conclusions (D2–D4 below). |
| 0.17 | Cross-paper mismatch 1 (reflexivity) | Correct | Confirmed: application l.957 builds reflexivity and "a.e.-equal models are tied" into "ranking on U". |
| 0.18 | Cross-paper mismatch 2 ("dominance property") | Correct, and worse than stated | Application l.961 says "Conditions (2)–(5) are the dominance property". Its (2) global coherence and (5) incoherent-model dominance are, in substance, the hypotheses of **LDG Prop 6.1(b)**. LDG Example 6.2 shows these do **not** imply LDG's dominance property. So the shared name labels two logically different properties. |
| 0.19 | Missing from the list | — | Lemmas 2.1–2.4, 3.1, 8.3. All examples and remarks. Mathematical background (A4). The three-model and finite-chain conditions, which are **absent** from LDG (B4, B5). |

---

## 1. Reader-facing inventory

### A. General framework and substantive assumptions

#### A0. Definitions (these assert nothing)

| ID | Name | Exact statement (l.) | Plain English | Scope | Status |
|---|---|---|---|---|---|
| A0.1 | Worlds | "Let Ω be a nonempty set of *worlds* ... Neither carries any structure." (l.58) | Any nonempty set of possibilities. | Model space | Definition |
| A0.2 | Models | "𝓜 a nonempty set of *models*." (l.58) | Any nonempty set of candidate opinions, forecasts, etc. | Model space | Definition |
| A0.3 | Ranking | "A *ranking* L consists of a nonempty set 𝓜_L ⊆ 𝓜, its *evaluation domain* ... and for each world ω a binary relation ⪯_ω on 𝓜_L ... We assume no property of these relations: they need not be reflexive, transitive or complete." (l.58) | At each world, some pairs of evaluable models are judged "at least as good as". Nothing else is assumed. | Ranking (one relation per world) | Definition |
| A0.4 | Dominance notions | Weak dominance (c ⪯_ω m at every world); tied at every world; dominance (weak dominance, not tied); strict dominance (c ≺_ω m at every world); U_L; the same notions "on S"; "*competitive on S*: every model m has some ω ∈ S with c ⪯_ω m" (l.61–67) | Standard dominance vocabulary, relative to one ranking. | Ranking | Definition |
| A0.5 | Coherent class | "The class 𝒞 ⊆ 𝓜 of *coherent* models is given in advance, independently of the rankings." (l.99) | Which models count as coherent is fixed before any ranking is chosen. | Model space | Definition (datum) |
| A0.6 | Undominated coherent models of L | "𝒞_L := {c ∈ 𝒞 ∩ 𝓜_L : no m ∈ 𝓜_L dominates c}. So 𝒞_L ⊆ U_L by definition. We do not assume that incoherent models are dominated." (l.100–103) | A **name** for a subclass, equal to 𝒞 ∩ U_L. It asserts neither that every undominated model is coherent nor that every coherent model is undominated. | Ranking | Definition |
| A0.7 | Loss ranking; uniform dominance | "A loss L: 𝓜_L × Ω → [0,∞] generates the ranking with m ⪯_ω m′ iff L(m,ω) ≤ L(m′,ω) ... Such a loss ranking is a preorder ranking with complete relations." Uniform dominance: L(c,·) finite and L(c,ω)+ε ≤ L(m,ω) for all ω. (l.76) | The special case where performance is a number. Its relations are automatically reflexive, transitive and complete. | Ranking | Definition. The order properties are immediate. |
| A0.8 | Priors, Bayes models, lsc | Δ_F, supp, "charges", π·L(m) summed over supp π only, V(π) := inf_{m∈𝓜_L} π·L(m), Bayes model, lower semicontinuity (l.78–82). Linked sets (l.241, l.330). | The probabilistic vocabulary for loss rankings. A Bayes model is optimal against **all** of 𝓜_L. | Ranking (loss) | Definition |
| A0.9 | Family; dominance principle | "Let 𝔏 be a family of rankings ... A model is *irrational* if every ranking in 𝔏 that evaluates it has an undominated model that dominates it. A model is *rationally permissible* if it is undominated under some ranking in 𝔏." (l.453) | The normative vocabulary. Irrational means beaten everywhere it is assessed. Permissible means unbeaten somewhere. | Family | Definition |

#### A1. Evaluability
- **Statement (l.455):** "every model is evaluated by some ranking in 𝔏." Formally, 𝓜 = ⋃_{L∈𝔏} 𝓜_L.
- **Plain English:** No model escapes assessment altogether.
- **Scope:** family.
- **Status:** assumed (stated as a condition on the family).
- **Required by:** **no proof**. The text says so at l.458. It only prevents a model that no ranking evaluates from counting as "irrational" vacuously. Nevertheless the closing sentence after Prop 6.5 (l.472) lists it among the premises (see revision R6).

#### A2. Coherent admissibility
- **Statement (l.456):** "every coherent model is an undominated coherent model of some ranking in 𝔏." Formally, 𝒞 ⊆ ⋃_{L∈𝔏} 𝒞_L.
- **Plain English:** Every coherent model survives under **at least one** reasonable way of assessing performance.
  - It does **not** require every coherent model to be undominated under **every** ranking.
  - It does **not** require any single ranking to leave all coherent models undominated.
  - It implies that every coherent model is evaluable by some ranking.
- **Scope:** family.
- **Status:** assumed. It cannot be derived from properties of individual rankings. By definition it is equivalent to "every coherent model is permissible": if c ∈ 𝒞 is undominated under L then c ∈ 𝒞 ∩ U_L = 𝒞_L. This follows immediately from A0.6 and A0.9 and is not a new claim.
- **Required by:** Prop 6.5, last sentence only ("With coherent admissibility ...", l.467; proof l.470).
  - The half "every coherent model is permissible" uses A2 **alone**, with no dominance property and no tie condition.
  - The half "permissible ⊆ coherent" does not use A2 at all. It uses D1 and A3 for every ranking.
- **Not to be confused with** per-ranking full admissibility (D5: every coherent model in 𝓜_L is undominated under **this** L). The applications prove D5 (l.513). It is stronger than A2 for any family containing L. See check 4.

#### A3. Closure under all-world ties
- **Statement (l.109):** "L is *closed under ties* if a model tied at every world with an undominated coherent model of L is itself an undominated coherent model of L."
  - **Loss-profile form A3′ (Thm 3.2, l.181):** "every model with the same loss profile as an undominated coherent model is coherent". The proof (l.184) shows A3′ ⇔ A3 for loss rankings, using numerical transitivity.
- **Plain English:** If a model does exactly as well as some undominated coherent model at every world, in both directions, then it too is coherent and undominated. The ranking cannot register any difference between them, so nothing incoherent can hide behind such a tie.
- **Scope:** one ranking, relative to 𝒞.
- **Status:** assumed wherever it is invoked. It is proved for:
  - the constructed rankings (Prop 7.1);
  - all the §8 examples under uniqueness or strictness hypotheses: Prop 8.1, Thm 8.2, Prop 8.4, Prop 8.6, Prop 8.7;
  - Examples 3.4, 4.4, 4.5 and 5.4.
- **Required by:**
  - Lemma 2.4(b), which is the only place it enters a proof directly.
  - Through Lemma 2.4(b): Thm 3.2 and Thm 3.3 (last claims), Thm 4.1(c), Cor 4.2, Thm 4.6 ("conclusion (c)"), Prop 6.1(a) (second sentence), and Prop 6.5(b).
  - The "iff" claim of Prop 6.5, as one alternative (the other is transitivity).
  - The final claim of Prop 6.5, "permissible = coherent", for **every** ranking in 𝔏.
- **What it does and does not do:**
  - It is not needed to obtain weak dominators (D1).
  - It is used to pass from D1 to exact identification U_L = 𝒞_L (D3), and to upgrade "weakly dominated" to "dominated" for models outside 𝒞_L (D2).
  - It is sufficient but **not necessary** for D3 in general. In Example 6.4 (l.448), U_L = 𝒞_L = {c} and the dominance property holds, yet m is tied with c and m ∉ 𝒞_L.
  - For transitive rankings with the dominance property it is also necessary for D3. This is immediate from Prop 6.3: U_L is the set of models tied with 𝒞_L.

#### A4. Mathematical background (imported, not axioms about rankings)

| Item | Where | Status |
|---|---|---|
| Brouwer fixed-point theorem | Lemma 3.1 (l.131) | Imported |
| Compactness via the finite intersection property; no separation axiom ("no separation property is needed", l.231) | Thms 3.3, 4.6, 5.1; Cor 5.2; Prop 5.3; Rem 4.7 | Imported |
| Compactness of the finitely additive probabilities in the weak-star topology, i.e. a closed subset of a product of intervals (Tychonoff) | §8.2 (l.528), §8.3 (l.550), Prop 8.6 | Imported |
| Axiom of choice; free ultrafilter | Rem 4.7 (l.348), Prop 8.6 (l.612) | Imported |
| Connectedness of Δ_F | Ex 4.4 (l.310), Ex 4.5 (l.320) | Stated (l.78) |
| Fatou's lemma | Prop 8.6 (l.616) | Imported |
| Nielsen, App. A Prop. 1 and Lemmas 1, 3 | Thm 8.2 (l.534, l.544) | Imported |
| SSK09 Lemma 5 | §8.1 merely-proper paragraph (l.525) | Imported |

---

### B. Ordering properties

General rule (l.58): **none of these is assumed in the general framework.** The general relational results are:
- Lemma 2.4, Lemma 3.1, Thm 4.1, Cor 4.2, Thm 4.6, Prop 6.1, Remarks 4.7–4.8, and Prop 6.5(a),(b).

They use none of B1–B5 (verified against each proof). §9 (l.650) says so for most of them. Prop 6.5(a),(b) and Rem 4.7–4.8 are not mentioned there.

| ID | Property | Exact statement | Scope | Assumed in | Proved for | Actually used by a proof |
|---|---|---|---|---|---|---|
| B1 | Reflexivity | m ⪯_ω m | World | Part of "preorder ranking" (l.58), so nominally assumed in **Prop 6.3** and **Prop 6.5(c)** | Loss rankings (l.76); the constructed ranking, Prop 7.1(a) (l.486, l.497); Examples 4.4, 6.2, 6.4 by stipulation | **Only** in Prop 7.1(b) ("c is tied with itself by reflexivity", l.499) and 7.1(c) ("weakly dominates itself", l.501), where it has just been proved. Also in example verifications: Ex 4.4 and Rem 4.8 (each model weakly dominates itself, so the dominance property holds). **Not used** in Prop 6.3/6.5(c): l.444 uses transitivity only. Membership of each c ∈ 𝒞_L in the set "tied with 𝒞_L" comes from Prop 6.1(a), not from reflexivity. |
| B2 | Completeness | m ⪯_ω m′ or m′ ⪯_ω m | World | Lemma 2.1 (converse direction, l.70) | Loss rankings (l.76) | Lemma 2.1 converse, and from there Lemma 2.3. Then Thm 3.2, Thm 3.3 and every §8 result built on them (8.1, 8.2, 8.4, 8.6, the §8.1 paragraph). **Not** in Thm 5.1 or Cor 5.2, which argue numerically. |
| B3 | Transitivity | m ⪯_ω m′ ⪯_ω m″ ⇒ m ⪯_ω m″ | World | Prop 6.3 and Prop 6.5(c), via "preorder ranking"; the "iff" claim of Prop 6.5 (alternative to A3) | Loss rankings (l.76); Ex 6.2 by stipulation. **Fails** for Ex 4.4 (l.304), Ex 6.4 (l.448), and in general for the constructed ranking (l.506) | Prop 6.3 (l.444, twice), hence Prop 6.5(c) and the "iff" claim of 6.5. Then Prop 8.1, Prop 8.4 and the §8.1 paragraph through 6.3. Numerical transitivity of ≤ in the reduction A3′ ⇔ A3 in Thm 3.2 (l.184): "a dominator of it would dominate c". |
| B4 | Three-model no-reversal | Not defined in LDG under this or any other name. Read as the k = 2 case of B5: no A ⪯_ω B ⪯_ω C with C ≺_ω A. (k = 1 is vacuous by the definition of ≺.) | World | **Nowhere** | Implied for the construction by Prop 7.1(a), but not stated there | **Nowhere.** No LDG proof uses it. |
| B5 | Finite-chain consistency (the companion paper's "acyclicity") | No chain A_0 ⪯_ω A_1 ⪯_ω … ⪯_ω A_k with A_k ≺_ω A_0 (companion l.968; **not** stated in LDG) | World | **Nowhere** | Implied for the construction by Prop 7.1(a) ("every cycle ... consists of equal models", l.486), but not stated | **Nowhere.** No LDG proof uses it. |
| B6 | Construction order properties | (i) m ⪯_ω m′, m ≠ m′ ⇒ φ_ω(m) > φ_ω(m′). (ii) Every cycle consists of equal models. (iii) Distinct models are never tied. (Prop 7.1(a), l.486) | World | Nowhere. l.506 says explicitly that these are "properties of this construction, not requirements of the general argument" | Prop 7.1(a), under C7.1 | (i) and (iii) are used in Prop 7.1(c) (l.501). **(ii) is stated and never used** in LDG. |
| B7 | Invariance under increasing rescaling (not an ordering property; recorded because §9 relies on it) | Lemma 2.2 (l.84) | Ranking | — | Proved (Lemma 2.2) | Ex 4.5 (l.318). The scope remark in §9 (l.650). |

**Summary for B.** Completeness and transitivity are imported only through loss rankings (Lemma 2.3 and Prop 6.3). Reflexivity is never used except in Prop 7.1, where it is proved. B4 and B5 appear nowhere in LDG. LDG proves a strictly stronger cycle property (B6(ii)) for its construction and then never uses it.

---

### C. Alternative sufficient hypotheses (and the construction's premises)

**These are alternatives, not cumulative axioms.** Each package (C1–C5) is a self-contained sufficient condition for the dominance property (D1) of **one** ranking. None is required of every permissible ranking. None is implied by D1 (Remark 4.8, l.357). The construction (C7) is a separate route and need not meet any of C1–C5 (l.506).

**C0. The common ingredient: assigned models are undominated coherent models of L.**
- Every package C1–C5 requires each assigned model c_p or c_θ to lie in 𝒞_L.
- This is the "other half" of the argument (l.46). It is the only dominance notion that appears in the hypotheses.
- **Verified against the proofs:** the mechanism (KKM plus closed sets, plus compactness where needed) proves "every model is weakly dominated by an assigned model" **without using C0**. The proofs at l.184, 243, 279 and 340 never use that the assigned model is coherent or undominated.
- C0 enters only at the last step. Weak domination by an assigned model becomes the dominance property, and Lemma 2.4 is applied to members of 𝒞_L.
- Thm 5.1 and Cor 5.2 never use C0 at all.
- Scope: one ranking. Status: assumed (for the applications, proved via D5).

#### C1. The original closed-selection condition (S): Corollary 4.2
- **Statement (l.289):** "Let Ω be finite. Suppose that to each prior p is assigned an undominated coherent model c_p, competitive on supp p, such that each set {p : c_p ⪯_ω m} is closed."
- **Components:**
  - (S1) assignment p ↦ c_p ∈ 𝒞_L (C0);
  - (S2) support-wise defence: for every rival m some ω ∈ supp p has c_p ⪯_ω m;
  - (S3) every **full** fixed-rival comparison set {p : c_p ⪯_ω m} is closed in Δ.
- **Plain English:** Each prior gets one undominated coherent model. Against any rival, that model does at least as well at some world the prior takes seriously. For a fixed rival and world, the priors whose model does at least as well there form a closed set.
- **Scope:** one ranking, Ω finite.
- **Status:** assumed (local hypothesis).
- **Yields:** D1, D3w, and D2/D3 with A3 (the conclusions of Thm 4.1).
- **Required by:** nothing downstream except as a special case.
  - Thm 3.2 "is the case of Corollary 4.2 for loss rankings" (l.295).
  - Ex 4.5 uses C1 to show it holds where C4 fails.

#### C2. The genuine finite-world weakening: Theorem 4.1
- **Statement (l.266–270):** Ω finite. To each prior p is assigned c_p ∈ 𝒞_L, "the same model whichever rival it is compared with". To each model m and world ω is assigned a closed A_ω(m) ⊆ Δ with:
  - (i) **guarantee:** c_p ⪯_ω m for every p ∈ A_ω(m);
  - (ii) **serving condition:** for every m, every p lies in A_ω(m) for some ω that p charges.
- **Plain English:** It suffices that **closed subsets** of the full comparison sets still serve every prior at a world it charges.
  - The assigned model may make further comparisons whose prior-sets are not closed, and it may jump.
  - One assigned model per prior must serve against **all** rivals at once. If the assignment may depend on the rival, the condition collapses into D1 (Rem 4.7(i)).
- **Scope:** one ranking, Ω finite.
- **Status:** assumed (local hypothesis).
- **Relation to C1:** C1 ⇒ C2 by taking A_ω(m) to be the full set (l.292). C2 does not imply C1 (Ex 4.4: C2 holds, C1 fails for every assignment).
- **Yields:** (a) D1⁺ and D1; (b) D3w; (c) with A3, D2 and D3.

#### C3. The local infinite-world conditions: Theorem 4.6
- **Statement (l.328–334):** Ω arbitrary.
  1. A compact space Θ and c_θ ∈ 𝒞_L for each θ. For each ω and m, a **closed** K_ω(m) ⊆ Θ with c_θ ⪯_ω m for all θ ∈ K_ω(m).
  2. Every finite set of worlds lies in a nonempty finite **linked** F. For each linked F there is a map θ_F: Δ_F → Θ, "not necessarily continuous and the same for every rival", and closed A^F_ω(m) ⊆ Δ_F (ω ∈ F) with:
     - (a) **local guarantees are global guarantees:** θ_F(p) ∈ K_ω(m) whenever p ∈ A^F_ω(m);
     - (b) **serving condition:** every p ∈ Δ_F lies in A^F_ω(m) for some ω that p charges.
- **How the finite-world guarantees are linked.** On each linked F:
  - C2-type data, with c_p := c_{θ_F(p)}, give a prior in every A^F_ω(m).
  - Condition 2(a) transports that prior to a point of ⋂_{ω∈F} K_ω(m) ⊆ Θ.
  - Cofinality of the linked sets gives the finite intersection property for {K_ω(m)}_{ω∈Ω}.
  - Compactness of Θ then gives one θ* that works at every world (proof l.340).
  - The link is therefore three things together: **one** compact Θ, **closed** global guarantee sets K_ω(m) in Θ, and the transport condition 2(a).
- **Scope:** one ranking.
- **Status:** assumed (local hypothesis).
- **Relations:**
  - On finite Ω, C3 ⇔ C2 (l.343).
  - C5 is the case K_ω(m) = {θ : L(c_θ,ω) ≤ L(m,ω)}, θ_F = σ_F (l.343).
  - Requiring closed **full** comparison sets {θ : c_θ ⪯_ω m} is strictly stronger (Rem 4.9).
  - Dropping the compact link breaks the theorem (Ex 3.4 and l.360).
- **Yields:** D1⁺, D1, D3w, and D2/D3 with A3.

#### C4. Loss-based conditions, finite worlds: Theorem 3.2
- **Statement (l.176–180):** Ω finite; ranking generated by a loss L: 𝓜_L × Ω → [0,∞]. To each p ∈ Δ is assigned c_p ∈ 𝒞_L such that:
  - (i) **Bayes choice:** "c_p is a Bayes model for some prior whose support lies within supp p";
  - (ii) **lower semicontinuity:** "for each world ω, the loss L(c_p,ω) is a lower semicontinuous function of p on Δ."
- **Support relation (exact):** the index is p ∈ Δ. The Bayes prior π is any prior with supp π ⊆ supp p. π may differ from p and need not depend continuously on it (l.187). Ex 8.5 shows this freedom is used. The assignment p ↦ c_p need not be continuous. The Bayes property is required only of the assigned models (l.187).
- **Optional extra hypothesis A3′** (l.181): this gives D2 and D3.
- **Scope:** one loss ranking, Ω finite.
- **Status:** assumed (local hypothesis).
- **Mechanism:** (i) gives S2 via Lemma 2.3, which uses B2. (ii) gives S3. So C4 ⇒ C1 (l.295).
- **Relation:** C1 does not imply C4. In Ex 4.5, C1 holds for the rescaled loss and C4 fails for it.

#### C5. Loss-based conditions, arbitrary worlds: Theorem 3.3
- **Statement (l.234–238):** Ω arbitrary; loss ranking. A compact space Θ and c_θ ∈ 𝒞_L such that:
  - (i) **lower semicontinuity:** for each ω, θ ↦ L(c_θ,ω) is lsc on Θ;
  - (ii) **continuous Bayes choices on finite sets of worlds:** every finite set of worlds lies in a nonempty finite F (linked) with a **continuous** σ_F: Δ_F → Θ such that each c_{σ_F(p)} is a Bayes model for some prior with support within supp p.
- **Support relation:** as in C4, with p ∈ Δ_F as the index and the Bayes prior supported in supp p.
- **Optional A3′** (l.239): gives D2 and D3.
- **Scope:** one loss ranking.
- **Status:** assumed (local hypothesis).
- **Relations:** C5 ⇒ C3 (l.343). On finite Ω, C5 ⇔ C4 (l.246). Without compactness the conclusion fails even for a complete transitive ranking (Ex 3.4).

#### C6. Refinement hypotheses for margins and strict dominance (§5)
- Thm 5.1 and Cor 5.2 assume C5.
  - Their proofs use compactness, lsc, continuity of σ_F, and Bayes choice with the support relation.
  - They do **not** use C0 or B2.
- **Prop 5.3** (l.393–396): Ω finite; C4 (as C5 with Θ := Δ, σ_Ω := id); and "**V is upper semicontinuous on Δ**". Two sufficient conditions for usc of V are given:
  - (a) "the assigned models have finite losses";
  - (b) "V is finite, each c_p is a Bayes model for p itself, and each p ↦ L(c_p,ω) is continuous".
  - Its last sentence adds "every Bayes model is an undominated coherent model".
- **Scope:** one loss ranking.
- **Status:** assumed (local).
- **Sharpness:** Ex 5.4 shows that without (a) or (b) the equivalence can fail.

#### C7. The construction proposition's own premises: Proposition 7.1
This is a **different route** to D1. It "need not satisfy the selection hypotheses" (l.506: "nothing requires a ranking built in this way to meet their hypotheses").

- **C7.0 Data** (l.476–479), scope: model space plus one world each:
  - a change for each ordered pair, with the change from m′ to m null only if m = m′;
  - for each ω, a set of changes *guided at ω* containing the null change;
  - a **real-valued** score φ_ω.
  - "Available to z" is **defined** from the change assignment. It is not additional data.
- **Defining rule** (l.481): m ⪯_ω m′ iff the change from m′ to m is guided at ω, **or** it is available to no coherent model and φ_ω(m) > φ_ω(m′).
  - Status: constructed.
  - This rule is where coherence enters the ranking, through the clause "available to no coherent model". It is a feature of the construction, not a general axiom (see check 2).
- **C7.1 Guided changes improve the score** (l.486): every non-null change guided at ω strictly raises φ_ω. Scope: world. Status: assumed (local). Used in (a) and (c).
- **C7.2 Guidance protects coherent models** (l.487): for every coherent c, the only model reached from c by a change guided at every world is c. Scope: ranking (all worlds), relative to 𝒞. Status: assumed (local). Used in (b) and (c).
- **(c)(ii) Existence of improvements** (l.491): every incoherent m has a coherent c such that the change from m to c is guided at every world, or available to no coherent model and score-raising at every world.
  - This is **not** a premise. It is one side of an equivalence and "must then be proved" (l.504).
  - The companion paper proves it (l.510).

#### C8. Application-level hypotheses (§8): ways of verifying C4/C5 for particular losses
These are not axioms of the general theory. Each is local to one result.

| Result | Setting assumptions | Hypotheses | Which conclusion needs which |
|---|---|---|---|
| Prop 8.1 (l.517) | Ω finite; 𝒞 = Δ ⊆ 𝓜_L | lsc of p ↦ L(p,ω) on Δ; **strict propriety relative to 𝓜_L**: p is Bayes for p, and every Bayes model for p has profile L(p) | Base claims: lsc plus strict propriety. "Exactly coherent" and "dominated": add **uniqueness** of Bayes models. Uniform dominance: uniqueness **and** (finite losses **or** continuity). |
| §8.1 event forecasts (l.525) | Finitely many events; continuous score s | Strictly proper s ⇒ Predd et al. Merely proper s_i with finiteness and normalisation ⇒ SSK conclusion | Uses Thm 3.2, Prop 5.3(b), and (merely proper) Prop 6.3 plus SSK09 Lemma 5 |
| Thm 8.2 (l.531) | Ω arbitrary; 𝓜_L = [0,1]^{2^Ω}; 𝒞 = finitely additive probabilities | **Quasi-strict propriety**; lsc of q ↦ L(q,ω) on 𝒞 | Uniform dominance: add "each probability has bounded loss across worlds" |
| Prop 8.4 (l.580) | Finite partition into nonempty cells; S_j: X_j × F_j → [0,∞) with each S_j(x,·) bounded (l.570) | **Block propriety**; lsc along coherent systems on Γ | Exact identification: add unique minimisers |
| Prop 8.6 (l.609) | A specific Brier example on ℕ | None beyond the specification | — |
| Prop 8.7 (l.627) | A specific counterexample | None beyond the specification | Shows that truth-directedness plus D5 for this single loss do not give D1 |

---

### D. Conclusions (kept out of the axiom list)

| ID | Conclusion | Exact form | Scope | What yields it (exactly) |
|---|---|---|---|---|
| D1 | **Dominance property** | "every evaluable model is weakly dominated by an undominated coherent model of L" (l.105) | Ranking | Any **one** of C1, C2, C3, C4, C5 (each including C0). Or C7.1 + C7.2 + the improvements (c)(ii) (Prop 7.1(c)). Never A1 or A2. Never a standing assumption. |
| D1⁺ | Weak domination by an assigned model | "every model is weakly dominated by one of the assigned models" (Thms 3.2, 3.3, 4.1(a), 4.6) | Ranking | The mechanism parts of C1–C5 **without C0** (see check 1). Adding C0 gives D1. |
| D2 | Undominated coherent **dominator** for every model outside 𝒞_L (so in particular for every incoherent model) | "every other model is dominated by an undominated coherent model" (Thm 3.2 l.181; Thm 4.1(c); Prop 6.1(a)) | Ranking | D1 + A3 (Lemma 2.4(b)). Alternatively D1 + B3 gives it for every model not tied with a member of 𝒞_L (Prop 6.3). |
| D2s | Strict or uniform domination | Prop 5.3; Prop 7.1(c); Thm 8.2; Prop 8.6; Prop 8.1 | Ranking | Strict: C7.1 + C7.2 + D1 (Prop 7.1(c)). Strict, and then uniform, domination of every model that is a Bayes model for no prior: C4 + C6 (Prop 5.3). Uniform: C5 + Thm 5.1 + bounded losses or margin (Thm 8.2, Prop 8.6). |
| D3 | **Every undominated model is coherent** (global coherence), equivalently U_L = 𝒞_L | "the undominated models are exactly the undominated coherent ones" | Ranking | D1 + A3 (Thm 4.1(c), Prop 6.1(a)). D1 alone gives only D3w. A3 is not necessary for D3 in general (Ex 6.4), but it is necessary for transitive rankings (immediate from Prop 6.3). |
| D3w | Every undominated model is tied at every world with a member of 𝒞_L | Thm 4.1(b); Prop 6.1(a); Prop 6.5(a) | Ranking | D1 alone (Lemma 2.4(a)) |
| D3t | U_L = models tied at every world with a member of 𝒞_L | Prop 6.3 | Ranking | D1 + B3. Reflexivity is not used. |
| D4 | **Permissible models are exactly the coherent ones** | Prop 6.5, last clause (l.467) | Family | D1 for **every** L ∈ 𝔏, + A3 for **every** L ∈ 𝔏, + A2. Not A1. |
| D4a | Every coherent model is permissible | Prop 6.5 (l.467, l.470) | Family | A2 **alone** (it is equivalent to A2) |
| D4b | Undominated under no ranking ⇔ irrational | Prop 6.5 (l.467) | Family | D1 for every L, + (A3 or B3) for every L |
| D4c | Every incoherent model is irrational | l.472 | Family | D4 + D4b. A1 is not needed: an unevaluated model is irrational vacuously. |
| D5 | Per-ranking full admissibility: every coherent model in 𝓜_L is undominated under L (𝒞 ∩ 𝓜_L ⊆ 𝒞_L) | Prop 7.1(b); first step of each §8 proof (l.513) | Ranking | Proved case by case: C7.2 + defining rule; propriety-type hypotheses (C8). It supplies C0 and, for any family containing L, the part of A2 for 𝒞 ∩ 𝓜_L. |
| D6 | Numerical refinements | Thm 5.1 (margin characterisation); Cor 5.2 (Bayes models exist among the c_θ); Prop 5.3 (strictly dominated ⇔ Bayes for no prior) | Ranking (loss) | C5 (5.1, 5.2); C4 + C6 (5.3) |

A further logical relation among the conclusions, proved in the text: D1 is strictly stronger than D3 combined with "every incoherent model is dominated by an undominated model". Those two are the hypotheses of Prop 6.1(b), and Ex 6.2 shows they do not imply D1. The coherent models a_n there have no weak dominator in 𝒞_L.

---

## 2. Internal dependency table

Columns:
- **Uses (items):** inventory IDs actually invoked in the proof.
- **Uses (results):** earlier numbered results invoked.
- **Check:** discrepancies between the statement and the proof.

| Result | Role | Uses (items) | Uses (results) | Check against proof |
|---|---|---|---|---|
| Lemma 2.1 (l.69) | Competitive ⇒ not strictly dominated; converse | A0.4; B2 (converse only) | — | OK. The forward direction is never used later. |
| Lemma 2.2 (l.84) | Rescaling invariance | A0.7 | — | OK. Used in Ex 4.5 and §9. |
| Lemma 2.3 (l.91) | Bayes model is competitive on S ⊇ supp π | A0.7, A0.8; B2 | Lemma 2.1 (converse) | OK. Bayes is relative to all of 𝓜_L. |
| Lemma 2.4 (l.111) | (a) undominated + weakly dominated by c ⇒ tied; (b) A3 + m ∉ 𝒞_L ⇒ c dominates m | A0.4, A0.6; A3 (b only) | — | (a) uses neither c ∈ 𝒞_L nor any order property. (b) uses A3. No order property. OK. |
| Lemma 3.1 (l.127) | KKM variant | A4 (Brouwer) | — | Pure topology. OK. |
| Thm 3.2 (l.175) | D1⁺, D1; with A3′, D2 and D3 | C4 (incl. C0); A3′ ⇔ A3; B2 via 2.3; B3 (numerical, in A3′ ⇔ A3) | Lemma 2.3, 3.1, 2.4(a)(b) | D1⁺ does not use C0. Otherwise OK. |
| Thm 3.3 (l.233) | D1⁺, D1; with A3′, D2 and D3 | C5 (incl. C0); A4 (FIP); B2 via 2.3; A3′ | Lemma 2.3, 3.1; "as in Thm 3.2" for the last claim | D1⁺ does not use C0. OK. |
| Ex 3.4 (l.250) | Compactness cannot be dropped from C5/C3 | Loss ranking (B1–B3 hold); A3 verified | Thm 3.3 (non-applicability) | Verified: all e_n undominated; x undominated and incoherent; bounded variant with 3 − 1/n correct. |
| Thm 4.1 (l.265) | (a) D1⁺, D1; (b) D3w; (c) with A3, D2 and D3 | C2 (incl. C0); A3 for (c) | Lemma 3.1, 2.4(a)(b) | No order property, as l.282 claims. (a) does not use C0. OK. |
| Cor 4.2 (l.288) | (S) ⇒ conclusions of 4.1 | C1 | Thm 4.1 | OK. |
| Ex 4.3 (l.297) | Serving cannot be weakened to "not strictly dominated on supp p" | Incomplete relation | — | OK. |
| Ex 4.4 (l.303) | C2 holds, C1 fails for every assignment | B1 holds, B3 fails; A3 verified | Thm 4.1, Cor 4.2; connectedness of Δ | All guarantees, serving cases and the Cor 4.2 contradiction verified. OK. |
| Ex 4.5 (l.315) | C1 holds where C4 fails; randomised CCT does not settle the question | Loss ranking; A3 verified | Lemma 2.2, Cor 4.2, Thm 3.2 (non-applicability) | OK. |
| Thm 4.6 (l.326) | D1⁺, D1; D3w; with A3, D2 and D3 | C3 (incl. C0); A4 (FIP); A3 for (c) | Lemma 3.1, 2.4 | No order property. D1⁺ does not use C0. OK. |
| Rem 4.7 (l.347) | Rival-dependent assignment, and abstract compactness, are each ⇔ D1 | **D1 as hypothesis** (deliberately); A4 (choice) | Thm 4.6 (proof technique) | Legitimate. It assumes D1 in order to show the collapse. |
| Rem 4.8 (l.356) | C2/C3 are not implied by D1 | Loss ranking (B1 used: "trivially") | — | Verified for both theorems. OK. |
| l.360 (unnumbered) | Finite guarantees without a compact link do not suffice | — | Thm 4.6, Ex 3.4 | The conclusion is about the theorem's hypotheses. The heading is phrased as a necessity claim (R4). |
| Rem 4.9 (l.362) | Closed full comparison sets are stronger than C3 | — | Thm 4.6 (conclusion), Ex 4.4, reduction l.343 | Verified. OK. |
| Thm 5.1 (l.371) | D6 margin characterisation | C5 **minus C0**; A4 | Lemma 3.1; Thm 3.3 (FIP step) | Does not use C0, B2 or Lemma 2.3. OK. |
| Cor 5.2 (l.385) | D6 Bayes existence | C5 minus C0; A4 | Thm 3.3 (D1⁺) | Does not use C0. OK. |
| Prop 5.3 (l.392) | D6 strict ⇔ Bayes for no prior; D2s | C4 + C6; C0 only in the last sentence (as "every Bayes model ∈ 𝒞_L") | Thm 5.1; Thm 3.2 (case (a)) | OK. |
| Ex 5.4 (l.407) | Sharpness of C6 | A3 verified | Thm 3.2 | OK. |
| Prop 6.1 (l.420) | (a) D1 ⇒ D3w; with A3, D3 and D2. (b) D3 + incoherent-dominated ⇒ U_L = 𝒞_L and weak domination of incoherent models | **D1 (hypothesis, (a))**; A3 ((a), second sentence); (b) hypotheses are conclusion-type | Lemma 2.4 | No order property. OK. |
| Ex 6.2 (l.433) | D1 is strictly stronger than the identification | B1, B3 by stipulation | Prop 6.1(b) | OK. |
| Prop 6.3 (l.440) | D1 + transitivity ⇒ D3t, D2 (for models not tied) | **D1 (hypothesis)**; **B3 only**. B1 is stated but unused. | Prop 6.1(a) | **Statement assumes "preorder"; the proof uses only transitivity** (R5). |
| Ex 6.4 (l.447) | Without B3, D3t fails | B1 holds, B3 fails | Prop 6.3 | Also shows A3 is not necessary for D3 (see A3). OK. |
| Prop 6.5 (l.460) | (a) D3w; (b) with A3, D3 and D2; (c) with B3, D3t; D4b; D4a; D4 | **D1 for every L (hypothesis)**; A3 / B3 per clause; A2 for the last sentence. **A1 not used.** | Prop 6.1(a), Prop 6.3 | D4a needs only A2, but the statement reads as if it depended on D1 (R6). (c) nominally needs a preorder, but only B3 is used (R5). |
| Prop 7.1 (l.483) | (a) B1 + B6; (b) D5 + A3; (c) D1 ⇔ improvements; D2s; A3 | C7.0, C7.1, C7.2; defining rule; B1 (proved in (a), used in (b)(c)) | — | Closure under ties follows from (b) alone, not from (c) (R7). B6(ii) (cycles) is never used. OK otherwise. |
| Prop 8.1 (l.516) | D5, D1, D3t; with uniqueness, A3, D3, D2; then D2s | C8 (Prop 8.1 row); C4 via c_p := p | Thm 3.2, Prop 6.3 (B3), Prop 5.3 (a)/(b) | Uniform dominance needs uniqueness too (correct in the text; the prelim list is wrong). OK. |
| §8.1 paragraph (l.525) | Predd et al. Thm 1; SSK Thm 2 | C8 row; C4 | Thm 3.2, Prop 5.3(b), Prop 6.3 (B3); SSK09 Lemma 5 | OK. |
| Thm 8.2 (l.530) | D5, D1, D3, D2; with bounded losses, D2s | C8 row; C5 (Θ = 𝒞); A3′ proved; A4 (Nielsen) | Thm 3.3 (+ last claim), Thm 5.1 | OK. |
| Lemma 8.3 (l.559) | Constructs a continuous σ_F into Γ with supp q_0 ⊆ supp p | — | — | Constructed. OK. |
| Prop 8.4 (l.579) | D5, D1, D3t; with uniqueness, A3, D3, D2 | C8 row; C5 (Θ = Γ) | Lemma 8.3, Thm 3.3, Prop 6.3 (B3) | OK. |
| Ex 8.5 (l.589) | The freedom in C4(i) is used; some Bayes models are dominated | — | Prop 8.4 | OK. |
| Prop 8.6 (l.608) | D5, A3, D1, D3, D2s with margin d² | C5 (Θ = finitely additive probabilities on ℕ); A4 (ultrafilter, Fatou) | Thm 3.3, Thm 5.1 | OK. |
| Prop 8.7 (l.626) | Truth-directedness + D5 (single loss) + A3 do not give D1 | Loss ranking | — (direct) | OK. The surrounding prose calls D5 "coherent admissibility" (R3). |

---

## 3. The four decisive checks

### Check 1. Does any proof assume a dominance claim it is meant to establish?

**No.** The evidence:

1. **The main theorems.** Thms 3.2, 3.3, 4.1, 4.6 and Cor 4.2 assume only C0 (undominatedness and coherence of the **assigned** models) plus the mechanism hypotheses. C0 is the other half of the argument, not D1.
   - The proofs (l.184, l.243, l.279, l.340) first establish D1⁺ ("weakly dominated by an assigned model") using **only** the mechanism.
   - C0 enters only in the final sentence, which converts D1⁺ into D1, and in the Lemma 2.4 step.
   - So the weak-domination half is derived from hypotheses that mention no dominance notion at all.
   - The paper does not say this explicitly. l.46 says only that apart from C0, "neither ingredient mentions dominance". Making the separation explicit is revision R2.
2. **Section 5.** Thm 5.1 and Cor 5.2 do not use C0 at all. Prop 5.3 case (a) uses D1⁺ from Thm 3.2, which is derived from Prop 5.3's own hypotheses (it includes Thm 3.2's). This is not circular.
3. **Section 6.** Prop 6.1(a), 6.3 and 6.5 **assume** D1. They are labelled as conditional consequences (l.416: "Nothing here is a reason to assume it"), and none of them is used to establish D1. Prop 6.1(b) assumes conclusion-type claims (global coherence; incoherent models dominated by an undominated model) and derives only the identification, not D1. Ex 6.2 shows D1 does not follow.
4. **Remark 4.7** assumes D1 on purpose, to show that two weakenings would be equivalent to it. That is the correct use.
5. **Prop 7.1(c)** is an equivalence. It derives D1 from C7.1, C7.2 and the improvements (c)(ii), and it does not assume D1.
   - Caveat for the reader: the defining rule builds coherence into the ranking through the clause "available to no coherent model". Together with C7.2 this delivers D5 by construction. This is not circular, but it is the place where the coherent half is secured by design rather than derived (see check 2). l.510 says so honestly: it "does not, by itself, derive coherence from independently justified comparisons of performance".
6. **Applications.** Each proves D5 first ("Every probability is undominated", l.534; "Coherent models are undominated", l.583; l.612; l.520). Only then does it invoke Thm 3.2 or 3.3, so C0 is established, not assumed. Identification via Prop 6.3 comes after D1 has been obtained from Thm 3.2 or 3.3.

### Check 2. Does any construction-specific restriction masquerade as a general accuracy axiom?

**Not in the formal results.** There are two places where the prose needs tightening.

1. **The general framework assumes no order property** (l.58). The construction's properties (reflexivity, score-monotone acceptance, no ties between distinct models, cycles of equal models) are explicitly labelled as "properties of this construction, not requirements of the general argument" (l.506).
2. **Prop 7.1's premises** C7.1 and C7.2 are stated as premises of that proposition only (l.486–488). They appear nowhere in §§3–6.
3. **The companion's maximality characterisation** is described at l.510 as characterising "this ranking" for "its score". Its third clause (a change available to a coherent model is accepted only as guidance) is flagged as stronger than coherent admissibility, with "independent justification ... open" (l.510, l.654). Correct.
4. **Defect (scope wording):** l.510 says the third clause is stronger than coherent admissibility, "which asks only that coherent models remain undominated". This drops "under some ranking in the family", which is the defining feature of A2 (R3).
5. **Defect (stated but unused):** Prop 7.1(a) proves "every cycle consists of equal models" (B6(ii)), and nothing in LDG uses it. LDG neither states nor uses finite-chain consistency (B5) or the three-model condition (B4).
   - The companion paper makes B5 a requirement of every covering ranking (companion l.968).
   - A reader comparing the two papers could therefore take the construction's cycle property as the general consistency requirement.
   - LDG should say in one sentence that its general results need none of these (R7).
6. **Closure under ties (A3)** is not a construction-specific restriction. It is a per-ranking identification condition, assumed where invoked. It **is** a substantive family-wide assumption in D4 (l.467), and the inventory lists it in A.

### Check 3. Does any sufficient proof condition masquerade as a necessary requirement?

**In the formal statements, no.**
- Remark 4.8 proves that the hypotheses of Thms 4.1 and 4.6 are not implied by D1.
- Remark 4.9 says closed full comparison sets are "not necessary".
- §9 is headed "Sufficient conditions".

**Several sentences of prose, however, read as necessity claims:**

| Location | Text | Problem |
|---|---|---|
| l.48 | "The content of these theorems lies in one requirement: a single assigned model **must** serve against every rival at once" | Remark 4.7(i) shows only that relaxing this makes the hypothesis equivalent to D1. It is not necessary for D1. |
| l.284 | "What **cannot be relaxed** is that one assigned model serves against every rival at once" | Same issue. It can be relaxed, but only at the cost of explanatory content. |
| l.360 (italic heading) | "Guarantees on finite sets of worlds **need** a compact family to link them." | Ex 3.4 shows that finite guarantees **alone** do not suffice. It does not show that D1 requires a compact link: Remark 4.8 and the companion paper (l.52, l.506) obtain D1 without C3. |
| l.648 | "On infinitely many worlds the local guarantees **must** be linked through one compact family (Example 3.4)" | Same issue. |
| l.643 | "something like the hypotheses of Theorem 3.2 or 4.1 **is needed**" | They are sufficient. What Prop 8.7 shows is that **some** further hypothesis is needed. |
| l.37 (abstract) | "for infinitely many worlds the assigned models **must** also belong to one compact family" | This sits inside an "it suffices" sentence, so it is a requirement of the sufficient condition. Acceptable, but "are also required to" is less ambiguous. |

Two further points:
- **Closure under ties** is presented as the condition "we use" (l.109), never as necessary. That is correct: it is not necessary for D3 in general (Ex 6.4) but is necessary for transitive rankings (Prop 6.3).
- **Coherent admissibility** is necessary for D4, being equivalent to D4a. The paper treats it as an assumption, which is correct. Stating the equivalence would explain why it must be assumed rather than derived (R1).

### Check 4. Are admissibility under some ranking and admissibility under every ranking kept distinct?

**In the definitions and in Prop 6.5, yes.**
- A2 is "some ranking" (l.456).
- The proof uses 𝒞 ⊆ ⋃_L 𝒞_L (l.470).
- No result assumes that a coherent model is undominated under every ranking.
- The main theorems ask undominatedness only of the **assigned** models (C0), not of all coherent models, and they never assert D5.

**The term is used for a single-ranking property in three places, and loosely in a fourth:**

| Location | Text | What it actually means |
|---|---|---|
| l.54 (intro) | "truth-directedness and coherent admissibility do not suffice, contrary to a theorem of Joyce" | D5 for one loss: Joyce's hypothesis "no coherent credence is dominated" (l.624) |
| l.643 | "So truth-directedness and coherent admissibility do not supply the missing condition" | D5 for one loss |
| l.510 | "coherent admissibility, which asks only that coherent models remain undominated" | Omits "under some ranking in the family" |
| l.513 | "Coherent admissibility for a family holds when every **intended** coherent model is undominated under at least one of the losses considered" | Correct scope. "Intended" is undefined, and A2 quantifies over **all** of 𝒞. |

For a one-member family, "some" and "every" coincide. That is exactly why the single-ranking usage blurs the distinction the guidance asks to keep. D5 (per ranking, all coherent models) is strictly stronger than A2 for any family with more than one member, and the applications prove D5 (l.513, step one). The inventory therefore keeps D5 and A2 separate (R3).

---

## 4. Ranked list of manuscript revisions

Ranking runs from structural (needed to present the axioms in the order assumptions → dominance → conclusions) down to local wording. Replacement text is given where it can be pinned down. "Insert after l.N" refers to the r69 .tex.

Every quoted "replace" target below was checked by `grep -F` and occurs **exactly once** in the .tex. The quotes show rendered numbers, e.g. "Remark 4.7", where the source has `\ref{...}`. The replacement text likewise uses rendered numbers and should be converted to `\ref` when spliced.

**R1 (structural). State the family-level assumptions with the other assumptions, before the theorems.**
- Currently, evaluability and coherent admissibility first appear in §6.3 (l.453–458), after all the dominance results. The guidance asks for independently stated assumptions first.
- **Location:** end of §2.1, after the closure-under-ties paragraph (after l.109, before Lemma 2.4).
- **Insert:**
  > *Families of rankings.* The normative conclusions of Section 6.3 concern a family 𝔏 of rankings and use two conditions on it, stated here so that every assumption of the paper appears before the results. *Evaluability*: every model is evaluated by some ranking in 𝔏. *Coherent admissibility*: every coherent model is an undominated coherent model of some ranking in 𝔏. Coherent admissibility is a condition on the family: it does not require any single ranking to leave every coherent model undominated, nor any coherent model to be undominated under every ranking. It is exactly the statement that every coherent model is undominated under some ranking, so it cannot be derived from properties of individual rankings and is assumed. No result before Section 6.3 uses either condition, and no proof uses evaluability.
- At l.453–458, keep the definitions of "irrational" and "permissible". Replace the bullet list with a back-reference ("the two conditions on the family stated in Section 2.1").

**R2 (structural; check 1). Make visible that the mechanism proves weak domination without the undominatedness of the assigned models.**
- **Location:** after the proof of Thm 4.1, extending l.282.
- **Replace** l.282 ("The proof uses no property of the relations, no topology on models, no parametrisation of the coherent models and no numerical values.") **with:**
  > The proof uses no property of the relations, no topology on models, no parametrisation of the coherent models and no numerical values. Nor does the proof of (a) use that the assigned models are coherent or undominated: the guarantee and serving conditions alone give a weak dominator among the assigned models. Their membership in 𝒞_L is used only to conclude that this weak dominator is an undominated coherent model, and in (b) and (c). The same holds for Theorems 3.2, 3.3 and 4.6. So the half of the argument that concerns incoherent models is derived from hypotheses that mention no dominance notion, and the other half, that the assigned models are undominated, is a separate hypothesis that each application verifies first.
- **Optional:** in l.513, add after "so that 𝒞_L = 𝒞": "(this establishes the hypothesis that the assigned models are undominated coherent models, before Theorem 3.2 or 3.3 is applied)".

**R3 (check 4). Stop using "coherent admissibility" for a single-ranking property.**
- **l.54:** replace "A short counterexample shows that truth-directedness and coherent admissibility do not suffice, contrary to a theorem of Joyce" with
  > A short counterexample shows that a truth-directed loss under which every coherent model is undominated need not dominate every incoherent model, contrary to a theorem of Joyce
- **l.643:** replace "So truth-directedness and coherent admissibility do not supply the missing condition; something like the hypotheses of Theorem 3.2 or 4.1 is needed." with
  > So truth-directedness, together with the undominatedness of every coherent credence under the given loss, does not supply the missing condition. A further hypothesis is needed; those of Theorems 3.2 and 4.1 are sufficient ones.
  This also fixes the necessity wording (check 3).
- **l.510:** replace "and it is stronger than coherent admissibility, which asks only that coherent models remain undominated;" with
  > and, together with the protection of coherent models by guidance, it is stronger than coherent admissibility, which asks only that each coherent model be undominated under at least one ranking in the family;
- **l.513:** replace "every intended coherent model" with "every coherent model". Add after "This verifies the conditions for a single ranking.":
  > Showing that every coherent model is undominated under a single loss is stronger than coherent admissibility, which needs this only for some loss in the family; it is needed here to identify the undominated models with the coherent ones.

**R4 (check 3). Remove necessity wording for sufficient conditions.**
- **l.48:** replace "The content of these theorems lies in one requirement: a single assigned model must serve against every rival at once (Remark 4.7)." with
  > The content of these theorems lies in one feature of their hypotheses: a single assigned model serves against every rival at once. If the assigned model could depend on the rival, the hypotheses would be equivalent to the conclusion (Remark 4.7).
- **l.284:** replace "What cannot be relaxed is that one assigned model serves against every rival at once (Remark 4.7)." with
  > What cannot be relaxed without making the hypotheses equivalent to the conclusion is that one assigned model serves against every rival at once (Remark 4.7).
- **l.360:** replace the italic heading "Guarantees on finite sets of worlds need a compact family to link them." with
  > *Guarantees on finite sets of worlds do not suffice by themselves.*
  Replace the final sentence "So guarantees on finite sets of worlds do not suffice without a compact family linking them." with
  > So, in Theorem 4.6, guarantees on finite sets of worlds do not suffice without a compact family linking them. This concerns the hypotheses of the theorem: the dominance property itself can hold when they fail (Remark 4.8, Section 7).
- **l.648:** replace "On infinitely many worlds the local guarantees must be linked through one compact family (Example 3.4)" with
  > On infinitely many worlds, Theorem 4.6 links the local guarantees through one compact family, and this link cannot be omitted from its hypotheses (Example 3.4); it is not a necessary condition for the dominance property (Remark 4.8)
- **l.37 (abstract), optional:** replace "the assigned models must also belong to one compact family" with "the assigned models are also required to belong to one compact family".

**R5 (states a property it does not use: reflexivity). Prop 6.3 and Prop 6.5(c) assume "preorder", but the proof uses only transitivity.**
- **l.441:** replace "Let L be a preorder ranking with the dominance property." with
  > Let L be a ranking whose relations are transitive (for instance, a preorder ranking), with the dominance property.
- **l.444 (end of proof), add:** "Reflexivity is not used."
- **l.465:** replace "if L is a preorder ranking" with "if the relations of L are transitive".
- **l.467:** replace "closed under ties or is a preorder ranking" with "closed under ties or has transitive relations".
- **l.650 (§9):** append to the first sentence:
  > Proposition 6.3 uses transitivity and no other property; Proposition 7.1 assumes none and proves reflexivity for its ranking.
- **l.58:** the definition of "preorder ranking" may stay. It is still used for loss rankings at l.76.

**R6 (states an assumption it does not use: evaluability; and hides that D4a needs only A2).**
- **l.467:** replace "With coherent admissibility, every coherent model is permissible; if in addition every ranking is closed under ties, the permissible models are exactly the coherent ones." with
  > Coherent admissibility alone makes every coherent model permissible. If, in addition, every ranking in 𝔏 is closed under ties, the permissible models are exactly the coherent ones.
- **l.472:** replace "So, given evaluability and coherent admissibility, if every ranking in the family meets the hypotheses of one of these theorems and is closed under ties, then the permissible models are exactly the coherent ones and every incoherent model is irrational." with
  > So, given coherent admissibility, if every ranking in the family has the dominance property (for instance, by Theorem 3.2, 3.3, 4.1 or 4.6, or by Proposition 7.1(c)) and is closed under ties, then the permissible models are exactly the coherent ones and every incoherent model is irrational. Evaluability is not needed for this conclusion; it ensures that no model is irrational merely because no ranking evaluates it.
- **l.461:** extend "(for instance, because it meets the hypotheses of Theorem 4.1 or 4.6)" to "(for instance, because it meets the hypotheses of Theorem 3.2, 3.3, 4.1 or 4.6, or of Proposition 7.1(c))".

**R7 (construction premises and unused order properties; check 2).**
- **Prop 7.1(b), l.487:** append "and L is closed under ties."
- **Prop 7.1(c), l.493:** replace "When they hold, closure under ties holds, and every incoherent model is strictly dominated by an undominated coherent model." with "When they hold, every incoherent model is strictly dominated by an undominated coherent model."
- **Proof:** move the last sentence of l.501 ("Finally, a model tied with a coherent c weakly dominates c, so it is c, by (b); this is closure under ties.") to the end of the proof of (b), l.499.
- **l.478:** to make clear this is a definition, not further data, replace "A change is *available to* a model z if ..." with "We say that a change is *available to* a model z if ...". This is a minor change.
- **l.506:** after "These are properties of this construction, not requirements of the general argument, which assumes no property of the relations." insert:
  > In particular, no result of Sections 2–6 uses reflexivity, the condition that no chain of comparisons ends in a strict reversal, or its three-model case, and the cycle property of Proposition 7.1(a) is not used elsewhere in this paper; it is recorded for comparison with the companion paper.

**R8 (dangling reference).** l.506 says "Proposition 7.1 answers the third question directly." The "three questions" framing was removed in an earlier restructure; earlier drafts at `r69/build/LDG_before_restructure.tex` l.37 still have it. **Replace with:**
> Proposition 7.1 thus gives a second route to the dominance property, independent of Sections 3 and 4.

**R9 (garbled sentence).** l.510: "its repair theorem shows that every incoherent model can be replaced by a coherent one through a change that no coherent model could make and that raises the score at every world by a uniform margin; the ranking is obtained as a consequence." **Replace** "the ranking is obtained as a consequence" **with:**
> the dominance property of its ranking follows, as in Proposition 7.1(c)

**R10 (name A3 in the loss-theorem statements).** Thm 3.2, l.181: replace "If, in addition, every model with the same loss profile as an undominated coherent model is coherent, then" with
> If, in addition, the ranking is closed under ties (for a loss ranking, equivalently: every model with the same loss profile as an undominated coherent model is coherent), then

Thm 3.3 (l.239) then inherits this by reference.

**R11 (make the C_L convention two-sided).** l.103: replace "So 𝒞_L ⊆ U_L by definition. We do not assume that incoherent models are dominated." with
> So 𝒞_L = 𝒞 ∩ U_L ⊆ U_L by definition. The notation names a subclass and asserts nothing: we assume neither that incoherent models are dominated nor that coherent models are undominated.

**R12 (abstract; low priority).** Replace "and if every coherent model is undominated under some ranking, the rationally permissible models are exactly the coherent ones" with
> and, for a family of rankings each with the dominance property and closed under ties, if every coherent model is undominated under some ranking in the family, the rationally permissible models are exactly the coherent ones

**Checked and found to need no change:**
- No ordering property is used without being stated. Every use of reflexivity, completeness or transitivity in a proof is covered by a stated hypothesis or by the declared properties of loss rankings (l.76).
- l.44 and l.107 ("never a standing assumption"; "a claim to be established, not an assumption") are accurate.
- l.416 ("Nothing here is a reason to assume it") is accurate.
- l.187 ("this freedom is needed") refers to applying Thm 3.2 in Ex 8.5 and is accurate in context.
- l.46 ("The compact family cannot be dropped") is a claim about the theorem's hypotheses and is accurate.

---

## 5. Verification of revised manuscript (r70)

**Audited:** `r70/Coherence and Dominance under General Rankings.tex` (678 lines) and its PDF (25 pages). The PDF is byte-identical to `r70/build/...pdf` and was built from the current .tex.

**Method:**
- `r70/build/LDG_r69_copy.tex` is byte-identical to the r69 source.
- A word-level diff of r69 against r70 is saved as `r70/build/ax70l_wdiff.txt`. Every changed span was read.
- Every `\ref`/`\eqref` was checked against the defined labels, and every `\cite` against the `\bibitem`s.
- Numbering was read from the r70 `.aux`.
- The log was scanned for warnings.

### 5.1 R1–R12 and corrections

| Item | Verdict | Where (r70 line) |
|---|---|---|
| R1 | Done as specified. The *Families of rankings* paragraph is in §2.1 before Lemma 2.4. §6.3 back-references it. | l.111; l.466 |
| R2 | Done verbatim, plus the optional §8 sentence | l.295; l.521 |
| R3 | Done at all four sites (l.54, l.651, l.518, l.521). No single-ranking use of "coherent admissibility" remains (grep: l.111, 133, 466, 518, 521, 654 are all family-level). | — |
| R4 | Done at all five sites, including the abstract | l.37, 48, 297, 373, 656 |
| R5 | Done: Prop 6.3, end of its proof, 6.5(c), the 6.5 "iff" claim, §9 | l.454, 457, 473, 475, 658 |
| R6 | Done: hypothesis examples, "Coherent admissibility alone ...", closing sentence | l.469, 475, 480 |
| R7 | Done: closure under ties moved to 7.1(b) (statement and proof); (c) still "Assume both conditions"; "We say that"; the sentence on unused order properties | l.486, 495, 501, 507, 514 |
| R8, R9, R10, R11, R12 | Done verbatim | l.514; l.518; l.194; l.103; l.37 |
| Prop 8.1 correction | Done. Uniqueness is now explicit in the uniform-dominance clause, matching the unchanged proof. | l.525 |

### 5.2 New §2.2 "What is assumed and what is proved" (l.125–134)

**Order and naming.** Both correct:
- The order is setting → substantive assumptions → ordering properties → alternative sufficient packages (selection argument → finite-world weakening → local infinite-world conditions → loss-based) → the separate construction with its own premises → conclusions.
- The section is placed before §3, so assumptions precede the dominance results.
- Only descriptive names are used, and no inventory labels.

**Accuracy and completeness.** All guidance items A–D are present, and the some-versus-every distinction is explicit. Three statements need correcting:
1. **Item (3) "None is assumed" is inaccurate.**
   - Transitivity **is** assumed in Prop 6.3 and 6.5(c), and completeness in the converse of Lemma 2.1. The intended claim is "no standing assumption".
   - "Transitivity enters only through Proposition 6.3" overlooks the transitivity of ≤ used in Thm 3.2's proof that the loss-profile form is equivalent to closure under ties (l.197).
   - The three-model case is omitted here, although the guidance lists it and l.514 mentions it.
2. **Item (2): "used wherever the undominated models are identified exactly"** overstates the role of closure under ties.
   - Prop 6.1(b) identifies them without it.
   - For non-transitive rankings it is not necessary for the identification (Ex 6.4).
   - Its actual role is to pass *from the dominance property* to the identification.
3. **Item (4)** describes the loss-based package without the compact family needed for infinitely many worlds (Thm 3.3).

### 5.3 The four decisive checks, re-run on r70

1. **No proof assumes the dominance claim it establishes.** No proof changed except the move within Prop 7.1. l.295 now states the separation explicitly.
2. **No construction-specific restriction is presented as general.** l.514 states that the cycle property, finite-chain consistency, the three-model case and reflexivity are unused in §§2–6. l.518 scopes the third maximality clause and its comparison with coherent admissibility correctly.
3. **No sufficient condition is presented as necessary.** Every remaining "must", "cannot" or "needed" concerns the hypotheses of a stated theorem or example: l.46, 200, 297, 308, 351, 651, 656. No necessity claim about the dominance property remains.
4. **"Some" versus "every" is distinct throughout.** See l.111, l.130 (§2.2(2)), l.466, l.518, l.521 and l.654.

### 5.4 Mathematical statements and cross-references

**Statement changes.** Only the intended ones, and each is supported by the existing proof:
- Prop 6.3, 6.5(c) and the 6.5 "iff" claim: the hypothesis is weakened from preorder to transitivity. The proof uses only transitivity.
- Prop 7.1(b) now also asserts closure under ties. Its proof sentence was moved, unchanged apart from dropping "by (b)".
- Prop 7.1(c) no longer asserts closure under ties. It is implied by (b).
- Thm 3.2: the extra hypothesis is renamed as closure under ties, in an equivalent form.
- Prop 8.1: uniqueness is made explicit.
- Prop 6.5: "every coherent model is permissible" is now attributed to coherent admissibility alone. This matches the unchanged proof (l.478).

No other statement, proof or example changed.

**Cross-references.**
- All labels resolve. There are no undefined references or citations and no duplicate labels.
- The log has no warnings and no overfull or underfull boxes.
- All result numbers are unchanged from r69. The new subsection is §2.2 (`sec:inventory`, not referenced). `sec:permissible` = §6.3.
- l.466's "Section 2" correctly points to the section containing §2.1.

### 5.5 Remaining required fixes (all in §2.2)

**F1. Replace item (3) (l.130) with:**
> \item \emph{Ordering properties.} None is a standing assumption: the relations need not be reflexive, complete or transitive, and neither finite-chain consistency (no chain of comparisons ending in a strict reversal) nor its three-model case is used anywhere. Completeness enters only through loss rankings, via Lemma~\ref{lem:bayes-competitive}, in Theorems~\ref{thm:bayes-finite} and~\ref{thm:bayes-infinite} and their applications. Transitivity is assumed only in Proposition~\ref{prop:profiles} and the results that cite it; for loss rankings, the transitivity of the order of the losses is also used in Theorem~\ref{thm:bayes-finite} to show that its loss-profile form of closure under ties is equivalent to closure under ties. Reflexivity is used only in Section~\ref{sec:construct}, where it is proved for the ranking constructed there.

**F2. In item (2) (l.129), replace** "On a single ranking: closure under ties, used wherever the undominated models are identified exactly and wherever weak domination is upgraded to domination." **with:**
> On a single ranking: closure under ties, used to pass from the dominance property to the exact identification of the undominated models with the undominated coherent ones, and to upgrade weak domination to domination.

**F3. In item (4) (l.131), replace** "and the loss-based conditions, Bayes choices for priors supported within the support of the indexing prior with lower semicontinuous losses (Theorems~\ref{thm:bayes-finite} and~\ref{thm:bayes-infinite})" **with:**
> and the loss-based conditions, Bayes choices for priors supported within the support of the indexing prior with lower semicontinuous losses, drawn for infinitely many worlds continuously from one compact family (Theorems~\ref{thm:bayes-finite} and~\ref{thm:bayes-infinite})
