# Referee report on J1_notes.md (conflict cycles, near-Bayes models, pattern switching)

15 Oct 2026, round 19. Adversarial reading against:
- H1_notes, H2_notes, H12_referee (including Prop. R.1), E1_notes, F2_notes;
- write-up "The Contamination Triangle.tex": §§2–3, §7.7 (Thm. M0closed), §8.5 (f′) "Round 17, note J1" block and (g).

Labels as in BRIEF13: **PROVED** (full proof here), **CHECKED**, **NUMERICS**. Scripts are in `j1ref_py/` (run with
`python3 -I`); no verdict rests on them. No assumption is added. Notation is that of J1: (J) = (EP) of the write-up,
Π^k_m = ⋃_{S∈𝒮_k} S_m, D_m = ⋃_k Π^k_m, ψ = (ρ_kμ)_k, d_t = Φ*_t, δ_k = 1_{E_kX} − 1_{E_kC}.

## 0. Verdicts

| Item | Verdict |
|---|---|
| Near-Bayes tool (Steps A–C): X = B_t off D_m, arbitrary on D_m; Φ(X) ≤ ∫_{D_m}Σρ_k; use of H1.0(c) | **CORRECT** |
| Lemma J1.0 (closure) | **CORRECT** |
| Theorem J1.1 (H2.3 without (h′)) | **CORRECT**. It is H12_referee Prop. R.1, proved independently by the same model. One depth detail, the same as H12_referee §2.4 (§2) |
| Theorem J1.2 (pattern switching) and the alignment hypothesis (Al) | **CORRECT** |
| Pairwise sufficient condition (i)–(iii) | **CORRECT** |
| J1.3(a) (H2 §5.1 template) | **CORRECT**. Stronger than stated: the hypothesis 𝒮₂ ⊆ {A, B} is unnecessary (§4.1). "At every t" is automatic |
| J1.3(b) | **CORRECT** (⊑ should be defined in §1) |
| J1.3(c) | **CORRECT** with a **one-line GAP (fixable)**: "S is a T1-wrong end of i" omits the case S T1-correct at i, which is case (i) (§4.3) |
| Example J1.4 (cap inside tube) | **CORRECT at CHECKED level**. Radii must start small enough that the sets lie in U ∩ O; the claim that two such pairs escape J1.2 is right when 𝒮_l = ∅ (§5) |
| Proposition J1.5 (shells) | **CORRECT**, with the same one-line gap as J1.3(c) (§6) |
| §4.2, the three failed repairs | **CORRECT as descriptions**. No impossibility is claimed, and none follows. (γ) yields a small proved by-product (§7) |
| Question J1.Q, wording "for every integrable admissible ψ" | **GAP (wording)**. J1.5 holds only for ψ with (b). Same defect as H2 §5.2 (H12_referee §2.6) |
| J1.Q, "if no, then no cover with finitely many end-protected worlds and integrable base endorsers" | **GAP: the inference is unproved**. The editor's flag is right. A negative answer closes only Γ = (2-cycle + isolated third world). The rest of (EP) is narrowed here by a new Theorem R.2 and Corollary R.3 (PROVED, §8) |
| §0, "no conflict cycle survives if one of its arrows is aligned" | **GAP (overstated)**. Proved in J1 only for 2-cycles with 𝒮_l = ∅. True for pure 3-cycles and for 2-cycles with an isolated third world by R.3. Not true as a consequence of R.2 for larger Γ (§8) |
| §5, why p ⊆ O is needed in H2.1(b) | Minor misattribution (§9) |

Net:
- Nothing is WRONG.
- The near-Bayes tool, J1.0, J1.1 and J1.2 are sound and are a real advance: the template of H2 §5.1 is closed.
- The headline consequence attached to J1.Q overreaches. The precise residual is stated in §8.4.

---

## 1. The near-Bayes tool (Steps A–C): CORRECT

**Step A (admissibility).**
- D_m is decreasing, contained in M (ends are subsets of M), and μ(D_m) → 0 (finitely many ends, finite μ).
- A comparison T1 ⪯_k Y with Y regular and Y = T1 on D_m is relevant (T1 ∈ C_L). Its vector vanishes on every S_m
  with S ∈ 𝒮_k, so it is base and is endorsed by (b). For integrable ρ_k the cancellation and total-cost readings
  coincide, so H1.1 applies as stated.
- I re-checked H1.1 steps 1–5 against H12_referee §1.3. They are as J1 says.

**Step B.**
- I_ψ is non-null: Tonelli gives null ties for a.e. t, and M0closed(a) (write-up §7.7, no integrability used) excludes
  coherent B_t for a.e. t.
- d_t > 0 by H1.0(a).

**Step C.**
- Regularity: D_m ⊆ M, so X = B_t on N₊, and B_t ⊇ N₊ a.e. because t·c > 0 there.
- The bound: X △ B_t ⊆ D_m and |t·c| ≤ Σ_k t_kρ_k ≤ Σ_kρ_k. So Φ(X) ≤ ∫_{D_m}Σρ_k.
- **This bound is uniform in the pattern on D_m.** That uniformity is what lets one fix m (after t) before choosing
  the pattern, and the whole of J1 relies on it.
- ψ_k(E_kX) < ∞ by integrability.
- Thm. kkm gives a selected undominated C ∈ C_L with C ⪯_k X for all k. It is coherent, and all three comparisons are
  relevant.
- H1.0(c) applies: X is regular, Φ(X) < d_t, costs are finite, C is coherent, and (R) holds for integrable ρ. So some
  comparison is unendorsed, hence not base by (b).

**Novelty.** Prop. R.1 (H12_referee) and H1.3 already used X = T1 on the deep ends. The new content is that *any*
pattern on D_m is admissible.

## 2. Lemma J1.0 and Theorem J1.1: CORRECT

**J1.0.**
- δ_k(g) = 0 iff g ∈ X ⟺ g ∈ C, since both models lie in U and E_k(·) at g depends only on membership and σ_k(g).
- End-protection is a disjunction over the whole family. So "δ_k ≤ 0 on S_{a_S} for every S" is exactly what is
  needed to exclude S-positivity everywhere and force "eventually ≥ 0 on every S".
- Finiteness gives the uniform m′.

**J1.1.** This is the statement and proof of Prop. R.1. Two details need care.
- m must exceed the T1-purity depth of every end. Then X = T1 is k-correct on S_m for T1-correct S (finitely many
  ends, so harmless).
- **The arrow i → l needs μ(W_M ∩ S_M) > 0 for every M.** The note covers P ∩ W_{j(M)} by the S_M. Take
  j(M) ≥ M; this is allowed, since the covering inclusion persists when j is raised. Then the needed set contains
  P ∩ W_{j(M)} ∩ S_M. This is the "trivial adjustment" of H12_referee §2.4, and the write-up already records it.

On P ∩ S_M (M ≥ m), X = T1 is l-correct. C gives the advice opposite to T1, because C is i-correct where T1 is i-wrong
(depth ≥ purity of W). So δ_l = −1 there. The rest re-derives.

## 3. Theorem J1.2 and (Al): CORRECT

**The quantifier order is right:**
- (Al) depends only on the ends and the signs, not on t or C;
- t is fixed first, then m (large, with (Al) and ∫_{D_m}Σρ < d_t);
- then C, then M = m′(C), which is arbitrary, and (Al) is required for *every* M;
- then j, which may be raised freely, so j ≥ m and Π^{k_s}_j ⊆ Π^{k_s}_m.

**The three cases of step 2.**
- Since g ∈ Π^{k₂}_m, r_m(g) ∈ {1, 2}.
- If r_m(g) = 2, or the signs agree, X is k₂-correct and δ ≤ 0.
- Otherwise g ∈ B²_m, so g ∈ Π^{k₁}_{m′₁}, where C = X.

**Step 3** uses Π^{k_q}_M ⊆ Π^{k_q}_{m′_q} for M ≥ m′_q. An empty family at k₁ or k₂ is harmless.

**Pairwise condition.**
- For g ∈ Π^{k_s}_j ∩ B^s_m, g lies in S′_j ∩ S_m with S ∈ 𝒮_{k_{r_m(g)}} and S′ ∈ 𝒮_{k_s}.
- Ends in different orthants are disjoint beyond the purity depths.
- The sign conflict at g is a sign conflict on the common orthant.
- (i) needs m ≥ j₀, which J1 imposes. (ii) and (iii) need j large. Finitely many pairs.

**The H2.1(b) supply of (ii)** is correct. A world of V(S′) with 𝒮 = ∅ makes the covering empty, so such S′ cannot
exist.

## 4. Corollary J1.3

### 4.1 (a): CORRECT, and stronger than stated

**Order (1, 3, 2).** World 3's ends are A and B, which are also world-1 ends, so S′_j ⊆ S′_M ⊆ Π¹_M for j ≥ M: this
is (ii). The concrete description (accept deep A, reject deep B; C copies X there; then δ₃ = 0 and δ₂ = 0 deep) is
accurate.

**Strengthening (PROVED): 𝒮₂ may be any finite refined family.** In order (1, 3, 2), world 2 is last. Check the pairs
(S ∈ {A, B}, S′ ∈ 𝒮₂) on conflicting orthants:
- **S′ T1-wrong at 2.** V(S′) ⊆ {1, 3}, both earlier, so (ii) holds by H2.1(b).
- **S′ T1-correct at 2.** The only conflicting pairs are:
  - A (in (+,+,−), conflict with world 3);
  - B (in (−,+,+), conflict with world 1).

  As ends of the earlier conflicting world, A is T1-correct at 3 and B is T1-correct at 1. So both members of the pair
  are T1-correct at worlds of opposite sign. Hence they are eventually disjoint: case (i).
- World 1's T1-wrong end A sits where σ₁ = σ₂, and world 3's T1-wrong end B where σ₃ = σ₂. So no pair needs (iii).

**"For every t ∈ I_ψ".** This is automatic and should be reworded. J1.2 contradicts (H_U) itself, so one t suffices.
The correct statement is: "the template is inconsistent with (EP)".

### 4.2 (b): CORRECT

S′ ⊑ S with S in an earlier world gives (ii) for every order. The symbol ⊑ ("∀M ∃j: S′_j ⊆ S_M") is used but never
defined in J1. Define it in §1.

### 4.3 (c): CORRECT up to one line (GAP, fixable)

In the second bullet, "S′ T1-correct at j ⇒ S is a T1-wrong end of i" is not literally true. T1's advice varies
within an orthant, so S may be a T1-correct end of i elsewhere in O.

**Fix.** If S is T1-correct at i, then beyond the purity depths T1 is i-correct on S_m and j-correct on S′_m, with
σ_i ≠ σ_j on O. So S_m ∩ S′_m is null, which is case (i). Only T1-wrong S needs the hypothesis (iii).

(This is also the reason why, in the write-up's (g), "for a 2-cycle next to a world without ends, no aligned order ⟺
both arrows misaligned" is an exact equivalence. With 𝒮_l = ∅ the conflict set B²_m ∩ Π^j_n is exactly the union of
the pair pieces, so (Al) for (i, j, l) is equivalent to alignment of i → j.)

## 5. Example J1.4: CORRECT (CHECKED)

**The geometry is right:**
- W_n ⊆ S_n, since r̂ ∈ γ;
- for θ_M < θ_m, the shell S_d ∩ W_m ∖ W_M contains a cone over a positive-measure set of directions for every d,
  because r̂ is in the relative interior of γ.

**Two precisions are needed:**
- **Containment.** Ends are subsets of M ⊆ U. θ₀ must be small enough that every cap and tube lies in U ∩ O, and in
  the region where T1's advice is constant if the ends are to be T1-wrong at i and T1-correct at j (or else start at a
  later depth).
- **"Escapes J1.2".** The claim is right when 𝒮_l = ∅ and W is i's only end in O. Then every one of the six orders
  reduces to one of the two arrows (§4.3 parenthesis).

**NUMERICS** (`j1ref_py/j1ref_geometry.py`). Setting: T1 with ε = 0.3, s = 0.9, in the ∂U collar of (+,+,−), where T1
rejects. So the cap is T1-wrong at world 1 and the tube T1-correct at world 3, as for end A of the template.
- **Containment.** The θ₀ = 0.04 tube is 18 % outside U, and T1 accepts 20 % of it. From θ₂ = 0.01 on, there are
  0 exceptions. This confirms the first precision.
- **Cap inside tube.** 0 exceptions at depths 0–3.
- **The shell is hit at every tested depth d ≤ 10.**

## 6. Proposition J1.5: CORRECT

**(1)** This is step 1 of J1.2. 𝒮_l = ∅ makes l's comparison base. i's comparison is base because δ_i = 0 on
Π^i_{m′}.

**(2)** If j's comparison were base too, Step C would be contradicted. End-protection then gives S′-positivity.

**T1-wrong S′ is excluded:**
- by H2.1(b), with V(S′) ⊆ {i, l} and 𝒮_l = ∅;
- this uses that the depth in H2.1(b) can be taken equal to m′.

**The positive set deep in S′:**
- it is where X is j-wrong;
- there r_m(g) = i (since r_m(g) ≤ 2 on Π^j_m) and σ_i ≠ σ_j;
- the i-end containing g in O must be T1-wrong. A T1-correct one is eventually disjoint from S′, by the §4.3 fix,
  which J1's "the ends of i there are T1-wrong" again omits;
- and g ∉ Π^i_{m′}.

So the positive set lies in (W_m ∖ Π^i_{m′}) ∩ S′, which is contained in J1's shells W_m ∖ W_{m′}.

**Consequence.** J1.5 implies that i → j is misaligned (take M = m′), consistent with J1.3(c).

## 7. §4.2: the three failed repairs (CORRECT as descriptions)

- **(α)** S′_n ∖ W_n is not decreasing: points of (W_n ∖ W_{n+1}) ∩ S′_{n+1} enter. The fixed-m pieces S′ ∖ W_m do
  decrease, but the positive set of J1.5 lies in S′ ∩ W_m, so nothing is gained. Accurate.
- **(β)** In the cap–tube geometry, points on or near γ have S-depth ≥ W-depth. So "deeper priority" hands most of
  the cap to j, and i's step 1 is lost. Accurate.
- **(γ)** Accurate. Here is a small by-product (**PROVED**).
  - Let X* be X made j-correct on all of Q := (Π^i_m ∖ Π^i_{m′}) ∩ {σ_i ≠ σ_j} (inside D_m).
  - If C ⪯_l X* (for instance if σ_l = σ_i on Q), then C ⋠_j X*.

  *Proof.*
  - X* is near-Bayes with the same m, and C ⪯_i X* by (G) and transitivity.
  - If C ⪯_j X* held, then δ*_j would be ≤ 0 deep on every end of j. X* is j-wrong only on Π^i_{m′}, where
    C = X = X*.
  - So J1.0 makes it base. The i- and l-comparisons are base as well, which contradicts Step C at X*. ∎

  So the kkm dominators of X and X* are different models, which is the regress J1 describes. It is not an
  obstruction.

## 8. J1.Q, and whether a negative answer closes the stated class

### 8.1 Wording of J1.Q (GAP, wording)

"For every integrable admissible ψ" is too broad. J1.5's shell conclusion uses (b) for ψ, through Step C. For an
admissible ψ without (b), the unendorsed dominator comparison can be base, and nothing forces shells. This is the
defect H12_referee §2.6 found in H2 §5.2.

**Replace by:** "for every tuple ψ of integrable base endorsers (automatically admissible, H1.1), every t ∈ I_ψ, and
every large m". The write-up repeats the phrase and should be corrected too.

### 8.2 The closure claim (GAP: unproved; the editor is right)

**What J1 defines and proves.**
- "Doubly misaligned" is defined (§4.1) only for a 2-cycle next to a world with 𝒮_l = ∅.
- J1.5, which gives the shell exchanges that J1.Q asks about, is proved only there.

**What a negative answer to J1.Q therefore closes:** (EP) with some world having no ends. In that case Γ is a 2-cycle,
and no aligned order is equivalent to double misalignment (§4.3).

**What it leaves open:** (EP) with all three worlds having ends and no aligned order. This includes 3-cycles, and
2-cycles whose third world has ends. These are exactly the editor's two cases. J1 does not analyse them.

The general tool below shows how far J1.2 reaches there and what is left.

### 8.3 Theorem R.2 (PROVED): order alignment from arrow alignment

**Statement.** Assume (EP), and fix an order (k₁, k₂, k₃). Suppose:
- **(F)** For every r < s, every T1-wrong W ∈ 𝒮_{k_r} and every T1-correct S′ ∈ 𝒮_{k_s} lying in a common orthant,
  and all large m: ∀n ∃d with S′_d ∩ W_m ⊆ ⋃_{q<s} Π^{k_q}_n. (Every *forward* arrow is aligned relative to the
  earlier worlds.)
- **(B)** For every T1-wrong S′ ∈ 𝒮_{k₂}, T1-correct S ∈ 𝒮_{k₁} and T1-correct T ∈ 𝒮_{k₃} lying in a common orthant,
  and all large m: ∀n ∃d with S′_d ∩ S_m ∩ T_n ⊆ Π^{k₁}_n.

Then the order is aligned, so (H_U) is contradicted (J1.2).

(B) is vacuous unless Γ contains both k₂ → k₁ and k₂ → k₃.

*Proof.* Use the pairwise condition of J1. Take m beyond all orthant-purity and T1-purity depths, and beyond every j₀
of eventually disjoint pairs. Consider a pair S ∈ 𝒮_{k_r}, S′ ∈ 𝒮_{k_s} (r < s) in a common orthant O with
σ_{k_r} ≠ σ_{k_s} on O.
1. **Both T1-correct, or both T1-wrong, at their worlds.** T1's single advice on S_m ∩ S′_m would be right (resp.
   wrong) at two worlds of opposite sign. So the intersection is null: case (i).
2. **S T1-wrong, S′ T1-correct.** This is (F), i.e. (iii).
3. **S T1-correct, S′ T1-wrong, s = 3.** V(S′) ⊆ {k₁, k₂}, both earlier, so (ii) holds by H2.1(b).
4. **S T1-correct, S′ T1-wrong, s = 2.** Given N, apply H2.1(b) at depth n := max(N, d₀). Then S′_d lies in the union
   of the T_n over T1-correct ends T of worlds of V(S′) ⊆ {k₁, k₃}.
   - Terms with T ∈ 𝒮_{k₁} lie in Π^{k₁}_n ⊆ Π^{k₁}_N.
   - A T ∈ 𝒮_{k₃} that does not meet S′ at every depth is eventually disjoint from it. With n, d ≥ d₀ these terms
     are null.
   - For the remaining T (an arrow k₂ → k₃), (B) gives S′_d ∩ S_m ∩ T_n ⊆ Π^{k₁}_N.
   - So S′_d ∩ S_m ⊆ Π^{k₁}_N, which is (iii).

**Vacuity of (B).** If S′ does not meet S at every depth, then S_m ∩ S′_d is null for our m. If S′ does not meet T at
every depth, the T-terms vanish as shown. ∎

**Corollary R.3 (PROVED).** Call an arrow a → b of Γ *aligned* if it satisfies J1.3(c)'s condition: for all T1-wrong
W ∈ 𝒮_a and T1-correct S′ ∈ 𝒮_b in a common orthant, ∀m, n ∃d with S′_d ∩ W_m ⊆ Π^a_n. Alignment relative to Π^a
implies (F) in every order in which a precedes b. Let Γ_mis be the set of misaligned arrows.
- **(a) Acyclic Γ_mis.** If Γ_mis is acyclic, (F) holds in every order in which all arrows of Γ_mis point backward
  (reverse topological orders of Γ_mis; they exist). So (H_U) is contradicted as soon as (B) holds for one of these
  orders. That is automatic if its middle world does not have arrows to both other worlds.
- **(b) Pure 3-cycles.** Let Γ = {a → b, b → c, c → a}. In the order (a, c, b), the only forward arrow is a → b, and
  the middle world c has out-degree 1.
  - So a → b aligned, even only relative to Π^a ∪ Π^c, gives a contradiction.
  - **A pure 3-cycle survives only if all three arrows are misaligned**, in this weaker-alignment sense.
  - So J1 §0's "no cycle survives if one arrow is aligned" is true for pure 3-cycles. J1 does not prove it.
- **(c) 2-cycles with an isolated third world.** Let Γ = {i → j, j → i}, with l incident to no arrow (𝒮_l arbitrary,
  possibly nonempty).
  - The orders (i, j, l) and (l, i, j) are aligned iff i → j is aligned. The mirror orders behave likewise for
    j → i.
  - **Prop. J1.5 holds verbatim with the order (l, i, j).**
    - l is first, so it closes.
    - i's step needs nothing, because no arrows involve l.
    - In j's step, T1-wrong S′ of j is covered by i's T1-correct ends, since l's are eventually disjoint from S′.
    - The l-led conflict points in S′ are null.
  - So J1.Q, posed with "third world isolated in Γ" in place of 𝒮_l = ∅, covers this case as well.

**NUMERICS** (`j1ref_py/j1ref_orders.py`): every 3-vertex digraph with a directed cycle, up to relabelling (10
digraphs).
- **With (B) assumed to hold,** a misaligned set escapes R.2 iff it contains a directed cycle: 0 mismatches over all
  subsets. This is the trivial direction of (a) together with its converse: a cycle in Γ_mis has a forward arrow in
  every order.
- **With (B) assumed to fail wherever it is needed,** there are extra survivors that contain no misaligned cycle. They
  occur exactly when the unique order making Γ_mis backward has a middle world with out-degree 2. Example:
  Γ = {0→1, 0→2, 1→0} with Γ_mis = {0→2, 1→0}.
- **For the complete digraph,** R.2 alone excludes nothing if (B) fails.

### 8.4 The precise residual of (EP) after J1.2, R.1, R.2

A cover of T1 in class (EP) needs one of the following:
- **(R-i) Γ = 2-cycle + isolated vertex, doubly misaligned.** A negative answer to J1.Q (with the §8.1 wording and the
  R.3(c) extension) closes exactly this case.
- **(R-ii) Γ = pure 3-cycle, triply misaligned** (each arrow a → b misaligned relative to Π^a ∪ Π^c). J1.5 has no
  analogue proved here. By the R.2 argument, in the order (a, c, b) the closure reaches worlds a and c, and the
  positive set of b's comparison lies in shells of a's T1-wrong ends that are shallow in Π^a ∪ Π^c. Proving this is
  the same argument as J1.5, but I state it as **CHECKED**, not PROVED.
- **(R-iii) Γ with at least three arrows, not a pure 3-cycle.** Either Γ_mis contains a directed cycle, or every order
  that makes Γ_mis backward has a middle world with arrows to both others at which (B) fails. Here the third world's
  comparison is not shown to be base, and no shell description is available.

**The single question that would close (EP)** (no conjecture stated) is the following.

> **J1.Q′.** Under (EP), if no order of the worlds satisfies (Al), is (H_U) contradictory?

J1.Q is its sub-case (R-i). The write-up's scoping sentence in the J1.Q paragraph is correct and should cite §8.4.

## 9. Minor points

- **J1 §5, H2.1(b).** p ⊆ O (beyond W's orthant-purity depth) is needed so that T1 is right at j on p, i.e. so that
  δ_j = +1 there. It is not needed for δ_j to vanish on the S_M; p already avoids every S_M. Harmless.
- **J1 §0.** "every configuration in which ends of different worlds are, orthant by orthant, either eventually
  disjoint or germ-equal" should read "mutually shadowed (⊑ both ways)". That is what J1.3(b) proves.
- **BRIEF16 "Excluded: aligned cycles (J1)".** This is accurate only in the sense of R.3. "Some aligned order" is the
  proved condition.

## 10. Requested changes

1. Define ⊑ in J1 §1 (§4.2).
2. J1.3(c) and J1.5: add "if S is T1-correct at i, the pair is eventually disjoint (case (i))" (§§4.3, 6).
3. J1.3(a): drop 𝒮₂ ⊆ {A, B} (§4.1). Replace "for every t ∈ I_ψ" by "the configuration is inconsistent with (EP)".
4. J1.4: require θ₀ small enough that the sets lie in U ∩ O and in a region of constant T1-advice (§5).
5. J1.Q:
   - replace "every integrable admissible ψ" by "every tuple of integrable base endorsers" (§8.1);
   - replace "𝒮_l = ∅" by "l isolated in Γ" (R.3(c));
   - restrict the stated consequence to case (R-i) and add J1.Q′ (§§8.2–8.4).
6. J1 §0: restrict "no conflict cycle survives if one of its arrows is aligned" to 2-cycles with an isolated third
   world and to pure 3-cycles, citing R.3 (§8.3).
7. Write-up §8.5(f′)/(g): add Theorem R.2 and Corollary R.3 (proved in a referee report, one reader), and the residual
   (R-i)–(R-iii) in place of "no order is aligned … doubly misaligned".

## 11. Files (`j1ref_py/`)

- `j1ref_geometry.py` (+ `.out`): Example J1.4 in the T1 collar of (+,+,−), as in §5.
- `j1ref_orders.py` (+ `.out`): the enumeration of §8.3.
