# N14: referee report on N12_notes.md (13 Oct 2026)

I did not write N12. I assumed nothing in it was correct until I had checked it.

**What I read.**
- Briefs: BRIEF.md–BRIEF6.md. BRIEF6 part (B) is the target.
- Background: R1 §§1–3 (Prop 2.1, 2.5, 3.1, Lemma 3.5, Thm 3.2); R4 Thm A, Thm B, Cor B1; R10b (Prop V, V1, Lemma FS, UVN, D, M, Thm PL, Cor PL2); R12's verdicts on those; R15 and R18 in full; N9.4 (the binary normal form, which is the U-domain: the evaluable models are the measurable subsets of U = D_{K′}).

**What I did.**
- Every step of N12 was re-derived by hand.
- Scripts rerun: `n12py/ode_check.py`, `twoslope_lp.py`, `twoslope_scaling.py`. All output reproduced exactly.
- New scripts in `n14py/`:
  - `curvature_check.py`: an independent symbolic check of the §5.2 curvature expansion, using a full C² ansatz for Λ⁻¹;
  - `edgebox_sanity.py`: Theorem 2.4 tested on an explicit U-domain realisation (described in §2.3).

**Verdicts.**
- **CORRECT**: the statement and proof stand.
- **CORRECT WITH REPAIR**: the statement stands after a local fix, which is given.
- **GAP**: the proof is incomplete.
- **FALSE**: the statement is wrong.
- **OVERSTATED**: the mathematics is right but the prose claims more than is proved.

Labels for my own additions follow the house rules: PROVED means a full proof is written here.

---

## 0. Summary table

| Item | Verdict | Reason (one line) |
|---|---|---|
| N12.1 Lemma 1.1, Props 1.2–1.4 (reduction to a credal family; Hausdorff continuity; p\* = u) | **CORRECT** (minor repair) | All steps check. The "null ties" in the converse of Prop 1.4 are *automatic* (§2.1), and the every-q statement follows without a limit argument |
| N12.2 Lemma 2.1 (weak chords, clusters) | **CORRECT** | Fubini, then open-set upgrades, then joint continuity. Valid for *every* mixed g |
| N12.2 Lemma 2.2 (level chords) | **CORRECT WITH REPAIR** | Each level set *contains* a separating chord, and may be fat. "Every level set is a straight chord" is false in general. Nothing downstream needs the strong form |
| N12.2 Lemma 2.3 (superadditivity) | **CORRECT WITH REPAIR** | Holds on int Δ only. The §0 summary drops "∩ int Δ" |
| **N12.3 Thm 2.4 (edge box)** | **CORRECT** | Re-derived. It uses only: the chart of each good gamble is a half-plane with strict signs; superadditivity of P; Fubini over (A, B, λ). Lemma FS is replaced by the strict-sign half-plane of A+λB. It survives in chart form on **every** decomposable domain with (LF) (§2.3). "Contains R15 Lemma 6.1" holds only *together with (PC)* |
| N12.4 Prop 2.5 (a)(b) (pivot dichotomy, tangency) | **CORRECT** | |
| N12.4 Prop 2.5 (c) (vertex pinning) | **CORRECT WITH REPAIR** | A uniform neighbourhood needs only the two endpoints of a sub-arc plus superadditivity. Say so |
| N12.4 Prop 2.6 (monotone pivot chords) | **GAP** | P(·,h+h′) ≥ 0 on S, and ≤ 0 on the negative side of ℓ″, is no contradiction (both can be = 0). It needs strict positivity on the positive sides. Used only in the §7 description |
| N12.5 Thm 3.1 ((PC)+(NS) ⇒ contradiction) | **CORRECT** (on the U-domain) | Every R15/R18 step is checked to use only chord lines. On general decomposable domains the box bridge needs (NA_w) (§3) |
| N12.6 Lemma 4.1 (two-slope form) | **CORRECT** | Re-derived, including the strip and orientation cases |
| N12.6 Lemma 4.2 (unique clusters) | **CORRECT** | |
| N12.6 Lemma 4.3 (concavity ⇒ projectivity; a × a′ conserved) | **CORRECT** | Lipschitz and BV regularity are *derived* from concavity, not assumed. Atoms of a″ are handled. Non-constancy is global on I because L_a is one constant |
| N12.6 Lemma 4.4 ((DD) ⇒ (NS)) | **CORRECT** | |
| N12.6 Thm 4.5 (no T1 realisation under (DD)) | **CORRECT** | On the U-domain, and more generally (§3). "(DF)+(ND) ⇒ (DD)" needs R15 Lemma 3.2 (Γ_k nonsingular). That holds for T1 |
| N12 §0 / N12.6 prose: "(DD) … one-sided directional derivatives continuous in the direction" | **OVERSTATED** | (DD) also requires D(·,h) to **take both signs**. First-order-flat (D ≡ 0) and half-flat (D = α[n·δ]₊) facets are *not* covered |
| §4 "what this excludes concretely" | **CORRECT WITH REPAIR** | Each instance needs the two-signed proviso |
| N12.7(a) (polygonal, local-homeomorphic vertex maps) | **CHECKED-level, citation gap** | The needed "local fundamental theorem" is for an *open family of lines with directions in an arc*, not all lines. Plausible, but needs a proof or exact citation. Also state that v_k(q) is the only vertex of K_q near v_k |
| N12.7(b) (C² dual charts ⇒ Möbius) | **CHECKED** | The curvature expansion was reproduced with a full C² ansatz (`curvature_check.py`). Hypotheses to state: Λ is well defined (unique clusters for all near-facet lines), C² on the *closed* facet segment (needed for (NS)), and w ≠ 0 |
| N12.8 Prop 6.1 (charges near a closed null set) | **CORRECT WITH REPAIR** | Existence of the interior Bayes minimiser is a hypothesis; null ties follow from a.e. uniqueness |
| **N12.C2** (arbitrary purely finitely additive parts) | **RESOLVED: PROVED here (§5.1)** | The small-carrier form of Yosida–Hewitt makes the splice argument work for *every* charge vanishing on μ-null sets. Dense carriers are irrelevant. This remains conditional on existence of interior Bayes minimisers (a part (A) issue) |
| N12.9 numerics | **Reproduced** | Exactly: 0 / 4.2e-4 / 2.2e-3 / 6.2e-3 / 5.2e-4; scaled 3.379, 3.470, 3.504; sympy residuals. They illustrate Lemma 4.3 (which is proved). They are not independent evidence for N12.C1 |
| §7 gap list (G1)–(G4), "equivalently, the only realisations still possible…" | **INCOMPLETE** | It omits (F3): D exists and is continuous but is flat or half-flat, which is (E3) itself. (G1) on arcs containing a crossing is already **excluded** by R10b Cor PL2 (§5.2). Isolated (DD)-failures are excluded unless degenerate (§5.3) |
| N12.C1 as formulated | **Correctly labelled, but mis-scoped** | For T1 it is logically equivalent to non-realisability, so it carries no extra structure. "Would give the full additive core (B)" overclaims: that holds only on (H2″)-type domains (§3), and for charges only given existence. A non-vacuous form is proposed in §6 |

**Measure-theoretic audit (§4).**
- Every a.e./Fubini passage is valid.
- No "for each q, a.e. g" is turned into "for a.e. g, all q" without justification.
- No silent regularity is used.
- No boundary-prior coherence is used.
- No Bayes-at-index selection is used.

**Net.** N12's main new theorem, Thm 4.5, is correct and is a genuine advance on R15 Thm 6.2:
- (DF) is replaced by the weaker (DD);
- (NA_w) is automatic on the U-domain;
- Lemma FS is not needed.

The additive core (B) for T1 is **not settled**. The precise remaining gap is stated in §6.

---

## 1. Setting

**The U-domain.**
- The evaluable models are the measurable X ⊆ U = D_{K′}, modulo null sets. U never contains both f and −f, so no evaluable model gives contradictory advice.
- On a pair {f,−f} meeting U, with f its orientation in U, the advice range is {+,0}: X advises choosing g in {g,h} (f = g−h) iff f ∈ X, and otherwise gives no advice. On pairs {f,−f} with f ∉ U and −f ∉ U, every evaluable model gives no advice. U is pointed, so each pair has at most one orientation in U.
- (LF) at D_T holds with any open cone N with ∂D_T∖0 ⊆ N ⊆ U. This is possible because U ⊇ cl D_T∖0, as K′ ⊆ ri T.
- This is N9.4's binary domain.

**What is automatic here.**
- B_{e_i} = U ∩ {g_i > 0} = D_{conv(K′∪{e_i})}, so vertex models are coherent. CCIBU then supplies (LA), (S), (C) from interior Bayes uniqueness and coherence, with nothing needed at boundary priors.
- K_q ⊇ K′ is 2-dimensional, so (FD) holds and hence there are no d-faces: (NA_w) is automatic.
- (R2) is forced by coverage. T is undominated, so it is Bayes at some prior (R1 Lemma 1.3(b)), and that prior is interior (R1 Prop 2.6).

---

## 2. Item-by-item

### 2.1 N12.1 (reduction). CORRECT.

**Lemma 1.1.**
- (a) D_{K_q} ∖ cl U is open and null, hence empty. So D_{K_q} ⊆ int cl U = U, which gives K_q ⊇ K′.
- (b) Intersection of coherent cones.
- (c) Injectivity of K ↦ D_K.

**Prop 1.2.**
- For each q the tie set is null by (R1), at *every* q. So B_{q_n} → B_q in measure.
- R1 Prop 3.1: K ↦ 1_{D_K} is a continuous injection of a compact space into L¹, hence a homeomorphism onto its image. This gives Hausdorff continuity.
- The Lipschitz bound is elementary.

**Prop 1.3.**
- c̃ = p\*⊙c amounts to reweighting the worlds' penalties by p\*_i. So it is a strictly guiding additive field on the same domain.
- B̃_{q̃} = B_{N(q̃⊙p\*)}, and N is a face-preserving projective bijection.
- Correct. (The same reweighting also works on general decomposable domains, applied to both c and c′.)

**Prop 1.4.**
- *Forward.* The set {(q,g) : 1[q·c(g) > 0] ≠ 1[P(q,g) > 0]} is jointly measurable (c is measurable, P is continuous), and each q-section is null. Fubini makes a.e. g-section null.
- *Converse. Repair (simplification).* The hypothesis "null ties" is redundant, and no limit in q is needed.
  - For good g, Lemma 2.1(a) gives P(q,g) = 0 on ℓ(g) ∩ int Δ, P ≥ 0 on H(g), and P ≤ 0 off cl H(g), for **every** q.
  - So, for every q, {g : q ∈ ℓ(g)} ⊆ {g : P(q,g) = 0} ∪ Bad, which is null.
  - Likewise B_q △ {P(q,·) > 0} ⊆ {P(q,·) = 0} ∪ Bad, which is null, for every q.
- Measurability of the normal: {P(q_m,·) > 0} is measurable for a countable dense set {q_m}, and it determines H(g). Fine.

**Claim "merely measurable c creates no extra freedom".** Correct in the precise sense that everything is determined by q ↦ K_q, together with (★).

### 2.2 N12.2 (chords).

**Lemma 2.1. CORRECT.**
- (a) For each q, {P(q,·) = 0} is the boundary of a closed convex cone, hence null. Fubini gives, for a.e. g, a null q-tie set. The rest is open-set algebra: an open set a.e. inside an open half-plane lies in it, and the complement is handled symmetrically.
- (b) Good g are dense, and chords of mixed good g separate vertices, so cluster lines exist in a compact space. The limit normal is not ∝ 𝟙 (weak mixed signs and unit length).
- Joint continuity transfers ≥ 0 / ≤ 0 to the closed sides. A cluster line may meet Δ only at a vertex. Harmless.

**Lemma 2.2. CORRECT WITH REPAIR.**
- What is proved is: for each level c ∈ (min g_i, P_{K′}(g)) there is a line ℓ_c with {P > c} ⊆ open positive side and {P < c} ⊆ open negative side.
- Hence {P = c} ⊇ ℓ_c ∩ int Δ. But {P = c} may have interior (plateaus), so "every level set is a straight chord" (N12.2, §0) is false as stated.
- Lemma 4.1 uses only the separation form. N12.7(a) proves the stronger form under its homeomorphism hypothesis (§2.7).
- Also write "every **mixed** g ∈ U" in the first bullet of N12.2.

**Lemma 2.3. CORRECT WITH REPAIR.** The inclusion is H(g) ∩ H(g′) ∩ int Δ ⊆ H(g+g′) (as proved). It does not extend beyond Δ.

### 2.3 N12.3: Theorem 2.4 (the key new claim). CORRECT.

**Re-derivation.**
1. The ratio condition A_b B_a < |A_a||B_b| is equivalent to the nonemptiness of the interval of λ with A_b/|B_b| < λ < |A_a|/B_a. On it, (A+λB)_a < 0 and (A+λB)_b < 0.
2. *Fubini.* For each fixed (B, λ), A ↦ A + λB is a translation, so {(A,B,λ) : A+λB bad} is null. Hence for a.e. (A, B) with A, B good, a.e. λ in the interval makes A+λB good. One such λ suffices.
3. Suppose q₀ ∈ H(A) ∩ H(B) ∩ [e_a, e_b]. The set H(A) ∩ H(B) is open in aff Δ, so O = H(A) ∩ H(B) ∩ int Δ ≠ ∅ accumulates at q₀.
4. On O, P(·,A) > 0 and P(·,B) > 0 a.e. (good A, B, null q-ties). By concavity and homogeneity in g, P(·,A+λB) ≥ P(·,A) + λP(·,B) > 0 a.e. on O.
   - If A+λB ∉ U, this contradicts P ≤ P_{K′} ≤ 0.
   - Otherwise O is a.e. inside H(A+λB), hence inside it. So q₀ ∈ cl H(A+λB) = {c(A+λB)·q ≥ 0}.
5. But c(A+λB)_a, c(A+λB)_b < 0, so c(A+λB) < 0 on the whole closed edge. Contradiction.

**What is used.**
- Half-plane charts with strict signs for A, B and A+λB.
- Superadditivity of P(q,·) at interior q.
- Fubini.

**What is not used.**
- No regularity of q ↦ K_q beyond continuity.
- No coherence at edge priors. The edge enters only through the affine extension of c, and H(g) is determined by its trace on int Δ, because the line separates two vertices.
- No Lemma FS. The strict-sign half-plane of A+λB does Lemma FS's job, gamble by gamble.

**Sanity test (`n14py/edgebox_sanity.py`).**
- Take M_i = [e_i, (1−θ)e_i + θu]. Then c_i(g) = min(g_i, (1−θ)g_i + θu·g) has the strict sign of g_i on U (since u·g > 0 there), and K_q = conv(K′ ∪ Σq_iM_i) is a genuine U-domain realisation (a gauge mixture).
- Over 300 000 draws for each θ ∈ {0.2, 0.6, 0.95}: 0 of 2306 ratio-satisfying pairs violate the box. 6999 ratio-failing pairs do have overlapping edge charts, so the test is sensitive.

**Two wording repairs.**
- "This contains R15 Lemma 6.1." What Theorem 2.4 replaces is Lemma 6.1 step 5 (Lemma FS) and the (NA_w)-dependent step 4. The inequalities Λ_{ab} ≤ 1 themselves need, in addition, the identification of the witnesses' edge charts with the cluster half-planes at p\*. That is (PC), as in Thm 3.1 step 6.
- "Needs neither (DF), (ND) nor (NA_w)": true on this domain, where (NA_w) is vacuous. See §3 for general domains.

**Extension (PROVED here): the chart form holds on every decomposable domain with (LF).**
- *Statement.* Under the axioms, for a.e. pair (A, B) with the stated signs and ratio, R(A) ∩ R(B) ∩ [e_a, e_b] = ∅, where R is the actual chart (wedges allowed).
- *Proof.* Steps 3–4 use only:
  - that R(g) is relatively open in Δ;
  - that R(g) ∩ int Δ = {P(·,g) > 0} a.e. for good g (R1 Thm 3.2(ii));
  - that R(g) ⊆ {c·q > 0} or R(g) ⊆ {d·q > 0}, with c and d strictly sign-preserving (R1 Prop 2.1), or R(g) = ∅.
- That every evaluable model accepts A+λB is excluded because A+λB is not nonnegative (R10b Cor V1, whose vertex coherence is forced by the axioms, R1 Lemma 1.5). ∎

### 2.4 N12.4.

**Prop 2.5(a). CORRECT.**
- B_{p\*} = D_T a.e. is a statement at the specific prior p\*, which is legitimate.
- Inner and outer good gambles near h ∈ ∂D_T both have positive measure.
- If neither the inner nor the outer cluster passes through p\*, then P ≥ 0 and P ≤ 0 near p\*.

**Prop 2.5(b). CORRECT.**

**Prop 2.5(c). CORRECT WITH REPAIR.**
- The neighbourhoods on which P(·,h) ≡ 0 depend on h. Take h₁, h₂ ∈ A and h₀ strictly between them, and intersect three neighbourhoods.
- Superadditivity gives P(q,·) ≥ 0 on cone(h₁, h₂).
- L_{h₀} ∩ {m·h₁ ≥ 0, m·h₂ ≥ 0} = {v_k}, since h₁ and h₂ are independent mod 𝟙 (𝟙 ∉ v_k^⊥).

**Prop 2.6. GAP.**
- On S, P(·,h) ≥ 0 and P(·,h′) ≥ 0 only weakly, because the positive sides of cluster chords carry only P ≥ 0. So P(·,h+h′) ≥ 0 on S.
- On the open negative side of ℓ″, P(·,h+h′) ≤ 0. These are compatible: both say P = 0 on S ∩ (negative side of ℓ″).
- What is actually proved is: either n″ ∈ cone(n, n′), or P(·,h) = P(·,h′) = P(·,h+h′) = 0 on a nonempty open sector at p\*.
- Repair: add the hypothesis "P(·,h) > 0 on a dense subset of the positive side near p\*" (true under (DD)), or state the dichotomy.
- §7 cites Prop 2.6 for monotonicity of ψ_k in the non-(DD) regime. That citation is therefore unproved.

### 2.5 N12.5: Theorem 3.1. CORRECT (on this domain).

**Item 3 (crossing rows).**
- The unique cluster at w = w_{ik} is a two-sided limit, so e_i ∈ ℓ_w. On the 2-plane v_k^⊥, the functional vanishes at ℝw, which gives λ_{ik}h_i.
- Weak signs give λ_{ik} ≥ 0.
- The collinearity argument for λ > 0 is correct and avoids UVN.

**Item 4 (nonsingularity).** (PC) gives Γ_k h ≠ 0 on the connected set relint F_k. Rank 1 would give a single chord, which contradicts the two crossing chords line(p\*, e_i) ≠ line(p\*, e_j).

**Item 6 (box).**
- Uniqueness of the cluster at A plus compactness give uniform convergence of the chords of good A′ → A.
- The conditions "H(A′) ∩ H(B′) meets the open edge" and the ratio condition are open. So a positive-measure set of pairs contradicts Theorem 2.4.
- Strict signs at the b-crossings follow from the chord line(p\*, e_b) (R18 §5 repair).

**Item 7.** This is R15 Thm 6.2 Steps 1–6, refereed CORRECT in R18. Only chord lines enter.

**Transfer between priors.** (PC) and (NS) are invariant under the projective reindexing of Prop 1.3, which maps lines to lines and acts linearly on Γ.

### 2.6 N12.6. CORRECT, with one overstatement.

**Lemma 4.1.** Re-derived.
- Finiteness and positivity of c at s > 0.
- Openness of {D ≷ s}, by continuity in δ.
- Disjoint level lines are parallel.
- Orientation. If ν′ = −ν, then {D > s′} ⊆ {ν·δ > c} ∩ {ν·δ < −c′} = ∅, a contradiction.
- Equal orientation with distinct offsets forces D ≡ s′ on a strip avoiding 0, which contradicts homogeneity.
- The subsequence depends on s, but each conclusion (D = s on L_s) is subsequence-free.

**Lemma 4.2.** Correct.

**Lemma 4.3.** Re-derived.
- Step 2 needs only α > 0, not a lower bound.
- Step 3: concavity of a·δ on a basis in C_J gives local Lipschitz regularity and a vector Radon measure a″ with a″(E) ∈ −C_J\*. Lebesgue–Besicovitch differentiation plus continuity of n gives a″ = −n m_a.
- Step 4: the Leibniz rule with a continuous BV factor, and a × n = 0 (atoms included).
- Step 5:
  - L_a = 0 ⇒ n′ = 0 a.e. ⇒ n constant on all of I. This is excluded by the two crossing chords, and L_a is a single constant on I, so n is nowhere locally constant.
  - L_b ≠ 0 too, because β > 0. Then β/α is constant, m_a = m_b = 0, and a is affine.
- Affine on every segment, plus homogeneity, gives linearity on v_k^⊥.

**Lemma 4.4.** Correct.
- Upper bound by concavity along [r, h₀] and continuity of the two-slope formula.
- Diagonal cluster from the facet-j side.
- Nonsingularity of Γ_k from item 4.

**Thm 4.5.** Correct.

**Overstatement (§0 first bullet; N12.6 last paragraph).**
- §0 says "No realisation … in any family whose facet support functions have one-sided directional derivatives at p\* that are continuous in the direction". (DD) also contains "D(·,h) takes both signs". That clause is essential:
  - α, β > 0 are used in Lemmas 4.1 (step 5), 4.2 and 4.3;
  - it excludes first-order-flat facets (D ≡ 0, i.e. (E3)) and half-flat facets (D = α[n·δ]₊, or −β[n·δ]₋).
- So "(DF) is removed" is right, but (ND) is replaced by two-signedness, not removed.
- "(DF)+(ND) ⇒ (DD)" needs γ_k(h) ≠ 0 at **every** h ∈ relint F_k. That is R15 Lemma 3.2 (Γ_k nonsingular when |C_k| ≥ 2), which holds in T1. Cite it.

### 2.7 N12.7.

**(a) CHECKED-level, citation gap.**
- The level-set step is sound: v_k is a local homeomorphism, so {v_k·g = c} near q₀ is an arc, and Lemma 2.2's separation then forces ℓ_c through q₀ and equal to the arc.
- But G (gambles minimised at v_k(q₀)) gives lines with **normals in an open arc** of the normal cone. That arc has length < π, so not all directions are available.
- The classical local fundamental theorem is for maps sending *all* segments of a domain to segments. The restricted-direction version is plausible: Pappus and harmonic-quadrangle configurations can be drawn with all lines in a narrow direction arc. But it must be proved or cited exactly.
- Also add the hypothesis that v_k(q) is the only vertex of K_q near v_k. Otherwise P(q,h) = v_k(q)·h can fail.
- The "vertex splitting" and "rank-one" paragraphs are sketches, and should be labelled as such.

**(b) CHECKED.**
- `n14py/curvature_check.py` uses X = s + yX₁ + y²X₂ and Y = yw + y²Y₂ along y = m(x − x₀). The O(m) term of X′Y″ − Y′X″ equals N12's brace exactly.
- The pair 2s′w′ = s″w, s′w″ = s″w′ forces A′ = A²/2 (A = s″/s′), hence s is Möbius. The case w′ = 0 gives s″ = 0, which is also Möbius.
- The direction needed is Λ⁻¹(q\*) ⊆ C_q: the chord of L passes through q ⇒ P(q, g_L) = 0 ⇒ L is tangent. So Λ⁻¹(q\*) is an arc of the convex curve C_q, and fat zero sets do no harm.
- Hypotheses to state explicitly:
  - Λ is well defined near F_k\*, i.e. unique clusters for every line near the facet segment (so uniqueness, the hard half of (PC), is assumed);
  - Λ⁻¹ is C² near the **closed** segment, so that (NS) at the corners also follows;
  - w ≠ 0.
- With these, (PC) and (NS) follow, and the flat case is excluded *in this smooth class*.

### 2.8 N12.8. CORRECT WITH REPAIR; N12.C2 is resolved (§5.1).

**Prop 6.1.**
- Weak (G) forces ν_i ≥ 0, so both Yosida–Hewitt parts are ≥ 0.
- Strict (G) off S forces ℓ_i > 0 a.e. off S.
- Splicing keeps ν^p fixed, because |ν^p|(U ∖ N_η(S)) = 0, and strictly lowers the countably additive term.

**Repairs.**
1. The proposition is about a Bayes model *if one exists*. With a nonzero ν^p, R_q need not minimise. If X beats R_q on the ν^p-term, the splices X_η = X on N_η(S) and R_q elsewhere converge in value, and no minimiser exists at q. (B) assumes existence. Whether coverage forces it is a part-(A) question.
2. "Assume R_q has null ties" is derivable. If the tie set Z is non-null, re-splicing a Bayes model on Z ∖ N_η(S) (non-null for small η) changes no term. That gives two distinct Bayes models, contradicting a.e. uniqueness.

### 2.9 N12.9. Reproduced.

**Exact outputs.**
- LP minimum violations: 0 (projective), 4.18e-4, 2.22e-3, 6.22e-3 (ε = .05, .2, .5), 5.15e-4 (linear angle).
- Scaling: 3.379, 3.470, 3.504.
- Sympy: Möbius residual 0. For s = x + x³, 3(1−6x²)/√(3x²+1).

**Caveats.**
- The s = x + x³ residual is of the second equation, after w has been fitted from the first. Fine.
- The LP bounds α, β ∈ [1, 50]. The normalisation is legitimate because violations scale with α, β.
- These numerics illustrate Lemma 4.3, which is proved. They are not independent evidence for N12.C1, whose content is precisely the non-(DD) regime.

---

## 3. General decomposable domains with (LF): what changes

**(i) Local theory at p\* transfers verbatim.**
- R1 Lemma 3.5: there is a convex neighbourhood Q″ of p\* on which, for a.e. g ∈ U′ = D_{K′} (R1 Prop 2.5), R(g) ∩ Q″ = {c(g)·q > 0} ∩ Q″. No wedges occur near p\*.
- So Lemmas 2.1–2.2 (on Q″), Prop 2.5, Lemmas 4.1–4.4 and items 3–5 of Thm 3.1 (crossing rows, nonsingularity, corners) hold. Their chord lines are those of the global vectors c(g).
- Hence (DD) ⇒ (PC) + (NS) on every decomposable domain with (LF).

**(ii) The edge box transfers in chart form (§2.3).**

**(iii) The bridge needs non-adjacency.**
- The box contradiction needs the witnesses' *actual* charts to contain the edge prior q₀ predicted by their pivot chords.
- With an adjacent pair whose advice range is {+,0,−}, R(A′) = {c > 0, d > 0}, and the d-line can cut q₀ off.
- So on general domains the box step needs (NA_w) on neighbourhoods of the six crossings, at priors in conv(p\*, edge). That is R15's (E4). By R4 Thm B, the escape requires degenerate K_p ⊆ g^⊥ on the d-faces.

**(iv) Exact reduction under non-adjacency (PROVED here).**
- *Hypothesis.* Suppose a.e. pair meeting U′ is non-adjacent ((H2″)_{U′}; implied by (FD), R4 Thm B).
- *Claim.* The restricted family K̂_q := conv(K_q ∪ K′) satisfies every hypothesis of N12.1 with U := U′. Hence all of N12 §§2–4, in particular Thm 4.5, apply unchanged.
- *Proof.*
  - B_q ∩ U′ ≈ D_{K̂_q} (R1 Prop 2.5).
  - For g ∈ U′, P_{K′}(g) > 0, so P_{K̂_q}(g) > 0 ⇔ P_{K_q}(g) > 0.
  - Charts of g ∈ U′ are half-planes {c(g)·q > 0} ∩ int Δ with strict signs (R4 Cor B1; (H0)_{U′} holds by R10b Cor V4). Every evaluable model accepts g only when g ≥ 0 (chart Δ, which is vertex-respecting).
  - K̂_{p\*} = conv(T ∪ K′) = T.
  - K̂_q ⊇ K′.
  - Hausdorff continuity holds.
  - Near p\*, P_{K̂_q}(h) = P_{K_q}(h) for h near ∂D_T, so (DD) for K and for K̂ coincide.
  - In Thm 2.4, A + λB ∉ U′ gives P_{K̂} ≤ 0, as required. ∎

**(v) Advice that every evaluable model gives.**
- Every evaluable model accepts f only when f is nonnegative (V1).
- Every evaluable model gives no advice on {f,−f} only when f ∉ U′ and −f ∉ U′ (for a.e. g ∈ U′, acceptance of g is in the advice range, R1 Prop 2.4).
- Neither affects the arguments.
- The advice range {+,0,−} matters only through adjacency, as in (iii).

**(vi) Vertex coherence.** It is automatic on the U-domain. On general domains it is forced by the axioms (R1 Lemma 1.5). Either way, no boundary-prior coherence is used.

**Conclusion for general domains.**
- Theorem 4.5 holds under (DD) + (NA_w). This strictly improves R15 Thm 6.2's (DF)+(ND)+(NA_w).
- It holds under (DD) alone whenever pairs meeting U′ are non-adjacent, e.g. under (FD).

---

## 4. Audit of a.e./Fubini, regularity, boundary priors, selections

| Passage | Type | Status |
|---|---|---|
| Prop 1.2 | fixed q, null tie set at that q (every q by (R1)), dominated convergence | valid |
| Prop 1.4 (forward) | joint measurability, then Fubini: a.e. g, a.e. q | valid |
| Prop 1.4 (converse) | every q, directly from Lemma 2.1(a) (§2.1) | valid; simpler than stated |
| Lemma 2.1(a) | Fubini to "a.e. g, a.e. q", then open-set and continuity to "a.e. g, **all** q" | valid. This is the only upgrade of that kind, and it is justified |
| Lemma 2.1(b), 2.2, 4.1–4.4 | deterministic (every h), via cluster limits of good gambles | valid |
| Lemma 2.3, Thm 2.4 | Fubini over (A, B, λ) via translations | valid |
| Prop 2.5(a) | (R2) at the specific prior p\* | valid |
| Thm 3.1 step 6 | uniform chord convergence ⇒ a positive-measure set of pairs | valid |
| Prop 6.1 | splice; ∩_η N_η(S) = S null | valid |

**Silent regularity.** None in the proofs.
- Hausdorff continuity is automatic.
- Lemma 4.3's Lipschitz and BV regularity are derived from concavity.
- N12.7's hypotheses are explicit.
- The §7 blow-up route flags "K_q Lipschitz at p\*" as a proviso. Correct.

**Boundary priors.** Edge priors occur only via the affine extension of c(g), which is determined by int Δ. No coherence at boundary priors is used anywhere. Vertex coherence is automatic (§1).

**Selections.** Nothing assumes that the selection is Bayes at its index. (R1)–(R2) concern Bayes models, which are forced by the axioms (R1 Lemmas 1.3–1.4; CCIBU for the converse).

---

## 5. Additions by the referee

### 5.1 N12.C2 is true (PROVED)

**Lemma Y (small carriers).**
- *Statement.* Let ν ≥ 0 be a purely finitely additive bounded charge, and μ a finite countably additive measure, on the same σ-algebra. For every ε > 0 there is a measurable F with μ(F) < ε and ν(F^c) = 0.
- *Proof.*
  1. For each n let λ_n = ν ∧ nμ in ba, i.e. λ_n(A) = inf_{B⊆A}[ν(B) + nμ(A∖B)].
  2. Then 0 ≤ λ_n ≤ nμ, so λ_n is countably additive (continuity at ∅ is inherited from μ).
  3. Also λ_n ≤ ν. Since ν is purely finitely additive, λ_n = 0.
  4. Pick B_n with ν(B_n) + nμ(B_n^c) < 2^{−n}, and put E_n = B_n^c. Then μ(E_n) < 2^{−n}/n and ν(E_n^c) < 2^{−n}.
  5. Let F_N = ∪_{n≥N} E_n. Then μ(F_N) < 2^{1−N}, and ν(F_N^c) ≤ ν(E_n^c) < 2^{−n} for every n ≥ N, so ν(F_N^c) = 0. ∎

**Theorem C2.**
- *Statement.* Let the penalties be arbitrary bounded charges ν_i vanishing on μ-null sets, on the U-domain (or for each kind of advice on any decomposable domain). Assume strict (G), weak (G), and that at an interior q a Bayes model X exists and is a.e. unique. Then:
  - ℓ_i > 0 a.e., where ℓ_i is the density of ν_i^c;
  - the countably additive rule R_q has null ties;
  - X = R_q a.e.
- *Proof.*
  1. Weak (G) gives ν_i ≥ 0, hence ν_i^c, ν_i^p ≥ 0.
  2. Apply Lemma Y to |ν_1^p| + |ν_2^p| + |ν_3^p| (purely finitely additive, being a sum of such): for every ε there is F_ε with μ(F_ε) < ε that carries all three.
  3. *Strictness.* If ℓ_i = 0 on a non-null Z, then removing errors on Z ∖ F_ε, which is non-null for small ε, changes neither part of L_i. That contradicts strict (G).
  4. *Null ties.* Re-splicing X on (tie set) ∖ F_ε contradicts a.e. uniqueness.
  5. *Main step.* Suppose μ(X △ R_q) = 3δ > 0. Take ε = δ and Y = (X △ R_q) ∖ F_δ, so μ(Y) ≥ 2δ. The splice X′ (R_q on Y, X elsewhere) is in the domain, has unchanged ν^p-terms (E_i(X′) △ E_i(X) ⊆ Y ⊆ F_δ^c), and a countably additive term lower by ∫_Y |q·c| dμ > 0. Contradiction. ∎

**Consequence.**
- For (B), purely finitely additive parts can never change an existing interior Bayes model, whatever their carriers (dense, near ∂D_T, anywhere). They cannot mimic kinks.
- BRIEF6's Yosida–Hewitt worry reduces entirely to **existence** of interior Bayes minimisers. That belongs to part (A): a charge can, in principle, destroy existence at q ≠ p\* (§2.8 repair 1). Whether coverage under (S) forces existence when penalties are charges is open there.

### 5.2 Vertex pinning along a crossing arc is impossible (PROVED, from R10b Cor PL2)

**Claim.** On the U-domain, or any decomposable domain with no adjacent pairs near ∂D_T, (G1) cannot occur on an open arc A ⊆ relint F_k that contains a crossing w of F_k.

**Proof.**
1. By Prop 2.5(c), with the repair in §2.4, there is an open O ∋ p\* such that, for q ∈ O, v_k ∈ K_q and P(q,h) ≥ 0 for all h ∈ cone(h₁, h₂) ⊆ A, with w strictly inside.
2. Choose the R10b balls U ⊂ Ũ around w with F_k ∩ cl Ũ ⊆ cone(h₁, h₂), inside the UVN balls. R10b §1 then gives O ⊆ Γ_{v_k}, and v_k ∈ K_q gives O ⊆ α_{v_k}.
3. Pick j with w_j > 0. UVN(a) gives V_j ∩ int Δ ⊆ Γ ∩ β.
4. G = int conv(O ∪ V_j) ⊆ Γ, by convexity of the charts of U⁺ gambles (R10b Thm PL proof).
5. There are no d-faces, so Cor PL2 (refereed CORRECT, R12) gives G ⊆ α or G ⊆ β. But G meets both. ∎

N12 §7 lists (G1) as "not excluded here". Only pinning arcs containing no crossing remain open.

### 5.3 No isolated (DD)-failures, unless degenerate (PROVED)

**Claim.**
- *Setting.* Let h(τ) be an affine section of relint F_k, and suppose (DD) holds at h(τ) for all τ ∈ (τ₀−η, τ₀+η) ∖ {τ₀}.
- *Conclusion.* D(·,h(τ₀)) exists, is continuous and has the two-slope form. It is two-signed, i.e. (DD) holds at τ₀, unless on one side n is constant and α or β tends to 0.

**Proof.**
1. On each side interval I_±, the constant L_a of Lemma 4.3 is either ≠ 0, so a is affine with |a(τ₀±)| > 0 (an affine a vanishing at τ₀ would make n constant), or = 0, so n ≡ n_± and α, β are positive concave functions. In both cases the one-sided limits D_±(δ) = lim_{τ→τ₀±} D(δ, h(τ)) exist and are two-slope.
2. *Lower bound.* Midpoint concavity of φ_t = P(p\*+tδ, ·)/t gives liminf_t φ_t(h(τ₀)) ≥ ½[D(δ, h(τ₀−s)) + D(δ, h(τ₀+s))]. Letting s → 0 gives ≥ ½(D₋ + D₊).
3. *Upper bound.* The bound of Lemma 4.4, applied from each side, gives limsup ≤ min(D₋, D₊).
4. Hence D₋ = D₊, and this common value is the limit. ∎

**Consequence.** A seam with distinct projective chord maps on its two sides, which would add free parameters like an extra facet of a hexagon, is impossible at an isolated ray. Any (DD)-failure set on a facet must be non-isolated (perfect, or containing an arc), or be degenerate in the stated sense.

---

## 6. Justified current status of the additive core (B) for T1, and the remaining gap

### PROVED (N12 Thm 4.5, with §§3 and 5 here)

**Theorem.** There is no strictly guiding additive realisation of T1 (or of any all-facing triangle in general position, at any interior p\*) with:
- every interior Bayes model a.e. unique and coherent, and T Bayes at p\*;
- (LF) at T;
- penalties given by integrals, or by arbitrary bounded charges vanishing on null sets, given existence of interior Bayes minimisers (Theorem C2);
- (DD) at p\* on all three facets: one-sided directional derivatives of the facet support functions that exist, are continuous in δ, and take both signs;

on either of the following:
- (a) any decomposable domain on which pairs meeting U′ are non-adjacent. This includes the U-domain (binary domain), every domain whose advice ranges near ∂T have two elements, and every system with full-dimensional interior K_q;
- (b) any decomposable domain with (LF), if (NA_w) holds near the six crossings.

### Further PROVED exclusions
- Vertex pinning along an arc containing a crossing (§5.2; non-adjacent domains).
- Isolated (DD)-failures (§5.3).
- Sliding edges at corners whose adjacent facets satisfy (DD) (Lemma 4.4).

### CHECKED exclusions
- Polygonal families with local-homeomorphic vertex maps, pending the restricted-direction projective-geometry lemma.
- C² transversally nondegenerate dual charts. These cover flat facets in that class.

### Precise remaining gap
On a non-adjacent domain, a realisation of T1 must have a facet F_k and a set Z_k ⊆ relint F_k of rays where (DD) fails. Z_k must be non-isolated, or degenerate in the sense of §5.3. At each h ∈ Z_k, one of the following holds:
- **(F1) oscillation:** lim_{t↓0} P(p\*+tδ, h)/t fails to exist for some δ;
- **(F2) direction-discontinuity:** the limit exists for all δ but is discontinuous in δ;
- **(F3) flatness:** the limit exists and is continuous but is not two-signed. Either D ≡ 0 (first-order-flat, (E3)), or D = α[n·δ]₊ or −β[n·δ]₋ (half-flat). This includes pivot degeneracy P(·,h) ≡ 0 near p\*. On an arc, that is possible only if the arc contains no crossing (§5.2).

In addition:
- sliding edges can occur only at corners adjacent to such a facet;
- on adjacent domains, (E4) is added: d-faces with K_p ⊆ g^⊥ cutting the witness charts;
- for charges, existence of interior Bayes minimisers is part (A).

N12 §7's list omits (F3) except pinning. It also wrongly keeps pinning on crossing arcs.

### Proposed reformulation of N12.C1 (CONJECTURE)
As stated, C1 for T1 is equivalent to the theorem itself. A non-vacuous, falsifiable version is the following.

**C1′.** For *every* interior polygon target T and every realisation on a non-adjacent domain, at p\*, on each facet of D_T with at least two crossings, there are a rate m(t) ↓ 0 and a sequence t_j ↓ 0 such that P(p\*+t_jδ, h)/m(t_j) → G(δ,h), locally uniformly in δ, with G continuous and two-signed for each h.

**What C1′ would give.**
- The argument of Lemma 4.1, without homogeneity, makes G a ridge φ_h(n(h)·δ) with φ_h strictly increasing.
- The argument of Lemma 4.2, along the subsequence, then gives unique pivot clusters.
- Projectivity would still need a version of Lemma 4.3 for non-linear φ_h. That is the remaining analytic step. It is *not* supplied by the numerics.

**Status of C1′.**
- It holds in every known realisation: gauge mixtures, including the explicit binary-domain family of §2.3, satisfy (DF)+(ND).
- It is the precise point at which the "blow-up" route of N12 §7 must be made rigorous. That route also needs Lipschitz control of K_q at p\* or a substitute, for compactness in δ.

---

## 7. Requested edits to N12 (priority order)

1. §0 and N12.6: state that (DD) includes two-signedness. Replace "(DF) is removed" by "(DF) is removed; (ND) is replaced by two-signedness". Remove "any family whose … derivatives are continuous".
2. §7: add (F3), flat and half-flat with continuous D. Strike (G1) on crossing arcs (§5.2). Note §5.3. Drop the reliance on Prop 2.6, or repair it (§2.4).
3. N12.C1: "full additive core (B)" → "(B) on non-adjacent domains, for integral penalties or charges with existing Bayes minimisers". Add the non-vacuous form C1′ or an equivalent.
4. N12.8/C2: replace C2 by Theorem C2 (§5.1). State existence of interior Bayes minimisers as the remaining (A)-issue.
5. N12.3: replace "contains R15 Lemma 6.1" by "replaces Lemma FS and (NA_w) in R15 Lemma 6.1; with (PC) it yields Λ_{ab} ≤ 1". Note the chart form on general decomposable domains.
6. N12.2: "level sets contain separating chords (possibly fat)"; "every mixed g"; "∩ int Δ" in superadditivity.
7. Prop 1.4: null ties are automatic.
8. Prop 2.5(c): the two-endpoint uniformity remark.
9. N12.7(a): give the restricted-direction projective lemma (proof or citation) and the "unique nearby vertex" hypothesis. Mark the splitting and rank-one paragraphs as sketches.
10. N12.7(b): list the hypotheses (well-defined Λ, C² on the closed segment, w ≠ 0). Note that uniqueness of clusters is assumed there.
11. "(DF)+(ND) ⇒ (DD)": cite R15 Lemma 3.2 for nonsingularity.

---

## 8. Files (`n14py/`)

| File | Purpose | Result |
|---|---|---|
| `curvature_check.py` | O(m) curvature term of Λ⁻¹(y = m(x−x₀)), full C² ansatz; solve A′ = A²/2 | difference from N12's brace = 0; A = −2/(x + C) |
| `edgebox_sanity.py` | Thm 2.4 on the explicit binary-domain gauge realisation c_i = min(g_i, (1−θ)g_i + θu·g) | 0 violations in 2306 ratio-satisfying pairs; 6999 ratio-failing pairs overlap (test is sensitive) |
