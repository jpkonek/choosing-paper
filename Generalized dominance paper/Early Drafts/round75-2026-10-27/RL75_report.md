# RL75 referee report: LDG full and short revisions (round 75)

Files reviewed: `ldg_full_revised.tex` against `ldg_full_device.tex`; `ldg_short_revised.tex` against `ldg_short_device.tex`. Requirements: BRIEF75_LDG.md and AUDIT_1352.md §§5–6. Writer's log: WL75_changes.md. Cross-references checked against `app_revised.tex` and `app_device.tex`.

My own compile is in `RL75_build/` (pdflatex, three passes each). Full: 29 pp. Short: 5 pp. Both have 0 errors, no undefined references or citations, no overfull or underfull boxes, and no LaTeX warnings.

## Verdict

**Minor revision. The core mathematics is correct.** The irrationality definition, the complement lemma, the family-level proposition, the arbitrary-family existence theorems and the tie-exclusion corollaries are all correct. They match what the audit asked for.

One proof was not re-checked after the theorems were generalised, and it now has a gap: full version, Remark 4.9. That is the only mathematical defect.

The other required fixes concern:
- one ambiguous sentence about transitivity in the short version;
- a misleading lead-in to the tie-exclusion corollary;
- one unclear sentence;
- a small full/short mismatch;
- `:=` in the short KKM proof.

## 1. Re-derivation of new and changed results

**Lemma 6.2 (full), Lemma 3.2 (short): complementarity. Correct.**
- "Irrational" means: for every L in 𝔏 with m ∈ M_L, m ∉ U_L.
- "Permissible" means: there is some L in 𝔏 with m ∈ M_L and m ∈ U_L.
- One is the negation of the other, with no hypothesis at all. In particular it needs no evaluability, transitivity, compactness or undominated dominators.
- Evaluability is used only for "an irrational model is dominated under at least one ranking". Both texts say this.
- The statement opens with "Assume evaluability", which makes the equivalence look conditional (optional O1).

**Proposition 6.3 (full), Proposition 3.3 (short): family-level conclusion. Correct.**
- Coherent models are permissible by (ii).
- Incoherent models are irrational by (i), hence not permissible.
- So permissible = coherent, and irrational = not permissible = incoherent.
- Evaluability is used only for the full version's extra sentence "Each incoherent model is dominated under at least one ranking". The short version uses it nowhere.
- Both versions state that the proposition does not prove its dominance premise. Both give the pointer to [KCM, Thm 4.1].

**Theorems 4.1 and 4.6 and Corollary 4.2 (full), Theorems 2.2 and 2.4 and Corollary 2.3 (short): existence for an arbitrary assigned family. Correct.**
- I checked every step. The KKM step uses only closedness and the serving condition. The guarantee step uses only (i), or 1 and 2(a). The compactness step uses only that the K_ω(m) are closed in a compact Θ.
- No step uses coherence or undominatedness of c_p or c_θ. The same holds for Theorems 3.2 and 3.3 (losses), which use (i), (ii) and completeness through Lemma 2.8.
- Section 5 (Theorem 5.1, Corollary 5.2, Proposition 5.3) also never uses properties of the assigned models beyond the Bayes choice. Proposition 5.3's last claim gets membership in C_L from its own hypothesis, "every Bayes model is an undominated coherent model". Its statement is unchanged from the device version.

**Corollaries 3.5 and 4.10 (full), Corollary 2.5 (short): tie exclusion. Correct.** Exactly which hypothesis excludes ties in each part:

- **(a)** Closure under ties of the assigned family 𝒜, through Lemma 2.12(c). The proof is right: m ∉ 𝒜 together with closure gives "not tied", and Lemma 2.12's first claim then gives dominance. The loss form in Corollary 3.5(a), "same profile ⇒ assigned", is equivalent because ties under a loss mean equal profiles.
- **(b)** No tie exclusion. It gives only the dominance property and "undominated ⇒ tied with a member of C_L". That is correct.
- **(c)** Closure under ties of L, meaning of C_L, through Lemma 2.12(b). Undominatedness and coherence of 𝒜 are used only to place the weak dominator in C_L. Corollary 3.5(c) says closure under ties is equivalent to the loss-profile condition. That equivalence uses transitivity of ≤ on [0,∞]. It is correct, and the inventory item (3) records it.
- **The restored old conclusions follow.** Old Theorem 3.2's last part is now Corollary 3.5(b),(c). Old Theorem 4.1(a)–(c) is now Theorem 4.1 plus Corollary 4.10(b),(c). Old Theorem 4.6's "(b),(c)" is now Corollary 4.10(b),(c). In the short version, old Theorem 2.2(a)–(c) is now Theorem 2.2 plus Corollary 2.5(b),(c).
- **The writer's counterexample to the brief's sample condition is right.** The brief suggested "the assigned models are undominated and the model is not among them". Take one world and two mutually ⪯ models, with 𝒜 = {a}. Then a is undominated, m ∉ 𝒜, and a only weakly dominates m. The paper states this after Lemma 2.12 (and after Lemma 1.7 in the short version). Correctly, it does not use the faulty condition.

**Proposition 6.8 (full), Proposition 3.6 (short): recast permissibility proposition. Correct.**
- If m is irrational and L evaluates m, then m ∉ U_L. So (b) or (c) gives a dominator in C_L.
- The converse is immediate.
- The last claim follows from (b) and coherent admissibility.
- The full version's remark that the last claim is an instance of Proposition 6.3 under evaluability is right.

**Examples.**
- Example 4.3: assignment now explicit. Fine.
- Example 4.4: the added sentence is needed and true. No x_s satisfies x_s ⪯_ω c_t, because a loss of 2 exceeds t and 1−t. So no x_s is competitive, and every assigned model is some c_t.
- Example 4.5 already excluded incoherent Bayes models. Fine.
- Example 3.6 is unaffected.
- **Remark 4.9 was not updated and now has a gap: see R1.**

## 2. Retained conclusions and the "undominated coherent replacement" framing

- No old conclusion is kept without its hypotheses. I grepped every citation of Theorems 3.2, 3.3, 4.1 and 4.6 and Corollaries 3.5 and 4.10 in Sections 3–9. Every use of the dominance property or of exact identification now goes through Corollary 3.5(b)/(c) or Corollary 4.10(b)/(c), with the undominated coherent assignment verified. Sections 8.1–8.5 check out. Remarks 4.7, 4.8 and the "guarantees on finite sets" paragraph correctly keep undominated coherent families where the dominance property is meant.
- The one exception is Remark 4.9 (R1). It keeps a conclusion whose proof relied on c_θ ∈ C_L, which Theorem 4.6 no longer gives.
- The framing is right in both versions:
  - the abstract, Intro paragraphs 1–2 and "The dominance argument";
  - Section 6's opening, Section 6.1, and the Section 6.2 lead paragraph ("a dominance argument need not produce an undominated coherent dominator");
  - Section 9;
  - the short version's Section 3.
- Nothing suggests that every dominance argument must find an undominated coherent replacement.

## 3. Consistency and cross-references

- The two versions use the same definitions: rankings, dominance, C_L, closure under ties for sets and for rankings, evaluability, coherent admissibility, irrationality and permissibility.
- Shared results agree in substance, with three exceptions:
  - the extra last sentence of Proposition 6.3 (R4);
  - the short version's "holds for every ranking" (R4);
  - the transitivity sentence in the short Section 3.1 (R3).
- The companion-paper numbers match both `app_revised.tex` (aux file) and `app_device.tex`: Theorem 4.1, Corollary 4.10, Proposition 5.5, Theorem 6.8, Corollary 6.9.
- The axiom names match: (A1) guidance, (A2) the three-model condition, (A3) transitivity through ties, (A4) consolidation, (A5) admissibility of 𝒦.
- (M1) is finite first moment and (M2) is null indifference boundaries. (M3′) is full support of the diffuse part. Theorem 4.1 assumes (M2) and (M3′) only. That matches both LDG versions, and neither LDG version claims the result "for every finite Borel measure".
- The repair theorem assumes (M1) and (M2), in a separable gamble space containing the constants. That matches the full version's Intro and Section 7.
- "Ordinary dominance, not undominated coherent dominators" is stated in both versions.
- The bibliographic title and authors of [KCM] match.

## 4. Style

- No named lemmas, theorems, propositions, corollaries or remarks. Definitions in the full version carry names, which is allowed.
- No banned jargon and no version-comparison commentary. A grep for "no longer", "previous", "old", "now", "certificate", "record", "safe", "route" and "dangerous" finds only mathematical uses.
- The full version uses `\coloneqq` throughout. **The short version does not** (R5).

## Required fixes

**R1. Full, Remark 4.9 (`rem:closed-comparisons`, line 419): the proof has a gap.**
- Theorem 4.6 now allows incoherent c_θ, so the family may contain some x_s. In that case the sets E_t ≔ {θ : c_θ = c_t} need not cover Θ, and "infinitely many disjoint nonempty open sets covering a compact space" does not follow.
- The claim is still true. The set of θ with c_θ coherent is a full comparison set, hence closed and compact. (I checked that x_s ⪯_1 x_q and x_s ⪯_2 x_0 are accepted, since 2 ≤ 2 and they are not exceptions. So the complements of E_q and E_0 are still exactly the stated full comparison sets.)
- Replace:
  > If they were closed, the $E_t$ would be infinitely many disjoint nonempty open sets covering a compact space, which is impossible.

  with:
  > If they were closed, every $E_t$ would be open. The full comparison set against $c_1$ at world~$1$ is $\bigcup_tE_t$, since $c_t\preceq_1c_1$ for every $t$ and no $x_s$ is at least as good as $c_1$ at world~$1$; so $\bigcup_tE_t$ is closed in $\Theta$, hence compact. The $E_t$ would then be infinitely many disjoint nonempty open sets covering a compact space, which is impossible.

**R2. Full, opening of Section 4.3 (line 423): the lead-in credits tie exclusion to the wrong hypothesis.**
- The current text says the second condition "adds that they are undominated coherent models". That attributes tie exclusion to undominated coherence. The closing paragraph says the opposite, correctly. This is the exact point the brief asked to make explicit.
- Replace:
  > The next corollary states two conditions under which ties are excluded. The first needs nothing of the assigned models; the second adds that they are undominated coherent models and gives the dominance property and its consequences.

  with:
  > The next corollary states two conditions under which ties are excluded: closure under ties of the assigned family, which needs nothing else of the assigned models; and closure under ties of $L$, used together with the hypothesis that the assigned models are undominated coherent models, which places the dominator in $\C_L$. Part (b) states what that hypothesis gives without any condition on ties.

**R3. Short, Section 3.1 lead paragraph (line 183): the transitivity sentence is ambiguous, and on one reading wrong.**
- "Under closure under ties or transitivity, they give dominators in $\C_L$" can be read as saying that transitivity yields the dominance premise. It does not: under transitivity, an incoherent model tied with a member of C_L is undominated (Proposition 3.5). The full version says this correctly.
- Replace:
  > Under closure under ties or transitivity, they give dominators in $\C_L$.

  with:
  > Under closure under ties they give that premise, with dominators in $\C_L$. Transitivity alone does not: an incoherent model tied at every world with a member of $\C_L$ is then undominated (Proposition~\ref{prop:profiles}). Under transitivity, the models that are dominated have dominators in $\C_L$.

**R4. Make Proposition 6.3 (full) and Proposition 3.3 (short) state the same thing.**
- (a) **Short, line 173 onwards.** At the end of the statement of Proposition 3.3, after "the irrational models are exactly the incoherent ones.", add:
  > Each incoherent model is dominated under at least one ranking in $\Lf$.

  The existing proof already covers this through Lemma 3.2.
- (b) **Short, line 180.** Replace:
  > the premise holds for every ranking satisfying the axioms

  with:
  > the premise holds for every family of rankings satisfying the axioms

  This matches the full version and the family-level quantifier.

**R5. Short, KKM proof (line 96): `:=` is used three times, for d_ω, s and G.** Replace each with `\coloneqq`.

**R6. Full, Section 6 opening, last sentence (line 487): unclear.**
- It is not stated which two premises "either dominance premise" means.
- Replace:
  > Nothing here is a reason to assume either dominance premise.

  with:
  > Neither ordinary dominance of incoherent models nor the dominance property is assumed; each must be established for the rankings at hand.

## Optional suggestions

- **O1.** Lemma 6.2 / 3.2: state the equivalence without hypotheses, and attach evaluability only to the second claim. For example: "A model is irrational if and only if it is not rationally permissible. Under evaluability, an irrational model is dominated under at least one ranking in $\Lf$." The note after the lemma would then need only its first sentence.
- **O2.** Full Intro, "The dominance argument" paragraph (line 51). "Only one of these additional conclusions uses transitivity" is hard to parse, because with closure under ties neither uses it. Suggested replacement: "Without closure under ties, transitivity gives a weaker identification (Proposition~\ref{prop:profiles})."
- **O3.** Abstract (line 38). "Weak domination becomes dominance once ties are excluded" should say what becomes dominated. Suggested: "Every model outside the assigned family is then dominated once ties are excluded, for instance when ...".
- **O4.** Full, inventory item (2) (line 158): "upgrade weak domination to domination" should read "to dominance". The same list calls the hypotheses "packages", which is mildly jargon-like; "sets of hypotheses" would do.
- **O5.** Full, paragraph after Theorem 4.1 (line 337): "enter only in Corollary 4.10(b) and (c)" should also mention Corollary 3.5(b),(c) for the loss theorems.
- **O6.** Full, Section 6.2 (line 521): in "Proposition~\ref{prop:family} does not need them", the referent of "them" is unclear. Suggested: "does not need these hypotheses".
- **O7.** Short, after Proposition 3.6: one sentence, as in the full version, saying its last claim is an instance of Proposition 3.3 given evaluability.
- **O8.** Short: the abstract environment is empty, so the PDF prints an "Abstract" heading with nothing under it. This was already so in the device version. The author lines also differ between versions: the full version has two authors, the short one. That too predates this round. The author should decide on both.
