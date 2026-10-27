# Terminology correction, 14 October 2026

The author's correction. A gamble f represents the binary choice {f, 0}, equivalently {g, h} for any g, h with f = g − h. A domain restriction is only a restriction on the class of evaluable models; no decision problem is removed, altered or given restricted options.

On the U-domain the evaluable models are the measurable subsets D of U = D_{K′}. Evaluable models are guaranteed to agree on the choice represented by f (all giving no advice) only when **f ∉ U and −f ∉ U**. If −f ∈ U, they may differ: some accept −f, some do not.

## What was changed

All 75 Markdown and LaTeX files that used the old wording were corrected, in both the dominance-paper folder and `CPMs/outputs`.
- **Old to new wording:**
  - "menu domain" becomes "decomposable domain" (a class of evaluable models closed under splicing and under limits in measure);
  - "menu" becomes "advice range" (the kinds of advice that evaluable models give on a choice);
  - "accept-or-silence domain" becomes "U-domain";
  - "three-action menus" becomes "two-sided domains" (advice range {+, 0, −});
  - "forced silence" becomes "every evaluable model gives no advice on that choice";
  - "forced acceptance" becomes "every evaluable model accepts f".
- **Where the old text said "forced silence outside X",** the new text says which pairs are meant: pairs {f, −f} with f ∉ X and −f ∉ X.
- **What was not changed:** no mathematical statement, hypothesis, status label or proof. LaTeX labels are unchanged. Files and folders whose names contained "Menu Domains" were renamed later the same day (see below).
- **The author's LaTeX documents:** in *Domain Closure and Extendability* and *Closed Choice from Interior Bayes Uniqueness*, every changed passage is marked in red, and both were recompiled.
- **The auditor's three Assessment files** received minimal wording changes and a header line saying so.
- **Originals:** the pre-correction versions are in `_archive/terminology-fix-2026-10-14-originals.zip`.

## Does anything depend on the false claim? (AUDIT_fU.md, in `decomposable-domains-2026-10-12/`)

The audit covered the write-up and the load-bearing notes: N9, N12, N13, N15, N17, N19, N22, N24, N25, N26 (with its scripts), N27, R1, R11 and CCIBU. No proof uses "evaluable models agree on f because f ∉ U". Every argument on the U-domain treats a model as a subset of U and indexes each pair by its orientation in U. That covers the charts, the Bayes models, the error sets, the weights and the integrals.

This matters, because the part of U with a negative first coordinate is not small. For T1 it is about a quarter of U, and it contains the whole facet F₁ and the box witness used in the main theorem. The two-world construction (N26.1) handles both orientations; an independent script confirms this (`audit_fU_py/orientation_check.py`).

Slips found and repaired, none affecting a result:
- **The write-up:**
  - the error encoding and the vectors c_i in the (CP-a) part were written as functions on H; they are now written as functions on U;
  - the set N_i is now stated explicitly;
  - the proof sketch of the two-world theorem now spells out both orientations.
- **The R6 referee report, §4 Remark (ii),** had a parenthetical that was false on the U-domain for h ∉ U with −h ∈ U. A dated correction now says so; no theorem uses that remark.
- **The R12 referee report** had "forced silence elsewhere" in its restatement of Theorem M, which was false for g with −g ∈ V. It now reads as the U-domain with U = V.
- **N22 and N24** build models by choosing advice pointwise. This is legitimate because every measurable choice from the advice ranges is evaluable (Domain Closure and Extendability, Prop. 2).

## Renaming (14 October, 13:15)

At the author's request, files and folders whose names contained "Menu Domain(s)" were renamed, and every reference to them in the Markdown, LaTeX and Python files was updated:
- `menu-domains-2026-10-12/` → `decomposable-domains-2026-10-12/`
- `Coverage on Menu Domains - Round Report 2026-10-12.md` → `Coverage on Decomposable Domains - Round Report 2026-10-12.md`
- `Consolidated Statements - Menu Domains 2026-10-12.md` → `Consolidated Statements - Decomposable Domains 2026-10-12.md`
- `CPMs/outputs/menu-domain-audit/` → `CPMs/outputs/decomposable-domain-audit/`
- `Assessment of Menu Domain Results 2026-10-12.md` → `Assessment of Decomposable Domain Results 2026-10-12.md`

The archive of originals (`_archive/`) was left as it is.
