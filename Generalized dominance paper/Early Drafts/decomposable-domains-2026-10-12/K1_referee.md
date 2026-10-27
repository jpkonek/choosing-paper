# Referee report on K1_notes.md (per-world safe tests, countable ends, the question K1.Q)

15 Oct 2026, round 19. This is an adversarial reading against:
- BRIEF16;
- J1_notes and J1_referee (including Theorem R.2, Corollary R.3 and the residual (R-i)–(R-iii));
- H1_notes, H2_notes, H12_referee (Prop. R.1), E1_notes;
- write-up "The Contamination Triangle.tex": §§2–3, §7.7 (Theorem kkm, Theorem M0closed), and §8.5 parts (f′) and (g).

Labels are as in BRIEF13. One scratch script is in `k1ref_py/`: `countable_conflict.py` and its `.out`, run with
`python3 -I`. It checks the set configuration of §5.2 at CHECKED level, and no verdict rests on it. No assumption is
added. Notation is K1's: (EP∞), ψ, T, m_t, d_t, Π^k(a), D(a), A^a_k, Ξ^s, (Al∞).

## 0. Verdicts

| Item | Verdict |
|---|---|
| The class (EP∞) | **CORRECT.** One sentence has a wording GAP: the purely finitely additive case (§1.1) |
| (F1) admissibility, (F2) the gap m_t = T(B_t) + d_t, (F3) refinement | **CORRECT** |
| K1.0, K1.0′ (safe closure) | **CORRECT** |
| K1.1 (shadowing, countable families) | **CORRECT**, re-derived step by step. This is a genuine extension of H2.1(b) to countable families in the integrable case |
| K1.1′ (diagonal measure argument in place of the pigeonhole) | **CORRECT**. It also absorbs the arrow-depth adjustment of H12_referee §2.4 |
| K1.2 (per-world safe tests) | **CORRECT**: every comparison is base, hence endorsed, and T(C) ≥ m_t for every coherent C. The tool is modest (§2.2), and §0 misattributes K1.4 and K1.5 to it |
| Canonical triple A^a; "k-worst" | **CORRECT** |
| K1.3 (KKM form) | **CORRECT**. "At some depth instead of every depth" is not a gain; the gain is countable families (§3) |
| K1.4 (acyclic Γ, countable families) | **CORRECT** |
| K1.5 (aligned orders, (Al∞)) | **CORRECT** |
| K1.5 "Sufficient condition" and "J1.3(a), (b) follow … end by end" | **GAP (fixable).** The clause "meets the earlier deep ends only in a null set at some depth (end by end)" is **false** if read pairwise (counterexample configuration, §5.2). It is correct with a uniform reading. J1.3(b) inherits the gap. J1.3(a) and (c) are fine. R.2/R.3 of J1_referee are not extended, and their case 4 needs the same uniform reading |
| K1.6(a), (c) (KKM, anti-safe points) | **CORRECT** |
| K1.6(b) 1–4 (shape of anti-safe points) | **CORRECT** |
| K1.6 "cover in (EP∞) ⟺ K1.Q yes" | **CORRECT but tautological.** ⇐ holds by definition, and the anti-safe clause of K1.Q is implied by membership in the class through (a). K1.Q *is* the class question. The §0 claim that this is "the third option of the brief" and "isolates the one property a cover must have" is **WRONG** as a description of what is achieved (§6) |
| §0/§5/§6.1: conflicts "persist at every depth only when … as an arrow of Γ does" | **WRONG for countable families.** An arrow implies a persistent conflict, but not conversely (§5.2) |
| §0 relation (a): "doubly misaligned cycles are exactly the configurations in which no order is aligned" | **GAP (overstated).** This holds only for a 2-cycle whose third world is isolated in Γ (J1_referee §4.3, R.3(c)). It is false as a description of 3-cycles and larger Γ (J1_referee (R-ii), (R-iii)) |
| §6, the four failed repairs | 1, 2, 3: **CORRECT** as descriptions. 2's displayed facts are proved. 3 cites K1.2 where H1.0(c) is meant (harmless). 4 is a heuristic with no statement and should be labelled or cut |
| References to "the brief's (a)–(c)" | BRIEF16 has no (a)–(c); its untouched cases are (i)–(iv). (c) ↔ (iii). Fix the citation |

**Net.**
- Nothing in the mathematics of K1.0–K1.6 is wrong.
- The real advance is K1.1/K1.1′ and through them K1.4 and K1.5. These close two whole subclasses of (EP∞):
  - acyclic Γ;
  - an aligned order in the (Al∞) sense.

  This answers BRIEF16 untouched case (iii) except along cyclic, non-aligned configurations.
- The headline deliverable, K1.Q, is the class question restated, so it is not a reduction.
- One structural sentence (persistent conflict ⇒ arrow) and one sufficient condition fail with countably many ends.

---

## 1. The class and the standing facts

### 1.1 (EP∞): CORRECT, with a wording GAP

**The definition is (EP) of the write-up with "finite" replaced by "countable".**
- An empty family makes end-protection vacuous and every relevant comparison base.
- H2.0 refines countable families and preserves both end-protection and the base comparisons. So the refined class is
  the same class.

**"Adds up with a countably additive weight ⇒ in the class with 𝒮_k = ∅": correct.**
- The weight is bounded and vanishes on null sets.
- Radon–Nikodym gives ρ_k ∈ L¹.
- Positivity on non-null sets gives ρ_k > 0 a.e.

**The wording GAP.** "A world that adds up only through a purely finitely additive weight has no integrable endorser
and is not in the class" is too strong.
- Such a world has no integrable endorser of *all* relevant comparisons. So it is not in the class *with
  𝒮_k = ∅*.
- It may still be in the class through a nonempty family of ends together with an integrable *base* endorser.
- **Fix:** "is not in the class with 𝒮_k = ∅; whether it is in the class through ends is not decided here".

### 1.2 (F1)–(F3): CORRECT

**(F1).**
- Summable depths exist: take a_S(m) with μ(S_{a_S(m)}) ≤ 2^{−r(S)−m}, increasing in m.
- D_m ⊆ M decreases and μ(D_m) → 0.
- T1 ⪯_k Y with Y = T1 on D_m is relevant, and it vanishes on S_{a_S(m)} for each S ∈ 𝒮_k, so it is base.
- H1.1 then applies (re-checked against H12_referee §1.3, which records that countably many ends suffice).
- I_ψ is non-null by M0closed(a). Integrability is not needed there (H12_referee §1.4).

**(F2).**
- B_t ⊇ N₊ a.e., so B_t is regular. H1.0(b) with Y′ = B_t gives T(Y) − T(B_t) = Φ_t(Y) for regular Y with finite
  costs.
- Coherent models are regular.
- H1.0(a) gives the attained d_t > 0.
- Hence T(C) ≥ m_t = T(B_t) + d_t for every coherent C.

**(F3)** is H2.0.

## 2. K1.0 and K1.2 (per-world safe tests)

### 2.1 K1.0, K1.0′, K1.2: CORRECT

**K1.0.**
- C ∈ C_L and A regular, so the comparison is relevant.
- δ ≤ 0 on S_{a_S} excludes S-positivity for every S.
- End-protection gives δ ≥ 0 on S_{b_S}, so δ = 0 on S_{max(a_S, b_S)}.
- "Base" is end by end, so no maximum over the family is needed.

**K1.0′.** δ(g) = 0 iff C and X give the same advice: on U the advice is determined by membership.

**K1.2, the question posed by the editor.**
- Each C ⪯_k A_k is relevant and, by K1.0, base. (b) gives ψ_k(C) ≤ ψ_k(A_k), all finite.
- Summing with weights t_k: T(C) ≤ Σ_k t_kψ_k(A_k) < m_t.
- C ∈ C_L is coherent, so T(C) ≥ m_t by (F2).

**The contradiction is genuine.**

**The cost bound is checked.**
- m_t is the minimum of T over the *coherent* models of M_U, and selected models are coherent.
- No regularity of the A_k beyond what K1.0 needs is used.
- The A_k need not be close to B_t or to each other.

### 2.2 Remarks on the tool (not errors)

- **Admissibility is a weak constraint.** The ideal triple (P_1, P_2, P_3), with P_k = U ∩ {h_k > 0}, is regular,
  k-safe and has T = 0 < m_t, so it is always admissible. For it, every p with |supp p| ≥ 2 and C_p ∉ {P_k} is
  anti-safe, by strict (G).
  - The binding constraint in K1.2 is C ⪯_k A_k, not the cost bound.
  - The useful triples are the *worst* admissible ones, which is why the canonical A^a_k (k-worst at depths a) is
    the right choice.
  - K1.Q quantifies over all admissible triples, including trivial ones (see §6).
- **Scope of the new tool.** K1.2 is H1.0(c) summed over different models. In the note it is used only in K1.3 and
  K1.6.
  - K1.4 and K1.5 do not use it: they use the near-Bayes models of J1 together with K1.0′ and K1.1′.
  - §0's heading "What the tool settles (PROVED)" over K1.3–K1.5 therefore misattributes K1.4 and K1.5.
  - **Fix:** attribute K1.4 and K1.5 to K1.1/K1.1′ with K1.0′.

## 3. Canonical triple and K1.3: CORRECT

**A^a_k.**
- It is regular: D(a) ⊆ M.
- It is k-safe: it is correct on Π^k(a) ⊇ S_{a_S}.
- ψ_k(A^a_k) ≤ ψ_k(B_t) + ρ_k(D(a)), so T(A^a) ≤ T(B_t) + ∫_{D(a)}Σρ.
- **"k-worst":** a k-safe Y at depths a that equals B_t off D(a) is at least as good as A^a_k at world k at every g
  (both correct on Π^k(a), A^a_k wrong on D(a) ∖ Π^k(a), equal elsewhere). So Y ⪯_k A^a_k by (G).

**K1.3, first part.** kkm gives C_p ⪯_k X ⪯_k A_k. Then apply K1.2.

**K1.3, second part.**
- Correctness at several worlds is consistent off the pairwise R_ij-overlaps, and a triple overlap is impossible on
  M.
- X ⪯_k A^a_k by (G).
- One small precision: admissibility of a depends on (ρ, t). The hypothesis should be stated as "conflict-free at
  some assignment a₀". Conflict-freeness is monotone, so a ≥ a₀ can then be taken admissible.

**What is and is not a gain.**
- "At some depth in place of every depth" (comparison with H1.3, second version) is **not a gain**. The condition is
  monotone in the depth, and H1.3's localizing families may be re-indexed to start at m₀.
- The gain is countable families, through K1.0.

## 4. K1.1, K1.1′, K1.4, K1.5

### 4.1 K1.1: CORRECT (re-derived)

**Reduction to larger assignments.** It is legitimate: a larger assignment gives a smaller right-hand side.

**Step 1.** For m ≥ n_W, T1 is i-wrong on W_m. Since σ_j ≠ σ_i on O, it is j-right there, so W_m misses
E_j(T1) ⊇ E_{M_E} (M_E ≥ n_E).

**Step 2.** Σ_E μ(E_{M_E}) ≤ Σ_E μ(E_{N_E}) < μ(R⁰_i)/2, so R is non-null.

**Step 3.**
- p_{m′} ⊆ W_{m′} (m′ ≥ n_W) with small ρ_j-mass exists, by integrability and non-atomicity.
- p ∩ R is null. If O is R⁰_i's orthant, T1 rejects on W (it is i-wrong there) and accepts on R ⊆ D_{T1}.

**Step 4.**
- **A(W).** X is strictly better at A(W)-worlds: on p it gives the advice that is right at i, hence right at j; on
  R, toggling is good at every world ≠ i.
- **World i.** δ_i = 1_R − 1_p is −1 at every depth of W. It is positive at no i-end, because R misses each
  E_{M_E}, including W_{N_W}.
- **Competitiveness.** T1 is competitive on {1,2,3}, via kkm: tied with C_q, which is competitive on supp q.

**Step 5.**
- δ_j = 1_p − 1_R vanishes at depth M_E on every end of j.
  - The T1-correct ends of j all lie in 𝒯, and p avoids them by construction.
  - The T1-wrong ends are avoided by step 1.
  - R avoids all ends.
- So the comparison is base, and ρ_j(R) ≤ ρ_j(p) contradicts the choice of p.

**Assessment.** This is H2.1(b) with the finite covering replaced by an arbitrary assignment, in the integrable
case. Nothing is missing.

### 4.2 K1.1′: CORRECT

**The two cases.**
- If m_k ≤ m′, then P ∩ W_{m′} ∩ S^k_{M_k} ⊆ P ∩ W_{m_k} ∩ S^k_{n_k}, which is null.
- If m_k > m′, then W_{m_k} ⊆ W_{m′}. The measure bound gives μ(P ∩ W_{m′}) ≤ ½ μ(P ∩ W_{m′}).

**The rest.**
- The empty-𝒯 case contradicts non-nullity of W_{m′}.
- The remark "μ(W_m ∩ S_n) > 0 for all m, n ⟺ for all m = n" is correct.
- So this is a clean replacement of the pigeonhole of H2.3 Step 4 and J1.1, including the depth adjustment of
  H12_referee §2.4.

### 4.3 K1.4: CORRECT

**Step 1.** a_S ≥ n_S makes X = T1 l-correct on T1-correct S_{a_S}.

**Step 2, the dichotomy.**
- "Not eventually ≥ 0 on some end": end-protection then gives positivity at some end.
- "Eventually ≥ 0 on all ends, not eventually 0 on E": then δ is E-positive, since the S_n decrease.
- By step 1, the positive end is T1-wrong.
- On P, C ≠ X whether X equals T1 or B_t there. Only "different advice" is used.

**Step 3.**
- K1.1′ applies to P ⊆ W_{n_W}, which meets every W_m.
- On P ∩ S_n with n ≥ a_S, X = T1 is l-correct and C differs, so δ_l = −1 at every depth.
- The arrow condition comes out of K1.1′ directly.

**Step 4.** The walk follows arrows of Γ, and an infinite walk on three vertices contains a directed cycle.

**Conclusion.** Acyclic Γ makes all three comparisons base. Φ_t(X) ≤ ∫_{D(a)}Σρ < d_t, so H1.0(c) is
contradicted.

**The heaviness-free, countable form of Prop. R.1 / J1.1 is therefore proved.**

### 4.4 K1.5 and (Al∞): CORRECT

**Quantifier order.** t, then a (aligned: a ≥ a₀ with ∫_{D(a)}Σρ < d_t), then X^a, then C, then M = m′(C), then J
from (Al∞). This is legitimate because (Al∞) holds for *every* M.

**Step 2.** If X is k₂-wrong at g ∈ S′_{J_{S′}} ⊆ Π^{k₂}(a), then r(g) = 1 with sign conflict. So g ∈ Ξ², hence
g ∈ ⋃ S_{m′_S}, where C = X.

**Step 3** is the same.

**No purity is needed.**

**Relation to J1's (Al).**
- For finite families, (Al∞) with uniform a is J1's (Al).
- Non-uniform a makes "aligned" weaker, so K1.5 is a mild strengthening even for finite families.

## 5. Where K1 fails with countably many ends

### 5.1 The sufficient condition after K1.5: GAP (fixable)

**What is fine.**
- **T1-wrong S′ with V(S′) earlier.** K1.1 gives, for every M, a depth j with
  S′_j ⊆ ⋃_{q<s}⋃ S_{M_S}. So J_{S′} := max(j, a_{S′}) works. ✓.
- **Purity-forced disjointness.** Both ends T1-correct, or both T1-wrong, at worlds of opposite sign on the common
  orthant: beyond the purity depths S_{n_S} ∩ S′_{n_{S′}} is null. This is built into every a ≥ n and J ≥ n,
  per end. ✓.

  So J1.3(a), and case 1 of J1_referee's R.2, extend.
- **J1.3(c) "with assignments in place of depths".** Correct when its hypothesis is read as: for every assignment a
  on i's ends and every M there is J with S′_J ∩ ⋃_W W_{a_W} ⊆ ⋃ S_{M_S}.

**What fails.** "or meets the earlier deep ends only in a null set at some depth (end by end), the order is aligned"
is **false** if read pairwise. That reading is "each pair (S, S′) is eventually disjoint", with geometric rather than
purity-forced disjointness. Pairwise disjointness needs *both* a_S and J_{S′} beyond the pair's depth. With
infinitely many later ends this can force a_S = ∞.

**Fix (PROVED; immediate from the K1.5 proof).** Read the clause uniformly:
> there is an assignment a₁ such that every later S′ on a conflicting orthant has a depth j(S′) with
> μ(S′_{j(S′)} ∩ ⋃_{q<s} Π^{k_q}(a₁)) = 0.

Then every a ≥ max(a₀, a₁) satisfies (Al∞) for these S′, with J_{S′} := max(j(S′), a_{S′}).

**Knock-on effects.**
- J1.3(b) in countable form needs this reading for its disjoint pairs.
- J1_referee's R.2, case 4, uses a uniform d₀ over the k₃-ends that do not meet S′ at every depth. It extends under
  the same reading, and only under it.
- K1 should say that R.2/R.3 are not extended as stated.

### 5.2 Persistent conflict without an arrow: the §0/§5/§6.1 sentence is WRONG for countable families

**What is claimed.** K1 states that conflicts "persist at every depth only when the deep ends of two worlds overlap
on R_ij at every depth, as an arrow of Γ does".

**What is true.** The direction arrow ⇒ persistent conflict holds: μ(W_m ∩ S_m) > 0 for all m, with W ⊆ O where
σ_i ≠ σ_l. The converse fails.

**Configuration (CHECKED; sets only, no ranking).**
- *Setting.* In a conflicting orthant, world 1 has one T1-wrong end W: cones over caps of radius θ_m = 0.2·2^{−m}
  around a ray r. World 2 has T1-correct ends S′_l: cones over caps of radius 0.01·2^{−l−n} around rays r′_l at
  angle 0.15·2^{−l} from r.
- *Pairwise.* Every pair (W, S′_l) is eventually disjoint, at depth l + 1. So there is no arrow between W and any
  S′_l.
- *But.* For every depth a of W and every M > a, the end S′_a lies, at every depth, inside the shell
  W_a ∖ W_M. So:
  - Π¹(a) ∩ Π²(a′) ∩ R_12 is non-null for every pair of assignments;
  - (Al∞) fails for any order placing world 1 before world 2, unless other earlier ends cover the shells.
- `k1ref_py/countable_conflict.py` checks the angle inequalities over a grid (0 failures) and the non-nullity by
  Monte Carlo.
- For the record, K1.1 forces W to be shadowed by some world of V(W). In this picture that must be world 3, which
  is consistent on (+,−,−).

**Consequences.**
- For countable families, K1.3 (conflict-free at some depth) and K1.4 (acyclic Γ) are logically independent
  exclusions.
- K1.6(b)3's conflicting pair does not yield an arrow.
- The sentence should read: "an arrow forces a persistent conflict; with countably many ends a persistent conflict
  can also come from infinitely many pairwise eventually disjoint ends".

### 5.3 Relation (a) of §0: GAP (overstated)

**What is claimed.** "Doubly misaligned cycles are exactly the configurations in which no order is aligned."

**What holds.** This is true for a 2-cycle whose third world is isolated in Γ (J1_referee §4.3 and R.3(c)).

**What does not.**
- For a pure 3-cycle, "no aligned order" is triple misalignment relative to Π^a ∪ Π^c (R.3(b)).
- For Γ with ≥ 3 arrows that is not a pure 3-cycle, it is (R-iii).

**Fix.** Cite J1_referee §8.4 and restrict the sentence to (R-i).

## 6. K1.6 and K1.Q

### 6.1 (a), (c): CORRECT

- F_k = {p : C_p ⪯_k A_k} is closed by (S), since A_k ∈ M_U is a fixed model.
- "No anti-safe point" gives Δ_S ⊆ ⋃_{k∈S} F_k for every face.
- The KKM lemma gives p* ∈ ⋂F_k. C_{p*} ∈ C_L, and K1.2 gives the contradiction.
- (c) is the contrapositive. **It is the useful, testable direction:** one triple without anti-safe points excludes
  the ranking.

### 6.2 (b) 1–4: CORRECT

**(b)1.** C_{e_k} ⪯_k A^a_k by competitiveness on {k}.

**(b)2.** A model X that is k-correct on Π^k(a) satisfies X ⪯_k A^a_k by (G). Transitivity would then make k
non-anti-safe.

**(b)3.** Otherwise the K1.3 model built from supp p is correct on every Π^k(a) with k ∈ supp p, against (b)2.

**(b)4.**
- An i-safe Y at depths a (equal to B_t off D(a)) satisfies Y ⪯_i A^a_i, so C_p ⋠_i Y.
- Competitiveness on {i, j} then gives C_p ⪯_j Y. The mirror statement is the same.

**Consistency.** These constraints are not contradictory in themselves.
- Let Y be i-safe and let Y′ be Y made j-correct on Π^j(a). Then Y′ is j-safe and Y′ ⪯_j Y by (G).
- C_p ⪯_j Y and C_p ⋠_j Y′ only place C_p strictly between Y′ and Y at world j.

**So (b) is a correct description of what a cover must do at the selection.**

### 6.3 The equivalence: CORRECT but tautological; the framing is WRONG

**The direction "K1.Q yes ⇒ cover".**
- A positive answer to K1.Q *is*, by its first clause, a ranking on M_U with (H_U) in (EP∞).
- (H_U) contains T1 ∈ C_L, and (LF) is automatic on M_U. So this is a cover in the class by definition.
- The anti-safe clause plays no role.

**The direction "cover ⇒ K1.Q yes".** This is (a). It shows that the anti-safe clause is *implied* by membership.

**Hence:**

  K1.Q ⟺ "is there a ranking with (H_U) in (EP∞)?"

verbatim. The "iff" is proved, but it has no content beyond (a).

**Why the framing is wrong.**
- K1.Q does not:
  - reduce the class question;
  - separate the selection from the ranking (the selection's closed sections, competitiveness and C_L are those of
    the full ranking);
  - remove any axiom.
- The §0 claims "the deliverable is the third option of the brief: one precise question … equivalent" and "K1.Q
  isolates the one property a cover must have" are therefore **WRONG** as descriptions.
- K1.6 gives a *necessary condition* and an *exclusion test*, both proved.
- BRIEF16's directive ("a precise single open question that would settle the matter") is met only formally. Any
  restatement of the class question settles the class question.

**Nearby statements that are available (to replace K1.Q).**
1. **Necessary condition K1.N (PROVED; this is K1.6(a), (b)).** In any cover in (EP∞), for every ρ, every t ∈ I_ψ
   and every admissible a, the canonical triple A^a has an anti-safe index p. Every such p:
   - has |supp p| ≥ 2;
   - has two worlds of supp p in persistent conflict at a;
   - if supp p = {i, j}, has C_p strictly between the i-safe and the j-safe models at worlds j and i, as in
     (b)4.

   **Exclusion test K1.6(c):** one non-anti-safe triple excludes the ranking.
2. **The honest residual (open).** By K1.4 and K1.5, the remaining part of (EP∞) is the configurations in which Γ
   has a directed cycle and no order of the worlds is aligned in the (Al∞) sense. The single open question is the
   countable form of J1_referee's J1.Q′:

   > **J1.Q′∞.** Under (EP∞), if Γ has a directed cycle and no order satisfies (Al∞), is (H_U) contradictory?

   This is a strict sub-question of the class question, because K1.4 and K1.5 are proved. It is the right
   statement of what is open.
3. **A selection-level test that would be a genuine reduction (not proved, not conjectured).** Use the 2-cycle with
   an isolated third world and the cap-in-tube template J1.4. Ask whether any *two-world* order on R_ij, with closed
   sections in p and competitiveness on the edge, can realise (b)4 at every large a for edge indices.
   - If none can, every anti-safe index must be interior (|supp p| = 3).
   - That is a statement one can try to refute with (b)2 at all three worlds.

   K1 should state explicitly that this is untested. It is not equivalent to the class question.

## 7. §6 of K1, the failed repairs

1. **Covering through one model.** CORRECT as a description. "Non-null at every depth whenever Γ has an arrow" is
   right in that direction (§5.2). "Only through a single model" is heuristic.
2. **Monotone iteration.** The displayed facts are proved:
   - X_r ⪯_i X_∞ and X_r ⪯_j X_s (r ≥ s) by (G);
   - C_{p*} ⪯_i X_∞ and, with σ_l = σ_i, C_{p*} ⪯_l X_∞, both by closed sections along C_{p_r} ⪯ X_r;
   - C_{p*} ⪯_j X_s for each s.

   The diagnosis is correct: (S) gives closedness in p for a *fixed* model, never continuity in the model, so
   C_{p*} ⪯_j X_∞ is not available.
3. **Fixed point.** The (IB) reformulation is correct. One precision: with A_k := [C_p on D, B_t off D], the
   contradiction comes from H1.0(c), because δ = 0 on D makes every comparison base. It does not come from K1.2,
   since this A_k need not be k-safe. The obstruction (a moving second argument, so closed sections do not apply) is
   correct.
4. **Counting.** No statement is made, and "each anti-safe comparison that is base costs a fixed ρ-mass" is not
   meaningful as written: anti-safe means *non*-comparisons. Label it as a heuristic or delete it.

## 8. Requested changes

1. §0 and §5: replace "the deliverable is … one precise question … equivalent" by K1.N + K1.6(c) (necessary
   condition, exclusion test) and J1.Q′∞ (the honest residual) (§6.3). Keep the equivalence sentence only with the
   remark that it is tautological.
2. §0 "What the tool settles": attribute K1.4 and K1.5 to K1.1/K1.1′ and K1.0′, not to K1.2 (§2.2).
3. Persistent conflict: replace "only when … as an arrow of Γ does" (§0, §5, §6.1) by "an arrow forces it; with
   countably many ends it can arise without an arrow" (§5.2).
4. Sufficient condition after K1.5, and "J1.3(b) follows": use the uniform reading (assignment a₁) (§5.1). State
   that J1_referee's R.2/R.3 are not yet extended, and that case 4 needs the same reading.
5. §0 relation (a): restrict it to a 2-cycle with an isolated third world; cite J1_referee §8.4 for 3-cycles and
   (R-iii) (§5.3).
6. (EP∞) paragraph: fix the purely-finitely-additive sentence (§1.1).
7. K1.3: state the second hypothesis at an assignment a₀ and enlarge it. Delete "at some depth instead of every
   depth" as a claimed gain (§3).
8. §6.3 (fixed point): cite H1.0(c) instead of K1.2. §6.4: label it as a heuristic or delete it.
9. Replace "brief's (a)–(c)" by BRIEF16's (i)–(iv). K1.4 and K1.5 answer (iii) outside cyclic non-aligned
   configurations.

## 9. For the write-up

- K1.0, K1.0′, K1.1, K1.1′, K1.2, K1.3, K1.4, K1.5 (with (Al∞)) and K1.6(a)–(c) may enter §8.5 as "proved in a note,
  refereed once".
- The "countably many ends" item of part (g), "Outside class (EP)", should be narrowed:
  - (EP∞) with acyclic Γ is excluded;
  - (EP∞) with an (Al∞)-aligned order is excluded;
  - what remains inside (EP∞) is J1.Q′∞.
- Part (f′)'s case (B) sentence "with countably many ends an arrow of Γ is not excluded" should become "with
  countably many ends, only cyclic non-aligned configurations remain (K1.4, K1.5)".

## 10. Files

- `k1ref_py/countable_conflict.py` (+ `.out`): the configuration of §5.2. It checks:
  - pairwise eventual disjointness;
  - shell-hitting for every tested (a, M, J): 0 cases without a hit;
  - non-nullity of the cap inside the shell by Monte Carlo (fraction 1.0).
