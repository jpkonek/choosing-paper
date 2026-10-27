# PP9. Joint defence and weakest-pair deletion: analytic attack

21 October 2026. Brief: attack the candidate in `AUDIT_joint_defence.md` on audit's family K_p = p + 3ε min_j p_j (Δ − u), C_p = D_{K_p}, Gaussian problems on ℝ³.

**Labels**
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation (rational cones, exact cells, exact anchor polygons, interval solid angles at 40 digits; every sign used is certified), script named.
- **NUMERICS**: double precision, evidence only.
- **CONJECTURE / OPEN**: as stated.

**Scripts** are in `PP9_py/`. Run each as `python3 -I -B <script>` inside that folder; each writes a `.out`. They import PP7's exact library (`PP7_py/core.py`) read-only. I add no assumption to the programme.

---

## 0. Verdicts

1. **Q1. No violating triple of R⁰ consists only of protected pairs and guidance (Theorem A, PROVED).**
   - So a protected (s = 1) pair is never the lowest-priority pair of a violating triple, and the deletion never touches it.
   - Every protected defence survives, and with it every face obligation of every protected record.
   - The construction asked for in the brief (two protected strict defences of one rival Y, at worlds j and k, out of the same C_p or of different C_p, C_q, each lowest in some triangle) **does not exist**.
   - The proof rests on one pointwise lemma: a pointwise world-j improvement of a regular model cannot additively improve both other worlds (Lemma R, PROVED; CHECKED by enumeration). An abstract random cross-check finds 0 counterexamples. When one irregular anchor is allowed, it finds counterexamples, so the regularity of anchors is what the proof uses.
2. **The rule nevertheless fails the defence clause (Theorem D, CHECKED in all four settings).**
   - Take a three-cone rival whose cones lie where some other C_q gives the majority answer. Its reverse record then has a coherent completion, so the record is **not protected**, although it is additively dominated at every world.
   - The joint choice gives it exactly one defending world (sticky).
   - One "drop" triangle deletes that defence, so the record is accepted at no world of R. Its anchor p₀ is interior.
   - Settings: near e₁ and near u, ε = 0.3 and 0.1.
3. **Unprotected sticky defences die in general (Theorem B, CHECKED).** On PP7's own family (cones in the largest silent cells), the record S→A on three cones with masses (2.2, 1, 1)a has b = (+, −, −). Its defences at worlds 2 and 3 are deleted by drop triangles.
   - Its world-1 defence is additively safe.
   - An additively safe defence can be deleted only through six specific triangle patterns (Proposition C, PROVED). Whether those patterns are realisable is OPEN.
4. **Q2. The deletion set is not open, and sections are not closed (Theorem E, PROVED from CHECKED data).**
   - Fix the rival X = C_{p₀} with A on S₁(s*) ∪ S₂ ∪ S₃, where s* is chosen by the intermediate value theorem so that b₁(rec(C_{p₀}, X)) = 0.
   - Along p(t) = (p₀ − t e₁)/(1 − t), t ↓ 0, the records rec(C_{p(t)}, X) are protected, hence never deleted (Theorem A).
   - Their limit rec(C_{p₀}, X) is unprotected and is deleted at world 2.
   - So {p : C_p R₂ X} contains p(t) for small t > 0 but not p₀, and the deletion set is not open in the record metric.
   - The mechanism is general: the protected class is open (strict inequalities), and its boundary records are deletable.
5. **Q2, tie-break (Proposition T).** At an exact additive tie of a doubly anchored record, objective 1 forbids accepting both directions, so any tie-break keeps exactly one. Then at least one of the two sections {p′ : C_{p′} R⁰_i C_q} and {q′ : C_{q′} R⁰_i C_p} is not closed.
   - PROVED under hypothesis (H_T): an interior pair with b_i = 0 and the other two b of opposite signs.
   - (H_T) is NUMERICS, found at every world in all four settings.
   - The minimal repair (accept both directions at exact ties) is CONJECTURE.
6. **Q3. PP7's three-cone family (Theorem G, PROVED; Proposition F, PROVED + CHECKED).**
   - Every "A on three cones/annuli" pattern of the family is unanchored. So every return comparison carrying it has no obligation and is refused: the return quarantine is automatic.
   - Every obligation of every family record is met by a protected defence, a guidance defence, or an additively safe (b ≥ 0) defence. The first two survive.
   - Survival on the family is therefore equivalent to survival of the additively safe s = 0 defences, which is OPEN.
   - One of the six patterns, (P,G), is PROVED impossible for the growing and two-growing records.
7. **Q4. Screens.**
   - **S9.** Its literal hypothesis fails, because of the eligibility filter. Its mechanism (P3 Prop 3.4, the drop triangle) is exactly what deletes the sticky defences in Theorems B and D.
   - **PP4 (P)/(T)/(E).** These are consequences of (TC) and hold in R. On the doubly anchored swap layer R⁰ is exactly additive, except that objective 1 violates (E) at exact three-way ties; deletion removes those ties.
   - **FF2 Cor 4.3.** Met at every world with a surviving protected defence (PROVED in outline, conditional on the survival of the additive swap layer).
   - **PP2 Thm 6.** Does not apply. (s, m) is a priority on records used only to choose deletions, not a gate. It is invariant under rearrangement of the steps, and R accepts opposite orientations of disjoint-location swaps at one world, so no fixed key satisfies PP2's (H2).
8. **Nearby result (§7).** "Extended protection" removes Theorem D's mechanism: s = 1 for every accepted, anchored, strictly additively dominated direction whose reverse is not accepted at that world. Theorem A holds verbatim for it (PROVED).
   - It does not repair Q2. A closed protection class breaks Theorem A's proof at the boundary: a degenerate PPG configuration becomes possible (PROVED).
   - Closed sections remain OPEN.

---

## 1. Reading of the rule

I implement `AUDIT_joint_defence.md` literally, with three readings made explicit.

- **(R1)** The priority of a pair is evaluated at the world i where it is present. s = 1 means: the pair contains a direction d accepted at i with A(d) ≠ ∅, A(rev d) = ∅, and b_j(d) < 0 at all three worlds.
- **(R2)** Marking and deletion are per world. A record marked at world i is deleted, with its reverse, from R_i in every context.
- **(R3)** The "pairs in a triple" are its three unordered pairs.
  - In a violating triple all three are present, since each carries a link of the cycle.
  - The faces met by A(d) are its relative-interior faces: those of q ∈ A(d) by supp q.

**Regular model.** A model is regular on a set if, a.e. there, it is never contradictory and is correct on unanimous problems. Every coherent C_q is regular everywhere, since K_q ⊆ Δ. So **A(d) ≠ ∅ implies that the old side of d is regular a.e. on D(d)**.

**Notation.** ⪯_i is accepted on records: X ⪯_i Y iff rec(X,Y) ∈ R_i. P_i are the errors Y adds and Q_i the errors it removes.
- b_i = ν(P_i) − ν(Q_i) = L_i(Y) − L_i(X).
- Φ_i = 4ν(P_i) − ν(Q_i).
- The pair priority is m = Φ_i/(ν(P_i) + ν(Q_i)) = (4r − 1)/(r + 1), with r = ν(P_i)/ν(Q_i). This is increasing in r, so **m ≥ 3/2 ⟺ b_i ≥ 0**.

---

## 2. Q1: protected pairs are never marked

**Lemma R (regular improvement; PROVED, CHECKED `p9_lemma.py` (1)).** Let c be a pointwise weak world-j improvement of a, with a regular a.e. on D = D(a,c). Let u, v be the other two worlds. Then, a.e. on D:
- δ_u + δ_v = 0 on M_u ∪ M_v;
- δ_u + δ_v = 2|δ_j| on M_j.

Hence

    b_u(rec(a,c)) + b_v(rec(a,c)) = 2 ∫_{D∩M_j} |δ_j| dμ ≥ 0.

*Proof.*
1. Every nontrivial change alters the rank at every world (CHECKED, (2)). So δ_j < 0 a.e. on D.
2. On a unanimous problem a is correct, so its world-j rank is 0 and cannot drop. So D misses the unanimous problems.
3. A change to contradiction raises every rank, so it is not an improvement.
4. That leaves regular → regular changes on mixed problems. The two majority worlds move together and the minority world moves opposite.
   - On M_j: δ_u = δ_v = −δ_j.
   - On M_u: δ_v = δ_j and δ_u = −δ_j, and symmetrically on M_v. ∎

The enumeration covers 27 improving cases with 0 violations: 18 with sum 0 (j in the majority), and 9 with sum 2 or 4 (j the minority).

**Lemma P (links of R⁰ at world i; PROVED).**
- **(a)** If a protected d is accepted at i, then rev d ∉ R⁰_i.
  - A(rev d) = ∅, so only guidance could accept rev d.
  - But then d would be a pointwise improvement at i, with Φ_i(d) = −ν(Q_i) < 0, so d could not be accepted.
- **(b)** If a pair carries a compulsory guidance comparison rec(y,x) at i, the other direction is a strict pointwise improvement at i. It is ineligible and not guidance, so it is refused.
- **(c)** Hence at world i:
  - a removable s = 1 pair is exactly a **protected link** X ≺_i Y: strict, X anchored on D(X,Y), and L_l(Y) < L_l(X) at all three worlds;
  - a guidance pair carries only its **guidance link** U ⪯_i V: V is pointwise weakly worse at i.

**Theorem A (PROVED).** At every world i, every (TC)-violating triple of R⁰_i contains a removable pair with s = 0.

*Proof.* Suppose all three pairs are protected or guidance. A violation is a cycle a ⪯_i b ⪯_i c ⪯_i a with a missing reverse. By Lemma P each link is P (protected) or G (guidance). Classify the cyclic words.
- **PPP.** L_l strictly decreases along every link at every world, which is impossible around a cycle.
- **GGG.** Composing pointwise worsenings, every model is pointwise weakly worse than every other. At world i the ranks determine the advice, so a = b = c and there is no violation.
- **PGG (and its rotations).** b ⪯ c ⪯ a are guidance links, so a is pointwise weakly worse than b at i. Then Φ_i(rec(a,b)) = −ν(Q_i) < 0, which contradicts its acceptance.
- **PPG.** a → b and b → c are protected, and c → a is guidance, so c is a pointwise weak world-i improvement of a.
  - *Regularity on D(a,c).* A(rec(a,b)) ≠ ∅, so a is regular a.e. on D(a,b), and b = a off it. Likewise b is regular a.e. on D(b,c), and c = b off it.
  - If a were irregular at some g ∈ D(a,c), then g ∉ D(a,b). So b(g) = a(g), which is irregular, so g ∉ D(b,c), so c(g) = a(g). That contradicts g ∈ D(a,c). Hence a is regular a.e. on D(a,c).
  - Lemma R then gives b_u(rec(a,c)) + b_v(rec(a,c)) ≥ 0.
  - But b(rec(a,c)) = b(rec(a,b)) + b(rec(b,c)) < 0 at every world. Contradiction. ∎

**Corollary A1 (PROVED).** In every violating triple some s = 0 pair has strictly lower priority than any s = 1 pair. So no s = 1 pair is ever marked, and **R_i contains every protected acceptance of R⁰_i**.

Every protected record keeps all its initial defences: at least two, by the κ = 4 theorem. Its face obligations, which the joint choice satisfies in R⁰, remain satisfied in R. This holds:
- at all worlds;
- for rivals defended out of one C_p or out of different C_p, C_q;
- for all realisations of the record, since the argument is record-level.

**Proposition A2 (shape of violations through a protected link; PROVED).** Write the cycle with the protected link first, and label the other two links G (guidance), P (protected) or 0 (s = 0). The possible words are:
- (P,P,0), (P,0,P), (P,0,G), (P,G,0), (P,0,0).

(P,P,P), (P,P,G), (P,G,P) and (P,G,G) are excluded by Theorem A's cases. In every admissible word, an s = 0 link is marked, never the protected one.

**CHECKED cross-check (`p9_lemma.py` (3)).** The abstraction:
- random finite "atom" models (7 atoms over M₁, M₂, M₃, U; random masses);
- a list of regular anchors standing in for the coherent family;
- 50 arbitrary models each, including contradictory ones.

Across 60 instances there are 190 protected links and **0** cycles made only of protected and guidance links. The control (one irregular anchor admitted) produces 6 such cycles. The cycles that mix protected links with ordinary eligible links number 1,086, so the check is not vacuous.

---

## 3. What the deletion does remove

### 3.1 Which triangles can mark an s = 0 link

**Proposition C (PROVED).** Let d = rec(X, X′) ∈ R⁰_l have s = 0 with rev d ∉ R⁰_l, and let {X, X′} be marked at l in a violating triple (X, X′, Z). Then:
- The cycle is X → X′ → Z → X.
- Each of the links X′→Z and Z→X is G, P, or an s = 0 link of priority m ≥ m_l(d).

Suppose moreover that **b_l(d) ≥ 0**, so d is an additively safe defence and m_l(d) ≥ 3/2. Then (X′→Z, Z→X) is one of:

    (P,G), (P,0), (G,P), (0,P), (P,P),   or   (0,0) with b_l = 0 on all three links.

If b_l(d) > 0 the last case is excluded.

The pattern (P,G) moreover needs b_j(d) + b_k(d) > 0 at the other two worlds.

*Proof.*
- Write β for b_l of a link. For an s = 0 link of priority ≥ m_l(d) ≥ 3/2, monotonicity of m gives β ≥ 0. For a G link, β > 0. For a P link, β < 0.
- The β's sum to 0 around the cycle and β(d) ≥ 0. So some link is P, unless all three β are 0.
- (G,G) would make X pointwise worse than X′, which d cannot accept.
- For (P,G): X is regular on D(X, Z), by the argument of Theorem A, using the anchors of d and of the P link. Lemma R then gives b_j(X→Z) + b_k(X→Z) ≥ 0, while b(X′→Z) < 0 at every world. ∎

For the three-cone S→A records, b_j + b_k = −2μ_l < 0, so the pattern (P,G) is impossible for them.

### 3.2 Drop triangles delete unprotected sticky defences

**Theorem B (PROVED).** Let d = rec(X, X′) ∈ R⁰_l be unprotected, with rev d ∉ R⁰_l. Suppose W is a strict pointwise world-l improvement of X with rec(X′, W) ∈ R⁰_l, carried by a pair of priority above (0, m_l(d)). Then d is marked, hence deleted, at l.

The cycle is X ⪯ X′ ⪯ W ⪯ X, and X′ ⪯_l X is refused. This is P3's Prop 3.4 / PP7 Prop 3.1 configuration. The joint rule resolves it in favour of the additive link.

**Instance B1 (CHECKED, `p9_B1.py`, all four settings).** The objects:
- S_w = shrunk(T_w, ·), sub-cones of PP7 t8's base cones (largest silent cell per class), with cone masses (2.2, 1, 1)·a, a = 0.4 τ;
- X = C_{p₀} with A on S₁ ∪ S₂ ∪ S₃;
- d* = rec(C_{p₀}, X);
- Z₂ = C_{p₀} with A on S₃ (a strict world-2 improvement), and Z₃ = C_{p₀} with A on S₂.

| setting | b(d*) | A(rev d*) | d* accepted (R⁰) | rec(X,Z₂) joint choice | world-2 triangle: priorities {C,X} / {X,Z₂} / {C,Z₂} | deleted at |
|---|---|---|---|---|---|---|
| e₁, .3 | (+5.31e−5, −5.84e−4, −5.84e−4) | ∅ (polygon empty) | worlds 1,2,3 | rev at 1; fwd at 2, 3 (3 guidance) | (0, .1905) / (0, 2.4375) / G | worlds 2 and 3 |
| e₁, .1 | (+1.51e−5, −1.66e−4, −1.66e−4) | ∅ | 1,2,3 | same | same | 2 and 3 |
| u, .3 | (+5.37e−4, −5.91e−3, −5.91e−3) | ∅ | 1,2,3 | same | same | 2 and 3 |
| u, .1 | (+1.82e−4, −2.00e−3, −2.00e−3) | ∅ | 1,2,3 | same | same | 2 and 3 |

Details:
- Every joint choice is the certified unique optimum, so objective 4 never acts. It is unchanged when the conservative face sets are replaced by interior-only ones.
- d* is a member of PP7's family: Y(t) with t outside the sticky box.
- After deletion d* keeps only its world-1 defence, which has b₁ > 0. By Proposition C, only the six patterns above can remove it.

### 3.3 The defence clause fails

**Theorem D (CHECKED, `p9_D.py`, all four settings; mechanism PROVED).** The objects:
- q, a selected index near p₀: q = p₀ + (1, 0, −1)/200 near e₁, and q = p₀ + (1, 1, −2)/200 near u.
- "Dominating-splice cells": cells where C_{p₀} is silent and C_q says A. They exist in **all three classes** (`p9_D_search.py`; also at ε = 0.1, through tilted lines).
- λ, the class with the largest such cell; here λ = 3 in all settings.
- Cones in those cells: T_λ of mass 1.2a, and T_j = T_j^drop ⊔ T_j^keep, T_k likewise, with masses 0.9a + 0.1a.
- Z′ = C_{p₀} with A on all five cones, and d = rec(C_{p₀}, Z′).
- E_j, a cone where C_{p₀} and C_q are both silent, of mass 0.05a.
- W = C_{p₀} with A on T_j^keep ∪ T_k^keep ∪ E_j, a strict world-λ improvement.

| setting | b(d) | c(d) | A(d) | A(rev d) | joint choice for d | rec(Z′,W): A(rev) | world-λ triangle: {C,Z′} / {Z′,W} / {C,W} | d in R |
|---|---|---|---|---|---|---|---|---|
| e₁, .3 | (−1.63e−5, −1.63e−5, −1.08e−5) | (.6875, .6875, .625) | ∋ p₀ (interior only) | ∋ q (verified exactly) | world 3 only; rev at 1, 2 | ∅ | (0, .875) / (0, 1.951) / G | **nowhere** |
| e₁, .1 | (−4.30e−7, −4.30e−7, −2.87e−7) | same | same | same | same | ∅ | same | **nowhere** |
| u, .3 | (−2.51e−4, −2.51e−4, −1.67e−4) | same | same | same | same | ∅ | same | **nowhere** |
| u, .1 | (−3.42e−5, −3.42e−5, −2.28e−5) | same | same | same | same | ∅ | same | **nowhere** |

*Mechanism (PROVED given the certified data).*
1. **d is unprotected.** A(rev d) ∋ q because Z′ is a splice of C_{p₀} with C_q, so s = 0 although b < 0 at every world.
2. **d gets one world.** Every non-guidance acceptance of d costs c_l(d) > 1/2, against 1 − c_l(d) for rev d. The defence clause needs one world for d, so objectives 1–3 give d exactly the world λ = argmin c_l(d) (sticky), and rev d the other two.
3. **The triangle at λ.**
   - C ⪯_λ Z′ is d, and Z′ ⪯_λ C is refused.
   - Z′ ⪯_λ W: the W side of rec(Z′, W) is silence on the dropped cones plus A on E_j, which is unanchored (outer polygon empty). So the rule accepts rec(Z′, W) at every eligible world, and b_λ(rec(Z′, W)) > 0 gives priority > 3/2.
   - W ⪯_λ C is guidance.
   - The pair {C, Z′} is the unique lowest and is deleted at λ. p₀ ∈ A(d) is interior, so the clause "some world accepts d" fails in R.
4. **Placement.** Z′ has PP7's three-cone form: A on silent lines of all three classes. Only the placement of the cones differs from PP7's (Prop. F below shows PP7's placement is immune). The audit note's sentence "their reverse records have no coherent completion" is placement-dependent.

---

## 4. Q2: openness of the deletion set and closed sections

**Lemma H (homothety; PROVED; CHECKED at t = 1/2000).** Let min_k p_k be attained at some k ≠ i, and p′ = (1−t)p + t e_i with t ∈ (0,1). Then:
- K_{p′} = (1−t)K_p + t e_i;
- C_{p′} is a pointwise weak world-i improvement of C_p, non-null for t > 0.

*Proof.*
- The formula for K_{p′} holds because min p′ = (1−t) min p.
- Each point of K_{p′} is (1−t)x + t e_i with x ∈ K_p, and e_i lies strictly on world i's correct side of a.e. line.
- So a model on the correct side stays there; a silent one becomes silent or correct; and a wrong one can only improve. ∎

**Theorem E (PROVED; the inequalities used are CHECKED in `p9_B1.py`, all four settings).** The objects:
- p₀ is the PP7 centre (min coordinate 3); S₂, S₃ are as in B1; S₁(s) = shrunk(T₁, s) is nested.
- μ₁(s_lo) < μ₂ + μ₃ < μ₁(s_hi) is certified, with s_hi − s_lo ≈ 2·10⁻⁹. So s* with μ₁(s*) = μ₂ + μ₃ exists by the intermediate value theorem.
- X := C_{p₀} with A on S₁(s*) ∪ S₂ ∪ S₃ is a fixed rival, and p(t) := (p₀ − t e₁)/(1 − t).

Then:
1. **d*(s*) := rec(C_{p₀}, X) is deleted at world 2 (and 3).**
   - b₁ = 0 exactly, so s = 0.
   - Uniformly in μ₁ ∈ [μ₁(s_lo), μ₁(s_hi)] (certified):
     - b₂, b₃ < 0;
     - Φ₂(d*) > 0;
     - both directions of rec(X, Z₂) are eligible at worlds 1 and 2;
     - c₂(rec(X,Z₂)) < 1/2 < c₁(rec(X,Z₂));
     - m(rec(X,Z₂), 2) > m(d*, 2).
   - A(rev d*) = ∅ already at s_lo, and adding constraints keeps it empty.
   - So B1's triangle applies at s*.
2. **For all small t > 0, rec(C_{p(t)}, X) is protected and in R⁰₂, hence in R₂ (Theorem A).**
   - b₁ = L₁(p₀) − L₁(p(t)) < 0 by Lemma H, since p₀ = (1−t)p(t) + t e₁.
   - b₂, b₃ and Φ₂ are within 6ρ and 15ρ of their values at t = 0, where ρ = μ(D(C_{p(t)}, C_{p₀})) → 0. So b₂, b₃ < 0 and Φ₂ > 0.
   - The reverse is unanchored by Proposition F, since X's side still carries A on the three cones.
   - CHECKED at t = 1/2000 for every s in the bracket: b₁ ≤ −2.8e−5, b₂, b₃ ≤ −1.2e−4, and Φ₂ ≥ 1.7e−4 (e₁, .1, the tightest setting).
3. **ρ(rec(C_{p(t)}, X), d*) = μ(D(C_{p(t)}, C_{p₀})) → 0.**

**Hence the deletion set Del₂ is not open, and {p : C_p R₂ X} contains p(t) for small t but not p₀. It is not closed, for a fixed rival X.**

*Reading.* This is not a feature of one example. The protected class {A(d) ≠ ∅, A(rev d) = ∅, b < 0} is cut out by strict inequalities in b. Wherever a fixed rival's records out of the selected family cross {b_l = 0} with a sticky defence at another world, the protected side survives and the boundary record is deletable.

**Proposition T (tie-break; PROVED under (H_T)).**

**(H_T).** Interior p ≠ q, with argmin of p and of q different from i, such that:
- b_i(rec(C_p, C_q)) = 0, b_j > 0 > b_k;
- A(rec(C_p,C_q)) and A(rec(C_q,C_p)) meet only the interior face.

Then in R⁰ at least one of {p′ : C_{p′} R⁰_i C_q} and {q′ : C_{q′} R⁰_i C_p} is not closed.

*Proof.*
1. Both directions are anchored (p and q).
2. At j the rule keeps d = rec(C_p, C_q) only, and at k it keeps rev d only. Each satisfies the other's obligation.
3. At i, P = Q, so Φ = 3ν(P) > 0 for both directions and each has c = 1/2. "Both" is penalised by objective 1 and "neither" by objective 2. So the tie-break keeps exactly one direction.
4. Say it keeps d. Put q′ = (1−t)q + t e_i. By Lemma H, L_i(q′) < L_i(q) = L_i(p), and by continuity the other signs and eligibilities persist. So the certified-unique choice for {C_{q′}, C_p} keeps rec(C_{q′}, C_p) at i, while rec(C_q, C_p) is not kept at i. Hence {q′ : C_{q′} R⁰_i C_p} is not closed at q.
5. If the tie-break keeps rev d instead, the symmetric argument with p′ = (1−t)p + t e_i applies. ∎

**NUMERICS (`p9_tie.py`).**
- (H_T)'s sign pattern holds at both tie points on a circle around p₀, at every world, in all four settings.
- The other two differences are ≈ ±5·10⁻³ (near e₁) and ≈ ±7·10⁻² (near u).

**Remarks.**
- The canonical orientation by "first nonzero box integral of the world-1 rank difference" does not matter here: any rule that keeps a single direction at exact ties fails.
- In R (rather than R⁰) the approaching records are additively safe s = 0 links. By Proposition C they can be deleted only through the six patterns. CONJECTURE: the non-closedness persists in R.
- **Minimal repair (CONJECTURE).** Do not count, in objective 1, the worlds at which c_i(d) = 1/2 exactly; that is, accept both directions at exact ties. The free doubly anchored layer is then {b_i ≥ 0}, which is closed. It also restores PP4's (E) at three-way ties (§6).

**Remark (a further source, CONJECTURE).** Along a family of records, A(rev d) can switch from ∅ to nonempty. The regime then changes from "accept at all eligible worlds" to "additive / lonely world", and sections can jump. Not tested.

---

## 5. Q3: PP7's three-cone family and its transferred return comparisons

**Family.** Y(t) = C_{p₀} with A on S_w(t_w) = shrunk(T_w, t_w), t ∈ (0,1]³ (PP7 Thm 4.2 / t8). Its records are:
- rec(C_{p₀}, Y(t)) and their reverses;
- the transferred rival-to-rival records rec(Y(t), Y(t′)). By (IB) these are records out of C_{p₀} on the annuli S_w(t′_w) Δ S_w(t_w), with growth set G (old side silent) and shrink set H (old side A);
- returns: records whose old side carries Y's A-pattern.

**Proposition F (PROVED; the key fact CHECKED by `p9_Q3_scan.py` (a), all four settings).** The nested family shrunk(T_w, s) shares one central ray c_w. No C_q is even weakly A at c₁, c₂, c₃: the exact outer anchor polygon is empty. Consequently:

**every record whose old side is A a.e. on sets R₁, R₂, R₃, with the closure of R_w containing the boundary rays of some S_w(t_w), is unanchored.**

*Proof.*
- a.e.-agreement gives weak agreement at the boundary rays, by closedness.
- g ↦ min_{x∈K_q} x·g is concave, so weak A at the three rays of S_w(t_w) gives weak A on the whole cone, in particular at c_w. ∎

This covers:
- rec(Y(t), C_{p₀}) for every t;
- the reverses of all-growing annulus records (the closure of S(t′)∖S(t) contains the rays of S(t′));
- all-shrinking records;
- every return comparison into C_q whose old side carries Y's pattern.

These carry no obligation and, not being guidance, are refused at every world. **The return quarantine needed by PP7 §6 is automatic** (PROVED). As a cross-check, (b) finds the reverses of full annuli for s ∈ {1/2, 4/5, 9/10, 19/20} unanchored by direct computation.

**Theorem G (PROVED).** Every face obligation of every record of the family is met in R⁰ by a protected defence, a guidance defence, or an additively safe (b ≥ 0) defence. Protected and guidance defences survive deletion. By record type:

| record | anchoring | how its obligations are met in R⁰ |
|---|---|---|
| rec(C_{p₀}, Y(t)); all-growing annuli (G = {1,2,3}) | p₀ ∈ A(d); interior face only (silence); A(rev d) = ∅ (Prop F) | if b < 0 at every world: **protected**, survives (Thm A). Otherwise some b_l ≥ 0, and the rule accepts d at every eligible world, including l: additively safe |
| G = {g} (H arbitrary) | interior face only | **guidance at g**, unremovable: S→A on g's own class and A→S on the classes in H both raise g's rank, so d is a pointwise world-g worsening |
| G = {g₁, g₂}, H = {h} | interior face only | rev d is guidance at h, so d is forbidden there. b_{g₁} + b_{g₂} = 2α_h > 0, so some g-world has b > 0, and the additive choice (or "all eligible" if rev is unanchored) gives d that world: additively safe |
| G = ∅, \|H\| ≤ 2 | vertices e_v with v ∉ H; edges; interior | d is guidance at every v ∉ H, which covers vertices, every face containing such v, and the interior. An open edge inside H, if met, has one world with b ≥ 0 (edge (E0)), chosen additively |
| \|H\| = 3, G = ∅; reverses of the all-growing records; returns | unanchored (Prop F) | no obligation |

So **survival on the family is equivalent to survival of its additively safe s = 0 defences.**
- **PROVED:** pattern (P,G) of Proposition C cannot delete them, for the all-growing and the G = {g₁, g₂} records. In both cases b_j + b_k < 0 at the other two worlds: −2μ_l and −2α_{g₁} respectively.
- **OPEN:** the patterns (P,0), (G,P), (0,P), (P,P) and the exact-tie pattern.
- **CHECKED (B1):** where a family record also has sticky defences, those are deleted.
- **CHECKED (D):** outside PP7's placement of the cones the clause fails outright.

So the honest answer to the brief's item 3 is as follows.
- On the protected range (PP7's sticky box U, and protected annuli) survival is PROVED.
- On the rest of the family, everything rests on the additively safe defences.
- The family "in the broad sense" (any cones in silent cells) does not survive.

---

## 6. Q4: the existing screens

**S9 (anchoring collapse).**
- *Literal form: does not bind.* S9's hypothesis is that verdicts on all Y carrying an anchor pattern, both into and out of C, are exactly ℓ's. Here Y ⪯ C is refused whenever Y's side is unanchored on D(Y, C), whatever L says, and C ⪯ Y is accepted whenever Φ⁴ ≥ 0. A small incoherent addition to Y breaks any would-be anchor.
- *Restricted form: binds.* On the doubly anchored layer at free worlds the rule is exactly additive in ν: the choice is the sign of b_i. P3's Prop 3.4 triangle (the ordered-rule half of S9's mechanism) then produces a (TC) violation against every non-ν verdict that the rule makes there or out of an unprotected singly anchored record. The deletion resolves each such violation in favour of the additive link.
- Theorems B and D are exactly these resolutions. Protected verdicts escape because the closing links would have to be protected or guidance links, which Lemma R forbids (Theorem A).

**PP4 (P), (T), (E).**
- These are consequences of (TC) (PP4 Thm 2), and R satisfies (TC) by construction, so they hold in R.
- In R⁰, on two-point swaps between doubly anchored locations at a free world, both directions are eligible when the mass ratio lies in [1/4, 4]. Outside that range only the heavier-adding direction is, and it is also the additive one. So the swap rule is ρ ≡ 1:
  - (P) holds with equality;
  - (T) holds with every cycle sum 0;
  - **(E) fails at exact three-way ties.** (E) needs both directions at a zero-sum triangle, and objective 1 forbids that. The violations have equal priority 3/2, so all three tie links are marked and deleted.
- This is harmless for obligations at generic points. It is a second instance of the tie problem of Proposition T, and the repair proposed there also restores (E).

**FF2 Cor 4.3 (PROVED in outline; conditional).** The requirement is: some world admits no strictly rank-increasing integrable penalty endorsing all its accepted bounded-support comparisons out of selected models. At a world l with a surviving protected defence C_{p₀} ≺_l Y (Theorem A; such defences exist at every interior p₀ by PP7 Thm 4.2):
1. Any endorsing penalty is a positive field w₁, w₂ on level-1 and level-2 steps.
2. The cross-class swaps "S→A on x ∈ M_l, S→A on y ∈ M_j" are splices of two selected models C_q, C_{q′} (q′ beyond both lines), so they are doubly anchored in both orientations.
3. Their joint choice is free at l: forbidden at k, guidance in reverse at k, and additive at j. So R⁰ accepts each orientation exactly when it is ν-additive.
4. If these survive in R, a Lebesgue-point argument (as in PP4 Example E) forces w₂(x) = w₁(y) at a.e. pair. The field is then ν on these steps.
5. ν does not endorse the protected defence, since b_l < 0. So no field exists at l, and Cor 4.3 is met.

The condition is the survival of that additive swap layer, the same open point as in §5.

**PP2 Thm 6 (S11). Does (s, m) amount to a fixed priority on problems? No.**
- (s, m) never restricts which comparisons are made. Admissibility comes from guidance, anchoring and Φ⁴. (s, m) only selects, inside a violating triple, which pair to delete.
- m depends only on ν(P_i), ν(Q_i), so it is invariant under every measure-preserving rearrangement of the changed steps. s depends on anchoring and signs of b. Neither orders problems or steps.
- PP2's hypothesis (H2) needs every accepted non-guidance comparison at world 1 to pass a weak gate for one fixed key. R accepts, at a single world, the swap x→y when m_x > m_y and the swap y→x when m_y > m_x, for disjoint doubly crossed locations. These are the free additive swaps, which survive deletion except at ties. No fixed key passes both, so (H2) fails for every key and Theorem 6 does not apply.
- PP2's residual screen (edge threshold models) concerns priorities used *through a gate*, of which the rule has none.
- The real danger lies elsewhere: Theorems D and E.

---

## 7. Nearby reachable results

1. **Extended protection removes Theorem D's mechanism (PROVED).**
   - Rule: give s = 1 to every direction d accepted at i with A(d) ≠ ∅, b < 0 at all three worlds, and rev d ∉ R⁰_i. A(rev d) is no longer required to be empty.
   - Theorem A's proof uses only that a P link is strict at i, has an anchored source, and has a target strictly better at all worlds. So it holds verbatim, and no extended-protected defence is ever marked.
   - In Theorem D, d is then protected at λ (rev d is accepted only at the other two worlds). In the triangle (C, Z′, W) the s = 0 pair {Z′, W} is marked instead.
   - What it leaves open: B1's world-1 question and Theorem E. The record d*(s*) there has b₁ = 0, so it is not strictly dominated.
2. **Closing the protected class is not free (PROVED).**
   - Suppose s = 1 were given on {b ≤ 0 everywhere, b ≠ 0}.
   - In the PPG case of Theorem A, Lemma R's equality case then allows c − a to sit on M_u ∪ M_v only, with equal masses and b_u = b_v = 0 on both P links: for example c = a with A on equal-mass cones of M_u and M_v.
   - So a violating triple made only of weakly protected and guidance pairs becomes possible, and the weaker defence is marked.
   - Whether such a triple ever marks the last defender of an obligation is OPEN. This is where (S)'s closedness and the defence clause meet in this design.
3. **Ties (CONJECTURE).** Accept both directions at exact additive ties (§4). This repairs Proposition T on the selected layer and PP4's (E).

**Single most important open point.** Do additively safe s = 0 defences survive the deletion? This is the five patterns of Proposition C besides (P,G), and the exact-tie pattern. Three things hinge on it:
- survival on PP7's family (§5);
- whether Theorem E's non-closedness is the only closedness failure of the extended rule;
- the survival of the swap layer that FF2 Cor 4.3 needs (§6).

---

## 8. Files (`PP9_py/`)

| script → output | content | label |
|---|---|---|
| `common.py` | record data with certified signs, guidance, exact anchor witnesses / empty outer polygons, faces, the 64-state joint choice (unique optimum certified), (s, m) priorities, (TC) test on a triple | library |
| `p9_lemma.py` → `.out` | Lemma R (27 cases); "every change alters every rank"; abstract cross-check of Theorem A with control | CHECKED |
| `p9_B1.py` → `p9_B1_all.out` | Instance B1 (drop triangles at worlds 2 and 3), and Theorem E's data: IVT bracket, uniform inequalities, exact homothety check and protection at t = 1/2000 | CHECKED |
| `p9_D_search.py` → `.out` | dominating-splice cells in all three classes, and both-silent cells | NUMERICS (used only to choose D) |
| `p9_D.py` → `p9_D_all.out` | Theorem D: anchored record with every defender deleted, all four settings | CHECKED |
| `p9_Q3_scan.py` → `.out` | Prop F (central rays: empty polygon); unanchored annulus reverses | CHECKED |
| `p9_tie.py` → `.out` | hypothesis (H_T) of Proposition T | NUMERICS |
