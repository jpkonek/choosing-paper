# R2. Do (G), (IB), (LA), (S), (C) force additive behaviour on decomposable domains?

12 October 2026. Notes for round 9. Status labels: **PROVED** (full proof below),
**CHECKED** (verified carefully, proof sketched), **CONJECTURE**.
Setting and notation are those of BRIEF.md: decomposable domain M, i.e. the class of evaluable models is
restricted to the models whose advice on the choice represented by g lies in a measurable advice range
𝒜(g) ⊆ {+,0,−,×}, g ∈ H; models mod null sets; at world i the ranks are good 0, silence 1,
bad 2, contradiction 3; C_L is the set of coherent undominated members of M; U_L is the set of
all undominated members of M. *Additive (strictly guiding) loss*: L_i(X) = ∫_H ℓ_i(g, a_X(g)) dμ,
where ℓ_i(g,·) depends only on the rank at world i and is strictly increasing in it, with an
integrable envelope (v3 eq. (local-penalties)). An *additive system* ranks each world by its
L_i. In n = 2, write r(g) = −g_2/(g_1−g_2) on mixed problems (g_1 > 0 > g_2). A coherent
model is D_{[α,β]}: it gives + if r < α, 0 if α < r < β, and − if r > β (unanimous problems: +).

## 0. Summary of answers

* **Q1, per-model form**: trivially yes (§1, Lemma 2). Every coherent D ∈ M is the *unique*
  Bayes model of some strictly guiding additive loss on M. This says nothing about coverage.
* **Q1, extension form** ("weaker"): **no** (§2, Prop. 4, PROVED). A lexicographic system
  satisfies all of (G), (IB), (LA), (S), (C), (E), yet has no one-sided strictly guiding
  additive (or finitely additive) extension at any world on selected-vs-arbitrary comparisons.
  Its selected family is nevertheless exactly the Bayes family of an additive (S),(C) system.
  So extension is sufficient for the reduction to additive realisation (Lemma 3), but not
  necessary. It is the wrong test.
* **Q1, family form** (the right form): is U_L the undominated set of some additive
  (LA),(S),(C) system on M_L? New rigidity of additive systems (§3, PROVED):
  * the interior Bayes model is unique (Lemma U);
  * U_add contains **no pair D_{K_A}, D_{K_B} with K_A ⊂ int K_B** (Theorem N, any n);
  * in n = 2, U_add is a continuous monotone path (Prop. P).

  Consequently, in **n = 2, Q1 (family form) ⇔ "U_L has no strictly nested pair"** (Theorem R,
  PROVED). In every n, a system whose U_L contains an interior-nested pair would be a Q2
  counterexample.
* **No-nesting proved beyond additivity** (§4, PROVED):
  * countable unanimity (Pareto) families of additive criteria (incomplete), any n;
  * n = 2 systems with one world additive and the other a two-level lexicographic ranking with
    additive levels (non-Archimedean). This class includes rankings with no additive extension.

  For these classes Q1 holds in n = 2.
* **Lexicographic rankings and (S)** (§5, PROVED): at a lexicographic world, the primary
  profile of the selection has a local minimum at every p where C_p can be improved within its
  primary level. So U_L has only countably many such primary levels. A decoupled two-lex system
  has nested pairs, indeed a whole 2-parameter family, in U_L, satisfies (G), (IB), (LA), (C),
  and **fails (S) for exactly this reason**.
* **Q2**: no counterexample found. The n = 2 search space is now narrowed to both worlds
  genuinely non-additive, with a coupling different from §4–5 (CONJECTURE 1: none exists).

---

## 1. Preliminaries

**Fact 0** (BA lem:complete-class, valid verbatim on any domain M; PROVED there).
Assume (LA),(S) on M.
(a) Every X ∈ M has a selected C_p with C_p ⪯_i X for all i.
(b) Every X ∈ U_L is tied at every world with some selected C_p.
The proof is KKM on Δ with A_i = {p : C_p ⪯_i X}: closed by (S), and covering faces by
competitiveness of C_p on supp p *against M*. Nothing else is used.

**Lemma 1 (PROVED).** Under (LA),(S),(C): U_L = C_L ⊆ coherent. U_L is exactly the set of
models tied at every world with a selected model.
*Proof.* Fact 0(b) ties each X ∈ U_L to a selected C_p ∈ C_L; (C) gives X ∈ C_L. Conversely, if
X ties C_p at every world and Y dominated X, then Y would dominate C_p by transitivity. ∎

So "undominated" and "selected mod ties" agree, and every undominated model is coherent. This
is the lever used throughout: **an incoherent undominated model contradicts (LA)+(S)+(C)**.

**Fact (exchanges; CHECKED, elementary).** By (IB), X ⪯_i Y depends only on
(Z, a_X|_Z, a_Y|_Z) with Z = {a_X ≠ a_Y}. Weakly favourable exchanges on disjoint supports sum
to a weakly favourable exchange: pass through the intermediate splice, which lies in M, and use
transitivity. (G) makes guidance-improving exchanges strictly favourable. Only this much of the
"exchange" structure is used below.

**Pointwise Bayes on decomposable domains (PROVED, standard).** For an additive loss and a prior p, a
model is p-Bayes on M iff a.e. it picks a minimiser of φ_p(g,a) = Σ p_i ℓ_i(g,a) over 𝒜(g).
(Otherwise, splice in a measurable pointwise minimiser — fixed tie order, finite advice ranges — on the
non-null bad set.) The attainable set {(L_i(X))_i : X ∈ M} is convex and compact (Aumann's
integral of a finite-valued measurable correspondence over an atomless measure; Lyapunov). So
**every X ∈ M not strictly dominated at every world is Bayes at some p ∈ Δ** (separation). This
is v3 lem:bayes-necessary (b) on decomposable domains.

## 1a. Per-model Q1 is trivial

**Lemma 2 (PROVED).** Let D ∈ M be coherent and p ∈ int Δ. There are bounded local penalties,
strictly increasing in rank at each world, for which D's advice is the unique minimiser of
φ_p(g,·) over 𝒜(g) at a.e. g. So D is the unique p-Bayes model mod null.

*Proof.* Fix g off null sets; write a = a_D(g) ∈ 𝒜(g); D never gives ×.
* (a = +). Coherence excludes g ≤ 0, so P = {i : g_i > 0} ≠ ∅. Use penalties (0,1,2,3)
  (good, silent, bad, ×) at worlds in P, and η·(0,1,2,3) elsewhere. Against b ∈ {0,−,×}:
  φ_p(b) − φ_p(+) ≥ p(P) − 2η(1 − p(P)) > 0 for η < p(P)/2.
* (a = −) is symmetric.
* (a = 0). Then g is mixed (g ≥ 0 would be accepted). Use (0, η, 1+η, 2+η) at every world.
  Against +: φ difference = p(N)·1 − p(P)·η, with N = {g_i < 0}. Against −:
  p(P)·1 − p(N)·η. Both are positive for η < min(p(N)/p(P), p(P)/p(N)). Against ×: positive.

The choices depend measurably on (sign pattern of g, a_D(g)). ∎

So "every undominated model is Bayes for some strictly guiding additive loss" holds trivially
model by model. What matters is a **single** additive system realising **all** of U_L, with
(S) and (C).

## 2. The extension form of Q1

**Lemma 3 (the trap on decomposable domains; PROVED, = BA thm:extension / CCF lem:cboi transplanted).**
Suppose each world k has an additive strictly guiding ℓ_k with the one-sided bound
(W_k): B ∈ C_L, X ∈ M, B ⪯_k X ⇒ ℓ_k(B) ≤ ℓ_k(X). Then
(i) every ℓ-Bayes B (any p) has a selected coherent C with ℓ(C) ≤ ℓ(B) coordinatewise; hence C
is p-Bayes, and ℓ(C) = ℓ(B) if p is interior;
(ii) every D ∈ U_L is ℓ-Bayes at some prior.

*Proof.* (i) Fact 0(a) and (W). (ii) D ∈ C_L (Lemma 1) is tied with a selected C_p,
competitive on supp p. For every X some i has C_p ⪯_i X, so ℓ_i(C_p) ≤ ℓ_i(X); thus C_p is not
strictly ℓ-dominated everywhere, so it is Bayes. (W) both ways along the tie gives
ℓ(D) = ℓ(C_p). ∎

So (W) gives *weak additive realisation*: D is ℓ-Bayes and every prior has a coherent ℓ-Bayes
model. These are exactly the hypotheses of the v3 three-vertex obstruction. That is how the
brief's "If yes, coverage reduces to additive realisation" works.

**Proposition 4 (one-sided extension fails, yet the family is additive; PROVED).** Let ℓ² be
any additive loss satisfying v3 thm:general on M = all models; e.g. the precise-target system,
or any v3/CSE construction. Put L¹_i(X) = μ{g unanimous : a_X(g) ≠ +}. This is weakly guiding,
with local penalties 0, 1, 1, 1. Rank each world lexicographically by (L¹_i, L²_i). Then:
1. (G) strict and weak, (IB), (E) hold.
2. U = {C_p} (the ℓ²-Bayes family); (LA), (S), (C) hold with the same selection.
3. At **every** world i there is no strictly guiding additive ℓ_i, nor any finitely additive
   one of CBOI's positive form, satisfying (W_i).

*Proof.*
1. Composite (G): a pointwise improvement weakly lowers both coordinates and strictly lowers
   L²_i if strict. (IB): both levels are integrals, so replacing common advice shifts both
   models' coordinates equally.
2. If L¹_j(X) > 0 for some j, change X to + on its non-+ unanimous set. This weakly improves
   every world pointwise and strictly on a non-null set, so the new model strictly dominates X.
   Hence undominated ⇒ L¹ ≡ 0. On M₀ = {L¹ ≡ 0} the system is ℓ², and v3 thm:general(c) gives
   U = {C_p}. Sections: {q : C_q ⪯_i X} is all of Δ if L¹_i(X) > 0, and the ℓ²-section
   otherwise; both are closed. Competitiveness: if L¹_i(X) > 0 for some i ∈ supp p then
   C_p ≺_i X; otherwise use ℓ²-competitiveness. (C): a lex tie everywhere is an ℓ²-tie, so use
   v3 (C).
3. Pick p with C_p ≠ D_i (e.g. p = e_j, j ≠ i). Then δ = ℓ_i(C_p) − ℓ_i(D_i) > 0, because C_p
   gives non-good advice at i on a non-null set. Choose a non-null unanimous N with
   ∫_N (ℓ_i(g,0) − ℓ_i(g,+)) dμ < δ. For a charge, partition the unanimous region into m pieces
   and take the lightest. Let X = D_i with silence on N. Then C_p ≺_i X (primary), but
   ℓ_i(X) < ℓ_i(C_p). ∎

*Moral.* Extension properties are sufficient for the reduction to additive realisation, but
not necessary. Q1 must be posed for families.

## 3. Rigidity of additive closed choice (new)

**Lemma U (uniqueness; PROVED).** Consider an additive strictly guiding system on a decomposable
domain M with (LA),(S),(C). For every p ∈ int Δ, any two p-Bayes models in M agree a.e.
Equivalently, the pointwise minimiser of φ_p over 𝒜(g) is a.e. unique.

*Proof.* Let B, B′ be p-Bayes, differing on a non-null Z where the advice of both is a pointwise
minimiser. Every splice B_S (B′ on S ⊆ Z, B elsewhere) is in M and p-Bayes.
Some B_S is incoherent:
* If B or B′ is incoherent, take S = ∅ or S = Z.
* Otherwise both are cones, so Z is a cone mod null. Take S = Z ∩ {‖g‖ < 1}. In polar
  coordinates, on a positive-measure set of directions in Z, B_S's advice changes with the
  radius. A coherent model's advice is scale invariant, so B_S is incoherent.

Let E = B_S be incoherent. Fact 0(a) gives a selected C with ℓ(C) ≤ ℓ(E) coordinatewise. Since
E is p-Bayes and p is interior, ℓ(C) = ℓ(E). So E is tied at every world with C ∈ C_L, (C) puts
E in C_L, and E is coherent. Contradiction. ∎

*Consequence.* The uniqueness hypothesis in v3 thm:general is **necessary** at interior priors.
Additive realisation on a decomposable domain therefore means a measurable, sign-preserving CPM,
restricted to the advice ranges, that is a.e. single-valued (non-tangent a.e.) at every interior prior. Distinct members of
U_add have disjoint sets of interior Bayes priors.

**Theorem N (no interior nesting for additive systems; PROVED, any n ≥ 2).** In the setting of
Lemma U, let D_{K_A}, D_{K_B} ∈ M. Suppose that for every mixed sign pattern σ the set
R_σ = {g : sign g = σ, A accepts g, B silent on {g,−g}} is non-null. Then A and B are not both
undominated. The hypothesis holds whenever K_A ⊂ int K_B (interior relative to Δ).

*Proof.* By §1, A is p_A-Bayes and B is p_B-Bayes. On R_σ, both + (from A) and 0 (from B) are
in the advice range. Let c(g) = (ℓ_i(g,0) − ℓ_i(g,+))_i; it has sign pattern σ. Pointwise optimality gives
p_A·c ≥ 0 ≥ p_B·c, so c(g)·u ≥ 0 a.e. on R_σ, with u = p_A − p_B.

If u ≠ 0, u has both signs, since Σu = 0. Take σ* with σ*_i = −sign u_i on supp u, completed
arbitrarily. σ* is mixed, and c·u < 0 on R_{σ*}: contradiction. So p_A = p_B = p. If p_j = 0
for some j, take σ with σ_i = + exactly on supp p. On R_σ, B's 0 requires p·c ≤ 0, but
p·c = Σ_{supp p} p_i c_i > 0. So p is interior, and Lemma U gives A = B, contradicting
non-null R_σ.

Sufficiency of K_A ⊂ int K_B: for σ with positive set P and negative set N, let
g = a·1_P − b·1_N. Choose b/a slightly below min_{K_A} m(P)/m(N). Then min_{K_A} m·g > 0, while
some m′ ∈ K_B near the minimiser has m′·g < 0 and m₀ ∈ K_A has m₀·g > 0, so B is silent. The
conditions are open, giving positive measure; varying the weights within P and N keeps the
pattern σ. ∎

So additive closed choice never selects a credal set together with one strictly inside it.
For example, an ε-contamination target T1 and the uniform precise model are never both in
U_add.

**Prop N2 (n = 2 form; PROVED).** In n = 2, "strictly nested" (α_B < α_A ≤ β_A < β_B) already
suffices: R1 = {α_B < r < α_A} and R2 = {β_A < r < β_B} are the two patterns.

**Prop P (n = 2, additive U is a continuous monotone path; PROVED).**
In n = 2, under Lemma U's hypotheses, U_add = {B_t : t ∈ [0,1]}:
* B_t is the unique t-Bayes model;
* α(t), β(t) are non-decreasing and continuous;
* B_0 and B_1 are the world-2-best and world-1-best evaluable models.

*Proof.*
* Monotone: the threshold argument of Prop N2 for t < t′. On a set where B_t gives + and
  B_{t′} gives 0 or −, one gets t ≥ (threshold) ≥ t′.
* Unique: at interior priors by Lemma U; at t = 0 or 1, because ranks are distinct at a world.
* Continuous in measure: the minimiser is a.e. unique, so it is eventually constant along
  t_k → t (as in v3 thm:general).
* U_add = Bayes set: by §1 (Bayes ⇒ undominated by uniqueness; undominated ⇒ Bayes). ∎

**Theorem R (n = 2 reduction; PROVED).** Let n = 2 and let L be any system on a decomposable domain M
with (G),(IB),(LA),(S),(C). Then U_L is the undominated set of an additive strictly guiding
(LA),(S),(C) system on M **iff** U_L contains no strictly nested pair.

*Proof.* (⇒) Prop N2.

(⇐) Step 1: U_L is a chain in the monotone order ⪯_m. Distinct members are strictly ordered
at both worlds by (G): v ≻_m u ⇒ v ≺_1 u and u ≺_2 v. So U_L = selected set exactly, by
Lemma 1. For u ∈ U_L, A_1(u) = {q : C_q ⪰_m u} and A_2(u) = {q : C_q ⪯_m u}; both are closed.

Step 2, no adjacent pairs. If u ≺_m v had nothing between them, A_2(u) and A_1(v) would split
Δ into two disjoint nonempty closed sets.

Step 3, no measure gaps. Let u_k ↑ strictly with (α_k, β_k) → (a′, b′), and let
X = D_{[a′,b′]}. X ∈ M: at each problem its advice is advice that the u_k give eventually.
Let L = {u : u ⪯_m some u_k} and R = U_L \ L. If X were not selected, then A_1(X) = {C_q ∈ R}
and A_2(X) = {C_q ∈ L}. These are disjoint, closed and nonempty (C_{e_1} ∈ R), which is
impossible. So X ∈ U_L; similarly for decreasing sequences.

Step 4. Parametrise by φ = α + β. It is strictly increasing on U_L, and by Steps 2–3 its image
is an interval. So α and β are continuous non-decreasing functions of the parameter, from
C_{e_2} (world-2-best evaluable model, by the vertex lemma) to C_{e_1}.

Step 5, realisation. At mixed g the path's advice moves − → 0 → + through the advice in the advice range,
switching at s_−(g) ≤ s_+(g). These switch points are functions of r and are hit at single
r-values by continuity, so {s_± = t} is null for every t.
* If s_− < s_+: world 1 penalties (+, 0, −) = (0, 1−s_+, 1−s_+ + 1−s_−); world 2 penalties
  (−, 0, +) = (0, s_−, s_− + s_+). The +/0 tie is at t = s_+ and the 0/− tie at t = s_−.
* If s_− = s_+: make silence costly, i.e. (0, 1−η, 1) and c(0, 1−η, 1) with η < ½ and c chosen
  for the +/− tie.
* × costs most; unanimous problems are good at both worlds.
* If a kind of advice is not in the advice range at g, or a switch point is 0 or 1, its zero gap is replaced by
  any positive gap. This does not move the Bayes advice among the advice in the advice range; the sets
  {s_± ∈ {0,1}} ∩ (0,1)-switches are null by the same continuity argument.

v3 thm:general (its proof is valid on decomposable domains) gives an additive (LA),(S),(C) system whose
t-Bayes model is the path at t. So U_add = U_L. ∎

So **Q1 in two worlds is exactly the No-Nesting property.** In n ≥ 3, Theorem N makes
"interior-nested pair in U_L" a sufficient certificate for a Q2 counterexample.

## 4. No-Nesting beyond additive rankings (n = 2 unless stated)

**Prop 5 (countable unanimity; PROVED, any n, with the R_σ hypothesis of Theorem N).**
Let X ⪯_i Y ⇔ L^k_i(X) ≤ L^k_i(Y) for all k ∈ ℕ. Each L^k_i is an integral of weakly ordered
local penalties (good ≤ silent ≤ bad ≤ ×) with an integrable envelope h_k. Suppose the
combined ranking has strict (G), (IB), (LA), (S), (C). Then U_L has no pair A, B as in
Theorem N.

*Proof.*
* Let ℓ = Σ_k c_k L^k with c_k = 2^{-k}/(1+∫h_k). By BA's corollary (essential-union argument
  over the *whole* family) it is strictly guiding a.e., and it weakly respects ⪯ in both
  directions.
* By competitiveness (Lemma 1), A and B are not strictly ℓ-dominated everywhere, so they are
  ℓ-Bayes. The argument of Theorem N forces a common interior prior p.
* Some incoherent splice E is p-Bayes (proof of Lemma U). Fact 0(a) gives a selected C with
  L^k_i(C) ≤ L^k_i(E) for all k, i. Interiority forces ℓ(C) = ℓ(E), hence every
  L^k_i(C) = L^k_i(E): an L-tie at all worlds.
* (C) then makes E coherent: contradiction. ∎

For uncountable families, the countable subfamily only gives ℓ-ties, not L-ties: OPEN.

**Theorem 6 (one lexicographic world; PROVED).** n = 2, decomposable domain M, (LA),(S),(C).
* World 2 is additive and strictly guiding (loss L₂).
* World 1 ranks lexicographically by (L¹₁, L²₁): additive levels, L¹₁ weakly guiding, L²₁
  weakly guiding and strict where L¹₁'s local differences vanish, so the composite is strictly
  guiding.

Then U_L has no strictly nested pair, so by Theorem R it is additively realisable. The theorem
also holds with the worlds swapped. The class contains rankings with **no** additive one-sided
extension, e.g. world 1 of Prop 4.

*Proof.* Let A, B ∈ U_L with R1 (A: +, B: 0) and R2 (A: −, B: 0) non-null. At world 1 on R1,
let d₁ = ℓ¹₁(0) − ℓ¹₁(+) ≥ 0; on R2, let e₁ = ℓ¹₁(−) − ℓ¹₁(0) ≥ 0. At world 2, d₂ and e₂ are
the analogues, both > 0.

K¹ = {(L¹₁, L₂)(X) : X ∈ M} is convex and compact (Aumann). An undominated A is weakly Pareto
minimal there: something strictly better in both coordinates would dominate it. So A is
supported by some (t, 1−t). t = 0 is impossible: then A would minimise L₂, but it gives + on
R1 where 0 is in the advice range and better at 2. Similarly for B. Two cases:
* Case 1: some support with t ∈ (0,1).
* Case 2: only t = 1, i.e. the model minimises L¹₁ over M.

*1/1.* A's + and B's 0 on R1 give t_A d₁ ≥ (1−t_A) d₂ > 0 and t_B d₁ ≤ (1−t_B) d₂. So
d₁ > 0 and t_B ≤ t_A. On R2, t_A e₁ ≤ (1−t_A) e₂ and t_B e₁ ≥ (1−t_B) e₂ > 0. So e₁ > 0 and
t_A ≤ t_B. Hence t_A = t_B = t₀.

Let 𝔅 be the decomposable domain of pointwise minimisers of t₀ℓ¹₁ + (1−t₀)ℓ₂ (the models in M whose
advice a.e. minimises it over 𝒜(g)); A, B ∈ 𝔅.
* Undominatedness makes A minimise L²₁ over {X ∈ 𝔅 : L¹₁(X) = L¹₁(A)}: on 𝔅, equal L¹₁ forces
  equal L₂.
* {(L¹₁, L²₁)(X) : X ∈ 𝔅} is convex and compact. L¹₁(A) is interior to its range: at the
  minimum, A would be an L¹₁-minimiser, but it gives − on R2 where 0 is in the advice range and e₁ > 0;
  the maximum fails on R1. So a finite multiplier λ_A exists, and A pointwise minimises
  ℓ²₁ + λ_A ℓ¹₁ over 𝔅's advice ranges. Likewise for B.
* On R1, λ_B ≤ −δ²/d₁ ≤ λ_A; on R2, λ_A ≤ −ε²/e₁ ≤ λ_B. Here δ², ε² are the ℓ²₁ differences.
  So λ_A = λ_B = λ*, and + and 0 (resp. − and 0) tie on R1 (resp. R2).
* Hence every splice E of A and B on R1 ∪ R2 minimises L²₁ + λ* L¹₁ over 𝔅.

Such an E is undominated:
* a dominator X cannot have smaller L¹₁, since t₀ > 0 and E is t₀-optimal;
* so L¹₁(X) = L¹₁(E), then L₂(X) = L₂(E) and X ∈ 𝔅;
* strictness would need L²₁(X) < L²₁(E), contradicting λ*-optimality.

Take E incoherent (the norm splice); this contradicts Lemma 1.

*1/2 and 2/1.* If B minimises L¹₁, then d₁ = 0 on R1, contradicting d₁ > 0 from A's case-1
inequality. Symmetrically, using e₁ on R2.

*2/2.* Then d₁ = 0 on R1 and e₁ = 0 on R2, so the secondary is strict there. Let 𝔐 be the decomposable
domain of L¹₁-minimisers. On 𝔐, world 1 is L²₁ (additive) and world 2 is L₂: the additive
threshold argument gives a common s* ∈ (0,1); the boundaries are excluded by the strict
secondary. The splice E is s*-Bayes on 𝔐 and E ∈ 𝔐. A dominator must lie in 𝔐 (its L¹₁ cannot
exceed the minimum), which contradicts s*-optimality. E is undominated and incoherent:
contradiction. ∎

## 5. Lexicographic rankings and closed sections

**Theorem 7 (local-minimum / countability; PROVED, any n, any real-valued levels).** Suppose
world i ranks by lex(L¹_i, L²_i) with real-valued (not necessarily additive) L¹_i, L²_i, and
(S) holds. Let f_i(q) = L¹_i(C_q). If some Z ∈ M has L¹_i(Z) = f_i(p) and
L²_i(Z) < L²_i(C_p) ("p improvable at i"), then p is a local minimum of f_i. Hence the set
{f_i(p) : p improvable at i} is countable. With (C), the same holds for
{L¹_i(X) : X ∈ U_L improvable at i}.

*Proof.* p ∉ A_i(Z), which is closed. So some neighbourhood N of p misses A_i(Z), i.e.
f_i ≥ f_i(p) on N. Choose a basic open V with p ∈ V ⊆ N from a countable base; then
f_i(p) = min_V f_i, so the value is determined by V. For X ∈ U_L, X is lex-tied with a selected
C_p (Lemma 1); a tie means equal (L¹_i, L²_i), so C_p is improvable iff X is. ∎

This is the general form of the step in BA prop:lex. Breakage of closed sections at primary
ties is **avoidable exactly when** the improvable members of U_L occupy countably many primary
levels at each lex world. In Prop 4 there is one level; there, too, the family is additive.

**Prop 8 (decoupled lex: nesting in U, failure of (S); PROVED).** n = 2. Fix nested
A = D_{[α_A,β_A]}, B = D_{[α_B,β_B]} with R1, R2 as above. Let the class M₀ of evaluable models consist of the models agreeing
with A off R1 ∪ R2, with advice range {+,0} on R1 and {0,−} on R2. Write a model as (S, T): S = its +
part of R1, T = its silent part of R2. Its coherent members are exactly D_{[x,y]},
x ∈ [α_B, α_A], y ∈ [β_A, β_B]. Rank:
* world 1 by lex(ν₁(R1\S), ν′₁(R2\T));
* world 2 by lex(ν₂(S), ν′₂(T)).

Here ν₁ = (1−r)μ, ν₂ = rμ on R1 and ν′₁ = (1−r)μ, ν′₂ = rμ on R2. Then (G), (IB), (LA), (C)
hold and U = {all D_{[x,y]}}: a 2-parameter family containing the nested pair A, B. Every
incoherent model is dominated. But **no selection satisfies (S)**.

*Proof.*
* U: if S is not Neyman–Pearson-optimal for (max ν₁, min ν₂), replacing S by a better S′
  dominates. If S is NP-optimal, any dominator has the same primaries, hence (no flats, since
  r/(1−r) is strictly increasing) the same S; then T must be NP-optimal. NP-optimal sets are
  initial r-segments. (C): equal values force the same (S, T).
* (S) fails: by Fact 0(b), any selection is onto U. If y(p) < β_B, then p is improvable at
  world 1 (Z = (S(p), R2)), and f₁ is strictly monotone in x. If y(p) > β_A, then p is
  improvable at world 2. Theorem 7 puts every x(p) in a countable set, but onto-ness needs all
  of [α_B, α_A]. ∎

*Reading.* Lexicographic independence genuinely enlarges undominated sets beyond anything
additive (Theorem N). The enlargement comes from *decoupling*: a region infinitesimal at both
worlds, cut independently of a region real at both. It is always a continuum of primary levels,
so (S) kills it. Theorem 6 shows that without decoupling at one world the additive picture
returns.

## 6. Status of Q1/Q2 and what remains

| Claim | Status |
|---|---|
| Per-model Q1 (Lemma 2) | PROVED, trivial |
| Extension-form Q1 is false; not necessary for additivity of the family (Prop 4) | PROVED |
| U_L = C_L ⊆ coherent under (LA),(S),(C) (Lemma 1) | PROVED |
| Uniqueness of interior Bayes models for additive (S),(C) systems (Lemma U) | PROVED |
| No interior-nested pair in U_add, any n (Theorem N) | PROVED |
| n = 2: additive U is a continuous monotone path; Q1 ⇔ No-Nesting (Prop P, Theorem R) | PROVED |
| No-Nesting for countable unanimity, any n (Prop 5) | PROVED |
| No-Nesting for one-lex + one-additive world, n = 2 (Theorem 6) | PROVED |
| Countability of primary levels at lex worlds (Theorem 7) | PROVED |
| Decoupled lex: nested U, (S) fails (Prop 8) | PROVED |
| CONJECTURE 1: in n = 2 every (G),(IB),(LA),(S),(C) system on a decomposable domain has no strictly nested pair (so Q1 holds in n = 2) | CONJECTURE |
| CONJECTURE 1′: the same for two-level lex at both worlds | CONJECTURE |
| Q1 for n ≥ 3 | OPEN |

Evidence for 1′: the only mechanism found for nesting is decoupling, and it fails (S). Without
decoupling, the ℝ(ε)-valued "nonstandard Bayes" threshold argument of Theorem 6 should run.
Not verified for both worlds lexicographic.

**What a Q2 counterexample must look like.**
* n = 2: both worlds genuinely non-additive, i.e. not countable-unanimity, not one-lex +
  additive, not decoupled-lex.
* Any n: an interior-nested pair in U_L suffices (Theorem N).
* Remaining candidates: ultrafilter or KPS-type complete orders (IRWAS, BA §3), with tuple or
  sample rankings excluded by BA thm:finite-sample; uncountable unanimity; incomplete
  non-unanimity relations; lex at both worlds with coupled tie regions.

**Facts in the brief, checked here.**
* "Equivalently, every selected model, mod ties": yes (Lemma 1).
* The trap: yes on decomposable domains (Lemma 3).
* "Lexicographic refinements break closed sections at primary ties": necessary at improvable
  points; avoidable only with countably many levels (Theorem 7).
* I did not verify the claim that non-additive (IB) relations are incomplete or
  non-Archimedean. Villegas: a complete, monotonely continuous, atomless qualitative
  probability is representable.
