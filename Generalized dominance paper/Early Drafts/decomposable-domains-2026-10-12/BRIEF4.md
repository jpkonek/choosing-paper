# Brief, round 5 (13 Oct 2026, 12:00): PERMITTED negligible-stakes ties. Read BRIEF.md, BRIEF2.md, BRIEF3.md first.

## The weakening (author-accepted in principle, 13 Oct)
Fix θ > 0 (state the norm: sup or Euclidean; say whether results depend on it). Band of world i: mixed problems with
|g_i| ≤ θ‖g‖. PERMITTED NSI_θ ("lenient reading"): in additive form, with r_i(g) := ℓ_i(g, silence) − ℓ_i(g, good),
- r_i(g) ≥ 0 on band-i problems (ties ALLOWED, not forced; the ranking chooses where, measurably);
- r_i(g) > 0 off the band;
- bad strictly worse than silence, contradiction strictly worst, unanimous problems strict, at every world.
(G) reads: weak improvements in the four-rank order are weak improvements; strict improvements outside the permitted tie
set are strict. The author ACCEPTS target-dependent placement of ties inside the band (a ranking built to vindicate
one target may tie exactly near that target's coordinate crossings), provided θ can be made small. Ideal result:
for EVERY θ > 0, T1 (ε-contamination of the uniform prior, n = 3; fix ε, e.g. ε = 0.3, and also state ε-dependence)
is covered EXACTLY. Approximation does not count.

Everything else as before: decomposable domains (SC + closed in measure), (IB), (LA), (S), (C), (E), (LF) at the target,
additive rankings first. No cheap realisation; nothing that makes (G) or (IB) vacuous.

## Why this might matter (the specific mechanism to test)
Under strict guidance, T1 is excluded only conditionally: R15 Thm 6.2 needs (DF), (ND), (NA_w). Its contradiction comes
from (i) crossing rows λ_{ik}e_i with λ_{ik} > 0 at each coordinate crossing w_{ik} ∝ v_k × e_i of a facet F_k
(R15 Thm 1(c)), (ii) corner proportionality, and (iii) the vertex-limit box (R15 Lemma 6.1, from R10b Lemma FS with
witnesses near the b-crossings). The positivity λ > 0 and the box witnesses use STRICT sign of c_i(g) at gambles near
the crossings, i.e. exactly in the band, for every θ > 0. Also R10a Thm V (vertex anchoring), R10a Thm R (ray lemma).
So permitted ties near crossings are available for every θ > 0, and they relax exactly the inputs of those no-gos.

## Known constraints on where ties can go (verify; these are author-CHECKED or referee-level as stated)
- N2 Lemma 0/1 (REFEREED): on tied band-i⁺ problems c_i = 0, and the chart is a union of rays from δ_i (ray transport).
- N2 Thm B tie-region version (REFEREED with repair, N4): ties on an open piece U of the band around a target-boundary
  gamble w on BOTH sides, with contact m cut by a strictly-good-at-i x whose acceptance is in the advice range (m·x < 0), are impossible.
- N2 Prop L (CHECKED only; verify): ties on the OUTER side (just outside D_T) near such w are impossible; ties on the
  INNER side only "add rigidity" (transport away from δ_i).
- N3 Thm PL_θ, Cor ST1 (REFEREED): no plateau under any tie rule (strictness off-band suffices).
- N3 Cor ST2 (REFEREED, under (NA)): near a tied crossing piece, the priors keeping T's local facet lie on one line
  through e_i and p*. For a non-plateau family this may be just {p*}: a constraint, not a contradiction.
- Claim of the coordinator (UNVERIFIED; check first): if ties are inner-side only near each crossing, R10a Thm V
  survives. Sketch: at q → e_i, outer band points near a crossing r (r_i = 0, r ∈ relint F_v) with h_i > 0 are strict
  (by Prop L) hence accepted; h_i < 0 points are rejected (bad is strict); so the tangent cone at r of the vertex
  acceptance cone contains {d_i ≥ 0, v·d ≤ 0} + span r; a nonnegative supporting normal n with n·r = 0 must then be
  ∝ e_i (write n = αe_i + β(v − v_i e_i), test d with d_i = 0, v·d < 0). So e_i ∈ V_i still.
- Closed choice: CCIBU (strict) and N3 Thm CC_θ (forced ties) give (S) from unique coherent interior Bayes models in
  n = 3. For permitted ties the vertex face can be large; re-check that N3's blow-up selection still works.
- Interior Bayes uniqueness from (C): tied kinds of advice still differ at the world with the largest stake if θ < 1 (sup)
  or θ < 1/√3 (Euclidean). So IBU is still forced.

## Files
All in this folder: BRIEF*.md, R1–R18 notes/referees, N1–N4, CCIBU.tex, Consolidated Statements, AUDIT_ASSESSMENT*.md.
Most relevant: R15_notes.md (+ R18_referee.md), N2_notes.md (§§1–3, 7), N3_notes.md (§§1, 5), N4_referee.md,
R10a_notes.md (Thm V, Thm R, Thm M, Prop M′), R10b_notes.md (Lemma FS, UVN, M, Thm PL), R1_notes.md (charts, Lemma 1.4,
Prop 2.1, Lemma 3.5). Python is available; put scripts in a new subfolder n5py/ (or n6py/). Do NOT write outside this
scratch folder. Do not use theorem names inside theorem environments if you write LaTeX (you need not).

## Labels
PROVED (full proof written), CHECKED (verified, sketch), CONJECTURE, NUMERICS. Be explicit about every hypothesis
beyond the adopted axioms; no regularity assumption may be imported silently. Do not overclaim: a no-go for a
restricted class must be labelled as such, and a construction must be checked against EVERY requirement (IBU and
coherence at EVERY interior prior, (LF), strict/permitted (G) everywhere, (IB), advice ranges measurable, T Bayes at p*).
