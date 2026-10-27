# Overlap audit: do C1–C8 rediscover existing results? (12 Oct 2026)

## Scope and sources

- **Read:** the staged copies in `/mnt/user-data/uploads/CPMs/` and `/mnt/user-data/uploads/Generalized dominance paper/`. The device folders `$HOME/mnt/CPMs` and `$HOME/mnt/Generalized dominance paper` were accessed read-only with `device_bash`, using only ls, grep, cat, head and sed.
- **Read in full or in the relevant sections:**
  - v3 (`Full Coverage by Homothetic Credal Families v3.tex`), Sections 3–5 and Appendices B–C.
  - LDG v2, the appendix on real-valued rankings (lines 483–640).
  - BAGR (`Beyond Additive Guidance Rankings.tex`), Section 2.
  - EDL (`Edge Dichotomy and Leverage.tex`), Sections 1–2.
  - CBOI (`Closed Choice Beyond Ordinary Integrals.tex`), Sections 1–2.
  - CC (`Closed Choice for Independent Rankings.tex`), Section "Structure forced by (S)".
  - CCFF (`Closed Choice Forces Fineness.tex`): intro, Sections 4–5, main results and remarks.
  - CANA (`Coverage after Neutral Abstention.tex`), all of it.
  - CSE (`Conditional Shunning of Error.tex`): most sections.
  - OBFRG (`Omission Blindness and Four Rank Guidance.tex`), all of it.
  - IRC (`Incomplete Rankings and Coverage.tex`): Summary only.
  - `START HERE -- Coverage Status.md`, `Assessment and Remaining Question.md` and `Review of Complete Rankings`.
  - `nonadditive_losses.tex` (NAL), all of it.
  - `truth_directed_losses.tex` (TDL), Sections 1–5.
  - v19b (`LSP_CPMs_v19b.tex`): Sections 1, 2.6, 3.6, 5, 7 (statements), 8, 9, 10.6 and 12; Theorem 14.9 statement.
  - The Pettigrew PDF, via text search.
  - `FAMILY_LATITUDE.tex` and `CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md`, first sections only.
  - Device-only notes:
    - `outputs/complete-class-research/realization-and-coherence.md`, in full.
    - `domain_penalised_error_loss_handoff.md`, first 150 lines.
    - `STATE_OF_THEOREMS.md`, Sections 0–4.
    - Headers of the other notes named in the brief.
- **Not read in full:**
  - IRC (46 pages).
  - TAW, FSE, Three/Complete Rankings and DT.
  - The proofs of thm:realise and of Section 14 in v19b.
  - The June projective-order notes (GPO_*, DQ_*, Fplus_*, FINITE_PO_PROGRAM, etc.). Their headers show they concern realisability of polytopes by CPMs on R^n or on halfspace domains, not rankings.
- **Numbering:** theorem numbers for v19b are taken from the device copy of `LSP_CPMs_v19b.aux`. Line numbers refer to the staged copies.

---

## Verdicts

### C1 "Trap" (one-sided strictly guiding additive extension ⇒ coherent Bayes models and Bayes targets ⇒ realisation)

**Verdict: REDISCOVERY**, with one gap in how it is phrased.

**Where it already is:**
- **v3 `lem:bayes-necessary`** (line 628), with the same proofs:
  - (a) is (i): KKM applied to `A_i={q:C_q ≼_i B}` for a pointwise Bayes model B.
  - (b) is (ii): closed convex range by atomless splicing, plus a separating hyperplane.
- **BAGR `lem:complete-class` + `thm:extension`** (lines 114, 144, 9 Oct) is exactly the trap. If the comparisons at every world are "weakly respected by additive guidance losses", then:
  - L has coherent Bayes models at every prior;
  - an undominated target is competitive, so it is L-Bayes;
  - three-vertex targets are therefore dominated.
  - The note adds: "deleting any number of comparisons from an additive guidance ranking cannot solve the coverage problem."
- **EDL `prop:one-sided`** (line 91): only the one-sided pairs (C coherent undominated, X regular) are needed.
- **CBOI `thm:fa`** (line 139): the same architecture with finitely additive (Yosida–Hewitt) extensions.
- **LDG v2** `cor:bayes` (529) and `thm:margin` / `cor:strict` (546, 573): the loss-generated version.
- **Restricted domains:**
  - NAL `lem:additive`(b)–(d) (line 111) proves (ii) for additive losses on any domain `M_U={D: λ(D\U)=0}`.
  - v19b `thm:dominance` 9.10 (line 2094) proves admissible ⇔ Bayes ⇔ contraction for CPM error losses on M_L.

**"Coverage reduces to CPM-style realisation" is also already there:**
- v3 App. C, in the proof of `prop:bayes-vertex-obstruction` (line 820, contrasts eq. 873), shows that every coherent p-Bayes model sandwiches `{p·ψ>0}` for a strictly sign-preserving measurable contrast ψ.
- v3 `lem:three-world` (691) is stated for such ψ "without continuity or homogeneity".

**Gap in the phrasing:**
- If the one-sided inequality is assumed only for *selected* models on the left, (ii) gives only that the selected `C_p` tied with the target is l-Bayes. It does not show the target itself is.
- EDL's class `K_i` puts *every coherent undominated* model on the left, which covers the target. CBOI assumes the inequality for all regular pairs.
- C1 should adopt EDL's class, or else state the conclusion for `C_p`.

**On a v19-type domain:** C1 survives. M_L is closed under splicing, so the profile set stays convex (v19b `prop:cpm-sandwich`(iv), `thm:lyapunov`).

### C2 Face-respecting selection (`C_p = D_{K_p}`, `K_p ⊆ Δ_{supp p}`, precise at vertices)

**Verdict: REDISCOVERY for all-model domains. FALSE as stated on v19-type domains.**

**Where it already is:**
- **CC `lem:face`** (line 418): strict (G) plus "D_K competitive on S" implies `K ⊆ Δ_S`. The proof is the same improve-at-every-world-of-S argument.
- **CC `cor:face`**(a): `C_{e_i} ≈ D_i`.
- v3 `lem:bayes-necessary`(c) (additive case); EDL Section 1 cites "CC's Lemma 7 (face support)".

**Domain caveat:**
- The improving gambles (`g_S>0`, `g_j ≪ 0`) lie outside every proper CPM domain V.
- v19b **`prop:boundary-support` 12.10** (line 3230) gives the correct domain replacement: `Q_p ⊆ conv(Q_V ∪ Δ_S)`, and boundary points have support exactly S.
- v19b **`prop:vertex-realise` 12.12** (line 3277) gives `Q_{e_j} = conv(M ∪ {e_j})` at vertex priors. This is not precise.

### C3 The axioms other than coherence see a problem only through its sign pattern

**Verdict: NEW as an explicit invariance principle. The idea behind it is in the existing work** (PARTIAL OVERLAP in substance).

- I found no statement of it in either folder. Searches for "sign pattern", "only through", "orthant-preserving" and "pullback" found nothing comparable.
- **What is already there:**
  - v19b `def:cpm` (F2) and `def:cpm-loss`: the score field is `WΦ` because Φ preserves coordinate signs, so the error structure pulls back.
  - v3 App. C remarks that coherence alone forces the edge trade-offs to depend on payoff ratios.
  - CANA **`thm:closure`** (line 248) makes coverage an exact question about choosing a coherent family plus closed sections. That is a sharper, already-proved reduction of "coverage = which coherent families are realisable".
- **Caveats when writing it up:**
  - The transformations must be nonsingular, so that null sets are preserved.
  - Mixed versus unanimous is itself a sign-pattern distinction, so it is preserved.
  - On restricted domains, membership of the domain V is extra structure that the transformation must also carry.

### C4 Additive loss with unique Bayes models; equivalence with a measurable sign-preserving CPM; (S) without Bayes choice

**Verdict: PARTIAL OVERLAP.**

- **"Every unique-Bayes model ties a selected coherent model"** is a rediscovery: v3 `lem:bayes-necessary`(a) ("Some coherent C_q does at least as well as B … It must also be p-Bayes") plus uniqueness, and the first paragraph of the BAGR `thm:extension` proof.
- **Sufficiency direction of the equivalence:** v3 **`thm:general`** (line 268). If the pointwise Bayes advice is a.e. unique and coherent at every p, then all of (LA), (S), (C), (G), (IB) hold.
- **Necessity:** v3 App. C, as cited under C1.
- **Continuous, restricted-domain analogues:** v19b `thm:bridge` 9.8 and `thm:dominance` 9.10; NAL `lem:additive`(d).
- **"(S) does not require Bayes choice"** is a rediscovery:
  - LDG v2 `ex:rescale` / `rem:bayeschoice` (lines 604–615), plus the explicit sentence after `lem:bayes-choice` (line 525).
  - CSE **`prop:bayessel`** (line 420): Bayes-at-prior selections fail (S) unless T=∅, T=Ω or n=2, and `thm:S` uses a non-Bayes selection.
- **What is new:** stating an exact "iff" with a *global measurable* (discontinuous) CPM.
- **Caveat for that "iff":** a single contrast ψ determines the Bayes action only if `p·ψ(g)` and `p·ψ(−g)` are never both positive. v3 secures this through `(forced-edge-bounds)`. In general it requires a measurable per-problem rescaling `s(g)ψ(g)`. One exists, because coherence of every contraction excludes both being positive, and Gordan's theorem then gives positive multipliers. This step needs to be written down.

### C5 V exception = omission-blind / shun-error; limit of normalized boxes; Σ_T coverage = closures of normalized boxes with free coordinates

**Verdict: REDISCOVERY, with every part already present.**

- **V exception = omission-blind / shun-error:**
  - OBFRG (line ~25 onward): "For M=Δ, (1) is precisely the accepted exceptional table."
  - TDL `def:ob` / `prop:ob` / `thm:coverage` (lines 330, 363, 419) and **`prop:price`(a)** (line 463): V is vindicated only with `V=R^n_{>0}` and zero loss.
  - NAL **Remark `twoshun`** (line 445): the world-wise shun-error mix gives normalized boxes; the repair at the endpoint gives the omission-blind loss.
- **Limit of normalized boxes:**
  - CANA **`thm:limit`** (line 88), which credits `twoshun`. The START HERE "attribution correction" already concedes "its underlying coverage idea is not new".
- **Σ_T coverage:**
  - CSE **`thm:coverage`** (line 526). The family covers exactly `K(l,u)`: the closure of normalized boxes, with l_i=0 allowed and u_i=∞ allowed where l_i=0.
  - Also in CSE: `thm:undominated` (264), `thm:S` (372), `prop:notcovered` (604), `cor:vertices` (683).
  - Precursor: TDL **`ex:jamesian`** (line 537). Its credal set `{m_3 ≥ η max(m_1/p_1, m_2/p_2)}` is exactly a box with free worlds 1 and 2, and it leaves the family's coverage open.
  - Further precursors: NAL `cor:all-gambles` (285), boxes touching the boundary when some p_i a_i=0; v19b `prop:global-concave` 2.6 (positive bounds); `cor:two-states` 12.13.

### C6 Worst-error (sup of normalized seriousness over the difference set) rankings

**Verdict: NEW. It answers an open question already flagged in the CPM notes** (PARTIAL OVERLAP).

- **Where the question is flagged:**
  - TDL **`rem:unsettled`** (line 607): "Largest-error losses, F_i(E)=ess sup_{g∈E} c_i(g/‖g‖) … their increments can vanish … they are flat … threatens (C∼). I have not determined their admissible sets."
  - NAL **`rem:open`**(1) (line 573) lists largest-error losses as open.
- **Different objects, not to be confused with it:**
  - TDL `prop:nonadditive`(b) (line 274) treats `max_l μ^l`, a maximum of finitely many *measures*, and shows its exchange rates vanish.
  - The Pettigrew PDF (accuracy without additivity) uses continuity plus strict propriety. It has no sup-type or lexicographic measures; only minimax "worst-case inaccuracy" is mentioned (text lines 105–110).
- **Related mechanisms that may shorten C6's proofs:**
  - CC `lem:primary` (line 500): (S) fails once uncountably many undominated models with distinct primary values have invisible improvements.
  - BAGR `prop:lex` (line 368): a priority (lexicographic) ranking admits no (S).
  - EDL `thm:leverage` (line 112): the leverage-sequence criterion for no one-sided extension.
- **Framework caveat:** if ties are intransitive, the weak relation is not a preorder. The rankings then fall outside the framework (LDG and CBOI require preorders), unless only the strict part is used and the framework is changed to allow that.

### C7 "Closed choice forces fineness; fineness + (IB) = Savage/de Finetti route to additivity; so closed choice pulls back to CPM"

**Verdict: REDISCOVERY, and the general form overstates what is proved.**

- **Where it already is:** CCFF intro (lines ~32–41) says it almost verbatim: "By (IB), the comparisons … of pure debt sets, and separately of pure credit sets, are comparative probabilities in de Finetti's sense. The closed sections of (S) … make them fine. The Savage–Wakker theorem then gives finitely additive probabilities … One exchange rate … assembles these into a weak extension of the form required by CBOI's theorem." The chain is:
  - `thm:fine` (314) → `lem:cp` (400) → `thm:SW` (417) → `thm:extension` (575) → `thm:A` (649) → `thm:reduction` (671);
  - "pull back to CPM" is then BAGR `thm:extension` or CBOI `thm:fa`.
- **Hypotheses the slogan omits:**
  - **Completeness:** CCFF `rem:complete` (782) says "Wakker's theorem needs a complete order". IRC uses (SC).
  - **The endpoint property (EP) on edges.** CCFF `rem:open` (837) says that EP for undominated V *is* the whole remaining complete-ranking conjecture. IRC Theorem A replaces it with T1o.
  - **The exchange-rate step,** which needs SI/AC pairs.
- **Counterevidence:**
  - IRC summary item 7: (NC) can fail. In the residual configuration, two worlds violate (NC) and have no one-sided extension (item 5).
  - IRWAS (`Independent Rankings Without Additive Structure.tex`, `thm:noprimary`, `thm:nolocal`): completeness + strict (G) + (IB) do not force additive structure.
- So "closed choice pulls the framework back to CPM" is proved only under completeness + EP (or T1o) + the SI/AC conditions, not in general.

### C8 What v19b's realisation theory actually covers

**Verdict: REDISCOVERY.** This is a record of v19b; nothing new is claimed.

**Targets:**
- **Non-tangential, LP maps:** parallel bodies `K = L + rB_H ⋐ int Δ` (`def:c2plus`, line 845), at any `q ∈ relint K`, by `thm:realise` 7.15 (line 1635). This is non-tangential: `cl D_K \ {0} ⊂ V_κ`.
  - These are full-dimensional with C² boundary (`prop:parallel-scope`(ii)).
  - **No polytope is a parallel body for n ≥ 3** (`prop:parallel-scope`(iii)).
- **Non-tangential, on V = R^n:**
  - normalized boxes with positive bounds, via global concave CPMs (`prop:global-concave` 2.6);
  - interior singletons (`ex:singleton` 12.7).
- **Non-tangential, on a halfspace or other proper V:** two polyhedral examples (`ex:box-realisation`, line 3034, on `V=D_q`; `ex:lp-hexagon`).
- **Approximation:** any target is approximated in measure (`cor:approx-all` 12.4).
- **Tangential:** boundary targets `conv(M ∪ {e_j})` at vertex priors (`prop:vertex-realise` 12.12).
- **n = 2:** everything except V (`cor:two-states` 12.13).

**Losses:**
- The CPM error loss `def:cpm-loss` 9.2 (line 1910): finite error loss with densities `W|Φ_i|` on V and 0 off V, with W>0 and `∫W|Φ_i| < ∞`.
- It is evaluated only on `M_L = {D : λ(D\V) = 0}`.
- Dominance theory needs null indifference sets (`thm:dominance` 9.10). Concave coordinates are sufficient (Lemma `lem:indiff-null`).

**Domains:** a CPM domain is an open convex cone `V ⊇ R^n_{≥0} \ {0}` (`def:poscone`, line 191). For LP maps, `V_κ = {P*_κ > 0}` is proper.

**(IB) on the domain:** holds. The loss is an integral over error sets, so (IB) holds whenever the four models are in M_L.

**(G) on the domain:**
- **Proper V:** `V ∩ (−V) = ∅`, so domain models are never contradictory on a non-null set. Good < silence < bad is strict wherever `W|Φ_i| > 0` (on V, off `{g_i = 0}`), so strict (G) holds on the improvements available within M_L.
- **V = R^n** (global boxes): contradiction costs `d_i < c_i + d_i` (bad), so the **four-rank (G) fails**.
  - OBFRG proof eq. (3) and CANA note this and fix it with a larger contradiction penalty.
  - The loss is truth-directed with respect to error-set inclusion, which is a weaker background order.

**Other properties:**
- (S) holds with Bayes choices and continuous losses (`thm:dominance`(i)).
- (E) needs a V = R^n member in the class.

**The boundary obstruction, Cor. 12.11 (`cor:boundary-support`, line 3257):**
- **Hypotheses:**
  - Φ is a CPM in the sense of `def:cpm` (continuous, positively homogeneous, *exactly* sign-preserving, F3) on a CPM domain containing **all of `R^n_{≥0} \ {0}`**, so every e_i ∈ V.
  - K has two boundary points of Δ with different supports, nested or incomparable.
  - The loss is a CPM error loss, which is additive.
- **Conclusion:** D_K is not a contraction at any prior; no coherent D with interior D_K is admissible; it is uniformly dominated if the indifference sets are null.
- **Proof route:** `prop:boundary-support` 12.10 (uses F2 at each e_i ∈ V), then `cor:error-cct` (admissible ⇒ Bayes).
- **Escape routes recorded in TDL `rem:designs`:** relax the domain to `R^n_{>0} ⊆ V`, or use omission blindness.

---

## A consequence for the non-tangency requirement in the brief

**On a proper v19-type domain, non-tangency cannot hold at boundary priors.**

The argument:
1. Let `S = supp p ≠ Ω`. Strict (G) on domain models and competitiveness on S against M_L force `C_p ⊇ V ∩ {g_S ≫ 0}` a.e. Adding those gambles is a domain-internal strict improvement at every world of S.
2. The ray `Σ_{s∈S} e_s − t e_k`, with k ∉ S, leaves V at a finite t. This is because `cl V ∩ R^n_{≤0} = {0}` (v19b `lem:halfspace`, `lem:three`).
3. So `cl C_p` contains a nonzero point of ∂V.

**What v19b already records:**
- Tangency at vertices for LP maps (`prop:vertex-realise` 12.12).
- Non-tangency only at full-support priors (`lem:nontangent` 3.6, line 649; FAMILY_LATITUDE `thm:containment`: "for any sequence r_k → e_i … these distances tend to zero").
- Non-tangency on a proper V forces full-dimensional K, so no precise selected models (`prop:dimension-necessary` 7.3, line 1217).

**Consequence:** requiring "every selected `C_p` has `cl C_p \ {0} ⊂ V`" forces V = R^n. The requirement should be restricted to full-support priors, or to the target.

---

## CPM-folder results bearing directly on coverage by NON-additive or partial rankings on restricted domains

**truth_directed_losses.tex**
- **`thm:obstruction` 2.4 (l.168) / `cor:vacuous` 2.5.** Truth-directed, possibly non-additive, losses on any domain closed under adding the thin cones A_ij(δ). With vanishing exchange rates, targets with incomparable boundary supports are dominated. The cones lie in every v19 domain containing e_i and e_j (`ex:cpm`).
- **`prop:nonadditive` 3.3 (l.274).** Vanishing rates hold for bi-Lipschitz transforms, max or min of finitely many error measures, and nonnegative sums. They can fail for √μ.
- **`rem:nested` 2.6.** Nested supports are open for non-additive losses.
- **`prop:price` 4.5(b) and `rem:designs` (l.463, 517).** Coverage of different-support boundary targets requires a domain omitting a boundary vertex, so it is tangential. Write-in losses on the target's own interior make the target compete only within that interior.
- **`ex:jamesian` and `rem:floor`.** A two-state κ-loss vindicates V; the same formula fails for n=3.
- **`rem:unsettled`.** Largest-error losses are flat. Infinite penalties break (S).

**nonadditive_losses.tex**
- **`thm:aggregation` (l.171), `cor:concave-ingredients` (247), `cor:all-gambles` (285).**
  - A rule that is not strictly dominated under a monotone convex, concave or differentiable combination of error losses on any domain V is Bayes for one additive loss at one prior.
  - With concave ingredients, that loss comes from one concave CPM on V.
  - On R^n, the result is normalized boxes only.
- **`prop:worldindependent`.** A world-independent truth-directed loss ignores mixed gambles.
- **`thm:obstruction` (l.491).** No truth-directed additive loss, on any measurable V, has the ε-contamination of q as Bayes rule for all q in an open set (n ≥ 3).
- **`rem:what-nonadditive-needs` and `rem:open`.** These list the open non-additive routes.

**LSP_CPMs_v19b.tex**
- **12.10, 12.11, 12.12, 3.6, 7.3:** see above.
- **10.6 `prop:precise-domain`.** In the self-recommending setting of `cor:selfrec`, a precise contraction `C = D_q` forces V = R^n.
- **14.9 `thm:hs-nogo`.** No concave CPM on any halfspace domain realises rounded segments or a rounded body with one flat face non-tangentially.

**CONTAMINATION_NOGO_SCOPE_AND_GEOMETRY.md** (§1–2)
- No continuous, non-tangential CPM realises the 3-state ε-contamination at any interior prior. This is additive and on restricted domains; scope n=3 only.

**FAMILY_LATITUDE.tex `thm:containment`**
- LP selections are non-tangential at full-support priors, but the gap to ∂V vanishes at vertices.

**`outputs/complete-class-research/realization-and-coherence.md`** (device)
- §2: a realisation theorem for an arbitrary model set. If Bayes profiles are compact and Bayes-convex, every profile is weakly dominated by an undominated Bayes profile.
- §3: finite-error losses with a.c. densities whose undominated profiles include incoherent ones. Realisation conditions alone do not force coherence.

**`domain_penalised_error_loss_handoff.md`** (device)
- An alternative to restricting the domain: evaluate all rules, but charge off-V acceptance at every world. This violates (G) for good acceptances outside V.

**From the dominance folder (directly relevant)**
- **CANA `thm:closure`:** an exact ordinal consistency test for partial rankings given a family and its sections.
- **OBFRG:** write-in, four-rank, domain-like coverage of every target, under the broader weakening, which has not been adopted.
- **CSE:** complete additive coverage of K(l,u).
- **BAGR `thm:extension`:** no partial ranking whose comparisons are weakly respected by an additive guidance loss escapes the three-vertex obstruction.
