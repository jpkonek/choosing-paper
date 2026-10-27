# N9. BRIEF5 Q2: explicit non-additive constructions for T1 (plateau designs)

13 Oct 2026. Labels: **PROVED** (full proof here), **CHECKED** (verified, proof sketched), **CONJECTURE**, **NUMERICS**.
Script: `n9py/checks.py` (NUMERICS only; no proof depends on it).
Standing: n = 3, T = T1 = D_K, K = (1−ε)u + εΔ, ε = 0.3, vertices v_j = (1−ε)u + εe_j, c = (1−ε)/3. Rankings are preorders,
one per world, on a decomposable domain, with strict (G), (IB) in the replacement form (comparisons depend only on
Z = {a_X ≠ a_Y} and the advice there), (LA), (S) in LDG's preorder sense, (C), (E), (LF) at T. Fact 0 = R2 Fact 0
(KKM: every model has a selected weak dominator; every undominated model is tied at every world with a selected one;
valid for preorders, LDG Thm kkm and rem:order).

---

## 0. Outcome

**Verdict: no construction. No ranking-level impossibility either.** Every plateau design tried fails, and the failures are
general lemmas, not artefacts of the designs. Three of them cover whole classes of designs. The general question for
arbitrary non-additive (IB) preorders stays open. What is still needed is pinned down in N9.9.

**N9.1 (PROVED) A plateau of the selection is free, so the literal test is empty.** Suppose any system satisfying all the
axioms has T undominated. Then some selection for the same system has u_p = T on a nonempty open set. Take
u′ = u∘φ with φ(p) = (1−λ(p))p + λ(p)p*, where λ: Δ → [0,1] is continuous, equals 1 near p* and 0 on ∂Δ (§2).
R10b Thm PL forbids a plateau of the **Bayes map**, a canonical object. It says nothing about selections. The
meaningful version of the brief's idea is therefore *thinness*: U_L near T should consist of T plus thin connecting
families, or, in lexicographic classes, the canonical lex-Bayes map should be constant on an open set.

**N9.2 (PROVED) Tie fibres are closed; edge families repel the target fibre.**
- (a) For every C ∈ C_L the set u^{-1}[C] = {p : u_p ~ C at every world} is closed. Consequently the selection takes
  uncountably many tie classes on every edge (Sierpiński).
- (b) **Lemma R.** Suppose X ≺_ω u_p for every ω ∈ S, with S ⊊ Ω. Then p has a neighbourhood on which no u_q is
  competitive on S. Moreover every interior q there has u_q ⪯_ω′ X for some ω′ ∉ S.
- (c) For T1, every point of P_T := u^{-1}[T] has a neighbourhood on which no selected model is competitive on any edge.
  So the "minimal thin design", in which U_L is [T] together with the three edge families, is impossible. Connecting
  families must consist of new models that are competitive on Ω only.

**N9.3 (PROVED under the hypothesis (A_T) of §3) Dominators accumulate at P_T from every gain direction.**
- Let W_k be a decreasing sequence of single-class exchanges from T with null intersection, and let ω be a gain world
  of the class.
- Then the closed sets D(W_k) = {p : u_p ⪯ T+W_k at every world} are nonempty and miss P_T, and dist(D(W_k), P_T) → 0.
- Along them u_{p_k} ≺_ω T.
- Without (A_T), the limit can be a *non-Archimedean neighbour* of T: weakly better at the gain worlds and
  infinitesimally worse at the loss worlds. Lexicographic rankings supply such neighbours.

**N9.4 (PROVED) Binary-domain normal form.** On R3's U-domain M_U = {X ⊆ U} (the evaluable models are the measurable subsets X of U), U = D_{K′}, K′ = u + s(K−u) (which has (LF) at T):
- each world's preorder is exactly a *qualitative measure* ≤_i on measurable subsets of U, applied to the world-i error
  sets E_i(X) = X △ P_i, where P_i = U ∩ {h_i > 0};
- ≤_i is a preorder, strictly monotone, and satisfies de Finetti cancellation A ≤ B ⇔ A∖B ≤ B∖A;
- (G) and (IB) are equivalent to these properties.

All designs below live on this domain unless stated.

**N9.5 (PROVED) Lex-IBU.** In a two-level lexicographic system with additive levels (F_i, S_i) satisfying (LA), (S), (C),
for every interior t the lex-t-Bayes model (minimise t·F, then t·S) is a.e. unique and coherent. This is R2 Lemma U
transferred; it needs no Bayes-for-index assumption on the selection.

**N9.6 (PROVED) Face-continuum theorem FC.** Take a two-level lex system with additive levels, a world i, and its
primary-optimal face 𝔐_i = argmin F_i. Suppose the secondary S_i trades off against another world's primary F_j on 𝔐_i,
in the following sense: the minimisers Y_λ of S_i + Σ_{l≠i} λ_l F_l over 𝔐_i are a.e. unique, improvable at j, and take a
continuum of F_j-values. Then **(S) fails, whatever the target.** Each Y_λ is undominated, and R2 Thm 7 allows only
countably many such F_j-levels. FC reproves R3 §5.4(i) as a special case.

**N9.7 (PROVED) Design A fails: the strongest plateau (T as primary ideal).** The *T-protective* lexicographic system of §4.2
has the following properties:
- strict (G) and (IB);
- (LF) at T1;
- T1 undominated and competitive on Ω;
- **every** interior lex-Bayes model equal to T1, i.e. a plateau of the canonical Bayes object on all of int Δ, which is
  exactly what R10b PL forbids for additive rankings;
- no additive weak extension at any world, so it is neither additive nor sandwiched.

It fails (S), by FC with i = 1, j = 2 (FC2 is visible in NUMERICS). More generally, any two-level lex system whose
lex-Bayes map is constant on int Δ makes that constant model the primary ideal (Prop 4.4), and then FC applies under
genericity.

**N9.8 (PROVED with an explicit witness) Design B fails: a free collar at ∂T.** Suppose the primary is blind (F-free) on a
neighbourhood Z of ∂T∖0 and error-strict at some point g ∈ int D_K ∖ Z.
- Then U_L contains the *decoupled* models X(t,b): primary-t-Bayes off Z and secondary-b-Bayes on Z, for independent
  interior t and b.
- With b → e_1 and t → e_2, X(t,b) is incoherent. Witness: h = (1, −0.875, 1) ∈ F_2, h′ = (1, 0.5, −0.6562) ∈ F_3, and
  h + h′ = (2, −0.375, 0.344) deep inside D_K, with normalised margin 0.168.
- Reason: lexicographic designs that let an additive secondary handle the target boundary *decouple* the two levels, and
  decoupling enlarges U_L (cf. R2 Prop 8). It does not thin it.

**N9.9 (CHECKED reduction, CONJECTURE status of residual) What is left, and why no impossibility proof.** Two-level lex
designs with no free region reduce (Prop 4.5) to an additive chart problem in which the chart vectors c_F(h) are only
*weakly* sign-respecting, with zeros allowed at any world, good~silence and bad~silence alike. This contains the
permitted-tie class of N1–N7, but N1/N6 do not cover bad~silence zeros.
- A ranking-level impossibility for general (IB) preorders would have to replace two things:
  - (i) the Archimedean step (A_T);
  - (ii) the per-problem chart structure: convexity and openness of R(h), and UVN.
- Both are additive or continuity inputs. Lemma R, N9.3 and FC are what survives at ranking level.
- Non-lexicographic, non-Archimedean preorders (ultrafilter or KPS-type) remain unexamined for T1. I give a heuristic
  (§6) for why closed sections are hard for them, but no theorem.

**Warm-up (§5).** No target is known for which additive coverage fails *only* because of the no-plateau theorem. PL
constrains the Bayes map, not coverage (N9.1 applies to additive systems too). The warm-up as posed therefore has no
instance among current results.

---

## 1. Setting and the binary normal form (N9.4)

Domain (R3 §5.1): U = D_{K′} with K′ = u + s(K−u), 0 < s < 1. Then cl D_K∖0 ⊆ U and U ∩ −U = ∅. This is the U-domain:
the evaluable models are the measurable subsets of U, M_U = {X ⊆ U measurable}. Since U never contains both g and −g, no
evaluable model gives contradictory advice. For g ∈ U, the advice range of the choice represented by g is {accept g, silence}; for
−g ∈ U it is {accept −g, silence}; if g ∉ U and −g ∉ U, every evaluable model gives no advice on that choice. (LF) holds at T with N = U. Coherent members are the D_M with M ⊇ K′. The world-i-best model is
P_i := U ∩ {h_i > 0} = D_{conv(K′ ∪ e_i)}, which is coherent. This is the vertex model forced by the vertex lemma.

At world i, on h ∈ U, accepting is good if h_i > 0 and bad if h_i < 0, and silence lies in between. Put
E_i(X) = X △ P_i, the set of problems where X's world-i advice is not the best in the advice range. X is pointwise at least as good
as Y at i iff E_i(X) ⊆ E_i(Y). Moreover E_i(X) △ E_i(Y) = X △ Y.

**Prop 1.1 (PROVED).** Preorders ⪯_i on M_U satisfying weak and strict (G) and (IB) correspond bijectively, via
X ⪯_i Y ⇔ E_i(X) ≤_i E_i(Y), to relations ≤_i on measurable subsets of U (mod null) that are:
- preorders;
- monotone: A ⊆ B ⇒ A ≤ B;
- strictly monotone: B∖A non-null ⇒ ¬(B ≤ A);
- cancellative: A ≤ B ⇔ A∖B ≤ B∖A.

*Proof.* X ↦ E_i(X) is a bijection of M_U onto the measurable subsets of U. Monotonicity is (G). For (IB): changing
the common part of X and Y changes E_i(X) and E_i(Y) only on the common part E_i(X) ∩ E_i(Y) or on the common complement.
So (IB) says that A ≤ B depends only on (A∖B, B∖A), which is cancellation. Conversely, cancellation gives (IB). ∎

**Exchanges.** For an exchange W from C (added set A ⊆ U∖C, removed set R ⊆ C), label h ∈ A by τ(h) = σ(h) (its sign
pattern) and h ∈ R by τ(h) = −σ(h). At world i the gain set is G_i = {τ_i = +} and the loss set is L_i = {τ_i = −}.

- C ⪯_i C+W ⇔ G_i ≤_i L_i.
- C+W ⪯_i C ⇔ L_i ≤_i G_i.
- Competitiveness of C on S: for every W, some i ∈ S has G_i ≤_i L_i.
- Undominatedness: no W has L_i ≤_i G_i at every i, strictly at some i.
- A *single-class* exchange has a constant label τ. It is a pure gain at the worlds where τ_i = + and a pure loss
  elsewhere.

## 2. The selection plateau is free (N9.1)

**Prop 2.1 (PROVED).** Suppose a system satisfies (LA), (S), (C) with selection u, and T ∈ C_L with K ⊂ int Δ and (LF). Then
there is a selection u′ for the same system with u′ = T on a nonempty open set.

*Proof.*
- By Fact 0(b), T ~ u_r at every world for some r. Replacing u_r by T leaves every section unchanged, by transitivity.
- r is interior. Otherwise T would be competitive on the proper face supp r, because competitiveness transfers along
  ties. But for S = Ω∖{k}, silencing T on the non-null set of accepted gambles with h_k > 0 > h_l for l ≠ k (near ∂T,
  where silence is in the advice range by (LF)) improves T pointwise and strictly at every world of S. By strict (G) this beats T strictly at every
  world of S, so T is not competitive on S.
- Let λ be as in N9.1 with p* = r. Then φ(p) is interior for interior p, and φ = id on ∂Δ, so supp φ(p) ⊆ supp p.
- Put u′ = u∘φ. Then {p : u′_p ⪯_ω m} = φ^{-1}{q : u_q ⪯_ω m}, which is closed.
- Competitiveness on supp φ(p) implies competitiveness on supp p. ∎

So any covering system, additive ones included, has plateau selections. R10b Thm PL, N3 PL_θ and N4 concern the
*Bayes* map, which is canonical for additive systems. For non-additive systems the natural canonical objects are U_L
itself and, in lexicographic classes, the lex-Bayes map. The tests below use those.

## 3. Ranking-level structure near the target fibre (N9.2, N9.3)

**Lemma 3.1 (closed fibres; PROVED).** For C ∈ C_L, u^{-1}[C] is closed.

*Proof.* Let p_k → p with u_{p_k} ~ C. The sections {q : u_q ⪯_ω C} are closed, so u_p ⪯_ω C at every ω. Since C is
undominated, u_p ~ C. ∎

*Consequence.* {u^{-1}[C]} partitions Δ into closed sets. u_{e_1} = P_1 and u_{e_2} = P_2 are not tied: P_1 ≺_1 P_2 by
strict (G). So by Sierpiński every edge meets uncountably many fibres. A plateau is one fibre with interior; the other
fibres may be thin.

**Lemma 3.2 (Lemma R; PROVED, any preorders).** Let X ≺_ω u_p for all ω ∈ S. Then p ∉ cl ∪_{ω∈S} A_ω(X), where
A_ω(X) = {q : u_q ⪯_ω X}. Hence some neighbourhood N of p has:
- (i) no u_q (q ∈ N) competitive on S;
- (ii) u_q ⪯_ω′ X for some ω′ ∈ supp q ∖ S, for each q ∈ N.

*Proof.*
- u_p ⋠_ω X for ω ∈ S, since X ≺_ω u_p. The sets A_ω(X) are closed, so their finite union misses a neighbourhood N of p.
- A model competitive on S would have u_q ⪯_ω X for some ω ∈ S, which fails on N. This gives (i).
- Competitiveness on supp q gives (ii). ∎

**Cor 3.3 (PROVED; T1, (LF)).** Every p ∈ P_T has a neighbourhood containing no index whose selected model is competitive
on an edge.

*Proof.* For the edge {1,2}, let X_{12} be T silenced on T ∩ {h_1 < 0, h_2 < 0} ∩ N. This set is non-null: for a > b > 0
the gamble (−a, −b, (0.5333a + 0.2333b)/0.2333) lies in relint F_1 of D_K. Silence is in the advice range there by (LF). X_{12}
pointwise improves T strictly at worlds 1 and 2. Apply Lemma 3.2 with S = {1,2}, and likewise for the other edges. ∎

*Consequence for thin designs.* Suppose U_L = [T] ∪ E_{12} ∪ E_{23} ∪ E_{13}, the edge families: the most economical design,
with the interior mapped into edge models off the plateau. Then points of ∂P_T would be limits of indices carrying edge
models, which Cor 3.3 forbids. So the minimal thin design is impossible. Every connecting family must contain models,
indexed arbitrarily close to P_T, that are competitive on Ω only. Lemma 3.2(ii) also gives a weak continuity at P_T:
near P_T, u_q ⪯_3 X_{12}(W) for each fixed silenced set W.

**Hypothesis (A_T) (Archimedean at T, world ω).** Let W_k be a single-class exchange sequence from T decreasing to a null
set, with ω a loss world of the class. If a model C satisfies C ⪯_ω T + W_k for all k, then C ⪯_ω T.

(A_T) holds for additive rankings, by dominated convergence. It fails for lex rankings with a primary that is blind on
the W_k.

**Prop 3.4 (dominator accumulation; PROVED under (A_T) at the loss worlds).** Let W_k be single-class exchanges from T,
decreasing with null intersection, whose class τ has a gain world.
- Then D_k = {p : u_p ⪯ T+W_k at every world} is nonempty and closed, D_k ∩ P_T = ∅, and dist(D_k, P_T) → 0.
- For p_k ∈ D_k, u_{p_k} ≺_ω T at every gain world ω.

*Proof.*
- Nonempty: Fact 0(a). Closed: a finite intersection of sections.
- At a gain world ω, T ⋠_ω T+W_k by strict monotonicity: W_k ≤ ∅ fails. So D_k ∩ P_T = ∅, and
  u_{p_k} ⪯_ω T+W_k ≺_ω T.
- Take a subsequence with p_k → p̄. At a loss world, for k ≥ j, T+W_k is pointwise at least as good as T+W_j, so
  u_{p_k} ⪯_ω T+W_j. Closedness gives u_{p̄} ⪯_ω T+W_j for every j, and (A_T) gives u_{p̄} ⪯_ω T.
- At gain worlds, u_{p_k} ⪯_ω T gives u_{p̄} ⪯_ω T.
- So u_{p̄} ⪯ T, and since T is undominated, u_{p̄} ~ T, i.e. p̄ ∈ P_T. ∎

So, under (A_T), arbitrarily close to P_T (in the index) there are selected, interior-only (Cor 3.3) models that are
strictly better than T at world i, for each i, and at each pair {i,j}, using classes {i} and {ij}. Counting alone does not
exclude three "legs" handling the six classes. A contradiction would need the quantitative exchange-rate structure across
locations on ∂T. That structure is additive (R10b, R15) and is exactly what a general preorder does not have. This is the
point where a ranking-level impossibility proof stops (§6).

## 4. Lexicographic designs

Class 𝓛₂ (R7 §1): world i ranks by lex(F_i, S_i), with F_i = ∫φ_i, S_i = ∫ψ_i measurable, integrable envelopes, φ_i
weakly guiding, and (φ_i, ψ_i) lexicographically strictly guiding. The rankings are complete with strict (G) and full
(IB). They are the natural non-Archimedean class in which (A_T) fails.

### 4.1 Lex-IBU (N9.5)

**Lemma 4.1 (PROVED).** In 𝓛₂ on a decomposable domain, with (LA), (S), (C): for interior t, any two lex-t-Bayes models agree a.e.,
and the lex-t-Bayes model is coherent.

*Proof.* Let B and B′ be lex-t-Bayes, differing on a non-null Z.
- Every splice is lex-t-Bayes, since the pointwise lex minimisers are interchangeable. As in R2 Lemma U, some splice E is
  incoherent.
- By Fact 0(a), some selected C has C ⪯_i E at every world. Lex comparisons give F_i(C) ≤ F_i(E) for every i.
- If some F_i(C) < F_i(E), then t·F(C) < t·F(E), since t is interior. This contradicts lex-optimality of E. So
  F(C) = F(E), and then S_i(C) ≤ S_i(E) for every i, with t·S equal. Hence S(C) = S(E).
- So C ~ E at every world, and (C) makes E coherent: contradiction.
- Coherence of the unique model follows by the same argument with E = B. ∎

So in 𝓛₂ every interior lex-Bayes model is undominated and coherent. This is R3 §2.2, made unconditional.

### 4.2 Design A: the target as primary ideal (N9.7)

**Definition (T-protective primary).** For an orientation h ∈ U (mixed, or nonnegative) and world i:
- if h ∈ T and h_i > 0: φ_i(h,0) − φ_i(h,+) = |h_i|. This is a strict reward for truth.
- if h ∈ T and h_i < 0: φ_i(h,+) = φ_i(h,0). This is a bad~silence tie.
- if h ∉ T and h_i < 0: φ_i(h,+) − φ_i(h,0) = |h_i|. This is a strict penalty.
- if h ∉ T and h_i > 0: φ_i(h,+) = φ_i(h,0). This is a good~silence tie.

Normalise φ_i(h,+) = 0 where a tie or reward applies. The secondary is ψ_i = (0, |h_i|, 2|h_i|) for (good, silent, bad).

**Prop 4.2 (PROVED).** On M_U, Design A has the following properties.
- (a) Strict (G) and (IB) hold, and (LF) holds at T.
- (b) T minimises every F_i, and {X : F(X) = F(T)} = {T}.
- (c) T is undominated and competitive on Ω.
- (d) The lex-t-Bayes model is T for **every** t ∈ int Δ, and also for every t whose support meets the positive set of
  every mixed h ∈ T and the negative set of every mixed h ∉ T.
- (e) At no world is there a strictly guiding additive L_i with X ⪯_i Y ⇒ L_i(X) ≤ L_i(Y) (no weak extension, so not
  sandwiched).
- (f) (S) fails.

*Proof.*
- (a) Both levels are integrals, which gives (IB). The composite is lex-strict, which gives (G).
- (b) Pointwise, T's choice is φ_i-optimal at every world, by the table. A mixed h ∈ T has a positive coordinate, where
  dropping h is strictly penalised. A mixed h ∉ T has a negative coordinate, where adding h is strictly penalised. So
  any X ≠ T on a non-null set has some F_i(X) > F_i(T).
- (c) For X ≠ T, pick i with F_i(X) > F_i(T). Then T ≺_i X. This gives competitiveness, and also X ⋠_i T, so X does not
  dominate T.
- (d) t·c_F(h) has T's sign for those t. Ties are null.
- (e) This is R2 Prop 4's argument. Take A := P_i made bad on a set Q ⊆ T ∩ {h_i < 0} of large measure. A is F_i-tied
  with P_i, and A ≺ any model with larger F_i. Take B := P_i silenced on a tiny set N ⊆ T ∩ {h_i > 0}. Then A ≺_i B, but
  L_i(A) − L_i(P_i) is at least the integral of the bad–good gap over Q, while L_i(B) − L_i(P_i) → 0 as μ(N) → 0.
- (f) Theorem FC below, with i = 1 and j = 2, using Lemma 4.3. ∎

**Theorem FC (face continuum; PROVED).** Take 𝓛₂ with additive levels on a decomposable domain M, and assume (LA), (S). Fix worlds
i ≠ j. Let 𝔐_i := argmin_M F_i; it is the decomposable subdomain of pointwise φ_i-minimisers. For λ ∈ (0,∞)^{Ω∖{i}}, let Y_λ
minimise Φ_λ := S_i + Σ_{l≠i} λ_l F_l over 𝔐_i. Suppose that, on some set Λ of λ's:
- (FC1) Y_λ is a.e. unique;
- (FC2) {F_j(Y_λ) : λ ∈ Λ} is uncountable;
- (FC3) each Y_λ is improvable at j: there is Z with F_j(Z) = F_j(Y_λ) and S_j(Z) < S_j(Y_λ).

Then there is a contradiction. No selection satisfies (S), whatever the target.

*Proof.*
- *Y_λ is undominated.* Let Z ⪯_l Y_λ at every l.
  - At world i, F_i(Y_λ) = min. So lex forces F_i(Z) = F_i(Y_λ), i.e. Z ∈ 𝔐_i, and S_i(Z) ≤ S_i(Y_λ).
  - At l ≠ i, F_l(Z) ≤ F_l(Y_λ).
  - So Φ_λ(Z) ≤ Φ_λ(Y_λ), and (FC1) gives Z = Y_λ a.e.
- By Fact 0(b), Y_λ is tied at every world with some selected u_p. A lex tie preserves F_j and S_j, so u_p is improvable
  at j with the same Z.
- R2 Thm 7 (R6/R7 form; needs only real-valued levels and (S)) makes {F_j(X) : X ∈ U_L improvable at j} countable.
  This contradicts (FC2). ∎

**Lemma 4.3 (FC1–FC3 for Design A, i = 1, j = 2; PROVED).**
- 𝔐_1 = {X : X ⊇ T ∩ P_1, X ⊆ T ∪ P_1}. The free set is Q_1 = (P_1∖T) ∪ (T∖P_1).
- A move on h ∈ Q_1 (add h ∈ P_1∖T, or drop h ∈ T∖P_1) gains |h_1| in S_1. It costs |h_l| in F_l for l ∈ J(h), where J(h)
  is the set of worlds l ≠ 1 with h_l < 0 (add) or h_l > 0 (drop).
- Y_λ moves h iff |h_1| > Σ_{l∈J(h)} λ_l|h_l|.
- (FC1): ties are null.
- (FC2): on the shell part {h ∈ P_1∖T : h_2 < 0 < h_3}, J = {2}. There the ratio |h_1|/|h_2| has a positive density on
  an interval (NUMERICS: (0, 2.28) for s = 0.9). So F_2(Y_λ) is continuous and strictly decreasing in λ_2 on an interval
  (NUMERICS: excess 0.0057, 0.0050, 0.0034, 0.0003, 0 at λ_2 = 0.2, 0.5, 1, 2, 5).
- (FC3): Y_λ ⊇ T ∩ P_1 ∩ {h_2 < 0}, which is non-null. There accepting is bad at 2 and F_2-tied with silence (row 2 of the
  table). Silencing a piece keeps F_2 and lowers S_2. ∎

**Prop 4.4 (a constant lex-Bayes map forces a primary ideal; PROVED).** In 𝓛₂ with no non-null F-free set (c_F(h) ≠ 0 a.e.),
suppose the lex-t-Bayes model is a fixed X* for every t ∈ int Δ. Then X* minimises every F_i.

*Proof.*
- For a.e. h, the lex chart {t ∈ int Δ : (t·c_F(h), t·c_S(h)) >_lex 0} contains int Δ or misses it. Since c_F(h) ≠ 0,
  this forces c_F(h) ≥ 0 or c_F(h) ≤ 0, with X*'s choice being the favoured one.
- So X*'s choice is φ_i-optimal pointwise at every i. ∎

*Reading.* Hence the strongest plateau, that of the canonical lex-Bayes object, always produces a Design-A-type system.
Such a system fails whenever FC1–FC3 hold on some face 𝔐_i, i.e. whenever the vertex direction P_i and the ideal X* are
separated by moves that cost another world's primary at a continuum of exchange rates. For T1 this is unavoidable on the
binary domain. P_1 ≠ T forces moves on Q_1. Each move on Q_1 is bad at some l ≠ 1, and F_l must penalise it, or X* = T
loses protection at l. A Σ_T-type "lock", leaving all Q_1-moves F-free, returns the problem to the secondary, which is
additive (Prop 4.5). The last step is **CHECKED**, not proved in full generality.

**Cross-check.** R3 §5.4(i) is FC with i = 1, j = 3: there 𝔐_1 = {F_1 = 0} and the multiplier family X_a. This
confirms that FC is the general form of that failure.

### 4.3 Design B: free collar at the target boundary (N9.8)

Idea: let a "global" primary (for instance a normalised-box loss, CSE) handle everything away from ∂T. Let the primary be
F-free (φ_l(h,·) constant for every l) on an open collar Z ⊇ ∂T∖0, so that the secondary alone decides near ∂T.

**Prop 4.5 (PROVED).** In 𝓛₂ with (LA), (S), let Z be F-free, and assume t·c_F ≠ 0 a.e. off Z for t in an open set Θ ⊆ int Δ.
For t ∈ Θ and b ∈ int Δ, let X(t,b) be the model that is primary-t-optimal off Z and S-b-Bayes on Z. Then X(t,b) is
undominated, hence selected up to a tie, hence coherent when (C) holds, or, without (C), equal to a selected model by
uniqueness.

*Proof.* Let Y weakly dominate X(t,b).
- F_l(Y) ≤ F_l(X) for every l, and t is interior, so t·F(Y) ≤ min. Hence F(Y) = F(X), and Y = X off Z, by pointwise
  uniqueness there.
- S_l(Y) ≤ S_l(X) for every l, and Y differs from X only on Z. So b·S(Y) ≤ b·S(X), and uniqueness on Z (ties null) gives
  Y = X.
- Fact 0(b) gives a selected model tied with X. Lex ties preserve every level, so the selected model minimises the same
  objectives and equals X. ∎

**Witness of incoherence (PROVED; numbers checked in `n9py/checks.py`).**
- Take h = (1, −0.875, 1), with v_2·h = 0, and h′ = (1, 0.5, −0.65625), with v_3·h′ = 0. Both are facet points of D_K,
  so they lie in Z, and h_1, h′_1 > 0.
- Their sum is g = (2, −0.375, 0.34375). Its lower prevision min_K m·g is 0.168‖g‖, so g lies deep inside D_K and outside
  a thin collar Z. Also g_2 < 0.
- Suppose the primary is error-strict at world 2 near g: c_F(·)_2 < 0 there. Let b → e_1. The S-charts accept a.e. point
  of small balls around h and h′, since c_S has the strict sign pattern of h. Let t → e_2 within Θ. The primary rejects
  a.e. point of a ball around g. So X(t,b) contains density neighbourhoods of h and h′ but misses one of h + h′.
- Since a coherent set is a convex cone, X(t,b) is incoherent, contradicting Prop 4.5.

*Reading.* This is R2 Prop 8's decoupling phenomenon in three worlds. With independent t and b, the undominated set
**grows** to a 4-parameter family. The design aimed at a thin U_L and produces the opposite.

### 4.4 Design C: no free set (reduction; CHECKED)

If c_F(h) ≠ 0 a.e., then for interior t the lex-t-Bayes model is a.e. the primary-t-Bayes model. By Lemma 4.1 these are
all coherent and undominated. So U_L contains an int Δ-indexed family with charts {t·c_F(h) > 0}. The c_F(h) are only
**weakly** sign-respecting: zeros are allowed at any world, for good~silence and for bad~silence alike.
- If this family is constant on all of int Δ, we are in Design A (Prop 4.4).
- If it is constant only on an open O ⊊ int Δ, the question is whether R10b PL survives zero patterns of c_F. N3 PL_θ
  shows that it survives good~silence zeros confined to bands, because Lemma M needs strictness at one facet point only.
  Bad~silence zeros (absent from NSI) remove the strict-badness inputs (Lemma FS, UVN(b), (a₋)_c ≤ 0). The status of
  this zero-pattern additive chart problem is **open**.
- A thin U_L is impossible in Design C regardless, since the lex-Bayes family is indexed by int Δ.

**CONJECTURE N9.** For T1 on decomposable domains, every 𝓛₂ system with (LA), (S), (C), (LF) either has a non-null free set
(Prop 4.5 then applies) or satisfies FC1–FC3 on some face, unless its primary-Bayes charts already form a strict-additive
cover of T1 near ∂T.

## 5. Warm-up

The brief asks for a simpler non-box interior target that additive rankings fail to cover *only* because of the no-plateau
theorem. By Prop 2.1, plateau-freedom of the Bayes map is never by itself an obstruction to additive coverage. Coverage
needs T to be the Bayes model at one prior, and the selection can be reparametrised. The additive no-gos for interior
targets that do exclude coverage use other inputs:
- R15 Thm 6.2: (DF), (ND), (NA_w);
- R2 Thm N: nesting;
- v3 App. C: three vertices, n ≥ 4.

So the warm-up has no instance among current results. The nearest honest analogue is the plateau of the canonical
lex-Bayes object, and there the answer is Design A: it exists (Prop 4.2(d)) and is then killed by (S) through FC. This
holds for every interior target T whose Q_1-shell supports a continuum of exchange rates, including every interior
triangle and box. So it is not a T1-specific phenomenon.

## 6. Does the conflict generalise? (ranking-level impossibility attempt)

What is ranking-level, i.e. holds for arbitrary preorders with (G), (IB), (S):
- vertex lemma (u_{e_i} = P_i);
- closed fibres (3.1);
- edge repulsion (3.2, 3.3);
- dominator accumulation (3.4), but only with (A_T);
- R2 Thm 7 and FC, but only for lexicographic real-valued levels.

What needs additivity or continuity, and has no preorder replacement found:
- (A_T): without it, limits of dominators are non-Archimedean neighbours of T, and nothing forces them to equal T.
- Per-problem chart structure: R(h) = {p : u_p accepts h} is open and convex for additive systems (R1 Prop 2.1). For
  preorders, closed sections constrain only comparisons of whole models. A chart can be arbitrary as long as the
  comparisons it induces are closed.
- UVN, Lemma FS and Lemma M all use continuity of pointwise minimisers in the prior.

Heuristic (not a theorem) for non-lex, non-Archimedean orders (ultrafilter or KPS type, Beyond Additive §3):
- Competitiveness of the interior-only models near P_T (Cor 3.3) needs, for every exchange W, a positive comparison at
  some world, chosen closed in p.
- In such orders, comparisons between nearby models are decided by "infinitesimal" ultrafilter events. These are not
  stable along index sequences, so closed sections would require the comparison pattern to be locally constant in p.
- A locally constant pattern is the staircase phenomenon again (Lemma 3.1 plus Sierpiński).

No proof is claimed.

**Precise residual.** For T1, a non-additive cover must:
- (a) use, near P_T, interior-only models (Cor 3.3);
- (b) violate (A_T), or contain dominators of every single-class perturbation accumulating at P_T (Prop 3.4);
- (c) if lexicographic with additive levels, have no free set meeting a neighbourhood of ∂T in the decoupled way of
  Prop 4.5, and have every face 𝔐_i degenerate in the FC sense, i.e. countably many F_j levels among improvable
  undominated models.

No design meeting (a)–(c) is known. Proving that none exists would include the open additive T1 problem as a special
case. That explains why no impossibility proof was obtained.

## 7. Use of the exact consistency test

Coverage after Neutral Abstention, thm:closure. In every design above, the conflict is a forbidden outcome of type (b): a
comparison C_p ⪯_i X with p outside the chosen closed section. Specifically:
- Design A: the comparisons u_q ⪯_2 Z, for improvable Y_λ ~ u_q, are forced at a continuum of primary levels. Their
  sections cannot all be closed (Thm 7).
- Cor 3.3: competitiveness at indices near P_T forces u_q ⪯_ω X_{12} for some ω ∈ {1,2}, at indices accumulating at p.
  Closing the section then installs T ⪯_ω X_{12}, reversing a strict (G) comparison (type (a)).
- Design B: the forced comparisons make X(t,b) undominated (rule 4), and it is incoherent (type (c)).

So the test was used in its intended role: the generated comparisons conflict, and each conflict has a finite
derivation.
