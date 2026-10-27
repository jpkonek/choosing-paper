# B3 referee report: complete worlds, almost-representability and order continuity on edges

Referee report on `B3_notes.md` (round 14), with its scripts in `b3py/`.

It is checked against:
- writeup §§2–3 and §8.5: Theorem S21, Cor S21, Thm Q36, Cor Q37, (Nest_e), Remark straighten, Prop plateau, Thm S22, the Level Lemma, Cor continuum and Prop R7.1;
- `P4B_referee.md` §8 (Lemma T and Theorem E3 via Savage);
- `S2_notes.md` and `S2_referee.md`;
- the source *Independent Rankings Without Additive Structure* (IRWAS).

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS / HEURISTIC. Referee scripts are in `b3ref_py/`, run with `python3 -I`.

## 0. Verdicts

| Item | Claim | Verdict |
|---|---|---|
| B3.1 | For a complete world, π is a leading charge on M ⟺ π is a nonzero almost-agreeing charge | **CORRECT** |
| B3.2 | AR on M ⇒ strictly positive and adds up, with no (Nest_e); the complete clause of Q37 generalises | **CORRECT**, with a **GAP (wording)** in §0 and §5 |
| B3.3 | Order continuity (E1), (E2) on edges from strict (G), (IB), (S) | **CORRECT** |
| B3.4 | Ultrafilter edge example: π legitimate; (K), closed sections, crossing, non-fineness | **CORRECT**; (d) can be upgraded; the scope remark is **WRONG as worded** |
| B3.4 | Does "leading charge" in S21 allow finitely additive charges? | **Yes** (§4.4) |
| B3.5 | Cancellative top levels with dense null sets are trivial | **CORRECT**. It also holds for incomplete worlds (§6), so the "incomplete alternative" remark is **WRONG** |
| B3.6 | Signature/IRWAS top levels and pure-charge first levels are excluded | **CORRECT**, with a small **GAP (description of IRWAS)** |
| B3.7 | Exchangeable signatures are additive | **CORRECT** within its hypotheses. The narrative built on it ("escaping B3.5 forces additivity") is **HEURISTIC** and should be labelled so |
| B3.C | Every complete world is AR | Plausible and **OPEN**. "Equivalently" is **WRONG** (one direction only), and "complete worlds are excluded from covers outright" is **WRONG as worded**. For n = 2 the conjecture contains a clean order-theoretic special case, B3.C′ (§7) |
| Scripts | — | Rerun with `python3 -I`; output byte-identical. Two checks are tautological (§8) |

Net assessment:
- The mathematics of B3 is sound.
- Every theorem-level claim survives.
- The repairs are to scope sentences and labels, not to proofs.

The referee adds three items:
- **Prop R1.** The B3.4 world is realised in a two-world ranking that fails only (C).
- **Remark R2.** B3.5–B3.7 extend to *leading top levels* of incomplete worlds.
- **Prop R3.** For n = 2, B3.C contains an exact order-theoretic special case, B3.C′.

## 1. B3.1 (leading ⟺ almost-agreeing, for complete worlds): CORRECT

Re-derived:
- **(⇒)** This is the second leading property, together with finite additivity: π(B) − π(A) = π(B∖A) − π(A∖B), and π is bounded.
- **(⇐)** Suppose π(B∖A) > π(A∖B). Then π(B) > π(A).
  - Almost agreement gives B ≤_i A ⇒ π(B) ≤ π(A), so B ≤_i A fails.
  - Totality then gives A ≤_i B.

Only totality on subsets of M is used.

**Terminology (fix).** The writeup's §2.6 already uses "complete" for a (CP-a) world whose credal set 𝓜_i is a singleton. B3, like Thm E3 and Q36(c), means "≤_i is total on the subsets of M". Say "total" (or "complete (total)") at the first use in B3 §1, so that the two meanings are not conflated.

## 2. B3.2: CORRECT; wording GAP

**The corollary.** AR gives a nonzero almost-agreeing π. B3.1 makes π a leading charge. S21 then gives strict positivity, endorsement and SP^reg. None of this uses (Nest_e), (C), (LA) beyond (S), or a third world. Correct, at the status of S21 (two readers).

**Consequence for Q37.**
- B3.1 shows that "complete and AR on M" is a *special case* of "leading charge nonzero on M".
- So the complete clause of Q37, in either form, adds nothing beyond the leading-charge clause. It survives only as one sufficient route to AR, namely Q36(c): nestedness ⇒ fineness ⇒ Savage.
- Recommend that the writeup say this in one sentence after Q37.

**GAP (wording), §0 item 1 (line 18) and §5 (line 193).** "A complete world in a cover must be non-AR on M" is false as written.
- A cover may contain complete worlds that add up, provided some *other* world does not add up.
- What B3.2 proves (and what B3 itself states correctly in the Corollary) is: *a complete world of a cover of T₁ that does not add up is non-AR on M*.
- **Fix:** insert "that does not add up" in both places.

**"Some edge at e_i must cross" (§2).** This is correct, as the contrapositive of Q36(c), which needs (Nest_e) on *every* edge at e_i. It is CHECKED (Savage import).

## 3. B3.3 (order continuity on edges): CORRECT

Re-derived:
- **(E1).** For p ∈ e_ij, C_p ⪯_i X_A iff c_p ≤_i A: both error sets lie in R_ij (Lemma Q34), and the normal form applies. S_i(X_A) is closed in Δ, so its trace on e_ij is relatively closed, and its complement is a neighbourhood of p*.
- **(E2).** E_j X_A = R_ij∖A ⊊ R_ij∖c_{p*} with non-null difference, so X_A ≺_j C_{p*} by strict (G) at j. Hence p* ∉ S_j(X_A), and a neighbourhood N of p* avoids S_j(X_A).
  - For q ∈ N with supp q = {i, j}, competitiveness gives C_q ⪯_i X_A.
  - q = e_j is impossible, because C_{e_j} ⪯_j X_A.
  - q = e_i is trivial, since c_{e_i} = ∅.

Inputs:
- (E1) uses only closedness of S_i.
- (E2) uses closedness of S_j, strict (G) at j, and competitiveness at edge indices.
- (IB) enters only through the normal form.

"Squeezed" in the gloss means squeezed in ≤_i, not set-theoretically: c_{p*}∖D <_i c_q ≤_i c_{p*} ∪ D′. Say so.

## 4. B3.4 (the ultrafilter edge example)

### 4.1 Is π = λ + c·δ_𝒰 a legitimate charge? Yes (PROVED)

- **The ultrafilter exists.** The classes [(1, 1+h)], h > 0, form a filter base in the measure algebra of [0, 2): finite intersections are again such intervals, all non-null. By the ultrafilter lemma (BPI, a weak form of choice; say so, as IRWAS does) the base extends to an ultrafilter 𝒰 of the measure algebra.
- **δ_𝒰 is a charge.** δ_𝒰 is {0,1}-valued and finitely additive:
  - for disjoint A and B, A ∪ B ∈ 𝒰 iff A ∈ 𝒰 or B ∈ 𝒰 (𝒰 is prime);
  - A and B are not both in 𝒰, since A ∧ B = 0.
- **δ_𝒰 vanishes on null sets,** because null sets are the zero of the algebra.
- **δ_𝒰 is not countably additive:** ⋀_h (1, 1+h) = 0.
- **π is legitimate.** π = λ + cδ_𝒰 is a bounded, finitely additive, strictly positive charge vanishing on null sets. Its countably additive part is λ, and its pure part is cδ_𝒰.

### 4.2 (a)–(c): CORRECT

- (a) holds because π is a strictly positive charge.
- (b): m is continuous at p = 1/3.
  - From the left, m = 3pc → c, and [0, c) ∉ 𝒰 because it is disjoint from (1, 1+h).
  - From the right, m = c + 1.5(p − 1/3) → c.
  - On (1/3, 1], every c_p ∈ 𝒰.
  - World j's section is {p : π(R∖c_p) ≤ π(R∖A)} = {p : m(p) ≥ π(A)}. Both sections are closed.
- (c): c_{1/3} = [0, c) and c_{1/2} = (1, 1.25) cross.

**Note.** (K) holds here *trivially*: m(p) ≤ π(A) or m(p) ≥ π(A) always. The two edge worlds are mirror images, both ranking by one complete order (§7, Lemma R3.0). So (K) carries no information in this example, and the script's (K) test is a tautology (§8).

### 4.3 (d): CORRECT; upgrade to PROVED without Savage

- **Non-fineness** is correct: a finite partition has exactly one piece in 𝒰, of value ≥ c > π(Z) = λ(Z).
- **Better proof of "no nested edge family with (K) and closed sections exists".** B3 derives this from Remark straighten and Q35(5), which carries the CHECKED (Savage) status. There is a two-line proof:
  - Let (c_b) be any chain from ∅ to R. Membership in 𝒰 is monotone along it, and λ(c_b) is nondecreasing.
  - Put b* := inf{b : c_b ∈ 𝒰}. Then b* > 0, since ∅ ∉ 𝒰 and R ∈ 𝒰. Hence m(b) = π(c_b) is nondecreasing with a jump ≥ c at b*.
  - The values π(A) fill [0, 2 + c]. So for any level a inside the jump, {m ≤ a} or {m ≥ a} is not closed.
  - This is PROVED, uses no Savage import, and does not use (K).
- **Fix:** replace the sentence in (d) by this argument.

### 4.4 Does "leading charge" in S21 allow finitely additive charges? Yes

- The writeup defines a leading charge as "a charge π ≥ 0 on U, bounded and vanishing on null sets".
- S2_notes S2.1 says "(finitely additive allowed)".
- S21's status line lists "countable additivity of π" under *not used*.

The proof uses finite additivity and monotonicity throughout:
- the small-set step (split E into k pieces);
- semicontinuity of m;
- the generic level;
- the π-null-set contradiction.

The final density statement uses the Yosida–Hewitt carrier lemma, which holds for bounded pure charges ≪ μ.

For B3.4's π, S21's conclusions hold, with ρ ≡ 1, so the example is consistent with S21 (and with B3.4(e)).

### 4.5 Scope remark (line 118): WRONG as worded

> "In a full two-world ranking this world is impossible: Theorem S2.2 forces nesting …"

S2.2 assumes "every axiom", including **(C)**; its proof uses Lemma PL with (C). Without (C) the B3.4 world *is* realised in a two-world ranking.

**Proposition R1 (PROVED; NUMERICS `b3ref_py/two_world_ultra.py`).** Setting: n = 2 on M_U, K′ = [α′, β′] ⊆ (0, 1).
- Let 𝒰 be an ultrafilter of the measure algebra of M⁺ containing every thin sector just outside S⁺(α₀), for some 0 < α₀ < α′. Here S⁺(α) is the world-1 error set of D_{[α,β]} on M⁺, and it grows as α decreases.
- Let π := μ + cδ_𝒰, with 0 < c small.
- Rank both worlds by lex(μ(N₊ part), π(M part)) of their error sets.
- Select coherent C_p = D_{[α(p),β(p)]}, with α ≤ α′ and β ≥ β′, along this path:
  - raise β from β′ to β_A, with α = 0;
  - raise α from 0 towards α₀;
  - at the index p_J where α reaches α₀, jump β down to β_B < β_A, so that S⁻ gains μ-mass exactly c;
  - then move (α, β) to (α′, 1).

Then:
- strict (G), (IB) and (LA) hold;
- (S) holds, with closed sections for **every** model, and every C_p is coherent and undominated;
- world 1 is complete (total) and not fine on M;
- the selection crosses (C_{.25} and C_{.5} differ by non-null sets on both sides);
- only (C) fails.

*Proof.*
- **The sum identity.** On M exactly one world errs, so for regular X, π(E₁X) + π(E₂X) = π(M) (as in R7.1).
- **Undominatedness and competitiveness.** Every regular model is undominated and competitive on {1, 2}. Non-regular models are strictly worse at both worlds through the lex-first N₊ coordinate. The vertex models are P₂ = D_{[0,β′]} and P₁ = D_{[α′,1]}.
- **Closed sections.**
  - m(p) = π(E₁C_p) is continuous: the loss of the germ at α₀ is compensated by the μ-jump of S⁻.
  - Hence {m ≤ v} and {m ≥ v} are closed. These are the sections for regular X; for non-regular X the section is Δ.
- **Non-fineness and crossing** are as in B3.4.
- **(C) fails** at any incoherent regular X with π(E₁X) = m(p). ∎

NUMERICS (Gaussian μ, angular sectors, K′ = [0.35, 0.6], c = 0.2, α₀ = 0.2):
- maximum step of m is 4.3·10⁻⁵ on a grid of 40 001 points, with m(0) = π(M) and m(1) = 0;
- the selection jumps by μ-mass 0.200 at p = .5, while m does not jump;
- crossing masses are 0.245 and 0.200;
- the sum identity and competitiveness show 0 failures on 3000 random regular models;
- the largest piece of a random partition has π ≥ 0.2001 > π(Z) = 0.05.

**Fix to line 118:** "In a two-world ranking with every axiom including (C) this world is impossible (S2.2, then E3). Without (C) it is realised (referee Prop R1)."

What R1 adds:
- R7.1 already showed that (C) is what forces nesting.
- R1 shows that, in a ranking and not merely an edge system, crossing and non-fineness of a complete world coexist, so Q35(5) and Q36(c) genuinely need (Nest_e).

## 5. B3.5 and B3.6: CORRECT

### 5.1 B3.5

Every step was re-derived.
- **Cancellation tools.** Cancellation of ⪯ gives:
  - A ∼ A∖D for D ⊆ A that is ⪯-null (A ⪯ A∖D ⟺ D ⪯ ∅);
  - A ∼ A ∪ D′ for D′ disjoint from A and ⪯-null.
- **(E1) step.** It is applied with A = c_{p*}∖D, and needs only c_{p*}∖D <_i c_{p*} (strict (G)).
- **(E2) step.** It is applied with A = c_{p*} ∪ D′.
- **Edge cases.** The null and co-null cases of c_{p*} are handled correctly.
- **Conclusion on one edge.** A locally constant f on the connected e_ij is constant, so [∅] = [R_ij], and monotonicity makes every subset ⪯-null.
- **Passage to M.** It uses M = ⋃_{k≠i} R_ik, valid for n ≥ 2, with no linking set needed.

Inputs are as stated. (C), (LA), a third world and nestedness are not used.

### 5.2 B3.6

- **Cancellation.** S(A∖B) = S(A)∖S(B) holds (prime filters). So a cancellative ≤₀ on signatures gives a cancellative top level.
- **Dense null sets.** IRWAS Lemma 4, with countably many removals of total measure < ε, gives a non-null W′ ⊆ W in no 𝒰_n. Then S(W′) = ∅, so W′ is ⪯-null.
- **Nontriviality.** Each 𝒰_j contains M = ⋃_k R_ik, hence some R_ik. Then ∅ <₀ S(R_ik), by (i) of IRWAS.
- **Pure charges.** The carrier lemma (N14 Lemma Y) gives dense σ-null sets.

All correct.

### 5.3 GAP (description of IRWAS; line 127)

IRWAS's actual order restricted to M_U is not "S(A) by ≤₀, then a tail". On U the ranks are:
- good or silent where h_i > 0;
- silent or bad where h_i < 0.

So the entries (S₃, S₂, S₁) reduce to lex(≤₀ on S⁻(E), ≤₀ on S⁺(E)). Here S^∓ are the signatures over the ultrafilters concentrated on M ∩ {h_i ≶ 0}, and common parts are replaced using IRWAS (ii).

Consequences:
- This is still a cancellative, strictly signature-monotone preorder on 2^J, so B3.6 covers it.
- It is non-AR only if the cells are placed so that the KPS order is not split between the two tiers; for instance, all 𝒰_j on one side.
- B3's *transported* world (one tier) is legitimate in its own right. By N9.4 any total, cancellative, strictly monotone order on error sets is a world with strict (G) and (IB). It is complete, strictly monotone and cancellative: the tail separates the measure algebra, and the first differing index is preserved under A, B ↦ A∖B, B∖A.

**Fix:** one sentence saying that B3.6 covers both the literal IRWAS order on M_U and the one-tier transport.

## 6. B3.7: CORRECT; extension to incomplete worlds

### 6.1 The proof

All steps were re-derived:
- **Disjoint pieces.** The G_j are built from separating sets H_jl, taken with complements, and then shrunk. Smallness in ν follows from ν ≪ μ, both finite.
- **Signatures.** S(A) = s and S(B) = t hold because A ⊆ ⋃_{j∈s} G_j ∪ W₀ is disjoint from G_l for l ∉ s.
- **Exchange identities.** Φ(A) − Φ(B) = x + D and Φ(A∖B) − Φ(B∖A) = x + D′.
- **Weak cancellation.** It follows from totality and cancellation.
- **D = D′.** If D ≠ D′, choose x strictly between −D and −D′. This is realisable because |D|, |D′| ≤ 2 max|κ| < ν(M)/2.
- **Additivity.** Taking t ⊆ s gives κ additive.
- **Signs.** ∅ ≤_i G with G ⊆ G_j gives κ_j ≥ 0.

**Scope.**
- B3.7 uses neither (S) nor edges. It is a statement about the form of a top level, not about crossings.
- The sentences "To vary continuously, the top level must be able to trade …", "Escaping B3.5 forces additivity" and line 195 ("the one mechanism that defeats fineness … makes it additive") are therefore **HEURISTIC**. B3.7 proves additivity only for value-form top levels with |κ| < ν(M)/4.
- **Fix:** label them HEURISTIC, and delete "the one mechanism". No result shows that crossing is the only way to defeat fineness.

### 6.2 Remark R2 (PROVED, by inspection): leading top levels

Call a total preorder ⪯ on subsets of R_ij (or M) a **leading top level** of world i if both of the following hold:
- A ⪯-strictly-below B implies A ≤_i B;
- A ≤_i B implies A ⪯ B.

For a complete world every top level is leading. Indeed, if A ≺ B then B ⪯ A fails, so B ≤_i A fails, so A <_i B.

**Claim.** Theorems B3.5, B3.6 and Proposition B3.7 hold verbatim for *any* world (complete or not) with "top level" replaced by "leading top level".

**Proof of B3.5.**
- Completeness was used once: from "c_q ≤_i c_{p*}∖D fails" to "c_{p*}∖D ⪯ c_q". The leading property gives this directly: if c_q ≺ c_{p*}∖D, then c_q ≤_i c_{p*}∖D.
- The (E2) step only needs "A ≤_i B ⇒ A ⪯ B".

**Proof of B3.7.**
- Φ(A) < Φ(B) ⇒ A ≤_i B (leading) ⇒ A∖B ≤_i B∖A (cancellation of the preorder ≤_i) ⇒ Φ(A∖B) ≤ Φ(B∖A). The swapped version is the same.
- So the same D = D′ argument runs.
- The resulting π = Φ satisfies both properties of a leading charge. S21 then makes world i add up.

**Consequence.** B3 §5, "*The incomplete alternative*" (line 213), says that for incomplete worlds "B3.5 says nothing". This is **WRONG**.
- An incomplete world of a cover that does not add up has no nonzero leading charge (Q37, contrapositive).
- By R2 it also has no nontrivial leading cancellative top level with dense null sets.
- It has no leading value top level ν + κ∘S with |κ| < ν(M)/4.

**Fix:** replace line 213 with this.

## 7. Conjecture B3.C

### 7.1 Logical repairs

1. **"Equivalently" (line 199) is WRONG.** The edge statement is about abstract edge systems: a complete non-AR order on M plus, on each edge at e_i, a path c_p and an order of world j on R_ij, with (K) and closed sections.
   - The edge statement *implies* B3.C, because a ranking supplies such systems (Lemma Q34).
   - The converse is unproved: an edge system need not extend to a ranking.
   - **Fix:** "B3.C would follow from the edge statement …".
2. **"Complete worlds are excluded from covers of T₁ outright" (lines 29 and 201) is WRONG as worded.**
   - B3.C ⇒ every complete world adds up (B3.2). So in a cover of T₁, *every world that does not add up is incomplete*.
   - In particular, no ranking all of whose worlds are complete covers T₁.
   - Complete worlds may still occur in a cover, alongside an incomplete world that fails.
   - **Fix:** replace both sentences with this.
3. **(Nest_e) failure.** "(Nest_e) can genuinely fail (B3.4 at edge level)": failure of (Nest_e) was already known (Prop plateau; Prop R7.1, in a ranking without (C)). B3.4's new content is *non-fineness together with crossing*.

### 7.2 Prop R3: for n = 2, B3.C contains an exact order-theoretic special case (PROVED)

**Lemma R3.0 (PROVED).** For a cancellative ≤ on subsets of M, A ≤ B ⟺ M∖B ≤ M∖A.

*Proof.* (M∖B)∖(M∖A) = A∖B and (M∖A)∖(M∖B) = B∖A. ∎

**Proposition R3 (PROVED).** Setting:
- n = 2 on M_U;
- ≤ is any total, cancellative, strictly monotone preorder on the measure algebra of M, with class chain L;
- both worlds rank their error sets by lex(μ(E ∩ N₊), E ∩ M under ≤).

Then:
- **(a) Axioms and undominatedness.** Strict (G), (IB) and (LA) hold. Every regular model is undominated and competitive on {1, 2}, because by R3.0, C ⪯₂ X ⟺ E₁X ≤ E₁C on regular models.
- **(b) When (S) holds.** A selection of coherent models with C_{e₁} = P₁ and C_{e₂} = P₂ satisfies (S) iff f(p) := [E₁C_p ∩ M] is continuous from Δ into L with its order topology. The world-1 and world-2 sections of regular X are the preimages of the closed rays; for non-regular X the sections are Δ.
- **(c) The class chain.** If (S) holds, then f(Δ) is connected and contains min L and max L, so f(Δ) = L. Then L is a Hausdorff continuous image of [0, 1], hence compact metrizable, and a connected compact metrizable linear order with endpoints. So **L is order-isomorphic to [0, 1]**: ≤ has a real-valued representation φ onto [0, 1].
- **(d) (C)** fails, as in R7.1. R7.1 is the case where ≤ is the μ-order; Prop R1 is the case where ≤ is the π-order.

**Consequence.** B3.C as stated (any n ≥ 2, no (C)) implies:

> **B3.C′.** Every total, cancellative, strictly monotone order on the measure algebra of M whose class chain is a continuous image of [0, 1], through some path of coherent error sets from M to ∅, is almost representable.

So a counterexample to B3.C′ refutes B3.C, and B3.C′ is the first test of the conjecture.
- B3.C′ is consistent with everything known:
  - IRWAS-type orders have gaps between signature blocks, so their L is not connected, matching B3.6;
  - the π-order of B3.4/R1 has L ≅ [0, 2 + c] and is AR.
- **HEURISTIC (sketch, not refereed).** If the order factors through a vector measure x = (ν_k) whose difference range is a full box, it is AR.
  - Cancellation makes A ≤ B depend only on d = x(A) − x(B).
  - u = x(M) is an order unit, and ℓ(d) := inf{q ∈ ℚ : d ≼ q·u} is additive and monotone, hence linear and ≥ 0.
  - Then ℓ∘x almost agrees with ≤.
- So a counterexample to B3.C′ must use two-valued (ultrafilter-type) pieces filled in by a continuous part, and must defeat the D = D′ mechanism of B3.7 *outside* its small-κ range while keeping L connected.
- B3.7's chaining argument suggests that connectedness of L makes the exchange graph on signatures connected, which forces additivity. This is a reasonable next lemma: **B3.7 with "4·max|κ| < ν(M)" replaced by "L connected"**. It is CONJECTURE.

### 7.3 Assessment

B3.C is plausible and open. Every known non-AR complete order fails it for a proved reason (B3.5 and B3.6). The extension of B3.5–B3.7 in R2 shows that the same obstruction also applies to incomplete worlds whose non-additivity sits in a leading top level.

What is still missing is a structure theory for complete qualitative probabilities on an atomless algebra whose class chain is connected. Prop R3 shows that, for n = 2 without (C), this question is the whole content of B3.C.

**Recommendation:** attack B3.C′ before the three-world, with-(C) form, because:
- it is pure order theory plus one path;
- a counterexample to B3.C′ would at once give a two-world ranking without (C) whose complete world does not add up;
- a proof would close the complete case in every setting, since R3's ranking is the most permissive one.

## 8. Scripts (rerun)

`python3 -I b3py/prop4_edge.py` and `python3 -I b3py/prop7_kappa.py` were rerun. Their output (`b3ref_py/rerun_*.out`) is byte-identical to `b3py/*.out`.

**prop4_edge.py.**
- The (K) test is a **tautology**: for every grid point, m ≤ v or m ≥ v. The "0 failures" line therefore checks nothing.
- The partition test uses intervals only; the abstract argument (§4.3) is what proves non-fineness.
- The continuity check (maximum step 1.5·10⁻⁴) and the crossing check are meaningful.

**prop7_kappa.py.** It checks the finite identity "D = D′ for all s, t ⟺ κ additive". That is correct, but it is the algebraic core only; it does not model realisability, as the script's docstring says.

**Referee's script.** `b3ref_py/two_world_ultra.py` (Prop R1); output in `two_world_ultra.out`, figures in §4.5.

## 9. Summary of fixes

1. "Total", not "complete", at the first use (§1).
2. Lines 18 and 193: "a complete world of a cover *that does not add up* is non-AR".
3. B3.4(d): replace the Remark straighten/Q35(5) argument with the jump argument of §4.3 (PROVED, no Savage). State that (K) is trivial in the example, and mention BPI.
4. Line 118: S2.2 needs (C); without (C) the world is realised (Prop R1).
5. Line 127: say that B3.6 covers both the literal two-tier IRWAS order on M_U and the one-tier transport.
6. B3.7 narrative and line 195: label HEURISTIC, and drop "the one mechanism".
7. Line 213: replace "B3.5 says nothing" with Remark R2.
8. Line 199: "Equivalently" becomes "would follow from".
9. Lines 29 and 201: "every world of a cover that does not add up is incomplete; an all-complete ranking does not cover T₁".
10. Writeup: after Q37, note that "complete and AR" is a case of "leading charge nonzero on M" (B3.1). Add B3.3 and B3.5–B3.7 (with R2) to §8.5 at PROVED status, and record B3.C and B3.C′ as CONJECTURE.
