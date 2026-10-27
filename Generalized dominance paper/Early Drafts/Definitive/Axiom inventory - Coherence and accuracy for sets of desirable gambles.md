# AX70A: Axiom inventory for "Coherence and accuracy for sets of desirable gambles"

**Auditor:** AX70A. **Date:** 26 October 2026.
**Text audited:** `r69/Coherence and accuracy for sets of desirable gambles.tex` (1731 lines), with its PDF.
**Terminology cross-checked against:** `r69/Coherence and Dominance under General Rankings.tex` ("LDG"), for terminology only.
**Binding guidance:** `r70/AUDIT_r70_axiom_audit.md`, §§2–3.

**Numbering.** Result numbers are taken from the compiled `.aux` file and match the PDF. "L*n*" means line *n* of the `.tex`. Two numbering coincidences are worth keeping in mind:
- Proposition 6.3 (`prop:maximal`) is a result, while §6.3 (`sec:undominated`) is the section that defines coverage.
- The application's Proposition 6.6 and Example 6.4 have no connection to LDG's Proposition 6.5 and Example 6.4.

**Method.** I checked each item below against the theorem statements and, more importantly, against the proofs. Where a proof uses less than its theorem states (for example only one instance of a measure condition), I record what is actually used. I introduce no new axioms. Where I suggest replacement wording, it only re-describes the status of assumptions that are already there.

**Verdict in one paragraph.** The formal architecture is sound.
- No proof assumes a dominance claim that it is meant to establish.
- "Global coherence" and "every incoherent model is dominated" appear only in two roles: as requirements in the definition of coverage, and as conclusions of Theorems 6.8 and 8.1 and Corollary 7.1.
- The weaknesses are in the wording around the definitions, not in the mathematics:
  1. The coverage definition labels requirements (2)–(5) "the dominance property". LDG uses that phrase for something else.
  2. The same definition implies that (1) is assumed while (2)–(5) are achieved, although all six must be proved.
  3. The definition of a ranking on a domain imports reflexivity, which LDG declines to assume and which no result here uses.
  4. In two places the prose lists disjoint additivity (and once the construction's own constraints) as if coverage required them.
  5. §9.2 and the open questions blur three different conditions: protection under one ranking, coherent admissibility across a family, and undominatedness of a single target.

  All five are fixable by rewording (Part 5).

---

## Part 1. Reader-facing inventory

The fields for each item are:
- **Statement**: exact mathematical content, quoted from or matched to the manuscript;
- **Meaning**: a plain-English explanation;
- **Scope**: world / ranking / family / model space;
- **Status**: assumed / defined (constructed) / proved;
- **Required by**: which results use the item, checked in the proofs.

---

### A. The mathematical setting

These items are standing assumptions or definitions. None of them mentions rankings or dominance.

#### A1. Worlds
- **Statement.** Ω is a nonempty set of any cardinality (L222).
- **Meaning.** The possible states of affairs. No structure is assumed.
- **Scope.** Model space (background).
- **Status.** Assumed.
- **Required by.** Everything.

#### A2. Gambles form a closed linear space of bounded functions
- **Statement.** E ⊆ ℓ∞(Ω) is a linear subspace that is closed in the sup norm ‖h‖ = sup_Ω|h| (L223–225).
- **Meaning.** Gambles are bounded payoffs, and limits of gambles are gambles.
- **Scope.** Model space.
- **Status.** Assumed.
- **Required by.** Completeness of E is needed for the Bochner integral m(X) ∈ E (L290–293, Lemma 3.1). It is also needed for duality in Lemma 2.1(e) and Lemma 2.3(b).

#### A3. Separability of the gamble space
- **Statement.** E is norm-separable (L224–225).
- **Meaning.** Countably many gambles approximate every gamble.
- **Scope.** Model space.
- **Status.** Assumed.
- **Required by.**
  - Metrizability of the state space (Lemma 2.1(a)), which Lemma 2.4(a),(b) uses through sequences and dense sequences.
  - The countable set of worlds Ω₀ (Lemma 2.1(f)), used in Lemma 6.5 and hence in Propositions 6.6 and 6.7.
  - Bochner integrability of the identity map, which gives the score and Lemma 3.1.
  - Existence of measures satisfying (M1)–(M3) (Lemma 2.2).

  The manuscript does not claim separability is necessary. Non-separable spaces are listed as an open question (L1297).

#### A4. An order unit: the constants, or a gamble bounded below by a positive constant
- **Statement.** 1 ∈ E (L225–226). More generally, it suffices that some e ∈ E has inf_Ω e > 0 (Remark B.3). All results then transfer, with margins multiplied by at least inf e.
- **Meaning.** There is a sure gain. States can be normalised on it, and adding a constant shifts lower previsions by that constant.
- **Scope.** Model space.
- **Status.** Assumed.
- **Required by.**
  - Normalisation of states and ‖q‖ = 1 (Lemma 2.1(a)).
  - The translation rule P_Q(h + t1) = P_Q(h) + t and ∂D_Q = {P_Q = 0} (Lemma 2.1(c)).
  - The fact −1 ∉ D_Q (Lemma 2.4(c)).
  - D_S open and containing 1 (Lemma 2.3(b)).
  - The construction of measures (Lemma 2.2).

  The manuscript argues that some condition of this kind is needed: at a world where every gamble pays 0, nothing is strict (L1268–1269). It also gives c₀ as an open case (L1298–1300).

#### A5. States, credal sets, lower previsions and the sets D_Q (definitions)
- **Statement.**
  - A *state* is a positive, normalised linear functional on E. S is the set of states, with the weak-* topology.
  - A *credal set* is a nonempty, weak-* closed, convex Q ⊆ S.
  - P_Q(h) = min_{q∈Q} q(h).
  - D_Q = {P_Q > 0} and C_Q = {P_Q ≥ 0}.
  - D_∅ = E by convention (L231–242).
- **Meaning.** Expectation functionals, sets of them, and the gambles they unanimously deem favourable.
- **Scope.** Model space.
- **Status.** Defined. The properties in Lemma 2.1 are proved.
- **Required by.** Everything after §2.1.

#### A6. A finite Borel measure on gambles
- **Statement.** μ is a finite Borel measure on (E, ‖·‖) (L267).
- **Meaning.** It weights gambles. It fixes which sets of gambles are negligible and how much each gamble counts in the score.
- **Scope.** Model space.
- **Status.** Assumed.
- **Required by.**
  - Finiteness gives L∞(μ) = L¹(μ)*, which Lemma 3.1 needs for weak-* compactness of the fractional acceptance choices.
  - It also underlies the score.

#### A7. Finite first moment (M1)
- **Statement.** ∫‖h‖ dμ(h) < ∞ (L269).
- **Meaning.** Large gambles are rare enough that integrated payoffs are finite.
- **Scope.** Model space.
- **Status.** Assumed throughout (L276).
- **What it does.**
  - With A3, it makes m(X) = ∫_X h dμ a Bochner integral in E, so the score m_ω(X) is defined and finite.
  - It makes the score map continuous in Lemma 3.1.
  - It gives dominated convergence in the trimming step of Theorem 5.1.
- **Required by.** Every result that mentions the score: Lemmas 2.4(d), 3.1 and 4.3; Corollaries 3.2 and 3.3; Theorem 5.1; Propositions 6.2, 6.3, 6.6 and 6.7; Theorem 6.8; Corollary 7.1; Theorem 8.1 (stated separately); Examples 6.4, B.1 and B.2.

  Propositions 6.2 and 6.3 use M1 and nothing else (L849 says so for 6.3, and this is correct).

#### A8. Null indifference boundaries (M2)
- **Statement.** μ{P_Q = 0} = 0 for every credal set Q (L270).
- **Meaning.** For every credal set, the gambles on its indifference boundary are negligible. In particular, for each state q the gambles it is exactly indifferent to are negligible, and so are the gambles that pay exactly 0 at a world.
- **Scope.** Model space.
- **Status.** Assumed where stated.
- **What it does.** Different instances do different jobs. This was verified in the proofs.

| Instance of M2 used | Job it does | Where |
|---|---|---|
| Q = {q}, a single state: μ{q = 0} = 0 | The optimal fractional acceptance against q is unique and is an ordinary set G ∩ {q > 0}. This is why the repair is an actual model and not a randomised one. | Lemma 3.1(b),(c); Corollary 3.3(b); Lemma 2.4(d) |
| Q = Q_B, the supporting states of a model | A consistent model lies inside its coherent hull, and the hull is the least coherent model containing it. This gives the test for whether a coherent model could make a change. | Lemma 2.4(b) (second sentence) and (c) (converse); Lemmas 2.6 and 4.3; Corollary 7.1(a) and its domain examples |
| Q = S: μ{inf_Ω h = 0} = 0 | A change guided at every world is null for every coherent model. This is **protection**. | Lemma 6.5, and hence Propositions 6.6 and 6.7 |
| All Q (including Q = K_D) | Coherent sets of desirable gambles, in Walley's sense or the weak sense, coincide with the coherent models modulo μ. | Lemma 2.3(b) (last sentence) and (c); Theorem 6.8(a) ("that is, …") |

  - **Essentiality.** Example B.2 shows that the instance Q = S is essential for protection: without it, a guided change strictly dominates a coherent model. The unnumbered example in §2.3 (L342–350) shows that without M2, Walley coherence and coherence modulo μ come apart. The manuscript does **not** claim, and does not show, that the full M2 is necessary for the repair theorem.
- **Required by.** Lemmas 2.3(b),(c), 2.4(b)–(d), 2.6, 3.1 and 4.3; Corollaries 3.2 and 3.3; Theorem 5.1; Lemma 6.5; Propositions 6.6 and 6.7 (these three only through the Q = S instance); Theorem 6.8; Corollary 7.1; Proposition C.1.

#### A9. Full support (M3)
- **Statement.** Every nonempty open subset of E has positive μ-measure (L271).
- **Meaning.** No region of gambles is ignored.
- **Scope.** Model space.
- **Status.** Assumed where stated.
- **What it does.** It distinguishes credal sets. Without it, distinct credal sets can give the same model (the point-mass example, L352–354). It is **not** used for repair, for the ranking's properties, for protection, for dominance or for coverage on E.
- **Required by.**
  - Lemma 2.3(a): an open set contained in D_Q a.e. is contained in D_Q, so Q ↦ D_Q is one-to-one.
  - Hence the bijection in Theorem 6.8(a), and nothing else in Theorem 6.8 (L1010–1011, L1015).
  - Appendix C: one-sidedness of each D_{K'}, and Proposition C.1, whose characterisation of local freedom rests on Lemma 2.3(a).
  - The "Reach" contrast in §8 (L1196–1197), which uses Lemma 2.3(a) to conclude that D_{p} is dominated.
- **The two roles kept apart.** Repair and dominance need M1 and M2. Full support only lets "covers K" tell different targets apart (L1028–1030) and lets local freedom on one-sided domains be characterised.

#### A10. Models, identified up to null sets
- **Statement.** A model is a subset of E that is measurable for the completion of μ. Models that are equal a.e. are identified, and inclusions between models are read a.e. (L312–315).
- **Meaning.** A model is a set of accepted gambles, and negligible differences are ignored.
- **Scope.** Model space.
- **Status.** Defined (a modelling choice).
- **Required by.** Everything. Which models count as incoherent depends on μ (L1271–1279).

#### A11. Coherence (definition, kept separate from everything above)
- **Statement.** A model X is *coherent* if X = D_Q a.e. for some credal set Q. Otherwise it is *incoherent*. Related definitions:
  - Q_B = {q : q(h) ≥ 0 for μ-a.e. h ∈ B} are the *supporting states* of B.
  - hull(B) = D_{Q_B} is the *coherent hull* of B (it equals E when Q_B = ∅).
  - B is *consistent* if Q_B ≠ ∅ (L316, L358–364).
- **Meaning.** A model is coherent if, up to negligible gambles, it accepts exactly the gambles that every member of some credal set rates positively.
- **Scope.** Model space. The coherent class is fixed before any ranking is defined, as in LDG.
- **Status.** Defined. Its link to Walley coherence is proved (Lemma 2.3, under M2).
- **Required by.** Everything from §2.4 on.

#### A12. The score (integrated payoff)
- **Statement.** m_ω(X) = ∫_X h(ω) dμ(h). Higher is better (L297–300).
- **Meaning.** The total payoff at ω of the gambles X accepts, weighted by μ. Up to a constant, minus the score is the weighted error at ω (L301–308).
- **Scope.** One world.
- **Status.** Defined. It is finite by M1.
- **Required by.** Theorem 5.1, Definition 6.1 and everything after them. The manuscript makes no claim for other scores (L1288–1292).

#### A13. Changes, availability and guidance (definitions)
- **Statement (Definition 2.5).**
  - The change from Y to X adds A = X∖Y and removes B = Y∖X.
  - It is *available to* Z ("Z could make it") if B ⊆ Z a.e. and A ∩ Z is null.
  - It is *guided by ω* if A ⊆ {h(ω) > 0} and B ⊆ {h(ω) < 0} a.e.
- **Meaning.**
  - A change is available to Z when Z holds everything it gives up and nothing it takes on.
  - A change is guided by ω when it only adds gambles that win at ω and only drops gambles that lose there.
- **Scope.** Availability concerns the model space and does not depend on the world. Guidance concerns one world.
- **Status.** Defined.
- **Required by.**
  - Lemmas 2.6, 2.7, 4.3 and 6.5.
  - Definition 6.1.
  - Coverage requirement B1 (strict guidance).
  - Theorem 8.1(a).

#### A14. Dominance nomenclature (definitions)
- **Statement (§6.2, L888–892).** Y *weakly dominates* X if Y ⪯_ω X at every world. Further:
  - Y *dominates* X if, in addition, Y ≺_ω X at some world.
  - Y *strictly dominates* X if Y ≺_ω X at every world.
  - Y *uniformly dominates* X if Y strictly dominates X and inf_ω (m_ω(Y) − m_ω(X)) > 0.
  - A model is *undominated* if no model dominates it.
- **Scope.** One ranking (all worlds).
- **Status.** Defined. "Dominates" agrees with LDG's definition: LDG says "not tied at every world", which it proves equivalent. "Uniformly" is tied to the integrated-payoff score.
- **Required by.** §6.2 onwards.
- **Note.** ≺_ω and "tied" are defined only inside Definition 6.1 (L758–759), that is, for the paper's own ranking. §6.3 then uses them for arbitrary rankings on a domain. See revision R1.

#### A15. Domains, models on a domain, and "ranking on a domain"
- **Statement (L955–958).**
  - A *domain* is a Borel set U ⊆ E.
  - The *models on U* are the models contained in U a.e., always represented inside U.
  - A *ranking on U* assigns to each world "a reflexive relation on the models on U under which a.e.-equal models are tied".
- **Scope.** The domain is part of the model space. A ranking on U is one ranking.
- **Status.** Defined. **Flag:** this definition imports a property that LDG does not assume. See Part 3, check 1(c), and revision R1.
- **Required by.** The definition of coverage, Corollary 7.1, Theorem 8.1 and Proposition C.1.

#### Summary: what each measure condition does

| Condition | Repair (Thm 5.1) | Ranking's structure (Props 6.2, 6.3) | Protection and strictness (Lem 6.5, Props 6.6, 6.7) | Coherent sets of desirable gambles = coherent models (Lem 2.3(b),(c)) | Distinct credal sets give distinct models (Lem 2.3(a); bijection in Thm 6.8(a)) | Local freedom on one-sided domains (App. C) |
|---|---|---|---|---|---|---|
| A6 μ finite | yes | (scores) | — | — | — | — |
| M1 finite first moment | yes | **only this** | (scores) | — | — | yes |
| M2 null boundaries | yes (singletons, hulls) | no | **only the Q = S instance** | yes (all Q) | — | yes |
| M3 full support | **no** (Rem 5.2(c)) | no | no | no | **yes** | yes |

---

### B. Requirements on a covering ranking (definition in §6.3, L955–978)

> **READ THIS FIRST.** Every item in this group is part of the *definition* of "a ranking on U covers K". These are **requirements that must be PROVED** for any ranking claimed to cover K. **They are not assumptions that the construction, or any theorem in the paper, may invoke.** For the ranking of Definition 6.1, Theorem 6.8(e) (on E) and Corollary 7.1(d) (on domains closed under coherent hulls) prove them. For the veto–Brier ranking, Theorem 8.1 proves them. Only three results quantify over *arbitrary* covering rankings: the second sentence of Corollary 7.1(d), and Proposition C.1(a) and (c). Each uses only B6a and B8, which concern the domain and the target, as **necessary conditions**. None of them uses a dominance requirement as a premise.

What the definition presupposes (A15): the relation at each world is reflexive, and a.e.-equal models are tied. Given the identification A10, or given B2 below, these two clauses say the same thing; each implies the other. So the presupposition amounts to **reflexivity**. LDG assumes no property of the relations (LDG L58). No result about arbitrary covering rankings uses reflexivity. See check 1(c).

The manuscript lists six requirements. I separate them into nine items, as the guidance asks, and split requirement (4) because its two halves concern different things.

#### B1. Strict guidance — manuscript requirement (1)
- **Statement.** If the change from Y to X is guided by ω and X ≠ Y a.e., then X ≺_ω Y.
- **Meaning.** A non-trivial change that only corrects errors at ω makes the model strictly better at ω. This is a form of truth-directedness.
- **Scope.** One world, one ranking. It concerns **the ranking alone**.
- **Status.** Requirement, to be proved. Proved for Definition 6.1 in Proposition 6.2(b), and for veto–Brier in Theorem 8.1(a), Step 2.

#### B2. Independence — requirement (1)
- **Statement.** Whether X ⪯_ω Y holds depends only on the change from Y to X: if X∖Y = X'∖Y' and Y∖X = Y'∖X' a.e., then X ⪯_ω Y if and only if X' ⪯_ω Y'.
- **Meaning.** A comparison is judged by what is added and what is removed, not by what stays the same.
- **Scope.** One world, one ranking. **The ranking alone.**
- **Status.** Requirement. Proved in Proposition 6.2(a) and Theorem 8.1(a).
- **Side effect.** Independence alone makes each relation respect a.e.-equality: X ⪯ Y and X' = X a.e. give X' ⪯ Y.

#### B3. Chain consistency (the manuscript's "acyclicity") — requirement (1)
- **Statement.** There is no chain A₀ ⪯_ω A₁ ⪯_ω ⋯ ⪯_ω A_k with A_k ≺_ω A₀.
- **Meaning.** Following weak comparisons forward never leads to something strictly worse than the start. Ties between distinct models are allowed (L983–984).
  - The case k = 1 is vacuous.
  - The case k = 2 is the **three-model no-reversal condition**: there is no A ⪯ B ⪯ C with C ≺ A.
  - The chain condition is what social-choice theory calls *Suzumura consistency*. It is strictly stronger than acyclicity of the strict part, and strictly weaker than transitivity.
- **Scope.** One world, one ranking. **The ranking alone.**
- **Status.** Requirement. Proved in Proposition 6.2(b), and in Theorem 8.1(a) (complete and transitive).
- **Not part of B3.** The stronger property "every cycle consists of a.e.-equal models" is *not* required (L985–988). It holds for Definition 6.1 because distinct models are never tied there.

#### B4. Global coherence — requirement (2)
- **Statement.** Every undominated model on U is coherent.
- **Meaning.** The ranking leaves nothing incoherent undominated.
- **Scope.** One ranking (all worlds), relative to the models on U. It concerns **the ranking and the coherent class**, not the target.
- **Status.** Requirement. Proved in Theorem 6.8(a) (on E), Corollary 7.1(c) (on U) and Theorem 8.1(b). **Never a premise** (check 1).

#### B5. Closure under ties — requirement (3)
- **Statement.** A model tied at every world with an undominated coherent model is itself undominated and coherent.
- **Meaning.** The ranking cannot fail to distinguish an incoherent model from an undominated coherent one.
- **Scope.** One ranking. Ranking and coherent class.
- **Status.** Requirement. Proved in Theorem 6.8(e) (distinct models are never tied), Corollary 7.1(c),(d) and Theorem 8.1(c). It is identical in wording to LDG's "closed under ties" (LDG L109).

#### B6a. The target lies in the domain — first half of requirement (4)
- **Statement.** D_K ⊆ U a.e.
- **Scope.** Domain and target. **It does not involve the ranking.**
- **Status.** Requirement. Automatic on E. On D_{K'} it is equivalent to K' ⊆ K, under M3 (Proposition C.1). For veto–Brier it is proved in Step 9 of Appendix D, but it is not stated in Theorem 8.1 (revision R10).
- **Used as a necessary condition** in Corollary 7.1(d) and Proposition C.1(a).

#### B6b. The target is undominated — second half of requirement (4)
- **Statement.** D_K is undominated among the models on U.
- **Scope.** One ranking and the target.
- **Status.** Requirement. Proved via Proposition 6.6 (protection) for Definition 6.1, and in Theorem 8.1(c), Step 8.
- **Note.** Only the *target* must be undominated. Coverage does not require every coherent model to be undominated. That is protection, D7 below, a property of this construction. Compare check 4.

#### B7. Incoherent-model dominance — requirement (5)
- **Statement.** Every incoherent model on U is dominated by an undominated coherent model.
- **Scope.** One ranking. Ranking and coherent class.
- **Status.** Requirement. Proved in Theorem 6.8(b) (uniformly), Corollary 7.1(c) and Theorem 8.1(c). **Never a premise** (check 1).

#### B8. Local freedom — requirement (6)
- **Statement.** Some open set containing ∂D_K ∖ {0} lies in U a.e.
- **Meaning.** The target can be perturbed near its boundary within the domain. So its undominatedness is not an artefact of forbidding nearby models (L979–981).
- **Scope.** Domain and target. **It does not involve the ranking.**
- **Status.** Requirement. Automatic on E. Characterised on one-sided domains in Proposition C.1, under M3. Proved for veto–Brier in Theorem 8.1(d).
- **Used as a necessary condition** in Corollary 7.1(d) and Proposition C.1(a),(c).

#### Which requirements concern what

| | Ranking alone (world by world) | Ranking's dominance structure on the models on U | Ranking and target | Domain and target only |
|---|---|---|---|---|
| Items | B1, B2, B3 | B4, B5, B7 | B6b | B6a, B8 |

#### Relation to LDG's "dominance property"
- LDG's dominance property says every evaluable model is weakly dominated by an undominated coherent model.
- That property together with B5 implies B4 and B7 (LDG Proposition 6.1(a)).
- The converse fails as a matter of logic. B4 and B7 say nothing about weak dominators of *dominated coherent* models; LDG Example 6.2 shows the abstract pattern.
- All three rankings in this paper nonetheless have LDG's property:
  - Theorem 6.8(c);
  - Corollary 7.1(c), via Theorem 6.8(c) on U;
  - Theorem 8.1(b), first sentence, together with (c).
- See Part 4.

---

### C. The construction's additional commitments

These items characterise **this** construction. They are not requirements on covering rankings: the veto–Brier ranking covers its target and violates C2(ii) and C2(iii) (see E3).

#### C1. The rule (Definition 6.1)
- **Statement.** X ⪯_ω Y if and only if the change from Y to X either (i) is guided by ω, or (ii) could be made by no coherent model and m_ω(X) > m_ω(Y).
- **Meaning.** Accept a change if it only corrects errors at ω. Otherwise accept it only if it strictly improves integrated payoff at ω **and** no coherent model could make it.
- **Scope.** One world. Availability does not depend on the world; guidance and the score do.
- **Status.** Defined.
- **Note.** The clause "could be made by no coherent model" refers to the coherent class (A11). The paper says so (L185–187, L1232–1235). This clause is why the result *represents* coherence rather than *deriving* it.
- **On restricted domains (§7).** Clause (ii) reads "no coherent model on U". Corollary 7.1(a) shows this is the same condition when U is closed under coherent hulls, which is a sufficient hypothesis of Corollary 7.1.

#### C2. Maximality characterisation (Proposition 6.3)
- **Statement.** For fixed ω and m_ω, ⪯_ω is the largest relation R on models such that:
  - (i) **guided comparisons are accepted:** if the change from Y to X is guided by ω, then X R Y;
  - (ii) **accepted comparisons between distinct models strictly improve the score:** if X R Y and X ≠ Y a.e., then m_ω(X) > m_ω(Y);
  - (iii) **changes available to a coherent model are accepted only through guidance:** if X R Y and some coherent model could make the change from Y to X, then that change is guided by ω.
- **Scope.** One world.
- **Status.** Proved. It is a *characterisation*, not an assumption of any theorem. Only M1 is used.
  - The containment half uses only (ii) and (iii). So ⪯_ω is already the largest relation with (ii) and (iii), and (i) then holds automatically (L845–848).
- **Consequences to record.**
  - (ii) by itself rules out ties between distinct models: X R Y and Y R X would give m(X) > m(Y) > m(X). The no-ties property D5 is therefore built into the characterisation. It is **not** built into coverage.
  - The paper keeps this separate (L983–988).
- **FLAG: (iii) is stronger than coherent admissibility.** This is recorded, not resolved, as the guidance asks.
  - Under the instance μ{P_S = 0} = 0 of M2, condition (iii) at every world implies **protection**: every coherent model is undominated under this one ranking (§9.2, L1252–1255).
  - Protection is itself stronger than LDG's coherent admissibility, which asks only that each coherent model be undominated under *some* ranking in a family.
  - (iii) is stronger still, in two ways:
    - (a) It constrains single-world comparisons even against a coherent model, short of weak dominance. In Example 6.4, X ⪯₁ C fails, although the change improves the score at world 1, because C could make it and it is not guided.
    - (b) It constrains comparisons between incoherent models.
  - Its independent justification is open (§9.2, L1256; open questions, L1303–1307).
- **Discussion slip.** L1227–1229 says that properties (2) and (3) "protect coherent models". The §9.2 argument uses only (3). See R5.

---

### D. Properties proved about the construction (Definition 6.1)

All of these are **proved**. None is assumed. The hypotheses listed are those actually used in the proofs.

| # | Property | Exact statement | Proved in | Uses |
|---|---|---|---|---|
| D1 | Reflexivity; a.e.-equal models tied | each ⪯_ω is reflexive, and X = Y a.e. ⇒ tied | Prop 6.2(a) | none beyond definitions |
| D2 | Independence | B2 | Prop 6.2(a) | — |
| D3 | Score monotonicity | X ⪯_ω Y and X ≠ Y a.e. ⇒ m_ω(X) > m_ω(Y) | Prop 6.2(b) | M1 |
| D4 | Strict guidance | B1 | Prop 6.2(b) | M1 |
| D5 | **No ties between distinct models** | X, Y tied at ω ⇒ X = Y a.e. | Prop 6.2(b); Thm 6.8(d) | M1 |
| D6 | Chain consistency, hence the three-model condition; also every cycle consists of a.e.-equal models | B3 and more | Prop 6.2(b) | M1 |
| D7 | **Disjoint additivity** | X ⪯_ω Y, Y ⪯_ω Z and (X△Y) ∩ (Y△Z) null ⇒ X ⪯_ω Z | Prop 6.2(c) | M1; Lemma 2.7 |
| D8 | Protection (strong form) | no coherent model has a weak dominator other than itself | Prop 6.6 | μ{P_S = 0} = 0; separability via Lemma 2.1(f) |
| D9 | All dominance is strict | for Y ≠ X a.e.: weak dominance ⇔ dominance ⇔ strict dominance ⇔ [no coherent model could make the change and the score rises at every world] | Prop 6.7 | μ{P_S = 0} = 0 |
| D10 | Repair | every incoherent X has a coherent N = D_Q with q(m(N) − m(X)) ≥ η > 0 for all states, N ⊆ hull(X∖N), location properties, and no coherent model could make the change | Thm 5.1 | A1–A4, M1, M2 |
| D11 | Coherent domination of every incoherent model, uniformly | every incoherent X is uniformly dominated by an undominated coherent N with N ⊆ hull(X∖N) | Thm 6.8(b) | D10, D8, D9 |
| D12 | Undominated = coherent | a model is undominated iff it is coherent, iff it is a.e. equal to a coherent set of desirable gambles | Thm 6.8(a) | D8, D11; M1, M2 (the last clause uses Lem 2.3(b),(c)) |
| D13 | LDG's dominance property | every model is weakly dominated by an undominated coherent model | Thm 6.8(c) | D1, D8, D11 |
| D14 | Ties with coherent models at a single world | a model tied with a coherent model at any one world equals it a.e. | Thm 6.8(d) | D5 (coherence not needed) |
| D15 | Bijection Q ↦ D_Q onto the undominated models | distinct credal sets give distinct (a.e.-classes of) undominated models | Thm 6.8(a) | **M3** (Lem 2.3(a)) |
| D16 | Covers every credal set on E | B1–B8 with U = E | Thm 6.8(e) | D1–D6, D12, D11 |
| D17 | Restricted domains | on U closed under coherent hulls: the analogues of D1–D14 hold with "coherent model on U", and the ranking covers K iff D_K ⊆ U a.e. and local freedom holds at D_K | Cor 7.1 | M1, M2, closure under hulls |

**Shown to fail.**
- **Transitivity** and **completeness** fail in general (Example 6.4: E = ℝ², μ with Lebesgue null sets).
- Not every dominance relation has a uniform margin (Example B.1). Every incoherent model nevertheless has *some* uniform dominator (D11).
- Without the instance μ{P_S = 0} = 0, protection fails (Example B.2).

**Explicitly:** "No ties between distinct models" (D5) and "disjoint additivity" (D7) are **not requirements on every covering ranking**.
- Coverage (B1–B8) mentions neither.
- The manuscript says so for D5 (L983–988, L1187–1189). It does not say so for D7, and the introduction at L135–137 reads as if D7 were required (R3).
- The veto–Brier ranking ties distinct models (L1183–1187). It happens to satisfy D7, because it is transitive. The reason it satisfies D7 is not that coverage asks for D7.

---

### E. The structured example: veto–Brier rankings (§8, Theorem 8.1, Appendix D)

#### E1. Its own assumptions (stated in Theorem 8.1; none is used in §§2–7)
- Ω = {1, …, n} with **n ≥ 2**, so E = ℝⁿ and S = Δ.
- μ is a finite Borel measure on ℝⁿ **with the null sets of Lebesgue measure** and ∫‖h‖ dμ < ∞. By Lemma 2.2 this gives M1–M3. It also makes μ **non-atomic**, which Lyapunov's theorem needs.
- p ∈ relint Δ and 0 < ε ≤ 1. The target is K = (1 − ε)p + εΔ = conv{v₁, …, v_n}, with veto points v_i = (1 − ε)p + εe_i.
- The domain is U = {h : p·h > 0} = D_{{p}}, an open half-space, closed under coherent hulls.
- The ranking at world i is the lexicographic order of (a_i, b_i), lower being better, where:
  - a_i(X) = ∫_X [−v_i·h]⁺ dμ is the veto;
  - b_i(X) = −m_i(X).
- Tools used in the proof: Lyapunov's convexity theorem (Step 3), **Zorn's lemma** (Step 4), finite-dimensional separation (Rockafellar Thm 11.3; Step 5), the Fubini argument of Lemma 2.2 (Step 6), and the geometry of Proposition C.1(b) (Step 9).
- **No leakage into the main theorem.** Theorems 5.1 and 6.8 and Corollary 7.1 use none of finite Ω, Lebesgue null sets, non-atomicity, Lyapunov or Zorn. Remark 5.2(c) says so explicitly, and I checked the proofs. Lyapunov appears outside §8 only in the motivating remark after Lemma 3.1 (L515–517) and in the delimiting Example B.1.

#### E2. Stronger ordering properties that it has (proved in Theorem 8.1(a), Step 2)
- Each ⪯_i is **complete and transitive**, a total preorder. Hence it is reflexive, chain-consistent (B3) and disjointly additive (D7, trivially from transitivity).
- It satisfies strict guidance (B1) and independence (B2).
- It covers K on U (B1–B8). It also has LDG's dominance property on U (Theorem 8.1(b), first sentence, with (c)).
- Closure under ties holds in a stronger form: a model tied with *any* undominated model is undominated and coherent.

#### E3. Properties of the universal construction that it lacks
- **No ties between distinct models** (D5) fails. By Lyapunov, a non-null Y ⊆ U splits into T and Y∖T, which are tied at every world and are distinct (L1183–1187). So Proposition 6.3(ii) fails.
- **Protection** (D8) fails. The coherent model U = D_{{p}} is dominated (Theorem 8.1(b) with Lemma 2.3(a), L1196–1197).
  - Since μ satisfies M2, Proposition 6.3(iii) would imply protection (§9.2). So **the veto–Brier ranking violates Proposition 6.3(iii)** at some world.
  - This confirms that C2(iii) is not a coverage requirement.
- **Undominated models are a proper subfamily of the coherent models on U.** Each undominated model is D_{K*} with p ∈ K* and some v_i ∈ K* (Theorem 8.1(b)).
- **Reach.** It covers one target, K, and it is built from that target. The universal ranking, restricted to the same U, covers every full-dimensional K̃ with p ∈ relint K̃ (Corollary 7.1(d) and Proposition C.1(a),(b)).
- **Margins.** Only "dominated" is proved for incoherent models (Theorem 8.1(c)). Neither strict nor uniform dominance is claimed, and the uniform margin of D11 is not available.
- It does not have the form of the rule C1, and it does not use the test "no coherent model could make this change". It does, however, encode its target through the v_i (L1205–1207).

---

## Part 2. Internal dependency table

The table lists, for every numbered result, the items it uses. Each row was checked against the proof, not only the statement. "Stated" gives the hypotheses written in the result. "Actually used" corrects them where they differ.

| Result | Stated hypotheses | Setting items actually used | Earlier results used | Discrepancy / remark |
|---|---|---|---|---|
| Lem 2.1 (states) | A2–A4 | (a) A3 (metrizability), A4 (norm 1), Banach–Alaoglu; (c) A4; (e) strict separation; (f) A3 | — | none |
| Lem 2.2 (measures exist) | A2–A4 | A3, A4; second claim: E = ℝⁿ, Lebesgue null sets, M1 | — | shows M1–M3 are jointly satisfiable |
| Lem 2.3 (identify) | (a) M3; (b) last sentence M2; (c) M2 | (b) first part: A4 (D_S open, 1 ∈ D_S), Hahn–Banach, bipolar | 2.1(c),(e) | none |
| Lem 2.4 (hull) | (b) 2nd sentence, (c) converse, (d): M2 | (a),(b) A3 via 2.1(a); (c) A4 (−1 ∉ D_Q); (d) M1, M2 (singleton instance) | 2.1(a) | none |
| Def 2.5 (change) | — | A10 | — | — |
| Lem 2.6 (test) | M2 | M2 (Q_B instance) | 2.4(b),(c) | none |
| Lem 2.7 (join) | — | A10 | — | none |
| Lem 3.1 (minimax) | M1, M2 | A6 (finite: L∞ = (L¹)*), A3 (Bochner), M1, M2 (singleton instance) | 2.1(a); Sion | none |
| Cor 3.2 | M1, M2 | M1, M2 | 3.1, 2.4(b), 2.1(c) | none |
| Cor 3.3 | M1, M2 | M1, M2 | 3.1, 2.4(a),(d) | none |
| Lem 4.1 (contraction) | — | — | 2.4(a) (Q_X closed) | none |
| Lem 4.2 (trim) | — | **no M2** (uses only the first sentence of 2.4(b)) | 4.1, 2.1(d), 2.4(a),(b) | none |
| Lem 4.3 (change) | M2 | M1, M2 | 2.4(c),(d) | none |
| Rem 4.4 | Gaussian on ℝ² | M1–M3 | 2.1(e), 2.4(c), 2.6 | example |
| **Thm 5.1 (repair)** | A1–A4, M1, M2 | A1–A4, A6, M1 (dominated convergence), M2 | 3.1, 3.2, 3.3, 4.2, 4.3, 2.6, 2.4(a)–(c), 2.1(c),(d) | no M3, Lyapunov or non-atomicity (Rem 5.2(c), verified) |
| Def 6.1 (ranking) | — | A11, A12, A13 | — | — |
| Prop 6.2 (structure) | none stated | **M1 only** | 2.7 | none. Its (b) gives B1, B3, D5; its (c) gives D7 |
| Prop 6.3 (maximality) | none stated | **M1 only** (L849, verified) | 6.2(b) | containment uses only (ii), (iii) |
| Ex 6.4 (intransitive) | E = ℝ², Lebesgue null sets, M1 | M1–M3 via 2.2 | 2.6 | witnesses failure of transitivity and completeness |
| Lem 6.5 (guided everywhere) | "M2" | **only μ{P_S = 0} = 0**; A3 via 2.1(f) | 2.1(c),(f) | over-stated hypothesis (harmless; R9) |
| Prop 6.6 (protection) | "M2" | **only μ{P_S = 0} = 0** | 6.5; clause structure of 6.1 | as above |
| Prop 6.7 (strict) | "M2" | **only μ{P_S = 0} = 0**; M1 | 6.2(b), 6.5 | as above |
| **Thm 6.8 (main)** | A1–A4, M1–M3 | M1, M2; **M3 only for the bijection in (a)** | 5.1, 6.2, 6.6, 6.7, 2.3(a)–(c) | disclosed at L1010–1011 and L1015. (e): B1–B3 from 6.2; B4 and B6b from (a); B5 from 6.2(b); B7 from (b); B6a and B8 trivial on E |
| Cor 7.1 (domains) | M1, M2; U closed under coherent hulls | same | 2.6, 5.1(3) (location), 6.2–6.7, 6.8(b)–(d) | (d) 2nd sentence uses only B6a and B8 of an *arbitrary* covering ranking |
| **Thm 8.1 (veto–Brier)** | n ≥ 2, E = ℝⁿ, Lebesgue null sets, M1, p, ε, U | non-atomicity; Lyapunov; Zorn; separation; Fubini argument of 2.2; C.1(b) geometry | — (does **not** use 5.1 or 6.1–6.8) | B6a proved in Step 9 but missing from the statement (R10) |
| Ex B.1 (non-uniform) | Ω = (0, 1], two-dimensional E, Gaussian | M1–M3; Lyapunov–Lindenstrauss | 2.6, 6.7 | delimits D11 |
| Ex B.2 (P_S essential) | M1, M3; M2 fails | — | 6.1 | shows the Q = S instance of M2 is essential for D8 |
| Rem B.3 (order unit) | inf e > 0 | A2–A4 transferred | all | — |
| Prop C.1 (one-sided) | M1–M3 | M3 through 2.3(a) | 7.1(d), 2.3(a), 2.1(c),(e); Rockafellar 11.6 | necessity claims in (a),(c) use only B6a and B8 |

Unnumbered results that carry assumptions:
- The Walley-versus-μ example (L342–350) delimits Lemma 2.3(b) without M2.
- The point-mass example (L352–354) shows that without M3, Q ↦ D_Q is not injective.
- The mutually singular measures (L1271–1279) show that incoherence depends on μ.

---

## Part 3. The four decisive checks

### Check 1. Does any proof assume a dominance claim it is meant to establish?

**Answer: No.**

**(a) The main chain is non-circular.**
- Theorem 6.8(b) uses Theorem 5.1, Proposition 6.7 and Proposition 6.6.
- Theorem 5.1 uses only §§2–4: the minimax lemma, the hull lemmas, trimming and Lemma 4.3. None of these mentions the ranking.
- Proposition 6.6 uses only Lemma 6.5 and the clause structure of Definition 6.1.
- Theorem 6.8(a) uses Proposition 6.6 together with (b).
- Theorem 6.8(c) uses Proposition 6.6, (b) and reflexivity (Proposition 6.2(a)).
- No step assumes that some model is dominated or undominated, except for coherent models after Proposition 6.6 has proved it.
- Theorem 8.1 is self-contained. Undominated weak dominators come from Zorn (Step 4) and coherence from separation (Steps 5–7). Step 8 derives closure under ties and incoherent-model dominance from Steps 3, 4 and 7.

**(b) Where "global coherence" and "every incoherent model is dominated" occur.**

| Occurrence | Role |
|---|---|
| L141–143, L146–148 (introduction) | description of what is proved; L146–148 explicitly says "proved, not assumed" |
| L970, L974 (definition of coverage) | **requirements in a definition**; not a premise of any result |
| Theorem 6.8(a), (b), (e) (L996–1009, L1024–1025) | **conclusions** |
| Corollary 7.1(c), (d) (L1050–1052, L1074) | **conclusions** |
| Theorem 8.1(b), (c) (L1163–1168) | **conclusions** |
| §9.1 (L1220–1223) | summary of conclusions |

They never appear as premises. The only results that take "R covers K" as a *hypothesis* about an arbitrary R are:
- the second sentence of Corollary 7.1(d) ("every ranking on U that covers K needs both conditions");
- Proposition C.1(a), second sentence;
- Proposition C.1(c).

Each extracts only B6a and/or B8, which concern the domain and the target. These are necessity results, valid by definition, and they use no dominance claim.

**(c) Does the definition of a ranking on a domain import properties LDG does not assume? Is it justified?**

*Yes, it imports exactly one property: reflexivity.*
- The definition (L956–958) requires "a reflexive relation … under which a.e.-equal models are tied".
- The two clauses say the same thing:
  - Since every model is a.e. equal to itself, "a.e.-equal models are tied" gives X ⪯ X, which is reflexivity.
  - Conversely, models are identified up to null sets (A10), so a.e.-equal models are the same model and the tie is just reflexivity. Even reading representatives literally, reflexivity together with independence (B2) gives the tie clause: the change between a.e.-equal models is the null change, which is the change from X to X.
- LDG explicitly does not assume reflexivity (LDG L58: "they need not be reflexive, transitive or complete").

*Is it used?* No result in the application uses reflexivity of an arbitrary ranking on U.
- The only statements about arbitrary covering rankings (listed in (b)) use B6a and B8 alone.
- Reflexivity of the paper's own rankings is used, in Theorem 6.8(c) ("a coherent model weakly dominates itself"), but there it is *proved* (Proposition 6.2(a); Theorem 8.1(a)).

*Is it justified?* It is harmless but not justified by anything in the paper, and it has a small cost.
- It is harmless because both rankings studied have it, so no theorem about them changes.
- It is not needed: nothing uses it.
- The cost: the necessity claims ("no ranking on U covers K unless …", Corollary 7.1(d) and Proposition C.1(a),(c)) quantify over rankings on U. Building reflexivity into "ranking on U" narrows the class they cover, so it **weakens those results for no gain**.
- It also creates a gratuitous difference from LDG, where the same paper pair stresses that the general results assume no order properties.

*Recommendation:* drop the clause and define ≺ and "tied" for arbitrary rankings there (R1, option A). If the authors prefer to keep it, add one sentence saying it is a convention, that LDG does not assume it, and that no result uses it (R1, option B). This is not a circularity issue.

### Check 2. Does any construction-specific restriction masquerade as a general accuracy axiom?

**Answer: not in any definition or theorem statement, but in three places of prose.**

*Clean.*
- Coverage requirement (1) contains only strict guidance, independence and chain consistency.
- L983–988 disclaims "every cycle consists of a.e.-equal models" and no-ties as construction-specific, and L1187–1189 uses the veto–Brier ties to justify that.
- Proposition 6.3 is presented as a characterisation of this ranking ("What singles out the ranking …", L816–819), not as axioms.
- The score is fixed, and no claim is made for other scores (L1292).

*Leaks.*
1. **Introduction, L133–137.** "The ranking satisfies strict guidance by the truth, independence, acyclicity … and disjoint additivity. It also has a property that the general argument does not require: it has no ties between distinct models." Flagging only no-ties implies that **disjoint additivity is required**. It is not: it is absent from coverage. (R3)
2. **Introduction, L175–177.** "a ranking meeting the constraints we impose on accuracy rankings can achieve the coverage property". "The constraints we impose" is unspecified. Following directly after the maximality sentence (L137–140), it can be read as Proposition 6.3(i)–(iii), which are construction-specific; (ii) builds in no-ties and (iii) is the open restriction. The intended referent is requirement (1). (R4)
3. **Discussion, L1215–1217.** This lists strict guidance, independence, acyclicity, disjoint additivity and no-ties together, without separating what coverage requires from what the construction adds. (R6)

*A structural point to make explicit.*
- Proposition 6.3(ii) forbids ties between distinct models, and (iii) forces protection under M2.
- The veto–Brier ranking violates both and still covers its target (E3).
- This is the cleanest evidence that neither is a general accuracy axiom. The manuscript does not draw this inference, so adding it is worthwhile (R5).

### Check 3. Does any sufficient proof condition masquerade as a necessary requirement?

**Answer: No, in the manuscript.** (The preliminary list contains one such overclaim; see Part 6.)

| Condition | How the manuscript presents it | Verdict |
|---|---|---|
| Closure under coherent hulls (Cor 7.1) | a hypothesis of the corollary; domains not closed under hulls are an open question (L1301) | correctly sufficient |
| M3 in Theorem 6.8 | in the headline hypotheses, but the theorem says that only the bijection uses it (L1010–1011); Intro scope item (3) agrees | correctly disclosed |
| M2 | "essential" is claimed only for the instance μ{P_S = 0} = 0 and only for protection (L911–912, L1285–1286); the identification role is supported by the L342–350 example | correct. But "Assume (M2)" in Lemma 6.5 and Propositions 6.6–6.7 over-states what is used (R9, optional) |
| Separability | used, not claimed necessary (open question, L1297) | correct |
| Order unit | "some condition like the second … is needed" (L1267–1269), with an argument | correct, and appropriately hedged |
| Lebesgue null sets, finite Ω (§8) | hypotheses of Theorem 8.1 only | correct |
| Local freedom (B8) | part of the *definition* of coverage, motivated at L979–981; Cor 7.1(d) "needs both conditions" is true by definition and presented as such | correct; it is a definitional choice, not a hidden hypothesis |
| Chain consistency (B3) | chosen as "the appropriate consistency requirement" (L983–984) and argued for via veto–Brier | a definitional choice, openly argued |

### Check 4. Are admissibility under *some* ranking and under *every* ranking kept distinct?

**Answer: mostly yes; one wording slip in §9.2 and one in the open questions.**

Three distinct conditions are in play:
1. **Target undominatedness (B6b):** D_K is undominated under the ranking being assessed. This is all that coverage of K needs.
2. **Protection (D8):** every coherent model is undominated under *this* ranking. This is a proved property of Definition 6.1, not a coverage requirement. The veto–Brier ranking lacks it.
3. **Coherent admissibility (LDG L456):** every coherent model is undominated under *at least one* ranking in a family. It does **not** require undominatedness under every ranking. For a one-member family it coincides with (2).

Assessment of the manuscript:
- The coverage definition and Theorems 6.8 and 8.1 keep (1) and (2) apart.
- Nothing in the application asserts or assumes (3) at the family level.
- §9.2 (L1250–1251) says "coherent admissibility, in the sense used for families of rankings: every coherent model is undominated (here, for a single ranking)". The parenthesis rescues the logic, but the sentence states the family notion in a form ("every coherent model is undominated") that omits "under some ranking". A reader can take it as "under every ranking". (R5)
- The open question (L1303–1305) asks whether (3) of Proposition 6.3 can be weakened "to coherent admissibility … while preserving coverage of every coherent target". This leaves open whether *one* ranking or a *family* should cover every target:
  - If one ranking must cover every target, the relevant weakening is protection (2).
  - If a family may share the work, family-level coherent admissibility (3) is enough for admissibility, and the veto–Brier construction already suggests one ranking per target.

  (R5)
- LDG echoes the slip at LDG L510 ("coherent admissibility, which asks only that coherent models remain undominated"). It should add "under some ranking". This is outside the application, but I note it for the LDG auditor.

---

## Part 4. Terminology mismatch with LDG

### 4.1 "The dominance property"
- **LDG (L105, L44, L52):** "every evaluable model is weakly dominated by an undominated coherent model of L". It is never assumed, and it is derived by Theorems 3.2, 3.3, 4.1 and 4.6 or reduced by Proposition 7.1(c).
- **Application, L961–962:** "Conditions (2)–(5) are the dominance property". These conditions are global coherence, closure under ties, the target, and incoherent-model dominance.
- **Application elsewhere:** the phrase is used in LDG's sense, or ambiguously:
  - L151, "Together they give the dominance property (Theorem 6.8)": ambiguous.
  - L1238 and L1244 describe LDG: these are in LDG's sense.
  - L59, "without assuming any dominance property": generic.
- So the application uses the term in **two senses**, and one of them conflicts with LDG.

**The two notions are logically different.**
- (2)–(5) include a target clause (4) and a ties clause (3), neither of which is in LDG's property.
- LDG's property, together with closure under ties, yields (2) and (5) (LDG Proposition 6.1(a)).
- (2) and (5) do not yield LDG's property: they are silent about weak dominators of dominated coherent models (LDG Example 6.2 is the abstract pattern).

**Recommended fix.** Keep "dominance property" exclusively in LDG's sense in both papers, and rename the application's (2)–(5).
1. L961–962: replace "Conditions (2)--(5) are the dominance property: they describe what a covering ranking must achieve, not what it is assumed to satisfy." with the R1 text, which calls (2)–(5) "the **dominance requirements** of coverage".
2. After the list of requirements (after L981), add:
   > The dominance requirements differ from the dominance property of the companion paper \cite{KCMcompanion}, that every model on $U$ is weakly dominated by an undominated coherent model. That property, with closure under ties, gives (2) and (5) \cite[Prop.~6.1]{KCMcompanion}; but (2)--(5) say nothing about weak dominators of coherent models that are dominated, and (4) concerns one target. Every ranking studied below has both: see Theorem~\ref{thm:main}(c), Corollary~\ref{cor:domains}(c) and Theorem~\ref{thm:vb}(b),(c).
3. L151: replace "Together they give the dominance property (Theorem~\ref{thm:main})." with
   > Together they give the dominance property in the sense of the companion paper \cite{KCMcompanion}: every model is weakly dominated by an undominated coherent model (Theorem~\ref{thm:main}(c)).
4. After the proof of Theorem 6.8 (after L1026), optionally add: "Part (c) is the dominance property of \cite{KCMcompanion}."
5. L1238 and L1244 can stay as they are, since they are already in LDG's sense once item 1 is made.

An alternative would be to rename LDG's term. I advise against it: "dominance property" is LDG's central defined notion, used throughout its abstract, introduction and §§3–7.

### 4.2 Other cross-paper terms (checked)

| Term | LDG | Application | Status / action |
|---|---|---|---|
| ranking | evaluation domain M_L plus a relation per world; **no properties assumed** (L58) | "ranking on U": reflexive, a.e.-equal models tied (L956–958) | mismatch; see check 1(c) and R1 |
| evaluable / evaluation domain | M_L | "models on U" | consistent in substance; R1 adds one cross-reference |
| ≺, tied | defined for every ranking (L58) | defined only inside Def 6.1 (L758–759), then used generally in §6.3 | move the definitions (R1) |
| dominates / strictly / undominated | L62–67 | L888–892 | consistent (equivalent definitions of "dominates") |
| uniformly dominates | loss rankings, with a finite-loss margin (L76) | strict dominance plus a score margin (L891) | compatible; no action |
| closed under ties / closure under ties | L109 | requirement (3), L971 | identical |
| coherent admissibility | family-level, "some ranking" (L456) | §9.2 and open questions, applied to one ranking | R5 |
| cycles / acyclicity | Prop 7.1(a): "every cycle consists of equal models" (the *stronger* property) | "acyclicity" = the chain condition (the *weaker* property, L968, L983) | the same word sits near two different strengths; rename to "chain consistency" (R7) |
| guided changes improve the score; guidance protects coherent models | the two conditions of Prop 7.1 | Prop 6.2(b); Lemma 6.5 with Prop 6.6 | consistent; add an explicit mapping (R12) |
| the change; available to | Prop 7.1 data | Def 2.5 | consistent. Definition 6.1 is an instance of LDG Prop 7.1 (L1241–1243 says so), and Thm 5.1 supplies its (c)(ii) |

---

## Part 5. Ranked list of manuscript revisions

The revisions are ranked by how much they affect the logical reading of the paper. Line numbers refer to `r69/…gambles.tex`. LaTeX replacement text is given where it is possible. None of it adds an assumption.

### R1 (highest). Rewrite the preamble to the definition of coverage (L955–964)

*Problem.*
- It calls (2)–(5) "the dominance property", which clashes with LDG.
- It implies that (1) is assumed while (2)–(5) are achieved, although all six are requirements that must be proved.
- It imports reflexivity.
- It uses ≺ and "tied" for arbitrary rankings, although they are defined only for Definition 6.1.

*Replacement, option A (preferred; aligns with LDG).* Replace from "and a \emph{ranking on $U$} assigns …" (L956) through "… A ranking on $U$ \emph{covers} $K$ if:" (L964) with:

```latex
and they form the evaluation domain in the sense of \cite{KCMcompanion}. A \emph{ranking on
$U$} assigns to each world $\omega$ a relation $\preceq_\omega$ on the models on $U$. We write
$X\prec_\omega Y$ if $X\preceq_\omega Y$ and not $Y\preceq_\omega X$, and call $X$ and $Y$
\emph{tied} at $\omega$ if each is at least as good as the other; the dominance notions of
Section~\ref{sec:ranking} apply to any ranking on $U$. As in \cite{KCMcompanion}, no property of
the relations is assumed beyond those listed in requirement~(1). We now say what it means for a
ranking to cover a target credal set $K$. Each requirement below is something that a proof of
coverage must establish; none of them is a hypothesis of any result in this paper.
Requirement~(1) concerns each world's relation on its own: strict guidance is a form of
truth-directedness \cite{Joyce}, and independence is a form of additivity across gambles
\cite{Pettigrew}. Requirements~(2), (3) and~(5) concern the dominance relations that the ranking
induces on the models on~$U$, and~(4) relates them to the target; we call (2)--(5) the
\emph{dominance requirements}. Requirement~(6) concerns only the domain and the target. For the
ranking of Definition~\ref{def:ranking}, Theorem~\ref{thm:main} proves all six. A ranking on $U$
\emph{covers} $K$ if:
```

*Option B (keeps reflexivity).* Use the same text, but replace its third and fourth sentences ("We write … apply to any ranking on $U$. As in … requirement~(1).") with:

```latex
... a reflexive relation $\preceq_\omega$ on the models on $U$; since models equal a.e.\ are
identified, reflexivity says that a.e.-equal models are tied. The companion paper
\cite{KCMcompanion} assumes no property of the relations, not even reflexivity. We include it
only because both rankings studied here have it; no result below about arbitrary rankings on $U$
uses it.
```

Option B keeps the narrowing of the necessity claims in Corollary 7.1(d) and Proposition C.1(a),(c). Option A removes it.

### R2 (high). The term "dominance property" elsewhere
Apply items 2–4 of §4.1: a new paragraph after L981, the replacement at L151, and the optional note after Theorem 6.8.

### R3 (high). Introduction L133–137: stop presenting disjoint additivity as required
Replace "The ranking satisfies strict guidance by the truth, independence, acyclicity (no chain of weak comparisons ends in a strict reversal) and disjoint additivity. It also has a property that the general argument does not require: it has no ties between distinct models (Proposition~\ref{prop:structure})." with:

```latex
The ranking satisfies strict guidance by the truth, independence and acyclicity (no chain of
weak comparisons ends in a strict reversal), which are all that coverage asks of each world's
comparisons (Section~\ref{sec:undominated}). It also has two properties that coverage does not
require: disjoint additivity, and the absence of ties between distinct models
(Proposition~\ref{prop:structure}).
```

### R4 (high). Introduction L175–177: name the constraints
Replace "that a ranking meeting the constraints we impose on accuracy rankings can achieve the coverage property of Section~\ref{sec:undominated} for every credal set, so that it represents coherence exactly." with:

```latex
that a ranking satisfying strict guidance, independence and acyclicity, the requirements that
coverage places on each world's comparisons, can cover every credal set in the sense of
Section~\ref{sec:undominated}, so that it represents coherence exactly.
```

### R5 (high). Separate protection from coherent admissibility, and (3) from (2)

*(a) L1227–1229.* Replace "Under (M2), properties (2) and (3) of Proposition~\ref{prop:maximal} protect coherent models, but …" with "Under (M2), property (3) of Proposition~\ref{prop:maximal} alone protects coherent models (Section~9.2), but …".

*(b) L1250–1258.* Replace from "A weaker, global requirement would be coherent admissibility, …" to the end of the paragraph with:

```latex
A weaker, global requirement is protection: every coherent model is undominated under this
ranking. Weaker still is coherent admissibility in the sense of \cite{KCMcompanion}, a condition
on a family of rankings: every coherent model is undominated under at least one ranking in the
family, not necessarily under every one. For the one-member family consisting of this ranking,
coherent admissibility is protection. Under the instance $\mu\{P_S=0\}=0$ of (M2), property (3)
implies protection: if (3) holds at every world and $Y$ weakly dominates a coherent model $C$,
then the change from $C$ to $Y$, which $C$ itself could make, is guided by every world, so $Y=C$
a.e.\ by Lemma~\ref{lem:guidedeverywhere} and the proof of Proposition~\ref{prop:protect}. But
(3) is stronger. It constrains comparisons at a single world, including comparisons with a
coherent model that fall short of weak dominance (in Example~\ref{ex:intransitive}, $X\preceq_1C$
fails although the change raises the score at world~$1$), and comparisons between incoherent
models. It is not needed for coverage: the veto--Brier ranking of Section~\ref{sec:vb} covers its
target, yet the coherent model $U=D_{\{p\}}$ is dominated there, which (3) would forbid. Its
independent justification remains open.
```

*(c) Open question, L1303–1305.* Replace with:

```latex
\item The third condition: can property (3) of Proposition~\ref{prop:maximal} be weakened, for
instance to protection together with other independently motivated conditions, while a single
ranking still covers every coherent target? If a family of rankings may share the work,
coherent admissibility in the sense of \cite{KCMcompanion} is the relevant weakening.
```

### R6 (medium). Discussion L1215–1217
Replace "The ranking built from this distinction satisfies strict guidance, independence, acyclicity and disjoint additivity, and has no ties between distinct models (Proposition~\ref{prop:structure});" with:

```latex
The ranking built from this distinction satisfies the requirements that coverage places on each
world's comparisons (strict guidance, independence and acyclicity), and two properties that
coverage does not require, disjoint additivity and the absence of ties between distinct models
(Proposition~\ref{prop:structure});
```

### R7 (medium; optional). Rename "acyclicity" to "chain consistency"
- *Locations:* L135, L780, L968, L983, L1161 ("hence acyclic" becomes "hence chain-consistent"), L1187, L1216.
- *Reason:* "Acyclicity" usually means that the *strict* part has no cycles. The paper's condition is Suzumura consistency, which is stronger. LDG's nearby phrase, "every cycle consists of equal models", is stronger still.
- *Suggested addition at L983:* "Its case $k=2$ is the three-model condition: no $A\preceq_\omega B\preceq_\omega C$ with $C\prec_\omega A$. The chain condition is known in social choice as Suzumura consistency; it is weaker than transitivity and stronger than acyclicity of the strict part."
- This changes no mathematics. If it is adopted, apply it to the R3 and R6 texts too.

### R8 (medium). §9.3 L1283–1286: list M2's roles accurately
Replace "Condition (M2) has two roles: it makes the optimal weighted choice in the minimax lemma an ordinary acceptance set, and it makes coherent sets of desirable gambles coincide with the coherent models modulo $\mu$ (Section~\ref{sec:setting}). Its instance $\mu\{P_S=0\}=0$ is essential for protection (Example~\ref{ex:PS})." with:

```latex
Condition (M2) has three roles. It makes the optimal weighted choice in the minimax lemma an
ordinary acceptance set; it places every consistent model inside its coherent hull, which gives
the test of Lemma~\ref{lem:test} for whether a coherent model could make a change; and it makes
coherent sets of desirable gambles coincide with the coherent models modulo $\mu$
(Section~\ref{sec:setting}). Protection uses only its instance $\mu\{P_S=0\}=0$, which is
essential (Example~\ref{ex:PS}).
```

### R9 (low; optional). State the instance of M2 actually used
In Lemma 6.5 (L895), Proposition 6.6 (L915) and Proposition 6.7 (L929), replace "Assume (M2)." with "Assume $\mu\{P_S=0\}=0$ (an instance of (M2))." This is a weakening of the stated hypotheses, not a new assumption. If it is adopted, also replace "Under (M2)" with "Under this instance of (M2)" in the R5(b) text.

### R10 (low). Theorem 8.1(d): include the containment of the target
Replace L1169, "$U$ is open and contains $\partial D_K\setminus\{0\}$, so local freedom holds at $D_K$.", with:

```latex
$D_K\subseteq U$; and $U$ is open and contains $\partial D_K\setminus\{0\}$, so local freedom
holds at $D_K$.
```

This makes requirement (4)'s first half explicit. It is already proved in Step 9 ("Since $p\in K$, $D_K\subseteq U$").

### R11 (low). Notation clash in §8
At L1200–1201, "every full-dimensional credal set $K'$ … with $p\in\relint K'$" uses K' for a *target*. Proposition C.1, which it cites, uses K' for the *domain's* credal set. Rename it to $\tilde K$.

### R12 (low). Make the instance of LDG's construction explicit
At L1242–1243, after "the ranking of Definition~\ref{def:ranking} is an instance of that construction", add:

```latex
its two conditions on guidance are Proposition~\ref{prop:structure}(b) (guided changes improve
the score) and Lemma~\ref{lem:guidedeverywhere} with Proposition~\ref{prop:protect} (guidance
protects coherent models), and the improvements it asks for are supplied by
Theorem~\ref{thm:repair}.
```

---

## Part 6. Corrections to the preliminary list (`r70/Axioms_in_each_paper.md`, application half and cross-paper section)

The LDG half was not audited. Per instruction, LDG was consulted for terminology only. The LDG-terminology claims that I did check (the definition of the dominance property, closure under ties, "no property of the relations", Proposition 7.1(a) reflexivity) are correct.

| Preliminary claim | Correction |
|---|---|
| A: M2 "Essential (Example B.2)" | Overclaim. Example B.2 shows only that the **instance μ{P_S = 0} = 0** is essential, and only **for protection**. The L342–350 example shows that M2 is needed for Walley coherence to coincide with coherence modulo μ. Necessity of the full M2 for repair is neither claimed nor shown. |
| A: M2 "used for: the minimax lemma and the repair theorem; protection; identifying …" | Incomplete. M2 is also used in the hull lemma (2.4(b) second sentence, (c) converse, (d)), the test (Lemma 2.6), Lemma 4.3, Proposition 6.7 and Corollary 7.1 with its domain examples. Lemma 6.5 and Propositions 6.6–6.7 use only the Q = S instance. |
| A: M3 "Used only to make Q ↦ D_Q one-to-one … and for local freedom on one-sided domains" | Correct in substance. Add: through Lemma 2.3(a), M3 also gives one-sidedness of D_{K'} and the "D_K ⊆ U a.e. iff K' ⊆ K" step in Proposition C.1, and it is used in the §8 contrast. |
| A: omitted | μ is **finite** (needed for L∞ = (L¹)* in Lemma 3.1). Norm-closedness and the order unit each have specific jobs (A2, A4). |
| B: "Condition 3 is the substantive assumption" | Mis-labelled. Proposition 6.3(iii) is not an assumption of any theorem. It is a defining feature of the construction, characterised in a proved proposition. Call it the construction's substantive *commitment*. Calling it an "assumption" conflicts with "dominance is proved, not assumed". |
| B: omitted | Proposition 6.3(ii) by itself forbids ties between distinct models, and the containment proof uses only (ii) and (iii). |
| C: "The dominance requirements (what must be achieved …): (2) … (5)" | The manuscript calls these "the dominance property". The list renamed them silently. Make the rename an explicit manuscript change (R1, R2). |
| C: "(4) D_K is a model on U and is undominated" under dominance requirements; "(6) On the domain" | Split (4). D_K ⊆ U a.e. concerns domain and target (B6a); undominatedness concerns ranking and target (B6b). (6) concerns **domain and target**, not the domain alone. |
| C: "proved, not assumed, for Definition 6.1" applied only to (2)–(5) | All six requirements must be proved for any covering ranking, (1) and (6) included. They are proved for both Definition 6.1 and veto–Brier. |
| C″: "The veto–Brier ranking is lexicographic, complete and transitive" listed as an assumption | Only "lexicographic" is part of the definition. Completeness and transitivity are **proved** (Theorem 8.1(a)). Also missing: n ≥ 2, and the tools used (Lyapunov, Zorn, separation). |
| D: "Protection (Prop 6.6) and dominance is always strict (Prop 6.7), under (M2)" | They use only μ{P_S = 0} = 0. |
| D: Coverage (Thm 6.8) list | Add (c), LDG's dominance property, and (d), ties at a single world. Note that M3 is used only for the bijection. |
| D: Prop 6.2 | Correct. Add that it uses only M1. |
| "Not used anywhere in the main results … Lyapunov's theorem (it appears only in the veto–Brier appendix)" | **False as stated.** Lyapunov is also used in the proof of Example B.1 and mentioned in the remark after Lemma 3.1. The main results (Theorems 5.1 and 6.8, Corollary 7.1) indeed do not use it (Remark 5.2(c)). Zorn's lemma is used only in Appendix D. |
| Cross-paper 1: "The difference is harmless, since the application's own ranking is proved reflexive" | True but incomplete. The tie clause is equivalent to reflexivity; it is unused; and it narrows the class over which the necessity results quantify, weakening them. Recommend dropping it (R1, option A). |
| Cross-paper 2: suggested rename to "dominance requirements" | Agreed. Add that (2)–(5) neither imply nor are implied by LDG's property, and that all rankings in the paper have both (§4.1). |

---

## Verification of revised manuscript (r70)

**Files checked.**
- `r70/Coherence and accuracy for sets of desirable gambles.tex` (1822 lines; PDF 28 pp.). I diffed it in full against r69.
- `r70/WA70_changes.md`.
- The revised LDG, `r70/Coherence and Dominance under General Rankings.tex`.

**Numbering.** Read from `r70/build/*.aux`.
- The application's numbering is unchanged; there are new labels `sec:dominance` = §6.2 and `sec:third` = §9.2.
- In LDG, Prop 6.1 is still `prop:conclusion` and Prop 7.1 is still `prop:construct`. Both can therefore be cited by number.
- The application log shows no warnings, undefined references or overfull boxes.

Line numbers below are r70 lines.

### V1. R1–R12

| Rev | Verdict | Notes |
|---|---|---|
| R1 option A (L1004–1022) | **Made** | Reflexivity and the a.e.-tie clause are gone. ≺ and "tied" are defined for any ranking. The dominance notions are said to apply (via the new label `sec:dominance`). The evaluation-domain link is in place, with "As in [companion], no property of the relations is assumed". The bold "to be proved" sentence is present, but its last clause is inaccurate (**F1**). |
| Split of (4) (L1032–1033) | **Made** | (4a) concerns domain and target; (4b) concerns ranking and target. Knock-on edits: Thm 6.8 proof (e) at L1097–1098 is correct; Cor 7.1(d) proof at L1149–1151 is correct ("(4b) holds whenever (4a) does, since a coherent model on U is undominated by (c)"). |
| "Dominance requirements" (L1019–1021, L1056–1061) | **Made, one slip** | The name is attached to (2), (3), (4b) and (5), as it should be. L1059 still says "(2)--(5) say nothing …", which now sweeps in (4a) (**F2**). L153 and L1101 are correct, in LDG's sense. |
| R3 (L134–139) | **Made** | |
| R4 (L179–181) | **Made** | |
| R5(a) (L1306–1307) | **Made, grammar slip** | The antecedent became singular ("property (3) … alone") but the text keeps "but they say nothing" (**F3**). |
| R5(b) (L1332–1346) | **Made** | All three conditions are separated. The single-world and veto–Brier points are present. |
| R5(c) (L1394–1396) | **Made** | |
| R6 (L1293–1296) | **Made** | |
| R7 "finite-chain consistency" | **Made** | `acycl` now occurs only in "acyclicity of the strict part" (L1049). The k = 2 and Suzumura additions are at L1046–1050. Thm 8.1(a) reads "hence finite-chain consistent". |
| R8 (L1371–1376) | **Made** | |
| R9 (L942, L963, L978) | **Made** | Correct: the proofs use only μ{P_S = 0} = 0 (re-verified). |
| R10 (L1245–1246) | **Made** | |
| R11 (L1277–1278) | **Made** | |
| R12 (L1321–1325) | **Made** | The mapping is correct against revised LDG Prop 7.1. LDG's "guidance protects coherent models" (no model other than c is reached from c by a change guided at every world) is exactly what the proof of Prop 6.6 derives from Lemma 6.5. Now that LDG's numbering is confirmed, cite the number (**F6**, optional). |

### V2. The new inventory at the start of §6 (L751–793)

**Order and placement.** The order is A–E, as required:
- (A) setting, assumed;
- (B) coverage requirements, to be proved;
- (C) construction's commitments, chosen;
- (D) proved;
- (E) veto–Brier.

It sits directly after `\section{The ranking}` and before §6.1, it is under a page, and it uses descriptive names only.

**Accuracy.**
- (A) Correct, with one exception. "no existence or dominance claim uses it [M3]" (L765) is too strong. The §8 and §9.2 statement that D_{p} is dominated under veto–Brier rests on Lemma 2.3(a), which is M3. Proposition C.1(a)'s "no ranking on U covers K unless …" also rests on Lemma 2.3(a). (**F4**)
- (B) Accurate and complete. It covers per-world, dominance and domain/target requirements, and says they are never assumed.
- (C) Accurate. All four features are listed. It says they characterise this construction only, flags the third as stronger than coherent admissibility, and points to §9.2.
- (D) Contains every item the guidance requires: reflexivity, strict guidance, independence, finite-chain consistency with the three-model case, disjoint additivity, no ties, protection, uniform coherent domination, coverage. It records the failures (Ex 6.4). One sentence justifies "not requirements" for disjoint additivity by citing veto–Brier ties, but veto–Brier *does* satisfy disjoint additivity (**F5**, recommended).
- (E) Accurate.
  - "None of these enters Sections 2–7" is true of use. The only mention of Lyapunov in §3 is the motivating remark after Lemma 3.1.

**Completeness.** It is adequate. "Undominated = coherent" and LDG's dominance property (Thm 6.8(a),(c)) are not listed separately in (D), but coverage implies the former and §6.3 states the latter. Not required.

### V3. Does dropping reflexivity break any proof or statement?

**It breaks none.** Checked:
- **Uses of "tied" and ≺ for general rankings.** Requirement (3), the §6.2 nomenclature, and Thm 8.1(c) all work without reflexivity. A model cannot dominate itself whatever the relation, because Y ≺ Y is impossible.
- **Reflexivity of the paper's own rankings.** It is used only in Thm 6.8(c) ("a coherent model weakly dominates itself"), and there it is *proved* (Prop 6.2(a)). Veto–Brier is complete, hence reflexive (App. D, Step 2). Nothing in the coverage proofs for either ranking needs reflexivity as a requirement.
- **Necessity results, now over the wider class.**
  - **Cor 7.1(d)**, second sentence ("Every ranking on U that covers K needs both conditions"). This holds by definition, because (4a) and (6) are listed requirements. No property of the relations enters.
  - **Prop C.1(a)**, second sentence ("No ranking on U covers K unless …"). The proof uses (4a), converted to K' ⊆ K via Lemmas 2.3(a) and 2.1(e), and (6), via Lemma 2.3(a) and the boundary argument. Neither uses the ranking.
  - **Prop C.1(c).** It uses only (6) and one-sidedness of the domain.

  All three hold verbatim for arbitrary relations, so they are now strictly stronger statements.
- **Well-definedness modulo null sets.** Models are identified up to null sets (A10), so a relation on models is a relation on classes. For covering rankings, independence (requirement (1)) yields invariance under a.e.-equal representatives in any case.
- The §8 claim that precise targets cannot be covered on any one-sided domain by any ranking (L1275–1276, citing C.1(c)) holds for the wider class.

### V4. The four decisive checks, re-run

1. **Circularity.** None.
   - "Global coherence" (L1029) and "incoherent-model dominance" (L1034–1035) are still only definitional requirements or conclusions: Thm 6.8(a),(b),(e), Cor 7.1(c),(d), Thm 8.1(b),(c).
   - The new inventory (B) states that the requirements are never assumed.
   - The ranking definition now imports no property absent from LDG.
   - The bold sentence's clause "none is a hypothesis of any result" is literally false. Cor 7.1(d) and Prop C.1(a),(c) take coverage as a hypothesis, to extract (4a) and (6) as necessary conditions. This is not circular, but it misdescribes those results (**F1**). The over-strong clause originated in my R1 text.
2. **Construction-specific restrictions masquerading as axioms.** None remain.
   - All three prose leaks are fixed (L134–139, L179–181, L1293–1296).
   - Prop 6.3's conditions are labelled "chosen … characterise this construction" (inventory (C)).
   - §9.2 uses veto–Brier to show that (3) is not needed for coverage.
3. **Sufficient conditions masquerading as necessary.** None.
   - R9 brings the stated hypotheses down to what is used.
   - M2's essentiality is claimed only for the P_S instance.
   - The one overstatement runs in the other direction: inventory (A)'s claim about M3 (**F4**).
4. **"Some" versus "every".** Kept distinct.
   - The new sentence after the coverage list (L1041–1044) separates target undominatedness from protection.
   - §9.2 separates protection from family-level coherent admissibility ("under at least one ranking … not necessarily under every one").
   - The open question distinguishes a single ranking from a family.
   - This matches the revised LDG: L111 ("does not require any single ranking to leave every coherent model undominated, nor any coherent model to be undominated under every ranking"), L129 and L518.

### V5. Terminology consistency with the revised LDG

| Term | Revised LDG | Revised application | Status |
|---|---|---|---|
| ranking | no properties; ≺ and tied defined (L58) | no properties; ≺ and tied defined (L1007–1011) | **consistent** |
| dominance property | every evaluable model weakly dominated by an undominated coherent model (L105) | same sense (L153, L1056–1057, L1101, L1316, L1326); (2), (3), (4b), (5) are "dominance requirements" | **consistent** |
| closed under ties | L109 | requirement (3) | identical |
| finite-chain consistency | "no chain of comparisons ending in a strict reversal", unused (L130, L514) | same gloss (L135, L1025–1027, L1046) | **consistent** |
| three-model case | named and unused (L514) | named (L1046–1047) | consistent |
| coherent admissibility | family-level, under *some* ranking (L111, L129) | family-level (L1333–1336, L1396) | **consistent** |
| guided changes improve the score / guidance protects coherent models | Prop 7.1(a),(b) (L494–495) | mapped at L1321–1325 | **consistent** |
| LDG's description of the application | "accept every guided comparison … be closed under ties …"; "the dominance property of its ranking follows, as in Prop 7.1(c)" (L518) | matches Prop 6.3 and Thm 6.8(c),(e) | consistent |

WA70 withheld the citation "[companion, Prop. 6.1]" because the numbering might change. It has not changed (Prop 6.1 = `prop:conclusion`, Prop 7.1 = `prop:construct`), so both can be cited by number (**F2**, **F6**).

### V6. Remaining fixes

**Required (F1–F4).**

**F1.** L1015–1016. Replace
"none of them is assumed, and none is a hypothesis of any result in this paper.}"
with:
```latex
none of them is assumed in proving that a ranking covers a target. The only results that take
coverage as a hypothesis, the necessity claims in Corollary~\ref{cor:domains}(d) and
Proposition~\ref{prop:onesided}(a),(c), use it only to extract (4a) and~(6).}
```

**F2.** L1058–1059. Replace
"gives (2) and (5) \cite{KCMcompanion}; but (2)--(5) say nothing"
with:
```latex
gives (2) and (5) \cite[Proposition~6.1(a)]{KCMcompanion}; but the dominance requirements say nothing
```

**F3.** L1307. Replace "but they say nothing" with "but it says nothing".

**F4.** L765. Replace "no existence or dominance claim uses it." with:
```latex
the repair theorem, the properties of the ranking, protection, the dominance results and coverage
on $E$ do not use it.
```
Optionally, change intro L172 from "every existence and dominance claim holds without it" to "every existence and dominance claim of Sections~\ref{sec:repair}--\ref{sec:domains} holds without it".

**Recommended.**

**F5.** L786–787. Replace "are not requirements on every covering ranking: the veto--Brier rankings of Section~\ref{sec:vb} tie distinct models." with:
```latex
are not among the coverage requirements; the veto--Brier rankings of Section~\ref{sec:vb}, for
instance, tie distinct models.
```

**F6.** L1321. Replace "is an instance of that construction:" with "is an instance of that construction \cite[Proposition~7.1]{KCMcompanion}:".

**Overall.** R1–R12 are implemented correctly, and dropping reflexivity is safe: it strengthens the necessity results. With F1–F4 applied, I have no outstanding objection on axiom status.
