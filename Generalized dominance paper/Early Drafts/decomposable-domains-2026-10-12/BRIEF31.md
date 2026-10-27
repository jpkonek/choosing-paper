# Brief, round 39 (18 Oct 2026, 19:00): verify; reopen the non-(Av) domain branch; nonprotected rate designs

Read FIRST: AUDIT_JJ.md and AUDIT_JJ_summary.md (audit's assessment of round 38). Adopt its corrections.

## Corrections adopted
1. **Scope of the new exclusion (PROVISIONAL, pending this round's checks).**
   - Protected weak-additive designs are excluded on the full domain and on (LF) domains satisfying (Av).
   - Still OPEN: protected designs on other admissible (LF) menu domains (JJ3 §7); non-protected rate designs; general (FC) rankings; the clone route.
   - (Av): for every pair of worlds l, o, accepting g is available for a.e. gamble positive at l and o, however negative at the third world. (LF) protects only a neighbourhood of ∂D_{T1}; the adopted domain axioms do not obviously imply (Av).
2. **Dependency on ccibu, stated precisely.**
   - JJ3's final step invokes ccibu.
   - JJ2's direct route (Thms 7.2, 7.4) CLAIMS to bypass ccibu by auditing gm's short route under weak signs (Table 7.2, items S8a, S8b). JJ2's alternative removal route uses ccibu.
   - The bypass must be checked, not assumed.
3. **Gap in JJ3 Lemma 4.2 step 6.** "t0 = max(m_h, m_h′), both s_h and s_h′ exceed t0" does not follow from m_h < s_h and m_h′ < s_h′. Likely repair (audit):
   - Show that the O-minimiser set on the WHOLE opposite edge is exactly (s_h, 1), modulo endpoints. Indeed c′(t) > 0 exactly for t > s_h; at t = s_h, c(t) < 0, so d = c − c′ < 0; and d(1) < 0. Linearity gives d < 0 on (s_h, 1); for t < s_h, c′ < 0 prevents O-minimisation.
   - Then Fubini identifies (s_h, 1) with (s_h′, 1) without truncation.
   - This must be inserted and verified explicitly.
4. **No headline that "the axioms exclude T1".** Approximate coverage stays a recorded side result, not the objective. The objective remains EXACT coverage of T1.

## This round
- **KK1. Referee JJ2 and JJ3.**
  - JJ3's new geometric argument, with the Lemma 4.2 repair written out.
  - JJ2's claimed ccibu bypass (Table 7.2, S8a/S8b; the claim that gm's short route uses a cover only through its interior Bayes family).
  - The removal lemmas of both notes.
- **KK2. A complete proof (or refutation) of ccibu,** with all boundary content explicit. CCIBU.tex is in this folder; the write-up has a sketch (search "thm:ccibu"). Audit names three points:
  - existence of the needed finite subgradients at endpoints;
  - uniqueness and coherence of directional minimisers;
  - lower semicontinuity of the quadratically selected loss coordinates after the boundary tie-break.
- **KK3. The non-(Av) branch (targeted).** Do the ADOPTED requirements (menu/decomposable domain with splice closure, (LF) at T1, a coherent selection with coherent vertex choices, closed competitive choice) force the edge confinement that JJ3 Lemma 4.2 needs, even without (Av)?
  - If yes, extend the impossibility theorem.
  - If no, exhibit a concrete admissible menu where confinement fails, and test a protected weak-additive construction there (then lift it by JJ1).
  - Do NOT return to M_U, which is already excluded.
- **KK4. Non-protected rate designs.**
  - Locate a failure of leading protection at a definite index, realised by an actual competitor.
  - Show how the lower level defends against it, and check II2's necessary condition (★) (Bayes on the defending worlds).
  - Then prove the defence is uniformly adequate across nearby indices, using the exact rate-bound criterion (RB).
  - A field that merely permits ties is not progress.

## Read
- AUDIT_JJ.md, AUDIT_JJ_summary.md, BRIEF30.md, AUDIT_II.md;
- JJ1_referee.md (lifting theorem), JJ2_notes.md, JJ3_notes.md;
- II1_notes.md (§§3, 6), II2_notes.md ((★), Thm 2.1, Thm 3.1, §3);
- CCIBU.tex; writeup/"The Contamination Triangle.tex" §§2, 4–7 (gm, its three routes, ccibu, kkm, CF(T1));
- AUDIT_HH_rate.md (RB).

## Rules
As in BRIEF13. Labels PROVED / CHECKED / CONJECTURE / NUMERICS. Add no assumptions. Write only your own note, plus scripts in a subfolder named after it. Exact arithmetic for checks.
