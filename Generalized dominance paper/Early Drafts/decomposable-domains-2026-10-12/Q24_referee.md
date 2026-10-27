# Referee report on Q2_notes.md Part I (round 22) and Q4_notes.md (round 21)

16 Oct 2026. Adversarial reading. Verdicts: **CORRECT**, **GAP** (fixable, with the fix), **WRONG**.

Background read against:
- R21_reduction;
- K3 §§1, 5 (K3.5, K3.5′, K3.6);
- H1 §§2–4 (H1.0, H1.1, H1.2);
- N2 Part I (N2.1–N2.3′);
- M1.3;
- M3 §§1, 3, 5–7, M23_referee §§6.7–6.13;
- D1 (statement, D1.1);
- N21 §§1–5 (N21.4, N21.6, N21.7);
- write-up §2 (axioms, C_L, (LF)), §5 (Lemma edgebox, Prop. boxbridge, Prop. T1), §6 (Lemmas walls, quasiconcave, B1;
  Thms TS, cuts, TSalways);
- **Q1_notes Part I** (Q1.20–Q1.26), for the consistency check the brief asked for.

Scratch: `q24ref_py/`.
- `q4_rerun.py`: a verbatim copy of `q4py/q4_checks.py`, run with `python3 -I`. Its `.out` is byte-identical to
  `q4py/q4_checks.out`.
- `radial_cycle.py` / `.out`: NUMERICS for §1.3 below. No verdict rests on it.

---

## 0. Summary

**Q2 Part I.** The σ-finite machinery is correct: Q2.10–Q2.13, Q2.16 and Q2.17. The **four inclusions of Q2.12 are
CORRECT**. Q2.12 is N2.3 verbatim, and positivity of the (Loc) densities replaces null joint blindness exactly where
strictness of e_θ′ − e_θ is needed.

The link-class freedom claims are **WRONG as stated**, and so is the positive lead built on them. These are Q2.14(c),
Q2.15′, the "Why this does not give (I)" paragraph of §7, §0 item 2, §8 2(b), and Conjecture Q2.C (as specified).

They conflict with Q1.22–Q1.24, written in parallel. The core of Q1.22(a) is a two-step rook cycle of edge cut moves.
Those cut moves are the "cut moves" of Q2.18 itself (= Q1.20). I re-derived the cycle in local form (§1.3, Lemma R1).
- It **sees the partner ratio ω = w₂/w₃ on the blind link class**.
- It forces ω to be constant along rays wherever world 1's two edge chains cross transversally.
- It uses no world-1 density, so Λ₁ is irrelevant.

So a ray-varying partner ratio does not make world 1 "automatically ¬(Loc)" in (V). On a transverse part of Q₁ it makes
strict (G) fail at world 1, so no system exists. The two notes are logically consistent (Q2.15′ is then vacuous there).
But Q2's "costs nothing", "no proved constraint touches the ratio" and "(I) cannot be proved by edge arguments" are
refuted on the transverse part.

**The nearby result that is available** (§1.4): the lead survives exactly on
- **comonotone** parts of Λ₁ ∩ Q₁, where the two chains share level sets with the same orientation;
- or at non-nested edges at e₁.

There Q2.15 (N1) still gives ¬(Loc) for free, and no cut-move cycle reaches ω. This is Q1's Q_Q1, and the two notes
should be merged on it.

**Q4.** **Theorem Q4.1 is CORRECT**, including Step 3 (edge box with E on a general domain) and Step 6 / Q4.0(a)
(vertex continuity for every tie-breaking). Lemma Q4.3 is CORRECT. The CHECKED claim that M3.9 uses (Av) nowhere else
is supported by my spot checks; **CHECKED stands**. Corollary Q4.2 is CORRECT at the status of M3.9 (CHECKED, M23_referee
GAP (ii)), so (GnAv-nd) is closed at that status. Prop. Q4.4 is CORRECT with two small GAPs. NUMERICS (2), (3) and (5)
are tautological, and (4) has a dead branch; none is load-bearing.

| Item | Verdict |
|---|---|
| Q2.10 (a)–(d) | CORRECT. Wording: (R-ii) is absorbed into (R-i), not removed |
| Q2.11 (a)–(c) | CORRECT. GAP (minor): "transfers verbatim to any domain" (§8) needs the ladder/selection form |
| **Q2.12, four inclusions** | **CORRECT**. GAP (cosmetic): add (LA) (M1.3 needs it) |
| **Q2.13 (a)–(c)** | **CORRECT** |
| Q2.14 (a), (b) | CORRECT (algebra, plus N2.3 / Q2.13(a)) |
| **Q2.14(c), the CHECKED reading** | **WRONG**. The list omits edge cut moves and their composition (Q2.18 / Q1.20, Q1.22). These see ω on Λ_i ∩ Q_i |
| Q2.15 (N0)–(N2) | CORRECT. GAP: the closing remark "(N1), (N2) only on Λ_i ∩ Q_i" conflates (Loc) densities with CA endorsers |
| **Q2.15′** | First bullet CORRECT but vacuous on transverse parts. "Costs nothing / no proved constraint / (I) false at world 1 / Q_P1 reduces to …" **WRONG as stated**. Fix in §1.4 |
| Q2.16, items 1–6 | CORRECT |
| Q_W | Well posed. Equals K3's (R-i) after Q2.10. Comment in §1.6 |
| Q2.17 | CORRECT |
| Q2.18 | CHECKED reading of the transfers fine. **Its "Why this does not give (I)" is WRONG** (Q1.23 proves (I) under (TC)) |
| Conjecture Q2.C | **Under-specified; false in every transverse realisation** (Lemma R1, Q1.25(b), q1_fiber_return). Restate on a comonotone link |
| Q4.0 (a)–(d) | CORRECT |
| **Q4.1, Steps 1–8** | **CORRECT**. Step 3 and Step 6 checked line by line. Cosmetic: shrink δ(s) ≤ s in Step 2 so that g_m → w\* |
| **Q4.3** | **CORRECT** |
| M3.9 "no other (Av)" (CHECKED) | **CHECKED stands** (spot checks §2.4) |
| **Q4.2** | **CORRECT at the status of M3.9** |
| **Q4.4** | **CORRECT**, with GAP (a): M3.7(a)/(b) used for degenerate fields; and GAP (b): §0's "automatic" in (iii) |
| Q4.5 | CORRECT |
| q4py NUMERICS | Reproduced exactly. (2), (3), (5) tautological given the test gambles; (4) dead branch |

---

## 1. Q2 Part I

### 1.1 Q2.10, Q2.11, Q2.16: CORRECT

- **Q2.10(a).** D̃^k decreases, and μ(D̃^k_m) ≤ μ(D^k_m) + μ{ρ_k > m} → 0. A D̃-localized δ (≤ 0 on D̃_m ⊇ D_m) is
  D-localized (K3 §1 definition). CORRECT.
- **Q2.10(b).** Author's risk item 6.
  - A point of D̃^k_{m₀} with σ_j ≠ σ_k lies in R_jk.
  - D̃^j_{m₀} ∩ D̃^k_{m₀} ∩ R_jk is null by (i), so ρ_j ≤ m₀ a.e. there.
  - The first sum of K3.5′(c)(ii) is therefore ≤ 6m₀μ(M). The min-term is ≤ 2m₀μ(M).
  - K3.5′(c)'s patch Y° is consistent by (i). Triple overlaps lie in some R_ij of a disagreeing pair, so they are null.
  - CORRECT.
- **Q2.10(c), (d).** CORRECT. (d) is trivial once ρ_j ≤ m off D̃^j_m.
  - *Wording.* "(R-ii) disappears unconditionally" should read "(R-ii) is absorbed into (R-i)". The common blow-up
    {ρ_i > m} ∩ {ρ_j > m} is the old minority mass, now counted as sheltering. §6.2 says this; §2's Reading should too.
- **Q2.11(a).** Author's risk item 2.
  - For W ⊆ G_m the vector of C ⪯_k (C △ W) is χ_k1_W.
  - It vanishes on D̃^k_m for every k ∈ S simultaneously, so it is D̃^k-localized at each k (definition: ≤ 0 on D_m).
  - The Lyapunov / separation / limit steps are N2.1(b) and H1.1 steps 2–3. Finiteness holds because ρ_k ≤ m on G_m.
  - CORRECT.
- **Q2.11(b).** N2.1(c)'s computation. CORRECT.
- **Q2.11(c).** H1.1 needs ρ_k integrable off D_m (true: ρ_k ≤ m there) and endorsement of T1's out-comparisons that
  equal T1 on D_m (δ = 0 on D_m ⊇ D̃^k_m). Step 4 uses only ρ_k > 0. This is K3.5's Step 2. CORRECT.
- **§8 claim "Q2.11 transfers verbatim to any domain": GAP (minor).** On a general domain, C △ W is not defined. One
  needs alternative measurable selections of A′(g), as in M3.4 step 3, with Lyapunov over finitely many alternatives,
  in ladder coordinates. That proof exists (M3.4(3)), so the fix is a citation, not new work.
- **Q2.16.**
  - Items 1–5 are Q2.10–Q2.14(a).
  - Item 6: c ≠ 0 a.e. and Tonelli give null Z_t for a.e. t, so (W) ⇔ (γ). Admissibility at an interior p̂ (Q2.11(c))
    plus M0closed(a), which uses no integrability (H12_referee §1.4, as quoted in H1.2's proof), gives the contradiction.
  - This is K3.5 Step 2 with (γ) assumed instead of derived from a patch.
  - CORRECT. "Equivalent to (W)" is correct in the trivial sense: if no all-(Loc) cover exists, (W) holds vacuously.

### 1.2 Q2.12 and Q2.13: CORRECT

**Q2.12(a), the four inclusions (author's risk 1).** With e_θ = θρ_i − (1−θ)ρ_j we have
e_θ′ − e_θ = (θ′−θ)(ρ_i+ρ_j), which has the strict sign of θ′ − θ a.e. because ρ_i, ρ_j > 0 a.e. Each case:
1. θ′ ≤ θ, X = E^{θ,−}. Then e_θ′ ≤ e_θ, so {e_θ < 0} ⊆ {e_θ′ < 0} ⊆ c. No strictness is needed.
2. θ′ > θ, X = E^{θ,−}. Then c ⊆ {e_θ′ ≤ 0}. Strictness gives e_θ < e_θ′ ≤ 0 a.e. there, so c ⊆ A. **This is where
   positivity is used.**
3. θ′ < θ, X = E^{θ,+}. Strictness gives {e_θ ≤ 0} ⊆ {e_θ′ < 0} ⊆ c a.e. **Positivity is used.**
4. θ′ ≥ θ, X = E^{θ,+}. Then c ⊆ {e_θ′ ≤ 0} ⊆ {e_θ ≤ 0}. No strictness is needed.

Then C ⪯_i X with E_iX ⊆ E_iC forces c = A by strict (G) at i. Likewise C ⪯_j X with E_jX ⊆ E_jC forces c = A at j.
Both are edge models, so X = C ∈ C_L.

The vertex cases are N2.3's:
- C_{e_i} competitive on {i} is P_i by strict (G);
- C ⪯_j X with E_jX ∩ R_ij = R_ij ∖ A forces A null.

The θ′-Bayes property of C_p is Q2.11(b). C_p is competitive on {i, j} and is an edge model (N2, "Edge models").
Boundary θ′ ∈ {0, 1} is covered: at θ′ = 1, e_1 = ρ_i > 0, so c is null.

**CORRECT.** The N2.3 hypothesis "null joint blind set" is replaced exactly by "ρ_i + ρ_j > 0 a.e."
- *Cosmetic GAP.* M1.3 assumes (LA) as well as (S) and strict (G). Q2.12's header should list it.
- E^{θ,±} must be regular and in M_U. It is: a measurable subset of U accepting N₊.

**Q2.12(b), (c).** CORRECT.

**Q2.13(a) (risk 3).**
- E^{θ,−} ∈ C_L is coherent. C_L is the coherent undominated set (write-up §2.2), and C_p ∈ C_L by (S).
- So {r > s} ∩ R_ij = E_i(D_K) ∩ R_ij a.e., which is a cone.
- r̂ := sup{s ∈ ℚ₊ : g ∈ K_s} is exactly 0-homogeneous and equals r off the null set N.
- r(λg) = r̂(λg) for a.e. g, because g ↦ λg preserves Lebesgue-null sets and μ ~ Lebesgue.
- Disjoint tie sets in a finite measure space: only countably many are non-null.
- CORRECT.

**Q2.13(b).** CORRECT. On Q_l ⊆ R_lj ∩ R_lk, write ρ_j = r_ljρ_l.

**Q2.13(c) (risk 4).** For t ∈ (e_i, e_j), on R_ij, t·c = σ_i(t_iρ_i − t_jρ_j).
- B_t is world-i-wrong exactly on {r_ij > s} with s = t_i/t_j = θ/(1−θ), θ = t_i, and rejects on {r_ij = s}.
- E^{θ,−} is P_i on the tie cone and E^{θ,+} is its complement there, so their intersection rejects on it. Off the tie
  cone, both agree with B_t.
- D_K ∩ D_{K″} = D_{co(K ∪ K″)}, using P_{co(K∪K″)} = min(P_K, P_{K″}).
- On Q_k, B_t = P_i = P_j.
- CORRECT.

**Q2.17.** CORRECT.
- The selected edge model with errors {r > s} is θ*-Bayes for (ρ*_i, ρ*_j) by N2.1(c), which gives the cut inequality.
- At θ* = 1 the inequality reads r > s ⇒ ρ*_i = 0 ⇒ r* = ∞ off J*, consistent with s* = ∞.
- The monotone-function step is F1.2(b)'s.

### 1.3 Q2.14(c) and the link-class freedom: WRONG. The cut-move cycle sees ω on Λ₁ ∩ Q₁

Q2.14(c) lists the constraints that "see the partners on Λ_i ∩ Q_i only through σ_j = σ_k and positivity". Q2.15′'s "no
proved constraint touches the partner ratio" and §8's "a ranking-level argument on Λ_i ∩ Q_i … none exists yet" both rest
on this list.

The list omits **edge cut moves**. Q2 itself states them in Q2.18 ("If ρ_j(Q) > ρ_j(P), then … C_b ⋠_j X by (RL-2) …
gives C_b ⪯_i X"). They are Q1.20 and the first paragraph of F1.2 (refereed in F12_referee). They need:
- competitiveness of an interior edge selection on {1, j};
- (RL-2) at the partner;
- (Nest_e) with no jumps (N1.4(a)).

They use **no density of world 1**, so they act inside Λ₁. Composed across the two edges at e₁, they constrain ω. The
following is the local core of Q1.22(a), which I re-derived independently of Q1's routing machinery.

**Lemma R1 (local pinning of the partner ratio; PROVED here).** Let world 1 satisfy strict (G) and (IB). Let its edge
selections at e₁ satisfy (H_E) of Q1 §1, with chain coordinates x₂, x₃ (c^j_t = {x_j < b} for every b ∈ (0,1)). Let
worlds 2 and 3 satisfy (RL-2) with densities w₂, w₃ > 0. Suppose:
- g ∈ Q₁ and λ > 0;
- w₂ and w₃ are continuous at g and at λg;
- χ = (x₂, x₃) is continuous and open near g.

Then ω(λg) = ω(g), where ω := w₂/w₃. More generally, ω(g) = ω(g′) whenever χ(g) = χ(g′) and χ is open near both.

*Proof.*
- Put z := χ(g) = χ(g′). The x_j are 0-homogeneous, since coherent edge models are cones. So χ(λg) = χ(g), and χ is
  open near λg.
- Openness makes the anti-diagonal corner sets non-null:
  - V ∩ {x₃ < z₂, x₂ ≥ z₁} near g;
  - V′ ∩ {x₃ ≥ z₂, x₂ < z₁} near g′.
- Suppose ω(g′) < ω(g). Fix η with (1+η)⁴ω(g′)/ω(g) < 1, and neighbourhoods on which w₂, w₃ vary by factors ≤ 1+η.
- Take S⁰ of small mass in the first corner.
- **13-cut at b = z₂** (Q1.20 with j = 3). Choose T¹ in the second corner with w₃(T¹) = (1+η)w₃(S⁰). Then
  1_{T¹} − 1_{S⁰} is accepted at world 1.
- **12-cut at b = z₁** (Q1.20 with j = 2). Choose T² ⊆ S⁰ with w₂(T²) = (1+η)w₂(T¹). This is possible because
  w₂(T¹) ≤ (1+η)²(ω(g′)/ω(g))·w₂(S⁰) < w₂(S⁰)/(1+η).
- By composition (Q1.21, i.e. (IB) and transitivity), 1_{T²} − 1_{S⁰} is accepted.
- This vector is ≤ 0 and non-zero, because T² ⊊ S⁰ with smaller w₂-mass. That contradicts strict (G).
- Exchange the roles of g and g′ for the other inequality. ∎

NUMERICS (`q24ref_py/radial_cycle.py`):
- Data: the linear-host chains x_j = |g₁|/|g_j|, w₂ = |g₂|(1+|g|), w₃ = |g₃|, g\* = (1, −.25, −.2) ∈ (+,−,−) ∩ U, and
  the cycle 2g\* → g\* → 2g\*.
- Both anti-diagonal corners are non-null.
- The deposit has w₂(T²)/w₂(S⁰) = 0.725 < 1.

So, in a (V)-cover with additive integrable partners and (Nest_e) at e₁:
- On every part of (+,−,−) ∩ U ⊆ Λ₁ ∩ Q₁ where world 1's chains cross transversally, a ray-varying ω is **forbidden by
  strict (G) at world 1**.
- Q2.15′'s premise is then unsatisfiable there. Its conclusion "world 1 is ¬(Loc)" holds only vacuously.

Q1.22–Q1.23 go further under (TC): they prove (Loc) at world 1 outright, i.e. (I). This refutes the following claims of
Q2:
- §0 item 2 ("(I) cannot be proved by any argument that uses only edge structure"). Q1.23 is such an argument, under
  (Nest_e) + (TC) with (RL-2) partners.
- Q2.15′, bullets 4–5 ("costs nothing", "no proved constraint", "(I) is false at world 1 of any such (V)-cover", "Q_P1
  reduces to Q_N2⁽³⁾ / Q_V+ for additive partners with a non-0-homogeneous ratio").
- The Reading after Q2.15′ ("chosen by the selection independently of the partners"). The selection chooses the chains,
  and then ω must factor through them, ω = ψ(x₃)/φ(x₂) (Q1.22(a)).
- §7, "Why this does not give (I)". Gluing is produced by composing the two edges' cut moves, not by window bounds.
- §8 2(b), first bullet.

Q1 is unrefereed. These verdicts rest only on Lemma R1, whose inputs are Q1.20 / Q2.18 (cut moves) and Q1.21
((IB) + transitivity). The full (TC)-routing of Q1.23 needs its own referee.

**Consistency with Q1.22–Q1.24 (the brief's question).**
- *Logically:* the notes are consistent. Q1 says "no system" (under (Nest_e) + (TC) + (RL-2) partners). Q2.15′ says "if
  such a system exists, world 1 is ¬(Loc)".
- *Substantively:* they are inconsistent. Q2 presents the region as open and the lead as cheap. Q1 shows the region is
  empty in the transverse case.
- Q2.14(a)'s factorization ρ_j/ρ_k = r_ij/r_ik, with r_1j a nonincreasing function of x_j, is exactly Q1.22(a)'s
  ω = ψ(x₃)/φ(x₂). Here r₁₂ = 1/φ(x₂), because {x₂ < b} = {r₁₂ > s(b)}. Q2 derives it from (Loc). Q1 derives it from
  strict (G) on the transverse part, with no (Loc) assumed.

### 1.4 The nearby positive lead that does survive

Lemma R1 needs non-null **anti-diagonal** corners at every turning point of a cycle. The turning conditions are:
- incoming 13-cut and outgoing 12-cut: {x₃ ≥ z₂, x₂ < z₁};
- incoming 12-cut and outgoing 13-cut: {x₂ ≥ z₁, x₃ < z₂}.

On a non-null set H ⊆ Λ₁ ∩ Q₁ where the two chains are **comonotone** (x₃ = f(x₂) with f increasing, i.e. shared level
sets, same orientation), these corners are null at every point of the interior of H. So no cycle has a turning point
there, and ω|_H enters no cycle constraint.

Anti-monotone dependence (f decreasing) does **not** escape: there both anti-diagonal corners are non-null.

So the correct form of Q2.15′ is:

> **Q2.15′ (corrected).** In (V), with worlds 2 and 3 (Loc), e.g. additive with integrable densities, world 1 is ¬(Loc)
> as soon as ω is not 0-homogeneous on a non-null part of Λ₁ ∩ Q₁ (Q2.15 (N1); CORRECT). Under (Nest_e) at e₁, such a
> part must lie, up to null sets, where χ = (x₂, x₃) is not open: a comonotone link, or a degenerate crossing (Lemma R1,
> plus density points in the measurable case, CHECKED as in Q1's Remark). Otherwise it lies on a non-null crossing of a
> non-nested edge at e₁. N2.2′ allows such crossings anywhere inside Λ₁ ∩ R₁ⱼ, which is entirely a θ = 1 tie set of
> the CA edge field.

This is exactly Q1's shift of aim (Q_Q1, the comonotone link). The two notes should be merged on it.
- The ¬(Loc) half is free there, by Q2.15.
- What a construction must still supply is a comonotone link at e₁ on (+,−,−), carrying the L2/P1 structure on the
  shared chain.

### 1.5 Q2.15 and Q2.C

- **Q2.15 (N0)–(N2): CORRECT.** If world i were (Loc), Q2.12–Q2.14(a) would apply to any fixed data of j and k.
- **GAP in the closing remark** "By Q2.14(b), (N1) and (N2) can only hold on Λ_i ∩ Q_i".
  - Q2.14(b) is about the CA maximal endorsers ρ\*. (N1) is about the (Loc) data ρ_j, ρ_k, e.g. w_j, w_k.
  - For an additive partner, ρ\*_j need not be a multiple of w_j: a maximal-support endorser can be a mixture with other
    endorsers.
  - *Fix:* state the remark for (Loc) data taken equal to the maximal CA endorsers, or add a lemma that additive
    partners' endorsers are proportional to their densities.
- **Conjecture Q2.C: under-specified, and false in its natural reading.**
  - It does not say how world 1's edge chains are positioned on (+,−,−).
  - With transverse chains, which is what the linear-host / L2 chains give (Q1.26), Lemma R1 refutes it. So do Q1.25(b)
    and `q1_fiber_return.out`: L2-type lifted generators near the e₁ ray are undone in two or three forced moves.
  - *Fix:* restate it with a comonotone link H ⊇ the non-homogeneity region. That is a sub-case of Q_Q1.

### 1.6 Q2.14(a), (b) and Q_W

- **Q2.14(a), (b): CORRECT.** The algebra is trivial. The content is 0-homogeneity, from Q2.13(a) and N2.3 respectively.
- **Q_W: well posed.**
  - After Q2.10 it is precisely K3.5′(c)'s residual (R-i): Q2.10 relabels (R-ii) as sheltering.
  - Q2.13(c) gives (γ) on ∂Δ ∪ {p̂} only.
- **A field-level remark (a reading, not a theorem).**
  - On (+,−,−) ⊆ Q₁, B_t = {t₁ > t₂r₁₂ + t₃r₁₃} (with h = ρ₁).
  - The sublevel sets {r₁ⱼ ≤ s} ∩ (+,−,−) are world-1-correct parts of coherent edge models, so they are convex: each
    r₁ⱼ is quasi-convex there.
  - A positive combination of two quasi-convex 0-homogeneous functions need not have convex sublevel sets.
  - So no argument from the structure items 1–5 alone gives (W). Q_W needs ranking input at the sheltered depths, as
    §6.3 says.
- **§6.3 is a correct statement of a route, and claims nothing.** A face-preserving, convex-valued correspondence with
  closed graph is indeed onto (KKM/degree).

---

## 2. Q4

### 2.1 Q4.0: CORRECT

- **(a) Vertex continuity (risk item 2).**
  - The margin bound: q·(ℓ(a) − ℓ(a_b)) ≥ q_b m_b − (1−q_b)·2env. With |q − e_b|₁ = 2(1−q_b) and q_b ≥ ½, this is
    positive off {m_b ≤ 4env|q−e_b|₁}.
  - That set decreases to a null set.
  - The unique e_b-optimum is coherent because a coherent e_b-Bayes model exists by (γ₀).
  - Every coherent q-Bayes model agrees with it off the set, whatever the tie rule. This includes D♭, the directional
    families, and K_q off E.
  - R1 Prop. 3.1 then gives Hausdorff convergence.
  - E plays no role. CORRECT.
  - Note: it needs world b's ladder density > 0 on all of M (G = M), as stated.
- **(b) Prop. V.** On a ball B ⊆ N ∩ G around a b-crossing, D_K ∩ B = {h_b > 0} ∩ B. For h_b < 0 the e_b-optimum is
  silence or "accept −h", and both leave h ∉ D_K. A convex cone with this trace has supporting plane {h_b = 0}, and
  D_K ⊆ {h_b > 0} ⇔ e_b ∈ K by separation. CORRECT.
- **(c) V1.** CORRECT. Forced acceptance would put h with h_b < 0 into the coherent e_b-Bayes model, and that model lies
  in 𝓜.
- **(d).** CORRECT, by uniform |ψ^q − ψ^t| ≤ |q−t|₁∫env and dominated convergence. 𝓜 is closed in measure.

### 2.2 Theorem Q4.1: CORRECT

- **Step 1.** This is Prop. T1's certificate, and the write-up (§5, Prop. T1 proof) has it in exact form. The rerun of
  q4py (1) reproduces it: exact c₁(A)·q₀ = ηx(1−2s) − s and c₃(B)·q₀ = sx − (1−s)ζ, all conditions True for every
  failing pair and ε.
- **Step 2.** CORRECT, given (C3).
  - c(g)/|c(g)| → c_k(h)/|c_k(h)| as vectors in ℝ³, so c(g)·q₀ > 0 for good g near A, even at the edge prior q₀.
  - This is boxbridge(c)'s step.
  - *Cosmetic:* take δ(s) ≤ s, so that g_m → w\* in Step 6.
- **Step 3: the edge box with E, on a general domain (risk item 1).** I checked each link.
  1. q₀ ∈ R(A′) ∩ R(B′) is an open condition in aff Δ. O ∖ E accumulates at q₀ because E is null.
  2. At q ∉ E and good A′, B′: P(q, ·) > 0 by M3.7(a). M3.7(a) needs only uniqueness of the Bayes model off E and
     convexity of {P^F > 0}; no (Av) is involved.
  3. The ratio condition gives λ with z′_a, z′_b < 0. Superadditivity gives P(q, z′) > 0, so z′ + (0, r)³ ⊆ D_{K_q} for
     every such q: a q-independent set of positive measure.
     - If z′ ≤ 0 this is already impossible.
  4. On B(z′, 2r), every h has h_a, h_b < 0. By Q4.0(c), applicable because world b is non-degenerate near both
     crossings, an alternative to + is available. It is strictly better at a and at b. × is worse still.
  5. supp q₀ = {a, b}, so + has a strictly positive q₀-gap. By continuity in q, + is not q-optimal for |q − q₀| < r(h).
  6. Dominated convergence gives μ(B(z′,2r) ∩ D_{K_q}) → 0 along O ∖ E, a contradiction.
  7. Fubini over 𝒜 × ℬ completes the step.

  CORRECT. This is a cleaner general-domain replacement of Lemma edgebox's "H(A+λB)" step. The input that must not be
  forgotten is Q4.0(c), excluding forced acceptance, and the note supplies it.
- **Step 4.** CORRECT.
  - (LF) on G ⊆ N gives + and 0.
  - Without −, R(g) = {c·q > 0} ∋ q₀.
  - With −, d·q₀ ≤ 0, so c′·q₀ > 0.
  - On M_U this is Prop. T1's contradiction.
- **Step 5.** CORRECT. d_a and d_b have opposite strict signs, so d is non-constant along the edge. R(−g) is an open
  cell, and M3.7(a) for −g gives K_q ⊆ {m·g < 0}.
- **Step 6.** CORRECT, with Q4.0(a) at world b (non-degenerate on M). Hausdorff limits of the K_{q_m}, together with
  g_m/|g_m| → w\*, give V_b ⊆ {m·w\* ≤ 0}.
- **Step 7.** CORRECT.
  - h = w\* − δ𝟙 + ηe_b ∈ N, with h_b > 0. Acceptance is available and strictly world-b-best, so D_{V_b} contains a ball
    at h and P_{V_b}(h) ≥ 0.
  - Combined with Step 6: η m_b ≥ δ. Let δ/η → 1.
- **Step 8.** CORRECT. D_{e_b} ∈ 𝓜 gives + ∈ A(g) for g_b > 0. A failing pair exists at every b, and every mixed ±g has
  a positive coordinate, so (Av) holds. Then M3.7(d) applies.
- **Normalisations.** The diagonal rescaling moves p\* to u and leaves the domain, V_b and the advice ranges unchanged.
  The transposition (x₋ → x₊) permutes coordinates, and hence the domain. That is harmless, because the theorem is
  stated for all (LF) domains and T1 is symmetric.
- **"No apex / Thm B / [a\*, z\*] limits / edge confinement."** Confirmed.
  - M3.7(c), third item (R4 Thm B), is not used.
  - M3.7(d) is used only after (Av) is proved.

### 2.3 Lemma Q4.3: CORRECT

- **For x_l > 0.** D_{V_l} contains a ball B(x, 2r), so P_{V_l} ≥ r on B(x, r) by level shift. Hausdorff convergence
  (Q4.0(a)) is uniform on bounded sets, so P(q, h) > r/2 near e_l.
- **For x_l < 0.** P_{V_l}(x) ≤ −δ by the mirror argument.
- **Families covered.** K^♭ (coherent at every q by M3.4.2), the directional families (q-Bayes by construction), and K_q
  off E.
- This is D1.1(c)'s argument, with the directional limit replaced by Q4.0(a). It does not need V_l = {e_l}.

### 2.4 "M3.9 uses (Av) nowhere else": CHECKED stands

My spot checks, in addition to M23_referee §6.10:
- **N21.4 item 2.** UVN is used only to put the vertex neighbourhoods V_l ∩ Ω inside A_τ or B_τ. Imprecise V_l is
  harmless.
- **TSalways step (i).** The wall argument uses UVN neighbourhoods V_l, Lemma walls (a)–(d) (R4 Thm B, quasi-concavity)
  and c-cluster signs. Neither precise vertex models nor edge confinement appears.
- **D1.6 and Lemma M.** These are walls toward T1's vertices v_k, with vertex continuity of Q4.0(a) type.

I found no (Av) use. Upgrading beyond CHECKED needs M23_referee GAP (ii) (Thm PL with approximate walls) written out,
as Q4 says.

### 2.5 Corollary Q4.2: CORRECT at the status of M3.9

The chain is M3.4 → D1 (any (LF) domain, by its statement) → M3.6 + M3.9 + Q4.3 → Q4.1 → (Av) → M3.10 (M3.8 with
M3.7(d)). Each link is valid on a non-(Av) domain.
- For rankings that add up, M3.1's last clause gives a non-degenerate maximal field.
- R21 Part B: (GnAv-nd) is closed at [CH] with GAP (ii).
- R21 §0 item 9 and §5 item 6 should be updated.
- M3.C's purpose is served. M23_referee §6.13's objection (M3.9 under (Av)) is answered by Q4.3 plus the reading in
  §2.4 above.

### 2.6 Prop. Q4.4: CORRECT, with two GAPs

- **Bookkeeping (risk item 4).**
  - [B_b] supplies Q4.0(b), (c) near the crossings (Step 3), d_b ≠ 0 (Step 5), and s_b > 0 at the test gambles
    (Step 7).
  - [G_ab] supplies the strict q₀-gap in Step 3. Weak guidance at the other world suffices because q₀ has full support
    on {a, b}.
  - Q4.0(d) replaces Q4.0(a) in Step 6, giving a coherent e_b-Bayes limit with K\* ⊆ {m·w\* ≤ 0}.
  - The statement concludes "some coherent e_b-Bayes model is D_{e_b}", which is all that Step 8 needs.
  - CORRECT.
- **GAP (a).** Steps 3 and 5 use M3.7(a), (b), "good" gambles and D1.1(b) convexity for a possibly degenerate field.
  These are stated in M3 §5 for strictly guiding fields. Their proofs need only:
  - E(ψ) null;
  - a unique coherent Bayes model off E;
  - countably many non-generic directions.

  A zero penalty-difference vector on a non-null set would make E = Ω. *Fix:* spell out "(γ) on Ω" as "E(ψ) null and
  Bayes models coherent off E", and add one sentence transferring M3.7(a), (b).
- **GAP (b), wording.**
  - §0 (iii) says "[W_b] fails … automatic if p\* is not interior, or if (PC) fails". That reverses the logic. §5 item 3
    says correctly that failure of [W_b] *needs* one of these.
  - Moreover, "[W_b] comes from (PC)" for a degenerate field with non-degenerate restriction near p\* is not proved. Mark
    it CHECKED or CONJECTURE.

### 2.7 NUMERICS (q4py), rerun

The output is byte-identical. But:
- **(2) and (3)** compute the Step 7 LP bound itself. The "collapse to 1.3·10⁻³" is 1 − δ/η at the chosen
  η = δ(1+10⁻³). It is a restatement, not a test.
- **(5) is circular.**
  - The sampled V_b points satisfy the test-gamble constraints by construction (the test gambles are appended to Hb).
  - Survival needs m·w\* ≤ 0, hence m_b ≥ 1/(1+10⁻⁴).
  - Points are sampled at distance ≥ 10⁻³ from e_b.
  - So 0 survivors is forced and carries no information.
- **(4).** The "force the boundary case d·q₀ = 0" branch is `pass`. Only the generic case d·q₀ < 0 is sampled, which is
  trivial (an open cell).

None of these is load-bearing.

---

## 3. Requested changes

1. **Q2 §0 item 2, Q2.14(c), Q2.15′ bullets 4–5 and Reading, §7 "Why this does not give (I)", §8 2(b).**
   - Add Lemma R1 / Q1.20–Q1.22 to the list of constraints on Λ_i ∩ Q_i.
   - Restrict every freedom claim to the comonotone (or non-open-χ) part of the link class, or to non-nested edges.
   - Replace Q2.15′ by the corrected form of §1.4.
   - Cross-reference Q1 and adopt Q_Q1 as the single lead.
2. **Q2.C.** Restate with a comonotone link containing the non-homogeneity region, or withdraw it.
3. **Q2.15's closing remark.** Separate (Loc) data from CA endorsers (§1.5).
4. **Q2.10 Reading.** Write "(R-ii) absorbed into (R-i)".
5. **Q2.12 header.** Add (LA).
6. **Q2 §8.** Replace "Q2.11 transfers verbatim" by the M3.4(3)-type selection argument.
7. **Q4.**
   - Step 2: δ(s) ≤ s.
   - Q4.4: GAP (a) sentence; fix §0 (iii) wording; label "[W_b] from (PC)" for degenerate fields.
   - Relabel NUMERICS (2), (3), (5) as restatements, and fix or delete the dead branch of (4).
8. **R21.**
   - (GnAv-nd) is closed at the status of M3.9 (Q4.2).
   - (V) with (RL-2) partners: under (Nest_e) + local transversality at e₁, a non-0-homogeneous partner ratio is
     excluded by strict (G). The surviving (V) designs need comonotone links or non-nested edges at e₁ (Q1, Lemma R1).

## 4. Files

- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/q24ref_py/q4_rerun.py`, `.out`,
  `.stdout`: rerun of q4py, identical output.
- `/tmp/claude-0/-home-claude/516e9253-01b8-5264-9018-734bfcf63f58/scratchpad/r9/q24ref_py/radial_cycle.py`, `.out`:
  Lemma R1 sanity check (deposit ratio 0.725).
