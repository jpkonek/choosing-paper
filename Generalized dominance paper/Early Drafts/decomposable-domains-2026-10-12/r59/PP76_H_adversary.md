# PP76. Adversary on H-repair: coupled refusals at committed sources, section closure followed by copying, and the repair operation

24 October 2026. Adversary, Brief 59. One author; not refereed. §3 attacks PP74 as posted in its DRAFT section (ASR, items 1–4, (U1)–(U4)); later PP74 sections were not available.

**Labels.**
- PROVED: complete argument here, or a cited result used inside its stated hypotheses.
- CHECKED: exact finite computation in `r9/PP76_py/` (enumeration of every case in the stated range).
- NUMERICS: Monte Carlo on a standard Gaussian sample, in `r9/PP76_py/`.
- CONJECTURE / OPEN: as stated.

**Axioms used** (Brief 59): reflexivity; strict (G); (IB); (TC); (S) (coherent selected models, undominated, competitive on supp p, closed fixed-rival sections); (LA); global (C). No score, symmetry, fixed successor or guidance-worsening assumption enters any axiom-level claim. Hypotheses that are properties of a *design* are named where used.

**Conventions.** X ⪯_w Y: X is at least as good as Y at world w. rec(X → Y) = (support {X ≠ Y} : old values → new values); a record *accepted at w* means old ⪯_w new. A model C *carries* r if C equals the old side on supp r; then C ⊕ r := C[supp r ↦ new]. "Strictly w-worse" means pointwise weakly w-worse a.e. and strictly on a non-null set (the strict-guidance relation). Coherent models never give contradictory advice.

**H in two-state form.** On R every H-model says h or S. At g ∈ R with odd world o(g) (PP62 §1.1) one of the two values is better at o(g) and worse at the other two worlds. For a model N ∈ H and g ∈ R put

  Up_N(g) := {worlds improved by flipping N at g} = {o(g)} or {1, 2, 3} ∖ {o(g)}.

Write Up_w(N) := {g : w ∈ Up_N(g)} and Down_w(N) := R ∖ Up_w(N). For a pure set E (all points of one *type*, i.e. one odd world and one N-state) write Up(E) for the common value. Every point lies in Up_w for one world (type "(o,0)", flipping improves only o) or two (type "(o,1)").

---

## 0. Verdict

1. **Task 1 (PROVED; CHECKED).** The first-generation coupled refusals are described exactly, for every accepted record and every committed carrier (Theorem 1.1). Within H this becomes a formula with no free parameter (Cor 1.4):
   - every protected N has a non-null *correction set* U_N := {B = N ≠ X} (generalised agreement obstruction, Lemma 1.3; axiom-level);
   - N is forced to refuse some rival at world w **iff** U_N ⊆ Up_w(N);
   - for X = N ⊕ E the refusal worlds contain ⋂_{g∈E} Up_N(g), so for a **pure** fill they are exactly Up(E) whatever the dominator. This is uniform over measurable, nested, overlapping and arbitrarily small E.
2. **No axiom-level obstruction at this layer (PROVED).**
   - One acceptance never exhausts a full-support source's defence against any rival (Cor 1.2).
   - One acceptance never produces a section-limit conflict, however its sources accumulate (Prop 1.5).
   - Exhaustion needs **two or more acceptances**. Its exact criterion is Prop 1.6 (CHECKED). Example 1.7: two dominators of complementary pure fills of T that share their layer L leave T without a defence against T ⊕ L. That is a constraint on choices, not on the axioms.
   - Whether every incoherent H-model can be dominated while T and a non-isolated family keep closed sections remains **OPEN**. §1.9 says what an obstruction would have to use: an acceptance that is *generated* (a forced defence, or an argmax defence), transported by sections and copies.
3. **Task 2 (PROVED; NUMERICS).** Section closure followed by copying breaks PP72 Theorem 6.2 (Prop 2.1). This is an independent construction, with different parameters, of the counterexample in REFEREE_round58 §1.3. The general mechanism is Lemma 2.2: an acceptance set is a property of records, so every invariant must be record-intrinsic and closed at **every** carrier's sections. REFEREE_round58's margin repair 𝒟₀^κ survives my version.
4. **Task 3 (PROVED; CHECKED; NUMERICS).** ASR is genuinely outside the zero-sum form on its domination records (§3.1). Its claim that affected sources are defended by anchor guidance with **no new acceptance** is false, in two ways:
   - The coupled rule over all copies refuses *extended* rivals, which have no guidance defence at any world. This happens in 2,220 of 7,236 affected pairs (Prop 3.2, CHECKED).
   - Sections force refusals at every neighbour of an affected source, and on PP72's family the anchor guidance fails at every R₂-neighbour of u (Prop 3.3).

   Also:
   - The (R1) class is not open.
   - The second application needs two further axiom-level clauses, (U1′) and (U2′), and (U3) must become a permanent invariant (§3.4).
   - Joint defeat (Prop 1.6) is not checked by ASR (§3.5).

   **None of these is an axiom-level contradiction.** The forced new acceptances never defeat C or B at first order (0 of 2,220, CHECKED). They are, however, *generated* acceptances, which is exactly the class that Prop 2.1's section-then-copy mechanism exploits. ASR must give them closed, record-intrinsic classes.

---

## 1. Task 1: which committed sources must refuse, and when defence is exhausted

### 1.1 The first generation, exactly

Let r = rec(B → X) be accepted at w, with D := supp r. The *coupled rule* is the (TC) + strict (G) consequence: for every common-context copy (B′, X′) = (W[D ↦ B], W[D ↦ X]) of r and every Y strictly w-worse than X′, refuse rec(Y → B′) at w, together with all its copies. (If Y ⪯_w B′ were accepted, B′ ⪯_w X′ ⪯_w Y ⪯_w B′ would be an accepted triangle, and (TC) would install the reverse of the strict guidance link X′ ⪯_w Y.) Call these refusals *first-generation*.

**Theorem 1.1 (PROVED; CHECKED, `check_t1_76.out`).** Let r = rec(B → X) be accepted at w, where r does not itself violate strict (G). Let C be any model. The first-generation refusals at the carrier C are exactly the refusals C ⋠_w Z with

  Z = C[G₁ ↦ B][G₂ ↦ n],

where:
- (a) G₁ ⊆ D ∩ {C ≠ B}, and C is weakly w-worse than X on G₁;
- (b) B is weakly w-worse than X on D ∖ G₁;
- (c) G₂ ∩ D = ∅, and n is strictly w-better than C at every point of G₂;
- (d) (strictness) on G₁, C is strictly w-worse than X somewhere; or on D ∖ G₁, B is strictly w-worse than X somewhere; or G₂ is non-null.

*Proof.* A refused record s = rec(Y → B′) is carried by C iff C = Y on S := {Y ≠ B′}, and then C ⊕ s = C[S ↦ B′]. Put G₁ := S ∩ D and G₂ := S ∖ D.
- On D we have B′ = B and X′ = X.
- On G₁, Y = C must be weakly w-worse than X; this is (a).
- On D ∖ G₁, Y = B′ = B must be weakly w-worse than X; this is (b).
- Off D, X′ = B′ = W. On G₂, Y = C differs from W = B′ =: n, and Y must be weakly w-worse than W, hence strictly worse pointwise, since distinct advice values have distinct ranks; this is (c).
- Off D ∪ S, Y = B′ = X′.
- "Strictly worse somewhere" is (d).

Conversely, given (a)–(d), choose W := n on G₂ and W := C off D ∪ G₂, and Y := C on S and Y := B′ elsewhere. ∎

CHECKED: on all H-instances with n ≤ 4 atoms, all odd-world patterns, every strict-(G)-admissible pair (B, X) and every C, the brute-force closure (every copy, every Y) equals the formula: 342,576 source/world checks, 0 mismatches.

**Corollary 1.2 (PROVED; CHECKED).** Suppose B, X and C give no contradictory advice.
- (i) No single accepted record forces C ⋠_w Z at all three worlds for the same Z. So a full-support source is never left without a defence by one acceptance.
- (ii) If one accepted record forces refusal of the same Z at both worlds i and j, then G₂ and D ∖ G₁ consist of odd-k points ({i, j, k} = {1, 2, 3}). So a source whose support is {i, j} can be exhausted by one acceptance, but only through odd-k material.

*Proof.* (i) The same Z fixes S, G₁, G₂ and n. At a point with no contradictory value, no value is weakly better at all three worlds than a different one: h, −h and S are pairwise mixed at mixed-sign g, and coherent models are correct at unanimous-sign g. So (c) at three worlds forces G₂ = ∅, and (b) forces B = X on D ∖ G₁, so D ∖ G₁ = ∅. Then (a) gives C = X on G₁, and (d) fails. (ii) At a point whose odd world is i or j, two values are never ordered the same way at both i and j. CHECKED: 0 counterexamples among 56,298 two-world refusals. ∎

### 1.2 Generalised agreement obstruction (axiom-level)

**Lemma 1.3 (PROVED).** Let B ⪯_w X at every w, with D := {B ≠ X} not a.e. a cone. Let N be protected (undominated, with direct (C)) and coherent. Then N ≠ X on a non-null part of D.

*Proof.* Suppose N = X a.e. on D. Then rec(B → X) = rec(N[D ↦ B] → N), so by (IB) N[D ↦ B] ⪯_w N at every w. Protection gives every reverse, so N and N[D ↦ B] tie at all worlds. By direct (C), N[D ↦ B] is coherent. But it differs from the coherent N exactly on D, because N = X ≠ B there, and two coherent models differ on a conic set. ∎

PP73 Lemma 2.4 is the case N = source. Lemma 1.3 applies to **every** protected model at once, including T, the rescalings and earlier defenders.

### 1.3 The H formula

**Corollary 1.4 (PROVED; CHECKED, `check_exh76.out`).** Let X, B and the protected N all lie in H, with D non-conic. Put

  U_N := {B = N ≠ X} (N's *correction set*),  L_N := {B ≠ N = X} (B's layer relative to N).

Then:
- (i) U_N is non-null (Lemma 1.3, using two states: N ≠ X and B ≠ X force B = N).
- (ii) N is forced to refuse some rival at world w **iff** U_N ⊆ Up_w(N) a.e. The forced rivals at w are exactly

  𝒵_w(N; B, X) = {N ⊕ G : G ∩ U_N = ∅, L_N ∩ Up_w(N) ⊆ G, G ∩ Down_w(N) ⊆ L_N}.

  N ⋠_w B itself is forced iff X is strictly w-better than N.
- (iii) The refusal worlds are W_N(B, X) = ess-⋂_{g∈U_N} Up_N(g), a proper subset of {1, 2, 3} (possibly empty).
- (iv) **Rigidity at the source.** If X = N ⊕ E, then U_N ⊆ E, so W_N ⊇ ⋂_{g∈E} Up_N(g). If E is pure, then W_N = Up(E) for **every** dominator B. This holds for arbitrarily small E, and for E nested in or overlapping earlier fills.
- (v) For a source M with {X ≠ M} large (another rescaling, or an earlier defender), W_M depends on B only through where B agrees with M on D. The dominator controls it completely by choosing U_M.

*Proof.* Theorem 1.1 with two states. On G₁ ⊆ {N ≠ B}, condition (a) forces X = N (if X ≠ N then B = N). On U_N, B = N, so (b) requires U_N ⊆ G₁, which contradicts G₁ ⊆ {N ≠ B} unless B is not w-better than X on U_N, i.e. U_N ⊆ Up_w(N). On L_N, B = flip(N) is w-better than X = N exactly on Up_w(N), and (b) puts those points in G. (c) with two states says G ∖ L_N ⊆ Up_w(N). (d) holds because U_N is non-null and N = B is strictly w-worse than X there. CHECKED: refusal worlds equal the formula in every case with U_N ≠ ∅, for n = 4, all odd-world patterns, all admissible pairs. ∎

So the choice of dominator determines **which correction set** each committed source sees. Mixing two types with disjoint Up-sets inside U_N removes every first-generation refusal at N. Pure fills are the irreducible case: an (o,1)-fill forces N ⋠_i B for i ≠ o, and then defence forces N ⪯_o B (the forced pattern). An (o,0)-fill forces N ⋠_o B.

### 1.4 Sections do not transport a single acceptance's refusals

**Proposition 1.5 (PROVED).** Let r be accepted, Z a fixed rival, and C_{q_n} → C_p a.e. selected sources. Suppose r forces C_{q_n} ⋠_i Z and C_{q_n} ⋠_j Z for all n, so that defence and closed sections give C_p ⪯_k Z. Then r does **not** force C_p ⋠_k Z. The same holds with the two refusals at the q_n coming from r at different n.

*Proof.* Advice values are discrete, so a.e. g has C_{q_n}(g) = C_p(g) for all large n. Conditions (a)–(c) of Theorem 1.1 are pointwise, so they hold at p for worlds i and j, in their weak form, with the same G. If r also forced refusal at k at p, then (a)–(c) would hold at all three worlds at p. The proof of Cor 1.2(i) then shows that (d) fails at k. ∎

So the configuration "refused at two worlds along a sequence and at the third world at the limit" needs **at least two** acceptances.

### 1.5 Exhaustion needs several acceptances: exact criterion

**Proposition 1.6 (PROVED; CHECKED).** Let d₁, …, d_m be accepted H-records with non-null correction sets U_ℓ ⊆ R at T, layers L_ℓ and refusal worlds W_ℓ (Cor 1.4). T has no defence against some rival **iff** there is an assignment σ : {1, 2, 3} → {1, …, m} with i ∈ W_{σ(i)} for which

  G₀ := ⋃_i (L_{σ(i)} ∩ Up_i(T))  satisfies  G₀ ∩ U_{σ(i)} = ∅  and  G₀ ∩ Down_i(T) ⊆ L_{σ(i)}  for every i.

The unprotected rival is then T ⊕ G₀.

*Proof.* By Cor 1.4(ii), the lower bounds on G are the sets L_{σ(i)} ∩ Up_i, and every other constraint is downward closed. So a G exists iff the least candidate G₀ works. ∎

CHECKED: 24,300 random pairs of admissible acceptances (n = 4, all odd-world patterns). 24 exhaust T, and the criterion agrees with brute force in every case.

**Example 1.7 (common layer; PROVED).** Let X₁ = T ⊕ E₁ be an (o,0)-fill and X₂ = T ⊕ E₂ an (o,1)-fill, with dominators B₁, B₂ whose layers relative to T coincide: L₁ = L₂ = L, with L ∩ (U₁ ∪ U₂) = ∅. Take σ(o) = 1 and σ(i) = σ(j) = 2. Then G₀ = L satisfies Prop 1.6, so **T has no defence against T ⊕ L**.

The audit's pigeonhole (one dominator serving two classes) is the special case of a shared dominator. The general rule is that dominators of complementary pure fills must not share layers in the sense of Prop 1.6.

### 1.6 The second generation and "works twice"

Theorem 1.1 holds for **every** accepted record, not only dominations. In particular, after an (o,1)-fill domination the forced defence T ⪯_o B generates refusals at every carrier:
- every Y strictly o-worse than B refuses T at o;
- at B itself, B ⋠_o B ⊕ G for every G ⊇ P := {g ∈ {T ≠ B} : T is o-better than B} with G ∖ {T ≠ B} ⊆ Up_o(B).

Now dominate B's own (o,1)-fill X′ = B ⊕ E′ by some B′, with layer L′ relative to B. Then the refusals of the same rival at world o (from T ⪯_o B) and at worlds i, j (from the domination of X′) are given exactly by Theorem 1.1 at B.

**Necessary condition (PROVED; CHECKED necessary, not sufficient).** B can be left without a defence only if:
- L′ ⊇ P; and
- L′ ∖ {T ≠ B} contains no points of the types (i,0), (j,0) or (o,1) relative to B.

The proof: the o-refusal needs G ⊇ P. The i- and j-refusals need G ∩ (Down_i ∪ Down_j)(B) ⊆ L′, and P misses the (o,1)-type.

CHECKED (`check_gen2_76.out`; n = 4, all odd-world patterns, every admissible T, E′ and B′ with non-null correction set): 1,860 configurations. In 438 of them B is left without a defence, and the condition holds in all 438. It holds in 636 configurations in all, so the strictness clause (d) and the condition G ∩ U′ = ∅ also matter.

So **a second-generation dominator that moves back toward T across all of P is the only way the forced defence and B's own repair can jointly kill B's defence.** This is the concrete content of "works twice" at the first two generations. It is a constraint on the choice of B′.

### 1.7 Answer to Task 1

- **Which sources refuse, and where:** Cor 1.4. The correction set U_N decides everything, and Lemma 1.3 makes it non-null at every protected N.
- **When defence is exhausted:** never by one acceptance (Cor 1.2), never through sections from one acceptance (Prop 1.5), and exactly under Prop 1.6 for several.
- **Axiom-level obstruction:** none is derivable from the coupled-refusal layer, for any single acceptance or any limit of one. Every exhaustion found needs a coincidence among chosen dominators (Example 1.7, §1.6).

I could not prove that the coincidences are always avoidable. Avoiding them requires changing the dominator's layer, and the dominator must be coherent and must dominate. So the full question remains **OPEN**.

An axiom-level obstruction would have to combine at least two acceptances, at least one of them *generated* (a defence forced by two refusals, or a section limit). §2 shows that this is exactly the configuration in which generation-based invariants fail.

---

## 2. Task 2: section closure followed by copying

**Lemma 2.2 (transfer; PROVED, axiom-level).** Let ρ be a record carried by selected sources C_a and C_c. Suppose c_m → c in the family with C_{c_m} ⪯_w C_c ⊕ ρ. Then C_a ⪯_w C_a ⊕ ρ.

*Proof.* The closed section at c for the fixed rival C_c ⊕ ρ gives C_c ⪯_w C_c ⊕ ρ. Its record is ρ. Apply (IB). ∎

Consequently Acc_w(ρ) at a source is **not** determined by that source's own sections. An invariant stated as "a record of kind K is accepted at w only if it was generated by …" must be checked at every carrier of every record.

**Proposition 2.1 (PP72 Theorem 6.2 is false; PROVED, NUMERICS `cex76.out`).** In PP72's 𝓡_θ (and the draft 𝓡(𝒟₀)), with priority 2 ≻ 3 ≻ 1, put:
- N := C_{sδ₃ + tδ₁} ∈ 𝓘 with s = 2t, so log N = (0, 3t, −3t) and world 1 is strictly middle;
- a := σ(−1, 2, −1) ∈ R₂ with 0 < σ < t;
- F := F⁺ ∪ F⁻, where F⁺ and F⁻ are radial slabs of equal |g|-mass in the odd-1 parts of L(u, N) ∖ L(u, a) on which N improves, respectively worsens, world 1;
- X := C_a[F ↦ N].

Then rec(C_a → X) is u¹-null and accepted at all three worlds, so the incoherent N[F ↦ C_a] is weakly no worse than the installed N at every world.

*Proof.*
- **The geometry.** Along R₂, advice changes at most once (single-coordinate shift), so the layers are nested and F ∩ L(u, a) = ∅. Both signs occur at odd-1 points of L(u, N): at Cor = {1} points, q_v(N) − q_v(u) = −(e^{3t} − 1)v₂|h₂| + (1 − e^{−3t})v₃|h₃|, which is positive near T's boundary where |h₃| ≫ |h₂|, and negative at the (2 3)-mirror points. The negative part lies outside L(u, a) once σ < t, since L(u, a) needs q_v(u) < (e^{3σ} − 1)v₂|h₂|.
- **World 2.** 𝒟₀ at a, since the record is null.
- **World 3.** The inward section at a: V(C_{a_n} → X) = Γ(a, a_n) = (y, −2y, y) exactly, a (1, 3) tie resolved to 3.
- **World 1.** T carries ρ_n := rec(C_{a_n} → X), because C_{a_n} = T on L(a_n, a) ∪ F. For c_m ∈ R₃ with c_m → u,

  V(C_{c_m} → T ⊕ ρ_n) = (y + z, z − 2y, y − 2z),

  which has a strict maximum at world 1. Lemma 2.2 at c = u gives C_{a_n} ⪯₁ X, and the section at a gives C_a ⪯₁ X.
- **The copy.** rec(N[F ↦ C_a] → N) = rec(C_a → X). ∎

NUMERICS (N = 4·10⁶; t = 0.04, σ = 0.01): zero −h answers; zero nesting violations; odd-1 both-sign masses 5.5·10⁻³ and 4.2·10⁻³; |V(F)| ≤ 3.6·10⁻⁷; T carries ρ_n exactly on the sample; argmax at world 1 in all nine (n, m) cases.

**Status of the repair.** Under REFEREE_round58's 𝒟₀^κ, the world-1 margin is V₁ − max(V₂, V₃) = 3z, and 3z/|V|_∞ → 0 as z → 0. So no κ-acceptance occurs near the limit, and the transfer chain is cut. I tried the other carriers available on 𝔽: R₂ carriers approached inward, R₃ carriers approached from inside, and u approached along R₂. All produce Γ-type perturbations of a Γ-vector, and so lie outside K^κ near the limit. **I found no break of invariant (J).**

**Test for any new generator (used in §3).** Is the class of records it accepts at each world record-intrinsic, and closed under fixed-rival limits at every carrier? If it is not, look for a carrier whose own section reaches the record from a direction the generator favours.

---

## 3. Task 3: attack on PP74's operation ASR (as posted in its DRAFT)

ASR, in brief:
- install d = rec(B → X) at all three worlds;
- refuse d⁻¹ at all three worlds (R0) and the coupled refusals (R1);
- defend each affected C by **weak guidance at an anchor world v** ("no new acceptance is made");
- admissibility conditions (U1)–(U4);
- among admissible defenders, minimise the affected pairs.

### 3.1 Zero-sum: ASR is genuinely outside the obstruction, and pays for it with route (U)

**Proposition 3.1 (escape taxonomy for H-domination; PROVED).** Let ψ be any additive field for which every H-model minimises Σ_wΦ^ψ_w. This covers u¹, and every field with the same λ-sums (REFEREE_round58 §3). If B ⪯_w X at every w and X ∈ H, then one of two things holds:
- **(U)** some world has V^ψ_w(d) < 0, so d is an unfavourable acceptance; or
- **(N)** V^ψ(d) = 0, and strictness needs the ψ-null d⁻¹ refused somewhere while d is accepted everywhere.

*Proof.* ΣV^ψ(d) = ΣΦ^ψ(X) − ΣΦ^ψ(B) ≤ 0. If no coordinate is negative, all vanish. ∎

**ASR's acceptance pattern** on d (Acc(d) = {1, 2, 3}, Acc(d⁻¹) = ∅) is **not** of the form "accept iff v_w ≥ 0" for any zero-sum antisymmetric v, linear or not, nor lexicographic (PROVED). Such a v would satisfy v(d) ≥ 0 and −v(d) = v(d⁻¹) < 0, so Σ_w v_w(d) > 0. So the audit's question is answered: **no, not on domination records.**

But the draft says nothing about verdicts on **non-designated** records: defences of committed models against unaffected rivals, and the closure. Those are where a hidden score could sit, and they are what §§3.2–3.3 show cannot be avoided.

### 3.2 Item 4 is false: extended rivals need new, non-guidance acceptances

PP74's item 4 treats only the refused rivals C[S ↦ B]. Theorem 1.1 shows that the coupled rule, applied to **all copies** as (R1) itself requires, also refuses the *extended rivals* C[G₁ ↦ B][G₂ ↦ n]. Here G₂ lies off D, and n is any pointwise strict w-improvement of C. These come from the copies whose context W equals n on G₂.

**Proposition 3.2 (PROVED; CHECKED, `check_anchor76.out`).** In H, let C be affected at w (U_C ⊆ Up_w(C)), and let {w, v, v′} = {1, 2, 3}. Choose G₂ ⊆ Up_w(C) ∖ D containing non-null sets of two types:
- (v′,1), i.e. flips that improve w and v;
- (v,1), i.e. flips that improve w and v′.

Then W := C ⊕ (L_C ∪ G₂) is refused at w by (R1), and it is weakly worse than C at neither v nor v′. So C's defence against W is **not** guidance at any world: a new, non-guidance acceptance C ⪯_v W or C ⪯_{v′} W is forced by the axioms (defence).

*Proof.* Cor 1.4(ii) with G = L_C ∪ G₂. On G₂ the flip improves v at the (v′,1) points and v′ at the (v,1) points. ∎

CHECKED (n = 4, three source states, all odd-world patterns, every admissible d with an anchored affected C): 7,236 affected pairs (C, w). In 2,220 of them some refused rival has **no guidance defence at any open world**. Every one of the 2,220 is an extended rival: none has the form C[S ↦ B].

**No defeat at first order (CHECKED, `check_gen2b_76.out`).** For each of the 2,220 forced acceptances and each open world x, I computed the first-generation refusals of d and of the new acceptance together, plus strict guidance. In no case did every choice of x leave C or B (both committed) without a defence. Moreover, single-domination defeat is decided by the restricted family C[S ↦ B] (`check_defeat76.out`: 666 defeats among 16,212 dominations, none missed). So **Theorem C of PP75 is complete for defeat, but not for defence options.**

**Consequence.** "Nothing else is newly accepted" is false. ASR must output a world, and a record-intrinsic closed acceptance class, for these forced defences. By REFEREE_round58 §6 and Lemma 2.2, each such class must also survive section-then-copy.

### 3.3 The refusal class is not open; anchors fail at neighbours

PP74 says every refusal class is open in record topology. The (R1) class is defined by a **weak pointwise inequality** ("Y′ weakly w-worse than X′ a.e."), which is a closed condition. Perturb Y′ on small sets where it becomes w-better: the perturbed records converge to a refused record but lie outside (R1). So the openness needed for sections must come from reservations, not from (R1).

The refusals at neighbours are nonetheless **forced by the axioms**. If C_{q_n} ⪯_w Z along q_n → a, the closed section gives C_a ⪯_w Z, which contradicts C_a's forced refusal.

**Proposition 3.3 (anchors fail at neighbours on PP72's family; PROVED, NUMERICS `anchor_num76.out`).** Let B = C_{τδ₃} dominate a class-3 fill of T. Then:
- T ⋠₁ B and T ⋠₂ B are forced, and the anchor is world 3 (T ⪯₃ B by guidance).
- For q = s(−1, 2, −1) ∈ R₂ with s small, sections force C_q ⋠₁ B and C_q ⋠₂ B. So C_q ⪯₃ B is forced.
- But B is strictly 3-better than C_q on a non-null set, so this acceptance is **not guidance**.

On the R₃ side (q = sδ₃, s < τ) guidance does hold.

*Proof.*
- Take Cor = {2} points (h₂ > 0 > h₁, h₃) near T's boundary with |h₃| ≪ h₂. Such boundary points exist, because there the boundary is v₂h₂ = v₁|h₁| + v₃|h₃| with |h₃| → 0.
- The R₂ move adds (e^{3s} − 1)v₂h₂ to every vertex form and gains h there.
- B's move adds only (1 − e^{−3τ})v₃|h₃|. So B = T stays silent on the open cone where |h₃| < κ(s/τ)h₂.
- Answering h is wrong at world 3 there, so B is strictly 3-better than C_q. ∎

NUMERICS: τ = 0.03. The |g|-mass where B is strictly 3-better than C_q is 1.1·10⁻³, 4.0·10⁻⁵ and 2.5·10⁻⁶ at s = 0.01, 0.002 and 0.0005 on R₂; it is 0 on R₃.

**Consequence.** On any committed family that is non-isolated in a direction which does not improve the anchor world pointwise, ASR's item 4 fails at a punctured neighbourhood of every affected source. The missing defences are **generated** acceptances with a section structure: this is exactly the configuration of Prop 2.1. ASR must state their acceptance class and prove it closed and record-intrinsic.

### 3.4 Second application: two missing admissibility clauses

When ASR is applied a second time (rival X₂, new defender B₂), the draft checks (U1)–(U4) only for the **new** record d₂. Two axiom-level requirements concern the **old** records:
- **(U1′)** B₂ must not carry any earlier d⁻¹. If it did, then B₂ = X on D for an earlier domination, and Lemma 1.3 gives an incoherent all-world tie partner of the committed B₂.
- **(U2′)** B₂ must not be defeated by an earlier domination's refusals. This is Theorem C (PP75) at Z = B₂.

CHECKED (`check_defeat76.out`): defeat of a source with a non-null correction set occurs in 666 of 16,212 admissible single dominations. So (U2′) is a live condition for the new defender, not a formality.

In addition, **(U3) must be a permanent invariant.** Suppose any later acceptance completes X′ ⪯_w Y ⪯_w B′ around a copy (B′, X′) of an earlier d. Then (TC) installs the reverse X′ ⪯_w B′, which is a copy of d⁻¹ and contradicts (R0). This applies to the forced acceptances of §§3.2–3.3 and to every later domination record.

### 3.5 Defence exhaustion and (TC) cascades

ASR minimises affected pairs **per rival**. By Prop 1.6 and PP75 Thm 4.3 (138 of 1,974 grid pairs), two individually admissible dominations can jointly leave T without a defence. Example 1.7 gives a common-layer instance.

An adaptive adversary installs an (o,0)-fill domination first. Then the next rival is an (o,1)-fill of T: every dominator whose layer satisfies Prop 1.6 with the first is excluded. ASR survives only if it adds Prop 1.6 to admissibility. That is a choice-level repair, but **as drafted ASR does not check it.**

The (TC) cascade of an unfavourable d (route (U)) is PP62's Lemma S. Every split X → Z → B of d with both links accepted at w would install a copy of d⁻¹ at w, contradicting (R0). So (R0) turns Lemma S into **forced refusals** of one link of every split, at every world. These refusals are carried by committed models only through Theorem 1.1, and so are already counted in (R1). No further obstruction was found.

### 3.6 Balanced swaps (Theorems Q and E)

- **Hypotheses.** ASR satisfies neither (L0⁺) nor u¹-endorsement, since it accepts d at unfavourable worlds. So Theorems Q and E do not apply as stated.
- **What still applies.** The axiom-level parts of PP62 Cor E.2(i) do apply. They use only (IB), defence, direct (C) and closed sections. So on a committed family that is two-dimensional at an interior source a with a balanced partner, the refusing world w spreads, and the neighbours in O_w directions must accept at a u¹-unfavourable world.
- **Consequence.** This is a third class of **forced generated acceptances** missing from ASR's "nothing else is newly accepted". With §§3.2–3.3 it shows that ASR's acceptance set cannot consist of guidance plus domination records alone. Any defence rule PP74 adds must pass the copied-limit balanced-swap test of Prop 2.1, not only PP73's (ρ1)–(ρ3).

### 3.7 The j-ideal models X\*_j (coordinator relay; PROVED)

PP75 Prop 9.1: X\*_j is pointwise j-better than every H-model. So for any dominator B of X\*_j (which must lie outside H):
- **every committed H-model C refuses B at j** (coupled rule with Y = C);
- by Theorem 1.1, C also refuses the copies C[G₁ ↦ B][G₂ ↦ n] at j, for every G₁ ⊇ P_j := {g ∈ D : B strictly j-better than X\*_j} with G₁ ⊆ D ∩ {C ≠ B}.

Consequences:
- **(a) Pigeonhole (axiom-level).** If one coherent B dominates X\*_1, X\*_2 and X\*_3, every committed H-model is left without a defence against B. Dominating two of them with one B forces C ⪯_k B at the third world k, for every committed C ∈ H.
- **(b) Three distinct dominators B_j.** They can jointly leave T without a defence only if each improvement region P_j(B_j) lies a.e. in ⋃_{i≠j} D_i.

  *Proof of (b).* At g ∈ P₁ ∖ (D₂ ∪ D₃), the common rival would equal B₁(g). That value is strictly 1-better than X\*₁(g), hence strictly 1-better than T(g). It would also have to be strictly 2- and 3-better than T(g), from the G₂ clauses of the other two refusals. So it would be better at all three worlds, which is impossible for a non-contradictory T(g). ∎

  So choosing dominators whose improvement regions avoid the other dominators' difference sets prevents joint defeat, at every scale. This is choice-level.

---

## 4. Level of each finding

| Finding | Axiom-level? | Every clause derived from axioms? |
|---|---|---|
| Thm 1.1, Cor 1.2, Lemma 1.3, Cor 1.4, Prop 1.5 | yes (descriptions and constraints) | yes |
| Exhaustion needs ≥ 2 acceptances; criterion Prop 1.6 | constraint on choices | yes, given the installed acceptances |
| Example 1.7, §1.6, joint defeat | choice-level | yes, given the choices |
| PP72 Thm 6.2 false (Prop 2.1) | no: refutes a rule | rule plus geometry |
| ASR item 4 false (Props 3.2, 3.3); refusal class not open | forced acceptances are axiom-level once d is installed | yes |
| (U1′), (U2′), (U3) as invariant | axiom-level necessary conditions | yes |
| X\*_j pigeonhole (3.7a) | yes | yes |
| An obstruction to dominating all incoherent H-models with T defended and sections closed | **not found; OPEN** | — |

**Where an obstruction, if any, must live** (Props 1.5, 3.2 and 3.3). It must involve at least two acceptances, one of them generated: a forced defence (§3.2), a neighbour's forced defence (§3.3) or a Cor E.2 acceptance (§3.6). These must be combined through section limits and copies (Lemma 2.2). The next adversarial computation should be a SAT run on a cell sub-universe containing u, a short R₂ segment, one class-3 domination, the extended rivals of §3.2 and the neighbour defences of §3.3. Every clause would be an axiom instance, and the defences would be left free.

---

## 5. Scripts (`r9/PP76_py/`; run `python3 -I -B <script>.py` inside the folder; output in `<script>.out`)

| Script | Content | Label |
|---|---|---|
| `hlib76.py` | exact two-state H model: atoms, odd worlds, records, copies, coupled refusals | library |
| `check_t1_76.py` | Thm 1.1 vs brute force (342,576 checks, 0 mismatches); Cor 1.2 | CHECKED |
| `check_exh76.py` | Cor 1.4 refusal worlds; Prop 1.6 criterion (24,300 pairs, 24 exhaustions, 0 mismatches) | CHECKED |
| `check_gen2_76.py` | §1.6 necessary condition (438 exhaustions, all satisfy it; 636 satisfy it) | CHECKED |
| `check_defeat76.py` | single-domination defeat: restricted family complete (666/16,212) | CHECKED |
| `check_anchor76.py` | Prop 3.2: 2,220 refused extended rivals with no guidance defence | CHECKED |
| `check_gen2b_76.py` | forced new acceptances never defeat C or B at first order (0/2,220) | CHECKED |
| `cex76.py` | Prop 2.1 counterexample to PP72 Thm 6.2 | NUMERICS |
| `anchor_num76.py` | Prop 3.3: anchor guidance fails at R₂ neighbours of u | NUMERICS |
| `lib73copy.py` | copy of PP73's library | library |
