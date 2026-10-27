# REF72 — Referee report on the two-world counterexample

27 October 2026. Sources read: BRIEF72.md, AUDITOR_reply_1016.md §1, GUIDANCE_after_r71.md §§3, 5–7, and app.tex §2 (setting), §6.1–6.2 (Definition `def:ranking`, Lemma `lem:guidedeverywhere`, Proposition `prop:protect`, the dominance definitions).

Overall verdict: **I could not break the counterexample. It is correct.** Its general form is stated and proved in Part II. I found one defect in how the brief states the axioms (item 0). It does not affect the example.

---

## Part I. Verdicts

**0. The brief's (G) contradicts its (R) as written. WRONG as stated; the fix is trivial.** BRIEF72 states (G) as "if the change Y→X is guided at ω, then X ≻_ω Y". A change between a.e.-equal models adds and removes only null sets, so it is guided at every world. Then (G) demands X ≻_ω X, while (R) demands a tie. Read literally, the class 𝓡 is empty. The intended reading is the one in app.tex, requirement (1): strict guidance applies only when X ≠ Y a.e. I use that reading throughout.

**1. R_{s'} ∈ 𝓡. PROVED.**
- (R) and (I): the verdict at ω depends only on the change (A, B) modulo null sets. Guidance, the scores and availability to a coherent model all depend only on (A, B). The choice of the world that refuses is a fixed rule applied to (A, B): the least world at which the change is not guided.
- (G): a non-null change guided at ω has a strictly positive score increment at ω. The refusal clause only acts at worlds where the change is *not* guided, so it never blocks a guided change.
- (SC): every accepted comparison between distinct models strictly raises s'_ω. So no chain can be reversed. Distinct models are never tied.
- (P): a model that weakly dominates a coherent model C and differs from it makes a change that C itself could make. Such a change raises the score at every world, so it is refused at one world. Contradiction.

The guidance-protection lemma (app.tex Lemma `lem:guidedeverywhere`) mentions no score: it concerns sets only. **CHECKED.** For a Gaussian on R², μ{P_S = 0} = μ{min(h₁, h₂) = 0} = 0, since that set is two half-lines. **CHECKED.** With finitely many worlds the hypothesis is **not needed at all** (PROVED, Lemma 1 below). Guidance uses strict inequalities, so a change guided at every one of finitely many worlds adds only gambles in the open positive orthant D_S.

Null sets are handled correctly everywhere (CHECKED). Models are a.e.-classes. A, B, guidance, availability (B ⊆ C a.e. and μ(A ∩ C) = 0) and ∫ f_ω dμ are all invariant under null modifications. Coherence is invariant by definition.

**2. Properties of X*. PROVED.**
- X* is the unique a.e. maximiser of s'_1 + s'_2. The zero set of φ(h) = h₁ + f(h₂) is two rays, which is a null set.
- X* = D_{(1/3, 2/3)} ∪ D_{(2/3, 1/3)}. It is the union of two half-planes, an open cone of angle about 216.9° > 180°.
- X* is not a.e. equal to any D_Q, for any credal set Q ⊆ Δ₂ (singletons and Q = S included). The Walley boundary convention (adding {h ≥ 0, h ≠ 0}) and the closed version C_Q differ from D_Q by null sets, so they change nothing.
- X* is strictly preferred to every Y ≠ X* a.e. at some world.

**3. Extensions and maximal members.**
- Every (E-strict) extension of R_{s'} leaves X* undominated. PROVED; this is immediate and uses no axioms.
- When Ω is finite, unions of chains preserve (R), (G) with strictness, (I), (SC), (P), and also (TC) and closure under ties. PROVED.
- So Zorn's lemma gives a maximal member of 𝓡 that extends R_{s'}. PROVED.
- *Is the maximal member needed?* The statement "X* is undominated under every E-strict extension of R_{s'}" needs no Zorn. But to refute the stated objective, which quantifies over *maximal members* of 𝓡, one needs at least one maximal member above R_{s'}. Otherwise "every maximal extension" could be vacuous. So Zorn (finite Ω) is genuinely used, and it is available. R_{s'} itself is not claimed to be maximal; I have not checked whether it is (UNCLEAR, and irrelevant).

**4. General version. PROVED** (Proposition 3).
- Setting: n ≥ 2 worlds, and any per-world scores s'_ω(X) = ∫_X f_ω dμ with f_ω integrable, f_ω > 0 a.e. on {h_ω > 0} and f_ω < 0 a.e. on {h_ω < 0}.
- Hypotheses: some nonzero weight vector π ≥ 0 has μ{Σ π_ω f_ω = 0} = 0, and the set X_π = {Σ π_ω f_ω > 0} is incoherent. A sufficient condition for incoherence is that X_π is not a.e. equal to any convex cone.
- Full support of π is **not needed**. Any nonzero π ≥ 0 works.
- The example defeats (TC), because (SC) implies (TC) and chain unions preserve (TC). It also defeats every property Π possessed by all E-strict-maximal members of 𝓡: a maximal member above R_{s'} has Π and leaves X_π undominated. PROVED.

**5. Closure under ties. PROVED: it changes nothing.**
- R_{s'} has no ties between distinct models, so it satisfies closure under ties trivially.
- With finite Ω, chain unions preserve closure under ties. So the class 𝓡 + (closure under ties) has maximal members above R_{s'}, and X* is undominated under each of them.
- I have not determined whether every maximal member of 𝓡 *without* that axiom satisfies closure under ties (UNCLEAR). The counterexample does not need to know.

**6. Infinite Ω. The obstacle is stated precisely; the counterexample does not need infinite Ω.**
- Unions of chains still preserve (R), (G), (I) and (SC), which are conditions on each world separately.
- (P) and closure under ties are conjunctions over all worlds. When Ω is infinite, a union can contain Y ⪰_ω C at every ω with witnessing stages unbounded in the chain. Then the union weakly dominates C (or ties with it at every world) although no stage does.
- So the Zorn argument fails as stated. Whether maximal members exist for infinite Ω is open (UNCLEAR).
- The counterexample is two-world, and a theorem claimed for arbitrary Ω must cover finite Ω. So the infinite-world gap does not rescue the objective.

**7. What the example does *not* settle.** Maximality under ordinary inclusion (E-incl) is untouched. An inclusion-extension may add Y ⪰_ω X* at the very world where X* was strictly preferred, so X* can be dominated there. I make no claim about that branch.

**8. Numerical illustration. NUMERICS (Monte Carlo, 4×10⁶ Gaussian draws).**
- Take Y = {h₁ + h₂ > 0}. Then Y ⊆ X*, and the change Y → X* adds A = X* \ Y.
- Estimated increments: s'_1-increment ≈ −0.0143 and s'_2-increment ≈ +0.0486. So X* ≻_2 Y and not X* ⪰_1 Y.
- The identity X* = {h₁ + 2h₂ > 0} ∪ {2h₁ + h₂ > 0} held on every draw.
- Sign check (PROVED): on A, the increment at world 1 equals ∫_{A∩{h₂<0}} (h₁ + h₂) dμ < 0 by swap symmetry, and the increment at world 2 is positive because 2h₁ + h₂/2 > 2h₁ + h₂ > 0 there.

---

## Part II. Proposition and proof (paper-ready)

### Setting

Let Ω = {1, …, n} with n ≥ 2, E = ℝⁿ, and μ a finite Borel measure on E. A *model* is a μ-measurable subset of E, and models that agree up to a μ-null set are identified. Write Δ for the probability simplex. For a nonempty closed convex Q ⊆ Δ (a *credal set*), put P_Q(h) = min_{q∈Q} q·h and D_Q = {h : P_Q(h) > 0}. A model is *coherent* if it equals some D_Q up to a null set. Each D_Q is an open convex cone, closed under addition because P_Q(x + y) ≥ P_Q(x) + P_Q(y). It contains the open positive orthant D_Δ = {h : min_ω h_ω > 0} and contains no h with max_ω h_ω < 0.

The *change from Y to X* adds A = X \ Y and removes B = Y \ X. A model C *could make* it if B ⊆ C a.e. and μ(A ∩ C) = 0. The change is *guided by ω* if A ⊆ {h_ω > 0} and B ⊆ {h_ω < 0} a.e.

A *ranking* assigns to each world ω a relation ⪰_ω on models. X ≻_ω Y means X ⪰_ω Y and not Y ⪰_ω X. Y *dominates* X if Y ⪰_ω X at every world and Y ≻_ω X at some world. A model is *undominated* if no model dominates it.

The class 𝓡 consists of the rankings satisfying:

- **(R)** models equal a.e. are tied at every world;
- **(G)** if the change from Y to X is guided by ω and X ≠ Y a.e., then X ≻_ω Y;
- **(I)** whether X ⪰_ω Y holds depends only on the pair (X \ Y, Y \ X), up to null sets;
- **(SC)** no chain X₁ ⪰_ω X₂ ⪰_ω ⋯ ⪰_ω X_k has X_k ≻_ω X₁;
- **(P)** every coherent model is undominated.

A ranking R' *extends R preserving strict preferences*, written R ⊑ R', if at every world each comparison accepted by R is accepted by R', and each strict preference of R is a strict preference of R'. This relation is a partial order on rankings. *Closure under ties* is the further condition that a model tied at every world with an undominated coherent model is itself an undominated coherent model.

### Lemma 1 (guidance at every world)

A non-null change that some coherent model could make is not guided by every world. No condition on μ is needed.

*Proof.* Suppose the change adding A and removing B is guided by every world, and D_Q could make it. Since Ω is finite, A ⊆ ⋂_ω {h_ω > 0} = D_Δ ⊆ D_Q a.e. But μ(A ∩ D_Q) = 0, so A is null. Likewise B ⊆ ⋂_ω {h_ω < 0} a.e., which is disjoint from D_Q, while B ⊆ D_Q a.e. So B is null. ∎

(With infinitely many worlds the intersection argument only gives inf h ≥ 0. This is why app.tex Lemma `lem:guidedeverywhere` needs μ{P_S = 0} = 0. That condition holds for every measure with the null sets of Lebesgue measure.)

### Lemma 2 (maximal extensions exist for finitely many worlds)

Let R₀ ∈ 𝓡. There is a member of 𝓡 that is maximal for ⊑ and extends R₀. The same holds for the class obtained by replacing (SC) with the three-model condition (TC), and for either class with closure under ties added.

*Proof.* Let (Rⁱ)_{i∈I} be a nonempty chain for ⊑ in 𝓡 above R₀. Let R^∪ accept X ⪰_ω Y iff some Rⁱ does.

*R^∪ is an upper bound.* Suppose X ≻ⁱ_ω Y. For j ⊒ i, X ≻ʲ_ω Y holds, so Y ⪰ʲ_ω X fails. For j ⊑ i, Y ⪰ʲ_ω X fails because ⪰ʲ_ω ⊆ ⪰ⁱ_ω. Hence X ≻^∪_ω Y. So every Rⁱ ⊑ R^∪.

*Each axiom survives in R^∪.* Each axiom forbids a configuration of finitely many comparisons, some required to hold and some required to fail. If such a configuration occurred in R^∪, each comparison that holds would hold from some stage onward. Each comparison that fails in R^∪ fails at every stage. Taking the latest of the finitely many stages involved, the configuration would occur in one Rⁱ, which is impossible. Concretely:

- (R), (G) (including its strict part, by the upper-bound step), (I), (SC) and (TC) are conditions on one world and finitely many comparisons.
- (P): if Y dominated a coherent C in R^∪, the n comparisons Y ⪰_ω C would all hold at some stage. The failing comparison C ⪰_{ω₀} Y fails at every stage. So Y would dominate C there.
- Closure under ties: a tie at every world with a coherent C involves 2n comparisons. So it already occurs at some stage, where the model is therefore coherent. By (P) for R^∪ it is undominated.

The set {R ∈ class : R₀ ⊑ R} is nonempty, and every chain in it has an upper bound in it. Zorn's lemma gives a maximal element. This element is maximal in the whole class, because anything extending it also extends R₀. ∎

The proof uses finiteness of Ω only for (P) and closure under ties.

### Proposition 3

Let f_1, …, f_n be μ-integrable functions on E with f_ω > 0 a.e. on {h_ω > 0} and f_ω < 0 a.e. on {h_ω < 0}. Put s'_ω(X) = ∫_X f_ω dμ. Suppose some nonzero π ∈ [0, ∞)ⁿ has μ{Φ = 0} = 0, where Φ = Σ_ω π_ω f_ω, and suppose that X_π = {Φ > 0} is incoherent. Then:

(a) there is a ranking R' ∈ 𝓡 under which, for every model Y ≠ X_π a.e., some world ω has X_π ≻_ω Y;

(b) X_π is undominated under every ranking R with R' ⊑ R;

(c) there is a member of 𝓡 that is maximal for ⊑ and under which X_π is undominated. The same holds with (TC) in place of (SC), and with closure under ties added. More generally, if every ⊑-maximal member of 𝓡 has some property Π, then 𝓡 restricted to Π contains a ranking under which X_π is undominated.

*Construction.* For the change adding A and removing B, write d_ω(A, B) = s'_ω(A) − s'_ω(B). Call the change *protected* if it is non-null, some coherent model could make it, and d_ω(A, B) > 0 at every world. By Lemma 1, a protected change is not guided by some world. Let ω(A, B) be the least such world. Define R' by X ⪰_ω Y iff the change from Y to X, adding A and removing B,

- is null, or
- satisfies d_ω(A, B) > 0 and is not the case "protected and ω = ω(A, B)".

Every ingredient is unchanged when A or B is altered by a null set, so the relation is well defined on models.

*R' ∈ 𝓡.*
- (R): a null change is accepted in both directions.
- (I): the verdict is a function of (A, B).
- (G): let the change be non-null and guided by ω. Then f_ω > 0 a.e. on A and f_ω < 0 a.e. on B, with A ∪ B non-null, so d_ω(A, B) > 0. Since ω(A, B) is a world that does not guide the change, ω ≠ ω(A, B). Hence X ⪰_ω Y. The reverse change has increment −d_ω(A, B) < 0 and is non-null, so it is refused. Hence X ≻_ω Y.
- (SC): if X ⪰_ω Y and X ≠ Y a.e., then s'_ω(X) > s'_ω(Y). A chain X₁ ⪰_ω ⋯ ⪰_ω X_k therefore has s'_ω(X₁) ≥ s'_ω(X_k). Suppose X_k ≻_ω X₁. Then X_k ≠ X₁ a.e., since otherwise X₁ ⪰_ω X_k by (R). So s'_ω(X_k) > s'_ω(X₁), a contradiction.
- (P): let C be coherent and suppose Y ⪰_ω C at every world. If Y ≠ C a.e., the change from C to Y is non-null. C itself could make it: it removes C \ Y ⊆ C and adds Y \ C, which is disjoint from C. Being accepted at every world, it has d_ω > 0 at every world. So it is protected, and it is refused at ω(A, B), a contradiction. Hence Y = C a.e. Such a Y is tied with C at every world, so it does not dominate C.

*X_π is preferred to each rival somewhere.* Let Y ≠ X_π a.e. The change from Y to X_π adds A = X_π \ Y and removes B = Y \ X_π, and

  Σ_ω π_ω d_ω(A, B) = ∫_A Φ dμ − ∫_B Φ dμ.

Here Φ > 0 on A, and Φ < 0 a.e. on B because {Φ = 0} is null. Since A ∪ B is non-null, the sum is strictly positive. So d_ω(A, B) > 0 for at least one ω with π_ω > 0.

- If d_ω ≤ 0 at some world, the change is not protected. It is then accepted at every world where d_ω > 0, and there is at least one such world.
- If d_ω > 0 at every world, the change is refused at no more than one world. Since n ≥ 2, it is accepted at some other world.

At a world ω where it is accepted, d_ω > 0 and the reverse change has increment −d_ω < 0, so Y ⪰_ω X_π fails. Thus X_π ≻_ω Y. This proves (a).

*(b) and (c).* If R' ⊑ R, the strict preferences in (a) persist in R. So for each Y ≠ X_π a.e., Y ⪰_ω X_π fails at some world, and Y does not dominate X_π. A model equal to X_π a.e. is tied with it everywhere. This proves (b).

For (c), apply Lemma 2 to R'. R' satisfies (TC), because (SC) implies it. R' satisfies closure under ties, because it has no ties between distinct models. Then apply (b). The final sentence of (c) follows because the maximal member above R' has Π. ∎

*Remarks.*
1. X_π is the unique maximiser of Σ π_ω s'_ω up to null sets. The proof shows this along the way.
2. If f_ω(h) = w(h) h_ω with a single positive weight w common to all worlds, then X_π = {π·h > 0} is coherent. The construction then yields nothing, in line with the lead's note that common weights only change μ. The example needs world-dependent distortion.

### Example 4 (two worlds)

Take n = 2, μ the standard Gaussian on ℝ², f₁(h) = h₁, f₂(h) = f(h₂) with f(t) = 2t for t ≥ 0 and f(t) = t/2 for t < 0, and π = (1, 1). Put φ(h) = h₁ + f(h₂) and X* = {φ > 0}.

The hypotheses of Proposition 3 hold:

- f₁ and f₂ have the required signs, and |f_ω(h)| ≤ 2‖h‖ is integrable.
- {φ = 0} is the union of the rays through (−2, 1) and (1, −2), which is null.
- X* = {h₁ + 2h₂ > 0} ∪ {2h₁ + h₂ > 0}. To see this, note that on {h₂ ≥ 0} the second half-plane is contained in the first, and on {h₂ < 0} the first is contained in the second.
- X* is incoherent. Suppose X* = D_Q a.e.
  - *First, X* ⊆ D_Q.* If x ∈ X* \ D_Q, pick q ∈ Q with q·x ≤ 0. Then {h ∈ X* : q·h < 0} is open. It is nonempty because it contains x − t(1, 1) for small t > 0. It is disjoint from D_Q. So it is a non-null subset of X* \ D_Q, which is impossible.
  - *Second, a contradiction.* a = (−3/2, 1) and b = (1, −3/2) lie in X*, since φ(a) = 1/2 and φ(b) = 1/4. Hence a + b = (−1/2, −1/2) ∈ D_Q. D_Q is open and φ(a + b) = −3/4 < 0, so some ball around a + b lies in D_Q \ X*. That ball has positive measure, a contradiction.
  - This covers every credal set Q, including singletons and Q = Δ. The boundary conventions C_Q (adding {P_Q = 0}) and D_Q ∪ {h ≥ 0, h ≠ 0} differ from D_Q by Lebesgue-null sets, so they do not matter.

Hence X* is strictly preferred, under the ranking of Proposition 3, to every other model at some world. It is undominated under every extension of that ranking that preserves strict preferences, including a maximal one, which exists by Lemma 2.

In plain terms, X* accepts exactly the gambles that at least one of two precise probability assignments, (1/3, 2/3) and (2/3, 1/3), finds favourable. That union is not convex, yet it maximises the total of two scores, each of which rewards accepting gambles that pay off at its world and rejecting gambles that lose there.

### Remark 5 (infinitely many worlds)

Lemma 1 then needs μ{P_S = 0} = 0, as in app.tex. Lemma 2 fails at (P) and at closure under ties. A union of a chain can contain Y ⪰_ω C at every world ω while the stages that supply these comparisons have no upper bound in the chain. Then Y weakly dominates C in the union, or is tied with C at every world, although no stage shows this. Whether ⊑-maximal members of 𝓡 exist when Ω is infinite is open. Example 4 uses two worlds, so this question does not affect it.
