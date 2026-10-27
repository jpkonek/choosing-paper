# JJ1 (round 38, BRIEF30). Referee report on the lifting theorem: a protected weak-additive leading field gives a full (FC) cover

18 Oct 2026. Rules of BRIEF13 and BRIEF30. The corrections of AUDIT_II.md are adopted. Labels:
- **PROVED**: the full argument is written or re-derived here (one reader: me).
- **CHECKED**: an exact computation with a stated script, or a step-by-step reading of a recorded result whose imports keep their recorded status.
- **CONJECTURE**: none offered.
- **NUMERICS**: none used.

Script: `jj1py/checks.py`. Run `python3 -I checks.py` inside `jj1py/`; the output is in `checks.out`. All arithmetic uses `fractions.Fraction`. Nothing in the verdict rests on the script. It only double-checks algebra that is proved below.

**What I read.**
- BRIEF30, AUDIT_II(+summary), AUDIT_HH_rate, BRIEF29, BRIEF28, BRIEF13.
- The write-up §2, and the statements of Theorem main, Cor coverage and Theorem gm.
- HH1 (whole). HH2 §§1, 5, 6.
- II1 (whole), II2 §§0–3.

**No assumption is added.** Every hypothesis named below is a hypothesis of the theorem being refereed, or of the stated sub-result.

---

## 0. Verdict

**The lifting theorem is correct (PROVED).** It needs one cosmetic repair, in the closed-sections proof of HH2 Prop 6.1(d). Every step that BRIEF30 lists holds on exactly the stated hypotheses:
- Φ is integrable, additive and weakly guiding;
- the selection is coherent, continuous in measure, passes through T1 and is (NT)/(SLP);
- Ψ is any integrable, strictly guiding second level;
- the domain is decomposable with (LF) at T1. This includes the full domain.

The audit's direct margin argument is sound, including at boundary limits. The transfer of records from C_{p_n} to C_{p*} is legitimate. Weak guidance of Φ is exactly what is used, and nothing more is needed. Strict (G) of the final relation holds for every non-null improvement, including those supported on the zero set of Φ.

Three points matter more than the verdict itself.
- **It is a conditional.** For T1 its hypotheses are not known to be satisfiable (problem P_w). On M_U they are unsatisfiable (II1 Prop 5.1, CHECKED).
- **Nothing in it is specific to T1, to three worlds, or to (FC) beyond what is stated.** See §4.2.
- **For admissibility and (C), (NT) does all the work directly.** The lexicographic base is needed only for (FC).

| Step | Verdict |
|---|---|
| S1 HH2 6.1(a): reflexive, (IB), strict (G) | correct |
| S2 HH2 6.1(b): strict ⇒ L-strict; (FC) with ordering extension L | correct (no choice principle needed) |
| S3 HH2 6.1(c): ties = lexicographic ties | correct |
| S4 HH2 6.1(d): closed sections | **correct with repair**: the case split "X = C_q" is wrong for non-injective selections; unified proof in §1.4 |
| S5 positive margin c(a) > 0 (audit; II1 Thm 3.2 under (NT); II2 Thm 2.1 + Cor 2.3) | correct, boundary supports and transfer included |
| S6 (RB) ⇒ continuous k (audit criterion) | correct; an explicit closed-form majorant is added |
| S7 competitiveness on supp p | correct |
| S8 every C_p undominated; T1 ∈ C_L; (LA) | correct; follows from (NT) directly, the lex base is not needed |
| S9 transitivity-free KKM (HH1 Prop 1(a),(b)) as used | correct |
| S10 direct (C); U_L = C_L = Σ | correct |
| S11 (LF) | correct (trivial on the full domain; a hypothesis on a general decomposable domain) |
| S12 weak guidance suffices; strict (G) on the zero set of Φ | correct |
| II1 Thm 2.4, Thm 4.1; II2 Thm 2.1, Cor 2.3, Cor 2.4 | correct |
| II1 Prop 5.1 (no (NT) design on M_U) | correct, modulo Theorem main / Cor coverage (refereed twice) |
| II1 Prop 5.2 (shape of Φ on the full domain) | correct, modulo Theorem gm. One reading note: "every zero is bad~silence" holds **after** the normalisation in (b) |
| BRIEF30 "elementary necessary condition" | correct (§3.3) |

---

## 1. The rate world (HH2 Prop 6.1(a)–(d))

**Notation.** As in II1 §1.1.
- Pairs are indexed by H. M := μ(H) < ∞.
- Records t = rec(X, Y). Increments are Φ_i(t) = Φ_i(Y) − Φ_i(X) and Ψ_i(t) likewise. Size is m(t) = μ(supp t).
- The envelope E(h) := max_{i,a}(|φ_i(h,a)| + |ψ_i(h,a)|) is integrable.
- Put B := 2 max_i ∫ E dμ. Then |Ψ_i(t)| ≤ B and |Φ_i(t)| ≤ B for every record.
- For continuous k : (0, M] → (0, ∞):
  𝒜_i^k := {ι} ∪ {t ≠ ι : Φ_i(t) ≥ 0 and Ψ_i(t) + k(m(t))Φ_i(t) ≥ 0},
  and X ≼_i Y ⟺ rec(X, Y) ∈ 𝒜_i^k.
- L_i is the lexicographic preorder on the pairs (Φ_i(X), Ψ_i(X)). It is a complete preorder on all models, because the envelope is integrable and so both values are finite.

The record facts used below are these. Increments depend on the record only. Φ_i(t⁻¹) = −Φ_i(t). supp t⁻¹ = supp t, so k(m(t⁻¹)) = k(m(t)). Strictly guiding means strict increase in world-i rank on the advice range, a.e.

### 1.1 (a) Reflexive, (IB), strict (G). Correct (PROVED)

- **Reflexive:** ι ∈ 𝒜^k.
- **(IB):** the verdict is a function of the record. In the write-up's (IB), the two pairs ((D∩A)∪F, (E∩A)∪F) and ((D∩A)∪G, (E∩A)∪G) have the same record. One direction of the record characterisation suffices, so this holds on every decomposable domain.
- **Strict (G).** Let X give advice weakly better than Y at world i, a.e., and let t = rec(X, Y).
  - If t = ι, then X ≼_i Y by reflexivity.
  - Otherwise the background order is a strict total order on the four advices at each pair, so X is strictly better on the non-null set supp t.
  - Weak guidance of φ_i gives Φ_i(t) ≥ 0. Strict guidance of ψ_i gives Ψ_i(t) > 0: the integrand is ≥ 0 a.e. and > 0 on a non-null set. Hence t ∈ 𝒜_i^k.
  - For t⁻¹: Φ_i(t⁻¹) ≤ 0 and Ψ_i(t⁻¹) < 0. If Φ_i(t⁻¹) < 0, the first clause fails. If Φ_i(t⁻¹) = 0, the second clause reads Ψ_i(t⁻¹) ≥ 0, which fails. So t⁻¹ ∉ 𝒜_i^k, and X ≺_i Y.

### 1.2 (b) Strict ⇒ L-strict; (FC). Correct (PROVED)

**𝒜^k ⊆ L.** Let t ≠ ι be accepted. If Φ_i(t) > 0, L accepts it. If Φ_i(t) = 0, then Ψ_i(t) ≥ 0, and L accepts it.

**Strict ⇒ L-strict.** Let t ∈ 𝒜^k with t⁻¹ ∉ 𝒜^k, and suppose L accepted t⁻¹. Then Φ_i(t) = 0 and Ψ_i(t) = 0. In that case Ψ_i(t⁻¹) + kΦ_i(t⁻¹) = 0 and Φ_i(t⁻¹) = 0, so t⁻¹ ∈ 𝒜^k, a contradiction.

**(FC).** No Suzumura or Szpilrajn argument is needed. A chain A_0 ≼_i … ≼_i A_k in 𝒜^k is a chain in L, so A_0 L_i A_k. If A_k ≺_i A_0 held in 𝒜^k, it would hold strictly in L, contradicting transitivity of L. So L_i is an ordering extension, and HH2 Lemma 1.5 is not even needed.

### 1.3 (c) Ties are lexicographic ties. Correct (PROVED)

If t, t⁻¹ ∈ 𝒜^k and t ≠ ι, then Φ_i(t) ≥ 0 and −Φ_i(t) ≥ 0, so Φ_i(t) = 0. Then ±Ψ_i(t) ≥ 0. Conversely, Φ_i(t) = Ψ_i(t) = 0 puts both t and t⁻¹ in 𝒜^k.

### 1.4 (d) Closed sections. Correct with repair (PROVED)

HH2 splits into the cases "X ∉ Σ" and "X = C_q", and says that "any limit point other than q is a continuity point". That is false when the selection is not injective. Every p′ ≠ q with C_{p′} = C_q a.e. is also a point where m vanishes. BRIEF30 explicitly forbids assuming injectivity. These points do lie in the section, by reflexivity, so the conclusion survives. The clean proof needs no case split.

**Repair.** Fix i and an evaluable X. Put t_p := rec(C_p, X) and m(p) := m(t_p).

**Continuity.** Let D(p, p′) be the set of pairs at which C_p and C_{p′} advise differently.
- The advice at a pair f ∈ H is determined by whether f and −f are members, and μ is symmetric. So μ(D(p, p′)) ≤ μ(C_p △ C_{p′}).
- Hence |m(p) − m(p′)| ≤ μ(D(p, p′)).
- Similarly |Φ_i(t_p) − Φ_i(t_{p′})| ≤ ∫_{D(p,p′)} 2E dμ, and likewise for Ψ_i.
- By continuity in measure and absolute continuity of ∫E, all three functions are continuous on Δ.

**Closedness.** Let p_n → p* with t_{p_n} ∈ 𝒜_i^k.
- If m(p*) = 0, then t_{p*} = ι, which is accepted by reflexivity. This is the endpoint case, and it covers every p* with C_{p*} = X, however many there are.
- If m(p*) > 0, then m(p_n) > 0 for large n, so t_{p_n} ≠ ι, and Φ_i(t_{p_n}) ≥ 0 and (Ψ_i + k(m)Φ_i)(t_{p_n}) ≥ 0.
- k is continuous at m(p*) ∈ (0, M]. Passing to the limit gives the same two inequalities at p*.

So the section is closed. The case "X selected" is the first case; "X not selected" falls under the second.

CHECKED (`checks.py` part (1); 200 000 random rational records, k(m) = 1 + 1/m): 𝒜^k ⊆ L; 𝒜^k-strict ⇒ L-strict; ties ⟺ Φ = Ψ = 0; worsening records are accepted and strict. No failures.

---

## 2. Rate bound, competitiveness, admissibility, (C)

### 2.1 The positive margin, with size as a coordinate. Correct (PROVED)

**Definition.**
c(a) := inf { max_{i ∈ supp p} [Φ_i(X) − Φ_i(C_p)] : p ∈ Δ, X evaluable, m(rec(C_p, X)) ≥ a }, for a ∈ (0, M].

**Claim.** Under (NT), continuity in measure and integrability, 0 < c(a) ≤ B for every a ∈ (0, M], and c is nondecreasing.

**Proof.**
1. **Bounds.** The set is nonempty for every a ≤ M: on the full domain, give advice different from C_p at every pair. On a general decomposable domain, read "for every a for which the set is nonempty" and set c := +∞ otherwise; nothing below changes. So c(a) ≤ B. Under (NT), every X ≠ C_p has some i ∈ supp p with a strictly positive increment, so c(a) ≥ 0.
2. **The bad sequence.** Suppose c(a) = 0. Choose (p_n, X_n) with m(rec(C_{p_n}, X_n)) ≥ a and max_{i∈supp p_n}[Φ_i(X_n) − Φ_i(C_{p_n})] ≤ 1/n.
   - Pass to a subsequence with constant support J and p_n → p*.
   - Then J* := supp p* ⊆ J, since coordinates of p* that are positive stay positive along the sequence.
   - **This is the boundary case. It is harmless: control at the worlds of J is control at the worlds of J*.**
3. **Transfer.** Let t′_n := rec(C_{p*}, X_n). This is an actual record, because X_n is the same evaluable model. By the bounds of §1.4, taken uniformly in X:
   - |Φ_i(t′_n) − [Φ_i(X_n) − Φ_i(C_{p_n})]| = |Φ_i(C_{p_n}) − Φ_i(C_{p*})| ≤ ∫_{D(p_n, p*)} 2E → 0;
   - |m(t′_n) − m(rec(C_{p_n}, X_n))| ≤ μ(D(p_n, p*)) → 0.

   So Φ_i(t′_n) ≤ 1/n + o(1) for i ∈ J*, and m(t′_n) ≥ a − o(1). **The transfer is legitimate.** This is II2 Lemma 1.1(b), and it needs no Young measures.
4. **Compactness and purification.** Let Z_{p*} be the set of vectors (m(t), (Φ_i(t))_i, (Ψ_i(t))_i) over records t out of C_{p*}.
   - Z_{p*} is the Aumann integral of the measurable, finite-valued, integrably bounded multifunction h ↦ {(1[b ≠ C_{p*}(h)], φ(h,b) − φ(h, C_{p*}(h)), ψ(h,b) − ψ(h, C_{p*}(h))) : b ∈ A(h)}.
   - The measure μ restricted to H is finite and non-atomic. So Z_{p*} is convex and compact (Aumann 1965; II2 Lemma 1.1(a)).
   - Every point of Z_{p*} is realised by an actual evaluable model. Take a measurable selection of the values. Choose the advice measurably, by taking the first admissible advice in a fixed order. By the write-up's Remark advicerange, that advice map is an evaluable model.
5. **Contradiction.** A limit point of (t′_n) in Z_{p*} is realised by some X* with:
   - m(rec(C_{p*}, X*)) ≥ a > 0, so X* ≠ C_{p*};
   - Φ_i(X*) ≤ Φ_i(C_{p*}) for every i ∈ J*.

   This contradicts (NT) at p*. ∎

**Answers to the brief's questions.**
- *Does the limit competitor have disagreement ≥ a and leading increments ≤ 0 at every world of the limit support?* Yes. The size is a linear coordinate of Z_{p*}, and it converges along the subsequence.
- *What if supports shrink?* (NT) at p* constrains only J*, and the bad sequence controls a superset of J*.
- *Is the transfer from C_{p_n} to C_{p*} legitimate?* Yes, uniformly in the competitor.

II1's route reaches the same result. Its Young-measure Lemma 1.2 plus (NT) makes (ND) vacuous in Thm 3.2. I checked that route too: the weak-* argument is correct, because L¹(H × 𝔄) is separable and the indicator test function 1[b = C_{p*}(h)] is in L¹. It is a longer path to the same compactness.

**From the margin to (RB).** Let X be a competitor with m(rec(C_p, X)) ≥ a. Some i ∈ supp p has Φ_i(t) ≥ c(a) > 0, so r_i = max(0, −Ψ_i/Φ_i) ≤ B/c(a). Hence

  sup{ r(p, X) : m ≥ a } ≤ B/c(a) < ∞, which is (RB).

The minimum over worlds in r is attained at a world with a positive leading increment, so no world with a leading tie is ever needed. **PROVED.**

### 2.2 (RB) ⇒ a continuous rate. Correct (PROVED, CHECKED)

**The audit's dyadic construction.** Put b(a) := sup{r : m ≥ a}, which is nonincreasing and finite for a > 0. Choose a nondecreasing sequence β_n ≥ b(M/2^{n+1}) + n + 1, and interpolate linearly between the points M/2^n.
- On [M/2^{n+1}, M/2^n], both endpoint values are ≥ b(M/2^{n+1}).
- β_{n+1} ≥ b(M/2^{n+2}) ≥ b(M/2^{n+1}), by monotonicity of b.
- A linear interpolant lies above the smaller endpoint value.
- Every record of size m in that interval has r ≤ b(M/2^{n+1}) ≤ k(m).

Divergence at 0 is not needed for the theorem.

**A closed form under (NT) (PROVED).** Put g(m) := B/c(m). It is finite, positive and nonincreasing. Let

  k(m) := (2/m) ∫_{m/2}^{m} g(s) ds.

- k is continuous and positive, because g is monotone, hence measurable and locally bounded on (0, M].
- k(m) ≥ g(m), since g(s) ≥ g(m) for s ≤ m.
- **Any** continuous k ≥ B/c works.

CHECKED (`checks.py` (2a), (2b)): both majorants dominate a discontinuous nonincreasing step bound at 15 977 and 597 rational points respectively. No failures.

### 2.3 Competitiveness on supp p. Correct (PROVED)

- For X = C_p, use reflexivity.
- For X ≠ C_p, the defending world i of §2.1 has Φ_i(t) > 0 and −Ψ_i(t) ≤ k(m)Φ_i(t). So t ∈ 𝒜_i^k, that is, C_p ≼_i X with i ∈ supp p.

### 2.4 Admissibility: every C_p undominated; T1 ∈ C_L; (LA). Correct (PROVED)

**Direct proof from (NT).** Suppose Y ≼_i C_p at every world. Then, at every world, either rec(Y, C_p) = ι or Φ_i(C_p) − Φ_i(Y) ≥ 0. In both cases Φ_i(Y) ≤ Φ_i(C_p) for i ∈ supp p. (NT) gives Y = C_p a.e. So nothing even weakly dominates C_p except C_p itself, and in particular nothing dominates it.

The route through the lexicographic base is also correct: (NT) ⇒ (U) ⇒ (A1) (II1 Lemma 2.3(c)), and then 𝒜^k-domination is L-domination by §1.2. But it is unnecessary.

**Consequences.**
- C_p is coherent by hypothesis, so C_p ∈ C_L.
- The selection maps into C_L, as (S) requires.
- T1 = C_{q₀} ∈ C_L.
- (LA) holds.

HH2 Cor 6.2's gap (AUDIT_HH_rate) is closed in this regime.

### 2.5 The transitivity-free KKM argument (HH1 Prop 1(a),(b)) as used. Correct (PROVED)

**(a).** Put A_i := {p : C_p ≼_i m}. These sets are closed by §1.4. Competitiveness puts each p into some A_i with i ∈ supp p. So every face Δ_S is contained in ∪_{i∈S} A_i, which is the KKM hypothesis. Hence ∩A_i ≠ ∅.

**(b).** Let m be undominated and C := C_{p_m}. We have C ≼_i m at every world. If not m ≼_j C at some world j, then C dominates m. So m ≼_i C at every world.

**What is used.** Only closedness, competitiveness, finiteness of Ω, and the definition of domination. There is no circularity: undominatedness of the C_p (§2.4) is proved before (S) is invoked, and it does not use KKM.

### 2.6 Direct (C) and U_L = C_L = Σ. Correct (PROVED)

- **Undominated ⇒ selected.** Let B be undominated. By §2.5, B ≼_i C_p at every world for some p. (NT) gives B = C_p. So U_L ⊆ Σ ⊆ C_L ⊆ U_L, and therefore U_L = C_L = Σ.
- **(C).** Let X ≈ C with C ∈ C_L. Then C = C_p for some p. X ≼_i C_p at every world, so (NT) gives X = C_p ∈ C_L.

**Trivial three-world ties with selected models.** These hold in the strong form: any model weakly better than C_p at the active worlds equals C_p.

### 2.7 (LF). Correct

- On the full domain every measurable R is evaluable, so (LF) holds with any N.
- On a general decomposable domain, (LF) at T1 is a hypothesis of the theorem, and the proof above runs verbatim. The only domain-dependent ingredient is the Aumann integral over the advice ranges A(h).

### 2.8 Is weak guidance enough? Does strict (G) hold on the zero set of Φ? Yes (PROVED)

**Weak guidance is used at exactly two points**, both in §1.1:
- worsening records have Φ_i ≥ 0, so they are accepted;
- improving records have Φ_i ≤ 0, so they are rejected.

It is also necessary for the rate rule to satisfy (G): if a worsening record had Φ_i < 0, the rule would reject it. No other step uses any guidance of Φ: not the margin, closedness, admissibility, KKM, (C) or (FC).

**Strict (G) on the zero set.** Take an improvement supported on a set where φ_i is flat, for instance a bad~silence zero. It has Φ_i = 0 and Ψ_i < 0, so it is rejected; its reverse has Φ_i = 0 and Ψ_i > 0, so it is accepted. This is §1.1 with Φ_i(t) = 0. The ties of Φ are ties of the **auxiliary** score only. The final relation separates them strictly, through Ψ (BRIEF30 correction 4: confirmed).

### 2.9 II1 Thm 2.4 and 4.1; II2 Thm 2.1 and Cor 2.3–2.4. Correct (CHECKED line by line)

- **II2 Thm 2.1.** Step 1 shows Φ_i(t_n) ≤ B/r → 0 at every active world, and Ψ_i(t_n) < 0 wherever Φ_i(t_n) ≥ 0. Steps 2–3 are §2.1, steps 3–5. Its third bullet follows by taking limits. Correct, and it uses no guidance.
- **II2 Cor 2.3.** This is §2.1 in non-quantitative form. (SLP) is literally (NT).
- **II2 Cor 2.4.** Its undominatedness proof is §2.4, in the direct form. Its (C) proof is §2.6. Correct.
- **II1 Thm 2.4** (under (A1), (A2), (RB)). Step 4 uses HH1 Prop 1(b) once and (A2) twice, in the right order. Correct.
- **II1 Thm 4.1.** "(NT) makes (ND) vacuous" is correct in the relaxed form. The equivalence between relaxed and actual records (Lemma 1.1(a)) must include the size coordinate f_0 = 1[b ≠ C_p(h)]. It does, because the lemma allows finitely many integrable functions.
- **II2 Cor 2.2** excludes only the special adversary, as AUDIT_II says. That is consistent with the above.

---

## 3. II1 Prop 5.1 and Prop 5.2, at the level of logic and imports

### 3.1 Prop 5.1 (no (NT) design on M_U). Correct, modulo imports (CHECKED)

- **Step 1.** On M_U each pair meeting U has exactly two available advices. If φ_k(h, right) = φ_k(h, wrong) on a non-null Z, then switching C_{e_k} on Z gives a different model with the same Φ_k. That contradicts (NT) at e_k.
  - This argument does not even need C_{e_k} = B^k.
  - Weak guidance plus injectivity on a two-element advice range is strict guidance. Pairs on which every evaluable model gives no advice need nothing.
- **Step 2.** Φ alone is a strictly guiding additive ranking with integrable envelope. It satisfies every axiom:
  - (G) and (IB);
  - competitiveness: a rival strictly cheaper at every world of supp p would violate (NT);
  - closed sections, by continuity;
  - undominatedness, by (NT);
  - (C): the write-up's Theorem kkm, valid for preorders, gives C ≈ C_p, and (NT) then gives C = C_p and X = C_p;
  - (LF) with N = U, and T1 = C_{q₀}.
- **Step 3.** Cor coverage applies (M_U is non-adjacent). Its status is: refereed twice (N18, N20). The logic is correct.

### 3.2 Prop 5.2 (the shape of Φ on the full domain). Correct, modulo Theorem gm (CHECKED)

- **(a) Strict-best.** (NT) at e_k makes C_{e_k} the unique model with Φ_k ≤ Φ_k(C_{e_k}). B^k is pointwise φ_k-minimal by weak guidance, so C_{e_k} = B^k a.e. (B^k agrees a.e. with D_{{e_k}}, so it is coherent.) An equality φ_k(h, b) = φ_k(h, best_k) on a non-null set would allow a switch of B^k that keeps Φ_k. Correct.
- **(b) The replacement φ_k(h, ×) ↦ max_a φ_k(h, a) + |h_k|.**
  - It preserves integrability (|h_k| is Gaussian-integrable) and weak guidance.
  - It leaves Φ(C_p) unchanged: coherent models never give ×, a.e.
  - It preserves (NT): Φ_J(Y) ≤ Φ′_J(Y) ≤ Φ′_J(C_p) = Φ_J(C_p).
  - **Reading note.** The statement "the only zeros are bad~silence" is about the **normalised** field Φ′. The original Φ may also have bad~× ties. These are irrelevant to the existence question, but BRIEF30's sentence "every zero of Φ must be a silence~bad tie" should read "after the WLOG normalisation of ×".
- **(c) Non-null zero set.** If every Z_k is null, then Φ′ is strictly guiding a.e.: the four advices are strictly ordered at each world. Step 2 of Prop 5.1, run on the full domain, makes Φ′ an additive cover of T1, which Theorem gm excludes. Status: Theorem gm, three routes. The logic is correct.
- **Prop 4.2.** I read it at the level of logic. Items (a)–(c) and (e) are correct, given 5.2(a) and C_{e_j} = B^j. Item (d) is a correct conditional. It is not used by the lifting theorem.

### 3.3 BRIEF30's elementary necessary condition. Correct (PROVED)

Let T1 = C_{q₀} with supp q₀ = Ω (II1 Prop 5.3(b)). Let T1 be silent on a non-null set Z of pairs with sign pattern (+, −, −).
- **Switching Z to "accept h".** This is world-1-improving, so Φ_1 ≤ 0 by weak guidance. (NT) then needs Φ_2 > 0 or Φ_3 > 0 for the switch on every non-null subset of Z.
  - Pointwise: for a.e. h ∈ Z, φ_2(h, M) > φ_2(h, S) or φ_3(h, M) > φ_3(h, S).
  - Otherwise take the non-null subset on which both are equalities.
  - So the silence~bad tie cannot sit at both world 2 and world 3.
- **Switching to "accept −h".** This improves worlds 2 and 3, so it forces φ_1(h, O) > φ_1(h, S) a.e. on Z. There is no tie at world 1.

The same argument applies to every selected model on its silence set, with the worlds of its support in place of Ω.

---

## 4. Remarks for the constructor and the write-up

### 4.1 Certificates for (NT) (PROVED)

**Sufficient: unique Bayes optimality at some weight supported inside supp p.** Suppose C_p is the a.e.-unique pointwise w-Bayes model of φ, and supp w ⊆ supp p. Inclusion is enough; the audit's "=" is not needed.

*Proof.* Let Φ_J(X) ≤ Φ_J(C_p). Then w·Φ(X) ≤ w·Φ(C_p). By decomposability, pointwise uniqueness makes C_p the unique minimiser of w·Φ, so X = C_p a.e.

**Not necessary.** Take one index with two active worlds. Let the increment vectors of the arrows out of C_p be:
- (1, −1) on a non-null set A;
- (−1, 1+ε) on non-null sets B_ε, ε ∈ (0, 1];
- together with other strictly w-positive arrows, for w = (½, ½).

The sign patterns are those of weakly (even strictly) guiding penalties on pairs with h_1 > 0 > h_2 and C_p silent there.
- **Only w = (½, ½) supports.** Every supporting weight must satisfy w_2(1+ε) ≥ w_1 for all ε, and w_1 ≥ w_2.
- **That weight is not unique Bayes.** w·(1, −1) = 0 on A.
- **(NT) holds.** If a non-negative combination of increments is ≤ 0, then its w-value is ≤ 0. Every term except the A-term has a strictly positive w-value. So all other coefficients vanish, ∫ε b_ε = 0, and then a(1, −1) ≤ 0 forces a = 0.

`checks.py` (3) checks the planar geometry exactly. So **(NT) is genuinely weaker than any single-weight uniqueness certificate.** BRIEF30's instruction not to replace (NT) by uniqueness at one weighting is right, and the gap is real. (Coherence and continuity of such a selection are not addressed by this remark.)

### 4.2 Scope of the theorem (PROVED by inspection of §§1–2)

The proof uses none of the following:
- three worlds (any finite Ω works, for KKM);
- the shape of T1 or ε;
- non-adjacency;
- symmetry, continuity or injectivity of anything beyond continuity in measure of the selection;
- full-dimensional credal sets;
- divergence of k.

**T1 enters only through C_{q₀} = D_{T1} and (LF) at T1.** So the theorem is a general lifting principle. For every coherent target D lying on a protected continuous coherent selection of a weakly guiding integrable additive field, on a decomposable domain with (LF) at D, there is a strict-guidance (IB) (FC) cover of D.

Its hypotheses are satisfiable in general. Take the linear payoff penalties φ_i(g, +) = −g_i, φ_i(g, 0) = 0, φ_i(g, −) = g_i, with × set to the maximum plus |g_i|. The precise Bayes selection p ↦ D_{{p}} is then coherent, continuous in measure and (NT) by §4.1. In this example Φ is strictly guiding, so lifting is redundant. **Whether the hypotheses can be met through T1 is exactly P_w.**

### 4.3 What the theorem reduces the T1 question to, in one sentence

Within this subclass, a strict-guidance (FC) cover of T1 exists as soon as there is a **weakly guiding** additive cover of T1 (that is, a cover in every respect except the strict half of (G)) whose selection is protected in the strong sense (NT). (NT) is strictly stronger than undominatedness of the selected models in Φ. It excludes:
- Φ-ties;
- rivals that are weakly Φ-better at every active world.

Rivals that are Φ-better at the active worlds and worse at an inactive one are excluded as well.

---

## 5. Final verdict

**The lifting theorem: PROVED**, with the closed-sections repair of §1.4. Its exact hypotheses are:
- (H0) Ω finite (three worlds here). The domain 𝓜 is decomposable, with (LF) at D_{T1}. The full four-advice domain is the case of interest, since on M_U the hypotheses are unsatisfiable (II1 Prop 5.1).
- (H1) φ = (φ_i) is additive, with integrable envelope, and **weakly** guiding.
- (H2) p ↦ C_p ∈ 𝓜 is a map of coherent models on Δ. It is continuous in measure and passes through T1: C_{q₀} = D_{T1} for some q₀.
- (H3) (NT): for every p ∈ Δ, every evaluable X with Φ_i(X) ≤ Φ_i(C_p) for all i ∈ supp p equals C_p a.e.
- (H4) ψ = (ψ_i) is additive, with integrable envelope, and **strictly** guiding. It is otherwise arbitrary.

**Conclusion.** c(a) > 0 on (0, M]. Every continuous k ≥ B/c on (0, M] makes the rate system 𝒜^k satisfy:
- reflexivity, (IB), strict (G), (FC) with ordering extension L;
- closed sections for every evaluable model;
- competitiveness of every C_p on supp p;
- every C_p undominated, hence (S) and (LA), with T1 ∈ C_L;
- direct (C), with U_L = C_L = Σ;
- (LF) at T1.

Hence 𝒜^k is a full (FC) cover of T1. Such a k exists, for instance the average formula in §2.2.

**It is a sufficient condition, not an equivalence.** The non-(NT) tie designs remain open (II1 §6; II2 (★), §3), as AUDIT_II says. For T1, satisfiability of (H1)–(H3) is the open problem P_w.

---

## 6. Clean statement and proof sketch for the write-up

Following the author's convention, the theorem environment carries no name.

```latex
\begin{theorem}\label{thm:lift}
Let $\M$ be a decomposable domain with (LF) at $D_{T_1}$. Let $\varphi=(\varphi_i)$ and
$\psi=(\psi_i)$ be additive penalties on $\M$ with integrable envelopes, $\varphi$ weakly
guiding and $\psi$ strictly guiding; write $\Phi_i,\Psi_i$ for the induced costs and,
for a record $t=\operatorname{rec}(X,Y)$, $\Phi_i(t)\coloneqq\Phi_i(Y)-\Phi_i(X)$,
$\Psi_i(t)$ likewise, and $m(t)\coloneqq\mu(\supp t)$. Let $p\mapsto C_p$ be a map from
$\Delta$ to the coherent members of $\M$, continuous in measure, with $C_{q_0}=D_{T_1}$
for some $q_0$, and such that for every $p\in\Delta$
\[
X\in\M,\ \Phi_i(X)\le\Phi_i(C_p)\ \text{for all } i\in\supp p\ \Longrightarrow\ X=C_p\ \text{a.e.}
\tag{NT}
\]
Then there is a continuous $k:(0,\mu(H)]\to(0,\infty)$ such that the relations
$X\preceq_iY\iff t\coloneqq\operatorname{rec}(X,Y)$ is the identity or
$\Phi_i(t)\ge0$ and $\Psi_i(t)+k(m(t))\Phi_i(t)\ge0$ are reflexive and satisfy (FC),
strict (G), (IB), (S) with this selection, (LA), direct (C) and (LF), and every undominated
model is a selected model. In particular they cover $T_1$.
\end{theorem}
```

**Proof sketch.** Proved here (JJ1), assembling HH2 Prop 6.1, II1 Thm 4.1, II2 Cor 2.3–2.4 and the criterion of AUDIT_HH_rate.

1. **Rate rule.** The verdict depends only on the record, so (IB) holds. Weak guidance of φ and strict guidance of ψ give strict (G), including on the zero set of φ. Every accepted record is accepted by the lexicographic preorder of (Φ_i, Ψ_i), and strict acceptances stay strict there. So that preorder is an ordering extension, and (FC) follows. Ties are exactly the records with Φ_i = Ψ_i = 0.
2. **Margin.** Put c(a) := inf max_{i∈supp p}[Φ_i(X) − Φ_i(C_p)] over all p and all X with m(rec(C_p, X)) ≥ a. Suppose c(a) = 0, and take a minimising sequence with p_n → p*. Since supp p* ⊆ supp p_n, it controls the worlds of supp p*.
   - Replacing C_{p_n} by C_{p*} changes every increment and the size by o(1), uniformly in X.
   - The set of (size, increment) vectors of records out of C_{p*} is compact, and every point is realised by an evaluable model (Lyapunov–Aumann, decomposability).
   - A limit point therefore gives X* ≠ C_{p*}, of size ≥ a, with Φ_i(X*) ≤ Φ_i(C_{p*}) on supp p*. This contradicts (NT).

   So c > 0. With B := 2 max_i ∫ envelope, every competitor of size ≥ a is defended at a world with Φ_i ≥ c(a) at a rate ≤ B/c(a). Take any continuous k ≥ B/c, for instance k(m) = (2/m) ∫_{m/2}^{m} B/c(s) ds.
3. **Selection.** Competitiveness on supp p follows from step 2. Sections {p : C_p ≼_i X} are closed:
   - where rec(C_p, X) has size 0, by reflexivity;
   - elsewhere, by continuity of the increments, the size and k.
4. **Admissibility and (C).** A model weakly dominating C_p has Φ_i ≤ Φ_i(C_p) on supp p, so (NT) makes it C_p. Hence every C_p, and in particular D_{T1}, is coherent and undominated.
   - The KKM lemma needs only closed sections and competitiveness, not transitivity. It gives, for any undominated B, a p with B ≼_i C_p at every world. So B = C_p by (NT).
   - Thus U_L = C_L = Σ, and a model tied with C_p everywhere equals C_p. This gives direct (C).
   - (LF) is a hypothesis on the domain. ∎

Suggested `\status` line: "proved (JJ1, one reader), assembling \src{HH2} Prop. 6.1 with the closed-section repair of JJ1 §1.4, \src{II1} Thm. 4.1 and \src{II2} Cor. 2.3–2.4. It is a sufficient condition. Its hypotheses are unsatisfiable on $\M_U$ (\src{II1} Prop. 5.1). Whether they can be met through $T_1$ on the full domain is open (P_w)."

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| §1.1–1.3 | HH2 6.1(a)–(c): reflexive, (IB), strict (G), (FC) via L, ties = lex ties | PROVED; CHECKED (`checks.py` (1)) |
| §1.4 | HH2 6.1(d) closed sections; repair of the non-injective case | PROVED |
| §2.1 | margin c(a) > 0 under (NT): boundary supports, transfer, purification with size coordinate; hence (RB) with bound B/c(a) | PROVED |
| §2.2 | (RB) ⇒ continuous k (audit), and the closed form k = (2/m)∫_{m/2}^m B/c | PROVED; CHECKED (`checks.py` (2)) |
| §2.3–2.7 | competitiveness, undominatedness (direct from (NT)), KKM without transitivity, direct (C), U_L = C_L = Σ, (LF) | PROVED |
| §2.8 | weak guidance of Φ suffices and is necessary for (G) of the rate rule; strict (G) on Φ's zero set | PROVED |
| §2.9 | II1 Thm 2.4, 3.2 (under (NT)), 4.1; II2 Thm 2.1, Cor 2.3, 2.4 | CHECKED (correct) |
| §3.1 | II1 Prop 5.1 | CHECKED, modulo Theorem main / Cor coverage |
| §3.2 | II1 Prop 5.2 (zero statement after normalising ×); Prop 4.2 | CHECKED, (c) modulo Theorem gm |
| §3.3 | BRIEF30 elementary necessary condition | PROVED |
| §4.1 | unique w-Bayes with supp w ⊆ supp p ⇒ (NT); not conversely | PROVED; CHECKED geometry (`checks.py` (3)) |
| §4.2 | scope: any finite Ω, any coherent selected target with (LF); hypotheses satisfiable in general (precise Bayes family) | PROVED |
| **Lifting theorem** | (H0)–(H4) ⇒ full (FC) cover of T1, for every strictly guiding integrable Ψ | **PROVED** (sufficient, not necessary) |
| P_w | existence of (H1)–(H3) through T1 on the full domain | open |

## 8. Files

`jj1py/checks.py` → `jj1py/checks.out`. It checks:
- (1) the rate-world algebra on 200 000 exact rational records;
- (2) the dyadic and averaged rate majorants against a discontinuous nonincreasing bound;
- (3) the planar instance showing that (NT) does not imply a unique supporting weight.
