# Round 82 brief: a self-contained note on cover rankings built from rescaled families (writer W82)

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r82/

## Inputs (same folder, read-only)
- **LR.tex** — "Loss Relations for Sets of Desirable Gambles". Read in full; it is the template for the loss construction, the Gaussian estimates and the budget lemma. Its Theorem (thm:main) assumes (U), (Lip) and (Dom), with standard Gaussian μ.
- **HOM.tex** — "Full Coverage by Homothetic Credal Families". Read §1, §2 (Thm family) and the section "Full coverage by bounded real-valued losses" (Thm numerical). It replaces (U) by compatibility of covers (CC), and builds a family through *every* credal set M satisfying (CC), (Lip) and (Dom).
- **ldgshort.tex** — the LDG Short paper. Use its exact definitions: ranking, dominance, C_L, closed under ties, Theorem thm:finite, Corollary cor:closed-choice, and the conditions (E), (A), (S), (T) in def:argument-assumptions. Note that in LDG, ⪯ means "at least as good".
- **appshort.tex** — the application Short paper. Use its names and statements for:
  - the measure conditions (M1)–(M3);
  - "almost coherent";
  - "change … guided at ω";
  - axiom (A1).

  Note that the application writes ⪰ for "at least as good". In the note, use LDG's convention.

## The author's request (binding)
"Is there a way to slightly generalise the approach to yield (A) for every coherent model? It is fine to introduce plausible restrictions on μ. Also fine to leave infinitely many worlds open for now. It is expected that L^M dominates every coherent model outside its family. Fine for 'guided at ω' to mean a non-null reduction of the errors at ω. Try to settle this. If we can generalise to yield (A) for every coherent model, then write up as a self-contained tex file with referee. Check that (E), (A), (S) and (T) all hold. We should only expect these conditions to hold for approximate coherence, not for coherence itself."

The author's aim: one ranking L^M per target credal set M. Where possible, (S) should hold with the assigned models c_p = D_{K_p}, where K_p = {p∗m/(p·m) : m ∈ M} (the *rescaled family*, with p∗m the componentwise product).

## Setting of the note
- Ω = {1,…,n}, n ≥ 2. Gambles are g ∈ ℝⁿ.
- μ is a Borel probability measure on ℝⁿ. Models are μ-measurable sets of gambles, with the completion of μ.
- **Coherent class.** 𝒞 = the *almost coherent* models: those X with X ≈ D for a coherent set of desirable gambles D, where D satisfies (D1)–(D4). Here ≈ means equality up to a μ-null set.
- D_K, φ_K, E_i(X) = X Δ G_i, G_i = {g_i > 0}, and X ≤_i Y iff E_i(X) ⊆ E_i(Y) a.e., all as in HOM.tex.

**Measure conditions.**
- (M1) finite first moment.
- (M3) full support: every nonempty open set has positive measure.
- **(M5), new: bounded density along constant shifts.** Write t(g) ≔ (1/n)Σ_k g_k and h(g) ≔ g − t(g)𝟙. There is c_μ < ∞ such that for all Borel a : ℝⁿ → ℝ and b : ℝⁿ → [0,∞),
  μ{g : |t(g) − a(h(g))| ≤ b(h(g))} ≤ 2c_μ ∫ b(h(g)) dμ(g).
  - Plain English: along every line of gambles that differ by a constant amount, μ has a bounded density.
  - Show that standard Gaussian μ satisfies (M5), since t and h are independent and t has density ≤ √(n/2π).
  - Show that the application's existence measure satisfies (M5), if appshort.tex defines one. This is the symmetric discrete measure pushed by g ↦ g + u𝟙 with Gaussian u: conditional on an atom, t has a Gaussian density. State and check the exact construction there.
  - Show that (M5) implies (M2): μ{φ_K = 0} = 0 for every credal set K. Apply (M5) with b ≡ 0, using φ_K(h + t𝟙) = φ_K(h) + t.
- Put C_μ ≔ max{2, 8c_μ ∫‖h(g)‖_∞ dμ}, which is finite by (M1).

## Results to state and prove (all proofs complete, self-contained)

### 1. Ranking-free facts
- (F1)–(F5) of HOM.tex.
- **Error-minimality of coherent sets.** If D is a coherent set of desirable gambles and E_i(X) ⊆ E_i(D) a.e. for every i, then X ≈ D.
  - *Proof.* g ∈ D∖X with g ∈ G_i would contradict D∩G_i ⊆ X; so g ≤ 0, and D contains no such g except on a null set. g ∈ X∖D with g ∉ G_i would contradict X∖G_i ⊆ D; so g > 0 coordinatewise, and then g ∈ D.
- **Lemma coherent** of HOM.tex: every coherent D has D ≈ D_M for its credal set M. Under (M5) this holds with μ in place of Lebesgue measure.
- **Lemma endpoints** of HOM.tex, using (M3) for "open ⇒ non-null".

### 2. General cover-ranking theorem (the "slight generalisation")
Let p ↦ K_p be any family of credal sets on Δ satisfying:
- **(CC)** compatibility of covers;
- **(Lip)** with constant A;
- **(Dom)** with constant B.

Assume (M1), (M3) and (M5). Define κ ≔ 2nC_μ(A + 2B) and fix 0 < η < 1/(nκ). Define L^K as in eq. (10) of HOM.tex / Def. loss of LR: min over covers of [1 − p_i − η·μ(E_i(D_{K_p}) ∖ E_i(X))], and 2 + μ(E_i(X)) if uncovered. Prove LR thm:main (a)–(f) in this generality, with (U) replaced by (CC). That is, prove:
- **(a)** Range [0,1] ∪ [2,3]; weakly monotone in error inclusion, and strict for non-null reductions; invariant under null modification.
- **(b)** L(D_{K_q}, i) = 1 − q_i.
- **(c)** D_{K_q} is competitive on supp q.
- **(d)** The sections {q : D_{K_q} ⪯_i X} = {q : q_i ≥ 1 − L(X,i)} are closed.
- **(e)** If X weakly dominates D_{K_q}, then X ≈ D_{K_q}.
- **(f)** Every model is weakly dominated by some D_{K_q}, and dominated unless X ≈ some D_{K_p}.

Replace the Gaussian constants by C_μ:
- *Lemma thin:* μ{|φ_K(g)| ≤ δ‖g‖_∞} ≤ C_μ δ. Re-prove it from (M5) with b(h) = 4δ‖h‖_∞ and a(h) = −φ_K(h), for δ ≤ ½; for δ > ½ the bound is trivial since C_μ ≥ 2.
- Then μ(D_K Δ D_{K′}) ≤ C_μ d_H(K, K′).
- *Lemma faces:* each set is bounded by 2nC_μ B q(T^c).
- *Budget:* s_j ≤ 2nC_μ(A + 2B)ρ = κρ.

Check every constant.

Then state the consequences in LDG terms, for the single ranking L^K with M_L = all models and coherent class 𝒞 = almost coherent models:
- C_L = {X : X ≈ D_{K_p} for some p};
- (S) holds via cor:closed-choice with c_p ≔ D_{K_p} ∈ C_L;
- L is closed under ties;
- every model outside C_L, incoherent or almost coherent, is dominated, in fact strictly dominated at every world by some D_{K_q} (LR's argument with q = β + slack);
- the ranking satisfies the application's (A1). Its "guided" change is a non-null reduction of errors at every world.

Remark: under **exact** coherence as the coherent class, (T) fails. A null modification of D_{K_p} by a non-coherent null set is tied with it at every world but is not coherent. This is why the conditions hold only for almost coherence.

### 3. The rescaled family (targets M ⊆ int Δ)
Let M ⊆ int Δ be closed and convex, δ ≔ min_{m∈M} min_k m_k > 0, and K_p ≔ {p∗m/(p·m) : m ∈ M}. Prove:
- **(i)** K_p is a credal set: a linear-fractional image with positive denominator preserves convexity. Also K_u = M, K_{e_i} = {e_i}, and K_p ⊆ relint Δ_{supp p}. The sign of φ_{K_p}(g) equals the sign of φ_M(p∗g), for all p ∈ Δ and g.
- **(ii) (Lip)** with A = 2/δ. For fixed m: F_k(p) − F_k(q) = m_k[p_k(q·m − p·m) + (p_k − q_k)(p·m)]/((p·m)(q·m)). Summing gives ‖F(p,m) − F(q,m)‖₁ ≤ 2‖p−q‖₁/(q·m) ≤ 2‖p−q‖₁/δ. Pairing images of the same m gives the Hausdorff bound.
- **(iii) (Dom)** with B = 1/δ.
- **(iv) (U) fails.** M = {(0.3, 0.05, 0.65)}, p = (0.4, 0, 0.6), q = (0.3, 0.7, 0). The upper probabilities of world 1 are 0.12/0.51 ≈ 0.235 and 0.09/0.125 = 0.72. Put this in a remark: it is why LR's theorem does not apply directly.
- **(v) (CC) holds (lead's proof, to be written out carefully).**
  - *Statement.* If D_{K_p} ∩ W_{ij} ⊆ D_{K_q} a.e., where W_{ij} = {g_i > 0 ≥ g_j} and i ≠ j, then p_i ≤ q_i. Lemma endpoints' first display shows that X ≤_i D_{K_p} and X ≤_j D_{K_q} give the hypothesis.
  - *Setup.* Assume p_i > 0. Let U = {g ∈ W_{ij} : φ_M(p∗g) > 0 > φ_M(q∗g)}. It is open, lies in D_{K_p} ∖ D_{K_q} by (i), and so is empty by (M3).
  - *Step 1: supp q ⊆ supp p.* If q_l > 0 = p_l, then l ≠ i. Take g = e_i/p_i − s·e_l with s > q_i/(p_i q_l δ). Then g_i > 0 and g_j ≤ 0, p∗g = e_i with φ_M(e_i) ≥ δ, and m·(q∗g) < 0 for every m. So g ∈ U.
  - *Step 2.* Let S = supp p and d_l = q_l/p_l (l ∈ S). Claim: d_i ≥ d_l for all l ∈ S. Suppose d_l > d_i.
    - *Case l ≠ j.* Let h = e_i − ε e_j − t e_l, with the ε term only if j ∈ S. Let g be given by g_k = h_k/p_k on S and g_k = 0 off S. Then g ∈ W_{ij}, p∗g = h and q∗g = d∗h.
    - Let t* = min_{m∈M}(m_i − εm_j)/m_l > 0 for ε < δ. For t < t*, φ_M(h) ≥ δ(t* − t) > 0.
    - At a minimiser m*, at t = t*, m*·(d∗h) = (d_i − d_l)m*_i + ε(d_l − d_j)m*_j ≤ −(d_l − d_i)δ + ε(d_l + d_j) < 0 for small ε. By continuity this stays negative for t slightly below t*. So g ∈ U.
    - *Case l = j.* Use h = e_i − t e_j and ε = 0.
  - *Step 3.* 1 = Σ_{l∈S} p_l d_l ≤ d_i, so q_i ≥ p_i. ∎
  - The lead checked this numerically: 187 random cases with n = 2…5, including boundary indices, found no failure.
- **Conclusion.** For M ⊆ int Δ, Theorem 2 applies, with c_u = D_M. So the rescaled family gives (S) with c_p = D_{K_p}, exactly as the author wanted.

### 4. Targets touching the boundary
- **(a) Coverage by rescaled families from interior targets.** The coherent models that are D_{K_p} for some interior target M and some p are exactly the D_{M′} with M′ ⊆ relint Δ_S, where S is the union of the supports of members of M′.
  - For ⊇: take M = (1−ε)M′ + εw, with w uniform on S^c (M = M′ if S = [n]), and p uniform on S.
  - For ⊆: K_p ⊆ relint Δ_{supp p}.
  - So the vacuous model D_Δ, and models like D_{conv{e₁,u}}, are not covered.
- **(b) Obstruction (lead's proof; write it out and check it).** Let n = 2 and M = Δ. Then K_p = Δ for interior p and K_{e_i} = {e_i}, so the assigned models would be D_Δ, G_1 ≈ D_{e_1} and G_2 ≈ D_{e_2}. No ranking satisfying the guidance axiom (A1) at a single world satisfies (S) with these assigned models. (A1) here means: if E_ω(Y) ⊆ E_ω(X) a.e. and μ(E_ω(X) ∖ E_ω(Y)) > 0, then Y ⪯_ω X and not X ⪯_ω Y.
  - *Witness.* Let X = D_Δ ∪ N with N ⊆ W_{12} = {g_1 > 0 ≥ g_2} non-null and W_{12} ∖ N non-null, e.g. N = W_{12} ∩ {g_1 > 1}.
  - *World 1:* E_1(X) = E_1(D_Δ) ∖ N, so D_Δ ⪯_1 X fails.
  - *World 2:* E_2(X) ⊊ E_2(G_1) non-null, so G_1 ⪯_2 X fails.
  - *World 1 again:* E_1(X) ⊊ E_1(G_2) non-null, so G_2 ⪯_1 X fails.
  - So no assigned model weakly dominates X, contradicting the conclusion of thm:finite / cor:closed-choice.
  - Verify each inclusion, up to null sets, with D_Δ ≈ {g_1 > 0, g_2 > 0}. Say plainly that for n ≥ 3 the analogous question is open, unless you or the referee can settle it.
  - Also include the n = 3 example M = conv{e₁, e₂, u}. Its rescaled family conv{e₁, e₂, p} fails (CC): X ≔ D_{K_p} ∪ D_{K_q} satisfies X ≤_1 D_{K_p} and X ≤_2 D_{K_q} for all interior p, q, since every D_{K_p} ⊆ G_1 ∩ G_2 a.e.
- **(c) Remedy.** For targets M ⊄ int Δ, use the homothetic family of HOM.tex, Thm family:
  - (CC) via the endpoint identity;
  - (Lip) with A = 1 + 2/min{d_i : d_i > 0}, or A = 1;
  - (Dom) with B = 1/λ, from the remark after Thm family;
  - K_r = M.
  Re-prove what is needed, briefly, so the note is self-contained.

### 5. The class and the dominance argument
Define 𝔏 ≔ {L^M : M a credal set}. L^M is built from the rescaled family if M ⊆ int Δ, and from the homothetic family otherwise. Under (M1), (M3) and (M5), verify each of the following against ldgshort.tex's exact wording:
- **(E)** every L^M evaluates every model;
- **(A)** every almost coherent model belongs to C_L for some L ∈ 𝔏: X ≈ D ≈ D_M = c_r, and X is tied at every world with c_r, so it is undominated;
- **(S)** holds for every L;
- **(T)** holds for every L.

Then state the conclusion of LDG thm:argument:
- the rationally permissible models are exactly the almost coherent ones;
- each L^M dominates every model, almost coherent or not, outside its family;
- every ranking satisfies (A1).

Also say that (A2)–(A4) of the application are **not** checked here.

## Style
- Self-contained LaTeX article, file **rescaled-coverage.tex**. Title: "Rescaled Credal Families and Coherent Admissibility". No author line.
- Lemmas, theorems and propositions are unnamed. Definitions may have short names in brackets.
- Use \coloneqq. Plain English.
- No jargon: avoid "certificate", "record", "safe", "route", "dangerous", "shelter". Say "via Corollary …" or "by Corollary …".
- Use only one-sentence plain-English glosses of the measure conditions and axioms. No other exposition.
- Every claim has a complete proof or a precise citation to a result proved in the note itself. Do not cite LR or HOM as authorities: re-prove what you use. You may cite LDG (Konek, *Coherence and Dominance under General Rankings*) for thm:finite, cor:closed-choice and thm:argument. Restate them precisely, in a short preliminary section, so the reader can check the hypotheses.
- Compile with pdflatex until clean: no errors, no undefined references, no overfull boxes. Output rescaled-coverage.pdf.
- Also write W82_report.md. List anything you could not prove, or that you found false. Label claims PROVED / CHECKED / UNCLEAR / FAILS.

Final message: under 250 words.

## Addendum (lead)

**(M3) in the application.** appshort's (M3) is "full support of the diffuse part μ_c", because atoms are allowed there. (M5) with b ≡ 0 excludes atoms, so under (M5) μ is atomless, and (M3) is plain full support. State this.

**The application's existence measure** is in lem:measure of appshort.tex. Fix ω₀ and put E₀ = {g : g(ω₀) = 0}. Take
ν = Σ_k (w_k/2)(δ_{g_k} + δ_{−g_k}),
with (g_k) dense in E₀, and push ν ⊗ N(0,1) forward under (g, u) ↦ g + u𝟙. Then h(g + u𝟙) = h(g) and t(g + u𝟙) = t(g) + u, so (M5) holds with c_μ = 1/√(2π). Verify this.
