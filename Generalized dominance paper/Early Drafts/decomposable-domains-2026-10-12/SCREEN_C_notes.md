# SCREEN_C. Transition pricing (candidate C): design checks and the S6 screen made precise

19 Oct 2026. Rules of BRIEF_DESIGN1. Labels:
- **PROVED**: the full argument is written here (one reader, me; not refereed).
- **CHECKED**: an import read step by step, or a standard fact.
- **CONJECTURE**.
- **NUMERICS**: exact-rational scripts in `screenC_py/`. Run `python3 -I <script>` inside that folder. Nothing rests on them.

No assumption is added to the programme. Hypotheses that belong to a single result are named there.

---

## 0. Verdict

**S6 as posed: C passes it literally, but S6's mechanism plus (TC) screens C out through S1. Two worlds: PROVED. n ≥ 3: CONJECTURE.**

1. **Hysteresis is excluded by (TC) alone** (Prop. 2.3(b), PROVED).
   - If some pair of advice states has a costly round trip (s := c(a,b) + c(b,a) > 0) on a non-null set, a two-problem swap creates a tie with slack. A small improvement then breaks (TC).
   - So ties between distinct models never come from hysteresis. Under (TC) a tie needs s = 0 on the whole changed set (§2.4).
2. **The S6 mechanism is a theorem in its correct form.** It concerns undominated models, not ties.
   - Competitiveness at weight w is pointwise self-stability (Lemma 2.6).
   - Under (TC), every model that is self-stable at an interior weight is undominated (Lemma 3.1).
   - The self-stable set is a product over problems. So (LA), (S) and direct (C) force a unique stable advice state on almost every problem, at every interior weight (Lemma 3.2, PROVED).
3. **C is not forced into potential form on relevant transitions.**
   - Example C1 (§4) is a full two-world system through K* = [1/3, 2/3]. It is non-potential on relevant transitions and satisfies strict (G), (IB), (TC), (FC) for every length, (LA), (S), direct (C) and (LF). PROVED; exact grid in NUMERICS.
   - It is also intransitive (CHECKED).
4. **Every survivor is additive in disguise (two worlds; Thm 3.5, PROVED).**
   - Fix any linear problem-separable rule satisfying the axioms with a selection continuous in measure.
   - Each world i then has an integrable, strictly guiding additive penalty ρ′_i. On every transition out of advice that a selected model can give, c_i(h,a,b) ≤ ρ′_i(h,b) − ρ′_i(h,a).
   - So every accepted comparison out of a selected model is endorsed by ρ′_i. That is S1, and FF2's (H3) holds with no localisation (S4).
   - The only non-potential freedom allowed on relevant transitions is a *balanced discount on the long jump −↔+* (the memo's "two-step jump costs less"). The adjacent potential endorses exactly that freedom.

**Scope of the PROVED screen.**
- Two worlds, the full four-advice domain, linear problem-separable rules with an integrable envelope.
- Axioms used: strict (G), (TC) (only problem by problem), (S) with a selection continuous in measure, (LA), direct (C).
- Not used: the target, (IB) (it is automatic), closed sections beyond continuity, (LF), (FC).
- One case needs an extra hypothesis, named in Thm 3.5.

**Open.**
- n ≥ 3 (§3.6).
- Selections that jump.
- Nonlinear rules (§5).

---

## 1. Setting

**Worlds, problems and advice.**
- Two worlds; t := p_1.
- Problems are indexed by h ∈ H = {h_1 > 0}.
  - *Unanimous* problems: h_2 > 0.
  - *Mixed* problems: h = (a, −b) with a, b > 0, and threshold τ(h) = b/(a+b). Here m·h > 0 iff m_1 > τ.
- Advice states: {+, 0, −, ×}.
- World ranks (better first):
  - unanimous: + < 0 < − < × at both worlds;
  - mixed, world 1: + < 0 < − < ×;
  - mixed, world 2: − < 0 < + < ×.

**Coherent models.** D_K with K = [l, u] gives:
- + if τ < l; 0 if l < τ < u; − if τ > u, on mixed problems;
- + on unanimous problems.

So coherent models are conic, and monotone in τ.

**Selected family.** This is FC v3 with width 1/3:
- K_t = [max(0, (4t−1)/3), min(1, 4t/3)];
- C_t := D_{K_t}, so C_{1/2} = D_{K*}, C_0 = D_{{0}} and C_1 = D_{{1}}.

The selection is continuous in measure.

**Rule C (linear).** C ≼_i X iff ∫ c_i(h, a_C(h), a_X(h)) dμ ≥ 0.
- c_i(h,a,a) = 0.
- c is measurable, with an integrable envelope e(h) ≥ max_{i,a,b} |c_i(h,a,b)|.

**Notation.** For each world:
- s(a,b) := c(a,b) + c(b,a) is the round-trip cost. Friction means s > 0; anti-friction means s < 0.
- k(x,y,z) := c(x,y) + c(y,z) − c(x,z) is the cocycle defect.
- c has *potential form* iff k ≡ 0. That forces s ≡ 0.

**Stability.** For w ∈ Δ:
- σ_w(h) := {a : w·c(h,a,b) ≥ 0 for all b}, the stable states;
- S(w) := {X : a_X(h) ∈ σ_w(h) a.e.}, a product over problems;
- W_a(h) := {w ∈ [0,1] : a ∈ σ_w(h)}, a closed interval.

---

## 2. Design checks (linear version)

**2.1 (IB). PROVED.** The integrand vanishes on unchanged problems. So the verdict is a function of the record (h, old, new) on the changed set, as S7 requires.

**2.2 Strict (G). PROVED.** Strict (G) holds iff, for a.e. h and every world i:
- c_i(h,a,b) ≥ 0 whenever b is worse than a at i;
- c_i(h,a,b) < 0 whenever b is better than a at i.

*Proof.* Apply (G) to pure records on arbitrary small sets. A pure worsening must satisfy X ≼ Y, and its reversal must fail Y ≼ X. ∎

Worsening costs may be 0. Thm 3.5 needs to exclude that in one degenerate case.

**2.3 (TC). PROVED.**
- (a) **Exact form.** Let V(h) ⊆ ℝ⁴ be the 64 vectors (α, β, γ, δ) = (c(x,y), c(y,z), c(z,x), c(x,z)) over triples (x,y,z). Let Q := {α, β, γ ≥ 0, δ < 0}. Then (TC) at world i fails iff ∫ v dμ ∈ Q for some measurable selection v of V. By Lyapunov, the achievable integrals are those of the selections of co V(h).
  - *Cell models* (finitely many problem types): (TC) holds iff there is a **uniform certificate** λ_1, λ_2, λ_3 ≥ 0 with
    c(x,z) ≥ λ_1 c(x,y) + λ_2 c(y,z) + λ_3 c(z,x)
    for all triples and types. This is Farkas: the alternative to a nonnegative combination in Q.
  - *Continuum c*: the uniform certificate is sufficient. **Necessary:** a certificate λ(h) exists for a.e. h. Otherwise, on a non-null set, select a failing combination at each h, integrate it, and realise it by a pure selection (Lyapunov). That gives three models violating (TC).
- (b) **No friction.** (TC) implies s_i ≤ 0 a.e., for every pair, at every world. Swap argument:
  - take two halves R_1, R_2 of a set on which s > 0, chosen by Lyapunov so that ∫_{R_1}(p, q) = ∫_{R_2}(p, q). Here p = c(u,v) and −q = c(v,u);
  - put A = u, B = v on R_1, and A = v, B = u on R_2;
  - then ∫c(A→B) = ∫c(B→A) = ½∫(p − q) > 0, a tie with slack;
  - let C improve A on a tiny extra set. Then A ≼ B ≼ C, C ≼ A, and not A ≼ C.

  NUMERICS: `example_check.out`, last two lines, and `tc_check.out` E4.
- (c) **Normal form.** Suppose that at h some pair has s = 0. This always holds on mixed problems under (S), (LA) and direct (C), by Thm 3.4.
  - The triples (x,y,x) and (x,x,z) force λ_1 = λ_2 = 1 + λ_3. So (TC) at h is equivalent to
    **k(x,y,z) ≤ θ·|s(x,z)| for all triples, for some θ ∈ [0,1).**
  - **Sub- and super-additivity.**
    - θ = 0 is super-additivity, c(x,z) ≥ c(x,y) + c(y,z). It gives **full transitivity** (sum the two inequalities).
    - θ > 0 allows a jump to cost *less* than its chain (k > 0), only on pairs with anti-friction, and only in a balanced way.
    - A jump that costs *more* than its chain violates (TC) through the triple (0, −, +). See `tc_check.out`:
      - E3, a jump surcharge: (TC) fails;
      - E2, a one-sided discount: (TC) fails;
      - E1, a symmetric discount: holds, with λ = (2, 2, 1).

**2.4 Ties. PROVED.** Under (TC), X ~_i Y iff ∫c_i(X→Y) = ∫c_i(Y→X) = 0 and s_i = 0 a.e. on the changed set. (The two integrals are ≥ 0 and sum to ∫s_i ≤ 0.)

So hysteresis cannot create ties. Anti-friction creates **incomparability** instead.

**2.5 Closed sections. PROVED.** Suppose the selection is continuous in measure. By dominated convergence (envelope e), t ↦ ∫c_i(h, a_{C_t}, a_X) is continuous, so {t : C_t ≼_i X} is closed.

**2.6 Competitiveness ⇔ pointwise self-stability. PROVED.** C is competitive on J iff C ∈ S(w) for some w ∈ Δ_J.
- (⇒) Put Z := {(∫c_i(h, a_C, a_X))_{i∈J} : X}. Z is convex by Lyapunov, and it misses the open negative orthant. Separation gives w ∈ Δ_J with w·Z ≥ 0. Switching on small sets makes this pointwise.
- (⇐) If w·z(X) ≥ 0, some i with w_i > 0 has z_i ≥ 0.

This is FF2 Step 1 with c in place of a field.

---

## 3. The S6 screen

**Lemma 3.1 (stable at an interior weight implies undominated; PROVED).** Assume (TC). If X ∈ S(w) with w ∈ int Δ, then X is undominated.

*Proof.*
- Suppose Y dominates X.
- Y ≼_i X and s_i ≤ 0 give ∫c_i(X→Y) = ∫s_i − ∫c_i(Y→X) ≤ 0 at every world.
- Stability gives Σ w_i ∫c_i(X→Y) ≥ 0. Since every w_i > 0, all of these integrals are 0.
- Then X ≼_i Y at every world, so the domination has no strict step. ∎

**Lemma 3.2 (uniqueness: the S6 mechanism; PROVED).** Assume (TC), (LA), (S) and direct (C). Let w ∈ int Δ with S(w) ≠ ∅. Then σ_w(h) is a singleton for a.e. h.

*Proof.*
- Fix C ∈ S(w). Suppose |σ_w| ≥ 2 on a non-null set E.
- Choose measurably β(h) ∈ σ_w(h) ∖ {a_C(h)}.
- Split E radially: E^low consists of the points below the radial median of their ray, under the Gaussian radial law.
- Put X := β on E^low and X := C elsewhere.
- Then X ∈ S(w). By Lemma 3.1, X is undominated. HH1 Prop. 1(c) (CHECKED) gives U_L = C_L, so X is coherent, hence a cone up to null sets.
- But on a non-null set of directions, X takes two values along a single ray: a_C on E^high and β on E^low. That is a contradiction. ∎

*Reading.* Without uniqueness, an incoherent model is undominated exactly as a selected one is. Direct (C) forbids this.

**Lemma 3.3 (covering; PROVED for n = 2).** Suppose the selection is continuous in measure. Then every w ∈ [0,1] lies in W(t) := {w : C_t ∈ S(w)} for some t.

*Proof.*
- W(t) is a closed interval. It is nonempty by 2.6.
- Its graph is closed: a_{C_{t_n}} → a_{C_t} a.e. along a subsequence, and the values are discrete.
- W(0) ∋ 0 and W(1) ∋ 1.
- An upper hemicontinuous correspondence with convex values on [0,1] has a connected graph. Its projection is therefore [0,1].
- For n ≥ 3 this is FF2 Step 3 (CHECKED import). ∎

**Theorem 3.4 (structure; PROVED, n = 2).** Assume strict (G), (TC), (LA), direct (C), and (S) with a selection continuous in measure. Put S(h) := {a : W_a(h) meets (0,1)}. For a.e. h:

- (i) **Tiling.** The intervals W_a(h) tile [0,1] with disjoint interiors.
  - Unanimous h: S(h) = {+} and W_+ = [0,1].
  - Mixed h: the order is W_−, then W_0 (possibly absent), then W_+. Also W_− ∋ 0 and W_+ ∋ 1, and both are nondegenerate.
- (ii) **Adjacent pairs are frictionless.** Consecutive states a, b in S(h) satisfy s_1(a,b) = s_2(a,b) = 0, i.e. they are antisymmetric.
- (iii) **Only a balanced discount on the jump.** Suppose S(h) = {−, 0, +}, and put
  J := c(−,+) − [c(−,0) + c(0,+)] and J′ := c(+,−) − [c(+,0) + c(0,−)].
  Then, at each world, J ≤ 0, J′ ≤ 0 and max(−J, −J′) ≤ θ(h)(−J − J′) with θ(h) < 1.
- (iv) **Selected advice is stable at interior weights.** Every selected model's advice lies in S(h) a.e.

*Proof.*
- (i), interiors. By Lemma 3.3, every rational w ∈ (0,1) lies in some W(t). So S(w) ≠ ∅, and Lemma 3.2 gives |σ_w(h)| = 1 for a.e. h. A countable union of null sets is null. The sets W_a(h) are closed and their union contains the rationals, so it is all of [0,1]. Their interiors are disjoint, since otherwise they would share a rational point.
- (i), order. At w = 0, strict (G) makes the world-2-best state the unique stable one. On a mixed problem that is −, so W_− comes first. Symmetrically W_+ comes last. If W_+ were {1}, its neighbour would contain 1 and would have to be +.
- (ii) A shared endpoint w* ∈ (0,1) gives w*·c(a,b) ≥ 0 and w*·c(b,a) ≥ 0. So w*·s ≥ 0. With s ≤ 0 and w* interior, s = 0 at both worlds.
- (iii) Take the per-problem certificate (2.3(a)) in its normal form (2.3(c)).
  - The triple (0, −, +) gives (1+μ)c(0,+) ≥ (1+μ)(c(0,−) + c(−,+)), i.e. J ≤ 0.
  - The triple (0, +, −) gives J′ ≤ 0.
  - The triples (−, 0, +) and (+, 0, −) give the balance, since k = −J or −J′ and |s(−,+)| = −J − J′.
- (iv) If W(t) contains an interior w, then a_{C_t}(h) ∈ σ_w(h), which lies in S(h). Otherwise W(t) is a vertex, and the state is + or −. ∎

**Theorem 3.5 (additive in disguise; PROVED, n = 2).** Under the hypotheses of 3.4, each world i has an integrable, strictly guiding additive penalty ρ′_i such that
**c_i(h,a,b) ≤ ρ′_i(h,b) − ρ′_i(h,a) for a.e. h, every a ∈ S(h) and every b**,
with equality on consecutive pairs.

Consequently:
- if B is selected and B ≼_i X, then ∫ρ′_i(X) ≥ ∫ρ′_i(B). Every world adds up, with a countably additive integral endorser, on all comparisons out of selected models, not only those to regular X;
- FF2's (H3) holds with ℓ = ρ′ and H_n = H.

*Extra hypothesis for one case.* On mixed problems with S(h) = {−, +}, strictness of ρ′_i(0) needs worsening costs to be strictly positive there. This case does not arise when every mixed problem has silence at some selected model.

*Proof.*
- **Mixed problems, on S(h).** Put ρ′(−) := 0, ρ′(0) := c(−,0) and ρ′(+) := c(−,0) + c(0,+).
  - Consecutive pairs give equality, in both directions by (ii).
  - The jumps satisfy ≤ by (iii).
  - Strictness: consecutive pairs are strict, by 2.2 together with antisymmetry. The path −, 0, + is monotone in rank at both worlds.
- **States outside S(h).** These are × on mixed problems, and 0, −, × on unanimous problems. All are rank-worse than every state of S(h) at both worlds.
  - Define ρ′ on them upward in rank by ρ′(b) := max(max_{a∈S(h)} [ρ′(a) + c(a,b)], ρ′(previous state)) + e(h).
  - Only lower bounds are needed. The envelope keeps ρ′ integrable.
- **The case S(h) = {−, +}.** The triple (+, 0, −) with s(+,−) = 0 gives c(+,0) ≤ c(+,−) − c(0,−). This places 0 strictly between − and + when c(0,−) > 0. ∎

*What this means for C.*
- In two worlds, a linear problem-separable rule satisfying the axioms is never (M1) or (M2) on relevant comparisons.
- Its acceptances out of selected models are a subset of those of the additive ranking ρ′.
- ρ′ keeps the same selection as weak Bayes models: w·c ≥ 0 together with c ≤ Δρ′ gives w·Δρ′ ≥ 0.

**3.6 n ≥ 3 (CONJECTURE).** Lemmas 2.6, 3.1 and 3.2 hold verbatim for any finite Ω. FF2 Step 3 gives covering.
- The interior adjacency graph on S(h) is connected, because int Δ is connected.
- Its edges are antisymmetric.
- On mixed problems S(h) ⊆ {+, 0, −}, so a spanning tree has at most two edges. The certificate argument of 3.4(iii) then gives c ≤ (tree potential) on the remaining pair.

Two gaps stand between this and the n-world version of Thm 3.5, which with FF2 Thm 4.1 would exclude every linear problem-separable cover of T1 with a continuous selection:
- **(i)** A model selected at a face may use a state that is stable only at boundary weights. For such a state antisymmetry is forced only at the worlds of the face.
- **(ii)** Strictness of ρ′ when the tree is not the rank path and some worsening cost is 0.

**Selections that jump** (not continuous in measure) are outside every statement of §3.

---

## 4. Example C1: a non-potential survivor through K* (PROVED; NUMERICS)

**The rule.** Take the FC v3 penalties ρ with width 1/3.
- Mixed problems: ρ_1 = (0, c_w, a, 2a) and ρ_2 = (b, c_w, 0, 2b) on the states (+, 0, −, ×), with c_w = 3ab/(4(a+b)).
- Unanimous problems: the FC v3 table.

Set c_i(h,x,y) := ρ_i(y) − ρ_i(x), except on mixed problems:

  **c_i(−,+) and c_i(+,−) are both lowered by J(h) = −ab/(4(a+b)), at both worlds.**

The rule is non-potential on relevant transitions: −→+ starts from a_{C_t} = − for small t, and k(−,0,+) = −J > 0.

**Checks.**
- **(G).** The changed worsening costs stay strictly positive: c_2(−,+) = b + J > 0 and c_1(+,−) = a + J > 0.
- **Competitiveness and uniqueness, at w = (t, 1−t).**
  - Without the discount, C_t is the a.e.-unique Bayes model (FC v3, Lemma thresholds).
  - The discount only lowers costs. So it cannot create new stable states.
  - It keeps − and + stable. On the region where − is selected (t < 3τ/4), w·c(−,+) = b − t(a+b) + J ≥ b/4 + J > 0. On the region where + is selected (t > (3τ+1)/4), w·c(+,−) ≥ a/4 + J > 0.
- **(TC).** A uniform certificate (2, 2, 1; 1) works. For any triple, c(x,z) − 2c(x,y) − 2c(y,z) − c(z,x) = −2J([xy] + [yz]) ≥ 0, where [·] indicates the jump pair. The potential parts cancel.
- **(FC) for every length.** Take a cycle A_0 ≼ … ≼ A_k ≼ A_0.
  - The edge integrals sum to ∫J·(number of jumps) ≥ 0. Since J < 0, no edge carries a jump.
  - So every edge integral is 0.
  - A_0 → A_k is the pointwise reversal of a jump-free edge, so its integral is 0, and A_0 ≼ A_k.
  - CHECKED for k = 3 by LP: `fc_check.out`.
- **Transitivity fails.** At world 1, the triple types (+0+, +0−, 0++) with weights (6, 6, 12) give A ≼ B ≼ C and not A ≼ C (`tc_check.out` E1).
- **Remaining axioms.**
  - Closed sections: by 2.5.
  - (LA): by Lemma 3.1, plus the vertex models, which are the unique world-optimal models.
  - Ties X ≈ C_t avoid jumps (s = 2J < 0). They are then additive ties, so X = C_t by uniqueness of the Bayes model. This gives direct (C) and C_L = {C_t}.
  - (IB) and (LF) are trivial.
- **Coverage.** K_{1/2} = [1/3, 2/3], so the target is covered.

**But.** c ≤ Δρ on every transition, so ≼^c_i ⊆ ≼^ρ_i. This is S1 in its purest form.

NUMERICS (`example_check.out`):
- an 8 × 8 grid of (a,b) and t ∈ {k/96};
- 6148 stability and uniqueness checks;
- 8192 certificate checks;
- 1536 checks each for (G) and for endorsement;
- no failures.

---

## 5. Nonlinear problem-separable rules (CONJECTURE)

Consider verdicts Φ_i(∫c_i^1, …, ∫c_i^m) ∈ A_i.

**What survives.**
- Lyapunov convexity of the statistic set Z.
- The product structure of every *pointwise* stability condition.
- For disjunctive worlds (accept iff some linear test passes), the complement is an intersection of open half-spaces. 2.6 then holds with a mixture cost Σ w_{ik} c_i^k.
- I expect §3 to run with that mixture once the per-test no-friction bound is established. It does not follow automatically from (TC).

**What does not survive.** For conjunctive or quorum worlds the complement is not convex, and the problem is the S3 collapse (NN1 Lemma 2.1, NN2 Thm 2.3), with transition integrands in place of additive scores.
- Those proofs use only finitely many linear functionals of the record. If they need nothing more, they apply verbatim.
- This note does not screen that class.

---

## 6. Task 3: does C escape FF2's single-field barrier (S4)?

**Formally, yes.** FF2 Thm 4.1 assumes an integrable, strictly guiding field ℓ that endorses local acceptances out of selected models, (H3). Rule C supplies no such field: its effective weighting c(a_C(h), ·) depends on the starting advice, as the memo says.

**It does not matter.**
- Thm 3.5 shows that in two worlds the axioms manufacture the field: (H3) holds with ℓ = ρ′, globally rather than only locally.
- Two worlds are not an obstruction anyway, since FC v3 covers additively. So C gains nothing there.
- In three worlds, C escapes S4 only through the gaps of §3.6: face-selected states that are stable only at boundary weights and carry non-antisymmetric costs, or degenerate zero worsening costs.
- C remains exposed to S2 regardless: competitiveness is pointwise (2.6), so the defence is per problem and never across regions.

**Recommendation.** Retire C (and linear transition pricing generally) as a mechanism. Keep §3 as the screen for any future per-problem rule: no friction (from (TC)), uniqueness (from direct (C)), and adjacent antisymmetry (from covering) together leave only discounts that an additive field endorses.

---

## 7. Files

- `screenC_py/exlp.py`: exact Phase-I simplex with Bland's rule.
- `screenC_py/tc_check.py` → `tc_check.out`: per-problem (TC), certificates and transitivity for the cases P and E1–E5.
- `screenC_py/example_check.py` → `example_check.out`: the Example C1 grid, and the friction-swap failure of (TC).
- `screenC_py/fc_check.py` → `fc_check.out`: (FC) with k = 3 for Example C1.
