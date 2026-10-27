# PP14. The cut skeleton on the rescaled contamination family: Theorem J never applies, and the skeleton is empty

21 October 2026. Brief 42, Task C. One reader (me); not refereed.

**Labels**
- **PROVED**: the full argument is given here.
- **CHECKED**: an exact finite computation in rational arithmetic (`fractions.Fraction`), with SAT verdicts from an exact clause encoding (pysat, CaDiCaL 1.9).
- **NUMERICS**, **CONJECTURE**, **OPEN**: as stated.

**Scripts** are in `PP14_py/`. Run each as `python3 -I -B <script>` inside that folder; outputs are in `*.out`.

**No assumption is added.** Every clause in every SAT instance is an instance of an adopted axiom: (G) both halves, face obligations (the defence clause of (S) transported by (IB)), undominatedness, (TC).

---

## 0. Verdicts

**1. Theorem J's hypotheses fail for this family, at T1, at every interior C_p, on every edge, for every ε (PROVED; CHECKED).**
- Theorem J needs a selected edge model C_r (r in the open edge Δ_ij) that is more A-ward than a selected C_a on non-null parts of **both** M_i and M_j. Call this a *J-pattern*.
- **Nesting criterion (Lemma 2.2).** Project from the third vertex e_k onto the edge, using the ratio x_j/x_i. A J-pattern exists at (a, r) only if the projections of K_r and K_a are **strictly nested**, in one direction or the other.
- **Translation lemma (Lemma 2.3).** In the rescaled family, x ↦ p∘x/(p·x) multiplies x_j/x_i by p_j/p_i. So every member's projection is a multiplicative translate of the projection of M:
  [ρ_p·(1−ε)/(1+2ε), ρ_p·(1+2ε)/(1−ε)], where ρ_p = p_j/p_i.
  The edge models included: they are imprecise segments of exactly the same log-width. Translates of one interval are never strictly nested.
- So there is **no J-pattern anywhere** (Theorem 2.4), including on boundary indices and in the mirror (S versus B) form.
- *Contrast (CHECKED).* T1 is also the centre of the homothetic family K_p = p + 3ε min p (Δ − u). There the edge models are precise points. They sit strictly inside the window at every interior index and on every edge (129/129 index–edge pairs), and the same rivals of T1 carry J-patterns.

**2. Stronger: no record into a selected model carries a forced exclusive choice of worlds (Theorem N, PROVED; CHECKED).**
- For every record d = rec(X, C_a) into a selected model of the rescaled family, the set of worlds at which guidance accepts d meets every face that the anchor set of d meets, whenever that set is nonempty.
- Hence (G), every face obligation, undominatedness and direct (C) are satisfied on d by "accept exactly where guidance accepts".
- So no record carries a forced "exactly one of i, j" (the content of Theorem J (1)) or a forced "exactly two" (Sperner-type) constraint.

**3. What the axioms force on the pattern families (PROVED; CHECKED).** Only a residual **order** constraint is left (Proposition 3.2).
- On every Theorem-J-type family, the reverse acceptance sets L_i and L_j at the two edge worlds are disjoint.
- They do not "invert": no member of L_j lies above a member of L_i in world i's order, with a member between them.
- Their ends are fixed by guidance.
- They need **not** cover the family. A gap, where the reverse record is accepted only at the third world, is allowed, and it can be the whole open family. Then L_i and L_j are closed.
- So there is no cut curve, no forced defending world, no forced jump, and no pinned defence of J4 type.

**4. At T1 several edges are carried at once, but harmlessly (PROVED; CHECKED).**
- A two-class majority pattern on M_i ∪ M_j is anchored at e_k, on Δ_ik and on Δ_jk, and never on its own edge Δ_ij. Every one of these obligations contains k, and world k accepts by guidance.
- A record anchored on all three edges lies, up to null sets, inside one class, and guidance decides it completely.

**5. Near the vertices (PROVED).**
- *Axioms only.* (G) with KKM pins the KKM dominator of a regular rival only when the rival is a vertex model (Proposition 3.5). So the axioms alone force no edge threshold model to be selected.
- *Conditional on weak gates.* Suppose a construction uses PP2-type weak gates. Then KKM forces its world-i keys, on the records of edge ij, to be exactly the log-odds translation keys L − log t_ij and −L − log t_ij, up to an increasing reparametrisation (Proposition 3.6).
- PP2 Theorem 6 then forces those keys to be chosen from the record on the vertex classes: t_ij for edge-ij records and t_ik for edge-ik records.

**6. Outcome: consistent. The cut skeleton is empty.**
- The minimal discontinuity forced by the Theorem-J mechanism on this family is **none**.
- J1 does not apply. Accepted-record sets that are closed in the record metric are not excluded by any refereed result for this family. Whether a ρ-closed system exists is **OPEN**.
- The freedom left is listed in §4.2.

**7. Corrections to the brief and the memo.**
- **Brief Observation 4 is false for this family.**
  - J1, as repaired by the referee (R1), needs strict nesting. The rescaled family never has it.
  - Audit's closed construction does not fail "as J1 predicts". It fails competitiveness of T1 against a single-class split-cell rival, which involves no edge anchoring at all.
- **DESIGN_MEMO §8.10.** "For imprecise interior targets such as T1, accepted comparisons must jump" should read "for selections with nested edge windows, such as the homothetic family". T1 itself is not the cause. The same T1 sits in a family (this one) where nothing jumps.
- **REFEREE_PP11 S2.** "At least two of R_1, R_2, R_3 are not ρ-closed" holds for the homothetic family only.

**Scope.**
- Nothing here uses contamination beyond the fact that M ⊂ int Δ is compact and convex. Every result holds for every diagonal-orbit family {p∘m/(p·m) : m ∈ M}.
- Theorem N holds for every selection whose edge projections are never strictly nested.
- No result here says that T1 is coverable.

---

## 1. Setting

- **Worlds and problems.** Worlds 1, 2, 3; problems are lines of the simplex (g ∈ R³ modulo sign).
- **Classes.** M_w is the class whose minority world is w.
- **Advice.** A is the majority advice, B the minority advice, S silence.
- **Ranks.** At a majority world: A 0, S 1, B 2. At the minority world: 2, 1, 0.
- **Order of advice.** "More A-ward" uses the order A > S > B. On M_w, being more A-ward is better for the two majority worlds and worse for w.
- **The family.**
  - T1 = D_M, with M = c1 + εΔ and c = (1−ε)/3.
  - Interior p: C_p = D_{K_p}, with K_p = {p∘m/(p·m) : m ∈ M}. This is the triangle with vertices p∘v_l/(p·v_l).
  - Boundary p: the map p ↦ K_p is Hausdorff-continuous on the closed simplex, because p·m > 0 on M. So the limits are:
    - on the open edge Δ_ij, a segment of Δ_ij;
    - at a vertex, the vertex itself.
- **Records and anchors.**
  - d = rec(X, Y) ∈ R_w means X ⪯_w Y.
  - The anchor set A(d) is the set of indices q with C_q equal to X on D(d). If A(d) meets a face I, then d must be accepted at some world of I.
  - Guid⁺(d) is the set of worlds at which weak (G) accepts d. Guid⁻(d) is the set at which strict (G) refuses it.
- **A remark used throughout.** On D(d), two different regular advices have different ranks at every world. So for a nontrivial regular record each world is either guidance-accepted (strictly, on all of D), guidance-refused, or free.
- **Coordinates for an edge.** For the edge Δ_ij with third vertex e_k, write ρ(x) = x_j/x_i, and t(g) for the ratio at which a line g of M_i ∪ M_j crosses [e_i, e_j]. Then t(g) = −g_i/g_j.
- **Projections.** For a set K, [lo_K, hi_K] is the range of ρ over K.

---

## 2. Theorem J's hypotheses on the rescaled family (Task C.1)

**Lemma 2.1 (perspective; PROVED).** Let ℓ be a line of M_i crossing [e_i,e_j] at ratio t. Then:
- its closed e_i-side lies in {ρ ≤ t};
- for a line of M_j, the closed e_j-side lies in {ρ ≥ t}.

*Proof.* The e_i-side of an M_i line is the triangle (e_i, z, y), with z on [e_i,e_j] and y on [e_i,e_k], so that y_j = 0. For x = αe_i + βz + γy we get x_j = βz_j and x_i ≥ βz_i, so ρ(x) ≤ z_j/z_i = t. The M_j case is symmetric. ∎

**Lemma 2.2 (nesting criterion; PROVED).** Let K_r ⊂ relint Δ_ij be a segment, and let K_a be compact and convex.
- **(a)** If C_r is more A-ward than C_a on a non-null set of M_i lines, then lo_r > lo_a or hi_r > hi_a.
- **(b)** If the same holds on a non-null set of M_j lines, then hi_r < hi_a or lo_r < lo_a.
- **(c) Converse.** If K_a ⊂ int Δ, then:
  - (a) holds as soon as lo_r > lo_a, or hi_r > max(hi_a, lo_r);
  - (b) holds as soon as hi_r < hi_a, or lo_r < min(lo_a, hi_r).
- **Consequence.** A J-pattern (both (a) and (b)) exists iff the two projections are strictly nested, in one direction or the other.

*Proof.*
- *Advice of the edge model.* For an M_i line crossing at t: C_r is A iff lo_r > t, S iff lo_r < t < hi_r, and B iff hi_r < t.
- *Advice of C_a.* By Lemma 2.1:
  - C_a ≠ A means K_a meets the closed e_i-side, which forces lo_a ≤ t;
  - C_a = B means K_a lies inside the closed e_i-side, which forces hi_a ≤ t.
- *The A-ward cases.* These are (A, S or B), which gives lo_r > t ≥ lo_a, and (S, B), which gives hi_r > t ≥ hi_a. That proves (a); (b) is symmetric.
- *The converse (c).*
  1. Take z on [e_i,e_j] at a ratio t in (lo_a, lo_r).
  2. Take the M_i line through z and a point of [e_i,e_k] close enough to e_k. Its e_i-side is then close to {ρ < t}, so it contains the vertex of K_a at which ρ is smallest. That gives C_a ≠ A while C_r = A.
  3. For the (S, B) case use t in (max(hi_a, lo_r), hi_r): then K_a lies inside the e_i-side and the line crosses K_r.
  4. All of these conditions are open, so they hold on a non-null cone of lines. ∎

**Lemma 2.3 (translation; PROVED).** If p_i, p_j > 0, then [lo_{K_p}, hi_{K_p}] = ρ_p·[lo_M, hi_M], with ρ_p = p_j/p_i.
- For contamination, [lo_M, hi_M] = [(1−ε)/(1+2ε), (1+2ε)/(1−ε)]. At ε = 3/10 this is [7/16, 16/7].

*Proof.* ρ(p∘m/(p·m)) = (p_j m_j)/(p_i m_i) = ρ_p ρ(m). ∎

**Theorem 2.4 (no J-pattern; PROVED).** For every a ∈ Δ (interior or boundary), every r in an open edge Δ_ij, and every ε ∈ (0,1): the set where C_r is more A-ward than C_a is null in M_i or null in M_j. More precisely:
- if ρ_r > ρ_a, it lies in M_i;
- if ρ_r < ρ_a, it lies in M_j;
- if ρ_r = ρ_a, it is null in both.

*Proof.*
- *a with a_i, a_j > 0.* By Lemma 2.3, lo_r > lo_a ⇔ hi_r > hi_a ⇔ ρ_r > ρ_a. Apply Lemma 2.2 (a) and (b).
- *a_j = 0.* K_a ⊂ {x_j = 0}, so ρ ≡ 0 and (b) is impossible. Directly: K_a lies on the majority side of every M_j line, so C_a = A on all of M_j.
- *a_i = 0.* Symmetric.
- *a = e_k.* C_{e_k} = A on M_i ∪ M_j, so nothing is more A-ward than it there. ∎

**What this says about Theorem J.** Referee-repaired hypothesis (ii) of Theorem J requires a selected C_r, r ∈ relint Δ_ij, saying A on non-null G_i ⊂ M_i and G_j ⊂ M_j on which C_a is silent. That is a J-pattern, so it fails everywhere. The same holds for the mirror form: C_r silent where C_a says B, a pattern that Theorem J (1) would also handle verbatim.

**Explicit geometry (Task C.1).** Fix the edge Δ_ij and an interior a.
- **The one-class pieces.**
  - E_i(a, r) := {g ∈ M_i : C_r is more A-ward than C_a} is non-null iff ρ_r > ρ_a. Up to null sets it is
    {lo_a ≤ t < lo_r, with the e_i-side meeting K_a} ∪ {hi_a ≤ t < hi_r, with K_a inside the e_i-side}.
  - E_j(a, r) is non-null iff ρ_r < ρ_a, with the mirror description.
  - At the "projection" r* of a (ρ_{r*} = ρ_a), C_{r*} says A on an M_i ∪ M_j line only where C_a already says A.
- **The two-class majority patterns.** G_i ⊂ M_i and G_j ⊂ M_j, non-null, with C_a silent on both. Their reverse record d = A→S on G_i ∪ G_j has anchor faces:
  - {k}, always: D_{e_k} = A on M_i ∪ M_j;
  - Δ_ik, whenever the crossings of G_i with [e_i,e_k] are bounded, using an s near e_k (C_s is A on all of M_j automatically);
  - Δ_jk, likewise for G_j;
  - possibly the interior;
  - **never Δ_ij.**

  Every one of these faces contains k, and world k accepts d by guidance. This is the precise sense in which "the pattern is anchored on the wrong edges".
- **The forward record** e = S→A on the same G is anchored on Δ_ij. The anchors are the edge models silent on all of G: those whose segment straddles every crossing. These exist when the ratio-spread of the crossings is below ((1+2ε)/(1−ε))². This is the forward obligation e ∈ R_i ∪ R_j; world k refuses e by guidance.

**CHECKED.**

| check | script | result |
|---|---|---|
| Lemma 2.3: exact projection of every member (43 interior indices, including (.98,.01,.01) and (.01,.01,.98), plus 45 edge points, × 3 edges) | `t1` (a) | 174/174 exact, for each of ε = 3/10, 1/10, 1/100 |
| strictly nested (interior a, edge r) pairs, rescaled | `t1` (a) | 0/1935, for each ε |
| the same, homothetic | `t1` (a) | 480 / 92 / 22 of 1935; the window is nonempty at every interior index and edge (129/129) |
| Lemma 2.2 (a), (b) on random exact lines; a interior, on Δ_ij, on Δ_ik/Δ_jk, or at a vertex | `t1` (b) | rescaled: 0 pairs with witnesses in both classes (500 pairs), 0 violations of the necessary condition; homothetic: both classes for 79/156 and 48/156 pairs |
| Lemma 2.2 (c), explicit exact witness lines | `t1` (c) | rescaled 600/600 at each ε, and 0 witnesses where none is predicted; homothetic all predicted (A-type) witnesses found |

---

## 3. What the axioms force (Task C.2)

### 3.1 No forced exclusivity

**Theorem N (PROVED).** Let d = rec(X, C_a) with C_a selected (any a ∈ Δ), X regular on D(d), and D(d) non-null. Then:
- **(i)** Guid⁺(d) ≠ {1,2,3};
- **(ii)** if Guid⁺(d) ≠ ∅, it meets every face met by A(d);
- **(iii)** the clauses of d alone, namely (G), every face obligation, undominatedness of C_a and direct (C), have a solution W(d) with |W(d)| ≤ 2. If Guid⁺(d) ≠ ∅, that solution is W(d) = Guid⁺(d). If Guid⁺(d) = ∅, a one-world solution exists;
- **(iv)** for no pair {i,j} of guidance-free worlds does every solution of (iii) contain exactly one of i, j. A solution size of 2 is forced only when |Guid⁺(d)| = 2, and then W(d) is fixed entirely by guidance.

*Proof.*
- **(i)** On M_w, weight the minority world 2 and each majority world 1. The weighted rank sum is 4 for every regular advice, so no change can be weakly better at all three worlds.
- **(ii)** Go through the faces.
  - *Vertex face {i}.* Then X = D_{e_i} on D. That model is world-i-optimal, so i ∈ Guid⁺.
  - *Interior face.* Any world meets it.
  - *Edge face containing a world of Guid⁺.* Nothing to show.
  - *Edge face not containing a world of Guid⁺.* If |Guid⁺| = 2, this cannot happen. So Guid⁺ = {k} and the face is Δ_ij.
    1. Then X = C_r on D for some r ∈ relint Δ_ij, and X is better than C_a at k on all of D.
    2. On M_k, C_r = A, which is worst for k. So D misses M_k.
    3. On M_i ∪ M_j, X is more A-ward than C_a. By Theorem 2.4, D then lies a.e. in one class, say M_i.
    4. There a more A-ward X is better for the majority world j. So j ∈ Guid⁺, a contradiction.
- **(iii)** If Guid⁺ ≠ ∅, take W = Guid⁺. By (ii) it meets every face, and by (i) it is not all three worlds.
  - It avoids Guid⁻ trivially.
  - Undominatedness and direct (C) hold, because rev(d) is refused at the worlds of Guid⁺. So there is no all-world tie, and d is not accepted at all three worlds.

  If Guid⁺ = ∅, the faces are edges or the interior (vertex faces lie in Guid⁺). Four facts settle this case.
  - *No edge face lies inside Guid⁻.* A record out of C_r, r ∈ Δ_ij, refused at both i and j would need the new side to be better at i and at j on D. That is impossible on M_k, where C_r = A is best for both, and on M_i and M_j, where ranks at i and j are opposite.
  - *The anchor set does not meet all three open edges.* If it did, the old side would be A on all of D: C_t = A on M_i for t ∈ Δ_jk, and so on. Theorem 2.4 on each edge would then confine D to one class, and D would be guided.
  - *Two edge faces Δ_ij, Δ_ik have their common world i outside Guid⁻.* If the new side were better at i on all of D, then D would miss M_j (C_s = A there for s ∈ Δ_ik, which is best for i) and M_k (C_r = A there). So D ⊂ M_i, where the old side is more A-ward. Then j, k ∈ Guid⁺, contradicting Guid⁺ = ∅.
  - *Guid⁻ ≠ {1,2,3}.* Otherwise rev(d) would be guidance-accepted at every world, contradicting (i).

  So one world outside Guid⁻ hits every face. It is not all three worlds, so undominatedness holds; and there is no all-world tie, so direct (C) holds.
- **(iv)** Let i, j be guidance-free.
  - If Guid⁺ = {k}, the solution {k} contains neither i nor j.
  - If Guid⁺ = ∅, then {i, j} is a solution. It avoids Guid⁻, it meets every edge and the interior, there are no vertex faces, and it is not all three worlds.
  - If |Guid⁺| = 2, there is at most one guidance-free world, so there is no such pair.

  One-world solutions exist whenever |Guid⁺| ≤ 1, by (iii). ∎

*Remark.* For the homothetic family (ii) fails, and the failures are exactly Theorem J's records (`t2`, below). So for any selection, Theorem N holds **iff** there is no strict nesting (Lemma 2.2).

*CHECKED (`t2_records.py`).*
- Exact anchor faces, including exact interior anchor sets by vertical decomposition, and exact guidance.
- Records come from random selected pairs (q, a), both interior and boundary, on random line sets D.
- Rescaled family, 1,470 records: (ii) holds 1,470/1,470, (iii) is satisfiable 1,470/1,470, and there are 0 forced exclusivities. In a targeted search (q on the edge near a's projection, D inside the A-ward set), 0 of 238 (q, a) pairs have A-ward lines in both classes.
- Homothetic family, same search: (ii) fails on 360 of 702 and 78 of 558 targeted records, every one a forced "exactly one". Example at a = (192, 632, 525)/1349, ε = 3/10: an edge-Δ₂₃ J-record with guidance at world 1, exclusive on {2,3}.

### 3.2 The residual order on pattern families: no cut curve

Take any Theorem-J-type family X_λ = C_a + A on G_i(λ) ∪ G_j(λ) (λ ∈ [0,1]; G_i shrinking, G_j growing, C_a silent on both, a interior). Let L_w = {λ : d(λ) ∈ R_w} and F_w = {λ : e(λ) ∈ R_w}.

**Proposition 3.2 (PROVED: PP11 Theorem J (2), steps 1–4, without the edge-anchor step).**
- **(a)** L_i ∩ L_j = ∅, by undominatedness of C_a and world-k guidance.
- **(b)** 0 ∈ L_j ∖ L_i and 1 ∈ L_i ∖ L_j, by guidance.
- **(c)** There are no μ < ν < μ′ with μ ∈ L_i and μ′ ∈ L_j. This uses Lemma 2.2 of PP11, the (TC) cut lemma, together with the forward obligation e(ν) ∈ R_i ∪ R_j.
- **(d)** Nothing forces L_i ∪ L_j = [0,1].
- Hence sup L_j ≤ inf L_i. Beyond the outermost members of L_i and L_j, PP11's strict verdicts hold. In the gap between them, e(λ) ∈ F_i ∪ F_j is the only constraint.
- **In particular, L_j = {0} and L_i = {1}, both closed, are allowed.**
- *Two parameters.* The same holds along every path that is monotone in world i's order. So L_i and L_j are *separated*: no point of L_j lies above a point of L_i with a member between. They are not forced to be complementary up-sets. The "cut curve" of PP11 Remark 3.5 becomes an optional separating band.

*Proof of (d).* (a)–(c) are exactly PP11's arguments. Coverage came only from the {i,j}-face obligation of d(λ), and by Theorem 2.4 that obligation does not exist here. The rest is CHECKED below.

*CHECKED (`t3_skeleton.py`).*
- Exact anchors, (G), every face obligation, FWD, UND and (TC) on all triples.
- Settings: T1 at ε = 3/10 and 1/10 on edge Δ₁₂, and a = (1/2, 3/10, 1/5) at ε = 3/10 on edges Δ₂₃ and Δ₁₃.

| query (1-parameter, n = 4) | rescaled | homothetic (same T1, same rivals) |
|---|---|---|
| reverse records of interior members anchored on the edge | 0 of 3, in every case (faces {3},{13},{23},{123} at T1) | 3 of 3 |
| all interior members refused at both edge worlds (L closed) | SAT, all 4 cases | UNSAT, all 4 cases |
| every cut position c = 1..4 | SAT | SAT |
| inversion with a member between | UNSAT | UNSAT |
| adjacent inversion | SAT | SAT |
| backbone on edge-world verdicts, beyond guidance | 0 | 0 |

| query (2-parameter, n = 3, 16 models) | rescaled | homothetic |
|---|---|---|
| two-class members anchored on the edge | 0/9, all 3 cases | 9/9 |
| all two-class members refused at both edge worlds | SAT | UNSAT |
| inversions with a member between, along world i's order | 0/15 SAT | 0/15 SAT |
| backbone on reverse edge-world verdicts | 0 | 0 |

Adjacent inversions are allowed in finite families for the same reason PP11 gives (no intermediate member). The homothetic module omits interior anchors, which makes it a relaxation, so its UNSATs are genuine.

### 3.3 Interaction of edges at T1

At T1 a single rival can be anchored on two or three edges at once. Theorem N describes every case.
- **Two-class majority pattern on M_i ∪ M_j.**
  - Anchored on Δ_ik, Δ_jk and at e_k (§2); all obligations are met by world k's guidance.
  - The only cross-world constraint is "not both i and j" (undominatedness).
  - There is no lower bound at i or j. So no Sperner labelling is forced, and PP11 §5.4's "three-class families anchored on all three edges" has nothing to label.
- **Records anchored on all three open edges.**
  - The old side is A on all of D: C_t = A on M_i for t ∈ Δ_jk, and so on.
  - Theorem 2.4 on each edge confines D to one class, say M_i.
  - Guidance is then {j,k} accepted and i refused. Nothing is free. (`t3` (d₀ rows): faces {2},{3},{12},{13},{23},{123}, guidance −++.)
- **Records into T1 from interior members, with no guidance.** Obligation: some world. Exclusion: not all three. Any one- or two-world choice works.

So the cut curves of different edges have nothing to interact with. There are none.

### 3.4 Fixed-rival limits

These hold for any selection with closed sections, and so here too:
- PP11 Lemma 2.3: pinning, (P1) strict-guidance refusals and (P2) two-world pinning.
- The (TC) refusals of returns that (P2) entails.

They are local in p and are not cuts. J4's pinned single-world defences need a forced singleton F(C_a, X_λ). By Proposition 3.2 that occurs only outside the gap, so only if a construction chooses nonempty L-zones.

Closed sections at the edge add nothing forced. Consider a fixed X and p → r ∈ Δ_ij. Interior acceptances at world k carry over to C_r ⪯_k X, which is a forward record out of C_r and carries no exclusion.

### 3.5 Near the vertices

**Proposition 3.5 (axioms only; PROVED).** Let X be regular and not a vertex model. Then some selected C_q is guidance-refused against X at no world. So (G) and KKM alone never force the KKM dominator to equal X, and in particular never force an edge threshold model to be selected.

*Proof.* "C_q ⪯_w X is refused by (G)" means that X is pointwise better than C_q at w.
- *Case 1: X ≠ A on non-null parts of two classes M_j and M_k.* Take q = e_i.
  - D_{e_i} is world-i-optimal.
  - At world j, X is pointwise better than D_{e_i} only if X = A a.e. on M_k, the one class where D_{e_i} is j-best. Likewise at world k.
- *Case 2: otherwise X = A a.e. on two classes, say M_i and M_j.* Since X ≠ D_{e_k}, it is not B on a non-null set N ⊂ M_k. Take q interior and close to e_k.
  - C_q ≠ A on non-null parts of M_i and M_j, so C_q is better there at i and at j.
  - C_q → D_{e_k} in measure, so C_q = B on a non-null part of N, where it is better at k. ∎

**Proposition 3.6 (conditional; PROVED from PP2 Lemmas 6.1–6.2, with `t4` CHECKED).** Suppose world i accepts non-guidance comparisons C ⪯_i X, with X equal to A on M_k, only through the weak gate of a key κ on the steps of M_i ∪ M_j. Then:
1. KKM forces each threshold model X_c to be selected (PP2 Lemma 6.1).
2. X_c is A on M_k, so X_c = C_r for some r in the closed edge Δ_ij.
3. In the rescaled family, on M_i ∪ M_j,
   U_i(C_r) = {(g,1) : t(g) < hi_r} ∪ {(g,2) : t(g) < lo_r}, with hi_r/lo_r = ((1+2ε)/(1−ε))²,
   and C_r = A on M_k.
4. So, up to an increasing reparametrisation φ:
   κ(g,1) = φ(L − log t_ij(g)) and κ(g,2) = φ(−L − log t_ij(g)), with L = log((1+2ε)/(1−ε)).

These are exactly gate2d's keys l⁻¹ and u⁻¹, here translations in log-odds, as Brief Observation 2 anticipates. By PP2 Theorem 6 (R1), world i must use the t_ik-version on edge-ik records. Its priority on M_i is therefore record-chosen (PP2 (E1)).

*CHECKED (`t4`).* 18,000/18,000 exact checks of the threshold description, including A on M_k, at three values of ε.

---

## 4. Outcome (Task C.3)

### 4.1 Consistent: the skeleton is empty

There are no forced cuts on this family:
- no J-pattern (Theorem 2.4);
- no record-level exclusivity (Theorem N).

So the question "can the forced cuts be made mutually consistent with (TC), undominatedness and closed sections?" is vacuous. What the axioms force on the pattern families, the order of Proposition 3.2 together with guidance and pinning, is consistent on every exact module (`t3`, all SAT). It is consistent in particular with the **gap allocation**: reverse records into selected models are accepted exactly where guidance accepts them. Theorem N shows that this allocation meets every record-level clause.

**The blueprint, i.e. the minimal discontinuity any construction must carry here, is none from this mechanism.** A construction for this family:
- **may** accept reverse records into selected models by guidance only, wherever some world is guidance-decided (this is gate2d's practice);
- **must** accept guidance-free records into selected models at a hitting set of at most two worlds of their anchor faces;
- **must** respect the separation order of Proposition 3.2 if it accepts any non-guidance reverse records on a J-type family;
- **if gated**, must use the translation keys of Proposition 3.6, chosen per edge on the vertex classes.

### 4.2 Freedom remaining (CHECKED on the modules; PROVED at record level)

- On every J-type family, the edge-world verdicts of reverse records are free. The choices are:
  - nothing (the gap);
  - a single cut at any position;
  - two separated zones.

  The only restrictions are disjointness and no far inversion.
- Forward records e(λ) are free in {i}, {j} or {i,j} inside the gap.
- Which world defends at any interior C_p against two-class patterns is never forced.
- Selected-to-selected records without guidance can use any one- or two-world hitting set.

### 4.3 What remains hard, and the nearby targets

- **Where the difficulty moves.** Theorem N removes undominatedness as a source of record-level cross-world conflict. Any obstruction for the rescaled family must therefore come from:
  - forward records, i.e. competitiveness and KKM against rivals;
  - (TC) or closed sections pushing a record into a selected model beyond its guidance set.

  This is where audit's closed construction actually failed: T1 was refused at every world against the split-cell rival. The defence there is one-class and unanchored on any edge.
- **Nearby reachable target (suggested shift).** DESIGN_MEMO §8.10's "next design target" (rules discontinuous across rivals at forced cuts) should be re-scoped. For the rescaled family:
  - ρ-closed rules are back on the table;
  - the binding known constraints are FF2 (no integrable field), PP2 Theorem 6 with Proposition 3.6 (record-chosen translation keys on vertex classes), and the defence clause for unanchored one-class rivals.
- **OPEN.**
  - Is there a ρ-closed system on the rescaled family?
  - Does the gap allocation extend to a full system?
- **CONJECTURE.** On the rescaled family, nothing beyond guidance, Proposition 3.2 and the closed-section pinnings is forced on finite modules built from J-type families and their (IB) closures. Evidence: the `t3` backbones are empty. Closure under splicing was not run.

### 4.4 Scope, as asked

- The emptiness depends on the selection, not on T1.
- It holds for every diagonal-orbit family with M ⊂ int Δ compact and convex, and for every selection without strict edge nesting.
- It fails for the homothetic family through the same T1. So Theorem J and J1 are statements about selections with nested edge windows, not about T1.

---

## 5. Scripts (`PP14_py/`)

| script → output | content | label |
|---|---|---|
| `lib14.py` | exact geometry: classes, advice, ranks, rescaled and homothetic credal sets; exact anchor faces (vertices; edges by exact breakpoints in ρ; interior by vertical decomposition); records; guidance | library |
| `t1_nesting.py` → `t1_nesting.out` | §2: Lemma 2.3 exactly; strict nesting counts, rescaled vs homothetic; Lemma 2.2 brute force; Lemma 2.2 (c) constructive witnesses | CHECKED |
| `t2_records.py` → `t2_records.out` | §3.1: Theorem N on random exact records into selected models, and its failure (Theorem J records) in the homothetic family | CHECKED |
| `t3_skeleton.py` → `t3_skeleton.out` | §3.2: exact 1- and 2-parameter Theorem-J modules; SAT, backbone, gap allocation, cut positions, inversions; rescaled vs homothetic | CHECKED |
| `t4_threshold_keys.py` → `t4_threshold_keys.out` | §3.5: edge models are threshold sets of the log-odds translation key | CHECKED |

Dependencies: Python 3 (`fractions`) and pysat (CaDiCaL 1.9). Nothing from other folders is imported.
