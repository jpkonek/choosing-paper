# N25. The exceptional-tie case M0, proof side: structure of E(ψ), what (S) forces, and what is left

14 Oct 2026. Task: BRIEF8, proof side. Labels: **PROVED** (full proof written here), **CHECKED** (verified against
the source; proof imported or sketched), **CONJECTURE**, **NUMERICS**. No scripts were needed and no claim rests on
numerics (`n25py/` was not created).

Terminology as in the Glossary of *START HERE -- Coverage Status.md*. Notes are cited by file name.

---

## Standing hypotheses and notation

**(H25)**
- n = 3.
- The domain is the U-domain M_U, with U = D_{K′} and K′ = u + s(T1 − u), 0 < s < 1. An evaluable model is a measurable
  X ⊆ U modulo μ-null sets.
- The ranking L has one preorder per world and satisfies strict (G), (IB), (LA), (S) (LDG preorder sense) and (C).
- T1 ∈ C_L. (LF) at T1 is automatic on M_U.
- p ↦ C_p is a selection with the properties in (S). A_i(X) := {p : C_p ⪯_i X} is closed.
- **(M0).** Every world adds up: there is a charge ν_i ≥ 0 on U, vanishing on null sets and positive on non-null sets, with
  ν_i(E_i(B)) ≤ ν_i(E_i(X)) whenever B ∈ C_L, X is regular and B ⪯_i X.
- ψ_i(X) := ∫_U 1_{E_i(X)} ρ_i dμ, where ρ_i is the density of the countably additive part of ν_i. By N19 Lemma R1,
  ρ_i > 0 a.e. on U. Put c_i(g) := ρ_i(g)·sign(g_i). Then the q-Bayes rule is "accept g iff q·c(g) > 0",
  B_q := {g ∈ U : q·c(g) > 0}, and the tie set at q is Z_q := {g ∈ U : q·c(g) = 0}.
- E := E(ψ) := {q ∈ int Δ : μ(Z_q) > 0}. For q ∉ E, K_q is the credal set with B_q = D_{K_q} a.e.
- P(q,g) := P_{K_q}(g) for q ∉ E.
- ℛ := {ψ(X) : X ∈ M_U}, which is compact and convex (Lyapunov). V(t) := min_{y∈ℛ} t·y. The face at t is
  F_t := argmin_ℛ t·y.
- A *realiser* of y ∈ ℛ is a model X with ψ(X) = y.

**Properties of ψ imported for (M0)** (N13 Prop B, N22 Thm 2.1; BRIEF8):
- (α) T1 is ψ-Bayes at an interior weighting p\*;
- (β) at every weighting some ψ-Bayes model is coherent;
- (γ) E is Lebesgue-null, and B_q is coherent for q ∈ int Δ ∖ E;
- (δ) the vertex Bayes models are coherent.

**(E_ψ) (an extra hypothesis, used only in §§1.2, 7–9).** ψ itself endorses the relevant comparisons:
B ∈ C_L, X regular, B ⪯_i X ⇒ ψ_i(B) ≤ ψ_i(X). This holds when the ν_i are countably additive (then ψ_i = ν_i). It
can fail when ν_i has a purely finitely additive part, because ψ_i is then only the integral part of ν_i.

---

## 0. Outcome

**Verdict.** I did not find a contradiction, and I did not find a construction. Several things are now proved:
- the exceptional set has a rigid structure: countably many full chords, plus countably many points;
- perturbing the supporting assessment removes every chord that is not forced, but in general it cannot remove the
  points;
- under (E_ψ), closed competitive choice forces the ranking to break ψ's ties "ideally", at almost every tied profile.
  This is an (n−1)-dimensional analogue of R2 Theorem 7 and R7 Lemma SF, and it needs no lexicographic structure;
- along a chord of E, (IB) makes every undominated way of splitting the tie the same at every weighting on the chord.
  Each such split must give a coherent model at every one of those weightings.

None of this yields a contradiction. As written, the N15 argument needs continuity on all of int Δ, with the box as
the only exception (§9.3). If p\* ∈ E, N15 cannot be applied at p\* even in principle.

### Numbered claims

**N25.1 (PROVED) Structure of E.** Assume only (γ) (any integral field with strict signs on M_U).
- V is concave on Δ. In int Δ it is differentiable exactly off E, and ∂V(t) = F_t.
- E = ⋃_k (ℓ_k ∩ int Δ) ∪ F. Here the ℓ_k are countably many *atom lines*: each is the chart line common to a non-null set
  G_k of gambles. F is a countable set of *fan points*: at a fan point, a non-null set of gambles has chart lines through
  the point, spread over a non-atomic set of directions.
- E meets every other line in a countable set.
- N22's "jump line" and "fan" are thus the only two possibilities, and there are countably many of each.

**N25.2 (PROVED) Coherent envelopes at every weighting.** Assume (γ). For every q ∈ int Δ:
- the strict Bayes set B^s_q := {q·c > 0} is coherent;
- for all but countably many directions δ, the directional limit X_δ := B^s_q ∪ (Z_q ∩ {δ·c > 0}) is coherent;
- every exposed point of F_q is ψ(X_δ) for some δ, and every extreme point of F_q has a coherent realiser;
- the canonical family K^♭_q (defined by D_{K^♭_q} = B^s_q) is upper semicontinuous on int Δ, equals K_q off E, and is
  continuous exactly at the points of int Δ ∖ E.

**N25.3 (PROVED) Anatomy of an atom.** Let G be an oriented atom: c(g) ∈ ℝ_{>0}b on G, with line ℓ = {q·b = 0}.
- G lies in a single open orthant O_σ, σ = sign b, and ℓ separates the vertices accordingly.
- At every q ∉ E on the positive side of ℓ the Bayes model contains G; at every q ∉ E on the negative side it misses G.
  This is global on int Δ.
- At every point t of a co-countable subset ℓ° of the chord, B^s_t and B^s_t ∪ G are coherent. So G is a coherent conic
  shell, G = D_{K_+(t)} ∖ D_{K^♭_t}.
- The support functions of K^♭_t and K_+(t) in the directions of G (mod 𝟙) do not depend on t ∈ ℓ°.
- *Cliff:* for g in the 𝟙-saturation of G, P(q,g) ≥ π⁺(g) on one side of ℓ and P(q,g) ≤ π^♭(g) on the other, with
  π⁺ > π^♭.

**N25.4 (PROVED) Anatomy of a fan point.** At a fan point x, B^s_x ∪ (Z_x ∩ γ^{−1}A) is coherent for every open arc A
of chart directions of length < π (endpoints outside a countable set). So the tie set is a family of coherent shells,
indexed by arcs of directions and additive over adjacent arcs. The face F_x has dimension ≤ 2, and all its extreme points
have coherent realisers.

**N25.5 (PROVED) Perturbation within the cone of supporting assessments.** Let 𝒩 be the convex cone of supporting
assessments (CA parts of endorsing charges; under (E_ψ), the endorsing integral fields).
- (a) *Pairwise.* For ψ, ψ′ ∈ 𝒩, for all but countably many s ∈ [0,1], every atom of (1−s)ψ + sψ′ lies in the *rigid set*
  R(ψ,ψ′). This is the set on which the chart direction of every mixture is locally constant. So such atoms are atoms
  of both ψ and ψ′.
- (b) *Generic member.* Some ψ\* ∈ 𝒩 has an atom set A\* of least measure, and A\* is contained (mod null) in the atom
  set of every member of 𝒩. If μ(A\*) = 0, then E(ψ\*) = F(ψ\*) is **countable**: there are no atom lines.
- (c) *Fans and rescalings cannot be perturbed away in general.* Per-world rescaling ψ ↦ κ⊙ψ always stays in 𝒩. It
  carries E and p\* together by a projective map of Δ, so E ≠ ∅ and "p\* ∈ E" are invariant under it. For fixed x the
  mixtures that tie at x are countable, but fan points can move with s.

So "a supporting assessment can always be chosen with E = ∅" is **not** provable by genericity. What genericity gives
is: no atom lines unless they are forced on every member.

**N25.6 (PROVED, needs (E_ψ)) The selection's ψ-profile is continuous where it matters.** Combine closed sections,
competitiveness and (G):
- *(LSC)* If q_m → p̄ and C_{q_m} → C_∞ in measure, then ψ(C_{p̄}) ≤ ψ(C_∞).
- *(USC)* If C_p admits arbitrarily cheap "all-but-j" improvements, then limsup_{q→p} ψ_j(C_q) ≤ ψ_j(C_p).
- Together: p ↦ ψ(C_p) is continuous at every p whose selected credal set lies in int Δ.

The LSC step is the "upper envelope of the tail" that N22 Remarks 3.3 could not use for charges. It works because ψ is
an integral.

**N25.7 (PROVED, needs (E_ψ)) Lemma Q: approach from a quadrant forbids hidden improvement.** Suppose q_m → p̄ and
ψ_i(C_{q_m}) > y_i for all i ≠ j. Then no regular Z has Z ≺_j C_{p̄} and ψ_i(Z) ≤ y_i for all i ≠ j.

**N25.8 (PROVED, needs (E_ψ)) The (n−1)-dimensional staircase.** Call C_p *j-improvable* if some regular Z has
Z ≺_j C_p and ψ_i(Z) ≤ ψ_i(C_p) for all i ≠ j. The set {(ψ_i(C_p))_{i≠j} : C_p j-improvable} is contained in countably
many graphs of 1-Lipschitz functions over the line 𝟙^⊥ ⊂ ℝ². In particular it is Lebesgue-null in ℝ². Consequences:
- *Fans.* At a 2-dimensional face, for area-a.e. tied profile y, no selected realiser of y is j-improvable for any j.
  So the undominated realisers of y contain no strict comparisons at any world (ideal tie-breaking).
- *Atoms.* Let j be the odd world of σ (the world whose sign differs from the other two). Along each atom face, all but
  countably many tied profiles have no j-improvable selected realiser.
- *Generic profiles.* For a.e. frontier profile y = ψ(B_w), world j never strictly prefers to B_w a model that is
  ψ-no-worse at the other two worlds.

**N25.9 (PROVED, needs (E_ψ)) Atoms under the ranking: (IB) transport.** Let G be an atom on ℓ with odd world j.
- The set 𝒰 of undominated "tie splits" S ⊆ Z_t is the same for all t ∈ ℓ°.
- For S ∈ 𝒰, B^s_t ∪ S is coherent for **every** t ∈ ℓ°.
- At every mass level θ (θ ∈ (0,1] if σ_j = −, θ ∈ [0,1) if σ_j = +) some selected split S_θ ∈ 𝒰 is ≤_j-minimal
  among all splits whose ψ-profile is no worse at the two worlds other than j.

**N25.10 (PROVED) The target at an exceptional weighting.** If p\* ∈ E, some boundary gambles h of D_{T1} (a relatively
open set of them) have q ↦ P(q,h) discontinuous at p\*: a directional limit is ≠ 0 = P_{T1}(h). Hence the N15 chain
cannot start at p\*. If p\* is a generic point of an atom line with pattern ±σ, the affected gambles have sign pattern σ
or −σ. Taking σ with single negative coordinate k, these are:
- the middle arc of F_k;
- the arcs adjacent to the corner ray r_{ii′} ({i,i′,k} = Ω).

**N25.11 (PROVED: the box is E-robust; CHECKED: the rest is not localisable).**
- Lemma edgebox (writeup Lemma `lem:edgebox`) holds for every integral field whose Bayes models are coherent at a.e.
  weighting. So the edge approaches never need uniqueness.
- The straight-level and pivot steps (Lemma `lem:levels`; Lemma `lem:nopin` via co(G ∪ V_l); Thm `thm:pivot`) use
  continuity of K on half-planes and wedges through p\* whose union is all of int Δ.
- Only the blow-up steps are local at p\*, and only after the pivot theorem. So the answer to the brief's item (d) is
  negative for N15 as written.
- **CONJECTURE N25.L.** N15 goes through when p\* ∉ E and E is countable and closed.

**N25.12 Brief's premise checked.** "Each incoherent ψ-minimiser Y at an exceptional t is weakly dominated by a selected C
with ψ(C) = ψ(Y)" is PROVED under (E_ψ) (§1.2). Without (E_ψ), when ν_i has purely finitely additive parts, I could not
prove it: endorsement gives only ν_i(E_iC) ≤ ν_i(E_iY), with uncontrolled singular parts. The glossary's sentence "it
endorses the relevant comparisons" is therefore an assumption when ν_i is not countably additive.

### Which configurations of E(ψ) remain possible (§10 for details)

Under (H25) + (M0) + (E_ψ), and choosing ψ = ψ\* generic (N25.5(b)), a cover of T1 requires one of:

| | Configuration | Excluded by N15? | What is forced |
|---|---|---|---|
| R-a | **p\* ∈ E** (atom through p\*, or fan at p\*); T1 an intermediate or end realiser at p\* | No: N15 cannot start (N25.10) | N25.8–9 at p\*; T1 coherent among ψ-equal splits |
| R-b | p\* ∉ E, **persistent atoms** (μ(A\*) > 0): every supporting assessment has an atom line | No: N15 uses continuity on all of int Δ (N25.11) | Uniformly coherent splits along each atom chord (N25.9); odd-world ideal breaking (N25.8) |
| R-c | p\* ∉ E, μ(A\*) = 0, **countably many fan points** | Open: CONJ N25.L would cover the case F closed | Arc-shell structure (N25.4); a.e.-ideal breaking on 2-dim faces (N25.8) |

Excluded outright:
- (i) tie-breaking that makes a selected model j-improvable at no ψ-cost elsewhere on a set of tied profiles whose
  projection has positive area. This is different from, and complementary to, the lexicographic exclusions of R2 Thm 7
  (§7.4).
- (ii) non-persistent atoms (perturb them away).
- (iii) E = ∅ for some member (N15).

---

## 1. Preliminaries

### 1.1 (α)–(δ) under (E_ψ) (CHECKED; direct re-derivation)

Under (E_ψ) the imported properties have short direct proofs. I record them because §§7–9 use the same mechanism.
- (β) Fix p ∈ Δ and let B be a pointwise ψ-p-minimiser, which is regular. By Fact 0 (LDG thm:kkm) some selected
  C ⪯_i B at every i. By (E_ψ), ψ(C) ≤ ψ(B), so C is p-Bayes and coherent.
- (γ) This is Tonelli on U × Δ: for a.e. g, the tie set {q : q·c(g) = 0} is a line. Off E the minimiser is pointwise
  unique, so it equals the coherent one from (β).
- (α) Lemma IC (R11, refereed in R13) makes T1 competitive on Ω. If a regular X had ψ_i(X) < ψ_i(T1) at every i, then
  T1 ⪯_i X for some i, and (E_ψ) would give ψ_i(T1) ≤ ψ_i(X), a contradiction. Lyapunov and separation give a supporting
  weight, and strict guidance pushes it into int Δ (R11 Thm W(d)).
- (δ) Strict guidance and the vertex lemma.

**Lemma 1.1 (PROVED; selected models are ψ-supported).** Under (E_ψ), every selected C_p is ψ-w-Bayes for some w ∈ Δ
with supp w ⊆ supp p.

*Proof.*
- Competitiveness on S = supp p and (E_ψ) give: no regular X has ψ_i(X) < ψ_i(C_p) for all i ∈ S.
- The regular models form a decomposable subdomain, so their profiles form a convex compact set. Separation in ℝ^S gives w with
  supp w ⊆ S minimising w·ψ over regular models at C_p.
- Pointwise w-minimisers are regular, since a unanimous problem has its correct advice strictly best at every world.
  So C_p is w-Bayes. ∎

### 1.2 Face points are selected profiles; the brief's premise (N25.12) (PROVED under (E_ψ))

**Lemma 1.2.** Let t ∈ int Δ and y ∈ F_t. Then y = ψ(C_p) for some selected C_p, and C_p is t-Bayes. If Y is t-Bayes,
there is a selected C with C ⪯_i Y at every i and ψ(C) = ψ(Y). If moreover Y is incoherent, then C ≺_j Y at some j.

*Proof.*
- y is the profile of a pointwise t-minimiser Y (Lyapunov: F_t is the set of profiles of pointwise minimisers, ψ being
  integral).
- Fact 0 gives a selected C ⪯_i Y at every i. By (E_ψ), ψ(C) ≤ ψ(Y), since Y is regular.
- t·ψ(C) ≥ V(t) = t·ψ(Y) with t > 0 forces equality.
- If C ~_i Y at every i, (C) makes Y coherent. ∎

Without (E_ψ) the second step fails. Endorsement gives ψ_i(C) + ν^s_i(E_iC) ≤ ψ_i(Y) + ν^s_i(E_iY), and the singular
parts are not controlled. N13 Prop B (β)'s carrier argument yields only near-minimisers and, in the limit, *some*
coherent minimiser, never one with the profile of a prescribed Y. This is N25.12.

---

## 2. Structure of the exceptional set (N25.1)

### 2.1 The value function

Pointwise, on M_U:
- silence at g costs Σ_{i:g_i>0} t_iρ_i;
- acceptance costs Σ_{i:g_i<0} t_iρ_i;
- the difference is t·c(g).

Hence
 V(t) = ∫_U Σ_{i: g_i>0} t_iρ_i dμ − Φ(t),  Φ(t) := ∫_U [t·c(g)]₊ dμ(g),
with Φ convex and positively homogeneous, and V concave.

By dominated convergence (|c| ∈ L¹), the one-sided directional derivative of Φ at t in direction δ is
 Φ′(t;δ) = ∫_{t·c>0} δ·c dμ + ∫_{Z_t} [δ·c]₊ dμ.

For δ ∈ 𝟙^⊥ (the tangent space of aff Δ), Φ′(t;δ) + Φ′(t;−δ) = ∫_{Z_t} |δ·c| dμ. So V is differentiable at t (along
aff Δ) iff δ·c(g) = 0 for a.e. g ∈ Z_t and every δ ∈ 𝟙^⊥, i.e. iff c(g) ∝ 𝟙 a.e. on Z_t. But t·c(g) = 0 with t ∈ int Δ
and c(g) ∝ 𝟙 forces c(g) = 0, which strict signs exclude. So

 **V is differentiable at t ∈ int Δ iff μ(Z_t) = 0, i.e. iff t ∉ E.**

By Danskin's theorem the superdifferential of V at t is F_t. ∎

*Remark (general decomposable domains).* For advice ranges ⊆ {+,0,−,×} the same holds with one tie line per pair of kinds of advice in the advice range.
- The pair {+,−} on a mixed problem has a mixed strict difference vector.
- A pair involving ×, or a pair on a unanimous problem, has a one-signed difference and never ties in int Δ.

### 2.2 Lines and pencils

**Setup.**
- Unanimous g have one-signed c(g) and never tie in int Δ. For mixed g let γ(g) := c(g)/|c(g)| ∈ S², and let
  m := γ_*(μ|_{U_mix}), a finite Borel measure on S².
- For q ∈ int Δ let Π_q := S² ∩ q^⊥, a great circle. Then μ(Z_q) = m(Π_q). For q ≠ q′ in int Δ (never proportional),
  Π_q ∩ Π_{q′} = {±(q×q′)/|q×q′|}, two points.
- Decompose m = m_a + m_c, with m_a purely atomic and m_c non-atomic. The atoms are countably many points b_k.
  - Each b_k has mixed signs: it is the direction of c(g) for mixed g.
  - So ℓ_k := {q ∈ aff Δ : q·b_k = 0} meets int Δ.
  - The *oriented atom* is G_k := γ^{−1}(b_k). The antipode −b_k gives the same line, with the opposite orientation.

**Theorem 2.1 (PROVED).** E = ⋃_k (ℓ_k ∩ int Δ) ∪ F, where F := {q ∈ int Δ : m_c(Π_q) > 0} is countable.

*Proof.*
- If q ∈ ℓ_k, then b_k ∈ Π_q and m(Π_q) ≥ m({b_k}) > 0.
- If q ∈ E, then m_a(Π_q) > 0 (some atom lies on Π_q, so q ∈ some ℓ_k) or m_c(Π_q) > 0 (q ∈ F).
- *Countability of F.* For q ≠ q′ in F, m_c(Π_q ∩ Π_{q′}) = 0, since the intersection is two points and m_c is
  non-atomic. So for every finite subfamily, Σ m_c(Π_q) = m_c(⋃Π_q) ≤ m(S²). Hence at most N·m(S²) points of F have
  m_c(Π_q) > 1/N. ∎

**Corollary 2.2 (PROVED).**
- E is Lebesgue-null.
- E meets every line of aff Δ that is not one of the ℓ_k in a countable set.
- E contains a segment only along some ℓ_k, and then contains the whole open chord ℓ_k ∩ int Δ.
- This sharpens the Zajíček-type description in BRIEF8: no curved pieces can occur.

*Remark.* Nothing here bounds the number of atom lines or fan points below "countable", and nothing prevents E from
being dense. Total atom mass is ≤ μ(U), and each fan point carries positive mass.

---

## 3. Coherent envelopes (N25.2)

Fix q ∈ int Δ. Let D_q be the countable set of directions (in 𝟙^⊥, up to sign) of atom lines through q.

**Lemma 3.1 (PROVED).** For δ ∈ 𝟙^⊥ ∖ D_q, X_δ := B^s_q ∪ {g ∈ Z_q : δ·c(g) > 0} is coherent, and
X_δ = lim_{s↓0, q+sδ∉E} B_{q+sδ} in measure.

*Proof.*
- *The ray avoids E except at countably many points.* The ray {q+sδ : 0 < s < s₀} lies on no ℓ_k. So it meets each ℓ_k at
  most once, and F is countable. Hence there are s_m ↓ 0 with q_m := q + s_mδ ∉ E, and B_{q_m} = D_{K_m} by (γ).
- *Pointwise limits.*
  - For g ∉ Z_q, sign(q_m·c(g)) → sign(q·c(g)).
  - For g ∈ Z_q, q_m·c(g) = s_m δ·c(g), so the sign is sign(δ·c(g)).
  - The set {q·c = 0 = δ·c} is the set of g whose chart line is the line through q in direction δ. That line is not an
    atom line, so the set is null.
  - So 1_{B_{q_m}} → 1_{X_δ} a.e., hence in measure.
- *Coherence of the limit.* Credal sets ⊇ K′ are Hausdorff-compact. If K_m → K, then D_{K_m} → D_K in measure (R1 Prop 3.1;
  CBOI lem:compact). So X_δ = D_K. ∎

**Lemma 3.2 (PROVED).** Countable intersections of coherent models are coherent: ⋂_m D_{K_m} = D_{K_∞} a.e., with
K_∞ := cl co ⋃K_m.

*Proof.*
- P_{K_∞} = inf_m P_{K_m}, so D_{K_∞} ⊆ ⋂ D_{K_m}.
- The difference lies in {P_{K_∞} = 0}, the boundary of the closed convex cone {P_{K_∞} ≥ 0}.
- That cone has interior (it contains ℝ³₊), so its boundary is null. ∎

**Theorem 3.3 (PROVED; N25.2).**
- (a) B^s_q is coherent for every q ∈ int Δ. It is the largest-credal-set coherent ψ-q-Bayes model: every coherent
  q-Bayes D_K has K ⊆ K^♭_q, where D_{K^♭_q} := B^s_q.
- (b) Every exposed point of F_q in a direction δ ∉ D_q is ψ(X_δ). Every extreme point of F_q has a coherent realiser.
- (c) q ↦ K^♭_q is upper semicontinuous: if q_m → q and K^♭_{q_m} → K, then K ⊆ K^♭_q. It equals K_q off E, and it is
  continuous at q iff q ∉ E.

*Proof.*
- (a)
  - For g ∈ Z_q, {δ : δ·c(g) < 0} is an open half-circle, so it meets a countable dense set Q ⊆ 𝟙^⊥ ∖ D_q. Hence
    B^s_q = ⋂_{δ∈Q} X_δ.
  - Lemmas 3.1 and 3.2 give coherence.
  - B^s_q is a pointwise minimiser, hence q-Bayes. Every q-Bayes model contains B^s_q.
- (b)
  - Among q-Bayes models B^s ∪ S (S ⊆ Z_q), δ·ψ(B^s ∪ S) = δ·ψ(B^s) − ∫_S δ·c. This is minimised exactly by
    S = {δ·c > 0}, uniquely mod null when δ ∉ D_q.
  - The δ ∈ 𝟙^⊥ give every linear functional on the plane q^⊥ of F_q: δ ↦ δ|_{q^⊥} is injective, since δ ∝ q is
    impossible for δ·𝟙 = 0 = q·𝟙 − 1. For δ ∈ D_q the δ-face of F_q is a non-degenerate segment, because a non-null
    atom has δ·c = 0. So the exposed points of F_q are exactly the ψ(X_δ), δ ∉ D_q.
  - By Straszewicz's theorem every extreme point is a limit of exposed points ψ(X_{δ_m}). The realisers X_{δ_m} have a
    subsequence converging in measure to a coherent model (compactness). Its profile is the limit, because ψ is
    continuous in measure.
- (c)
  - If q·c(g) > 0 then q_m·c(g) > 0 eventually, so 1_{B^s_q} ≤ liminf 1_{B^s_{q_m}} pointwise.
  - In the limit (R1 Prop 3.1), D_{K^♭_q} ⊆ D_K, i.e. K ⊆ K^♭_q.
  - At q ∉ E, Z_q is null, so 1_{B^s_{q_m}} → 1_{B_q} a.e. for any q_m → q: continuity.
  - At q ∈ E two directional limits differ (Lemma 3.1 with δ and −δ: they differ exactly on Z_q), so there is no limit. ∎

So a coherent Bayes family K^♭ exists on all of int Δ. It has half-plane charts (for a.e. g, {q : g ∈ B^s_q} =
H(g) ∩ int Δ), and it is semicontinuous with discontinuities exactly on E. This is the precise sense in which (BU) fails
only "at E". Hausdorff continuity on int Δ, which N15 uses (writeup Rem. `rem:N20`), fails exactly there.

---

## 4. Anatomy of an atom (N25.3)

Fix an oriented atom G := γ^{−1}(b), its line ℓ := {q·b = 0}, the open sides H^± := {±q·b > 0}, and σ := sign b.
- Let G′ := γ^{−1}(−b), possibly null; it is the oppositely oriented atom on the same line.
- Let ℓ° := (ℓ ∩ int Δ) ∖ (F ∪ ⋃_{ℓ_k≠ℓ} ℓ_k). It is co-countable in the chord.
- For t ∈ ℓ°, Z_t = G ∪ G′ mod null.

**Theorem 4.1 (PROVED).**
- (a) G ⊆ O_σ := {g : sign g = σ} mod null, and e_i ∈ H⁺ iff σ_i = +.
- (b) For every q ∈ int Δ ∖ E: G ⊆ B_q if q ∈ H⁺, and G ∩ B_q = ∅ if q ∈ H⁻ (mod null).
- (c) For t ∈ ℓ°: B^s_t, B^s_t ∪ G and B^s_t ∪ G′ are coherent. They are the limits from the two sides, and F_t is the
  segment {ψ(B^s_t) − λb : −∫_{G′}|c| ≤ λ ≤ ∫_G|c|} (in units where |b| = 1). B^s_t realises an interior point of F_t
  when both G and G′ are non-null.
- (d) G = D_{K_+(t)} ∖ D_{K^♭_t} mod null, with D_{K_+(t)} := B^s_t ∪ G. So G is conic mod null.
- (e) *(Frozen support.)* Let Π := the essential 𝟙-saturation of G, i.e. the g whose line g + ℝ𝟙 meets G in a non-null
  set. On Π, P_{K_+(t)} and P_{K^♭_t} do not depend on t ∈ ℓ°. Call them π⁺, π^♭; then π^♭ < π⁺ on Π, and
  G ∩ (g+ℝ𝟙) = {g − s𝟙 : π^♭(g) ≤ s < π⁺(g)}.
- (f) *(Cliff.)* For g ∈ Π: P(q,g) ≥ π⁺(g) for all q ∈ H⁺ ∖ E, and P(q,g) ≤ π^♭(g) for all q ∈ H⁻ ∖ E.
- (g) For a.e. g ∈ Π ∖ G, the chart line of g does not cross the open chord ℓ ∩ int Δ. Gambles whose directions mod 𝟙
  are those of G never switch along ℓ.

*Proof.*
- (a) c(g) has the strict sign pattern of g; e_i·b = b_i.
- (b) For g ∈ G, q·c(g) has the sign of q·b.
- (c) This is Lemma 3.1 at t, with δ transversal to ℓ (D_t = {direction of ℓ}). Then {δ·c > 0} ∩ Z_t = G if δ·b > 0
  and = G′ if δ·b < 0. Theorem 3.3(a) gives B^s_t. The face is the Lyapunov range of the vector measure −c μ on G ∪ G′,
  and c is parallel to b there.
- (d) is (c).
- (e) Since P_K(g − s𝟙) = P_K(g) − s, the 𝟙-section of D_{K_+}∖D_{K^♭} through g is the stated interval.
  - G is fixed. By Fubini along 𝟙, for a.e. g ∈ Π the interval's endpoints agree for any two t, t′ ∈ ℓ°.
  - Continuity of P_K in g gives equality on all of Π (on the support of Π).
- (f) Let q ∈ H⁺ ∖ E and s ∈ (π^♭(g), π⁺(g)).
  - Then π^♭(g − s𝟙) < 0 < π⁺(g − s𝟙). The open set {π^♭ < 0 < π⁺} lies in G mod null, so its points are density points
    of G ⊆ B_q = D_{K_q}.
  - Hence P(q, g − s𝟙) ≥ 0, i.e. P(q,g) ≥ s. Let s ↑ π⁺(g).
  - The H⁻ case is symmetric: G ∩ D_{K_q} = ∅ gives P(q, g − s𝟙) ≤ 0, i.e. P(q,g) ≤ s. Let s ↓ π^♭(g).
- (g) For g ∈ Π with π^♭(g) > 0, g ∈ D_{K^♭_t} for all t ∈ ℓ°. By Fubini on U × ℓ°, t·c(g) > 0 for a.e. t ∈ ℓ°, and a
  half-plane chart then contains the open chord. The case π⁺(g) ≤ 0 is symmetric. ∎

*Reading.*
- An atom is a coherent "cliff" across a full chord of Δ.
- Along the chord, only the parts of K^♭_t not facing G can move.
- The jump is the same along the whole chord, P(·,g) jumping by at least π⁺(g) − π^♭(g).
- This is N22's "jump line", now with its global geometry pinned down.

---

## 5. Anatomy of a fan point (N25.4)

Fix x ∈ F. For g ∈ Z_x, γ(g) lies on the great circle Π_x.
- For δ ∈ 𝟙^⊥, δ restricted to x^⊥ is nonzero (x·𝟙 = 1 ≠ 0 = δ·𝟙). So {δ·c > 0} ∩ Z_x = Z_x ∩ γ^{−1}(Θ(δ)), with
  Θ(δ) an open half of Π_x, and every open half arises.
- For an arc A ⊆ Π_x put Z_x(A) := Z_x ∩ γ^{−1}A.

**Theorem 5.1 (PROVED).**
- (a) For every open half-circle Θ with endpoints off the countable set of m-atoms on Π_x, X_Θ := B^s_x ∪ Z_x(Θ) is
  coherent. Also X_Θ ∪ X_{−Θ} = B^s_x ∪ Z_x mod null.
- (b) For every open arc A of length < π with endpoints off that set, B^s_x ∪ Z_x(A) is coherent. If A, A′ are adjacent
  with |A ∪ A′| < π, then (B^s ∪ Z(A)) ∪ (B^s ∪ Z(A′)) = B^s ∪ Z(A ∪ A′) is coherent.
- (c) F_x has dimension ≤ 2. It equals ψ(B^s_x) − {∫_S c dμ : S ⊆ Z_x}, and all its extreme points have coherent
  realisers.

*Proof.*
- (a) Lemma 3.1, with half-circles corresponding to directions δ ∉ D_x.
- (b) An arc of length < π is the intersection of two open half-circles. Use Lemma 3.2.
- (c) The profiles of x-Bayes models are ψ(B^s) − ∫_S c, S ⊆ Z_x, and c(Z_x) ⊆ x^⊥. Use Theorem 3.3(b). ∎

*Reading.* Every short arc of chart directions through x carries a coherent extension of D_{K^♭_x}. The extensions are
disjoint for disjoint arcs, and adjacent ones combine. Near x, K_{x+rδ} ≈ K_{Θ(δ)} depends on the direction δ only: a
rotating truncation of K^♭_x. This is N22's "fan".

**Remark 5.2 (why fans matter for N15).** A degree-0 family q ↦ K(θ(q − x)) near x is compatible with half-plane
charts, provided each gamble's acceptance set of angles is ∅, full, or a half-circle. N15's blow-ups at p\* presuppose
P(q,h) → 0 as q → p\*. At a fan point that fails (N25.10). So a fan at p\* is the natural escape from the corner/box
contradiction. I have neither excluded nor built one.

---

## 6. Perturbation within the cone (N25.5)

Let 𝒩 be the set of supporting assessments: integral fields ψ′ on M_U with densities > 0 a.e. that arise as CA parts of
endorsing charges (under (E_ψ): integral fields that endorse the relevant comparisons).
- 𝒩 is a convex cone, and every member satisfies (α)–(δ).
- It is closed under countable sums Σw_kψ_k when Σw_k‖ψ_k‖ < ∞: the CA part is a norm-continuous linear projection, and
  endorsement inequalities add.

For two members ψ, ψ′ write ψ^s := (1−s)ψ + sψ′ and c^s := (1−s)c + sc′, whose sign pattern is that of g for s ∈ [0,1].

*Rigid set.* R(ψ,ψ′) is the essential union, in the measure algebra, of the non-null W on which, for every s ∈ [0,1],
γ^s(g) := c^s(g)/|c^s(g)| is constant on W.
- R(ψ,ψ′) ⊆ A(ψ) ∩ A(ψ′), where A(·) denotes the union of the oriented atoms (s = 0, 1).

**Lemma 6.1 (PROVED; N25.5(a)).** For all but countably many s ∈ [0,1], A(ψ^s) ⊆ R(ψ,ψ′) mod null.

*Proof.*
- Suppose uncountably many s have an atom G^s with μ(G^s ∖ R) > 0; replace G^s by G^s ∖ R, still an atom.
- *Finding a triple overlap.* For some N, uncountably many have μ(G^s) > 1/N. Pick M of them with M/N > 2μ(U). Then
  ∫Σ_k 1_{G^{s_k}} > 2μ(U), so some three, s₁ < s₂ < s₃, share a non-null W.
- *On W*, c^{s_k}(g) = λ_k(g)b_k with fixed unit vectors b_k and λ_k > 0. Since s ↦ c^s(g) is affine,
  λ₂b₂ = αλ₁b₁ + βλ₃b₃ with fixed α, β > 0.
  - If b₁, b₃ are independent, the ratios λ₁/λ₂ and λ₃/λ₂ are fixed constants. So c^{s₁}(g) and c^{s₃}(g) are fixed
    vectors times one scalar λ₁(g). Every c^s(g), being an affine combination of them, is a fixed vector times λ₁(g).
  - If b₁ ∥ b₃, then b₁ = b₃ (same strict sign pattern), and every c^s(g) is parallel to b₁.
  - Either way W ⊆ R, a contradiction. ∎

**Theorem 6.2 (PROVED; N25.5(b)).** Let a(ψ) := μ(A(ψ)) and a\* := inf_𝒩 a. There is ψ\* ∈ 𝒩 with a(ψ\*) = a\*.
For every ψ′ ∈ 𝒩, A(ψ\*) ⊆ R(ψ\*,ψ′) ⊆ A(ψ′) mod null.

*Proof.*
- *Setup.* Take ψ_k ∈ 𝒩, normalised (∫|c_k| ≤ 1; scaling changes no direction), with a(ψ_k) → a\*. On
  𝒲 := ∏_k[2^{−k}, 2^{1−k}] with normalised product Lebesgue measure λ^∞, put c^w := Σ w_kc_k, which is jointly
  measurable. Then ψ^w ∈ 𝒩.
- *Bad sets.* B_k := {w : μ(A(ψ^w) ∖ A(ψ_k)) > 0}.
- *B_k is measurable.* μ(A(ψ^w) ∖ A(ψ_k)) > 0 iff the push-forward of μ|_{U∖A(ψ_k)} under γ^w has an atom. That holds iff
  ∬ 1{γ^w(g) = γ^w(g′)} dμ|_{U∖A_k}(g) dμ|_{U∖A_k}(g′) > 0, because that integral equals Σ_x ν({x})². The integrand
  is jointly measurable in (w,g,g′).
- *B_k is null.* Fix the coordinates w_l, l ≠ k, and let w_k = x vary. Then c^w = R + x c_k, whose directions are those
  of (1−s)R + s c_k with s = x/(1+x). Lemma 6.1 applied to the pair (R, ψ_k) shows the x-section of B_k is countable.
  Fubini gives λ^∞(B_k) = 0.
- *Generic w.* For a.e. w, A(ψ^w) ⊆ ⋂_k A(ψ_k). So a(ψ^w) = a\*; put ψ\* := ψ^w.
- *Comparison with any ψ′.* For co-countably many s, A(ψ\*^s) ⊆ R(ψ\*,ψ′) ⊆ A(ψ\*), where ψ\*^s := (1−s)ψ\* + sψ′.
  Since a(ψ\*^s) ≥ a\* = a(ψ\*), R(ψ\*,ψ′) ⊇ A(ψ\*) mod null. ∎

**Corollary 6.3 (PROVED).**
- If a\* = 0, then E(ψ\*) = F(ψ\*) is countable (Theorem 2.1).
- If a\* > 0, then every member of 𝒩 has atom lines. On each rigid piece W ⊆ A(ψ\*), every ψ′ has constant chart
  direction, and its line may depend on ψ′.

**Proposition 6.4 (PROVED; N25.5(c)).**
- (a) For κ ∈ (0,∞)³, κ⊙ψ ∈ 𝒩. Its tie set at q is Z_{φ_κ(q)}(ψ) with φ_κ(q) := (q⊙κ)/(q·κ), a projective
  bijection of Δ fixing the vertices. So E(κ⊙ψ) = φ_κ^{−1}(E(ψ)), and T1 is κ⊙ψ-Bayes at φ_κ^{−1}(p\*).
  Atoms, fans, and the relation "p\* ∈ E" are invariant.
- (b) For fixed x ∈ int Δ, {s : x ∈ E(ψ^s)} is countable, unless μ(Z_x(ψ) ∩ Z_x(ψ′)) > 0, in which case it is all
  of [0,1].
- (c) The set of s for which ψ^s has *some* fan point can be all of [0,1]. Example: ψ′ = κ⊙ψ with ψ having a fan point.

*Proof.*
- (a) (q⊙κ)·c = q·(κ⊙c); endorsement inequalities are world-wise and scale.
- (b) If (x·c(g), x·c′(g)) ≠ (0,0), then g ∈ Z_x(ψ^s) for exactly one s. Disjointness then gives countability.
- (c) follows from (a), since ψ^s = ((1−s)𝟙 + sκ)⊙ψ. ∎

So genericity removes every atom that is not forced on all of 𝒩. It cannot remove fans, and it cannot move p\* out of E
by rescaling. If 𝒩 is just {κ⊙ψ} (one ray per world, i.e. the ranking's adding-up is rigid), E is the same in every
member up to the projective reindexing.

---

## 7. What closed choice forces (N25.6–N25.8)

Throughout this section (H25) and (E_ψ) hold.

### 7.1 Profile closure

**Lemma 7.1 (LSC; PROVED).** If q_m → p̄ and C_{q_m} → C_∞ in measure, then ψ(C_{p̄}) ≤ ψ(C_∞) coordinatewise.

*Proof.*
- *Tail sets.* Pass to a subsequence with Σ_m μ(C_{q_m} △ C_∞) < ∞, and put S_M := ⋃_{m≥M}(C_{q_m} △ C_∞), so
  μ(S_M) → 0. Coherent models agree on unanimous problems (they accept every g ≫ 0, and g ≪ 0 ∉ U), so S_M contains
  none.
- *The worsened model.* Fix i, and let X_M equal C_∞ off S_M and give the world-i-bad advice in the advice range {+,0} on S_M.
  - X_M ∈ M_U, and X_M is regular.
  - For m ≥ M, C_{q_m} gives advice at least as good as X_M at world i a.e. So C_{q_m} ⪯_i X_M by (G).
- *Closed sections.* A_i(X_M) is closed, so C_{p̄} ⪯_i X_M. Since C_{p̄} ∈ C_L, (E_ψ) gives
  ψ_i(C_{p̄}) ≤ ψ_i(X_M) ≤ ψ_i(C_∞) + ∫_{S_M}ρ_i dμ → ψ_i(C_∞). ∎

This is the "upper envelope of the tail" of N22 Remarks 3.3. There it failed because members of M_i could carry pure mass
on S_M. Here ψ is an integral, and completeness is not needed.

**Lemma 7.2 (USC; PROVED).** Let p ∈ Δ and j ∈ Ω. Suppose that for every η > 0 there is a regular Z with Z ≺_i C_p for
all i ≠ j and ψ_j(Z) ≤ ψ_j(C_p) + η. Then limsup_{q→p} ψ_j(C_q) ≤ ψ_j(C_p).

*Proof.*
- For i ≠ j, p ∉ A_i(Z), which is closed. So on a neighbourhood N of p, C_q ⋠_i Z for all i ≠ j.
- Competitiveness on supp q then forces j ∈ supp q and C_q ⪯_j Z.
- (E_ψ) gives ψ_j(C_q) ≤ ψ_j(Z) ≤ ψ_j(C_p) + η. ∎

**Corollary 7.3 (PROVED; N25.6).** Write C_p = D_K.
- (IMP_j) holds if the set (C_p ∩ O_j⁺) ∪ ((U ∖ C_p) ∩ O_j⁻) is non-null, where O_j^± := {±g_j > 0 > ±g_i, i ≠ j}.
  Removing (adding) a small subset of it is strictly better at both i ≠ j and costs ψ_j at most its ρ_j-mass. So
  Lemma 7.2 applies.
- (IMP_j) holds for all j when K ⊆ int Δ (then C_p ∩ O_j⁺ is non-null).
- At every such p, q ↦ ψ(C_q) is continuous: any limit z satisfies ψ(C_p) ≤ z by Lemma 7.1 (with compactness in measure)
  and z ≤ ψ(C_p) by Lemma 7.2.
- If moreover ψ(C_p) has a unique coherent realiser (for example ψ(B_w) with w ∉ E), then q ↦ C_q is continuous in
  measure at p.

### 7.2 Lemma Q (N25.7)

**Lemma 7.4 (PROVED).** Let q_m → p̄, j ∈ Ω and y ∈ ℝ³ with ψ_i(C_{q_m}) > y_i for all i ≠ j and all m. Then no regular
Z ∈ M_U has Z ≺_j C_{p̄} and ψ_i(Z) ≤ y_i for all i ≠ j. If moreover ψ(C_{q_m}) → y and y is strongly Pareto-minimal in
ℛ, then ψ(C_{p̄}) = y.

*Proof.*
- *No such Z.* Z ≺_j C_{p̄} gives p̄ ∉ A_j(Z), which is closed. So C_{q_m} ⋠_j Z for large m.
- Competitiveness of C_{q_m} on supp q_m gives some i ∈ supp q_m, necessarily i ≠ j, with C_{q_m} ⪯_i Z.
- (E_ψ) then gives ψ_i(C_{q_m}) ≤ ψ_i(Z) ≤ y_i, a contradiction.
- *Second statement.* Lemma 7.1 (with a subsequence converging in measure) gives ψ(C_{p̄}) ≤ y ∈ ℛ, and strong
  Pareto-minimality gives equality. ∎

Every face point y ∈ F_t with t ∈ int Δ is strongly Pareto-minimal: y′ ≤ y forces t·y′ ≤ V(t), hence y′ = y.

### 7.3 The (n−1)-dimensional staircase (N25.8)

**Theorem 7.5 (PROVED).** For j ∈ Ω let I_j be the set of p ∈ Δ such that some regular Z has Z ≺_j C_p and
ψ_i(Z) ≤ ψ_i(C_p) for all i ≠ j. Write π_j(y) := (y_i)_{i≠j}. Then π_j(ψ(C_{I_j})) is contained in a countable union of
*strict antichains* of ℝ² (no two points with both coordinates strictly ordered). Each strict antichain is the graph,
over the line 𝟙^⊥ ⊂ ℝ², of a 1-Lipschitz function. In particular π_j(ψ(C_{I_j})) is Lebesgue-null and of σ-finite
length.

*Proof.*
- *A ball for each p.* For p ∈ I_j fix such a Z_p. Since p ∉ A_j(Z_p), which is closed, pick B(p) from a countable base
  with p ∈ B(p) and B(p) ∩ A_j(Z_p) = ∅.
- *What the ball gives.* For q ∈ B(p), as in Lemma 7.4 there is i ∈ supp q, i ≠ j, with
  ψ_i(C_q) ≤ ψ_i(Z_p) ≤ ψ_i(C_p).
- *Same ball, antichain.* If B(p) = B(p′), then p′ ∈ B(p) and p ∈ B(p′). So π_j ψ(C_{p′}) is not strictly above
  π_jψ(C_p), nor vice versa.
- *Antichains are Lipschitz graphs.* For u, v in a strict antichain write v − u = λ𝟙 + w with w ⊥ 𝟙. Excluding
  v − u > 0 and v − u < 0 gives |λ| ≤ max_i|w_i| ≤ |w|. So the antichain is a 1-Lipschitz graph over 𝟙^⊥. ∎

The same proof gives antichains in ℝ^{n−1} for any n. This is the replacement for R2 Theorem 7 (countably many primary
levels), which needed a lexicographic primary to convert ψ-inequalities into L-comparisons. Here competitiveness at the
*other* worlds supplies the conversion, and the price is one dimension.

**Corollary 7.6 (PROVED; consequences listed in N25.8).**
- (a) *Fans.* Let x ∈ F with dim F_x = 2. The plane of F_x, {x·y = V(x)}, projects bijectively under π_j because
  x_j ≠ 0. So for area-a.e. y ∈ F_x and every j, no selected realiser of y is j-improvable. Hence:
  - every undominated realiser of y is j-unimprovable for every j: it is tied with a selected realiser, ties transfer,
    and every realiser has ψ = y;
  - no undominated realiser of y strictly beats another at any world;
  - every incoherent realiser is weakly dominated by an undominated one, strictly at some world (Lemma 1.2).

  This is ideal tie-breaking, the analogue of R7 Lemma SF, at a.e. profile of every 2-dimensional face.
- (b) *Atoms, odd world.* Let G (with G′) be an atom of pattern σ, and j the world with σ_j different from the other two
  signs. On F_t (t ∈ ℓ°) the two coordinates i ≠ j of b have equal sign. So π_j(F_t) is a strictly monotone segment and
  meets each strict antichain at most once. Hence all but countably many points of F_t have no j-improvable selected
  realiser.
- (c) *Ordinary profiles.* For π_j-a.e. frontier profile y = ψ(B_w), w ∉ E: if Z ≺_j B_w, then ψ_i(Z) > ψ_i(B_w) for
  some i ≠ j. A partial converse of endorsement thus holds almost everywhere on the frontier.

### 7.4 What this excludes

There are two different notions of "improvable", and they exclude different things.
- *Lexicographic rankings (R2's notion).* World j ranks by ψ_j and then by a secondary s_j, and an improvement keeps
  ψ_j and lowers s_j. R2 Thm 7 allows only countably many ψ_j-levels of such improvable undominated models. Whenever
  the tie-breaking secondary makes improvable models occur along a continuum of ψ_j-levels, as in R3 §3, (S) fails.
- *Arbitrary preorders (the notion of Theorem 7.5).* An improvement Z ≺_j C keeps every *other* world's ψ no worse.
  Here the ranking need not be lexicographic, complete, or related to ψ beyond (E_ψ). Corollary 7.6 excludes:
  - any such ranking whose undetected strict comparisons let a selected model lose at j, to a model that is ψ-no-worse
    elsewhere, on a set of tied profiles whose projection has positive area;
  - or, for the odd world of an atom, at uncountably many profiles of one atom face.
- Neither notion contains the other. Under either, what survives is tie-breaking in which selected models never lose
  in that sense at a.e. tied profile. In the second case the undominated splits then form an "ideal fibre" at every
  world.

---

## 8. Atoms under the ranking: (IB) transport (N25.9)

Throughout this section (H25) and (E_ψ) hold. Fix an atom line ℓ with Z_t = G ∪ G′ for t ∈ ℓ°. A *split* is a
measurable S ⊆ G ∪ G′, and Bayes models at t are exactly B^s_t ∪ S. Write v(S) := ∫_S c dμ, which lies in ℝb. Then
ψ(B^s_t ∪ S) = ψ(B^s_t) − v(S).

**Lemma 8.1 (PROVED; IB transport).** For splits S, S′, worlds i and t, t′ ∈ ℓ°:
B^s_t ∪ S ⪯_i B^s_t ∪ S′ iff B^s_{t′} ∪ S ⪯_i B^s_{t′} ∪ S′.

*Proof.* Apply (IB) with A := (S △ S′) ∪ −(S △ S′), D = S, E = S′, and contexts F₁ := B^s_t ∪ (S∩S′) and
F₂ := B^s_{t′} ∪ (S∩S′). Both contexts lie in A^c, because B^s_t ∩ (G ∪ G′) = ∅ and −(G ∪ G′) ∩ U = ∅ (U is
pointed). Then (D∩A) ∪ F₁ = B^s_t ∪ S and (E∩A) ∪ F₁ = B^s_t ∪ S′, and likewise with F₂. ∎

So each world induces a t-independent preorder ≤_i^ℓ on splits.

**Theorem 8.2 (PROVED).**
- (a) B^s_t ∪ S is L-undominated iff no split S″ with v(S″) = v(S) dominates S in the orders (≤_i^ℓ)_i. In particular the
  set 𝒰 of undominated splits does not depend on t ∈ ℓ°.
- (b) For every S ∈ 𝒰 and **every** t ∈ ℓ°, B^s_t ∪ S is coherent.
- (c) *Odd world.* Let j be the odd world of σ, with σ_j = −; the case σ_j = + is the mirror image, with θ ∈ [0,1). For
  every t ∈ ℓ° and θ ∈ (0,1] (θ the accepted fraction of ∫_G|c|, taking G′ null for brevity), some selected realiser
  B^s_t ∪ S_θ of the face point y_θ has the following property: no split S′ with ∫_{S′}|c| ≥ ∫_{S_θ}|c| satisfies
  S′ <_j^ℓ S_θ.
  - By Corollary 7.6(b), for all but countably many θ this holds for *every* selected realiser of y_θ.

*Proof.*
- (a) A dominator of a t-Bayes model Y is weakly dominated by a selected C (Fact 0). By transitivity of the preorders, C
  dominates Y, and Lemma 1.2's argument gives ψ(C) = ψ(Y). So C is a realiser of the same face point. Lemma 8.1
  transports domination among realisers between t and t′, and v(·) does not depend on t.
- (b) Every undominated model is tied with a selected one (Fact 0) and is coherent by (C).
- (c) *Approach along the face.* For θ′ < θ, the face points y_{θ′} have y_{θ′,i} > y_{θ,i} for i ≠ j (b_i > 0 there).
  Each is the profile of a selected model (Lemma 1.2). Let θ′ ↑ θ along a sequence, and let p̄ be an accumulation point
  of the indices.
- Lemma 7.4 gives ψ(C_{p̄}) = y_θ, so C_{p̄} = B^s_t ∪ S_θ. It also forbids every regular Z ≺_j C_{p̄} with
  ψ_i(Z) ≤ y_{θ,i} (i ≠ j).
- Take Z = B^s_t ∪ S′ with ∫_{S′}|c| ≥ ∫_{S_θ}|c|, and apply Lemma 8.1. ∎

*Reading.*
- An atom chord carries a whole t-independent family of undominated splits 𝒰 (at least one for each mass level).
- Each split must be a coherent partial shell over D_{K^♭_t} simultaneously for all t on the chord. By Theorem 4.1(e),
  the G-facing support of K^♭_t is frozen, so this is consistent.
- The odd world's restricted order must have, at each mass level, a selected split that no heavier split beats.
- The undetected strict comparisons (Lemma 1.2) are context-free along the chord.

I found no contradiction among these requirements. A lexicographic secondary with Neyman–Pearson level sets satisfies
all of them *on the faces alone*. As a global lexicographic ranking it falls under R2 Thm 7 as soon as it makes
undominated models R2-improvable at a continuum of ψ_j-levels (§7.4). I have not shown that this always happens. Whether
some ranking, lexicographic or not, satisfies these requirements together with the global ones of N25.8 is exactly
residual R-b.

---

## 9. The target, the box, and localisation (N25.10, N25.11)

### 9.1 p\* ∈ E (N25.10)

**Theorem 9.1 (PROVED).** Assume (γ) and (α), and suppose p\* ∈ E. Then there are directions δ and a relatively open set
of boundary gambles h ∈ ∂D_{T1} ∖ 0 with P_{T1}(h) = 0 but lim_{s↓0} P(p\*+sδ, h) = P_{K_δ}(h) ≠ 0, where X_δ = D_{K_δ}.
So q ↦ P(q,h) has no limit at p\*.

*Proof.*
- *Two directional limits differ.* Z_{p\*} is non-null, and X_δ, X_{−δ} differ exactly on Z_{p\*} (Lemma 3.1, with δ
  off the countable set D_{p\*}). So K_δ ≠ K_{−δ}, and one of them, say K_δ, differs from T1.
- *A boundary gamble where it shows.* D_{K_δ} and D_{T1} are open cones that differ on a non-null set, so their symmetric
  difference contains an open set. Pick g₀ there.
  - If P_{K_δ}(g₀) > 0 ≥ P_{T1}(g₀), put h₀ := g₀ − P_{T1}(g₀)𝟙. Then P_{T1}(h₀) = 0 and
    P_{K_δ}(h₀) = P_{K_δ}(g₀) − P_{T1}(g₀) > 0, since P_K(g − s𝟙) = P_K(g) − s.
  - The reverse case gives P_{K_δ}(h₀) < 0 the same way.
  - Either way h₀ ∈ ∂D_{T1} ∖ 0 and P_{K_δ}(h₀) ≠ 0. By continuity in h the same holds on a relative neighbourhood of h₀
    in ∂D_{T1}.
- Lemma 3.1 gives K_{p\*+s_mδ} → K_δ in the Hausdorff metric, hence P(p\*+s_mδ, h) → P_{K_δ}(h). ∎

So N15's first step fails at p\* outright. It needs P(·,h) to be continuous at p\* with value 0 (Lemma `lem:levels` at
level 0 through p\*, and Theorem `thm:pivot` Step 1: p\* ∈ λ⁺_τ). Where the affected h lie:
- Suppose p\* is a generic point of an atom line (p\* ∈ ℓ°), so Z_{p\*} = G ∪ G′. Then W := D_{K_δ} △ D_{T1} ⊆ G ∪ G′
  mod null, since both cones lie between B^s and B^s ∪ Z.
- The h of the proof can be taken in ∂D_{T1} ∩ cl W.
  - If D_{K_δ} ⊄ cl D_{T1}, the open connected cone D_{K_δ} meets ∂D_{T1}, and those points are limits of W.
  - Otherwise K_δ ⊋ T1, some h ∈ ∂D_{T1} has P_{K_δ}(h) < 0, and points just inside D_{T1} near h lie in W.
- So h ∈ cl(G ∪ G′) ⊆ cl(O_σ ∪ O_{−σ}) (Theorem 4.1(a)): the affected h have sign pattern σ or −σ, up to zero
  coordinates.
- By writeup Lemma `lem:signs` (on F_k, h_k < 0, with the other two coordinates in the patterns (−,+), (+,+), (+,−)):
  - a pattern with exactly one negative coordinate k occurs only on the middle arc (τ_i, τ_j) of F_k;
  - a pattern negative at k and i occurs only on the arcs of F_k and F_i adjacent to the corner ray r_{ki}.
- So for σ with single negative k (and −σ negative at the other two worlds i, i′), the affected gambles lie on the
  middle arc of F_k and on the arcs adjacent to r_{ii′}.

By Proposition 6.4(a), "p\* ∈ E" survives every rescaling of ψ. Whether a generic mixture can move p\* off E is open:
p\*(ψ^s) moves with s in a way I could not control.

### 9.2 The box is E-robust (N25.11, first part)

**Proposition 9.2 (PROVED).** Writeup Lemma `lem:edgebox` holds for every integral field on M_U with strict signs whose
Bayes models are coherent at a.e. weighting (no continuity, no condition at E).

*Proof.* Re-reading the proof, it uses only three facts.
- (i) Half-plane charts for a.e. g: {q : P(q,g) > 0} = H(g) up to a null set of q. This is Fubini over U × (Δ ∖ E) and
  needs K_q only for a.e. q.
- (ii) P(q, A+λB) ≥ P(q,A) + λP(q,B) for a.e. q ∈ O. This is concavity of P(q,·), for every q ∉ E.
- (iii) K_q ⊇ K′ for a.e. q.

The conclusion, q₀ ∈ cl H(A+λB) together with c(A+λB) < 0 on the closed edge, involves only the chart of the single
gamble A + λB. ∎

So the edge approaches never need uniqueness, at edge priors or anywhere else. In Prop `prop:boxbridge`(c), what needs
E = ∅ is the identification of the cluster lines at A and B (Thm `thm:pivot`). That is a statement about P near p\* and
along the facets.

### 9.3 Localisation (N25.11, second part; CHECKED, plus CONJECTURE N25.L)

I re-read the writeup's §4 for where Hausdorff continuity of q ↦ K_q is used.
- Lemma `lem:chords`(b) and Lemma `lem:levels`: on all of int Δ. Straight levels are convexity statements along segments
  between arbitrary q₁, q₂.
- Lemma `lem:PL2` and Lemma `lem:nopin`: on co(G ∪ V_j), a set reaching from p\* to a fixed relative neighbourhood V_j
  of a vertex. In Thm `thm:pivot` Step 1 this is used with vertices e_l, for each l with h(σ_i)_l > 0, and over all
  facets.
- Thm `thm:pivot` Steps 0–5 and Thm `thm:nosliding`: zero sets as lines across int Δ, and continuity at p\*.
- Prop `prop:regularity`, Prop `prop:blowup`: local at p\*.
- Lemma `lem:edgebox`: E-robust (Proposition 9.2).

**Proposition 9.3 (CHECKED, by reading).** The open sets on which N15 uses Hausdorff continuity of K cover int Δ.

*Why.*
- In Thm `thm:pivot` Step 1 and Lemma `lem:nopin`, continuity is used on G := int(P_{σ₁} ∩ P_{σ₂}) and on
  co(G ∪ V_l) for each l with h(σ₁)_l, h(σ₂)_l > 0.
- In Lemma `lem:levels` and Steps 0 and 4, continuity is used on the closed half-planes P_σ ∩ int Δ. Their boundary
  lines pass through p\*, and their positive sides contain e_l whenever h(σ)_l > 0.
- As h runs once around ∂D_{T1} ∖ 0, its sign pattern runs through all six mixed patterns. So the positive half-planes
  turn through a full circle about p\*, and their union is int Δ.
- Thus N15 *as written* needs continuity on all of int Δ. An atom chord anywhere, or a fan point anywhere, sits inside
  one of these sets.

The steps that do localise are:
- the box (Proposition 9.2), which needs no continuity;
- Prop `prop:regularity`, Prop `prop:blowup`, Thm `thm:nosliding` and Cor `cor:PCNS`. These are local at p\* *once* the
  global conclusions of Thm `thm:pivot` (exact zero lines through p\*, unique clusters) are available.

So the brief's item (d) has a negative answer for N15 as written. The global input is the pivot theorem. I see no way to
obtain its conclusions from continuity near p\* alone, because Lemma `lem:nopin` transports information from the vertex
neighbourhoods to p\* across the whole wedge. This is a statement about the proof, not a proof that no localised
argument exists. Under N25.5(b) with a\* = 0, the exceptional set that would have to be tolerated is a countable set F
of fan points.

**CONJECTURE N25.L.** If E is countable and closed (hence discrete in int Δ, for example finite) and p\* ∉ E, the chain
of writeup §4 goes through.
- Evidence: int Δ ∖ E is then open and connected, and every argument above uses either convexity of a set (true mod a
  countable set) or connectedness of an open set.
- What must be re-checked: Lemma `lem:levels` with segments through points of E, which needs the a.e. version plus
  continuity in q off E; and PL2's clopen argument on G ∖ E.
- A countable dense F is not covered.

---

## 10. What remains possible: exact list

Under (H25), (M0) and (E_ψ), with ψ = ψ\* chosen as in Theorem 6.2, a cover of T1 requires E(ψ\*) ≠ ∅ (N22 Cor 2.3 /
writeup Cor `cor:residual`, in M0 form) and one of the following.

**R-a (p\* ∈ E).**
- *Configuration.* T1 is a coherent realiser of a point of F_{p\*}, through an atom line ℓ ∋ p\* or a fan point at p\*.
- *Forced:*
  - by Thm 9.1, P(·,h) jumps at p\* for an open set of boundary gambles of T1. When p\* is a generic point of an atom
    line, this happens on the arcs of ∂D_{T1} with the patterns ±σ;
  - the face F_{p\*} is a segment or a 2-dimensional convex set. Its extreme points have coherent realisers (Thm 3.3);
  - tie-breaking at F_{p\*} is ideal at a.e. point (fan, Cor 7.6(a)) or at all but countably many points for the odd
    world (atom, Cor 7.6(b));
  - for an atom, the splits are coherent all along ℓ° (Thm 8.2).
- *Not available:* N15, at any step that involves p\*.

**R-b (p\* ∉ E, persistent atoms: a\* > 0).**
- *Configuration.* Every supporting assessment has atom lines. On the rigid pieces, every member's chart direction is
  locally constant.
- *Forced:* Theorems 4.1 and 8.2 for each atom; Corollary 7.6(b), (c).
- *Not available:* N15 as written. It uses continuity on all of int Δ (Proposition 9.3), and an atom chord passes
  through that region.

**R-c (p\* ∉ E, a\* = 0).**
- *Configuration.* E(ψ\*) = F, a countable non-empty set of fan points. Either F is not closed, or F is closed and
  N25.L fails.
- *Forced:* Theorem 5.1 (arc-shells), and Corollary 7.6(a) at every 2-dimensional fan face.

**Not decided here.**
- Whether ideal tie-breaking at a.e. tied profile can coexist with (S) globally for a non-lexicographic incomplete
  ranking.
- Whether a fan at p\* can carry T1 with half-plane charts. This is additive geometry and could be tested by
  construction (Remark 5.2).
- Whether (E_ψ) can be dropped (N25.12).

**Suggested next steps, in decreasing order of expected yield.**
1. *Additive test of R-a.* Try to build an integral field on M_U with half-plane charts and coherent Bayes models off a
   fan point x = p\* (or an atom chord through p\*), with T1 an intermediate coherent minimiser at p\*. Use the
   degree-0 structure of Remark 5.2 and the arc-shell constraint of Theorem 5.1.
   - If this is impossible, a short additive lemma excludes R-a.
   - If it is possible, the M0 question becomes purely ordinal: ideal tie-breaking at one face, which N25.8 permits.
2. *CONJECTURE N25.L*, by re-running writeup §4 with int Δ replaced by int Δ ∖ F.
3. *Persistent atoms.* Use Theorem 4.1(e)–(g) (frozen G-facing support, no switching of G-directional gambles along ℓ)
   together with writeup Lemma `lem:UVN` at the two ends of the chord. The cliff must be compatible with the vertex
   limits K_q → co(K′ ∪ {e_i}).

---

## 11. Status table

| Claim | Status | Hypotheses beyond (H25) + (M0) |
|---|---|---|
| Thm 2.1 / Cor 2.2: E = countably many atom chords ∪ countable fan set; V differentiable exactly off E | PROVED | (γ) only |
| Lemma 3.1, Thm 3.3: B^s_q coherent ∀q; directional limits coherent; extreme points coherent; K^♭ usc, continuous exactly off E | PROVED | (γ) |
| Thm 4.1: atom anatomy (orthant, global chart, shell, frozen support, cliff, no switching) | PROVED | (γ) |
| Thm 5.1: fan anatomy (arc-shells, face dim ≤ 2) | PROVED | (γ) |
| Lemma 6.1: pairwise genericity (atoms ⊆ rigid set for co-countable s) | PROVED | — |
| Thm 6.2 / Cor 6.3: generic member with least, universal atom set; a\* = 0 ⇒ E countable | PROVED | 𝒩 closed under countable sums |
| Prop 6.4: rescaling invariance; fixed-point countability; fans not removable | PROVED | — |
| Lemma 1.1, Lemma 1.2 (selected ψ-supported; face points selected; brief's premise) | PROVED | (E_ψ) |
| Brief's premise without (E_ψ) | not established (N25.12) | — |
| Lemma 7.1 (LSC), Lemma 7.2 (USC), Cor 7.3 (profile continuity) | PROVED | (E_ψ) |
| Lemma 7.4 (Lemma Q) | PROVED | (E_ψ) |
| Thm 7.5: (n−1)-dim staircase (antichains, Lipschitz graphs, null) | PROVED | (E_ψ) |
| Cor 7.6: ideal tie-breaking a.e. on 2-dim faces; odd-world countability on atom faces; a.e. partial converse | PROVED | (E_ψ) |
| Lemma 8.1, Thm 8.2: IB transport, uniformly coherent splits, odd-world minimal split at every level | PROVED | (E_ψ) |
| Thm 9.1: p\* ∈ E ⇒ P(·,h) discontinuous at p\* on an open set of ∂D_{T1} | PROVED | (α), (γ) |
| Prop 9.2: Lemma edgebox is E-robust | PROVED | (γ) |
| Prop 9.3: N15's continuity is used on sets covering int Δ (no localisation as written) | CHECKED (reading) | — |
| CONJ N25.L: N15 with countable closed E, p\* ∉ E | CONJECTURE | — |
| A contradiction in R-a, R-b or R-c | open | — |
