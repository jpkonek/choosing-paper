# PP68. Adversary for round 56: what any uniform fill co-design is forced to do, a check of PP67, and the second generation

23 October 2026. Adversary task of Brief 56. One author; not refereed. I read Brief 56 and its binding audits (AUDIT_round56, AUDIT_round55_direction, AUDIT_round55_answers), PP64, PP65, PP67 (draft at 23:01, final at 23:12), REFEREE_round55 §2.4, §4 and §5 (relayed), and the background listed in the brief.

**Labels.**
- PROVED: complete argument here, or a cited result used within its hypotheses.
- CHECKED: exact SAT or exact rational computation in `r9/PP68_py/`.
  - Verdict scripts end ALL PASS.
  - `cycle68.py` ends "RESULT: UNSAT", which is the predicted outcome.
  - `cycle68b.py`–`cycle68e.py` print the UNSAT cores and the derivations quoted in §4.
  - `pp67sat.py` prints SAT and its forced-verdict table.
- NUMERICS: sampled checks used only as evidence.
- CONJECTURE / OPEN: as stated.

No axiom is added. Named hypotheses: **(GC)** "G-closure" (§4), used only where stated.

**Sub-universe principle for CHECKED claims.** Each SAT instance restricts the models to a finite sub-universe and encodes only axiom instances on it (lib68.py). So UNSAT on an instance implies UNSAT in the full model domain. SAT is evidence only.

---

## 0. Verdict

1. **What any uniform choice E ↦ (N_E, p(E)) must satisfy (§1; PROVED).**
   - The signed clauses are uniform in E: Theorem 1.1 (nested and overlapping E), Lemma 1.2 (the A-part exclusion and a three-fill guidance trap), and Prop 1.3 (sharing).
   - **Sharing has a price.** If one model serves two nested fills, it beats the smaller one strictly at all three worlds. Then no coherent carrier of rec(X_E, N) can be selected **at any index**. For PP67's N this bans:
     - every precise D_m with m ∈ M other than the e₃-vertex;
     - every tightening of T that answers A somewhere on E₀.

     (Prop 1.3; CHECKED.)
2. **Where p(E) goes (§1.4; PROVED).**
   - The fill axioms alone fix **no** limit location. A constant p(E) is consistent with the full signed closure. I found such a model independently, N\* = D_{conv(M ∪ {(½,½,0)})}, before PP67 appeared; PP67's N is the least such model.
   - One restriction does bind: if each N_{E_n} also serves the larger fills, then p(E_n) cannot accumulate on the open edge {1, 2}.
3. **PP67 checked (§2).**
   - Correct: Prop 1.1, Lemma 3.1, Theorem 4.1 and Theorem 5.1, within the module.
   - N strictly dominates **every** X_E, including E = E₀ of full mass. The strictness is at world 3, from Lemma 3.1(d) and the κ key.
   - Three costs are not stated in PP67:
     - **(a) Fixed balls force plateaus.** If every later refusal at M ∈ {T, N, D\*} keeps the ball B_M, every model placed in cl(B_M) is all-world tied to M (Prop 2.1).
     - **(b) Carrier exclusion** (Prop 1.3).
     - **(c) G-closure fails at T one step down.** Whichever world N uses to defend against T, T must make **non-guidance** acceptances against a continuum of N's class-1 or class-2 fills (Prop 2.2).
4. **Referee relays (§3).**
   - Every Prop G kill pair has its T-literal refused by unit propagation, uniformly in E, but **only for D\***. Each further open-edge model needs its own refusal at installation.
   - Fills alone cannot create accumulation in PP67, because p(E) is constant. The entailed clause ¬[N ⪯₁ D] ∨ ¬[N ⪯₂ D] holds for **every** open-edge D.
5. **Second generation (§4). The barrier of PP67 Prop 7.4 is a certificate-level fact. The axiom-level fact is different.**
   - **Edge lemma (PROVED).** If B dominates a class-3 fill of a selected C, then C ⪯₃ B and C ⋠₁,₂ B. Every 2-cycle or 3-cycle of fill-domination forces world-3 ties (Theorem 4.3). CHECKED: N and its second-generation dominator cannot dominate each other's fills; T cannot dominate the fills of N's fill-dominator.
   - **Under (GC) at every generation, the dominator chain is infinite and strictly 3-descending (Theorem 4.4; PROVED).** No finite module is closed under its forced rivals. Any finite closed module must contain a non-guidance world-3 edge.
   - **The second generation can be uniform (Prop 4.5).** L₀ := D_{conv(v₃, M₀)} is weakly 3-worse than N, equals N on M₃, and adds only 3-wrong B answers on M₁ ∪ M₂. CHECKED: it consistently dominates every N-fill on the module's instance.
   - **An explicit (GC) chain flows to the edge** (Prop 4.6; CHECKED): L(t) = D_{conv(v₃ + t(h₁₂ − v₃), M₀)} → D\*.
   - Index accumulation is therefore **not** forced at generation 2. Where accumulation does occur, I give two (H_acc)-type constraints (Prop 4.7).
6. **Mixed-class fills (§5).** Within PP67's 𝒲₇ they are dominated by the class dominator N_k of any class they meet, after enlarging that class's weight W_k (PROVED, given Theorem 6.1).
7. **Negative route (§6).** No axiom-level conflict was found. Every UNSAT reported here is a conflict under stated optional commitments, or an exclusion of a candidate dominator.

| Item | Result | Label |
|---|---|---|
| Uniform forced clauses for nested and overlapping fills | Thm 1.1 | PROVED |
| A-part exclusion; three-fill trap at A-answering models | Lemma 1.2 | PROVED |
| Sharing ⇒ strict at all worlds ⇒ carrier exclusion; banned class | Prop 1.3 | PROVED; CHECKED |
| No forced limit location; a constant p(E) is consistent | Prop 1.4 | PROVED; CHECKED |
| PP67 Prop 1.1, Lemma 3.1, Thm 4.1, Thm 5.1 | §2 | checked; correct within the module |
| Fixed balls force tie plateaus cl(B_M) ⊆ Φ_M | Prop 2.1 | PROVED |
| N's defence world against T forces non-guidance acceptances at u | Prop 2.2 | PROVED |
| Prop G pairs and accumulation for PP67 | §3 | PROVED |
| Agreement trap for mutual fill domination | Lemma 4.1 | PROVED; CHECKED |
| Edge lemma; short cycles force world-3 ties | Lemma 4.2, Thm 4.3 | PROVED; CHECKED |
| (GC) forever ⇒ infinite strictly descending chain | Thm 4.4 | PROVED |
| Uniform (GC) second generation L₀ | Prop 4.5 | PROVED (geometry); CHECKED (cells) |
| (GC) chain L(t) → D\* | Prop 4.6 | CHECKED |
| Accumulation constraints for E-dependent chains | Prop 4.7 | PROVED |
| Mixed-class fills | Prop 5.1 | PROVED given PP67 Thm 6.1 |

---

## 1. What every uniform choice is forced to satisfy

**Setting.** As in Brief 56.
- E₀ ⊆ Q₃ := Sil(T) ∩ M₃. X_E := T[E ↦ A] for non-null E ⊆ E₀. N_E is a selected model with N_E ⪯_w X_E at every w, at index p(E).
- "Y ⊲_w Z": Y is pointwise no better than Z at w and differs from it. Strict (G) then refuses Y ⪯_w Z.
- The basic kill (from (TC)). The cycle Y ⪯ N ⪯ Z ⪯ Y is forbidden at w if any reverse is refused there. In particular **N ⪯_w Z and Z ≺_w Y imply Y ⋠_w N.**

**Theorem 1.1 (PROVED).** For every choice of dominators, every w ∈ {1, 2}, and every non-null E ⊊ E′ ⊆ E₀ with E′ ∖ E non-null:
- (i) T ⋠_w N_E and T ⪯₃ N_E (PP65 Prop 2.4).
- (ii) Y ⋠_w N_E for every Y with X_E ⊵_w Y strictly; and Y ⋠₃ N_E for every Y ⊴₃ X_E with Y ≠ X_E. That is: Y ⊴_w T off E and Y arbitrary on E (w = 1, 2); Y ⊴₃ T off E and Y = A on E (w = 3).
- (iii) **Nested fills.** X_E ⋠_w N_{E′} and X_{E′} ⋠₃ N_E.
- (iv) **Overlapping fills.** With F := E ∩ E′ and U := E ∪ E′, if these are proper and non-null:
  - X_F ⋠_w N_E and X_F ⋠_w N_{E′};
  - X_U ⋠₃ N_E and X_U ⋠₃ N_{E′}.

  X_E and X_{E′} are mixed against each other at every world, so no clause links N_E and X_{E′} directly.
- (v) **T/N_E splices** (PP64 Lemma 4.1(b), with N_E for D). Let P_w(N) := {N strictly w-better than T}. Then T ⋠_w T[H ↦ N_E] whenever P_w(N_E) ∖ E ⊆ H ⊆ {N_E ≠ T} (non-degenerate H). So T ⪯₃ T[H ↦ N_E] whenever H ⊇ (P₁ ∪ P₂)(N_E) ∖ E.

*Proof.*
- (ii): N_E ⪯_w X_E ≺_w Y with Y ⪯_w N_E is a forbidden cycle.
- (iii): N_{E′} ⪯_w X_{E′} ⪯_w X_E (guidance), and X_E ⪯_w X_{E′} is strictly refused. At world 3, swap the roles: N_E ⪯₃ X_E ⪯₃ X_{E′}.
- (iv): apply (iii) to F ⊊ E and to E ⊊ U.
- (v): PP64 Lemma 4.1(b), referee-checked; it uses only N_E ⪯_w X_E. ∎

**Lemma 1.2 (PROVED).** Let C be selected with C = A a.e. on a non-null E (for example any model of the closed edge [e₁, e₂], or the A-part of a dominator).
- (a) rec(X_E, C) = rec(T, C[E ↦ S]). So T's competitiveness gives the positive clause ∨_w [X_E ⪯_w C].
- (b) **Three-fill trap.** Let E‴ ⊊ E ⊊ E′ ∩ E″, with all differences non-null. Then the acceptances

  C ⪯₁ X_{E′},  C ⪯₂ X_{E″},  C ⪯₃ X_{E‴}

  are jointly forbidden. Each pair is allowed.
- (c) **A-part exclusion.** If N dominates X_{E′} and N = A on a non-null E ⊊ E′, then N ⋠₃ X_{E‴} for every non-null E‴ ⊊ E. So **one model cannot serve a fill lying inside its own A-part.** A model serving every E ⊆ E₀ must be ≠ A a.e. on E₀.

*Proof.*
- (a): both records have support {C ≠ T} ∖ E, with old side T and new side C.
- (b): by Theorem 1.1(iii) (applied to C), the three acceptances kill X_E ⪯_w C at w = 1, 2, 3 respectively. That contradicts (a).
- (c): N ⪯₁,₂ X_{E′} kills X_E ⪯₁,₂ N. So (a) forces X_E ⪯₃ N, and then N ⪯₃ X_{E‴} ⪯₃ X_E closes a forbidden cycle. ∎

Lemma 1.2(b) is the generalised guidance trap **across three different fills**. Unit propagation finds it.

**Prop 1.3 (sharing ⇒ strictness ⇒ carrier exclusion; PROVED, CHECKED).**
- (a) If one model N serves every fill E ⊆ E₀, then rec(X_E, N) is refused at **all three** worlds whenever E₀ ∖ E is non-null.
- (b) Hence **no selected model, at any index, carries rec(X_E, N).** A carrier C (C = T on L_N := {N ≠ T}, and C = A on E) would refuse its own copy C ⊕ rec(X_E, N) at every world of its support.
- (c) **For PP67's N** (L_N as in PP67 Lemma 1.2(d)), the banned class therefore contains:
  - every precise D_m with m ∈ M ∖ {v₃};
  - every tightening D_K (K ⊆ M) that answers A on a non-null part of E₀ (for example PP65's D_{K₀}, K₀ = [v₁, v₂]).
- (d) **For my N\***, with a smaller L_N, the banned class is larger. It also contains the precise edge models D_{(½,0,½)} and D_{(0,½,½)}, and every edge-{1,3} model whose credal ratios m₃/m₁ all lie in [7/9, 16/7).

*Proof.*
- (a) is Theorem 1.1(iii) applied to the same N at both ends.
- (b) is competitiveness.
- (c), (d): D_m (m ∈ M) equals T on Ans(T) ⊇ L_N. It is A wherever m·g > 0 on Q₃, which is a non-null set unless m = v₃, the minimising vertex on M₃.
- For (d), carriers of N\* need agreement with T only on L\* = {T's answer s has s(g₁ + g₂) < 0}. The ratio window comes from the suprema of |g₁|/|g₃| over T's answer regions on L\* ∩ M₁ (7/9) and on Q₃ (16/7). ∎

CHECKED:
- `carrier68.py`: precise D_m selected together with a single N\* serving every fill: UNSAT. Without D_m: SAT. With D_m, but N\* serving only the maximal fill: SAT.
- `geom68.py`: geometry of the carriers (L6), exact.

**Reading.** Sharing removes index accumulation in E. In exchange it bans a large explicit class of coherent models at **every** index. Posterior members are not carriers (NUMERICS: 0 of 230 grid members, `geom68` L7). So the ban is avoidable, but it binds any construction that later wants precise members inside M.

### 1.4 Where p(E) must go

**Prop 1.4 (PROVED, CHECKED).**
- (a) **No location is forced.**
  - N\* := D_{conv(M ∪ {h₁₂})} with h₁₂ = (½, ½, 0) is T with exactly the answers s with s(g₁ + g₂) < 0 silenced. Each such answer is 3-correct.
  - The partial system {T at u, N\* at one interior index; N\* ⪯_w X_E for all w and all E ⊆ E₀; guidance} is closure-clean. Its signed closure has no conflict.
  - So p(E) ≡ const is consistent with every finitary clause, and no limit point arises.
- (b) **Upward sharing excludes the open edge.** Suppose N_{E_n} ⪯_w X_{E_m} at every w for all n ≥ m, with E_n ⊆ E_m. Then p(E_n) cannot accumulate at any p in the closed edge [e₁, e₂].
- (c) **The guidance trap on the edge** (PP65 Prop 2.3; REFEREE_round55 §4) is the only uniform constraint on edge indices.

*Proof.*
- (a) Every copy of r_E := rec(N\*, X_E) is mixed at every world. Two copies, or a copy of r_E and a copy of PP67-style rec(D, X_E), are never consecutive in a triangle: a carrier would have to be S and T's answer on t₃ := M₃ ∩ {T = B} simultaneously. A triangle with exactly one mixed link cannot close with two guidance links (PP21 Lemma 2.1). No copy ends at a registered model, and the Pareto lemma covers guidance. So rules II–IV add nothing. Refusals propagate only to non-accepted records.
- (b) By closed sections, C_p ⪯_w X_{E_m} at every w. But C_p = A on E_m, contradicting PP65 Prop 2.3(b).

CHECKED: `single68.py` (SAT; the forced pattern of (a) and of Theorem 1.1(iii) holds exactly) and `geom68.py` (L1–L5, exact on 21,689 samples). ∎

---

## 2. PP67 checked

**Prop 1.1 (least element): correct.** Polyhedral duality gives Δ ∩ P\* = conv(M ∪ M₀), and any D_K weakly 3-worse than T has K ⊆ Δ ∩ P\*. My N\* has K\* ⊆ K_N, so it answers wherever N does: consistent (`geom68`). N\* is **not** the least element, and PP67's N is more silent.

**Lemma 3.1: correct.** Items (a)–(f) are single triangle kills or guidance. I re-derived (a), (c) and (d) as Theorem 1.1. One addition: (d) together with Prop 1.3(b) gives the carrier exclusion, which §5 and §8 of PP67 do not list.

**Theorem 4.1: correct as a certificate of the finitary clauses.**
- 𝒲 is total at each world: Φ₁, Φ₂ are real preorders and world 3 is lexicographic. So (TC) holds on every triangle.
- (IB) holds: Φ and κ differences depend only on the record.
- Strict (G) holds: κ is monotone in the 3-rank, and Φ is strictly monotone.
- Protection and defence of T, N and D\* come from unique pointwise Bayes acts. I checked that the defence argument survives the key: if the Bayes world is 3, κ(T) = κ(N) = 0 ≤ κ(Y).
- **N strictly dominates every X_E, including E = E₀:**
  - κ(N) = 0 < μ(E) = κ(X_E);
  - in Σ_fam itself, X_{E₀} ⋠₃ N comes from Lemma 3.1(d) with a non-null E′ ⊊ E₀ (μ is atomless).
- What 𝒲 does **not** certify:
  - closed sections, and (I8) at unassigned indices;
  - competitiveness of any model other than T, N and D\*.

  The κ key is a lexicographic level inside the certificate only. That is legitimate for a consistency proof, but a total relation of this form cannot be the final ranking (Prop 7.3).

`pp67sat.py`, with PP67's own cell types and commitments C1–C6: SAT. The forced verdicts agree with PP67's Prop 3.2.

**Theorem 5.1: correct for Σ_fam.** Two consequences that PP67 does not draw:

**Prop 2.1 (fixed balls force tie plateaus; PROVED).** Suppose that, in a later chain, every refusal committed at M ∈ {T, N, D\*} is reserved on the fixed ball B_M, as PP67 §2 prescribes. Then every model eventually assigned at q ∈ cl(B_M) is all-world tied to M.

*Proof.*
- Let q ∈ B_M and suppose C_q ≉ M. If M ⪯_w C_q held at every w, then C_q's undominatedness would give C_q ⪯_w M at every w, a tie. So M ⋠_w C_q at some w.
- That refusal is reserved on B_M ∋ q, so C_q ⋠_w C_q, against reflexivity.
- For q ∈ ∂B_M, closed sections applied to the rival M give C_q ⪯_w M at every w (since M ⪯_w M). M's protection then gives the tie. ∎

Within Σ_fam alone, the same argument already excludes from B_M every model that is a strict pointwise w-improvement of M at some world. So PP67's provisional Ĉ = M on B_M is **forced up to ties** once the rule persists. This is consistent, but it is a design commitment: the tie fibres Φ_T, Φ_N and Φ_{D\*} must have interior. It also rules out the −e₃ posterior ray near u (each member C_s is A on its own new layer R_s ⊆ Q₃ and weakly 3-worse than T, so C_s ⋠₃ X_{R_s}, while B_u refuses X_{R_s} at worlds 1 and 2).

**Prop 2.2 (G-closure fails at T one level down; PROVED).** N ⋠₃ T by strict (G), so N defends against T at world 1 or 2. Say N ⪯₁ T (PP67 commits both, in C3).
- Then T ⋠₁ Z for every strict 1-improvement Z of N: the cycle N ⪯₁ T ⪯₁ Z ⪯₁ N has its reverse N ⪯₁ Z strictly refused.
- Take Z_F := N[F ↦ A] with F ⊆ Q₂ non-null. Here A is correct at worlds 1 and 3 and wrong at 2. Z_F is mixed against T:
  - at world 2: worse on F and on L_N ∩ M₁, better on R_B;
  - at world 3: better on F, worse on L_N.
- So T must accept Z_F at world 2 or 3, and **by a non-guidance acceptance, for every F ⊆ Q₂.**
- With N ⪯₂ T the same holds for every F ⊆ Q₁.

PP67 derives (GC) from the slogan "non-guidance acceptances at u are what kill". Prop 2.2 shows that (GC) cannot be honoured at u even for the forced rivals of the module's own dominator. In 𝒲 these acceptances are pending and satisfiable. They are not a conflict, but they are exactly the kind of literal for which PP67's §5.3 (O1) is open.

---

## 3. The referee's relays, applied to PP67

**(1) Generalised trap (REFEREE_round55 Prop G).**
- For D\*, PP67 commits b₁(E) and b₂(E) for every E. Unit propagation then refuses r_w@w = rec(Z_w, D\*) at w for every partial splice Z_w = T[G_w ↦ D\*] with G_w ⊆ {D\* weakly w-worse} ∪ E. T carries each such r_w, so the refusal sits at u on B_u. **Every Prop G pair at D\* is resolved, uniformly in E (PROVED).** This agrees with PP67 Lemma 3.1(b).
- The open edge carries infinitely many values (PP65 Prop 3.2). **For every other open-edge model D, PP67 commits nothing.** Each needs T's refusal of D at one edge world at installation (the referee's recommendation). Under Prop 2.1 this is automatic for q ∈ B_u (C_q ≈ T), but not elsewhere.

**(2) Can fills chosen after the commitments make acceptances accumulate at both literals of a kill clause?**
- **Not through the fills (PROVED).** p(E) and the edge index are constant. Every module kill clause has a literal refused on a full ball (PP67 Theorem 5.1(iv), which I confirm). Adaptive, nested or shrinking E_n add no index.
- **A clause that the fills do not decide (PROVED).** For **every** open-edge model D, the clause ¬[N ⪯₁ D] ∨ ¬[N ⪯₂ D] is entailed by 𝒦 alone. D must defend against N's class-3 fills Y_F at 1 or 2, and N ⪯_i D, D ⪯_i Y_F, Y_F ⪯_i N (guidance) is a forbidden cycle. The same holds for T with T's fills (the referee's ¬a₁ ∨ ¬a₂).
  - With Ĉ = N on B_N, the literals at q ∈ B_N are the **same records** as at p_N. So no accumulation of distinct literals can occur there.
  - If a later step places a model tied to N but different from N in B_N, the referee's Prop 5.3 configuration becomes available. Under PP67's fixed-ball rule it is then fatal already at a **finite** stage: one acceptance at 1 and one at 2 inside B_N, followed by N's forced refusal reserved on B_N.
- **Repair, implicit in Prop 2.1.** Keep Ĉ = M itself, not merely tied models, on B_M.

**(3)** I agree that unit propagation catches both traps (Lemma 1.2(b) is one more instance) and does not catch accumulation.

**(4)** Noted. Nothing here uses PP65 Prop 4.1 or 4.2.

---

## 4. The second generation: what is forced, and is the barrier axiom-level?

**Notation.** For selected, registered B and C with 3 ∈ supp C, write **B →₃ C** if B ⪯₁ Y and B ⪯₂ Y for some class-3 fill Y = C[F ↦ A] (F ⊆ Sil(C) ∩ M₃ non-null and non-conic). In particular this holds if B dominates such a fill.

**Lemma 4.1 (agreement trap; PROVED; CHECKED).** Let w ∈ {1, 2} and let F, F′ ⊆ {Y = N} ∩ Sil(Y) ∩ M₃ be disjoint and non-null. Then Y ⪯_w N[F ↦ A] and N ⪯_w Y[F′ ↦ A] are jointly forbidden.

*Proof.*
- Z := N[F ↦ A] carries β := rec(N, Y[F′ ↦ A]), whose support is {N ≠ Y} ∪ F′, and Z ⊕ β = Y[F ∪ F′ ↦ A].
- Y[F ∪ F′ ↦ A] ⪯_w Y by guidance. So Y → Z → Y[F ∪ F′ ↦ A] → Y is accepted at w, while its reverse Y ⪯_w Y[F ∪ F′ ↦ A] is strictly refused. ∎

CHECKED (`cycle68b.py`): the minimal UNSAT core is exactly these two acceptances, at world 2.

**Lemma 4.2 (edge lemma; PROVED).** If B →₃ C, then C ⋠₁ B, C ⋠₂ B and C ⪯₃ B.
- (a) In particular, **B →₃ C is impossible if B is pointwise weakly 3-better than C and B ≠ C.** So T can never serve the fills of a G-closed dominator of T.

*Proof.* C ⪯_i B ⪯_i Y ⪯_i C (Y ⊵_i C strictly) is a forbidden cycle for i = 1, 2. C then defends at 3. For (a), C ⪯₃ B is refused by strict (G). ∎

CHECKED (`cycle68f.py`): T dominating any N-fill is UNSAT, even without N's own commitments.

**Theorem 4.3 (short cycles force world-3 ties; PROVED, CHECKED).**
- A 2-cycle B →₃ C →₃ B gives B ≈₃ C.
- A 3-cycle B →₃ C →₃ D →₃ B gives C ⪯₃ B ⪯₃ D ⪯₃ C, so by (TC) all three are tied at world 3.
- Hence no cycle of length 2 or 3 through two models of which one is pointwise strictly 3-better than the other.

CHECKED (`cycle68c/d/e.py`, models T, N\*, Y = D_{[v₃, h₁₂]}):
- N\* serves T's fills and Y serves N\*'s fills: SAT.
- Adding "T serves Y's fills": UNSAT. The core is four literals, and the derivation is N\* ⋠₁,₂ Y ⇒ N\* ⪯₃ Y ⇒ Y ⋠₃ T (cycle with T ≺₃ N\*) ⇒ Y undefended against T.

Longer cycles are **not** excluded by triangle-(TC). A 4-cycle needs non-transitive world-3 acceptances (OPEN whether that is consistent).

**Hypothesis (GC) at an edge B →₃ C:** B is weakly 3-worse than C. This is PP67's G-closure, applied at every generation.

**Theorem 4.4 (G-closed recursion never closes; PROVED).** Let L₀ = T, and for each k let L_{k+1} →₃ L_k with (GC). Then:
- every L_k is silent on a non-null part of M₃;
- the L_k are pairwise distinct;
- L₀ ⊳₃ L₁ ⊳₃ L₂ ⊳₃ … pointwise and strictly.

So no finite set of selected models that contains T is closed under "every class-3 fill of a member is dominated by a member, by a G-closed edge". Every finite closed set has a non-G-closed edge. On a cycle that edge is a non-guidance acceptance C ⪯₃ B, and on a 2- or 3-cycle it is a world-3 tie (Theorem 4.3).

*Proof.*
- L_{k+1} ⪯_{1,2} L_k[F_k ↦ A] (some non-null F_k ⊆ Sil(L_k) ∩ M₃) with L_k registered. Lemma E(ii) gives L_{k+1} ≠ A on a non-null part of F_k.
- By (GC), on that part L_{k+1} is no 3-better than S, so it is S (B is 3-correct, and coherent models are never contradictory). So Sil(L_{k+1}) ∩ M₃ is non-null, and L_{k+1} has non-conic fills.
- L_{k+1} ≠ L_k, because a model never accepts its own strict 1-improvement. (GC) is pointwise, so the order is strict and the models are distinct. ∎

**Reading against PP67 Prop 7.4.** Prop 7.4 says an additive-at-1,2 certificate allows only finitely many uniform generations. Theorem 4.4 says (GC) at every generation requires infinitely many generations. Together:

> (GC) forever + uniform generations forever ⇒ no additive-at-1,2 certificate.

Each half is a different kind of fact. Theorem 4.4 is axiom-level given (GC). Prop 7.4 is certificate-level. **The axioms themselves force only Theorem 4.4.** Dropping (GC) at one edge per cycle is consistent with every lemma here.

**Prop 4.5 (a uniform G-closed second generation exists; PROVED geometry, CHECKED cells).** Let L₀ := D_{conv(v₃, M₀)}, with v₃ = c·1 + εe₃. Then:
- (i) K_{L₀} ⊆ K_N, so L₀ answers wherever N does, with N's answer.
- (ii) L₀ = N on M₃. In particular L₀ is silent on every N-fill set in M₃.
- (iii) Every new answer of L₀ is B on M₁ ∪ M₂, which is 3-wrong. So L₀ is weakly 3-worse than N, strictly 1-better than N on part of M₁, and strictly 2-better on part of M₂.

*Proof.*
- (ii) On M₃ (g₁, g₂ > 0 > g₃), d₁·g and d₂·g are positive, so L₀ answers + iff v₃·g > 0. That is T's (and N's) + condition, because v₃ is T's minimising vertex there.
- (iii) On M₁ (g₁ > 0 > g₂, g₃), L₀ says − (A) only if 16g₁ + 7g₂ < 0 and v₃·g < 0. Then (c + ε)g₁ < (16/30)(7/16)|g₂| = c|g₂|, so cΣg + εg₁ < c·g₃ < 0, and T and D\* both say −. So any new answer is B. M₂ is symmetric.

CHECKED:
- `chain68.py` C1: exact, with new-answer types {(M₁, S → B), (M₂, S → B)}.
- `gen2_68.py` G1: PP67's C1–C3 together with "L₀ dominates every N-fill at every world" is SAT.
- `gen2_68.py` G2: T, N, D\* and L₀ each dominating an L₀-fill are UNSAT. So a third generation needs a fifth model, as Theorem 4.4 predicts. ∎

So the second generation does **not** have to be E-dependent, contrary to PP67 §7's reading. PP67 Prop 7.2 itself is correct, since it does not claim non-existence. Whether a **uniform** G-closed third generation exists is OPEN. NUMERICS: every symmetric or asymmetric shrinking of conv(v₃, M₀) that I tested adds 3-correct A answers, so it fails (GC).

**Prop 4.6 (an explicit G-closed chain to the edge; CHECKED).** Let L(t) := D_{conv(v₃ + t(h₁₂ − v₃), M₀)}, for t ∈ [0, 1). Then:
- L(0) = L₀;
- for s < t, L(t) is weakly 3-worse than L(s), with new answers only A on M₃ and B on M₁ ∪ M₂;
- L(t)'s class-3 silence shrinks to null as t → 1, and L(1) = D\*.

CHECKED (`chain68.py` C2–C3) on a grid of 12 values of t.

This is the G-closed recursion made explicit. Fills of L(s) are served by L(t) with t > s, provided L(t) is still silent on part of the fill. The dominators flow to the {1, 2} edge. This is "the edge" answer to the brief's question, for the **generations** rather than for E.

**Prop 4.7 (where E-dependent generations do accumulate; PROVED).**
- (a) For a fixed fill Y = L[F ↦ A] of a selected L at p_L, the set of its dominators misses an open neighbourhood of p_L. Indeed L ⋠₁ Y (strict (G)), A₁(Y) is closed, and p_L ∉ A₁(Y). So thin fills near L's boundary may push their dominators toward p_L, but **each fixed fill's dominators are bounded away from p_L.** No fixed-rival limit literal at p_L arises.
- (b) If dominators L_k accumulate at an open-edge index p∞, then for each fixed earlier member L_j:
  - every L_k (k > j, (GC)) refuses L_j at 3;
  - so L_k ⪯₁ L_j or L_k ⪯₂ L_j;
  - and C_{p∞} must not inherit both literals, because the clause ¬[C ⪯₁ L_j] ∨ ¬[C ⪯₂ L_j] holds for edge models C (§3(2)).

  So **the defence world of the chain against each earlier member must eventually be constant.** This is (H_acc) in the "isolation" form. It is satisfiable, but it is a policy that must be carried in the invariant. ∎

**Answer to the relay's item (2).**
- Accumulation is not forced at generation 2: L₀ is uniform.
- It is not forced at all by the axioms in a way I could exhibit. Prop 4.7 lists the constraints it must obey when it occurs.
- The generation barrier of PP67 Prop 7.4 belongs to its additive certificate. The axiom-level barrier is Theorem 4.4: an endless (GC) chain, or a non-guidance world-3 edge somewhere.

---

## 5. Mixed-class fills

Let X := T[E ↦ A₃, F ↦ A₁] with E ⊆ E₀³ ⊆ Q₃ and F ⊆ Q₁, both non-null. Then:
- X is a strict 2-improvement of T, and mixed at worlds 1 and 3;
- by PP65 Prop 2.2, R₂(X) ⊇ P₂.

**Prop 5.1 (PROVED, given PP67 Theorem 6.1).** In 𝒲₇ with W₃ enlarged, N₃ ⪯_w X at every w, and N₃ strictly dominates X.

*Proof.*
- World 3: κ₃(X) = μ(E) > 0 = κ₃(N₃).
- Worlds 1 and 2: Φ_w(X) ≥ Φ_w(T) − ∫_{Q₃ ∪ Q₁}|g| dμ, and Φ_w(T) − Φ_w(N₃) ≥ W₃∫_{R_B³}|g| dμ − C. Neither bound depends on W₃.
- PP67's decoupling keeps every other family's inequalities, so W₃ can be enlarged alone. ∎

The forced literals (Theorem 1.1 with the class-3 part) are those of the class-3 family, plus X ⋠₁ N₃ (from X_E ⪯₁ X). No new kill pattern appears. Mixed fills are **not** a source of new dominators in PP67's architecture.

---

## 6. Negative route

No axiom-level conflict was found. The derived constraints are:
- Theorem 1.1;
- Lemma 1.2 (three-fill trap);
- Prop 1.3 (carrier exclusion under sharing);
- Lemma 4.2 / Theorem 4.3 (edge lemma; ties on short cycles);
- Theorem 4.4, given (GC).

Every UNSAT in `PP68_py` follows either from an optional commitment (sharing, mutual or cyclic fill domination, a chosen dominator) or from an exclusion of a candidate. A genuine conflict would need the **unavoidable** fills' KKM dominators to be forced into a short cycle with a pointwise 3-strict pair, or into an accumulation that violates (H_acc). I could not force either.

---

## 7. Records and obligations that remain unassigned (after PP67 + this note)

1. Every index except u, p_N and p\*. Under Prop 2.1 the three balls are tie plateaus.
2. Dominators of the third and later generations. Under (GC) they form an infinite chain (Theorem 4.4); one explicit chain is L(t) (Prop 4.6). The uniform G-closed third generation is OPEN.
3. Dominators of the T/N splices Z_H (PP67 Prop 7.1). Not addressed here.
4. T's non-guidance acceptances against the N-fills on Q₁ or Q₂ (Prop 2.2). They are pending; their (TC) kill clauses fall under (O1).
5. T's and N's refusal world against each further open-edge model, by §3: each must be committed, with its ball, at installation.
6. Whether 4-cycles of fill domination with non-transitive world-3 acceptances are consistent (OPEN).

---

## 8. Scripts (`r9/PP68_py/`; run `python3 -I -B <script>.py` inside the folder; outputs in `<script>.out`)

| Script | Content | Label |
|---|---|---|
| `lib68.py` | SAT encoding of the axioms on a cell instance (guidance, strict (G), (IB) via record variables, (TC) on all ordered triples, defence, rule III, direct (C)); sub-universe support | — |
| `geom68.py` | Exact geometry: N\* (L1–L4), D\* (L5), carriers (L6); NUMERICS on posterior carriers (L7) | CHECKED |
| `single68.py` | One N\* serving every fill: SAT, with the forced pattern of Thm 1.1(iii) | CHECKED |
| `carrier68.py` | Prop 1.3: a selected precise carrier with sharing is UNSAT; controls SAT | CHECKED |
| `joint68.py` | N\* and an edge defender: SAT; N\* ⪯₃ D forced; N\* ⪯₁ D ∧ N\* ⪯₂ D is UNSAT | CHECKED |
| `pp67sat.py` | PP67's commitments C1–C6 on its own cell types: SAT, with forced table | CHECKED |
| `cycle68.py`, `cycle68b.py` | Mutual fill domination UNSAT; minimal core = Lemma 4.1 | CHECKED |
| `cycle68c.py`–`cycle68e.py` | 3-cycle UNSAT; core and derivation (Thm 4.3) | CHECKED |
| `cycle68f.py` | T cannot serve N-fills (Lemma 4.2(a)) | CHECKED |
| `gen2_68.py` | L₀ serves all N-fills consistently; no module model serves L₀'s fills | CHECKED |
| `chain68.py` | Prop 4.5(iii) and Prop 4.6, exact on samples | CHECKED |
