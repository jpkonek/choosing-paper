# JJ3 (round 38, BRIEF30, impossibility side). No protected weak-additive leading field through T1 on the full domain: the zeros either can be removed without changing any Bayes model, or they force an interior credal set onto an edge, which strict-best forbids

18 Oct 2026. Rules of BRIEF13 and BRIEF30; the corrections of AUDIT_II.md are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: none offered.

Scripts are in `jj3py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All arithmetic is
`fractions.Fraction`; the two Jacobians are computed symbolically (sympy).

Setting: three worlds, T1 = D_K with K = (1−ε)u + εΔ, any ε ∈ (0,1), c₀ := (1−ε)/3; notation of the write-up §2, FF2 and
II1 §1. No assumption is added. Every extra hypothesis below is a hypothesis of the stated result and is named there.

---

## 0. Outcome

**The impossibility theorem holds on the full four-advice domain, with exactly the hypotheses of the sufficient theorem
(II1 Thm 4.1 / II2 Cor 2.4).** It holds on every decomposable domain with (LF) at D_{T1} that has the edge-availability
property (Av) of §4. It is PROVED modulo Theorem gm and Theorem ccibu.

**Theorem 5.1 (PROVED modulo Theorem gm and Theorem ccibu).** Let M be the full domain, or any decomposable domain with
(LF) at D_{T1} satisfying (Av). There is no pair (Φ, p ↦ C_p) with these properties:
- Φ is an integrable, weakly guiding additive leading field on M;
- p ↦ C_p is a selection of coherent models, continuous in measure, with T1 = C_{q₀};
- the selection is (NT): each C_p is the only model with Φ_i ≤ Φ_i(C_p) at every i ∈ supp p.

So the protected-leading-field subclass is empty there, and II1's question P_w has the answer NO. Only this subclass is
closed. The non-(NT) tie designs (II1 §6; II2 (★), §3), other exchange-rate constructions and general non-transitive FC
covers are untouched.

**The route** (the brief's route, but in a different order). I do not re-run gm's chain for weak signs. I show instead:
- (NT) supplies all of gm's *input* (unique coherent Bayes models at every interior weight; T1 Bayes at an interior weight);
- all but one kind of zero can be deleted without changing a single Bayes model;
- the remaining kind cannot occur.

The field is then strictly guiding, and gm applies to it verbatim.

1. **(NT) gives the full Bayes structure (§2; PROVED).**
   - Theorem 2.1: for EVERY w ∈ int Δ, the w-Bayes model of Φ is a.e. unique and is a selected (coherent) model D_{K_w}.
     The proof is KKM for the leading ranking plus (NT); this replaces II1 Prop 5.3(a), which had "a.e. w".
   - w ↦ K_w is Hausdorff-continuous.
   - T1 = B_{w*} for some w* ∈ int Δ (Prop 2.5).
   - The every-weight chart identities of the write-up's Prop CF hold for weak signs (Lemma 2.4).
2. **Zero shapes (§3; PROVED, CHECKED).** After II1 Prop 5.2 (strict-best; × strictly worst), every zero is a bad~silence
   zero. On a pair, let Σ(h) be the set of weights at which silence is a weak Bayes advice.
   - Σ(h) is empty if the zero sits at the odd world, at both positive worlds, or on a unanimous pair.
   - For a single zero at a positive world j, Σ(h) either lies in the edge opposite e_j, or is a triangle with base on
     that edge. Its silence/rejection side then lies on a line through the vertex e_j (Lemma 3.1).
3. **Removal (§3; PROVED, CHECKED).** Every zero on a pair whose Σ(h) misses int Δ can be deleted: lower φ(S) by a small
   pair-dependent δ. No minimiser set changes at any weight of the closed simplex (Lemma 3.2). The only zeros that
   cannot be deleted this way are the **essential** ones: a single zero at a positive world, on a pair silenced by
   Bayes models at an open set of interior weights.
4. **Essential zeros are null (§4; PROVED on (Av) domains; inputs CHECKED).**
   - Two essential pairs that differ only in the zero-world coordinate share their rejection boundary, a line through
     e_j. This uses the edge family on the opposite edge (Lemma 4.2).
   - So the interior credal sets along that line contain a point of the opposite **edge** of Δ (Lemma 4.3).
   - That makes a non-null set of strictly-best pairs, accepted by T1, have a chart boundary on a line through e_j. Strict
     best at world j forbids this (Lemma 4.4).
5. **Conclusion (§5).**
   - With no essential zeros, the lowered field Φ′ is integrable and strictly guiding, and has the same Bayes models as Φ
     at every weight.
   - Theorem ccibu makes Φ′ a ranking with (LA), (S), (C) that covers T1 on M.
   - Theorem gm excludes that.

**What strict guidance did in gm / ccibu / the transfer proof, and what replaces it:** §6, table.

**Single most important open point.** Lemma 4.2's edge confinement on decomposable (LF) domains *without* (Av). These are
domains on which acceptance is unavailable on a non-null set of gambles positive at two worlds. There, the essential
single positive-world zeros of §3 are the only pattern not excluded; they are described exactly in §7. Within this
subclass, nothing else is open.

---

## 1. Setting, the class, and the zero vocabulary

### 1.1 The class (the hypotheses of the sufficient theorem)

**(H)**
- M is a decomposable domain with (LF) at D_{T1}, with advice ranges A(h) ⊆ {M, S, O, ×}.
- Φ = (Φ_1, Φ_2, Φ_3), Φ_i(X) = ∫ φ_i(h, a_X(h)) dμ, has measurable penalties with an integrable envelope E(h).
- Φ is weakly guiding: φ_i(h, a) ≤ φ_i(h, b) whenever a is weakly better than b in world-i rank, for a.e. h.
- p ↦ C_p ∈ M is a selection of coherent models on Δ, continuous in measure, with T1 = C_{q₀}.
- (NT) holds: for every p and every X ∈ M, if Φ_i(X) ≤ Φ_i(C_p) for every i ∈ supp p, then X = C_p a.e.

Pairs are indexed by their majority orientation h, as in FF2: a mixed h has two positive coordinates, the *positive
worlds* j, l, and one negative coordinate, the *odd world* o. A unanimous h is ≥ 0. Advices are:
- M (accept h only);
- S (silence);
- O (accept −h only);
- × (both).

World ranks, better first:
- at a positive world of a mixed h, and at every world of a unanimous h: M, S, O, ×;
- at the odd world: O, S, M, ×.

### 1.2 Two facts from II1 Prop 5.2, re-proved for an arbitrary decomposable domain

**Lemma 1.1 (PROVED; II1 Prop 5.2(a), (b), any decomposable domain).**
- **(a) Strict-best.** For a.e. h and every world k, the world-k-best advice best_k(h) in A(h) is strictly cheapest:
  φ_k(h, best_k(h)) < φ_k(h, b) for every other b ∈ A(h).
- **(b) × strictly worst.** Replacing φ_k(h, ×) by max_{a ∈ A(h)∖{×}} φ_k(h, a) + |h_k| preserves (H). After the
  replacement, every equality φ_k(h, a) = φ_k(h, b) between distinct advices of A(h) is a **bad~silence zero**:
  - φ_k(h, S) = φ_k(h, W_k) with W_k the k-wrong acceptance (O at a positive world, M at the odd world, O at every world
    of a unanimous pair);
  - this requires best_k(h), S, W_k ∈ A(h), hence {M, S, O} ⊆ A(h).

*Proof.*
- (a) The world-k-best model B^k (pointwise best_k advice; evaluable by Remark advicerange) minimises Φ_k by weak
  guidance.
  - (NT) at e_k says C_{e_k} is the only Φ_k-minimiser, so C_{e_k} = B^k.
  - If φ_k(h, b) = φ_k(h, best_k(h)) on a non-null set for some b ≠ best_k(h), switching B^k to b there gives a second
    Φ_k-minimiser.
- (b) Coherent models never give ×, so Φ(C_p) is unchanged. Φ(X) weakly increases for every X. So
  Φ′_J(X) ≤ Φ′_J(C_p) gives Φ_J(X) ≤ Φ_J(C_p), hence X = C_p. Integrability, weak guidance and continuity are
  unaffected.
  - An equality at world k involves neither best_k (by (a)) nor ×.
  - The non-best, non-× advices at world k are S and W_k.
  - If best_k ∉ A(h), the world-k ranking on A(h) starts with S or W_k, and (a) applies to it. ∎

From now on × is strictly worst. For a mixed h with positive worlds j, l and odd world o, with {M, S, O} ⊆ A(h), put

  c(h) := φ(h,S) − φ(h,M),  c′(h) := φ(h,S) − φ(h,O),  d(h) := c − c′ = φ(h,O) − φ(h,M)   (vectors over worlds).

By Lemma 1.1:
- c_j, c_l > 0 and c_o ≤ 0;
- c′_o > 0 and c′_j, c′_l ≤ 0;
- d_j, d_l > 0 > d_o.

The possible zeros are:
- **z_o**: c_o = 0;
- **z_j**: c′_j = 0;
- **z_l**: c′_l = 0.

At a weight w (writing f_a(w) := w·φ(h,a)):
- M is the unique minimiser iff c·w > 0 and d·w > 0;
- O is the unique minimiser iff c′·w > 0 and d·w < 0;
- S is a weak minimiser iff c·w ≤ 0 and c′·w ≤ 0.

× never minimises at any w ∈ Δ. Put **Σ(h) := {w ∈ Δ : S is a weak minimiser of w·φ(h,·)}**.

**Remark 1.2 (BRIEF30's elementary necessary condition; PROVED).** Let C_q be silent on a non-null set E of mixed pairs
of one type (positive worlds j, l; odd o).
- Switching S → M on E has increments −∫_E c. These are negative at j, l and nonnegative at o. So (NT) needs o ∈ supp q
  and c_o < 0 a.e. on E: there is no z_o.
- Switching S → O has increments −∫_E c′. These are negative at o and nonnegative at j, l. So (NT) needs a world of
  supp q ∩ {j, l} with c′ < 0 a.e. on E. In particular, z_j and z_l do not both occur on E.

This is the brief's condition: on the pattern (+,−,−), "reject" = M and "accept" = O.

The same switches show that no selected model is silent on a non-null set of pairs carrying z_o, both z_j and z_l, or a
zero on a unanimous pair. The removal argument of §3 does not need this.

---

## 2. What (NT) supplies: the full Bayes structure of Φ

A model B is **w-Bayes** if a_B(h) minimises w·φ(h,·) over A(h) for a.e. h. Bayes models exist: a measurable pointwise
minimiser is evaluable. The **tie set** at w is T_w := {h : the minimiser is not unique}.

**Lemma 2.2 (KKM for the leading ranking; PROVED).** Put X ≼_i Y iff Φ_i(X) ≤ Φ_i(Y). Then every model that is
undominated in (≼_1, ≼_2, ≼_3) is tied at every world with some C_p.

*Proof.*
1. **Undominated.** Every C_p is undominated, since a dominating model would violate (NT).
2. **Competitive.** For X ≠ C_p, (NT) gives some i ∈ supp p with Φ_i(X) > Φ_i(C_p).
3. **Closed sets.** F_i(X) := {p : Φ_i(C_p) ≤ Φ_i(X)} is closed: |Φ_i(C_p) − Φ_i(C_q)| ≤ 2∫_{C_p ≠ C_q} E dμ, which
   tends to 0 as q → p by continuity in measure and absolute continuity of the integral.
4. **KKM.** For every face Δ_S, each p ∈ Δ_S lies in F_i(X) for some i ∈ supp p ⊆ S. So the KKM lemma gives
   p ∈ F_1(X) ∩ F_2(X) ∩ F_3(X).
5. **Conclusion.** If X is undominated, none of the comparisons C_p ≼_i X is strict, so X is tied with C_p. (This is the
   write-up's Theorem kkm.) ∎

**Theorem 2.1 (PROVED).** Assume (H). For every w ∈ int Δ:
- the tie set T_w is null;
- the w-Bayes model B_w is a.e. unique;
- B_w is a selected model, so B_w = D_{K_w} for a credal set K_w.

*Proof.*
1. **Every w-Bayes model is selected.** Let B be w-Bayes.
   - If Y dominated B, then w·Φ(Y) < w·Φ(B), since w has full support. So B is undominated.
   - By Lemma 2.2, Φ(B) = Φ(C_p) for some p, so Φ_i(B) ≤ Φ_i(C_p) on supp p.
   - (NT) gives B = C_p a.e. In particular B is coherent.
2. **Uniqueness.** Suppose T_w is non-null.
   - Measurable pointwise minimisers B_1, B_2 can be chosen to differ on T_w. Both are coherent by step 1:
     B_r = D_{K_r} a.e.
   - The difference set G := {h : a_{D_{K_1}}(h) ≠ a_{D_{K_2}}(h)} is a non-null cone.
   - Let A := {‖h‖ < 1}, a symmetric set. The splice X := (B_1 ∩ A) ∪ (B_2 ∖ A) is again a pointwise minimiser, so it is
     coherent: X = D_K a.e.
   - For a.e. (h, t) with h ∈ G ∩ A and t > 1/‖h‖, the advice of D_K at h equals its advice at th. That is B_1's advice
     at h and B_2's advice at th, i.e. at h. These differ on G.
   - This is a set of (h, t) of positive measure, and a null modification of a cone is invisible to a.e. (h, t) by
     Fubini. So we have a contradiction. ∎

**Lemma 2.3 (PROVED).**
- (a) w ↦ K_w is Hausdorff-continuous on int Δ, and P(w, g) := min_{m∈K_w} m·g is jointly continuous, with
  |P(w,g) − P(w′,g)| ≤ ‖g‖ d_H(K_w, K_{w′}).
- (b) Let w₀ ∈ ∂Δ be such that w₀·φ(h,·) has a unique minimiser for a.e. h. Then K_w converges, as w → w₀ through
  int Δ, to a credal set K(w₀), and the w₀-minimiser model equals D_{K(w₀)} a.e.

*Proof.*
- (a) Let w_n → w. Off the null set T_w the strict minimiser at w stays the strict minimiser at w_n for large n, so
  B_{w_n} → B_w in measure.
  - Let K′ be any Hausdorff cluster point of (K_{w_n}). Then P_{K_{w_n}}(g) → P_{K′}(g) for every g, so
    D_{K_{w_n}} → D_{K′} in measure, off the null set ±∂D_{K′}.
  - Hence D_{K′} = D_{K_w} a.e., so K′ = K_w (injectivity of K ↦ D_K, write-up §2).
  - The Lipschitz bound is immediate.
- (b) The same argument with w replaced by w₀ and B_w by the w₀-minimiser model. ∎

For a gamble x, let R(x) ⊆ int Δ be the set of interior weights at which "accept x and not −x" is the unique minimiser,
at the pair of x. It is an intersection of finitely many open half-planes of aff Δ with int Δ, possibly empty. Weak
signs do not matter here.

**Lemma 2.4 (charts at every weight; PROVED).**
- (a) For **every** gamble x and every c ∈ ℝ, the sets {w ∈ int Δ : P(w,x) > c} and {w ∈ int Δ : P(w,x) ≥ c} are
  convex.
- (b) For a.e. x: R(x) = {w ∈ int Δ : P(w,x) > 0} exactly, and the zero set Z(x) := {w ∈ int Δ : P(w,x) = 0} is
  Lebesgue-null.
- (c) For a.e. x with R(x) ≠ ∅: {w ∈ int Δ : P(w,x) ≥ 0} ⊆ cl R(x). Consequently Z(x) lies in the relative boundary of
  R(x) in int Δ, which is contained in the finitely many lines {w : w·(φ(x,b) − φ(x,acc)) = 0}, b ∈ A(x) ∖ {acc}, where
  acc is the advice "accept x".

*Proof.*
- **(a)** Replacing x by x − c𝟙 reduces to c = 0. Let P(q_1,x), P(q_2,x) > 0 and q ∈ [q_1, q_2].
  - P(q_r, ·) is 1-Lipschitz in sup norm, so P(q_r, x″) > 0 on a sup-norm ball U around x.
  - For each fixed interior q′, B_{q′} = D_{K_{q′}} a.e. and T_{q′} is null. So for a.e. x″,
    q′ ∈ R(x″) ⟺ P(q′, x″) > 0.
  - Apply this at q_1, q_2 and q. For a.e. x″ ∈ U, q_1, q_2 ∈ R(x″), hence q ∈ R(x″) (convexity), hence P(q, x″) > 0.
  - By continuity P(q, ·) ≥ 0 on U. Then P(q, x) = P(q, x − t𝟙) + t ≥ t for small t > 0.
  - The "≥" sets are intersections of "> c − 1/n" sets.
- **(b)** The sets {(w, x) : 1[w ∈ R(x)] ≠ 1[P(w,x) > 0]} and {(w, x) : P(w,x) = 0} are jointly measurable.
  - For each w their x-sections are null: the first by Theorem 2.1; the second because P(w, ·) is concave and
    P(w, x + t𝟙) = P(w,x) + t, so its zero set is a graph over 𝟙^⊥.
  - Fubini: for a.e. x both w-sections are null.
  - R(x) and {P(·,x) > 0} are then open convex sets (by (a) and Lemma 2.3(a)) that agree a.e. Open convex sets that agree
    a.e. are equal: each lies in the closure of the other, and int cl O = O for open convex O.
- **(c)** Put C := {P(·,x) ≥ 0} (convex) and O := R(x) (open convex, nonempty). Suppose z ∈ C ∖ cl O.
  - Some ball V around z misses cl O.
  - For small s > 0 and a ball B ⊆ O, the set (1−s)z + sB is open, lies in V ∩ C ∖ O, and P = 0 on it.
  - This contradicts (b).
  - A point of cl O ∖ O inside int Δ satisfies one of the defining strict inequalities of R(x) with equality. ∎

**Proposition 2.5 (PROVED).** T1 = B_{w*} for some w* ∈ int Δ.

*Proof.*
1. **A weak Bayes weight exists.** II1 Prop 3.1(a) (FF2 Step 1; Lyapunov convexity and separation; competitiveness of
   C_{q₀} in the leading ranking, which (NT) gives) yields α ∈ Δ_{supp q₀} at which T1 is a pointwise weak α-Bayes model.
2. **α is interior.** Suppose α_3 = 0 (the other faces are symmetric).
   - Gambles near (1, 1, −t) with t slightly above 2c₀/(c₀+ε) form an open set O′ outside cl D_{T1} (FF2 Step 5).
     T1 is silent there.
   - Taking O′ inside the (LF) neighbourhood N, the model D_{T1} ∪ O′ is evaluable. So acceptance lies in A(h) for a.e.
     h ∈ O′.
   - There, α·(φ(h,S) − φ(h,M)) = α_1c_1 + α_2c_2 > 0 by Lemma 1.1(a), for every α ∈ Δ_{12}, vertices included. So T1 is
     not weak α-Bayes.
3. **Conclusion.** α ∈ int Δ. Theorem 2.1 gives T1 = B_α. ∎

*Remark (the brief's suggested certificate is not needed).* The brief proposed: Pareto-uniqueness, then Bayes optimality
at some weight with the same support. This is not used.
- Uniqueness at *every* interior weight comes from KKM (Theorem 2.1).
- The interiority of T1's weight comes from strict-best and (LF).
- For general compact convex attainable sets, Pareto-uniqueness alone need not give a supporting weight with full support
  (a disc tangent to an axis at 0). I make no claim either way about the Lyapunov sets here.

---

## 3. Zero shapes, and removal of every zero that no interior Bayes model sees

**Lemma 3.1 (PROVED; CHECKED, `sregion.py`).** Let h carry at least one zero, with {M, S, O} ⊆ A(h).
- (a) If h is unanimous, or carries z_o, or carries both z_j and z_l, then Σ(h) = ∅ (on the closed simplex).
- (b) Suppose h carries exactly one zero, z_j, at a positive world j; l is the other positive world and o the odd world.
  Then exactly one of the following holds.
  - (b1) Σ(h) ⊆ {w_j = 0}.
  - (b2) Σ(h) is a nondegenerate triangle with vertices m_h, s_h on the open edge (e_l, e_o) and t_h ∈ int Δ, where
    m_h is strictly closer to e_l than s_h. Its side [t_h, s_h] lies on the line L_h := {c′·w = 0}, which passes through
    e_j. Its side [t_h, m_h] lies on {c·w = 0}.

    Write σ_h := (t_h, s_h) (open segment) = {w ∈ int Δ : c′·w = 0, c·w < 0}. For w on the edge (e_l, e_o) near s_h,
    the unique minimiser is S on the side of e_l and O on the side of e_o.

*Proof.* Throughout, × never minimises.
- **(a), unanimous.** M is strictly cheapest at every world, so f_M < f_S on Δ.
- **(a), z_o.** c = (c_j, c_l, 0) with c_j, c_l > 0. So {c·w ≤ 0} ∩ Δ = {e_o}, and c′·e_o = c′_o > 0.
- **(a), z_j and z_l.** c′ = (0, 0, c′_o). So {c′·w ≤ 0} ∩ Δ is the edge {w_o = 0}, where c·w = c_jw_j + c_lw_l > 0.
- **(b), the S-side of the c-line.** Now c_o < 0 < c_j, c_l, so the line {c·w = 0} separates e_o from e_j and e_l.
  Then {c ≤ 0} ∩ Δ = co{e_o, a, b} with a ∈ (e_j, e_o) and b ∈ (e_l, e_o).
- **(b), the S-side of L_h.** c′ = (0, c′_l, c′_o) with c′_l < 0 < c′_o. So L_h passes through e_j and meets (e_l, e_o)
  at the point s_h with o-coordinate |c′_l|/(|c′_l| + c′_o). The side {c′ ≤ 0} contains e_l.
- **(b), the intersection.** c′·a = c′_oa_o > 0 and c′·e_o > 0, so only b can lie on the S-side.
  - If c′·b > 0, then Σ = ∅.
  - If c′·b = 0, then Σ = {b} ⊆ {w_j = 0}.
  - If c′·b < 0, then Σ is the triangle with vertices b =: m_h, the point s_h of L_h on [b, e_o], and the point t_h of
    L_h on [a, b], which is interior because a and b are on open edges.
- **The last sentence of (b).** On the edge, c·w < 0 strictly beyond m_h, and c′·w changes sign at s_h. ∎

CHECKED (`sregion.py` → `sregion.out`): 6000 random exact pair configurations over all orderings of (j, l, o), with every
zero pattern.
- (a): 3801 cases, Σ = ∅ in each.
- (b2): 718 cases, each a triangle with two vertices on {w_j = 0}, e_j, t_h and s_h collinear on {c′ = 0}, and
  m_h closer to e_l.
- (b1): 755 cases, Σ ⊆ {w_j = 0}.
- 0 failures.

**Definition.** A pair is **essential** if it is in case (b2), i.e. Σ(h) ∩ int Δ ≠ ∅. Then its only zero is a single
positive-world zero. Let **E^{j}_{l,o}** be the set of essential pairs with zero world j, other positive world l and odd
world o (six sets), and let E be their union.

**Lemma 3.2 (removal; PROVED; CHECKED, `removal.py`).** Let h carry zeros at the worlds Z(h) and be non-essential. There
is δ(h) > 0, measurable in h and at most half of every gap φ_i(h,S) − φ_i(h, best_i(h)) with i ∈ Z(h), with this
property: lowering φ_i(h,S) by δ(h) for each i ∈ Z(h)
- makes the penalties at h strictly increasing in world rank at every world;
- leaves the set of minimisers of w·φ(h,·) unchanged for **every** w ∈ Δ.

*Proof.*
1. **The function G.** Put G(w) := min(f_M, f_O)(w) − f_S(w). S is a weak minimiser iff G ≥ 0. The perturbed function is
   G_δ = G + δσ_Z, with σ_Z(w) := Σ_{i∈Z} w_i, and f_M, f_O, f_× are unchanged.
2. **Zeros of G.** Non-essential means G < 0 on int Δ, so G ≤ 0 on Δ by continuity. By Lemma 3.1, G can vanish only
   where σ_Z = 0.
   - In case (a), G < 0 on all of Δ.
   - In case (b1), G vanishes only on {w_j = 0} (Σ(h) ⊆ {w_j = 0}), and Z = {j}.
3. **Choice of δ.** G is affine on each of the two closed cells {f_M ≤ f_O} ∩ Δ and {f_O ≤ f_M} ∩ Δ, which are convex
   polygons. Let V be their finitely many vertices, rational functions of φ(h,·).
   - Put 2δ := min{−G(v)/σ_Z(v) : v ∈ V, σ_Z(v) > 0}, capped by the gaps.
   - Then G + 2δσ_Z ≤ 0 at every vertex, hence on each cell, hence on Δ.
4. **Minimiser sets are unchanged.**
   - Where σ_Z(w) > 0: G_δ(w) ≤ −δσ_Z(w) < 0, so S is not a minimiser before or after.
   - Where σ_Z(w) = 0: nothing changed.
5. **Strictness.** The order at i ∈ Z becomes best_i < S < W_i < ×. ∎

CHECKED (`removal.py` → `removal.out`): 3000 random exact instances.
- Every removable pattern: 2575 cases. The perturbed penalties are strictly guiding, and the minimiser sets are identical
  at all 325 points of the denominator-24 grid of the closed simplex and at every cell vertex.
- The 425 essential instances all carry a single positive-world zero.
- 0 failures.

**Proposition 3.3 (PROVED).** Assume (H) and μ(E) = 0. Let Φ′ be Φ with φ_i(h,S) lowered by δ(h) at every zero (Lemma
3.2, on the co-null set of non-essential pairs). Then:
- Φ′ is additive with an integrable envelope (δ ≤ E);
- Φ′ is strictly guiding a.e.;
- for every w ∈ Δ, the w-Bayes models of Φ′ and of Φ coincide.

In particular, for every w ∈ int Δ the w-Bayes model of Φ′ is a.e. unique and coherent (Theorem 2.1), and
T1 = B′_{w*} with w* ∈ int Δ (Prop 2.5). ∎

---

## 4. Essential zeros do not occur

**(Av_{l,o})**: for a.e. gamble g with g_l > 0 and g_o > 0, acceptance of g lies in A(g). **(Av)** means (Av_{l,o}) for
all two-element sets {l, o}. The full domain has (Av).

Fix (j; l, o) and write coordinates in the order (j, l, o). For h ∈ E^{j}_{l,o}, put:
- λ := h_l + |h_o|;
- π := π(h) := h_l/λ ∈ (0,1);
- ρ := h_j/λ > 0.

So h = λ h̄, with h̄ = h̄(ρ, π) := (ρ, π, −(1−π)). Let P_π := (0, 1−π, π) be the point of the edge Δ_{lo} with o-coordinate
π, so that P_π·h̄(ρ, π) = 0 for every ρ. The map (π, ρ, λ) ↦ h is a diffeomorphism onto {h_j > 0, h_l > 0, h_o < 0}
with Jacobian λ² (CHECKED symbolically, `t1_accept.py`), so null sets correspond.

**Lemma 4.2 (the edge family; PROVED).** Assume (H) and (Av_{l,o}). Parametrise the edge by w₀(t) := (0, 1−t, t). Then
for a.e. t ∈ (0,1):
- the w₀(t)-minimiser is a.e. unique;
- it equals D_{K₀(t)} a.e., with K₀(t) = Lemma 2.3(b)'s limit;
- K₀(t) = {(0, 1−x, x) : x ∈ [α(t), β(t)]} ⊆ Δ_{lo}.

Moreover, for a.e. h ∈ E^{j}_{l,o}, the point s_h of Lemma 3.1(b2) depends only on π(h). Precisely, there is a full-measure
set G_C such that s_h = s_{h′} whenever h, h′ ∈ E^{j}_{l,o} ∩ G_C and π(h) = π(h′).

*Proof.*
1. **Uniqueness at a.e. edge weight.** For each pair, the minimiser of w₀(t)·φ(h,·) fails to be unique only at
   finitely many t. Two advices a ≠ b that could both be minimisers are never blind on the edge (φ_l, φ_o equal):
   - if l, o are both positive for h, or h is unanimous, M is strictly best at l and o (Lemma 1.1(a));
   - if exactly one of l, o is positive for h, then M differs from S and from O at the positive one, S differs from O at
     the odd one, and × is strictly worst.

   Tonelli gives a null tie set for a.e. t.
2. **The edge credal sets.** Lemma 2.3(b) gives the minimiser D_{K₀(t)}.
3. **Confinement.** D_{K₀(t)} accepts a.e. g with g_l, g_o > 0, by (Av_{l,o}) and since M is then the strict minimiser
   at a weight supported on {l, o}.
   - If m ∈ K₀(t) had m_j > 0, the open set of g near (−N, 1, 1) with N > (m_l + m_o)/m_j would have P_{K₀(t)}(g) < 0.
   - So K₀(t) ⊆ Δ_{lo}.
4. **The advice of D_{K₀(t)} on h.** For m = (0, 1−x, x), m·h̄ = π − x. So D_{K₀(t)} gives O on h iff α(t) > π(h).
5. **The pair's own edge advice.** Let h ∈ E^{j}_{l,o}. By Lemma 3.1(b2) its unique edge minimiser on (m_h, 1) is S on
   (m_h, s_h) and O on (s_h, 1). The map (t, h) ↦ [pair advice at w₀(t) ≠ advice of D_{K₀(t)}] is jointly measurable,
   with null h-sections for a.e. t. By Fubini there is a full-measure G_C on which, for a.e. t, the two advices agree.
6. **Conclusion.** For h, h′ ∈ E^{j}_{l,o} ∩ G_C with π(h) = π(h′) = π₀ and t₀ := max(m_h, m_{h′}):
   (s_h, 1) ∩ (t₀, 1) =_{a.e.} {t > t₀ : α(t) > π₀} =_{a.e.} (s_{h′}, 1) ∩ (t₀, 1).

   Since s_h, s_{h′} > t₀, it follows that s_h = s_{h′}. ∎

**Lemma 4.3 (edge touching; PROVED; algebra CHECKED, `edge_touch.py`).** Assume (H) and (Av_{l,o}), and let
h_1 = λ_1h̄(ρ_1, π₀) and h_2 = λ_2h̄(ρ_2, π₀) be in E^{j}_{l,o} ∩ G_C ∩ G_B, with ρ_1 < ρ_2. Here G_B is the full-measure
set of h for which Lemma 2.4(b) holds for the gamble −h. Then:
- there is a nondegenerate open segment σ ⊆ int Δ, on the line L through e_j and s := s_{h_1} = s_{h_2}, such that
  P_{π₀} ∈ K_w and K_w ⊆ {m : m·h̄(ρ_1, π₀) ≤ 0} for every w ∈ σ;
- consequently, for every a > 0, the gamble y(a) := (a, −π₀, 1−π₀) satisfies P(w, y(a)) = 0 for every w ∈ σ.

*Proof.*
1. **The common segment.**
   - By Lemma 4.2, L_{h_1} = L_{h_2} = L.
   - By Lemma 3.1(b2), σ_{h_r} is the open segment of L from t_{h_r} to s.
   - Put σ := σ_{h_1} ∩ σ_{h_2}, the open segment of L from the later of t_{h_1}, t_{h_2} to s; it is nonempty.
2. **The rejection boundary.** Fix w ∈ σ and r ∈ {1, 2}.
   - c′(h_r)·w = 0, so w ∉ R(−h_r) and P(w, −h_r) ≤ 0, by Lemma 2.4(b) for −h_r.
   - Points w′ near w with c′·w′ > 0 still have c·w′ < 0, hence d·w′ < 0. So w′ ∈ R(−h_r) and P(w′, −h_r) > 0.
   - By continuity P(w, −h_r) = 0, i.e. max_{m∈K_w} m·h̄(ρ_r, π₀) = 0.
3. **Edge touching.** Put f(x) := max_{m∈K_w}(m_jx + m_lπ₀ − m_o(1−π₀)). It is convex and nondecreasing (m_j ≥ 0), with
   f(ρ_1) = f(ρ_2) = 0.
   - So f ≡ 0 on [ρ_1, ρ_2], and its right derivative at ρ_1, which is max{m_j : m ∈ argmax at ρ_1} (Danskin), is 0.
   - A maximiser m* exists. It has m*_j = 0 and m*·h̄(ρ_1, π₀) = 0, so m* = P_{π₀}.
4. **The gamble y(a).** For m ∈ K_w, m·h̄(ρ_1, π₀) ≤ 0 gives
   m·y(a) = m_ja − (m_lπ₀ − m_o(1−π₀)) ≥ m_j(a + ρ_1) ≥ 0.
   Also P_{π₀}·y(a) = 0. So P(w, y(a)) = 0. ∎

CHECKED (`edge_touch.py` → `edge_touch.out`):
- 4000 random exact polytopes through P_π inside {m·h̄_2 ≤ 0}: max m·h̄_1 = max m·h̄_2 = 0, and min m·y(a) = 0 at four
  values of a, with the bound m·y(a) ≥ m_j(a + ρ_1).
- 4000 edge-free controls: f(ρ_2) − f(ρ_1) ≥ (ρ_2 − ρ_1) min{m_j : argmax} > 0.
- The identities P·y = P·h̄ = 0.
- 0 failures.

**Lemma 4.4 (PROVED; input CHECKED, `t1_accept.py`).** Let a > 1 + ε/c₀ and 0 < π₀ < 1, and let y(a) be placed with
coordinates (j, l, o) as above. Then P_{T1}(y(a)) > 0: T1 accepts y(a).

*Proof.* The vertices of T1 are v_k = c₀𝟙 + εe_k, and v_k·y(a) = c₀(a + 1 − 2π₀) + εy(a)_k. The minimum over k is at least
c₀(a − 1) − ε > 0. ∎

CHECKED: 5616 exact cases (six values of ε, all orderings, 39 values of π₀, four values of a), 0 failures.

**Theorem 4.1 (PROVED).** Assume (H) and (Av_{l,o}). Then μ(E^{j}_{l,o}) = 0.

*Proof.* Suppose μ(E^{j}_{l,o}) > 0.

**Step 1 (two essential pairs per ratio).**
- E^{j}_{l,o} ∩ G_C ∩ G_B has positive measure. In the coordinates (π, ρ, λ), Fubini gives a set Π ⊆ (0,1) of positive
  length such that, for π₀ ∈ Π, the (ρ, λ)-section has positive area.
- A set of positive area is not contained in a line {ρ = const}. So for each π₀ ∈ Π there are h_1, h_2 as in Lemma 4.3.
- Let σ(π₀) be the segment it provides, on the line L(π₀) through e_j.

**Step 2 (a non-null family of auxiliary gambles).** Let A₀ := 1 + ε/c₀ and
Y := {λ(a, −π₀, 1−π₀) : π₀ ∈ Π, a > A₀, λ > 0} (coordinates (j, l, o)). The map (π₀, a, λ) ↦ λ(a, −π₀, 1−π₀) has Jacobian
of absolute value λ² (CHECKED, `t1_accept.py`), so Y is non-null. By Lemma 4.3 and homogeneity, P(w, y) = 0 for every
y ∈ Y with parameter π₀ and every w ∈ σ(π₀).

**Step 3 (a good auxiliary gamble).** Choose y ∈ Y, with parameter π₀, outside the null exceptional sets of
Lemma 2.4(b)–(c) and of Lemma 1.1(a) for the pair of y, and with a_{T1}(y) = M. This last holds for a.e. y ∈ Y: T1
accepts y (Lemma 4.4) and T1 ∈ M. Then:
- acceptance M lies in A(y), and P(w*, y) = P_{T1}(y) > 0, so w* ∈ R(y) ≠ ∅;
- y has positive worlds j, o and odd world l, so best_j(y) = M, and strict-best gives
  φ_j(y, b) − φ_j(y, M) > 0 for every b ∈ A(y) ∖ {M}.

So none of the lines ℓ_b := {w : w·(φ(y,b) − φ(y,M)) = 0} passes through e_j. Those whose normal is a multiple of 𝟙 are
empty, because the constant is then positive.

**Step 4 (contradiction).** By Step 2, σ(π₀) ⊆ Z(y). By Lemma 2.4(c), σ(π₀) is covered by the finitely many lines ℓ_b.
- A nondegenerate segment covered by finitely many lines shares two points with one of them, ℓ_b say.
- Then ℓ_b = L(π₀) ∋ e_j, against Step 3. ∎

*Reading.*
- An essential zero at world j makes the rejection boundary of its pair a line through e_j. That is possible only because
  the pair's own penalty is blind at j between silence and rejection.
- Two such pairs differing only in their j-stake must share the line, by the edge family. Then the interior credal sets
  along it reach the opposite edge.
- But then *every* gamble y(a) (positive at j and o, negative at l, on the ratio π₀) is exactly at the acceptance
  boundary along that line.
- For y(a) the leading field is strictly signed at j, because M is j-best. So its acceptance boundary cannot run through
  e_j.
- The zero that made the configuration possible is at the pair h. The contradiction is at the different pairs y(a),
  where no zero is allowed at j.

---

## 5. The main theorem

**Theorem 5.1 (PROVED modulo Theorem gm and Theorem ccibu).** On the full domain, and on every decomposable domain with
(LF) at D_{T1} satisfying (Av), no (Φ, p ↦ C_p) satisfies (H).

*Proof.*
1. **Strictly guiding Φ′.** Assume (H). By Lemma 1.1(b), × is WLOG strictly worst. By Theorem 4.1, μ(E) = 0. By Prop 3.3,
   Φ′ is an integrable strictly guiding additive field on M whose w-Bayes model, for every w ∈ int Δ, is a.e. unique and
   coherent, with T1 = B′_{w*}, w* ∈ int Δ.
2. **Φ′ is a cover.**
   - Theorem ccibu (write-up §4; CCIBU.tex; author-checked, no formal referee report) gives (LA), (S), (C) for the
     additive ranking Φ′, and makes every undominated model coherent.
   - T1, an interior Bayes model, is undominated, so T1 ∈ C_{Φ′}.
   - (LF) at D_{T1} is a property of M.
   - (G) and (IB) hold for strictly guiding additive rankings.
3. **Contradiction.** So Φ′ covers T1, which Theorem gm excludes: three routes I1, I2, C2, each refereed once (write-up
   §6). ∎

**Corollary 5.2 (same status).**
- II1 Theorem 4.1 and II2 Corollary 2.4 have no instance on the full domain, nor on any (LF) domain with (Av).
- II1's P_w has the answer NO.
- In the exchange-rate class of BRIEF29, every cover of T1 (if any), on such domains, comes from a base whose selection is
  **not** leading-level protected, i.e. a tie design of II1 §6 / II2 (★).

**Remark 5.3 (what of (NT) is used; PROVED).** (NT) enters only through three properties:
- (i) the leading ranking with the selection satisfies (LA) and (S): each C_p is undominated and competitive on supp p,
  with closed sections;
- (ii) a model tied with some C_p at all three worlds equals C_p;
- (iii) C_{e_k} is the unique minimiser of Φ_k for each k.

Lemma 1.1, Lemma 2.2, Theorem 2.1 and Prop 2.5 use only (i)–(iii) (for Prop 2.5, competitiveness), and §§3–4 use only
their conclusions. So Theorem 5.1 also excludes every integrable weakly guiding additive Φ with a coherent selection,
continuous in measure, through T1, satisfying (i)–(iii). Lemma 1.1(b) needs care here: raising φ(×) preserves (i)–(iii)
because coherent models never give ×. I state this class only as a by-product. It is not claimed to contain any tie
design of interest.

**Scope (BRIEF30, correction 6).** The theorem closes exactly the protected-leading-field subclass on these domains. It
says nothing about:
- rate systems whose selection is not (NT): the tie designs, where II2's (★) and II1 Cor 3.4–3.6 are the known
  constraints;
- other exchange-rate rules;
- general non-transitive FC covers;
- decomposable (LF) domains violating (Av) (§7).

---

## 6. Where strict guidance entered gm, ccibu and the transfer theorem, and what replaces it

| Place | What strict guidance did there | Substitute here |
|---|---|---|
| Prop necessary(a) (via (C), R1 Lemma 1.4); INTERSECTIONS Steps 3–4 | interior Bayes models unique and coherent at every interior weight | Theorem 2.1: KKM for the leading ranking + (NT) (ties with selected models trivial); the splice argument needs no guidance |
| R1 Prop 3.1 / Prop reduction(b) | Hausdorff continuity of K_q from null tie sets | Lemma 2.3: tie sets null at every interior w by Theorem 2.1 |
| Prop CF (every-q form); Lemma quasiconcave | charts equal to {P > 0} at every q; convex superlevel sets | Lemma 2.4: only convexity of charts is used, and it holds for weak signs |
| FF2 Step 5; INTERSECTIONS Step 6 ("w is interior") | accepting a two-positive gamble strictly better than silence at both positive worlds | strict-best (Lemma 1.1(a)), from (NT) at the vertices; with (LF) for availability (Prop 2.5) |
| FF2 Step 4 / (γ) | Fubini over lines of ties | not needed (Theorem 2.1 is stronger) |
| gm chain (TS, PC, NS, box, corner equation, collars; "strict badness" c_i < 0 where g_i < 0) | sign of chart vectors at bad coordinates, including vertex signs at crossings | **not re-run.** Zeros = failures of strict badness; non-essential ones are deleted without changing any Bayes model (Lemma 3.2), and essential ones do not exist (Theorem 4.1); gm is then applied to the strictly guiding Φ′ |
| ccibu (vertex and edge weights: unique and directional minimisers) | strict guidance at boundary weights | applied to Φ′, which is strictly guiding |
| FF2 Thm 4.1 Step 6 (D1 → BB2 Thm 6.1 → M3.7/M3.8) | the field contradiction for strictly guiding fields | not used at all; Theorem gm is the contradiction (II1 Prop 5.3's suggestion to extend Step 6 is bypassed) |

The brief's guess was that the danger lies in Bayes models that are "silent or wrong indifferently" on the zero set. That
is right in one sense, and the case analysis is exact.
- At interior weights, a zero on a pair *never* produces a Bayes tie: the tie set is null at every interior w.
- A zero at the odd world, at both positive worlds, or on a unanimous pair cannot even make silence a weak Bayes advice.
- A single positive-world zero can. It then tilts the rejection boundary onto a vertex line, and §4 shows this tilt is
  incompatible with strict-best elsewhere.

Remark 1.2 is consistent with this: selected models are never silent on the zero types in (a), and an essential zero sits
exactly where a selected model with full support may be silent.

---

## 7. What is left inside the subclass: domains without (Av)

On a decomposable (LF) domain violating (Av_{l,o}), only Lemma 4.2's confinement step can fail. Its other steps, and
Lemmas 1.1, 2.2–2.5, 3.1–3.3, 4.3's steps 2–4 and 4.4, hold on every such domain.

(Av_{l,o}) is equivalent to K₀(t) ⊆ Δ_{lo} for a.e. t, given the rest of Lemma 4.2.

**Precise residual (PROVED reduction).** Assume (H) on a decomposable domain with (LF). If Φ exists, then:
- for some (j; l, o), μ(E^{j}_{l,o}) > 0 and (Av_{l,o}) fails;
- every zero outside E is removable (Lemma 3.2);
- every essential pair h ∈ E^{j}_{l,o} has:
  - {M, S, O} ⊆ A(h), a single zero φ_j(S) = φ_j(O), and no zero at l or o;
  - a silence region Σ(h) that is a triangle with base on the edge (e_l, e_o) and rejection side on a line through e_j;
- the edge Bayes sets K₀(t) on that edge are not confined to Δ_{lo} on a set of t of positive length;
- (equivalently) acceptance is unavailable on a non-null set of gambles positive at l and o. This includes gambles
  (−N, 1, 1)-like in direction, beyond the reach of T1 and of the (LF) neighbourhood.

The obstruction to finishing is concrete. Without confinement, two essential pairs on one ratio π₀ have rejection lines
L(ρ) through e_j that may rotate monotonically with ρ:
- s(ρ) is nondecreasing, since the O-sets {t : max_{K₀(t)} m·h̄(ρ) < 0} decrease in ρ;
- the convexity argument of Lemma 4.3 needs two of them to coincide.

No CONJECTURE is offered for this residual.

*Note on the full domain.* (Av) is automatic there, so nothing is left within the subclass on the full domain, modulo the
imports.

---

## 8. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | strict-best; × strictly worst WLOG; zeros are bad~silence zeros on pairs with {M,S,O} ⊆ A(h), any decomposable domain | PROVED (II1 5.2(a)(b), re-proved) |
| 1.2 | BRIEF30's elementary condition: no odd-world zero, and not both positive-world zeros, where a selected model is silent | PROVED |
| 2.2 | KKM for the leading ranking under (NT) | PROVED (KKM lemma) |
| **2.1** | **every interior w: tie set null, Bayes model unique and selected** | **PROVED** |
| 2.3 | Hausdorff continuity; edge limits at weights with unique minimisers | PROVED |
| 2.4 | quasi-concavity for every gamble; every-weight charts; zero sets in chart boundary lines | PROVED |
| 2.5 | T1 = B_{w*}, w* interior | PROVED (imports II1 Prop 3.1(a) = FF2 Step 1) |
| 3.1 | shapes of the silence region by zero pattern | PROVED; CHECKED (`sregion.py`, 6000 cases) |
| **3.2** | **non-essential zeros removable with all minimiser sets unchanged on the closed simplex** | **PROVED; CHECKED (`removal.py`, 3000 cases)** |
| 3.3 | no essential zeros ⇒ strictly guiding Φ′ with the same Bayes models | PROVED |
| 4.2 | edge family on (e_l,e_o) confined to the edge under (Av_{l,o}); s_h a function of π(h) | PROVED |
| **4.3** | **two essential pairs on one ratio ⇒ interior K_w contain an edge point along a segment of a vertex line** | **PROVED; algebra CHECKED (`edge_touch.py`)** |
| 4.4 | T1 accepts y(a) for a > 1 + ε/c₀ | PROVED; CHECKED (`t1_accept.py`, 5616 cases) |
| **4.1** | **essential zero sets are null under (Av)** | **PROVED** |
| **5.1** | **no protected weak-additive leading field through T1 on the full domain, or on (LF) domains with (Av)** | **PROVED modulo Theorem gm (each route refereed once) and Theorem ccibu (author-checked)** |
| 5.2 | II1 Thm 4.1 / II2 Cor 2.4 vacuous there; P_w answered NO | same status |
| 5.3 | same conclusion under (i)–(iii) in place of (NT) | same status |
| §7 | residual on (LF) domains without (Av): essential single positive-world zeros with unconfined opposite edge | PROVED reduction; open |
| — | non-(NT) tie designs, other rate rules, general FC covers | **untouched** |

**Referee priorities.**
1. **Lemma 4.2 step 5 and step 6.** The Fubini identification of each essential pair's edge switch point with the edge
   family, and the conclusion s_h = s_{h′}. This is the only place where (Av) enters.
2. **Lemma 4.3 step 2.** That P(·, −h) vanishes on the open rejection segment uses Lemma 2.4(b) for −h and the strict
   inequality c·w < 0 on σ_h, so that nearby points with c′ > 0 are in the O-chart.
3. **Theorem 4.1 Step 3.** The good y must be chosen outside three null sets simultaneously, and inside the T1-accepted
   part of Y; and Lemma 2.4(c)'s lines must exclude e_j.
4. **Theorem 2.1 step 1.** That (NT) turns a three-world tie into equality: Φ(B) = Φ(C_p) gives Φ_i(B) ≤ Φ_i(C_p) on
   supp p.
5. **Lemma 3.2.** That zeros of G occur only where σ_Z = 0 (Lemma 3.1), so the vertex bound is finite and positive.
6. **The use of ccibu.** As in the write-up's INTERSECTIONS transfer theorem, the contradiction passes through
   ccibu → cover → gm. A referee who prefers to avoid ccibu needs a direct (S) for Φ′. I did not find one: the
   original selection need not be (NT) for Φ′, because edge-weighted selected models may be silent on lowered pairs.

## 9. Files (`jj3py/`)

- `common.py`: exact helpers. Random strict-best weakly guiding pair penalties with prescribed zeros; polygon clipping of
  the simplex; minimiser sets; rational grids.
- `sregion.py` → `sregion.out`: Lemma 3.1, 6000 cases, 0 failures.
- `removal.py` → `removal.out`: Lemma 3.2, 3000 cases. Minimiser sets compared at 325 grid points and all cell vertices;
  0 failures.
- `edge_touch.py` → `edge_touch.out`: the convexity and edge-point algebra of Lemma 4.3, with edge-free controls;
  0 failures.
- `t1_accept.py` → `t1_accept.out`: Lemma 4.4 (5616 exact cases) and the two Jacobians (λ², symbolic).
