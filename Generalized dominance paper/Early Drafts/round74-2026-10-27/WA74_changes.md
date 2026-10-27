# WA74 changes: app_r70.tex -> core.tex

27 Oct 2026. `core.tex` compiles cleanly with pdflatex (latexmk). There are no warnings, no undefined references and no overfull boxes. The PDF is 14 pages.

## Kept as is
- The preamble, macros, title, authors and date. The only additions are `\DeclareMathOperator{\spt}{spt}`.
- The setting: arbitrary Ω, and a separable, norm-closed E ⊆ ℓ∞(Ω) that contains 𝟙.
- The proofs of `lem:states`, `lem:measure`, `lem:identify`(b), `lem:hull`(a)–(c), the minimax lemma, the two minimax corollaries, contraction, trimming, `lem:change`, the repair theorem, `lem:guidedeverywhere`, and protection. These are streamlined but unchanged in substance.

## Cut
- The abstract, introduction, discussion, scope and open questions.
- The paragraph on the "five kinds of item", and all prose between results.
- `lem:test`, `lem:join`, `rem:bothneeded`, `rem:repair`.
- `prop:maximal` and `ex:intransitive`. Disjoint additivity (`prop:structure`(c)).
- The coverage definition and requirements (1)–(6). `prop:strict` as a separate result.
- `sec:domains`/`cor:domains`, `sec:vb`/`thm:vb`/`app:vb`, `app:onesided`/`prop:onesided`.
- `app:examples` (`ex:nonuniform`, `ex:PS`) and `rem:orderunit`.
- `lem:identify`(a) and (c), and old `lem:states`(e) (D_{Q1} ⊆ D_{Q2} iff Q2 ⊆ Q1), since they are unused.
- The bibliography except DiestelUhl and Sion. Sierpiński (1922) is added.

## New material
- **Definitions.** Numbered definitions for every notion:
  - gamble space and worlds (1.1); states, credal sets, P_Q, D_Q, C_Q (1.2);
  - (M1)–(M3) (1.4); atoms, the diffuse part μ_c and (M3′) (1.5);
  - models and coherent models (1.7); the support spt X (1.8); hull (1.11);
  - change, null, available, guided at ω (1.13);
  - margin triples, in sum and midpoint form, with a uniform margin as in REF73b §6 (1.14); consolidation (1.15);
  - ranking, comparison, strict comparison, tie (2.1); dominance, strict dominance, undominated/admissible (2.2).
- **One axiom list (Def 3.1), (A1)–(A5),** with glosses. The (A4) gloss says that equality of μ-masses fixes how much of each part is replaced.
- **Section 4: Theorem D′** (`thm:dominance`) under (M2) and (M3′) with (A1)–(A4). Its proof is organised as ties, then guidance and upward closure, then geometric identification. Corollary `cor:admissible` covers (A5) for a family 𝒦, and for all coherent models.
- **Section 5: the integral ranking.**
  - `prop:axioms`: under (M1), (A1)–(A4) hold. With μ{P_S=0}=0, (A5) holds for all coherent models.
  - `cor:existence`: a μ with (M1), (M2), (M3′) exists for every E, because `lem:measure`'s measure is atomless.
- **Section 6.** `cor:repair`: under the integral ranking, every incoherent model is strictly dominated by an undominated coherent model, with a uniform score margin.

## Mathematical changes relative to DPR73 / REF73 / REF73b (no gaps found)
1. **(U2) uses supports.**
   - It is stated as: "no x ∈ spt X, z ∈ spt(E∖X) with z − x ∈ D_S". This is REF73's Lemma U form, not μ⊗μ(P_X)=0.
   - All product-measure and Tonelli steps disappear, together with the measurability question for E²/E³.
   - `lem:U2` uses REF73's construction (balls about x, (z−x)/2, z), with G₁ and G₂ chosen disjoint (REF73b correction 6).
   - `lem:open`(a) becomes a two-line contradiction with (U2).
2. **Atoms are handled in full, not sketched.**
   - spt and (U2) are taken with respect to μ_c, and every G_i is chosen off the countable atom set. So μ-masses equal μ_c-masses.
   - Atoms enter only at the end of `lem:open`(e), via `lem:tools`(d): under (M2), atoms lie in D_S ∪ (−D_S).
   - REF73b's atom–atom slip does not arise.
3. **`lem:tools`(b).** It proves that a finite Borel measure on a separable metric space with no point masses has no atoms (a few lines), then applies Sierpiński.
4. **(A4) for the integral ranking.**
   - The score increase is proved with sup/inf bounds from the uniform margin: m_ω(G₃) ≥ γcm ≥ (α+β)m + cκm. No coupling π is needed.
   - Unavailability to coherent models is direct: P_Q(z) ≥ (P_Q(x)+P_Q(y))/c + κ. Neither (M2) nor the hull is used.
5. **Hypotheses of the membership proposition.** It is stated under (M1) only for (A1)–(A4), and μ{P_S=0}=0 for (A5). This is more precise than the brief's "(M1)–(M3) with atomless μ". The atomless, full-support case is recorded in `cor:existence`.
6. **`lem:states` additions.**
   - (b) now includes max_S q(h) = sup_Ω h, used for atoms.
   - (c) now lists superadditivity and monotonicity of P_Q explicitly.
7. **Other trims.**
   - `lem:hull`(d) is folded into the proof of `lem:change`.
   - The repair theorem keeps only (1) uniform improvement, (2) N ⊆ hull(X∖N), and (3) unavailability. The "location" clause is dropped.
8. **What is not included.**
   - The explicit description of the dominator ("at most two consolidations then one guided change") is not included, because the brief bans remarks.
   - The restricted-domain version (open convex cone U) is also not included.
   - Neither is needed for the theorem.

## Label map (old app_r70 -> new core)
| old | new |
|---|---|
| sec:setting | sec:setting |
| lem:states (a)(b)(c)(d)(f) | lem:states (a)(b)(c)(d)(e) |
| lem:measure | lem:measure (+ atomless) |
| lem:identify (b) | lem:identify |
| lem:hull (a)(b)(c) | lem:hull (a)(b)(c) |
| lem:hull (d) | inside proof of lem:change |
| def:change | def:change |
| lem:test, lem:join | cut |
| lem:minimax | lem:minimax (G renamed H) |
| cor:consistent | cor:consistent |
| cor:losing (a)(b) | cor:losing (a)(b); (c) cut |
| lem:contraction | lem:contraction (c renamed a, T′ renamed Ψ) |
| lem:trim | lem:trim |
| lem:change | lem:change |
| thm:repair | thm:repair (old (4) is now (3); old (3) cut) |
| def:ranking (the integral rule) | def:integral |
| (none) | def:ranking (general ranking) |
| prop:structure (a)(b) | lem:structure |
| lem:guidedeverywhere | lem:guidedeverywhere |
| prop:protect | prop:axioms, (A5) part |
| prop:strict | used inside cor:repair |
| thm:main | cor:existence, cor:repair, cor:admissible |
| prop:maximal, ex:intransitive, cor:domains, thm:vb, prop:onesided, ex:nonuniform, ex:PS, rem:* | cut |
| DPR73 Lemma 1 | lem:U1 |
| DPR73 Lemma 2 (tie lemma) | lem:tie |
| DPR73 Lemma 3 | lem:constie |
| DPR73 Lemma 4, Cor 4′ | lem:U2, cor:U |
| DPR73 Lemma 5 | lem:open |
| DPR73 Lemma 6 | lem:gap |
| Theorem D′ | thm:dominance (Theorem 4.1) |
| (G_E), (SC₃), (TT), (CAm-u), (P)/admissibility | (A1), (A2), (A3), (A4), (A5) |

## Flagged gaps
None. Every proof in core.tex is complete as written.
