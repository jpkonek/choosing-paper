# Brief 68: write the two definitive manuscripts, then verify the manuscripts themselves (26 Oct 2026)

Write only in this folder (`r68/`).

## Binding inputs
- `AUDIT_r68_message.md` contains the author's decisions via the auditor. It is binding.
- The author's addition, below, is also binding.
- Outlines:
  - `OUT67_application_outline.md` (application), refereed in `REF67_out_notes.md`, together with `RF67a_notes.md` and `RF67b_notes.md`;
  - `LDGO67_outline.md` (LDG), refereed in `REF67_ldgo_notes.md`, together with `CC67_notes.md` and `REF67_cc_notes.md`.
- Sources:
  - `Universal coverage of coherent sets of desirable gambles (draft).tex`;
  - `LDG_v3.3.tex`;
  - `Covering coherent sets of desirable gambles (draft).tex`, for veto–Brier, its admissibility argument and the separation lemma;
  - `VB_dominance_note.md`, `P61_notes.md` and `REF61_pos_notes.md`.

## The author's addition: make the ranking explicit in the application paper
1. **State the rule plainly.** Accept a change if it only corrects errors. Otherwise, accept it only when it strictly improves integrated payoff and no coherent model could make that change. Explain "could make" using the gambles added and removed.
2. **Distinguish the definition from its consequences.**
   - Prove guidance, independence, finite-chain consistency, disjoint additivity, and the absence of ties between distinct models.
   - State that the ranking is generally incomplete and not transitive.
   - Say that these properties alone do not characterise it.
3. **Include a short exact characterisation.** For the fixed score, the ranking is the largest relation satisfying:
   - every guidance comparison is accepted;
   - every accepted comparison between distinct models strictly improves the score;
   - a change available to a coherent model is accepted only when guidance permits it.

   Check this characterisation and give its elementary proof. It should be a short explanatory proposition, not another elaborate axiomatic framework.

   (The lead's check: let R′ satisfy the three conditions, and take an accepted comparison between distinct models at ω. Then its score strictly improves. If the change is available to a coherent model, it must be guidance at ω. Otherwise it is unavailable and strictly improving. Either way it is in R. Conversely, R satisfies all three conditions, because a non-null guidance change strictly improves its own world's score. Equal models are compared by the null change, which is guidance. Verify this.)
4. **Keep the repair theorem central.** Its substantive achievement is to show that this restricted ranking still gives every incoherent model a coherent dominator. The maximality characterisation does not replace that theorem.
5. **Record the stronger assumption, but do not investigate it this round.**
   - The third condition restricts individual comparisons at individual worlds.
   - Coherent admissibility only requires that coherent models remain undominated.
   - The former is stronger, and its independent justification remains open.
   - We will return later to whether it can be weakened while preserving coverage.

## Other binding points (AUDIT_r68_message)
- **Application paper structure.**
  - Lead with the repair theorem and its interpretation before the full technical setting.
  - The ranking is a consequence of the repair theorem.
  - Explain the minimax mechanism clearly: fractional acceptance gives a compact convex problem, and the null-boundary condition makes the optimal choice an ordinary acceptance set. This is why the method delivers an actual coherent model.
  - Keep only the auxiliary results that explain the mechanism or delimit the headline. Move the rest to appendices.
  - Keep the general restricted-domain corollary. The detailed one-sided classification is secondary and goes to an appendix or a short remark.
- **Headline statement.**
  - Use a full-support admissible measure, then say immediately that full support can be dropped if distinct credal sets need not stay distinguishable.
  - Put these points in the statements and introduction, not only in a scope section:
    - the gamble space is separable with an order unit;
    - models are identified up to null sets;
    - arbitrary sets of worlds do not mean arbitrary spaces of bounded gambles;
    - every incoherent model has *some* uniformly improving replacement, but not every dominating comparison has a uniform margin.
- **Philosophical achievement and limitation, stated together.**
  - The construction shows that the agreed ranking requirements are compatible with coherence and can represent it exactly.
  - It supplies a substantive repair theorem.
  - Its ranking uses the distinction between changes available and unavailable to coherent models. So it does not by itself derive coherence from independently justified accuracy comparisons.
  - Neither dismiss the theorem as trivial nor present it as an independent accuracy argument.
- **The veto–Brier example.**
  - Keep exactly one representative example: a contamination result. Give the rule and its significance in the main text, and put the admissibility and separation arguments needed in an appendix.
  - Do not depend on any argument removed from LDG.
  - Its point is the contrast: complete, transitive, score-based rankings can cover genuinely imprecise targets, whereas the universal construction uses a weaker ordering structure.
  - No general visibility theorem and no catalogue of extensions.
- **LDG structure.** Separate three questions:
  - What follows once coherent undominated replacements exist?
  - What conditions, checkable independently, ensure that they exist?
  - How can suitable rankings be constructed?

  The application answers the third directly. It must not be forced through LDG's Bayes-choice or compact-family conditions. Do not retell the history of (S).
- **Not this round:** the nonseparable sketch, spaces without an order unit, and further domain classifications. State them as open questions.

## Conventions for both manuscripts
- Plain English. No jargon: no "certificate", "record", "safe", "route", "repair region", "gate", or labels such as (B), (S), (I), (CC), (GI), (GP), (SI), (RS), (TG), (TS), (FCC) in statements. A few named conditions with descriptive names are acceptable.
- Self-contained. No commentary on earlier drafts or project history.
- No names on theorem-like environments, including examples and remarks. Use \coloneqq. Call the objects "models". Use the standard dominance nomenclature (weak dominance, dominance, strict dominance, uniform dominance).
- Keep illustrative figures where they still illustrate retained results.
- Author block: Jason Konek and Catrin Campbell-Moore, as in LDG v3.3 and the covering paper. The lead will flag this to the author.
- Compile cleanly with pdflatex: no undefined references, no overfull boxes over 5pt.
- Each manuscript should be much shorter than its sources. The completion criterion is clarity and correctness, not a page target, but aim for about 25 pages for each.

## Roles
- **WA68:** the definitive application paper. Write `Coherence and accuracy for sets of desirable gambles.tex` and its PDF, or propose a better title (state it in the changes file). Also produce `WA68_changes.md`, mapping each result to its source and its refereeing.
- **WL68:** the definitive LDG. Write `Loss dominance generalized (definitive).tex` and its PDF, or propose a better title. Also produce `WL68_changes.md`.
- **After both are drafted:** independent verification of the manuscripts themselves.
  - Two referees for the application paper and one for LDG.
  - A cross-paper check: no circular dependence; neither paper relies on deleted material; consistent statements and terminology.
  - Particular attention to every passage the outlines list as not re-refereed, including LDG Proposition 9.1 (constructing rankings).
