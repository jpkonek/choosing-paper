# AUDIT A — v3, CC, CBOI, BA, VT, CNA, OB, EDL, FAED, OR, LRCF, LRSDG, LDG v2 appendix

Auditor scope: read in full: v3 (909 lines), CC (603), CBOI (443), BA (520), VT (279), CNA (367), OB (182),
EDL (691), FAED (422), OR (392), LRCF (433), LRSDG (388). LDG v2: lines 30-139 (axioms) and 483-807 (appendix
through `rem:threeworld-bounds`). NOT read: LDG v2 lines 807-913 (`prop:countable`, Joyce section), and the
companion files cited but not assigned (Three Complete Rankings, Complete Rankings Any n, truth_directed_losses,
nonadditive_losses). v19b read only at lines 185-260 and 1890-1960.

Abbreviations: GD files as in the task. "V-domain" = M_L = {D measurable : lambda(D \ V) = 0}, V an open convex
cone, V ⊇ R^n_{>=0} \ {0}. "Restricted Bayes" = minimiser of expected loss over M_L only.

---------------------------------------------------------------------------------------------------------------

## 0. Structural facts about v19-type domains that decide most verdicts

These are checked directly (elementary convex analysis), not taken from the files.

**F1 (shape of V).** If V ≠ R^n then V ∩ R^n_{<=0} = ∅ (v19b `lem:three`, l.1893-1906), so 0 ∉ V and
V ∩ (−V) = ∅. Writing K_V := V* ∩ Δ (normalised dual cone), K_V is a nonempty compact convex subset of int Δ
and V = {g : min_{m∈K_V} m·g > 0}. [Proof: V open ⇒ every nonzero m ∈ V* has m·v > 0 on V; V ⊇ orthant ⇒
m ≫ 0; V open convex ⇒ V = int(cl V) = {P_{K_V} > 0}.]

Consequences for a proper V:
* **No model in M_L ever gives contradictory advice** (g, −g ∈ V impossible). The 4th rank of the v3 order is
  unattainable for evaluable models; on each pair meeting V, every evaluable model either accepts the V-orientation or
  gives no advice, and on each pair {g,−g} with g ∉ V and −g ∉ V every evaluable model gives no advice. (The decision
  problems themselves are unchanged; only the class of evaluable models is restricted.)
* **A coherent D_M lies in M_L iff K_V ⊆ M** (v19b `lem:extension`(ii), l.1935-1936; dualise
  {P_M>0} ⊆ {P_K>0}). So every coherent domain model has a credal set containing K_V ⊂ int Δ. In particular
  **no coherent model in a proper V-domain has its credal set on a face of Δ** (no ideal D_i, no edge models,
  no precise models except possibly the single point K_V={p}).
* **D_M is non-tangential iff M is full-dimensional and K_V ⊆ relint M.** If M is lower-dimensional, take
  g ≠ 0 orthogonal to aff M and to 1: P_M(g)=0=P_K(g), so g ∈ cl(D_M) \ V.

**F2 (targets that force V = R^n).** Any coherent target whose credal set M ⊆ ∂Δ (precise boundary models,
edge/face models, conv{e1,e2,e3} in n ≥ 4, ...) can lie in M_L only if V = R^n (K_V ⊆ M ∩ int Δ = ∅). Any
lower-dimensional M can be non-tangential only if V = R^n. **For all such targets, every all-models
argument applies verbatim**, whatever reading of non-tangency is adopted.

**F3 (non-tangency of selected models clashes with strict (G) + (S)).** Let V be proper, let C be coherent,
C ∈ M_L, competitive on S ⊊ Ω (against M_L), and let strict (G) hold at every world of S for the change
"silence → good" on mixed problems. Then C ⊇ V ∩ {g_S > 0} a.e. [Otherwise let E agree with C except that it
accepts g on Z = (V ∩ {g_S>0}) \ C; −g ∉ V so C is silent there; E ∈ M_L and E ≺_s C for every s ∈ S,
contradicting competitiveness.] Hence cl(C) contains g = 1_S − t·1, t = min_{m∈K_V} m(S) ∈ (0,1), which
has P_{K_V}(g) = 0, so g ∉ V: **C is tangent.** At a vertex, C_{e_i} ≈ V ∩ D_i exactly.
So: **under the brief's literal requirement that every selected C_p be non-tangential, (S) at boundary priors
plus strict (G) on mixed problems forces V = R^n.** A proper V is usable only if, at every world i, good and
silence tie on (a positive-measure part of) the V-pairs near ∂V ∩ D_i — i.e. essentially the agreed
exceptional system, or Σ_T with T = Ω. Σ_T with T ≠ Ω still forces tangency at e_i for i ∉ T.
Note: v19b's own non-tangency (`def:cpm`, l.247-250) is required only of the *realised target* D, not of all
q-contractions; indeed v19's own q = e_i contraction is Φ^{-1}(D_{e_i}) = V ∩ D_i, which is tangent.

I therefore give two verdicts where they differ:
* **R1** = brief's reading (all selected / undominated coherent models non-tangential).
* **R2** = v19b's reading (only the covered target non-tangential; competitors and selected models
  restricted to M_L, selected models may be tangent).

Under R1, every result whose hypotheses include strict (G) on mixed problems at all worlds (or at the vertex
world used) and (S) automatically has V = R^n, so its proof SURVIVES verbatim. Results that assume only weak
(G) or the exceptional system are not covered by this shortcut.

**F4 (repair template).** Most proofs below use one of: (i) the pointwise Bayes model over all four kinds of advice;
(ii) the ideal D_i or D_j; (iii) the face-support lemma (competitive coherent model on S has credal set in
Δ_S). In a V-domain: (i) has a direct repair (minimise over the advice in the V-domain's advice ranges; the minimiser is in
M_L and splices/mixtures of M_L-models stay in M_L); (ii) has the analogue V ∩ D_i (best at i within M_L);
(iii) has **no** repair: its V-analogue (F3) gives only K ⊆ conv(Δ_S ∪ K_V) plus tangency, never face
support. Every obstruction that routes through face support therefore FAILS as proved under R2.

---------------------------------------------------------------------------------------------------------------

## 1. Full Coverage by Homothetic Credal Families v3

Setup (l.48-145): Gaussian μ, null-set identification, pairs on H={g1>0}, 4-rank order, (G) weak+strict,
(IB), (E),(LA),(A),(S),(C). **l.145: "All rankings constructed below evaluate every measurable model."**

| Result | Hypotheses (lines) | Extra assumptions | R1 | R2 |
|---|---|---|---|---|
| `prop:obstruction` (l.161-198) | ranking on all measurable models; (a) every non-coherent model strictly dominated by a coherent one; (b) on models accepting all of B=R^n_{>0}∪R^n_{<0}, comparison = ⊴_i | (a) all models explicit; (g) hypotheses (a),(b) specific to v2 ordinal recipe | SURVIVES (V=R^n by F3) | FAILS / N.A.: uses E = D_1 inside ball, D_2 outside (l.173) and C' = C ∪ B, Ɛ' = Ɛ ∪ B (l.191), which accept strictly negative gambles; impossible in proper V (F1: V ∩ R^n_{≤0} = ∅). The contradiction mechanism does not exist in proper V |
| Remark (old indices) l.208-222 | homothetic v2 family; fixed local penalties | (c) additive | survives (pure pointwise algebra) | survives |
| `lem:local-independence` (l.251) | integral loss (eq. local-penalties) | (c) additive; integrable envelope | SURVIVES | SURVIVES (restriction of an additive loss to M_L keeps (G),(IB)) |
| `thm:general` (l.268-322) | strictly ordered local penalties with envelope; for every p the pointwise min over {+,0,−,×} is a.e. unique and equals advice of a coherent C_p | (a) all models (proof compares with every D); (c) additive; (d) Bayes choice; (f) Gaussian/H | SURVIVES (V=R^n) | SURVIVES-WITH-REPAIR as a construction: minimise over the advice in the V-domain's advice ranges; need the *restricted* minimiser coherent. But by F3 its boundary selections are tangent (e.g. C_{e_i} ≈ V∩D_i), so it never yields R1-admissible proper-V rankings |
| `lem:thresholds`, `prop:bayes-interval`, `thm:full` (l.368-459) | n=2, tables (mixed/unanimous), w ∈ [0,1] | (a) all models (l.458 "every ranking evaluates every measurable model"); (c); (d); selections include C_0≈D_2, C_1≈D_1 (l.426) | SURVIVES at V=R^n | SURVIVES at V=R^n. Not transferable to proper V (C_0, C_1 are ideals, outside V). Note: n=2 targets that are points or contain a vertex need V=R^n anyway (F2) |
| `thm:additive-obstruction` (l.487-496, proof l.898-907) | n≥3; ranking **of all measurable models** with additive strictly ordered penalties; (LA),(S) | (a) explicit; (c) additive; (d) via lem:bayes-necessary; (f) | **SURVIVES** (ℓ(good)=0<ℓ(0) is strict (G) on mixed problems ⇒ V=R^n by F3) | Targets with M ⊆ ∂Δ (all three-vertex targets when n≥4 that lie in a face, e.g. conv{e1,e2,e3} ⊂ Δ_4): **SURVIVES verbatim** (F2 forces V=R^n). Full-dimensional targets incl. vacuous for n=3: **FAILS as proved** — see the next three rows. Conclusion UNCLEAR |
| `lem:bayes-necessary` (l.628-682) | (a) (LA),(S) + additive; (b) additive; (c) D_M p-Bayes | (a) all models; (d) | SURVIVES | (a) SURVIVES-WITH-REPAIR: B (l.642) is the pointwise min over all four kinds of advice — e.g. at p=e_i it is D_i ∉ M_L; replace by restricted min, which is in M_L; then conclusion = "coherent restricted-Bayes model". (b) SURVIVES (mixing two M_L-rules by measurable subsets stays in M_L; separation unchanged). (c) **FAILS**: l.674-679 needs acceptance of g with g_S>0 and g_j ≪ 0; such g ∉ V (K_V full-support). V-analogue: only K ⊆ conv(Δ_S ∪ K_V); and by F1 no coherent domain model has M ⊆ Δ_S at all |
| `lem:three-world` (l.691-801) | measurable sign-preserving ψ; for every p∈Δ_I a coherent D_{K_p} with **K_p ⊆ Δ_supp p** completing {p·ψ>0} | (g) face support of the completions | pure lemma, SURVIVES | Lemma is true but its hypothesis is **unsatisfiable** by coherent models in a proper V-domain (F1). Not applicable |
| `prop:bayes-vertex-obstruction` (l.820-896) | coherent p-Bayes model at every p; D_M with three vertices p^0-Bayes | (a),(c),(d) | SURVIVES | **FAILS**: (i) l.827 uses lem:bayes-necessary(c); (ii) l.832-850 claims a coherent r^{ij}-Bayes model has credal set exactly the edge Δ_{ij} — impossible in proper V (F1); (iii) l.852-862 compares silence with *both* recommendations on one pair — in proper V the advice range of each pair contains the acceptance of at most one orientation; (iv) l.834 "gambles with g_j<0 and every other coordinate positive": their acceptance is in the advice range only on the V-part of that region |
| ¶"Allowing infinite additive losses" (l.517-528) | strict (G), nonnegative local penalties on all models | uses the **everywhere-contradictory model** | survives | N.A. in proper V (that model ∉ M_L; no contradictions exist in M_L) |
| `lem:representation`, `lem:kkm` (appendices A,B) | — | — | SURVIVE | SURVIVE |

---------------------------------------------------------------------------------------------------------------

## 2. Closed Choice for Independent Rankings (CC)

Setting l.46-80 imports v3/BA unchanged (all models). (KKMa/b) from (LA)+(S): domain-relative, fine.

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `thm:regular` (l.84-124) | n≥3; **ranking of all measurable models**; (G),(LA),(S); additive weak extension (eq. regular-extension) on regular models | (a) explicit; (c) one-sided additive extension; (d) via pointwise Bayes B | SURVIVES | **FAILS as proved** at "v3's Proposition 13 forbids this" (l.120-121), which needs lem:bayes-necessary(c)/face support. B (l.98) repairable by restricted min; regularisation Ɛ° stays in M_L (correct unanimous advice is in V; proper-V models never contradict). Conclusion UNCLEAR |
| `rem:collapse` (l.131-154) | BA six-region family | — | survives | survives (regular F_A can be chosen inside V) — not checked in detail |
| `prop:priority` (l.161-217) | additive L meeting v3 thm:general | (c); uses **D_i** and Ɛ_ε = D_i silenced on Z_ε (l.205-216) | SURVIVES | diagnostic only; with proper V, D_i ∉ M_L; analogue with V∩D_i plausible, not checked → UNCLEAR |
| `lem:debreu` (l.249-340) | complete, independent, weakly monotone, continuous preorder on rank functions x: H'→{0,1,2} | (b) completeness; (e) continuity in measure (open strict contour sets); (f) | SURVIVES | SURVIVES-WITH-REPAIR: in a proper V-domain the regular models are the measurable models whose world-i ranks lie in pair-dependent 2-element sets ({0,1} or {1,2} at world i, or {1}, i.e. every evaluable model gives no advice, if neither orientation is in V), not {0,1,2}; product/Debreu structure and path-connectedness still hold |
| `thm:continuous` (l.342-379) | as thm:regular + regular-model ranking is an intersection of complete independent weakly monotone continuous preorders | (b),(e) | SURVIVES | inherits thm:regular: **FAILS as proved** |
| `lem:face` (l.418-433) | strict (G); D_K competitive on S | uses Ɛ accepting g with g_S>0, g_j ≪ 0 (l.423-430) | SURVIVES | **FAILS** as stated (that Ɛ ∉ M_L). Correct V-analogue is F3: K ⊆ conv(Δ_S ∪ K_V) and D_K ⊇ V∩{g_S>0}; never face support |
| `cor:face` (l.435-450) | (G),(LA),(S) | — | SURVIVES | (a) C_{e_i}≈D_i FAILS; analogue C_{e_i}≈V∩D_i (F3). (b) FAILS (no edge models). (c) "vacuous tied only with full-support selections" **SURVIVES** via F3 (D_Δ does not contain V∩{g_S>0} for S ⊊ Ω) |
| `lem:fibres` (l.455-492) | (G),(LA),(S); (c) also completeness | (b) for (c) | SURVIVES | (a) SURVIVES. (b),(c) SURVIVE-WITH-REPAIR using V∩D_i ≺_i V∩D_j (strict (G) inside V). Under the exceptional system both vertex selections may be the vacuous model and (b) FAILS (no two tie classes) |
| `lem:primary` (l.500-531) | (S) [+ (LA) for (c)]; real primary | (g) existence of a real primary | SURVIVES | SURVIVES (all competitors are the invisible improvements, which can be taken in M_L) |

---------------------------------------------------------------------------------------------------------------

## 3. Closed Choice Beyond Ordinary Integrals (CBOI)

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `lem:dominator` (l.84-101) | (LA),(S) | — | SURVIVES | SURVIVES (domain-relative) |
| `thm:fa` (l.139-245) | n≥3; (G),(LA),(S); finitely additive one-sided extension eq.(weak) on regular models, charges strictly positive on non-null sets | (c) FA extension; (d); uses v3 obstruction for L^c; implicitly all models (B over all advice, l.210) | SURVIVES | **FAILS as proved**: imports v3 obstruction (face support). Splices X_m and the L^c-minimiser B are repairable within M_L |
| `lem:split`, `lem:compact` (l.156-201) | Yosida–Hewitt; Hausdorff compactness | — | SURVIVE | SURVIVE (coherent M_L-models = {M ⊇ K_V} closed under Hausdorff limits) |
| `prop:example` (l.276-321) | ultrafilter charge η; costs (0,¾b,b,2b) | (c) FA; uses D_i, precise C_p = D_{p} | SURVIVES at V=R^n | positive example lives at V=R^n only (precise models, F2) |
| `lem:edge-continuity` (l.339-366) | (G),(S); primary continuous in measure | first step = face support (l.345-349); D_j "guidance-worst at i among coherent edge models" (l.359-360) | SURVIVES | **UNCLEAR**: face-support step FAILS; V∩D_i analogue fine for lsc half; the usc half needs "V∩D_j is worst at i among competitive-on-{i,j} coherent models", which is not obvious in V (a coherent C ⊇ V∩{g_i,g_j>0} may accept V-gambles with g_i,g_j<0) |
| `thm:blind` (l.385-406) | (G),(S); primary blind on arbitrarily small sets | same two facts | SURVIVES | UNCLEAR (same reason) |

---------------------------------------------------------------------------------------------------------------

## 4. Beyond Additive Guidance Rankings (BA)

l.69: "All rankings here evaluate every measurable model."

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `lem:complete-class` (l.114-134) | (LA),(S) | — | SURVIVES | SURVIVES |
| `thm:extension` (l.144-163) | n≥3; **ranking on all models**; (LA),(S); comparisons weakly respected by additive guidance losses | (a); (c); (d) | Note: **no strict (G) assumed**, so F3 shortcut does not apply; but v3's obstruction it imports is about rankings with strictly ordered penalties on all models → UNCLEAR whether V=R^n is forced | **FAILS as proved** (imports v3 obstruction; face support) |
| Corollary (l.172-203) | intersection of additive criteria + strict (G) | (c) | SURVIVES | inherits thm:extension: FAILS as proved |
| `prop:genuine` (l.255-288) | six-region tuple ranking | (g) specific construction; all models | positive; SURVIVES at V=R^n | not checked for proper V |
| `thm:finite-sample` (l.305-345) | tuple measure π; strictly guidance-respecting sampled penalties | uses Ɛ giving ideal world-i advice on A_i (l.334) | SURVIVES | SURVIVES-WITH-REPAIR: replace ideal advice by V-ideal advice; competitive ⇒ C ≈ V∩D_i; the disconnection argument is unchanged |
| `prop:lex` (l.368-421) | lexicographic (B_i,T_i) | uses ideal D_j (l.373-377); family C^t with M_t ⊇ {e_1..e_{n−1}} | SURVIVES | UNCLEAR: "undominated with no silence ⇒ D_j" is false in proper V (every evaluable model gives no advice on pairs {g,−g} with g ∉ V and −g ∉ V); needs reworking. C^t ∈ M_L iff K_V ⊆ M_t |
| §5 complete lexicographic example (l.435-464) | — | (b); positive except (S) | survives | N.A. |

---------------------------------------------------------------------------------------------------------------

## 5. Vacuous Targets and Transfinite Construction (VT)

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `prop:strict` (l.60-86) | penalties 0,c,1,2, c<1/n | (c); positive, all models | SURVIVES | SURVIVES |
| `prop:neutral` (l.110-145) | penalties mixed 0,0,1,2; unanimous 0,1,2,3 | weak (G) only (good~silence on mixed); (c) | **SURVIVES even with proper V**: vacuous model dominates every M_L-model; constant selection C_p = D_Δ is non-tangential in every CPM domain (cl = orthant ⊆ V∪{0}). This is the one construction in the corpus that is R1-admissible for proper V | SURVIVES |
| `lem:union` (l.188-210) | increasing union of stages with (G),(IB), target undominated | — | SURVIVES (domain-agnostic) | SURVIVES |
| closed-section invariant (l.225-238) | — | — | SURVIVES | SURVIVES |
| §1 claims (l.25-49) re complete-ranking theorem | cites Three Complete Rankings / Any n | not audited here | — | — |

---------------------------------------------------------------------------------------------------------------

## 6. Coverage after Neutral Abstention (CNA)

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `thm:limit` (l.88-176) | table (1), 0<ε≤1 | (c) additive; (d); all models; selections include C_{e_i} = D_i (l.204) | SURVIVES at V=R^n (strict (G) for ε>0 forces it anyway) | SURVIVES at V=R^n; not usable on proper V (boundary selections are ideals). ε=0 limit: as `prop:neutral`, fine for proper V |
| eq.(3)-(4) boxes (l.178-199) | 0<λ_i≤η_i | same | SURVIVES at V=R^n | same |
| **`thm:closure` (exact consistency test)** (l.248-292) | fixed family C_p containing the target; closed A_i(X) for every model X with covering property (5); four rules; forbidden (a),(b),(c) | none beyond permitted list; finite n | SURVIVES | **SURVIVES-WITH-REPAIR (domain relativisation only)**: read "every model X" (l.218) as every X ∈ M_L; rule 3 "every replacement of shared advice" as replacements that keep both models in M_L (in a V-domain this is a product over pairs of the advice ranges, so replacements stay in M_L); forbidden (a) only for strict improvements between M_L-models. The proof (l.264-291) uses only these relativised objects and the simplex lemma. With proper V and R1, the test itself will report inconsistency for any family whose boundary members are non-tangential unless strict (G) is weakened near ∂V (F3 manifests as forbidden outcome (a) via rule 2 at p=e_i) |
| "replace C_r by the target" (l.294-299) | — | — | SURVIVES | SURVIVES |
| §4 status bullets (l.315-354) | — | — | "Still impossible: additive, n≥4, conv{e1,e2,e3}" — **SURVIVES under both readings** by F2 | same |

---------------------------------------------------------------------------------------------------------------

## 7. Omission Blindness and Four-Rank Guidance (OB)

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| Theorem (l.73-139) | table (1) with c_i = |g_i| 1{h_i(g)∈U}, U = {P_M>0} | (g) **target-dependent weakening of (G)** (good~silence where the good orientation ∉ U) — outside the agreed list (l.62-69 says so); (c) additive; imports truth_directed_losses §4 Bayes facts (not audited) | SURVIVES at V=R^n (domain is all models; non-tangency vacuous) | same. Note: setting V := U does NOT make this a non-tangential v19 construction — selected B_p = U ∩ {p·g>0} and the target U itself have closures meeting ∂U |
| §3 remarks | — | — | descriptive | — |

---------------------------------------------------------------------------------------------------------------

## 8. Edge Dichotomy and Leverage (EDL)

Setting l.49-87 relies on **CC Lemma 7 (face support)** for the edge-threshold description (l.77-86).

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `prop:one-sided` (l.91-101) | CC thm1 / CBOI thm2 | — | SURVIVES | reduction valid, but both targets FAIL as proved under R2 |
| `thm:leverage` (l.112-175) | finitely additive one-sided extension ⇔ no leverage sequence | (c) FA; Kreps–Yan (Rokhlin) | SURVIVES | SURVIVES (𝒦_i is defined over domain models; the functional analysis is domain-agnostic) |
| `rem:weak-star` (l.191-210) | — | — | SURVIVES | SURVIVES |
| `lem:regular-primary` (l.249-298) | (G),(S); regular primary | (c) uses C_{e_i}=D_i, D_j, splice X_s of C_p with D_i (l.271-283) | SURVIVES | (a),(b) SURVIVE. (c) UNCLEAR (needs V∩D_i analogue + the "D_j worst" step, as in CBOI) |
| `thm:dichotomy` (l.300-414) | (G),(S); additive regular primary | edge threshold structure from face support | SURVIVES | **FAILS as proved** (edge models do not exist in proper V; thresholds α,β in t undefined) |
| `thm:lex` (l.440-463) | n≥3; (G),(LA),(S); lexicographic additive with a non-blind level | — | SURVIVES | FAILS as proved (uses dichotomy + CC thm1) |
| `thm:one-world` (l.489-603) | n=3; (G) strict only at world 1; (S); vacuous undominated; one-sided additive extensions at worlds 2,3 | (c); (d) | SURVIVES (strict (G) at world 1 + (S) at e_1 ⇒ tangency ⇒ V=R^n) | **FAILS as proved**: Step 1 (l.507-522) uses B minimising ℓ_2+κℓ_3 over all advice and v3 Lemma 11(c) (face support); Steps 2,5,6 depend on it. Step 3/4 trade (X accepts on Q_1 ⊆ R_1, Q_2 ⊆ −R_2) is repairable only on the V-part of those regions |
| `cor:reduction` (l.610-642) | as above | uses D_2, D_3 at edge ends (l.628) | SURVIVES | FAILS as proved |

---------------------------------------------------------------------------------------------------------------

## 9. Finitely Additive Edge Dichotomy (FAED)

Setting l.81-96 again imports face support ("credal set of C_p lies on that edge ... C_{e_i}=D_i").

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `lem:cheap` (l.100-109) | finite charge | — | SURVIVES | SURVIVES |
| `lem:continuity` (l.115-145) | (G),(S); FA regular primary | D_i minimises, D_j maximises among coherent edge models (l.120-121) | SURVIVES | UNCLEAR (as CBOI `lem:edge-continuity`) |
| `thm:dichotomy` (l.162-258) | (G),(S) | edge thresholds (face support) | SURVIVES | FAILS as proved |
| `cor:lex` (l.284-308) | n≥3; (G),(LA),(S); FA lexicographic hierarchy | uses W_i = "bad at i on every mixed problem" (l.293) — ∉ proper V (needs the bad orientation in V on every mixed pair); CBOI obstruction | SURVIVES | FAILS as proved |
| `prop:two-worlds` (l.322-392) | n=3; (G),(LA),(S); V undominated; FA one-sided extensions at worlds 2,3 | FA splices; EDL Steps 1,3 | SURVIVES | FAILS as proved (Step 1 edge Bayes models; Hausdorff limits of *edge* credal intervals) |

---------------------------------------------------------------------------------------------------------------

## 10. Ordinal Refinement by Slack Envelopes (OR)

Background order is **error inclusion** E_i(X) = X △ G_i (l.47-52), not the 4-rank order. Models = all
measurable sets (l.45).

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| Lemmas `lem:elementary`, `lem:stability`, `lem:envelope` (l.113-223) | (1) face support K_p ⊆ Δ_supp p; (2) continuity; (3) compatibility (CC) | (g) face support; (g) (CC); (a) all models | SURVIVE (V=R^n) | Face support puts D_{e_i} = D_i in the family, ∉ proper V ⇒ construction unavailable for proper V. Survive at V=R^n |
| `thm:refinement` (l.258-330) | (1)-(3) | incomplete (b) allowed; (a) | SURVIVES (strict B2 + (S) ⇒ V=R^n by F3, error-inclusion version of the same argument) | SURVIVES at V=R^n only |
| `prop:counterexample` (l.350-383) | n=2, precise family, loss on unit ball | (c); uses A ⊂ B^c ∩ G_1 ∩ {q·g<0} | survives as a counterexample (only needs one setting) | N.A. for proper V (precise family needs V=R^n, F2) |

---------------------------------------------------------------------------------------------------------------

## 11. Loss Relations from Credal Families (LRCF)

Error-inclusion background (B1),(B2) (l.56-69). l.78: "Every ranking here is defined on all models."

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `lem:faces` (l.106-112), `lem:glue`, `lem:bets` | — | — | SURVIVE (pure facts) | SURVIVE |
| `thm:general` (l.174-198) | family orders with (G)-glue,(FC),(ND),(Cl); rank by extension ⪯* | (a) competitors all models; only (B1) | SURVIVES | **SURVIVES verbatim provided every D_p ∈ M_L** (proof only uses covers of X and the family; no outside model is built; no (F) assumed). Because only weak (B1) is assumed, F3 does not force tangency here; whether a non-tangential family satisfying (G),(FC),(ND),(Cl) exists in a proper V is not addressed |
| `cor:upper`, `cor:level` (l.229-248) | (R); (U) | — | SURVIVE | SURVIVE (abstract) |
| `lem:budget` (l.260-278) | (U); (b) needs (F) | (F) face support | SURVIVES | (b) needs (F) ⇒ V=R^n |
| `thm:strict` (l.304-325) | (U),(F),(R) | (F) | SURVIVES | V=R^n only ((F) ⇒ D_{e_i} = D_i) |
| `prop:noclosed` (l.329-337) | (U), (B2), refinement of ⪯* | uses A = {g_i>0, φ_q(g)<0} — can lie outside V | SURVIVES | SURVIVES-WITH-REPAIR when D_q is non-tangential: use A ∩ V, nonempty since g = 1 − c e_j with 1/Ub_q(j) < c < 1/Ub_{K_V}(j) lies in it (Ub_{K_V}(j) < Ub_q(j) when K_V ⊆ relint K_q) |
| `prop:noselection` (l.339-351) | (U),(F),(R),(B1),(B2) | (F); uses σ(e_i) = e_i | SURVIVES | scope is V=R^n ((F)) |
| `prop:family`, `cor:main`, `rem:class` (l.357-417) | M ⊆ int Δ | (F) family, Lipschitz (R); LR loss for (c) | SURVIVE at V=R^n | positive results at V=R^n only. Note: these targets M ⊆ int Δ are exactly the ones that *could* sit non-tangentially in a proper V, but this family cannot |

---------------------------------------------------------------------------------------------------------------

## 12. Loss Relations for Sets of Desirable Gambles (LRSDG)

| Result | Hypotheses | Extra | R1 | R2 |
|---|---|---|---|---|
| `thm:main` (l.118-129, proof l.262-288) | (U),(Lip),(Dom), 0<η<η_0 | (c) real-valued loss; (a) all models; (Dom) ⇒ K_{e_i} = {e_i} and K_p ⊆ Δ_supp p | SURVIVES | SURVIVES at V=R^n only (the family contains D_{e_i} ≈ G_i ∉ proper V). Proof itself is domain-relative (competitiveness uses only the budget inequality for Y) |
| `lem:thin`, `lem:faces`, `lem:twoworlds`, `lem:attain`, `lem:budget`, `lem:box`, `prop:band` | — | (Dom),(Lip),(U) | SURVIVE (math) | SURVIVE (math) |
| Example (v) (l.372, 376-382) | — | — | SURVIVES | SURVIVES (V=R^n) |

---------------------------------------------------------------------------------------------------------------

## 13. Loss Dominance Generalized v2 — appendix from l.483

Appendix assumes (l.484) rankings **generated by a loss L: M_L × Ω → [0,∞]** = extra (b) completeness and
(c) numerical representation.

| Result | Hypotheses | Extra | Verdict (both readings) |
|---|---|---|---|
| `prop:ordinal` (l.498-503) | strictly increasing f_ω | (b),(c) | SURVIVES |
| `lem:bayes-choice` (l.516-521) | c Bayes for finitely supported π, supp π ⊆ S | (b),(c),(d) | SURVIVES, provided "Bayes" = minimiser over **M_L**. **Text issue:** V(p) is defined as inf over **M** (l.493), not M_L; same at l.551, l.558. In a v19 domain this must read M_L, otherwise Bayes models may be outside the domain. Recommend correcting |
| `cor:bayes` (l.529-534) | (I) with lsc losses; (S_∞) | (e) lower semicontinuity of losses along the selection | SURVIVES (gives coherent restricted-Bayes models) |
| `thm:margin` (l.546-563) | (I) lsc; (S_∞) with Bayes choices | (d),(e) | SURVIVES with inf over M_L (fix l.551) |
| `cor:strict`, `cor:upperconvex`, `prop:strict-general` (l.573-643) | + finite losses / V usc | (c),(d),(e) | SURVIVE domain-relative |
| `ex:rescale`, `prop:random` (l.604-631) | M_L=[0,1]^2 | — | SURVIVE (explicitly a restricted domain) |
| `thm:bounds`, `lem:bayesbounds` (l.692-707) | (LA),(I),(B) | — | SURVIVE |
| `prop:threeworld` (l.744-757) | Ω={1,2,3}, **M_L = C_L** (finite toy domain) | — | SURVIVES (already a restricted-domain example) |
| `ex:discontinuous`, `prop:necessary`, `ex:hole` (l.761-793) | — | — | SURVIVE |

---------------------------------------------------------------------------------------------------------------

## 14. Summary of the obstruction picture under a v19-type domain

1. Under the brief's literal non-tangency (R1), **F3 makes every obstruction in this batch survive verbatim**:
   any ranking with strict (G) on mixed problems at the vertex world(s) and (S) must have V = R^n. Proper
   cones are compatible with (S) + R1 only if strict (G) fails at every world near ∂V (agreed exceptional
   system, or Σ_T with T = Ω). VT `prop:neutral` / CNA ε=0 is the only construction here that is R1-admissible
   in a proper V.
2. Under v19b's own reading (R2: only the target non-tangential):
   * targets with credal set in ∂Δ, or lower-dimensional, are forced to V = R^n (F2), so the v3 three-vertex
     obstruction for, e.g., conv{e1,e2,e3} in n ≥ 4 **stands**, as do all "precise/boundary target" results;
   * for full-dimensional targets (the vacuous model when n = 3; any full-dimensional three-vertex target),
     every obstruction proof in v3, CC, CBOI, BA, EDL, FAED **fails as written**, always at the face-support
     step (v3 `lem:bayes-necessary`(c), `prop:bayes-vertex-obstruction`; CC `lem:face`/`cor:face`; EDL and FAED
     edge-threshold structure). The failing models are: ideals D_i/D_j; edge models; models accepting
     g_S>0 with g_j ≪ 0; models giving both recommendations/contradictions; the everywhere-contradictory model;
     v3's E (ball splice) and C∪B. Whether the conclusions hold is UNCLEAR; the natural V-analogue of face
     support is K ⊆ conv(Δ_S ∪ K_V) with forced tangency (F3).
3. Domain-agnostic tools survive in every case: KKM/complete-class lemmas, CC `lem:primary`, EDL
   `thm:leverage`, FAED `lem:cheap`, VT `lem:union`, CNA `thm:closure` (after relativising "every model" and
   "every replacement" to M_L), LRCF `thm:general` (if the family lies in V), LDG appendix (after replacing
   inf over M by inf over M_L at l.493/551/558).
4. Every positive construction in the batch (v3 thm:general/thm:full, CNA thm:limit/boxes, OB, OR, LRCF
   cor:main, LRSDG thm:main) is a V = R^n construction whose boundary selections are ideals or face models;
   none transfers to a proper V as written.
