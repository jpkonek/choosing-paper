# FL75 changes: final LDG full and short versions

Inputs: `ldg_full_revised.tex` and `ldg_short_revised.tex`. These were not modified.
Outputs: `ldg_full_final.tex`/`.pdf` (29 pp.) and `ldg_short_final.tex`/`.pdf` (5 pp.). Build files are in `FL75_build/`.
Compile: pdflatex, three passes each. 0 errors, no undefined references or citations, no overfull or underfull boxes, no LaTeX warnings.

## Required fixes (RL75 R1–R6): all applied

### R1. Full, Remark 4.9 (`rem:closed-comparisons`)
- The referee's replacement text is used verbatim. The family may now contain incoherent members x_s, so the argument restricts to the set of θ with c_θ coherent. That set is the full comparison set against c_1 at world 1, so it is closed, hence compact. The open E_t partition it.
- **One clause added before it**, to complete the argument. The claim that the comparison sets against x_q (world 1) and x_0 (world 2) are the complements of the E_t now also holds when the family contains some x_s. Added: "every $x_s$ is at least as good as $x_q$ at world 1 and as $x_0$ at world 2, and among the $c_t$ only $c_q$, respectively $c_0$, is not."
- Checked against the accepted comparisons of Example 4.4:
  - x_s ⪯_1 x_q and x_s ⪯_2 x_0 hold, since 2 ≤ 2 and neither is an exception.
  - c_t ⪯_1 c_1 holds for all t.
  - x_s ⪯_1 c_1 fails, since 2 > 1.
  - E_t ≠ ∅ still follows from the theorem's conclusion, because every weak dominator of c_t is c_t itself.

### R2. Full, opening of Section 4.3
The lead-in to Corollary 4.10 is replaced with the referee's text. Tie exclusion is now credited to closure under ties of 𝒜, and of L. Undominated coherence only places the dominator in C_L.

### R3. Short, Section 3.1 lead paragraph
The ambiguous transitivity sentence is replaced with the referee's three sentences, which cite Proposition 3.5.

### R4. Short, Proposition 3.3 and the paragraph after it
- (a) Added the referee's sentence to the end of the statement: "Each incoherent model is dominated under at least one ranking in $\Lf$." The proof's "which also gives the second claim" now reads "which also gives the remaining claims", because the statement has three claims. This matches the full version's proof word for word.
- (b) "for every ranking satisfying the axioms" now reads "for every family of rankings satisfying the axioms".

### R5. Short, KKM proof
The three uses of `:=` (for d_ω, s and G) are now `\coloneqq`. No `:=` remains in either file.

### R6. Full, Section 6 opening
The last sentence is replaced with the referee's text.

## Optional suggestions

Applied (each local and an improvement):
- **O1 (both versions).** Lemma 6.2 (full) and Lemma 3.2 (short) now state the equivalence with no hypothesis, and attach evaluability only to the second claim: "Under evaluability, an irrational model is dominated ...". The proofs are unchanged.
  - Full: the note after the lemma no longer says "Evaluability is used only for the second claim". It keeps the explanation of why evaluability is needed (vacuous irrationality).
  - Short: the note keeps only its first sentence.
- **O2 (full, Intro).** "Only one of these additional conclusions uses transitivity." is replaced with "Without closure under ties, transitivity gives a weaker identification (Proposition 6.6)."
- **O3 (full, abstract).** "Weak domination becomes dominance once ties are excluded" is replaced with "Every model outside the assigned family is then dominated by an assigned model once ties are excluded". This is the referee's wording with "by an assigned model" added. The rest of the sentence is unchanged.
- **O4 (full, inventory).** "to domination" is now "to dominance". "packages" is now "sets of hypotheses" in items (4) and (6).
- **O5 (full, after Theorem 4.1).** Added "and, for the loss theorems, in Corollary 3.5(b) and (c)".
- **O6 (full, Section 6.2).** "does not need them" is now "does not need these hypotheses".
- **O7 (short, after Proposition 3.6).** Added the full version's sentence: under closure under ties, the last claim is an instance of Proposition 3.3, given evaluability.

Not applied:
- **O8.** The empty abstract in the short version, and the different author lines (two authors in the full version, one in the short). The referee leaves both to the author.

## Consistency
- Lemma 6.2/3.2 and Proposition 6.3/3.3 now have the same statements in both versions.
- The short Section 3.1 and the full Section 6.2 now say the same about transitivity.
- No other shared definition or statement was changed.
