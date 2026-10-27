# L3 — Ordinal limits and two-grade worlds: the limit exists, and a veto kills it (round 20)

Scripts: `l3py/` (`gauge_fixed_U.py`, `vb_system.py`, `two_sided_boxes.py`, the exploratory
`fixed_domain_gauges*.py`, `fastgeo.py`, with `.out` files).
Labels: PROVED (in this note, not refereed) / CHECKED / CONJECTURE / NUMERICS. Notation as in the write-up
§§2–6, R10a (Thm V, Cor V2, Thm M, Thm R) and P3 (exact consistency test, Thm 4.1). No assumption is added:
every hypothesis below is a hypothesis of a stated theorem, and it is verified where the theorem is applied.

---

## 0. Outcome

**No cover of T1. Strategy (I) was carried to the end. Its limit object exists and is explicit. It satisfies
every requirement except closed sections, and its failure there is a theorem.** Strategy (II) leads to the same
theorem or to the known (M0) residual. The only exception is a narrow precise-edge escape for full vetoes, stated in
L3.6(b).

The single obstruction is the following theorem (§4).

> **Theorem L3.4 (vetoes cannot be paid; PROVED).** Take any ranking on any decomposable domain with strict (G).
> Suppose world i *refines a veto* Φ: an additive charge on i-wrong advice, with Φ(X) < Φ(Y) ⇒ X ≺_i Y.
> Suppose the world-j-best model pays it, Φ(B^j) > 0.
> Suppose every selected model on the edge [e_i,e_j] that pays it has a Φ-neutral strict world-i improvement.
> Then no selection is competitive on supp p along [e_i,e_j] with closed sections at worlds i and j.
> This holds for every target. It needs no (IB), no (C), no totality and no third world.

Each step of the attempt is proved, and §§1–5 give them in this order.

1. **Two-sided domains have no gauge sequence (Prop L3.1).**
   - On a decomposable domain that is two-sided near ∂D_{T1} with (LF), every ranking with strict (G), (S), (LA) and
     T1 ∈ C_L has *precise* vertex models C_{e_i} = {g : g_i > 0}.
   - So every gauge mixture there is a normalised-box system. Its targets stay at Hausdorff distance ≥ c(ε) > 0
     from T1 (c(0.3) ≈ 0.037, NUMERICS).
   - The brief's premise, gauge covers converging to T1 on two-sided domains, is therefore **false**. The polygons of
     R10a Prop M′ live on one-sided (U-)domains.
2. **On a fixed one-sided domain the sequence exists (Prop L3.2).**
   - Take M_U with U = D_{K'} and u ∈ K' ⊆ relint T1 (so (LF) at T1 holds with a fixed margin).
   - The gauges M_i = conv{a e_i, b K', b v_i} cover polygons K_u with d_H(K_u, T1) ≤ C(ε)·a/b.
   - So the degeneration of the limit is *not* a loss of (LF) margin, contrary to the brief's diagnosis. It is a
     separation of scales inside the gauges.
3. **The ordinal limit is the veto–Brier ranking VB (Thm L3.3).** The limit is taken lexicographically as a/b → 0, or
   along any ultrafilter.
   - World i ranks first by the veto Φ_i, the |v_i·h|-weighted mass of accepted gambles beyond the plane of the
     facet F_i. It then ranks by Brier error.
   - The limit selection is C_p = D_{conv(K' ∪ {p} ∪ {v_m : m ∈ supp p})}. It equals T1 on the whole plateau p ∈ T1.
   - VB satisfies strict (G), (IB), (LA), (C) and (LF) at T1, with T1 ∈ C_L. Every C_p is coherent, competitive on
     supp p and undominated, at every p ∈ Δ, boundary priors included.
   - Its sections are closed relative to int Δ. They fail to be closed exactly at boundary priors.
   - This answers positively the question P3 §4 left open ("whether T1 on M_U admits a system with everything except
     (Cl)"; the boundary members are checked here).
   - VB's worlds do not add up.
4. **Theorem L3.4** applies to VB, and (Thm L3.5) to every renormalisation-free ordinal limit of gauge covers
   converging to T1 on a common domain whose leading level is visible on the domain (hypothesis (N)).
   - The reason is "Thm R survives the limit as a veto". The leading level of such a limit is always a pure veto: it
     is ≤ 0, it vanishes on cl D_{T1}, and it is paid by a vertex model.
   - So the limit preorders admit **no selection at all** with closed sections.
   - A repair, including any repair through the exact consistency test, must give up refining the limit's leading
     level at the vetoing world, that is, give up the ordinal limit.
5. **Strategy (II) (Prop L3.6).** Two-grade worlds compatible with (IB) fall into three kinds.
   - **Silence before wrong** violates (G).
   - **Wrong before silence** is a full veto.
     - T1 is not certified against the vacuous model at such a world, so a cover has at most two of them.
     - Thm L3.4 forbids closed choice for them, except through edge selections that are precise on an uncountable set
       of edge priors (a narrow residual, CONJECTURE: empty).
   - **Strictly positive leading combinations, or unanimities of them**, add up. They land in the one open (M0) branch
     on two-sided domains, D1's E(ψ) ≠ ∅ with p\* ∉ E.
     - In that branch, routes I1, I2, C2 and the short route break at exactly one input: (BU) at every interior prior,
       on the atom chords.

**Nearby result (per the project preferences).**
- T1 is covered on M_U by a lexicographic ranking under every requirement, with sections closed in the open simplex
  (VB).
- Closed choice fails only at boundary priors, where the veto must be paid (Thm L3.4).
- Dropping boundary priors from (S) is *not* a good repair: it trivialises coverage. The full-veto ranking then covers
  the vacuous model with a constant selection.
- So the boundary of Δ is exactly where closed choice carries content against lexicographic structure.

---

## 1. Two-sided domains: precise vertex models; gauges are boxes (Prop L3.1)

Two-sided means, as in write-up §5: for some open N′ ⊇ ∂D_{T1}∖0, a.e. pair with an orientation in N′ has an advice
range containing {+,0,−}.

**Proposition L3.1 (PROVED).**
- (a) Let a ranking on a decomposable domain that is two-sided near ∂D_{T1} satisfy strict (G), (S) and (LA), with
  (LF) at T1 and T1 ∈ C_L. Then C_{e_i} = {g : g_i > 0} a.e. for every i. In particular, acceptance is in the advice
  range for a.e. g that is not ≤ 0.
- (b) Every R10a gauge mixture on such a domain has M_i ⊆ ℝ₊e_i, i.e. M_i = [α_i, β_i]e_i. Its covered targets are
  the normalised boxes ν(p\*⊙∏[α_i,β_i]).
- (c) inf over all boxes of d_H(ν(box), T1) =: c(ε) > 0.

*Proof.*
- **(a), first two inputs.**
  - R10a Thm V (any ranking with these hypotheses) gives C_{e_i} = D_{V_i} with e_i ∈ V_i.
  - R10a Cor V2(a),(b) give Av ∩ D_i ≈ D_{V_i} and compatibility V_i ⊆ conv(V_j ∪ e_i), where Av is the set of
    orientations whose acceptance is available. Both proofs use only competitiveness at vertices and strict (G).
- **(a), the wedge W_k.**
  - Let g ∈ relint F_k lie on the middle arc, so g_k < 0 < g_i, g_j.
  - Two-sidedness puts −g′ ∈ Av for a.e. g′ near g. Also −g′ ∈ D_k. So −g′ ∈ D_{V_k}, i.e. V_k ⊆ {m : m·g′ < 0}.
  - By continuity, V_k ⊆ W_k := {m ∈ Δ : m·g ≤ 0 for all g on the middle arc of F_k}.
  - The zero lines of these g rotate about v_k, from lin(v_k,e_i) to lin(v_k,e_j). So W_k is the closed wedge beyond
    v_k between the two crossing lines. It lies on the closed e_k-side of lin(e_i,v_k).
- **(a), the half-planes.** Let L_j := lin(e_i, v_j) and let H_j be its closed side containing e_j. Then W_j ⊆ H_j
  and e_i ∈ L_j, so conv(W_j ∪ e_i) ⊆ H_j. Likewise conv(W_k ∪ e_i) ⊆ H_k.
- **(a), conclusion.**
  - L_j and L_k meet [e_j,e_k] at x_j = (e_j-parameter c₀/(2c₀+ε)) and x_k = (parameter (c₀+ε)/(2c₀+ε)), and
    x_j strictly precedes x_k.
  - Write m ∈ Δ as m = e_i + λ(y − e_i) with y ∈ [e_j,e_k]. Then m ∈ H_j ∩ H_k forces y ∈ [e_j,x_j] ∩ [x_k,e_k] = ∅,
    or λ = 0.
  - So V_i ⊆ H_j ∩ H_k ∩ Δ = {e_i}.
- **(b)** For gauges, e_i ∈ V_i is (M1), and Cor V2 holds by construction from (M2). So ν(M_i) = {e_i}.
- **(c), no box image equals T1.**
  - On ν(∏[α,β]) the maximum of x_i is attained at ν(β_i,α_j,α_k). The minimum of x_k is
    α_k/(α_k+β_i+β_j).
  - On T1 the maximum of x_i is attained only at v_i, and v_i attains the minimum c₀ of x_k.
  - So ν(box) = T1 would force ν(β_i,α_j,α_k) = v_i and α_k/(α_k+β_i+α_j) = α_k/(α_k+β_i+β_j), i.e. α_j = β_j.
  - By symmetry the box is then a point, which is not T1.
- **(c), compactness.**
  - Boxes whose images converge to T1 have bounded ratios. Otherwise some image reaches within o(1) of a vertex of
    Δ, or of a face of Δ.
  - So a limit box would have image T1, which was just excluded. ∎

NUMERICS (`two_sided_boxes.out`).
- 2·10⁵ sampled points of Δ lie in both H_j and H_k only at e_i, for ε ∈ {.05,.3,.6,.9} and each i.
- min d_H(ν(box),T1) = 0.0080, 0.0375, 0.0314, 0.0168 at ε = .05, .3, .6, .9.

*Consequence for (I).* On two-sided domains there is no sequence of gauge covers converging to T1, so (I) has no input
there. (a) is the ranking-level form of write-up Cor. availability, which was proved for additive covers.

---

## 2. Fixed one-sided domain: gauge covers converging to T1 (Prop L3.2)

Fix K′ with u ∈ K′ ⊆ relint T1. The standard choice K′ = u + s(T1−u) is allowed, and so is s = 0. Put U = D_{K'};
M_U then has (LF) at T1 with N = U.

**Proposition L3.2 (PROVED).** Let 0 < a < b and M_i := conv{a e_i, b K′, b v_i}.
- (R10a Thm M) This is a compatible gauge tuple, V_i = conv(e_i ∪ K′), with domain Av = U. So it is a full additive
  system on M_U, and for every interior p its target is D_{K_p}, K_p = ν(Σp_iM_i), with (LF).
- d_H(K_u, T1) ≤ C(ε, K′)·a/b.

*Proof.*
- **Thm M hypotheses.** v_i ∈ [u, e_i] ⊆ conv(K′ ∪ e_i). So V_i = conv(e_i ∪ K′), and
  V_i ⊆ conv(V_j ∪ e_i) because K′ ⊆ V_j. Then Av = ∪D_{V_i} = D_{K'} = U.
- **Points of K_u near T1.** For y = Σλ_iv_i ∈ T1, the point Σ_i[λ_i b v_i + (1−λ_i) a e_i]/3 has ν-image within
  O(a/b) of y.
- **A general point.** Take x_i = α_i a e_i + γ_i b k_i + β_i b v_i (k_i ∈ K′, α+β+γ = 1). Its image is
  λz + (1−λ)y with:
  - y ∈ conv(K′ ∪ T1) = T1;
  - z = ν(α);
  - λ = aΣα/(aΣα + bσ), where σ = Σ(β_i+γ_i).
- **Case σ ≥ 1.** Then λ ≤ 3a/b.
- **Case σ < 1.** Then every α_i ≥ 1−σ, so |z − u| ≤ C₁σ.
  - If C₁σ is at most the inradius of T1 about u, then z ∈ T1 and the point lies in T1.
  - Otherwise λ ≤ 3aC₁/(b·inradius). ∎

NUMERICS (`gauge_fixed_U.out`, K′ = {u}).
- d_H(K_u,T1)/(a/b) → 0.63, 0.92, 1.27 at ε = .05, .3, .6, for a/b down to 10⁻³.
- (G)-sign violations: 0 of about 10⁵ sampled h.
- Bayes act vs D_{K_p}: 0 mismatches at 12 priors.

*Scales.* f_i(h) = min(a h_i, b·min_{K'} k·h, b v_i·h).
- On U the leading scale b gives min(0, v_i·h): a **veto** of acceptances beyond the plane of F_i.
- Off the veto, f_i/a → h_i: Brier. NUMERICS: errors 4.5·10⁻⁶ and 4·10⁻¹⁶ at a/b = 10⁻⁶.

(The exploratory scripts `fixed_domain_gauges*.py` first found, by blind optimisation over gauges, ratios
d_H/margin ≈ 0.05 on a fixed U-domain. That is what suggested L3.2.)

---

## 3. The ordinal limit: the veto–Brier ranking VB (Thm L3.3)

Work on M_U as in §2. For h ∈ U, v_i·h = (1−ε)u·h + εh_i (u ∈ K′), so v_i·h < 0 ⇒ h_i < 0.

**Levels.**
- Φ_i(X) := ∫_{X ∩ {v_i·h<0}} |v_i·h| dμ. This counts only i-wrong acceptances, so it is weakly guiding.
- Ψ_i(X) := ∫_{E_i(X)} |h_i| dμ. This is the Brier/identity loss, strictly guiding.

**Orders.** X ⪯_i Y iff (Φ_i(X),Ψ_i(X)) ≤_lex (Φ_i(Y),Ψ_i(Y)).

**Selection.**
- C_p := U ∩ {p·h > 0} ∩ ⋂_{m∈supp p}{v_m·h ≥ 0} = D_{K_p}, with K_p = conv(K′ ∪ {p} ∪ {v_m : m ∈ supp p}).
- Interior p: K_p = conv(T1 ∪ {p}).
- Vertex e_j: C_{e_j} = U ∩ {h_j > 0}, because h_j > 0 and u·h > 0 imply v_j·h > 0.

**Theorem L3.3 (PROVED).**
- (a) VB is the ordinal limit of the systems of L3.2:
  - lexicographically as a/b → 0, its orders are exactly (Φ,Ψ)-lex;
  - along any non-principal ultrafilter, the orders refine (Φ,Ψ)-lex, breaking only exact two-level ties by o(a)
    terms;
  - its selection is the Hausdorff limit of the stage Bayes families at every p ∈ Δ.
- (b) VB satisfies strict (G), (IB), (LA), (LF) at T1 and (C). Every C_p is coherent, competitive on supp p and
  undominated, for every p ∈ Δ. T1 = C_p for every p ∈ T1. So T1 ∈ C_L, and there is a plateau.
- (c) Every section {p : C_p ⪯_m X} is closed relative to int Δ, and relative to each open edge. For
  X := C_{e_j} ∖ A, with A a non-null proper part of C_{e_j} ∩ {v_i·h<0}, the world-i section contains int Δ but not
  e_j.
- (d) No world of VB adds up.

*Proof.*
- **(a), the stage losses.** At stage (a,b), L_i = bΦ_i + aΨ_i + R. Here |R| ≤ a∫_{layer}|h_i|, and the layer is
  {0 > v_i·h > (a/b)h_i}, whose measure → 0. So the lexicographic limit is (Φ,Ψ)-lex. An ultrafilter limit agrees
  whenever one of the two levels differs.
- **(a), the selection.** K_p = ν(Σp_iM_i). Its b-parts give conv(K′ ∪ {v_m : p_m > 0}), its a-parts give p, and
  their mixtures give the hull, up to O(a/b) as in L3.2.
- **(b), strict (G) and (IB).** A pointwise world-i improvement weakly shrinks the set of vetoed i-wrong acceptances
  and strictly lowers Ψ_i. (IB) holds because both levels are integrals.
- **(b), lex-Bayes.** Pointwise, with weight p on both levels, accepting h has level-0 cost Σ_{m∈supp p} p_m|v_m·h|
  1[v_m·h<0], against 0 for silence. On the level-0 ties, level 1 accepts iff p·h > 0. The resulting model is C_p,
  unique a.e.
- **(b), competitiveness.**
  - If Σ_S p_mΦ_m(X) > 0 = Σ_S p_mΦ_m(C_p), some m ∈ S has C_p ≺_m X.
  - Otherwise Φ_m(X) = 0 = Φ_m(C_p) on S. Level-1 optimality then gives some m ∈ S with Ψ_m(C_p) ≤ Ψ_m(X).
- **(b), undominatedness.**
  - X ⪯_m C_p at every m forces Φ_m(X) = 0 and Ψ_m(X) ≤ Ψ_m(C_p) for m ∈ S.
  - So X is p-optimal at level 1 inside {Φ_m = 0, m ∈ S}, and hence X = C_p a.e.
- **(b), (C): vector uniqueness.** We show that if B is undominated and X has the same six numbers, then X = B a.e.
  - Suppose D := XΔB is non-null.
  - On the activity region R_A := {h ∈ U : v_m·h < 0 iff m ∈ A}, the exchange density is ±M_Ah, with
    M_Ah := ((−v_m·h)1[m∈A], −h) ∈ ℝ⁶. This is linear in h.
  - The exchange σ(S) := vec((X∩S)∪(B∖S)) − vec(B) is a non-atomic vector measure with σ(U) = 0. So its range is a
    symmetric convex set. It contains a ball about 0 in L := span{±M_Ah : h ∈ D}.
  - L ⊇ M_A(ℝ³) for any A with D ∩ R_A non-null. In particular L ∋ M_A𝟙 = (−1[m∈A], −𝟙), which is lex-negative at
    every world.
  - So some splice equals vec(B) + tM_A𝟙 and dominates B, a contradiction.
  - Lex ties at every world are equalities of the six numbers. So a model tied with a member of C_L is that member,
    which gives (C).
- **(b), the plateau.** For p ∈ T1, conv(T1 ∪ {p}) = T1.
- **(c), closed in the open simplex.** For interior p, Φ_m(C_p) = 0 and p ↦ Ψ_m(C_p) is continuous, since C_p is
  continuous in measure. So the section is either all of int Δ or a closed sublevel set. The same holds on open edges.
- **(c), not closed at e_j.** Φ_i(C_q) = 0 < Φ_i(X) for interior q, while X ≺_i C_{e_j} by strict (G).
- **(d)** Let ν_i be a bounded weight, positive on non-null sets, that endorses the relevant comparisons.
  - B = C_u ⪯_i X holds whenever X improves B at world i on any non-vetoed set A and adds an arbitrarily small vetoed
    set P.
  - So ν_i(P) ≥ ν_i(A) for arbitrarily small non-null P, which is impossible for a bounded positive weight. ∎

NUMERICS (`vb_system.out`; empirical measure, 6·10⁴ gambles, ε = .3, s = .5). The empirical system is atomic, so
this checks the pointwise and lexicographic algebra only.
- Competitiveness violations: 0 of 4480 tests (20 priors including vertices and edges; competitors are other C_q,
  random coherent models, random additive Bayes models, and random flips near ∂D_{T1}).
- Dominations: 0.
- Plateau |C_p Δ T1| = 0 at three p ∈ T1.
- The section of X = C_{e2} minus half of its world-1 veto set contains q = (1−t)u + te₂ for t up to 0.9999, but not
  e₂.

*Comparison with N9.7 Design A.*
- Design A's T-protective primary also rewards truth inside T, so its lex-Bayes map is constant on int Δ, and FC
  (N9.6) kills it.
- VB's primary only vetoes outside T. Its selection moves (conv(T1∪p)), and T1 is a plateau only on T1.
- P3 §4 left the boundary members unchecked. Here they are checked.

---

## 4. The single obstruction: vetoes cannot be paid (Thm L3.4)

**Setting.**
- A decomposable domain M (any; two-sided included). A ranking with strict (G), and a selection p ↦ C_p.
- B^m is the world-m-best model. Competitiveness at e_m and strict (G) give C_{e_m} = B^m.
- A **veto at world i** is Φ(X) = ∫ω(g, a_X(g)) dμ with ω ≥ 0, ω(g,a) = 0 unless a is i-wrong at g, and Φ(B^i) = 0.
- World i **refines** Φ if Φ(X) < Φ(Y) ⇒ X ≺_i Y.

**Theorem L3.4 (PROVED).** Let world i refine a veto Φ, and let j ≠ i. Assume:
- (V) Φ(B^j) > 0;
- (Imp) every selected C_q, q ∈ [e_i,e_j], with Φ(C_q) > 0 has a model Z with Φ(Z) = Φ(C_q) and Z ≺_i C_q.

Then no selection has both of the following:
- competitiveness on supp q for q ∈ [e_i,e_j];
- closed sections at worlds i and j.

*Proof.* Put f(t) := Φ(C_{q_t}), q_t = (1−t)e_i + te_j, and let G_j := {g : ω(g, b^j(g)) > 0}, so that
Λ := Φ(B^j) = ∫_{G_j}ω(g,b^j).

1. **lsc.** For c < Λ, the set {t : f(t) ≤ c} is closed.
   - Splices of B^i and B^j along increasing sets give models Z with every value Φ(Z) ∈ [0,Λ] (non-atomicity).
   - If f(t_k) ≤ c < Φ(Z), refinement gives C_{q_{t_k}} ⪯_i Z. Closedness at i then gives C_{q_t} ⪯_i Z.
   - So refinement forbids Φ(Z) < f(t). Letting Φ(Z) ↓ c gives f(t) ≤ c.
2. **usc off T** (the E2 step of B3.3). Let T := {t : a_{C_{q_t}} = b^j a.e. on G_j}.
   - For t ∉ T, take a small non-null P ⊆ G_j on which C_{q_t} differs from b^j, with ∫_Pω(g,b^j) < δ. Let Y be
     C_{q_t} with b^j's advice on P.
   - Then Y ≺_j C_{q_t} by strict (G), and Φ(Y) ≤ f(t) + δ.
   - Closedness of S_j(Y) gives a neighbourhood on which C_{q_{t'}} ⋠_j Y.
   - Competitiveness on {i,j} then gives C_{q_{t'}} ⪯_i Y, and refinement gives f(t′) ≤ f(t) + δ. (At t′ = 0 this is
     trivial; t′ = 1 is excluded, since B^j ⪯_j Y.)
3. **The open set Q.** On T, f ≥ Λ. Let Q := {t ∉ T : f(t) < Λ}.
   - Q is relatively open: steps 1–2 give f < Λ near any t ∈ Q, which excludes T there.
   - 0 ∈ Q, since b^i ≠ b^j on G_j.
   - 1 ∉ Q, since 1 ∈ T.
   - Let t\* := sup{t : [0,t] ⊆ Q}. Then t\* ∉ Q, so f(t\*) ≥ Λ, and by lsc liminf_{t↑t\*} f ≥ Λ. Also f is continuous
     on [0,t\*).
4. **Gap.** Fix c := Λ/2.
   - Let t_c be the first t with f(t) = c. So f < c on [0,t_c).
   - Take Z from (Imp) at t_c.
   - For t ↑ t_c, f(t) < c = Φ(Z) gives C_{q_t} ⪯_i Z. Closedness at i gives C_{q_{t_c}} ⪯_i Z, which contradicts
     Z ≺_i C_{q_{t_c}}. ∎

*Remarks.*
- Step 4 is the mechanism of R2 Thm 7 / FC (N9.6): improvable undominated models carry only countably many values.
  The new input is steps 2–3. Closed choice and edge competitiveness *produce* the continuum of values that FC had to
  assume (FC2), as soon as a vertex model pays a veto.
- In the abstract statement the target plays no role. In covers of T1 it enters only through (Imp): there (Imp) comes
  from the veto vanishing on cl D_{T1} (see L3.5 and §3).

**Application to VB (PROVED).**
- (V): B^j = U ∩ {h_j>0} contains the non-null set of gambles just beyond the middle arc of F_i.
- (Imp): let C = D_K be coherent with Φ_i(C) > 0. Then C accepts an i-negative gamble, so e_i ∉ K.
  - Hence e_i ∉ conv(K ∪ T1), and some open set of h with h_i < 0 is positive on K ∪ T1.
  - Those h are accepted by C, i-wrong, and not vetoed, since the veto vanishes on cl D_{T1}.
  - Removing a piece of them gives Z with the same Φ_i and Z ≺_i C.
- So VB's preorders admit no selection whatever with closed sections. In particular, (c) of L3.3 cannot be repaired by
  changing the selection.

---

## 5. Every ordinal limit of gauge covers ends in a veto (Thm L3.5); strategy (II) (Prop L3.6)

**Setting for L3.5.**
- Gauge systems (M_{i,n}) on a common domain with (LF) at T1, with K_{u,n} → T1.
- Normalise by s_n := max_i max_{M_{i,n}}|m|, so that f_{i,n}/s_n → f^∞_i = min_{M^∞_i} m·h uniformly on S².
- (N): f^∞ ≢ 0 on Av. This holds for L3.2, where f^∞_i = min(0, v_i·h).
- An *ordinal limit* is any order that refines the leading scale: the ultrafilter limit, or the lexicographic limit
  along the degenerating scale.

**Theorem L3.5 (PROVED, under (N)).** f^∞_i ≤ 0 everywhere, f^∞_i = 0 on cl D_{T1} ∪ (Av ∩ {h_i ≥ 0}), and 0 ∈ M^∞_i.
Consequently:
- the leading level of the ordinal limit is a pure veto Φ_i (ω = −f^∞_i on i-wrong acceptances);
- some vertex model pays it;
- (Imp) holds;
- so by Thm L3.4 the limit preorders admit no selection with closed sections.

*Proof (Thm R in the limit).*
- **Signs.** Stage signs give f^∞_i ≥ 0 on Av ∩ {h_i>0} and ≤ 0 on {h_i<0}. K_{u,n} → T1 gives Σu_if^∞_i = 0 on
  ∂D_{T1}.
- **The R10a Thm R argument with weak signs.**
  - Each f^∞_i is linear on each facet.
  - On a crossing facet of i, f^∞_i = α_ih_i with α_i ≥ 0, and α_i is the same on both crossing facets.
  - At the three corner rays, Σu_iα_ir_i = 0. So α = 0, and f^∞ ≡ 0 on ∂D_{T1}.
- **Concavity.**
  - Concavity gives f^∞_i ≥ 0 on cl D_{T1}.
  - h_i < 0 near F_i inside D_{T1} gives f^∞_i = 0 on an open set.
  - Concavity on ℝ³ then gives f^∞_i ≤ 0 everywhere. Evaluating at 𝟙 gives 0 ∈ M^∞_i.
- **The leading penalties are a pure veto.** Dominated convergence (|f_{i,n}| ≤ s_n|h|) gives L_{i,n} = s_n(Φ_i + o(1))
  on every pair of models. The R1 penalties give leading-scale cost −f^∞_i(±h) exactly on i-wrong advice.
- **(V).** Under (N) the veto set {h ∈ Av : f^∞_i(h) < 0} ⊆ {h_i<0} is non-null for some i. Each of its points lies in
  some D_{V_j} with j ≠ i, and B^j accepts it.
- **(Imp)** is proved as for VB in §4, using that the veto vanishes on cl D_{T1} ⊆ Av. ∎

*What a repair must do.* Let a successful system for T1 be built from the limit, by changing the selection, or by
sub-relations through the exact consistency test with R5.
- By L3.5 its vetoing world cannot refine the limit's leading level. So it must delete leading-scale strict
  comparisons of the limit near the boundary of Δ.
- An ordinal limit therefore cannot keep all its scales, which was the point of (I).
- With the natural limit selection this is concrete. When the veto meets a one-positive cone {h_j > 0 > h_i, h_k}
  (it does for VB), every choice κ drawn from the limit order at interior priors q_k → e_j forces R5 to install
  C_{e_j} ⪯_i X or C_{e_j} ⪯_k X, where X = C_{e_j} minus a small vetoed one-positive piece. Both are outcome (a). The
  remaining world j is excluded because L_{j,n}(C_{q_k}) > L_{j,n}(X) at every stage. CHECKED.

**Proposition L3.6 (two-grade worlds).** Work on a two-sided domain. By L3.1(a), every mixed pair there has all three
advices available. Let world i depend, compatibly with (IB), only on a wrong-advice charge W_i and a silence charge
S_i, both positive on non-null sets. Let R be the regular vacuous model, which is silent on every mixed pair.

- **(a) Total worlds (PROVED).** Translation invariance (IB) and totality make world i's order on value differences
  (ΔW,ΔS) a half-plane with inner normal a ≥ 0, a ≠ 0, which may contain part of its boundary line. There are three
  cases.
  - a ∝ (0,1), silence first, violates (G): changing wrong advice to silence would be level-0-worse.
  - a ∝ (1,0) is the *wrong-first lexicographic* world. It refines the full veto W_i (ω > 0 on all wrong advice).
  - a > 0 gives a strictly guiding additive leading level, with a lexicographic tie-break at most. This world adds up,
    with a·(w,σ) as endorser, and so belongs to (c).
- **(b) Wrong-first worlds (PROVED).**
  - T1 ⋠_m R at every wrong-first world m, since W_m(R) = 0 < W_m(T1). So at most two worlds of a cover are
    wrong-first.
  - Thm L3.4 applies to a wrong-first world with (V) automatic: B^j gives i-wrong advice on available gambles.
  - (Imp) holds at every selected model that is not precise: silence → right advice on its non-null silent region is
    W-neutral and strictly better.
  - So such a world is compatible with closed choice only if the edge selection is **precise** at every first-hitting
    point t_c of the proof, i.e. on an uncountable set of edge priors. For precise models (Imp) genuinely fails:
    S = 0 already, and W-neutral exchanges are S-neutral. This narrow residual is not settled (CONJECTURE: it is
    empty).
- **(b′) Unanimities over a set A_i of directions in the closed quadrant (PROVED).**
  - If (1,0) ∈ A_i, world i never certifies T1 against R.
  - If (0,1) ∈ A_i, world i never certifies T1 against the precise model D_{p\*}, which is never silent on a two-sided
    domain.
  - Otherwise world i adds up, with any member as endorser.
- **(c) Adding-up two-grade worlds** (a > 0 in (a), or A_i in the open quadrant). The supporting assessment ψ falls
  under D1.
  - ψ has p\* ∉ E(ψ) and, by Prop M0, E(ψ) ≠ ∅.
  - The routes of Theorem gm, applied to ψ, need Prop necessary(a) (a.e.-unique coherent Bayes model at *every*
    interior prior), and that fails exactly on the atom chords E(ψ).
  - Through it, Hausdorff continuity of q ↦ K_q (R1 Prop 3.1, all routes) and the every-q CF chart form fail there.
    The every-q chart form is used in Lemma nostraddle (I2, C2, short route, via Thm collar(a)) and in the
    joint-continuity step of Lemma forcedlines (I1).
  - No other step of any route uses additivity beyond what ψ supplies.
  - This is D1's open branch. Nothing two-grade adds to it.

---

## 6. Status

| Result | Status |
|---|---|
| L3.1(a): on two-sided (LF) domains every ranking has precise vertex models | PROVED (from R10a Thm V, Cor V2) |
| L3.1(b),(c): two-sided gauges are normalised boxes; d_H(box, T1) ≥ c(ε) > 0 | PROVED; c(ε) NUMERICS |
| L3.2: fixed-margin gauge covers on M_U with d_H(K_u, T1) = O(a/b) | PROVED; NUMERICS |
| **L3.3: VB satisfies every requirement except closed sections; T1 covered; plateau; closed on int Δ** | **PROVED**; NUMERICS |
| L3.3(d): VB's worlds do not add up | PROVED |
| **L3.4: veto theorem (no closed choice for a world refining a paid veto)** | **PROVED** |
| L3.5: ordinal limits of gauge covers → T1 have a paid veto (under (N)) | PROVED |
| L3.5 without (N) | CONJECTURE (concavity on Av at the first visible scale is what is missing) |
| R5 repair with the natural selection rejected (one-positive veto) | CHECKED |
| L3.6: two-grade worlds | PROVED (a),(b),(b′); precise-edge escape for full vetoes: CONJECTURE (empty); (c) is the D1 residual, unchanged |
| A cover of T1 on a two-sided domain | none; (I) and (II) blocked as above |

**Referee priorities.**
1. Thm L3.4, steps 2–3: the E2 usc step along the edge, and openness of Q.
2. Thm L3.3(b), (C): the vector-uniqueness lemma, especially the claim that the range of σ contains a ball of L about 0.
3. Prop L3.1(a): the inclusion conv(W_j ∪ e_i) ⊆ H_j, and the ordering of x_j and x_k.
4. Thm L3.5: dominated convergence for the leading scale, and the "zero on an open set" step.

**The open question that remains** is the general one, with lexicographic structure removed. It has two parts:
- a world that does not add up and is *not* a refinement of any veto paid at a vertex (incomplete, non-lexicographic);
- or D1's adding-up branch with exceptional chords.

Ordinal limits and two-grade designs reach neither.
