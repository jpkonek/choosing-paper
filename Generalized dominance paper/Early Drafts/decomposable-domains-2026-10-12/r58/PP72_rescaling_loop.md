# PP72. Mixed-class repair on the exact rescaling loop

24 October 2026. Constructor, Brief 58. One author; not refereed. **This file is being written in stages. The DRAFT section below is posted first for PP73 and will not be changed in substance; results follow below it.**

---

## DRAFT (posted first for PP73)

**Coordinates.** Indices are written in log-likelihood coordinates modulo (1,1,1): an index m ∈ int Δ is identified with log m ∈ R³/R(1,1,1). C_m := D_{M_m}, M_m = {m∘p/(m·p) : p ∈ M}. Put δ₃ = (1,1,−2), δ₁ = (−2,1,1), δ₂ = (1,−2,1) (so d_k = exp(log a · δ_k), δ₁ + δ₂ + δ₃ = 0). Moving the index by +tδ_k (t > 0) is a pure decrease of world k's likelihood; C_{m+tδ_k} is pointwise no better than C_m at world k, strictly somewhere (PP57 Lemma 4.1 inverted).

**Family of sources (D1).** For s₀ > 0 small (fixed below; (2V) must hold on the whole set):

  𝔽 := {u} ∪ R₃ ∪ R₂,  R₃ := {sδ₃ : 0 < s ≤ s₀},  R₂ := {s(δ₃ + δ₁) = s(−1, 2, −1) : 0 < s ≤ s₀}.

So for a = e^s the loop u → m₁(a) = sδ₃ → m₂(a) = s(δ₃+δ₁) → u lies in 𝔽 for every a ∈ (1, e^{s₀}]. 𝔽 is compact, has no isolated point, and its only branch point (and the only accumulation point of loops) is u. The three loop edges at scale s are the moves +sδ₃, +sδ₁, +sδ₂.

**Installed models (D2).** 𝓘 := {C_{m + tδ_k} : m ∈ 𝔽, k ∈ {1,2,3}, 0 ≤ t ≤ t₀}, t₀ small, all posterior. Members of 𝓘 ∖ 𝔽 are *defenders*: they need defence against every measurable rival and protection, but no sections and no fill domination (brief, scope).

**Repair rule (D3), rival-dependent.** For m ∈ 𝔽, a class k, and a non-null measurable E ⊆ Sil(C_m) ∩ M_k, put X = C_m[E ↦ A] and

  B(m, E) := C_{m + τ δ_k},  τ = τ_k(m, E) := ½ · sup{ t ∈ (0, t₀] : C_{m+tδ_k} is silent on a non-null part of E }.

The repairing move is always the class-k move +δ_k. It is a loop edge exactly when (m, k) is (u, 3), (sδ₃, 1) or (s(δ₃+δ₁), 2) with τ = s; otherwise B is a defender. By guidance C_m ⪯_k B, which is the acceptance the forced pattern requires; the refusals C_m ⋠_i B (i ≠ k) are to be supplied by the relation.

**Relation (D4).** The relation is not given by a score. It is the least relation 𝓡(𝒟) containing:
- reflexivity and weak guidance at every world;
- the domination records rec(B(m,E), C_m[E ↦ A]) at all three worlds, with all (IB) copies;
- a defence assignment 𝒟: for every installed C and every measurable X ≠ C, one world 𝒟(C, X) ∈ {1,2,3} at which C ⪯ X is accepted (record-level, so shared by all copies);

and closed under (TC)-completion, the protection rule III, the tie rule IV and fixed-rival section limits on 𝔽. Everything else is refused. Success means: for some 𝒟, 𝓡(𝒟) has no reversed strict guidance (F1), no incoherent registered model (F2), every domination strict, and the forced refusals C_m ⋠_i B(m,E), i ≠ k.

The first candidate defence assignment is the u¹-witness 𝒟₀(C, X) := a world maximising V_w(rec(C, X)) for PP56's balanced field (ties broken toward the record's designated world). §2 below tests 𝒟₀ against Theorems Q and E and against direction counting before anything is built on it.

---
**Addendum to the DRAFT after PP73 (§5.2) and the relays; no substantive change.** The tie rule left undefined in (D4) is now fixed: among the maximal coordinates of V(rec(C, X)), 𝒟₀ chooses by the priority **2 ≻ 3 ≻ 1** (so a u¹-null record is defended at world 2). Prop 2.1 below shows this meets PP73's conditions (ρ1)–(ρ3).

---

## 0. Verdict

**The full deliverable is not reached; a substantial part of it is, in one relation.**

1. **Main positive result (Theorem 6.2; PROVED).** On the non-isolated family 𝔽 (both loop rays, every scale, with the accumulation point u), with a two-parameter set 𝓘 of installed posterior defenders, one record-based relation 𝓡_θ satisfies reflexivity, strict (G), (IB) with all copies, (TC) on every triangle, closed fixed-rival sections on 𝔽, and **universal defence, protection and direct (C) for every installed model against every measurable rival**. In it:
   - at T, every sufficiently small fill of **each of the three classes** with −h fraction ≥ 8θ is strictly dominated, by the class-k move C_{u+tδ_k} at a rival-dependent t (Cor 6.3);
   - two of the loop's three edges, u →(3) m₁ and m₂ →(2) u, are realised **in-family at rival-dependent scales**, together with their translates along the rays; the middle edge m₁ →(1) m₂ is realised only for fills with a large −h fraction, by defenders;
   - u¹ is used only as a **witness** (argmax defences; certified dominations). The relation does not contain u¹'s strict part, so Theorem Q does not apply; Theorem E does not apply on 𝔽 (§2).
2. **What remains, exactly (PROVED).** Pure-h fills of every class and every splice between installed models are H-models. In any u¹-endorsed relation they can be dominated only through u¹-null records (Prop 3.2), and a null record accepted at all worlds is the Theorem-Q(ii) pattern. **So these rivals need u¹-unfavourable acceptances.** The elementary (TC) cascade of such acceptances is absorbed: the member-carried records it forces to be refused are all defended at the class world by guidance (Prop 4.1).
3. **No single score can supply the favourable comparisons** (§3; PROVED, certificate-level): strict part ⇒ endorsement (Prop 3.1); direction counting, three pairwise disjoint cones per member (Prop 3.3); Theorem Q on arcs forces exact flatness of the score at world 1 or 2 (Prop 3.5).
4. **Exact finite instances (§5; CHECKED):** mixed-class recurrence with all three fill classes of all three loop members, the loop's own edges forced, and 240 consecutive-member splices, is SAT (every clause an axiom instance). The one UNSAT instance is the forced-pattern pigeonhole on a finite defender set (minimal core: 2 fills).
5. **Level.** No axiom-level conflict was found. Every failure is a feature of a choice (§7). The decisive open step is a two-sided version of Theorem 6.2's invariant that admits the unfavourable records of item 2 (§7).

| Item | Result | Label |
|---|---|---|
| Priority tie rule meets PP73 (ρ1)–(ρ3); Q, E inapplicable to 𝓡(𝒟₀) on 𝔽 | Prop 2.1 | PROVED (with PP73 §5.2) |
| Strict part of a field on all records ⇒ endorsement | Prop 3.1 | PROVED |
| u¹-containing relations dominate H-models only by null records | Prop 3.2 | PROVED |
| Direction counting: three disjoint cones per member | Prop 3.3, Cor 3.4 | PROVED |
| Flatness forced by Theorem Q on arcs (any field) | Prop 3.5 | PROVED |
| Lemma-S cascade misses member-carried records | Prop 4.1 | PROVED (elementary splits); general splits OPEN |
| Choice of scale: deficient worlds of a pure-h domination | Prop 4.2 | PROVED (with PP73 Prop 2.5(a)) |
| Finite instances: pigeonhole core; rich instances with loop edges and splices | §5 | CHECKED |
| Geometry of 𝔽: Φ injective, no strict world-1 maximum | Lemma 6.0 | PROVED |
| 𝓡_θ: all axioms, universal defence, protection, closed sections, θ-endorsed dominations | Thm 6.2 | PROVED |
| Coverage of (D3′): three classes at u; in-family edges along both rays | (D3′), Cor 6.3 | PROVED |
| Pure-h fills and installed splices (H-models) in one relation with sections | — | OPEN (needs unfavourable acceptances) |

---

## 1. Responses to PP73 and to the relays

| Item | Response |
|---|---|
| PP73 (1): one loop has no balanced swap; Q, E only across scales | Accepted (PP73 Cor 1.3). 𝔽 contains every scale, so cross-scale balanced pairs exist (PP73 Prop 4.1); §2 handles them. |
| PP73 (2): fill–splice identity; the successor cannot dominate splice-fills | Accepted. (D3) never uses the fixed successor: τ is half the agreement threshold, so B(m,E) is silent on part of E (PP73 §5.1(a)). The splice-fills of S_i are repaired at a smaller move, by a defender. |
| PP73 (3): the tie rule decides the balanced-swap test | Fixed: priority 2 ≻ 3 ≻ 1 (Prop 2.1). |
| PP73 (4), relay (1): Q at u hinges on T ⪯₃ X | Under the priority rule defence and sections give only world 2 at u on balanced X (Prop 2.1(c)); in the endorsed relation 𝓡_θ no null record is ever accepted at world 1 (Thm 6.2, step 3), so the all-world tie cannot form whatever happens at world 3. |
| PP73 (5): splices of installed models; (TC) with non-endorsed records | §4 (cascade), §5 (finite splice runs). In the endorsed relation 𝓡_θ, (TC) is PROVED on all triangles (Thm 6.2); with unfavourable records it remains OPEN (§7). |
| PP73 (6): design constraints | (D3) uses one repairer per (source, class) and distinct move directions per class, so the two-branch exclusion (PP73 Prop 3.2) is not triggered (PP73 §5.1(c)); dominators of a fixed fill are a single model, so Props 3.3–3.4 are not triggered. |
| Relay (2): forced refusals must be committed | They are: 𝓡(𝒟) refuses by default, and 𝒟₀ never selects them (PP73 §5.1(b)). |
| Relay (3)–(6) | Used as stated; 𝒲's rows are not reused. |

---

## 2. The tie rule and Theorems Q and E

Write Acc(r) for the set of worlds at which record r is accepted in 𝓡(𝒟₀).

**Prop 2.1 (PROVED, given PP73 §5.2).** Let 𝒟₀ break ties among maximal coordinates of V by 2 ≻ 3 ≻ 1.
- (a) For a ∈ R₃ and X with V(C_a → X) = 0: the R₃-outward records have V₁ = V₂ maximal (PP73 Lemma 4.7), so 𝒟₀ picks 2; the inward records pick 3 robustly; at a itself 𝒟₀ picks 2. The worlds forced by defence and section limits are {2, 3}.
- (b) For b ∈ R₂ and Y with V(C_b → Y) = 0: R₂-inward ties (1, 3) give 3, R₂-outward gives 2 robustly, and b itself gives 2. Forced worlds {2, 3}.
- (c) At u: R₃-outward gives 2, R₂-outward gives 2, u gives 2. Forced worlds {2}.
- (d) Hence PP73's (ρ1)–(ρ3) hold with ρ₁ = 2, ρ₂ = 3, and no balanced record out of a member of 𝔽 is accepted at all three worlds: the Theorem-Q(ii) tie never forms. The refused world of every u¹-null record out of 𝔽 is 1.
- (e) **Theorem Q** needs (L0⁺) for some field. 𝓡(𝒟₀) accepts a member-carried record only at its argmax world (plus guidance and closure), so it refuses strictly u¹-favourable comparisons at non-argmax worlds; (L0⁺) fails for u¹. For a general field ℓ, see Prop 3.5.
- (f) **Theorem E** (PP73 Thm 4.4) needs a family sequence in O_w for the refusing world w = 1. By PP73 Table 4.5, 𝔽 has no O₁-direction at any member. So it does not apply.

*Proof.* (a)–(c): V(C_{a′} → X) = Γ(a, a′) for a′ in 𝔽, and Lemma 6.0's proof gives the exact sign patterns (Γ₁ = Γ₂ = −Γ₃/2 on R₃, Γ₁ = Γ₃ = −Γ₂/2 on R₂). (d) is PP73's sufficiency statement for this test. (e)–(f) are read off. ∎

The section limits used in (a)–(c) concern member-carried records only. Defenders carry no section obligation, so their tie choices are free; we use the same priority.

**Caveat.** Prop 2.1 concerns the acceptances generated by defence and sections. Acceptances generated by (TC) from the non-endorsed domination records could in principle add world 1 to some Acc(r). §4 shows that the elementary splits do not; the general case is part of the OPEN step.

---

## 3. What a single score cannot do (certificate-level)

Throughout, ℓ is an integrable strictly guiding field (|ℓ_w(g, x)| ≤ K|g|, strictly increasing in the w-rank) and Φ(X) := ∫ ℓ(g, X(g)) dμ. For a source C and a class k, a *thin class-k fill sequence* is X_n = C[E_n ↦ A], E_n ⊆ Sil(C) ∩ M_k non-null, μ(E_n) → 0. Put v_n := Φ(X_n) − Φ(C). By strict guiding, v_{n,i} < 0 for i ≠ k and v_{n,k} > 0, and v_n → 0.

**Prop 3.1 (strict part ⇒ endorsement; PROVED).** If ⪯_w satisfies (TC) and strict (G) and contains {(X, Y) : Φ_w(Y) > Φ_w(X)} on all models, then X ⪯_w Y ⇒ Φ_w(X) ≤ Φ_w(Y).

*Proof.* PP71 Prop 2.6 used the whole order {Φ_w(X) ≤ Φ_w(Y)}, but its proof uses only strict instances. Suppose X ⪯_w Y and Φ_w(X) > Φ_w(Y). Then Y is not a.e. contradictory (otherwise Φ_w(Y) is maximal). Worsen Y on a small non-null set (μ atomless) to get Z with Φ_w(Y) < Φ_w(Z) < Φ_w(X). Then Y ⪯_w Z and Z ⪯_w X are strict instances, the triangle X → Y → Z → X is accepted, and (TC) installs Z ⪯_w Y, reversing strict guidance. ∎

**Prop 3.2 (u¹ and H-models; PROVED).** Let the relation contain the strict part of u¹ on all records, and let B be a posterior model in the (2V) region. If B dominates an H-model X, then V(rec(B, X)) = 0.

*Proof.* By Prop 3.1, B ⪯_w X ⇒ V_w(rec(B, X)) ≥ 0. B and X are both pointwise λ-Bayes for λ = (1,1,1) with equality on H-records (PP62 (U2)–(U3)), so Σ_w V_w = 0. Three non-negative numbers with zero sum vanish. ∎

So domination of a pure-h fill or of a member splice is then possible only at PP73's knife-edge (mass-balanced) scale, one scale per rival, and every such domination record is u¹-null. By Theorem Q(i)'s mechanism, a null record accepted at all worlds out of a family member with closed sections propagates to its (IB) copies; this is how Prop 3.2 and Theorem Q interact.

**Prop 3.3 (direction counting; PROVED).** Suppose the relation is ℓ-endorsed (for instance by Prop 3.1), and let C be installed and defended, with a supporting weight λ ≫ 0: λ·Φ(Y) ≥ λ·Φ(C) for all models Y. If installed B_n dominate thin class-k fills X_n of C, then Φ(B_n) → Φ(C), Φ(B_n) ≠ Φ(C), and every limit direction of (Φ(B_n) − Φ(C))/|Φ(B_n) − Φ(C)| lies in

  K̄_k(λ) := {z : z_k ≥ 0 ≥ z_i (i ≠ k), λ·z ≥ 0, |z| = 1}.

The three sets K̄₁(λ), K̄₂(λ), K̄₃(λ) are pairwise disjoint.

*Proof.* Endorsement and domination give z_n := Φ(B_n) − Φ(C) ≤ v_n coordinatewise. So limsup z_n ≤ 0, and λ·z_n ≥ 0 with λ ≫ 0 forces z_n → 0. z_n ≠ 0 since z_{n,i} ≤ v_{n,i} < 0. A limit direction z has z_i ≤ 0 for i ≠ k and λ·z ≥ 0, so z_k ≥ 0. If z ∈ K̄_j ∩ K̄_k with j ≠ k, then z_j = z_k = 0 and the third coordinate is ≤ 0, so λ·z ≥ 0 forces z = 0, which is not a unit vector. ∎

**Cor 3.4 (PROVED).** Under the hypotheses of Prop 3.3, if C has non-null silence in all three classes and thin fills of every class are dominated, the installed set must approach Φ(C) from three pairwise disjoint direction sets. If, near Φ(C), the Φ-image of the installed set is contained in finitely many arcs each having one-sided tangent directions at Φ(C), there must be at least three arc-ends there, one for each class. In particular:
- 𝔽 alone fails at every interior ray point (two arc-ends);
- the loop alone at one scale fails at each of its members (forced pattern: the other two members serve at most two classes);
- an additive (or Bayes-act) certificate for the brief's target needs an installed set whose Φ-image is "three-branched at every member", which for a continuum of members means a genuinely two-dimensional Bayes sheet around 𝔽: a local realisation problem.

*Proof.* Each arc-end contributes one direction, which lies in at most one K̄_k. ∎

This is a certificate-level statement: it binds endorsed relations with strictly positive Bayes weights only. It does not bind 𝓡(𝒟₀), whose domination records are not endorsed.

**Prop 3.5 (Theorem Q on arcs forces flatness; PROVED).** Let J be an open sub-arc of R₃ on which the relation satisfies (L0⁺) for some strictly guiding field ℓ and has closed sections, and suppose every a ∈ J has an ℓ-balanced non-conic swap with a registered model. Then there are i ∈ {1, 2} and an open sub-arc I ⊆ J on which a ↦ Φ_i(C_a) is constant.

*Proof.* Let W(a) be the set of worlds w for which some family sequence b_n → a has Φ_w(C_{b_n}) < Φ_w(C_a). Inward points of R₃ are pointwise strictly 3-better, so 3 ∈ W(a). Theorem Q (PP57 Thm 4.2; its proof uses only such sequences, not pure shifts) and the balanced swap give a direct-(C) failure if W(a) = {1, 2, 3}. Hence each a ∈ J is a local minimiser of Φ₁∘C or of Φ₂∘C along J. Put A_{i,n} := {a ∈ J : Φ_i(C_{a′}) ≥ Φ_i(C_a) whenever |a′ − a| < 1/n}. These sets are relatively closed (a ↦ Φ(C_a) is continuous by continuity in measure and dominated convergence) and cover J. By Baire, some A_{i,n} contains an open arc I′; on a sub-arc I of length < 1/n every point is a local minimiser of the continuous function Φ_i∘C, which is therefore constant on I (PP56 Prop 5.1, step 4). ∎

So any score that both supplies the favourable comparisons out of ray members and survives Theorem Q must be exactly flat at world 1 or 2 along some piece of the ray. For u¹ itself Φ₁ = Φ₂ is strictly decreasing outward, so u¹ fails everywhere on R₃ (PP73 Prop 4.3). A flat ℓ is then exposed to Prop 3.3: along I, z₁ = 0 for the ray directions, so ray members cannot dominate class-2 or class-3 thin fills, which need z₁ < 0.

---
## 4. The (TC) cascade of a non-endorsed domination record

Fix a source C = C_m (m ∈ 𝔽), a class k, a fill X = C[E ↦ A] with E ⊆ Sil(C) ∩ M_k, and its repairer B = C_{m+τδ_k} from (D3). Let L := {B ≠ C} (the layer), E_A := E ∩ {B = A} (on E, B ∈ {S, A}, PP73 Lemma 1.2(b)–(c)), and r := rec(B → X). Then

  r⁻¹ = rec(X → B) = (E ∖ E_A : A → S) ⊕ (L ∖ E : C → B).

Write U := E ∖ E_A (the "unfill" part) and, for a world j, L_j := the odd-j points of L ∖ E.

**u¹ ledger of the layer (PROVED; PP62 (1.1) and PP73 Lemma 1.2).** For i ≠ k let j be the third world. On rec(C → B), per unit |g|-mass: odd-i points contribute −2 to V_i, odd-k points −1, odd-j points +1; at world k every layer point contributes +1 or +2 (B is pointwise k-worse).

**Prop 4.1 (the elementary cascade; PROVED).** Suppose the relation accepts r at a world w with V_w(r) < 0, and consider the triangles B → X → Z_Q → B with Z_Q := B[Q ↦ X], Q ⊆ supp r. Their two non-domination links are the halves h_{Q^c} := (supp r ∖ Q : X → B) and h_Q := (Q : X → B).
- (a) **w = i ≠ k.** If h_{Q^c} is pointwise weakly i-worse for its new side (that is, Q^c ⊆ U ∪ L_j), it is a guidance acceptance and (TC) with strict (G) forces h_Q ∉ Acc_i. The member-carried halves among these are exactly
  h_Q = (Q : C → B) with L_i ∪ L_k ⊆ Q ⊆ L ∖ E,
  i.e. C's records against the splices C[Q ↦ B] that contain all of B's i-improvements off E. So C must refuse these splices at world i. **They are all defended at world k by guidance** (C → B is pointwise k-worse), and their protection holds at k (strict (G)). Moreover V_k(h_Q) − V_i(h_Q) = 3(m(Q ∩ L_i) + m(Q ∩ L_k)) > 0, so 𝒟₀ chooses k for them, robustly in the source (the perturbation Γ → 0 along 𝔽). Hence no section limit on 𝔽 forces C ⪯_i C[Q ↦ B]: **the forced refusals are compatible with defence, protection, the priority rule and sections.**
- (b) **w = k.** A guidance half at world k must avoid U (the unfill A → S improves world k), so every forced-refused half contains U and is **not carried by C**, nor by any model silent on U. If an installed model D carries one (D = A on U and D = C on Q ∖ U), the refusal becomes D's refusal at k, and D must defend that record at i or j. For the δ_k-defenders of C this does not occur when Q ∖ U ≠ ∅ (they answer A on all of U only beyond the agreement threshold, and then differ from C on all of L); for other defenders of the two-parameter set 𝓘 it is not checked here (part of the OPEN step).
- (c) In both cases the cascade forces refusals only. Refusals never trigger (TC), so the elementary splits generate no further acceptances.

*Proof.* (a) The triangle is accepted at i if h_Q and h_{Q^c} are; (TC) then installs the reverse of the guidance link h_{Q^c}, which strict (G) forbids if h_{Q^c} is strictly i-worse somewhere (it is: U or L_j is non-null whenever the half is non-trivial). A half is carried by C iff X = C on it, i.e. iff it misses U. The ledger gives V_k − V_i. Robustness: for C′ = C_{m′} with m′ → m in 𝔽 and the fixed rival C[Q ↦ B], V(C′ → C[Q ↦ B]) = Γ(m, m′) + V(h_Q) and Γ(m, m′) → 0 (continuity in measure). (b) A half that is a world-k guidance link cannot contain any point of U, since there the new side S is k-better than A; hence the refused half contains U, where X = A ≠ S = C. The δ_k-defender claim is nesting along the δ_k ray (PP73 Lemma 1.2): C_{m+tδ_k} = A on all of U only for t beyond the agreement threshold, and its layer then contains L. ∎

**Prop 4.2 (which worlds are deficient; PROVED with PP73 Prop 2.5(a)).** For a pure-h class-3 fill of T repaired at layer mass p (u¹-mass of L) with fill mass e:

  V(B → X) = (p − e, p − e, 2e − 2p).

So the domination is deficient at the two non-class worlds if p < e, at the class world if p > e, and u¹-null at p = e. (D3) does not control which case occurs; Prop 4.1 covers both. The same computation at the other members of 𝔽 is NUMERICS-level (PP73 Lemma 1.4(b)), with the same sign structure.

**What remains of the cascade (OPEN).** Prop 4.1 treats the triangles through r whose third vertex is a splice of r's own endpoints. A general triangle through a copy of r has links (Y → Z) and (Z → X′) that each contain a piece of r⁻¹ plus mutually inverse extra parts. When both links are 𝒟₀-acceptances or other domination records, the argument above does not apply as stated. This is the precise open step in (TC) for 𝓡(𝒟₀). §5 tests it exactly on finite sub-universes, with the defences left free.

---
## 5. Exact finite instances (CHECKED)

**Encoding** (`PP72_py/lib72b.py`, a memory-lean re-implementation of PP71's lib71 with the same clauses). Cells are the faces of the exact plane arrangement of all installed models (PP71's exact census); every cell where some installed model is silent is split into a bounded piece and its rest. One SAT variable per (record, world), so all (IB) copies inside the sub-universe share it. Clauses: reflexivity; weak and strict (G) on every pair; defence of every installed model at a world of {1,2,3} against every model of the sub-universe; protection and direct (C) for every installed model (bounded fills are incoherent; every other non-installed model is treated as *possibly coherent*, the weakest labelling); (TC) added lazily with a final check over every ordered triple. Domination of a rival by "some installed model" is a disjunction with fresh selector variables (all three worlds accepted, some reverse refused). **Every clause except the domination requirements is an axiom instance, so UNSAT means no relation satisfying the axioms on the full domain makes those installed models defended and protected and meets those requirements; SAT is evidence only.** Candidates for dominating a rival are pre-screened by two axiom-level filters: the agreement obstruction (PP73 Lemma 2.4) and strict (G) (a candidate pointwise worse than the rival at some world can never be ⪯ it there). A rival with no admissible installed candidate is *deferred*: in the continuum it needs a smaller move.

**Loop and moves.** In unnormalised coordinates the loop at scale b = a³ is T = (1,1,1) → C1 = (b,b,1) → C2 = (1,b,1) → T. A move of class k by factor c divides coordinate k by c. b = 5/4 throughout ((2V) checked exactly for every installed index). Fills: for each loop member and class, each single silent bounded piece, the union of all of them, and the whole class silence (conic).

| Run | Installed | Cells / models | Requirement | Result |
|---|---|---|---|---|
| E0 | loop + one move (c = 9/8) per non-loop class: 9 models | 186 / 495 | every admissible fill of every class of T, C1, C2 dominated by an installed model (159 fills; 3 deferred) | **UNSAT; minimal core = 2 fills** |
| E0′ | same | same | T's three classes only | UNSAT (53 fills); each class alone SAT |
| E1 | loop + moves c ∈ {5/4, 17/16} for every member and class: 18 models | 594 / 486 | as E0 (465 fills; 3 deferred) | **SAT** |
| E1L | as E1 | as E1 | E1 **and** the loop successor itself dominates every fill of its edge's class that it can admissibly dominate (T's class 3 by C1, C1's class 1 by C2, C2's class 2 by T) | **SAT** |
| E2 | as E1 | 594 / 688 | E1L **and** 80 sampled splices per consecutive loop pair (single-cell and co-single-cell H; 240 in all), each dominated by an installed model other than its ends | **SAT** |
| E3 | as E1 | 594 / 626 | T's 155 fills of all classes with the loop edge forced, **and** 40 sampled splices for each of 12 installed pairs (480 in all): the three loop pairs, each member with its class moves, and two defender–defender pairs (DIGEST) | **SAT** (no splice deferred) |

**E0's core** (`core72_s54.out`): T's class-1 fill on the piece `1SSAASSSAA` and T's class-3 fill on the piece `3SAASSSAAA` both have the single admissible candidate C1>2 (the class-2 move of C1). By the forced pattern, one ordered pair (T, B) cannot repair two classes. **This is the audit's pigeonhole, met by a finite defender set; it disappears in E1.** It is a design rule: every (source, class) needs admissible candidates of its own, at rival-dependent moves.

**E1 / E1L verdicts among the loop members** (A = accepted, r = refused, worlds 1, 2, 3):

| | vs T | vs C1 | vs C2 |
|---|---|---|---|
| T (E1L) | — | rrA | Arr |
| C1 (E1L) | rAr | — | Arr |
| C2 (E1L) | rAr | rrA | — |

The three loop edges carry exactly the forced pattern (T ⪯₃ C1 only; C1 ⪯₁ C2 only; C2 ⪯₂ T only), every member defends against every other at exactly one world, and against each of its class-k moves exactly at world k (`sat72c_E1L.out`). The deferred fills are the innermost-layer pieces of each edge (one per edge), which need a move smaller than 17/16.

**What these runs show.** At cell level (E1L–E3), mixed-class recurrence with all three fill classes of all three members, the loop's own edges exercised, is consistent with every axiom instance, including all (TC) triangles of the sub-universe and the non-endorsed domination records. So the open step of §4 has no finite counterexample on these instances. They do not supply a rule: the defences are found by the solver, not by 𝒟₀ (a SAT run with 𝒟₀'s choices imposed would need the u¹ masses of every cell; not done).

## 6. The strongest partial theorem: a clean endorsed relation on 𝔽, with mixed-class repairs at u

§§2–4 suggest separating what u¹ can witness from what it cannot. This section proves that everything the brief asks for holds on 𝔽 for the rivals u¹ can witness, and isolates the rest.

**Setting.** s₀, t₀ are small enough that every installed index lies in the (2V) region with margin, and u¹ is PP56's balanced field for a (2V) family containing 𝓘. Every installed model is then pointwise λ-Bayes for u¹ with λ = (1,1,1), so Σ_w V_w(rec(C → X)) ≥ 0 for installed C and every X (PP62 (U2)).

**Lemma 6.0 (geometry of 𝔽; PROVED).**
- (a) a ↦ Φ(C_a) is injective and continuous on 𝔽.
- (b) For a, a′ ∈ 𝔽 with a′ ≠ a close to a, the vector Γ(a, a′) := Φ(C_a) − Φ(C_{a′}) never has a strict maximum at world 1, and Γ₁(a, a′) ≠ 0.

*Proof.* Continuity: continuity in measure and |u¹| ≤ K|g|. All members are H-related, so ΣΦ is constant on 𝔽. The transposition (1 2) fixes R₃ ∪ {u} and (1 3) fixes R₂ ∪ {u} (PP73 Lemma 4.7), so Φ₁ = Φ₂ on R₃ and Φ₁ = Φ₃ on R₂; at u all three coincide. Along R₃, Φ₃ is strictly increasing outward (outward moves are pointwise strictly 3-worse and u¹ is strictly guiding), and along R₂, Φ₂ is strictly decreasing outward. So each ray maps injectively onto a segment of a line, the two lines {Φ₁ = Φ₂} and {Φ₁ = Φ₃} (inside ΣΦ = const) meet only at Φ(T), and (a) follows. For (b), near a the family is one ray (two at u). On R₃: Γ₁ = Γ₂ = −Γ₃/2 with Γ₃ ≠ 0, so the maximum is the tie {1, 2} (outward) or world 3 (inward), and Γ₁ ≠ 0. On R₂: Γ₁ = Γ₃ = −Γ₂/2 with Γ₂ ≠ 0, so the maximum is world 2 (outward) or the tie {1, 3} (inward), and Γ₁ ≠ 0. ∎

**Definition 6.1 (the relation 𝓡_θ).** Fix θ ∈ (0, 1]. Call a pair (B, X), B ∈ 𝓘 and X a fill of a member of 𝔽, *θ-endorsed* if

  V(rec(B → X)) ≥ 0 at every world,  and  max_w V_w(rec(B → X)) ≥ θ · m(supp rec(B → X)),

where m is |g|-mass. Choose for each fill X at most one θ-endorsed designated dominator B(X) (rule (D3′) below). Let 𝓡_θ be the least relation containing
- reflexivity and weak guidance;
- the defences 𝒟₀ (argmax of V(rec(C → X)), ties by 2 ≻ 3 ≻ 1), for every installed C and every measurable X;
- the designated records rec(B(X) → X) at all three worlds;

closed under (IB) (everything is record-level), (TC) completion, rules III and IV, and fixed-rival section limits on 𝔽. It exists by Knaster–Tarski: the operator is monotone on sets of (record, world) pairs, and the fixed point is reached through transfinite stages whose unions preserve everything below.

**Theorem 6.2 (PROVED).** 𝓡_θ satisfies reflexivity, strict (G), (IB) with all copies, and (TC) on every triangle of measurable models. Every installed model (members of 𝔽 and defenders) is defended against every measurable rival, is undominated, and has no all-world tie partner; so rules III–IV never fire, and direct (C) holds. Fixed-rival sections are closed on 𝔽, including at u. Every designated B(X) strictly dominates X.

*Proof.*
1. **Endorsement invariant.** Every accepted (r, w) has V_w(r) ≥ 0. Generators: guidance (non-trivial ⇒ V_w > 0, u¹ strictly guiding); 𝒟₀ (the maximal coordinate of a vector with non-negative sum); designated records (by definition). Completion: an accepted triangle at w has V_w-values ≥ 0 summing to 0, so all vanish, and the installed reverses have V_w = 0. Section limits: V_w(rec(C_{a_n} → X)) ≥ 0 passes to the limit by continuity. Rule III: if X ⪯_w N at every w, endorsement gives V(rec(X → N)) ≥ 0, while its sum is ≤ 0 (N is λ-Bayes), so it is 0 and the installed reverses have V = 0.
2. **Strict (G), (IB), (TC).** A reversed strict guidance record has V_w < 0, so it is never accepted. (IB) and (TC) hold by construction.
3. **No null record is ever accepted at world 1.** (A record r is *null* if V(r) = 0.) By induction over the stages. Guidance records are not null. 𝒟₀ sends a null record to world 2. Designated records have max V ≥ θ m(supp) > 0. Completion at world 1 installs reverses of the links of an accepted world-1 triangle; by the induction hypothesis those links are non-null, and the reverse of a non-null record is non-null. Rule III needs an earlier null acceptance at every world. It remains to consider section limits at world 1. Suppose C_{a_n} ⪯₁ X with a_n → a and rec(C_a → X) null; by Lemma 6.0(a), a is the unique member with Φ(C_a) = Φ(X), so V(rec(C_{a_n} → X)) = Γ(a, a_n) with a_n ≠ a. Each acceptance at a_n was produced by one of the following.
   - Guidance: then X is pointwise 1-worse than C_{a_n} for infinitely many n, hence weakly 1-worse than C_a a.e. (C_{a_n} → C_a a.e. along a subsequence), so V₁(C_a → X) > 0 unless X = C_a. Contradiction.
   - 𝒟₀: impossible, since Γ(a, a_n) never has a strict maximum at 1 (Lemma 6.0(b)).
   - Completion: it needs V₁ = Γ₁(a, a_n) = 0, which is excluded by Lemma 6.0(b).
   - A copy of a designated record: then |Γ(a, a_n)|_∞ ≥ θ m(supp rec(C_{a_n} → X)) ≥ θ m({X ≠ C_a})/2 for large n, contradicting Γ(a, a_n) → 0.
   - A section limit at a_n: such acceptances are limits of acceptances of the four kinds above at points a′ ≠ a. Guidance and designated acceptances do not accumulate at a (first and fourth bullets), and the other two kinds never occur at points a′ ≠ a near a. So, by induction on the stage, a is not in the closure of the world-1 acceptance set of X, and no limit installs rec(C_a → X) at world 1.
4. **Defence.** 𝒟₀ supplies a world for every installed C and every X.
5. **Protection and (C).** If X ⪯_w C at every w for installed C, then by step 1 rec(X → C) is null and accepted at world 1, which contradicts step 3. So no installed model is weakly dominated by any other model, and has no all-world tie partner.
6. **Strict domination.** B(X) ⪯_w X at every w. Some coordinate of V(rec(B(X) → X)) is positive, so at that world the reverse has V < 0 and is refused by step 1.
7. **Sections.** The acceptance sets are closed under fixed-rival limits on 𝔽 by construction. ∎

**Rule (D3′) and its coverage (PROVED).** For a member m, a class k and a fill X = C_m[E ↦ A], write e and f for the |g|-masses of the h-part and the −h part of E, x = e + f, and B_t = C_{m+tδ_k}. On a class-k fill, the h-part contributes −ε_k per unit mass, and the −h part contributes the "otherwise" row of u¹, (4 at world k, −1 elsewhere). With the layer ledger of §4 (odd-k mass α(t), odd-i and odd-j masses β_i(t), β_j(t)):

  V(B_t → X)_k = 2e + 4f − (2α + β_i + β_j),  V(B_t → X)_i = α + 2β_i − β_j − x,  V(B_t → X)_j = α + 2β_j − β_i − x.

Put Q(t) := α + (β_i + β_j)/2 and Δ(t) := β_i − β_j. Q is continuous and increasing from Q(0) = 0. (D3′) takes B(X) := B_t for the least t with Q(t) = x + f/2, provided such t ≤ t₀ exists and the pair is θ-endorsed. Then:
- (a) **Symmetric classes, exact.** If Δ ≡ 0 along the move, then V(B_t → X) = (f/2, f/2, f) (in the order i, j, k), and (B_t, X) is θ-endorsed for every fill with f ≥ 8θx and x + f/2 ≤ Q(t₀). This holds:
  - **at u for all three classes**, by the S₃-symmetry of T, μ and u¹;
  - **along R₃ ∪ {u} for class 3**, where the move +tδ₃ stays on R₃ ((1 2)-symmetric). These repairers are **loop members m₁ at a rival-dependent scale**: the loop edge u →(3) m₁, and its translates along R₃;
  - **along R₂ ∪ {u} for class 2**, where the move +tδ₂ runs inward along R₂ ((1 3)-symmetric). These are **in-family repairs, including the loop edge m₂ →(2) u** at the scale where the move reaches u.
- (b) **Asymmetric classes.** If |Δ(t)| ≤ κ Q(t), then (B_t, X) is endorsed whenever f ≥ 3κ(x + f/2), and θ-endorsed with θ of order f/x. This covers the loop's middle edge m₁ →(1) m₂ (class 1 at R₃ members) only for fills with a large −h fraction; the repairer is then generally a defender, not m₂.
- (c) **The agreement obstruction is automatic** when f > 0: posterior models never answer −h in the (2V) region, so B_t is silent on the −h part of E.

*Proof.* The three coordinates are V(C_m → X) − V(C_m → B_t), with the ledger of §4 and the u¹ rows (PP73 Prop 2.5(a)). In (a), Q(t) = x + f/2 gives the displayed vector. Its maximum is f, and m(supp) ≤ x + m(L) ≤ x + 2Q ≤ 4x (|g|-mass of the layer is at most twice its u¹-mass), which gives the θ bound. The symmetries: a transposition fixing the source index and the move direction preserves μ, |g|, M and u¹, so it exchanges the odd-i and odd-j layer masses, and Δ = 0. (b) is the same computation with |Δ| ≤ κQ. (c) is (2V). ∎

**Cor 6.3 (what is repaired, and by whom).** In one relation 𝓡_θ, with universal defence, protection, (IB), (TC) and closed sections on the non-isolated family 𝔽 (accumulation point u included):
- at T, every fill of **each of the three classes** whose −h fraction is at least 8θ and whose mass is small enough is strictly dominated, by C_{u+tδ_k} at a rival-dependent t;
- two of the loop's three edges are realised in-family at rival-dependent scales (u →(3) m₁ and m₂ →(2) u), with all their translates along the rays;
- the middle edge is realised only for fills with a large −h fraction, by defenders.

**What 𝓡_θ cannot do, and why (PROVED).** Pure-h fills (f = 0) of every class and every member, and every splice between installed models, are H-models. By step 1 every acceptance of 𝓡_θ is u¹-endorsed, so by Prop 3.2 they can be dominated only through u¹-null records. A null domination record is accepted at world 1, which breaks step 3, the step on which protection rests. (When such a record is a balanced member swap, accepting it at all worlds is exactly the Theorem-Q(ii) pattern.) So **these rivals require non-endorsed acceptances**, or a different world playing step 3's role, i.e. a departure from 𝓡_θ in the place PP73 Prop 2.5(c) and §4 identify. For them the available evidence is Prop 4.1 (the elementary cascade is harmless) and §5 (cell-level SAT, with the loop edges forced and consecutive splices included).

---

## 7. Level of the failure, and the next step

- **Axiom-level conflict: none found.** The only UNSAT instance (E0) is the forced-pattern pigeonhole on a finite defender set and disappears with a second move size.
- **Choice-level failures, each proved:** the fixed successor (PP73 Thm 2.3); finite defender sets (E0); score-supplied favourable comparisons (Props 3.1–3.5); endorsement for H-model rivals (Prop 3.2 with Theorem 6.2's step 3).
- **Scores as witnesses only.** In 𝓡_θ, u¹ witnesses the defending world (argmax) and certifies the dominations, but 𝓡_θ does not contain u¹'s strict part (it refuses favourable comparisons at non-argmax worlds), so Theorem Q does not apply, and Theorem E does not apply on 𝔽. Mixed triangles across the three generator types (guidance, argmax defences, designated dominations) are handled by the single invariant of step 1, which does not depend on which piece a link comes from.
- **The precise next step.** Extend Theorem 6.2's invariant from "V_w ≥ 0" to a two-sided invariant that admits u¹-unfavourable designated records for pure-h fills and member splices, while keeping two facts: (i) no null record at a fixed world (step 3), and (ii) for every unfavourable designated record r at w, every bipartition of r⁻¹ into a guidance half and a member-carried half has the member-carried half refused at w (Prop 4.1; it is then defended at k by guidance). E1L–E3 show this is consistent on the cell sub-universes tested.

---

## 8. Scripts (`r9/PP72_py/`; run `python3 -I -B <script>.py` inside the folder; environment variables as listed)

| Script → output | Content | Label |
|---|---|---|
| `geom72.py` | posterior vertices, the loop at scale b, class moves, (2V) test (imports PP71's exact geometry unchanged) | library |
| `lib72b.py` | lean SAT encoding: (G), (IB), defence, protection + (C), lazy (TC) with full final check; `DIGEST=1` uses 128-bit record digests (a collision can only add constraints, so SAT results stay valid) | library |
| `inst72.py` | cells with piece/rest splits, fills of all three classes, splices, disjunctive domination | library |
| `explore72.py` | one loop: cell census; each edge strictly worse at its world and mixed at the other two | CHECKED |
| `sat72b.py` → `sat72b_E0T.out`; `core72.py` → `core72_s54.out`, `core72_T_rich.out` | E0′ (T only, one move size): UNSAT; E0: UNSAT, minimal core of 2 fills (forced-pattern pigeonhole); T only with two move sizes: SAT | CHECKED |
| `sat72c.py` → `sat72c_E1.out`, `sat72c_E1L.out`, `sat72c_E2.out`, `sat72c_E3.out` | E1 (rich moves): SAT; E1L (loop edges forced): SAT; E2 (+240 consecutive splices; DIGEST): SAT; E3 (+480 member–repairer and defender splices; DIGEST): SAT | CHECKED |
| `diag72.py`, `size72*.py` | candidate screening; instance sizes | — |
