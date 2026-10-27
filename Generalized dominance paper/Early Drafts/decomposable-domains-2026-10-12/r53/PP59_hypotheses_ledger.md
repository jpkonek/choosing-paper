# PP59. Hypotheses ledger for the round-53 module (single-world ties allowed, no gates)

23 October 2026. This is a ledger, not new mathematics. Every entry was checked against its source note and, where one exists, its referee report. Labels: CHECKED means "re-read against the source and referee; the hypotheses are as stated here". PROVED marks the two short observations in §5, which are mine. Nothing here is NUMERICS or CONJECTURE unless it says so.

---

## 0. The module the ledger is checked against

- **M1 Family.** Posterior models C_a = D_{M_a}, index = likelihood, with a ranging over a *closed* two-dimensional neighbourhood N_u of u. All indices are interior, so supp a = {1, 2, 3} everywhere. No edge or vertex index is selected. T = C_u is selected.
- **M2 Relations.** Arbitrary disagreement-based relations. (IB) applies to every installed comparison, reverses included. An acceptance need **not** come from an old-side coherent realiser. There are no gates, fields, kernels or endorsers.
- **M3 Axioms.** Reflexivity; strict (G); (IB); actual (TC) in implication form; (S) on N_u (coherent, undominated, the defence disjunction ⋁_i [C_a ⪯_i X], fixed-rival sections closed in N_u); (LA); direct (C), split into coherent and incoherent rivals.
- **M4 Ties.** Single-world ties are allowed. All-world ties are allowed only between coherent models.
- **M5 Continuity.** Nothing beyond (S). In particular, verdicts need not be closed along paths on which the rival changes, and nothing is L¹-continuous.
- **M6 Sections.** A section enters a certificate only through an actual sequence a_k → a, with the same rival and acceptance proved at every a_k.
- **M7 Scope.** Protection (undominatedness, direct (C)) is checked for the selected C_a only.

**Dependency codes** used in the table:
- **Cp:** completeness of a world's ranking;
- **Fam:** a particular family other than M1 (multicap, segments, rays, precise models, edges);
- **Gt:** gate acceptance, i.e. acceptance only through guidance or an old-side realiser's field;
- **St:** strictness or no single-world ties;
- **Ct+:** continuity beyond (S), e.g. closedness along changing-rival paths or L¹-continuity;
- **Ad:** additivity or endorsement by a field;
- **WS:** a whole-simplex selection (vertices, edges or KKM over Δ).

**Verdicts:**
- **SAFE:** the conclusion may be encoded as a derived clause in the base (ties-allowed) run.
- **TOOL:** safe, but it certifies a property of a candidate; it is not a clause.
- **COND-WS / COND-Ct+:** goes only into a separately labelled conditional run.
- **NOT SAFE:** its hypotheses fail in the module. Use it only in the "gate-derived" or "no-ties" comparison runs, or as an adversarial test.

---

## 1. Summary table

| # | Result | Hypotheses hold in module? | Extra dependencies | Verdict |
|---|---|---|---|---|
| 1 | LEAD Lemma A (tie fibres closed) | yes, relative to N_u | none | SAFE (already implied by base clauses) |
| 2 | LEAD Lemma B (C_{e_i} = V_i; V_i has no ties) | first half no; second half yes | WS (first half) | strict-(G) half SAFE; rest COND-WS |
| 3 | LEAD Theorem C (i)/(ii)/(iii) | no | WS; (ii) St | COND-WS; (ii) NOT SAFE |
| 4 | LEAD Lemma D (private witnesses countable) | yes (a measure fact) | none | SAFE as a design constraint |
| 5 | LEAD Lemma E (Φ_T inside the open simplex) | vacuous (no edges) | WS | inner (TC) step SAFE |
| 6 | Audit §1 face preservation | yes (vacuous at interior a) | none | SAFE, vacuous |
| 7 | Audit §1 tripod surjectivity | no | WS, continuity of f | COND-WS |
| 8 | Audit §2 addition lemma | yes | none | TOOL |
| 9 | Audit §3 local construction theorem | yes (it is a template) | none | TOOL |
| 10 | PP18 Theorem Z | no (KKM over Δ) | WS | COND-WS |
| 11 | PP18 Lemma Z0 | yes | none | SAFE |
| 12 | PP19 Theorem 1 | yes | none | SAFE (point form); sequence form via M6 |
| 13 | PP19 Theorem 4 | (a), (b), (c)-disjointness yes; (c)-nonemptiness, (d) no | (c) WS; (d) WS | (a), (b) SAFE; rest COND-WS |
| 14 | PP19 Theorem 5 | yes | none | SAFE |
| 15 | REFEREE_Z_PP19 Prop S | yes | none | SAFE |
| 16 | PP30 Theorem 3.1 | yes | none | SAFE (for any N, §5) |
| 17 | PP33 Theorem 3.1 | yes | none | SAFE |
| 18 | PP36 Prop K (and PP40 splice form K^S) | yes | none | SAFE |
| 19 | PP32 Theorem 3.1 | no | Ad (rank-linear), Fam + WS (edge) | NOT SAFE |
| 20 | REFEREE_PP32 Theorem A, Cor A′ | no | Ad (one general field), Fam + WS (edge) | NOT SAFE |
| 21 | PP38 Theorem 3.1 | no | Ad, Cp; (iii) St | NOT SAFE |
| 22 | PP43 Theorem 3.4 | no | Gt, Ad, Fam | NOT SAFE |
| 23 | PP45 Thm 3.1 = PP46 Thm A | no | Gt, Ad, Fam, St (T's uniqueness) | NOT SAFE |
| 24 | PP47 Thms 2.5, 2.7 | no | Gt, Ad, Fam | NOT SAFE |
| 25 | PP47 Theorem 4.1 | no | Gt, Ad, St | NOT SAFE |
| 26 | PP49 Theorem A | no (a sufficiency theorem) | Gt, Ad, St, Ct+, WS | NOT SAFE (no clause) |
| 27 | PP49 Theorem N | no | Gt, Ad, Ct+, WS | NOT SAFE |
| 28 | PP50 Theorem K | no | Gt, Ad, St | NOT SAFE; geometry SAFE |
| 29 | PP51 Theorem 5.1 | no | Gt, Ad, St | NOT SAFE; instance geometry SAFE |
| 30 | PP52 Theorem 4.1 | no (needs Ct+) | Ct+ | COND-Ct+; vacuous on selected posterior pairs (§5) |
| 31 | PP52 Prop 7.3 | no | Gt (OA), St (strict argmax) | NOT SAFE; proof gap (audit) |
| 32 | PP52 Conjecture 7.2 | — | Gt (OA) | CONJECTURE; nothing to encode |
| 33 | REFEREE_round50 Theorem R1 | no | Gt, Ad, St (strict gates (R)) | NOT SAFE |
| 34 | REFEREE_round50 Lemma S | no | Gt, Ad, Ct+ | NOT SAFE as a clause |
| 35 | AUDIT_posterior_pairs (pair ordering) | yes (pure geometry) | none | SAFE (geometry) |

**No result in the table depends on completeness, except** the single-field results (19–21, 27). A field ranks every record it judges, so those results are complete on their records.

---

## 2. Entries

### A. Lead's selection count (LEAD_selection_count; referee in REFEREE_six_source §7)

**1. Lemma A.**
- *Conclusion:* Φ_M := {p : C_p ≈ M} = ⋂_w A_w(M), and this set is closed.
- *Hypotheses:* M undominated (selected or not; the referee strengthened this); closed sections for the rival M.
- *In module:* holds, with closedness relative to N_u. It is about ties, so ties are allowed.
- *Encode:* "C_p ⪯_w M at every w ⇒ M ⪯_w C_p at every w", for protected M. This is M's undominatedness clause, so it is already in the base. Closedness of Φ_M enters only through M6.

**2. Lemma B.**
- *Conclusion:* C_{e_i} = V_i, and V_i has no all-world tie with any other model.
- *Hypotheses:* e_i is in the index set; competitiveness at e_i; strict (G).
- *In module:* the first half fails, because no vertex is selected. The second half is pure strict (G): V_i ≺_i M for every M ≠ V_i.
- *Encode:* if V_i appears as a rival, [V_i ⪯_i M] true and [M ⪯_i V_i] false. These are guidance clauses already in the base.

**3. Theorem C.**
- *Conclusion:* (i) no (S)-selection takes finitely many values; (ii) with no all-world ties among selected models, fibres are closed and the selection is uncountable; (iii) OPEN.
- *Hypotheses:* (i) whole Δ, Lemma B at two vertices, connectedness; (ii) adds no ties.
- *In module:* not applicable. Index = likelihood is injective anyway.
- *Encode:* nothing. (ii) uses an explicit no-tie hypothesis.

**4. Lemma D.**
- *Conclusion:* only countably many models (in the referee's repair, groups) can each have a non-null set on which they alone are definite.
- *Hypotheses:* a σ-finite measure. Nothing else.
- *Encode:* not a clause. It is a design constraint: any protection device for the 2-D module must use witnesses shared by uncountably many members.

**5. Lemma E.**
- *Conclusion:* Φ_T is compact and lies in the open simplex.
- *Hypotheses:* T undominated; (TC) (in a form valid with ties); strict (G); edge indices present.
- *In module:* vacuous, since there are no edge indices.
- *Encode:* only the inner step. If C ≈ T, then C ⋠_i X for every X with X ≺_i T. This is a (TC) instance with a strict-guidance link, so it is SAFE.

### B. AUDIT_section_topology (author-checked; no referee)

**6. Face preservation (§1).**
- *Conclusion:* a selected D_K that is competitive on supp a has K ⊆ Δ_{supp a}.
- *Hypotheses:* strict (G); competitiveness against an open-set fill. Both hold in the module.
- *Encode:* vacuous, because every module index is interior.

**7. Tripod surjectivity (§1).**
- *Conclusion:* every continuous face-preserving map f : Δ → Δ is onto. So a continuous whole-simplex posterior selection cannot avoid any neighbourhood of posterior models near T.
- *Hypotheses:* the whole closed simplex, and continuity of f.
- *In module:* not applicable; locally the module uses f = id.
- *Note:* using it as an *obstruction* needs Theorem K (gate, strict CG2), as the audit itself says ("if Theorem K excludes gating the omitted models").
- *Encode:* nothing.

**8. Addition lemma (§2).**
- *Conclusion:* adding any comparisons whose disagreement sets lie in an ideal I with no non-null cone preserves closed fixed-rival sections along a coherent selection with closed model fibres.
- *Hypotheses:* closed fibres hold, since the posterior family is continuous in measure and injective (AUDIT_posterior_pairs §1, PP49 Lemma 1.1). The base relation must already have closed sections.
- *Ties:* irrelevant.
- *Limits:* it licenses **additions only**. It concerns sections along the original coherent selection, **not** the annular section condition of AUDIT_radial_transport. The models JC_a are not conic, so its "at most one conic model per class" step fails for them.
- *Encode:* TOOL. Use it to certify sections of a candidate, not as a clause.

**9. Local construction theorem (§3).**
- *Conclusion:* R_i := guidance ∪ {d(X, Y) ∈ I and X Q_i Y} satisfies (G), (IB), (TC), and closed sections along every continuous coherent selection.
- *Hypotheses:* Q_i is reflexive, with strict (G), (IB) and (TC) on the full domain.
- *Ties:* allowed in Q_i. I re-checked the (TC) proof. Reverses come from Q_i's own (TC) and have support in I. The one-I-link case closes by strict (G) in Q_i. No strictness is used.
- *Limits:* it gives no defence, undominatedness, (C) or (LA). Verdicts must not use "the coherent model in this class" (an (IB) failure).
- *Encode:* TOOL.

### C. PP18 and PP19 (REFEREE_Z_PP19: both correct, with repairs as noted)

**10. PP18 Theorem Z.**
- *Conclusion:* for every world w and every non-null mixed set R, some accepted strict all-world domination C_p ⪯_v X out of a selected model makes advice w-correct on part of R. Hence every correctness zone lies in U.
- *Hypotheses:* (IB); strict (G); (S) on the **whole** simplex, through Lemma B at vertices and KKM; direct (C) for incoherent X. No (TC), no T1, no no-ties (the referee confirmed).
- *In module:* fails, because KKM over Δ is unavailable.
- *Encode:* COND-WS. Its design moral stands for any eventual system: do not build protection from correctness zones.

**11. PP18 Lemma Z0.**
- *Conclusion:* if P is a 1-zone at w, N is undominated, and Q ⊆ P is non-null with N not w-correct there, then no model dominates N[Q → w-correct].
- *Hypotheses:* (IB), reflexivity, N undominated. All hold for selected N.
- *Encode:* the zone-free core, which is PP19 Lemma 0.4. If Z ⪯_v X at every v, strictly somewhere, and X = N on {Z ≠ X}, then N[{Z ≠ X} → Z] dominates N. Under exact (IB) this is N's undominatedness clause. SAFE and redundant.

**12. PP19 Theorem 1.**
- *Conclusion:* if X ≺_w T, then A_w(X) ∩ Φ_T = ∅, at positive distance. So near Φ_T, selected models defend against X only at worlds where X does not beat T.
- *Hypotheses:* T ⪯_w C_p for p ∈ Φ_T; (TC); closed sections; Φ_T compact.
- *In module:* holds if N_u is closed (Φ_T is then compact by Lemma A). Ties allowed: the conclusions are refusals, and Φ_T may contain several points.
- *Encode:* point form. For every p with T ⪯_w C_p (p = u at least), add ¬[C_p ⪯_w X] whenever X ≺_w T by strict (G). If X ≺_w T is itself an accepted strict non-guidance comparison, the clause is conditional on it. The neighbourhood form enters **only** through M6.

**13. PP19 Theorem 4.**
- *Conclusion:*
  - (a) For every C, the set I_T(C) ≠ {1, 2, 3}.
  - (b) If C ⪯_i X and C ⪯_j X′ with X ≺_i T and X′ ≺_j T, then T ⋠_i C, T ⋠_j C, T ⪯_k C, and C ⋠_k Y for every Y ≺_k T.
  - (c) The dominator classes Dom_k are nonempty, pairwise disjoint and disjoint from Φ_T.
  - (d) The opposite closed edge is avoided.
- *Hypotheses:* T competitive at all worlds; (TC); strict (G). (c) uses KKM for nonemptiness. (d) needs edges and no ties, or (referee's repair) E non-conic.
- *In module:* (a), (b) and the disjointness in (c) hold. Nonemptiness in (c) and all of (d) do not.
- *Encode:* (b) as a clause: [C ⪯_i X] ∧ [C ⪯_j X′] ⇒ ¬[T ⪯_i C] ∧ ¬[T ⪯_j C] ∧ [T ⪯_k C]. Here the strict links X ≺_i T and X′ ≺_j T come from strict (G). The last conjunct comes from T's defence disjunction.

**14. PP19 Theorem 5 (with Lemma 5.0).**
- *Conclusion:* if C ⪯_i X_{E_i} and C ⪯_j X_{E_j} (majority fills on M_k), and C is exposed on both, then C's compensation set P is non-null.
- *Hypotheses:* (IB); strict (G); (TC); T competitive against the constructed rival Y = T[D_Y → C]. Only weak acceptances are used. C need not be selected. The referee confirmed that no single-world-tie prohibition is used.
- *In module:* holds, since T = C_u must defend against Y.
- *Encode:* ¬([C ⪯_i X_{E_i}] ∧ [C ⪯_j X_{E_j}]) whenever exposure holds and P(C) is null. P is computed pointwise from advice.

**15. Prop S (REFEREE_Z_PP19 §3.4).**
- *Conclusion:* split defenders C (at i) and C″ (at j) of majority fills must have a non-null set O.
- *Hypotheses:* as for Theorem 5.
- *Encode:* ¬([C ⪯_i X_E] ∧ [C″ ⪯_j X_{E′}]) when both are exposed and O is null. SAFE. Note that PP19's "sharing within a class is free" is **wrong**; use Prop S instead.

### D. Forced refusals (all derived from reflexivity, strict (G), (IB), (TC): PP47 Prop 2.1; REFEREE_round47, REFEREE_round48, REFEREE_round50 confirm)

**16. PP30 Theorem 3.1.**
- *Conclusion:* for every p and bounded non-null G ⊆ Sil(T) there is a world w with:
  - R_{p,G} := D_p[G → S] ⪯_w D_p, which is the same verdict as T ⪯_w T[G → D_p];
  - D_p ⋠_w D_p[G → S, E → w-correct] for every non-null E ⊆ G.
- *Hypotheses:* reflexivity, strict (G), (IB), (TC), and T competitive at all three worlds. All hold, since T = C_u.
- *Encode:* for any model N that answers a.e. on G (§5), a clause tying T's defence variable against T[G → N] to N's refusals. Thms 3.2 and Cor 3.3 use S_0 (Ad) and are not part of this entry.

**17. PP33 Theorem 3.1 (ordinal refusal).**
- *Conclusion:* if C ⪯_v Y, Y = N off a bounded set, and N ≤_v C pointwise on Q = {C ≠ N} with Q not essentially bounded, then Y ⋠_v N[H ↦ C] for every bounded H ⊆ Q.
- *Hypotheses:* reflexivity, strict (G), (TC).
- *Encode:* [C ⪯_v Y] ⇒ ¬[Y ⪯_v N[H ↦ C]]. Only Q ∖ H non-null is really needed. The budget form, Cor 3.2, needs an optional potential (Ad). The referee requires it to be marked conditional: NOT SAFE.

**18. PP36 Prop K and PP40 Prop 3.1 (K^S).**
- *Conclusions:*
  - Prop K: if N ⪯_i Z with Z = C[G → S, E → w-correct], and Z ≺_i D by strict (G), then D ⋠_i N.
  - K^S: if C ⪯_i Z and Z ≺_i D[S ↦ C], then D ⋠_i C[S ↦ D], which by (IB) is the same verdict as D[S ↦ C] ⪯_i C.
- *Hypotheses:* (TC), strict (G), and (IB) for K^S. PP40 lists "D's universal competitiveness", but it is used only for consequences.
- *Corollaries:*
  - Cor K1 needs D coherent, or D ≠ Z off G (referee).
  - Cor K2 needs KKM over Δ: COND-WS.
  - Cor K3 and Lemma P1 are geometry of precise models. They are true but not about M1.
  - The kernel form, PP40 Cor 3.2, is Ad: NOT SAFE.
  - The PP36 claim "one answerer at one defence world is Prop-K-safe" is **wrong** (REFEREE_round48 §3.4).
- *Encode:* [N ⪯_i Z] ⇒ ¬[D ⪯_i N], and [C ⪯_i Z] ⇒ ¬[D ⪯_i C[S ↦ D]], when the closing link is strict guidance. If the closing link is an accepted non-guidance strict comparison, the clause is conditional on it.

### E. Single-field and additive results

**19. PP32 Theorem 3.1.**
- *Conclusion:* no positive rank-linear densities endorse both the edge models' comparisons (worlds 1, 2) and T's majority-fill acceptances on three small pieces of Sil(T).
- *Hypotheses:* an edge selection on [e_1, e_2] with closed sections for D_{(1/2,1/2,0)}; strict (G) at worlds 1 and 2; T competitive; **rank-linear endorsement**. PP35 corrected "additive" to "rank-linear".
- *In module:* no edge, no endorsement.
- *Encode:* nothing.

**20. REFEREE_PP32_penalties Theorem A and Cor A′.**
- *Conclusion:* Theorem A is the seam barrier for any general field with silence costly, (H4) α_1α_2 ≥ β_1β_2. Cor A′, for any single field: every selected non-vertex edge model's window reaches an end of the band J.
- *Hypotheses:* one endorsing field (Ad); an edge selection (Fam, WS).
- *Encode:* nothing.

**21. PP38 Theorem 3.1 (potential kernels).**
- *Conclusion:*
  - (i) A potential kernel plus guidance gives (G), (IB), (TC) on bounded records, with ties exactly at Φ_w = 0.
  - (ii) A model is competitive against every bounded rival iff it is λ-Bayes for the field at a weight in its support.
  - (iii) Rules III and IV are inert under a.e.-unique Bayes models.
- *Hypotheses:* one strictly guiding integrable field decides all bounded records (Ad; complete on bounded records). (iii) adds uniqueness (St).
- *In module:* not assumed. Note that (ii) "⇒" is a statement about this architecture, not about the axioms.
- *Encode:* nothing. Use only in a labelled "potential-kernel" branch.

### F. Gate architectures (all assume Gt + Ad; none applies to M2)

**22. PP43 Theorem 3.4.**
- *Conclusion:* no jump from T to segments B_ij(t_n) at indices p_n → p_0. An explicit rival X_n* is refused at every world.
- *Hypotheses:* a fixed ℓ^T kernel on bounded records; additive gates V^C = Φ + Π^C under (AR); segment family (Fam); (H_rc); closed sections at p_0.
- *Not used:* the zero rule, and ties.
- *Encode:* nothing.

**23. PP45 Theorem 3.1 = PP46 Theorem A.**
- *Conclusion:* T and a combined cut C_(a,b,0) cannot both be gated. CG2 fails at some world, so (TC) fails.
- *Hypotheses:* gate union under (R) or (R0); own-Bayes additive fields; the multicap family; AB universally competitive (H1); T a.e.-uniquely own-Bayes (H2).
- *Silent use:* REFEREE_round51 says T's uniqueness is an **unstated** hypothesis of PP46 Thm A (§3). That is a silent strictness assumption.
- *Rule-independent residue:* PP52 Thm 4.1 (entry 30).
- *Encode:* nothing.

**24. PP47 Theorems 2.5 and 2.7.**
- *Conclusions:*
  - 2.5: without T's uniqueness, under (R0), T is all-world tied with an incoherent fill (direct (C) fails); under (R), T is uncompetitive at the four-model checkpoint.
  - 2.7: the full cut is excluded using the A-families alone.
- *Hypotheses:* gate union; CG2 at all worlds; weak own-Bayes; multicap family. For 2.7 the weak case needs N undominated, which the referee says is missing.
- *Note:* 2.5 does not assume no ties. It **produces** a tie through zero acceptance.
- *Encode:* nothing.

**25. PP47 Theorem 4.1.**
- *Conclusion:* in a two-valued family under (R0), (TC) holds iff the closed interval test holds with positive constants and no tight triple has all three extremes attained.
- *Hypotheses:* gate union (R0); (BR); **strict CG2 a.e. for every pair**. Through Lemma 1.3, strict CG2 means **no two distinct models tie at any world**.
- *Silent use:* the headline (§0 item 3) and DESIGN_MEMO §8.20 state the equivalence without strict CG2 (REFEREE_round51 §4.6; AUDIT_posterior_pairs §5). The theorem does not show that zero-accepting (TC) systems are tie-free.
- *Encode:* nothing, except in the no-ties comparison run.

**26. PP49 Theorem A.**
- *Conclusion:* (H0)–(H5) imply every axiom, (S) on closed Δ, and KKM dominance strict at every world, with **no single-world ties**.
- *Hypotheses:* the gate union over the whole posterior family; (H2) strict CG2 (St, explicit); (H4) L¹-continuity (Ct+).
- *Kind:* a sufficiency theorem. It yields no constraint. Theorem K shows its hypotheses fail near u.
- *Family facts (Lemmas 1.1, 1.2):* the selection is continuous in measure and injective, and overlapping posteriors never give opposite answers. These are SAFE geometry.

**27. PP49 Theorem N.**
- *Conclusion:* every solution of (H0)–(H5) has a world with no integrated global witness.
- *Hypotheses:* (H0)–(H5) with (H4)(c); whole simplex; FF2 Thm 4.1's import chain, which needs continuity in measure and a strictly guiding witness.
- *Encode:* nothing.

**28. PP50 Theorem K.**
- *Conclusion:* at ε = 3/10, gated posterior index sets meet U₀ = {|x| < 10⁻⁵} in a null set. So no positive-measure posterior family through T is gateable.
- *Hypotheses:* own-Bayes gates, **strict CG2** (explicit), the closed triple test, and PP51 Thm 5.1. "No axiom is involved" (PP50 §6.3).
- *SAFE part:* Prop 6.2, the exact box certificate that the kink's oriented matroid and cells are fixed on the box, is pure geometry. It may be used to enumerate cells.

**29. PP51 Theorem 5.1 (kink certificate).**
- *Conclusion:* a two-valued gated triple with own-Bayes fields and positive constants passing the closed triple test is impossible under (K1)–(K3).
- *Hypotheses:* gate union, own-Bayes fields, constants. In addition, **either** T is a.e.-uniquely own-Bayes **or** CG2 is strict on the two certificate cells. This is explicit.
- *Gap:* the stated gap (§5.2), weak own-Bayes with non-strict CG2 on both cells, is exactly the tie case.
- *SAFE part (CHECKED in PP50 §6.2):* the instance geometry. There are 18 two-valued cells. In one cell T answers alone, wrong only at world 1 ("above"). In another T answers alone, right only at world 1 ("below"). Every pair is two-signed at every world.
- *NOT SAFE part:* the admissible orders of log(ω^A/ω^B) and log(ω^A/ω^D) in (K2) are field statements (Ad).

**33. REFEREE_round50 Theorem R1.**
- *Conclusion:* for two-valued families under **strict** gates (R), (TC) holds iff every pair passes the sandwich and every triple has common nonnegative constants.
- *Hypotheses:* gate union under (R). The necessity proof refuses reverses "using strictness of (R)".
- *Under (R0):* only sufficiency and pair necessity are established.
- *Encode:* nothing.

**34. REFEREE_round50 Lemma S.**
- *Conclusion:* closed fixed-rival sections for a compact gated family.
- *Hypotheses:* (R0); (S1) gated models continuous in measure; (S2) L¹-continuous field differences; (S3) a continuous selection; (S4) **no other acceptance routes**.
- *In module:* (S4) and the gate structure fail. Lemma S also builds in closedness along rival mass paths, because integral values are continuous.
- *Encode:* nothing. It is a section tool only for a pure gate-union candidate.

### G. PP52 (unrefereed; audit cautions in AUDIT_section_topology §5 and AUDIT_round53_final)

**30. PP52 Theorem 4.1 (KKM test).**
- *Conclusion:* let N defend on its support, and suppose bounded pieces E_1, E_2, E_3 exist on which M beats N at every world but k. Then a bounded modification Y = M[D ↦ N] has Y ⪯_w M at every w. So M is dominated **or all-world tied with an incoherent model**. Both are excluded for a coherent protected M by undominatedness and direct (C). This survives single-world ties.
- *Hypotheses:* strict (G); N's defence; and **N's verdicts on its own records closed along mass paths**, where the rival changes along the path. This is stronger than (S), which fixes the rival (audit).
- *In module:* the last hypothesis is not available (M5).
- *Encode:* COND-Ct+ only. Even there it adds nothing among selected models (§5, observation 2).

**31. PP52 Prop 7.3.**
- *Conclusion:* designation cannot remove a strict co-activity.
- *Hypotheses:* own-argmax gates (Gt); a strict argmax with a strictly positive maximum (St).
- *Proof gap:* per the audit, the padding excludes one alternative realiser M′, not a continuum of them.
- *Encode:* nothing.

**32. PP52 Conjecture 7.2.**
- *Status:* CONJECTURE (NUMERICS search). It states that every OA field system on the kink triple fails (PX).
- *Encode:* nothing. Do not treat the "selective exit is closed" reading as proved.

### H. AUDIT_posterior_pairs (refereed correct in REFEREE_round51 §5; extended to boundary pairs by PP49 Prop 5.2 and PP52 Prop 5.1)

**35. Pair-ordering theorem.**
- *Conclusion:* at every disagreement of C_a and C_b, min_{i∈W} b_i/a_i < max_{j∈R} b_j/a_j.
- *Hypotheses:* M compact and convex in int Δ. There are no ranking hypotheses at all.
- *In module:* holds exactly.
- *Encode:* as geometry. Every enumerated disagreement type of two posterior models must satisfy it, which is a cell-enumeration sanity check. Consequence (PP52 Cor 5.2): two posterior models never show all three single-better types, in either orientation.
- *Caution (audit §3):* do **not** install D = log(a/b) as compatibility constants or prices.

---

## 3. Where no-ties or strictness entered

**Explicit hypotheses** (no hidden use):
- LEAD Theorem C(ii) (no all-world ties);
- PP19 Theorem 4(d), Prop 2(e) and Prop 9(a) (no all-world ties; repaired for non-conic sets);
- PP19 Cor 1.1 "Sources" and Prop 3(b) (strict source pattern);
- PP38 Theorem 3.1(iii) (unique Bayes);
- PP45 Theorem 3.1 (T's uniqueness, H2);
- PP49 Theorem A ((H2) strict CG2, so no ties is an output);
- PP50 Theorem K (strict CG2);
- PP51 Theorem 5.1 (uniqueness or strict CG2 on two cells);
- PP52 Prop 7.3 (strict argmax);
- REFEREE_round50 Theorem R1 (strict gates (R)).

**Silent or under-stated uses:**
1. **PP46 Theorem A.** It uses T's a.e.-unique own-Bayes property without stating it (REFEREE_round51). PP47 Thm 2.5 removes it under (R0), but only by turning the failure into an all-world tie.
2. **PP47 Theorem 4.1.** The headline (§0 item 3, the "Answer" paragraph) and DESIGN_MEMO §8.20 drop "strict CG2 a.e.". Under that hypothesis Lemma 1.3 forbids **every** single-world tie. So the "exact (TC) test for zero-accepting gates" is an exact test only for tie-free gate unions.
3. **PP51 Theorem 5.1 → PP50 Theorem K → DESIGN_MEMO §8.21.** The memo's "no positive-measure posterior family or 2-D patch through T can be realised" omits that the certificate needs strict own-Bayes for T or strict CG2 on the two cells. PP51 §5.2 lists the weak-tie case as its one gap. The headline should carry it.
4. **DESIGN_MEMO §8.21, PP52 entry.** "Rule-independent … holds for any rule with closed verdicts" uses "closed" to mean closed along changing-rival mass paths, not (S). This is a continuity assumption, not a tie assumption, but it is the same kind of under-statement.

**No silent use of no-ties** in the axiom-level results 11–18 (PP18 Lemma Z0, PP19 Thms 1, 4, 5, Prop S, PP30, PP33, PP36/PP40). The referee checked PP18 and PP19 explicitly (REFEREE_Z_PP19 §4). Each of these results ends in a refusal (⋠) or a domination. None ends in a strict non-guidance preference. They therefore survive ties unchanged. The referee (REFEREE_Z_PP19 §5.2) also notes that their kills close with a strict **guidance** link. Completing those triangles would be F1, so tie completion cannot absorb them.

---

## 4. Encoding plan by run (audit's three versions plus two conditional runs)

**Run 1: ties allowed (base).** Use the axioms of M3 exactly, plus derived clauses labelled with their source:
- PP19 Thm 1 (point form at indices tied with T at w);
- PP19 Thm 4(a), (b);
- PP19 Thm 5;
- Prop S;
- PP30 Thm 3.1 (any N answering on G);
- PP33 Thm 3.1;
- Prop K and K^S (strict-guidance closing link);
- the Lemma Z0 / Lemma 0.4 exposure clause;
- LEAD Lemma E's inner step.

Import them only when the auxiliary models they name (Y, Y^w_E, N[H ↦ C], C[S ↦ D]) are realised on actual positive-measure sets in the instance, or with the derivation recorded. Use the geometry of entries 28, 29 and 35 for cell enumeration. Sections enter only by M6.

**Run 2: ties forbidden.** Run 1 plus "no two distinct models tie at any world". Source: imposed by assumption, as in PP47 Lemma 1.3 and PP49 Lemma 3.2. It is not derived.

**Run 3: gate-derived.** Run 2 plus the following:
- realiser gating (Gt);
- own-Bayes for each selected model (PP45 Lemma 2.3, which is valid only under Gt);
- strict CG2 for each pair;
- the closed triple test (Thm R1 / PP47 Thm 4.1);
- ω-separability per cell (PP50 Lemma 6.1).

PP51 Thm 5.1 and PP50 Thm K predict that this run fails on the kink.

**Run COND-WS.** Assume an eventual whole-simplex system. Add:
- Theorem Z (no correctness zones);
- Cor K2;
- PP19 Thm 4(c) nonemptiness;
- LEAD Lemma B and Thm C(i);
- tripod surjectivity.

These are statements about the eventual system, not about the local module.

**Run COND-Ct+.** Add closedness of each selected model's own verdicts along mass paths (PP52 Thm 4.1). By §5 observation 2 it adds no clause among selected posterior models. It can bite only if non-posterior coherent models are protected.

---

## 5. Two short observations (PROVED)

**Observation 1: PP30 Thm 3.1 holds for every model N, not only precise D_p.** Let G ⊆ Sil(T) be non-null and let N answer a.e. on G.
1. rec(T, T[G → N]) = (G, S → N|_G) = rec(N[G → S], N).
2. For non-null E ⊆ G, T[E → w-correct] ≺_w T by strict (G), and rec(T[G → N], T[E → w-correct]) = rec(N, N[G → S, E → w-correct]).
3. T's defence against T[G → N] gives a w with N[G → S] ⪯_w N. (TC) then refuses N ⪯_w N[G → S, E → w-correct] at that w.

Only reflexivity, strict (G), (IB), (TC) and T's defence are used. This is PP33 Prop 2.1(f) and PP38 A2 in general form. In the module it applies to every C_a on the part of Sil(T) where C_a answers. ∎

**Observation 2: PP52 Thm 4.1 is vacuous among selected posterior models.** In the module, its conclusion contradicts an axiom only if M is protected, so M = C_b is selected. Its hypotheses need N to defend on its support, so N = C_a is selected too. The theorem needs, for each k, a disagreement at which C_b beats C_a exactly at the worlds other than k. That means K₂(C_a, C_b) = {1, 2, 3} in PP52's notation. PP52 Cor 5.2, which follows from the pair-ordering theorem, says this never happens for two posterior models. So the "rule-independent" obstruction cannot be what drives the kink, which is consistent with PP52 §5 ("the posterior family's difficulty is not at pair level"). The kink's own mechanism (PP51) lives entirely in Gt + Ad + St. ∎

---

## 6. Bottom line

- **SAFE to encode in a ties-allowed, non-gate module.**
  - Clauses: PP18 Lemma Z0 (exposure form); PP19 Theorem 1 (point form; neighbourhood form only by actual sequences), Theorem 4(a) and (b), Theorem 5; Prop S; PP30 Theorem 3.1 (for any N); PP33 Theorem 3.1; PP36 Prop K with the PP40 splice form; LEAD Lemma A (redundant) and Lemma E's inner step; the strict-(G) half of Lemma B.
  - Geometry: the pair-ordering theorem; PP49 Lemmas 1.1–1.2; the kink cell structure (PP50 Prop 6.2, PP51 instance).
  - Tools and design constraints: the addition lemma and the local construction theorem (certify candidates, with the annular caveat); LEAD Lemma D.
- **Conditional only.**
  - Whole-simplex: Theorem Z, LEAD Lemma B (first half), Theorem C(i), Lemma E, PP19 Theorem 4(c) nonemptiness and 4(d), Cor K2, tripod surjectivity.
  - Changing-rival closedness: PP52 Theorem 4.1, which is vacuous on selected posterior pairs.
- **NOT SAFE (gate, additive or strict architecture).** LEAD Theorem C(ii); PP32 Thm 3.1; Thm A and Cor A′; PP38 Thm 3.1; PP43 Thm 3.4; PP45 Thm 3.1 = PP46 Thm A; PP47 Thms 2.5, 2.7, 4.1; PP49 Thms A and N; PP50 Thm K; PP51 Thm 5.1; PP52 Prop 7.3 and Conjecture 7.2; Thm R1; Lemma S. These belong only in Runs 2–3 or as adversarial tests.
