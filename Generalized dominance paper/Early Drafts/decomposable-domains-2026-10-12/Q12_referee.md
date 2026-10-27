# Q12. Referee report on the two-world results of Q2_notes.md and Q1_notes.md

15 Oct 2026, round 12. Independent, adversarial referee; I wrote neither note.

- **Read:** BRIEF11; Q2_notes (all); Q1_notes (all); P4_notes Part B (§§5–6); P4B_referee (all); writeup §2
  (axioms, Thm kkm = "Fact 0", Def. CP-a, Def. addup).
- **Scope:** the two-world (n = 2) results. Q2 §6, Q1 §5 (Q1.7–Q1.10) and Conjecture Q2.E are n ≥ 3 and are
  **not refereed here** (§5 notes one consistency point).
- **Verdicts:** CONFIRMED / CONFIRMED WITH REPAIR / GAP / WRONG.
- **New statements** (§4) are labelled PROVED / NUMERICS and are kept separate from the verdicts.
- **Scripts:** `q12ref_py/`, run with `python3 -I`. No proof depends on them.

Notation as in Q2 §1: (Nest), chain c_b, d_b = M∖c_b, slabs [s,t) = c_t∖c_s (all mod null), cut pairs (P,Q) with
P ⊆ c_b, Q ⊆ d_b, and (K): P ≤₁ Q or Q ≤₂ P at every interior b. 𝓜₁, 𝓜₂ are the endorsing probability charges.

---

## 0. Summary

| Claim | Verdict | One-line reason |
|---|---|---|
| Q2 Lemma T₂ | CONFIRMED | The symmetry b ↦ 1−b, 1 ↔ 2 preserves (Nest), (Cl)₁₂, (K) and strict (G)₁₂, so P4B's DL, DR, SE and T all mirror. |
| **Q2 Theorem LF** (+ uniform form) | **CONFIRMED** | (K) at the single cut a plus T₂ at each x ∈ [0,a]; compactness and a Lebesgue number. Every comparison is a cut pair at a. |
| **Q2 Corollary IS** (i)–(iv) | **CONFIRMED** | Every step re-derived. Remark: ν(c_{a\*}) itself may be > 0 (finitely additive left mass at a\*); IS does not claim otherwise. |
| Q2 mirror statements LF₂, IS₂ | CONFIRMED | By symmetry. |
| **Q2 Proposition MP** | **CONFIRMED** (hypothesis can be weakened) | Steps 1–2 need **no** overlap condition. Bounded overlap is used only in step 3. The sharp condition is in §4 N1. |
| Q2 Cor MP-loop | CONFIRMED | Re-derived: mirror T₂ at x = 0 with W = d_{b₀}. |
| Q2 Cor MP′ | CONFIRMED | The CP-a clause is valid because every member of a CP-a credal set endorses *all* comparisons, including the non-relevant Z ≤₁ A_j. |
| Q2 Prop NS | CONFIRMED WITH REPAIR (precision) | b₀ must be the b₀(Z) of MP (it depends on Z through Lemma T₁). Uses no world-2 hypothesis. |
| Q2 §4.1 necessary conditions | CONFIRMED WITH REPAIR (wording of (b)) | "No exported mass can be sent into a fixed small slab" is a reading. Lemma T fixes the source; certificate sources vary. (a), (c)–(f) are correct. |
| Q2 §4.2, §4.3, §4.4 | CONFIRMED (as remarks / failure report) | §4.2(ii) (charges at 1⁻ lie in 𝓜₁) checked. §4.4's "every attempt fails" sentences are not theorems and are not labelled as such. |
| Q2 §5.1 lattice of coherent error sets | CONFIRMED | Re-derived; NUMERICS `q12_lattice.py`: 28,749 mixed gambles, 0 mismatches. |
| Q2 §5.2 one-dimensional KKM, Lemma G-SE | CONFIRMED | G-SE needs X regular, so that E₂X = M∖E₁X; this is stated. |
| Q2 CONJECTURE Q2.N | — (open) | Correctly labelled. |
| Q1.0 cut form of (K), (U), 𝔚^reg | CONFIRMED | The (U) item uses (C) exactly as stated in writeup (C). |
| **Q1.1** band ∪ exotic cones is a (G)+(IB) world | **CONFIRMED** | Key step re-derived; it needs Nn placed to the right (Remark 2.2). |
| **Q1.2** every axiom except one closed world-1 section, with ¬SP^reg₁ | **CONFIRMED WITH REPAIR** | "By Fact 0 every undominated model is tied with a selected one" is **not available**. Fact 0 (Thm kkm) assumes (S) with closed sections, and this system fails them at world 1. Repair (direct, PROVED §1.2): b₂ := μ̄(A) − μ̄(N) (clipped) lies in S₁(X) ∩ S₂(X) for every model X. With that, C_L = the selection, (C) and (LA) hold as claimed. |
| **Q1.3** exact section; failing section [0, a+d+h) | **CONFIRMED** | Formula re-derived, including the empty case (G_D ≱ G_F). NUMERICS `q13_sections.py` uses the **actual** disjoint dyadic family (Q1's script used density surrogates): the formula equals the exact bisection to 10⁻¹²; β_{A_j} < 0.5 and β_{A_j} → 0.5; the band value is 0.2. |
| **Q1.4** mirroring | CONFIRMED WITH REPAIR | (a) and (b) are proved. The summability hypothesis and the passage to Z′ are superfluous for (a): MP's argument gives (a) for every j with h₁ = η(Z). **§0 item 2 misstates the certificate** as "d_{1−h} ≤₂ P_j for disjoint P_j". What is proved is d_{1−h} ≤₂ A_j, equivalently d_{1−h}∖A_j ≤₂ A_j ∩ c_{1−h}. After this repair Q1.4 and Q2 MP have **the same conclusion**. |
| Q1.5 | CONFIRMED | Spread certificates are impossible next to an SP world. |
| **Q1.6** additive partner: no Z ≤₁ vanishing sets; no star certificates | **CONFIRMED** | (a) via MP; (b) via chaining (disjoint sources, disjoint targets) and pigeonhole. Scope: Q1.6 handles certificates with a **fixed** source. §3 explains why this matters. |
| Q1 §4 designs B, C, D | not refereed in detail (failure reports) | B's "(K) fails" is correct for the fibrewise-unanimity part. C and D are unproved, as Q1 itself says. |

**Net.**
- Both notes are sound on the two-world side.
- One genuine gap, repaired here: Q1.2's use of Fact 0 in a system that lacks the closedness Fact 0 needs. The
  conclusion survives through a direct argument.
- One misstatement, repaired: Q1 §0's world-2 certificate.
- The hypotheses of Q2 MP and Q1.4 are stronger than their proofs need (§4 N1 gives the sharp form).
- No claim is WRONG.
- Q1.4 and Q2 MP are **consistent**: both give, for t ∈ [b₀(Z),1) and every target A, the relevant world-2
  comparison d_t ≤₂ A with the *same* sets A.

---

## 1. Q1 (construction side)

### 1.1 Q1.0, Q1.1: CONFIRMED

- **Q1.0.** With P = c_b∖A, Q = A∖c_b: C_b ⪯₁ X ⟺ P ≤₁ Q, and C_b ⪯₂ X ⟺ Q ≤₂ P (cancellation, E₂ = M∖E₁ on M), exactly as stated.
  - X ⪯₁ C_b and X ⪯₂ C_b ⟺ Q ≤₁ P and P ≤₂ Q.
  - A tie at both worlds puts X in C_L by (C). C_L is the chain (N0(ii)), and strict (G) along the chain gives
    X = C_b.
  - Otherwise X dominates C_b.
- **Q1.1.**
  - 𝒞₊ ⊆ band. Nonzero δ ≤ 0 has τ_δ(0) < 0, and τ_δ(a) ≤ 0 < μ̄(F).
  - band + 𝓖(F) ⊆ 𝓖(F) by linearity of τ.
  - Key step, for s ∈ 𝓖(F), t ∈ 𝓖(F′), s + t ∈ 𝒞:
    - on [a,2], use τ_{g_{F′}} ≥ 0;
    - on [0,a), use τ_s(a) ≥ μ̄(F), τ_t(a) ≥ μ̄(F′), s + t ≥ −1, and μ̄{x ≤ x(h) < a} = a − x (no Nn there).
    - This gives τ_{s+t}(x) ≥ μ̄(F) + μ̄(F′) − (a−x) ≥ τ_{g_F}(x). Correct.
  - Cancellation and transitivity follow from the cone form (N9.4).

### 1.2 Q1.2: CONFIRMED WITH REPAIR

**The gap.** The proof ends: "By Fact 0 every undominated model is tied with a selected one, so C_L is the selection,
and (C) and (LA) hold." Fact 0 is writeup Thm kkm. Its hypotheses are (LA) **and (S) with closed sections at every
world**. Q1.3 shows that world 1 of this very system has a non-closed section. So Fact 0 cannot be cited.
- Without it, a non-coherent undominated model tied with no C_b is not excluded by the argument as written.
- Nor is a coherent model off the path that is undominated.

**Repair (PROVED).** Let X = (A,N) be any model (A = E₁X ∩ M, N = unaccepted non-negative problems), and put
b₂ := min(1, max(0, μ̄(A) − μ̄(N))).
- *World 2:* ψ₂(C_{b₂}) = 1 − b₂ ≤ 1 − μ̄(A) + μ̄(N) = ψ₂(X). So C_{b₂} ⪯₂ X. (If μ̄(A) − μ̄(N) > 1, then b₂ = 1 and
  C_1 = P₂ has ψ₂ = 0.)
- *World 1 (band):* if b₂ = 0, then C_0 = P₁ ⪯₁ X. Otherwise δ := 1_{A∪N} − 1_{c_{b₂}} has:
  - τ_δ = μ̄(N) ≥ 0 on (1,2];
  - τ_δ ≥ 0 on [b₂,1];
  - for x < b₂, τ_δ(x) ≥ μ̄(A) − x + μ̄(N) − (b₂ − x) ≥ 2μ̄(N) ≥ 0.
  So δ ∈ band and C_{b₂} ⪯₁ X.
- Hence every model is weakly dominated by, or tied with, C_{b₂}. Q1.2 shows that C_{b₂} has no tie partner. So
  every model other than C_{b₂} is dominated by it. Therefore:
  - U_L ∩ coherent = the path, i.e. C_L = the selection;
  - (C) holds;
  - (LA) holds.
- NUMERICS `q12_fact0.py`: 400 random models, with the band plus a 6-set exotic family; b₂ ∈ S₁ ∩ S₂ in all cases.

The rest of Q1.2 is CONFIRMED:
- competitiveness at the vertices and at interior b;
- undominatedness and absence of tie partners (re-derived; the case split b ≤ a / b > a is correct);
- closed world-2 sections for every model;
- (LF) at interior C_b. Since α(t) < k₁ and β(t) > k₂, ∂D_{K_b}∖0 ⊆ U.
- ¬SP^reg₁: c_a ≤₁ A_j are relevant comparisons, and the A_j are disjoint.

### 1.3 Q1.3: CONFIRMED

For b ≤ a: δ_b − g_F = 1_D − 1_F + 1_{[b,a)}, whose tails are ≥ 0 iff G_D ≥ G_F on [a,1].

For b > a:
- the conditions are G_D(x) − G_F(x) ≥ (b−x)₊ on [a,1];
- on c_a, δ_b − g_F = 0, so x < a reduces to x = a;
- given G_D ≥ G_F, this is exactly b ≤ min_{x∈[a,1]} (x + G_D − G_F);
- if G_D(x₀) < G_F(x₀) for some x₀ ≥ a, the set is empty (both b ≤ x₀ and b > x₀ fail).

**Example.** min_x(x + G_D) = a+d+h, attained exactly on [a,a+d].
- G_{A_j} > 0 there, and G_{A_j} ≤ 2^{1−j}(1−x).
- So β_{A_j} < a+d+h and β_{A_j} → a+d+h, while the band value is d+h.
- Hence S₁ = [0, a+d+h).

`q13_sections.py`, exact rationals, actual disjoint family truncated at 12 dyadic blocks:
- for j = 1, 2 the precondition fails, and the section is empty (formula and grid agree);
- for j = 3…8, β = 0.41252, 0.45626, 0.47813, 0.48907, 0.49453, 0.49727 (formula = bisection to 10⁻¹²);
- 0.5 itself is not in the section.

### 1.4 Q1.4, Q1.5, Q1.6

**Q1.4: CONFIRMED WITH REPAIR.**
- (a): the proof is correct. Z′ ≤₁ A_j follows by cancellation and monotonicity. The contradiction case uses
  (K) at 1 − h_k, cancellation with R_k, and Lemma T at x = 1. However:
  - J₀, Z′ and summability are not needed. Lemma T₁ at x = 1 with Z itself gives η, and for every j and h < η
    the argument of Q2 MP step 2 applies.
  - L_{j,h} is non-null automatically: otherwise A_j ⊆ d_{1−h} and Z ≤₁ A_j contradicts T₁.
- (b): correct. Summability is irrelevant; disjointness (or §4 N1's condition) is what is used.
  - Summability alone does **not** suffice. Take A_j decreasing with a common free filter: a charge on that filter
    has ν(A_j) = 1 for all j.
- (c): correct by symmetry.
- **Repair to Q1 §0 item 2 and the italic text of Q1.5.** Replace "d_{1−h} ≤₂ P_j for disjoint P_j" with
  "d_{1−h} ≤₂ A_j (equivalently d_{1−h}∖A_j ≤₂ A_j ∩ c_{1−h})".
  - d_{1−h} ≤₂ L_{j,h} is strictly stronger when A_j ∩ d_{1−h} is non-null, and it is not proved.

**Q1.5: CONFIRMED.** The E2, E3 and N22 inputs are applied at world 2 by symmetry. Additive world 2 with a
strictly positive weight is a special case.

**Q1.6: CONFIRMED.**
- (a): ν₂(d_{1−h}) ≤ 2ν₂(A_j) → 0, by uniform absolute continuity.
- (b): the vectors 1_{Q_il} − 1_{P_i} (i ≤ k) have disjoint positive parts, disjoint negative parts, and Q's
  disjoint from N. Chaining (cancellation applied k times) gives N ≤₁ B_l. Pigeonhole gives some μ̄(B_l) ≤ 1/m.
- Note: (b) needs only (a); it does not need the P_i ≤₁ Q_il to be relevant comparisons.

### 1.5 Axiom bookkeeping in Q1 (checked)

- Q1.2 verifies every listed axiom for **every** model, including non-regular ones (N ≠ ∅ handled), once the Fact 0
  repair is made.
- Q1.4–Q1.6 use (Cl) only at regular models (through Lemma T and SE), (K) at interior cuts, strict (G) at both
  worlds, and cancellation. They do not use (C), and they use (LA) only through N0. As claimed.

---

## 2. Q2 (exclusion side), n = 2

### 2.1 LF: CONFIRMED

- The open slabs (x−η_x, x+η_x) are E_{x+η}∖E_{x−η} mod null. Because μ(E_b) = bμ(M) is continuous, {x(h) = b} is
  null for each b, and slabs are parameter intervals mod null.
- The finite subcover and the Lebesgue number δ are standard on the compact [0,a].
- For non-null Q ⊆ c_a ∩ J_i: (Q,Z) is a cut pair at a. (K) gives Q ≤₁ Z or Z ≤₂ Q, and T₂ excludes the second.
- Null Q is handled by monotonicity.
- Inputs exactly as stated.

### 2.2 IS: CONFIRMED

- (i): d_{a₀} = ⋃_{b↓a₀} d_b mod null, using μ-continuity; then LF at the interior cut b with Z ∩ d_b.
- (ii): Σ2^{−k}ν_k converges in norm, and 𝓜₁ is convex and norm-closed.
- (iii): both directions are correct. A strictly positive SP weight vanishes on null sets (Def. addup(b)), so after
  normalisation it lies in 𝓜₁.
- (iv): correct. The certificate form is the bipolar argument (−1_B ∈ closure of cone(𝔚) + L^∞₊).
- **Remark (precision, not an error).** IS shows ν(c_a) = 0 for a < a\*. It does not show ν(c_{a\*}) = 0. A member
  can carry a finitely additive "left mass" at a\*. So the 𝓜₁-null ideal is
  {Z ⊆ c_{a\*} : ν̄(Z) = 0} ⊇ {Z ⊆ c_a, a < a\*}. Inclusion may be strict.

### 2.3 MP, MP-loop, MP′, NS

- **MP: CONFIRMED.** In step 2, A_j∖d_t = A_j ∩ c_t = P and d_t∖A_j = Q, so P ≤₁ Q ⟺ A_j ≤₁ d_t (cancellation).
  Lemma T₁ at x = 1 forbids Z ≤₁ d_t. (K) at the interior cut t gives Q ≤₂ P, i.e. d_t ≤₂ A_j. In step 3,
  Σ_{j≤J}ν(A_j) = ν(Σ1_{A_j}) ≤ r.
- **MP-loop: CONFIRMED.**
  - At a cut s, (K) on (c_s∖A_j, A_j ∩ d_s): world 2's alternative is A_j ≤₂ c_s (cancellation).
  - With d_{b₀} ≤₂ A_j that gives d_{b₀} ≤₂ c_s, which T₂ at x = 0 forbids for s ≤ s₀.
  - So c_s ≤₁ A_j, a relevant comparison.
  - "Same targets" means the same *sets*. These are E₁ of one model and E₂ of another (E₁ = M∖A_j).
- **MP′: CONFIRMED.**
  - Complete: E3's P almost agrees with *all* of ≤₁.
  - Leading charge: E2's implication holds for all A, B.
  - CP-a: every member of 𝓜_i endorses every ⪯_i comparison (Def. CP-a), and N22 gives one member with an a.e.
    positive CA part.
  - So the non-relevant comparisons Z ≤₁ A_j are legitimately used.
- **NS: CONFIRMED WITH REPAIR.** State b₀ = b₀(Z) from MP explicitly. The proof uses only MP step 2 (Lemma T₁ and
  transitivity) and the contrapositive of the hypothesis. t = b₀ itself is in the range, so π(d_{b₀}) = 0 directly.
- **Consistency check (PROVED, immediate).** (K) forces every strict cut comparison of each ν₂ ∈ 𝓜₂ into world 1.
  So NS applied with π = ν₂ re-derives ν₂(d_{b₀}) = 0, in agreement with MP. NS applied to Q1's attempt A, where
  world 1 contains the μ̄-band, forces a failure of a hypothesis of Lemma T₁. This is exactly the world-1
  closedness failure of Q1.3. The two notes agree.

### 2.4 §4.1–§4.4

- (a), (c), (d), (e), (f) are correct.
  - (f): integrating the certificate against ν̄ with ν̄(c_a) = 0 gives 0 ≤ λ_k(ν̄(Q_k) − ν̄(P_k)) ≤ ε for each k.
    On c_a, Σλ_k1_{P_k} ≥ 1 − ε a.e.
- (b), second sentence: Lemma T₁ quantifies over a **fixed** source Z. Certificate sources P_k vary, and can be thin.
  Replace the sentence with: "for each fixed source P and point x there is η(P,x) such that no non-null target
  inside the η-slab at x is ≥₁ P; η has no lower bound uniform in P."
  - This is exactly where §4.3 locates the missing rate, so Q2 is internally consistent once reworded.
- §4.2(ii): any Banach limit of μ(·∩d_b)/μ(d_b) as b → 1 vanishes on null sets and on each c_t (t < 1), so it
  endorses every cut pair. Confirmed.

### 2.5 §5: CONFIRMED

- Lattice (re-derived; NUMERICS above).
- One-dimensional KKM: S₁ ∋ 0 and S₂ ∋ 1 by vertex competitiveness; S₁ ∪ S₂ = [0,1]; connectedness.
- G-SE: q ∈ S₁ ∩ S₂; E₂X ⊊ E₂C_p by regularity of both; strict (G)₂; undominatedness of C_p.

---

## 3. Consistency between Q1.4 and Q2 MP (requested)

- Same mechanism: Lemma T₁ at x = 1, then (K) at cuts t near 1.
- Same conclusion: d_t ≤₂ A for every target A with Z ≤₁ A, for all t ∈ [b₀(Z),1), uniformly in A.
- Different, and in both cases redundant, side hypotheses:
  - Q1.4 assumes summability (needed for nothing) and disjointness (for nullity);
  - MP assumes bounded overlap (for nullity).
- The nullity step needs exactly the condition of §4 N1.
- Q1 §0's "d_{1−h} ≤₂ P_j" is the only inconsistency. It is a misstatement (repaired above).
- Q2 MP-loop and Q1.4(c) / design D ("ping-pong") describe the same closed loop of comparisons. Neither note claims
  a contradiction from it, and I find none (§4 N2).

---

## 4. New results (separate from the verdicts)

### N1 (PROVED). Sharp form of MP; a quantitative consequence of SP at the partner world

Under (Nest), fix a non-null Z and let 𝒰₁(Z) := {A : Z ≤₁ A}. Let b₀ = b₀(Z) < 1 be given by Lemma T₁ at x = 1.

- (a) d_t ≤₂ A for **every** A ∈ 𝒰₁(Z) and every t ∈ [b₀,1). These are relevant world-2 comparisons. No overlap
  condition is needed (this is MP steps 1–2).
- (b) For a family 𝒜 ⊆ 𝒰₁(Z), the following are equivalent:
  - (b1) every charge ν ≥ 0 has inf_{A∈𝒜} ν(A) = 0;
  - (b2) inf{‖f‖_∞ : f ∈ conv{1_A : A ∈ 𝒜}} = 0 ("𝒜 is uniformly Cesàro-thin").

  If they hold, then:
  - every ν ∈ 𝓜₂ vanishes on d_{b₀};
  - by MP-loop, every ν ∈ 𝓜₁ vanishes on c_{s₀};
  - **both worlds fail SP^reg**.

  Pairwise disjoint (Q1.4) and bounded overlap (Q2 MP) are special cases. Summability is not.
- (c) If world 2 satisfies SP^reg₂ with weight ν₂, then for every non-null Z:

    ν₂(A) ≥ ν₂(d_{b₀(Z)}) > 0 for every A with Z ≤₁ A,

  and hence ‖f‖_∞ ≥ ν₂(d_{b₀(Z)}) for every f ∈ conv{1_A : Z ≤₁ A}. Symmetrically with the worlds exchanged.

*Proof.*
- (a) is MP steps 1–2 verbatim. They use only Z ≤₁ A, Lemma T₁ and (K).
- (b): the states on L^∞ form a weak*-compact convex set, K := conv{1_A} is convex, and (ν,f) ↦ ν(f) is bilinear
  and weak*-continuous in ν. Sion's minimax theorem gives
  sup_ν inf_{f∈K} ν(f) = inf_{f∈K} sup_ν ν(f) = inf_{f∈K} ‖f‖_∞ (f ≥ 0).
  Also inf_{f∈K} ν(f) = inf_A ν(A). So (b1) ⟺ (b2). Then ν ∈ 𝓜₂ gives ν(d_{b₀}) ≤ inf_A ν(A) = 0. MP-loop applies
  with W = d_{b₀}.
- (c): by (a), ν₂(d_{b₀}) ≤ ν₂(A), and ν₂(d_{b₀}) > 0 by strict positivity. Then ‖f‖_∞ ≥ ν₂(f) ≥ ν₂(d_{b₀}). ∎

*Reading.* Simple certificates are exactly "Z ≤₁ a uniformly Cesàro-thin family". Next to an SP world, the
world-1 upper set of each Z is uniformly non-thin, with a modulus ν₂(d_{b₀(Z)}). That modulus depends on Z only
through Lemma T₁'s radius, which has no rate. This is the precise point at which general certificates (thin,
varying sources) escape.

### N2 (PROVED). Closure of a mirrored pair

Let 𝒜 ⊆ 𝒰₁(Z) be any family, and put:
- s₁ := max{s : c_s ≤₁ A for all A ∈ 𝒜};
- t₁ := min{t : d_t ≤₂ A for all A ∈ 𝒜}.

Both are attained, because ⋂_A S₁(A) and ⋂_A S₂(A) are closed, and s₁ > 0 and t₁ < 1 (MP-loop). If s₁ < t₁, then

  c_{s₁} ≤₁ d_{t₁} and d_{t₁} ≤₂ c_{s₁},

so the cut pair (c_{s₁}, d_{t₁}) is accepted by **both** worlds, in the favourable direction.

*Proof.*
- For b ∈ (s₁,1), some A ∈ 𝒜 has c_b ≰₁ A. (K) on (c_b∖A, A ∩ d_b) gives A ≤₂ c_b (cancellation). So
  d_{t₁} ≤₂ A ≤₂ c_b.
- The mirror of Lemma DL (world 2; x = s₁, F = c_{s₁}, W = d_{t₁} ⊆ d_{s₁+η}, η = t₁ − s₁) then gives
  d_{t₁} ≤₂ c_{s₁}.
- The world-1 statement is the mirror argument: for b < t₁, (K) on (A ∩ c_b, d_b∖A) gives A ≤₁ d_b; then Lemma DL
  at x = t₁. ∎

*Reading.* (U) forbids only the *reverse* acceptance (Q ≤₁ P and P ≤₂ Q). Every comparison generated by the
ping-pong goes in the favourable direction at its world. So **(U), (C) and (K) give no contradiction from mirrored
pairs.** Any proof of Q1.C4 must come from closedness, i.e. from a rate in Lemma T. This confirms Q2 §4.3's
diagnosis from a second direction.

### N3 (PROVED; NUMERICS illustration). Why the a\* = 1 extreme fails, in the simplest non-trivial family

For K > 0 let 𝒦_K := {δ : ∫_{x(h)≥y} e^{Kx(h)} δ dμ̄ ≥ 0 for all y} (first-order dominance after an exponential tilt).

- By integration by parts along x, 𝒦_K ⊆ 𝒦_{K′} for K < K′. So 𝒜₁ := ⋃_K 𝒦_K is a convex cone. It contains 𝒞₊ and
  no nonzero δ ≤ 0. It is therefore a legitimate cancellative, strictly monotone world (N9.4).
- It accepts **every** cut pair with non-null target. So every endorsing charge lives at 1⁻: this is a\* = 1, the
  extreme case of Q2 §4.2(ii).
- But for Z ⊆ c_{x−η}, S₁(c_x∖Z) = [0,x), which is open. This is exactly the configuration Lemma DL excludes.
- NUMERICS `q12_tilt.py`: the pair (Z,[b,x)) is accepted from K = 2, 8, 15, 21 for b = 0.5, 0.59, 0.599, 0.5999
  (x = 0.6, Z = [0.1,0.3)).

So "infinitely steep" weights collapse to the rightmost-point world. A surviving world needs a weight that is
infinitely heavy on **spread** thin sets and light on **concentrated** ones, i.e. it must be non-additive in the
chain direction. This matches Q2 §4.4 and Q1 §4.

### N4 (observation, PROVED by inspection). What Q1.6 does not cover

Q1.6(b) handles certificates with a fixed exported set N and disjoint targets per round. Consider a certificate
built from thin sources P_i (pieces of c_a of size a/K), each with L targets Q_il that overlap *across* i, with
multiplicity ≤ εL. Integrating with μ̄ gives average μ̄(Q_il) ≤ ε/K, against μ̄(P_i) = a/K: a scale-free ratio
ε/a.
- Neither Q1.6(a) nor Lemma T applies: the sources shrink, and Lemma T's radius η(P_i) may shrink with them.
- Chaining does not apply either: the targets overlap.

So, even next to an **additive** partner, the open case is exactly "ratio certificates with thin sources". Q1.C1
needs a Lemma T whose radius is bounded below in terms of μ̄(P) and the position, i.e. the same missing rate.

---

## 5. Exact established statements (n = 2, under (Nest), strict (G), (IB), (LA), (S), (C))

1. (Q2 LF) For a ∈ (0,1) and non-null Z ⊆ d_a, there is δ(Z,a) > 0 such that every Q ⊆ c_a inside a slab of
   width < δ satisfies Q ≤₁ Z. Mirror: LF₂.
2. (Q2 IS) ¬SP^reg₁ ⟺ some c_a, a > 0, is 𝓜₁-null. With a\* := inf_ν a₀(ν):
   - c_a is 𝓜₁-null for every a < a\*;
   - every 𝓜₁-null set lies in c_{a\*} mod null;
   - one ν̄ ∈ 𝓜₁ is positive on every non-null subset of d_{a\*}.
   Mirror for world 2 with final segments.
3. (Q2 MP + §4 N1) If Z ≤₁ A for every A in a uniformly Cesàro-thin family, then:
   - d_t ≤₂ A for t ≥ b₀(Z) and c_s ≤₁ A for s ≤ s₀;
   - both worlds fail SP^reg;
   - neither world is complete, CP-a, or has a nonzero leading charge (MP′, E3 CHECKED).
4. (Q1.5, Q1.6, N1(c)) If one world has SP^reg, the other has no simple certificate. If the SP weight is uniformly
   absolutely continuous, then no Z is ≤₁ sets of vanishing measure, and there are no star certificates.
5. (Q1.2 repaired, Q1.3) Under every axiom **except closedness of world-1 sections**, ¬SP^reg₁ is realisable
   (n = 2, any interval target). For attempt A the failing section is exactly [0, a+d+h).
6. (Q2 §5) Without (Nest): the lattice {σ < α} ∪ {τ ≤ β}, one-dimensional KKM, and G-SE.

---

## 6. The precise remaining two-world question

Under (Nest), with every axiom (closed sections for every model):

- **(R1) Mirrored simple pairs.** Is there a system with a non-null Z and a uniformly Cesàro-thin family 𝒜 such that
  Z ≤₁ A for all A ∈ 𝒜? By N1 and MP-loop this is the same as asking for c_{s₀} ≤₁ A and d_{b₀} ≤₂ A for all
  A ∈ 𝒜. By N2 the ping-pong generates only favourable-direction comparisons. A proof must therefore use
  closedness quantitatively.
- **(R2) General certificates.** If neither world has a simple certificate, must both satisfy SP^reg? Equivalently
  (IS): can c_a be 𝓜₁-null through "ratio certificates" whose sources are thin pieces of c_a, with overlapping
  targets (N4)? This is open even when world 2 is additive (Q1.C1).
- **(R3) The missing lemma, common to R1 and R2.** A rate in Lemma T:
  - *Statement:* for P ⊆ c_b non-null and x > b, the radius η(P,x) admits a lower bound depending only on (μ̄(P),
    x − b).
  - *Consequence:* this would give Q1.C1, and with LF it would give a Vitali argument for N17.B′(2).
  - *What is known:* closedness supplies only a qualitative radius, one cut at a time.
- **(R4)** CONJECTURE Q2.N: (S) forces (Nest) in n = 2. Without it, nothing beyond G-SE is known.

**Constructions.** None exists. Any example must:
- fail SP^reg at **both** worlds if its certificate is simple;
- be non-additive in the chain direction in both worlds (N3; Q2 NS; Q1.6);
- pass Q1.3-type closedness. In Q1.3 this exactly requires the family of target profiles to be compact, which a
  thin family cannot be.

Q2.E (n = 3) is essentially Q1.8 (CHECKED there under (Nest_ij)). That consistency point is noted but not refereed.

---

## 7. Files (`q12ref_py/`, run with `python3 -I`)

- `q13_sections.py` (+ `.out`): Q1.3 with the actual disjoint dyadic family, exact. Formula = bisection; the
  section is [0,0.5), not closed.
- `q12_fact0.py` (+ `.out`): the Q1.2 repair. b₂ ∈ S₁ ∩ S₂ in 400 random models; no domination of C_b found.
  The undominatedness test is weak; the proof is exact.
- `q12_lattice.py` (+ `.out`): Q2 §5.1 lattice, 28,749 mixed gambles, 0 mismatches.
- `q12_tilt.py` (+ `.out`): N3 illustration. Tilted-FSD worlds accept the trimmed cut pairs for all b < x, so the
  section is open.
