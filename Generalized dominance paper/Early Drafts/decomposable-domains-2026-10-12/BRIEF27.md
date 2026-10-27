# Brief, round 35 (18 Oct 2026, 09:00): the non-Archimedean credal class — settle it

## Author's directive
Take a high-level view. Make the most ambitious step that can settle the T1 question. Do not polish edge cases. Do not push hard on a small problem.

## Where the project stands (one paragraph)
- **Excluded covers of T1 (refereed or proved):**
  - additive covers (gm);
  - covers in which every world adds up (M0closed; Q4.2 on all (LF) domains);
  - intersections of real additive rankings (project doc);
  - vetoes / lexicographic designs ranking wrong acceptances first (L3.4);
  - decorated additive bases (H1, H2, E1, J1, K1, U1);
  - non-additivity placed at the simplex edges, for selections continuous in measure (FF2 Thm 4.1, unrefereed).
- **Necessary features of a cover:**
  - a degenerate ("blind") endorser field (L4, Q3.25);
  - non-additivity in the bulk near T1 (FF2 Cor 4.3);
  - incomparability (three complete worlds cannot cover).
- **Round 34 (FF1, FF3; unrefereed).** For the plain posterior family, the threshold scheme's selected layer is consistent: its ties are the level sets of the upper probability of world i. FF1 Prop 8.1: a cover follows if each world's comparisons are additively separable on every finite subfamily, with witnesses varying.

## The class to settle
- **Definition (NA-credal world).** World i is NA-credal if
  ≼_i = ⋂_{L ∈ Π_i} ≤_L,
  where each L : models → (ordered abelian group, e.g. hyperreals *ℝ, Hahn series ℝ((ε^Γ)), or ℝ^n lexicographic) is
  - additive in the record sense: L(X) − L(Y) depends only on rec(X, Y), so that every (IB) transport and every cancelled-change composite is respected;
  - strictly guiding: every non-null pointwise guidance improvement strictly lowers L.

  Real-valued L is the special case giving intersections of additive rankings (already excluded).
- **Automatic properties.** Any NA-credal world has strict (G), (IB) and transitivity (one line: each ≤_L has them, and intersection preserves them). Only (LA), (S) (closed sections, competitiveness), (C), (LF) and T1 undominated are at stake.
- **Expected equivalence (GG3 to prove).** By compactness / Łoś over finite subfamilies, a world is NA-credal iff it is closed under (IB) and transitivity, and every accepted comparison set together with every single NON-comparison is finitely additively separable by cell witnesses (FF1 §3 and Prop 8.1).
- **Consequences of the equivalence:**
  - The NA-credal class is exactly the world type with no finite obstruction, plus separability of non-comparisons; this is essentially write-up type (M2).
  - Worlds outside it have a finite non-priceable obstruction, as the CC1 seeds do (type M1).
- **Why this class is natural.**
  - The standard part of L may be blind (zero) on non-null regions, matching the L4 necessary condition. Infinitesimal layers keep guidance strict there.
  - In the literature these are sets of lexicographic / non-Archimedean probabilities (Blume–Brandenburger–Dekel 1991; Seidenfeld–Schervish–Kadane coherent choice without the Archimedean axiom; Van Camp–De Bock lexicographic choice; Benci–Horsten–Wenmackers non-Archimedean probability).
  - VB is a two-level instance with a single L per world. It fails only closed sections at boundary weightings.

## The decisive question
**Is there a cover of T1, on some (LF) decomposable domain (M_U or the full two-sided domain), in which every world is NA-credal?**
- **Yes:** T1 is covered, which settles the project positively.
- **No:** every cover needs a world with a genuine finite obstruction. That is a strong, publishable impossibility, leaving one precisely described residual class.

## Rules
As in BRIEF13. Every construction must verify every axiom: strict (G), (IB), transitivity, (LA), (S) with closed sections for EVERY evaluable model and competitiveness on supp p, (C), (LF) at T1, and T1 undominated. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it, in this folder. Deliver a theorem or a construction, not a list.

## Read
- writeup/"The Contamination Triangle.tex":
  - §2: axioms, domains, (S), (C), (LF), guidance;
  - the (M0)/(M1)/(M2) division (search "(M2)");
  - §7: M0closed and kkm;
  - §8.6: fixed-point reduction, R21, K3 Yosida–Hewitt classification (search "Yosida").
- /home/claude/proj/nonadditive_map.md (exploration map).
- FF1_notes.md (§§3–5, Prop 8.1), FF2_notes.md (Thm 4.1, Lemma 2.4, Lemma 3.2), FF3_notes.md.
- L3_notes.md (VB, L3.3–L3.4), L4_notes.md (fixed point), BB2_notes.md, CC3_referee.md (Q4.2), AUDIT_BB.md (Lemma 2.0).
- AUDIT_nonlinear_programme.md and AUDIT_EE_ties.md.
- INTERSECTIONS_additive.md in this folder: the real-valued intersection theorem, with its 7-step proof. This is the template that GG2 must generalise. Watch where it uses real values:
  - Step 1, countable dense mixture;
  - Step 2, strictness transfers to the mixture;
  - Step 5, Lyapunov plus separation in ℝ^S;
  - Step 6, a zero weight versus an infinitesimal weight.
