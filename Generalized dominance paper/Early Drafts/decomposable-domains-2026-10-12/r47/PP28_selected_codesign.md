# PP28. Selected-family co-design for incoherence certificates

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact finite computation (rational geometry; boolean matrices over every model of a cell set; one LP cross-check). Cells check record bookkeeping only. They say nothing about (S). NUMERICS: none. CONJECTURE / OPEN: as stated.

**Scripts** (`r9/PP28_py/`; run `python3 -B <script>` inside the folder; outputs in the `.out` files):

| Script | Content | Label |
|---|---|---|
| `lib28.py` | exact class-1 line geometry, advice of D_K, line order | (library) |
| `cells28.py` | the B-heavy padding configuration on radially split cells, with a steep silent padding line and a steep line where T says B; Theorems 3.1, 4.1, 5.1 on cells; three allocations | CHECKED |
| `forced_list.py` | the forced pairs of Theorem 5.1 and their realisers | CHECKED |
| `polarity_witness.py` | a (TC) failure created by polarity reallocation over Ω (§6.3) | CHECKED |
| `separation_check.py` | Lemma 2.1 on cells against 400 random credal sets | CHECKED (LP) |

**Inputs.** Brief 47; AUDIT_selected_realizability §§3–5 (the obligation lemma); AUDIT_answers47 (binding); PP23 §§1–4 (Lemmas 1.1, 4.3, 4.4, Theorem 4.5, Props 4.6–4.7); REFEREE_round46 §2.5 (repaired Prop 4.7, P1–P3) and R46.1; AUDIT_completion (rules I–IV, F1/F2); LEAD_selection_count (Lemmas A, B); PP18–19 and REFEREE_Z_PP19 (Lemma H); PP26 Theorem V and Prop 1.4. Only Brief 47's axioms are used. Transitivity, absence of ties and continuity are never assumed.

---

## 0. Verdict

1. **The incoherence-certificate mechanism survives selected-family obligations, for a large class of families (PROVED).** The key fact is geometric.
   - **Separation lemma (Lemma 2.1).** If d is an inverted departure and d⁻¹ = x·y with both old sides realised by coherent models C_x, C_y, then C_x and C_y have **disjoint** credal sets. In fact a line of a class that d touches has one of them strictly inside its corner triangle and the other strictly outside it. One realiser says A on all of that class's A-part of d; the other says B on all of its B-part.
   - So a decomposition of d⁻¹ can be compulsory at all only if the selected family contains a **separated pair**. This is the "two-set pattern" invariant the brief anticipated: each piece is a two-set pattern realised by one model, and the two pieces need two disjoint models.
2. **The adversary is admitted (Theorem 4.1, PROVED).** The family is the vertices plus any family of coherent models whose credal sets pairwise intersect. Add every inverted departure at every world on top of any (TC) base whose non-guidance comparisons have selected-realised old sides. Then:
   - (G), (IB) and (TC) hold;
   - the selected models stay undominated, with no ties at any world;
   - every obligation of the base is kept;
   - each selected N strictly dominates N·d at all three worlds, for every inverted d inside N's silence;
   - the closure rules I–IV force nothing.

   This covers the repaired B-heavy padding configuration (P1–P3) that universal Prop 4.7 excludes. §4.2 gives an explicit instance:
   - index domain int Δ ∪ {e₁, e₂, e₃}, with T on M and the segment models D_[m₀,p] elsewhere;
   - the obligatory records listed explicitly; Prop 4.7's padding record x is obligatory there;
   - accepting worlds within supp(p).

   The omitted padding record y has no realiser, so no closure rule and no section requirement can mention it.
3. **Sections (Prop 3.3, PROVED).** The certificate layer is section-neutral. For each fixed X and world w, the full section is the base section, possibly together with one fibre {p : C_p = C} of the unique coherent C with X = C·d. So, absent all-world ties, closed base sections give closed full sections. I do **not** verify closedness of the base sections for the Ω base of §4.2; I verify only the support half of (S) there.
4. **Growth (Theorem 5.1, PROVED; Prop 5.2, PROVED).** A new coherent candidate adds conflicts only through separated pairs.
   - Over Ω-type bases, a separated pair is fatal for B-heavy certificates in its band exactly when a cone condition on the "padding types" of the pair holds (Theorem 5.1).
   - For small (point-like) inner models this condition is **crossing at the separating class's vertex** (Prop 5.2). By the median rule every generic pair of distinct points is crossed at exactly one vertex region.
   - Hence a forcing-free family of point-like inner models lies on one ray through a vertex, or has at most three points (Cor 5.3).
   - Fat models avoid this by overlapping.
   - Growth rule: overlap is free; separation must be nested at the separating class.
5. **All decompositions matter (CHECKED, Example 5.4).** Two precise models, or even one precise inner point together with one outside model, force a decomposition that Prop 4.7's split misses. Its padding sits on a steep line where **T says B**, not where T is silent. So the audit's observation ("T and all precise models do not realise x") is specific to Prop 4.7's split. Over Ω the B-heavy certificate dies as soon as such a pair is selected.
6. **Where the mechanism stops (§6).**
   - Every (S)-system contains separated non-vertex selected models (Prop 6.1, PROVED, via the edges).
   - Supports never force a conflict: a polarity allocation always meets them (Lemma 3.4, PROVED).
   - But over an Ω base, polarity reallocation breaks (TC) (CHECKED witness, §6.3). Ω cannot run the edges anyway.
   - Region-first lexicographic repairs at a majority world are excluded by a localized Theorem V (Lemma 6.2, PROVED).
   - **So the open problem is the base layer near the boundary**, stated precisely as (E) in §6.4.

---

## 1. Setting and notation

Brief 47's setting. On a mixed problem of class M_k the values are A (majority answer), S, B (minority answer) and X. World k ranks them B 0, S 1, A 2; the two majority worlds rank them A 0, S 1, B 2. A record r = (D, a → b) has old side a and new side b on its support D. All common-context copies share a verdict (IB).

**Lines and charts.** A line of M_1 is given by its edge coordinates (z₁₂, z₁₃): where it meets [e₁, e₂] and [e₁, e₃], measured from e₁. Its corner triangle is tri(ℓ) = {m : m₂/z₁₂ + m₃/z₁₃ < 1}. D_K says:
- B on ℓ if K ⊂ tri(ℓ);
- A if K misses the closed triangle;
- S otherwise.

The line order is ℓ ≤ ℓ′ iff tri(ℓ) ⊆ tri(ℓ′). Write (u, v) := (log m₂/m₁, log m₃/m₁) for the log-ratio chart at e₁, and similarly at e₂ and e₃. For points k, k′ of the open simplex, every M_1-line through k has k′ on its closed e₁-side iff u′ ≤ u and v′ ≤ v. (Write the line as −m₁ + a m₂ + b m₃ = 0 with a, b ≥ 0. Then k′·g = k′₁(−1 + a k′₂/k′₁ + b k′₃/k′₁) ≤ (k′₁/k₁)(k·g) = 0.) The two extreme lines (a = 0 or b = 0) show that the condition is also necessary. Call k′ **e₁-below** k if this holds, and call k and k′ **crossed at e₁** if (u′ − u)(v′ − v) < 0.

**Inverted departures** (PP23 §4.2). d = (D, S → b), with b ∈ {A, B}. For each touched class k, both D_k^A and D_k^B are non-null, and line(g) ≤ line(g′) for a.e. g ∈ D_k^B, g′ ∈ D_k^A. Lemma 4.3 (PP23): no coherent model says B at g and A at g′ when line(g) ≤ line(g′). Its proof uses only convexity of K, so it holds for every closed convex K ⊆ Δ, vertices and edges included.

**Obligations** (audit §4). For a selection p ↦ C_p put P(r) = {p : C_p = a a.e. on D}. The support-defence part of (S) is: A(r) ∩ supp p ≠ ∅ for every p ∈ P(r). A record is **selected-realised** if P(r) ≠ ∅, and **𝒮°-realised** if some p ∈ P(r) has a non-vertex value.

**Base systems.** A base is a family of record-based relations B_i = W_i ∪ 𝒞_i, where:
- W_i is weak guidance at i;
- every record in 𝒞_i is selected-realised and not a pure improvement at i;
- each B_i satisfies (TC).

A **linear base** is the special case 𝒞_i ⊆ {r : r ≥_i 0} for a record-based, strictly guiding linear order ≤_i on models; Ω (PP23 §3) is one. 𝓘_i denotes a record-based set of bounded inverted departures. The full system is

  X ⪯_i Y :⟺ rec(X, Y) ∈ W_i ∪ 𝒞_i ∪ 𝓘_i.

---

## 2. The separation lemma

**Lemma 2.1 (classification of realisable decompositions; PROVED).** Let d be inverted, with new side b on D, and let x·y = d⁻¹. Write the triangle as P ⪯ Q ⪯ R ⪯ P with R ⪯ P the copy of d, x = rec(P, Q), y = rec(Q, R). Split D into:
- D₁ = {Q = S}: x changes b → S, y is trivial;
- D₂ = {Q = b}: x is trivial, y changes b → S;
- D₃ = {Q ∉ {S, b}}: x changes b → Q, y changes Q → S.

Write F for supp x ∖ D = supp y ∖ D (the **padding**), and e = rec(R|_F → Q|_F). Suppose both old sides are coherent-realisable. Then in each touched class k exactly one of the following holds:
- **(b) "A-first":** D₁ ∪ D₃ = D_k^A, D₂ = D_k^B, Q = B on D₃. Then x's old side is A on D_k^A and R on F, and y's old side is B on D_k^B ∪ D₃ and Q on F.
- **(c) "B-first":** D₁ ∪ D₃ = D_k^B, D₂ = D_k^A, Q = A on D₃. Then x's old side is B on D_k^B and R on F, and y's old side is A on D_k^A ∪ D₃ and Q on F.

(All equalities hold within class k, up to null sets.)

*Proof.* x's old side on D is b on D₁ ∪ D₃. It contains no inverted pair (Lemma 4.3, non-null form), so D₁ ∪ D₃ misses D_k^A or D_k^B. Suppose it misses D_k^B. Then D_k^B ⊆ D₂, so y's old side is B on D_k^B, and y's old side on D₂ ∩ D_k^A would be A. Coherence of y then forces D₂ ∩ D_k^A to be null. So D₂ = D_k^B and D₁ ∪ D₃ = D_k^A. On D₃ ⊆ D_k^A, Q ∉ {S, A} and Q is regular (a coherent old side is never X), so Q = B. This is (b). The other case is symmetric, giving (c). ∎

**Corollary 2.2 (separated realisers; PROVED).** In either case one realiser says A a.e. on D_k^A and the other says B a.e. on D_k^B. Take Lebesgue points g ∈ D_k^B and g′ ∈ D_k^A with line(g) ≤ line(g′). Then the B-realiser's K′ lies in tri(line g) ⊆ tri(line g′), and the A-realiser's K misses the closed tri(line g′). So **K ∩ K′ = ∅**, separated by a line of class k with K′ on the corner side. In particular:
- the two realisers are distinct (no single model realises both pieces);
- no decomposition is doubly realised by models whose credal sets meet. ∎

CHECKED (`separation_check.out`). The cell set is the one of §7. The pool is 400 random rational credal sets (points, segments and triangles). I examined the 26 inverted departures out of the all-silent cell model, and all their decompositions. That gives 834 doubly realised decompositions and 16,150 realiser pairs. In every pair the credal sets are disjoint (LP feasibility test).

**Remark.** Corollary 2.2 is the precise form of the audit's point that "one model must realise both parts of a pattern simultaneously". Each *piece* of a decomposition is a two-set pattern: its D-part together with its padding part. Each piece must be realised by one model, and the two pieces need two separated models. Pointwise sweeping cannot produce such a pair.

---

## 3. Certificates over an arbitrary base

**(iii_sel).** For every world i and every d ∈ 𝓘_i, no x, y ∈ 𝒞_i satisfy x·y = d⁻¹.

**Theorem 3.1 (selected room reduction; PROVED).** Let B be a base system (not necessarily linear) and 𝓘 any record-based sets of bounded inverted departures. Then W ∪ 𝒞 ∪ 𝓘 satisfies strict (G) and (IB). It satisfies (TC) iff (iii_sel) holds.

*Proof.* (IB) holds because every piece is record-based. For strict (G): an inverted departure has a loss at every world (PP23 Thm 4.5(4)), so it is never a pure improvement, and 𝒞 excludes pure improvements by definition.

For (TC) use PP23 Lemma 1.1 with 𝒜_i = (𝒞_i ∖ W_i) ∪ 𝓘_i (all of kind M).

*(P1) pairs.*
- Inside 𝒞 they are excluded by the base's own (TC).
- A pair (d, c) with c ∈ 𝒞_i: c has a coherent (selected) old side. Both records are accepted at i, so neither is a pure improvement there. Lemma 4.4 then says neither d·c nor c·d is of kind I. Lemma 4.4 uses only Lemma 4.3, which holds for every coherent model.
- A pair (d, d′) composes only on disjoint supports and keeps d's loss.

*(P2) triangles.*
- All-𝒞 triangles are handled by the base.
- A triangle with an 𝓘-edge d, say R ⪯ P, has its other two edges x·y = d⁻¹. If one of them is in 𝓘, the third has old side b on supp d. That old side is not coherent, so the third edge is not in 𝒞; it is not a departure either, so it is guidance, and that is excluded exactly as in PP23 Thm 4.5.
- If x, y ∈ 𝒞_i, the reverse d⁻¹ is needed. It is never accepted: its old side is not coherent, it is not a departure, and it is of kind M. So (TC) holds iff no such triangle exists, which is (iii_sel). ∎

This is PP23 Theorem 4.5 with two generalisations:
- the covering part is only selected-realised (audit §3);
- the base need not be a linear order. Only the base's own (TC) is used.

**Proposition 3.2 (closure is idle; PROVED).** Assume (iii_sel), and that every selected model is competitive in the base (for every X there is i ∈ supp p with rec(C_p, X) ∈ B_i). Then:
- (a) **Protection (rule III).** No X ≠ C_p has X ⪯_i C_p at every world unless the base already has it. In a linear base no selected model is weakly dominated at all.
- (b) **Ties (rule IV).** The certificate layer creates no tie at any world.
- (c) **Triangle completion (rule II).** The full system has no accepted triangle that lacks a reverse.
- (d) **Domination.** If N is silent on supp d and d ∈ 𝓘₁ ∩ 𝓘₂ ∩ 𝓘₃, then N ⪯_i N·d at every i and N·d ⪯_i N at no i.

*Proof.*
- (a) rec(X, C_p) ∈ 𝓘 would make the new side C_p carry an inverted pattern, which contradicts Lemma 4.3. So every acceptance X ⪯_i C_p is a base acceptance. In a linear base, X <_i C_p would then hold at every i. Competitiveness gives C_p ⪯_j X at some j:
  - via the base, this contradicts the strict linear order;
  - via 𝓘_j, X = C_p·d′ and rec(X, C_p) = d′⁻¹ is not accepted anywhere.
- (b) A tie through 𝓘 needs d⁻¹ accepted, and it never is.
- (c) Theorem 3.1.
- (d) d⁻¹ is refused everywhere, as in (b). ∎

So the full system adds strict dominations and nothing else. All verdicts of the base, its strict parts included, are preserved, so this is an exact extension in the sense of AUDIT_completion §3.

**Proposition 3.3 (sections; PROVED).** Fix X and w. Then

  {p : C_p ⪯_w X} = {p : rec(C_p, X) ∈ B_w} ∪ J_w(X),

where J_w(X) is either empty or the fibre F_C = {p : C_p = C} of the unique coherent C with X = C·d for some bounded inverted d. Consequently, suppose every base section is closed and no two distinct selected models tie at all worlds. Then every full section is closed.

*Proof.* Suppose X = C_p·d = C_q·d′. Then C_p and C_q agree off the bounded set supp d ∪ supp d′. Their disagreement set is conic, so they agree a.e. (Lemma H). Hence J_w(X) ⊆ F_C, and since 𝓘_w is record-based, J_w(X) is all of F_C or empty.

For the second claim: a coherent C is never of the form C′·d, by Lemma 4.3. So the full sections at X = C coincide with the base sections there. By LEAD Lemma A, Φ_C = ∩_w A_w(C) is then closed, and without ties Φ_C = F_C. ∎

**Lemma 3.4 (supports never force the conflict; PROVED).** Assume strict (G), and that every selected model is competitive on its support. Take a doubly realised decomposition as in Lemma 2.1, and call the piece whose old side is A on D_k^A the **A-holder** and the other the **B-holder**. Then:
- every realiser of the A-holder has an index p with supp p ∩ {majority worlds of k} ≠ ∅, and the A-holder is not a pure improvement at either majority world;
- every realiser of the B-holder has k ∈ supp p, and the B-holder is not a pure improvement at k.

*Proof.*
- The A-holder changes A on D_k^A, which is a loss at both majority worlds. Its realiser says A on a non-null part of M_k, so it is not V_k (which says B on M_k) and its index is not e_k.
- The B-holder changes B on D_k^B, which is a loss at k. Its realiser says B on a non-null part of M_k. Edge models on the opposite edge say A a.e. on M_k (PP19 Thm 4(d), first step: by strict (G) and competitiveness at the edge's worlds). So the realiser's index has p_k > 0. ∎

So a **polarity allocation** is always available as far as supports go: A-holders at majority worlds, B-holders at the owner world. Any forced conflict comes from the base, never from supp(p).

---
## 4. The adversary admitted: an intersecting core

**Theorem 4.1 (intersecting core; PROVED).** Let the selected values consist of:
- the vertex models V_1, V_2, V_3;
- a family 𝒮° of coherent D_K whose credal sets K pairwise intersect.

The family may be of any size, and the index assignment and multiplicities are arbitrary. Let B be any base system whose 𝒞_i consist of 𝒮°-realised records. Let 𝓘_i be **all** bounded inverted departures, at every world. Then (iii_sel) holds, so Theorem 3.1 and Props 3.2–3.3 apply. In particular:
- if every C ∈ 𝒮° is base-competitive on its support, all support-defence obligations of 𝒮 are met;
- every N ∈ 𝒮° strictly dominates N·d at all three worlds, for every bounded inverted d inside N's silence.

*Proof.* By Corollary 2.2, a decomposition with x, y ∈ 𝒞_i needs two 𝒮°-realisers with disjoint credal sets, and there are none.

Vertex obligations are met by guidance: V_k is k-correct everywhere, so every record with old side V_k is a weak worsening at k. A vertex-realised piece that is not 𝒮°-realised lies outside 𝒞, so it can be accepted only as guidance. Lemma 4.4 handles that case inside Theorem 3.1. ∎

**4.2 Explicit instance for the repaired B-heavy configuration.** Take ε = 3/10, c = 7/30 and m₀ := c·1 + ε e₂ ∈ M (a vertex of M). I list each element the brief asks for.

- **Index domain and values.**
  - I = int Δ ∪ {e₁, e₂, e₃}.
  - C_{e_k} = V_k.
  - C_p = T for p ∈ M.
  - C_p = D_[m₀,p] (a segment) for p ∈ int Δ ∖ M.

  All non-vertex credal sets contain m₀, so Theorem 4.1 applies.
- **Base.** Ω (PP23 §3): a record-based, strictly guiding linear order at each world.
  - 𝒞_i = {r : P(r) contains an interior index, Ω_i(r) ≥_lex 0}.
  - 𝓘_i = all bounded inverted departures.
- **Obligatory records.** r is obligatory iff its old side, on supp r, is the restriction of T, of some D_[m₀,p], or of some V_k. Every interior index has full support. PP23 Thm 3.1(e) gives each such r an Ω-acceptable world, so the obligation is met in 𝒞. Vertex obligations are met by guidance (Theorem 4.1).
- **Accepting worlds.** A(r) = {i : Ω_i(r) ≥_lex 0} for obligatory non-vertex records. For other records, A(r) is the set of guidance worlds, together with all three worlds when r is an inverted departure.
- **The adversary (class 1).** Lines are written (z₁₂, z₁₃).
  - ℓ_B = (4/5, 11/20); ℓ_A = (41/50, 57/100), with ℓ_B ≤ ℓ_A; the steep line ℓ_F = (1/2, 9/10).
  - T is silent on all three (CHECKED exactly).
  - D^B and D^A are the cones over small neighbourhoods of ℓ_B and ℓ_A, cut to the annulus 1 ≤ |g| ≤ 2. Their Gaussian masses satisfy β > α (B-heavy). F is a steep set near ℓ_F with mass φ ∈ (α, β).
  - **P1:** ess inf z over D^B is ≈ (4/5, 11/20) > 0.
  - **P2:** z₁₂(F) ≈ 1/2 < 4/5 − ε′ and z₁₃(F) ≈ 9/10 > 57/100 + ε′.
  - **P3:** φ ∈ (α, β), available for small α and β.

  All these conditions are open, so they persist on small neighbourhoods.

**The fate of every padding record (PROVED; CHECKED on cells §7).**

| Decomposition of d⁻¹ | x (old side; obligatory?) | y (old side; obligatory?) | verdict |
|---|---|---|---|
| Prop 4.7's split | A on D^A, S on F; **yes**, by C_p with p = p₁ = (3/10, 1/20, 13/20), and on an open set of p (CHECKED: [m₀,p₁] says A on ℓ_A and S on ℓ_F) | B on D^B, A on F; **no** | x ∈ 𝒞₁ only (Ω₁ = 2(φ−α) > 0 > α−φ = Ω₂ = Ω₃). y is refused everywhere. |
| padding on a steep line where T says B (ℓ_G = (3/4, 97/100)) | A on D^A, B on G; **yes** (e.g. p = (1/10, 1/10, 4/5)) | B on D^B, A on G; **no** | as above |
| every other decomposition | at most one piece 𝒮°-realised (Cor 2.2) | | (iii_sel) holds |

y is not obligatory because:
- every D_[m₀,p] contains m₀, which says A on ℓ_B (CHECKED), so none of them says B on D^B;
- V₁ says B on F, not A;
- V₂ and V₃ say A on D^B.

y is of kind M at every world, is not a departure, and is not in 𝒞, so it is refused at every world.

**Why the omitted records are not forced back.**
- **(IB) copies.** Every copy of y has the same old side, and that old side is no selected value on supp y. So no comparison out of a selected model is ever a copy of y.
- **Triangle completion (II).** By Theorem 3.1, no accepted triangle through d exists at all.
- **Protection (III).** Prop 3.2(a): no selected model has a weak all-world dominator.
- **Ties (IV).** None exist (Prop 3.2(b) and linearity of Ω).
- **Sections.** By Prop 3.3, sections gain only fibres. y never occurs as rec(C_p, X), so no section mentions y.

**Sections verified, precisely.**
- (i) The support half of (S) at every p ∈ I.
- (ii) Section-neutrality of the certificate layer (Prop 3.3).
- (iii) Nothing about closedness of the Ω-lex base sections along this selection. I do not claim them, and they fail in general: lexicographic sublevel sets are not closed. §6.2 shows that Ω cannot be the base near the edges anyway.

**Corollary 4.3 (PROVED).**
- (a) **Selected Conjecture 4.9.** For intersecting families, all inverted departures (A-heavy and B-heavy, every mass ratio, every class) are accepted at every world on top of any covering subset of Ω drawn from 𝒮°-realised records. No list colouring is needed.
- (b) **Non-endorsement.** In §4.2 no integrable strictly guiding field endorses the comparisons out of T at any world. Inverted departures inside Sil(T) with B-mass → 0 are accepted at the majority worlds, and those with A-mass → 0 at the owner world. PP23's computation after Conjecture 4.9 then gives the failure at each world.
- (c) **The extra hypothesis in Prop 4.7 does essential work.** Under selected obligations, the B-heavy configuration is dominated at all three worlds.

---

## 5. Growth: separated pairs and the invariant

From now on the base is Ω and every non-vertex index is interior. An **allocation inside Ω** is any choice of 𝒞_i ⊆ {Ω_i ≥_lex 0} ∩ {𝒮°-realised} that puts every obligatory record into some 𝒞_i.

Fix a bounded inverted d in class 1 alone with Ω₁(d) <_lex 0 <_lex Ω₂(d), Ω₃(d). Under Ω this is the B-heavy case, β > α. Call a decomposition (x, y) of d⁻¹ **forced** if:
- both x and y are 𝒮°-realised;
- Ω_j(x) <_lex 0 and Ω_j(y) <_lex 0 for j = 2, 3.

**Theorem 5.1 (exact criterion; PROVED).** Some allocation inside Ω admits d ∈ 𝓘₁ ∩ 𝓘₂ ∩ 𝓘₃ with (TC) iff no forced decomposition exists.

*Proof.*
- (⇐) Let 𝒞₁ consist of the realised records with Ω₁ ≥ 0 and Ω₂, Ω₃ < 0. Let 𝒞_j (j = 2, 3) consist of all realised records with Ω_j ≥ 0. Every realised record has some world with Ω ≥ 0 (PP23 Thm 3.1(e)), so obligations are met.
  - At j = 2, 3, Ω_j(x) + Ω_j(y) = Ω_j(d⁻¹) <_lex 0, so x and y are not both in 𝒞_j.
  - At world 1, x, y ∈ 𝒞₁ would make the decomposition forced.
  - Theorem 3.1 finishes the argument.
- (⇒) In a forced decomposition both pieces are obligatory, and world 1 is their only Ω-acceptable world. Supports are full, so any allocation inside Ω puts both into 𝒞₁, and (iii_sel) fails. ∎

**Padding form.** By Lemma 2.1, write the forced pieces with realisers C_A (A on D^A) and C_B (B on D^B). Their padding is e = (F, a_F → b_F) with F ⊆ G := {C_A ≠ C_B} ∖ D. Let (ω₂, ω₃) be the Ω-densities of e at worlds 2 and 3. Per step:
- on M₁: A-ward (−1, −1), B-ward (+1, +1);
- on M₂: A-ward (+2, −1), B-ward (−2, +1);
- on M₃: A-ward (−1, +2), B-ward (+1, −2);
- on U: nothing (coherent models agree there).

In case (b), e runs C_A → C_B. The pair is forced iff Ω_j(e) ∈ (−β − μ(D₃), −α − μ(D₃)) for j = 2, 3. In case (c), e runs C_B → C_A. The pair is forced iff Ω_j(e) ∈ (α + μ(D₃), β + μ(D₃)) for j = 2, 3. (Rank bookkeeping as in PP23 Prop 4.7.)

**Corollary 5.1′ (cone form; PROVED).** Let (C, C′) be a selected pair, with C saying A on a non-null set H ⊆ Sil(T) ∩ M₁, C′ saying B on L ⊆ Sil(T) ∩ M₁, and lines(L) ≤ lines(H) on non-null pieces (a **straddle**). Then some B-heavy certificate d with D^A ⊆ H and D^B ⊆ L has a forced decomposition of type (b) iff the padding cone of C → C′ on G meets the open negative quadrant. That holds iff G contains, on non-null sets:
- an M₁-point where C′ is A-ward of C (type **1A**); or
- both an M₂-point and an M₃-point where C′ is B-ward of C (types **2B** and **3B**).

For type (c), with the roles swapped, the condition is: **1B**, or both **2A** and **3A**.

*Proof.* Achievable vectors ∫_F ω form the range of an atomless vector measure, hence the zonoid {∫ fω : 0 ≤ f ≤ 1} (Lyapunov). It lies in the closed cone generated by the essential range of ω, and it contains small multiples of each present type. The boxes of Theorem 5.1 lie in the open quadrant. Shrinking α and β, with β/α large, puts a box around any direction of that quadrant. The listed combinations are exactly those whose positive hull meets the open quadrant: (−1, −1) itself, and (−2, 1) + (1, −2) = (−1, −1). No other combination of the table reaches the open quadrant. ∎

**Proposition 5.2 (point-like inner pairs; PROVED).** Let K and K′ be small discs about centres k ≠ k′ in int M, with generic centres (no equality between the relevant log-ratios). Then (K, K′) straddles in at least one of the orders (b), (c), with K the A-side in order (b) iff u > u′ or v > v′. It forces a class-1 B-heavy certificate, in some order, iff **k and k′ are crossed at e₁**: (u′ − u)(v′ − v) < 0.

*Proof.* Inner models agree with T where T answers, so G consists of lines through M. On such lines the types are decided by the following strict inequalities (§1; the extreme lines of each pencil give necessity):
- 1A (in case (b), with C at k): u′ > u or v′ > v;
- 2B: u′ > u or v′ − u′ < v − u;
- 3B: v′ > v or v′ − u′ > v − u.
Straddling (b) needs u > u′ or v > v′. If the centres are nested (u′ ≤ u, v′ ≤ v), there is no 1A, and 2B and 3B require opposite strict inequalities, so they cannot both occur. If the centres are crossed, 1A occurs. Case (c) is symmetric: 1B iff u > u′ or v > v′, 2A iff v − u < v′ − u′, 3A iff v′ − u′ < v − u. ∎

**Corollary 5.3 (dimension; PROVED).** Put the three classes' charts together, using the median rule (PP26 Prop 1.4): two distinct points are crossed exactly at the region whose log-ratio change is the strict median. So a family of point-like inner models with no forcing pair for any class has all pairwise differences in log-ratio space parallel to (1, 0), (0, 1) or (1, 1). Equivalently, every pair lies on a ray through a vertex. Such a set is contained in one such ray, or it consists of three points forming a triangle with one side in each direction. (Take three non-collinear points. Each further point would lie on one of the three lines through each of them, and the only common points are the three themselves.) So **forcing-free point-like families are one-dimensional**. This is the median-rule half of PP26's (N3). Fat models escape by overlapping, which is exactly Theorem 4.1.

**Example 5.4 (all decompositions matter; CHECKED, `forced_list.out`).** Add to the cell core of §7 either the precise model q″ = (7/20, 11/20, 1/10) alone, or q = (3/10, 1/50, 17/25) together with q′ = (11/50, 77/100, 1/100). Forced decompositions then appear. Each is realised by a core member together with the separated model. The forced pairs are:
- **Prop 4.7's split**, Q = BBSSAB: x is realised by S1 = [m₀, p₁], y by q′ (resp. q″);
- **the ℓ_G route**, Q = BBSSSA: x = (A→S on D^A) ∪ (B→A on ℓ_G), realised by the *precise inner* model {m₀} (and by S1, S2, q); y realised by q′. Here the padding sits on a steep line where T says B. This decomposition is invisible in Prop 4.7, and its x-side needs no silence at all;
- Q = BBBBAA (x realised by S1, y by q′), with leading Ω₁(y) = 0, so the verdict is decided at a later level.

Every allocation inside Ω then violates (TC) at world 1: 57 violating triples with q and q′, and 18 with q″. The violations remain after the owner-minimal reallocation.

**Growth rule (G).** Maintain the selected family 𝒮 and the admitted certificates 𝔇.
- **G1 (overlap is free).** If K_C meets every non-vertex credal set already selected, add C. Its new obligations are its base obligations (competitiveness on supp p), and no certificate conflict can arise (Theorem 4.1).
- **G2 (separated partners).** For each selected C′ with K_C ∩ K_{C′} = ∅, find the classes k whose lines separate them (Cor 2.2) and the straddle bands in Sil(·). Then:
  - **over Ω:** admit C iff, for each such class and band, the pair passes Cor 5.1′ in both orders. For small models this means nested at e_k (Prop 5.2).
  - **over a general base:** use the polarity allocation of Lemma 3.4. The A-holder goes to the majority worlds of k in its realisers' supports, and the B-holder to k. Admit C iff the base accepts the A-holder there and does not accept it at k (condition (E), §6.4).
  - **otherwise:** remove from 𝔇 the certificates in the conflicting band. Their incoherent rivals N·d then need other dominators, which is permitted (AUDIT_answers47, point 4).
- **Invariant.** Separated selected pairs are nested at each class that separates them (more precisely, they pass Cor 5.1′). Overlapping pairs are unconstrained.

---
## 6. Where the mechanism stops: a precise account

**Proposition 6.1 (separated pairs are unavoidable; PROVED).** In any (S)-system with strict (G), two non-vertex selected values have disjoint credal sets.

*Proof.* REFEREE_round46 §2.3 ("nearby result", PROVED there from strict (G) and closed sections) gives: the selection on each closed edge [e_i, e_j] is not vertex-valued. A selected value at an edge index is A a.e. on M_k (PP19 Thm 4(d), first step), so its K lies in the face m_k = 0 (same proof).

Suppose all non-vertex values pairwise intersect. A non-vertex [e₁, e₂]-value must meet some non-vertex [e₂, e₃]-value, and those two faces share only e₂. It must also meet some [e₁, e₃]-value, which forces e₁ ∈ K. So K = [e₁, e₂]. Hence the closed edge [e₁, e₂] carries only the three values V₁, V₂ and E := D_[e₁,e₂].

By LEAD Lemma A, the tie fibres Φ_{V₁}, Φ_{V₂} and Φ_E are closed. They are pairwise disjoint, because V₁ and V₂ have no ties (LEAD Lemma B). They cover the edge, and Φ_{V₁} ∋ e₁ and Φ_{V₂} ∋ e₂ are both nonempty. This contradicts connectedness of the edge. ∎

So any (S)-family has a boundary layer outside every intersecting core. There, Theorem 5.1 and Lemma 3.4 govern conflicts.

**Cross-edge pairs (PROVED).** Let K′ ⊆ [e₁, e₂] and K ⊆ [e₁, e₃] be edge credal sets with K′ ∌ e₁ and K ∌ e₃. Every M₁-line with z₁₂ < min_{K′} m₂ and z₁₃ > max_K m₃ has D_K = B and D_{K′} = A. These lines form a non-null set. So the pair (A-side K, B-side K′) has a type-1A point. Whenever its straddle band meets Sil(T), Cor 5.1′ makes it a forcing pair over an Ω-type base.

**6.2 Ω cannot be the base on the edges, even with certificates (PROVED).** Let C be a non-vertex value at q ∈ (e₁, e₂). By §6.1, C = D_K with K ⊆ [e₁, e₂] and K ≠ {e₁}, {e₂}. Then C ≠ B on non-null subsets E₁ ⊆ M₁ and E₂ ⊆ M₂. (If K ∌ e₁, then C is A on the lines with z₁₂ < min_K m₂; if K ∋ e₁, then C is S on the lines with z₁₂ < max_K m₂. Similarly on M₂.)

Let Y be C moved one step B-ward on E₁ and on E₂, with μ(E₁) = μ(E₂) = m. The leading Ω-values are:
- Ω₁ = −2m + m = −m;
- Ω₂ = m − 2m = −m;
- Ω₃ = 2m.

The record is not an inverted departure, because it never moves toward A. So C ⪯_i Y fails at both i ∈ supp q, and C is not competitive. With the nearby result of R46.1, this contradicts (S). The base at the edge worlds must therefore accept such B-ward trades, which Ω does not. (The additive edge benchmark of AUDIT_selected_realizability §2 does accept them.)

**Lemma 6.2 (localized veto; PROVED).** Assume strict (G) and (S) with closed sections. Let j be a majority world of class k, and Z ⊆ M_k a non-null set. Suppose world j refuses every record whose restriction to some non-null bounded Z′ ⊆ Z is a j-improvement and which is trivial on Z ∖ Z′. This holds, for example, under a "Z-first" lexicographic rule whose leading level is Ω_j restricted to Z. Then there is a contradiction.

*Proof.* Take a bounded non-null Z′ ⊆ Z and X := V_k[Z′ → A]. X is incoherent by Lemma H. KKM gives a selected C with C ⪯_w X at every w.
- At j: on Z′, the record C → X moves C to A, the best value at j. So if C ≠ A on a non-null part of Z′, the record is refused. Hence C = A a.e. on Z′.
- At k: off Z′, X = V_k, which is pointwise k-best; on Z′, X = C. So X is a weak k-improvement of C, strict unless C = X. Strict (G) then forces C = X, which is incoherent. ∎

This is PP26's (V-maj) argument made local. It rules out the obvious way to make majority worlds accept A-holders: giving the zone priority over everything else.

**6.3 Polarity over Ω collapses (CHECKED, `polarity_witness.out`).** Take the cells of §7 with the core plus q″. Move the forced A-holder (x = A→S on D^A, S→A on ℓ_F) from world 1 to worlds 2 and 3, against Ω. World 1 becomes clean (0 violations). But worlds 2 and 3 acquire 153 violations each. One witness at world 2:
- AAAASA ⪯ AASSAA (the moved A-holder, Ω₂ = −1);
- AASSAA ⪯ AABAAA (a base record realised by the core, leading Ω₂ = 0);
- AABAAA ⪯ AAAASA (a base record, Ω₂ = +1);
- the reverse AAAASA ⪯ AABAAA is refused.

This is PP23 Lemma 4.1's tiny-worsening collapse, with selected-realised partners. Over an Ω base, a majority world that accepts every realised Ω-positive record cannot also accept an Ω-negative A-holder.

**6.4 The remaining problem (exact).** By Theorem 3.1 and Props 3.2–3.3, the certificate mechanism decouples completely. What remains is a property of the base and of the boundary layer:

> **(E)** Find record-based base relations B_i = W_i ∪ 𝒞_i, with every non-guidance comparison selected-realised and each B_i satisfying (TC), together with a selection, such that:
> - **(E1)** every selected model is base-competitive on its support, and the base sections are closed (Prop 3.3 then closes the full sections);
> - **(E2)** for every separated selected pair straddling a band in which certificates are wanted, the pair either passes the cone test (nested at the separating class), or the base accepts its A-holders at a majority world of their realisers' supports and refuses them at the owner world.

The section bookkeeping is then exact. KKM dominators of rivals of the form N·d come from the fibre of N; all other rivals must be handled by the base.

What is known about (E):
- the base cannot be Ω near the edges (§6.2), and cannot be region-first (Lemma 6.2);
- over Ω-type bases, polarity collapses (§6.3);
- on the boundary layer, (E2) is a genuine trading condition at the majority worlds. It must hold at bounded exchange rates, because a veto is excluded.

**CONJECTURE 6.5.** There is a base satisfying (E) in which:
- the boundary layer is a two-world additive edge system (AUDIT_selected_realizability §2) near each edge;
- the interior is an intersecting core of coarse models around T;
- the two are joined so that every separated pair straddling a certificate band is a cross-edge pair, and is handled by polarity at the far edge world.

Evidence: Lemma 3.4 makes the supports cooperative, and the additive edge benchmark accepts the B-ward trades of §6.2. Unproved: (TC) of the joined base, and closed sections across the join.

---

## 7. Cells (CHECKED; `cells28.out`)

**Cell set.** The cells have:
- class-1 lines ℓ_B, ℓ_A (both T-silent, ℓ_B ≤ ℓ_A), each split **radially** into two pieces of masses (2, 2) and (1, 1), so β = 4 > α = 2;
- the **steep silent padding** line ℓ_F, mass 3 ∈ (α, β);
- the steep line ℓ_G where T says B, mass 3/2.

That gives 6 pieces and all 729 regular models.

The relation is guidance, plus Ω-lex (total, then piece by piece) restricted to records realised by the family, plus all inverted departures (26 out of the all-silent model) at every world. (TC) is checked on every triple by boolean matrix products, using the exact characterisation P ⪯ Q ⪯ R with R ⪯ P accepted and P ⪯ R refused. Omitted: X values, U problems (a sub-domain), and (S).

| Family (all contain m₀ unless marked) | (TC) violations | pure improvements accepted | selected competitive vs all 729 | dominators of selected | doubly realised decompositions of d⁻¹ |
|---|---|---|---|---|---|
| core (T, {m₀}, five segments/triangles at m₀) + vertices | **0** | 0 | yes | 0 | **0** |
| core + q, q′ (separated, crossed at e₁) | 3,275 (57 with 𝓘 = copies of d) | 0 | yes | 0 | 20 (3 forced) |
| core + q″ | 1,095 (18 with 𝓘 = copies of d) | 0 | yes | 0 | 12 (1 forced) |

Further findings:
- With the core alone:
  - T ⪯_i T·d at all worlds, and T·d ⪯_i T at none;
  - Prop 4.7's x is realised (by S1) and accepted only at world 1; its y is realised by nothing and accepted nowhere.
- The large counts with separated pairs come from the other admitted certificates, including A-heavy ones whose deficits sit at worlds 2 and 3.
- Allocations:
  - **canonical** (every Ω-acceptable world) and **owner-minimal** give identical counts;
  - **polarity** clears world 1 for q″ but creates violations at worlds 2 and 3 (§6.3).
- Separation lemma: 0 intersecting realiser pairs in 16,150 (`separation_check.out`).

---

## 8. Answers to the brief

| Brief item | Answer |
|---|---|
| 1. Adversary configuration with selected models, obligations and worlds | §4.2: the explicit index domain and values (T on M, D_[m₀,p] elsewhere, vertices), the obligatory records, and the accepting worlds. The B-heavy repaired configuration (P1–P3) is dominated by T at all worlds. **Every** decomposition is blocked, by the separation lemma (Cor 2.2), not only Prop 4.7's split. The omitted padding records are not forced back by (IB), (TC), protection, ties or sections (§4.2). PROVED. |
| 2. Growth rule and invariant | Rule G (§5). The invariant: **overlapping selected models are free; separated selected pairs must be nested at their separating class** (Cor 5.1′, Prop 5.2). This is the "two-set pattern" condition: each piece needs one model, and a doubly realised decomposition needs two disjoint ones. For point-like families it forces one-dimensionality (Cor 5.3). |
| 3. Sections | Verified: the support half of (S) on I; section-neutrality of certificates (Prop 3.3); with closed base sections and no all-world ties, closed full sections. Not verified: closedness of Ω-lex base sections. |
| Does Prop 4.7 survive selection? | Not for intersecting families. For families with a separated pair crossed at e₁, it does over Ω, and through more decompositions than Prop 4.7 uses (Example 5.4, the ℓ_G route). |
| Does the mechanism fail at the stated scope? | The certificate layer itself never fails; it decouples (Thm 3.1, Props 3.2–3.3). The failure is in the base: (S) forces separated pairs (Prop 6.1); Ω cannot run the edges (§6.2); polarity collapses over Ω (§6.3); region-first fixes are vetoes (Lemma 6.2). The open requirement is (E). |

**Most important next step.** Attack (E) on one edge neighbourhood. Join the additive two-world edge system on [e₁, e₂] to an intersecting core around T. Prove (TC) for the joined base, with the cross-edge A-holders accepted at the far edge world by additive trading. Then test closed sections across the join, using Prop 3.3 to ignore the certificate layer.

