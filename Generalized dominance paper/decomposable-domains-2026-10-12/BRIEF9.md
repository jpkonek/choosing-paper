# Brief, round 10 (14 Oct 2026, 13:45): the organised attack on the additive triangle problem

Read first:
- the Glossary and the 14 October interpretation note at the top of
  /mnt/user-data/uploads/Generalized dominance paper/START HERE -- Coverage Status.md, or the local copy if that path is stale;
- termfix/TERMFIX_RULES.md in the scratchpad.

Domains are classes of evaluable models only. Use "decomposable domain", "advice range" and "U-domain". Never use the superseded terms listed in TERMFIX_RULES.md.

Then read writeup/"The Contamination Triangle.tex":
- all of §§2–3;
- §4, the main theorem on the U-domain. Know its chain: straight levels, no pinning, pivot chords, no sliding, slope–rotation, blow-up, projectivity, corner equation, box;
- §5, general decomposable domains: (TS), the wall lemma, apex, vertex-free interiors, Lemma R1, CF(T), Prop CF, diagonal symmetries, and what is open.

## OBJECTIVE (author and auditor, verbatim intent)

Construct an exact additive cover of T1 on a general decomposable domain, or prove that no such cover exists, without adding assumptions.

By Prop CF this is the problem CF(T1). ⇒ is proved; ⇐ holds at the status of CCIBU.

Attack the WHOLE family, including compatibility between its interior, its edges and its vertices.
- Local constructions and computations must serve the global attempt; they are not destinations in themselves.
- Do NOT produce another list of necessary conditions or another "narrow residual" as your outcome.
- A residual can be narrowly described and still contain the entire hard problem.

If you fail, write an honest failure report. Say what the global obstruction or construction would have to look like, and where exactly your attempt broke.

## THE PROBLEM CF(T1)

Find a Hausdorff-continuous map q ↦ K_q from int Δ to credal sets, with K_{p*} = T1 for some interior p*. By symmetry p* may be any interior point.

For a.e. mixed g ∈ ℝ³ there must be vectors c, c′ with sign c_i = sign g_i = −sign c′_i, such that for EVERY q ∈ int Δ:
- P_{K_q}(g) > 0 ⟺ c·q > max(0, c′·q);
- P_{K_q}(−g) > 0 ⟺ c′·q > max(0, c·q).

Here P_K(g) = min_{m∈K} m·g. In words: for a.e. pair the triangle of priors is cut into "accept g", "accept −g" and "neither" by three rays from one point, the apex. The apex may lie outside Δ.

Non-mixed g are automatic (unanimous gambles are accepted by every K_q ⊆ Δ).

FULL FREEDOM is allowed:
- K_q may change dimension (points, segments, polygons, curved sets);
- K_q may be discontinuous in shape, though it must be Hausdorff-continuous (that is forced);
- the apexes may lie anywhere;
- the chart data may be any measurable choice.

Equivalent "self-consistency" form, to verify before use. Given chart data (c, c′) for a.e. g, put K_q := ∩{m : m·g ≥ 0 for g with q ∈ R(g)}. The data are consistent iff the induced K_q reproduce every chart exactly. A construction is a self-consistent chart field passing through T1.

## KNOWN NECESSARY CONDITIONS FOR ANY SOLUTION COMING FROM A COVER (statuses as in the write-up)

- **Basic structure.**
  - (TS), (PC) and (NS) hold.
  - The advice range of a.e. mixed pair contains both acceptances, so competition is required.
  - Single-vertex pinning near p* never occurs.
  - [Thm TSalways, one referee.]
- **Behaviour at the vertices and edges.**
  - K_q → {e_b} as q → e_b.
  - Edge limits are confined to the edge.
  - At each world with a failing box (the edge box Λ_ab > 1), cuts exist and their apexes converge to e_b.
  - Competition at positive distance from ∂Δ is impossible.
  - [Thm cuts, Thm apex, one referee.]
- **Interior credal sets.**
  - No interior K_q contains a vertex of Δ.
  - Every chord line λ_τ separates int Δ globally (Lemma R1, one reader).
  - K_q is never a singleton on a crossing chord λ_b = line(p*, e_b).
  - No precise prior lies on a crossing chord.
  - A precise cap on a full vertex neighbourhood is impossible.
  - [Prop vertexfree.]
- **Walls and d-faces.**
  - Walls W_{m0} = {q : K_q = {m0}} are convex and relatively closed.
  - A_b = {e_b ∉ K_q} is open and convex.
  - d-faces avoid priors whose K_q contains any m0 with m0·g ≠ 0.
  - [Lemma walls.]
- **Projective symmetries.** Diagonal projective maps act on priors and on probabilities (Prop diag). Use them to normalise.
- **What is NOT excluded.** The referee's sector-cap example (N28_referee §4.3, counterexample C1, NUMERICS) passes every constraint above. It consists of the identity K_q = {q} on a sector at e_b next to the failing edge, which carries the cuts.
  - The open gluing problem: glue the sector caps at the three vertices, a non-precise layer along the crossing chords, and the core near p* where K_{p*} = T1, under one concurrent chart for a.e. g.

## KNOWN CONSTRUCTIONS TO LEARN FROM

- **R10a Thm M (gauge mixtures).** Explicit additive systems covering polygons arbitrarily close to T1, including advice range {+,0,−} cases.
  - Why do these polygons succeed while T1 (apparently) does not?
  - What exactly changes in the limit? The gauge-mixture approximants converge to the cheap realisation, whose (LF) margin is O(a).
- **The two-world theory.** Every target is covered in two worlds (Full Coverage v3).
- **The main theorem's mechanism on the U-domain.** Half-plane charts force projective facet maps, which give the corner equation x + 1/x = κ + 1, which conflicts with the box 1/κ ≤ x² ≤ κ.
  - On general domains, wedge charts with competition near the crossings are what escape the corner/box contradiction.

## RULES

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- State every hypothesis.
- Add NO assumption to the problem. If a partial result needs one, say so in the result's statement.
- Never assume regularity (smoothness, continuity of chart data, finitely many pieces) unless you prove it.

Files:
- Write only your own note, plus scripts in a subfolder named after it, inside this folder:
  /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/
- You may read the other team's files, but do not depend on them; they run concurrently.
