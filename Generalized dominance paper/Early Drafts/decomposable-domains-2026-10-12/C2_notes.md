# C2 (round 15). The leading-density theorem (LD) is false: comonotone credal sets on an edge

15 Oct 2026, BRIEF14 (question C2). Labels: **PROVED** (full proof here), **CHECKED** (proof sketched or read off a
cited proof), **CONJECTURE**, **NUMERICS** (scripts in `c2py/ld_*.py`, run with `python3 -I`; no proof depends on
them). No assumption is added. Notation as in the write-up, §8.5 "Notation": P_i, E_i(X) = X △ P_i, M (mixed part of
U), N_+ (nonnegative part), R_ij = {h ∈ U : h_i h_j < 0}, edge test models X^{ij}_A, c_p := E_i(C_p) for p ∈ e_ij;
for n = 3 the link class Q_i = R_ij ∩ R_ik (B1 notes). Leading density as in B1 §2: a positive integrable ρ on
S ⊆ M is *leading for world i on S* if ρ(E_iZ ∖ E_iY) > ρ(E_iY ∖ E_iZ) ⇒ Y ⪯_i Z for regular Y, Z with Y △ Z ⊆ S.

(The round-10 note that previously occupied this file, "C2: a faithful discretisation of CF(T1)…", is kept
verbatim at the end, after the line "ARCHIVE". Its scripts in `c2py/` are untouched; the new scripts are `ld_*`.)

---

## 0. Outcome

**(LD) is false.** It fails in a full ranking on M_U that satisfies every axiom, with closed sections for every
evaluable model:

- **Theorem C2.1 (PROVED; counterexample).** n = 2, any K′ = [α′, β′] ⊆ (0,1). World 2 additive (density 1 w.r.t.
  μ); world 1 the Pareto (unanimity) order of two densities (1 + x)μ and (1 + 3x²)μ, where x is the chain coordinate
  of the coherent path C_s = D_{[α′s, β′+(1−β′)s]}; selection p ↦ C_{p_2}. Strict (G), (IB), (LA), (S) with closed
  sections for **every** model, competitiveness, and (C) all hold; C_L = {C_s}; every interior C_s is covered
  ((LF) on M_U). World 1 has **no nonzero leading density on R_12 = M**, and no nonzero leading charge either.
  The same holds for every comonotone family of members at either world, both worlds incomplete included.
- **What closed choice + competitiveness force on an edge (Theorem C2.3, PROVED, any n ≥ 2, any K′).** If world i's
  edge comparisons are the unanimity order of a family 𝒜 of densities on R_ij and world j's are that of a family ℬ,
  then every edge-selected error set is a common sublevel set of all ratios ρ_a/ρ_b, the edge selection sweeps
  every level band, and hence **all ratios ρ_a/ρ_b are a.e. comonotone on R_ij**. A leading density exists iff 𝒜 is
  a single ray. So the answer to the brief's "head-on" question is **no**: competitiveness and closed choice force
  comonotonicity of the edge credal set; they give a leading member only when the set is a single ray. In two worlds comonotonicity is also sufficient
  (Theorem C2.1 is the general form).

**Consequences for T1.**
- The route "(LD) + B1.3 + M0closed ⇒ T1 not coverable" is unavailable as stated. Any proof of (LD) for n = 3 must
  use the third world through the link class. The abstract edge inputs (strict (G), (IB), (K), closed sections at
  edge test models; Prop. Q35, S21, B3.3) cannot prove it, because the system of C2.1 satisfies all of them
  (Corollary C2.5).
- **Three worlds: link rigidity (Proposition C2.6, PROVED).** Let worlds j, k be additive with densities, and let world
  i's comparisons on R_ij and on R_ik be density unanimities. Suppose the two edge chain coordinates ρ_j/ρ_a and
  ρ_k/ρ_a have a jointly non-degenerate law on some part of the link class Q_i (the law is equivalent to Lebesgue
  measure on a connected open set). Then the members are proportional wherever those coordinates range, so world i
  has a leading density there. With linear or normalised-box neighbours (and one member of the same type) this
  is all of M (Corollary C2.7). So in three worlds the two-world mechanism needs *aligned* pricing of the link
  class.
- The refuting worlds are (CP-a) and add up, so C2.1 is not a step towards a cover of T1: M0closed already
  excludes systems in which all worlds add up. What C2.1 reopens is the escape of Corollary B1.4 in principle. A
  world whose edge orders are incomplete has no leading density, and then B1.3 does not generate its interior
  comparisons. In three worlds this escape now needs aligned link pricing (C2.6). The three-world question is
  open: **CONJECTURE C2.C** below.

NUMERICS (`c2py/ld_two_world.py`, output `ld_two_world.out`; 800 x-cells with exact Gaussian angle masses):
- the path is exactly the error sets of D_{[α′s, β′+(1−β′)s]} (0 mismatches);
- competitiveness: 0 failures over 400 random models × 41 indices, and the exact fractional-knapsack worst case is
  ≥ −1·10⁻¹⁶;
- every random model is strictly dominated by some C_s or equal to it (400/400);
- sections are closed intervals (0 violations);
- explicit leading-density violations for ρ ∈ {each member, their mean, a random density};
- the same checks hold for both-worlds-incomplete and for the envy form C2.2;
- negative control: a non-comonotone pair makes competitiveness fail at 19 of 19 tested indices.

---

## 1. The counterexample

**Setting.** n = 2, K′ = [α′, β′] ⊆ (0,1) in the weight t of world 2, U = D_{K′}, M_U. As in write-up §8.5(d):
M = M⁻ ⊔ M⁺, with M⁻ = {g₁ < 0 < g₂} ∩ U, σ(g) = −g₁/(g₂ − g₁) ∈ (0, α′), and M⁺ = {g₁ > 0 > g₂} ∩ U,
τ(g) = g₁/(g₁ − g₂) ∈ (β′, 1). The coherent members of M_U are the D_{[α,β]}, α ≤ α′ ≤ β′ ≤ β, with
E_1(D_{[α,β]}) ∩ M = {σ < α} ∪ {τ ≤ β} (Prop. lattice).

**Chain coordinate.** Put x(g) := σ(g)/α′ on M⁻ and x(g) := (τ(g) − β′)/(1 − β′) on M⁺. Then x : M → (0,1), each
level set {x = s} is a union of two rays, hence null, and s ↦ μ{x < s} is continuous and strictly increasing. For
s ∈ [0,1] put

  C_s := D_{[α′s, β′+(1−β′)s]}, so that c_s := E_1(C_s) ∩ M = {x < s} (mod null), E_2(C_s) ∩ M = {x ≥ s}.

C_s is coherent, regular, and contained in U (its credal set contains K′). C_0 = P_1, C_1 = P_2. For s ∈ (0,1) its
credal set contains K′ in its relative interior, so ∂D_{C_s} ∖ 0 ⊆ U and (LF) holds at C_s with N = U.

**Members.** Fix a positive integrable ρ₀ on U (for instance ρ₀ ≡ 1). Let 𝒜 and ℬ be nonempty families. Each
a ∈ 𝒜 is a pair (F_a, φ_a), and each b ∈ ℬ a pair (G_b, γ_b), where:
- F_a, G_b : (0,1) → (0, ∞) are measurable, with F_a ρ₀ and G_b ρ₀ integrable on M;
- φ_a, γ_b > 0 are integrable on N_+.

Put ν_a := F_a(x)ρ₀ μ on M and φ_a μ on N_+, and ν_b := G_b(x)ρ₀ μ on M and γ_b μ on N_+. Define

  X ⪯_1 Y ⟺ ν_a(E_1X) ≤ ν_a(E_1Y) for all a ∈ 𝒜;  X ⪯_2 Y ⟺ ν_b(E_2X) ≤ ν_b(E_2Y) for all b ∈ ℬ.

Selection: C_p := C_{p₂} for p = (p₁, p₂) ∈ Δ. Hypotheses:
- **(Co)** for all a, b, the ratio r_ab := F_a/G_b is nondecreasing on (0,1);
- **(St)** for some pair (a*, b*), r_{a*b*} is strictly increasing.

**Theorem C2.1 (PROVED).** Under (Co) and (St):
1. both world orders are preorders on M_U with strict (G) and (IB);
2. (S) holds: every C_s with s ∈ (0,1) is competitive on {1,2}, C_0 on {1}, C_1 on {2}, and for every
   X ∈ M_U the sections {p : C_p ⪯_i X} are closed;
3. every X ∈ M_U other than the C_s is strictly dominated by some C_s, and each C_s is undominated with no tie
   partner but itself; hence U_L = C_L = {C_s : s ∈ [0,1]}, and (LA) and (C) hold;
4. each C_s, s ∈ (0,1), is covered ((LF) and C_s ∈ C_L);
5. world 1 has a nonzero leading density on M iff all F_a are proportional to one another; if two members are
   not proportional, it has no nonzero leading charge on M either; and symmetrically for world 2.

In particular 𝒜 = {1 + x, 1 + 3x²}, ℬ = {1}, ρ₀ ≡ 1 (all φ_a = γ_b = 1) refutes (LD). So does
ℬ = {1, 2 − x}, where both worlds lack leading densities.

*Proof.* Write, for a model X, A := E_1X ∩ M and N := N_+ ∖ X. Then E_1X = A ∪ N and E_2X = (M ∖ A) ∪ N, since
both worlds err on unaccepted nonnegative gambles and exactly one world errs at each g ∈ M. Write ν(S) for ν of a
subset S ⊆ M when no confusion arises.

(1) *Preorders, (G), (IB).*
- A unanimity of preorders X ↦ ν(E_iX) is a preorder.
- On M_U the world-i advice at g ∈ U is either correct or an error (no contradictory advice), so "X is at least as
  good as Y at world i a.e." means E_iX ⊆ E_iY a.e. That gives ν(E_iX) ≤ ν(E_iY) for every member. If the
  difference is non-null, every member gives strict inequality, because all densities are > 0 a.e. on U. So
  X ≺_i Y: strict (G).
- ν(E_iX) − ν(E_iY) depends only on the set where X and Y differ, and on their advice there. So every member
  comparison, and hence every finite or infinite conjunction of them, satisfies (IB).

(2) *Competitiveness.*
- C_0 = P_1 has E_1 = ∅, so C_0 ⪯_1 X for all X; likewise C_1 ⪯_2 X.
- Let s ∈ (0,1), c := c_s, and suppose C_s ⋠_2 X. Then for some b, ν_b(M ∖ c) > ν_b(M ∖ A) + ν_b(N) ≥ ν_b(M ∖ A),
  that is, ν_b(A) > ν_b(c).
- Fix any a. By (Co) there is k ≥ 0 with r_ab ≤ k on {x < s} and r_ab ≥ k on {x ≥ s}. Then
  ν_a(A) − ν_a(c) = ∫_{A∖c} r_ab dν_b − ∫_{c∖A} r_ab dν_b ≥ k(ν_b(A ∖ c) − ν_b(c ∖ A)) = k(ν_b(A) − ν_b(c)) ≥ 0,
  so ν_a(E_1X) = ν_a(A) + ν_a(N) ≥ ν_a(c) = ν_a(E_1C_s).
- This holds for every a, so C_s ⪯_1 X.

*Closed sections.*
- s ↦ ν_a(c_s) is continuous and nondecreasing: dominated convergence, and μ{x = s} = 0. So
  {s : C_s ⪯_1 X} = ⋂_a {s : ν_a(c_s) ≤ ν_a(E_1X)} is an intersection of closed initial segments [0, s_a], hence
  closed. Likewise {s : C_s ⪯_2 X} is a closed final segment.
- p ↦ p₂ is continuous, so the sections in p are closed.

(3) *Domination.*
- Let S_1(X) = [0, s₁] and S_2(X) = [s₂, 1] be the sections. They are closed intervals whose union is [0,1], by
  competitiveness, so s₂ ≤ s₁. Every C_s with s ∈ [s₂, s₁] satisfies C_s ⪯_1 X and C_s ⪯_2 X.
- *Ties force equality.* Suppose X is tied with C_s at both worlds. Take (a*, b*) from (St), write r := r_{a*b*},
  and choose k as in (2).
  - The world-2 tie for b* gives ν_{b*}(A) − ν_{b*}(c) = ν_{b*}(N) ≥ 0.
  - Then ν_{a*}(A) − ν_{a*}(c) = ∫_{A∖c}(r − k) dν_{b*} + ∫_{c∖A}(k − r) dν_{b*} + k ν_{b*}(N) ≥ 0.
  - The world-1 tie for a* gives ν_{a*}(A) − ν_{a*}(c) = −ν_{a*}(N) ≤ 0.
  - So N is null and both integrals vanish. Since r is strictly increasing, r − k > 0 on {x > s} and k − r > 0
    on {x < s}. Hence A ∖ c and c ∖ A are null, and X = C_s.
- So every X ∉ {C_s} is weakly dominated by some C_s and not tied with it at some world, i.e. strictly dominated.
- *C_s is undominated.* If Y weakly dominates C_s, then some C_{s′} weakly dominates Y.
  - If s′ < s, then E_2C_{s′} ⊋ E_2C_s with non-null difference, so C_s ≺_2 C_{s′}, a contradiction.
  - If s′ > s, the same argument at world 1 gives a contradiction.
  - So s′ = s, Y is tied with C_s at both worlds, and Y = C_s.
- So U_L = {C_s}, all coherent, C_L = U_L, and (LA) holds. The only model tied with C_s at every world is C_s, so
  (C) holds.

(4) This is the (LF) remark in the setting.

(5) *Leading densities and charges.*
- *Leading density forces proportionality.* Let ρ be a leading density of world 1 on M and a ∈ 𝒜. Suppose
  f := F_aρ₀/ρ is not a.e. constant on M. Choose k, δ > 0 with S₋ := {f < k − δ} and S₊ := {f > k + δ} both
  non-null, and η > 0 with (k − δ)(1 + η) < k + δ. Since ρμ is atomless, pick non-null P ⊆ S₋ and Q ⊆ S₊ with
  ρ(P) = (1 + η)ρ(Q). Then
  ν_a(P) ≤ (k − δ)(1 + η)ρ(Q) < (k + δ)ρ(Q) ≤ ν_a(Q).
  The regular models Y := P_1 △ Q and Z := P_1 △ P have E_1Y = Q and E_1Z = P. ρ strictly favours Y, but
  ν_a(Q) > ν_a(P), so Y ⋠_1 Z, against leadingness. So every F_aρ₀ is proportional to ρ, and all F_a are
  proportional to one another.
- *Proportional members give a leading density.* If all F_a are proportional, world 1 is additive on M with
  density F_aρ₀, which is then leading.
- *No leading charge.* Let F_a, F_{a′} be non-proportional, and suppose π is a nonzero leading charge of world 1 on
  M.
  - By Theorem S21 (n = 2: strict (G), (IB), (S)), π(D) > 0 for every non-null D ⊆ M.
  - With f := F_a/F_{a′} not a.e. constant, take S₋, S₊ as above. By Lyapunov, choose non-null P ⊆ S₋, Q ⊆ S₊ with
    ν_a(P) = ν_a(Q); then ν_{a′}(P) > ν_{a′}(Q).
  - For every e ⊆ P with 0 < ν_a(e) and ν_{a′}(e) < ν_{a′}(P) − ν_{a′}(Q), put P_e := P ∖ e. Then
    ν_a(P_e) < ν_a(Q) and ν_{a′}(P_e) > ν_{a′}(Q). So the error sets Q and P_e are incomparable at world 1.
  - Both properties of a leading charge then give π(P_e) = π(Q).
  - Taking e ⊊ e′ (both admissible, with e′ ∖ e non-null) gives π(e′ ∖ e) = π(P_e) − π(P_{e′}) = 0. This
    contradicts strict positivity.
- World 2 is the mirror. ∎

*Remarks.*
- (i) The proof never uses that 𝒜 or ℬ is finite. Any family of comonotone members works, for instance a whole
  interval of exponents {1 + x^θ : θ ∈ [1,3]}.
- (ii) The system is (CP-a) at both worlds, with countably additive members. So each world adds up (every member
  endorses every comparison), is monotonely continuous (Corollary MC(a)), and has nested C_L (Theorem MC).
  Nothing here contradicts the corpus. Theorem S22 needs a leading charge, which this system does not have.
  Corollary CPaU concerns T1 with n = 3.
- (iii) In the corpus's terminology, world 1 is "incomplete in an essential way (unanimity over several
  non-proportional densities)", which is the first alternative of B1 §3. B1 §3 left open whether this can occur
  inside a full system. C2.1 shows that it can, in two worlds.

**C2.2 (the envy form; PROVED as a special case).** Take world 2 additive with density ρ₂, and world 1 the
unanimity of ρ_a and ρ_b := ρ_a + λρ₂ on M (λ > 0), with ρ_a/ρ₂ = F(x) strictly increasing.
- Then r_b = F + λ, so (Co) and (St) hold.
- On M the world-1 and world-2 error sets are complementary. So ν_b(E_1X ∩ M) = ν_a(E_1X ∩ M) − λν₂(E_2X ∩ M)
  + λν₂(M).
- So the second member is "own loss minus λ times the other world's loss": world 1 accepts an exchange only if it
  improves its own loss both outright and net of world 2's loss.
- NUMERICS: `ld_two_world.py`, system C2.2.

---

## 2. The incomplete case head-on: what an edge forces

Standing hypotheses for this section: n ≥ 2, M_U for any credal set K′ ⊆ Δ°, a ranking with strict (G) at worlds i
and j, (IB), and (S). Fix an edge e_ij. (IB) gives the error-set normal form, so for regular Y, Z with
Y △ Z ⊆ R_ij the comparison Y ⪯_i Z depends only on (E_iY ∩ R_ij, E_iZ ∩ R_ij), and similarly at world j. By
Lemma Q34, c_p ⊆ R_ij and E_jC_p ∩ R_ij = R_ij ∖ c_p for p ∈ e_ij. Also c_{e_i} = ∅ and c_{e_j} = R_ij.

Say that **world i is a density unanimity on R_ij** if there is a family 𝒜 of densities ρ_a > 0 a.e. on R_ij,
integrable, such that for A, B ⊆ R_ij: A ≤_i B ⟺ ∫_A ρ_a ≤ ∫_B ρ_a for all a. Define the same for world j and a
family ℬ, comparing complements: R_ij ∖ A ≤_j R_ij ∖ B ⟺ ∫_{R∖A} ρ_b ≤ ∫_{R∖B} ρ_b for all b. Additive edge worlds
are the singleton case. Write R := R_ij and r_ab := ρ_a/ρ_b.

**Theorem C2.3 (edge comonotonicity; PROVED).** Let worlds i and j be density unanimities on R_ij, with families 𝒜
and ℬ.

- (a) **Separation.** For every p ∈ e_ij and all a, b: ess sup_{c_p} r_ab ≤ ess inf_{R∖c_p} r_ab.
- (b) **Sweep.** For all a, b and λ₁ < λ₂ with {r_ab = λ₁} and {r_ab = λ₂} null, some p ∈ e_ij has
  {r_ab < λ₁} ⊆ c_p ⊆ {r_ab ≤ λ₂} (mod null).
- (c) **Comonotonicity.** For all a, b, a′, b′, the functions r_ab and r_{a′b′} are a.e. comonotone on R: the set
  of pairs (h, h′) ∈ R × R with (r_ab(h) − r_ab(h′))(r_{a′b′}(h) − r_{a′b′}(h′)) < 0 is μ⊗μ-null.
- (d) World i has a nonzero leading density on R_ij iff all members of 𝒜 are proportional on R_ij. So "at least
  one density of the edge credal set is leading" holds iff the edge credal set is a single ray.

*Proof.*

(a) Vertices are trivial (c = ∅ or c = R). Let p lie in the open edge, put c := c_p, and suppose (a) fails.
- Choose k > δ > 0 and non-null P ⊆ c ∩ {r_ab > k + δ} and Q ⊆ (R ∖ c) ∩ {r_ab < k − δ}.
- Fix η > 0 with (k − δ)(1 + η) < k + δ. Shrinking P (Lyapunov for ρ_b μ), arrange ρ_b(Q) = (1 + η)ρ_b(P).
- Put A := (c ∖ P) ∪ Q and X := X^{ij}_A.
- World j: ρ_b(R ∖ c) − ρ_b(R ∖ A) = ρ_b(Q) − ρ_b(P) > 0, so C_p ⋠_j X.
- World i: ρ_a(A) − ρ_a(c) = ρ_a(Q) − ρ_a(P) ≤ ((k − δ)(1 + η) − (k + δ))ρ_b(P) < 0, so C_p ⋠_i X.
- This contradicts competitiveness of C_p on {i, j}.

(b) Put L := {r < λ₁} and H := {r > λ₂}, with r := r_ab. Let P₁ := {p ∈ e_ij : L ⊆ c_p} and
P₂ := {p ∈ e_ij : c_p ∩ H null}.
- *Cover.* If p ∉ P₁, then L ∖ c_p is non-null, so ess inf_{R∖c_p} r < λ₁. By (a), ess sup_{c_p} r < λ₁ < λ₂, so
  p ∈ P₂. Hence P₁ ∪ P₂ = e_ij.
- *Non-empty.* e_i ∈ P₂ and e_j ∈ P₁.
- Suppose P₁ ∩ P₂ = ∅. We show that both sets are closed.
  - *P₂ = e_ij ∩ S_i(X^{ij}_{R∖H}).* If p ∈ P₂, then c_p ⊆ R ∖ H, so C_p ⪯_i X^{ij}_{R∖H} by (G). If p ∉ P₂,
    then p ∈ P₁ and c_p ∩ H is non-null. So ess sup_{c_p} r > λ₂, and by (a), ess inf_{R∖c_p} r > λ₂. Since
    {r = λ₂} is null, R ∖ c_p ⊆ H, i.e. c_p ⊋ R ∖ H with non-null difference. Strict (G) gives
    X^{ij}_{R∖H} ≺_i C_p.
  - *P₁ = e_ij ∩ S_j(X^{ij}_L),* by the mirror argument at world j, using that {r = λ₁} is null.
- Sections are closed, so P₁ and P₂ are disjoint, closed, nonempty and cover the connected e_ij, which is
  impossible. Any p ∈ P₁ ∩ P₂ satisfies (b).

(c) Suppose not. Then there are rationals λ₁ < λ₂ and μ₁ < μ₂, avoiding the countably many non-null level sets,
and non-null P ⊆ {r < λ₁, r′ > μ₂} and Q ⊆ {r > λ₂, r′ < μ₁}, where r := r_ab and r′ := r_{a′b′}.
- By (b) take p with P ⊆ c_p and Q ⊆ R ∖ c_p.
- (a) for r′ gives μ₂ ≤ ess sup_P r′ ≤ ess inf_Q r′ ≤ μ₁, a contradiction.

(d) Reduce to edge test models by the normal form. Then argue as in C2.1(5): a leading ρ must be proportional to
every member, and a single ray is additive. ∎

*Uses:*
- strict (G) at i and j;
- the normal form;
- competitiveness at open-edge indices;
- C_{e_i} = P_i and C_{e_j} = P_j;
- closed sections at the edge test models.

*Not used:* (C), (LA), the third world, nestedness, coherence, completeness.

**Corollary C2.4 (two worlds: an exact characterisation along coherent paths; PROVED).** For n = 2 on M_U, with
density-unanimity worlds and every axiom, all ratios r_ab are pairwise comonotone on M (C2.3(c)). Conversely, if
ρ_a = F_a(x)ρ₀ and ρ_b = G_b(x)ρ₀ along the chain coordinate of any comonotone coherent path, with (Co) and (St),
the system has every axiom (C2.1). In both directions, world 1 has a leading density iff 𝒜 is a ray.

**Corollary C2.5 (edge inputs cannot prove (LD); PROVED).** No argument that uses only the restriction of a ranking
to one edge proves (LD) or its three-world case. Such arguments use:
- worlds i, j;
- edge test models;
- strict (G) and the normal form;
- competitiveness at edge indices;
- (K) and closed sections at edge test models.

Proposition Q35, Theorem S21, Lemma B3.3 and Theorem B3.5 are of this kind. Indeed, the system of C2.1 is such an
edge system (R_12 = M), with every one of these properties and no leading density. Transport it to any R_ij by a
measure-algebra isomorphism that carries the chain to a chain. *Hence any proof of (LD) for n = 3 must use the
link class Q_i or the third world.*

---

## 3. Three worlds: link rigidity

Let n = 3 and fix world 1. Assume:
- world 1 is a density unanimity on R_12 and on R_13, with the same family 𝒜;
- worlds 2 and 3 are additive on R_12 and R_13, with densities ρ₂ and ρ₃.

Fix a reference a ∈ 𝒜, and put A := ρ₂/ρ_a, B := ρ₃/ρ_a and ψ_b := ρ_b/ρ_a. These are the two edge chain coordinates
seen from world 1: A on R_12, B on R_13.

**Proposition C2.6 (link rigidity; PROVED).** Assume strict (G), (IB) and (S). Let W ⊆ Q_1 be non-null, and suppose
the image of μ|_W under (A, B) is equivalent to Lebesgue measure on a connected open set D ⊆ (0, ∞)². Let I_A and
I_B be the projections of D (open intervals). Then for every b ∈ 𝒜 there is κ_b > 0 with ψ_b = κ_b a.e. on W, on
{h ∈ R_12 : A(h) ∈ I_A}, and on {h ∈ R_13 : B(h) ∈ I_B}. In particular, if I_A contains the essential range of A on
R_12 and I_B that of B on R_13, then every ρ_b is proportional to ρ_a on M, and ρ_a is a leading density of world
1 on both edge regions.

*Proof.*
- *Step 1: ψ_b is a function of A on W.* By C2.3(c) on R_12 (ℬ = {ρ₂}), X := ρ_a/ρ₂ = 1/A and Y := ρ_b/ρ₂ = ψ_b/A
  are comonotone. The essential support of the law of (X, Y) is then a chain in the product order. So it lies in
  a maximal monotone relation whose vertical sections are the intervals [F(x−), F(x+)], for a nondecreasing F,
  and Y ∈ [F(X−), F(X+)] a.e. The law of X on W has no atoms, and F has countably many jumps, so ψ_b = A·F(1/A)
  =: Φ₁(A) a.e. on W.
- *Step 2: ψ_b is a function of B on W.* Likewise, from R_13, ψ_b = Φ₂(B) a.e. on W.
- *Step 3: ψ_b is constant on W.* Φ₁(a) = Φ₂(b) for Lebesgue-a.e. (a, b) ∈ D. On each open rectangle I × J ⊆ D,
  Fubini makes Φ₁ a.e. constant on I. Overlapping rectangles share the constant, and D is connected, so Φ₁ ≡ κ a.e.
  on I_A, and likewise Φ₂ ≡ κ a.e. on I_B.
- *Step 4: extension.* F(y) = κy for a.e. y ∈ 1/I_A. F is monotone, so this holds for every interior y,
  F(y±) = κy, and Y = κX wherever A ∈ I_A, atoms included. The same holds on R_13.
- κ > 0 because the densities are positive. ∎

**Corollary C2.7 (PROVED).** Suppose that on each sign class the densities ρ_a, ρ₂, ρ₃ are positive constants times
|h₁|, |h₂|, |h₃| respectively. This covers the linear densities and the normalised-box densities of *Coverage
after NA* (4), on M_U. Then every density-unanimity world 1 with reference member ρ_a is additive on M.
- *Proof.* Take W := (−,+,+) ∩ U ⊆ Q_1. There (A, B) = (c₂h₂/|h₁|, c₃h₃/|h₁|), whose image is the open
  connected set {(A, B) ∈ (0,∞)² : k₂A/c₂ + k₃B/c₃ > k₁ for all k ∈ K′}. The map is a submersion and μ has a
  density, so the image law is equivalent to Lebesgue measure there. Both projections are (0, ∞). ∎
- *For T1, under (H_U) (PROVED at the status of Theorem M0closed(b)):* if worlds 2 and 3 are additive with
  densities and world 1's edge orders satisfy the hypotheses of C2.6 with full projections, then ρ_a is leading on
  R_12 and R_13. So world 1 adds up (B1.3), the ranking is in (M0), and T1 is not covered (Theorem M0closed(b)).
  This is a new excluded class: world 1 may be arbitrary, and non-additive, on interior comparisons.

**Remark C2.8 (why the two-world mechanism stalls in three worlds; PROVED identity, consequence from C2.3).** The
mechanism of C2.1/C2.2 extends verbatim to any n at the level of Bayes sets. Let u_a = (ρ_aσ₁, ρ₂σ₂, ρ₃σ₃) be the
chart vector of the additive system (ρ_a, ρ₂, ρ₃), and for s₁₁, c > 0 and s₁₂, s₁₃ ≥ 0 put

  s₁₁ρ_b := cρ_a − s₁₂σ₁σ₂ρ₂ − s₁₃σ₁σ₃ρ₃ (positive if the s₁ⱼ are small and the ratios bounded).

Then (Tp)·u_b = c p·u_a pointwise, with Tp := (s₁₁p₁, s₁₂p₁ + cp₂, s₁₃p₁ + cp₃) ∈ Δ (up to scale). So
B_b(Tp) = B_a(p) for every p, and every interior base-Bayes model is Bayes for both members: it is competitive on
{1,2,3} in the unanimity system. On M this member is "own loss minus Σⱼ s₁ⱼ × world j's loss", up to constants.
On the edges, however, T moves e_12 off e_12 when s₁₃ > 0, and e_13 off e_13 when s₁₂ > 0. Then the base edge
models are not edge-competitive, and C2.3 shows that no other edge selection is, unless the link pricing is
aligned. Concretely:
- the e_12 condition requires ρ₃/ρ₂ to be a function of ρ_a/ρ₂ on R_12 (sign-adjusted between Q_1 and Q_2), or
  s₁₃ = 0;
- the e_13 condition is the mirror.

With s₁₂ = s₁₃ = 0 the members are proportional.

**CONJECTURE C2.C ((LD) in three worlds, density-unanimity class).** Let n = 3 on M_U (any K′), with every axiom and
closed sections for every model. If world i is a density unanimity on R_ij and on R_ik, then its members are
proportional on R_ij ∪ R_ik.
- *Evidence:* C2.6 and C2.7 (the conjecture holds whenever the link class is priced non-degenerately, in particular
  for linear and box neighbours) and Remark C2.8.
- *A counterexample would need:*
  - aligned link pricing: (ρ_j/ρ_a, ρ_k/ρ_a) degenerate on Q_i;
  - interior selected models that are Bayes for every member at once (the KKM/Pareto argument: every undominated
    model is tied with a selected one, and a competitive selected model is weakly Pareto-minimal, hence Bayes, for
    each member);
  - coherence of all these Bayes sets.
- None of this has been attempted beyond the obstructions recorded here.
- *What it would not settle:* worlds without a leading density whose edge orders are not density unanimities
  (band-and-translates, lexicographic-with-charge, non-AR complete). For those, (LD) in three worlds stays open, as
  in B1 §3 and B3.C.

---

## 4. Status and reading for the programme

| Item | Statement | Label |
|---|---|---|
| (LD), as posed (any n ≥ 2, any target) | false | **PROVED** (C2.1) |
| C2.1 | two-world comonotone-unanimity systems: every axiom, closed sections for every model, no leading density or charge | PROVED; NUMERICS |
| C2.2 | envy form (own loss and own-minus-other loss) | PROVED |
| C2.3 | on any edge, competitiveness + closed choice ⇒ the edge credal sets are comonotone (separation, sweep); leading density ⇔ ray | PROVED |
| C2.4 | two worlds: comonotonicity is also sufficient (along coherent paths) | PROVED |
| C2.5 | edge-only inputs cannot prove (LD) | PROVED |
| C2.6, C2.7 | three worlds: link rigidity; (LD) holds for density unanimities with non-degenerate link pricing (linear and box neighbours); new excluded class for T1 | PROVED |
| C2.8 | the envy mechanism lifts to interior Bayes sets in any n, and stalls on edges without aligned link pricing | PROVED (identity) + C2.3 |
| C2.C | (LD) for density unanimities in three worlds | CONJECTURE |

**Reading.**
- The decisive answer to BRIEF14's question is negative: (LD) fails in a full system. The failure is not a
  pathology: it is the generic incomplete edge order permitted by closed choice, a comonotone credal set.
- The positive route that Corollary B1.4 left open, "a world with no leading density on an edge region", is
  realisable in two worlds by worlds that add up. For T1 those are already excluded by M0closed.
- The live three-world question splits in two:
  - (i) density-unanimity edges: governed by the link class (C2.6; Conjecture C2.C), and closed when the link is
    priced non-degenerately;
  - (ii) edge orders that are not density unanimities: unchanged from B1 §3, B3.C and the two-world core (R1),
    (R2).
- The suggested new aim, per the nearby-result principle: prove C2.C, or find aligned link pricing with coherent
  doubly-Bayes interiors. The former closes the density-unanimity escape for T1. The latter is the only remaining
  way to realise B1.4's escape with countably additive edge structure.

## 5. Files (`c2py/`)

- `ld_two_world.py` (+ `ld_two_world.out`): NUMERICS for C2.1 (two variants), C2.2 and a negative control.
- `_round10_C2_notes_backup.md`: a byte copy of the round-10 note, also reproduced below.

---
---

# ARCHIVE: round-10 note C2 (14 Oct 2026), kept verbatim

# C2: a faithful discretisation of CF(T1), and the impossibility it led to (14 Oct 2026)

Construction side, round 10. Scripts and outputs: `c2py/`. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
Terminology as in TERMFIX_RULES (decomposable domain, advice range, U-domain). Notation as in the write-up
(*The Contamination Triangle*, §§2–5): T1 = (1−ε)u + εΔ, κ = (1+2ε)/(1−ε), p* = u (WLOG, Prop. reduction (d)),
facet data x ∈ {x₊, x₋}, x + 1/x = κ + 1, PC vectors c_k(h) (§4.6), h_k(τ) = (1−τ)r₀ + τr₁ on F_k.
For a world b with failing pair (a,b) and third index c: crossings w′ ∈ F_a, w ∈ F_c, chord λ_b = line(u,e_b),
tangent lines ℓ′ = w′^⊥, ℓ = w^⊥ from e_b, tangent wedge W_b := {m ∈ Δ : m·w′ ≥ 0, m·w ≥ 0}.

---

## 0. Outcome

**(b), but not by a finite certificate alone.** The discretisation did not produce a solution. Its per-prior
part pointed to one new constraint, and that constraint, pushed through the continuum, gives an impossibility.

**Theorem 5.1 (PROVED here, conditional on the cited inputs listed in §5.3; single author, not yet refereed).**
For ε ∈ {1/20, 1/10, 1/5, 3/10, 1/2, 3/5, 9/10}, and for every ε ∈ (0,1) outside a finite set (possibly empty), T1
has no additive cover with integral penalties on any decomposable domain with (LF). Hence CF(T1) has no solution
that comes from a cover. Every solution comes from a cover at the status of CCIBU, so at that status CF(T1) has no
solution. This settles Conjecture N21/N28 at these statuses.

The chain has six steps.
1. **Lemma 3.1 (no straddling on the positive side of a chord), new.** If c_k(h)·q > 0 for an exact facet gamble h,
   then K_q strictly accepts h or −h, unless K_q is a single point on h^⊥.
2. **Uniformity (Cor. 3.2).** Near a vertex, a non-precise K_q has half-plane charts for every facet gamble of the
   two facets crossing b. There are no cuts at non-precise priors.
3. **Forced precise caps (Thm 4.1).** The failing box then forces K_q to be a singleton on a relative neighbourhood
   of the failing edge near each vertex. So the sector caps of the referee's C1 are not merely allowed, they are
   *required*. By R4 Prop. D the cap map is diagonal-projective, σ_b(q) = ν(W_b q).
4. **Gluing (Lemma 4.2).** At every boundary point of the cap near e_b, σ_b(q) lies on both pencil lines L^a(q) and
   L^c(q), which the PC data fix. Infinitely many such points accumulate at e_b. So two explicit conics in q share
   a component (Bezout).
5. **Pinning (Prop. 4.3, exact algebra).** Only two W_b allow a shared component. One of them violates (R1) next to
   the edge. What remains is **W_b = κ off b and 1 at b**, with the cap bounded by the line through e_b of slope 1/x.
   In blow-up coordinates the apexes of all cut facet gambles lie on that line.
6. **Two caps cannot coexist (Prop. 5.2).** A gamble whose line meets the images of two caps would need its d-line
   to be both (W₁g)^⊥ and (W₂g)^⊥. Since W₁ = diag(1,κ,κ) and W₂ = diag(κ,1,κ) are not proportional, this is
   impossible.

**Finite core and continuum inputs** (as the brief asked, §5.4). The finite core is:
- the two box witnesses A, B and one combination A + λB at each vertex;
- one prior on each crossing chord;
- one double-cap gamble g.

The continuum inputs are:
- (PC) cluster limits at exact facet gambles;
- Hausdorff continuity;
- a.e. goodness of gambles;
- Prop. D (precise regions are projective);
- the arc/Bezout argument on infinitely many interface points.

No finite family of gambles and priors that is blind to these can be inconsistent. §2 explains why the plain
discretisation stays feasible.

**Discretisation results (NUMERICS).**
- DCF(G,F) is exactly necessary (Prop. 1.1, PROVED).
- Generic instances are feasible at ε = 0.3 and 0.6.
- DCF+ (adding the facet-pencil constraints) is feasible at ε = 0.3 and 0.6 (δ* = 0.0053, 0.0032; cells and charts re-verified).
  The solutions exploit the finite τ-grid and are wildly discontinuous, so they are artefacts and not constructions.
- The per-prior pencil MILP CHECKS several facts:
  - C1's identity sector, φ_max = 0.125 at ε = 0.3 and 0.025 at ε = 0.6;
  - the referee's N1;
  - the new chord statement (Cor. 3.3): on λ_b, K_q ⊂ W_b and touches both ℓ′ and ℓ. **It does not poke beyond
    them.** This corrects the write-up's §5.3 description.

---

## 1. The discretisation

**Definition 1 (DCF(G,F)).** Fix a finite set of interior priors G ∋ u and a finite family F of mixed gambles. The
unknowns are a cell z(q,g) ∈ {+,0,−} for q ∈ G, g ∈ F. The requirements are as follows.
- **(CH)** For each g, the column z(·,g) is the cell pattern of max{0, c·q, c′·q} for some c, c′ with
  sign c_i = sign g_i = −sign c′_i. Once z is fixed this is an LP in (c,c′). It is homogeneous, so margin 1 is
  exact.
- **(DC)** For each q, put Acc(q) = {g : z = +} ∪ {−g : z = −}. There is a credal set K with P_K > 0 on Acc(q) and
  P_K ≤ 0 on the rejected members of ±F.
- **(TP)** z(u,·) is the pattern of T1.

**Proposition 1.1 (PROVED).**
- (a) (DC) holds iff C(q) := {m ∈ Δ : m·a > 0 ∀a ∈ Acc(q)} ≠ ∅ and C(q) ∩ {m·h ≤ 0} ≠ ∅ for every rejected h.
- (b) Equivalently, Acc(q) satisfies the q-independent Horn clauses "S ⇒ h": no rejected h lies in
  posi(S) + ℝ³_{≥0}, for S ⊆ Acc(q). It also contains no S with 0 ∈ posi(S) + ℝ³_{≥0} (no sure loss). Minimal S have
  |S| ≤ 3 (Carathéodory in ℝ³).
- (c) **Faithfulness.** If CF(T1) has a solution and every g ∈ F is good (its CF chart holds at every q), then DCF(G,F)
  is feasible for every G. A.e. g is good, so for every nominal F₀ and η > 0 there is a feasible F within η of F₀.
  Infeasibility for *all* η-perturbations of F₀ therefore proves that CF(T1) has no solution.

*Proof.*
- (a) Take K = conv of one witness per rejected h. It lies in the open convex set C(q).
- (b) Farkas on cl C(q). Strictness holds because rejected gambles are mixed.
- (c) Restrict K_q and the chart data to G × F. ∎

**Witness form (used in the code).** Each prior gets one witness point per rejection requirement. All witnesses
satisfy every acceptance, with a common margin δ that is maximised. The problem is feasible iff δ* > 0. This form is
exact and imposes no shape on K_q (`dcfplus.py`). The lazy Horn-clause form (`dcf.py`, `horn.py`) is equivalent but
converges slowly: 116 905 clauses with |S| ≤ 2 for 66 gambles; ~1 600 lazily generated clauses after 18 rounds.

**DCF+ (`dcfplus.py`).** This adds per prior the facet-pencil constraints below, for facet gambles h_k(τ) on a τ-grid
refined around the chord root τ*_k(q).
- **(R1)** If c_k(h)·q < 0, some witness has m·h ≤ 0 (writeup Lemma R1, relaxed to ≤).
- **(C)** If c_k(h)·q > 0, all witnesses lie on one closed side of h^⊥ (the weak form of Lemma 3.1).

Every constraint is necessary for a cover with data x. There are three artefacts:
- the vertex margin dv = 10⁻³ (vertex-freeness is an open condition in the continuum);
- the bound |c|, |c′| ≤ 10³;
- the finite τ-grid.

**What a finite system cannot see.** Hausdorff continuity is not encoded: no modulus is known, and imposing one would
be an added assumption. Nor are the limit statements:
- (PC) cluster uniqueness at exact facet gambles, which are a null set;
- Prop. D;
- accumulation at vertices.

§§3–5 show that the obstruction lives exactly there.

## 2. Computations (NUMERICS unless stated)

| run | ε | size | result |
|---|---|---|---|
| lazy Horn DCF (`run2.py`) | 0.3, 0.6 | 60 gambles × 14 priors | every round feasible. Still adding ~100 clauses per round after 13/18 rounds (stopped) |
| witness DCF, no pencil (`run_plus.py … nopencil`) | 0.3 | 36 × 16 | feasible, δ* = 0.0080 |
| DCF+ (`run_plus.py`) | 0.3 | 36 × 16; 6 304 vars, 162 088 rows | feasible, δ* = 0.0053 |
| DCF+ | 0.6 | 36 × 16 | feasible, δ* = 0.0032 (0 cell mismatches, 36/36 charts, 1 188 fine-grid violations: the same artefact) |

Independent check of the ε = 0.3 DCF+ solution (`verify_plus.py`, `verify_plus_e03.out`):
- 0 cell mismatches when P_{K_q}(±g) is recomputed from the witness hulls;
- 36/36 charts realisable from scratch;
- **658 violations of (R1)/(C) on a 2 000-point τ-grid.**

So the solution lives in the gaps of the τ-grid. Its K_q are far from T1 next to u (Hausdorff distance up to 1.1 on
the ring of radius 0.04) and have no continuity. **Reading:** finite unstructured systems are feasible, and their
"solutions" carry no structure that could become an exact family. This is the expected failure mode.

**Per-prior pencil MILP (`pencil.py`, `pencil_tests.py`, CHECKED; `pencil_tests_eps03.out`).** For a single prior, is
there a vertex-free K satisfying (R1) and (C) for all three facets?
- On λ_b at t ∈ {.02, .1, .3, .6, .9}:
  - an admissible K exists;
  - none pokes beyond ℓ′ or ℓ by 10⁻³t (infeasible);
  - no precise K exists.
- On arcs around e_b (ρ = .05, .01):
  - precise K exists only for φ < ½, on the failing side (the referee's N1);
  - the identity is admissible exactly for φ ≤ 0.125 (C1: 0.127).

(The first run of this script had a big-M sign bug and a vertex-tolerance problem; both are fixed. The outputs
quoted are from the corrected code.)

## 3. No straddling on the positive side of a chord

Standing hypotheses for §§3–5: a strictly guiding additive ranking with integral penalties covers T1 on a
decomposable domain with (LF), and K_q are its interior Bayes credal sets. So (Cor. TSalways):
- (TS), (PC) and (NS) hold, with x ∈ {x₊, x₋};
- K_q → {e_b} at the vertices;
- edge confinement holds;
- the charts are those of CF(T1) for a.e. g, at every q (Prop. CF ⇒).

Nothing else is assumed.

**Lemma 3.1 (PROVED).** Let h ∈ relint F_k and q ∈ int Δ with c_k(h)·q > 0. Then P(q,h) > 0, or P(q,−h) > 0, or K_q
is a singleton contained in h^⊥.

*Proof.*
1. **The CF cells.** For good g, the cell {c·q > 0} misses the silence wedge {c ≤ 0, c′ ≤ 0}. So every q with
   c(g)·q > 0 lies in A(g) ∪ A(−g) ∪ {c = c′ > 0}. On the d-ray, P(q,±g) = 0 by continuity, since q lies in the
   closure of both open cells.
2. **Straddling gambles near h.** Suppose the conclusion fails. Then K_q is not a singleton and meets both closed
   sides of h^⊥. The set of g with min_K m·g < 0 < max_K m·g is open. It has points arbitrarily close to h:
   - h itself, if K_q straddles strictly;
   - h ∓ t𝟙, if K_q touches h^⊥ from one side;
   - h + tn, with n separating two points of K_q, if K_q ⊂ h^⊥.
3. **The chart of such a g.** For a good g in that set, P(q,g) < 0 and P(q,−g) < 0. By step 1, c(g)·q ≤ 0.
4. **The PC limit.** Take good g_m → h in the set. By (PC) (Thm TS, every cluster line of h is the PC line with
   its positive side), c(g_m)/|c(g_m)| → c_k(h)/|c_k(h)|. Hence c(g_m)·q > 0 for large m, a contradiction. ∎

Fix q and a facet k. Put χ_q(τ) := c_k(h_k(τ))·q. It is affine in τ, with root τ*_k(q) (which exists unless q = u).
Put I⁺ := {χ_q > 0} ∩ (0,1), Φ(τ) := P(q,h(τ)) and Ψ(τ) := P(q,−h(τ)).

**Corollary 3.2 (uniformity; PROVED).** If K_q is not a singleton, then either Φ > 0 on all of I⁺ or Ψ > 0 on all
of I⁺.

*Proof.* {Φ > 0} and {Ψ > 0} are disjoint (Φ + Ψ ≤ 0) and open, and by Lemma 3.1 they cover the interval I⁺. ∎

Near e_b the first alternative holds, for k ∈ {a,c}. Some τ₁ has h(τ₁)_b > 0. Then:
- χ_q(τ₁) → λ_{bk} h(τ₁)_b > 0 (crossing rows, Prop. boxbridge (a));
- Φ_q(τ₁) → h(τ₁)_b > 0 (K_q → {e_b}).

Hence, near e_b:
- **a non-precise prior is never cut by a facet gamble of F_a or F_c;**
- **K_q touches the pencil line L^k(q) := {m : m·H_k(q) = 0}**, where H_k(q) := (c_k(r₁)·q) r₀ − (c_k(r₀)·q) r₁
  ∝ h_k(τ*_k(q)). Indeed Φ > 0 on I⁺, and Φ ≤ 0 on I⁻ by N21.1′, so Φ(τ*) = 0.

**Corollary 3.3 (chord; PROVED).** For q ∈ λ_b ∩ int Δ, q ≠ u: K_q ⊂ W_b, P(q,w′) = P(q,w) = 0, and K_q meets ℓ′
and ℓ at points other than e_b.

*Proof.*
1. On λ_b, χ for F_a vanishes at τ_b with nonzero slope. A strict straddle of ℓ′ would persist to τ ∈ I⁺ near τ_b,
   which Lemma 3.1 forbids (q ∉ ℓ′'s singleton case, Prop. vertexfree (iv)). So K_q lies on one closed side of ℓ′,
   and likewise of ℓ.
2. N21.1′ gives P(q,w′), P(q,w) ≤ 0.
3. Every other combination of sides puts e_b ∈ K_q, by Fact 4.0, against Prop. vertexfree (i). ∎

This corrects the write-up's §5.3 bullet "poking strictly beyond ℓ … beyond both ℓ and ℓ′ on the chord". On the chord,
K_q touches the tangent lines and stays inside the tangent wedge. It pokes beyond ℓ′ only off the chord, on the
e_a-side (N28 Remark). CHECKED numerically (§2).

## 4. Forced precise caps and their pinning

WLOG x = x₊ (transposition; `pin_caps.py` also runs x₋). The failing pairs are (a,b) = (1,2), (2,3), (3,1).

**Theorem 4.1 (forced caps; PROVED).** For each b there are s₀ > 0 and a connected open O′_b ⊂ int Δ such that:
- O′_b contains a relative neighbourhood of every edge prior q₀(s) = (1−s)e_b + s e_a, for 0 < s < s₀;
- K_q is a singleton for every q ∈ O′_b.

*Proof.*
1. **Witnesses.** For small s there are box witnesses A ∈ relint F_a and B ∈ relint F_c with
   c_a(A)·q₀ > 0 < c_c(B)·q₀ and A_b B_a < |A_a||B_b|. This is the write-up's Prop. T1 computation, valid
   because x² > κ.
2. **A non-precise prior near q₀ would accept both.** The positivities persist near q₀. For a non-precise q close to
   e_b, Cor. 3.2 gives P(q,A) > 0 and P(q,B) > 0, since τ_A ∈ I⁺_a(q) and τ_B ∈ I⁺_c(q).
3. **Contradiction with the edge.** Then P(q, A+λB) > 0, where A + λB < 0 in coordinates a and b. But K_q is close to
   the edge [e_a,e_b] (edge confinement), where m·(A+λB) < 0.
4. **Connectedness.** Let O′_b be the union of these neighbourhoods; it is connected. ∎

Let O_b be the component of int{q : K_q singleton} containing O′_b.
- By R4 Prop. D (CHECKED), σ_b := the point of K_q is constant or σ_b(q) = ν(W_b q) on O_b, with W_b positive
  diagonal.
- A constant map is excluded: it would have to be e_b, against Prop. vertexfree (i).

**Lemma 4.2 (gluing; PROVED).** Every q ∈ ∂O_b ∩ int Δ close to e_b satisfies Q^a(q) = 0 and Q^c(q) = 0, where
Q^k(q) := (W_b q)·H_k(q). Such points exist at every small distance r from e_b, inside the sector between the failing
edge and λ_b.

*Proof.*
1. **Boundary points are limits of non-precise priors.** Otherwise a precise neighbourhood would join O_b.
2. **Touching passes to the limit.** Non-precise priors near e_b touch L^a(q) and L^c(q) (after Cor. 3.2).
   Hausdorff continuity carries the touching points to the singleton σ_b(q), and H_k is continuous.
3. **Arc argument.** The arc of radius r from the failing edge (which is in O′_b) to λ_b (whose points are
   non-precise, Prop. vertexfree (iv)) crosses ∂O_b. ∎

**Proposition 4.3 (pinning; PROVED by exact algebra, CHECKED numerically).** Infinitely many common zeros accumulate at
e_b, so by Bezout the conics {Q^a = 0} and {Q^c = 0} (both through e_b; neither form vanishes identically for any w > 0: if one did, R ≡ 0 and w would lie in the solution set of (I) below, at which both forms are nonzero — `pin_symbolic.out`) share a
component through e_b. With w_b = 1 there are exactly two possibilities.
- **(I) The conics coincide.** Then (w_a, w_b, w_c) = (x₊, 1, 1/x₊).
- **(II) A common line.** Then (w_a, w_b, w_c) = (κ, 1, κ), and the common line through e_b has direction
  d_c/d_a = 1/x₊ (for both data x₊ and x₋, with a the failing index).

Evidence for the classification:
- Gröbner bases over ℚ(x) (`pin_general.py`): (I) is {w_a − x²w_c, w_c(xw_c − 1)}. (II) is the ideal generated by
  (r−1)(rx−1) together with two linear relations; the branch r = 1 forces w = 0.
- Exact sympy solves at ε ∈ {1/20, 1/10, 1/5, 3/10, 1/2, 3/5, 9/10}, all three vertices, x₊ and x₋, confirm this
  (`glue_conics*.out`, `pin_caps_eps0*.out`).
- Multistart numerics find nothing else.

**Excluding (I).** On the failing edge, F := Q^c vanishes identically and ∂F/∂η ≠ 0 with the violating sign
(`edge_check.out`). So every interior point of the cap next to the edge violates (R1) for pencil c. The exact τ-test
in `cap_R1.py` gives 0 admissible directions out of 120, at ρ = 10⁻², 10⁻³ and ε = .3, .6. The blow-up margin is
y_c(x²κ − 1)/x > 0 (`pin_symbolic.out`).

**What (II) gives.**
- (II) satisfies (R1) exactly on the sector up to slope 1/x, and fails beyond it (`cap_R1`: φ_max = 0.25 against the
  prediction 0.2534 at ε = .3; 0.135 against 0.1362 at ε = .6).
- In the blow-up, the apexes of the cut facet gambles of both pencils lie on the cap boundary. This is exact:
  κ(−y_a + κy_c) = (κ/x)(y_c − y_a) ⟺ y_c/y_a = 1/x, and the same for pencil c.

So **the vertex structure of any cover is forced:**
- σ_b = ν(W_b ·), with W_b = κ off b and 1 at b, on a cap bounded near e_b by the line of slope 1/x;
- non-precise K_q touching both pencil lines beyond it;
- inside W_b on λ_b.

## 5. The contradiction

**Proposition 5.2 (PROVED).** Two open precise regions O, O′ with σ = ν(W·) and σ′ = ν(W′·), W and W′ not proportional,
cannot both exist.

*Proof.*
1. **Choose g.** Let I = σ(O) and I′ = σ′(O′). The set of g whose line g^⊥ meets both I and I′ is open and nonempty,
   so it contains good, mixed g with all g_i ≠ 0.
2. **The d-line through O.** On O, A(g) = {(Wg)·q > 0}. The segment S = {(Wg)·q = 0} ∩ O lies in
   cl A(g) ∩ cl A(−g) ⊂ {c = c′ ≥ 0} ⊂ {d·q = 0}. So the d-line of g is {(Wg)·q = 0}, i.e. d ∝ Wg.
3. **The d-line through O′.** Likewise d ∝ W′g.
4. **Conclusion.** Wg ∥ W′g with W′W⁻¹ having distinct diagonal entries forces g onto a coordinate axis. ∎

**Theorem 5.1 (PROVED, at the status of §5.3).** Apply Prop. 5.2 to O₁ and O₂. By Prop. 4.3, W₁ = diag(1,κ,κ) and
W₂ = diag(κ,1,κ), and W₂W₁⁻¹ = diag(κ, 1/κ, 1) has distinct entries since κ > 1.

`two_caps.py`: over 2 000 double-cap gambles, the angle between W₁g and W₂g is ≥ 0.03° (ε = .3) and ≥ 0.12°
(ε = .6). It is nonzero, as it must be.

**5.3 Inputs and their status.**

| input | status |
|---|---|
| Prop. CF (⇒), Prop. necessary, reduction | proved; once refereed with repair |
| Thm TSalways ⇒ (TS), (PC) clusters near Σ, (NS), x ∈ {x±}; Cor. TSalways (c) | one referee |
| crossing rows (Prop. boxbridge (a)); box witnesses (Prop. T1) | refereed |
| N21.1′ (A_τ ⊆ H⁺_τ) | refereed once. Lemma R1 is *not* needed |
| Prop. vertexfree (i), (iv); Fact 4.0 | one referee |
| R4 Prop. D (precise regions are diagonal-projective) | CHECKED (local fundamental theorem of projective geometry). **The weakest link.** |
| Lemma 3.1, Cor. 3.2, 3.3, Thm 4.1, Lemma 4.2, Prop. 5.2 | PROVED here, unrefereed |
| Prop. 4.3 | exact algebra: Gröbner over ℚ(x) (generic ε) plus exact solves at 7 values of ε. Uniqueness at finitely many exceptional ε is not checked |

No regularity is assumed: no smoothness, no continuity of chart data, no linear scaling at the vertices. The blow-up
(linear-scaling) computations in §4 are used only as corroboration. Steps 4–5 use the exact conics.

**5.4 The finite core.** At one vertex pair (b, b′) the following finite system is jointly inconsistent:
- box witnesses A, B and A + λB near q₀(s);
- one point of λ_b on each small arc;
- one double-cap gamble g.

This holds *given* three continuum facts:
- (i) the PC cluster limit at the exact facet gambles A, B and h(τ₁);
- (ii) Prop. D on the cap;
- (iii) infinitely many interface points (Hausdorff continuity and connectedness), needed for Bezout.

Without (iii) the cap map is not pinned. Without (i), Lemma 3.1 fails. This is why DCF, which sees only finitely many
good gambles and no continuity, stays feasible.

## 6. Effect on the write-up, and what a referee should check

- §5.3 "Where a solution of CF(T1) would have to live" is superseded.
  - C1's identity caps are *forced to be* caps, but with W_b = κ-diag, not the identity. So C1 itself is not part of
    any cover.
  - The chord layer lies inside the tangent wedge (Cor. 3.3).
- Conjecture N21 becomes Theorem 5.1, at the status above. Corollary: no additive cover of T1 on any (LF)
  decomposable domain (integral penalties). The charge version needs the existence proviso, as in Cor. charges.
- A referee should check, in order:
  1. Lemma 3.1, step 4: cluster convergence of the *c*-vectors on general domains, which Thm TS states for h near Σ;
  2. Prop. D (re-derive it; the diagonal step uses the strict signs of d);
  3. Lemma 4.2 (the limit of touching points; that the arc crossing lies near e_b);
  4. the exclusion of (I) (the orientation of the violating sign);
  5. Prop. 5.2.
- Possible generalisation (CONJECTURE): the same chain should work for every all-facing triangle in general position.
  The pinning algebra would then use the R15 pinched ratios.

## 7. Files (`c2py/`)

`dcf.py`, `horn.py`, `families.py`, `run1.py`, `run2.py`, `count.py` (lazy Horn DCF); `dcfplus.py`, `run_plus.py`,
`verify_plus.py` (witness DCF / DCF+); `pencil.py`, `pencil_tests.py` (per-prior MILP); `glue_conics.py`,
`pin_caps.py`, `pin_general.py`, `pin_symbolic.py`, `edge_check.py`, `cap_R1.py`, `two_caps.py` (§§4–5);
outputs `*.out`, `plus_e03.pkl`.
