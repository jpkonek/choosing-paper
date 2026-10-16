# Brief, round 8 (13 Oct 2026, 19:30). Read BRIEF.md–BRIEF6.md first, then N12_notes.md and N14_referee.md (§§0, 5, 6).

## Where things stand (REFEREED, N14 §6)
No strictly guiding additive realisation of T1 exists (integral penalties, or bounded charges vanishing on null sets
given existence of interior Bayes minimisers) with unique coherent interior Bayes models, T1 Bayes at p*, (LF), on a
non-adjacent domain (e.g. the U-domain, whose evaluable models are the measurable subsets of U = D_{K′}), PROVIDED (DD) holds at p* on all three facets of D_T:
for facet gambles h, the one-sided directional derivative D(δ,h) = lim_{t↓0} P(p*+tδ, h)/t exists, is continuous in δ,
and takes both signs (P(q,h) = min_{m∈K_q} m·h). The edge box holds unconditionally (N12.3). Excluded already: vertex
pinning on arcs containing a crossing, isolated (DD)-failures, sliding edges next to (DD) facets.

Remaining gap: on some facet F_k a non-isolated set Z_k of rays where (DD) fails, via
 (F1) oscillation of P(p*+tδ,h)/t as t ↓ 0; (F2) direction-discontinuity of the limit; (F3) flatness: limit ≡ 0, or
 half-flat α[n·δ]₊ / −β[n·δ]₋ (incl. pivot degeneracy P(·,h) ≡ 0 near p*, possible only on arcs with no crossing).
Proposed route (N14 C1′): rescaled limits P(p*+t_jδ,h)/m(t_j) → G(δ,h) locally uniformly, G continuous two-signed;
then Lemma 4.1 ⇒ ridge G = φ_h(n(h)·δ), φ_h increasing; Lemma 4.2 ⇒ unique pivot clusters; still needed: a version of
Lemma 4.3 (projectivity) for non-linear φ_h; and compactness (Lipschitz control of K_q at p*, or a substitute).

Structural facts to exploit (verify): P(q, h − c𝟙) = P(q,h) − c, so every level set {q : P(q,h) = c} contains a
separating chord and every superlevel set {P(·,h) > c} is (a.e.) an open half-plane in int Δ (vertex-respecting).
So each P(·,h) is a function on the simplex all of whose strict superlevel sets are half-planes: its level sets are
"straight", and level sets of different levels do not cross. Rescaling preserves this. P is concave in h for each q.

## Tasks
- N15 (proof): close the gap: prove that every realisation satisfies the conclusions needed by the corner/box argument
  (unique limiting chords through p* with a projective facet map; no sliding edges), without assuming (DD). Use the
  straight-level-set structure directly (it may give regularity for free: a function whose superlevel sets are
  half-planes is, near p*, determined by a non-crossing family of chords), blow-ups, and concavity in h. Or prove the
  corner/box contradiction directly in terms of chords, without derivatives.
- N16 (adversary): try to BUILD a realisation exploiting (F1)–(F3): e.g. oscillating/spiralling vertex motion of K_q
  near p*, direction-discontinuous chord fields, flat facets. Check every requirement (coherence at every interior q:
  K_q compact convex with K_q ⊇ K′; half-plane positivity sets for every gamble; K_{p*} = T1; strict signs). If every
  attempt fails, isolate the reason and turn it into a lemma.
Labels PROVED / CHECKED / CONJECTURE / NUMERICS; no silent regularity; scripts in subfolder named after your note.
