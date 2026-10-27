# Brief 46: local defences for every selected model (22 October 2026)

This round aims at the co-design step audit identified: a coherent defender chosen TOGETHER with its own defence rule, so that defence is a property of a whole family, not of T alone. Be original and ambitious. Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. Plain English. Add no assumptions beyond those stated; name any you need as hypotheses. Keep each note under about 12 pages. Write only inside the scratch folder below.

## Read first (paths relative to /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/)
- `AUDIT_local_defences.md` (audit's new note: Proposition 1, Corollaries 2–4, the extension principle in §5, the round plan in §6–7). This defines the task.
- `PP20_completion_measurable.md` (coarsening defenders; T competitive against every model; records a, b, t).
- `AUDIT_completion.md` (closure rules I–IV, failures F1/F2; (TC) = triangle completion).
- `PP18_source_field.md` (Theorem Z), `REFEREE_Z_PP19.md` (Lemma H, Prop S), `PP21_closure_engine.md` (minimal failure shapes; Lemma Q).
- `DESIGN_MEMO.md` §§5, 8 (screens, gates, PP2 Thm 6, quorum rules, convexity screen S8) and `gate2d/Separation-Gated-Evaluators.tex` (the two-world construction, which works).

## Setting
- Three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain, models modulo null sets. Ranks good 0 < silent 1 < bad 2 < contradictory 3. Mixed problems split into M_1, M_2, M_3 (M_k: world k is the minority sign); U = unanimous problems.
- T = T1 = D_M, M = c·1 + εΔ.
- Axioms: reflexivity; strict (G); (IB) (verdict depends only on the record: disagreement set and the two advice values on it; all common-context copies share it); (TC) only (no transitivity; equivalently every accepted triangle has all three reverses); (S): coherent selected C_p, undominated, competitive on supp p, closed sections {p : C_p ⪯_w X} for fixed X; (LA); direct (C) (all-world tie partners of a coherent undominated model are coherent).
- Do not use approaches equivalent to the CPM realisation problem. Do not make ℓ^m proper.

## The obligation (audit Prop 1, Cor 4)
Every competitive coherent model N other than T and V_1, V_2, V_3 needs accepted, non-guidance, bounded-support comparisons N ⪯_i Y against small local rivals Y, whose old side is N's advice (not T's). In particular, for disjoint small sets E_1, E_2, E_3 where N is not i-correct, the rival correcting N at i on E_i must be defended at some world.

## Lead's observations (check them; use or discard)
1. **Uniformity comes free from (IB).** A local defence is a property of record classes (D, a → b). All models with the same advice a on D share it. So a rule on local record types automatically treats a whole family uniformly. The question is which record types can be accepted, at which worlds, consistently.
2. **Triangle lemma.** If D(A,B) and D(B,C) are bounded, so is D(A,C). So in every triangle the number of edges with unbounded disagreement is 0, 2 or 3. Local (bounded) defences and global dominations (unbounded, e.g. coherent defender → rival) interact only in triangles with exactly one bounded edge, or within the bounded layer.
3. **Departures.** Call a record a *departure* if its old advice is silent throughout D. Candidate rule: at each world, accept every departure that is not a pure improvement at that world. Sketch: two departures compose only on disjoint supports into a departure, and an accepted departure keeps an i-harm that guidance cannot remove, so departures plus guidance appear (TC)-safe (prove or refute, with all copies). PP20's t records (T → fill of T's silence) and b records (coarsening → rival) are departures. This rule defends EVERY model against fills of its own silence, including audit's concrete rival against C_w.
4. **Retreats break it.** Departures (silent → answer) and retreats (answer → silent) accepted at the same world under "not a pure improvement" form a pump. Example at world i: A → B departs on {g, h} (wrong at g, correct at h); B → C retreats on {g, h, F} (F: B wrong at i). Composite A → C improves only on F, so C ≺_i A by guidance: a (TC) violation. Retreats and flips in a model's answered region therefore need a different structure (gates, region assignment, or something new).
   - Retreats cannot simply be refused. If all departures are accepted, then Z := N with silence on pieces of M_1, M_2, M_3 where N gives the majority answer satisfies Z ⪯_i N at every world (each piece is wrong at some world). If no retreat N ⪯_i Z is accepted, Z strictly dominates N. So each world must decide which departures and which retreats it accepts, and the pump in point 4 constrains that split.
5. **Region structure.** On M_k the two majority worlds see identical rank changes, so each region is a two-world problem ({k} versus the other pair), where the gated two-world construction works. Records spanning several regions are the genuinely three-world part.
