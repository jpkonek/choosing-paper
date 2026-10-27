# REFL75 — reflection and null sets for the advice reading

Files (all in this folder):
- `REFL75_report.md` (this report)
- `REFL75_core.tex`: `../r74/core.tex` with the proposed changes spliced in. Compiles cleanly (`REFL75_build/REFL75_core.pdf`, no warnings, no overfull boxes).
- `REFL75_core.diff`: diff against `../r74/core.tex`.

## Answers first

1. **The equivalence: PROVED.** Advice is well defined on a.e.-classes of models exactly when μ and μ̌ have the same null sets, where μ̌(B) = μ(−B). It makes no difference whether negligible sets of choices are measured by μ or by μ+μ̌. A stronger form also holds: suppose 𝒩 is *any* σ-ideal such that "X = Y a.e. ⟺ the advice of X and Y differs only on a set in 𝒩". Then μ ~ μ̌ already follows. One more point: one-sided absolute continuity, μ̌ ≪ μ, is enough, because reflection is an involution and so μ̌ ≪ μ ⟺ μ ≪ μ̌. Under (M4), X ↦ α_X is a bijection between classes of models and classes of four-state advice maps that respect reflection. So models *are* advice systems, up to null sets.

2. **Cost of each option:**
   - **(a) μ ~ μ̌.** This is the minimal condition, and it is exactly what the interpretation needs. No proof uses it. It lets μ split a choice's weight unequally between its two orientations, as long as neither orientation gets zero weight.
   - **(b) μ = μ̌.** Strictly stronger. Like (a), it changes no theorem. Its extra cost is that it narrows which mass assignments the consolidation axiom (A4) and the integral ranking can use. Its bonus (CHECKED) is that the integral score becomes a per-choice score: ±½|f(ω)| for strict advice, and **0 for both silence and contradiction**. Under (a) alone, contradiction on f scores ½(1 − dμ̌/dμ)(f)·f(ω), which is generally not 0.
   - **(c) Unordered choices.** A distribution π over unordered choices is a measure on the symmetric Borel sets. It has exactly one symmetric extension μ_π to oriented choices: split each choice's weight in half (PROVED). Any extension μ of π has the same null sets as μ_π iff μ satisfies (M4), and (μ+μ̌)/2 = μ_π always. So "orientation does not affect negligibility" is literally (M4). The natural derived measure is the symmetric one.

3. **Compatibility with the paper:**
   - Theorem 4.1, Corollary 4.10, Proposition 5.5, Theorem 6.x and Corollary 6.x need **no change**. None of their proofs uses reflection, so they hold a fortiori under (M4).
   - The measure of Lemma `lem:measure` **as written** satisfies μ ~ μ̌ **iff** the set {g_k} is symmetric (−g_k ∈ {g_j} for every k). This is not guaranteed, so the measure fails (M4) in general (PROVED).
   - Fix (PROVED): use ν = Σ (w_k/2)(δ_{g_k} + δ_{−g_k}). Then μ is symmetric and still satisfies (M1), (M2), (M3), (M3′) and is atomless. Equivalently, (μ+μ̌)/2 is the lemma's construction with the doubled sequence.
   - For a *general* μ, symmetrising preserves (M1), (M3), (M3′) and atomlessness, but **not (M2)** (PROVED). (M2) for μ̌ is μ{max_{q∈Q} q = 0} = 0. This follows from (M2) under (M4), and when |Ω| ≤ 2 or Q is a polytope. It does **not** follow in general: there is an explicit counterexample with |Ω| = 3 and Q a disc. The lemma's construction does satisfy it (Fubini, as for (M2)).

4. **Recommendation:**
   - Adopt **(M4) Reflection: μ(B) = 0 iff μ(−B) = 0** as the official condition. Use it **only** in a new Proposition (`prop:advice`) that justifies the advice reading. Motivate it by (c): negligibility should not depend on orientation.
   - Make the existence measure symmetric (a one-line change), and record the symmetric case in a remark as the canonical one, with its per-choice score.
   - Add an example showing that (M1)–(M3′) do not imply (M4): μ_0 + δ_𝟙.
   - Do not impose μ = μ̌ globally: nothing needs it except the "contradiction scores 0" feature of the integral ranking, and whether that feature is wanted is a philosophical choice for the authors.
   - Paper-ready text is given below and is spliced into `REFL75_core.tex`.

---

## 1. The equivalence (PROVED)

**Setting.** For a model X and a gamble f, write α_X(f) = (𝟙_X(f), 𝟙_X(−f)) ∈ {0,1}². The four values are:
- (1,0): strict advice for f
- (0,1): strict advice against f
- (0,0): silence
- (1,1): contradictory advice

Let τ swap the two coordinates. Then α_X(−f) = τ α_X(f) for every f.

**Key identity.** For models X, Y put N := X △ Y. Then
  {f : α_X(f) ≠ α_Y(f)} = N ∪ (−N).    (∗)
The reason is that α_X(f) ≠ α_Y(f) iff X and Y differ at f or at −f.

**Proposition.** The following are equivalent:
- (a) μ̌ ≪ μ (for Borel B, μ(B) = 0 ⇒ μ(−B) = 0).
- (a′) μ ≪ μ̌.
- (a″) μ ~ μ̌, which is (M4).
- (b) X = Y a.e. ⇒ {α_X ≠ α_Y} is μ-null (choices measured by μ).
- (c) X = Y a.e. ⇒ {α_X ≠ α_Y} is (μ+μ̌)-null (choices measured in both orientations).
- (d) There is a σ-ideal 𝒩 ⊆ 2^E such that, for all models X and Y: X = Y a.e. ⟺ {α_X ≠ α_Y} ∈ 𝒩.

*Proof.*
- **(a) ⇔ (a′).** Assume (a) and suppose μ̌(B) = 0, that is, μ(−B) = 0. Apply (a) to −B: μ(B) = 0. The converse is symmetric. So (a), (a′) and (a″) coincide.
- **(a) ⇒ (c).** Let N be null, N ⊆ N₀ with N₀ Borel and μ(N₀) = 0. Put M := N₀ ∪ (−N₀). Then μ(M) = 0 by (a), and μ̌(M) = μ(−M) = μ(M) = 0 since M = −M. By (∗), {α_X ≠ α_Y} ⊆ M.
- **(c) ⇒ (b).** μ ≤ μ+μ̌.
- **(b) ⇒ (d).** Take 𝒩 = the μ-null sets. The "⇒" direction is (b). For "⇐": if N ∪ −N is null, then N is null.
- **(d) ⇒ (a).** Let B be Borel with μ(B) = 0.
  - With X = B and Y = ∅, (d) and (∗) give B ∪ −B ∈ 𝒩.
  - Now take X = −B, which is Borel and so a model, and Y = ∅. By (∗) the disagreement set is the same set B ∪ −B, which lies in 𝒩. So (d) gives −B = ∅ a.e., that is, μ(−B) = 0. ∎

**Remarks.**
- (d) needs no orientation-invariance assumption on 𝒩. Asking only that "the model determines the advice and the advice determines the model" already forces (M4).
- The one-way requirement "X = Y a.e. ⇒ advice agrees off 𝒩" is satisfiable trivially by a huge 𝒩 (for example 𝒩 = 2^E). That is why the right formulation is either (b)/(c), where the choices are measured by μ or μ+μ̌, or the two-way requirement (d).
- **Measurability.** Without (M4), −X need not even be μ-measurable, so α_X need not be measurable. Under (M4), −X is a model whenever X is: write X = B ∪ M with B Borel and M ⊆ M₀ null; then −M ⊆ −M₀, which is null.

**Bijection (PROVED).** Under (M4), X ↦ [α_X] is a bijection from classes of models onto classes of measurable α : E → {0,1}² that satisfy α(−f) = τα(f) for a.e. f.
- *Injective.* X △ Y ⊆ {α_X ≠ α_Y}, and this holds with no assumption on μ.
- *Surjective.* Let X := {α₁ = 1}, and let Z := {f : α(−f) ≠ τα(f)}, which is null (and Z = −Z). For f ∉ Z, α_X(f) = (α₁(f), α₁(−f)) = (α₁(f), α₂(f)) = α(f).

**The failure, concretely (PROVED).** Let μ := μ₀ + δ_𝟙, with μ₀ any atomless measure satisfying (M1)–(M3).
- μ still satisfies (M1), (M2) and (M3′): P_Q(𝟙) = 1 ≠ 0, and μ_c = μ₀.
- {−𝟙} is null; {𝟙} has mass 1.
- D_S and D_S ∪ {−𝟙} are the same model. But on the choice 𝟙 (sure gain vs nothing) the first gives strict advice for and the second gives contradictory advice, and that choice has positive mass.
- So Theorem 4.1's hypotheses do not secure the interpretation.

## 2. Costs of the three options

### (a) μ ~ μ̌, i.e. (M4)
- **Theorems.** No cost. Every result is proved for all μ satisfying its stated conditions, so adding (M4) only shrinks the class of μ for which the interpretation is claimed.
- **Interpretation.** μ may still weight "f is desirable" and "−f is desirable" differently, provided neither weight is zero where the other is positive.
- **Integral ranking.** Let r = dμ̌/dμ, which exists under (M4). Then
  m_ω(X) = ½∫[𝟙_X(f) − r(f)𝟙_X(−f)] f(ω) dμ(f),
  so contradictory advice on f scores ½(1 − r(f))f(ω). This is generally ≠ 0 and has either sign (CHECKED).
- (M4) also gives (M2) ⇒ (M2̄) (see §3). So the boundaries of *both* the strict-for region {P_Q > 0} and the strict-against region {P̄_Q < 0} of a coherent model are null, where P̄_Q(h) := max_{q∈Q} q(h).

### (b) μ = μ̌
- Implies (a). The extra cost is that it restricts the masses used by (A4) and by the integral ranking. The theorem itself is unaffected.
- **Gain (CHECKED):** for symmetric μ, ∫g dμ = ∫g(−·) dμ gives
  m_ω(X) = ½∫(𝟙_X(f) − 𝟙_X(−f)) f(ω) dμ(f).
  Per choice:
  - strict advice for f contributes +½ f(ω)
  - strict advice against f contributes −½ f(ω) = ½(−f)(ω)
  - silence contributes 0
  - contradiction contributes 0
- So at ω, correct strict advice earns ½|f(ω)|, wrong strict advice loses ½|f(ω)|, and no usable advice earns nothing. This is a clean accuracy reading. It also bears on the auditor's §2 point about contradictory advice: under symmetric μ the integral ranking treats contradiction exactly like silence. Whether that is wanted is a philosophical choice.

### (c) Unordered choices
A set of unordered choices {f, −f} is the same thing as a symmetric set B = −B. A distribution over unordered choices is therefore a finite measure π on 𝒮, the σ-algebra of symmetric Borel sets. Symmetric Borel functions are 𝒮-measurable.

- **Symmetric extension (PROVED).** μ_π(B) := ∫ ½(𝟙_B(f) + 𝟙_B(−f)) dπ(f) is a Borel measure. It is symmetric, and it agrees with π on 𝒮.
  - *Uniqueness.* If μ is symmetric and agrees with π on 𝒮, then μ(B) = ½∫(𝟙_B + 𝟙_{−B}) dμ. The integrand is 𝒮-measurable, so this equals μ_π(B).
- **Any extension (PROVED).** Let μ be any Borel extension of π, meaning any rule for orienting the weight, for example the image of π under a Borel orientation selector. Then μ(B ∪ −B) = π(B ∪ −B) = 2μ_π(B), so μ ≪ 2μ_π always. Moreover, μ ~ μ_π ⟺ μ satisfies (M4):
  - (⇐) If μ(B) = 0, then μ(−B) = 0, so μ_π(B) = 0. If μ_π(B) = 0, then μ(B ∪ −B) = 0.
  - (⇒) μ_π is symmetric, so its null sets are reflection-invariant.
  - A selector that sends every choice to a fixed half-space typically violates (M4).
- **Every μ comes from its unordered shadow (PROVED).** (μ+μ̌)/2 = μ_π with π = μ|_𝒮, since ∫½(𝟙_B + 𝟙_{−B}) dμ = ½(μ(B) + μ(−B)).
- **What is natural.** The auditor's demand that "choosing an orientation for {g,h} should not change whether the opportunity is negligible" is exactly (M4). The orientation-neutral way to put weight on oriented choices is the equal split, μ_π, which is symmetric. So (c) gives a principled *derivation* of (b) as the canonical case and of (a) as the general condition, rather than an assumption imposed for convenience.
- **Not checked:** how mass equalities in margin triples translate into π-masses when G_i meets −G_j. When a set G contains no pair f, −f, μ_π(G) = ½π(G ∪ −G).

## 3. Compatibility with the paper

**Theorem 4.1 and Corollary 4.10.** No change. They use (M2) and (M3′) only, and the proofs never reflect a set. Adding (M4) restricts the hypotheses, so they hold a fortiori.

**Lemma `lem:measure` as written (PROVED).** μ = Φ_*(ν⊗λ) with ν = Σ w_k δ_{g_k}.
- μ is concentrated on the lines L_k = g_k + ℝ𝟙.
- For g ∈ E₀, μ(g + ℝ𝟙) = ν{g}, because E₀ ∩ ℝ𝟙 = {0}.
- Hence, if −g_k ∉ {g_j}, the line −L_k is μ-null while μ̌(−L_k) = μ(L_k) ≥ w_k > 0.
- More fully, since λ is symmetric: μ(B) = 0 ⟺ λ{t : g_k + t𝟙 ∈ B} = 0 for all k; and μ̌(B) = 0 ⟺ the same holds with −g_k in place of g_k.
- So μ ~ μ̌ iff {g_k} = −{g_k}. Symmetry (μ = μ̌) holds iff in addition the weights agree on g and −g.
- The lemma does not choose the sequence, so as stated it **does not** secure (M4).

**Fix (PROVED).** Take ν := Σ_k (w_k/2)(δ_{g_k} + δ_{−g_k}).
- ν is still a probability measure with full support and finite first moment, and it is symmetric.
- Φ(−g, −t) = −Φ(g, t), and ν⊗λ is invariant under (g,t) ↦ (−g,−t). So μ(−B) = μ(B).
- (M1), (M2), (M3) and atomlessness have unchanged proofs.
- This is exactly (μ_old + μ̌_old)/2 when the old sequence is reused.

**Symmetrising a general μ: what survives.** Let σ := (μ+μ̌)/2.
- **(M1)** survives: ∫‖h‖ dμ̌ = ∫‖−h‖ dμ.
- **(M3)** survives: −W is open whenever W is.
- **Atoms and diffuse part:** A_σ = A_μ ∪ −A_μ, and σ_c = (μ_c + (μ_c)ˇ)/2 ≥ μ_c/2. The reason is that μ_c gives no mass to the countable set −A_μ. Hence:
  - **(M3′)** survives;
  - **atomlessness** survives.
- **(M2)** for σ ⟺ (M2) for μ and (M2̄) for μ. Here
  (M2̄): μ{P̄_Q = 0} = 0 for every credal Q,
  because μ̌{P_Q = 0} = μ(−{P_Q = 0}) = μ{P̄_Q = 0}. This is the condition in the brief.
- **When (M2) implies (M2̄) (PROVED):**
  - under (M4), since −{P_Q = 0} is null whenever {P_Q = 0} is;
  - when Q is a polytope conv{q₁, …, q_k}, since {P̄_Q = 0} ⊆ ∪_i {q_i = 0} and each {q_i = 0} is null by (M2) for {q_i};
  - in particular for every Q when |Ω| ≤ 2.
- **The lemma's construction satisfies (M2̄) for any sequence:** P̄_Q(g + t𝟙) = P̄_Q(g) + t, so the same Fubini argument applies.

**Counterexample: (M2) does not imply (M2̄) (PROVED).**

*Setting.* Ω = {1,2,3}, E = ℝ³. States are probability vectors. Let u = (⅓,⅓,⅓), let P be the orthogonal projection onto 𝟙^⊥, and let Q := {u + v : v ⊥ 𝟙, |v|₂ ≤ 1/6}. Q lies in the simplex because 1/6 < 1/√6. Then
  P̄_Q(h) = u·h + |Ph|/6.

*The measure.* Let C := {−u + w : w ⊥ 𝟙, |w|₂ = 2}. On C, P̄_Q = −⅓ + 2/6 = 0. Let ρ be normalised arc length on C. It is compactly supported and atomless.

*Claim: ρ{P_{Q′} = 0} = 0 for every credal Q′.*
- Let c = −u + w_c ∈ C with P_{Q′}(c) = 0. Pick q′ = u + a ∈ Q′ attaining the minimum, so a ⊥ 𝟙. Then:
  - q′(c) = 0;
  - C_{Q′} ⊆ {q′ ≥ 0}, since q′ ≥ P_{Q′} ≥ 0 on C_{Q′};
  - on C, q′(−u + w) = −⅓ + a·w =: f(w).
- **Case A: a ∥ w_c.** Then f(w_c) = 0 forces a = w_c/12, so q′ = q_c, the unique maximiser over Q at c. Now f(w) = −⅓ + w_c·w/12 < 0 for every w ≠ w_c on the circle. So C ∩ C_{Q′} = {c}, a single point.
- **Case B: a not parallel to w_c (and a ≠ 0, since f(w_c) = 0).** Then the derivative of f along the circle at w_c is nonzero. So f < 0 on an open arc on one side of c, and that arc misses C_{Q′}. Hence c is not a Lebesgue density point of the closed set C ∩ C_{Q′}.
- If any point of C ∩ {P_{Q′} = 0} falls in Case A, the whole set is a single point. Otherwise every point is a non-density point of C ∩ C_{Q′}. By the Lebesgue density theorem the set is ρ-null either way.

*Conclusion.* Let μ := μ₀ + ρ, with μ₀ the lemma measure on ℝ³.
- μ satisfies (M1), (M2) and (M3′), and is atomless.
- μ{P̄_Q = 0} ≥ 1, so μ̌ and (μ+μ̌)/2 violate (M2).
- μ(−C) = 0: ρ(−C) = 0, and each line g_k + ℝ𝟙 meets the plane {σ = 1} in exactly one point, while μ₀ is atomless. So μ also violates (M4).
- Interpretive reading: for this μ, a coherent model D_Q has a non-negligible set of choices sitting exactly on the boundary between its strict-against region and its silence region.

**Integral ranking (§5) and repair (§6).** No change needed. They use (M1) and (M2) and never reflect. Corollary `cor:existence` should list (M4) among the properties of its measure. That is free once the lemma measure is symmetric. Only one further point bears on interpretation, and it is not a mathematical gap: the per-choice score under symmetric μ given in §2(b).

## 4. Recommendation and paper-ready text

**Recommendation.**
- Adopt (a) as the official condition (M4), motivated by (c).
- Make the existence measure symmetric, which is case (b), and note the symmetric score in a remark.
- (M4) is used **only** for the interpretation (Proposition `prop:advice`), and in **no** proof.
- Keep the theorem's quantifier as it is: "every μ satisfying (M2) and (M3′)". The advice reading is claimed for those μ that also satisfy (M4).

**Changes (all spliced into `REFL75_core.tex`).**

(i) In Definition `def:measure`, after (M3):
```latex
  \item[(M4)] \emph{Reflection:} for every Borel set $B\subseteq E$, $\mu(B)=0$ if and only if
  $\mu(-B)=0$.
\end{itemize}
Since $B\mapsto-B$ is an involution, (M4) holds as soon as $\mu(B)=0$ implies $\mu(-B)=0$ for
every Borel $B$. Every \emph{symmetric} measure, one with $\mu(-B)=\mu(B)$ for every Borel $B$,
satisfies (M4). Under (M4), $-X$ is null whenever $X$ is null; and (M2) then also gives
$\mu\{h:\max_{q\in Q}q(h)=0\}=0$ for every credal set $Q$, because this set is
$-\{P_Q=0\}$.
```

(ii) At the end of the "uses" paragraph in Definition `def:atoms`:
```latex
Condition (M4) is used only in
Proposition~\ref{prop:advice}, which concerns the reading of models as advice; no other result
uses it.
```

(iii) Lemma `lem:measure`:
```latex
For every gamble space $E$ there is an atomless, symmetric finite Borel measure on $E$ that
satisfies (M1), (M2) and (M3), and hence (M3$'$) and (M4).
```
In its proof, replace ν by
```latex
$\nu\coloneqq\sum_k\frac{w_k}2(\delta_{g_k}+\delta_{-g_k})$, a Borel
probability measure on $E_0$ with full support, $\int\|g\|\,d\nu<\infty$ and $\nu(-B)=\nu(B)$
for every Borel $B$.
```
and append
```latex
Symmetric: $\Phi(-g,-t)=-\Phi(g,t)$, and $\nu\otimes\lambda$ is invariant under $(g,t)\mapsto
(-g,-t)$ because $\nu$ and $\lambda$ are; so $\mu(-B)=\mu(B)$, and (M4) holds.
```

(iv) A new subsection "Models as advice" after Definition `def:models`, containing:
- Definition `def:advice` (Advice): the four states, the reflection rule, and the fact that coherent models never give contradictory advice;
- Proposition `prop:advice`: the equivalence (a)–(d) and the bijection, with the proof from §1;
- Remark `rem:unordered`: unordered choices, μ_π, (M4) as orientation-independence of negligibility, and the symmetric score formula;
- Example `ex:noreflection`: μ₀ + δ_𝟙.

The full LaTeX is in `REFL75_core.tex` (search for `\subsection{Models as advice}`). It is too long to duplicate here. The diff is in `REFL75_core.diff`.

(v) Corollary `cor:existence` and its proof: "(M1), (M2), (M3′) and (M4)".

**Optional, not spliced.** The circle counterexample from §3 could become a footnote to the sentence about (M2) in (i): "(M2) alone does not give this when |Ω| ≥ 3." It is not needed for the paper's argument. I would leave it out unless a referee asks why (M4) is stated separately rather than derived.

## Status labels
- **PROVED (hand):**
  - the equivalence (a)–(d) and the bijection;
  - μ̌ ≪ μ ⟺ μ ≪ μ̌;
  - the μ₀ + δ_𝟙 example;
  - the characterisation of when the lemma measure satisfies (M4), and the symmetric fix;
  - what symmetrisation preserves;
  - (M2) ⇒ (M2̄) under (M4) or for polytopes;
  - the circle counterexample;
  - uniqueness of the symmetric extension, and "any extension μ ~ μ_π ⟺ (M4)".
- **CHECKED (computation):**
  - the symmetric-score formula;
  - the contradiction score under (M4) alone;
  - compile of `REFL75_core.tex`.
- **Not checked:** how the masses in a margin triple read in terms of π when G_i ∩ (−G_j) ≠ ∅. This bears on the interpretation of (A4) only.
