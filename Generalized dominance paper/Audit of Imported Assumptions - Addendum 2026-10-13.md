# Audit of imported assumptions: addendum, 13 October 2026

This addendum does two things. Part A assesses the auditor's feedback on negligible-stakes indifference (NSI). Part B checks whether the current state of play rests on any assumption beyond the adopted ones: (G), (IB), (E), (LA), (A), (S), (C), (LF) at the target, and decomposable domains (SC plus closedness in measure). It pays particular attention to the error LDG's conditional case warns against: satisfying, or analysing, (S) through a selection that sends each index p to a model that is Bayes for p itself.

Status labels: CHECKED means verified by me for this note, with the reason given; it is not an independent referee pass.

---

## Part A. The auditor's feedback

**A1. Forced and permitted ties are different classes. Agreed.**
- For additive losses put r_i(g) = ℓ_i(g, silence) − ℓ_i(g, good). Strict guidance requires r_i > 0, forced NSI requires r_i = 0 on the band, and permitted NSI requires r_i ≥ 0 on the band (with r_i > 0 off it).
- The N1–N4 obstruction uses the equality r_i = 0 on a whole open piece of the band (ray transport, N2 Lemma 1; Thm B Step 1). Permitted ties do not supply that.
- **Correction.** The Round 4 addendum said that under the permitted reading "T1 is the open strict problem again". That is wrong as stated. The permitted class contains the strict class, but nothing shows that the two have the same coverage. N2 §7 Prop L is CHECKED, not refereed, and it restricts where ties may be placed without proving equivalence. N1 §4.5 likewise leaves exceptions unspecified. The equivalence is an open question.
- **Second correction.** The Round 4 "Lesson" stated a general principle: any useful weakening must avoid a boundary between tied and strict problems inside one world near the target boundary. N4 accepted only a narrower statement: such an interface is harmful when it meets the target boundary in the configuration of N2 Thm B. The general principle is withdrawn.

**A2. Where the difficulty now sits. Agreed, with one precision.**
- In three worlds, closed choice follows once every strictly positive weighting has a unique coherent optimum (CCIBU for strict guidance; N1 Thm 3.1 and N3 Thm CC_θ for forced NSI). For permitted NSI the same should hold, but the vertex step has not been rechecked: a vertex face can be large when ties are allowed. Status: expected, unchecked.
- The requirement that every strictly positive weighting have a unique coherent optimum is not an artefact of the proofs. Part B, item B2.3, shows that it follows from (S), (C), the guidance condition and additivity. It does not depend on how (S) is satisfied.

**A3. Scope of the forced-tie result. Agreed.** It excludes additive constructions with forced ties for contamination targets, for every threshold, in both norms. It says nothing about non-additive (IB) rankings. The small-threshold theorem (N2 Thm Z) concerns full-dimensional interior credal sets.

**A4. The recommended sequence. Agreed.** First the permitted-ties problem for one fixed contamination triangle. Then, if that fails, an exact non-differentiable additive realisation (R15's corner constraints alone are consistent). Then a genuinely different ordinal mechanism.

What is already known about the permitted-ties problem narrows it as follows.
- *Plateaus remain excluded.* N3 Thm PL_θ needs strictness at only one facet point off the band, and N3 Cor ST1 excludes plateaus under any tie rule (with (NA)). So the permitted version cannot work by holding the target fixed on an open set of weightings.
- *Ties on the target's outer side near a boundary gamble are excluded* by the N2 Thm B mechanism if they fill an open piece of the band there (N2 Prop L, CHECKED only).
- *Ties on the inner side are constrained but not excluded.* By N2 Lemma 1(a), acceptance on tied problems is transported along lines through the corner δ_i. By N3 Cor ST2 (with (NA)), the weightings that keep the target's local facet near a tied crossing lie on one line through e_i and the target weight. For a non-plateau family that may be a single point, so this is a constraint, not a contradiction.
- *The strict no-gos use strictness exactly where inner-side ties are allowed.* R10a Thm V (vertex anchoring), R10a Thm R (ray lemma) and R15 Thm 6.2 (corner calculus) all use r_i > 0 at target boundary gambles with g_i = 0. Those gambles lie in the band for every θ > 0.

So the precise first question is: **can ties placed only on the target's inner side, near its coordinate crossings, remove the positive slopes that R10a Thm R and R15 Thm 6.2 need, while respecting the cevian constraint of N3 Cor ST2?** That is the permitted-ties problem in a form that is not already settled.

---

## Part B. Assumption audit

### B1. Is (S) satisfied or analysed through Bayes-for-p selections anywhere?

**No current result does this.** CHECKED, item by item.

1. **Negative results never use the selection map.** Every no-go (R1–R5, R7, R10a, R10b, R11, R15, N1–N3) uses (S) only through two general consequences that LDG proves for arbitrary preorders:
   - every model is weakly dominated by a selected model (the KKM step);
   - together with (C), every undominated model is selected, up to ties, and hence coherent (Lemma 1 of the decomposable-domain notes).
   The Bayes facts they use concern the additive ranking at strictly positive weightings, and these facts are derived (B2.3 below). The index p of (S) never appears in them. N2 states explicitly that nothing at boundary weightings is used.
2. **Positive results use deliberately reindexed selections.** CCIBU's selection at index p minimises Q_p(x) = Σ p_i (x_i − a_i)². The chosen model is Bayes for a weighting proportional to (p_i (x_i − a_i))_i, not for p. At an edge index it is a particular efficient boundary model, singled out by a secondary minimisation. This is the device of LDG lem:section: the certifying weighting differs from the index. N3 Thm CC_θ uses a blow-up at the vertices, which serves the same purpose.
3. **No result requires every Bayes model at a boundary weighting to be coherent.** LDG ex:conditional shows that this can fail, and in our setting it can fail too. CCIBU needs only that each undominated boundary profile has a unique coherent realisation (its Lemma 2), and it proves this. Vertex models under strict guidance are coherent because the vertex minimiser is unique and therefore undominated. That is derived, not assumed. Under any tie rule this vertex argument is unavailable. N1–N3 do not use it.
4. **Where the error did occur, it has been withdrawn or superseded.**
   - R1 Thm 4.1 excluded a family indexed by the weighting (K_q = (1−ε)σ(q) + εΔ). It was withdrawn as an obstruction to the target (auditor, 12 Oct).
   - The phrase "Bayes uniqueness = selection uniqueness" was withdrawn (example: C_t = B_{t²}).
   - R11 Lemma BT shows that a selection indexed by interior Bayes models fails (S) when there are boundary ties. On its own that shows nothing about (S). CCIBU later confirmed that (S) holds anyway in three worlds. Lemma BT is now only a remark about one kind of selection.
5. **Remaining risk.** For n ≥ 4 the selection problem is open beyond vertices and edges (R14). An argument there that infers a failure of (S) from the failure of a Bayes-indexed or interior-limit selection would repeat the error that LDG's conditional case exposes. Any n ≥ 4 negative claim must construct, or rule out, *every* closed competitive selection.

**A structural remark.** For an additive ranking on a decomposable domain the attainable loss set is convex (splicing and atomlessness). So any model that is competitive on supp p is Bayes for *some* weighting supported in supp p. Hence every admissible selection automatically makes Bayes choices in LDG's sense, with a certifying weighting that may differ from p and need not vary continuously. LDG ex:rescale, where no Bayes choices exist, needs a non-convex attainable set. That cannot happen for additive rankings on decomposable domains, but it can happen for rankings that are only ordinally equivalent to additive ones. That is one more reason why the additive restriction is a restriction of scope (B2.1).

### B2. Other possible imported assumptions

| | Assumption | Status | Where it does work |
|---|---|---|---|
| B2.1 | Each world's ranking is additive, or sandwiched by additive losses | **Scope restriction**, not an axiom | Every no-go |
| B2.2 | Losses finite, with integrable envelopes | **Derived** | Continuity in measure; compactness of the attainable set |
| B2.3 | Unique coherent Bayes model at every strictly positive weighting | **Derived** from (S), (C), the guidance condition, additivity and splicing | All triangle and NSI results |
| B2.4 | The target is Bayes at a full-support weighting | **Derived** from (LF) and K ⊆ int Δ (R1 Prop 2.6) | Every T1 argument |
| B2.5 | Vertex models contain their vertex (R10a Thm V) | **Derived** under strict guidance from (LF); **not available** under any tie rule | Strict no-gos |
| B2.6 | Boundary Bayes models coherent | **Never assumed** (and false in general) | — |
| B2.7 | (C) rather than LDG's (C_~) | **Required by the goal** | Forces B2.3 |
| B2.8 | Gaussian measure; models modulo null sets; "strict" means "on a non-null set" | **Formalisation choice in v3** | Makes integral losses possible at all |
| B2.9 | Contradiction ranked strictly worst | **Adopted**; I found no argument where it matters | — |
| B2.10 | (LF) at the target; decomposable domains | **Adopted by the author** | Thm V, B2.4, convexity, existence of Bayes models |
| B2.11 | n = 3; K ⊆ int Δ | **Scope** | CCIBU, CC_θ, every T1 result |

Reasons, where the status is not self-evident:

**B2.1 (additivity, completeness).** LDG allows each world's ranking to be an incomplete preorder. Sandwiched rankings include the unanimity (Pareto) orders of several additive losses, so this kind of incompleteness is covered: R3 §2.4 shows that it relaxes undominatedness only, and in three worlds R11 Thm W with R13 Prop S and CCIBU reduces sandwiched coverage of an interior target to additive coverage. Incomplete (IB) orders that are not sandwiched are not covered by any current no-go.

There is a pointer here, not a result. In the earlier work on the vacuous model with all models evaluable (*Incomplete Rankings and Coverage*, Corollaries 13, C and refined), any configuration in which the vacuous model is undominated must contain at least two incomplete worlds that are not (W)-worlds. Under fineness these violate (NC), so they lie outside the sandwiched class. The class about which the decomposable-domain no-gos are silent is the same class that the earlier work identified as the only possible home for that coverage.

**B2.2 (finite losses). CHECKED.** Suppose an additive ranking on a decomposable domain assigned infinite loss at world i to some model X.
- Let I_i be the pointwise world-i best advice in the advice ranges. It lies in the domain, and L_i(I_i) ≤ L_i(Y) for every Y.
- If L_i(I_i) = ∞, all models tie at world i. Strict (G) is then violated by any strict improvement, and one exists unless every advice range contains a single kind of advice almost everywhere.
- If L_i(I_i) < ∞, then L_i(X) = ∞ comes from the set where X differs from I_i. That set is a countable union of sets on which X's penalty is bounded, so one of them, S, is non-null and contributes a finite amount. Replace X's advice by I_i's on S. Strict guidance makes I_i's advice strictly better at world i there, so the result is a strict guidance improvement, but its loss is still ∞. That is a tie, contrary to strict (G). (If penalties may themselves be +∞ on a non-null set, split that set and improve on one half; the same tie results.)

So every model in the domain has finite loss at every world. The pointwise worst advice in the advice ranges is itself a model, so the envelope is integrable. This uses strict (G) for strict guidance. Under permitted ties the argument has to place the improvement where strictness is still required; I expect this to work, but I have not checked it.

**B2.3 (unique coherent interior Bayes models). CHECKED as a dependency chain.**
- At a strictly positive weighting every Bayes model is undominated.
- By (S) (the KKM step) and (C), it is selected and therefore coherent.
- If two kinds of advice tied for the weighted minimum on a non-null set of problems, splicing would produce many Bayes models with different profiles. They would all have to be coherent, and R1 Lemma 1.4 shows that they cannot be.
- For this the two tied kinds of advice must have different loss vectors. Under strict guidance they differ at every world with g_i ≠ 0. Under forced or permitted NSI they still differ at some world: in the sup norm some coordinate has |g_k| = ‖g‖ > θ‖g‖ whenever θ < 1. In the Euclidean norm the same holds for θ < 1/√3, because otherwise ‖g‖² ≤ 3θ²‖g‖².

So the requirement rests on (S), (C) and additivity, not on any presumption about the selection map.

**B2.7 ((C) versus (C_~)).** Without (C), a ranking satisfying (LA) and (S) can leave incoherent models undominated, namely those tied with selected ones. The target conclusion, that the union of the undominated sets is exactly the coherent class, then fails. LDG's (C_~) gives the weaker conclusion that every undominated model is equivalent to a coherent one. That would be acceptable only if the author wants the weaker conclusion. So (C) is not an imported assumption. It is the axiom that turns B2.3 into a requirement.

**B2.8 (measure).** Only the null sets of the Gaussian measure matter. Any measure with the same null sets gives the same class of additive rankings, since the density can be absorbed into the penalties. The choice that "strict improvement" means "strictly better on a non-null set" is what makes integral losses available. If strict (G) applied to changes on single problems, no integral loss would satisfy it. This is a modelling choice made in v3, not hidden in the proofs.

**B2.9 (contradiction).** At a strictly positive weighting contradiction is never pointwise optimal. I found no step in the triangle or NSI arguments that uses its position relative to bad advice. Not checked line by line.

### B3. Conclusion

The current state of play is not due to Bayes-for-p selection. The negative results rest on four things:
1. additivity, or sandwiching (a scope restriction);
2. strictness of guidance at target boundary gambles whose world-i coordinate is zero (relaxed by permitted NSI);
3. (LF) at the target (adopted);
4. decomposable domains (adopted).

Only items 1 and 2 are not adopted axioms. Item 1 is the known scope limit; item 2 is exactly what the permitted-ties problem in A4 tests.
