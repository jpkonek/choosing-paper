# PP11. The coupled module, adversarial side: no contradiction, but a forced allocation jump

21 October 2026, Round 41 (adversarial side of brief §4 of `AUDIT_round40_brief.md`).

**Labels**
- **PROVED**: the full argument is given here. One reader (me); not refereed.
- **CHECKED**: an exact finite computation. Exact rational cones, exact cell guidance, exact anchor polygons (PP7/PP8 geometry, imported unmodified from `PP8_py/`). SAT verdicts come from an exact clause encoding, and every satisfying assignment is re-verified by an independent plain-loop checker.
- **NUMERICS**: evidence only.
- **OPEN** / **CONJECTURE**: as stated.

**Scripts** are in `PP11_py/`. Run each as `python3 -I -B <script>` inside that folder; outputs are in `*.out` and `*_run.log`.

**No assumption is added.**
- Every clause of every SAT instance is an instance of an adopted axiom (list in §1.3).
- No proof uses an additive rule, a margin rule or a priority.
- The one additive object in this note, L* (§5.3), is a diagnostic. It is labelled as such and is not proposed as a construction.

---

## 0. Verdicts

**1. No contradiction was obtained on the coupled module.**
- The axioms force nothing beyond guidance on the splice cube alone (CHECKED).
  - The exact finite module is satisfiable in all four settings (near e₁ and near u, ε = 0.3 and 0.1). The cube is C_a, C_q, Y_plus, Y_minus, all splices on the three mixed regions and the return region T, and all (IB) transfers inside the pool.
  - Every free literal can be flipped in some solution: the **backbone is empty**.
- The full module is also satisfiable (CHECKED, four settings), with every solution re-verified. It adds:
  - the Theorem-J splice family (fractional refinement);
  - PP8 F-B's selected model C_p;
  - six selected germs C_{a+tv} with closed-section clauses against every fixed rival.
- The full module's backbone has 312 literals in each setting. At e₁ .3, every one of them is a closed-section consequence: a (P1) refusal, a (P2) pinned defence, or a (TC) refusal of a return into a germ (§5.1).

**2. New theorem (Theorem J, PROVED, axioms only): a forced allocation jump.**
- *The family.* Fix any interior selected C_a and any edge, say Δ₁₂. Let X_λ = C_a with the majority advice A on G₁(λ) ∪ G₂(λ), where:
  - G₁(λ) ⊂ M₁ shrinks and G₂(λ) ⊂ M₂ grows, both inside C_a's silent region;
  - some precise edge model C_r, r ∈ Δ₁₂, gives A on the whole pattern (Lemma J0: such patterns exist at **every** interior index, for every ε and every edge).
- *Exactly one world.* Every record d(λ) = rec(X_λ, C_a) is accepted at **exactly one** of worlds 1, 2.
  - At least one: the edge model's defence clause.
  - Not both: if both, then X_λ ⪯ C_a at all three worlds, strictly at world 3, so C_a is dominated.
- *A cut.* With (TC), the world switches at a single cut λ₀. Every comparison between C_a and the family is then **strict** and fixed:
  - below the cut: C_a ≺₁ X_λ, X_λ ≺₂ C_a, X_λ ≺₃ C_a;
  - above the cut: the same with worlds 1 and 2 exchanged.
- *Exact check.* CHECKED on the exact pump geometry in all four settings, with deletion-minimal cores. These cores are the implication chains the brief asks for (§3.3).

**3. Consequences of Theorem J (PROVED).**
- **(J1) Closedness in the rival argument is inconsistent with the axioms.**
  - For the edge model C_r, the sets {λ : C_r ⪯₁ C_r^[S on G(λ)]} and {λ : C_r ⪯₂ C_r^[S on G(λ)]} partition [0,1]. So they are not both closed.
  - So no system satisfying the axioms has accepted-record sets R_i that are closed in the record metric. This holds even along one path of records, at any interior index.
  - *Rules excluded.*
    - every rule that accepts on record-continuous conditions over closed eligibility sets: AF, additive acceptance, acceptance wherever Φ^κ ≥ 0, and the anchor plan's §6 rule;
    - the anchor plan's §7 target ("closed subsets R_i of the eligible sets");
    - PP8's proposed "closed, record-level rule realising O", if closed is read in the record metric;
    - any global closed-graph condition. The brief excluded this as a replacement for (S); J1 shows it is in fact contradictory.
- **(J2) The forced verdicts are lexicographic.**
  - On each such family, every admissible system behaves like a two-level lexicographic order with a cut.
  - No record-continuous verdict can do this.
  - This is the axiom-level form of audit §2's diagnosis that protected defences are lexicographic.
- **(J3) No fixed-rival section ever sees the jump.**
  - For any fixed model X, at most one selected C_p has rec(C_p, X) in the jump family.
  - So (S)'s closed sections cannot by themselves forbid the jump.
- **(J4) Pinned defences.**
  - For λ ≠ λ₀ there is a neighbourhood N(λ) of a on which C_p ⪯_w X_λ is forced at one world (1 below the cut, 2 above) and refused at the other two.
  - These are compulsory non-guidance comparisons. CHECKED with germs, four settings.

**4. What remains free (precise; the brief's "otherwise" output).**
- The cut λ₀ of each jump family is free: every cut position is realisable on the exact finite family (CHECKED).
- Beyond guidance, the cuts, and the closed-section consequences, the module forces nothing (CHECKED). The closed-section consequences are the (P1) refusals, the (P2) and J4 pinned defences, and the (TC) refusals these entail.
- **An explicit complete assignment L\*** (world 1 minority-first, world 2 majority-first, world 3 minority-first, each lexicographic) satisfies, in all four settings:
  - every guidance, (TC), (IB), face-obligation, undominatedness and direct-(C) clause of the full module;
  - it fails **only** the closed-section clauses (61–183 per setting).
  - L\* realises Theorem J's cut at λ₀ = 1.
- The SAT solutions satisfy the closed-section clauses as well.

**5. Where a contradiction would need more structure.**
- **(a) Closedness of R_i in the rival argument.** This would give a contradiction at once (J1). It is not an axiom, and J1 shows it cannot be added.
- **(b) A disjointness mechanism on fibres.**
  - Theorem J's contradiction-shaped step ("not both worlds") uses undominatedness, which constrains only comparisons with the selected model on the right.
  - Sections constrain comparisons with the selected model on the left.
  - A fibre version would need every fibre record of an edge path to be realised also with a selected model on the right, and to be compulsory at the third world. This is impossible (Remark 3.6).
- So the coupled module, as specified, does not yield an impossibility through the mechanisms the brief lists:
  - KKM dominators;
  - closed-section limits;
  - (TC) with guidance;
  - symmetric mirror reasoning.

  The atomless module **with** section closedness is OPEN: it is the one place finite pools cannot reach.

**6. Scope.**
- Theorem J uses only two facts about the family:
  - some interior selected model has a credal set with nonempty interior;
  - the selected models on the open edge are precise (K_r = {r}), so that C_r says A on the chosen lines.
- It does **not** use:
  - the mirror rivals;
  - the double anchoring of Y_plus;
  - KKM;
  - direct (C);
  - closed sections.
- J3 also uses the triangle shape of K_p.
- No result here says T1 is uncoverable.

---

## 1. Setting

### 1.1 Notation

- **Records and verdicts.**
  - X ⪯_w Y means rec(X, Y) ∈ R_w.
  - For a selected C and a model X, F(C, X) = {w : C ⪯_w X} and R(C, X) = {w : X ⪯_w C}.
- **Classes and ranks.** Classes M₁, M₂, M₃ are as in PP2.
  - On M_w, world w is the minority world. Its ranks are A 2, S 1, B 0.
  - The two majority worlds rank A 0, S 1, B 2.
- **The record metric.** ρ(d, d′) is the mass of the problems on which the (old, new) labels of d and d′ differ.
- **The family.** K_p = p + 3ε min_j p_j (Δ − u), C_p = D_{K_p}.

### 1.2 The module (brief §4, items 1–6)

- **Geometry.** PP8's pump geometry (`cfg_pp5_pump`; PP5's own a, q at e₁ .3):
  - cones S₁ ⊂ M₁, S₂ ⊂ M₂, S₃ ⊂ M₃ on which C_a is silent and C_q says A;
  - a cone T ⊂ M₁ (the lead class) on which both are silent.
- **Splice cube.** C_a with σ_w ∈ {S, A, B} on S_w and τ ∈ {S, B} on T: 54 models.
  - Y_plus = AAA (PP8's doubly anchored rival), Y_minus = BBB, Z = SSS|B (the return), and every independent splice.
- **(IB) transfers.** The pool is closed under splicing its own records into its own models (PP8's closure). This adds the C_q-contexts, for example W = C_q with S on the cones, for which rec(C_q, W) = rec(Y_plus, C_a).
- **Fractional refinement.** The Theorem-J family X_k = C_a + A on (shrunk S₁ by (n−k)/n) ∪ (shrunk S₂ by k/n), for n = 4 or 5.
- **Selected models.**
  - C_a and C_q;
  - PP8 F-B's C_p, at PP8's exact p = a + tv;
  - six germ models C_{a+tv}, with t = 10⁻⁷ and v the six directions ±(1,−1,0), ±(0,1,−1), ±(1,0,−1).
- **Every comparison is a free variable**, including those between selected models.

### 1.3 The encoding (`pp11sat.py`): axioms only

There is one boolean per (directed record, world). So **(IB)** is built in: one variable per record, shared by all its contexts. The clauses are:

| clause | axiom instance |
|---|---|
| (G) | weak worsening at w ⇒ accepted; strict improvement at w ⇒ refused (units) |
| (TC) | for every world and every ordered triple of distinct pool models: X⪯Y, Y⪯Z, Z⪯X ⇒ X⪯Z |
| OBL | for every record d and every face I met by the exact anchor set A(d): accepted at some world of I (competitiveness on supp q, transported by (IB)) |
| UND | every selected pool model is undominated by every pool model |
| DC | no all-world tie of a selected model with a certified-incoherent model |
| CL | closed sections, through germs (below) |

- **CL (closed sections through germs).** For a germ P = C_{p(t)} and every **fixed** model X (one not built from P), the clause is P ⪯_w X ⇒ C_a ⪯_w X.
  - This is sound. Choose a sequence t_n → 0 along which the finitely many verdicts involving C_{p(t_n)} are constant. Closedness of {p : C_p ⪯_w X} then gives the clause.
  - The pool's combinatorial data (cells, guidance, anchor faces, record identities) depend semi-algebraically on t, so they are constant on some interval (0, t₀). That the t used lies in (0, t₀) is not certified (NUMERICS).
  - This matters only for statements that rest on the germ clauses (t5). Every SAT verdict ("no contradiction") is independent of it.
- **What is not encoded.** KKM dominators (their witness need not be in the pool). So no unsound clause is added.
- **How to read the verdicts.** The instance is a **relaxation** of the axioms restricted to the pool. UNSAT would prove inconsistency; SAT says no contradiction exists at that level.
- **Utilities.**
  - `backbone`: the literals forced in every solution, i.e. the compulsory comparisons.
  - `core`: a deletion-minimal unsatisfiable set of labelled axiom instances, i.e. an implication chain.
  - `check`: an independent re-verifier.

---

## 2. Tools (PROVED)

**Lemma 2.1 (pair lemma).**
- *Hypotheses.*
  - d = rec(C_a, Y) with a interior.
  - The reverse is realised out of a selected C_q: C_q agrees with Y on D(d).
  - W := C_q with C_a's advice on D(d), so that rec(W, C_q) = d by (IB).
  - Y and W are incoherent.
- *Conclusion.* F := {w : d ∈ R_w} and R := {w : rev d ∈ R_w} satisfy:
  - F ≠ ∅ and F ≠ {1,2,3};
  - R ∩ supp q ≠ ∅;
  - R ≠ {1,2,3}.

*Proof.*
1. F ≠ ∅ and R ∩ supp q ≠ ∅: competitiveness of C_a against Y, and of C_q against W.
2. R = all would make Y ⪯ C_a at every world. Undominatedness then forces C_a ⪯_w Y at every world, an all-world tie, so direct (C) makes Y coherent.
3. F = all gives the same conclusion for W against C_q. ∎

*Data.* In the pump geometry:
- Y_plus is doubly anchored: A(rev) ∋ q, interior, and rec(Y_plus, C_a) also meets the edge Δ₁₂.
- Y_minus is not: A(rec(Y_minus, C_a)) = ∅ in all four settings (CHECKED, `t0_cube_backbone.out`).

So the mirror pair is not symmetric here. Only Y_plus has the two-sided constraint.

**Lemma 2.2 (cut lemma).** Let C be selected, w a world, and X_f a strict pointwise w-improvement of X_r. Then C ⪯_w X_f and X_r ⪯_w C cannot both hold.

*Proof.* X_r ⪯ C ⪯ X_f together with X_f ≺ X_r is a forbidden (TC) triangle. ∎

**Lemma 2.3 (pinning).** Let X be fixed and a interior. There is a neighbourhood N of a such that for every p ∈ N, ∅ ≠ F(C_p, X) ⊆ F(C_a, X).

*Proof.* Each {p : C_p ⪯_w X} is closed. For w ∉ F(C_a, X) it misses a, so it misses a neighbourhood of a. Competitiveness at interior p gives F(C_p, X) ≠ ∅. ∎

Two cases are compulsory.

- **(P1) Strict guidance at a.** If X strictly improves C_a pointwise at world w, then C_p ⋠_w X for p near a.
- **(P2) Guidance pinning.** If X strictly improves C_a pointwise at two worlds u and v, then for p near a:
  - C_p ⪯_w X at the third world w (forced);
  - by (TC), Z ⋠_w C_p for every Z that is a strict pointwise w-worsening of X.

**Lemma 2.4 (KKM dominators; standard).** For every X there is q with C_q ⪯_i X at all worlds. If X is incoherent, the comparison is strict at some world, by undominatedness and direct (C). In Lemma 2.1, q ≠ a.

This lemma did not yield a contradiction in any configuration tried (§5.4).

---

## 3. Theorem J: a forced allocation jump

### 3.1 Geometry

**Lemma J0 (PROVED; CHECKED).**
- *Statement.* Let a be interior and 0 < ε < 1, and let {i, j, k} = {1, 2, 3}. There are:
  - non-null open cones of problems G_i ⊂ M_i and G_j ⊂ M_j;
  - a point r of the open edge Δ_ij;

  such that:
  - C_a is silent on G_i ∪ G_j;
  - the precise edge model C_r says A on G_i ∪ G_j.

*Proof (i = 1, j = 2).*
1. **The projection ζ.** For x in the open simplex, let ζ(x) = x₂/(x₁+x₂). This is the e₂-coordinate of the point Z*(x) where the line through e₃ and x meets [e₁,e₂]. int K_a is a nonempty open set and ζ is not constant on it. Pick x, x′ ∈ int K_a with ζ(x) < ζ(x′), and r = (1−ρ, ρ, 0) with ζ(x) < ρ < ζ(x′).
2. **The M₁ line through x.** Rotate the line (e₃, x) slightly about x, so that its crossing with [e₁,e₂] moves to a point z with ζ(x) < z₂ < ρ. Its other end then moves to the e₁-side of e₃ and crosses the open edge (e₁, e₃).
   - So the line cuts off e₁: it is in M₁.
   - r lies on the e₂-side of z, which is the majority side, so C_r says A.
   - The line passes through x ∈ int K_a, so C_a is silent on it.
3. **The M₂ line through x′.** Symmetrically, a line through x′ crossing [e₁,e₂] at z′ with ρ < z′₂ < ζ(x′) is in M₂, has r on its majority (e₁-) side, and passes through int K_a.
4. **Open conditions.** All these conditions are open, so small cones of lines around the two lines work. ∎

*CHECKED (`t4_geometry.py`).* The construction was carried out exactly:
- 20 interior indices (including (.98,.01,.01) and (.01,.01,.98)) × ε ∈ {.3, .1, .01} × 3 edges, so **180/180** instances;
- in each: silence of C_a, the classes, C_r's advice on every ray, and that the exact anchor polygon of "A on G_i ∪ G_j" meets the open edge.

The pump cones S₁, S₂ themselves are an instance on Δ₁₂ in all four settings: rec(X[AAS], C_a) meets Δ₁₂ (`t2_threshold` (a)).

### 3.2 The theorem

**Theorem J (PROVED).**
- *Setting.* Let a, G₁, G₂, r be as in Lemma J0 (edge Δ₁₂; any other edge by symmetry). For λ ∈ [0,1] let G₁(λ) ⊆ G₁ be non-increasing and G₂(λ) ⊆ G₂ non-decreasing, with:
  - G(λ) Δ G(λ′) non-null for λ ≠ λ′;
  - G₂(0) = ∅ and G₁(1) = ∅;
  - G(λ) := G₁(λ) ∪ G₂(λ) non-null.
- *Definitions.*
  - X_λ := C_a with A on G(λ);
  - d(λ) := rec(X_λ, C_a), the change A→S on G(λ), and e(λ) := rec(C_a, X_λ);
  - L_w := {λ : d(λ) ∈ R_w} and F_w := {λ : e(λ) ∈ R_w}.
- *Assumptions.* Reflexivity, strict (G), (IB), the defence clause of (S) at r and at a, and undominatedness of C_a. Part (2) also uses (TC).
- *Conclusions.*
  - **(1)** L₁ ∩ L₂ = ∅ and L₁ ∪ L₂ = [0,1], with 0 ∈ L₂ and 1 ∈ L₁.
  - **(2)** There is λ₀ ∈ [0,1] with [0,λ₀) ⊆ L₂ and (λ₀,1] ⊆ L₁.
    - For λ < λ₀: C_a ≺₁ X_λ, X_λ ≺₂ C_a and X_λ ≺₃ C_a.
    - For λ > λ₀: X_λ ≺₁ C_a, C_a ≺₂ X_λ and X_λ ≺₃ C_a.
  - **(3)** If λ ↦ μ(G_w(λ)) is continuous, then R₁ and R₂ are not both closed in ρ, not even relative to {d(λ)}.

*Proof.*

**(1) Exactly one of worlds 1, 2.**
1. *At least one.* C_r says A on G(λ), and r ∈ Δ₁₂. By (IB), d(λ) = rec(C_r, C_r with S on G(λ)). Competitiveness of C_r on supp r = {1,2} gives d(λ) ∈ R₁ ∪ R₂.
2. *World 3.* On M₁ ∪ M₂, world 3 is a majority world, and A→S raises its rank from 0 to 1. So C_a is a pointwise world-3 worsening of X_λ, strictly on G(λ). By (G), d(λ) ∈ R₃ and e(λ) ∉ R₃.
3. *Not both.* If λ ∈ L₁ ∩ L₂, then X_λ ⪯_w C_a at every world while C_a ⋠₃ X_λ. So C_a is dominated, which is impossible.
4. *Ends.* d(0) is A→S on G₁(0) ⊂ M₁, a strict improvement for world 1 (its minority class). So 0 ∉ L₁, and 0 ∈ L₂. Symmetrically, 1 ∈ L₁.

**(2) The cut.**
1. *Guidance along the family.* For λ < λ′, X_{λ′} differs from X_λ by A→S on G₁(λ)∖G₁(λ′) ⊂ M₁ and S→A on G₂(λ′)∖G₂(λ) ⊂ M₂, at least one of them non-null. Both changes lower world 1's rank and raise world 2's. So X_{λ′} ≺₁ X_λ and X_λ ≺₂ X_{λ′}, both by strict (G).
2. *The two cuts.* By Lemma 2.2 at world 1: μ ∈ L₁ and ν > μ imply ν ∉ F₁. At world 2: μ ∈ L₂ and ν < μ imply ν ∉ F₂.
3. *The forward obligation.* a ∈ A(e(ν)) with a interior, and e(ν) ∉ R₃. So ν ∈ F₁ ∪ F₂.
4. *A single cut.* Hence there are no μ ∈ L₁ and μ′ ∈ L₂ with μ < μ′: any ν between them would lie in neither F₁ nor F₂. So sup L₂ ≤ inf L₁ =: λ₀.
5. *Above the cut.* For ν > λ₀, pick μ ∈ (λ₀, ν) ⊆ L₁. Then ν ∉ F₁, so ν ∈ F₂. With ν ∈ L₁ ∖ L₂ this gives the stated strict verdicts.
6. *Below the cut.* For ν < λ₀ the argument is symmetric.

**(3) Not both closed.** L₁ and L₂ are complementary and nonempty, and [0,1] is connected. If R_w were ρ-closed, then L_w = d⁻¹(R_w) would be closed, because ρ(d(λ), d(λ′)) = μ(G(λ) Δ G(λ′)) is continuous. ∎

### 3.3 The exact implication chains (CHECKED, `t2_threshold.py`)

The pool is C_a, C_q and X₀..X₅ (n = 5), closed under splicing: 68 models and 926 records.

| check | result, all four settings |
|---|---|
| (a) every interior d_k meets the edge Δ₁₂ | yes |
| (b) assume d_k ∈ R₁ ∩ R₂ (k = 1..4) | UNSAT. Core: **{UND: C_a undominated vs X_k}** plus (G) units: d_k ∈ R₃, e_k ∉ R₃ |
| (c) assume d_j ∈ R₁ and d_k ∈ R₂ with j < k | UNSAT exactly when there is a family member strictly between (pairs (1,3), (1,4), (2,4)), or when (G) alone refutes it (j = 0 or k = 5). Core for (1,3): **{OBL: rec(C_a,X₂) at some world; TC world 1 on (X₁, C_a, X₂); TC world 2 on (X₃, C_a, X₂)}** plus (G) units |
| adjacent pairs (1,2), (2,3), (3,4) | SAT. A finite family cannot see the strict jump; the continuum argument needs an intermediate member, which always exists there |
| (d) cut realisable at every position m = 1..5 | SAT |

**Chain (b) in words.**
- Suppose X_k ⪯₁ C_a and X_k ⪯₂ C_a.
- X_k ⪯₃ C_a holds by guidance.
- C_a ⋠₃ X_k holds by strict guidance.
- So C_a is dominated.

**Chain (c) in words.**
- Some world accepts C_a ⪯ X₂ (the face obligation at a), and world 3 cannot (strict G).
- At world 1: X₁ ⪯₁ C_a ⪯₁ X₂ with X₂ ≺₁ X₁ (guidance) violates (TC).
- At world 2: X₃ ⪯₂ C_a ⪯₂ X₂ with X₂ ≺₂ X₃ (guidance) violates (TC).

### 3.4 Corollaries

**J1 (record-level closedness is impossible; PROVED).** At every interior a and on every edge:
- R₁ and R₂ cannot both be ρ-closed;
- equivalently, for the edge model C_r, the acceptance sets {X : C_r ⪯_w X} (w = 1, 2) cannot both be closed in the rival under convergence in measure.

The axioms make each world's acceptance closed in the selected index (sections) and, necessarily, not closed in the rival. Excluded:
- every rule R_w = Guid_w ∪ {d : Φ_w(d) ≥ 0} ∩ E_w with ρ-continuous Φ_w and ρ-closed E_w (Guid_w = {ν(Q_w) = 0} is ρ-closed);
- AF, additive and Φ^κ-eligibility rules;
- the anchor plan's §6 rule (whose closedness the plan notes);
- PP7 §7's closed AF sets;
- any construction step that starts from closed accepted-record sets and removes open sets (audit Theorem 4's closedness route).

**J2 (forced lexicographic verdicts; PROVED).**
- Theorem J (2) is a two-level lexicographic pattern at worlds 1 and 2 with a cut. For λ₀ = 1, world 1 reads "fewest A-errors on M₁ first" and world 2 "fewest errors on its majority classes first".
- Under any record-continuous verdict, the cut would become a tie: the additive verdict ties at μ(G₁) = μ(G₂). Theorem J (1) forbids that tie.
- So audit §2's diagnosis (protected defences belong to a fixed lexicographic additive ranking) is not an artefact of PP9's rule. On these families the axioms force a cut of exactly that shape.
- The location of the cut is free (CHECKED, (d)).

**Proposition J3 (fibres do not see the jump; PROVED).**
- *Statement.* For a fixed model X, at most one p ∈ Δ has rec(C_p, X) ∈ {d(λ)}, and at most one has rec(C_p, X) ∈ {e(λ)}.
- *Proof.*
  1. *Reduction.* Suppose rec(C_p, X) = d(λ) and rec(C_{p′}, X) = d(λ′). Then C_p = A on G(λ), X = S there, and X = C_p elsewhere; likewise for p′. So C_p and C_{p′} agree a.e. off G(λ) ∪ G(λ′) ⊂ M₁ ∪ M₂, and differ only by A↔S there. In particular they agree a.e. on M₃.
  2. *Both precise (boundary).* Precise models are never silent on non-null sets, so the A↔S differences are null and p = p′.
  3. *One precise, one interior.* The interior model is silent on a non-null open set of M₃-lines (those near the lines x₃ = c, min_K x₃ < c < max_K x₃), and the precise one is not. So they disagree on M₃, a contradiction.
  4. *Both interior.* Use the M₃-problems g(c, δ) = (−c+δ, −c−δ, 1−c), 0 < c < 1, |δ| < c. On the simplex, g·x = x₃ − c + δ(x₁−x₂).
     - For small |δ|, max_{K_p} g·x is attained at the vertex v³ (the largest x₃), and the minimum at v² for δ > 0 and at v¹ for δ < 0.
     - Silence is the open region min < 0 < max in the (c, δ)-plane. Its two boundary curves are affine in δ and determined by the vertices.
     - The map (c, δ) ↦ g(c, δ) is a local diffeomorphism onto an open set of problem directions, so null sets correspond.
     - Two open regions with a null difference have the same closure, hence here the same boundary curves. So v¹, v², v³ agree, K_p = K_{p′}, and p = p′ (p is the centroid of K_p).
  5. *The e-family.* The argument is identical. ∎
- *Meaning.* The closed-section requirement of (S) never sees two records of a jump family. So (S) does not by itself forbid the jump.
- *Transport through (TC)/(IB).* The only such transport we found is J4, and it is consistent (§5.1).

**Corollary J4 (pinned defences; PROVED; CHECKED).**
- *Statement.* For λ < λ₀ there is a neighbourhood N(λ) of a such that every p ∈ N(λ) has C_p ⪯₁ X_λ, C_p ⋠₂ X_λ and C_p ⋠₃ X_λ. For λ > λ₀ the same holds with worlds 1 and 2 exchanged.
- *Proof.* By (2), F(C_a, X_λ) = {1} (respectively {2}). Apply Lemma 2.3. ∎
- *CHECKED (`t5_pinning.py`, four settings).*
  - Family n = 4, six germs. For each assumed cut position m, the forced pattern of (P_v ⪯₁, ⪯₂, ⪯₃ X_k) over all six germs is TFF for k ≤ m−2 and FTF for k ≥ m+1, as predicted.
  - World 3 is forced F for every k. This is (P1), because e_k ∉ R₃ by strict (G).
  - The two members adjacent to the cut are free, as in §3.3.

**Remark 3.5 (2-parameter families).**
- *Setting.* Take a two-parameter family X_g = C_a + A on G₁(g₁) ∪ G₂(g₂), with nested G_w(·).
- *Claim.* Theorem J applied along every path that decreases g₁ and increases g₂ shows:
  - L₁ is an up-set of world-1 goodness, i.e. it is closed under g₁↓, g₂↑;
  - L₂ is an up-set of world-2 goodness;
  - so the cut is a monotone curve.
- *Status.* PROVED from Theorem J, which allows monotone paths. Beyond the monotone cut curve, nothing more was found to be forced by these families.

**Remark 3.6 (Theorem J has no fibre version; PROVED for its mechanism).**
- *Which axioms link different worlds.* (G), (IB) and (TC) act world by world, and face obligations are positive disjunctions. Only undominatedness and direct (C) relate verdicts at different worlds, and both involve a comparison with the selected model on the **right**.
- *How Theorem J uses this.* Its "not both" step uses exactly this. d(λ) = rec(X_λ, C_a) has C_a on the right, and the same record is the fibre record rec(C_r, X′_λ) of the edge model.
- *Why the path must lie on an edge.* On an interior path, a two-world disjunction would need world 3 to be forbidden on the fibre records, while domination would need it compulsory. So only edge paths can work.
- *What a fibre version would need.* Take a fixed rival X and an edge path p(s) ⊂ Δ₁₂, which supplies the two-world obligation. "C_{p(s)} ⪯₁ X and C_{p(s)} ⪯₂ X cannot both hold" would need each fibre record rec(C_{p(s)}, X) to satisfy two conditions:
  - it is also realised as rec(Y_s, C_{c(s)}) with C_{c(s)} selected, so that C_{c(s)} agrees with X on D_s := D(C_{p(s)}, X);
  - it is compulsory and strict at world 3 by guidance: X is pointwise weakly worse than C_{p(s)} at world 3, and strictly somewhere.
- *This is impossible on any path with p(0) ≠ p(1).*
  1. *M₃.* On M₃ every edge model says A, world 3's worst regular advice. So D_s misses M₃.
  2. *Band lines.* On a band line (a line of M₁ ∪ M₂ crossing the edge between p(0) and p(1)), the edge models along the path give both A and B. Being weakly worse at world 3 than every one of them wherever it differs forces X = B there.
  3. *The interior of the path.* For interior s, D_s therefore contains:
     - the M₁ lines (all admissible slopes) crossing in (p(0), p(s)), with X = B;
     - the M₂ lines crossing in (p(s), p(1)), with X = B.
  4. *No selected model fits.* C_{c(s)} = B a.e. on the first set forces K_{c(s)} ⊆ [e₁, p(0)]; on the second, K_{c(s)} ⊆ [p(1), e₂]. These are incompatible. ∎
- *Conclusion.* So the disjointness that drives Theorem J exists only for records with the selected model on the right. It is invisible to the section-closedness of (S): fibres carry no such disjointness. This is the precise sense in which a contradiction would need more structure than (S) provides.

---

## 4. The module computations

### 4.1 The splice cube alone (`t0_cube_backbone.py`; CHECKED)

| setting | models (closed) | records | SAT, re-check | backbone |
|---|---|---|---|---|
| e₁ .3 | 108 (closed) | 3,086 | SAT, re-check clean | **0** of 8,496 free variables |
| e₁ .1 | 108 (closed) | 3,086 | SAT, re-check clean | **0** of 8,496 |
| u .3 | 108 (closed) | 3,086 | SAT, re-check clean | **0** of 8,496 |
| u .1 | 108 (closed) | 3,086 | SAT, re-check clean | **0** of 8,496 |

- *Pool size.* About 2.59 million clauses per instance. Certified-incoherent rivals (used for direct (C)): 93, 88, 91 and 95 of 106.
- *Empty backbone.* Every non-guidance comparison of the cube can be decided either way in some solution satisfying all the axioms on the pool.

- *Faces of the mirror pair* (`t0_cube_backbone.out`). In all four settings:
  - A(rec(C_a, Y_plus)) meets only the interior face;
  - A(rec(Y_plus, C_a)) meets Δ₁₂ and the interior (doubly anchored, plus the F-B edge);
  - A(rec(C_a, Y_minus)) meets only the interior face;
  - A(rec(Y_minus, C_a)) = ∅.
- *Edge anchors* (`t8_edge_faces.out`). Genuine edge obligations are those where the anchor set meets an open edge and no world of that edge is guidance. In the cube pool:
  - on Δ₁₂: every such record has old side A on S₁, together with A on S₂ and/or S₃ or B on T (30 records at e₁ .3, 48 elsewhere);
  - on Δ₁₃: old side B on S₃ (12–48 records);
  - on Δ₂₃: old side B on S₂ and on S₃ (12 records).
- *Which are of Theorem J's type.* Only the Δ₁₂ records whose changes are A→(S or B) on S₁ ∪ S₂ alone qualify: there the third world's rank rises. For the others the third world is strictly improved by the change, so undominatedness supplies no "not both" step.

### 4.2 The full module (`t1_module_sat.py`; CHECKED)

The pool is the cube plus the transfers, the Theorem-J family (three interior members, frozen), PP8 F-B's C_p and six germs: 118 models, of which 9 are selected and 6 are germs.

| setting | records | clauses | genuine edge obligations (Δ₁₂ / Δ₁₃ / Δ₂₃) | SAT, re-check | backbone |
|---|---|---|---|---|---|
| e₁ .3 | 5,336 | 3,577,045 | 45 / 60 / 15 | SAT, re-check clean | 312 of 14,982 free |
| e₁ .1 | 5,336 | 3,577,226 | 69 / 36 / 15 | SAT, re-check clean | 312 of 14,982 |
| u .3 | 5,336 | 3,577,129 | 69 / 15 / 15 | SAT, re-check clean | 312 of 14,982 |
| u .1 | 5,336 | 3,577,198 | 69 / 36 / 15 | SAT, re-check clean | 312 of 14,982 |

The edge column counts records whose anchor set meets the edge away from both of its vertices; some of these are also met by guidance. The re-check covers (G), (TC), obligations, undominatedness, direct (C) and the closed-section clauses.

### 4.3 One explicit solution (`t7_solution_table.py`, e₁ .3; CHECKED)

The worlds accepting each direction are listed as "C ⪯ X" / "X ⪯ C".

| comparison | solution 1 | solution 2 (defence moved to world 1) | faces fwd / rev |
|---|---|---|---|
| C_a vs Y_plus | {3} / {2} | {1} / {1} (a tie at world 1) | interior / Δ₁₂, interior |
| C_a vs Y_minus | {3} / ∅ | {2,3} / ∅ | interior / none |
| Y_plus vs Y_minus | {2} / ∅ | {2,3} / ∅ | Δ₁₂, interior / none |
| C_a vs Z (Z ≺₁ C_a by (G)) | {2,3} / {1} | {2,3} / {1} | interior / vertex e₁, … |
| Y_plus vs Z | {3} / ∅ | {3} / {1} | interior / none |
| C_a vs C_q | {3} / {2} | {1} / {2,3} | interior / interior |
| C_a vs C_p (F-B) | {3} / {2} | {3} / {1} | interior / interior |
| C_p vs Y_plus (F-B) | {2} / ∅ | {1,2,3} / ∅ | interior / none |
| germ P_(1,−1,0) vs Y_plus | {3} / ∅ | {1} / ∅ | interior / none |
| C_q vs W (transfer of rev(C_a, Y_plus)) | {2} / {3} | {1} / {1} | Δ₁₂, interior / interior |
| Theorem-J family d_k, k = 0..4 | {2,3},{2,3},{1,3},{1,3},{1,3}: cut between k = 1 and 2 | {2,3},{2,3},{2,3},{1,3},{1,3}: cut between k = 2 and 3 | |

Both solutions pass the independent re-check.

- *Solution 2 is PP8's F-A configuration.* C_a defends against Y_plus at world 1, the lead world.
- *The return is refused there.* Y_plus ⪯₁ Z is refused, as (TC) requires. This is the return quarantine, chosen and not imposed.
- *Ties are allowed.* The pair {C_a, Y_plus} and its transfer {C_q, W} are tied at world 1 and incomparable elsewhere.
- *Everything here is a choice.* Every comparison between selected models, every defender and the cut are choices, not consequences.

---

## 5. What is forced, what is free, and the explicit assignment L\*

### 5.1 Everything forced on the full module (CHECKED, `t6_backbone_classify.py`, e₁ .3)

The backbone of the full instance has 312 literals (out of 14,982 free variables). Every one falls into one of three classes; none is left over.

| class | count | mechanism |
|---|---|---|
| germ ⪯_w X refused, where C_a ⪯_w X is refused by strict (G) | 192 | (P1): closedness of {p : C_p ⪯_w X} at a |
| germ ⪯_w W forced, W a strict improvement of C_a at the two other worlds | 18 | (P2) pinning |
| Z ⪯_w germ refused, via a pinned W with W ≺_w Z by (G) | 102 | (TC) applied to (P2) |
| other | **0** | |

- *The (P1) refusals.* All 192 lie on records whose face obligation (the interior face, from the germ itself) leaves two other worlds available.
- *The (TC) refusals.* None of the 102 lies on a record with any face obligation.

So, on the module, the compulsory non-guidance comparisons are exactly:
- the closed-section consequences of Lemma 2.3: (P1) refusals and (P2) pinned defences;
- the (TC) refusals of returns into germs that P2 entails;
- conditionally on the cut, J4.

None of them makes an obligation unsatisfiable (the instance is SAT).

### 5.2 Why these pinnings do not combine into a contradiction (PROVED, for this mechanism)

1. *What P2 refuses.* P2 refuses C_q ⪯_w C_p (p near a, C_q selected) only through some W that strictly improves C_a at the two worlds other than w and satisfies W ≺_w C_q by guidance.
2. *What that requires.* That W differs from C_a only on M_w, moving toward A. Then W ≺_w C_q forces C_a to be a pointwise w-improvement of C_q.
3. *Only one world.* C_a can be a pointwise improvement of C_q at two worlds only if they agree on two classes. By the vertex argument of J3, that forces q = a.
4. *Conclusion.* This mechanism refuses C_q's defence against nearby C_p at **at most one** world. So, on its own, it never blocks C_q's competitiveness against C_p.
5. *Returns into germs.* The (TC) refusals of returns Z ⪯ C_p carry no face obligation in any of the 102 cases (§5.1, CHECKED). Their old side is C_a on D(C_p, C_a) together with Z's modifications, which no selected model realises.

### 5.3 The explicit complete assignment L\* (diagnostic; CHECKED, `t3_lex_witness.py`)

*Definition.*
- World 1: lex(J₁, E₁, cell-lex).
- World 2: lex(Jmaj₂, E₂, cell-lex).
- World 3: lex(J₃, E₃, cell-lex).

Here J_w is world w's error on its minority class, Jmaj₂ is world 2's error on M₁ ∪ M₃, E_w is the total error, and cell-lex breaks every remaining tie on the first changed cell.

*Why the structural axioms hold.* Each world is a total preorder of records. So reflexivity, (G), (IB) and (TC) are automatic.

*Results* (`t3_lex_witness.out`):

| setting | violations of the full module's clauses | uncertified level signs |
|---|---|---|
| e₁ .3 | G 0, TC 0, OBL 0, UND 0, DC 0, **CL 61** | 12, treated as 0, so the implemented assignment is L\* up to these |
| e₁ .1 | all 0 except **CL 183** | 0 |
| u .3 | all 0 except **CL 78** | 0 |
| u .1 | all 0 except **CL 69** | 0 |

- *The failures.* Every failure is of type (P1). For example, P_{(1,−1,0)} ⪯₁ Z while C_a ⋠₁ Z, Z being a strict world-1 improvement of C_a. Minority-first world 1 accepts it because J₁(C_p) < J₁(C_a) for p moved toward e₁. A complete lexicographic world cannot refuse it.
- *The jump.* On the Theorem-J family, L\* has λ₀ = 1.
- *Reading.* L\* is the brief's "fixed minority-first evaluation". It gives no new mechanism (stop condition 2). Its role is to show exactly where the module's difficulty lies:
  - a complete, record-discontinuous rule meets every requirement **except** closed sections;
  - Theorem J shows that record-continuous rules fail;
  - so a construction must be record-discontinuous (J1), incomplete enough to refuse the (P1) comparisons near every selected model, and closed along fibres.

### 5.4 Adversarial routes tried and why they stop (summary)

| route | outcome | label |
|---|---|---|
| doubly anchored Y_plus: pair lemma + cut lemma over its nested family | consistent: a constant allocation F = {1}, R = {2,3} satisfies all the derived constraints | PROVED (2.1, 2.2); CHECKED (pools SAT) |
| PP7-style antichain argument without AF ties | needs ties forced at one world. None of the forcing mechanisms found forces a tie: obligations, (G), the pair lemma, pinning and Theorem J. Theorem J forces the opposite, strict verdicts. Forced single acceptances come only from guidance (audit Thm 2) or pinning | PROVED for these mechanisms |
| mirror rivals (B-patterns), including Y_minus | no jump: on B-type families the third world is strictly improved, so there is no "not both" step. In the pump geometry rec(Y_minus, C_a) is unanchored, so Y_minus carries one-sided constraints only | PROVED (mechanism); CHECKED (faces) |
| record-closed allocation | contradiction (J1) | PROVED |
| closed sections + KKM on the edge for the jump family | J3: no fibre meets the family twice. Remark 3.6: no fibre disjointness | PROVED |
| pinning (P2, J4) + (TC) + selected-selected comparisons | refuses at most one world per selected pair (5.2); all pools SAT | PROVED / CHECKED |
| three-class families anchored on all three edges | would force a Sperner-type "missing world" labelling. The "largest minority mass" labelling satisfies the derived constraints. Such triple edge anchoring is moreover not generic near a | sketch only |
| finite most-permissive search over the whole module | SAT in all settings | CHECKED |

---

## 6. Answers to the brief

**Adversarial output.**
- No chain ending in a contradiction exists among those we could build from the listed tools on the module.
- The chains we did build (§3.3) end in a **forced structure**: an allocation jump with strict lexicographic verdicts. They do not end in an impossibility.
- Every link is an axiom instance. No link is a margin or additive comparison.

**"State precisely what freedom remains."**
- (i) One cut per edge-anchored AA-family, which is a monotone curve in two-parameter families. All positions are realisable.
- (ii) Beyond guidance, the closed-section pinnings and their (TC) refusals, nothing is compulsory on the module.
- (iii) An explicit consistent assignment exists for every clause except closed sections (L\*). Assignments meeting the closed-section clauses as well exist on all exact pools.

**"The first place a contradiction would need more structure."**
- Closedness in the rival argument: Theorem J makes this contradictory at once.
- Or a disjointness principle on fibres, which (S) lacks (Remark 3.6).
- Neither is among the axioms, and the first cannot be added.

**Stop conditions.**
1. Unrestricted assignments work on every pool. So no priority was patched.
2. L\* is fixed minority-first evaluation and is reported only as a diagnostic.
3. Theorem J is not a theorem about a shrinking subclass. It constrains **every** system satisfying the axioms. But it does not settle the coupled problem, because it yields a forced jump and not a contradiction.
4. The jump theorem's dependence on the homothetic selection is stated in §0.6. No claim about T1 being uncoverable is made.

**Suggested shift for the constructive side (nearby reachable target).** Design rules that are:
- closed **along fibres** {rec(C_p, X) : p ∈ Δ} only;
- deliberately **discontinuous across rivals**, with the cut of Theorem J placed on records that no fibre meets twice (J3);
- **incomplete** wherever (P1) requires a refusal near a selected model.

L\* already has the first two properties except closedness along fibres. The open problem is to make a lexicographic-type rule fibre-closed by refusing exactly the (P1) comparisons, without breaking (TC).

---

## 7. Scripts (`PP11_py/`)

| script → output | content | label |
|---|---|---|
| `pp11sat.py` | most-permissive axiom encoding; solve; backbone; deletion-minimal labelled cores; streaming mode; independent checker | library |
| `modules.py` | pump geometry (PP8 `cfg_pp5_pump`), splice cube, closure excluding frozen (germ) models, path points | library |
| `t0_cube_backbone.py` → `t0_cube_backbone.out` | §4.1: cube alone, four settings: SAT, re-check, empty backbone, mirror faces | CHECKED |
| `t1_module_sat.py` → `t1_module_sat_*.out`, `t1_run.log` | §4.2: full module, four settings | CHECKED |
| `t2_threshold.py` → `t2_threshold_e1_3_e1_1_u_3_u_1.out` | §3.3: Theorem J on exact pools, with cores | CHECKED |
| `t3_lex_witness.py` → `t3_lex_witness.out` | §5.3: L\* against every clause | CHECKED (12 uncertified level signs at e₁ .3) |
| `t4_geometry.py` → `t4_geometry.out` | Lemma J0, 180 exact instances | CHECKED |
| `t5_pinning.py` → `t5_pinning.out` | Corollary J4 with germs, four settings | CHECKED |
| `t6_backbone_classify.py` → `t6_backbone_classify_e1_3.out` | §5.1: classification of the full module's backbone | CHECKED |
| `t7_solution_table.py` → `t7_solution_table_e1_3.out` | §4.3: one verified solution, and a second with Y_plus's defence moved | CHECKED |
| `t8_edge_faces.py` → `t8_edge_faces.out` | §4.1: genuine edge obligations of the cube pool, by edge and pattern, four settings | CHECKED |

**Dependencies.** `PP8_py/` (unmodified; python-flint, numpy, mpmath) and pysat (CaDiCaL 1.9).
