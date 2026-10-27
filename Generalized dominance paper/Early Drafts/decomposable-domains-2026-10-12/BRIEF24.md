# Brief, round 32 (17 Oct 2026): synchronized seeds, patched posterior family, defence regions

Read FIRST:
- **AUDIT_CC_seeds.md:** audit's note "CC1–CC3 Assessment and Synchronized Seeds". It contains the bundle construction and its proofs.
- **AUDIT_CC_summary.md** and **AUDIT_CC_plan.md:** audit's two messages, the second with the concrete construction plan.
- **CC1_notes.md:** the seed, its seven regions, the four seed comparisons, and the obstruction Theorem 4.1.

## Audit's construction (to be extended)
- **Synchronized seeds.** Take small pieces of CC1's seven regions and match their points into seven-problem BUNDLES, each carrying the four seed patterns. A seed comparison is permitted on ANY measurable collection of bundles.
  - Within a bundle, two seed applications cannot compose.
  - The resulting world-1 preorder has strict (G), (IB), and a graph closed under convergence in measure.
  - Every positive-measure collection of bundles carries the four-comparison certificate. So there is non-additivity AT EVERY SCALE.
  - With the guidance order alone at worlds 2 and 3, the four coherent seed models (T1 included) are undominated. The result is a system with (G), (IB), (LA), (C), (LF) and closed comparison graphs. It lacks only (S).
- **Seeds are to be RETAINED, not used as an upper bound.** Requiring agreement bundle by bundle would impose vetoes. Compensation between bundles must be permitted without turning into additive pricing.
- **Coupling warning.** The seven regions cannot be made independently interchangeable. Splitting the bundle parameter into four parts, applying one seed on each, and rearranging within regions yields a pure guidance improvement. So compensation must preserve WHICH changes belong to the same bundle: whole bundle patterns are exchanged, and their components are never rearranged independently.

## Concrete plan (audit)
1. **The coherent family.**
   - Start from the posterior family K_p^0 = co{ p⊙v_k/(p·v_k) : k = 1,2,3 }, where v_k are T1's vertices.
   - Patch it with bumps: K_p = (1 − Σβ_k(p))K_p^0 + Σβ_k(p)K_k, passing through the other seed credal sets K_2, K_3, K_4 at designated interior indices.
   - The result is continuous on Δ, gives T1 at u, and keeps the boundary family.
2. **Defence regions.**
   - For each competitor X choose r(X) ∈ Δ, and require C_p ≼_i X ⟺ p_i ≥ r_i(X). These regions are closed and automatically cover Δ using supported worlds.
   - Set r(C_q) = q, so that C_p ≼_i C_q ⟺ p_i ≥ q_i.
   - Seeds impose inequalities: a retained C_{q_k} ≼_1 X_k^A needs r_1(X_k^A) ≤ (q_k)_1.
3. **Close and check.** Close under (IB) and actual composition, forbidding:
   - guidance reversals;
   - domination of selected models;
   - incoherent all-world ties.

   Every generated comparison out of a selected model must respect its defence region.
4. **The decisive lemma.** A new competitor can always be assigned a defence vector without creating a forbidden finite composition.
5. **If coordinate thresholds fail,** relax them to general closed covers. Keep the family and the seeds, and say exactly which assumption failed.

## Read also
- AUDIT_BB.md and AUDIT_AA.md.
- CC2_notes.md and CC3_referee.md.
- Y1_notes.md (monotone rays of the posterior family; relevant to C_p ≼_i C_q ⟺ p_i ≥ q_i).
- X1_notes.md, AUDIT_nonlinear_programme.md.
- writeup §2.

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it.
