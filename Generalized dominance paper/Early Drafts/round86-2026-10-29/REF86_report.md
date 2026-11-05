# REF86: referee report on ldg_countable.tex and app_ldg.tex

29 October 2026. Referee REF86. I read both .tex files line by line against GUIDANCE86.md and BRIEF86.md, and checked the compiled numbering in ldg_countable.aux and app_ldg.aux. I re-derived every written proof myself and did not rely on VER86_report.md. No source file was modified.

Labels: **ERROR** (a false statement or invalid step), **GAP** (a step that is true but not proved as written), **MINOR** (precision, notation or style), **OK**.

## Summary

- **No ERROR and no GAP in either paper.** Every written proof is complete and correct as it stands.
- All cross-references from the application to LDG are correct. This includes Theorem 3.4's part letters (a), (d) and (e), Corollary 3.5, and the orientation correspondence.
- Every hypothesis of each cited LDG result is verified in the application.
- Both builds are clean: no errors, warnings, undefined references, or overfull or underfull boxes. LDG is 7 pp and the application 13 pp, both within the 15-page ceiling.
- Author lines are exact, `\coloneqq` is used throughout, and the jargon list does not occur.
- There are 17 MINOR points, listed below. The ones most worth fixing are:
  - L4: the separate statement of (S_σ) and (T_σ) leaves open which family (T_σ) refers to. The same issue is A10.
  - L7: the "is replaced by" wording in LDG §4 reads as a comparison of versions.
  - A2: notation clashes in the application (L, d, P, C).
  - A12: the Scope section does not mention (M1)–(M2).
  - S1: theorem environments in the application carry citations in their optional argument.

---

## Part I. ldg_countable.tex

### Section 1 (setting)

**OK: Definitions 1.1–1.6.** The ranking, dominance, pmf, coherent class, tie-closure, evaluability and admissibility definitions are all explicit, and each has a one-sentence gloss. C_L = C ∩ U_L is stated correctly. No property of the relations is assumed.

**OK: Lemma 1.7.** The main claim and (a)–(c) are correct. In (c), m ∉ 𝒜 and closure under ties rule out a tie at every world. (b) is then (c) with 𝒜 = C_L.

**L1 (MINOR): remark after Lemma 1.7.** The counterexample does not name the set 𝒜.
- Fix: name it.
- Replacement: "…in (c): take one world, two models a and m, each at least as good as the other, and 𝒜 ≔ {a}. Then a is undominated, a ∈ 𝒜 and m ∉ 𝒜, but a weakly dominates m without dominating it."

### Section 2 (selection)

**OK: Lemma 2.1 (KKM).** The proof is correct.
- Each A_ω is nonempty by coverage at δ_ω.
- G maps Δ_F into Δ_F continuously.
- A fixed point gives p_ω s = d_ω for every ω, and coverage at some ω ∈ supp p forces s = 0.

**L2 (MINOR): letter clash.** The Brouwer map in Lemma 2.1 is called G, but G later denotes a finite set of worlds (Definitions 2.2–2.3 and Theorem 2.5).
- Fix: rename the map Φ.
- Replacement: "The map Φ(p)_ω ≔ (p_ω+d_ω(p))/(1+s(p)) is continuous … with Φ(p)=p …"

**OK: Definitions 2.2–2.4.**
- The data are: compact Θ_j, with no separation axiom (correctly flagged, since the FIP argument needs none); b^j_θ ∈ M_L, as VER86 (6b) requires; and, for every finite G including ∅, a nonempty finite F_j(G) ⊇ G with an arbitrary map t_{j,G}.
- (W1)–(W3) are stated exactly.
- The tie clause is universal over ⋂_ω K_ω(x), and the text explains why an existential clause would assume the conclusion.
- The order of quantifiers is stated explicitly and is correct.

**OK: Theorem 2.5.**
- For each finite G, KKM gives p_G, and (W2) gives t_{j,G}(p_G) ∈ K_ω for all ω ∈ F_j(G) ⊇ G. This is the finite-intersection property, using every finite G, not a sequence of them.
- Compactness then gives ⋂_ω K_ω ≠ ∅.
- (W1) gives weak dominance, and exclusion of ties upgrades it to dominance.
- No coherence, relation property or model structure is used, as claimed. Countability is correctly said to play no role in the proof.

**L3 (MINOR): hypothesis of Theorem 2.5.** "Suppose L satisfies countable selection on I" is stronger than the proof uses. Only a fixed family and one x with witnesses are needed.
- Fix (optional): "Fix a countable family of assignments for L, and let x ∈ M_L have witnesses at index j. Then …" The app's restatement (Theorem 5.2) would follow.

**OK: Corollary 2.6.** Continuity makes the preimages closed, (W2) holds by construction, and (W3) is the hypothesis.

**OK: Corollary 2.7.** The instantiation Θ_j = Δ, F_j(G) = Ω, t = id and K = A is correct. Δ is compact and F_j(G) ⊇ G.
- MINOR wording: the conclusion uses x and j as free variables. Write "Then, for every x ∈ I and its index j, ⋂_ω A_ω(x) ≠ ∅ …".

**OK: Lemma 2.8 and Corollary 2.9.**
- If b ∈ C_L is tied with x at every world, tie-closure gives x ∈ C_L. Incoherent models are not in C_L ⊆ C.
- 2.9(a) and (b) follow from Theorem 2.5.

### Section 3 (dominance argument)

**OK: Definition 3.1 and Lemma 3.2.** The equivalence "irrational ⇔ not permissible" is correct and needs no (E).
- MINOR: the proof of the second sentence stops at "some ranking evaluates it". Add: "…by evaluability some L ∈ 𝔏 evaluates it, and irrationality gives a dominator under that L."

**L4 (MINOR, precision): Definition 3.3, (T_σ).** "The index and witnesses in (S_σ) … can be chosen to exclude ties" does not fix the family. (S_σ) may hold with several families, but tie exclusion must hold for the same family that supplies the witnesses. Definition 2.4's "with exclusion of ties" is unambiguous, so use it.
- Replacement for (T_σ): "**(T_σ)** *Exclusion of ties*: the family in (S_σ) can be chosen so that, in addition, the index and witnesses for each incoherent x ∈ M_L exclude ties; that is, L satisfies countable selection on M_L∖C with exclusion of ties (Definition 2.4)."
- Apply the same fix in Corollary 3.5. Replacement: "Let L satisfy countable selection on M_L∖C with a family whose assigned models all lie in C_L. If the witnesses for this family can be chosen to exclude ties, or if L is closed under ties, then …".

**OK: remark "Exclusion of ties cannot be dropped".** With one world and all four comparisons holding, a and m are tied. Both are undominated and C_L = {a}. (E), (A) and (S_σ) hold with the constant assignment a, and m is permissible. Correct.

**OK: Theorem 3.4 (a)–(e).** Each part has exactly the hypotheses its proof uses.
- (a) uses only (S_σ) and (T_σ). U_L ⊆ C follows from the dominance of incoherent models, and C_L ⊆ U_L holds by definition. It does not use coherent assigned models, as GUIDANCE §3.4 requires.
- (d) does not use (E), as VER86 (8a) requires.
- The note after the theorem says this correctly.

**OK: Corollary 3.5.** Tie-closure gives (T_σ) by Lemma 2.8, and Corollary 2.9(a) with I = M_L∖C gives dominators in C_L. Since I ∩ C = ∅, I ∖ C_L = I. The lift to families is correct. (L4 applies to the wording.)

**OK: summary (P1)–(P3)/(C) and the companion-paper paragraph.** The companion paper is described accurately:
- the coherent class is the almost coherent models;
- the ranking has full domain;
- the assigned models lie in C_L;
- there are no ties between distinct models, so C_L is trivially closed under ties.
Corollary 3.5 therefore applies. The paragraph cites no theorem numbers, so it cannot go stale.

### Section 4 (countable versus single assignment)

**L5 (MINOR): "Without some such restriction the condition would be empty".** The condition would not be empty. It would be trivially satisfied by every dominated x, that is, equivalent to dominance.
- Replacement: "Without some such restriction the condition would add nothing to dominance itself: if the assignment could be chosen separately for each x, …"

**L6 (OK): the limitation paragraph.**
- Constant assignments from countably many known dominators do satisfy countable selection with exclusion of ties.
- The disclaimer about converses matches GUIDANCE §3.5.
- The paragraph does not say that countability drives the KKM argument.

**L7 (MINOR, house style): version-comparison wording.** The guidance requires this paragraph's content, but "One common assignment **is replaced by** a fixed countable family … Closure of C_L under ties **is replaced by** exclusion of ties" reads as a comparison between versions. Phrase it as a comparison of two conditions that are both defined in the paper.
- Replacement: "Countable selection on M_L∖C with exclusion of ties is weaker than single-assignment selection on M_L together with closure under ties, in four respects. It allows a fixed countable family of assignments, and each model to be dominated may use any one of its members. It requires witnesses only for incoherent models. It requires the exclusion of ties only at the points common to all the witnessing sets, not closure of C_L under ties. Neither requires a dominance conclusion or a coherent dominator: these are derived (Theorem 2.5, Corollary 3.5)."
- In the next paragraph, replace "instead specifies" with "specifies".

**OK: Example 4.1.**
- The relations are: reflexivity, c₁ ⪯ x₁ and c₂ ⪯ x₂. Each c_i is undominated, ties are only self-ties, and C_L is closed under ties.
- Two constant assignments give witnesses with exclusion of ties: c_i ⪯ x_i, but x_i ⪯ c_i fails.
- No single assignment works. For G = Ω, F₁(Ω) = Ω and Δ_Ω = {δ_ω}, so θ₀ would have to lie in K_ω(x₁) ∩ K_ω(x₂). But {m: m ⪯ x₁} = {c₁, x₁} and {m: m ⪯ x₂} = {c₂, x₂} are disjoint. Correct.

**OK: Example 4.2.** Each index j fixes one model b^j_{θ_j}. That model can be ⪯ x_t only if it lies in {c_t, x_t}, which determines t. So countably many indices serve countably many x_t. Correct.

**L8 (MINOR): empty abstract.** `\begin{abstract}\end{abstract}` prints an empty "Abstract" heading. The application has no abstract environment at all.
- Fix: delete the environment, or supply a placeholder for the author.
- Suggested text: "We prove that, for arbitrary worlds and arbitrary world-indexed relations, a countable family of assignments fixed in advance, together with closed comparison witnesses that cover every finitely supported prior, yields dominance of every incoherent model. A dominance principle then classifies the coherent models as exactly the rationally permissible ones."

---

## Part II. app_ldg.tex

### Section 1 (setting and geometry)

**OK: Definition 1.1 and the infinite-world sentences.**
- E is separable, norm-closed and contains 𝟙.
- ℓ^∞(Ω) is excluded for infinite Ω and C(Ω) is allowed for compact metrizable Ω. This is accurate and stated in two sentences.

**OK: Definitions 1.2–1.3.** D1–D4 agree with app_short.tex, using g in place of f. The definitions of P_Q, D°_Q, C_Q and D_Q are exact.

**OK: Lemma 1.4.**
- (a) S lies in the unit ball, is weak-* closed and hence compact (Banach–Alaoglu). The metric Σ2^{-n}|q(h_n) − r(h_n)| gives a continuous bijection from a compact space onto a Hausdorff space, so S is metrizable.
- (b) Correct.
- (c) Lipschitz, superadditivity, homogeneity, monotonicity and translation all hold. conv(Q₁∪Q₂) is the continuous image of Q₁×Q₂×[0,1], since Q₁ and Q₂ are convex, and the min formula holds.
- (d) Correct.
- (e) Correct, with the bound inf_{Ω₀}h ≤ inf_Ω h + 2η.

**OK: Lemma 1.5.**
- (D1)–(D4) hold. In the mixed case of (D4), superadditivity with P_Q ≥ 0 on D_Q gives the result.
- Borel measurability holds.
- (b) and (c) follow by taking the union with {g ⪈ 0}.

**OK: Definitions 1.6–1.7.** Only (M1) and (M2) are assumed. Full support and atomlessness are not, and (M3) is not carried over. One μ is fixed, so M, almost coherence and C are unambiguous, and the results are stated per μ (GUIDANCE §4).

**OK: Lemma 1.8.**
- (a) The Hahn–Banach argument for the open cone V = D + D°_S is correct. The limits λ → 0 and λ → ∞ give c ≤ 0 and φ ≥ 0 on V, and positivity, φ(𝟙) > 0, q ∈ K_D and q(h) ≤ 0 follow. h = 0 gives K_D ≠ ∅.
- (b) D∖D_{K_D} ⊆ {P_{K_D} = 0} is null by (M2). The identification "almost coherent ⇔ D_Q a.e." is proved, and D_Q = D°_Q a.e. is stated once (GUIDANCE §4).
- (c) D_P ∩ {q>0} differs from D_{conv(P∪{q})} only inside {q = 0}, which is null by (M2) applied to {q}.
- Nowhere is exact coherence claimed for b^j_q. VER86 item 9 is respected.

**OK: Definition 1.9 and the paragraph after it.** Bochner integrability follows from Borel measurability, separable range and (M1). Functionals commute with the integral. Diestel–Uhl comes from the author's app_long.

**OK: Definition 1.10 and Lemma 1.11.**
- (a) Convexity, closedness and monotonicity hold. Closedness is tested by sequences, which metrizability permits.
- (b) A dense sequence in Q_B gives P_{Q_B} ≥ 0 a.e. on B, and (M2) gives B ⊆ H(B) a.e.
- (c)–(e) are correct.

**OK: Lemma 1.12 (contraction).** Ψ maps Q_Z into Q_Z, because q′ ≥ P_{Q_Z} pointwise and the null sets combine. The iterates converge to q in norm, Q_Z is nonempty and closed, and a = 0 is trivial.

**OK: Lemma 1.13 (trimming).** All three cases are covered:
- g ∈ Z ∩ D°_{Q_τ} gives q(g) ≥ P_S(g) > −aP(g);
- g ⪈ 0 gives q(g) ≥ 0 ≥ −aP(g);
- a.e. g ∈ Z∖N gives q(g) ≥ 0 and P(g) ≥ 0, by Lemma 1.11(b), which does not need (M2).

The covering Z ⊆ (Z∩D_{Q_τ}) ∪ (Z∖N) ∪ (N∖D_{Q_τ}) is correct. The proof is complete and needs no early-draft citation (GUIDANCE §7).

### Section 2 (ranking)

**OK: Definition 2.1 and the orientation paragraph.** "LDG's a ⪯_ω x is our a ⪰_ω x" is correct. Under this reading, LDG's weak dominance, ties, dominance, U_L and C_L (LDG Definitions 1.2 and 1.4) coincide with those here, M_L = M, and LDG's C is the class of almost coherent models.

**OK: Definitions 2.2–2.4.**
- Guidance is world-by-world, not the old "guided at all worlds".
- Independence is stated for arbitrary contexts.
- Finite-chain consistency, the three-model condition and tie substitution are defined explicitly.
- Each has a gloss. Transitivity is not claimed.

**OK: Lemma 2.5.** The countable Ω₀ from Lemma 1.4(e) reduces the problem to a countable union of null sets, so no uncountable union is ever taken (GUIDANCE §5). The D1/D2/D4 argument for B ∩ C is correct.

**OK: Proposition 2.6 (a)–(f).**
- (a) m(Y) − m(X) = m(A) − m(B), and the guidance and hull clauses depend only on the a.e. classes of A and B (Lemma 1.11(e)). This gives well-definedness on classes, full evaluability and independence.
- (c) There are no ties between distinct classes at any world, and ≻ coincides with "⪰ and ≠".
- (d) The gain is ∫_{A∪B}|g(ω)| dμ > 0.
- (e) The chain gives m(X₀)(ω) ≥ m(X_k)(ω), which contradicts strictness.
- (f) is trivial.

### Section 3 (admissibility first)

**OK: Proposition 3.1.**
- Hull case: B ⊆ D_Q gives H(B) ⊆ D_Q, so A is null and m(B) < 0 at every world. For q ∈ Q, q > 0 a.e. on B by (M2), so q(m(B)) > 0, contradicting q(m(B)) ≤ 0.
- Guided case: Lemma 2.5 forces A and B to be null.
- The proof is placed before selection, as GUIDANCE §5 and §9 require.

### Section 4 (fixed assignments)

**OK: Definition 4.1.** The lists are countable, include the empty list (P = S), and depend only on (h_k). Strict margin is defined.

**OK: Lemma 4.2 (approximation).**
- *Separation.* The cited Rudin results are correct: Theorem 3.10 for the dual of the weak-* topology and Theorem 3.4(b) for compact/closed separation. The margin arithmetic gives r(h_k) < P_Q(h_k) − η.
- *Lists.* The finite subcovers of S∖U_n, the concatenation, strict margins (so Q ⊆ P_{j_n}), P_{j_n} ⊆ U_n and ⋂P_{j_n} = Q are all correct. The case P = S (empty list) is handled.
- *(c).* λ_n = min{½, min_i ε_i/(2‖h_{k_i}‖+1)} gives (1−λ_n)Q + λ_nS ⊆ P_{j_n}, with strict inequality.
- The closing sentence says correctly that interior containment also suffices by compactness. It therefore does not repeat the implication that GUIDANCE §6 calls unjustified, and it agrees with VER86 item 2.
- *(d).* ⋃_n D_{P_{j_n}} = D_Q holds exactly, so (M2) is not needed here, and the lemma correctly assumes only (M1). Dominated convergence then gives the integral limit.

**OK: Definition 4.3 and Lemma 4.4.**
- F(∅) ≔ {ω₀} is fixed, as VER86 (6a) requires.
- (a) b^j_q is Borel, almost coherent by Lemma 1.8(c), and undominated by Proposition 3.1.
- (b) Correct.
- (c) Norm continuity: the indicators converge off the null set {q = 0}, which covers boundary states including δ_ω, and dominated convergence applies.
- (d) Correct.

### Section 5 (selection and dominance)

**OK: dependency paragraph.** It shows the dependency GUIDANCE §9 asks for: geometry, then assignments and witnesses (Lemmas 5.5–5.7), then the LDG compactness theorem, then dominance. Admissibility is proved separately.

**A1 (MINOR): Definition 5.1, (W2)/(W3).** The quantifier "for every finite G and every ω ∈ F_j(G)" appears only in the lead-in.
- Replacement: "(W2) t_{j,G}(A^G_ω(x)) ⊆ K_ω(x) for every finite G ⊆ Ω and every ω ∈ F_j(G); (W3) for every finite G ⊆ Ω, every p ∈ Δ_{F_j(G)} lies in A^G_ω(x) for some ω ∈ supp p."

**OK: Theorem 5.2.** It restates LDG Theorem 2.5 word for word, apart from the orientation.

**OK: Definition 5.3.** It agrees with LDG Definitions 3.1 and 3.3, with M_L = M.
- A10 (MINOR): (T_σ) has the same family ambiguity as L4.
- Replacement: "(T_σ) the family in (S_σ) can be chosen so that the witnesses for every incoherent model exclude ties."

**OK: Theorem 5.4.**
- (a) matches LDG Theorem 3.4(a) and LDG Corollary 3.5. The hypotheses match: (S_σ), (T_σ), and assigned models in C_L.
- (b) matches LDG Theorem 3.4(d), with hypotheses (A), (S_σ) and (T_σ).
- (c) matches LDG Theorem 3.4(e), with hypotheses (E), (S_σ) and (T_σ).
- All the part letters agree with the final LDG numbering, including the change of part letters recorded in WL86_changes.md.

**OK: Lemma 5.5 (gap), consistent case.**
- φ ≥ 0 because X ⊆ G a.e.
- φ(q) = 0 forces X = G ∩ {q>0} a.e., using (M2) on {q}. That set is almost coherent, which contradicts the incoherence of X.
- Continuity follows by dominated convergence with bound ‖g‖, and compactness gives γ > 0.

**OK: Lemma 5.5, inconsistent case.**
- f < 0 because Q_X = ∅.
- *Derivative.* The quotient is bounded by 2‖g‖ and converges pointwise off {q₀ = 0}, which is one null set independent of ω. Dominated convergence along t_n ↓ 0 gives m(L)(ω) ≤ q₀(m(L)) = −d for every world. The argument is valid for arbitrary Ω.
- *Gap.* ∫_{H(Z)}q⁺ ≥ q(m(Z)) and q(m(L)) ≤ −d give the bound d.

**A2 (MINOR, notation): the application reuses several letters.**
- The ranking is L (and L_μ), but in Lemma 5.5 L is also the set X ∩ {q₀<0}.
- d is a metric (Lemmas 1.4 and 4.2), −f(q₀) (Lemma 5.5), and γ/2 (Lemma 5.7). The last two conflict because γ = d in Lemma 5.5.
- P is P_{Q_Z} (Lemmas 1.12–1.13), a credal set (Lemma 1.8(c)), and a listed set (Lemma 5.6).
- C is an almost coherent model (Proposition 3.1), C_Q is a cone, and 𝒞 is the class.
- Three different dense sequences are called (h_n), (h_j) and (h_k).

Fix:
- In Lemma 5.5, rename L to X⁻ and d to β, so that γ ≔ β.
- In Lemma 5.7, rename d to κ ≔ γ/2.
- In Lemmas 1.12–1.13, write \underline P_Z ≔ P_{Q_Z}.
- In Proposition 3.1, write the model as K.
- In Lemma 1.4(a) and (e), use (e_n) and (u_j) for the dense sequences.

**OK: Lemma 5.6 (choice of index).**
- Lemma 4.2(d) gives e < γ/2, and Lemma 4.2(c) gives the homothety, so D_P ⊆ D_{(1−λ)Q+λS}.
- Trimming with N = D_P gives H(Z∖D_P) = G.
- The chain A_q ⊆ b_q ⊆ D_P ⊆ G = H(Z∖D_P) ⊆ H(X∖D_P) ⊆ H(X∖b_q) holds exactly, for every q, using Z ⊆ X and Lemma 1.11(d) twice. This is GUIDANCE §7 Step 2 verbatim.
- (b) uses D_P ⊆ G and q⁺ ≤ ‖g‖.
- (c) follows from Definition 2.3 together with (a).

**OK: Lemma 5.7 (witnesses).**
- Closedness follows from Lemma 4.4(c) and (d).
- (W1) follows from Lemma 5.6(c).
- (W3) follows from Lemma 5.6(b) at q = t_F(p) by averaging over supp p. Note supp p ⊆ F(G).
- Exclusion of ties: on ⋂K_ω the gain is at least d at every world, so b ≠ X, and Proposition 2.6(c) excludes ties at every world. This is the universal clause.
- The order of quantifiers is correct. The data (h_k), (ℓ_j), b^j_q, F and t_F depend only on E and ω₀. Z, γ, j, K_ω and A^G_ω are chosen per X.

**OK: Theorem 5.8.**
- (a) follows from Proposition 2.6 and (b) from Proposition 3.1.
- (c) verifies every hypothesis of LDG Theorem 2.5 and LDG Definition 3.3 (see the table below).
- (d) applies Theorem 5.2 to get a dominator, which is almost coherent and undominated by Lemma 4.4(a), with uniform margin ≥ d.
- (e) follows correctly.
- The statement matches GUIDANCE §8. The paper calls the dominator "almost coherent", never "coherent", as VER86 item 9 requires.

**OK: the paragraph after Theorem 5.8.** It does not claim that L_μ is the unique ranking with these properties, or that coherent admissibility has an independent justification (GUIDANCE §8).

**A3 (MINOR): Corollary 5.9, last sentence.** "These hypotheses … continue to hold when every member of 𝔏 is required, in addition, to satisfy world-by-world guidance and independence" is ambiguous. The intended claim is that the restricted class of families is nonempty.
- Replacement: "In particular 𝔏 ≔ {L_μ} satisfies these hypotheses, and its member also satisfies world-by-world guidance and independence; so the conclusions hold for, and are not vacuous over, families of rankings that are in addition required to satisfy guidance and independence. More generally, (A) may be assumed for 𝔏 directly, without L_μ ∈ 𝔏."

The proof of Corollary 5.9 is OK. The note on (E) after it is also correct: D_S ∈ 𝒞 and (A) force 𝔏 ≠ ∅, and full-domain rankings then give (E).

### Section 6 (measures)

**OK: Lemma 6.1(a).** All properties are verified:
- (M1): Σw_k‖f_k‖ ≤ cΣ2^{-k}.
- (M2): Pr(T = −P_Q(f_k)) = 0.
- Atomless.
- Full support, via the ball B(g, r).

The standard normal law is a concrete choice satisfying the GUIDANCE §8 conditions.

**OK: Lemma 6.1(b).** Separation gives an open W ⊆ D°_Q disjoint from D_{Q′}, and full support gives μ(W) > 0.

### Section 7 (Scope)

**A12 (MINOR): scope sentence.** The section is accurate on almost coherence (the D ∪ {0} example is correct, since {0} ⊆ {P_S = 0} is null under (M2)) and on separability. It omits that everything is relative to a fixed μ satisfying (M1)–(M2). Adding this keeps the section to two sentences.
- Replacement for the second sentence: "The results hold for each finite Borel measure satisfying (M1) and (M2) on a separable gamble space, so the full space of bounded gambles on an infinite set of worlds is not covered; and they neither provide a single assignment serving all incoherent models nor derive dominance from guidance and independence alone."

---

## Part III. Cross-references and hypotheses

### Numbering (checked against ldg_countable.aux)

| Application cites | LDG label | LDG number | Content match |
|---|---|---|---|
| Definitions 2.2–2.4 | def:family, def:witnesses, def:selection | 2.2, 2.3, 2.4 | OK |
| Theorem 2.5 | thm:general | 2.5 | OK, verbatim up to orientation |
| Definitions 3.1, 3.3 | def:permissibility, def:argument-assumptions | 3.1, 3.3 | OK |
| Theorem 3.4(a) | thm:argument (a) | 3.4(a) | OK: dominance under L and U_L = C_L |
| Theorem 3.4(d) | thm:argument (d) | 3.4(d) | OK: partition, with (A), (S_σ), (T_σ) |
| Theorem 3.4(e) | thm:argument (e) | 3.4(e) | OK: non-vacuity, with (E) |
| Corollary 3.5 | cor:coherent-dominators | 3.5 | OK: dominators in C_L |

LDG cites the application only by title, with no numbers. OK.

### Orientation

LDG's a ⪯_ω x means "a performs at least as well as x", and the application's a ⪰_ω x means "a is at least as good as x". The correspondence is stated in the application at §2 and again after Definition 5.1, and each paper uses one convention throughout. OK.

### Hypotheses of each cited LDG result, as verified in the application

| LDG hypothesis | Where verified |
|---|---|
| Ω nonempty; M nonempty; 𝒞 fixed independently of the rankings | Definitions 1.1 and 1.7 (μ is fixed first) |
| Relations ⪯_ω on M_L, well defined | Proposition 2.6(a); M_L = M |
| Θ_j compact | Lemma 1.4(a) (Θ_j = S) |
| b^j_θ ∈ M_L | Lemma 4.4(a) |
| F_j(G) nonempty, finite, ⊇ G for every finite G including ∅ | Definition 4.3 |
| Data fixed independently of x | Definition 4.3 and Theorem 5.8(c) |
| K_ω(x), A^G_ω(x) closed | Lemma 5.7 (closedness) |
| (W1), (W2), (W3) | Lemma 5.7 |
| Exclusion of ties (universal) | Lemma 5.7 (ties) |
| Assigned models in C_L (Corollary 3.5) | Lemma 4.4(a) and Proposition 3.1 |
| (A) (Theorem 3.4(d)) | Theorem 5.8(b), or by assumption in Corollary 5.9 |
| (E) (Theorem 3.4(e)) | The note after Corollary 5.9 |

All hypotheses are verified. OK.

---

## Part IV. House style

| Check | ldg_countable | app_ldg |
|---|---|---|
| Theorems, lemmas, propositions and corollaries unnamed | OK | **S1 (MINOR)**, see below |
| Definitions with short bracketed names; one-sentence gloss each | OK | OK |
| `\coloneqq` throughout; no `:=` or `=:` | OK | OK |
| No jargon (certificate, record, gate, route, safe, catalogue, shelter, dangerous) | OK (grep clean) | OK (grep clean) |
| No historical labels or version-comparison commentary | **L7 (MINOR)** | OK |
| Author line exactly "Jason Konek" | OK | OK |
| One orientation per paper | OK | OK |
| Cuts per GUIDANCE §3.6 and §9 | OK | OK: no consolidation, maximality, boxes, numerics, repair theorem, ρ-robustness or subcover |

**S1 (MINOR).** `\begin{theorem}[{\cite[Theorem~2.5]{LDG}}]` and `\begin{theorem}[{\cite[Theorem~3.4 and Corollary~3.5]{LDG}}]` put a citation in the theorem-name slot. This is common practice, but to follow the "unnamed" rule strictly, move the citation into the body.
- Replacement: "\begin{theorem}\label{thm:LDGgeneral} The following is \cite[Theorem~2.5]{LDG}. Let L satisfy …", and similarly for Theorem 5.4.

**S2 (MINOR, optional).** The last sentence of Lemma 4.2(c) ("it also follows from Q ⊆ int_S P …, which is not needed here") is commentary. It can be cut under the formal-core rule. It is accurate.

---

## Part V. Bibliography

### \bibitem entries in the drafts

| Item | Paper | Verdict |
|---|---|---|
| KCM: Konek, *Coherence and accuracy for sets of desirable gambles*, manuscript, 2026 | LDG | OK. It matches the application's title and ldg-references.bib (Konek2026). |
| KKM: Knaster, Kuratowski, Mazurkiewicz, "Ein Beweis des Fixpunktsatzes für n-dimensionale Simplexe", *Fund. Math.* 14 (1929) 132–137 | LDG | OK. This is the standard citation. |
| LDG: Konek, *Coherence and dominance under general rankings*, manuscript, 2026 | App | OK. It is taken from app_short. |
| Rudin, *Functional Analysis*, 2nd ed., McGraw-Hill, New York, 1991 | App | OK. Theorem 3.4 (separation) and Theorem 3.10 (the X′-topology and its dual) are correctly numbered for the 2nd edition. **MINOR:** Banach–Alaoglu is cited without a number; add "[Theorem 3.15]". |
| Diestel and Uhl, *Vector Measures*, AMS, 1977 | App | OK. It is taken verbatim from the author's app_long. The full form is "J. Diestel and J. J. Uhl, Jr., *Vector Measures*, Mathematical Surveys 15, AMS, Providence, RI, 1977". Adding "Jr." and the series is optional. |

No invented details.

### ldg-references.bib (not used by either draft)

Neither draft uses this file, since both use `thebibliography`. The entries are nonetheless as follows.
- Correct as standard: de Finetti 1974; Wald 1950; KKM1929; Predd et al. 2009 (IEEE TIT 55, 4786–4792); Briggs and Pettigrew 2020 (Noûs 54, 162–181); Joyce 2009 (Synthese Library 342, 263–297); Pettigrew 2016 (OUP).
- SSK2009 (*Decis. Anal.* 6, 202–221): confirmed, including the note's reference to CMU Statistics Technical Report 865 (stat.cmu.edu/tr/tr865).
- Exist, but pages not independently confirmed:
  - Pettigrew 2022 (*Philos. Sci.* 89, 128–151) is confirmed on the Cambridge and PhilArchive records.
  - Nielsen 2023 (*Mind* 132, 402–427) is confirmed on PhilArchive and X-MOL.
  - Nielsen 2021 (*Philos. Stud.* 178, 3217–3236): I could not confirm the volume and pages here.
- Flag these three page ranges for the author to check if any entry is later cited.

---

## Part VI. Theorem-by-theorem verdicts

### ldg_countable.tex

| Result | Verdict | Notes |
|---|---|---|
| Definitions 1.1–1.6 | OK | |
| Lemma 1.7 (ties) | OK | L1 (remark wording) |
| Lemma 2.1 (KKM) | OK | L2 (rename map) |
| Definitions 2.2–2.4 | OK | |
| Theorem 2.5 (general compact theorem) | OK | L3 (optional hypothesis trim) |
| Corollary 2.6 (inverse images) | OK | |
| Corollary 2.7 (finite worlds) | OK | Free-variable wording |
| Lemma 2.8 (tie sufficiency) | OK | |
| Corollary 2.9 | OK | |
| Definition 3.1, Lemma 3.2 | OK | Complete the second sentence of the proof |
| Definition 3.3 ((E), (A), (S_σ), (T_σ)) | OK | L4 (fix the family in (T_σ)) |
| Tie-necessity remark | OK | |
| Theorem 3.4 (a)–(e) | OK | |
| Corollary 3.5 | OK | L4 wording |
| §4 paragraphs | OK | L5, L7 |
| Example 4.1 | OK | |
| Example 4.2 | OK | |
| Front matter | OK | L8 (empty abstract) |

### app_ldg.tex

| Result | Verdict | Notes |
|---|---|---|
| Definitions 1.1–1.3 | OK | |
| Lemma 1.4 (states) | OK | Add the Banach–Alaoglu theorem number |
| Lemma 1.5 (D_Q) | OK | |
| Definitions 1.6–1.7 | OK | |
| Lemma 1.8 (identification) | OK | |
| Definition 1.9 (payoff) | OK | |
| Definition 1.10, Lemma 1.11 (hull) | OK | |
| Lemma 1.12 (contraction) | OK | A2 notation |
| Lemma 1.13 (trimming) | OK | A2 notation |
| Definitions 2.1–2.4 and orientation | OK | |
| Lemma 2.5 (guidance at every world) | OK | |
| Proposition 2.6 (ranking properties) | OK | |
| Proposition 3.1 (admissibility) | OK | A2 notation (C) |
| Definition 4.1, Lemma 4.2 (approximation) | OK | S2 optional |
| Definition 4.3, Lemma 4.4 (assignments) | OK | |
| Definition 5.1 | OK | A1 (quantifiers) |
| Theorem 5.2 (cites LDG 2.5) | OK | S1 |
| Definition 5.3 | OK | A10 (= L4) |
| Theorem 5.4 (cites LDG 3.4(a),(d),(e) and 3.5) | OK | S1 |
| Lemma 5.5 (gap) | OK | A2 (L, d) |
| Lemma 5.6 (index and hull chain) | OK | |
| Lemma 5.7 (witnesses) | OK | A2 (d) |
| Theorem 5.8 (main) | OK | |
| Corollary 5.9 | OK | A3 (last sentence) |
| Lemma 6.1 (measures) | OK | |
| §7 Scope | OK | A12 (add (M1)–(M2)) |

**Overall verdict.** Both drafts are mathematically complete and correct in their declared scope: almost coherence, a separable E, and a fixed μ satisfying (M1)–(M2). Cross-references and hypothesis verification are exact. Only MINOR drafting and style revisions remain, and none affects any result.
