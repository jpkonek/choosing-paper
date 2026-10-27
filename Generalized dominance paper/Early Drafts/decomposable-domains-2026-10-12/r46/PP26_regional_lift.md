# PP26: lifting the two-world gate to three worlds, region by region

22 October 2026. Answers Brief 46, task PP26. Unrefereed. Scripts are in `PP26_py/`, with outputs in `*.out` next to each script. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Finite cells are diagnostics only.

## Summary

The verdict is negative for (S) and positive for local defences.

1. **A region is not a one-coordinate two-world problem (§1, PROVED).**
   - On M_k the rank changes really are two-world: the two majority worlds move together, and the minority world moves the opposite way.
   - But the problem space of M_k is two-dimensional. It splits into a one-parameter family of genuine two-world problems, the *pencils*: lines through a common point of the extended edge opposite e_k. On each pencil a coherent model is an interval. The two extreme pencils are the edge problems at e_k.
   - The lead's claim is false as stated. D_K on M_k is not determined by any one projection of K. It is not determined by the two edge projections either, unless K has a lowest and a highest point in the e_k-ratio order. T1 has no highest point.
   - A precise model is determined by its restriction to any single region. Two generic precise models are crossed on exactly one region: the one whose coordinate is the median of the log-ratio differences.
2. **Every combination rule with a veto fails (S) (§2, Theorem V, PROVED).**
   - Suppose one world refuses every record that purely improves it on one region (its own region, or a majority region), in the patterns stated in §2. Then (S) with closed sections fails.
   - The rival is X = (B on M_i, B on M_j, A on M_k) or AAA. Neither has a coherent dominator.
   - The argument uses one veto at one world, plus strict (G) at one other world. It uses no keys, no gates, no verdicts and no (TC). So region-dependent or record-dependent keys cannot rescue such a lift.
   - **AND** across regions has a veto at every region. It is acyclic, but its competitive coherent models are exactly V_1, V_2, V_3.
   - **Lexicographic** by region has a veto at its first region.
   - **Every mass-blind rule** has a veto (Theorem M; PROVED by exhaustive enumeration). Here a mass-blind rule is any rule that judges region-pure records by their improve/worsen pattern alone, and is (TC)-safe with strict (G). Its accepted patterns are contained in those of one of the six lexicographic orders.
3. **Region-weighted rules collapse to additive ones (§3, Theorem R, PROVED for region-constant weights).**
   - Sticky sums across regions violate (TC).
   - Take any linear rule "accept iff weighted added ≥ σ_i × weighted removed". Suppose it covers both the A-ward and the B-ward three-region rivals out of one interior imprecise model. Then σ_i = 1 at every world, and a Perron root equals exactly 1.
   - After that, (TC) forces every accepted record supported in at most two regions to be additively endorsed. The gated sticky verdict that carries gate2d's non-additivity is excluded.
4. **PP2 Thm 6 (§4).**
   - The lexicographic and AND lifts with gate2d-style regional keys are fixed-key weak gates: put the regions' keys in separate bands. So they meet Thm 6's hypothesis whenever the own-region level-1 key is not constant (PROVED).
   - The failure does not depend on that key. At a band boundary, Lemma 6.1's threshold model is exactly Theorem V's incoherent X, and this gives the contradiction even with a constant key.
   - Region-dependent or record-dependent keys cannot help any veto rule. Only giving up vetoes avoids the obstruction, and then §3 applies.
5. **Positive result: local defences along regionally nested chains (§5, Theorem C, PROVED).**
   - Use one region order for all worlds, chain-adapted regional keys, and the sticky gated verdict on the first region where a record is nontrivial.
   - Every member of the chain C_t = D_{(1−t)M + t e_1}, t ∈ [0,1], from T1 to V_1, is then coherent, undominated and competitive against every model, bounded or not. The system has strict (G), (IB) and no cycles. No positive integrable field endorses world 1's comparisons out of the chain.
   - This passes audit's two-model test (T1 versus any C_t), uniformly along a one-parameter family, with non-additive defences that are actually used.
   - It cannot be extended to a model that is crossed with the chain on some region. So it cannot reach a two-dimensional family, and (S) fails by Theorem V.
6. **T1 (Q5).**
   - Each pencil projection of T1 is an interval, but its regional profile is not an interval of any single coordinate.
   - T1 is a member of three regionally nested chains (homotheties toward the vertices), so Theorem C gives it full local defences.
   - T1 cannot be selected under any veto lift. Under a linear region-weighted lift, its competitiveness forces the additive collapse of Theorem R.

**Bottom line.** Within the kinds of lift the brief names (AND, lexicographic, Boolean, region-weighted), there is a precise obstruction to (S). There is also a precise positive module for local defences along chains. A regional lift that could still work must have no veto at any world. Its cross-region trading must therefore be mass-sensitive in both directions, and it must not be linear with region-constant weights. That is no longer "gate2d region by region".

---

## 0. Setting and notation

- **Problems and regions.** Problems are g ∈ R³ modulo sign, with the Gaussian μ. U is the unanimous problems. M_k is the mixed problems whose odd coordinate is k (world k is the *minority* world; the other two are the *majority* worlds).
- **Advice on M_k.** A is the advice good for the two majority worlds, B the advice good for world k, S is silence, Ct is contradiction.
- **Ranks on M_k.** At a majority world: A 0, S 1, B 2, Ct 3. At world k: A 2, S 1, B 0, Ct 3.
- **Steps and records.** U_w(Y) is the set of world-w rank steps of Y, as in gate2d.
  - A record's *M_r-part* is its restriction to M_r.
  - The part is a *pure world-w improvement* if the new model is weakly better at w on M_r and differs from the old one on a non-null subset of M_r. *Pure worsening* is the mirror case, and *trivial* means no change on M_r.
  - For a record that is trivial on U and pure on each region, its *pattern at world w* lists, region by region, T (trivial), W (pure worsening) or I (pure improvement).
- **(★) KKM consequence of (S)** (PP2 §0, PROVED). (S) with closed sections, with C_p competitive on supp p, gives the following: for every model X there is a selected coherent C_q with C_q ⪯_w X at all three worlds.
- **Lemma 0 (PROVED; PP2 Lemma 6.2).**
  - A coherent model that is A a.e. on M_a is D_K with K inside the face opposite e_a.
  - A coherent model that is B a.e. on M_a is V_a. If K contained m ≠ e_a, a non-null set of M_a-lines would pass between e_a and m.
  - Hence a coherent model that is A a.e. on two regions M_a, M_b is V_c, where c is the third index.

## 1. What a region looks like

**Proposition 1.1 (rank identity; PROVED).** On M_k the two majority worlds have equal ranks under every advice. For regular advice (A, S, B), the minority rank is 2 minus the majority rank. Ct has rank 3 at all worlds. So every record restricted to M_k is a two-world record for the sides {k} and {i, j}, and the two majority worlds always reach the same regional judgement if they use the same regional key and verdict.

**Proposition 1.2 (pencils; PROVED).** Take k = 1.
- **The pencils.** An M_1-line in the simplex separates e_1 from [e_2,e_3]. It meets the line through e_2 and e_3 outside the closed segment [e_2,e_3], or is parallel to it. So M_1 is the disjoint union of the pencils of lines through the points P of that extended line outside the segment, together with the point at infinity.
- **Coordinates.** In coordinates, write g = (−a, b, c) with a, b, c > 0, and s = b/(b+c). Then g lies in the pencil P_s, and on it D_K is
  - B if a > max ψ_s(K),
  - A if a < min ψ_s(K),
  - S otherwise,

  where ψ_s(m) = (s m_2 + (1−s) m_3)/m_1. So on each pencil a coherent model is an interval of the threshold coordinate: a genuine two-world problem.
- **The edges.** As s → 1 the pencil point tends to e_3, and ψ_1(m) = m_2/m_1 is the central projection onto [e_1,e_2]. As s → 0 it tends to e_2, and we get the projection onto [e_1,e_3].
- **Status.** The formula is CHECKED exactly on 2,000 random cases (`regions.py` §2).

**Proposition 1.3 (no single coordinate; PROVED).**
- **(a) Edge projections do not determine the profile.** Let K = conv{(1,1,1)/3, (1,2,2)/5} and K' = conv{(1,1,2)/4, (1,2,1)/4}.
  - Both have e_1-ratio ranges m_2/m_1 ∈ [1,2] and m_3/m_1 ∈ [1,2], so both edge projections agree.
  - On the line (−7/2, 1, 1), D_K is S and D_{K'} is B. All 840 lines of a small box around it differ (exact).
  - Neither edge projection determines D_K|M_1, and neither does any single ψ_s, since K and K' agree at s → 0, 1 and differ at s = 1/2.
- **(b) When edge projections do determine it.** D_K|M_1 is determined by the two edge projections exactly when K has a product-order lowest point lo and highest point hi in the ratio coordinates (m_2/m_1, m_3/m_1). Then D_K|M_1 = D_{conv{lo,hi}}|M_1.
  - *Proof.* The e_1-side of an M_1-line is a down-set {b m_2 + c m_3 < a m_1}, and the far side is an up-set.
  - If hi is not attained, put hi* = (max x, max y). The down-closure of K is convex (projective maps preserve convexity) and misses hi*. A strictly separating line with positive normal, perturbed to an open set of M_1-lines, has K strictly on the e_1-side and hi* not. So conv(K ∪ {hi*}) has the same edge projections and a different profile on a non-null set. ∎
- **(c) T1 has no highest point.** For T1 = D_M, M = c·1 + εΔ, the e_1-ratios of the vertices (ε = 3/10) are v_1 (7/16, 7/16), v_2 (16/7, 1) and v_3 (1, 16/7). The maximum of m_2/m_1 is at v_2 and that of m_3/m_1 is at v_3.
  - So T1's M_1 profile is fixed by v_1 (its A-boundary) and the far facet [v_2,v_3] (its B-boundary). It is not an interval of any coordinate.
  - CHECKED: on the line (−776/175, 1, 1), T1 is B and the box model with the same edge projections is S.
- **(d) A single region determines a precise model.** For precise p, D_p|M_k determines p. The lines with p strictly on the e_k-side are the open half-planes containing p and e_k, and they cut out p.

**Proposition 1.4 (median rule; PROVED).** Let p, q be precise and interior, and put δ_r = log q_r − log p_r.
- D_p and D_q are nested on M_k (U_k(D_p) ∩ M_k ⊆ U_k(D_q) ∩ M_k or the reverse; equivalently, at the majority side) iff δ_k is not strictly between the other two δ's.
- So two generic precise models are crossed on exactly one region, the region of the median δ.
- *Proof.* On g = (−a, b, c) ∈ M_1, D_p is B iff a > b p_2/p_1 + c p_3/p_1. Inclusion for all a, b, c > 0 holds iff both ratios move the same way. ∎
- CHECKED (`regions.py` §3): 300 random pairs and 4,000 lines per region. There were no refutations; the sampler missed 37 thin crossings. Every pair is predicted crossed on exactly one region.

**Proposition 1.5 (homothety chains; PROVED).** Let K_t = (1−t)M + t e_1.
- At every problem the world-1 rank of D_{K_t} is non-increasing in t. Each vertex value (1−t)v·ĝ + tĝ_1 moves linearly toward ĝ_1, so the minimum and the maximum change sign at most once.
- So the chain is nested on every region at every world. World 1 improves everywhere. World w ≠ 1 worsens on M_1 and M_w and improves on the third region.
- **The tripod is not nested.** The legs toward e_1 and toward e_2 are crossed on M_3. CHECKED with exact witnesses; on fresh lines 773 go one way and 825 the other.

**Reading.** gate2d works because the selected models are threshold sets of one key at each world, and so are nested. Regionally, the same mechanism needs the selected restrictions to M_k to be nested. By 1.3(d) and 1.4 that holds only along chains, not across a two-dimensional family: precise models collinear with a vertex, homothety rays, and the like.

## 2. Combination rules with a veto

### Definition and theorem

**Definition (veto region).** World i has a veto region if one of the following holds.
- **(V-own)** For some j ≠ i (k the third index), world i refuses every record, trivial on U, whose pattern at i is
  - (own I, M_j W, M_k I), or
  - (own I, M_j W, M_k T).
- **(V-maj)** For some f ≠ i (o the third index), world i refuses every record, trivial on U, whose pattern at i is
  - (own W, M_f I, M_o I), or
  - (own W, M_f I, M_o T).

Patterns with no W are pure improvements and are refused anyway under strict (G).

**Theorem V (PROVED).** Assume strict (G) at every world and (S) with closed sections, through (★). Then no world has a veto region.

*Proof.*

(V-own) at world i with index j. Let X be B on M_i and on M_j, A on M_k, and correct on U. X is incoherent by Lemma 0. By (★), some coherent C has C ⪯_w X at all w.
1. **World i.** On M_i, X is best for i. On M_j, X is worst for i (B is bad for a majority world). On M_k, X is best. So the record C→X has pattern (I or T, W or T, I or T) at i.
2. Every pattern with I on M_i is refused, by the veto or by strict (G). So C = X = B a.e. on M_i, and C = V_i by Lemma 0.
3. **World j.** V_i and X differ only on M_j, where V_i is A and X is B, the best advice for the minority world j. So X is a strict pointwise world-j improvement of V_i, and strict (G) refuses V_i ⪯_j X. Contradiction.

(V-maj) at world i with region f. Let X = AAA, that is, A on every mixed problem and correct on U. X is incoherent. Take C from (★).
1. **World i.** The record C→X has pattern (W or T, I or T, I or T) at i. A coherent C is never contradictory, and AAA is worst for i on M_i and best on the other regions.
2. The veto and strict (G) give C = A a.e. on M_f.
3. **World f.** On M_f, C equals X. On the two other regions, X is A, which is best for f as a majority world there. So X is a weak world-f improvement of C everywhere, and strict (G) at world f forces C = X, which is incoherent. Contradiction. ∎

**What it does not use.** Theorem V uses no (TC), no (IB), no keys, no gate and no verdict. It needs one veto at one world, together with strict (G) at one other world (j, resp. f).

### Corollaries

**Corollary 2.1 (AND; PROVED).** Suppose world i accepts a record iff each region-part is accepted by i's regional relation, and each regional relation satisfies regional strict (G) (as gate2d's does).
- **Acyclic.** In a cycle, a nontrivial step differs on some region. On that region the cycle is a cycle of an acyclic relation with a nontrivial step.
- **But it has a veto at every region.** The B-ward rival "C made B on small sets E_k ⊆ M_k, k = 1, 2, 3" has a pure own-region improvement at every world. So it beats every coherent model other than V_1, V_2, V_3.
- So the competitive coherent models are exactly the three vertex models. This is audit's Proposition 1 rival, now with bounded support in all three regions.
- CHECKED at pattern level: AND leaves 8 of 26 rival directions uncovered (`bitlevel.py`).

**Corollary 2.2 (lexicographic; PROVED).** Suppose world i decides on the first region (in a fixed order σ_i) where the record is nontrivial, using a regional relation with regional strict (G).
- Then σ_i's first mixed region is a veto region for i: (V-own) if it is M_i, (V-maj) otherwise. So (S) fails.
- Lexicographic composition of acyclic relations is acyclic: the earliest region touched by a cycle carries a cycle of its regional relation.
- So these lifts have (G), (IB) and (TC) for free, and still fail (S).

**Corollary 2.3 (PP4's Σ_loc; PROVED).** Row 5 of PP4 §4.1 says "foreign adds, own-class removes: refuse".
- The B-ward three-class rival out of a silent C_p has pattern (own I, W, W) at every world. So, read as a rule on that record, Σ_loc refuses it everywhere.
- PP4's "guidance covers it at a third world" holds only for two-class records.
- CHECKED in `bitlevel.py` §4.

### The mass-blind theorem

**Theorem M (mass-blind rules; PROVED by exhaustive enumeration).** Suppose each world's verdict on records that are trivial on U and pure on every mixed region depends only on the world's pattern, with (TC) and strict (G). Then:
- (a) the accepted mixed patterns at each world are contained in those of one of the six lexicographic region orders;
- (b) every world has a veto region, so (S) fails by Theorem V.

*Proof.*
1. **Reduction to patterns.** A triple of patterns (x, y, z) is realisable as a 3-cycle X→Y→Z→X by region-pure records iff, on each region, the three entries are all T or contain both W and I. For example, (I, W, W) means: improve on P_1 ∪ P_2, worsen on P_1, worsen on P_2. Any ranks are available, because the base model is arbitrary.
2. **Why every realisable triangle is a violation.** No accepted mixed pattern can have its swap (W ↔ I) accepted: x followed by its swap, refined to a sub-set, is a 2-step pump, and its triangle closes by guidance. Reverses of guidance links are strict improvements. So every realisable triangle among accepted and guidance patterns violates (TC).
3. **Enumeration.** I enumerated all 2¹² sets of mixed patterns. 265 are (TC)-safe, and the 6 maximal ones are exactly the lexicographic orders. All 265 have a veto region at every world.
4. **Monotonicity.** Veto conditions pass to subsets. (`bitlevel.py`, exact.) ∎

Covering is not needed in Theorem M. For the record, 90 of the 216 triples of maximal sets cover all 26 rival directions, and in all 90 some world puts its own region first (CHECKED).

## 3. Region-weighted rules

**Proposition 3.1 (sticky sums pump; PROVED, exact).** Let world i accept a region-pure record iff Σ_r w_r(2·added_r − removed_r) ≥ 0.
- X→Y: remove 2 on M_1 (a gain), add 1 on M_2. Accepted (2 − 2 = 0).
- Y→Z: remove that 1 on M_2, add 1/2 back on M_1. Accepted.
- Then Z is X improved by 3/2 on M_1. Guidance gives Z ⪯_i X, and strict (G) refuses X ⪯_i Z. So (TC) fails.
- (`weighted.py` (a).)

**Class R_w (linear region-weighted rules).** For each world i there are weights f_{i,r,j} > 0 (region r, level j) and a spread σ_i > 0. World i accepts a record that is trivial on U and pure on every region iff

> Σ f·(added steps) ≥ σ_i · Σ f·(removed steps),

with masses taken in ν = μ ⊗ counting.

**Theorem R (PROVED).** Let a system have its region-pure verdicts in R_w, with (TC) and strict (G). Let some coherent C be competitive on {1,2,3}, where on every region C is S on a non-null set and A on a non-null set (for example T1, or any D_K with K in the open simplex and int K ≠ ∅). Then:
- (i) σ_i = 1 at every world;
- (ii) the matrix B = (β_ir/α_i), with α_i = f_{i,i,2} and β_ir = f_{i,r,1} for r ≠ i, has Perron root exactly 1;
- (iii) at each world, every accepted record supported in at most two of the three mixed regions (and trivial on U) is endorsed: f_i(added) ≥ f_i(removed).

In particular, the gate2d sticky verdict (accept removed ≤ 2·added) cannot be used on any region, and every local comparison at every world is endorsed by one positive region-constant field.

*Proof.*

(i), lower bound: (TC) gives σ_i ≥ 1. Take the two-region pump of 3.1 with the rate σ_i. X→Y removes mass m on M_r and adds m' on M_{r'}; it is accepted iff f' m' ≥ σ f m. Y→Z undoes the M_{r'} part and re-adds m'' ≤ m on M_r; it is accepted iff f m'' ≥ σ f' m'. Then m'' = σ² m < m is possible when σ < 1, and Z strictly improves X.

(i)–(ii), covering.
1. **The A-ward rival.** Move C from S to A on P_r ⊆ M_r, with masses m_r. World i adds own level-2 steps (mass m_i) and removes foreign level-1 steps (masses m_r). It accepts iff m_i ≥ σ_i (Bm)_i.
2. **The B-ward rival.** Move C from A to S on Q_r, with the same masses. It hits the same step types in reverse. World i accepts iff (Bm)_i ≥ σ_i m_i.
3. **Collatz–Wielandt.** Write S = diag(σ_i). Then:
   - the A-ward rival is refused everywhere for some m > 0 iff ρ(SB) > 1;
   - the B-ward rival is refused everywhere for some m > 0 iff ρ(S⁻¹B) < 1.
4. **Conclusion.** Competitiveness of C needs ρ(SB) ≤ 1 ≤ ρ(S⁻¹B). Since S ≥ I, SB ≥ S⁻¹B entrywise. B is irreducible (positive off-diagonal), so if some σ_i > 1 the Perron root is strictly larger for SB, a contradiction. Hence S = I and ρ(B) = 1.

(iii), endorsement.
1. Suppose X ⪯_i Y is accepted, supported in at most two regions, adds A and removes B with f(A) < f(B). Let M_{r'} be a region it does not touch.
2. Put U_i(Z) := (U_i(X) ∩ U_i(Y)) ∪ C, where C is a set of steps on M_{r'} with f(A) ≤ f(C) < f(B). Then:
   - Y→Z removes A and adds C, so it is accepted;
   - Z→X adds B and removes C, so it is accepted;
   - X→Z removes B and adds C, so it is refused (σ = 1).
3. All three records are region-pure. So X ⪯ Y ⪯ Z ⪯ X is accepted without the reverse X ⪯ Z, which violates (TC). ∎

**Remarks.**
- **Checks.** `weighted.py` (b): 3,000 random weightings with some σ_i > 1 all left a rival uncovered. All 500 cases with σ = 1 and ρ(B) = 1 covered both rivals. (c) is the exact (TC) triangle against a sticky within-region record.
- **Direction-dependent rates (PROVED by the same computation).** Let the rates differ by trade type: σ^A_i for "own adds, foreign removes" and σ^B_i for the reverse type. The pump gives σ^A_i σ^B_i ≥ 1, and covering gives ρ(S_A B) ≤ 1 ≤ ρ(S_B⁻¹ B). Together these force σ^A_i σ^B_i = 1, that is, exact reciprocity: no spread at all on three-class trades.
  - Σ_loc's choice (σ^A = 1/2, σ^B = ∞) meets (TC) but fails the B-ward covering, as in Corollary 2.3.
- **Scope.**
  - Theorem R refines PP4 Prop 3.3 (triple-local Bayes). Adding the B-ward rival turns "some potential" into "exact reciprocity", with Perron root 1.
  - For position-dependent continuous weights, the same argument should run at Lebesgue points straddling C's S/A boundary (CONJECTURE).
  - Records with mixed parts in all three regions are not covered by (iii).
  - FF2 Thm 4.1 needs endorsement on an exhausting family of supports, so (iii) gives screen S4's hypothesis for local records but not FF2's literal one.

## 4. Where PP2 Theorem 6 bites (Q4)

**Proposition 4.1 (PROVED).** A lexicographic lift (Corollary 2.2) whose regional relations are identity, regional guidance or a regional weak (or strong) gate in a fixed regional key is a fixed-key weak gate in Thm 6's sense.
- **The global key.** Map each regional key increasingly into (0,1), and add the band offset 10·(position of the region in σ_i).
- **Why it works.** An accepted record has all its added steps on its first nontrivial region R at or below the removed steps of R, and every later region lies in a higher band. So ess inf(added) < ess inf(removed).
- **AND is a sub-relation.** AND's acceptances are lexicographic acceptances for every region order, so the same holds for AND.
- **The chain lift.** For the chain lift of §5, the world-1 key on the level-1 steps of M_1 is the switching time, which is not essentially constant. So Thm 6's hypothesis (H2) is met and (S) fails. This is consistent with Theorem V.

**Proposition 4.2 (the band edge; PROVED).** Take order (M_1, M_2, M_3) at world 1 and a cut c between the M_1-band and the M_2-band.
- Lemma 6.1's X_c is then B on M_1 (all keys below c), B on M_2 (world-1 rank 2), and A on M_3. That is exactly Theorem V's X.
- Lemma 6.1 needs only the weak gate at world 1 and strict (G) at world 2, so X_c must be selected. But it is incoherent outright. If M_2 comes first instead, the band-edge X_c is AAA. If M_3 comes first, the companion X'_c (A on M_2, with world 3) is AAA.
- So the contradiction does not need Thm 6's non-constancy (the strip argument). It arises already at a band boundary. R2's escape (a constant own-region key) does not save lexicographic lifts.

**Answer to Q4.**
- **Does the regional construction meet Thm 6's hypothesis?** Yes, as soon as the own-region level-1 key is not constant, and every chain-adapted key is not.
- **Do region-dependent keys help?** No. They are already allowed in Thm 6 and in Theorem V.
- **Do record-dependent keys help?** No, for any veto rule: Theorem V never looks at keys. The only way around is to give up every veto, at every world. Then the lift must accept, at each world i and for each region R, some records that purely improve i on R and are paid for elsewhere. Theorem M makes that impossible mass-blind, and Theorem R makes it additive when linear in region-constant weights.

## 5. A positive result: local defences along regionally nested chains (Q2)

**The chain lift Λ.**
- **Order and sides.** Fix the common order (U, M_1, M_2, M_3). On M_k the sides are {k} and {i, j}; the two majority worlds share key and verdict.
- **The chain.** C_t = D_{K_t}, K_t = (1−t)M + t e_1, t ∈ [0,1], with C_0 = T1 and C_1 = V_1.
- **Keys.** By Proposition 1.5, on each (region, side) membership of a step in U_side(C_t) is monotone in t, with a direction that depends only on (region, side). Let θ(g, j) be the switching time, and set the key to θ for decreasing sides and −θ for increasing ones.
  - Steps that never switch get keys 2 + τ(g) (always in) or −1 − τ(g) (never in). Contradiction steps get −2 − τ(g). τ is any function with null level sets.
  - Level sets are null: steps switching at time t lie over lines through a vertex of K_t.
- **The rule.** World w accepts X ⪯_w Y iff one of the following holds:
  - X = Y;
  - on the first region in the order where the record is nontrivial, w's side sees a pure worsening;
  - on that region, w's side sees a strong-gate pass with Φ = 2ν(added) − ν(removed) ≥ 0.

**Theorem C (PROVED).** Λ satisfies:
- reflexivity, strict (G) and (IB);
- no cycles at any world, hence (TC), antisymmetry and direct (C).

Every C_t is coherent, undominated, and competitive on {1,2,3} against every model, of bounded or unbounded support. No integrable f > 0 a.e. on rank steps endorses all world-1 comparisons out of chain members.

*Proof.*
- **(IB).** The first nontrivial region and the regional record depend only on the record.
- **Strict (G) and guidance.** The first nontrivial region of a pointwise weak improvement (worsening) carries a pure improvement (worsening). Regional strict (G) holds as in gate2d.
- **No cycles.** Use Corollary 2.2 together with gate2d's Lemma (acyclic) applied to each (region, side) key.
- **Competitiveness.**
  1. If the rival differs on U, every world sees a pure worsening, since C_t is correct on U.
  2. Otherwise, on the first region R: C_t is a threshold set of both sides' keys there, so by gate2d's Lemma (sep) every nontrivial added set passes the gate at both sides.
  3. If one side adds nothing, the other side sees a pure worsening.
  4. Otherwise the regional count of gate2d (V3) gives Φ_min + Φ_maj = a + b + 2c_min + 2c_maj ≥ 0, so some side accepts. All worlds on that side accept the whole record.
- **Undominatedness.** A model weakly better than C_t at all worlds would, on the first region where they differ, pass "into C_t" at both sides. The threshold property makes it pointwise weakly better at both sides. That is impossible for a different regular advice (rank pairs (0,2), (1,1), (2,0), (3,3)), as in gate2d.
- **Non-endorsement.** This is gate2d's Proposition (instance)(b) verbatim.
  1. The M_1-lines whose level-1 world-1 status switches in (0,1) form a non-null set, since T1 is not B on them and V_1 is. Pick a Lebesgue point g_0 of f(·,1) there, with switching time θ_0.
  2. Near g_0 the switching surface is a smooth hypersurface: the pencil through one far vertex of K_{θ_0}, times the radius.
  3. Let X_ε be C_{θ_0} silenced on Q_ε (B-side) and made B on R_ε (S-side), with μ(R_ε) = 2μ(Q_ε). The record lives only on M_1, passes the gate, and has Φ = 0, so it is accepted at world 1.
  4. Endorsement would give ∫_{R_ε} f ≤ ∫_{Q_ε} f, which is false in the limit. ∎

**Checks (finite cells, diagnostic; `chain_cells.py`).** 9 lines (3 per region), random masses, all 4⁹ = 262,144 models.
- 10 chain members, T1 included: 0 rivals refused at every world, and 0 dominating models.
- No 2- or 3-cycles among 234 models near the chain.
- Theorem V's X = (B, B, A) and AAA have no dominator among 232 distinct coherent profiles.
- Tripod-leg models (homothety toward e_2) are not competitive under the chain keys: 192 uncovered rivals each.

**Proposition 5.1 (the limit of the mechanism; PROVED).** Fix regional keys for which a chain member C is a threshold set on M_k, and let D be coherent with D crossed with C on M_k. Then:
- D is not a threshold set of either side's key on M_k: threshold sets of one key are nested, and the majority side's steps are complements of the minority side's with levels swapped.
- So D has crossed pairs at both sides. gate2d Proposition (three)'s rival (contradiction under one pair, side-good advice under the other) can be placed on small disjoint subsets of M_k. It is then bounded, and it defeats D at all three worlds.
- With fixed regional keys, the competitive coherent models therefore form a family that is pairwise nested on every region. By Proposition 1.4, a precise such family has empty interior. CONJECTURE: every regionally nested coherent family is at most one-dimensional.

**Answer to Q2.**
- **AND:** competitive coherent models are exactly V_1, V_2, V_3 (Corollary 2.1).
- **Lexicographic with no world's own region first:** the A-ward three-region rival defeats every coherent model with A-ward room on all three regions, in particular every K that meets the open simplex. In particular T1 is defeated.
- **Common order (or any order where a world's own region comes first) with chain keys:** exactly the regionally nested family is competitive against all rivals, bounded and unbounded (Theorem C, Proposition 5.1).
- **"Models whose regional projections are two-world selected intervals":** with one index common to all pencils of a region, this is a regionally nested family, so the answer is yes for its members. But such families are chains, not two-dimensional.

**Answer to Q3.** KKM dominators fail for every veto lift: Theorem V's X = (B on M_i, B on M_j, A on M_k), or AAA. These are exactly rivals whose regional changes pull in different directions. Under linear region weights, the A-ward and B-ward three-region rivals can both be covered only on the knife edge σ = 1, ρ(B) = 1 (Theorem R).

**Relation to audit's two-model test (AUDIT_local_defences §6).**
- Theorem C gives T1 and every C_t (t ∈ (0,1]) all of the following:
  - coherent and undominated;
  - competitive against every measurable rival, including the bounded rivals of audit's Proposition 1;
  - record-based, with (G) and (TC) holding for all copies;
  - non-additive defences that are actually used.
- It is uniform over a one-parameter family. The same works for the rays toward e_2 and e_3, one at a time, and for any regionally nested chain.
- The defence rule is a property of record classes, as in observation 1 of Brief 46. Every model with the same advice on D as a chain member shares its defences.
- What it does not do is audit's extension step: adjoining a model crossed with the chain on some region breaks it (Proposition 5.1), and (S) is excluded (Theorem V).

## 6. T1 (Q5)

- **(a) Projections.** Each pencil projection ψ_s(M) is an interval, so on each pencil T1 is a two-world interval model. But T1's M_1 profile is fixed by v_1 and the facet [v_2, v_3]. It is not an interval of either edge coordinate, nor of any single coordinate (Proposition 1.3(c), CHECKED).
- **(b) Local defences.** T1 = C_0 of the e_1-homothety chain, so Theorem C gives T1 full local defences against every model, with non-additive defences. The same holds along the e_2- and e_3-chains, one chain at a time. The three cannot be served together with fixed regional keys, because the legs cross (Proposition 1.5).
- **(c) Selection.** T1 is not selectable under any veto lift (Theorem V), under any mass-blind lift (Theorem M), or under a lexicographic lift without an own-region-first world (the A-ward rival defeats it). Under a linear region-weighted lift, T1's competitiveness forces σ = 1, ρ = 1 and additivity on two-region records (Theorem R).

## 7. What a regional lift would still have to do

The results fix the shape of anything that survives.

1. **No veto, anywhere (Theorem V).** At every world i:
   - for every j, some record purely improving i on M_i, worsening on M_j, and improving or not touching the third region must be accepted;
   - for every f ≠ i, some record purely improving i on M_f, worsening on M_i, and improving or not touching the third region must be accepted.
2. **Mass-sensitive in both directions (Theorem M).** No pattern rule works. Cross-region trading must depend on masses.
3. **Not linear with region-constant weights (Theorem R).** Otherwise there is exact reciprocity, and additivity on two-region records.
   - What remains: position-dependent cross-region rates (my CONJECTURE: excluded the same way at Lebesgue points), non-linear tests on three-region records (PP4 Thm 3's polyhedral hypothesis then matters), or region priorities chosen from the record's masses (PP2's (E1) at the region level).
   - None of these reduces to "gate2d on each region". In each, (TC) must be designed directly, which is the open route (a) of the design memo.
4. **Nearby targets I would propose.**
   - **(N1)** Keep Theorem C as the local-defence module for one chain through T1. It is complete for that purpose.
   - **(N2)** Screen record-dependent region priorities against Theorem V. A world escapes a veto only if its priority can put a later region first when the masses demand it. That makes the priority mass-dependent, so test it for pumps with PP4 Lemma 2.4 before any construction.
   - **(N3)** Decide the CONJECTURE in Proposition 5.1. If every regionally nested family is one-dimensional, then no fixed-key regional mechanism can defend a two-dimensional selection, even locally. Local defences for every selected model (the brief's aim) would then need keys that differ by record within a region, with (TC) re-proved from scratch.

## Scripts (`PP26_py/`)

| Script | What it does | Label |
|---|---|---|
| `bitlevel.py` | Enumerates all mass-blind pattern rules: 265 (TC)-safe sets per world, maximal = the 6 lexicographic orders, every safe set has a veto region; AND/OR/lex sanity checks; Σ_loc leaves the B-ward rival uncovered | PROVED (exact enumeration) / CHECKED |
| `regions.py` | Equal edge projections with different M_1 profiles; pencil formula; median rule for precise pairs; T1 has no product maximum; homothety chain monotone at every world; tripod legs crossed on M_3 | CHECKED (exact, except the sampled nesting test) |
| `weighted.py` | Sticky region sums pump; Collatz–Wielandt covering test over 3,000 random weightings; exact endorsement triangle | CHECKED / NUMERICS (LP) |
| `chain_cells.py` | Chain lift on 9 cells, all 262,144 models: competitiveness, undominatedness, no short cycles, no dominator of (B,B,A) or AAA, failure of a tripod leg | NUMERICS (diagnostic) |
