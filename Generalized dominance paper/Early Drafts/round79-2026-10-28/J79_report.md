# J79: Joyce (2009), "Accuracy and coherence", against LDG's conditions

Paper: J. M. Joyce, "Accuracy and coherence: prospects for an alethic epistemology of partial belief", in *Degrees of Belief*, Springer 2009, 263–297. Source: `papers/Degrees of Belief 2009 Joyce.txt`. Page numbers are the printed ones.

## Results

The class of scoring rules in Joyce's Theorem 2 is: finite, continuous, truth-directed, and satisfying coherent admissibility (CA). Call it 𝒥_N, where N is the number of cells.

| Condition | Whole class 𝒥_N | Verdict |
|---|---|---|
| (E) evaluability | every rule is defined on all of [0,1]^N | **HOLDS** (PROVED, trivial) |
| (A) coherent admissibility | Joyce's CA says exactly that C_L = C for **every** rule | **HOLDS** (PROVED). Joyce's version is stronger than ours. |
| (S) selection | fails for LDG's prop:joyce loss (N = 3), and also for a new **additive, extensional, strictly convex** loss (N = 3) | **FAILS** for N ≥ 3 (PROVED). **HOLDS** for N = 2 (PROVED). |
| (T) closure under ties | fails for a convex loss with two cells; holds for the prop:joyce loss | **FAILS** in general (PROVED). Holds under strict propriety or strict convexity (PROVED). |

**Subclasses where all four conditions hold.**
- **Strictly proper rules** (Joyce's PROPRIETY) with p ↦ S(p,ω) lower semicontinuous on Δ. Values in [0,∞] are allowed, so this includes the log score and Joyce's "hybrid" score, which his Theorem 2 does not cover. The route is thm:bayes-finite with c_p := p. Proposition prop:proper also gives uniform, hence strict, dominance. (PROVED, via prop:proper.)
- **Additive rules with C¹ components** whose derivatives have strict signs on (0,1), with N ≥ 3, satisfying CA together with either 0/1-symmetry or Lindley's endpoint conditions. Here CA forces strict propriety, so the previous bullet applies. (CHECKED; sketch in §3.5.)
- **N = 2**: the whole class 𝒥_2 satisfies (E), (A) and (S). Adding (T), for example through strict convexity, gives all four.

**About the prop:joyce loss.** It satisfies all of Joyce's exact hypotheses: finite, continuous, truth-directed in his sense, CA, and also his standing assumption of permutation invariance (p. 271, n. 9). So it is a valid counterexample to Theorem 2 (CHECKED analytically and numerically). Against our conditions, (E), (A) and (T) hold, and **(S) fails**. On the natural route (cor:closed-choice with c_p := p), the hypothesis that fails is **competitiveness on supp p** at p = (½,½,0): the coherent credence (½,½,0) is strictly beaten at worlds 1 and 2 by x* = (1,1,0). The comparison sets are closed. On the Bayes route, Bayes choices exist (vertex choices), but every coherent assignment that meets the Bayes-choice condition fails lower semicontinuity.

**What the author must know.**
1. **Joyce's Theorem 2 has a second gap: ties.** In Lemmas 2 and 2*, the fixed-point case where every difference f_n(p) is 0 does not contradict CA, because CA excludes dominance of a coherent credence but not ties. Two-cell counterexample: L_1 = (1−x_1+x_2)², L_2 = (1+x_1−x_2)². Every credence, including Joyce's inconsistent (0,0), is tied with a coherent one and is undominated. LDG §8 diagnoses only the Lemma 1* gap.
2. **Additivity, extensionality and strict convexity do not rescue Theorem 2.** Take s(b,1) = 3(1−b)² + 4(1−b), s(b,0) = 3b² + 2b, and L(x,ω) = Σ_n s(x_n, 1{n=ω}) with N = 3. This loss is finite, continuous, truth-directed and CA, and no two distinct models are tied. But (⅔,⅔,0) is the unique Bayes model for the prior (½,½,0), so nothing else weakly dominates it. This partly answers LDG's open question in §9.
3. **For credences whose coordinates sum to less than one, Joyce's argument is sound up to ties.** Such a credence is strictly dominated by, or tied with, a coherent credence. With (T), it is strictly dominated.

---

## 1. Joyce's setting, precisely

**Models.** Credence functions on a finite partition X = ⟨X_1,…,X_N⟩, identified with vectors b ∈ B_X = [0,1]^N (§1, p. 265).

**Worlds.** The consistent truth-value assignments V_X = {ν^1,…,ν^N}, where ν^n has a 1 in place n and 0 elsewhere (p. 265).

**Coherent class.** P_X, the probability vectors, which equal the convex hull of V_X (p. 265).

**Scoring rule.** "a scoring rule S_X that, for each b in B_X and ν in V_X, assigns a real number S_X(b,ν) ≥ 0 which measures the epistemic disutility" (p. 266). Rules are finite-valued in general. Standing assumption (p. 271, n. 9): "the ordering of the propositions in X is immaterial to the value of the scoring rule". That is, S is invariant under permuting the cells together with the worlds.

**Dominance vocabulary.**
- Joyce's plain "dominated" is strict: S(b,ν) > S(b*,ν) for every ν (p. 267).
- ADMISSIBILITY uses weak dominance (≥ at every world, > at some), which is LDG's dominance: "Epistemically rational credences are never weakly dominated in this way" (p. 267).
- "Admissible" means undominated in LDG's sense.

**Conditions on rules.** Joyce assumes the first three throughout (p. 271); the rest are optional.
- **TRUTH-DIRECTEDNESS** (p. 269): if, at ν, every coordinate of b lies between the corresponding coordinate of b* and ν_n, with strict "between" somewhere, then S(b*,ν) > S(b,ν). On [0,1]^N with 0/1 truth values this is exactly LDG's def:truth-directed (|c'_n − e_ω(n)| ≤ |c_n − e_ω(n)| for all n, strictly for some).
- **ADMISSIBILITY** (p. 267): weakly dominated credences are irrational.
- **COHERENT ADMISSIBILITY** (p. 280): "S is unreasonable if there are b ∈ P_X and c ∈ B_X such that S(b,ν) ≥ S(c,ν) for every ν and S(b,ν) > S(c,ν) for some ν". In words: no coherent credence is dominated, in LDG's sense, under S.
- Optional: SEPARABILITY (p. 271); EXTENSIONALITY (p. 273); 0/1-SYMMETRY and NORMALITY (p. 274); PROPRIETY (p. 276), which is *strict*: Exp_b S(b) < Exp_b S(c) for b ∈ P_X and c ≠ b; CONVEXITY (p. 282), which is strict midpoint convexity in b at each ν.
- Continuity and finiteness enter only as hypotheses of Theorem 2.

**Main results.**
- **Theorem 1 (Lindley), p. 286.** For an additive rule with C¹ components, s_n'(b,0) > 0 > s_n'(b,1) on (0,1), and endpoint ratio conditions: b is admissible only if the transform p_n = s_n'(b_n,0)/[s_n'(b_n,0) − s_n'(b_n,1)] is coherent. Conversely if the transform is one-to-one.
- **Corollary, p. 287.** For a truth-directed, (strictly) proper, additive rule with differentiable components: b is incoherent iff some c weakly dominates it.
- **Theorem 2, pp. 287–288; restated as Theorem 4 in the Appendix, p. 293.** "If S satisfies TRUTH-DIRECTEDNESS and COHERENT ADMISSIBILITY, and if S(b,ν) is finite and continuous for all b in B_X and ν ∈ V_X, then (i) every incoherent credence function is inadmissible relative to S and, moreover, is dominated by some coherent credence function, and (ii) every coherent credence function is admissible relative to S." With "dominated" read as on p. 267, (i) asserts **strict** dominance by a coherent credence. The proof (pp. 293–296) aims at f_n(p) < 0 for all n.
- **Proof structure.** Fix incoherent c.
  - If Σc < 1, Joyce defines b^m by raising c_m to 1 − Σ_{n≠m} c_n. Lemma 1 (p. 294): if λ_m = 0 then f_m(p) > 0. Then a Brouwer fixed point argument, with Lemma 2 (p. 295).
  - If Σc > 1, the mirror case defines b^m by b^m_m = c_m and b^m_n = c_n(1−c_m)/Σ_{k≠m}c_k. Lemma 1* (p. 295) and Lemma 2* (pp. 295–296).
- **Theorem 3 (Savage), p. 291.** A characterisation of quadratic scores; not a dominance result.
- Joyce notes the limitation himself: Theorem 2 "fails to address scoring rules, like the logarithmic rule, that go infinite at their extreme points" (p. 288).

## 2. Translation into LDG

- Ω = {1,…,N}, with world n ↔ ν^n.
- 𝓜 = [0,1]^N.
- 𝒞 = Δ (= P_X).
- Each rule S is a loss ranking with L(m,ω) := S(m,ν^ω) ∈ [0,∞), and M_L = 𝓜 for every L.
- 𝔏 = 𝒥_N := {S : S finite and continuous in b for each ν, truth-directed, CA, permutation-invariant}. This is the class in Theorem 2. Joyce's premise (IV) (p. 290) instead takes a single correct rule per context, 𝔏 = {S}; the verdicts below are the same.
- Subclasses studied:
  - 𝒥_N^prop: rules with strict PROPRIETY and lower semicontinuity on Δ. Values in [0,∞] allowed, so this class lies partly outside 𝒥_N.
  - 𝒥_N^add: additive rules S(b,ν) = Σ_n λ_n s_n(b_n,ν_n) in 𝒥_N.
- LDG's dominance principle (def:permissibility) is the narrow-scope reading of Joyce's (III), which Bronfman questions (pp. 288–290). This is context only, not a condition.

## 3. The conditions

### 3.1 (E): HOLDS (PROVED)
Every S is defined on all of [0,1]^N, so M_L = 𝓜. The family is nonempty, since the Brier score is in 𝒥_N.

### 3.2 (A): HOLDS (PROVED)
Joyce's CA, for a single S, says that no c ∈ B_X dominates any b ∈ P_X in LDG's sense. So C_L = C ∩ U_L = C for every L ∈ 𝒥_N. Our (A) needs this only for *some* L per coherent model, so (A) holds a fortiori. Theorem 2(ii) is this restatement (Joyce: "(ii) is just a restatement of COHERENT ADMISSIBILITY", p. 293).

### 3.3 (T): FAILS for the class (PROVED); holds under extra assumptions

**Counterexample (N = 2).** Let L_1(x) := (1−x_1+x_2)² and L_2(x) := (1+x_1−x_2)².
- **In 𝒥_2.** The loss is finite, continuous and permutation-invariant. It is truth-directed: L_1 is strictly decreasing in x_1 and strictly increasing in x_2 on [0,1]², because 1−x_1+x_2 ≥ 0 and squaring is strictly increasing on [0,∞); L_2 symmetrically. It is convex, though not strictly.
- **CA holds.** Write d := x_1 − x_2. The profile of x is ((1−d)², (1+d)²). For coherent b = (t,1−t), d_b = 2t−1. If L(x) ≤ L(b), then d ≥ d_b and d ≤ d_b, so the profiles are equal. No coherent credence is dominated.
- **(T) fails.** Every x is tied with the coherent credence ((1+d)/2, (1−d)/2). For example, Joyce's "inconsistent" (0,0) has profile (1,1), the same as (½,½). Since C_L = C, a model tied with an undominated coherent model is not coherent, so (T) fails.
- **Every model is undominated.** A dominator of x would dominate the coherent model tied with it. So every incoherent credence is rationally permissible under 𝔏 = {L}.
- **(S) holds here.** c_p := p is a Bayes model for p, since p·L(x) = p_1(1−d)² + p_2(1+d)² is minimised at d = p_1 − p_2. The losses are continuous. This is LDG's "merely proper" situation; prop:profiles applies.

This also refutes Theorem 2(i) by a route different from LDG's. The gap is in Joyce's Lemma 2, first case (p. 295): "The first two possibilities entail S(p,ν_n) ≥ S(c,ν_n) for all n, which contradicts COHERENT ADMISSIBILITY". The all-zero possibility is a tie and contradicts nothing. The same applies to Lemma 2*.

**Sufficient extra assumptions for (T).**
- **Strict propriety (PROVED).** If L(x) = L(b) with b coherent, then Exp_b L(x) = Exp_b L(b), so x = b.
- **Strict convexity of each L(·,ω), with CA (PROVED).** If x ≠ b and L(x) = L(b), the midpoint (x+b)/2 strictly dominates b, contradicting CA.
- **Any loss with no ties between distinct models.** This covers prop:joyce and the additive example below.

**Nearby variant without (T).** Loss rankings are transitive, so whenever the dominance property holds, prop:profiles identifies the undominated models as those tied with a coherent model. In the example above, that is every model.

### 3.4 (S): FAILS for N ≥ 3 (PROVED); HOLDS for N = 2 (PROVED)

Since C_L = C, any instance of (S) yields, through thm:finite, cor:closed-choice or thm:local, weak domination of every model by a coherent model. So (S) fails for L whenever some model has no coherent weak dominator.

**(a) LDG prop:joyce loss, N = 3.** L_i(x) = (1−s_i(x))² + ε(Σx−1)², with s the softmax and ε = 1/250.
- *Consistency with Joyce's exact hypotheses (CHECKED).*
  - Finite and continuous on [0,1]³.
  - Truth-directed in Joyce's sense: strict monotonicity in each coordinate. The bounds 1/7 < s_i < 3/5 and the derivative bounds in LDG's proof are correct, and 20,000 random points showed no sign violations.
  - CA holds; indeed L(x) ≤ L(b) with b coherent forces x = b.
  - Permutation-invariant: s_{σ(i)}(σx) = s_i(x), and Σx is symmetric.
- *Numbers.* L_1(x*) = L_2(x*) = 0.33772 < 49/144 + 1/250 = 0.34428 < 9/25. Over a 0.0025-grid of Δ, the minimum over coherent b of max_{i∈{1,2}} [L_i(b) − L_i(x*)] is 0.0422 > 0. So x* has no coherent weak dominator.
- *Our conditions.* (E) holds, (A) holds (C_L = C), (T) holds (no ties), **(S) fails**.
- *Where each route breaks.*
  - **cor:closed-choice with c_p := p.** The comparison sets {p : L(p,ω) ≤ L(m,ω)} are closed, by continuity. Competitiveness holds at interior p (CA plus completeness, Lemma lem:competitive) and at vertices (truth-directedness). It **fails** at p = (½,½,0): L_1(p) = L_2(p) = 0.3799 > L_i(x*), so x* strictly beats p on supp p = {1,2}.
  - **thm:bayes-finite.** Bayes choices with coherent models exist at every p; for example c_p = e_ω for some ω ∈ supp p is a Bayes model for δ_ω. For the edge priors (q,1−q,0), the global Bayes model is incoherent for q ∈ {0.5, 0.6} (for example (1,1,0) at q = ½, with V = 0.3377 against a coherent minimum of 0.3799), and is (1,0,0) for q ≥ 0.75. Since the conclusion fails, every coherent assignment satisfying the Bayes-choice condition (i) must violate lower semicontinuity (ii).
  - **thm:finite.** Excluded by the failure of the conclusion.
- *Side observation (CHECKED numerically, not proved).* Minimising ΣL over B = {L ≤ L(x*)} returns y = x* itself, so x* appears to be undominated, not just some y ∈ B. LDG's proof does not need this.

**(b) New additive, extensional, strictly convex counterexample, N = 3 (PROVED).** Let
s(b,1) := 3(1−b)² + 4(1−b), s(b,0) := 3b² + 2b, and L(x,ω) := Σ_{n=1}^3 s(x_n, 1{n=ω}).
- *In 𝒥_3, and more.*
  - Finite and continuous.
  - Truth-directed: s'(b,1) = −6(1−b) − 4 ≤ −4 and s'(b,0) = 6b + 2 ≥ 2.
  - Permutation-invariant, additive, separable, extensional, and strictly convex (Joyce's CONVEXITY).
  - L(e_ω,ω) = 0.
  - It is not proper, not normal and not 0/1-symmetric.
- *Bayes models.* Under a prior p, the expected loss is Σ_n [p_n s(x_n,1) + (1−p_n) s(x_n,0)]. Each summand has derivative 6x_n + 2 − 12p_n and second derivative 6. So the unique Bayes model is x_n = clip(2p_n − ⅓, 0, 1). Lindley's transform is T(b) = b/2 + 1/6.
- *CA and (T).* For coherent b, put p := b/2 + (1/6)(1,1,1). Then p ∈ Δ with every p_n ≥ 1/6, so p is interior, and its unique Bayes model is b. Since p is interior, any weak dominator of b is a Bayes model for p, hence equals b. So every coherent credence is undominated and no other model is tied with it.
- *(S) fails.* For p = (½,½,0), the unique Bayes model is x_a = (⅔,⅔,0), with Σ = 4/3. Any weak dominator z has p·L(z) ≤ p·L(x_a) = V(p), so z = x_a. So x_a is incoherent, undominated, and weakly dominated by no coherent credence. Numerically, the minimum over coherent b of max_ω [L(b,ω) − L(x_a,ω)] is 1/6 > 0. On the c_p := p route, competitiveness again fails at (½,½,0): L(·,1) and L(·,2) are 4.5 at (½,½,0) and 13/3 at x_a.
- *Why this matters.* Theorem 2 fails even under every 2009 condition except PROPRIETY, NORMALITY and 0/1-SYMMETRY. Joyce stresses that Theorem 2 needs no additivity, separability or convexity (p. 288), but adding them does not make it true. Joyce's own conjecture about convexity (p. 288) concerns infinite scores, so it is not refuted here.

**(c) N = 2: (S) HOLDS for every S ∈ 𝒥_2 (PROVED).**
- *Route.* cor:closed-choice with c_p := p.
- *Closed comparison sets:* by continuity.
- *Competitiveness on supp p.*
  - Interior p: CA means p is not dominated, so not strictly dominated, and Lemma lem:competitive (completeness of loss rankings) makes p competitive on Ω = supp p.
  - p = δ_ω: c_p = e_ω is the unique best model at ω, by truth-directedness.
  - With N = 2 there are no other boundary priors.
- *Assigned models* are coherent, hence undominated by CA.
- *Consequence.* Every credence is weakly dominated by a coherent one, so Theorem 2(i) holds for N = 2 up to ties. The tie example of §3.3 shows that ties really occur.
- *Side note.* For N = 2 Joyce's Lemma 1* has the wrong sign under truth-directedness. With p = b^m and k ≠ m, b^m equals c in coordinate m and is further from the truth in coordinate k, so f_k(p) > 0, not < 0. For Brier with c = (0.8,0.7), f_2(b^1) = 0.55. The theorem holds for N = 2 by a different argument.

**(d) Nearby sufficient hypothesis for all N (PROVED).** Call it *face coherent admissibility*: for every p ∈ Δ, no credence is strictly better than p at every world p charges. With continuity, this gives (S) by the same cor:closed-choice route with c_p := p. This condition is not Joyce's. It fails for both counterexamples at p = (½,½,0), and it is not necessary for the dominance property (rem:vertex).

**(e) Credences with Σc < 1 (PROVED; this repairs Joyce's own argument).**
- Lemma 1 (p. 294) is correct. With λ_m = 0, p equals c in coordinate m and is at least c elsewhere, strictly somewhere, so it is further from the truth at ν^m.
- Lemma 2's second case correctly derives that c strictly dominates the coherent p, contradicting CA.
- Its first case leaves exactly two outcomes: f ≡ 0 (a tie) or f < 0.
- So, under Theorem 2's hypotheses, every c with Σc < 1 is strictly dominated by, or tied with, a coherent credence. With (T), it is strictly dominated.
- Both counterexamples use Σ > 1 (x* has Σ = 2, x_a has Σ = 4/3). In the additive example every Bayes model has Σ ≥ 1; a minimum of 1.000 was found over 2,000 random priors.

### 3.5 Subclasses where (E), (A), (S), (T) all hold

1. **𝒥_N^prop: strictly proper (Joyce's PROPRIETY), with p ↦ S(p,ω) lower semicontinuous on Δ. Values in [0,∞] allowed (PROVED, via prop:proper).**
   - *Route.* thm:bayes-finite with c_p := p.
     - (i) p is a Bayes model for p, and supp p ⊆ supp p.
     - (ii) Lower semicontinuity holds by hypothesis.
     - Competitiveness follows from lem:bayes-competitive.
     - The assigned models are undominated coherent models: a weak dominator of p is a Bayes model for p, hence equals p.
   - *(T)* holds by §3.3.
   - *Uniform dominance.* prop:proper's last clause gives uniform dominance, which is strict since Ω is finite, when the losses on Δ are finite or continuous.
   - *Members.* Brier, the power scores, spherical, every additive rule with continuous strictly proper components, and the log and hybrid scores (p. 275), whose losses are continuous as maps into [0,∞].
   - *Caveat for the log score.* For uniform dominance, prop:strict(b) is needed, with "continuous" read as continuity into [0,∞]. Its proof only uses continuity at worlds in supp p, where the losses are finite. **Suggest stating this reading in prop:strict(b).**
   - *Truth-directedness* is not needed.
   - This class contains Joyce's Corollary to Lindley (p. 287) and the Lieb et al./Predd result he cites.
2. **Additive, C¹ components with s_n'(b,0) > 0 > s_n'(b,1) on (0,1), N ≥ 3, CA, plus either 0/1-symmetry or Lindley's endpoint conditions T_n(0+) = 0 and T_n(1−) = 1 (CHECKED, sketch).**
   - *Step 1.* CA at an interior coherent b, together with Gordan's alternative, gives p ∈ Δ with Σ_ω p_ω ∇L_ω(b) = 0. If no such p existed, a direction d with ∇L_ω(b)·d < 0 at every ω would strictly dominate b. So p_n = T_n(b_n) and Σ_n T_n(b_n) = 1 on the open simplex.
   - *Step 2.* Continuous Pexider solutions give T_n(x) = αx + β_n with Σβ_n = 1 − α.
   - *Step 3.* The endpoint conditions give β_n = 0 and α = 1. Alternatively, 0/1-symmetry gives T_n(1−b) = 1 − T_n(b), hence β_n = (1−α)/2, and so (1−α)(N/2 − 1) = 0, which forces α = 1 when N ≥ 3.
   - *Step 4.* T_n = id gives s_n'(b,1) = −(1−b)h(b) and s_n'(b,0) = b h(b) with h > 0. So the derivative of q s(b,1) + (1−q) s(b,0) is h(b)(b − q), and the rule is strictly proper; subclass 1 applies.
   - *Corollary.* For **normal** additive rules (Joyce 1998's setting), Theorem 2 is true. Example (b) has T(b) = b/2 + 1/6, which violates both extra conditions, as it must.
3. **N = 2, strictly convex or strictly proper rules in 𝒥_2 (PROVED).** (S) holds by §3.4(c) and (T) by §3.3.
4. **𝒥_N with face coherent admissibility and no ties (PROVED).** This is §3.4(d) together with (T).

## 4. What Joyce claims beyond our conclusion

- **Theorem 2(i): strict dominance by a coherent credence. FAILS in general,** by prop:joyce and §3.4(b), and also through ties (§3.3).
  - It holds for N = 2 up to ties, and for Σc < 1 up to ties.
  - LDG §5 does not recover it for 𝒥_N, because prop:strict needs the hypotheses of thm:bayes-finite.
  - The Σc < 1 strict statement comes from Joyce's own fixed-point argument, not from LDG §5.
- **On 𝒥_N^prop,** prop:proper and prop:strict recover strict (indeed uniform) dominance by coherent credences that are themselves undominated, without finiteness or truth-directedness. This answers Joyce's stated limitation about the log score (p. 288).
- **Corollary to Lindley (p. 287): incoherent iff weakly dominated by some credence.** Recovered and strengthened by prop:proper: the dominator is coherent and the dominance uniform. Joyce notes that Lindley "does not … show that any incoherent credence is always strictly dominated by a coherent one" (p. 287). prop:proper does.
- **Theorem 2(ii)** is (A).

## 5. Is LDG §8's treatment still accurate?

The mathematics of prop:joyce is correct under the current axioms (CHECKED), and the statement on line 516 that (S) fails for it is correct. The changes below are about precision and completeness.

**(a) Footnote to def:dominance (line 83).** Joyce's terminology is misdescribed.
- Old: "Schervish, Seidenfeld and Kadane~\cite{SSK09} and Joyce~\cite{Joyce} call our dominance ``weak dominance''. With finitely many worlds, their strict dominance is ours."
- New: "Schervish, Seidenfeld and Kadane~\cite{SSK09} and Joyce~\cite{Joyce} call our dominance ``weak dominance''. With finitely many worlds, the strict dominance of~\cite{SSK09} is ours, and Joyce's unqualified ``dominance'' is our strict dominance~\cite[p.~267]{Joyce}."

**(b) Line 803.**
- Old: "Joyce~\cite[Theorem~2, pp.~287--288]{Joyce} states that a finite, continuous, truth-directed loss on partition credences under which no coherent credence is dominated makes every incoherent credence strictly dominated by a coherent one. This is false as stated."
- New: "Joyce~\cite[Theorem~2, pp.~287--288]{Joyce} states that a finite, continuous, truth-directed loss on partition credences under which no coherent credence is dominated makes every incoherent credence inadmissible and strictly dominated by a coherent one (his `dominated' is our strict dominance, p.~267). This is false as stated, in two ways."
- Simpler alternative: keep the old sentence and change only "This is false as stated." to "This is false as stated, in two ways."

**(c) prop:joyce statement (line 810).** Add Joyce's standing permutation assumption, to pre-empt the objection that the loss is not admissible in his framework.
- Old: "This loss is continuous and truth-directed."
- New: "This loss is finite, continuous and truth-directed, and it is unchanged when the cells and the worlds are permuted together, as Joyce assumes~\cite[p.~271, n.~9]{Joyce}."
- Add to the proof's first paragraph: "Permuting cells and worlds together leaves the loss unchanged, since $s_{\sigma(i)}(\sigma x)=s_i(x)$ and $\sum_jx_j$ is symmetric."

**(d) Paragraph after the proof (line 822).** The diagnosis is incomplete: it omits the tie gap, and the page range is off.
- Old: "The failure lies in the sign claim of Joyce's Lemma~$1^*$ (pp.~295--296), for credences whose coordinates sum to more than one."
- New: "One failure lies in the sign claim of Joyce's Lemma~$1^*$ (p.~295), for credences whose coordinates sum to more than one. At $\nu_k$, the point $b^m$ with $m\ne k$ is closer to the truth than $c$ in the coordinates other than $k$ and $m$ but further in coordinate~$k$, so truth-directedness gives no sign; with two cells it gives the opposite sign."
- Keep the $b^3$ sentence. Replace the last two sentences ("So truth-directedness, … sufficient ones.") with:

> A second gap concerns ties. In Lemmas~2 and~$2^*$, a fixed point at which every difference $S(p,\nu_n)-S(c,\nu_n)$ vanishes does not contradict coherent admissibility, which excludes dominance of a coherent credence but not ties. With two cells, $L_1(x)\coloneqq(1-x_1+x_2)^2$ and $L_2(x)\coloneqq(1+x_1-x_2)^2$ define a finite, continuous, convex and truth-directed loss under which no coherent credence is dominated; but every credence $x$ is tied with the coherent credence $\bigl(\frac{1+x_1-x_2}2,\frac{1-x_1+x_2}2\bigr)$, so every credence, including $(0,0)$, is undominated. Here selection holds and closure under ties fails. Apart from ties, Joyce's argument for credences whose coordinates sum to less than one is sound: each such credence is strictly dominated by, or tied with, a coherent credence.
>
> Additivity, extensionality and strict convexity do not repair the theorem. With $N=3$, let $s(b,1)\coloneqq3(1-b)^2+4(1-b)$, $s(b,0)\coloneqq3b^2+2b$ and $L(x,\omega)\coloneqq\sum_ns(x_n,\one\{n=\omega\})$. This loss is finite, continuous, truth-directed, additive, extensional and strictly convex. For a prior $p$ its unique Bayes model is $x_n=\min(\max(2p_n-\frac13,0),1)$. Each coherent $b$ is therefore the unique Bayes model for the prior $\frac12b+\frac16(1,1,1)$, which charges every world, so no other credence weakly dominates $b$: every coherent credence is undominated and closure under ties holds. But $(\frac23,\frac23,0)$ is the unique Bayes model for $(\frac12,\frac12,0)$, so no other credence weakly dominates it.
>
> In the terms of Theorem~\ref{thm:argument}, Joyce's hypotheses give evaluability and coherent admissibility, but neither selection nor closure under ties. Strict propriety supplies both (Proposition~\ref{prop:proper}).

**(e) Intro (line 55).** "need not dominate every incoherent model" makes the loss the dominator, which reads oddly.
- Old: "A short counterexample shows that a truth-directed loss under which every coherent model is undominated need not dominate every incoherent model, contrary to a theorem of Joyce~\cite{Joyce}."
- New: "Short counterexamples show that, under a finite, continuous, truth-directed loss under which every coherent model is undominated, an incoherent model need not be dominated, contrary to a theorem of Joyce~\cite{Joyce}; this remains so for additive, strictly convex losses under which no two models are tied."
- If (d)'s second paragraph is not adopted, end the new sentence after "\cite{Joyce}".

**(f) Scope, open question (line 833).** It can now be sharpened.
- Old: "So is the question, within Joyce's framework, of which natural condition on a truth-directed loss makes every credence whose coordinates sum to more than one dominated by a coherent credence."
- New: "So is the question, within Joyce's framework, of which natural condition on a finite, continuous, truth-directed loss under which no coherent credence is dominated makes every credence whose coordinates sum to more than one weakly dominated by a coherent credence. Additivity, extensionality and strict convexity do not suffice (Section~\ref{sec:joyce}); strict propriety does."
- Optional: add "and so, for additive losses with continuously differentiable components and at least three cells, does $0/1$-symmetry", but only if the §3.5 item 2 argument is written into the paper.

**(g) Line 516.** Accurate as it stands. Optional addition after "no coherent credence weakly dominates $x^*$": "; for that loss (E), (A) and (T) hold."

**(h) No change needed.** def:truth-directed is equivalent on [0,1]^N to Joyce's p. 269 condition; the citation of Theorem 2 (pp. 287–288) is correct; the b³ computation is correct (L_1(b³) = 0.3799 > L_1(x*) = 0.3377).

## Appendix: checks

The scripts are /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r79/j79work/check.py and /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r79/j79work/check2.py. They check:
- the prop:joyce bounds and truth-directedness signs;
- the grid minimum 0.0422;
- the edge-prior Bayes models;
- for the additive example: the Bayes model (⅔,⅔,0) with V = 13/3; the coherent margin 1/6; and that each coherent b is the Bayes model for b/2 + 1/6, with maximum error 2·10⁻⁸ over 300 random b;
- the Lemma 1* sign for N = 2.
