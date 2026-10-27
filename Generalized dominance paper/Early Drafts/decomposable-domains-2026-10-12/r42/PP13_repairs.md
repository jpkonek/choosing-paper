# PP13. The rescaled family: a certificate inside the family, the repair lemma, and (TC) for repair records

21 October 2026. Round 42, Task B (audit's brief `AUDIT_round42_brief.md`, steps 1–3).

**Labels.**
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact rational computation (Python `fractions`). Floats and LPs are used only to *find* witnesses, and every reported witness is re-verified exactly.
- **NUMERICS**: evidence only.
- **OPEN**, **CONJECTURE**: as stated.

**Scripts** are in `PP13_py/`. Run each as `python3 -u -I -B <script>` inside that folder. Outputs are in `*.out`.

**No assumption is added.** I use the brief's axioms: reflexivity; (G), both halves; (IB); (TC); (S); (LA); direct (C). Selected models are the rescaled family only.

---

## 0. Verdicts

**Step 1: the certificate exists inside the family (PROVED for every ε; CHECKED at ε = 3/10 and 1/10).**
- There are four indices p₀ = u, p₁, p₂, p₃ and four disjoint open cones B₀..B₃ of world-1-minority problems (one sign pattern) such that:
  - C_{p_j} is silent on B_j;
  - C_{p_j} accepts g, which is world-1-correct, on every B_k with k ≠ j.
- Audit's four indispensable world-1 defences rebuild verbatim with sources C_{p_k}. The finite additive contradiction is unchanged.

**Step 2: the repair lemma.**
- **(a) always holds (Theorem R1, PROVED).** For every rival X outside the family, the set G(X) of indices p at which X strictly improves C_p pointwise at no world is open and nonempty. The proof is the open KKM lemma. So strict (G) never obstructs a KKM dominator in this family.
- **Exposure is PROVED for every locally coherent rival (Theorem E).** This covers:
  - every coherent rival D_K with K ⊂ int Δ;
  - every rival that agrees with a selected C_a off a closed set of problems containing no line through a vertex of M_a. This includes the rivals near T1, the rescaled PP8-type rivals, edge rivals, vertex rivals and certificate-type rivals.
- **CHECKED:** exact (a)+(b) certificates for 15 named rivals, including two rivals outside Theorem E's class.
- **OPEN:** arbitrary measurable rivals that are coherent near none of their own boundary lines (for example, fine mixtures of selected models). No counterexample was found.
- **Two structural corrections (PROVED).**
  - The rescaled family has **no three-class pump**. PP8's doubly anchored rival (A on one cone per class, realised by another member) does not exist here. Its two-class analogue is a strict pointwise improvement of its base at one world.
  - **Theorem J's configuration never occurs** in the rescaled family, for any interior index, any ε and any edge. So J1 says nothing about this family, and the brief's observation 4 ("any successful construction must jump at forced cuts") is not established for it.

**Step 3: (TC) fails for repair records (CHECKED, exact).**
- With repairs accepted at all three worlds (as KKM dominators need), there are forbidden triangles made of two repairs and one strict-guidance link:
  - **at world 1**, and at **worlds 2 and 3**, using the same two selected models on three cones of one pencil (`s3_tc_violation.py`);
  - again with both repairs taken from **vertex** indices (`s3_vertex_chain.py`);
  - with **T1's own certificate defence** (and C_{p₃}'s) followed by one repair (`s3_cert_violation.py`).
- So the class of all admissible repairs fails (TC), and so does the nearest-index repair rule.
- **Mechanism: the precision window.** Along any pencil of problems, every selected model's silent band has log-width in a fixed interval. An exposed (incoherent) new side can therefore contain a sub-pattern that another selected model realises, and the second repair transports that sub-pattern again. The composite of two "coherent → incoherent" records is "coherent → strictly better coherent", and (G) forbids ranking that below the original.
- **Positive (PROVED):** one-directional repair classes satisfy (TC) together with guidance (and, for informing repairs, also the certificate). These are informing-only (old side silent) and silencing-only (new side silent). But they cannot cover: the rival BBB has no one-directional repair.

---

## 1. Setting and tools

**Advice.**
- A problem g is taken modulo sign. φ_k(p, g) = Σ_j (c + ε δ_jk) p_j g_j for k = 1, 2, 3.
- C_p accepts g ("P") iff min_k φ_k > 0, and accepts −g ("N") iff max_k φ_k < 0; otherwise it is silent. Boundary indices use the same formula (the limits).
- Since φ is linear in p, C_p accepts g iff T1 accepts p∘g (the lead's observation 1, CHECKED).

**The class-1 chart.** Write g = (1, −x, −y) with x, y > 0, and put a = p₂/p₁, b = p₃/p₁, κ = ε/c. Then:
- C_p says B (world-1-correct) iff F_p := (ax + by) + κ max(ax, by) < 1;
- C_p says A (majority) iff G_p := ax + by > 1 + κ;
- C_p is silent otherwise.

For q = a∘r one has F_q(x, y) = F_a((r₂/r₁)x, (r₃/r₁)y), and the same for G. The diagonal action is a translation in log-coordinates.

**Lead's observations, checked.**
- Observations 1–3 are correct: diagonal maps preserve the signs of coordinates, ranks and null sets. In each chart the invariant measure is dx dy/(xy), which is infinite.
- Observation 4 is corrected in §3.3.
- Observation 5 is now false for repair engines (§4).

**Lemma 1.1 (precision window; PROVED).** Fix a pencil g_t = (1, −t x₀, −t y₀), t > 0.
- Every selected model reads B, then S, then A as t grows. This holds because every φ_k is non-increasing in t.
- For interior p the silent band [t_l, t_u] has t_u/t_l = (1+κ)(1 + κm) with m = max(ax₀, by₀)/(ax₀ + by₀) ∈ [½, 1). So t_u/t_l ∈ [(1+κ)(1+κ/2), (1+κ)²).
- Closed form, used for exposure: if some C_q satisfies min φ ≥ 0 at g_t and max φ ≤ 0 at g_{t'}, then t'/t ≥ (1+κ)(1+κ/2).
  - *Proof.* Write s = q₂x₀ + q₃y₀. The first condition gives c q₁ ≥ t s (c + ε/2). The second gives (c + ε) q₁ ≤ c t' s. Here s > 0, since s = 0 forces q = e₁, which accepts g everywhere. ∎

At ε = 3/10 the window is [184/49, 256/49] ≈ [3.755, 5.224].

**Lemma 1.2 (exposure is non-betweenness; PROVED).** Write D_p = {C_p ≠ X}. The following are equivalent:
- some C_q agrees with X a.e. on D_p;
- D_p ∩ D_q is null;
- X ∈ {C_p, C_q} a.e., written X ∈ Betw(C_p, C_q);
- ρ(X, C_p) + ρ(X, C_q) = ρ(C_p, C_q).

Spl(X) := {p : exposure fails at p} is closed, because p ↦ C_p is continuous in measure on the closed simplex.

---

## 2. Step 1: the certificate inside the family

**Theorem 1 (PROVED, every ε ∈ (0, 1)).**
- *Vectors.* Put v_p = ((1+κ)a, b) and w_p = (a, (1+κ)b). Then F_p(z) = max(v_p·z, w_p·z). For p₀ = u, v₀ = (1+κ, 1) and w₀ = (1, 1+κ), with R² := |v₀|².
- *Choice of p₁, p₂, p₃.* Choose them with v_j on the circle |v| = R, strictly between v₀ and the x-axis, so that b_j < a_j.
- *Strict maximum.* Since |v|² − |w|² = ((1+κ)² − 1)(a² − b²), every w_j (j ≥ 1) lies strictly inside the circle. Also w₀·v₀ = R² − κ². Hence at z = v_j the vector v_j is the unique maximiser of the eight inner products. So F_{p_j}(v_j) = R² > F_{p_k}(v_j) for every k ≠ j.
- *The certificate.* Take z_j = t_j v_j with t_j R² > 1 > t_j F_{p_k}(v_j) for all k ≠ j. Then C_{p_j} is not "B" at g_j = (1, −z_j) while every other C_{p_k} is.
- *Silence, not A.* G ≤ F/(1 + κ/2), and F is close to 1.
- *Cones.* All conditions are strict, so small open cones B_j around g_j work.
- *Rationality.* Rational points of the circle come from rational chords through v₀, which gives an exact instance. ∎

**CHECKED** (`s1_certificate.py`), at ε = 3/10:

| index | value |
|---|---|
| p₀ | u |
| p₁ | (1918, 2009, 1346)/5273 |
| p₂ | (212, 229, 76)/517 |
| p₃ | (5278, 5761, 34)/11073 |

Lower and upper expectations, row C_{p_j}, column g_l:

| | g₀ | g₁ | g₂ | g₃ |
|---|---|---|---|---|
| C₀ | (−.00095, .410) | (.00095, .417) | (.0072, .427) | (.018, .439) |
| C₁ | (.00099, .443) | (−.00099, .447) | (.0012, .453) | (.0085, .462) |
| C₂ | (.0083, .491) | (.0015, .491) | (−.0013, .493) | (.0013, .497) |
| C₃ | (.023, .556) | (.010, .551) | (.0015, .547) | (−.0014, .546) |

- The pattern holds on whole cones of aperture 1/4000, verified at the generators. The cones are disjoint.
- ε = 1/10 also passes.
- The margins are about 10⁻³. They are small but exact.

**The rebuilt defences.** Audit §6 rebuilds word for word with C_k := C_{p_k}:
- the P₀-cell integrals at world 1 are (−s on S_k; +s/4 on each other S_j);
- in audit's ranking each defence is accepted at world 1 and refused at worlds 2 and 3 (three negative cells survive every refinement);
- summing the four endorsement inequalities gives −ν(unused quarters) < 0, so no strictly positive charge endorses all four. This is an exact identity.

Two remarks:
- One source is T1 itself; all four are selected models.
- Indispensability is a property of audit's ranking. At the axiom level, competitiveness against Y_k could be met at worlds 2 or 3.

§4.4 shows that the defences of C_{p₀} = T1 and of C_{p₃} are (TC)-incompatible with the repair class.

---

## 3. Step 2: the repair lemma

### 3.1 The (a)-half: Theorem R1 (PROVED)

Let W_i(X) = {p : X ≤_i C_p pointwise}. For X outside the family, "≤" is strict.

**Theorem R1.** For every X outside the family, G(X) = Δ ∖ (W₁ ∪ W₂ ∪ W₃) is open and nonempty.

*Proof.*
1. *Irregular X.* If X contradicts itself, or errs on unanimous problems, on a non-null set, then every W_i is empty. Assume X is regular.
2. *W_i is closed.* Pointwise a.e. inequalities pass to limits in measure.
3. *e_i ∉ W_i.* X ≤_i I_i would force X = I_i.
4. *No point of W_i ∩ W_j on the face Δ_ij.* Take p on Δ_ij and let k be the third world.
   - C_p says A on every M_k problem, which is world-i- and world-j-correct. So X = A there.
   - On M_i and M_j, the ranks of regular advice at worlds i and j are reversed (rank_j = 2 − rank_i). So X = C_p there.
   - Hence X = C_p, a contradiction.
   - The same argument shows W₁ ∩ W₂ ∩ W₃ = ∅.
5. *Conclusion.* The open sets O_i = Δ ∖ W_i satisfy e_i ∈ O_i, Δ_ij ⊆ O_i ∪ O_j and Δ = ∪ O_i. The open KKM lemma gives ∩ O_i ≠ ∅. ∎

**Lemma R2 (PROVED).** If p ∈ G(X) and X ∈ Betw(C_p, C_q), then C_q ≤_i C_p on D_p fails at every world.
- *Proof.* Otherwise X ≤_i C_p.
- *In particular,* no partner of an (a)-index is a vertex, and none lies on the e_i-ward cevian from p.

### 3.2 The world-wise order and splice monotonicity

**Lemma 3.1 (PROVED).** C_q ≤_i C_a pointwise iff q lies on the cevian through e_i and a, on the e_i side.
- *Proof.* Pointwise ≤_i between coherent models means: M_q ⊆ conv(M_a ∪ e_i) and M_a ⊆ shadow_{e_i}(M_q). This forces equal angular ranges as seen from e_i. The silhouette lines from e_i pass through v_j and v_l, so equal ranges give q_j/q_l = a_j/a_l. ∎

**Lemma 3.2 (splice monotonicity; PROVED).** Put r = q/a componentwise. On class-k problems:
- C_q is somewhere strictly more majority-ward than C_a iff r_k < max_{i≠k} r_i;
- C_q is somewhere strictly more minority-ward than C_a iff r_k > min_{i≠k} r_i.

*Proof.* F_q(z) = F_a(Dz) and G_q(z) = G_a(Dz), with D = diag(r_i/r_k, r_j/r_k). F_a and G_a are increasing in each coordinate. ∎

CHECKED: 180 random (a, q, class) triples, 0 counterexamples (`s2_more.py`).

### 3.3 Consequences for PP8 and PP11 (PROVED)

**(i) No three-class pump.** "C_q says A where C_a is silent" on all three classes would need r_k < max r for every k, which is impossible. The same holds for B.
- The realisable doubly anchored rivals are Y₂ = C_a + A on cones of the two classes k ≠ M = argmax r.
- Y₂ is a strict pointwise world-M improvement of C_a. So a ∉ G(Y₂), and the splice partners a and q are both non-exposed.

**(ii) No Theorem-J configuration.**
- For r on the open edge Δ_ij, r_k = 0.
- "A on a class-i pattern inside C_a's silent region" needs r_i/a_i < r_j/a_j. On class j it needs the reverse. So the two cannot hold together.
- *Geometric reading.* In log-odds along the edge, every edge segment M_r has width exactly 2 log(1+κ). That is also the width of every interior M_a's shadow from the opposite vertex. So the strict window of Lemma J0 is never open.
- CHECKED: 0 of 300 random (a, r) pairs have the configuration.
- B-type patterns exist, but they give no "not both" step (PP11 §5.4).
- **So J1 does not constrain the rescaled family.** Closedness in the rival argument is not known to be contradictory here. Audit's closed construction fails for its own reason (audit §5), not by J1.

### 3.4 Exposure: Theorem E (PROVED)

A line *supports* a convex set K if it meets K and leaves K on one closed side.

**Theorem E.** Let X be outside the family. Suppose X agrees a.e. with a coherent model D_K outside a closed set Ē of problems that contains no line supporting K at a vertex. Here either K ⊂ int Δ with K not of the form M_q, or K = M_a with a interior. Then some index near a vertex of Δ is an (a)-index at which X is exposed.

**Case K = M_a (a interior), E = D_a ⊆ Ē.**
1. *Every vertex lies in G.* e_k ∈ W_l iff X = A a.e. on the third class. But a line of that class through a vertex of M_a, shifted slightly into M_a, lies outside Ē, and there X = C_a = S.
2. *Choice of vertex.* A(X|E) := {p : C_p = X on E} is closed. Some e_k lies outside it, since the three ideal models disagree on every mixed problem.
3. *Choice of p.* Take an interior p ∈ G ∖ A(X|E) close enough to e_k that M_p lies in the vertical-angle region of M_a at v_k(a). That region is open and contains e_k, by projective invariance from M.
4. *Separating lines.* From inside the vertical-angle region, M_p is strictly separated from M_a by a line supporting M_a only at v, for each of the three vertices v. On a neighbourhood N_v of such a line, C_p takes M_p's side while C_a is S or the opposite side. And N_v ∩ Ē = ∅. So N_v ⊆ D_p, and X = C_a there.
5. *Rigidity.* A partner q needs C_q = C_a a.e. on N_v. The sets of lines meeting M_q and M_a are regular closed, so they agree on N_v. So an arc of lines through v supports M_q, which gives v ∈ M_q.
6. *Conclusion.* Hence M_a ⊆ M_q. If S_q S_a⁻¹ maps M_a into itself it has an interior fixed point, so it is the identity and q = a. But a is a partner iff p ∈ A(X|E), which was excluded. ∎

**Case K ⊂ int Δ.**
1. *Matching fronts.* Take p near e_k. The lines strictly separating K from M_p lie in D_p. So a partner q has h_{M_q} = h_K on the open arc N_p of separating normals, and the endpoint argument gives N_p(M_q) = N_p(K).
2. *M_q ⊆ K.* For p near e_k, N_p contains the normals of M_q's two edges at v_k(q), because e_k is strictly outside both edge lines (projective invariance). The margin is uniform over the possible q, since M_q must contain K's front. So K ⊇ M_q.
3. *Contradiction.* Pick x₀ ∈ int K at distance at least δ₀ from M_q. Here δ₀ > 0 is uniform over the compact set {q : M_q ⊆ K}. The lines through points near x₀ that miss M_q form an open set O ⊆ D_q. Betweenness forces C_p = S on O, which fails once M_p is small. ∎

**Further cases.**
- *Points and segments K.* The same argument applies; the front cannot be two edges of a triangle.
- *Edge a (proof sketch).* The off-edge vertex e_k works with separation at both endpoints when X|E ≠ I_k|E. Otherwise an on-edge vertex works, with shallow lines through the segment replacing separation at the far endpoint.
- *Vertex a.* Every interior p ∈ G works, by Lemma R2.

### 3.5 CHECKED instances (`s2_instances.py`, `s2_more.py`, `s2_hull.py`, ε = 3/10)

Each row gives an index p with exact (a)-witnesses at all three worlds and an exact exposure witness. The exposure witness is a set of 2–3 lines of D_p on which the closed family system is infeasible.

| rival | exposed (a)-index p |
|---|---|
| T1 + B on a silent cone (world-1 improvement of T1) | (1, 200, 2)/203 |
| T1 + A on the same cone | (200, 1, 2)/203 |
| D_K, K = M minus the cap at its vertex 1 (coherent, near T1) | (200, 1, 2)/203 |
| D_K, K = M minus a thin cap at its vertex 2 | (200, 1, 2)/203 |
| splice: T1 on {\|g₁\| > \|g₂\|}, C_(31,34,35) elsewhere (outside Theorem E) | (200, 1, 2)/203 |
| two-class PP8 analogue Y₂ = C_a + A on class-1 and class-2 cones where C_q says A; a = (5,3,2)/10, q = (49,29,22)/100; not exposed at a or q, and a ∉ G | (200, 1, 2)/203 |
| edge rival: C_(3,2,0)/5 + B on a class-3 cone | (200, 1, 2)/203 |
| edge-majority rival: C_(3,2,0)/5 + A on a class-1 cone where it is silent | (200, 2, 7)/209 |
| vertex rival: I₁ + silence on a cone | (200, 1, 2)/203 |
| precise interior model D_(5,3,2)/10 | (200, 1, 2)/203 |
| D_K, K = M_q₁ ∩ M_q₂ ∩ M_q₃ (q_k = u moved away from e_k) | (200, 1, 2)/203 |
| D_K, K = conv(M_p₁ ∪ M_p₂), p₁ = (4,3,3)/10, p₂ = (3,4,3)/10, overlapping (a C_p₁/C_p₂ splice, so neither p₁ nor p₂ is exposed); exact cutting-plane witness of 10 lines | (7, 200, 2)/209 |
| BBB (minority advice everywhere; outside Theorem E) | (200, 1, 2)/203 |
| AAA (majority advice everywhere) | (200, 1, 2)/203 |
| the two §4 rivals X₁ and X₂ | p and p′ themselves |

### 3.6 Exposure at a KKM-dominator index

**(G)-admissibility.** "C_q ⪯_i X required at all three worlds" is (G)-admissible exactly when q ∈ G(X). Theorem R1 makes this possible for every rival, and Theorem E finds exposed points of G(X) for the locally coherent class.

**The natural near indices are the wrong ones.**
- For Y₂: a ∉ G(Y₂), and both a and q are non-exposed.
- For patch rivals, the exposed indices produced by the proof are near the vertices of Δ, far from the rival. So the repair records are long-range, with D large.
- PP11's pinned neighbourhoods (J4) do not arise, because Theorem J has no instance here (§3.3).

**But exposure plus all-world acceptance is not enough.** §4 shows that such records, transported by (IB), violate (TC). In fact the following holds in any system with (G), (IB) and (TC), for the rivals X₁ and X₂ of §4.2 (PROVED):
- C_p ⪯₁ X₁ and C_{p′} ⪯₁ X₂ cannot both hold.
- So the KKM dominators of tiny precision-violating patches cannot all be local.

### 3.7 What remains OPEN

Exposure for rivals that agree with no coherent model near any of its supporting lines, for example measurable fine mixtures of selected models.

A minimal counterexample needs G(X) ⊆ Spl(X). That would require, at least on any component of G(X) where partners are locally unique, a common partner q with:
- X = C_q on every line whose arrangement crosses that component;
- G(X) ⊆ A(X|D_q).

At interior boundary points of such a component, the separation argument of §3.4 then gives (a) back, which is a contradiction **whenever** M_q can be separated from some e_i by a line supporting the boundary model at a vertex. I have no proof that this always happens.

---

## 4. Step 3: (TC) for repair records

### 4.1 Classes and the shape of a hard violation

**The repair classes.**
- A record d = (D, old, new) is **repair-eligible** if:
  - its old side is a family pattern on D;
  - its new side is not;
  - it is a strict pointwise improvement at no world.
- These conditions depend on the record only, so they are compatible with (IB).
- **R_all** accepts every eligible record at all three worlds, in every context.
- **R_near** accepts, for each rival, the record from its nearest eligible index.

**Lemma 4.1 (PROVED).** Suppose a forbidden triangle X ⪯ Y ⪯ Z ≺ X is closed by strict guidance, so that it cannot be repaired by adding acceptances. Then two non-guidance links compose to a strict pointwise improvement.
- *Proof.* If one of the forward links is guidance, the ranks chain gives that the other link is a weak improvement. That contradicts eligibility. ∎

### 4.2 Theorem T (CHECKED, `s3_tc_violation.py`)

**Configuration.**
- One pencil g_t = (1, −t, −t) of world-1-minority problems.
- Cones K₁, K₂, K₃ of aperture 1/200 at t = 1, 27/20, 4. Here 4 lies in the window and 80/27 ≈ 2.96 lies below it.
- p = (200, 74, 37)/311: C_p is silent on K₁, K₂, K₃.
- p′ = (200, 59, 59)/318: C_{p′} says B on K₁ and A on K₃.

**The records.**

| record | old side | new side | non-family because |
|---|---|---|---|
| d₁ | C_p: SSS on K₁K₂K₃ | BBA | B at t₂ and A at t₃ are closer than the window |
| d₂ | C_{p′}: B·A on K₁·K₃ | S·B | non-monotone |
| d₁′ | SSS | BAA | B at t₁, A at t₂ |
| d₂′ | B·A | A·S | non-monotone |

- Each record is mixed at every world, and each new side is closed-infeasible (exact).
- X₁ := C_p with BBA agrees with C_{p′} on K₁ ∪ K₃. So by (IB),

  C_p ⪯₁ X₁ (d₁),  X₁ ⪯₁ U″ (a copy of d₂),  U″ = C_p + B on K₂ ∪ K₃.

- U″ strictly improves C_p at world 1, so U″ ≺₁ C_p by (G), and (TC) is violated.
- The primed pair gives C_p ⪯ X₁′ ⪯ C_p + A on K₁ ∪ K₂, a strict improvement at worlds 2 and 3.

**R_near fails too (PROVED).**
- Choose sub-cones so small that μ(cones) < ½ min{ρ(C_p, C_q) : C_q ≠ C_p on the cones}. Then p is the unique nearest selected model to X₁, and p′ the unique nearest to X₂.
- Both are eligible, so R_near selects both records.

### 4.3 Far repairs fail too (CHECKED, `s3_vertex_chain.py`)

**The records.**
- X₁ = I₂ on M₁ ∪ M₂ and A on M₃, except silence on a cone W₁ ⊂ M₃.
- X₂ = A on M₂ and S on M₁; on M₃ it is A, except silence on a cone W₂.
- d₁ = rec(I₁, X₁) and d₂ = rec(I₂, X₂) are both eligible (exact certificates).
- X₁ = I₂ on D₂. So I₁ ⪯₃ X₁ ⪯₃ U″, where U″ is a strict world-3 improvement of I₁.

**What this shows.**
- So R_all fails even when restricted to vertex indices, which are the exposed indices that Theorem E produces.
- These two rivals are not each other's nearest repair. This chain refutes R_all and "repair from the vertex", not R_near.

### 4.4 The certificate (CHECKED, `s3_cert_violation.py`; `s3_cert_chains.py`)

**Necessary form.** A chain made of a certificate link c_k and one repair, in either order, needs the repair's old side to be:
- "not B" on every E_{j,k} (j ≠ k);
- "B" on part T of S_k.

With E_{j,k} measure-dense in S_j, this becomes a closed condition at the central lines (PROVED). The set E_{j,k} can be any measure-dense subset.

**k = 0 (T1's defence) and k = 3: violations.**
- An explicit C_q, e.g. q = (2162, 2500, 47)/4709 for k = 0, realises the old side on whole cones.
- The repair also turns a cone W on the pencil of g_k from S to B, beyond T. Then the new side (S on T, B on W) is non-monotone.
- Result: C_k ⪯₁ Y_k ⪯₁ C_k + B on (S_k ∖ T) ∪ W, which is strictly better. Forbidden.

**k = 1, 2.** The closed old-side system is infeasible at the central lines (exact), and so on thin enough cones. So no single repair chains with these two defences.

### 4.5 A class for which (TC) holds (PROVED)

**Theorem 4.2.**
- R_inf (informing repairs: old side S on D) together with guidance and the certificate records with all their copies has no nontrivial accepted 3-cycle at any world. Hence (TC) holds.
- R_sil (silencing repairs) together with guidance also satisfies (TC) at every world.

*Proof.* In an accepted cycle each problem's advice returns to its start.
1. *An informing link must undo itself.* By (a), an informing link has a non-null part where S changes to world-i-bad advice.
2. *Nothing can undo it.* Returning that advice to S would need:
   - a guidance link that lowers rank (impossible);
   - another informing link (impossible: its old side must be S);
   - a certificate link (impossible: certificate links change only B ↔ S).
3. *Cycles of certificate copies and guidance alone* are cycles of audit's ranking, which has none (audit §3).
4. *R_sil.* The argument is the same with the roles of the two directions exchanged. ∎

**Coverage fails (PROVED).** BBB has no one-directional repair:
- an informing repair needs a selected model that agrees with BBB wherever it is not silent, and every member says A somewhere;
- a silencing repair needs BBB to be silent somewhere, and it never is.

BBB is nonetheless exposed at an (a)-index (§3.5). So the obstruction is one-directionality, not exposure.

---

## 5. Answers to the brief, and the nearby target

**Step 1.**
- Achieved inside the family, for every ε.
- The geometric certificate is the four indices with silence at their own cones and acceptance at the others'.

**Step 2.**
- (a) is universal (R1).
- Exposure is PROVED for the locally coherent class (Theorem E) and CHECKED beyond it.
- The general measurable case is OPEN (§3.7).
- The analysis of PP8 and PP11 changes in this family: there is no three-class pump and no Theorem-J configuration.

**Step 3.**
- (TC) is violated by certified triangles made of two repairs and one guidance link at each world.
- It is also violated by a certificate defence (T1's), one repair and one guidance link.
- (TC) holds only for one-directional repair classes, and those do not cover.
- **This is the exact obstruction outcome for the proposed mechanism with all-world, local or vertex repairs.**

**Nearby reachable target (proposed).** Keep one-directional repairs, which are (TC)-safe. Allow mixed repair records only through a selection that is coordinated across rivals. Necessary conditions:
- it must never accept both links of a precision-window pair (§4.2) at the same world;
- it must never accept a mixed repair that undoes a certificate defence's E-worsening (§4.4).

The cleanest test case is the one-pencil, three-cone module of §4.2: decide by an exact SAT search whether some world-allocation of mixed repairs covers every rival of the module, keeps (TC), and keeps the KKM requirement. An UNSAT answer there would turn §4 into an obstruction for every repair selection, not just for R_all, R_near and vertex repairs.

---

## 6. Scripts (`PP13_py/`)

| script → output | content | label |
|---|---|---|
| `pp13core.py`, `s2_geometry.py` | exact advice, cones, closed and strict feasibility over the closed simplex, polygon clipping | library |
| `s1_certificate.py` → `.out` | Theorem 1 instances (ε = 3/10 and 1/10), cones, rebuilt audit §6 | CHECKED |
| `s1_search.py` | choice of circle chords (margins) | search only |
| `s2_instances.py`, `s2_more.py`, `s2_hull.py` → `.out` | §3.5 certificates; splice-monotonicity and Theorem-J screens | CHECKED (screens NUMERICS) |
| `s3_tc_violation.py` → `.out` | Theorem T, worlds 1, 2, 3 | CHECKED |
| `s3_vertex_chain.py` → `.out` | §4.3 | CHECKED |
| `s3_cert_chains.py`, `s3_cert_violation.py` → `.out` | §4.4 | CHECKED |
| `explore_chain.py` | the one-pencil search that found Theorem T | NUMERICS |
