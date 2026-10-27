# W64 — the covering paper: changes, sources and flags (25 Oct 2026)

Deliverables (all in `r64/`):
- `Covering coherent sets of desirable gambles (draft).tex` and `.pdf`. 38 pages. It compiles cleanly with pdflatex: no undefined references, no overfull boxes, no warnings.
- `w64py/`: the exact (Fraction) scripts used to re-check every computed example.
  - `hull.py`: hulls, facets and world types.
  - `n4_check.py`: Example 6.13. Runtime is about 45 s.
  - `n3_check.py`: Examples 5.11, 5.12 and 6.16, and the reversed triangle.

Labels:
- **PROVED-ref**: proved in a refereed source note, re-proved in the paper.
- **PROVED-W64**: the proof in the paper is W64's own write-up of a refereed result. The argument or its organisation is new, so a referee should read it.
- **CHECKED**: exact computation.
- **STATED**: recorded without proof.

## 1. Structure

| § | Content |
|---|---|
| 1 | Introduction |
| 2 | Framework. Gambles and credal sets; (M); domains $U$ and the model class $\M_U$; one-sided, essentially one-sided and full domains; global coherence; relations reflexive with a.e. ties and (TC); dominance nomenclature; requirements (G), (IB), (GC), (C), (ID), (LF); Definition 2.5 (cover); (W); Lemma 2.6 and Remark 2.7; §2.5 on what strict guidance alone forces |
| 3 | Two-level integral rankings: the general admissibility route (Theorem 3.7) |
| 4 | Veto–Brier rankings: family, covering theorem, exempt point, visibility, examples, near the reversed triangle, dense approximation |
| 5 | Orthant-planar targets: closed-orthant identity, pullback, ratio criterion, planarity obstruction, covering theorem, precise targets, boxes and density-ratio classes, three-world cevian characterisation, examples |
| 6 | Composition: conjugacy, covering theorem, reach, three-world limitation, Theorem F with the $[1,2]^4$ example, Theorem BE with the pentagon |
| 7 | Scoped exclusions: veto–Brier; vetoes then Brier-type error; further exclusions recorded without proof; composition; what the exclusions do not show |
| 8 | Open problems |

## 2. Framework changes (binding framework)

- **Relations.** The relations are reflexive, tie a.e.-equal models, and satisfy (TC). Transitivity and completeness are not assumed.
- **Requirements.** Definition 2.5 lists exactly the requirements of BRIEF64: (G); (IB); global coherence; direct (C); the target $D_K$ is a model and is undominated; incoherent-model dominance; (LF) at $D_K$. Decomposability holds automatically, because models are all measurable $X\subseteq U$.
- **Not required.** (W) is stated only as a stronger objective. The list of non-requirements in §2.4 includes transitivity and completeness.
- **What every construction satisfies.** Every construction is a two-level integral ranking with (SC), null ties and coherent minimisers. So it is score-generated, complete and transitive, and it gives (W) and the strong form of (C). This is stated in the intro, after Theorem 3.7, and in every covering theorem.
- **W62 Lemma `lem:dominance` (now Lemma 2.6).** The W62 proof used *transitivity*, not completeness, in its (C) step: $Z\preceq X\preceq Y\Rightarrow Z\preceq Y$, and $Z\prec X\preceq Y\Rightarrow Z\prec Y$. Its "by completeness" step is only the definition of $\prec$.
  - Rescoped. (a) If every model is weakly dominated by an undominated model and (GC) holds, then (W) holds. If direct (C) also holds, (ID) follows. Part (a) uses no property of the relations.
  - (b) If the relations are transitive, (GC) implies (C).
  - Remark 2.7 gives a three-model relational configuration that satisfies (TC) and in which (C) fails. So (C) must be listed separately.
- **Strict guidance alone (§2.5).** Lemma 2.8 (world-best model undominated), Theorem 2.9 (domain dichotomy) and Proposition 2.10 (lower-dimensional targets) use only (G) at single worlds. No (TC), (IB), transitivity or completeness is needed.
- **The admissibility route (§3) is now general.** It covers arbitrary domains and arbitrary integrands $\varphi_i\ge0,\psi_i$, under (SC) and null ties. Veto–Brier, chart and composed rankings are all instances. The proofs are W62 Lemmas 3.3–3.6 with $-h_i$ replaced by $\psi_i$.

## 3. Map of results to sources and referee reports

### 3.1 Veto–Brier coverage and the visibility class (§4; §7.1)

| Paper | Source | Referee | Status |
|---|---|---|---|
| Lemmas 2.1–2.3, 4.2, 4.5, 4.12, 4.13, 4.16; Theorems 4.4, 4.6, 4.9, 4.14; Corollaries 4.8, 4.15, 4.17–4.19, 4.25, 4.27; Propositions 4.21, 4.23, 4.24, 4.26, 4.28, 4.29 | W62 §§2–8 (P61 Thms A, B, V; O61 Thm C; E61 Prop 6.1) | REF61_pos; the impossibility referee (ROUND61 §§2–4) | PROVED-ref. Text as W62, adapted to §3 |
| Lemma 4.3 (VB satisfies (SC) and null ties; exact minimisers) | W62 Lemmas `unique` and `coh` | as above | PROVED-ref |
| Theorem 7.3 (VB targets in the open simplex are exactly "all but one extreme point uniformly visible"); Corollaries 7.4, 7.5; Lemma 7.1; Remark 7.2 | W62 §9 (P61 V6, I5; O61) | REF61; FD62 §6 rows 4–6 | PROVED-ref |
| Proposition 6.14 (VB face count: at most one extreme point of support exactly $S$) | W62 Prop `contamzero`, case $\|S\|\ge2$; REF63_comp §2.5 | REF63_comp R14 | PROVED-W64. Factored out of W62 so that Theorem BE can use it |
| Proposition 7.6 (contaminations with centre on $\partial\Delta$ are not VB targets, every zero pattern) | W62 Prop `contamzero` (P61 D3 with REF61 §2.6) | REF61 §2.6 | PROVED-ref |
| Smooth sets: the normal cone of a convex sublevel set | W62 cited Rockafellar Cor 23.7.1 | — | Replaced by a direct three-line argument; citation removed |

### 3.2 Orthant-planar coverage and boxes (§5)

| Paper | Source | Referee | Status |
|---|---|---|---|
| Definition 5.1; Lemma 5.2 (closed-orthant identity) | REF62_fd Prop R2 | REF62_R2 §3 (both inclusions) and row 11 ($d_\sigma\gg0$) | PROVED-ref |
| Lemma 5.3 (pullback $c(h)\in D_Q\iff h\in D_{Q\star K}$ on $O$) | RC63 §2.1 | RC63 row 1; REF63_comp R8 | PROVED-ref |
| Lemma 5.4 (ratio criterion: orthant-planar iff, on each mixed orthant, one point maximises all ratios $m_b/m_a$, $a\in P$, $b\in N$) | Implicit in FD62 §4.1 (boxes) and in CC63 Lemma A / REF62_R2 row 18 (deciding vertices) | — | PROVED-W64. New lemma. (a) is elementary; (b) is new. Needs refereeing |
| Lemma 5.5(a) (orthant-planar ⇒ polytope) | REF63_comp §2.4, proof of Lemma U | REF63_comp | PROVED-W64 (details written out) |
| Lemma 5.5(b)–(d) (planarity obstruction: a no-zero-coordinate normal exposing ≥2 points; edges cevian; facet normals not all nonzero) | CC63 Lemma O1; REF62_R2 §4 (necessity) | REF63_comp C2 | PROVED-W64. A different, self-contained proof |
| Theorem 5.7 (chart ranking covers $K$ on $\R^n$ and on $D_{K'}$, $K'\subseteq\relint K$; exact undominated family) | REF62_fd Prop R2; FD62 Prop FD-B | REF62_R2 rows 10–14 ((LF) needs $K'\subseteq\relint K$: done) | PROVED-ref, through §3 |
| Corollary 5.8 (Brier covers every precise interior target on the full domain; its undominated models are the precise models) | FD62 FD-1c; ROUND61 "precise targets" | REF62_fd row 7 | PROVED-W64. Immediate from Theorem 5.7 |
| Proposition 5.9 (boxes; concave chart $\min(l_jh_j,u_jh_j)$; density-ratio class $=\nu(p\odot[1,k]^n)$; criterion $E_ph^+>kE_ph^-$) | FD62 Prop FD-B | REF62_fd rows 10–11 | PROVED-ref |
| Theorem 5.10 (three worlds: orthant-planar polygon ⇔ every edge line cevian) | REF62_fd R2 "n = 3 geometry"; REF62_R2 §4; CC63 Lemma A (log coordinates) | REF62_R2 row 15 | PROVED-W64. Sufficiency goes through log coordinates and Lemma 5.4(a); necessity through Lemma 5.5(c) |
| Example 5.11 (cyclic triangle: orthant-planar, no visible vertex, not a box) | REF62_fd R2 examples; REF62_R2 row 18 | REF62_R2 | PROVED by hand in the text; CHECKED (`n3_check.py`) |
| Example 5.12 (non-box hexagon) | REF62_fd R2; REF62_R2 row 17 | REF62_R2 | CHECKED (`n3_check.py`). Labelled "(Exact computation.)" in the text |

### 3.3 Composition (§6; §7.4)

| Paper | Source | Referee | Status |
|---|---|---|---|
| Definition 6.1 (composed ranking); Lemma 6.2 (conjugacy: the ranking is VB$(L',A)$ under $\mu_c=c_\sharp\mu$); Theorem 6.3 (covers $L\star K_0$; exact undominated family $D_{K(W_0,\beta,\alpha)\star K_0}$; (LF)) | AUDIT_r62_composition §1; RC63 §§2.1, 2.7, 2.8 | RC63 (all steps CORRECT); REF63_comp R8 | PROVED-ref. Uses RC63's shorter proof through the pushed-forward measure |
| Lemma 6.4 (reach: extreme points come from extreme pairs) | AUDIT_r62 §1 "What to do"; RC63 §3.1 | RC63 row 11 | PROVED-ref |
| Lemma 6.5 (uniform visibility off $\nu(\pi^\ast\odot K_0)$) | REF63_comp §2.4 Lemma U; CC63 F3 | REF63_comp R13 | PROVED-ref |
| Lemma 6.6 (n = 3: not visible ⇔ $x\in M_i(S)$) | RC63 §3.3 Lemma N3 | RC63 row 16; REF63_comp R12 (scope: $M_i$ restricted to relint Δ; cross-multiplied form) | PROVED-W64. The sector argument is written out in full |
| Lemma 6.7 (decoupling) | RC63 §3.3 "Decoupling"; CC63 Lemma R | REF63_comp R12, C3 | PROVED-ref, in cross-multiplied form |
| **Theorem 6.8 (n = 3, $\pi^\ast$ interior: $\mathsf N(L\star K_0)=\mathsf N(L)\le1$; all other extreme points uniformly visible; so composition adds no interior three-world target)** | RC63 §3.4; REF63_comp §2.3 (equality) and §2.4 (Lemma U; any compact convex $L$) | REF63_comp R12+, R13 | PROVED-W64. Here $M_i(K_0)\ne\emptyset$ comes from Lemma 5.4(b) rather than CC63 Lemma A(iv), so it holds for $K_0$ of any dimension |
| Lemma 6.10 (two-pair rule) | CC63 Lemma TP | REF63_comp C3 | PROVED-ref |
| **Theorem 6.11 (Theorem F)** | CC63 §4.5 (with Theorem G §4.3 and Lemma NP §4.4) | REF63_comp C4–C6 | PROVED-W64. Hypothesis (F-d) is stated as "a facet normal of $L$ with no zero coordinate" and used with Lemma 5.5(d). CC63's version, "three or more nonzero coordinates", needs CC63 Lemma O1's facet part, which the paper does not include. This is a slight weakening of the stated hypothesis, but the explicit family satisfies the stronger form (REF63_comp §3.4) |
| Corollary 6.12 (the explicit family satisfies (L), (F) and the facet condition) | CC63 §4.5 "family"; REF63_comp §3.4 ("(F-d) automatic") | REF63_comp C6 | PROVED-ref |
| **Example 6.13 ($[1,2]^4$ box, $p_0=(4,3,2,1)/10$, $\varepsilon=1/20$)**: 32 vertices, 63 edges, 33 facets; five vertices visible from no world, all tangential; six facet normals with no zero coordinate | CC63 §4.6 | REF63_comp C7 | CHECKED. Re-run independently by W64 (`n4_check.py`): 32/63/33; five bad vertices AATT, ATAT, ATTA, ATTT, TATT; facet counts by nonzero coordinates 12/15/6. Theorem F accounts for four of the five |
| **Theorem 6.15 (Theorem BE)** | CC63 §5.1; RC63 §3.5 | REF63_comp C8 (with the wording repairs) | PROVED-W64. (c) uses Proposition 6.14. (d), "not orthant-planar", is definitional only, as REF63 notes |
| **Example 6.16 (three-world pentagon)** | RC63 §3.5; CC63 §3 | REF63_comp R14 | CHECKED (`n3_check.py`): five vertices as stated; three of the five facet normals have no zero coordinate (non-cevian edges); L's vertices have types CCS, CCC, ASC |
| Proposition 7.14 (not orthant-planar and no visible extreme point ⇒ never an undominated (LF) target of a composed ranking) | RC63 §3.2; REF63_comp §2.2 (general form) | REF63_comp R10 | PROVED-ref |
| Corollary 7.15 (pari-mutuel models, including the reversed triangle) | REF63_comp §2.2 | REF63_comp R10 | PROVED-W64. Not orthant-planar via Lemma 5.5(d) |
| Corollary 7.16 (two-cevian interior triangles: not VB, not orthant-planar, not composed with interior $\pi^\ast$) | CC63 §6 (vertex-region lemma) | REF63_comp C11 (interior only) | PROVED-W64 |
| **Proposition 7.17 (contaminations whose centre has exactly one zero are never $L\star K_0$)** | CC63 §5.2; REF63_comp §3.6 | REF63_comp C9 (scope: exactly one zero) | PROVED-W64. Dimension 0 is handled directly, not through P61 D3; dimension 1 by the face argument; dimension ≥ 2 by the cevian-edge argument (Lemma 5.5(c) and a standard vertex-degree fact, cited to Ziegler without a number). Scoped to exactly one zero coordinate, and the text says so |

### 3.4 Domains (§2.5)

| Paper | Source | Referee | Status |
|---|---|---|---|
| Lemma 2.8 (world-best model undominated under (G) alone) | FD62 Lemma W1 | REF62_fd row 2 | PROVED-ref |
| Theorem 2.9 (domain dichotomy) | FD62 Thm FD-1 | REF62_fd row 4. Uses its strengthening: only the $n$ world-best models need be coherent | PROVED-ref |
| Proposition 2.10 (lower-dimensional targets need a domain that is not essentially one-sided; under (GC) and n ≥ 3, essentially the full domain) | W62 Prop `lowdim`; P61 D1; O61 Rem 1.1; FD62 FD-1c | REF62_fd row 7 ((LF) named: done) | PROVED-W64. Generalised from $U=D_{K'}$ to any domain |

### 3.5 Exclusions (§7)

| Paper | Class excluded | Source | Referee | Status |
|---|---|---|---|---|
| §7.1 (Theorem 7.3, Corollaries 7.4, 7.5, Proposition 7.6) | VB-type: two-level sublinear veto then Brier, on open convex one-sided domains | W62 §9; P61 | REF61 | PROVED-ref |
| Lemmas 7.8–7.11, Theorem 7.12, Corollary 7.13 | $\mathcal V_{\rm B}$: complete lexicographic, measurable vetoes, then a Brier-type error with a common weight $w$, on one-sided domains with (LF) | O61 Lemmas 1–4 and Thm A | ROUND61 §3 (impossibility referee CORRECT); FD62 §4.3 item 8 for scope | PROVED-ref; proofs reproduced. Corollary 7.13 (every PMM vertex invisible, any $n\ge3$) is PROVED-W64 from the generators (FD62 §4.2 general rule) |
| §7.3 item (1) | Convex error levels: reversed triangle and every interior PMM triangle | O61 Thm B; REF62_R2 row 24 (upgrade) | ROUND61; REF62_R2 | STATED |
| §7.3 item (2) | Concave charts within finite-view unanimity with convex vetoes | E61 Cor 5.2 | ROUND61 §3 | STATED |
| §7.3 item (3), first part | Regular single charts ((DF), (ND) at $\pi^\ast$) | R15 Thm 1; A62 Cor 2.3 | ROUND62 §1.4 ("within R15's regular class … CHECKED") | STATED |
| §7.3 item (3), second part | Full-domain regular certificate charts ⇒ orthant-planar | REF62_fd Thm R1(a)–(b) | REF62_R2 rows 1–9 | STATED |
| §7.3 item (4) | Continuous piecewise-linear charts, any one-sided $U$ | C62 Thm 4.1 | REF62_corner (repair to Lemma 4.3) | STATED |
| §7.3 item (5) | Direction-continuous piecewise-linear charts, with (C2) at $\pi^\ast$ | DC63 Thm DC | REF63_neg §1 (GAP repaired by adding (C2) at $u=\pi^\ast$) | STATED, with (C2) at $\pi^\ast$ named |
| §7.3 item (6) | Finite unanimity with concave, or convex-veto then concave, views | IN63 Thm C | REF63_neg §0.3 | STATED |
| §7.4 | Composition | see §3.3 | | PROVED |

The section says each exclusion concerns its construction class, and §7.5 says the universal question is open. It does not say that pari-mutuel models are impermissible.

## 4. Citations

**Verified online.**
- Rockafellar, Thm 11.6: a non-trivial supporting hyperplane to $C$ containing a convex $D$ exists iff $D\cap\operatorname{ri}C=\emptyset$. Confirmed by arXiv:1905.08157, which cites it in exactly this sense.
- Schrijver, Cor 7.1h (affine Farkas lemma) and Cor 7.1a (Farkas–Minkowski–Weyl). Confirmed by arXiv:2307.13318, which cites both in these senses.

**Not verified** (searched; no source quoting the number was found). The numbers are kept from my knowledge of the standard 1970 and 1986 editions:
- Rockafellar Thm 6.3 ($\operatorname{ri}(\operatorname{cl}C)=\operatorname{ri}C$);
- Rockafellar Thm 11.3 (proper separation iff the relative interiors are disjoint);
- Rockafellar Thm 13.2 (support functions are exactly the closed proper positively homogeneous convex functions);
- Schrijver §8.5 ("Minimal faces and vertices").

**Removed.** Rockafellar Cor 23.7.1, replaced by a direct argument.

**Added.** Ziegler, *Lectures on Polytopes*, cited without a theorem number, for "each vertex of a $d$-polytope lies on at least $d$ edges with independent directions".

Lyapunov, Lindenstrauss, Shapley, Ichiishi, Shafer and Walley are as in W62 and were not re-checked.

## 5. Flags (could not verify, or need attention)

1. **§7.3 is recorded without proof.** Items (1)–(6) are refereed in the source notes, but the proofs are long (O61 Thm B, E61 Cor 5.2, R15/A62, REF62 R1, C62 Thm 4.1, DC63, IN63 Thm C). A journal version must either include them or cite them as published papers. The hypotheses are compressed from the notes. The compressed statements of item (3) (R15's (SH), (DF), (ND)) and item (2) (E61 Thm 5.1's architecture) in particular should be checked against the sources.
2. **"One-sided" in Theorem 7.12.** The domain is kept one-sided, as in O61. In the set formalism the proof does not appear to use one-sidedness. I did not drop the hypothesis, because the referee checked it as stated.
3. **New write-ups that need a referee:**
   - Lemma 5.4 (ratio criterion, especially (b));
   - Lemma 5.5 (planarity obstruction);
   - Theorem 5.10 (sufficiency proof);
   - Lemma 6.6 (sector proof);
   - Theorem 6.8 (proof route);
   - Theorem 6.11 (F-d) in its "no zero coordinate" form;
   - Theorem 6.15 as organised;
   - Propositions 6.14 and 7.17;
   - Corollaries 7.13 and 7.16;
   - Proposition 2.10 (generalisation).

   Each re-proves a refereed statement (or a trivial corollary of one), but the text is new.
4. **Remark 6.9 and open problem (5)** say the two-term criterion is not necessary in $n\ge4$. That rests on CC63 §4.7's gap example (CHECKED; REF63_comp C14), which I did not reproduce. The text labels it "an exact computation on an example".
5. **The KL-ball example** (end of §4.3) needs $G$ to be extended to a convex differentiable function on a neighbourhood. The text says so briefly. A referee may want a sentence more.
6. **Theorem BE (d)** is only definitional (the target meets $\partial\Delta$). REF63's general three-world non-cevian-edge proof is not included. The pentagon's three non-cevian edges are computed.
7. **Not included** (out of brief scope, or superseded):
   - F61 Thm D, which gives relative coherence only;
   - E61 Cor 5.3 (target-neutral vetoes with finitely additive levels);
   - IN63 Theorem S and the cap analysis (Conjecture 7.2);
   - REF62_R2's continuous non-box chart;
   - the box holonomy criterion. The paper uses only the necessary direction, as the product test in Example 5.11.
8. **The authors on the title page** are kept from W62: Konek and Campbell-Moore.

---

# Revision (25 Oct 2026, after REF64_paper and REF64_pc)

The revised `.tex` and PDF replace the earlier files under the same name.
- 43 pages.
- pdflatex compiles cleanly: no warnings, no undefined references, no overfull boxes.
- The author block is unchanged.
- New exact script: `w64py/t_check.py`. It covers Example 6.7: facets, world types, the barycentric coordinates of k, q = (10/11)k + (1/11)e₃, ν(6,2,2) = s, and k·r > 0 on the extreme rays.

## R1. Renumbering

- A new §6, "Veto–box rankings", is inserted between orthant-planar (§5) and composition (now §7).
  - It is placed after §5 rather than before it, because its triangle corollary uses the box geometry and Theorem 5.10.
- Old §6 becomes §7, old §7 becomes §8, and old §8 becomes §9.
- Old → new numbers:
  - Theorem 6.3 → 7.3; Theorem 6.8 → 7.8; Theorem 6.11 (F) → 7.12; Example 6.13 → 7.14.
  - Proposition 6.14 → 7.15; Theorem 6.15 (BE) → 7.16; Example 6.16 → 7.17.
  - Theorem 7.3 → 8.3; Theorem 7.12 → 8.12; Proposition 7.17 → 8.17.

## R2. REF64_paper required changes, in ranked order

| # | Required change | Done |
|---|---|---|
| 1(a) | §8.3 item (6) | Restricted to an open convex one-sided cone U ⊇ C_R∖{0} with no nonzero h ≤ 0, with concave gains on U. "Jointly strictly guiding" is defined as (SG): for each j, a.e. on {h_j ≠ 0} some view at j has a nonzero integrand |
| 1(b) | Item (2) | The veto is convex and −σ_v is concave on an open convex set containing C_R∖{0}. Further levels are allowed. Domain: any one-sided domain with (LF), as in E61 Thm 5.1 |
| 1(c) | Items (4)–(5) | "Domain" is now "open convex cone U ⊇ C_R∖{0} containing no nonzero h ≤ 0". Item (5) is stated at full strength: an arbitrary positive measurable scale, direction linear on each cone and continuous, with (C2) at π\* kept |
| 1(d) | Item (3) | "R is not orthant-planar" now cites Lemma 5.5(d), and "two-sided" is now "not essentially one-sided" |
| 1(e) | Preamble | Now says "items (3)–(5)", and π ∈ ℝ³₊∖{0} is written in (C2) and (C3) |
| 1(f) | Proof status | The heading stays "recorded without proof". The preamble now says the results are established "in unpublished notes". The abstract no longer says "provably fail": exclusions are proved for VB, vetoes-then-Brier-type and composition, and "recorded without proof" for the rest |
| 2 | Remark 2.7 | Reworded as the referee suggested. The configuration concerns abstract relations, is not a ranking on 𝓜_U, and need not satisfy (G) or (IB). We say we do not know whether (G)+(IB)+(TC)+(GC) imply (C), and that this is why (C) is a requirement. The optional record-level witness from REF64_or is not added |
| 3 | Remark 6.9 (now 7.10) and open problem (5) | The unsupported claim is removed. 7.10 says "we do not know whether it is necessary there". Open problem (5) asks for a decision on necessity. The CC63 §4.7 data were not available in full, so the example is not given |
| 4 | Theorem 6.15(d) (now 7.16(d)) | Replaced by a substantive statement with its hypothesis: *if n = 3 and K is a polygon, some edge line of K is non-cevian*. Full proof given (REF63_comp §3.6's argument, written out). Example 7.17 now cites it |
| 5(a) | Intro, n = 3 composition | Now reads: "every target of the form L⋆K₀ of Theorem 7.3 that lies inside the open simplex is already a veto–Brier target". The abstract was changed to match |
| 5(b) | Theorem 2.9(b) wording | The intro and abstract now say "contains every gamble that is not a sure loss". Open problem (7) was reworded to match. Theorem 2.9's proof gains a three-case summary sentence |
| 6 | (M) versus Lebesgue measure | Added after (M): the requirements depend on μ only through its null sets; (M) only makes the scores finite; a ranking built with (M) is a ranking in the framework's sense for Lebesgue measure or any positive density |
| 7 | Notation | "Anti-visible" and "crossing" are now defined in Definition 4.11(b). The box face in Theorem 7.12's proof is renamed G_x. The `=:` is now `\eqqcolon` (Proposition 4.21). Proposition 2.10's sentence is rewritten (coordinates h_a ≥ 0 and h_b ≤ 0 with a ≠ b, then h + t(e_a − e_b) ∈ M). The Proposition 7.17 typo disappears in the rewrite (R4) |
| 8 | Small hypotheses | Corollary 8.5(c) now says "full-dimensional". Theorem 8.12's last sentence derives full-dimensionality from Proposition 2.10. The abstract says "open convex one-sided cones containing the positive orthant". The KL paragraph now names V, an open convex set containing the sublevel set, with V = relint Δ for KL. Theorem 3.7(e) now cites only Lemma 2.6(a). The box paragraph after Proposition 5.9 now requires a lower-bound coordinate and full-dimensionality |
| 9 | Optional strengthening of the contamination exclusion | **Done.** See R4 |
| 10 | Optional (TP) remark | Not done, pending REF64_or |
| 11 | Second author | Left unchanged, as instructed |

## R3. Citations

- Kept as confirmed: Rockafellar Thm 11.6; Schrijver Cor 7.1a and 7.1h.
- Each unconfirmed number now carries the LaTeX comment `% citation number to be verified`. These are:
  - Rockafellar Thm 6.3 (Lemma 2.3);
  - Rockafellar Thm 11.3 (Lemma 3.5 and Lemma 4.13);
  - Rockafellar Thm 13.2 (Lemma 8.1);
  - Schrijver §8.5 (Corollary 8.5).
- Ziegler is still cited without a number.

## R4. Strengthened contamination exclusion (Proposition 8.17)

The proposition now says: for p with exactly one zero coordinate, D_K is not an undominated model of *any* composed ranking. That holds for any orthant-planar K₀ of any dimension and any L′, A as in (L), and needs no (LF). In particular K ≠ L⋆K₀. This is the referee's sketch, carried out.
- Write K = Q⋆K₀ with Q = K(W₀,β,α).
- **Dimension 0.** Q ∩ Δ_{Ω∖{k}} = T_{p₀}⁻¹(face) has n − 1 ≥ 2 extreme points of support Ω∖{k}. This contradicts Proposition 7.15, with K″ = L′.
- **Dimension 1.** The face of K equals T_{m′}(Q ∩ Δ_{Ω∖{k}}), giving the same contradiction.
- **Dimension ≥ 2.** As before: the cevian-edge argument, now with q ∈ ext Q.
- The scope is still exactly one zero coordinate. The text keeps the sentence that two or more zeros are not treated.

**Status:** PROVED-W64. A referee should read it.

## R5. New positive theorem: veto–box rankings (§6)

| Paper | Source | Referee | Notes |
|---|---|---|---|
| Definition 6.1; Lemma 6.2 (box chart: concave, sign-correct, \|c_j\| ≤ u_j\|h_j\|, c_j(h + t𝟙) ≥ c_j(h) + t l_j, Σβ_j c_j = min_{ρ∈R}(β⊙ρ)·h) | PC64 §2.1, Lemma BX1 | REF64_pc §A, §B | PROVED |
| **Lemma 6.3 ((SC), null ties, coherent minimisers)** | PC64 BX3, BX4 | REF64_pc §B.2–3 | PROVED |
| **Theorem 6.4 (Theorem BX: one exempt normalised box, possibly degenerate, β possibly on ∂Δ, any n)** | PC64 Theorem BX | REF64_pc row 3 (CORRECT) | PROVED |
| Lemma 6.5 (box geometry) | PC64 §2.3 remarks; PC64 BX3 step 4; REF64_pc §B.6 | REF64_pc | PROVED-W64 |
| **Corollary 6.6 (BX3: veto–box targets among interior triangles are exactly V ∪ X)** | PC64 Cor BX3 | REF64_pc row 4 (CORRECT, scoped to VBox on 𝓜_{D_{K′}}) | PROVED. Stated with the referee's scope: (i) VBox(K′,B,R) on 𝓜_{D_{K′}} with D_T undominated and (LF); (ii) covered by such a ranking; (iii) V or X |
| **Example 6.7 (T = conv{(1,2,2), (2,1,2), (3,1,1)}/5)** | PC64 §§1, 2.4 | REF64_pc rows 1, 2a–2f | PROVED in the text, and CHECKED by `w64py/t_check.py` |
| **Corollary 7.9 (reach of this paper's constructions on interior triangles = V ∪ X ∪ all-cevian)** | REF64_pc row 8, the "nearby PROVED statement" | REF64_pc | PROVED-W64 |

Details:
- **Lemma 6.3.**
  - *Uniqueness* uses only β·l > 0, through g(h + t𝟙) ≤ g(h) − tβ·l and Lemma 3.8. So boundary priors are covered, as the referee notes.
  - *Coherence* uses the referee's formulation: g = max_{w∈W}(−w·h) with W compact, w ≥ 0 and 𝟙·w ≥ β·l > 0. The incomplete "convex veto + concave chart" reason is not used, and the paper says explicitly what the coherence step uses.
- **Theorem 6.4.** The proof goes through the general route of §3. The paper notes that it contains Theorem 4.9 (R a point) and the one-sided box coverage of Proposition 5.9.
- **Lemma 6.5.** It has three parts: (a) ν(R′) = {m : l′_i m_j ≤ u′_j m_i}; (b) every cevian segment in relint Δ is a degenerate box; (c) in n = 3, edges are cevian, one-dimensional boxes lie on cevian lines, and no normalised box is a triangle. Part (c) has a full log-coordinate proof: each vertex of a putative triangle forces one coordinate to be degenerate.
- **Corollary 6.6.** The proof of (i) ⇒ (iii) follows PC64 steps 1–5, with step 5 split by the dimension of the box.
- **Example 6.7.** It includes:
  - the facets (2,2,−3), (0,−1,1), (−1,4,−1);
  - vertex types ACC, CAS, TCC, read off Lemma 4.16;
  - k = (22,11,17)/50 = p/10 + 3q/5 + 3s/10;
  - q = (10/11)k + (1/11)e₃;
  - R = [1,6]×{2}×{2}, so ν(R) = [p,s];
  - the ranking table and the domain {22h₁ + 11h₂ + 17h₃ > 0}.
  - Short scoped exclusions only: not orthant-planar (Theorem 5.10), not a VB target (Corollary 8.4), not L⋆K₀ with interior π\* (Theorem 7.8). The concave-chart, piecewise-linear and 𝒱_B exclusions for T are omitted as not short.
- **Corollary 7.9.**
  - Orthant-diagonal chart targets with (LF) are ν(π⊙K₀), which is orthant-planar.
  - Interior composed targets L⋆K₀ need π\* interior; then Theorem 7.8 applies.
  - VB and veto–box targets come from Corollary 6.6.
- **Not included:** the census percentages; Lemma CM; the first-order direction systems; the 𝒱_B exclusion for T.

## R6. Scope corrections from REF64_pc

- **§8.3 item (1) (convex error levels).** It now applies to R and the interior pari-mutuel triangles, because the collar mechanism reaches all three faces and the extreme-ray system is nonsingular. It also applies to polytopes in relint Δ₃ with two or more vertices at which every world is crossing. The text does not call the pari-mutuel vertices "all-crossing". It also says the conclusion does not extend to all targets with two non-visible vertices, because Example 6.7's cover is a veto followed by a convex error level.
- **Open problem (4), the three-world characterisation.** The brief called this "(7)"; in the paper it is item (4). Item (7), on two-sided domains, was also reworded (R2 5(b)).
  - It now says that VB ∪ orthant-planar is refuted by Example 6.7.
  - It states the proved nearby statement (Corollary 7.9).
  - It states the replacement conjecture: an interior triangle is covered iff every edge joining two non-visible vertices is cevian. It carries the referee's caveat: the "only if" half implies that the reversed triangle is not covered, so the conjecture is strictly stronger than open problem (1).
  - Test cases: two class-N triangles. One is conv{(1,6,1)/8, (6,1,3)/10, (6,1,1)/8}; the other is CC63's two-cevian triangle conv{(6,4,1)/11, (6,1,3)/10, (6,1,1)/8}. Both were classified exactly: in each, the two bad vertices are joined by a non-cevian edge.
- **Corollary 8.16 (two-cevian triangles).** It is unchanged and still true. A following sentence notes that a two-cevian triangle whose two bad vertices are joined by a cevian edge is a veto–box target.
- **Census percentages:** not included.

## R7. Remaining flags

1. §8.3 is still recorded without proof, now attributed to unpublished notes.
2. New W64 write-ups that need a referee:
   - Theorem 7.16(d);
   - Proposition 8.17 (strengthened);
   - Lemma 6.5;
   - Corollary 7.9;
   - the wording of Corollary 6.6's proof.
3. Theorem BX itself is refereed once (REF64_pc). REF64_pc recommends a second refereeing before it is listed with the positive theorems. It is included here as the coordinator instructed.
4. The (TP) note (REF64_paper optional item 10) is deferred until REF64_or's verdict.

---

# Revision 2 (25 Oct 2026, after REF64_bx)

The revised `.tex` and PDF replace the earlier files under the same name. The PDF is 44 pages. pdflatex compiles cleanly: no warnings, no undefined references, no overfull boxes.

## REF64_bx required changes

| # | Change | Done |
|---|---|---|
| 1 | §8.3 item (1) omitted (G); the sentence was false without it | The class now reads "…then any further levels, and that satisfy (G), on a one-sided domain…". It also notes that Lemma 8.11's proof uses only Lemmas 8.8–8.10, which hold for any ranking of this kind with (G) (optional 6g) |
| 2 | Introduction, item (3) | Now reads "every interior triangle with **exactly** two non-visible vertices joined by such an edge" |
| 3 | Corollary 7.9, chart-ranking step | Replaced by the referee's domain-free argument, stated as a new **Lemma 5.8**. On any domain U, if D_K is an undominated (LF) model of a chart ranking for orthant-planar K₀ and K is a polytope, then K = ν(π⊙K₀). If K ⊆ relint Δ, K is orthant-planar. The proof uses Theorem 3.7(c) and Lemma 5.3, gives E ⊆ K, and shows that an exposed vertex outside E would contradict (LF). Corollary 7.9 now says "a chart ranking of an orthant-planar credal set **on any domain**" and cites Lemma 5.8 |
| 4 | Open problem (4) | The reach sentence now says "in the sense of Corollary 7.9 (in particular, with composition restricted to targets of the form L⋆K₀)". It adds "the 'if' half holds by Corollary 7.9, so the content of the conjecture is its 'only if' half". "Strictly stronger" is replaced by "proving the conjecture would settle the simplest open case of problem (1), negatively" |
| 5 | §8.5 scope | Re-scoped. The reversed triangle lies in the scope of every exclusion. For other pari-mutuel models, the paper lists the exclusions that apply: Corollary 8.5(a), Theorem 8.12 with Corollary 8.13, Corollaries 8.15 and 8.16, and §8.3 item (1) for triangles in relint Δ₃. A ranking covering another pari-mutuel model would have to lie outside the classes whose exclusions apply to it |
| 5′ | The referee's corollary on pari-mutuel models, any n ≥ 3 | **Added** as Corollary 8.16, because its proof is complete as given. No pari-mutuel model K ⊆ relint Δ is an undominated (LF) model of a veto–box ranking on some 𝓜_{D_{K′}}, or of a chart ranking of an orthant-planar credal set on any domain |

The proof of Corollary 8.16:
- **Veto–box case.** The steps of Corollary 6.6 (i)⇒(iii) that do not use n = 3 give K = E, a normalised box with β ≫ 0. A box is orthant-planar (Proposition 5.9). Pari-mutuel facet normals have no zero coordinate (Lemma 5.5(d)), which gives the contradiction.
- **Chart case.** Lemma 5.8, and the same contradiction.

§8.4 is renamed "Composition, veto–box and chart rankings".

## Polish (change 6)

| | Change |
|---|---|
| (a) | After Lemma 6.3: "a maximum of −w·h over a compact W ⊆ ℝⁿ₊ with 𝟙·w > 0 on W". Compactness gives an attained maximum and a compact ν(W) |
| (b) | After Theorem 6.4: when β has zeros, ν(β⊙R) is a normalised box of the face Δ_{supp β}, and the vertex e_j when supp β = {j} |
| (c) | Proof of Corollary 6.6: "here t < 1, because x ∈ relint Δ" |
| (d) | Example 6.7, last sentence: T is not of the form L⋆K₀ with (L) at all, since T ⊆ relint Δ forces π\* ∈ relint Δ, and then Theorem 7.8 applies |
| (e) | Theorem 7.16(d): K is a polygon whenever L is, by Lemma 5.5(a) and Lemma 7.4 |
| (f) | Proposition 8.18: the tangent cone is renamed 𝒯 |
| (g) | As in change 1 |

## Numbering

- The new Lemma 5.8 shifts later §5 numbers by one. Corollary 5.8 (precise targets) is now 5.9, Proposition 5.9 is 5.10, and so on.
- The new Corollary 8.16 shifts the two-cevian corollary to 8.17 and the contamination proposition to 8.18.
- The cross-references in the table above use the new numbers.

## Status

- Lemma 5.8 and Corollary 8.16 are the referee's arguments (REF64_bx §2 and §5.4), written out by W64. Each has been checked once, by REF64_bx.
- The earlier flags in R7 are unchanged.
