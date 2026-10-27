# PP12. Equivariance for the rescaled family: the reduction, an exact obstruction, and what survives

21 October 2026. Brief 42, Task A. One reader (me); not refereed.

**Labels.** PROVED: full argument given here. CHECKED: exact rational computation. NUMERICS: evidence only. OPEN / CONJECTURE: as stated. "Imported" marks a result from an earlier note that is used and not re-proved.

**Scripts** are in `PP12_py/`. Run each as `python3 -I -B <script>` from inside that folder; outputs are in `*.out`. Scripts use 0-based worlds and write advice A/B as M/O.

**No assumption is added.** Invariance is the hypothesis under test and is stated wherever it is used.

---

## 0. Verdicts

1. **Observations 1 and 2 are correct (PROVED; CHECKED).**
   - For every p in the closed simplex, C_p = T1∘S_p with S_p(g) = p∘g. This covers the edge and vertex models too, with S_p singular there.
   - The interior models form one orbit of the diagonal group G. Each open edge is one more orbit, and each vertex model is fixed by G.
   - Under invariance the axioms reduce to the list (R0)–(R8) in §2.
2. **Theorem E: the reduced problem has no solution (PROVED).**
   - *The rival.* Λ := "accept the majority orientation on every mixed problem, correct on unanimous ones". Λ is fixed by G.
   - *The mechanism.* Under invariance, the interior section {p : C_p ⪯_i Λ} is either empty or all of int Δ. Closed sections then force C_{e_m} = B^m ⪯_i Λ for every vertex m. But strict (G) refuses this for every m ≠ i, because Λ is a strict pointwise world-i improvement of B^m. So T1 is defended against Λ at no world.
   - *What it uses.* Only the strict half of (G), competitiveness of T1, closed sections at the vertices, and invariance on the records rec(C_q, Λ).
   - *What it does not use.* (TC), (IB), undominatedness, (C), (LA).
   - *Consequence.* No choice of verdict can help: germs, asymptotic densities and lexicographic levels are all invariant objects. The obstruction is a single G-invariant record of infinite Haar mass.
3. **The nearby weaker notion "invariance under a subgroup" also fails (Corollary E2, PROVED).**
   - Invariance under one non-scalar diagonal map d is already impossible. The orbit {d^n q} runs to two boundary points, and Λ strictly beats the boundary model there at every world.
   - Only the scalar maps, which fix every selected model, escape.
   - The two-world version also fails, with the coherent rival D_Δ (Corollary E3). So the two-world gated template has equivariant keys but cannot have invariant verdicts.
4. **Compatibility checks (§4).**
   - (G), both halves, and (IB) are G-invariant conditions, so there is no conflict there.
   - **Theorem J and J1 do not apply to the rescaled family (Proposition P, PROVED; CHECKED).**
     - No edge model is strictly A-ward of an interior model on non-null parts of two minority classes. So hypothesis (ii) of Theorem J, as stated in REFEREE_PP11, fails at every interior index and on every edge.
     - Hence there are no forced cuts, and the question "does invariance fix the cut positions?" does not arise.
     - Brief observation 4 does not hold for this family. J1 does not exclude rules whose accepted records form closed sets for the rescaled family, and audit's construction did not fail in the way J1 predicts.
   - **PP2 Thm 6.** An order-equivariant fixed key is excluded. An invariant key is blind on each class, so all content goes to a record-based secondary rule (PROVED, given PP2 Thm 6 and referee R2).
   - **FF2.** Haar-invariant fields are never integrable, so FF2 Thm 4.1 neither applies to them nor is contradicted by them. If such a field endorses T1's local comparisons, it is blind at T1 (PROVED).
   - **S9.** Under invariance an anchor is transported to every C_p. An anchored complete world must then be one additive loss that is relatively invariant (exponential density), and it is blind at T1 (sketch, given S9).
   - **X2 (round 26) is directly relevant, though the brief does not list it.**
     - X2 studied this same equivariant setting; its posterior family is the rescaled family.
     - Its X2.9 needs only **local** invariance, but it uses transitivity.
     - Theorem E needs invariance on non-local records, but no transitivity and no (TC).
5. **What survives: local invariance (§5).** Here invariance is imposed only on records bounded away from the coordinate planes.
   - **Lemma D (PROVED).** For a fixed rival, rec(C_p, X) has finite Haar mass for at most one p. So local invariance never meets the closed-section clause, and Theorem E cannot reach it.
   - **Theorem L (PROVED; geometry CHECKED for 10 values of ε).** Under (TC), X2.2(c) and X2.9 hold for every world that is complete on the relevant local records. So a locally invariant cover needs local **incomparability** at each world near its vertex. In particular X2.7's balanced Haar-lexicographic rules, and every total, additive or lexicographic local rule, are excluded.
   - **Lemma N (PROVED).** The records that closed choice at a vertex actually forces under (TC) never compose with each other. Together with guidance alone they create no (TC) violation.
   - **OPEN.** Does a locally invariant system satisfying every axiom with (TC) exist?
6. **What this means for constructions (§6).**
   - Any system for the rescaled family must break the diagonal symmetry on records of infinite Haar mass, already on the single rival Λ.
   - The sections of Λ must form a Sperner-type cover of Δ in which world i's set avoids the edge opposite e_i and the other two vertices.

---

## 1. Setting and the orbit (observation 1)

**Problems and classes.**
- A problem is g ∈ R³ modulo sign, with coordinates nonzero (the rest is null).
- U is the unanimous class. M_w is the class whose majority orientation h has h_w < 0 and the other two coordinates positive.
- Advice relative to h: A (accept h), S (silence), B (accept −h), X (contradiction).
- On M_w, world w ranks A 2, S 1, B 0, and the two majority worlds rank A 0, S 1, B 2. X has rank 3.

**The group.** G = (R_{>0})³ acts by S_d g = d∘g, and on models by X ↦ X∘S_d.
- S_d preserves every coordinate sign, hence every class and the orientation h. So r_i(X∘S_d, g) = r_i(X, S_d g).
- S_d maps μ to an equivalent measure, so null sets are preserved.
- In the log chart of a class, S_d is a translation. On M_w, write (x, y) = (log h_j/|h_w|, log h_l/|h_w|). Then S_d acts on (x, y) by (+log d_j/d_w, +log d_l/d_w). Scalar d acts trivially there.

**T1 in the chart (PROVED, direct computation).** T1 = D_M with vertices v_i = c1 + εe_i, so T1 accepts h iff cΣh + ε min h > 0. Put A_ := 1 + ε/c. On M_w:
- **A** iff e^x + e^y > A_ (an up-set);
- **B** iff c(e^x + e^y − 1) + ε max(e^x, e^y) < 0 (a convex down-set);
- **S** on the band between these two regions.

The band contains two asymptotic strips, {x → −∞, 1/A_ < e^y < A_} and its mirror image. On U, T1 is correct.

**Observation 1 (PROVED; CHECKED, `e0_orbit.out`).** For every p ∈ Δ, boundary included, D_{M_p}(g) = T1(p∘g), with M_p = {p∘m/(p·m) : m ∈ M}.

*Proof.*
- Since M ⊂ int Δ, p·m > 0 for every m ∈ M and every p ∈ Δ. So (p∘m)·g/(p·m) = m·(p∘g)/(p·m).
- The minimum over M is positive iff min_m m·(p∘g) > 0, and the maximum is negative iff max_m m·(p∘g) < 0. ∎

*Exact check.* 56,000 exact agreements over interior, edge and vertex indices at ε = 3/10 and ε = 1/10.

**Consequences (PROVED).**
- **Equivariance.** C_{ν(d∘p)} = C_p∘S_d, where ν normalises to the simplex. (CHECKED: 8,000/8,000.)
- **Interior.** int Δ is one orbit. Its stabiliser is the scalars.
- **Edges.** For p in the open edge {p_l = 0}, C_p = E_{jk}∘S_{d}, where E_{jk} := C_{(e_j+e_k)/2} and d = (2p_j, 2p_k, anything). So each open edge is one G-orbit, and E_{jk} is fixed by the one-parameter subgroup H_l that scales coordinate l.
- **Edge models in the chart.** E_{jk} says A on all of M_l. On M_j its advice is a function of the single ratio h_k/|h_j|: a vertical strip of S of log-width 2 log A_, with A on one side and B on the other. M_k is the mirror image. (CHECKED.)
  - These are exactly T1's asymptotic profiles: the limit of T1 at (x, y + s) as s → −∞.
  - The edges are imprecise, with credal set an interval of [e_j, e_k].
- **Vertices.** C_{e_m} = B^m := {h : h_m > 0}, which is B on M_m and A on the other two mixed classes. It is G-fixed.
- **Convergence.** p_n → p in Δ implies C_{p_n} → C_p in measure. The reason: T1(p∘g) is locally constant in p wherever p∘g avoids the boundary cones of T1, which holds for a.e. g. Then use dominated convergence. (CHECKED along p_n → edge points.)

This is the toric picture. Δ is the compactification of the orbit R² by the moment map v ↦ ν(e^v). Faces of Δ are orbits of quotient tori, and the boundary models are the limits of translates of T1.

**Lemma 1.1 (the orbit map is continuous; PROVED).** For each model X, v ↦ X∘S_{e^v} is continuous in μ-measure.

*Proof.* In each chart μ has a density ρ ∈ L¹ with respect to Lebesgue measure. For measurable E,

  μ(τ_v E Δ E) ≤ ‖(1_E ρ)(· − v) − 1_E ρ‖₁ + ‖ρ(· − v) − ρ‖₁ → 0,

by continuity of translation in L¹. ∎

**No finite invariant measure (observation 3; PROVED).** A finite translation-invariant measure on R^k gives equal mass to every unit cube of the lattice tiling. Those masses are summable, so each is 0.

---

## 2. The reduction (observation 2) and the reduced T1 problem

Assume each ⪯_i is G-invariant: X ⪯_i Y iff X∘S ⪯_i Y∘S, for all S ∈ G. Then C_p ⪯_i X iff T1 ⪯_i X∘S_p^{-1} (PROVED: apply invariance with S = S_p^{-1}). Write V_i(X) := {v ∈ R² : T1 ⪯_i X∘S_{e^v}^{-1}}.

**The reduced T1 problem (PROVED equivalent to the axioms on the rescaled family, given invariance).** These are conditions on G-invariant relations ⪯_1, ⪯_2, ⪯_3 on the full domain.

- **(R0)** Reflexivity, (G) both halves, (IB) and (TC), at each world.
- **(R1) Interior defence.** For every X there is some i with T1 ⪯_i X.
- **(R2) Edge defence.** For every edge jk and every X, E_{jk} ⪯_j X or E_{jk} ⪯_k X. One model per edge suffices, because each edge is one orbit.
- **(R3) Vertex defence.** B^m ⪯_m X for every X. This is automatic by the weak half of (G), since B^m has world-m rank 0 everywhere.
- **(R4) Undominatedness.** T1 and the three E_{jk} are undominated. Vertices are automatically undominated: X ⪯_m B^m forces X = B^m, by strict (G).
- **(R5) Closedness along the interior orbit.** Each V_i(X) is closed in R².
  - By Lemma 1.1, this says that world i's rival-section {Y : T1 ⪯_i Y} has closed preimage under every orbit map v ↦ X∘S_{e^v}^{-1}.
  - This is weaker than closedness in measure, which J1 does not forbid for this family (§4.2).
- **(R6) Closedness along the edge orbits.** For each edge jk, the set {s ∈ R : E_{jk} ⪯_i X∘S_{d(s)}^{-1}} is closed, where d(s) = (e^{s/2}, e^{−s/2}) on coordinates (j, k).
- **(R7) Closedness at infinity.** If v_n → ∞ with ν(e^{v_n}) → r ∈ ∂Δ and v_n ∈ V_i(X), then C_r ⪯_i X. The same holds along edge orbits running to a vertex.
- **(R8) Direct (C) and (LA).**
  - The coherent class is G-stable: D_K∘S_d = D_{T_d K} with T_d(m) = d∘m/(d·m), a projective automorphism of Δ that preserves convexity (Rescaling note, Thm 3(iii)). The undominated set is G-stable too.
  - So (C) reduces to: every X tied with T1, or with some E_{jk}, at all three worlds is coherent and undominated (plus the same statement for the remaining members of C_L).
  - (LA) follows from (R4).

**What the remaining clauses become.**
- **KKM dominators** (a consequence of (R1), (R2), (R5)–(R7)). For every X, either T1 ⪯_i X∘S_d at all three worlds for some d (T1 dominates a translate of X), or some edge or vertex model dominates X at all three worlds.
- The interior defence clause is "T1 is competitive on {1,2,3} against every model". Undominatedness of every interior C_p is undominatedness of T1. Both are as the brief says.

---

## 3. Theorem E: the reduced problem is unsatisfiable

Let Λ be the model that is A on M_1, M_2 and M_3 and correct on U. Λ∘S = Λ for every S ∈ G.

**Lemma 3.1 (PROVED; CHECKED, `e1_invariant_rivals.out` (1)).**
- (a) For m ≠ i, Λ is a strict pointwise world-i improvement of B^m.
- (b) For an open edge jk with third world l, Λ is a strict pointwise world-l improvement of every edge model C_r, r ∈ (e_j, e_k).

*Proof.*
- (a) Λ and B^m differ only on M_m, where Λ says A and B^m says B. World i ≠ m is a majority world on M_m, so this lowers its rank from 2 to 0.
- (b) On M_l both models say A. On M_j and M_k, the edge model says S or B on non-null sets (the strip structure of §1). World l is a majority world on both classes, so A has rank 0 there. ∎

**Theorem E (PROVED).** Let ⪯_1, ⪯_2, ⪯_3 be any relations on the full domain, with the rescaled family through T1 as selection. Assume:
- (a) the strict half of (G) at every world;
- (b) T1 is competitive on {1,2,3} against Λ;
- (c) the sections {p ∈ Δ : C_p ⪯_i Λ} are closed at the three vertices;
- (d) C_q ⪯_i Λ iff T1 ⪯_i Λ, for every q ∈ int Δ and every i. This holds if each ⪯_i is G-invariant, because Λ is G-fixed and C_q = T1∘S_q.

Then these assumptions are inconsistent.

*Proof.*
1. By (b), T1 ⪯_i Λ for some i.
2. By (d), C_q ⪯_i Λ for every interior q.
3. By (c), C_{e_m} = B^m ⪯_i Λ for every m. Take m ≠ i.
4. Lemma 3.1(a) and strict (G) refuse B^m ⪯_i Λ. Contradiction. ∎

**Remarks.**
- *Domain.* Λ is measurable, so it lies in the full domain. It is incoherent; its coherence is never used.
- *Unused axioms.* The theorem uses no (TC), (IB), undominatedness, (C), (LA), and no edge clause.
- *Why no verdict design helps.* The brief asks for verdicts that handle disagreements of infinite Haar mass, for example through germs, asymptotic densities, or lexicographic structure relative to T1's boundary curves. Any such device that is G-invariant gives the same verdict on every record of the orbit {rec(C_q, Λ) : q ∈ int Δ}. That forces V_i(Λ) ∈ {∅, R²}, which is all the proof uses.
- *Other invariant rivals (CHECKED, `e1` (2)).* G-invariant models are a.e. class-constant (the standard ergodicity of a transitive translation action), so there are 256 of them. Exactly four have every world excluded by the mechanism of Theorem E: Λ, and the three models with one S among A, A, A.
  - The coherent class-constant models are not obstructions. B^1 leaves worlds {2, 3}, D_{[e_1,e_2]} leaves {3}, and D_Δ leaves all three.
- *Link to PP2.* PP2's numerics found Λ ("A on every mixed problem") as the centre of the minimal unbeaten tripods.

**Corollary E2 (a single non-scalar map; PROVED; CHECKED, `e1` (2)).**
- *Statement.* Replace (d) by invariance under one diagonal map d that is not a scalar: X ⪯_i Y iff X∘S_d ⪯_i Y∘S_d for all X, Y. Equivalently, invariance under the cyclic group of d, or under any one-parameter subgroup that is non-trivial modulo scalars. Keep (a), (b) at one interior q₀, and closed sections at the boundary points named below. The assumptions are again inconsistent.
- *Proof.* Write θ = log d, which is not proportional to (1,1,1).
  1. C_{ν(d^n∘q₀)} = C_{q₀}∘S_{d^n} and Λ∘S_{d^n} = Λ. So C_{q₀} ⪯_i Λ forces C_{ν(d^n q₀)} ⪯_i Λ for all n ∈ Z.
  2. As n → +∞ (resp. −∞), ν(d^n∘q₀) converges to the point r⁺ (resp. r⁻) of the face spanned by the coordinates where θ is maximal (resp. minimal). Closedness gives C_{r±} ⪯_i Λ.
  3. In every case strict (G) refuses one of these at each world:
     - unique max k and unique min l: r± = e_k, e_l. Lemma 3.1(a) excludes every i ≠ k (via B^k) and every i ≠ l (via B^l), so no world remains;
     - max attained on {j, k}: r⁺ lies on the open edge jk and r⁻ = e_l. Lemma 3.1(b) excludes l, and (a) via B^l excludes j and k;
     - min attained on {j, l}: symmetric. ∎
  - CHECKED: Λ is excluded for all 12 types of θ; it is the only class-constant model excluded for every type.
- *Scope.* Scalar maps fix every selected model, so they escape. Nothing here says scalar invariance is harmful.

**Corollary E3 (two worlds; PROVED; CHECKED, `e1` (3)).**
- *Statement.* For a two-world interval target [a, b] ⊂ (0, 1), take the rescaled family and invariance under any non-scalar d. Then the target is not competitive against the vacuous model D_Δ (silent on every mixed problem).
- *Proof.*
  - The vertex models are "accept g" and "accept −g".
  - D_Δ is a strict world-1 improvement of the second vertex model and a strict world-2 improvement of the first.
  - The proof of Theorem E then applies with D_Δ in place of Λ. ∎
- *Consequence for the brief's template.* The gated construction of gate2d, applied to the rescaled two-world family, is a valid system: its keys are translations in log-odds, so the gate is order-equivariant. But its verdict Φ = 2·on − off is measured by the Gaussian μ, and it cannot be replaced by an invariant one. The template is equivariant only in its gate.

---

## 4. Compatibility checks (brief item 2)

These checks are recorded for their independent value. Theorem E already excludes invariance.

### 4.1 (G), both halves, and (IB): no conflict (PROVED)
- Ranks are equivariant and null sets are preserved. So X is a pointwise weak (strict) world-i worsening of Y iff X∘S is one of Y∘S.
- G acts on records, (S, X|_D, Y|_D) ↦ (S⁻¹D, …), and preserves "record of".
- So (IB) together with invariance is just invariance of R_i as a set of records. Guidance-only relations satisfy all of (G), (IB), (TC) and invariance.

### 4.2 Theorem J and J1: their hypothesis fails for the rescaled family (PROVED; CHECKED, `e2_J0_rescaled.out`)

**Proposition P.** Let a be interior and r a point of the open edge {p_3 = 0}. Write π(a) := (a_1, a_2, 0)/(a_1 + a_2).
- **(P1)** On M_1 ∪ M_2, the advice of C_a is weakly A-ward of the advice of the edge model C_{π(a)}.
- **(P2)** Along the edge, edge-model advice on M_1 is A-ward monotone in r_2/r_1, and on M_2 it is A-ward monotone in r_1/r_2.
- **(P3)** Hence no edge model C_r is strictly A-ward of C_a on non-null subsets of both M_1 and M_2. In particular, no C_r says A on G_1 ∪ G_2 (with G_w ⊂ M_w non-null) while C_a is silent there.

The same holds on every edge, by symmetry.

*Proof.* Take g ∈ M_1, so g_1 < 0 < g_2, g_3. Put t := a_2 g_2/(a_1|g_1|) and s := r_2 g_2/(r_1|g_1|).
- C_a says A iff c(a_2g_2 + a_3g_3) > (c+ε)a_1|g_1|. C_{π(a)} says A iff c a_2 g_2 > (c+ε) a_1|g_1|, i.e. iff t > A_. Since a_3g_3 > 0, C_{π(a)} = A implies C_a = A.
- C_a says B iff c(a_2g_2 + a_3g_3 − a_1|g_1|) + ε max(a_2g_2, a_3g_3) < 0. This implies c(a_2g_2 − a_1|g_1|) + ε a_2g_2 < 0, which says C_{π(a)} = B.
- Together these give (P1).
- C_r (r_3 = 0) says A iff s > A_ and B iff s < 1/A_. That is (P2) on M_1. M_2 is the mirror image.
- For (P3): strictly A-ward of C_a somewhere on M_1 forces, by (P1), strictly A-ward of C_{π(a)} there. By (P2) this forces r_2/r_1 > a_2/a_1. On M_2 it forces r_1/r_2 > a_1/a_2. These are incompatible. ∎

*Check.* 18,000 exact random cases for each of (P1) and (P2) at ε ∈ {3/10, 1/10, 1/100}, with no violations. 60,000 draws give no J0 instance for the rescaled family. Untargeted draws find 7 J0 instances for the homothetic family at ε = 3/10 and none at the smaller ε; PP11's `t4` constructs them exactly (180/180).

**Consequences (PROVED).**
- Theorem J (1)–(2), J1 and J4 need a selected edge model saying A on two-class patterns where an interior selected model is silent (REFEREE_PP11, scope (ii)). For the rescaled family there is no such pair at any interior index, for any ε, on any edge.
  - This is the gate2d mechanism ("selected bands are never strictly nested") carried over to three worlds. Each edge model is a fixed-width translate of the asymptotic strip, and every interior model's A-boundary on M_1 ∪ M_2 lies beyond that of its own projection onto the edge.
- The single-class version gives nothing. With G ⊂ M_1 only, world 1 is excluded by strict (G), and the record goes to world 2 without any cut.
- **So there are no forced cuts for this family, and invariance has nothing to fix.**
- **Brief observation 4 should be withdrawn for this family.**
  - J1 does not exclude rules for the rescaled family whose accepted-record sets are closed in the rival argument.
  - Audit's construction does not fail "as J1 predicts". J1 predicts that a closed rule leaves an interior selected model dominated, or loses an edge defence. Audit's rule leaves every regular model undominated, and it fails competitiveness against a split-cell rival (AUDIT_rescaling_construction §5), which is a different failure.
- OPEN: whether some other mechanism forces non-closed accepted-record sets for the rescaled family.

### 4.3 PP2 Thm 6: invariant fixed keys (PROVED, given PP2 Thm 6 with referee R1, and referee R2)

Consider a world-1 weak gate with a fixed key k_1, and require the gate to be G-invariant. There are two cases.
- **(a) Order-equivariant key.** Here k_1(Sg, j) = φ_S(k_1(g, j)) with φ_S increasing, e.g. any increasing function of a linear functional of the log coordinates. If k_1(·,1) is not essentially constant on M_1, Thm 6 (in R1's form) excludes it, whatever the verdicts and the selection.
- **(b) Invariant key.** Here k_1(Sg, j) = k_1(g, j). G is transitive on each class, so k_1 is a.e. constant on each pair (class, level), and Thm 6 does not apply.
  - R2 then forces one constant on all mixed level-1 steps, and min(k_1(·,2), κ) constant as well.
  - So the gate only compares coarse step types, and all ordering content lies in a record-based secondary rule. That is design (E1) of PP2 §4.
- **What is left:** priorities chosen from the record itself. Theorem E excludes their invariant versions too.

### 4.4 FF2 (PROVED)
- Suppose a field is Haar-invariant: ℓ_i(g, a) dμ = ψ_i(g, a) dλ with ψ_i(Sg, a) = ψ_i(g, a), where λ is Haar measure. Then ψ_i depends only on the class and the advice, and ∫ max|ℓ| dμ = ∞ unless ℓ = 0.
  - So FF2's (H2) fails, and Thm 4.1 neither applies nor is contradicted.
- If such a field endorses T1's local comparisons at all three worlds, FF2's Step 1 runs on sets of finite Haar mass: Lyapunov's theorem holds for the σ-finite λ on sets H_n with λ(H_n) < ∞.
  - That step makes T1 pointwise weak w-Bayes at some w.
  - T1 uses A, S and B on non-null subsets of every mixed class. So w·ψ(c, A) = w·ψ(c, S) = w·ψ(c, B) for every class c: the field is blind at T1.
  - X2.7's level 0 is of exactly this form.
- In the other direction, invariance does not weaken FF2's conclusion. If an integrable ℓ endorses an invariant world, every transported ℓ^S does too, and each is integrable.

### 4.5 S9 anchoring (sketch, given S9 for worlds complete on small records)
- *Transport.* Suppose verdicts on records out of C that contain an anchor pattern are exactly ℓ's. Then by invariance, verdicts out of C∘S on the transported pattern are exactly ℓ^S's.
- *What S9 then forces.* If the world is complete on small records, S9 makes it equal to ℓ there and also equal to ℓ^S. So ℓ^S = κ(S)ℓ, and the Haar density satisfies ψ(x + v, a) = e^{θ·v} ψ(x, a). The density is exponential in log coordinates, hence never integrable.
- *Blindness at T1.* Within a class the minimiser of w·ψ(x, ·) does not depend on x. So if all three worlds are anchored, T1 must be blind, exactly as in §4.4.
- *Direct (C) fails.* T1 then ties, at every world, with the incoherent models obtained by changing T1's advice on part of one class.

### 4.6 X2 (round 26): the decisive prior result
- X2 §5 defines "equivariant systems": every A_i is G′-invariant. That is full invariance, and Theorem E excludes them in two lines, without transitivity.
- X2.9 (refereed in X12; geometry repaired there) assumes only that **local** accepted records are invariant. But it uses closure under realisable composition in two places:
  - X2.2(c), where the rival C_p ⪯_k X_P is composed with a pure worsening;
  - the final step.
- Under (TC) the final step is still a (TC) violation, X ⪯ Y ⪯ Z ≺ X. The first step is where the gap lies (§5).

---

## 5. The nearby notion: local invariance

**Definition.** A record is **local** if its disagreement set has relatively compact image in every class chart (X2 §5). World i is **locally invariant (LI)** if R_i ∩ {local records} is G-invariant.

**Lemma D (decoupling; PROVED; NUMERICS, `e4_haar_mass.out`).**
- (a) For distinct interior p, q, the Haar measure of {C_p ≠ C_q} is infinite.
- (b) For a fixed X, rec(C_p, X) has finite Haar mass, and in particular is local, for at most one p ∈ int Δ.

*Proof.*
- (a) On M_1, C_q is T1 translated by v = (log q_2/q_1 − log p_2/p_1, ·) ≠ 0 relative to C_p. Suppose v_1 ≠ 0. The A-boundary has the vertical asymptote x = log A_ as y → −∞, so a half-strip of x-width |v_1| at y → −∞ separates the two A-regions. If v_1 = 0, use the horizontal asymptote instead.
- (b) Two such p, q would give λ(C_p Δ C_q) ≤ λ(D(C_p, X)) + λ(D(C_q, X)) < ∞, contradicting (a). ∎

*Numerics.* The disagreement area in [−R, R]² grows linearly in R, for four translations.

So LI says nothing about how verdicts on rec(C_p, X) vary with p. It cannot meet closed sections, and Theorem E cannot reach it. This agrees with X12 §2.9.

**What closed choice at a vertex forces under (TC).** Fix a world k, a compact cone P ⊂ M_k, and X_P := B^k with S on P.
- **(V) PROVED.** There is a neighbourhood N_P of e_k such that C_p ⪯_k X_P for every interior p ∈ N_P.
  - *Reason (X2.2(c), first half).* X_P is a strict improvement of B^k at both majority worlds j, l. So the closed sections {p : C_p ⪯_j X_P} and {p : C_p ⪯_l X_P} miss a neighbourhood of e_k, and competitiveness leaves world k. No composition is used.
  - *The record.* rec(C_p, X_P) corrects **all** of E_k(C_p), the problems where C_p is not k-correct, and silences P.
  - *Not local.* E_k(C_p) has infinite Haar mass.
- **(♠) PROVED, from (V), weak (G) and (TC).** For every measurable F ⊆ E_k(C_p) and p ∈ N_P, put Y_F := C_p[F → k-correct, P → S]. Then Y_F ≺_k C_p is impossible.
  - *Reason.* X_P ⪯_k Y_F by weak (G), because Y_F is X_P with C_p's errors restored on E_k(C_p) ∖ F. So Y_F ≺_k C_p would make C_p ⪯ X_P ⪯ Y_F ≺ C_p a (TC) violation.
  - *Comparison with X2.2(c).* X2.2(c) asserted the stronger C_p ⪯_k Y_F, using transitivity.

**Lemma N (the forced records are (TC)-consistent among themselves; PROVED).**
- *Statement.* No (TC) violation at world k can be built from records of type (V) (at any p, P), guidance links and strict-guidance refusals alone.
- *Two (V)-records never compose.*
  - The first ends k-correct on E_k(C_p). The second starts with C_q's k-incorrect advice on E_k(C_q).
  - E_k(C_p) ∩ E_k(C_q) ∖ P is non-null: both contain the far A-region of M_k. So the middles never match.
- *A (V)-record never closes a violation with guidance alone.* A violation X ⪯ Y ⪯ Z ≺ X whose refusal X ⋠ Z comes from strict guidance needs Z to be a pointwise k-improvement of X. On the far piece P of the (V)-record, its old side is B (k-rank 0) and its new side is S (k-rank 1).
  - *(V) first, guidance second.* X has rank 0 on P. Y has rank 1 there, and Z is weakly k-worse than Y, so Z has rank ≥ 1 > 0 on P. Z does not improve X.
  - *Guidance first, (V) second.* Y has rank 0 on P, and X is weakly k-better than Y, so X has rank 0 there. Z has rank 1 on P. Z does not improve X.
  - Links that are all guidance compose pointwise, so they never violate (TC). ∎

So under (TC), X2.9's mechanism cannot be rebuilt from what (S) forces at the vertex, and an extra ingredient is needed. Completeness is enough.

**Theorem L (X2.2(c) and X2.9 under (TC) for locally complete worlds; PROVED; geometry CHECKED, `e3_far_swap.out`).**
- *Hypotheses.*
  - At world k: (G) both halves, (IB), (TC) and LI.
  - At worlds j, l: the strict half of (G).
  - Competitiveness at interior indices near e_k.
  - Closed sections at e_k for worlds j, l and the rivals X_P.
- *Conclusion.*
  - **(a)** If world k is complete on the pair {C_p, Y_F}, then C_p ⪯_k Y_F. This is X2.2(c)'s conclusion, without transitivity. LI is not needed for (a).
  - **(b)** For every ε ∈ (0,1) there are explicit local boxes P, Π_1, Π_2, E_1 in M_k, and t_0, such that the following holds for all t_1, t_2 ≥ t_0. Put q = ν(1, 1/t_2, t_1), in coordinates (k, j, l). Then world k is **incomparable** on at least one of two local pairs: {T1, Y_1} and {C_q, Y_2}. By LI, the second is equivalent to a pair out of T1.
- *Corollary.* No LI world that is complete on local records can satisfy the hypotheses. This excludes X2.7's balanced Haar-lexicographic rules, which are complete and transitive, and every total, additive or lexicographic local rule. X12 referee R1 (that X2.7's rules fail at a vertex) therefore also holds under (TC).

*Proof.*
- **(a)** By completeness, C_p ⪯_k Y_F or Y_F ⪯_k C_p. In the second case (♠) forbids strictness, so C_p ⪯_k Y_F.
- **(b) The boxes.** Work in the M_k chart, h = (−1, X, Y), with X = e^x and Y = e^y.
  - P = [1−η, 1+η]², with η = (A_−1)/(8A_).
  - Π_1 = ν(t_1,1,1)∘P, a box around (1/t_1, 1/t_1).
  - Π_2 = S_q^{-1}(ν(t_2,1,1)∘P), a box around (1, 1/(t_1t_2)).
  - E_1 = [R−η, R+η]², with R = 2 + ε/c.
  - t_0 = 4 + 4ε/c + 1/η. These ε-dependent choices are X12's repair of X2.9.
- **(b) Where T1 and C_q stand on the boxes.** T1's B-region is a down-set and its A-region an up-set, so corner checks certify whole boxes. They give:
  - T1 = B on Π_1, S on Π_2, A on E_1;
  - C_q = S on Π_1, B on Π_2.
- **(b) The two (♠) instances.**
  - Π_1 is a far piece of T1 in the sense of (V), with p = ν(t_1,1,1).
  - Π_2 is a far piece of C_q: C_q at Π_2 is T1 at ν(t_2,1,1)∘P.
  - Let Y_1 := T1[Π_2 ∪ E_1 → B, Π_1 → S] and Y_2 := C_q[Π_1 → B, Π_2 → S].
  - (♠) applies to both: at T1, after LI transport from ν(t_1,1,1); at C_q, after LI transport from ν(t_2,1,1). All records involved are local.
- **(b) The violation.** Suppose both pairs are comparable. By (a), T1 ⪯_k Y_1 and C_q ⪯_k Y_2.
  - Y_1 agrees with C_q on Π_1 ∪ Π_2 (S, B). So by (IB), rec(Y_1, Z) = rec(C_q, Y_2), where Z := Y_1[Π_1 → B, Π_2 → S] = T1[E_1 → B].
  - Hence Y_1 ⪯_k Z. Z is a strict world-k improvement of T1, since world k is the minority world on M_k.
  - So T1 ⪯ Y_1 ⪯ Z ≺ T1 violates (TC). ∎

*Check.* 90 exact configurations: ε ∈ {10⁻⁴, 10⁻³, 10⁻², 0.1, 0.3, 0.5, 5/8, 0.7, 0.9, 0.999}, with t_i ∈ {t_0, 10t_0, …}. All piece positions, disjointness, the far-piece identity and composability are verified.

**Status of local invariance.**
- *Free.* Every local obligation reduces to T1 (X2.7a, imported). Local consistency holds (X2.7, under transitivity, hence under (TC)).
- *Forced.* Near e_k, the forced vertex records are non-local and pairwise non-composable (Lemma N). By Theorem L, each world must be incomparable on local crossed far-swaps.
- *What incomparability implies.* When world k refuses rec(T1, Y_1), competitiveness of T1 must be met at j or l. There Y_1 is mixed: Π_1 B→S helps j and l, while Π_2 S→B and E_1 A→B hurt them. Nothing found so far makes this impossible.
- **OPEN.** Does a system with LI at every world satisfy all of (R0), (S), (LA) and direct (C)? CONJECTURE: none. Neither direction has a proof.

**Patch equivariance (remark).** Requiring C_p ⪯_i X iff T1 ⪯_i X∘S_p^{-1} only for p in a compact K ⊂ int Δ escapes Theorem E, because the orbits it uses never reach ∂Δ. It buys only the reduction of K's own obligations to T1. Requiring invariance of the relation under all S in a neighbourhood of the identity is not weaker than full invariance: such a neighbourhood generates G.

---

## 6. What this means for constructions (brief item 3)

1. **No invariant system exists (Theorem E).** By Corollary E2, none exists for any non-scalar subgroup either. The per-sign-region translation picture is still the right geometry, but it describes the selection, not the rankings.
2. **The symmetry must be broken on records of infinite Haar mass, already on one rival.**
   - In every system with (S) for the rescaled family, the sets A_i(Λ) = {p : C_p ⪯_i Λ} are closed and cover Δ in the KKM sense.
   - By Lemma 3.1, A_i(Λ) contains no vertex other than e_i and does not meet the open edge opposite e_i.
   - KKM gives a point p* in all three, i.e. a selected dominator of Λ.
   - Under any symmetry the A_i(Λ) ∩ int Δ would be unions of orbits, which is impossible. This is the precise "price of invariance" behind brief observation 3.
3. **The rescaled family escapes Theorem J and J1 (§4.2).** For this family, closed rules are not excluded by J1. This matters independently of equivariance: rules with closed accepted-record sets (AF-type, Φ^κ-eligibility, audit's §6 rule) were set aside for the homothetic family because of J1. For the rescaled family they need a fresh screen, and the screen must include Λ and the split-cell rival of AUDIT_rescaling_construction §5.
4. **Suggested next questions.**
   - (i) Local invariance under (TC): find a local rule that is incomparable on crossed far-swaps and passes the X2.7a obligations at T1. Alternatively, prove that incomparability there breaks T1's competitiveness at the majority worlds. This is the one open part of Task A.
   - (ii) A closed (non-invariant) rule for the rescaled family, screened on Λ, on the class-constant killers of `e1`, and on the split-cell rival.

---

## 7. Scripts (`PP12_py/`)

| script → output | content | label |
|---|---|---|
| `pp12lib.py` | exact T1 and M_p geometry, classes, ranks | library |
| `e0_orbit.py` → `e0_orbit.out` | Observation 1: D_{M_p} = T1∘S_p (interior, edges, vertices), equivariance, edge strips, vertex models, convergence to the boundary | CHECKED |
| `e1_invariant_rivals.py` → `e1_invariant_rivals.out` | boundary advice sets; all 256 class-constant rivals under full and one-parameter invariance (Theorem E, E2); two-world D_Δ (E3) | CHECKED |
| `e2_J0_rescaled.py` → `e2_J0_rescaled.out` | Proposition P (P1), (P2); no J0 instance for the rescaled family; homothetic sanity | CHECKED (P1, P2); NUMERICS (search) |
| `e3_far_swap.py` → `e3_far_swap.out` | Theorem L geometry, exact boxes, 10 values of ε × 9 (t_1, t_2) pairs | CHECKED |
| `e4_haar_mass.py` → `e4_haar_mass.out` | Lemma D: linear growth of the disagreement area between translates | NUMERICS |
