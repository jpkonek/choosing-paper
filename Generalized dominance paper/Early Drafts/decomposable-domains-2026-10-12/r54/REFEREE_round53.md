# REFEREE for round 54 (file name as briefed: REFEREE_round53): imported results for the refusal allocation

23 October 2026. Independent referee for Brief 54. I referee PP56 §4–5, PP57 §4–5, PP55 (Prop F, Thm 5.1′, Prop SR), Theorem K′ (REFEREE_round52 = PP60, §4.4; memo §8.22), the audit's robust refusal lemma, and the audit's alternative theorem. I also give a ledger of where each "already killed" architecture applies. I add no axiom. The setting is Brief 54's.

**Labels.**
- PROVED: a complete argument is given or checked here.
- CHECKED: an exact computation (Fractions) in `r9/REFEREE53_py/`, or a re-run whose output matches the author's.
- NUMERICS: floating-point or sampled evidence. LPs only propose; every witness is verified exactly.
- OPEN: as stated.

**Verdict scale.** correct / correct with repair / wrong.

**Conventions.** "X ⪯_w Y" means X is at least as good as Y at w. A *record* is (support, old advice, new advice). Δ^ℓ_w(X, Y) = ∫ [u^ℓ_w(Y) − u^ℓ_w(X)] dμ.

---

## 0. Summary of verdicts

| # | Item | Verdict |
|---|---|---|
| 1a | PP56 (2V), and its validity on small posterior neighbourhoods | **correct**. The region where it holds is explicit: normalise(1/a) ≥ c coordinatewise, equivalently u ∈ M_a. It contains B and D (CHECKED). |
| 1b | Balanced field u¹ | **correct** (CHECKED independently on a 41-member sampled family) |
| 1c | Theorem L: (IB), (TC), no ties (π–λ), strict (G), protection; all measurable rivals | **correct**. One cosmetic repair: take the boxes in a fundamental domain of g ↦ −g. |
| 1d | Cor 4.3 (no section-free certificate) | **correct**, within the module's scope (M7: protection for selected models only; no global (C)) |
| 1e | Prop 5.1 (Λ-type relations have a non-closed section) | **correct** |
| 1f | Prop 5.2 (staircase) | **correct as a consistency statement for the listed clauses only** (CHECKED exactly). The audit is right: it is a set of selected comparisons, not a relation. In addition its parameter indexes the **rival**, so it concerns changing-rival closedness, not (S). The "two-parameter" morals drawn downstream do not follow. |
| 2a | (L0⁺) | well posed. It is a hypothesis about architecture, not an axiom. |
| 2b | Lemma 4.1 (pure shifts) | **correct with repair (wording)**. "C_b answers wherever C_a does" is false. The monotonicity conclusion is true (CHECKED: 116 sampled counterexamples to the wording, 0 to the conclusion). |
| 2c | Theorem Q (i), (ii) | **correct**. (ii) needs C_b selected; it then violates direct (C) as encoded. |
| 2d | PP57 Cor 4.3 | **correct** (needs u and B interior to N_u) |
| 2e | Cor 4.4 and its OPEN item | **correct as a conditional**. The OPEN item is genuine: the degenerate case reduces to a two-dimensional cancellation question, stated in §2.5. |
| 2f | Prop 4.5 | **correct with repair (wording)**: "the section is open" should read "the section is not closed at the source" |
| 2g | Lemma 5.1 | **correct, and only local openness**. The audit is confirmed: there is no monotonicity along a ray, and nothing specific to improving directions. |
| 3a | PP55 Prop F (with F′, F″, Prop B) | **correct**, on finite instances |
| 3b | Thm 5.1′ | **correct with scope repair**: the (R) branch is local to the triple; (H*) is essential |
| 3c | Prop SR | (a) **correct**. (b) the **stated argument is wrong** (audit confirmed), but **the conclusion survives a two-case repair** (§3.3). (c) **does not follow** (audit confirmed); there is a concrete coupling the argument misses. Downstream claims that rest on SR or on Prop 5.2 are listed in §3.4. |
| 4 | Theorem K′ | **correct** as a gate-architecture theorem. The memo's gloss "PP55 Thm 5.1′ closes [exact indifference] too" is **overstated** (§4). |
| 5 | Robust refusal lemma | **correct**. All non-section conclusions survive, at every localisation level. The refusal is open in the source for the fixed rival. |
| 6 | Alternative theorem | **correct**. Full proof in §6.1; compact-family version in §6.2, under exact hypotheses. Within the reweighted construction it is an **exact** test for *open* refusals (§6.3). Finite sampling cannot replace the measure certificate (example in §6.4). |
| 7 | Ledger applicability | Only Theorem K/K′ and Theorem Q (with Cor 4.4) are local on N_u, and both are architecture-conditional. The single-field, M0, intersection and L4/R21 results are full-cover only. Theorem L is in fact a **local counterexample** to any section-free local reading of them. PP38 is local but specific to the fixed kernel ℓ^T (§7). |

---

## 1. PP56: (2V), u¹, Theorem L, Cor 4.3, Props 5.1–5.2

### 1.1 Hypothesis (2V) and where it holds

The posterior model C_a answers + at g iff Σ_i a_i m_{v,i} g_i > 0 at every vertex m_v of M. It answers − iff all three sums are negative.

**Claim (PROVED).** If u ∈ M_a, every answer of C_a has the sign of g₁ + g₂ + g₃.
- *Proof.* C_a answers x only if p·g has sign x for every p ∈ M_a, and p = u is one such p. ∎
- *Where it holds.* u ∈ M_a holds iff m := normalise(1/a) ∈ M, that is, iff m_i ≥ c for every i. This is a neighbourhood of u because u ∈ int M.
- B and D lie inside it: normalise(1/B) ≈ (0.328, 0.316, 0.357) > c = 0.2333.

So on any N_u inside this region the family answers only h(g) = sign(Σg) or S everywhere, and (2V) holds on R and off it.

**CHECKED (`ref53_posterior.py` (A)).**
- 22,079 exact random (a, g) pairs inside the region: no violation.
- Outside the region an answer against sign(Σg) is found, so the condition is not idle.

**Verdict: correct.**

### 1.2 The balanced field u¹

I re-derived the three rows.
- **On R, with x = h(g):** λ·u¹(x) = −|Wr||Cor| + |Cor||Wr| = 0 = λ·u¹(S).
- **The other answer:** λ·u¹ = |Wr||Cor| > 0, because a mixed sign makes both sets nonempty.
- **Common advice off R:** λ·u¹ = −|Wr||Cor| < 0.
- **Contradictory advice:** 3(1 + max|k|)|g| > 0.
- **Unanimous sign:** rank·|g|. Every coherent model answers correctly there.

Strict guidance needs −k_c < 0 < k_r < 1 + max|k|, which holds. The envelope is |u¹| ≤ 5|g|, which is μ-integrable. The field depends on 𝒮 only through R(𝒮) and the common advice. Both are Borel for the posterior family: ∩_a Ans(C_a) is open by compactness, and ∪_a Ans(C_a) is open.

**CHECKED (`ref53_posterior.py` (B)), from my own code.** On a family of 41 members (A, B, D and the 38 of 40 random indices that fell in the region), at 2,997 random problems:
- strict guidance at every world over all four values;
- every member pointwise λ-Bayes at λ = (1, 1, 1);
- exact balance on R;
- strict optimality off R.

**Verdict: correct.**

### 1.3 Theorem L

I checked each step.

1. **(IB).** Δ is an integral over the record's support of a fixed function of (g, advice). Correct.
2. **(TC) and reflexivity.** Δ is additive termwise. Lexicographic nonnegativity is closed under addition, and every sequence or its negative is ≥_lex 0. So each world is a total preorder, and (TC) is immediate (a 3-cycle forces all ties). Correct.
3. **No ties (π–λ).** Fix w, and X ≠ Y on a non-null E.
   - f = u¹_w(·, Y) − u¹_w(·, X) is integrable and ≠ 0 a.e. on E. At a.e. g the four advice values have distinct w-ranks, and u¹_w is strictly increasing in rank.
   - Suppose every level vanishes. Then ∫_A f = 0 for A = R³ (level 0) and for every rational open box.
   - The class {A Borel : ∫_A f = 0} is a λ-system: complements use the level-0 equation, and countable disjoint unions follow by dominated convergence. The rational boxes, with ∅, form a π-system generating the Borel sets. Dynkin's theorem gives ∫_A f = 0 for all Borel A, so f = 0 a.e., a contradiction.

   Correct. *Cosmetic repair.* Problems live in R³ modulo sign. The integrand is sign-symmetric and μ is symmetric, so the argument works on R³ as written. But in Prop 5.1 the balls and boxes should be taken inside a fixed fundamental domain (say {Σg > 0}), so that a box does not pick up the antipodal copy of a ball.
4. **Strict (G).** Weak (G) is also immediate. Correct.
5. **Protection.**
   - Each level is 1_B·u¹, so the pointwise inequality λ·(u^ℓ(X) − u^ℓ(N)) ≥ 0 survives localisation.
   - Take the first level ℓ₀ at which the vector V = (Δ^{ℓ₀}_w(N, X))_w is nonzero; it exists by step 3. Then λ·V ≥ 0 with λ > 0, so some V_w > 0.
   - At that w every earlier level is 0, so N ≺_w X.

   Correct. It uses nothing about X beyond measurability, so **the extension to all measurable rivals is correct**.

**Consequences.**
- Defence on supp a = {1, 2, 3} (all indices are interior).
- Undominatedness (its antecedent is always false).
- Direct (C) for coherent and incoherent rivals.
- (LA), since T = C_u ∈ 𝒮.

**Re-runs (CHECKED).** `cells56`, `lex56`, `instance56` and `kink56` reproduce their archived outputs byte for byte, and all end in ALL PASS.

**Verdict: correct.**

### 1.4 Corollary 4.3

Λ satisfies every listed axiom on N_u. So it satisfies every clause derivable from them, with any cells, subdivisions or advice values. That includes the SAFE ledger entries in point form, since their derivations use (TC), strict (G), (IB) and T's defence only.

**Scope.** The corollary is about the module (M7). It does not cover:
- global (C) ("every incoherent model is dominated", which is existential);
- protection of non-selected coherent models;
- any clause whose derivation uses a section.

PP56 says this. **Verdict: correct.**

### 1.5 Proposition 5.1

I re-derived all seven steps.
- Continuity of f^ℓ_w uses continuity in measure plus the 5|g| envelope.
- Injectivity together with step 3 of Theorem L gives a non-constant level.
- The topological lemma ("every point a local minimum ⇒ constant") holds: along a path the argmax set is open and closed.
- The two silent points can be chosen off all box boundaries, which are null. No box of index ≤ ℓ* separates them.
- The cancelling balls give a rival that agrees with C_{a′} on all levels < q and is strictly better at level q.
- Along a_k the first nonzero term is f^{ℓ*}_w(a′) − f^{ℓ*}_w(a_k) > 0.

The proof uses only these properties of the field: silence has value 0, a w-correct answer is negative, contradiction is positive, and there is an envelope. So it applies verbatim to the reweighted fields q·u¹ of §5. **Verdict: correct** (with the fundamental-domain remark of §1.3).

### 1.6 Proposition 5.2 (the staircase)

**CHECKED exactly (`ref53_staircase.py`).** The six sets are closed intervals with endpoints in {0, 3/8, 1/2, 3/2, 13/8, 2}. So checking the endpoints, two points in each gap, and all ordered pairs of these is a **complete** check, not a grid sample. It confirms:
- both defence covers;
- F₁ ∩ F₃ = ∅ and G₁ ∩ G₂ = ∅;
- no single-world tie;
- both families of (TC) clauses;
- the endpoint values.

So the proposition is correct as stated: those clauses are jointly satisfiable by closed tie-free sets.

**Two limits.**
1. **(audit confirmed) This is not a relation.** Only the 2 × 3 literals on the two-cell records of A (and, by (IB), of B and D) are assigned, along one path. Not checked:
   - (TC) triangles leaving the path;
   - other (IB) copies;
   - the other selected models' obligations on these records;
   - and above all the fixed-rival sections in the source.

   It is "a consistent one-parameter set of selected comparisons".
2. **(new) The parameter is the rival.** F_w = {s : A ⪯_w X_s} has the source fixed and the rival X_s moving. Its closedness is therefore closedness along a changing-rival mass path, the PP52 Thm 4.1 hypothesis, which M5 says is not an axiom. It says nothing about (S), which fixes the rival and moves the source. PP56 itself states Prop 5.2 only for its class (iii), so PP56 is internally consistent. But three later uses read it as a statement about (S)-sections (§3.4), and those readings do not follow.

---

## 2. PP57 §4–5

### 2.1 (L0⁺)

(L0⁺) says the strict part of one additive, strictly guiding, integrable field is accepted out of selected models. It is well defined. It holds for Λ and for every tie-break of Λ's level 0. It also holds, with ℓ = q·u¹, for the reweighted relations of §5.

It is a hypothesis about how a relation is built, not an axiom. **Note:** it is the *opposite* inclusion to "endorsement" (acceptance ⇒ Φ ≥ 0), which is what the M0 and FF2 results assume. This matters for §7.

### 2.2 Lemma 4.1 (pure likelihood shifts)

Put b = a∘(1 + te_w). Then Σ_i b_i m_{v,i} g_i = Σ_i a_i m_{v,i} g_i + t a_w m_{v,w} g_w, up to normalisation. Take g_w > 0, so that "+" is w-correct.
- If C_a says +, then C_b says +.
- If C_a says S, then C_b says S or +.
- If C_a says −, which is w-wrong, then C_b says −, S or +.

Every change is a w-improvement, and the case g_w < 0 is symmetric. The change set is a non-null wedge, because b∘m_v is not parallel to a∘m_v when a is interior.

**The proof's wording "C_b answers wherever C_a does" is false** in the case where C_a answers − and C_b falls silent. The conclusion is unaffected.

**CHECKED (`ref53_posterior.py` (C), my own code).** Over random interior a, worlds and t ∈ (0, 1/10]:
- 0 w-worsenings;
- 223 strict w-improvements;
- 116 points where C_a answers and C_b is silent.

`shift57.py` re-run: identical output, ALL PASS. **Verdict: correct with repair (wording).**

### 2.3 Theorem Q

**(i).** The shifts b_k stay in N_u, because a is interior. Φ_w(C_{b_k} → C_a) > 0 by Lemma 4.1 and strict guiding, and additivity gives Φ_w(C_{b_k} → X) > 0. (L0⁺) applies at each selected b_k, with the same rival throughout, so this is a legitimate M6 sequence. A closed section then gives C_a ⪯_w X. Correct.

**(ii).**
- Φ_w(C_a → C_a[F ↦ C_b]) = 0 at every w, so (i) accepts at every world.
- Exact (IB) gives rec(C_a → X) = (F : C_a → C_b) = rec(Y → C_b), with Y = C_b[F ↦ C_a].
- Y is incoherent. If Y were conic, F = {Y ≠ C_b} would be a.e. a cone, since both models are conic.
- So Y ⪯_w C_b at every world, which violates direct (C) for C_b as the brief encodes it.

The audit's remark ("an incoming weak domination does not alone violate (C)") is about the general form of (C). What makes (ii) a violation is the **protection context**: C_b is selected. With that, (ii) is correct. Neither (TC) nor ties are used. **Verdict: correct.**

### 2.4 PP57 Corollary 4.3

The level-0 increments of h → S are (−2, 1, 1)|g| on Ep and (2, −1, −1)|g| on Em.
- **CHECKED** independently (`ref53_posterior.py` (D)), at exact points of both cells.
- Radial slabs of equal ∫|g| exist (μ is atomless) and are non-conic.
- The corollary needs u and B both interior to N_u, with sections closed at the index used.

**Verdict: correct.**

### 2.5 Corollary 4.4 and its OPEN item

**First bullet.** Under the sandwich, acceptance out of a member implies Φ_w ≥ 0. So the range of (Φ_w(C_a → X))_w over rivals misses the open negative orthant. That range is convex by Lyapunov. Separation and localisation make C_a weakly λ-Bayes. This is FF2 Step 1, which is local. Correct.

**Conditional part.** Granting strict (K2) for the effective weights, PP57 Prop 2.2 steps 1–4 give exactly opposite price vectors on Ep and Em. Hence there is a null non-conic F, and Theorem Q applies. Correct.

**Lexicographic relations are covered.** Every lexicographic relation whose first level is additive is sandwiched by that first level. So Cor 4.4 covers it too.

**The OPEN item is genuine.** In the weak form of (K2) (REFEREE_round52 Lemma R1) the all-tied ratio vector is admissible, so z^A = z^B, say, cannot be excluded. Then:
- A and B are weakly Bayes for one λ, so their increment field d = φ(B) − φ(A) lies in the plane λ^⊥ a.e. on {A ≠ B}.
- Theorem Q(ii) needs a non-null, non-conic F ⊆ {A ≠ B} with ∫_F d = 0 ∈ R³.

By Lyapunov applied to (d, 1), a non-null F with ∫_F d = 0 exists iff some q ≥ 0, q ≠ 0, has ∫ q d = 0. (Non-conicity of F then needs a further argument; in the non-degenerate case it is free, because the increments are scalar multiples of one ν and radial slabs work.) Such a q **fails** to exist exactly when there is a θ ∈ λ^⊥ with θ·d ≥ 0 a.e. and with d a.e. on a single open ray on {θ·d = 0}. That is a lexicographic Gordan alternative in the plane.

On Ep and Em, d lies in opposite open sectors of λ^⊥, but the directions of d within each sector depend on the field. So the alternative can go either way for a general field. I could not settle it. **Status: OPEN, correctly labelled.**

### 2.6 Proposition 4.5

The records (F : h → S) and (F : S → h) are mutual inverses. By (IB), [B ⪯_w B[F ↦ h]] = [A[F ↦ S] ⪯_w A]. In a tie-free linear order exactly one of these is refused at each w. Theorem Q(i)'s sequence accepts at every shift on both sides.

So the refused side's section contains points converging to the source but not the source. It is **not closed**. Calling it "open" is a misnomer. **Verdict: correct with repair (wording).**

### 2.7 Lemma 5.1

The complement of a closed section is open in N_u. So if C_a ⋠_w X, then C_b ⋠_w X on a neighbourhood of a, whose size depends on (a, X, w). **The audit is confirmed:**
- this is local openness only;
- it says nothing for larger t, so there is no monotonicity along a ray;
- nothing in it is specific to w-improving directions: any direction works.

The §5 "dilemma" text uses it only in the local form, so its use there is fine.

---

## 3. PP55

### 3.1 Prop F (with F′, F″ and Prop B)

I re-checked the six steps.
- On a cell, the sign pattern of g is constant, so ranks are cell-constant and injective. The lexicographic rank order is therefore a strict linear order plus reflexivity.
- (IB), strict (G), (TC) and no ties follow.
- **Protection.** At the deciding piece, a coherent model is never contradictory and is correct where g is unanimous. On mixed cells h, S and −h are pairwise incomparable across worlds. So some world, which lies in the support because indices are interior, has C_a ≺_w X.

**F′.** Deleting acceptances keeps (TC) (a subset of a linear order) and DEF (own records). UND remains vacuous, because its antecedent was already false.

**F″.** Refine, then restrict. That is correct.

**Prop B.** Correct, and **re-run (CHECKED)**: `sections55.py 0` gives 0 violations under all four orders, with 37,396 two-witness literals. The output matches the archive except for timings.

**Verdict: correct**, as a statement about finite instances. PP55 §3 itself says that this makes finite SAT uninformative about the continuum.

### 3.2 Theorem 5.1′

I checked the case analysis.
- **S₃ < z^A₃:** contradiction even with every tie.
- **S₃ ≥ z^A₃:** a chain of equalities, so S = z^A. Then ℓ(z^B) = ℓ(z^D) = ℓ(S), because a strict interior convex combination of unequal values is below the maximum.
- **Case (i)** is killed by the strict pair inequalities supplied by (H*). Case (ii) is indifference a.e. on U ∪ L.
- **Step 4** needs one scalar cancellation ∫_{E_U} κ = ∫_{E_L} κ′, and atomlessness supplies it.
- **Step 5 (R0)** is a valid chain in any zero-accepting gate union: (IB), then B's undominatedness, then (IB), then T's direct (C).

**Re-runs (CHECKED).** `v3ties55` is identical. `v3core55` is identical up to the print order of one set.

**Repairs of scope.**
- **(H*) is essential.** Without it, case (i) (z^A = z^B or z^A = z^D) is not excluded. That is exactly the degenerate case of §2.5.
- **The (R) branch (step 6) is local to the triple.** In a 2-D gate union another gated member that answers h on E could realise T's record. PP57 Prop 2.2 states this caveat; PP55 does not.

**Verdict: correct with scope repair.**

### 3.3 Proposition SR

**(a) Correct.** A subsequence converges a.e. Advice is discrete, so the pointwise weak rank inequality passes to the limit.

**(b) The stated justification is wrong. The audit is confirmed.** "Strict pure improvement at w for all large k ⇒ strict pure improvement at the limit" fails. The audit's example (C_{b_k} pure w-worsenings of C_a, with X = C_a) is a valid counterexample.

**But the conclusion of (b) is true, by a two-case repair (PROVED).** Let W∞ be the set of worlds at which X is *not* a strict pure improvement of C_{a_k} for infinitely many k.
- **Case X = C_a a.e.** The clause ⋁_{w∈W∞} [C_a ⪯_w X] holds by reflexivity. W∞ ≠ ∅, by DEF and pigeonhole.
- **Case X ≠ C_a on a non-null N₀.** For w ∉ W∞, the weak limit gives rank_w X ≤ rank_w C_a a.e. Ranks are injective in the advice, so the inequality is strict on N₀. So X is a strict pure w-improvement of C_a, and strict (G) refuses w at a. Hence DEF at a implies ⋁_{w∈W∞} [C_a ⪯_w X].

So the pigeonhole clause is indeed redundant. The audit's counterexample is precisely the reflexive case.

**(c) Does not follow. The audit is confirmed.** Here is a concrete coupling that Prop B cannot see.
- Suppose X is a strict pure 1-improvement of C_a, but is mixed against each C_{a_k} at world 1. Then a closed section at world 1 forces "C_{a_k} ⪯₁ X for only finitely many k".
- With DEF, this forces [C_{a_k} ⪯₂ X] ∨ [C_{a_k} ⪯₃ X] for **all but finitely many** k.
- Yet no single literal is forced (Prop B). This is a cofinite restriction on the approximants, and it can propagate through (TC) and protection clauses at each a_k.

Three further points:
1. A section clause has infinitely many premises. Propositional compactness does not apply to it.
2. M6 allows the acceptances along the sequence to be proved inside a case split. Prop B rules out only unconditional forcing.
3. A finite instance contains only finitely many indices, so it cannot even represent an actual sequence.

Nothing here shows that sections *do* create UNSAT. SR(c) is simply unproved.

### 3.4 What depended on SR(c), and on reading Prop 5.2 as a statement about (S)

| Place | Claim | Status after this report |
|---|---|---|
| PP55 §0 table, row "V1 + section clauses … SAT (Prop SR)" | finite section shadows are redundant | **withdraw**; true only for the guidance and pigeonhole shadows ((a), repaired (b)) |
| PP55 §0 item 5; §7 "What a section-based kink would need" | an axiom-level kink must be non-finitary, over a two-parameter rival family | **unsupported** (rests on SR(c) and on Prop 5.2 read as (S)) |
| DESIGN_MEMO §8.22, PP55 entry | "finite section clauses cannot create UNSAT … needs NON-FINITARY section arguments over 2-parameter rival families" | **unsupported**; reword as "the guidance and pigeonhole section shadows are redundant" |
| DESIGN_MEMO §8.22, Open (i) | "…for 2-parameter balanced swaps" | the "2-parameter" qualifier is **unsupported**. Also, the fixed-rival, fixed-world forcing version is **refuted** by the robust refusal lemma (§5). |
| PP57 §5 aim (a) and "Most important next step" | "Prop 5.2 of PP56 shows one parameter is not enough" | **non sequitur** (5.2 is changing-rival closedness). The forcing question in aim (a) is refuted by §5 in its fixed-rival form. |
| PP56 §0 item 5, §5.2 Reading, §6 item 2, Conj 5.3 | two parameters are needed for a (iii)-level kink (mass-path closedness) | **consistent as stated** (class iii), but only for the listed clause family on one path |

---

## 4. Theorem K′ (PP60 = REFEREE_round52 §4.4; memo §8.22)

**Statement.** ε = 3/10; the gate union under (R0); weakly own-Bayes gates; (TC) with single-world ties allowed. G_s is the set of gated indices that are a.e.-uniquely own-Bayes. Then G_s ∩ U₀ is outer-null.

I checked the chain.
1. Density points exist for outer measure.
2. Because a₀ is a density point of G_s, the two fixed-fraction boxes of Prop 6.2 meet G_s. So b, d can be chosen gated, and Prop 6.2 makes (a₀, b, d) a kink triple with the same cells.
3. (TC) ⇒ the closed pair sandwich. REFEREE_round50 Thm 3.1(c) proves this, and its closing reverse is a pure improvement, so it is tie-robust.
4. R1(ii) needs reverses refused, not merely "not tied". Its separation produces three links with **strictly positive** gate values. Lemma R2 then refuses every reverse, by guidance and by every realiser, so allowing ties does not rescue the triangle.
5. (K3) gives positive constants.
6. Thm 5.1 needs strictness only for the odd model, on one cell (REFEREE_round52 §4.3(a)); a₀ ∈ G_s supplies it.

**Re-run (CHECKED).** `PP60_py/kink_ref.py` reproduces the archived output, ALL PASS.

**Verdict: correct.**

**Scope.** K′ is a theorem about realiser-gated unions with own-Bayes additive gates. It does not touch M2 relations. Λ already has 2,803 of 6,048 acceptances with no realiser, which is CHECKED by the re-run of `kink56`.

**The memo's gloss is overstated.** "Only exact indifference escapes, and PP55 Thm 5.1′ closes that too" does not follow from 5.1′:
- 5.1′ assumes (H*), that B and D are strictly own-Bayes off U ∪ L. But K′'s escape set consists of members that are themselves indifferent, and those may fail (H*) as partners in other triples.
- The (R) branch of 5.1′ is local to the triple (§3.2).

Correct wording: "inside gate unions, the members that escape K′ are Bayes-indifferent on both certificate cells. Thm 5.1′ excludes the all-indifferent triple under (H*) (for (R), within the triple)."

---

## 5. The robust refusal lemma (AUDIT_robust_refusals §1)

**Setting.** Fix N = C_a ∈ N_u, a measurable rival X, and a world w at which X is strictly better than N on a non-null set. Put d = u¹_w(X) − u¹_w(N), so d < 0 on a non-null set. Choose E ⊆ {d < 0} with ∫_E d < 0, and q = 1 + K·1_E with K > max(0, ∫d)/|∫_E d|. Use the field v = q·u¹ for **every** world.

**What survives (PROVED).** Each step of §1.3 goes through with u¹ replaced by v:

| Theorem L ingredient | Why it survives |
|---|---|
| strict guidance at every world | q(g) > 0 is a common positive scalar at each g |
| pointwise λ-Bayes of every member, λ = (1, 1, 1) | λ·(v(X) − v(N)) = q·λ·(u¹(X) − u¹(N)) ≥ 0; this needs q to be **common to all worlds** |
| integrability | 1 ≤ q ≤ 1 + K |
| (IB), (TC), reflexivity | the same additive lexicographic form |
| no ties | q·f ≠ 0 a.e. on {X ≠ Y}, and the π–λ step is unchanged |
| later levels | 1_B·v (or 1_B·u¹) keep the pointwise inequality. With 1_B·u¹, the whole-space equation follows from boxes (−n, n)³ and dominated convergence. |
| protection, defence, undominatedness, direct (C), (LA) | step 5 verbatim |

**Which hypotheses on q are used.** Only q > 0 a.e. and q·|g| integrable. "Bounded below by 1" is more than needed, but q may not vanish on a non-null set: no ties and strict (G) would then fail there. World-dependent q_w would break the Bayes step.

**The refusal (PROVED).**
- Δ⁰_w(N, X) = ∫ q d < 0, so N ⋠_w X, decided at level 0.
- b ↦ ∫ q[u¹_w(X) − u¹_w(C_b)] is continuous on N_u: C_b is continuous in measure (PP49 Lemma 1.1, SAFE geometry) and the envelope (1 + K)·5|g| is integrable.
- So C_b ⋠_w X on a relative neighbourhood of a in N_u, including all small pure shifts.

The rival is fixed throughout, as Brief 54 requires.

**No section claim.** Prop 5.1 applies to q·u¹ (§1.5), and so does Theorem Q (ii): take radial slabs with ∫_{F⁺} q|g| = ∫_{F⁻} q|g|. So the reweighted relation still fails sections, as the audit says.

**Verdict: correct.** It refutes the fixed-rival, fixed-world forcing statement, and only that (AUDIT_robust_refusals §2).

---

## 6. The alternative theorem

Let (Ω, μ) be a finite measure space (here Gaussian). Let d₁, …, d_m ∈ L¹(μ).

### 6.1 Finite family

**Theorem A (PROVED).** The following are equivalent:
- (a) there is q ∈ L^∞ with q ≥ δ > 0 a.e. and ∫ q d_k dμ < 0 for every k;
- (a′) there is q ∈ L^∞, q ≥ 0, with ∫ q d_k < 0 for every k;
- (b) there is no α ∈ R^m, α ≥ 0, α ≠ 0, with Σ_k α_k d_k ≥ 0 μ-a.e.

*Proof.*
- **(a) ⇒ (a′):** trivial.
- **(a′) ⇒ (b).** If such an α existed, 0 ≤ ∫ q Σ_k α_k d_k = Σ_k α_k ∫ q d_k < 0, since α ≥ 0, α ≠ 0 and every integral is negative.
- **(b) ⇒ (a′).**
  - Let K = {(∫ q d_k)_k : q ∈ L^∞, q ≥ 0} ⊆ R^m. K is a convex cone containing 0.
  - Suppose K misses the open negative orthant N₋. Two disjoint convex sets, one of them open, can be separated: there is α ≠ 0 and c with α·y < c ≤ α·v for all y ∈ N₋ and v ∈ K.
  - Since K is a cone containing 0, c ≤ 0 and α·v ≥ 0 on K.
  - If some α_j < 0, take y = −M e_j − η1: then α·y → +∞ as M → ∞, contradicting α·y < c. So α ≥ 0.
  - Now take q = 1_A with A = {Σ_k α_k d_k < 0}. Then ∫_A Σ α_k d_k ≥ 0, so μ(A) = 0, and Σ_k α_k d_k ≥ 0 a.e. This contradicts (b).
  - So some q₀ ≥ 0 bounded has ∫ q₀ d_k < 0 for all k.
- **(a′) ⇒ (a).** Put q = q₀ + η with 0 < η < min_k |∫ q₀ d_k| / (1 + ‖d_k‖₁). ∎

**Remarks.**
1. **The partition form is without loss of generality.** Approximate q₀ uniformly by a nonnegative simple function; the map q ↦ ∫ q d_k is L^∞-continuous. Then rescale. So the brief's q = 1 + Σ_ℓ t_ℓ 1_{E_ℓ} (t_ℓ ≥ 0) can always be achieved on *some* finite partition. Failure on a *given* partition is not a certificate. An α is.
2. **Finite-atom instances.** On finitely many atoms the theorem is Gordan's alternative. CHECKED (`ref53_alternative.py`): 400 random integer instances, each classified as q-feasible (171) or α-certified (229), with every witness verified exactly and none unresolved.

**The audit's swap example: the full world table (CHECKED).** Forward record "A refuses A[F ↦ S]" at world w, reverse record "B refuses B[F ↦ h]" at world v, with increments (−2, 1, 1) and (2, −1, −1):

| | v = 1 | v = 2 | v = 3 |
|---|---|---|---|
| w = 1 | α = (1,1) | q | q |
| w = 2 | q | α | α |
| w = 3 | q | α | α |

So the two refusals are jointly q-feasible exactly when the worlds straddle the split {1} | {2, 3}. Both refusals need the same sign of z = ∫_{E₊} q − ∫_{E₋} q, and that happens iff one world is 1 and the other is 2 or 3. This confirms and extends the audit's §3.

**Obstructions need not be pairwise (CHECKED).** d₁ = 1_{E₁} − 1_{E₂}, d₂ = 1_{E₂} − 1_{E₃}, d₃ = 1_{E₃} − 1_{E₁}: every pair is q-feasible, but the triple has α = (1, 1, 1). So the adaptive experiment must re-test the *whole* accumulated set, as the brief says.

### 6.2 Compact family

**Theorem A′ (PROVED). Hypotheses.**
- (H1) T is a compact metric space.
- (H2) t ↦ d_t is continuous from T into L¹(μ) (norm continuity).

Then the following are equivalent:
- (a) there is q ∈ L^∞ with q ≥ δ > 0 and sup_t ∫ q d_t < 0;
- (a′) there is q ∈ L^∞, q ≥ 0, with ∫ q d_t < 0 for every t;
- (b) there is no finite positive Borel measure ν ≠ 0 on T whose Bochner integral D_ν := ∫_T d_t ν(dt) ∈ L¹ satisfies D_ν ≥ 0 a.e.

*Proof.*
- **The map.** Q(q)(t) := ∫ q d_t is continuous in t, because |Q(q)(t) − Q(q)(s)| ≤ ‖q‖_∞ ‖d_t − d_s‖₁. So Q : L^∞ → C(T) is linear.
- **(a′) ⇒ (a).** Q(q) attains its maximum on compact T, so the maximum is negative. Add η < |max Q(q)| / (1 + sup_t ‖d_t‖₁); the supremum is finite by (H2).
- **(a′) ⇒ (b).** D_ν is well defined, because t ↦ d_t is continuous and bounded, hence Bochner integrable. Bochner integrals commute with the bounded functional ⟨q, ·⟩, so ⟨q, D_ν⟩ = ∫_T Q(q) dν < 0 if ν ≠ 0. That is incompatible with D_ν ≥ 0.
- **(b) ⇒ (a′).**
  - K = Q(L^∞_+) is a convex cone in C(T). N₋ = {f : max f < 0} is open and convex.
  - If they are disjoint, Hahn–Banach gives φ ∈ C(T)*, φ ≠ 0, with φ < c on N₋ and φ ≥ c on K. Since both sets are cones, c = 0.
  - For f ≥ 0, −f − η ∈ N₋ gives φ(f) > −ηφ(1). So φ ≥ 0, and by Riesz φ = ν, a positive Radon measure.
  - Then ⟨q, D_ν⟩ = ∫_T Q(q) dν ≥ 0 for all q ≥ 0 bounded, so D_ν ≥ 0 a.e. ∎

**In the application.** d_t = u_{i}(X_t) − u_{i}(C_{a_t}) satisfies (H2) when:
- t ↦ C_{a_t} and t ↦ X_t are continuous in measure (the envelope 10|g| gives L¹-continuity by dominated convergence);
- the refusing world i is constant on T. If it is not, split T into finitely many closed pieces on which it is.

For swap rivals X_t = C_{a_t}[F_t ↦ C_{b_t}], one also needs μ(F_t △ F_s) → 0. With T compact and the bound uniform, the refusal neighbourhoods can be made uniform as well, provided the map (t, b) ↦ ∫ q d_{t,b} is jointly continuous, which it is under the same hypotheses.

### 6.3 Within the reweighted construction the test is exact for *open* refusals

**Proposition A″ (PROVED).** Take a relation Λ_q (any q > 0 with q|g| integrable, common to all worlds, any box tie-breaks). Let a be interior in N_u. Then C_a ⋠_w X with a refusal set that is a neighbourhood of a **iff** ∫ q d < 0, where d = u¹_w(X) − u¹_w(C_a).

*Proof.*
- **(⇐)** is §5.
- **(⇒)**
  - If ∫ q d > 0, the relation accepts at a.
  - If ∫ q d = 0, the shifts b_t = a∘(1 + te_w) give ∫ q[u¹_w(X) − u¹_w(C_{b_t})] = ∫ q[u¹_w(C_a) − u¹_w(C_{b_t})] > 0 (Lemma 4.1). So they accept, and the refusal set is not a neighbourhood. ∎

So an α-certificate is an **exact** obstruction for the entire reweighted family: every q and every tie-break. It is not just a failure of one search. It says nothing about general relations. That matches the brief's (W) / (W¬R) classification.

### 6.4 Finite sampling cannot replace the measure certificate

Take Ω the circle with Lebesgue measure, an irrational θ ∈ (0, 1), and d_t(x) = 1_{[t, t+θ)}(x) − θ, for t ∈ T = the circle. (H1) and (H2) hold.
- **ν = Lebesgue is a certificate:** D_ν ≡ 0. So no q gives sup_t ∫ q d_t < 0.
- **No finite α ≥ 0, α ≠ 0 is a certificate:**
  - Each d_t has mean 0, so Σ_j α_j d_{t_j} ≥ 0 would force Σ_j α_j d_{t_j} = 0.
  - Its k-th Fourier coefficient is d̂(k) Σ_j α_j e^{−2πikt_j}, with d̂(k) = (1 − e^{−2πikθ})/(2πik) ≠ 0 for every k ≠ 0.
  - So the atomic measure Σ_j α_j δ_{t_j} would have every nonconstant Fourier coefficient zero, which is impossible for a finitely supported measure.

So every finite subfamily is q-feasible, by Theorem A, while the compact family is not. This proves the audit's warning that "finite sampling alone does not establish that bound".

**Usable finite certificate.** Suppose {t_j} is an L¹-δ-net of {d_t} and max_j ∫ q d_{t_j} < −‖q‖_∞ δ. Then sup_t ∫ q d_t < 0.

**A finite-dimensional case.** If span{d_t} is finite-dimensional, for instance on a fixed finite partition, Carathéodory reduces any ν to at most dim + 1 atoms.

---

## 7. Ledger applicability to a LOCAL module on N_u (four-advice domain)

"Local" means the M1–M7 module: closed 2-D N_u, interior indices, arbitrary M2 relations, sections by M6.

| "Killed" architecture | Source and its hypotheses | Constrains a local module on N_u? |
|---|---|---|
| **Single fields, additive or general** | REFEREE_PP32 Thm A, Cor A′: an edge selection on [e₁, e₂] (Fam, WS). Contamination Triangle Q4.2: a full selection on Δ with T1 Bayes at an interior p*, the facet analysis of M3.9, (NC) at every world. | **Only full covers / edge families.** The four-advice domain is an (LF) decomposable domain, so the *domain* hypothesis of Q4.2 holds, but the *selection* hypothesis is global. **Local substitute (PROVED from PP56 §2.3, PP57 Prop 2.2, Cor 4.4).** A single additive field relation that defends A, B and D is killed on N_u **without sections** once a null non-conic member swap exists: under (R0) by an all-world tie with an incoherent model; under (R) by loss of defence. Such a swap exists for u¹, and for every defending field under strict (K2). In the degenerate case it is OPEN (§2.5). No local result covers non-additive "general" single fields. |
| **M0 "adds up" (incl. intersections)** | Thm M0closed on M_U (a *different* two-action domain); Q4.1–Q4.2 and the intersection proof on (LF) domains; all are FULL covers (EXPLORATION_MAP's own caution). | **Only full covers.** Locally they are **false without sections**: Λ is endorsed at every world, on every record, by the single integrable strictly guiding field u¹ (acceptance ⇒ Δ⁰ ≥ 0), and satisfies every non-section axiom on N_u (Thm L). FF2 Thm 4.1 needs the whole-Δ covering step (Step 3: Browder plus Brouwer). Only its Step 1 (local competitiveness ⇒ weak Bayes) localises. With sections: an endorsement-only (M0) relation is **not** covered by Theorem Q, which needs the opposite inclusion (L0⁺). An intersection of additive rankings also fails (L0⁺) for any single field. **No local exclusion of M0 or of intersections is established.** |
| **PP38 bounded kernel ℓ^T** | PP38 Thm 3.1(ii): competitiveness against bounded rivals ⇔ ℓ^T-Bayes (pointwise, so local). The coherence lemma: the coherent ℓ^T-Bayes models are T, edge segments B_ij(t) and vertices. PP42 Thm 2.1: a single witness field registers only its own Bayes models. | **Local, but specific to ℓ^T.** A module that decides bounded records out of members by ℓ^T alone can register only T among the posterior models near u. It does not constrain other kernels: every member of N_u is u¹-Bayes, so PP42 Thm 2.1 is harmless for u¹. Kernels with ties at 0 then die on null member swaps, as in the first row. |
| **Realiser-gated unions (PP50 Thm K, PP60 Thm K′)** | Gt + Ad; K: strict CG2; K′: a.e.-unique own-Bayes members, (R0), ties allowed | **Local (U₀ near u, posterior family, four-advice domain), but architecture-conditional.** They bind only gate-union modules (acceptance = guidance ∪ own-Bayes additive gates of old-side realisers). They do not bind M2 relations (Λ, Prop F). Inside gates the residual escape is Bayes-indifferent members (§4). |
| **Lexicographic levels (Theorem Q)** | (L0⁺) for one additive strictly guiding field; a null non-conic member swap for that field; closed sections at one interior member | **Local on N_u; conditional on (L0⁺) and on the swap.** Every lexicographic relation with an additive first level is sandwiched, so Cor 4.4 supplies the swap under strict (K2) (OPEN in the degenerate case). For Λ and every q·u¹ reweighting the swap is explicit, so those are killed outright. It does not constrain relations that refuse some strict first-level acceptances out of shifted members, and in particular not record-based allocations. |
| L4 / R21 (blind sets), EXPLORATION_MAP 2a.5 | Hahn–Banach fixed point over a FULL cover | **Only full covers.** As the brief says, a structural hint, not a constraint on a module. |

**Bottom line for the allocation round.** The only established local constraints on a record-based allocation are:
- the axiom-level clauses (PP59 SAFE entries, satisfied by Λ, hence never contradictory without sections);
- Theorem Q, which applies only to allocations that contain the strict part of one additive field out of members;
- the alternative theorem, which applies only to allocations certified by one common q.

Everything else is either full-cover or gate-specific.

---

## 8. Scripts (`r9/REFEREE53_py/`; run `python3 -I -B <script> > <script>.out` inside the folder)

| Script | Content | Label |
|---|---|---|
| `ref53_posterior.py` | own posterior advice. (A) the (2V) region and a counterexample outside it; (B) u¹ on a 41-member family: strict guidance, λ-Bayes, balance; (C) Lemma 4.1 monotonicity, plus the wording counterexamples; (D) Ep/Em increments | CHECKED, ALL PASS |
| `ref53_alternative.py` | swap example: full world table; cyclic triple (pairwise feasible, jointly α = (1,1,1)); 400 random instances classified with exact witnesses | CHECKED (LP proposes, Fractions verify), ALL PASS |
| `ref53_staircase.py` | Prop 5.2, a complete exact check on the interval partition | CHECKED, ALL PASS |

**Re-runs (outputs identical to the archives, CHECKED):**
- PP56: `cells56`, `lex56`, `instance56`, `kink56`;
- PP57: `shift57`, `geom57`;
- PP55: `v3ties55`, `pieces55`, `v3core55` (one set printed in a different order), `sections55 0` (timings differ);
- PP60: `kink_ref`.

I did not re-run the SAT runs `run55_L*` or PP57's closure searches. No verdict above depends on them.

**Most important next step.** By §6.3 the α-test is exact for the whole reweighted family. So the round-54 adaptive experiment should record, for each accumulated set of prescribed refusals, either one q (W fails to bite) or one α-certificate. For each α-certificate it should then ask the purely relational question: do defence, protection, (IB) copies and (TC) still admit the prescribed refusals with open fixed-rival refusal sets? The straddling table of §6.1 shows which world assignments on a single balanced swap are q-certifiable. The cyclic-triple example shows that the joint test must be re-run on the whole accumulated set, not pairwise.
