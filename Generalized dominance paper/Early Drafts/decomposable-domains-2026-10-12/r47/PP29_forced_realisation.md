# PP29. Forced realisation of the padding records: what is forced, what is not, and the exact escape

22 October 2026. Adversary's note for Brief 47 (task PP29). One reader (me); not refereed.

**Labels.** PROVED: complete argument here. CHECKED: exact finite computation on cells (rational/LP geometry, exhaustive enumeration or SAT). Cells check bookkeeping only; they say nothing about (S) or about continuum padding beyond the pieces present. CONJECTURE / OPEN: as stated. NUMERICS: none.

**Scripts** (`r9/PP29_py/`; run `python3 -B <script>` inside the folder; outputs in `.out` files).

| Script | Content | Label |
|---|---|---|
| `lib29.py` | cell record algebra; realisability of an old side by a coherent D_K with K inside each face of the simplex (interior, three edges, three vertices) | library |
| `single_d_check.py` | Theorem 4.1 on cells: the explicit verdict rule passes guidance, every support-sensitive obligation and disjointness, for every intermediate model Q, six configurations (steep padding, padding in other classes, radial splits, T answering on some lines) | CHECKED |
| `forced_sat.py` | SAT: all inverted departures accepted at every world, inverses refused at every world, maximal support-sensitive obligations, undominatedness, direct (C), full (TC) via P1/P2 over all composable pairs; plus tests of the rule σ and of forced verdicts; Ω-subset control. Outputs `sat_<config>_<mode>.out` | CHECKED |

**Inputs.** Brief 47; AUDIT_answers47 (binding); AUDIT_selected_realizability §§3–5 (the support-sensitive obligation lemma); PP23 §§2–4 (Lemmas 4.3, 4.4, Theorem 4.5, Props 4.6–4.7); REFEREE_round46 §2.5 (repaired hypotheses P1–P3); AUDIT_completion (rules I–IV); LEAD_selection_count (Lemmas A, B, Theorem C); PP18 (Theorem Z); REFEREE_Z_PP19 (Lemma H, Prop S); PP19 (Lemma 0.4, Theorems 1, 4, 5). Axioms: Brief 47's, nothing more. No continuity of any kind is used. Single-world ties and triangle completion are allowed throughout.

---

## 0. Verdict

**The strong theorem is false as stated, for every admissible selection, and for a structural reason.** Audit's theorem says that every admissible selection through T realises both padding records of some decomposition x·y = d⁻¹ at indices whose supports force the two records onto one world. That conclusion never holds. Whatever the selection realises, the obligations, guidance, vertex and edge structure, closed sections and KKM never force the two pieces of any decomposition onto a common world.

What this does *not* show: that T can dominate all its inverted rivals in a full (S)-system. A (TC) clash could still be forced through triangles that do not pass through d. §6.4 reduces that possibility to two explicit shapes, and Conjecture 6.6 states the remaining claim.

1. **Theorem 4.1 (PROVED; CHECKED on cells).** Fix any selection satisfying strict (G) and competitiveness on supports. Closed sections are not even needed. Fix any inverted departure d in one class M_k, with any masses, any geometry, localized or not, B-heavy or not. Then every decomposition x·y = d⁻¹ admits verdicts with the following properties:
   - they accept every weak pure worsening and refuse every pure improvement;
   - they meet every support-sensitive obligation of both records (for an unmarked record: whenever its own obligations are satisfiable at all, which (S) requires anyway);
   - they never accept x and y at a common world.

   The verdicts are explicit, the **retreat split**:
   - a realisable record that retreats from **B on all of D^B** goes to the **owner k** only;
   - a realisable record that retreats from **A on all of D^A** goes to the **opponents j, l** only;
   - an unrealisable record keeps only the worlds where guidance forces it.

   The obligations can never collide. Every selected realiser of a B-retreat has k in its support (the closed edge [e_j, e_l] is A on M_k). Every selected realiser of an A-retreat has j or l in its support (C_{e_k} = V_k is B on M_k).

2. **What actually drove PP23 Prop 4.7 (Theorem 5.1, PROVED).** The B-heavy owner obstruction holds in a selected family under three conditions together:
   - (a) the opponents refuse both padding records, as Ω-additivity at j and l makes them do;
   - (b) selected models realise both old sides;
   - (c) d⁻¹ is refused at the owner.

   Theorem 4.1 shows that (b) and (c) without (a) force nothing. So the essential hypothesis in Prop 4.7 is **additivity at the opponents**, not universal realisation. Universal realisation only made the two records compulsory. The B-heavy mass condition matters only through (a).

3. **Forced realisation: the true part (§5).**
   - Edge-selected models are edge-supported. The vertex and edge structure fixes which faces can realise each record (Lemma 3.3).
   - On an edge, closed sections give an **inside-or-straddle dichotomy** (Prop 5.2, PROVED). Either some edge model realises y's two-set pattern on [e_k, e_j], or some edge model is silent across the whole window.
   - Closed-section inheritance never transfers a realisation to a boundary index (Lemma 5.3).
   - KKM dominators of padding rivals are exposed (Lemma 5.4), so they never realise the rival's padding.
   - So realisation is forced only in a weak form. By Theorem 4.1 it is harmless anyway.

4. **The escape and what it costs (§6).**
   - (i) **Non-additivity at an opponent (Prop 6.1, PROVED).** If both of Prop 4.7's padding records are accepted somewhere, some opponent accepts a record with Ω^(0) < 0. The same holds for every additive field under which d⁻¹ is negative at both opponents.
   - (ii) **Owner strictness is optional (Lemma 2.3, PROVED).** Refusing d⁻¹ at a world is forced only by T's dominations of the *enlargements* of d. Without them a tie at the owner is a second, cheaper escape.
   - (iii) **σ has a section cost (Prop 6.3, PROVED).** σ needs the selection never to jump directly between models that retreat from B on D^B and models that retreat from A on D^A (condition J_d).
   - (iv) **σ cannot be applied to all departures at once (Prop 6.2, PROVED).** Every model whose credal set crosses T's silent lines both ways in one class would lose its defence against T. Examples are the precise models inside int M and small sets displaced sideways from M. A multi-departure escape must therefore choose verdicts model by model.
   - CHECKED on cells: such per-model verdicts exist. In every configuration, with steep padding present and maximal support-sensitive obligations, **all** inverted departures are accepted at every world with inverses refused everywhere. This holds even where σ itself is UNSAT, and no padding verdict is forced. The Ω-subset control reproduces Prop 4.7's UNSAT.

5. **Where an obstruction could still come from (§6.4).** Theorem 4.1 is a single-departure statement. A real obstruction would need one of two things:
   - a **star**: one selected C whose x-records rec(T·d, C), over many d, are forced onto every world at which C may defend against T;
   - a **domination record that is also a padding piece**: a KKM domination rec(C, R), accepted at all worlds, equal to one padding record whose partner is selected-realised.

   Both reductions are PROVED. Neither instance is known (OPEN). The cells contain neither.

**Classification of the failures (rules of the brief).**

| Claim or obstruction | Source |
|---|---|
| Collision of one padding pair | never follows: not from the axioms, the selection or the geometry (Thm 4.1) |
| d⁻¹ refused at every world | optional comparisons: T ⪯ T·d′ for the enlargements d′ (Lemma 2.3) |
| Prop 4.7's owner collision | design choice: Ω-additive opponents, plus selection choice: realise x and y (Thm 5.1) |
| y realised on [e_k, e_j] | axioms (edge dichotomy), unless an edge model straddles the window (selection choice) |
| x realised | selection choice only. It needs a selected non-precise model silent on steep lines beyond the A-lines; vertex, edge and dominance arguments never force it |
| Opponent non-additivity | axioms + T ⪯ T·d at all worlds + d⁻¹ refused everywhere (optional enlargements) + realisation of both padding records (Prop 6.1) |
| σ fails globally | the chosen rule σ, not the axioms (Prop 6.2; cells SAT without σ) |
| Section separation J_d | the chosen rule σ (Prop 6.3) |

---

## 1. Setting and notation

Brief 47's setting is used throughout.
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain; models modulo null sets.
- On a mixed problem of M_k: k is the **owner** (minority world), and j, l are the **opponents**.
- Ranks on M_k:
  - at k: B 0, S 1, A 2, X 3;
  - at j and l: A 0, S 1, B 2, X 3.
- T = D_M, with M = c·1 + εΔ.
- Coherent models are D_K, for K ⊆ Δ closed and convex. They are never X, and correct on U.

**Records.** A record is r = (D_r, a → b). A(r) is the set of worlds accepting r; by (IB) it does not depend on context. P(r) is the set of indices p with C_p = a a.e. on D_r. The record is **realisable** if some coherent model equals a a.e. on D_r. For a record r and world w:
- G(r) ∋ w if r is a weak pure worsening at w; guidance forces w ∈ A(r);
- I(r) ∋ w if r is a pure improvement at w; strict (G) forces w ∉ A(r).

**Obligation lemma (audit §4).** The support-defence part of (S) is equivalent to: A(r) ∩ supp p ≠ ∅ for every r and every p ∈ P(r).

**The departure.** d = (D, S → b) is inverted in M_k, with D = D^A ⊔ D^B. b = A on D^A and b = B on D^B, both non-null, and every B-line lies below or equal every A-line in the line order of M_k (PP23 §4.2). The record d has old side S, so d is a record out of T whenever D ⊆ Sil(T).

**Hypothesis (H_d).** T ⪯_w T·d at every world w. Equivalently, A(d) = {1, 2, 3}.

**Marks.** A record r is
- **A-marked** (for d) if D^A ⊆ D_r a.e. and its old side is A a.e. on D^A;
- **B-marked** if D^B ⊆ D_r and its old side is B a.e. on D^B.

**Lemma 1.1 (PP23 Lemma 4.3, non-null form; PROVED there).** No coherent model is A a.e. on a non-null subset of D^A and B a.e. on a non-null subset of D^B. In particular no realisable record is both A-marked and B-marked, and no realisable old side carries A on part of D^A together with B on part of D^B.

---

## 2. Reductions

**Lemma 2.1 (triangles through d are decompositions; PROVED).** Every accepted triangle containing a copy of d has the form P ⪯ P·d ⪯ Q ⪯ P, with P = S on D. Its other two edges x := rec(P·d, Q) and y := rec(Q, P) satisfy x·y = d⁻¹. Conversely, every pair of records with x·y = d⁻¹ arises this way. Under (H_d), (TC) holds on all triangles through d iff, for every such pair and every world w ∉ A(d⁻¹), x and y are not both accepted at w.

*Proof.*
- Triangle edges are cyclic, so any triangle containing d can be rotated to start with d.
- (TC) is equivalent to "every accepted triangle has all three reverses" (AUDIT_completion §2).
- If w ∉ A(d⁻¹), the reverse of d is missing at w. So the triangle must not be accepted, i.e. x and y are not both in A_w.
- If w ∈ A(d⁻¹), (TC) asks for the other two reverses as well, which is a separate completion question. ∎

**Lemma 2.2 (some world refuses d⁻¹; PROVED).** Under (H_d) and direct (C), A(d⁻¹) ≠ {1, 2, 3}.

*Proof.* Otherwise T·d ≈ T. Direct (C) then makes T·d coherent, contradicting Lemma 1.1 (or Lemma H: {T·d ≠ T} = D is bounded, hence not a.e. a cone). ∎

**Lemma 2.3 (enlargement; PROVED).** Let E be fresh, non-null and in Sil(T).
- Put d′ := d ∪ (S → B on E), with E ⊆ M_k on lines below every A-line of d. If T ⪯_k T·d′, then k ∉ A(d⁻¹).
- Put d″ := d ∪ (S → A on E), with E ⊆ M_k on lines above every B-line. If T ⪯_w T·d″ for some w ∈ {j, l}, then w ∉ A(d⁻¹).

d′ and d″ are again inverted, and localized if d is.

*Proof.* At k, T·d′ is T·d with S replaced by B on E, so it is pointwise k-better, strictly on E. Strict (G) gives T·d′ ≺_k T·d. If T·d ⪯_k T, then T·d ⪯_k T ⪯_k T·d′ ≺_k T·d, which violates (TC). At an opponent, use d″, since A is correct at j and l. ∎

**Consequence and first escape.** If T dominates every localized inverted rival in its silence, which is audit's intended test (answer 4), then A(d⁻¹) = ∅ and Lemma 2.1 demands A(x) ∩ A(y) = ∅ for every decomposition. If T dominates d alone, d⁻¹ may be accepted at some worlds: single-world ties T·d ≈_w T. This is allowed (Lemma 2.2 only needs one refusing world). A tie at the owner kills Prop 4.7's mechanism at once, since that mechanism lives at k.
- The cost is the enlargements: by Lemma 2.3, T may not then dominate d′ at k (or d″ at a tied opponent).
- Classification: the strictness of d⁻¹ is forced only by **optional comparisons** (T ⪯ T·d′, T ⪯ T·d″).
- The cell runs use such ties spontaneously when strictness is not imposed. `sat_C0_sel_nostrict.out`: d⁻¹ is accepted at both opponents and refused only at the owner.
- From here on I impose **A(d⁻¹) = ∅**, which is the hard case.

---

## 3. Which records can be realised, and at which indices

**Proposition 3.1 (two types; PROVED).** Let x·y = d⁻¹, with x = rec(P·d, Q) and y = rec(Q, P). If x and y are both realisable, exactly one of the following holds:
- **Type I.** D_x ∩ D = D^A, and Q ∈ {S, B} on D^A. Then x is A-marked and y is B-marked (y retreats B → S on D^B).
- **Type II.** D_x ∩ D = D^B, and Q ∈ {S, A} on D^B. Then x is B-marked and y is A-marked (y retreats A → S on D^A).

*Proof.*
1. On D, x's old side is b and y's new side is S.
2. **Where x does not act.** On D ∖ D_x we have Q = b ≠ S, so y acts there with old side b.
3. **Where x acts.** By Lemma 1.1, D_x ∩ D cannot meet both D^A and D^B. So it lies a.e. in one of them, say D^A.
4. **Type I.** Then y's old side is B on all of D^B and A on D^A ∖ D_x (step 2). Lemma 1.1 forbids this unless D^A ∖ D_x is null. So D_x ⊇ D^A, and x is A-marked.
5. On D^A, Q ≠ A because x acts there. Where Q ≠ S the point lies in D_y, so Q ≠ X because y is realisable. Hence Q ∈ {S, B} on D^A, and y (which acts on all of D^B with old side B) is B-marked. Type II is symmetric. ∎

**Lemma 3.2 (rank pattern of marked records; PROVED).**
- An A-marked record has a loss at both opponents (on D^A: A goes to S, B or X) and is never a pure improvement there. Unless it has X on D^A it gains at k on D^A, so it is not a weak pure worsening at k.
- A B-marked record has a loss at k (on D^B) and is never a pure k-improvement. Unless it has X on D^B it gains at both opponents there, so it is not a weak pure worsening at either opponent. ∎

**Lemma 3.3 (realisers on the boundary; PROVED from strict (G) and competitiveness on supports alone).**
1. **Vertices.** C_{e_i} = V_i (lead's Lemma B).
2. **Open edges.** If supp p = {i, i′}, then C_p = D_K with K ⊆ [e_i, e_{i′}]. In particular C_p = A a.e. on M_{i″}, the third class.
3. **Faces that cannot realise each mark.**
   - An A-marked record is never realised by C_{e_k}.
   - A B-marked record is never realised at any index of the closed edge [e_j, e_l].
4. **Supports of the remaining realisers.** Every p ∈ P(A-marked) has supp p ∩ {j, l} ≠ ∅. Every p ∈ P(B-marked) has k ∈ supp p.

*Proof.*
- (2) Suppose C_p ≠ A on a non-null E ⊆ M_{i″}. Then C_p[E → A] is strictly better at i and at i′ by strict (G), so C_p is not competitive on supp p. Hence C_p = A a.e. on M_{i″}. Now take any m ∈ K with m_{i″} > 0. Lines g ∈ M_{i″} with g_{i″} very negative have m·g < 0, which gives a non-null set where D_K ≠ A. So K lies in the edge.
- (3) V_k is B on M_k. Every model selected on the closed edge [e_j, e_l] is A on M_k, by (1) for V_j, V_l and by (2) on the open edge.
- (4) This is (3) with the faces listed: the remaining supports are e_j, e_l, the edges and the interior for A-marked records; e_k, the two edges at e_k and the interior for B-marked ones. ∎

**Proposition 3.4 (where Prop 4.7's pair can be realised; PROVED; CHECKED on cells).** Take the repaired configuration of REFEREE_round46 §2.5:
- x = (A → S on D^A) ∪ (S → A on F);
- y = (B → S on D^B) ∪ (A → S on F);
- F is a set of steep lines, with z_kj below the B-lines by ε and z_kl above the A-lines by ε.

Measure positions on the edge [e_k, e_v] by m_v ∈ [0, 1]. An edge model D_{[a,b]} on [e_k, e_v] gives a class-k line crossing at c the answer B if b < c, A if a > c, and S otherwise. Then:
- **x**: realised at an interior index, or on [e_k, e_l] by an interval [a, b] with sup_{D^A} z_kl < a ≤ inf_F z_kl and b ≥ sup_F z_kl. Such a model is necessarily non-precise. x is never realised by T (T is silent on D^A), by a precise model, by a vertex, or on [e_k, e_j] or [e_j, e_l].
- **y**: realised at an interior index, or on [e_k, e_j] by any interval inside the window W := (sup_F z_kj, inf_{D^B} z_kj), precise models included. Never realised at a vertex, or on [e_k, e_l] or [e_j, e_l].

*Proof.* Direct from the interval rule, using steepness: sup_F z_kj < inf_{D^B} z_kj ≤ inf_{D^A} z_kj, and inf_F z_kl > sup_{D^A} z_kl ≥ sup_{D^B} z_kl.
- x on [e_k, e_j] would need a > sup_{D^A} z_kj (A on D^A) and a ≤ inf_F z_kj (S on F). These are incompatible.
- y on [e_k, e_l] would need b < inf_{D^B} z_kl (B on D^B) and a > sup_F z_kl (A on F). Since a ≤ b, these are incompatible.
- x on [e_k, e_l] needs a ≤ inf_F z_kl ≤ sup_F z_kl ≤ b. F is a non-null set of lines, so z_kl is not a.e. constant on it, and hence a < b.
- The other faces fail by Lemma 3.3 and by the vertex values (V_k is B on F, while V_j and V_l are A on D^B and on F). CHECKED: `forced_sat.py C0` lists the faces as [int, e02] for x and [int, e01] for y (worlds indexed from 0, k = 0). ∎

So even if the selection realises both, the forced worlds are a world of {k, l} for x and a world of {k, j} for y: different edges at the owner.

---

## 4. The main theorem

**Theorem 4.1 (retreat split; PROVED; CHECKED).**

*Assumptions.*
- Strict (G).
- A selection p ↦ C_p of coherent models, each competitive on supp p. Neither closed sections nor undominatedness is used.
- d is an inverted departure in one class M_k.

*The rule σ.* For every record r with r·y = d⁻¹ or x·r = d⁻¹ for some partner, put:
- σ(r) := G(r) ∪ {j, l} if r is realisable and A-marked;
- σ(r) := G(r) ∪ {k} if r is realisable and B-marked;
- σ(r) := G(r) if r is not realisable;
- σ(r) := any set H ⊇ G(r) that avoids I(r) and meets supp p for every p ∈ P(r), if r is realisable and unmarked. Such an H exists whenever r's own obligations are satisfiable at all, which (S) requires independently of d.

*Conclusion.* For every decomposition x·y = d⁻¹:
1. G(r) ⊆ σ(r) and σ(r) ∩ I(r) = ∅;
2. σ(r) ∩ supp p ≠ ∅ for every p ∈ P(r);
3. σ(x) ∩ σ(y) = ∅.

σ is a function of the record alone (marks, realisability and G do not depend on the role), so it respects (IB).

*Proof.*

**Step 1: G(x) ∩ G(y) = ∅.** Suppose w lay in both. Then P·d is weakly better than Q, and Q weakly better than P, pointwise at w. So d⁻¹ would be a weak pure worsening at w. But d⁻¹ is of kind M at every world: at k it gains on D^A and loses on D^B, and at an opponent the reverse.

**Step 2: properties 1 and 2.**
- Property 1 follows from Lemma 3.2 and the definitions.
- Property 2 follows from Lemma 3.3(4) for marked records. Unrealisable records have P(r) = ∅. Unmarked ones hold by the choice of H.

**Step 3: property 3, case by case.** Write Q for the intermediate model.

*Both pieces realisable.* By Prop 3.1 one is A-marked and the other B-marked. So σ(x) ∩ σ(y) ⊆ (G(x) ∪ {j, l}) ∩ (G(y) ∪ {k}) or the mirror image.
- G(A-marked) ∌ k: an X on D^A would put X in the partner's old side, but the partner is realisable.
- G(B-marked) ∌ j, l: same reason.
- With Step 1, the intersection is empty.

*x realisable and marked, y not.*
- **x A-marked.** We need G(y) ∩ {j, l} = ∅. If y were a weak pure worsening at j, Q would be A or S on D. Since x changes all of D^A, Q = S on D^A. On D^B, Q ∈ {A, S} differs from B, so x also carries old side B on D^B. That makes x B-marked as well, which is impossible for a realisable record (Lemma 1.1).
- **x B-marked.** We need k ∉ G(y). That would need Q ∈ {B, S} on D, hence Q = S on D^B and Q ≠ A on D^A. This makes x A-marked as well, again impossible.

*y realisable and marked, x not.*
- **y A-marked.** If j ∈ G(x), then Q ∈ {B, X} on D^B. y is realisable, so Q = B there, which makes y B-marked too. Impossible.
- **y B-marked.** If k ∈ G(x), then Q ∈ {A, X} on D^A, hence Q = A, which makes y A-marked too. Impossible.

*A realisable unmarked piece.* Its partner is unrealisable and has G = ∅.
- **x unmarked.** Then D^A ⊄ D_x and D^B ⊄ D_x. So y carries A on part of D^A and B on part of D^B, and is unrealisable by Lemma 1.1. A weak pure worsening of y at k needs Q ∈ {B, S} on D, but Q = A on D^A ∖ D_x. At an opponent it needs Q ∈ {A, S}, but Q = B on D^B ∖ D_x.
- **y unmarked.** Then Q ≠ A on part of D^A and Q ≠ B on part of D^B. These parts lie in D_x, with old sides A and B respectively, so x is unrealisable. A weak pure worsening of x at k needs Q ∈ {A, X} on D^A. Hence Q = X on part of D^A, and that point lies in D_y, contradicting y's realisability. The opponents are symmetric.

So H only has to avoid ∅.

*Neither realisable.* σ(x) ∩ σ(y) = G(x) ∩ G(y) = ∅ by Step 1. ∎

**Corollary 4.2 (the strong theorem fails; PROVED).** Take any admissible selection through T: T selected at an interior index, (S) with closed sections, strict (G), (IB), (TC), (LA), direct (C). Take any inverted d in Sil(T) with T ⪯_w T·d at every world, including the B-heavy localized ones satisfying P1–P3. Then:
- no decomposition x·y = d⁻¹ has x and y both obligatory and *forced* onto one world;
- whatever P(x) and P(y) are, the admissible verdict sets of x and y have disjoint members, namely σ(x) and σ(y).

What remains possible is that some *other* triangle, not through d, makes σ's verdicts inconsistent. That is the subject of §6.4.

**Remarks.**
1. **Nothing quantitative enters.** The masses, the B-heavy condition, steepness, padding mass (P3) and localisation are never used. Inversion is used only through Lemma 1.1.
2. **The context P is arbitrary.** The theorem covers every decomposition of the record d⁻¹, not just those in context T.
3. **σ is not the only escape.** On cells the SAT solver often chose the mirror for the specific pair of Prop 4.7: x at the owner, y at the opponents (`forced_sat.py C0`). That is admissible when neither record is guidance-forced at an opponent. σ is the canonical choice: its world sets are fixed by the marks.
4. **CHECKED** (`single_d_check.out`, ALL PASS). Six configurations: steep and mirror-steep padding; padding in M_2 and M_3; T answering on some lines; radial splits giving 25 inverted departures. In total 25,520 decompositions, 2,658 of them with both pieces realisable, and 0 failures of properties 1–3 under maximal obligations (every face that can realise an old side contributes its clause).

---

## 5. What is forced: the nearby true results

### 5.1 Selected-family Prop 4.7

**Theorem 5.1 (PROVED).** Let d be B-heavy and satisfy P1–P3, and let F, φ ∈ (α, β), x, y be as in Prop 4.7. Suppose:
- (a) neither x nor y is accepted at j or l;
- (b) P(x) ≠ ∅ and P(y) ≠ ∅;
- (c) k ∈ A(d) and k ∉ A(d⁻¹).

Then (TC) fails.

*Proof.* By (b) and the obligation lemma, A(x) and A(y) are nonempty. By (a) both equal {k}. Then (c) and Lemma 2.1 give a (TC) violation at k. ∎

In PP23:
- (a) came from Ω-subset coverings: Ω_j^(0)(x) = α − φ < 0 and Ω_j^(0)(y) = φ − β < 0;
- (b) came from universal coverage;
- (c) came from Theorem 4.5's systems having no ties.

Theorem 4.1 shows that (b) and (c) alone force nothing, because σ violates (a). So **(a) is the hypothesis doing the essential work.** Only (a) uses the masses. The answer to audit §5 ("is the universal-realisation hypothesis doing essential work?") is: it is needed only to make the records compulsory, and compulsoriness is harmless without (a).

### 5.2 Edges: inside or straddle

**Proposition 5.2 (edge window dichotomy; PROVED).** Use closed sections, competitiveness and strict (G). On the edge [e_k, e_j], measure positions by θ = m_j. Let 0 < s ≤ t < 1 and let P := D_{[s,t]}, the edge model on the segment θ ∈ [s, t]. Then some index λ in the open edge has C_λ = D_{[a,b]}, by Lemma 3.3, with one of:
- [a, b] = [s, t];
- s < a ≤ b < t (strictly inside);
- a < s and b > t (strictly straddling).

*Proof.*
1. **Two closed sets covering the edge.** A_k(P) and A_j(P) are closed. Every edge index lies in their union. e_k ∈ A_k(P), since V_k is k-best, and e_j ∈ A_j(P). The edge is connected, so the two sets meet at some λ.
2. **λ is not a vertex.** V_k is pointwise j-worse than P, so P ≺_j V_k. Symmetrically at e_j.
3. **Ranks along the edge.** A class-k or class-j line crosses the edge at some c. At world k, D_I is correct, silent or wrong according as I lies left of c, contains c, or lies right of c (B on M_k, A on M_j when K is on the e_k side). At world j the order is reversed. On M_l and on U both models are correct.
4. **Ruling out the comparable cases.** Suppose a ≤ s and b ≤ t, not both equal. Then C_λ is pointwise no worse than P at k and no better at j. Crossings fill (0, 1) with positive density, so the difference is strict on a non-null set. Then P ≺_j C_λ, contradicting C_λ ⪯_j P. The case a ≥ s, b ≥ t is symmetric. ∎

**Corollary 5.3.** Let W be y's window of Prop 3.4. For every [s, t] ⊂ W, either some edge model on [e_k, e_j] realises y's old side, or some edge model is silent on every class-k line crossing in [s, t].
- With precise edge models (the additive benchmark) the first alternative always holds: y is realised on [e_k, e_j].
- x has no analogue: its realisation needs silence on positive mass. Neither vertex, edge nor dominance arguments ever force silence. (Lemma 3.3 forces only unanimous-correct answers; Lemma 5.4 below pushes dominators off a rival's silence.)

Whether the straddling alternative can be sustained along a whole window is OPEN. It does not matter for Theorem 4.1.

### 5.3 Closed sections and KKM do not create realisations

**Lemma 5.3 (inheritance transfers ties, not realisations; PROVED).** Let p_n → p.
- If C_{p_n} realises r for every n, closed sections give C_p ⪯_w C_{p_n}∘r only for w ∈ A(r) and for each *fixed* rival. The rival changes with n unless C_{p_n} is eventually constant.
- If C_{p_n} = C for all n, then C_p ≈ C (Lemma A), and C_p ⪯_w C∘r for w ∈ A(r).
- Nothing forces C_p to realise r. By direct (C) and Lemma H, C_p and C may differ on any a.e.-conic set, and such a set may meet D_r.

So inheritance creates the record rec(C_p, C∘r) at the worlds of A(r). That is a *different* record unless C_p = C. (Under σ it can conflict with σ's verdicts only through a jump of the kind in Prop 6.3.) ∎

**Lemma 5.4 (KKM dominators are exposed; PP19 Lemma 0.4 restated).** Let R = N off a set E, with N undominated, and let C be a strict all-world dominator of R. Then C ≠ R on a non-null part of E.

So a rival built to carry a padding pattern on E, for example V_l[F → S], which is A on D^A and S on F, has dominators that are *not* silent on part of F. KKM dominators are pushed away from the padding patterns, not onto them.

---

## 6. The escape: costs, and the multi-departure frontier

### 6.1 Opponent non-additivity

**Proposition 6.1 (PROVED).** Take Prop 4.7's pair (x, y) with φ ∈ (α, β). Suppose A(d) = {1, 2, 3}, A(d⁻¹) = ∅, and A(x), A(y) are both nonempty (e.g. both records are selected-realised). Then some opponent accepts x or y, and Ω^(0) < 0 there.

More generally, let ℓ_j be any integrable strictly guiding additive field. Write
- a := ∫_{D^A}(ℓ_j(S) − ℓ_j(A)),
- b := ∫_{D^B}(ℓ_j(B) − ℓ_j(S)).

If b > a, every padding F with ℓ_j-mass strictly between a and b makes both records ℓ_j-negative at j. Such a padding exists because μ is atomless. If this holds at both opponents, some opponent accepts an ℓ-negative record.

*Proof.* A(x) and A(y) are disjoint and nonempty, so at most one of them contains k, and the other contains an opponent. The values are ℓ_j(x) = a − f and ℓ_j(y) = f − b, which sum to ℓ_j(d⁻¹) = a − b. ∎

By PP23 Lemma 4.1, that opponent cannot accept every Ω^(0)-positive (respectively ℓ-positive) bounded record. This is the precise price of the escape. It is exactly the non-additivity at the majority worlds that PP23 §6 asked for.

### 6.2 σ is not a global rule

**Proposition 6.2 (PROVED).** Apply σ to every localized inverted departure of every class at once, with verdicts *restricted* to the mark sets: B-marked records refused at both opponents, A-marked records refused at the owner. Let C be selected at q, and suppose C is B a.e. on some non-null set L₁ of T-silent class-k lines, and A a.e. on some non-null set L₂ of T-silent class-k lines. Then C is not competitive against T. In particular, under global σ no such C can be selected.

This includes:
- every precise model D_{{m}} with m ∈ int M;
- every small K displaced from M sideways, i.e. parallel to the edge opposite e_k.

*Proof.*
1. **The pieces.** y_C := rec(C, T) is a piece of the decomposition with Q = C, for every d. Shrink L₁ and L₂ to non-null sets that leave room above and below inside the open set of T-silent lines. Choose an inverted d with D^B ⊆ L₁ and D^A on higher T-silent lines. Choose an inverted d′ with D′^A ⊆ L₂ and D′^B on lower T-silent lines.
2. **The marks.** y_C is realisable (by C), B-marked for d and A-marked for d′.
3. **No world left.** G(y_C) = ∅: C is worse than T at k on L₂ (A against S) and worse at j and l on L₁ (B against S). So restricted σ refuses y_C at j and l (d) and at k (d′). But C must defend against T at some world of supp q.
4. **The examples.** For m ∈ int M, rotating a class-k line about a point of M near m puts m strictly on either side, on open sets of T-silent lines. For the sideways displacement, tilt the line through c ∈ int M parallel to [e_j, e_l] either way. ∎

CHECKED: in `forced_sat.py C2`, which has crossing lines lS, lT, 48 records carry both marks. Imposing σ's restrictions on the single-mark records alone is already UNSAT, because the double-marked records' partners pin them from both sides. The same happens across classes in C5 (96 records labelled by departures of M_1 and of M_2). Yet the unrestricted problem is SAT in both. So the multi-departure escape exists on cells, but it is **model-dependent**: the world at which a double-marked C defends against T is chosen per model, not by type.

### 6.3 The section cost of σ for one departure

**Proposition 6.3 (PROVED).** Let
- B_d := {p : C_p = B a.e. on D^B};
- A_d := {p : C_p = A a.e. on D^A}.

These two sets are disjoint by Lemma 1.1.

Under σ with mark-restricted verdicts, closed sections for the fixed rival T force cl(B_d) ∩ A_d = ∅ = B_d ∩ cl(A_d).

*Proof.* For p ∈ B_d, rec(C_p, T) is realisable and B-marked, and its G is empty at j and l (B is wrong there, against S). So σ gives p ∈ A_k(T) ∖ (A_j(T) ∪ A_l(T)). For p ∈ A_d, the record is A-marked and k ∉ G, so p ∈ (A_j(T) ∩ A_l(T)) ∖ A_k(T). Closedness of A_k(T) gives cl(B_d) ⊆ A_k(T), which misses A_d. Closedness of A_j(T) gives cl(A_d) ⊆ A_j(T), which misses B_d. ∎

Call this condition J_d: **no direct jump between a model strictly inside the D^B triangles and a model strictly beyond the D^A lines.**
- Continuity in measure implies it.
- So do precise edge sweeps: B_d ends at m_j = inf_{D^B} z_kj and A_d starts at sup_{D^A} z_kj, which is larger.
- It is not implied by (S), and it is not needed by every escape. A general escape needs only, for each fixed X, that the world sets of the pieces rec(C_p, X) inherit along limits.

**Selection behaviour near T.**
- For one departure, the escape asks nothing special of the selection near T. T and its tie partners are silent on D, so they carry neither mark, and σ only adds J_d.
- For all departures at once (§6.2), the models that matter are those near M that cross T's silent lines both ways. Examples are refinements of T, and the T-mimic collar of PP19 Thm 1 if it contains such models. Each must defend against T at a world chosen so that none of its x-records rec(T·d, C) is forced there.

### 6.4 What an obstruction would have to look like

**Proposition 6.4 (star reduction; PROVED).** Let 𝒟 be a family of inverted departures with A(d) = {1, 2, 3} and A(d⁻¹) = ∅ for every d ∈ 𝒟. Let C be selected at q. Then
- V(C) := A(rec(C, T)) is a nonempty set meeting supp q (competitiveness);
- V(C) ∩ A(rec(T·d, C)) = ∅ for every d ∈ 𝒟 (Lemma 2.1 with Q = C).

Hence (S) with T selected fails as soon as, for some selected C and every world w ∈ supp q ∖ I(rec(C, T)), some d ∈ 𝒟 has rec(T·d, C) forced to w: by guidance, or by obligations whose every admissible transversal contains w.

Theorem 4.1 says a single d never forces such a world once V(C) is chosen by C's mark. So a star obstruction needs at least two departures, crossing in the sense of §6.2. That is exactly where σ breaks. The cells show such stars are not forced there.

**Proposition 6.5 (domination records as pieces; PROVED).** Suppose a KKM domination record rec(C, R) is accepted at every world (C selected, C ⪯ R everywhere) and equals one piece of a decomposition of d⁻¹, with A(d⁻¹) = ∅. Then its partner must be refused at every world. If the partner is realised by a selected model, (TC) or (S) fails.

*Proof.* Lemma 2.1 and the obligation lemma. ∎

This is the strongest form of "use KKM aggressively". Lemma 5.4 restricts it: the domination record must change R on R's own modification set. So the piece must be shaped like the *rival's* modification, not like the padding. No instance is known.

**Cell evidence (CHECKED, `forced_sat.py`).** All lines lie in M_1 (one config also uses M_2) and meet T1's credal set (ε = 3/10), so T is silent on all of them. The steep padding line F = (0.40, 0.95) satisfies P2 relative to lB = (0.55, 0.55) and lA = (0.65, 0.65). Constraints:
- maximal support-sensitive obligations (every face that can realise an old side contributes its clause);
- strict (G);
- undominatedness of every coherent-old record's source;
- direct (C) for records with non-realisable new side;
- full (TC) through P1/P2 over all composable pairs on the sub-domain {A, S, B};
- every inverted departure accepted at every world, and its inverse refused at every world.

| Config | Pieces | Inverted departures | Result | σ imposed | Forced padding verdicts |
|---|---|---|---|---|---|
| C0: lB, lA, F | 3 | 1 | SAT | SAT | none (36 checked) |
| C1: lB², lA², F (radial) | 5 | 25 | SAT | SAT | none (60 checked) |
| C2: lB, lA, lS, lT, F (crossing departures) | 5 | 2 | SAT | **UNSAT** (48 double-marked records) | none |
| C3: lB², lA, F, G (both steep directions) | 5 | 7 | SAT | SAT | none |
| C4: lB, lA, F, G, lS | 5 | 1 | SAT | SAT | none |
| C5: lB, lA in M_1; mB, mA in M_2; F | 5 | 3 (one per class, one two-class) | SAT | **UNSAT** (96 records with two labels across classes) | none |
| Ω-subset control, C0, C1, C2 (masses 3 on lB, 1 on lA, 2 elsewhere) | | | UNSAT (reproduces Prop 4.7) | | |
| Ω-subset control, C1 without F | 4 | 25 | SAT (the obstruction needs the steep line, as REFEREE_round46 §2.5 says) | | |

The mirror rule σ′ (A-marked records at the owner) is UNSAT everywhere, as it must be. A-marked records can be weak pure worsenings at an opponent, so σ′ violates guidance.

**What cells omit.** X values and unanimous problems; masses (irrelevant here: no Ω outside the control); unbounded records; (S) itself: sections, KKM and selection values are not modelled. Maximal obligations are an upper bound on any selection's obligations, so SAT transfers to every selection *at the level of these clauses*.

**CONJECTURE 6.6.** Let 𝒟 be the family of all localized inverted departures in Sil(T). Then there is a record-based verdict assignment, on records whose old sides are realised by selected models of a selection through T, with:
- strict (G) and (TC);
- every support-sensitive obligation met;
- A(d) = {1, 2, 3} and A(d⁻¹) = ∅ for every d ∈ 𝒟.

By Prop 6.2 such an assignment must choose each double-marked model's defence world individually. This is the selected-family form of PP23 Conjecture 4.9, and it now covers the B-heavy departures too. Prop 4.7 does not obstruct it once the opponents are non-additive (Thm 5.1, Prop 6.1).

---

## 7. Answers to the brief

| Brief item | Answer |
|---|---|
| Prove the strong theorem | **False as stated** (Cor 4.2). For every admissible selection and every single inverted d, the padding records' admissible verdict sets have disjoint members. The explicit escape is σ: B-retreats to the owner, A-retreats to the opponents. |
| Support-sensitive lemma | Gives hitting constraints. By Lemma 3.3 the supports of A-retreat realisers always meet {j, l}, and those of B-retreat realisers always contain k. That is why no collision is ever forced. |
| Closed sections and inheritance | Transfer ties, not realisations (Lemma 5.3). Edge dichotomy: inside-or-straddle (Prop 5.2). Cost of σ: J_d (Prop 6.3). |
| Vertex lemma | Decides which faces can realise each mark (Lemma 3.3). Vertex-realised pieces are never forced to collide (contained in Thm 4.1). |
| Theorem C | Forces many selected values, but no particular bounded two-set pattern: the edge dichotomy shows a straddling alternative. Not needed. |
| KKM dominators | Exposed (Lemma 5.4), so never realisers of the padding they dominate. The only forcing route left is domination records as pieces (Prop 6.5). |
| PP19 compensation | Concerns fills of T; it constrains dominators' compensation but produces no d-piece with a forced world. Not used. |
| Theorem Z vertex fill | Its dominator is exposed on the filled set (step 5). Same conclusion as Lemma 5.4. |
| Pointwise sweep vs joint realisation | On an edge, sweep is (essentially) the s = t case of Prop 5.2. The joint version holds only as inside-or-straddle. Irrelevant to the collision by Thm 4.1. |
| Exact escape and its cost | σ (Thm 4.1). Costs: Ω-negative (indeed non-additive) acceptance at an opponent whenever both padding records are live (Prop 6.1); J_d for σ (Prop 6.3); inverses refused at every world only via optional dominations of enlargements (Lemma 2.3). For all departures together the escape must be model-dependent (Prop 6.2); cells SAT. |

**Most important next step.** Attack Conjecture 6.6 through the star reduction (Prop 6.4). For each selected model near M that crosses T's silent lines both ways, choose its defence world against T. The x-records rec(T·d, C) are the only records that can block that choice. Either:
- find a rule, presumably lexicographic in the line order through M, that keeps every x-record off C's chosen world while meeting their own obligations; or
- produce two crossing departures whose x-records are both forced, by edge obligations plus guidance, onto the two worlds of some edge-selected C's support. That would be the genuine selected-family obstruction.
