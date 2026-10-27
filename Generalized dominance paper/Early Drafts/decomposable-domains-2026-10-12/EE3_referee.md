# EE3. Referee report on AUDIT_DD_slack.md (strict budget slack), DD1_notes.md and DD2_notes.md

17 Oct 2026, round 33 (BRIEF25). This is an adversarial, independent reading. Every proof named in the brief was
re-derived line by line. Labels for my own claims:
- **PROVED**: full argument here (one reader: me, unrefereed);
- **CHECKED**: exact finite computation (script in `ee3ref_py/`, run `python3 -I <name>.py` inside it);
- **NUMERICS**: sampled; nothing rests on it.

**Reruns.** All with `python3 -I`; the outputs are in `ee3ref_py/rerun/`.
- Identical byte for byte:
  - DD1: `test_geom`, `test_fast`, `verify_certs`, `edge_dirs`, `nc_window_exact`;
  - DD2: `patterns`, `cycle_check`, `veto_bfs` (21 s), `edge_chain` (41 s).
- `nc_window_exact.py` rewrites `dd1py/nc_window_exact.json` when run. Its content is unchanged.
- Not reproduced: DD1's `nc_transition_U`, `proj_width`, `pair_G` and `nc_local`. They need command-line arguments
  (D, ρ, N, seed) that are not recorded in the note or the `.out` files. They are NUMERICS and nothing depends on them.
  Record the invocations.
- I removed the `dd2py/__pycache__` that my reruns created. No other file outside `ee3ref_py/` and this note was
  touched.

---

## 0. Verdicts

| # | Item | Verdict |
|---|---|---|
| **S1** | Audit §2: r_i(Z) = 0 for the everywhere-contradictory Z; exact budgets impossible | **CORRECT** |
| **S2** | Lemma 1: X ⪯_i Y ⇒ r_i(X) ≥ r_i(Y) | **CORRECT.** It uses r_i(X) ≤ 1, which competitiveness at e_i forces |
| **S3** | Lemma 2: protection; undominatedness; (C) | **CORRECT.** Injectivity of the selection is *forced* by r(C_p) = p, not an extra assumption |
| **S4** | Lemma 3: C_p ≺_i X at every world, p_i = r_i(X) + s/3 | **CORRECT.** p ∈ int Δ; C_p is defined (the selection covers Δ) and ≠ X; strict at every world |
| **S5** | Competitiveness and closed sections from the caps | **CORRECT** (the supp p clause included) |
| **S6** | Downward closure keeps strict slack, limit stages included | **CORRECT.** Better stated as a least fixed point; including the endpoint is *forced*, not chosen (§1.6) |
| **S7** | (F1), (F2) exhaust the failures | **CORRECT**, with the precondition that the selection is injective. Failures of protection, (C) and selected-layer strict (G) all appear as (F1) |
| **D1** | DD1 Prop 1.1: patched family coherent, continuous in measure, injective | **CORRECT** |
| **D2** | DD1 Thm 2.1: reduction to coordinate thresholds | **CORRECT** |
| **D3** | DD1 Thm 2.4 (NC) | **CORRECT.** It uses only Σr ≤ 1, so it survives strict slack verbatim |
| **D4** | DD1 Prop 2.5, "equality only on the diagonal" | **Statement CORRECT (CHECKED, boundary included); proof GAP (fixable).** The margin c(p¹) vanishes on ∂Δ; the proof covers p¹ ∈ Δ° only |
| **D5** | DD1 nine certificates and the forbidden configuration | **CORRECT** (independently CHECKED). **GAP (wording):** a window binds only if its witnesses lie outside every bump. In the D = 3/50 design one witness lies inside a bump (harmless there) |
| **D6** | DD1 Prop 2.6, commuting squares | (a) **CORRECT**; (b) **GAP (fixable):** the argument is a sketch. A support-function proof is in §2.6. (c) **CORRECT** given (b); also extends to edge and vertex models |
| **D7** | DD1 Lemma 2.7, seeds harmless | **CORRECT for bounded cells.** False as stated for conic cells. DD2's tension is real but conditional (§2.7) |
| **D8** | DD1 Lemma 3.2 / Cor 3.3 (frontier) and Prop 3.4 / Cor 3.5 (Pexider) | **CORRECT as conditionals on r(X) ∈ Δ (confirmed).** Under strict slack the frontier rule collapses into Lemma 2. Prop 3.4(a),(b) survive; (c) and Cor 3.5 fail (explicit non-affine example, §2.8) |
| **E1** | DD2 Thm 3.3 / Cor 3.4 | **CORRECT modulo the imported chain, with the audit's scope.** Hypothesis (iii) restricts only comparisons *out of selected models* with records off R. **GAP (statement):** (a) concerns the transported field. **WRONG as worded:** the summary's claim "uses only competitiveness and continuity" (§0 item 3) and §3.3's "beside the point while R is bounded" both omit (iii) |
| **E2** | DD2 Lemma 2.2, Cors 2.3–2.4: defence regions are closed lower sets | **CORRECT** |
| **E3** | DD2 Prop 2.5: thresholds on edges | **CORRECT** |
| **E4** | DD2 Prop 3.8: valued bundle worlds | **CORRECT** |
| **E5** | DD2 §3.5: cell-level veto | **Conclusion CORRECT; method GAP, now closed.** `veto_bfs.py` transports generators only, not composites. I computed the full closure (transitivity plus (IB) transport of every accepted pair to a fixed point). It is clean at both edges (CHECKED). No positive additive certificate exists (LP infeasible), so the cleanliness is genuinely non-additive |

No item that the strict-slack programme relies on is WRONG. The one WRONG verdict (E1) concerns how DD2 summarises
its own theorem.

---

## 1. The audit's strict-budget-slack lemmas

Notation:
- (T) means: C_p ⪯_i X ⟺ p_i ≥ r_i(X), with r_i(X) ≥ 0.
- (SS) means: Σ_i r_i(X) < 1 for every X ∉ {C_p : p ∈ Δ}.
- r(C_p) = p throughout.

### 1.1 S1: r_i(Z) = 0 (CORRECT)

1. Z accepts every gamble, so its advice is × on every problem, and × is ranked worst at every world.
2. A coherent D_K never gives ×, since P_K(f) > 0 and P_K(−f) > 0 are incompatible. So C_p is pointwise strictly
   better than Z at every world, and C_p ⪯_i Z by (G).
3. Hence the section is all of Δ, which contains points with p_i = 0, so r_i(Z) = 0.

Strictness of (G) is not needed.

Scope remark: the argument needs a model that is weakly worse, at each world i, than some selected model with
p_i = 0. On the full domain Z is such a model. On M_U no model is ×-valued, and I see no immediate analogue there. This
is irrelevant to the programme, which runs on the full domain.

### 1.2 S2: Lemma 1 (CORRECT)

Transitivity gives {p : C_p ⪯_i X} ⊆ {p : C_p ⪯_i Y}. Since r_i(X) ∈ [0,1], pick p ∈ Δ with p_i = r_i(X). Then
p_i ≥ r_i(Y).

The bound r_i(X) ≤ 1 is not an extra assumption. Competitiveness at e_i, whose support is {i}, forces
e_i ∈ A_i(X) (DD2 Lemma 2.2(d)). Without it the inclusion is vacuous when the section is empty.

### 1.3 S3: Lemma 2 (CORRECT)

The proof is as written:
- X ⪯_i C_p at every i gives r(X) ≥ p coordinatewise, so Σ r(X) ≥ 1.
- By (SS), X = C_q. Then q ≥ p coordinatewise, and both sum to 1, so q = p.

Two remarks:
- r(C_p) = p makes p ↦ C_p injective automatically: C_p = C_q forces p = r(C_p) = q. So injectivity is a
  consistency condition on the chosen family, not an extra hypothesis. DD1 Prop 1.1(d) supplies it.
- Undominatedness, the absence of all-world ties with selected models, and (C) follow at once, given C_L = {C_p}
  (S4).

### 1.4 S4: Lemma 3 (CORRECT)

Here s = 1 − Σ r_j(X) > 0, and r_i(X) ≥ 0.
- p ∈ Δ: Σ p_i = Σ r_i + s = 1, and p_i ≥ s/3 > 0. So p ∈ int Δ.
- C_p ⪯_i X: since p_i > r_i(X).
- Not X ⪯_i C_p: Lemma 1 would give r_i(X) ≥ p_i > r_i(X).

So C_p ≺_i X at **every** world.
- "C_p undefined" cannot happen: (S) gives a selection on all of Δ.
- "C_p = X" cannot happen: X is nonselected. It would also give r(X) = p with Σ = 1, contradicting (SS).

Consequently U_L = C_L = {C_p}, and (LA) and (C) hold.

Side observation: the dominating index is always interior. Edge-selected models are never needed as dominators.

### 1.5 S5: caps (CORRECT)

The sections {p_i ≥ r_i} are closed.

Competitiveness on supp p follows from Σ r ≤ 1: if p_i < r_i for every i ∈ supp p, then
1 = Σ_{supp p} p_i < Σ r_i ≤ 1.

The converse also holds, so Σ r ≤ 1 is exact (DD1 Thm 2.1(c), DD2 Cor 2.3).

### 1.6 S6: the closure process (CORRECT; recommended formulation)

**Formulation.** Let 𝔄 be the lattice of world-labelled relations containing the fixed initial data:
- guidance;
- seeds;
- the caps of r⁰, with r⁰(C_p) = p.

Define Φ(R) as the closure under transitivity and (IB) of R together with the caps
{C_p ⪯_i X : p_i ≥ inf{q_i : (C_q, X) ∈ R_i}}.

Φ is monotone: a larger R gives smaller infima, hence larger caps. By Knaster–Tarski it has a least fixed point R*.
The audit's transfinite iteration reaches R*.

**Exact sections at R*.** Fix X and i, and let S = {p : (C_p, X) ∈ R*_i}. Then S contains the cap at inf S, and
every p ∈ S has p_i ≥ inf S. So S equals that cap. Thus (T) holds at R* with r = r*, and r* ≤ r⁰.

**Strict slack survives.** Σ r*(X) ≤ Σ r⁰(X) < 1 for every nonselected X, limit stages included. (CORRECT.)

**Adding the endpoint is forced, not a choice.** Suppose a successful system extends the current relation and
keeps r(C_q) = q. Its section at X is closed and contains S. So it contains a limit point p* with
p*_i = inf S, and then it contains every C_q ⪯_i C_{p*} ⪯_i X with q_i ≥ p*_i.

Hence **R* is contained in every successful system that extends the initial commitments and keeps the selected
thresholds pinned.** The decisive theorem is therefore *equivalent* to:

> some strict-slack r⁰ has a least fixed point with neither (F1) nor (F2).

This is sharper than the audit's "sufficient".

### 1.7 S7: exhaustiveness (CORRECT)

Suppose R* has no (F1) and no (F2). Then:
- transitivity and (IB) hold by construction;
- weak (G) is installed, and strict (G) is the absence of (F2) (X1 Thm 1.1.1);
- (T) holds exactly with r(C_p) = p, and (SS) holds;
- Lemmas 1–3 then give closed sections, competitiveness, undominatedness, (LA) and (C);
- (LF) holds because the domain is the full domain;
- T1 is selected at u.

Every other conceivable failure appears as (F1).
- **Protection.** Suppose X ⪯_i C_p at every i with X ≠ C_p. Composing with X's caps gives C_q ⪯_i C_p for
  q_i = r_i(X). By (SS), some coordinate has r_i(X) < p_i, and that is (F1).
- **(C)** and **selected-layer (SL)-(G):** the same argument applies.

Precondition: the selection is injective (§1.3). Otherwise r⁰ is ill-defined.

---

## 2. DD1

### 2.1 D1: the patched family (CORRECT)

I checked the following.
- **Bump separation.** |d_k| = 1 and the d_k are 120° apart, so |q_k − q_l| = D√3 = 0.104 > 2ρ = 0.05. D > ρ, so u is
  in no bump, and the bumps lie in Δ°.
- **(b) Continuity.** |P_K(h) − P_L(h)| ≤ d_H(K,L)·|h|. So advice is locally constant off ∂D_K ∪ −∂D_K, which is
  null; dominated convergence (μ finite) finishes.
- **(d) Injectivity.**
  - `edge_dirs.out` lists *unoriented* edge directions. The union rule dir(A+B) = dir(A) ∪ dir(B) holds for
    unoriented directions as well, and K_4 has no parallel edges (6 vertices, 6 directions). So the counts 4, 5, 6
    and the pairwise differences of at least 4 are valid.
  - The cancellation step is valid via support functions. Triangles are Minkowski-indecomposable, and K_k has at
    least 4 vertices.
  - The posterior step rests on Prop 2.6(c), which I CHECKED (§2.6, `shared_vertex.out`).

### 2.2 D2: Thm 2.1 (CORRECT)

The reduction is as written. Note that the reduction itself already allows Σr < 1; the audit's point concerns only
§3.

### 2.3 D3: Thm 2.4, (NC) (CORRECT)

The steps:
- X ≠ C_{p^i} and X is weakly i-better. World-i rank is injective in the advice, so X ≺_i C_{p^i}, and hence
  r_i(X) > p^i_i.
- p := (p^i_i)/Σ violates competitiveness.
- In the selected case X = C_{p^m}, injectivity gives r_i(X) = p^m_i > p^i_i when p^i ≠ p^m.

Only Σr ≤ 1 is used. **(NC) and the nine windows remain necessary conditions under strict slack.**

### 2.4 D4: Prop 2.5 (statement CORRECT, proof GAP)

The proof's margin is c(p¹) = min(p¹_o, 1 − p¹_o). It vanishes when p¹ ∈ ∂Δ. The ratio-cone representation
q ∈ cone(p, e_j, e_l, −e_o) is also derived by diagonal rescaling, which needs p > 0. So "equality only on the
diagonal" is proved only for p¹ ∈ Δ°.

**What I checked (CHECKED, `check_nc.out`).** I used my own exact compatibility test (`indep_compat.py`). It enumerates
the extreme rays of the closed polyhedral cones acc/rej ∩ cl Q_o and shares no code with `geom.py`.
- It agrees with DD1's `compatible_fast` on 600 posterior triples (133 compatible, a third with p¹ ∈ ∂Δ):
  0 mismatches.
- I ran **all** triples on the grids Δ ∩ (1/6)ℤ³ and Δ ∩ (1/8)ℤ³, boundary and vertices included: 1153 and 3555
  compatible triples, with 0 violations of "Σ p^i_i ≤ 1, with equality only on the diagonal".

**Partial boundary proof (PROVED).** Suppose p¹_o = 0 for some o ∈ {2,3}. Then K^1 accepts all of Q_o, since
m_o = 0 on K^1. So acc(K^1) ⊆ acc(K^o) forces K^o to accept all of Q_o. Sending h_o → −∞ gives m_o = 0 on K^o, so
p^o_o = 0 = p¹_o, and that gap is 0.

The remaining boundary cases reduce to edge models, which ignore one coordinate, and pointwise comparability then
forces equality. I verified this by hand on edges and vertices, but did not write it out in full.

**Fix.** Either add the boundary analysis, or state Prop 2.5 on Δ° and cite the grid check for ∂Δ.

### 2.5 D5: the nine certificates (CORRECT; wording GAP)

Independent confirmation (CHECKED, `check_nc.out` (a)):
- all nine triples are compatible under my cone test;
- each window value equals 1 − p^j_j − p^l_l exactly;
- the witnesses are interior points of Δ.

The forbidden configuration at D = 1/4 is confirmed: (q_2)_2 = 0.5101 ≥ 99/200, and every witness is at least 0.0785
from every bump centre (ρ = 0.025). So all witnesses are genuine posterior models.

**Wording.** A certificate binds a design only if its two witnesses p^j, p^l lie outside every bump. Otherwise
C_{p^j} is not D_{K⁰_{p^j}}. In the adopted design D = 3/50, the K_3/slot-1 witness (19/50, 29/100, 33/100) lies inside
q_4's bump (distance 0.0055). This is harmless, because q_3 lies inside its window anyway. But the table should read
"(q_k)_i < U whenever the witnesses are posterior indices".

### 2.6 D6: Prop 2.6, commuting squares

**(a) CORRECT.** C_{p'} = C_p on supp R1 because both records fix the from-advice there. Also p' ≠ p, since
otherwise C_q = C_{q'} and q = q' by injectivity.

**(b) GAP (fixable).** The text is a sketch: "both supports approach" a common facet piece is not shown. Here is a
complete argument (PROVED).

1. **Lines picture.** Identify h with the affine function m ↦ h·m on the plane Σm = 1. Write it as n·m − c. This
   linear change of variables preserves null sets. Then h ∈ D_K ⟺ c < g_K(n) := min_{m∈K} n·m. So D_p △ D_q is the
   region of c strictly between g_p(n) and g_q(n).
2. **Disjointness.** Disjoint supports of R1 and R2 (as symmetric sets) imply that for a.e. n, the signs of
   g_q − g_p and g_{p'} − g_p are not equal and nonzero.
3. **Convexity.** Suppose instead that, on an open set of n, the signs are opposite and both nonzero. Then the fibre
   of D_{q'} = D_p ⊕ R1 ⊕ R2 is (−∞, min) ∪ [g_p, max), which has a gap. So D_{q'} is not of the form
   {c < g(n)}, and is not coherent.
4. Hence N_1 := {g_q ≠ g_p} and N_2 := {g_{p'} ≠ g_p} are disjoint open sets of directions.
5. **Each vertex of K_p is shared.** For each vertex v of K_p with open normal arc A_v, one of three cases holds:
   - A_v misses N_1: then g_q = g_p on A_v;
   - A_v misses N_2: then g_{p'} = g_p on A_v;
   - A_v meets both: then g_q = g_p on the open set A_v ∩ N_2.

   In each case a support function equals n·v on an open arc. So v is a vertex of K_q or of K_{p'}.

**(c) CORRECT given (b).**
- `shared_vertex.out`: no two vertex identifications give the same q ≠ p (CHECKED, exact).
- Edge models (segments on one edge): the two shared endpoints force q and p' onto opposite sides along the edge.
  Then g_q − g_p and g_{p'} − g_p are nonzero with opposite signs for every n not normal to the edge, so (b)'s
  coherence condition fails.
- Vertex models: only K⁰_{e_i} contains e_i.

So the posterior family has no commuting squares anywhere on Δ.

### 2.7 D7: Lemma 2.7 and the bounded/conic tension

**The lemma is CORRECT for bounded cells.**
- Coherent advice and sign(h_i) are invariant under scaling, so the strict-improvement set is a cone.
- A measurable cone that is null outside a ball is null. (Lebesgue null sets are scale-invariant, and Gaussian
  measure has the same null sets.)

**Consequences (i) and (ii) are CORRECT.**
- (i) needs C_p ≠ B_k, which holds because X_k^A is worse than B_k on the cells S ∋ k. It then needs strict (SL)-(G)
  to get p_1 < (q_k)_1.
- (iii) I did not re-check. Nothing below uses it.

**The tension is real but conditional.**
- Lemma 2.7 fails for conic cells: a difference of coherent cones can live in a narrow cone, namely near a corner ray
  (an edge line of K).
- DD2 Thm 3.3 is against bounded cells **only under (iii)**.
- BRIEF25 keeps bounded cells and leaves the comparisons off R free. So Lemma 2.7 is available to the programme, and
  Thm 3.3 does not apply to it (§3.1).

### 2.8 D8: frontier rule and Pexider rigidity

**Both conditionals are confirmed.** Lemma 3.2 and Prop 3.4 explicitly assume r(X) ∈ Δ. Under (SS), C_{r(X)} does not
exist.

**Frontier rule under (SS) (PROVED).**
- **Statement.** Let p ∈ Δ with p ≥ r(X); such p exist, e.g. Lemma 3's index. Then no selected C_v agrees with X on
  supp rec(C_p, X).
- **Proof.** Lemma 3.2(b) verbatim, with Lemma 2 in place of (T3).
- **Effect on Cor 3.3(a).** It becomes: r(X_E) ≰ p and r(X_E) ≰ q coordinatewise.
- **Reading.** This is exactly protection of C_q, respectively C_p, transported by (IB). Under (SS) it adds nothing
  beyond Lemma 2.
- **Cor 3.3(b).** Its hypothesis Σλ_kν(E_k) = 0 is incompatible with (SS), which forces Σ_iν_i(E) < 0. So (b) is moot.

**Pexider rigidity.**
- (a) and (b) use no budget and survive: r_i(X_q) = ρ_i(q_i) is nondecreasing, and verdicts are constant on A_t.
- (c) needs Σ_i ρ_i(q_i) = 1, and fails under (SS).

The audit's example ρ_i(s) = s² satisfies (a)–(b) only for a record t accepted at every world (since s² ≤ s), which
is a guidance-worsening t.

**A better counterexample (PROVED; sampled in-session, 0 violations in 2·10⁵ points).** Let t be a local strict
world-1 improvement that worsens worlds 2 and 3. Take
- ρ_1(s) = s + ηs²;
- ρ_2(s) = ρ_3(s) = (1 − 2η)s;
- 0 < η < 1/2.

Then:
- each ρ_i is nondecreasing and non-affine;
- ρ_1(q_1) > q_1, so world 1 rejects t, as strict (G) requires;
- ρ_j(q_j) ≤ q_j, so worlds 2 and 3 accept, as guidance requires;
- Σρ = 1 + η(q_1² + 2q_1 − 2) < 1 exactly when q_1 < √3 − 1.

So on any agreement region inside {q_1 < 0.73}, the local constraints of Prop 3.4 hold with strict slack and without
homothety. Cor 3.5 (homothety toward e_1, with 1 − c = O(diam D)) has no strict-slack analogue.

---

## 3. DD2

### 3.1 E1: Theorem 3.3 (CORRECT modulo the imported chain; scope as the audit says)

**Proof re-derived.**
- **Step 1** is CC1 Thm 3.1(a) restricted to competitors that agree with C_q on R. DD3 rated CC1 Thm 3.1 CORRECT;
  the restriction changes nothing.
- **Step 2.** T(h) = h + Mh/|h| is a diffeomorphism onto {|h| > M} that preserves null sets. For h ∈ B ∖ R_0, the
  ray of h misses the conic R_0, and |T(h)| > M, so T(h) ∉ R. Coherent advice and world ranks are ray-invariant.
- **Steps 3–4.** The transported field is bounded and strictly guiding, with φ = φ⁺ > 0. Conditions (γ₀) and (γ)
  then come from CC1 Lemmas 3.3–3.4′, and the chain is invoked at its DD3/CC3 status.

**Scope (confirmed, and slightly narrower than the audit's phrasing).** Hypothesis (iii) constrains only accepted
comparisons **out of selected models** whose records lie off R (X = C_q a.e. on R). It leaves unconstrained:
- every comparison whose record meets R;
- every comparison between nonselected models.

The justified conclusion is the audit's: bounded seeds cannot rescue a system whose off-R comparisons from selected
models stay in finite-seed countably additive envelopes.

**Statement GAP, conclusion (a).** ℓ^τ is defined only on R^c, because Ψ_i lives on R^c. So "C_q is weak-Bayes for
ℓ^τ a.e. off R_0" is ill-posed on R ∖ R_0. The proof establishes this for the **transported** field ℓ′. Restate (a)
with ℓ′, as the audit says. Part (b) is unaffected.

**WRONG as worded:**
- §0 item 3: "it uses only competitiveness and continuity of the selection, so it applies to DD1's thresholds and to
  every relaxation";
- §3.3: "every bundle-internal repair … is beside the point while R is bounded".

Both omit (iii), which DD2's own Cor 3.4 and its (α)/(β) discussion state. Fix: append "under (iii)" to both.

**Positive reading for the programme (PROVED, contrapositive).** Take any successful system with bounded seed region
R, a continuous selection, and T1 = C_u. Then **for every** choice of finite envelope data (λ_i, Ψ_i, G_i) on R^c,
some accepted C_q ⪯_i X with record off R lies outside the envelope.

Step 1 of the proof shows where this happens: at Lyapunov-shrunk competitors that are additively worse at every
world in supp q. So, with bounded cells, the strict-slack construction must accept off R small records that every
fixed finite envelope rejects. Its non-additivity off R cannot be of finite-seed type. This is a necessary condition
on r⁰ and its closure, not an obstruction.

**Conjecture 3.7** remains a conjecture, as the audit says. DD3 noted that CC2 Cor 5.7 can be strengthened to every
off-plane boundary point, but that result is for Brier cores only.

### 3.2 E2: defence regions are closed lower sets (CORRECT)

- Lemma 2.2(a)–(c) are transitivity. (d) is KKM at e_i.
- **Cor 2.3.** An up-set in coordinate i that is compact and nonempty is the cap {q_i ≥ min}. KKM ⟺ Σr ≤ 1.
- **Cor 2.4.** Lower sets of a chain are initial segments.

### 3.3 E3: edge thresholds (CORRECT)

For p on edge {i,j} with odds o, K⁰_p is the segment with odds in [o/κ, oκ]. On the opposite-sign quadrant the advice
moves through −, 0, + as o increases.
- Weak (G) then gives q ⊑_i p for q closer to e_i, and strict (G) forbids the converse. So ⊑_i on the edge is exactly
  the p_i-chain.
- Each A_i(X) ∩ edge is a closed upper ray in p_i containing e_i.
- Covering the edge with supported worlds forces a_i + a_j ≤ 1.

This is consistent with (SS), since there a_i = r_i(X).

### 3.4 E4: valued bundle worlds (CORRECT)

- Ladder vectors telescope, so composites add.
- (V1) is superadditivity. V takes finitely many values, so the integral is defined in [−∞, ∞).
- Strict (G): either a non-null set of bundles carries d ≤ 0 with d ≠ 0, where V < 0, or the off-R part improves
  strictly, where the strictly guiding ℓ^off is < 0. Both parts are ≤ 0.
- (IB): Φ_1 depends only on the record.
- **(e)** V_B: (B) is closed under composition (audit Lemma 1; DD3 A2), so (V1) holds.
- **(d)** The conversion cycle is reproduced exactly (`cycle_check` identical). Since every seed has V ≥ 0, some
  conversion must have V < 0.

### 3.5 E5: the cell-level veto (conclusion CORRECT; method gap closed)

**The gap.** `veto_bfs.py` transports each forced generator to every base and then takes the transitive closure. It
never transports **composite** records. This is the same gap DD3 (C2) found in CC1 Thm 1.1(b). In this fragment it
matters in principle, because paths can change a cell and later restore it.

**Full closure (CHECKED, `veto_ib_closure.out`).** I iterated Warshall closure followed by (IB) transport of every
accepted pair until nothing new appeared.
- Fixed point after 2 rounds, with 134 463 records and 1 067 256 accepted pattern pairs.
- **No strict world-2 improvement at edge {1,2}, and none at world 3 at edge {1,3}.**
- Sanity checks (`veto_sanity.out`):
  - 20 000 sampled triples: 0 transitivity violations;
  - sampled transports: 0 (IB) violations;
  - the improvement detector fires on an injected improving move.

**Additive certificate fails (CHECKED, `veto_record_closure.out`).** No weights w ≥ 1 make every forced record's
world-2 (resp. world-3) rank sum ≥ 0: the LP is infeasible at both edges. So the cleanliness is not explained by any
additive world-2 valuation.

DD2's verdict, "a world-1 veto alone is not refuted at the cell level", stands, now on the correct closure. Its scope
is a fragment: one bundle, three advices, × omitted.

---

## 4. A nearby positive result for the decisive theorem (PROVED, one reader)

The audit's process makes it natural to ask which initial assignments survive the **transitive** part of the
closure. That part can be settled now.

**Setting.**
- Let λ_i(X) := max{p_i : X is pointwise weakly i-better than C_p}, or 0 if no such p exists.
- The set {p : X weakly i-better than C_p} is closed, because q ↦ C_q is continuous in measure and advice is
  four-valued. So the max is attained.

**Proposition EE3.1.** Assume:
- (SL) is consistent with weak and strict (G) at the selected layer;
- (NC*): Σ λ(X) < 1 for every nonselected X;
- the seed cells are bounded (Lemma 2.7 applies).

Then:
- (a) **When (NC*) holds.** It holds whenever all three witness sets of X are nonempty and compatible triples off the
  diagonal have Σ p^i_i < 1 (strict (NC)).
  - If a witness set is empty, (NC*) needs the two-slot form: K^2 ≤_2 K^1 forces p^1_1 + p^2_2 ≤ 1 − p^1_3.
  - Equality there forces an edge configuration with X selected. The posterior gap argument shows this, with the
    boundary caveat of §2.4. This case is a sketch, not proved.
- (b) For each nonselected X choose δ_X > 0 with 3δ_X < 1 − Σλ(X). For seed competitors also require
  δ_X ≤ (q_k)_1 − λ_1(X_k^A), which is > 0 by Lemma 2.7 and strict (SL)-(G). Then r⁰ := λ + δ_X·𝟙 satisfies (SS)
  and retains the seeds.
- (c) The closure of guidance ∪ caps(r⁰) ∪ seeds **under transitivity and cap completion only** contains no (F1)
  and no (F2).

*Proof.*
- **(a)** When all three sets are nonempty, the maximisers (p^1, p^2, p^3) form a compatible triple witnessed by X.
  If Σ = 1 they are equal, say p^i = p*. Then X is weakly better than C_{p*} at all three worlds, so X = C_{p*},
  because coherent advice is Pareto-optimal in the three background orders (DD3 A6). That contradicts X being
  nonselected.
- **(c)** Every non-guidance step starts at a selected model. So a chain from C_a to C_b splits into segments of
  three kinds:
  - guidance only;
  - a cap C_a → X followed by guidance to C_b;
  - a seed B_k → X_k^A followed by guidance to C_b.

  Each segment gives a_i ≥ b_i:
  - for a cap segment, by r⁰_i(X) > λ_i(X) ≥ b_i;
  - for a seed segment, by Lemma 2.7.

  So there is no (F1). For (F2), let Y →guid* C_a → … → C_b → X →guid* Y′ with Y′ strictly i-better than Y. Then X
  is strictly i-better than C_a.
  - In the cap case, this gives b_i ≥ r⁰_i(X) > λ_i(X) ≥ a_i.
  - In the seed case, Lemma 2.7 and strict (SL) give a_1 < b_1.

  Either way this contradicts a_i ≥ b_i.
- Cap completion adds nothing here: lowered thresholds are minima of r⁰ along guidance chains, and their caps are
  already transitive consequences. ∎

**Status of the hypotheses.**
- For the unpatched posterior family, with seeds absent, they hold on interior witness triples (Prop 2.5). Boundary
  triples are CHECKED on grids (§2.4), and the empty-witness case is the sketch in (a).
- For the patched family they are DD1's NUMERICS.

**What remains.** All remaining difficulty in the decisive theorem lies in **(IB) transport of caps and composites to
nonselected bases**. That is where (F1) or (F2) must be sought. This localises the open problem. It does not
solve it.

---

## 5. Requested changes

1. **AUDIT_DD_slack §3.** Note that injectivity is forced by r(C_p) = p. State the closure as a least fixed point, and
   note that adding the endpoint is forced, so the decisive theorem is an equivalence (§1.6).
2. **DD1 Prop 2.5.** Add the boundary case, or restrict the statement to Δ° and cite the grid check.
3. **DD1 §2.4 table.** Add "whenever the witnesses are posterior indices"; flag the K_3/slot-1 witness inside q_4's
   bump at D = 3/50.
4. **DD1 Prop 2.6(b).** Replace the sketch with the support-function argument of §2.6, and extend (c) to edge and
   vertex models.
5. **DD1 §§3.2–3.3.** Label them "under r(X) ∈ Δ (exact budget; inconsistent on the full domain)". Add the
   strict-slack frontier rule (§2.8). Mark Prop 3.4(c) and Cor 3.5 as not transferring.
6. **DD1 scripts.** Record the command-line arguments of the four NUMERICS scripts.
7. **DD2 Thm 3.3(a).** State it for the transported field ℓ′. In §0 item 3 and §3.3, add "under (iii)".
8. **DD2 §3.5.** Replace the generator-transport BFS by the full closure, or cite `ee3ref_py/veto_ib_closure.py`.

## 6. Files (`ee3ref_py/`)

- `indep_compat.py`: an exact compatibility test by H→V cone enumeration, independent of `geom.py`.
- `check_nc.py` → `.out`: the nine certificates, witness-to-bump distances, agreement with DD1, and Prop 2.5 on full
  grids (≈ 4 min).
- `shared_vertex.py` → `.out`: posterior triangles share at most one vertex.
- `veto_ib_closure.py` → `.out`: the full transitive + (IB) closure of the veto fragment.
- `veto_sanity.py` → `.out`: sanity checks for that closure.
- `veto_record_closure.py` → `.out`: the additive-certificate LP (infeasible).
- `rerun/`: rerun outputs of the DD1 and DD2 scripts.
