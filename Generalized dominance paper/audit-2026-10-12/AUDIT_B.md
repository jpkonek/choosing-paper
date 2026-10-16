# Audit B: the edge, fineness, counting and cancellation toolkit under a v19-type domain

Auditor B, 12 Oct 2026. The source files are in `/mnt/user-data/uploads/Generalized dominance paper/`. Abbreviations:

| Abbr. | File |
|---|---|
| CCF | Closed Choice Forces Fineness |
| ECS | Edge Cycles and Separability |
| IC | Independence Chains |
| DT | Dense Thresholds and Debt Reduction |
| TAW | Two Additive Worlds Without Completeness |
| FSE | Fineness Spreads Along Edges |
| FFN | Fineness for Any Finite Number of Worlds |
| TCR | Three Complete Rankings Cannot Cover |
| CRANW | Complete Rankings for Any Number of Worlds |
| IRWAS | Independent Rankings Without Additive Structure |
| CSE | Conditional Shunning of Error |
| IRC | Incomplete Rankings and Coverage |

## 0. What I read

- **Read in full:** CCF, ECS, IC, DT, FFN, TCR, IRWAS and CSE.
- **TAW (3202 lines):** read lines 1–840 (setting, inputs, preliminaries, separability) and 1343–1642 (silent targets and Theorem I) in full. Also read the main theorem and remarks (3040–3202). I did *not* read the routing primaries (822–1342), the one-sided case (1643–1715) or the finitely additive sections (1716–3043). For those I rely on the hypothesis audit in TAW's own Remark `rem:uses` (3127–3156).
- **FSE (2732 lines):** read lines 1–1233 in full. That covers the tools, edge transfer and one fine world. Also read Lemma `leading`, Lemma `FC` and Theorem `tame` (1730–1872), the low-cone section (2048–2232) and Proposition `GC` / Theorem `ECC` (2353–2460). For the fine-edge section (1229–1455), the AExt section (1894–2035) and the shape section (2533–2677) I read the statements only.
- **CRANW (1634 lines):** read the setting, Lemma `regions`, the inputs (1–504) and the main results and remarks (1415–1634). I did not read the proofs in Sections 3–6 (LH, own-region, dichotomy, rich, counting; 505–1414). Those sections are stated to be n-world versions of FSE and TCR arguments, which I did read.
- **IRC (3723 lines, 46 pp.):** read the summary (51–183) and the setting and tools (185–870) in full. Also read the whole cancellation block: change vectors, Lemma `accept`, Theorem `NC`, Corollaries `NCext` and `NCclasses`, and Lemma `smallcanc` (2043–2440). I read the definition of Conf(θ) (2536–2575). For every other theorem I read the statement only: `EP`, `onecomplete`, `SCext`, `SC`, `T1otools`, `LH`, `A`, `B`, `conf`, `confT1`, `Ts`, `SACo`, `Astar`, `Bstar`, `crossing`, `twoNC`, Corollaries `C` and `refined`, and Proposition `F4`. I did not read the proofs from 870–2040 or 2440–3723.
- **Dependency files I did not read:** CBOI, CC (the face lemma), EDL, FAED, Lemma 1 of CBOI (KKM) and v3's Appendix C. Verdicts that depend on them are marked UNCLEAR where it matters.

## 1. Structural facts about a v19-type domain

These are proved here because every verdict below depends on them. Notation: K is the proper open convex cone of the brief (called V there). I write K to avoid a clash with the vacuous model V.

**F0. Reducing to K = R^n.** If K = R^n, then M_L is all models and non-tangency is vacuous. Every result below then **SURVIVES verbatim**. Everything that follows concerns a proper K, that is, K ≠ R^n.

**F1. The domain is the set of sub-models of one coherent model.**
- *K and −K are disjoint.* If h and −h both lay in K, convexity would put 0 in K, and then K = R^n (v19 `lem:zero-in-V`).
- *At most one option per problem.* So on each binary problem {g, −g} at most one acceptance is admissible. Domain models are therefore **never contradictory**, and on every problem they choose between "silence" and "the one admissible option". The admissible option exists exactly when g or −g lies in K.
- *Credit and debt regions are fixed.* At world v, put Cr_v := {problems whose admissible option is good at v} and Db_v := {problems whose admissible option is bad at v}. These are disjoint, and they are fixed by K. A domain model can give credit at v only on Cr_v and debt at v only on Db_v. It must be silent on the problems with no admissible option.
- *The dual credal set M_K.* Let M_K := {q ∈ Δ : q·h ≥ 0 for all h ∈ K}. It is nonempty, closed and convex, and it lies in int Δ. (K is open and contains each e_i, which gives q_i > 0.) W := K is then the open part of the coherent model D_{M_K}.
- *Which coherent models are in the domain.* A coherent D_M lies in the domain a.e. iff M ⊇ M_K. Proof: an open cone is a.e. inside the open convex W iff it is inside W; then take duals.
- *Consequences:*
  - Every coherent model whose credal set lies in a proper face Δ_S (S ≠ Ω) is **outside** the domain. This covers D_i, edge models, V_{1j}, B_θ and any credal set in a face.
  - A precise model D_p is in the domain only if K is exactly the half-space {p·h > 0}. Even then it is tangential.
  - V is in the domain and is non-tangent.

**F2. A relative face lemma.** Assume strict (G) at the worlds of S = supp p, applied only to domain models, and S ≠ Ω. Then every domain model C competitive on S against domain models satisfies two conditions:
1. C ⊇ K ∩ {h_S ≫ 0} a.e.;
2. C ∩ {h_S ≪ 0} is null.

Proof: put X := (C \ {h_S ≪ 0}) ∪ (K ∩ {h_S ≫ 0}). X lies in the domain. At every i ∈ S, X's advice is pointwise at least as good as C's: added acceptances are good at every i ∈ S, and removed ones were bad or contradictory there. It is strictly better wherever (1) or (2) fails, so X ≺_i C for all i ∈ S, and C is not competitive on S.

Consequences:
- M_K ⊆ cred(C_p) ⊆ conv(M_K ∪ Δ_S).
- At the vertices, **C_{e_i} = D_i ∩ K =: D_i^K**, uniquely.
- The open set {h_S ≫ 0} meets ∂K. Otherwise it would lie inside K, and cl K would contain −e_k for k ∉ S, which with e_k ∈ K forces K = R^n. Hence cl C_p contains nonzero points of ∂K.

So **non-tangency fails for every C_p with supp p ≠ Ω**. Read literally, the brief asks that every selected C_p be non-tangent. That requirement is **inconsistent with (S) plus strict (G)** unless K = R^n. Below I therefore read "non-tangency" as applying to C_p with p in int Δ. Boundary selections are then tangential and fixed by F2.

The same argument repairs IC/TAW (K4): "V undominated implies V competitive on all worlds". V is tied with some C_p and is therefore competitive on supp p. F2 then forces supp p = Ω, because V ⊉ K ∩ {h_S ≫ 0} when S ≠ Ω.

**F3. What breaks.** The original face lemma (CC Lemma 7; used as IC §1, TAW (K3), FSE §1.1, TCR §2.1, CRANW §2.1, IRC §2.1) is false in a proper domain. Every note in my set rests on its consequences:
- C_{e_i} = D_i;
- edge selections are "edge models" (α, β): credit at v where t^v_w > α, silence between the two thresholds, debt where t^v_w < β;
- the endpoint families E_j(b) and E^j_1(a), and V_{1j};
- (EP_{ij}), "two-sided" selections, germ points, far ends.

In the domain, an edge selection is some D_M with M_K ⊆ M ⊆ conv(M_K ∪ [e_v, e_w]). Its advice on D_{vw} depends on every coordinate, not on t^v_w alone. These selections do not form a one-parameter, totally ordered family. None of the threshold machinery has a domain counterpart without new work.

**F4. What transfers.** A great deal of the toolkit is pure order algebra from (G), (IB) and transitivity:
- the debt/credit orders ⪯_d and ⪯_c, SI/AC pairs and their composition;
- ideals J_A and K_T, ultrafilters, fineness;
- Savage–Wakker comparative probability, the exchange rate and the weak extension;
- the counting lemma, lightness composition and sweeps;
- finite cancellation (NC) and the (FC) group primary.

All of it transfers if three repairs are made:
1. Debt sets at v are chosen inside Db_v, and credit sets inside Cr_v.
2. The ideal model D_v is replaced by D_v^K. D_v^K is the pointwise-best domain model at v and the vertex selection; W_1 (debt everywhere) is replaced by the domain model accepting everything in Db_1.
3. A "full change from credit to debt on W" is replaced by "change from D_v^K's advice to D_w^K's advice on W". These two models agree off D_{vw}, as needed. A credit and a debt option on the same problem never coexist in the domain.

**F5. Near versus far.** By F2, the boundary selections D_i^K jointly cover K. So "near the selected family" places no restriction inside a v19 domain. The real issue is that the selected families the proofs presuppose (face-lemma edge models, D_i) are not in the domain.

Within the original proofs, the auxiliary models fall into five classes:
- **(A) Local edits** of a selected model or of V on chosen sets: silencing, or adding one option. These are in the domain iff the added options are admissible, and that is repairable by intersecting the sets with Cr or Db. Examples: CCF Y and F; IC chain-lemma X, X′, Y; the IB transfers everywhere.
- **(B) Ideal-model edits.** D_v, D_w, D_v + debt_v(W), D_2 + sil(T), D_j silenced, D_1 silenced on bands, and W_1. These are far from int-Δ selections and outside the domain. Use D_v^K instead.
- **(C) Edge selections used as competitive bases or approach sequences.** E_j(s), E^j_1(a), V_{12}, two-sided (α, β), and the far-end sequences C_{q_m} → D_j. These are outside the domain and have **no threshold-structured replacement**. Almost every substantive step uses class C.
- **(D) Far KKM targets and Bayes models.**
  - DT `lem:bayes`/`thm:dense`: B_θ on [e_2, e_3] and X_j; explicitly "over all models", DT L141.
  - TAW silent targets Σ^b: debt on Θ_s ⊂ P_1, which includes problems where −g ∉ K, plus credit on all of F_b.
  - IC `prop:good`: X = D_2 silenced.
  - CSE: Bayes selections C_{e_j} = D_j.
  - IRC Conf(θ): precise selections D_p.
- **(E) Closedness or continuity assumptions at arbitrary models** beyond (S): IC path-closedness, FSE (CC-a/b), (MC), (GC), (ECC), and IRC (T1°), (T1^s), (T1^cc), (T1^cut), (E2), (SC).

## 2. Per-file audit

Verdict key, under a proper v19 domain with non-tangency read as in F2: **S** = SURVIVES, **SR** = SURVIVES-WITH-REPAIR, **F** = FAILS, **U** = UNCLEAR.

Assumptions common to every file are listed once here and not repeated. They are: binary problems on H with Gaussian μ; null-set identification; the four-rank background order; strict (G); (IB); (S) on all of Δ; and n = 3 unless stated otherwise. Most results are reductio arguments under "V undominated". That hypothesis matters only as a tool assumption.

### CCF — Closed Choice Forces Fineness

| Result (lines) | Hypotheses and extra assumptions | Models used | Verdict |
|---|---|---|---|
| Lemma `cboi` (125–136) | n ≥ 3, (G), (S), CBOI-form loss with (W_k) at every world. Extra: (c) finitely additive representation at all worlds. | CBOI Thm 2 internals (not read) | **U**: depends on CBOI's constructions. |
| Lemma `edge` (172–196) and Lemma `approach` (198–210) | (G) at worlds 1 and j, (S), (EP_{1j}). Implicit: face lemma; C_{e_1} = D_1. | D_1, D_j, E^j_1(a), E_j(b) (class C) | **F**: these models are outside the domain (F1); the face lemma is false (F3). |
| (T1), (T2) (229–238) | Closed sections and competitiveness. (T1) also needs completeness. | Any X | **S** in general form: q ∉ A_k(Y) gives C_q ⋠ Y nearby, for domain Y. |
| Lemmas `debtbands` and `creditbands` (244–310) | (EP), completeness at world 1, (IB). | Y = E_j(b) silenced on A; F = E_j(b) + debt(A), with A anywhere in {t ≥ c} (far); edge approach sequences | **F** (class C). |
| Theorem `fine` (314–386) | As above, (EP_{1j}) for all j. Extra: (b) completeness; (g) fineness is the conclusion. | Built from the band lemmas | **F**. Fineness would have to be proved on the restricted algebras of Cr_1 and Db_1 by other means. |
| Lemma `cp`, Theorem `SW`, Lemma `Pd` (400–474) | Completeness, (G), (IB) at world 1, fineness. Extra: (b), (g). | V + debt(B), V + cred(B) | **SR**: restrict the debt algebra to Db_1 and the credit algebra to Cr_1. Savage–Wakker on algebras applies unchanged. |
| SI/AC definitions, Lemma `rates`, Lemma `kappa` (478–573) | Completeness, fineness. | V + debt(A) + cred(T); T* ⊂ H′ \ (A′ ∪ A_0′) | **SR**: choose T* ⊂ Cr_1. Since Cr_1 and Db_1 are disjoint (F1), the mass bound at L535–539 simplifies to P_c(Cr_1 \ T-pieces). |
| Lemma `SIAC` (493–509) | As above. | E_j(1) + cred(Z); E^j_1(1) + debt(A) (class C) | **F** as written. **SR** if SI and AC pairs are supplied by another route, as FSE `prop:localext` does by hypothesis. |
| Theorem `extension` (575–645) | Completeness, fineness, κ. | N + debt + cred, all regular | **SR**: Λ(M) = P_d(debt M) − κ P_c(cred M) on domain models. This is the cleanest transferable tool. |
| Theorem `A` (649–669) | (EP) on all edges at world i. | | **F**: (EP) and fineness come from edges. The construction of the loss from Λ is **SR**. |
| Theorem `reduction` (671–683) | Completeness everywhere, (EP) on every edge. | | **F** (EP) / **U** (CBOI). |
| Proposition `FA` (689–738) | Losses with (W) at worlds v and w, V undominated, (IB) at u. Extra: (c). | IC Lemma 2 models X, Y, with T and B inside C's credit and debt on P_2 and P_1 (credal interval on the edge) | **F** as stated (credal interval on the edge, F3). The chain-lemma core is **SR**; see IC. |
| Theorem `two`, Corollaries `SH` and `shape` (740–778) | | | **F**: they rest on the above. |

### ECS — Edge Cycles and Separability

| Result (lines) | Hypotheses and extra assumptions | Models used | Verdict |
|---|---|---|---|
| (SH) | n = 3; worlds 2 and 3 exactly additive with integrable envelope; world 1 (G)+(IB); (S); V undominated. Extra: (c) additive representation at two worlds. | | |
| Lemma `sep-moves` (158–195) | IC Lemma 7 (all edge models selected). | Bases E_2(β), E_3(β), E_1(β), E_1′(β) (class C); IB transfer to M | **F**. The IB transfer itself is (A) and **SR**, but competitive bases with threshold structure do not exist. |
| Lemmas `sep-debt` and `sep-credit` (231–384) | `sep-moves` plus the chain principle. | V + o_23(A_j) and V + o_1(Z_i): class (A), in the domain if the sets lie in Db_1 / Cr_1 | **F** (depends on sep-moves). |
| Abstract part: Lemmas `sep-box`, `sep-env`, `sep-interleave`, `sep-diag`, `sep-points`, `sep-potential` and Proposition `sep-abstract` (396–737) | Measure theory only: cycle condition (C) ⇒ separability. | none | **S** as mathematics. Its use needs (C), which came from edges. |
| Theorem `sep` and Corollary `sep` (741–774) | | | **F**. |

### IC — Independence Chains

| Result (lines) | Hypotheses and extra assumptions | Models used | Verdict |
|---|---|---|---|
| **Lemma `chain` (127–152)** | n = 3, V competitive on {1,2,3}, C competitive on {1,2}, (IB) and strict (G) at world 1. | X′ = V + o_12(S) and X = X′ with C's advice on ±A: (A), near V when S is a thin set; Y = C silenced | **SR**: choose S ⊂ P_3 ∩ K. This set is non-null because K is open and contains e_1 and e_2. The lemma never uses the face lemma. Domain-robust. |
| Proposition `endpoint` (165–200) | Additive one-sided extensions at worlds 2 and 3. Extra: (c). | T ⊂ C's credit on P_2 and B ⊂ C's debt on P_1, read off the edge credal interval | **F** as stated (F3). An advice-level restatement is **SR**: "no C competitive on {1,2} gives o_13 on a non-null part of P_2 and o_23 on a non-null part of P_1". This needs only the chain lemma and the additive bounds. |
| Definition of path-closed and Theorem `pathclosed` (205–250) | (G), (IB), V competitive. Extra: (e) path-closedness at V and at V + o_12(S) along all continuous-in-measure families. | M_r, M′_r, X_s: all (A) edits of V | **SR** after the same advice-level restatement, with S ⊂ K. The hypothesis is category (e). |
| (SH) (265–269) | Worlds 2 and 3 exactly additive. Extra: (c). | | |
| Lemma `edges` (289–313) | Face lemma, EDL Lemma 4(c). | edge families | **F**. |
| Lemma `weights` (315–356) | Splicing of improvements, separation. | improvements Y of C | (a) and (b) are **SR**: the splices stay in the domain if improvements use admissible options. (c) is **SR**. |
| Lemma `tied` (358–371) | | Y = V + o_12(Q_3) + o_13(Q_2) | **SR**: take Q_2, Q_3 inside K. Each t_23 level meets K in a non-null set because K ∋ e_1. |
| Lemma `noboth` (373–420) | | uses base E_2(τ) | **F** (class C). |
| Lemma `shape`, Proposition `good` (422–534) | | D_2 and X = D_2 silenced (class B/D); excludes alternatives using edge models | **F**. |
| Lemma `closing` (547–569) | EDL Lemma 4(c), edge injectivity. | X = E_3(b′) + o_12(S); approach E_3(b′ − 1/n) | **F**. |
| **Lemma `compose` (571–581)** | (IB) and transitivity only. | V + o_12 + o_23 | **S/SR**: sets inside K. |
| Lemma `ratio`; Theorems `flat`, `U`, `rho` (583–782) | (SH). | bases E_2(ℓ), E_3(θ_0), good bases | **F**. |

### DT — Dense Thresholds and Debt Reduction

Every result rests on IC's edge models, good bases and closing lemma (facts (iii)–(vi), L89–122).
- **Lemma `bayes` (140–168)** states "minimizer of L_2 + κL_3 **over all models**" (L141). That is an explicit M_L = all models assumption (a). B_θ has its credal set on [e_2, e_3], so it is outside the domain.
- **Theorem `dense` (170–239)** applies KKM to X_j, which is B_θ edited. Its conclusion K_j → K_θ, a set on a face, is impossible in the domain, because there M_K ⊆ cred(C_q) for all q.
- **Lemmas `contract` and `flexible`; Theorems `bounded` and `factor`; Corollaries `flat`, `jumps` and `onesided` (243–520)** use the bases E_2(ℓ) and E_3(θ_0).

**Verdict: F for all.** The "debt-reduction" mechanism (rounds of IB transfers) is class (A) and would transfer only once suitable bases exist.

### TAW — Two Additive Worlds Without Completeness

- **Extra assumptions:** (c) finitely additive one-sided extensions (W_k) at worlds 2 and 3, with Yosida–Hewitt decomposition (L274–291).
- **(K1) KKM (L183–186):** **SR**, if the targets are domain models.
- **(K2), (K4):** **SR** via F2.
- **(K3) face lemma (L189–192):** **F**.
- **Lemmas `diff`, `YH`, `forced`, `F` (246–384):** **SR**, with sets restricted to Cr/Db. `forced` is pure (W) plus competitiveness. Lemma `F` (F1)–(F5) is pure (G)/(IB).
- **Lemma `edges` (401–437), `moves` (M1)–(M5) (443–477), `noncomp` (527–574), `closing`, `ratio`, Proposition `dg`, `noboth`, `pos` (583–820):** all use edge bases E_2(s), E_1(s), V_12, E_1′(a′), D_2 and D_2 silenced (classes B and C). **F**.
- **Lemma `noedge` (684–708):** a selection with credal set inside [e_2, e_3] cannot exist in the domain anyway (F1). The statement is vacuous.
- **Theorem `sep` (757–780):** **F** (ECS).
- **Silent targets (1343–1641):**
  - **Lemma `corner` (1410–1479):** the convexity-in-a-chart argument is pure geometry (**S**). But the target Σ_p gives debt on Θ_s ⊂ P_1, which includes problems where −g ∉ K. The corner (x_1, y_1) lies at large x and y, where −g ≈ −e_1 ∉ K.
  - **Lemma `kkmsilent`:** Σ^b gives credit on all of F_b. For large b this set lies in K, which I checked from its geometry, so it is near the orthant faces. But Σ^b as a whole is not a domain model.
  - In a proper domain the corner region has no admissible debt option at all, so the construction does not even start. **F**.
- **Theorem `I`, Theorem `main` (3047–3064), Corollary `atmostone` (3068–3082):** **F**.
- **Not read** (§§ routing, totals, FA): by TAW Remark `uses` (3127–3156), all comparisons there come from edge selections and from KKM at fixed edge or edge-Bayes targets. On that basis I expect **F**, but did not check.

### FSE — Fineness Spreads Along Edges

| Result (lines) | Verdict and reason |
|---|---|
| Definition `fine`; Lemmas `ideal` (205–217) and `uf` (a), (b), (c) (275–305) | **S/SR**: ideal and ultrafilter algebra. Restrict ideals to the measure algebras of Db_v and Cr_v. |
| Lemma `germ` (239–253) and Lemma `uf`(d) | Compactness of [0, ∞] in the t_j coordinate. **SR** as mathematics, on the band sets of D_{1j} ∩ Db or Cr. Its *use* needs heavy germs tied to edge selections: **F**. |
| Lemma `ends` (432–464) | X = E_j(2b), D_j, E^j_1(a/2) (classes B and C). **F**. In the domain the vertex block {q : C_q = D_j^K} is still closed; that is the closedness half of `ends`(b). |
| Lemmas `E12`, `yard`, Corollary `X5`, Lemma `fineregion`, Lemma `SAC` (468–596) | D_1, D_j, the approach C_{q_m} → D_j with thresholds. **F**. |
| Theorem `SIAC` (600–693) | Continuity of β_q over the edge (class C). **F**. |
| **Proposition `localext` (697–749)** | Fineness on R, plus an SI and an AC pair in R, plus completeness and (IB) ⇒ local Λ. Pure CCF §§5–6 algebra. **SR** with R ⊂ Cr ∪ Db. A key transferable tool. |
| Lemma `silent` (775–786) | Selection on the open edge, competitive on {1, j}; X = N + debt(B′). **SR**: B′ must be admissible as debt at 1. The ω/swap identity (eq. swap) holds on D_{1j} for admissible options. |
| Partner bounds, Lemmas `sources`, `creditconf`, `SIpartner`; Theorem `transfer`; Corollary `edgefine`; Proposition `third`; Theorem `onefine` (797–1218) | **F**: they work "at the far end of the edge", near C = D_j, with edge models (α, β) (L1035–1041). In the domain the far end is D_j^K, the selections near it are tangential, and they lack thresholds. |
| Section `edge` (1229–1455), statements only | Uses T_0(E), B_0(E) of two-sided edge models: **F** (not checked line by line). |
| Lemma `YH` (1460), Lemma `atoms` (1486) | Measure theory. **S**. |
| Lemma `chain` (1565–1572) | **SR** (= IC). |
| Theorems `chainEP` and `chainW` (1589, 1698) | Conclude (EP). **F**. |
| **Lemma `leading` (1744–1792)** | Hölder reduction of a group primary to a real primary: **S**. Positivity of the charges is taken from FAED Theorem 3 on edges: **U/F**. |
| **Lemma `FC` (1805–1837)** | Completeness + (FC) ⇒ exact group-valued primary. Compactness theorem plus Motzkin. **SR** on the domain: the regular models become domain models, and u^X has layer 1 varying only on Cr_v and layer 2 only on Db_v. Strict (G) gives non-constancy, using D_v^K versus the all-debt domain model. |
| Theorem `tame` and Corollary `tameshape` (1843–1890) | **F** (they route through `onefine` and `chainW`). |
| AExt (1894–2035) | Statements only. **F**: transfer at the far end. |
| Lemma `excl` (2055–2063) | Pure. **S**. |
| Lemma `conestails` (2065–2101) | Uses `yard`. **F**. |
| Lemmas `EPnotCN`, `CNtoDI`, `DItoCN`; Theorem `LH`; Corollaries `relLH`, `LHcons` (2103–2316) | Edge bases. **F**. |
| **Proposition `GC`** (2353–2391) | (a) **SR**: germ compactness. (b) uses W_1 and D_1 (class B). **SR** with W_1^K := the model giving debt on all of Db_1, and D_1^K. The hypotheses are category (e). |
| Theorem `ECC` (2398–2450), Theorem `arch` (2460) | Endpoint chain M^j_s. **F**. |
| Proposition `ex:germ` (2479) | A counterexample on all models. **U** in the domain, but plausibly **SR** by restriction. |
| Theorems `ownregion`, `dense`, `shape` (2540–2677) | Statements only. Two-sided edge selections. **F**. |

### FFN — Fineness for Any Finite Number of Worlds

- **Inputs (1)–(6) (L68–98)** are FSE's edge results (vertex-block, yardstick, SAC, edge transfer, SI-partner).
- **Lemma `remaining` (123–212), Theorems `allfine`, `fineedge`, `oneextension` and `LH` (214–467):** all use the edge sequence C_m = (α_m, β_m) → D_j and yardsticks. **F**.
- **What does transfer:** the observation (L254–260) that options ω_v on the regions O_v improve every world outside the active triple. This is class (A). It is **SR** for sets in O_v ∩ K, and these are non-null because K is open around the vertices.

### TCR — Three Complete Rankings Cannot Cover

- **Lemma `reach` (371–385):** pure order theory. **S**.
- **Theorem `cut`, no saturated cut (393–439):** hypotheses: world v complete, (G) at v and w, (S), a band-dense family 𝔅.
  - The proof uses the face lemma (C_{e_v} = D_v ∈ R, C_{e_w} = D_w ∉ R), edge models (α_q > 0 ⇒ a band in the silence/debt region), (T1) and (T2).
  - **Verdict: SR, conditional.** In the domain, F2 gives C_{e_v} = D_v^K and C_{e_w} = D_w^K. Off D_{vw}, edge selections agree with D_v^K: by F2, C ⊇ K ∩ {h_v, h_w > 0} and C ∩ {h_v, h_w < 0} = ∅ — I checked this. Both openness steps go through if "band-dense" is replaced by **hereditary density**: every non-null subset of (Cr_v ∪ Db_v) ∩ D_{vw} contains a non-null member of 𝔅.
  - Band-density no longer suffices, because without thresholds the difference set between C_q and D_v^K or D_w^K need not contain a band. That stronger density condition is exactly what the light-set family of Proposition `finite` does *not* provide (it is built at chosen t-levels).
- **Lemma `count`, the counting lemma (453–513):** hypotheses: a preorder with weak (G) and (IB) at v, a connecting chain from D_v to D_w of length ≥ 2, perturbation sets in F, and disjoint heavy K_l outside F.
  - Uses D_v, Π_k = D_v + debt_v(K…), X⁺ and X⁰ (class B).
  - **Verdict: SR.** Replace D_v and D_w by D_v^K and D_w^K, and "debt_v(B)" by "D_w^K-advice on B". Steps (a)–(d) use only that D_v^K and D_w^K are the pointwise best and worst at v on D_{vw} among domain models, which they are. The final step Π_ℓ ≤_pw D_w^K holds because the two agree off D_{vw}. No completeness or (S) is used.
- **Proposition `rich`, rich far ends (547–661):** E_2(b), E_2(z) ± sets, edge continuity of β, FSE Theorem 64. **F**.
- **Definition `light`, Lemma `near` (680–718):** lightness is defined through D_2 + debt_2(W), which in the domain must be redefined via D_2^K → D_1^K-advice. `near` uses the far-end sequence. **F**.
- **Lemmas `compose` and `buys` (720–772):** pure (IB) plus weak (G). **SR** with D_2^K and admissible sets.
- **Proposition `finite`, Theorem `main`, Corollary `coverage` (794–921):** **F**. They need `rich`, `near` and FSE Theorem 64. The light family is only band-dense (see `cut`).

### CRANW — Complete Rankings for Any Number of Worlds

- **Lemma `regions` (321–389):**
  - (a)–(c) and (e) are geometry and (G). **S/SR**: O_v ∩ K, and the option ω_v is admissible only where it lies in K.
  - (d) is about edge models. **F**.
  - (f): D_K silent on D_{xy} when e_x, e_y ∈ K. **S** for coherent targets. In the domain the target's credal set also contains M_K, which does not change (f).
- **Inputs (F1)–(F6), (C1)–(C2), (N1)–(N2) (405–494):** inherited as above. (F1) is **S**; (N2) counting is **SR**; the rest are **F**.
- **LH, own region, dichotomy, rich, counting (505–1414):** proofs not read. By the summary (L95–104) and remarks (L1549–1554), "the selections used are all on edges". **F** expected.
- **Theorem `count` (1415–1449), Theorem `clique` (1456–1471), Theorem `main` (1473–1485), Corollary `consequences` (1492–1517):** **F**. They rest on (EP), two-sided selections, Theorem `own` and Proposition `rich`.
  - The clique *constraint* (that (EP) holds on edges between vertices in K) has no meaning in the domain, where no selection's credal set lies on an edge.
  - Remark `open` (1580–1632) is a correct diagnosis for all-models.

### IRWAS — Independent Rankings Without Additive Structure

- **Hypotheses:** a finite KPS/Conder–Slinko comparative probability, ultrafilters and AC (L35–92). Extra: (g) AC and a transfinite lexicographic order. No (S) by design (L26–31).
- **Theorem `GIB` (94–116):** **S** after restriction to domain models: restriction preserves completeness, (G) and (IB).
- **Theorems `noprimary` (130–157), `nolocal` (171–212), `LHDH` (216–234):** use V + debt(E_A) and a model "good on H′ \ E_A" (credit everywhere; class B).
  - **Verdict: SR.** Choose the partition cells E_j inside Db_i for the debt-layer argument and inside Cr_i for the credit-layer argument. Replace "good on H′ \ E_A" by credit on Cr_i \ E_A. The counterexample remains a counterexample for domain-restricted rankings. It is not a tool and supplies no (S).

### CSE — Conditional Shunning of Error (a positive construction)

- **Hypotheses:** additive complete losses Σ_T(λ, η) on all models (L65–85). Extra: (c), plus (a), because the losses are defined on and compared over all models (Prop `basic`).
- **Proposition `basic`, Lemma `Q`, Proposition `bayes` (87–225):** **S** as facts about Σ_T. Restricting the rankings to the domain keeps (G), (IB), completeness and (C) (ties with undominated models stay undominated).
- **Theorem `undominated` (264–326):** necessity uses separation over all attainable loss vectors. **SR** over domain models (splices stay in the domain). But the set of undominated *domain* models is larger and is not characterised. **U**.
- **Proposition `V` (328–352):** the competitor Y = V ∪ A ∪ B, with A and B thin cones near e_j and e_k. These lie inside K for small δ: a **near-V construction**. **S**: "V dominated if |U| ≥ 2" holds in every domain.
- **Theorem `S` (372–416):** the selection has C_{e_j} = M(0, e_j) = D_j for j ∈ U, and boundary selections C_q = M(α, β) with credal sets on faces. These are outside a proper domain (F1). **F as written.**
  - Likely repair, **U**: use C_q ∩ K, which is coherent with credal set conv(K(l,u) ∪ M_K). It is the domain-Bayes model and so competitive within the domain. Its losses are plausibly continuous by the same dominated-convergence argument. I have not checked undominatedness at q ∈ Δ_T, where Σ_T has ties, or non-tangency for interior q (it fails whenever K(l,u) does not contain M_K in its interior).
- **Proposition `bayessel` (420–452):** compares Bayes models on faces. **F/U** in the domain.
- **Lemmas `intrinsic`, `credal`, `ident`; Theorem `coverage`; Example `covered`; Proposition `notcovered`; Corollary `vertices` (454–698):**
  - **S** as statements about which credal sets K(l,u) the all-model systems cover.
  - In a domain, the covered targets would be D_{conv(K(l,u) ∪ M_K)}. The covered/not-covered lists (precise models, faces, ε-contamination) change accordingly. Precise models and faces are never domain models (F1).

### IRC — Incomplete Rankings and Coverage

Priority items: the stated main results and the §1 summary list.

- **Definition `T1o` (258–266) and its variants (T1^s), (T1^cc), (T1^cut), (E2) (2757–2784):** extra assumptions of category (e). They are stated along edges, so they are defined only through edge selections.
- **Counting remark `rem:bounded` (553–568):** **SR**, as for TCR `count`. This is "counting to a bounded target X": replace D_v by D_v^K.
- **Theorem `cut` (572–618):** the TCR theorem with completeness replaced by (T1°_w). Verdict as for TCR `cut`: **SR** only under hereditary density, and it needs F2 for the endpoints.
- **Lemma `light` (a)–(d) (632–673):** pure (G)+(IB) with D_v. **SR** with D_v^K and admissible sets.
- **Lemma `near` (675–701):** far-end edge sequence. **F**.
- **Lemma `forced` (705–749):** (a) is **SR** (pure (W) plus competitiveness); (b) and (c) use E_k(s) under (EP). **F**.
- **Lemma `chain` (756–776):** **SR**, as IC's.
- **Ideal N^x_S (778–786) and Lemma `sweep` (788–859):**
  - Hypotheses: (G), (IB) at x; pairwise-disjoint S, T, Q; (T, Q) not weakly AC; the cover condition (eq. cover).
  - Models: V + cred(S) + debt(T) + cred(Σ), all class A.
  - **Verdict: SR**, with S, Σ, Q ⊂ Cr_x and T ⊂ Db_x. No completeness is used. A good domain-robust tool.
- **Change vectors, Lemma `accept` (2058–2134):** **SR**. In a proper domain the vector u^X varies in layer 1 only on Cr_v and in layer 2 only on Db_v. Ω′ effectively reduces to (Cr_v × {1}) ∪ (Db_v × {2}). (c) and (d) need the restricted sets.
- **Theorem `NC` (2188–2250), the finite-cancellation/extension theorem:**
  - (a) is "no property of a ranking" (L2252): Tychonoff plus minimax. **S**.
  - (b) needs covers of H′; in the domain, covers of Db_v and Cr_v. **SR**.
  - (c) is **S**.
- **Corollaries `NCext` (2255–2306) and `NCclasses` (2314–2380):** (i)–(iii) are **SR**, with the full extension consisting of charges on Cr_v (layer 1) and Db_v (layer 2). `NCclasses` (iv) uses CCF §§5–6. **SR**, given fineness on the restricted algebras.
- **Lemma `smallcanc`, Examples `K4` and `half5` (2389–2535):** **S/SR**. These are single-layer algebra, and the examples are choices of sets.
- **Conf(θ), Theorem `conf`, Proposition `confT1` (2536–2747):**
  - Rankings are defined on **all models** (L2538–2539, an explicit (a)), with precise selections C_p = D_p.
  - In a proper domain these selections are outside the domain or tangential (F1).
  - **F** as a v19 example. The claim "(S) does not imply (T1°)" would need a domain construction.
- **Edge-based results** (statements read; their summaries name edge selections, (EP), rich far ends or crossing cuts): Theorems `EP`, `onecomplete`, `SCext`, `SC`, `LH`, `A`, `B`, `Astar`, `Bstar`, `crossing`, `twoNC`; Corollaries `C` and `refined`; Proposition `F4`. Proofs not read. **F expected.**
  - Corollary `Wforces` and the logical shape results inherit **F**.

## 3. Summary of verdicts and recommendations

**1. The toolkit splits cleanly in two.**
- *Survives with repair.* The order-algebraic layer, driven only by (G), (IB) and transitivity, plus the chain lemma's competitiveness step:
  - ⪯_d and ⪯_c, SI/AC pairs, ideals, ultrafilters;
  - comparative probability → (P_d, P_c, κ) → Λ (CCF Thm 14; FSE Prop 13);
  - the (FC) group primary (FSE Lemma `FC`) and the Hölder reduction;
  - finite cancellation (IRC Theorem `NC` and its corollaries; `smallcanc`);
  - the counting lemma, lightness composition and buys;
  - sweeps;
  - the chain lemma and composition;
  - ECS's measure-theoretic separability step.
  
  The repair is mechanical: debt sets in Db_v, credit sets in Cr_v, D_v ↦ D_v^K.
- *Fails as written.* Everything that produces comparisons from (S), because it relies on edge selections:
  - the face lemma and thresholds;
  - (EP) and the endpoint families;
  - band and yardstick lemmas, and fineness from (EP);
  - germ transfer, partner bounds and the far end;
  - rich far ends, light sets near the far end and good bases;
  - the closing lemma and the routing primaries;
  - the clique theorem;
  - all V-domination theorems.
  
  The reason is not a far competitor but F1–F3. In a proper v19 domain no coherent model with credal set in a proper face is evaluable, the face lemma becomes the relative face lemma F2, and edge selections lose their one-parameter threshold structure.

**2. The non-tangency requirement must be weakened.** As stated in the brief, it is inconsistent with (S) and strict (G) for every proper K (F2): every C_p with supp p ≠ Ω is tangential. The natural reading is non-tangency for p ∈ int Δ, with C_{e_i} = D_i ∩ K forced. This reading matches v19's own q-contractions at boundary q, which are tangential.

**3. The nearby reachable result.** Because domain models are exactly the sub-models of the single coherent model W = D_{M_K}, the whole programme can be restated relative to W:
- V is the bottom coherent model and W the top;
- vertices become D_i ∩ W;
- each problem has at most one admissible option, so contradiction disappears.

The surviving layer then gives, at any world that is fine on Cr_v ∪ Db_v and has SI/AC pairs, an exact characterisation: a full extension exists iff (NC) holds (IRC `NC`, transferred). What has to be rebuilt is the source of fineness, SI/AC pairs and connecting chains from (S). That means the "edge" analysis of selections on conv(M_K ∪ [e_v, e_w]), using F2 in place of the face lemma.

**4. Open dependencies I could not check:** CBOI Theorem 2 and Lemmas 1, 3 and 4; CC Lemma 7; EDL Theorems 2 and 8; FAED; and the unread parts of TAW, CRANW and IRC listed in §0.
