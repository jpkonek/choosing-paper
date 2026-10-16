# Interpretation fix: domains as classes of evaluable models (14 Oct 2026)

Backup of the previous version: `The Contamination Triangle (pre-interpretation-fix).tex`.
Line numbers below refer to the new `The Contamination Triangle.tex`. It compiles cleanly with `latexmk -pdf`: no errors, no undefined references, no overfull boxes. No mathematical statement, hypothesis or proof step was changed. The only labels that changed are `def:menu` → `def:domain` and the new `rem:advicerange`.

## What changed

1. **§2.1 (l. 122–136).** A new paragraph, "What a gamble represents", states the author's representation. A gamble f represents {f,0}, which is equivalent to {g,h} for any g, h with f = g−h. The gambles f and −f represent the same choice with the options' roles swapped. The four kinds of advice are listed, each with what it advises in {g,h}. The representative-in-H convention is kept, explicitly as bookkeeping only. The background order now reads "no advice" for "silence".
2. **§2.2 (l. 144–170).**
   - New opening paragraph: restricting a domain only restricts which models are evaluated. Problems are never altered or removed, and never given restricted options. The world orders concern every binary problem.
   - Definition `def:domain` replaces `def:menu`. A *decomposable domain* is a nonempty class of evaluable models, closed under splicing (on symmetric measurable sets) and under convergence in measure.
   - Remark `rem:advicerange` (l. 151) characterises these classes by an *advice range* A(f). Its status line reads "standard; checked, not written out": it is Hiai–Umegaki 1977, Thm 3.1, applied to the advice as a {0,1}²-valued function. A bibliography entry `HU1977` was added.
   - A paragraph "Earlier terminology" (l. 160) records that "menus", "menu domains", "available actions", "accept-or-silence domain" and "forced silent" are superseded and must be read as restrictions on the class of evaluable models.
   - A sentence after the axioms (l. 170) notes that (G) is unchanged, because it compares the advice two evaluable models give.
   - (LF) is glossed in advice-range terms (l. 178).
3. **§2.4 (l. 203–205).** Penalties are defined only on the advice range: only the advice that evaluable models actually give enters. On a problem where all evaluable models give the same advice, the penalty is the same for every evaluable model and drops out of every comparison, although it is still part of the ranking. "Menu" is replaced by "advice range" and "best actions" by "best advice".
4. **§2.5 (l. 207–220).** "The accept-or-silence domain" becomes "the U-domain M_U", defined as the class of measurable subsets of U. Its consequences are spelled out exactly as in the author's text:
   - U never contains both f and −f;
   - so no evaluated model gives contradictory advice;
   - for f ∈ U, an evaluated model D advises "choose g" iff f ∈ D, and otherwise gives no advice;
   - for −f ∈ U, the roles of g and h swap;
   - for f with f ∉ U and −f ∉ U, there is no advice (f ∉ U alone is not enough: if −f ∈ U, evaluated models differ on f).

   The text adds explicitly that those last problems remain problems. "Other pairs have menu {0}" was removed.
5. **"Two-sided" (l. 609).** The term is defined at its first use in the §4 preamble. It replaces "three-action menus" and "three-action menu domains" (§6.1, Q2). "Three-action pairs/gambles" becomes "pairs/gambles with advice range {+,0,−}".
6. **Whole file.**
   - "menu domain" → "decomposable domain".
   - "menu" → "advice range".
   - "available model" → "evaluable model".
   - "offers both orientations" / "acceptance is available" → "the advice range contains both acceptances" / "accepting h lies in the advice range".
   - "forced menus" → "pairs on which every evaluable model gives the same advice".
   - "menu equal to {0}" → "every evaluable model gives no advice".
   - "forced on almost every mixed pair" → "required".
   - The hypotheses of Prop. `prop:A` and of (UN) were reworded in advice terms (l. 857, 903).
   - Source descriptions now say "(called menu domains there)". File names are unchanged.
   - The table entry "two-sided chords" is now "non-precise credal sets on crossing chords", to avoid a clash with the new term.
7. **Kept deliberately.**
   - "Forced ties" / "forced-tie reading" (l. 111, 1055): this is the weakened-guidance axiom NSI_θ, not a domain restriction.
   - Logical uses of "forces" (for example "a cover forces E(ψ) ≠ ∅").
   - "silence" as a synonym for "no advice", where it names advice kind 0.
   - Internal label names such as `cor:availability` and `sec:aos`, which are not printed.

## Possible substantive dependence

None found. These places were checked because they look as if they might use more than "the class of evaluable models is restricted":

- **Error indicator and adding up on M_U (l. 239, 247; Def. `def:addup`).** Errors are counted only inside U, so giving no advice on problems with f ∉ U and −f ∉ U costs nothing. This is harmless. Every evaluable model gives no advice there, so any penalty is common to all models. It cancels in the differences ΛY − ΛX used by (CP-a), and in the endorsement inequalities ν(E(B)) ≤ ν(E(X)). Positivity of ν_i is needed only where models can differ.
- **"Regular" (l. 242).** This means correct advice on unanimous problems. U contains every nonzero nonnegative gamble, so no problem is ignored.
- **Cor. `cor:R234` and Cor. `cor:TSalways`(b) (l. 686, 725).** These rule out covers on domains whose advice range lacks an acceptance on a non-null set of mixed pairs. The proof uses only that the Bayes models are evaluable and coherent with K_q → {e_b}. Note that M_U is itself such a domain, which is consistent with Cor. `cor:coverage`.
- **Lemma `lem:raytransfer`(b), Prop. `prop:noWLOG`, Prop. `prop:normalform` and N_i, and (UN) (l. 622, 691, 814, 857).** All of these are statements about which advice evaluable models give.

## Other observations (not interpretive; not changed)

- **Prop. `prop:CF` (l. 776–781).**
  - The statement says the converse cover lives "on the all-model domain", but the proof of (⇐) takes advice ranges {+,0,−}. Contradictory advice (×) is not mentioned.
  - In (⇒), "advice ranges are {+,0,−} or {+,−}" likewise ignores ×.
  - Under strict guidance × is worst at every world and is never Bayes advice. The gap therefore looks cosmetic, but the text should say so.
