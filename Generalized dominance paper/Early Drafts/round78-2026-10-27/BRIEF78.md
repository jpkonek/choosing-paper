# Round 78 brief: rewrite "The dominance argument" (writer WD78)

Write ONLY in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r77/.

Inputs (same folder):
- short_current.tex: the Short LDG paper; §3 "The dominance argument".
- handout_updated.tex: the handout; §3 follows the Short paper's numbering.
- full_current.tex: the full LDG paper; §6 "The dominance argument", subsections 6.1–6.4.
- LDGv2_sec4.md: the model to follow.

Outputs:
- short_v78.tex, handout_v78.tex and full_v78.tex, with their PDFs.
- WD78_changes.md.

## The author's complaint (binding)

The current section reads as if the irrationality of incoherent models were *assumed*. Proposition prop:family takes "every incoherent model is dominated under every ranking that evaluates it" as a premise. That is wrong as a presentation.

Coherent admissibility, together with our other assumptions on the rankings, is used to **prove** that incoherent models are irrational. The section must also **state every assumption we make about our rankings in this argument**.

The author wants an argument as clean as §4 of the old LDG v2 (see LDGv2_sec4.md). That section has three ingredients: a dominance principle (a definition of irrationality and permissibility); one explicit list of the assumptions on the family of rankings; and a premise–conclusion argument, (P1) the family satisfies the assumptions, (P2) the dominance principle, (P3) the theorem, (C) the conclusion. It should also reflect everything that has changed since v2.

## Content for the new section (all three documents, kept consistent)

### 1. Dominance principle (named definition, as now)
- A model is *irrational* if, under every ranking in 𝔏 that evaluates it, some model dominates it.
- A model is *rationally permissible* if it is undominated under some ranking in 𝔏 that evaluates it.
- Keep the complement lemma.

### 2. Assumptions on the family 𝔏
State these in one named, numbered definition or list, each with a one-line plain-English gloss:
- **(E) Evaluability.** Every model is evaluated by some ranking in 𝔏.
- **(A) Coherent admissibility.** Every coherent model is undominated under some ranking in 𝔏 that evaluates it.
- **(S) Selection.** For each L ∈ 𝔏 there is a set 𝒜_L of *coherent* models, the assigned models, that satisfies the hypotheses of Theorem thm:finite (finitely many worlds), of Corollary cor:closed-choice, or of Theorem thm:local (any set of worlds).
- **(T) Closure under ties.** For each L ∈ 𝔏, 𝒜_L is closed under ties: a model tied at every world with a member of 𝒜_L belongs to 𝒜_L.

Use whichever exact formulation matches the papers' existing definitions (tie-closure is defined for any set of models in the Short paper). Say explicitly what is **not** assumed:
- transitivity or completeness of the rankings;
- that the assigned models are undominated;
- that incoherent models are dominated, which is what is proved.

### 3. Theorem (the dominance argument)
Under (E), (A), (S) and (T): the rationally permissible models are exactly the coherent ones, and the irrational models are exactly the incoherent ones.

Proof in short steps:
1. Fix L and an incoherent model m that L evaluates. By thm:finite, cor:closed-choice or thm:local, some a ∈ 𝒜_L weakly dominates m.
2. m ∉ 𝒜_L, because 𝒜_L consists of coherent models. By (T), m is not tied with a at every world, so a dominates m (Lemma lem:ties(c), or Corollary cor:coherent-assigned(a)).
3. So every incoherent model is dominated under every ranking that evaluates it; that is, it is irrational. By (E) and the complement lemma, it is not rationally permissible.
4. By (A), every coherent model is rationally permissible.

Then the premise–conclusion summary in the v2 style, (P1)–(P3) and (C), adapted.

### 4. One short sentence on the alternative route for sets of desirable gambles
For each L, the companion paper's axioms (A1)–(A4) can replace (S) and (T): by its Theorem 4.1, given its measure conditions (M2) and (M3′), every ranking satisfying them dominates every incoherent model. Keep the citation wording exactly as now.

### 5. The old Proposition prop:family
Delete it, or demote it so it is never presented as the argument; if kept, it must not read as an assumption. Put whatever remains of the purely logical step inside the theorem's proof.

### 6. Additional conclusions
Keep the existing additional results (prop:conclusion, prop:profiles, prop:permissible), with their hypotheses, in a short later subsection clearly labelled as further conclusions under extra hypotheses. In the full paper, keep its subsections 6.2–6.4 content but make §6.1 the clean argument.

Check the intro, abstract or inventory sentences of the full paper that describe §6, and update them if they describe the old proposition.

### 7. Handout
§3 must mirror the Short paper's new §3 exactly, in numbering and statements:
- statement boxes;
- step proofs with \stp;
- a figure for the theorem: reuse or adapt the existing permissibility figure, with an accurate caption;
- remove the boxes for deleted results;
- every number must match the compiled Short paper (use its .aux).

## Style
- Plain English; named definitions only; \coloneqq.
- No jargon ("certificate", "record", "safe", "route").
- No version-comparison commentary. Do not mention v2 in the papers.

Compile all three with pdflatex until references settle, with no errors, undefined references or overfull boxes.

Final message: summary under 250 words, with page counts.

## UPDATE (binding; supersedes the items above where they conflict)

1. **Handout input.** The author has edited the handout since round 77. Start from handout_user1529.tex, NOT handout_updated.tex. The author's edits include:
   - a new title;
   - removed figures;
   - \begin{comment} blocks;
   - lines commented out with %;
   - rewordings, and Lemma 1.7(c) commented out.

   Preserve all of them. Change only what the new §3 needs, plus any numbering that consequently changes. Do not un-comment anything the author commented out.
2. **Tie assumption: the author's choice.** Use the v2 form, not the 𝒜_L form.
   - **(S) Selection.** For each L ∈ 𝔏, there are assigned models that are undominated coherent models (members of C_L) and satisfy the hypotheses of Theorem thm:finite, Corollary cor:closed-choice or Theorem thm:local.
   - **(T) Closure under ties.** Each L ∈ 𝔏 is closed under ties, meaning C_L is closed under ties.
   - Proof step 2 then uses Lemma 1.7(b) (lem:ties(b)): a ∈ C_L weakly dominates an incoherent m ∉ C_L, so a dominates m.
   - Also record the by-product U_L = C_L (Corollary cor:coherent-assigned(c)).
   - Do not rely on Lemma 1.7(c) or Corollary 2.5(a) in the argument.
3. **Scope.** Make the change in all three documents (handout, Short, full), with numbering kept in sync.
4. **v2 model text.** It is in LDGv2_sec4.md, which the lead will fill in shortly. If the file is empty, use the description in this brief.
