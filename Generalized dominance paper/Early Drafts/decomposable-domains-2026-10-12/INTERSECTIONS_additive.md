# Intersections of Additive Rankings (project doc, 16 Oct 2026; copied in summary-verbatim form for agents)

An intersection of additive rankings is a transitive, generally incomplete, non-additive ranking satisfying (G) and (IB). In three worlds it covers no target with an interior credal set that some additive ranking on the same domain does not cover. Consequently no such intersection covers T1 on any decomposable domain with (LF).

**Setting.**
- An *additive ranking* has measurable penalties ℓ_i(g,a), a ∈ A(g), with an integrable envelope h_i ≥ |ℓ_i|, and L_i(X) = ∫ ℓ_i(g, a_X(g)) dμ(g).
- It is *strictly guiding* if ℓ_i(g,·) is strictly increasing in world-i rank on A(g) for a.e. g.
- A model is *q-Bayes* if it minimises q·L.
- Given a family 𝒦 of strictly guiding additive rankings L^k, the intersection R is: X R_i Y iff L^k_i(X) ≤ L^k_i(Y) for every k.

**Theorem (transfer).**
- *Hypotheses.* 𝓜 is decomposable with (LF) at D_K, K ⊆ Δ°. R is an intersection satisfying (LA), (S), (C), with D_K ∈ 𝒞_R.
- *Conclusion.* There is a strictly guiding additive ψ with integrable envelope such that:
  - (a) for every q ∈ Δ° the q-Bayes model of ψ is a.e. unique and coherent;
  - (b) D_K is p*-Bayes for some p* ∈ Δ°.
- Hence ψ covers D_K (Theorem ccibu of the write-up).

**Proof steps.**
1. **Mixture.** L¹ is separable, so 𝒦 has a countable dense subfamily 𝒦₀. Put ψ = Σ_k w_k L^k with w_k > 0 and summable envelopes.
2. **Strict comparisons transfer.** X R_i Y implies ψ_i(X) ≤ ψ_i(Y). If also not Y R_i X, then ψ_i(X) < ψ_i(Y). Reason: some k has L^k_i(X) < L^k_i(Y); by density some k' ∈ 𝒦₀ does too, and w_{k'} > 0.
3. **Interior Bayes models are coherent.** Let B be q-Bayes for ψ, q ∈ Δ°. If X dominated B in R, Step 2 would give q·ψ(X) < q·ψ(B). So B is undominated in R. By (LA), (S) and KKM, B is tied at every world with some C_p; by (C), B is coherent.
4. **Uniqueness of Bayes models.** Two q-minimisers on a non-null set would give two coherent Bayes models whose difference is a bounded non-null cone, which is impossible.
5. **D_K is Bayes at a weighting supported in supp p0.**
   - D_K is tied with some selected C_{p0} (KKM), so ψ(D_K) = ψ(C_{p0}).
   - Competitiveness on S = supp p0, with Step 2, says no X is ψ-better on all of S.
   - The attainable set {ψ(X)} is convex (Lyapunov). Separation gives w ∈ Δ, supp w ⊆ S, with D_K w-Bayes.
6. **w is interior.** If w_j = 0, (LF) gives an open ball O of gambles near ∂D_K, with g_i > 0 for i ≠ j, on which accepting is available and D_K does not accept. Strict guidance then makes D_K not w-Bayes.
7. **Conclusion.** Theorem ccibu applies, so ψ covers D_K. That contradicts gm.

**Remark.** Strict (G), (IB) of R hold automatically. Step 2 is the key difference from general "adds up" rankings: there, supporting assessments endorse comparisons only weakly, so strict comparisons can become ties, which produces exceptional weightings. The argument applies to unanimity over any family of countably additive integral losses sharing the domain. It does NOT cover families with purely finitely additive parts: Step 2 needs a countable dense subfamily and integral penalties.
