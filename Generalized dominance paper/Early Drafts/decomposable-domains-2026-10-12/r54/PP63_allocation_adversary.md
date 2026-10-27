# PP63. Adversary for round 54: refusal surgery, shifted records, a Radon obstruction for additive kernels, and attacks on PP62

23 October 2026. Adversary task of Brief 54. One author; not refereed. Takes in the coordinator's relay of REFEREE_round53 (§3.3 SR(c) coupling; §7 ledger bottom line) the final PP62 (§6), and PP61 §1 and Theorem C (read for §4.4–4.6).

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: exact rational computation in `r9/PP63_py/`; every script ends ALL PASS.
- NUMERICS: none is used for any claim (`harness63.py` is an unused test library).
- CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF54 and its binding audits (AUDIT_round54, _test, _answers, AUDIT_robust_refusals); PP56 §4–5; PP57 §4–5; PP59; PP30 §1–3; PP36 §0–3; REFEREE_round53 §3.3, §7; PP61 (§1, Theorem C) and PP61_py (read only); PP62 (final). No axiom is added. Extra hypotheses are named where they enter.

---

## 0. Verdict

1. **No axiom-level obstruction found (§4; OPEN). Its possible location is narrowed.**
   - The referee's coupling, in exact form (Lemma 4.1): every refusal at a member spreads to a neighbourhood for the same rival, and two refused worlds force a *definite* acceptance on a neighbourhood.
   - Its obvious three-world use does not close (Remark 4.3).
   - Finite instances with **hierarchical scales** are sound carriers of section clauses (Prop 4.4). With PP61's Theorem C, which I re-checked, one-level instances, PP61's included, are **always satisfiable** (Cor 4.5). A certificate needs at least two levels, so that a rival can depend on the relation.
   - PP62's Cor E.2 cascade at u is consistent for every rival fixed in advance (Prop 4.6, witness Λ_q, with the local shape given). It bites only on swaps balanced for the relation's own weighting, which are chosen after the relation.
2. **Single-world incomparability is never blocked by (TC), undominatedness, (C) or sections (Lemma 3.1, Cor 3.2; PROVED).** Refusing a record *and its inverse* at one world, on a metric neighbourhood, preserves reflexivity, strict (G) (away from guidance), (IB), (TC), undominatedness, direct (C) and closed sections. Only **defence slack** can block it. This settles the brief's question in every coupled configuration.
3. **The suggested shifted-record identification is false (§2; PROVED; CHECKED 36/36).**
   rec(C_{a_t} → C_a[F ↦ C_b]) = rec(C_b[F ∪ σ_t ↦ C_{a_t}] → C_b) holds **iff σ_t ∩ D_ab is null**, and for the kink triple and every pure shift (±e_w, all six ordered pairs) it is **not** null. The C_b-copy carries the record of the **t-dependent** rival C_a[F ↦ C_b][σ_t ∩ D_ab ↦ C_b], so it never enters a fixed-rival section. The fixed-rival shifted record has no C_b realiser; generically its inverse is an orphan.
4. **Theorem J (PROVED; certificate CHECKED): additive kernels with an incomparability margin cannot defend a genuinely 2-D posterior family.** If a relation refuses C_a ⪯_i X whenever ∫ j_i(g, C_a(g), X(g)) dμ < 0 for a kernel with strictly negative (h, S) two-cycles, then some member of N is undefended. The certificate is four indices (a kite, inside any neighbourhood of u) and seven problem cones; the proof is **Radon's theorem** applied to the members' Bayes weights. One-parameter families escape. This kills tolerance-band, margin and loss-averse allocation rules, and lexicographic rules with such a first level, which are the natural additive ways to make inverse records incomparable. Together with Theorem Q it closes the additive-kernel family on N except an exactly-potential residual (Prop 5.3).
5. **Attacks on PP62 (§6).**
   - Its rule R₀ (u¹-sign verdicts; null records refused at w₀ = 2) passes every non-section clause (independently CHECKED).
   - Theorems R, P and E (at u, by a symmetry argument I confirm) are sound. The corollary to its Lemma S has a gap; I repair it.
   - **Its module (Thm M) does not reach the target.** The family N_u ∪ N_B is not a neighbourhood of u (u is a sector apex; PROVED). On that very family, the interior member a₁ = u∘(1 − s e₂) has a balanced swap with B whose section fails at a₁ (exact witness, `lobe63.out`). The balanced rivals that Thm M handles come from the single apex pair (u, B).
6. **Ledger (§7):** Lemma 3.1 and Prop 4.4 are axiom-level TOOLs; Theorem J is architecture-level (Ad), a new LOCAL constraint, consistent with REFEREE_round53 §7. PP30 Thm 3.1 and Prop K apply to the brief's swap rivals only in the forms stated in §7.

| Item | Result | Label |
|---|---|---|
| Records as pairs (P, Q); metric d; section maps continuous | Lemma 1.1 | PROVED |
| Shifted-record formulas and the criterion σ_t ∩ D_ab = ∅ | Prop 2.1 | PROVED |
| Criterion fails for all 36 (pair, ±shift) cases of the kink triple | Prop 2.2 | CHECKED (`shift63.out`) |
| Refusal surgery on inverse-closed d-open sets | Lemma 3.1 | PROVED; CHECKED on exact instances (`surgery63.out`, `surgery63_ties.out`) |
| Single-world incomparability blocked only by defence slack | Cor 3.2 | PROVED |
| Refusals spread; definite acceptances near two-world refusals | Lemma 4.1 | PROVED |
| One-rival germ system satisfiable (all rays) | Prop 4.2 | PROVED |
| Hierarchical-scale instances are sound for sections | Prop 4.4 | PROVED |
| One-level instances (incl. PP61's) are always SAT; certificates need two levels | Cor 4.5 | PROVED (with PP61 Thm C) |
| PP62 Cor E.2 cascade at u, fixed rivals: consistent; local shape | Prop 4.6 | PROVED |
| Axiom-level coupled obstruction | — | OPEN |
| Additive kernels with negative two-cycles fail defence on 2-D N | Thm 5.1 | PROVED; kite CHECKED (`kite63.out`) |
| Weak two-cycles: escape forces exact potential cones and collinear Bayes weights | Prop 5.3 | PROVED |
| Rules that read records only through a vector measure with a null member swap fail (C) | Prop 5.4 | PROVED |
| PP62's R₀: non-section clauses | §6.1 | PROVED; CHECKED (`r0_63.out`) |
| R₀ fails sections at every interior member with a null rival | Prop 6.1 | PROVED |
| PP62 Thm E confirmed; Lemma S corollary repaired | §6.3 | PROVED |
| PP62 Thm M: u ∈ ∂N; failing balanced swap out of an interior lobe member | §6.4 | PROVED; CHECKED (`lobe63.out`) |

---

## 1. Language

Setting of BRIEF54; (2V) on N. On the disagreement region R every member says h(g) or S. Coherent members satisfy **C_a(g) = T(a∘g)** (posterior sign = sign of m·(a∘g)), so the answer set A_a := {g ∈ R : C_a answers} is cut out by the three linear forms f_v(a; g) = c Σ a_i g_i + ε a_v g_v > 0 (v = 1, 2, 3). For fixed g, **Ans(g) := {a : g ∈ A_a} is an intersection of three half-planes in index space**; its corners are where two forms vanish (the "kink" corners).

A **two-valued record** is a pair (P, Q) of disjoint subsets of R: P is silenced (h → S), Q is answered (S → h). Its inverse is (Q, P). For models agreeing off R, rec(X, Y) = (A_X ∖ A_Y, A_Y ∖ A_X).

Records with general values are partial maps g ↦ (old, new). Put d(ρ₁, ρ₂) := μ{g : ρ₁(g) ≠ ρ₂(g)} (with "undefined" a value).

**Lemma 1.1 (PROVED).** (a) Inversion is a d-isometry. (b) For each fixed rival X, a ↦ rec(C_a, X) is continuous into (records, d). Hence every d-open set of records is **section-open**: its preimage under every section map is open in N.

*Proof.* (a) is clear. (b) rec(C_a, X)(g) = rec(C_b, X)(g) wherever C_a(g) = C_b(g), so d ≤ μ(C_a ≠ C_b) → 0 (continuity in measure, PP49 Lemma 1.1). ∎

---

## 2. Shifted records, exactly (brief: "prove any such identification exactly")

Let a, b ∈ N, F ⊆ D_ab, X := C_a[F ↦ C_b], and a pure shift a_t := a∘(1 ± t e_w). Put σ := {C_{a_t} ≠ C_a}, σ⁺ := A_{a_t} ∖ A_a, σ⁻ := A_a ∖ A_{a_t}, F⁺ := F ∩ A_a, F⁻ := F ∖ A_a. Assume F ∩ σ = ∅ (true for small t when F has positive angular distance from ∂A_a).

**Proposition 2.1 (PROVED).**
- (i) rec(C_{a_t} → X) = (F⁺ ∪ σ⁺, F⁻ ∪ σ⁻).
- (ii) rec(C_b[F ∪ σ ↦ C_{a_t}] → C_b) = (F⁺ ∪ (σ⁺ ∖ A_b), F⁻ ∪ (σ⁻ ∩ A_b)).
- (iii) They coincide iff σ ∩ D_ab is null. In general (ii) is rec(C_{a_t} → X_t″) with **X_t″ := X[σ ∩ D_ab ↦ C_b]**, a rival that depends on t.

*Proof.* (i) On F, C_{a_t} = C_a; off F, X = C_a. (ii) On σ⁺ ∩ A_b and on σ⁻ ∖ A_b, C_{a_t} = C_b, so those points drop out. (iii) Compare (i) and (ii); for the last claim, X_t″ agrees with C_{a_t} exactly off F ∪ (σ ∖ D_ab). ∎

**Proposition 2.2 (CHECKED, `shift63.py`).** For the kink triple, every ordered pair (a, b) ∈ {A, B, D}², every w and both signs of the shift (t = ±1/1000), σ ∩ D_ab contains open cells (2 to 16 of them). So (iii) fails in all 36 cases. Formulas (i), (ii) hold exactly on every cell, and the shift record s_t = rec(C_{a_t} → C_a) is guidance at w (G+ for +e_w, G− for −e_w) and mixed at the other two worlds.

*Reason.* σ is a layer along **all** of ∂A_a ∩ {g_w ≠ 0}; D_ab is adjacent to ∂A_a on the σ-side somewhere, because b's boundary crosses a's.

**Consequences for germ literals (PROVED).**
1. The protection clause "C_b[F ∪ σ_t ↦ C_{a_t}] is incoherent, so some world refuses" constrains R(rec(C_{a_t} → X_t″)), **not** R(rec(C_{a_t} → X)). Since X_t″ varies with t, it never enters a fixed-rival section sequence.
2. A new-side realiser of rec(C_{a_t} → X) is a member equal to C_b on F and to C_a on σ. C_b is never one here. A realiser exists only in special position (e.g. F inside the layer of the opposite pure shift a∘(1 ∓ s e_w), whose difference set is disjoint from σ).
3. The inverse rec(X → C_{a_t}) needs a member equal to X on F ∪ σ for any defence obligation. Generically there is none: **the inverse of a shifted record is an orphan.** It carries only C_{a_t}'s protection clause (some world refuses it).

So the only automatic obligations on a fixed-rival shifted record are C_{a_t}'s defence and protection, (G), and (TC) with its triangle partners. This is what makes Prop 4.2 below possible.

---

## 3. Refusal surgery

**Lemma 3.1 (refusal surgery; PROVED).** Let ⪯ satisfy reflexivity, strict (G), (IB), (TC), undominatedness and direct (C) for the members. Fix a world i and a set 𝒰 of non-empty records with
- (U1) 𝒰⁻¹ = 𝒰;
- (U2) no ρ ∈ 𝒰 is weakly i-favourable for its old side (old side pointwise no worse at i).

Let ⪯′ refuse every ρ ∈ 𝒰 at i and agree with ⪯ otherwise. Then:
- (a) ⪯′ satisfies reflexivity, strict (G), (IB), (TC), undominatedness and direct (C);
- (b) ⪯′ satisfies defence iff every ρ ∈ 𝒰 with an old-side member realiser is accepted by ⪯ at some world other than i;
- (c) if ⪯ has closed fixed-rival sections and 𝒰 is section-open (for instance d-open, Lemma 1.1), then so does ⪯′.

*Proof.*
- (IB): verdicts still depend only on records. Reflexivity: the empty record is not in 𝒰. Strict (G): by (U2) no guidance acceptance at i is removed; refusals are only added.
- (TC): take a triangle accepted under ⪯′ at a world k. If k ≠ i nothing changed. If k = i, its links are accepted under ⪯ and lie outside 𝒰. By (TC) for ⪯ the reverses are accepted under ⪯. The reverse of a link ℓ is ℓ⁻¹, and ℓ ∉ 𝒰 implies ℓ⁻¹ ∉ 𝒰 by (U1). So the reverses are still accepted under ⪯′.
- Undominatedness: if X ⪯′_k C_a at every k, the same holds under ⪯, so C_a ⪯_k X at every k. At k = i, rec(X, C_a) ∉ 𝒰, so rec(C_a, X) ∉ 𝒰 by (U1), and the acceptance survives. Direct (C) only asks for refusals, or for an all-world tie, which survives by the same argument.
- (b) is immediate. (c): the new refusal set for a rival X at world i is the old one united with {a : rec(C_a, X) ∈ 𝒰}, and both are open. ∎

**Corollary 3.2 (single-world incomparability; PROVED).** Let r be a record that is *robustly mixed at i*: both {old strictly i-better} and {old strictly i-worse} have μ-mass > δ₀. For δ < δ₀ put 𝒰_δ := B_δ(r) ∪ B_δ(r⁻¹) (d-balls). Then refusing 𝒰_δ at i, starting from any admissible relation (all axioms, including closed sections), gives an admissible relation **iff** every realised record in 𝒰_δ keeps an accepting world other than i. In that case r and r⁻¹ are robustly incomparable at i.

*Proof.* (U1) holds by Lemma 1.1(a). (U2) holds because a record within δ of r (or of r⁻¹) keeps points of both kinds. Then apply Lemma 3.1. ∎

**Answer to the brief's question.** Refusing both r and r⁻¹ at one world is **never** blocked by (TC), undominatedness, direct (C) or closed sections, in any coupled configuration. It is blocked only by guidance or by a lack of defence slack on a neighbourhood. In particular the audit's q-infeasible pattern (mutual inverses refused at one world) is a genuine "weights fail, relations survive" pattern **at the axiom level**, wherever defence has slack. §5 shows that it cannot be produced by any **additive** kernel on a 2-D family.

---

## 4. The axiom-level attempt

### 4.1 The engine (formalising REFEREE_round53 §3.3)

Without sections there is no certificate (PP56 Cor 4.3). By Lemma 3.1, refusals are free modulo defence, so every contradiction must be driven by **forced acceptances**. There are exactly four sources of them: guidance; (TC) reverse completion; defence with the other worlds refused; and section limits.

**Lemma 4.1 (spreading; PROVED, axiom-level).** Fix a rival X and a member a.
- (a) If C_a ⋠_k X, for any reason (strict (G), a (TC) kill such as PP30 Thm 3.1(b) or Prop K, or a case split), then C_{a′} ⋠_k X for all a′ in a neighbourhood W(X, k) of a.
- (b) If C_a ⋠_k X and C_a ⋠_l X (k ≠ l), then C_{a′} ⪯_m X for all a′ ∈ W(X, k) ∩ W(X, l), where m is the third world. These are **definite acceptances of non-guidance records**.
- (c) Germ form: for every ray v at a, the set Γ_v of worlds accepting rec(C_{a+tv} → X) for arbitrarily small t satisfies ∅ ≠ Γ_v ⊆ Acc(rec(C_a → X)).

*Proof.* (a) is openness of the refusal set. (b) is (a) plus defence at a′. (c): defence at a + tv, pigeonhole, then (a). ∎

The referee's cofinite restriction is (b) with k = 1 and X a strict pure 1-improvement. In fact the restriction holds on a whole neighbourhood, not only along a sequence. The typical case of (b) is X = C_a[E ↦ S], with E inside the cells where C_a answers h that is correct only at m: X is strictly better at k and l, and near a, C_{a′} ⪯_m X is forced although the record s ⊕ e is mixed at m.

### 4.2 What one rival cannot do

**Proposition 4.2 (one-rival germ system is free; PROVED).** Let X = C_a[F ↦ C_b] with F ⊆ D_ab non-conic, mixed at every world, at positive angular distance from ∂A_a. Write r := rec(C_a → X) and ρ_{t,v} := rec(C_{a+tv} → X). The following clauses hold together, for all rays v and all small t:
- defence and protection of C_a, C_b and every C_{a+tv} against X and its copies;
- strict (G);
- (TC) on the triangles (C_{a+tv}, C_a, X) and (C_{a+tv}, X, C_a);
- the germ clauses of Lemma 4.1(c).

The satisfying assignment is:
- R(r) = [3] ∖ {j} and R(r⁻¹) = {j};
- R(ρ_{t,v}) = [3] ∖ {j} for every v and t (germ-constant);
- R(ρ_{t,v}⁻¹) = [3] (an orphan, §2 item 3);
- the shift records s_t carry any admissible member–member verdicts (guidance at w).

*Proof.*
- Defence and protection: each relevant record has one accepting and at least one refusing world. ρ⁻¹ is refused everywhere, which is protection for C_{a_t}. For C_a, r⁻¹ is refused at j and accepted at the other two worlds. For C_b, r is refused at two worlds (protection) and r⁻¹ is accepted at two (defence).
- (TC) on (C_{a_t}, C_a, X): its links are s_t, r and ρ⁻¹, and ρ⁻¹ is never accepted.
- (TC) on (C_{a_t}, X, C_a): its links are ρ, r⁻¹ and s_t⁻¹. ρ is accepted only at j, where r⁻¹ is refused.
- Germ clauses: Γ_v = {j} = Acc(r). ∎

This is the axiom-level counterpart of the robust refusal lemma. It extends that lemma to all rays and to every triangle that involves the shift.

### 4.3 Why the three-world coupling does not close

To break protection one needs some ρ = rec(Q → C_c), with Q incoherent and c a member, accepted at **all three** worlds. The only definite forced acceptances available are those of Lemma 4.1(b). Suppose all three come from (b), with members b_k, nearby members a′_k ∈ W(X_k), and two-world improvements X_k = C_{b_k}[E_k ↦ ·], k = 1, 2, 3. Then (IB) forces ρ = E_k ⊔ s_k with s_k = D(C_{a′_k}, C_{b_k}), so **E_k ⊆ s_l for l ≠ k**.

**Remark 4.3 (PROVED as an implication; not a theorem about all relations).** This needs each improvement set E_k to fit inside the shift layers s_l of the other two worlds. Each layer is thin, of width at most the radius of W(X_l). That radius is chosen by the relation and may depend on X_l, hence on E_l. The requirement is cyclic (E₁ ⊆ s₂ needs a′₂ chosen after E₁, and E₂ ⊆ s₁ needs the reverse). It can be met only if the radii are bounded below in terms of the masses, and the axioms give no such bound (BRIEF54: "its size may depend on the rival").

In every continuous additive relation the radius is proportional to the mass of E_k, and protection is never violated. So any obstruction must use (TC) chains between germ records in different directions, not three parallel spreadings.

### 4.4 Finite carriers of section clauses

**Proposition 4.4 (hierarchical scales are sound; PROVED).** Suppose the rivals of an instance are organised in levels L₀, L₁, …, L_n. Level-k rivals may use layers of shifts at scales t₁, …, t_k, with t₁ ≫ t₂ ≫ ⋯. Each scale t_{k+1} is chosen after the finitely many rivals of levels ≤ k, so that every shifted member at scale t_{k+1} lies in W(X, i) for every such X and every refused i. Then every clause

  [C_{a_t} ⪯_i X] ⇒ [C_a ⪯_i X]  (X of level ≤ k, t = t_{k+1})

holds in every admissible relation. If the combinatorial type (chirotope) is stable on (0, t*], an UNSAT instance of this kind is an axiom-level obstruction.

*Proof.* Quantifier order: the relation is given first, then the scales are chosen, finitely many at a time. The clause is the contrapositive of Lemma 4.1(a). Chirotope stability makes the instance's records independent of the chosen t. ∎

**Hygiene note on PP61 (CHECKED by reading `inst61.py`).** The solver's SEC clauses are exactly of this form with one level. They are applied only to fixed base rivals, never to rivals containing σ-atoms. They are therefore **sound**. Both justifications work: the one above ("choose t* after the base rivals") and PP61's (a constant verdict vector along an actual sequence t_k → 0, by stability and pigeonhole). A clause with a σ-containing rival at the same scale would **not** be sound.

**Corollary 4.5 (one level is never enough; PROVED, using PP61 Theorem C).** Every instance of Prop 4.4 with **one** level and stable combinatorics is satisfiable. This includes PP61's instances, whose SEC clauses use only fixed base rivals.

*Proof.*
- The base rivals and base points are countably many. PP61 Theorem C, which I re-checked (a Baire argument on q ↦ ∫ q d, valid as written), gives a Λ_q with all non-section axioms whose verdicts are locally constant at every (base point, base rival) pair.
- Choose t below the resulting radii and inside the stability interval. Every clause of the instance, the SEC clauses included, then holds for Λ_q at that t.
- By stability, the instance is the same for every t in the interval. ∎

So an axiom-level certificate needs **at least two levels**: level-1 rivals built from shift layers whose scale t₁ is chosen after the relation. Only then can a rival depend on the relation, which Theorem C (Cor 4) shows is necessary. Prop 4.4 is the sound carrier for such two-level certificates, and Cor 4.5 says that nothing less can work.

### 4.6 The Cor E.2 cascade at u, without endorsement (coordinator item 3): consistent

PP62 Cor E.2 concerns one fixed balanced rival X = C_u[F ↦ C_B] (u¹-null) and the records forced around u along the six pure shifts: the u¹-unfavourable germ acceptances, their Lemma S splits, the ties, and the reverses demanded by (TC).

**Proposition 4.6 (PROVED).** For any countable set of such fixed rivals and splits (fixed in advance), all the clauses of the cascade hold simultaneously in an admissible relation: closed sections at u and at every listed germ point, (TC), (G), defence, direct (C), undominatedness, and the splits.

*Proof.* Apply PP61 Theorem C to the countable set of (point, rival) pairs. The resulting Λ_q satisfies every non-section axiom everywhere and has locally constant verdicts at each pair. The rest of this proof records what its verdicts look like.
- X is u¹-null but, for generic q, not q-null. Since λ·d = 0 pointwise on h/S records, Σ_i V^q_i(rec(C_u → X)) = 0 with V^q ≠ 0.
- So R(rec(C_u → X)) = {i : V^q_i < 0} has one or two worlds, and the reverse is refused on the complement.
- Along every pure shift, V^q(rec(C_{u_t} → X)) = V^q(rec(C_u → X)) + O(t) keeps its sign pattern. So the germ acceptances at v ∉ R are exactly PP62's u¹-unfavourable literals E.2(i): q-favourable, u¹-unfavourable. ∎

**Local shape.** Near u, the cascade is the q-sign pattern of the fixed rival, frozen on a neighbourhood:
- refusals at the q-negative worlds, the reverse refused at the q-positive worlds;
- ties only where V^q_v = 0;
- E.2(ii) is resolved inside the q-additive structure (the repaired Lemma S refuses one favourable split link, and the refused link is q-unfavourable).

**What this shows.** Cor E.2 cannot close into a contradiction about any rival fixed in advance. The contradiction PP62's cascade is looking for appears only when the balanced rival is chosen **after** the relation: for each q there is a q-balanced swap F_q (equal q|g|-mass on Ep and Em), and Theorem Q kills Λ_q on F_q. In the language of Prop 4.4, F_q is a level-1 rival. That is the precise location of the open problem: a rule must handle the **uncountable** family {C_a[F ↦ C_b] : a, b ∈ N, F balanced for some weighting}, which no single weighting does.

### 4.7 Configurations shown free, and why

| Configuration | Free? | Reason |
|---|---|---|
| Inverse records refused at the same world (incomparability), any coupling | yes, iff defence slack | Lemma 3.1, Cor 3.2 |
| One swap rival, all rays, its shift triangles, protection of both ends | yes | Prop 4.2 |
| Mixed triangle (C_a, C_a[F ↦ b], C_a[G ↦ d]): links = defence variables of a, b, d (PP56 (D2)) | yes, whenever one link has slack at that world | refusing that link with its inverse (Lemma 3.1) breaks the triangle; (TC) needs all three links |
| Fixed-rival limits along non-pure paths and toward ∂N | no new clause | Lemma 4.1(c) holds for every ray; at ∂N sections are relative to N, and Lemma 1.1 is unchanged |
| (IB) copies of shifted records with incoherent sides | carry no fixed-rival obligation | Prop 2.1(iii), §2 items 1–3 |
| Three parallel spreadings giving an all-world acceptance | not forced | Remark 4.3 |
| PP62's Cor E.2 cascade at u (germ acceptances, Lemma S splits, ties, (TC) reverses), any countable family of fixed rivals | yes | Prop 4.6 (Λ_q, generic q) |
| Any one-level hierarchical instance (PP61's included) | yes | Cor 4.5 |

**What remains OPEN.** An obstruction must live on **defence-tight** records: records whose other two worlds are refused for structural reasons (strict (G) or (TC) kills), spread by Lemma 4.1. It must chain those through (TC) across germ records in different directions. Prop 4.4 is the sound way to search for one.

---

## 5. Theorem J: a Radon obstruction for additive kernels

**Setting.** For each world i let j_i(g, x, y) be measurable on R × {h, S}², with j_i(g, x, x) = 0 and |j_i| ≤ K|g|. Write J_i(Y, Z) := ∫_R j_i(g, Y(g), Z(g)) dμ, and α(g) := j(g, h, S), β(g) := j(g, S, h) (vectors in ℝ³).

**(H_J)** For every member C_a and every rival X that agrees with C_a off R and is two-valued on R: if J_i(C_a, X) < 0, then C_a ⋠_i X.

**(N2C) negative two-cycles:** α_i(g) + β_i(g) < 0 for every i and a.e. g ∈ R.

Examples are margin or tolerance-band rules (refuse unless the increment exceeds κ times its absolute size), loss-averse kernels, any kernel relation with strictly cyclically subadditive j (these satisfy (TC) vacuously and have closed sections automatically), and every lexicographic rule whose first level is such a J.

**Theorem 5.1 (PROVED).** Under (H_J) and (N2C), some member of every genuinely two-dimensional N (with (2V)) is undefended against some two-valued rival.

*Proof.*
1. **A Bayes vector for each member.** Fix a and put φ_a(g) := j(g, C_a(g), flip C_a(g)). The vectors J(C_a, X) form the range V_a of the vector measure E ↦ ∫_E φ_a dμ, so V_a is convex by Lyapunov.
   - Defence and (H_J) give V_a ∩ O₋ = ∅, where O₋ is the open negative orthant.
   - Separation gives λ(a) ∈ Δ with λ(a)·v ≥ 0 on V_a, hence λ(a)·φ_a ≥ 0 a.e.
   - So, for a.e. g: if g ∈ A_a then λ(a)·α(g) ≥ 0; if g ∉ A_a then λ(a)·β(g) ≥ 0.
2. **Strict separation at each problem.** For λ ∈ Δ, (N2C) gives λ·α + λ·β < 0, so the closed half-planes {λ·α(g) ≥ 0} and {λ·β(g) ≥ 0} are disjoint on Δ. Hence, for any finite P ⊂ N and a.e. g,
     conv λ(P ∩ Ans(g)) ∩ conv λ(P ∖ Ans(g)) = ∅.
3. **Radon.** Choose P = {p₁, …, p₄} ⊂ N so that every one of the 7 bipartitions of P equals {P ∩ Ans(g), P ∖ Ans(g)} for g in an open cone of R. By Radon's theorem in the plane Δ, some bipartition of λ(P) has intersecting convex hulls. This holds also with coincident or collinear points. That contradicts step 2 at a g from the corresponding cone, chosen outside the finitely many null sets. ∎

**The kite (CHECKED, `kite63.py`).** p₁, p₃ = u + s(τ, τ + 1)·(−1, −1, 2) and p₂, p₄ = u + s((τ + ½)(−1, −1, 2) ± 6(1, −1, 0)), with τ = 1/10, at s = 10⁻³ and s = 10⁻⁶. At s = 10⁻⁶ the kite lies inside PP61's N = conv{B, D, B′, D′}.
- The diagonal bipartition {p₁, p₃} | {p₂, p₄} comes from the **corner problem g = (−7, −7, 23)**, apex u. Its two active forms vanish at u, and its answer region is a wedge of opening about 154.5° along (−1, −1, 2).
- The other six bipartitions come from single-active-form problems.
- Every inequality is strict, so each bipartition holds on an open cone. (2V) is checked at each point, and on every certificate problem the answering members share one sign.

**Why two dimensions are needed (PROVED).** On a segment, Ans(g) ∩ segment is an interval, so the "alternating" bipartition {q₁, q₃} | {q₂, q₄} of four collinear points never occurs. The images can be placed on a convex arc, where every interval is separable. This is the kernel-level shadow of PP57's one-parameter milestone (c).

**Corollary 5.2 (PROVED).** No allocation that refuses every record with J_i < 0, for a kernel satisfying (N2C), defends a 2-D posterior neighbourhood. With the balanced field u¹ even T alone is undefended under a tolerance band. On Ep ∪ Em, λ·ν ≥ κλ·|ν| and λ·(−ν) ≥ κλ·|ν| cannot both hold. Theorem 5.1 says that no choice of kernel repairs this once the family is 2-D.

So **"weights fail, relations survive" cannot be realised by an additive kernel with incomparability margins.** The incomparability that Cor 3.2 allows must be **non-additive in the record**.

**Proposition 5.3 (weak two-cycles; PROVED).** Replace (N2C) by: α + β ≤ 0 at every world, j_i(g, x, y) > 0 whenever x is strictly i-better than y, and (H_J) for two-valued rivals on all mixed problems.
- (a) If α(g) + β(g) ≠ 0 a.e. on R, Theorem 5.1 still holds.
  - Each λ(a) is interior: members answer non-null sets with Cor = {k}, where λ_k = 0 would give λ·φ_a < 0.
  - Then H_α ∩ H_β ∩ int Δ = ∅, and the same Radon argument applies.
- (b) In general, defence of the kite forces a bipartition cone W on which α + β = 0 a.e. (an **exact potential**, so no incomparability at any world there). On W, at least two kite members, and three if their weights are distinct, satisfy λ(a)·α(g) = 0: they are exactly h/S-indifferent. Their weights lie on one line ℓ, and α(g) ⊥ ℓ a.e. on W.

*Proof of (b).* Weak separation of a Radon partition by a line forces each crossing hull (a segment, or an inner point) onto the line. ∎

**OPEN residual.** Whether (b) plus closed sections, which are automatic for "J ≥ 0" rules, always yields Theorem Q's null non-conic member swap. On W all record values are parallel to one vector, so a null swap needs cancellation across cones. This is exactly PP57 Cor 4.4's OPEN degenerate case.

**Proposition 5.4 (rules that read a record only through a vector measure; PROVED).** Let m(r) := ∫_{D(r)} κ(g, old(g), new(g)) dμ ∈ ℝᵏ for an integrable κ, and suppose every verdict on a two-valued record is a function of m(r) alone.
- (a) Reflexivity puts m = 0 in every world's acceptance set.
- (b) Hence, if some non-conic F ⊆ D_ab between members has m(F : a → b) = 0, the incoherent C_b[F ↦ C_a] is accepted as at least as good as C_b at all three worlds. Direct (C) fails. No sections and no (TC) are used.
- (c) For the balanced level-0 vector V = u¹-increment (k = 3), the kink's balanced swap has V = 0. So **every rule that decides records by V(r) alone fails**, however the regions K_i ⊆ Π are drawn. This is Theorem Q's lesson with sections removed.
- (d) A valuation that separates the empty record from every non-empty one is needed. An example is the 12 per-class masses: silenced or answered, by the odd world, and by whether that world is the only right or the only wrong one. If such a rule is of the form "J_i(m(r)) ≥ 0" with J_i linear and (N2C), Theorem 5.1 applies.

---

## 6. Attacks on PP62

PP62 (final text read 18:49). Its rule: for an ordered record r, let V(r) := Φ(new) − Φ(old) ∈ ℝ³ be the u¹-value (PP56 level 0, all four advice values). Then
- R₀(∅) = ∅;
- R₀(r) = {w : V_w(r) < 0} if V(r) ≠ 0;
- R₀(r) = {w₀} (w₀ = 2) if r ≠ ∅ and V(r) = 0 (a "null record").

PP62 claims:
- Thm R: every non-section clause, on all records;
- Thm P: openness except on null fibres at non-minimisers of Φ₂;
- Thm M: a two-lobe module N = N_u ∪ N_B on which every clause holds, including openness, for balanced swaps between u and B, with an α-certificate;
- Thm E: u¹-endorsed allocations cannot have closed sections at an interior member that has a balanced member swap.

**6.1 Thm R: confirmed (PROVED; CHECKED independently, `r0_63.out`).**
- *Independent check.* I re-checked on PP56's exact instances with equal Ep/Em masses (18 to 196 null ordered pairs), w₀ = 1, 2, 3, values {h, S} and all four values: strict (G), (TC) on every ordered triple, defence and protection all hold.
- *Attacks that fail.* All of the brief's non-section attacks fail against R₀:
  - mixed triangles (one link per swap, the third a member link): every accepted cycle has all V_w = 0, and the reverse of a link with V ≠ 0, V_w = 0 is accepted;
  - inverse records: null records are incomparable at w₀ and tied elsewhere, which is Cor 3.2's pattern with full defence slack;
  - (IB) copies with incoherent old or new sides;
  - (TC) on reverses of accepted cycles.

**6.2 Thm P is right, and the exception is total in the interior (PROVED; consistent with PP62).**

*Proposition 6.1.* If a ∈ int N and X ≠ C_a has V(rec(C_a → X)) = 0, then {a′ : C_{a′} ⪯_{w₀} X} is not closed at a.

*Proof.*
- At a the record is null, so it is refused at w₀.
- At a_t := a∘(1 + t e_{w₀}), V(rec(C_{a_t} → X)) = V(rec(C_{a_t} → C_a)), whose w₀-coordinate is > 0 (PP57 Lemma 4.1 and strict guiding), so it is accepted at w₀.
- a_t → a. ∎

Every interior member has such rivals (silence balanced amounts of its own Ep- and Em-type answers). R₀ by itself is in PP57 Cor 4.3's class (Λ's strict level-0 verdicts, any tie treatment), so it is a control, not a candidate. PP62 says as much.

**6.3 Thm E: confirmed. One proof gap in the corollary to Lemma S, repaired.**
- PP62's Lemma 1.3(b) proves Γ(u, u∘(1 + t e_w)) ∈ O_w by the transposition fixing w; I had found the same argument independently. Its Theorem E proof (one refusing world w from C_B's direct (C), then openness along e_w, defence, endorsement) is correct as written, and is a **new local exclusion of u¹-endorsed (M0-type) allocations**. It is unconditional at u and conditional on (H_Γ) elsewhere.
- *Gap.* The sentence after Lemma S, "a relation that accepts every record with V_w > 0 has all its acceptances at w endorsed", does not follow from Lemma S as stated: (TC) there only forces two more unfavourable acceptances.
- *Repair (PROVED).* Take E inside {Y strictly w-better than X}, which is non-null because V_w(rec(X, Y)) < 0, and small enough that 0 > V_w(rec(X, Z)) > V_w(rec(X, Y)). Then Y ⪯_w Z and Z ⪯_w X both have V_w > 0, so they are accepted. (TC) then demands X ⪯_w Z. But Z is a strict pure w-improvement of X, so strict (G) refuses it. Hence X ⋠_w Y. With this choice the corollary holds.
- *Lemma 1.3(a), (b) and Cor E.2(i): checked exactly.*
  - (a) follows from Lemma 1.1, using V = Σ c_i ε_i with c_w = α and c_v = −β_v.
  - (b) follows by the transposition fixing w. R is not symmetric in general, but the layer lies in R, where u¹ has the symmetric formula, and μ and the shift are τ-invariant.
  - E.2(i) uses σ_t ∩ F = ∅ and additivity, both valid.
- *E.2(ii) can be sharpened.* With E chosen inside {X strictly v-better than C_{u_t}} as in the repair above, the alternative "or accepts two more u¹-unfavourable comparisons" is excluded: the allocation **must refuse** one of the two u¹-favourable split links at v.
- *Remark.* PP62's first design, "accept iff V_w ≥ ρ_w(r)" with ρ_w = κ ∫|δ_w|, is an additive kernel with negative two-cycles. **Theorem 5.1 kills it without sections**: some member of the 2-D family is undefended. Theorem E kills it through sections. The two kills are independent.

**6.4 Thm M: correct as scoped, but it meets neither the brief's family nor its rival family (PROVED; CHECKED).**

*(a) u is not an interior point of N.* By Lemma 4.1, u∘(1 + t e₂) has Φ₂ < Φ₂(C_u), so it violates N_u's defining inequality, and it is far from N_B. Hence u ∈ ∂N: u is the apex of the sector N_u, and B likewise.
- The brief fixes "a compact, genuinely two-dimensional **neighbourhood** N of u".
- Thm M escapes Theorem Q and Theorem E exactly as the brief's item "fixed-rival limits toward the boundary of N" anticipates: the only shifts that would close the section leave the family. PP62 says this itself in §3.2 ("through the shape of the family").

*(b) Inside N, balanced member swaps out of interior members break openness (exact counterexample).*
- Let a := u∘(1 − s e₂), normalised. This is PP62's own interior witness a₁ in the proof of Lemma 3.1(i).
- `lobe63.py` (exact cells of {a, B}, s = 1/100 and 1/1000) shows: world 1 is the strictly middle coordinate of log(B/a), and {C_a ≠ C_B} contains non-null cells of both kinds (Ep-type: Wr = {1}, a answers, B silent; Em-type: Cor = {1}, a answers, B silent).
- So, by PP62 Cor 1.2 and Lyapunov, there is a non-conic F with V(F : a → B) = 0, and X := C_a[F ↦ C_B] is a null rival of the interior member a.
- By Prop 6.1 the section {a′ ∈ N : C_{a′} ⪯₂ X} is not closed at a: a∘(1 + t e₂) lies in N for small t, because a is interior.
- So on Thm M's own family, R₀ fails (S) for a rival of the brief's form X = C_a[F ↦ C_b] with a, b ∈ N. Thm M's scope (Z_X ⊆ {u, B}) excludes exactly this rival.

*(c) The module's rival family is one pair.* The open conditions (cell persistence, a strict middle coordinate) make (b) hold for every a in a neighbourhood of u. So every interior point of N_u near u has a balanced partner (B) and a section failure. The balanced swaps that Thm M handles are those of the single pair (u, B), at the two apexes. The sources vary in 2-D; the balanced rivals do not.

*(d) Consequence (PROVED).* For R₀ on any family N: if a balanced member swap X = C_a[F ↦ C_b] (a, b ∈ N) has its section closed at a, then a∘(1 + t e₂) ∉ N for small t. Under Thm E with (H_Γ), the same holds for every u¹-endorsed rule and the refusing world. So the brief's overlapping swap family over a genuine neighbourhood is out of reach for this whole class. That is the content of PP62's own "main gap", now with an exact witness inside its module.

*(e) Non-pure paths inside N; genuine 2-D (checked).*
- Thm P's openness is a pointwise statement about a ↦ V(rec(C_a → X)). For in-scope rivals it holds along every sequence in N, along every path and toward ∂N, so non-pure paths give no further failure.
- N_u is genuinely 2-D and its apex u is the strict Φ₂-minimiser by construction (Lemma 3.1, whose interior witness a₁ is valid).
- The defect is not the claimed properties but where u sits: at the apex.

**Verdict on PP62.**
- Thm R, Thm P, Thm E (at u) and the α-certificate are sound.
- The corollary to Lemma S needs the repair in 6.3.
- Thm M is a correct module, but it does not reach the brief's target outcome. The family is not a neighbourhood of u, and the balanced-swap rivals come from one pair of apex members; on the same family, balanced swaps out of interior members fail openness (6.4(b)).
- No exact counterexample to any *stated* theorem of PP62 was found.

**6.5 Ready tests for any revised rule.**
- **T1 (Thm 5.1).** Refusals ⊇ {J_i < 0} for an additive kernel with negative two-cycles ⇒ the kite has an undefended member.
- **T2 (§2).** Steps using rec(C_{a_t} → X) = rec(C_b[F ∪ σ_t ↦ C_{a_t}] → C_b) need σ_t ∩ D_ab = ∅ (fails 36/36).
- **T3 (Prop 5.4).** V-only rules fail (C) at the balanced swap.
- **T4 (Prop 6.1, Thm E).** Endorsed rules fail at every interior member with a balanced partner. Check where the partners are (`lobe63.py`).

---

## 7. Ledger hygiene

| Imported clause | Hypotheses (PP59) | Applies to the brief's swaps? |
|---|---|---|
| PP30 Thm 3.1 (entry 16, SAFE) | reflexivity, strict (G), (IB), (TC), T's defence; G ⊆ Sil(T) bounded, N answers a.e. on G | Yes, for answering-only swaps T[G ↦ C_b] with G ⊆ A_b ∖ A_u. The defence world w(G) is **independent of b** (T[G ↦ C_b] = T[G ↦ h]). The kill is at every member answering on G. It does **not** apply to swaps with a silencing part F⁺ ≠ ∅ (then G ⊄ Sil(T)). |
| PP36 Prop K / PP40 K^S (entry 18, SAFE) | (TC), strict (G), (IB); the closing link must be strict guidance, or the clause is conditional on an accepted strict comparison | Only with the closing link checked. In the mixed triangles of §4.7 the closing link is a member–member record (not guidance), so Prop K gives no clause there. |
| Theorem Q | (L0⁺) + a null non-conic member swap | Not to allocations that refuse some strict level-0 acceptances (REFEREE_round53 §7). |
| Theorem 5.1 here | (H_J) + (N2C) | Architecture-level (Ad): a LOCAL constraint on kernel-certified allocations; not a clause. |
| Lemma 3.1, Prop 4.4 | axioms only | TOOLs (they certify modifications and instances). |

---

## 8. Scripts (`r9/PP63_py/`; run `python3 -I -B <script>` inside the folder)

| Script | Content | Label |
|---|---|---|
| `kite63.py` → `kite63.out` | Theorem 5.1 certificate: kite, the seven bipartitions, exact problems, (2V), strictness, at two scales | CHECKED, ALL PASS |
| `surgery63.py 0` and `surgery63.py 1` → `surgery63.out`, `surgery63_ties.out` | Lemma 3.1 on PP56's exact 64-model instance: base Λ (0) and its level-1 relation with ties (1); 60 random (r, i) each: refusing {r, r⁻¹} at i keeps strict (G), (TC) on all ordered triples, protection; defence survives exactly as 3.1(b) predicts. Control: refusing r alone breaks (TC) in 36/60 trials on the tie base (0/60 on Λ, which has no ties) | CHECKED, ALL PASS |
| `r0_63.py` → `r0_63.out` | PP62's R₀ on PP56's exact instances with null records (equal Ep/Em masses), w₀ = 1, 2, 3, two and four values: strict (G), (TC) on all ordered triples, defence, protection | CHECKED, ALL PASS |
| `lobe63.py` → `lobe63.out` | §6.4(b): interior lobe point a = u∘(1 − s e₂) (s = 1/100, 1/1000) has Ep- and Em-type cells against B and middle world 1, so it has a balanced member swap | CHECKED, ALL PASS |
| `harness63.py` | Monte Carlo sample, members, balanced swap, V (for testing revised rules) | library (NUMERICS) |
| `shift63.py` → `shift63.out` | Prop 2.1–2.2: formulas (i)–(iii) cell by cell; σ ∩ D_ab ≠ ∅ in 36/36 cases; guidance status of s_t | CHECKED, ALL PASS (about 35 s) |
