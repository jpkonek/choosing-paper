# SCREEN_P3. Pair-indexed proper scoring (memo §7, Proposal 3), two worlds first

20 Oct 2026. Rules of BRIEF_DESIGN1. Labels:
- **PROVED**: full argument here (one reader, me; not refereed).
- **CHECKED**: an import read step by step, or a standard fact.
- **CONJECTURE**.
- **NUMERICS**: exact-rational scripts in `screenP3_py/` (`python3 -I <script>` inside that folder). Nothing rests on them.

No assumption is added to the programme. Hypotheses that belong to one result are stated there.

**Refocus (author, via coordinator), adopted throughout.** A Bayes-adapted ℓ^m (C_m the m-Bayes model) is exactly an LP-CPM error loss at the single prior m, and the author does not want the scheme to fall back into the LP-CPM realisation programme. So this note does **not** use "decoding p" or Bayes-adaptedness.
- ℓ^m is **any** family of strictly guiding additive penalties with integrable envelopes. It is a parametrised source of record-wise verdicts.
- Competitiveness is read record by record: under (IB) it asks only that the base side of t win at some active world under ℓ^{m(t)}. That verdict is the same for every selected model with that local advice.

(The earlier observation, that any m(t) whose C_m agrees with the base side on the changed set gives competitiveness, so that touching a boundary is irrelevant, is one sufficient route. It is not used below.)

---

## 0. Verdicts

1. **Record-wise competitiveness is free (PROVED, Lemma 2.1).**
   - For every record out of a selected base there is a strictly guiding additive penalty under which the base wins at an active world, strictly.
   - When both sides are selected, one penalty makes both bases win.
   - So (S)-competitiveness and direct (C) never bind on their own. **(TC) and closed sections are the whole problem.**
2. **(TC) has an exact form.**
   - *Symmetric rules* (m(t) depends on the unordered record): every pair is comparable, so **(TC) ⟺ transitivity** (Prop. 3.1, PROVED).
   - With a rich family, symmetric P3 rules are exactly the (IB), strictly guiding **total preorders**. The scheme then lands in the write-up's "total world" class.
   - *Ordered rules*: (TC) is strictly weaker. It needs orientation sign-consistency (Prop. 3.4, PROVED necessary).
3. **Anchoring collapse (Thm 3.2, PROVED; any number of worlds; any (IB) rule, not only P3).**
   - Hypothesis: for **one** model C and one additive ℓ, the world's verdicts on records out of C that contain a fixed small "anchor" pattern are exactly ℓ's (that is, m(t) is locally constant there).
   - Conclusion: (TC) forces ℓ to endorse **every** comparison on small records away from the anchor. For complete rules the world *equals* ℓ there.
   - If every score the rule uses anchors somewhere, the world is globally the single additive loss ℓ (Cor. 3.3).
   - Exact (TC) failure: `tc_instance.py`, two FC-type scores on chained records. It is the same mechanism as the splicing 3-cycle.
4. **Answer to the author's (b).**
   - *If m(t) is locally constant near a selected model, yes: the collapse is not merely to a local single-loss (CPM-type) problem but to one global additive loss* (Thm 3.2 + Cor. 3.3). In two worlds it is then additive (S1). In three worlds it is excluded for T1 by gm.
   - Whether (TC) + closed sections *force* local constancy is **not settled**. m(t) itself is never identified; only the verdicts are.
   - Escape requires that **no** model have an anchored constant score. For symmetric rules it also requires a total (IB) world that is not almost representable: Cor. B32 and Thm E3 (imports, CHECKED) make every AR total world add up. In two worlds with a nested selection, complete worlds add up.
   - The natural record statistics do not escape:
     - argmax_m P_m(h_t) always picks a **vertex** (PROVED; NUMERICS `argmax_vertex.py`), so it is a two-score rule and anchors.
     - σ(v) is continuous in h_t: "approximately anchored", CONJECTURE that it collapses.
5. **Non-additivity (Q3).**
   - Formally the scheme escapes S3 (a continuum of scores) and S8 (the accepted set is not convex).
   - Anchoring (call it **S9**) is stronger than both for this class. With an anchor the system is merely additive. Without one it is an unscreened total or ordered world.
   - No finite certificate of genuine non-additivity is available in any (TC)-consistent instance found here.

---

## 1. Setting

**Domain and target.** Two worlds, t := p_1, full four-advice domain, Gaussian μ.
- Mixed problems are g = (a, −b), a, b > 0, with τ = b/(a+b).
- C_p = D_{[l(p),u(p)]} with l ≤ p ≤ u, continuous, with precise vertices. It advises:
  - + if τ < l;
  - 0 if l < τ < u;
  - − if τ > u;
  - + on unanimous problems.
- Example family: FC v3 with width 1/3, K_p = [max(0, (4p−1)/3), min(1, 4p/3)], through K* = [1/3, 2/3].

**Rule P3.** A record t = (N, a, b) is the changed set N with the old and new advice on it. Write Δ^m_i(t) := ∫_N [ℓ^m_i(h, b) − ℓ^m_i(h, a)] dμ.
- Ordered P3: X ⪯_i Y iff Δ^{m(t)}_i(t) ≥ 0, where t = rec(X → Y).
- *Symmetric* P3: m(t) = m(t̄), where t̄ swaps old and new.

**FC_w (scripts).** Mixed problem, a + b = 1:
- + ↦ (0, b);
- 0 ↦ (c, c), with c = ab/(1+w);
- − ↦ (a, 0);
- × ↦ (2a, 2b).

---

## 2. Design checks

**(IB). PROVED.** The verdict is a function of t.

**Strict (G). PROVED.** A pure world-i improvement has Δ^m_i < 0 for every strictly guiding ℓ^m, whichever m either orientation uses.

**Ties.** Per-world ties between distinct models occur, so the memo's "no ties" is false (CHECKED).
- For a record with an improvement on S₁ and a worsening on S₂, choose masses with Δ^m_1(t) = 0.
- Such ties are harmless except through direct (C).

**Lemma 2.1 (record-wise winnability; PROVED).** Let t = (N, a, b) with a = C|N for a coherent D_K, and b ≠ a on N.
- (a) Some strictly guiding additive ℓ gives Δ_i(t) > 0 at some world i, so the base wins strictly. If K is a vertex model W_i, every ℓ does so at i.
- (b) If b = C'|N for a second coherent model as well, some single ℓ gives Δ_1 Δ_2 < 0, so each base wins at one world.

*Proof.* If b is a.e. weakly world-1-better than a, then it is a pure world-1 improvement.
- Coherent bases give + on unanimous problems, where no improvement exists. On mixed problems every world-1 improvement out of {−, 0, +} is a strict world-2 worsening.
- So Δ_2 > 0 for every ℓ.
- Otherwise b is world-1-worse on a non-null set R. Taking ℓ_1 large on R gives Δ_1 > 0.

For (b), choose ℓ_1 and ℓ_2 separately in the same way, with roles reversed at world 2. ∎

**Consequences.**
- Competitiveness of every selected model, and the exclusion of double ties X ≈ C_p (which, with (S) and HH1 Prop. 1(c), CHECKED, gives direct (C)), can always be arranged *record by record*.
- Every constraint therefore comes from consistency across records: (TC) and closed sections.

**Closed sections (PROVED, partial).**
- If p ↦ m(rec(C_p, X)) is continuous, and m ↦ ℓ^m is continuous in L¹ under the envelope, then {p : C_p ⪯_i X} is closed, by dominated convergence and continuity in measure of the selection.
- Rules whose score switches when a record gains or loses contact with a region (§3.3) have sections that can jump. Under the collapse of §3 the sections are those of one additive loss, hence closed.

---

## 3. (TC)

### 3.1 Symmetric rules

**Prop. 3.1 (PROVED).** For symmetric P3, every pair is comparable, and (TC) at world i ⟺ ⪯_i is transitive.
- If the family is rich (it can up-weight any region at either world, for instance ρ(h)·FC_w with ρ > 0 arbitrary), then the symmetric P3 worlds satisfying (TC) are exactly the (IB), strictly guiding total preorders.

*Proof.*
- Comparability: Δ ≥ 0 or Δ ≤ 0.
- For complete relations, "not C ≺ A" is equivalent to "A ⪯ C", so (TC) is transitivity.
- Converse: take any (IB) strictly guiding total preorder, and a record that is not pure. Lemma 2.1's construction gives a strictly guiding ℓ with Δ of either prescribed sign. Ties are handled by a convex combination of the two, which is again strictly guiding. Let m(t) index it. ∎

So for symmetric P3 the index m(t) carries no information beyond the verdict. Whether a "non-additive" P3 exists is exactly whether a suitable total (IB) world exists. That is the write-up's total-world question (§4).

### 3.2 Anchoring

**Anchors.** Fix a world i, a model C and an additive strictly guiding ℓ. An *anchor* is a pair of disjoint sets V and R₀ such that:
- V is a set with advice v ≠ C|V on it;
- R₀ is a region on which C is not world-i-best;

and, for every Y with Y|V = v and Y = C off V ∪ R₀ ∪ G (G disjoint from V ∪ R₀), the relations C ⪯_i Y and Y ⪯_i C hold exactly as under L = ∫ℓ_i.

In P3 terms: m(t) is constant (up to positive scale plus per-problem shift of ℓ_i) on the records out of C that carry the pattern (V, v), whatever else they contain.

**Theorem 3.2 (anchoring collapse; PROVED).** Assume (IB), strict (G) and (TC) at world i, and an anchor (C, ℓ, V, R₀). There is η > 0 such that for every record (E, x, z) with E disjoint from V ∪ R₀ and ∫_E e dμ < η (e the envelope of ℓ_i), and all X, Z with that record:

X ⪯_i Z ⟹ L(X) ≤ L(Z).

So ℓ_i endorses every such comparison. If ⪯_i is complete on these records, then X ⪯_i Z ⟺ L(X) ≤ L(Z).

*Proof.*
- **Achievable compensation.** As W ranges over subsets of R₀ and w over advice, d_W := ∫_W [ℓ_i(w) − ℓ_i(C)] covers an interval [−A₀, B₀] with A₀, B₀ > 0 (Lyapunov). Let d_V := ∫_V [ℓ_i(v) − ℓ_i(C)]. Take η := min(A₀, B₀)/3, with V chosen so that |d_V| < η.
- **Construction.** Given (E, x, z), put X := x on E, v on V, w on W, and C elsewhere. Define Z in the same way with z. By (IB), the verdict between X and Z depends only on (E, x, z).
- With D_X := ∫_E [ℓ_i(x) − ℓ_i(C)] and D_Z defined in the same way:
  - L(X) − L(C) = d_V + d_W + D_X;
  - L(Z) − L(C) = d_V + d_W + D_Z.
  - Every value of d_V + d_W in [−2η, 2η] is available, and |D_X|, |D_Z| < η.
- **Suppose L(X) > L(Z), i.e. D_X > D_Z, and X ⪯_i Z.** Choose d := d_V + d_W with −D_X < d ≤ −D_Z.
  - Then L(Z) ≤ L(C) < L(X) relative to C. These records are anchored, so Z ⪯_i C, C ⪯_i X and not X ⪯_i C. Hence C ≺_i X.
  - The triple X ⪯_i Z ⪯_i C with C ≺_i X violates (TC).
- **Completeness.** If ⪯_i is complete and L(X) ≤ L(Z) but not X ⪯_i Z, then Z ≺_i X.
  - Choose d with L(X) ≤ L(C) ≤ L(Z) relative to C.
  - Then X ⪯_i C ⪯_i Z (anchored) and Z ≺_i X, again violating (TC). ∎

*Remarks.*
- Only (IB) is used to make the X–Z verdict independent of V, W and C. The theorem therefore applies to every record-based rule: Proposal 2's μ_t, quorums, transition pricing. It explains, for example, why Screen C's survivors are endorsed by ρ′.
- It is a statement about **one** model and **one** pattern.

**Corollary 3.3 (global collapse; PROVED).** Let a symmetric P3 world satisfy (TC). Suppose every score ℓ^m that it uses anchors at some model, and that some small set G is disjoint from the anchors of two given scores. Then:
- ℓ^m_i(h, b) − ℓ^m_i(h, a) = κ_{mm′}(ℓ^{m′}_i(h, b) − ℓ^{m′}_i(h, a)) for a.e. h and all a, b, with κ_{mm′} > 0;
- ⪯_i is the additive ranking of any one ℓ^{m₀}_i on *all* records.

*Proof.*
- By Thm 3.2, the two scores agree in sign on all small records inside G.
- By Lyapunov, the joint integrals (Δ^m, Δ^{m′}) over sub-records of G form a convex set that is symmetric under swapping old and new. It avoids the open second and fourth quadrants. So it lies on one line. Its slope is positive and finite, by strict (G) on pure records.
- Cover a.e. h by countably many such G; the slopes agree on overlaps.
- The verdict on any record is the sign of some Δ^{m(t)} = κ Δ^{m₀}. ∎

Bayes-adapted P3 on an injective family satisfies these hypotheses: a record touching both boundaries of C_p pins the score. So that version collapses to one additive loss, the case the author wants to avoid. It also forces a nested selection in two worlds, since a Bayes family of one additive loss is comonotone (CHECKED).

### 3.3 Exact (TC) failure on chained records (NUMERICS, exact; `tc_instance.py`)

**Ingredients.**
- Rule: on records meeting the anchor V use A = FC_{1/4}; on other records use B = FC_{1/3}.
- Anchor: V consists of the sectors adjacent at τ = 1/4.
- C = C_{3/16} = D_{[0,1/4]} from the FC v3 family. It is FC_{1/4}-Bayes at weight 1/5, CHECKED on all cells, so its base side wins on the anchored records.

**Record E.**

| cell | τ | mass | X | Z |
|---|---|---|---|---|
| E₁ | 1/10 | 1 | 0 | + |
| E₂ | 9/10 | 23/10 | 0 | − |

At world 1:
- L₁(Z) − L₁(X) = −19/2500 under A;
- L₁(Z) − L₁(X) = +29/4000 under B.

**Anchor and compensation.**
- On V: C gives (0, −), while X and Z both give (−, 0). This is a non-monotone pattern, so X and Z are not coherent there.
- W is at τ = 1/20 with mass 299/4000.

**Outcome at world 1.**
- Z ⪯₁ C and C ⪯₁ X, both under A;
- X ≺₁ Z under B.

So (TC) fails. Every inequality has slack, so it survives replacing the cells by thin sectors.

**Mechanism.** This is the splicing 3-cycle's mechanism: the two edges through C are judged in C's context, and the closing edge in another context. Theorem 3.2 shows the failure is unavoidable whenever the two contexts disagree in sign on any small record.

### 3.4 Ordered rules

**Prop. 3.4 (PROVED, necessary condition).** Let A ⪯_i B with record t. Let C_S be A improved at world i on a small set S, and t_S := rec(B → C_S).
- If Δ^{m(t_S)}_i(t_S) ≥ 0 for some S, then (TC) fails. (C_S ≺_i A holds by (G).)
- So if m(t_S) → m′ as S → ∅, (TC) needs: Δ^{m(t)}_i(a → b) ≥ 0 ⇒ Δ^{m′}_i(a → b) ≥ 0. That is, the scores used in the two orientations must agree in sign with slack.

**What is not covered.** Ordered rules can have incomparable pairs, and Theorem 3.2 needs both orientations anchored. A *base-indexed* rule escapes it formally: X ⪯ Y is scored by an index read from X's local advice, so out-of-C and into-C relations use different scores.
- CONJECTURE: base-indexed rules whose index is anchored in both bases collapse in the same way.
- Sketch: Prop. 3.4 plus Lyapunov, applied to the affine family "anchor patterns + small free records", gives proportionality of the two scores.

---

## 4. Local constancy, the author's (b), and non-additivity (Q3)

**Does (TC) + closed sections force m(t) to be locally constant near selected models?**

- **As posed, no.** m(t) is not identified, since any score with the same sign gives the same verdict (Prop. 3.1).
- **The right form is anchoring.**
  - If the verdicts out of *any one* model are those of one loss on a cofinal family of records (anchored), Thm 3.2 and Cor. 3.3 give a collapse.
  - The collapse is not to a local single-loss problem but to **global** sign-agreement with that loss on small records, and to global additivity for symmetric rules.
  - That is stronger than the LP-CPM reduction the author wants to avoid.
- **Whether (TC) + closed sections force an anchor is open.**
  - For symmetric rules this is the total-world question.
  - Cor. B32 (CHECKED import, on M_U, preorders): a total, (IB), strictly guiding world with (S) that is almost representable (AR) adds up.
  - Thm E3 (CHECKED import): two worlds, nested selection, complete ⇒ adds up.
  - Cor. MC (CHECKED import): a non-nested two-world system needs both worlds to lack monotone continuity and a leading charge.
  - All three apply verbatim to symmetric P3 + (TC), since those worlds are total preorders.
- **Escaping mechanism, as far as it can be named.** Verdicts out of every model must depend on the rival's change at every scale, so that no pattern pins the score; and the total order must be non-AR (a non-fine qualitative probability on error sets).
  - Lexicographic rules (score switching on ties) do not escape: they are endorsed by their first level, and S3 and M0closed exclude them for T1.
  - No escaping instance is known.

**The natural record statistics.**
- **argmax_m P_m(h_t).** P_m(h) = h₂ + (h₁ − h₂)·(l(m) if h₁ > h₂, else u(m)). So the argmax is the vertex 1 when h₁ > h₂ and 0 when h₁ < h₂ (PROVED; NUMERICS `argmax_vertex.py`, two families, 0 violations).
  - The rule is therefore "ℓ^1 or ℓ^0 by the sign of h₁ − h₂". A pattern with dominant |h₁ − h₂| anchors each score, so by Thm 3.2 and Cor. 3.3 (TC) forces ℓ^0 ≅ ℓ^1, which is additive (PROVED in outline: the anchoring pattern's ℓ-cost must be compensable, which holds for small E).
  - With the natural vertex scores FC₀ it also fails competitiveness: D_{K*} silent at τ = 2/5 and 3/5 is beaten at both worlds for mass ratios in (2/3, 3/2) (CHECKED by hand: FC₀ is precise scoring).
- **σ(v).** It is continuous in h_t, so no pattern pins it exactly.
  - CONJECTURE: a limiting form of Thm 3.2, using continuity of m ↦ ℓ^m, gives the same collapse.

**S3 and S8.**
- Both are formally escaped: there is a continuum of scores, and the accepted set is not convex.
- S9 (anchoring) is the operative screen for this class.

---

## 5. Three worlds and T1 (Q4)

Theorem 3.2 and Corollary 3.3 are per world and do not use n = 2.

**What collapses.** Any P3 cover of T1 whose scores anchor (in particular every Bayes-adapted, decoding version) is an additive ranking, and so is excluded by Theorem gm. Pair-indexing evades gm only if no world has an anchored score at any model.

**Symmetric P3 in three worlds.** The worlds are total (IB) preorders, so a cover needs a total world that does not add up. By the last clause of Cor. B32 under (H_U), that world is non-AR, and some edge family at e_i is non-nested.

**Decoding in three worlds.** Faces add a second issue: a record out of an edge model can be consistent with interior models, so a decoded score need not make the base win inside supp p. Lemma 2.1 avoids this by choosing the score record-wise.

**First obstruction to check for any refined proposal:** does any selected model have an anchor, that is, a pattern fixing the score on all records containing it? If yes, the proposal is additive.

---

## 6. Files

- `screenP3_py/tc_instance.py` → `tc_instance.out`: the exact (TC) failure of §3.4, with the Bayes check of C on the cells.
- `screenP3_py/argmax_vertex.py` → `argmax_vertex.out`: argmax_m P_m(h) is a vertex (FC v3 family, and a non-nested bump family).
