# Q2. Conjecture N17.B′ in two worlds: the null sets of a failing world are initial segments, and certificates come in mirror pairs

15 Oct 2026, round 12, exclusion side. Labels: **PROVED** (full proof here, from the cited inputs), **CHECKED**,
**CONJECTURE**, **NUMERICS**. Terminology as in TERMFIX_RULES and the writeup (decomposable domain, U-domain M_U,
advice range). Inputs used, all refereed: P4B_referee (Lemma N0, Lemma B0, Lemma B1 with Cor N1, Lemmas DL, DR,
Lemma T, Thms E2, E3, the cut-pair reformulation of §5), N22 Lemma 1.1 / Thm 1.2, N19 Lemma R1, writeup Thm kkm
("Fact 0"). No assumption is added. No script was needed this round, so `q2py/` was not created; no proof uses NUMERICS.

---

## 0. Outcome

**Nested n = 2 (the setting of P4 §5, P4B §1).** N17.B′(2) is **not** proved in full. New structural results (LF, IS, MP)
cut the open class down considerably.

- **Theorem LF (PROVED; left-fineness).** Fix a cut a ∈ (0,1) and a non-null Z to the right of it (Z ⊆ d_a). Then
  c_a splits into finitely many slabs, and every subset Q of any of them satisfies Q ≤₁ Z. These are relevant
  comparisons. The proof uses competitiveness together with Lemma T **of the other world**. A Lebesgue-number form
  gives the "uniform Lemma DR" that P4B §8.5 asked for.
- **Corollary IS (PROVED; the null sets are initial).** World 1 fails SP^reg iff some initial segment c_a with a > 0
  is null for every endorsing charge. More precisely, let a\* := inf over endorsing charges ν of
  sup{a : ν(c_a) = 0}. Then:
  - SP₁ ⇔ a\* = 0;
  - if a\* > 0, every c_a with a < a\* is 𝓜₁-null, and every 𝓜₁-null set lies in c_{a\*};
  - some single endorsing charge is strictly positive on d_{a\*}.

  So a spread-out certificate can only export the mass of an **initial segment**. It can never isolate a set lying in
  the middle or at the right.
- **Proposition MP (PROVED; mirror pairs).** Suppose a non-null Z satisfies Z ≤₁ A_j for infinitely many pairwise
  disjoint A_j (P4's "minimal shape"; bounded overlap suffices). Then some final segment d_{b₀}, b₀ < 1, satisfies
  d_t ≤₂ A_j for all j and all t ∈ [b₀,1). So **world 2 fails SP^reg too**, with the mirror certificate.
- **Corollary MP′ (PROVED).** In such a system, neither world is complete, CP-a, or has a nonzero leading charge.
  - The open class of P4B §8.5 must therefore be inhabited at **both** worlds at once.
  - Neither world can be additive, even on a sub-family containing the base comparisons, in the way that N17.8's band
    is (Prop NS).
- **Exact surviving certificate shape (§4).**
  - It exports the mass of an initial segment c_a.
  - Its targets avoid every slab near every point (Lemma T).
  - The left-fineness comparisons do not help it.
  - In its simple form it is mirrored by a world-2 certificate exporting a final segment through the **same** targets.
  - §4.3 states exactly where the proof stops: a quantitative link between the width of Lemma T's neighbourhoods and
    the measure of the target is missing.

**Non-nested n = 2 (§5).**
- PROVED: on M_U, coherent world-1 error sets form a two-parameter lattice {σ < α} ∪ {τ ≤ β}.
- PROVED: one-dimensional KKM, and a general strict-escape lemma (Lemma G-SE) for any selection.
- Lemmas DL, DR, T, LF all need the chain. Nothing beyond G-SE is proved without nestedness. Whether (S) forces a
  nested C_L in n = 2 is **open** (CONJECTURE Q2.N).

**n = 3 (§6).** What transfers:
- G-SE, in a weakened form;
- the reduction "¬SP ⇔ an 𝓜-null set", via N22.

What breaks, all from one cause: the absence of a complementary world along a cut.
- LF uses (K) on a cut pair with **exactly one** other world. In n = 3 a cut pair's failure at world 1 is absorbed by
  either of two other worlds, and neither is forced.
- Mirror pairs become cyclic triples, with no Lemma T available for them.

---

## 1. Setting

(Nest) as in P4B §1:
- n = 2 on M_U, with strict (G), (IB), (LA), (S), (C);
- the world-1 error sets of the members of C_L form a chain {E_b : b ∈ [0,1]};
- c_b := E_b, d_b := M∖E_b, and [s,t) := E_t∖E_s ("slabs"), where M is the set of mixed problems of U.
- By Lemma N0, C_L is the chain, and (K) holds at every interior b.

World orders are the N9.4 relations ≤₁, ≤₂ on measurable subsets of M:
- they are cancellative and strictly monotone;
- world 2 compares world-2 error sets, and E₂ = M∖E₁ on mixed problems.

**Cut pairs (P4B §5, PROVED there).** For b ∈ (0,1), P ⊆ c_b and Q ⊆ d_b:
- the relevant comparison C_b ⪯₁ X with E₁X = (c_b∖P) ∪ Q is equivalent to P ≤₁ Q;
- the relevant comparison C_b ⪯₂ X with E₂X = (d_b∖Q) ∪ P is equivalent to Q ≤₂ P;
- **(K)** says: P ≤₁ Q or Q ≤₂ P.

𝔚^reg₁ consists exactly of the vectors 1_Q − 1_P for cut pairs with P ≤₁ Q. Put

  𝓜₁ := {probability charges ν on M, vanishing on null sets, with ν(P) ≤ ν(Q) for every cut pair P ≤₁ Q}.

𝓜₁ is weak\*-compact, convex and nonempty. Since it is weak\*-closed, it is also norm-closed. SP^reg₁ means that some
ν ∈ 𝓜₁ is strictly positive on non-null sets. Define 𝓜₂ in the mirror way.

**Symmetry.** Reverse the chain, b ↦ 1 − b, and swap the worlds. The hypotheses ((Nest), (Cl) at both worlds, (K),
strict (G) at both worlds) are invariant. So every result of P4B §8 (DL, DR, T, E2, E3) holds verbatim for world 2,
with c and d exchanged. In particular:

**Lemma T₂ (PROVED by symmetry from P4B Lemma T).** Let W be non-null and x ∈ [0,1]. There is η > 0 such that no
non-null Q contained in the slab (x−η, x+η) satisfies W ≤₂ Q.

*Proof.* Lemma T for world 2, with m = 1, says that there is no sequence of non-null Q_j ⊆ (x−1/j, x+1/j) with
W ≤₂ Q_j for all j. If every j admitted such a Q_j, they would form one. ∎

Lemma T₁ is the same statement for world 1.

---

## 2. Left-fineness, and why null sets are initial

### 2.1 Theorem LF (PROVED)

Let a ∈ (0,1) and let Z ⊆ d_a be non-null. There are finitely many slabs J_1, …, J_m covering c_a such that every
measurable Q ⊆ c_a ∩ J_i satisfies Q ≤₁ Z, for every i.
- Each comparison Q ≤₁ Z is a relevant comparison (a cut pair at a).
- Hence every ν ∈ 𝓜₁ satisfies ν(c_a) ≤ m·ν(Z).
- *Uniform form:* there is δ = δ(Z,a) > 0 such that Q ≤₁ Z for every Q ⊆ c_a lying in a slab of width < δ.

*Proof.*
1. For each x ∈ [0,a], Lemma T₂ (applied with W = Z) gives η_x > 0 such that no non-null Q ⊆ (x−η_x, x+η_x)
   satisfies Z ≤₂ Q.
2. The open intervals (x−η_x, x+η_x) cover the compact interval [0,a]. Take a finite subcover J_1, …, J_m, and a
   Lebesgue number δ for it. Every slab of width < δ inside [0,a] then lies in some J_i.
3. Let Q ⊆ c_a ∩ J_i.
   - If Q is null, Q ≤₁ Z by monotonicity (Q ~₁ ∅ ⊆ Z).
   - If Q is non-null, (Q, Z) is a cut pair at the interior cut a. By (K), Q ≤₁ Z or Z ≤₂ Q. The second is excluded
     by step 1. So Q ≤₁ Z.
4. For ν ∈ 𝓜₁: ν(c_a) ≤ Σ_i ν(c_a ∩ J_i) ≤ m·ν(Z). ∎

*Inputs used:*
- (K) at one interior cut;
- Lemma T for world 2, which uses (Cl) at both worlds, (K) and strict (G) at both worlds (P4B §7 table, mirrored).

*Reading.*
- This is P4B's Lemma DR made uniform: the width δ depends on Z only, not on the position x.
- It is the "left half" of Savage fineness, obtained without completeness: (K) converts world 2's inability to rank a
  concentrated set above Z into world 1's ranking of that set below Z.
- It concerns only sets to the **left** of Z. Relevant comparisons are always "left ≤₁ right", so LF bounds ν on the
  left by ν on the right. It gives no lower bound on the left. That is exactly why it does not finish the proof.

### 2.2 Corollary IS (PROVED; the 𝓜₁-null ideal is generated by an initial segment)

For ν ∈ 𝓜₁ put a₀(ν) := sup{a ∈ [0,1] : ν(c_a) = 0}, and a\* := inf_{ν∈𝓜₁} a₀(ν).
- (i) If ν ∈ 𝓜₁, then ν(Z) > 0 for every non-null Z ⊆ d_{a₀(ν)}.
- (ii) Some ν̄ ∈ 𝓜₁ has a₀(ν̄) = a\*. So ν̄ is strictly positive on non-null subsets of d_{a\*}.
- (iii) SP^reg₁ ⇔ a\* = 0.
- (iv) If a\* > 0:
  - every c_a with a < a\* is 𝓜₁-null;
  - every 𝓜₁-null set is contained in c_{a\*} (mod null).

  Hence ¬SP^reg₁ ⇔ some initial segment c_a, a > 0, is 𝓜₁-null. Equivalently, for every ε > 0 there are cut pairs
  P_k ≤₁ Q_k and λ_k ≥ 0 with

    1_{c_a} + Σ_k λ_k (1_{Q_k} − 1_{P_k}) ≤ ε  a.e.

*Proof.*
- (i)
  - Let Z ⊆ d_{a₀} be non-null, with a₀ = a₀(ν) < 1. The case a₀ = 1 is vacuous.
  - By countable additivity of μ, Z ∩ d_b is non-null for some b ∈ (a₀,1).
  - ν(c_b) > 0, since ν(c_·) is nondecreasing and b > a₀.
  - LF at the cut b gives ν(c_b) ≤ m·ν(Z ∩ d_b). So ν(Z) > 0.
- (ii)
  - Choose ν_k ∈ 𝓜₁ with a₀(ν_k) ↓ a\*, and put ν̄ := Σ_k 2^{−k}ν_k. It lies in 𝓜₁, which is convex and norm-closed,
    and the series converges in norm.
  - For a > a\*, some k has a₀(ν_k) < a, so ν̄(c_a) ≥ 2^{−k}ν_k(c_a) > 0. Hence a₀(ν̄) ≤ a\*, and so a₀(ν̄) = a\*.
  - Apply (i).
- (iii)
  - (⇐) By (ii) with a\* = 0, ν̄ is strictly positive on M = d_0. It endorses every relevant comparison, since in the
    nested case these are exactly the cut pairs (Lemma N0(ii)). So SP^reg₁ holds.
  - (⇒) A strictly positive ν has ν(c_a) > 0 for every a > 0, so a₀(ν) = 0.
- (iv)
  - For a < a\* ≤ a₀(ν), ν(c_a) = 0 for every ν.
  - If Z is non-null with Z ∩ d_{a\*} non-null, then Z ∩ d_b is non-null for some b > a\*, and ν̄(Z) > 0 by (ii).
  - The certificate form is the separation step of P4 §5.5 (CONFIRMED in P4B §5), applied to B = c_a. ∎

*Remark (relation to N22 Lemma 1.1).*
- N22 Lemma 1.1 produces *some* non-null 𝓜-null set inside any set on which every member's countably additive part
  vanishes.
- Cor IS says much more in the nested two-world case: the 𝓜₁-null ideal contains no set disjoint from c_{a\*}.
- So the "spread-out" certificates of P4B §8.5 are spread out only in their **targets** Q_k. What they export is
  always the mass of an initial segment.

### 2.3 Mirror statements (PROVED by symmetry)

- For world 2 the right-fineness theorem LF₂ holds: for Z ⊆ c_a, d_a is a finite union of slabs whose subsets are
  ≤₂ Z.
- ¬SP^reg₂ ⇔ some final segment d_b, b < 1, is 𝓜₂-null.

---

## 3. Simple certificates come in mirror pairs

### 3.1 Proposition MP (PROVED)

Let Z be non-null. Suppose Z ≤₁ A_j for j = 1, 2, …, where the A_j have bounded overlap: Σ_j 1_{A_j} ≤ r.
(These need not be relevant comparisons.) Then there is b₀ ∈ (0,1) such that, for every j and every t ∈ [b₀,1):
- d_t ≤₂ A_j;
- this is the relevant world-2 comparison C_t ⪯₂ X with E₂X = A_j.

Consequently every ν ∈ 𝓜₂ vanishes on d_{b₀}, and **¬SP^reg₂**.

*Proof.*
1. Lemma T₁ at x = 1 with Z gives η > 0 such that no non-null Q ⊆ d_{1−η} satisfies Z ≤₁ Q. Put
   b₀ := max(1−η, ½).
2. Fix t ∈ [b₀,1) and j. Consider the cut pair (P, Q) := (A_j ∩ c_t, d_t ∖ A_j) at the interior cut t.
   - Suppose P ≤₁ Q. By cancellation this is A_j ≤₁ d_t, because A_j∖d_t = P and d_t∖A_j = Q.
   - Then Z ≤₁ A_j ≤₁ d_t, with d_t ⊆ d_{1−η} non-null. This contradicts step 1.
   - So P ≰₁ Q, and (K) gives Q ≤₂ P. That is C_t ⪯₂ X with E₂X = (d_t∖Q) ∪ P = (d_t ∩ A_j) ∪ (A_j ∩ c_t) = A_j.
     In set form, d_t ≤₂ A_j.
3. For ν ∈ 𝓜₂: ν(d_t) ≤ ν(A_j) for all j. Summing over j gives J·ν(d_t) ≤ Σ_{j≤J} ν(A_j) ≤ r for all J. So
   ν(d_t) = 0. ∎

**Corollary MP-loop (PROVED).** Apply MP, then its mirror image (to W := d_{b₀} ≤₂ A_j). This gives s₀ > 0 with
c_s ≤₁ A_j for all j and all s ∈ (0, s₀]. So:
- a simple world-1 certificate with *any* exported set Z upgrades to one exporting an initial segment, with the same
  targets (consistent with Cor IS);
- a simple certificate in either world forces one in the other, through the **same** targets A_j.

**Corollary MP′ (PROVED).** Suppose a system has a simple certificate (as in MP) at world 1. Then **each** world is:
- not complete;
- not CP-a;
- without a nonzero leading charge.

*Proof.*
- World 1:
  - A complete world has a strictly positive P with B ≤₁ C ⇒ P(B) ≤ P(C) (Thm E3, CHECKED). Then P(Z) ≤ P(A_j) → 0,
    a contradiction.
  - A CP-a world has a member with countably additive density > 0 a.e. (N22 Thm 1.2), and that member endorses all of
    its comparisons. The same contradiction follows.
  - A nonzero leading charge is strictly positive and satisfies A ≤₁ B ⇒ π(A∖B) ≤ π(B∖A) (Thm E2). The same
    contradiction follows.
- World 2: the same three arguments, applied to d_{b₀} ≤₂ A_j (MP), using E2, E3 and N22 for world 2 (by symmetry). ∎

### 3.2 What this means for constructions

**Proposition NS (PROVED; no additive scaffold).** Let π be any charge ≥ 0 vanishing on null sets. Suppose world 1
accepts every cut pair that π strictly favours, i.e. π(P) < π(Q) ⇒ P ≤₁ Q, at least for cut pairs at cuts
t ∈ [b₀,1). If world 1 has a simple certificate Z ≤₁ A_j, then π(d_{b₀}) = 0.

*Proof.*
- By step 2 of MP, A_j ∩ c_t ≰₁ d_t∖A_j for t ≥ b₀. Hence π(d_t∖A_j) ≤ π(A_j ∩ c_t) ≤ π(A_j).
- So π(d_t) ≤ 2π(A_j). The A_j are disjoint (or of bounded overlap), so π(A_j) → 0 along a subsequence. Hence
  π(d_t) = 0. ∎

*Consequence.*
- N17.8's architecture, "an additive band (unanimity over densities bounded below) plus exotic patches", cannot carry
  a simple certificate.
- Its band contains the strict μ-comparisons on cut pairs, and μ(d_{b₀}) > 0.
- More generally, any world 1 in such a system must reject cut pairs of the form "tiny spread set ≤₁ almost-full
  final segment" near the right end. World 2 must reject their mirrors near the left end.
- In particular the strict comparisons of every ν₂ ∈ 𝓜₂, which (K) forces into world 1, give nothing on d_{b₀}.
  This is consistent with MP.

---

## 4. Nested n = 2: what survives, and where the proof stops

### 4.1 Exact shape of a surviving certificate (PROVED necessary conditions)

If world 1 fails SP^reg in a nested two-world system, then all of the following hold.

- **(a) What is exported.** The exported set is an initial segment c_a with a > 0 (Cor IS). For every ε there are cut
  pairs P_k ≤₁ Q_k (P_k left of the cut a_k, Q_k right of it) with 1_{c_a} + Σλ_k(1_{Q_k} − 1_{P_k}) ≤ ε. Every set
  disjoint from c_{a\*} is charged by the single endorsing charge ν̄.
- **(b) The targets are not concentrated.**
  - No non-null set is ≤₁ sets shrinking to finitely many points (Lemma T₁).
  - In particular no exported mass can be sent into a fixed small slab around any point.
- **(c) Left-fineness holds and is irrelevant.** Subsets of narrow slabs to the left of any non-null Z are ≤₁ Z (LF).
  These comparisons only bound mass on the left by mass on the right.
- **(d) Escape.** Strict escape (B1, Cor N1) and the slab-dropping lemmas DL and DR hold.
- **(e) If simple, it is mirrored.**
  - If the certificate can be taken simple (Z ≤₁ A_j with bounded overlap), then world 2 fails SP^reg through the
    mirror certificate d_t ≤₂ A_j, with the **same** targets (MP).
  - Neither world is complete, CP-a, or has a nonzero leading charge (MP′).
  - Neither world accepts all strict cut comparisons of a charge charging the far end (Prop NS).
- **(f) Charge bounds.** By (a) and §5.5 of P4 there is a charge ν̄ ∈ 𝓜₁, positive on non-null subsets of d_{a\*},
  with ν̄(c_a) = 0 for a < a\*. Integrating the certificate against ν̄ gives
  0 ≤ λ_k(ν̄(Q_k) − ν̄(P_k)) ≤ ε for every k.
  So each target Q_k is ν̄-almost as light as its source P_k, while the sources jointly cover c_a with weight ≥ 1 − ε.

### 4.2 Two remarks ((i) PROVED; (ii) a remark and an open case)

- **(i) The world-1 restriction to d_{a\*} has SP.**
  - Its endorsing charge is ν̄ restricted to d_{a\*}.
  - It endorses the cut comparisons inside d_{a\*}, by monotonicity of ≤₁ (P ∩ d_{a\*} ⊆ P).
  - So the failure is *localised*: the system restricted to the right of a\* is fine.
  - The failure is the impossibility of extending any such ν̄ to the left. That is, the exported mass of c_a is
    always absorbed by targets that every endorsing charge sees as arbitrarily light.
- **(ii) Trivial members of 𝓜₁, and the case a\* = 1.**
  - Every charge concentrated at 1⁻ lies in 𝓜₁: ν(d_b) = 1 for all b < 1, for instance a Banach-limit density at 1
    from the left. Such a ν vanishes on every c_t with t < 1, so ν(P) = 0 ≤ ν(Q) for every cut pair at a cut t < 1.
  - So 𝓜₁ ≠ ∅ is automatic and carries no information. Every ν with a₀(ν) = 1 is of this degenerate kind.
  - Nothing proved here excludes a\* = 1, i.e. that *only* such charges exist. That is the extreme form of the open
    case.

### 4.3 Where the proof stops (honest failure report)

The missing step is to show that c_a, a > 0, cannot be 𝓜₁-null. The natural attempt is to perturb ν̄ by a small charge
τ that charges c_a. The constraint is

  τ(P) − τ(Q) ≤ ν̄(Q) − ν̄(P)  for every cut pair P ≤₁ Q.

This fails exactly on cut pairs whose source P has substantial τ-mass in c_a and whose target Q is ν̄-light.

The available tools control *where* such Q can lie:
- not inside any shrinking neighbourhood of finitely many points (Lemma T₁);
- if the certificate is simple, the same targets are also small in world 2's eyes against final segments (MP).

They do not control *how much* ν̄-mass Q carries. Turning (b) into a lower bound on ν̄(Q) would need a quantitative
link between:
- the radius η in Lemma T₁ (which depends on Z and x, with no rate), and
- the measure of the target.

Closedness of sections supplies only qualitative limits, one cut at a time. Concretely:
- Lemma T₁ excludes Z ≤₁ Q_j when the Q_j shrink to points;
- it says nothing when the Q_j are *thin but spread*. Examples are slabs × thin fibres in the radial coordinate of
  M_U (a mixed problem g and 2g lie on one ray but are distinct problems), or fat-Cantor families in the chain
  coordinate.

A Vitali-type argument that would push spread targets to the right piece by piece needs disjoint receivers D_i whose LF
width δ(D_i) beats the piece width. LF supplies a width for each receiver, but with no rate. That is the same circle
P4B §8.5 identified, now with the "uniform DR" half supplied and the "rate" half missing.

**General certificates versus simple ones.** MP needs the simple shape (one exported set, bounded-overlap targets).
For a general certificate, Lemma T₁ cannot be applied comparison by comparison: the sources P_k are not the exported
set, and the chain of transfers passes through intermediate regions. So **"¬SP₁ ⇒ ¬SP₂" is open in general.** For
simple certificates it is PROVED.

### 4.4 What a counterexample (construction side) must do in n = 2 nested

All PROVED necessary conditions, combining §§2–4 with P4B §8.
1. At world 1: an initial segment c_a, a > 0, null for every endorsing charge, exported to spread-out, thin targets.
   No target family may concentrate near finitely many points.
2. If the export is simple, then world 2 must export a final segment d_b to the **same** targets. Both worlds must
   then lie in the open class: incomplete, not CP-a, no leading charge.
3. Neither world may contain the strict cut comparisons of any charge that charges the far segment (Prop NS). In
   particular the N17.8 "band + exotic patches" architecture is excluded.
4. (K) must hold for every cut pair. Near the right end, world 2 must accept "almost-full final segment ≤₂ thin spread
   set". Near the left end, world 1 must accept "initial segment ≤₁ thin spread set". In between, each cut pair must be
   accepted by at least one world, while every section stays closed.

The natural place to look is the radial (fibre) direction of M_U: targets of the form slab × thin radial set, which
Lemma T cannot see. I did not find a world with closed sections there. Every lexicographic attempt with a non-additive
"shadow" primary (primary = chain-measure of the set of rays a set meets) fails closedness at primary ties, by the
R2 Thm 7 mechanism. For example A = (whole chain) × (thin radial band) has section [0,½), which is open. Every
unanimity-of-charges attempt is CP-a, hence SP. Every strict-unanimity attempt fails closedness at its boundary.
**No construction is claimed.**

---

## 5. n = 2 without nestedness

### 5.1 The coherent error-set lattice on M_U (PROVED)

Let K′ = [α′, β′] ⊂ (0,1), with t the weight on world 2. Write the mixed problems of U as M = M⁺ ⊔ M⁻:
- M⁺ := {g ∈ U : g₁ > 0 > g₂}, with τ(g) := g₁/(g₁−g₂) ∈ (β′,1);
- M⁻ := {g ∈ U : g₁ < 0 < g₂}, with σ(g) := −g₁/(g₂−g₁) ∈ (0,α′).

The coherent members of M_U are the D_K with K = [α,β] ⊇ K′. Their world-1 error sets are

  E₁(D_{[α,β]}) = {g ∈ M⁻ : σ(g) < α} ∪ {g ∈ M⁺ : τ(g) ≤ β},  α ∈ [0,α′], β ∈ [β′,1],

and E₂ = M∖E₁.

*Proof.* For g ∈ M⁺, t ↦ (1−t)g₁ + tg₂ decreases, so D_K accepts g iff β < τ(g). Not accepting is the world-1 error.
For g ∈ M⁻ it increases, so D_K accepts g iff α > σ(g), which is the world-1 error. D_K ⊆ U iff K ⊇ K′. ∎

So E₁ is a two-parameter family, increasing in (α,β) for the product order. C_L is nested iff (α,β) is co-monotone
along it. (This is N17.8's X_{α,β}.)

### 5.2 What holds for any selection (PROVED)

**Fact 0 in one dimension.** For every regular X:
- S₁(X) := {p : C_p ⪯₁ X} and S₂(X) := {p : C_p ⪯₂ X} are closed;
- 0 ∈ S₁(X) and 1 ∈ S₂(X), by competitiveness at the vertices;
- S₁(X) ∪ S₂(X) = [0,1], by competitiveness on {1,2} at interior p.

Hence S₁(X) ∩ S₂(X) ≠ ∅ by connectedness. This is writeup Thm kkm for n = 2.

**Lemma G-SE (strict escape, any selection).** Let C_p ∈ C_L, and let X be regular with E₁X ⊋ E₁C_p (non-null
difference). Then some selected C_q satisfies:
- C_q ⪯₁ X;
- C_q ≺₂ C_p;
- C_q ⋠₁ C_p.

*Proof.*
- Take q ∈ S₁(X) ∩ S₂(X). Then E₂X ⊊ E₂C_p, so X ≺₂ C_p by strict (G), and C_q ⪯₂ X ≺₂ C_p.
- C_p is undominated, so C_q ⋠₁ C_p. ∎

In the nested case G-SE is P4's Lemma B1: q is the point φ₁(A) > b.

### 5.3 What breaks

- Lemma N0 (continuity of β, identification of C_L with the chain) uses nestedness.
- So do B0 (sections are initial segments), the cut-pair form of 𝔚^reg, DL, DR, T, and hence LF, IS and MP. All of
  them parametrise the selection by the position of a single cut.
- Without nestedness, a relevant comparison is P ≤₁ Q with P ⊆ E₁C, Q ⊆ M∖E₁C, for a lattice element E₁C. There are
  two independent "cuts", in M⁻ and in M⁺.
- The sections S₁(X) are closed but need not be intervals, so B0's φ₁ is not defined.

**CONJECTURE Q2.N.** In n = 2 on M_U, strict (G), (IB), (LA), (S) and (C) force {E₁C : C ∈ C_L} to be a chain, i.e.
(α_p, β_p) co-monotone.

If true, the nested analysis above is the whole n = 2 case. I have no proof. The natural route, a non-co-monotone
crossing p < q, combined with G-SE applied to E₁C_p ∪ E₁C_q (the lattice join, a coherent model), produces a third
selected model but no contradiction.

---

## 6. n = 3: what transfers and what breaks

**Transfers (PROVED as stated):**
- Lemma G-SE, in the form: for X with E_iX ⊋ E_iC_p, some selected C_q ⪯_i X with C_q ⪯_j X for all j. This is
  Fact 0. If moreover E_jX ⊆ E_jC_p for all j ≠ i, with one inclusion strict, then C_q ≺_j C_p at that j.
  - On M_U in n = 3, E_j is **not** M∖E_i. So "growing E_i" does not shrink the other error sets, and the second clause
    has no automatic instances. This is the first break.
- The reduction ¬SP_i ⇔ some non-null 𝓜_i-null set ⇔ ε-certificates (N22 Lemma 1.1 + separation). This is
  dimension-free.

**Breaks:**
1. **LF** uses (K) on a cut pair: when world 1 fails, world 2 must accept, and Lemma T₂ forbids that acceptance for
   concentrated sets.
   - In n = 3, competitiveness on {1,2,3} of C_p at interior p gives: C_p ⪯₁ X or C_p ⪯₂ X or C_p ⪯₃ X.
   - A world-1 failure is absorbed by world 2 **or** world 3, and the choice can vary with the concentrated set Q.
   - LF would need Lemma T at both other worlds *jointly*, i.e. no Q in a small neighbourhood with W ≤₂ Q **or**
     W ≤₃ Q. That needs a common neighbourhood, which compactness supplies.
   - But first Lemma T itself is needed at worlds 2 and 3. Its proof (DL, DR, Cor N1) runs along one chain with a
     complementary world, and both are missing along the two-dimensional selection.
2. **Mirror pairs (MP).** The step "A_j ≤₁ d_t is impossible, so world 2 accepts the mirror" turns into "world 2 or
   world 3 accepts". This gives a cyclic distribution of mirror certificates over two worlds, with no single world
   forced to fail SP.
3. **Initial segments (IS)** use the linear order of the cuts. In n = 3 the selected error sets cross (N17.3), and the
   𝓜_i-null ideal has no reason to be generated by one selected error set.

**What a proof in n = 3 would need.**
- A Lemma T at every world: no non-null set is ⪯_i-below sets that shrink to finitely many points, along a
  two-dimensional selection.
- In n = 2 this came from closedness plus strict escape along a chain.
- In n = 3 the natural analogue replaces the chain by the segment of selected models on an edge of Δ. There the third
  world is inactive (competitiveness on a two-element support), so the n = 2 machinery should run on each edge with the
  third world as a spectator.

**CONJECTURE Q2.E.** On each edge [e_i, e_j] of Δ in n = 3, the edge selection, restricted to the problems on which the
third world's error is unchanged along the edge, satisfies the hypotheses of §1, so LF, IS and MP hold there.

This would give the n = 3 analogues for comparisons out of edge models only. Interior selected models, which are the
ones the cyclic (M1) certificates of N17.3 use, would remain open.

---

## 7. Status table

| Statement | Status |
|---|---|
| Lemma T₂ (Lemma T for world 2) | PROVED (symmetry of P4B Lemma T) |
| **Theorem LF (left-fineness; uniform DR)** | **PROVED** |
| **Cor IS: ¬SP₁ ⇔ some initial segment c_a (a > 0) is 𝓜₁-null; 𝓜₁-null sets ⊆ c_{a\*}; ν̄ positive on d_{a\*}** | **PROVED** |
| Mirror statements LF₂, IS₂ | PROVED |
| **Prop MP: a simple world-1 certificate forces a world-2 certificate with the same targets** | **PROVED** |
| Cor MP-loop; Cor MP′ (both worlds incomplete, non-CP-a, no leading charge) | PROVED (MP′ uses E3, which is CHECKED, for the "complete" clause) |
| Prop NS (no additive scaffold; N17.8 architecture excluded) | PROVED |
| §4.1 necessary conditions on a surviving certificate | PROVED |
| N17.B′(2), nested, general certificates | **open** (§4.3: missing a rate in Lemma T) |
| "¬SP₁ ⇒ ¬SP₂" for general certificates | open |
| §5.1 lattice of coherent error sets; Fact 0 in 1-D; Lemma G-SE | PROVED |
| CONJECTURE Q2.N (C_L nested in n = 2) | CONJECTURE |
| n = 3: transfers / breaks (§6) | PROVED as stated; N17.B′(3) open; CONJECTURE Q2.E |
| Construction of a ¬SP world with closed sections | none found; §4.4 lists PROVED necessary conditions |

**Hypotheses added: none.** (Nest) in §§1–4 is the declared hypothesis of the nested case. §5 drops it. All inputs are
listed in the header. No NUMERICS were used.
