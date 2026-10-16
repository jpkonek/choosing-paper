# N27 referee report: compact collar, ray transfer, and the unconditional theorem under permitted ties

14 Oct 2026. Independent referee. I did not write N27, and I treated nothing in it as correct until I had re-derived it.
I use the Glossary of START HERE throughout.

**Read.**
- BRIEF8, the START HERE Glossary, BRIEF4–BRIEF7.
- The writeup "The Contamination Triangle.tex": §§2–5 in full, and §7.1.
- N27 in full, with `n27py/`.
- Against these: N21 in full; N23 in full; N5 in full; N7 in full.
- The parts of N12, N15, N18 and N20 that bear on (LF)/N and on sign uses.
- R1 §§1–3 (Lemmas 1.1–1.5, Props 2.1, 2.4–2.8, 3.1); R10b §§1–3 (setting, Prop V, V1, V2, UVN, Lemma D, Lemma M);
  N2 Lemmas 0–2 and Thm B; N1 Prop 2.3.

**Verdict scale.** CONFIRMED / CONFIRMED WITH REPAIR (the statement stands after the local fix given) / GAP / WRONG.

**Scripts (`n27ref_py/`, evidence only).**
- `thresholds_ref.py` (`.out`): a symbolic derivation (sympy) of the Euclidean threshold and its maximiser; θ_x for
  the sup norm and the Euclidean norm; Θ_NT; θ_x(T,U) for two choices of U.
- `escape_check.py` (`.out`): the open regime of N27 §2.7 at ε = 0.3, run on 2·10⁶ directions.
- I reran N27's own `lf_example.py` and `thresholds.py`. Their outputs are identical to `n27py/*.out`.

---

## 0. Verdict table

| N27 item | Verdict | One-line reason |
|---|---|---|
| §1.1 inventory of uses of N | **CONFIRMED** | My own inventory (§1) finds the same uses and no others. Every use concerns gambles near a fixed compact set of boundary gambles, at bounded norm. No step rescales a gamble inside N₀, takes a ray through N₀ or uses homogeneity of advice ranges |
| Repair 27.1 (compact collar N₀ᵇ replaces the conic N₀) | **CONFIRMED** | Constants re-derived: c₀ < η/√3, and r₁ chosen after c₀. One wording addition (§1.4): (PC) on general domains is asserted for h ∈ cone(Σ) via linearity of Γ_k; the cluster clause is proved only near Σ, which is all that is used |
| Lemma 27.2 (ray transfer of charts) | **CONFIRMED** | Measurability, Fubini and the open-convex step all re-derived. No guidance is used |
| Cor 27.3 (advice ranges can differ along rays only by × and by silence on thin-silence pairs) | **CONFIRMED** | Exact form in §2.2. It needs strict guidance; under permitted ties (a) fails, as N27 says |
| Cor 27.3′ (conic N21.2 at chart level) | **CONFIRMED, and slightly stronger** | Its three conclusions give the full N21.2 form R(g) ∩ C = {c(g)·q > 0} ∩ C (§2.3) |
| §1.5 (M_U and the non-adjacent corollary are unaffected by (i)) | **CONFIRMED** | U is explicit. R1 Prop 2.5 needs only that N is open |
| Prop 27.4 (covering ⇒ permitted-tie realisation; IBU for every θ) | **CONFIRMED** | R1 Lemma 1.4 uses no guidance (§3.1). The θ < 1 / θ < 1/√3 caveat of BRIEF4, N5 and N7 (§1 and caveat 5) is superseded |
| "UVN(a) at relint facet points is the only tie-sensitive input" | **CONFIRMED** | My own pass through the writeup's §4 chain (§3.2). Two further changes are harmless: Prop 3.3(c) (vertex models coherent) fails under ties but is unused, and R10b Prop V/V2 are not used on M_U |
| Lemma 27.5 (UVN(a) ⇔ (VP_x)) | **CONFIRMED** | |
| Lemma 27.5′ (VP at relint facet points from N5 Thm 3.3, facet clause) | **CONFIRMED** | Re-derived through N5 Prop 3.2, Lemma 3.1 and Lemma 2.2 (N2 Lemmas 1–2). It uses only (X_lk) for the same facet k, which is the facet clause N7 found CORRECT for θ < θ_x |
| N7's corner-ray gap is unused | **CONFIRMED** | Every UVN(a) call is at h(τ), τ ∈ (0,1), at a crossing, or at w± ∈ relint F_k (list in §3.4) |
| Weak-sign Lemma M Step 4 (PROVED) | **CONFIRMED** | Re-derived. It is redundant once 27.5′ is available |
| Weak-sign pivot Step 4 (CHECKED) | **CONFIRMED (CHECKED)** | Redundant: Steps 0–1 need UVN(a) anyway |
| **Theorem 27.6** | **CONFIRMED** | Exact statement in §6 |
| Thresholds (sup: all θ ∈ (0,1); Euclidean: θ < √((κ²+1)/(κ²+2))) | **CONFIRMED** (recomputed symbolically) | New: the Euclidean value is the maximum of x_l/|x| over the whole half-space {v_k·x ≤ 0}, so θ_x(T1,U) = θ_x(T1) for every U (§3.5) |
| §2.4 Scope: θ_x(T,U) ≥ θ_x(T) also suffices | **CONFIRMED, but void for T1** | Equality holds for every U (§3.5) |
| Lemma 27.7 (countable-union reach cone) | **CONFIRMED** | |
| Cor 27.8 (non-adjacent domains under ties) | **CONFIRMED at CHECKED level, with two wording repairs** | §4. The half-plane form of non-adjacent charts for the advice range {+,0,−} under weak signs needs one extra line, supplied there |
| §2.7 the open regime and (VP) | **CONFIRMED WITH REPAIR** | (VP) is the right missing statement. Repairs: "(X_lk) fails" must read "(X_lk) is not automatic"; the escape W = [e_l,v_k] violates K_q ⊇ K′ and must be W′ = co(K′ ∪ {e_l, v_k}); state the conjecture norm by norm (§5) |
| §1.4 recommendations; §3 requested edits | **CONFIRMED** | Plus the additions in §7 below |

**Overall: CONFIRMED.** No step of N27's proved chain fails. Both auditor repairs are closed.
- **Repair (i).** It is closed with no change to (LF).
- **Repair (ii).** The unconditional main theorem holds under permitted ties below θ_x: every θ ∈ (0,1) in the sup
  norm, and Euclidean θ < √((κ²+1)/(κ²+2)) (> √(2/3)) for T1.
- **Euclidean window.** In the window [θ_x, 1) the theorem still holds for every ranking that leaves a non-null set of
  band points beyond each facet plane untied. The open case is a tie placement that ties all of them.

---

## 1. Repair 27.1: independent inventory of every use of N₀ and of conic neighbourhoods

Method:
- I grep-searched N21, N23, N12, N15, N18/N20 (as cited), CHECK_REPORT and the writeup for N₀, N, "conic",
  "cone(", "homogen", "rescal", "ray", "scale" and "dilat".
- I then read each hit in context.
- "Bounded-local" means the property is needed only for gambles in a neighbourhood of a fixed compact Σ ⊆ ∂D_T∖0.

### 1.1 Uses of N₀ or N (general decomposable domains: N21, N23, writeup §5)

| # | Place | Gambles involved | Rescaling, ray or homogeneity? | Verdict |
|---|---|---|---|---|
| 1 | N21 §1 / writeup §5 preamble: N₀ closed conic nbhd, P_{K″} > 0 on N₀ | definition | conic only in the definition | replaced by N₀ᵇ |
| 2 | N21.2 = writeup Lemma 5.2: "for a.e. g ∈ N₀" no R(−g), no d-face, half-plane chart where K_q ∩ K″ ≠ ∅ | pointwise in g. N23 §3 made the proof pointwise: (1.1), Thm B, P_{K″}(g) > 0 | none | bounded-local |
| 3 | N21.4 item 1 (with the N23 repair): local Lemma 2.1 at levels c with h − c𝟙 ∈ int N₀ | h(τ) − c𝟙 with \|c\| ≤ c₀, τ ∈ [0,1] | **shifts** along 𝟙, not rescalings | bounded-local |
| 4 | N21.4 items 2–4, Lemma 2.3 with r₁ | levels f(q) for q ∈ B₁ | none. Rescalings in §§5–6 are of q (p\* + tδ), never of g | bounded-local, given \|Ψ\| < c₀ on B₁ × [0,1] |
| 5 | N21.4 item 5 (c-clusters at h(τ), h(τ)_i < 0) | good g_m → h(τ) | none | bounded-local |
| 6 | N21.4 item 6 / N23 §4.6 (no sliding): r ∈ int N₀ | normalised corner ray r and r − t𝟙 | none | bounded-local |
| 7 | N21.4 item 8 / Cor 4.19: Γ_k extended **linearly** to v_k^⊥ | defined from h(τ) | homogeneity of the *linear map* Γ_k, not of advice ranges | the cluster clause is proved near Σ only; see §1.4 |
| 8 | N21.6 Step 1: witness balls around A_s → w′, B_s → w; chart-form box (N14 §2.3) | balls shrinking to the two b-crossings | none | bounded-local. The limits must be in Σ in the normalisation used (for T1: (−β, 0, 1) and (1, 0, −β), the w/κ form) |
| 9 | N21.6 Step 1: "no advice that every evaluable model gives on N (V1)" | g in the witness balls | none | bounded-local |
| 10 | N21.6 Steps 3–4: N21.2 and P_{K″}(g_m) > 0 for cut gambles | near w\* | none | bounded-local |
| 11 | N21.6 Step 7: test gambles h = w\* − δ𝟙 + ηe_b ∈ N; edge forcing (R1 Prop 2.8) on non-null subsets of small balls | δ, η ↓ 0, so h → w\* | none | bounded-local |
| 12 | N21.7(a),(c),(d); N21.9(iii); R23.4: acceptance in the advice range on {h_b > 0}, {v_k·h > 0} | cones D_{K_q} | conic, but **derived** from B_q ≈ D_{K_q}, not from N | no N used |
| 13 | R23.1 Step 1: R10b ball U around w = h(τ_c), U ⊆ int N₀, F_k ∩ cl Ũ ⊆ cone h([σ₁,σ₂]) | ball around one crossing | "homogeneity then gives K_q ⊆ W_{v_k}(Ũ)": homogeneity of m·(·), the R10b §1 decomposition h = w″ + (v_k·h)𝟙 | bounded-local |
| 14 | R23.1 Step 2: N21.2 for good h ∈ U⁻ | U⁻ ⊆ U | none | bounded-local |
| 15 | R23.2 Steps 4–5; R23.3 (U_η → w) | balls at crossings | none | bounded-local |
| 16 | N21.9(i)–(ii) (with N23 §7.4): Lemma M on int conv(O ∪ V_j) | U around a crossing | none | bounded-local |
| 17 | R10b imports: Prop V (ball B ⊆ N around w with w_i = 0); UVN (B₀ ⊆ N); Lemma D; Lemma M Steps 1–3 | single balls | Lemma M Step 1 uses homogeneity of m·w′ only | bounded-local |
| 18 | writeup Def. 2.3 (LF); §2.5 (M_U: "any open N with ∂D_T∖0 ⊆ N ⊆ U") | — | — | already in open form |

### 1.2 Uses of U on M_U (N12, N15, writeup §4)

| Place | What is used | Verdict |
|---|---|---|
| Prop 3.3, Def. 3.2 | c is defined on all of the explicit open cone U | no N |
| Lemma 4.6 (levels), I_g = (min g_i, P_{K′}(g)) | g − t𝟙 ∈ U: a shift; U is a cone, so this holds at every scale anyway | no N |
| Lemma 4.11 (nopin) | "by homogeneity K_q lies in the wedge W": homogeneity of m·(·) | no N |
| Lemma 4.20 (edge box) | A + λB ∉ U ⇒ P ≤ P_{K′} ≤ 0 | no N |
| UVN, Lemma D, Lemma M | balls inside U | no N |
| N15 line 170 "x ∈ N" | on M_U, N = U | no N |

### 1.3 Check of the repair's constants

Facts:
- Σ is compact.
- Its norms lie in [a, b] ⊂ (0,∞). For T1 at ε = 0.3: [1.092, 3.577]; the endpoints are the w/κ crossings and
  the corner rays.
- N is open and contains Σ.

Choices, in this order (no circularity):
1. η > 0 with {dist(·,Σ) ≤ η} ⊆ N, and with P_{K″} > 0 on that collar. Possible because P_{K″} > 0 on Σ, by N23 §1.
2. The R10b shrinking (off −cl D_T, off {h ≤ 0}). It keeps an open set containing Σ, since Σ ∩ (−cl D_T) = ∅ and
   Σ ∩ {h ≤ 0} = ∅ (K ⊆ int Δ).
3. c₀ < η/√3, so that ‖c𝟙‖₂ < η.
4. r₁ so small that K_q ⊇ K″ (N21.2) and |Ψ_k(q,τ)| < c₀ on B(p\*, r₁) × [0,1]. This uses joint continuity of P,
   uniformly on the compact [0,1], and Ψ(p\*, ·) = 0 on [0,1].
5. Shrinking r₁ never invalidates a downstream statement. Every statement is "on B₁" or "outside B₁", and in N21.6(ii)
   the claim a\* ∉ B₁ only gets weaker.

**Verdict on Repair 27.1: CONFIRMED.**

### 1.4 One wording point (not a gap)

Writeup Thm 5.3 asserts "(PC) and (NS) hold" on general domains. The cluster clause of (PC) ("every cluster line of h
∈ relint F_k is {Γ_k h·(q − p\*) = 0}") is proved there only for h near Σ.
- Everything downstream uses it only at Σ: crossing rows at w_{ik}, the box witnesses and the N21.6 margins.
- If the full conic clause is wanted, it follows from Cor 27.3′ (charts on B₁ are ray-invariant for a.e. (g,t)),
  because cluster lines on B₁ are limits of chart lines.
- Suggested wording: "(PC) for h ∈ Σ, extended to cone(Σ) by linearity of Γ_k".

---

## 2. Lemma 27.2 and Corollaries 27.3, 27.3′

### 2.1 Lemma 27.2: CONFIRMED

1. *Joint measurability (N27's own risk point).* R(h) = ∩_{a ≠ acc(h), a ∈ A(h)} {q : q·(ℓ(h,a) − ℓ(h,acc h)) > 0}.
   - Each set {(q,h) : q·φ(h) > 0} with φ measurable is product-measurable, since (q,h) ↦ q·φ(h) is Carathéodory.
   - The case split over the finitely many advice ranges is a measurable partition.
   - The map (q,g,t) ↦ (q, tg) is a submersion for t > 0, so it pulls null sets back to null sets, and the
     composition is Lebesgue-measurable. It preserves H.
2. *Sections.* For fixed (q,t) the g-section is B_q △ t⁻¹B_q ⊆ (B_q △ D′) ∪ t⁻¹(B_q △ D′), with D′ a cone. This is
   null. Only a.e. q is needed.
3. *Fubini* gives, for a.e. (g,t), that R(g) ∩ Ω and R(tg) ∩ Ω agree a.e.
4. *Equality.* Both sets are relatively open and convex. If x ∈ A ∖ cl B, a neighbourhood of x in A misses B, which is a
   non-null difference. So the closures agree, and A = int cl A for open convex A. The empty case is covered by the same
   argument.

The proof uses no guidance at all, so it holds under permitted ties.

### 2.2 Cor 27.3: CONFIRMED. The brief's question

Is it proved that advice ranges differ along a ray only in whether silence is in them, and only where the silence region
has empty interior? **Yes, under strict guidance**, in this exact form.

For a.e. mixed g and a.e. t > 0:
- *Acceptances.* + ∈ A(tg) ⇔ + ∈ A(g), and − ∈ A(tg) ⇔ − ∈ A(g).
  - Proof: an orientation whose acceptance is in the advice range has R(h) ∋ e_l (l ∈ P(h)), so R(h) ∩ Ω ≠ ∅. One that no evaluable model accepts has R(h) = ∅.
- *Acceptance by every evaluable model.* Every evaluable model (effectively) accepts tg ⇔ every evaluable model (effectively) accepts g. By V1 this never happens on mixed pairs of a
  covering ranking.
- *Silence.* 0 ∈ A(tg) ≠ 0 ∈ A(g) is possible only if S(g) ∩ Ω = S(tg) ∩ Ω has empty interior, i.e. lies in a line.
  - The only possible change is {+,0,−} ↔ {+,−} (modulo ×) at a pair with advice range {+,0,−} and a thin silence cell.
  - {0} ↔ {0} necessarily, since S = Ω.
  - {+,0} keeps silence: S = {c·q ≤ 0} ∩ Ω has interior because c has strict mixed signs.
  - {+,0} ↔ {+} is impossible, since a {+,0} chart misses a neighbourhood of e_k (k ∈ N(g)).
- *×.* Whether × is in the advice range may change arbitrarily. It is invisible (R1 Prop 2.1).
- *Advice range {×} alone.* It occurs only on a null set (LA). Its preimage under dilation is null.

The example after the proof (same advice range, different c̃ ∝₊ c) is right: penalty vectors do not transfer.

The closing paragraph says near-facet g keep silence along rays, because S(g) ⊇ a half-disc of B₁. This needs a
unique cluster near p\* ((PC), from (TS) or N15). Without (TS) it is not established, but nothing uses it. Label it
CHECKED under (TS).

### 2.3 Cor 27.3′: CONFIRMED, with a strengthening

*Passage from "a.e. (g,t)" to "a.e. point of cone(int N₀ᵇ)".*
- Let E be the good set in int N₀ᵇ × (0,∞): N21.2 holds at g, and Lemma 27.2 holds for g and −g at (g,t).
- Its image under the diffeomorphism (g,t) ↦ (tg,t) has full measure in {(g′,t) : g′/t ∈ int N₀ᵇ}.
- For g′ ∈ cone(int N₀ᵇ), the t-fibre {t : g′/t ∈ int N₀ᵇ} is open and nonempty.
- So for a.e. g′ some t works. ✓

*No d-face.* d has the strict mixed sign of g, so it is nonconstant on aff Δ. Points near p ∈ F(g′) with d < 0 < α have
β = α − d > 0, so they lie in R(−g′) ∩ C, which is empty. ✓

*Strengthening.* The three conclusions already give the c-form of N21.2. For g′ with advice range {+,0,−}:
- {α > 0, d < 0} ⊆ R(−g′) misses C;
- {α > 0, d = 0} = F(g′) misses C;
- hence {α > 0} ∩ C ⊆ {d > 0}, and R(g′) ∩ C = {c(g′)·q > 0} ∩ C.

So the full conic N21.2 holds for a.e. g′ ∈ cone(int N₀ᵇ), with its own vector c(g′).

### 2.4 §1.5: CONFIRMED

- On M_U the only cone used is U.
- In R1 Prop 2.5, "N ⊆ W° a.e. ⇒ N ⊆ int cl W°" needs only that N is open.
- int cl W° is an open cone, because W° is a finite union of open cones.

---

## 3. Theorem 27.6 (permitted ties)

### 3.1 Prop 27.4 and "R1 Lemma 1.4 never uses guidance": CONFIRMED

Lemma 1.4(i):
- LDG thm:kkm (valid for preorders; it needs only (LA) and (S)) gives U_L = C_L under (C).
- Lemma 1.3(c) (an interior Bayes model is undominated) uses only additivity and p_j > 0.

Lemma 1.4(ii):
- Two distinct kinds of advice in {+,0,−,×} always differ in the acceptance of g or of −g.
- The X_F are splices of evaluable models, so they lie in the domain.
- The radial-Fubini contradiction uses only that each X_F is a.e. a cone.
- I checked the case a = +, b = −, where the −Z part also lies on the ray through θ. The argument survives:
  - (X_∅)_θ misses Z_θ, hence is null;
  - (X_Z)_θ ⊇ Z_θ, hence is co-null;
  - so Z_θ is co-null, and X_{Z∩{|h|<1}} has section ≈ (0,1).

No ranks are compared anywhere. So (BU) holds at every interior q, for every θ and either norm.

Consequence: BRIEF4's caveat "(C) forces IBU only for θ < 1 (sup), θ < 1/√3 (Euclidean)", repeated in N5 (SH_θ) and
in N7 §1 and caveat 5, is superseded. The results of N5 and N7 that assumed IBU in that range are therefore
unconditional on it.

The other two inputs:
- (TP): Lemma 1.3(b) (Lyapunov; no guidance) and N1 Prop 2.3 (strict badness only). ✓
- Prop 3.3: (a), (b), (d) verbatim. (e) holds in the weak form, since c_l ≥ 0 gives e_l ∈ {c·q ≥ 0} = cl H(g)
  (c ≠ 0 has a negative entry).
- (c) fails under ties: the e_i-Bayes model is not determined on τ_i. I verified that (c) is used nowhere in §4 of the
  writeup.

### 3.2 Where strictness of good-vs-silence enters the writeup §4 chain (my own pass)

| Step | Sign use | Under permitted ties |
|---|---|---|
| Lemma 4.4 (signs), Lemma 4.8 (caps), Lemma 4.17 (two-slope), Prop 4.22 algebra | none | unchanged |
| Lemma 4.5(a),(b) | (b)'s vertex clause is a limit of signs of c | weak signs suffice. "Not ∝ 𝟙" needs only weak mixed signs |
| Lemma 4.6 (levels), Lemma 4.7 (sandwich) | Lemma 4.5(b) at levels in I_g | unchanged |
| Lemma 4.9 UVN(b) | strict badness; on M_U silence is in the advice range of every pair, so V1 is not needed | unchanged |
| **Lemma 4.9 UVN(a)** | strict good-vs-silence at e_l, used as R10b's "strict vertex minimiser" | **the only tie-sensitive input** |
| R10b Lemma D | convexity | unchanged |
| Lemma 4.10 (PL2 = Lemma M Steps 2–4) | Step 4: (a₊)_c > 0 via UVN(a) at w₊ | UVN(a) via 27.5′, or the weak-sign replacement (§3.3) |
| Lemma 4.11 (nopin) | UVN(a) at w for j (the β-point); h(τ) > 0 on W∖{v_k} is geometry | via 27.5′ (w ∈ relint F_k, w_j > 0) |
| Thm 4.12, Steps 0, 1, 2 | UVN(a) at h(τ), h(σ₁), h(σ₂), τ, σ ∈ (0,1) | via 27.5′ |
| Thm 4.12, Steps 3, 5, cluster clause | none | unchanged |
| Thm 4.12, Step 4 | > 0 side via Step 1; < 0 side via UVN(b) | unchanged given Step 1 |
| Thm 4.13 (no sliding), Lemma 4.14, 4.15, Prop 4.16, 4.18, Cor 4.19 | none beyond Thm 4.12 | unchanged |
| Lemma 4.20 (edge box) | strict badness of c(A + λB) at a, b | unchanged |
| Prop 4.21(a) λ_{ik} > 0 | Thm 4.12's n_τ·(e_i − p\*) > 0 (or N5 Lemma 4.2 with (PC) in place of (DF)) | unchanged |
| Prop 4.21(b),(c) | unique clusters | unchanged |
| Transposition c^σ(g) = σc(σg) | the band is permutation-invariant in both norms; U, u and T1 are σ-invariant; (X_{ik}) for c^σ is (X_{σi,σk}) for c | unchanged |
| Prop 3.3(c), R10b Prop V, V2 | vertex coherence | **not used** on M_U |

This agrees with N27 §2.3 row by row.

### 3.3 Lemma 27.5, Lemma 27.5′ and the weak-sign replacement: CONFIRMED

**Lemma 27.5.**
- |P(q,h) − P(q,x)| ≤ ‖h − x‖_∞, since K_q ⊆ Δ.
- For good h, {P(·,h) > 0} ≈ H(h) ∩ Ω.
- An open convex set containing a.e. point of the convex open V_l ∩ Ω contains all of it. ✓

**Lemma 27.5′.** Re-derived through N5. Fix x ∈ relint F_k and l with x_l > 0; then l ∈ C_k (all-facing).
- *The outer slab (N5 Prop 3.2, w_l > 0 case).* c_l > 0 a.e. on {−c′ < v_k·y < 0} near x. Its inputs:
  - N2 Lemma 2 (vertex pull): needs only e_l ∈ R(x₀), i.e. c_l(x₀) > 0. On M_U, R = {c·q > 0}.
  - N2 Lemma 1(a),(b) (transport of tied points along (e_l, p\*]): no strictness.
  - one strict point x₀ ∈ U with v_k·x₀ < 0, i.e. **(X_lk), for the same facet k**.
- *The inner side (N5 Lemma 3.1 with Lemma 2.2).* Inner h dominate slab centres h − σ𝟙. Strict badness only.
- *The facet clause of Thm 3.3.* These two give c_l > 0 a.e. on B ∩ {h_l > 0} for a ball B ∋ x. N7 §2 found this
  clause CORRECT for θ < θ_x. The GAP N7 found is the corner-ray outer clause, which is a different clause.
- *Then:* x⁻ = x − s𝟙 ∈ B; dominated convergence at e_l on a ball B₀ ∋ x⁻ where c_l > 0; the half-ball argument gives
  x⁻ ∈ D_{K_q} on V_l; finally P(q,x) = P(q,x⁻) + s > s. ✓
- *(X_lk) holds for θ < θ_x.* The point x = h̄ − s𝟙, with h̄ ∈ F_k, h̄_l > θ‖h̄‖, is open-off-band, lies in U, and
  has v_k·x = −s. ✓

**Weak-sign Lemma M Step 4.**
- UVN(b) at w₋ gives {a₋·q > 0} ∩ V_c ∩ Ω = ∅. A point q there would have ĉ(h₋ⁿ)·q > 0 for large n.
- The line {a₋ = 0} passes through the interior point Q. If a₋·e_c ≥ 0, its open positive side meets every
  neighbourhood of e_c in Ω. So (a₋)_c < 0 ≤ (a₊)_c, which contradicts a₊ = λa₋. ✓
- On M_U the charts of exterior gambles are the global half-planes H(h), as required.

### 3.4 N7's corner-ray gap is genuinely unused: CONFIRMED

UVN(a) is called only at the following points, all in relint F_k with the relevant coordinate positive:
- h(τ) with τ ∈ (0,1) (Step 0);
- h(σ₁), h(σ₂) with 0 < σ₁ < σ₂ < 1 (Step 1);
- h(τ) with τ ∈ (0,τ_j) or (τ_i,1) (Step 2);
- the crossing w = h(τ_c) for world j (nopin);
- w₊ for world c (Lemma M).

Corner rays enter only Thm 4.13, Cor 4.19 (affine extension of a to [0,1]) and the corner equations (NS). None of these
uses UVN. Anchoring (N5 Prop 3.5) and V1 are not used on M_U.

### 3.5 Thresholds (recomputed; `thresholds_ref.py`)

**Euclidean norm (symbolic).**
- On F_1 = cone{r₁₂, r₃₁}, f(t) = h₃/|h| has a single stationary point t\* = (κ−1)/(κ(κ+2)) ∈ (0,1).
- The point is h ∝ (−1, −1/κ, κ + 1/κ). It lies in relint F_1: v₁·h = 0, v₂·h, v₃·h > 0.
- f(t\*)² = (κ²+1)/(κ²+2) exactly. The corner value is (κ+1)²/((κ+1)² + 2), i.e. Θ_NT, which is smaller.
- So θ_x = √((κ²+1)/(κ²+2)) = √(1 − v_{kl}²/|v_k|²).
- θ_x² − 2/3 = (κ−1)(κ+1)/(3(κ²+2)) > 0, so θ_x > √(2/3) for every ε. ✓

**Sup norm.** θ_x = 1, attained on an open arc of F_k near the corner where l is the only positive coordinate (arc
fraction 0.37–0.50 of the parameter interval). So (X) holds for every θ < 1. For θ ≥ 1 every mixed problem is band.
So "every θ ∈ (0,1)" is exactly the range in which the band is a proper subset of the mixed problems. ✓

| ε | κ | θ_x (sup) | θ_x (Euclidean) | closed form | Θ_NT | θ_x(T,U), s = .9 / .99 |
|---|---|---|---|---|---|---|
| 0.05 | 1.1579 | 1 | 0.837056 | 0.837056 | 0.836386 | 0.837056 / 0.837056 |
| 0.10 | 1.3333 | 1 | 0.857493 | 0.857493 | 0.855186 | same |
| 0.30 | 2.2857 | 1 | 0.928214 | 0.928214 | 0.918532 | same |
| 0.60 | 5.5000 | 1 | 0.984374 | 0.984374 | 0.977140 | same |
| 0.90 | 28.000 | 1 | 0.999364 | 0.999364 | 0.998813 | same |

N27's values (0.837 / 0.928 / 0.999) and N5/N7's closed forms are reproduced.

**New observation (PROVED).** The Euclidean maximiser is the normalised projection of e_l onto the plane v_k^⊥, and it
lies in relint F_k. So it maximises x_l/|x| over the **whole** half-space {v_k·x ≤ 0}, not just over F_k. Hence:
- θ_x(T1,U) = θ_x(T1) for every U. N27's "θ_x(T,U) ≥ θ_x(T) also suffices" is true but gains nothing for T1.
- For Euclidean θ ≥ θ_x, **no gamble at all** with v_k·x < 0 (whether or not its acceptance is in the advice range, in any domain) is off-band at l. Then
  (X_lk) can come only from the ranking's choice not to tie some band points.
- Numerically (`escape_check.py`): max x₃/|x| = 0.92807 over 2·10⁶ random directions with v₁·x < 0, against
  θ_x = 0.92821.

---

## 4. Lemma 27.7 and Cor 27.8

**Lemma 27.7: CONFIRMED.**
- R(h) ∩ Ω is open, so if it is nonempty it contains a point of the countable dense Q.
- A countable union of a.e. equalities is an a.e. equality.
- t(E ∖ W°_Q) = tE ∖ W°_Q, because W°_Q is a cone.
- cone(E) = ∪_{t∈ℚ₊} tE for open E: if g = s g′ with g′ ∈ E, then (s/t)g′ ∈ E for rational t near s.

**Cor 27.8: CONFIRMED at CHECKED level.** I re-checked each step.
1. *Off-band gambles whose acceptance is in the advice range lie in the reach set.* For g ∈ N ∩ Off, R(g) ∋ e_i, so N ∩ Off ⊆ W a.e. Off is an open
   cone, so cone(N) ∩ Off = cone(N ∩ Off) ⊆ W°_Q ⊆ Av a.e. For K′ close to T, D_{K′} ⊆ D_T ∪ cone(N), and
   D_T ≈ B_{p\*} ⊆ Av.
2. *Gambles that no evaluable model accepts meet no D_{K_q}.* Such g ∈ D_{K′} ∖ Off lie in no D_{K_q} at all, not just a.e. in q.
   If g ∈ D_{K_q}, then g ∈ D_{K_{q′}} for q′ ∈ Q near q (P(·,g) is continuous), and ∪_{q∈Q} D_{K_q} ⊆ Av a.e.
3. *The constructed signs are admissible.* The assigned c (−1 on negative entries, 0 on positive ones) is admissible,
   because every positive entry is band. Its chart is ∅, it has no ties in Ω, and it is consistent with
   B̂_q = B_q ∩ D_{K′} ≈ D_{K_q} ∩ D_{K′} = D_{K̂_q}.
4. *Excluded advice.* That every evaluable model accepts a mixed gamble is excluded by V1, via N5 Prop 3.5 (refereed CORRECT in N7). That needs
   (X_ik) with strict points h̄ − s𝟙 ∈ N whose acceptance is in the advice range, which holds for θ < θ_x. {+,−} pairs are adjacent, since d has the
   strict sign of g (R4 Thm A); non-adjacency therefore excludes them.
5. **Missing line (supplied here).** Let g be a non-adjacent pair with advice range {+,0,−} and weak signs. Then
   R(g) ∩ Ω = {c·q > 0} ∩ Ω:
   - If c_l > 0 at some positive l: near e_l both α > 0 and d > 0 (d is strict). Since {α > 0} ∩ Ω is connected and
     misses {d = 0} (no d-face), it lies in {d > 0}.
   - If c_l = 0 at every positive l: α < 0 on Ω, so R(g) ∩ Ω = ∅ = {α > 0} ∩ Ω.
   N27 asserts this conclusion without the argument.
6. *Wording.* Unanimous g ∈ D_{K′} a.e. have their acceptance in the advice range, since otherwise no B_q would be coherent. They have c > 0.
   Acceptance of −g for g ∈ D_{K′} is irrelevant to K̂.

With these points, K̂_q is a permitted-tie realisation on M_{D_{K′}} satisfying (X_ik), and Thm 27.6 applies.

---

## 5. The open regime and (VP) (N27 §2.7): CONFIRMED WITH REPAIR

- **(VP) is stated correctly.** It is equivalent to UVN(a) at x (Lemma 27.5). It is needed exactly at the relint points
  listed in §3.4.
- **Under (VP) the chain holds for every θ > 0, in either norm** (§3.2). Correct.
- **Equivalent form (CHECKED here).** By Blaschke compactness, liminf_{q→e_l} P(q,x) = min over the Hausdorff
  cluster sets W of K_q at e_l of P_W(x). Hence (VP) for the pair (l,k) is equivalent to: every such W satisfies
  W ⊆ {m : m·w_{lk} ≥ 0, m·r > 0}.
  - Here w_{lk} is the l-crossing of F_k, and r is the corner ray at the l-positive end of F_k. For T1, (l,k) = (3,1)
    gives r = r₁₂.
  - Since w_{lk}^⊥ ∩ aff Δ = line(e_l, v_k) and r^⊥ ∩ aff Δ = line(v_k, v_i), the condition says: W stays on T's side
    of line(e_l, v_k), and strictly inside T's side of the T-edge line through v_k, so v_k ∉ W.
  - `escape_check.py` (3): e₃ is admissible (boundary of the first constraint); v₁ fails the strict one; K′ is
    admissible.
- **Repair 1 (wording).** N27 §0 says "For θ ≥ θ_x, (X_lk) fails". Permitted ties are *allowed, not forced*.
  - What is true (§3.5): for θ ≥ θ_x no beyond-facet gamble is off-band at l.
  - So (X_lk) holds iff the ranking leaves a non-null set of l-positive points of U ∩ {v_k·x < 0} untied.
  - The open case is exactly: **for some crossing pair (l,k), c_l = 0 a.e. on U ∩ {x_l > 0, v_k·x < 0}.**
- **Repair 2 (the escape).** The proposed directional limit W = [e_l, v_k] is not admissible on M_U, because every K_q
  contains the two-dimensional K′ (Prop 3.3(a)).
  - The admissible version is W′ = co(K′ ∪ {e_l, v_k}), with D_{W′} = U ∩ {h_l > 0} ∩ {v_k·h > 0}.
  - It satisfies N5's local requirements (α) (in the strong form D_{W′} ⊇ A_l°) and (β). P_{W′} = 0 on the l-positive
    arc of F_k, so (VP) fails.
  - `escape_check.py` (2), ε = 0.3: at θ = θ_x + 10⁻³ no off-band 3-positive point of U lies outside D_{W′}; at
    θ = θ_x − 0.02 there are 1310 such points (beyond F₁), so the escape needs θ ≥ θ_x.
  - The conclusion of the paragraph is unchanged. It remains a CHECKED, local consistency statement, not a
    construction.
- **Repair 3 (the conjecture).** State it by norm.
  - Sup norm: nothing is open for θ ∈ (0,1) (Thm 27.6).
  - Euclidean norm: CONJECTURE that no permitted-tie realisation of T1 exists for θ ∈ [θ_x(T1), 1), equivalently that
    the all-tied configuration of Repair 1 is impossible.
  - Unsupported either way; no construction attempted (N27's own label).

---

## 6. Exact statement of what is established

**Theorem (N27 Thm 27.6 with Prop 27.4; refereed here: CONFIRMED).**

*Setting.*
- T ⊆ Ω is an all-facing triangle in general position, p\* ∈ Ω, θ > 0, and the norm is sup or Euclidean.
- c is a permitted-tie realisation of T at p\* on a U-domain M_U (evaluable models: the measurable subsets of U), U = D_{K′}, K′ ⊆ ri T. That is:
  - c : U → ℝ³ is measurable;
  - c_i(g) ≥ 0 on band-i⁺ g, c_i(g) > 0 if g_i > θ‖g‖ or g is unanimous, c_i(g) < 0 if g_i < 0;
  - (BU) holds at every q ∈ Ω, and (TP) K_{p\*} = T.

*Conclusion.* If (X_ik) holds for every facet F_k and every crossing coordinate i of F_k, then no such c exists. (X_ik)
means: a non-null set of x ∈ U with v_k·x < 0 and c_i(x) > 0. The same conclusion holds with (X) replaced by (VP).

**(X) holds automatically when θ < θ_x(T).** For T1:
- sup norm: every θ ∈ (0,1), i.e. every θ for which the band is proper;
- Euclidean norm: every θ < √((κ²+1)/(κ²+2)) = √(1 − v_{kl}²/|v_k|²), at every ε ∈ (0,1) and every interior p\*.
- In particular, for every Euclidean θ < √(2/3) and every ε, uniformly in ε.

**Coverage consequence.** No additive ranking on M_U covers T if it has:
- penalties obeying permitted NSI_θ, with ties placed measurably and target-dependently anywhere in the band;
- integrable envelopes;
- (LA), (S), (C);
- θ in the range above, or any θ with (X).

(BU) at every interior q is forced by (LA), (S), (C) for every θ (R1 Lemma 1.4 is guidance-free), and p\* is interior
(N1 Prop 2.3).

**Corollary (Cor 27.8; CHECKED level, confirmed).** The same holds on every (LF) decomposable domain (arbitrary open N) whose
pairs with an orientation in some D_{K′}, K′ ⊆ ri T, are a.e. non-adjacent, for θ < θ_x(T).

**Repair (i) (CONFIRMED).**
- Every result of writeup §5 (N21, N23) holds with the conic N₀ replaced by a compact collar N₀ᵇ ⊆ N of the compact Σ
  of normalised facet, crossing and witness gambles, with c₀ < η/√3 and r₁ chosen after c₀.
- (LF) needs no strengthening.
- For additive rankings with (BU), charts are ray-invariant (Lemma 27.2). Under strict guidance, advice ranges along a.e. ray
  differ only by × and by silence at pairs with advice range {+,0,−} and a thin silence cell (Cor 27.3). The conic N21.2 holds in
  full c-form at chart level (Cor 27.3′, strengthened in §2.3).

**Open.**
- Euclidean θ ∈ [θ_x(T1), 1), and only for rankings that tie a.e. every l-positive point of U beyond some facet plane
  F_k. The precise missing input is (VP), equivalently the vertex-limit condition of §5.
- General adjacent decomposable domains under ties.
- The charge version (writeup Cor 4.3) under ties.

---

## 7. Requested edits

**To N27.**
1. §0 and §2.7: "(X_lk) fails" → "(X_lk) is not automatic: it fails iff c_l = 0 a.e. on U ∩ {x_l > 0, v_k·x < 0}".
   Add the §3.5 fact that for Euclidean θ ≥ θ_x no beyond-facet gamble is off-band.
2. §2.4 Scope: note that θ_x(T1,U) = θ_x(T1) for every U.
3. §2.7: replace W = [e_l, v_k] by W′ = co(K′ ∪ {e_l, v_k}). State the conjecture separately for each norm.
4. Cor 27.3′: add the c-form conclusion (§2.3).
5. Cor 27.3, closing paragraph ("near ∂D_T this cannot happen"): label it CHECKED under (TS)/(PC).
6. §2.6: insert the non-adjacent weak-sign chart argument (§4, item 5) and the unanimous-gamble remark.
7. §4 status table: Thm 27.6 can now read "PROVED; refereed once (N27_referee: CONFIRMED)".

**To the writeup.** N27 §3 items 1–4 are endorsed. In addition:
- §5 preamble: say that Σ includes the box-witness limits in the normalisation used in Prop 4.22 ((−β,0,1), (1,0,−β)
  for T1).
- Thm 5.3: "(PC) for h near Σ, extended by linearity" (§1.4).
- §7.1: state Thm 27.6 with the hypothesis (X) and the automatic range. Add the uniform corollary
  "Euclidean θ < √(2/3), sup θ < 1, every ε". Describe the open case as the all-tied configuration of §5,
  Repair 1.
- §7.1 and the N5/N7 status lines: delete the IBU threshold, citing R1 Lemma 1.4 (guidance-free).

---

## 8. Files (`n27ref_py/`)

| File | Content | Result |
|---|---|---|
| `thresholds_ref.py` / `.out` | sympy: stationary point and closed form; numerics for θ_x (sup, Euclidean), Θ_NT, θ_x(T,U) | t\* = (κ−1)/(κ(κ+2)); f² = (κ²+1)/(κ²+2) exactly; sup θ_x = 1 on an open arc; θ_x(T,U) = θ_x(T) |
| `escape_check.py` / `.out` | ε = 0.3: half-space maximum; W′ = co(K′ ∪ {e₃, v₁}); vertex-limit form of (VP) | max over 2·10⁶ directions 0.92807 ≤ θ_x; D_{W′} ⊆ {h₃ > 0}; P_{W′} = 0 on the arc; no off-band 3-positive point of U outside D_{W′} for θ > θ_x |
| `lf_example_rerun.out`, `thresholds_rerun.out` | reruns of N27's scripts | identical to `n27py/*.out` |
