# PP36. Joint search for defence worlds and replacement dominators on the forced-defence family

22 October 2026. One author; not refereed.

**Labels.** PROVED: complete argument given here. CHECKED: exact finite computation in rational arithmetic on the cell models below. CONJECTURE: unproved. No NUMERICS were used. Finite results are diagnostics only: cells have no measure and no sections, and they say nothing about (S).

**Scripts** (`r9/PP36_py/`; run `python3 -B <script> <args>` inside that folder; outputs are in the `.out` files):

| Script | Content | Label |
|---|---|---|
| `cells36.py` | Directions, radial pieces, cone-structured exact coherence, catalogue; `refined()` adds wedge directions | CHECKED |
| `engine36.py`, `verify36.py` | PP21's rules I–IV and F1/F2, with rule II vectorised. Identical to PP21's engine on 400/400 random family request sets; 0 definition-level violations | CHECKED |
| `family36.py`, `base36.py`, `solver36.py`, `joint36.py` | The family, the self-domination base, and the joint greedy search with all obligations | (library) |
| `exp_selfdom.py` | T as the replacement dominator (§3) | CHECKED |
| `exp_rules.py` | Joint runs under w-rules (§2) | CHECKED |
| `exp_retreat.py` | Census of retreat dominators (§4) | CHECKED |
| `exp_kill.py` | The competitiveness kill (§5) | CHECKED |
| `exp_rounds.py` | The repeatable extension, round by round (§6) | CHECKED |
| `exp_split36.py` | Finer radial splitting (§7) | CHECKED |
| `exp_fills.py` | Probe: dominators for the fills X (§8) | CHECKED |

---

## 0. Verdict

**The defence world matters little. The replacement dominator carries the whole design problem, and it is constrained by one mechanism.**

1. **Where the defence world is forced (PROVED, Lemma 1).** For the record (G, S → V_j), T's defence is automatic, by guidance, at every non-j world at which V_j is wrong throughout G. A genuine choice exists only when G meets **both** classes other than M_j. On cells, all 8 rules for the three two-class free patterns close cleanly at stage 0 (CHECKED). Nothing found depends on that choice.
2. **T can be the dominator, locally (PROVED + CHECKED, Prop SD).** Write E′ := E ∩ {V_j not w-correct}. If E′ is non-null, T itself dominates Z. One inert request set does this for every such Z, every G and every w-rule at once. If E′ is null, Z is a **pure retreat** V_j[G∖E → S], and no model silent on G∖E can dominate it, T included (Lemma E).
3. **Retreat dominators must answer like V_j (PROVED, Lemma E).** A dominator of V_j[G′ → S] gives V_j's answer on a non-null part of G′, so on the cones through it. On cells the survivors are other vertex models (when G′ lies in their common majority class), precise models near e_j, tightenings and crossings (CHECKED census).
4. **The obstruction (PROVED, Prop K).** Suppose N dominates Z = C[G → S, E → w-correct]. Then D ⋠_i N for every model D that Z beats pointwise at world i. For a vertex family this means: D errs at world j on the piece where Z was corrected. On cells this two-request kill is exactly what stops D ⪯_i T on the self-domination base: 6,303/6,303 and 5,254/5,254 cases agree (CHECKED). Consequences:
   - **No single dominator may serve rivals whose answerers dominate some selected model at every world of its support** (Cor K2).
   - In particular, **T cannot be the universal replacement dominator** once any selected model errs inside Sil(T) at every world of its support. Every precise non-vertex model does (Cor K3).
   - One precise model is pointwise no worse than a **distinct** precise model at one world at most (Lemma P1). So "one precise answerer, at one defence world, per dominator" is safe from Prop K.
5. **Joint runs (CHECKED, §6).** The stage-0 family (vertex family plus all retreats, with every registered defender competitive on full support) closes cleanly on the refined cells under the rule "one answerer per dominator". It fails at stage 0 when T dominates everything. Every recorded stuck point has a deletion-minimal failing set of 1 or 2 requests, of three shapes only:
   - exposure (Lemma E / PP21 Lemma 0.4);
   - the Prop K kill;
   - cross-exposure against another protected model.
6. **Splitting.** Twin and radial splitting preserve every failure (PP21 Lemma 2.2; CHECKED on 4 radial pieces). Refining **directions** near the planes e_j^⊥ makes things worse: "precise near V_j" dominators disappear, and the universal-T failure moves from round 1 to round 0.

**Nearby reachable targets.** "One dominator for everything" is out. Two variants survive Prop K, and both can be stated measurably:
- **(A) Colour dominators by answerer and defence world.** Each dominator serves the rivals of one answerer at one world. T may serve at most one vertex family. This is PROVED Prop K-safe for precise selections. Its answerer-only form is CHECKED clean at stage 0 on the refined cells. Its next obstacle is cross-exposure at round 1.
- **(B) Keep T as the universal dominator** of genuine Z, and require every other selected model to be **error-free inside Sil(T) at some world of its support**. Examples are credal sets containing a vertex e_i, and coarsenings K ⊇ M. On cells this condition is exactly the survival criterion (CHECKED: exact on all 2,152 and 1,784 models tested). It is incompatible with PP30's Ans(T)-kept geometry, which forces precise boundary models.

---

## 1. The model

**Directions** (`cells36.py`). As in PP21: ε = 3/10, c = 7/30, T = D_M. For each class k there are five silent directions, obtained by permuting a class-1 template:

| Name | Class-1 template | Role |
|---|---|---|
| Gp | (−6/5, 1, 1) | axis; uniform prior gives the majority answer |
| Gm | (−3, 1, 1) | axis; uniform prior gives the minority answer |
| Kp | (−17, 3, 23) | PP30's kill directions h±, steep |
| Kq | (−17, 23, 3) | PP30's kill directions h±, steep |
| F | (−9, 9, 1) | PP28's steep padding line ℓ_F |

Further directions:
- J_k (T answers the majority);
- W_k (T answers the minority);
- U (unanimous).

The **refined** model adds six wedge directions Y (g_j = −1/10, the other two coordinates 1 and −1/2). They lie in Sil(T), close to e_j^⊥ and away from u^⊥. On them, precise models off e_j disagree with V_j.

**Radial splitting.** Every mixed direction is split into the bounded pieces .0 and .1 and the unbounded outer piece .i. A bounded G is a union of .0/.1 pieces. Coherent models take one value per direction (cone structure, Lemma H on cells). Coherence of the direction vector is decided exactly by PP21's clipping test and meet-closure catalogue, which agree on all samples.

| Model | Directions | Cells | Coherent direction vectors |
|---|---|---|---|
| standard (std) | 22 | 64 | 19,486 |
| refined (ref) | 28 | 82 | 114,180 |
| fine radial (4 pieces) | 22 | 85 | 19,486 |

**Family** (`family36.py`). For each V_j and each G (single pieces, both bounded pieces of a direction, cross-class pairs, same-class pairs, one-per-class triples), and each E ⊆ G (single pieces and E = G):
- X = T[G ↦ V_j], R = V_j[G ↦ S], Z = R[E ↦ w-correct];
- the defence T R_w X is requested at the rule's world;
- **every** world at which the record ends up accepted, by rule or by guidance, spawns its Z's.

The family has up to 690 records and 2,415 Z's.

**Obligations** (`joint36.py`):
- (i) the defence;
- (ii) a coherent dominator for every Z at every accepting world, and for every retreat R (KKM applies to every incoherent model);
- (iii) T competitive against every member of P and every rival;
- (iv) every registered defender D_K competitive against T, V_1–V_3, the other registered defenders, and every rival X, R, Z.

**Stated support:** each registered defender is declared selected at an interior index of its credal set, so its support is all three worlds. Every cell pattern is realised by a credal set with interior, since all constraints are strict. Full support is the most permissive choice for (iv); edge supports only remove worlds.

**Rounds** (`exp_rounds.py`). Round r + 1 adds, for every defender D registered so far:
- **its own forced family** (Theorem 3.1 with D_p := D): T R_w T[G′ ↦ D] for bounded G′ ⊆ Sil(T) where D answers, with the corresponding Z′ and retreats D[G′ ↦ S];
- D's forced defences against D[G′ ↦ V_j] on D's silence outside Sil(T). Inside Sil(T) these are the same records as T's, by (IB).

The search is greedy with the PP21 closure. Options are tried in this order:
- existing members of P;
- catalogue models ordered by Hamming distance to the rival, up to 400 per obligation.

A new dominator is accepted only together with a clean T-defence against it. Greedy is incomplete, so "stuck" is never a proof of infeasibility.

---

## 2. The defence world

**Lemma 1 (where T's defence is automatic; PROVED).** Fix V_j and G ⊆ Sil(T) bounded, and let {j, k, l} = {1, 2, 3}. V_j says B on M_j, which is wrong at k and at l. It says A on M_k (wrong at k, right at l) and A on M_l (right at k, wrong at l).

So the record (G, S → V_j) is:
- a pure improvement at j, so T never defends there;
- guidance at k iff G ∩ M_l is null;
- guidance at l iff G ∩ M_k is null.

Hence:
- G ⊆ M_j: T defends at **both** k and l automatically, and Theorem 3.1 applies at both;
- G meets M_k but not M_l: T defends at k automatically;
- G meets both M_k and M_l: there is no guidance world, and T must accept a non-guidance record at k or at l. **This is the only genuine choice.** In pattern form the free cases are {kA, lA} and {jB, kA, lA}, three of each.

A rule may add a mixed world on top of a guidance world, but that only creates more Z's. It never helps.

**CHECKED** (`exp_rules.out`, family of single pieces, same-direction pairs and cross-class pairs, retreats included, all obligations):
- all 2³ choices for the three {kA, lA} patterns close cleanly, with |P| = 7–10;
- dominators: T for the 750 genuine Z's; for the retreats, precise models near the vertices or another vertex model.

With triples, the self-domination system (§3) closes for the three rules tested: all-low, all-high and alternating (`exp_selfdom.out`).

**Pattern:** w is a function of how G is spread over the classes:
- **the non-j class G meets, if it meets only one;**
- either non-j world if G ⊆ M_j (both are then forced);
- free if G meets both.

No cell evidence prefers either free choice. Prop K below does not involve w at all: the kill happens at the answerer's world j.

---

## 3. T as the replacement dominator

**Prop SD (self-domination; PROVED).** Let Q contain:
- for any set of records ρ = (G, S → V_j) with G ⊆ Sil(T) bounded, each assigned any non-improving world w(ρ), the requests T R_{w(ρ)} X_ρ;
- one request T R_{w_j} V_j (w_j ≠ j) per vertex;
- T R_i Z at every world i, for every Z = V_j[G → S, E → w-correct] such that the record is accepted at w and E′ := E ∩ {V_j not w-correct} is non-null.

Then Q satisfies (a)–(c) of PP21 Lemma 2.3 with P₀ = {T, V_1, V_2, V_3}. So Guid ∪ Q is closed under I–IV with neither F1 nor F2. T strictly dominates every such Z, and V_j ⋠_w Z (Theorem 3.1(b)) holds.

*Proof.* All conditions are pointwise a.e. conditions on pairs of records.

- **(a) No requested record is a weak improvement.**
  - rec(T, X) at w: by choice of w.
  - rec(T, Z) at j: it worsens on E′, where the w-correct answer is j-wrong.
  - rec(T, Z) at i ≠ j: it worsens on Sil(T) ∩ M_i ∖ G, where V_j says A, which is i-wrong. This set is a non-null cone minus a bounded set.
  - rec(T, V_j) at w_j: it worsens on Sil(T) ∩ M_{w_j}.
- **(b) Compositions.** Copies of two requested records compose only in these cases:
  - (rec(T, X₁), rec(T, X₂)) with G₁ ∩ G₂ null. The inverse composite moves answers to S on G₁ ∪ G₂. It is guidance only if both answers are w-correct, which would contradict (a).
  - (rec(T, X₁), rec(T, Z₂)), in either order, with G₁ ⊆ G₂ ∖ E₂. Otherwise Z₂, which equals V_{j₂} on Sil(T) ∖ G₂, differs from S on G₁. The composite is rec(T, Z₂[G₁ → V_{j₁}]). Its inverse is guidance at w′ only if V_{j₂} is w′-correct on Sil(T) ∖ G₂, which forces w′ = j₂. But at j₂ it fails on E₂′.
  - Two rec(T, Z) never compose, because Sil(T) ∖ (G₁ ∪ G₂) is non-null.
  - rec(T, V_j) composes with nothing requested: V_j answers on all of Sil(T).

  No inverse composite is requested either, since every requested record has old side T on its support.
- **(c) Rule III.** The only records accepted at all three worlds are the rec(T, Z). Such a record ends at V_j only if Z = V_j on its support, which E′ excludes. It ends at V_i (i ≠ j) only if V_j = V_i on Sil(T) ∖ G, which is false. It never ends at T.

Strictness: rec(Z, T) is neither guidance nor requested at w, because it mixes the gain on E with V_j's w-errors. Finally, rec(V_j, Z) at w improves on E′, so it is neither guidance nor requested, and the refusal of Theorem 3.1(b) stands. ∎

**Lemma E (exposure; PROVED).** Let C be coherent and in P, and let G′ be bounded, with C answering a.e. on G′.

- **(i) Retreats.** Every dominator D of R = C[G′ → S] answers on a non-null part of G′. Otherwise rec(D, R) ends at C, and rules III/IV register the non-conic splice D[G′ → C]: F2 by Lemma H. If C = V_j, D is moreover j-correct, i.e. gives V_j's answer, on a non-null part of G′. Otherwise rec(D, R) is a weak j-improvement, since R is j-perfect off G′ (F1). In particular **T never dominates a retreat**. This covers the Z with E′ null: they are V_j[G ∖ E → S].
- **(ii) Fills.** Every dominator D of X = T[G → C] differs from C on a non-null part of G. Otherwise rec(D, X) ends at T, and D[G → S] would be registered (F2), or the record is a pure improvement at a world where C is right on G (F1).

**CHECKED** (`exp_selfdom.out`, 2,415 Z's including triples, under rules all-low, all-high and alternating):
- "T dominates Z alone iff E′ is non-null" matches 2,415/2,415. The 450 failures have 1-request minimal sets (F1, or F2 via an all-world tie with V_j); derivations are printed.
- With all defences, T dominates all 1,965 genuine Z's in one closed system: clean, **inert** (0 records added by rules II–IV), and 0 definition-level violations.

---

## 4. Who dominates the retreats (CHECKED, `exp_retreat.out`)

The test runs on the self-domination base (with T R V_j at the cyclic worlds). For 57 representative retreats (45 single-piece types and 12 two-class ones), each candidate must pass:
- dom(C, R);
- T R_w C at some world;
- C R_w T at some world.

The pool has 464 models: all precise models, the vertices, and a sample of the catalogue.

- **Every survivor gives V_j's answer on G′** (1,976 survivor–retreat pairs). On single directions it does so on all of G′ (cone structure). On two-class G′ it does so on all of G′ (1,514 pairs in total) or on part of it (462), as Lemma E predicts.
- **Survivors by kind.**
  - Precise models agreeing with V_j on every Sil(T) cell ("pV"): 3–4 for every retreat.
  - The other vertex model V_i, when G′ lies in M_l (l ∉ {i, j}), the class where V_i and V_j both say A. This appears for two of the three families (V_3 for V_2's retreats, V_1 for V_3's). The third is blocked by a two-link F1 with T's chosen world against V_i.
  - Other precise models (135 pairs).
  - Tightenings (0–6 per retreat) and many crossings.
- **K is genuinely variable here.** Several kinds always survive. But the pV survivors are a cell artefact (§7): in the continuum no precise λ ≠ e_j agrees with V_j on all of Sil(T).

---

## 5. The competitiveness kill

Write C ⊵_i D if C is pointwise no worse than D at world i, a.e.

**Prop K (PROVED).** Let N ⪯_i Z with Z = C[G → S, E → w-correct]; for example, N dominates Z. Suppose:
- C ⊵_i D off G;
- D is not i-correct a.e. on G ∖ E;
- D is i-wrong a.e. on the part of E where the w-correct answer is i-wrong;
- D ≠ Z on a non-null set.

Then D ⋠_i N.

*Proof.* Z ≤_i D pointwise and strictly somewhere, so Z ≺_i D by strict (G). D ⪯_i N ⪯_i Z ≺_i D violates (TC). ∎

**Cor K1 (vertex families; PROVED).** Take C = V_j, a bounded single-class piece G ⊆ Sil(T) on which D is j-wrong, E = G, and w a guidance world of (G, S → V_j). There V_j's answer is w-wrong, so the w-correct answer is j-wrong. Then **any dominator N of this Z satisfies D ⋠_j N**. V_j ⊵_j D holds for every D.

**Cor K2 (one dominator cannot serve everything; PROVED).** Assume (S). Let D be selected at an index with support s, and for each i ∈ s let D be i-wrong on a non-null part of Sil(T). Build Z_i by Cor K1 on a piece of that set. Each Z_i is incoherent (Lemma H), so it has a selected dominator N_i by KKM, and D must be competitive against every N_i. By Cor K1, **the N_i (i ∈ s) are not all the same model.**

**Cor K3 (precise models; PROVED).** For λ ≠ e_j, D_λ is j-wrong on a non-null part of Sil(T) ∩ (one class).

*Proof.* D_λ and V_j disagree on the open double wedge between λ^⊥ and e_j^⊥.
- If λ is not on the median through e_j, the wedge meets u^⊥ ∖ {0} ⊆ Sil(T) in an open sector.
- If λ is on the median, the two planes meet in a line of u^⊥. Every neighbourhood of that line meets the wedge, and Sil(T) is an open cone containing u^⊥ ∖ {0}. ∎

Hence, if one model N dominates all the genuine single-piece Z's of all three vertex families, then **no precise non-vertex model can be competitive against N**. With N = T, or any selected N, (S) fails at every index carrying such a model. In particular it fails at the edge indices of an Ans(T)-kept system (PP30 Cor 5.4; edge values are not vertex-valued, REFEREE_round46 §2.3). The same holds for any dominator serving two vertex families j, k against an edge model on [e_j, e_k].

**Lemma P1 (PROVED).** For distinct precise models C = D_λ and D = D_μ, C ⊵_i D holds for at most one world i.

*Proof.* Suppose C ⊵_i D and C ⊵_{i′} D with i ≠ i′, and let i″ be the third world.
- **Signs on the disagreement set.** Let W be the open double wedge where the answers differ. On W, C's answer is correct at both i and i′. An answer correct at both worlds exists only where g_i and g_{i′} have the same sign.
- **Where W can lie.** Each half of W is a connected lune with vertices ±g*, where g* spans λ^⊥ ∩ μ^⊥. So it lies in one of the two antipodal regions {g_i, g_{i′} > 0} and {g_i, g_{i′} < 0}. Their closures meet only on the line ℝe_{i″}. Hence g* ∥ e_{i″}, that is, λ_{i″} = μ_{i″} = 0.
- **Contradiction.** Then λ·g and μ·g depend only on (g_i, g_{i′}), and they have the same sign wherever g_i g_{i′} > 0. So W ⊆ {g_i g_{i′} < 0}. ∎

**Prop K with D = C.** If Z ≺_w C by strict guidance, and N ⪯_w Z, then C ⋠_w N. Every Z built at a *guidance* world w of C's own record is such a strict w-improvement of C: C is w-wrong on all of G, and Z puts S or the w-correct answer there. So **one model must not dominate C's own Z's at every world of C's support.**

So suppose each dominator serves the rivals of **one** precise answerer **at one defence world**. Then it kills at most one world of each precise D: for D ≠ C by Lemma P1, and for D = C by the remark above. Prop K therefore never blocks a model whose support has at least two worlds. Vertex answerers kill only their own world. **Imprecise** answerers can kill two worlds: take C = D with D's minority answers removed.

**CHECKED** (`exp_kill_std.out`, `exp_kill_ref.out`). On the self-domination base, D R_i T was tested for 2,152 (std) and 1,784 (ref) coherent models at every world.
- The engine verdict equals Prop K's pointwise criterion in **6,303/6,303** and **5,254/5,254** cases.
- **D keeps a free world iff D is error-free inside Sil(T) at some world** (std 972 + 1,180, ref 240 + 1,544, with no exceptions).

Survivors:

| Kind | std | ref |
|---|---|---|
| vertices | 3/3 | 3/3 |
| coarsenings | 7/7 | (none in sample) |
| precise non-vertex | 15/163 (all of them cell artefacts agreeing with a vertex on Sil(T)) | **0/283** |
| tightenings | 71/491 | 21/642 |
| crossings | 813/1,341 | 203/804 |

---

## 6. Joint runs and rounds (CHECKED, `exp_rounds_*.out`)

The family uses single pieces and same-direction pairs (crosspairs too at stage 0, std), rule all-low, with retreats. All obligations of §1 are on, including defender competitiveness on full support.

| Model | Dominator policy | Outcome | Minimal failing sets at the stuck point |
|---|---|---|---|
| std | free (T first) | stage 0 clean; **round 1 stuck**: defender D4 (precise; equal to V_1 except B on F2 and T's answers on J1, W2, W3) cannot meet D4 R_w T | 2 requests at each world: dom(T, Z[V1:F2.0, w2]) + cmp D4 R_1 T, and the analogues with V_2, V_3: **Prop K** |
| std | T barred | round 1 stuck: D4 R_w V3 | 2 requests: V3 serves families of V1 and V2 → **Prop K** at worlds 1, 2 |
| std | one vertex family per dominator | stage 0 clean (|P| = 9, inert); round 1 stuck: D6 R_w T | **Prop K** through near-vertex answerers D2, D3 (≈ V2, V3 on cells) |
| std | one answerer per dominator | stage 0 and round 1 clean; **round 2 stuck** (|P| = 19 entering round 2) at a dominator for a defender's retreat | 2 requests: **cross-exposure** (an existing domination record ends at the candidate; F2 by rule IV), or two-link F1 |
| ref | free (T first) | **stage 0 stuck**: D1 R_w T | **Prop K** through the wedge cell Y1a (world 1). At world 2, the same (TC) triangle with T's own defence T R_2 D3 in place of a domination (D3 ≺_2 D1 by guidance) |
| ref | one vertex family per dominator | stage 0 clean; round 1 stuck at a retreat of a precise defender | 2 requests: **cross-exposure** |
| ref | one answerer per dominator | **stage 0 clean**: |P| = 16, 0 records added by rules II–IV, 630 rivals; round 1 stuck | 2 requests: **cross-exposure** (e.g. rec(D6, Z[V3:Kp1.0]) ends at the candidate for R[D5:Gm1.0]) |

Two features of the clean stage-0 solution on ref under (A):
- T dominates the genuine Z's of a single vertex family (105).
- All 12 new defenders are precise, or nearly precise, separated models, each serving one answerer, and **none agrees with a vertex on Sil(T)**.

Every stuck point has a 1- or 2-request minimal failing set of one of the shapes exposure, Prop K or cross-exposure (PP21 §4 "exposure against another protected model"). No deeper derivation and no non-inert clean closure occurred.

---

## 7. Further splitting

- **Twin and radial splitting.** By PP21 Lemma 2.2 every failure and every clean closure lifts verbatim. CHECKED on 4 radial pieces (85 cells, `exp_split36.out`):
  - T against a retreat fails (F1, and F2 via V2) on single fine pieces;
  - a tightening agreeing with a fill on G fails (Lemma E(ii));
  - 77/77 precise D that are 1-wrong on F2 lose D R_1 T after T dominates V1[F2.2 → w-correct] (Prop K);
  - the self-domination system stays clean and inert (315 defences, 840 dominations).
- **Refining directions.** This changes the picture:
  - in std, 5 precise models per vertex look like V_j on Sil(T);
  - the six wedge directions remove them all (only V_j itself remains);
  - Prop K then kills every precise non-vertex model (0/283);
  - the universal-T failure moves from round 1 to round 0.

  This matches Cor K3: the std survivors were cell artefacts.
- **What persists.** The three failure shapes persist. Prop K and Lemma E are measurable statements. Cross-exposure is a pairwise pointwise condition (PP21 Lemma 2.3(c)). Whether it is forced, or only a greedy artefact, is not decided.

---

## 8. Continuum implications the cells omit

1. **Closed sections are not modelled.** Cells cannot test "p ∈ cl{q : C_q R_i Z} ⇒ C_p R_i Z". Under (A) each answerer C needs its own dominator N(C). As C varies continuously along a fibre, the sections {p : C_p ⪯_i Z} must be closed for each fixed Z. PP30 Prop 4.2(c) keeps them away from e_j. Nothing here checks closedness. Under (B) no new defender is registered for genuine Z, so the only new sections are T's own (closed if T's fibre is closed, LEAD Lemma A). The retreats still need answer-like dominators.
2. **Measure.** E cannot be made arbitrarily small on cells. Prop SD, Lemma E and Prop K are pointwise and hold for every non-null E.
3. **Wedges.** The std cells miss the disagreement wedges of precise models near vertices (§7). Any cell model without directions near e_j^⊥ ∩ Sil(T) overstates what precise dominators can do.
4. **Fills.** KKM also demands dominators for every fill X = T[G ↦ V_j]. By Lemma E(ii) they must disagree with V_j on G and compensate elsewhere, which is PP21's territory. They are omitted from the runs above, except one probe (`exp_fills.out`).
   - It sticks at the second fill, T[Gp2.0 ↦ A], after 10 steps; 403 of the 404 candidates fail.
   - Of the first 80 candidates:
     - 60 fail by a 2-request **cross-exposure** with the tightening T[Gp2 ↦ A] chosen for the first fill;
     - 19 fail by 1-request exposure (Lemma E(ii));
     - 1 fails by a two-link F1.
   - Fills need their own colouring. That is not attempted here.
5. **Other selected models.** Only T, the vertex models and registered defenders are in P. Edge selections, and the full KKM over all models, are not imposed. Cor K2 and K3 are where they enter.
6. **Search.** Greedy with a 400-candidate cap is incomplete. The catalogue is finite, and imprecise K's appear only through their cell patterns.

---

## 9. Patterns for the measurable construction

**P1 (defence world; PROVED).** w(ρ) = the unique non-j class that G meets, when there is one. If G ⊆ M_j, both non-j worlds are forced. If G meets both non-j classes, the choice is free. Prop SD holds for every choice, and Prop K does not see w.

**P2 (genuine Z; PROVED locally).** For E′ non-null, T is a valid dominator, all at once and inert. Globally, Cor K2 decides how far this can go:
- if T serves the genuine Z's of families j and k, no selected model on the edge (e_j, e_k) may err inside Sil(T) at both j and k. Precise non-vertex edge models do (Cor K3). So with precise models on all three edges, T serves **at most one** vertex family;
- in general, T may serve a set of answerers only if every selected model keeps a world of its support that none of them kills.

**P3 (retreats; PROVED shape, CHECKED kinds).** The dominator of V_j[G′ → S] gives V_j's answer on part of G′, and it is not V_j itself, which would expose T.

V_i works when G′ lies in the common majority class of V_i and V_j. Otherwise use a precise model D_λ, at a rival-dependent positive distance from e_j (PP30 Prop 4.2(c)), whose wedge with e_j misses part of G′, or a tightening answering like V_j on the cones of G′.

**P4 (the invariant to prove; CONJECTURE).** Rule (A):
- assign to each rival family its own dominators N(C, w), indexed by the answerer C (V_j or a registered defender) and by the defence world w;
- use T for at most one vertex family;
- choose N(C, w) for retreats as in P3, and freely for genuine Z's.

Invariant: **for every selected D and every selected dominator N, the worlds killed by Prop K miss a world of supp(D).** Here the killed worlds are κ(N, D) := {i : some Z served by N satisfies Z ≺_i D pointwise}.
- For precise answerers and precise D, |κ| ≤ 1, by Lemma P1 and the remark after it. So the invariant holds whenever |supp D| ≥ 2.
- At a vertex index it holds by guidance.
- Imprecise answerers need |κ| ≤ |supp D| − 1 checked separately.

The stage-0 runs used "one answerer per dominator" without the world index. Answerers there are vertex models, for which the index is irrelevant. The world index starts to matter from round 1, which the runs reached only partly.

What remains open, in the order the runs met them:
1. **Cross-exposure.** No accepted all-world record rec(N₁, Z₁) may end at another protected N₂. In pointwise form: N₂ ≠ Z₁ on supp rec(N₁, Z₁).
2. **The recursion.** Each new precise defender brings its own retreats on its wedge with the nearest vertex; their dominators must answer like it there (Lemma E). These answers are j-wrong for that vertex, which pushes the next dominators away from e_j, not toward it.
3. **Sections** for the family N(C) as C varies.

**Alternative (B) (CONJECTURE).** Keep T as the dominator of every genuine Z, and select only models that are error-free inside Sil(T) at a world of their support:
- vertex-anchored credal sets (e_i ∈ K), e.g. edge values [e_i, μ];
- coarsenings K ⊇ M.

Prop K then never applies, and on cells this criterion is exact (§5). The price is PP30 Cor 5.4: such a system cannot keep S_0 on Ans(T), whose edge values must be precise.
