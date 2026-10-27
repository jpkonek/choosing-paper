# Round 73 brief: how promising is consolidation? (27 Oct 2026)

Read first: ROUND72_report.md (§1 has the axioms and §2.4 the summary), AX72_report.md §C3 (lines ~128–215: the definitions, C3.1–C3.8), REF72_report.md and REF72b_report.md (corrections), and GUIDANCE_after_r71.md §§2, 6–9 (rules: the axioms must be score-free; the integral may be used only in constructions and proofs).

## The class
𝓡 is the class of rankings, one relation per world, on models: measurable sets of gambles modulo μ-null sets. They satisfy:
- (R) reflexivity;
- (G) strict guidance for models that are not a.e. equal;
- (I) independence;
- (SC) the chain condition (Suzumura consistency);
- (P) every coherent model is undominated (one ranking; the strongest premise).

Closure under ties (CT) is NOT assumed unless a task says so. CT says: a model tied at every world with an undominated coherent model is itself an undominated coherent model.

**Maximal** means maximal under extensions that keep weak and strict comparisons. Inclusion maximality coincides with this above rankings of the manuscript's form (entrenchment lemma), and the inclusion branch is closed.

## Consolidation (C3), chain form, from AX72
A *matched triple* is three pairwise disjoint non-null sets G1, G2, G3 together with bijections T: G1 → G2 and S: G1 → G3, with T_*(μ|G1) = μ|G2, and either:
- (sum) S(h) = h + T(h) and S_*(μ|G1) = μ|G3; or
- (midpoint) S(h) = (h + T(h))/2 and S_*(μ|G1) = ½ μ|G3.

For Z ⊇ G1 ∪ G2 with Z ∩ G3 null, the consolidation is Z′ = (Z∖(G1∪G2)) ∪ G3.

(C3) At no world is there a chain Z ⪰_ω … ⪰_ω Z′ with a strict link. In words: no improving chain leads from the consolidated model to the split one.

## Known (round 72)
- Under (C3), R_{s'} and every distorted-score counterexample are excluded.
- In the integral-score test family, (C3) holds iff every per-world density is superlinear. The Bayes sets are then coherent.
- R0, R∩, the round-71 maximal rankings and veto–Brier satisfy (C3).
- Chain unions preserve (C3), so for finite Ω maximal members of 𝓡+(C3) exist.
- **C3.7(ii)** (proved in outline; step 3 not fully written): under 𝓡+(C3), any model strictly defended against every rival at some world is coherent.
- **OPEN (C3.8):** is every incoherent model dominated in every maximal member of 𝓡+(C3)? Two ways an incoherent model might survive:
  - (a) ties with its consolidations;
  - (b) incomparabilities blocked through other contexts, by independence.
- (C3) uses μ beyond null sets. Matched triples are proved to exist only for rotation-invariant μ on R².

## Labels
PROVED / CHECKED / CONJECTURE / NUMERICS / WRONG. Plain English. No jargon such as "certificate", "record", "safe", "dangerous" or "route" in any paper-ready prose. Write only in this folder: /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r73/
