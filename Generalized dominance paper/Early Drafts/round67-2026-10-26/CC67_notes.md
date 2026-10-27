# CC67: compactness in LDG (referee report and theorem formulation)

26 October 2026. Role CC67 of BRIEF67. Binding input: AUDIT_r67_message2 point 1.

**Labels.** PROVED: argued line by line here. CHECKED: exact rational computation in `cc67py/` (run with `python3 -I`; every `.out` file ends in ALL PASS). CONJECTURE / OPEN: not settled.

**Scripts**
- `cc67py/check_audit_example.py`: the AUDIT_r67_compactness §5 example on a grid of t-values, with two worlds only. It checks the relation's properties, the dominance facts, the global closed sets, joint realisation, and local coverage on Δ_F for F with up to two worlds of each type.
- `cc67py/check_escape_example.py`: the new example of §3.5 below, truncated to finitely many worlds and rivals. It checks (LA), (C), (W), the finite-set conditions on every F with up to three worlds (including the exact switching points p₁ = 1/2 and 1/3), and the finite core of the failure argument. It is run twice: `6 8 8`, where every e_n exists for the F tested, and `9 8 10`, where there are more worlds than e_n's, so that the uniqueness claims become visible.

**Notation.** As in LDG v3.3. C_L is the class of undominated coherent evaluable models, given by (LA). (W) says that every evaluable model is weakly dominated by a member of C_L. For a finite set F of worlds, "(B) on F" means LDG's finite condition (B) for the ranking restricted to the worlds in F, with realisers taken from C_L, where C_L is still defined using all of Ω.

---

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1a | (CC) ⇒ (W) under (LA) (AUDIT §3) | CORRECT (PROVED). It needs no reflexivity, transitivity, completeness or numerical structure. |
| 1b | (W) ⇒ (CC) via the cofinite topology | CORRECT (PROVED). It needs only (LA) and the axiom of choice. Nonemptiness of C_L follows from (W), because M_L ≠ ∅. Reflexivity is not needed. |
| 1c | Can a stronger topology rescue (CC)? | NO (PROVED). The collapse survives a requirement that Θ be compact Hausdorff (use the one-point compactification). It also survives a requirement that Θ be compact metrizable, whenever the dominators used number at most the continuum. Hence (CC) ⟺ (W), as AUDIT_r67_message2 states. |
| 2a | AUDIT §5 example: (LA), (C), (W), (CC) and the local version hold, but (I)+(B∞) fails for every compact indexing | CORRECT (PROVED; CHECKED). One unstated fact: the relations are not transitive. This is harmless, since LDG assumes no transitivity. |
| 2b | Simplification | The copies are unnecessary. The same argument works with Ω = {1,2}, one world of each type. So even for **finite** Ω, (B) does not imply (I)+(B∞) (PROVED). |
| 2c | Re-interpretation | "(I)+(B∞) is strictly stronger than (W)" is correct, but LDG already shows it: Example `ex:hole` (two worlds, a loss ranking) has (W) and not (B), and for finite Ω, (I)+(B∞) ⇒ (B). What is new in the AUDIT example is that **(I)+(B∞) is strictly stronger than the local theorem's hypotheses**. |
| 3a | Statement of the local theorem, without the word "certificate" | Given in §3.1 below. PROVED. |
| 3b | Does it collapse into (W)? | NO (PROVED). Its hypotheses imply (B) on every finite set of worlds, and LDG's Example `ex:hole` has (W) without that. A second example has no ideal coherent model at a world. |
| 3c | Cofinite topology, discrete or singleton choices | These do not collapse it (PROVED). They fail because a single index must serve **all rivals at once** at each point of Δ_F. If the index may depend on the rival, the theorem does collapse into (W) (PROVED). This is LDG §4.3's second point. |
| 3d | Does the compact link add anything beyond "(W) plus (B) on every finite set"? | YES (PROVED; finite core CHECKED). In a new example (§3.5), (LA), (C), (W) and (B) on every finite F all hold, but the local theorem's hypotheses fail. The compact link requires that limits of the local dominators keep their other guaranteed comparisons, and this is a genuine requirement. |
| 3e | Can the hypotheses be checked without knowing the conclusion? | YES. In every LDG application they follow from propriety plus lower semicontinuity, through (I)+(S∞) or (I)+(B∞). In the AUDIT example they are checked directly while (I) fails. For finite Ω they are exactly (B). |
| 3f | Resulting hierarchy | (I)+(S∞) ⇒ (I)+(B∞) ⇒ local hypotheses ⇒ [(W) and (B) on every finite F] ⇒ (W) ⟺ (CC). Every implication is strict. For finite Ω the third and fourth conditions coincide, since both are equivalent to (B), and the other implications remain strict. |
| 4 | What (I)+(B∞) gives that the local theorem does not | Comparisons with bounds that are not losses of models. Every appendix result that uses them already assumes (I) with lower semicontinuous losses, and most also assume Bayes choices. None of them needs (B∞) or the old infinite theorem except Cor. `cor:bayes`, which needs only (I) with lsc plus "every model is weakly dominated by a member of the compact family". A row-by-row list is in §4. |
| 5 | Applications satisfy the local hypotheses directly | YES (PROVED): Theorem `thm:nielsen`, Prop. `prop:blocks`, Prop. `prop:countable`, and §6.1. In each case they hold through the existing verification of (I)+(S∞) or (S). No application needs the weakening, but none loses anything. |
| 6 | Text in v3.3 that the result falsifies | Line 157: "nothing in this paper shows that (I) can be dropped when Ω is infinite". This must change. See §6 for the edits for LDGO67. |

---

## 1. (CC) is equivalent to (W)

**Setting.** A ranking L satisfies (LA). Condition (CC) (AUDIT §2) asks for the following:
- a nonempty compact space Θ;
- for each θ, a member c_θ of C_L;
- for each θ and world ω, a set B_ω(θ) of evaluable models.

These must satisfy three clauses:
1. each set K_ω(x) = {θ : x ∈ B_ω(θ)} is closed;
2. c_θ ⪯_ω x whenever x ∈ B_ω(θ);
3. for each rival x and finite nonempty F ⊆ Ω, some θ has x ∈ B_ω(θ) for every ω ∈ F.

(The audit phrases clause 2 as "a single c ∈ C_L realises everything at θ". Writing c_θ for that choice gives the form above.)

**(CC) ⇒ (W). PROVED.** Fix x. By clause 3, the closed sets K_ω(x), ω ∈ Ω, have the finite intersection property. Compactness gives a θ in all of them. By clause 2, c_θ ⪯_ω x at every ω. The proof uses no property of the relations. Adding (C) gives ordinary dominance of every model outside C_L, and U_L = C_L, by Prop. `prop:W`(a).

**(W) ⇒ (CC). PROVED.**
- (W) and M_L ≠ ∅ give C_L ≠ ∅. Using choice, fix for each x ∈ M_L a member d(x) ∈ C_L that weakly dominates it.
- Let Θ = C_L with the cofinite topology. It is compact: an open cover contains a nonempty member, which has finite complement, and finitely many more members cover that complement.
- Put c_θ = θ and B_ω(θ) = {x : d(x) = θ}.
- Clause 1: K_ω(x) = {d(x)} is finite, hence closed.
- Clause 2: if d(x) = θ, then θ ⪯_ω x.
- Clause 3: θ = d(x) works for every F.

Nothing else is used: no reflexivity (a coherent model in C_L is weakly dominated by d(x), which need not be itself), and no property of Ω.

**Stronger topologies do not rescue (CC). PROVED.**
- *Hausdorff.* Use the one-point compactification Θ = C_L ⊔ {∞} of the discrete space C_L. Let c_∞ be any member of C_L and B_ω(∞) = ∅. Singletons {d(x)} ⊆ C_L are closed, and the space is compact Hausdorff.
- *Metrizable.* If the set d(M_L) of dominators actually used has at most continuum many members, inject it into the Cantor set 2^ℕ. Every other point carries an arbitrary realiser and no listed rivals. The sets K_ω(x) are singletons, which are closed.

So imposing more topology does not make (CC) say more than (W). This confirms AUDIT_r67_message2 point 1. Keep the elementary compactness argument as the last step of the local theorem (§3), and do not present (CC) as a hypothesis with independent content.

**The rival-specific variant (AUDIT §6) also collapses. PROVED.** Take Θ_x = {d(x)} and the closed sets K_{ω,x} = Θ_x. This is the infinite-world form of LDG §4.3's second point.

---

## 2. The strict-separation example (AUDIT_r67_compactness §5)

**Verdict: CORRECT** (PROVED; CHECKED with `check_audit_example.py` on t ∈ {0, 1/6, …, 1}).

Line-by-line checks:
- *The relation.*
  - The removed pairs have strictly smaller loss on the coherent side: q < 2 at type 1, and 1 < 2 at type 2.
  - So every accepted comparison is a score comparison (≤), and every score tie is kept in both directions.
  - Hence an accepted cycle has constant scores. Each of its steps then has its reverse accepted, so no step is strict.
  - Reflexivity and (TC) follow. CHECKED.
- *Not transitive* (not stated in the audit). For 0 < q < s, we have c_q ⪯₁ c_s and c_s ⪯₁ x_q, but not c_q ⪯₁ x_q. CHECKED. LDG's abstract results do not use transitivity, so this is harmless. But the example cannot be cited for preorder rankings.
- *Dominance facts.*
  - The only weak dominator of c_t is c_t itself: a weak dominator needs loss at most t at type 1 and at most 1−t at type 2.
  - x_q is dominated by every c_s with s ≠ q.
  - No incoherent model is tied with a coherent one at every world.
  - So (LA), (C) and (W) hold, with U_L = C_L = {c_t}. CHECKED.
- *(CC) data.*
  - The sections are [0,s], [s,1], {0}, Θ and {1}, all closed.
  - At θ, c_θ meets every listed comparison. Checked case by case: c_θ ⪯₁ c_s iff θ ≤ s; c_0 ⪯₁ x_q for q > 0; c_θ ⪯₂ x_q for q > 0; c_θ ⪯₁ x_0; c_1 ⪯₂ x_0. CHECKED.
- *Local version.*
  - θ(p) is the total p-mass on type-2 worlds, which is continuous.
  - Coverage for c_s: if θ(p) ≤ s a type-1 world is charged, unless p is concentrated on type 2, in which case θ(p) = 1 ≥ s. The case θ(p) ≥ s is symmetric.
  - Coverage for x_q, q > 0: certified at every charged type-2 world. If no type-2 world is charged, then θ = 0, which certifies x_q at type 1. The case x_0 is symmetric. CHECKED.
- *No compact indexing satisfies (I)+(B∞).*
  - Theorem `thm:infinite-bounds` makes f onto C_L.
  - The full type-1 section against x_q (q > 0) is Ξ∖E_q. The full type-2 section against x_0 is Ξ∖E_0.
  - Condition (I) makes these closed, so every E_t is open. This gives a cover of Ξ by infinitely many disjoint nonempty open sets, which has no finite subcover. PROVED.

**Simplification (2b). PROVED.** The proof uses one world of each type, so Ω = {1,2} suffices. Then:
- (B) holds, with Θ-pullback certificates on Δ = Δ_{{1,2}};
- (I)+(B∞) fails for every compact indexing, by the same open-partition argument. For finite Ω, (B∞) requires Ω ∈ 𝔉, so (I) must hold for a family containing a weak dominator of each c_t.

So, already for two worlds, LDG's (I) is a genuine extra requirement beyond (B). This is consistent with LDG (line 157 says (I) can be dropped for finite Ω). It shows that the drop is not cosmetic.

**Re-interpretation (2c).**
- That (I)+(B∞) is strictly stronger than (W) is true, but it is already witnessed in LDG by Example `ex:hole`. That example uses a loss ranking with two worlds: (W) holds trivially, and (B), hence (I)+(B∞) (Prop. `prop:SBinfty`), fails.
- The AUDIT example shows something stronger: (I)+(B∞) is strictly stronger than the **local theorem's hypotheses** (§3). It should be cited for that, with two worlds and with the intransitivity stated.
- OPEN (low priority): does some *preorder* or loss ranking separate (B) from (I)+(B∞)? Prop. `prop:necessary` shows that a loss example needs a non-compact set of coherent profiles.

---

## 3. The local finite-to-infinite theorem

### 3.1 Statement

**Theorem (finite sets of worlds to all worlds). PROVED.** Let Ω be any nonempty set and let L satisfy (LA). Suppose there are the following.

1. **One compact family.**
   - a compact space Θ;
   - for each θ ∈ Θ, a model c_θ ∈ C_L;
   - for each world ω and evaluable model x, a closed set K_ω(x) ⊆ Θ such that c_θ ⪯_ω x for every θ ∈ K_ω(x).

   We say the comparison with x at ω is *guaranteed* at θ when θ ∈ K_ω(x). Not every comparison that c_θ makes needs to be guaranteed.
2. **Local guarantees on finite sets of worlds.** A family 𝔉 of finite nonempty sets of worlds such that every finite set of worlds lies in some member of 𝔉. For each F ∈ 𝔉:
   - a map θ_F : Δ_F → Θ, which need not be continuous and **does not depend on the rival**;
   - for each ω ∈ F and evaluable x, a closed set A^F_ω(x) ⊆ Δ_F.

   These must satisfy:
   - (a) *the local guarantees are global guarantees:* if p ∈ A^F_ω(x), then θ_F(p) ∈ K_ω(x);
   - (b) *every rival is met where p puts weight:* for every p ∈ Δ_F and every x, p ∈ A^F_ω(x) for some ω ∈ supp p.

Then every evaluable model is weakly dominated by some c_θ, which is in C_L. With (C), U_L = C_L, and every model outside C_L is dominated by a member of C_L.

*Plain-English version.* On each finite set of worlds, every weighting p of those worlds is assigned one member of a fixed compact family of coherent undominated models, and this one member must serve against every rival. For each rival and world, the weightings at which the comparison is guaranteed form a closed set, and every rival is guaranteed at some world that p charges. In the compact family, the members guaranteed to match or beat a given rival at a given world form a closed set. Then a single member of the family matches or beats the rival at every world.

**Proof.**
- Fix x and F ∈ 𝔉. By (b), the closed sets A^F_ω(x), ω ∈ F, satisfy the hypothesis of Lemma `lem:kkm`. That lemma gives p_F lying in every one of them.
- By (a), θ_F(p_F) ∈ ⋂_{ω∈F} K_ω(x).
- Given finitely many worlds, some F ∈ 𝔉 contains them all. So the closed sets K_ω(x), ω ∈ Ω, have the finite intersection property.
- Compactness gives θ* in all of them. Then c_{θ*} ⪯_ω x for every ω.
- The rest is Prop. `prop:W`(a).

No property of the relations ⪯_ω is used: not reflexivity, transitivity or completeness, and no numerical structure.

**Convenient special case (continuous indices). PROVED.** Suppose each θ_F is continuous. Then (a) and (b) can be replaced by the single requirement that every rival x and every p ∈ Δ_F have some ω ∈ supp p with θ_F(p) ∈ K_ω(x). Take A^F_ω(x) to be the preimage θ_F⁻¹(K_ω(x)), which is closed. This is the form in which every application of LDG verifies the hypotheses (§5).

### 3.2 Relation to LDG v3.3's conditions (all PROVED)

- **(I)+(B∞) ⇒ local hypotheses.**
  - Let K_ω(x) = {θ : c_θ ⪯_ω x}, which is closed by (I).
  - Let A^F_ω(x) = {p : x ∈ B_{F,ω}(p)}, which is closed by (B∞).
  - Let θ_F(p) be an index given by (B∞)(i), chosen using the axiom of choice.

  Then (a) holds by (B∞)(i), and (b) holds by (B∞)(ii). So Theorem `thm:infinite-bounds` and Corollary `cor:infinite` become corollaries of the local theorem.
- **(I)+(S∞) ⇒ the continuous special case**, with θ_F = σ_F and the full comparison sections of (I).
- **Finite Ω: local hypotheses ⟺ (B).**
  - (⇒) Cofinality forces Ω ∈ 𝔉. Put B_ω(p) = {x : p ∈ A^Ω_ω(x)}, with realiser c_{θ_Ω(p)}.
  - (⇐) Put Θ = Δ, let c_p be a realiser at p, let K_ω(x) = {p : x ∈ B_ω(p)}, which is closed by (B1), let θ_Ω be the identity, and let A = K.

  So for finite Ω the local theorem **is** Theorem `thm:main`, and nothing is lost in the finite case.
- **Local hypotheses ⇒ (B) on every finite set G of worlds.**
  - Choose F ∈ 𝔉 with F ⊇ G.
  - Restrict to the face Δ_G ⊆ Δ_F and to the worlds of G.
  - Use the certificates {x : p ∈ A^F_ω(x)}, ω ∈ G, with realiser c_{θ_F(p)}.
  - Coverage holds because supp p ⊆ G.

### 3.3 Does it collapse into (W)? No.

**(W) does not imply the local hypotheses. PROVED.** By §3.2, the hypotheses imply (B) on every finite set of worlds. Two examples have (W) but fail this.
- LDG Example `ex:hole`: two worlds, coherent profiles (t, 1−t) with t ∈ [0,1]∖{½}, and M_L = C. Here (W) holds trivially, and (B) fails.
- *No ideal model.* Two worlds, M_L = C, and coherent profiles (t, 1−t) with t ∈ (0,1], which are pairwise incomparable. Again (W) holds trivially. But (B) on {1} needs a member of C_L that matches or beats every model at world 1, and no profile has first coordinate 0.

**The cofinite topology and discrete choices do not collapse it. PROVED.** The §1 trick fails because of (b): at each p, **one** index must be guaranteed against **every** rival at some charged world.

- *Singleton guarantee sets.* If each K_ω(x) is the singleton {d(x)}, then (a) and (b) force θ_F(p) = d(x) for every x. So one coherent model would weakly dominate every rival on F at the worlds where it is guaranteed. That is not available in general (for example, in Example `ex:hole`).
- *The cofinite topology on C_L.* The closed sets are the finite sets and C_L itself. So the hypotheses hold with this topology if and only if there are local data such that, for each ω and x:
  - either every member of C_L matches or beats x at ω;
  - or only finitely many distinct indices θ_F(p), over all F and p, are guaranteed against x at ω.

  This fails already for the Brier score on two worlds, where c_t has profile (2(1−t)², 2t²) and C_L = C. The argument is PROVED:
  - For a rival c_s, the KKM point gives an index guaranteed against c_s at both worlds. That index must be c_s itself. So every c_s occurs as an index.
  - An index c_t with t > s is guaranteed against c_s at world 1 whenever it is used at a point charging world 1, since c_t meets c_s only at world 1.
  - So infinitely many indices are guaranteed against c_s at world 1, while c_0 does not match c_s there when s > 0. Neither alternative holds.
- *Discrete choices (θ_F constant on each Δ_F).* By (b) at the vertices, the constant index must be guaranteed against every rival at every world of F. So one coherent model must be *ideal at every world of F*. This is far stronger than (W). It is the "finite ideal-model" condition, and it fails, for example, for the Brier score on two worlds.

**If the index may depend on the rival, the theorem does collapse. PROVED.** Allow θ_F(p) = θ_F^x(p). Under (W), put θ_F^x ≡ d(x), K_ω(x) = {d(x)} and A^F_ω(x) = Δ_F. Then (a) and (b) hold trivially. This is exactly the point of LDG §4.3: the substance lies in **one index per weighting, serving all rivals**. The statement must say that θ_F does not depend on the rival, and the proof must not let it.

### 3.4 Can the hypotheses be checked without the conclusion? Yes.

- In every LDG application (§5), the hypotheses follow from propriety-type optimality (Bayes choices, Lemma `lem:bayes-choice`) together with lower semicontinuity of θ ↦ L(c_θ, ω) on a compact family. Neither ingredient mentions dominance.
- In the AUDIT example, the hypotheses are verified directly from the relations, using two closed intervals and a continuous θ(p), while (I) provably fails for every compact indexing.
- For finite Ω the hypotheses are exactly (B), which LDG already treats as checkable. Section 4.2 and Remark `rem:threeworld-bounds` give explicit instances.

### 3.5 The compact link has content: (W) together with (B) on every finite set does not suffice

**Example. PROVED; finite core CHECKED (`check_escape_example.py`, both configurations ALL PASS).**

*Worlds and models.*
- Worlds: Ω = ℕ = {1, 2, …}.
- Coherent models: d, h, and e_n for n ≥ 1.
- Incoherent models: x, z, and w_k for k ≥ 1.

*Relations.* At every world:
- every two coherent models are related in both directions;
- every model is related to itself;
- an incoherent model is related to nothing else;
- a coherent c satisfies c ⪯_ω y, for incoherent y, exactly when y appears in the following table.

| at world ω | x | z | w_k |
|---|---|---|---|
| d | every ω | ω ≥ 2 | ω > k |
| e_n | ω ≤ n | ω = 1 | every ω |
| h | ω ≥ 2 | every ω | every ω |

**Claims.**
1. **(LA), (C) and (W) hold, with C_L = C.**
   - Only coherent models are related to coherent models, and coherent models are tied at every world. So no coherent model is dominated.
   - No incoherent model is related to a coherent one, so no incoherent model is tied at every world with a coherent one. This gives (C).
   - Weak dominators exist: d for x, h for z, h for every w_k, and each coherent model for itself.
2. **(B) holds on every finite F.** Let N = max F.
   - *Realiser.* At p, use e_N if 1 ∈ F and p₁ ≥ ½, and h otherwise.
   - *Listed comparisons.*
     - Coherent rivals and every w_k: at every world of F and every p.
     - x: at every world ω ≥ 2 of F for every p, and at world 1 when p₁ ≥ ½.
     - z: at world 1 when p₁ ≥ ⅓, and at every world ω ≥ 2 when p₁ ≤ ⅓.
     - If 1 ∉ F: everything at every world, with realiser h.
   - *Closed sections:* each of these sets of p is closed.
   - *Coverage:*
     - x: a weighting p ≠ δ₁ charges some ω ≥ 2, and δ₁ has p₁ = 1.
     - z: if p₁ ≥ ⅓ then world 1 is charged, and otherwise some ω ≥ 2 is charged.
   - *Realisation:*
     - e_N meets x at every ω ≤ N, z at world 1, and every w_k everywhere.
     - h meets x at ω ≥ 2, and z and every w_k everywhere.
     - On [⅓, ½), the realiser is h, which meets z at world 1.

   CHECKED exactly for every F ⊆ {1,…,6} with |F| ≤ 3, on a rational grid plus the switching points.
3. **The local hypotheses fail, whatever Θ, c, K, 𝔉, θ_F and A are chosen.**
   - Suppose they held. Fix F ∈ 𝔉 with 1 ∈ F. Such F are cofinal, since every finite set together with {1} lies in some member of 𝔉.
   - KKM gives p_F with x ∈ A^F_ω(x) for every ω ∈ F. Let θ = θ_F(p_F). Then c_θ meets x at every world of F, including world 1. So c_θ is d or some e_n with n ≥ max F.
   - c_θ ≠ d. By (b), the rival w_k with k = max F is guaranteed at some charged world, but d meets w_k only at worlds ω > k, which lie outside F.
   - So c_θ = e_n, which meets z only at world 1. Hence (b) for the rival z forces θ ∈ K₁(z).
   - So the closed sets K_ω(x), ω ∈ Ω, together with K₁(z), have the finite intersection property. Compactness gives θ* with c_{θ*} meeting x at every world and z at world 1.
   - No coherent model does this. Only d meets x at every world (e_n fails at ω > n, and h fails at 1), and d fails z at world 1. CHECKED on the truncation with 9 worlds and n ≤ 8.

**What this shows.**
- The compact link is not implied by (W) together with every finite-world fact.
- Here each finite set has local dominators of x, namely the e_n, that keep a further guarantee (z at world 1).
- The only global dominator of x is d, and it does not keep that guarantee. The local dominators have no "limit" in C_L.

The relations here are not transitive: d ⪯₁ h ⪯₁ z, but not d ⪯₁ z. OPEN (low priority): find a preorder or loss-ranking version.

### 3.6 What exactly the compact link requires

**Reformulation without topology. PROVED.** Let D be the set of pairs (F, p) with F ∈ 𝔉 and p ∈ Δ_F. The local theorem's hypotheses hold if and only if there are local data with the following properties:
- realisers r(F, p) ∈ C_L;
- closed sets A^F_ω(x);
- coverage (b);
- r(F, p) meets x at ω whenever p ∈ A^F_ω(x);
- for every ultrafilter 𝒰 on D, some member of C_L meets every comparison (ω, x) that is listed at 𝒰-almost every pair, that is, every (ω, x) with {(F, p) : p ∈ A^F_ω(x)} ∈ 𝒰.

*Proof.*
- (⇐) Let Θ be the Stone–Čech compactification of the discrete set D, that is, the ultrafilters on D. Let c at an ultrafilter be the member given by the last property, or r(F, p) at a principal ultrafilter. Let K_ω(x) be the closure of {(F, p) : p ∈ A^F_ω(x)}. This is a basic clopen set, and every ultrafilter in it contains the set in question.
- (⇒) Push 𝒰 forward along (F, p) ↦ θ_F(p). By compactness it converges to some θ*. Each closed K_ω(x) whose preimage lies in 𝒰 contains θ*.

**Plain English.** Whenever the coherent models chosen locally keep making a given set of guaranteed comparisons, along any limiting process, some coherent undominated model makes all of those comparisons at once.

In applications this is exactly what lower semicontinuity of losses along a compact family supplies. The example in §3.5 fails it. Because ultrafilters are not plain English, the paper should state the compact-family form (§3.1) and mention this characterisation at most in a remark.

**Nearest non-collapsing version, and what gives it content.** The brief asks for this in case of a collapse. There is none, but the content can be located precisely.
1. One index per weighting, serving all rivals. Dropping this collapses the theorem to (W) (§3.3).
2. Closed guaranteed comparisons in one compact family, that is, inheritance by limits (§3.5–3.6). Dropping this leaves only (B) on every finite set, which does not imply (W). Example (PROVED): keep only e_n, h and x from §3.5, with the same table. Then (B) holds on every finite F with the same realisers and listed comparisons, but no coherent model meets x at every world. Even when (W) holds, the compact link is not implied, by §3.5.

Stated differently: the finite-world condition gives local dominators, and the compact family requires those local dominators to have coherent undominated limits that keep their guaranteed comparisons. The extra structure suggested in the brief (a fixed index space, continuity of the map from local to global indices, Bayes choices) is not needed for the theorem. Each item is a sufficient way to verify its hypotheses:
- continuity of θ_F gives (a) automatically (§3.1);
- Bayes choices give (b) (Lemma `lem:bayes-choice`);
- lower semicontinuity gives closed K_ω(x).

---

## 4. What (I)+(B∞) gives that the local theorem does not

The local theorem keeps two of the old conclusions:
- the weak dominator lies in the compact family {c_θ};
- every conclusion that uses only (W): Prop. `prop:W`, Prop. `prop:profiles`, Cor. `cor:strict-ordinal`, Prop. `prop:permissible` and Prop. `prop:permissible-equivalence`.

What it does **not** give is a comparison of the family with **bounds that are not losses of evaluable models**. Under (I), the full sections {θ : c_θ ⪯_ω m} are closed for every model m. With lower semicontinuous losses, the sublevel sets {θ : L(c_θ, ω) ≤ a} are closed for **every** real a. The local theorem guarantees closed sets only against the rivals themselves, and only for the listed comparisons.

Appendix results of v3.3, row by row (PROVED by inspecting each proof):

| Result | Uses beyond (W) | Status under the local theorem |
|---|---|---|
| Prop. `prop:SBinfty` | (I), (S∞) | Restate as: (I)+(S∞) ⇒ (I)+(B∞) ⇒ local hypotheses (§3.2). The finite clauses are unchanged. |
| Thm. `thm:infinite-bounds`, Cor. `cor:infinite` | (I), (B∞) / (S∞) | Become corollaries of the local theorem. |
| Cor. `cor:strict-ordinal` | transitivity | Holds under the local hypotheses: it uses only (W). |
| Prop. `prop:ordinal` | — | The local hypotheses depend only on the ranking, so they transfer unchanged. Add them to the list. |
| Cor. `cor:bayes` | (I) with lsc; dominators in the family | The proof needs only (a) the family losses are lsc, which already gives (I), and (b) every model is weakly dominated by some c_θ. So the hypothesis can be "(I) with lsc losses, and (W) with dominators in the family". The local hypotheses supply (b) but not (a). (B∞) is not needed as such. |
| Thm. `thm:margin` | (I) with lsc; (S∞) with Bayes choices | Unchanged. It compares with arbitrary x : Ω → (−∞, ∞], which needs lsc sublevel sets. It does **not** follow from the local hypotheses. |
| Cor. `cor:strict`, Cor. `cor:upperconvex`, Prop. `prop:strict-general` | as Thm. `thm:margin`; finite or continuous losses | Unchanged. They need lsc and Bayes choices. |
| Remark `rem:direct` | own index Bayes; lsc | Unchanged. |
| Lemma `lem:bayesbounds` and the paragraph after it ("margin theorem also holds under (I) with lsc and (B∞) with numerical certificates") | (I) with lsc; numerical lsc Q_F | Still correct. The new theorem does not weaken it, because it uses numerical bounds Q_F(p) that are not losses of models. |
| Prop. `prop:threeworld`, Remark `rem:threeworld-bounds`, Prop. `prop:necessary`, Example `ex:hole` | finite Ω | Unchanged, since for finite Ω the local hypotheses are (B). Prop. `prop:necessary`'s statement "(I) and (B∞) hold with Θ = K" remains true. |
| Uniform dominance in Thm. `thm:nielsen` and after Prop. `prop:countable` | Thm. `thm:margin` | Unchanged. They need lsc and Bayes choices, which those applications have. |

**Summary.** The results that need extra hypotheses are exactly the numerical ones: Bayes-model existence, margins, uniform and strict dominance, and mixtures. They need scores, Bayes choices and lower semicontinuous losses along a compact family. Each is already stated with those hypotheses, and none is affected by replacing the infinite theorem's headline hypotheses. The only textual change is in Cor. `cor:bayes`, where "(B∞)" can be replaced by "every model weakly dominated by a member of the family". That change is optional.

---

## 5. Applications satisfy the local hypotheses directly

All PROVED. In each case the existing verification of (I)+(S∞), or of (S), already gives the continuous special case of §3.1.

- **Section 6.2, probabilism on arbitrary domains (Theorem `thm:nielsen`).**
  - Θ = C, the finitely additive probabilities in the weak-star topology, which is compact. Let c_q = q.
  - K_ω(x) = {q : L(q, ω) ≤ L(x, ω)}, which is closed by lower semicontinuity (or all of C if L(x, ω) = ∞).
  - θ_F(p) = p, with p viewed in C. This map is continuous.
  - Coverage (b): quasi-strict propriety makes p a Bayes model for p. For finitely supported p, Nielsen's E_p f equals Σ_{ω∈supp p} p_ω f(ω) for [0, ∞]-valued f. So Lemma `lem:bayes-choice` makes p competitive on supp p. Since loss rankings are complete, every rival is matched at some charged world.

  No knowledge of dominance is used. The uniform-dominance clause still goes through Thm. `thm:margin`.
- **Section 6.3, conditional reports (Prop. `prop:blocks`).** Θ = Γ, c = ρ, K from (LSC), and θ_F = the continuous map of Lemma `lem:section`. Coverage holds because ρ(σ_F(p)) is Bayes for q₀ with supp q₀ ⊆ supp p. The certifying prior differs from the index, which the local theorem allows, as LDG already does.
- **The countable example (Prop. `prop:countable`).**
  - Θ = 𝒫(ℕ), c_θ = (θ{n})_n.
  - K_ω(x) = sublevel sets of the lsc map θ ↦ ‖c_θ‖² + 1 − 2θ{ω}.
  - θ_F(p) = p.
  - Coverage holds because p is Bayes for itself.

  The coherent profiles are not closed, and the theorem does not need them to be.
- **Section 6.1, proper scores on finite domains.** Here Ω is finite, so the local hypotheses are (B), which (S) gives (Prop. `prop:SB`).
- **The AUDIT example.** It satisfies the local hypotheses and not (I)+(B∞). This is currently the only example in which the weakening matters. No LDG application needs the weakening, and none loses anything.

---

## 6. Edits for LDGO67 (recommendations; no manuscript is being written in this round)

1. **Replace the infinite theorem's hypotheses** by those of §3.1, written without "certificate".
   - Suggested names: "a compact family of coherent undominated models with closed guaranteed comparisons", and "local guarantees on finite sets of worlds".
   - State in words that the index θ_F(p) does not depend on the rival.
   - Theorems `thm:infinite-bounds` and `cor:infinite` become corollaries, by §3.2.
2. **Line 157** ("nothing in this paper shows that (I) can be dropped when Ω is infinite") is now false. Replace it with a sentence saying that (I) is one way to obtain the closed guaranteed comparisons. Cite the AUDIT example (two worlds suffice; the relations are not transitive) as showing that it is strictly stronger.
3. **Present (CC) ⟺ (W) as a remark**, with the cofinite proof (§1), to explain why the local formulation is the substantive one. Also add a remark that the theorem collapses if the index may depend on the rival (§3.3). This one sentence extends LDG §4.3's second point to infinitely many worlds.
4. **Keep the §3.5 example only if space allows.** It shows that the compact link is not implied by (W) plus every finite-world fact. If included, state that its relations are not transitive.
5. **Leave the numerical appendix as it is** (§4). Optionally restate Cor. `cor:bayes`'s hypothesis as "(I) with lsc losses, and every model weakly dominated by a member of the family".
6. **Update the hypothesis table.**
   - New rows: the local theorem; the remark (CC) ⟺ (W).
   - Change the `thm:infinite-bounds` and `cor:infinite` rows to "corollary".
   - Add the local hypotheses to the list in Prop. `prop:ordinal`.
7. **Jargon** (BRIEF67 decision 5).
   - "Certificate" is replaced by "guaranteed comparison" and "local guarantee".
   - "Realiser" may become "the model at θ".
   - "Route A/B/C" should go, in line with the brief.
