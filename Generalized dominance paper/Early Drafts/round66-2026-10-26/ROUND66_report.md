# Round 66 report: simple safe-improvement ranking, infinite worlds, two-sided domains, LDG route C

26 October 2026. Four constructors or writers: TS66, UN66, LDG66 and the auditor's own proofs (AUDIT_r66_extension). Seven referees: SR66, IW66a, IW66b, REF66_ldg, REF66_un, REF66_iw_section and REF66_ts.

Labels: PROVED (refereed at least once; independent referees named) / CHECKED / CONJECTURE / NUMERICS. Notes are in this folder.

## 1. Headlines
1. **The simple safe-improvement ranking works** (auditor; SR66, REF66_un). At world ω, accept a change if it is guidance, or if it is safe and strictly raises the Brier score at ω. A change is safe when it can be applied to no coherent model.
   - The ranking satisfies every agreed axiom, finite-chain consistency and (Add).
   - Every coherent model is protected, and every incoherent model is strictly dominated.
   - No designated deletion world, tie clause or lexicographic level is needed.
2. **Infinitely many worlds** (auditor's theorem; IW66a and IW66b, independently; REF66_iw_section for the write-up). The ranking is a universal cover on any set of worlds, for any separable sup-norm-closed space of bounded gambles containing constants, with a suitable measure on gambles. As an application, contamination models are covered on C(Ω), for every ε ∈ (0,1].
3. **Two-sided domains** (TS66; REF66_ts). On the full domain ℝⁿ, one ranking covers **every credal set**, including precise, lower-dimensional and boundary ones. More generally, the ranking is a universal cover on every hull-closed domain.
4. **Route C in the generalized loss dominance paper (LDG v3.3)** (LDG66; REF66_ldg, two rounds). The abstract safe-improvement construction theorem now sits beside route A (compact certificates) and route B (admissibility through scores). It is stated as a construction theorem, not an axiom.

**Consequence.** In finitely many worlds, every credal set is covered under the agreed axioms, by a single ranking on ℝⁿ.

## 2. The simple ranking (SR66, REF66_un)

**Definition.** For a change from Y to X, let A = X∖Y and B = Y∖X. Then X ⪯_ω Y iff:
- (A,B) is guidance at ω (including the null record); or
- (A,B) is safe and ∫_A h_ω dμ > ∫_B h_ω dμ.

**Safety test.**
- On one-sided domains: safe ⟺ μ(A ∩ hull B) > 0.
- On two-sided domains: safe ⟺ Q_B = ∅ or μ(A ∩ hull B) > 0.

**Proved properties.**
- Every accepted non-trivial comparison strictly raises that world's Brier score. This gives (TC), finite-chain consistency, and no non-trivial ties, so (C) holds trivially.
- (Add): a union of disjoint records that contains a safe part is safe.
- Protection: a change out of a coherent model is unsafe. It is therefore accepted only as guidance at every world, which forces it to be null.
- Dominance: Theorem H supplies a safe, strictly better coherent defender for every incoherent model.

**New facts (PROVED).**
- For this ranking, weak dominance by a different model, dominance, strict dominance, and "safe change with strict Brier gain at every world" are all equivalent (Prop 3.6, REF66_un).
- The ranking is not transitive. There is an exact counterexample, valid for every admissible measure.
- At world ω the ranking uses only ω's score, ω's guidance and the world-independent safety test.

**Lower-dimensional targets on one-sided domains (corrected statement).** Every coherent evaluable model, including the lower-dimensional ones, is undominated. What fails for lower-dimensional targets is (LF), and therefore coverage as defined.

## 3. The proof of Theorem H, as now written
Let X be incoherent.
1. **Relative minimax.** Optimise inside hull(X), not inside the whole domain. A minimax argument gives a coherent model N₀ that beats X strictly at every world.
2. **Hull-preserving shrink.** Shrink N₀ uniformly towards the simplex. The strict margin survives.
3. **Contraction lemma.** After the shrink, hull(X∖N) = hull(X).

In plain English, the new advice is already implied by the advice being removed. So the change cannot be applied to any coherent model.

## 4. Infinitely many worlds (IW66a, IW66b; written as §7 of the note, REF66_iw_section)

**Setting.**
- Any set Ω of worlds.
- E is a separable, sup-norm-closed space of bounded gambles. It contains 𝟙, or any order unit bounded below by a positive constant.
- The states S are weak-* compact and metrizable. E embeds in C(Ω̂), and the states are countably additive probabilities on Ω̂.

**Measure.**
- μ is finite, with ∫‖h‖ dμ < ∞.
- {P_Q = 0} is null for every compact Q. In particular {P_S = 0} is null, and that condition is essential: an explicit example shows guidance alone can otherwise dominate a coherent model.
- Construction: μ is the law of g + t𝟙, with weights satisfying Σ w_k(1 + ‖g_k‖) < ∞.
- Full support of μ is used only to identify models.

**Theorem (PROVED).** Every incoherent X has a coherent N such that:
- inf over states of the Brier gain is positive;
- hull(X∖N) = hull(X);
- μ(N∖X) > 0.

The proof uses relaxed choices with Sion's minimax theorem in place of Lyapunov. The contraction lemma is dimension-free, and a countable norming set Ω₀ handles guidance at every world.

**Ranking.** Every clause carries over.
- Dominance over Ω and dominance over Ω₀ are different relations, with an explicit example, but they have the same undominated set.
- With infinitely many worlds, dominance gives improvement at every world, not a uniform margin. There is an explicit example.

**Local freedom and coverage.**
- (LF) holds iff K′ ⊆ K and every k ∈ K′ is strictly positive on C_K∖{0}.
- The ranking is a universal cover on U. Every K with K_⊥ = {0} is covered on some domain.
- No K with K_⊥ ≠ {0} is covered on any one-sided domain. In infinite dimensions this excludes precise and finitely generated targets on one-sided domains.
- The uniform version of (LF) fails on C(Ω) for infinite Ω. It can hold in other infinite-dimensional spaces (the ℝ ⊕₁ ℓ¹ example).

**Contamination.** K = (1−ε){p} + εS on C(Ω), Ω compact metric, p of full support, 0 < ε ≤ 1, is covered on {p(h) > 0}. If p lacks full support, the target is covered on D_{k′} with k′ = (1−ε)p + εr, for any r of full support.

**Coherent sets of desirable gambles.** Every coherent set of desirable gambles is μ-a.e. equal to some D_Q.

**Scope.**
- Separability is essential: a nonseparable E has no finite full-support Borel measure.
- An order unit is needed. A world at which every gamble pays 0 makes every model undominated. The c₀ case is open.
- Which models count as incoherent depends on μ, since admissible measures can be mutually singular.
- One-sidedness uses a definition suited to asymmetric null sets. It is implied by the finite definition and is strictly weaker.

## 5. Two-sided domains (TS66; REF66_ts)

**Theorem (PROVED).**
- *Hypotheses:* finitely many worlds; μ with Lebesgue's null sets and a finite first moment; U = ℝⁿ; coherent models D_Q for every credal set Q.
- *Conclusion:* the simple ranking covers every credal set, including precise, lower-dimensional and boundary ones. It also satisfies (W), (Add), finite-chain consistency and strong (C).

**Proof.**
- **Nonempty hull (Q_X ≠ ∅).** Use the round-65 proof with K′ replaced by any point of Q_X. Step 2 only ever needed k·h ≥ 0 a.e. on X.
- **Empty hull (Q_X = ∅).**
  - *Lemma E:* Q_X = ∅ iff some prior λ makes X ∩ {λ·h < 0} a net Brier sure loss, m ≪ 0. Any such λ works; optimality is not needed (REF66_ts G2).
  - *Defender:* one relative minimax inside hull(X ∩ {λ·h > 0}) gives a coherent N with a strict gain at every world.
  - *Safety:* N lies in {λ·h > 0}, so the removed part contains the net sure loss. Its hull is empty, so the change is safe automatically. No shrink is needed.
  - *Degenerate cases:* X ∩ {λ·h > 0} may be null or coherent, and N∖X may be null; the proof covers each.

**Hull-closed domains (PROVED).** The ranking is a universal cover on every domain where traces of coherent models are coherent. These include:
- ℝⁿ;
- V₀ (all gambles that are not sure losses), and every domain between V₀ and ℝⁿ;
- every one-sided D_{K′}, and D_{K′} together with the sure losses;
- for n = 2, every domain admitting a (G) + (GC) ranking.

**Local freedom.**
- On ℝⁿ, (LF) holds for every credal set.
- On V₀, it holds exactly for those meeting relint Δ.
- Plain Brier on ℝⁿ covers exactly {p} for p ∈ Δ, which extends the covering paper's precise-target corollary.

**Corrections from REF66_ts.**
- "U ∪ (−U) is not hull-closed" holds for FD62's witness only. It fails for K′ = Δ and for singleton K′.
- TS66's two "obvious fix is unsafe" examples hold at the minimax prior, but not robustly: nearby half-spaces can be safe.

**Open.**
- Domains that are not hull-closed (settled for n = 2).
- A two-sided infinite-world version.

**Checks.** An independent exact engine certified the constructions on TS66's rivals and on new adversarial rivals, under two measures. Some long re-runs were stopped early; the verdict rests on the proofs.

## 6. LDG v3.3 (LDG66; REF66_ldg, two rounds; one fix by the lead)

**§3.7, route C.**
- **Theorem 3.13.** Each clause names its own hypotheses: (GI), (GP), (SI), plus (RS), (TG), (TS) for independence and (Add).
- **Hypotheses are exact (Remark 3.14).** (GP) ⟺ protection. Given (GI), (SI) ⟺ every incoherent model is dominated by a coherent one, and such dominance is always strict. Given (GI) and (GP), (SI) ⟺ (W).
- **Remark 3.15.** The record structure carries the content: with the finest possible records the theorem is trivial.

**Set-valued models.**
- Lemma 3.16 gives the set-valued claims, with the exact equivalence to independence.
- Lemma 3.17: (a) the hull test; (b) for countable Ω, a sufficient and necessary condition for (GP). The uncountable counterexample shows countability is needed.
- Example 3.18 is finite, shows intransitivity, and was checked by exact enumeration.

**Other changes.**
- Proposition 5.1 now assumes (LA) and (W). This is a strict generalisation, so the (P1) recipe can use route A, B or C.
- The §1 sentence on strict and uniform dominance is corrected.

43 pages; compiles cleanly.

## 7. Documents
- `Universal coverage of coherent sets of desirable gambles (draft).tex/.pdf`, 28 pages. It contains:
  - the simple ranking;
  - relative minimax, the shrink and the contraction lemma;
  - the abstract construction lemma;
  - infinite worlds;
  - scope.

  It does **not** yet contain the two-sided theorem of §5.
- `LDG_v3.3.tex/.pdf`, 43 pages.
- The covering paper is unchanged this round. Its framing (open problem (1) and the §8 exclusions) still predates universal coverage.

## 8. Coverage map
- **Finitely many worlds:** every credal set is covered, by one ranking on ℝⁿ. On a one-sided D_{K′}, the covered targets are exactly the full-dimensional K with K′ ⊆ relint K. On V₀, they are exactly those meeting relint Δ.
- **Infinitely many worlds, separable E with an order unit, one-sided domains:** exactly the K with K_⊥ = {0}, each on a suitable domain.
- **Score-generated rankings** (complete, transitive, (Add)) reach the VB class, class X, the orthant-planar polygons and boxes, and composed targets.
- **Open:**
  - two-sided infinite worlds;
  - domains that are not hull-closed (n ≥ 3);
  - nonseparable gamble spaces, such as all bounded gambles on an infinite Ω;
  - spaces without an order unit;
  - the philosophical question of independent accuracy-based justification, set aside by decision.

## 9. Proposed next steps
1. Add the two-sided theorem to the universal note as a section. The note would then state that every credal set is covered on ℝⁿ.
2. Reframe the covering paper around universal coverage. Present the score-generated constructions as more structured routes.
3. Two-sided domains with infinitely many worlds: TS66 has a sketch.
4. Nonseparable gamble spaces: decide whether this is worth pursuing.
