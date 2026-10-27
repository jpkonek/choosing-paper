# N10: referee report on N8 (structure) and N9 (constructions), BRIEF5

13 Oct 2026. Independent referee. I checked every load-bearing claim line by line against LDG v2 §§1–3 (preorder rankings,
LDG-competitiveness, (S) with u : Δ → C_L, lem:kkm, thm:kkm, rem:order, ex:incomparable), v3 §1 ((G), (IB)),
R10a/R10b, R2 (Lemma U, Thm 7) and the Consolidated Statements.
Script: `n10py/checks.py` (NUMERICS only). It re-runs N9's numbers, checks the N8/N9 example gambles, tests a general form
of the Design-B witness, and gives a toy check of the (A_T) direction.

Verdict key:
- **C** = CORRECT.
- **CR** = CORRECT WITH REPAIR (repair given).
- **GAP** = argument incomplete, or claim not supported as stated.
- **F** = FALSE as stated (counterexample or reason given).

---

## Summary table

| # | Claim | Verdict | One-line reason / repair |
|---|---|---|---|
| N8 C1 | Closed fibres F_a; Z_S closed, ⊇ Δ_S, saturated | **C** | Uses only closed sections, undominatedness and transitivity |
| N8 C2 | u∘φ (φ continuous, supp φ(p) ⊆ supp p) and ≈-replacement preserve (S) | **C** | Minor: in Lemma 2.3(c), supp φ(p) ⊆ supp p, not "=" (they differ where λ = 1); only ⊆ is used |
| N8 C3 | Vertex anchoring: u_{e_i} = Best_i, e_i ∈ V_i, compatibility, accepted by every evaluable model ⇒ positive, vertex profiles distinct | **C** | Coherence of u_{e_i} is legitimate, since (S) maps Δ into C_L. "≈" is overloaded (a.e. equality vs profile tie); say which |
| N8 C4 | Face lemma for decomposable domains (a), (b); all-model face lemma false on decomposable domains | **C** | Counterexample (R10a Thm M, common-W) is valid with T = a Thm-M target, not T1. For T1-covering systems it is open (none known) |
| N8 C5 | T1 competitive on no proper S; T1-indices interior | **C** | — |
| N8 C6 | Competitive on both pairs ∋ i ⇒ e_i ∈ K_c | **C** | Uses only "not strictly dominated on S" plus availability on N |
| N8 C7 | No coherent model competitive on all three pairs | **C** | — |
| N8 R3 §2.1 | Completeness-free | **C** | — |
| N8 audit table | RL / non-RL classification | **C**, one cell **GAP** | "R10b Cor V2 false for selections (Lemma 2.3)" is unsupported: C2 *preserves* continuity at vertices. Replace with "not ranking-level" |
| N8 C8 | Selection plateau at T1 always exists | **C** | Also for additive rankings |
| N8 C9 | What Thm PL needs: (P1)–(P4) | **CR** | Add (P5) strict sign-respect of the canonical chart vectors at crossings and vertices (UVN(a), Lemma M step 4). This is exactly what N9's Design C lacks. "(P1) indispensable" and "escape by doing nothing" are heuristics: lacking a canonical structure escapes PL's *proof*, not the obstruction |
| N8 C10 | Edges: "continuum many" fibres; pure-edge set E′ ≠ ∅ with many fibres | **CR** | Sierpiński gives **uncountably** many, not 𝔠 (a partition of [0,1] into ℵ₁ closed sets is consistent with ¬CH). The rest is correct |
| N8 C11(a) | O = Δ∖∪Z_ij nonempty, open, interior; each component meets many fibres | **CR** | Same cardinality repair. Dual-KKM reduction to lem:kkm checked |
| N8 C11(b) | F_T compact ⊆ O; F_T∩W proper, not open | **C** | — |
| N8 C12 | Order squeeze at the frontier of F_T | **C** | Completeness only in (iii), as stated |
| N8 C13 | No continuous factorisation through dendrite / finite graph | **C**; (b) upgradable to **PROVED** | Lift ψ itself to the universal cover (a tree), since Δ is simply connected. ψ̃(Δ) is a finite subtree; apply (a) |
| N8 C14 | Abstract one-parameter decomposition satisfies the combinatorial consequences | **CR** | True for C1, C7, C10, C11, C13. C12 is order-theoretic and is not tested by the example. The example shows only that *these* consequences are insufficient; it does not show that (IB) is what is missing |
| N8 global | "(IB) unused; completeness only in C12(iii); valid for every interior target" | **CR** | Shrinking N with N∩(−cl D) = ∅ needs K full-dimensional (K spanning ℝ³). It fails for segment targets (T3), where (A0) and Prop 3.3 need re-checking |
| N9.1 | Selection plateau free | **C** | Same as N8 C8 |
| N9.2(a) | Closed tie fibres; uncountably many on each edge | **C** | (Correct cardinality) |
| N9.2(b) | Lemma R | **C** | — |
| N9.2(c) | Edge repulsion; "T + three edge families" impossible | **C** | Equivalent to N8 C11 (F_T ⊆ O, O open) |
| N9.3 | Dominator accumulation under (A_T) | **C** (proof); remark **F** | The remark is reversed: (A_T) *holds* for lex rankings whose primary is blind on W_k, and *fails* when the primary strictly registers the loss (take C with F(C) = F(T), S(C) > S(T)). No proof uses the remark. On general decomposable domains, W_k ⊆ N is needed |
| N9.4 | Binary-domain normal form (qualitative-measure preorders) | **C** | — |
| N9.5 | Lex-IBU in 𝓛₂ | **C** | Restricted class. Uses (C) and the model-level splice step of R2 Lemma U |
| N9.6 | Face-continuum theorem FC | **C** | Restricted class (𝓛₂, additive levels). Rests on R2 Thm 7 (refereed C) |
| N9.7 | Design A: (a)–(f) | **C** | Prop 4.4 is correct, and its hypothesis c_F ≠ 0 is not needed for its conclusion. "More generally … under genericity" is CHECKED-level only |
| N9.8 | Design B: Prop 4.5 + explicit witness | **C** (witness), **CR** (general claim) | The general claim needs error-strictness at a world j with g_j < 0, g ∉ cl Z, and t → e_j through a.e.-good t. A witness then exists for *every* such g (§2.8; numerics 300/300) |
| N9 §4.4 / N9.9 | Design C reduces to a weak-sign additive chart problem | **GAP** | Misses the case where T is lex-undominated but is a primary-Bayes model only non-uniquely or only at boundary weights (T on a primary face, decided by the secondary). Also "thin U_L impossible in Design C regardless" is **F**: Design A is a Design-C instance with a constant lex-Bayes family |
| N9 Conj. N9 | Dichotomy free set / FC | conjecture; loosely posed | "Prop 4.5 then applies" needs the free set to contain a collar of ∂T∖0. A free set elsewhere gives decoupled undominated models but no incoherence witness |
| N9.9 | Residual; an impossibility would contain the additive T1 problem | **C** | Important for the frontier (§4) |
| Joint (i) | Additive obstructions do not lift | **CR** | True of the *proofs* for general preorders. False if read as covering lex classes: lex-IBU lifts (N9.5), and Prop 4.4 + FC is a lex analogue of PL. No ranking is known where their *conclusions* fail under (S) |
| Joint (ii) | Decisive question = must U_L contain a 2-parameter family near T1; a proof would need (IB) | **not correct / not well-posed** | See §4 for the corrected frontier |

---

## 1. N8, line by line

**Ground rules checked throughout.**
- Competitiveness is used in LDG's preorder sense. Every model-level consequence N8 draws (Lemma 2.1, problemwise S-Pareto) uses only the weaker corollary "no member of M_L is strictly better at every world of S". That corollary does follow (LDG §1).
- Closedness of Z_S (C1(b)) genuinely needs LDG's sense, and N8 uses it there.
- Coherence of boundary-index selected models is an axiom, not an assumption: LDG (S) takes u : Δ → C_L. The brief's warning concerns *Bayes* models at boundary priors. N8 never uses those, so its uses of coherence of u_{e_i} and of edge-index models (C3, C4, C6, C7) are legitimate.
- No argument assumes that selections are Bayes for their indices, or that they are continuous.
- KKM is used in three places: thm:kkm (U_L = C_L, quoted); KKM with m = T (C8); dual KKM (Lemma 2.5). In Lemma 2.5 I checked the relabelling C_1 = A_2, C_2 = A_3, C_3 = A_1 against every face condition of lem:kkm. It is correct.

**C1 (Lemma 2.2).**
- (a) Let p ∈ ∩_ω A_ω(a). Then u_p ⪯ a, and since a is undominated, u_p ≈ a.
- (b) Z_S = ∩_m ∪_{ω∈S} A_ω(m) is an intersection of finite unions of closed sets. Δ_S ⊆ Z_S because competitiveness on supp p ⊆ S gives competitiveness on S. Saturation follows by transitivity.

**C. C2 (Lemma 2.3).**
- (a), (b): correct.
- (c): for i ∈ supp p₀ and |p − p₀| < 2r we have p_i > 0, so supp φ(p) = supp p ∪ supp p₀ = supp p when λ(p) < 1. When λ(p) = 1, supp φ(p) = supp p₀ ⊆ supp p. Only "⊆" is needed.
- At a vertex, p₀ = e_i works, giving u ≡ Best_i near e_i.

**C. C3 (Thm 3.1).**
- (i) The splice giving the best advice in the advice range is measurable, because advice ranges are measurable. Strict (G) and ideality at i give u_{e_i} = Best_i. Uniqueness holds because the four ranks are distinct.
- (ii) Best_i is ideal at i, hence competitive on every S ∋ i, so Lemma 3.4 applies.
- (iii) T ∈ M_L puts "+" in the advice range on D, and (A0) does the same on N. Open sets a.e. inside an open convex set lie inside it (separation through a boundary point leaves a non-null half-ball outside). Also D_K ∩ D_i = D_{conv(K∪e_i)}.
- (iv) D_{V_j} ⊆ D_j ∪ {h ≥ 0} because e_j ∈ V_j. Then the nested-cone duality applies. Implicitly, Av must count an orientation as in Av when "+" (or "×") is in its advice range. Advice ranges {×} alone are a.e. absent because Best_i is coherent.
- (v), (vi): checked. For (vi), use the (g3) open set (verified: w = e_i − t*e_j).

**C. C4 (Prop 3.2).**
- (a) On {h_S < 0}, it is not the case that every evaluable model (effectively) accepts h, by 3.1(v). So 0 or − is in the advice range, and each is strictly better than + or × at every world of S. Strict separation in aff Δ, extended linearly (0 ∉ aff Δ), produces h.
- (b) Av ∩ {h_S > 0} = D_{V_i} ∩ D_{Δ_S} for i ∈ S, by 3.1(iv). Correct.
- (c) In R10a Thm M with M_i = conv{a_i e_i, b_i W̃}, ½M_1 + ½M_2 ∋ ½(b_1 + b_2)w, so ν(w) ∈ K_{(½,½,0)} ∩ int Δ. The Bayes map is an (S)-selection (Thm M(c)), and the target there is D_{K_{p*}} (for example the hexagon), which satisfies SH.
- So the all-model face lemma is false under SH. For T1 itself it is merely unprovable by the old route.

**C. C5 (Prop 3.3).**
- The g₀ example (1, 1, −0.875) is verified: V·g₀ has minimum 0.
- On B∖cl D, T is silent, because −h ∈ D would put h ∈ −cl D ∩ N = ∅.
- Lemma 2.1 then applies. Transfer along ≈ uses transitivity.

**C. C6 (Lemma 3.4), C7 (Thm 3.5).**
- I re-derived every step. The (g1) example (1, 0, −0.4375) is verified (min V·w = 0).
- Step 6: a linear functional that is positive on {d_i > 0} is a positive multiple of e_i. Test d = (δ, −M, 0)-type vectors.
- Thm 3.5: K_c = Δ forces c ≈ D_Δ, which accepts no mixed gamble. But c accepts the non-null mixed set B ∩ {h_i > 0}. Correct.
- These two lemmas are the genuinely new ranking-level content and are sound.

**R3 §2.1 re-check: C.** Completeness is indeed not needed.

**Audit table (§4).** I spot-checked every row against R10a/R10b (read for this report):
- Lemma FS uses the q₀-gap persisting at q_η.
- UVN uses dominated convergence in q.
- Lemma P uses convexity of R(h) (G′ = int conv(O ∪ B_A)).
- Lemma M step 1 uses Hausdorff continuity and R4 Thm B; steps 3–4 use the affine chart lines and strict signs.

The classification is right, with one exception:
- *Cell "R10b Cor V2 … false for selections (Lemma 2.3)": GAP.* A C2-reindexing u∘φ is continuous at e_i whenever u is, because φ(e_i) = e_i and φ is continuous. Lemma 2.3 therefore does not produce a vertex discontinuity.
- What is true: the statement is not ranking-level (it needs a topology on models and IBU). Whether some (S)-selection of an additive IBU system can be L¹-discontinuous at a vertex is not settled here; closed sections give only lower semicontinuity of losses.
- Repair: "not RL; not established for general selections."

I did not independently re-verify the IRC rows (T1)/(T2); they are not load-bearing for N8's results.

**IBU remark: C.** Let W = X|A₁ ∪ Y|A₂ and Z = Y|A₁ ∪ X|A₂. Then (IB) gives exactly X ⪯ W ⟺ Z ⪯ Y and W ⪯ X ⟺ Y ⪯ Z. The additive example L(W) − L(X) = ∫_{A₂}(ℓ_Y − ℓ_X) = L(Y) − L(Z) shows that Z ≺ X ∼ Y ≺ W is consistent. So world-wise ties do not splice.

**C. C8 (Thm 5.1).** KKM with m = T gives an interior p* (Prop 3.3). Replace by T (Lemma 2.3(b)), then compose with φ (Lemma 2.3(c)).

**CR. C9 (Prop 5.3).** The list (P1)–(P4) is accurate as far as it goes, but one further ingredient is load-bearing:
- **(P5) strict sign-respect of the canonical chart vectors.** UVN(a) needs acceptance to be the *strict* minimiser at e_i on N ∩ {h_i > 0}. Lemma M step 4 needs (a₋)_c ≤ 0 together with UVN(a) at w₊. Lemma FS needs a strict gap at q₀.
- (P5) is precisely what fails in N9's Design C, where the lex-Bayes map has half-plane charts, so (P1) holds, but c_F is only weakly sign-respecting.
- So "(P1) is the indispensable one" is not supported. A class with (P1) but without (P5) does not automatically fall under PL. That is N9's open zero-pattern problem.
- Also, "to escape, a ranking only has to lack such a structure" should read "to escape PL's *proof*". Escaping the coverage obstruction is a different matter (§4).

**CR. C10 (Thm 6.1).**
- (a) The edge is a continuum partitioned into ≥ 2 nonempty, pairwise disjoint closed fibres (vertex profiles are distinct by 3.1(vi)). Sierpiński gives **uncountably** many fibres.
- "Continuum many" (= 𝔠) does not follow. It is consistent with ¬CH that [0,1] is a union of ℵ₁ pairwise disjoint closed sets (Stern; Miller for 2^ω). Repair: "uncountably many" here and in Lemma 2.4, C11 and the Net. Nothing downstream uses 𝔠.
- (b) Z_ik ∩ edge and Z_jk ∩ edge are closed, nonempty and disjoint: a common point lies in Z_ij, contradicting C7. The edge is connected, so E′ ≠ ∅.
- On a component (a, b) carrying one fibre, closedness puts the endpoints in that fibre. Saturation of Z then puts the whole interval in Z_ik ∪ Z_jk. Contradiction. Correct.

**CR / C. C11 (Thm 6.2).**
- (a) The clopen argument is correct: W ⊆ F_c ⊆ O gives cl W ⊆ O, so cl W = W (W is a component). The cardinality repair applies.
- (b) Correct.

**C. C12 (Prop 6.3).**
- (i) By closedness and transitivity, T ≈ u_p ⪯_ω m.
- (ii) By undominatedness of a_k.
- (iii) Completeness converts ⋠ into ≻.
- The caution "no measure-theoretic closeness" is right and important (§4).

**C. C13 (Thm 6.4).**
- (a) The median argument in a dendrite is sound. It uses hereditary unicoherence: the intersection of two arcs from y₂ is an arc [y₂, c].
- (b) It is cleaner to lift ψ itself. Δ is simply connected and locally path-connected, so ψ lifts to ψ̃ : Δ → Ỹ, the universal cover, which is a tree. ψ̃(p) = ψ̃(q) implies ψ(p) = ψ(q). ψ̃(Δ) is a compact connected subset of a locally finite tree, i.e. a finite subtree, hence a dendrite. Apply (a). This is **PROVED**.

**CR. C14 (§6.6).**
- The decomposition does satisfy C1, C7, C10, C11 and C13. C10(b) holds because E′ = edge minus the δ-neighbourhoods is nonempty.
- C12 is a statement about orders and is vacuous for an order-free decomposition. Remove it from the list.
- The legitimate conclusion: *the index-combinatorial consequences derived in N8 do not force two-parameter structure or local injectivity.*
- It does **not** follow that a proof "must use (IB)". The decomposition discards all model-level content: which coherent sets carry which fibres, KKM-domination of every member of M_L, the geometry of coherent sets near T, and (C). To show that (IB) is necessary one would need a non-(IB) ranking, satisfying everything else, with thin U_L near T1. None is exhibited. N8 itself hedges correctly ("most plausibly (IB), possibly together with (C)"). The joint conclusion does not.

**CR. Global hypothesis claim.** "Every proof uses only K ⊆ int Δ" is wrong for lower-dimensional K. The shrink N ∩ (−cl D) = ∅ uses ∂D ∩ (−cl D) = {0}, which needs K to span ℝ³ (R10a §1 states this). For a segment K ⊆ int Δ, ±w ∈ ∂D for w ⊥ span K. Then (A0) needs the variant R = (D∖{−h}) ∪ {h}, and Prop 3.3's "T silent on B∖cl D" needs re-checking. For T1 there is no issue.

---

## 2. N9, line by line

**C. 2.1 N9.1 (Prop 2.1).**
- Interiority is shown with a different set from N8's: silence T on accepted gambles with h_k > 0 > h_l (l ≠ k) near ∂T. Such boundary points exist; e.g. (−a, −b, c) on F_1 with a > b > 0, verified in `checks.py`. Silence (no advice) is in the advice range by (LF).
- φ with λ = 0 on ∂Δ is support-non-enlarging. Correct.

**C. 2.2 N9.2.**
- Lemma 3.1 = N8 C1(a). "Uncountably many" is the correct cardinality.
- Lemma R: the finite union of the closed sets A_ω(X), ω ∈ S, misses p, which gives (i). (ii) follows from competitiveness on supp q.
- Cor 3.3: X_12 strictly improves T at worlds 1 and 2 (gamble verified: V·h = (0, +, +) on F_1). X_12 ≺_ω T ∼ u_p.
- The "minimal thin design" consequence is correct, provided "edge family" means models competitive on some pair, which includes everything selected at edge indices.

**2.3 N9.3 (Prop 3.4): proof C; remark F.**
- D_k ≠ ∅ by Fact 0(a). D_k ∩ P_T = ∅ by strictness at the gain world.
- Limits: T + W_k ⪯_ω T + W_j for k ≥ j at loss worlds, by weak (G). Closedness gives u_{p̄} ⪯_ω T + W_j for all j, and (A_T) gives u_{p̄} ⪯_ω T.
- The proof gives more than "dist → 0": every limit point of any p_k ∈ D_k lies in P_T, i.e. sup_{D_k} dist(·, P_T) → 0.

*The remark "(A_T) … fails for lex rankings with a primary that is blind on the W_k" is reversed.* At a loss world ω with ⪯_ω = lex(F, S):
- **Primary blind on W_k.** Then F(T + W_k) = F(T), and C ⪯_ω T + W_k for all k gives either F(C) < F(T), or F(C) = F(T) with S(C) ≤ S(T + W_k) → S(T). So (A_T) **holds**.
- **Primary strict on W_k.** Then F(T + W_k) ↓ F(T) strictly. Any C with F(C) = F(T) and S(C) > S(T) satisfies C ⪯_ω T + W_k for every k but not C ⪯_ω T. So (A_T) **fails** whenever such a C exists in M_L.
- Toy check in `checks.py`.
- (Curiously, in Design A no such C exists at T, because T is S-worst on its primary face.)
- Repair: swap the attribution. Note also that only C = u_{p̄} matters, so (A_T) can be restricted to selected models. On a general decomposable domain the W_k must lie in N.
- N9.3's summary sentence ("non-Archimedean neighbour … lexicographic rankings supply such neighbours") is correct.
- Prop 3.4's own uses of (A_T) are unaffected.

**C. 2.4 N9.4 (Prop 1.1).**
- M_U, the U-domain (evaluable models: the measurable subsets of U = D_{K′}), is a decomposable domain: advice range {+,0} on pairs with an orientation in U (indexed by that orientation), and {0} on pairs {g,−g} with g ∉ U and −g ∉ U.
- (LF) at T holds with N = U: R △ D ⊆ U and D ⊆ U give R ⊆ U.
- cl D_K ∖ 0 ⊆ U because K′ ⊆ int K.
- E_i(X) = X △ P_i, and "pointwise at least as good at i" ⟺ E_i(X) ⊆ E_i(Y).
- (IB) with A = the symmetrised disagreement set gives exactly cancellation A ≤ B ⟺ A∖B ≤ B∖A. Conversely, cancellation gives (IB).
- Strict (G) ⟺ strict monotonicity.

**C. 2.5 N9.5 (Lemma 4.1).**
- Lex-t-Bayes models are exactly the pointwise lex-minimisers of (t·φ, t·ψ), so splices of two of them are lex-t-Bayes.
- R2 Lemma U's incoherent-splice step (radial truncation) is model-level and transfers.
- The F-then-S equality argument with t interior is correct and uses (C).
- Restricted class (𝓛₂). No Bayes-for-index assumption on the selection is made.

**C. 2.6 N9.6 (Thm FC).**
- Y_λ is not even weakly dominated by any other model: Z ⪯ Y_λ gives Z ∈ 𝔐_i and Φ_λ(Z) ≤ Φ_λ(Y_λ), and (FC1) applies.
- Fact 0(b) gives a selected model with equal (F_j, S_j), hence improvable at j.
- R2 Thm 7 (refereed C; I re-read the proof: improvable p is a local minimum of f_j; countable base) gives countably many levels, contradicting (FC2).
- "Whatever the target" is correct.

**C. 2.7 N9.7 (Design A, Prop 4.2, Lemma 4.3, Prop 4.4).**
- (a) The primary table is weakly guiding and the lex composite strictly guiding, which gives strict (G). Both levels are integrals, which gives (IB).
- (b), (c) Every h ∈ U∖T has a negative coordinate (nonnegative gambles lie in T), and every h ∈ T a positive one.
- (d) t·c_F(h) has T's sign for every interior t.
- (e) Q is F_i-tied with P_i, while L_i(A) − L_i(P_i) ≥ ∫_Q gap > 0 and L_i(B) − L_i(P_i) → 0.
- (f) / Lemma 4.3:
  - 𝔐_1 and Q_1 are correct, and so are the move rule and J(h).
  - (FC1): ties lie on a cone surface.
  - (FC2): reproduced; the ratio range on the J = {2} shell is (0, 2.28), and F_2 excess 0.0057 → 0 over λ₂ ∈ [0.2, 5]. The shell is a non-null open set, so the ratio has a density there.
  - (FC3): T ∩ P_1 ∩ {h_2 < 0} is non-null and F_2-tied.
- Prop 4.4: correct. The hypothesis c_F ≠ 0 is not needed for "X* minimises every F_i", since t·c_F(h) ≥ 0 for a.e. t gives c_F(h) ≥ 0.
- The extension "any constant-lex-Bayes system … FC applies under genericity" is a CHECKED-level heuristic, not a theorem. The summary should label it so.

**2.8 N9.8 (Design B). Prop 4.5: C. Witness: C. General claim: CR.**
- Witness verified: V·h = (0.5625, 0, 0.5625), V·h′ = (0.4969, 0.3469, 0), P_K(g)/‖g‖ = 0.1681.
- The density step is correct, because a coherent cone that contains most of B(h, r) and of B(h′, r) contains B(h, r/2) + B(h′, r/2) = B(g, r).

The general sentence "error-strict at some point g ∈ int D_K ∖ Z" needs three repairs:
- (1) The error-strict world j must have g_j < 0, with c_F(·)_j < 0 near g. Primary rewards at worlds where g is positive give no rejection of g.
- (2) g ∉ cl Z.
- (3) t → e_j through t's at which primary-t-Bayes is a.e. unique off Z. By Fubini this is a.e. t, which suffices; "within Θ" needs Θ to accumulate at e_j.

With these repairs **a witness exists for every such g**:
- Pick i with g_i > 0.
- For a boundary direction w, P_K(g − λw) is concave in λ, positive at 0 and → −∞ (since −w ∉ cl D). So h′ = g − λ(w)w ∈ ∂D for a unique λ(w) > 0.
- Take w near a coordinate-i crossing (w_i = 0, (g1)) with w_i > 0 small. Then h = λ(w)w and h′ = g − h both lie in ∂D ⊆ Z, with h_i > 0 and h′_i ≈ g_i > 0.
- `checks.py` finds such a pair for 300/300 random g ∈ int D_K with a negative coordinate.

**2.9 Design C (§4.4) and N9.9: GAP, plus one false sentence.**
- The reduction "c_F ≠ 0 a.e. ⇒ U_L ⊇ an int-Δ-indexed primary-Bayes family that must be coherent" is correct (Lemma 4.1). But coverage also needs T ∈ U_L, and T's relation to that family is not settled.
- By Lyapunov the primary profile set is convex. If T minimised t·F for no t ∈ Δ, some Y would have F(Y) < F(T) at every world, and Y would lex-strictly dominate T. So T is primary-t-Bayes for some t ∈ Δ.
- That t may be on ∂Δ, or T may be one of a non-null face of primary-t-minimisers, with the secondary deciding. Neither case reduces to the "weak-sign additive chart problem", and PL-type questions about plateaus of the primary family are then beside the point.
- These are FC-type face cases and must be listed as a separate residual: (C-i) T is the a.e.-unique primary-t*-Bayes model at an interior t*; (C-ii) T lies only on a primary face, at a boundary or non-unique weight.
- "A thin U_L is impossible in Design C regardless" is **false as stated**. Design A has c_F ≠ 0 a.e. and a constant lex-Bayes family, so the indexed family can be a single model. Thinness fails there through FC, not through the indexing.
- Conjecture N9 is a legitimate conjecture but loosely posed. "Strict-additive cover" is undefined. "Prop 4.5 then applies" holds only if the free set contains a collar of ∂T∖0; a free set elsewhere yields decoupled undominated models but no incoherence witness.
- **C:** "(A_T) and per-problem chart structure are additive or continuity inputs".
- **C, and important:** "proving no design exists would include the open additive T1 problem". Additive rankings satisfy (A_T), Prop 3.4, Cor 3.3 and the rest of (a)–(c), and additive coverage of T1 is excluded only conditionally (R15: (DF), (ND), (NA_w)).

**C. 2.10 Warm-up.** N9.1 shows that plateau-freedom of the Bayes map is never by itself an obstruction to coverage.

---

## 3. Reconciling N8 and N9

1. **Plateau.** N8 C8 = N9.1, with the same φ-construction and different interiority witnesses; both are valid. Both correctly conclude that PL concerns a canonical map, not selections.
2. **Edge repulsion vs pure-edge continuum and O.** These are consistent, and in fact the same fact seen from two sides.
   - N9 Cor 3.3: F_T has a neighbourhood containing no index whose model is competitive on a pair. This is exactly N8's F_T ⊆ O with O open (Z_ij closed, and T competitive on no pair).
   - N8's pure-edge profiles live on E′ ⊆ ∂Δ ∩ Z_ij, a closed set disjoint from a neighbourhood of F_T.
   - "T + three edge families impossible" (N9) is the special case of N8 C11(a)/(b): the frontier of F_T in its component W of O is approached by indices in W∖F_T, which carry strictly interior non-T profiles.
3. **Cardinality.** N9's "uncountably many" is right; N8's "continuum many" needs the repair above.
4. **Order squeeze vs dominator accumulation.**
   - N8 C12 needs completeness at some world but no Archimedean hypothesis. It gives, along index sequences converging to ∂F_T, models a_k ≺_ω T that are eventually worse than every m ≺_ω T.
   - N9 Prop 3.4 needs (A_T) but no completeness. It gives, for each gain class, selected dominators of T + W_k converging to P_T.
   - They are complementary. Neither gives measure-theoretic or Hausdorff closeness to T.
5. **Vertex models.** N9's P_i on M_U is N8's Best_i = D_{V_i} with V_i = conv(K′ ∪ e_i), and N8 C3(iii) holds there.
6. **C9 vs Design C.** N9's Design C supplies exactly the counter-case to N8's "(P1) is indispensable": half-plane charts are present, strict signs are absent, and PL's status is open. Hence the (P5) repair to C9.

---

## 4. The joint conclusion and the frontier

**(i) "Additive obstructions do not lift to ranking level": CORRECT WITH REPAIR.**
- Correct reading: the *proofs* of R1 1.4(ii) (IBU), R10b Lemma FS / UVN / M / P / Thm PL and R15's corner calculus use objects that a general preorder ranking does not have:
  - a canonical index → model map;
  - half-plane charts in the index;
  - continuity of pointwise minimisers in the weight (Archimedean continuity);
  - strict chart signs.
- No ranking-level substitute has been found. The ranking-level analogue of IBU ("no two distinct members of C_L are tied at every world") is open (N8 remark).
- Repairs:
  - (a) "Do not lift" is a statement about proofs. No ranking satisfying (S) is known in which their *conclusions* fail. The selection plateau is not their conclusion.
  - (b) In the lex class 𝓛₂ they partly do lift: N9.5 is lex-IBU, and Prop 4.4 + FC is a PL-type obstruction for the canonical lex-Bayes map (conditional on FC1–FC3).
  - (c) Several additive steps are ranking-level and survive: Thm V, Lemma D, R1 Prop 2.6, R3 §2.1, Lemma E in the form N8 C4(a), and the new C6/C7.

**(ii) "The decisive open question is whether U_L must contain a two-parameter family near T1, and a proof that it must would need (IB)": NOT CORRECT and NOT WELL-POSED.** There are four defects.

1. **Not well-posed.** "Near T1" and "two-parameter" need a topology on U_L, and none is fixed.
   - Index topology is not invariant: C2 reindexing changes the fibre picture.
   - Index-nearness yields only order-nearness (C12). With no continuity hypothesis linking ⪯_ω to convergence in measure, members of U_L indexed near F_T may be far from T1 in Hausdorff distance of credal sets. Even whether T1 can be Hausdorff-isolated in U_L is open.
   - So the question must name a topology, e.g. Hausdorff distance on {K_c : c ∈ C_L}, before it says anything.
2. **Not decisive in either direction.**
   - A forced two-parameter family is not a contradiction. Additive systems that cover interior polygons arbitrarily close to T1 (R10a Thm M, Prop M′) have two-parameter U_L. The additive no-go needed specific incoherence mechanisms (corner calculus, box), not thickness.
   - Conversely, coverage does not require thinness: a thick U_L that is entirely coherent would do.
   - Thinness is a design heuristic, not the frontier.
3. **The (IB) clause is unproved.** C14 shows only that the index-combinatorial consequences listed are insufficient. A proof of any lower bound could also use model-level content not used in C14: KKM-domination of every member of M_L, the geometry of coherent cones near ∂T, and (C). "Needs (IB)" would require a non-(IB) ranking, satisfying everything else, with thin U_L near T1. None is exhibited.
4. **It skips the additive case.** By N9.9, any ranking-level impossibility contains the additive T1 problem. That problem is still open in R15's escape cases (E1)–(E4) (only conditionally excluded). A "thickness" lemma cannot be the missing step unless it also closes those cases.

**Justified frontier statement (replacement).** Setting: n = 3, T1 (any ε ∈ (0,1)), decomposable domains, preorders, strict (G), (IB), (LA), (S), (C), (LF) at T1.

- **(F0) Status.** Coverage of T1 is open in both directions. The additive subcase is itself open: it is excluded only conditionally (R15 needs (DF), (ND), (NA_w); escapes (E1)–(E4)). Every ranking-level impossibility must also settle the additive case.
- **(F1) Proved necessary structure** (no additivity, no (IB), no completeness unless stated). These are necessary conditions, mutually consistent, realisable index-combinatorially by thin decompositions, and so incapable by themselves of excluding coverage:
  - vertex anchoring and compatibility (N8 C3);
  - the face lemma for decomposable domains (C4);
  - T1 strictly interior (C5);
  - two-pair anchoring and triple exclusion (C6, C7);
  - closed fibres and Z_S (C1);
  - uncountably many edge, pure-edge and strictly-interior profiles (C10, C11);
  - F_T compact in O and nowhere filling a component (C11(b));
  - Lemma R and edge repulsion (N9.2);
  - order squeeze at complete worlds (C12);
  - no factorisation through a tree or graph (C13);
  - dominator accumulation under (A_T) (N9.3).
- **(F2) What an impossibility proof must do.** Exhibit a forced *incoherent* member of U_L, i.e. a forced undominated model violating convexity, as in the Design-B witness. Every known mechanism for this uses an ingredient missing for general preorders:
  - (a) a canonical index → model map with half-plane charts **and** strict chart signs (IBU / PL / R15; in 𝓛₂, lex-IBU + Prop 4.4);
  - (b) an Archimedean link between ⪯_ω and convergence in measure ((A_T), or N8's (MC));
  - (c) a quantitative-level count (FC via R2 Thm 7) or decoupling geometry (Prop 4.5).

  The open ranking-level question is whether (IB) + (S) + (C) (with strict (G) and (LF)) supply a substitute for (a)–(c) near ∂F_T. One example would be an (IB)-splice argument between T and the order-converging a_k of C12 that produces a non-convex undominated model. Proving that U_L is two-dimensional would be neither necessary nor sufficient for this.
- **(F3) Construction side, well-posed form.** On the binary domain M_U (N9.4), coverage of T1 is achieved iff there are:
  - three preorders ≤_i on the measure algebra of U = D_{K′} that are strictly monotone and cancellative;
  - a map u : Δ → {D_M : M ⊇ K′} with T1 = u(p*);
  - such that u_p is competitive on supp p in the error-set sense (for every X, some i ∈ supp p has E_i(u_p) ≤_i E_i(X));
  - the sections {p : E_i(u_p) ≤_i E_i(X)} are closed;
  - and (C) holds.

  A positive answer settles coverage. A negative answer settles only this domain.
- **(F4) Inside 𝓛₂ the residual is sharp:**
  - (C-i) T is the a.e.-unique primary-t*-Bayes model at an interior t*. This is the weak-sign (good~silence and bad~silence zeros) additive chart problem: do PL/R15 analogues survive without (P5)?
  - (C-ii) T is reached only on a primary face (boundary or non-unique weight). This needs an FC-type analysis.
  - Free-set designs whose free set contains no collar of ∂T∖0 are untested.
  - Non-lex non-Archimedean preorders remain unexamined.
- **(F5) Thinness, if pursued,** must be posed in a named topology on U_L (e.g. "can U_L ∩ B_Haus(K, r) be a set of covering dimension ≤ 1, or {T1}?"). It should be presented as a design target, not as the decisive question.

---

## 5. Scripts

`n10py/checks.py` (NUMERICS, run with `python3 -I`):
- the N8 (g1)/(g2) gambles and the N9 Cor 3.3 gambles lie on ∂D_K as claimed;
- the N9 Design-B witness;
- the generalised witness of §2.8, 300/300 random g;
- the (A_T) direction check: blind primary → (A_T) holds; strict primary → it fails.

N9's `n9py/checks.py` was re-run and reproduces its stated numbers.
