# N8: structure of U_L for general rankings covering T1 (BRIEF5 Q1)

13 Oct 2026. Labels:
- **PROVED**: full proof written here.
- **CHECKED**: verified, proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

No numerics were needed, so there is no `n8py/`.

Sources:
- LDG = *Loss Dominance Generalized v2* (§§1–3; lem:kkm, thm:kkm, ex:incomparable, ex:rescale).
- v3 = *Full Coverage by Homothetic Credal Families v3* (§1: (G), (IB)).
- IRC = *Incomplete Rankings and Coverage*; FSE = *Fineness Spreads Along Edges*; CCF = *Closed Choice Forces Fineness*.
- R1, R3, R10a, R10b, R15, as corrected in the Consolidated Statements (CS).

---

## 0. Outcome

**Standing hypotheses (SH).** Throughout, n = 3, and:
- M_L is a decomposable domain.
- Each world carries a **preorder** ⪯_i. Completeness is not assumed, nor any numerical, additive or continuity structure.
- Strict (G) holds, together with (LA) and (S): u : Δ → C_L, u_p competitive on supp p against M_L, closed sections A_ω(m) = {p : u_p ⪯_ω m}.
- T = D_K is a coherent target with K ⊆ int Δ, T ∈ C_L, and (LF) holds at T.

Everything is stated for T1, K = (1−ε)u + εΔ, but every proof uses only K ⊆ int Δ. So every claim holds for every ε ∈ (0,1) and for every interior target.

**(IB) is used nowhere. (C) is used only to quote U_L = C_L in C1. Completeness is used only in C12(iii). Transitivity is used only through the invariance of comparisons under ≈ (C1, C2, C5, C12, C13, 3.1(vi)).** So every lower bound below holds for preorders without (IB). Any stronger lower bound must use (IB) or more.

**Advice that every evaluable model gives.** We say that every evaluable model accepts h (in effect) when the advice range of the choice represented by h contains only + and/or × (× = contradictory advice). The advice ranges may be arbitrary outside N, as BRIEF allows.

### (a) What U_L must contain; which earlier steps are ranking-level

**C1 (PROVED). Closed fibres and closed competitiveness sets.** The facts are:
- For every selected profile a, the fibre F_a = {p : u_p ≈ a} is closed.
- For every S ⊆ Ω, the set Z_S = {p : u_p is competitive on S} is closed and contains the face Δ_S.
- For the record, LDG thm:kkm gives U_L = C_L under (LA), (S), (C). (C) is used for this sentence only.

**C2 (PROVED). Reindexing and replacement lemma.** Let u satisfy (S). Then u∘φ also satisfies (S), with the same set of selected models, for:
- every continuous φ : Δ → Δ with supp φ(p) ⊆ supp p;
- every replacement of u_p by a ≈-equivalent member of C_L.

Consequently no statement of the form "the selection is non-constant near the point p₀" holds for any p₀ ∈ Δ (vertex, edge or interior), for any ranking, additive ones included. Only properties invariant under C2 are structural.

**C3 (PROVED). Vertex anchoring at ranking level.** Re-proves R10a Thm V and R10b Prop V. Up to null sets, u_{e_i} = Best_i, the pointwise best advice in the advice range at world i. Moreover:
- Best_i is coherent, Best_i ≈ D_{V_i} with **e_i ∈ V_i**, and V_i ⊆ conv(K ∪ {e_i}). In fact D_{V_i} ⊇ (T ∪ N) ∩ {h_i > 0}.
- V_i ⊆ conv(V_j ∪ {e_i}) (compatibility).
- Gambles accepted (in effect) by every evaluable model have all coordinates positive (a.e.).
- The three vertex profiles are pairwise distinct.

The ingredients are only strict (G), splicing, (S) at δ_i, coherence of u_{e_i}, and the advice ranges on N.

**C4 (PROVED / FALSE-AS-STATED). Face lemma on decomposable domains.**
- For supp p = S, u_p is problemwise S-Pareto: no advice in the advice range is strictly better at every world of S on a non-null set.
- If u_p ≈ D_{K_p}, then K_p ∩ Δ_S ≠ ∅, and K_p ⊆ ∩_{i∈S} conv(V_i ∪ Δ_S). PROVED.
- The all-model face lemma, K_p ⊆ Δ_{supp p} (FSE §1.1, IRC §2.1), is **false on decomposable domains**. Counterexample, CHECKED: R10a Thm M with a common-W tuple, where the edge-index model contains interior points.
- K_p ⊆ Δ_S does hold whenever V_i ⊆ Δ_S for some i ∈ S, for example when V_i = {e_i}.

**C5 (PROVED). The target is competitive only on Ω.** T1 is competitive on no proper subset of Ω. Hence every index carrying T1's profile is interior. This is the ranking-level R1 Prop 2.6.

**C6 (PROVED). Two-pair anchoring (new).** If a coherent c ∈ M_L is competitive on both two-element sets containing world i, then e_i ∈ K_c.

**C7 (PROVED). Triple exclusion (new).** No coherent model of M_L is competitive on all three two-element sets {1,2}, {1,3}, {2,3}. Equivalently Z_{12} ∩ Z_{13} ∩ Z_{23} = ∅.

**Audit (§4, CHECKED).** For each earlier step, §4 records which of additivity, the Bayes structure, completeness or ranking-level facts it uses:
- **Ranking-level:**
  - Thm V / Prop V, Cor V1, V2(a)–(d) (R10a);
  - Lemma D (it is model-level geometry);
  - R1 Prop 2.6;
  - R3 §2.1 and Cor 2.1a. The "completeness" in R3 §2.1's last clause is not needed.
  - The KKM half of R1 Lemma 1.4(i).
- **Not ranking-level:**
  - R10a Lemma E (ranking-level substitute: C4);
  - R10b Cor V2 (continuity at vertices), Lemma FS, UVN, Lemma M, Lemma P, Thm PL, Cor PL2;
  - R1 Lemma 1.4(ii) (interior Bayes uniqueness);
  - all of R15's corner calculus. The only exception is concavity of the support function of one fixed model, which is trivial.

### (b) Plateau test: verdict

**C8 (PROVED). Plateaus of the selection always exist.** Let L satisfy (SH), and in particular T1 ∈ C_L. Then L admits an (S)-selection with u_p = T1 (exactly, not merely ≈) for every p in a nonempty open ball of int Δ. This holds equally for additive rankings. The proof is C2 plus KKM.

So **the plateau test has a positive answer for every ranking that covers T1**. Impossibility cannot be proved at ranking level, or at all, for selections.

**C9 (CHECKED). What Thm PL really needs.** Its object is the **Bayes map** q ↦ B_q of an additive ranking. That object is canonical, unlike an (S)-selection. Thm PL needs:
- (P1) **chart convexity**: for a.e. h, {q : h ∈ B_q} is an intersection of at most two open half-planes;
- (P2) openness of the charts and vertex containment (UVN);
- (P3) Hausdorff continuity of q ↦ K_q (from IBU and dominated convergence);
- (P4) R4 Thm B (adjacency ⇒ degenerate K_q, itself a consequence of (P1)).

(P1) is the indispensable one: Lemma P and Step 3 of Lemma M are convexity arguments in q. None of (P1)–(P4) is defined for a general ranking. The ranking-level residue of Thm PL is C11(b): T1's fibre is compact, avoids ∂Δ, and never fills a component of the strictly interior region.

A class of rankings recovers a PL-type rigidity only if it supplies a canonical index structure with convex charts. One example is a strictly guiding additive weak extension with unique Bayes models, as in R3 §2.2, R5 sandwiched rankings, R11 and R13. To escape, a ranking only has to lack such a structure. No further mechanism is needed.

### (c) Lower bounds on U_L

**C10 (PROVED). Edges.** On each closed edge [e_i, e_j] the selection takes **continuum many** pairwise distinct coherent profiles (Sierpiński). Moreover:
- some nonempty relatively open subset of (e_i, e_j) carries "pure edge" profiles, competitive on {i,j} and on no other pair;
- they too are continuum many.

**C11 (PROVED). Strictly interior profiles (new).**
- (a) The set O = Δ ∖ (Z_{12} ∪ Z_{13} ∪ Z_{23}) is a nonempty open subset of int Δ. Its indices carry profiles competitive on Ω and on no pair ("strictly interior").
- Each connected component of O carries **continuum many** strictly interior profiles, none of which is selected anywhere on ∂Δ.
- T1 is strictly interior (C5).
- (b) T1's fibre F is a compact subset of O, and F ∩ W is a proper, non-open subset of each component W of O that it meets. So F has frontier points p ∈ W, approached by indices q_k → p whose selected models a_k are strictly interior and a_k ≉ T1.

The proof is the dual-KKM lemma applied to Z_{ij} ⊇ [e_i, e_j], plus C7.

**C12 (PROVED). Order-squeeze at the frontier of T1's fibre.** In C11(b):
- (i) for every ω and every m ∈ M_L with T1 ⋠_ω m, a_k ⋠_ω m for all large k;
- (ii) each a_k has a world ω_k with T1 ⋠_{ω_k} a_k;
- (iii) if world ω = ω_k (along a subsequence) is complete, then a_k ≺_ω T1, and for every m ≺_ω T1, eventually m ≺_ω a_k. At every complete world ω′, every m ≺_{ω′} T1 is eventually ≺_{ω′} a_k.

So in the complete case U_L contains, in every order-theoretic sense available, strictly interior profiles converging to T1 from below at some world. **No measure-theoretic closeness follows without a continuity hypothesis.**

**C13 (PROVED for dendrites, CHECKED for finite graphs). No one-parameter factorisation.** Let Y be a dendrite (in particular an arc) or a finite connected graph. There is no continuous ψ : Δ → Y such that u_p ≈ u_q whenever ψ(p) = ψ(q). In particular the selected profile cannot depend only on a continuous real parameter t(p).

**C14 (CHECKED / open). What is not forced by C1–C13.**
- An abstract decomposition of Δ into closed fibres satisfies every combinatorial consequence C1, C7, C10–C13 while being one-parametric near T1: concentric circles on a disc around F_{T1}, with points elsewhere (§6.6).
- Hence "U_L contains a 2-parameter family near T1" and "u is locally injective somewhere" are **not consequences of the ranking-level facts used here**. Whether (IB) forces them is **OPEN**. Neither direction is conjectured here.
- "Non-constant near the edges" is **false** (C2).

**Net.** For general rankings the forced part of U_L consists of:
- three anchored vertex models;
- continuum families on each edge with the face constraints for decomposable domains (C4);
- a nonempty open region of strictly interior indices with continuum many profiles, among which T1 is never alone and never touches the boundary.

The additive no-plateau theorem has no ranking-level counterpart. Its only ranking-level shadow is C11(b).

---

## 1. Setting and the advice-range facts

As in BRIEF5. Write:
- D = T = D_K;
- D_i = {h : h_i > 0};
- Av for the set of orientations h whose acceptance lies in the advice range (some evaluable model accepts h).

**Shrinking N.** Shrink N (R10a §1) so that it is an open cone with N ∩ (−N) = ∅ and N ∩ (−cl D) = ∅, containing no h ≤ 0. Then:

**(A0)** For every h ∈ N, both "accept h" and silence belong to the advice range of the choice represented by h.

*Proof (as R10a §1).* Take R = D ∪ E or R = D ∖ E with E ⊆ N. Then R △ D ⊆ N, so R ∈ M_L by (LF). On N the target never accepts −h, so these R give "accept h" and silence. The advice range contains every advice that some evaluable model gives. ∎

**Strict (G) on decomposable domains.** Let X ∈ M_L, let E be non-null, and let a(g) ∈ A(g) be measurable on E and strictly better at world ω than X's advice for g ∈ E. Then the splice X^E (a on E, X elsewhere) lies in M_L and X^E ≺_ω X. In particular X ⋠_ω X^E. This is used repeatedly as follows.

**Lemma 2.1 (problemwise S-Pareto; PROVED).** Let c be competitive on S. Then for a.e. pair g, no a ∈ A(g) is strictly better than c's advice at every world of S.

*Proof.* Suppose such a exists on a non-null E (measurably). Then the splice m = c^E has m ≺_ω c for every ω ∈ S. So no ω ∈ S has c ⪯_ω m, contradicting competitiveness. Transitivity is not used. ∎

**Gambles of three sign types near ∂T (geometry, PROVED).** Let K ⊆ int Δ.
- (g1) For each i there is w ∈ ∂D ∖ 0 with w_i = 0. Every such w has w_j > 0 > w_k for some labelling {i,j,k} = Ω. (R10a Thm V gives existence. If w_j, w_k ≥ 0, not both 0, then P_K(w) > 0; if both ≤ 0, then P_K(w) < 0.)
- (g2) For each two-element S there is g₀ ∈ ∂D ∖ 0 with (g₀)_S > 0 and (g₀)_k < 0 (R1 Prop 2.6: g(t) = 𝟙_S − t e_k).
- (g3) For i ≠ j there is a point of ∂D near which N contains open sets with h_i > 0 > h_j. Take the zero of t ↦ P_K(e_i − t e_j) and perturb.

For T1 with ε = 0.3, for example:
- w = (1, 0, −0.4375) in (g1);
- g₀ = (1, 1, −0.875) in (g2), with S = {1,2}.

---

## 2. Tools

**Lemma 2.2 (closed fibres and competitiveness sets; PROVED).**
(a) If a = u_q, then F_a := {p : u_p ≈ a} = ∩_ω A_ω(a), which is closed.
(b) For S ⊆ Ω, Z_S := {p : u_p competitive on S} = ∩_{m∈M_L} ∪_{ω∈S} A_ω(m), which is closed. Also Z_S ⊇ Δ_S, and Z_S is a union of fibres.

*Proof.*
- (a) u_p ≈ a gives u_p ⪯ a. Conversely, u_p ⪯ a with u_p ≉ a means u_p dominates a, which is impossible because a ∈ C_L is undominated.
- (b) The identity is the definition. Finite unions and arbitrary intersections of closed sets are closed. If supp p ⊆ S, competitiveness on supp p implies competitiveness on S.
- Fibres: if u_p ≈ u_q, then u_q ⪯_ω m implies u_p ⪯_ω m by transitivity. ∎

**Lemma 2.3 (reindexing and replacement; PROVED).**
(a) Let φ : Δ → Δ be continuous with supp φ(p) ⊆ supp p for all p. Then u′ = u∘φ satisfies (S), and u′(Δ) ⊆ u(Δ).
(b) Let u″_p be any member of C_L with u″_p ≈ u_p. Then u″ satisfies (S).
(c) For every p₀ ∈ Δ there is φ as in (a) with φ ≡ p₀ on a relative neighbourhood of p₀ and φ = id outside a slightly larger one.

*Proof.*
- (a) u_{φ(p)} ∈ C_L is competitive on supp φ(p) ⊆ supp p, hence on supp p. Also {p : u_{φ(p)} ⪯_ω m} = φ^{-1}(A_ω(m)), which is closed.
- (b) By transitivity, u″_p ⪯_ω m ⟺ u_p ⪯_ω m. So the sections and competitiveness are unchanged.
- (c) Let r > 0 with 2r < min{p₀_i : i ∈ supp p₀}. Let λ be continuous on Δ with values in [0,1], λ = 1 on B(p₀, r) and λ = 0 off B(p₀, 2r). Put φ(p) = (1−λ(p))p + λ(p)p₀.
  - φ is continuous.
  - If λ(p) > 0, then |p − p₀| < 2r, so supp p ⊇ supp p₀ and supp φ(p) = supp p.
  - If λ(p) = 0, then φ(p) = p. ∎

This is the content of AUD-1 (C_t = B_{t²}) in full generality. It makes every "local in the index" claim about a selection void.

**Lemma 2.4 (Sierpiński).** A continuum (compact connected metric space) is not a union of countably many, at least two, pairwise disjoint nonempty closed sets. This is a standard theorem. Hence if a continuum is partitioned into at least two closed fibres, it has continuum many fibres.

**Lemma 2.5 (dual KKM; PROVED).** Let A_1, A_2, A_3 be closed subsets of Δ covering Δ, with A_k ⊇ the edge opposite e_k. Then A_1 ∩ A_2 ∩ A_3 ≠ ∅.

*Proof.* Put C_1 = A_2, C_2 = A_3, C_3 = A_1. Check the hypothesis of LDG lem:kkm:
- e_1 ∈ A_2 = C_1, e_2 ∈ A_3 = C_2, e_3 ∈ A_1 = C_3;
- [e_1,e_2] ⊆ A_3 = C_2;
- [e_2,e_3] ⊆ A_1 = C_3;
- [e_1,e_3] ⊆ A_2 = C_1;
- Δ = ∪C_k.

So every p lies in ∪_{k∈supp p} C_k. LDG lem:kkm gives a point of ∩C_k = ∩A_k. ∎

---

## 3. Ranking-level re-proofs and new lemmas

**Theorem 3.1 (vertex anchoring; C3; PROVED).** Under (SH):
- (i) u_{e_i} = Best_i a.e.;
- (ii) Best_i ≈ D_{V_i} with e_i ∈ V_i;
- (iii) D_{V_i} ⊇ (D ∪ N) ∩ D_i, and hence V_i ⊆ conv(K ∪ {e_i});
- (iv) Av ∩ D_i ≈ D_{V_i}, and V_i ⊆ conv(V_j ∪ {e_i});
- (v) every orientation accepted (in effect) by every evaluable model is a.e. strictly positive;
- (vi) u_{e_i} ≉ u_{e_j} for i ≠ j.

*Proof.*
- (i) (S) at δ_i gives u_{e_i} ⪯_i m for all m. If u_{e_i}'s advice were not the best in the advice range at i on a non-null set, splicing would give m ≺_i u_{e_i} (strict (G)), a contradiction. Ranks are distinct, so the best advice is unique.
- (ii) This is Lemma 3.4 below, since Best_i is competitive on every S ∋ i. Alternatively, R10a Thm V's proof uses only (i), (A0) and coherence of u_{e_i} ∈ C_L.
- (iii) T ∈ M_L gives D ⊆ Av, and (A0) gives N ⊆ Av. Best_i accepts every h ∈ Av with h_i > 0. An open set that is a.e. inside the open convex D_{V_i} is inside it. Now D ∩ D_i = D_{conv(K∪e_i)} ⊆ D_{V_i}, and duality of credal sets gives V_i ⊆ conv(K ∪ e_i).
- (iv) By (i)–(ii), Av ∩ D_i ≈ Best_i ∩ D_i ≈ D_{V_i}. Then D_{V_j} ∩ D_i ≈ Av ∩ D_j ∩ D_i ⊆ D_{V_i}. The left side is D_{conv(V_j∪e_i)}. Nested open convex cones correspond to reversed credal inclusion.
- (v) An h accepted (in effect) by every evaluable model is accepted, in particular, by Best_i ⊆ D_i ∪ {h ≥ 0}, for each i.
- (vi) If u_{e_i} ≈ u_{e_j}, then u_{e_j} is ideal at i as well (transitivity), so Best_i = Best_j a.e. On the open set of (g3), accept-h is best at i, while silence (or accept −h) is better at j. ∎

**Proposition 3.2 (face lemma on decomposable domains; C4).** Let supp p = S and u_p ≈ D_{K_p}.
- (a) PROVED: K_p ∩ Δ_S ≠ ∅.
- (b) PROVED: K_p ⊆ conv(V_i ∪ Δ_S) for each i ∈ S.
- (c) CHECKED: (b) cannot be improved to K_p ⊆ Δ_S on decomposable domains.

*Proof.*
- (a) Take h with h_S < 0. Not every evaluable model accepts h (3.1(v)), so silence or accept −h is in the advice range. Each is strictly better than accept-h (bad) or × at every world of S. Lemma 2.1 gives that u_p does not accept h, a.e. So D_{K_p} ∩ {h_S < 0} is null; being open, it is empty. If K_p ∩ Δ_S = ∅, strict separation in aff Δ, extended linearly, gives h with m·h > 0 on K_p and h_S < 0. Contradiction.
- (b) For a.e. h ∈ Av with h_S > 0, accept-h is strictly better than 0, − or × at every world of S. So u_p accepts it (Lemma 2.1). Now Av ∩ {h_S > 0} ≈ D_{V_i} ∩ D_{Δ_S} = D_{conv(V_i∪Δ_S)} for i ∈ S, by 3.1(iv). So D_{conv(V_i∪Δ_S)} ⊆ D_{K_p}.
- (c) In R10a Thm M with M_i = conv{a_i e_i, b_i W̃} and W̃ in the open orthant:
  - the edge Bayes model at p = (½, ½, 0) is K_p = ν(½M_1 + ½M_2) ∋ ν(½b_1w + ½b_2w) = ν(w) ∈ int Δ;
  - the Bayes map is an (S)-selection (R1 Thm 2.2(S); CS: REFEREED-CORRECT). ∎

The all-model face lemma used that + is in the advice range on all of {h_S > 0}. On decomposable domains, + is in the advice range only on D_{V_i} ∩ {h_S > 0}. The (LF) neighbourhood does not restore it away from N.

**Proposition 3.3 (C5; PROVED).** For each two-element S, T is not competitive on S. Hence if u_p ≈ T, then supp p = Ω.

*Proof.*
- Take g₀ from (g2), and a ball B ⊆ N around g₀ with h_S > 0 on B.
- B ∖ cl D is non-null: g₀ ∈ ∂D, and D is an open convex cone.
- There T is silent, since −h ∉ D because N ∩ −cl D = ∅. Accept-h is in the advice range (A0) and good at every world of S.
- Lemma 2.1 is violated.
- If u_p ≈ T, then T is competitive on supp p by transitivity. Competitiveness on a singleton {i} implies it on {i,j}. ∎

**Lemma 3.4 (two-pair anchoring; C6; PROVED).** Let c ∈ M_L be coherent and competitive on {i,j} and on {i,k}, where {i,j,k} = Ω. Then e_i ∈ K_c.

*Proof.*
1. Take w from (g1) with w_i = 0, and label so that w_j > 0 > w_k. Fix a ball B ⊆ N around w on which h_j > 0 > h_k.
2. For h ∈ B with h_i > 0, accept-h is good at i and j. By (A0) it is in the advice range, and it is strictly better than 0, − and × at i and j. So c accepts h a.e. (Lemma 2.1 with S = {i,j}).
3. For h ∈ B with h_i < 0, accept-h is bad at i and k, and silence (in the advice range) is strictly better at both. So c does not accept h a.e. (Lemma 2.1 with S = {i,k}).
4. Hence c ∩ B ≈ {h_i > 0} ∩ B. B contains no nonnegative gamble, so D_{K_c} ∩ B ≈ {h_i > 0} ∩ B. Both sets are open and convex, hence equal.
5. Thus P_{K_c}(w) = 0. Pick m* ∈ K_c with m*·w = 0.
6. For every d with d_i > 0 and small t > 0, w + td ∈ B ∩ {h_i > 0} ⊆ D_{K_c}. So 0 < m*·(w+td) = t m*·d.
7. A linear functional positive on the open half-space {d_i > 0} is a positive multiple of e_i. Test d = e_i + sv with v_i = 0 and all s ∈ ℝ.
8. As m* ∈ Δ, m* = e_i ∈ K_c. ∎

**Theorem 3.5 (triple exclusion; C7; PROVED).** No coherent c ∈ M_L is competitive on all of {1,2}, {1,3} and {2,3}.

*Proof.*
- Lemma 3.4 for each i gives e_1, e_2, e_3 ∈ K_c, so K_c = Δ and c ≈ {h ≥ 0, h ≠ 0}.
- But in step 2 of Lemma 3.4's proof c accepts the non-null set B ∩ {h_i > 0} of mixed gambles. Contradiction. ∎

The proof needs only the pairs {i,j} and {i,k} for each i, and the existence of the (g1) crossings, which every interior target has. It does not need general position of a triangle, unlike R10a Thm R and R15.

**R3 §2.1 re-checked (PROVED, completeness-free).**
- If u_q = C* on Q and p ∈ cl Q, closedness of A_i(C*) ∋ Q gives u_p ⪯ C*. So u_p ≈ C* if C* is undominated.
- If p = e_k and C* ≠ Best_k on a non-null set, strict (G) gives Best_k ≺_k C*, contradicting ∼_k.
- No completeness is used. Cor 2.1a (e_k ∉ cl{q : u_q = T}) follows, and is superseded by C5: cl F_T ∩ ∂Δ = ∅.

---

## 4. Audit of the earlier steps

Key:
- **RL** = ranking-level (uses only (G), (S) competitiveness and closed sections, (LF) advice ranges, coherence of selected models, splicing, transitivity).
- **A** = additivity of the losses.
- **B** = Bayes structure (selected model = per-problem minimiser of q·ℓ at index q).
- **Co** = completeness.

| Step | Uses | Ranking-level status |
|---|---|---|
| R10a Thm V (vertex anchoring) | (S) at δ_i, strict (G), (LF), coherence | **RL**. Re-proved as Thm 3.1 |
| R10a Cor V1 (acceptance by every evaluable model) | Thm V | **RL** (3.1(v)) |
| R10a Cor V2(a)–(d) (advice ranges = compatible tuple) | Thm V, T ∈ M_L, (LF) | **RL** (3.1(iii)–(iv)) |
| R10a Prop V4 converse (Thm M) | A, B | construction, additive |
| R10a Lemma E (boundary Bayes models meet the face) | B at boundary priors | not RL. **RL replacement: 3.2(a)** for the selected boundary model |
| R10a Thm M, Thm R, Thm P | A, B; concave chart representatives; R4 (K1),(K3) | not RL |
| R10b Prop V | same as Thm V | **RL** |
| R10b Cor V2 (Hausdorff continuity at vertices) | B + dominated convergence | not RL; **false** for selections (Lemma 2.3) |
| R10b Lemma FS (forbidden support near q₀) | B: a strict gap at q₀ persists at nearby q_η | not RL. Survives only at q₀ itself (3.2(a)) |
| R10b Lemma UVN | B: charts contain vertex neighbourhoods by continuity in q | not RL |
| R10b Prop L | A (construction) | n/a |
| R10b Lemma D (dichotomy) | geometry of one coherent model | **RL** (model-level) |
| R10b Lemma M | (P1) half-plane charts, (P3) Hausdorff continuity, (P4) R4 Thm B, UVN | not RL |
| R10b Lemma P | (P1) chart convexity: R(h) ⊇ O ∪ B_A ⇒ R(h) ⊇ conv | not RL |
| R10b Thm PL, Cor PL2 | Lemmas M, P, UVN | not RL; its object is the Bayes map |
| R3 §2.1, Cor 2.1a | closed sections, undominatedness, strict (G) | **RL**; "complete" in the last clause is superfluous |
| R1 Prop 2.6 (interior target prior) | strict (G), (LF) | **RL** (Prop 3.3) |
| R1 Lemma 1.4(i) | KKM (RL) + "Bayes ⇒ undominated" (A) | KKM half RL (U_L = C_L) |
| R1 Lemma 1.4(ii) (IBU) | B: splices of two minimisers of q·ℓ are minimisers | not RL. See remark below |
| R15 Thm 1 (corner calculus), Lemma 4.1, Prop 5.2, Thm 5.1, Lemma 6.1, Thm 6.2 | (DF),(ND) on q ↦ P_{K_q}; chart rows c(g) with strict signs (A, B); box from Lemma FS (B) | not RL. Only concavity of one model's support function survives, and it is trivial |
| FSE/IRC face lemma (K_p ⊆ Δ_{supp p}) | + in the advice range on all of {h_S > 0} (all-model domain) | **false on decomposable domains** (3.2(c)); RL replacement 3.2(a),(b) |
| IRC (T2) | closed sections + edge competitiveness | **RL** on decomposable domains (verbatim) |
| IRC (T1) | Co | RL only at complete worlds |
| IRC edge models (α,β), connecting chains, counting lemma | all-model (regular-model) freedom; (IB) | **not available** on decomposable domains with (LF) only near T. Splices are restricted to the advice ranges; edge models need not have the (α,β) form |

**Remark (no ranking-level IBU; CHECKED).** Let X ∼_ω Y, split their disagreement set into symmetric A_1 ⊔ A_2, and let:
- W = X on A_1, Y on A_2;
- Z = Y on A_1, X on A_2.

(IB) gives X ⪯_ω W ⟺ Z ⪯_ω Y and W ⪯_ω X ⟺ Y ⪯_ω Z. These are compatible with Z ≺_ω X ∼_ω Y ≺_ω W even for complete additive worlds: L(W) − L(X) = ∫_{A_2}(ℓ_Y − ℓ_X), which need not vanish. So (C), (IB) and completeness do not make splices of tied models tied. R1 1.4(ii)'s mechanism (minimisers of a *weighted* objective splice) and R5 Lemma TJ's mechanism (Lyapunov with additive tie functionals) have no ranking-level analogue. Whether two distinct members of C_L can be tied at every world is open for general rankings. Nothing below uses it.

---

## 5. The plateau test

**Theorem 5.1 (C8; PROVED).** Assume (SH). There is an (S)-selection u′ for L, with u′(Δ) ⊆ u(Δ) ∪ {T}, and an open ball B ⊆ int Δ, such that u′_p = T for all p ∈ B.

*Proof.*
1. By LDG thm:kkm with m = T, some u_{p*} ⪯ T. T is undominated, so u_{p*} ≈ T. By Prop 3.3, p* ∈ int Δ.
2. Replace u_q by T wherever u_q ≈ T. This is allowed by Lemma 2.3(b), since T ∈ C_L.
3. Compose with φ from Lemma 2.3(c) at p₀ = p*. ∎

**Corollary 5.2.** Thm PL (R10b) and N3 Thm PL_θ cannot be read as statements about selections: for additive rankings too, a selection may plateau at T1.

**Proposition 5.3 (C9; CHECKED). Exactly what PL needs.** Thm PL is a theorem about the Bayes map B : q ↦ B_q of an additive ranking with IBU. Every step uses at least one of:
- (P1) for a.e. h, the chart {q : h ∈ B_q} is the intersection of at most two open half-planes in q (R1 Prop 2.1), in particular convex. Lemma P uses "R(h) ⊇ O ∪ B_A ⇒ R(h) ⊇ int conv(O ∪ B_A)". Lemma M Step 3 compares two affine functionals q ↦ a_±·q.
- (P2) UVN: charts contain fixed vertex neighbourhoods (continuity of q ↦ q·ℓ(g,·)).
- (P3) q ↦ K_q is Hausdorff-continuous on int Δ (IBU + dominated convergence + R1 Prop 3.1).
- (P4) R4 Thm B: an adjacent pair's d-face priors have K_q ⊆ g^⊥. This is derived from (P1) and IBU.

(P1) is the load-bearing ingredient: (P4) is derived from it, and (P2)–(P3) only localise it. For a general ranking:
- there is no canonical map from indices to models;
- the set of indices at which a fixed gamble is accepted by an (S)-selection is an arbitrary set compatible with C1, and Lemma 2.3 can make it non-convex and non-open.

So a ranking escapes PL by doing nothing special. The escape needs only that no canonical convex-chart index structure is present.

Such a structure is present, and PL-type rigidity returns for the associated Bayes map, when the ranking has a strictly guiding additive weak extension with a.e.-unique interior Bayes models (R3 §2.2, R5 sandwiched worlds, R11 Thm W, R13 Prop S, CCIBU). In that case the coverage question reduces to the additive one, as in BRIEF5.

**Ranking-level residue of PL.** This is C11(b) (Theorem 6.2(b) below). The fibre of T1:
- is compact;
- avoids ∂Δ;
- lies in the strictly interior region O;
- never contains a component of O.

So T1 cannot be the only strictly interior profile near it. This holds for every ranking satisfying (SH), with no additivity, completeness or (IB).

---

## 6. Lower bounds

**Theorem 6.1 (edges; C10; PROVED).** Fix i ≠ j and let k be the third world.
(a) The closed edge [e_i, e_j] meets continuum many fibres.
(b) E′ := (e_i, e_j) ∖ (Z_{ik} ∪ Z_{jk}) is nonempty and relatively open. Its indices carry profiles competitive on {i,j} and on no other pair. Each component of E′ meets continuum many fibres.

*Proof.*
- (a) Fibres meet the edge in closed sets (Lemma 2.2(a)). At least two of them are nonempty, by Thm 3.1(vi). Apply Lemma 2.4 to the edge.
- (b), first part.
  - Z_{ik} ∩ [e_i,e_j] ∋ e_i and Z_{jk} ∩ [e_i,e_j] ∋ e_j are closed.
  - They are disjoint: a common point lies in Z_{ij} as well (edge index), contradicting Thm 3.5.
  - The edge is connected, so the two sets cannot cover it.
- (b), second part.
  - Let I be a component of E′, an open interval (a, b). Its endpoints lie in Z_{ik} ∪ Z_{jk} or at a vertex, hence not in E′.
  - If I carried one profile c, the fibre F_c would be closed and contain [a, b]. Then the endpoint profiles would equal c's profile and so be competitive only on {i,j}, contradicting endpoint ∈ Z_{ik} ∪ Z_{jk}.
  - So I meets at least two fibres. Any closed subinterval meeting two of them is a continuum partitioned into closed fibres, so Lemma 2.4 applies. ∎

**Theorem 6.2 (strictly interior profiles; C11; PROVED).**
(a) O := Δ ∖ (Z_{12} ∪ Z_{13} ∪ Z_{23}) is nonempty, open, contained in int Δ, and a union of fibres. Each component W of O meets continuum many fibres. Their profiles are competitive on Ω and on no pair, and none is selected at any boundary index.
(b) F := F_T ⊆ O is compact. For each component W with W ∩ F ≠ ∅, W ∩ F is a proper subset of W that is not open in W.

*Proof.*
- (a)
  - Z_{ij} is closed and contains [e_i, e_j] (Lemma 2.2(b)).
  - If the three sets covered Δ, Lemma 2.5 (with A_k = Z_{ij}, the set containing the edge opposite e_k) would give a common point, contradicting Thm 3.5.
  - O ∩ ∂Δ = ∅, because boundary indices lie in some Z_{ij}.
  - Fibre-saturation follows from Lemma 2.2(b).
  - Let W be a component of O. W is open in ℝ² ∩ aff Δ, hence path-connected. If W met exactly one fibre F_c, then W ⊆ F_c ∩ O. Since F_c is closed and O is a union of fibres, F_c ⊆ O. Then cl W ⊆ F_c ⊆ O, so ∂W = ∅ and W is clopen in Δ. That is impossible, since ∅ ≠ W ≠ Δ.
  - So W meets at least two fibres. An arc in W joining points of two fibres is a continuum partitioned into closed fibres (at least two), and Lemma 2.4 gives continuum many.
  - Boundary indices carry profiles competitive on some pair, so these profiles are never selected on ∂Δ.
- (b)
  - F ⊆ O by Prop 3.3 and fibre-saturation; F is closed in compact Δ.
  - If W ⊆ F, then cl W ⊆ F ⊆ O, and the clopen argument above applies. So W ∩ F ≠ W.
  - W ∩ F is relatively closed and nonempty, and W is connected, so W ∩ F is not open in W. ∎

**Proposition 6.3 (order squeeze; C12; PROVED).** Let p ∈ W ∩ F be a non-interior point of F relative to W. Take q_k ∈ W ∖ F with q_k → p and put a_k = u_{q_k}. Then the a_k are strictly interior, a_k ≉ T, and:
- (i) if T ⋠_ω m, then a_k ⪯_ω m for only finitely many k;
- (ii) for each k there is ω_k with T ⋠_{ω_k} a_k;
- (iii) for any world ω equal to ω_k along a subsequence: if ⪯_ω is complete, then a_k ≺_ω T along it, and every m ≺_ω T has m ≺_ω a_k eventually. At every complete world ω′, every m ≺_{ω′} T has m ≺_{ω′} a_k eventually.

*Proof.*
- (i) Otherwise p ∈ cl A_ω(m) = A_ω(m), i.e. T ≈ u_p ⪯_ω m.
- (ii) T ⪯ a_k with a_k undominated forces T ≈ a_k.
- (iii) Completeness turns "⋠" into "≻". Then apply (i) to m with m ≺_ω T. ∎

The evaluable m include every strict pointwise ω-improvement of T (using advice in the advice ranges) on any non-null set, in particular inside N. So in the complete case T is an order-limit of other strictly interior members of U_L. Without a continuity hypothesis linking ⪯_ω to convergence in measure, nothing says a_k → T in measure. A hypothesis of that kind would be extra, e.g. (MC): X ⪯_ω m_n for all n and m_n → m monotonically in measure ⇒ X ⪯_ω m.

**Theorem 6.4 (no one-parameter factorisation; C13).** Let ψ : Δ → Y be continuous with u_p ≈ u_q whenever ψ(p) = ψ(q).
- (a) PROVED: Y is not a dendrite (e.g. an arc or a tree).
- (b) CHECKED: Y is not a finite connected graph.

*Proof of (a).*
1. Put y_i = ψ(e_i). P_{ij} := ψ([e_i,e_j]) is a subcontinuum of Y containing y_i and y_j. Subcontinua of dendrites are dendrites, hence arcwise connected, and arcs in a dendrite are unique. So P_{ij} ⊇ [y_i, y_j], the unique arc (a point if y_i = y_j).
2. The arcs [y_2,y_1] and [y_2,y_3] intersect in an arc [y_2, c], by unique arcwise connectedness.
3. [y_1,c] ∪ [c,y_3] is an arc from y_1 to y_3, so it equals [y_1, y_3] ∋ c. Hence c ∈ [y_1,y_2] ∩ [y_2,y_3] ∩ [y_1,y_3].
4. Pick p_{ij} ∈ [e_i,e_j] with ψ(p_{ij}) = c. Then u_{p_{12}} ≈ u_{p_{23}} ≈ u_{p_{13}}.
5. Each u_{p_{ij}} is competitive on supp p_{ij} ⊆ {i,j}. By transitivity the common profile is competitive on all three pairs, contradicting Thm 3.5. ∎

*Sketch of (b).* ψ∘(boundary loop) is null-homotopic in Y, since it extends over Δ. So it lifts to a closed loop in the universal cover, which is a tree. Apply the median argument there to the lifted images of the three edges, which are compact connected subsets of a tree, and project. ∎

**6.6 What is not forced (C14; CHECKED, abstract).** Consider the following abstract decomposition of Δ:
- take a closed disc Ď ⊆ int Δ, foliated into concentric circles together with the centre;
- make every other point a singleton fibre;
- let Z_{ij} be the closed δ-neighbourhood of [e_i,e_j], with δ small enough that the three neighbourhoods have no common point and miss Ď.

It satisfies every combinatorial consequence derived above:
- the fibres are closed;
- Z_S is closed, contains the faces and is fibre-saturated;
- triple exclusion holds;
- each edge has continuum many fibres;
- O ⊋ Ď, with continuum many fibres in each component;
- taking F_T to be one circle, Theorem 6.2(b) holds;
- no factorisation through a dendrite or graph exists.

Near F_T it is one-parametric. So "U_L contains a two-parameter family near T1" and "u is locally injective somewhere" do not follow from C1–C13. This example is not a ranking. It shows only that a proof of either claim must use something not used here, most plausibly (IB), possibly together with (C). Whether a ranking satisfying all axioms can realise such a thin decomposition is the construction question BRIEF5 Q2. **OPEN.**

---

## 7. Remarks for Q2 and next steps

1. **The binding ranking-level constraints on a T1-covering ranking.** These are Thm 3.1, Prop 3.2, Prop 3.3, Lemma 3.4, Thm 3.5 and Theorem 6.2. They are the only places where T enters, and they enter only through the advice ranges on N, i.e. only through the (g1)–(g3) crossings.
   - In particular, by C11, a construction must provide an open set of indices whose models are competitive on Ω but on no pair.
   - It must also provide an "interior continuum" of such models, in the order-closure sense of C1.
   - Closed sections must be verified for every m in the domain, not only for the selected models.
2. **Where additional rigidity could come from.** (IB) has been used nowhere. The all-model papers (IRC, CCF, FSE) get their strength from (IB) via counting and connecting chains on edges. On decomposable domains these must be redone with splices restricted to the advice ranges. Near T only N is free, so the chains live inside N ∪ Av.
3. **Edge index sets.**
   - On decomposable domains, edge models need not have the (α,β) form: K_p ∩ edge ≠ ∅ only.
   - The FSE/IRC edge machinery transfers only where Av ⊇ {h_S > 0}, for instance where V_i = {e_i}.
   - Choosing small vertex sets V_i is therefore a design freedom that a construction can use. It weakens every edge argument imported from the all-model work.
4. **Ranking-level plateaus.** By C8 a T1-covering ranking can always be presented with a plateau at T1. Any Q2 construction may assume one without loss of generality. It must then supply the rest of O (C11).
