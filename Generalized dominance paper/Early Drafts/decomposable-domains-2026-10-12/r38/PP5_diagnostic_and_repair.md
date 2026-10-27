# PP5. The greedy diagnostic near e_1, the local repair, and what a rule needs

20 October 2026, Brief 38, Task A. Labels:
- **PROVED**: the full argument is given here (one reader, me; not refereed).
- **CHECKED**: exact cone geometry (integer rays) with interval-certified masses, or an exact finite check. The script is named.
- **NUMERICS**: exact cone geometry with double-precision solid angles. Every violation quoted from a scan was re-certified as CHECKED.
- **CONJECTURE / OPEN**: as stated.

The family, pool and rule are audit's (`AUDIT_anchor_plan.md`). Throughout, ε = 3/10, and C_p = D_{K_p} with K_p = p + 3ε min(p)(Δ − u). I add no assumption. Scripts are in `PP5_py/`; run them as `python3 -I <script>`, and each writes a `.out` file.

---

## 0. Verdicts

1. **The diagnostic is CONFIRMED (CHECKED).** The two masses audit estimated are now interval-certified. The interval widths are below 10⁻³⁵, and two independent mass formulas agree.
   - Φ(C_a,C_b) = (0.0185831, −0.0153229, 0.0495234), and a·Φ = (0.0167248, −0.0007661, 0.0024762).
   - Φ(C_b,C_c) = (0.0111180, 0.0481162, −0.0167300), and b·Φ = (0.0100174, 0.0038493, −0.0003179).
   - Audit's Monte Carlo values lie within about one standard error of these.
   - **The anchor sets are exactly the source points:** A(rec(C_a,C_b)) = {a} and A(rec(C_b,C_c)) = {b}. So audit's choice of the source as witness was not a lower bound; it is the whole rule. The greedy rule therefore accepts both records at world 1 only.
   - C_c is a pointwise strict world-1 improvement of C_a. This is PROVED analytically and CHECKED on every cell.
   - So (TC) fails at world 1.
2. **The mechanism.**
   - rec(C_a,C_b) is additively safe at world 1: its rank-step balance is add₁ = ν(P₁) − ν(Q₁) = +0.00184.
   - rec(C_b,C_c) is *sticky-only* at world 1: add₁ = −0.00311 < 0 ≤ Φ₁.
   - The greedy rule makes 3,888 sticky-only world-1 acceptances among the local scan's selected models. Every one of them is the reverse of an additively safe acceptance, so world 1 accepts both directions of the pair: hysteresis in PP4's sense (P).
   - Every scanned violation uses one of these links.
3. **The diagnostic is not isolated (NUMERICS; two further triples CHECKED).** The greedy rule violates (TC) at world 1 on:
   - 1,599 (x,z) pairs on a 0.01 grid near e_1;
   - 7,996 pairs on a 0.003 grid around a, b, c.

   It never violates (TC) at worlds 2 or 3.
4. **The proposed repair: eligible, face-free and closed (PROVED/CHECKED), but it creates new forbidden triples (CHECKED).**
   - **Face obligations.** No selected model is nested in another (Lemma 3.1). Hence every record between distinct selected models with an interior source has its anchor set in the open simplex, and its only face obligation is W(d) ≠ ∅.
   - **Neighbourhoods.** The reassignment holds on explicit ρ-balls of radius 0.00550 (for d_ab) and 0.00535 (for d_bc), with R_i closed.
   - **New triples.** Removing world 1 from rec(C_a,C_b) makes the greedy reverse acceptance C_b ⪯₁ C_a strict, and a ⪯₁ (.898,.047,.055) ⪯₁ b then closes a new forbidden triple. The same happens at (b, (.907,.044,.049), c).
   - This happens at every radius, because it involves the centre records themselves. The count grows with the radius: 2, 7 and 25 new violating pairs.
5. **What the repair needs, as a rule (§4).**
   - **(a)** A record and its reverse must be decided together, and world 1 needs a potential on selected records.
   - **(b)** The *additive-first* allocation AF supplies one: accept at every additively safe world, and use the sticky pool only when every world is additively improved.
     - AF is closed, record-based and strictly guiding, and meets all seven face obligations (PROVED, from audit's counting bound).
     - It reproduces audit's move of rec(C_b,C_c) to world 2, but keeps rec(C_a,C_b) at worlds 1 and 3.
     - Near e_1 no selected model is additively dominated by another (NUMERICS, with relative margin ≥ 0.19). So among selected models AF is the expected-rank order at each world, and has **no forbidden triple** (PROVED given that fact; 0 of 12.7 million scanned triples).
6. **Does it extend near e_1?**
   - **For selected models: plausibly yes.** The expected-rank surface has strictly positive normals at all 780 grid points near e_1 (NUMERICS).
   - **For rivals: no, not as stated (CHECKED).**
     - At every interior index and every world there are *forced* sticky records. These are mixed records whose only eligible world is i (PROVED).
     - (TC) then obliges world i to refuse every *return* record into the source's world-i improvement cone (Proposition 4.4, PROVED).
     - An exact instance at a shows such a return record anchored at another selected model (q = (.901,.051,.048)). Both AF and the greedy rule accept it at world 1, which gives a (TC) violation.
     - The return is eligible, and additively safe, at worlds 2 and 3. So this is a design constraint with slack, not an impossibility.
     - The rule still lacks a world-i *return quarantine* that is closed and record-based. That is OPEN.

---

## 1. Conventions and method

- **Problems and models.** A problem is {g, −g}, with g standard Gaussian in ℝ³; μ is its law, of total mass 1. Since K_p lies in Δ, C_p accepts g iff V_j(p)·g > 0 for the three vertices V_j(p) of K_p. So the acceptance set A_p is the open simplicial cone with facet normals V_j(p).
- **Ranks.** At world i, orient the problem by h_i > 0. The rank is 0 if h is accepted, 1 if C_p is silent, and 2 if −h is accepted.
- **Records and verdicts.** U_i(X) is the set of rank steps, and ν = μ ⊗ counting on levels. For d = rec(X,Y), P_i = U_i(Y)∖U_i(X) and Q_i = U_i(X)∖U_i(Y). Then
  - Φ_i = 2ν(P_i) − ν(Q_i) (audit's pool), and
  - add_i = ν(P_i) − ν(Q_i) = L_i(Y) − L_i(X), with L_i(X) = ∫ r_i(X) dμ the expected world-i rank.

  This reproduces audit's numbers (§2.1), so it is the normalisation audit used.
- **Exact masses, two independent ways.**
  - (i) Enumerate all cells of the central arrangement of the facet planes, the diagonal planes and the coordinate planes, by exact clipping of the eight octants. The cells partition ℝ³ up to null sets, and on each cell both models' advice is constant. Masses are solid angles via Van Oosterom–Strackee, using `mpmath.iv` at 40 digits (`records.py`).
  - (ii) Signed sums of masses of convex cones H_i ∩ (±A_x) ∩ (±A_y) (`cones.py`).
  - In both, the total mass is the interval [1, 1] ± 10⁻³⁹.
- **Exact anchor sets (`anchors.py`).**
  - *Fact used.* On a cell of the arrangement, argmin g and argmax g are fixed. So P_q(g) = q·g + ε q_k(3 min g − Σg) is linear in g on the closed cell, and linear in q on the chamber {q_k = min q}.
  - *Reduction.* Matching X's advice a.e. on a changed cell is therefore the same as finitely many weak linear inequalities in q, one per extreme ray. Acceptance > 0 a.e. ⟺ ≥ 0 at the rays, because a nonzero linear form vanishes only on a null set. Silence gives two inequalities ≤ 0 at the rays.
  - *Result.* A(d) is an exact union of three rational polygons. Faces are read off its vertices. This is audit's §2 structure made computable.

---

## 2. Task A.1: the diagnostic, certified

### 2.1 The three records (CHECKED, `t1_certify.py`)

Values are rounded to 10 significant digits. Every interval is narrower than 10⁻³⁵, and methods (i) and (ii) agree.

| record | world | ν(P_i) | ν(Q_i) | Φ_i | add_i |
|---|---|---|---|---|---|
| rec(C_a,C_b) | 1 | 0.01674578346 | 0.01490847103 | **+0.01858309588** | +0.001837312422 |
| | 2 | 0.005443790997 | 0.02621046349 | −0.0153228815 | −0.0207666725 |
| | 3 | 0.02705920531 | 0.004595049183 | +0.04952336143 | +0.02246415612 |
| rec(C_b,C_c) | 1 | 0.01422601914 | 0.01733400148 | **+0.01111803681** | **−0.003107982334** |
| | 2 | 0.02655874166 | 0.005001278966 | +0.04811620435 | +0.02155746269 |
| | 3 | 0.004943327345 | 0.02661669328 | −0.01673003859 | −0.02167336593 |
| rec(C_a,C_c) | 1 | **0 (exact)** | 0.001270669912 | −0.001270669912 | −0.001270669912 |
| | 2, 3 | 0.001030730052 | 0.00023993986 | +0.001821520244 | +0.000790790192 |

**Transitions** (μ-masses, in the class / regular-advice notation of PP2 §0; unanimous problems never change):
- **rec(C_a,C_b).**
  - M1: S→A 4.1827e-3, S→B 4.5150e-3, A→S 8.8151e-4, B→S 4.1234e-4, A→B 2.3663e-5.
  - M2: S→B 7.4844e-3, A→S 4.5774e-3, A→B 4.4500e-5.
  - M3: S→A 8.0768e-3, B→S 8.9167e-4, B→A 2.4811e-4.
  - Changed problems on which C_a is silent: 0.024259.
- **rec(C_b,C_c).**
  - M1: A→S 4.3665e-3, B→S 4.1545e-3, S→A 8.1841e-4, S→B 5.7687e-4, B→A 1.4169e-5.
  - M2: B→S 7.5010e-3, S→A 4.7754e-3, B→A 5.7149e-5.
  - M3: A→S 7.8954e-3, S→B 8.9167e-4, A→B 2.1881e-4.
  - Silent-old mass: 0.0070623.
- **rec(C_a,C_c).**
  - M1: A→S 2.5635e-4, S→B 5.3444e-4.
  - M2 and M3: B→S 2.9294e-5 and S→A 2.1065e-4 each.
  - Every change improves world 1.

**Comparison with audit.** Audit's estimates (0.018948, −0.015474, 0.049590) and (0.010856, 0.048464, −0.016576) differ from the certified values by at most 0.00037. A world-1 Φ estimate from 500,000 draws has standard error about 0.0004.

### 2.2 Anchor sets and the greedy verdicts (CHECKED)

Exact anchor sets:
- A(rec(C_a,C_b)) = {a}, and A(rec(C_b,C_a)) = {b}.
- A(rec(C_b,C_c)) = {b}, and A(rec(C_c,C_b)) = {c}.
- A(rec(C_a,C_c)) is the segment from (839/1000, 161/2000, 161/2000) to a, along the line through e_1 and u.
- A(rec(C_c,C_a)) is the segment from c to (108/115, 7/230, 7/230).

All of these meet only the full face. Hence the greedy rule's set W_G(d) is computed exactly at the source.

| record | source·Φ | margins x₁Φ₁ − x_jΦ_j | W_G |
|---|---|---|---|
| rec(C_a,C_b) | (0.016724786, −0.00076614408, 0.0024761681) | 0.017491, 0.014249 | **{1}** |
| rec(C_b,C_c) | (0.010017351, 0.0038492963, −0.00031787073) | 0.0061681, 0.010335 | **{1}** |

### 2.3 C_c is pointwise strictly better than C_a at world 1

**PROVED (audit's argument, checked).**
- Along p = (t, (1−t)/2, (1−t)/2) with t > 1/3 we have min p = (1−t)/2. So P_p(g)/(1−t) = [t/(1−t)]g₁ + (g₂+g₃)/2 + (ε/2)(3 min g − Σg).
- With the world-1 orientation h₁ > 0, increasing t increases P_p(h) and decreases P_p(−h). So good advice expands and bad advice shrinks.
- Both a (t = .9) and c (t = .902) lie on this line.

**CHECKED.** On all 68 cells of the joint arrangement, C_c's world-1 rank never exceeds C_a's. Strict improvement holds on mass 0.001270669912, so ν(P₁(rec(C_a,C_c))) = 0 exactly.

### 2.4 The violation (CHECKED, `t4_certify_grid.py`)
- C_a ⪯₁ C_b and C_b ⪯₁ C_c hold under the greedy rule.
- C_c ⪯₁ C_a is guidance.
- C_a ⪯₁ C_c is refused: Φ₁ < 0, and the record is not guidance because ν(Q₁) > 0.
- So C_a ⪯₁ C_b ⪯₁ C_c ≺₁ C_a, and (TC) fails at world 1.

Two triples from the 0.01 grid are also certified violations:
- (.95,.01,.04) ⪯₁ (.96,.03,.01) ⪯₁ (.96,.01,.03) ≺₁ (.95,.01,.04);
- (.94,.01,.05) ⪯₁ (.95,.04,.01) ⪯₁ (.96,.01,.03) ≺₁ (.94,.01,.05).

So a 0.01 grid does detect the failure once masses are exact. Audit's earlier miss was not a matter of spacing alone.

---

## 3. Task A.2: the proposed repair

The repair sets W(rec(C_a,C_b)) := {3} and W(rec(C_b,C_c)) := {2}.

### 3.1 Eligibility and faces

**Eligibility (CHECKED).** Φ₃(rec(C_a,C_b)) = 0.0495 > 0 and Φ₂(rec(C_b,C_c)) = 0.0481 > 0.

**Lemma 3.1 (no nesting; PROVED).** K_q ⊆ K_p implies q = p.

*Proof.*
1. An upright triangle in the plane of Δ is fixed by its three lower bounds, and K_p = {w : w_i ≥ p_i − εm_p}. So containment means q_i − εm_q ≥ p_i − εm_p for every i.
2. Summing over i gives m_q ≤ m_p.
3. At k = argmin q, (1−ε)m_q = q_k − εm_q ≥ p_k − εm_p ≥ (1−ε)m_p. So m_q = m_p, and every lower bound coincides. ∎

**Corollary 3.2 (PROVED).** Let x ≠ y with x interior. Then A(rec(C_x,C_y)) ∩ ∂Δ = ∅. So the only face obligation of a record between selected models with an interior source is W ≠ ∅.

*Proof.*
- K_x ⊄ K_y by Lemma 3.1. So an open set of lines meets K_x and misses K_y.
- On those lines C_x is silent and C_y is not, so the changed set carries non-null silent-old advice.
- A boundary C_q is silent only on a null set, so no boundary q matches X there. ∎

This is consistent with the scans: none of 62,222 anchor sets touches ∂Δ, and 32,032 of them are the source point.

### 3.2 The reassignment on whole neighbourhoods (PROVED)

**The metric.** Let ρ(d,d′) = μ{(old,new) labels differ}, with the label "none" off the changed set. If X_n → X and Y_n → Y in measure, then rec(X_n,Y_n) → rec(X,Y) in ρ. So ρ-balls are neighbourhoods in audit's topology.

**Two bounds.**
- The integrand of Φ_i lies in [−3, 6], so |Φ_i(d) − Φ_i(d′)| ≤ 9ρ(d,d′).
- Let s(d) be the silent-old mass of d's changed set. If ρ(d′,d) < s(d), then d′ still has non-null silent-old changes, so A(d′) ∩ ∂Δ = ∅, as in Corollary 3.2.

**Radii.** Put η(d) = min(s(d), Φ_w(d)/9).
- For d_ab: η = min(0.024259, 0.0055026) = **0.0055026**, with w = 3.
- For d_bc: η = min(0.0070623, 0.0053462) = **0.0053462**, with w = 2.

**The repaired sets.** For any η′ < η, set:
- R_w′ = R_w ∪ B̄(d, η′);
- R₁′ = (R₁ ∖ B(d, η′)) ∪ Guid₁.

Both are closed. On B̄(d, η′), world w is eligible and is the only obligation.

Guidance at world 1 is untouched. Records within ρ < 0.00497 of d_ab, or < 0.00578 of d_bc, are not world-1 guidance, since ν(Q₁) > 0 there.

So **closedness, eligibility and the defence clause all survive the reassignment on a neighbourhood.** The local repair costs nothing in (S).

### 3.3 New forbidden triples (CHECKED, `t6_certify_repair.py`; scan NUMERICS, `t5_repair_scan.py`)

Removing a world from a record can make its reverse strict.
- **First triple.** The greedy rule accepts C_b ⪯₁ C_a: Φ₁ > 0 with add₁ < 0, so this acceptance is sticky-only.
  - Under the repair, C_a ⪯₁ C_b is refused, so C_b ≺₁ C_a.
  - With y₁ = (449/500, 47/1000, 11/200), the greedy rule has C_a ⪯₁ y₁ ⪯₁ C_b. This is a **certified violation**.
- **Second triple.** Symmetrically, C_c ⪯₁ C_b is accepted, and the repair refuses C_b ⪯₁ C_c.
  - With y₂ = (907/1000, 11/250, 49/1000), C_b ⪯₁ y₂ ⪯₁ C_c ≺₁ C_b. This is a **certified violation**.

Both triples use the centre records themselves, so they appear for every radius. Scan of the 227 local selected models:

| repair radius η′ | records in the two balls | violating (x,z) pairs at world 1 (greedy: 7,996) | new pairs at world 1 | new pairs at worlds 2, 3 |
|---|---|---|---|---|
| 0.0010 | 2 + 2 | 7,998 | 2 | 0, 0 |
| 0.0025 | 7 + 6 | 8,003 | 7 | 0, 0 |
| 0.0050 | 60 + 63 | 8,008 | 25 | 0, 0 |

The repair removes the diagnostic triple and adds new triples at world 1. No new triple appears at worlds 2 or 3.

---

## 4. Task A.3: what the repair needs, as a rule

### 4.1 What the failures show
- **(N1) A record and its reverse cannot be repaired separately.** The greedy rule accepts 3,888 selected pairs in both directions at world 1, one direction sticky-only in each case. Removing either direction makes the other strict, and chains through nearby selected models then close (§3.3).
- **(N2) Every greedy violation contains a sticky-only world-1 link (NUMERICS).** Among violating pairs, none is realisable with two chain links that are additively safe or guidance.

This suggests letting each world's selected-model comparisons follow its expected rank:

**Lemma 4.1 (PROVED).** Suppose that, on a set 𝓜 of models, world i's accepted relation is exactly {X ⪯ Y ⟺ L_i(X) ≤ L_i(Y)}. Then (TC) holds on 𝓜. This relation contains all guidance on 𝓜.

*Proof.* The relation is a total preorder. Guidance gives L_i(X) ≤ L_i(Y). ∎

### 4.2 The additive-first allocation

**Definition (AF).**

R_i = Guid_i ∪ {d : add_i(d) ≥ 0} ∪ {d : Φ_i(d) ≥ 0 and add_j(d) ≤ 0 for all j}.

Optionally, intersect the last two sets with H_{123} = {A(d) ≠ ∅}, so that only records with obligations are accepted.

**Proposition 4.2 (PROVED, using audit's §4 counting bound).**
- R_i is closed: add and Φ are 6ρ- and 9ρ-Lipschitz, and H_{123} is closed.
- AF is record-based.
- R_i ⊆ E_i ∪ Guid_i, because Φ_i = add_i + ν(P_i).
- AF satisfies strict (G): a pure strict improvement has Φ_i, add_i < 0.
- AF meets all seven face obligations:
  - |I| = 1: guidance.
  - |I| = 2: the bound gives Σ_I add ≥ 0, so some i ∈ I is additively safe.
  - |I| = 3: either some add_j ≥ 0, or every add_j ≤ 0 and Σ Φ ≥ 0 makes the sticky branch nonempty.

**AF on the diagnostic (CHECKED).**
- W(rec(C_a,C_b)) = {1,3}, since both additive balances are positive.
- W(rec(C_b,C_c)) = {2}.

So AF performs audit's second reassignment and not the first, and either suffices for this triple.

### 4.3 Near e_1, among selected models (NUMERICS; consequence PROVED)

**No additive domination.** add(rec(C_x,C_y)) ≤ 0 componentwise means L(C_y) ≤ L(C_x): one selected model is additively Pareto-dominated by another.
- On 105 + 227 scanned models (62,222 ordered pairs) there is no such pair.
- min max_j add_j ≥ 5.2e-4, and the relative margin max_j add_j / max_j |add_j| ≥ 0.195. Errors are about 10⁻¹⁵.

**Positive normals.** The surface p ↦ L(C_p) has normals with all components of one sign at all 780 points of a 0.005 grid with p₂ + p₃ ≤ 0.2. The smallest component is 0.029 (`t2_Lsurface.py`). So locally there is no domination either.

**Consequence.** On selected models near e_1, AF is exactly the expected-rank order of Lemma 4.1. It therefore has no forbidden triple, matching the scan: 0 violations at every world on 1,124,760 + 11,542,950 ordered triples (`t3_*.out`).

### 4.4 Beyond selected models: forced sticky records and their returns

**Proposition 4.3 (forced sticky records; PROVED).**
- *The rival.* For interior p, C_p is silent on non-null parts of M1, M2 and M3, namely on lines of each class through K_p. Let Y be C_p with advice A on parts S₁, S₂, S₃ of these, of masses m₁, m₂, m₃.
- *The verdicts.* Then:
  - add_1 = m₁ − m₂ − m₃, and cyclically for the other worlds;
  - Φ₁ = 2m₁ − m₂ − m₃, and cyclically.
- *Forcing.* For m₂ = m₃ = s·m₁ with s ∈ (1/2, 1):
  - every add_j < 0;
  - Φ₁ ≥ 0 > Φ₂, Φ₃.

  The record is mixed at every world and p ∈ A(d). So every allocation from the pool must accept it at world 1, and only there.
- The same holds at every world, by permuting the classes.

**Proposition 4.4 (pump window; PROVED).**
- *Statement.* Suppose world i accepts d₁ = rec(X,Y). Let Z be a guidance improvement of X at world i, so U_i(Z) ⊆ U_i(X) and Z ≠ X. Then d₂ = rec(Y,Z) satisfies ν(P_i(d₂)) ≤ ν(Q_i(d₁)) and ν(Q_i(d₂)) ≥ ν(P_i(d₁)). Hence Φ_i(rev d₂) ≥ Φ_i(d₁) ≥ 0, and (TC) requires d₂ ∉ R_i.
- *Proof.* U_i(Z) ⊆ U_i(X) gives U_i(Z)∖U_i(Y) ⊆ U_i(X)∖U_i(Y) and U_i(Y)∖U_i(Z) ⊇ U_i(Y)∖U_i(X). If d₂ ∈ R_i, then X ⪯_i Y ⪯_i Z ≺_i X. ∎

**Exact instance (CHECKED, `t7_rival_pump.py`).**
- *Setup.* Take p = a and q = (901/1000, 51/1000, 48/1000). Every upper bound of K_q is below K_a's (0.9298 < 0.93, 0.0798 < 0.08, 0.0768 < 0.08). So lines cutting each corner of K_a miss K_q on the majority side.
  - S₁, S₂ and S₃ are exact rational sub-cones of such lines: C_a is silent there and C_q says A.
  - Their masses are m₁ = 8.5277e-6 and m₂ = m₃ = 6.3958e-6 (s = 3/4).
  - Z is C_a with advice B on a set T ⊂ M1 of mass 3.198e-7, where both C_a and C_q are silent.
- *Results.*
  - **(i) The forced first link.** rec(C_a,Y) has Φ = (4.264e-6, −2.132e-6, −2.132e-6) and every add_j < 0. It is forced at world 1.
  - **(ii) The anchored return.** rec(Y,Z) has q ∈ A(rec(Y,Z)): C_q equals Y on S₁ ∪ S₂ ∪ S₃ ∪ T, checked cell by cell. It has add = (3.944e-6, 8.848e-6, 8.848e-6) and Φ = (1.674e-5, 2.409e-5, 2.409e-5). Both rules accept it at world 1:
    - AF accepts it because add₁ > 0;
    - the greedy rule accepts it because q₁Φ₁ = 1.508e-5 is the largest score at the witness q.
  - **(iii) The strict link.** Z is a strict pointwise world-1 improvement of C_a.
- *Conclusion.* **Both AF and the greedy rule violate (TC):** C_a ⪯₁ Y ⪯₁ Z ≺₁ C_a.
- *Relation to S9.* This is the anchoring mechanism of S9 (SCREEN_P3 Thm 3.2). AF's verdicts are ν's on records whose additive balance is robustly positive somewhere. I have not written out the formal anchor; the instance does not need it.

**What the instance leaves open.** The return record is eligible, and additively safe, at worlds 2 and 3. So assigning it to {2,3} removes this violation. The constraint is therefore a quarantine with slack, not an impossibility.

### 4.5 Answer to item 3

**What the local repair needs, as a rule:**
- **(R1) Pairs at the dominant world.** World 1 must decide a selected record and its reverse together. Near e_1 it must order selected models by a potential. AF's expected rank L₁ does this, and among selected models it is the whole rule.
- **(R2) The sticky pool.** Sticky-only acceptances are allowed only on records that improve every world additively (the AF branch). Proposition 4.3 forces such records at every interior index and every world.
- **(R3) Return quarantine.** Each world must refuse the returns of its forced sticky records (Proposition 4.4). The refused class is fixed by the first link, but under (IB) it must be recognised from the return record alone. Some returns are anchored at other selected models, so the refusal must override additive safety at that world. The returns must then be covered elsewhere.

**Extension near e_1:**
- **(R1) and (R2): plausible.** The positive-normal and no-domination facts hold throughout the scanned region near e_1 (NUMERICS). For selected models the problem is solved there.
- **(R3): OPEN.**
  - *The suggested quarantine.* Proposition 4.4 suggests: outside the sticky branch, accept at world i only if ν(P_i) ≥ 2ν(Q_i), i.e. only if the reverse is not eligible. This is PP4's ratio-2 spread, which is triangle-safe.
  - *What it blocks.* Every pump whose first link is sticky with Φ_i > 0 and whose return lies outside the sticky branch, since then Φ_i(rev d₂) > 0. This includes the t7 instance.
  - *What it does not block.* Pumps with two sticky links, or with a sticky second link.
  - *Its cost.* It weakens the edge covers, where the counting bound gives only Σ_I add ≥ 0.
  - Neither point is checked here.
- **Next step.** Screen (R3) against S9, and against PP4's no-hysteresis condition (P), which the greedy rule violates at world 1 on 3,888 selected pairs.

---

## 5. Scripts (`PP5_py/`)

| script | content | label |
|---|---|---|
| `geom.py`, `records.py`, `cones.py`, `anchors.py` | exact family, cell arrangements, interval solid angles, two mass methods, exact anchor polygons | — |
| `t1_certify.py` | §2: records, Φ, add, transitions, anchors, greedy scores, C_c vs C_a | CHECKED |
| `exact_rules.py`, `t4_certify_grid.py` | certified greedy and AF verdicts; three certified violations | CHECKED |
| `fast.py`, `scan.py`, `tc_analyse.py`, `t3_grid.py` | scans (105-model 0.01 grid; 227-model 0.003 grid with a, b, c) and (TC) counts | NUMERICS |
| `t5_repair_scan.py`, `t6_certify_repair.py` | repair balls, new triples (scan), certification of two of them | NUMERICS / CHECKED |
| `t2_Lsurface.py`, `t8_stats.py` | expected-rank normals; AF margins; structure of greedy violations | NUMERICS |
| `t7_rival_pump.py` | forced sticky record and anchored return at a | CHECKED |
