# S1 referee report: (R4) nestedness from (S), proof side (S1_notes.md)

15 Oct 2026, round 13. Independent, adversarial referee; I did not write S1_notes.md.

- **Read:** BRIEF12; S1_notes.md (all) and `s1py/` (both scripts re-run: outputs reproduced exactly); write-up §2
  (axioms, Thm kkm, Def. CP-a, Def. addup), §8.4(c), §8.5(b)–(d) (Lemma Q34, (Nest_e), Prop Q35, Thm Q36,
  Cor Q37, Prop comonotone, part (c) up to Prop N2, Prop lattice, Lemma G-SE, Conj. Q2.N); Q2_notes §5;
  Q3_notes §4.2; Q3_referee §§4.1–4.4; Q12_referee §0; S2_notes.md (all, for consistency only; S2 is not refereed
  here).
- **Verdicts:** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG. New statements are labelled PROVED / NUMERICS.
- **Scripts:** `s1ref_py/`, run with `python3 -I`. No proof depends on them.
- Notation is S1's: n = 2 on M_U, M = M⁻ ⊔ M⁺, lattice D_{[α,β]}, crossing pair C, C′ with E₁C = m ∪ B,
  E₁C′ = m ∪ A, splices X_{a,b} (E₁ = m ∪ a ∪ (B∖b)) and Y_{a,b} (E₁ = m ∪ (A∖a) ∪ b), a ◁ b for "strictly smaller
  at both worlds", 𝓛 = C_L/~.

---

## 0. Summary

| Claim | Verdict | One-line reason |
|---|---|---|
| **S1.1** Level Lemma | **CONFIRMED** | Re-derived. Uses only (S) (closed sections, 1-D KKM), strict (G), undominatedness and regularity of U, V. |
| **S1.2** (a)–(e) | **CONFIRMED** | (a) needs only S1.1 + competitiveness. (b) order-topology continuity from closed rays. (c)–(e) re-derived. |
| **S1.3** nested selection ⟺ nested representatives | **CONFIRMED** | Every selection hits every class (Thm kkm); replacing C_p by a tied representative preserves (S). |
| **S1.4** five patterns | **CONFIRMED** | Re-derived by hand and by `patterns_ref.py`, which computes the tables by set algebra instead of hard-coding them. The 16-case enumeration is exhaustive (a preorder relation is one of <, >, ~, ∥). |
| **S1.5** rigid crossings | **CONFIRMED**, (ii) **strengthened** | Mixed patterns are excluded for **all** pairs, not only non-segment ones. New: (~,~) occurs **only** at (a,b) = (∅,∅) or (A,B), because (C) must also make Y_{a,b} coherent (§3). |
| (MC_i) definition; additive and countably additive (CP-a) worlds have it | **CONFIRMED** | Monotone / dominated convergence, member by member. New: under (IB) the two clauses of (MC_i) are equivalent (§4.1). |
| **S1.6** (MC) ⇒ chain | **CONFIRMED WITH REPAIR** | (MC₁) and (MC₂) proofs correct. The claim that (MC_sel) is "weaker" than (MC_i) is **false as stated**: S1's (MC_sel) has a world-1 half and a world-2 half, and (MC₁) gives only the first. Repair (PROVED, §4.3): **each half alone suffices**. |
| **S1.7** (a)–(c) | **CONFIRMED** (scope note on (b)) | The "both worlds non-additive" sentence inherits Prop Q15's scope (fixed-source simple/star certificates). It does not say that a world next to an additive world adds up; ratio certificates (N4) remain open. |
| S1 §4 necessary shape | **CONFIRMED WITH REPAIR** | "For each non-initial a … switches" is wrong for a with B ◁ a (no switch). The correct form is unconditional for every non-final b. "(MC_sel) fails at both worlds along that chain, world 1 from above, world 2 from below" holds only across the **pair** of chains (X-splices at C, Y-splices at C′). Along one chain only one half fails, and which one depends on whether the switch is attained (§5). |
| **S1.8** Q35/Q36 need only a nested family | **CONFIRMED WITH REPAIR** | Correct for Q36(a), (b), (d) and Q37. Repairs: Q35(5) and Q36(c) (complete worlds) also transfer and should be listed; LF/IS/MP keep their "relevant comparison" reading only if the family members are (i,j)-tied with C_L members; after S2.1, Q36(c) is the live payoff (§6). |
| **S1.9** edge axioms do not force nesting | **CONFIRMED**, **strengthened** | Verified. S1.9 is not a ranking (its "selected" sets are not coherent or undominated), so it does not model Q35's literal hypothesis (S). A full ranking on M_U (n = 2) with strict (G), (IB), (LA), (S) and a crossing coherent undominated selection exists; only (C) fails (§7, PROVED + NUMERICS). |
| **S1.10** weak edge undominatedness; (EU_ij) for additive i, j | **CONFIRMED** | Trivial. The additive case has a direct two-line proof (§8). |
| **S1.11** under (EU_ij) | **CONFIRMED** (conditional) | Needs that C_q is itself an edge test model (Lemma Q34), so (EU_ij) applies to it. True, but unstated. |
| **S1.12** pairwise straightening | **CONFIRMED** (conditional) | Re-derived, including coherence of D_{M_{x″,y_V}}. |
| S1.13, S1.R | labels correct (CONJECTURE) | §5.6 has an expository gap in "W⁻ ⪯_j c⁻", filled in §9. S1.R can be weakened to one half of (MC_sel). |
| Consistency with S2 | **no conflict** | S1.6 (MC) and S2.2 (leading charge) are complementary; they overlap only on additive/integral worlds (§10). |

**Net.**
- No claim is WRONG in substance.
- One misstatement is repaired, in S1.6: what (MC_sel) is weaker than. The repair strengthens the theorem.
- The §4 "necessary shape" is repaired.
- Two results are strengthened: S1.5(ii) and S1.9.
- The two-world core of the note (S1.1–S1.6) is sound and is a genuine advance. The open part of Q2.N is now
  "both worlds fail (MC_sel), and neither has a nonzero leading charge".

---

## 1. Lemma S1.1 (Level Lemma): CONFIRMED

Re-derivation:
1. U ~₂ V gives S₂(U) = S₂(V) =: G by transitivity. G is closed by (S), since (S) is required for **every**
   X ∈ M_L. Also 1 ∈ G.
2. **0 ∈ G.** Then P₁ ⪯₂ U with E₂U ⊆ M = E₂P₁ (U regular), so strict (G) gives E₂U = M a.e., i.e. U = P₁. Likewise
   V = P₁.
3. **0 ∉ G.** O = [0,1]∖G is open in [0,1], nonempty and proper. 1-D KKM (S₁ ∪ S₂ = [0,1]; Q2 §5.2) gives
   O ⊆ S₁(U) ∩ S₁(V), which is closed. A boundary point q ∈ cl O∖O lies in all four sections. Undominatedness of U
   and V makes all four relations ties, so U ~₁ C_q ~₁ V.

Remarks:
- The proof gives more than the statement: a **selected** C_q tied with both U and V at both worlds.
- Coherence is used only through regularity; (C), (LA) and (IB) are not used. This matches S1's input list.

## 2. Corollary S1.2 and Proposition S1.3: CONFIRMED

**(a)** Every C ∈ C_L is competitive on {1,2}. By Thm kkm it is tied at both worlds with a selected C_s. If
s ∈ {0,1}, then C ~₁ P₁ (or ~₂ P₂), which forces C = P₁ (or P₂) by strict (G).

The four combinations of the two competitiveness disjunctions give three cases: a double tie (by S1.1 whenever one
world ties), U ≺₁ V with V ≺₂ U, or the mirror. Hence ⪯₁ is total on C_L and U ⪯₁ V ⟺ V ⪯₂ U.

Undominatedness is not needed beyond S1.1. A pair "U ≺₁ V and V ~₂ U" is excluded by S1.1 itself.

**(b)** π is onto by Thm kkm. π⁻¹{W ⪯ [U]} = S₁(U) and π⁻¹{W ⪰ [U]} = S₂(U) are closed, so preimages of open rays
are open. A Hausdorff continuous image of [0,1] is compact and connected. A connected linear order topology is dense
and Dedekind complete, and compactness adds end points. [P₁] ≠ [P₂].

**(c)** R₁(X) = π(S₁(X)) is a compact down-set containing [P₁], so it is [min, u_X]; mirror for R₂(X). The cover
R₁ ∪ R₂ = 𝓛 together with density gives l_X ⪯ u_X.

**(d)** Every D ∈ [l_X, u_X] has D ⪯₂ X ≺₂ W, so W ≺ D. Hence the whole interval, not only u_X, lies strictly above
W.

**(e)** W_s ⪯₁ X for each s by (G), and R₁(X) is a closed down-set, so sup S ∈ R₁(X). In the second half, the
hypothesis E₁X ⊆ ess∩E₁W_s ⊆ M forces X regular, so E₂X ⊇ E₂W_s.

**S1.3.**
- Every selection meets every class (Thm kkm applied to it; C_L does not depend on the selection).
- Conversely, C′_p := r(π(p)) is tied with C_p at both worlds, so it has the same sections and the same
  competitiveness, and it lies in C_L.
- The "in particular" (singleton crossing classes ⇒ every selection non-nested) follows.

## 3. Lemma S1.4 and Theorem S1.5: CONFIRMED; S1.5(ii) strengthened

**S1.4.**
- Cancellation gives the tables, and I re-derived each entry. For example, (m∪B)∖X_{a,b} = b and X_{a,b}∖(m∪B) = a,
  and the world-2 differences are swapped.
- `s1ref_py/patterns_ref.py` builds E₁ as sets of atoms {m, a, A∖a, b, B∖b, rest}, with E₂ = M∖E₁. It computes the
  difference pairs by set algebra, imposes K_C, K_C′ and non-domination of C and C′, and recovers exactly the five
  patterns. The edge version (competitiveness only) gives exactly nine patterns.
- Exhaustiveness: the relation between two sets in a preorder is one of <, >, ~, ∥, so the 4 × 4 enumeration is
  complete.

**S1.5(i).** Both mixed-pattern exclusions are correct. Each uses 1-D KKM at X, then S1.1 or S1.2(a) at the pair
(C_r, C). Neither uses that (a,b) is non-segment, so **the mixed patterns are excluded for every (a,b)**. The (C) step
excluding (~,~) for non-segment pairs is correct.

**S1.5(ii)′ (strengthening, PROVED).** If (a,b) has pattern (~,~), then (a,b) ∈ {(∅,∅), (A,B)}.

*Proof.*
1. Pattern (~,~) gives C ~ X_{a,b} at both worlds (S1.4 table). It also gives C′ ~ Y_{a,b} at both worlds (second
   table: C′ ⪯ᵢ Y ⟺ a ≤ᵢ b or b ≤ᵢ a according to i, both true).
2. By (C), both X_{a,b} and Y_{a,b} are coherent.
3. By Prop lattice:
   - X_{a,b} is coherent iff a is σ-initial and b τ-final in A, B;
   - Y_{a,b} is coherent iff a is σ-final and b τ-initial.
4. Since σ and τ have positive densities on their ranges, a ∈ {∅, A} and b ∈ {∅, B}.
5. (∅,B) and (A,∅) are excluded by strict (G), since ∅ <ᵢ B and ∅ <ᵢ A. ∎

NUMERICS: `patterns_ref.py` (2), with 5 + 5 cells and all 1024 pairs. Only the four corners have both splices
coherent.

*Consequence.* In a tied crossing (C ~ C′), every splice other than C and C′ is strictly comparable with C, with
the same direction at both worlds. This includes the coherent lattice points between them. S1 §4's "every segment
lattice point doubly tied with C lies in C_L" is therefore true but vacuous beyond C′.

## 4. Monotone continuity and Theorem S1.6

### 4.1 The definition (CONFIRMED) and a clause equivalence (new, PROVED)

(MC_i) is Villegas-type monotone continuity of the set order ≤_i on subsets of M, with an ↑ clause and a ↓ clause.

**Proposition R4.1 (PROVED).** Under (IB) (de Finetti cancellation), the ↓ clause implies the ↑ clause, and
conversely.

*Proof (↓ ⇒ ↑).*
1. Let Y_k ↑ Y and Y_k ≤ Z. Put p_k := Y_k∖Z and q_k := Z∖Y_k, so p_k ≤ q_k.
2. Add D_k := (Y∖Y_k)∖Z, which is disjoint from p_k and q_k, to both sides. Cancellation is unchanged, so
   Y∖Z ≤ q_k ∪ D_k.
3. The right side decreases to Z∖Y. If x is in every q_k ∪ D_k but leaves q_K, then x ∈ D_k for all k ≥ K. Since
   D_k ↓ ∅, this is impossible.
4. The ↓ clause gives Y∖Z ≤ Z∖Y, i.e. Y ≤ Z.

The converse is the same with the moving set on the other side: add r₁∖r_k to l_k ≤ r_k. ∎

So "(MC_i)" may be read as either clause.

**Additive worlds.** ψ(Y) = ∫_Y w dμ with w ∈ L¹, w > 0 a.e. Monotone convergence gives (MC).

**(CP-a) with countably additive members.**
- On M_U, Λ_iY − Λ_iX = w_i(1_{E_iY} − 1_{E_iX}), with w_i = |λ_i(·,+) − λ_i(·,0)| bounded and > 0 a.e.
- For each P ∈ 𝓜_i, P is countably additive and P ≪ μ. Dominated convergence passes P(w(1_{Y_k} − 1_Z)) ≥ 0 to the
  limit for that P, and the conclusion is "≥ 0 for every P".
- No uniformity over 𝓜_i is needed. CONFIRMED.

Finitely additive members can fail (MC) (e.g. a Banach-limit charge), as S1.7(c) says.

### 4.2 The (MC₁), (MC₂) and (MC_sel) proofs: CONFIRMED

I checked every step, including the end cases:
- β* = β_{C′}: then B ≤₁ a, against a ◁ B;
- β* = β_C: then a ≤₁ ∅, against strict (G).

The other checks:
- Non-initiality of a_k makes every (a_k, b) non-segment.
- 𝔅 is an up-set because b(β) ↓ as β ↑ and both worlds are strictly monotone.
- The ↓ limit b(β) ↓ b(β*) holds modulo the null cone {τ = β*}.

The (MC_sel) proof, which uses both halves, is also correct.

### 4.3 Repair: what (MC_sel) is weaker than

S1 calls (MC_sel) "the weaker property". As defined in S1, (MC_sel) has two halves:
- **(MC_sel)₁:** for W ∈ C_L, if E₁X_k ↓ E₁X and W ⪯₁ X_k for all k, then W ⪯₁ X;
- **(MC_sel)₂:** for W ∈ C_L, if E₁X_k ↑ E₁X and W ⪯₂ X_k for all k, then W ⪯₂ X.

(MC₁) implies (MC_sel)₁ (take Z = E₁W in the ↓ clause). It does **not** imply (MC_sel)₂, which is a world-2
property. So (MC_sel) as stated is weaker than (MC₁) ∧ (MC₂), not than (MC₁).

**Theorem S1.6′ (PROVED).** In n = 2 with every axiom, (MC_sel)₁ alone forces C_L to be a chain, and so does
(MC_sel)₂ alone. Since (MC_i) ⇒ (MC_sel)_i, this contains S1.6. It is weaker than (MC₁) ∨ (MC₂), as S1 intended.

*Proof from (MC_sel)₁.* Let C, C′ cross, as in S1.6.
1. **A piece a with a ◁ B.** If B ◁ a_k for all k, then C ⪯₁ X_{a_k,B}, with E₁ = m ∪ a_k ↓ m. So C ⪯₁ (model with
   E₁ = m), against strict (G). Fix a := a_k with a ◁ B.
2. **The switch.** Define 𝔅 and β* as in S1.
3. **From above, at C.** For β > β*, b(β) ◁ a, so C ⪯₁ X_{a,b(β)}. As β ↓ β*, E₁X_{a,b(β)} = m ∪ a ∪ (B∖b(β))
   decreases to E₁X_{a,b(β*)}. (MC_sel)₁ at W = C gives b(β*) ≤₁ a. If β* = β_{C′}, this contradicts a ◁ B.
4. **From below, at C′.** Otherwise, for β ∈ [β_{C′}, β*), a ◁ b(β), so a ≤₁ b(β), i.e. C′ ⪯₁ Y_{a,b(β)}. As
   β ↑ β*, E₁Y_{a,b(β)} = m ∪ (A∖a) ∪ b(β) decreases (mod null) to E₁Y_{a,b(β*)}. (MC_sel)₁ at W = C′ gives
   a ≤₁ b(β*).
5. **Contradiction.** So a ~₁ b(β*) at a non-segment pair, against S1.5(i).

(MC_sel)₂ is the mirror:
- Y_{a_k,B} has E₁ ↑ as a_k ↓ ∅, which gives B ≤₂ ∅.
- From above, at C′: Y_{a,b(β)} with E₁ ↑ as β ↓ β*.
- From below, at C: X_{a,b(β)} with E₁ ↑ as β ↑ β*. ∎

The point S1 missed: the world-1 half can be used **at C′ along the Y-splices** for the side where S1 used the
world-2 half at C.

## 5. S1.7 and S1 §4

**S1.7 (a), (c): CONFIRMED**, by §4.1.

**S1.7 (b): CONFIRMED**, with a scope note on its last bullet.
- With (Nest) derived, Lemma N0 and §8.5(c) apply verbatim, including Prop Q15 when world 2 is additive with
  integrable density (or countably additive (CP-a), by Cor CPaU(b) and Thm fullsupport).
- "Any two-world counterexample needs both worlds non-additive" is the write-up's gloss on Prop Q15. Q15 covers
  simple, vanishing-target and star certificates with a fixed source. Next to an additive world, ratio
  certificates with thin sources (writeup, after Prop N2; Q12_referee N4) are not excluded.
- S1.7(b) removes (Nest) from that gloss, which is correct. It does not widen its scope. The write-up's wording
  should say "any two-world counterexample of the Q15 types".

**§4 "Rigid crossing" orientation, "Tied crossing": CONFIRMED.**
- C ≺ C′ in 𝓛 gives B <₁ A (world-1 cancellation) and B <₂ A (world-2 differences swapped).
- S1.5(ii)′ makes the tied case sharper (§3).

**§4 "Necessary shape": CONFIRMED WITH REPAIR.**
1. *Switches.* For non-initial a with B ◁ a, b(β) ⊆ B gives b(β) ◁ a for every β, so there is no switch. Without
   (MC), step 1 of S1.6 cannot produce an a with a ◁ B. The correct unconditional statement (PROVED) is the
   following. In either kind of crossing, for every non-null non-final b ⊆ B, b ◁ A, because b ≤ B ≤ A and (b, A)
   is non-segment, hence strict. Along the σ-initial chain a(α) := {α_C ≤ σ < α}:
   - ∅ ◁ b ◁ A;
   - every (a(α), b) is non-segment;
   - so the cross relation switches at some α* with no tie.

   For non-initial a, a switch along b(β) exists iff a ◁ B.
2. *Which half of (MC_sel) fails, and where (PROVED).* Fix one switch, say along b(β) at β*.
   - **Attained** (b(β*) ◁ a): the world-2 half fails at C along X_{a,b(β)}, β ↑ β*, and the world-1 half fails at
     C′ along Y_{a,b(β)}, β ↑ β*.
   - **Not attained** (a ◁ b(β*)): the world-1 half fails at C along X, β ↓ β*, and the world-2 half fails at C′
     along Y, β ↓ β*.

   So both halves fail in every case, as S1 says, but at **different** members of the pair. Along a single chain at
   C, only one half fails. This agrees with §4.3: each half alone would force a chain.

**§4 consequences and "Inhabitation":** CONFIRMED (conditional statements; nothing is claimed to exist).

## 6. Remark S1.8: CONFIRMED WITH REPAIR

I checked the stated input list against Q3_notes §4.2 and Q3_referee §4.1.
- **"No missing value" and continuity.** They use only the sections at the test sets ess∪{c : β < t} and
  ess∪{d : β > t}. These are closed by hypothesis, and they disjointly cover the index space if t is missed. So any
  chain family indexed by a compact **connected** set works, with c = ∅ and c = R_ij at two index points and (K) at
  every index whose β ∈ (0,1). The family can then be reparametrised by β.
- **B1, N1, DL, DR, T and E2.** They use the chain, closed b-sections, (K), strict (G), cancellation and test sets
  inside R_ij (Q3_referee §4.1). None uses that the family is selected.
- **Q36(a), (b), (d) and Q37.** A leading charge with density, or a Savage measure, endorses every comparison, so
  SP^reg does not depend on which family produced it.

Repairs:
1. **Missing items.** Q35(5) (Lemma T with m = 1, completeness, compactness) and hence **Q36(c)** (complete worlds,
   CHECKED via Savage) also use only these inputs. They belong in S1.8's list. S1.13's payoff sentence should then
   read "Thm Q36 (a)–(d) and Cor Q37".
2. **Reading of LF, IS and MP.** These hold for the family's cut pairs. Their identification with *relevant*
   comparisons (Lemma cutform; Q3_referee §4.3's Q1.10 transfer) needs each family member to be tied at worlds i
   and j with a member of C_L. S1.12's straightened models have this property; an arbitrary nested family need not.
3. **Interaction with S2 (conditional on S2.1 being confirmed).** If S2.1 holds, Q36(a), (b) and Q37's
   leading-charge clause hold without (Nest_e). The live content of straightening is then Q36(c) / Q35(5) for
   complete worlds, which is exactly the item S1.8 omits.

## 7. Example S1.9: CONFIRMED; the strengthening

**S1.9 checked.**
- For c and A: either μ(c) ≤ μ(A), or μ(R∖c) ≤ μ(R∖A). So (K) holds at every b.
- The b-sections {p : μ(c_p) ≤ μ(A)} are closed by continuity.
- Strict (G) and (IB) hold.
- The path is continuous at p = 1/3 and p = 2/3, and c_{1/3} ∩ c_{2/3} = ∅.
- Re-run of `plateau_edge.py`: reproduced.

S1.9 shows what S1.8 needs: the edge-level inputs do not force (Nest_e).

**What S1.9 does not show.** Q35's literal hypotheses are a ranking on M_U with strict (G), (IB), (LA) and (S).
(S) includes C_p ∈ C_L: coherent and undominated. S1.9 is not a ranking, and its sets c_p are neither. That gap is
closed by:

**Proposition R7.1 (PROVED; NUMERICS `s1ref_py/mu_equal_density.py`).** Let n = 2, M_U with K′ = [α′,β′] ⊂ (0,1),
ψ₁(X) = μ(E₁X) and ψ₂(X) = μ(E₂X). Let p ↦ C_p = D_{[α(p),β(p)]} be any path of lattice points with
m(p) := μ(E₁C_p) continuous and nondecreasing, (α,β)(0) = (0,β′) and (α,β)(1) = (α′,1). Then strict (G), (IB),
(LA) and (S) hold, closed sections included for every model. For a non-comonotone path, for instance
(0,β′) → (α′,β′) → (α₁,β₁) at constant mass → (α′,β₁) → (α′,1), (Nest_e) fails on e₁₂ = Δ. Only (C) fails.

*Proof.*
1. **The key identity.** For every X ⊆ U, ψ₁(X) + ψ₂(X) = μ(M) + 2μ(N₊∖X). On M exactly one world errs at each g;
   on N₊ both err or neither does.
2. **Regular models.** Every regular model therefore minimises ψ₁ + ψ₂. Hence it is undominated and competitive on
   {1,2}.
3. **Vertices.** C₀ = P₁ is competitive on {1}, since ψ₁(P₁) = 0. Likewise C₁ = P₂ on {2}.
4. **Sections.** S₁(X) = {m(p) ≤ ψ₁(X)} and S₂(X) = {μ(M) − m(p) ≤ ψ₂(X)} are closed.
5. **(C) fails.** It fails at any incoherent regular model of the same mass. ∎

NUMERICS (exact angular masses, Gaussian μ, K′ = [0.35, 0.6]):
- the path is nondecreasing, with maximum step 1.0·10⁻⁴ on 4001 points;
- C_{1/4} = D_[0.35,0.6] and C_{1/2} = D_[0.1,0.828] cross, with differences of mass 0.061 each;
- 300 random models give 0 violations of the identity and 0 violations of competitiveness.

So (Nest_e) is not a consequence of Prop Q35's hypotheses, even for a full ranking. In n = 2 the missing ingredient
is exactly (C). This answers the brief's question 5: yes, and more sharply than S1.9 says.

S1's sentence "any derivation must use three-world undominatedness or (C)" is correct. For n = 3, "world 3" should
be read as "(C), or undominatedness through world 3". This is consistent with S2.0(c), which uses both.

## 8. S1.10, S1.11, S1.12: CONFIRMED (S1.11, S1.12 conditional)

**S1.10.** Immediate.

**(EU_ij) for additive i, j with densities > 0: CONFIRMED.** A direct proof, simpler than the zonoid argument:
1. Suppose A has ν_i(A) < ν_i(c) and ν_j(R∖A) = ν_j(R∖c).
2. If R∖A were null, then c = R mod null, against ν_i(A) < ν_i(c). So R∖A is non-null.
3. Add to A a non-null D ⊆ R∖A with ν_i(D) < ν_i(c) − ν_i(A). Then A ∪ D is strictly better than c at both worlds,
   since ν_j(D) > 0. That contradicts competitiveness.
4. The other case is the mirror.

NUMERICS: `eu_zonoid.py`. With positive weights there are 0 competitive-but-not-Pareto sets over 40 × 2¹⁰ subsets.
With w_j = 0 on one cell there are 6, so positivity of both densities is needed.

**S1.11.**
- (a) Step 5 of S1.1 needs C_q ⪯ U at i and j to be ties. (EU_ij) speaks of *edge test models*. C_q is one by
  Lemma Q34: it equals P_i off R_ij and is determined by E_iC_q. With this added, the proof is complete. The vertex
  case uses E_j(P_i) = R_ij.
- (b) π is onto by the definition of the edge family.
- (c) The patterns are those of S1.4 with (EU_ij) in place of undominatedness, and the mixed patterns are excluded
  by edge KKM. Correct. (~,~) survives because (C) needs ties at all three worlds, and edge splices differ at world
  3.

**S1.12.**
- (a) {s : a(s) <_i B} is a down-set. Both (MC_i) limits and completeness on cross pairs (S1.11(c)) give
  a(s*) ~_i B with s* ∈ (0,1), and then (~,~). X ⊆ E_iV.
- (b) From Prop comonotone:
  - m = F(x_U) ∪ G(y_V), A = F(x_V)∖F(x_U), B = G(y_U)∖G(y_V);
  - m ∪ a(s*) = F(x″) ∪ G(y_V) is the error set of D_{M_{x″,y_V}}, valid since x″ ≤ x_U ≤ y_U < y_V;
  - both models equal P₁ off R₁₂.
- The straightened model is nested with V and tied with U. By §4.1, (MC_i) here may be either clause.

## 9. S1.13, S1.R and §5.6

The labels are correct (CONJECTURE).

**§5.6 expository gap (filled).** S1 shows only that no D ≺ W⁻ has D ⪯_j c⁻, i.e. l_{c⁻} ⪰ W⁻. To get
W⁻ ⪯_j c⁻:
1. c⁻ ~_i W⁻ gives u_{c⁻} = W⁻. Every D ≻ W⁻ has c⁻ ≺_i D.
2. Edge KKM (R_i ∪ R_j = 𝓛_e) puts every D ≻ W⁻ in R_j(c⁻).
3. By density and closedness, W⁻ ∈ R_j(c⁻). (If W⁻ = max, then W⁻ = [P_j]-type, and this is trivial.)

The stated missing inequality c⁻ ⪯_j W⁻ is then indeed the gap.

**S1.R can be weakened.** By §4.3 it suffices that (S) forces **one** half, (MC_sel)₁ or (MC_sel)₂, and only for
W ∈ {C, C′} along splice chains inside the crossing rectangle. This is the "nearby target" to aim at.

## 10. Consistency with S2_notes

**Overlap.**
- S2.2 (a nonzero leading charge at either world ⇒ chain, two worlds, every axiom) and S1.6′ ((MC_sel)_i at either
  world ⇒ chain) are logically independent.
  - A lexicographic world lex(ν, λ) with a countably additive first level has a leading charge but can fail (MC).
  - An incomplete countably additive (CP-a) world has (MC) but in general no single leading charge.
- Both cover additive integral worlds.

**Combined necessary condition (PROVED, modulo S2.2's referee).** A non-nested two-world system with every axiom
has both worlds failing (MC_sel)₁, (MC_sel)₂ and (MC), and both worlds without a nonzero leading charge.

**No conflicts.**
- S2's "cross-agreement" (§3, via PL) is the special case of S1.4/S1.5 with an incoherent splice. S1.5(ii)′ is the
  PL observation applied to both X_{a,b} and Y_{a,b} = F△(P∪Q).
- S2.2's "each member fixed by its π-level" means singleton classes in 𝓛, consistent with S1.2.
- S2.0(c) (additive three-world edge selections are nested) is consistent with S1.9 and with §7. It uses (C) and
  world k.
- S2.0(c) does make S1 §5.7's phrase "doubly tied crossings are the expected genuine non-nested possibility" too
  strong. In additive systems they cannot occur, and S2.4 shows that they need world-k fans. The phrase should be
  "the only non-nested possibility not excluded".
- S1.10's additive (EU_ij) and S1.12 are moot in the fully additive case (S2.0(c)), but not when worlds i, j are
  non-additive with (EU_ij) and (MC).

## 11. Exact established statements (after this report)

Two worlds (n = 2, M_U, strict (G), (IB), (LA), (S), (C) unless noted):
1. **Level Lemma** (no (C), (IB), (LA) needed). U, V undominated and regular, U ~_i V ⇒ U ~_j V. Moreover some
   selected C_q is tied with both at both worlds. PROVED.
2. **Continuum.** ⪯₁ totally preorders C_L and ⪯₂ is its reverse. 𝓛 = C_L/~ is a compact linear continuum, π is a
   continuous surjection, R₁(X) = [min, u_X], R₂(X) = [l_X, max], l_X ⪯ u_X. Strict escape: E₁X ⊋ E₁W ⇒
   [l_X, u_X] ≻ W. Inclusion closedness. PROVED.
3. **S1.3.** A nested selection for the given ranking exists iff the ~-classes of C_L have nested representatives.
   PROVED.
4. **Crossings.** For crossing C, C′ ∈ C_L and every (a,b): the pattern is (<,<) or (>,>), except that
   (a,b) ∈ {(∅,∅),(A,B)} has (~,~). PROVED (S1.4, S1.5, S1.5(ii)′).
5. **Chain criteria.** If (MC_sel)₁ or (MC_sel)₂ holds, in particular if (MC₁) or (MC₂) holds (either clause), then
   C_L is a chain and Q2.N holds. This applies when one world is additive with integrable density, or (CP-a) with
   countably additive members, and then all of §8.5(c) holds without (Nest). PROVED.
6. **Necessary shape of a crossing.** For every non-null non-final b ⊆ B there is a tie-free switch along the
   σ-initial chain of A. Both halves of (MC_sel) fail, one at C and the other at C′. PROVED.
7. **Without (C), (Nest_e) fails.** A full ranking with strict (G), (IB), (LA), (S) and a crossing coherent
   undominated selection exists (R7.1). So Prop Q35's hypotheses do not imply (Nest_e). PROVED.

Edges (n = 3):

8. S1.10. PROVED. (EU_ij) holds for additive i, j with positive densities. PROVED.
9. Under (EU_ij): edge Level Lemma, 𝓛_e, patterns (<,<), (>,>), (~,~). PROVED (conditional).
10. Under (EU_ij) + (MC_i) on R_ij: pairwise straightening, coherent on the D_{M_{x,y}} family. PROVED
    (conditional).
11. Q35(1)–(5), Q36(a)–(d) and Q37 hold for any nested edge family with the S1.8 inputs. For LF, IS and MP to read
    as relevant comparisons, the members must be (i,j)-tied with C_L. PROVED (inspection).

Open (CONJECTURE):
- Q2.N in general, reduced to S1.R, which is weakened to one half of (MC_sel) at the crossing pair;
- S1.13, global edge straightening, whose live payoff (given S2.1) is Q36(c).

## 12. Files (`s1ref_py/`, `python3 -I`)

- `patterns_ref.py`, `.out`:
  - S1.4 tables computed by set algebra, with the five patterns (and nine without (EU));
  - S1.5(ii)′, where on 5 + 5 cells only the four corners have both splices coherent.
- `mu_equal_density.py`, `.out`: Proposition R7.1, a full n = 2 ranking on M_U with a crossing selection. It uses
  exact angular masses and Monte Carlo checks of the identity and competitiveness.
- `eu_zonoid.py`, `.out`: (EU_ij) for positive additive densities, and its failure when one density vanishes on a
  cell.
