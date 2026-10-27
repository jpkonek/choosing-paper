# GG3 (round 35, BRIEF27). The representation theorem for NA-credal worlds, the classification of the known constructions, the dichotomy for covers of T1, and a referee report on FF1 Thm 5.2 / Prop 8.1 and FF2 Thm 4.1 / Cor 4.3

18 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact computation or line-by-line reading of a stated source.
- **NUMERICS**, **CONJECTURE** as usual.

No script was needed; there is no `gg3py/` folder. No assumption is added: every extra hypothesis is a hypothesis of a
stated result.

---

## 0. Outcome

**Part A.**

1. **Representation theorem (Theorem 2.1; PROVED).** Let ≼ be a relation on the evaluable models of a decomposable
   domain, with strict (G). The following are equivalent:
   - (i) ≼ is NA-credal: an intersection of strictly guiding record-additive rankings valued in ordered abelian groups;
   - (ii) every finite set of accepted comparisons, together with any single non-comparison X ⋠ Y, is separated by a
     bounded strictly guiding cell witness (on an arbitrary finite measurable partition);
   - (iii) a finite cancellation condition in records: whenever N·φ_{rec(X,Y)} − Σ_k φ_{rec(A_k,B_k)} is a pointwise
     worsening flow, with A_k ≼ B_k accepted and N ≥ 1, then X ≼ Y;
   - (iii′) equivalently, the accepted records are exactly the records that lie in a convex cone (not necessarily
     closed) that contains every worsening flow and no nonzero improving flow.

   Each of (ii), (iii) already implies (IB) and transitivity, cancelled-change composites included. So the standing
   hypothesis (IB) is not needed.
2. **Value groups (Theorem 3.1, Proposition 3.2; PROVED).**
   - One fixed ultrapower *ℝ = ℝ^I/U suffices for every NA-credal world on every decomposable domain. Here I is the
     set of finite sets of pairs of models and U is any ultrafilter containing the cones {F ⊇ F₀}. Every member can
     be taken to be an ultraproduct of countably additive cell witnesses. By Hahn embedding, a Hahn group ℝ((Γ))
     with Γ the archimedean classes of *ℝ also suffices.
   - Nothing essentially smaller suffices. There is an NA-credal world (the "left-germ world", §3) every respecting L
     of which has a chain of archimedean classes order-isomorphic to the reversed interval (0,1). So ℝ, ℝ^n
     lexicographic for every n, countably many levels, and any well-ordered family of levels all fail.
3. **(ii) is not "(M2) + separability".** Separability of non-comparisons alone is (ii), and it already excludes
   every finite obstruction among *all* accepted comparisons (Prop 4.1). So NA-credal ⊆ ¬(M1), and NA-credal worlds
   can be (M0) or (M2). The converse fails: the (M2) worlds of D2, D2′, H2.4, L2, P1 and T2n.1 are not NA-credal.
   The brief's sentence "real-valued L gives intersections of additive rankings (already excluded)" holds only for
   integral L. Real-valued finitely additive members are a larger class; Prop 6.3 excludes them, for continuous
   selections, through FF2.
4. **Classification (§5; PROVED unless marked).** The table is in §5.0.
   - **NA-credal:** C2.1 (both worlds; real, integral members); VB and VB′ (each world one ℝ²-lex L); FF2's
     end-priority P (one ℝ²-lex L per world); every additive world.
   - **Not NA-credal, of type β** (a non-comparison forced by cancellation):
     - world 1 of L2, P1 and both worlds of T2n.1, for all parameters;
     - world 1 of D2, and both worlds of H2.4, for designs with h₀ + sup_γ μ(P_γ) < a, which includes D2.2's design
       whenever h₀ < a/2;
     - world 1 of D2′_H, when μ(W) < μ(S)/2; such parameters exist on both hosts.

     In each case the certificate is the system's own level-averaging certificate, read as a cancellation.
   - **Not NA-credal, of type α** (a finite improving combination): any world containing CC1's seed or the audit's
     synchronized seeds.
   - **D2's NA-credal hull exists but has a non-closed section** (Prop 5.4). D2 refuses cancellation exactly where
     closed sections need it.
5. **Dichotomy for covers of T1 (Theorem 6.1; PROVED).** Every cover of T1, on every decomposable domain, falls under
   exactly one of the following:
   - (A) all three worlds are NA-credal, with all members in one *ℝ;
   - (B) some world i has a finite non-separable configuration: accepted comparisons A_k ≼_i B_k, integers N, n_k ≥ 1
     and a pair X ⋠_i Y, with N·φ_{rec(X,Y)} − Σ n_k φ_{rec(A_k,B_k)} a pointwise worsening flow at world i.

   (B) splits into (B-α), a nonzero improving combination of accepted records (on M_U and relevant comparisons this is
   exactly (M1)), and (B-β), the rest. In case (B-β), passing to NA-credal hulls preserves every axiom except possibly
   closed sections, undominatedness and (C) (Prop 6.2). In case (A) with a selection continuous in measure through
   T1, some world has no real-valued member at all, even a finitely additive one (Prop 6.3; status of FF2's chain).

**Part B (referee).**

6. **FF1 Theorem 5.2: CORRECT.** Steps 1–8 check, including steps 2, 4, 5 and 7, in both tiers. Only presentation
   points need adding: bets at a level value lie on cell boundaries, so use nearby non-null cells; cells are common to
   the three worlds. FF3's "(C) open" and FF3 Remark 5.3 (CONJECTURE "additive functionals do not decide (C)") are
   superseded: non-homogeneous cell witnesses adapted to S decide it.
7. **FF1 Proposition 8.1: CORRECT.** By Theorem 2.1 its hypothesis says exactly that the NA-credal hull of Γ_i exists
   and avoids Φ_i (Cor 2.4).
8. **FF2 Theorem 4.1: CORRECT, modulo its import chain.** D1 [R1], BB2 Thm 6.1 [R1 per CC3] and M3.7–M3.8 [R1] all
   apply with hypotheses verified. AUDIT_BB Lemma 2.0 is correct and in fact unnecessary here: Step 3 gives
   coherence at *every* interior weight off E. The closed-graph step is correct.
9. **FF2 Corollary 4.3: CORRECT AS STATED; its readings need a repair.** (H1) includes "T1 is a selected model". The
   readings in FF2 §0.5 and after Cor 4.3, and BRIEF27's "necessary feature (FF2 Cor 4.3)", say "every cover with a
   selection continuous in measure". That does not follow when T1 ∈ C_L is merely tied with a selected model.
   **Repair (Thm 4.1′, PROVED):** replace "T1 = C_{q₀}" by "T1 is competitive on supp q₀", which every cover gives
   by Theorem kkm and transitivity, and add T1's own local comparisons to (H3).

**Single most important open point.** Does closed choice force NA-credal worlds to add up? Precisely: in a ranking
with strict (G), (IB), (LA), (S) (closed sections for every model) and (C), must every NA-credal world add up, or at
least have a real-valued respecting member? CONJECTURE: yes.
- Evidence: the three known NA-credal worlds that do not add up all lose closed sections. These are VB (L3.4), FF2's P
  (FF2 Cor 2.5) and D2's hull (Prop 5.4).
- Consequence of yes: by Theorem 6.1 with Q4.2 / M0closed, T1 has no all-NA-credal cover, and every cover has a world
  with a finite cancellation failure. That is the "No" answer to BRIEF27's decisive question.
- Consequence of no: a counterexample in two worlds is the natural next construction. Start from D2's hull and close
  its sections.

---

## 1. Setting

**Domain.** 𝓜 is a decomposable domain with advice range A(h) (write-up Remark advicerange). The full four-advice
domain has A ≡ {+, 0, −, ×}; on M_U, A(h) = {+, 0} for orientations h ∈ U. For a world i and a.e. h, write ⪯ᵢʰ for the
world-i rank order on A(h) (good ≺ silent ≺ bad ≺ contradictory, restricted to A(h)). Coordinate planes are null.

**Records** (AUDIT_nonlinear_programme). For models X, Y, rec(X,Y)(h) is ι where the advice agrees and the ordered pair
(a_X(h), a_Y(h)) elsewhere, modulo null sets. Records compose pointwise where their arrows match. Opposite arrows give
ι (cancelled change), and ι is then realised with any common advice. A relation is record-dependent iff it satisfies
(IB).

**Flows.** For a record d put φ_d(h, ·) := δ_b − δ_a ∈ ℝ^{A(h)} where d(h) = (a, b), and 0 where d(h) = ι. Then:
- φ_{d∘e} = φ_d + φ_e pointwise for every realisable composite, cancelled ones included;
- d is determined by φ_d up to null sets.

A **flow** is a measurable f(h, a), a ∈ A(h), bounded, with Σ_a f(h,a) = 0. It is a **worsening flow (at world i)**
if, for a.e. h and every a′ ∈ A(h),

  Σ_{a ⪯ᵢʰ a′} f(h, a) ≤ 0   (cumulative mass on the advices at least as good as a′).

Equivalently, f(h,·) is a nonnegative combination of elementary moves δ_b − δ_a with b worse than a. (On a chain
a₀ ≺ … ≺ a_r with partial sums F_k ≤ 0 and F_r = 0, f = Σ_{k<r}(−F_k)(δ_{a_{k+1}} − δ_{a_k}).) An **improving flow**
is the negative of a worsening flow. A record d is a guidance worsening iff φ_d is a worsening flow. On M_U, with
δ_d := 1_{E_iY} − 1_{E_iX}, "φ_e − Σ z_k φ_{d_k} is worsening" reads δ_e − Σ z_k δ_{d_k} ≥ 0 a.e.

**Record-additive rankings.** Let G be an ordered abelian group. A map L from evaluable models to G is
**record-additive** if L(Y) − L(X) depends only on rec(X, Y); write λ(rec(X,Y)) := L(Y) − L(X). Realising composites
through middle models gives λ(d∘e) = λ(d) + λ(e) for every realisable composite, cancelled ones included.

Splitting a record into its arrow pieces gives, for each arrow type (a,b), a G-valued finitely additive set function
m_{ab}(F) := λ(arrow a→b on F, ι elsewhere). It vanishes on null sets, and m_{ab} + m_{bc} = m_{ac}. Then

  λ(d) = Σ_{(a,b)} m_{ab}({d = (a,b)}).

L is **strictly guiding** if λ(d) > 0 for every nontrivial guidance worsening d. Equivalently, m_{ab}(F) > 0 for every
non-null F on which b is worse than a.

For a Hahn-group or lexicographic value this means "the leading nonzero layer is positive". It does not mean
"positive at some layer", which the brief's gloss might suggest. Each ≤_L is a total preorder with strict (G), (IB) and
transitivity.

**NA-credal.** ≼ is NA-credal if ≼ = ⋂_{L∈Π} ≤_L for a nonempty family Π of strictly guiding record-additive maps,
each valued in some ordered abelian group.

**Cell witnesses.** Let 𝒞 be a finite partition of H into non-null measurable sets, each contained in one sign class of
h_i and one class of the advice-range map. A cell witness is ψ(h, a) := x_c(a)/μ(c) for h ∈ c, with x_c(·) strictly
increasing in world-i rank on A(c), and L_ψ(X) := ∫ψ(h, a_X(h)) dμ. It is a bounded, countably additive, strictly
guiding, record-additive ranking defined on every model (FF1 Lemma 3.1, with measurable instead of open cells).

A finite configuration of models always generates such a partition: the joint advice pattern of the models, refined by
sign h_i and A(h). "Measure-theoretic" models therefore cause no difficulty. Cells are arbitrary measurable sets, and
only finiteness matters.

---

## 2. The representation theorem

**Lemma 2.0 (transfer of finite systems; PROVED).** Let a finite homogeneous system of strict, weak and equality
linear constraints with integer coefficients have a solution with entries in an ordered abelian group G. Then it has
a real solution.

*Proof.*
1. Suppose there is no real solution. By Motzkin's transposition theorem there is a certificate with rational
   coefficients (the data are rational): y ≥ 0 on the strict rows, not all zero; z ≥ 0 on the weak rows; free
   coefficients on the equalities; with Σ y_j u_j + Σ z_k v_k + Σ e_l w_l = 0.
2. Clear denominators, so that all coefficients are integers.
3. Evaluate at the G-solution x. In an ordered group n·g > 0 for g > 0 and n ≥ 1. So the left side is > 0 in G,
   while it equals 0. ∎

**Theorem 2.1 (PROVED).** Let ≼ be a relation on the evaluable models of a decomposable domain 𝓜, and let world i
have strict (G): X ≼ Y and Y ⋠ X whenever rec(X,Y) is a nontrivial guidance worsening. The following are equivalent.
- **(i)** ≼ is NA-credal.
- **(i*)** ≼ = ⋂_{L∈Π} ≤_L with every L valued in the single ultrapower *ℝ of Theorem 3.1, and each L an ultraproduct
  of cell witnesses.
- **(ii)** For every finite set 𝒢 of accepted comparisons and every pair X ⋠ Y there is a cell witness L with
  L(A) ≤ L(B) for all (A ≼ B) ∈ 𝒢 and L(X) > L(Y).
- **(iii)** For all accepted A_k ≼ B_k (k ≤ m), all integers N, n_k ≥ 1, and all X, Y:
  if N·φ_{rec(X,Y)} − Σ_k n_k φ_{rec(A_k,B_k)} is a worsening flow, then X ≼ Y.
- **(iii′)** There is a convex cone 𝒦 of flows with 𝒦 ⊇ {worsening flows} and 𝒦 ∩ {improving flows} = {0}, such that
  X ≼ Y iff φ_{rec(X,Y)} ∈ 𝒦.

Each of (ii) and (iii) implies that ≼ is reflexive, transitive and record-dependent ((IB), cancelled-change composites
included). In (ii), "cell witness" may be replaced by any intermediate class, without changing the condition:
- bounded integral strictly guiding additive rankings;
- real finitely additive strictly guiding record-additive rankings;
- G-valued ones.

*Proof.*

**(i) ⇒ (ii).**
1. Let 𝒢 and X ⋠ Y be given. Pick L ∈ Π with L(X) > L(Y); it respects 𝒢.
2. Let 𝒞 be the partition generated by the models of 𝒢 ∪ {X, Y}, refined by sign h_i and A(h).
3. On a cell c, every model of the configuration has constant advice. Put x_c(a) := m_{a₀a}(c) for a fixed a₀ ∈ A(c).
   Then m_{ab}(c) = x_c(b) − x_c(a), and for each model Z of the configuration L(Z) − L(Z₀) = Σ_c
   (x_c(a_Z(c)) − x_c(a_{Z₀}(c))).
4. The G-vector (x_c(a)) solves a finite integer system:
   - strict rows x_c(b) − x_c(a) > 0 for b worse than a on c (strict guidance, c non-null);
   - weak rows for 𝒢;
   - one strict row for (X, Y).
5. By Lemma 2.0 there is a real solution. The cell witness ψ := x_c(a)/μ(c) separates.

**(ii) ⇒ (i*).**
1. Let I be the set of finite subsets of ≼ (as pairs). Let U be an ultrafilter on I containing every cone
   {F : F ⊇ F₀}; the cones have the finite intersection property.
2. Fix X ⋠ Y. For F ∈ I, (ii) gives a cell witness L_F respecting F with L_F(X) > L_F(Y). Put
   L_{XY}(Z) := [(L_F(Z))_F]_U ∈ ℝ^I/U.
3. Record-additivity holds coordinatewise, hence in the ultrapower.
4. Strict guidance: a nontrivial worsening d has λ_F(d) > 0 at every coordinate (cell witnesses are strictly guiding on
   every non-null set), hence λ(d) > 0.
5. Respect: for A ≼ B the set {F : (A,B) ∈ F} is a cone, hence in U, so L_{XY}(A) ≤ L_{XY}(B).
6. Separation: L_{XY}(X) > L_{XY}(Y) at every coordinate.
7. Π := {L_{XY} : X ⋠ Y} is nonempty, because strict (G) gives non-comparisons. ⋂_Π ≤_L = ≼.

**(i*) ⇒ (i)** is trivial.

**(ii) ⇒ (iii).**
1. Suppose the hypothesis of (iii) holds, but X ⋠ Y. Take L from (ii) for 𝒢 = {A_k ≼ B_k} and (X, Y).
2. For any additive L, λ(d) = ∫Σ_a ψ(h,a) φ_d(h,a) dμ.
3. For a worsening flow f and ψ(h,·) strictly increasing in rank, Abel summation gives ∫Σ_a ψ f ≥ 0.
4. Hence N·λ(rec(X,Y)) ≥ Σ n_k λ(rec(A_k,B_k)) ≥ 0, i.e. L(X) ≤ L(Y). This is a contradiction.

**(iii) ⇒ (ii).**
1. Let 𝒢 = {A_k ≼ B_k} and X ⋠ Y. Take 𝒞 generated by all these models, refined as usual, and consider the finite
   system of the proof of (i) ⇒ (ii) over ℝ.
2. If it is infeasible, Motzkin gives rational y_e ≥ 0 (separation row), y_{c,ab} ≥ 0 (guidance rows), not all zero,
   and z_k ≥ 0 with

     y_e v(rec(X,Y)) = Σ z_k v(rec(A_k,B_k)) + Σ y_{c,ab}(e_b − e_a)_c.

3. Every record of the configuration is cell-constant, and φ_d(h, ·) = v_c(d) for h ∈ c. So this is a pointwise
   identity of flows. Its last term is a worsening flow.
4. **Case y_e > 0.** Scale to integers. Then (iii) gives X ≼ Y, a contradiction.
5. **Case y_e = 0.** Some y_{c₀,ab} > 0. Let e₀ be the elementary record with arrow b → a on c₀. It is realisable, and
   it is a nontrivial guidance improvement.
6. Write φ_k := φ_{rec(A_k,B_k)}, w₀ := (e_b − e_a)_{c₀} (so φ_{e₀} = −w₀), and Σ_{(c,w)} y_{c,w} w for the
   worsening term. The identity of step 2 with y_e = 0 reads Σ_k z_k φ_k = −Σ_{(c,w)} y_{c,w} w. Hence

     φ_{e₀} − Σ_k (z_k/y_{c₀,ab}) φ_k = −w₀ + Σ_{(c,w)} (y_{c,w}/y_{c₀,ab}) w = Σ_{(c,w)≠(c₀,w₀)} (y_{c,w}/y_{c₀,ab}) w,

   which is a worsening flow. Scale the rational coefficients to integers.
7. So (iii) accepts the improvement e₀, against strict (G). Hence the system is feasible, and its real solution is the
   required cell witness.

*Real coefficients.* The proof of (ii) ⇒ (iii) never uses integrality. So under (ii), and hence under (iii), the
implication of (iii) also holds with real coefficients z_k ≥ 0 in place of n_k/N.

**(iii) ⇔ (iii′).**
- Given (iii), let 𝒦 := cone{φ_d : d accepted} + {worsening flows}. By the real-coefficient form of (iii), the
  accepted records are exactly the records with φ in 𝒦.
- If 𝒦 contained a nonzero improving flow, step 6 above would produce an accepted elementary improvement, against strict
  (G).
- Conversely, (iii′) implies (iii) at once, and strict (G) follows from 𝒦 ∩ improving = {0}.

**Consequences of (ii) and (iii).**
- Reflexivity: (ii) with X ⋠ X would need L(X) > L(X).
- Transitivity and record dependence: by (iii), since φ_{d∘e} = φ_d + φ_e and equal records have equal φ. The same
  holds for (IB)-transports of composites with cancelled changes. ∎

**Remarks.**
- (a) (iii′) answers AUDIT_nonlinear_programme's distinction exactly. A general world is closed only under admissible
  composition. An NA-credal world is closed under conic (posi) combination, with no topological closure. It is never
  required to be closed under limits.
- (b) The real (archimedean) special case of (i) uses real-valued L. These are bounded, finitely additive charges (see
  Prop 6.3), not necessarily integral. INTERSECTIONS_additive covers only integral members (its own remark).

**Corollary 2.4 (NA-credal hull; PROVED).** Let Γ be a set of world-i comparisons. Let hull(Γ) be the set of pairs
(X, Y) such that N·φ_{rec(X,Y)} − Σ n_k φ_{rec(A_k,B_k)} is a worsening flow for some finitely many (A_k, B_k) ∈ Γ
and integers N, n_k ≥ 1. Then:
- (a) hull(Γ) satisfies (iii). It is the least relation containing Γ that does.
- (b) hull(Γ) is NA-credal iff it contains no nontrivial guidance improvement, iff Γ has no **α-obstruction**: a
  positive integer combination of finitely many φ_{rec(A_k,B_k)} that is a nonzero improving flow.
- (c) In that case hull(Γ) = ⋂{≤_L : L strictly guiding, record-additive, *ℝ-valued, respecting Γ}.
- (d) FF1 Prop 8.1's hypothesis, for (Γ_i, Φ_i), holds iff hull(Γ_i) is NA-credal and contains no pair of Φ_i.

*Proof.*
- (a): hull(Γ) is closed under the operation in (iii), because sums of worsening flows are worsening.
- (b): Theorem 2.1 and the case y_e = 0 of its proof.
- (c): every respecting L respects every cancellation consequence (proof of (ii) ⇒ (iii)). Conversely, apply (ii) ⇒ (i*)
  to hull(Γ).
- (d): FF1's hypothesis is (ii) for Γ_i with the non-comparisons restricted to Φ_i. By Lemma 2.0 and the ultrapower,
  it is equivalent to the existence of *ℝ-valued strictly guiding L respecting Γ_i: one for every finite subset, and
  one separating each pair of Φ_i. ∎

---

## 3. Which value groups suffice

**Theorem 3.1 (PROVED).** Fix a decomposable domain 𝓜. Let I be the set of finite subsets of 𝓜 × 𝓜 and U an
ultrafilter on I containing all cones. Then every NA-credal world on 𝓜 (at any world i) is an intersection of
*ℝ := ℝ^I/U-valued strictly guiding record-additive rankings, each an ultraproduct of cell witnesses. The same *ℝ
serves for every world and every NA-credal ranking on 𝓜. Composing with an order embedding of *ℝ into a Hahn group
ℝ((Γ)) (Hahn), with Γ the archimedean classes of *ℝ, gives Hahn-series-valued members.

*Proof.* Theorem 2.1 (i) ⇒ (ii) ⇒ (i*). The index set of the proof of (ii) ⇒ (i*) can be taken to be I itself, by
restricting each F to pairs in ≼. Order embeddings preserve record-additivity, strict guidance and ≤. ∎

**The left-germ world.** Work on the full domain at world i, with rank r(h, a) ∈ {0,1,2,3} (an injective rank, so
ρ_d := r(h,b) − r(h,a) ≠ 0 on supp d). Let τ(h) := Φ(h₁), where Φ is the standard normal distribution function, so
that τ is uniform on (0,1). For a record d put

  F_d(t) := ∫_{τ<t} ρ_d dμ,  t*(d) := ess inf of τ on supp d.

**Accept** d iff d = ι, or F_d(t) > 0 for all t in some interval (t*(d), t*(d) + δ).

**Proposition 3.2 (PROVED).**
- (a) The left-germ world is a preorder with strict (G) and (IB), and it is NA-credal.
- (b) Let L be any strictly guiding record-additive map, into any ordered abelian group, that respects it. Then the
  archimedean classes of ℓ_t := λ(w_{{τ>t}}), t ∈ (0,1), are pairwise distinct and strictly decreasing in t. Here w_S
  is the record "good→silent where h_i > 0, silent→bad where h_i < 0" on S.

  Hence no ordered abelian group whose chain of archimedean classes contains no copy of the reversed interval (0,1)
  can carry any member. This excludes ℝ, ℝ^n lexicographic for every n, countably many levels, and well-ordered
  families of levels.

*Proof.*

(a)
1. **Record dependence and reflexivity** are clear.
2. **Strict (G).** A worsening d ≠ ι has ρ_d > 0 on supp d, so F_d > 0 just right of t*(d). An improving one has
   F_d ≤ 0 throughout.
3. **(iii) of Theorem 2.1.** Let d_k be accepted, n_k, N ≥ 1, and let N φ_e − Σ n_k φ_{d_k} be worsening. Taking mean
   ranks gives Nρ_e ≥ Σ n_k ρ_{d_k} a.e.
   - If every n_k d_k is trivial, e is a worsening, and it is accepted by step 2.
   - Otherwise let t₀ := min t*(d_k) over the nontrivial d_k. Then G := Σ n_k F_{d_k} vanishes on (0, t₀] and is
     > 0 on (t₀, t₀+δ). Also N F_e ≥ G, and ρ_e ≥ 0 on {τ < t₀}.
   - If supp e meets {τ < t₀} non-nully, then F_e > 0 on (t*(e), t₀] and NF_e ≥ G > 0 just after t₀.
   - If it does not, then t*(e) ≥ t₀ and N F_e ≥ G > 0 on (t₀, t₀ + δ), which forces t*(e) = t₀.
   - Either way e is accepted.
4. Theorem 2.1 gives NA-credality. Transitivity is the case of a single composite.

(b)
1. For A ⊆ {τ < c} non-null and disjoint B_1, …, B_m ⊆ {τ > c}, the record d = w_A ∘ w_{B_1}^{-1} ∘ … has
   ρ_d = 1_A − Σ 1_{B_j} and F_d(t) = μ(A ∩ {τ < t}) > 0 on (t*(d), c]. So d is accepted, and
   λ(w_A) ≥ Σ_j λ(w_{B_j}).
2. For s < t, split {s < τ < t} into m non-null pieces A_j. Then λ(w_{{s<τ<t}}) = Σ_j λ(w_{A_j}) ≥ m ℓ_t for every m.
   Also ℓ_t > 0 by strict guidance.
3. So ℓ_t is infinitesimal relative to λ(w_{{s<τ<t}}) ≤ ℓ_s. ∎

So the ultrapower of Theorem 3.1 is not an artefact. NA-credal worlds can need a dense continuum of infinitesimal
scales. VB and FF2's P need only ℝ² lexicographic.

---

## 4. Relation to the write-up's (M0)/(M1)/(M2)

**Proposition 4.1 (PROVED).** Work on M_U, for a world of a ranking with every axiom except possibly a cover.
- (a) If the world is NA-credal, it has no finite obstruction among *all* its accepted comparisons. In particular it
  is not (M1). So it is (M0) or (M2).
- (b) "(M2) + separability of non-comparisons" is the same as separability of non-comparisons, i.e. (ii). The (M2)
  part is implied, and it is not sufficient. The (M2) worlds of D2, D2′, H2.4, L2, P1 and T2n.1 (§5) are not
  NA-credal.
- (c) Not-(M1) relative to relevant comparisons is equivalent to the following: every finite family of relevant
  comparisons is weakly respected by a strictly positive cell weight (Stiemke form of Motzkin). This is (ii)
  restricted to relevant comparisons and without the separation clause.

*Proof.*
- (a) An (M1) certificate is an α-obstruction (Cor 2.4(b)). An NA-credal world has none, since a respecting strictly
  guiding L would give 0 ≤ Σλ < 0.
- (b) Theorem 2.1, and §5.
- (c) Motzkin with one strict block. ∎

---

## 5. Classification of the known constructions

### 5.0 Table

| Construction (source, status) | World | NA-credal? | Reason | Label |
|---|---|---|---|---|
| C2.1 (write-up Thm C21) | 1, 2 | **yes** | unanimity over strictly positive integrable densities: real integral members | PROVED |
| D2 (Thm D21) | 2 | yes | additive | PROVED |
| D2 | 1 | **no** (type β), for designs with h₀ + sup μ(P_γ) < a; D2.2's design when h₀ < a/2 | Lemma 5.1: forces C_a ≼₁ X_T, T = {x ≥ 1−h₀}, which (R⁰) rejects; no α (Prop 5.3) | PROVED |
| D2′_H (Thm F16) | 1 | **no** (β) when μ(W) < μ(S)/2 (exists on both hosts) | Lemma 5.1 with c = S, T = W | PROVED |
| H2.4 (Thm H24) | 1, 2 | **no** (β) under the D2 condition for (a, h₀, 𝒢) and its mirror for (a′, h₀′, 𝒢′) | as D2, at each world | PROVED |
| L2 (Thm L21) | 1 | **no** (β), all parameters | Lemma 5.1 with level-n certificate, T = S_n | PROVED |
| P1 (Thm P1.10) | 1 | **no** (β), all parameters | Lemma 5.1, c = Σ_n, T = S_n | PROVED |
| T2n.1 | 1, 2 | **no** (β) | P1's argument at world 1; its mirror at world 2 | PROVED |
| L2, P1, D2, D2′ | 2 | yes | additive | PROVED |
| VB, VB′ (L3 Thm L33) | each | **yes** | one ℝ²-lex L = (Φ_i, Ψ_i) (resp. (Φ_i, Ψ̃_i)) | PROVED |
| FF2's end-priority P | each | **yes** | one ℝ²-lex L = (E_i, B_i) | PROVED |
| CC1 seed (CC1 Thm 1.1) | any world containing it | **no** (type α) | Σ_k φ_{g_k} is a nonzero improving flow | PROVED from CC1's CHECKED data |
| AUDIT_CC synchronized seeds | world 1 (bundle relation (B)), or any world containing X_k^A | **no** (α), at every scale | sum of the four records = −4 on one increment of f_∅(A), 0 elsewhere | PROVED (audit Lemma 3 is elementary) |
| FF1 plain posterior selected layer | each | its hull is NA-credal (no α) | FF1 Thm 5.1 + Cor 2.4(b) | PROVED (at FF1's status, confirmed in §7) |

### 5.1 The design principle

**Lemma 5.1 (PROVED).** Work on M_U at world i. Suppose the world accepts δ_γ := 1_{Q_γ} − 1_{P_γ} for γ in a finite
family with weights w_γ > 0, and that, for measurable c and T with c ∩ T = ∅:
- Σ_γ w_γ 1_{P_γ} ≥ 1 on c;
- every Q_γ ⊆ T and is disjoint from c;
- Σ_γ w_γ 1_{Q_γ} ≤ 1 everywhere.

If the world is NA-credal, it accepts 1_T − 1_c. Concretely, C ≼_i X for any C with c ⊆ E_i(C), T ∩ E_i(C) = ∅, and
E_i(X) = (E_i(C) ∖ c) ∪ T.

*Proof.* The Q_γ are disjoint from c, so Σ w_γ δ_γ = Σ w 1_Q − Σ w 1_P. Check 1_T − 1_c ≥ Σ w_γ δ_γ pointwise:
- on c: the right side is −Σ w 1_P ≤ −1;
- on T: the right side is ≤ Σ w 1_Q ≤ 1;
- elsewhere: the right side is −Σ w 1_P ≤ 0.

So 1_T − 1_c − Σ w_γ δ_γ ≥ 0, a worsening flow on M_U. Theorem 2.1(iii), in its real-coefficient form, gives
acceptance. ∎

So every world whose non-additivity comes from a "design certificate" (thin sources, spread targets, finitely many
generators averaged) is NA-credal only if it accepts the **averaged comparison** C ≼ X_T. All the designs of the
project refuse it.

### 5.2 D2, D2′, H2.4

**Proposition 5.2 (PROVED).**
- (a) Let 𝒢 be a design with h₀ + sup_γ μ(P_γ) < a, in the notation of Thm D21. Then world 1 of D2 is not NA-credal.
  For the design of Lemma D2.2 (μ(P_{n,i,l}) = a2^{−n} ≤ a/2), h₀ < a/2 suffices. Designs with this property exist for
  every a.
- (b) World 1 of D2′_H is not NA-credal whenever μ(W) < μ(S)/2. Such parameters exist on both hosts: for given z₀,
  take y₀ close to 1. This only shrinks W and keeps sup_{z<z₀} x < inf_{y≥y₀} x.
- (c) Both worlds of H2.4 fail under the conditions of (a) for (a, h₀, 𝒢) and for (a′, h₀′, 𝒢′).

*Proof.*

(a)
1. By (d4), for ε < 1 there are finitely many γ with Σ w 1_P = 1_{c_a} and Σ w 1_Q ≤ ε. By (d1), Q_γ ⊆ T := {x ≥ 1−h₀},
   and T ∩ c_a = ∅.
2. Lemma 5.1 (C = C_a) says an NA-credal world 1 would accept δ := 1_T − 1_{c_a}, with D(δ) = 0.
3. By (R⁰), δ is accepted iff δ ∈ 𝒦₀ or δ − γ′_* ∈ 𝒦₀ for some γ′.
   - δ ∉ 𝒦₀, since τ_δ(0) = h₀ − a < 0.
   - Q_{γ′} ⊆ T by (d1), so δ − γ′_* = 1_{T∖Q_{γ′}} − 1_{c_a∖P_{γ′}}. Its tail at 0 is
     h₀ − μ(Q_{γ′}) − a + μ(P_{γ′}) < 0.
4. So δ is rejected.

(b)
1. In D2′_H the sources partition S at each level (μ(P_{n,i,l}) = μ(S)/K_n ≤ μ(S)/2), the targets lie in W, and
   S ∩ W = ∅. The (d4) analogue holds with S for c_a (F1 Thm F1.6, step "Certificate").
2. δ := 1_W − 1_S has D = 0 and τ_δ(0) = μ(W) − μ(S) < 0, so δ ∉ 𝒦₀^W.
3. δ − γ′_* has τ(0) = μ(W) − μ(Q′) − μ(S) + μ(P′) < 0. So δ is rejected.

(c) Thm H24's world 1 is D2's world-1 rule on (x, 𝒢), and its world 2 is the same rule on (x̃, 𝒢′). ∎

**Proposition 5.3 (D2 has no α-obstruction, among all accepted comparisons; PROVED).** Let Σ z_k δ_k ≤ 0 a.e. with
δ_k accepted and z_k > 0.
1. Integrating over N₊ gives Σ z_k D(δ_k) ≤ 0. All accepted δ have D ≥ 0, so D(δ_k) = 0 for every k, and all are
   (R⁰)-accepted.
2. Near x = 1, a generator term is ≥ 1_{Q_γ} and a 𝒦₀ term is ≥ 0. Since Q_γ meets every neighbourhood of 1 non-nully
   (d2), no generator term occurs.
3. So Σ z_k δ_k ∈ 𝒦₀, with ∫ ≥ 0, and it is 0.

So D2's world 1 is a pure type-β world, and its hull is NA-credal (Cor 2.4(b)). This is a slightly stronger statement
than Thm D21 step 8, which treats relevant comparisons only. ∎

**Proposition 5.4 (D2's NA-credal hull has a non-closed section; PROVED).** Let 𝒢 be any design with a + 2h₀ ≤ 1. Let
X_T be the regular model with E₁X_T ∩ M = T = {x ≥ 1 − h₀}. In hull(world 1), the world-1 section
{b : C_b ≼ X_T} equals [0, a + h₀). It is not closed. In D2 itself the section is closed (Lemma D24).

*Proof.*
1. **The hull's acceptances with D = 0.** A ternary δ with D(δ) = 0 lies in hull(world 1) iff δ ≥ Σ z_k δ_k for
   accepted δ_k. Terms with D(δ_k) > 0 cannot occur, by integration over N₊. Each (R⁰)-accepted δ_k lies in 𝒦₀ or in
   γ_* + 𝒦₀, and 𝒦₀ is a convex cone closed under adding nonnegative functions. So every such δ lies in
   𝒦₀ + cone{γ_*}.
2. For b ≤ a + h₀ ≤ 1 − h₀, the vector is δ_b = 1_T − 1_{c_b}.
3. **b ≤ a is in the section.** Take any (d4) family with ε < 1. Then δ_b − Σ w γ_* = (1_T − Σ w 1_Q) + 1_{c_a∖c_b}
   ≥ 0. So δ_b ≥ Σ w γ_*, and δ_b is in the hull.
4. **b ∈ (a, a + h₀) is in the section.** Identify T with [0, h₀) by a measure isomorphism. For m ≥ 1 let T_j
   (j < m) be the cyclic interval of length b − a starting at j h₀/m. Put κ_j := 1_{T_j} − 1_{(a,b)}, writing (a,b)
   for c_b ∖ c_a.
   - Each κ_j is ternary, D(κ_j) = 0, κ_j ≥ 0 near 1, and for t ∈ (a, b), τ_{κ_j}(t) = (b − a) − (b − t) ≥ 0. So
     κ_j ∈ 𝒦₀, and it is accepted by (R⁰).
   - Every point of T lies in at most m(b − a)/h₀ + 2 of the T_j.
   - Choose ε and m with ε + (b − a)/h₀ + 2/m ≤ 1, and a (d4) family for ε.
   - Then δ_b − Σ w γ_* − Σ_j m^{−1} κ_j vanishes on c_b and equals 1 − Σ w 1_Q − m^{−1}#{j : h ∈ T_j} ≥ 0 on T.
   - So δ_b is in the hull.
5. **b = a + h₀ is not.** Suppose δ_b ∈ hull. By step 1, f := δ_b − Σ z_γ γ_* ∈ 𝒦₀ for some finite z ≥ 0. Using
   Q_γ ⊆ T, the tail of f at t ∈ (a, b) is (t − a) − Σ z_γ μ(Q_γ). Continuity at t = a forces z = 0. Then
   τ_{δ_b}(0) = h₀ − b < 0, so δ_b ∉ 𝒦₀. ∎

*Reading.*
- Any NA-credal world containing D2's world 1 accepts C_b ≼ X_T for every b < a + h₀. If it also has closed sections,
  it must accept C_{a+h₀} ≼ X_T.
- D2 keeps closed sections by refusing exactly these cancellation consequences: its (d3) finiteness bounds the
  generator branches by β_γ ≤ h₀ + μ(P_γ).
- Whether some larger NA-credal world containing D2's world 1 has closed sections and keeps the rest of Thm D21 is
  the two-world form of the open point.

### 5.3 L2, P1, T2n.1

**Proposition 5.5 (PROVED).** World 1 of L2 (Thm L21) and world 1 of P1 (Thm P1.10) are not NA-credal, for all
parameters. Hence neither world of T2n.1 is NA-credal.

*Proof for L2* (notation L2 §2).
1. **The forced comparison.** Generators g_{n,i,l} = 1_{Q_{n,i,l}} − 1_{P_{n,i}} are accepted: take F picking g at
   level n, and f = 0. The level-n average is h_n = Σ_{i,l} L_n^{−1} g_{n,i,l} = Σ L_n^{−1} 1_Q − 1_{c_a}, with
   Σ L_n^{−1} 1_Q ≤ ε_n ≤ 4·2^{−n} (G3).

   Put S_n := ⋃_{k∈I_n} ref_k ⊇ every level-n target, disjoint from c_a. Lemma 5.1 says an NA-credal world 1 accepts
   e := 1_{S_n} − 1_{c_a}, for n ≥ 2 (ε_n ≤ 1). Here D(e) = 0 and e = 0 on N₊.
2. **Rejection.** Suppose e|_M = g_F + f with f ∈ T.
   - If F(n′) ≠ ⊥ for some n′ > n, take k on its line. On M ∩ {x ≥ u_k} ⊆ d_a we have e = 0 and g_F ≥ 0, with
     g_F = 1 on ref_k. So τ_f(u_k) ≤ −λ(ref_k) < 0, which is impossible.
   - So only levels n′ ≤ n are used. Then
     ∫_M f = λ(S_n) − a − Σ_{n′≤n, F(n′)≠⊥}(λ(Q_{F(n′)}) − a2^{−n′}) ≤ λ(S_n) − a2^{−n}.
   - λ(S_n) ≤ r_{min I_n} = (1−u₀)5^{−min I_n}, and min I_n ≥ Σ_{m<n} Π_m grows super-exponentially. So for all large n,
     ∫_M f = τ_f(0) < 0, which is impossible.
3. So e is rejected.

*Proof for P1* (notation P1 §2).
- Replace c_a by Σ_n = S ∩ c_{v_n}, which is partitioned by the P_{n,i} with λ(P_{n,i}) = λ(Σ_n)/K_n.
- e := 1_{S_n} − 1_{Σ_n} ≥ h_n is forced, as above.
- Rejection of levels n′ > n: on {x ≥ u_k}, e = 0 and τ_f(u_k) ≤ −λ(ref_k) + Θ(F, k) ≤ −(16/25)r_k + r_k/25 < 0, by
  Lemma P1.10a.
- Then ∫_M f ≤ λ(S_n) − 2^{−n}λ(Σ_n) ≤ r_{min I_n} − 2^{−n}u₀ < 0 for large n, since
  r_{min I_n} ≤ 2^{−n}/(q_n+1).

*T2n.1:* its worlds are P1's world 1 and the mirror image. ∎

### 5.4 The NA-credal members

- **C2.1.** L_a(X) := ν_a(E₁X), a ∈ 𝒜, with densities F_aρ₀ > 0 on M and φ_a > 0 on N₊. Each L_a is real, record-
  additive and strictly guiding, and the world is ⋂_a ≤_{L_a}. The same holds at world 2.
- **VB.** L_i := (Φ_i, Ψ_i) ∈ ℝ²_lex.
  - Φ_i is record-additive and weakly guiding. The veto region within U lies in {h_i < 0}: u ∈ K′ gives Σh > 0 on U,
    so v_i·h < 0 forces h_i < 0. So Φ charges only i-wrong acceptances.
  - Ψ_i is strictly guiding and integral.
  - The lexicographic leading nonzero layer of a worsening is therefore positive.
- **VB′** is the same with Ψ̃_i. On the veto region a worsening adds a wrong acceptance there and raises Φ_i strictly.
- **FF2's P.** L_i := (E_i, B_i). E_i is real, purely finitely additive and weakly guiding (FF2 Prop 2.1(b)); B_i is
  strictly guiding.
- **Seeds.**
  - CC1 Thm 1.1: the four ladder records sum to a nonzero, nonpositive ladder vector, i.e. a nonzero improving flow. An
    α-obstruction.
  - AUDIT_CC_seeds Lemma 3: the sum is −4 on the designated increment over f_∅(A). An α-obstruction for every A.

---

## 6. The dichotomy for covers of T1

**Theorem 6.1 (PROVED).** Let R be a ranking on a decomposable domain whose world orders have strict (G). In
particular, R may be any ranking covering T1 under strict (G), (IB), (LA), (S), (C), (LF) on any decomposable domain.
Then exactly one of the following holds.
- **(A)** Every world is NA-credal. Its members can then be chosen in the single *ℝ of Theorem 3.1, as ultraproducts
  of cell witnesses.
- **(B)** Some world i has a **finite non-separable configuration**: finitely many accepted A_k ≼_i B_k, integers
  N, n_k ≥ 1, and a pair X ⋠_i Y such that N·φ_{rec(X,Y)} − Σ_k n_k φ_{rec(A_k,B_k)} is a worsening flow at world i.
  Equivalently, no cell witness respecting {A_k ≼ B_k} separates (X, Y).

Moreover (B) is the disjoint union of two cases.
- **(B-α)** Some world has an α-obstruction: Σ n_k φ_{rec(A_k,B_k)} is a nonzero improving flow. On M_U, restricted to
  relevant comparisons, this is (M1) of the write-up. The CC1 and audit seeds are of this kind.
- **(B-β)** No world has an α-obstruction, but some world's hull is strictly larger than the world. D2, D2′, H2.4, L2,
  P1 and T2n.1 are of this kind.

*Proof.* Theorem 2.1 at each world: (ii) fails iff (iii) fails, and a failure of (iii) is the displayed configuration.
The split is Cor 2.4(b). ∎

**Proposition 6.2 (hull reduction; PROVED).** Let R satisfy strict (G), (IB), (LA), (S), (C), (LF) with T1 ∈ C_R and no
α-obstruction at any world. Let R̄ replace each world by its hull. Then:
- R̄ has strict (G), (IB) and transitivity;
- R̄ has the same domain, hence (LF);
- every selected C_p is still competitive on supp p.

R̄ covers T1 iff, in R̄:
- (a) every section {p : C_p ≼̄_i X} is closed;
- (b) every C_p and T1 are undominated;
- (c) (C) holds.

Hence: either T1 has an all-NA-credal cover, or every cover without α-worlds loses (a), (b) or (c) on passing to hulls.

*Proof.*
- Cor 2.4: the hull of a world with no α-obstruction is NA-credal, hence has strict (G), (IB) and transitivity.
- ≼̄_i ⊇ ≼_i preserves the competitiveness disjunction.
- The remaining requirements of a cover are exactly (a)–(c). ∎

Prop 5.4 shows (a) failing in the hull of a full two-world system (D2).

**Proposition 6.3 (archimedean members are excluded for continuous selections; PROVED modulo FF2 Thm 4.1's import
chain, see §8).** Work on the full four-advice domain. Let q ↦ C_q be a selection continuous in measure, competitive on
supp q for every q. Let either T1 = C_{q₀}, or T1 be competitive on supp q₀ (as in every cover, by Theorem kkm and
transitivity). Suppose each world i has a **real-valued** strictly guiding record-additive L_i, finitely additive
allowed, such that L_i(C) ≤ L_i(X) whenever C ≼_i X, for C = C_q with i ∈ supp q, and for C = T1 with i ∈ supp q₀.
Then there is a contradiction.

In particular, in case (A) of Theorem 6.1 with such a selection, some world has no real-valued member. Every member of
its Π is non-archimedean.

*Proof.*
1. **The arrow charges are bounded.** On the region where b is worse than a, m_{ab} ≥ 0, hence m_{ab}(F) ≤ m_{ab}(that
   region). On the complement m_{ab} = −m_{ba} ≤ 0, likewise.
2. **Yosida–Hewitt.** m_{ab} = ρ_{ab}μ + π_{ab}, with ρ_{ab} ∈ L¹ and π_{ab} purely finitely additive. Put
   ℓ_i(h,a) := ρ_{a₀a}(h). Then ℓ_i has an integrable envelope.
3. **Concentration of π.** A bounded π ≥ 0 that is singular to μ has, for every δ, a set E with μ(E) < δ and
   π(E^c) = 0. Take E_k with μ(E_k) < δ2^{−k}, π(E_k^c) < 2^{−k}, and E := ⋃E_k.
4. **ℓ_i is strictly guiding.** If ρ_{ab} = 0 on a non-null R inside the worsening region, step 3 applied to |π_{ab}|
   gives a non-null R′ ⊆ R with m_{ab}(R′) = 0, against strict guidance.
5. **Localisation.** Apply step 3 to the 36 charges |π_{ab}| (12 arrows, 3 worlds). This gives increasing H_n with
   ⋃H_n co-null and |π_{ab}|(H_n) = 0. For X equal to C off H_n, L_i(X) − L_i(C) = ∫(ℓ_i(X) − ℓ_i(C)) dμ.
6. So (H2) and (H3) of FF2 Thm 4.1 hold, with T1's comparisons included in the second case. Thm 4.1, or Thm 4.1′ of
   §8.3, gives the contradiction. ∎

This extends INTERSECTIONS_additive (integral members, no continuity needed) to finitely additive members, at the price
of continuity in measure. Together with Prop 4.1, it locates any all-NA-credal cover with a continuous selection: some
world is not (M1), and is not archimedean at all. Each of its members has a standard part that is blind, which matches
L4.

**CONJECTURE 6.4 (the open point of §0).** In any ranking with strict (G), (IB), (LA), (S) (closed sections for every
model) and (C), on M_U or the full domain, every NA-credal world adds up.
- If it holds, Theorem 6.1 with Q4.2 / M0closed shows that every cover of T1 is in case (B).
- Evidence: VB (L3.4: the veto cannot be paid at the boundary), FF2's P (FF2 Lemma 2.4 / Cor 2.5) and D2's hull
  (Prop 5.4). These are the only known NA-credal worlds that fail to add up, and each fails closed sections.

---

## 7. Part B, first half: FF1

### 7.1 FF1 Theorem 5.2 — CORRECT

I checked the inputs first.
- **Lemma 2.1(a).** Derivations are finite. ✓
- **Lemma 3.1(c), (d).** A cell witness is record-additive on all models, so it is invariant along every derivation
  step, (IB) transports of cancelled composites included. In the stronger tier guidance steps may use arbitrary
  measurable models; L is defined and monotone on them. ✓
- **Lemma 3.3.** The Motzkin reading is correct.
  - The coefficient of a_c gives τ_c F_λ(g_c) = y_c ≥ 0. The coefficient of b_c gives sign((−g_c)_i)F_λ(−g_c) ≥ 0.
  - The ×-rows decouple, because selected models never give ×.
  - The nontriviality condition is right. ✓
- **Theorem 5.1, step 1.** Φ ≥ 0 from the allowed moves and Φ ≤ 0 from bets. Use c off the level values, where b_c
  lies in an open cell; Φ is a step function. The least q_{k,i} argument is correct. ✓
- **Theorem 5.1, step 2.** Rotations split levels (Lemma 4.1(b): a unique maximiser at a vertex with strictly descending
  edges; the contact point is distinct from the pivot, so w_l z_j − w_j z_l ≠ 0). Level 0 is handled by grading (iii).
  ✓

**Theorem 5.2, line by line.**
- **Step 1.** For any model X and cell witness, L(X) − L(C_p) = Σ_{c,a} x_c(a)(π_c(a) − [a_{C_p}(c) = a]). This is
  correct, and needs no cell-constancy of X. (In the tie tier X is in fact cell-constant, since records of E_i(S) are,
  but nothing depends on it.) ✓
- **Step 2.** W_i = V_i ∩ {open conditions}: sign rows, × above the others, and strict selected rows in the stronger
  tier. It is nonempty by Thm 5.1, hence relatively open and spanning.
  - L(X) = L(C_p) on W_i: by Lemma 3.1(c) in the tie tier; by (d) both ways in the stronger tier.
  - A linear functional vanishing on a spanning set vanishes on V_i. ✓
- **Step 3.** ψ_c(×) are free coordinates of V_i, because tie rows involve only ± coordinates. Their coefficients
  π_c(×) vanish. ✓
- **Step 4.** V_i = {x : t·x = 0 for all tie vectors t}, so V_i^⊥ = span{t}. The (c,±) entries of t_{pq} are
  (δ_q − δ_p)(A(±g_c)). So z = F_{λ_i}, with λ_i a combination of δ_q − δ_p over pairs with p_i = q_i: zero mass on
  every level of coordinate i. ✓
- **Step 5.** z depends only on X, C_p and the cells. 𝒞(S) is defined by S and the full sign pattern, so it is common
  to the three worlds. Hence F_{λ_1} = F_{λ_2} = F_{λ_3} on all oriented cell gambles.

  Injectivity of F on measures on S: world-1 bets and rotations realise every initial segment of the total order
  (level 0 by decreasing ρ₋, then levels, each ordered along its line), and 𝟙 realises S.

  *Presentation point:* a bet exactly at a level value lies on the boundary of D_{K_q} for q on that level. Use gambles
  in a small neighbourhood of the rotated bet. Their + acceptance set is constant there (Lemma 4.1(b) is an open
  condition), and some non-null cell of 𝒞(S) meets the neighbourhood. Its z_{(c,+)} is λ(that segment). ✓
- **Step 6.** π_c(+) = (δ_p + λ)(A(g_c)) ∈ [0,1], from z_{(c,+)} and π_c(×) = 0. ✓
- **Step 7.** For c ≠ p_i, β = [p_i < c] because λ has zero mass on each level below c. The two rotation signs give
  β ± P ∈ [0,1], using λ(level) = 0 and p ∉ level. Hence P = 0.
  - Level 0: the bets of Lemma 4.1(c) give λ(final ρ₋-segment) ∈ [0,1] and λ(initial ρ₊-segment) ∈ [0,1]. These are
    complementary within level 0 by grading (iii), and λ(level 0) = 0. Hence both vanish.
  - Level 1 is the single atom e_i, with zero mass.
  - ✓
- **Step 8.** supp λ ⊆ ⋂_i{q_i = p_i} = {p} and λ(level p_i) = 0 give λ = 0. Then π_c is C_p's advice on every cell,
  so X = C_p a.e. ✓

**Verdict: CORRECT** in both tiers, for every graded selection, all p ∈ Δ, and every ε.

Corrections to the record:
- FF3 §0.5 and §5.4 ("(C) is open") are superseded.
- FF3 Remark 5.3's CONJECTURE ("additive functionals are not expected to decide (C)") is false as a statement about
  additive functionals in general. It holds only for FF3's homogeneous class. FF1's functionals are cell witnesses
  adapted to S, and the bets give them enough test gambles.
- FF3 Lemma 5.2's moment identities are correct necessary conditions, of a now-empty class.
- In the language of §2, Thm 5.2 says: the three worlds' tie generators have NA-credal hulls whose common tie class at
  each selected model is a singleton.

### 7.2 FF1 Proposition 8.1 — CORRECT

1. The least (IB)-closed preorder containing Γ_i is the set of pairs with finite derivations from finite 𝒢 ⊆ Γ_i.
2. A cell witness respecting 𝒢 respects every derivation: transports keep the record, and transitivity adds.
3. A Φ_i-pair derived from 𝒢 contradicts the separating witness for (𝒢, that pair).
4. Strict (G): weak (G) holds because Γ_i ⊇ guidance. A derived X ≼ Y with Y strictly better contradicts any witness
   for 𝒢 (L(X) ≤ L(Y) < L(X)). Such a witness exists by the first hypothesis.

The application (clean fixed point, then a cover with strict slack) is conditional on EE1 Thms 3.1 and 2.1, as FF1 says.

Strengthening (Cor 2.4(d)): the hypothesis is equivalent to "hull(Γ_i) is NA-credal and avoids Φ_i". The conclusion
can then be stated for hull(Γ_i) ⊇ the least (IB)-closed preorder. FF1's "(M2) necessarily" remark (§8.3) should read:
such a cover is in case (A) of Theorem 6.1 at every world where the hull is used. By Prop 4.1 this implies not-(M1),
and by Q4.2 some world does not add up, so that world is (M2).

---

## 8. Part B, second half: FF2

### 8.1 Theorem 4.1 — CORRECT (modulo the import chain)

- **Step 1.**
  - The range Z_n is convex by Lyapunov: integrals over H_n of selections from four integrable values, with
    nonatomic μ.
  - Z_n misses the open negative orthant: competitiveness gives some i ∈ supp q with C_q ⪯_i X, and (H3) gives
    z_i ≥ 0.
  - Finite-dimensional separation gives w_n ≥ 0 with w_n·Z_n ≥ 0.
  - Pointwise (WB) a.e. on H_n, by a measurable switch inside H_n (the switched model equals C_q off H_n).
  - Countably many n and compactness of Δ_J give a limit w with (WB) a.e. on ⋃H_m.
  - ✓
- **Step 2 (closed graph).** Convergence in measure of C_{q_n} gives a.e. convergence of advice along a subsequence.
  Advice takes four values, so it is eventually constant a.e. The (WB) inequalities pass to the limit. W(q) uses all
  w ∈ Δ (the CC1/AA repair). ✓
- **Step 3.** This is CC1 Lemma 3.4. Strict separation of w* from compact convex W(q) can be projected to T, because
  differences lie in T.
  - The graph of O is open by upper hemicontinuity, so Browder gives a continuous selection.
  - Brouwer gives a fixed point of π_Δ(q − v(q)), hence −v(q) ∈ N_Δ(q).
  - Interior: N_Δ ∩ T = {0}. Face q₃ = 0: v = c(e₃ − u), c > 0, and v·(w₀ − w*) = −c w*₃ < 0. Vertices likewise.
  - ✓
- **Step 4.** For a ≠ b every coordinate of ℓ(h,a) − ℓ(h,b) is nonzero, so its zero set in Δ is a segment or empty.
  Fubini gives null ties for a.e. w. A weak Bayes model with null ties is the unique Bayes model. ✓

  *Remark.* Step 3 covers **every** interior w. So at every w ∉ E the unique Bayes model equals some C_q and is
  coherent. That is the write-up's strong form of (γ) (every q off a null E), which D1 uses. AUDIT_BB Lemma 2.0 is
  correct (pointwise stability of a unique optimum plus closedness of coherent models, R1 Prop 3.1) but is not needed
  here.
- **Step 5.** Two-world weight: gambles near (1, 1, −t), t slightly above t* = 2c₀/(c₀+ε), are outside cl D_{T1}, and
  −h ∉ D_{T1} because t* < 2. So T1 is silent there, and acceptance is available and better at worlds 1, 2. Vertex
  weight: T1 is not P₁. ✓
- **Step 6 (imports).** I checked the stated hypotheses against what Steps 1–5 deliver.
  - **D1** [write-up Thm D1, R1]: strictly guiding, integral penalties, integrable envelope, (γ), D_{T1} Bayes at an
    interior p*, (LF). All are delivered. Conclusion: p* ∉ E. ✓
  - **BB2 Thm 6.1** [= M3.9; R1 per CC3]: (H1) (LF) with acceptance and silence available near ∂D_{T1}: full domain ✓.
    (H2) strictly guiding with × last ✓. (H3) (γ) ✓. (H4) ✓. BB2 states that (γ₀) at boundary weights, integrability
    and (Av) are not used.
  - **M3.8** [R1]: standing data of M3 §5 (strictly guiding integral (γ)-field, unique Bayes at p* ∈ Ω), (Av) (trivial
    on the full domain), (C2) and (C3) (BB2), E null and p* ∉ E. All delivered.
  - **M3.7(d)** uses only limits through Ω and closedness of coherent models. ✓
  - No step uses the ranking.

**Verdict: CORRECT**, at the status of D1, BB2 Thm 6.1 and M3.7–M3.8 (each refereed once). FF2's "What is and is not
used" list is accurate.

### 8.2 Corollary 4.3 — CORRECT AS STATED; the readings overstate

Cor 4.3 assumes (H1), which includes "T1 = C_{q₀}". The sentences "in every cover whose selection is continuous in
measure …" (FF2 §0.5; Reading after Cor 4.3; BRIEF27 "necessary features") drop that hypothesis.

In a cover T1 ∈ C_L is only tied at every world with some selected C_{q₀} (Theorem kkm). Then (H3) says nothing about
comparisons out of T1, and Step 5 cannot be run for T1. Replacing C_{q₀} by T1 in the selection keeps competitiveness
and sections (ties), but may destroy continuity in measure at q₀.

### 8.3 Repair

**Theorem 4.1′ (PROVED, same status).** In Thm 4.1, replace "T1 = C_{q₀}" by "T1 is competitive on supp q₀ for some
q₀". Strengthen (H3) to include, for i ∈ supp q₀ and X equal to T1 off H_n, the implication
T1 ⪯_i X ⇒ ∫(ℓ_i(X) − ℓ_i(T1)) ≥ 0. The conclusion is unchanged.

*Proof.*
- Steps 1–4 concern the selection only.
- Step 5: run Step 1 with T1 in place of C_q. This uses only competitiveness of T1 on supp q₀ and the added (H3). It
  gives (WB) for T1 at some w ∈ Δ_{supp q₀}, and the Step-5 argument makes w interior.
- Step 6 is unchanged. ∎

In every cover T1 is competitive on supp q₀: C_{q₀} ⪯_i X for some i ∈ supp q₀, and T1 ⪯_i C_{q₀}. So the corrected
reading is: **in every cover with a selection continuous in measure, some world admits no integrable strictly guiding
penalty endorsing its local comparisons out of selected models and out of T1.** Prop 6.3 uses this form.

---

## 9. Status table

| Item | Statement | Label |
|---|---|---|
| 2.0 | finite integer systems transfer from ordered groups to ℝ | PROVED |
| 2.1 | NA-credal ⟺ finite additive separability (cell witnesses) ⟺ finite cancellation in records ⟺ conic (posi) acceptance cone; (IB), transitivity automatic | PROVED |
| 2.4 | NA-credal hull; α-obstructions; FF1 Prop 8.1 ⟺ hull avoids Φ | PROVED |
| 3.1 | one ultrapower *ℝ (or Hahn ℝ((Γ))) suffices for all NA-credal worlds | PROVED |
| 3.2 | left-germ world: NA-credal, needs a (0,1)-chain of archimedean classes; ℝ^n-lex, countable or well-ordered levels insufficient | PROVED |
| 4.1 | NA-credal ⟹ ¬(M1) (all accepted comparisons); ≠ (M2) | PROVED |
| 5.1 | design principle: NA-credal forces the averaged comparison | PROVED |
| 5.2–5.3 | D2 (h₀ + sup μ(P) < a), D2′ (μ(W) < μ(S)/2), H2.4 not NA-credal; D2 has no α | PROVED |
| 5.4 | D2's hull: section of X_T = [0, a+h₀), not closed | PROVED |
| 5.5 | L2, P1, T2n.1 not NA-credal (all parameters) | PROVED |
| 5.0 rest | C2.1, VB, VB′, FF2's P NA-credal; CC1/audit seeds type α | PROVED |
| 6.1 | dichotomy (A) all NA-credal / (B) finite non-separable configuration, (B-α) ⊇ (M1), (B-β) | PROVED |
| 6.2 | hull reduction | PROVED |
| 6.3 | real (finitely additive) members excluded for continuous selections through T1 | PROVED modulo FF2's chain |
| 6.4 | NA-credal worlds in full systems add up (⇒ no all-NA-credal cover of T1) | CONJECTURE |
| B1 | FF1 Thm 5.2 | CORRECT (presentation points only) |
| B2 | FF1 Prop 8.1 | CORRECT |
| B3 | FF2 Thm 4.1 | CORRECT modulo D1, BB2 6.1, M3.7–8 |
| B4 | FF2 Cor 4.3 | CORRECT as stated; readings repaired by Thm 4.1′ |
