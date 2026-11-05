# W82 report: rescaled-coverage.tex

**Output:** `rescaled-coverage.tex` and `rescaled-coverage.pdf` (14 pages). pdflatex runs cleanly: no errors, no warnings, no undefined references, no overfull or underfull boxes.

**Answer to the author.** Yes, the approach generalises. Replace the upper-probability condition (U) of LR by the cover compatibility condition (CC). Then each credal set M gets one ranking L^M:
- for an interior target M, L^M is built from the rescaled family, so c_p = D_{K_p};
- for a target that touches the boundary, L^M is built from the homothetic family.

The class 𝔏 satisfies (E), (A), (S) and (T) under (M1), (M3) and (M5). Here the coherent class is the almost coherent models.

## Status of the brief's claims

| Claim | Status | Where in the note |
|---|---|---|
| (M5) excludes atoms and implies (M2) | PROVED | Lemma 1.1(a) |
| Gaussian measure satisfies (M5) with c_μ = √(n/2π) | PROVED | Lemma 1.1(b) |
| The application's measure satisfies (M1), (M3) and (M5) with c_μ = 1/√(2π) | PROVED | Lemma 1.1(c) |
| Under (M5), the application's (M3) is plain full support | PROVED | Section 1 |
| (F1)–(F5) | PROVED | Lemma 3.1 (see Note 1) |
| Error-minimality of coherent sets | PROVED | Lemma 3.3 |
| Lemma coherent, under (M2) | PROVED | Lemma 3.4 |
| Lemma endpoints | PROVED | Lemma 3.6 |
| Added: D_K ≈ D_{K'} forces K = K', under (M3) | PROVED | Lemma 3.5 |
| Added: the two readings of "guided at ω" agree under (M2), and (A1*) implies (A1) | PROVED | Lemma 3.2 |
| Lemma thin, μ{\|φ_K\| ≤ δ‖g‖_∞} ≤ C_μ δ | PROVED | Lemma 4.2 |
| μ(D_K Δ D_{K'}) ≤ C_μ d_H(K, K′) | PROVED | Lemma 4.2 |
| Lemma faces, bound 2nC_μ B q(T^c) | PROVED | Lemma 4.3 |
| Budget, s_j ≤ κρ with κ = 2nC_μ(A + 2B) | PROVED | Lemma 4.5 |
| Theorem 2, parts (a)–(f) with (CC) in place of (U), plus (g) strict dominance at every world | PROVED | Theorem 4.6 |
| LDG consequences for a single cover ranking: C_L, (S) via Corollary closed-choice, closure under ties, strict dominance, (A1) | PROVED | Corollary 4.7 |
| Under exact coherence, (T) fails (D_p ∪ {0}); the conclusion of LDG thm:argument fails too | PROVED | Remark 4.8 |
| Rescaled family (i)–(iii): credal set, sign identity, (Lip) with A = 2/δ, (Dom) with B = 1/δ | PROVED | Proposition 5.1 |
| (U) fails for the rescaled family (0.235 < 0.72) | CHECKED | Remark 5.2 |
| (CC) holds for the rescaled family | PROVED, after one correction (Note 2) | Proposition 5.3 |
| Coverage by rescaled interior families: exactly the credal sets whose members all have the same support; D_Δ and D_conv{e₁,u} are not covered | PROVED | Proposition 6.1 |
| Obstruction for n = 2 | PROVED | Proposition 6.2 and Corollary 6.3 |
| Obstruction for n ≥ 3 | PROVED; the brief calls this open (Note 3) | Proposition 6.2 and Corollary 6.3 |
| n = 3 with M = conv{e₁, e₂, u}: K_p = conv{e₁, e₂, p} and (CC) fails | PROVED | Example 6.4 |
| Homothetic family: credal set, K_r = M, (Dom) with B = 1/λ, (Lip) with A = 1 + 2/δ_M (or A = 1), (CC) | PROVED | Proposition 6.5 |
| (E), (A), (S), (T) for 𝔏, with the conclusions of LDG thm:argument | PROVED | Theorem 7.2 and Corollary 7.3 |
| Numbers of the results cited from LDG: Thm 2.2, Cor 2.3, Thm 2.4, Defs 3.1 and 3.3, Thm 3.4; and App Lemma 4.3 | CHECKED against the numbering in the source files | Section 2 |

## Notes

1. **No items (F1)–(F5) in HOM.tex.** HOM.tex has no items labelled (F1)–(F5). I took them to be the five elementary facts in §1 of HOM:
   - the Lipschitz estimates;
   - translation and superadditivity of φ_K;
   - coherence of D_K;
   - D_K ≈ {φ_K > 0};
   - the error-set identities.

   The note states and proves these as Lemma 3.1.

2. **FAILS, minor: step (v) "Setup".** The brief says U = {g ∈ W_ij : φ_M(p∗g) > 0 > φ_M(q∗g)} is open. That is false, because W_ij = {g_i > 0 ≥ g_j} is not open. The Step 1 witness e_i/p_i − s·e_l has g_j = 0 whenever j ≠ l, so it lies on the boundary of W_ij.
   - **Correction.** If g is such a point, then g − εe_j lies in the open set U° ⊆ W°_ij = {g_i > 0 > g_j} for small ε > 0. This uses monotonicity of φ_M and the Lipschitz bound.
   - With this correction, Steps 1–3 go through as the lead sketched. I added explicit choices: ε < min{δ/2, (d_l − d_i)δ/(d_l + d_j)}, and s* ≥ δ/2.
   - I also tested the witness construction numerically in 9375 random cases (n = 2…6, with zero coordinates in p and q). It never failed.

3. **The n ≥ 3 case is settled, not open.** For every n ≥ 2, rescaling M = Δ assigns c_p = D_{Δ_supp p} ≈ G^+_{supp p}. For these assigned models, (S) fails under any ranking that satisfies (A1*).
   - **Witness.** X = (G₁ ∩ (G₂ ∪ … ∪ G_n)) ∪ N, with N = {g₁ > 1, g_k ≤ 0 for all k ≥ 2}.
   - For n = 2 this is the lead's example, D_Δ ∪ N.
   - For n ≥ 3 the set N may be dropped.

4. **The obstruction uses (A1*), not (A1).** The obstruction needs the world-by-world axiom (A1*), as the brief states. The application's (A1) needs guidance at every world, so it does not reach the n = 2 witness: adding N ⊆ W₁₂ is not guided at world 2. The rankings in 𝔏 satisfy (A1*).

5. **(M3) is not used in Theorem 4.6.** It is still assumed there, as the brief asks. (M3) enters only when (CC) is verified for a particular family.

6. **(A2)–(A4).** The brief says to write that (A2)–(A4) are not checked. I added one line instead: (A2) and (A3) hold trivially, because every relation is induced by a real-valued loss. (A4) is not checked. Infinitely many worlds are left open.

7. **Constants, all checked.**
   - For the rescaled family, κ = 8nC_μ/δ.
   - The homothetic constant A = 1 + 2/δ_M is valid but not sharp. Since ‖p − q‖_∞ ≤ ½‖p − q‖₁ on Δ, A = 1 + 1/δ_M also works. The note does not use the sharper constant.
   - For the Gaussian measure, C_μ ≤ max{2, 8√(n(n−1)/2π)}.

No claim is left UNCLEAR.

## Revisions after referee (REF82)

The version before these revisions is saved as `rescaled-coverage-v1.tex`. I applied all ten MINOR fixes, M1–M10, using the referee's replacement text. The revised note runs to 15 pages and compiles cleanly: no errors, no warnings, no undefined references, no overfull or underfull boxes.

| Fix | Change |
|---|---|
| M1 | The sentence after Definition 2.7 now says (A1\*) is the world-by-world form of (A1): the difference between them is the quantifier over worlds, not what "guided" means. |
| M2 | New Remark 6.4 after Corollary 6.3, with the ranking σ = ℓ + 3ι. Under (A1) alone, (S) and (T) can hold with c_p = D_{Δ_supp p}. So the obstruction genuinely needs (A1\*). The remark needs only (M2). |
| M3 | Remark 5.2 now states (U) and shows that (U) implies (CC) under (M3), via Lemma 3.6(b). |
| M4 | Proposition 5.3 now assumes (M3) only. |
| M5 | (M3) is dropped from Theorem 4.6. The sentence after the theorem now says (M3) is not assumed there. |
| M6 | Remark 7.4 now states (A2) and (A3), in LDG's convention. |
| M7 | Definition 2.1 now says that strict dominance at every world and competitiveness are not notions of LDG. |
| M8 | The first sentence of Remark 4.8 is now restricted to "the rankings of this note". |
| M9 | Lemma 1.1(b) now includes the bound ∫‖g‖_∞ dμ ≤ n√(2/π). |
| M10 | In Proposition 6.1, "under (M3)" now applies only to the "In particular" clause. |

**Check of the M2 proof: PROVED.** I checked the referee's §(b) proof independently.
- **(A1).** For a change guided at every world, A ⊆ G^{++} a.e. and B ⊆ G^{--} a.e. So ℓ(Y) = ℓ(X) − μ(XΔY).
  - If ι(X) = 0, then ℓ(X) = 0, so no such change exists.
  - If ι(X) = 1, then σ(Y) < σ(X).
- **(S).** ℓ(D_{Δ_S}) = 0, because G^{++} ⊆ D_{Δ_S} and D_{Δ_S} ∩ G^{--} = ∅. Also ι(D_{Δ_S}) = 0, because D_{Δ_S} ≈ G_S^+, which uses (M2). So σ(c_p) = 0 is the minimum score.
- **(T).** U_L = C_L = {σ = 0}, and C_L is closed under ties.
- I found no error in the referee's proof.

**Effect on the original report.** Corollary 4.7 still follows: (M2) comes from (M5), and (M3) is not needed there. Theorem 7.2 still assumes (M3), so its statement is unchanged. Nothing else in the report changes.
