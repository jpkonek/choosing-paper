# JJ2 (round 38, BRIEF30, construction side). The protected weak-additive leading field cannot be built: every zero the brief proposes is invisible to the Bayes family, the only visible zeros are "active" single zeros, and Theorem gm's proof survives weak signs

18 Oct 2026. Rules of BRIEF13 and BRIEF30; the corrections of AUDIT_II.md are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: none offered.

Scripts are in `jj2py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All arithmetic is
`fractions.Fraction`.

Setting: three worlds, T1 = D_K with K = (1−ε)u + εΔ = {m ∈ Δ : m_k ≥ c₀ for all k}, any ε ∈ (0,1), c₀ := (1−ε)/3,
κ := (1+2ε)/(1−ε). Notation of the write-up §2, II1 §1 and II2 §1. The domain is the full four-advice domain. No
assumption is added. Every extra hypothesis below is a hypothesis of the stated result and is named there.

The parallel note JJ3 (impossibility side, same round, not refereed) reaches the same final conclusion by a different
treatment of the hardest case. Where the two notes overlap (§4, §5) the arguments were found independently; the
perturbations used for removal differ. JJ1 (parallel referee report) finds the lifting theorem (II1 Thm 4.1 / II2
Cor 2.4) correct. Neither is used as an input here.

---

## 0. Outcome

**No construction exists. The object the brief asks for is excluded on the full domain, for every zero pattern
(Theorem 7.4; PROVED modulo the imported chain of Theorem gm's short route, through the sign audit of §7).** So the
sufficient theorem has no instance for T1, and the protected-leading-field subclass is empty. The non-(NT) tie designs
(II1 §6, II2 (★)) are untouched.

What was done, in the order of the brief.

1. **The certificate (§2; PROVED, CHECKED).**
   - Unique pointwise Bayes optimality of w(p)·Φ with supp w(p) ⊆ supp p implies (NT). This holds at vertices and on
     edges as well (Lemma 2.1).
   - Conversely, at a weight with full support on supp p, (NT) fails exactly when a tie record has zero leading
     increment (Lemma 2.2). In the abstract cell setting, ties do not by themselves violate (NT) (CHECKED example).
   - On the real domain, (NT) forces the certificate at every interior weight, because tie sets there are null
     (Lemma 4.1).
2. **The key tension (§3; PROVED, CHECKED).** The brief's condition is correct, and holds for every support (Lemma 3.1).
   - A selected model silent on a pair needs, among its active worlds, a world where accepting is bad and not tied with
     silence, and a world where rejecting is bad and not tied.
   - Every zero at world i on a gamble g with g_m > 0 forces the two acceptances to compete directly along the edge
     (e_i, e_m) (Lemma 3.3). It also forces the selected edge models there to be precise on a set of positive length
     carrying the zero ratios (Theorem 3.4).
3. **The brief's suggested zero patterns are all invisible (§5; PROVED modulo Theorems gm and ccibu).** Several
   placements were suggested:
   - zeros only where every selected model gives definite advice;
   - zeros at worlds never active for the silent models;
   - zeros where T1 and every C_p accept or reject.

   In each case every zero is **inactive**: its zero line runs through the region where the good acceptance strictly
   wins (Corollary 5.6). Such zeros can be removed by an explicit rotation that changes no weak minimiser at any weight
   of the closed simplex (Proposition 5.3; CHECKED on 1505 exact instances, with a complete test-point set). The field
   then becomes strictly guiding with the same Bayes family, and Theorem gm applies verbatim (Theorem 5.5).
   - **Exact reason these patterns fail:** the Bayes family they produce is the Bayes family of a strictly guiding
     field.
4. **The only zeros that matter are active single zeros (§§5–6; PROVED).** On such a zero, the acceptance/silence
   interface of a two-negative gamble g lies on a line through the vertex e_i with g_i < 0. No strictly guiding field
   can reproduce it (Proposition 5.4).
   - These zeros sit exactly where the brief's suggestion says not to put them: at a world that is active for silent
     interior models.
   - Their forced structure is recorded in Proposition 6.1:
     - edge precision;
     - degenerate interior credal sets along their d-faces;
     - near ∂D_{T1}, confinement to the six crossing rays (Prop 7.3).
5. **Theorem gm does not break (§7; PROVED modulo its imported chain).**
   - In the short route (Theorem collar, Theorem D, Theorem A, with their inputs), the field's signs enter in only three
     forms:
     - (F1) the good acceptance is strictly best at each world;
     - (F2) d = φ(acc −g) − φ(acc g) has the strict sign pattern of g;
     - (F3) c^g_i ≤ 0 where g_i < 0.
   - Strict-best gives (F1) and (F2). Weak guidance gives (F3).
   - Strict badness, (F4) c^g_i < 0 where g_i < 0, is used strictly in exactly two places:
     - the edge box, which also follows from (F2);
     - one sentence of the cut theorem, which is unaffected (Table 7.2, items S8a–b).
   - With Lemma 4.1 supplying (BU) at every interior weight, the route runs verbatim for a strict-best weakly guiding
     field. So no "weak cover" of T1 exists (Theorem 7.2), and in particular no (NT) design.
6. **T1's weight.** In every (NT) design, T1 is the unique Bayes model of Φ at some interior w* (Lemma 4.3). This is
   what the brief asked to check. It holds, and it is part of what makes gm applicable.

**Answer to "check that gm's proof breaks exactly there".**
- For inactive zeros, gm never sees them: the Bayes family is unchanged by deleting them.
- For active zeros, gm's proof does not break either. Every step uses (F1)–(F3) only.

The bad~silence zeros that II1 Prop 5.2 required are therefore no escape. The "missing strict badness" of II1 §5.3 was
needed only on the U-domain, where no rejecting advice is available (II1 Prop 5.1). On the full domain the strict sign
of d does its work.

**Single most important open point.** A second, independent reading of the sign audit in §7. It covers the two strict
uses of strict badness:
- S8a, the chart-form edge box via d;
- S8b, the cut theorem's Step 2 at the crossing.

It also covers the claim that the short route uses a cover only through its interior Bayes family (W1)–(W6).
JJ3 §4 is an alternative, elementary exclusion of the same active zeros. If either survives refereeing, the protected
subclass is closed, and the programme should turn to the non-(NT) tie designs governed by II2 (★).

---

## 1. Setting and notation

### 1.1 The class

**(H)** (exactly the hypotheses of the sufficient theorem; BRIEF30):
- Φ_i(X) = ∫ φ_i(h, a_X(h)) dμ, with measurable penalties and an integrable envelope E(h). Φ is weakly guiding:
  φ_i(h,a) ≤ φ_i(h,b) whenever a is weakly better than b in world-i rank, for a.e. h.
- p ↦ C_p is a selection of coherent models on Δ, continuous in measure, with T1 = C_{q₀}.
- **(NT)**: for every p and every model X, if Φ_i(X) ≤ Φ_i(C_p) for every i ∈ J := supp p, then X = C_p a.e.

### 1.2 Pairs, orientations and the three sign facts

A pair {g, −g} carries four advices: accept g, silence S, accept −g, and ×. When the pair is indexed by its majority
orientation h (two positive coordinates j, l, one negative coordinate o), "accept h" is called M and "accept −h" is
called O. For an *oriented* gamble g put

  c^g := φ(S) − φ(acc g),  d^g := c^g − c^{−g} = φ(acc −g) − φ(acc g)   (vectors over worlds).

Thus c = c^h, c′ = c^{−h} and d = d^h in II1/JJ3 notation. At a weight α ∈ Δ:
- accept g is the unique minimiser iff α·c^g > 0 and α·d^g > 0;
- S is a weak minimiser iff α·c^g ≤ 0 and α·c^{−g} ≤ 0.

The *chart lines* are {α·c^g = 0}, {α·c^{−g} = 0} and {α·d^g = 0}. They are concurrent, since d^g = c^g − c^{−g}.

**Imported (II1 Prop 5.2(a),(b), PROVED there; re-proved in JJ3 Lemma 1.1).** Under (H):
- C_{e_k} = B^k, the world-k-best model;
- **strict-best**: the world-k-best advice is strictly cheapest at world k, for a.e. pair and every k;
- × may be made strictly worst without loss of generality (this preserves (H)).

From now on × is strictly worst. It is never a weak minimiser at any α ∈ Δ, and it is ignored. Under (H), for a.e.
mixed pair and both orientations g:

- **(F1)** c^g_i > 0 whenever g_i > 0. Accept g is the good advice there, hence strictly best.
- **(F2)** d^g_i has the strict sign of g_i at every i. Of the two acceptances, the good one is strictly best.
- **(F3)** c^g_i ≤ 0 whenever g_i < 0. Accept g is bad there, and silence is weakly better.

Strict guidance would add:

- **(F4)** c^g_i < 0 whenever g_i < 0 (strict badness).

A **zero** at world i for g is the failure of (F4): g_i < 0 and c^g_i = 0, that is φ_i(S) = φ_i(acc g). Every zero is
of one of three kinds.
- **Odd zero.** g has one negative coordinate, i (so g is the majority orientation, and i its odd world).
- **Double zero.** g has two negative coordinates i, k, and c^g_i = c^g_k = 0.
- **Single zero.** g has two negative coordinates i, k, and c^g_i = 0 > c^g_k.

These are II1 Prop 5.4's Z^odd, Z^maj and single positive-world zeros (JJ3 z_o; z_j and z_l together; z_j alone).

---

## 2. The certificate

**Lemma 2.1 (PROVED; CHECKED, `certificate.py` (1)).** Let p ∈ Δ and w ∈ Δ with supp w ⊆ supp p. Suppose that for a.e.
h, C_p(h) is the unique minimiser of w·φ(h, ·) over the advice range. Then (NT) holds at p.

*Proof.* Let X satisfy Φ_i(X) ≤ Φ_i(C_p) for every i ∈ supp p.
- Since w ≥ 0 is supported in supp p, w·Φ(X) ≤ w·Φ(C_p).
- On the other hand, w·Φ(X) − w·Φ(C_p) = ∫ [w·φ(h, a_X(h)) − w·φ(h, a_{C_p}(h))] dμ. The integrand is ≥ 0 a.e., and > 0
  a.e. on {X ≠ C_p}. Integrability comes from the envelope.
- So equality forces μ{X ≠ C_p} = 0. ∎

*Boundary indices.*
- Only supp w ⊆ supp p is used, not equality.
- At p = e_k, necessarily w = e_k. The certificate then says that C_{e_k} is the unique world-k minimiser, i.e.
  C_{e_k} = B^k, which strict-best makes a.e. unique.
- On an edge, w lies on that edge or at one of its ends.

CHECKED: 52 000 exact pure and relaxed records on random finite cell models, for weights at the vertices, on the edges
and in the interior, and for random supports J ⊇ supp w. There were 0 records with Φ_i ≤ 0 at every i ∈ J.

**Lemma 2.2 (PROVED; CHECKED, `certificate.py` (2)).** Let C_p be a pointwise weak α-Bayes model with supp α = J =
supp p. Then (NT) fails at p iff there is a non-null record t out of C_p, supported on the α-tie set, with Φ_i(t) = 0
for every i ∈ J. Here the α-tie set is the set of pairs where C_p(h) is not the unique α-minimiser, and the record
switches to other α-minimisers there.

*Proof.*
- (⇐) Such a record violates (NT).
- (⇒) Let Φ_J(t) ≤ 0 with t non-null. Then α·Φ(t) ≤ 0, while pointwise α·δφ ≥ 0 by weak Bayes optimality.
  - Hence α·δφ = 0 a.e. on supp t, so t switches only along ties.
  - Then Σ_{i∈J} α_iΦ_i(t) = 0 with every term ≤ 0 and every α_i > 0. So Φ_J(t) = 0. ∎

*Reading.* In the abstract cell setting a certificate is sufficient, not necessary.
- Example A: two ties at w = u, with increments (1,−1,0) and (1,0,−1). These satisfy (NT), because the first coordinate
  of every record is ≥ 0, and = 0 only for the trivial record. The same base is then a strict minimiser at the interior
  weight w′ = (53/150, 97/300, 97/300).
- Example B: opposed ties (1,−1,0) and (−1,1,0) give the exact record Φ = 0, and (NT) fails.

On the real domain, Lemma 4.1 shows that tie sets at interior weights are null. So there (NT) and the certificate
coincide at every index whose separating weight can be taken interior.

---

## 3. The key tension, verified and generalised

**Lemma 3.1 (PROVED; CHECKED exhaustively, `certificate.py` (3)).** Let C_q be silent on a non-null set E of pairs. For
a.e. h ∈ E, and for each orientation g of h, (NT) at q requires the following:

  some i ∈ supp q with g_i < 0 and c^g_i < 0.

That is: switching to "accept g" must be strictly costly at an active world where accepting g is bad.

*Proof.* Suppose it fails on a non-null E′ ⊆ E for one orientation g. Switch S → accept g on E′. At every i ∈ supp q
the increment is −∫_{E′} c^g_i:
- it is < 0 where g_i > 0, by (F1);
- it is = 0 where g_i < 0, since c^g_i = 0 there.

So Φ_{supp q} ≤ 0 on a non-null record, against (NT). ∎

Applied to both orientations of a pair (majority h, positive worlds j, l, odd world o):
- for g = h: o ∈ supp q, and no odd zero;
- for g = −h: supp q contains a positive world of h at which −h carries no zero.

At T1 (supp q₀ = Ω) on the brief's pattern g = (+,−,−):
- switching to accept g must be strictly costly at world 2 or 3, so g carries no double zero;
- switching to accept −g must be strictly costly at world 1, so −g carries no odd zero.

The script checks all 7 supports × 8 zero patterns on an exact T1-silent gamble g = (1, −1/2, −1/2) at ε = 1/7. It
confirms that a switch is defended iff the condition holds.

**Corollary 3.2 (PROVED).**
- (a) On pairs carrying an odd or a double zero, no selected model is silent (II1 Prop 5.4(a)).
- (b) On a pair whose orientation g carries a single zero at i (other negative world k, positive world m), every silent
  selected model has {k, m} ⊆ supp q.

  So silence there is forbidden at the three vertices and on the edges [e_i, e_m] and [e_i, e_k]. It is allowed in the
  interior and on [e_k, e_m].

**Lemma 3.3 (zeros force direct competition at an edge; PROVED; CHECKED, `zeros.py` Part A).** Let g carry a zero at i,
and let m be a positive world of g. On the open edge (e_i, e_m) of the weight simplex:
- silence is never a weak minimiser;
- accept g is the unique minimiser between e_m and the point P_d := {α·d^g = 0} ∩ (e_i, e_m);
- accept −g is the unique minimiser between P_d and e_i.

At P_d exactly the two acceptances tie, and both beat S. The d-face {α·d^g = 0 < α·c^g} contains P_d and a
non-degenerate segment of interior weights.

*Proof.*
- On the edge, α·c^g = α_m c^g_m > 0 by (F1) and c^g_i = 0. So S never weakly minimises.
- d^g_m > 0 > d^g_i by (F2). So the d-line meets the open edge at a single point P_d, transversally.
- At P_d, α·c^{−g} = α·c^g − α·d^g = α·c^g > 0, so both acceptances beat S.
- {α·c^g > 0} is open, so a segment of the d-line through P_d stays in it. The d-line is not the edge line (it
  separates e_i from e_m), so that segment enters int Δ. ∎

CHECKED: 3661 (zero, positive world) incidences over 1700 exact random pairs with all zero patterns, 0 failures.

**Theorem 3.4 (edge precision; PROVED from (H) alone).** Fix worlds i ≠ m. Let Z be the set of pairs with an
orientation g such that g_i < 0 < g_m and c^g_i = 0. For h ∈ Z let r(h) ∈ (e_i, e_m) be the point of the edge with
r(h)·g = 0. Suppose μ(Z) > 0.
- (a) For every p ∈ [e_i, e_m], K_p ⊆ [e_i, e_m] and μ{h ∈ Z : r(h) ∈ K_p} = 0.
- (b) Let N := ⋃_{p∈[e_i,e_m]} relint K_p, a relatively open subset of the edge. Then r(h) ∉ N for a.e. h ∈ Z, and
  N^c has positive length.
- (c) The set {K_p : p ∈ [e_i, e_m], K_p a singleton} of precise selected edge models covers a set of positive length.

*Proof.*
- **(a), confinement.** For p on the edge, J = {i, m}. Pairs g′ with g′_i, g′_m > 0 have accept g′ strictly best at
  both active worlds (F1). If C_p did not accept them on a non-null set, switching would decrease Φ_i and Φ_m. So C_p
  accepts a.e. such g′.
  - If m′ ∈ K_p had m′_k > 0 (k the third world), the open set of g′ near (1, 1, −N) with N large would be rejected.
  - Hence K_p ⊆ [e_i, e_m].
- **(a), the null set.** For m′ ∈ [e_i, e_m], m′·g = m′_i g_i + m′_m g_m vanishes only at r(h). So C_p is silent at h
  iff r(h) ∈ K_p. Silence on a non-null subset of Z would contradict Lemma 3.1, since i is the only world of J where g
  is negative, and it carries a zero.
- **(b).** The push-forward ν := r_*(μ|Z) is absolutely continuous on the edge (r is a submersion on each sign cone).
  By (a), ν(relint K_p) = 0 for every p. N is a countable union of such intervals (Lindelöf), so ν(N) = 0. Since
  ν ≠ 0, Leb(N^c) > 0.
- **(c).** Give the edge the coordinate τ ∈ [0,1], with τ = 0 at e_m and τ = 1 at e_i. Let p(s), s ∈ [0,1], run along
  the index edge from e_m to e_i, and write K_{p(s)} = [a(s), b(s)].
  - a and b are continuous (Hausdorff continuity of the selection), with a(0) = b(0) = 0 and a(1) = b(1) = 1.
  - Fix τ ∈ N^c ∩ (0,1) and put s₁ := inf{s : b(s) > τ}. Then s₁ > 0 and b(s₁) = τ: points left of s₁ have b ≤ τ, and
    points right of it, arbitrarily close, have b > τ.
  - If a(s₁) < τ, then for s slightly right of s₁ with b(s) > τ we also have a(s) < τ by continuity. So
    τ ∈ relint K_{p(s)} ⊆ N, a contradiction.
  - Hence a(s₁) = b(s₁) = τ, and K_{p(s₁)} = {τ} is a precise selected model.
  - So N^c ⊆ {τ : K_p = {τ} for some edge index p}, and (b) gives positive length. ∎

*Reading.* Zeros need the selection to be precise along part of the edges adjacent to the zero world, and the zero
ratios must live exactly there.
- Odd zeros need this on both edges at the odd world.
- Single zeros need it on the edge to the positive world.

This is the edge counterpart of Prop 5.4(b) of II1, and it holds for single zeros too.

---

## 4. What (NT) supplies: the full Bayes family

**Lemma 4.1 (PROVED; the same statement is JJ3 Thm 2.1, found independently).** Assume (H). For every w ∈ int Δ:
- every minimiser of w·Φ is a selected model;
- the w-tie set is null;
- the w-Bayes model B_w is a.e. unique, and B_w = D_{K_w}.

*Proof.*
1. **Leading ranking.** Put X ≼_i Y iff Φ_i(X) ≤ Φ_i(Y). It satisfies (LA) and (S) with the given selection:
   - every C_p is coherent and undominated, since a dominating model violates (NT);
   - C_p is competitive on supp p, since (NT) gives some i ∈ supp p with Φ_i(X) > Φ_i(C_p) for every X ≠ C_p;
   - the sections {p : Φ_i(C_p) ≤ Φ_i(X)} are closed, since |Φ_i(C_p) − Φ_i(C_q)| ≤ 2∫_{C_p ≠ C_q} E dμ → 0.
2. **Bayes models are selected.**
   - The write-up's Theorem kkm (Loss Dominance Generalized v2; valid for preorders) makes every undominated model tied
     at every world with a selected C_p. (NT) then gives equality.
   - A w-minimiser B with w ∈ int Δ is undominated: a dominating Y would have w·Φ(Y) < w·Φ(B).
   - So B is selected, hence coherent.
3. **Null ties.** Suppose the w-tie set T is non-null.
   - Let B be a pointwise minimiser, and B′ the pointwise minimiser obtained from B by switching, on E := T ∩ {|h| < R},
     to another minimiser (chosen measurably).
   - Choose R so that E and T ∖ E are both non-null.
   - Both are coherent by step 2. Coherent models are cones (a_{D_K}(th) = a_{D_K}(h) for t > 0), so their disagreement
     set E would be a cone modulo null sets.
   - A cone contained, modulo null sets, in {|h| < R} is null. This is a contradiction. ∎

**Lemma 4.2 (PROVED).** Assume (H).
- (a) w ↦ K_w is Hausdorff-continuous on int Δ, and P(w, g) := min_{m∈K_w} m·g is jointly continuous.
- (b) K_w → {e_b} as w → e_b. Every Hausdorff limit of K_w at an edge weight with support S lies in Δ_S.
- (c) **Every-weight chart identity.** For a.e. g, R(±g) ∩ int Δ = {w ∈ int Δ : P(w, ±g) > 0}. Here R(x) is the open
  convex set of interior weights at which accept x is the unique minimiser.
- (d) For a.e. g and every interior w in the closed d-face of g, K_w ⊆ g^⊥.

*Proof.*
- (a) Fix w. By Lemma 4.1 the tie set at w is null. Off it, the minimiser at w stays the minimiser nearby, so
  B_{w_n} → B_w in measure. R1 Prop 3.1 (refereed) converts this to Hausdorff convergence.
- (b) The e_b-minimiser is B^b, unique a.e. with a positive gap (strict-best). Dominated convergence gives
  B_w → B^b in measure.
  - For the edge: pairs positive at every world of S have accept as their strict minimiser at the edge weight, by (F1)
    at every world of S. Hence every limit set accepts a.e. such gamble, which forces it into Δ_S (as in N21.7(d)).
- (c) This is the write-up's Prop CF (⇒) in its every-q form (refereed twice). Its proof uses only (a), the null tie
  sets of Lemma 4.1 at every interior weight, joint measurability, Fubini, and the convexity of both sets. The latter is
  N21.1 for {P > 0}, and the chart table for R(·). No sign of the penalties enters. (JJ3 Lemma 2.4 writes it out.)
- (d) At such w there are nearby weights in R(g) and in R(−g). By (c) and continuity, P(w,g) ≥ 0 ≥ −P(w,−g). This is
  R4 Thm B (refereed once). ∎

**Lemma 4.3 (PROVED; same as JJ3 Prop 2.5).** Assume (H). There is w* ∈ int Δ with T1 = B_{w*}. Thus T1 is the unique
w*-Bayes model.

*Proof.*
- II1 Prop 3.1(a) (PROVED there: Lyapunov convexity of the leading increments out of T1, separation from the open
  negative orthant, then pointwise switching) gives α ∈ Δ with T1 pointwise weak α-Bayes.
- Suppose α_k = 0. Take the open set of gambles g′ near (1, 1, −t) (relabelled so that k is the third world) with t
  slightly above 2c₀/(c₀+ε). T1 is silent there.
- Accepting is strictly better than silence at both worlds of supp α, by (F1). So T1 is not weak α-Bayes, a
  contradiction.
- At a vertex weight, T1 would equal B^k, which is false.
- So α ∈ int Δ, and Lemma 4.1 gives T1 = B_α. ∎

**Corollary 4.4 (PROVED).** In every (NT) design:
- the interior Bayes family {B_w : w ∈ int Δ} of Φ is a Hausdorff-continuous family of coherent models;
- it has (BU) at every interior weight, contains T1 at an interior weight, has vertex limits {e_b}, and has
  edge-confined limits;
- every B_w is a selected model, certified by Lemma 2.1 with w(p) = w.

**Corollary 4.5 (degenerate credal sets along zero d-faces; PROVED).** For a.e. pair carrying a zero (orientation g,
world i, positive world m of g), there is a non-degenerate segment of interior weights on which K_w ⊆ ℓ_g, so
dim K_w ≤ 1. It lies on the d-line of g and ends at the edge point P_d of Lemma 3.3.

*Proof.* Lemma 3.3 places a non-degenerate segment of the d-face in int Δ. Lemma 4.2(d) applies. ∎

---

## 5. Inactive zeros are invisible; active zeros are intrinsic

**Definition 5.1.** A zero of g at i is **active** if

  I(g) := {α ∈ Δ : α·c^g = 0 > α·c^{−g}}

is non-empty. I(g) is the interface where accept g and silence tie and both beat accept −g. Otherwise the zero is
**inactive**.

**Lemma 5.2 (PROVED; CHECKED, `zeros.py` Part B).** Let g carry a zero at i.
- (a) Odd and double zeros are inactive. For them, S is a weak minimiser at no α ∈ Δ.
- (b) Let the zero be single, with other negative world k and positive world m. Let P be the point where the zero line
  {α·c^g = 0} meets the opposite edge (e_m, e_k), and put π := P·c^{−g}.
  - If π > 0, S is never a weak minimiser on Δ, and the zero is inactive.
  - If π = 0, S is a weak minimiser only at P (a triple tie), and the zero is inactive.
  - If π < 0, the zero is active. Then I(g) is a non-degenerate segment of the line through e_i and P, with interior
    points in int Δ. S is the unique minimiser on a non-empty open set of interior weights (a triangle with two vertices
    on (e_m, e_k)).
- (c) Hence a zero is active iff it is a single zero on a pair whose silence region has interior.

*Proof.*
- (a), odd zero. {α·c^g ≤ 0} ∩ Δ = {e_i}, and c^{−g}·e_i > 0 by (F1) for −g.
- (a), double zero. {α·c^g ≤ 0} ∩ Δ = [e_i, e_k], where c^{−g} > 0 by (F1) for −g.
- (b) c^g_m > 0 > c^g_k and c^g_i = 0. So the zero line runs from e_i to P ∈ (e_m, e_k), and
  {α·c^g ≤ 0} ∩ Δ = co{e_i, P, e_k}.
  - The affine function α·c^{−g} is positive at e_i and at e_k, by (F1) for −g, and equals π at P. So on this triangle
    it is positive except possibly near P. All three cases follow.
  - When π < 0, the set {c^{−g} < 0} cuts the triangle in a sub-triangle at P with two vertices on (e_m, e_k).
- (c) Combine (a) and (b). ∎

This agrees with JJ3 Lemma 3.1: their case (b2) is "active", and their (a) and (b1) are "inactive".

CHECKED: 608 single-zero instances (195 active). Activity equals "silence is the unique minimiser at an interior test
point" in every case. For each active instance, two distinct interior points of I(g) were exhibited, with the stated
tie and collinearity with e_i. 0 failures.

**Proposition 5.3 (rotation removes an inactive zero; PROVED; CHECKED, `zeros.py` Part C).** Let g carry only inactive
zeros, and fix t ∈ (0,1). Replace, on this pair,

  φ(acc g) ↦ φ(acc g) + t c^{−g},  φ(acc −g) ↦ φ(acc −g) + t c^{−g},  φ(S), φ(×) unchanged (× re-raised if needed).

Equivalently, c^g ↦ c^g − t c^{−g}, c^{−g} ↦ (1−t) c^{−g}, and d^g is unchanged: the zero line rotates about the
concurrency point. Then:
- (a) the set of weak minimisers of α·φ(h, ·) is unchanged at **every** α ∈ Δ;
- (b) the new c^g is strictly negative at every negative world of g, and still positive at its positive worlds. The
  zeros of −g, if any, are untouched. Activity is a property of the minimiser sets (Lemma 5.2(c)), which do not change,
  so inactive zeros of −g stay inactive and are removed by the same rotation applied to −g. (If g is a minority
  orientation, the zeros of −g are odd zeros. If g carries an odd zero, silence is never a weak minimiser. Either way,
  the zeros of −g are inactive.);
- (c) the change is bounded by 2E(h), uses one constant t, and is measurable.

*Proof of (a).*
- The minimiser set at α is determined by the signs of α·c^g, α·c^{−g} and α·d^g. The last two signs are unchanged.
- Suppose the sign of α·c^g changes. There are two cases.
  - **Case 1:** 0 ≤ α·c^g ≤ tα·c^{−g}, not both zero. Then α·c^{−g} > 0 and α·d^g = α·c^g − α·c^{−g} ≤ (t−1)α·c^{−g} < 0.
    So accept −g is the unique minimiser before, and also after, since (1−t)c^{−g} and d^g keep their signs.
  - **Case 2:** tα·c^{−g} ≤ α·c^g ≤ 0, not both zero. Then α lies in the closed silence region. By Lemma 5.2 this
    region is empty or equal to {P} with c^g(P) = c^{−g}(P) = 0, so Case 2 never occurs.
- *(b)* At a negative world i of g, c^{−g}_i > 0 by (F1) for −g, so c^g_i − t c^{−g}_i < 0. At the positive world m,
  c^{−g}_m ≤ 0, so c^g_m − t c^{−g}_m ≥ c^g_m > 0.
- *(c)* |c^{−g}| ≤ 2E. ∎

CHECKED (`zeros.py` Part C): 1505 exact instances with every inactive pattern, including 200 deliberately borderline
instances (π = 0). For each, the minimiser sets of the old and rotated fields were compared at every vertex of the
common line arrangement (the six chart lines and the three edges), at every midpoint of two vertices, and at every
centroid of three vertices. This is a complete test: each open face, edge and vertex of the arrangement contains one of
these points, and the minimiser sets are constant on each. All 1505 agree at t = 1/2, and the rotated fields are
strictly guiding. 0 failures.

**Proposition 5.4 (active zeros are intrinsic; PROVED; CHECKED, `zeros.py` Part D).** Suppose the zero of g at i is
active, and Φ″ has, at this pair, the same unique-minimiser regions as Φ in int Δ. Then Φ″ also has c″^g_i = 0. Consequently, take any field Φ″ whose minimiser at every interior weight is a.e. unique
and equal to that of Φ. Then Φ″ carries the same active zeros at a.e. pair of Z^act, the set of pairs carrying an active zero. No strictly guiding field has the
Bayes family of an (NT) design with μ(Z^act) > 0.

*Proof.*
- For the second claim: for each interior w, the two unique minimisers agree for a.e. pair. By Fubini, for a.e. pair
  they agree for a.e. w. The unique-minimiser regions are open and convex, so they then coincide.
- The open segment I(g) ∩ int Δ is the common boundary of R(g) and the silence region, away from R(−g). For Φ″ it must
  lie on {α·c″^g = 0}.
- That line therefore contains a non-degenerate segment of the line through e_i, and so it passes through e_i. ∎

CHECKED: all 195 active instances resist every rotation t = 2^{−1}, …, 2^{−20}. In each case an exact point of the
arrangement shows a changed minimiser set.

**Theorem 5.5 (PROVED modulo Theorem gm and Theorem ccibu).** In every (NT) design, the set of pairs carrying an active
zero is non-null.

*Proof.*
- Suppose a.e. zero is inactive. Apply Proposition 5.3 with t = 1/2 to every zero-carrying pair, for both orientations.
  The new field Φ′ is integrable, strictly guiding and strict-best, and has the same weak-minimiser sets at every
  weight of Δ.
- By Lemmas 4.1 and 4.3, every interior minimiser of Φ′ is a.e. unique and coherent, and T1 is the w*-minimiser.
- The write-up's Corollary realisation (Theorem ccibu, author-checked) makes Φ′ a strictly guiding additive ranking on
  the full domain with (LA), (S), (C), covering T1. This contradicts Theorem gm.
- Without ccibu: Theorem gm's routes use a cover only through Prop necessary (a), (b), (d), the vertex models and (LF)
  (§7, (W1)–(W6)), all of which Φ′ has. ∎

**Corollary 5.6 (the brief's suggested patterns; PROVED modulo the same).** Each of the following zero placements, on a
non-null set Z of pairs, consists a.e. of inactive zeros. So no design consists of them alone.
- (a) No selected model is silent on Z: for every p, μ{h ∈ Z : C_p(h) = S} = 0.
- (b) Every selected model silent on part of Z has the zero world outside its support.
- (c) T1 and every C_p accept or reject on Z, with silence strictly dominated at every relevant weight.

*Proof.*
- In (b), the interior Bayes models are selected (Lemma 4.1) and have full support, so (b) implies (a). (c) is (a).
- Under (a), for every interior w, μ{h ∈ Z : S uniquely minimises at w} = 0, since B_w is selected.
- By Fubini, for a.e. h ∈ Z the open set of interior weights where S uniquely minimises is null, hence empty.
- By Lemma 5.2(c) the zeros of such h are inactive. ∎

*The exact reason, in words.* The brief suggested placing ties where silence is never chosen. A zero is a tie between
silence and a bad acceptance, so if silence is never chosen the tie is never decisive. Its chart line then runs through
the region where the good acceptance wins, and it can be rotated away without changing any Bayes model. The resulting
Bayes family is that of a strictly guiding field, which Theorem gm excludes. Decisive zeros must instead sit where
interior Bayes models are silent (Lemma 5.2(c)), at a world that is active for them (Lemma 3.1).

---

## 6. The remaining pattern, described exactly

**Proposition 6.1 (PROVED; (d) modulo §7).** Let Z^act be the non-null set (Theorem 5.5) of pairs carrying an active
zero: orientation g with negative worlds i, k and positive world m, c^g_i = 0 > c^g_k, and π < 0. Then:
- (a) the interior weights in the silence region of g form an open triangle. The Bayes models there are selected and
  silent on g, and Lemma 3.1 is met (k and m are active and strictly signed);
- (b) the acceptance/silence interface I(g) lies on the line through e_i and P, so on the vertex line through e_i
  (Lemma 5.2);
- (c) by Theorem 3.4, the selected edge models on [e_i, e_m] are precise on a set of positive length carrying r(h) for
  a.e. h ∈ Z^act. By Corollary 4.5, interior credal sets are at most one-dimensional along a d-face segment ending at
  the edge;
- (d) near ∂D_{T1}, Z^act is concentrated at the crossing rays. For every compact subset C of a facet's relative
  interior avoiding its i-crossing ray, Z^act contains no zero at i on a neighbourhood of the cone over C. Zeros at the
  facet's own world k never occur near it (Proposition 7.3).

Before §7, this was the precise residual of the protected subclass on the full domain. §7 closes it.

---

## 7. Theorem gm under weak signs

**Definition 7.1.** A **weak cover** of T1 is a field Φ satisfying (W1)–(W6) below (all supplied by an (NT) design, by
§4).
- (W1) Φ is integrable, additive, weakly guiding and strict-best on the full domain, with × strictly worst. So
  (F1)–(F3) hold.
- (W2) For every q ∈ int Δ the q-minimiser B_q is a.e. unique and equal to D_{K_q}.
- (W3) q ↦ K_q is Hausdorff-continuous on int Δ, and P is jointly continuous.
- (W4) K_{p*} = T1 for some p* ∈ int Δ.
- (W5) K_q → {e_b} at each vertex, the vertex minimisers are B^b, and edge limits are edge-confined.
- (W6) The every-weight chart identity holds, and K_q ⊆ g^⊥ on closed d-faces, for a.e. g (Lemma 4.2(c),(d)).

**Theorem 7.2 (PROVED modulo the imported chain of Theorem gm's short route, at its recorded status; the sign audit
below is part of this proof).** T1 has no weak cover, for any ε ∈ (0,1).

*Proof.* Run the short route of Theorem gm (collar, then Theorem D, then Theorem A) on (W1)–(W6). Every step, with all
its inputs, is listed below. Each entry records where the field's signs enter and why weak guidance suffices.
- "Family" means the step uses only (W2)–(W6) and properties of credal sets.
- (F1)–(F4) are as in §1.2.

**Table 7.2 (the audit).** Sources read for this audit:
- the write-up §§5–6;
- N21 (whole), N28 §§1–4, R10b §§1–5, N12 §§2–3, N14 §2.3, N23 §7, I2 §§1–4, PropD §§1–3;
- the archived round-10 C1 note §§4–5.

| Step | Statement used | Where signs enter | Weak version |
|---|---|---|---|
| S1 | normalisation p* = u, x = x₊ (Prop diag(a), transposition) | rescaling world i's penalties by p*_i | preserves (F1)–(F3) |
| S2 | N21.1 (quasi-concavity), N21.1′, N21.2 = Lemma B1 (half-plane charts on B₁), Lemma raytransfer | none (chart convexity, R4 Thm B, K_q ⊇ K″) | family |
| S3a | R10b UVN(a) | accept h strictly best at e_l when h_l > 0 | (F1) |
| S3b | R10b UVN(b), via Lemma FS | "0 or − is in the advice range; both are strictly better than + at every world of supp q₀" | on the full domain − is available and strictly better by (F1) for −h; the clause for 0 is not needed |
| S3c | R10b Lemma D, Lemma M, Lemma P, Theorem PL, Cor PL2 | Lemma M Step 4: (a₋)_c ≤ 0 "because c(h₋)_c < 0" | only the limit inequality ≤ 0 is used: (F3) |
| S3d | N21.9, Lemma R23.1, Cor R23.2, N28 Lemmas 2.1–2.4, Prop 3.1, Lemmas 3.2–3.4, Thm 3.5: (TS) holds | N28 Prop 3.1 Step 2 and N23 §7.2 Step 3: c-cluster sign n·(e_l − p*) ≤ 0 when h_l < 0 | (F3) |
| S4 | N21.4 items 1–8: pivot chords, no sliding, rotation, regularity, blow-up, (PC), (NS) | item 5: ĉ·e_i ≤ 0 from c(g_m)_i < 0 | (F3); the non-constancy argument needs only ">0 on one side, ≤0 on the other" |
| S5 | N12 Thm 3.1 items 3–5 (crossing rows λ_{ik} > 0, rank 2, corner equation); Prop boxbridge; Prop T1 | item 3: weak vertex signs plus non-collinearity | (F3); the facet algebra is CHECKED (`t1_facts.py`) |
| S6 | Lemma veccluster | "ĉ ∦ 𝟙 since ĉ has the weak sign pattern of h" | (F1), (F3) |
| S7 | facet-map sign at a positive coordinate (used in collar (a)) | c_k(h)_b = λ_{bk}h_b > 0 when h_b > 0 | S5 |
| S8a | chart-form edge box (N14 §2.3), inside Thm cuts Step 1 | "R(g) ⊆ {c·q > 0} or R(g) ⊆ {d·q > 0}, c, d strictly signed" | use d: R(g) ⊆ {d^g > 0}, and d^{A+λB} < 0 on the closed edge by (F2). (F4) is not needed |
| S8b | Thm cuts (N21.6) Step 2: α(e_a) < 0 (A-case), α(e_b) < 0 (B-case) | strict badness (F4) at a vertex | A-case: near w′ every good g has c(g)_a < 0, since by S6 c(g)/|c(g)| → c_a(w′)/|c_a(w′)| and c_a(w′)_a < 0 (CHECKED). B-case: with c(g)_b = 0 the α-line meets the edge at σ = e_b instead of in (e_b, q₀); Steps 3–7 use only d(σ) < 0 (F2) and σ_m → e_b, both unchanged |
| S8c | Thm cuts Steps 3–7, test gambles w* − δ𝟙 + ηe_b | "{α ≤ 0} contains points near some e_l with g_l < 0, where d < 0"; vertex and edge forcing | (F2); the half-neighbourhood still exists if α(e_l) = 0; (F1) for forcing |
| S9 | Thm apex (N28 4.1), Prop vertexfree (N28 4.3), Lemma R1N28, Lemma walls | none | family |
| S10 | Lemma nostraddle (I2 Lemma 1) | c(g)·q > 0 ⇒ q ∉ silence cell | no sign; uses S6 and (W6) |
| S11 | Theorem collar (I2 Thms 2–3) | (a): S7 at e_b, (W5), N21.1′; (b): box certificate, superadditivity, edge confinement | S7; the box certificate is CHECKED exactly for four values of ε (`t1_facts.py` (5)) |
| S12 | Theorem D (PropD Lemmas 1.1(b), SL, Z, 2–4) | condition (C) = (DL): "ℓ_i(g,+) < ℓ_i(g,−) when g_i > 0, and the reverse when g_i < 0" | this is (F2) |
| S13 | σ constant on the collar is excluded | Prop vertexfree(i) | family (S9) |
| S14 | Theorem A (C1 Lemmas 4.1–4.3, 5.0, Thm A) | Lemma 5.0 Step 4: "Aᵀg has the strict sign pattern of g" via d(g) | (F2) |

With the table, the short route gives the contradiction verbatim:
- S11 gives a precise collar O_b;
- S12 gives σ constant or σ_w on it;
- S13 excludes constant σ;
- S14 excludes injective σ_w. ∎

*Remarks on the audit.*
- Strict badness (F4) occurs in its strict form in exactly two places, S8a and S8b. Both are replaced as stated. Every
  other occurrence is a closed-side statement or a limit, for which (F3) suffices.
- No step uses (S) or (C) of a cover except through Prop necessary (a), (b), (d), which (W2), (W4) and (W5) supply.
  Corollary TSalways(b), "both acceptances in the advice range", holds trivially on the full domain. Corollary
  TSalways(c) is (W5).
- N15's U-domain chain, R1, R4 and C2 were not re-read. The general-domain local chain enters through N21.4, whose edit
  list was read item by item. R4 Thm B and R1 Prop 3.1 are used only as stated, and contain no field signs.

**Proposition 7.3 (zeros near ∂D_{T1}; PROVED modulo S4–S6; algebra CHECKED, `t1_facts.py` (3)).** In every weak cover:
- (a) for every facet F_k there is a conic neighbourhood of each compact subset of relint F_k in which a.e. good gamble
  has c(g)_k < 0;
- (b) for l ≠ k, the same holds for c(g)_l of the right sign, on neighbourhoods of compact subsets of relint F_k that
  avoid the l-crossing ray.

So, near the facets, zeros at l can accumulate only at the l-crossing rays, whose chords line(p*, e_l) pass through e_l
anyway.

*Proof.* If good g_m with a zero at l converged to h ∈ relint F_k, then c(g_m)_l = 0 for all m. Lemma veccluster (S6)
then gives c_k(h)_l = 0.
- For l = k this contradicts c_k(h)_k < 0 on the closed facet segment.
- For l ≠ k, c_k(h)_l = λ_{lk}h_l with λ_{lk} > 0 vanishes only at the crossing. ∎

**Theorem 7.4 (PROVED modulo the imported chain of Theorem gm's short route; uses Lemma 4.1–4.3 and Theorem 7.2).**
Assume (H) on the full domain. Then there is no such design: no integrable weakly guiding additive leading field with a
coherent selection, continuous in measure, through T1, satisfying (NT). In particular:
- the hypotheses of the sufficient theorem (II1 Thm 4.1, II2 Cor 2.4) are never met for T1;
- II1's question P_w has the answer NO.

*Proof.* By §4, an (NT) design is a weak cover. Theorem 7.2 excludes weak covers. ∎

*Two routes to Theorem 7.4.*
- (i) Theorem 7.2 directly. This is the only route needed.
- (ii) Theorem 5.5 removes every inactive zero and reduces the claim to Z^act. Z^act is then excluded either by
  Theorem 7.2, or by JJ3 §4 (elementary, parallel, not refereed).

Route (ii) shows exactly what the transfer must handle: the active single zeros of §6, which by Proposition 5.4 no
strictly guiding field reproduces.

---

## 8. What this says about the programme

1. **The construction target is empty.**
   - The brief's freedoms do not help: joint design of Φ and family, Bayes optimality away from the label,
     reindexing, degenerate credal sets, and asymmetric or discontinuous penalties.
   - By Lemma 4.1, (NT) collapses them. The selected family must contain the whole interior Bayes family of Φ, with
     unique minimisers at every interior weight. Reindexing can only reach boundary-certified models.
2. **Where the strict-badness requirement lived.**
   - On the U-domain (II1 Prop 5.1) there is no rejecting advice. There d is unavailable, and strict badness is what
     the chain needs.
   - On the full domain, d's strict signs, which follow from (NT) at the vertices, replace it everywhere. That is why the
     bad~silence zeros of II1 Prop 5.2 are no escape.
3. **The lifting theorem remains a valid sufficient condition.** JJ1 finds it correct. It is vacuous for T1 on the full
   domain. The negative theorem closes only the protected subclass (AUDIT_II recommendation 6).
4. **The remaining branch is the non-(NT) designs.**
   - There Lemma 4.1 fails: undominated leading-level models need not be selected, because Ψ breaks their ties.
   - So the leading Bayes family can have non-null ties at interior weights. Prop 3.1 and Cor 3.4–3.6 of II1 and II2's
     (★) govern them.

---

## 9. Status

| Item | Statement | Label |
|---|---|---|
| 2.1 | certificate (supp w ⊆ supp p) ⇒ (NT), boundary included | PROVED; CHECKED (52 000 records) |
| 2.2 | at a full-support weak-Bayes weight, (NT) fails iff a tie record has zero leading increment; certificate not necessary abstractly | PROVED; CHECKED (Examples A, B) |
| 3.1 | BRIEF30's tension, for every support | PROVED; CHECKED (7 supports × 8 patterns) |
| 3.2 | silence and zero types: where silent selected models may sit | PROVED |
| 3.3 | every zero forces direct competition at the edge (e_i, e_m), with a d-face entering int Δ | PROVED; CHECKED (3661 incidences) |
| 3.4 | edge precision: zero ratios live on precise selected edge models of positive length | PROVED (from (H) alone) |
| 4.1 | (NT) ⇒ every interior minimiser selected, null ties, (BU) at every interior weight | PROVED (Theorem kkm imported) |
| 4.2 | continuity, vertex and edge limits, every-weight chart identity, Thm B form | PROVED (R1 Prop 3.1, Prop CF proof imported) |
| 4.3 | T1 = B_{w*}, unique, w* interior | PROVED (II1 Prop 3.1(a) imported) |
| 4.5 | degenerate credal sets along zero d-faces | PROVED |
| 5.2 | active ⟺ single zero with π < 0 ⟺ silence uniquely chosen at interior weights | PROVED; CHECKED (608 cases) |
| 5.3 | rotation by any t ∈ (0,1) removes every inactive zero, all minimiser sets on Δ unchanged | PROVED; CHECKED (1505 cases, complete test sets) |
| 5.4 | active zeros cannot be removed by any field with the same interior Bayes models | PROVED; CHECKED (195 cases) |
| 5.5 | every (NT) design has a non-null set of active zeros | PROVED mod Theorem gm and Theorem ccibu (or gm alone, via §7) |
| 5.6 | the brief's three suggested placements are inactive, hence excluded | PROVED mod the same |
| 6.1 | exact description of the residual (active single zeros) | PROVED ((d) mod §7) |
| 7.2 | no weak cover of T1 (gm's short route under weak signs) | **PROVED mod the imported chain; audit Table 7.2** |
| 7.3 | zeros near ∂D_{T1} only at crossing rays | PROVED mod S4–S6; CHECKED algebra |
| **7.4** | **no (NT) design through T1 on the full domain; P_w = NO** | **PROVED mod gm's short-route chain, via 7.2** |
| — | cover of T1 | **not obtained; the protected subclass is empty** |

**Referee priorities.**
1. Table 7.2, S8a and S8b: the only two strict uses of strict badness.
2. The claim, made in the remarks after Table 7.2, that the short route uses a cover only through (W1)–(W6).
3. Lemma 4.1 step 3: the disagreement set of two coherent models is a cone modulo null sets.
4. Proposition 5.3, Case 2: that the closed silence region of an inactive zero is ∅ or the single triple-tie point P.
5. Theorem 3.4(c): the infimum argument giving a precise edge model at every point of N^c.

## 10. Files (`jj2py/`)

- `common.py`: exact helpers, random strict-best weakly guiding pair fields with prescribed zeros, and the complete
  arrangement test set (vertices, midpoints, centroids).
- `certificate.py` → `certificate.out`: Lemma 2.1 on 52 000 records; Examples A and B of Lemma 2.2; Lemma 3.1
  exhaustively on a T1-silent (+,−,−) gamble at ε = 1/7.
- `zeros.py` → `zeros.out`:
  - Part A: Lemma 3.3, 3661 incidences.
  - Part B: Lemma 5.2, 608 single zeros, 195 active.
  - Part C: Proposition 5.3, 1505 removals at t = 1/2, including 200 borderline cases, complete comparison.
  - Part D: Proposition 5.4, 195 active zeros resist all rotations.
- `t1_facts.py` → `t1_facts.out`: at ε ∈ {1/19, 1/7, 4/13, 16/31} (x₊ = 3/2, 2, 3, 5), it checks:
  - the corner equation and x₊² > κ;
  - the facet maps: c_k(h)_k < 0 on the closed facet, and crossing rows vanishing exactly at the crossings;
  - the A-case sign c_a(w′)_a < 0 and the B-case crossing row c_c(w)_b = 0;
  - explicit exact box certificates for the three failing pairs at s = 1/100 and 1/1000 (and at s = 1/10 except for
    ε = 16/31, where s = 1/10 is not yet small).
