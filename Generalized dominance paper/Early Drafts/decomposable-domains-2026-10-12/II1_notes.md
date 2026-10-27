# II1 (round 37, BRIEF29). The exchange-rate design decided by (RB): the repaired coverage corollary, a compactness reduction of (RB) to pointwise conditions, a conditional full cover, and where the class ends

18 Oct 2026. Rules of BRIEF13 and BRIEF29; the corrections of AUDIT_HH_rate.md and AUDIT_HH_summary.md are adopted.
Labels:
- **PROVED**: full argument here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**.

Scripts are in `ii1py/`. Run `python3 -I <script>.py` inside that folder; outputs are in `*.out`. All arithmetic is
`fractions.Fraction`.

Setting: three worlds, T1 the ε-contamination of u for any ε ∈ (0,1), the notation of the write-up §2, FF1 §1 and
HH2 §§1, 6. The domain is the full four-advice domain unless M_U is named; every statement of §§1–4 holds verbatim on
M_U (advice ranges {+,0}). Each world ≼_i is reflexive and is not assumed transitive. (FC) is as in BRIEF28. Strict (G),
(IB), (LA), (S) (closed sections F_i(X) = {p : C_p ≼_i X} for every X, competitiveness on supp p), (C) in its direct
form, (LF) at T1 and T1 ∈ C_L are unchanged. No equal-profile quotient is used. No assumption is added: every extra
hypothesis below is a hypothesis of a stated result and defines the class that result is about.

---

## 0. Outcome

**No cover of T1 was obtained.** The exchange-rate class was reduced to a single additive question, and the part of the
class that breaks leading ties with the second level was cut down by an explicit adversary.

1. **Part A: the repairs (§2; PROVED).**
   - HH2 Prop 6.1(e) is replaced by Prop 2.1. A fixed record is judged lexicographically at small scale. Records with a
     bounded exchange ratio are judged lexicographically uniformly. But every world with a Φ-blind improvement rejects,
     at every scale, records that the lexicographic order accepts.
   - Prop 2.2 gives the exact condition under which HH2 Thm 5.1 binds a rate world. This replaces the claim "Thm 5.1
     does not bind".
   - Theorem 2.4 is the corrected Cor 6.2. Its admissibility hypotheses are (A1) every C_p is undominated in the
     lexicographic base and (A2) three-world lexicographic ties with selected models are trivial. Both follow from one
     uniqueness property (U) (Lemma 2.3), which holds for every strict pointwise lexicographic Bayes selection.
   - Lemma 2.5 (new necessary condition): in every rate cover, every model undominated in the lexicographic base is
     coherent; under (U) it is selected.
2. **(RB) reduced to pointwise conditions (§3; PROVED).** Weak-* (Young-measure) compactness along a selection continuous
   in measure gives:
   - Theorem 3.2: (RB) holds if every selected model is "non-degenerate" (ND). Every record whose leading increments
     are ≤ 0 at all active worlds must be lower-level costly at some active world where nearby selected models pay no
     improvable leading cost.
   - Theorem 3.3: (RB) fails, with an explicit adversarial family, if some selected model has a record v with leading
     increments ≤ 0 at all active worlds, together with a record s that improves the leading level at every world of
     I(v), the active worlds where v is leading-neutral and lower-level costly.
   - Cor 3.4: (RB) forces C_p to be a weak Bayes model of the leading field for some weight carried by I(v).
   - Cor 3.5: as a consequence, a fully blind record that improves two worlds at the lower level, out of a model that pays
     an improvable leading cost at the third world, defeats every continuous rate. CHECKED on an exact atomic instance
     in which the selected model is the strict lexicographic u-Bayes model (`adversary.py`).
3. **The tie-free design and a conditional full cover (§4; PROVED).** Call a selection *(NT)* if each C_p is the only
   model whose leading costs are no larger than its own at every world of supp p. Theorem 4.1: if Φ is integrable and
   weakly guiding, and the selection is coherent, continuous in measure, passes through T1 and is (NT), then for EVERY
   integrable strictly guiding Ψ the rate system is a full cover of T1 under (FC). Every axiom is verified for arbitrary
   measurable competitors. All known barriers are respected automatically (Prop 4.2).
4. **Where the tie-free design can live (§5).**
   - On M_U it cannot (Prop 5.1; PROVED modulo the write-up's Theorem main and Cor coverage). There, (NT) at the
     vertices makes Φ strictly guiding, so Φ alone would be an additive cover.
   - On the full domain, (NT) forces Φ to be strict-best, with every zero a bad~silence zero, and the zero set non-null
     (Prop 5.2; PROVED modulo Theorem gm).
   - Φ satisfies Steps 1–5 of FF2 Thm 4.1 (Prop 5.3; PROVED). Only Step 6, the field contradiction proved for strictly
     guiding fields, is missing.
   - A zero set of odd or double type forces uncountably many selected models with degenerate (at most one-dimensional)
     credal sets (Prop 5.4; PROVED).
5. **Designs that break ties with Ψ (§6).** The plain posterior family is not the weak lexicographic Bayes family, at
   its own index, of any finite-level additive base (Prop 6.1; PROVED, CHECKED for four values of ε). In every other
   tie design, Cor 3.4 restricts where the selection may pay leading costs, and Cor 3.6 does so at T1 itself. VB-type
   plateaus satisfy (ND) but their selections jump at the vertices.

**Single most important open point (P_w).** Is there an integrable additive leading field Φ on the full domain with the
following properties?
- It is weakly guiding and strict-best: the world-i-best advice is strictly cheapest at world i.
- It has a non-null set of exact bad~silence zeros.
- It admits a coherent selection continuous in measure through T1 such that each C_p is the unique model whose leading
  costs at the worlds of supp p do not exceed its own.

A YES gives a full (FC) cover of T1 by Theorem 4.1, with any strictly guiding second level. A NO follows if the FF2 Step 6
import chain (D1 → BB2 Thm 6.1 → M3.7/M3.8) survives bad~silence zeros. That is the zero-pattern residual left open in
N9.9, N10 (C-i), R16 §2.8 and N26 §5.

---

## 1. Setting and two compactness facts

### 1.1 Bases, records, the rate world

- **Advice and records.** At a pair h the advice range is A(h) ⊆ {M, S, O, ×} (all four on the full domain). Pairs are
  indexed by majority orientation as in HH2 §4.1. Records and their realisations are as in HH2 §1.1. A record *out of*
  C_p is rec(C_p, X).
- **Base.** For each world i there are measurable penalties φ_i(h, a) (leading) and ψ_i(h, a) (lower), with an integrable
  envelope E(h) := max_{i,a}(|φ_i(h,a)| + |ψ_i(h,a)|).
  - φ_i is **weakly guiding**: φ_i(h, a) ≤ φ_i(h, b) whenever a is weakly better than b in world-i rank, for a.e. h.
  - ψ_i is **strictly guiding**: the same with strict inequality for a ≠ b.
- **Costs and increments.** For a model X put Φ_i(X) := ∫φ_i(h, a_X(h)) dμ, and Ψ_i(X) likewise. For t = rec(X, Y) put
  Φ_i(t) := Φ_i(Y) − Φ_i(X) and Ψ_i(t) := Ψ_i(Y) − Ψ_i(X). These depend on t only. Put m(t) := μ(supp t) and
  M := μ(H) < ∞.
- **Lexicographic base.** L_i accepts t iff Φ_i(t) > 0, or Φ_i(t) = 0 and Ψ_i(t) ≥ 0. It is a transitive (IB) world
  with strict (G).
- **Rate world (HH2 Prop 6.1).** For continuous k : (0, M] → (0, ∞),
  𝒜_i^k := {ι} ∪ {t : Φ_i(t) ≥ 0 and Ψ_i(t) + k(m(t))Φ_i(t) ≥ 0}.
  HH2 Prop 6.1(a)–(d) stand (AUDIT_HH_rate):
  - (a) reflexive, (IB), strict (G);
  - (b) strict records of 𝒜^k are L-strict, so (FC) holds with ordering extension L;
  - (c) ties of 𝒜^k are exactly lexicographic ties;
  - (d) closed sections when the selection is continuous in measure.
- **Exchange-rate requirement (AUDIT_HH_rate).** For p ∈ Δ, J := supp p, and t = rec(C_p, X) ≠ ι, and for i ∈ J:
  - r_i(p, X) := 0 if Φ_i(t) = 0 ≤ Ψ_i(t);
  - r_i(p, X) := max(0, −Ψ_i(t)/Φ_i(t)) if Φ_i(t) > 0;
  - r_i(p, X) := ∞ otherwise.

  Put r(p, X) := min_{i∈J} r_i(p, X). The criterion is
  **(RB)** for every a > 0, sup{r(p, X) : p ∈ Δ, X a model, m(rec(C_p, X)) ≥ a} < ∞.
  AUDIT_HH_rate proves: a continuous k with r(p, X) ≤ k(m(rec(C_p, X))) for all p, X exists iff (RB) holds.

**Selections** are maps p ↦ C_p of coherent models with C_{e_i} = B^i (the world-i-best model; forced by competitiveness
at e_i and strict (G)). *Continuous in measure* means μ(C_{p_n} △ C_p) → 0 (as advice-disagreement sets) whenever
p_n → p. Σ := {C_p}.

### 1.2 Relaxed records

A **relaxed record out of C_p** is a measurable w : H → Δ(A(h)), a probability on the available advices at each pair.
Its increments and support mass are
- Φ_i(w; p) := ∫ Σ_b w_b(h)[φ_i(h, b) − φ_i(h, C_p(h))] dμ, and likewise Ψ_i(w; p);
- m(w; p) := ∫(1 − w_{C_p(h)}(h)) dμ.

An actual record rec(C_p, X) is the case w = δ_{X(h)}.

**Lemma 1.1 (PROVED; Lyapunov–Aumann).** Fix p and finitely many functions f_1, …, f_N on H × 𝔄 with integrable
envelope.
- (a) The set {(∫Σ_b w_b f_n(h,b) dμ)_n : w relaxed} is compact and convex. It equals the set of values
  (∫ f_n(h, a_X(h)) dμ)_n over models X.
- (b) **Proportional restrictions.** For every record t and θ ∈ [0, 1] there is E ⊆ supp t such that t|_E (t on E, ι
  elsewhere) has every listed integral, and its support mass, equal to θ times that of t.

*Proof.* (a) The integrand is the integral of a finite-valued, integrably bounded multifunction over a non-atomic finite
measure. Aumann's theorem (convexity and compactness of the integral, and equality with the integral of its convex hull)
gives both claims. (b) Lyapunov's theorem for the non-atomic vector measure E ↦ (μ(E), ∫_E (f_n(b_t) − f_n(a_t)) dμ)_n on
supp t: its range is convex and contains 0 and the full vector. ∎

So conditions on records may be stated for actual records or for relaxed ones alike. HH2 used (b) in Thm 4.5 and Thm 5.1.

**Lemma 1.2 (Young limits along a continuous selection; PROVED).** Let the selection be continuous in measure, p_n → p*,
and X_n any models. Along a subsequence there is a relaxed w out of C_{p*} with the following properties.
- (a) For every f ∈ L¹(H × 𝔄): ∫[f(h, X_n(h)) − f(h, C_{p_n}(h))] dμ → ∫[Σ_b w_b f(h, b) − f(h, C_{p*}(h))] dμ.
- (b) m(rec(C_{p_n}, X_n)) → m(w; p*).

*Proof.*
- The indicator vectors w_n(h) := (1[X_n(h) = b])_b lie in the unit ball of L^∞(H; ℝ^𝔄) = (L¹)*. L¹ is separable, so a
  subsequence converges weak-* to some w. Weak-* limits keep w_b ≥ 0, Σ_b w_b = 1 and w_b = 0 off A(h), a.e.
- This gives ∫Σ_b w_{n,b} f(h,b) → ∫Σ_b w_b f(h,b).
- f(h, C_{p_n}(h)) → f(h, C_{p*}(h)) in measure, with integrable domination. So the second terms converge in L¹.
- (b): |1[X_n = C_{p_n}] − 1[X_n = C_{p*}]| ≤ 1[C_{p_n} ≠ C_{p*}]. That tends to 0 in L¹, and
  ∫ 1[X_n = C_{p*}] = ∫ w_{n, C_{p*}(h)} → ∫ w_{C_{p*}(h)}. ∎

---

## 2. Part A: the repairs

### 2.1 HH2 Prop 6.1(e), corrected

**Proposition 2.1 (PROVED; replaces HH2 Prop 6.1(e)).** Fix a world i.
- (i) **Constant rate.** If k ≡ K, every accepted record satisfies (Ψ_i + KΦ_i)(t) ≥ 0. So the integrable, strictly
  guiding field ψ_i + Kφ_i endorses every accepted comparison. If this holds at every world, FF2 Thm 4.1 (at its
  recorded status) excludes a selection continuous in measure, competitive and through T1.
- (ii) **Fixed records are lexicographic at small scale.** Let k(m) → ∞ as m → 0. Let t ≠ ι, and let t_θ (θ ∈ (0,1]) be
  proportional restrictions of t (Lemma 1.1(b) for μ, φ_i and ψ_i). Then there is θ₀ > 0 such that, for θ < θ₀,
  t_θ ∈ 𝒜_i^k iff t ∈ L_i.

  Uniformly: for every R < ∞ there is m_R > 0 such that every record t with m(t) < m_R, and with Φ_i(t) ≤ 0 or
  −Ψ_i(t) ≤ RΦ_i(t), receives the lexicographic verdict.
- (iii) **Not uniformly.** Suppose that, out of some model Z, there are a record t_E with Φ_i(t_E) > 0 and a record t_F
  with disjoint support, Φ_i(t_F) = 0 and Ψ_i(t_F) < 0 (a Φ_i-blind improvement). Then for every θ ∈ (0, 1] there is a
  record t out of Z with:
  - m(t) ≤ θ(m(t_E) + m(t_F));
  - Φ_i(t) > 0, so L_i accepts t;
  - t ∉ 𝒜_i^k.

  This holds for every continuous k.

*Proof.*
- (i) Immediate.
- (ii) If Φ_i(t) < 0, or Φ_i(t) = 0, both verdicts are independent of θ and agree. If Φ_i(t) > 0, then t_θ is accepted
  iff k(θ m(t)) ≥ −Ψ_i(t)/Φ_i(t), which holds for small θ. For the uniform statement choose m_R with k ≥ R on
  (0, m_R).
- (iii) Write α := Φ_i(t_E) > 0, β := Ψ_i(t_E), γ := −Ψ_i(t_F) > 0, and m_E, m_F for the support masses.
  - For x, y ∈ [0, 1], let t_{x,y} be the union of proportional restrictions of t_E (fraction x) and t_F (fraction y).
    Then Φ_i = xα, Ψ_i = xβ − yγ and m = x m_E + y m_F.
  - Put y := θ, and let K_θ be the maximum of k on [θ m_F, θ(m_E + m_F)].
  - Put x := θc with c := min(1, γ/(2(|β| + K_θα + 1))).
  - Then Ψ_i + kΦ_i ≤ θ(c(|β| + K_θα) − γ) < 0, while Φ_i = θcα > 0. ∎

The audit's example (AUDIT_HH_rate) is (iii) with unit densities: leading increment a = μ(E), lower increment 2a − m, and
0 < a < m/(k(m)+2).

CHECKED (`rate_example.py` → `rate_example.out`, k(m) = 1/m):
- at m = 1, 1/2, 1/10, 10⁻³ and 10⁻⁶, a record with a = m/(k(m)+3) is accepted by L and rejected by 𝒜^k;
- for a fixed record (a₀, m₀) = (1/100, 1), the exact threshold of (ii) is θ₀ = 1/98, and the dyadic restrictions
  switch to the lexicographic verdict at θ = 1/128.

So the sentence "if k(m) → ∞, verdicts on small records are lexicographic" is false. The true statements are (ii) and
(iii). What it was used for, escaping HH2 Thm 5.1, needs the separate argument below.

### 2.2 When HH2 Theorem 5.1 binds a rate world

**Proposition 2.2 (PROVED).** Let k(m) → ∞ as m → 0. Fix a world i, an integrable strictly guiding ℓ_i and an exhausting
sequence (H_n), and write Δℓ_i(r) := ∫(ℓ_i(b_r) − ℓ_i(a_r)) dμ.
- (a) World 𝒜_i^k satisfies (Loc_i) (HH2 §5) iff the following holds for every q with i ∈ supp q and every n. No
  record r out of C_q with supp r ⊆ H_n is of either kind:
  - (α) Φ_i(r) > 0 > Δℓ_i(r);
  - (β) Φ_i(r) = 0 ≤ Ψ_i(r) and Δℓ_i(r) < 0.
- (b) In particular, (Loc_i) fails for **every** ℓ_i if some C_q with i ∈ supp q has, inside some H_n, both a non-null
  set of Φ_i-blind i-improving arrows and a disjoint non-null set of arrows with δφ_i > 0.

*Proof.*
- (a), ⇐. Let r have Δℓ_i(r) < 0, and let E ⊆ supp r satisfy ∫_EΔℓ_i ≤ (μ(E)/2m(r))Δℓ_i(r). Then r|_E is a record out
  of C_q in H_n with Δℓ_i(r|_E) < 0. It is not of kind (α), so Φ_i(r|_E) ≤ 0. If Φ_i(r|_E) < 0 it is rejected. If
  Φ_i(r|_E) = 0, it is not of kind (β), so Ψ_i(r|_E) < 0 and it is rejected. Thus (Loc_i) holds with any t₀.
- (a), ⇒. Let r be of kind (α) or (β), and take proportional restrictions r_θ (Lemma 1.1(b) for μ, φ_i, ψ_i, ℓ_i). Then
  ∫_{E_θ}Δℓ_i = θΔℓ_i(r) ≤ (θ/2)Δℓ_i(r), and μ(E_θ) = θm(r).
  - Kind (α): r_θ is accepted once k(θm(r)) ≥ −Ψ_i(r)/Φ_i(r).
  - Kind (β): r_θ is accepted for every θ.

  Either way no t₀ works.
- (b) Let A be the blind improvement. Strict guidance of ℓ_i gives Δℓ_i(A-part) < 0. Let B be the paid set. The record
  "A-part ∪ θ·(B-part)" is of kind (α) for small θ. ∎

*Correct reading of "Theorem 5.1 does not bind".* HH2 Thm 5.1 excludes a rate system (selection continuous in measure,
competitive, through T1) iff one field ℓ = (ℓ_1, ℓ_2, ℓ_3) satisfies (a) at all three worlds. A design escapes only if,
for every ℓ, some world admits a record of kind (α) or (β). Prop 2.2(b) gives a sufficient, ℓ-free escape.

### 2.3 Admissibility, and the corrected coverage corollary

**Definition.** The selection has **(U)** if, for every p ∈ Δ, any model Y with
(Φ_i(Y), Ψ_i(Y)) ≤_lex (Φ_i(C_p), Ψ_i(C_p)) for every i ∈ supp p equals C_p a.e.

**Lemma 2.3 (PROVED).**
- (a) (U) implies:
  - (A1) every C_p is undominated in the lexicographic base L;
  - (A2) every model lexicographically tied with a selected C_p at all three worlds equals C_p.
- (b) (U) holds if every C_p is the a.e.-unique **pointwise lexicographic p-Bayes** model. That is, for a.e. h and every
  b ≠ C_p(h), either p·δφ(h) > 0, or p·δφ(h) = 0 and p·δψ(h) > 0, where δ denotes increments of the arrow
  C_p(h) → b.
- (c) (U) holds if the selection is (NT) (§4).

*Proof.*
- (a) Lexicographic domination of C_p, or a three-world lexicographic tie with C_p, is a case of the hypothesis of (U).
- (b) Let Y satisfy the hypothesis and put J := supp p.
  - Pointwise Bayes gives Σ_J p_iΦ_i(Y) ≥ Σ_J p_iΦ_i(C_p), while the hypothesis gives Φ_i(Y) ≤ Φ_i(C_p) for i ∈ J.
  - Since p_i > 0 on J, Φ_i(Y) = Φ_i(C_p) for every i ∈ J.
  - Equality in the weighted sum forces p·δφ = 0 a.e. on the disagreement set, so Ψ decides there and
    Σ_J p_iΨ_i(Y) ≥ Σ_J p_iΨ_i(C_p), strictly unless Y = C_p a.e.
  - The hypothesis also gives Ψ_i(Y) ≤ Ψ_i(C_p) on J. So Y = C_p a.e.
- (c) Lexicographic ≤ at i implies Φ_i(Y) ≤ Φ_i(C_p). ∎

**Theorem 2.4 (corrected HH2 Cor 6.2; PROVED).** Assume the following.
- (H1) The base is integrable, Φ_i weakly guiding, Ψ_i strictly guiding.
- (H2) p ↦ C_p is a selection of coherent models, continuous in measure, with T1 = C_{q₀}.
- (H3) (A1) and (A2) hold; for instance (U).
- (H4) (RB) holds.

Let k be the continuous rate of AUDIT_HH_rate built from (RB). Then 𝒜^k = (𝒜_1^k, 𝒜_2^k, 𝒜_3^k) has the following
properties.
- It is reflexive, (IB), strict (G) and (FC).
- (S) holds: competitiveness of every C_p on supp p, and closed sections for every model.
- Every C_p is coherent and undominated, so (LA) holds and T1 ∈ C_L.
- Direct (C) holds, and U = C_L = Σ.
- (LF) holds at T1.

So 𝒜^k is a full cover of T1 under (FC).

*Proof.*
1. **Prop 6.1(a)–(d).** These give reflexivity, (IB), strict (G), (FC) (ordering extension L) and closed sections.
2. **Competitiveness.** Let X ≠ C_p. Then r(p, X) ≤ k(m) < ∞, so some i ∈ supp p has r_i ≤ k(m).
   - If Φ_i > 0, then −Ψ_i ≤ kΦ_i, so Ψ_i + kΦ_i ≥ 0.
   - If Φ_i = 0, then Ψ_i ≥ 0.

   Either way rec(C_p, X) ∈ 𝒜_i^k. For X = C_p use reflexivity.
3. **Admissibility.** Suppose Y dominates C_p in 𝒜^k. Then rec(Y, C_p) ∈ 𝒜_i^k ⊆ L_i at every world. It is 𝒜^k-strict
   at some world, hence L-strict there (Prop 6.1(b)). So Y dominates C_p in L, against (A1). Hence C_p ∈ C_L. Also
   T1 = C_{q₀} ∈ C_L.
4. **(C).** Let X ≈ C with C ∈ C_L.
   - HH1 Prop 1(b) (arbitrary relations, (LA), (S)) gives C ≈ C_p for a selected C_p.
   - Ties in 𝒜^k are lexicographic ties (Prop 6.1(c)), so (A2) gives C = C_p.
   - Then X is lexicographically tied with C_p at all three worlds, so X = C_p ∈ C_L.

   The same argument gives U = Σ: an undominated model is ≈ some C_p, hence equal to it.
5. **(LF)** holds on the full domain, and on M_U with N = U. ∎

*What was wrong in HH2 Cor 6.2, and what replaces it.*
- Competitiveness does not exclude a rival that is weakly better at every world and strictly better at one. That case is
  excluded here by (A1) through Prop 6.1(b).
- "T1 undominated and (C) in 𝒜^k" are now consequences, not hypotheses.
- The direction of HH2's "C_L ⊆ Σ" step is now correct (step 4).

**Lemma 2.5 (a necessary condition on the base; PROVED).** Let 𝒜^k satisfy (LA), (S) and direct (C), for some
continuous k and some selection. Then every model undominated in the lexicographic base L belongs to C_L, so it is
coherent. Under (A2) it is a selected model.

*Proof.*
- If X is L-undominated, it is 𝒜^k-undominated: 𝒜^k-domination is L-domination by Prop 6.1(b).
- HH1 Prop 1(c) gives U = C_L in 𝒜^k.
- Under (A2), HH1 Prop 1(b) and Prop 6.1(c) give X lexicographically tied with some C_p at all worlds, so X = C_p. ∎

*Use.* A base whose lexicographic preorder has an incoherent undominated model cannot be the base of any rate cover,
whatever k and whatever selection. N9 §4.3 (Prop 4.5, imported at its recorded status) exhibits such models
("decoupled" X(t, b)) for bases with a non-null free set and an additive second level near ∂D_{T1}. So **free sets are
excluded in the rate class too.**

---

## 3. (RB) reduced to pointwise conditions

Throughout this section (H1) holds, and the selection is coherent and continuous in measure.

**Proposition 3.1 (lexicographic competitiveness gives a weak Bayes weight for the leading field; PROVED).** Suppose
C_p is competitive on J := supp p in L. This holds in particular if it is competitive in 𝒜^k ⊆ L, or if r(p, ·) < ∞.
Then:
- (a) there is α ∈ Δ_J such that, for a.e. h and every b, α·δφ(h; C_p(h) → b) ≥ 0. Write W_Φ(p) for the closed convex
  set of all α ∈ Δ with this property;
- (b) if this holds for every p, then W_Φ has closed graph, and every α* ∈ int Δ lies in W_Φ(q) for some q.

*Proof.*
- (a) By Lemma 1.1, Z := {Φ_J(t) : t out of C_p} is convex and contains 0. A record with Φ_i(t) < 0 for all i ∈ J would
  be lexicographically negative at every active world. So Z misses the open negative orthant. Separation gives
  α ∈ Δ_J with α·z ≥ 0 on Z. The pointwise statement follows by switching on non-null sets, as in FF2 Thm 4.1 Step 1.
- (b) This is FF2 Thm 4.1 Steps 2–3 verbatim. Closed graph uses continuity in measure; covering uses Browder–Brouwer and
  W_Φ(q) ∩ Δ_{supp q} ≠ ∅. Neither step uses strict guidance of the field. ∎

### 3.1 A sufficient condition

**Definition (ND).** For p ∈ Δ let W(p) be the set of i ∈ supp p for which some neighbourhood N of p in Δ has the
following property: for every q ∈ N, C_q(h) minimises φ_i(h, ·) over A(h) for a.e. h. That is, nearby selected models
pay no improvable leading cost at world i.

The selection is **(ND)** if, for every p ∈ Δ, every relaxed record w out of C_p with m(w; p) > 0 and Φ_i(w; p) ≤ 0
for all i ∈ supp p has Ψ_i(w; p) > 0 for some i ∈ W(p).

**Theorem 3.2 (PROVED).** (ND) implies (RB).

*Proof.*
1. **The bad sequence.** Suppose (RB) fails. Then there are a > 0, p_n ∈ Δ and models X_n such that t_n := rec(C_{p_n}, X_n)
   has m(t_n) ≥ a and r(p_n, X_n) → ∞. Pass to p_n → p*, and put J* := supp p*.
   - For large n, supp p_n ⊇ J*. A minimum over a larger index set is smaller, so r_i(p_n, X_n) → ∞ for every i ∈ J*.
2. **The limit.** Lemma 1.2 gives a relaxed w out of C_{p*} with Φ_i(t_n) → Φ_i(w; p*), Ψ_i(t_n) → Ψ_i(w; p*) and
   m(w; p*) = lim m(t_n) ≥ a.
3. **Leading increments.** Let C := 2∫E dμ, so |Ψ_i(t_n)| ≤ C. If Φ_i(t_n) > 0, then Φ_i(t_n) ≤ C/r_i(p_n, X_n) → 0.
   Hence limsup Φ_i(t_n) ≤ 0, and Φ_i(w; p*) ≤ 0 for every i ∈ J*.
4. **Lower increments at W(p*).** For i ∈ W(p*), eventually p_n lies in the neighbourhood N of the definition, so
   Φ_i(t_n) ≥ 0.
   - Then r_i → ∞ forces Ψ_i(t_n) < 0: if Φ_i(t_n) = 0 and Ψ_i(t_n) ≥ 0, then r_i = 0; if Φ_i(t_n) > 0, then
     r_i = max(0, −Ψ_i/Φ_i).
   - So Ψ_i(w; p*) ≤ 0 for every i ∈ W(p*).
5. **Contradiction.** This contradicts (ND) at p*. ∎

*Remarks.*
- By Lemma 1.1, (ND) may be checked on actual records.
- The proof is where continuity in measure enters: the requirement is controlled uniformly in p only through limits of
  selected models.

### 3.2 A sufficient condition for failure, with the explicit family

For a record v out of C_p with Φ_i(v) ≤ 0 for all i ∈ J := supp p, put
I(v) := {i ∈ J : Φ_i(v) = 0 and Ψ_i(v) ≥ 0},
the active worlds at which v is leading-neutral and not improving at the lower level. I(v) = ∅ means that v already
violates lexicographic competitiveness.

**Theorem 3.3 (PROVED).** Let p ∈ Δ, J := supp p. Suppose:
- v ≠ ι is a record out of C_p with Φ_i(v) ≤ 0 for every i ∈ J;
- s is a record out of C_p with Φ_i(s) < 0 for every i ∈ I(v). If I(v) = ∅, take s := ι.

Then (RB) fails at a := ηm(v), for some η ∈ (0, 1]. Explicitly:
- choose η ∈ (0, 1] and E ⊆ supp v by Lemma 1.1(b) applied to the densities of v and of s|_{supp v};
- put s′ := s restricted to H ∖ E;
- for δ ∈ (0, 1] let F_δ ⊆ supp s′ carry the proportion δ of every increment of s′.

The models X_δ := C_p modified by v on E and by s on F_δ satisfy m(rec(C_p, X_δ)) ≥ ηm(v) and r(p, X_δ) → ∞ as δ → 0.

*Proof.*
1. **Choice of η.** Φ(s′) = Φ(s) − ηΦ(s|_{supp v}). For η small (η = 1 if supp s ∩ supp v is null), Φ_i(s′) < 0 for every
   i ∈ I(v).
2. **Increments.** The increments of t_δ := rec(C_p, X_δ) are Φ_i = ηΦ_i(v) + δΦ_i(s′) and Ψ_i = ηΨ_i(v) + δΨ_i(s′). Take
   i ∈ J.
   - If Φ_i(v) < 0: Φ_i(t_δ) < 0 for small δ, so r_i = ∞.
   - If i ∈ I(v): Φ_i(t_δ) = δΦ_i(s′) < 0, so r_i = ∞.
   - Otherwise Φ_i(v) = 0 and Ψ_i(v) < 0, and Ψ_i(t_δ) < ηΨ_i(v)/2 for small δ.
     - If Φ_i(s′) ≤ 0: Φ_i(t_δ) ≤ 0 and Ψ_i(t_δ) < 0, so r_i = ∞.
     - If Φ_i(s′) > 0: r_i ≥ η|Ψ_i(v)|/(2δΦ_i(s′)) → ∞.
3. **Support.** m(t_δ) ≥ m(v|_E) = ηm(v). ∎

CHECKED (`adversary.py` → `adversary.out`). An exact two-cell atomic surrogate with p = u:
- φ weakly guiding, ψ strictly guiding;
- the selected advice is the **strict lexicographic u-Bayes** advice in both cells;
- v (silence → acceptance on cell A) is Φ-blind at all three worlds with Ψ(v) = (−1, −1, 3), so I(v) = {3};
- s (acceptance → silence on cell B) has Φ(s) = (1, 1, −1).

Along X_δ the support mass stays ≥ 1, and r = (1 − δ)/δ, from 9 at δ = 10⁻¹ to 99 999 999 at δ = 10⁻⁸. So the hypotheses
of Theorem 3.3 are compatible with every pointwise requirement a lexicographic Bayes selection meets.

**Corollary 3.4 (a necessary condition for (RB); PROVED).** If (RB) holds, then for every p and every v ≠ ι out of C_p
with Φ_{supp p}(v) ≤ 0:
- I(v) ≠ ∅;
- there is λ ∈ Δ_{I(v)} such that C_p is a pointwise weak λ-Bayes model of the leading field:
  λ·δφ(h; C_p(h) → b) ≥ 0 for a.e. h and every b.

*Proof.* Otherwise the convex set {Φ_{I(v)}(s) : s out of C_p} (Lemma 1.1) meets the open negative orthant. Separation
and the switching argument of Prop 3.1. Theorem 3.3 then applies. ∎

**Corollary 3.5 (blind majority moves; PROVED).** Let p ∈ Δ, J := supp p and k ∈ J. Suppose:
- (a) there is a non-null set A of pairs and advice changes on A that are Φ_i-neutral for every i ∈ J and strictly
  improving, in world rank, at every i ∈ J ∖ {k};
- (b) C_p is not pointwise φ_k-minimal: some non-null set carries an arrow out of C_p with δφ_k < 0.

Then (RB) fails.

*Proof.* Let v be the change on A. Then Φ_J(v) = 0 and Ψ_i(v) < 0 for i ∈ J ∖ {k}, so I(v) ⊆ {k}. The arrow of (b) gives
s with Φ_k(s) < 0. Apply Theorem 3.3. ∎

*Reading.* On a mixed pair with odd world o, the only changes that improve two worlds and worsen the third are the moves
S → M and O → M (with k = o). So (a) at an interior index says: C_p is silent or rejecting on a non-null set where the
leading penalties do not distinguish its advice from acceptance at any world. Such a model must pay no improvable
leading cost at the odd world. This is the brief's "natural adversary": the leading changes cancel exactly at k (and are
made slightly favourable by δs), while the lower-level gain at the other two worlds stays fixed.

If the change on A were strictly Φ-improving at the two other worlds, Prop 3.1 would force C_p to be φ_k-minimal, and
(b) would fail. So Cor 3.5 concerns exactly the leading-blind regions that GG1 Lemma 2.2 proposed for protecting T1.

**Corollary 3.6 (at T1; PROVED).** Let T1 = C_{q₀}, supp q₀ = Ω (necessary; see Prop 5.3(b) for (NT) designs, and
HH1 Lemma 2.2 in general), and let (RB) hold. If T1 pays an improvable leading cost at world k, then on a.e.
two-positive pair with odd world k on which T1 is silent or rejecting, φ(h, M) ≠ φ(h, T1(h)) at some world. This is
Cor 3.5 at q₀. More generally, Cor 3.4 holds at q₀.

GG1 Prop 4.1 (transferred by HH2 §6) says that T1 or interior selected models must pay leading costs. Cor 3.4–3.6 say
which records out of such models must then be visible at the leading level.

---

## 4. The tie-free design: a conditional full cover

**Definition (NT).** The selection is **(NT)** if, for every p ∈ Δ, every model X with Φ_i(X) ≤ Φ_i(C_p) for all
i ∈ supp p equals C_p a.e. That is, C_p is the unique model whose leading costs at the active worlds do not exceed its
own. By Lemma 1.1 it is equivalent to require this for relaxed records: m(w; p) = 0 whenever Φ_{supp p}(w; p) ≤ 0.

**Theorem 4.1 (PROVED).** Let Φ = (Φ_1, Φ_2, Φ_3) be integrable and weakly guiding. Let p ↦ C_p be a selection of
coherent models, continuous in measure, with T1 = C_{q₀}, that is (NT). Let Ψ be ANY integrable strictly guiding field.
Then:
- (RB) holds;
- with the rate k of AUDIT_HH_rate, the rate system 𝒜^k is a full cover of T1 under (FC). Every axiom of Theorem 2.4
  holds, for arbitrary measurable competitors.

*Proof.* (NT) makes (ND) vacuous: no relaxed record with m > 0 has Φ_{supp p} ≤ 0. So Theorem 3.2 gives (RB). (NT)
gives (U) (Lemma 2.3(c)), hence (A1) and (A2). Theorem 2.4 applies. ∎

*Reading.*
- The second level is completely free. Its only roles are strict (G) and the tie structure of 𝒜^k. The exchange rate
  is only needed against records whose leading increment is small and positive: no record with leading increments ≤ 0
  at all active worlds remains to be defended.
- Viewed alone, Φ is an additive ranking that satisfies every axiom of a cover except the strict half of (G). Its
  sections {p : Φ_i(C_p) ≤ Φ_i(X)} are closed and its selection is competitive. Then:
  - the lexicographic tie-break by Ψ restores strict (G) but destroys closed sections (FF2 Lemma 2.4; AA1.3);
  - the rate rule restores closed sections and keeps strict (G), at the price of transitivity, keeping (FC).

  So **within the exchange-rate class, the T1 question for tie-free designs is exactly the question of a "cover by an
  additive ranking with weak guidance, strict at the selection" (P_w of §0).**

**Proposition 4.2 (the barriers are respected; PROVED).** Every design as in Theorem 4.1 on the full domain has the
following properties.
- (a) Interior selected models near each vertex pay leading costs at the other worlds. So GG1 Prop 3.1 / Prop 4.1 and
  HH2 §6's transfer are met without a hypothesis.
- (b) HH2 Lemma 3.1 (vertex lemma) is a consequence of Theorem 4.1's closed sections and competitiveness. It is
  consistent with the selection because the selection is continuous at the vertices.
- (c) Φ charges the bulk near T1: every non-best advice is charged at every world (Prop 5.2(a)). So FF2 Cor 4.2 does
  not bind.
- (d) If the bad~silence zero set of some world k (Prop 5.2) meets the k-wrong advice of some selected C_q with
  k ∈ supp q, inside some H_n, then (Loc_k) fails for every ℓ_k (Prop 2.2(b)). So HH2 Thm 5.1 is escaped at k.
- (e) Q4.2 / M0closed(b) ("some world does not add up") hold for arbitrary relations (HH1 §2.2). They are therefore not
  hypotheses to check: they are consequences that any such design satisfies.

*Proof.*
- (a) By Prop 5.2(a), Φ_i(B^j) > Φ_i(B^i) = min Φ_i for j ≠ i, because B^j is i-wrong on a non-null set and strict-best
  charges it. Continuity in measure gives Φ_i(C_q) → Φ_i(B^j) as q → e_j.
- (b) As stated.
- (c) Prop 5.2(a).
- (d) The move from the k-wrong acceptance to silence is Φ_k-blind and k-improving. The move to × is Φ_k-charged
  (× strictly worst; Prop 5.2(b)).
- (e) As stated. ∎

---

## 5. Can the tie-free design pass through T1?

**Proposition 5.1 (on M_U: no; PROVED modulo the write-up's Theorem main and Cor coverage, refereed twice).** On M_U no
design as in Theorem 4.1 exists.

*Proof.*
1. **Strict guidance.** At e_k, (NT) says that B^k is the unique minimiser of Φ_k. On M_U each pair h ∈ U has two
   available advices, one k-right and one k-wrong. If φ_k(h, wrong) = φ_k(h, right) on a non-null set, switching B^k
   there keeps Φ_k. So φ_k is strictly guiding, at every world.
2. **Φ alone is an additive cover.** Consider the additive ranking X ≼_i Y ⟺ Φ_i(X) ≤ Φ_i(Y).
   - **(G), (IB).** Φ is strictly guiding and additive.
   - **Competitiveness.** If Φ_i(X) < Φ_i(C_p) for all i ∈ supp p, (NT) is violated.
   - **Closed sections.** {p : Φ_i(C_p) ≤ Φ_i(X)}, by continuity in measure.
   - **Undominatedness.** Every C_p is undominated, by (NT).
   - **(C).** If X is tied with some C ∈ C_L, then by Theorem kkm C is tied with some C_p. (NT) gives C = C_p, and then
     X = C_p.
   - **(LF), T1.** (LF) holds on M_U, and T1 = C_{q₀}.
3. **Contradiction.** This is an additive cover of T1 on M_U, which the write-up's Cor coverage excludes. ∎

**Proposition 5.2 (on the full domain: the shape of Φ; PROVED, (c) modulo Theorem gm).** Let a design as in Theorem 4.1
live on the full domain.
- (a) **Strict-best.** For a.e. h and every world k, the k-best advice is strictly cheapest:
  φ_k(h, best_k(h)) < φ_k(h, b) for all b ≠ best_k(h).
- (b) **× strictly worst, without loss of generality.** Replacing φ_k(h, ×) by max_a φ_k(h, a) + |h_k| preserves every
  hypothesis of Theorem 4.1. After this replacement the only zeros of Φ, that is pairs of advices with equal penalty at
  some world, are **bad~silence zeros**: φ_k(h, S) = φ_k(h, wrong acceptance).
- (c) **The zero set is non-null.** For some world k, the set Z_k of pairs carrying a bad~silence zero at k has
  μ(Z_k) > 0.

*Proof.*
- (a) (NT) at e_k, as in Prop 5.1 step 1, now with all four advices.
- (b) Coherent models never give ×, so Φ(C_p) is unchanged. Every model's Φ weakly increases, so (NT) persists:
  Φ′_J(Y) ≤ Φ′_J(C_p) gives Φ_J(Y) ≤ Φ′_J(Y) ≤ Φ_J(C_p), hence Y = C_p. Integrability, weak guidance and continuity are
  unaffected. A zero at world k is a pair of equal penalties at k. By (a) it cannot involve best_k, and by the
  replacement it cannot involve ×. So it is S ~ wrong acceptance.
- (c) If every Z_k is null, Φ is strictly guiding a.e. Then Prop 5.1 step 2, verbatim, makes Φ alone an additive cover
  of T1 on the full domain, which Theorem gm excludes. ∎

**Proposition 5.3 (FF2 Steps 1–5 hold for the leading field; PROVED).** Let a design as in Theorem 4.1 live on the full
domain, with × strictly worst (Prop 5.2(b)). Then:
- (a) the field Φ has property (γ): for a.e. w ∈ int Δ, the w-Bayes model of Φ is a.e. unique, and it is a selected
  (coherent) model;
- (b) T1 is a weak Bayes model of Φ at some w ∈ int Δ, and supp q₀ = Ω.

So Φ meets every standing hypothesis of FF2 Thm 4.1 Step 6 (D1 → BB2 Thm 6.1 → M3.7/M3.8) except strict guidance. It
fails strict guidance exactly on the non-null bad~silence zero sets.

*Proof.*
- (a) Prop 3.1 gives W_Φ(q) ∩ Δ_{supp q} ≠ ∅ for every q, closed graph, and covering of int Δ.
  - **No fully blind pairs.** At a mixed pair, M is best at some world and O at another. By (a) of Prop 5.2, every pair
    of advices from {M, S, O} is strictly separated at some world. × is strictly worst everywhere.
  - So for a.e. h and a ≠ b, φ(h, a) − φ(h, b) is either not proportional to 𝟙 (zero set in Δ a line) or of constant
    strict sign.
  - Fubini gives null ties for a.e. w. Covering gives a q with w ∈ W_Φ(q), so the unique w-Bayes model is C_q. This is
    FF2 Step 4.
- (b) FF2 Step 5 verbatim, using Prop 5.2(a). Near (1, 1, −t) T1 is silent and acceptance is strictly cheaper at
  worlds 1 and 2, which excludes two-world weights. At a vertex weight T1 would be world-1-best. So w ∈ int Δ. Since
  w ∈ Δ_{supp q₀}, supp q₀ = Ω. ∎

*Where the open point sits.* The write-up's permitted-tie analysis (§sec:open-ties, Theorem permitted) records that the
chain of Theorem main uses "strict badness (c_i < 0 where g_i < 0, never tied)". Bad~silence zeros are exactly the
failure of strict badness. That is the zero-pattern residual of N9.9 / N10 (C-i) / R16 §2.8 / N26 §5, which no earlier
round closed. So P_w is closed negatively if, and as far as I can see only if, some form of the Step 6 chain is proved for
strict-best fields.

**Proposition 5.4 (what the zero sets force on the selection; PROVED).** Let a design as in Theorem 4.1 live on the full
domain. Index pairs by majority orientation (positive worlds j, l, odd world o). Put:
- Z^odd := {h : φ_o(h, S) = φ_o(h, M)}, a bad~silence zero at the odd world;
- Z^maj := {h : φ_j(h, S) = φ_j(h, O) and φ_l(h, S) = φ_l(h, O)}, bad~silence zeros at both positive worlds.

Then:
- (a) for every q ∈ Δ, C_q is not silent on a non-null part of Z^odd ∪ Z^maj. In particular T1 accepts h or −h for
  a.e. h ∈ Z^odd ∪ Z^maj;
- (b) for a.e. h ∈ Z^odd ∪ Z^maj there is a non-vertex q ∈ Δ with K_q ⊆ h^⊥. Hence, if Z^odd ∪ Z^maj is non-null, the
  selection contains uncountably many distinct non-vertex models whose credal sets have dimension at most one.

*Proof.*
1. **(a) on Z^odd.** At q with supp q ∋ o, the change S → M on Z^odd ∩ {C_q = S} is Φ_o-neutral. It is weakly
   Φ_j-improving and Φ_l-improving, since M is j- and l-best. So it has Φ_{supp q} ≤ 0, and (NT) makes it null.
   - If o ∉ supp q, the same change has Φ_{supp q} ≤ 0 again.
   - At e_o, C = B^o gives O on Z^odd, since h_o < 0.
2. **(a) on Z^maj.** The change S → O there is Φ_j- and Φ_l-neutral and Φ_o-improving.
3. **(b), the switching set.** K_q is Hausdorff-continuous in q, since D_K are cones with interior (R1 Prop 3.1, as in
   the write-up's Prop reduction(b)). So P(q, h) := min_{m∈K_q} m·h is jointly continuous, and
   S_h := {q : P(q,h) ≤ 0, P(q,−h) ≤ 0} is closed in Δ.
4. **(b), Fubini.** By (a) and Fubini on Δ × (Z^odd ∪ Z^maj), for a.e. h the set S_h has Lebesgue measure 0, hence empty
   interior.
5. **(b), the two open regions.** Put M_h := {P(q,h) > 0} and O_h := {P(q,−h) > 0}. They are relatively open, disjoint,
   and cover Δ ∖ S_h.
   - K_q → {e_o} as q → e_o (C_{e_o} = B^o = D_{{e_o}} and continuity), so O_h contains a neighbourhood of e_o.
   - Likewise M_h contains a neighbourhood of e_j.
6. **(b), connectedness.** S_h has empty interior, so cl M_h ∪ cl O_h = Δ. Since Δ is connected, some q lies in
   cl M_h ∩ cl O_h. There P(q, h) ≥ 0 ≥ −P(q, −h), so m·h = 0 on K_q. Vertices are excluded because h has no zero
   coordinate.
7. **(b), uncountably many.** A segment K_q serves one direction ±h. A point K_q = {m} serves the great circle m^⊥. The
   directions of a non-null set of pairs form a set of positive measure on the sphere, which no countable union of great
   circles and points covers. ∎

*Reading.* Odd or double bad~silence zeros cannot sit where any selected model is silent. Each pair carrying one must be
switched, as the index moves from e_o to e_j, through selected models with degenerate credal sets. This is a zero-pattern
analogue of the "precise collars" of Theorem gm's route I2. Theorem A of the short route excludes injective precise open
regions for strictly guiding covers, but not degenerate switching curves for strict-best fields. Single-world zeros
(Z_j alone) force nothing of this kind.

---

## 6. Designs that break leading ties with the second level

**Proposition 6.1 (the plain posterior family is not lexicographic Bayes at its own index; PROVED; inputs CHECKED).**
Let L be any lexicographic base with finitely many additive levels φ^1, …, φ^m, measurable at each pair, the last
strictly guiding. Then there is a non-null open set G of pairs with the following property: for a.e. h ∈ G, the plain
posterior advice C_p(h) fails to be a weak lexicographic p-optimal advice at h for some p ∈ int Δ.

*Proof.*
1. **Two interface lines.** Use the posterior formula (HH2 §4.1; recomputed from the definition in the script). For a
   pair h with odd world o, the O-region is {p : g_j(p) < 0, g_l(p) < 0}, with g_k(p) := p·h + λp_kh_k, and the M-region
   is {g_o > 0}.
   - CHECKED (`wedge.py` → `wedge.out`, ε ∈ {1/20, 3/10, 1/2, 9/10}, h = (3, 1, −2)): for each ε there are exact points
     x_j ∈ int Δ on {g_j = 0} with g_l(x_j) < 0 and g_o(x_j) < 0, and x_l on {g_l = 0} with g_j(x_l) < 0 and
     g_o(x_l) < 0.
   - At each of them the advice on the two sides of the line is O and S.
   - The two lines are distinct.
   - All conditions are strict, so they persist on a neighbourhood G of h. Each line then carries a segment of positive
     length along which the O-region borders the S-region with no M nearby.
2. **One line from the base.** Fix h ∈ G and suppose C_p(h) is weakly lexicographic p-optimal for every p ∈ int Δ. Let
   ℓ_r(p) := p·(φ^r(h, S) − φ^r(h, O)), and let r* be the first r for which ℓ_r is not identically zero on aff Δ. It
   exists: the last level is strictly guiding with the sign pattern of the mixed pair, so its ℓ is not proportional to 𝟙.
3. **Separation by that line.** On the O-region, O is weakly lexicographic ≤ S, so ℓ_{r*} ≥ 0. On the S-region,
   ℓ_{r*} ≤ 0. By continuity ℓ_{r*} = 0 on both interface segments. Then ℓ_{r*} is not constant, so its zero set is one
   line, and it contains two segments of distinct lines. Contradiction. ∎

*Consequence.* "Design base and selection together" cannot mean "the plain family is the lexicographic Bayes family of
the base". By Prop 3.1 a rate cover with the plain family needs weak Bayes weights α(p) ≠ p somewhere, or leading ties
at p. The ties are governed by Cor 3.4–3.5.

*Where the tie designs stand (PROVED pieces assembled; no new theorem).*
- **Plateau designs** (VB, the T1-shadow of the write-up's Theorem M11):
  - near the plateau every world is in W(p), so (ND) holds there. The design fails only because the selection jumps at
    the vertices (HH2 Prop 3.2; for the shadow, the selection is T1 on int Δ and B^k at e_k);
  - with a continuous selection, GG1 Prop 3.1 (transferred, HH2 §6) and continuity force leading costs near the
    vertices (as in Prop 4.2(a)).
- **Continuous tie designs.** Every selected model that pays an improvable leading cost at world k must satisfy
  Cor 3.4. Every fully blind record out of it that improves the two other worlds is excluded (Cor 3.5). At T1, Cor 3.6
  applies.
- **Free sets** are excluded by Lemma 2.5 with N9 Prop 4.5.
- **What remains.** Tie designs whose blind records out of leading-paying models only ever hurt several worlds jointly
  certified as Bayes (Cor 3.4 with |I(v)| ≥ 2), together with the uniformity of (ND). No member through T1 was
  constructed.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | Aumann–Lyapunov: relaxed and actual increment ranges coincide; proportional restrictions | PROVED (standard) |
| 1.2 | Young limits of records along a continuous selection | PROVED |
| 2.1 | corrected HH2 6.1(e): constant rate excluded; fixed records, and bounded-ratio records uniformly, lexicographic at small scale; NOT uniformly: a blind improvement gives lex-accepted rejected records at every scale | PROVED; CHECKED (`rate_example.py`) |
| 2.2 | exact condition for (Loc_i) in a rate world; ℓ-free escape from HH2 Thm 5.1 | PROVED |
| 2.3 | (U) ⇒ (A1), (A2); strict lex-Bayes ⇒ (U); (NT) ⇒ (U) | PROVED |
| **2.4** | **corrected Cor 6.2: (H1)–(H4) ⇒ full (FC) cover, every axiom** | **PROVED** |
| 2.5 | in every rate cover, lex-undominated models are coherent (selected under (A2)); free sets excluded | PROVED (free sets: with N9 Prop 4.5, imported) |
| 3.1 | lex competitiveness ⇒ weak Bayes weight for Φ; closed graph and covering | PROVED (FF2 Steps 1–3) |
| **3.2** | **(ND) ⇒ (RB)** | **PROVED** |
| **3.3** | **explicit adversarial family: (AD) ⇒ ¬(RB)** | **PROVED; CHECKED (`adversary.py`)** |
| 3.4 | (RB) ⇒ weak λ-Bayes on I(v) | PROVED |
| 3.5, 3.6 | blind majority moves out of leading-paying models defeat every rate; the T1 form | PROVED |
| **4.1** | **every (NT) design through T1 is a full (FC) cover, for any strictly guiding Ψ** | **PROVED** |
| 4.2 | GG1 3.1/4.1, vertex lemma, FF2 4.2, Thm 5.1, Q4.2 all respected | PROVED |
| 5.1 | no (NT) design on M_U | PROVED mod Theorem main / Cor coverage |
| 5.2 | full domain: strict-best, × WLOG, non-null bad~silence zeros | PROVED ((c) mod Theorem gm) |
| 5.3 | Φ satisfies FF2 Steps 1–5; only Step 6 (strict badness) is missing | PROVED |
| 5.4 | odd/double zeros avoid all silent regions; uncountably many degenerate switching models | PROVED |
| 6.1 | plain posterior family not lexicographic Bayes at its own index for any finite-level additive base | PROVED; CHECKED (`wedge.py`, 4 values of ε) |
| P_w | existence of a strict-best weakly guiding Φ with an (NT) selection through T1 | **open** (no CONJECTURE offered) |
| — | cover of T1 | **not obtained** |

**Sharpest proved statement.** Take the class of HH2 §6: additive two-level bases, a selection coherent and continuous
in measure through T1, the rate rule.
- **Positive.** A full cover of T1 under (FC) exists as soon as the leading field admits a strict-Pareto (NT) selection.
  Then (RB), competitiveness against every measurable competitor, admissibility, (C) and every other axiom follow, for
  any strictly guiding second level (Theorems 4.1, 3.2, 2.4).
- **On M_U.** No such leading field exists (Prop 5.1).
- **On the full domain.** Such a field must be strict-best with a non-null set of exact bad~silence zeros (Prop 5.2). It
  satisfies every hypothesis of FF2 Thm 4.1's field contradiction except strict badness (Prop 5.3). Its odd and double
  zeros force uncountably many degenerate switching models (Prop 5.4).
- **Tie designs.** Designs that instead break leading ties with the second level fail (RB) whenever a fully blind record
  improving two worlds leaves a selected model that pays a leading cost at the third (Cor 3.5). More generally, they fail
  whenever the worlds of I(v) cannot jointly certify the model as a leading-field Bayes model (Theorem 3.3, Cor 3.4).

**Referee priorities.**
1. Theorem 3.2 step 4: that W(p*) is defined with a neighbourhood. This is exactly what the uniformity in p needs.
2. Lemma 1.2: weak-* compactness, and the replacement of C_{p_n} by C_{p*} in the support mass.
3. Theorem 2.4 step 4: the order "C ≈ C_p, then C = C_p, then X = C_p", which uses (A2) twice and (A1) once.
4. Prop 5.2(b): that raising φ(×) preserves (NT).
5. Prop 5.4(b): Fubini needs the joint closedness of {(q, h) : C_q(h) = S}, which uses Hausdorff continuity of K_q.

## 8. Files (`ii1py/`)

- `rate_example.py` → `rate_example.out`: Prop 2.1(ii)–(iii). Lexicographically accepted, rate-rejected records at five
  scales; the exact small-scale threshold for a fixed record.
- `adversary.py` → `adversary.out`: Theorem 3.3 / Cor 3.5 on an exact two-cell instance. Guidance of both levels, strict
  lexicographic u-Bayes advice, I(v) = {3}, Φ_3(s) < 0, and r(u, X_δ) = (1 − δ)/δ → ∞ at support mass ≥ 1.
- `wedge.py` → `wedge.out`: Prop 6.1. Two distinct O/S interface lines of the plain posterior family, for
  ε ∈ {1/20, 3/10, 1/2, 9/10}, computed from the definition C_p = {g : p⊙g ∈ D_{T1}}.
