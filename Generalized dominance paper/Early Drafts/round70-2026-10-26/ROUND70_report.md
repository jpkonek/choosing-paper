# Round 70: axiom audit of both papers (26 October 2026)

Two independent auditors, AX70L for LDG and AX70A for the application paper, each inventoried their paper's axioms against the theorem statements and proofs. Each inventory has four parts:
- items grouped by kind (LDG A–D, application A–E);
- for each item: its exact statement, a plain-English explanation, its scope, whether it is assumed, constructed or proved, and which theorems use it;
- a dependency table checked against the proofs;
- answers to four decisive checks, with ranked revisions.

The writers revised both papers. Each auditor then verified the revision against its own inventory. The lead applied the final fixes (LDG F1–F3; application F1–F4).

## The four decisive checks, both papers: all pass after revision
1. **Does any proof assume a dominance claim it is meant to establish?** No.
   - **LDG:** Theorems 3.2, 3.3, 4.1 and 4.6 obtain weak domination by an assigned model without using that the assigned models are coherent or undominated. Those two properties are used only to reach the dominance property. The paper now says so.
   - **Application:** the coverage requirements must be proved for a ranking; none is assumed. The only results that take coverage as a hypothesis are the necessity claims, and they use only D_K ⊆ U and local freedom.
2. **Does any construction-specific restriction pass as a general axiom?** Not in any formal result. Three prose passages that did so have been fixed. In the application, "no ties", disjoint additivity and the maximality conditions are now marked as properties of the construction only. The veto–Brier example has ties.
3. **Does any sufficient condition pass as a necessary one?** Not in any formal result. LDG prose that read as necessity ("must be linked through one compact family") is fixed.
4. **Are "under some ranking" and "under every ranking" kept distinct?** Yes, after fixes. Coherent admissibility (under some ranking, across a family) is kept apart from three other things: protection of every coherent model, which the construction proves; undominatedness of the target, which coverage requires; and single-loss uses.

## Main corrections
**LDG**
- Evaluability and coherent admissibility are now stated in §2.1, before any theorem.
- New §2.2, "What is assumed and what is proved".
- Props 6.3 and 6.5(c) need only transitivity.
- Prop 7.1 states its two guidance conditions as hypotheses.
- Prop 8.1's uniform-dominance clause needs unique Bayes models.
- Each permissibility conclusion names exactly the conditions it uses. Evaluability is used in no proof.
- The three-model no-reversal condition and finite-chain consistency are neither assumed nor used.

**Application**
- Reflexivity is dropped from the definition of a ranking on a domain. Nothing used it, and dropping it strengthens the necessity results.
- Requirements (2)–(5) are now "the dominance requirements". "Dominance property" keeps LDG's meaning, which the application paper gives as Thm 6.8(c).
- "Acyclicity" is renamed "finite-chain consistency".
- Requirement (4) is split into (4a) D_K ⊆ U and (4b) D_K undominated.
- Lemma 6.5 and Props 6.6–6.7 now assume only μ{P_S = 0} = 0. That is the only part of (M2) shown essential, and only for protection.
- The scope of (M3) is corrected: the veto–Brier claim and Prop C.1(a) use it too.
- A new A–E inventory opens §6.

## Corrections to the lead's preliminary list
- Prop 7.1(c) does assume both guidance conditions.
- The dominance property is a hypothesis of Props 6.1(a), 6.3 and 6.5 and of Remark 4.7, although never a standing assumption.
- Only the S-instance of (M2) is shown to be essential.
- Lyapunov's theorem is also used in Example B.1.
- Local freedom concerns the target as well as the domain.

## Page counts
LDG 25 pages; application 28 pages. Both compile cleanly.
