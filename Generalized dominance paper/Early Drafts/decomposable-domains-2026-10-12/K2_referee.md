# K2 referee report: (M1) certificates in full systems (divisibility, two worlds, frontier, decoration scheme, edge obstruction)

15 Oct 2026, round 19. Referee of `K2_notes.md` against:
- BRIEF16 (and BRIEF13 rules);
- N17 §§0–3 and N19_referee §2.3 (Lemma 3.1 confirmed there);
- B1 §§0–2 (sign classes, Def. of leading density, Lemma B1.0);
- H1 §§0–2;
- write-up §§2–3 and §8.5 (Thm S22, Lemma level, Cor continuum, Lemma rigid, Thm MC, Cor MC, Prop R71, Conj Q2N), with their S1/S2 referee statuses as recorded there.

Scripts:
- `k2py/` was rerun with `python3 -I`. Both outputs reproduce exactly.
- Referee checks are in `k2ref_py/k2ref_checks.py` (+ `.out`). They are NUMERICS only.

## Summary of verdicts

| Item | Verdict | One line |
|---|---|---|
| K2.1 Divisibility Theorem | **CORRECT** | Integer reduction, Lyapunov equipartition, assignment, chaining and strict (G) all check. |
| K2.2 forced ⇒ divisible (incl. transport to tied C_p) | **CORRECT** | Both halves check. |
| K2.2′ second sentence | **GAP (wording, fixable)** | It proves "ρ_j(E_jX) ≥ ρ_j(E_jB) for some j", not "X ⊀_j B". |
| K2.3 (n = 2) | **CORRECT** | Essentially immediate from N17.3 + Cor MC(b). Two loose phrasings. |
| K2.4 (a)–(e) | **CORRECT** | — |
| K2.4 readings | **GAP (fixable)** | "Crossing for free" needs interleaving. "(M1) ⇒ H1 case (A)" uses a wrong inference; the conclusion holds via H1.2 directly. |
| K2.5 construction scheme | **CORRECT** | Every axiom checks, closed sections and (C) included, from (fit), (E), (P), (Cert). |
| K2.6 (linear endorsers) and K2.6a (Brier satisfies SPREAD) | **CORRECT** | — |
| K2.6, outcome wording | **GAP (wording)** | "Both hold for the Brier base": only SPREAD is proved. ADJ holds there numerically. |
| K2.6, strengthening | **New (R6.2, PROVED here, one reader)** | Over the Brier base the linear ansatz is unnecessary: every nonnegative integrable endorser of the small edge trades is cρ_1 on M. So the K2.5 template is empty for every weak-* closed cone 𝒦. |
| K2.7 edge sweep | **CORRECT** | — |
| §0 "single obstruction in words", §8 "what a T1 cover must therefore do" | **OVERSTATED** | These hold for K2.5-type decorations, not in general. They are conditional on CONJECTURE K2.6′. |

There is no WRONG item. The mathematics is sound line by line. The defects are scope statements in the readings, the outcome and §8.

---

## 1. K2.1: Divisibility Theorem. CORRECT

**Definition.**
- Divisibility of δ ∈ 𝒜_i means acceptance of every sub-move δ′ that is proportional with one common f ∈ (0,1] in every measure of a finite family ℳ_δ ∋ μ|_U.
- It is well posed.
- The inclusion of μ|_U is exactly what step 5 needs: the uncovered negative piece has μ-mass μ(c₀)/N₀ > 0.

**Step 1 (integer weights).**
- Λ = {λ ≥ 0 : Dλ ≤ 0} is a rational polyhedral cone, so it has integer generators.
- (Dλ)_{c₀} = Σ μ_s (Dw_s)_{c₀} < 0, with every term ≤ 0. So some generator is strict at c₀.
- Zero entries of n are discarded harmlessly: a zero vector δ_k contributes nothing.

**Step 2 (equipartition).**
- ℳ is a finite family of finite measures, all ≪ μ. They are atomless because μ is Gaussian. Each ρ_jμ in K2.2 is finite because leading densities are integrable by B1's definition.
- Iterated Lyapunov therefore gives N₀ pieces per cell, equal in every m ∈ ℳ.

**Steps 3–4 (assignment).**
- In each cell, the negatives take Σ_neg n_k ≤ N₀ distinct pieces.
- The positives take Σ_pos n_k ≤ Σ_neg n_k pieces among the negative ones. A positive piece of k is never k's own negative piece, since δ_k(c) = +1 there.
- k gets exactly n_k pieces in every cell of its support. So m(δ′_k^±) = (n_k/N₀)·m(δ_k^±) for all m ∈ ℳ_{δ_k}, with one fraction f_k = n_k/N₀ ≤ 1.
- The bound n_k ≤ N₀ holds in both kinds of cell.

**Step 5 (contradiction).**
- Gains are pairwise disjoint and losses are pairwise disjoint, so the chaining lemma N17.1(b) applies.
- The sum is 0 or −1 on each piece, and −1 on some piece of c₀.
- This contradicts strict (G).

**Script.** Rerun: 3000 certificates, 0 failures. The script checks steps 3–5 combinatorially, which is the only nontrivial bookkeeping.

**The remark on N17.7's g_i is CORRECT.**
- At f = 1/2 a proportional part violates G_θ, since 0.6f > θ·0.4f.
- It violates every 𝒢_l: μ(C_l ∖ δ′⁺) ≥ 0.2 > 1.2θ/(1−θ) for l = i, and ≥ 0.3 for l ≠ i.
- One failing f suffices for non-divisibility.

**The D2 remark (CHECKED in K2) is plausible but was not re-derived in full.**
- A route: run Lyapunov shell by shell near x = 1, adding λ|_{Q_{g′} ∩ shell} for finitely many g′ per shell. The part then misses a positive fraction of every tail of every Q_{g′}.
- It is a remark and nothing depends on it.

## 2. K2.2 and K2.2′: forced comparisons are divisible. CORRECT, with one wording gap

**"It holds."**
- B and C_p are coherent members of M_U, hence regular. So Lemma B1.0 (L2), applied both ways, gives ρ_j(E_jB) = ρ_j(E_jC_p).
- B1.0 + (L1) give the strict form: ρ_j(E_jX) < ρ_j(E_jC_p) ⇒ X ≺_j C_p.
- Competitiveness on supp p then leaves only world i, and B ∼_i C_p transports the comparison to B. This is the "transport to tied members of C_L" asked about. It is correct.
- J = ∅ (p = e_i) is covered vacuously.

**"Divisible."**
- X′ = B △ supp δ′ is regular, because supp δ′ ⊆ M.
- Its vector is δ′, and (1.1) gives ρ_j(E_jX′) − ρ_j(E_jB) = f·(ρ_j(E_jX) − ρ_j(E_jB)) < 0. All four measures lie in ℳ_δ.
- The comparison is re-forced through the same C_p. Correct.
- Cosmetic: ρ_j is defined on M, so write ρ_jμ|_{A_ij ∩ M}. δ vanishes on N₊ anyway.

**K2.2′, first sentence: CORRECT.**

**K2.2′, second sentence: GAP (wording).**
- The negation of "forced" is: some j ∈ supp p ∖ {i} has ρ_j(E_jX) ≥ ρ_j(E_jB).
- Read with ≺_j, "X is not strictly better than B at j" is stronger. With a leading density, X ≺_j B and ρ_j(E_jX) = ρ_j(E_jB) can coexist (lexicographic tie-breaking).
- **Fix:** state it in ρ_j.

## 3. K2.3: two worlds. CORRECT (one comment on novelty)

**Proof.**
- For n = 2 and regular models, exactly one world errs at each h ∈ M. So E_2 = M ∖ E_1, and world-2 crossing is equivalent to world-1 crossing.
- N17.3 Lemma 3.1 (confirmed, N19_referee §2.3) applied to the bases alone: if the bases formed a chain, the largest error set would contain all the others and the certificate would vanish. So two bases cross, and {E_1C : C ∈ C_L} is not a chain. That gives (a) and the first part of (c).
- (b) is exactly write-up Cor. MC(b), the contrapositive of Thms S22 and MC. Those need every axiom including (C), which K2.3 assumes.
- The "class closed" list matches Cor. MC(a) and the status note of Cor. MC: additive with density, (CP-a) with countably additive members, lexicographic with a charge first level, monotonely continuous.

**Precision points.**
- (c) "C_L is a linear continuum in the order of world 1" should read: the set 𝔏 of double-tie classes of C_L is a compact linear continuum (Cor. continuum(b)).
- (c) "A jump without a tie at every crossing" paraphrases the necessary-shape status of Thm MC. In that statement the relation of b with the initial σ-bands of A switches with no tie. Quote it that way.

**Novelty.**
- K2.3 is N17.8(c) + Lemma 3.1 + Cor. MC(b) assembled.
- Its value is the explicit statement that an (M1) two-world example **is** a Q2N counterexample of the hardest kind: no leading charge and no (MC_sel) at either world.
- The reading "at least as hard as refuting Q2N" is correct. The remark that a two-world (M1) system without (C) is "not excluded here" is fair. Note that Prop. R71, the known non-(C) crossing system, has both worlds additive and so no (M1).

## 4. K2.4: frontier family. (a)–(e) CORRECT; readings need repair

**(a)**
- 𝒯 is countable: the tie sets {r = κ(s)} ∩ R_jk are disjoint and of finite measure.
- Off 𝒯, the pointwise minimiser of sψ_j + (1−s)ψ_k is a.e. unique. On Q_i and N₊ the field never vanishes.
- Fact 0 gives a selected C with C ⪯_l F_s at every l. Additivity at j, k makes C a minimiser, so C = F_s, and F_s ∈ C_L.

**(b)** Correct. A forcing index p ⊇ {j, k} would need X to be ψ-strictly better at both j and k, so X would be a second minimiser.

**(c)** Verified class by class (Q_i: the j, k side is wrong at i; Q_j: side with j iff r < κ; Q_k: side with k iff r > κ; N₊ correct).
- NUMERICS: k2py 0 mismatches.
- Referee check (4): 243 722 candidate gain points over 200 random frontier families, 0 outside the predicted class.

**(d)** The set differences are right.

**(e)**
- By Lemma 3.1, the gain of a comparison at a base lies in the error set of some base with a different error set.
- For the least s, the other bases' error sets meet Q_k ∩ {r ≤ κ} only in null sets. So the gain lies in Q_j ∩ {r ≥ κ}. The largest s is the mirror case.
- The least and largest s differ, otherwise the bases form a chain.

**On "executable as a pair."**
- Disjoint gains alone do not put δ_k + δ_l in 𝒞, because the losses can overlap (both contain Q_i-parts).
- The claim is still true after weakening. 𝒜_i is upward closed in 𝒞 (sum with 1_O ≥ 0). So replace δ_l by δ_l + 1_{O}, with O the common loss; then the chaining lemma applies.
- In K2.5 terms the content is cleaner: disjoint gains give ∫(g_k + g_l)φ ≤ ∫_{g_k⁺ ∪ g_l⁺}φ ≤ ∫_Uφ, so (P) fails at that pair. State it this way.

**Readings, GAP 1: crossing is not "for free".**
- The frontier models cross only if r = ρ_k/ρ_j interleaves on Q_j and Q_k. It does for Brier (NUMERICS).
- If ess sup_{Q_j} r ≤ ess inf_{Q_k} r, the frontier is a chain. Nothing in K2 excludes this when the F_s are coherent.
- **Fix:** add "when r interleaves" in the outcome (item 3) and in §8.

**Readings, GAP 2: the route to H1's case (A) is wrong.**
- "An (M1) world has no positive endorser at all, so it sits in H1's surviving case (A)" does not follow.
- An (M1) certificate excludes bounded positive weights, and σ-finite densities that are finite on the certificate's supports.
- It does not exclude an a.e.-finite density of infinite mass on those supports. For example, the cancellation reading (E2) can be ∞ ≤ ∞, as in D2's world (Prop. D2sigma).
- Nor does it say anything about H1's D-localized comparisons, which are a different family.
- The intended conclusion still holds, by a different route. If j and k are additive with integrable densities, H1's (B) (a second exceptional world) and (C) (purely finitely additive endorsers at the other worlds) are excluded. So by H1.2 every T1 cover in this class has its third world in (A), whether or not it is (M1).
- **Fix:** cite H1.2 directly.

## 5. K2.5: the construction scheme. CORRECT

Every axiom was checked line by line.

**Normal form.**
- δ ≥ 0 lies in 𝒦, since Ψ ≥ 0.
- A nonzero δ ≤ 0 is not in 𝒦, by ρ_1 > 0, and not in g_k + 𝒦, by the (E) witness.
- 𝒦 + 𝒦 ⊆ 𝒦 and 𝒦 + (g_k + 𝒦) ⊆ g_k + 𝒦.
- (g_k + 𝒦) + (g_l + 𝒦) misses 𝒞 by (P), since τ ≤ 1 and φ ≥ 0.
- N17.1(a) then gives a preorder with strict (G) and (IB). Worlds 2 and 3 are strictly guiding additive rankings.

**Competitiveness, for every model X (not only regular ones).**
- q_1 = 0: (2,3)-Bayes optimality.
- q = e_1: E_1P_1 = ∅.
- q_1 > 0: otherwise the vector is forced in K2.5's sense, which allows any X, and hence lies in 𝒦. This is why K2.5 defines forced vectors for all X. Correct.
- ρ_1 ∈ Ψ endorses every forced vector by Bayes optimality, so C ≠ ∅.

**Undominatedness and (C).**
- Weak dominance at worlds 2 and 3 plus Bayes optimality give ∫wρ_1 ≤ 0, with equality only for a second q-minimiser. Null ties make that Y = B_q.
- ∫wρ̃_j = ψ_j(Y) − ψ_j(B_q) ≤ 0, and c_0 > 0, so ∫wφ_c < 0 for every φ_c ∈ Ψ. Hence w ∉ 𝒦, and w ∉ g_k + 𝒦 at the (E) witness.
- Edge and vertex indices are handled: at a world-1 edge, q_3 = 0 and the ψ_3 term is still ≤ 0 by assumption.
- Theorem kkm then gives U_L = {B_q} = C_L. So (LA) and (C) hold.

**Closed sections.**
- B_q is continuous in measure because ties are null for every q and μ is finite.
- Each {q : v_q − g ∈ 𝒦} is an intersection of closed half-sets, and there are finitely many g_k. So the world-1 sections are closed for every X ∈ M_U. Worlds 2 and 3 have closed sections by continuity of ψ_j(B_q).

**(M1).** g_k ∈ 𝒜_1 because 0 ∈ 𝒦. B_{q_k} ∈ C_L and X_k is regular, so the comparison is relevant. (Cert) completes the certificate.

**The Remark on interior indices is correct:** ∫tφ_c = c_0Δ_1 + c_1|Δ_2| + c_2|Δ_3| > 0.

**Addition (PROVED, referee). The design choice "forced ⊆ 𝒦" is not a restriction for small trades.**
- Let φ_k be the (E) witness for g_k, with γ_k := ∫g_kφ_k > 0.
- Let t be any forced vector with ∫_{t⁺}φ_k < γ_k for all k. Then t ∉ g_k + 𝒦, since membership would give ∫tφ_k ≥ γ_k.
- So if t ∈ 𝒜_1, then t ∈ 𝒦.
- K2.6's trades can be taken this small, by absolute continuity of each φ_k. So K2.6 also covers the relaxed template in which forced vectors are only required to lie in 𝒜_1.

## 6. K2.6 and K2.6a: the edge obstruction. CORRECT; a strengthening is available

### 6.1 Verification

- At q = (q_1, q_2, 0) with q_1/q_2 = θ: E_1(B_q) ∩ R_12 = {r_2 > θ}, and B_q is correct on Q_3 and N₊.
- The trade X = B_q △ (B ∪ B′) has ψ_2(X) − ψ_2(B_q) = ρ_2μ(B) − ρ_2μ(B′) < 0. So t = 1_{B′} − 1_B is forced.
- On Q_1, φ_c/ρ_2 = c_0/r_2 + c_1 + c_2ρ_3/ρ_2. On Q_2 it is c_0/r_2 + c_1 − c_2ρ_3/ρ_2. Both signs of ρ̃ check.
- The SPREAD and ADJ estimates and the limits ε, η ↓ 0 are correct. The bound on B′ needs no sign condition, because ρ_2μ(B′) = (1+η)ρ_2μ(B) exactly.
- Edge (1,2) kills c_2 and edge (1,3) kills c_1. The final (E)/(Cert) clash is correct, because the g_k vanish on N₊ and Σλ_kg_k ≤ 0, ≠ 0 on M.

**K2.6a.**
- The map g ↦ (|g_2/g_1|, |g_3/g_2|) on (+,−,−) ∩ U has rank 2 (∂x/∂g_2 = −1/g_1, ∂y/∂g_3 = 1/g_2). So the images of open sets are open, and preimages of open subsets of the image are non-null. The rectangle argument is fine. (SPREAD₁₃) follows by exchanging 2 and 3.
- The domain is nonempty, since r_23 ∈ Q_1.

**Numerics.**
- k2py (B) reproduces.
- The table's claim "(1, 0.3, 0) killed by edge (1,3)" was **not tested** by K2's script, which treats edge (1,2) only. The referee's check (1) confirms it at θ = 1, band 0.05, with 126 × 124 pairs:
  - c = (1, 0.3, 0): +3.67 (violation);
  - c = (1, 0.05, 0): +0.59 (violation);
  - c = (1, 0, 0.3): −0.003 (endorsed at this edge).
- Script cosmetics: `worst` is initialised at 0, so "0.0000 (endorsed)" is uninformative. Initialise at −∞.

**Wording.**
- Outcome item 5 says "(SPREAD) or (ADJ); both hold for the Brier base, PROVED". Only SPREAD at both edges is proved.
- ADJ₁₂ also holds there numerically (check (2): at θ = 1 both sets are non-empty for a up to 10). Write "SPREAD at both edges holds for Brier (PROVED); ADJ holds numerically".

### 6.2 Strengthening (PROVED here, one reader): over the Brier base the linear ansatz is unnecessary

**Proposition R6.2.**
- *Setting.* The Brier base: ρ_l = |g_l|, U = D_{K′}, K′ = u + s(T1 − u).
- *Hypothesis.* φ ∈ L¹(U) with φ ≥ 0, and ∫tφ ≥ 0 for every two-set forced trade at the world-1 edges (1,2) and (1,3). The trades may be restricted to arbitrarily small mass.
- *Conclusion.* φ = cρ_1 a.e. on M for some c ≥ 0.

*Proof.*
1. **Edge inequality.** For each θ > 0, the K2.6 trade with arbitrary B ⊆ R_12 ∩ {r_2 > θ} and B′ ⊆ R_12 ∩ {r_2 ≤ θ} gives
   G⁺(θ) := ess sup_{R_12∩{r_2>θ}} φ/ρ_2 ≤ G⁻(θ) := ess inf_{R_12∩{r_2≤θ}} φ/ρ_2.
   - If this failed, pick α < α + γ with φ/ρ_2 > α + γ on a non-null part of the first set and < α on a non-null part of the second.
   - Take B, B′ there with ρ_2μ(B′) = (1+η)ρ_2μ(B) and (1+η)α < α + γ.
   - Then ∫_{B′}φ < ∫_Bφ, which is a violation.
2. **φ/ρ_2 is a function of r_2.**
   - H := G⁻ is nonincreasing.
   - For rational θ < θ′, φ/ρ_2 ∈ [H(θ′), H(θ)] a.e. on {θ < r_2 ≤ θ′}.
   - So φ/ρ_2 = H(r_2) a.e. on R_12, off r_2^{−1}(discontinuities of H). That set is null, because the level sets {|g_2| = x|g_1|} are null.
   - Likewise φ/ρ_3 = H_3(r_3) a.e. on R_13.
3. **Gluing on the link class.**
   - On Q_1 ∩ {g_1 < 0} = (−,+,+) ∩ U, put x = r_2 = g_2/|g_1| and y = r_3 = g_3/|g_1|.
   - Dividing ρ_2H(r_2) = ρ_3H_3(r_3) by |g_1| gives a(x) := xH(x) = b(y) := yH_3(y), a.e. for the law of (x,y).
   - That law is equivalent to Lebesgue measure on W := {(x,y) > 0 : (−1,x,y) ∈ U}. The radial integral of the Gaussian density is positive.
   - W is open and up-closed, since K′ ⊆ Δ° gives m_2, m_3 > 0. Its x- and y-projections are (0,∞).
   - So every section {y : (x,y) ∈ W} is a ray (h(x), ∞), and any two rays overlap. Fubini gives a ≡ c a.e. on (0,∞), and likewise b ≡ c.
   - Check (3) found 0 violations of up-closure and down-closure in 2·10⁵ samples.
4. **Conclusion.** H(x) = c/x, so φ = ρ_2c/r_2 = cρ_1 a.e. on R_12, and likewise on R_13. Since M = R_12 ∪ R_13, φ = cρ_1 on M. ∎

**Consequences.**
- **(i)** In K2.5, replace Ψ by any set of nonnegative integrable functions containing ρ_1. Equivalently, take 𝒦 to be any weak-* closed convex cone; by the bipolar theorem for the (L^∞, L¹) pairing it is such a dual. Then every φ ∈ Ψ is cρ_1 on M.
  - The g_k vanish on N₊, so (E) and (Cert) clash exactly as in K2.6.
  - By §5's addition, this holds even if forced vectors are only required to lie in 𝒜_1.
  - So over the Brier base the whole dual-cone decoration template is empty, not only its linear version, and no SPREAD/ADJ hypothesis is needed.
- **(ii)** This supplies missing piece (i) of the evidence for CONJECTURE K2.6′ in the Brier case. The weak-* closed convex cone generated by the edge-forced trades and the nonnegative vectors has dual {cρ_1 on M} ⊕ (≥ 0 on N₊). So its closure contains every ρ_1-strict improvement.
  - Piece (ii), passing from the closed convex hull to the acceptance set itself (a transfer chain in the manner of B1.2), remains open. 𝒜_1 is neither convex nor closed.
  - So K2.6′ for the Brier selection now hinges on exactly that step. This is the nearby, sharper open question I recommend in place of (Q-K2a).
- **(iii)** For general bases the same proof works under: null level sets of r_2 on R_12 and of r_3 on R_13, plus a "linked sections" condition on the law of (r_2, r_3) on Q_1 that reaches the full ranges of r_2 and r_3. This is an alternative to (SPREAD)/(ADJ) that needs no linear ansatz.

## 7. K2.7: edge sweep. CORRECT

- On R_ij, being correct at i means erring at j, so E_jC_{p_m} ⊇ A.
- X := P_j △ A′ has E_jX = A′ ⊊ A, so X ≺_j C_{p_m}. Competitiveness on {i, j} gives C_{p_m} ⪯_i X.
- The section {p : C_p ⪯_i X} is closed, so C_{e_j} ⪯_i X.
- C_{e_j} = P_j by strict (G) at j.
- E_iP_j = R_ij, so E_iX = R_ij ∖ A′ ⊊ E_iP_j, and X ≺_i P_j. Contradiction.
- Only strict (G) and (S) are used. "Any n" is right.
- The "Use" paragraph is heuristic except for the first sentence, which uses M = R_ij ∪ R_ik (n = 3).

## 8. Scope statements to correct

1. **§0, "single obstruction in words".** "Protection needs endorsers … that concentrate on the overlaps" and "What is left is ρ_i" describe the K2.5 template only.
   - With R6.2 this is proved over Brier for every dual-cone template.
   - It is not proved for world orders outside the template.
   - **Fix:** say "within dual-cone decorations of a Bayes base".
2. **§8, "What a T1 cover with an (M1) world must therefore do".** "Its selection is non-Bayes for every additive field on an open set of indices, and its rigid comparisons are protected by endorsers of a forced cone that is not a half-plane family" is **not proved**.
   - Nothing in K2 excludes a non-template world order over a Bayes selection. That is exactly CONJECTURE K2.6′.
   - "On an open set of indices" is not derived anywhere.
   - **Fix:** label it CONJECTURE (conditional on K2.6′), or restrict it to K2.5-type decorations.
3. **§8, second bullet.** "The crossing bases a certificate needs are available, through the frontier family" holds only when r interleaves (§4 above).
4. **Status table, Task (3).** "K2.5 decorations over generic additive Bayes bases" should say "with linear endorsers; with arbitrary L¹ endorsers over the Brier base (R6.2)".

## 9. Assessment

K2 delivers what it claims as theorems:
- **K2.1–K2.2:** a genuine class closure for any n: certificates made only of forced comparisons are impossible.
- **K2.3:** a clean reduction of the two-world route to refuting Q2N in its hardest class.
- **K2.4:** the frontier family, crossing under interleaving.
- **K2.5:** a correct sufficient construction scheme that verifies every axiom.
- **K2.6:** a correct proof that the scheme is empty over generic bases.

There is no false step. The overstatements are in the interpretive paragraphs (§0 obstruction-in-words, §8) and in two readings of K2.4.

**Recommended nearby target (in the spirit of the brief).** Prove the closure-to-acceptance step for the Brier-Bayes selection, i.e. K2.6′ for Brier. By R6.2 the endorser side is settled there.
- **If the step goes through:** a Bayes-shaped selection over Brier-additive worlds 2 and 3 forces world 1 to add up. That closes the frontier-crossing part of BRIEF16 class (i) for that base.
- **If it fails:** the failure must sit in the non-convexity of 𝒜_1, i.e. in pairwise sums leaving 𝒞. That is precisely where a non-decorative (M1) world would have to live.

## Files

- `k2ref_py/k2ref_checks.py` (+ `.out`), run with `python3 -I`:
  - (1) edge (1,3) kills c_1 (confirms the untested table entry);
  - (2) ADJ₁₂ on the Brier base;
  - (3) up/down-closure of the link-class regions used in R6.2;
  - (4) K2.4(e) gain-class check on random frontier families.
- `k2py/` reruns reproduce K2's outputs exactly.
