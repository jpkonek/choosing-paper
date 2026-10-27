# CEX73: attempt to refute dominance under consolidation (C3)

27 October 2026. Setting throughout: Ω = {1, 2}, E = R², μ the standard Gaussian, models modulo null sets. Notation: Q++ = {h₁ > 0, h₂ > 0}, Q−− = {h₁ < 0, h₂ < 0}, Q+− and Q−+ the mixed quadrants. A change (A, B) adds A and removes B. "The change Y→X is accepted at ω" means X ⪰_ω Y. A chain X ⪰_ω … ⪰_ω Y is written X ⪰*_ω Y.

Script: `cex73_py/checks.py` (numerical sanity checks only).

## 0. Results

| # | Statement | Label |
|---|---|---|
| 0 | **No counterexample found.** Every attempt is blocked, and the blocks are listed below. | — |
| 1 | **Pure ties do not shelter.** Suppose R ∈ 𝓡+C3 accepts, at every world, the consolidation of some matched triple inside X. Suppose further that the triple's second piece lies in Q++ or its sum piece lies in Q−− (hypothesis (H)). Then R has an extension in 𝓡+C3 in which X is strictly dominated at every world, so X is dominated in some maximal member above R. Ties with consolidations therefore never protect a model satisfying (H). | PROVED (Thm G) |
| 2 | (H) holds for every incoherent X except those that are, a.e., upward closed (X + Q++ ⊆ X), closed under "halve, then add a positive gamble", and with X + X missing Q−−. A staircase example of this exceptional kind exists. | PROVED; example CHECKED + NUMERICS |
| 3 | **Score-monotone rankings fail.** Let s be linear, or any superlinear score from the test family. If every accepted comparison of R ∈ 𝓡+C3 weakly raises s_ω at its world, and X has a coherent-unavailable change raising s at both worlds, then X is dominated in some maximal member above R. For s = m, the repair theorem supplies that change for every incoherent X. | PROVED (Lemma A, Cor A′) |
| 3′ | The same holds for every loss-averse test score (density c_ω h_ω⁺ − d_ω h_ω⁻ with 0 < c_ω ≤ d_ω, which is the whole C3 test family on R²). | CHECKED (Prop B; geometric proof, not refereed) |
| 4 | **Entrenched ties are consistent but useless.** "Score + protection refusal + ties on every change with zero score increment at both worlds" lies in 𝓡+C3. It is score-monotone, so item 3 kills it. | PROVED (Prop C) |
| 5 | **Patching fails.** A distorted-score ranking R_{s′} cannot be repaired by declaring every exact consolidation change a tie: the E3 route still violates C3. | PROVED (uses AX72 C3.1 numerics) |
| 6 | **Shape of mechanism (b).** If X survives its consolidation rival X′ at some world through a blocked incomparability, the blocking configuration must use the consolidation change in at least two contexts, or form a C3 chain for a *different* triple. One instance in one context never suffices. | PROVED (Lemma D) |
| 7 | **Closure under ties (CT).** CT kills every design in which X is tied at every world with a coherent undominated model, including "X is a split of a coherent C". CT is silent when X's consolidations are incoherent. Since items 1–4 already defeat pure ties, CT adds nothing new there. | PROVED |
| 8 | **The surviving target.** A counterexample, if one exists, needs three things. (i) X is of the exceptional kind in item 2. (ii) R is not monotone for m or for any loss-averse score. (iii) For every repair of X there is a chain at some world, with a strict link that lowers m, using several contexts. I could not build such an R. | CONJECTURE-level map |

**Bottom line.** The two shelters named in AX72 C3.8 are much narrower than they looked.
- **(a) Ties with consolidations** fail outright for every incoherent model except a thin exceptional class (items 1–2). The reason is short: once the consolidation is accepted at every world, "consolidate, then make a step guided at every world" can be added at every world, and that gives strict dominance.
- **(b) Context-blocked incomparabilities** must be genuinely multi-context (item 6), and they must defeat every score-monotone structure (items 3–4).

I found no ranking that does both. This is evidence for the dominance conjecture, not a proof of it. The exceptional class in item 2 is where a proof attempt should look next.

---

## 1. Pure ties do not shelter (Theorem G)

**Setting.** R ∈ 𝓡+C3. X contains Q++ and misses Q−− a.e. (if not, a guided rival already strictly dominates X in R). Let τ = (G₁, G₂, G₃; T, S) be a matched triple (sum or midpoint) with G₁ ∪ G₂ ⊆ X and G₃ ∩ X null. Let c = (G₃, G₁ ∪ G₂) be its consolidation change and X′ = X∘c.

**Hypothesis (H).** One of the following holds:
- (H1) G₂ ⊆ Q++. Then e := (G₃, G₁): remove G₁, add G₃.
- (H2) G₃ ⊆ Q−−. Then e := (∅, G₁ ∪ G₂): remove both pieces.

**Theorem G (PROVED).** Assume (H), and assume R accepts c at both worlds, i.e. X′ ⪰_ω X for ω = 1, 2. This holds in particular when X ~_ω X′ at both worlds, which is shelter (a). Let R⁺ be R with the change e also accepted at both worlds, in every context. Then:
- R⁺ ∈ 𝓡+C3;
- R ⊑ R⁺, with all weak and strict comparisons kept;
- Y := X∘e satisfies Y ≻⁺_ω X at both worlds.

By AX72 (chain unions preserve the class and C3; Ω finite), Zorn gives a maximal member above R⁺. X is dominated there.

**Step 1: e is chain-realised in R at each world, in every context, with a strict link.** Let W be any context of e (W contains the removed set and misses the added set).

- **(H1), case G₂ ⊆ W.** W∘e = (W∘c) ∪ G₂. The chain is W∘e ≻_ω W∘c ⪰_ω W.
  - The first link adds G₂ ⊆ Q++, so it is guided at ω, and strict by (G).
  - The second link is c, which R accepts in every context by (I).
- **(H1), case G₂ ∩ W null.** The chain is W∘e = (W ∪ G₂)∘c ⪰_ω W ∪ G₂ ≻_ω W.
- **(H1), mixed case.** Split τ into the sub-triples over T⁻¹(G₂ ∩ W) and T⁻¹(G₂ ∖ W). Restrictions of a matched triple are matched triples. Their changes have disjoint supports, so the two chains above can be run one after the other.
- **(H2).** Split G₃ into G₃ᵃ = G₃ ∩ W and G₃ᵇ = G₃ ∖ W. Put W₁ = W ∖ G₃ᵃ and W₂ = W₁∘c = (W∖B) ∪ G₃. The chain is W∘e = W ∖ B ⪰_ω W₂ ⪰_ω W₁ ⪰_ω W.
  - The first link removes G₃ᵇ ⊆ Q−−, so it is guided.
  - The second link is c.
  - The third link removes G₃ᵃ ⊆ Q−−, so it is guided.
  - At least one of G₃ᵃ, G₃ᵇ is non-null, so at least one link is strict.

  In the midpoint case the same holds, since W₁ ⊇ G₁ ∪ G₂ and W₁ ∩ G₃ is null.

**Step 2: no coherent model could make e.**
- (H1): if D_Q ⊇ G₁, then D_Q ⊇ G₁ + G₂ (sum case), or D_Q ⊇ ½(G₁ + G₂) (midpoint case), since D_Q ⊇ Q++ ⊇ G₂ and D_Q is a convex cone. Hence D_Q ⊇ G₃ = S(G₁). But e adds G₃, which is non-null.
- (H2): G₁ ∪ G₂ is inconsistent. A state q ≥ 0 a.e. on both pieces would give q·S(h) ≥ 0 on G₁, while S(G₁) = G₃ ⊆ Q−− forces q·S(h) < 0.

**Step 3: the axioms for R⁺, every instance included.**
- **(R), (I).** e is added as a change, in every context, at both worlds.
- **No reversal of R's strict comparisons.** Only ē-instances could lose strictness. Suppose ē ∈ R_ω in some context W∘e, i.e. W ⪰_ω W∘e. Joined with the Step 1 chain W∘e ⪰*_ω W, this gives an R-cycle with a strict link, contradicting (SC) for R. So ē ∉ R_ω at either world.
- **(G).** A guided change g at ω could lose strictness only if ḡ = e at ω. Then ē would be guided, so ē ∈ R_ω, which was just excluded.
- **(SC).** Replace each e-link in a would-be R⁺ cycle by its Step 1 chain. The result is an R-cycle containing a strict link, which contradicts (SC) for R. This covers every number of e-instances and every context.
- **(C3).** Make the same replacement in a would-be C3 chain Z ⪰*⁺ Z′ for any triple. It becomes an R-chain Z ⪰* Z′ with a strict link, contradicting (C3) for R.
- **(P).** The only new comparisons are e-instances. A coherent C dominated in R⁺ but not in R would have to make the change e. Step 2 excludes this.
- **Strict dominance.** Y ⪰⁺_ω X at both worlds. X ⪰⁺_ω Y would be ē, and ē ∉ R⁺. ∎

**Corollary G′.** Ties with consolidations (AX72 C3.8(a)) protect X only if no consolidation of X that is accepted at both worlds satisfies (H). Equivalently: for each (H)-triple, X must already be protected at some world by mechanism (b).

## 2. Which incoherent models escape (H) (PROVED; example CHECKED)

**Existence of triples.** By AX72 C3.1 and C3.7(ii) step 2, matched triples exist inside small polar sectors around any non-collinear density points. The pieces can be placed inside X, or inside its complement.

- **(H1) with a sum triple** exists iff there are density points x of X (x ∉ Q++) and p ∈ Q++ with x + p a density point of E∖X. So (H1)-sum fails iff X is a.e. upward closed.
- **(H1) with a midpoint triple and p near 0** exists iff some density point x of X has (x + p)/2 ∉ X, which for small p means x/2 ∉ X.
- **(H2)** exists iff some density points x, y of X have x + y ∈ Q−− (for midpoints the condition is the same, since Q−− is a cone).

So the exceptional class is: models that are a.e. upward closed, satisfy ½x + Q++ ⊆ X, and have X + X disjoint from Q−−. Every incoherent model outside this class is covered by Theorem G. That includes:
- all reflex cones, such as X* = D_{(1/3,2/3)} ∪ D_{(2/3,1/3)};
- all models that are not upward closed;
- all models that are not closed under halving.

**Staircase example (exceptional and incoherent).** X = {h : −h₁ < 2ᵏ < h₂ for some k ∈ Z} ∪ Q++.
- X is upward closed. It is closed under h ↦ h/2 + p for p ∈ Q++. It lies in {h₂ > 0}, so X + X misses Q−−.
- X is not a cone: (−0.9, 1.2) ∈ X but 1.5·(−0.9, 1.2) ∉ X.
- X is not convex under sums: x = (−0.98, 1.04) and y = (−0.46, 0.52) lie in X, but x + y = (−1.44, 1.56) ∉ X. So X has (non-(H)) consolidation triples.
- NUMERICS (`checks.py`): 5·10⁴ random draws found no failure of upward closure or half-closure, and no sum in Q−−.

## 3. Score-monotone rankings fail (Lemma A)

Let s_ω(X) = ∫_X g_ω dμ, where g_ω is sign-respecting and superlinear. Every consolidation then weakly raises s at both worlds. Call R **s-monotone** if X ⪰_ω Y implies s_ω(X) ≥ s_ω(Y).

**Lemma A (PROVED).** Let R ∈ 𝓡+C3 be s-monotone. Let X and Y be models such that:
- the change e = X→Y raises s_ω strictly at both worlds;
- no coherent model could make e.

Then R⁺ = R + e (at both worlds, in every context) lies in 𝓡+C3, extends R, and makes Y ≻⁺_ω X at both worlds.

*Proof.*
- **ē ∉ R.** ē lowers s_ω at both worlds, while R is s-monotone. So no strict comparison of R is reversed, and (G) is kept.
- **(SC).** Every link in an R⁺ cycle weakly raises s, and every e-link raises it strictly. So a cycle contains no e-link, and is an R-cycle with the same strictness. (SC) for R excludes it.
- **(C3).** In a chain Z ⪰* Z′ from split to consolidated, s(Z) ≥ s(Z′) ≥ s(Z), so every link has zero increment. Hence the chain contains no e-link, and it is a chain of R, which (C3) for R excludes.
- **(P).** e is unavailable. ∎

**Corollary A′ (PROVED).** Take s = m. Then every incoherent X has such a Y: the repair N of app.tex Theorem `thm:repair`, by items (1) and (4).

So every m-monotone R ∈ 𝓡+C3 is useless as a counterexample. This covers:
- R0, R∩ and every round-71 maximal ranking;
- the ranking R_X of §6 below;
- every "linear score + any ties on zero-increment changes" ranking.

**Prop B (CHECKED, two worlds).** On R², the sign-respecting superlinear densities are exactly g_ω = c_ω h_ω⁺ − d_ω h_ω⁻ with 0 < c_ω ≤ d_ω. To see this, note that g_ω is positively homogeneous and concave, and vanishes on the axis {h_ω = 0}. Then g(1, t) is concave in t with g(1, t)/t → 0 at ±∞, so it is constant.

For each such s, every incoherent X ⊇ Q++ missing Q−− has an unavailable change that raises s strictly at both worlds:
- **X ∩ Q−+ is not a.e. a full sector (90°, α*).** Take a gap at an angle φ₀ below an X-piece at angle φ₁ > φ₀. Move mass from the piece into the gap: A ⊆ gap, B ⊆ piece, with ∫_A h₂ = (1+ε)∫_B h₂.
  - On Q−+, s is linear: s = (d₁ m₁, c₂ m₂). The ratio |h₁|/h₂ is smaller on A than on B, so both increments are positive for small ε.
  - A ⊆ hull(B), so the change is unavailable.
  - The case X ∩ Q+− is the mirror image.
- **Both mixed parts are full sectors, and X is a reflex cone.** Remove small pieces near the two boundary rays a and b. Both increments are positive iff the mass ratio lies in (c₁b₁/(d₁|a₁|), d₂|b₂|/(c₂a₂)). This window is non-empty because |a₁||b₂| > a₂b₁ (reflex) and c ≤ d (NUMERICS: `checks.py`). The removed pair is inconsistent, so the change is unavailable.
- **Otherwise** X is a.e. a convex cone, hence coherent.

So every s-monotone ranking in the C3 test family fails.

## 4. Entrenched ties are admissible but harmless (Prop C, PROVED)

Fix s as in §3. Let d_ω(A, B) be the s_ω-increment of a change. Call a change *protected* if it is non-null, some coherent model could make it, and d > 0 at both worlds. Let ω(A, B) be the least world that does not guide it; this exists by REF72 Lemma 1. Define R_s^T: accept (A, B) at ω iff

(i) d_ω(A, B) > 0 and not [protected and ω = ω(A, B)], or

(ii) d(A, B) = (0, 0), which covers null changes and also ties on every doubly zero-increment change.

Checks:
- **(R), (I).** Immediate.
- **(G).** A guided non-null change has d_ω > 0, and refusal never occurs at a guiding world. Its reverse has d_ω < 0, so it is refused.
- **(SC).** Strict links have d > 0, because (ii) is symmetric. Every accepted link has d ≥ 0. A cycle therefore has no strict link.
- **(C3).** Suppose a chain runs from Z to Z′ with a strict link. Then s(Z) > s(Z′), but superlinearity gives s(Z′) ≥ s(Z).
- **(P).** Suppose C is coherent and C→Y is accepted at both worlds and strict somewhere. Strictness excludes clause (ii) at that world, so d ≠ (0, 0), and then clause (ii) cannot apply at either world. So d > 0 at both worlds, the change is protected, and it is refused at ω(A, B).

Chain unions preserve every clause.

R_s^T is s-monotone. Lemma A and Prop B (or Cor A′ for s = m) therefore defeat it.

The REF72 mechanism needs X to be the unique Bayes maximiser. With superlinear s that maximiser is coherent (C3.7(i)), and the zero sets are null, so ties cannot enlarge it.

## 5. Patching a distorted score fails (PROVED)

Let R̂ be R_{s′} with every exact consolidation or splitting change declared a tie at both worlds. Take any triple near (a, b, a+b) as in AX72 C3.1, any split model Z (containing G₁ ∪ G₂ and missing G₃), and a tiny ball K ⊆ Q++ ∩ Z. Then Z ≻₂ Z ∖ K by guidance. The change Z′ → Z∖K is not an exact splitting change, because the measures differ. Its s′₂-increment is ≈ +1.49 μ(G₁) − s′₂(K) > 0. Its s′₁-increment is −s′₁(K) < 0, so it is not protected, and R̂ accepts it at world 2.

So Z ⪰₂ Z∖K ⪰₂ Z′ is a chain with a strict link, and C3 fails. Ties on exact consolidation changes cannot neutralise a non-superlinear score. Chain-form C3 forces the score structure near every consolidation, perturbations included.

## 6. What mechanism (b) must look like (Lemma D, PROVED)

**Lemma D.** Let R ∈ 𝓡+C3 and let c be any consolidation change.
- (i) In no context W does R contain a chain W ⪰*_ω W∘c⁻¹, i.e. from the consolidated model up to the split one. This is C3 itself.
- (ii) Hence adding c at ω cannot create a forbidden cycle that uses a single c-instance in a single context. Such a cycle is W∘c ⪰ W ⪰* W∘c, and its R-part is a chain from the split model to the consolidated one. If that chain has a strict link, C3 forbids it. If it has none, the cycle's only possible strict link is the new c-link, and that link is strict only if the split direction is absent. In that case W ⪰* W∘c, so the new link closes a weak cycle, and it can be kept as a tie.
- (iii) Therefore a block of mechanism (b) against X′ at ω uses at least two instances of c in different contexts, or creates a C3 chain for a different triple through a c-link.
- (iv) Under (H), Theorem G shows that even such blocks are useless once c is accepted at the *other* world as well. The block must therefore sit at the very world where c is absent, for every (H)-triple of X.

**The guidance-and-ties ranking R_X (PROVED in 𝓡+C3).** It accepts guided changes, plus every X-type consolidation and splitting change at both worlds.
- m is a potential for it: ties have zero m-increment and guided links strictly raise m. This gives (SC) and (C3).
- (P): a change accepted at both worlds is either a tie (never strict) or guided at both worlds (null, by REF72 Lemma 1).
- X is undominated *in R_X*. But R_X is m-monotone, so by Cor A′ X is dominated in some maximal member above it.

This is the cleanest illustration of the gap: ties are consistent, but the repair extension is always available.

## 7. Closure under ties (CT)

- **Designs where X is tied at every world with a coherent undominated model** (for example X = a split of a coherent C, with X ~ C as a consolidation tie) are excluded outright by CT. PROVED: this is the definition of CT, and C is undominated by (P).
- **Ties with incoherent consolidations** are not touched by CT. Theorem G already disposes of them under (H).
- **For the exceptional class**, CT gives nothing extra unless a single consolidation of X is coherent. For the staircase, every one-step consolidation is still non-convex, so CT is silent.

## 8. What a counterexample would still need (map, not a result)

A counterexample R would need all of the following:
1. X in the exceptional class of §2 (upward closed, half-closed, X + X missing Q−−), such as the staircase.
2. R not monotone for m, nor for any loss-averse score (§3).
3. For the m-repair N of X, and for every other unavailable improving change, R contains at some world a chain from X down to that rival with a strict link that lowers m. Alternatively, it contains a multi-context cycle that becomes forbidden once the change is added. Every such chain must itself survive (SC) and (C3) in every context, (P) at both worlds, and (G).
4. For the staircase, the repairs fill the gaps between steps from the outer steps (a hole-filling exchange inside Q−+). By the §3 argument, each such exchange equals "consolidate an outer piece with a positive piece, then …" only at world 2, where re-adding a Q−+ piece is guided. At world 1 the exchange lowers m₁. This is why Theorem G does not apply, and it is the one place I see room. The block would have to be a world-1 chain that lowers m₁ and that no extension can neutralise.

I tried lexicographic rankings (primary linear or loss-averse score, non-linear tie-breaker). The primary level forces X to be Pareto-optimal for the primary score, which makes X a Bayes set and so coherent. I also tried veto-primary rankings, where veto-only primaries violate (G)-strictness or (P) on all of E. Complete (total-preorder) rankings with (I) and (P) for all coherent models seem to need a non-Archimedean primary level. I did not find one that also passes (C3). These attempts are not written as proofs (UNCLEAR).

## Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/CEX73_report.md` (this report)
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/cex73_py/checks.py`: staircase membership, closure tests, and Prop B mass-ratio windows.
