# N27: the conic-neighbourhood repair on general decomposable domains, and the unconditional theorem under permitted ties

14 Oct 2026. Task: BRIEF8, the two auditor repairs. Labels: **PROVED** (full proof here, or a line-by-line re-reading
of a refereed proof with every changed step written out), **CHECKED** (verified, proof sketched), **CONJECTURE**,
**NUMERICS**. Glossary of START HERE is used throughout. Scripts: `n27py/`.

Read: BRIEF8, Glossary, BRIEF4–BRIEF7, writeup "The Contamination Triangle.tex", N5, N6 (via N7), N7, N15, N18, N20,
N21, N23, CHECK_REPORT, and the imports they use (R1 §§1–3, R10b §§1–5, N14 §§1–3, N2 §§1–3, AUDIT_ASSESSMENT2).

---

## 0. Outcome

**(i) Conic neighbourhood.** The auditor is right that (LF) supplies only an open N, and that N need not contain a
conic neighbourhood of ∂D_T∖0. The example N = {g : dist(g,∂D_T) < e^{−‖g‖}} is one: it contains all nonzero boundary
points, but the ray t(h₀ + ρn) leaves it for large t (`lf_example.py` (a)).

The damage is nil:
- **Repair 27.1 (PROVED).** Every use of the conic N₀ in N21/N23 (and in the writeup's §"General decomposable domains") is a
  statement about gambles in a small neighbourhood of one fixed **compact** set Σ of boundary gambles at bounded norm.
  Σ consists of the normalised corner rays, the facet segments h([0,1]), the crossings in both normalisations used, and
  the limits of the box witnesses and test gambles. Replace N₀ by a compact collar N₀ᵇ ⊆ N of Σ. All statements and
  proofs then hold verbatim, provided the level bound c₀ and the radius r₁ are taken small relative to the collar width
  (§1.2).
- **Lemma 27.2 (ray transfer, PROVED).** On any decomposable domain with (BU), for a.e. (g,t), R(tg)∩Ω = R(g)∩Ω. The brief's
  suggested route works at the level of charts. Advice ranges *can* differ along a ray, but under strict guidance only in
  whether silence is in them, and only on pairs with advice range {+,0,−} whose silence cell in Ω has empty interior (Cor 27.3). So the
  chart-level content of the conic N₀, i.e. the conic form of N21.2, is recovered anyway.
- **Nothing must be added to (LF).**
- **U-domain (evaluable models: the measurable subsets of U): unaffected (confirmed).** The cone U is given explicitly, (LF) holds with the open cone
  N = U, and the N12/N15 chain uses U, never N.
- **Non-adjacent corollary: unaffected (confirmed).** The cone D_{K′} is explicit in the hypothesis. The cone on which
  acceptance is in the advice range comes from R1 Prop 2.5, which already handles an arbitrary open N via the conic reach set.

**(ii) Permitted ties.**

**Theorem 27.6 (PROVED, resting on N5 Thm 3.3's facet clause, refereed CORRECT in N7).** The unconditional main theorem
(writeup Thm 4.1 = N15.8) holds for permitted-tie realisations, provided θ < θ_x(T). Here

  θ_x(T) := min over facets F_k and crossing coordinates i ≠ k of sup_{h ∈ F_k∖0} h_i/‖h‖.

The same holds for the coverage corollaries on M_U, and also on domains that are non-adjacent near T (the latter at
CHECKED level, §2.6).

For T1:
- *sup norm:* θ_x = 1, so the theorem holds for **every θ ∈ (0,1)**, i.e. every θ for which the band is a proper subset
  of the mixed problems;
- *Euclidean norm:* θ_x = √((κ²+1)/(κ²+2)) (0.837 / 0.928 / 0.999 at ε = .05 / .3 / .9), which is > √(2/3) ≈ 0.816 for
  every ε.

The values are reproduced in `thresholds.py`. The corner threshold Θ_NT < θ_x of N7 is **not** needed, because the
chain never needs vertex positivity at corner rays.

**Where the danger points are.** Item by item through N15's chain (§2.3):
- **only one input is tie-sensitive**: UVN(a), i.e. vertex positivity of a facet gamble x ∈ relint F_k at a world l
  with x_l > 0;
- every crossing is a band point for every θ > 0, so strictness never supplies this input near the crossings
  (`thresholds.py`: for every θ a positive fraction of each facet is band);
- **it is supplied by N5 Thm 3.3** (no ties accumulate at facet points with h_l > 0) when θ < θ_x;
- every other strict-sign use is either strict *badness* (c_i < 0 where g_i < 0, never tied) or can be replaced by
  weak signs:
  - Lemma M/PL2 Step 4;
  - pivot Step 4;
  - box bridge (a), via N5 Lemma 4.2.

**Beyond θ_x (Euclidean θ ∈ [θ_x, 1)): open.** The precise missing statement is

  (VP) for every x ∈ relint F_k and l ≠ k with x_l > 0: liminf_{q→e_l, q∈Ω} P(q,x) > 0.

(VP) is equivalent to UVN(a) at x (Lemma 27.5). Under (VP) the transfer holds for every θ. For θ ≥ θ_x, (X_lk) fails,
and the vertex analysis no longer excludes directional vertex limits W ∋ v_k (e.g. W = [e_l, v_k]), which violate (VP)
on all of F_k (§2.7). Status: CONJECTURE that no realisation exists there either; no construction attempted.

**Side corrections.**
- (C) forces interior Bayes uniqueness for **every** θ and both norms. R1 Lemma 1.4 uses no guidance at all, so the
  caveat "θ < 1 (sup), θ < 1/√3 (Euclidean)" in BRIEF4/N7 is unnecessary (§2.1).
- R1 Prop 2.4(ii) (the reach set is a finite union of cones) uses strict vertex uniqueness. Under ties it is replaced by
  a countable-union version (Lemma 27.7) that uses no vertex facts.

---

## 1. Part (i): the neighbourhood N of (LF)

### 1.1 Inventory of every use of N (or of a neighbourhood derived from it)

"Bounded-local" means the step needs the property only for gambles in a neighbourhood of a compact set of nonzero
boundary gambles, at norms in a fixed interval [a, b] ⊂ (0, ∞).

| Place | What is used | Scale | Verdict |
|---|---|---|---|
| Writeup Def. LF, Glossary | open N ⊇ ∂D∖0 | — | already the open form |
| BRIEF7, START HERE "Strategy" bullet, N5 (SH_θ), N14 §1, R10a §1 | "open cone N" | — | inherited convention; see 1.4 |
| R1 Prop 2.6 (interior p\*) | a ball B ⊆ N around one g₀ ∈ ∂D∖0 | bounded-local | unaffected |
| R1 Prop 2.5 (conic U′ ⊆ W) | N ⊆ W a.e.; W° a finite union of cones | arbitrary N handled | unaffected; Lemma 27.7 for ties |
| R10b §1 (U ⊆ N; shrink N off −cl D and off {h ≤ 0}) | small ball U around a crossing; N∖(−cl D) is open | bounded-local | unaffected |
| R10b UVN, Prop V, Lemma D, M, Cor PL2 | balls in N around single points | bounded-local | unaffected |
| N12, N15 (U-domain) | advice ranges {+,0} on all of U | U explicit | unaffected |
| N14 §3(iv), writeup Cor 4.2 | non-adjacency on an explicit D_{K′}; U′ from R1 Prop 2.5 | conic by hypothesis/derivation | unaffected |
| **N21 §1, writeup §5 preamble** | closed **conic** N₀ ⊆ N with P_{K″} > 0 | see below | **repair 27.1** |
| N21.2 = writeup Lemma 5.2 | "for a.e. g ∈ N₀": no R(−g), no d-face, half-plane chart on {K_q ∩ K″ ≠ ∅} | pointwise in g | bounded-local |
| N21.4 item 1 (N23 repair) | levels c with h − c𝟙 ∈ int N₀, ⊇ [−c₀, c₀] for facet gambles | facet family, \|c\| ≤ c₀ | bounded-local |
| N21.4 item 5 | good g_m → h(τ) in N₀ | near h(τ) | bounded-local |
| N21.4 item 6 / Thm 4.3 | r ∈ int N₀ (normalised corner ray) | one point | bounded-local |
| N21.6 Step 1 | witness balls around A_s → w′, B_s → w (s ↓ 0) | near two crossings | bounded-local |
| N21.6 Steps 3–4 | N21.2 for the cut gambles g_m (near w\*) | near w\* | bounded-local |
| N21.6 Step 7 | test gambles h = w\* − δ𝟙 + ηe_b ∈ N, δ, η ↓ 0 | near w\* | bounded-local |
| N21.7(a), N21.9(iii), R23.4 | acceptance in the advice range on {h_b > 0}, {v_k·h > 0} | **conic, but derived from cones D_{K_q}** | no N used |
| N23 R23.1 Step 1–2 (CHECK_REPORT: "U ⊆ int N₀ is needed") | R10b ball U around w with U ⊆ int N₀ | near w | bounded-local |
| N23 R23.2, R23.3 | R23.1 and N21.4 items 1–4; balls U_η shrinking to w | near w | bounded-local |

No step uses N₀ at norms tending to 0 or ∞. No step uses a ray through a gamble of N₀, except through homogeneity of
P(q,·) = min_{K_q} m·(·). That is a property of K_q, not of the domain: "Ψ ≥ 0 on [σ₁,σ₂] gives K_q ⊆ W_{v_k}(Ũ)" uses
only that F_k ∩ cl Ũ ⊆ cone h([σ₁,σ₂]).

### 1.2 Repair 27.1 (PROVED)

**Setting.** Strictly guiding additive ranking on a decomposable domain, (LF) at T with an arbitrary open N, (R1) = (BU) at every
interior q, (R2), and T all-facing in general position (T1 included). Fix a compact K″ ⊆ int T.

**Construction.**
- Let Σ ⊆ ∂D_T∖0 be the compact set consisting of:
  - the three facet segments h([0,1]) between the normalised corner rays;
  - the crossings in every normalisation used (e.g. w₂₁ = (−1,0,κ) and w₂₁/κ for T1);
  - the limits of the box witnesses (writeup Prop 4.22) and of the N21.6 test gambles.

  Its norms lie in [a, b] with 0 < a < b < ∞.
- Since N is open and Σ is compact, there is η > 0 with N₀ᵇ := {g : dist(g, Σ) ≤ η} ⊆ N.
- Since P_{K″} > 0 on Σ (N23 §1: a zero of P_{K″} at h ∈ ∂D_T∖0 would make h vanish on aff Δ) and P_{K″} is continuous,
  we may also take η so small that P_{K″} > 0 on N₀ᵇ.
- After the R10b §1 shrinking, N₀ᵇ ∩ (−cl D_T) = ∅ and N₀ᵇ contains no h ≤ 0, so advice ranges on N₀ᵇ are {+,0} or {+,0,−}.

**Claim.** With N₀ replaced by N₀ᵇ, every statement of N21 §§2–6, N23 §§1–8 and writeup §5 holds, with the same proof,
provided:
- c₀ < η/√3, so that h(τ) − c𝟙 ∈ int N₀ᵇ for |c| ≤ c₀;
- r₁ is shrunk so that |Ψ_k(q,τ)| < c₀ on B(p\*,r₁) × [0,1] for each facet (joint continuity; Ψ(p\*,·) ≡ 0 on [0,1]);
- R10b's balls U around crossings, and the witness and test-gamble neighbourhoods, are taken inside int N₀ᵇ. This is
  possible because their centres lie in Σ or converge to points of Σ.

**Proof.** Go through the table in 1.1.
- **N21.2.** The proof is pointwise in g (N23 §3 improvement): it uses only g ∈ N (advice ranges), P_{K″}(g) > 0 and goodness of
  g. Both hold on N₀ᵇ.
- **Local straight levels (N21.4 item 1, N23 repair).** They use only good gambles in int N₀ᵇ near h(τ) − c𝟙 with
  |c| ≤ c₀.
  - Lemma 2.1 needs levels c ∈ (0, min f(q_i)) and (c, c + η′) for points q_i ∈ B₁.
  - All such levels are < c₀ in absolute value by the choice of r₁. (This is N15's "Uniformity" remark, now with c₀
    fixed by the collar.)
  - The sandwich Lemma 2.3 uses the levels c = f(q), q ∈ B₁, which are again < c₀.
- **Item 5 (c-clusters).** It uses good g_m → h(τ), eventually in int N₀ᵇ.
- **Thm 4.3.** It uses only r ∈ Σ.
- **§§5–6 of N15 on B₁.** These steps are local in q and use only h(τ), τ ∈ J ⊂ (0,1), and levels below c₀.
- **N21.6, Steps 1–7.**
  - The witness families A_s, B_s converge to the two b-crossings, so for small s their balls lie in int N₀ᵇ.
  - The cut gambles g_m are taken in those balls.
  - The test gambles converge to w\* ∈ Σ.
  - Edge forcing (R1 Prop 2.8) is applied to non-null subsets of small balls around them, which lie in N.
- **N21.7, N21.9(iii), R23.4.** These use cones D_{K_q} ≈ B_q ⊆ Av and no neighbourhood.
- **R23.1–R23.3.** The R10b ball U (and U_η) around the crossing w ∈ Σ is chosen inside int N₀ᵇ. The UVN balls and the
  points w_± are inside U.
- **Homogeneity steps.** These concern K_q only. ∎

`lf_example.py` (b): for the auditor's N at ε = 0.3, the norms on Σ lie in [1.09, 3.58], a collar of width 0.0085
around Σ lies in N (0/20000 random collar points outside N), and the repair needs c₀ < 0.0049. NUMERICS, illustration
only.

### 1.3 Ray transfer: what scale invariance does and does not give

**Lemma 27.2 (ray transfer of charts; PROVED).**
- *Hypotheses.* An additive ranking (strictly guiding, or with permitted ties) on a decomposable domain, with measurable
  penalties, such that for every q ∈ Ω the set B_q := {h : q ∈ R(h)} of orientations accepted at q satisfies
  B_q ≈ D_{K_q} ∪ {h ≥ 0}. This is (BU), forced by (LA), (S), (C) via R1 Lemma 1.4.
- *Conclusion.* For a.e. (g,t) ∈ ℝ³ × (0,∞): R(tg) ∩ Ω = R(g) ∩ Ω.

*Proof.*
1. The set M := {(q,g,t) ∈ Ω × ℝ³ × (0,∞) : 1[q ∈ R(g)] ≠ 1[q ∈ R(tg)]} is measurable. Each R(g) is cut out of Δ by
   finitely many strict affine inequalities whose coefficients (penalty differences) and whose case distinction (the
   advice range) are measurable in g.
2. *Each (q,t)-section is null.* For fixed (q,t), the g-section is B_q △ t⁻¹B_q. The set D_{K_q} ∪ {h ≥ 0}∖0 is a cone,
   and dilation preserves null sets, so B_q △ t⁻¹B_q ⊆ (B_q △ D′) ∪ t⁻¹(B_q △ D′) with D′ := D_{K_q} ∪ {h ≥ 0}. This is
   null.
3. *Fubini.* M is null. Hence for a.e. (g,t), the q-section is null, i.e. R(g)∩Ω and R(tg)∩Ω agree a.e. on Ω.
4. *Equality.* Both sets are relatively open and convex in Ω, since every entry of R1's table of charts for each advice range is. Two open convex
   sets that agree a.e. have the same closure, and an open convex set is the interior of its closure. ∎

**Corollary 27.3 (what may and may not change along a ray; PROVED).** Under the hypotheses of Lemma 27.2 with
strictly guiding penalties, for a.e. mixed g and a.e. t > 0:
- (a) "accept g" is in the advice range at tg iff it is in the advice range at g. Likewise for −g.
- (b) Every evaluable model (effectively, i.e. up to ×) accepts tg iff every evaluable model (effectively) accepts g. For mixed g in a covering ranking this never
  happens (R10b Cor V1).
- (c) If S(g) ∩ Ω := Ω ∖ (R(g) ∪ R(−g)) has nonempty interior, then silence is in the advice range at tg.
- (d) Silence can be absent from the advice range at tg while present at g (or conversely) only if S(g) ∩ Ω has empty interior. Then
  R(g) ∪ R(−g) covers Ω up to a line.

Consequently, advice ranges may differ along a ray. But under strict guidance they differ only by × and by silence on
thin-silence pairs, and the charts never differ.

*Proof.*
- (a) Under strict guidance, an orientation h of a mixed pair whose acceptance is in the advice range has R(h) ∋ e_l in its relative interior for
  every l ∈ P(h) (R1 vertex property), so R(h) ∩ Ω ≠ ∅. An orientation that no evaluable model accepts has R(h) = ∅. Apply Lemma 27.2 to h
  and −h.
- (b) For a mixed pair, R(h) ∩ Ω = Ω iff the advice range (minus ×) is {+}. Every other chart misses a neighbourhood of
  e_k, for k ∈ N(h).
- (c), (d) If silence is not in the advice range at tg, the advice range minus × is {+,−}, {+} or {−}. ({×} alone is excluded by (LA), R1
  Prop 2.1.) So R(tg) ∪ R(−tg) ⊇ Ω minus the d-line, and S(tg) ∩ Ω = S(g) ∩ Ω lies in a line. ∎

*Example showing (d) is real (CHECKED).* At g take advice range {+,0} and chart {c·q > 0}. At tg take advice range {+,0} but with any
other c̃ ∝₊ c. Rescaling is invisible.

The only possible variations are, at pairs with advice range {+,0,−} and an empty silence cell, removing silence from the advice range and keeping d. That
is consistent: R1's chart table is unchanged.

Near ∂D_T this cannot happen on a non-null set:
- for g near a relint facet point, R(−g) ∩ B₁ = ∅ (N21.2);
- the chart line of g passes near p\* (unique clusters, N21.4);
- so S(g) ⊇ an open half-disc of B₁.

**Corollary 27.3′ (conic N21.2 at chart level; PROVED).** For a.e. g ∈ cone(int N₀ᵇ), and every convex open
C ⊆ {q : K_q ∩ K″ ≠ ∅}:
- R(−g) ∩ C = ∅;
- R(g) ∩ C is ∅, C, or an open half-plane ∩ C;
- no d-face of g meets C.

*Proof.*
- The first two statements are Lemma 27.2 applied to g/t ∈ N₀ᵇ. Only the dilation argument of Lemma 27.7's proof is
  needed to pass from "a.e. (g,t)" to "a.e. point of the cone".
- *No d-face.* Suppose p ∈ F(g) ∩ C. Then d(p) = 0 < α(p). The affine function d is nonconstant on aff Δ, because d has
  the strict mixed sign of g. So points near p in C have d < 0 < α, hence β = α − d > 0, hence lie in R(−g). This
  contradicts the first statement. ∎

So the conic statement N21 wrote down is true for covering rankings. Only its *proof* needed a conic N₀, and the repair
makes that unnecessary. What does not transfer along rays:
- the penalty vectors c(tg) (only their charts transfer);
- whether silence is in the advice range on thin-silence pairs;
- under permitted ties, whether acceptance is in the advice range at gambles whose positive coordinates are all band points and tied.
  There R(g) = ∅ can occur with + in the advice range.

### 1.4 The "open cone" convention elsewhere

BRIEF7, START HERE's 13-Oct strategy bullet, N5's (SH_θ), N14 §1 and R10a §1 state (LF) with an open cone. Status of
each:
- **N5–N7.** These arguments are bounded-local (N7 §1 already said so). Nothing changes. On M_U, N = U anyway.
- **R10a §1 ("shrink N so that it is an open cone").** As AUDIT_ASSESSMENT2 notes, this shrinking is not available. R10a
  results (Thm V, Thm R, Thm M) are not used by the main chain or by §5 of the writeup. Where needed, the cone on which acceptance
  is in the advice range comes from the reach set (R1 Prop 2.4–2.5, or Lemma 27.7), as the auditor recommends. Each R10a use
  should be re-read with that substitution. *Not done here.*
- **Recommendation.** Make the Glossary's open-set form the official definition, and add one sentence: "for additive
  rankings with (BU), charts are ray-invariant (Lemma 27.2), so the conic form holds at the level of charts".

### 1.5 The U-domain and non-adjacent theorems (CONFIRMED)

- **On M_U.** U = D_{K′} is given. Every pair with an orientation in U has advice range {+,0}. (LF) holds with N = U, an open
  cone. A realisation (writeup Def 3.2) is defined on all of U. N12 §1, N15 and writeup §4 use U (levels g − t𝟙 ∈ U,
  t ∈ I_g; edge box A + λB ∉ U ⇒ P ≤ P_{K′} ≤ 0) and never a neighbourhood from (LF). **Unaffected.**
- **Domains non-adjacent near T (writeup Cor 4.2).** The hypothesis names an explicit cone D_{K′}. The reduction
  (N14 §3(iv)) needs acceptance in the advice range a.e. on U′ := D_{K′} ∩ D_{K′₁}, where D_{K′₁} ⊆ W comes from R1 Prop 2.5. Since
  D_{K′} ∩ D_{K′₁} = D_{co(K′ ∪ K′₁)} with co(K′ ∪ K′₁) ⊆ ri T, both properties hold on one explicit cone.
  - R1 Prop 2.5's proof handles an arbitrary open N: N ⊆ W° a.e., and W° is an open cone, a finite union of D_{V^i}.
    The step "N ⊆ int cl W°" needs only openness of N.
  - **Unaffected.**

---

## 2. Part (ii): the unconditional theorem under permitted ties

### 2.1 Setting and the reduction to a realisation

**Permitted NSI_θ (BRIEF4), additive form, on M_U.** For g ∈ U put c(g) := ℓ(g,0) − ℓ(g,+). Then:
- c_i(g) ≥ 0 if g is band-i⁺ (mixed, 0 < g_i ≤ θ‖g‖), with ties placed by the ranking;
- c_i(g) > 0 if g_i > θ‖g‖, or if g is unanimous;
- c_i(g) < 0 if g_i < 0 (bad is strictly worse than silence; never tied).

(N2 Lemma 0 / N5 Lemma 2.1.) The norm is sup or Euclidean, θ > 0.

**Permitted-tie realisation of T at p\* on M_U.** A measurable c : U → ℝ³ with these weak signs, together with (BU) at
every q ∈ Ω and (TP) K_{p\*} = T.

**Proposition 27.4 (reduction; PROVED).** A permitted-tie additive ranking on M_U (integrable envelopes) with (LA), (S),
(C) that covers T yields a permitted-tie realisation of T at an interior p\*.

*Proof.*
- **(BU).** R1 Lemma 1.4: (i) interior Bayes models are undominated (Lemma 1.3(c), additivity only), hence coherent
  (KKM + (C), valid for preorders); (ii) a non-null tie set yields a family X_F of Bayes models that cannot all be
  a.e. cones (radial Fubini).
  - **Neither step uses (G).** So (BU) holds at every interior q, for every θ and both norms. This corrects the
    BRIEF4/N7 remark that (C) forces it only for θ < 1 (sup) or θ < 1/√3 (Euclidean).
  - On M_U the point is moot anyway: two distinct kinds of advice + and 0 on a mixed g differ strictly at the world where g is
    negative.
- **(TP).** T ∈ C_L is undominated, hence p\*-Bayes for some p\* (R1 Lemma 1.3(b), additivity only), and B_{p\*} ≈ T.
  p\* is interior by N1 Prop 2.3, which uses only strict badness (N7 §1).
- Charts are {c(g)·q > 0}, as in R1's table. ∎

Writeup Prop 3.3 (a), (b), (d) hold verbatim. Rescaling c̃ = p\*⊙c preserves zeros, and the band is a property of g.
(e) holds with the vertex clause weakened to "e_i ∈ cl H(g) if g_i > 0 (∈ H(g) if c_i(g) > 0); e_i ∉ cl H(g) if
g_i < 0".

### 2.2 The one tie-sensitive input

**Lemma 27.5 (UVN(a) ⇔ vertex positivity; PROVED).** Let x ∈ U be mixed and x_l > 0. Then UVN(a) at x for world l
holds iff

  (VP_x) liminf_{q→e_l, q∈Ω} P(q,x) > 0.

UVN(a) here means: a ball B₁ ∋ x and a relative neighbourhood V_l of e_l with P > 0 on (V_l∩Ω) × B₁, and H(h) ⊇ V_l∩Ω
for a.e. h ∈ B₁.

*Proof.*
- (⇒) is trivial.
- (⇐) Let P(q,x) ≥ η > 0 on V_l ∩ Ω. Since K_q ⊆ Δ, |P(q,h) − P(q,x)| ≤ ‖h − x‖_∞. So P(q,h) > 0 for ‖h − x‖_∞ < η.
  For good h, the open convex set H(h) ∩ Ω contains a.e. point of the convex open V_l ∩ Ω, hence all of it. ∎

**Lemma 27.5′ (vertex positivity at facet points; PROVED from N5 Thm 3.3).**
- *Hypotheses.* A permitted-tie realisation of an all-facing T on M_U, and (X_ik) for every facet F_k and every i ≠ k.
  (X_ik): a non-null set of x ∈ U with v_k·x < 0 and c_i(x) > 0. It holds whenever θ < θ_x(T): take x = h̄ − s𝟙 near a
  facet point h̄ with h̄_i > θ‖h̄‖, an off-band point. Then x ∈ U, v_k·x = −s, and x is strict.
- *Conclusion.* (VP_x), hence UVN(a), holds at every x ∈ relint F_k and every l with x_l > 0.

*Proof.*
- On relint F_k every positive coordinate l is a crossing coordinate (all-facing: h_k < 0, and both others cross;
  writeup Lemma 4.4).
- By N5 Thm 3.3, facet clause, there is a ball B ∋ x with c_l > 0 a.e. on B ∩ {h_l > 0}. The facet clause is: slab from
  N5 Prop 3.2 (outer collar), inner side from N5 Lemma 3.1 (VT). N7 checked it CORRECT for θ < θ_x and found no gap in
  that clause; the gap concerns only corner rays.
- Put x⁻ := x − s𝟙 with s small, so x⁻ ∈ B and x⁻_l > 0. Take a ball B₀ ∋ x⁻ inside B ∩ {h_l > 0}.
- For a.e. g ∈ B₀, e_l ∈ H(g) (c_l(g) > 0). So g ∈ B_q for |q − e_l| < r(g), and dominated convergence gives
  μ(B₀ ∖ D_{K_q}) → 0. This is N5 Lemma 2.2; the strictness R10b drew from the vertex minimiser is replaced by c_l > 0
  on B₀.
- An open convex cone missing x⁻ misses a half-ball of B₀, so x⁻ ∈ D_{K_q} on some V_l.
- Then P(q,x) ≥ P(q,x⁻) + s > s on V_l ∩ Ω. ∎

**Why nothing weaker suffices near the crossings.** At a crossing w = h(τ_c), w_c = 0, so every nearby facet point with
x_c > 0 is a band-c point for every θ > 0. `thresholds.py`: at ε = .3 the band fraction of the facet parameter interval
is 0.011 at θ = 0.01 (sup), and positive for every θ. So UVN(a) for world c near w can never come from off-band
strictness, and N15 uses it there:
- Step 0/1 at h(τ) for τ ↓ τ_c;
- Lemma M Step 4 at w₊.

### 2.3 N15's chain, step by step, under permitted ties

Notation as in the writeup §4. "Strict badness" means c_i < 0 where g_i < 0, which is never tied. "27.5′" means
UVN(a) at a relint facet point, available for θ < θ_x.

| Step (writeup / N15) | Sign uses | Under permitted ties |
|---|---|---|
| Prop 3.3 (a) K_q ⊇ K′; (b) Hausdorff continuity, joint continuity of P; (d) p\*⊙c | none / (BU) only | **unchanged** |
| Prop 3.3 (e) half-plane charts | vertex clause | **weak form** (e_i ∈ cl H for g_i > 0; strict for g_i < 0) |
| Lemma 4.4 (facet signs) | geometry of T | unchanged |
| Lemma 4.5 (chords; cluster lines genuine) | limits of signs, so weak anyway; "not ∝ 𝟙" needs only weak mixed signs (ĉ_l ≥ 0 on P, ≤ 0 on N) | **unchanged** |
| Lemma 4.6 (straight levels) | Lemma 4.5(b) at levels t ∈ I_g | **unchanged** |
| Lemma 4.7 (sandwich), Lemma 4.8 (caps) | none | **unchanged** |
| Lemma 4.9 UVN | (a) strict vertex minimiser at e_l; (b) strict badness | (b) **unchanged**; (a) **only via 27.5′** (θ < θ_x) |
| R10b §1, Lemma D (Γ_v, α_v, β_v; collar) | convexity only | **unchanged** |
| Lemma 4.10 = Cor PL2 (Lemma M Steps 2–4) | Step 4: (a₋)_c ≤ 0 by strict badness; (a₊)_c > 0 by UVN(a) at w₊ | **every θ, with a weak-sign replacement** (below); or via 27.5′ |
| Lemma 4.11 (no pinning) | UVN(a) at the crossing w for world j (V_j ⊆ Γ ∩ β); strict positivity of h(τ) on W∖{v_k} (geometry) | **via 27.5′** (w ∈ relint F_k, w_j > 0) |
| Thm 4.12 Step 0 | UVN(a) at h(τ) (A_τ ⊇ V_l); UVN(b) (B_τ ⊇ V_k) | (a) **via 27.5′**; (b) unchanged |
| Step 1 | UVN(a) at h(σ₁), h(σ₂) (G ≠ ∅); n_τ·(e_l − p\*) > 0 | **via 27.5′** |
| Step 2 (monotone) | pairwise intersections via V_j | **via 27.5′** |
| Step 3 (continuity) | none (convexity of Z) | **unchanged** |
| Step 4 (strict monotonicity, crossing values) | > 0 on the h_i > 0 side (UVN(a)); < 0 on the h_i < 0 side (UVN(b)) | **weak suffices on the positive side** (below); 27.5′ gives it anyway |
| Step 5, cluster clause | none | **unchanged** |
| Thm 4.13 (no sliding) | none | **unchanged** |
| Lemma 4.14 (rotation), 4.15, Prop 4.16 (regularity), Lemma 4.17 (two-slope), Prop 4.18 (blow-up), Cor 4.19 | none beyond Thm 4.12 | **unchanged** |
| Lemma 4.20 (edge box) | strict badness at coordinates a, b of A + λB | **unchanged** |
| Prop 4.21 (a) λ_{ik} > 0 | from Thm 4.12's n_τ·(e_i − p\*) > 0 | unchanged given Thm 4.12; **also for every θ** by N5 Lemma 4.2 (sign–rank: weak signs + Γ_k ≠ 0, which Cor 4.19 gives) |
| Prop 4.21 (b), (c) | unique clusters, Lemma 4.20 | **unchanged** |
| Prop 4.22 (T1 algebra), transposition c^σ(g) = σc(σg) | permutation invariance | **unchanged** (both norms are permutation invariant, so c^σ is a permitted-tie realisation with the same θ) |
| general all-facing pinching (R15 Thm 6.2 algebra) | algebra | **unchanged** |

**Weak-sign replacement in Lemma M Step 4 (PROVED, every θ, on M_U and wherever the charts of exterior gambles near w
are global half-planes {c·q > 0}).**
- With a₊ = λa₋ (λ > 0), a±·Q = 0 and Q ∈ Ω, we need a contradiction.
- (a₊)_c ≥ 0, because c_c(h₊ⁿ) ≥ 0 (weak sign, (h₊ⁿ)_c > 0).
- UVN(b) at w₋ for world c gives H(h₋ⁿ) ∩ V_c = ∅ for a.e. h₋ⁿ near w₋. In the limit {a₋·q > 0} ∩ V_c ∩ Ω = ∅: a point
  of it would lie in H(h₋ⁿ) for large n.
- If a₋·e_c ≥ 0, then the line {a₋·q = 0} through the interior point Q either has e_c on its open positive side, or
  passes through e_c. In both cases its open positive side meets every neighbourhood of e_c in Ω. So a₋·e_c < 0, i.e.
  (a₋)_c < 0 ≤ (a₊)_c, which contradicts a₊ = λa₋.
- So Cor PL2 needs **no** vertex positivity. Only Lemma 4.11's α-exclusion (a β-point V_j) does.

**Weak-sign replacement in Step 4 (CHECKED, every θ, given Steps 0–3 and 5 on the monotone pieces).**
- Non-constancy needs n·(e_i − p\*) ≥ 0 on the h_i > 0 side and < 0 on the other.
- The weak inequality follows from the cluster clause: the cluster line of h(τ) is λ_τ with orientation, and Lemma
  4.5(b) puts e_i in its closed positive side when h_i > 0.
- The strict side is UVN(b).
- Continuity then gives λ_{τ_i} = line(p\*, e_i).
- The cluster clause depends only on Step 5 and Lemma 4.5(b), not on Step 4, so the order is consistent.

### 2.4 The theorem

**Theorem 27.6 (PROVED).** Let T ⊆ Ω be all-facing in general position, p\* ∈ Ω, θ > 0, and the norm sup or Euclidean.
Suppose (X_ik) holds for every facet F_k and every i ≠ k; θ < θ_x(T) suffices. Then T has no permitted-tie realisation
at p\* on any U-domain M_U.

Consequently (Prop 27.4) no additive ranking with permitted NSI_θ ties, integrable envelopes, (LA), (S), (C), on M_U,
covers T.

For T1:
- sup norm: every θ ∈ (0,1);
- Euclidean norm: θ < √((κ²+1)/(κ²+2)), for every ε ∈ (0,1) and every interior target weighting.

*Proof.*
- Prop 27.4 gives the realisation. Reduce to p\* = u by p\*⊙c.
- Lemma 27.5′ supplies UVN(a) at every relint facet point and positive coordinate. With it, every row of the table in
  §2.3 holds, so writeup Thm 4.12, Thm 4.13 and Cor 4.19 give unique pivot chords, (PC) and (NS).
- Prop 4.21 gives crossing rows, corner equations and the box.
- Prop 4.22 (T1; transposition allowed, since c^σ is again a permitted-tie realisation) or the general pinching algebra
  gives the contradiction.
- Nothing in §§4.1–4.6 uses strictness of good-vs-silence except through UVN(a) (§2.3). ∎

*Scope.*
- The R10b ball conditions "inside the UVN balls at w (for j) and at w_± (for c)" are met by Lemma 27.5′. The w₊ one is
  not even needed (weak-sign replacement).
- Corner-ray vertex positivity, where N7 found the Euclidean gap θ ∈ [Θ_NT, θ_x), is never used: Steps 0–1 take
  σ₁ > 0 and τ ∈ (0,1); Thm 4.13 uses no UVN.
- The threshold can be read with U: (X_ik) asks only for strict x ∈ U beyond the plane of F_k. So
  θ_x(T,U) := min_{k,i} sup{x_i/‖x‖ : x ∈ U, v_k·x < 0} ≥ θ_x(T) also suffices.

### 2.5 Values

`thresholds.py` (NUMERICS against N5's closed forms, matching N7):

| ε | κ | θ_x sup | θ_x Euclidean | Θ_NT (not needed) | φ_j(w), Euclidean |
|---|---|---|---|---|---|
| 0.05 | 1.158 | 1 | 0.83706 | 0.83639 | 0.7568 |
| 0.10 | 1.333 | 1 | 0.85749 | 0.85519 | 0.8000 |
| 0.30 | 2.286 | 1 | 0.92821 | 0.91853 | 0.9162 |
| 0.60 | 5.500 | 1 | 0.98437 | 0.97714 | 0.9839 |
| 0.90 | 28.00 | 1 | 0.99936 | 0.99881 | 0.9994 |

φ_j(w) is the positive-coordinate ratio at a crossing. Below it, Lemma 4.11's β-point is supplied by off-band
strictness alone, but Steps 0–1 near the crossings still need Thm 3.3.

### 2.6 Domains non-adjacent near T (CHECKED)

R1 Prop 2.4(ii) and 2.5 used the strict vertex minimiser (R1 Lemma 1.5) to make the reach set a finite union of cones.
Under ties, replace it by the following.

**Lemma 27.7 (conic reach set without vertex facts; PROVED).** Let W := {h : R(h) ∩ Ω ≠ ∅}, and let Q be a countable
dense subset of Ω. Then W = ∪_{q∈Q} B_q, so W ≈ W°_Q := ∪_{q∈Q} D_{K_q} ∪ {h ≥ 0}∖0, an open cone. If E is open and
E ⊆ W a.e., then cone(E) ⊆ W°_Q a.e.

*Proof.*
- R(h) ∩ Ω is open, so if nonempty it contains some q ∈ Q, and then h ∈ B_q.
- A countable union of a.e. equalities is an a.e. equality.
- For the cone: (E ∖ W°_Q) is null, so t(E ∖ W°_Q) = tE ∖ W°_Q is null for each rational t > 0 (W°_Q is a cone).
- cone(E) = ∪_{t∈ℚ₊} tE, because E is open. ∎

Let Off := {g mixed : g_i > θ‖g‖ for some i}, a cone. Those g ∈ Off whose acceptance is in the advice range have R(g) ∋ e_i, so N ∩ Off ⊆ W a.e. Lemma
27.7 then gives cone(N) ∩ Off = cone(N ∩ Off) ⊆ W°_Q ⊆ Av a.e. Also D_T = B_{p\*} ⊆ W. So for K′ ⊆ ri T close to T:
- a.e. g ∈ D_{K′} ∩ Off has its acceptance in the advice range;
- a.e. g ∈ D_{K′} ∖ Off either has its acceptance in the advice range, or lies in no D_{K_q} (q ∈ Ω; as B_q ⊆ Av).

On the latter set put c(g) := −1 on the negative coordinates and 0 on the positive ones. These are admissible weak signs,
since all positive coordinates are band, and the chart is ∅, consistent with (BU).
- That every evaluable model accepts a mixed gamble is excluded by R10a Cor V1 in N5's form: anchoring of C_{e_k} or of directional vertex limits,
  N5 Prop 3.5, refereed CORRECT, needing (X_ik).
- {+,−} pairs are adjacent (R4 Thm A; d has the strict sign of g, since good-vs-bad is never tied).
- So non-adjacency near T gives half-plane charts {c(g)·q > 0} on D_{K′} with weak signs.
- N14 §3(iv) then turns K̂_q = co(K_q ∪ K′) into a permitted-tie realisation on M_{D_{K′}}, and Theorem 27.6 applies.

**Corollary 27.8 (CHECKED).** For θ < θ_x(T), no permitted-tie additive ranking covers T on any (LF) decomposable domain
(arbitrary open N) that is non-adjacent near T.

### 2.7 Beyond the threshold (open)

**What fails.** For Euclidean θ ∈ [θ_x(T1), 1), every point of U beyond the plane of F_k has all positive coordinates in
band. So (X_ik) can fail, and Lemma 27.5′ has no input.

**The escape it opens (CHECKED, local).** At a vertex e_l, let W be a directional limit of K_q (q → e_l). The local
requirements are:
- D_W accepts every off-band l-positive gamble whose acceptance is in the advice range (N5 §3.4(α));
- D_W rejects every gamble with h_l < 0 (β).

When (X_lk) fails, the off-band l-positive gambles of U all satisfy v_k·h > 0. So W = [e_l, v_k], with
D_W = {h_l > 0, v_k·h > 0}, meets both requirements. Then P_W(x) = 0 for every x ∈ F_k, and (VP_x) fails on all of F_k.

Pivot Steps 0–1 and Lemma 4.11's β-point then have no source. The realisation would have K_q accumulating at sets
containing v_k near e_l, i.e. pinning F_k near a vertex.

**Status.** CONJECTURE (unsupported either way): no permitted-tie realisation of T1 exists for any θ < 1.

The specific statement to prove is (VP) at band facet points without (X), for instance from the global chord structure:
- at facet parameters τ where some positive coordinate of h(τ) is off band, vertex positivity comes from strictness
  alone (`thresholds.py` gives the complementary band fraction);
- one would have to propagate them across the band arcs using concavity in τ.

I did not attempt this. The regime needs θ > 0.816, far from "negligible stakes".

**Not examined:**
- general (adjacent) decomposable domains under ties (N21/N23 under permitted ties);
- the charge version (writeup Cor 4.3) under ties.

---

## 3. Requested edits

**Writeup "The Contamination Triangle.tex":**
1. §5 preamble: replace "a closed conic neighbourhood N₀ ⊆ N of ∂D_T∖0 with P_{K″} > 0 on N₀" with "a compact
   neighbourhood N₀ ⊆ N of the compact set Σ of normalised facet, crossing and witness gambles, with P_{K″} > 0 on N₀;
   c₀ and r₁ small relative to its width (N27 Repair 27.1)". Add a remark citing Lemma 27.2 / Cor 27.3′ (the conic form
   of Lemma 5.2 holds at chart level).
2. §2.5 / Def 2.3: one sentence that (LF) is the open-set form and that M_U uses the explicit cone U.
3. §7.1 (permitted ties): replace "Whether the unconditional chain … has not been examined" with Theorem 27.6
   (θ < θ_x(T); T1: every θ ∈ (0,1) in sup norm; Euclidean θ < √((κ²+1)/(κ²+2))), Corollary 27.8, and the open regime
   (VP).
4. §7.1 forced/permitted bullet: delete the implied IBU threshold. (C) forces IBU for every θ (R1 Lemma 1.4 is
   guidance-free).

**START HERE:** in the 13-Oct strategy bullet, "open cone N" → "open set N" (the Glossary already says so).

**R10a §1:** the conic shrink is not available. Re-read Thm V/R/M with the cone on which acceptance is in the advice range taken from the reach set (R1 Prop
2.4–2.5 / Lemma 27.7). Not done here; not used by the main chain.

---

## 4. Status summary

| Item | Status |
|---|---|
| Inventory of N-uses (N12, N14, N15, N21, N23, R1, R10b, writeup) | CHECKED, §1.1 |
| Repair 27.1 (bounded collar replaces conic N₀) | PROVED |
| Lemma 27.2 (ray transfer of charts) | PROVED |
| Cor 27.3 (advice ranges differ along rays only in silence on thin-silence pairs; strict guidance) | PROVED |
| Cor 27.3′ (conic N21.2 at chart level) | PROVED |
| U-domain theorem unaffected by (i) | CONFIRMED (PROVED) |
| Non-adjacent corollary unaffected by (i) | CONFIRMED (PROVED) |
| Prop 27.4 (covering ⇒ permitted-tie realisation; IBU for every θ) | PROVED |
| Lemma 27.5 (UVN(a) ⇔ (VP)) | PROVED |
| Lemma 27.5′ (VP at relint facet points for θ < θ_x) | PROVED from N5 Thm 3.3 (refereed once, N7) |
| Weak-sign replacements (Lemma M Step 4: PROVED; pivot Step 4: CHECKED; λ > 0 via N5 Lemma 4.2: refereed in N7) | PROVED / CHECKED |
| **Theorem 27.6** (no permitted-tie realisation on M_U, θ < θ_x(T); T1 sup: all θ ∈ (0,1); Euclidean: θ < √((κ²+1)/(κ²+2))) | **PROVED** (one-author; needs a referee) |
| Lemma 27.7 (countable-union reach cone) | PROVED |
| Cor 27.8 (non-adjacent domains under ties, θ < θ_x) | CHECKED |
| Euclidean θ ∈ [θ_x, 1) (and the degenerate sup θ ≥ 1) | open; precise missing input (VP); CONJECTURE |
| Threshold values | NUMERICS (`thresholds.py`), matching N5/N7 closed forms |
| Auditor's N example: no conic neighbourhood; bounded collar exists | NUMERICS (`lf_example.py`) |

**Referee risk points.**
- Lemma 27.2 step 1: joint measurability of (q,g) ↦ 1[q ∈ R(g)].
- Lemma 27.5′: the claim that N5 Thm 3.3's facet clause needs only (X_ik), and in particular that N5 Prop 3.2's hull
  uses only strict points beyond F_k, which exist for θ < θ_x.
- The weak-sign Lemma M Step 4, and its reliance on global half-plane charts of exterior gambles (true on M_U and after
  the K̂ reduction).
- §2.6's assignment of c on all-band gambles that no evaluable model accepts.

## 5. Files (`n27py/`)

| File | Content | Result |
|---|---|---|
| `thresholds.py` (`.out`) | θ_x (sup, Euclidean; numeric vs closed form), Θ_NT, φ_j(w); band fraction of the facet for small θ | θ_x(sup) = 1; Euclidean matches √((κ²+1)/(κ²+2)) to 6 digits; band fraction > 0 for every θ |
| `lf_example.py` (`.out`) | auditor's N = {dist < e^{−‖g‖}}: no conic neighbourhood; norms of Σ; collar width | ray leaves N for t ≥ 4 (ρ = .01); Σ norms ⊂ [1.09, 3.58]; collar 0.0085 ⊆ N (0/20000 failures) |
