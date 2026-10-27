# REF65_un: referee report on "Universal coverage by comparison deletion (draft)" (26 Oct 2026)

Labels: PROVED (checked by hand, line by line) / CHECKED (exact computation) / NUMERICS (sanity only).
Every verdict below rests on the note's own proofs. I used the source notes only to compare.

Scripts are in `ref65un_py/`:
- `ex71_exact.py` and `.out`: an independent exact rational check of Example 7.1. It shares no code with `ref64es_py/` or `un65py/`. It builds its own arrangement of cells, extreme rays, a fan triangulation, and closed-form simplicial-cone moments for the density e^{-|h|_1}.
- `thmH_2d_sanity.py` and `.out`: NUMERICS. Two worlds, 80 random incoherent conic rivals. It runs Steps 1–3 of Theorem 5.3 and checks the margin, N ⊆ hull(X∖N), μ(N∖X) > 0 and Q_{X∖N} = Q_X. There were 0 failures.
- `build/`: a fresh compile. pdflatex ran twice with no warnings, no overfull or underfull boxes and no undefined references. The output is 14 pages, and its text is identical (pdftotext diff) to the supplied PDF.

## Headline

**The note is mathematically correct.** I re-derived every proof and found no ERROR in any theorem, lemma or corollary. Theorem 5.3 ((H) with a strict margin and N ⊆ hull(X∖N)) holds in full generality. Its three steps are:
- minimax over Δ × ℳ_G;
- a uniform shrink to D_{(1−τ)Q_X+τΔ};
- the contraction lemma.

The main theorem holds with exactly the stated coverage set.

The required changes are about scope and presentation:
- one overclaim in the abstract;
- an undefined term ("universal cover");
- one remark that states an unproved lemma;
- a few small expository gaps.

## Verdicts by item

### 1. Framework definitions — CORRECT (two minor presentational points)

I compared the note with the covering paper §2 (`def:dom`, Requirements, `def:cover`) and with `AUDIT_r64_decisions.md`. The note matches on every point:
- rankings are families of reflexive relations, a.e.-equal models are tied, and (TC) holds, with no transitivity or completeness;
- (G) is the strict form (X ≺_i Y);
- (IB) matches verbatim;
- (GC) is the global version (coherent means X = D_Q a.e. for a credal Q);
- (C) is direct closure under ties with members of 𝒞*;
- cover (iv) is that the target is undominated;
- (ID) asks for domination by a member of 𝒞*;
- (LF) matches;
- (W) is listed explicitly as not required;
- (FCC) is presented as an extra condition and correctly noted to contain (TC) as the case k = 2.

The dominance nomenclature matches the paper: weak dominance, dominance, strict dominance, and uniform dominance in Brier loss. The note's uniform dominance in Brier loss, β_i(Y) + ε ≤ β_i(X), is equivalent to m(Y) − m(X) ≫ 0 because β_i = c_i − m_i with c_i finite by (M).

Minor points:
- (a) **(LF) gloss.** The paper's (LF) ends "belongs to ℳ_U, *that is, satisfies X ⊆ U a.e.*". The note drops the gloss, but its proofs use exactly that reading (Lemma 2.5(b),(c)). Restore the gloss for an exact match.
- (b) **"One-sided".** The note defines one-sided as "U ∩ (−U) null". The cited covering paper defines it as "U ∩ (−U) = ∅" and also has "essentially one-sided". The note's definition is self-consistent and makes Lemma 2.5(c) slightly stronger than the paper's empty version. However, the same word now means different things in the note and in [KCM], which the note cites in §6. Add one sentence acknowledging this, or use a different word.

### 2. Domain lemma (Lemma 2.5) — CORRECT

- **(a)** D_K ∈ ℳ_U ⟺ D_K ⊆ U a.e. ⟺ D_K ⊆ D_{K'}, by Lemma 2.1(d) since D_K is open. This holds ⟺ K' ⊆ K by Lemma 2.1(c).
- **(b), relint ⇒ (LF).** Take h ∈ C_K∖{0} and x ∈ relint K. If x·h = 0, then d·h = 0 for all d ⊥ 𝟙, so h = c𝟙 with c = x·h = 0. This is a contradiction, so x·h > 0. Then ∂D_K∖{0} ⊆ cl D_K∖{0} ⊆ C_K∖{0} ⊆ D_{K'} = U, and N := U works.
- **(b), (LF) ⇒ relint.** I checked Rockafellar Thm 11.6: a non-trivial supporting hyperplane to C contains D iff D ∩ ri C = ∅. Because K is full-dimensional, ri K in Rockafellar's sense equals the note's relint K. The rest of the argument holds:
  - h = g − (g·x)𝟙 ∈ C_K∖D_K with h ≠ 0, and h ∈ ∂D_K;
  - the model D_K ∪ N lies in ℳ_U, so N ⊆ U a.e., and then N ⊆ U by Lemma 2.1(d);
  - x·h = 0 with x ∈ K' gives h ∉ U, a contradiction.
- **(c), lower-dimensional.** dim aff K ≤ n−2 and 0 ∉ aff K, so dim span K ≤ n−1, and some h ≠ 0 is orthogonal to K. Then ±h ∈ ∂D_K∖{0}. (LF) for X = D_K ∪ N gives N ⊆ V a.e. The ball B(h,r) ⊆ V ∩ (−V) a.e. is non-null, which contradicts the null definition of one-sidedness. The argument does not need D_K ∈ ℳ_V separately: (LF) applied to X = D_K already forces it.

Lemma 2.1 (all parts) and Lemma 2.2 (the hull lemma) are also CORRECT:
- the graph-over-𝟙^⊥ nullity argument is right;
- (d) works via h − ε𝟙 ∈ O;
- closedness of Q_B works via sequences;
- B ⊆ hull(B) a.e. works via a Lindelöf countable subcover of ⋃_{q∈Q_B}{q·h<0};
- the three-way equivalence in 2.2(c) holds.

### 3. Deletion lemma (Lemma 3.2) — CORRECT

With φ valued in any totally ordered T:
- (a) and (b) give X ≺ Y ⇒ φ(X) < φ(Y);
- a chain gives φ(A_0) ≤ φ(A_k);
- so A_k ≺ A_0 is impossible.

This yields (FCC), and (TC) as the case k = 2.

Minor: the gloss that follows the lemma still says "a real score". Change it to "a score in a totally ordered set".

Lemma 3.1 (record relations satisfy (IB)) is CORRECT: X△Y ⊆ S a.e. gives r(X,Y) = r(X',Y') a.e.

### 4. CD(𝒩) and the reduction theorem (Theorem 4.1) — CORRECT

**Existence of the deletion world.** Suppose r ∈ G_i for all i. Then A ⊆ int ℝⁿ₊ and B ⊆ {h ≪ 0} a.e. Since U ∩ {h ≪ 0} = ∅, B is null. If r attacks D_Q ⊇ int ℝⁿ₊, then A is null. So the deletion world exists. The rule always picks i(r) with r ∉ G_{i(r)}. Preferring a world with m_i(r) > 0 only reduces the number of tie-inverse deletions; correctness does not depend on it.

**"Attack".** If B ⊆ Z a.e. and A ∩ Z is null, then r(Z⊕r, Z) = r and Z⊕r ∈ ℳ_U. This is right. So every record in ℛ(𝒩) is the record of some pair (Y,N) with N ∈ 𝒩 and m(Y) ≥ m(N). The sentence "No other comparison is removed" is therefore accurate at the level of records. The preceding sentence ("applies in every context") makes clear that comparisons between incoherent models are removed too.

**(a) Axioms.**
- The null record is accepted.
- **(G).** A non-null r ∈ G_i has m_i(r) = ∫_A|h_i| + ∫_B|h_i| > 0. It is never deleted at i:
  - it is not a first-type deletion, because i ≠ i(r) when r ∈ G_i;
  - it is not a tie inverse, because m_i(r) ≠ 0.
  
  Its inverse is not in Br_i.
- **Tie symmetry.** Both cases are correct:
  - if r^{-1} ∈ ℛ with i(r^{-1}) = i, then r is deleted as its tie inverse;
  - if r^{-1} = s^{-1}, then s = r is deleted.
- **(FCC)** then follows from Lemma 3.2 with φ = −m_i.

**(b) Protection.** If Y weakly dominates N ∈ 𝒩 and Y ≠ N, then r(Y,N):
- is non-null;
- has m ∈ ℝⁿ₊;
- attacks N, since (Y∖N) ∩ N = ∅ and N∖Y ⊆ N.

So r(Y,N) ∈ Del_{i(r)}, which is a contradiction.

**(c) (★) ⇒ dominance.** Deleting d = r(N,X) as an inverse would need m(X) ≥ m(N), hence m(X) = m(N), which (★) excludes. Strictness at every j holds when m(N) − m(X) ≫ 0.

**(d) Dominance ⇒ (★).** If m(N) = m(X), tie symmetry gives X ⪯_i N at every i.

**(e)** (1) ⟺ (2) follows from (c) and (d). Then 𝒰 = 𝒞* = 𝒩, and (GC), (C) in the strong form, (ID) and (W) follow.

### 5. (ID) ⟺ (H), the hull formula and the witness — CORRECT (one minor expository point)

**Corollary 4.2.**
- If A ∩ hull(B) is null, then (A,B) attacks hull(B) ∈ 𝒞_U.
- Conversely, if (A,B) attacks D_Q, then hull(B) ⊆ D_Q by Lemma 2.2(c).

The (ID) ⟺ (H) bookkeeping through Theorem 4.1(d),(e) is right. When B is null, Q_B = Δ and hull(B) = int ℝⁿ₊, and the statements remain correct.

**Lemma 4.3: hull(B) = cone(B_d) + int ℝⁿ₊.**
- **"⊆" direction.** q ∈ Q_B is non-negative on B_d, by the density-point and positive-measure argument. So q·a ≥ q·p > 0.
- **"⊇" direction.** Separate a ∉ E from the open convex set E. Then:
  - q ≥ 0, using 𝟙 + s e_i ∈ E;
  - q·b ≥ 0 on B_d (let s → ∞; the note leaves this implicit — add "(let s→∞)");
  - q·a ≤ 0, using t𝟙.
  
  Then q̂ ∈ Q_B and q̂·a ≤ 0.

**Corollary 4.4 (witness, r ≤ n).**
- **⇐.** a ∈ hull(B), which is open, and a is a density point of A, so the intersection has positive measure.
- **⇒.** Some a ∈ A_d lies in hull(B), and conic Carathéodory reduces the combination to linearly independent b_j, so r ≤ n. The positive residual p is untouched. The case r = 0 is included through cone ∅ = {0}.

**Minor GAP, Remark 5.4(b).** The remark says "By Corollary 4.4, every density point of N∖X carries a finite witness". This needs every density point of N∖X to lie in hull(X∖N), which the corollary does not supply.
- *Repair (one sentence):* a density point of N∖X is a density point of the open convex set N. A boundary point of a convex set with nonempty interior has upper density ≤ 1/2, so every density point lies in N ⊆ hull(X∖N). Then apply Lemma 4.3 and Carathéodory.

### 6. Theorem 5.3 ((H)) — CORRECT in full

**Step 1 (minimax).**
- The vector measure Y ↦ ∫_Y h dμ is finite by the first-moment condition. It is non-atomic because μ has the null sets of Lebesgue measure, so points are null, and each component is absolutely continuous with respect to μ.
- So by Lyapunov, ℳ_G is compact and convex, and x = m(X) = m(X∩G) ∈ ℳ_G.
- f(λ,z) = λ·(z − x) is bilinear and continuous on the compact convex set Δ × ℳ_G. So Sion's theorem (von Neumann's would do) applies, and both optima are attained.
- v ≥ 0 always holds, because x ∈ ℳ_G. If v = 0, then x maximises λ*·z. The maximiser is unique a.e. because hyperplanes are null, so X = G ∩ {λ*·h > 0} a.e., and X would be coherent. Hence v > 0.
- The saddle argument gives z* maximising λ*·z, so z* = m(N_0) with N_0 = G ∩ {λ*·h > 0}. Also m(N_0) − m(X) = z* − x ≥ v𝟙 ≫ 0. **The strict margin comes from v > 0 in every coordinate. This is right.**
- **Coherence.** N_0 = D_{conv(Q_X ∪ {λ*})} by Lemma 2.1(a). This credal set contains K' because Q_X ⊇ K'. The case λ* ∈ ∂Δ is allowed.

**Step 2 (shrink).**
- If N_0∖X were null, then k·(m(N_0) − m(X)) = −∫_{X∖N_0} k·h ≤ 0 for k ∈ K', which contradicts the margin. This uses K' ≠ ∅.
- N_τ = D_{conv(Q_X ∪ {λ*} ∪ Q_τ)} ∈ 𝒞_U, again containing K'.
- P_{Q_τ} = (1−τ)P + τ min_i h_i, and min_i h_i ≤ P. So D_{Q_τ} increases as τ ↓ 0, and 𝟙_{N_τ} → 𝟙_{N_0} pointwise on N_0, because P > 0 there.
- Dominated convergence, with dominating functions |h| and 1, applies.
- The choice μ(N_0∖N_τ) < μ(N_0∖X) gives μ(N∖X) > 0.

**Step 3, through Lemma 5.1 and Corollary 5.2.**
- **Lemma 5.1.** T(q') = (q + cq')/(1+c) maps Q_X into Q_X. For a.e. x ∈ X, (q + cq')·x ≥ q·x + cP(x) ≥ 0. The exceptional null set depends only on q, not on q'. T is a contraction with ratio c/(1+c) and fixed point q, and Q_X is closed and nonempty, so q ∈ Q_X.
- **Corollary 5.2.** On X ∩ N, q·x ≥ min_i x_i > −cP(x). On X∖N, q·x ≥ 0 ≥ −cP(x) a.e., because P > 0 a.e. on X; this is stated earlier. So Q_{X∖N} = Q_X, and N ⊆ N_0 ⊆ G = hull(X∖N).
- **N ⊆ U** because K' ⊆ Q_X.

**The standing assumption K' ⊆ Δ (not relint Δ) — CORRECT.** I searched every proof for a use of K' ⊆ relint Δ. Sections 3–5 and Remark 7.2 use only:
- (i) U ∩ {h : h ≤ 0} = ∅, and in particular U ∩ {h ≪ 0} = ∅;
- (ii) every coherent model contains int ℝⁿ₊;
- (iii) K' ≠ ∅, used in Lemma 2.2(a) and Step 2.

All three hold for any nonempty compact convex K' ⊆ Δ.

The note's proofs are written directly under this assumption. So the extension to K' ⊆ Δ is *proved*, not just asserted by inspection. I re-checked each place:
- the existence of i(r);
- Theorem 4.1(b);
- Corollary 4.2;
- Remark 7.2(b),(c).

Under the coverage clause, a K' that meets ∂Δ yields a ranking that covers nothing, because K' ⊆ relint K ⊆ relint Δ is forced. That is consistent with the sentence after the proof of Theorem 6.1. *Optional:* say explicitly that the coverage set is then empty, although (a)–(d) still hold.

**NUMERICS** (two worlds, 80 rivals, `thmH_2d_sanity.out`): there were 0 failures of the margin, of N ⊆ hull(X∖N), of μ(N∖X) > 0 or of Q_{X∖N} = Q_X.

**Remark 5.4.**
- (a) is CORRECT: no use of regularity, pointedness, dim K' or relint Δ.
- (c) is CORRECT: Step 1 with G = U.
- (b) has the minor GAP noted in item 5.
- **(d) is a GAP at journal standard.** It states a "generation" lemma whose proof is omitted, together with the claims "the hypothesis cl N_1 ∩ L = {0} cannot be dropped in general" and "Securing it uses K' ⊆ relint Δ". None of these is proved or illustrated in the note. The remark is also a record of an alternative route, which is history rather than content.
  - *Repair:* delete (d). Alternatively, reduce it to a single sentence with no mathematical claims ("A second proof generates hull(X) from support points of X; we do not pursue it.").

### 7. Main theorem §6 — CORRECT (scope clauses accurate)

- **(a)** This is Theorem 4.1(a). "Sub-relation of Brier, symmetric on Brier ties" is exactly Brier compatibility plus tie symmetry.
- **(b)** It follows from (H) via Theorem 5.3, Corollary 4.2 and Theorem 4.1(b),(e): 𝒰 = 𝒞* = 𝒞_U, and no weak dominator other than itself.
- **(c)** "Strictly dominated" follows from Theorem 4.1(c) with m(N) − m(X) ≫ 0. "Uniformly dominated in Brier loss" is the same inequality, with c_i finite by (M). N is undominated by (b).
- **(d)** (GC), (ID), (W), and (C) in its strong form.
- **(e)** Cover ⟺ (K' ⊆ K and (LF)) ⟺ (K full-dimensional and K' ⊆ relint K), by Lemma 2.5(a)–(c). U is one-sided because U ∩ (−U) = ∅. The "full-dimensional" qualifier is present, so the earlier scope error flagged in REF65_hA f2 has been repaired.
- **Corollary 6.2 (every full-dimensional K is covered on some domain):** CORRECT, with K' = {k_0} and k_0 ∈ relint K.
- **Proposition 6.3 (lower-dimensional targets excluded on one-sided domains):** CORRECT, via Lemma 2.5(c).
- **The paragraph after Proposition 6.3.** The citations [KCM, Prop. 2.10] and [KCM, Cor. 5.9] match the current paper's numbering (I checked the aux file in `w65build/`). The statements match the paper:
  - essentially one-sided domains are excluded;
  - the Brier ranking covers precise {p}, p ∈ relint Δ, on the full domain.
- **"Two-sided domains open"** is stated accurately. Two points are correctly identified:
  - Q_B may be empty, which breaks Corollary 4.2's attack on hull(B);
  - Step 2 uses an element of K'.
  
  The claim that the construction "still makes sense" is also right. Existence of i(r) needs only that coherent models contain int ℝⁿ₊ and no h ≤ 0.
- **§7.1** is CORRECT. For any ranking on ℳ_{D_{K'}}, a cover of a full-dimensional K forces K' ⊆ relint K, because Lemma 2.5 does not depend on the ranking.

### 8. §7 — Example 7.1 CHECKED; Remark 7.2 CORRECT; one scope ERROR in the abstract

**Example 7.1 — CHECKED exactly** (`ex71_exact.out`, 138 full-dimensional cells, using the unnormalised density e^{-|h|_1}). The sanity checks pass: total mass 8 and total first moment 0. The results:
- K' ⊆ Q ⊆ K, N ⊆ U and D_K ⊆ N: True.
- m(D) = (68269/2370816)𝟙; m(S_1) = (1691077/59270400, 122655769/2963520000, −58937269/2963520000); m(S_2) = (163/617400, −37319519/2963520000, 16030391/329280000). **All three match the note exactly**, and m(S_1) + m(S_2) = m(D).
- μ(N ∩ {v_2·h < 0, h_1 < 0}) = 1853/70560: **matches**. Also μ(D ∩ {h_1 < 0}) = 737/14112 > 0.
- The required signs hold: m_1(S_1) > 0 > m_3(S_1); m_1(S_2) > 0 > m_2(S_2); m(D) ≫ 0.
- The deletion world of (D, ∅) is 1.

The logical steps in the example are right:
- (S_1, ∅) ∉ ℛ, and it is not an inverse, since −m(S_1) ∉ ℝⁿ₊;
- the same holds for (S_2, ∅);
- (D, ∅) ∈ ℛ(𝒩) for every 𝒩 ∋ D_K, and it is deleted at world 1;
- S_1 ∩ S_2 = ∅.

So (Tr) and (Add) fail at world 1, and Y_0, Y_2 are incomparable there, consistently with (FCC).

**Remark 7.2 (LD(𝒩)) — CORRECT.**
- **(a)**
  - The null record lies in G_i.
  - **(G):** the inverse of a non-null record in G_i has L_i <_lex 0 and is not in G_i.
  - Every accepted record has L_i ≥_lex 0. An accepted record with L_i = 0 is null or lies in the third set, which is closed under inverses. So Lemma 3.2 applies with T = ℝ² ordered dually to lex. This gives (FCC) and (TC).
  - **(Add):** I checked the identity r(X,Z) = r(X,Y) ⊔ r(Y,Z) for non-overlapping steps. For closure under ⊔:
    - both records in G_i: the union is in G_i;
    - otherwise r_1 ∈ NA, so the union is in NA by the "fact". L_i is additive, and since ℝ²_lex is an ordered group, a zero sum forces both terms to be zero. Then the third-set condition passes to the union through the inverse.
- **(b)** A weak dominator's record attacks N. So it must be in G_i at every world, which forces Y = N a.e.
- **(c)**
  - **(★) ⇒ dominance:** Σ_j m_j(r) > 0 gives L_i >_lex 0 at every i, so the dominance is *strict*.
  - **Dominance ⇒ (★):** a record that is not in NA would have to be (A, ∅) with A ⊆ int ℝⁿ₊ non-null. Such a record attacks no coherent model, which is a contradiction. If m(N) = m(X), the record is in the third set at every world, so the reverse comparison holds.
- **(d)** This follows by Corollary 4.2 and Theorem 5.3. **The "only if" direction is scoped to LD(𝒞_U) itself**, and the text says explicitly that it does not say every (Add)-ranking cover yields (H). This repairs REF65_ad E1. Transitivity is not claimed.

Minor points on Remark 7.2:
- (i) "reverse lexicographic order" is ambiguous, since it usually means colex. Write "the order dual to ≥_lex", or apply Lemma 3.2 with φ := −Φ_i under ≤_lex.
- (ii) This is a result with a proof, and the abstract relies on it. Promote it to an unnamed Proposition.

**Scope statements (§7.2, §7.3, §7.4) — CORRECT and not editorialised.**
- §7.2 states that the ranking *represents* coherence and does not derive it from accuracy considerations specified independently of coherence.
- It notes that the dominance part is not definitional, because (ID) ⟺ (H).
- It notes cross-world dependence.

Wording nit: "Theorem 6.1 shows that, under (G), (IB), (TC) and (FCC), …" should read "…that, by a ranking satisfying (G), (IB), (TC) and (FCC), …". The §7.4 claims also hold: strict CD comparisons are Brier-strict; the relation is incomplete; and there are coherent models that are uniformly Brier-dominated yet undominated.

**ERROR (scope), abstract.** The abstract says "The ranking … is not transitive, and violates disjoint additivity." This is proved only for one instance: n = 3, the reversed-triangle K', and the density e^{-|h|_1}. The body says it correctly ("satisfies neither (Tr) nor (Add) *in general*").
- *Repair:* "… need not be transitive and can violate disjoint additivity."

**GAP (undefined term).** "Universal cover" and "universal coverage" (title, abstract, §6 heading, §7.3) are never defined.
- *Repair, a nearby result that is available and makes the word precise:* add a corollary after Theorem 6.1: **"For U = D_{K'}, CD(𝒞_U) covers K if and only if some ranking on ℳ_U covers K."**
- *Proof:* if any ranking on ℳ_U covers K, then D_K ∈ ℳ_U and (LF) holds at D_K. So K' ⊆ K, K is full-dimensional by Lemma 2.5(c), and K' ⊆ relint K by Lemma 2.5(b). Then apply Theorem 6.1(e).
- Then define "a universal cover on U" as a ranking that covers every credal set that is coverable on U, and say the same for LD(𝒞_U).

The abstract also says "we delete … each comparison that would let a model weakly dominate a coherent model, *and nothing else*". This is loose: the reverse comparisons on Brier ties are also deleted, and deletions apply to every pair with the same record.
- *Repair:* "… each comparison whose record would let some model weakly dominate a coherent model, together with its reverse on Brier ties, and nothing else."

### 9. Conventions — CORRECT (one self-containment point)

- I grepped for names on theorem-like environments: none.
- No ":=" appears; `\coloneqq` is used throughout.
- The objects are called "models".
- The dominance terms are standard and match the paper.
- I grepped for project-internal labels (ES64, H65, X65, WT65, AD65, REF, round, R_lex, "auditor", "referee", "project"): none.
- The paper compiles cleanly.

Self-containment:
- every result used in the main line is proved in the note;
- [KCM] is cited only in side remarks;
- Rockafellar 11.6, Sion and Lyapunov/Lindenstrauss are standard and the bibliographic data are correct.

Two exceptions:
- Remark 5.4(d), which states unproved material (item 6);
- (M) is not declared as a standing assumption, although Theorem 4.1 (moments), Lemma 4.3 and Corollary 4.4 (density points via μ) use it. Only Theorems 5.3 and 6.1 say "Assume (M)".
  - *Repair:* "Throughout, μ satisfies (M)."

Intro wording: "a ranking covers a coherent model D_K" should become "covers a credal set K" (Definition 2.4).

## Required changes, ranked

1. **Abstract scope (ERROR).** "is not transitive, and violates disjoint additivity" → "need not be transitive and can violate disjoint additivity (Example 7.1)".
2. **Define "universal cover/coverage" (GAP).** Add the corollary "CD(𝒞_U) covers K ⟺ some ranking on ℳ_U covers K" (two-line proof from Lemma 2.5 and Theorem 6.1(e)), and use it to fix the meaning of the title, the abstract and §7.3. State the same for LD(𝒞_U).
3. **Remark 5.4(d) (GAP).** Delete it, or strip it of all unproved claims: the generation lemma, "cannot be dropped", and "uses K' ⊆ relint Δ".
4. **Remark 7.2 → Proposition.** It carries a proved result that the abstract relies on. Also replace "reverse lexicographic order" with "the order dual to ≥_lex", or use φ := −Φ_i.
5. **(M) as a standing assumption.** Theorem 4.1, Lemma 4.3 and Corollary 4.4 use it implicitly.
6. **Remark 5.4(b) (minor GAP).** Add the one-line density argument: density points of an open convex set are its points, so N_d ⊆ N ⊆ hull(X∖N).
7. **Abstract "and nothing else".** Add "together with its reverse on Brier ties", and say that deletion is by record.
8. **Terminology alignment.**
   - Add the (LF) gloss "that is, X ⊆ U a.e.".
   - Note that "one-sided" here (U ∩ (−U) null) differs from [KCM]'s "one-sided" (empty).
   - Intro: "covers K", not "covers a coherent model D_K".
9. **Small expository points.**
   - After Lemma 3.2: "real score" → "score in a totally ordered set".
   - Lemma 4.3: add "(let s → ∞)".
   - §7.2: "under (G)…" → "by a ranking satisfying (G)…".
   - Optional: after Theorem 6.1, note that a K' meeting ∂Δ gives an empty coverage set, although (a)–(d) still hold.

None of these affects the correctness of Theorems 4.1, 5.3 and 6.1, Corollaries 4.2, 4.4 and 6.2, Proposition 6.3, Example 7.1 or Remark 7.2.

## Status table

| Item | Verdict |
|---|---|
| 1 Framework | CORRECT (minor: (LF) gloss; "one-sided" differs from [KCM]) |
| 2 Lemma 2.5 (a)(b)(c); Lemmas 2.1, 2.2 | CORRECT |
| 3 Deletion lemma (FCC/TC, totally ordered T) | CORRECT (gloss says "real") |
| 4 CD(𝒩), i(r), tie symmetry, strict (G), attack, Thm 4.1(a)–(e) | CORRECT |
| 5 Cor 4.2 ((ID) ⟺ (H)); Lemma 4.3; Cor 4.4 | CORRECT; Remark 5.4(b) minor GAP |
| 6 Thm 5.3 Steps 1–3; Lemma 5.1; Cor 5.2; K' ⊆ Δ extension | CORRECT (PROVED; NUMERICS 80/80); Remark 5.4(d) GAP |
| 7 Thm 6.1 (a)–(e); Cor 6.2; Prop 6.3; two-sided left open | CORRECT |
| 8 Ex 7.1 | CHECKED (exact; every printed rational matches) |
| 8 Remark 7.2 (LD) incl. scoped "only if" | CORRECT (promote to Proposition) |
| 8 Scope statements | CORRECT in body; abstract ERROR ("is not transitive…"); "universal cover" undefined (GAP) |
| 9 Conventions | CORRECT; (M) not declared as a standing assumption |

**Recommendation:** accept after minor revision (changes 1–9).
