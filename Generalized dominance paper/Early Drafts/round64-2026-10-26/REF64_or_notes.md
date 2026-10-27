# REF64_or — Referee report on OR64_notes.md (25 Oct 2026)

Referee: REF64_or. Standard: journal-level rigour. I checked every claim myself, by hand, measure-theoretically. I re-ran OR64's scripts and wrote independent ones.

Framework used: BRIEF64 "binding framework" and AUDIT_r64. That is: reflexivity, a.e.-identification, (TC), strict (G) and (IB) as in W62 §2. The cover requirements are global coherence, direct (C), target undominated, incoherent-model dominance and (LF). Transitivity and completeness are **not** assumed.

Scripts (folder `ref64or_py/`, run with `python3 -I`):
- `geom_rerun.out`, `records_rerun.out`: OR64's two scripts, re-run. The output is byte-identical to OR64's `.out` files (`diff` empty). ALL PASS.
- `tcmat.py` → `tcmat.out`: an independent implementation. Each world's relation is a boolean matrix over **all** models, and (TC) is checked over **all** triples at once through the boolean product L·L.
  - Richer atom sets than OR64's: M1 and M1b on 12 atoms (every sign pattern present, three R-atoms); 𝒯 on 13 atoms (every admissible sign pattern inside and outside D_K).
  - It also checks that 𝒯 has no non-trivial ties, and that 𝒯 satisfies (VA). ALL PASS.
- `w62dom.py` → `w62dom.out`: a (TC) system showing that the (C)-step of W62 Lemma `lem:dominance` needs transitivity. ALL PASS.

---

## 0. Summary verdict

OR64 is careful and mostly right. The two headline mathematical results are correct:
- the counter-model M1;
- Lemma OC.

The box-lemma repairs and the diagnostic 𝒯 are also correct. Prop K and Theorem VA are correct as stated.

I found:
- **one logical error** (C21). It is minor and easily repaired, but it bears on criterion (B). OR64 says 𝒯 shows that (VA2) cannot be derived from the requirements outside 𝓘. In fact **𝒯 satisfies (VA)** (with R_j := OUT ∩ neg_j). The correct statement must quantify over veto families that miss the collar.
- **one gap in the architecture ledger** (C23). W62 Lemma `lem:dominance` uses **transitivity** in its (C)-step, not only completeness in its last step. Counterexample: `w62dom`.
- **several overstatements**:
  - "No world can veto any non-null part of the collar, **in any relational form**": E61-priority regions are not excluded without (TP).
  - "Theorem VA **contains** E61 Cor 5.3": it contains Cor 5.3's no-cover consequence, not Cor 5.3 itself.
  - "Lemma OC is a **strict generalisation** of E61 Lemma 3.4": the two lemmas have incomparable hypotheses.
  - 𝒯 "satisfies **all axioms**": only the relational ones, together with target undominatedness and direct (C).
  - "**finite-looking** local problem".

Item 3 of the referee brief asked whether every priority region used in E61, O61 and IN63 is strong. It is **CORRECT**. I close OR64's open point on depth-leximax and Pareto vetoes in §3, by a record criterion (LV). No earlier theorem is damaged.

---

## 1. Verdict table

| # | Claim (OR64 numbering) | Verdict | Note / repair |
|---|---|---|---|
| C1 | Prop 1.1: record form of (IB) | CORRECT | Records are a.e.-classes; both directions checked. |
| C2 | Prop 1.2: composition formula, commutativity, converse; (TC) in record form | CORRECT | The converse builds A, B, C from the records. They are models because models are all measurable subsets of U (or, in a splice-closed class, they are splices). |
| C3 | Prop 1.3: (TC) + completeness ⇔ transitivity | CORRECT | — |
| C4 | Prop 1.4(a)–(d) | CORRECT | (d) is checked in §2.4 below. Strengthening: *every* (TC) violation involves at least two non-guided accepted records at one world (r₁ and c⁻¹), not only anti-guided composites. |
| C5 | **Prop 2.1, counter-model M1** | **CORRECT** | Verified on the actual model space (§2.1). R is an E61 priority region in E61's exact sense; X_i is dominated by Y₀. 12-atom exhaustive check passes. Wording: there is *one* special record r₀, accepted at two worlds. |
| C6 | Lemma 2.2: box lemma under strong priority, strict (G) at i only | CORRECT | Uses no (TC), transitivity or completeness. |
| C7 | Lemma 2.3: box lemma under strict priority; (TC) needed (M1b) | CORRECT | M1b satisfies reflexivity, strict (G), (IB) and strict priority, yet X_i is dominated (§2.2). So (TC) cannot be dropped. Wording: (TC) fails "for example", not "exactly", on that chain. The 12-atom version has 35 504 violating pairs. |
| C8 | Prop 2.4: inclusion vetoes (direct proof) | CORRECT | Minor: E61's density step uses "U ∩ pos_i open". For a general decomposable U, use the density of R instead (§2.3). "Impossible" should read "non-trivial inclusion vetoes are impossible (R ⊆ {h ≤ 0} a.e.)". |
| C9 | Prop 2.5: E61 Lemma 3.4 for strong or strict priority | CORRECT | Minor: in the binding framework U need not be open. Replace O₂ := U ∩ pos_i ∩ pos_j by the open set (D_K ∪ N) ∩ pos_i ∩ pos_j, where N is the (LF) neighbourhood. E61's hull point B already lies there. |
| C10 | **Prop 2.6: every region used in E61, O61 and IN63 is strong** | **CORRECT** (completed here) | Depth-leximax and Pareto vetoes are strong under every (IB)-compatible formalisation (§3). Downstream theorems are safe twice over: their classes are transitive, *and* their regions are strong. Strongness is what saves E61 Cor 5.3 with its "then anything" tails. |
| C11 | Prop 2.7: strictly sign-correct additive rankings have no priority regions; boxes are covered (FD-B) | CORRECT | The same proof also excludes E61-priority regions. FD-B (c_j = min(l_j h_j, u_j h_j)) is single-level and strictly sign-correct; refereed CORRECT in REF62_fd. |
| C12 | Facts (a), (b), (c); F1–F6 | CORRECT | — |
| C13 | Prop 3.1, **Lemma T**, T1–T3 | CORRECT | These are elementary consequences of (IB) and undominatedness of D_K. They are valid for any target and any dominator, not only coherent ones. |
| C14 | **Lemma OC** (a)–(c) | **CORRECT** | Uses: strict (G) at i (step 3) and at j (step 4); incoherent-model dominance; (LF); positive density (W62 Lemma `lem:open`); (IB) only for the "every context" remark. Does **not** use (TC), transitivity, completeness, global coherence, target undominatedness or direct (C). Holds for every world j, every i ≠ j, and every measurable R ⊆ U ∩ neg_j with μ(R∩D_K) = 0 < μ(R∩C_i). Same caveat about O₂ as C9. |
| C15 | Cor OC, and the summary "no world can veto any non-null part of the collar, **in any relational form**" (§0.4, §2.4) | Corollary CORRECT; summary **GAP (overstatement)** | Excluded forms: strong priority; strict priority (uses (TC)); E61-priority *with (TP)*; any veto of (VA1) form. **Not excluded:** E61-priority regions inside the collar without (TP). That is exactly the M1 mechanism. Repair: "no relational veto that, against the dented box, refuses every coherent undominated R-acceptor". |
| C16 | **Prop 3.5 (𝒯)** (a)–(e) | **CORRECT** | Measure-theoretic proof re-checked (§4). 13-atom exhaustive check passes: undominated set = 𝓘 (181 models); all 45 collar-type additions are refused at every world. |
| C17 | What 𝒯 satisfies; the status-table phrase "all axioms" | **GAP (wording)** | 𝒯 satisfies: reflexivity, a.e., strict (G), (IB), (TC), target undominated, direct (C) (trivially: 𝒯 has no non-trivial ties at any world), and incoherent-model dominance *outside 𝓘*. It **fails** global coherence, incoherent-model dominance and (W), exactly on the incoherent one-world improvements (e.g. D_K ∪ P₁ and the dented boxes). Some one-world improvements are coherent (D_K, D_K ∩ pos_w, B_w when U∩pos_w is coherent); most are not. 𝒯 is a diagnostic, not a near-cover. |
| C18 | §3.6 classification V1–V5, "none produced by the forced data" | GAP (label) | The classification just restates the requirements. "None produced" is a report of a search, not a theorem. Label it informal. |
| C19 | **Theorem VA** (proof) | **CORRECT** | All four steps checked (§5). Uses (VA1), (VA2), Lemma OC (hence strict (G), incoherent-model dominance, (LF)), target undominated and direct (C). It uses (TC) only if (VA1) is obtained from strict priority. It does not use global coherence. |
| C20 | "Theorem VA **contains** E61 Cor 5.3" | GAP (minor) | It contains Cor 5.3's *no-cover* consequence. Cor 5.3 itself assumes only global coherence and concludes *strict* dominance of D_K. Theorem VA assumes incoherent-model dominance and direct (C). Variant VA′ (§5.3) recovers Cor 5.3 exactly. "Extends to non-transitive orders": yes, and no (TC) is needed when the R_j are strong. |
| C21 | "§3.5 shows … (VA2) cannot be derived from [the requirements outside 𝓘]" | **ERROR (minor, repairable)** | 𝒯 satisfies (VA) with R_j := OUT ∩ neg_j. (VA1) holds vacuously, because each dented box is in 𝓘_i and so undominated. (VA2) holds by guidance, because C ∖ R_j ⊆ pos_j. CHECKED in `tcmat`. Correct statement: in 𝒯, (VA2) fails for **every** family with μ(R_j∩C) = 0 (for instance R_j = ∅, where (VA1) is vacuous). So "requirements outside 𝓘 + (VA1)" do not imply (VA2). |
| C22 | **Prop K**; "(A) would settle the chart problem negatively" | **CORRECT** | Every requirement re-derived: (G), (IB), (TC), global coherence, weak dominators, incoherent-model dominance, direct (C), target, (LF). Needed and present: strict sign-correctness a.e.; "every minimiser" for every π ∈ Δ, *including boundary π*; a.e.-uniqueness of D_K. With only weak sign-correctness, or with only the a.e.-unique Bayes acts required to be coherent, the conclusion can fail (slab lemma E2). The reduction is correctly stated for this formulation of the chart problem. |
| C23 | Architecture ledger | Mostly CORRECT; **GAP** | (i) W62 Lemma `lem:dominance`: the (C)-step "Z ⪯ X ⪯ Y ⇒ Z ⪯ Y" uses **transitivity**. That is the first architectural step, earlier than the completeness step OR64 cites. Under (TC), adding completeness restores transitivity, so the single extra hypothesis "completeness" still suffices. Counterexample: `w62dom` (§6). (ii) Missing rows: E61 Thm 5.1 / Cor 5.2 and C62 §6.3. They cross at the Lyapunov + separation step (LDG lexbayes), and their regions are strong. (iii) "None uses (TP) outside a class where it holds automatically" is literally false for Cor 5.3's "then anything" tails, but harmless by C10. (iv) The "same decisive step" summary is interpretive; label it so. |
| C24 | Success criteria: (A) not achieved, (B) achieved, (C) achieved | CORRECT, with comments | (B) is a correct but thin conditional result. Once Lemma OC clears the collar, (VA2) almost is the conclusion. Its "needed" evidence must use the repaired C21. (C) is met modestly: Lemma OC removes (TP) for vetoes of (VA1) form and describes the forced dominators. |
| C25 | §6 "finite-looking local problem" | GAP (wording) | 𝓘 is infinite-dimensional. Say "the problem is localised to 𝓘". |

---

## 2. Checks of M1, M1b, (TC) propagation, Prop 2.4 (referee brief items 1–2)

### 2.1 M1 on the actual model space
Setup: Acc_i = G_i ∪ {r₀}, Acc_j = G_j ∪ {r₀}, Acc_k = G_k, with r₀ = (E∪A, B), where E ⊆ (+,−,+), A ⊆ (−,+,+) and B ⊆ (+,+,−) are non-null and E ⊆ R ⊆ U ∩ neg_j.
- **Reflexivity and a.e.-ties.** rec(X,X′) is null whenever X = X′ a.e., and the null record is guided.
- **(IB).** Holds by Prop 1.1.
- **Strict (G).** A non-null record cannot be both guided and anti-guided.
  - r₀ is not anti-guided at i (E ⊆ pos_i) and not anti-guided at j (A ⊆ pos_j).
  - So the inverse of a non-null guided record is never accepted.
- **(TC).** I re-derived OR64's composites. At j, r₀∘g contains A ⊆ pos_j in its positive part. At i, it contains E ⊆ pos_i. So its inverse is neither guided nor r₀. r₀∘r₀ is not composable. All checks are a.e. set identities, so they hold on the real model space.
- **Priority in E61's exact sense.** No Y with μ(Y∩R) > 0 has Y ⪯_j M_R:
  - the guided route forces Y∩R null;
  - the r₀ route needs B ⊆ M_R ⊆ neg_j, but B ⊆ pos_j.
- **Domination.** B ⊆ X_i, E∪A is disjoint from X_i, so rec(Y₀, X_i) = r₀ ∈ Acc_i ∩ Acc_j. At k the record is guided and non-null, hence strict.

So E61's box lemma is false under (TC), and (TC) does not imply (TP). CHECKED again on 12 atoms with every sign pattern (`tcmat.out`). There are 195 806 non-transitive pairs.

### 2.2 M1b
The added records rec(M_R, Y), for Y meeting R, are never anti-guided at j: their inverse adds Y∩R ⊆ neg_j. So strict (G) survives.

Strict priority holds. Y ⪯_j M_R would need rec(Y,M_R) to be guided, or r₀, or some rec(M_R,Y′). The last would need Y∖M_R ⊆ M_R, which is impossible.

Y₀ still dominates X_i. By Lemma 2.3, (TC) must therefore fail, and it does. **"(TC) genuinely needed" is supported.**

### 2.3 Prop 2.4 and E61's density step for general U
X_E = (U ∩ pos_i) ∖ (R∩B′) a.e. Pick a density point p of R ∩ pos_i, and nested balls B′ ⊂ B″ around p on which R ∩ pos_i has density > 1−η.

Then D_Q contains a.e. a (1−η)-full part of B″∖B′. The midpoint argument of IN63 E2 then puts the core of B′ inside D_Q. That contradicts D_Q ∩ R ∩ B′ = ∅ a.e.

Openness of U is not needed.

### 2.4 Prop 1.4(d) and the general shape of (TC) violations
Let r ∈ Acc_w and let g be guided and composable with r. If r∘g were anti-guided, then P_g ⊆ N_r, N_g ⊆ P_r, P_r ⊆ neg_w and N_r ⊆ pos_w, so r would be anti-guided. That is excluded by strict (G).

A (TC) violation is r₁, r₂ ∈ Acc with c := r₁∘r₂ ∉ Acc and c⁻¹ ∈ Acc.
- If r₂ is guided, then c⁻¹ is not guided, by (d).
- So at least two of r₁, r₂, c⁻¹ are non-guided accepted records.

---

## 3. Prop 2.6 completed: depth-leximax and Pareto vetoes (referee brief item 3)

**Lemma (LV) (PROVED here).** Assume (IB). R ⊆ U ∩ neg_j is a strong priority region at j iff Acc_j contains no record (A,N) with μ(A∩R) > 0 and μ(N∩R) = 0.

*Proof.*
- (⇐) rec(Y,Z) with Y meeting R and Z avoiding R is such a record.
- (⇒) Given such a record (A,N), the models Y := A and Z := N realise it, and Z avoids R. ∎

By comparison, E61-priority forbids only the records (A,N) with N ⊆ neg_j ∖ R and A ⊆ R ∪ pos_j. The gap between the two notions is exactly the set of records that also remove j-correct gambles. That is r₀ in M1.

**Applications.** In each case, (LV) says that a record adding vetoed mass and removing none must be strictly refused at the leading level.
- **Leading integral vetoes and countable veto blocks.** For a lexicographic order of integrals, or one view of a unanimity order, take the first index s with μ(A ∩ {φ_s > 0}) > 0. Then the record's veto difference is lexicographically positive, so it is refused. Strong.
- **IN63's R_v.** On N, both φ_v and c_v vanish, because N ∩ R_v is null. On A, either ∫φ_v > 0, or ∫φ_v = 0 and ∫c_v < 0. Refused. Strong.
- **Inclusion vetoes.** Strong, immediately.
- **Pareto vetoes** (a vector of non-negative vetoes compared componentwise at the first level). The record's N-side vector is 0, and its A-side vector is ≥ 0 and non-zero. Under every reading in which a Pareto-worse veto vector blocks ⪯ (strictly worse, or incomparable), the record is refused. Strong.
- **Depth-leximax or "worst violation first" vetoes**, with depth d > 0 on R.
  - Under (IB) the veto compares the depth profile of A with that of N.
  - N's profile is identically 0, and A's is not. Every leximax rule ranks the zero profile strictly best.
  - So the record is refused. Strong.
  - A whole-model version ("ess sup of depth over X") violates (IB), so it lies outside the framework.

E61 never defined these two vetoes formally. They occur only in its list of examples and in its §4.3 and §7 summaries, and no theorem of rounds 61–63 rests on them.

**Downstream theorems.**
- E61 Cor 5.3, Thm 5.1 and Cor 5.2; §4.4 and §4.6;
- O61 Lemma 3, where the veto sets A∖Z_j and A∖Z_k are strong at j and k, so Lemma 3 is a strong-priority box lemma;
- IN63 Thm C, steps 1 and 1′;
- C62 §6.3.

All use strong regions. **No earlier theorem is damaged.**

---

## 4. Diagnostic 𝒯 (referee brief item 6)

- **(TC).** Re-proved, all three cases (G∘G, T∘T, T∘G).
  - T∘T: the composite is (F₁∪F₂, N₁∪N₂). It is anti-guided only if both factors are.
  - T∘G: if the inverse of the composite were in G_w, then N_g ⊆ F and P_g ⊆ N. If it were in T_w, then N ⊆ P_g and F ⊆ N_g. Either way r would be anti-guided.
- **No non-trivial ties (PROVED here).** Suppose r and r⁻¹ are both accepted at w and r is non-null.
  - If either were guided, the other would be anti-guided, which is not accepted.
  - So both lie in T_w. Then X∖Y and Y∖X are each contained in IN ∩ OUT, so both are null.
  - Hence direct (C) holds trivially. CHECKED: 0 ties on 13 atoms.
- **Coherence of 𝓘.** D_K ∪ P₁ (P₁ a small ball in C₁ ⊆ pos₁) lies in 𝓘₁. It is incoherent, being not a cone. The dented box B_i∖R lies in 𝓘_i whenever R ∩ D_K = ∅, and it is incoherent by Lemma OC step 1. D_K ∩ pos_w = D_{conv(K∪e_w)} is coherent and lies in 𝓘_w.
- **(VA) holds in 𝒯.** Take R_j := OUT ∩ neg_j.
  - (U∖R_j) ∩ pos_i ∈ 𝓘_i, so it is undominated and (VA1) holds vacuously.
  - P ⊆ C∖R_j ⊆ pos_j, so (P,∅) is guided and (VA2) holds.
  - This is the basis of C21.
- **Exact statement of what 𝒯 shows.** Consider the relational axioms, target undominatedness, direct (C), and incoherent-model dominance for models outside 𝓘. These are jointly consistent with every world refusing every collar addition that is wrong somewhere at every world.
  - Hence any axiom-level proof must use global coherence or incoherent-model dominance on some incoherent member of 𝓘.
  - Since 𝓘 contains every pointwise-best-at-one-world model, this localisation is correct but not sharp.

---

## 5. Theorem VA and Prop K (referee brief items 7–8)

### 5.1 Theorem VA: the proof
1. **The veto regions miss the collar.** Lemma OC contradicts (VA1) when μ(R_j∩C_i) > 0 for some i ≠ j. Also C_j ⊆ pos_j is disjoint from R_j.
2. **A collar trade.** The balls B_k around c_k are disjoint and lie in C_k for small ρ, and Σc_k = (2−δ)𝟙. Then ∫_P h_j ≥ γ − Mε > 0.
3. **Incoherence.** For t > max_k (|c_k|+ρ)/(|c_k|−ρ), close to 1, tP′ misses every B_l, lies outside cl D_K and is non-null.
4. **Contradiction.** D_K ∪ P weakly dominates D_K. Target undominatedness then gives a tie at every world, and direct (C) makes D_K ∪ P coherent, which contradicts step 3.

All steps are correct.

### 5.2 Cor 5.3's class satisfies (VA)
Take R_j := ∪_v ∪_s {φ_{v,s} > 0}. This lies in neg_j, by (G) applied to S versus ∅, and it is strong. Let E_ε be the union of the Yosida–Hewitt sets.

For P ⊆ C∖(R_j∪E_ε) with ∫_P h_j > 0, every view ties on the vetoes and on the finitely additive levels, since ν_s(P) = 0, and is strictly better at Brier. So (VA2) holds, in fact with ≺_j.

### 5.3 Variant VA′ (repair for C20)
Make two changes:
- replace (VA1) by "R_j is strong";
- strengthen (VA2) to D_K ∪ P ≺_j D_K.

Then step 1 follows from Lemma 2.2 + global coherence + the hull step (Prop 2.5). Step 4 gives strict dominance of D_K directly. No incoherent-model dominance, no direct (C) and no (TC) are used. This is exactly E61 Cor 5.3 for (TC)-free relations.

### 5.4 Prop K
Checked step by step; see C22. The binding requirements are all met:
- (G): strict sign-correctness a.e.;
- (IB) and (TC): the ranking is integral, complete and transitive;
- global coherence: Lyapunov + a supporting π ∈ Δ, then hypothesis (i), which must cover non-unique minimisers and boundary π;
- weak dominators: maximise −Σz on the lower section;
- incoherent-model dominance: equal scores mean Pareto-minimal, hence coherent;
- direct (C): same score;
- target: (ii) with a.e.-uniqueness;
- (LF): assumed.

The contrapositive "(A) ⇒ no such chart" is correctly stated. It applies to this formulation of the chart problem, which is the one in O61 §7 (all minimisers coherent) and E61 §5's converse. It does not apply to E61 Thm 5.1's weaker necessary formulation (weakly sign-correct; only a.e.-unique Bayes acts coherent). (A) does not settle that one.

---

## 6. W62 Lemma `lem:dominance` needs transitivity (ledger, C23)

**Example (PROVED here; CHECKED in `w62dom.out`).** Take a one-sided U ⊇ D_K. Fix non-null sets:
- A ⊆ int ℝ³₊ ∩ U;
- B_w ⊆ U ∩ {h_w > 0, h_v < 0 for v ≠ w}, for each w.

Put t := (B₁∪B₂∪B₃, A), and Acc_w := G_w ∪ {t, t⁻¹} at every world.
- **Strict (G).** t removes A ⊆ pos_w and adds B_w ⊆ pos_w, so it is neither guided nor anti-guided at any w.
- **(TC).** The composites t∘g and t⁻¹∘g with non-null guided g have inverses that are neither guided, nor t, nor t⁻¹. The pairs t∘t and t⁻¹∘t⁻¹ are not composable, and t∘t⁻¹ is null.
- **Y is undominated.** Let Y := U ∩ int ℝ³₊, which is coherent (Y = D_Δ). The records accepted at every world are the Pareto-guided ones, t and t⁻¹. Of these, only t applies to Y, and it produces a tie.
- **X is tied with Y but dominated.** X := (Y∖A) ∪ B₁ ∪ B₂ ∪ B₃ is tied with Y at every world, yet it is dominated by X ∪ A.

So W62's inference "Z dominates X ⇒ Z dominates Y" fails under (TC). In the binding framework this is harmless, because direct (C) is a requirement. W64 should restrict the lemma to transitive (equivalently, under (TC), complete) rankings, or delete its (C) part.

---

## 7. Recommendations to the lead

1. Accept M1, Lemmas 2.2–2.3, Prop 2.4, Prop 2.6 (with §3 above), Lemma T, Lemma OC, 𝒯 and Prop K as refereed.
2. Re-word four things:
   - "any relational form" (C15);
   - "contains Cor 5.3", using VA′ instead (C20);
   - "strict generalisation of Lemma 3.4": the hypotheses are incomparable, since Lemma OC trades global coherence for incoherent-model dominance;
   - "all axioms" for 𝒯 (C17).
3. Fix C21. Replace it with: "for every veto family with μ(R_j∩C) = 0, (VA2) fails in 𝒯".
4. Ledger: add the transitivity step for W62 Lemma `lem:dominance`, and the rows for E61 Thm 5.1 and C62 §6.3.
5. Status labels: §3.6 is informal, not PROVED. Criterion (B) stands as a scoped result. Criterion (A) remains open, and Prop K is the right calibration.
