# WD78: the dominance argument rewritten (Short §3, handout §3, Full §6.1)

Outputs: short_v78.tex/.pdf (6 pp), handout_v78.tex/.pdf (7 pp), full_v78.tex/.pdf (30 pp).
Build: build78/, pdflatex x3 each; no errors, warnings, undefined references, overfull or underfull boxes.

## Numbering (Short, from build78/short_v78.aux; handout matches)
§1–2 unchanged: Def 1.1–1.6, Lem 1.7 | Lem 2.1, Thm 2.2, Cor 2.3, Thm 2.4, Cor 2.5.
§3: Def 3.1 (Dominance principle), Lem 3.2 (complement), Def 3.3 (Assumptions on the rankings),
Thm 3.4 (The dominance argument), §3.1 Further conclusions under extra hypotheses: Prop 3.5, 3.6, 3.7.
Full §6: Def 6.1, Lem 6.2, Def 6.3, Thm 6.4; 6.2–6.4 keep Props 6.5, 6.7, 6.9 and Examples 6.6, 6.8.

## Content (all three)
- Def 3.1 named "Dominance principle"; complement lemma kept.
- Def 3.3: (E), (A), (S) [assigned models in C_L, hypotheses of Thm 2.2 / Cor 2.3 / Thm 2.4], (T) [C_L closed under ties], one-line gloss each (UPDATE form).
- What is not assumed: no property of the relations; no assumption that any incoherent model is dominated (proved); no ranking must leave every coherent model undominated. (The brief's "assigned models need not be undominated" is dropped: the UPDATE's (S) makes them members of C_L.)
- (T) cannot be dropped: one-world example (coherent a, incoherent m, all comparisons hold). Full also: (S) cannot be dropped (Example 3.6).
- Thm 3.4: permissible = coherent, irrational = incoherent; each incoherent model dominated by a member of C_L under every evaluating ranking; U_L = C_L (Cor 2.5(c)); with (E), dominated under at least one ranking. Six-step proof using Lem 1.7(b); no use of Lem 1.7(c) or Cor 2.5(a).
- Note after proof: (E) used only for non-vacuity; (S) used only via "every model weakly dominated by a member of C_L".
- (P1)–(P3), (C) summary.
- KCM sentence: (A1)–(A4) can replace (S) and (T) [KCM, Thm 4.1], citation wording kept.
- Old Prop 3.3 / 6.3 (prop:family) deleted from Short and Full.
- Further conclusions: intro rewritten (no reference to the deleted premise); closing remark after Prop 3.7 / 6.9 now relates it to Thm 3.4 / 6.4.

## Full paper, other passages updated
Abstract (first sentences); intro ¶2 sentence on the premise; intro ¶ "The dominance argument"; Def 2.9 sentence; Def 2.11 (pointer to Def 6.3); inventory items (2), (4), (6); §7 sentence listing applicable §6 results; Scope ("One ranking at a time", "What depends only on the ranking"). §6.2 retitled "Further conclusions: what the dominance property adds". Added: (S) holds for loss rankings under Thm 3.2/3.3 with undominated coherent assigned models.

## Handout (from handout_user1529.tex; §1–2 byte-identical)
- Def 3.1 box retitled; new boxes Def 3.3 and Thm 3.4 (+ "Not assumed" line); \stp proof; summary.
- Permissibility figure moved from Prop 3.6 to Thm 3.4, with step markers and a new caption.
- Props renumbered 3.4/3.5/3.6 -> 3.5/3.6/3.7 in boxes, captions, proof headings and cross-references.
- Old Prop 3.3 box and steps wrapped in \begin{comment} (author's in-box % edit kept verbatim).

## Conflicts between the author's handout edits and the brief
1. The author commented out the KCM paragraph; the brief puts the KCM sentence in all three documents. The author's comment is left alone, and the new sentence is added only as a % line, so it does not appear in the PDF.
2. The author edited the Prop 3.3 box (last sentence commented out); the brief deletes Prop 3.3. The box is hidden inside a comment block, not erased.
3. The author commented out Lemma 1.7(c) and the proofs of Lemma 1.7 and Cor 2.5; consistent with UPDATE item 2 (not relied on). Cor 2.5(c), used in step 6, is still in its box.
4. The author removed the definition "tied at every world" from Def 1.1–1.4 and the remark "None of these proofs uses coherence...". Theorem 3.4 uses both notions; left as the author has them.
