# REFEREE for round 55 (file name as briefed: REFEREE_round54): PP61–PP63 and the decreasing-limit lemma

23 October 2026. Independent referee for Briefs 54–55. Scope: PP61 (Theorem C, Cor C.5, the α-certificates, the Cor E.2 run, allocation E2); PP62 (Theorems R, P, M, E, Lemma 1.3(b), Cors E.1–E.2, Lemma S); PP63 (Lemma 3.1, Cor 3.2, Lemma 4.1, Props 2.1, 4.4–4.6, Cor 4.5, Theorem J); the decreasing-limit lemma, with the audit's three cautions (AUDIT_round55_answers). I add no axiom. The setting is Brief 55's.

**Labels.**
- PROVED: the argument is complete here, or checked line by line here.
- CHECKED: an exact computation in `r9/REFEREE54_py/`. This is either an independent re-implementation, or a re-run whose output matches the author's. Each is marked.
- OPEN: as stated.

**Verdict scale.** correct / correct with repair / wrong.

**Conventions.**
- "X ⪯_w Y" means X is at least as good as Y at world w.
- Global (C) comes in two forms, which must be kept apart:
  - **(C∃)**: every incoherent model is dominated (PP55 §4's "global (C)");
  - **(C_dir)**, the audit's "global direct (C)": for every coherent undominated N and every incoherent X, some world refuses X ⪯ N.
- **(C⁺)** is AUDIT_completion's Rule IV, read as an invariant: every all-world tie partner of a coherent undominated model is itself coherent and undominated.

---

## 0. Summary of verdicts

| # | Item | Verdict |
|---|---|---|
| 1a | PP61 Theorem C (countable closure) | **correct** |
| 1b | PP61 Cor C.5 (no finite propositional certificate at any depth) | **correct**, under its stated stable-combinatorics hypothesis. It supersedes PP63's "two levels are needed" wording (3d). |
| 1c | PP61 α-certificates A1, A4 and the inverse-pair (1, 1) | **correct** (CHECKED, re-derived per atom) |
| 1d | PP61 Cor E.2 run: V0/V1 SAT models; V2 13-clause core | **correct** (CHECKED independently: models re-verified; core rebuilt, UNSAT and minimal). **One wording is wrong**: the model is not "R₀ with w₀ = 3 modified exactly on the e₃ germs" (§1.4). |
| 1e | PP61 allocation E2 | **correct as stated on the finite instance**: defended, protected, (TC) on every triple, (IB), (G), SEC (CHECKED independently, 0 violations). "Openness" means persistence along the three +e_w rays only. |
| 2a | PP62 Theorem R | **correct** (PROVED; re-run CHECKED) |
| 2b | PP62 Theorem P | **correct** |
| 2c | PP62 Theorem M | **correct as scoped; does not reach the brief's target.** PP63's objections are right (CHECKED). |
| 2d | PP62 Lemma 1.3(b) at u | **correct** |
| 2e | PP62 Theorem E, Cor E.1 | **correct** |
| 2f | PP62 Lemma S and Cor E.2 | Lemma S and Cor E.2(i) are **correct**. The sentence after Lemma S is **correct with PP63's repair**. Cor E.2(ii) can be **sharpened** further (§2.6). |
| 3a | PP63 Lemma 3.1, Cor 3.2 | **correct for the clauses listed.** It needs a **scope repair** for global (C) in Brief 55's sense (same mechanism as §4). |
| 3b | PP63 Lemma 4.1 | **correct** |
| 3c | PP63 Prop 2.1 / 2.2 | **correct.** Prop 2.2 is CHECKED for every small t, not just t = 1/1000 (§3.3). |
| 3d | PP63 Props 4.4–4.6, Cor 4.5 | **correct.** The §0 phrase "a certificate needs at least two levels" should read "needs quantitative content" (Cor C.5). |
| 3e | PP63 Theorem J (Radon kite) | **correct with repair (scope)**: proved for N containing a neighbourhood of u (kite CHECKED independently), not yet for "every" 2-D N |
| 4a | Decreasing-limit lemma (fixed selection): (G), (IB), (TC), closed sections, support defence, undominatedness of models protected at every stage | **PROVED** (§4.1). It also preserves members' direct (C). |
| 4b | Caution 1: global direct (C) is not automatic | **confirmed** for partial systems: an explicit chain in which every stage satisfies the stated axioms **and** Rule IV, but the limit fails (C_dir) (CHECKED). **Refined** for a full selection on Δ: (C∃) is automatic at the limit, and (C_dir) is automatic if every stage satisfies (C⁺) (PROVED, §4.2–4.3). |
| 4c | Caution 2: stages that fail (C) are not repaired | **confirmed**, in a precise form: an all-world tie survives to the limit iff it is present at every stage |
| 4d | Caution 3: "finitely many changes" does not give closed sections | **confirmed** ([1/n, 1] example). The positive form holds: with committed, never-withdrawn reservations, final refusal sets are open (§4.4). |

**Bottom line.**
- No stated theorem of PP61–PP63 is wrong.
- The repairs are in scope (Lemma 3.1, Theorem J) and in wording (PP61 §5.1's "local shape"; PP63 §0 on levels).
- The decreasing-limit lemma holds exactly as the audit lists it.
- Of the audit's two (C) cautions:
  - the first is correct for partial systems;
  - but for a completed selection on all of Δ, KKM recovers (C∃) for free, and (C_dir) follows from the AUDIT_completion invariant (C⁺) maintained at every stage.

  So Brief 55's invariant should include (C⁺) explicitly. Its limit argument should be run only once the selection covers Δ, or else carry (C_dir) as an explicit obligation.

---

## 1. PP61

### 1.1 Theorem C (PROVED: correct)

I checked each step.

- **Step 1.** It imports Λ_q's non-section axioms for every common q. This is REFEREE_round53 §5.
- **Step 2.** f(a′) = ∫ q[u¹_i(X) − u¹_i(C_{a′})] is continuous in a′, by continuity in measure and the K|g| envelope.
  - If f(a) ≠ 0, the level-0 verdict is constant near a.
  - In that case C_{a′} ≠ X near a, so the null-record case does not arise.
- **Step 4.** Z = {q : ∫ q d = 0} is closed in the complete space Q.
- **Step 5.** Z has empty interior.
  - Choose E inside {d > 0} or {d < 0}, and inside {q ≤ 3/2} or {q ≥ 3/2}.
  - Move q by +δ1_E in the first case and by −δ1_E in the second. Either way q stays in Q.
- **Step 6.** Baire's theorem applies to the countable family Γ × {1, 2, 3}.

The conclusion is exactly local constancy **at the listed pairs**. Nothing is claimed elsewhere, and the note says so.

### 1.2 Cor C.5 (PROVED: correct, under its hypothesis)

The quantifier order is sound:
1. fix a countable sequence of scale tuples;
2. put every branch rival at every tuple into Γ;
3. choose q generic;
4. then choose the scales hierarchically below the radii of local constancy.

The actual instance at those scales has the same formula Φ, by the stable-combinatorics hypothesis, and Λ_q satisfies it. So Φ is satisfiable.

**Hypothesis to keep visible.** "Stable combinatorics" must hold on the hierarchical scale region (t_{k+1} ≪ t_k), not just on a box. This is a two-parameter chirotope statement. For Prop 4.4-type instances it is the natural hypothesis, but it is a hypothesis.

**Consequence.** Branch-dependent rival choice has no propositional content. An obstruction must use masses against relation-chosen radii. PP63 §0 item 1 ("a certificate needs at least two levels") is therefore superseded: two levels are necessary, but no finite number of levels is sufficient.

### 1.3 α-certificates (CHECKED, `alpha_ref.py`)

I re-derived the increments per atom, from PP56's field and also from the closed formula on R (φ(h) − φ(S) = −|Wr| at Cor worlds, +|Cor| at Wr worlds). The two agree.

- **A1.** The increments are K09.c1: (−2, 1, 1) and K11.c1: (2, −1, −1).
  - d₁ + 2d₃ = 0 on both atoms.
  - E2 does refuse this record at worlds 1 and 3.
- **A4.** The increments are (2, −1, −1) on K10 and (−2, 1, 1) on K17.
  - d₂(r₁) + ½d₁(r₂) = (0, 1, 0) on (K10.c1, K17.c1, K17.c2). This is ≥ 0 and not identically 0, so it is a valid certificate.
  - The inequality reading in §4.2 is right.
- **Inverse pairs.** d(r⁻) = −d(r) pointwise, so α = (1, 1) needs no computation.

By Prop A″ these are obstructions for every reweighted relation, as claimed.

### 1.4 Cor E.2 run (§5.1)

**Re-run.** `corE2_rerun.py` is a verbatim copy of run61d that saves its data. Its output matches `run61d.out` line by line: V0 and V1 SAT; V2 UNSAT with 13 clauses.

**Independent model check (`check_corE2.py`).**
- I recomputed from the model vectors: records, ranks, guidance, (IB), DEF, C/UND, SEC, (TC) on all 314³ ordered triples, and the endorsement units.
- V0 and V1 have **0 violations**.
- (My first pass flagged pairs of identical models under different names. That was my bug, not theirs: they are empty records, accepted by reflexivity.)

**Core.** I rebuilt the 13 clauses from my own records:
- one C clause;
- three DEF clauses;
- three SEC clauses;
- six END2 units.

Checks:
- rec(Y′ → C_B) = rec(C_u → X′) holds exactly.
- The END2 units have V_v < 0 at every v ≠ w.
- Brute force over the 12 variables: the clause set is UNSAT, and every 12-clause subset is SAT. So the core is **minimal**.

It is Theorem E clause by clause, and only the END2 units are non-axioms. Correct.

**Caveat on the V-values.** The printed V-values use equal masses on the layer atoms. They are not the true Γ: at u, Lemma 1.3(b) gives Γ_{w′} = Γ_{w″}, whereas the printed e₂ and e₃ rows are asymmetric (−60 vs −18). Only the signs enter the core, and those are Lemma 1.3(b). This is legitimate, but the numbers should not be quoted.

**Wording error (wrong as stated).** PP61 §0.6 and §5.1 describe the V0 model as "R₀ with w₀ = 3 plus exactly one u¹-unfavourable acceptance per e₃-germ", "modified exactly on the germs of the e₃ direction".
- That is true of the **seven displayed records** only: the base record and the six germ records against X.
- Against R₀(w₀ = 3), evaluated with PP61's own mass convention, the V0 model departs on 13,129 of 38,382 comparable (record, world) verdicts (`r0_vs_V0.out`).
- Two tests settle what *can* be kept (CHECKED, `corE2_R0test.py`, `corE2_R0tight.py`):
  - **(T1) SAT.** Fix R₀(w₀ = 3) on every record that touches neither an e₃-shifted member nor its splits and copies (13,908 units). A model exists (re-verified, 0 violations).
  - **(T2) UNSAT.** Fix R₀(w₀ = 3) on every record outside the rows and columns of the two e₃-shifted members themselves. The minimal core has 15 clauses: one C, one DEF (the e₃ member), three SEC, two TC, and eight R₀-fixing units on records outside those rows and columns, including the e₁ and e₂ germ acceptances against X′.

**Correct statement.** R₀(w₀ = 3) can be kept everywhere except on the records touching the e₃-shifted members and their Lemma S splits and copies. It cannot be kept on the splits themselves (Cor E.2(ii); §2.6 below says which split links must change). This is still not an axiom obstruction, since the T2 core contains fixing units.

### 1.5 Allocation E2 (CHECKED, `check_E2.py`; independent except for the instance and the verdict vector)

I recomputed the following from the model vectors, using my own canonical records (σ/minus refinement) and my own ranks:
- (IB): 532,873 records. My partition coincides with PP61's, and **0 records have inconsistent verdicts**.
- Reflexivity; strict (G) on every pair, in both directions.
- DEF for every selected model, shifted ones included.
- Protection: C for incoherent rivals, UND for coherent ones.
- SEC along the nine germs.
- (TC) on every ordered triple of the base block and of all nine sub-instances, at every world.

**All 0.** The pattern is as stated:
- 10 balanced swaps with {13}/{23};
- 10 with {23}/{13};
- 4 with {23}/{23};
- every pair is refused at world 3 in both directions;
- germ refusal sets equal the base ones at both ends.

So E2 **is** defended, protected and (TC)-closed on the stated instance.

**Scope of "openness".**
- The SEC clauses and the germ check use the three directions a∘(1 + te_w) only. They cover neither a neighbourhood nor the −e_w directions.
- The verdict on a shifted record is one verdict per combinatorial type, i.e. uniform in t ∈ (0, 10⁻⁵].
- So E2 is a finite candidate, as PP61 says. "Open in the source" should read "persistent along the three pure-shift rays".

---

## 2. PP62

### 2.1 Theorem R (PROVED: correct; re-run CHECKED, `rerun_r0_check.out` ALL PASS)

- **Steps 1–3 ((IB), reflexivity, strict (G)).** A non-null record with V = 0 is mixed at every world. Ranks are injective in the advice, and (U1) holds, so a one-sided record has V_w ≠ 0.
- **Step 4 ((TC)).** The three V's of a triangle sum to 0 because V(rec(X, Y)) = Φ(Y) − Φ(X), with Φ finite by (U1).
  - An accepted link has V_w ≥ 0, so every V_w is 0.
  - If V ≠ 0, the reverse has V_w = 0 and is accepted.
  - If V = 0, acceptance at w forces w ≠ w₀, and R₀(r⁻) = {w₀}.
- **Step 5 (defence and protection).** It needs only (U2): Σ_w V_w(rec(C_a, X)) ≥ 0 for every measurable X. This is PP56's pointwise λ = (1, 1, 1)-Bayes property of members, over all four values.
  - If V ≠ 0, some coordinate is ≥ 0 (defence) and some coordinate is > 0 (protection).

**What the proof uses about members.** It is exactly the λ-Bayes inequality. So Theorem R holds for every family inside 𝒮₀ and for every rival. Exact undominatedness and direct (C) for members are vacuous consequences of protection. Remark 3 ((LA)) is asserted, not re-derived; I accept it as in Theorem L.

### 2.2 Theorem P (PROVED: correct)

- **Continuity.** a ↦ V(rec(C_a, X)) = Φ(X) − Φ(C_a) is continuous.
- **Points with V_w < 0.** Openness there is immediate.
- **Null points.** At a null point, refusal at w₀ persists exactly under (★).
- **Interior null points.** At an interior null point the pure w₀-shift is pointwise strictly w₀-better (Lemma 1.1 with d = e_{w₀}). So Φ_{w₀} drops, the shifted index leaves Z_X, and the shifted member accepts.
- **Minor point.** The proof should also note the points with C_{a′} = X (null record, accepted). They do not affect openness of the refusal set.

### 2.3 Theorem M (PROVED: correct as scoped; PP63's objections correct)

**The theorem itself.**
- **Lemma 3.1.** Parts (i) and (ii) hold as written. For (iii), it suffices that the B → u disagreement contains odd-world-3 cells with c₃ < 0 ≤ c₂.
- **Scope.** The condition Z_X ⊆ {u, B} makes Theorem P give openness for every in-scope rival.
- **Certificate.** The α = (1, 1) certificate is right, because rec(C_B, Y_F) is the reverse of rec(C_u, X_F).

**PP63's objections, all verified.**
- **(a) u ∈ ∂N.** u∘(1 + te₂) lowers Φ₂, so it violates N_u's inequality. N is not a neighbourhood of u, as the brief requires.
- **(b) Interior failure** (re-run `lobe63.py`: ALL PASS). At a₁ = u∘(1 − se₂), log(B/a₁) has strict middle coordinate 1, and both cell kinds are present.
  - So by Cor 1.2 and Lyapunov a balanced non-conic F exists.
  - By Prop 6.1, R₀'s section fails at the interior point a₁ for X = C_{a₁}[F ↦ C_B].
  - Theorem M's scope excludes exactly this rival. Since (S) quantifies over every rival, R₀ on N_u ∪ N_B is **not** an (S)-module. It is a rival-restricted module.
- **(c)–(d).** Correct.

### 2.4 Lemma 1.3(b) at u (PROVED: correct)

τ = (2 3) has the following properties:
- it preserves μ and |g|;
- it permutes the vertices of M;
- it fixes u and u∘(1 + te₁);
- it maps odd-world-2 layer points to odd-world-3 layer points.

On R, the field depends only on the sign pattern (vals = {h, S}), so it is τ-equivariant there, and the layer lies in R. Hence β₂ = β₃, and Γ₂ = Γ₃ = −(α + β) < 0. Part (a) is the Lemma 1.1 bookkeeping, with Γ = −Σ c_i ε_i. I re-derived the signs.

### 2.5 Theorem E and Cor E.1 (PROVED: correct)

- **Step 1.** Y is incoherent (non-conic F). Direct (C) for C_b gives a refusing world w, and (IB) transfers it to rec(C_a, X).
- **Step 2.** Closed sections give refusal along a∘(1 + te_w).
- **Step 3.** Defence then gives acceptance at some v ≠ w.
- **Steps 4–5.** Additivity gives Ψ(rec(C_{a_t}, X)) = Γ^ψ(a, a_t), and (H_Γ) makes both coordinates v ≠ w negative. This contradicts endorsement.

No (TC) and no (G) are used. Cor E.1's list is right; an intersection containing u¹ accepts only u¹-accepted records, so it is endorsed.

### 2.6 Lemma S and Cor E.2 (PROVED)

- **Lemma S** is correct. Lyapunov gives E with ∫δ < ∫_E δ < 0.
- **The sentence after it** does not follow as written. PP63's repair is correct: take E inside {Y strictly w-better} and small. Then Z ⪯_w X and Y ⪯_w Z are accepted by global (L0⁺), and X ⪯_w Z is refused by strict (G), so X ⋠_w Y.
- **Cor E.2(i)** is correct.
- **Cor E.2(ii), sharpened.**
  - Put X₀ = C_{u_t}, with X₀ ⪯_v X accepted and V_v < 0.
  - Take E inside {X strictly v-better than X₀} with |∫_E δ| < |V_v|, and Z = X₀[E ↦ X].
  - Z ⪯_v X₀ is **guidance-accepted**, and X₀ ⪯_v Z is guidance-refused.
  - So (TC) on X₀ → X → Z forces the refusal of the specific u¹-favourable link **X ⪯_v Z**, for every such small E.
  - "Refuse one of the two links" (PP63) is therefore "refuse this one". The V0 model's 30 refused-favourable split records are of this kind.

---

## 3. PP63

### 3.1 Lemma 3.1 and Cor 3.2 (PROVED: correct for the listed clauses; scope repair)

I checked each clause.
- **Strict (G).** (U2) excludes exactly the records that guidance accepts.
- **(TC).** An accepted ⪯′-triangle at i avoids 𝒰. Its reverses lie outside 𝒰 by (U1), and they were accepted by (TC) for ⪯.
- **Undominatedness and direct (C) of members.** If X ⪯′ C_a at all worlds, then X ⪯ C_a at all worlds, so C_a ⪯ X at all worlds. At world i, rec(C_a, X) ∉ 𝒰 by (U1).
- **Part (c).** Openness is preserved because the new refusal set is a union of two open sets (Lemma 1.1(b)).
- **Cor 3.2.** A d-ball of radius < δ₀ keeps both kinds of point.

The re-runs `surgery63.py 0` and `surgery63.py 1` reproduce PP63's output (ALL PASS).

**Repair (scope).** "Admissible" in Cor 3.2 must mean the module's axioms: M7 protection for selected models only. Refusal surgery can destroy dominations, so:
- **(C∃)** survives only through KKM, i.e. when (S) holds on all of Δ;
- **(C_dir)** can fail for a coherent model that the surgery newly makes undominated. The mechanism is exactly §4.2's.
- **(C_dir) is preserved if the input satisfies (C⁺).** This is the proof of Prop L3 below, with "after surgery" in place of "at the limit".

In Brief 55's global setting, Lemma 3.1 must therefore be stated with "(S) on Δ and (C⁺) at input" as hypotheses.

A smaller point: in (b), "another world" should read "another world in supp a".

### 3.2 Lemma 4.1 (PROVED: correct)

- (a) is openness.
- (b) is (a) plus defence at interior a′.
- (c) is pigeonhole plus closedness.

### 3.3 Prop 2.1 and Prop 2.2 (PROVED / CHECKED: correct)

**Prop 2.1.** I re-derived (i)–(iii) from the two-valued pair calculus.
- On σ⁺ ∩ A_b and σ⁻ ∖ A_b, C_{a_t} = C_b.
- σ⁺ ∩ D_ab = σ⁺ ∩ A_b and σ⁻ ∩ D_ab = σ⁻ ∖ A_b.
- X″ agrees with C_{a_t} exactly off F ∪ (σ ∖ D_ab). On σ ∩ D_ab, C_{a_t} = C_b.

**Prop 2.2.** The re-run `shift63.py` passes. I also give a **t-uniform** proof (`shift_ref.py`, all 36 cases).
- At a facet point g of A_a, the shift changes f_v by s·t·m_{v,w}a_w g_w.
- So the layer sits on the a-silent side iff s·g_w > 0.
- If g is off ∂A_b, σ_t ∩ D_ab contains an open set for **every** small t iff C_b answers (in the first case) or is silent (in the second) at g.
- An exact facet witness exists in every one of the 36 cases.

### 3.4 Props 4.4–4.6 and Cor 4.5 (PROVED: correct)

- **Prop 4.4.** The quantifier order is "relation first, then scales". Each clause is Lemma 4.1(a) contraposed.
- **Cor 4.5.** It follows from Theorem C as stated.
- **Prop 4.6.** It is Theorem C applied to the cascade's countable pairs. The sign bookkeeping is right: the v ∉ R acceptances are q-favourable and u¹-unfavourable along e_w for w ∈ R.

See 1.2 for the wording about levels.

### 3.5 Theorem J (PROVED: correct with repair (scope); kite CHECKED independently, `kite_ref.py`)

**The proof.**
- **Lyapunov.** The set V_a is convex.
- **Separation.** It gives λ(a) ∈ Δ, and λ(a)·φ_a ≥ 0 a.e.
- **(N2C).** This makes the two half-planes disjoint on Δ.
- **Radon.** It applies to four points, coincident or collinear ones included.

**My re-check of the kite**, with my own advice code at both scales:
- (2V) holds at the four points;
- all 7 bipartitions are realised;
- all 12 forms are non-zero, so each bipartition holds on an open cone;
- the answerers share one sign;
- the problems have mixed signs.

**Repair.** The kite's diagonal bipartition uses the corner problem g = (−7, −7, 23), whose two active forms vanish **at u**. So the theorem is proved for N containing a neighbourhood of u (e.g. PP61's N at scale 10⁻⁶). "Every genuinely two-dimensional N" needs the same construction at an interior point of N: choose g with f₁(a; g) = f₂(a; g) = 0. That is plausible but not checked.

---

## 4. The decreasing-limit lemma and the audit's cautions

**Setting.**
- The selection p ↦ C_p is fixed on an index set I. Write I = Δ for a full selection, or any I ⊆ Δ for a partial one.
- (⪯^α)_{α<λ} is a chain of relations, decreasing in α, indexed by an ordinal (or any directed set).
- The limit is ⪯^λ := ⋂_α ⪯^α at each world.
- **Two facts used throughout.**
  - (F1) An acceptance at the limit is an acceptance at every stage.
  - (F2) A refusal at some stage is a refusal at the limit and at every later stage.

### 4.1 Lemma L1 (PROVED)

If every stage satisfies the clause in question, the limit satisfies it.

- **(a) Reflexivity, (IB) and strict (G).**
  - Reflexivity and (IB): if each verdict is a function of the record, so is the intersection.
  - Strict (G): its acceptances are present at every stage (F1-dual), and its refusals at some stage (F2).
- **(b) (TC).** If A ⪯^λ B ⪯^λ C ⪯^λ A at w, then the same holds at every stage (F1). So the reverses are accepted at every stage, hence at λ.
- **(c) Closed fixed-rival sections.** A^λ_w(X) = ⋂_α A^α_w(X) is an intersection of closed sets. This uses that the selection is fixed.
- **(d) Support defence.** S_α := {w ∈ supp p : C_p ⪯^α_w X} is non-empty and decreasing in α. A decreasing chain of non-empty subsets of a three-element set is eventually constant, so ⋂_α S_α ≠ ∅.
  - Equivalently: if every w ∈ supp p were refused at some stage α_w, then the stage max_w α_w would refuse all of supp p.
- **(e) Undominatedness of a model M protected at every stage** (cofinally many stages suffice).
  - Suppose Y ⪯^λ_w M at every w and M ⋠^λ_k Y.
  - Then M ⋠^{α₀}_k Y at some stage α₀ (F2), while Y ⪯^{α₀}_w M at every w (F1).
  - So Y dominates M at α₀. Contradiction.
- **(f) Direct (C) of members.** "Some world refuses X ⪯ C_p" (X incoherent) persists by (F2). The coherent case is (e).

### 4.2 What the limit gives for global (C)

**Prop L2 (C∃ is automatic for a full selection; PROVED).** Suppose I = Δ and every stage satisfies (S) and the members' direct (C). Then the limit satisfies (C∃).

*Proof.*
1. By L1 the limit satisfies (S).
2. For any N, the sets A^λ_w(N) are closed (L1(c)), and support defence (L1(d)) makes them a KKM cover of Δ. So some p has C_p ⪯^λ_w N at every w.
3. If N is undominated at λ, then N ⪯^λ_w C_p at every w, i.e. N ≈ C_p at λ.
4. If N were incoherent, the members' direct (C) at any stage refuses N ⪯_k C_p for some k, and this persists (F2). Contradiction. ∎

The proof never uses the stages' (C∃). So **(C∃) cannot be lost at a limit of full-(S) stages**, and stages that fail (C∃) while satisfying (S) and members' direct (C) do not exist (KKM).

**Prop L3 (C_dir under (C⁺); PROVED).** Suppose, in addition to L2's hypotheses, that every stage satisfies (C⁺). Then the limit satisfies (C_dir), and in fact (C⁺).

*Proof.*
1. Let N be coherent and undominated at λ. By L2's KKM step, N ≈ C_p at λ, hence at every stage (F1).
2. C_p is protected at every stage, so (C⁺) at stage α makes N coherent and undominated at α.
3. If X ≈ N at λ, then X ≈ N at every stage, so (C⁺) makes X coherent and undominated at every stage. By L1(e), X is undominated at λ. ∎

So under (C⁺) the audit's scenario ("a coherent model becomes undominated only at the limit") **cannot occur**: N was protected at every stage.

### 4.3 Caution 1 confirmed: an explicit failure (CHECKED, `limit_toy.py`)

The selection is partial: one assigned index, with T at u, as in a Brief 55 partial system.

**Models and stages.**
- Coherent models: T, N, D, D₂. Incoherent models: X, Y₀, Y₁, ….
- Stage n accepts, besides reflexivity:
  - T ⪯₁ Z for every Z;
  - X ≈ N at every world;
  - D ⪯ X at every world, and D₂ ⪯ Y_j at every world;
  - Y_j ⪯₂ N and Y_j ⪯₃ N for every j;
  - Y_j ⪯₁ N iff j ≥ n.
- Everything else is refused. The chain is decreasing.

**At every stage (checked):**
- (TC) holds: there is no accepted 3-cycle;
- T is defended, undominated, and satisfies direct (C);
- (C∃) holds: D dominates X, and D₂ dominates each Y_j;
- N is dominated by Y_n, so the coherent undominated models are exactly T, D, D₂;
- (C_dir) and Rule IV hold.

**At the limit:**
- no Y_j ⪯₁ N survives, so N is coherent and undominated;
- its all-world tie partner X is incoherent, so **(C_dir) fails**;
- (TC) and (C∃) still hold.

**Reading.**
- The example satisfies Rule IV at every stage and still fails. The only missing ingredient is the KKM step of L3, i.e. a selection covering Δ.
- So for partial systems the caution is exactly right. A limit taken before the selection is complete must carry (C_dir) as an explicit obligation.
- The example is abstract: (IB) is vacuous and there is no guidance pair. It shows that the lemma's listed items do not imply (C_dir). It is not a construction in the Gaussian domain.

**Full selection without (C⁺): OPEN, but heavily constrained.** Suppose I = Δ, every stage satisfies (S), members' direct (C) and (C_dir), and the limit fails (C_dir) through N and X. Then (PROVED, from L1–L2, (TC) and KKM):

- (i) N is dominated at **every** stage. Otherwise (C_dir) at that stage refuses X ⪯_k N permanently.
- (ii) P_N := ⋂_w A^λ_w(N) ≠ ∅ is closed, and N ≈ C_p for every p ∈ P_N at every stage. So (C⁺) fails at every stage.
- (iii) Take p ∈ P_N.
  - At each world, X and C_p are tied or incomparable. If C_p ⪯_w X, then (TC) on C_p → X → N → C_p forces X ⪯_w C_p, and conversely.
  - At least one world k(p) is incomparable.
  - The refusal set {q : C_q ⋠_{k(p)} X} is an open neighbourhood of p.
- (iv) P_X := ⋂_w A^λ_w(X) ≠ ∅ is disjoint from P_N, and every q ∈ P_X is incomparable with N at some world.

Item (iii) is a single-world incomparability, open in the source, between a member and an incoherent model. This is the configuration of PP62 Cor E.2 and PP63 Cor 3.2.

By hand argument (not written out here), two simple member structures cannot host (i)–(iv):
- translation-invariant cone relations (C_p ⪯_w Z iff π(C_p) − π(Z) ∈ K_w);
- per-world total preorders on members.

In both, (TC) through N forces P_X ⊆ P_N. I did not find a full-selection counterexample. **The recommended invariant is (C⁺)**, which AUDIT_completion's closure already maintains.

### 4.4 Cautions 2 and 3

**Caution 2 (confirmed, sharpened).** By (F1)/(F2), an all-world tie survives to the limit **iff** it is present at every stage. A constant chain shows that the limit repairs nothing by itself. By L2, failures of (C∃) under full (S) can only come from a failure of the members' direct (C), and those are also never repaired unless some stage repairs them.

**Caution 3 (confirmed).** The sections A^n = [1/n, 1] are closed, each point changes once, and the limit (0, 1] is not closed. This requires refusals to be **withdrawn**, i.e. acceptance sets to increase; in a decreasing chain L1(c) holds.

**Positive form (PROVED).** Suppose every final refusal at (p, X, i) is a commitment carrying a fixed open U ∋ p. Suppose also that commitments are never withdrawn and every index is eventually assigned. Then every q ∈ U is eventually assigned and refuses X at i, so the final refusal set is open.

In the [1/n, 1] example, the point 0 is refused at every stage, but only with the shrinking neighbourhoods [0, 1/n). It never has a fixed reservation, so the positive form does not apply there. This matches Brief 55's "built into the invariant".

### 4.5 Recommendations for Brief 55's extension lemma

1. **Carry (C⁺) in the invariant**, as AUDIT_completion Rule IV with "registered" in place of "protected". L1 + L3 then pass global (C) to the limit, **once the selection covers Δ**.
2. **Before that, carry (C_dir) as an obligation.** In a partial system, every coherent model that could become undominated keeps its tie partners under a disjunctive obligation. §4.3 shows the limit will not discharge this.
3. **Only refusals may change across limit stages.** Withdrawn refusals must be provisional, and they are exactly what caution 3 forbids at the end. A growing selection is outside L1: the lemma is for a fixed selection.
4. **State Lemma 3.1-type surgery inside the invariant** with the same hypotheses as L3, i.e. (S) on Δ and (C⁺) at input.

---

## 5. Computations (`r9/REFEREE54_py/`; run `python3 -I -B <script>` there)

| Script → output | Content | Status |
|---|---|---|
| `check_E2.py` → `check_E2.out` | E2: own records, ranks, (IB), (G), DEF, protection, SEC, (TC) on all triples of all 10 blocks; pattern and germs | independent; 0 violations (143 s) |
| `corE2_rerun.py` → `corE2_rerun.out`, `corE2_V*.pkl` | verbatim run61d that saves its data | re-run; matches `run61d.out` |
| `check_corE2.py` → `check_corE2.out` | V0/V1 models re-verified from vectors; V2 core rebuilt; brute-forced UNSAT and minimal | independent; PASS |
| `r0_vs_V0.py` → `r0_vs_V0.out` | departures of the SAT models from R₀(w₀ = 3) | 13,129 / 38,382 (V0) |
| `corE2_R0test.py`, `corE2_R0tight.py` → `.out` | R₀ kept off the e₃ models and their splits: SAT; kept off the e₃ rows only: UNSAT (15-clause core) | CHECKED (SAT re-verified) |
| `alpha_ref.py` → `alpha_ref.out` | A1, A4 per atom, with the field recomputed in closed form | independent; PASS |
| `kite_ref.py` → `kite_ref.out` | Theorem J kite, own advice code, both scales | independent; PASS |
| `shift_ref.py` → `shift_ref.out` | Prop 2.2 for every small t (facet witnesses, 36/36) | independent; PASS |
| `limit_toy.py` → `limit_toy.out` | §4.3 chain: all stages pass, the limit fails (C_dir) | PASS |
| `rerun_r0_check.out`, `rerun_r0_63.out`, `rerun_shift63.out`, `rerun_surgery63_{0,1}.out` | re-runs of PP62/PP63 scripts (`lobe63` and `kite63` were also re-run) | ALL PASS |
