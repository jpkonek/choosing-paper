# RA76 referee report: app_in.tex -> app_fixed.tex (USER_1425 coherence correction)

## Verdict

**Accept with one minor required fix in app_fixed.tex (Fix 1). Fix 2, in ldg_full_final.tex, is recommended but not required.**
I re-derived every changed statement and proof and found no mathematical error. The new definition matches
USER_1425 and the Loss Relations convention: (D1)–(D4), D_Q = {P_Q>0} ∪ {g ⪈ 0}, and a model is coherent if it is equal a.e. to a coherent set of desirable gambles.
The only problem is one prose sentence that the weakened hypotheses have made inaccurate.

Compile: I compiled it myself in `r76/ra76_build/` (pdflatex ×3). Exit code 0, with no warnings, no undefined references and no overfull or underfull boxes.
Form: every `definition` has a name, there are no remark environments, there is no `:=` (`\coloneqq` throughout, with one `\eqqcolon`), and Sections 2–6 keep their numbering.
The only labels the LDG papers cite are Thm 4.1, Cor 4.10, Lemma 5.3(b), Prop 5.5, Thm 6.8 and Cor 6.9, and all of them keep their numbers.

## Re-derivations (all correct)

- **Lemma 1.5 (lem:DQ).**
  - g ⪈ 0 gives P_Q(g) ≥ 0 by monotonicity, so D_Q ⊆ C_Q and D_Q∖D_Q° ⊆ {P_Q=0}.
  - (D1)–(D3) hold.
  - (D4): if both summands are ⪈ 0, so is the sum. Otherwise one summand is in D_Q° and the other has P_Q ≥ 0, so superadditivity gives P_Q(sum) > 0.
  - Borel: {g ≥ 0} is an intersection of closed half-spaces; removing {0} leaves a Borel set.
  - Interior: take h ∈ D_Q∖D_Q°. Then P_Q(h − t𝟙) = −t < 0, and h − t𝟙 ≥ 0 would force P_Q(h − t𝟙) ≥ 0. So h is not an interior point, and int D_Q = D_Q°.
- **Lemma 1.17(a).**
  - D_S° is open and contains 𝟙, so int D is a nonempty open convex cone that misses 0, and D ⊆ cl int D.
  - Any nonzero ψ ≥ 0 on D is positive, because h + t𝟙 ∈ D_S° for h ≥ 0. So ψ(𝟙) > 0, and ψ/ψ(𝟙) ∈ K_D.
  - Geometric Hahn–Banach (open convex set against a point) works in any real normed E with 𝟙 ∈ E. It gives K_D ≠ ∅.
  - The bipolar theorem gives cl D = C_{K_D}. Then D°_{K_D} ⊆ int cl D = int D ⊆ D.
- **Lemma 1.17(b).**
  - A coherent set D meets the hypotheses of (a). By (D2), D_{K_D} = D°_{K_D} ∪ {⪈0} ⊆ D.
  - Under (M2), D∖D_{K_D} ⊆ C_{K_D}∖D°_{K_D} = {P_{K_D}=0}, which is closed and null. So D is completion-measurable and D = D_{K_D} a.e.
  - The converse direction follows from Lemma 1.5.
- **Def 1.9, "equal a.e." for arbitrary sets:** if X is a model and X△Y is null, then Y = X△(X△Y) is measurable. So the D in "X = D a.e." is automatically a model. This is what makes Prop 1.11(b) applicable in the advice sentence of Def 1.10, which is correct: D never contains both f and −f, by (D4) and (D1).
- **Example 1.14.** D_S = {⪈0} is coherent. {−𝟙} is null and {𝟙} is not. μ{P_Q=0} gets nothing from δ_𝟙 because P_Q(𝟙) = 1. The example is correct.
- **Lemma 1.19.**
  - (b): B ⊆ D°_{Q_B} ⊆ D_{Q_B} a.e. under (M2).
  - (c): q ≥ P_Q ≥ 0 on D_Q, and P_{Q_B} ≤ P_Q, so D_{Q_B} ⊆ D_Q.
- **Lemma 1.23 (Wincoherent), with no measure condition.**
  - G_1∖D ⊆ (G_1∖W) ∪ (W∖D) is null, so some x ∈ G_1∩D exists; likewise some y ∈ G_2∩D.
  - (x+y)/c ∈ D by (D3) and (D4).
  - z − (x+y)/c ≥ κ𝟙 ⪈ 0, so z ∈ D by (D2) and (D4). Hence G_3 ⊆ D, and G_3∩W is non-null. This gives the contradiction.
- **Section 4.**
  - Using D_S° in (U1), (U2) and Lemmas 4.5–4.9 is necessary. A gamble h ⪈ 0 can vanish at some worlds, so the change in Lemma 4.5 would not be guided. Lemma 4.8(c),(d) also need D_S° to be open.
  - Lemma 4.8(e): Lemma 1.17(a) gives D_K° ⊆ V ⊆ C_K. The estimate μ_c(X△D_K°) = 0 is correct. Atoms lie in ±D_S° (Lemma 1.16(d)) and are handled by (U1).
  - D_K∖D_K° is null by (M2), so X = D_K a.e., and D_K is coherent by Lemma 1.5. The contrapositive used in the proof of Thm 4.1 is valid.
- **Lemma 5.4, with no measure condition.**
  - Ω_0 is nonempty (inf_{Ω_0}𝟙 = 1). Off a null set, every h ∈ A has h > 0 on Ω_0, so h ≠ 0 and inf_Ω h = inf_{Ω_0} h ≥ 0, that is, h ⪈ 0.
  - B is handled symmetrically.
  - D_S ⊆ D by (D2). D∩(−D_S) = ∅ by (D2), (D4) and (D1).
- **Prop 5.5 (A5) under (M1) alone.**
  - The change from a coherent model C to Y has B = C∖Y ⊆ C and A = Y∖C, which misses C. So it is available to C in the exact sense of Def 1.20, and clause (ii) of Def 5.2 is blocked. Domination therefore forces guidance at every world.
  - Lemma 5.4 then gives Y = C a.e., hence a tie, which contradicts domination.
  - "Coherent model" means a model equal a.e. to a coherent set of desirable gambles. Availability depends only on the a.e.-class, so this is well defined.
  - Without (M2) this family is larger than the a.e.-classes of the D_Q, so the strengthened (A5) is a genuinely stronger and correct claim.
  - (A4) uses Lemma 1.23, which also needs no measure condition.
- **Cor 5.6.** (A1)–(A5) hold under (M1). "Undominated = coherent" holds under (M1)+(M2), via Cor 6.9.
- **Section 6.**
  - Cor 6.3: N_0 = H∩D_{q*}, and D_{q*}∖{q*>0} ⊆ {q*=0}, which is null by (M2). So N_0 = N* a.e. and m(N_0) = m(N*). In the v=0 case, X = N_0 a.e., so X is coherent. The exact equality claimed in the old version is indeed false for the new D, and the change is right.
  - Lemma 6.6: the case h ⪈ 0 ∖ D°_{Q_τ} gives q(h) ≥ 0 ≥ −aP(h). Correct.
  - Lemma 6.7: the reduction to D_Q via Lemma 1.17(b) is correct, and q ≥ P_Q ≥ 0 on D_Q.
  - Thm 6.8, consistent case: N_τ = D_{conv(...)} by Lemma 1.4(c),(d). N_τ increases to N_0 as τ decreases to 0, using the split between h ⪈ 0 and P(h) > 0. This is correct.
  - Thm 6.8, inconsistent case: H ⊆ C_{Q_{X+}} ⊆ {q*≥0}, which is enough because L ⊆ {q*<0}. N is equal a.e. to H∩{π*>0}. Part (3) uses Lemmas 1.17(b) and 1.19(c). All correct.
  - Cor 6.9: correct.
- **Global search.** I found no remaining claim that D_Q or D_S is open, and no use of "incoherent" that silently needs (M2). Every claim that coherent models are the a.e.-classes of the D_Q carries (M2) or sits in Section 6, where (M2) is standing.
- **Conditions table.** It matches: (M2) is used by Thm 4.1, Cor 4.10, the last claim of Cor 5.6 and Section 6, and not by Prop 5.5. (M1) and (M3′) are unchanged and correct.

## Required fixes

**1. app_fixed.tex, Def 1.7 (lines 179–181).** The sentence "the results of Sections 5 and 6 assume (M1), (M2) or both" is now false for Lemma 5.4, which assumes no condition. Its old version assumed μ{P_S=0}=0. The sentence also hides that Prop 5.5 needs only (M1).

Replace
```
The main results are not claimed for every finite Borel measure:
Theorem~\ref{thm:dominance} and Corollary~\ref{cor:admissible} assume (M2) and (M3$'$), and the
results of Sections~\ref{sec:integral} and~\ref{sec:repair} assume (M1), (M2) or both.
```
with
```
The main results are not claimed for every finite Borel measure:
Theorem~\ref{thm:dominance} and Corollary~\ref{cor:admissible} assume (M2) and (M3$'$);
Proposition~\ref{prop:axioms} assumes (M1); and the last claim of
Corollary~\ref{cor:existence} and the results of Section~\ref{sec:repair} assume (M1) and (M2).
```

## Recommended (not required)

**2. ldg_full_final.tex line 624, last sentence.** The current sentence is true, but it suggests that (M2) is a hypothesis of Prop 5.5. Replace
```
The integral ranking, defined under (M1), satisfies (A1)--(A4), and under (M2) it also leaves every coherent model undominated~\cite[Proposition~5.5]{KCM}.
```
with
```
The integral ranking, defined under (M1), satisfies (A1)--(A4), and also (A5) for the family of all coherent models: it leaves every coherent model undominated~\cite[Proposition~5.5]{KCM}.
```

All other KCM statements in ldg_full_final.tex remain true: line 518 (Thm 4.1 under (M2), (M3′)) and line 624 (Thm 6.8 and Cor 6.9 under (M1), (M2); Cor 4.10; Lemma 5.3(b)). ldg_short_final.tex line 180 (Thm 4.1) also remains true. Neither file cites a Section 1 number, so the Section 1 renumbering affects neither.

Log nit (not in the paper): WA76_changes.md calls the table "Def 1.6", but it sits in Def 1.7.
