# M3. The fixed point on every decomposable domain: ladder endorsers, local one-sidedness at p*, and the non-degenerate branch closed along route I1

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up or
refereed notes mark proved, each named), **CHECKED** (a step-by-step reading against the cited proofs, not a
re-derivation), **CONJECTURE**, **NUMERICS** (`m3py/`, run with `python3 -I`; no proof rests on it). No assumption is
added: every hypothesis below is either a hypothesis of the T1 question or is stated as the hypothesis of a theorem.
Notation: write-up §§2, 5, 6, 7.5–7.7; L4 §§1–2; K3 §§1–2; D1; B2 + B2_referee; I1 + I1_referee; N21 §§2–3, 6; N28 §3;
R10b §5. T = T1, n = 3, Ω = Δ°, H = representatives of pairs, M = mixed pairs.

---

## 0. Outcome

**The extension holds, positively, on every decomposable domain with (LF) on which both acceptances are available
(this includes every domain that is two-sided near ∂D_{T1}). On such domains every cover of T1 by a ranking whose worlds
satisfy (NC) forces every endorser tuple to be degenerate (a non-null blind set of the ladder), exactly as L4 found on
M_U. One input is CHECKED rather than PROVED. Outside the availability class, one precise step is missing.**

> **Theorem M3.10 (PROVED except one CHECKED input, Prop. M3.9).** Let 𝓜 be a decomposable domain with (LF) at D_{T1}
> such that **(Av)** a.e. mixed pair has both acceptances in its advice range. Let a ranking on 𝓜 satisfy strict (G),
> (IB), (LA), (S) with closed sections for every model, (C), T1 ∈ C_L, and (NC) at every world. Then for **every**
> endorser tuple ν the ladder field ψ^ν of §1 has a world k whose ladder density vanishes on a non-null subset of the
> ladder Γ_k. Equivalently, some world has a non-null canonical blind set Λ_k ⊆ Γ_k (Thm M3.1(c)).
>
> (Av) holds on every domain that is two-sided near ∂D_{T1}, for every ranking with these axioms (L3 Prop. L3.1(a),
> PROVED in L3, not yet refereed).

What each step gives:

1. **Normal form (§1; PROVED).** On a general decomposable domain a world's background order ranks the advice range
   A(g) of each pair. A model is encoded by its **ladder** profile: one indicator per rank step. For a {+,0,−} pair
   there are two steps:
   - the *silence increment* (rank ≥ 1: not good);
   - the *wrong increment* (rank ≥ 2: bad).

   Relevant comparisons, (NC) and the Hahn–Banach endorsers transfer to L^∞ of the ladder, with every part of K3.1
   unchanged (Thm M3.1).
2. **A pair of charges, not one graded charge (Prop. M3.2; PROVED).** The endorser of a world is a charge on its ladder,
   i.e. a pair (ν^s_k, ν^w_k). No axiom, (IB) included, reduces it to one charge on graded errors, i.e. to ν^w = ν^s
   (bad costs twice silence).
   - The single graded charge is not merely unforced: it is **incompatible** with every non-degenerate fixed point.
   - At such a fixed point, Σ_k p*_k (w_k − s_k) > 0 a.e. on T1's silent two-sided pairs: on p*-average, the wrong
     increment strictly exceeds the silence increment wherever T1 is silent.
3. **The fixed point (Thm M3.4; PROVED).** This is L4.1 on every decomposable domain. Every endorser tuple is undefeated,
   with zero gap at every t ∈ Δ. Its countably additive ladder field ψ^ν has properties (γ₀) and admissibility:
   - (γ₀): a **coherent ψ^ν-t-Bayes model in 𝓜 at every t ∈ Δ**, boundary and exceptional weights included;
   - admissibility: **T1 ψ^ν-Bayes at some p* ∈ Δ**.

   If ψ^ν is strictly guiding, then p* ∈ Ω. Boundary p* forces joint blindness, of both ladder steps, of the worlds in
   supp p* on their joint T1-error sets.
   - **By-product (Cor. M3.5; PROVED).** Claim B2.0, the general-domain M0 reduction that B2_referee rated a
     documentation GAP, is now proved. With it, Cor. D1.7 holds at the status of Theorem D1.
4. **Theorem gm does not apply as it stands (§4, audit).** The fixed-point field satisfies three of gm's inputs:
   - integral penalties with an integrable envelope (always);
   - strict guidance (iff non-degenerate);
   - Prop. necessary (b)–(d) (always).

   It satisfies Prop. necessary(a) (a.e.-unique Bayes model at **every** interior q) only if E(ψ) = ∅. So D1 (p* ∉ E)
   together with gm leaves exactly D1's open branch, E ≠ ∅ ∌ p*.
5. **Local one-sidedness at p* (Lemma M3.6; PROVED, new).** If ψ is a strictly guiding integral (γ)-field with T1 its
   unique Bayes model at p* ∈ Ω, there is a ball B₁ ∋ p* on which, for **every** q ∈ B₁ and every tie-breaking:
   - near-facet pairs behave exactly as on a U-domain: rejection is never weakly optimal, and the cells are the
     half-planes {c·q > 0};
   - every non-null tie at q is an accept-vs-silence tie of a near-facet pair, frozen along its whole chord inside B₁;
   - P^A(·, g) is quasi-linear at near-facet levels.

   So inside B₁ a two-sided field **is** a U-domain field, and chords accumulating at p* are handled by the U-domain
   audit Prop. chainchords.
6. **Route I1 across chords (Props. M3.7, M3.8; PROVED).** Under (Av), and given (C2) (TS), (PC), (NS) at p* and (C3)
   the unique clusters, route I1 runs for every strictly guiding (γ₀)-field with any null E ∌ p*. The proof uses only:
   - priors q ∉ E;
   - edge confinement and precise vertex limits, which (Av) gives directly;
   - the fact that pinned chart lines carry no atoms.
7. **(C2), (C3) for such fields (Prop. M3.9; CHECKED).** These are Thm TS plus TSalways:
   - their local steps by M3.6 and the chainchords audit;
   - their global wall steps by D1.6's wall-across-chords argument.

| | Statement | Label |
|---|---|---|
| M3.0 | normal form: ranks, ladder Γ_k, relevant comparisons | PROVED |
| M3.1 | K3.1 on the ladder: endorsers ⇔ (NC); p.f.a. localization; canonical blind set Λ_k ⊆ Γ_k | PROVED |
| M3.2 | endorsers are pairs (ν^s, ν^w); single graded charge impossible at non-degenerate fixed points | PROVED; NUMERICS |
| M3.3 | absorption on the ladder | PROVED |
| M3.4 | fixed point: undefeated, (γ₀) at every t ∈ Δ, admissible; interior or joint ladder-blindness | PROVED |
| M3.5 | Claim B2.0 proved; Cor. D1.7 unconditional | PROVED |
| M3.6 | local one-sidedness at p* (uniform B₁, U-type cells, frozen near-facet ties, local quasi-linearity) | PROVED; NUMERICS |
| M3.7 | (γ)-fields: exact chart form off E; K^♭ exact everywhere; edge confinement and K → {e_b} under (Av) | PROVED |
| M3.8 | route I1 for (γ₀)-fields given (C2), (C3) | PROVED (transfer written out) |
| M3.9 | (C2), (C3) for non-degenerate (γ₀)-fields, chords allowed | CHECKED |
| M3.10 | non-degenerate fixed points are impossible on (Av)-domains | PROVED except M3.9 |
| M3.11 | vertex ties come only from silence-blind ladder steps | PROVED |
| Q_M3 | (a) degenerate (ladder-blind) fixed points on (Av)-domains; (b) domains without (Av) other than U-domains | open |

---

## 1. Normal form on a general decomposable domain

**Ranks.** Let A(g) be the advice range of the domain (write-up Remark advicerange) and A′(g) := A(g) ∖ {×}.
- For a.e. mixed g and each world k (g_k ≠ 0 a.e.), the advices good, silent, bad, × have distinct world-k background
  ranks. Write r_k(g, a) ∈ {0, …, |A′(g)| − 1} for the rank of a within A′(g) at world k.
- Example: for A′(g) = {+,0,−}, r_k is 0, 1, 2 for good, silent, bad. For A′(g) = {+,0} with g_k < 0, silence has rank 0
  and + has rank 1.
- A model is **regular** if it is correct on a.e. unanimous pair and gives contradictory advice on a null set only.
  Coherent models are regular.

**Ladder.** Γ_k := {(g, j) : g ∈ M, 1 ≤ j ≤ |A′(g)| − 1}, with the measure μ ⊗ counting. The ladder profile of a regular
X at world k is λ_k(X)(g, j) := 1[r_k(g, a_X(g)) ≥ j].

**Lemma M3.0 (normal form; PROVED).**
- (a) Two regular models with the same ladder profile at world k agree a.e.
- (b) Strict (G) at world k says exactly two things about ⪯_k on regular models:
  - λ_k(X) ≤ λ_k(Y) a.e. implies X ⪯_k Y;
  - strict inequality on a non-null set implies X ≺_k Y.
- (c) For a {+,0,−} pair, ladder step 1 is the **silence error** (the model is not correct) and step 2 is the
  **wrong-acceptance error** (the model accepts the world-k-wrong orientation).

*Proof.*
- (a) Distinct advices in A′(g) have distinct ranks, and the ladder profile determines the rank.
- (b) The background order on A′(g) is the order of r_k, and r_k(g,a) ≤ r_k(g,b) iff the ladder indicators of a are
  ≤ those of b.
- (c) is the definition. ∎

**Relevant comparisons and (NC).**
- 𝔚_k := {δ = λ_k(X) − λ_k(B) : B ∈ C_L, X regular, B ⪯_k X}. These are L4's relevant comparisons, read in ladder
  coordinates.
- (NC_k): no finite nonnegative combination of members of 𝔚_k is ≤ −1 a.e. on Γ_k.
- Endorsers: 𝒩_k := {ν ∈ ba₊(Γ_k) : ν(Γ_k) = 1, ν(δ) ≥ 0 for every δ ∈ 𝔚_k}, where ba₊ consists of the charges that
  vanish on null sets.

**Ladder field.** Write ν = ρ_ν(μ⊗#) + π_ν (Yosida–Hewitt), and define the penalty
ℓ^ν_k(g, a) := Σ_{j ≤ r_k(g,a)} ρ_ν(g, j), for a ∈ A′(g). On unanimous pairs and on × use any fixed strictly guiding
integrable penalty (these coordinates never enter a relevant comparison).
- ψ^ν is an additive field on 𝓜 with integral penalties and integrable envelope Σ_j ρ_ν(·, j).
- It is weakly guiding, and **strictly guiding iff ρ_ν > 0 a.e. on Γ_k for every k**.
- For a {+,0,−} pair write s_k := ρ(g,1) (silence increment) and w_k := ρ(g,2) (wrong increment). Then:

  | advice | world k with g_k > 0 | world k with g_k < 0 |
  |---|---|---|
  | + | 0 | s_k + w_k |
  | 0 | s_k | s_k |
  | − | s_k + w_k | 0 |

  So c_k = ℓ_k(0) − ℓ_k(+) equals s_k (g_k > 0) or −w_k (g_k < 0). Likewise c′_k equals −w_k or s_k, and
  d_k = ±(s_k + w_k).

**Theorem M3.1 (K3.1 on the ladder; PROVED).** Assume strict (G) at world k (and the other axioms only to define C_L).
- (a) 𝒩_k ≠ ∅ iff (NC_k).
- (b) For ν ∈ 𝒩_k there is a localizing family D^ν ⊆ Γ_k with π_ν(Γ_k ∖ D^ν_m) ≤ 2^{−m}, and ∫ρ_ν δ ≥ 0 for every
  D^ν-localized δ ∈ 𝔚_k.
- (c) There is ν* ∈ 𝒩_k whose density is positive exactly off a set Λ_k ⊆ Γ_k (unique mod null), with ρ_ν = 0 a.e. on
  Λ_k for every ν ∈ 𝒩_k.
- (d)–(f) The non-localizable blind set, (S_int) ⇔ Λ_∞ null, and ratio certificates, verbatim.
- If world k **adds up** in the general sense of B2 Prop. B2.0 (a bounded strictly guiding λ_k and a weight positive on
  non-null sets of problems with non-singleton advice range, endorsing all relevant comparisons), then Λ_k is null.

*Proof.* K3.1's proofs use only that the space is a finite measure space and that 𝔚 is a set of bounded functions:
- Hahn–Banach against 𝒦 = cone 𝔚 + L^∞₊;
- the lattice infimum π ∧ μ;
- countable mixtures;
- duality with ratio certificates.

They apply verbatim on (Γ_k, μ⊗#), which has total mass at most 2μ(M).

For the last clause, put ν̂(A × {j}) := ∫_A (λ_k(g, a_j) − λ_k(g, a_{j−1})) dν_k(g), with a_j the advice of rank j. Then:
- ν̂(δ) = ν_k(λ_k(·, a_X) − λ_k(·, a_B)) ≥ 0 on 𝔚_k;
- its density is ρ_{ν_k} times the λ-increments, which is > 0 a.e. The factor ρ_{ν_k} > 0 a.e. by the last bullet of
  K3.1(c) (N19 Lemma R1), whose proof is about charges only. The λ-increments are > 0 by strict guidance of λ_k. ∎

---

## 2. A pair of charges, not one graded charge

**Proposition M3.2 (PROVED).**
- (a) The dual object of §1 is a charge on Γ_k. On {+,0,−} pairs this is a pair (ν^s_k, ν^w_k) on M.
  - A single charge on graded errors (cost ∫ r_k dν) is the special case ν^w = ν^s.
  - Nothing in the axioms reduces the pair to this case. (IB) in particular is used nowhere in §§1–3: the Hahn–Banach
    step and absorption need only strict (G), (LA), (S) and relevance.
- (b) Let ψ be a strictly guiding integral field with (γ) whose Bayes model at some p* ∈ Ω is D_{T1} (for instance a
  non-degenerate fixed point, Thm M3.4). On a.e. pair g ∈ M at which T1 is silent and A′(g) = {+,0,−}:

  Σ_k p*_k (w_k(g) − s_k(g)) > 0.

  In particular **no non-degenerate fixed point has single graded charges at every world**. The same is true whenever
  w_k ≤ s_k for all k on a non-null part of T1's silent two-sided pairs.
- (c) The set in (b) is non-null on every domain that is two-sided near ∂D_{T1}. It contains h − s𝟙 for h near the
  middle arc of any facet and 0 < s < P̄_{T1}(h).

*Proof of (b).* T1 is ψ-p*-Bayes, so silence is p*-optimal on such g. With the table of §1:
- c·p* = Σ_{g_k>0} p*_k s_k − Σ_{g_k<0} p*_k w_k ≤ 0;
- c′·p* = Σ_{g_k<0} p*_k s_k − Σ_{g_k>0} p*_k w_k ≤ 0.

Adding the two gives Σ p*_k s_k ≤ Σ p*_k w_k. If equality held on a non-null set, both inequalities would be equalities
there, so +, 0 and − would all be optimal: a non-null set of apex ties at p*. B2.1(d) excludes this. B2.1 needs only
strict guidance, integral penalties, (γ) and D_{T1} Bayes at an interior weight; it needs neither (LF) nor D1. ∎

*Proof of (c).* P_{T1}(h − s𝟙) = −s < 0, and P_{T1}(−h + s𝟙) = s − P̄_{T1}(h) < 0. These gambles lie in N′, where the
advice range is {+,0,−}. ∎

NUMERICS (`m3py/m3_checks.py` (1)):
- 0 sign-pattern violations of c, c′, d;
- 0 violations of q·s ≤ q·w among 21 800 random silence-optimal instances;
- with s = w, silence is never weakly optimal off apex ties.

*Remark.* The pair matters for the geometry. With ν^w = ν^s one gets c′ = −c, so the silence cell
{c·q ≤ 0, c′·q ≤ 0} collapses to the line {c·q = 0}: a single graded charge makes every interior Bayes model precise.
T1 needs a genuinely two-dimensional silence cell, so it needs w > s, i.e. ℓ(bad) > 2ℓ(silent), on the part of the
silent set that matters at p*.

---

## 3. The fixed point on every decomposable domain

Fix (H_𝓜): a decomposable domain 𝓜 ∋ D_{T1}; strict (G), (IB), (LA), (S) with closed sections, (C); T1 ∈ C_L; (NC_k) at
every world. Take an endorser tuple ν = (ν₁, ν₂, ν₃), ν_k ∈ 𝒩_k.

**Costs.**
- t·ν(X) := Σ_k t_k ν_k(λ_k(X)) for regular X.
- ψ^t(X) := Σ_k t_k ∫ λ_k(X) ρ_k is its countably additive part.
- Gap_t(ν) := inf_{coh} t·ν − inf_{reg} t·ν ≥ 0.
- d_t(ψ) := inf_{coh ∈ 𝓜} ψ^t − min ψ^t ≥ 0. The minimum is over all models of 𝓜. It is attained by a pointwise
  minimiser of ℓ^t(g, ·) over A′(g), chosen correct on unanimous pairs, hence regular.

**Lemma M3.3 (absorption; PROVED).** Gap_t(ν) ≥ d_t(ψ) for every t ∈ Δ.

*Proof (L4.0 on the ladder).*
1. **Localization.** π := Σ_k π_{ν_k} is purely finitely additive. By M3.1(b) (Step 1 of K3.1(b)) there are D_m ⊆ M,
   decreasing, with μ(D_m) → 0 and π((M ∖ D_m) × {1,2}) ≤ 2^{−m}.
2. **The purely finitely additive cost.** For each a ∈ {+,0,−}, the purely finitely additive cost of a model X is
   Σ_a π^t_a({g : a_X(g) = a}). Here π^t_a(S) := Σ_k t_k π_k({(g,j) : g ∈ S, j ≤ r_k(g,a)}) is a purely finitely
   additive charge, supported where a ∈ A′(g). Put OPT := inf over measurable selections of A′ of this cost.
   - Restricting a selection to D_m does not raise its cost.
   - So some selection A_m on D_m costs at most OPT + 2^{−m}.
3. **An upper bound.** Let B be a pointwise ψ^t-minimiser. Put X_m := B off D_m and A_m on D_m.
   - X_m is in 𝓜 (Remark advicerange) and regular (choose correct advice on unanimous pairs).
   - ψ^t(X_m) ≤ min ψ^t + ∫_{D_m} Σ_j ρ → min ψ^t.
   - The purely finitely additive cost is ≤ OPT + 2^{1−m}.
4. **A lower bound.** Every coherent C ∈ 𝓜 has ψ^t(C) ≥ min ψ^t + d_t and purely finitely additive cost ≥ OPT. ∎

**Theorem M3.4 (the fixed point; PROVED).** Under (H_𝓜), for every endorser tuple ν:
1. **(Undefeated.)** For every regular X there is C ∈ C_L with C ⪯_k X at every k and ν_k(C) ≤ ν_k(X) at every k.
   Hence Gap_t(ν) = 0 for every t ∈ Δ.
2. **(γ₀).** d_t(ψ^ν) = 0 for every t ∈ Δ, and the infimum is attained: some coherent model of 𝓜 is ψ^ν-t-Bayes, at
   every t ∈ Δ (vertices, edges and exceptional weights included).
   - If ψ^ν is strictly guiding, then (γ) holds.
   - The directional families D^δ_q of D1.1(a) and the strict-Bayes set D♭_q (silence on every tie) are then coherent
     at every q ∈ Ω.
3. **(Admissible.)** For a.e. g, T1's advice is p*-optimal over A′(g) for some p* ∈ Δ. That is, D_{T1} is
   ψ^ν-p*-Bayes.
4. **(Interior, or joint blindness.)**
   - If p* lies in the open edge (e_i, e_j), then on every non-null set of pairs where T1's advice is wrong at both
     i and j, ρ_i and ρ_j vanish on every ladder step separating T1's advice from an available advice correct at both.
     - If T1 accepts g with g_i, g_j < 0, this is s and w at i and j when the other acceptance is available, and w at
       i and j when only silence is.
     - If T1 is silent on g with g_i, g_j > 0, it is s at i and j.
   - If p* = e_i, the same holds for world i alone, on all of T1's world-i errors.
   - In particular, if ψ^ν is strictly guiding then p* ∈ Ω.

*Proof.*
1. Theorem kkm gives C ∈ C_L (selected, undominated) with C ⪯_k X at every k. Each of these comparisons is relevant,
   so ν_k(λ_k X − λ_k C) ≥ 0.
2. By M3.3, d_t ≤ Gap_t = 0.
   - **Attainment.** The coherent models of 𝓜 are compact for convergence in measure: the coherent models form a
     compact set (H1.0(a), R1 Prop. 3.1), and 𝓜 is closed in measure. If X_n → X in measure, the advice converges a.e.
     along a subsequence, so ψ^t(X_n) → ψ^t(X) by dominated convergence (envelope in L¹).
   - **(γ) under strict guidance.** For each g, its ties lie on at most three lines {v·q = 0} (v a difference of two
     penalty vectors, with mixed strict signs). By Tonelli, Z_q is null for a.e. q, and the unique Bayes model is
     then the coherent one.
   - **Directional families.** D1.1(a) uses (γ) only. D♭_q is the intersection of countably many generic D^θ_q (on
     every tie type θ·(tie vector) takes both signs), and an intersection of countably many coherent open cones is
     coherent mod null.
3. This is H1.1 steps 1–3 on the ladder, with the localization of L4.1 step 3.
   - For relevant T1 ⪯_k Y with Y = T1 on D_m: |π_k(δ)| ≤ 2^{−m′} for every m′ ≥ m, so ∫ρ_kδ ≥ 0.
   - If some measurable alternative selection on A ⊆ M ∖ D_m lowered all three countably additive costs, then
     Y := T1 altered there would be regular. T1 ⪯_k Y would hold at some k: by kkm T1 is tied with a selected C_p that
     is competitive on supp p, so C_p ⪯_k Y for some k ∈ supp p. This contradicts endorsement.
   - Lyapunov (finitely many alternatives) and separation give p^{(m)} ∈ Δ with p^{(m)}·(ℓ(g,a) − ℓ(g, a_{T1}(g))) ≥ 0
     for a.e. g ∈ M ∖ D_m and every a ∈ A′(g). Then take a limit p*.
4. Pointwise p*-optimality of T1's advice against the alternative named gives Σ_{k∈supp p*} p*_k Δℓ_k ≥ 0 with
   every Δℓ_k ≤ 0. So every term vanishes. The sets named are non-null:
   - T1 accepts gambles near r_ij inside D_{T1} with g_i, g_j < 0;
   - T1 is silent on h − s𝟙 for h near the middle arc of F_l, l the third index, which is positive at i and j.

   For strict guidance, the first set with silence as alternative (available by (LF)) already gives a contradiction
   when p*_l = 0. ∎

**Corollary M3.5 (PROVED).**
- (a) **Claim B2.0 holds.** Under strict (G), (IB), (LA), (S), (C), T1 ∈ C_L and (M0) in the general sense, every
  supporting assessment ψ satisfies (α*) at an interior weight, (β) at every weight, (γ) and (δ). By M3.1 (last
  clause), M3.4 applies with a strictly positive tuple.
- (b) Consequently Cor. D1.7 holds at the status of Theorem D1, not of Claim B2.0.
- (c) The analogues of L4.4 hold verbatim on the ladder:
  - an (M1) certificate with (NC) makes its negative set blind;
  - Λ_k ⊇ Λ_∞;
  - strongly (M1) worlds (failing (NC)) are the only worlds outside M3.4.
- (d) The analogue of L4.5 holds: the gap alone cannot decide.

---

## 4. Which inputs of Theorem gm the fixed-point field satisfies

The question is whether gm applies to ψ = ψ^ν. Theorem gm is stated for covers (rankings with (LA), (S), (C)), but its
proofs use these axioms only through Prop. necessary (a)–(d) and the field (CHECKED: a reading of §§5–6 of the
write-up; every "cover" statement there is used through K_q, the vertex models, or (BU)).

| input | where the routes use it | fixed-point field |
|---|---|---|
| integral penalties, integrable envelope | R1 Lemma 1.2 (Bayes = pointwise minimiser), R1 Prop. 3.1, Fubini, dominated convergence (all routes) | always (p.f.a. parts absorbed by M3.3) |
| strict guidance (strictly positive ladder densities) | strict sign patterns of c, c′, d (R1 Lemma 1.1; every chart cell; Lemma 1 of I1; vertex signs); Prop. necessary(b), hence UVN, the only entry of (LF); ball lemmas; B2.1 | iff no blind ladder step (non-degenerate) |
| Prop. necessary(b): vertex Bayes model = world-i-best, coherent | UVN (all routes) | yes: (γ₀) at e_i plus strict guidance |
| Prop. necessary(c): a coherent Bayes model at every boundary weight | edge limits, edge forcing | yes: (γ₀) at every t ∈ ∂Δ |
| Prop. necessary(d): T1 Bayes at interior p* | (TP) | yes, if non-degenerate (M3.4.4) |
| Prop. necessary(a): a.e.-unique Bayes model at **every** interior q, hence Hausdorff continuity of K and the every-q CF chart form | Thm TS, TSalways walls, cuts, apex, vertexfree; routes I1, I2, C2, short | **only if E(ψ) = ∅** |

So:
- if E(ψ) = ∅, gm excludes ψ (CHECKED, through the reading above; alternatively at the status of Thm ccibu through
  Cor. realisation);
- if E(ψ) ≠ ∅, D1 gives p* ∉ E and nothing in gm applies.

The remaining sections close this branch along route I1, for both E = ∅ and E ≠ ∅.

Routes I2, C2 and the short route use (BU) more heavily:
- precise collars;
- σ continuous on precise regions (Thm D);
- the measurable fibration of Thm A, which needs continuity of P.

They are not transferred here, and they are not needed.

---

## 5. Local one-sidedness at p*, and exact charts off E

Standing data for §§5–6: ψ is a strictly guiding integral (γ)-field on 𝓜 with (LF) at D_{T1}, and D_{T1} is its
a.e.-unique Bayes model at p* ∈ Ω, i.e. p* ∉ E. (D1 gives p* ∉ E whenever D_{T1} is ψ-Bayes at an interior p*.) N₀
and K″ are as in write-up §5:
- N₀ is the compact collar of the normalised facet segments Σ;
- K″ ⊆ int T1 is compact with P_{K″} > 0 on N₀.

A **tie-breaking family** is any assignment of q-Bayes models X_q, q ∈ Ω.

**Lemma M3.6 (local one-sidedness; PROVED).**
- (a) **Uniform closeness.** For every η > 0 there is r > 0 such that every q-Bayes model X with |q − p*| < r has
  μ(X △ D_{T1}) < η.
- (b) **Uniform credal closeness.** For every η > 0 there is r > 0 such that every coherent q-Bayes model D_K with
  |q − p*| < r has d_H(K, T1) < η. Hence there is r₁ > 0 with K ⊇ K″ for all such K and all q ∈ B₁ := B(p*, r₁). This
  covers the directional families, D♭, and every coherent tie-breaking.
- (c) **No rejection near facets.** For a.e. pair with orientation h ∈ cone(N₀), "accept −h" is weakly optimal at **no**
  q ∈ B₁. Hence, for every q ∈ B₁:
  - h is accepted iff c(h)·q > 0 or (c(h)·q = 0 and the tie rule accepts);
  - the only possible tie is accept-vs-silence, on the line {c(h)·q = 0}, and there c′(h)·q < 0.
- (d) **Where ties live.** There is r₂ ∈ (0, r₁] such that, for q ∈ B(p*, r₂), every non-null tie set at q consists,
  mod null, of pairs with an orientation in cone(N₀). By (c) these are accept-vs-silence ties. A near-facet atom tied
  at one point of B(p*, r₂) is tied at every point of its chord inside B(p*, r₂).
- (e) **Local quasi-linearity.** Let A be a set-type tie rule (X_q = B_q ∪ (Z_q ∩ A)) coherent at every q ∈ B₂ :=
  B(p*, r₂). Examples are A = ∅ (K^♭), A_δ = {δ·c > 0} (directional) and every admissible A of write-up §7.7. Let g₀,
  t, ρ > 0 have B(g₀ − t𝟙, ρ) ⊆ cone(N₀). Then on B₂, near level t, q ↦ P^A(q, g₀) is quasi-concave and quasi-convex:
  for q ∈ [q₁, q₂] ⊆ B₂ with |P^A(q_i, g₀) − t| small, min_i P^A(q_i, g₀) ≤ P^A(q, g₀) ≤ max_i P^A(q_i, g₀).

*Proof.*
- **(a)** For a.e. g, the p*-optimal advice a*(g) is unique and is T1's advice. Its margin is
  m(g) := min_{a≠a*} p*·(ℓ(g,a) − ℓ(g,a*)) > 0. Let env(g) := max_{k,a} ℓ_k(g, a) < ∞ a.e. Then
  |(q − p*)·(ℓ(g,a) − ℓ(g,a*))| ≤ 2|q − p*|₁ env(g). So a* is the unique q-optimum unless g ∈ G_r := {m ≤ 2r env}. The
  sets G_r decrease to a null set as r ↓ 0, and every q-Bayes model agrees with D_{T1} off G_r.
- **(b)** K ↦ 1_{D_K} is continuous and injective from the compact space of credal sets into L¹(μ) (R1 Prop. 3.1),
  so its inverse is uniformly continuous at T1. For the containment use the inner parallel body: if d_H(K, T1) < η,
  then K ⊇ {x ∈ T1 : dist(x, ∂T1) > η}, by separating a missed point (the argument of N21.2 step 4). Choose
  η < dist(K″, ∂T1). NUMERICS (`m3_checks.py` (3)): 0 failures on 3000 random near-T1 polygons.
- **(c)**
  1. Fix q ∈ B₁. If −h were q-optimal on a non-null set G′ ⊆ cone(N₀), some directional family D^δ_q would accept −h
     on a non-null part of G′. If −h is the unique optimum, every family accepts it. If it is tied, for a.e. h the
     set of δ favouring −h is an open half-plane of directions, so Fubini over δ applies. But D^δ_q = D_K with K ⊇ K″,
     and P_K(−h) ≤ P_{K″}(−h) ≤ −P_{K″}(h) < 0. So for each q the set is null.
  2. By Tonelli, for a.e. h the closed reject cell W(h) := {c′(h)·q ≥ 0, d(h)·q ≤ 0} meets B₁ in a Lebesgue-null set.
  3. If the open cell R(−h) is non-empty, then W(h) = cl R(−h). The two closed half-planes have boundaries that are
     not parallel with opposite sides, unless c′ − a d ∈ ℝ𝟙 with a > 0, which by the sign patterns forces W(h) = ∅.
     NUMERICS (`m3_checks.py` (2)): 19 845 exact boundary points, 0 failures. So a point of W(h) ∩ B₁ would give a
     non-empty open subset R(−h) ∩ B₁ of a null set. Hence W(h) ∩ B₁ = ∅.
  4. With − never weakly optimal: c·q > 0 implies d·q = c·q − c′·q > 0 or c′·q < 0, so + is strictly optimal. At
     c·q = 0, − is not weakly optimal, so c′·q < 0.
- **(d)** Let ω(r) := 2 sup{d_H(K, T1) : D_K coherent q-Bayes, |q − p*| < r} → 0. Suppose a non-null Z′ ⊆ Z_q consists
  of pairs with min(|P_{T1}(g)|, |P_{T1}(−g)|) > ω|g|. Three cases:
  - T1 strongly accepts g: every coherent K within ω/2 of T1 accepts it, since |P_K − P_{T1}| ≤ d_H|g|;
  - T1 strongly rejects g: the same with −g;
  - T1 is strongly silent on g: no such K accepts g or −g.

  In each case some directional family breaks the tie against this advice on a non-null part (Fubini over δ). That is
  a contradiction. By compactness of the unit sphere and since {P_{T1} = 0} = ∂D_{T1} is covered by the open cone over
  int N₀, for small r the remaining pairs have an orientation in cone(N₀). Frozen ties: by (c), on B₂ the tie condition
  of such a pair is c(h)·q = 0 alone.
- **(e)** By (c)–(d), for a.e. gamble g in B(g₀ − t𝟙, ρ), the set of q ∈ B₂ at which g ∈ X^A_q is an open half-plane
  {c(g)·q > 0}, plus its boundary line if g ∈ A. So X^A_{q₁} ∩ X^A_{q₂} ⊆ X^A_q ⊆ X^A_{q₁} ∪ X^A_{q₂} on that ball, for
  q ∈ [q₁, q₂]. This is the whole input of the proof of write-up Lemma quasilin(a): balls around g₀ − t𝟙. ∎

So on B₂ the two-sided field restricted to near-facet pairs is, at every weight and for every tie rule, a U-domain field:
- half-plane charts;
- accept-vs-silence ties frozen along chords;
- quasi-linear levels;
- the ball lemma for c-ties (B2 Lemma 7, one tie type), since by (d) all ties there have one type.

Lines through p* meet E ∩ B₂ in a countable set. An atom chord through p* inside B₂ would be frozen up to p*, against
p* ∉ E. Off the atom lines, E is countable (B2 §2).

**Lemma M3.7 (exact charts off E; vertex and edge limits; PROVED).** Call g *good* if
{q ∈ Ω ∖ E : P(q, ±g) > 0} agrees a.e. with R(±g) (Fubini: a.e. g is good; at q ∉ E the Bayes model is unique, with
credal set K_q).
- (a) For good g and every convex tie-breaking family F (K^♭, or K^δ): R(g) ⊆ {P^F(·, g) > 0} ⊆ cl R(g). Equality holds
  at every q ∉ E. For F = K^♭ equality holds at every q ∈ Ω.
- (b) K is Hausdorff-continuous at every q ∉ E, for values at nearby points taken from any tie-breaking family.
- (c) For good g and q ∉ E:
  - q ∈ cl R(±g) ⇒ P(q, ±g) ≥ 0;
  - K_q strictly straddles ℓ_g ⇒ q ∈ S(g);
  - q ∈ cl F(g) ⇒ K_q ⊆ g^⊥ (R4 Thm B at q ∉ E).
- (d) Under (Av), for every tie-breaking family and every edge prior q₀ with support S, every limit of K^F_q as
  q → q₀ through Ω lies in Δ_S. Also K^F_q → {e_b} as q → e_b.

*Proof.*
- **(a)** {P^F(·, g) > 0} is convex: by D1.1(b) for K^δ; for K^♭, because strict acceptance cells are convex. It agrees
  a.e. with the open convex R(g). A convex set C with μ(C △ R) = 0 has int C = int cl C = R, so R ⊆ C ⊆ cl R.
  - At q ∉ E with q ∈ cl R ∖ R and P(q, g) > 0: continuity (b) gives P > 0 on a neighbourhood, so q ∈ int cl R = R,
    which is a contradiction.
  - For K^♭, {P^♭ > 0} is open, because K^♭ is upper semicontinuous: limits of strict acceptances. Two open convex sets
    that agree a.e. are equal.
- **(b)** Every g untied at q keeps its strict optimum near q, so the advice converges a.e., hence in measure. Then
  apply R1 Prop. 3.1.
- **(c)** The first item is (b), using points of R(±g) ∖ E nearby. For the second: strict straddling means P(q,g) < 0
  and P(q,−g) < 0, so q ∉ cl R(g) ∪ cl R(−g) ⊇ cl F(g), and the remaining cell is S(g). The third: both one-sided
  values are ≥ 0.
- **(d)** Let g_i, g_j > 0, i, j ∈ S. Then c(g)·q₀ > 0 and d(g)·q₀ > 0, so for q near q₀ (depending on g) acceptance is
  the strict q-optimum. It is available by (Av). By dominated convergence, every limit model accepts a.e. g with
  g_i, g_j > 0. A credal set K with D_K ⊇ {g_i > 0, g_j > 0} has K ⊆ [e_i, e_j]: if m ∈ K has m_l > 0, test
  g = (η, η, −1) in the coordinates (i, j, l). At e_b, + is eventually optimal where g_b > 0 and − where g_b < 0, both
  available. So the limit is the precise model D_{e_b}. ∎

---

## 6. Route I1 across chords, and the main theorem

Route I1 (I1 §1) cites exactly four inputs:
- (C1) the every-q CF chart form with both acceptances;
- (C2) (TS), (PC), (NS) at p* = u, with the corner equation;
- (C3) unique clusters c(g)/|c(g)| → c_k(h)/|c_k(h)|;
- (C4) edge confinement.

"Nothing else is used" (I1 §1; confirmed, I1_referee). The normalisations p* = u and x = x₊ are field operations that
preserve (γ) and move E projectively.

**Proposition M3.8 (route I1 for (γ)-fields; PROVED, transfer written out).** Assume the standing data of §5, (Av),
(C2) and (C3), with E null and p* ∉ E. Then there is a contradiction.

*Proof.* Replace (C1) by M3.7(a)–(c) and (C4) by M3.7(d). In every step, use only priors q ∉ E (a co-null set) and
limits through Ω ∖ E. The steps:
- **Lemmas 1, 2 (edge maps).** These are facet algebra from (C2): crossing rows, monotone chord normals, (NS).
  Unchanged.
- **Prop. E (edge limits).** Limits through Ω ∖ E.
  - Step 3 needs, for q ∉ E with c(g)·q > 0 and g ranging over an open set near ĥ, that K_q does not strictly straddle
    ℓ_g. At q ∉ E the Bayes model is unique and silence is not optimal for a.e. such g. So a.e. such g has g or −g in
    D_{K_q}, and strict straddling, an open condition in g, is excluded. No R4 Thm B is needed.
  - Step 4 needs: c(g)·q < 0 ⇒ g ∉ D_{K_q} a.e. near ĥ ⇒ P(q, ·) ≤ 0 there.
  - Step 1 is M3.7(d).
- **Thm R (pinned c-lines).** Step 1: K_q strictly on the positive side for q ∉ E near q₀ gives P(q, g) > 0, hence
  q ∈ R(g) (M3.7(a), equality off E). Step 2: strict straddling at q ∉ E gives q ∈ S(g) (M3.7(c)). S(g) is closed.
- **No atoms among pinned gambles.** Let g be good, with ℓ_g crossing E₁, E₂ at parameters t₁, t₂ whose μ-images
  y₁ ∈ N_{E₁}, y₂ ∈ N_{E₂}.
  - Thm R puts its c-line through y₁ and y₂. These are distinct points on different open edges, so the c-line is
    determined by ℓ_g: the μ_o are homeomorphisms.
  - ℓ_g determines g up to a positive factor.
  - So the set of g sharing one c-line inside this regime is null. Hence a.e. good g near the gamble g_L of Lemma S
    lies in no atom. Moreover its c-line is none of the countably many atom lines of other gambles: each such line is
    the c-line of a null set of pinned g. By B2 §2 (E ⊆ atom lines ∪ a countable set), its c-chord meets E in a
    countable set.
- **Lemma S (forced supporting lines).** For good non-atom g_n → g_L, choose q_n ∉ E on the c-chord of g_n with
  q_n → q, where q ∉ E is the window point.
  - At q_n, P(q_n, g_n) ≥ 0 by M3.7(c) (q_n ∈ cl R(g_n)) and ≤ 0 (q_n ∈ S(g_n), not in R(g_n)). So P(q_n, g_n) = 0.
  - By M3.7(b) at q ∉ E, P(q, g_L) = lim P(q_n, g_n) = 0.
- **Lemma window, and the first proof.** These are local at u = p*. The certificate point is chosen off E on the side
  of C₁ where ϱ > 0, which is open. The contradiction m·g₂ ≥ ϱ(q) > 0 on K_q against min_{K_q} m·g₂ = 0 is a
  statement at the single prior q ∉ E. ∎

**Proposition M3.9 ((C2), (C3) for non-degenerate (γ₀)-fields; CHECKED).** Under the standing data of §5 and (Av):
(TS) holds, and the conclusions of Thm TS hold on a ball around p* for K^♭ (equivalently for K_q, q ∉ E). These are
(PC), (NS), crossing rows, x ∈ {x₊, x₋} and the cluster clause. Hence (C2) and (C3) hold.

*Reading (item by item; the risky items first).*
1. **Thm TS = N21.4.** N21.4 is a list of edits to the N15 chain, and everything not edited is local on B₁. Its
   non-local inputs:
   - UVN: D1.1(c) for directional families, under (LF);
   - quasi-concavity on Ω: D1.1(b), and M3.7(a) for K^♭;
   - N21.2 (half-plane charts on B₁): replaced by M3.6(c), which is stronger, being pointwise in q for every
     tie-breaking.
   - *If p* ∉ cl E*, every local statement holds verbatim on a ball missing E.
   - *If chords accumulate at p**, M3.6 makes B₂ a U-domain for near-facet pairs. The write-up's Prop. chainchords (two
     readings) audits every step of the N15 chain with K^♭ across chords: straight levels from Lemma quasilin (here
     M3.6(e)), PL2 for K^♭ via the ball lemma at Q (here B2 Lemma 7, one tie type, by M3.6(d)), pivot step 4 on λ ∖ E
     (co-countable, see after M3.6), anchors chosen off E, and the cluster clause from exact charts (M3.7(a)). The
     global steps of that audit (Lemma nopin, U-box) are exactly those N21.4 does not use: N21.4 replaces nopin by
     the hypothesis (TS). Its one new argument (item 5, c-clusters at crossings) uses R15 Lemma C on B₁ and pointwise
     signs of c(g_m). Both are available.
2. **TSalways = N28 Thm 3.5.** Assume (TS) fails. The steps:
   - Cor. R23.2 and Lemma R23.1 are local. R23.1 needs PL2 for K^♭ on a ball, chords allowed (item 1).
   - N21.9's pinned set O and its wall toward V_l: the pinned set is local. The wall is Lemma M along segments from O
     to V_l, which may cross chords. This is exactly D1.6, which proves "for a.e. (o, y) the segment contains q ∉ E with
     K_q ⊆ B(v, η)" across chords (cases Q ∉ E, (A), (B); D1_referee: CORRECT after the open-chart repair of Step 1).
   - Prop. 3.1: d := dist(p*, approximate wall) > 0 by M3.6(b). Lemma 2.4 for the approximate wall holds with the convex
     set {P^δ(·, h^i(τ)) > 0}, which misses p* since K^δ_{p*} = T1.
   - Lemma 3.2: Thm PL with approximate walls. The nearest-point argument on [o, A] goes through as follows.
     - The first point Q of cl β_{v′} is independent of the approximate wall point used.
     - If Q ∉ E, continuity at Q separates K ≈ {v} from K ≈ {v′}.
     - If Q ∈ E, D1.6 case (B) gives v′ in both one-sided limits, which is incompatible with the other side being within
       η of v.
   - Lemma 3.3 is combinatorics.
   - Lemma 3.4 (surround) needs only d > 0 (D1_referee §6).
   - Step 5 uses the convex sets of D1.1(b).

Referee priorities for M3.9:
- (i) the chords-accumulating case of item 1, i.e. that every use of K in N15/N21.4 on B₁ is through near-facet levels,
  so that M3.6(e) suffices;
- (ii) Thm PL with approximate walls;
- (iii) R23.1 for K^♭ with chords in the ball.

**Proof of Theorem M3.10.** Let ν be an endorser tuple and ψ = ψ^ν. Suppose ψ is strictly guiding. Then:
- by M3.4, (γ) holds, D_{T1} is ψ-Bayes at some p*, and p* ∈ Ω;
- by D1, p* ∉ E(ψ), so D_{T1} is the unique Bayes model there;
- Props. M3.9 and M3.8 give a contradiction. (The case E = ∅ is included; it is also gm's case, §4.)

So ρ_ν vanishes on a non-null subset of some Γ_k. Taking ν = ν* (componentwise maximal support, M3.1(c)) gives a non-null
canonical blind set. The last sentence of the theorem is L3.1(a): on such domains acceptance is in the advice range for
a.e. g that is not ≤ 0, and each mixed g and −g has a positive coordinate. ∎

**Corollary M3.10′.** On every decomposable domain with (LF) and (Av) (in particular every domain two-sided near
∂D_{T1}), no ranking with strict (G), (IB), (LA), (S), (C) and T1 ∈ C_L has every world adding up. This is case (M0),
closed as on M_U by Thm M0closed(b), and it answers D1 §4's conjecture on these domains. Status: that of M3.10. Every
cover there needs a world with a non-null ladder-blind set, or a strongly (M1) world.

---

## 7. What remains, and the configuration handed over

**Q_M3(a): degenerate fixed points on (Av)-domains.** The degeneracy now has two kinds per world:
- Λ^s_k, *silence-blind*: s_k = 0, so silence costs world k nothing;
- Λ^w_k, *wrong-blind*: w_k = 0, so a wrong acceptance costs world k no more than silence.

**Lemma M3.11 (where vertex fans can come from; PROVED).** Assume (Av). At a vertex e_k, the optimal advices of the
fixed-point field on a mixed pair are:
- {correct acceptance}, off Λ^s_k;
- {correct acceptance, silence}, on Λ^s_k.

Wrong-blindness never creates a tie at a vertex. Consequently:
- the directional vertex limits at e_k (the "fan" of L4.6(a)) differ from the precise model D_{e_k} only on Λ^s_k;
- UVN at e_k can fail only for gambles of Λ^s_k (the proof of D1.1(c) uses strict world-k optimality only at the
  gambles concerned);
- each coherent fan model D_K has e_k ∈ K, and Λ^s_k ⊇ {g : g_k > 0, P_K(g) < 0} (mod null), the analogue of K3.7(β′).

*Proof.* With good available, the world-k losses are 0, s_k, s_k + w_k, so the minimisers are as stated. A vertex limit
along any direction therefore has the following form:
- it accepts the correct orientation off Λ^s_k;
- on Λ^s_k it accepts the correct orientation or is silent;
- it never accepts a world-k-wrong orientation.

So D_K ⊆ D_{{e_k}}, i.e. e_k ∈ K. Also every g with g_k > 0 that D_K does not accept lies in a Λ^s_k-pair. ∎

So on (Av)-domains the M_U template of L4 (configuration (I): chart lines of blind gambles through a vertex) is
reproduced by **silence-blindness alone**: on Λ^s_k, c_k = 0 (g_k > 0) or c′_k = 0 (g_k < 0). Wrong-blindness is a
different, non-vertex degeneracy:
- c_k = 0 for g_k < 0 (or c′_k = 0 for g_k > 0) puts the accept-wrong-vs-silence lines through e_k;
- at an interior p* it is constrained by Prop. M3.2(b): w cannot vanish at every world on T1's silent set;
- at a boundary p*, M3.4.4 forces both kinds of blindness on joint T1-error sets.

The full wrong-first world (Λ^s_k = all of M) is L3.6(b), which Thm L3.4 excludes except for edge selections that are
precise on an uncountable set of edge priors.

**Q_M3(b): the single precise obstruction to "all decomposable domains".** By L3.1(a), (Av) holds whenever the domain
is two-sided near ∂D_{T1}. On the U-domains, L4.1 with M0closed(a) covers the case. What is not covered is a domain with
(LF) on which (Av) fails on a non-null set of mixed pairs, other than a U-domain: partially one-sided near ∂D_{T1}. Then
the ranking's vertex models D_{V_b} are not all precise (R10a Cor. V2). For additive covers, Cor. TSalways(b) excludes
this through the cut theorem N21.6/N21.7, which shows that K_{q_m} → {e_b} along interior priors and forces
availability. The missing step is precisely:

> **CONJECTURE M3.C.** Thm N21.6 and Cor. N21.7(a), (b) hold for non-degenerate (γ₀)-fields (strictly guiding, integral,
> D_{T1} the unique Bayes model at p* ∈ Ω), with E ≠ ∅ allowed.

Its inputs are the chart-form edge box at an edge prior and N21.2 (here M3.6). It also needs R4 Thm B at the cut apex,
and Hausdorff limits along [a*, z*]; these need the off-E/one-sided-limit replacements of M3.7 and D1.1(d). Given
M3.C, Thm M3.10 holds on every decomposable domain with (LF): M3.C yields (Av), and the U-domain case is the special
case already closed.

**Outside the theorem, as in L4:** strongly (M1) worlds, which fail (NC).

**What a positive answer must now be.** On every decomposable domain with (LF) and (Av), and on M_U, a cover of T1 must
contain one of two kinds of world:
- a strongly (M1) world;
- a world whose countably additive endorsers all vanish on a non-null ladder set.

Moreover the ladder blindness must be silence-blindness wherever it is to produce the vertex mechanism of L4's
configuration (I). The two-sided mechanism that one might have hoped would escape (exceptional chords away from p*,
where wedge charts break quasi-linearity) does **not** escape. Near p* the field is one-sided at every weight (M3.6).
Away from p*, route I1 needs only priors off E (M3.8).

---

## 8. Dependencies and files

**Used.**
- K3.1 (refereed CORRECT, K3_referee §1), Yosida–Hewitt, N19 Lemma R1 in K3.1(c).
- Theorem kkm; H1.0(a), H1.1 (H12_referee); R1 Prop. 3.1; R1 Lemmas 1.1, 1.2; Remark advicerange.
- B2.1 (B2_referee: CORRECT) and B2 Lemma 7 (one tie type), B2 §2 (E ⊆ lines ∪ countable).
- Theorem D1 and Lemma D1.1, D1.6 (D1_referee: CORRECT after repairs).
- Route I1 (I1, I1_referee: CONFIRMED), with its cited inputs (C1)–(C4) replaced as in M3.8.
- N21.2, N21.4, N21.9 (refereed in N23); N28 Lemmas 2.1–3.4, Thm 3.5 (two readings); R10b Lemma D, Lemma M,
  Thm PL (R12); R23.1, R23.2 (N23, second reading).
- Write-up Lemma quasilin (its proof), Prop. chainchords (two readings), Cor. realisation, Thm ccibu (only for the
  alternative status of the E = ∅ case).
- L3 Prop. L3.1(a) (PROVED in L3, not refereed), only to derive (Av) from two-sidedness.

**Not used.** N13 Prop. B, N19 Prop. R3(a), Claim B2.0 (now proved, M3.5), routes I2, C2 and the short route, Thm D,
Thm A, (E_ψ), the L4 one-blind-world analysis (§§4–5 of L4), and any specific penalty normalisation.

**New and unrefereed, in order of risk.**
1. Prop. M3.9 (CHECKED), priorities (i)–(iii) above.
2. Lemma M3.6(c)–(d): the passage from "for each q, null" to "for a.e. h, for every q ∈ B₁" (Tonelli, plus closed
   reject cell = closure of open cell); and the three-case tie exclusion in (d).
3. Prop. M3.8: the no-atom argument for pinned gambles, and the use of non-atom g_n in Lemma S.
4. Theorem M3.4.3: H1.1 with several alternatives per pair (Lyapunov for a finite partition).
5. Prop. M3.2(b): the reduction of equality to apex ties.

**Files** (`m3py/`, run with `python3 -I m3_checks.py` from inside it; output in `m3_checks.out`):
- (1) ladder algebra: sign patterns; silence-optimality ⇒ q·s ≤ q·w; single graded charge ⇒ no silence off apex ties;
- (2) closed reject cell = closure of the open cell, at 19 845 exact boundary points;
- (3) inner-parallel-body containment for 3000 random convex polygons near T1.
