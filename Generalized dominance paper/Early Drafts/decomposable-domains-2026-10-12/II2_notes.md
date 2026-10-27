# II2 (round 37, BRIEF29, adversarial side). Can the exchange-rate class meet (RB)? Where defeating competitors must come from, what (RB) forces, and the one regime in which it holds automatically

18 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: floating point or sampling. Nothing below uses NUMERICS.
- **CONJECTURE**: none is offered.

Scripts are in `ii2py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All
arithmetic is `fractions.Fraction`.

Setting: BRIEF29 and AUDIT_HH_rate.md. Three worlds; T1 the ε-contamination of u, any ε ∈ (0,1); notation of the
write-up §2 and of HH2 §§1, 4, 6. Sections 1–3 hold on any decomposable domain. Section 4 is on the full four-advice
domain, which is HH2's setting and the domain of FF2 Theorem 4.1. Each result states its hypotheses. Every hypothesis
is a defining property of the class being examined or a hypothesis of that result. No assumption is added.

**The class.** World i has a base (Φ_i, Ψ_i) of additive levels with integrable envelopes: Φ_i weakly guiding,
Ψ_i strictly guiding. The selection p ↦ C_p consists of coherent models, is continuous in measure on Δ, and passes
through T1 (T1 = C_{q₀}). The rate rule is the one in BRIEF29. By AUDIT_HH_rate.md (PROVED there), a continuous
positive rate k with k → ∞ at 0 makes every C_p competitive on supp p exactly when

  (RB) for every a > 0, sup{ r(p,X) : p ∈ Δ, X evaluable, μ(supp rec(C_p,X)) ≥ a } < ∞,

with r(p,X) = min_{i∈supp p} r_i(p,X) and r_i as in the audit. Admissibility (every C_p undominated in the
lexicographic base) and T1 undominated are also in the class. **None of the obstructions below uses them.**

---

## 0. Outcome

**The target theorem, "(RB) fails for every base in the class", is not proved. Any such theorem would have to
contain a new exclusion of additive covers by weakly guiding fields.** The reason is Corollaries 2.3–2.4: (RB) holds
automatically when the leading level alone strictly protects every selected model, and in that case the rate rule
gives a full (FC) cover of T1. What is proved:

1. **The audit's natural adversary does not exist (Corollary 2.2; PROVED).** Take records of size ≥ a whose leading
   increments tend to 0 (of either sign) while every lower-level increment stays ≤ −c < 0 at every active world.
   Such records occur only if some selected model is already lexicographically beaten at all its active worlds by a
   single competitor. Compactness of the attainable set (Lemma 1.1) and continuity in measure force this.

2. **Where defeating competitors must come from (Theorem 2.1; PROVED).** Every sequence that defeats (RB) has a
   limit. That limit is a record of size ≥ a out of a selected model, at a limit index p\*, whose leading increment is
   ≤ 0 at every world that stayed active. Call it a **leading-nonpositive record**.

   The correct adversary is therefore a pair:
   - tiny leading **improvements** (Φ_i < 0) at the worlds where the limit record is lower-level-nonimproving;
   - tiny leading costs, with a substantial lower-level gain (Ψ ≤ −c), only at the other worlds.

3. **The regime where (RB) is automatic (Corollaries 2.3, 2.4; PROVED, the second modulo HH2 Prop 6.1 and the
   transitivity-free KKM argument, both judged sound in AUDIT_HH_rate.md).**
   - Call C_p **strictly leading-protected (SLP)** if no non-null record out of C_p has Φ_i ≤ 0 at every
     i ∈ supp p.
   - If every C_p is SLP, then (RB) holds.
   - In that case the rate system is a full (FC) cover of T1: (IB), strict (G), (FC), closed sections,
     competitiveness, every C_p undominated, (C), (LF), and T1 ∈ C_L.
   - **The exchange-rate class therefore contains a cover of T1 whenever there is a weakly guiding integrable additive
     field Φ that strictly protects a selection continuous in measure through T1.** Ψ is then only a tie-breaker.

   This is the precise sense in which the base is "effectively Archimedean": it has one real endorser, Φ. But Φ is
   only weakly guiding. FF2 Theorem 4.1, Theorem gm and the intersection theorem all need **strictly** guiding fields,
   so none of them excludes this regime. (They do exclude strictly guiding Φ: Proposition 4.4.)

4. **Exact criterion at a fixed index (Theorem 3.1; PROVED).**
   - If C_p fails the condition (★_p) below, explicit competitors of fixed size defeat every rate, with r ≥ c/s
     along a segment.
   - (★_p): for every leading-nonpositive record z of positive size, C_p is a pointwise weak Bayes model of the
     leading field Φ at a weight supported on I^≥(z) = {i ∈ supp p : Φ_i(z) = 0, Ψ_i(z) ≥ 0}.
   - (RB) implies (★_p) at every p.
   - A strict form of (★_p) is sufficient at that index. The only gap is worlds where the limit record has both
     increments 0.
   - Across indices one more condition is needed (Proposition 3.2): leading improvability must not appear faster
     than transported leading costs.

5. **Obstruction theorem (Theorem 4.1; PROVED modulo FF2 Thm 4.1's import chain).** Suppose (RB) holds. Then there
   are distinct worlds i, j and a neighbourhood V of e_j with two properties:
   - every interior selected model indexed in V pays a leading cost at world i;
   - Φ_i is **strictly** signed at world i along every step towards acceptance (O→S, O→M, S→M) out of those models'
     advice, a.e. on gambles whose only negative coordinate is i.

   Consequently (Corollary 4.2) (RB) fails for:
   - every base whose leading levels are blind at the odd world along such steps near every vertex;
   - in particular, **every one-sided (veto-type) leading charge** (charges only wrong acceptances), with any
     selection whose interior credal sets lie in the open simplex, the plain posterior family included;
   - every **missed-gain charge** (charges only failure to accept the good orientation);
   - for the plain posterior family, every leading level that is flat between O and S, or between S and M, on any
     near-coordinate cone {h_i < 0 < h_j, h_l < η₀|h_i|} (Corollary 4.3; inputs CHECKED).

   Proposition 4.4: a strictly guiding Φ already fails lexicographic competitiveness. Corollary 2.5: no base in the
   class meets (RB) with a bound that is uniform in a.

6. **(IB) and (FC) are not used at all.** Nor are closed sections, (C), admissibility, T1's undominatedness, or the
   form of the rate rule beyond the audit's criterion. The obstructions are statements about competitiveness of a
   continuous selection through T1 for the base alone. (IB), (FC) and closed sections appear only as **conclusions**
   in Corollary 2.4.

**Single most important open point.** Is there a weakly guiding, integrable, additive field Φ (three worlds, full
domain) such that some selection continuous in measure through T1 is strictly leading-protected at every index?
- By Lemma 5.2 such a Φ must be strictly signed at the singly-worsened world along the steps that selected models
  use, and at one of the two worsened worlds along two-world worsenings.
- Its non-strictness, which Proposition 4.4 requires, must therefore sit at improved worlds, or at one positive world
  at a time.

A **yes** is a full (FC) cover of T1 by Corollary 2.4. A **no** needs an extension of the FF2 Thm 4.1 chain (D1,
BB2 Thm 6.1, M3.7–M3.8) to such fields. It would leave only bases that are not SLP, which must satisfy (★) at every
index.

---

## 1. Notation and two basic facts

**Records and increments.** For an evaluable X and an index p, write t = rec(C_p, X). Its **size** is
m(t) := μ{h : X(h) ≠ C_p(h)}, pairs indexed by H as in write-up §2. For an additive level F with penalty f, put
F(t) := ∫ (f(h, X(h)) − f(h, C_p(h))) dμ. Each world i has increments Φ_i(t) and Ψ_i(t).

**Attainable set.** Let Z_p ⊂ ℝ⁷ be the set of vectors (m(t), Φ_1(t), Φ_2(t), Φ_3(t), Ψ_1(t), Ψ_2(t), Ψ_3(t)) over
evaluable X. A point of Z_p is a "record (value) out of C_p".

**Leading-nonpositive records and leading weights.** Let J := supp p.
- G(p) := {z ∈ Z_p : Φ_i(z) ≤ 0 for all i ∈ J}.
- W^Φ(p) := {w ∈ Δ : for a.e. h and every advice b in the advice range, Σ_i w_i(φ_i(h,b) − φ_i(h,C_p(h))) ≥ 0}.
  These are the weights at which C_p is a pointwise weak Bayes model of the leading field.
- For z ∈ G(p), I^≥(z) := {i ∈ J : Φ_i(z) = 0 and Ψ_i(z) ≥ 0}.

**(SLP_p)** C_p is strictly leading-protected: every z ∈ G(p) has m(z) = 0, i.e. z = 0.

**Lemma 1.1 (PROVED).**
- (a) Z_p is compact and convex.
- (b) Let p_n → p and let D_n be the set of pairs on which C_{p_n} and C_p advise differently. For every additive
  level F with integrable envelope e_F,
  |F(rec(C_{p_n},X)) − F(rec(C_p,X))| ≤ 2∫_{D_n} e_F dμ and |m(rec(C_{p_n},X)) − m(rec(C_p,X))| ≤ μ(D_n),
  uniformly in X. Both bounds tend to 0.

*Proof.*
- **(a)** Z_p is the set of integrals of measurable selections of the multifunction h ↦ {f(h,b) : b ∈ A(h)}, where
  f(h,b) := (1[b ≠ C_p(h)], φ(h,b) − φ(h,C_p(h)), ψ(h,b) − ψ(h,C_p(h))) and A(h) is the advice range.
  - The values are finite sets, the multifunction is measurable (Remark advicerange of the write-up), and it is
    integrably bounded.
  - μ is non-atomic and finite. So the integral is convex (Lyapunov; Aumann 1965) and compact (closed values,
    integrable bound; Aumann 1965, Thm 4).
  - A measurable selection of the values is induced by a measurable advice choice: take the first admissible advice,
    in a fixed order, that realises the value. By decomposability that advice choice is an evaluable model (write-up
    Remark advicerange). This is FF2 Step 1's convexity, now with the size coordinate.
- **(b)** The two records differ only on D_n, where the integrands differ by at most 2e_F, respectively by 1.
  Continuity in measure gives μ(D_n) → 0: the advice at a pair is determined by membership of h and −h, and μ is
  symmetric. Absolute continuity of the integral of e_F does the rest. ∎

**Lemma 1.2 (PROVED).** If (RB) holds, then:
- (a) every C_p is lexicographically competitive on supp p: every X has some i ∈ supp p with
  (Φ_i, Ψ_i)(rec(C_p,X)) ≥_lex 0;
- (b) on the full domain, C_{e_j} = B^j := {g : g_j > 0} a.e. for every j.

*Proof.*
- **(a)** r_i(p,X) = ∞ exactly when Φ_i(t) < 0, or Φ_i(t) = 0 and Ψ_i(t) < 0. That is exactly a strict lexicographic
  improvement at i. If this held at every i ∈ supp p, then X ≠ C_p, and the supremum in (RB) at a = m(t) > 0 would be
  infinite.
- **(b)** B^j is pointwise world-j best and evaluable. Apply (a) at e_j against X = B^j:
  - Φ_j(B^j) ≤ Φ_j(C_{e_j}), by weak guidance;
  - so lexicographic acceptance forces equality, and Ψ_j(B^j) ≥ Ψ_j(C_{e_j});
  - strict guidance of Ψ_j then forces C_{e_j} = B^j a.e. ∎

---

## 2. Where defeating sequences come from

**Theorem 2.1 (PROVED).** Let Φ, Ψ be additive with integrable envelopes (no guidance property is needed). Let the
selection be continuous in measure. Suppose a > 0 and (p_n, X_n) satisfy m(t_n) ≥ a and r(p_n, X_n) → ∞, where
t_n = rec(C_{p_n}, X_n). Then along a subsequence:
- supp p_n = J is constant and p_n → p\*, with supp p\* ⊆ J;
- there is an evaluable X\* such that z\* := rec(C_{p\*}, X\*) satisfies
  m(z\*) ≥ a, Φ_i(z\*) = lim Φ_i(t_n) ≤ 0 for all i ∈ J, and Ψ_i(z\*) = lim Ψ_i(t_n);
- Ψ_i(z\*) ≤ 0 for every i ∈ J at which Φ_i(t_n) ≥ 0 for infinitely many n.

In particular z\* ∈ G(p\*) and m(z\*) ≥ a.

*Proof.*
1. **Leading increments vanish from above.** Let E := 2 max_i ∫ e_{Ψ_i} dμ, so that |Ψ_i(t)| ≤ E for every record.
   Fix i ∈ supp p_n and suppose r_i(p_n, X_n) ≥ R > 0.
   - If Φ_i(t_n) > 0, then −Ψ_i(t_n) ≥ RΦ_i(t_n), so 0 < Φ_i(t_n) ≤ E/R and Ψ_i(t_n) < 0.
   - If Φ_i(t_n) = 0, then Ψ_i(t_n) < 0, since r_i = 0 otherwise.
   - Otherwise Φ_i(t_n) < 0.

   So Φ_i(t_n) ≤ E/r(p_n, X_n) → 0 at every active world. Ψ_i(t_n) < 0 whenever Φ_i(t_n) ≥ 0.
2. **Transfer to the limit index.** Pass to a subsequence with constant support J and p_n → p\*. Put
   t′_n := rec(C_{p\*}, X_n). By Lemma 1.1(b), every increment and the size of t′_n differ from those of t_n by o(1).
3. **Compactness.** t′_n ∈ Z_{p\*}, which is compact (Lemma 1.1(a)). A further subsequence converges to some
   z\* ∈ Z_{p\*}, realised by some evaluable X\*. The limits are as stated. ∎

**Corollary 2.2 (the audit's adversary; PROVED).** Suppose there are a, c > 0 and (p_n, X_n) with m(t_n) ≥ a,
Φ_i(t_n) ≤ η_n → 0 and Ψ_i(t_n) ≤ −c at every i ∈ supp p_n. Then some selected model C_{p\*} is lexicographically
beaten at every world of supp p\* by a single competitor X\*. So such sequences exist only when (RB) already fails
for one competitor of one selected model, by Lemma 1.2(a).

*Proof.* Steps 2–3 of Theorem 2.1 use only the convergence of the increments. They give z\* ∈ Z_{p\*} with
Φ_i(z\*) ≤ 0 and Ψ_i(z\*) ≤ −c < 0 for all i ∈ J ⊇ supp p\*. At each i ∈ supp p\*, either Φ_i(z\*) < 0, or
Φ_i(z\*) = 0 and Ψ_i(z\*) < 0. Either way z\* is a strict lexicographic improvement at i. ∎

*Reading.*
- The brief asked for a proof that attainable sets "must contain points with Φ_i ≥ 0 tiny and Ψ_i ≤ −c < 0 at all
  active worlds". They cannot, unless the base is not even lexicographically competitive.
- In any genuine defeating sequence, some active worlds are beaten by **tiny leading improvements** (Φ_i < 0). Only
  the remaining worlds are beaten by rate (Φ_i > 0 tiny, Ψ_i bounded away from 0).
- At the limit the first kind of world has Φ_i(z\*) = 0, and Ψ_i(z\*) may be **positive**. That is the lexicographic
  discontinuity: Φ_i < 0 → 0 with Ψ_i > 0 converges to a strict lexicographic worsening.

**Corollary 2.3 (PROVED).** If every selected model is SLP, then (RB) holds.

*Proof.* A failure of (RB) gives, by Theorem 2.1, a non-null z\* ∈ Z_{p\*} with Φ_i(z\*) ≤ 0 for every
i ∈ J ⊇ supp p\*. This contradicts SLP at p\*. ∎

The proof is not quantitative. In a polyhedral surrogate (`segment_examples.py`, part (3)) the bound comes from the
exact protection margin c(a) := min{max_{i∈J} Φ_i(z) : z ∈ Z_p, m(z) ≥ a} > 0, which gives r ≤ E/c(a) (CHECKED there:
c(a) = a/5).

**Corollary 2.4 (PROVED, modulo HH2 Prop 6.1(a)–(d), the transitivity-free KKM argument, and the audit's rate
criterion).** Let the base and selection be as in the class, on the full domain. Suppose every C_p is SLP. Let k be
the rate supplied by (RB) (Corollary 2.3 and the audit's criterion). Then the rate system 𝒜^k is a full (FC) cover
of T1.

*Proof.*
- **Base properties.** HH2 Prop 6.1 gives reflexivity, (IB), strict (G), (FC), and closed sections, the last because
  the selection is continuous in measure. Competitiveness is (RB).
- **Every C_p is undominated.** Suppose X ≠ C_p satisfies X ≼_i C_p at every world. Then rec(X, C_p) is accepted at
  every world, hence lexicographically accepted: Φ_i(X) ≤ Φ_i(C_p) for every i. So rec(C_p, X) has Φ_i ≤ 0 on
  supp p and is non-null, contradicting SLP. Thus every C_p ∈ C_L, and T1 = C_{q₀} ∈ C_L.
- **(C).** Ties in 𝒜^k are lexicographic ties (HH2 6.1(c)), and SLP excludes non-trivial lexicographic ties with
  any C_p. Let B be undominated.
  - The KKM argument, valid without transitivity (AUDIT_HH_rate.md), gives p with C_p ≼_i B at every world. No
    comparison is strict, since B is undominated, so B is tied with C_p and B = C_p.
  - Hence C_L is the selected family. A model tied at every world with some C_p equals C_p.
- **(LA), (LF).** (LA) is immediate. (LF) at T1 holds on the full domain. ∎

**Corollary 2.5 (PROVED modulo FF2 Thm 4.1's chain).** No base in the class satisfies sup over all a > 0 of the (RB)
bounds being finite.

*Proof.* A finite overall bound K makes the constant rate K competitive. Rate acceptance implies Ψ_i + KΦ_i ≥ 0.
The field Ψ + KΦ is strictly guiding with integrable envelope. So FF2 Thm 4.1 applies with ℓ = Ψ + KΦ, giving a
contradiction. This is HH2 6.1(e) in the language of (RB). ∎

So in every member of the class that meets (RB), the required rate must diverge at small sizes. Under SLP this
divergence comes from records that hug the tie surfaces of the leading level, where the protection margin c(a) of
Corollary 2.3 degenerates.

---

## 3. The exact criterion at one index

**Theorem 3.1 (PROVED).** Fix p and J = supp p.

- **(a) Segment competitors.** Let z\*, z′ ∈ Z_p with m(z\*) > 0, z\* ∈ G(p), and Φ_i(z′) < 0 for every
  i ∈ I^≥(z\*). For s ∈ (0,1) let X_s be an evaluable model with value z_s := (1−s)z\* + s z′ ∈ Z_p (Lemma 1.1).
  Then m(X_s) ≥ (1−s)m(z\*), and r(p, X_s) ≥ c/s for small s, for some c > 0 (possibly r = ∞). Hence (RB)
  fails.
- **(b) Necessity.** Consequently (RB) implies:

  (★_p) for every z ∈ G(p) with m(z) > 0, some w ∈ W^Φ(p) has supp w ⊆ I^≥(z).

  Conversely, if (★_p) fails, the competitors of (a) exist. In particular (★_p) contains lexicographic
  competitiveness against G(p), since I^≥(z) ≠ ∅.
- **(c) Sufficiency at this index.** Suppose every z ∈ G(p) with m(z) > 0 admits w ∈ W^Φ(p) such that
  Φ_i(z) = 0 < Ψ_i(z) for all i ∈ supp w. (Call this the strong form (★★_p).) Then
  sup{r(p,X) : m(rec(C_p,X)) ≥ a} < ∞ for every a > 0.

*Proof.*
- **(a), sizes.** m is a linear coordinate on Z_p, so m(z_s) = (1−s)m(z\*) + s m(z′).
- **(a), rates.** Take i ∈ J.
  - If Φ_i(z\*) < 0: Φ_i(z_s) < 0 for small s, so r_i = ∞.
  - If i ∈ I^≥(z\*): Φ_i(z_s) = sΦ_i(z′) < 0, so r_i = ∞.
  - If Φ_i(z\*) = 0 and Ψ_i(z\*) < 0: Ψ_i(z_s) → Ψ_i(z\*) < 0 and Φ_i(z_s) = sΦ_i(z′). Then r_i = ∞ if Φ_i(z′) ≤ 0,
    and r_i ≥ |Ψ_i(z\*)|/(2sΦ_i(z′)) otherwise, for small s.
- **(b).** Let I := I^≥(z) for a z ∈ G(p) with m(z) > 0.
  - If no z′ ∈ Z_p has Φ_i(z′) < 0 for all i ∈ I, the convex set {(Φ_i(z′))_{i∈I} : z′ ∈ Z_p} misses the open
    negative orthant of ℝ^I.
  - Separation gives w ∈ Δ supported in I with w·Φ ≥ 0 on Z_p. The measurable-switching argument of FF2 Step 1
    makes this pointwise, so w ∈ W^Φ(p).
  - If I = ∅, any z′ works in (a): z_s with z′ = z\* is a lexicographic improvement at every active world.
  - Conversely, such a w excludes z′, since w·Φ(z′) ≥ 0.
- **(c).** Suppose z_n ∈ Z_p with m(z_n) ≥ a and r(z_n) → ∞.
  - By compactness, a subsequence converges to some z ∈ G(p) with m(z) ≥ a (Theorem 2.1 with p_n ≡ p).
  - Take w as in (★★_p). For large n, Ψ_i(z_n) > 0 for every i ∈ supp w. Since r_i(z_n) → ∞ and r_i = 0 when
    Φ_i ≥ 0 and Ψ_i > 0, we get Φ_i(z_n) < 0 for all i ∈ supp w.
  - Then w·Φ(z_n) < 0, contradicting w ∈ W^Φ(p). ∎

*Reading.*
- (★_p) is a **lexicographic Bayes condition on the leading-nonpositive face**. Lexicographic competitiveness only
  asks that each z ∈ G(p) leave **one** world i with Φ_i(z) = 0 ≤ Ψ_i(z).
- (★_p) asks more: that world's position must be backed by a weight at which C_p is leading-weak-Bayes, and **every**
  world in the support of that weight must be Ψ-nonimproved by z.
- If W^Φ(p) is a single interior weight, (★_p) says C_p is Ψ-optimal **at every world** among leading-nonpositive
  records, which is a unanimity condition.
- GG1 Lemma 2.2 (competitive, Bayes at no weight) fails (★): W^Φ = {w₁ ≥ 2w₂}, and z\* = b has I^≥ = {2}. The
  segment of (a) gives r = (1−s)/s at size 1 (CHECKED, `segment_examples.py` part (1)).
- **The gap in (b)/(c).** The gap is worlds i ∈ supp w with Φ_i(z) = Ψ_i(z) = 0. There the verdict depends on how
  Z_p curves at z, that is, whether tangential approaches with Φ_i = o(|Ψ_i|) exist. Smooth densities produce curved
  zonoids; polyhedral surrogates do not.

**Proposition 3.2 (limit version; PROVED).** Let p_n → p\* with supp p_n = J. Let X\* be evaluable with
z\* := rec(C_{p\*}, X\*) of positive size and Φ_i(z\*) ≤ 0 for i ∈ J. Put:
- I := {i ∈ J : Φ_i(z\*) = 0 ≤ Ψ_i(z\*)};
- t_n := rec(C_{p_n}, X\*);
- δ_n := max_{i∈I} Φ_i(t_n)⁺;
- γ_n := sup{min_{i∈I}(−Φ_i(z′)) : z′ ∈ Z_{p_n}}.

If γ_n > 0 and δ_n/γ_n → 0, then (RB) fails.

*Proof.*
- **Choice of competitors.** Pick z′_n ∈ Z_{p_n} with min_I(−Φ_i(z′_n)) ≥ γ_n/2. Let s_n := 4δ_n/γ_n + 1/n, which
  tends to 0. Put z_n := (1−s_n)t_n + s_n z′_n ∈ Z_{p_n}.
- **Worlds in I.** Φ_i(z_n) ≤ δ_n − s_nγ_n/2 < 0, so r_i = ∞.
- **Worlds outside I.** By Lemma 1.1(b) the increments of t_n converge to those of z\*, and s_n → 0.
  - If Φ_i(z\*) < 0, eventually Φ_i(z_n) < 0.
  - If Φ_i(z\*) = 0 > Ψ_i(z\*), then Φ_i(z_n) → 0 and Ψ_i(z_n) → Ψ_i(z\*) < 0, so r_i → ∞.
- **Size.** m(z_n) → m(z\*) > 0. ∎

*Reading.* This is the cross-index part of the criterion. Suppose C_{p\*} is leading-optimal at the worlds of I, so
that (★) holds at p\*, but nearby C_{p_n} are leading-improvable there at a rate larger than the leading cost of the
transported record. Then (RB) fails although no single index violates (★). So (★) at every index is necessary but not
evidently sufficient for (RB). FF2 Lemma 2.4 shows that leading levels along a continuous selection generically have
exactly this profile.

---

## 4. The obstruction

Pairs are indexed by majority orientation h; h is **i-odd** if h_i < 0 < h_j, h_l. On i-odd h the advices O, S, M
(accept −h, silence, accept h) are ordered **towards acceptance**. A step a → b with a ∈ {O, S} and b ∈ {S, M} strictly
later is an **upward step**. By the write-up's background order:
- an upward step strictly improves worlds j and l and strictly worsens world i;
- so its Ψ-increments have signs (−, −, +) at (j, l, i);
- by weak guidance, its Φ-increments at j and l are ≤ 0.

The step is **Φ_i-blind** if Φ_i(h, a) = Φ_i(h, b). C_q is **Φ_i-optimal** if Φ_i(h, C_q(h)) = min_b Φ_i(h, b) for
a.e. h, i.e. C_q pays no leading cost at world i. Let Q_i be the set of interior q for which C_q is Φ_i-optimal. Q_i is
relatively closed in int Δ, because pointwise optimality passes to limits in measure along a.e.-convergent
subsequences.

**Lemma 4.0 (PROVED).** Assume (RB). Let i ∈ supp q, and suppose that on a non-null set of i-odd h some upward step
out of C_q(h) is Φ_i-blind. Then C_q is Φ_i-optimal.

*Proof.* Switch along the blind step on a non-null bounded piece E. This gives z\* with:
- Φ_i(z\*) = 0 and Φ_j(z\*), Φ_l(z\*) ≤ 0;
- Ψ_i(z\*) > 0 and Ψ_j(z\*), Ψ_l(z\*) < 0.

So z\* ∈ G(q), m(z\*) = μ(E) > 0, and I^≥(z\*) = {i}. Theorem 3.1(b) gives w ∈ W^Φ(q) with supp w ⊆ {i}, i.e.
w = e_i. That is pointwise Φ_i-optimality. ∎

(If C_q is not Φ_i-optimal, Theorem 3.1(a) gives the explicit defeating competitors: switch along the blind step on
E, plus a small multiple of a Φ_i-improving record. The three-world surrogate in `segment_examples.py` part (2) shows
min_i r_i = (1−2s)/(2s) at size 1, while every point is lexicographically defended.)

**Theorem 4.1 (PROVED modulo FF2 Thm 4.1 Steps 2–6 and their import chain).** Work on the full domain, with a base and
selection of the class. If (RB) holds, then for some ordered pair (i, j) of distinct worlds, Q_i does not accumulate
at e_j. Equivalently, there is a neighbourhood V of e_j with both of the following:
- every interior C_q with q ∈ V pays a leading cost at world i;
- for a.e. i-odd h, every upward step out of C_q(h) is strictly Φ_i-costly: Φ_i(h, C_q(h)) < Φ_i(h, b).

*Proof.* Assume (RB), and suppose Q_i accumulates at e_j for all six ordered pairs.
1. **Vertex models pay no leading cost.** By Lemma 1.2(b), C_{e_j} = B^j. Take q_n ∈ Q_i with q_n → e_j. Continuity
   in measure gives a subsequence along which C_{q_n}(h) = B^j(h) eventually, for a.e. h. Hence
   Φ_i(h, B^j(h)) = min_b Φ_i(h, b) a.e., for all i ≠ j.
2. **The leading levels are flat on {M, S, O} for mixed pairs.** Fix i and a mixed h.
   - If h is i-odd, B^j(h) = M for both j ≠ i, and M is i-worst in {M, S, O}.
   - If h_i > 0 and k is the odd world, then B^k(h) = O, which is i-worst.

   (CHECKED over all sign patterns, `posterior_witness.py` Check B.) So the i-worst advice has the minimal Φ_i-value.
   By weak guidance Φ_i(h, ·) is constant on {M, S, O}, for a.e. mixed h and every i.
3. **Reduction to Ψ.** Fix q and X.
   - Let X′ agree with X where h is mixed and X(h) ∈ {M, S, O}, and with C_q elsewhere.
   - Selected models are coherent. So they never give ×, and they accept h on unanimous pairs, which is the best
     advice at every world there.
   - So rec(C_q, X′) has Φ_i = 0 at every world, and Ψ_i(X) − Ψ_i(X′) ≥ 0 at every world.
   - By Lemma 1.2(a), some i ∈ supp q accepts rec(C_q, X′) lexicographically. Then Ψ_i(X′) ≥ Ψ_i(C_q), hence
     Ψ_i(X) ≥ Ψ_i(C_q).

   So the selection is competitive for the additive ranking Ψ.
4. **Contradiction.** Ψ is strictly guiding with integrable envelope, and the selection is continuous in measure
   through T1. FF2 Thm 4.1 applies with ℓ = Ψ and the relations of Ψ itself, for which (H3) is trivial.
5. **The equivalent form.** If Q_i does not accumulate at e_j, some neighbourhood V of e_j contains no q ∈ Q_i. By
   Lemma 4.0 no C_q with q ∈ V has a Φ_i-blind upward step on a non-null set of i-odd h. ∎

*What the defeating competitor is.* Exactly one of the following holds:
- some C_q is defeated by the explicit segment competitors of Theorem 3.1(a), built from a blind upward step and a
  Φ_i-improving record;
- all relevant C_q pay no leading cost, and FF2 supplies one competitor that is Ψ-better at every active world of
  one selected model. By Step 3 this competitor is a lexicographic improvement at every active world.

**Corollary 4.2 (PROVED, same status).** Work on the full domain with the class hypotheses, and suppose the
following hypothesis (BS) holds:

(BS) for every ordered pair (i, j) there are interior q_n → e_j such that each C_{q_n} has a Φ_i-blind upward step
on a non-null set of i-odd h.

Then (RB) fails. (BS) holds in particular when:
- **(a) one-sided (veto-type) charges:** Φ_i(h, a) = Φ_i(h, S) whenever a is silence or the i-correct acceptance,
  and the interior credal sets K_q satisfy min_{m∈K_q} m_i > 0 (e.g. K_q ⊆ int Δ);
- **(b) missed-gain charges:** Φ_i(h, a) = Φ_i(h, S) whenever a is silence or an i-wrong acceptance, and the interior
  K_q lie in int Δ and are not singletons.

*Proof.* By Lemma 4.0, (BS) makes Q_i accumulate at every e_j, and Theorem 4.1 gives the contradiction.
- **(a)** O→S is Φ_i-blind on every i-odd h, since O accepts the i-good orientation −h. C_q = D_{K_q} gives O at h
  iff max_{m∈K_q} m·h < 0. Take h = (−1 at i, η at j, η at l) with η < min_{K_q} m_i/2. The inequality is strict on a
  neighbourhood, so the set is non-null.
- **(b)** S→M is Φ_i-blind on i-odd h. If m ≠ m′ in K_q, pick an i-odd h with m·h = 0 ≠ m′·h. The i-odd cone is open
  and spans ℝ³, and one can rescale h_i, using m_i > 0. Perturbing h_i gives an open set on which
  min_K m·h < 0 < max_K m·h, i.e. silence. ∎

These classes contain the VB-type vetoes transplanted to the full domain (charges on wrong acceptances only) and every
leading level that charges only wrong acceptances or only missed gains. HH2 §3 and GG1 Thm 3.3 excluded VB-like
designs through their selections and on M_U. Corollary 4.2(a) excludes them for **every** selection continuous in
measure through T1 with interior credal sets, under any rate.

**Corollary 4.3 (plain posterior family; PROVED, inputs CHECKED).** Let C_q = {g : q⊙g ∈ D_{T1}}, and suppose that for
each i, Φ_i is flat between O and S (or between S and M) on a.e. point of some cone
N_i(η₀) := {h : h_i < 0 < h_j, h_l, max(h_j, h_l) < η₀|h_i|} with η₀ > 0. Then (RB) fails.

*Proof.* Write λ := ε/c₀ and m := max(q_j, q_l). HH2 §4.1 gives C_q(h) = O iff q·h + λ max(q_jh_j, q_lh_l) < 0, and
C_q(h) = S iff q·h + λq_ih_i ≤ 0 ≤ q·h + λ max(q_jh_j, q_lh_l). Consider h = (−1 at i, η at j, η at l).
- **O region.** For every interior q, h lies in the open O-region when 0 < η < q_i/(q_j + q_l + λm).
- **S region.** h lies in the open S-region when q_i/(q_j + q_l + λm) < η < q_i(1+λ)/(q_j + q_l). For q → e_j these
  bounds tend to 0, so the interval meets (0, η₀).

So (BS) holds along every sequence q_n → e_j with the corresponding blind step. Apply Corollary 4.2.

CHECKED (`posterior_witness.py` Check A):
- 360 cases: four values of ε, all six ordered pairs, and fifteen indices q → e_j with q_i, q_l ∈ {1/n, 1/n²};
- in each case, exact witnesses in N_i(1/10) for both regions, with strict inequalities;
- the advice was computed both from the definition min_k v_k·(q⊙g) and from the closed form, and the two agree;
- 0 failures. ∎

**Proposition 4.4 (PROVED modulo FF2 Thm 4.1's chain).** If Φ is strictly guiding with integrable envelope, then no
selection continuous in measure through T1 is lexicographically competitive. So (RB) fails, and so does the
lexicographic base itself.

*Proof.* Lexicographic acceptance of rec(C_q, X) at i implies Φ_i(X) ≥ Φ_i(C_q). That is FF2's (H3) with ℓ = Φ. ∎

**Subclass (ii): leading levels with continuous densities.** Let Φ_i(X) = ∫φ_i(h, X(h)) dμ with each φ_i(·, a)
continuous on the open sign cells.
- If the differences along every advice step vanish only on null sets, Φ is strictly guiding a.e., and
  Proposition 4.4 excludes it.
- Otherwise, Theorem 4.1 says: if (RB) holds, then for some (i, j), near e_j, the continuous functions
  φ_i(·, S) − φ_i(·, O) and φ_i(·, M) − φ_i(·, S) vanish only on null subsets of the O- and S-regions of the
  selected models on i-odd gambles.
- So within (ii) the zero sets of these differences must avoid those regions near some vertex. Corollary 4.3 excludes
  open zero sets that contain a near-coordinate cone, for the posterior family.
- The remaining blindness must sit at worlds that the steps improve, or away from those regions. There SLP can hold
  at individual indices (Lemma 5.1), and then (RB) holds there.

---

## 5. Exactly which base property would allow (RB)

**Lemma 5.1 (PROVED).** Suppose C_p is pointwise weak w-Bayes for Φ with supp w = supp p, and the w-tie set
{h : w·(φ(h,b) − φ(h,C_p(h))) = 0 for some b ≠ C_p(h)} is null. Then C_p is SLP.

*Proof.* Take z ∈ G(p). Then w·Φ(z) ≤ 0, since Φ_i(z) ≤ 0 on supp w. But w·Φ(z) is the integral of a pointwise
nonnegative function that is positive off the tie set on supp z. So μ(supp z) = 0. ∎

**Lemma 5.2 (PROVED).** Suppose C_q is SLP at an interior q. Then for a.e. mixed h, at the advice C_q(h):
- every step out of C_q(h) that worsens exactly one world i has Φ_i strictly increasing;
- every step that worsens two or three worlds strictly increases Φ at one of them, at least.

*Proof.* Switching along the step on a non-null piece gives a record. If the stated strictness failed on a non-null
set, all its Φ-increments would be ≤ 0, since the improved worlds have Φ-increments ≤ 0 by weak guidance. That
contradicts SLP. ∎

**Summary of what (RB) needs (all PROVED above).**
- *Necessary.*
  - Lexicographic competitiveness (Lemma 1.2), and C_{e_j} = B^j.
  - (★_p) at every index (Theorem 3.1(b)).
  - The cross-index condition of Proposition 3.2.
  - Φ not strictly guiding (Proposition 4.4).
  - No uniform bound (Corollary 2.5): the required rate must diverge at small sizes.
  - Near some vertex, some world's leading level is strictly costly along every upward step out of the selected
    advice, and selected models pay leading costs there (Theorem 4.1).
- *Sufficient.*
  - SLP at every index (Corollary 2.3), which then gives a full cover (Corollary 2.4).
  - At a single index, (★★_p) (Theorem 3.1(c)).
- *Exact at a single index*, except at worlds where both increments of the limit record vanish: (★_p).

**The property that allows (RB).** The base must protect its selected models lexicographically **with a leading
weight**: every leading-nonpositive record must be lower-level-worse at every world of the support of a leading Bayes
weight. Two cases arise.
- **SLP case.** No leading-nonpositive records exist, the condition is vacuous, and (RB) is automatic. By Lemma 5.2
  the leading level is then a weakly guiding field that is strictly signed at singly-worsened worlds along the
  selected steps. Its non-strictness, which Proposition 4.4 requires, lies at improved worlds, or at one of two
  worsened worlds.
- **Non-SLP case.** (★) is a unanimity-type requirement on a non-trivial face, and Theorem 4.1 shows it fails
  whenever the face contains blind upward steps near every vertex.

*Context only (not used, not claimed).* The SLP pattern of Lemma 5.2 has ties allowed at one positive world at a time
and strict signs at the odd world. It resembles the permitted-tie realisations of write-up §8 (Weakened guidance),
whose open case is the "all-tied configuration". That theorem concerns M_U and band-type ties. Whether it transfers to
SLP fields on the full domain has not been examined.

---

## 6. What is used

| Result | Uses | Does not use |
|---|---|---|
| Lemma 1.1, Thm 2.1, Cor 2.2, Cor 2.3, Thm 3.1, Prop 3.2, Lemmas 5.1–5.2 | integrable envelopes, non-atomic finite μ, decomposable domain, continuity in measure (2.1–2.3, 3.2) | (IB), (FC), transitivity, closed sections, (C), admissibility, T1, guidance (2.1), the rate rule (only the audit's criterion) |
| Lemma 1.2 | (RB), weak guidance of Φ_j, strict guidance of Ψ_j, B^j evaluable | everything else |
| Lemma 4.0, Thm 4.1, Cor 4.2–4.3, Prop 4.4, Cor 2.5 | the above, T1 = C_{q₀}, full domain, FF2 Thm 4.1 (Steps 2–6: D1, BB2 Thm 6.1 with AUDIT_BB Lemma 2.0, M3.7–M3.8, each refereed once) | (IB), (FC), closed sections, (C), admissibility, T1 undominated |
| Cor 2.4 (positive direction) | HH2 Prop 6.1(a)–(d) (PROVED in HH2; audit: sound), transitivity-free KKM (audit: correct), audit's rate criterion | — |

**Answer to the brief's last question: the obstruction uses neither (IB) nor (FC).** It is a statement about
competitiveness of a continuous selection through T1 for the base (Φ, Ψ) under the rate criterion. The
caveat of HH2 §5 also applies here: T1 is assumed selected, as in the class. Covers in which T1 is only tied with a
selected model are not covered by the FF2 step.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | attainable set (size, Φ, Ψ) compact convex; uniform transfer between indices | PROVED (imports Lyapunov/Aumann) |
| 1.2 | (RB) ⇒ lexicographic competitiveness, C_{e_j} = B^j | PROVED |
| **2.1** | **every (RB)-defeating sequence has a leading-nonpositive limit record of size ≥ a at a limit index** | **PROVED** |
| 2.2 | the audit's adversary (Φ → 0, Ψ ≤ −c at all active worlds) exists only if lexicographic competitiveness fails | PROVED |
| 2.3 | SLP at every index ⇒ (RB) | PROVED |
| **2.4** | **SLP at every index ⇒ the rate system is a full (FC) cover of T1** | **PROVED mod HH2 6.1, KKM, audit criterion** |
| 2.5 | no base in the class has a uniform (RB) bound | PROVED mod FF2 chain |
| 3.1 | exact criterion (★_p) at one index: segment competitors; (★★_p) sufficient | PROVED; CHECKED on GG1 data |
| 3.2 | cross-index mechanism: improvability faster than transported cost defeats (RB) | PROVED |
| 4.0 | blind upward step at an active world i ⇒ (RB) forces C_q Φ_i-optimal | PROVED |
| **4.1** | **(RB) ⇒ near some vertex some world's leading level is strictly costly on every upward step, and charges selected models** | **PROVED mod FF2 chain** |
| 4.2 | (RB) fails under (BS): one-sided (veto-type) charges, missed-gain charges | PROVED mod FF2 chain |
| 4.3 | plain posterior + blind near-coordinate cones ⇒ (RB) fails | PROVED mod FF2 chain; inputs CHECKED (360 cases) |
| 4.4 | strictly guiding Φ ⇒ not even lexicographically competitive | PROVED mod FF2 chain |
| 5.1–5.2 | sufficient condition for SLP; structure of SLP fields | PROVED |
| — | (RB) fails for every base in the class | **not proved**; it is equivalent, on the SLP part, to excluding SLP leading fields (open) |
| — | T1 cover | **not obtained**; Cor 2.4 reduces the class's SLP part to the existence of one weakly guiding field |

**Referee priorities.**
1. Theorem 2.1 Step 1. The sign bookkeeping of r_i: r_i ≥ R forces Φ_i ≤ E/R, and Ψ_i < 0 when Φ_i ≥ 0. Note that
   worlds beaten by leading improvement keep no sign on Ψ.
2. Lemma 1.1(a). Compactness with the size coordinate, and realisability of every point of Z_p by an evaluable
   model.
3. Corollary 2.4. That every undominated B is tied with a selected model without transitivity, and that SLP makes
   the tie trivial.
4. Theorem 4.1 Step 3. That the reduction X → X′ uses only coherence of selected models, and that lexicographic
   acceptance of a Φ-null record is Ψ-acceptance.
5. Proposition 3.2. The choice of s_n.

## 8. Files (`ii2py/`)

- `posterior_witness.py` → `posterior_witness.out`:
  - Check A. Exact witnesses that the plain posterior O- and S-regions on i-odd gambles meet every near-coordinate
    cone N_i(1/10), for q → e_j. This covers all six (i, j), four ε, and fifteen q per pair (360 cases, 0 failures).
    Advice is computed from the definition and from the closed form, and they agree.
  - Check B. Each mixed sign pattern and world i has a vertex model giving the i-worst advice (Theorem 4.1 Step 2).
- `segment_examples.py` → `segment_examples.out`:
  - (1) GG1 Lemma 2.2 data: (★) fails, and the segment gives r = (1−s)/s at size 1; 0 of 2197 grid points are
    lexicographically better at both worlds.
  - (2) A three-world surrogate of Lemma 4.0: lexicographically defended points with min_i r_i = (1−2s)/(2s).
  - (3) An SLP surrogate: exact LP value c(a) = a/5, the bound E/c(a), and grid maxima under the bound.
  - (4) A non-SLP surrogate satisfying (★★): grid maxima of r finite.
  - (5) The audit's counterexample to HH2 6.1(e) in r-notation.
