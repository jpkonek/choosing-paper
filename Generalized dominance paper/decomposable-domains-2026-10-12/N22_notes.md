# N22. Part (A) for coherent almost-preference rankings: what is left after the CA route

13 Oct 2026. Task: BRIEF6 part (A), gaps (1) countable detection, (2) attainment for charges, (3) atomic singular parts.
Labels: **PROVED** (full proof here), **CHECKED** (verified; proof imported with source or sketched), **CONJECTURE**.
No scripts were needed (no claim below rests on numerics).

Imported, refereed: N11 Fact 1.2, Lemma 3.1, Cor 3.2 (N13: CORRECT); N13 Prop B; N14 Lemma Y and Theorem C2;
R11 Lemma IC, Lemma K, Fact 0 (LDG thm:kkm); R2 Lemma U; CBOI lem:compact (= R1 Prop 3.1); part (B):
N15 Thm 7.1 and Cor 7.2 (non-adjacent decomposable domains), Cor 7.3 (charges, given existence), refereed CORRECT in N18.

Standing hypotheses **(H)**: n worlds (n = 3 for T1); decomposable domain M (a class of evaluable models closed under measurable splicing, closed in
measure); the ranking L satisfies strict (G), (IB), (LA), (S), (C); N_i := the set of problems whose advice range has ≥ 2
elements (the same set for every i; "non-singleton problems": not every evaluable model gives the same advice). **Coverage of T1**: T1 = D_K ∈ C_L with (LF) at T1,
K = (1−ε)u + εΔ ⊆ int Δ. Notation as in N11: Λ_iX = λ_i(·, a_X(·)) ∈ L^∞(μ); a state is a positive normalised linear
functional on L^∞(μ); P = P^c + P^s (Yosida–Hewitt), P^c = ρ_P μ.

---

## 0. Outcome

**Verdict.** Gaps (2) and (3) are closed: they are artefacts of using the full charge field, and they disappear on the
integral (countably additive) route, whose one remaining hypothesis (FS^c) turns out to be automatic. Gap (1) does not
disappear: it becomes the single explicit residual (U) below, a property of one *integral* field. (U) is now PROVED for
complete worlds with arbitrary charges, atoms included. This is new; N11.7 needed (CD) + (SN) and got attainment only at
p_T. In general (U) is CONJECTURE.

**N22.1 (PROVED) Full support is automatic.** Under (CP-a) and strict (G) at world i, some member P_i ∈ M_i has a
countably additive part with density ρ_i > 0 a.e. on N_i. The proof is a Kneser minimax argument plus the small-carrier
lemma (§1). So N13's (FS^c) is not a hypothesis. Every "relative-interior-type" mixture (1−t)P_i + tQ, with Q ∈ M_i and
t < 1, inherits the property.

**N22.2 (PROVED) The integral reduction under (CP-a) alone.** Assume (H), (CP-a) and coverage of T1. For **every**
choice P = (P_1, …, P_n) with P_i ∈ 𝒫_i^+ := {P ∈ M_i : ρ_P > 0 a.e. on N_i} (non-empty by N22.1), the integral field
 ψ^P_i(X) := ∫ λ_i(g, a_X(g)) ρ_{P_i}(g) dμ(g)
is strictly guiding, has an integrable envelope, lives on the same domain M (so (LF) at T1 is kept), and satisfies:
- (α) T1 is ψ^P-Bayes at some p_T ∈ int Δ;
- (β) for every p ∈ Δ some ψ^P-p-Bayes model is coherent;
- (γ) the exceptional set E(P) := {p ∈ int Δ : the pointwise tie set Z_p(P) is non-null} is Lebesgue-null, and at every
  p ∈ int Δ ∖ E(P) the ψ^P-p-Bayes model is a.e. unique and coherent;
- (δ) at each vertex e_i the Bayes model is W_i(M) = C_{e_i}, which is coherent.

No detection, no attainment and no non-atomicity hypothesis is used. Purely finitely additive parts, atomic or not,
enter only through finitely many small carriers (§2).

**N22.3 (PROVED, using part (B)) The sharp residual.** Suppose L covers T1 on a non-adjacent decomposable domain (for example
the U-domain M_U, whose evaluable models are the measurable subsets of U = D_{K′}). Then E(P) ≠ ∅ for every P ∈ ∏_i 𝒫_i^+. Equivalently, the impossibility theorem for
(CP-a) holds as soon as

 **(U)** some choice P ∈ ∏_i 𝒫_i^+ has no non-null pointwise Bayes tie at any interior weight.

**N22.4 (PROVED) Cases where (U) holds.**
- (a) **Complete worlds, arbitrary charges.** Each M_i = {P_i} is a singleton, i.e. ⪯_i is a complete coherent
  almost-preference (Walley's R9) represented by a single state. Atoms and purely finitely additive parts are allowed.
  Domain proviso (UN): the unanimous non-singleton problems are non-null (true on M_U and on the all-model domain).
  Then the charge field P∘Λ attains its infimum at **every** p ∈ Δ, its interior minimisers are unique and coherent,
  and E(P) = ∅. Hence **T1 cannot be covered by complete coherent almost-preference rankings** on a non-adjacent domain.
- (b) (D^CA) (N11.2), in particular Case CA.
- (c) Locally: if at p_0 the charge field P∘Λ attains its infimum and detection (R) holds at p_0 on the Lemma-K pairs,
  then p_0 ∉ E(P).

**N22.5 (PROVED) What a covering system must look like.** By N22.3–N22.4, any (CP-a) cover of T1 on a non-adjacent
domain has all of the following:
- some world is incomplete (M_i not a singleton);
- for every P ∈ ∏𝒫_i^+ there is p_0 ∈ int Δ with a non-null ψ^P-tie set;
- at each such p_0, either the charge field P∘Λ fails to attain, or some Lemma-K pair at p_0 is strictly L-comparable
  but tied by P (a detection failure at p_0);
- if moreover some P has all P_i countably additive, then at every p_0 ∈ E(P) the whole face of p_0-Bayes profiles
  (a set of dimension ≥ 1) is realised by **selected** models (§4).

**CONJECTURE N22.U.** (U) holds for every (CP-a) system satisfying (H). By N22.3 this is equivalent, on non-adjacent
domains, to "no (CP-a) system covers T1". It is the precise successor of N11.A (detection), N11.B (atoms) and N14's
existence proviso: all three are now subsumed by (U).

**N22.6 Final formulation of (CP-a) for the paper (§5).**

---
## 1. Full support of countably additive parts is automatic (N22.1)

**Lemma 1.0 (PROVED). Strict (G) in (CP-a) form.** Assume (CP-a), with λ_i bounded and strictly increasing in world-i
rank a.e. Then strict (G) at i holds iff P̄_i(1_A) := max_{P∈M_i} P(1_A) > 0 for every non-null A ⊆ N_i.

*Proof.* (⇐) Let f = Λ_iY − Λ_iX ≥ 0 a.e. with f > 0 on a non-null A. Then A_δ := {f ≥ δ} ∩ A is non-null for some
δ > 0, and P(f) ≥ δP(A_δ). Hence P̄_i(f) ≥ δP̄_i(A_δ) > 0, which is strictness by N11 Prop 1.1(ii).
(⇒) Given non-null A ⊆ N_i, let X be W_i(M), and let Y be X with a strictly worse advice in the advice range substituted on A
(a measurable choice). Then 0 ≤ f ≤ 2‖λ_i‖_∞ 1_A and f > 0 on A. Strict (G) gives P(f) > 0 for some P, so P(A) > 0. ∎

**Lemma 1.1 (PROVED). Pure families cannot detect everything.** Let M be a weak-* compact convex set of states on
L^∞(μ), μ finite and atomless, and let A be non-null with P^c(A) = 0 for every P ∈ M. Then there is a non-null N ⊆ A
with P(N) = 0 for every P ∈ M.

*Proof.*
1. *One step.* Let A′ ⊆ A be non-null and let η ∈ (0,1), ε > 0. We claim there is B ⊆ A′ with
   μ(B) ≥ (1−η)μ(A′) and max_{P∈M} P(B) ≤ ε.
   - Put Φ := {f ∈ L^∞ : 0 ≤ f ≤ 1_{A′}, ∫f dμ = (1−η²)μ(A′)}. This is convex and non-empty.
   - For fixed P ∈ M, inf_{f∈Φ} P(f) = 0. Indeed, P(1_{A′}·) = P^s(1_{A′}·), since P^c vanishes on subsets of A. By
     Lemma Y (N14 §5.1) there is F with μ(F) < η²μ(A′) and P^s(H∖F) = 0. Take B_0 ⊆ A′∖F with
     μ(B_0) = (1−η²)μ(A′) (μ is atomless). Then f = 1_{B_0} ∈ Φ and P(f) = 0.
   - Kneser's minimax theorem (Kneser 1952; Fan 1953) applies. M is compact and convex in the weak-* topology, Φ is
     convex, and (P, f) ↦ P(f) is bilinear and weak-* continuous in P. Hence
     inf_{f∈Φ} max_{P∈M} P(f) = max_{P∈M} inf_{f∈Φ} P(f) = 0.
   - Choose f ∈ Φ with max_P P(f) ≤ (1−η)ε, and put B := {f ≥ 1−η} ⊆ A′. From
     (1−η²)μ(A′) = ∫f ≤ μ(B) + (1−η)(μ(A′) − μ(B)) we get μ(B) ≥ (1−η)μ(A′). From 1_B ≤ f/(1−η) we get
     P(B) ≤ ε for all P ∈ M.
2. *Iteration.* Put B_0 = A. Apply step 1 to A′ = B_{k−1} with η_k = 2^{−k−1} and ε_k = 2^{−k}. This gives a
   decreasing sequence B_k with μ(B_k) ≥ ∏_{j≤k}(1−η_j)μ(A) ≥ ½μ(A) and max_P P(B_k) ≤ 2^{−k}.
3. Put N := ∩_k B_k. Then μ(N) ≥ ½μ(A) > 0, because μ is countably additive. Monotonicity gives
   P(N) ≤ P(B_k) ≤ 2^{−k} for all k, so P(N) = 0 for every P ∈ M. ∎

*Remark.* Step 3 is the only place where countable additivity is used, and it is applied to μ, not to the members.
The members are used only through finitely many small carriers, one at a time; that is why no common carrier for an
uncountable family is needed (cf. N11 Prop 5.2, where none exists).

**Theorem 1.2 (PROVED; N22.1).** Assume (CP-a) and strict (G) at world i. Then 𝒫_i^+ := {P ∈ M_i : ρ_P > 0 a.e. on
N_i} is non-empty. Moreover, if P ∈ 𝒫_i^+, Q ∈ M_i and t ∈ [0,1), then (1−t)P + tQ ∈ 𝒫_i^+.

*Proof.*
- Let s* be the essential supremum (in the measure algebra of μ) of the sets {ρ_P > 0}, P ∈ M_i. By the countable
  chain condition there are P_k ∈ M_i with s* = ∪_k {ρ_{P_k} > 0} a.e.
- If μ(N_i ∖ s*) > 0, then P^c(N_i∖s*) = 0 for all P ∈ M_i. Lemma 1.1 gives a non-null N ⊆ N_i with P̄_i(N) = 0,
  contradicting Lemma 1.0. So s* ⊇ N_i a.e.
- Put P* := Σ_k 2^{−k}P_k. The series converges in norm, and M_i is convex and norm-closed (weak-* closed sets are
  norm-closed). So P* ∈ M_i.
- The map P ↦ P^c is the band projection of ba onto its countably additive band. It is linear and norm-continuous.
  Hence ρ_{P*} = Σ_k 2^{−k}ρ_{P_k} > 0 a.e. on s* ⊇ N_i.
- The mixture statement holds because (1−t)ρ_P + tρ_Q ≥ (1−t)ρ_P. ∎

*Relation to earlier notes.* N19 Lemma R1 is the single-charge case (a strictly positive charge has an a.e.-positive CA
part). Theorem 1.2 is the family version. It is false without weak-* closedness. N11 Prop 5.2's family needs μ̄ for
strict (G), which is consistent with Theorem 1.2.

---

## 2. The integral reduction under (CP-a) alone (N22.2)

**Theorem 2.1 (PROVED).** Assume (H), (CP-a) and coverage of T1, and let P ∈ ∏_i 𝒫_i^+ (non-empty by Theorem 1.2).
Then ψ := ψ^P satisfies (α)–(δ) of N22.2.

*Proof.* This is N13 Prop B, whose only extra hypothesis was (FS^c), now supplied by Theorem 1.2. I re-check the points
where charges, atoms or attainment could enter.
- *Strict guidance and envelope.* ρ_{P_i} > 0 a.e. on N_i, and λ_i is strictly rank-increasing a.e. The envelope is
  ‖λ_i‖_∞ ρ_{P_i} ∈ L¹.
- *(α).* N11 Cor 3.2(d). Lemma IC makes T1 competitive on Ω. Lemma 3.1 (the splice) uses a common small carrier for the
  n pure parts P_i^s. Such a carrier exists for any finitely many charges vanishing on null sets, atomic or not (Fact 1.2
  or Lemma Y applied to Σ_i P_i^s). Lyapunov applies to the integral parts, separation gives p_T, and strict guidance
  pushes p_T into int Δ.
- *(β).* N13 Prop B (β), which is CBOI's proof of thm:fa transplanted. It uses:
  - Fact 0(a);
  - (W) for the full members P_i;
  - one finite family of carriers;
  - sequential compactness in measure of coherent models (CBOI lem:compact);
  - closedness of M in measure;
  - continuity in measure of ψ (integrable envelope).

  No infimum of a charge is ever required to be attained. The coherent limit C_∞ attains the *integral* minimum, which
  always exists by pointwise minimisation.
- *(γ).* E(P) is λ-null by Fubini (N13 Prop B (γ)). For p ∉ E(P) the pointwise minimiser is a.e. unique, and every
  ψ-p-Bayes model is a pointwise minimiser (integral field). So it equals the coherent model of (β).
- *(δ).* At e_i the objective is ψ_i alone. It is strictly guiding, so W_i(M) is its a.e.-unique minimiser. The vertex
  lemma (DCE prop:ideal) gives W_i(M) = C_{e_i}, which is coherent. ∎

**What happened to the three gaps.**
- *Gap (2), attainment.* It is irrelevant on this route, because the field is integral and minimisers exist pointwise.
  Charge-valued fields enter only through (W) in the Fact-0 step of (β), and there only inequalities between values
  are used.
- *Gap (3), atoms.* They are irrelevant, for the same reason. Every use of a singular part is "change advice off a
  small carrier of finitely many charges", and atoms (ultrafilter charges) have small carriers like every purely
  finitely additive charge (Lemma Y). The separation step is done in the integral coordinates (Lyapunov), never in the
  charge coordinates. So N11 Remark 5.4's non-convexity never arises.
- *Gap (1), detection.* What survives of it is only the uniqueness at the weights in E(P). At p ∉ E(P), uniqueness is
  pointwise and needs no detection. The detection problem is thus localised to the λ-null set E(P), and it can bite only
  there. This is made precise in N22.4(c) and §4.

**Remark 2.2 (selectedness).** At p ∉ E(P) the Bayes model is shown coherent, not selected; N19 made the same point.
Part (B) needs only coherence, so this does not matter for the impossibility. If the charge field P∘Λ attains at such a
p, the minimiser is selected (Prop 3.3(i)).

### 2.3 The sharp residual (N22.3)

**Corollary 2.3 (PROVED, modulo the imported part (B)).** Let M be a non-adjacent decomposable domain (pairs meeting U′
non-adjacent, N14 §3(iv); e.g. M_U). If L satisfies (H) + (CP-a) and covers T1, then E(P) ≠ ∅ for every
P ∈ ∏_i 𝒫_i^+.

*Proof.* If E(P) = ∅, then ψ^P is a strictly guiding integral additive field on M with (LF) at T1. At every interior
weight its Bayes model is a.e. unique (γ) and coherent (β). Its vertex Bayes models are coherent (δ), and T1 is Bayes
at p_T ∈ int Δ (α), hence the unique such model. This is excluded by N15 Thm 7.1 on M_U, and by Cor 7.2 on non-adjacent
domains (refereed CORRECT in N18). ∎

So, **under (CP-a) alone, coverage of T1 yields an integral additive field with every property the no-go needs, except
uniqueness on a Lebesgue-null set E(P) of interior weights.** The no-go applies as soon as E(P) = ∅ for one choice.

---
## 3. When (U) holds

Throughout this section fix P ∈ ∏_i 𝒫_i^+ and write φ_i := P_i∘Λ_i for the **charge** field (full members), and ψ := ψ^P
for its integral part. So φ_i = ψ_i + φ^s_i with φ^s_i(X) = P_i^s(Λ_iX). Let F denote a common small carrier of
P_1^s, …, P_n^s, i.e. μ(F) small and P_i^s(H∖F) = 0 for all i (Lemma Y applied to Σ_i P_i^s).

**Lemma 3.0 (PROVED; the main step of N14 Thm C2, ties allowed).** Let p ∈ int Δ. If X attains inf_M p·φ, then for a.e. g
the advice a_X(g) minimises Σ_i p_iρ_i(g)λ_i(g, ·) over the advice range A(g). That is, X is a pointwise ψ-p-minimiser.

*Proof.* Suppose not. Then Y := {g : a_X(g) is not a minimiser} is non-null. Choose F with μ(F) < μ(Y)/2, and let X′ be
X with a pointwise minimiser substituted on Y∖F. The pure terms are unchanged, because X′ = X on F. The integral term
drops by a positive amount, because ρ_i > 0 a.e. on N_i ⊇ Y. This contradicts minimality. ∎

### 3.1 Local criteria (N22.4(c))

**Prop 3.3 (PROVED).** Let p ∈ int Δ and suppose inf_M p·φ is attained.
- (i) If p ∉ E(P), every attaining model is a.e. equal to a selected model. In particular it is coherent and in C_L.
- (ii) Suppose that, at p, detection holds on Lemma-K pairs: whenever C is selected, B attains, C ⪯_i B at every i and
  P_i(Λ_iB − Λ_iC) = 0 for every i, then C ~_i B at every i. Then p ∉ E(P).

*Proof.*
- (i) Let B attain. Fact 0(a) gives a selected C with C ⪯_i B for all i. By (W), φ(C) ≤ φ(B) coordinatewise, so C
  attains too. By Lemma 3.0 both B and C are pointwise ψ-p-minimisers. Off the null set Z_p(P) the minimiser is
  unique, so B = C a.e.
- (ii) *Every attaining B is coherent.* As in (i), C attains, and since p is interior, φ_i(C) = φ_i(B) for every i.
  Detection gives C ~_i B for all i, and (C) gives that B is coherent.
- *Suppose Z := Z_p(P) is non-null.* Take an attaining B and a carrier F with μ(F) < μ(Z)/2. Let B′ be B with the
  other tied advice substituted on R := (Z∖F) ∩ {|g| < 1}.
  - B′ attains: its integral value is unchanged because the two kinds of advice are tied on Z, and its pure value is unchanged
    because B′ = B on F.
  - So B′ is coherent, and so is B.
  - Then B △ B′ = R would be a cone modulo null sets. But R is non-null and contained in the unit ball, so it is not
    (R2 Lemma U / R1 Lemma 1.4(ii)). Contradiction.
  (Finitely many pairs of kinds of advice: substitute measurably on the piece where a given pair ties.) ∎

(ii) is N11 Thm 5.5's uniqueness argument with global (CD) replaced by detection at the single weight p, and with no
(SN). Detection is thus needed only at weights in E(P), and only on pairs both of which attain there.

### 3.2 Complete worlds: (U) holds, atoms included (N22.4(a))

**(UN)** For each i there is a non-null U_+ ⊆ N_i on which every coherent model in M gives the world-i-best advice in the
advice range.
- On M_U this holds with U_+ = U ∩ {g ≫ 0}: coherent models accept such g, and acceptance is correct at every world.
- On the all-model domain it holds with the unanimous problems.

**Theorem 3.1 (PROVED).** Assume (H) and (UN), and suppose every world is a complete coherent almost-preference. That is,
(CP-a) holds with M_i = {P_i} (Walley R9), so ⪯_i is represented by φ_i = P_i∘Λ_i. The P_i are arbitrary states,
with any purely finitely additive and atomic parts. Then:
- (a) for every p ∈ Δ, inf_M p·φ is attained, by a selected model;
- (b) for every p ∈ int Δ the φ-p-minimiser is a.e. unique, coherent and selected;
- (c) P ∈ ∏𝒫_i^+ (forced), and E(P) = ∅: the integral field ψ^P has an a.e.-unique coherent Bayes model at every
  interior weight.

*Proof.* P_i ∈ 𝒫_i^+ by Theorem 1.2 (M_i = {P_i}).

(a) Fix p and put I := inf_M p·φ.
1. *Selected models approach I.* Take X_m with p·φ(X_m) → I. Fact 0(a) gives selected C_m = C_{q_m} with C_m ⪯_i X_m,
   hence φ(C_m) ≤ φ(X_m). By compactness of Δ, of the coherent models in measure (CBOI lem:compact), and of the bounded
   profile vectors, pass to a subsequence with q_m → q*, C_m → C_∞ in measure (C_∞ coherent) and φ(C_m) → z. Then
   p·z = I.
2. *Values just above z_i are attained.*
   - Fix a carrier F of P_i^s with μ(F) < μ(U_+). For a model C, let w̄(g) be the world-i-worst advice in the advice range and
     ν_C(S) := ∫_S (λ_i(g, w̄(g)) − λ_i(g, a_C(g))) ρ_i(g) dμ for S ⊆ H∖F. This is a finite non-atomic measure.
   - Worsening C to w̄ on S ⊆ H∖F leaves the pure part unchanged and gives the value φ_i(C) + ν_C(S). Hence
     V_i := {φ_i(X) : X ∈ M} ⊇ φ_i(C) + [0, ν_C(H∖F)] (one-dimensional Lyapunov).
   - By dominated convergence, ν_{C_m}(H∖F) → ν_{C_∞}(H∖F) =: 2δ. Moreover δ > 0, because on U_+∖F (non-null)
     C_∞ gives the world-i-best advice, which is strictly better than w̄, and ρ_i > 0 there.
   - Since φ_i(C_m) → z_i, for every ε ∈ (0, δ) some m has φ_i(C_m) ∈ (z_i − ε/2, z_i + ε/2), and then
     V_i ⊇ [φ_i(C_m), φ_i(C_m) + 2δ] meets (z_i, z_i + ε).
3. *Closed sections give l.s.c. along the sequence.*
   - Let X ∈ M with v := φ_i(X) ∈ (z_i, z_i + ε). For all large m, φ_i(C_{q_m}) < v, i.e. C_{q_m} ⪯_i X (here the
     representation, i.e. completeness, is used). By (S), A_i(X) = {q : C_q ⪯_i X} is closed, so q* ∈ A_i(X).
   - Hence φ_i(C_{q*}) ≤ v < z_i + ε. As ε ↓ 0, φ_i(C_{q*}) ≤ z_i.
4. Therefore p·φ(C_{q*}) ≤ p·z = I, so the selected model C_{q*} attains.

(b) Let p be interior and B attain. Fact 0(a) gives a selected C ⪯ B, and p·φ(C) ≤ p·φ(B) with every coordinate ≤
forces φ(C) = φ(B). Since φ_i represents ⪯_i, C ~_i B for all i, and (C) gives B coherent, in C_L. So every attaining
model is coherent. Uniqueness follows from complementary splices, as in N11 Thm 5.5: if B, B′ attain, then the splices
E_A, E′_A satisfy Λ_iE_A + Λ_iE′_A = Λ_iB + Λ_iB′, so both attain by linearity; both are coherent; R2 Lemma U then
gives a contradiction unless B = B′ a.e. Selected: by (a), C_{q*} attains, so B = C_{q*}.

(c) Prop 3.3(ii). Detection is automatic: φ-ties are L-ties. ∎

**Corollary 3.2 (PROVED, with part (B)).** On the U-domain, or any non-adjacent decomposable domain satisfying
(UN), no ranking satisfying (H) whose worlds are complete coherent almost-preferences (arbitrary states, atoms allowed)
covers T1. *Proof.* Theorem 3.1(c) and Corollary 2.3. Alternatively, by (a)+(b) the charge field φ itself satisfies the
existence proviso of N15 Cor 7.3. ∎

**Remarks 3.3.**
- *Consistency check.* CBOI's Prop prop:example (ν = μ/2 + η/2) is a complete charge system satisfying (H). Theorem 3.1
  says its Bayes infimum is attained by a selected model at every p. That is true there: C_p = D_{{p}} is φ-Bayes.
  CBOI Thm fa excludes the vacuous target, and Corollary 3.2 excludes T1.
- *What is new relative to N11.7.* Neither (SN) nor (CD) is needed. Attainment is proved at every weight, not only at
  p_T. The non-convexity of the charge attainable set caused by atoms (N11 Remark 5.4) is irrelevant: the l.s.c. step
  needs only one-dimensional value intervals produced by the *integral* part off a carrier, and those exist whatever
  the atoms do.
- *Why it does not extend to incomplete worlds.* Step 3 needs the converse of (W): φ_i(C) ≤ φ_i(X) ⇒ C ⪯_i X. For a
  non-singleton M_i, the only general way to make C_{q_m} ⪯_i X unanimously is to make X pointwise at least as bad as
  every C_{q_m}. The natural choice is the upper envelope of the tail, which equals C_∞ off sets S_N with μ(S_N) → 0.
  Members of M_i may carry pure mass on S_N. Then φ_i(X) does not converge to φ_i(C_∞), and the bound is lost. This
  happens already for finitely generated M_i, where (CD) holds. So attainment at every interior weight is OPEN for
  finitely generated incomplete worlds. On the integral route, though, attainment is needed only to *test* detection
  (Prop 3.3), not for the field itself.

### 3.3 Other cases

- *(D^CA)* (N11.2: each strict comparison is detected by a CA member). N11 Thm 2.1 gives an integral aggregate with
  unique coherent Bayes models at **every** interior weight, so (U) holds for that aggregate. Note that N11's
  aggregate need not use members of 𝒫_i^+ individually; its density is > 0 a.e. by N11 Thm 2.1 step 3.
- *Case CA* (all members countably additive) is a special case. So is every M_i that is the weak-* closure of its CA
  members (N13).

---
## 4. Anatomy of an exceptional weight (N22.5)

**Prop 4.1 (PROVED).** Assume (H), (CP-a), and suppose P ∈ ∏𝒫_i^+ consists of countably additive members, so that
φ = ψ = ψ^P. Let p_0 ∈ E(P), with tie set Z := Z_{p_0}(P) non-null, and let 𝔉 := {ψ(B) : B is ψ-p_0-Bayes}. Then:
- (i) 𝔉 is compact, convex, contained in the hyperplane {y : p_0·y = min}, and of dimension ≥ 1;
- (ii) every y ∈ 𝔉 is the profile of a selected model;
- (iii) there are a selected C, an incoherent ψ-p_0-Bayes B′ with ψ(B′) = ψ(C), a world j and a member Q ∈ M_j with
  Q(Λ_jB′ − Λ_jC) > 0 = P_j(Λ_jB′ − Λ_jC). That is, there is an undetected strict comparison at p_0.

*Proof.*
- (i) The p_0-Bayes models are exactly the pointwise minimisers. So 𝔉 = ψ(B_0) + {∫_A w dμ : A ⊆ Z} for a fixed
  minimiser B_0, with w(g) = ψ(g, b(g)) − ψ(g, a(g)) on the piece of Z where B_0 takes a(g) and the tied advice is b(g).
  This is the range of a non-atomic vector measure: compact and convex by Lyapunov. Also w ≠ 0 a.e. on Z (strict
  guidance), so the range is not a point.
- (ii) Let B be p_0-Bayes. Fact 0(a) gives a selected C ⪯_i B for all i. By (W), ψ(C) ≤ ψ(B). Since p_0 is interior
  and B is a minimiser, ψ(C) = ψ(B).
- (iii) Let B′ be a minimiser B_0 switched on Z ∩ {|g| < 1} (as in Prop 3.3(ii)). B′ is a minimiser and is not a.e. a
  cone, so it is incoherent. Fact 0(a) gives a selected C ⪯_i B′, with ψ(C) = ψ(B′) by (ii)'s argument. If C ~_i B′ held
  at every world, (C) would make B′ coherent. So C ≺_j B′ at some j. By N11 Prop 1.1(ii), Q(Λ_jB′ − Λ_jC) > 0 for some
  Q ∈ M_j, while P_j(Λ_jB′ − Λ_jC) = ψ_j(B′) − ψ_j(C) = 0. ∎

**Reading.** In a hypothetical cover, the selection must realise, at each exceptional weight, a non-degenerate face of
Bayes profiles of a fixed integral field. It must also keep the incoherent realisers of those profiles out of C_L by
comparisons that the field's own members do not see. This is the (CP-a) analogue of R11's mechanism (M2), now pinned to
a Lebesgue-null set of weights and to pairs with *equal* profiles.

**Proof of N22.5.**
- First bullet: Corollary 3.2.
- Second bullet: Corollary 2.3.
- Third bullet: Prop 3.3(ii) (contrapositive).
- Fourth bullet: Prop 4.1(ii). ∎

**On proving (U): what does not work, and what might.**
1. *Additive data alone do not exclude E(P) ≠ ∅.* I did not find a proof that an integral field whose Bayes models are
   a.e.-unique and coherent at a.e. weight, and coherent somewhere at every weight, must have no tie weights.
   - The candidate obstruction is a "jump line": a non-null set G of problems all of whose chart lines equal one line ℓ.
     The one-sided Hausdorff limits K_± at ℓ then satisfy D_{K_+} = D_{K_−} ∪ G mod null.
   - The candidate "fan" is a pencil of distinct chart lines through p_0.
   - A short argument (CHECKED, sketch) restricts both. For g ∈ G, the directional limits K_v at p_0 have
     v ↦ P_{K_v}(g) two-valued: their superlevel sets are nested open half-circles of equal length, hence equal. The
     tie set G is also invariant under small 𝟙-shifts.
   - Rank-deficient projective vertex maps, the natural source of fans, violate K ⊆ Δ.
   - None of this excludes ℓ outright. So (U) must use L, not only (α)–(δ).
2. *Using L: perturbing the member choice.* ∏𝒫_i^+ is convex, and every choice satisfies (α)–(δ). For two choices P, Q
   and a fixed p_0, the mixing parameters t for which (1−t)P + tQ has a tie at p_0 form a countable set: they are the
   atoms of the push-forward of μ under g ↦ −p_0·c_P(g)/p_0·c_Q(g). But p_0 ranges over a continuum. A genericity
   argument would need a family of choices whose CA densities are "rich in direction". That is false in general: in
   N11 Prop 5.2 all CA parts of the world are multiples of μ̄. If *every* world were of that kind, the CA field on M_U
   would be flat and its generic Bayes models would be unions of sign orthants (accept h iff Σ_{h_i>0} p_ic_i >
   Σ_{h_i<0} p_ic_i). Those are incoherent, contradicting (β). So Theorem 2.1 already excludes systems in which all
   worlds are flat, though not a single flat world. This suggests a dichotomy (CONJECTURE N22.D):
   - either 𝒟_i := {ρ_P : P ∈ M_i} is rich enough for a generic choice to have E = ∅;
   - or it is rigid enough that detection at E(P) follows from Prop 4.1(iii) together with (S).
3. *Using L: closed sections at p_0.* For p ∉ E(P) near p_0, the selected models approximating the unique Bayes model
   B_p (it is their limit in measure, Prop B (β)) converge, as p → p_0 along a direction v, to the coherent directional
   limit X_v. Their indices accumulate at points q_v. For any X that is pointwise at least as bad as a tail, (S) gives
   C_{q_v} ⪯_i X. In the integral case (Prop 4.1) this yields ψ(C_{q_v}) ≤ ψ(X_v), so C_{q_v} is a selected
   p_0-Bayes model with the v-extreme profile of 𝔉. Turning this into a contradiction would need a link between
   v ↦ q_v and the closed sections at the interior of 𝔉. I have not found one. (Compare R11 §4.3: at a *boundary* tie,
   the analogous face is harmless after reindexing. At an interior weight, reindexing cannot remove a tie of a fixed
   field, so the contradiction, if any, must come from L.)

---

## 5. (CP-a) for the paper (N22.6)

**Definition (coherent almost-preference worlds).** Fix a decomposable domain M on the problem space (H, μ) and a world i.
World i's ranking is a *coherent almost-preference over losses* if there are
- (CP-a1) a measurable penalty λ_i(g, a), bounded on the graph of the advice-range correspondence g ↦ A(g), with
  λ_i(g, a) < λ_i(g, b) whenever a is strictly better than b in world-i guidance rank at g (for μ-a.e. g); and
- (CP-a2) a coherent lower prevision P̲_i on L^∞(H, μ) (Walley 1991, Def. 2.3.3),

such that, for all X, Y ∈ M,
 X ⪯_i Y ⟺ P̲_i( λ_i(·, a_Y(·)) − λ_i(·, a_X(·)) ) ≥ 0.

*Equivalent forms* (Walley 1991, Thm 3.8.1 and §3.8.4; L^∞(μ) is a linear space containing the constants):
- (i) X ⪯_i Y iff the loss difference lies in a coherent class D_i of almost-desirable gambles on L^∞(μ) (D0–D4: a
  sup-norm-closed convex cone containing L^∞_+ and no gamble with ess sup < 0).
- (ii) X ⪯_i Y iff P(Λ_iY − Λ_iX) ≥ 0 for every P in a non-empty weak-* closed convex set M_i of linear previsions on
  L^∞(μ). These are the positive normalised linear functionals, i.e. finitely additive probabilities vanishing on
  μ-null sets.
- (iii) ⪯_i is a coherent almost-preference relation (R0–R5) on the loss gambles, transported to models by X ↦ −Λ_iX.

*Gambles are taken modulo μ-null sets*: "X ≥ Y" means ≥ a.e. This is the only modification of Walley's setting, and it
is what makes the relation well defined on models.

*What is not assumed.*
- No countable additivity, separability or non-atomicity of M_i.
- No completeness.
- No conglomerability (Walley's D5).

*Automatic consequences* (N11 Prop 1.1; §1 here).
- ⪯_i is a preorder; (IB) and weak (G) hold.
- Strict (G) at i holds iff P̄_i(A) > 0 for every non-null set A of non-singleton problems (Lemma 1.0). It then implies
  that some member of M_i has an a.e.-positive countably additive part (Theorem 1.2).
- Every member P ∈ M_i weakly respects ⪯_i (W).

*Instances.*
- Additive rankings with integral penalties (M_i = {ρμ}).
- Charge-valued additive rankings (M_i = {P}), e.g. CBOI's example.
- Unanimity (Pareto) of any family of additive rankings sharing the encoding.
- Credal-set rankings.

*Excluded.*
- Walley's strict-preference variant (CP-s) and the Walley-2000 variant (CP-b) with D_i = D_i^+: these are inconsistent
  with (S) in the additive case (N13 Prop A).
- Genuinely non-Archimedean (lexicographic) desirability: (CP-b) with invisible desirability, N11.10.

*Canonical encoding on M_U* (BRIEF6): λ_i(g, a) = 1 if a is a world-i error at g, else 0. Then
Λ_iX = 1_{E_i(X)} with E_i(X) = X △ (U ∩ {h_i > 0}), and X ⪯_i Y iff P(E_i(Y)) ≥ P(E_i(X)) for all P ∈ M_i.

*Suggested statement of the result in the paper.*

> **Theorem.** Let M be a non-adjacent decomposable domain (e.g. the U-domain), and let L satisfy strict (G), (IB), (LA),
> (S), (C), with (LF) at T1. Suppose each world's ranking is a coherent almost-preference over losses.
> - (a) If every world is complete, then T1 ∉ C_L.
> - (b) In general, if T1 ∈ C_L, then for every choice of members with a.e.-positive countably additive parts, the
>   integral field built from those parts has non-null Bayes ties at some interior weight.

---

## 6. Status

| Claim | Status | Hypotheses beyond (H) + (CP-a) |
|---|---|---|
| Lemma 1.0: strict (G) ⇔ P̄_i > 0 on non-null sets of non-singleton problems | PROVED | — |
| Lemma 1.1: a weak-* compact convex set of states with no CA mass on A has a common non-null null-set N ⊆ A (Kneser minimax) | PROVED | — |
| Thm 1.2 (N22.1): (FS^c) is automatic; 𝒫_i^+ non-empty, convex, absorbing | PROVED | strict (G) |
| Thm 2.1 (N22.2): integral field with (α)–(δ) for every P ∈ ∏𝒫^+ | PROVED | coverage of T1 |
| Gaps (2) attainment and (3) atoms are irrelevant on the integral route | PROVED (as stated, §2) | — |
| Cor 2.3 (N22.3): cover ⇒ E(P) ≠ ∅ for all P | PROVED, using N15 Thm 7.1 / Cor 7.2 | non-adjacent domain |
| Lemma 3.0: charge minimisers are pointwise CA minimisers (ties allowed) | PROVED | — |
| Prop 3.3: attainment + local detection at p ⇒ p ∉ E(P); attainment at p ∉ E ⇒ minimiser selected | PROVED | — |
| Thm 3.1: complete worlds ⇒ attainment at every weight, unique coherent selected minimisers, E = ∅ (atoms allowed) | PROVED | (UN); M_i singletons |
| Cor 3.2: no complete coherent almost-preference cover of T1 | PROVED, using part (B) | non-adjacent domain, (UN) |
| (D^CA) ⇒ (U) | PROVED (N11 Thm 2.1) | (D^CA) |
| Prop 4.1: anatomy of an exceptional weight (CA members) | PROVED | CA members in 𝒫^+ |
| Two-valued directional support functions at a tie weight | CHECKED (sketch) | — |
| Attainment at every weight for finitely generated incomplete M_i | OPEN | — |
| N22.U: (U) for every (CP-a) system ⇔ no (CP-a) cover of T1 (non-adjacent domains) | CONJECTURE | — |
| N22.D: rich-or-rigid dichotomy for CA densities | CONJECTURE | — |

**For the paper.**
- Complete case: closed. "Each world's accuracy ranking is a complete coherent almost-preference" already makes T1
  uncoverable, with arbitrary finitely additive penalties.
- Incomplete case: the reduction is complete except for one explicit property (U) of one integral field. Detection,
  attainment and atoms no longer appear as separate hypotheses.
