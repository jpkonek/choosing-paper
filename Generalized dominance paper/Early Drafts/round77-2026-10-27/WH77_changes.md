# WH77: handout_device.tex -> handout_updated.tex

Source of truth: short_current.tex, compiled (build_short/short_current.aux).
Numbering: Def 1.1-1.6, Lem 1.7 | Lem 2.1, Thm 2.2, Cor 2.3, Thm 2.4, Cor 2.5 | Def 3.1, Lem 3.2, Prop 3.3, Prop 3.4, Prop 3.5, Prop 3.6.

## Section 1
- Defs 1.1-1.4 box: added reading of m <=_w m', "tied at w", and "model means a member of M_L".
- Defs 1.5-1.6 box: closure under ties now defined for a set A; L closed under ties iff C_L is.
- Lemma 1.7: restated for arbitrary weak dominator a (iff-claim, (a), (b) with a in C_L, new (c) for any tie-closed A). Steps redone (4 steps); added the paper's one-world remark.

## Section 2
- Thm 2.2: c_p "not necessarily coherent or undominated"; conclusion is only weak domination (old (b),(c) and step 5 removed). Fig. 5 caption "Theorem 2.2(a)" -> "Theorem 2.2".
- Cor 2.3: same weakening; conclusion "every model is weakly dominated by some c_p"; added step 2 (conditions (i), (ii)).
- Thm 2.4: c_theta not necessarily coherent/undominated; conclusion weak domination only; step 5 updated.
- Added the paper's remark (proofs use no coherence; weak domination is not dominance).
- NEW Cor 2.5 box (a)-(c), 4-step proof, and new Fig. 8 (tie failure vs closure under ties).

## Section 3 (old 3.1-3.4 renumbered and recast)
- NEW Def 3.1 (irrational = dominated by some model under every evaluating ranking; permissible = undominated under some evaluating ranking).
- NEW Lemma 3.2 (complement) + steps + remark.
- NEW Prop 3.3 (family) + steps + the paper's paragraph citing [KCM, Theorem 4.1], same wording; KCM bibliography entry added.
- "Additional conclusions" intro paragraph added.
- Old Props 3.1/3.2 -> 3.4/3.5 (content unchanged); Fig. 9 caption and proof headings renumbered; proof of 3.5 now opens with the forward direction.
- Old Def 3.3 + Prop 3.4 -> Prop 3.6, recast ("irrational iff some member of C_L dominates under every evaluating ranking"; "closed under ties + coherent admissibility => permissible = coherent"); old "coherent admissibility alone" sentence dropped. Proof steps redone; Fig. 10 caption -> 3.6 (+ "so x is irrational"); closing remark linking to Prop 3.3 added.

## Unchanged
All other figures, Lemma 2.1 and its proof, author line, preamble style.

## Note for author
Short says Cor 2.5(a) gives the premise "when the assigned models are coherent"; (a) also needs A closed under ties (Full says so explicitly). Copied Short verbatim.

Build: pdflatex x3, no errors/warnings/overfull/undefined refs; 8 pages.
