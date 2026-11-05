# P79 report: Pettigrew (2022), "Accuracy-first epistemology without additivity", Philos. Sci. 89, 128–151

## Results first

| Condition | Verdict for Pettigrew's class (continuous, strictly proper I : C × W → [0,∞], W finite) |
|---|---|
| (E) evaluability | **HOLDS** (PROVED). Every I is defined on all of C. |
| (A) coherent admissibility | **HOLDS** (PROVED), in the strong form: under *every* admissible I, every p ∈ P is undominated, so C_L = P. |
| (S) selection | **HOLDS** (PROVED). Route: Theorem `thm:bayes-finite` with c_p := p, which is a case of Corollary `cor:closed-choice`. Bayes choice for p itself; lower semicontinuity from continuity along P; Ω finite, so no compact family needed. |
| (T) closure under ties | **HOLDS** (PROVED). No credence function other than p has the loss profile of p ∈ P. Ties among distinct *incoherent* credence functions do occur, but (T) does not concern them. |

The whole class satisfies the conditions; no subclass fails. LDG needs less than Pettigrew assumes: lower semicontinuity of p ↦ I(p,i) **on P only**, not continuity on all of C; and only that each p be the unique Bayes model for itself, which is Pettigrew's strict propriety.

Things the author must know:
1. **Pettigrew's proof of Theorem 1 has a gap when losses can be infinite** (CHECKED). His framework allows losses in [0,∞], and his own example, the enhanced log score, takes the value ∞. For W = {w1,w2} and c = (c(∅), c({1}), c({2}), c(W)) = (0, 0, 0.5, 1), his Lemma 5 projection is c* = δ_{w2}, and I(c*,1) = ∞ = I(c,1). So c* does not strictly dominate c at w1. The step "D(w^i,c) ≥ D(w^i,c*) + D(c*,c), D(c*,c) > 0, hence D(w^i,c) > D(w^i,c*)" fails when both sides are ∞. Lemma 5(ii) also takes a limit of an expression containing ∞ − ∞. **The theorem itself is true**: p_ε = (ε, 1−ε) strictly dominates c for small ε. LDG's Proposition `prop:proper`, last claim, through `prop:strict`(b), proves it, with uniform dominance. So LDG's "contains" claim is correct, and LDG in fact repairs the infinite-valued case.
2. `prop:proper` and `prop:strict`(b) say "continuous" for [0,∞]-valued maps. For the enhanced-log case this must mean continuity **into [0,∞] with its order topology**, because boundary probabilities have infinite loss. Please say so explicitly (see §5).
3. Minor: as printed, Pettigrew's non-additive example LSE (p. 133) is negative at the truth and not proper (CHECKED numerically). The intended score is the Bregman divergence of φ(x) = log(1 + Σ_X e^{x(X)}), which is strictly proper. This does not affect LDG.
4. The §8 text is accurate. It needs only small precision edits and one sentence linking it to Theorem `thm:argument` (§5 below).

---

## 1. The paper's setting, precisely

**Worlds.** W = {w1,…,wn}, finite. "We assume W is finite" (p. 132).

**Models.** F is the set of all subsets of W. C is the set of all functions c : F → [0,1], with no constraints. In particular c(∅) and c(W) are free.

**Coherent class.** P ⊆ C consists of the probabilistic c: p(⊤) = 1, and p(A ∨ B) = p(A) + p(B) for disjoint A and B. Then p(∅) = 0, and p ↦ (p({w_i}))_i is an affine bijection P → Δ_W. It is a homeomorphism, using the topology of pointwise convergence on F (footnote 5).

**Losses.** "An inaccuracy measure is a function I : C × W → [0, ∞]" (p. 132; the closed bracket at ∞ was checked in the PDF). Infinite values are allowed, for example by the enhanced log score L*.

**Conditions** (NC, p. 137: "We will assume only that inaccuracy measures satisfy continuity and strict propriety").
- *Continuity*: "For each world w_i, I(c, i) is a continuous function of c." This is continuity on all of C. The topology on [0,∞] is not stated; the extended (order) topology is the only reading that admits L*.
- *Strict Propriety*: "For all p in P, Σ_i p_i I(c,i) is minimized uniquely, as a function of c, at c = p." Here c ranges over **all of C**, so p is the unique minimiser among all credence functions. The 0·∞ convention is left implicit. With 0·∞ = 0, which is LDG's convention, strict propriety makes p·I(p) finite.
- Additivity is **not** assumed. That is the point of the paper. Examples it endorses: Brier, enhanced log, LSE, and Lewis–Fallis's asymmetric spherical rule.
- Lemma 4(ii) silently uses I(w^i,i) = 0. This is harmless for Theorem 1: the term cancels as long as I(w^i,i) < ∞, which strict propriety at p = w^i gives.

**Main theorems** (p. 138ff).
- **Theorem 1.** "Suppose I is continuous and strictly proper. If c is not in P, there is c* in P, such that I(c*,i) < I(c,i) for all w_i in W." This is strict dominance by a probabilistic credence function. It is the theorem LDG cites.
- **Theorem 2** (chance dominance). If c ∉ cl(A⁺), the closed convex hull of the set A of possible chance functions, then some c* ∈ cl(A⁺) has Σ_i ch_i I(c*,i) < Σ_i ch_i I(c,i) for all ch ∈ A.
- **Theorem 3** (diachronic, sums of two scores). Not cited by LDG; see §6.

**Bridge principle** (Worldly dominance): "If there is c* such that, for all possible worlds w_i, I(c*,i) < I(c,i), then c is irrational." This is relative to the legitimate measure I. Pettigrew states only the incoherent-is-irrational direction. He never states that probabilistic credences are undominated, although his Lemma 4(i) implies it.

**Proof method.** He uses the restricted divergence D_I(p,c) = p·I(c) − p·I(p) on P × C (Lemma 4). Lemma 5 takes the projection q of c onto P that minimises D_I(·,c) and proves a generalised Pythagorean inequality. Theorem 1 follows by evaluating at the vertices w^i.

## 2. Translation into LDG

- Ω := W (finite).
- M := C = [0,1]^F. The probability vectors in Δ := Δ_W are identified with P via p(X) := Σ_{w_i∈X} p_i.
- 𝒞 := P.
- 𝔏 := the set of all I : C × W → [0,∞] that are continuous (into [0,∞]) and strictly proper. Any nonempty subfamily, including a singleton {I}, works equally well, since every condition below is verified for each I separately.
- M_L := C for every L = I ∈ 𝔏.
- The ranking is the loss ranking of I: c ⪯_i c′ iff I(c,i) ≤ I(c′,i).

Bayes models (Definition `def:bayes`): V(π) = inf_{c∈C} π·I(c), with expected loss summed over supp π, that is, 0·∞ = 0. Strict propriety says exactly: **for every p ∈ Δ, p is a Bayes model for p, and the only one**, and V(p) = p·I(p) < ∞. Finiteness holds because C has more than one element and the strict inequality p·I(p) < p·I(c) forces the left side to be finite.

## 3. The conditions

Fix I ∈ 𝔏.

**Lemma A (C_L = P).** PROVED. Let p ∈ P, and suppose c weakly dominates p, so I(c,i) ≤ I(p,i) for all i. Then p·I(c) ≤ p·I(p) = V(p) < ∞, so c is a Bayes model for p, and c = p by uniqueness. So no model dominates p, and P ⊆ C_L. Conversely C_L ⊆ 𝒞 = P by definition. Hence C_L = P. This uses neither continuity nor additivity.

**(E) HOLDS.** M_L = C = M for every I. If 𝔏 is taken to be the whole class, it is nonempty (the Brier score).

**(A) HOLDS.** By Lemma A, every p ∈ P is an undominated coherent model of every I ∈ 𝔏. This is stronger than (A) requires.

**(T) HOLDS.** Suppose m is tied at every world with some p ∈ C_L = P, so I(m) = I(p). Then p·I(m) = p·I(p) = V(p), so m is a Bayes model for p, and m = p by uniqueness. So C_L is closed under ties. This is the "loss-profile form" in Corollary `cor:bayes-coherent`(c).

*Ties among distinct credence functions.* These do occur, but only between incoherent ones. Example (Brier score, W = {w}): F = {∅, W}, c = (0.3, 0.6) and c′ = (0.4, 0.7) both have loss 0.25. Ties between a probability and any other credence function are impossible, as just shown. So (T) holds for every I in the class. Prop `prop:profiles` is not needed.

**(S) HOLDS.** Route: Theorem `thm:bayes-finite`, which LDG notes is a case of Corollary `cor:closed-choice`; equivalently Corollary `cor:bayes-coherent`(b),(c). Assignment: c_p := p for p ∈ Δ.
- *Loss ranking on finite Ω*: yes.
- *Bayes choice*: c_p = p is a Bayes model for p itself, whose support is supp p. This is strict propriety.
- *Competitiveness on supp p*: follows from the Bayes choice by Lemma `lem:bayes-competitive`, since loss rankings are complete.
- *Closed comparison sets / lower semicontinuity*: p ↦ I(p,i) is the composition of the affine homeomorphism Δ → P ⊆ C with c ↦ I(c,i), which is continuous into [0,∞]. So it is continuous into [0,∞], and every sublevel set {p : I(p,i) ≤ a} is closed. Hence {p : c_p ⪯_i m} = {p : I(p,i) ≤ I(m,i)} is closed: it is all of Δ when I(m,i) = ∞ and a sublevel set otherwise.
- *Compact family / linked sets*: not needed, since Ω is finite. (If wanted: Θ = Δ, σ_Ω = id.)
- *Assigned models are undominated coherent*: yes, by Lemma A.

So the hypotheses of `cor:closed-choice` hold with assigned models in C_L, which is (S).

*Weaker hypotheses suffice for LDG* (CHECKED). Continuity on C \ P is never used. Only lower semicontinuity of p ↦ I(p,i) on P is needed for (S), and continuity on P is needed for the uniform-dominance refinement.

*Nearby variant.* Suppose strict propriety is weakened to profile-strict propriety (Definition `def:propriety`: every Bayes model for p has profile I(p)). Then (E), (A) and (S) still hold, (T) can fail, and Prop `prop:profiles` gives the identification by profiles. This is the first claim of `prop:proper`.

**Conclusion.** Theorem `thm:argument` applies to 𝔏, and to every nonempty subfamily. The rationally permissible credence functions are exactly the probabilities. Every non-probabilistic c is dominated, under every I ∈ 𝔏, by some p ∈ P. U_I = P for every I.

## 4. What Pettigrew proves beyond LDG's conclusion, and whether §5 recovers it

- **Strict dominance by a coherent model.** Theorem 1 gives c* ∈ P with I(c*,i) < I(c,i) at every world. LDG's §5 recovers this, and gives **uniform** dominance with c* having finite losses (the same as strict here, since Ω is finite). Route: `prop:strict`(b), with V finite, c_p = p a Bayes model for p, and p ↦ I(p,i) continuous into [0,∞]. Every incoherent c is a Bayes model for no prior, by uniqueness. This is exactly the last claim of `prop:proper`. RECOVERED (PROVED).
- **The dominator is undominated.** c* ∈ P = C_L, so it is an undominated coherent model. LDG gives the same.
- **Explicit dominator.** Pettigrew's c* is the D_I-projection of c onto P. LDG's is obtained non-constructively (KKM plus margins). This is not recovered, and does not need to be. Moreover, **the projection does not always work when losses are infinite** (CHECKED):
  - Take the enhanced log score L*(c,i) = Σ_X [w^i(X)(−log c(X)) + c(X)], W = {w1,w2}, and c = (c(∅), c({1}), c({2}), c(W)) = (0, 0, 0.5, 1).
  - Then L*(c,1) = ∞ and L*(c,2) = 1.5 + log 2 ≈ 2.193.
  - D(x,c) = ∞ for every x ∈ P with x_1 > 0, and D(δ_{w2},c) ≈ 0.193. So the unique projection is c* = δ_{w2}, whose L*(c*,1) = ∞. Strict dominance fails at w1.
  - Some coherent c does strictly dominate: p_ε = (ε, 1−ε) has L*(p_ε,1) < ∞ and L*(p_ε,2) = 2 − log(1−ε) < 2.193 for small ε.
  - So the theorem is true but its proof needs repair for infinite-valued I. LDG's proof covers that case. Pettigrew's Lemma 5 also asserts existence of a minimiser from strict convexity alone. Existence needs lower semicontinuity of D_I(·,c), which follows from upper semicontinuity of V, as in the proof of `prop:strict`(b). For finite-valued continuous I that is immediate.
- **Not proved by Pettigrew.** He does not state that probabilities are undominated, which is LDG's (A) and Lemma A. This follows from his Lemma 4(i) but is not stated.
- **Theorem 2** (chance dominance) is a different result. It is not used by LDG; see §6.

## 5. Is LDG §8's treatment still accurate? Exact edits

`prop:proper` itself is correct under the current axioms, and its proof goes through for Pettigrew's class (CHECKED). The paragraph after it (line 674) reads:

> "This contains Pettigrew's Theorem~1~\cite{Pettigrew}. There the models are the credence functions on all subsets of a finite $\Omega$, the probabilities among them correspond to the points of $\Delta$, expected losses are read with $0\cdot\infty=0$, and uniqueness and continuity on all credence functions are assumed. Continuity cannot simply be dropped~\cite{SSK09}; a discontinuous strictly proper score such as that of Figure~\ref{fig:profiles}(b) is not lower semicontinuous on the probabilities."

Assessment:
- **Sentence 1** is accurate (PROVED above): the last claim of `prop:proper` gives Theorem 1, and more.
- **Sentence 2** is accurate in substance. Two points of precision. First, the 0·∞ convention is LDG's reading; Pettigrew leaves it implicit while allowing values in [0,∞]. Second, "continuity" must be continuity into [0,∞] if his infinite-valued examples are to be covered.
- **Sentence 3** is accurate as a general remark. However, Figure 1(b) is a score on event forecasts f ∈ [0,1]², not on credence functions on all subsets, so "such as" slightly overstates the fit.
- **Missing:** the link to the current axioms (E), (A), (S), (T), and to Theorem `thm:argument`. The paragraph was written when the result was read off directly.

**Replacement text** for the paragraph:

> This contains Pettigrew's Theorem~1~\cite{Pettigrew}. There the models are the credence functions on all subsets of a finite $\Omega$, the probabilities among them correspond to the points of $\Delta$, losses take values in $[0,\infty]$ (we read expected losses with $0\cdot\infty=0$, which he leaves implicit), and uniqueness of Bayes models and continuity, as maps into $[0,\infty]$, on all credence functions are assumed. Proposition~\ref{prop:proper} uses continuity only along the probabilities, and lower semicontinuity suffices for dominance. In the terms of Theorem~\ref{thm:argument}, let $\Lf$ be any nonempty family of such inaccuracy measures. Every member evaluates every credence function, which gives (E). Each member has $\C_L=\C$, which gives (A). Each meets the hypotheses of Theorem~\ref{thm:bayes-finite} with $c_p\coloneqq p$, which gives (S). Each is closed under ties, which gives (T). So the rationally permissible credence functions are exactly the probabilities. Pettigrew's proof projects $c$ onto the probabilities by a divergence. When losses can be infinite, as for the enhanced logarithmic score he considers, the projection can share an infinite loss with $c$ at some world. For instance, with two worlds, $c(\{w_1\})=0$, $c(\{w_2\})=\frac12$, $c(\Omega)=1$ and $c(\varnothing)=0$, the projection is $\delta_{w_2}$, and both have infinite loss at $w_1$. Proposition~\ref{prop:strict}(b) shows that a uniformly dominating probability exists in every case. Continuity cannot simply be dropped~\cite{SSK09}: a discontinuous strictly proper score of the kind in Figure~\ref{fig:profiles}(b) is not lower semicontinuous on the probabilities.

If the author prefers not to comment on Pettigrew's proof, delete the two sentences beginning "Pettigrew's proof projects" and "For instance". Everything else stands.

**Related small edits:**
- `prop:proper`, last sentence. Replace "or each $p\mapsto L(p,\omega)$ is continuous" with "or each $p\mapsto L(p,\omega)$ is continuous as a map into $[0,\infty]$".
- `prop:strict`(b). Replace "each $p\mapsto L(c_p,\omega)$ is continuous" with "each $p\mapsto L(c_p,\omega)$ is continuous as a map into $[0,\infty]$". The proof already handles this case: it uses continuity only at worlds in supp p, where losses are finite.
- Optional, in the intro (line 55): "The results recover theorems on proper scores of Pettigrew~\cite{Pettigrew}, …" is accurate as it stands.

## 6. Theorems 2 and 3 (not cited by LDG; for completeness)

**Theorem 2, translated.**
- Ω := A, the possible chance functions; may be infinite.
- M_L := C.
- L(c, ch) := Σ_i ch_i I(c,i).
- 𝒞 := cl(A⁺).
- For a finitely supported prior π on A, π·L(c) = p̄·I(c) with p̄ = Σ π_ch ch ∈ A⁺. By strict propriety, p̄ is the unique Bayes model for π.

(S) via `thm:bayes-infinite` (CHECKED):
- Θ := cl(A⁺), which is compact.
- c_θ := θ.
- Every finite F ⊆ A is linked, with σ_F(π) := p̄, which is continuous.
- Lower semicontinuity holds because θ ↦ Σ_i ch_i I(θ,i) is continuous into [0,∞].

**For finite-valued I**, all four conditions hold (CHECKED). If m weakly dominates θ ∈ cl(A⁺), take θ_n ∈ A⁺ with θ_n → θ. Then θ_n·I(m) ≤ θ_n·I(θ). In the limit θ·I(m) ≤ θ·I(θ), so m = θ. This gives C_L = cl(A⁺) and (T).

**For infinite-valued I, (A) can fail for a single measure** (CHECKED).
- Take the enhanced log score, W = {w1,w2}, and A = {(t, 1−t) : 0 < t ≤ ½}.
- δ_{w2} ∈ cl(A⁺) has L(δ_{w2}, ch_t) = ∞ for every t > 0.
- The probability (¼, ¾) has finite loss throughout, so it strictly dominates δ_{w2}.
- So a member of Pettigrew's permitted set cl(A⁺) is chance-dominated. This does not contradict his Theorem 2, which concerns only c ∉ cl(A⁺).
- (S), in the form requiring all c_θ to be undominated, then fails for Θ = cl(A⁺).
- *Nearby*: (A) holds for any family 𝔏 containing one finite-valued measure (e.g. Brier). Whether the projection argument for Theorem 2 survives infinite values is UNCLEAR. It has the same ∞ − ∞ gap as Theorem 1.

**Theorem 3** (diachronic; the loss of a prior–posterior pair is a sum of two inaccuracies): UNCLEAR, not analysed. Pettigrew himself notes that this sum is a remaining additivity assumption.
