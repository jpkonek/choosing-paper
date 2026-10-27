# PP19. Sections near T: what any (S)-selection must look like around T's tie fibre

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof given here. CHECKED: exact exhaustive computation over finite cells, used only to check the bookkeeping of a proof (rank tables, copy identities). Finite cells are atoms and say nothing about (S); no CHECKED item below is offered as evidence about (S). OPEN / CONJECTURE: as stated.

**Script.** `r9/PP19_py/pointwise.py` (run `python3 -I -B pointwise.py`; output in `pointwise.out`, ALL PASS).

**Inputs used.** Audit's note `AUDIT_six_source.md` (§§1, 2, 9–14), the lead's `LEAD_selection_count.md` (Lemmas A–E), and the referee report `REFEREE_six_source.md` (PP17), in particular: Lemma A and Lemma E hold for undominated but unselected T; fibre accumulation (cl F_N ⊆ Φ_N); Theorem C(iii) cannot be settled by closedness data alone; T has no defence in audit's module against X* = T[A_1 ∪ A_2 → majority]; and installing target-reference records at every worsening world makes the C_i dominated.

---

## 0. Verdicts

| Question | Answer | Where |
|---|---|---|
| Q1. Which worlds can selected models near T's tie fibre Φ_T use? | Against any fixed rival X, only worlds at which X is **not** strictly better than T. This holds on an open neighbourhood N(X) of Φ_T whose size depends on X. For majority fills X_E on M_k this means world k only; for minority fills, worlds i or j only. Sections put **no** restriction on which world is used against T itself; the restriction there is by type (Prop 1.2). Uniformity in E is OPEN. Sources accumulating at Φ_T obey a Ramsey dichotomy. | Thm 1, Cor 1.1, Props 1.2, 2, 3 (PROVED) |
| Q2. Where must the KKM dominators of X_E sit? | In one of three pairwise disjoint classes Dom_1, Dom_2, Dom_3, at a rival-dependent positive distance from Φ_T, off the opposite closed edge (when there are no ties). Each dominator is defended against by T only at the minority world, refuses there every strict improvement of T, and **must carry a compensation set outside E**: audit's B_i and R_i are forced, not design choices. A two-source version constrains how majority-fill and minority-fill dominators may share compensation. | Thms 4, 5, 6 (PROVED) |
| Q2'. Is audit's discontinuity compatible with closed sections when sources move? | Yes. The discontinuity is **forced** for every dominator at some world (Thm 7(a)). Moving the source changes it in one of exactly two ways (Thm 7(b)): either the dominators approach Φ_T, and then acceptance becomes non-monotone in the rival; or the limit model is itself not tied with T. Neither conflicts with fixed-rival sections. | Thm 7 (PROVED); Remark 7.1 |
| Q3. Do (IB) copies between nearby sources break (TC) or undominatedness? | Copies between disjoint or nested supports only reproduce existing T/source relations (Lemma 8). Copies of **partial-source** records do bind: T must refuse T[D′ → C] at some world, for every selected C and every non-null D′ ⊆ {C ≠ T}, unless there is an all-world tie. This is the axiom-level form of the referee's all-worlds failure. No necessary obstruction to a continuum of reciprocal sources was found. The source layer alone has a consistent local skeleton, so any obstruction must come from rivals whose records cross source supports. | Lemma 8, Prop 9, Prop 10 (PROVED); obstruction OPEN |
| Q4. The tie escape | Genuinely open, but now reduced. Theorem 1 and Props 2–3 transfer to an unselected T. Theorems 4–6 do not apply to T itself: they apply to its selected tie partner C, with C's own fills. New necessary conditions: tie-partner refusals, direct-(C) transport, and dominators of T must touch {C ≠ T}. Theorem C(iii) stays open; the referee's §7.3 shows closedness facts cannot settle it. | Prop 11 (PROVED); verdict OPEN |

---

## 1. Setting and tools

**Problems, classes and ranks.** Problems are g ∈ R³ mod sign. Write M_k for the mixed problems whose minority world is k, and U for the unanimous ones. Advice relative to the majority orientation is A (majority answer), S (silence), B (minority answer), X (contradiction).
- On M_k at world k, the ranks are B 0, S 1, A 2, X 3.
- On M_k at the two majority worlds i, j, they are A 0, S 1, B 2, X 3.
- On U, they are A 0, S 1, B 2, X 3 at every world.

Write a <_w b at g if r_w(a, g) < r_w(b, g). Write Y ≤_w X pointwise if r_w(Y(g)) ≤ r_w(X(g)) a.e.

T = T1 = D_M, with M = c·1 + εΔ. T is coherent, never X, A on U, and strictly silent on open sets in every M_k.

**Records and copies.** rec(X, Y) is the disagreement set D = {X ≠ Y} together with X|_D and Y|_D. A copy is any pair (Z[D → X], Z[D → Y]). (IB): X ⪯_w Y iff every copy is accepted at w.

**Axioms used.**
- Strict (G): Y ≤_w X pointwise implies Y ⪯_w X, and strictly so (Y ≺_w X) if strict on a non-null set.
- (TC): A ⪯_w B ⪯_w C implies not C ≺_w A.
- (S): every C_p is coherent and undominated; C_p is competitive on supp p; every A_w(X) := {p : C_p ⪯_w X} is closed.
- Direct (C), only where stated: a model tied at every world with a coherent undominated model is coherent and undominated.

**Standing hypothesis (H).** (S) holds with T = C_{p*} at an interior index p*, so T is competitive at all three worlds. Write W_T(X) := {w : T ⪯_w X} (nonempty for every X) and I(X) := {w : X ≺_w T}. Write Φ_T := {p : C_p ≈ T}, where ≈ is the all-world tie.

**Fill rivals.** For non-null E ⊆ M_k ∩ {T ≠ A}, the majority fill is X_E := T[E → A]. For F ⊆ M_k ∩ {T ≠ B}, the minority fill is Z_F := T[F → B]. By strict (G), I(X_E) = {i, j} and I(Z_F) = {k}.

**Lemma 0.1 (inheritance; PROVED).** If p_n → p and p_n ∈ A_w(X) for all n, then p ∈ A_w(X). This is closedness of the section.

**Lemma 0.2 (audit §1, exact form; PROVED).** Let N be any model and w any world. If C ⪯_w X for some X with X ≺_w N, then N ⋠_w C.
*Proof.* Otherwise N ⪯_w C ⪯_w X ≺_w N, which violates (TC). ∎
Only (TC) is used. Nothing requires C to dominate X or to be selected. The conclusion is "N ⪯_w C fails". It does **not** say that C is strictly better than N at w: C and N may be incomparable at w.

**Lemma 0.3 (lead's Lemmas A and E, with the referee's strengthening; PROVED there).** If T is undominated (selected or not), then Φ_T is closed. It is also a compact subset of the open simplex.

**Lemma 0.4 (exposure against every undominated model; PROVED).** Suppose C ⪯_w X at every w, and N is undominated with N = X a.e. on D := {C ≠ X}. Then N[D → C] ≈ N. In particular, if some C ⪯_v X is strict, there is a contradiction.
*Proof.* (N[D → C], N) is a copy of rec(C, X). So N[D → C] ⪯_w N at every w, strictly at v if C ≺_v X. Since N is undominated, no comparison is strict and all reverses hold. ∎
For N = T this is audit's §2.

---

## 2. Q1: competitiveness near the tie fibre

**Theorem 1 (exclusion near Φ_T; PROVED).** Let X be any model. For every w ∈ I(X), A_w(X) ∩ Φ_T = ∅. Hence N(X) := Δ \ ⋃_{w ∈ I(X)} A_w(X) is an open neighbourhood of Φ_T, and δ(X) := dist(Φ_T, ⋃_{w ∈ I(X)} A_w(X)) > 0. Every selected C_q with q ∈ N(X) is competitive against X only at worlds in supp q \ I(X).

*Proof.* Let p ∈ Φ_T, so T ⪯_w C_p. If C_p ⪯_w X with X ≺_w T, Lemma 0.2 (with N = T) is violated. The sets A_w(X) are closed and Φ_T is compact (Lemma 0.3), which gives δ(X) > 0. The last sentence is the definition of N(X). ∎

**Corollary 1.1 (the three rival types; PROVED).** Shrink N(X) inside the open simplex. Then for q ∈ N(X):
- **Majority fills.** C_q ⪯_k X_E, and C_q ⋠_i X_E, C_q ⋠_j X_E.
- **Minority fills.** C_q ⪯_i Z_F or C_q ⪯_j Z_F, and C_q ⋠_k Z_F.
- **Referee's X\*.** For X* = T[A_1 ∪ A_2 → A], strict (G) gives 3 ∈ I(X*). So near Φ_T the models must defend against X* at world 1 or 2: the defence T itself lacks in audit's module.
- **Sources.** If C is a selected source with C ≺_1 T and C ≺_2 T (audit's pattern for a world-3 source), then C_q ⪯_3 C and C_q ⋠_{1,2} C.

All of these neighbourhoods depend on the rival.

**Proposition 1.2 (against T itself: type, not sections; PROVED).** Φ_T ⊆ A_w(T) for every w, so sections impose nothing on which world a nearby C_q uses against T. Write V(q) := {w : C_q ⪯_w T} and I_T(C) := {w : C ⪯_w Y for some Y ≺_w T}. Then for every selected C_q not tied with T:
- (a) V(q) is nonempty and proper;
- (b) W_T(C_q) is nonempty and disjoint from I_T(C_q);
- (c) V(q) \ W_T(C_q) ⊆ I_T(C_q).

*Proof.*
- (a) Nonempty by competitiveness. If V(q) were everything, then since T is undominated no comparison is strict, so C_q ≈ T.
- (b) Nonempty because T is competitive. Disjoint by Lemma 0.2.
- (c) If C_q ⪯_w T and T ⋠_w C_q, then C_q ≺_w T, and C_q ⪯_w C_q witnesses w ∈ I_T(C_q). ∎

**Proposition 2 (dependence on E; PROVED except (d)).**
- (a) δ(X_E) > 0 for every E.
- (b) Let q_n → Φ_T. For each fixed X, only finitely many q_n lie in ⋃_{w∈I(X)} A_w(X).
- (c) Hence inf_E δ(X_E) = 0 iff there are q_n → Φ_T and E_n with C_{q_n} ⪯_w X_{E_n} for some w ∈ {i, j}. In that case each model X_{E_n} occurs only finitely often: the accepted fills escape every fixed rival.
- (d) **OPEN.** Whether inf_E δ(X_E) > 0 (a uniform T-mimic collar) or = 0 (creeping acceptance). None of the results here decides it.
- (e) **Fibre separation.** If there are no distinct all-world ties, the fibres F_N are compact and pairwise disjoint (Lemma A), so dist(F_N, F_T) > 0 for every selected N ≠ T. Without that hypothesis, cl F_N ∩ cl F_T is contained in the set of indices whose model is tied with both N and T (referee, fact (a)).

*Proof.* (a) and (b) are Theorem 1, and (c) follows from (b). For (e): cl F_N ⊆ Φ_N because Φ_N is closed. A common point q has C_q ∈ {N or ≈ N} ∩ {T or ≈ T}. If C_q = T or C_q = N, then N ≈ T. ∎

**Proposition 3 (sources accumulating at Φ_T; PROVED).** Let q_n → q_0 ∈ Φ_T with every q_n interior, and C_n := C_{q_n}.
- (a) For each m there is N(m) such that for n ≥ N(m), C_n ⪯_w C_m only for w ∉ I(C_m).
- (b) Suppose every C_n follows audit's pattern for a world-3 source (C_n ≺_1 T and C_n ≺_2 T). Then some subsequence (n_k) has, for all j < k, C_{n_k} ⪯_3 C_{n_j} and C_{n_k} ⋠_{1,2} C_{n_j}, and one of the following:
  - (i) for a fixed w ∈ {1, 2}, C_{n_1} ≺_w C_{n_2} ≺_w ⋯ (a strict ascending chain at w; every term is ≺_w T);
  - (ii) all pairs are tied at world 3 and mutually incomparable at worlds 1 and 2.

*Proof.*
- (a) Apply Theorem 1 to X = C_m.
- (b) Here I(C_m) ⊇ {1, 2}, so (a) and competitiveness give C_n ⪯_3 C_m and C_n ⋠_{1,2} C_m for n ≥ N(m). Choose n_{k+1} ≥ max_{j ≤ k} N(n_j).
  - Colour each pair j < k by the least w with C_{n_j} ⪯_w C_{n_k}; such a w exists because C_{n_j} is competitive.
  - The infinite Ramsey theorem gives an infinite homogeneous set.
  - Colour w ∈ {1, 2}: C_{n_j} ⪯_w C_{n_k} together with C_{n_k} ⋠_w C_{n_j} gives a strict ascent.
  - Colour 3: by minimality C_{n_j} ⋠_{1,2} C_{n_k}, and C_{n_k} ⪯_3 C_{n_j} holds in both directions. ∎

---

## 3. Q2: the dominators

### 3.1 Three classes

For each world k, with the other two worlds i and j, put 𝒳_k := {X : X ≺_i T and X ≺_j T}, Dom(X) := ⋂_w A_w(X) (closed), and Dom_k := ⋃_{X ∈ 𝒳_k} Dom(X).

**Theorem 4 (dominator classes; PROVED).**
- (a) I_T(C) ≠ {1, 2, 3} for every model C, selected or not.
- (b) Suppose C ⪯_i X and C ⪯_j X′ for some X ≺_i T and X′ ≺_j T (in particular, if C weakly dominates some X ∈ 𝒳_k). Then:
  - T ⋠_i C and T ⋠_j C, while T ⪯_k C (possibly a tie at k);
  - C ⋠_k Y for every Y ≺_k T, and in particular for every minority fill on M_k.
- (c) Dom_1, Dom_2 and Dom_3 are nonempty for T1, pairwise disjoint, and disjoint from Φ_T. Moreover Dom(X) ∩ N(X) = ∅.
- (d) (opposite edge) Assume T is tied at all worlds with no distinct model. Then for every majority fill X_E with E ⊆ M_k, Dom(X_E) misses the closed edge [e_i, e_j].

*Proof.*
- (a) Lemma 0.2 at every world would leave W_T(C) = ∅, contradicting T's competitiveness.
- (b) The first part is Lemma 0.2 at i and j, plus competitiveness for T ⪯_k C. If C ⪯_k Y with Y ≺_k T, then T ⪯_k C ⪯_k Y ≺_k T violates (TC).
- (c) Majority fills on the silent part of M_k lie in 𝒳_k, and KKM gives each one a dominator. A point in Dom_k ∩ Dom_l would give I_T = {1, 2, 3}, contradicting (a). Disjointness from Φ_T is Theorem 1.
- (d) Let p ∈ [e_i, e_j], so C_p is competitive at i or j.
  - **C_p says A on M_k.** If E′ := M_k ∩ {C_p ≠ A} were non-null, then Y := C_p[E′ → A] would satisfy Y ≺_i C_p and Y ≺_j C_p by strict (G). So C_p = A a.e. on M_k.
  - **The copy into T.** Hence D := {C_p ≠ X_E} misses E, and X_E = T on D. If C_p ⪯_w X_E at all w, the copy of rec(C_p, X_E) in context T gives T[D → C_p] ⪯_w T at all w. Since T is undominated, this is a tie; by the hypothesis, T[D → C_p] = T, so C_p = X_E a.e.
  - **C_p ≠ X_E.** C_p = A on all of M_k, so X_E would be the full fill on M_k. Any coherent D_K with A on all of M_k has K in the face m_k = 0. On M_i, take the open set near h = (−1 at i, η at j, L at k) with L > 1/c and η small. T accepts there, since every m ∈ M has m_k ≥ c. D_K accepts only if every m ∈ K has m_i ≤ η m_j for all small η, which forces K = {e_j}. Symmetrically on M_j it forces K = {e_i}. So the full fill is incoherent, while C_p is coherent. ∎

So audit's §11 "necessary division among defenders" is the disjointness in (c). And T's defence against a dominator in Dom_k is available only at k (b): this is audit's reservation (R).

### 3.2 Compensation is necessary

**Lemma 5.0 (single-world kill; PROVED; bookkeeping CHECKED).** Fix a world w. Suppose C ⪯_w X, where:
- X = T off a set E;
- X ≤_w C pointwise on E, strictly on a non-null part.

Let Y := T[D_Y → y] satisfy:
- D_Y ∩ E = ∅;
- {C <_w T} \ E ⊆ D_Y;
- y ≤_w C pointwise on D_Y.

Then T ⋠_w Y.

*Proof.* Let D := {C ≠ X}, A₀ := T[D → C] and B₀ := T[D → X]; this is a copy of rec(C, X).
- Off E, X = T. So B₀ = T on D_Y, and Z₀ := B₀[D_Y → y] makes (B₀, Z₀) a copy of rec(T, Y).
- **Comparing Z₀ with A₀:**
  - on D_Y, Z₀ = y ≤_w C = A₀ (where C = T, A₀ = T = C);
  - on D ∩ E, Z₀ = X ≤_w C;
  - on D \ (E ∪ D_Y), Z₀ = T, and T ≤_w C because the points with C <_w T outside E lie in D_Y;
  - off D ∪ D_Y the two agree.
- Strictness comes from E.

So Z₀ ≺_w A₀, and T ⪯_w Y would give A₀ ⪯_w B₀ ⪯_w Z₀ ≺_w A₀. ∎

**Theorem 5 (compensation is necessary; PROVED; table CHECKED).** Under (H), let C ⪯_i X_{E_i} and C ⪯_j X_{E_j}, where these are majority fills on M_k (E_i and E_j may differ) and C ≠ A on a non-null part of each. Then the **compensation set**

  P := [({C <_i T} \ E_i) ∪ ({C <_j T} \ E_j)] \ [{C <_k T} \ (E_i ∪ E_j)]

is non-null. Off E_i ∪ E_j, class by class, P consists of:
- points of M_k where C is strictly more A-ward than T (for example C = A where T is silent);
- points of M_i or M_j where C is strictly more B-ward than T (C better than T at that class's minority world);
- never points of U.

*Proof.* Suppose P is null. Put D_Y := {C <_k T} \ (E_i ∪ E_j) and Y := T[D_Y → C].
- Lemma 5.0 with y = C applies at i and at j, so T ⋠_i Y and T ⋠_j Y.
- If D_Y is non-null, then Y ≺_k T by strict (G). So T ⋠_k Y, and T is not competitive against Y.
- If D_Y is null, then T ≤_i C off E_i, so X_{E_i} ≤_i C everywhere, strictly on E_i ∩ {C ≠ A}. Then X_{E_i} ≺_i C, contradicting C ⪯_i X_{E_i}.
- The class description is a rank computation (`pointwise.py` check 1). ∎

**Corollaries (PROVED).**
- **5.1. B_i and R_i are forced.** Every dominator of the majority fills on A ⊆ M_k needs a non-null region outside A of the kind audit's B_i and R_i are. These sets are not artifacts of the construction.
- **5.2. The full fill.** The dominator of X^k := T[M_k ∩ {T ≠ A} → A] has no room on M_k, since T = A there off the fill. It must be strictly more B-ward than T somewhere on M_i ∪ M_j.
- **5.3. Strictly stronger than §1.** Let E_B be the part of E where T says B, and C := T[E_B → S]. Lemma 0.2 allows this C: T ⪯_k C holds by guidance, since C is worse than T at k only inside E. Theorem 5 excludes C as a dominator of X_E, because it has no compensation. The conclusion of PP16's Theorem B, that the dominator of a one-class majority fill cannot be pointwise no worse than T at the minority world, already follows from Lemma 0.2 and strict (G) for every ranking satisfying (H). Theorem 5 strengthens it.

### 3.3 Two classes together

**Theorem 6 (two-source kill; PROVED; bookkeeping and feasibility CHECKED).** Under (H), on M_3 with worlds 1 and 2 the majority worlds, suppose:
- C ⪯_1 X_E and C ⪯_2 X_E (exposed: C ≠ A on a non-null part of E);
- C′ ⪯_3 Z_F (exposed: C′ ≠ B on a non-null part of F);
- E ∩ F = ∅.

Let K := ({C <_1 T} ∪ {C <_2 T}) \ E ∪ ({C′ <_3 T} \ F). Then at least one of the following holds:
- (a) K meets E ∪ F in a non-null set;
- (b) on a non-null part of K ∩ M_3, C is strictly more A-ward than C′;
- (c) on a non-null part of K ∩ (M_1 ∪ M_2), C is strictly more B-ward than C′.

(Points where C or C′ says X never obstruct.)

*Proof.* Suppose none holds. Pointwise on K there is advice y with y ≤_1 C, y ≤_2 C and y ≤_3 C′ (`pointwise.py` check 2). The cases:
- on M_3, y lies between C and C′ in A-ward order, which needs C′ at least as A-ward as C;
- on M_1 and M_2, y = C, which needs C at least as A-ward as C′;
- on U, y = A.

Put Y := T[K → y], with D_Y = K. Lemma 5.0 applies to C at worlds 1 and 2, and to C′ at world 3 with the minority fill, where B is best at 3. So T has no defence against Y. ∎

**Reading.** A majority-fill dominator C and a minority-fill dominator C′ may not agree on C's compensation. On C's M_3 compensation, where C is A-ward of T, C′ must be strictly less A-ward than C somewhere, unless K meets the fill sets. Audit's six sources satisfy this, because other groups are silent on each R_i. Lemma D allows only countably many private witness groups (the referee's repair). So uncountable dominator families must share compensation, and Theorem 6 says that sharing across the majority/minority divide is constrained, while sharing **within** a class is not.

### 3.4 The discontinuity

**Theorem 7 (PROVED).**
- **(a) The discontinuity is forced.** Every all-world weak dominator C of X ∈ 𝒳_k has a world w with C ⪯_w X and C ⋠_w T. If C ≺_i T and C ≺_j T (audit's pattern), then w = k: C ⪯_k X and C ⋠_k T. If instead C ⪯_k T (a tie at k), then w ∈ {i, j}.
- **(b) Moving sources, two regimes.** Let μ(E_n) → 0 and q_n ∈ Dom(X_{E_n}), with q_n → q_0. Either:
  - (i) q_0 ∈ Φ_T. Then for every fixed m, C_{q_n} ⋠_i X_{E_m} and C_{q_n} ⋠_j X_{E_m} for all large n, although C_{q_n} ⪯_i X_{E_n}. If the E_n decrease, X_{E_m} is a strict pointwise i-improvement of X_{E_n}, so acceptance at i is not monotone in the rival. Or:
  - (ii) q_0 ∉ Φ_T. Then C_{q_0} ⋠_w T for some w, by Lemma A.

*Proof.*
- (a) If C ⪯_w T at every w, then since T ⋠_i C (Theorem 4(b)), C ≺_i T and C dominates T. The two special cases follow because C ⪯_w X holds at every w.
- (b) (i) is Theorem 1 applied to the fixed rivals X_{E_m}. (ii) is Φ_T = ⋂_w A_w(T). ∎

**Remark 7.1 (why sections cannot see it).** (S) is a separate closedness condition for each fixed rival. Neither regime puts a limit point outside a section that must contain it:
- in (i), the q_n leave each fixed A_i(X_{E_m}) and the limit lies in A_k(X_{E_m});
- in (ii), nothing about X_{E_n} is inherited at q_0.

A contradiction would need an (IB) identity between rec(C_{q_n}, X_{E_n}) and a record with a fixed rival. Lemma 8 shows that such identities arise only when sources agree on whole disagreement sets. So the answer to audit's question is **compatible**, with the forced form above. This is an explanation, not a consistency proof.

---

## 4. Q3: (IB) copies between nearby sources

**Lemma 8 (copy calculus; PROVED, immediate from (IB)).** Write D_C := {C ≠ T}.
- **(a) Disjoint supports.** If D_C ∩ D_{C′} = ∅ and H := C′[D_C → C], then:
  - C ⪯_w T ⟺ H ⪯_w C′;
  - T ⪯_w C ⟺ C′ ⪯_w H;
  - for a rival T[E → x] with E ∩ D_{C′} = ∅: C ⪯_w T[E → x] ⟺ H ⪯_w C′[E → x].

  Consequently H dominates C′ iff C dominates T, and C′ (if interior) is competitive against H because T is competitive against C. Disjoint supports therefore reproduce only the existing relations between T and the sources.
- **(b) Nested supports.** If C′ = C on D_C ∪ E, then C ⪯_w T[E → x] ⟺ C′ ⪯_w C′[D_C → T, E → x]. Again nothing new: this is a copy of C's own record.
- **(c) Shared regions.** If C = C′ on P, then rec(C, C′) = rec(C[P → T], C′[P → T]). Comparisons between sources are blind to a shared compensation region.
- **(d) Crossing supports.** If C ≠ C′ on a non-null part of D_C ∩ D_{C′}, no copy of rec(C, ·) starts or ends at C′ through that part. Only here can new constraints arise.

**Proposition 9 (partial-source rivals; PROVED; identity CHECKED).** Let C be selected at q. Let D′ ⊆ D_C be non-null, X := T[D′ → C] and C° := C[D′ → T]. Then rec(T, X) = rec(C°, C) and rec(X, T) = rec(C, C°), and:
- (a) If T ⪯_w X at all three worlds, then X ≈ T and C° ≈ C, both distinct ties. Under direct (C), X and C° are then coherent and undominated. In the no-tie regime, W_T(X) is therefore a nonempty **proper** subset of the worlds. In particular X is never a pointwise weak worsening of T at all three worlds.
- (b) X ⪯_w T for some w ∈ supp q, because C is competitive against C°.

*Proof.* The identities hold because both records are (D′, T|_{D′} → C|_{D′}); see `pointwise.py` check 5.
- (a) The hypothesis gives C° ⪯_w C at all w. Since C is undominated, nothing is strict, so C ⪯_w C° at all w, which is the copy of X ⪯_w T. So X ≈ T.
- (b) Competitiveness of C against C° gives C ⪯_w C° for some w ∈ supp q, which is a copy of X ⪯_w T. ∎

**What this explains.** The referee's failed fix installed T ⪯_w X at every world where X worsens T somewhere. For X = T[A_1 ∪ B_1 → C_1], that is all three worlds, and C_1 becomes dominated. Proposition 9 shows that this is a theorem about every (S)-system without ties, not a feature of audit's module: target-reference rules must refuse each partial-source rival at one or more worlds. The referee's one-world rule is consistent with Proposition 9. Lemma 0.4 is the same mechanism for source-to-rival records: no undominated model may agree with a dominated rival on the dominator's disagreement set. This is what audit's W_ij enforce.

**Proposition 10 (the source layer has a consistent local skeleton; PROVED).** Take indices q_n → p* and selected models C_n, and let the relations among {T} ∪ {C_n} be:
- worlds 1 and 2: C_1 ≺ C_2 ≺ ⋯ ≺ T (C_m ⪯ C_n iff m ≤ n; C_n ⪯ T);
- world 3: T ≺ ⋯ ≺ C_2 ≺ C_1 (C_n ⪯_3 C_m iff n ≥ m; T ⪯_3 everything).

These relations satisfy:
- (TC), because each world is a strict linear order;
- strictness and mutual undominatedness, since every pair is split across worlds;
- competitiveness within the family;
- closed sections along {q_n} ∪ {p*} for every rival in the family. For example, A_1(C_m) ∩ {q_n} = {q_n : n ≤ m} and A_3(C_m) ∩ ({q_n} ∪ {p*}) = {q_n : n ≥ m} ∪ {p*}.

They also satisfy Theorem 1, Theorem 4(b) and case (i) of Proposition 3.

*Proof.* Each item is a direct check against the definitions. ∎

**Verdict on Q3.** No necessary obstruction to a continuum of reciprocal sources follows from the tools here, and none was found. The pieces of a possible obstruction are now isolated:
- copies through disjoint, nested or shared supports are inert (Lemma 8);
- the relations among T and the sources are consistent (Prop 10);
- partial-source copies give a refusal condition, not a contradiction (Prop 9).

An obstruction would therefore need rivals whose records **cross** source supports (Lemma 8(d)), used through single-world kills (Lemma 5.0). That is where to look. Theorems 5 and 6 are the first two instances. Status: OPEN.

---

## 5. Q4: the tie escape

Suppose T is undominated but not selected. By KKM, Φ_T ≠ ∅, so some selected C ≈ T, and by Lemma 0.3 every such C sits at an interior index.

**Proposition 11 (what transfers; PROVED).**
- **(a) Unchanged.** Theorem 1, Corollary 1.1, Proposition 2 and Proposition 3 hold verbatim. Their proofs use only T ⪯_w C_p for p ∈ Φ_T.
- **(b) Not for T.** Lemma 0.2 still holds for N = T, but T need not defend itself. So Theorem 4(b), Lemma 5.0 and Theorems 5–7 do **not** constrain T's defences.
- **(c) For the tie partner.** They do constrain the tie partner C, which is selected at an interior index, with C's own fills X^C_E := C[E → A]. For E ∩ {C ≠ T} = ∅, X^C_E ≈ X_E (a copy of the tie record).
- **(d) Tie-partner refusals.** C ⋠_w Y for every Y ≺_w T, and T ⋠_w Y for every Y ≺_w C, at every w.
- **(e) Direct-(C) transport.** Let D := {C ≠ T}. Every coherent undominated S with S = T a.e. on D has S[D → C] ≈ S, so S[D → C] is coherent and undominated. The same holds with C and T exchanged.
- **(f) T's undominatedness is threatened only through D.** If Y dominates T, then {Y ≠ T} meets D in a non-null set.

*Proof.*
- (a) Inspect the proofs.
- (c) The copy of rec(C, T) in context X_E is (X^C_E, X_E).
- (d) Use T ⪯_w C ⪯_w Y, and the reverse chain.
- (e) The copy of the tie record in context S is (S[D → C], S).
- (f) Otherwise, copying rec(Y, T) in context C makes C[{Y ≠ T} → Y] dominate C. ∎

**Verdict on Q4.** The escape is genuinely open, and this note does not close it.
- All the near-fibre structure transfers.
- Every obstruction found so far against selecting T works by killing **T's defences**: audit's §1, PP16 Theorems B and O, and Theorems 5–6 here. Those defences are not required of an unselected T.
- Route (b) of DESIGN_MEMO §8.12 is therefore equivalent to selecting a coherent C ≈ T at an interior index. All of §§2–4 then apply to C and its own geometry, and T must additionally satisfy (e) and (f).

Closing the route would need an argument that two distinct coherent models cannot be tied at all worlds in an (S)-system. Nothing here excludes it: per world, a tie only requires each model to be strictly better on some non-null set, which coherent models with crossing credal sets can be.

For lead's Theorem C(iii), the referee's §7.3 shows that closedness data cannot settle it. One more necessary condition (PROVED): some tie component K is infinite and U_K is not closed. So there are p_n ∈ Φ_{M_n}, with distinct M_n ∈ K, converging to p_0, where N := C_{p_0} ∉ K. Applying Theorem 1 with N in place of T, each fixed X with X ≺_w N is accepted at w by only finitely many C_{p_n}. This constrains (iii) without closing it.

---

## 6. Implications for the design of the selection

1. **Three source classes are forced, and their shape with them** (Theorems 4–5).
   - Dominators of two-world improvements fall into three disjoint classes.
   - T defends against each only at its minority world k (possibly by a tie).
   - Each class refuses at k every strict improvement of T there, and stays off the opposite closed edge (absent ties).
   - Each dominator carries a compensation set outside the fill it dominates.

   Audit's architecture, with C_i/F_i and B_i/R_i, is therefore necessary in outline, not an arbitrary choice. Design effort should go into how compensation is **shared**, since private witnesses are countable. Sharing within a class is free; sharing across the majority/minority divide must respect Theorem 6.
2. **Around Φ_T, build a T-mimic collar for each rival** (Theorem 1). Selected models near Φ_T must use T's own worlds against every fixed strict improvement of T.
   - The simplest compatible design keeps the dominators of small fills at positive distance from Φ_T, as fixed sources serving all small E, like audit's C. The discontinuity of Theorem 7(a) is then harmless for sections.
   - Letting dominators creep toward Φ_T is allowed only with escaping, non-monotone acceptance (Theorem 7(b)(i)), and their pairwise relations must follow Proposition 3: a strict chain at a majority world, or world-k ties.
3. **Target-reference rules must be one-world-ish on partial sources** (Proposition 9). For every selected C, each partial source T[D′ → C] must be refused by T at one or more worlds. This matches the referee's finding that the all-worlds rule fails and the one-world rule passes the cell checks. Proving that one-world extension, as the referee recommends, is consistent with everything here. Near Φ_T, X*-type rivals must then be defended at worlds 1 or 2 (Corollary 1.1).
4. **Where an obstruction could still come from** (Lemma 8, Proposition 10). Rivals whose records cross the supports of two selected sources, entering through single-world kills (Lemma 5.0). Any construction of the collar and the transition models should be checked first against Lemma 5.0 at each world where it installs a defence of T or of a collar model.
5. **Tie route** (Proposition 11). It is a re-targeting: select a coherent C ≈ T and verify (e) and (f). It is worth pursuing only if C's geometry avoids the T1-specific kills.

---

## 7. Script

`PP19_py/pointwise.py`, with output in `pointwise.out`. All checks are exact and exhaustive. They check proof bookkeeping only, not (S).

| Check | Content | Count |
|---|---|---|
| 1 | Compensation classification (Theorem 5) | 48 cases |
| 2 | Pointwise feasibility of y (Theorem 6) | 64 cases |
| 3 | Lemma 5.0 / Theorem 5 triangles on 4 cells: both copies are genuine (IB) copies, the closing link is a strict pointwise improvement at worlds 1 and 2, and Y is a strict world-3 improvement | 1,127,520 configurations |
| 4 | Theorem 6 triangles on 3 cells, at all three worlds | 444,528 configurations |
| 5 | Partial-source record identities (Proposition 9) | 173,745 cases |
