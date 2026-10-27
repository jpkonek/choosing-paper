# X65 — the adversary's attack on (H) (26 Oct 2026)

Labels: **PROVED** (complete argument here; not yet refereed) / **CHECKED** (exact rational computation) / **CONJECTURE** / **NUMERICS**. Scripts are in `x65py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file.

Binding inputs read: `BRIEF65.md` (role X65), `AUDIT_r65_brief.md`, `AUDIT_r65_message.md`, `ES64_notes.md` (§3, §5), `REF64_es_notes.md` (centroid calculation, §3.2, R1, R2), and `WT65_notes.md` (received mid-task; its tools are used as checked).

**Independence statement.** I worked on my own until I had the two-world theorem (§3) and the hull-slack and cut lemmas (§4). Then, while checking which notes had appeared in the folder, I read the verdict paragraph of `H65_notes.md` (its first 60 lines). It states H65's idea: apply ES64 Lemma 5.1 *inside hull(X)* rather than inside U. Step 1 of the proof in §2 is that idea. Steps 2–5 are mine. They use a single uniform shrink instead of cuts at extreme rays, so they need no pointedness assumption. I did not read the rest of H65's proof. §5.2 is an adversarial check aimed at any proof that generates hull(X) from boundary support points.

---

## 0. Verdict in plain English

1. **There is no counterexample. (H) is true**, in every number of worlds, for every μ and K′ in the brief's setting (Theorem H.1, PROVED). The defender always has a strict margin in every coordinate. So the WT65 caveat about zero-margin defenders does not arise.
2. **Why the "surround" attack fails.**
   - The surround configuration exists. Added regions can surround hull(X∖N) without meeting it, exactly as the centroid calculation (REF64_es §3.2) allows.
   - On an exact spike rival, 90 of the 104 strict U-Bayes dominators on a 1/60 grid have this shape and give no witness (CHECKED).
   - But the shape needs a defender that **sticks out of hull(X)**. A defender inside hull(X) adds nothing outside hull(X). After a cheap uniform shrink, the hull of what it removes contains the whole defender.
   - So the optional restriction that produced every "failure" in ES64 and REF64 was **taking Bayes acts of U as the base defender**. Bayes acts of hull(X) remove it.
3. **Independent elementary proof in two worlds** (Theorem 2D, PROVED; 384/384 random rivals CHECKED exactly). It also gives an exact characterisation in two worlds: a dominator fails to witness if and only if it contains X.
4. **An adversarial warning for proofs of (H)** (§5.2, PROVED). If cl hull(X) contains a line, which can happen only when dim K′ < n−1, the X-limit points on ∂hull(X) need not generate hull(X). Any proof that generates hull(X) from extreme rays or boundary support points therefore needs either pointedness or an extra argument. The uniform shrink of §2 is such an argument.
5. **Fallback.** Not triggered. Since (H) holds, Δ(all coherent models) covers every K with K′ ⊆ relint K. That is ES64 Cor 3.5 with REF64_es §2.5, both refereed. The auditor's scope corrections still apply (§6).

---

## 1. Setting

As in BRIEF65 and ES64 §3:
- n ≥ 1 worlds;
- μ is a finite measure with the null sets of Lebesgue measure (for instance, a positive density) and a finite first moment;
- K′ ⊆ relint Δ is nonempty, compact and convex, and U := D_{K′}.

Further notation:
- Models are measurable X ⊆ U, modulo null sets. Coherent models are the D_Q with K′ ⊆ Q.
- m(X) := ∫_X h dμ.
- Q_B := {q ∈ Δ : q·h ≥ 0 for a.e. h ∈ B}, and hull(B) := D_{Q_B}.
- P_Q(h) := min_{q∈Q} q·h.
- X_d is the set of Lebesgue density points of X.

Tools used:
- **W1** (WT65, checked): hull(B) = cone(B_d) + int ℝⁿ₊. I use only the inclusion "⊆", which has a two-line proof. If b ∈ hull(B) = int C with C = cl cone(B_d ∪ ℝⁿ₊), then b − 2η𝟙 ∈ C for small η > 0. Approximate it within η in sup norm by c ∈ cone(B_d) + ℝⁿ₊. Then b ∈ c + int ℝⁿ₊.
- **Claim 0** (WT65): if q ∈ Q_B and b ∈ B_d, then q·b ≥ 0.

---

## 2. Theorem H.1: (H) holds (PROVED)

**Theorem H.1.** Let X ⊆ U be incoherent. Then there is a coherent N with
- m(N) − m(X) ∈ int ℝⁿ₊, and
- μ((N∖X) ∩ hull(X∖N)) > 0.

No pointedness and no condition on n or dim K′ is needed.

*Proof.* Put G := hull(X) and P := P_{Q_X}. Then:
- G is open, convex and coherent, because K′ ⊆ Q_X;
- X ⊆ G a.e. (REF64_es E23);
- P > 0 on G and P ≥ 0 on cl G;
- P is concave, positively homogeneous and superadditive, and P(h + p) ≥ P(h) + min_i p_i, since every q ∈ Q_X is a probability vector.

**Step 1 (a strict dominator inside the hull; ES64 Lemma 5.1 relativised, which is H65's idea).**
- Let ℳ_G := {m(Y) : Y ⊆ G measurable}. By Lyapunov it is convex and compact; μ is atomless and the first moment is finite.
- It is full-dimensional, because G is open and nonempty.
- For λ ≠ 0, λ·m is maximised over ℳ_G exactly by Y = G ∩ {λ·h > 0}, uniquely a.e., because {λ·h = 0} is null.
- **Interior case.** Suppose m(X) ∈ int ℳ_G.
  - A maximiser z of Σz over ℳ_G ∩ (m(X) + ε𝟙 + ℝⁿ₊) is Pareto-maximal in ℳ_G.
  - Separating z + int ℝⁿ₊ from ℳ_G gives λ ∈ ℝⁿ₊∖0 with z = m(G ∩ {λ·h > 0}).
- **Boundary case.** Suppose m(X) ∈ ∂ℳ_G.
  - Every outer normal ν ≠ 0 at m(X) gives X = G ∩ {ν·h > 0} a.e.
  - If some ν ≥ 0, then X = G ∩ {π·h > 0} with π := ν/Σν. That set equals D_{conv(Q_X ∪ {π})} and is coherent. This is a contradiction.
  - So the normal cone meets ℝⁿ₊ only in 0. ES64's argument (pointed normal cone, separation from ℝⁿ₊) then gives d ≫ 0 with m(X) + td ∈ int ℳ_G for small t > 0, and the interior case applies.
- In both cases there is π ∈ Δ such that **N₀ := G ∩ {π·h > 0}** is coherent and m(N₀) − m(X) ∈ int ℝⁿ₊.

**Step 2 (the gain is non-null).**
- Suppose A₀ := N₀∖X were null. Then m(N₀) − m(X) = −m(X∖N₀).
- For k ∈ K′ we have k·h > 0 on U ⊇ X. So k·(m(N₀) − m(X)) ≤ 0, contradicting strict dominance.
- So A₀ is non-null. Fix a density point a of A₀ with a ∈ N₀. Then P(a) > 0.

**Step 3 (uniform shrink).**
- For τ ∈ (0,1) put Q_τ := (1−τ)Q_X + τΔ ⊆ Δ. Then P_{Q_τ}(h) = (1−τ)P(h) + τ min_i h_i.
- Put N_τ := N₀ ∩ D_{Q_τ} = D_{conv(Q_{N₀} ∪ Q_τ)}. It is coherent, since K′ ⊆ Q_{N₀}.
- Every h ∈ N₀ ⊆ G has P(h) > 0, so h ∈ N_τ for all small τ. Hence N₀∖N_τ ↓ ∅ as τ ↓ 0, and m(N₀∖N_τ) → 0 by dominated convergence (finite first moment).
- Fix τ so small that m(N_τ) − m(X) ∈ int ℝⁿ₊ and a ∈ N_τ.
- Then a is a density point of A := N_τ∖X, because N_τ is open. Put B := X∖N_τ.

**Step 4 (a representation that almost reaches the boundary).**
- Fix δ with 0 < δ < τP(a)/2, and put b := a − (P(a) − δ)𝟙. Then P(b) = δ > 0, so b ∈ G.
- By W1, b = Σ_j λ_j x_j + p′ with λ_j ≥ 0, x_j ∈ X_d and p′ ≫ 0, finitely many terms.
- The boundary ∂N_τ is null, being the boundary of a convex set. So each x_j can be moved slightly to a point of X_d off ∂N_τ while keeping p′ ≫ 0.
- Then each x_j is either **kept** (x_j ∈ N_τ) or **removed** (x_j in the exterior of N_τ). A removed x_j is a density point of B, since a ball around it misses N_τ.

**Step 5 (a uniform margin on Q_B).** Let q ∈ Q_B.
- Removed x_j: q·x_j ≥ 0, by Claim 0.
- Kept x_j: x_j ∈ N_τ gives (1−τ)P(x_j) + τ min_i x_{j,i} > 0. Since q ∈ Δ, q·x_j ≥ min_i x_{j,i} ≥ −((1−τ)/τ) P(x_j). This also holds trivially when min_i x_{j,i} ≥ 0, because P(x_j) ≥ 0, as x_j ∈ cl G.
- Superadditivity and P ≥ 0 on cl G give
  Σ_j λ_j P(x_j) ≤ P(Σ_j λ_j x_j) = P(b − p′) ≤ P(b) − min_i p′_i < δ.
- Hence
  q·a = Σ_j λ_j q·x_j + q·p′ + (P(a) − δ) > −((1−τ)/τ)δ + P(a) − δ = P(a) − δ/τ > P(a)/2.

So min_{q∈Q_B} q·a ≥ P(a)/2. For every a′ with |a′ − a|_∞ < P(a)/2 we get q·a′ > 0 for all q ∈ Q_B, so the ball lies in D_{Q_B} = hull(B). (If B is null, then Q_B = Δ and the same bound holds.) Since a is a density point of A, μ(A ∩ hull(B)) > 0. N := N_τ is the required defender. ∎

**Remarks.**
- Steps 3–5 replace "cut the support points of X on ∂G" by one shrink that uses no geometry of ∂G. The only facts used are P ≥ 0 on cl G, superadditivity, and the slack δ < τP(a)/2.
- **Where the WT65 tools are used.** W1 (one inclusion, proved above) and Claim 0. Compactness and the lower semicontinuity of the overlap are not used.
- **Exact illustration** (CHECKED, `surround3d.out`, Part 3). For the spike rival of §5.1:
  - π = (1017/5000, 3983/10000, 3983/10000) and τ = 10⁻⁴;
  - m(N) − m(X) = (9.09·10⁻⁴, 1.87·10⁻⁴, 1.87·10⁻⁴) ≫ 0, exact;
  - the section area of (N∖X) ∩ hull(X∖N) is 0.2094 > 0, exact.

**Corollary H.2 (PROVED, using refereed results).** By ES64 Thm 3.2 / Cor 3.5 and REF64_es §2.5 (refereed CORRECT), the relation Δ(all coherent models) on U satisfies the binding framework, and:
- its undominated models are exactly the coherent models on U;
- every incoherent model is dominated by a coherent one, with a strict margin in every coordinate;
- every K with K′ ⊆ relint K is covered, including the reversed triangle.

---

## 3. Theorem 2D: an independent elementary proof in two worlds (PROVED; CHECKED)

I proved this before Theorem H.1. It is kept because it is independent, it gives an exact two-world characterisation, and it shows concretely what a counterexample would need in higher dimensions.

**Coordinates.**
- L-rays: h = x(1, −t), with 0 < t < T_L := min_{k∈K′} k₁/k₂.
- R-rays: h = y(−s, 1), with 0 < s < T_R := min_{k∈K′} k₂/k₁.
- T_L T_R ≤ 1, with equality iff K′ is a point.
- Coherent models: N_{α,β} := L(0,α) ∪ int ℝ²₊ ∪ R(0,β), with 0 ≤ α ≤ T_L and 0 ≤ β ≤ T_R. In two worlds, every such set is coherent and every coherent model is of this form.
- By ES64 Prop 5.4, assume X ⊇ int ℝ²₊.
- Put e_L := ess sup of t over X∩L, and f_L := sup{α : L(0,α) ⊆ X a.e.}. Define e_R and f_R likewise.
- Then hull(X) = N_{e_L,e_R}. X is coherent iff f_L = e_L and f_R = e_R.

**Lemma 2D.1 (exact two-world witness criterion; PROVED).** Let N = N_{α,β}. Then μ((N∖X) ∩ hull(X∖N)) > 0 iff f_L < α < e_L or f_R < β < e_R. If N weakly dominates X (m(N) ≥ m(X), not equal), with X incoherent, and has no witness, then **X ⊆ N a.e.**

*Proof.*
- Since B_L := X∩L∖N lies in {t ≥ α}, when it is non-null its essential supremum of slope exceeds α. Then hull(B) ⊇ L(0, ess sup) ⊇ N∩L ⊇ A_L. Hence the L-side contributes a witness iff A_L and B_L are both non-null, that is, iff f_L < α < e_L.
- Without a witness, on each side A or B is null. Of the four combinations:
  - A_L = A_R = ∅ gives N ⊆ X. Then k·m(X∖N) ≤ 0, so N = X, which is coherent: a contradiction.
  - A_L = B_R = ∅ gives m₁(N) − m₁(X) = m₁(A_R) − m₁(B_L) ≤ 0, with equality only if both are null: again N = X.
  - The mirror case is the same.
  - The only remaining combination is B_L = B_R = ∅, that is, X ⊆ N. ∎

**Theorem 2D (PROVED).** In two worlds, every incoherent X satisfies (H).

*Proof.*
- Let H := hull(X)∖X and v := m(H). Write a₁ := m₁(H_L) > 0 and a₁ t̄ := ∫_{H_L}|h₂| dμ, where t̄ < e_L when H_L is non-null. Similarly a₂ := m₂(H_R) and a₂ s̄ := ∫_{H_R}|h₁| dμ, with s̄ < e_R.
- Then v = (a₁ − a₂s̄, a₂ − a₁t̄). Also k·v > 0, so v ∉ −ℝ²₊.
- Note that m(N_{α,β}) − m(X) = v + [m(N_{α,β}) − m(N_{e_L,e_R})].

Four cases:
- **(a) v ≥ 0, v₁ > 0.** Then a₁ > 0, so f_L < e_L. Take N_{e_L−ε, e_R}. The change is −m(L(e_L−ε, e_L)) = (−x, +y), with x, y > 0 and x → 0. So the margin is ≫ 0 for small ε, and α ∈ (f_L, e_L).
- **(b) v₁ = 0, v₂ > 0.** Mirror: take N_{e_L, e_R−ε}.
- **(c) v₂ < 0, so v₁ > 0 and a₁ > 0.**
  - *Room:* the R-wedge (e_R, T_R) has second moment ≥ |v₂|. Pick β with m₂(R(e_R, β)) = |v₂|. Its first-moment cost is at most β|v₂|, and
    v₁ − β|v₂| = a₁(1 − βt̄) + a₂(β − s̄) > 0,
    since βt̄ < T_R T_L ≤ 1 and β ≥ e_R ≥ s̄. Then N_{e_L−ε, β} is ≫ 0 for small ε, and α ∈ (f_L, e_L).
  - *No room:* every N_{α,β} with α ≥ e_L and β ≥ e_R has second coordinate ≤ v₂ + (room) < 0. So no dominator contains X. A dominator exists (ES64 Lemma 5.1, any n), and by Lemma 2D.1 it is a witness.
- **(d) v₁ < 0.** Mirror of (c). ∎

**CHECKED** (`two_world.py` → `two_world.out`).
- 384 random incoherent cone rivals (unions of up to four slope intervals per side), with random U, density e^{−|h|₁} and exact rational wedge moments.
- In every instance the proof's construction gave a dominator and a witness, both verified exactly (384/384).
- Case counts: (a) 129, (b) 0, (c) room 72, (c) no room 57, (d) room 67, (d) no room 59.

**What the two-world proof shows about higher dimensions.** In two worlds, a non-witness defender must *contain* X (Lemma 2D.1). In three worlds it need not: added regions can sit in "caps" beside a spike-shaped hull(X∖N). That is the surround shape, and the only room a counterexample could have had (§5.1). Theorem H.1 shows the room is never enough.

---

## 4. Lemmas proved on the way (PROVED; subsumed by Theorem H.1, recorded as tools)

**Lemma 4.1 (cut lemma).**
- Let N = D_Q be coherent, and let e ∈ ∂N have e_i < 0 for some i. Pick q ∈ Q with q·e = 0, and put q_τ := (1−τ)q + τe_i.
- Then N_τ := N ∩ {q_τ·h > 0} is coherent; N∖N_τ ↓ ∅, so m(N∖N_τ) → 0; and N∖N_τ ⊇ N ∩ {q_τ·h < 0}, an open neighbourhood of e intersected with N.
- So any X-density points of N near e can be moved into X∖N at arbitrarily small Brier cost. Finitely many cuts combine.

**Prop 4.2 (hull slack).**
- If m(hull(X)∖X) ∈ int ℝⁿ₊ and cl hull(X) is pointed, then (H) holds with N = hull(X) minus finitely many cuts at extreme rays.
- Pointedness holds automatically when dim K′ = n−1, for example K′ = (u+K)/2.
- Theorem H.1 removes both hypotheses: its Step 1 manufactures the slack, and its Step 3 replaces the cuts.

**Lemma 4.3 (localisation).**
- Let S := cl(X_d) ∩ ∂hull(X) (as rays), and let O be any open cone containing S∖0. Then hull(X∩O) = hull(X).
- *Proof.* The directions of X_d∖O have compact closure inside hull(X). So their constraints are uniformly slack near Q_X, and Q_X is relatively open and closed in the convex set Q_{X∩O}. Hence the two are equal.

---

## 5. Adversarial findings

### 5.1 The surround rival: it exists for U-Bayes defenders and disappears inside the hull (CHECKED)

Rival (`surround3d.py`):
- X = D_K ∪ P on the reversed triangle of ES64, where P is a narrow spike beyond face F₁ (lateral half-width 1/40) running out to ∂U;
- density e^{−|h|₁};
- exact cone moments from es64py/cones.py, and exact polygon areas in the section Σh = 1.

Results:
- **Part 1.** On the 1/60 prior grid there are 104 strict U-Bayes dominators. 14 give a witness. 90 do not: their added part surrounds hull(X∖N) without meeting it, as REF64_es §3.2 anticipated. Three examples are printed, with margins up to 0.2.
- **hull(X) itself** has m(hull) − m(X) = (0.158, −0.046, −0.046), so it is not a dominator.
- **Inside-hull Bayes acts.** No strict dominator of the form hull(X) ∩ {π·h > 0} exists on the 1/60 or 1/120 grids. A refined line search finds 3 on π = (1−2p, p, p), with margin about 2·10⁻⁴ (NUMERICS for the search; each found dominator CHECKED exactly). Step 1 guarantees one exists. The window can be very small, so a grid search is not a reliable way to find it.
- **Part 2** (vertex cuts) and **Part 3** (uniform shrink, τ = 10⁻⁴): both give an exact strict dominator with an exact witness, of section area ≈ 0.21.

*Reading.* Every "surround" failure is a failure of a defender that leaves hull(X). The added part of an inside-hull defender lies in hull(X), and after the shrink, hull(X∖N) ⊇ N.

### 5.2 A trap for proofs: boundary support points need not generate hull(X) (PROVED)

**Example NP.** Take n = 3 and K′ = {u}, so U = {Σh > 0} is a half-space and is not pointed. Write h = αw + βw′ + γ𝟙/√3, with w ⊥ w′ unit vectors orthogonal to 𝟙. Let

  X := int ℝ³₊ ∪ {h : γ > 0, γ|h| < β² < 4γ|h|}.

Then:
- **hull(X) = U.** Write q = u + z with z ⊥ 𝟙.
  - Near ±w, X contains directions with γ → 0 and β ≈ ±√γ (both signs).
  - On these points q·h = γ/√3 + αz·w + βz·w′ ≥ 0. Letting γ → 0 forces z·w = 0. Then, since |β| ≫ γ with both signs, it forces z·w′ = 0.
  - So Q_X = {u}.
- **The X-limit rays on ∂U are only ±w.** On ∂U, γ = 0 forces β = 0.
- **They do not generate.** cone(±w) + int ℝ³₊ = ℝw + int ℝ³₊ ≠ U. For example, w′ + ε𝟙 is not in it for small ε, because w′ has a coordinate −2/√6 and w has 0 in that coordinate when w = (1,−1,0)/√2.

*Consequence.* A proof that builds the witness from X-limit points on ∂hull(X), such as extreme rays or support points, needs cl hull(X) to be pointed, or an extra argument. Here the witness must use interior X points near ±w. They are tangential, so cone(B_d) contains directions close to ±w′.

Theorem H.1's shrink handles this automatically: it removes every X-point whose negative part is large compared with P(x), wherever it is. Lemma 4.3 is the corresponding localisation fact. **I flag this for the referee of H65:** check how its "Generation Lemma" treats non-pointed hulls.

### 5.3 What a counterexample would have needed (historical; now vacuous)

Before Theorem H.1, the strongest necessary structure I could prove was the following. For every strict dominator N:
- the added part N∖X misses cone(Z_N ∪ (X∖N)_d) + int ℝⁿ₊, where Z_N is the set of points of ∂N∖cl ℝⁿ₊ approached by X∩N (Lemma 4.1 + W1);
- N has an X-free boundary layer;
- the coherent model generated by the X-touched extreme rays of N lies inside X.

The defender hull(X) ∩ {π·h > 0}, shrunk, violates all three, so the class of candidates is empty.

### 5.4 Margins (WT65's caveat)

WT65 warns that zero-margin defenders escape every 𝒦_δ. For a counterexample they would have had to be ruled out too. Theorem H.1 always produces a defender with a strict margin in every coordinate, so the question does not arise.

---

## 6. Fallback and scope

- **Fallback (brief).** Not needed: no counterexample exists. For the record, (★) for any smaller family 𝒩 ∋ D_K is now unnecessary for coverage. Δ(all coherent) already covers.
- **Measure.** Theorem H.1 holds for **every** μ in the setting, which is more than the cover needs (one ν; REF64_es E14).
- **Auditor's scope corrections still apply.**
  - "Universal" means within a fixed U. Coverage of a target needs K′ ⊆ relint K and (LF).
  - The construction is coherence-informed. It shows that coherence is *representable* by dominance under the agreed axioms. It is not an independent accuracy-based justification of coherence.
  - With (H) proved, the binding framework's covering question is trivial for every target with K′ ⊆ relint K. Whether to strengthen the framework, for example by (Add), is the separate normative question (AD65), not a correction.
- **Not claimed.**
  - Nothing about rankings other than Δ(𝒩).
  - Nothing about (Add)-closed variants.
  - Nothing about U that is not of the form D_{K′} with K′ ⊆ relint Δ.

---

## 7. Status table

| Item | Status |
|---|---|
| **Counterexample to (H)** | **None exists** (by Theorem H.1) |
| **Theorem H.1: (H) for every incoherent X, any n, any μ with Lebesgue null sets and finite first moment, any K′ ⊆ relint Δ; strict margin in every coordinate; no pointedness needed** | **PROVED** (Step 1 is H65's relativisation of ES64 Lemma 5.1; Steps 2–5, the uniform shrink, are X65's) |
| Corollary H.2: Δ(all coherent) is a universal cover on U (every K with K′ ⊆ relint K) | PROVED, given refereed ES64 Thm 3.2 / Cor 3.5 and REF64_es §2.5 |
| Lemma 2D.1: in two worlds, a dominator fails to witness iff it contains X | PROVED |
| Theorem 2D: (H) in two worlds, elementary and independent | PROVED; 384/384 random rivals CHECKED exactly (`two_world.out`) |
| Lemma 4.1: cut lemma (any boundary point with a negative coordinate can be cut at vanishing cost) | PROVED |
| Prop 4.2: hull slack ⇒ (H) (pointed case) | PROVED (subsumed) |
| Lemma 4.3: localisation, hull(X∩O) = hull(X) | PROVED |
| §5.1: surround rival; 90/104 U-Bayes strict dominators have no witness | CHECKED (grid; each verdict exact) |
| §5.1: inside-hull defenders (vertex cuts; uniform shrink) certified on the surround rival | CHECKED exactly |
| §5.1: strict inside-hull Bayes dominators are rare there (3 found on a fine line; none on the 1/60 or 1/120 grids) | NUMERICS (each found one CHECKED) |
| Example NP: boundary support points need not generate a non-pointed hull | PROVED |
| §5.3: necessary structure of a counterexample | PROVED (now vacuous) |
| Fallback (smaller 𝒩) | not needed |

## 8. Files (`x65py/`)

| File | Content |
|---|---|
| `two_world.py` / `.out` | exact two-world rivals; the Theorem 2D construction and its witness, verified in rationals |
| `surround3d.py` / `.out` | spike rival D_K ∪ P: U-Bayes grid (surround failures); inside-hull defender with vertex cuts; uniform-shrink defender of Theorem H.1; exact moments and exact section areas |
