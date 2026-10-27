# B3. A complete world with crossing edge selections: construction attempt and failure report

Round 14, note B3 (15 Oct 2026). Scripts: `b3py/` (run with `python3 -I`).
Labels: PROVED / CHECKED / CONJECTURE / NUMERICS. No assumptions are added to (H_U).

## 0. Outcome

**No cover of T₁ was constructed.** This is a failure report.

The route was: a complete world that does not add up, whose edge selections cross. The attempt broke at its first step, the choice of world 1's order. The selection through T₁ and the exact consistency test with (R5) (plan items 3–4) were never reached.

What the attempt established:

1. **The operative property is almost-representability, not nestedness (B3.1, B3.2; PROVED).**
   - For a complete world, a leading charge is the same thing as a nonzero almost-agreeing charge.
   - So Theorem S2.1 already makes every complete world that is almost representable on M add up. No (Nest_e) is needed.
   - Theorem Q36(c) is the special case in which almost-representability comes from Savage fineness.
   - A complete world in a cover must therefore be **non-almost-representable (non-AR) on M**.
2. **Crossing does break Savage fineness, but that buys nothing (B3.4; PROVED, edge level).**
   - There is an edge system with (K) and closed sections at both worlds, in which the complete edge world is not fine and the path crosses.
   - That world is almost representable, so it adds up.
3. **Where it broke (B3.5–B3.7; PROVED).**
   - The only non-AR complete orders on record (IRWAS) have a discrete top level: a KPS comparison of finitely many ultrafilter signatures.
   - An order-continuity lemma on edges (B3.3) excludes every complete world whose top level has densely many null sets. This holds in any ranking with strict (G), (IB) and (S), for every n and every K′. It needs no (C), no third world and no nestedness.
   - To escape, the top level would have to trade heavy pieces against continuous mass at a crossing (the mechanism of B3.4). Cancellation then forces the exchange rates to be additive, which makes the world AR.

**The single obstruction is order continuity on edges against non-almost-representability.**
- **CONJECTURE B3.C.** Every complete world of such a ranking is almost representable on M.
- If B3.C is true, complete worlds are excluded from covers of T₁ outright (Corollary B3.2). The complete-and-crossing route is then closed.
- The suggested form of the obstruction, "(C) plus the third world forces (Nest_e)", is the wrong target:
  - neither (C) nor the third world enters anywhere;
  - (Nest_e) can genuinely fail (B3.4 at edge level), but it no longer matters.

## 1. Setting

Standing hypotheses (H_U): n = 3, the U-domain M_U for T₁, and strict (G), (IB), (LA), (S), (C), with T₁ ∈ C_L. Where a result needs less, this is stated.

Notation, as in writeup §8.5:
- P_i = U ∩ {h_i > 0}, and E_i(X) = X △ P_i;
- M is the mixed part of U;
- R_ij = {h ∈ U : h_i h_j < 0}, and for n ≥ 2, M = ⋃_{j≠i} R_ij;
- for p ∈ e_ij, c_p := E_i(C_p) ⊆ R_ij, and E_j(C_p) = R_ij ∖ c_p (Lemma Q34);
- c_{e_i} = ∅ and c_{e_j} = R_ij;
- X_A is the edge test model (equal to P_i off R_ij, with E_i X_A = A);
- by (G) and (IB), world i is a cancellative, strictly monotone order ≤_i on world-i error sets (N9.4).

**Definitions.**
- World i is **almost representable on M (AR)** if some finitely additive π ≥ 0 on M, vanishing on null sets, with π(M) > 0, satisfies A ≤_i B ⇒ π(A) ≤ π(B) for all measurable A, B ⊆ M.
- A **top level** of world i is a total preorder ⪯ on measurable subsets of M with A ≤_i B ⇒ A ⪯ B.
- A set D is **⪯-null** if D ∼ ∅.

## 2. The reduction

**Lemma B3.1 (PROVED).** Let world i be complete on subsets of M. A charge π ≥ 0 that vanishes on null sets and has π(M) > 0 is a leading charge of world i on M if and only if it almost agrees with ≤_i on M.

*Proof.*
- (⇒) This is the second defining property of a leading charge.
- (⇐) Almost agreement gives the second property, because π(B) − π(A) = π(B∖A) − π(A∖B).
- For the first property, suppose π(B∖A) > π(A∖B). Then π(B) > π(A), so B ≤_i A fails. By completeness, A ≤_i B. ∎

**Corollary B3.2 (PROVED, at the status of Theorem S2.1 and Corollary Q37).** Assume strict (G), (IB) and (S) on M_U, for any n ≥ 2 and any K′.
- Every complete world that is AR on M is strictly positive, endorses every comparison between subsets of M, and adds up (Lemma B3.1 with Theorem S2.1). No nestedness is used.
- Hence the complete clause of Corollary Q37 holds with "complete and edge-nested" replaced by **"complete and AR on M"**. The old clause is the case where AR comes from fineness (Prop Q35(5), Savage).
- Contrapositive, under (H_U): a complete world of a cover of T₁ that does not add up is not AR on M.
- Since edge-nested complete worlds are fine and hence AR (Theorem Q36(c), CHECKED), some edge at e_i must cross. This is the premise of the brief.

So the route needs a **complete non-AR order**. Crossing is necessary for this, but as §3 shows it is not sufficient.

## 3. Order continuity on edges, and crossing against fineness

**Lemma B3.3 (OC; PROVED).** Assume strict (G), (IB) and (S), any n ≥ 2, any K′. Fix an edge e_ij, a point p* ∈ e_ij and a set A ⊆ R_ij.
- (E1) If c_{p*} ≤_i A fails, then c_q ≤_i A fails for all q ∈ e_ij near p*.
- (E2) If A ⊋ c_{p*} with non-null difference, then c_q ≤_i A for all q ∈ e_ij near p*.

*Proof.*
- (E1): the section S_i(X_A) is closed.
- (E2): by strict (G), X_A ≺_j C_{p*}. Closedness of S_j(X_A) gives a neighbourhood N of p* on which C_q ⋠_j X_A. For q ∈ N, competitiveness on supp q ⊆ {i, j} then gives C_q ≼_i X_A, and e_j ∉ N. ∎

Uses: strict (G) at i and j; closed sections at edge test models; competitiveness at edge indices. No (C), no (LA), no third world. This is the semicontinuity step of Theorem S2.1 with the charge removed. If world i is complete, (E1) reads c_q >_i A, so near p* the set c_q is squeezed between c_{p*} ∖ D and c_{p*} ∪ D′ for every fixed non-null D ⊆ c_{p*} and D′ ⊆ R_ij ∖ c_{p*}.

**Why nested paths are fine, and crossing paths need not be.** Let 𝒰 be an ultrafilter of the measure algebra that is heavy for some Z, meaning every member of 𝒰 is >_i Z. At an index p* where c_p switches membership in 𝒰, (E2) gives:
- G ∖ D′ ≤_i L ∪ (D′ ∖ c_q), where G := c_q ∖ c_{p*} ∈ 𝒰 and L := c_{p*} ∖ c_q;
- if the path is nested, L = ∅, and a small D′ gives a contradiction (this is the content of Lemma T);
- if the path crosses, a heavy piece can enter while a compensating piece L leaves.

The next example realises exactly this.

**Proposition B3.4 (crossing defeats fineness; PROVED; edge system, not a ranking).** Setting:
- R = [0, 2) with Lebesgue measure λ (any atomless edge region R_ij is measure-isomorphic to it);
- 𝒰 is an ultrafilter of the measure algebra containing every interval (1, 1 + h);
- 0 < c < 1 and π := λ + c·δ_𝒰;
- both edge worlds rank their error sets by π: c ≤_i A iff π(c) ≤ π(A), and R∖c ≤_j R∖A iff π(c) ≥ π(A);
- the path is
  - c_p = [0, 3pc) for p ≤ 1/3;
  - c_p = (1, 1 + 1.5(p − 1/3)) for 1/3 < p ≤ 2/3;
  - for p > 2/3, c_p grows continuously in measure from (1, 1.5) to R, keeping (1, 1.5).

Then:
- (a) both worlds satisfy strict (G) and (IB);
- (b) m(p) := π(c_p) is continuous, with m(0) = 0 and m(1) = 2 + c. So every section {p : m(p) ≤ π(A)} and {p : m(p) ≥ π(A)} is closed, and (K) holds at every index;
- (c) c_{1/3} = [0, c) and c_{1/2} are disjoint and non-null, so the path crosses. The path jumps in measure at p = 1/3, but not in π;
- (d) ≤_i is not fine: for Z ∉ 𝒰 with λ(Z) < c, every finite partition of R has a piece in 𝒰, of value ≥ c > π(Z). So, by Remark straighten with Prop Q35(5) (CHECKED), no nested edge family with (K) and closed sections exists for this pair of edge worlds;
- (e) π is a strictly positive leading charge, so the world is AR and adds up.

*Proof.*
- (a): π is a strictly positive charge.
- (b): the swap at p = 1/3 replaces λ-mass c by a germ of 𝒰, whose value tends to c as η ↓ 0.
- (c) and (d) are as stated.
- (e) is Lemma B3.1. ∎

NUMERICS: `b3py/prop4_edge.py`, with 𝒰 acting on interval unions through its germ at 1⁺:
- m is continuous (maximum step 1.5·10⁻⁴ on a grid of 30 000 points);
- 0 failures of (K) over 2000 random test sets;
- c_{1/3} and c_{1/2} cross;
- for every random partition, the largest piece has π ≥ 0.401 > π(Z) = 0.05.

*Scope.*
- In a full two-world ranking this world is impossible: Theorem S2.2 forces nesting, and Theorem E3 then forces fineness.
- Whether a third world can realise it in a full three-world ranking (it would need to break the many π-ties among edge models, as in Prop R7.1) is not settled.
- This does not matter for T₁, by (e).

**Consequence for the plan.** Item (2) of the brief, using crossing to break the Savage argument, is achievable, but by itself it yields only AR worlds, which Corollary B3.2 already excludes. A cover needs non-AR structure as well.

## 4. Where the attempt broke: inserting non-AR structure

The only non-AR complete orders in the project are those of *Independent Rankings Without Additive Structure* (IRWAS).
- Their top level is S(A) := {j ∈ J : A ∈ 𝒰_j}, compared by a finite comparative probability ≤₀ on 2^J that is not almost representable (KPS / Conder–Slinko, |J| = 6), followed by a lexicographic tail.
- Transported to error sets on M_U, with cells E_j ∈ 𝒰_j partitioning M, such a world is complete, strictly monotone and cancellative.
- It is non-AR on M: an almost-agreeing π would give weights w_j = π(E_j) almost agreeing with ≤₀, so w = 0 and π(M) = 0.

**Theorem B3.5 (order-continuity triviality; PROVED).** Hypotheses:
- strict (G), (IB) and (S) on M_U, any n ≥ 2, any K′;
- world i complete on subsets of R_ij;
- ⪯ a top level of world i on subsets of R_ij that is cancellative (A ⪯ B iff A∖B ⪯ B∖A);
- every non-null W ⊆ R_ij contains a non-null ⪯-null set.

Then all subsets of R_ij are ⪯-equivalent. If these hypotheses hold on every edge at e_i, and ⪯ is a cancellative top level on M, then ⪯ is trivial on M.

*Proof.*
- Let f(p) be the ⪯-class of c_p, for p ∈ e_ij. Fix p*.
- If c_{p*} is non-null, choose a ⪯-null non-null D ⊆ c_{p*}. Strict (G) gives c_{p*} ∖ D <_i c_{p*}, and (E1) with completeness gives c_{p*} ∖ D <_i c_q near p*. Hence c_{p*} ∼ c_{p*} ∖ D ⪯ c_q. (By cancellation, removing a ⪯-null set does not change the class.)
- If c_{p*} is null, then f(p*) = [∅] ⪯ f(q) by monotonicity.
- Symmetrically, (E2) with a ⪯-null D′ ⊆ R_ij ∖ c_{p*} gives c_q ⪯ c_{p*} ∪ D′ ∼ c_{p*}. If R_ij ∖ c_{p*} is null, then c_q ⊆ c_{p*} up to null sets.
- So f is locally constant on the connected edge e_ij. Hence ∅ = c_{e_i} ∼ c_{e_j} = R_ij, and by monotonicity every subset of R_ij is ⪯-null.
- Every A ⊆ M is a finite disjoint union of pieces inside the R_ik, k ≠ i. By cancellation, adding ⪯-null pieces does not change the class, so A ∼ ∅. ∎

Uses: only Lemma B3.3, strict (G) and completeness of ≤_i on subsets of R_ij. No (C), no third world, no nestedness, no coherence.

**Corollary B3.6 (PROVED).** Under strict (G), (IB) and (S) on M_U, no complete world has a nontrivial top level of the form A ↦ S(A) := {j : A ∈ 𝒰_j}, compared by a comparative probability on signatures, for countably many ultrafilters 𝒰_j of the measure algebra.

In particular:
- **IRWAS-type worlds (a KPS top level over finitely many ultrafilters) cannot occur in any such ranking, for any n and any target.**
- {0,1}-valued first levels (one ultrafilter) are excluded. So are purely finitely additive first levels: apply B3.5 directly, using the carrier lemma (a pure charge vanishes off sets of arbitrarily small μ-measure), which makes its null sets dense. This recovers Corollary S2.1(b) for pure charges.

*Proof.*
- S(A∖B) = S(A) ∖ S(B), so the top level is cancellative.
- Every non-null W contains a non-null set lying in no 𝒰_j. Inductively remove sets G_n ∈ 𝒰_n with μ(G_n) < ε2⁻ⁿ; every ultrafilter contains sets of arbitrarily small measure inside any of its members (IRWAS Lemma 4). The remainder W ∖ ⋃G_n is non-null and lies in no 𝒰_n.
- Such a set leaves S unchanged, so it is ⪯-null.
- Theorem B3.5 then makes the top level trivial on M.
- For IRWAS, S(R_ij) ∪ S(R_ik) = J ≠ ∅ (each 𝒰_j contains M = R_ij ∪ R_ik), so the top level is nontrivial; a contradiction. ∎

**Escaping B3.5 forces additivity.** By B3.5, a discrete top level cannot vary along an edge path, because invisible sets let the path move with its class fixed. To vary continuously, the top level must be able to trade a heavy signature against continuous mass at a crossing, as in B3.4. The natural form is a value top level.

**Proposition B3.7 (exchangeable signatures are additive; PROVED).** Hypotheses:
- world i is complete, with top level Φ(A) = ν(A) + κ(S(A)), meaning A ≤_i B ⇒ Φ(A) ≤ Φ(B);
- 𝒰_1, …, 𝒰_m are distinct ultrafilters and S is the signature map;
- ν is a non-atomic finite measure with ν ≪ μ;
- κ : 2^[m] → ℝ with κ(∅) = 0 and 4·max|κ| < ν(M) (signature differences can be compensated).

Then κ is additive with κ_j ≥ 0, and π := ν + Σ_j κ_j δ_{𝒰_j} almost agrees with world i. So world i is AR, and by Corollary B3.2 it adds up.

*Proof.*
- **Disjoint pieces.** Choose pairwise disjoint G_j ∈ 𝒰_j of small measure: take H_jl ∈ 𝒰_j with M ∖ H_jl ∈ 𝒰_l, put H_lj := M ∖ H_jl, intersect, and shrink.
- **Invisible room.** W₀ := M ∖ ⋃G_j lies in no 𝒰_j, and ν(W₀) ≥ ν(M) − η.
- **Realising s, t and x.** For s, t ⊆ [m], set A := ⋃_{j∈s} G_j ∪ I_A ∪ I_C and B := ⋃_{j∈t} G_j ∪ I_B ∪ I_C, with disjoint I_A, I_B, I_C ⊆ W₀ (Lyapunov).
  - Then S(A) = s and S(B) = t.
  - x := ν(A∖B) − ν(B∖A) ranges over (−ν(M) + 2η, ν(M) − 2η).
  - Φ(A) − Φ(B) = x + D, with D = κ(s) − κ(t).
  - Φ(A∖B) − Φ(B∖A) = x + D′, with D′ = κ(s∖t) − κ(t∖s).
- **Weak cancellation.** By completeness and cancellation of ≤_i: Φ(A) < Φ(B) ⇒ A <_i B ⇒ A∖B <_i B∖A ⇒ Φ(A∖B) ≤ Φ(B∖A), and the same with A and B swapped.
- **Conclusion.** If D ≠ D′, an x strictly between −D and −D′ (realisable, since |D|, |D′| < ν(M)/2) violates weak cancellation. So D = D′ for all s, t.
  - Taking t ⊆ s gives κ additive.
  - Monotonicity against a small G ∈ 𝒰_j gives κ_j ≥ 0.
  - Φ = π is then a nonzero charge vanishing on null sets. ∎

NUMERICS: `b3py/prop7_kappa.py` (exact rationals, m ≤ 4, 400 random κ): 205 additive κ give no violation; all 195 non-additive κ give an explicit violating (s, t, x) in the realisable range.

*Not claimed.* Mixed regimes in which some signature differences exceed the compensable range are not analysed. In such a regime the signature acts lexicographically on those differences, and B3.5 is the expected tool, but no theorem is stated.

## 5. The single obstruction

The attempt broke in the following way.
- A complete world in a cover must be non-AR on M (B3.2).
- Non-AR structure in all known forms is a discrete top level, which order continuity along edges excludes (B3.3, B3.5, B3.6).
- Making that structure continuous enough to pass through a crossing, the one mechanism that defeats fineness (B3.4), makes it additive (B3.7).

**CONJECTURE B3.C (almost-representability from closed choice).** Let a ranking on M_U (any n ≥ 2, any K′) satisfy strict (G), (IB) and (S), and let world i be complete. Then world i is almost representable on M.

Equivalently: no complete, cancellative, strictly monotone, non-AR order on the measure algebra of M admits edge paths with (K) and closed sections at both edge worlds (Lemma B3.3 is the usable form).

*If true:* complete worlds are excluded from covers of T₁ outright (B3.2 with Theorem M0closed(b)), with no nestedness. The route of this brief is then closed.

*If false:* the counterexample is a complete non-AR order with both of the following properties. No such order is known.
- Its top level has no dense family of null sets.
- It is not exchangeable against a non-atomic measure in the sense of B3.7.

*Relation to the old question.*
- The edge form of (R4) and global straightening (Conjecture S1.13) concerned (Nest_e), which mattered for complete worlds only through Theorem Q36(c).
- After B3.2, they matter for complete worlds only as one possible route to B3.C.
- B3.4 shows that this route cannot be the general one: crossing can coexist with non-fineness on an edge.
- (C) and the third world are not used anywhere above, so "(C) plus the third world forces (Nest_e)" would not settle the complete case. B3.C would.

*The incomplete alternative.* For an incomplete world, (E1) yields only that c_q ≤_i A fails near p*, with no lower bound, so B3.5 says nothing. This alternative was not pursued; it remains the two-world-core questions (R1), (R2), (R4) and the interior step of §8.5(f).

## 6. Files

- `b3py/prop4_edge.py`, `.out`: Proposition B3.4 (NUMERICS sanity check; the ultrafilter acts through its germ on interval unions).
- `b3py/prop7_kappa.py`, `.out`: the algebra of Proposition B3.7 (NUMERICS, exact).
