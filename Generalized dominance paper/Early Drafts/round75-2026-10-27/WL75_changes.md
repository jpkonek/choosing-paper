# WL75 changes (round 75)

Numbers refer to the compiled revised files. Both compile cleanly (no undefined references, no overfull boxes). Full: 29 pp (was 26). Short: 5 pp (was 4; page 5 holds the end of the last proof and the references).

## ldg_full_revised.tex

**Abstract.** Rewritten. Two premises of the argument (coherent admissibility; ordinary dominance of incoherent models); conclusion that the permissible models are the coherent ones; ordinary dominance needs no coherent or undominated dominator; main results stated for an arbitrary assigned family (weak domination); tie-exclusion; the dominance property only when the assigned models are undominated and coherent. Removed the "two halves ... dominated by a coherent model that is itself undominated" framing.

**Introduction.**
- Para 1: the argument needs only that incoherent models be dominated; coherent undominated dominators are an additional conclusion.
- Para 2: the premise is ordinary dominance (Sec. 6); main results give weak domination by an assigned family, dominance once ties are excluded, and the dominance property when the assigned models are undominated coherent.
- "Conditions that yield weak domination" (renamed): assigned models "coherent or not"; dominance property via Cor. 3.5.
- "General theorems" para: selection argument assigns "a model"; compactness of "the assigned family"; new sentences on weak domination vs dominance, pointer to Cor. 4.10.
- "The dominance argument" para (replaces "What the dominance property gives"): new definitions of irrationality and permissibility, Prop. 6.3, statement that it does not prove its premise, pointer to [KCM, Thm 4.1] with (A1)–(A4), (M2), (M3′); additional conclusions of the dominance property (Props 6.4, 6.8).
- "Constructing rankings" para: companion conditions named exactly ((M1), (M2), separable gamble space containing the constants); repair theorem cited as [KCM, Thm 6.8 and Cor. 6.9], for its integral ranking.

**Section 2.**
- Def. 2.9 and the paragraph after it: dominance property no longer "the target"; it asks for more (undominated coherent dominators) and less (only weak domination); with closure under ties it yields dominance (Prop. 6.4).
- Def. 2.10: closure under ties defined for an arbitrary set of models; a ranking is closed under ties if C_L is (old meaning unchanged).
- Def. 2.11: coherent admissibility phrased "under some ranking that evaluates it"; "no proof uses evaluability" replaced by: evaluability is used only to make irrationality non-vacuous (Lemma 6.2).
- Lemma 2.12: now for an arbitrary weak dominator a. Adds: a dominates m iff m does not weakly dominate a; (a) unchanged in content (never used a ∈ C_L); (b) as before; new (c) for any set closed under ties. Paragraph after it: one-world two-model example showing undominatedness of a does not exclude ties; every set is closed under ties when distinct models are never tied (Prop. 7.3(a)).
- Sec. 2.2 inventory: items (2), (3), (4), (6) updated (packages give weak domination for arbitrary assigned families; corollaries add tie-exclusion and the dominance property; Prop. 6.3 and recast Prop. 6.8 listed; transitivity of losses now used in Cor. 3.5).

**Section 3.**
- Opening paragraph: results give weak domination by an assigned family; corollaries add tie-exclusion and the dominance property.
- Thm 3.2: assigned c_p need not be coherent or undominated; conclusion is weak domination only. Old closure-under-ties conclusion moved to Cor. 3.5. Sentence after proof: proof uses (i), (ii), completeness, never coherence/undominatedness.
- Thm 3.3: same change; old "last conclusion" clause removed.
- New Cor. 3.5: (a) if every model with the profile of an assigned model is assigned, every non-assigned model is dominated; (b) undominated coherent assigned models give the dominance property; (c) plus closure under ties (loss-profile form) gives the old exact identification and dominance of incoherent models. Short paragraph before it states that weak domination may be a tie.

**Section 4.**
- Thm 4.1: assigned c_p arbitrary; conclusion reduced to the old part (a) (weak domination). Old (b), (c) moved to Cor. 4.10. Following paragraph rewritten: proof uses no property of the assigned models.
- "Weakening of the selection argument" para: "assigns ... a model".
- Cor. 4.2: assigned models arbitrary; conclusion weak domination; proof adds "Theorem 4.1 applies".
- Ex. 4.3: assignment of a stated explicitly.
- Ex. 4.4: added that no x_s is competitive anywhere, so any assignment satisfying Cor. 4.2 takes values among the c_t (needed now that Cor. 4.2 allows incoherent assigned models).
- Thm 4.6: item 1 retitled; c_θ arbitrary; conclusion weak domination only; sentence after proof.
- Rem. 4.7(ii), Rem. 4.8, "guarantees on finite sets" paragraph: wording adjusted to the arbitrary-family theorems (undominated coherent families named where the dominance property is meant).
- New Sec. 4.3 "From weak domination to dominance" with Cor. 4.10: (a) assigned family closed under ties gives dominance of every non-assigned model (in particular when distinct models are never tied); (b) undominated coherent assigned models give the dominance property and old Thm 4.1(b); (c) plus closure under ties gives old Thm 4.1(c) and dominance of incoherent models. Closing paragraph: undominatedness does not exclude ties; in (c) closure under ties does.
- The sentence "The results of the next section need more..." moved to the start of Sec. 5.

**Section 5.** Opening: hypotheses are those of Thm 3.3; assigned models need not be coherent or undominated. Prop. 5.3 proof: last claim now explains why the uniformly dominating assigned model is undominated coherent (it is a Bayes model).

**Section 6 (retitled "The dominance argument"; restructured).**
- Opening paragraph: ordinary dominance; the dominator need be neither coherent nor undominated.
- 6.1 Rational permissibility now first. Def. 6.1: irrational = under every ranking that evaluates it, some model dominates it; permissible = undominated under some ranking that evaluates it.
- New Lemma 6.2 (complementarity; one-line proof) with note that the equivalence needs no hypothesis and evaluability is used only for non-vacuity.
- New Prop. 6.3 (family-level conclusion). Paragraph: (ii) is coherent admissibility; it does not prove premise (i); pointer to [KCM, Thm 4.1] ((A1)–(A4), (M2), (M3′), ordinary dominance only); Cors 3.5(c), 4.10(c), parts (a) with coherent assigned models closed under ties, and Prop. 7.3(c) as other sufficient conditions.
- 6.2 "What the dominance property adds": new paragraph (dominance property alone does not give premise (i); closure under ties does; transitivity alone does not). Prop. 6.4, Ex. 6.5 unchanged.
- 6.3 Ties and transitivity: unchanged.
- 6.4 "Undominated coherent dominators across a family": old Prop. permissible kept as Prop. 6.8, parts (a)–(c) unchanged; family claim restated for the new irrationality (irrational iff dominated under every evaluating ranking by an undominated coherent model of it); last claim proved directly; note that it is also an instance of Prop. 6.3.

**Section 7.** "recorded" -> "stated"; Prop. 6.3 added to the list of applicable results; "route" removed. Companion paragraph rewritten: (M1), (M2) for the repair theorem [KCM Thm 6.8, Cor. 6.9]; integral ranking identified with Def. 7.1; Theorem 4.1 of [KCM] stated with (M2) null indifference boundaries, (M3′) full support of the diffuse part, axioms (A1)–(A4), ordinary dominance only, (A5) and [KCM Cor. 4.10]; integral ranking satisfies (A1)–(A4) under (M1) and leaves coherent models undominated under (M2) [KCM Prop. 5.5].

**Section 8.** Opening paragraph: the first step (C_L = C) is needed only for Cor. 3.5. Prop. 8.2 proof, Predd and SSK paragraph, Thm 8.4 proof, Prop. 8.9 proof, Prop. 8.11 proof: cite Cor. 3.5 where the old theorem conclusions were used. Sec. 8.5 last sentence: sufficient hypotheses are those of Cors 3.5(c), 4.10(c).

**Section 9.** "One ranking at a time" and "Sufficient conditions" updated (ordinary dominance suffices for Prop. 6.3; undominatedness enters only through the corollaries); "What depends only on the ranking" adds Lemma 6.2, Prop. 6.3, Cor. 4.10.

## ldg_short_revised.tex

- Def. 1.5: closure under ties for an arbitrary set; ranking closed under ties if C_L is.
- Lemma 1.7: arbitrary weak dominator a; iff-clause; (a), (b) as before; new (c). One-sentence example after it (undominatedness does not exclude ties).
- Thm 2.2: c_p need not be coherent or undominated; conclusion = old (a) only.
- Cor. 2.3: arbitrary c_p; conclusion weak domination.
- Thm 2.4: c_θ arbitrary; conclusion weak domination only.
- New paragraph and Cor. 2.5: (a) assigned family closed under ties; (b), (c) = old Thm 2.2(b), (c) when the assigned models lie in C_L.
- Sec. 3: Def. 3.1 (new irrationality; permissibility "that evaluates it"); new Lemma 3.2 (complementarity) and Prop. 3.3 (family-level conclusion); pointer paragraph to [KCM, Thm 4.1] with (A1)–(A4), (M2), (M3′), ordinary dominance only, and to Cor. 2.5. New Subsec. 3.1 "Additional conclusions" (short paragraph that weak domination by C_L alone does not give the premise); Props 3.4, 3.5 unchanged; Prop. 3.6 (old permissible) with the family claim restated for the new irrationality and a direct proof of the last claim.
- Bibliography: [KCM] added.

## Mathematical points found

1. Lemma 6.2 / 3.2: complementarity of "irrational" and "rationally permissible" is a quantifier negation and holds without evaluability. Evaluability is stated as required, but the text says it is used only for non-vacuity (an irrational model is dominated under at least one ranking). Prop. 6.3 / 3.3 likewise uses evaluability only for that clause.
2. Item 4: no existence proof uses coherence or undominatedness (Thms 3.2, 3.3, 4.1, 4.6, Cor. 4.2; also Sec. 5). But the brief's sample tie-exclusion condition "the assigned models are undominated and the model is not among them" is not sufficient. Counterexample: one world, two models a, m, each at least as good as the other, assigned family {a}. A sufficient condition is that the assigned family be closed under ties (automatic when distinct models are never tied), or closure under ties of L with assigned models in C_L.
3. The dominance property does not by itself give premise (i) (ties), and transitivity alone does not either. Old wording implying the dominance property "assumes more" than ordinary dominance was avoided.
4. Ex. 4.4 needed an extra sentence once Cor. 4.2 allows incoherent assigned models.
