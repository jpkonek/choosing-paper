# WA76 changes: app_in.tex -> app_fixed.tex

Purpose: restore the Loss Relations convention (USER_1425). A coherent set of desirable gambles
is now defined; D_Q is now a coherent set of desirable gambles; a model is coherent iff it is
a.e. equal to a coherent set of desirable gambles. Numbering in Sections 2-6 is unchanged
(Thm 4.1, Cor 4.10, Lemma 5.3, Prop 5.5, Thm 6.8, Cor 6.9 keep their numbers, as cited by LDG).
Section 1 items after Def 1.1 shift by up to 2 (new Def 1.2 and Lemma 1.5).

## Section 1 (setting)

| Item | Change | Why |
|---|---|---|
| Def 1.1 Worlds and gambles | Added: g ⪈ 0 means g ≥ 0 and g ≠ 0. | Needed for (D2) and D_Q. |
| **New Def 1.2** [Coherent sets of desirable gambles] | (D1) 0 ∉ D; (D2) g ⪈ 0 ⇒ g ∈ D; (D3) positive scaling; (D4) closed under addition. One-line gloss. | The draft never defined this. |
| Def 1.3 States and credal sets | Now D_Q^∘ := {P_Q > 0} (open part) and D_Q := D_Q^∘ ∪ {g ⪈ 0}; {q>0} = D^∘_{q}. | Old D_Q = {P_Q>0} misses nonzero g ≥ 0 with P_Q(g)=0, so it was not coherent. |
| Lemma 1.4(b) | D_S^∘ = {inf h > 0}, −D_S^∘ = {sup h < 0}, and D_S = {h ⪈ 0}. | D_S changed meaning; proofs needing openness now use D_S^∘. |
| Lemma 1.4(c) | Openness and convex cone claims now about D_Q^∘; D_S^∘ ⊆ D_Q^∘; neither D_Q^∘ nor D_Q contains h with sup h ≤ 0; intersection rule holds for both D^∘ and D. | As above. |
| **New Lemma 1.5** (lem:DQ) | D_Q is a coherent set of desirable gambles and Borel; D_Q^∘ is its interior; D_Q^∘ ⊆ D_Q ⊆ C_Q; D_Q \ D_Q^∘ ⊆ {P_Q = 0}. Short proof inline. | Task item 2. |
| Def 1.6 (table) | (M2) row: "boundary of D_Q^∘"; Used by: Thm 4.1, Cor 4.10, last claim of Cor 5.6, Section 6 (where Lemma 1.17(b) makes coherent models exactly the a.e.-classes of D_Q); explicitly *not* Prop 5.5. | Prop 5.5 no longer uses any instance of (M2). |
| Def 1.9 Models and coherence | "Equal a.e." now defined for arbitrary sets (then X model iff Y model). Coherent := X = D a.e. for some coherent set of desirable gambles D. Sentence: every model a.e. equal to a D_Q is coherent (Lemma 1.5); under (M2) every coherent model is of that form (Lemma 1.17(b)). Removed "Each D_Q is open". | Task item 3, 6(iii). |
| Def 1.10 Advice | D_Q sentence replaced: a coherent set of desirable gambles never contains both f and −f (f + (−f) = 0 ∈ D by (D4), contra (D1)); under (M4) a coherent model gives contradictory advice only on a null set of choices (Prop 1.11). | Task item 5. |
| Example 1.14 | Now: "the coherent set of desirable gambles D_S and the model D_S ∪ {−1} are equal a.e., so the second is a coherent model; yet …". Mathematics unchanged (D_S = {g ⪈ 0} still gives strict advice for 1). | Shows the (M4) clause of the advice sentence is needed. |
| Lemma 1.16(d) | A_μ ⊆ D_S^∘ ∪ (−D_S^∘). | Old D_S was the open set. |
| Lemma 1.17 (lem:identify) | Now two parts. (a) old statement with D_S^∘: convex cone, 0 ∉ D, D_S^∘ ⊆ D ⇒ K_D credal and D^∘_{K_D} ⊆ D ⊆ C_{K_D} (needed for the open set V in Lemma 4.8). (b) every coherent set D: K_D credal and D_{K_D} ⊆ D ⊆ C_{K_D} (stronger than D^∘ ⊆ D, because (D2)); under (M2), D is a model and D = D_{K_D} a.e.; so under (M2) coherent models = a.e.-classes of the D_Q. Proof in appendix adapted from app_r70 (Hahn-Banach separation with 1 ∈ E). | Task item 4. |
| Lemma 1.19 (hull) | Statement unchanged; hull(B) = D_{Q_B} now uses the new D. Proofs of (b),(c) adjusted (B ⊆ D^∘_{Q_B} ⊆ D_{Q_B} a.e.; q ≥ P_Q ≥ 0 on D_Q). | Remains true for new D_Q. |
| Lemma 1.23 (Wincoherent) | Statement unchanged; **new proof for any coherent set D, no measure condition**: W = D a.e. and G_1 non-null ⇒ G_1 ∩ D non-null ⇒ pick x; same for y; (x+y)/c ∈ D by (D3),(D4); z − (x+y)/c ≥ κ1 ⪈ 0 ⇒ z ∈ D by (D2),(D4); so G_3 ⊆ D and G_3 ∩ W is non-null. | Task note (i). |

## Section 4 (dominance theorem)

| Item | Change | Why |
|---|---|---|
| Def 4.4 (U1),(U2) | D_S → D_S^∘. | Proofs use the open set {inf > 0}; with D_S = {g ⪈ 0} they would fail without (M2). |
| Lemmas 4.5, 4.6, Cor 4.7 | D_S → D_S^∘ throughout (statements and proofs). Hypotheses unchanged. | Same. |
| Lemma 4.8 (lem:open) | V := spt X + D_S^∘; (c),(d) with D_S^∘. (e): uses Lemma 1.17(a) to get D^∘_K ⊆ V ⊆ C_K, shows μ(X △ D^∘_K) = 0, then D_K \ D^∘_K ⊆ {P_K = 0} is null by (M2), so X = D_K a.e., and D_K is a coherent set of desirable gambles (Lemma 1.5); hence X is coherent. Hypotheses unchanged ((M3′); (M2) in (e)). | Coherence-identification step now matches the new definition. |
| Lemma 4.9, proof of Thm 4.1 | D_S → D_S^∘. | Same. |
| Thm 4.1, Cor 4.10 | Unchanged statements. Under (M2) the new and old notions of coherent model coincide (Lemma 1.17(b)). | — |

## Section 5 (integral ranking)

| Item | Change | Why |
|---|---|---|
| Def 5.2 | Unchanged; "available to a coherent model" now means a model a.e. equal to a coherent set of desirable gambles (availability depends only on the a.e.-class). | — |
| Lemma 5.4 (guidedeverywhere) | **Hypothesis μ{P_S = 0} = 0 removed.** New statement: guided at every world ⇒ A ⊆ D_S = {h ⪈ 0} a.e. and B ⊆ −D_S a.e.; every coherent model contains A a.e. and meets B in a null set. Proof: countable Ω_0 gives h(ω) > 0 on Ω_0, hence h ≠ 0 and inf h ≥ 0; then (D2) for A, and D ∩ (−D_S) = ∅ by (D2),(D4),(D1) for B. | Task note (ii). |
| Prop 5.5 | **Now: assume (M1); the integral ranking satisfies (A1)–(A4), and (A5) for the family of all coherent models.** (Old: (A5) needed μ{P_S = 0} = 0.) (A5) proof rewritten for an arbitrary coherent model C. | Follows from new Lemma 5.4. |
| Cor 5.6 (existence) | **Now: for every μ with (M1), the ranking satisfies (A1)–(A4) and (A5); if μ also satisfies (M2), its undominated models are exactly the coherent models.** (Old: (M1) and (M2) for everything.) | Same. |

## Section 6 (repair)

| Item | Change | Why |
|---|---|---|
| Section preamble | Added: by Lemma 1.17(b), under the standing (M1),(M2), coherent models are exactly the models a.e. equal to some D_Q. | Task 6(iii). |
| Cor 6.3 (consistent) | **Statement changed:** N_0 := D_{conv(Q_X ∪ {q*})} is coherent, is equal a.e. to hull(X) ∩ {q* > 0}, and satisfies the bound. (Old claimed the exact equality hull(X) ∩ {q*>0} = D_{conv}, false for the new D.) Proof: N_0 = H ∩ D_{q*} differs from H ∩ {q*>0} only within {q* = 0}, null by (M2). | Exact equality fails on {g ⪈ 0, q*(g) = 0}. |
| Lemma 6.6 (trim) | Statement unchanged; proof adds the case h ∈ N \ D^∘_{Q_τ}, where h ⪈ 0 gives q(h) ≥ 0 ≥ −aP(h). | N ⊆ D_{Q_τ} may now contain such h. |
| Lemma 6.7 (change) | Statement unchanged; proof now starts from an arbitrary coherent model and uses Lemma 1.17(b) ((M2)) to replace it by some D_Q; q ≥ P_Q ≥ 0 on D_Q via Lemma 1.5. | New definition of coherent model. |
| Thm 6.8 (repair) | Statement unchanged. Consistent case: N_0 = H ∩ D_{q*} ⊆ H; N_τ = D_{conv(...)} exactly (Lemma 1.4(c) for D); monotone convergence argument now treats h ⪈ 0 separately. Inconsistent case: H ⊆ {q* ≥ 0} (not {q* > 0}); N := D_{conv(Q_{X+} ∪ {π*})} = H ∩ D_{π*}, a.e. equal to H ∩ {π*>0} by (M2); (3) uses Lemma 1.17(b). | Old proof used the open D_Q. |
| Cor 6.9 | Statement unchanged; proof cites Lemma 1.5 for coherence of N = D_Q. | — |

## Appendix

- Proof of Lemma 1.4: (b) adds D_S = {h ⪈ 0}; (c) open/cone claims for D_Q^∘, sup h ≤ 0 excluded from both, intersection rule for D^∘ and D.
- Proof of Lemma 1.16(d): D_S^∘.
- Proof of Lemma 1.17: (a) old Steps 1–4 with D_S^∘ and D^∘_{K_D}; (b) new: coherent D satisfies (a)'s hypotheses, D_{K_D} ⊆ D by (D2), and under (M2) D \ D_{K_D} ⊆ {P_{K_D} = 0} is null.
- Proof of Lemma 1.19(b),(c): adjusted as above.

## Statements whose hypotheses changed

- Lemma 5.4: drops μ{P_S = 0} = 0 (now no measure condition).
- Prop 5.5: (A5) now under (M1) alone.
- Cor 5.6: (A1)–(A5) under (M1) alone; (M2) only for "undominated = coherent".
- Lemma 1.17: now two parts; (b) is new (coherent sets; (M2) for the a.e. identification).
- Cor 6.3: N_0 now defined as D_{conv(Q_X ∪ {q*})}, equal a.e. (not exactly) to hull(X) ∩ {q*>0}.
- Lemma 1.23: unchanged statement, proof now needs no measure condition.

## Note for the companion paper (not edited)

ldg_full_final.tex line 624 says the integral ranking "under (M2) also leaves every coherent model
undominated [KCM, Prop 5.5]". Still true, but (M2) is no longer needed: (M1) suffices.
