# REF66_un: referee report on "Universal coverage of coherent sets of desirable gambles (draft)" (26 Oct 2026)

Labels: PROVED (argument checked, or supplied here) / CHECKED (exact computation) / CONJECTURE (none used).
The verdicts below rest on my own reading of the note's proofs. SR66, REF65_hA and REF65_un were used only for comparison.
Scripts are in `ref66un_py/`. Both scripts end in ALL PASS.
- `ex71_exact.py` → `ex71_exact.out`: Example 7.1, exact (sympy).
- `prop36_check.py` → `prop36_check.out`: Proposition 3.6, Corollary 3.7, the §7.3 variant and the §6 record-free remark, on exact two-world cone models. `cone2d.py` is a verbatim copy of SR66's exact interval library. Safety is tested from the definition, by brute force over coherent models, not by the hull test.
- `build/`: my own three-pass compile of the note.
- `kcm/`: a compile of the covering paper, used to check the cited numbers.

## 0. Headline

**The mathematics of the note is correct.** I re-proved the following myself and found no error in any of them:
- every clause of Propositions 3.5–3.6, Corollary 3.7 and Theorem 5.1;
- the safety lemmas;
- the contraction lemma, Proposition 4.2 and Theorem 4.3;
- Proposition 5.5;
- the abstract Lemma 6.1 with its verification for the gamble ranking;
- Example 7.1.

There are two defects, both confined to remarks:
- **One ERROR.** The paragraph after the proof of Lemma 6.1 describes a "record-free" construction as written. That relation is *transitive*, so it satisfies (Add). What it loses is (G) and (IB), not (IB) and (Add).
- **One GAP.** §7.3 asserts without proof that "the proofs go through" for a lexicographic variant. The claims are true, and §5 below supplies the proof. One clause of Proposition 3.5(b) does *not* transfer, and the remark should say so.

Everything else is minor: scope wording, notation and precision.

## 1. Verdict table

| # | Item | Verdict | Repair (if any) |
|---|---|---|---|
| 1 | Def 3.3 (safe-improvement ranking); Lemmas 3.1, 3.2, 3.4 | CORRECT | — |
| 2a | Prop 3.5(a): reflexivity, a.e. ties, (IB) | CORRECT | — |
| 2b | Prop 3.5(b): strict Brier increase; no nontrivial ties; sub-relation of Brier (strict part too) | CORRECT | — |
| 2c | Prop 3.5(c): strict (G) | CORRECT | — |
| 2d | Prop 3.5(d): (FCC), (TC), all cycles trivial | CORRECT | — |
| 2e | Prop 3.5(e): (Add), including the mixed guidance/safe case | CORRECT | — |
| 2f | Cor 3.7: protection (no weak dominator other than itself) | CORRECT | — |
| 2g | Thm 5.1(c): strict dominance of every incoherent model, with the geometric properties | CORRECT | — |
| 2h | Thm 5.1(b),(d): 𝒰 = 𝒞* = 𝒞_U, (GC), (ID), (W), strong (C) | CORRECT | — |
| 2i | Thm 5.1(e): target undominated, (LF), covers K ⟺ K full-dimensional and K′ ⊆ relint K; Cor 5.3, Cor 5.4 | CORRECT | — |
| 3 | **Prop 3.6** (new): weak dominance by Y ≠ X ⟺ dominance ⟺ strict dominance ⟺ r(Y,X) safe and m(Y) − m(X) ≫ 0 | **CORRECT** (PROVED; CHECKED on 1 400 exact pairs, 798 positive) | — |
| 4a | §4 setup; equation (4.1) | CORRECT | — |
| 4b | Lemma 4.1 (contraction) | CORRECT | — |
| 4c | Prop 4.2 (hull(X∖N) = hull(X); safety of r(N,X)) | CORRECT | — |
| 4d | Thm 4.3: Step 1 (relative minimax), Step 2 (non-null gain and shrink), Step 3 | CORRECT | Minor: Remark 4.4(a) under-reports where K′ ≠ ∅ is used (R4) |
| 4e | Remark 4.4(b)–(d) | CORRECT | — |
| 5 | Prop 5.5 and the paragraph after it, against SR66 C1 (i)–(ii) | CORRECT; matches SR66 exactly. [KCM, Prop. 2.10] and [KCM, Cor. 5.9] checked against a fresh compile of the covering paper | — |
| 6a | Lemma 6.1: hypotheses (A1)–(A5) and conclusions (a)–(f) | CORRECT. All four of SR66's missing hypotheses are present or made unnecessary (§3) | — |
| 6b | Verification of (A1)–(A5) for the gamble ranking | CORRECT | Minor overclaim: "yields Theorem 5.1(a)–(d)" (R5) |
| 6c | Paragraph "The record layer is what gives the lemma content" | **ERROR** | R1 |
| 7 | Example 7.1: (Tr) fails at world 1 for every μ satisfying (M) | **CORRECT** (PROVED; CHECKED exactly) | — |
| 8 | §7.3 lexicographic remark | **GAP** (claims true, proof absent; one clause does not transfer) | R2: insert the proof in §5 below, or delete |
| 9 | §8 Scope | Factual. One inaccuracy: "All results concern finitely many worlds" is false of Lemma 6.1 (GAP, minor) | R3 |
| 10 | Conventions | CORRECT, with small exceptions | R6–R8 |

## 2. Section 3: the ranking, Proposition 3.5, Proposition 3.6 and Corollary 3.7

**Def 3.3 and its lemmas.**
- *Lemma 3.1(a).* Y := (Z∖B) ∪ A gives r(Y,Z) = (A,B) a.e., using A ∩ Z null, B ⊆ Z a.e. and A ∩ B = ∅.
- *Lemma 3.1(b).* The pointwise indicator identity holds off the null overlap.
- *Lemma 3.1(c).* (IB) reduces to equality of records.
- *Lemma 3.2(a).* ⇐: if A ∩ hull(B) is null, the record applies to hull(B) ∈ 𝒞_U, by Lemma 2.2(a),(b). ⇒: if it applies to D_Q, then hull(B) ⊆ D_Q, by Lemma 2.2(c).
- *Lemma 3.2(b).* B null gives Q_B = Δ vacuously and hull(B) = D_Δ = int ℝⁿ₊. That set is in 𝒞_U because K′ ⊆ Δ.
- *Lemma 3.2(c).* If r₁ ⊔ r₂ applies to Z, then r₁ applies to Z. This holds for *every* model Z, so no decomposability is needed.
- *Lemma 3.4(a).* m_i(r) = ∫_A |h_i| + ∫_B |h_i|, which is positive unless A ∪ B ⊆ {h_i = 0} a.e. That hyperplane is null.
- *Lemma 3.4(c).* B ⊆ {h ≪ 0} ∩ U = ∅, because k·h < 0 for k ∈ K′.
- G_i, safety and m_i are invariant under null modification, so Acc_i is a well-defined set of record classes. This is implicit in the note but immediate.

**Prop 3.5.** Each part checks:
- (b) is the potential argument: m_i(r(X,Y)) = m_i(X) − m_i(Y), and every accepted non-null record has m_i > 0.
- (d) follows from (b).
- (e) Case 1: both records are guidance, so the union is guidance. Case 2: one record is safe-accepted. Then the union is safe by Lemma 3.2(c), and the other record has m_i ≥ 0 by Lemma 3.4(b).

The components of r₁ ⊔ r₂ are disjoint up to the null overlap (A₁ ∩ B₂ and A₂ ∩ B₁ both lie in the overlap of supports). So r₁ ⊔ r₂ is a record class. In any case it equals r(X,Z) by Lemma 3.1(b).

**Prop 3.6** (new, and refereed only here). PROVED, as follows.
- (iii)⇒(ii)⇒(i) are immediate. Ω ≠ ∅, and a strict comparison at some world rules out a tie, hence a.e. equality.
- (i)⇒(iv):
  - r := r(Y,X) is non-null and accepted at every i, so m_i(Y) > m_i(X) for every i, by 3.5(b).
  - If r were unsafe, it would be guidance at every world, hence safe by Lemma 3.4(c), since it is non-null.
  - Uniform Brier dominance ⟺ m(Y) − m(X) ≫ 0 uses only finiteness of Ω and c_i < ∞.
- (iv)⇒(iii): a safe r with m_i(r) > 0 is accepted at every i. m(Y) ≠ m(X) forces Y ≠ X a.e., and 3.5(b) makes each comparison strict.

The load-bearing observation is Lemma 3.4(c): a non-null record that is guidance at *every* world is safe. That is exactly what makes weak dominance by a different model automatically strict.

CHECKED (`prop36_check.out`):
- 1 400 exact pairs on four domains, including K′ = [0, ½], which meets ∂Δ. In every pair the four conditions agree, and 798 pairs satisfy (iv).
- No nontrivial ties occur in 2 800 tests.

**Cor 3.7.** PROVED. It also follows in one line from Prop 3.6: a weak dominator Y ≠ C would make r(Y,C) safe, but r(Y,C) applies to C. The direct proof in the note is also correct.

The remark after it is accurate: only "every coherent model contains int ℝⁿ₊" and "no coherent model contains an h ≪ 0" are used, together with the fact that safety quantifies over the coherent models. CHECKED: 1 000 pairs (C, Y), half of them C modified by a change guided at one world.

## 3. Sections 4 and 5

**(4.1)** holds because the minimum over a Minkowski sum is the sum of the minima, and min_Δ q·h = min_i h_i.

**Lemma 4.1.** Correct.
- T(q′) ∈ Q_X because q′·x ≥ P(x) for q′ ∈ Q_X.
- T is a contraction with ratio c/(1+c) and fixed point q.
- Q_X is closed and nonempty (it contains K′).
- The case c = 0 is trivial.

**Prop 4.2.** Correct.
- Kept points x ∈ X ∩ N satisfy q·x ≥ min_i x_i > −cP(x), by (4.1).
- Removed points satisfy q·x ≥ 0 ≥ −cP(x) a.e., because P > 0 a.e. on X (Lemma 2.2(b)). This disposes of REF65_hA's d3 point.
- The second part is a two-line consequence of Lemma 3.2(a).

**Thm 4.3.**
- *Step 1.*
  - Lyapunov applies: the vector measure h dμ is finite by (M) and non-atomic.
  - "Since μ vanishes on points" is a valid reason for a finite Borel measure on ℝⁿ, but citing the non-atomicity already stated in §2.1 is cleaner.
  - Von Neumann/Sion applies to a continuous bilinear f on compact convex sets.
  - The case v ≤ 0 forces X to be the a.e.-unique maximiser G ∩ {λ*·h > 0}, which is coherent.
  - The saddle argument shows that z* maximises λ*·z, so z* = m(N₀) by uniqueness.
  - min_i (z*_i − x_i) = v, so z* − x ≥ v𝟙.
- *Step 2.*
  - Non-null gain via k ∈ K′.
  - N_τ = D_{conv(Q_X ∪ {λ*} ∪ Q_τ)} ∈ 𝒞_U.
  - 𝟙_{N_τ} → 𝟙_{N₀} pointwise, and dominated convergence applies.
  - The choice of τ preserves both the margin and μ(N∖X) > 0.
- *Step 3.* Follows from Proposition 4.2.
- *Remark 4.4(b).* The density-point argument is correct: density points of an open convex set are its points, because boundary points have upper density ≤ ½.
- *Remark 4.4(d).* Correct. Coherence of U is not actually needed there.

**Theorem 5.1.** All clauses are correct.
- (e): (i)–(iii) and (v) hold by (a) and (d).
- (iv) ⟺ K′ ⊆ K, by Lemma 2.5(a) together with protection.
- (vi) is ranking-independent: Lemma 2.5(b) for full-dimensional K, and Lemma 2.5(c) for the rest.
- Corollary 5.3 is a correct two-line argument.

**Proposition 5.5 versus SR66 C1.** The note contains SR66's precise version:
- (a) D_K is coherent on U and has no weak dominator other than itself.
- (b) (LF) fails on every one-sided V.
- The paragraph adds SR66's precisions (i) and (ii):
  - lower-dimensional coherent models on U exist iff K′ is not full-dimensional;
  - for lower-dimensional K ⊇ K′, exactly requirement (vi) fails;
  - for K′ ⊄ K, (iv) fails as well.

The citations check out against a fresh compile of the covering paper (`kcm/kcm.aux`):
- Prop 2.10 is `prop:lowdim`, which says U is "not essentially one-sided". The note correctly paraphrases "essentially one-sided".
- Cor 5.9 is `cor:precise`: the Brier ranking covers precise {p} with p ∈ relint Δ on the full domain.

## 4. Section 6: the abstract construction lemma

**Hypotheses versus what the proof needs, and versus SR66's four gaps:**
1. *The null record must be guidance.* This is (A1): 0 ∈ 𝒢_ω.
2. *Scores must be potentials whose differences are record-based.* σ_ω and d_ω satisfy d_ω(r(X,Y)) = σ_ω(X) − σ_ω(Y).
3. *The reading of "safe".* The note defines safe as "ρ ≠ r(Y,C) for all Y, C", the existential reading, under which SR66 noted that upward closure needs decomposability. The note does not derive upward closure. It *assumes* it, on the set 𝒯 of non-overlapping triples, in (A4). That is legitimate and suffices for (e).
4. *Null-invariance.* This is built in, because ℳ is a set of classes and r(X,Y) = 0 ⟺ X = Y.

Nothing is left unstated.

**Conclusions.** All six check:
- (a): reflexivity, FCC via the potential, and strict guidance via no ties.
- (b): (A1) is used only for "undominated", through reflexivity.
- (c): the record from (A3) is accepted at every world, N ≠ X, and (a) makes it strict.
- (d): follows from (a)–(c).
- (e): case split; the other summand is ≥ 0 by (a).
- (f): (A5) makes an all-guidance non-null record safe, and the equivalence then follows.

**Verification for the gamble ranking.** Correct:
- (A2) follows from Lemma 3.4(c) and int ℝⁿ₊ ⊆ C;
- (A4) follows from Lemma 3.1(b), ⊔-closure of G_i and Lemma 3.2(c);
- (A5) is Lemma 3.4(c).

Minor overclaim: "Lemma 6.1 thus yields Theorem 5.1(a)–(d)". The geometric clauses of 5.1(c) (N ⊆ hull(X) = hull(X∖N), and μ(N∖X) > 0) come from Theorem 4.3 directly, not from the lemma. The uniform Brier clause also uses finiteness of Ω. See R5.

**ERROR in the record-layer paragraph.** The note says: "Without records one could simply let X ⪯_ω Y hold when X = Y, or when Y ∉ 𝒞 and σ_ω(X) > σ_ω(Y); … but '(IB) and (Add) are lost'."

As written, this relation is **transitive**. Suppose X ⪯ Y ⪯ Z with X ≠ Y and Y ≠ Z. Then Z ∉ 𝒞 and σ(X) > σ(Y) > σ(Z), so X ⪯ Z. In particular it satisfies (Add). It loses (G) instead: a guided change out of a coherent model is refused. It also loses (IB).

CHECKED: `prop36_check.out`, RF0, gives 285 transitivity premises, all satisfied, plus explicit (G) and (IB) failures.

The meaningful record-free comparator adds the guidance clause: X ⪯_ω Y iff r(X,Y) ∈ 𝒢_ω, or Y ∉ 𝒞 and σ_ω(X) > σ_ω(Y). That relation does lose both (IB) and (Add). Example 7.1's own sets give both failures (C = U, with A and B as there):
- *(IB) fails.* The record (∅, B) has m₁ > 0 and is not guidance at world 1. From C it is refused, because C is coherent. From the incoherent model Y = C∖A the same record (Y∖B versus Y) is accepted.
- *(Add) fails.* C∖A ⪯₁ C by guidance, and C∖(A∪B) ⪯₁ C∖A because C∖A is incoherent and −m₁(B) > 0. The steps have disjoint supports A and B. But C∖(A∪B) ⪯₁ C fails: the record (∅, A∪B) is not guidance, and C is coherent.

CHECKED: RF1, on the analogous cone-model instance.

## 5. Section 7

**Example 7.1.** PROVED and CHECKED (`ex71_exact.out`). Every inequality in the note's proof is a statement about the balls (containment in U, disjointness, coordinate ranges) or a linear bound in the masses, so it holds for every μ satisfying (M).
- The witness a′ − (3/5)b′ has coordinate infima 1/25 and 26/25.
- m₁(r(X,Y)) > (43/40)δ > 0.
- m₁(B) < −(13/8)δ < 0.

Independently, for the concrete admissible μ with density 1 on the three balls:
- Q_B = {(t, 1−t) : t ≤ (1499 − √1299)/2498 ≈ 0.5857}, computed exactly without using the note's 3/5 witness;
- inf over Q_B × cl A of q·h ≈ 0.607 > 0, so A ⊆ hull(B);
- m₁(r(X,Y)) = π/80 > 0.

The incomparability of X and C, and the overlap remark, are correct.

**§7.2.** Correct, given Remark 4.4(d) and Proposition 3.6.

**§7.3: GAP.** The claims are true. Here is the missing proof. Let L_i(r) := (m_i(r), Σ_j m_j(r)) ∈ (ℝ², ≤_lex), an ordered abelian group, and Acc_i^lex := G_i ∪ {r safe : L_i(r) >_lex 0}.
- *Potential.* L_i(r(X,Y)) = Λ_i(X) − Λ_i(Y), where Λ_i := (m_i, Σ_j m_j). A non-null guidance record has m_i > 0, hence L_i >_lex 0. So every accepted non-null record has L_i >_lex 0. This gives:
  - reflexivity, a.e. ties and (IB), as in Prop 3.5(a);
  - (G);
  - no nontrivial ties;
  - (FCC) and (TC);
  - all cycles trivial.
- *(Add).* The proof of Prop 3.5(e) goes through verbatim, because L_i is additive and the other summand is ≥_lex 0.
- *Prop 3.6 analogue.* Suppose Y ≠ X weakly dominates X. Then L_i(r) >_lex 0 for every i, so m(Y) ≥ m(X); and m(Y) ≠ m(X), since otherwise every L_i = (0,0). Safety follows exactly as before.

  Conversely, suppose r is safe, m(Y) ≥ m(X) and m(Y) ≠ m(X). Then Σ_j m_j(r) > 0, so for each i, either m_i(r) > 0 or L_i(r) = (0, Σ_j m_j(r)) >_lex 0. So r is accepted strictly everywhere. Cor 3.7 also holds, by the same proof.

**What does not transfer.** The last two sentences of Prop 3.5(b) fail in the lexicographic variant: "m_i(X) > m_i(Y) unless X = Y" and "≺_i lies in the strict Brier order". A strict comparison can have m_i(r) = 0. Only ⪯_i ⊆ ⪯^B_i survives; strictness holds for the lexicographic potential. CHECKED: one exact dominance instance with some m_i(r) = 0.

**Recommendation (R2).** Do one of the following:
- (preferred) delete §7.3, because Theorem 4.3 makes it moot; or
- keep it, with the four-line proof above inserted and the sentence "(the strict part is then contained in the strict lexicographic order, not in the strict Brier order)".

## 6. Scope (§8) and conventions

**Scope.**
- §8.1–8.3 are factual and precise, with one exception. "All results concern finitely many worlds …" is false of Lemma 6.1, which is stated for Ω of any cardinality.
- Optional precision for the title (PROVED): modulo null sets, the coherent models on U are exactly the sets D ∩ U, where D is a coherent set of desirable gambles in the usual sense (a convex cone containing the positive gambles and no h ≤ 0). The argument:
  - int ℝⁿ₊ ⊆ D, so int D ≠ ∅;
  - D∖int D lies in the boundary of a convex set, which is Lebesgue-null;
  - int D is an open convex cone not containing 0, so int D = D_Q with Q the normalised dual cone, a nonempty credal set;
  - D_Q ∩ U = D_{conv(Q∪K′)}.

  One sentence in §2.2 or §8.1 would justify "coherent sets of desirable gambles" in the title, while recording that boundary (non-Archimedean) choices are invisible modulo μ.

**Conventions.**
- No names on theorem-like environments: OK (grep).
- \coloneqq is used throughout, except "aff Δ = {m : 𝟙·m = 1}" (line 124), which is a definition.
- "Models": OK. Standard dominance nomenclature: OK.
- No project-internal labels: grep finds none of Theorem H, (H), (★), CD, deletion, attack, round, audit.
- Self-contained: the only external dependence is two cited results of [KCM], used in prose only.
- Placeholder `% INFINITE-WORLD SECTION: pending refereeing` is present, between §6 and §7.
- Author block: "Jason Konek".
- Compile: my own three-pass pdflatex gives 17 pages, with no warnings, no overfull or underfull boxes and no undefined references. The PDF in the folder matches.

## 7. Required changes, ranked

1. **R1 (ERROR, §6 paragraph after the proof of Lemma 6.1).** The record-free relation as written is transitive, so it satisfies (Add). Replace the paragraph with:
   > "Without records one could let X ⪯_ω Y hold when r(X,Y) ∈ 𝒢_ω, or when Y ∉ 𝒞 and σ_ω(X) > σ_ω(Y). Given coherent models that improve every incoherent model at every world, this yields protection and dominance. But acceptance then depends on whether Y is coherent, which is not a property of r(X,Y). In the setting of Example 7.1, with C = U, the record (∅, B) is refused from C but accepted from the incoherent model C∖A, so (IB) fails. Moreover C∖(A∪B) ⪯₁ C∖A ⪯₁ C by disjoint steps, while C∖(A∪B) ⋠₁ C, so (Add) fails."

   Alternatively, keep the guidance-free version and say "(G) and (IB) are lost".
2. **R2 (GAP, §7.3).** Delete the remark (preferred), or insert the proof of §5 above together with the caveat that the strict part lies in the strict lexicographic order, not the strict Brier order.
3. **R3 (scope, §8.1).** "All results concern finitely many worlds" → "Apart from the abstract Lemma 6.1, all results concern finitely many worlds". Optionally add the modulo-null identification of coherent models with coherent sets of desirable gambles (§6 above).
4. **R4 (Remark 4.4(a), precision).**
   - K′ ≠ ∅ is used not only in Step 2. It is also used in Step 1, where G = hull(X) must be a coherent model and the maximiser's credal set must contain K′, and in Step 3, where Lemma 4.1 needs Q_X ≠ ∅.
   - (M) is also used in Step 3, through Lemma 2.2(b).
   - Say "It uses K′ ≠ ∅ throughout (Q_X ⊇ K′), and in Step 2 through an element k ∈ K′".
5. **R5 (§6, last paragraph).** "Lemma 6.1 thus yields Theorem 5.1(a)–(d)" → "yields the order-theoretic and dominance clauses of Theorem 5.1(a)–(d). The geometric clauses of (c) come from Theorem 4.3, and uniform Brier dominance uses the finiteness of Ω."
6. **R6 (paragraph after Theorem 5.1).** "(ID) … is equivalent to the conclusion of Theorem 4.3 that …" → "(ID) … is equivalent to the existence, for every incoherent X, of a coherent N with m(N) − m(X) ≫ 0 and r(N,X) safe (by Proposition 3.6 and Corollary 3.7)". The theorem's actual conclusion is stronger, since it includes hull invariance.
7. **R7 (Introduction).** The gloss of "covers" omits (C) and D_K ∈ ℳ_U. Add "is closed under ties with undominated coherent models", or say "(Definition 2.4 lists the exact requirements)".
8. **R8 (notation).**
   - r denotes both records and an integer count (Cor 3.9, "0 ≤ r ≤ n"; Remark 4.4(b)). Use k.
   - λ_j clashes with λ ∈ Δ in Step 1. Use, for instance, c_j or t_j.
   - B denotes both a ball and the removed set.
   - Write aff Δ ≔ {…}.
   - In Step 1, cite "μ is non-atomic (§2.1)" rather than "vanishes on points".

None of R1–R8 affects any theorem, proposition, corollary or lemma statement.

## Second round (Revision 2; 28 pages)

I compared the revised file with the version refereed above (`un66build/rev1_backup.tex` is byte-identical to it), read every changed hunk in Sections 1–6, 8 and 9, and recompiled it myself (`ref66un_py/build2/`). Three pdflatex passes give 28 pages, with no warnings, no overfull or underfull boxes and no undefined references. Conventions still hold:
- no named theorem-like environments;
- no `:=`;
- no project-internal labels.

The infinite-world placeholder comment is gone. That is expected, since Section 7 is now in place.

### Required changes 1–8: all made correctly

| # | Verdict | Check |
|---|---|---|
| R1 | DONE, CORRECT | The comparator now has the guidance clause. Incoherence of C∖A is correct: a.e. equality with D_Q gives D_Q ⊇ U∖cl A by Lemma 2.1(d); D_Q is convex, and conv(U∖cl A) ⊇ A; so μ(A ∩ D_Q) = μ(A) > 0, a contradiction. (IB) fails: (∅,B) is refused from C (not guidance, because B₊ ⊆ {h₁ > 0}; C is coherent) and accepted from C∖A (incoherent, with −m₁(B) > 0 for every admissible μ). (Add) fails: the supports A and B are disjoint, and (∅, A∪B) is refused from C. This matches `prop36_check.out` (RF1). The forward reference to Example 8.1 resolves |
| R2 | DONE | §7.3 deleted. The lexicographic material is now one sentence, which defines the variant and states "we do not use it". No claim is made |
| R3 | DONE, CORRECT | §9.1 says that §§2–5 concern finitely many worlds, and that Lemma 6.1 and Section 7 allow any set of worlds. The optional identification with coherent sets of desirable gambles is now Prop 7.16, with "the same holds in the finite setting, with the same proof". That is correct (cf. my §6 argument) |
| R4 | DONE, CORRECT | Remark 4.4(a) |
| R5 | DONE, CORRECT | §6, last paragraph |
| R6 | DONE, CORRECT | The paragraph after Theorem 5.1 |
| R7 | DONE | The introduction's gloss now includes (C) and D_K ∈ ℳ_U, and points to Definition 2.4 |
| R8 | DONE | k and t_j replace r and λ_j; W replaces E in Lemma 3.8; Ball(h,ρ) is used; aff Δ ≔; Step 1 cites §2.1 for non-atomicity. Lemma 2.5(c) now also says why −Ball(−h,ρ) ⊆ −V a.e. (Lebesgue-null sets are symmetric). That is a genuine improvement |

### Consistency of Sections 1–6, 8 and 9 with Section 7 (Section 7 itself not refereed here)

I found no conflict in Sections 2–6 or 8.
- Section 7 reuses Lemma 3.1, Lemma 3.2(c) and Lemma 6.1. Line 1336 says explicitly that the first two are set-theoretic and hold verbatim. That is correct, since their proofs use no geometry or measure.
- Lemma 6.1 already allowed any set of worlds.
- The new one-sidedness of §7.6 is implied by §2's definition in finite dimensions, as stated. So "covered on no one-sided domain" in §5 and in Theorem 7.13(c) are compatible statements.

Four points outside Section 7 now overstate or under-qualify Section 7's results:

1. **§9.4 (must fix).** "every incoherent model strictly dominated … and every dominance relation a uniform Brier improvement" is attributed to Theorems 5.1 *and* 7.9. Theorem 7.9(b) characterises dominance by m_ω(Y) > m_ω(X) for every ω. That is pointwise; only the repair of 7.9(d) has a uniform margin. Repair: "every dominance relation a Brier improvement at every world (uniform when Ω is finite)".
2. **Abstract and introduction (should fix).** In the extended setting they state that "precise and finitely generated targets are not covered on any one-sided domain". Theorem 7.13(c) proves this only when E is infinite-dimensional. The setting includes finite-dimensional E: E = ℝⁿ is the special case of Remark 7.10, where full-dimensional polytopes *are* covered by Theorem 5.1. Repair: insert "when E is infinite-dimensional".
3. **Abstract and introduction (should fix).** The measure hypotheses are listed as "finite first moment and null indifference boundaries". The coverage claims (Theorem 7.13, and C_U being all coherent models on U) also use (M3), full support. Repair: add "and full support".
4. **Minor.**
   - The abstract's "contamination models (1−ε){p}+εS are covered" holds in E = C(Ω) with Ω compact metric (Prop 7.15), on D_{p} when p has full support, and on D_{k′} for every p. Add "on C(Ω)".
   - §9.1 uses "one-sided" in §2's sense and in §7.6's sense in consecutive sentences. Add "(in the sense of §7.6)" to the second.

### Second-round verdict

Required changes 1–8 have all been made correctly. Before circulation, fix the one conflict with Section 7 (point 1, §9.4) and the two qualifications in the abstract and introduction (points 2 and 3). Nothing in Sections 1–6 or 8 needs to change.
