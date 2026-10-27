# REF64_es — Referee report on ES64_notes.md (25 Oct 2026)

Referee: REF64_es. Standard: journal-level rigour. I checked every step myself, by hand, and I re-ran ES64's exact scripts. I also wrote independent scripts.

Framework: BRIEF64's binding framework and AUDIT_r64. That is:
- reflexivity, a.e.-identification and (TC);
- strict (G) and (IB) as in W62 §2;
- the cover requirements: global coherence, direct (C), target undominated, incoherent-model dominance, (LF).

Transitivity, (TP) and completeness are **not** assumed.

Labels: PROVED / CHECKED (exact computation) / CONJECTURE / NUMERICS. Results marked "referee" are new here and have not been refereed.

Scripts are in `ref64es_py/`. Run each with `python3 -I <script>` from that folder; each has an `.out` file.
- `xcone.py`: an **independent** re-implementation of exact cone moments under e^{−|h|₁}. It reproduces ES64's m(N∖D_K) = 0.0287955708·𝟙 exactly.
- `atoms.py` → `atoms.out`: the deletion relation Δ(𝒩) on 8 atoms (256 models), for 7 families 𝒩. Checked exhaustively:
  - reflexivity, strict (G), (TC), finite-chain consistency, protection;
  - "(★) ⟺ undominated = 𝒩 with 𝒩-dominance of the rest", for each family and model by model.
  - (Add) and (TP) failures are counted; the (Add) count uses sampled record pairs.
- `add_fail.py` → `add_fail.out`: an exact failure of disjoint additivity in Δ(𝒩) on the reversed triangle.
- `midpiece.py` → `midpiece.out`: an exact (H) certificate for an E61-type collar trade near the face midpoints. This is the case ES64's Prop 5.6 misses.
- `t1_recheck.py` → `t1_recheck.out`: a strict re-check of the two printed T1 certificates.
- `rerun/`: ES64's `prop56`, `bump`, `t1c`, `pi_dk` and `collar`, re-run. `bump`, `t1c` and `collar` are byte-identical. `prop56` is identical apart from the lines it prints when it imports `bump.py`. `pi_dk` now defaults to a 1/40 grid; see E16.

---

## 0. Summary verdict

**The central mathematics of ES64 is correct.**
- The deletion lemma (Lemma 1.3) is correct.
- Theorem 3.2 is correct in full: the axioms, protection, and the reduction of the cover to (★).
- The equivalence of (★), for 𝒩 = all coherent models, with (H) is correct. ES64 proves one direction; I prove the other (§2.5).

So, under the binding framework:
- **target protection is free**: any family of coherent models can be made immune to weak dominance;
- **if (H) holds, one ranking covers every K with K′ ⊆ relint K.** In that ranking, every coherent model is undominated and every incoherent model is dominated by a coherent one.

(H) is honestly labelled CONJECTURE. I found no counterexample. I prove two further cases (§3.3, referee Props R1 and R2): small holes inside a Bayes act, and small bumps outside one, when kept away from its boundary.

Errors and gaps found:
- **GAP, overclaim (E26).** ES64 says Prop 5.6 "includes E61's collar trades". It does not. E61's pieces sit near the face midpoints, and Prop 5.6 needs mass in the box corners, at lateral offset ≥ 0.096. Repair: a different defender, whose boundary crosses the piece. CHECKED exactly (`midpiece.out`).
- **GAP, Lemmas 4.1 and 4.3 are not sharp (E18, E20).** Their escape clauses ("unless the attacked copy is coherent"; "or N∖P is coherent and tied with D_K") can never occur. By (IB), a dominance record never applies to an undominated model (OR64 Prop 3.1 and Lemma T). Repair: state OR64's T1, μ(P∖N) > 0 always.
- **Minor.**
  - The ledger sentence on E61 Cor 5.3 says it uses priority regions "via (TP)" (E9). REF64_or C10 shows its regions are strong, so (TP) is not needed there.
  - Lemma 5.3's section form needs normalisation (E24).
  - Two wording points (E21, E30).
  - A grid-dependent number in a background line (E16).

**Point 6 (§5) is the important finding for the author.** Three facts:
- Protection-for-free survives the auditor's stronger "finite-chain consistency" (AUDIT_nontransitive). Δ(𝒩) is Suzumura-consistent, because Brier is an ordering extension of it.
- Δ(𝒩) is excluded by (TP), by transitivity, and by a weaker closure condition, **disjoint additivity (Add)** (CHECKED exactly). (Add) holds in every score-generated construction of the paper.
- (Add) also excludes both of OR64's round-64 (TC) diagnostics, M1 and 𝒯.

---

## 1. Verdict table

| # | ES64 claim | Verdict | Note / repair |
|---|---|---|---|
| E1 | Lemma 1.1: (IB) ⟺ record relations | CORRECT | Same as OR64 Prop 1.1 (refereed CORRECT). |
| E2 | Lemma 1.2: (TC) ⟺ 3-cycle reversal closure | CORRECT | Both directions checked; repeated models are harmless. |
| E3 | **Lemma 1.3, the deletion lemma** | **CORRECT** | The proof is complete, including Brier ties (§2.1). *Strengthening (referee, PROVED):* the same hypotheses give **finite-chain (Suzumura) consistency**, A₀ ⪯ ⋯ ⪯ A_k ⇒ ¬(A_k ≺ A₀). They are exactly "the relation has an ordering extension that preserves strict comparisons", which is the easy half of Suzumura's extension theorem (Suzumura 1976). |
| E4 | Lemma 2.1: strong priority ⇒ box lemma, strict (G) only | CORRECT | Same as OR64 Lemma 2.2. |
| E5 | Lemma 2.2: E61-priority + (TC) ⇒ the dominator is incomparable with M_R | CORRECT | X_i ⪯_j M_R is guided (X_i∖M_R ⊆ pos_j, M_R∖X_i ⊆ neg_j). Then (TC) and Y ⋠_j M_R give M_R ⋠_j Y. |
| E6 | Lemma 2.3: a pure-guidance world rules out every cover | CORRECT | Minor: incoherence of X_i follows directly. X_i is a cone minus a ball, hence not a.e. a cone. E61's convexity argument is not needed. |
| E7 | §2.4: explicit (TP) failure | CORRECT (CHECKED, re-run) | Needs: P₁ ⊆ pos₁ (exact); r(N, D_K∪P₁) attacks no coherent model (Prop 5.6 certificate, since P₁ = B₁ meets the corners); r(N, D_K) ∈ 𝓡 with i = 1, since N∖D_K meets neg₁ (mass 0.026, `add_fail.out`). |
| E8 | **Prop 2.5: Δ(𝒩) has no priority region, even in E61's weak sense** | **CORRECT** | The record contains int ℝ³₊, so it attacks no coherent model. It is strict at j, so it is not a tie-inverse. Valid for every family 𝒩. |
| E9 | §2 ledger paragraph | GAP (minor) | "E61 Cor 5.3 and Thm 5.1 use priority regions via (TP)": their regions are strong, so (TP) is not needed (REF64_or C10 and (LV)). The conclusion "none applies to Δ(𝒩)" stands, since those classes are transitive or view-generated. |
| E10 | Def 3.1 is well defined: the deletion world i(r) exists | CORRECT | i(r) is a function of the record, an a.e.-class, so no measurable selection is needed and (IB) is automatic. Existence: if r ∈ G_i at every world, then B ⊆ U ∩ (−int ℝ³₊) and A ⊆ int ℝ³₊; then B ⊆ N forces B null, and A ∩ N = ∅ with N ⊇ int ℝ³₊ forces A null. *Also valid on two-sided domains*, because a coherent N contains no all-negative gamble. |
| E11 | **Thm 3.2: reflexivity, a.e.-ties, strict (G), (IB), (TC)** | **CORRECT** | §2.2. Deletions never fall on a guided record at its own world, and tie-inverses are never guided (guided non-null records are Brier-strict). |
| E12 | **Thm 3.2(i): members of 𝒩 have no weak dominator** | **CORRECT** | This includes dominators that are Brier-tied at some or all worlds: r(Y,N) ∈ 𝓡 needs only m(Y) ≥ m(N), and it is deleted at i(r). CHECKED on atoms, 7 families. |
| E13 | **Thm 3.2(ii)–(iii) under (★)** | **CORRECT** | *Addition (referee, PROVED):* within Δ(𝒩), "X is dominated by a member of 𝒩" ⟺ "(★) holds at X" (§2.5). So (★) for incoherent X is necessary as well as sufficient for Δ(𝒩) to be a cover with C* = 𝒩. CHECKED model by model on atoms. |
| E14 | Thm 3.2(iv): D_K ∈ 𝒩 and (★) ⇒ cover of K | **CORRECT** | Every BRIEF64 requirement checked (§2.4). (LF) holds because K′ = (u+K)/2 ⊆ relint K. Remark: the brief allows Lebesgue μ, where Brier is infinite. The ranking may use any finite ν with the same null sets and a finite first moment, so (H) is needed for **one** such ν, not all. |
| E15 | Lemma 3.3: strictly improving records attack no Bayes act | CORRECT | Uses a.e.-uniqueness of the π-maximiser. Works for π on ∂Δ. |
| E16 | Prop 3.4 (𝒩 = ℬ ∪ {D_K} fails at X₁) | CHECKED on grid; general claim NUMERICS (honest) | Re-run identical (102/102 dominators contain P₁). Background line: "every π_k ≥ 0.267 on the 1/30 grid" is grid-dependent. On the 1/40 grid (the script's current default) the minimum is 0.25. Report it as a grid value only. |
| E17 | Cor 3.5: (H) ⇒ universal cover | **CORRECT** given (H) | *Addition:* the converse holds. Δ(all coherent) is a cover ⟺ (H) (§2.5). |
| E18 | Lemma 4.1 (protection transfer) | **GAP (not sharp; vacuous)** | Its hypotheses are inconsistent. If r = r(N,X) is a dominance record (accepted everywhere, its inverse refused at some j), then by (IB) N°⊕r dominates N°, so N° is not undominated. Correct statement (OR64 Prop 3.1 and Lemma T(a)): **a dominance record never applies to an undominated model.** The clause "unless the attacked copy is again coherent" should go. |
| E19 | Lemma 4.2 (collar refusal) | CORRECT | — |
| E20 | Lemma 4.3 (bump defender) | **GAP (not sharp)** | The second alternative is impossible, by E18. Correct statement: μ(P∖N) > 0 for every dominator N of D_K ∪ P (OR64 T1, refereed). |
| E21 | Remark (scope): Δ(𝒩) satisfies 4.1–4.3 | CORRECT, with wording | 4.1 holds vacuously. "(P,∅) is refused at world i(r)" holds when m(P) ≥ 0. Otherwise Brier itself refuses (P,∅) at a world where m_i(P) < 0. |
| E22 | **Lemma 5.1: every non-Bayes model is strictly dominated by a Bayes act** | **CORRECT** | Interior case: Pareto-maximal point, separation, a.e.-uniqueness. Boundary case: pointed normal cone, separation from ℝ³₊, and the standard fact int T_ℳ(x) = ∪_{t>0} t(int ℳ − x). Needs a finite first moment and no atoms (Lyapunov). |
| E23 | Lemma 5.2 (hull facts) | CORRECT | Q_B = {q : q·b ≥ 0 at density points of B}; bipolar; W62 Lemma D(b). Also B ⊆ hull(B) a.e., since ∂D_{Q_B} is null; this is used in §2.5. |
| E24 | Lemma 5.3 (point certificate) | CORRECT | Minor: the "section Σh = 1" form needs Σb_k > 0 (true for ES64's U, since K′ ∋ u), and "int conv" means relative interior in the plane. |
| E25 | Prop 5.4: (H) when X misses part of int ℝ³₊ | CORRECT | — |
| E26 | **Prop 5.6** (exact certificate) | CORRECT as stated; **GAP in the claim "this includes E61's collar trades"** | Re-run identical. The proof checks out: the sign pattern on the boxes; the Brier bound for every measurable P inside the boxes; the four strict linear checks at extreme rays, which extend to the cone; the open conditions for Lemma 5.3. **But** E61's collar pieces lie "near m_k", the face midpoints, at lateral offset ≈ 0 (E61 notes l.57; OR64 R1). They do not meet the corner cones (lateral ∈ ±[0.096, 0.1)), and for such P the defender D_{Q_{3/23}} contains P, so the certificate does not apply. *Repair (referee, CHECKED, `midpiece.out`):* choose t so that ∂D_{Q_t} crosses the piece; certify with corner points of P∖N next to ∂N (§3.4). |
| E27 | §5.5(i) T1 certificates | CORRECT (CHECKED) | Strict re-check passes (`t1_recheck.out`): explicit λ = (8/25, 127/200) and (67/200, 5/8). The "PROVED by Lemma 3.3" step (strict dominators cut both lobes) is correct. |
| E28 | §5.5(ii) random hunt | NUMERICS (honest) | Counts verified: 4 + 7 + 6 = 17 certified; 5 cases with no dominator found; 8 uncertified, with slacks 3.8·10⁻⁷ to 1.2·10⁻⁴. |
| E29 | **CONJECTURE H** | CONJECTURE (honest); OPEN | No counterexample found (§3). New proved cases: R1 and R2 (§3.3). An exact reformulation (§3.2) shows where a counterexample would have to live. |
| E30 | §0.7 / §4 Remark / §6.2: "any axiom-level impossibility must refute (★) for every 𝒩 ∋ D_K, in particular (H)" | CORRECT | Wording: a refutation of (H) is **necessary** for an impossibility proof, not sufficient. It excludes only the Brier-based universal construction. ES64 §6.2 says this; §4's "concrete target for OR64" should say so too. |
| E31 | §6.1: (TP), or a monotone closure of accepted records, would exclude Δ(𝒩) | CORRECT | Both exclude it. See §5 for what does **not** exclude it (finite-chain consistency) and for a weaker excluding condition (Add). |
| E32 | "Deliverable level (2), strong form" | CORRECT | Axioms everywhere: PROVED. Protection of every coherent model against every rival: PROVED. Global coherence and incoherent-model dominance ⟺ (H). Not a cover; ES64 does not claim one. |

---

## 2. Theorem 3.2 and the deletion lemma (brief points 1–4)

### 2.1 The deletion lemma (point 3)
Let φ be real on models, with (a) X ⪯ Y ⇒ φ(X) ≤ φ(Y), and (b) X ⪯ Y and φ(X) = φ(Y) ⇒ Y ⪯ X.
- By (b), X ≺ Y forces φ(X) < φ(Y). Otherwise φ(X) = φ(Y), and (b) gives Y ⪯ X.
- A ⪯ B ⪯ C gives φ(A) ≤ φ(C), so C ≺ A, which needs φ(C) < φ(A), is impossible.

The equal-score case is exactly (b). Nothing else is needed. ✓

*Chains (referee).* For A₀ ⪯ ⋯ ⪯ A_k, the same argument gives φ(A₀) ≤ φ(A_k), so ¬(A_k ≺ A₀). So (a) + (b) give **finite-chain consistency**.

*Converse.* A relation satisfies (a) + (b) for some complete preorder R* (with φ replaced by R*) iff it is Suzumura-consistent; that is Suzumura's theorem. So "deletions from a total preorder, symmetric on its ties" is exactly the class of finite-chain-consistent relations.

In Δ(𝒩), φ_i = −m_i, Acc_i ⊆ Br_i, and tie-symmetry holds (§2.2(d)).

### 2.2 The axioms (points 1 and 2)
- **(a) Reflexivity.** (∅,∅) ∈ Br_i. It is not in 𝓡, which contains only non-null records, and it is not a tie-inverse, since inverses of non-null records are non-null.
- **(b) (IB).** Acc_i is a set of records.
- **(c) Strict (G) (point 1).** Let r ∈ G_i be non-null. Then m_i(A) − m_i(B) = ∫_A h_i + ∫_B |h_i| > 0, since a.e. h_i ≠ 0 and the moment is finite. So r ∈ Br_i and r⁻¹ ∉ Br_i. r is not deleted at i:
  - i(r) is by definition a world where r ∉ G_{i(r)};
  - tie-inverses are ties at their world, and r is strict there.

  **The deletion world is always admissible** (E10). In the fallback case (no strict non-guided world), i(r) is a tie world, and both r and r⁻¹ are removed there. Neither is guided at that world.
- **(d) Tie-symmetry.** Let r ∈ Acc_i be a tie at i with r⁻¹ ∈ Del_i. Either r⁻¹ ∈ 𝓡 with i(r⁻¹) = i, and then r is deleted as its tie-inverse; or r⁻¹ is the tie-inverse of r ∈ 𝓡 with i(r) = i, and then r ∈ Del_i. Both contradict r ∈ Acc_i. ✓

**Point 2, (IB) consistency.**
- Deletions are defined on records, so they are context-free and well defined by construction. No pair (Y,N) "chooses" anything: i(r) depends only on r = r(Y,N).
- They remain tie-symmetric by (d).
- They never remove a guidance comparison, by (c).
- They never remove a defender's comparison r(N,X) in (★):
  - r(N,X) ∈ 𝓡 would require an attack on a member, which (★) excludes;
  - r(N,X) as a tie-inverse would require r(X,N) ∈ 𝓡, hence m(X) ≥ m(N), hence m(X) = m(N), which (★) excludes.
- **Is "attack" exactly what is needed?** Yes. In *every* cover, not only Δ(𝒩), a dominance record cannot apply to an undominated model (E18; OR64 Prop 3.1). In Δ(𝒩) the undominated set contains 𝒩, so the non-attack clause of (★) is forced. The Brier clause of (★) is forced too, within Δ(𝒩), since Acc_i ⊆ Br_i (§2.5).

### 2.3 Protection, Theorem 3.2(i)
- Let Y ⪯_i N at every world, with Y ≠ N a.e.
- Then m(Y) ≥ m(N), and r(Y,N) = (Y∖N, N∖Y) attacks N.
- So r(Y,N) ∈ 𝓡 and is missing from Acc_{i(r)}. Contradiction.

Brier ties at some or all worlds change nothing. **No member of 𝒩 has a weak dominator other than itself**, so direct (C) holds at members in the strong form "tied ⇒ equal". ✓

### 2.4 The cover (point 4)
Under (★), every X ∉ 𝒩 is dominated by a member of 𝒩 (ES64's (ii) is correct). Hence:
- the undominated models are exactly 𝒩, so **global coherence** holds;
- **incoherent-model dominance** holds, since an incoherent model is not in 𝒩;
- **direct (C)** holds, by §2.3;
- **(W)** holds.

With D_K ∈ 𝒩:
- **target undominated** holds;
- D_K ∈ ℳ_U, since K′ ⊆ K;
- **(LF)** holds: every h ∈ ∂D_K∖0 has m·h > 0 on relint K ⊇ K′, so U itself is the (LF) neighbourhood;
- the domain ℳ_{D_{K′}} is decomposable and one-sided.

Nothing more is needed: **D_K ∈ 𝒩 together with (★) suffices.** ✓

### 2.5 (★) is also necessary within Δ(𝒩) (referee, PROVED; CHECKED on atoms)
Claim: in Δ(𝒩), N ∈ 𝒩 dominates X ⟺ the triple (X, N) satisfies (★).

(⇒)
- N ⪯_i X at every world, so r(N,X) ∈ ∩ Br_i, that is, m(N) ≥ m(X).
- r(N,X) is not in 𝓡; otherwise it is deleted at i(r). Since m(N) ≥ m(X), this means it attacks no member.
- If m(N) = m(X), then r(N,X) is a tie at every world. By tie-symmetry its inverse is accepted at every world, and N does not dominate X.

(⇐) This is Theorem 3.2(ii).

*Consequence for 𝒩 = all coherent models.* A coherent N° = D_Q contains B a.e. iff Q ⊆ Q_B, iff D_Q ⊇ hull(B). Also hull(B) ⊇ B a.e. (E23). So r(N,X) attacks some coherent model iff hull(X∖N) ∩ (N∖X) is null. Hence:

**Δ(all coherent) is a cover ⟺ (H).** ✓

---

## 3. (H) (brief point 5)

### 3.1 The stated proofs
- **Models missing part of the positive orthant** (Prop 5.4): correct.
- **Every non-Bayes model is strictly dominated by a Bayes act** (Lemma 5.1): correct (E22). The boundary case is the delicate one, and it is handled correctly.
- **Thin-box collar class** (Prop 5.6): correct for the class stated, P inside the boxes with μ(P∩C) > 0 (E26).
  - The Brier bound uses the exact sign pattern on the boxes (h_k > 0 and h_j < 0 on B_k). I verified it in the re-run.
  - The corner condition is genuinely needed. y(p) = p + (s/9)(e₃ + ⋯) must leave the box laterally while staying beyond F₁ (depth ∈ [0.07, 0.09] against the shift 0.4·s/9 ≈ 0.044·s).
- **Labels.** CHECKED and NUMERICS are used honestly throughout, with two exceptions: the E61-inclusion sentence (E26) and the grid number in Prop 3.4's background line (E16).

### 3.2 An exact reformulation (referee, PROVED)
Assume U ⊆ {Σh > 0} (true for ES64's U, since u ∈ K′). For a non-null set Y put M(Y) := ∫_Y Σh dμ > 0 and c(Y) := m(Y)/M(Y). This is the Σh-weighted centroid of Y's directions, a point of the plane Σ = 1.

Write A := N∖X and B := X∖N. Then m(N) − m(X) ≥ 0, ≠ 0, holds iff
- M_A > M_B, and
- c_A ∈ θ c_B + (1−θ) Δ, with θ := M_B / M_A.

*Proof.* v := M_A c_A − M_B c_B ≥ 0 and v ≠ 0 give Σv = M_A − M_B > 0, and c_A = θ c_B + (1−θ) v/Σv, where v/Σv ∈ Δ. The converse is the same computation. ∎

So **the centroid of the added part always lies in cl conv(B ∪ Δ)**, the closed hull of the removed part (in the plane section). (H) asks for more: that the added part itself has positive measure inside hull(B).

A counterexample to (H) must therefore be an X such that, for *every* coherent Brier dominator N:
- the added part N∖X misses hull(X∖N),
- yet its centroid lies in it.

So N∖X must surround the hull from at least two sides. That is the precise shape of the obstruction to look for.

### 3.3 Two new proved classes (referee, PROVED)
Setting: U = D_{K′} with K′ ⊆ relint Δ compact and convex; μ finite, with positive density and finite first moment. Work in the affine section {k̄·h = 1}, k̄ ∈ relint K′. cl U is pointed, so lines map to lines and hull(B) ⊇ the cone over int conv(B̃_d) (Lemma 5.2).

**Prop R1 (small interior holes).** Let π ∈ Δ, and let Γ be a closed cone with Γ∖0 ⊆ N_π. There is η > 0 such that (H)'s conclusion holds at every X = N_π∖H with H ⊆ Γ measurable, μ(H) > 0 and ∫_H |h| dμ < η.

*Proof.*
1. **Strict dominators are close to π.** Let Π₀ := {π′ : N_{π′} = N_π}, a compact set. Put g(π′) := π·(m(N_π) − m(N_{π′})) = ∫_{N_π△N_{π′}} |π·h| dμ. It is continuous and vanishes exactly on Π₀.
   - Every strict Bayes dominator N_{π′} of X (one exists by Lemma 5.1, since X is not a Bayes act) has g(π′) < π·m(H) ≤ ∫_H |h| < η.
   - So π′ lies within δ(η) of Π₀, and δ(η) → 0 as η → 0.
   - By compactness of Π₀ × (Γ∩S²), with π″·h ≥ c > 0 there, we get Γ∖0 ⊆ N_{π′} for small η.
   - Strict dominators form an open set of π′, so we may take π′ ∈ relint Δ.
2. **Thin cuts.** Put q_j(τ) := (1+τ)k_j − τπ′ for the vertices k_j of a polytope containing K′ near its boundary (finitely many cut points suffice for a general K′), and q₀(τ) := (1+τ)π′ − τk̄. For small τ these lie in Δ.
   - Let N := N_{π′} ∩ ⋂{q·h > 0}. It is coherent, and S_τ := N_{π′}∖N is a union of thin wedges along every face of N_{π′}, with m(S_τ) → 0.
   - So N still strictly dominates X for small τ.
3. **Supports.** Put N′ := N_π ∩ N_{π′}, and let E := ∂Ñ′ ∩ ∂Ñ_{π′}.
   - Every point of E has, in each neighbourhood, a positive-measure part of S_τ ∩ N_π ∖ Γ ⊆ X∖N.
   - The rest of ∂Ñ′ is the segment L_π ∩ cl Ñ′, whose endpoints lie in E. Hence cl conv E = cl Ñ′.
4. **Hull.** Γ̃ is compact in int Ñ′. Every point of Γ̃ lies in the interior of the convex hull of finitely many points of E. Perturbing those points to density points of X∖N gives Γ∖0 ⊆ hull(X∖N).
5. **Conclusion.** H ⊆ N∖X, since H ⊆ Γ ⊆ N_{π′} and Γ misses S_τ for small τ. So μ((N∖X) ∩ hull(X∖N)) ≥ μ(H) > 0. ∎

**Prop R2 (small exterior bumps).** Let Γ′ be a closed cone with Γ′∖0 ⊆ U∖cl N_π. There is η > 0 such that (H)'s conclusion holds at X = N_π ∪ P for every measurable P ⊆ Γ′ with μ(P) > 0 and ∫_P |h| < η.

*Proof.*
1. **Close dominators miss P.** As in R1, every strict dominator N_{π′} has π′ near Π₀, so P ∩ N_{π′} = ∅.
2. **The gained part is non-null.** W⁺ := N_{π′}∖N_π is non-null. Otherwise k·(m(N_{π′}) − m(X)) = −∫_{(N_π∖N_{π′})∪P} k·h < 0 for k ∈ K′, contradicting strict dominance.
3. **The triangle.** In the section, let J̄ = [a, b] be the closure of the part of the chord L_π ∩ cl Ũ on which π′ > 0. Take π′ generic, so that a and b are each either a chord endpoint on ∂Ũ or the hinge L_π ∩ L_{π′}. For a density point p of P, the triangle T = conv(p, a, b) is non-degenerate, because π·p < 0. Near the midpoint of J, an open set O ⊆ W̃⁺ lies in int T and away from P̃.
4. **Supports at a and b.**
   - At the hinge: the lost wedge N_π∖N_{π′} ⊆ X∖N.
   - At a chord endpoint on the U-face of k* ∈ K′: one thin cut q = (1+τ)k* − τπ′ produces positive-measure parts of X∖N in every neighbourhood.
5. **Conclusion.** N := N_{π′} with these cuts still strictly dominates for small τ. O ⊆ N∖X, and O ⊆ int conv(density points of X∖N near p, a, b) ⊆ hull(X∖N). ∎

Scope of R1 and R2:
- They cover "deep holes far from every face" when the holes are small relative to their distance from ∂N_π. ES64 flagged this as delicate. The reason it works: the thin-shell cut costs arbitrarily little Brier, while its hull is the whole of N_π ∩ N_{π′}.
- They do **not** cover:
  - defects touching ∂N_π;
  - defects comparable in size to the slack;
  - perturbations of non-Bayes coherent models, such as the collar rivals D_K ∪ P (Prop 5.6 and §3.4 below treat instances of these).

### 3.4 E61-type collar trades at the face midpoints (repair of E26; CHECKED, `midpiece.out`)
Data:
- P₁ := {lateral ∈ (−1/50, 1/50), depth ∈ (1/100, 1/20)} beyond F₁, inside U; P₂ and P₃ by permutation.
- Defender N := D_{Q_t}, with t = 42453/500000 chosen so that ∂N crosses P₁ at depth ≈ 3/100.

Exact results:
- m(N) − m(D_K ∪ P₁) = (0.01686, 0.01986, 0.01986) ≫ 0.
- m(N) − m(D_K ∪ P₁∪P₂∪P₃) = 0.01813·𝟙 ≫ 0.
- Corner cone C* = {lateral ∈ [0.018, 0.02], depth ∈ [0.0310, 0.0350]}. It lies in cl P₁ and outside N.
- y(p) := p + (1/50)s(p)(e₃ + (e₁+e₂)/1000). At all four extreme rays: y ∈ N; v₁·y < 0; lateral(y) > 1/50; v₂·y > 0 and v₃·y > 0. So Lemma 5.3 applies: **(H) holds at this collar trade.**

The mechanism is general: choose the shrink so that the defender's boundary straddles the piece, then push corner points of P∖N laterally into N. This needs a piece of positive depth and small lateral width. The Brier slack m(D_{Q_t}∖D_K) = c(t)·𝟙, with c(t) > 0 for every t by permutation symmetry, pays for any sufficiently small piece.

### 3.5 Counterexample search: outcome
I tried the following, analytically or semi-analytically:
- two-world analogues: angular holes and slivers;
- holes and notches at the boundary of Bayes acts;
- strips along a U-face with a dent;
- unions of Bayes acts;
- nested coherent cones with bumps.

In every case a defender was found: a Bayes tilt plus thin cuts, a shrink that straddles the defect, or a cut through the defect.

**No counterexample to (H) is known, and no general proof.**
- By §3.2, a counterexample must keep the added part of every coherent dominator outside the removed part's hull while its centroid lies inside.
- By R1, R2 and §3.4, the defects must touch the boundary of every near-optimal dominator, or be large relative to the slack.

(H) remains CONJECTURE.

---

## 4. E61 audit claims and §4 ordinal lemmas (brief point 7)
- **§2.1–2.3.** All correct (E4–E6). They agree with OR64 and REF64_or.
- **§2.4.** Correct, CHECKED (E7). Without (TP), a composite of an accepted record and a guided record need not be accepted.
- **Prop 2.5.** Correct for every 𝒩 (E8). Δ(𝒩) has no priority region in any of the three senses (E61, strong, strict). So it lies outside every class to which E61 Lemma 3.4, O61 Thm A or IN63 Thm C applies, which is consistent with OR64 Cor OC.
- **"The necessary ordinal lemmas of §4 all hold in Δ(𝒩)".** True, but 4.1 holds only vacuously and 4.3 in its weak form (E18, E20).
  - The sharp necessary facts are OR64's Prop 3.1 / Lemma T (a dominance record never applies to an undominated model) and T1 (μ(P∖N) > 0).
  - Δ(𝒩) satisfies both under (★), by Theorem 3.2: dominance records attack no member of 𝒩.
  - It also satisfies Lemma OC wherever (★) holds at the dented boxes. R1 gives (H) for small dented boxes B_i∖R, since B_i = N_{e_i} and R lies in a closed cone inside N_{e_i}. Its defender meets R, as Lemma OC(a) requires.

---

## 5. Point 6 — what this shows about the binding framework (separate section)

### 5.1 What is proved without (H)
**Theorem (ES64 Thm 3.2(i), verified; strengthened here).** Under the binding framework, let 𝒩 be any family of coherent models. Then there are relations satisfying:
- reflexivity, a.e.-ties, strict (G), (IB), (TC);
- **and** finite-chain consistency;

under which no member of 𝒩 has a weak dominator. Each relation is a sub-relation of the Brier order: every comparison it makes agrees with Brier.

Hence, in the binding framework:
- "D_K undominated" and "every coherent model is protected" carry **no information at all**;
- direct (C) at members is automatic;
- **the whole content of a cover lies in the dominance half**: global coherence, plus incoherent-model dominance by records that attack no undominated model.

This holds for every target, the reversed triangle included.

### 5.2 What follows if (H) holds
One ranking, Δ(all coherent), would make the undominated models exactly the coherent ones, for every K with K′ ⊆ relint K at once. The complete-class statement "undominated ⟺ coherent" would hold for a single admissible ranking, and the covering question would become trivial. No axiom-level impossibility (OR64's criterion (A)) could exist for any target.

This does not conflict with OR64 as refereed:
- **Prop K** says (A) would settle the chart problem negatively. Δ(𝒩) is incomplete, so it is not a chart and says nothing about that problem.
- **Theorem VA** requires (VA2), acceptance of improving collar trades. Δ(𝒩) refuses each such trade at the world i(r), so (VA) fails, as it must.
- **Lemma OC and T1** are satisfied (§4).
- **𝒯** is a different diagnostic.

### 5.3 The construction is degenerate in ways the axioms do not exclude
1. **Coherence-informed accuracy.** Whether world i compares Y with N depends on whether the record attacks a *coherent* model. So the accuracy ranking is defined using the notion of coherence it is supposed to vindicate. For an accuracy-dominance justification of coherence this is circular. The axioms cannot see it: (IB) requires dependence on the record only, and "attacks some D_Q" is a property of the record.
2. **Cross-world verdicts.** A comparison at world i is removed because the record improves Brier at *other* worlds. Note, however, that W62's veto–Brier rankings also use cross-world information (vetoes in v·h), so "world-locality" cannot be the remedy without losing the positive theorems.
3. **Failure of non-cancelling composition.** CHECKED exactly (`add_fail.out`). Take N = D_{Q_{3/23}} and split N∖D_K = S₁ ⊔ S₂, with
   - m(S₁) = (0.02853, 0.04139, −0.01989),
   - m(S₂) = (0.00026, −0.01259, 0.04868).

   Both (S₁,∅) and (S₂,∅) are accepted at world 1: they are Brier-positive there and never deleted, since each has a negative coordinate. Their disjoint union (N∖D_K, ∅) is deleted at world 1.

   In models: N ⪯₁ D_K ∪ S₂ ⪯₁ D_K, with steps of disjoint support, yet N ⋠₁ D_K. Unlike §2.4, neither step is a guidance step.

### 5.4 Which condition excludes it
| Condition | Excludes Δ(𝒩)? | Status |
|---|---|---|
| (TC) (three-model consistency) | No | ES64 Thm 3.2 (PROVED) |
| **Finite-chain consistency** (AUDIT_nontransitive, option 2) | **No** | PROVED (§2.1: Brier is an ordering extension); CHECKED on atoms (FCC holds in all 7 families) |
| Acyclicity of the strict part, and any other condition implied by Suzumura consistency | No | Same reason |
| "Deletions context-free in a stronger sense" | No useful version | The deletions are already record-level (context-free). The degeneracy is in *which* records are refused, not in context-dependence. |
| (TP): Y ⪯ X and X pointwise at least as good as M ⇒ Y ⪯ M | Yes | §2.4 (CHECKED); thousands of (TP) failures on atoms |
| Transitivity of each ⪯_i | Yes | Implied by the above |
| **(Add) disjoint additivity**: r₁, r₂ ∈ Acc_i with disjoint supports ⇒ r₁ ⊔ r₂ ∈ Acc_i | **Yes** | CHECKED exactly (§5.3(3)) |

Remarks on (Add):
- Under (IB), (Add) ⟺ **transitivity along non-overlapping chains**: X ⪯ Y ⪯ Z with (X△Y) ∩ (Y△Z) = ∅ ⇒ X ⪯ Z. Realise disjoint records (A₁,B₁), (A₂,B₂) by X = A₁∪A₂, Y = B₁∪A₂, Z = B₁∪B₂.
- (Add) is implied by transitivity, and it is satisfied by every integral, lexicographic-integral or view-unanimity construction in the paper: veto–Brier, orthant-planar charts, composition. A sum of lexicographically non-positive vectors is lexicographically non-positive.
- (Add) also **excludes OR64's round-64 diagnostics**, both by direct arguments:
  - **M1:** r₀ ⊔ g, for a guided g disjoint from r₀, is neither guided nor r₀.
  - **𝒯:** (F₁, N₁) with F₁ ⊆ D_K ∩ neg_w and N₁ ⊆ OUT ∩ neg_w lies in T_w, and (P₂, ∅) with P₂ ⊆ OUT ∩ pos_w is guided. Their union lies neither in T_w (P₂ ⊄ D_K) nor in G_w (F₁ ⊄ pos_w).

  So OR64's two "(TC)-only" conclusions are both specific to frameworks without (Add): the failure of E61's box lemma (M1), and the localisation of any proof to the one-world improvements 𝓘 (𝒯).

**Assessment.** The binding framework is too weak for coverage to be a substantive accuracy question. Even without (H), it gives protection for free; with (H), it gives a universal cover. The natural repair is a *closure* condition on accepted records, not a context condition.

(Add) is the weakest candidate that excludes every round-64 escape (Δ(𝒩), M1, 𝒯) while keeping all positive theorems. (TP) is the other natural candidate.

**Whether (G) + (IB) + (TC) + (Add), or + (TP), still admit protection-for-free or a cover of the reversed triangle is OPEN.** I recommend it as the round-65 question. The first sub-question: does a (TP)-closed or (Add)-closed variant of Δ(𝒩) exist, with deletions propagated to all records that compose to a deleted one?

---

## 6. Recommendations
1. Accept as refereed:
   - Lemma 1.3 and Theorem 3.2 (with E13/E17: (★) is necessary and sufficient within Δ(𝒩); Δ(all coherent) is a cover ⟺ (H));
   - Lemmas 2.1–2.3, Prop 2.5, Lemma 3.3, Lemma 5.1–5.3, Prop 5.4;
   - Prop 5.6 for its stated class.
2. Correct:
   - E26: "includes E61's collar trades". Replace with "includes the full boxes". Cite §3.4 for the midpoint pieces.
   - E18 and E20: replace Lemmas 4.1 and 4.3 by OR64 Prop 3.1 / Lemma T(a) and T1.
   - E9: ledger wording.
   - E16: grid number.
   - E30: wording.
3. Keep (H) as CONJECTURE. Record R1, R2 and §3.4 as additional proved or CHECKED cases, and §3.2 as the exact shape of any counterexample.
4. Point 6. Report to the author that:
   - protection is free under the binding framework, even with finite-chain consistency;
   - (H) would make the framework's covering problem trivial;
   - (Add) — transitivity along non-overlapping chains — is a minimal closure condition that excludes Δ(𝒩), M1 and 𝒯, and holds in every positive construction.

   Whether to adopt it is the author's decision. Without such a condition, no axiom-level impossibility can be proved unless (H) fails.
