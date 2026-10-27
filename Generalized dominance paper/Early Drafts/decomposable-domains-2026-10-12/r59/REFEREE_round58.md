# REFEREE_round58. Referee report on PP72 and PP73 (round 58), the audit's H argument and zero-sum obstruction, and the rescaling inequalities

24 October 2026. Independent referee for round 59. I read BRIEF59_H_repair, BRIEF58_rescaling_loop, AUDIT_round59 (with its answers and the rescaling note), DESIGN_MEMO §8.27 and its correction bullets, LEAD_selection_count §1, AUDIT_completion (rules I–IV), PP56 §4, PP57 §4, PP62 §§1–4, PP66 §§1–3, and PP72 and PP73 in full.

**Labels.**
- PROVED: I checked the argument, or I give one here.
- CHECKED: exact computation.
- NUMERICS: Monte Carlo on an S₃-symmetrised Gaussian sample, in `r9/REFEREE58_py/`. None of the authors' scripts is imported. The sample is closed under all coordinate permutations, so the exact (1 2) and (1 3) ties hold to rounding.

**What I re-implemented.**
- **`lib58.py`.** The posterior models, from the vertex inequalities, and u¹ on H-records.
- **`cex58.py`.** The counterexample of §1.3.
- **`check58.py`, `prop41b58.py`.** Checks of:
  - the rescaling inequalities and composition;
  - PP73 Cor 1.3, Thm 2.3, Prop 4.1 and Lemma 4.7;
  - PP72 Lemma 6.0, the (D3′) ledger and Prop 4.2.
- **PP72's SAT runs E0′ and E1L.** I re-ran these with the authors' own code; outputs are in `rerun_*.out`. I also re-derived the E0 core by hand.

**Verdict scale:** correct / correct with repair / wrong.

---

## 0. Verdicts at a glance

| Item | Verdict | Short reason |
|---|---|---|
| PP72 Thm 6.2, steps 1, 2, 4–7 | correct, given step 3 | endorsement invariant and closure bookkeeping are sound |
| **PP72 Thm 6.2, step 3, and hence the theorem** | **wrong as stated; correct with repair** | **Section closure followed by copying puts a u¹-null record at world 1 (explicit counterexample, §1.3). With it an installed defender is weakly dominated by an incoherent splice. Repair: a margin rule at world 1 (§1.4), after which an intrinsic invariant survives every operation, copying included.** |
| PP72 Lemma 6.0 | correct with a stated hypothesis | needs u¹ built on an S₃-symmetric (2V) reference family |
| PP72 Prop 2.1 (a)–(c), (f); tie rule 2 ≻ 3 ≻ 1 meets (ρ1)–(ρ3) | correct | (a)–(c) describe the worlds forced by a record's *own* section |
| PP72 Prop 2.1 (d) ("no balanced record out of 𝔽 accepted at all three worlds") | **wrong** for 𝓡(𝒟₀) and 𝓡_θ; true after the repair | §1.3 |
| PP72 Prop 2.1 (e) | not established for 𝓡_θ; PROVED after the repair | refusals in a least fixed point need an invariant |
| PP73 (ρ1)–(ρ3) | necessary: correct. "Also sufficient": **wrong** | §1.3 satisfies them and still fails |
| PP72 Prop 3.1 | correct | |
| PP72 Prop 3.2 | correct with repair (of the proof) | "B is λ-Bayes" needs B ∈ H; the conclusion holds for every B, by minimality of X |
| PP72 Props 3.3, 3.5; Cor 3.4 | correct | certificate-level; Cor 3.4's "sheet" is a reading |
| PP72 Prop 4.1 | correct for the forced refusals and their defences; "compatible with sections" unproved | same section-then-copy gap |
| PP72 Prop 4.2, (D3′), Cor 6.3 | correct (NUMERICS agree), Cor 6.3 given the repaired Thm 6.2 | the h-points on common silence count as "f" (§1.7) |
| PP72 SAT runs | correct as finite statements; reproduced (E0′, E1L) | they impose **neither** 𝒟₀ **nor any section clause** and use no u¹ data |
| Audit's H argument | correct, with the exact H stated | H is relative to the reference family 𝒮; fills off R(𝒮) are not in H |
| Audit's zero-sum obstruction | correct | literal "iff v_i ≥ 0" rules; it escapes only by asymmetric tie-breaking of null records |
| PP66 on H-records | falls under it; dominates no H-model at all | §3 |
| PP73 Cor 1.3 (one loop, no balanced swaps) | correct; (2V) not even needed | |
| PP73 Thm 2.3 (fill–splice identity), Lemma 2.4 | correct (NUMERICS: 100% at a = 1.03, 1.10) | |
| PP73 Props 3.2–3.5 (two branches) | correct | |
| PP73 Prop 4.1 | correct | for a′ > a the both-sign world is 3, not 2 |
| PP73 Props 4.3, 4.6, 4.8; Thm 4.4; Table 4.5 | correct | 4.3's numerics are unnecessary under symmetry |
| PP73 Lemma 4.7 | correct; its NUMERICS bullet over-attributes gaps to noise | asymmetric rows are real (§4) |
| Rescaling inequalities; composition | correct (PROVED; NUMERICS 0 disagreements) | linear in m, not in log m; μ and \|g\| are not transported |

---

## 1. PP72

### 1.1 An implicit hypothesis

Lemma 6.0 relies on the exact identities Φ₁ = Φ₂ on R₃ and Φ₁ = Φ₃ on R₂. These need the field u¹ itself to be (1 2)- and (1 3)-invariant. u¹ depends on its reference family 𝒮 through R(𝒮) and the common advice off R(𝒮). The installed set 𝓘 is not S₃-symmetric: (1 3) sends R₃ to the δ₁-ray. So the reference family must be chosen symmetric, for example PP62's 𝒮₀ = {a : normalise(1/a) ≥ c + η}.

**Hypothesis (Sym):** u¹ is PP56's field for an S₃-symmetric (2V) family 𝒮 ⊇ 𝓘.

Everything below assumes (Sym). Without it Lemma 6.0(b), Prop 2.1 and the tie analysis all lose their proofs.

### 1.2 Steps 1, 2 and 4–7 of Theorem 6.2: correct, given step 3

- **Step 1 (every acceptance has V_w ≥ 0).** This is correct for every generator and every closure operation. Two points are needed:
  - for installed C, ΣV(rec(C → X)) ≥ 0;
  - V is continuous along fixed-rival sections, because a ↦ Φ(C_a) is continuous.
- **Steps 2 and 4.** Correct.
- **Steps 5–6 and rules III–IV.** Each reduces to "no non-trivial u¹-null record is accepted at world 1". Write X ⪯_w N for every w with N installed. Then V(rec(X → N)) ≥ 0 and its sum is ≤ 0, so the record is null.
- **Step 7.** Holds by construction.

So the theorem stands or falls with step 3.

### 1.3 Step 3 fails: section closure followed by copying (PROVED; NUMERICS illustration)

The audit's concern is justified, and it is not only a gap: there is a counterexample. The last bullet of step 3 assumes that a world-1 acceptance of rec(C_{a_n} → X) produced by a section limit is a limit along **X's own** section. It can instead be the limit along another rival's section at another source, transported to (C_{a_n}, X) by (IB).

**Proposition R1 (PROVED, under (Sym)).** Make the following choices.
- A defender c = sδ₃ + tδ₁ ∈ 𝓘 with s ≠ t. Then log c has a strictly middle coordinate m; for s = 2t, m = 1.
- A point a = s_a(−1, 2, −1) ∈ R₂ with s_a > 0 so small that the odd-m part of L(u, c) ∖ L(u, a) contains non-null sets on which C_c improves world m and on which it worsens world m. Here L(u, ·) := {T ≠ C_·}. Such an s_a exists because μ(L(u, a)) → 0 while both parts of L(u, c) are non-null (PP62 Cor 1.2 and the Prop 4.1 argument).
- A non-conic F inside that part with c_m(F) = 0, so that V(F : T → C_c) = 0.

Put X := C_a[F ↦ C_c] and Y′ := C_c[F ↦ T]. Then in 𝓡_θ (and in the draft 𝓡(𝒟₀)), r := rec(C_a → X) is u¹-null and is accepted at **all three worlds**. Since r = rec(Y′ → C_c), the incoherent Y′ is no worse than the installed defender C_c at every world.

This contradicts Theorem 6.2's protection, undominatedness and direct (C). Rules III–IV then register Y′, which is failure F2.

*Proof.*

0. **Monotonicity along R₂.** Index s(−1, 2, −1) is proportional to (1, e^{3s}, 1). For every vertex α, the quantity Σ_i m_i v^α_i g_i equals v^α₁g₁ + e^{3s}v^α₂g₂ + v^α₃g₃, which is monotone in s with the sign of g₂ for all three α. So under (2V) each g changes its advice at most once along R₂. Hence, for 0 < s_n < s_a:
   - L(u, a_n) ⊆ L(u, a);
   - C_{a_n} = C_a on L(u, a_n);
   - C_{a_n} = T off L(u, a_n).

   On F we have C_a = T, because F ∩ L(u, a) = ∅. So V(C_a → X) = V(F : T → C_c) = 0.
1. **World 2.** V(C_a → X) = 0, so 𝒟₀(C_a, X) = 2 by the priority 2 ≻ 3 ≻ 1.
2. **World 3.** Take a_n ↑ a along R₂. Then V(C_{a_n} → X) = Γ(a, a_n) = (q_n, −2q_n, q_n) with q_n > 0, exactly, by (1 3)-symmetry and ΣΦ = const. This is a tie between worlds 1 and 3, so 𝒟₀ = 3. The closed section at a gives C_a ⪯₃ X.
3. **World 1.** This takes four moves.
   - **The copy.** Fix n and put F_n := {C_{a_n} ≠ X}. On L(u, a_n), X = C_a = C_{a_n}; off L(u, a_n), C_{a_n} = T. So **C_{a_n} = T on F_n**. Put Y_n := T[F_n ↦ X]. Then rec(T → Y_n) = rec(C_{a_n} → X) =: r_n, with the same support, the same old values and the same new values.
   - **The defence at R₃ points.** Take b_j = s_jδ₃ ∈ R₃ with s_j → 0. Then
     V(C_{b_j} → Y_n) = V(r_n) + Γ(u, b_j) = (q_n + p_j, −2q_n + p_j, q_n − 2p_j),  with p_j > 0.
     So V₁ − V₂ = 3q_n > 0 and V₁ − V₃ = 3p_j > 0: a **strict** maximum at world 1. 𝒟₀ installs C_{b_j} ⪯₁ Y_n.
   - **The first section limit.** The section at u for the rival Y_n gives T ⪯₁ Y_n. Its record is r_n, so C_{a_n} ⪯₁ X by (IB), for every n.
   - **The second section limit.** The section at a for the rival X gives C_a ⪯₁ X.
4. **The dominated defender.** r = (F : T → C_c) = rec(Y′ → C_c), so Y′ ⪯_w C_c at w = 1, 2, 3. Y′ differs from the coherent C_c on the non-conic F, so it is incoherent. ∎

**NUMERICS (`cex58.out`; N = 2.4·10⁶; s_c = 0.06, t_c = 0.03, s_a = 0.02).**
- (2V) holds for every index used.
- Both-sign odd-1 masses in L(u, c) ∖ L(u, a) are 0.00247 and 0.00046. F has mass 0.00091, and V(C_a → X) ≈ 10⁻⁷.
- For n = 1, …, 5 the copy identity holds exactly on the sample, and V(C_{a_n} → X) = Γ(a, a_n) has the shape (q, −2q, q). For example, at n = 1 it is (0.00922, −0.01843, 0.00922).
- For every j, V(C_{b_j} → Y_n) has a strict maximum at world 1, with V₁ − V₂ = 3q_n and V₁ − V₃ = 3p_j.

**Where PP72's proof breaks.** Step 3's "𝒟₀: impossible" bullet concerns 𝒟₀ at (C_{a_n}, X). The world-1 acceptance here comes from 𝒟₀ at a different pair, (C_{b_j}, Y_n), whose V is not a Γ-vector. The "section limit" bullet then treats that acceptance as part of X's section.

**Consequences.**
- Prop 2.1(d) is false as stated for 𝓡(𝒟₀) and 𝓡_θ: the record r above is balanced, out of a ∈ R₂, and accepted at {1, 2, 3}.
- PP73 §5.2's claim that (ρ1)–(ρ3) are "also sufficient" for the balanced-swap test is false for the same reason. The priority rule meets (ρ1)–(ρ3), and still the test fails.

### 1.4 The repair: a margin at world 1, and an invariant that survives copying (PROVED)

**Definition (𝒟₀^κ).** Fix κ ∈ (0, 1]. For installed C and X ≠ C, let V := V(rec(C → X)).
- If V ≠ 0 and V₁ ≥ max(V₂, V₃) + κ|V|_∞, choose world 1.
- Otherwise choose the larger of V₂ and V₃, with ties going to 2. Null records therefore go to 2.

**Admissibility.** Suppose V₁ is the only non-negative coordinate. Then V₁ ≥ |V₂| + |V₃| (since ΣV ≥ 0), so V₁ = |V|_∞, and V₁ − V_i ≥ V₁ = |V|_∞ ≥ κ|V|_∞. So world 1 is chosen. In every other case some world in {2, 3} has V_w ≥ 0. So 𝒟₀^κ is an endorsed defence.

On Γ-vectors and on null records it makes exactly the choices of 2 ≻ 3 ≻ 1, because Γ-vectors never have a κ-margin at 1. So Prop 2.1(a)–(c) are unchanged.

**Theorem 6.2′ (PROVED).** Let 𝓡′_θ be 𝓡_θ with 𝒟₀ replaced by 𝒟₀^κ. Then every conclusion of Theorem 6.2 holds for 𝓡′_θ, and Cor 6.3 holds unchanged.

*Proof.* Only step 3 changes. For a non-trivial record r, call r **admissible** if it lies in 𝒦 := G₁ ∪ D_θ ∪ K^κ ∪ Z₁, where:
- **G₁**: the new side is strictly 1-worse at every support point;
- **D_θ**: V(r) ≥ 0 coordinatewise and max V ≥ θ·m(supp r);
- **K^κ**: V ≠ 0 and V₁ ≥ max(V₂, V₃) + κ|V|_∞;
- **Z₁**: V₁ = 0 ≠ V.

Each class is a property of the record alone, so it is shared by every common-context copy. No class contains a u¹-null record.

**Invariant (J).** Every non-trivial record accepted at world 1 is admissible. I prove (J) by transfinite induction over the stages; unions at limit stages preserve it.
- **Generators.** Guidance gives G₁. 𝒟₀^κ gives K^κ. Designated records give D_θ.
- **(TC) completion at world 1.** By step 1 its links have V₁ = 0. By (J) they are non-null. So the installed reverses lie in Z₁.
- **Rules III and IV.** Their premise requires a non-trivial null record accepted at world 1 (§1.2), which (J) excludes. So they never fire.
- **Section limits.** Suppose C_{a_n} ⪯₁ X are accepted at earlier stages, a_n → a in 𝔽, and rec(C_a → X) is non-trivial. Pass to a subsequence lying in one class.
  - **If the limit is null,** then V(C_{a_n} → X) = Γ(a, a_n) exactly. Γ-vectors have a negative coordinate, so they are not in D_θ. They have no κ-margin at world 1 (their maximum is a {1, 2} or {1, 3} tie, or lies at world 2 or 3), so they are not in K^κ. They have Γ₁ ≠ 0 (Lemma 6.0(b)), so they are not in Z₁. That leaves G₁. But G₁ is closed along fixed-rival sections: C_{a_n} → C_a pointwise a.e., so rank₁(X) ≥ rank₁(C_a) a.e., with strict inequality on the support. So the limit is in G₁ and has V₁ > 0, which contradicts nullness.
  - **If the limit is non-null,** it lies in the same class. D_θ and K^κ are closed conditions (V and m(supp) are continuous along sections, by dominated convergence). Z₁ is closed among non-null records, and so is G₁.

Copying never matters, because admissibility is intrinsic to the record. This is exactly the invariant the audit asked for: it survives section closure followed by common-context copying.

Steps 5–7 then go through as written. Prop 2.1(e) now holds as well. Take a record out of T with V = (1, 4, −5)·ε that is mixed at world 1; such records exist, with c = (−1, −2, 1) in (1.1). It is u¹-favourable at world 1 but is in no class of 𝒦, so it is refused there, and (L0⁺) fails. ∎

**Status.** With this one-line change, PP72's main positive result is a theorem. Its limits are unchanged:
- H-models are never dominated (§2);
- the defenders carry no section obligation.

### 1.5 The tie rule and PP73's (ρ1)–(ρ3)

Under (Sym), the exact shapes are as follows.
- On R₃: Γ(a, a′) = (p, p, −2p) outward and (−p, −p, 2p) inward.
- On R₂: (q, −2q, q) inward and (−q, 2q, −q) outward.

The rule 2 ≻ 3 ≻ 1 picks 2 on R₃-outward ties and 3 on R₂-inward ties. It gives 2 on null records. So (ρ1)–(ρ3) hold with ρ₁ = 2, ρ₂ = 3, and Prop 2.1(a)–(c) are correct as statements about the worlds forced by defence and by the record's own section.

(ρ1)–(ρ3) are **necessary** (PP73's derivation is right). They are **not sufficient** once acceptances transported by copies are counted (§1.3). Prop 2.1(f) is correct: no family direction in 𝔽 lies in O₁, because each of the four Γ-shapes has a positive coordinate other than world 1.

### 1.6 The score-certificate propositions

- **Prop 3.1: correct.** The worsening Z exists because μ is atomless and u¹ is strictly increasing in rank. Only strict instances of the field order are used.
- **Prop 3.2: correct with a repair of the proof.** "B is pointwise λ-Bayes" holds only for B ∈ H. The repaired proof works for every B: ΣV(rec(B → X)) = ΣΦ(X) − ΣΦ(B) ≤ 0 because X ∈ H attains the pointwise minimum, and endorsement gives V ≥ 0, so V = 0. In 𝓡_θ endorsement is step 1 itself, so Prop 3.1 is not needed.
- **Prop 3.3: correct.** z_n ≤ v_n and λ·z_n ≥ 0 force z_n → 0; the limit cones are pairwise disjoint. **Cor 3.4: correct as stated.** The "two-dimensional Bayes sheet" is an interpretation.
- **Prop 3.5: correct.** A_{i,n} is relatively closed, and Baire's theorem then gives an arc on which Φ_i∘C is constant. PP56 Prop 5.1 is not needed.

### 1.7 Props 4.1, 4.2, (D3′) and Cor 6.3

- **Prop 4.1: correct, with one gap.** I re-derived:
  - the support identity r⁻¹ = (E ∖ E_A : A → S) ⊕ (L ∖ E : C → B);
  - the ledger: per unit mass on rec(C → B), odd-i points give (V_i, V_j, V_k) = (−2, 1, 1), odd-k points (−1, −1, 2), and odd-j points (1, −2, 1);
  - V_k − V_i = 3(m(Q∩L_i) + m(Q∩L_k)) and V_k − V_j = 3(m(Q∩L_k) + m(Q∩L_j)), so k is the strict argmax.

  Part (b) and the δ_k-defender claim also hold, by nesting. **Gap:** "no section limit forces C ⪯_i C[Q ↦ B]" checks only Q's own section. It is unproved in the presence of copies.
- **Prop 4.2 and the (D3′) formulas: correct.** NUMERICS (`check58.out`): the direct V(B → X) agrees with the ledger formulas to five decimals at t = 0.01 and 0.03, with β_i = β_j exactly by symmetry. Prop 4.2's (p − e, p − e, 2e − 2p) is reproduced exactly. The θ-bound is conservative: f ≥ 4θx suffices.
- **One addition.** A pure-h fill point on the reference family's **common silence** (off R) takes u¹'s "otherwise" row, which is (−1, −1, 4), the same as a −h point. It therefore counts in f, not in e. So (D3′) and Cor 6.3 cover such fills, and only fills supported in R(𝒮) are H-models.
- **Cor 6.3: correct for 𝓡′_θ.** Its loop-edge statements concern fills with a non-H part of fraction ≥ 8θ only. "Repairs most fills" was rightly withdrawn.

### 1.8 The SAT runs

I re-ran E0′ (`rerun_E0T.out`: UNSAT, 53 fills, one deferred, 8 s, on a smaller model set than PP72's, which only strengthens the UNSAT). I also re-ran E1L (`rerun_E1L.out`). It reproduces exactly: SAT, 465 fills, 3 deferred, 307 s. The loop verdicts are identical to PP72's table: T vs C1 rrA, C1 vs C2 Arr, C2 vs T rAr.

The E0 core is explained by the forced pattern alone:
- both fills have the single admissible candidate C1>2;
- a class-1 domination forces T ⋠_i C1>2 for i ≠ 1, and a class-3 domination forces it for i ≠ 3;
- so T is undefended against an installed model.

The pre-screens (Lemma 2.4 on bounded pieces, and strict (G)) are axiom-level, so the UNSAT is a genuine statement about these nine models.

**What the runs do not test.** The encoding (`lib72b.py`, `inst72.py`) contains:
- no u¹ data;
- no 𝒟₀ — defence is a free disjunction over {1, 2, 3};
- **no section clause of any kind**.

So the audit is right: they say nothing about Theorem 6.2, its step 3, or the gap of §1.3. By PP61 Thm C they settle nothing either way.

---

## 2. The audit's H argument: correct, with H stated exactly

**Definition.** Fix the reference family 𝒮 of u¹, which is (2V) and S₃-symmetric. Then

  H := {X measurable : X = the common advice of 𝒮 a.e. off R(𝒮), and X ∈ {h, S} a.e. on R(𝒮)}.

The brief's wording is the right one. The audit's first wording ("only h or silence") omits the off-R condition, without which minimality fails.

**Step 1 (PROVED): H is exactly the set of minimisers of Σ_wΦ_w.** From PP56's table:
- on R, λ·u¹(g, ·) with λ = (1, 1, 1) is 0 for h and S, and positive for −h and for C;
- off R, the common advice is the strict pointwise minimiser.

So ΣΦ(X) ≥ ∫ min_x λ·u¹(g, x) dμ, with equality iff X ∈ H.

**Step 2 (PROVED).** In any u¹-endorsed relation, B ⪯_w X at every w with X ∈ H gives V(rec(B → X)) ≥ 0 and ΣV = ΣΦ(X) − ΣΦ(B) ≤ 0. So V = 0. This holds for **every** B, not only posterior B.

**Step 3 (PROVED).** A domination record is non-trivial. By step 3 of Thm 6.2 (true after the repair; in the unrepaired relation step 3 itself fails), it is refused at world 1. So no H-model is dominated in 𝓡′_θ. Global (C) fails at **every incoherent element** of H, for example:
- every non-conic h/S splice between members of 𝒮;
- every pure-h fill on a non-conic subset of R(𝒮) ∩ Sil.

**Scope.** H grows with 𝒮, but (Sym) forces 𝒮 to contain the symmetrisation of 𝓘. The coherent elements of H need not be protected (BRIEF59).

---

## 3. The zero-sum obstruction; PP66

**Correct (PROVED).** Suppose a rule accepts at i iff v_i(r) ≥ 0, with Σ_i v_i(r) = 0 and v(r⁻¹) = −v(r). Then acceptance at all worlds gives v(r) = 0, so v(r⁻¹) = 0, so the reverse is accepted everywhere, and there is no strict domination.

**Two refinements.**
- **Ties.** The argument uses "iff" at v_i = 0. A rule that breaks null ties asymmetrically (accepting r but refusing r⁻¹ at some world) can produce strict domination, but only through null records. That is Prop 3.2's knife-edge territory again, so the audit's conclusion stands in substance.
- **Lexicographic levels.** The argument extends to lexicographic score sequences whose levels are each zero-sum and antisymmetric (Λ-type rules). The first non-zero level has a negative coordinate, at which r is refused.

**PP66 falls under it, and in a strong form.**
- For every g and every value x, Σ_iψ_i(g, x) = Σ_iu¹_i(g, x) (PP66 Lemma 1(i)). So H is still the set of ψ-sum minimisers.
- R₀^ψ accepts at i only if V^ψ_i ≥ 0, and refuses null records at w₀ in both directions. The surgery only adds refusals.
- So, by §2's step 2 with ψ in place of u¹, R₁ **dominates no H-model at all**, whatever the dominator.
- The Λ^ψ variant (Cor 2.1) is covered by the lexicographic extension.

PP66 can therefore supply individual witnesses only, as the audit says.

**A general form, which says where an escape must lie (PROVED).** Let f be any integrable pointwise field and λ ≫ 0. Suppose two models C and D are both λ-minimal for Σ_wλ_wΦ^f_w over all measurable models, or equivalently pointwise λ-Bayes a.e. Then every splice C[A ↦ D] is λ-minimal. Consequently, any f-endorsed relation can dominate such a splice only through f-null records.

So an endorsing additive field can repair splices of C and D only if C and D have **no common supporting weight**. For u¹, every member of 𝒮 has the weight (1, 1, 1); that is the whole H phenomenon.

The nearby positive route therefore has two branches:
- **(a)** acceptances that are not endorsed by any field for which source and defender share a weight. This is PP72 §7's "unfavourable acceptances".
- **(b)** a field that separates the weights of every source and its defenders. That is a Bayes-type certificate and is close to the excluded realisation approach.

The brief's coupled-refusal programme is consistent with (a).

---

## 4. PP73

- **Cor 1.3: correct.** Each loop pair is a single-coordinate shift. By Lemma 1.2(a) the successor is strictly worse at the shifted world at every support point, so no strictly guiding field has a balanced swap within one loop. Lemma 1.2 does not use (2V).
  NUMERICS: at a = 1.03 and 1.10 there are zero improving points at the edge world; within each loop pair, every odd world has a single sign.
- **Thm 2.3 and Lemma 2.4: correct.** The exponent bookkeeping checks out: m_{i+1} ∝ m_{i−1}∘(k_{i+1} : 1/b), and both raised coordinates differ from the odd world of S_i. NUMERICS: P_{i−1} = A and P_{i+1} = A at 100% of S_i points, for all three edges at both scales. In Lemma 2.4, B[E ↦ C] is incoherent because coherent models are conic and E is not.
- **Props 3.2–3.4: correct** (sections plus the forced pattern; (IB) plus direct (C); (TC)). **Prop 3.5(a): correct.** On the M₃ quadrant the binding vertex is v³, so P₁(a′) answers A iff ρ < τ₀a′³.
- **Prop 4.1: correct.** NUMERICS (`prop41b58.out`):
  - for a′ < a, the odd-2 layer carries both signs (0.0086 / 0.0065);
  - for a′ > a, the strictly middle world is 3, and the odd-3 layer carries both signs (0.0066 / 0.0070), as "roles exchanged" intends;
  - for u versus sδ₃ + tδ₁ with s ≠ t, the middle world carries both signs. This is the fact used in §1.3.
- **The Q/E reductions: correct.**
  - Prop 4.3 is Theorem Q(i)–(ii) with family sequences in place of pure shifts. PP57's proof uses only Γ_w(a, b_k) > 0. Under (Sym), the outward Γ₁ = Γ₂ > 0 on R₃ is exact, so the cited NUMERICS are unnecessary.
  - Thm 4.4 is PP62 Thm E with the shift replaced by a_n. Openness at a comes from the closed section, and only Γ(a, a_n) ∈ O_w is used.
  - Table 4.5 is exact for the family directions of 𝔽, by the four Γ-shapes of §1.5.
  - Props 4.6 and 4.8 are correct as statements about the worlds forced by the record's own section. Like (ρ1)–(ρ3), they do not account for copied limits.
- **Lemma 4.7: correct.** The exact ties hold along family directions; NUMERICS give (0.9243, 0.9243, −1.8487) at u along R₃. Its NUMERICS bullet calls all top-two gaps of 0.001–0.07 noise. That is right for family directions, but the rows at non-family directions are **real asymmetries**: for example, at m₂(1.05) along δ₃, Γ₁ ≠ Γ₂ by about 9% (`check58.out`). Nothing in PP72 or PP73 uses those rows.

---

## 5. The rescaling inequalities and composition: correct (PROVED; NUMERICS)

- **The inequalities.** g ∈ D_{M_m} iff Σ_i m_ip_ig_i/(m·p) > 0 for all p ∈ M. Since m·p > 0 and positivity of a linear function on a polytope is decided at the vertices, this holds iff Σ_im_iv^α_ig_i > 0 for α = 1, 2, 3. The condition is linear in m (not in log m).
- **Silence requirements.** Under (2V), C_m is silent at g iff m lies outside the open convex cone K_g. So a partial compatibility set P(X; S) is an intersection of convex cones with complements of convex cones, and is generally **not convex**.
- **Composition.** {b∘q/(b·q) : q ∈ M_m} = M_{m∘b}, and C_{m∘b}(g) = C_m(b∘g). Pointwise guidance is transported, since g ↦ b∘g preserves sign patterns and null sets.
- **What is not transported.** μ and |g| are not invariant under g ↦ b∘g, so u¹-masses, verdicts and section proofs are not transported. This confirms the audit's caveat.
- **NUMERICS (`check58.out`).** Zero disagreements between the vertex inequalities and a 4,000-point sampled credal set, at five random m. Zero disagreements in C_{m∘b} = C_m∘b, pointwise and vertexwise, at five random pairs.

---

## 6. What this changes for round 59

1. **Theorem 6.2 is repaired, not lost.** The margin rule 𝒟₀^κ and the intrinsic invariant (J) give the "global invariant surviving section closure followed by copying" that the audit asked for. The method is reusable: make every world-1 acceptance class a **closed, record-intrinsic** class that avoids null records and the four Γ-shapes. Any new generator in the round-59 operation must come with such a class, or it reopens §1.3.
2. **The counterexample is a design warning for the coupled-refusal operation.** A defence chosen at one source for one rival (here at b_j against Y_n) can, through a section limit and a copy, become an acceptance between a different source and a different rival. The operation's "surviving defence options" must therefore be computed on records, not on (source, rival) pairs.
3. **The H obstruction is sharper than stated** (§3, general form). Any additive endorsing field fails on every splice of two models sharing a supporting weight. The H-repair must use acceptances outside that envelope, as the brief already directs.

---

## 7. Scripts (`r9/REFEREE58_py/`; run `python3 -I -B <script>` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `lib58.py` | posterior advice from the vertex inequalities; odd worlds; u¹ on H-records; S₃-symmetrised sample | library |
| `cex58.py` → `cex58.out` | §1.3: (2V), the balanced F, the copy identity, Γ-shapes, the strict world-1 maximum at stage 1, Y′'s record, the margin rule's choices | NUMERICS (the argument is PROVED) |
| `check58.py` → `check58.out` | §5; PP73 Cor 1.3, Thm 2.3, Lemma 4.7 rows; PP72 Lemma 6.0 shapes, (D3′) ledger, Prop 4.2; ΣV = 0 on H-records | NUMERICS |
| `prop41b58.py` → `prop41b58.out` | PP73 Prop 4.1 in both scale orders; both-sign worlds of u → sδ₃ + tδ₁ | NUMERICS |
| `rerun_E0T.out`, `rerun_E1L.out` | PP72's own `sat72b.py` (E0′) and `sat72c.py` (E1L, LOOPEDGE=1), re-run unchanged | reproduction |
