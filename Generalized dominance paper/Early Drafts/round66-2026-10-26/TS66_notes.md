# TS66 — Universal coverage on two-sided domains (26 Oct 2026)

Role: TS66 (BRIEF66). Labels: PROVED (proved here; not yet refereed) / CHECKED (exact rational computation) / CONJECTURE / NUMERICS. Every hypothesis is named where it is used.
Scripts: `ts66py/` (run each with `python3 -I <script>` from that folder; each writes a `.out` file).

## 0. Answers in brief

**(A) is reached.** The simple safe-improvement ranking of AUDIT_r66_extension §2 works on the full domain, and more generally on every *hull-closed* domain (§3.1). On ℝⁿ it is one ranking that covers **every** credal set, including precise, lower-dimensional and boundary ones.

1. **The rivals the round-65 proof misses are exactly those with Q_X = ∅** (Lemma 2.1, Remark 3.5). Equivalently, some finite non-negative combination of density points of X is a sure loss. When Q_X ≠ ∅, the round-65 proof works on the full domain once its one use of K′ (Step 2) is replaced by a point of Q_X.

2. **Lemma E (PROVED; CHECKED).** Q_X = ∅ holds iff some prior λ ∈ Δ makes the part of X it disapproves of a *net sure loss in Brier moment*:

     m(X ∩ {λ·h < 0}) ≪ 0.

   The proof is one minimax over subsets of X (Lyapunov).

3. **Safe strict improvement for every incoherent rival (Theorem 3.4, PROVED).** Let U be hull-closed; this includes ℝⁿ, V₀ := {h : h_l > 0 for some l}, every U ⊇ V₀, and every one-sided D_{K′}. Every incoherent X ∈ 𝓜_U then has a coherent N ∈ 𝓜_U with m(N) − m(X) ≫ 0 and a safe record r(N,X).
   - If Q_X = ∅, the proof is short: take λ from Lemma E, and do one relative minimax inside hull(X ∩ {λ·h > 0}).
   - **No shrink is needed in that case.** The removed part X∖N contains the net sure loss X ∩ {λ·h<0}, so no coherent model contains X∖N, and the record is safe automatically. This is the brief's "degenerate hull" mechanism, and the construction forces it.

4. **The naive defender can fail (CHECKED).** The naive defender is the full-domain Brier-minimax half-space {π₀·h > 0}. Two exact Case-2 rivals are found on which its record is **unsafe**: Q_{X∖N₀} ≠ ∅ and the witness mass is 0. The construction in item 3 is certified on both. So Lemma E is doing real work.

5. **Protection is free on every domain (Lemma 2.3, PROVED).** Pure guidance can never weakly dominate a coherent model nontrivially, two-sided or not. A record that is guidance at every world adds only sure gains and removes only sure losses. A coherent model already contains every sure gain and no sure loss.

6. **Which full domain FD-1 gives, and coverage there (Prop 5.2, Cor 5.3, PROVED).**
   - FD-1(b) gives U ⊇ V₀ a.e. It does not constrain U on the sure losses −ℝⁿ₊. Both V₀ and ℝⁿ are admissible, and so is everything in between. The dominance theorem holds for all of them.
   - **(LF) on U ⊇ V₀.** Write S_K := ⋃_{k∈K} supp k. (LF) holds at D_K iff either K ∩ relint Δ ≠ ∅, or U contains a.e. the sure losses in a neighbourhood of F_K := {h ≤ 0, h ≠ 0 : h_i = 0 for all i ∈ S_K}.
   - **On ℝⁿ: every credal set is covered, by one ranking.**
   - **On V₀: exactly the credal sets meeting relint Δ are covered.** This includes every precise {p} with p ∈ relint Δ and every lower-dimensional K through relint Δ.
   - D_K is always undominated, because every coherent model is.

7. **Consistency checks (PROVED).**
   - Plain Brier on ℝⁿ covers exactly the precise credal sets {p}, for every p ∈ Δ. The covering paper's Cor. "precise" states only p ∈ relint Δ: an understatement on ℝⁿ, but exact on V₀.
   - The simple ranking is a sub-relation of Brier, so it keeps more undominated models: all coherent ones.
   - For n = 2, every domain admitting a (G)+(GC) ranking is an open sector plus sure losses. Such domains are hull-closed, so the simple ranking is a universal cover on each of them.

**(B)/(C)** are not needed: no counterexample exists on hull-closed domains. What remains open is listed in §7. The main open item is two-sided domains that are **not** hull-closed, where some coherent model's trace on U is not coherent. For n ≥ 3 and targets meeting no edge, FD-1 already rules out every two-sided domain except U ⊇ V₀, so nothing is lost there.

---

## 1. Setting and named hypotheses

- **(Ω)** Ω = {1,…,n}, n ≥ 2. Gambles h ∈ ℝⁿ. Δ is the simplex. For S ⊆ Δ, D_S := {h : q·h > 0 ∀q ∈ S}. A *credal set* is a nonempty closed convex Q ⊆ Δ.
- **(M)** μ is a finite Borel measure on ℝⁿ with the null sets of Lebesgue measure and ∫|h| dμ < ∞. m(X) := ∫_X h dμ.
- **Domains.** A domain is a measurable U ⊆ ℝⁿ. Models 𝓜_U are the measurable X ⊆ U, modulo null sets.
  - V₀ := {h : h_l > 0 for some l} = ℝⁿ ∖ (−ℝⁿ₊).
  - A *full domain* is any U with V₀ ⊆ U a.e. It can be written U = V₀ ∪ E a.e. with E ⊆ −ℝⁿ₊ (sure losses and 0).
- **Coherence.** X is coherent if X = D_Q a.e. for a credal set Q (any Q: boundary, lower-dimensional and precise Q are allowed). 𝒞_U := {D_Q : D_Q ⊆ U a.e.}. Every D_Q ⊆ V₀, so on a full domain 𝒞_U = all D_Q.
- **Hull.** For measurable B: Q_B := {q ∈ Δ : q·h ≥ 0 for μ-a.e. h ∈ B}, which may be empty. When Q_B ≠ ∅, hull(B) := D_{Q_B}.
- **Records, guidance, safety** (BRIEF66).
  - For a change from Y to X, the record is (A,B) = (X∖Y, Y∖X), and d_ω(A,B) := m_ω(A) − m_ω(B).
  - (A,B) is *guidance at ω* if A ⊆ {h_ω > 0} and B ⊆ {h_ω < 0} a.e.
  - (A,B) *attacks* Z if B ⊆ Z a.e. and A ∩ Z is null.
  - (A,B) is *safe on U* if it attacks no member of 𝒞_U.
- **The simple ranking on U.** X ⪯_ω Y iff r(X,Y) is guidance at ω, or r(X,Y) is safe on U and d_ω(r(X,Y)) > 0.
- Requirements (G), (IB), (TC), (FCC), (Add), (GC), (C), (ID), (W) and (LF) are exactly as in the universal-coverage note, §2.

## 2. Basic lemmas

**Lemma 2.1 (hull with possibly empty Q; PROVED).** Let B be measurable and B_d its set of Lebesgue density points.
- (a) Q_B is closed and convex, and Q_B = {q ∈ Δ : q·b ≥ 0 for all b ∈ B_d}.
- (b) If Q_B ≠ ∅, then B ⊆ hull(B) a.e. For a credal set Q: B ⊆ D_Q a.e. ⟺ Q ⊆ Q_B ⟺ hull(B) ⊆ D_Q. Also hull(B) = cone(B_d) + int ℝⁿ₊.
- (c) **Q_B = ∅ ⟺ cone(B_d) meets −int ℝⁿ₊.** That is, there are b₁,…,b_r ∈ B_d (r ≤ n) and λ_j ≥ 0 with Σλ_j b_j ≪ 0: a *sure-loss combination*.
- (d) If some measurable L ⊆ B has m(L) ≪ 0, then Q_B = ∅.

*Proof.*
- (a) Closedness: if q_k → q in Q_B, then B ∩ {q·h<0} ⊆ ⋃_k B ∩ {q_k·h<0}, which is null. Convexity is clear. The description by density points is the first paragraph of the proof of the note's hull formula (Lemma "hullformula"); it uses neither U nor K′.
- (b) These are the note's Lemma "hull"(b),(c) and the hull formula. Their proofs use only Q_B ≠ ∅, the Lindelöf property and the nullity of {P_{Q_B} = 0}. They use neither K′ nor the domain.
- (c) "⇐": if c = Σλ_j b_j ≪ 0, every q ∈ Δ has q·c < 0, so q·b_j < 0 for some j, and q ∉ Q_B by (a).
  "⇒": suppose the convex cone C = cone(B_d) misses the open convex cone −int ℝⁿ₊. Separation gives q ≠ 0 with q·c ≥ 0 on C and q·y ≤ 0 on −int ℝⁿ₊. The second inequality forces q ≥ 0. Then q/(𝟙·q) ∈ Q_B by (a).
  For r ≤ n: write −𝟙 − p = Σλ_j b_j with p ≫ 0, and apply the conic Carathéodory theorem.
- (d) If q ∈ Q_B, then q·m(L) = ∫_L q·h dμ ≥ 0. But q ∈ Δ and m(L) ≪ 0 give q·m(L) < 0. ∎

**Lemma 2.2 (the safety test; PROVED).** Let U be hull-closed (Def. 3.1), and let (A,B) be a record of subsets of U. Then (A,B) is safe on U ⟺ Q_B = ∅, or μ(A ∩ hull(B)) > 0.
- Special cases:
  - If B is null, then Q_B = Δ and hull(B) = int ℝⁿ₊. The record is safe iff μ(A ∩ int ℝⁿ₊) > 0.
  - Q_B = Δ also happens whenever B ⊆ int ℝⁿ₊ a.e.
  - **If no coherent model contains B (Q_B = ∅), every record with removed part B is safe**, whatever A is.
- On U ⊇ V₀ (or ℝⁿ), adopt the convention D_∅ := ℝⁿ. The test then reads: μ(A ∩ hull(B)) > 0, or A null and Q_B = ∅.

*Proof.*
- If Q_B = ∅, no D_Q contains B a.e. by Lemma 2.1(b), so nothing is attacked.
- If Q_B ≠ ∅, then hull(B) ∈ 𝒞_U (hull-closedness) and B ⊆ hull(B) a.e. So when μ(A ∩ hull(B)) = 0, the record attacks hull(B).
- Conversely, if the record attacks D_Q ∈ 𝒞_U, then hull(B) ⊆ D_Q by 2.1(b), and A ∩ hull(B) ⊆ A ∩ D_Q is null. ∎

**Lemma 2.3 (protection is free on every domain; PROVED).** Let U be any domain, C ∈ 𝒞_U and Y ∈ 𝓜_U, and suppose r(Y,C) = (A,B) is guidance at every world.
- Then A ⊆ ⋂_ω {h_ω > 0} = int ℝⁿ₊ a.e. and B ⊆ −int ℝⁿ₊ a.e. (finitely many null sets).
- A = Y∖C is disjoint from C ⊇ int ℝⁿ₊, so A is null.
- B = C∖Y ⊆ C, and C contains no h ≤ 0, so B is null. Hence Y = C a.e.

So **pure guidance never weakly dominates a coherent model nontrivially**. One-sidedness is not used. ∎

**Lemma E (net sure loss; PROVED).** Let X be measurable, under (M). The following are equivalent:
- (i) Q_X = ∅;
- (ii) v_X := min_{λ∈Δ} ∫_X (λ·h)⁻ dμ > 0;
- (iii) some λ ∈ Δ has m(X ∩ {λ·h < 0}) ≪ 0;
- (iv) some measurable L ⊆ X has m(L) ≪ 0.

Moreover, if λ* attains the minimum in (ii), then m(X ∩ {λ*·h < 0}) ≤ −v_X 𝟙.

*Proof.*
- **(i)⟺(ii).** λ ↦ ∫_X (λ·h)⁻ is continuous on Δ (dominated by |h|), and it vanishes exactly on Q_X.
- **(ii)⟹(iii), and the "moreover".**
  - The vector measure Y ↦ m(Y) on measurable Y ⊆ X is finite (first moment) and non-atomic (μ ≪ Lebesgue). By Lyapunov, M_X := {m(Y) : Y ⊆ X} is compact and convex.
  - Put x := m(X) and f(λ,z) := λ·(z − x) on Δ × M_X. f is bilinear and continuous. By the minimax theorem (von Neumann/Sion), max_z min_λ f = min_λ max_z f, and both are attained, at z* and λ*.
  - For each λ ∈ Δ, max_{Y⊆X} λ·m(Y) = ∫_{X∩{λ·h>0}} λ·h. So max_z f(λ,z) = ∫_X(λ·h)⁻. The common value is v_X > 0.
  - Saddle point: f(λ*,z*) ≤ max_z f(λ*,·) = v_X and f(λ*,z*) ≥ min_λ f(·,z*) = v_X. So z* maximises λ*·z over M_X.
  - Write z* = m(Y*). Then ∫_{Y*} λ*·h ≤ ∫_{Y* ∩ {λ*·h>0}} λ*·h ≤ ∫_{X∩{λ*·h>0}} λ*·h. Equality throughout forces Y* = X ∩ {λ*·h > 0} a.e., because the hyperplane {λ*·h = 0} is null for λ* ≠ 0.
  - Hence min_i (m(X∩{λ*·h>0}) − m(X))_i = v_X, that is, m(X ∩ {λ*·h<0}) ≤ −v_X 𝟙.
- **(iii)⟹(iv)** is trivial. **(iv)⟹(i)** is Lemma 2.1(d). ∎

*Plain English.* A set of gambles contains a sure-loss combination exactly when one prior can point to a part of it whose total Brier moment loses at every world.

## 3. Safe strict improvements on hull-closed domains

### 3.1 Hull-closed domains

**Definition 3.1.** U is *hull-closed* if hull(B) ⊆ U a.e. for every measurable B ⊆ U with Q_B ≠ ∅.

**Proposition 3.2 (PROVED).**
- (a) U is hull-closed ⟺ U ∩ D_Q is coherent (a.e.) for every credal set Q. In words, on U the trace of a coherent model is coherent: relative and global coherence (FD62 (RC) and (GC)) coincide for traces.
- (b) The following are hull-closed:
  - every U = D_{K′} (K′ nonempty compact convex);
  - every D_{K′} ∪ E with E ⊆ −ℝⁿ₊;
  - every full domain U ⊇ V₀ (in particular V₀ and ℝⁿ);
  - for n = 2, every U = W ∪ E with E ⊆ −ℝ²₊ and W an open sector containing int ℝ²₊ and contained in V₀.
- (c) F61's A_K is not hull-closed, and neither is U ∪ (−U) for non-singleton K′ in FD62's witness.
- (d) For n = 2, a domain on which some ranking satisfies (G) and has coherent world-best models B_i = U ∩ {h_i > 0} is, a.e., of the form in (b)'s last item. (This holds under (GC) by the covering paper's Lemma "worldbest".)

*Proof.*
- (a) "⇐": let B ⊆ U with Q_B ≠ ∅. Then T := U ∩ hull(B) is coherent, say T = D_{Q′}, and B ⊆ T a.e. By minimality, hull(B) ⊆ D_{Q′} = T ⊆ U.
  "⇒": T := U ∩ D_Q satisfies Q ⊆ Q_T, so Q_T ≠ ∅. hull(T) ⊆ D_Q by minimality, and hull(T) ⊆ U by hull-closedness. So hull(T) ⊆ T a.e., and T ⊆ hull(T) a.e. Hence T = hull(T), which is coherent.
- (b)
  - D_{K′} ∩ D_Q = D_{conv(K′∪Q)}.
  - With E ⊆ −ℝⁿ₊: a set B with Q_B ≠ ∅ has B ∩ E null, because −int ℝⁿ₊ has full measure in −ℝⁿ₊ and any q ∈ Δ is negative there. So B ⊆ D_{K′} a.e.
  - For U ⊇ V₀: D_Q ⊆ V₀ ⊆ U.
  - For n = 2, in angle coordinates the coherent models are exactly the open sectors (γ,δ) with −π/2 ≤ γ ≤ 0, π/2 ≤ δ ≤ π and δ − γ ≤ π. Write W = (α,β) with −π/2 ≤ α ≤ 0, π/2 ≤ β ≤ π. Then W ∩ D_Q = (max(γ,α), min(δ,β)) is again of that form. Use (a), with E handled as above.
- (c) FD62 §2.1: x = (1,−1,−20) and y = (1,4,−1) lie in A_K, with e₁ ∈ Q of small balls around them. But x+y = (2,3,−21) ∈ hull of those balls and lies outside A_K, robustly (margin 5/3). The same works for U ∪ (−U) with REF62's witness x = (13/5, −3/2, 19/4) ∈ U and y = (1/2, −7/5, −9/2) ∈ −U: both have h₁ > 0, and x + y ∉ U ∪ −U.
- (d) B₁ = D_{Q₁} ⊆ {h₁>0} and B₂ = D_{Q₂} ⊆ {h₂>0} are coherent sectors containing int ℝ²₊. Their union U ∩ V₀ is an open sector inside V₀. ∎

### 3.2 The two cases

**Theorem 3.3 (Case 1: nonempty hull; PROVED).** Let U be hull-closed, X ∈ 𝓜_U incoherent, and Q_X ≠ ∅. Then there is N ∈ 𝒞_U with:
- m(N) − m(X) ≫ 0;
- N ⊆ hull(X∖N) = hull(X);
- μ(N∖X) > 0.

In particular r(N,X) is safe.

*Proof.* This is the round-65 proof (note, Theorem "H": relative minimax, then the uniform shrink, then Lemma "contraction"/Cor "shrink"), with three changes.
1. G := hull(X) = D_{Q_X} lies in U by hull-closedness. So every coherent N ⊆ G is in 𝒞_U.
2. In Step 2 ("the gain is non-null"), replace k ∈ K′ by any k ∈ Q_X. Then k·h ≥ 0 a.e. on X. If N₀∖X were null, k·(m(N₀) − m(X)) = −∫_{X∖N₀} k·h ≤ 0 would contradict m(N₀) − m(X) ≫ 0.
3. Lemma "contraction" and Cor "shrink" use only that Q_X is nonempty, closed (Lemma 2.1(a)) and convex.

Everything else is as written: Lyapunov on G; uniqueness of the maximiser G ∩ {λ·h>0} = D_{conv(Q_X∪{λ})}; v > 0 by incoherence; the shrink N_τ = N₀ ∩ D_{(1−τ)Q_X+τΔ}.

Safety: (N∖X) ∩ hull(X∖N) = N∖X, which is non-null; apply Lemma 2.2. ∎

**Theorem 3.4 (Case 2: empty hull; PROVED).** Let U be hull-closed, X ∈ 𝓜_U, and Q_X = ∅ (so X is incoherent). Let λ*, v_X be as in Lemma E. Put:
- X₁ := X ∩ {λ*·h > 0};
- G₁ := hull(X₁) (λ* ∈ Q_{X₁}, so Q_{X₁} ≠ ∅);
- π* := a minimiser over Δ of the convex function π ↦ max_{Y⊆G₁} π·m(Y) − π·m(X);
- N := G₁ ∩ {π*·h > 0} = D_{conv(Q_{X₁} ∪ {π*})}.

Then:
- (a) N ∈ 𝒞_U and m(N) − m(X) ≥ v_X 𝟙 ≫ 0;
- (b) N ⊆ {λ*·h > 0}. Hence X∖N ⊇ X ∩ {λ*·h<0}, a set with moment ≪ 0, so **Q_{X∖N} = ∅ and r(N,X) is safe on U**.

*Proof.*
- (a) X₁ ⊆ U, and Q_{X₁} ∋ λ*. So G₁ ∈ 𝒞_U by hull-closedness, and X₁ ⊆ G₁ a.e. (Lemma 2.1(b)).
  - Run the minimax of Lemma E with M_{G₁} := {m(Y) : Y ⊆ G₁} (Lyapunov) and x := m(X). Note that X need not lie in G₁.
  - The value v′ := max_{z∈M_{G₁}} min_i (z − x)_i is at least min_i (m(X₁) − x)_i ≥ v_X, since m(X₁) ∈ M_{G₁} and Lemma E gives m(X₁) − m(X) = −m(X∩{λ*·h<0}) ≥ v_X 𝟙.
  - The saddle-point argument (as in Lemma E) shows that the maximiser is G₁ ∩ {π*·h>0}, unique a.e. So m(N) − m(X) ≥ v′𝟙.
  - N = D_{Q_{X₁}} ∩ D_{π*} = D_{conv(Q_{X₁}∪{π*})} is coherent, and N ⊆ G₁ ⊆ U.
- (b) N ⊆ G₁ = D_{Q_{X₁}} ⊆ D_{λ*}. So the set L := X ∩ {λ*·h < 0} is disjoint from N, and L ⊆ X∖N. Lemma E gives m(L) ≪ 0. Lemma 2.1(d) gives Q_L = ∅, hence Q_{X∖N} ⊆ Q_L = ∅. Lemma 2.2 gives safety. ∎

*Remarks.*
- On a full domain one may take G₁ := {λ*·h>0}, a half-space, instead of hull(X₁). Then N = D_{[λ*,π*]} is a "two-prior" model.
- No shrink and no contraction lemma are needed in Case 2.
- An alternative route also works, and is checked: apply Theorem 3.3 to X₁ when X₁ is incoherent (it has Q_{X₁} ≠ ∅), or take N := X₁ when X₁ is coherent. Then m(N) − m(X) = (m(N) − m(X₁)) + (m(X₁) − m(X)) ≫ 0, and X∖N ⊇ X∖X₁ again has empty Q.

**Corollary 3.5 (PROVED).** On every hull-closed U, every incoherent X ∈ 𝓜_U has N ∈ 𝒞_U with m(N) − m(X) ≫ 0 and r(N,X) safe on U. In particular this holds on ℝⁿ, on V₀ and on every full domain.

**Remark 3.6 (what the round-65 proof misses, exactly).** On a hull-closed U the round-65 argument (with K′ → Q_X) applies iff Q_X ≠ ∅. By Lemma 2.1(c) and Lemma E, the remaining rivals are exactly those containing a sure-loss combination, equivalently those containing a net Brier sure loss. There, three steps break:
- Step 1 has no coherent G ⊇ X to optimise in.
- Step 2 has no k with k·h ≥ 0 on X. The conclusion of Step 2 genuinely fails for N₀ (REF65_hA §2(b): X = N₀ ∪ E with E ⊆ −int ℝⁿ₊).
- The contraction lemma needs Q_X ≠ ∅.

The obvious repair — use the full-domain Brier-minimax half-space N₀ = {π₀·h>0} — **can produce an unsafe record** (CHECKED, §6.2). So Lemma E is not cosmetic.

## 4. The simple ranking on hull-closed domains

**Theorem 4.1 (PROVED).** Let U be hull-closed, and consider the simple ranking on 𝓜_U.
- (a) Each ⪯_ω is reflexive, ties a.e.-equal models, and satisfies strict (G), (IB), (TC), (FCC) and (Add). X ⪯_ω Y with X ≠ Y a.e. implies m_ω(X) > m_ω(Y). So the ranking is a sub-relation of Brier with no nontrivial ties.
- (b) No coherent model has a weak dominator other than itself.
- (c) Every incoherent model is strictly dominated by a coherent model N, with m(N) − m(X) ≫ 0.
- (d) 𝒰 = 𝒞* = 𝒞_U; (GC), (ID) and (W) hold, and (C) holds in the strong form "tied at every world ⇒ equal".

*Proof.*
- **Reflexivity, ties, (IB).** The null record is guidance; the rule depends only on the record (the note's Lemma "record").
- **Positivity.** A non-null guidance record has d_ω = ∫_A |h_ω| + ∫_B |h_ω| > 0, because {h_ω = 0} is null. A safe accepted record has d_ω > 0 by definition. So accepted non-null records strictly raise m_ω.
- **Strict (G).** The reverse of a non-null guidance record has d_ω < 0. It is not guidance either: that would force both sides null. So it is rejected.
- **(TC), (FCC).** Apply the note's Lemma "deletion" with φ = −m_ω. Clause (b) of that lemma holds vacuously except for a.e.-equal models, which are tied.
- **(Add).** Let r₁, r₂ be accepted at ω with disjoint supports.
  - If both are guidance, so is r₁ ⊔ r₂.
  - Otherwise one, say r₂, is safe. If r₁ ⊔ r₂ attacked C, then r₂ would attack C, since its parts are subsets of the union's. So r₁ ⊔ r₂ is safe, and d_ω(r₁ ⊔ r₂) = d_ω(r₁) + d_ω(r₂) > 0, because guidance records have d_ω ≥ 0.
  - r(X,Z) = r(X,Y) ⊔ r(Y,Z) under the (Add) hypothesis (the note, §"Transitivity and disjoint additivity").
- **(b).** Let Y weakly dominate C ∈ 𝒞_U. r(Y,C) attacks C, so it is not safe. So it is guidance at every world, and Lemma 2.3 gives Y = C.
- **(c).** Take N from Cor 3.5. r(N,X) is safe with d_ω > 0 at every ω, so N ⪯_ω X. The reverse record has d_ω < 0 and is not guidance (as in strict (G)). So N ≺_ω X for all ω.
- **(d).** By (b), 𝒞_U ⊆ 𝒰. By (c), 𝒰 ⊆ 𝒞_U. (W) holds because every model is either coherent (and weakly dominates itself) or strictly dominated by a coherent model. Strong (C): a model tied at every world with C weakly dominates C, so it equals C by (b). ∎

## 5. Coverage

**Lemma 5.1 (PROVED).** Let K be a credal set and U a domain with D_K ⊆ U a.e. Then (LF) holds at D_K ⟺ some open O ⊇ ∂D_K∖{0} has O ⊆ U a.e.

*Proof.*
- "⇒": take the N of (LF), and test it with X := D_K ∪ N.
- "⇐": if X △ D_K ⊆ O a.e., then X ⊆ D_K ∪ O ⊆ U a.e. ∎

**Proposition 5.2 ((LF) on full domains; PROVED).** Let U = V₀ ∪ E a.e., with E ⊆ −ℝⁿ₊. Let K be a credal set, S_K := ⋃_{k∈K} supp k, and F_K := {h ∈ −ℝⁿ₊∖{0} : h_i = 0 ∀ i ∈ S_K}.
- D_K ∈ 𝓜_U always.
- (LF) holds at D_K ⟺ F_K = ∅, or some open O′ ⊇ F_K has O′ ∩ (−ℝⁿ₊) ⊆ E a.e.
- F_K = ∅ ⟺ S_K = Ω ⟺ K ∩ relint Δ ≠ ∅.

*Proof.*
- ∂D_K = {P_K = 0}. For h ≤ 0, P_K(h) = 0 ⟺ k·h = 0 ∀ k ∈ K ⟺ h vanishes on S_K. So ∂D_K ∖ {0} ⊆ V₀ ∪ F_K.
- V₀ is open. So, by Lemma 5.1, the open set V₀ ∪ O′ works whenever O′ ⊇ F_K is open with O′ ∩ (−ℝⁿ₊) ⊆ E a.e.
- Conversely, an open O ⊇ ∂D_K∖0 with O ⊆ U a.e. is such an O′.
- If S_K = Ω, pick k_i ∈ K with (k_i)_i > 0. Their average lies in K ∩ relint Δ. The converse is trivial. ∎

**Corollary 5.3 (PROVED).** Every hull-closed U carries the simple ranking, which covers K ⟺ D_K ∈ 𝓜_U and (LF) holds at D_K. Since any cover needs these two conditions, **the simple ranking is a universal cover on every hull-closed domain**. In particular:
- (a) **U = ℝⁿ: every credal set is covered** — precise, lower-dimensional, touching ∂Δ, including Δ itself and {e_i}. One ranking covers all of them.
- (b) **U = V₀: exactly the credal sets with K ∩ relint Δ ≠ ∅ are covered.**
  - Example: K = {(½,½,0)} (n = 3) fails, because F_K is the ray through −e₃, and near it (LF) would need sure losses.
  - Every K that meets no edge, with n = 3, passes, since a K in a proper face of Δ₃ lies in an edge.
  - For n ≥ 4 a K inside a 2-face (meeting no edge) fails on V₀ and passes on ℝⁿ.
- (c) **U = D_{K′} (one-sided):** exactly the full-dimensional K with K′ ⊆ relint K. This is round 65, unchanged; one-sided domains are hull-closed.
- (d) **n = 2, U = (α,β) as in Prop 3.2(b), with E null:** K with q-angles [φ₁,φ₂] is covered ⟺ α < φ₂ − π/2 and φ₁ + π/2 < β. (A non-null E can only help at the rays of angle −π/2 and π, exactly as in Prop 5.2.) Precise {p} is covered iff α + π/2 < φ_p < β − π/2. This is nonempty exactly when U is two-sided (β − α > π), consistent with the covering paper's Prop "lowdim".

*Proof.* Thm 4.1 gives (i)–(v) of the cover definition for every K with D_K ∈ 𝓜_U, because D_K is coherent and hence undominated. (vi) is (LF). Prop 5.2 gives (a) and (b). For (c), see the covering paper's Lemma "LF". For (d): D_K = (φ₂ − π/2, φ₁ + π/2). Apply Lemma 5.1 to the two boundary rays; the open sector U is the neighbourhood. ∎

**Reconciliation (PROVED).**
- **FD-1 / Prop "lowdim".** Let n ≥ 3, K meet no edge, and suppose K is covered on a U that is not essentially one-sided. Then U ⊇ V₀ a.e. (FD-1(b), via (GC)), and the simple ranking on U covers K too.
  - If K is lower-dimensional, (LF) forces a domain that is not essentially one-sided (Prop "lowdim", first part).
  - So: **a lower-dimensional K meeting no edge is coverable on U ⟺ U ⊇ V₀ a.e. and Prop 5.2's condition holds; it is always coverable on ℝⁿ.**
- **Plain Brier on the full domain.**
  - On ℝⁿ its undominated models are exactly D_{{q}}, q ∈ Δ. They are the unique maximisers of q·m. Any other model is uniformly Brier-dominated by one of them: the note's Remark "H"(c), with G = ℝⁿ.
  - Brier is complete and transitive, so (C) follows from (GC).
  - Hence **plain Brier on ℝⁿ covers exactly the precise credal sets {p}, p ∈ Δ**, including p ∈ ∂Δ, since (LF) is trivial on ℝⁿ. On V₀ it covers exactly the {p} with p ∈ relint Δ (Prop 5.2).
  - The covering paper's Cor "precise" ("p ∈ relint Δ") is therefore correct, but understated on ℝⁿ; its proof inherits K ⊆ relint Δ from Thm "opcover".
  - The simple ranking accepts only comparisons with d_ω ≥ 0, so it is a sub-relation of Brier and keeps strictly more undominated models: every coherent model, not just the precise ones. Both cover every precise {p} on ℝⁿ.

## 6. Checks (CHECKED unless stated)

Measure: density e^{−|h|₁} on ℝ³ (satisfies (M)). Rivals are finite disjoint unions of open polyhedral cones. Cone masses and moments are exact (orthant split, gamma integrals). Q_X is an exactly clipped polygon of Δ built from the generators of the piece closures. Priors are found by float minimisation of the convex dual functions and then **re-verified exactly**. Library: `ts66py/geo3.py`.

### 6.1 `case2_check.py` → `case2_check.out`: 30 rivals with Q_X = ∅

Designed rivals:
- T1: {u·h>0} ∪ (−int ℝ³₊);
- T2: X = ℝ³;
- T3: {h₁>0} ∪ {h₂>0};
- T4: {p₁·h>0} ∪ {p₂·h>0};
- T5: three thin cones around (1,−3,1), (1,1,−3), (−3,1,1), plus int ℝ³₊;
- T6: D_K ∪ (−D_K), reversed triangle;
- T7: ℝ³ ∖ D_K;
- T8: ℝ³ ∖ int ℝ³₊;
- T9: {u·h>0} plus a thin cone just outside its boundary;
- T10: {u·h>0} plus a far cone.

Also 20 random unions of 2–5 random simplicial cones and half-spaces (seed 66).

For each rival, all of the following hold exactly:
- Q_X = ∅;
- a rational λ with m(X ∩ {λ·h<0}) ≪ 0 (Lemma E);
- λ ∈ Q_{X₁} and X₁ ⊆ hull(X₁);
- **main construction (Thm 3.4):** N = hull(X₁) ∩ {π·h>0} has m(N) − m(X) ≫ 0, N ∩ {λ·h<0} null, Q_{X∖N} = ∅, and the record is safe;
- **alternative route (Thm 3.3 on X₁, or N = X₁):** the margin, Q_{X₁∖N} = Q_{X₁}, μ(N∖X₁) > 0 and μ(N∖X) = μ(N∖X₁) are certified as well. X₁ was incoherent (so Thm 3.3 ran) in 24 rivals and coherent in 6 (T1, T2, T5, T6, T9, T10).

Result: **30/30 main, 30/30 alternative.**
- Smallest margins: about 10⁻⁷ (T9, exactly positive) and 2·10⁻⁴ (T5).
- In T5 the certified prior is π = (0, 3/10, 7/10), on ∂Δ, which the theorem allows.
- On these 30 rivals the naive half-space happened to be safe as well.

### 6.2 Controls: the naive full-domain defender can be unsafe

- `naive_case1.py` (seed 5) → `naive_case1.out`.
  - Among 97 random rivals with Q_X ≠ ∅ (unions of coherent cones sharing a prior, with a hole), the full-domain Brier-minimax half-space {π₀·h>0} has an unsafe record in 6, with witness mass exactly 0.
  - Two of these were then **lifted** to Case-2 rivals: add a thin cone E around s with π₀·s > 0 and q·s < 0 on Q_X. Then Q_{X∪E} = ∅ exactly, and **the naive defender is still unsafe** (Q_B ≠ ∅, witness 0, exact).
  - The main construction is certified on both lifts. One margin is 2.5·10⁻⁵, against the naive margin 0.05. Safety costs margin.
- `naive_hunt.py`, `naive_target.py`: random and first-order-targeted Case-2 rivals of the form "half-space plus a thin outside cone". 0 naive failures in 59 + 84 rivals (NUMERICS). Naive failures appear to need a Case-1-type defect underneath.

### 6.3 Not computed

The ranking clauses (Thm 4.1) and the (LF) characterisations (Prop 5.2, Cor 5.3) are short proofs and were not checked by computer. SR66 is checking the finite ranking clauses independently.

## 7. Scope, nearby results, open items

1. **Domains that are not hull-closed (OPEN).** On these the simple ranking's undominated class still contains 𝒞_U (Lemma 2.3 does not need hull-closedness), but Case 1 can produce hull(X) ⊄ U.
   - For n ≥ 3 and targets meeting no edge, FD-1 says such domains are either full domains, which are hull-closed, or essentially one-sided (branch (a)). On the latter, lower-dimensional targets are excluded anyway, by (LF).
   - The live questions are therefore:
     - (i) branch-(a) domains U = ⋃ D_{Q_i} that are not convex. Does any ranking satisfy (G)+(GC)+(ID) there?
     - (ii) n ≥ 3 targets meeting an edge, where FD-1 does not apply.
   - CONJECTURE: hull-closedness (equivalently, by Prop 3.2(a), "traces of coherent models are coherent") is necessary for (GC)+(ID) under (G). It is PROVED for n = 2 (Prop 3.2(d)), and for n ≥ 3 in FD-1's two-sided branch.
2. **Infinite worlds, two-sided (CONJECTURE, sketch only).** This is the audit's §4 setting with U = E (all of the separable gamble space), coherent models D_Q for any nonempty weak-* compact convex Q ⊆ S.
   - Lemma E transfers. S is weak-* compact, and q ↦ ∫_X q(h)⁻ dμ is continuous by dominated convergence. The relaxed minimax over 0 ≤ f ≤ 1_X with the boundary-null measure returns the indicator of X ∩ {q*(h) > 0}.
   - Theorem 3.4's proof then needs only the audit's relaxed minimax inside hull(X₁), with no shrink.
   - Protection transfers (Lemma 2.3 with the countable norming set of the audit's Step E).
   - Contingent on IW66's verdict on the audit theorem; not written out here.
3. **Coherence-informed definition.** As on one-sided domains, the ranking refers to the coherent class through "safe". Nothing here changes that.
4. **Suggested text for the universal note** (UN66's lower-dimensional paragraph): "On the full domain ℝⁿ the same ranking makes exactly the coherent models undominated and covers every credal set, including precise and lower-dimensional ones. The only new case is a rival with an empty coherent hull. Some prior then identifies a part of it that loses in Brier moment at every world, and a coherent improvement that removes that part is automatically safe."

## 8. Status table

| # | Result | Hypotheses | Status |
|---|---|---|---|
| 1 | Lemma 2.1: Q_B closed convex; hull facts when Q_B ≠ ∅; **Q_B = ∅ ⟺ sure-loss combination of ≤ n density points**; m(L) ≪ 0 for some L ⊆ B ⇒ Q_B = ∅ | (M) | PROVED |
| 2 | Lemma 2.2: safe ⟺ Q_B = ∅ or μ(A ∩ hull(B)) > 0 (cases B null, Q_B = Δ, Q_B = ∅) | U hull-closed | PROVED |
| 3 | Lemma 2.3: pure guidance never weakly dominates a coherent model nontrivially | any domain | PROVED |
| 4 | **Lemma E**: Q_X = ∅ ⟺ ∃λ: m(X ∩ {λ·h<0}) ≪ 0 ⟺ min_λ ∫_X(λ·h)⁻ > 0 | (M) | PROVED; CHECKED (32 rivals) |
| 5 | Prop 3.2: hull-closed ⟺ traces of coherent models coherent; examples (D_{K′}, D_{K′} ∪ sure losses, every U ⊇ V₀, n = 2 sectors); A_K and U ∪ −U are not hull-closed; n = 2 (G)-domains with coherent world-best models are sectors | (M) | PROVED |
| 6 | Thm 3.3 (Q_X ≠ ∅): round-65 relative minimax + shrink, with K′ → Q_X | U hull-closed | PROVED; CHECKED (26 incoherent X₁ with Q_{X₁} ≠ ∅: 24 in §6.1 + 2 lifts) |
| 7 | **Thm 3.4 (Q_X = ∅): Lemma E + one relative minimax in hull(X ∩ {λ·h>0}); removed part has empty Q, so the record is safe** | U hull-closed | PROVED; CHECKED (30 + 2 lifted rivals, exact) |
| 8 | Cor 3.5: every incoherent model has a coherent strict Brier improvement with a safe record | U hull-closed (incl. ℝⁿ, V₀) | PROVED |
| 9 | The round-65 proof misses exactly the Q_X = ∅ rivals; the naive full-domain Brier half-space can be unsafe on them | — | PROVED (characterisation); CHECKED (2 exact examples) |
| 10 | Thm 4.1: simple ranking has reflexivity, a.e. ties, strict (G), (IB), (TC), (FCC), (Add), no nontrivial ties; 𝒰 = 𝒞_U; strict dominance of incoherent models; (GC), strong (C), (ID), (W) | U hull-closed | PROVED |
| 11 | Lemma 5.1: (LF) ⟺ ∂D_K∖0 has an open neighbourhood inside U a.e. | D_K ∈ 𝓜_U | PROVED |
| 12 | Prop 5.2: on U = V₀ ∪ E, (LF) ⟺ K ∩ relint Δ ≠ ∅, or E contains the sure losses near F_K | full domains | PROVED |
| 13 | **Cor 5.3(a): on ℝⁿ one ranking covers every credal set** (precise, lower-dimensional, boundary) | U = ℝⁿ | PROVED |
| 14 | Cor 5.3(b): on V₀ exactly the K meeting relint Δ are covered (n = 3: every K meeting no edge; n ≥ 4: 2-face targets fail on V₀) | U = V₀ | PROVED |
| 15 | Cor 5.3(c),(d): universal cover on every hull-closed U; one-sided result unchanged; n = 2 sector coverage criterion | as stated | PROVED |
| 16 | FD-1 reconciliation: n ≥ 3, K meeting no edge, lower-dimensional ⇒ coverable on U ⟺ U ⊇ V₀ a.e. plus Prop 5.2; always coverable on ℝⁿ | n ≥ 3, (G), (GC) | PROVED |
| 17 | Plain Brier on ℝⁿ covers exactly {p}, p ∈ Δ (covering paper Cor "precise" understated on ℝⁿ, exact on V₀) | (M) | PROVED |
| 18 | Naive defender safe on "half-space + thin cone" Case-2 rivals | n = 3 | NUMERICS (0/143 failures) |
| 19 | Two-sided infinite-world analogue | audit §4 setting | CONJECTURE (sketch) |
| 20 | Non-hull-closed two-sided domains (FD-1 one-sided nonconvex branch; targets meeting an edge, n ≥ 3); necessity of hull-closedness | — | OPEN (CONJECTURE: necessary) |
