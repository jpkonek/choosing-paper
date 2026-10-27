# Audit of imported assumptions, 12 October 2026 (revised 15:50)

**Notation.** From here on:
- the vacuous model is **D_Δ**, not V;
- a ranking's evaluation domain is **M_L**, as in LDG v2;
- when a domain consists of the rules whose acceptances lie (a.e.) in a set of gambles, that set is **U_L**;
- D_i is the ideal model at world i;
- a coherent model D_K has credal set K.

The audit tables in `audit-2026-10-12/` predate this convention and use V for both the vacuous model and
the v19 domain cone.

Scope: every written note in this folder from v3 onward, the LDG v2 appendix, and the CPM-folder notes
`LSP_CPMs_v19b.tex`, `truth_directed_losses.tex` (TDL), `nonadditive_losses.tex` (NAL),
`FAMILY_LATITUDE.tex`, `CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md`. Permitted assumptions: (G), (IB), (E),
(LA), (A), (S), (C) of LDG v2 §2 and v3 §1, with the agreed weakenings (the exception for D_Δ and the Σ_T
systems). The line-by-line tables in `audit-2026-10-12/` (AUDIT_A: collaborator-lineage notes; AUDIT_B:
the CCT-session notes; OVERLAP: rediscovery check) come from AI audit passes and have not been refereed.
Items marked *checked* I verified directly.

## 1. The main imported assumption: every ranking evaluates every measurable model

LDG v2 gives each ranking its own evaluation domain M_L, and (S) asks for competitiveness only against
models in M_L. Nothing requires M_L to contain every measurable model. Nothing requires M_L to have any
particular shape either: not a cone domain, not a convex one.

The all-models requirement entered as a property of constructions. v3 line 145 says "All rankings
constructed below evaluate every measurable model". It then became a standing hypothesis:
- *Stated:* v3 `thm:additive-obstruction`; CCIR `thm:regular` and `thm:continuous`; BA `thm:extension`;
  VT's first proposition; START HERE ("The constructions discussed here evaluate all measurable models").
- *Implicit:* every proof that builds a far-away competitor, in CCF, ECS, IC, DT, TAW, FSE, FFN, TCR,
  CRANW and IRC.

Every obstruction in the programme uses at some step a competitor that a restricted domain need not
contain. The usual ones:
- the ideal models D_i;
- edge models and face models;
- gambles positive on a face but very negative elsewhere (the face lemma: v3 `lem:bayes-necessary`(c),
  CCIR `lem:face`);
- contradictory advice;
- the everywhere-contradictory model.

The audit tables test the special case of v19-type domains (rules inside a proper open convex cone U_L).
Even there, for full-dimensional targets, no obstruction applies as proved. With arbitrary domains, which
is all LDG requires, still less transfers: a domain need not contain any of these competitors. Whether the
conclusions of the obstructions still hold is open.

**Survives with mechanical repair:**
- the simplex/KKM lemmas;
- the order-algebra layer: the counting lemma, the chain lemma, finite cancellation (IRC Thm NC), the group
  primary, leverage;
- the exact consistency test (CANA `thm:closure`), with "every model" read as "every model in M_L";
- LRCF `thm:general`, if the family lies in M_L.

**Holds in any domain containing the relevant near-vertex cones:**
- TDL `thm:obstruction` (truth-directed losses with vanishing exchange rates);
- CSE's proposition that D_Δ is dominated when two worlds seek truth.

**Other non-axiomatic assumptions** were all stated explicitly in their notes:
- completeness (the P1 notes);
- additive, finitely additive or one-sided extension hypotheses (CCIR, CBOI, EDL, BA, TAW);
- the endpoint property, T1°, and the debt/credit pair conditions (CCF, FSE, IRC);
- Bayes choice (v3 `thm:general`, sufficient only).

## 2. Non-tangency: what it is for, and a formulation for arbitrary domains

**Purpose (author, 12 Oct).** The aim is to rule out cheap realisation. The model case is v19 with domain
cone = int D and φ = identity: the target is vindicated only because every model that would make a
borderline judgement differently has been removed from the domain. Tangency in limit cases is acceptable
if it does not make realisation cheap.

**Withdrawn.** The earlier version of this note claimed two things:
- "C_L ⊆ int M_L" forces the all-models case;
- lower-dimensional targets need all-model domains.

Both assumed that the domain is the set of rules inside a proper open convex cone. That assumption is not
forced and is dropped.

**Proposed condition (LF), local freedom at the target.** L vindicates a coherent target D non-cheaply if:
- D ∈ C_L; and
- for some open set N ⊆ ℝⁿ containing ∂D \ {0}, every measurable rule R with R △ D ⊆ N (mod null) belongs
  to M_L.

In words: the ranking must let the target compete with every model that disagrees with it only about
gambles near the edge of its acceptance region. Cheapness is shielding exactly those borderline
judgements from competition.

*Checked:*
- v19 non-tangency (cl D \ {0} ⊆ U_L, U_L open) implies (LF): take N = U_L.
- The cheap case (U_L = int D) fails (LF): adding a small set of gambles just outside D near ∂D leaves the
  domain.
- (LF) assumes nothing about the shape of M_L. For a lower-dimensional K, (LF) can hold in proper
  domains, for example with U_L an open but non-convex neighbourhood of cl D \ {0}.

**Two facts about where (LF) is imposed (*checked*).**
1. **Local face lemma.** Suppose the selection C_p = D_{K_p} at a prior with support S ≠ Ω satisfies (LF).
   Then K_p ⊆ Δ_S.
   - Otherwise put t = min over K_p of m(S)/m(S^c) (over m with m(S^c) > 0) and h = 1_S − t·1_{S^c}.
     Then h ≠ 0, h_S > 0 and P_{K_p}(h) = 0.
   - Gambles near h − ε·1_{S^c} are S-unanimous and rejected by C_p, and C_p is silent on them because
     P_{K_p}(−g) < 0.
   - Adding a small open set A of them changes C_p only inside N. That is a strict guidance improvement at
     every world of S, so C_p is not competitive on S.
   - So imposing (LF) on boundary-prior selections brings back face-respecting selections, and precise
     ideals D_i at the vertices. The far-away competitors used by the old obstructions still do not
     return.
2. **Vertex condition on domains.** Competitiveness at δ_i plus strict (G) means C_{δ_i} admits no strict
   guidance improvement at world i inside M_L.
   - For a domain of rules inside U_L, the pointwise best model at world i is U_L ∩ D_i (mod null). So
     U_L ∩ D_i must be coherent for every i.
   - This does not force U_L to be convex. For n = 2, U_L = D_1 ∪ D_2 meets it.

Since the author accepts tangency in limit cases, the natural place for (LF) is the target only. A
coverage axiom in that form:

**(A_LF)** every coherent model c is vindicated by some L with c ∈ C_L satisfying (LF).

## 3. Recent claims of mine that are rediscoveries

| Claim (12 Oct conversation) | Already in |
|---|---|
| "Trap": a strictly guiding one-sided additive extension reduces coverage to Bayes realisation | v3 `lem:bayes-necessary`(a,b); BA `thm:extension`; EDL `prop:one-sided`; CBOI `thm:fa`; NAL `lem:additive`(c), on any measurable U; NAL `thm:aggregation` (convex, concave or differentiable aggregations reduce to additive at one prior) |
| Face-respecting selections | CCIR `lem:face`, `cor:face`; v3 `lem:bayes-necessary`(c). Not forced on restricted domains; §2 gives the local version under (LF) |
| Worst-error (largest-error) rankings | TDL `rem:unsettled`, NAL `rem:open`(1), where flatness is already flagged. New only: the strict part is transitive, ties must be incomparable, and closed sections fail at ties |
| Σ_T conditional values | TDL `ex:jamesian` (James's two duties). CSE settles the (S) and coverage questions TDL left open |
| "Closed choice forces fineness, hence additivity, hence CPM" | CCF introduction. Proved only under completeness, the endpoint property and the pair conditions; IRC and IRWAS show it can fail otherwise. My general statement overstated it |

## 4. Correction to the 12 October remark about v19

I wrote that if closed choice forces additive extensions, the general route reduces to "CPM realisation,
though in a weaker form than v19, since finitely additive losses and restricted domains are both allowed".
That is wrong about domains: v19 has them, with integral losses (`def:cpm-loss` 9.2) and non-tangential
realisation (`def:cpm`). The differences are:
- general local penalty fields in place of CPM maps (NAL `lem:additive` already treats these);
- finite additivity (CBOI);
- domains not of cone form, which v19 does not consider.

## 5. Where the open question now sits

- **Additive or integral rankings:** essentially v19's problem. NAL `lem:additive`(c) holds on any
  measurable region U, so the Bayes reduction is unaffected by the shape of the region.
  - For domains that are not closed under splicing (not of the form "rules inside U"), the convexity step
    in that reduction can fail. Additive rankings on such domains are not covered by either folder.
  - Positive: parallel bodies (Thm 7.15), normalised boxes, interior singletons, the hexagon.
  - Negative: ε-contamination triangles (n = 3) for continuous non-tangential realisers
    (CONTAMINATION_NOGO); truth-directed additive losses at all priors in an open set (NAL
    `thm:obstruction`).
  - Whether non-convex regions U widen what is realisable is not addressed in either folder.
- **Finite non-additive aggregations** (NAL `thm:aggregation`): each undominated rule is Bayes at one prior
  for one additive map, which may change with the prior. This is the one relaxation of the global CPM
  constraint that the CPM folder identifies (NAL `rem:what-nonadditive-needs`).
- **Ordinal or partial rankings with (IB), domains of arbitrary shape, (LF) at the target:** no existing
  obstruction applies as proved, for any target. This is the open region.

## 6. Candidate conditions against trivialising (G) and (IB) (added 16:30; none adopted)

Setting: models are measurable acceptance sets D ⊆ ℝⁿ modulo null sets; a_D(g) is the advice of D on the
pair {g,−g}, g ∈ H. For X, Y and a measurable A = −A, the **splice** is X|_A Y := (X ∩ A) ∪ (Y \ A).
(G) applies to pairs in M_L, and (IB) applies whenever all four models in its statement lie in M_L.
Author's ruling: anything that makes (IB) empty is cheap. The 15:49 gluing construction is abandoned for
that reason.

- **(G)-closure.** If X, Y ∈ M_L and i is a world, then X ∨_i Y ∈ M_L. Here X ∨_i Y is the model whose
  advice on each pair is whichever of a_X(g), a_Y(g) is better at world i, choosing a_X(g) on ties. It is
  the splice X|_A Y with A the symmetric set of pairs on which a_X(g) is at least as good at i.
- **(SC) splice closure.** If X, Y ∈ M_L and A = −A is measurable, then X|_A Y ∈ M_L. (SC) implies
  (G)-closure. Up to measurability details, (SC) says M_L is a product of per-pair advice ranges (the advice that evaluable models give on each pair).
  All-model domains and v19 domains satisfy it.
- **(Ext) extendability.** There are preorders ⪯*_i on all measurable models such that:
  - (i) ⪯*_i restricted to M_L equals ⪯_i exactly, so strict parts and incomparabilities within M_L are
    preserved;
  - (ii) ⪯* satisfies (G) and (IB) on all models.

  Nothing else is required of ⪯*: not (S), (LA), (C), completeness, or any representation. Closed choice
  and competitiveness stay relative to M_L.

  Weaker variants:
  - (Ext⁺) asks only ⪯_i ⊆ ⪯*_i on M_L, so the extension may add comparisons within M_L;
  - (Ext_SC) asks for an extension only to the splice closure of M_L.

  The author has not chosen among these. Whether any version of (Ext) blocks the gluing construction is
  unchecked.
