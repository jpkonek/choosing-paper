# PP10. The coupled module, constructive side: a closed covering rule, and what blocks (TC)

21 October 2026, round 41 (constructive side of `AUDIT_round40_brief.md` §4). Labels as in PP7–PP9:
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation. Rational cones and exact anchor polygons; every sign used is certified against a rigorous error bound (160-bit arb cell masses from PP8's library, or 40-digit mpmath intervals). The script is named.
- **NUMERICS**: pool survival, sampled path points, or a step that is checked only at finitely many points.
- **CONJECTURE / OPEN**: as stated.

Scripts are in `PP10_py/` (`python3 -I -B <script> [cap]`; outputs `*.out`). They import PP8's library (`PP8_py/jd.py`, `pp7core.py`, `configs.py`) read-only. I add no assumption to the programme. Everything is on PP8's e₁ setting `e1_3`: a = (9/10, 1/20, 1/20), ε = 3/10, q = (901/1000, 51/1000, 48/1000), PP8's exact pump cones.

---

## 0. Verdicts

1. **No rule was found that meets every requirement of the module.** The constructive output defined in the brief (one explicit rule with proofs of (G), (IB), (TC), both directions' face defences, closed sections, undominated selected models and no incoherent all-world tie) is **not achieved**. The report gives the best explicit rule found, proves what it does, and isolates exactly what blocks it and every other attempt tried.

2. **The constructive part: rule R_VE (Theorem B, PROVED).** R_VE is one explicit record-level formula. It decides forward defences, reverse defences, returns, selected-to-selected and rival-to-rival comparisons together. It uses no priced initial order, no 4:1 pool, no deletion, and no protection priority. It satisfies:
   - reflexivity, strict (G) and (IB);
   - closed accepted-record sets, hence closed sections {p : C_p R_i X} for every rival X along every continuous selected path;
   - **every face obligation of (S), in both directions, for every record of the full four-advice domain and every member of the family, not only on the module.** This includes vertex, edge (PP8 F-B's edge among them) and interior obligations.
   
   The rule uses two fixed additive fields:
   - E_i = ∫ r_i dμ (PP7's L_i);
   - V_i = E_i + J_i, with J_i = ∫_{M_i} r_i dμ.
   
   R_VE accepts an anchored record at world i when ΔV_i ≥ 0. It accepts by E_i only as an edge fallback: the record is anchored on an edge containing i and V fails at both edge worlds.

3. **Two exact covering fields (Proposition 2.2, PROVED).**
   - V is *interior-perfect*: for every anchored record, Σ_i ΔV_i ≥ 0.
   - E is *edge-perfect*: for every record anchored on the edge Δ_ij, ΔE_i + ΔE_j ≥ 0.
   - Neither covers the other's faces on the module (CHECKED by the anchor table).
   
   So the face obligations alone are cheap. All the difficulty lies in (TC), direct (C) and undominatedness, coupled with closedness.

4. **Where R_VE fails. The failures are exactly located.**
   - **(TC), open failure (Proposition 4.1, PROVED; instance CHECKED).** Every (TC) violation of R_VE has one of two forms:
     - a triangle at an edge world that mixes an E-fallback link with a V-link;
     - an exact V-null cycle.
     
     The certified instance is the PP8 F-B triangle C_a ⪯₂ C_p ⪯₂ Y ⪯₂ C_a with C_p ⪯₂ C_a refused, at the fallback world 2. All its signs are strict, so it persists on an open set of rivals and paths.
   - **Direct (C) fails at the brief's own mirror rival (Proposition 4.3, PROVED; data CHECKED).** Take Y_plus with exactly equal masses on the three classes. It has ΔV ≡ 0, and its reverse is anchored at q. So C_a and Y_plus are tied at every world. This tie is **forced by closed sections** for every rule that contains all strict V-acceptances.
   - **Undominatedness at exact edge-balance (Proposition 4.2, PROVED).** With the closed argmax fallback, C_a is dominated by the balanced rival Y* of Theorem D. An index tie-break removes this inside the module (§4.2).

5. **Constraints that every rule must meet on the module (PROVED).**
   - **Theorem C (no fixed fields).** No assignment of one strictly positive integrable rank-step field per world, of any problem- or level-dependence, endorses the interior defences out of C_a together with the Δ₁₂ returns out of an edge model.
     - Corollary C′: if worlds 1 and 2 are additive and world 3 is lexicographic, then world 3's first level must ignore its level-1 steps on R₁ ∪ R₂. On the module this is exactly the minority-first structure that the brief's diagnostic targets.
   - **Theorem D (section quarantine; signs CHECKED).**
     - *Setting.* Y* is C_a with majority advice on exactly balanced sub-cones of R₁ and R₂, a strict pointwise world-3 improvement of C_a. The path is p(t) = (1−t)a + t e₃.
     - *Conclusion.* Every rule with strict (G) and closed sections refuses C_{p(t)} ⪯₃ Y* for all small t > 0. Hence world 1 or 2 must accept it, although the additive balance is negative at both worlds (certified for every t ∈ (0, 10⁻⁵]).
     - *Corollary D′.* A J₃-first lexicographic world 3 therefore has a non-closed section (relies on a NUMERICS step).
   - **Theorem E (forced roles at Y*).** Undominatedness and the Δ₁₂ obligation give the return of Y* to exactly one edge world. World 3 cannot defend near a. By (TC), the return world may defend a nearby C_p only if it does not rank C_a strictly above that C_p.

6. **Finite exact screens (CHECKED on pools; discovery only).**
   - Unrestricted record assignments are SAT on module pools of up to 100 models (2.6·10⁶ (TC) clauses). The constraints are: all obligations, undominatedness, no incoherent all-world ties, and the section quarantine of Theorem D.
   - Assignments restricted to R_VE's acceptances are also SAT.
   - The exact minimal repair of R_VE (MaxSAT) removes only V-acceptances at the fallback world 2: 21 changes at 40 models, 30 at 60. These include selected-to-selected comparisons and defences of transferred rivals.
   - So **stop condition 1 applies**: unrestricted assignments work and no priority patch is proposed. What is missing is a record-level rule that makes the "fallback world becomes additive near the doubly explained record" choice consistently (§7, B5).

7. **Diagnostic (brief §2).** R_VE's defences are **not** all endorsed by a fixed minority-first lexicographic ranking. Y_minus, for example, is defended by V and E, where (J_i, E_i) prefers Y_minus. But every R_VE acceptance is endorsed by **one of two fixed additive fields**: V_i = E_i + J_i (the brief's αJ_i + E_i with α = 1) or E_i. R_VE's only non-additive feature is the switch between them by anchor face. It therefore **does not supply a new non-additive mechanism**, and I do not present it as one. Theorem C shows the module needs genuine non-additivity at some world. R_VE has it only through the switch, and its (TC) failures sit exactly at the switch.

---

## 1. The module

**Problems and ranks.** These follow PP7.
- On a mixed problem g ∈ M_w (world w alone in the minority), the advice labels have these ranks:

  | advice | rank at w | rank at j ≠ w |
  |---|---|---|
  | A (majority) | 2 | 0 |
  | S (silent) | 1 | 1 |
  | B (minority) | 0 | 2 |

- On unanimous problems: correct 0, silent 1, wrong 2. Contradiction: 3 everywhere.
- E_i(X) = ∫ r_i(g, X) dμ = ν(U_i(X)), and J_i(X) = ∫_{M_i} r_i dμ.
- V_i := E_i + J_i, i.e. world i counts its own minority class twice.
- For a record d: ΔE_i(d) = b_i(d) = ν(P_i) − ν(Q_i), and ΔV_i, ΔJ_i likewise.

**Module 𝔐 (brief §4, items 1–6).**
- *Bases.* C_a; C_q; the selected paths through a used in PP8 (v = (1,−1,0), (0,1,−1)) together with p(t) = (1−t)a + t e₃; and the analogous paths through q.
- *Regions.* PP8's exact cones: R_w ⊂ M_w where C_a is silent and C_q says A (w = 1, 2, 3), and T ⊂ M₁ where both are silent.
  - Cone masses (solid angle/4π; each problem counts g and −g): μ(R₁) = 1.674·10⁻⁶ and μ(R₂) = 1.2555·10⁻⁶, arb-certified.
  - μ(R₃) ≈ μ(R₂): PP8 carves the two to the same target.
  - Record masses in the tables are problem masses, twice the cone masses.
- *Rivals.* Every measurable splice of a base with advice in {A, S, B} on any measurable subsets of R₁, R₂, R₃ and T: the majority rivals, their minority counterparts and all mixtures, at all masses.
- *Records.* Every transfer of such a record into another context (IB).
- *Obligations.* Face obligations in both directions (anchor plan §3): d ∈ H_I ⇒ W(d) ∩ I ≠ ∅.

**Anchor table (CHECKED, `m0_anchor_table.py`, exact polygons for the whole cones).** The faces met by A(d), by the old-side pattern on (R₁, R₂, R₃), with '-' meaning not in D:

| old side | faces | role |
|---|---|---|
| SSS (any sub-pattern of S) | interior only | defences out of C_a: interior obligation only |
| AAA | Δ₁₂, interior | reverse of Y_plus: the PP8 F-B edge obligation |
| AA- | e₃, Δ₁₂, Δ₁₃, Δ₂₃, interior | maj→S on R₁ ∪ R₂: guidance at 3, and Δ₁₂ |
| A-A / -AA | e₂ (resp. e₁), edges, interior | |
| BBB, BB-, BS-, SB-, SSA | **empty** | e.g. the reverse of Y_minus is unanchored |
| AAAS (with T) | interior only | the pump return rec(Y, Z) |

Sub-records have larger anchor sets (fewer constraints), so every face listed for a whole-cone pattern is met by all its sub-patterns. Only that direction of the table is used below.

---

## 2. Two exact covering fields

**Lemma 2.1 (pointwise; PROVED).** Let o be regular at g: not contradictory, and correct if g is unanimous. Let n be any advice, and δ_i = r_i(g, n) − r_i(g, o).
- (a) Σ_i (δ_i + 1_{g∈M_i} δ_i) ≥ 0. Equality holds iff n = o, or g is mixed and n is regular.
- (b) Let {i, j, k} = {1, 2, 3}. If additionally o is correct for i and j whenever g ∈ M_k, then δ_i + δ_j ≥ 0.
- (c) If o is correct for world i, then δ_i ≥ 0.

*Proof.*
- On g ∈ M_w with n regular, δ_w = −δ_j = −δ_k (PP9 Lemma R). So the sum in (a) is 2δ_w + δ_j + δ_k = 0. For (b): if w ∈ {i, j}, then δ_i + δ_j = 0.
- If n = contradiction, every δ is positive.
- If g is unanimous, o has rank 0, so every δ_i ≥ 0; the J-terms vanish there.
- If g ∈ M_k in (b), o has rank 0 at i and j.
- (c) is immediate. ∎

**Proposition 2.2 (PROVED).** Let d be a record with q ∈ A(d).
1. Σ_i ΔV_i(d) ≥ 0. This holds for every q ∈ Δ, since every C_q is regular: K_q ⊆ Δ.
2. If q ∈ relint Δ_ij, then ΔE_i(d) + ΔE_j(d) ≥ 0. Here K_q = {q} is precise, and on g ∈ M_k its sign q_i g_i + q_j g_j is the majority's, a.e.
3. If q = e_i, then d is a pointwise weak world-i worsening, i.e. guidance at i.

*Proof.* Integrate Lemma 2.1 (a), (b), (c) over D, using o = C_q on D. ∎

So **V covers every interior obligation and E covers every edge obligation, with no slack parameter.** By contrast, PP8 needed κ = 4 and audit's Theorem 3.

**Neither suffices on 𝔐 (PROVED from the table).**
- *E fails at the interior.* Y_plus has ΔE_i = 2x_i − X < 0 at every world whenever x lies in the triangle cone {x_i < x_j + x_k}.
- *V fails at Δ₁₂.* Take maj→S on R₁ ∪ R₂ ∪ R₃ with masses (x, x, x₃) and x₃ < x. Then ΔV₁ = ΔV₂ = X − 3x < 0, although the pattern is Δ₁₂-anchored.

---

## 3. The rule R_VE

For a record d and a world i, put d ∈ R_i iff one of the following holds:
- **(G)** d is a pointwise weak world-i worsening. This includes the identity.
- **(V)** A(d) ≠ ∅ and ΔV_i(d) ≥ 0.
- **(F)** For some edge I = {i, j} ∋ i, all of the following hold:
  - A(d) ∩ Δ_I ≠ ∅;
  - max(ΔV_i(d), ΔV_j(d)) ≤ 0;
  - ΔE_i(d) ≥ 0;
  - ΔE_i(d) ≥ ΔE_j(d).

  This is the edge fallback, at the edge world(s) where the rival's additive advantage is smallest. The version `fallback='all'` in the scripts drops the last condition.

**Theorem B (PROVED).** R_VE is reflexive and satisfies strict (G) and (IB). Each R_i is closed in PP5's record metric, so every section {p : C_p R_i X} along a continuous selected path is closed. Every face obligation of every record holds: for any rival, any family member, and both directions.

*Proof.*
- *(IB).* The clauses use only D, the old advice, the new advice, ν, μ and A(d).
- *Strict (G).* The reverse of a strict pointwise world-i worsening has ΔE_i < 0 and ΔJ_i ≤ 0, so ΔV_i < 0. Each clause then fails: (G) and (V) directly, and (F) needs ΔE_i ≥ 0.
- *Closedness.*
  - The pointwise worsenings form a closed set: an a.e. inequality is preserved under convergence in measure.
  - {A(d) ≠ ∅} and {A(d) ∩ Δ_I ≠ ∅} are closed, by the compactness and closed graph of the anchor plan §2.
  - ΔE_i and ΔV_i are ρ-Lipschitz, since their integrands are bounded (|δ_i| ≤ 3 and |δ_i(1 + 1_{M_i})| ≤ 6). Max, ≤ and ≥ are closed conditions.
  - A finite union of closed sets is closed. Sections are then closed because p ↦ rec(C_p, X) is continuous: C_p is continuous in measure (plan §1).
- *Obligations.*
  - Interior: by Proposition 2.2(1), some i has ΔV_i ≥ 0, so (V) applies.
  - Edge I = {i, j} met by A(d): if some world of I has ΔV ≥ 0, (V) applies there.
  - Otherwise both ΔV are negative. Then A(d) ∩ Δ_I contains no vertex: a vertex anchor makes d guidance at that world, with ΔV > 0. So it contains a relative-interior point, and 2.2(2) gives ΔE_i + ΔE_j ≥ 0. The larger is ≥ 0, and (F) applies at it.
  - Vertex: guidance, by 2.2(3). ∎

**What R_VE does with the brief's objects (PROVED, by evaluating the clauses).**
- *Y_plus (masses x).* Defended at every world with 3x_w ≥ X. That is at least one world, and two in the "balanced" region U = {x₁, x₂ > X/3}. Its reverse is accepted by V where 3x_w ≤ X. On Δ₁₂ it falls back to E only when x₁, x₂ > X/3.
- *Y_minus.* Defended by V or E at the worlds where it is not better. Its reverse is unanchored (BBB is empty) and is refused everywhere. So C ≺_i Y_minus is strict wherever it is defended.
- *PP8's pump F-A.*
  - The return rec(Y, Z) has the interior-only pattern AAAS, so it is evaluated by V.
  - At the defending world 1, ΔV₁ = −1.925·10⁻⁶ < 0, so the return is refused and the pump triangle does not form.
  - This is CHECKED: `m3_rule_VE.out` shows 0 violations at world 1. Under the plain union rule R_U = (G) ∪ {anchored, max(ΔE, ΔV) ≥ 0} the same pool has the PP8 pump violation and C_a dominated by Y (`m2_union_rule.out`).
- *Mixed pools.* PP8's edge triangle F-B and the rival families carry over; see §4.

---

## 4. Where R_VE fails

### 4.1 (TC)

**Proposition 4.1 (PROVED).** Every (TC) violation of R_VE at world i is one of:
- (α) a triangle containing a link accepted *only* by (F) (so ΔV_i < 0 ≤ ΔE_i) and a link with ΔV_i ≥ 0;
- (β) an exact V-null cycle: all three links have ΔV_i = 0 and are anchored, and the strict link has an unanchored reverse.

*Proof.*
- Suppose no link is (F)-only. Then every link has ΔV_i ≥ 0. A nontrivial guidance link has ΔE_i > 0 and ΔJ_i ≥ 0, so ΔV_i > 0.
- V_i is a potential, so ΔV_i sums to 0 around the cycle. Hence every link has ΔV_i = 0, and there is no guidance link.
- The reverse of a link with ΔV_i = 0 also has ΔV_i = 0. It is accepted iff it is anchored. So a strict link needs an unanchored reverse. This is (β).
- Otherwise some link is (F)-only, so it has ΔV_i < 0. Since ΔV_i sums to 0, some other link has ΔV_i > 0. That link is a V-link or a guidance link. This is (α). ∎

**Certified instance of (α) (CHECKED, `m7_RVE_certificates.py`).**
- *Models.* C_a; C_p with p = a + 10⁻⁶(1, −1, 0); Y_x = C_a with A on R₁, R₂ and one fifth of R₃.
- *World 2.* Every decisive sign below exceeds its rigorous error bound (about 10⁻¹⁹ to 10⁻²⁰).

  | link at world 2 | accepted by | ΔE₂ | ΔV₂ |
  |---|---|---|---|
  | C_a ⪯ C_p | (V) | +7.63e-7 | +1.114e-6 |
  | C_p ⪯ Y_x | (V) | −2.10e-6 | +5.79e-8 |
  | Y_x ⪯ C_a | (F): Δ₁₂-anchored; ΔV₁ = −3.68e-6, ΔV₂ = −1.17e-6; ΔE₁ = −3.3e-7 < ΔE₂ = +1.34e-6 | +1.34e-6 | −1.17e-6 |
  | C_p ⪯ C_a | refused | −7.63e-7 | −1.114e-6 |

- This is PP8's F-B shape. The fallback world must hold the return. V then orders C_a strictly below C_p, and C_p's defence against Y_x passes through V.
- On the pools of `m3_rule_VE.out`, every violation of R_VE (argmax fallback) has the source words (V,F,V), (F,V,V) or (F,V,G), all at world 2. These are 12 and 10 ordered triples.

### 4.2 Undominatedness at exact edge-balance

**Proposition 4.2 (PROVED).**
- *Rival.* Let Y* = C_a with A on S₁(s*) ∪ R₂, where S₁(s) = shrunk(R₁, s) and μ(S₁(s*)) = μ(R₂). Such an s* exists by the intermediate value theorem, since μ(R₁) > μ(R₂) (certified in `m6_quarantine_certificate.out`).
- *Claim.* Under R_VE with the closed argmax fallback, C_a is dominated by Y*.

*Proof.*
1. rec(Y*, C_a) has the old pattern A on R₁ and R₂, i.e. AA-.
   - It is guidance at world 3: majority advice on M₁ ∪ M₂ is correct for world 3.
   - It is Δ₁₂-anchored.
   - ΔV₁ = ΔV₂ = −x < 0 and ΔE₁ = ΔE₂ = 0, so (F) accepts it at both 1 and 2.
2. So Y* ⪯_i C_a at every world.
3. Y* is a strict world-3 improvement of C_a, so C_a ⪯₃ Y* is refused. ∎

*Repair inside the module.*
- With R_VE, the Δ₁₂ anchoring of the returns rec(C_p, X*) is present only at p = q, where X* = C_q silenced on the same cones. At q + 10⁻⁶v the anchor set is interior-only for all ten directions tried (CHECKED, `m10_return_near_q.py`).
- So an index tie-break at exact ΔE-ties (fallback at one world only) keeps the module's sections closed and removes this dominance.
- Outside the module, sections made of edge-anchored records out of boundary models can approach exact ties from both sides. There a single-world tie-break is not closed (OPEN).

### 4.3 Forced V-ties, and direct (C) at the brief's mirror rival

**Proposition 4.3 (PROVED; signs CHECKED, `m9_forced_ties.py`).**
- *Rival.* Let Y_bal = C_a with A on sub-cones S_w ⊆ R_w of exactly equal masses, w = 1, 2, 3. This is the brief §3's Y_plus; equal masses exist by the intermediate value theorem.
- *Claim.* Every rule with closed sections that accepts, at each world i, every anchored record with ΔV_i > 0 among the records below has C_a and Y_bal tied at every world. Y_bal is incoherent, so direct (C) fails. R_VE is such a rule, and there the tie is immediate.

*Proof.*
1. **The two records.**
   - d = rec(C_a, Y_bal) has ΔV_i = 3x − 3x = 0 at every world.
   - rev d = rec(Y_bal, C_a) is anchored at q (sub-pattern of AAA) and also has ΔV ≡ 0.
2. **Sections at a.**
   - For p near a with C_p still silent on the cones (exact ray test), rec(C_p, Y_bal) = rec(C_p, C_a) ⊕ d. Hence ΔV_i = v_i(p) := V_i(C_a) − V_i(C_p).
   - Σ_i v_i(p) = 0 exactly: V-sums are constant on regular models, by Lemma 2.1(a). The m9 data confirm this to 10⁻²².
   - For each i, some direction gives a certified v_i(p) > 0. The directions are (1,−1,0), (−1,1,0) and (0,−1,1).
   - Along each, v_i/t is certified positive at t = 10⁻⁶, 10⁻⁸, 10⁻¹⁰ and 10⁻¹². The values (1.15372, 0.99307, 0.95325) agree to six digits across scales, and the advice on the cones is unchanged.
   - So rec(C_{p(t_n)}, Y_bal) is accepted at i along t_n → 0. Positivity at *all* small t is not needed: a sequence suffices for closedness.
   - Closedness of {p : C_p R_i Y_bal} gives C_a ⪯_i Y_bal at every i.
3. **Sections at q.** The same argument applies at q to the sections of X_bal = C_q silenced on the S_w. There rec(C_q, X_bal) = rev d, and the directions are (1,−1,0), (−1,1,0), (1,−1,0). It gives Y_bal ⪯_i C_a at every i.
4. **Incoherence of Y_bal.** Its acceptance set is that of C_a together with the small cones S_w (suitably oriented). These cones lie strictly inside silent cells of C_a, at a positive angle from C_a's acceptance cone. So the acceptance set is not convex, and Y_bal is not D_K for any K. ∎

So **V-covering cannot be monotone in a closed rule.** At some world, some strictly V-positive anchored defences near a doubly anchored balanced rival must be refused. The brief's mirror pair is exactly where this bites: Y_plus at equal masses is the V-null point, while Y_minus is harmless because its reverse is unanchored.

---

## 5. Constraints on every rule

### 5.1 No fixed fields; the lexicographic escape is minority-first

**Theorem C (PROVED; the anchoring is CHECKED).**
- *Hypothesis.* Suppose that at each world i, every accepted comparison among the records below is endorsed (weakly) by one fixed strictly positive integrable rank-step field f_i(g, ℓ), of arbitrary dependence on the problem g and the level ℓ.
- *Claim.* Then the following obligations cannot all hold:
  - (I) for every measurable S ⊆ R₁ ∪ R₂ ∪ R₃, some world accepts rec(C_a, C_a with A on S); this is interior, anchored at a;
  - (E12) for every measurable S′ ⊆ R₁ ∪ R₂, some world in {1, 2} accepts maj→S on S′ out of C_e. Here e is a relative-interior point of Δ₁₂ in A(AA- on the whole cones): the table lists Δ₁₂ for AA- but neither vertex e₁ nor e₂. Every sub-record is anchored at e.

*Proof.*
1. **Gordan at a.**
   - The vectors (Δ_i(S))_i range over a convex set as S varies (Lyapunov). By (I) this set misses −int ℝ³₊.
   - Separation gives λ ≥ 0, λ ≠ 0, with λ·h(g) ≥ 0 a.e. on R, where h is the density. Writing a_i = f_i(g, 1) and b_i = f_i(g, 2) at g:
     - (i) λ₁b₁ ≥ λ₂a₂ + λ₃a₃ on R₁;
     - (ii) λ₂b₂ ≥ λ₁a₁ + λ₃a₃ on R₂;
     - (iii) λ₃b₃ ≥ λ₁a₁ + λ₂a₂ on R₃.
   - (i)–(iii) force λ₁, λ₂, λ₃ > 0.
2. **Gordan at e.** In the same way there are κ₁, κ₂ > 0 with:
   - (iv) κ₂a₂ ≥ κ₁b₁ on R₁;
   - (v) κ₁a₁ ≥ κ₂b₂ on R₂.
   
   Put ρ = κ₂/κ₁.
3. **Combination.**
   - (i) with (iv): ρλ₁ − λ₂ ≥ λ₃a₃/a₂ > 0, a.e. on R₁.
   - (ii) with (v): λ₂ − ρλ₁ ≥ ρλ₃a₃/a₁ > 0, a.e. on R₂.
   - These contradict each other. ∎

This is the module form of FF2 Cor 4.3. It uses only defences out of C_a and returns out of one edge model. The rivals must have all masses, so the argument genuinely uses atomlessness, as PP3 warned.

**Corollary C′ (PROVED).** Suppose worlds 1 and 2 are endorsed by positive fields and world 3 by a lexicographic hierarchy of nonnegative fields with first level f₃⁽¹⁾. Then f₃⁽¹⁾(g, 1) = 0 for a.e. g ∈ R₁ ∪ R₂.

*Proof.* Run the same argument on first levels: an all-negative first level means a strict lexicographic preference. With a₃, b₃ now the values of f₃⁽¹⁾, (i)–(v) hold as before. Consider the cases for λ.
- λ₁ = λ₂ = 0, λ₃ > 0. Then (i) and (ii) give λ₃ f₃⁽¹⁾(·, 1) = 0 a.e. on R₁ and on R₂.
- λ₁ > 0 = λ₂. Then (ii) reads 0 ≥ λ₁a₁ + λ₃a₃ > 0, which is impossible. The case λ₂ > 0 = λ₁ fails in the same way through (i).
- λ₁, λ₂ > 0. Adding the two inequalities of step 3 gives λ₃ f₃⁽¹⁾(·, 1) = 0 a.e. on R₁ ∪ R₂. Here λ₃ > 0 by (iii).

In every possible case f₃⁽¹⁾(·, 1) = 0 a.e. on R₁ ∪ R₂. ∎

So the only lexicographic-additive escape lets world 3's first level ignore world-3 improvements on M₁ ∪ M₂. That is the minority-first structure of brief §2, located on the module.

### 5.2 Section quarantine

**Theorem D (PROVED; inputs CHECKED, `m6_quarantine_certificate.py`).** Let Y* be as in §4.2 and p(t) = (1−t)a + t e₃. For any system with strict (G), closed sections and the defence clause, there is t₀ > 0 such that, for all t ∈ (0, min(t₀, 10⁻⁵)]:
- (a) world 3 refuses C_{p(t)} ⪯₃ Y*;
- (b) world 1 or world 2 accepts it;
- (c) b₁ and b₂ of rec(C_{p(t)}, Y*) are both < 0.

*Proof.*
1. **(a).** Y* is a strict pointwise world-3 improvement of C_a, so strict (G) refuses C_a ⪯₃ Y*. If world 3 accepted C_{p(t_n)} ⪯₃ Y* along some t_n → 0, closedness of {p : C_p R₃ Y*} would put a in that section. So such t₀ exists.
2. **(b).** p(t) is interior, so the defence clause needs some world. By (a) it is 1 or 2.
3. **(c).**
   - *Silence on the cones.* C_{p(t)} is silent on R₁ and R₂ for t ∈ [0, 10⁻⁵]. The lower previsions are strictly negative at every cone ray at t = 0 and at t = 10⁻⁵. They are linear in p on the chamber {p₂ = min}, hence negative on the whole segment. They are also linear in g on the cells, hence negative on the cones.
   - *The balance.* So rec(C_{p(t)}, Y*) = rec(C_{p(t)}, C_a) ⊕ rec(C_a, Y*), and the second part contributes 0 to b₁ and b₂ by balance. Therefore b_w = β_w(t) := L_w(C_a) − L_w(C_{p(t)}).
   - *The sign.* Forward-mode interval differentiation of PP6's closed-form L, with t as an interval, encloses dL₁/dt in [0.453, 0.474] and dL₂/dt in [0.00715, 0.0131] for every t ∈ [0, 10⁻³]. So β₁, β₂ < 0 on (0, 10⁻³]. (On [0, 10⁻²] the enclosure of dL₂/dt contains 0.)
   - Pool cross-checks at t = 10⁻⁶, …, 10⁻¹² give β₁ ≈ −0.461t and β₂ ≈ −0.0101t, certified. ∎

**Corollary D′ (PROVED given a NUMERICS step).** A world 3 ranked by (J₃, E₃) lexicographically has a non-closed section {p : C_p R₃ Y*} at a.
- ΔJ₃(rec(C_{p(t)}, Y*)) = J₃(C_a) − J₃(C_{p(t)}) > 0. This is certified at t = 10⁻⁶, 10⁻⁸, 10⁻¹⁰ and 10⁻¹² (exactly linear in t, ≈ 0.2355t). That it holds for *all* small t is the NUMERICS step.
- At t = 0 the record is a strict world-3 improvement and is refused.

The defences that (b) forces at worlds 1 and 2 have additive deficit |β_w(t)| = O(t), against a record mass ≥ μ(R₂). That is, their *relative* non-additivity tends to 0.

R_VE provides them through V:
- ΔV₁ = x − 0.809t + o(t) and ΔV₂ = x − 0.133t + o(t), from the m6 data.
- Here x is the problem mass of R₂, twice its cone mass, so x ≈ 2.51·10⁻⁶.
- Both are positive for t below about 3·10⁻⁶.

### 5.3 Theorem E: forced roles at the balanced doubly explained rival

**Theorem E (PROVED).** Assume reflexivity, strict (G), (IB), (TC), closed sections, the defence clause, and undominated C_a. Then for Y* and p(t):
1. Theorem D (a)–(c) hold.
2. Some world w ∈ {1, 2} refuses Y* ⪯_w C_a, and the other world w′ accepts it.
   - *Refusal at w.* Y* ⪯₃ C_a is compulsory guidance and C_a ⪯₃ Y* is refused by strict (G). So undominatedness needs a refusal at 1 or 2.
   - *Acceptance at w′.* rec(Y*, C_a) is Δ₁₂-anchored.
3. Whenever w′ defends C_{p(t)} ⪯_{w′} Y*, it must not have C_a ≺_{w′} C_{p(t)} strictly. This follows from (TC) on C_{p(t)} ⪯ Y* ⪯ C_a. So at w′ either:
   - the selected comparison is non-additive: C_{p(t)} ⪯_{w′} C_a although β_{w′}(t) < 0; or
   - the additive comparison C_a ⪯_{w′} C_{p(t)} is refused.
4. rec(C_a, C_{p(t)}) must be accepted at world 1 or 2. At world 3 it is the reverse of a strict pointwise improvement.
   - The improvement is weak by Lemma H.
   - It is strict because dL₃/dt ∈ [−0.711, −0.702] on [0, 10⁻³] (m6), so L₃(C_{p(t)}) < L₃(C_a).

*Proof.* Each item is the cited axiom applied to the named records. The anchorings are from the table and §4.2. ∎

So near Y* any solution has three features:
- exactly one edge world holds the return;
- world 3 does not defend near a;
- the return world either does not defend nearby C_p against Y*, or makes its comparison with C_a non-strict.

The theorem does not force which edge world defends.

R_VE breaks these constraints in two places:
- item 2 at exact balance (§4.2);
- the analogue of item 3 for the unbalanced rival Y_x (§4.1).

In both cases the fault is the same: R_VE lets the return world keep V-evaluating the neighbourhood.

---

## 6. Finite exact screens (discovery only)

**The free screen (`m4_sat_screen.py`).** One Boolean x[r, i] per record and world, for every record in the pool: forward, reverse, return, selected and rival-to-rival. There is no initial order.
- *Clauses.*
  - guidance compulsory, strict reverse forbidden;
  - (TC) on every ordered triple;
  - every exact face obligation;
  - undominated selected models;
  - no all-world tie of a selected model with a non-selected one (stronger than direct (C));
  - the quarantine units of Theorem D at p(10⁻⁶).
- *Quarantine filter.* A unit is imposed only when every score sign of the record matches its limit record at a; Theorem D forces refusal only for t < t₀(Y). A first version without this filter gave a spurious pool-mode UNSAT, through a rival smaller than the selected shift (`m8_core.out`).
- *Pool.* C_a, C_{a+10⁻⁶(1,−1,0)}, C_{p(10⁻⁶)}, C_q, PP8's pump Y and Z, four majority and two minority splice rivals, and closure under splicing.

| pool (closure cap) | models / records | free | restricted to R_VE's acceptances |
|---|---|---|---|
| 0 | 12 / 132 | SAT | SAT |
| 60 | 60 / 2,362 | SAT (5.4·10⁵ (TC) clauses) | SAT |
| 100 | 100 / 5,046 | SAT (2.6·10⁶ (TC) clauses) | SAT |

Every SAT state re-checks with 0 (TC) violations, 0 unmet obligations, 0 dominated models and 0 ties.

**Minimal repair of R_VE (`m5_min_repair.py`, exact MaxSAT with RC2).**
- *Starting point.* R_VE with argmax fallback has (TC) violations [0, 170, 0] at cap 40 and [0, 306, 0] at cap 60, all at world 2.
- *Minimal changes.* 21 at cap 40 and 30 at cap 60. **Every one removes a (V)-acceptance at world 2.** The removed acceptances include:
  - the selected comparisons rec(C_a, C_{a+10⁻⁶(1,−1,0)}) and rec(C_a, C_{p(10⁻⁶)});
  - the V-defences of C_a and C_p against the rivals whose Δ₁₂ return world 2 holds;
  - records whose old side is a rival: 2 at cap 40 and 7 at cap 60.
- *Free mode.* The same minimal count. At cap 60 one of the changes adds an acceptance outside R_VE; at cap 40 there are only removals.

**Reading.**
- On finite pools the coupled problem is solvable, and nearly by R_VE itself. The fix is that the fallback world switches to additive evaluation on everything near the doubly explained record.
- Finite pools cannot decide the continuum question (PP3). Theorem C shows the continuum forces non-additivity, which no finite pool sees.
- Stop condition 1 therefore applies: I do not propose a priority patch.

---

## 7. What blocks: the coupled constraints, precisely

- **B1 (coverage forces non-additivity; Theorem C).** Some world's comparisons out of the module's selected models are not endorsed by any fixed positive field. Among lexicographic-additive designs, world 3 must be minority-first on R₁ ∪ R₂.
- **B2 (closedness against monotone evaluators).**
  - *Theorem D, Corollary D′.* A J₃-first world 3 has non-closed sections. Worlds 1 and 2 must take defences that the additive order refuses at both, with vanishing relative deficit.
  - *Proposition 4.3.* A closed rule that contains every strict V-acceptance has incoherent all-world ties at the V-null rival, which is the brief's Y_plus at equal masses.
  
  So the needed non-additive verdicts can be neither a fixed lexicographic order (not closed) nor a monotone use of the exact covering field V (ties).
- **B3 (the obligations are not the obstacle; Theorem B).** R_VE meets every face obligation globally, closed. The coupled difficulty is entirely (TC), (C) and undominatedness.
- **B4 (the switch is where (TC) breaks; Proposition 4.1, Theorem E).**
  - Every open (TC) failure of R_VE is a V/E mix at an edge world.
  - In R_VE the mix occurs exactly at doubly explained rivals: their reverse is anchored at q and on Δ₁₂, and V fails at both edge worlds.
  - Theorem E then requires the return world not to V-order the selected models near a strictly against the rival.
- **B5 (IB against "mode", the remaining obstruction; CONJECTURE that it blocks every record-local selector).**
  - *What the pools show.* At the return world, the comparisons that must change mode are rec(C_p, Y), rec(C_a, C_p) and the transferred rival records: those "between" C_a and Y.
  - *Why a record cannot see this.* A record rec(C_p, Y) is a union of a selected part (C_p→C_a, near ∂K_a) and a rival part (on R), but its per-class score vector mixes them. The two parts use the same transition types (S→A occurs in both).
  - *The best-fit decomposition is unreliable.* Decomposing by the selected model that best fits the new side is scale-dependent. At the module's scales (selected shifts ~10⁻⁶, rivals ~10⁻⁶) the best fit can be C_q rather than C_a. These are the brief's "two coherent explanations".
  - *R_VE itself.* R_VE does not restrict V-acceptances at the return world at all. The §4.1 instance is exactly that.
  - *The natural score-based restriction.* Allow a V-defence d at an edge world only where ΔE(d) is largest, i.e. away from the fallback world of its reverse.
    - Write e_w(p) = E_w(C_a) − E_w(C_p), so ΔE_w(rec(C_p, Y(x))) = e_w(p) + 2x_w − X.
    - For a rival with x₁ > x₂, whose return sits at world 2, the restriction sends the defence of C_p to world 2 exactly when e₂(p) − e₁(p) > 2(x₁ − x₂) > 0. This is a direct computation.
    - Along p(t) we have e₂ − e₁ ≈ 0.45t > 0, and there C_a is strictly V-better than C_p at world 2 (v₂ ≈ −0.133t < 0, m6). So the F-B triangle reappears for 0 < x₁ − x₂ ≲ 0.22t.
    - The signs are CHECKED at t = 10⁻⁶. That this persists for all small t is NUMERICS.

**Not shown.** No contradiction follows from the axioms on this module. Theorems C, D and E and Propositions 4.2–4.3 constrain designs. Every local configuration examined here is satisfiable, and the finite screens are SAT. An adversarial chain would have to combine B4–B5 with the atomless arguments of B1–B2.

---

## 8. Diagnostic and stop conditions

- **The diagnostic (brief §2).**
  - R_VE's interior defences are endorsed by the fixed field V_i = E_i + J_i: the brief's αJ_i + E_i with α = 1, not lexicographic. Its edge fallbacks are endorsed by E_i.
  - It is not endorsed by fixed minority-first lexicographic ranking: the defence of C against Y_minus with ΔE > 0 > ΔJ is accepted.
  - Its non-additivity is only the anchor-face switch between two fixed fields. **It supplies no new non-additive mechanism.**
  - Theorem C, Corollary C′ show what such a mechanism must do on the module: break Theorem C's Gordan structure. R_VE breaks it only through the switch.
- **Stop condition 1.** Applies: the screens are SAT unrestricted and the minimal repairs are clean. No new priority is proposed.
- **Stop condition 2.** No proof here uses fixed minority-first evaluation as a mechanism.
  - Corollary C′: within the lexicographic-additive designs with additive worlds 1 and 2, coverage forces that evaluation.
  - Corollary D′: its J₃-first form is excluded by closed sections.
  - Not excluded here: a problem-dependent first level that is blind both to R₁ ∪ R₂ and to the moving boundary lines of the path. Excluding it would need FF2/S3-type density arguments over many boundary points, which this module does not contain (OPEN).
- **Stop condition 3.** No result here is a theorem about a shrinking subclass presented as settling the problem. Theorem B is global; its failures are stated.
- **Stop condition 4.** The negative statements use the family K_p = p + 3ε min p (Δ − u), PP8's e1_3 cones and the homothetic path p(t) (Lemma H).
  - Theorems C, D and E and Proposition 4.3 are statements about that family and that module. They do not establish that T1 is uncoverable.
  - Theorem B and Proposition 2.2 hold for any selected family whose members are regular and whose boundary members are precise.

**Attempt of the full family with the same rule.** Theorem B's positive properties are global: every record, every p, and closed sections along every continuous path. Its failures (§4) use only:
- a three-class majority splice whose reverse is anchored at a nearby q and on an edge;
- exact balances supplied by the intermediate value theorem.

PP9's `p9_D_search` found such dominating-splice cells in all four settings. That they exist at every interior index is a CONJECTURE (PP5 Prop 4.3 gives the silent cones).

---

## 9. Scripts (`PP10_py/`)

| script → output | content | label |
|---|---|---|
| `pp10lib.py` | J and V per record with error radii; the union rule R_U; R_VE ('all' and 'argmax' fallbacks); triangle typing | library |
| `m0_anchor_table.py` → `m0_anchor_table_e1_3.out` | exact anchor faces for every old pattern on R₁, R₂, R₃, T (three lead worlds) | CHECKED |
| `m1_selected_directions.py` → `.out` | directions at a where C_p is additively worse at worlds 1 and 2 | NUMERICS (used only to choose the path) |
| `m2_union_rule.py` → `.out` | R_U on the pump and edge pools: (TC) violations, PP8 F-A, C_a dominated by the pump Y | CHECKED |
| `m3_rule_VE.py` → `.out` | R_VE on pools with splice rivals: obligations, dominance, violation words | CHECKED (instances) / NUMERICS (pool survival) |
| `m4_sat_screen.py` → `m4_sat_screen{,_cap60,_cap100}.out` | unrestricted and R_VE-restricted exact SAT with quarantine | CHECKED on pools |
| `m5_min_repair.py` → `m5_min_repair_cap{40,60}.out` | exact MaxSAT minimal repair of R_VE | CHECKED on pools |
| `m6_quarantine_certificate.py` → `.out` | Theorem D: interval derivative of L, exact silence on the segment, mass order, J₃ samples | CHECKED |
| `m7_RVE_certificates.py` → `.out` | certified (TC) violation of R_VE at world 2; dominance comparison of R_U and R_VE | CHECKED |
| `m8_core.py` → `.out` | diagnosis of the spurious UNSAT under the unfiltered quarantine proxy | CHECKED |
| `m9_forced_ties.py` → `.out` | Proposition 4.3: v(p) around a and q, sum zero, certified positive coordinates | CHECKED |
| `m10_return_near_q.py` → `.out` | Δ₁₂ anchoring of rec(C_p, X) exactly at q but not at q + 10⁻⁶v | CHECKED |

**Dependencies.** As in PP8: python-flint (arb), mpmath, numpy, pysat (Cadical, RC2).
