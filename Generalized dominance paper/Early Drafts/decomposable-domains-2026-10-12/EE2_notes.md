# EE2 (round 33, BRIEF25). The two failure modes of the strict-slack closure: shortest forced chains, the selected-layer transports the posterior family does carry, and what is (not) forced independently of the initial assignment

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument here, one reader (me), not refereed;
- **CHECKED**: exact rational computation with a stated script (or a step-by-step reading);
- **NUMERICS**: sampled; nothing rests on it;
- **CONJECTURE**.

Scripts: `ee2py/` (run `python3 -I <script>.py` inside it; outputs `*.out`). Domain: the full four-advice domain, three
worlds, the patched posterior family of DD1 §1 (D = 3/50, ρ = 1/40), r(C_p) = p, strict slack Σ_i r_i(X) < 1 for
nonselected X, exact threshold sections C_p ≼_i X ⟺ p_i ≥ r_i(X). No assumption is added; every extra hypothesis is a
hypothesis of a stated result.

---

## 0. Outcome

1. **There ARE assignment-independent IB-transports of selected comparisons, and the posterior family carries many
   (new).** A selected comparison C_s ≼_i C_t transports onto a pair (X, C_p) exactly when C_t is a.e. a *splice* of C_s
   and C_p; then X is the complementary splice (Lemma 2.2). In the posterior family every collinear triple s, t, p (t
   between) whose direction avoids three narrow double-sectors around the edge directions is a splice triple, at least
   for short segments (Thm 2.4: exclusion PROVED; the predicted sectors match an exact 1° sweep at u, CHECKED).
   - **T1 = C_u itself is a splice** of two other selected models, e.g. along the e_1-axis with |s − u| = |p − u| ≈ 0.024.
     These points lie in the posterior region of the patched family, so this is a statement about the actual family
     (CHECKED, `splice_cert.out`).
   - DD1 Prop 2.6 (no commuting squares of four *selected* models) does not exclude this: the fourth corner is
     nonselected.
   - Forced consequence (PROVED): r_i(X) ∈ (min(s_i,p_i), max(s_i,p_i)] at every world, so slack(X) < ½|s − p|_1. On
     level lines these become forced ties (CHECKED at c = (1/5, 3/5, 1/5)).
2. **Task 1: classification of the shortest F1 chains C_q ≼_i X ≼_i C_p, q_i < p_i (§3).**
   - Both links guidance or seeds: X exists iff C_q is pointwise weakly i-better than C_p (cone principle, PROVED). So
     this is selected-layer (G) and nothing else.
   - One link a selected transport (GT, TG): reduces to the same pointwise comparison. PROVED to first order (all four
     points in a small neighbourhood); CHECKED on 475 exact random instances, none found.
   - Both links selected transports: on one line consistent (PROVED); across lines it needs a partial agreement that I
     could not realise (CONJECTURE: none).
   - First link a cap: F1 is avoidable for X iff r_i(X) ≥ Λ_i(X) := sup{p_i : X ≼_i C_p forced}. It is unavoidable for
     **every** assignment iff Σ_i Λ_i(X) ≥ 1 (PROVED). This is the three-world (NC).
     - DD1's nine certificates are exactly such unavoidable chains, but only for designs with far bumps. For D = 3/50 the
       designated indices clear every window by ≥ 0.079 (CHECKED).
     - Seeds never enlarge Λ beyond compatible triples (PROVED).
     - T-relaxation does not either (CONJECTURE, first-order argument; NUMERICS 0/200).
   - Second link a transported cap: this is complementary-splice duality, which gives a partner-covering criterion for a
     forced protection failure (PROVED). The criterion cannot fire for bounded modifications (PROVED).
3. **Task 2: no assignment-independent obstruction at chain length ≤ 2 for the D = 3/50 design, beyond (NC) (§4).**
   The new transports do not obstruct strict slack.
   - **On a single splice line, strict slack is consistent.** In the discretised cube every strict-box initial assignment
     closes without F1 (PROVED; "rightmost change is forward" invariant).
   - In the continuum there is an explicit strict-slack fixed point: world-wise additive switch densities 1 + θλ along
     the line (PROVED; CHECKED on grid cubes, 0 violations).
   - The naive "slack ∝ gap" assignment is *not* a fixed point (CHECKED, 170–258 violations). So the initial assignment
     matters.
   - Responsible feature in the only known forced chains: the designated indices r(C_{q_k}) = q_k far from u (DD1). It is
     not strict slack, thresholds as such, or the selection family. The minimal modification is to keep q_k in the
     windows (already done).
   - **What remains for EE1:** endpoint inclusion (closed sections) combined with accumulation of transported caps
     *across* splice lines and with the seeds. Line by line nothing breaks. Any obstruction must be two-dimensional.
4. **Task 3, F2 (§5).**
   - One non-guidance generator: that generator is itself a strict improvement (PROVED).
   - Every F2 passing through a selected model C_s forces a threshold coincidence r_i(Y′) = s_i = r_i(Y). It is
     therefore the strict form of the same (NC) condition (PROVED). Assignment-independently it occurs iff selected-layer
     (G) fails (PROVED).
   - DD2's conversion cycle (its Lemma 2.10) is automatically blocked under exact sections (PROVED).
   - F2 among nonselected models only needs ≥ 2 transported caps (or a seed plus a cap). Seeds plus selected transports
     cannot produce it with two generators (PROVED). No assignment-independent F2 was found.
   - The mechanism to watch is step 4 of the closure (endpoint inclusion) at tight levels, which level-line ties create.

---

## 1. Records, generators, and two reductions

World i's accepted set 𝒜_i is a set of transition records (AUDIT_nonlinear_programme), closed under (IB) (it is a set of
records) and realisable composition. In the strict-slack closure its generators are:
- **G**: guidance-worsening records;
- **S** (world 1): the synchronised seed records (supports in the bounded cells R);
- **Cap**: rec(C_s, Z) whenever s_i ≥ r_i(Z), for every model Z.

The selected-layer records **Sel**, rec(C_s, C_t) with s_i ≥ t_i, are the caps at selected Z, because r(C_t) = t.
Transports of Sel onto non-selected pairs are called **T-links**.

**Lemma 1.1 (fixed points; PROVED).** The closure started at r changes no threshold, and in particular has no (F1), iff
r_i(X) ≥ r_i(Y) for every i and every pair (X, Y) whose record is a generator.
- (⇐) Monotonicity along generators passes to realisable composites by transitivity of ≥. So every forced C_q ≼_i Z has
  q_i = r_i(C_q) ≥ r_i(Z), which is already a cap.
- (⇒) This is the audit's Lemma 1 at the fixed point.

**Lemma 1.2 (F1 is decided by the last link; PROVED).** (F1) at (C_p, i) occurs iff the closure contains X ≼_i C_p for
some X with r_i(X) < p_i (current thresholds). For then C_q ≼_i X for q with q_i = r_i(X), by the cap.

So the task reduces to classifying the forced comparisons **into** selected models. Write

  Λ_i(X) := sup{p_i : X ≼_i C_p is in the closure}.

(F1) is avoided iff r_i(X) ≥ Λ_i(X) for all X and i, with strict inequality when the supremum is attained by a strict
comparison.

**Lemma 1.3 (one non-guidance generator; PROVED).** Suppose a composite of guidance records and a single other generator
ρ is a strict i-improvement. Then ρ itself is a pointwise weak i-improvement, strict on a non-null set.
- Ranks never decrease along guidance steps.
- So, pointwise, the rank change of ρ is at most the (non-positive) total change, and it is negative where the total is.

---

## 2. Assignment-independent generators

### 2.1 Seeds: the cone principle

**Theorem 2.1 (PROVED).** Let C_q, C_p be coherent. Suppose a realisable chain from C_q to C_p consists of guidance
steps and transports of records supported in a bounded set R. Then C_q is pointwise weakly i-better than C_p a.e.
- *Proof.* Off R every step is guidance, so the world-i rank is non-decreasing along the chain at a.e. h ∉ R.
- The set where C_p is strictly i-better than C_q is a cone, since coherent advice and sign(h_i) are scale-invariant.
- That cone lies in R up to a null set. A cone that is null outside a bounded set is null (DD1 Lemma 2.7). ∎

So seeds can never cause (F1) between selected models, at any chain length, unless selected-layer (G) fails. (F2)
from guidance and seeds alone is excluded by the audit's Lemma 1 (DD3, A2–A3).

### 2.2 Transports of selected comparisons are splices

**Lemma 2.2 (PROVED).**
- (a) rec(X, C_p) = rec(C_s, C_t) iff both of the following hold:
  - C_t = C_p a.e. on D := supp(C_s △ C_t); equivalently C_t(h) ∈ {C_s(h), C_p(h)} for a.e. h ("C_t is a splice of
    C_s and C_p");
  - X = C_s on D and X = C_p off D.
- (b) rec(C_q, X) = rec(C_s, C_t) iff C_s is a splice of C_q and C_t, and X = C_t on D, X = C_q off D.

*Proof.* Equal records have equal supports and equal before/after advice on them, and the two endpoints agree off the
support. ∎

If (s, t, p) is a splice triple, put

  X := C_s on {C_t = C_p ≠ C_s},  C_p on {C_t = C_s ≠ C_p},  common advice elsewhere.

This is the **complementary splice**. The square C_s → C_t → C_p, C_s → X → C_p commutes, with disjoint supports. X is
nonselected in the posterior part, by DD1 Prop 2.6(c).

**Lemma 2.3 (line criterion; PROVED).**
- *Coordinates.* Write g ↔ (θ, c), with θ = (g_1 − g_3, g_2 − g_3) and c = −g_3; this linear bijection preserves null
  sets. In 2-D coordinates m = (m_1, m_2), m·g = θ·m − c.
- *Advice of D_K.* D_K accepts g iff c < min_K θ·m; it rejects iff c > max_K θ·m; otherwise it is silent.
- *Splice test.* C_t is a splice of C_s and C_p iff, for every θ:
  - h_{K_t}(θ) and h_{K_t}(−θ) lie between the corresponding values for K_s and K_p;
  - the interval I_t(θ) lies in the closure of I_s(θ) ∪ I_p(θ).
- *Decision procedure.* Taking open arcs of θ between the perpendiculars of all point differences, and open c-intervals
  between all breakpoints, gives non-null cells covering a conull set. On each cell every class and every sign of g is
  constant. So any a.e. statement about the advice of finitely many polygonal models is decided exactly by finitely
  many representatives.
- *Scripts.* `cells.py` implements this and `splice.py` the support-function form. They agree on 72/72 cases
  (`t_cells.out`). Direct sampling of 40 000 random gambles per case finds no violation whenever the test says splice
  (`crosscheck_splice.out`).

### 2.3 Splice triples in the posterior family

**Proposition 2.3a (diagonal invariance; PROVED).** C_x = {g : x ⊙ g ∈ D_{T1}} (a.e.). Also {g : d ⊙ g ∈ C_x} = C_{ν(x⊙d)},
and g ↦ d ⊙ g preserves null sets. So (s, t, p) is a splice triple iff (ν(s⊙d), ν(t⊙d), ν(p⊙d)) is one. The maps
x ↦ ν(x⊙d) are projective, fix the vertices, and act transitively on Δ°.

**Theorem 2.4 (local splice directions).** Let s = t − δd and p = t + δd.
- **(a) PROVED.** At t = u define the open double sectors
  - E_1, between the rays (ε, 1, −1−ε) and (−ε, 1+ε, −1), together with their negatives;
  - E_2 and E_3, defined cyclically.

  If d ∈ E_k, then (s, u, p) is not a splice triple for any small δ. At other t, use the image sectors under 2.3a.
- **(b) CHECKED at u; CONJECTURE in general.** If d lies outside the closed sectors, (s, u, p) is a splice triple for
  small δ.
- *Predicted versus exact.* The predicted sectors in the chart angle of `splice_cert.py` are (10.18°, 28.07°),
  (68.63°, 111.37°) and (151.93°, 169.82°). The exact 1° sweep at δ = 1/100 gives non-splice exactly at 11–28°, 69–111°
  and 152–169° (`splice_cert.out`). Each sector contains one edge direction, and has width 180° − 154.6° = 25.4° at
  u in true angle (154.6° being the opening of Γ_k).

*Proof of (a).*
- **The acceptance region is a wedge.** For h of pattern (+,−,−), put f_k(q) = c_0 q·h + ε q_k h_k. Then f_1 > f_2, f_3,
  so Acc(h) := {q : C_q accepts h} = {f_2 > 0, f_3 > 0}. This is a wedge.
- **Its apex can be put at u.** That happens for h ∝ (κ′, −1, −1), with κ′ = (2c_0 + ε)/c_0.
- **The wedge's cone.** Since 3c_0 + ε = 1, the cone Γ_1 = {x_1 − εx_2 > 0, (1+ε)x_1 + εx_2 > 0} (with x_3 = −x_1 − x_2)
  has rays (ε, 1, −1−ε) and (ε, −1−ε, 1).
- **The violation.** Perturb h. The apex z sweeps a neighbourhood of u, and the cone varies continuously. Suppose
  d ∉ ±cl Γ_1. For apexes z with u − z ∈ int Γ_1 and |u − z| ≪ δ, the line through u in direction d meets z + Γ_1(z) in
  a short interval that contains u but neither s nor p.
- **Conclusion.** So C_u accepts while C_s and C_p are silent on an open set of h: the triple is not a splice. E_1 is
  the complement of ±Γ_1; E_2 and E_3 follow by symmetry. ∎

*Remarks.*
- (i) Half-plane regions can never separate the middle of a segment from both of its ends. The Acc-to-Rej crossing
  through silence needs a long segment. This is why (b) is plausible; it is not proved in general.
- (ii) No non-collinear local splice triples: 0 of the 1770 non-antiparallel direction pairs at 6° resolution are
  splice (`local_noncollinear.out`). None among 295 random far triples either (`test_posterior_splice.out`). Both are
  exact per sample; the sampling is NUMERICS.

**Certificates in the patched family (CHECKED, `splice_cert.out`).** Points within 7/200 = D − ρ of u lie outside every
bump, so their credal sets are posterior. The following are exact splice triples through u:
- s, p = u ∓ (1/100)(2, −1, −1), along the e_1-axis;
- s, p = u ∓ (1/100)(−1, −1, 2), along the e_3-axis;
- a generic 50° direction with half-length 1/20.

The edge-parallel direction (0, 1, −1) gives an explicit non-splice cell.

### 2.4 What the transports force

**Proposition 2.5 (PROVED).** Let (s, t, p) be a splice triple on a line along which every coordinate is strictly
monotone, and let X be the complementary splice. Let i be a world with s_i > t_i > p_i.
- X ≼_i C_p, because rec(X, C_p) = rec(C_s, C_t).
- C_s ≼_i X, because rec(C_s, X) = rec(C_t, C_p).
- C_p ⋠_i X, because rec(C_p, X) = rec(C_t, C_s) is rejected by exact sections.

Hence r_i(X) ∈ (p_i, s_i]; symmetrically when the order is reversed. So

  r(X) ∈ ∏_i (min(s_i,p_i), max(s_i,p_i)],  and  1 − Σ_i r_i(X) < ½|s − p|_1.

- At u along the e_1-axis, r(X) ∈ (0.3133, 0.3533] × (0.3233, 0.3433]². At world 1 the forced comparisons are guidance
  (the e_1-axis is a guidance line for world 1); at worlds 2 and 3 they are not (CHECKED).
- Along the generic direction, none of the six forced comparisons is a guidance comparison (CHECKED). The T-links are
  genuinely new information.

**Level lines (CHECKED, `level_lines.out`).** The level line {x_1 = 1/5} through (1/5, 3/5, 1/5) is a splice line. It is
not one through u, (1/4, 1/2, 1/4) or (3/5, 1/5, 1/5). Along such a line C_a ∼_1 C_b, and the transports force X ∼_1 C_s
∼_1 C_p, i.e. r_1(X) = 1/5 exactly. Together with the frontier rule (Lemma 3.7) this pins
r(X) ∈ {1/5} × (p_2, s_2] × (s_3, p_3].

---

## 3. Task 1: the shortest (F1) chains

Notation: C_q ≼_i X ≼_i C_p with q_i < p_i. The first link is of type G, S, T or Cap; the second of type G, S or T,
or a transported cap ("CT").

| first ∘ second | when such X exists | label |
|---|---|---|
| G, S ∘ G, S (any length) | iff C_q pointwise weakly i-better than C_p (Thm 2.1) | PROVED |
| G ∘ T, T ∘ G | first order: iff C_q pointwise i-better than C_p (Prop 3.2) | PROVED (first order); CHECKED 475 exact random instances: none |
| T ∘ T | same line: never; across lines: needs a partial agreement C_t = C_{s′} on D ∩ D′ | PROVED / CONJECTURE (none) |
| Cap ∘ (G,S,T) | avoidable iff r_i(X) ≥ Λ_i(X); unavoidable for all assignments iff Σ_iΛ_i(X) ≥ 1 (Thm 3.4) | PROVED |
| Cap ∘ CT | complementary-splice duality, partner covering (Prop 3.9) | PROVED; cannot fire for bounded modifications |

Pointwise i-comparison of posterior models holds only along lines through e_i, with the larger i-coordinate better
(ratio order, DD1 Lemma 2.3 / Prop 2.5). So the first three rows never produce (F1) in the posterior part. In the bumps
this is DD1's NUMERICS (18 pairs, all correctly oriented).

**Proposition 3.2 (GT, TG reduce to G; PROVED to first order).** Let q, s, t, p lie in a small neighbourhood of a point
of Δ°, with (s, t, p) a splice triple and X its complementary splice. If C_q is pointwise weakly i-better than X, then
C_q is pointwise weakly i-better than C_p.

*Proof (blow-up).* Near the point, a problem's classes are determined either by one line ℓ (half-plane type), with
normal in a fixed union of arcs N_i, or by a wedge z + Γ with a fixed cone.
- **Half-plane case.** Suppose ν·q < c < ν·p for a relevant i-good normal ν (an open set of offsets c). X must take
  s's class on all these lines, which forces ν·s ≤ ν·q and ν·t ≥ ν·p. Since t lies between s and p, ν·t ≤ ν·p, so
  ν ⊥ (t − p). So the violating normals would all be perpendicular to the line. They form an open subset of N_i, so if
  any exists, one survives.
- **Wedge case.** A violation by wedges with p inside and q outside has representatives with apex z just behind p. For
  those, s and t are on the same side of the wedge, since s − p ∥ t − p. So X takes p's class, and the violation
  persists.
- **TG** is the mirror image. ∎

The finite-size statement is CONJECTURE. `chain_tests.out`: 301 GT and 174 TG exact instances, including q on the
e_i-line through p, gave no chain.

**T ∘ T (PROVED on one line).** On a splice segment each problem switches advice at most once, at λ*(h). Records between
the models of the line are signed sets of switch parameters, and the T-links accept exactly the one-signed ones in the
coordinate-decreasing direction. A composite selected record [0,a] → [0,b] with the wrong orientation would need
cancellation of opposite-signed parts, and T supplies none.

**Theorem 3.4 (cap-mediated chains; PROVED).**
- (a) The chain C_q ≼_i X (cap) ≼_i C_p (forced) is excluded iff r_i(X) ≥ p_i.
- (b) If Σ_i Λ_i^0(X) ≥ 1, where Λ^0 counts only comparisons forced independently of the assignment (G, S, T and their
  composites), then **every** strict-slack assignment produces (F1).
  - Some i has r_i(X) < Λ_i^0(X). Take q with q_i = r_i(X); then C_q ≼_i X ≼_i C_p with q_i < p_i.
  - If X = C_m is selected, the same argument gives m_i ≥ Λ_i^0 for all i, hence equality, or (F1) directly.
- (c) Conversely, if Σ_iΛ_i^0(X) < 1, the single model X can be given an assignment avoiding all length-2 chains of
  this row. The coupling to other models is through row 5 only.

**Proposition 3.5 (seeds add nothing to (NC); PROVED).** Let X ≼_i Y_i ≼_i C_{p^i}, where Y_i is C_{p^i} or a
seed-transport of it.
- Off the bounded cells, X is pointwise better than C_{p^1}, C_{p^2}, C_{p^3} at the respective worlds.
- The conditions of DD1 Lemma 2.3 are cone conditions, so they hold a.e. and the triple is compatible. DD1's (NC) for
  compatible triples then gives Σ p^i_i < 1.

**Conjecture 3.6 (T-relaxation adds nothing to (NC)).** Replace C_{p^o} in slot o by Y_o = (C_{a^o} on D(a^o, b^o),
C_{p^o} elsewhere), where (a^o, b^o, p^o) is a splice triple and a^o_o ≥ b^o_o ≥ p^o_o, so that Y_o ≼_o C_{p^o} by T.
Then compatibility still forces Σ_o p^o_o < 1.
- *First-order reason.* A plain incompatibility with normal ν is witnessed on the whole offset interval
  (ν·p^j, ν·p^o). A needle interval ν·[a^o, b^o] never has ν·p^o as an endpoint unless ν ⊥ L_o. So the relaxation can
  absorb the violation only by using the needle's far end a^o, whose o-coordinate is larger. The triple then behaves as
  if a^o sat in slot o.
- *Numerics.* 0 of 200 near-diagonal triples with Σ ≥ 1 became compatible under random T-relaxations (`chain_tests.out`).

**The nine DD1 certificates (CHECKED, `dd1py/verify_certs.out`, `window_margins.out`).** Each is an exactly compatible
triple (K_{p^j}, K_k, K_{p^l}) giving Λ(X) > (p^j_j, (q_k)_i, p^l_l). By Theorem 3.4(b), (F1) is forced for every
assignment iff (q_k)_i ≥ U_i(k). These are exactly the assignment-independent (F1) chains of the brief.
- For D = 3/50: q_2 = (0.3333, 0.3758, 0.2909), q_3 = (0.2909, 0.3333, 0.3758), q_4 = (0.3758, 0.2909, 0.3333).
- The window margins are ≥ 0.0792, the minimum at (q_4)_1 against 91/200. **No certificate bites.**

### 3.5 Transported caps (the second link is CT)

**Lemma 3.7 (frontier rule, strict-slack form; PROVED).** Let Y be nonselected and m ∈ P(Y) := {m ∈ Δ : m ≥ r(Y)}.
Then no selected C_v ≠ C_m agrees with Y a.e. on supp(C_m △ Y).
- *Proof.* Otherwise Y′ := C_v reset to C_m's advice on that support has rec(Y′, C_v) = rec(C_m, Y). So Y′ ≼_i C_v at
  every world.
- Lemma 2 of the audit then gives Σ r(Y′) ≥ 1. So Y′ is selected and equals C_v, which is absurd. ∎

**Lemma 3.8 (complementary-splice duality; PROVED; DD2 §2.6 in threshold form).** Put W(E) := C_s on E, C_v off E.
Then rec(C_v, W(E)) = rec(W(E^c), C_s). Hence, at each world:
- r_i(W(E)) ≤ v_i ⇒ r_i(W(E^c)) ≥ s_i;
- r_i(W(E^c)) ≤ s_i ⇒ r_i(W(E)) ≥ v_i.

**Proposition 3.9 (partner covering; PROVED).** Let Y := C_s ⊕ (c on F) be nonselected, with partners A_c(F) := {v : C_v
= c a.e. on F}. Put W_v := C_v ⊕ (C_s's advice on F). Then rec(C_v, W_v) = rec(Y, C_s), and each nonselected W_v has
C_v ≼_i W_v at some world (because Σ r(W_v) < 1 = Σ v).
- So if, for every k ∈ Ω, some partner is forced to have C_v ⋠_j W_v at both j ≠ k, then Y ≼_k C_s at all three
  worlds. That contradicts strict slack, so (F1) is forced for every assignment.
- This is the exact assignment-independent form of the frontier rule.

**Proposition 3.10 (it cannot fire for bounded F; PROVED).** Let F be bounded.
- **Guidance.** By the cone principle, a forced W_v ≼_j C_m via G or S needs C_v ≥_j C_m pointwise. That gives
  m_j ≤ v_j, by ratio order in the posterior part.
- **Transports.** A forced W_v ≼_j C_m via T makes rec(C_v, C_m) a selected record equal to another one. By DD1 Prop
  2.6(c) then (v, m) = (a, b), so m_j ≤ v_j.
- So the only forced exclusions are the worlds where the fixed record (c → C_s on F) is a strict pointwise improvement.
  These are the same for every partner, so at most one world k is ever forced. ∎

---

## 4. Task 2: is there an assignment avoiding all such chains?

### 4.1 The exact first-generation constraint system

For every nonselected X, with Λ^0 and μ^0_i(X) := inf{q_i : C_q ≼_i X forced} computed from G, S and T:
- (i) Λ^0_i(X) ≤ r_i(X) ≤ μ^0_i(X), strict at attained strict comparisons;
- (ii) Σ_i r_i(X) < 1;
- (iii) duality (Lemma 3.8) for every complementary pair of 2-splices;
- (iv) the frontier rule, which follows from (ii) and (iii).

All length-2 chains are avoided iff (i)–(iii) hold (§3). Condition (i) needs Λ^0 ≤ μ^0, the single-world rows of §3; and
Σ_iΛ_i^0 < 1, which is (NC).

**For D = 3/50 no assignment-independent violation of (i)–(ii) is known.** That relies on DD1's numerics for (NC),
Conjecture 3.6, and the cross-line T∘T conjecture.

### 4.2 Splice cubes: the new transports do not break strict slack

Fix a splice segment x(λ) = x_0 + λw, λ ∈ [0,1], all of whose sub-triples are splice triples. Its **cube** consists of
the models Y_J (J a finite union of intervals): post-switch advice where λ*(h) ∈ J, pre-switch advice elsewhere. Then:
- Y_{[0,λ]} = C_{x(λ)};
- records are pairs (F, G), with forward switches on F and backward switches on G;
- T accepts (F, ∅) at worlds with w_i < 0 ("D-worlds") and (∅, G) at worlds with w_i > 0 ("U-worlds");
- caps are C_{x(ν)} ≼_i Y_J ⟺ x_i(ν) ≥ r_i(Y_J).

Write μ_i(J) for the position with x_i(μ_i) = r_i(Y_J). T-monotonicity forces μ_i(J) ∈ [ι(J), sup J], where ι(J) is the
length of J's initial segment. Strict slack is Σ_i w_i μ_i(J) < 0.

**Theorem 4.1 (discrete cube; PROVED).** Grid the cube into N cells. Start from any assignment with ι(J) < μ_i(J) < sup J
for non-initial J (the strict box). Then the closure (transports and realisable composition inside the cube) never
produces (F1), and thresholds stay in the strict box.
- *Proof.* At a D-world every generator satisfies RF: "the rightmost changed cell is switched forward".
  - Pure forward records satisfy it trivially.
  - A cap from [0, ν] has G ⊆ [0, ν) and F = J ∖ [0, ν] ∋ sup J, because ν ≤ μ_i(J) < sup J.
- RF is preserved by realisable composition. Let M be the largest forward cell of either record. M cannot be cancelled,
  since every backward cell of the other record lies left of that record's own largest forward cell.
- A wrong-way selected record [0,b] → [0,a] (a < b) is pure backward and violates RF.
- U-worlds are the mirror case: "the leftmost changed cell is switched backward". ∎

**Theorem 4.2 (continuum cube: an explicit fixed point; PROVED).**
- *The rule.* At a D-world accept (F, G) iff ∫_F ψ − ∫_G ψ ≥ 0, with ψ(λ) = 1 + θλ, θ > 0. At a U-world accept iff
  |F| − |G| ≤ 0. At a world with w_i = 0, accept all records (ties).
- *Axioms.* Each world is additive in the switch parameter, so it is a preorder with (IB) and closed sections.
- *Selected thresholds.* Pure forward records are accepted at D-worlds and pure backward ones rejected; selected
  thresholds stay r(C_x) = x.
- *Positions.* The induced positions are μ_D(J) = Ψ^{−1}(∫_J ψ) and μ_U(J) = |J|, with Ψ(t) = t + θt²/2. For
  non-initial J, μ_D(J) > |J| = μ_U(J), because J's mass sits to the right of [0, |J|].
- *Strict slack.* Σ_i r_i(Y_J) − 1 = W(μ_U − μ_D) < 0.

CHECKED on grid cubes (`cube_assignment.out`): with θ ∈ {1/2, 2}, three line types including a level line, all 64 cube
models give 0 violations. The checks are:
- r(C_x) = x;
- strict slack;
- T-monotonicity;
- monotonicity along every in-cube transport of every cap;
- the frontier rule.

By contrast, the naive rule r_i(Y_J) = x_i(|J|) − κ|w_i|·(gap) is **not** a fixed point: 170–258 cap-transport
violations. The closure would move it. So the initial assignment has real content.

*Remark (where the continuum risk is).* With the naive rule the closure can push μ_D(J) towards sup J along chains of
transported caps. Endpoint inclusion (step 4 of the brief) then installs the pure-backward cap C_{x(sup J)} ≼ Y_J. Its
transport to [0,b] → [0,a] is (F1).
- Theorem 4.2 shows a good starting assignment avoids this on a line.
- **Whether the line-wise additive structures can be chosen compatibly across the two-dimensional family of splice
  lines, the bumps and the seeds is the open core.** A single global additive density is excluded by the project's
  no-additive-cover theorems. So any successful assignment must be non-additive in how the lines are glued, while it
  may be additive along each line.

### 4.3 Which feature is responsible

- The only exact assignment-independent (F1) chains known are DD1's nine. They are caused by **the designated indices
  r(C_{q_k}) = q_k lying far from u**. They are not caused by strict slack, by thresholds as such, or by the posterior
  selection.
- r(C_p) = p is no restriction in itself: re-indexing the selection by a support-preserving homeomorphism σ of Δ gives
  another strict-slack system. What matters is *where* each credal set sits. The minimal modification is the DD1
  design, bumps inside the windows, which the D = 3/50 family already satisfies with margin ≥ 0.079.
- The new T-links impose constraints (the boxes of Prop 2.5, the level-line ties, and the strict-box requirement of
  Thm 4.1), but no forced chain.

---

## 5. Task 3: strict guidance reversal (F2)

**Proposition 5.1 (PROVED).**
- (a) **One non-guidance generator.** By Lemma 1.3, (F2) needs that generator itself to be a strict improvement.
  - For Sel or T-links that is a failure of selected-layer (G).
  - For seeds it never happens (each seed raises rank on its P_k).
  - For a cap rec(C_s, Z) it means Z is strictly i-better than C_s with s_i ≥ r_i(Z), which the lower bound
    r_i(Z) > s_i in (i) excludes.
- (b) **Through a selected model.** Suppose Y ≼_i C_s ≼_i Y′ with Y′ pointwise strictly i-better than Y. Then
  r_i(Y) ≥ s_i ≥ r_i(Y′) ≥ r_i(Y), so all three are equal.
  - So (F2) through C_s is exactly "the closure pushes r_i(Y′) down to a level at or below a strict lower bound". This
    is the strict form of the (NC) bookkeeping of §3, and the same obstruction test applies.
  - Assignment-independently, with both links from G, S and T, it occurs iff selected-layer (G) fails. A T-link C_s ≼ Z
    followed by guidance Z ≼ Y′ ≺ C_s makes the transported record R(a,b) a pointwise improvement.
- (c) **DD2's conversion cycle** (Lemma 2.10) is B_1 → X_1 → … → X_4 → B_1′ with B_1′ ≺_1 B_1. Under exact sections every
  accepted chain has non-increasing r_1, while r_1(B_1′) > (q_1)_1 = r_1(B_1). So such a chain is never accepted at a
  fixed point. That constraint is therefore automatic; it fails only if the closure moves r_1(B_1′).
- (d) **Among nonselected models.** At least two transported caps are needed (or a seed and a cap). Thresholds are
  constant around such a cycle, so they cannot detect it.
  - With a seed and a T-link: off the cells the composite is the T-record, which must then be weakly improving off a
    bounded set. By the cone principle it is weakly improving a.e., i.e. a selected-layer (G) failure.
  - So seeds plus T-links give no (F2) with two generators.
  - Inside a splice cube, records of non-guidance lines are mixed at every world, so no (F2) occurs. On guidance lines
    the RF/LB invariants exclude the only improving records.

**What is forced.** No assignment-independent (F2) was found at length ≤ 2. The risk sits with endpoint inclusion at
*tight* levels.
- The level-line ties of §2.4 make some levels tight independently of the assignment: X ∼_1 C_s.
- Every strict improvement Y′ of such an X then needs r_1(Y′) > s_1.
- To first order, assignment-independent caps cannot accumulate at s_1 for such Y′. By Prop 3.2, C_q ≥_1 Y′ > X would
  force C_q ≥_1 C_s and C_q ≥_1 C_p pointwise, which is impossible for s ≠ p on a level line.
- Caps coming from the assignment can accumulate, so the initial assignment must keep a margin there. That is a
  constraint, not an obstruction.

---

## 6. Status

| Item | Statement | Label |
|---|---|---|
| 1.1–1.3 | fixed points ⟺ monotone along generators; F1 decided by last link; one-generator F2 | PROVED |
| 2.1 | cone principle: seeds never create F1/F2 between coherent endpoints | PROVED |
| 2.2–2.3 | selected transports ⟺ splice triples; exact line/cell criterion | PROVED; CHECKED (two methods + sampling) |
| 2.3a | diagonal invariance of splice triples | PROVED |
| 2.4(a) | excluded double-sectors around edge directions | PROVED |
| 2.4(b) | all other directions splice locally | CHECKED at u (1° sweep matches prediction); CONJECTURE elsewhere |
| 2.4 cert. | T1 = C_u a splice of two patched-family members | CHECKED |
| 2.5 | forced boxes for complementary splices; level-line ties | PROVED; CHECKED |
| 3.2 | GT/TG reduce to G | PROVED (first order); CHECKED 475 instances |
| 3.4 | cap chains unavoidable ⟺ Σ Λ^0 ≥ 1 | PROVED |
| 3.5 | seeds add nothing to (NC) | PROVED |
| 3.6 | T-relaxation adds nothing to (NC) | CONJECTURE; NUMERICS 0/200 |
| DD1 certs | exactly the forced chains; D = 3/50 clears all nine windows by ≥ 0.079 | CHECKED |
| 3.7–3.10 | frontier rule, duality, partner covering, no firing for bounded F | PROVED |
| 4.1 | discrete splice cube: every strict-box start is F1-free | PROVED |
| 4.2 | continuum splice cube: additive switch densities give a strict-slack fixed point | PROVED; CHECKED |
| naive rule | not a fixed point | CHECKED |
| 5.1 | F2 classification; DD2 Lemma 2.10 automatic | PROVED |
| decisive theorem | some strict-slack assignment closes cleanly on the full domain | **open**; no obstruction at length ≤ 2 for D = 3/50; the risk is the 2-D gluing of splice lines |

## 7. Files (`ee2py/`)

- `cells.py`: exact cell enumeration of problem space for polygonal models; splice and pointwise tests; posterior
  family.
- `splice.py`: support-function splice test.
- `t_cells.py` → `t_cells.out`: agreement of the two exact tests; ratio-order sanity checks.
- `crosscheck_splice.py` → `crosscheck_splice.out`: direct random-gamble cross-check.
- `test_posterior_splice.py` → `test_posterior_splice.out`: random far triples; direction sweep at two lengths.
- `splice_cert.py` → `splice_cert.out`: certificates through u (outside bumps), forced comparisons and their
  non-guidance status, 1° sweep against the predicted sectors.
- `local_noncollinear.py` → `local_noncollinear.out`: only antiparallel local pairs are splice.
- `level_lines.py` → `level_lines.out`: level-line splice lines (ties).
- `chain_tests.py` → `chain_tests.out`: exact GT, TG, and T-relaxed (NC) searches.
- `cube_assignment.py` → `cube_assignment.out`: grid-cube fixed-point checks (naive vs additive-density rules).
- `window_margins.out`: designated indices versus DD1's nine windows.
