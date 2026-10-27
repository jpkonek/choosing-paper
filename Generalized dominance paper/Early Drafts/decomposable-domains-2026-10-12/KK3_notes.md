# KK3 (round 39, BRIEF31). The non-(Av) branch of the protected route is empty: an evaluable target plus coherent vertex models make a domain either two-sided everywhere or one-sided on every mixed pair, and both cases exclude protected weak-additive designs

18 Oct 2026. Rules of BRIEF13 and BRIEF31; the corrections of AUDIT_JJ.md are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: none offered.

Scripts are in `kk3py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All arithmetic is
`fractions.Fraction`. Nothing in the proofs rests on the scripts; they re-check algebra that is proved below.

Setting and notation: three worlds, T1 = D_K with K = (1−ε)u + εΔ, any ε ∈ (0,1), c₀ := (1−ε)/3; the write-up §2, and
JJ3 §1 (advices M, S, O, ×; world ranks; c, c′, d; Σ(h); essential pairs E^j_{l,o}). The hypothesis set **(H)** is JJ3
§1.1 verbatim. No assumption is added. Every extra hypothesis below is a hypothesis of the stated result and is named
there.

---

## 0. Outcome

**Answer to the question of the brief: yes, in the strongest form.** The adopted requirements force (Av) whenever the
protected design has an essential zero, and they make the design zero-free on mixed pairs otherwise. The impossibility
theorem of JJ3 extends to every admissible domain.

The decisive fact is a dichotomy about domains. It needs neither (LF) nor additivity.

**Theorem 2.4 (PROVED; no imports beyond elementary convexity).** Let M be a decomposable domain in which D_{T1} is
evaluable and whose three world-best models B^1, B^2, B^3 are coherent. Then exactly one of the following holds:
- **(A)** B^i = {g : g_i > 0} a.e. for every i. Then acceptance is available for a.e. gamble that is not ≤ 0, and a.e.
  mixed pair has both acceptances in its advice range. In particular (Av) of JJ3 §4 holds.
- **(B)** a.e. mixed pair has at most one acceptance in its advice range.

So a domain cannot be "partly" two-sided. A non-null set of mixed pairs with both acceptances, anywhere in gamble
space, forces (Av) on the whole domain.

**Main Theorem 5.1 (PROVED modulo the imports listed in §5).** Let M be any decomposable domain with (LF) at D_{T1}.
There is no pair (Φ, p ↦ C_p) satisfying (H). That is:
- Φ an integrable, weakly guiding additive leading field;
- a selection of coherent models, continuous in measure, through T1;
- (NT).

Hence the protected-leading-field subclass is empty on every admissible domain. JJ3's residual of §7 is empty. The
lifting theorem (JJ1) has no instance for T1 on any decomposable (LF) domain.

**How the cases close.**
- **Case (A)** is a domain with (Av). JJ3 Theorem 5.1 applies as stated, with the repair of its Lemma 4.2 step 6
  written out in §3. Its imports are Theorem gm and Theorem ccibu.
- **Case (B)** is a one-sided domain. The design has no zeros on mixed pairs. Its unanimous zeros can be raised away
  without disturbing (NT). The field is then a strictly guiding additive cover with the original selection. Corollary
  TSalways(b) (or Theorem gm) excludes it. **ccibu is not needed in case (B).**

**What JJ3 used (Av) for (§1).**
- (Av_{l,o}) enters only at Lemma 4.2 step 3. There it confines the edge Bayes sets K₀(t) to the edge Δ_{lo} opposite
  the zero world, for each triple (j; l, o) with μ(E^j_{l,o}) > 0.
- The weakest sufficient property is this confinement itself. It is equivalent to (Av_{l,o}) (Lemma 1.1).
- Essential pairs in E^j_{l,o} are mixed pairs across the edge {l, o} with both acceptances in their advice range. So
  Theorem 2.4 puts the domain in case (A), and confinement follows (Corollary 3.1).
- A second proof of the confinement uses only the edge family of Φ, not the vertex models (Remark 3.2).

**On the brief's suggested route through the lifted system (§6).**
- The lifted rate system of JJ1 is a strict-(G) full cover. So every ranking-level result applies to it, and Theorem 2.4
  applies to it.
- Proposition L3.1(a), however, does **not** apply as stated. It assumes two-sidedness near ∂D_{T1}, and (LF) does not
  give that: (LF) supplies "accept h" and silence on the neighbourhood N, never "accept −h".
- R10a Thm V and Cor V2 do apply, on every decomposable domain. They supply the vertex anchoring and the identity
  Av ∩ D_i ≈ D_{V_i} used in §2. The missing step is the extreme-point lemma, Lemma 2.3.
- Theorem 2.4 is a strict generalisation of L3.1(a). It needs only a non-null set of two-sided mixed pairs and an
  evaluable interior target, and no (LF).

**Domain axioms alone do not force (Av) (Remark 2.6; PROVED, CHECKED).** Admissible one-sided domains violating (Av)
exist. They are decomposable, have (LF) at T1, contain T1 and have coherent vertex choices, but are not two-sided.
Example: vertex sets V_i = conv(e_i, Q) with Q ⊆ int T1; M_U is one instance. But they are all case (B), where the
design has nothing to exploit.

So the brief's alternative, "a concrete admissible menu where confinement fails, with a protected construction there",
is answered as follows. Confinement fails exactly on one-sided domains, and Proposition 4.2 excludes every protected
design there. No construction is possible, and none is attempted.

**Not touched (scope, BRIEF31 correction 1):**
- non-(NT) tie designs (II1 §6, II2 (★); KK4's target);
- non-protected rate designs;
- other exchange-rate rules;
- general (FC) rankings;
- the clone route.

As AUDIT_JJ insists, nothing here says that the adopted axioms exclude T1.

---

## 1. Where JJ3 uses (Av), and what would suffice

**(Av_{l,o})** (JJ3 §4): for a.e. gamble g with g_l > 0 and g_o > 0, accepting g lies in A(g).

Reading JJ3 line by line, (Av_{l,o}) is used exactly once: Lemma 4.2 step 3 ("confinement").
- Lemma 4.3 and Theorem 4.1 use (Av_{l,o}) only through Lemma 4.2 (the identity L_{h₁} = L_{h₂} and the good set G_C).
- Lemmas 1.1, 2.2–2.5, 3.1–3.3 and 4.4 use no availability beyond (LF) and T1 ∈ M. JJ3 §7 makes the same claim. I
  re-read the steps that could use availability:
  - Lemma 1.1 needs only evaluability of the world-best model and of switched models, which is decomposability.
  - Prop 2.5 needs acceptance on an open set inside N, which (LF) gives.
  - Theorem 4.1 Step 3 needs acceptance of y ∈ Y, which T1 ∈ M gives.
  - II1 Prop 3.1(a), imported by Prop 2.5, uses the Aumann convexity of the attainable set over the advice ranges
    (II1 Lemma 1.1), which holds on every decomposable domain.

Fix (j; l, o), coordinates in the order (j, l, o), and the edge weights w₀(t) := (0, 1−t, t). As in JJ3 Lemma 4.2
steps 1–2 (which use no (Av); see Lemma 3.3 below), for a.e. t the w₀(t)-minimiser is a.e. unique and equals D_{K₀(t)}.
Call such t **good**.

**(Conf_{l,o})**: K₀(t) ⊆ Δ_{lo} for a.e. t.

**Lemma 1.1 (PROVED).** Assume (H) on a decomposable domain with (LF). Then (Conf_{l,o}) ⟺ (Av_{l,o}).

*Proof.*
- **(⇐)** is JJ3 step 3: for good t, D_{K₀(t)} accepts every available g with g_l, g_o > 0. Accepting is then the
  strict minimiser at w₀(t), by strict-best at l and o (JJ3 Lemma 1.1(a)). If K₀(t) had a point m with m_j > 0, an
  open set of g near (−N, 1, 1) would be rejected.
- **(⇒)** If K₀(t) ⊆ Δ_{lo} for some good t, then every m ∈ K₀(t) has m·g = m_l g_l + m_o g_o > 0 whenever
  g_l, g_o > 0, so P_{K₀(t)}(g) > 0. The evaluable model D_{K₀(t)} accepts a.e. such g, so acceptance is in the advice
  range. ∎

**What is actually needed downstream** is less: that the advice of D_{K₀(t)} on an essential pair depends on the pair
only through π(h). That is what (Conf_{l,o}) gives in JJ3 step 4. Since (Conf_{l,o}) will be derived in full, the weaker
form is not pursued.

---

## 2. Two-sided or one-sided: a dichotomy for domains with an evaluable interior target

Throughout this section, M is a decomposable domain with advice ranges A(·) (write-up Remark advicerange). Notation:
- D_i := {g : g_i > 0};
- Av := {g : "accept g (and not −g)" ∈ A(g)}, a measurable set of orientations;
- the **world-i-best model** B^i is the model whose advice at a.e. pair is the world-i-best element of A(h) in the
  background order (good ≺ silence ≺ bad ≺ ×). It is evaluable by Remark advicerange.

For a credal set V write D_V^∘ := {g : P_V(g) > 0}, the open part of D_V. Then D_V = D_V^∘ ∪ {g ≥ 0, g ≠ 0}, and the two
differ by a null set off the positive orthant.

**Where the hypotheses come from.**
- **In (H):** JJ3 Lemma 1.1(a)'s proof shows C_{e_k} = B^k. C_{e_k} is coherent because the selection is.
- **In any ranking with strict (G), (S), (LA):** C_{e_i} is competitive on {i}. With strict (G) this forces it to be
  world-i-best a.e., since otherwise switching to the better advice on a non-null set would give a strictly better
  evaluable model (DCE prop:ideal; R10a Thm V, first bullet). C_{e_i} ∈ C_L is coherent.
- **The lifted system of JJ1:** a ranking of the second kind, with the same vertex models C_{e_i}.

**Lemma 2.1 (PROVED).** Suppose B^i = D_{V_i} a.e. for a credal set V_i. Put U_i := conv(V_i ∪ {e_i}). Then:
- (a) Av ∩ D_i ≈ D_{U_i}^∘ (equality modulo null sets);
- (b) if D_{T1} ∈ M, then U_i ⊆ conv(T1 ∪ {e_i}).

*Proof.*
- **(a)** Let g ∈ D_i. Accepting g is good at world i, so it is the world-i-best advice whenever it is in A(g).
  - Hence, for a.e. g ∈ D_i: the advice of B^i at the pair is "accept g" iff g ∈ Av.
  - B^i = D_{V_i} is coherent, so it contains both g and −g only on a null set. For a.e. g ∈ D_i, "accept g" therefore
    means g ∈ D_{V_i}.
  - So Av ∩ D_i ≈ D_{V_i} ∩ D_i.
  - Finally, P_{U_i}(g) = min(P_{V_i}(g), g_i). So D_{V_i}^∘ ∩ D_i = D_{U_i}^∘, and D_{V_i} ∩ D_i differs from it by a
    null set.
- **(b)** For a.e. g ∈ D_{T1} that is not ≥ 0, the advice of D_{T1} is "accept g", so g ∈ Av.
  - Hence D_{T1}^∘ ∩ D_i ⊆ Av ∩ D_i ≈ D_{U_i}^∘ a.e. The left side is D_C^∘ with C := conv(T1 ∪ {e_i}).
  - Suppose m ∈ U_i ∖ C. Separate strictly in aff Δ and add a multiple of 𝟙: some gamble g has min_C m′·g > 0 > m·g.
    A ball around g then lies in D_C^∘ and misses D_{U_i}^∘. This contradicts a.e. inclusion. ∎

**Lemma 2.2 (PROVED; (b) CHECKED, `dichotomy.py` (1)).**
- (a) **Injectivity** (write-up §2): D_A ≈ D_B modulo null sets only if A = B.
- (b) **Hull identity:** P_{conv(V ∪ {e_l, e_o})}(g) = min(P_V(g), g_l, g_o). Hence D_V^∘ ∩ D_l ∩ D_o
  = D^∘_{conv(V ∪ {e_l, e_o})}.
- (c) **Interior target:** conv(T1 ∪ {e_i}) ∩ ∂Δ = {e_i}.

*Proof.*
- (b) A linear function attains its minimum over a convex hull at a point of the generating set.
- (c) Every point other than e_i has the form λe_i + (1−λ)x with λ < 1 and x ∈ T1 ⊆ int Δ, so all its coordinates are
  positive. (The vertices c₀𝟙 + εe_k of T1 have all coordinates ≥ c₀ > 0; CHECKED for seven values of ε.) ∎

**Lemma 2.3 (the edge lemma; PROVED; CHECKED, `dichotomy.py` (3)).** Under Lemma 2.1's hypotheses, fix l ≠ o. Then:
- (a) W_{lo} := conv(U_l ∪ {e_o}) = conv(U_o ∪ {e_l}), and Av ∩ D_l ∩ D_o ≈ D^∘_{W_{lo}}.
- (b) If W_{lo} ⊄ Δ_{lo}, then U_l ∩ U_o contains a point m* ∉ Δ_{lo}. Consequently, a.e. gamble g with
  g_l > 0 > g_o has at most one of its two acceptances in A(g).
- (c) If a non-null set of g with g_l > 0 > g_o has both acceptances in A(g), then U_l = {e_l} and U_o = {e_o},
  provided also D_{T1} ∈ M.

*Proof.*
- **(a)** By Lemma 2.1(a) and Lemma 2.2(b):
  Av ∩ D_l ∩ D_o ≈ D_{U_l}^∘ ∩ D_o = D^∘_{conv(U_l ∪ {e_o})}, and symmetrically ≈ D^∘_{conv(U_o ∪ {e_l})}.
  Injectivity gives equality of the two credal sets.
- **(b)**
  - W_{lo} is compact and convex, so it is the convex hull of its extreme points. Δ_{lo} is convex, so some extreme point
    m* of W_{lo} lies outside Δ_{lo}.
  - Extreme points of the convex hull of a compact set belong to that set. Since m* ∉ {e_l, e_o}, writing
    W_{lo} = conv(U_l ∪ {e_o}) gives m* ∈ U_l, and writing W_{lo} = conv(U_o ∪ {e_l}) gives m* ∈ U_o.
  - Now let g_l > 0 > g_o.
    - If "accept g" ∈ A(g), then g ∈ Av ∩ D_l ≈ D_{U_l}^∘. So, for a.e. such g, m*·g > 0.
    - If "accept −g" ∈ A(g), then −g ∈ Av ∩ D_o ≈ D_{U_o}^∘. So, for a.e. such g, m*·g < 0.
  - Both cannot hold.
- **(c)** By (b), W_{lo} ⊆ Δ_{lo}. So U_l ⊆ Δ_{lo} ∩ conv(T1 ∪ {e_l}) = {e_l}, by Lemma 2.1(b) and Lemma 2.2(c). Likewise
  U_o = {e_o}. ∎

**Theorem 2.4 (PROVED).** Let M be a decomposable domain with D_{T1} ∈ M, and suppose B^1, B^2, B^3 are coherent. Then
exactly one of (A), (B) of §0 holds.

*Proof.*
- **Suppose (B) fails.** A non-null set of mixed pairs has both acceptances. Every mixed orientation g has some
  l with g_l > 0 and some o with g_o < 0. So for one ordered pair (l, o), a non-null set of g with g_l > 0 > g_o has
  both acceptances.
  - Lemma 2.3(c) gives U_l = {e_l} and U_o = {e_o}.
  - Let c be the third world. Lemma 2.3(a) for the pair {l, c} gives conv(U_c ∪ {e_l}) = conv(U_l ∪ {e_c}) = Δ_{lc}, so
    U_c ⊆ Δ_{lc}. Likewise U_c ⊆ Δ_{oc}. Hence U_c = {e_c}.
- **Consequences.**
  - U_i = conv(V_i ∪ {e_i}) = {e_i} forces V_i = {e_i}, so B^i = D_{{e_i}} = {g : g_i > 0} a.e. Lemma 2.1(a) gives
    Av ∩ D_i ≈ D_i for every i.
  - Every g that is not ≤ 0 lies in some D_i, so it is in Av. A mixed g and its negative are both not ≤ 0, so a.e.
    mixed pair has both acceptances. That is (A).
- **Exclusivity.** (A) and (B) are incompatible, because mixed pairs form a non-null set. ∎

**Corollary 2.5 (PROVED).** Let L be any ranking on a decomposable domain with strict (G), (S) and (LA), with D_{T1}
evaluable. (L need not have T1 ∈ C_L, and (LF) is not needed.) Then the domain is of type (A) or of type (B).
- In type (A), C_{e_i} = {g : g_i > 0} a.e.
- This contains Proposition L3.1(a) of the write-up. There, two-sidedness near ∂D_{T1} supplies an open, hence
  non-null, set of mixed pairs with both acceptances. L3.1(a) also assumed (LF) and T1 ∈ C_L.
- It applies in particular to the lifted rate system of JJ1.

*Proof.* The vertex models are the coherent world-best models (paragraph before Lemma 2.1). Apply Theorem 2.4. ∎

**Remark 2.6 (domain axioms do not force (Av); PROVED, CHECKED `dichotomy.py` (4)).** Let Q be a nonempty compact
convex subset of int T1. Put:
- V_i := conv(e_i, Q);
- A(g) ∋ "accept g" iff g ∈ ∪_i D_{V_i}^∘, and likewise for −g;
- silence always available;
- × optional.

Then:
- the domain is decomposable;
- D_{T1} is evaluable, because D_{T1}^∘ ⊆ D_Q^∘ ∩ (∪D_i) ⊆ ∪_i D_{V_i}^∘;
- (LF) holds at T1: every h ∈ ∂D_{T1} ∖ 0 has P_Q(h) > 0, since Q ⊆ int T1, and some h_i > 0. So h lies in the open set
  D_{V_i}^∘, with silence available;
- the world-best models are B^i = D_{V_i}, which are coherent;
- (Av_{l,o}) fails for every edge: (−N, 1, 1) in coordinates (j, l, o) is not available for N > 3/min_Q m_j;
- the domain is one-sided: g and −g in Av would need P_Q(g) > 0 and P_Q(−g) > 0.

Q = u + s(T1 − u) gives exactly the U-domain M_U (write-up §2, `aos`). The exact check covers 240 random such domains
(four values of ε): compatibility, (LF) at 2393 boundary points, one-sidedness on 10594 mixed gambles, and the
non-availability witnesses. 0 failures.

So the answer to "do the adopted domain requirements force (Av)?" is **no**. But by Theorem 2.4 every domain without
(Av) is one-sided on mixed pairs, and that is what §4 exploits.

---

## 3. JJ3 Lemma 4.2 without the hypothesis (Av), with the step-6 repair

**Corollary 3.1 (PROVED).** Assume (H) on a decomposable domain with (LF). If μ(E^j_{l,o}) > 0 for some (j; l, o),
then the domain is of type (A). In particular (Av) and (Conf_{l,o}) hold.

*Proof.*
- An essential pair h ∈ E^j_{l,o} has h_l > 0 > h_o. It carries a zero, so {M, S, O} ⊆ A(h) (JJ3 Lemma 1.1(b)). So both
  acceptances are in its advice range.
- The vertex models are coherent world-best models (§2). T1 ∈ M.
- Theorem 2.4 gives type (A), and Lemma 1.1 gives (Conf_{l,o}). ∎

**Remark 3.2 (a second proof of (Conf_{l,o}) from the edge family alone; PROVED; edge algebra CHECKED,
`edge_flip.py`).** This route does not use the vertex models.
- **The edge sets span a common hull.** For good t and a.e. g with g_l, g_o > 0:
  - if g ∈ Av, accepting is the strict w₀(t)-minimiser (strict-best at l and o);
  - otherwise it is not available.
  - So D_{K₀(t)} ∩ D_l ∩ D_o ≈ Av ∩ D_l ∩ D_o, which does not depend on t. By Lemma 2.2, W := conv(K₀(t) ∪ {e_l, e_o})
    is the same set for all good t.
- **Suppose (Conf_{l,o}) fails.** Then W ⊄ Δ_{lo}. As in Lemma 2.3(b), an extreme point m* ∉ Δ_{lo} of W lies in
  K₀(t) for **every** good t.
- **Flips are then impossible.**
  - Let a_t(h) be the unique w₀(t)-minimiser at h. The map (t, h) ↦ a_t(h) is jointly measurable, because φ is
    measurable and the weights are affine in t.
  - Let F be the set of (t₁, t₂, h) with t₁, t₂ good, a_{t₁}(h) = accept h and a_{t₂}(h) = accept −h.
  - If F were non-null, Tonelli would give good t₁, t₂ with a non-null h-section. For a.e. h in it,
    h ∈ D^∘_{K₀(t₁)} and −h ∈ D^∘_{K₀(t₂)}, so m*·h > 0 > m*·h.
- **Essential pairs flip.** By Lemma 3.3(b), each h ∈ E^j_{l,o} has a_t(h) = M on [0, m_h) and O on (s_h, 1], both
  intervals of positive length. So F ⊇ {(t₁, t₂, h) : h ∈ E^j_{l,o}, t₁ < m_h, t₂ > s_h, t₁, t₂ good}, which has
  positive measure by Tonelli. So μ(E^j_{l,o}) > 0 forces (Conf_{l,o}).

**Lemma 3.3 (JJ3 Lemma 4.2, rewritten; PROVED; (b) CHECKED, `edge_flip.py`).** Assume (H) on a decomposable domain
with (LF), and (Conf_{l,o}). This holds whenever μ(E^j_{l,o}) > 0, by Corollary 3.1.

- (a) For a.e. t ∈ (0, 1):
  - the w₀(t)-minimiser is a.e. unique;
  - it equals D_{K₀(t)} a.e.;
  - K₀(t) = {(0, 1−x, x) : x ∈ [α(t), β(t)]}.
- (b) For every h ∈ E^j_{l,o}, the unique minimiser of w₀(t)·φ(h, ·) is:
  - M on [0, m_h);
  - S on (m_h, s_h);
  - O on (s_h, 1].

  At m_h exactly M, S tie; at s_h exactly S, O tie. In particular the O-set on the **whole** edge is (s_h, 1].
- (c) There is a full-measure subset G_C of E^j_{l,o} such that, for h ∈ G_C, (s_h, 1) =_{a.e.} {t : α(t) > π(h)}.
  Hence s_h = s_{h′} whenever h, h′ ∈ G_C and π(h) = π(h′).

*Proof.*

**(a), uniqueness.** For a.e. h, no two distinct advices a, b ∈ A(h) agree at both l and o. (× is strictly worst after
JJ3 Lemma 1.1(b).)
- If h_l, h_o have the same sign, the world-l and world-o ranks coincide. So b := best_l(h) = best_o(h), whichever
  advices are available, and b is strictly cheapest at both l and o (JJ3 Lemma 1.1(a)). Hence b is the unique
  w₀(t)-minimiser for **every** t ∈ [0, 1].
- If h_l > 0 > h_o: M (if available) is strictly best at l, so it differs from S and O at l. O (if available) is
  strictly best at o, so it differs from S at o.
- So, for such h, w₀(t)·(φ(h,a) − φ(h,b)) is a nonzero affine function of t for each a ≠ b among the non-× advices,
  and ties occur at finitely many t. Tonelli gives a null tie set for a.e. t.

  (JJ3's step 1 said "M is strictly best at l and o" when l, o are both positive. On a non-(Av) domain M may be
  unavailable there; the argument above covers that case. In type (A) it is moot.)

**(a), the edge sets.** JJ3 Lemma 2.3(b) gives the coherent limit D_{K₀(t)}, and (Conf_{l,o}) gives the form.

**(b).** Write c·w₀(t) = c_l(1−t) + c_o t with c_l > 0 > c_o, which vanishes at m_h; and c′·w₀(t) = c′_l(1−t) + c′_o t
with c′_l < 0 < c′_o (c′_j = 0 is the zero), which vanishes at s_h. Essential means case (b2) of JJ3 Lemma 3.1, i.e.
m_h < s_h; both lie in (0, 1).
- On [0, m_h): c·w > 0. Also d = c − c′ has d·w₀(0) = d_l > 0 and d·w₀(m_h) = −c′·w₀(m_h) > 0, so d·w > 0 on [0, m_h].
  So M is the unique minimiser.
- On (m_h, s_h): c·w < 0 and c′·w < 0, so S is the unique minimiser.
- On (s_h, 1]: c′·w > 0. Also d·w₀(s_h) = c·w₀(s_h) < 0 (since s_h > m_h) and d·w₀(1) = d_o < 0, so d·w < 0 on
  [s_h, 1] by linearity. So O is the unique minimiser.
- For t < s_h, c′·w < 0 makes S strictly cheaper than O. So O is never a weak minimiser before s_h.
- × never minimises. This is the audit's repair (AUDIT_JJ point 3), written out.

CHECKED (`edge_flip.py`): 10007 random exact essential pairs, all orderings of (j, l, o), 190133 exact edge points,
including the two tie points, points within 10⁻⁶ of s_h, and the five sign conditions above. 0 failures.

**(c).**
- *Measurability.* For good t, K₀(t) = lim_n K_{w_n(t)} with w_n(t) := (1 − 1/n)w₀(t) + u/n. Each t ↦ K_{w_n(t)} is
  continuous (JJ3 Lemma 2.3(a)). So t ↦ K₀(t) is Borel on the good set, as a pointwise limit of continuous maps into the
  Hausdorff metric space. Also α(t) = min_{m ∈ K₀(t)} m_o, which is Hausdorff-continuous in the set.
- *The bad set.* Let Bad := {(t, h) : t good, h ∈ E^j_{l,o}, 1[a_t(h) = O] ≠ 1[α(t) > π(h)]}. It is jointly measurable.
  For m = (0, 1−x, x), m·h̄ = π − x. So D_{K₀(t)} gives O at h iff max_{K₀(t)} m·h̄ < 0 iff α(t) > π(h).
- *Sections.* For good t, the minimiser model equals D_{K₀(t)} a.e. So each t-section of Bad is null. Tonelli: for a.e.
  h ∈ E^j_{l,o} the h-section is null. Let G_C be this set of h.
- *Conclusion.* For h ∈ G_C, (b) gives {t : a_t(h) = O} = (s_h, 1]. So (s_h, 1) =_{a.e.} {t : α(t) > π(h)}. The right
  side depends on h only through π(h). Two intervals (s, 1) and (s′, 1) agree a.e. only if s = s′. No truncation at
  max(m_h, m_{h′}) is needed. ∎

With Lemma 3.3 in place of JJ3 Lemma 4.2, JJ3 Lemma 4.3 and Theorem 4.1 run verbatim. The only things they take from
Lemma 4.2 are L_{h₁} = L_{h₂} (from s_{h₁} = s_{h₂} and e_j ∈ L_h) and the set G_C. This gives:

**Corollary 3.4 (PROVED modulo JJ3 Lemmas 2.3–2.4, 4.3, 4.4 at their recorded status).** Under (H) on any decomposable
domain with (LF): μ(E) = 0.

*Proof.* If μ(E^j_{l,o}) > 0, then (Conf_{l,o}) holds by Corollary 3.1. JJ3 Theorem 4.1 then gives
μ(E^j_{l,o}) = 0, a contradiction. ∎

---

## 4. Case (B): one-sided domains, without ccibu

**Lemma 4.1 (PROVED; CHECKED, `edge_flip.py`).** Assume (H), with × strictly worst (JJ3 Lemma 1.1(b)). On every
unanimous pair (index h ≥ 0), replace:
- φ_k(h, O) by φ′_k(h, O) := φ_k(h, O) + h_k;
- φ_k(h, ×) by max(φ_k(h, ×), φ′_k(h, O)) + h_k;

for each k, leaving everything else unchanged. Then (H) still holds, with the same selection, and the new field has no
zero on any unanimous pair.

*Proof.*
- **Coherent models are unaffected.** A coherent model D_K contains every h ≥ 0, h ≠ 0, and never −h (P_K(−h) < 0). So
  it gives M a.e. on unanimous pairs. Hence Φ′(C_p) = Φ(C_p).
- **(NT) is preserved.** Φ′(X) ≥ Φ(X) for every X. So Φ′_J(X) ≤ Φ′_J(C_p) gives Φ_J(X) ≤ Φ_J(C_p), hence X = C_p a.e.
- **Other properties.** Integrability holds, because h_k is Gaussian-integrable. Weak guidance and continuity are
  untouched.
- **No zeros.** At every world, on a unanimous pair, the order is M (strictly best, Lemma 1.1(a)) < S < O < ×, with
  strict steps after the raise. ∎

CHECKED: 5000 random exact instances. Strict order, M unchanged, all costs weakly increased.

**Proposition 4.2 (PROVED modulo Corollary TSalways(b)).** On a type-(B) decomposable domain with (LF) at D_{T1}, no
pair satisfies (H).

*Proof.*
1. **A strictly guiding field.** Assume (H). Normalise × (JJ3 Lemma 1.1(b)) and raise as in Lemma 4.1. After this, every
   equality between distinct available advices at a world is a bad~silence zero on a pair with {M, S, O} ⊆ A(h) (JJ3
   Lemma 1.1(b)).
   - On a mixed pair this needs both acceptances, which type (B) excludes a.e.
   - On unanimous pairs, Lemma 4.1 removed them.

   So the field Φ″ is strictly increasing in world rank a.e.: it is strictly guiding.
2. **A cover with the original selection.** This is II1 Prop 5.1 Step 2, whose logic JJ1 §3.1 CHECKED. With the original
   selection, Φ″ is an additive ranking with (G) and (IB). Further:
   - **(S):** C_p is competitive on supp p, because a rival with Φ″_i(X) ≤ Φ″_i(C_p) for all i ∈ supp p equals C_p by
     (NT). The sections {p : Φ″_i(C_p) ≤ Φ″_i(X)} are closed, by continuity in measure and the integrable envelope.
     C_p is coherent and, by (NT), undominated.
   - **(LA):** holds.
   - **(C):** Theorem kkm (valid for preorders) ties every undominated model at every world with some C_p, so (NT)
     makes it C_p. Hence C_L is the set of selected models, and a model tied with C_p at every world is C_p.
   - **(LF):** at T1 it is a property of M, and T1 = C_{q₀} ∈ C_L.
3. **Contradiction.** Φ″ is a strictly guiding additive ranking with integral penalties covering T1 on a decomposable
   domain with (LF). On that domain the advice range of a.e. mixed pair lacks one acceptance. Corollary TSalways(b)
   excludes this (status: N28 Cor 3.6; refereed once; second reading of (b) CONFIRMED in TS_second_referee §2). So
   does Theorem gm. ∎

*Remarks.*
- Proposition 4.2 contains II1 Prop 5.1 (the U-domain), which is of type (B) by Remark 2.6.
- It needs neither ccibu, nor JJ3 Theorem 2.1, nor any essential-zero analysis.

---

## 5. The main theorem

**Theorem 5.1 (PROVED modulo the imports below).** Let M be a decomposable domain with (LF) at D_{T1}. No
(Φ, p ↦ C_p) satisfies (H).

*Proof.*
- Under (H), T1 = C_{q₀} ∈ M, and the vertex models C_{e_k} = B^k are coherent (JJ3 Lemma 1.1(a)). So Theorem 2.4
  applies.
- **Type (A).** (Av) holds. JJ3 Theorem 5.1 applies as stated, with Lemma 3.3 in place of JJ3 Lemma 4.2. Equivalently:
  - Corollary 3.4 gives μ(E) = 0;
  - JJ3 Prop 3.3 gives a strictly guiding Φ′ with the same Bayes models at every weight;
  - Theorem ccibu makes it a cover of T1;
  - Theorem gm excludes that.
- **Type (B).** Proposition 4.2. ∎

**Dependencies.**

| Branch | Inputs | Status |
|---|---|---|
| both | Theorem 2.4 (with Lemmas 2.1–2.3) | PROVED here, no imports |
| both | JJ3 Lemma 1.1(a)(b): strict-best, C_{e_k} = B^k, × normalisation, zero location | PROVED in JJ3 (one reader), re-read here; II1 Prop 5.2(a)(b) refereed (JJ1 §3.2) |
| (A) | JJ3 Thm 2.1, Lemmas 2.2–2.4, Prop 2.5 (imports II1 Prop 3.1(a)), Lemmas 3.1–3.3, 4.3, 4.4, Thm 4.1 | PROVED in JJ3 (one reader, not refereed; KK1 is refereeing them this round) |
| (A) | JJ3 Lemma 4.2 | **replaced** by Lemma 3.3 here (repair of step 6 written out; step 1 generalised) |
| (A) | Theorem ccibu | author-checked, no formal referee report (KK2 this round) |
| (A) | Theorem gm | three routes, each refereed once; shared inputs read twice (write-up Table gmdeps) |
| (B) | Lemma 4.1, II1 Prop 5.1 Step 2 logic, Theorem kkm | PROVED here; CHECKED in JJ1 §3.1; proved (Loss Dominance Generalized v2) |
| (B) | Corollary TSalways(b) | refereed once; second reading CONFIRMED (TS_second_referee §2); rests on N21 Thm N21.6 (an input of gm) |

**Corollary 5.2 (same status).**
- On every decomposable domain with (LF) at D_{T1}, the hypotheses of II1 Thm 4.1, II2 Cor 2.4 and JJ1's lifting
  theorem have no instance through T1.
- II1's problem P_w has the answer NO on every such domain, not only on the full domain.
- JJ3 §7's residual is empty.
- In the exchange-rate class of BRIEF29, every cover of T1 (if any), on any admissible domain, has a leading selection
  that is not (NT): it is a tie design, a non-protected rate design, or lies outside the class.

**Remark 5.3 (the by-product class of JJ3 Remark 5.3).** JJ3 Theorem 5.1 also excludes weakly guiding Φ with a
coherent continuous selection through T1 satisfying JJ3's (i)–(iii) in place of (NT). The extension holds for that class
too.
- Theorem 2.4 needs only (iii) (C_{e_k} = B^k, coherent).
- Lemma 4.1 needs that (i)–(iii) survive raising costs of advices that coherent models never give. They do, as for ×.
- Step 2 of Proposition 4.2 uses (i), (ii) and Theorem kkm.

---

## 6. Answers to the brief's specific questions

1. **What (Av) is used for; what weaker availability suffices.**
   - Only JJ3 Lemma 4.2 step 3, for the triples with μ(E^j_{l,o}) > 0.
   - Edge confinement (Conf_{l,o}) suffices, and it is equivalent to (Av_{l,o}) (Lemma 1.1).
   - What is needed downstream is less still: s_h a function of π(h) on essential pairs.
2. **Do the write-up's general-domain results supply it?**
   - *Cor availability / TSalways(b),(c)* are proved for strictly guiding additive covers through the (TS)/cuts chain.
     They do not apply to Φ, which is only weakly guiding. JJ3 deliberately avoids re-running that chain.
   - *The lifted system* is a strict-(G) (FC) cover on the same domain with the same vertex models. Ranking-level
     results apply to it.
     - L3.1(a) needs two-sidedness near ∂D_{T1}, which (LF) does not give, so it does not apply as stated.
     - R10a Thm V and Cor V2 do apply.
     - Combined with the extreme-point Lemma 2.3, they give Theorem 2.4 (Corollary 2.5).
     - The input that makes it bite is that essential pairs are two-sided across their edge.
   - So yes: the needed property is supplied. It comes either through the lifted system (Corollary 2.5) or directly
     from (H) (Corollary 3.1). Remark 3.2 gives a third, edge-family proof.
3. **A concrete admissible menu where confinement fails.**
   - Such menus exist (Remark 2.6, CHECKED).
   - By Theorem 2.4 they are all one-sided on mixed pairs. On them a protected design has no essential zeros, and
     indeed no zeros on mixed pairs. Proposition 4.2 excludes it.
   - Hence there is nothing to construct. The prescribed construction (silence~bad zeros of JJ3 §7's surviving pattern)
     needs both acceptances at the zero pairs, and that is exactly what forces type (A).

**Side consequence for the write-up (PROVED, one reader; not used above).**
- Corollary 2.5 says every decomposable domain carrying a ranking with strict (G), (S), (LA) and an evaluable D_{T1} is
  either an (Av) domain in the write-up's sense ("a.e. mixed pair has both acceptances") or one-sided on mixed pairs.
- So the configurations (GnAv-nd), (GnAv-d) of R21 Part B concern one-sided domains only. On those, additive covers are
  excluded by Cor TSalways(b).
- I do not claim that this closes those configurations for general rankings.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | (Conf_{l,o}) ⟺ (Av_{l,o}) under (H) | PROVED |
| 2.1 | Av ∩ D_i ≈ D°_{U_i}; U_i ⊆ conv(T1 ∪ e_i) | PROVED |
| 2.2 | injectivity; hull identity; conv(T1 ∪ e_i) ∩ ∂Δ = {e_i} | PROVED; (b), (c) CHECKED |
| **2.3** | **common off-edge extreme point of the two vertex sets; two-sided pairs across an edge force precise vertex sets at its ends** | **PROVED; CHECKED (2908 hulls, 116320 gambles)** |
| **2.4** | **dichotomy: type (A) (two-sided, precise vertex models, (Av)) or type (B) (one-sided on mixed pairs)** | **PROVED** |
| 2.5 | ranking-level form; contains L3.1(a); applies to the lifted system | PROVED |
| 2.6 | admissible non-(Av) domains exist (all one-sided); M_U is one | PROVED; CHECKED (240 domains) |
| 3.1 | μ(E^j_{l,o}) > 0 ⇒ type (A) ⇒ (Conf_{l,o}) | PROVED |
| 3.2 | second proof of confinement from the edge family | PROVED; edge algebra CHECKED |
| **3.3** | **JJ3 Lemma 4.2 with the step-6 repair (whole-edge O-set (s_h, 1]) and a general step 1** | **PROVED; (b) CHECKED (10007 pairs, 190133 points)** |
| 3.4 | μ(E) = 0 on every decomposable (LF) domain | PROVED modulo JJ3 Lemmas 4.3, 4.4 and §2 |
| 4.1 | raising unanimous O-costs keeps (NT) and removes unanimous zeros | PROVED; CHECKED (5000) |
| 4.2 | no (H) design on one-sided (LF) domains | PROVED modulo Cor TSalways(b) (no ccibu) |
| **5.1** | **no protected weak-additive leading field through T1 on any decomposable domain with (LF)** | **PROVED modulo: (A) gm, ccibu, JJ3 §§2–4 (one reader); (B) Cor TSalways(b)** |
| 5.2 | P_w = NO on every admissible domain; lifting theorem has no T1 instance; JJ3 §7 empty | same |
| — | tie designs, non-protected rate designs, general FC covers, clone route | **untouched** |

**Referee priorities.**
1. Lemma 2.3(b): the extreme-point step. An extreme point of conv(U_l ∪ {e_o}) other than e_o lies in U_l; with the
   hull identity of (a), it lies in both sets. Check also that "a.e. g ∈ Av ∩ D_l is in D°_{U_l}" is applied to
   orientations with g_l > 0 > g_o only.
2. Lemma 2.1(a): that B^i's advice on a pair with g_i > 0 is "accept g" exactly when that advice is available. This
   uses that the background order is total and that × never occurs a.e. in a coherent model.
3. Theorem 2.4's propagation to the third world. Lemma 2.3(a) for {l, c} with U_l = {e_l} gives
   conv(U_c ∪ {e_l}) = Δ_{lc}.
4. Lemma 4.1: that coherent models give M a.e. on unanimous pairs, so raising O and × changes no selected cost.
5. Lemma 3.3(c): the Borel measurability of t ↦ K₀(t) on the good set (pointwise limit of continuous maps).

---

## 8. Files (`kk3py/`)

- `kk3common.py`: exact helpers (lower previsions over vertex lists, exact 2-D hulls, point-in-hull, T1 vertices).
- `dichotomy.py` → `dichotomy.out`:
  - (1) hull identity, 20000 cases;
  - (2) interiority of T1's vertices, seven values of ε;
  - (3) Lemma 2.3 on 2908 random hull instances (hull equality verified exactly), 116320 gambles across the edge, with
    the precise control (all two-sided);
  - (4) Remark 2.6 on 240 random one-sided admissible domains.
  - 0 failures.
- `edge_flip.py` → `edge_flip.out`:
  - Lemma 3.3(b) and the audit's repair inequalities on 10007 random exact essential pairs (190133 exact edge points),
    and the M → O flip used in Remark 3.2;
  - Lemma 4.1 on 5000 random unanimous pairs.
  - 0 failures.
