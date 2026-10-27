# Brief, round 13 (15 Oct 2026, 09:40): edge nestedness (R4) and mirrored pairs (R1)

## Read first
1. termfix/TERMFIX_RULES.md.
2. writeup/"The Contamination Triangle.tex":
   - §§2–3;
   - §7.7 (M0 closed);
   - §8.4 (sec:open-ordinal), in particular part (c), two worlds with a nested selection: strict escape, E2, E3, B2, the open class;
   - §8.5 (sec:open-core), all of it:
     - Theorem R3;
     - Lemma Q34 (edge complementarity);
     - (Nest_e);
     - Prop Q35 (edge reduction);
     - Thm Q36 and Cor Q37;
     - Prop comonotone (on the edge models co(K′ ∪ [x,y]), (Nest_e) ⟺ comonotone endpoints);
     - part (c): cut form, Lemma T₂, Theorem LF, Corollary IS, Prop MP, MP-loop, MP′, Prop NS;
     - part (d): the two-parameter lattice of coherent error sets without nestedness, 1-D KKM, G-SE, Conjecture Q2.N;
     - part (e): Q1.0–Q1.6, the exponential-tilt world, N1–N4;
     - part (f): (R1)–(R4) and how they lift.
3. Notes:
   - Q1_notes.md, Q2_notes.md, Q3_notes.md;
   - Q3_referee.md (§4.4 comonotonicity);
   - Q12_referee.md (§4 N1–N4; §6 the remaining question);
   - P4_notes.md Part B and P4B_referee.md (Lemmas DL, DR, T, strict escape, E2, E3).

## TASKS (this round)
- **(R4) Nestedness from (S).**
  - Two worlds: does closed competitive choice (strict (G), (IB), (LA), (S) with closed sections for every model, (C)) force the selected coherent models to have nested world-1 error sets (Conjecture Q2.N)?
  - Edge form in three worlds: on each edge, does it force (Nest_e), equivalently comonotone endpoints on the coherent edge models?
  - The write-up notes that (Nest_e) "can fail at exceptional edge weights where a non-null tie set is split in crossing ways". So the right statement may be:
    - "some selection satisfying (S) is nested", or
    - "every non-nested selection can be replaced by a nested one without losing (S), (C) or coverage of the target", or
    - "non-nestedness gives a cover nothing".
  - Find the true statement and prove it, or build a system in which non-nestedness is essential.
- **(R1) Mirrored simple pairs.**
  - Does a two-world nested system exist with every axiom, a non-null Z, and a uniformly Cesàro-thin family 𝒜 with Z ≤₁ A for all A ∈ 𝒜?
  - By N1 and MP-loop this is the same as c_{s0} ≤₁ A and d_{b0} ≤₂ A for all A ∈ 𝒜.
  - Construct one with every axiom verified (closed sections for EVERY model), or prove that none exists.
  - Proposition N2 says the mirrored pair alone gives no contradiction. A proof must therefore use closedness quantitatively, e.g. through a rate in Lemma T (R3), or the closedness test of Prop Q13 (a compact family of target profiles).

## RULES
- Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.
- Add no assumption to the framework.
- A construction counts only when every axiom is verified.
- If an attempt fails, write an honest failure report saying exactly where it failed.
- Write only your own note and scripts (in a subfolder named after the note), in /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/.
