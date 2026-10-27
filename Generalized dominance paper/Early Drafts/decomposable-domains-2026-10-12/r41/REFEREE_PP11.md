# Referee report on PP11: Theorem J and J1–J4

21 October 2026. Adversarial referee, one reader. Scope: `PP11_coupled_obstruction.md` §§0, 2, 3 and 6, the scripts behind §3 (`t2_threshold.py`, `t4_geometry.py`), and context from `AUDIT_round40_brief.md`, `AUDIT_anchor_plan.md`, `PP8_joint_defence_test.md`, `DESIGN_MEMO.md` §8 and `gate2d/Separation-Gated-Evaluators.tex`. I did not re-referee the module SAT runs of §§4–5 (t0, t1, t3, t6, t7).

Definitions used are the project's own (Consolidated Statements §0.2):
- *undominated* means no Y has Y ⪯_i C at every world and Y ≺_j C at some world;
- (G) has a weak half and a strict half;
- (S) is competitiveness on supp p, plus closed sections in p;
- (TC) forbids X ⪯ Y ⪯ Z ≺ X.

## Verdicts

| # | item | verdict |
|---|---|---|
| 1 | Lemma J0: the two-class patterns X_λ exist | **CONFIRMED** |
| 2 | Theorem J (1): exactly one of worlds 1, 2 | **CONFIRMED** |
| 3 | Theorem J (2): a single cut via (TC) | **CONFIRMED** (one wording point) |
| 4 | J1: closed accepted-record sets are impossible | **CONFIRMED WITH REPAIR**. The proof is correct. The headline is stated without the hypothesis on the selection, and in that unqualified form it is false. |
| 5 | Consistency with known positive constructions | **CONFIRMED** (consistent). Two-world gated systems have ρ-closed R_i. J1 genuinely needs three worlds; the two places where they are used are named below. |
| 6a | J3 | **CONFIRMED**. Its "meaning" sentence is heuristic. |
| 6b | J4 | **CONFIRMED** (conditional on the cut, as stated) |
| 6c | Scope statement | **CONFIRMED WITH REPAIR** |
| (extra) | J2, the "no record-continuous verdict" claim | **CONFIRMED WITH REPAIR** (overstated) |

No item is WRONG. The mathematical core is sound: Lemma J0, Theorem J (1)–(3), J3 and J4. The repairs concern the statements of J1, J2 and the scope, and one strengthening that the note misses: **J1 does not use (TC)**.

---

## 1. Lemma J0: existence of the patterns. CONFIRMED

**The geometry.** I re-derived it with the edge Δ₁₂, the third world 3, and ζ(x) = x₂/(x₁+x₂).
- *The M₁ line.* Take the line through x ∈ int K_a that crosses [e₁,e₂] at z, with ζ(x) < z₂ < ρ. Its other end lies on the e₁-side of e₃, so it crosses the open edge (e₁,e₃). The line therefore separates e₁ from {e₂,e₃}, and it is in M₁.
  - r = (1−ρ, ρ, 0) lies on the e₂-side of z, which is the e₂/e₃ side. So C_r = D_{r} gives the advice of worlds 2 and 3: the majority advice A.
  - The line passes through int K_a, so min_{K_a} < 0 < max_{K_a} and C_a is silent.
- *The M₂ line* (through x′, crossing at z′ with ρ < z′₂ < ζ(x′)) is the mirror image.
- *Openness.* Every condition is a strict inequality, so small open cones (non-null under the Gaussian measure) around each line work. Both orientations of g belong to the same class, and "A" is defined relative to the class, so the orientation does not matter.

**Quantifiers.**
- *Every interior index, every ε ∈ (0,1).* int K_a ≠ ∅ whenever min a > 0 and ε > 0, and ζ is non-constant on any open set. The admissible r form the whole open window ζ(int K_a) ⊂ (0,1) of the edge.
- *Every edge.* The family K_p = p + 3ε min p (Δ − u) is permutation-equivariant, and the proof uses only int K_a ≠ ∅ anyway.
- *The whole pattern.* G(λ) ⊆ G₁ ∪ G₂ for every λ, so the single model C_r says A on every G(λ).

**Re-run.** `t4_geometry.py` gives 180/180, byte-identical to the archived output. Its silence test uses a common strictly negative vertex and a common strictly positive vertex of K_a for the three rays of a simplicial cone. Silence is linear along the cone, so this is exact for the whole cone.

**Small sharpening (not needed).** Precision of the edge model is sufficient but not necessary. Any selected C_r with r in the open edge that says A on G₁ ∪ G₂ will do. For example, a short credal segment K_r ⊂ Δ₁₂ whose ζ-range lies inside the window works.

## 2. "Exactly one of worlds 1, 2". CONFIRMED

**At least one: which axiom, and anchored where.**
- The obligation is the **{1,2}-face obligation of d(λ)**, anchored at the edge point r ∈ A(d(λ)) ∩ relint Δ₁₂.
- Unpacked: the precise selected model C_r is competitive on supp r = {1,2} against C_r^[S on G(λ)]. By (IB),
  rec(C_r, C_r^[S on G(λ)]) = (A→S on G(λ)) = rec(X_λ, C_a) = d(λ),
  so d(λ) ∈ R₁ ∪ R₂.
- The other faces met by A(d(λ)) impose nothing beyond guidance.
  - The vertex e₃ is always in A(d(λ)): world 3 is a majority world on M₁ ∪ M₂, so C_{e₃} says A on both classes. Its obligation is world 3, which is guidance.
  - Any interior anchor gives the obligation {1,2,3}, again met by world 3.
  - This matches the archived face lists (`t2` (a)): d₀ meets the vertices e₂ and e₃, d_n meets e₁ and e₃, and every interior d_k meets Δ₁₂.

**World 3 accepts by guidance.**
- On M₁ ∪ M₂, world 3 ranks A 0 and S 1. So the change A→S is a weak world-3 worsening, strict on the non-null set G(λ).
- The weak half of (G) gives X_λ ⪯₃ C_a, i.e. d(λ) ∈ R₃.
- The strict half gives C_a ⋠₃ X_λ, i.e. e(λ) ∉ R₃.
- **Both halves of (G) are needed.** The theorem's hypothesis line says "strict (G)". It should say "(G), both halves". The project's strict (G) does include the weak half (PP4, Consolidated §0.2), so this is a wording point only.

**Not both.**
- If d(λ) ∈ R₁ ∩ R₂, then X_λ ⪯_w C_a at every world, and X_λ ≺₃ C_a.
- That is domination in the project's weak sense. It contradicts the undominatedness of the selected C_a.
- The argument would fail under a "strictly at every world" notion of domination. That is not the project's notion.

**The ends.**
- d(0) is A→S on G₁(0) ⊂ M₁, where world 1 is the minority (A 2 → S 1). That is a strict world-1 improvement, so d(0) ∉ R₁ and hence d(0) ∈ R₂.
- d(1) is symmetric.

**Independent check.** `REFEREE_PP11_py/ref_skeleton.py` encodes the family abstractly: no geometry, one variable per record and world, the (G) units derived by hand from the rank table, EDGE, FWD, UND, and every (TC) triangle on {C_a, X₀..X₅} at all three worlds. The world-3 comparisons between members are left free, because they are not guidance.
- With all clauses, every solution has exactly one of {1,2} on every d_k.
- Removing UND produces "both" solutions. Removing EDGE produces "neither" solutions.
- So the two clauses the note names are exactly the ones doing the work.

## 3. The single cut via (TC). CONFIRMED

**The triangles are actual triples of models.**
- At world 1, for μ < ν, the triple is (X_μ, C_a, X_ν), with links d(μ), e(ν) and rec(X_ν, X_μ).
- The third link is fixed by (G):
  - from X_μ to X_ν, the change is A→S on G₁(μ)∖G₁(ν) ⊂ M₁ and S→A on G₂(ν)∖G₂(μ) ⊂ M₂;
  - both moves lower world 1's rank and raise world 2's;
  - so X_ν ≺₁ X_μ strictly, and X_μ ≺₂ X_ν strictly.
- (IB) only identifies verdicts across contexts. A (TC) clause on a genuine triple cannot conflict with it, so there is nothing to make consistent.

**The step from the cut lemma to the conclusion.**
- Lemma 2.2 gives: μ ∈ L₁ and ν > μ imply ν ∉ F₁; μ ∈ L₂ and ν < μ imply ν ∉ F₂.
- Competitiveness of C_a on all three worlds, together with e(ν) ∉ R₃, gives ν ∈ F₁ ∪ F₂.
- So any ν strictly between some μ ∈ L₁ and some μ′ > μ in L₂ is impossible. With (1), this gives sup L₂ ≤ inf L₁, and the strict verdicts on each side.
- The intermediate member always exists on the continuum.
- In finite families a single *adjacent* inversion is allowed. My skeleton finds such solutions (e.g. `L1 ...1.1 / L2 222.2.`), and none with an inversion at distance ≥ 2. This matches `t2` (c).

**Re-run.** `t2_threshold.py` (a referee copy) reproduces the archived output identically in all four settings, including both deletion-minimal cores.

**What the skeleton shows each clause does.**
- Without FWD, 48 of 352 projected solutions have a far inversion. Without (TC), 648 of 1296 do.
- So the cut needs exactly the forward obligation plus the two (TC) triangles, as the note says.

**Wording point.** §0.2 says "every comparison between C_a and the family is then strict and fixed". This holds for λ ≠ λ₀ only. At λ₀ itself, F(C_a, X_{λ₀}) may be {1,2}: the skeleton finds such solutions, e.g. `L1 ....11, F1 1111.., F2 ...222`. The statement of Theorem J (2) is correct; only the summary sentence needs "λ ≠ λ₀".

## 4. J1. CONFIRMED WITH REPAIR

### 4.1 The topology

ρ(d, d′) = μ{g : lab_d(g) ≠ lab_{d′}(g)}, where lab_d(g) ∈ {unchanged} ∪ {(old, new) : old ≠ new}. This is convergence in measure of the label maps.

Two facts make it the right topology for the notes J1 targets:
- ρ(rec(X,Y), rec(X′,Y′)) ≤ μ(X≠X′) + μ(Y≠Y′), so rec is continuous for convergence in measure.
- Conversely, a ρ-convergent sequence of records lifts to convergent pairs of models. Keep one context fixed off the changed sets; the extra mass is at most ρ.

Hence, under (IB), **R_w is ρ-closed iff the graph {(X,Y) : X ⪯_w Y} is closed in both arguments under convergence in measure**. This is exactly the "closed graph" of the anchor plan §2 and the "closed" of anchor plan §7 and PP8 §7. So J1's reading is the natural one, not a strawman.

Any coarser topology has fewer closed sets, so J1 excludes closedness there too. A strictly finer topology on records would escape J1, but none is proposed anywhere.

### 4.2 Does the jump really contradict closedness? Yes, and no hidden assumption is used

- **No continuity of verdicts is assumed.** λ ↦ d(λ) is ρ-continuous because ρ(d(λ), d(λ′)) = μ(G(λ) Δ G(λ′)). Such families exist: take G₁(λ) = G₁ ∩ {h₁ > λ} and G₂(λ) = G₂ ∩ {h₂ < λ}, with h_w measurable and of continuous, strictly increasing distribution.
- **No assumption on which world accepts the limit.** J1 uses only Theorem J (1), applied to every member including λ₀: L₁ and L₂ partition [0,1], with 0 ∈ L₂ and 1 ∈ L₁. Connectedness then forbids both from being closed.
  - Concretely, suppose d(λ₀) ∈ L₁. Then d(λ) ∈ R₂ for λ ↑ λ₀ while d(λ₀) ∉ R₂, so R₂ fails to be closed.
  - If d(λ₀) ∈ L₂, then R₁ fails to be closed from the right.
  - At the ends, (G) fixes the side: λ₀ = 0 forces failure of R₁, and λ₀ = 1 forces failure of R₂.
- **Search for gaps.** I looked for a hidden premise in five places and found none:
  - the realisability of X_λ: it lies in the full domain, and in any decomposable domain containing C_a and C_r, since only S and A are used on G;
  - that d(λ) is the same record in both contexts;
  - non-nullness of G(λ) at every λ;
  - the definition of domination;
  - the endpoint cases.

### 4.3 Repairs and sharpenings

**(R1) The headline needs the hypothesis on the selection; unqualified, it is false.** §0.3 says "no system satisfying the axioms has accepted-record sets R_i that are closed in the record metric".
- *Counterexample to the unqualified form.* Additive three-world systems with a.e.-unique coherent Bayes minimisers satisfy (G), (IB), (LA), (S), (C) with C_p = B_p (Consolidated, "(S) Sufficiency", REFEREED-CORRECT).
  - Their R_w = {∫_D (ℓ_w(new) − ℓ_w(old)) dμ ≥ 0} are ρ-closed: the integrable envelope gives absolute continuity.
  - They escape Theorem J only because no interior selected model is silent on non-null cones of M₁ and M₂ crossing the edge on both sides of a selected edge point.
- *Repair.* State J1 for selections with Theorem J's hypotheses: an interior selected C_a silent on non-null cones G_i ⊂ M_i and G_j ⊂ M_j, and a selected C_r with r in the open edge Δ_ij that says A on G_i ∪ G_j. The homothetic K_p family has these at every interior a.
- §0.6 already has the right scope; the J1 bullets in §§0.3 and 3.4 should repeat it.

**(R2) "Equivalently" should read "more strongly".** The rival form ({X : C_r ⪯_w X}, w = 1,2, not both closed under convergence in measure) implies the record form, not conversely: R_w closed implies every rival-section closed. The rival form is the stronger statement, and it is the one proved.

**(R3) "Necessarily, not closed in the rival" is too broad as written.** J1 concerns:
- the rival-sections of the **edge** models C_r;
- equivalently, the reverse sections {X : X ⪯_w C_a} into the interior model.

It says nothing about the forward sections {X : C_a ⪯_w X} of the interior model. Along a jump family these can both be closed: F₁ = [0, λ₀] and F₂ = [λ₀, 1] are consistent with every clause (skeleton). The sentence should be restricted.

**(S1) Strengthening: J1 does not use (TC).** Part (3) uses only part (1). Part (1) uses reflexivity, (G) (both halves), (IB), the edge defence at r, and undominatedness of C_a. (TC) and closed sections play no role. The skeleton confirms it: without (TC), "exactly one" still holds on every member.

Every excluded rule therefore fails already at **undominatedness or the edge defence**, independently of its (TC) behaviour:
- *Φ^κ rules* R_w = Guid_w ∪ {κ·on_w − off_w ≥ 0}, with x = μ(G₁), y = μ(G₂). Then Φ₁ = κy − x and Φ₂ = κx − y.
  - For κ ≥ 1 both worlds accept on y/x ∈ [1/κ, κ], so C_a is dominated. The additive rule (κ = 1) fails exactly at the tie x = y; κ = 2 fails on λ ∈ [1/3, 2/3].
  - For κ < 1 neither world accepts on y/x ∈ (κ, 1/κ), so C_r's edge defence is lost.
  - Computed exactly in `ref_skeleton.out`.
- *The anchor plan's §6 rule.* It is ρ-closed and strictly guiding, and the plan proves it covers every face obligation. J1 then predicts that **it makes some interior selected C_a dominated by some X_λ**, quite apart from the (TC) failure PP5 found. This is a free corollary worth recording. I have not computed the explicit λ.

**(S2) Sharp count.** Applying J1 on all three edges shows that **at least two of R₁, R₂, R₃ are not ρ-closed**. Whether one world can keep a closed R_w, for example by always putting d(λ₀) on its side, is OPEN. It is a natural nearby question for the constructive side.

## 5. Consistency with positive constructions. CONFIRMED (consistent)

**Two worlds: gated systems have ρ-closed R_i.** Take gate2d's rule R_i = Id ∪ Guid_i ∪ {i-separated and Φ_i ≥ 0}, with a ρ-continuous Φ_i. Two examples are the instance 2·on − off, and the additive on − off, which satisfies (V1)–(V3) and so is also a two-world cover.

*Proof that R_i is closed.*
1. **Steps track records.** ν(T^on(d) Δ T^on(d′)) ≤ 3ρ(d, d′), and likewise for T^off.
2. **Setup.** Let d_n ∈ R_i with d_n → d, and pass to a subsequence that stays in one clause.
3. **Guidance clause.** The guidance set {ν(T^off) = 0} is closed.
4. **Gate clause.** Φ_i(d) ≥ 0 by continuity.
   - If T^on(d) is null, then off(d) ≤ 2·on(d) = 0, or off ≤ on for the additive rule. So d is trivial, hence accepted.
   - Otherwise, suppose d is not separated. Then for some κ′ < κ the sets T^on(d) ∩ {k > κ} and T^off(d) ∩ {k < κ′} have positive mass.
   - For large n, the same holds for d_n, which is then not separated: a contradiction.

So gate2d's instance has closed accepted-record sets, not only closed sections. J1 must therefore use the third world, and it does so in two places.

**(a) The "at least one" step needs a selected model whose support is a proper face with two worlds.**
- In two worlds the proper faces are vertices, and their defences are guidance.
- The interior cannot play the role either. In gate2d, for a family X_λ = C_a with accept-g on P and accept-(−g) on Q inside C_a's band [l(a), u(a)], an anchoring C_r would need l(a) < l(r) and u(r) < u(a). That is impossible because l and u are strictly increasing: the selected bands are never strictly nested.
- So d(λ) carries no obligation. Gate2d accepts reverse records into selected models only by guidance (proof of its main theorem), so L₁ = L₂ = ∅ on such families, and nothing is violated.
- In three worlds, the precise edge model anchors d(λ) without being nested in K_a. It only has to lie on the majority side of the lines through C_a's silence.

**(b) The "not both" step needs a world that is a majority world on both classes**, so that d(λ) is a strict worsening there. In two worlds every regular mixed change improves one world and worsens the other, so there is no such third world.

**Additive covers.**
- The gated additive two-world cover has closed R_i: consistent, as just shown.
- The ungated additive rule with an imprecise two-world selection fails for a different reason. Silent→(g on P, −g on Q) with μ(P) = μ(Q) ties at both worlds, and for interleaved P, Q the tie is with an incoherent model, which violates (C). This is not a J1 effect.
- The three-world additive Bayes systems (§4 R1) are closed and consistent, because Theorem J's hypotheses fail for precise interior selections. This is why the repair R1 is needed.

## 6. J3, J4, J2 and the scope

**J3: CONFIRMED.**
1. *Reduction.* rec(C_p, X) = d(λ) forces D(C_p, X) = G(λ), C_p = A and X = S there, and C_p = X elsewhere. So two such C_p, C_{p′} agree a.e. off G(λ) ∪ G(λ′) ⊂ M₁ ∪ M₂, in particular on M₃.
2. *Both precise.* Precise models are silent only on null sets, so the two models agree and p = p′.
3. *One precise, one interior.* The interior model is silent on an open set of lines near x₃ = c, and the precise one is not.
4. *Both interior.* For small |δ|, the vertex analysis of the (c, δ) family is right: the max is attained at v³, and the min at v² for δ > 0 and at v¹ for δ < 0. Two open sets with null symmetric difference have equal closures, which yields the same boundary functions. Each boundary function determines x₃ and x₁ − x₂ of a vertex, hence the vertex. p is the centroid of K_p.
5. *The e-family.* Identical.

The argument uses the triangle shape, as the scope says.

*Caveat on the "meaning" sentence* ("(S) does not by itself forbid the jump"):
- J3 is about **exact** membership of fibre records in the family.
- Closed sections act through limits. A fibre can approach d(λ₀) through records outside the family, and J3 says nothing about those.
- The sentence is a correct heuristic and is suitably hedged by "the only such transport we found is J4", but it is not a theorem.

**J4: CONFIRMED.**
- By Theorem J (2), F(C_a, X_λ) = {1} for λ < λ₀. Lemma 2.3 (closed sections plus competitiveness at interior p) then gives F(C_p, X_λ) = {1} on a neighbourhood N(λ).
- J4 uses (TC), through (2), and closed sections. It is conditional on the cut, which is free.
- N(λ) is not uniform as λ → λ₀; nothing claims it is.
- The CHECKED part (t5) rests on the germ clauses, whose t ∈ (0, t₀) is NUMERICS. The note says so (§1.3).

**J2: CONFIRMED WITH REPAIR.** "No record-continuous verdict can do this" is overstated.
- A ρ-continuous score with a weak inequality at one world and a strict one at the other reproduces the cut exactly. Example: R₁ = Guid ∪ {on − off ≥ 0} and R₂ = Guid ∪ {on − off > 0}. On the family, L₁ = {y ≥ x} and L₂ = {x > y}, with the cut at λ = ½.
- What is excluded is verdicts {Φ_w ≥ 0} at **both** worlds with ρ-continuous Φ_w, which is J1 again.
- *Repair:* "no verdict that is closed at both worlds". Whether such mixed open/closed verdicts survive the other edges and (S) is open, and is related to §4 S2.

**Scope (§0.6): CONFIRMED WITH REPAIR.**
- *State the hypotheses in the form used.* Theorem J and J1 need:
  - (i) an interior selected C_a silent on non-null cones G_i ⊂ M_i and G_j ⊂ M_j;
  - (ii) a selected C_r, r in the open edge Δ_ij, saying A on G_i ∪ G_j;
  - (iii) three worlds, through the common majority world k.

  "int K_a ≠ ∅" and "precise edge models" are sufficient conditions for (i) and (ii). Precise interior selections violate (i), and closed systems exist for them (§4 R1).
- *Say which part uses what:*
  - J3 additionally uses the triangle shape of K_p;
  - J4 additionally uses closed sections and (TC);
  - J1 uses neither (TC) nor closed sections (§4 S1).
- "No result here says T1 is uncoverable" is correct.

## Scripts (`REFEREE_PP11_py/`)

| file | content |
|---|---|
| `ref_skeleton.py` → `ref_skeleton.out` | The abstract implication skeleton of Theorem J (n = 5), with clause ablations (TC, UND, EDGE, FWD) and the exact Φ^κ demonstration of §4 S1 |
| `rerun_t2.py` → `rerun_t2_e1_3_e1_1_u_3_u_1.out`, `rerun_t2.log` | Referee copy of PP11's `t2_threshold.py`. Output is identical to the archived `orig_t2.out` in all four settings |

**Housekeeping.**
- Re-running `PP11_py/t4_geometry.py` in place rewrote `PP11_py/t4_geometry.out` with **byte-identical** content (180/180).
- A stray copy of the t2 output, written into `PP11_py/` because `modules.py` rebinds `HERE`, was moved into `REFEREE_PP11_py/`.
- `PP11_py/` is otherwise untouched.
