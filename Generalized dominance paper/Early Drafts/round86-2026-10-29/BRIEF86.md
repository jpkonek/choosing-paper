# Round 86 brief: verification and two new drafts

Folder (write ONLY here): /tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r86/

**The binding instruction is GUIDANCE86.md** (the audit's "Guidance for two revised papers", 29 Oct). Follow it exactly.

The author has confirmed that the ordinary payoff score may be used instrumentally. It is used only in the application's construction, never as an LDG axiom.

## Sources (in this folder)
- **GUIDANCE86.md**: the guidance (binding).
- **AUDIT_fixed_countable.md**: the audit's completed construction with the fixed countable list.
- **AUDIT_countable.md**, **R85a_report.md**, **R85b_report.md**: the previous construction and its refereeing. Its steps are verified there.
- **ldg_short.tex**: the author's current LDG Short paper, the base for the LDG draft.
- **ldg_full.tex**: the full LDG paper, for reference only.
- **app_short.tex**: the author's current application Short paper, the base for notation and definitions.
- **app_long.tex**: the long application paper. Use it for the hull, identification, contraction and trimming lemmas, the guidance lemma for arbitrary worlds, and the measure-existence lemma.
- **ldg-references.bib**.

## The author's standing style rules
- Theorems, lemmas, propositions and corollaries are unnamed. Definitions and axioms may have short names in brackets.
- Use \coloneqq.
- Formal core only. Give an explicit definition of every technical notion and an explicit list of all assumptions. The only prose is a one-sentence plain-English gloss of each definition or assumption.
- No jargon. Avoid: certificate, record, gate, route, safe, dangerous, shelter, catalogue. Do not use historical project labels.
- No commentary comparing versions.
- Author line: exactly "Jason Konek". Do not invent bibliographic details.
- LDG uses a ⪯_ω x to mean "a performs at least as well as x". The application Short paper writes Y ⪰_ω X for "Y is at least as good". Use one convention per paper, consistently. Where the application cites LDG, say how the conventions correspond.

## Tasks

### VER86 (verifier)
Carry out the ten verification tasks in GUIDANCE86 §10, independently and line by line.
- Pay particular attention to the finite-inequality approximation and its margins.
- Check the hull-inclusion chain in §7 Step 2.
- Check both cases of the gap lemma, including dominated differentiation for arbitrary Ω.
- Check closedness of K_ω.
- Check the order of quantifiers.
- Check the U_L = C_L claim, and that it does not need coherent assigned models.
- Check the measure-existence lemma.
- Check the identification of almost coherence.

Output **VER86_report.md**. For each task give OK / GAP / ERROR, with a fix, and replacement text where it is short. Final message: under 250 words.

### WL86 (LDG writer)
Write **ldg_countable.tex**, titled "Coherence and Dominance under General Rankings". The deliverable is named in GUIDANCE86 §2; the lead renames it on copying.
- Follow GUIDANCE86 §3 exactly. Base it on ldg_short.tex: keep its setting, definitions and the KKM lemma and its proof.
- Replace the selection theorems and the dominance argument with the countable versions:
  - the general compact theorem, with no coherence assumption, then the finite-world specialisation;
  - the local tie condition, and the sufficient condition via C_L closed under ties;
  - the family-level argument with (E), (A), (S_σ) and (T_σ);
  - U_L = C_L;
  - the stronger conclusion when the assignments lie in C_L;
  - the paragraph on what changed;
  - the two short examples.
- Keep the literature applications (§8 of ldg_full / the applications insert) only if they remain accurate under the new conditions and fit within about 12 pages. If they don't fit, omit them and list them in the change log. Do not rewrite them.
- Length about 10–12 pages, 15 at most.
- Compile ldg_countable.pdf cleanly with pdflatex: no errors, no undefined references, no overfull boxes.
- Write WL86_changes.md.

### WA86 (application writer)
Write **app_ldg.tex**, titled "Coherence and accuracy for sets of desirable gambles". The deliverable is named in GUIDANCE86 §2.
- Follow GUIDANCE86 §§4–9 exactly:
  - the setting and scope;
  - the ranking and its elementary properties;
  - admissibility first;
  - the fixed assignments and the finite-inequality approximation lemma, with its correction;
  - selection verified directly in Steps 1–4;
  - the application of LDG's countable theorem, cited as a numbered result of the LDG draft. Coordinate numbering with WL86 by reading ldg_countable.tex when it exists. Otherwise cite by name and leave a clearly marked TODO for the lead;
  - the main theorem and its corollary;
  - the measure-existence lemma;
  - the limitations, in two sentences.
- Include complete proofs of every lemma used: hull, identification, contraction and trimming, and the guidance lemma for arbitrary worlds. Take them from app_long.tex and tighten them.
- Do not include consolidation, maximality, boxes, numerical work, the repair theorem, neighbourhood robustness or the countable-subcover argument.
- Length about 10–12 pages, 15 at most.
- Compile app_ldg.pdf cleanly.
- Write WA86_changes.md, listing anything you could not prove.

## All agents
- Labels: PROVED / CHECKED / GAP / ERROR.
- Write only in r86.
- Never modify the source files.
