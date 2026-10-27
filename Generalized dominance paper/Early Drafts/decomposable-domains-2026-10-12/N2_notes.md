# N2 (round 20). No blind targets: Pareto off the carriers, the T1-shadow is impossible, and what the edge exchange really leaves

16 Oct 2026, round 20 (BRIEF17; BRIEF13 rules). This file has two parts. **Part I (this note)** is the round-20 note N2
asked for in the round-20 brief. **Part II** (after the horizontal rule at the end) is the earlier note "N2" of
13 Oct 2026 (round 2), kept verbatim, because the write-up cites it as \src{N2}; a copy is also in
`n2py/archive_N2_notes_2026-10-13.md`.

Labels: **PROVED** (full proof here, from results the write-up or the notes mark proved, each named, with the
refereeing status of each input stated), **CHECKED**, **CONJECTURE**, **NUMERICS** (`n2py/r20/`, run with
`python3 -I -B n2_checks.py` from inside `n2py/r20/`; no proof rests on it). No assumption is added; every extra
hypothesis is a hypothesis of a stated theorem.

Notation (as in M1, L4, K3): n = 3, U = D_{K′}, K′ = u + s(T1 − u), M = mixed part of U, N₊ = nonnegative part,
σ_k = sign g_k, P_k = U ∩ {g_k > 0}, E_k(X) = X △ P_k. Q_l = sign class with odd world l, R_ij = Q_i ∪ Q_j (worlds
i, j disagree there; on Q_k they agree). For {i, j, k} = {1, 2, 3}: J_l = {g ∈ M : T1 correct only at l},
W_l = {g ∈ M : T1 wrong only at l}; on R_ij, E_i(T1) ∩ R_ij = W_i ∪ J_j and E_j(T1) ∩ R_ij = J_i ∪ W_j. Write
c_T^{ij} := E_i(T1) ∩ R_ij. Y_k := T1 on R_ij, P_i (= P_j) on Q_k (M1 §1; incoherent by M1.6(b)).
(H_U) = strict (G), (IB), (LA), (S) with closed sections for every model, (C), T1 ∈ C_L, on M_U.
Endorsers (K3 §1, L4 §1): 𝒩_k = {ν ∈ ba₊(M) : ν(M) = 1, ν(δ) ≥ 0 for every relevant world-k comparison δ};
𝒩_k ≠ ∅ iff (NC) at world k (K3.1(a)). Yosida–Hewitt: ν = ρμ + π, π purely finitely additive. ν*_k is a
maximal-support endorser and Λ_k := {ρ*_k = 0} ∩ M its (canonical) blind set (K3.1(c)); V_k := M ∖ Λ_k.

**Edge models.** An *edge model* (for {i, j}) is a model equal to P_i on Q_k and accepting N₊; it is determined by
its world-i error set c ⊆ R_ij, and its world-j error set is R_ij ∖ c. Every selected C_q with q in the closed edge
[e_i, e_j] is an edge model (competitiveness on supp q ⊆ {i, j} and strict (G); Lemma Q34). For densities ρ_i, ρ_j
on R_ij and θ ∈ [0, 1] put

  e_θ := θρ_i − (1 − θ)ρ_j   (on R_ij),

so that θψ_i(X) + (1 − θ)ψ_j(X) = const + ∫_{c_X} e_θ dμ for edge models X. An edge model is **θ-Bayes** (for
(ρ_i, ρ_j)) if c ⊆ {e_θ ≤ 0} and R_ij ∖ c ⊆ {e_θ ≥ 0} a.e. Its two extreme versions are E^{θ,−} (world-i errors
L_θ := {e_θ < 0}) and E^{θ,+} (world-i errors U_θ := {e_θ ≤ 0}); in M1's notation E^{θ,−} = T^i_θ, E^{θ,+} = T^j_θ.
Note: e_θ is nondecreasing in θ, and e_θ = e_θ′ for θ ≠ θ′ only on the **joint blind set** {ρ_i = ρ_j = 0}.

---

## 0. Outcome

**The "no blind targets" theorem is TRUE and PROVED, in a stronger form than asked and by a different mechanism
than L3.4: it needs no closed sections. It kills the T1-shadow (Q_M1 has answer NO) and every exact one-sided
shadow. But the edge exchange M1.7 itself does NOT fail in general, so NO COVER does not follow: the exchange
survives as a *visible* exchange or as an exchange *internal to one world's blind set*. I prove NO COVER for the
classes (a)–(d) of Theorem N2.7 and hand over the escaping configuration (§6): internal exchanges, whose two-world
form is exactly L2's edge picture.**

1. **Theorem N2.1 (Pareto off the carriers; PROVED).** Let C ∈ C_L be competitive on S ⊆ Ω and let ν_k ∈ 𝒩_k
   (k ∈ S) be **any** endorsers, with countably additive (CA) densities ρ_k. Then C is weakly Pareto for the CA
   assessments ψ_k = ∫_{E_k(·)∩M} ρ_k, and hence C is c-Bayes at some weight w ∈ Δ_S, ties free. The purely finitely
   additive parts never protect C: competitiveness can always be tested by partial trades **off their carriers**.
   On an edge: every interior edge-selected model (indeed every edge model in C_L competitive on {i, j}) is
   θ-Bayes for (ρ_i, ρ_j), for some θ ∈ [0, 1].
2. **Corollary N2.2 (no blind targets; PROVED).** If such a C is world-i-correct on a non-null part of
   {ρ_i = 0 < ρ_j} ∩ R_ij, then **all** of C's world-i errors on R_ij lie in {ρ_i = 0}. So no relevant comparison
   out of C has a target that is CA-blind at i and CA-visible at j together with a CA-visible source. A blind target
   forces a blind source. (In two worlds next to an additive world this is the structure behind K3.8; here no
   additivity, nestedness or closedness is used.)
3. **Theorem N2.3 (every extreme edge Bayes model is selected; PROVED from M1.3).** Under (H_U), if worlds i, j have
   endorsers whose CA parts have a null joint blind set on R_ij, then for **every** θ ∈ [0, 1] both E^{θ,−} and
   E^{θ,+} lie in C_L (hence are coherent). In particular X_ij (world-i errors = Λ_i ∩ R_ij) is selected, so every
   blind set that its edge partner sees is the world-i error set of a coherent "between" model D_K,
   K ∩ [e_i, e_j] ≠ ∅, K ⊆ co(K′ ∪ [e_i, e_j]). This is K3.7(β′)'s rigidity at the ranking level, for every world
   at once, without (γ), (B1) or CA endorsers.
4. **Theorem N2.4 (anatomy of the edge exchange; PROVED from M1.7).** The dominator C of M1.7 on {i, j} is θ*-Bayes,
   and exactly one of three things happens:
   - **(vis)** θ* ∈ (0, 1): F_i ⊆ V_i ∪ (Λ_i ∩ Λ_j) with θ*ρ_i ≥ (1−θ*)ρ_j on F_i, and F_j ⊆ V_j ∪ (Λ_i ∩ Λ_j) with
     the reverse inequality: each target carries CA weight of its own world comparable to the partner's;
   - **(int_i)** θ* = 1: E_i(C) ∩ R_ij ⊆ Λ_i, so source and target of world i's trade are both i-blind;
   - **(int_j)** θ* = 0: the mirror statement.
5. **Theorem N2.5 (edge-Bayes targets; PROVED).** If c_T^{ij} is θ₀-Bayes, the exchange lives on the tie set
   Z_{θ₀} = {e_{θ₀} = 0} ∩ R_ij (joint blind set included). This generalises M1.9 and M1.9′(b) from CA endorsers to
   arbitrary endorsers. It applies whenever p* lies on the closed edge [e_i, e_j]. Separately (Lemma N2.5′), T1 is
   always (i,j)-Bayes on E_k(T1) ∩ R_ij = J_i ∪ J_j; this is M1 §4.3 without additivity.
6. **Corollary N2.6 (Q_M1: NO; PROVED).** No cover has, on any edge, Λ_i ∩ R_ij = E_i(T1) ∩ R_ij together with
   Λ_j ∩ E_i(T1) ∩ R_ij null: X_ij would be Y_k, which is selected but incoherent. The T1-shadow (all three worlds
   exactly shadow-blind) is the case where this holds on every edge. M1's requirement (W2) cannot be met.
7. **Theorem N2.7 (no cover: what is now excluded, with hypotheses; §5).** It also says exactly which hypotheses are
   removed from M1.5(b), M1.8, M1.9, M1.9′, K3.7(β′) and L4.7, and that (NC) at the two worlds of an edge (or M2's
   (RL) partners) is still needed.
8. **What escapes (§6).**
   - The theorem asked for ("the edge exchange cannot hold") is false as stated: exchanges of type (vis) occur in
     every strictly positive field, and those are excluded only globally, by M0closed(a).
   - The blind-target blueprint is dead (N2.2).
   - The surviving blueprint is the **internal exchange** (int_i). Its two-world form exists: it is L2's full system
     (blind segment c_a = E₁(C_a), path inside c_a up to C_a, then containing it).
   - For T1 it is pinned to the vertex configuration (V), with items (V1)–(V6) of §6 PROVED. The two open sub-cases
     are (V0) (world 1 totally CA-blind) and (V+) (world 1 does not refine its CA veto; if it does, L3.4 kills it).
   - The multi-blind interior configurations must have all exchanges of type (vis) or (int), and every seen blind
     set rigid (N2.3).

| | Statement | Label |
|---|---|---|
| N2.1 | Pareto off the carriers: every C ∈ C_L competitive on S is c-Bayes at some w ∈ Δ_S, for any endorsers | PROVED |
| N2.1′ | the same with M2's forced endorser at world 1 next to (RL) partners | PROVED |
| N2.2 | no blind target with a visible source out of an {i,j}-competitive member of C_L | PROVED |
| N2.2′ | edge selections cross only inside tie sets of the CA edge field ((Nest_e) for tie-free endorsers) | PROVED |
| N2.3 | all extreme edge θ-Bayes models selected (null joint blindness); seen blind sets rigid | PROVED (uses M1.3, unrefereed) |
| N2.4 | the M1.7 exchange is (vis), (int_i) or (int_j) | PROVED (uses M1.7, unrefereed) |
| N2.5, N2.5′ | edge-Bayes targets: exchange on ties; T1 (i,j)-Bayes on E_k(T1) ∩ R_ij | PROVED |
| N2.6 | Q_M1 = NO; one-sided exact shadows impossible; L4.7 at ranking level | PROVED (uses M1.3, M1.6(b), unrefereed) |
| N2.7 | no-cover assembly, classes (a)–(d) | PROVED, inputs as listed in §5 |
| §6 | the escaping configuration (V) with (V1)–(V6); sub-cases (V0), (V+) | (V1)–(V6) PROVED; existence open |
| Q_N2 | (V0): a full two-world system whose world 1 has no CA endorser at all (Λ = M)? | open |

NUMERICS (`n2py/r20/n2_checks.out`):
- (A) On 4000 random cell models (blind cells at i, at j and joint, random and near-threshold sets), weak Pareto
  (tested by LP) and the threshold property of N2.1 agree in 4000/4000 cases (1930 weakly Pareto).
- (B) For the shadow on edge (1,2), X_12 coincides with Y_3 on the whole sample, and it fails midpoint convexity on
  435/41892, 257/40010, 232/38461 sampled pairs at (ε, s) = (0.1, 0.9), (0.3, 0.9), (0.6, 0.5). T1 fails on 0 pairs.

---

## 1. Pareto off the carriers

**Theorem N2.1 (PROVED).** Let C ∈ C_L be competitive on S ⊆ Ω, S ≠ ∅ (no other axiom is used).
Let ν_k = ρ_kμ + π_k ∈ 𝒩_k for k ∈ S, and ψ_k(X) := ∫_{E_k(X)∩M} ρ_k dμ.
- **(a)** There is no measurable W ⊆ M with ψ_k(C △ W) < ψ_k(C) for every k ∈ S.
- **(b)** There is w ∈ Δ_S with Σ_{k∈S} w_k χ_k ρ_k ≥ 0 a.e. on M, where χ_k(g) := +1 if C is correct at world k at g
  and −1 otherwise. That is, C's advice is pointwise optimal for the field w·c, ties free.
- **(c) (edge form.)** If S = {i, j} and C is an edge model, then C is θ-Bayes for (ρ_i, ρ_j) with θ = w_i.

*Proof.*
- **(a), the carrier.** Suppose W violates (a), with margin 3η > 0 at every k ∈ S. π := Σ_{k∈S} π_k is purely
  finitely additive (K3.1(c), fact (F2)). By K3.1(b) Step 1, for every ε > 0 there is a measurable E ⊆ M with
  μ(E) < ε and π(M ∖ E) < ε. By absolute continuity, choose ε so small that also ρ_k(E) < η for all k ∈ S, and
  ε ≤ η. Put W′ := W ∖ E and X := C △ W′.
- **(a), X is a legal test.** X ⊆ U is measurable, so X ∈ M_U. C is coherent, hence regular, and W′ ⊆ M, so X is
  regular. So every comparison C ⪯_k X is relevant.
- **(a), every endorser strictly prefers X.** For k ∈ S:
  - ψ_k(X) − ψ_k(C) = ∫_{W′} χ_k ρ_k dμ ≤ ∫_W χ_k ρ_k + ρ_k(E) < −3η + η = −2η;
  - |π_k(E_k(X)) − π_k(E_k(C))| ≤ π_k(W′) ≤ π(M ∖ E) < η.

  So ν_k(E_k(X)) − ν_k(E_k(C)) < −η < 0.
- **(a), contradiction.** Competitiveness on S gives k ∈ S with C ⪯_k X. That comparison is relevant, so ν_k
  endorses it: ν_k(E_k(X)) ≥ ν_k(E_k(C)). Contradiction.
- **(b).** The map W ↦ v(W) := (∫_W χ_k ρ_k dμ)_{k∈S} is a non-atomic finite vector measure on M, so its range 𝒱 is
  convex and compact (Lyapunov). 0 ∈ 𝒱, and by (a), 𝒱 misses the open negative orthant. Separation gives w ≥ 0,
  w ≠ 0 (normalise to w ∈ Δ_S) with w·v ≥ 0 on 𝒱. Taking W = {Σ w_kχ_kρ_k < 0} gives the claim.
- **(c).** On Q_k, C is correct at both i and j, so the condition holds there. On R_ij, χ_j = −χ_i. Where C is
  i-correct the condition reads θρ_i − (1−θ)ρ_j ≥ 0, i.e. e_θ ≥ 0. Where C is i-wrong it reads e_θ ≤ 0. ∎

*An elementary proof of (c)* (no Lyapunov). Put a(θ) := μ(c ∩ {e_θ > 0}), which is nondecreasing with a(0) = 0, and
b(θ) := μ((R_ij ∖ c) ∩ {e_θ < 0}), which is nonincreasing with b(1) = 0. Let θ_a := sup{a = 0} and
θ_b := inf{b = 0}. Since {e_θ > 0} and {e_θ < 0} are monotone unions, a(θ_a) = 0 = b(θ_b).
- If θ_b ≤ θ_a, any θ ∈ [θ_b, θ_a] works.
- Otherwise pick θ_a < θ′ < θ″ < θ_b. The sets P := c ∩ {e_θ′ > 0} and Q := (R_ij ∖ c) ∩ {e_θ″ < 0} are non-null.
  - On P: ρ_i > 0 and ρ_j < αρ_i, with α = θ′/(1−θ′).
  - On Q: ρ_j > 0 and ρ_i < βρ_j, with β = (1−θ″)/θ″, and αβ < 1.
  - Take P₀ ⊆ P with ρ_i(P₀) = u > 0 small, and Q₀ ⊆ Q with ρ_j(Q₀) = αu.
  - Then ρ_j(P₀) < αu = ρ_j(Q₀) and ρ_i(Q₀) < αβu < u = ρ_i(P₀). Moving P₀ out of and Q₀ into C's world-i error set
    improves both CA assessments strictly, against (a).

NUMERICS (A) confirms the equivalence on cell models.

**Remark N2.1′ (M2's setting; PROVED).** Let world 1 have only an M2 forced endorser φ ∈ 𝒩(𝔉𝔏), and let worlds j ≠ 1
satisfy (RL) (M2 §1), with ν_j := ρ_jμ. Then (a)–(c) hold for C = C_q with supp q = S ∋ 1, and for C = T1 with
S = Ω.
- In the proof of (a): ψ_j(X) < ψ_j(C) for every j ∈ S ∖ {1}. So (RL-2) gives C ⋠_j X, and competitiveness gives
  C ⪯₁ X.
- (C, X) is then a forced pair (M2 §1), so φ endorses it. The carrier argument at world 1 is unchanged.

So every result below that uses only N2.1 at edges {1, j} holds in M2's setting, with Λ♮ in place of Λ₁.

**Corollary N2.2 (no blind targets; PROVED).** Let C ∈ C_L be an edge model competitive on {i, j}, and let ν_i, ν_j
be endorsers. Then:
- **(a)** if (R_ij ∖ E_i(C)) ∩ {ρ_i = 0 < ρ_j} is non-null, then E_i(C) ∩ R_ij ⊆ {ρ_i = 0};
- **(a′)** equivalently: if C has a non-null CA-visible world-i error (E_i(C) ∩ {ρ_i > 0}), then
  E_i(C) ⊇ {ρ_i = 0 < ρ_j} ∩ R_ij;
- **(b)** consequently, for every relevant comparison C ⪯_i X with X an edge model, whose target
  (E_i(X) ∖ E_i(C)) meets {ρ_i = 0 < ρ_j} non-nully, the source (E_i(C) ∖ E_i(X)) lies in {ρ_i = 0};
- **(c)** the mirror statements hold at world j.

*Proof.* By N2.1(c), C is θ-Bayes. On the given non-null set, e_θ = −(1−θ)ρ_j ≥ 0 with ρ_j > 0, so θ = 1. Then
E_i(C) ∩ R_ij ⊆ {e₁ ≤ 0} = {ρ_i = 0}. (a′) is the contrapositive, and (b) follows. ∎

*Why the boundary is not needed.* The brief expected L3.4's mechanism (closed choice at the boundary of Δ).
- For a blind target the full trade can be carried by π_i, which lives on carriers of arbitrarily small measure.
- A *partial* trade off those carriers is also a competitor of C. Only CA parts see it, and both worlds strictly
  prefer it.
- So the obstruction is competitiveness itself. L3.4's closed-choice mechanism is needed only for *visible* sources,
  i.e. for vetoes (§6, (V+)).

**Corollary N2.2′ (crossings live on ties; PROVED).** Let C, C′ be edge models competitive on {i, j} in C_L, θ-Bayes
and θ′-Bayes for the same endorser pair.
- If θ < θ′: E_i(C′) ∩ R_ij ⊆ {e_θ′ ≤ 0} ⊆ L_θ ∪ {ρ_i = ρ_j = 0} ⊆ E_i(C) ∪ {ρ_i = ρ_j = 0}.
- If θ = θ′: they differ only on Z_θ := {e_θ = 0} ∩ R_ij.

So two members of an edge selection cross only inside the tie sets Z_θ of the CA edge field (the joint blind set and
the blind sets {ρ_i = 0} = Z₁, {ρ_j = 0} = Z₀ included). Hence:
- **(Nest_e)** holds on {i, j} whenever some endorser pair has ρ_i, ρ_j > 0 a.e. on R_ij and μ({ρ_i = rρ_j} ∩ R_ij) = 0
  for every r > 0;
- this extends S2.0(c) (additive worlds) and S2.4 (leading charges) to arbitrary worlds with endorsers.

---

## 2. Every extreme edge Bayes model is selected

**Theorem N2.3 (PROVED; inputs M1.3 (face KKM with strict (G)), N2.1).** Assume (H_U). Let ν_i ∈ 𝒩_i, ν_j ∈ 𝒩_j with
μ({ρ_i = ρ_j = 0} ∩ R_ij) = 0. Then for every θ ∈ [0, 1], E^{θ,−} and E^{θ,+} belong to C_L.

*Proof.* Let X be E^{θ,−} or E^{θ,+}. X is an edge model, regular, and in M_U. Its world-i error set A is L_θ or U_θ.
M1.3 with I = {i, j} gives p ∈ [e_i, e_j] and C := C_p ∈ C_L with C ⪯_i X and C ⪯_j X. Write c := E_i(C) ∩ R_ij.
- **Vertices.** If p = e_i, then C = P_i and c = ∅. If A were non-null, X ≺_j P_i by strict (G); so A is null and
  X = P_i. If p = e_j, then c = R_ij, and similarly A = R_ij and X = P_j.
- **Interior p.** C is competitive on {i, j}, so by N2.1(c) it is θ′-Bayes for some θ′. Recall that e_θ′ − e_θ has the
  sign of θ′ − θ off the joint blind set, which is null.
  - X = E^{θ,−}, θ′ ≤ θ: c ⊇ {e_θ′ < 0} ⊇ {e_θ < 0} = A.
  - X = E^{θ,−}, θ′ > θ: c ⊆ {e_θ′ ≤ 0} ⊆ {e_θ < 0} = A (mod null).
  - X = E^{θ,+}, θ′ < θ: c ⊇ {e_θ′ < 0} ⊇ {e_θ ≤ 0} = A (mod null).
  - X = E^{θ,+}, θ′ ≥ θ: c ⊆ {e_θ′ ≤ 0} ⊆ {e_θ ≤ 0} = A.
- **Conclusion.** So c ⊇ A or c ⊆ A. In the first case C ⪯_i X and strict (G) at i give c = A. In the second,
  C ⪯_j X and strict (G) at j give c = A. Both are edge models, so X = C ∈ C_L. ∎

**Corollary N2.3′ (PROVED).** Let ν*_i, ν*_j be maximal-support endorsers with Λ_i ∩ Λ_j ∩ R_ij null.
- **(a)** X_ij := E^{1,+} (world-i errors Λ_i ∩ R_ij) and X_ji := E^{0,−} (world-i errors V_j ∩ R_ij, i.e. world-j
  errors Λ_j ∩ R_ij) are in C_L.
- **(b) Rigidity.** Λ_i ∩ R_ij = E_i(D_K) ∩ R_ij for a coherent D_K with K ∩ [e_i, e_j] ≠ ∅ and
  K ⊆ co(K′ ∪ [e_i, e_j]). This is K3.7′, since X_ij is coherent and equals P_i on Q_k.
- **(c) Upgrades of M1.5.** This is M1.5(b) without CA endorsers, and M1.5(a) on edges (tie-broken edge Bayes models
  selected) without CA endorsers. Null joint blindness on R_ij is the replacing hypothesis.
- **(d)** Every extreme edge Bayes model of the maximal CA edge field is coherent, at every θ ∈ [0, 1], boundary values
  included. This is an edge form of (γ₀) for both tie-breakings, obtained at the ranking level.

*Proof.* (a) and (d) are N2.3, with {ρ*_i = 0} = Λ_i and E^{0,−} having world-i errors {ρ_j > 0}. (b) is (a) together
with H12_referee §1.1 (coherent models of M_U are the D_K with K ⊇ K′) and Lemma K3.7′. ∎

---

## 3. The edge exchange, and edge-Bayes targets

**Theorem N2.4 (anatomy of the edge exchange; PROVED from M1.7, N2.1).** Assume (H_U) and endorsers at i, j. Let
C ∈ C_L and F_i = c_T^{ij} ∖ E_i(C), F_j = E_i(C) ∩ R_ij ∖ c_T^{ij} (both non-null) be as in M1.7.
- C = C_p with p in the open edge (M1.7's proof: p = e_i or e_j contradicts strict (G) at j or i), so N2.1(c) makes
  C θ*-Bayes.
- F_i ⊆ R_ij ∖ E_i(C) ⊆ {e_θ* ≥ 0} and F_j ⊆ E_i(C) ⊆ {e_θ* ≤ 0}. Reading this at θ* ∈ (0,1), at θ* = 1 and at θ* = 0
  gives exactly (vis), (int_i) and (int_j) of §0.4.
- In (vis), on F_i ∩ {ρ_i = 0} one has (1−θ*)ρ_j ≤ 0, so ρ_j = 0. ∎

So the M1.7 inequalities ν_i(F_i) ≥ ν_i(F_j), ν_j(F_j) ≥ ν_j(F_i) are carried as follows:
- in (vis), by CA weight of world i on its own target F_i, of the size (1−θ*)/θ* · ρ_j (this is the "positive
  countably additive weight comparable to the trade on the target" the brief asked for), except on jointly blind
  pieces;
- in (int_i), at world i by π_i alone, but with a blind source.

**Theorem N2.5 (edge-Bayes targets; PROVED from M1.7, N2.1).** Assume (H_U), endorsers at i, j, and that c_T^{ij} is
θ₀-Bayes for (ρ_i, ρ_j). Let θ* be as in N2.4.
- If θ* < θ₀, then F_i ⊆ {ρ_i = ρ_j = 0}.
- If θ* > θ₀, then F_j ⊆ {ρ_i = ρ_j = 0}.
- If θ* = θ₀, then F_i ∪ F_j ⊆ Z_{θ₀}.

Hence:
- **(a) (M1.9 for arbitrary endorsers.)** If moreover Z_{θ₀} is null (joint blind set included), (H_U) is
  contradictory.
- **(b) (M1.9′(b) for arbitrary endorsers.)** If the joint blind set on R_ij is null, the two-sided tie shell of
  M1.9′(b) is forced, by M1.9′(b)'s facet-plane argument (M1.6(a)), for f.a. endorsers:
  - Z_{θ₀} ∩ E_i(T1) and Z_{θ₀} ∖ E_i(T1) are non-null near every point of every R_ij-arc of some facet;
  - the input "T^i_{θ*}, T^j_{θ*} coherent" is now N2.3 instead of M1.5(a).
- **(c) When the hypothesis holds.** If p* (L4.1.3) lies on the closed edge [e_i, e_j], then c_T^{ij} is θ₀-Bayes
  with θ₀ = p*_i/(p*_i + p*_j).
  - On R_ij, p*·c = σ_i e_{θ₀} (since p*_k = 0), and admissibility reads E_i(T1) ⊆ {e_{θ₀} ≤ 0},
    R_ij ∖ E_i(T1) ⊆ {e_{θ₀} ≥ 0}.
  - At p* = e_i (θ₀ = 1): the exchanges on both edges at e_i are internal to Λ_i, or have F_i jointly blind.

*Proof.*
- c_T is θ₀-Bayes and E_i(C) ∩ R_ij is θ*-Bayes.
- If θ* < θ₀: on F_i (in c_T, not in E_i(C)) one has e_θ₀ ≤ 0 ≤ e_θ*. Since e_θ* ≤ e_θ₀, both vanish, and θ* ≠ θ₀
  forces ρ_i + ρ_j = 0. The case θ* > θ₀ is the mirror on F_j. If θ* = θ₀, both F's lie where e_θ₀ = 0.
- (a): one of F_i, F_j is null, against strict (G) (M1.3).
- (b): N2.3 makes T^i_{θ₀} = E^{θ₀,−} and T^j_{θ₀} = E^{θ₀,+} selected, hence coherent. M1.9′(b)'s argument then runs
  verbatim.
- (c) is the computation stated. ∎

**Lemma N2.5′ (T1 on the joint error set of the third world; PROVED from Lemma IC, N2.1).** Assume (H_U) and
endorsers at i, j. There is θ₀ ∈ [0, 1] with J_j ⊆ {e_θ₀ ≤ 0} and J_i ⊆ {e_θ₀ ≥ 0}. That is, T1 restricted to
E_k(T1) ∩ R_ij = J_i ∪ J_j is (i, j)-Bayes.

*Proof.*
- T1 is competitive on Ω (Lemma IC: R11, refereed R13). T1 errs at k on J_i ∪ J_j. So for W ⊆ J_i ∪ J_j non-null,
  T1 △ W ≺_k T1 by strict (G), and competitiveness passes to {i, j}.
- Run N2.1(a)–(b) with S = {i, j} and W restricted to J_i ∪ J_j. On that set T1's world-i errors are J_j. ∎

This is M1 §4.3's "(PROVED) with worlds 2, 3 additive", now for arbitrary endorsers.

---

## 4. The shadow is impossible (Q_M1: NO)

**Corollary N2.6 (PROVED from N2.3, M1.6(b)).** Assume (H_U) and (NC) at worlds i and j. Suppose
Λ_i ∩ R_ij = E_i(T1) ∩ R_ij (mod null) and Λ_j ∩ E_i(T1) ∩ R_ij is null. Then there is a contradiction.

*Proof.*
- The joint blind set on R_ij is Λ_i ∩ Λ_j ∩ R_ij = Λ_j ∩ c_T^{ij}, which is null.
- N2.3′(a) puts X_ij ∈ C_L.
- X_ij has world-i errors c_T^{ij} on R_ij and equals P_i on Q_k, so X_ij = Y_k. This is incoherent (M1.6(b);
  NUMERICS (B)), whereas members of C_L are coherent. ∎

Consequences (all PROVED, with the same inputs):
- **(a) Q_M1 has answer NO.** If the maximal endorser field is the T1-shadow (Λ_k = E_k(T1) ∩ M for every k), then on
  R_ij one has Λ_j ∩ E_i(T1) = E_j(T1) ∩ E_i(T1) ∩ R_ij = ∅, since on R_ij a model errs at exactly one of i, j.
  - So no ranking with (H_U) has the shadow as its maximal field.
  - Equivalently (M1.1(b)), no cover has T1 admissible at all three vertices.
  - M1 §4.1's requirement (W2) is unrealisable: it asks for an exchange whose targets are blind at i and visible at
    j, which N2.2 forbids.
- **(b) M1.8 without CA endorsers.** M1.8 needed a CA endorser of world i. Now, with any endorsers: in a cover, world i
  is never blind exactly on E_i(T1) ∩ R_ij while world j sees E_i(T1) ∩ R_ij.
- **(c) L4.7 at the ranking level.** Under (B1) (ρ₂ > 0), Λ₁ = E₁(T1) ∩ M gives X₁₂ = Y₃, a contradiction. No (γ) or
  (β′) is used.
- **(d) M1.11 at the ranking level.** An exact shadow-blind world next to a partner that sees its T1-errors on the
  common edge region is impossible.

---

## 5. The no-cover assembly

**Theorem N2.7 (PROVED; inputs and their status listed below).** Assume (H_U) on M_U and (NC) at every world (or, in
(d), M2.6's setting). Let Λ_k be the maximal blind sets and c* the maximal CA field. There is **no cover** in any of
the following cases.
- **(a) One-sided exact shadow.** On some edge, Λ_i ∩ R_ij = E_i(T1) ∩ R_ij and Λ_j ∩ E_i(T1) ∩ R_ij is null (N2.6).
  This includes the T1-shadow and every field of M1.1(a).
- **(b) Tie-free edge-Bayes target.** On some edge, c_T^{ij} is θ-Bayes for (ρ*_i, ρ*_j) with Z_θ null (N2.5(a)).
  In particular this applies when p* lies on the closed edge [e_i, e_j] and the edge field has no ties at θ₀ there.
- **(c) Boundary target weight without a tie shell.** p* lies in the open edge (e_i, e_j), the joint blind set on R_ij
  is null, and Z_{θ₀} ∩ R_ij fails to accumulate (on both sides of T1's boundary) along the R_ij-arcs of every facet
  (N2.5(b), N2.5(c)).
- **(d) The vertex configuration with a refined veto.**
  - *Setting.* Worlds 2, 3 add up and world 1 satisfies (NC) (or the M2.6 setting), so the configuration is (V) of
    L4 / L4_referee. Assume V₁ is non-null, and that world 1 refines its CA veto Φ₁(X) := ∫_{X∩V₁} ρ*₁ dμ, i.e.
    Φ₁(X) < Φ₁(Y) ⇒ X ≺₁ Y.
  - *Proof.*
    - M1.2 gives V₁ ⊆ {g₁ < 0} ∖ cl D_{T1} ⊆ R₁₂ ∪ R₁₃ (every mixed g with g₁ < 0 lies in R₁₂ or R₁₃). So Φ₁ is a
      veto (it charges only world-1-wrong acceptances, and Φ₁(P₁) = 0), and V₁ ∩ R_{1j} is non-null for some j.
    - L3.4's hypothesis (V) holds: Φ₁(P_j) = ρ*₁(V₁ ∩ R_{1j}) > 0.
    - L3.4's (Imp) holds by N2.2. A selected edge model C_q on [e₁, e_j] with Φ₁(C_q) > 0 has a visible world-1
      error, so by N2.2(a′) it errs on all of Λ₁ ∩ R_{1j}, which is non-null by M1.2 (Λ₁ ⊇ M ∩ {g₁ > 0}). Fixing a
      non-null piece of it is Φ₁-neutral and strictly better at world 1 by strict (G).
    - L3.4 (refereed CORRECT) then forbids closed choice on [e₁, e_j].

Also excluded, by earlier results (for the record):
- non-degenerate fixed points (L4.1.4 + M0closed(a); L4_referee);
- one blind world with p* ∈ Δ° (L4.9 + L4_referee Prop. R, with case (II) CHECKED; L1, modulo L1.7 and L1.C,
  CHECKED);
- the minimal vertex instance (L4.7, now N2.6(c)).

**Inputs and status.**
- N2.1, N2.2, N2.2′ use only competitiveness, strict (G), relevance and K3.1(b) (refereed CORRECT).
- N2.3–N2.6 use M1.3, M1.6 and M1.7 (M1, **unrefereed**; a referee is checking M1).
- (d) uses L4 (refereed, with Prop. R), M1.2 (unrefereed) and L3.4 (refereed CORRECT).

**Which hypotheses are removed.**
- **CA endorsers / (ZER)** are removed from:
  - M1.5(b), replaced by null joint blindness on R_ij;
  - M1.5(a) on edges;
  - M1.8, replaced by partner visibility on E_i(T1) ∩ R_ij;
  - M1.9, M1.9′(b).
- **(γ)/(B1)** are removed from the rigidity K3.7(β′) (N2.3′(b)), which now holds for every world whose blind set the
  partner sees.
- **Additivity of worlds 2, 3** is removed from M1 §4.3 (N2.5′).

**Which hypotheses are still needed.**
- (NC) at the two worlds of the edge, or the M2 setting (an (RL) partner with M2's forced endorser at world 1, N2.1′).
  Strongly (M1) worlds next to non-(RL) partners remain outside.
- For the global conclusion, the M0closed-type field rigidity for degenerate fields. The edge results never exclude
  (vis) exchanges, because strictly positive fields have them.

---

## 6. What escapes: the precise configuration (positive blueprint)

**Is "the edge exchange cannot hold" true?** No, not as stated.
- In any cover attempt with strictly positive fields, exchanges of type (vis) exist. T1 is not edge-Bayes on R_ij for
  p* ∈ Δ°, and the third world's weight p*_k tilts T1 toward j on Q_i and toward i on Q_j.
- So the edge alone cannot decide. Those fields are excluded globally (M0closed(a)).
- What *is* true is N2.2: no blind target with a visible source.

**The blind-target blueprint is dead.** M1 §4.2–§5 proposed a closed-section tilt whose purely finitely additive end
lies in its own T1-error set and is traded against visible correctness. N2.2 forbids this for every ranking with
competitive selection, closed or not.
- M1 §5's "first test for a yes" asked for a two-world world 1 whose purely finitely additive end is traded against
  visible correctness. Next to any partner with an endorser that sees the end, N2.2 makes this impossible. (A blind
  end traded only against blind sources is possible: that is L2.)
- K3.3's tilt escapes N2.2 only because it is totally blind (Λ = M), so its sources are blind too.

**The surviving mechanism: internal exchanges.** In (int_i), world i trades errors **inside its own blind set**
against errors inside its own blind set. Every endorser may vanish there entirely, π included, as in L2.
- **Its two-world form exists:** L2.1/L2.4 is a full two-world system (every axiom, closed sections for every model).
  - World 1's blind set is c_a = E₁(C_a), with C_a selected (compare N2.3′(a)).
  - The path runs inside c_a for b < a (θ = 1 phase) and contains c_a for b > a (θ < 1 phase), exactly as N2.2
    dictates.
  - Its comparisons C_b ⪯₁ X with E₁(X) ⊆ c_a crossing c_b are internal exchanges (accepted iff the tail condition
    holds).
- **This is the positive blueprint to hand over.**

**For T1 the surviving one-blind configuration is (V), now pinned as follows.** Setting: worlds 2, 3 add up, world 1
satisfies (NC) (or M2.6).
- **(V1)** p* = e₁, A(c*) = {e₁}, Λ₁ ⊋ E₁(T1) ∩ M, Λ₁ ⊇ M ∩ {g₁ > 0}, and V₁ ⊆ {g₁ < 0} ∖ cl D_{T1}. Source: L4,
  L4_referee, M1.2.
- **(V2)** X₁₂ = D_{K₁} and X₁₃ = D_{K₀} are **selected** (N2.3′, since ρ₂, ρ₃ > 0), with e₂ ∈ K₁ and e₃ ∈ K₀ (M1.2).
  This is new: M1.5(b) needed a CA endorser of world 1.
- **(V3)** Every interior model of the selection on [e₁, e₂] has world-1 error set c ⊆ Λ₁ ∩ R₁₂ (θ = 1 phase) or
  c ⊇ Λ₁ ∩ R₁₂ (θ < 1 phase, a θ-threshold set of ρ*₁/ρ₂ on V₁ ∩ R₁₂) (N2.2).
  - The two phases are glued at D_{K₁}. By N2.3's proof applied to X₁₂: S₁(X₁₂) = {0} ∪ {c ⊊ Λ₁^R} ∪ {c = Λ₁^R} and
    S₂(X₁₂) = {c ⊋ Λ₁^R} ∪ {c = Λ₁^R} ∪ {1}, both closed.
  - The same holds on [e₁, e₃].
- **(V4)** The M1.7 exchange on [e₁, e_j] is **internal** (int₁): its dominator has c ⊊ Λ₁ ∩ R_{1j}, crossing
  E₁(T1) ∩ R_{1j} inside Λ₁ (N2.4, N2.5(c) with θ₀ = 1).
- **(V5)** T1 is (2, 3)-Bayes on E₁(T1) ∩ R₂₃ = J₂ ∪ J₃ (N2.5′).
- **(V6)** Either V₁ is null (**(V0)**: world 1 has no CA endorsement at all, the K3.3/M1.1(c) pattern), or world 1
  does **not** refine its CA veto Φ₁ (**(V+)**; N2.7(d)). If worlds 2, 3 have integrable CA endorsers (e.g. (RL)),
  world 1 is moreover not (Loc) (H1.2), so by K3.7 it is (M1) or lies in (N).

**The precise handover.**
- **(V+)** is "L2 on each edge at e₁" (a description, not a theorem). On [e₁, e_j], world 1 must look like L2's
  world 1, with C_a ↔ D_{K₁} (resp. D_{K₀}) and c_a ↔ Λ₁ ∩ R_{1j}.
  - L2's world 1 does not refine its veto λ|_{d_a} (PROVED). L2 has closed sections. The veto is paid at e₂
    (λ(d_a) > 0). (Imp) holds by N2.2: a selected C_b with visible errors contains c_a, and fixing a piece of c_a is
    neutral for the veto. So L3.4 forbids refinement.
  - Tail dominance trades blind sources for visible targets, which is exactly the direction N2.2 allows.
- **What is missing for a cover:**
  - (i) a three-world lift with the T1-specific crossing exchange inside Λ₁ (L2 §7, Q_L2);
  - (ii) next to integrable partners, a non-(Loc) version of L2. This contradicts Conjecture L2.C in two worlds next
    to an additive world, so the partners would need endorsers with nonzero purely finitely additive parts.
- **(V0)** reduces to a two-world question on which N2 says nothing (all its edge models are θ = 1 models).
  - **Q_N2.** Is there a full two-world system on M_U (every axiom, closed sections for every model), next to an
    additive world, in which world 1 has **no** countably additive endorsing part at all (Λ = M, a_∞ = 1 in K3.8's
    notation)?
  - K3.3 has this except for closed sections. L2 reaches every a < 1, not a = 1.
- **Multi-blind configurations** (L1.D and the joint blindness of L4.3) must have every exchange of type (vis) or (int)
  on every edge, and every seen blind set rigid (N2.3′(b)). N2.3′ supplies at the ranking level, for all worlds
  simultaneously, the rigid "between" models that L1 §6.3 said a simultaneous induction would need. I did not run
  that induction.

---

## 7. Dependencies, files, and what a referee should check

**Used.**
- K3.1(b) Step 1 and (F2) (purely finitely additive carriers; refereed CORRECT).
- Lyapunov.
- Lemma IC (R11/R13).
- M1.3, M1.6(a)(b), M1.7, M1.9′(b)'s facet argument, M1.2 (M1, unrefereed).
- Lemma K3.7′, H12_referee §1.1.
- L4.1.3 (admissibility), L4, L4_referee Prop. R; L1 (for the record only).
- L3.4 (refereed CORRECT).
- M2 §1 definitions (for N2.1′).
- K3.7, H1.2 (for (V6) only).
- L2.1/L2.4 (refereed CORRECT; for §6).

**Not used.** Closed sections in N2.1–N2.2′ (only competitiveness); (C) anywhere except through C_L membership; (IB);
any (γ)-type field property in N2.1–N2.6; M0closed's proof.

**Referee priorities.**
1. N2.1(a): the single carrier for Σπ_k, and that the off-carrier X is a relevant competitor.
2. N2.3: the four inclusions, and the use of null joint blindness.
3. N2.6(a): the identification X_ij = Y_k, which relies on M1.6(b).
4. N2.7(d): the verification of L3.4's (V) and (Imp) for Φ₁ via M1.2 and N2.2.

**Files** (`n2py/r20/`):
- `n2_checks.py`, `n2_checks.out` (NUMERICS (A), (B));
- `n2_geo.py` (a copy of `m1py/m1_common.py`, so that nothing is imported from `m1py/`).

`n2py/archive_N2_notes_2026-10-13.md` is a verbatim copy of Part II.

---
---

# Part II — the earlier note N2 (13 Oct 2026, round 2), verbatim

# N2: construction attempt under negligible-stakes indifference NSI_θ

13 Oct 2026. Labels as in BRIEF.md:
- **PROVED**: full proof written here.
- **CHECKED**: verified, with the proof sketched.
- **CONJECTURE**: not proved.
- **NUMERICS**: evidence only.

Citations:
- R1 (Lemma 1.1, Prop 2.1, Lemma 1.4, Prop 3.1), R10a (Thm M, Prop M′, Thm R, Thm V), R10b (Lemma UVN, Lemma M, Thm PL), all with the repairs in R6/R8/R12.
- CSE = *Conditional Shunning of Error*; CCIBU.

Scripts are in `n2py/`.

---

## 0. Outcome

**No construction exists. The task's target is provably out of reach, and so is most of its neighbourhood.** Under NSI_θ as BRIEF3 defines it, the band ties are *forced*, not merely permitted. Forced ties create a new rigidity that kills additive coverage:

1. **T1 is never covered.** For every θ > 0, every ε ∈ (0,1), and either norm (sup or Euclidean), there is no additive system on a decomposable domain with:
   - NSI_θ-(G);
   - a.e. unique, coherent interior Bayes models;
   - (LF) at T1;
   - T1 as the Bayes model at an interior prior.

   This is Cor C1. It holds for ε-contamination of **every** interior baseline, in every n ≥ 3.
2. **No interior full-dimensional target is covered for small θ.** For θ < θ_cap(K) (defined in §1), no interior full-dimensional target K is covered (Thm Z). Here θ_cap(K) > 0 depends only on the distance of K from the vertices of Δ. So the author's ideal ("every θ > 0") fails for **every** interior full-dimensional target. Small θ is the *worst* regime, not the best.
3. **Triangles.**
   - Every interior triangle in general position with an edge ray of D_K having a single positive coordinate is excluded for **every** θ (Cor C2). These are the "upright" triangles, including T1; about 87% of random triangles (vertices sampled Dirichlet(3,3,3)) are of this kind.
   - The remaining ("inverted") triangles are excluded for θ < θ_cap(K). Above θ_cap(K) only an exceptional coincidence configuration remains (Prop C3, CHECKED).
4. **The mechanism (Thm B, PROVED, any n ≥ 3).**
   - On a band problem at world i, the chart is a pencil through δ_i. So acceptance at the target prior p\* is transported unchanged along the whole ray (δ_i, p\*].
   - Near δ_i, strictly guided non-band gambles must be accepted.
   - Convexity of the Bayes cone then forces acceptance of band gambles that are rejected at p\*.

   Corollary: whenever a supporting functional (contact point) m ∈ K of a band-i boundary gamble is cut by a non-band-i gamble whose acceptance is in the advice range, the system fails.
5. **What survives (nearby results).**
   - (a) Under the *lenient* reading ("ties permitted, not forced"), all strict-(G) results stand: R10a Thm M polygons converge to T1. Thm B then shows that ties are forbidden on the exterior band collar of the target, so they buy nothing there (§7).
   - (b) The lesson for the definition: **partial (stake-limited) indifference at a world, with strictness elsewhere at the same world, is harmful.** The obstruction needs a strict/tie interface at world i. Σ_T (total indifference at a world) has none, which is why CSE covers boxes.
   - (c) Precise targets, two-world targets, and targets meeting the caps escape these arguments. Their status is open.

**Numerics** (§9) exhibit the Thm B witness explicitly in a band-surgered R10a 9-gon system.

---

## 1. Setting, conventions, and what NSI_θ-(G) forces

The setting is that of BRIEF.md, BRIEF2.md and BRIEF3.md. Additive rankings L_i(X) = ∫ ℓ_i(g, a_X(g)) dμ on a decomposable domain.

Notation:
* φ_i(h) = h_i/‖h‖, for either norm. The results hold for both norms, and §§2–5 hold for any norm unless stated.
* An orientation h is *band-i⁺* if it is mixed and 0 < h_i ≤ θ‖h‖.
* C_θ(i) = {h : h_i > θ‖h‖}. This is an open convex cone, because h ↦ h_i − θ‖h‖ is concave and positively homogeneous. Its elements are mixed or unanimous gambles with a *non-negligible* positive world-i stake.
* **cap_θ(i)** = {m ∈ Δ : m·h ≥ 0 for all h ∈ C_θ(i)}, the dual cap. It is a neighbourhood of e_i in Δ:
  * Euclidean norm: cap_θ(i) = {m : ∠(m, e_i) ≤ arcsin θ}, the dual of a round cone of half-angle arccos θ;
  * sup norm: cap_θ(i) = {m : m_i ≥ 1/(1+θ)}, obtained by dualising the generators (θ, ±1, ±1) of C_θ(i).
* θ_cap(K) = sup{θ : K ∩ cap_θ(i) = ∅ for all i}. This is positive for K ⊆ int Δ:
  * Euclidean: min_i sin(min_{m∈K} ∠(m, e_i));
  * sup: min_i (1/max_K m_i − 1).
  * For T1, the sup-norm value is 2(1−ε)/(1+2ε), and the Euclidean value is 0.77 / 0.53 / 0.25 / 0.05 at ε = .05 / .3 / .6 / .9 (`geometry.py`).

**Standing hypotheses (H).**
* We have an additive system on a decomposable domain with NSI_θ-(G).
* For every interior q the Bayes act is a.e. unique and the Bayes model B_q is a.e. coherent, B_q ≈ D_{K_q}. Under (LA), (S), (C) this is R1 Lemma 1.4; the task also requires it directly.
* D = D_K is B_{p\*} for an interior p\*.
* (LF) holds at D with an open N ⊇ ∂D∖0. So for a.e. h ∈ N, the advice range of the choice represented by h contains both "accept h" and silence.

**Nothing at boundary priors is used anywhere below.** No (S), no CCIBU, and no vertex coherence is needed, so the vertex step of CCIBU that BRIEF3 flags is irrelevant to these results.

**Lemma 0 (penalty form of NSI_θ-(G)). PROVED.** For each i and a.e. g, on the kinds of advice in the advice range A(g):
* on band problems (mixed, |g_i| ≤ θ‖g‖), ℓ_i(good) = ℓ_i(silence) < ℓ_i(bad) < ℓ_i(contradictory);
* elsewhere ℓ_i is strictly increasing in the four-rank order.

Hence, for an orientation h with accept-h and silence in its advice range, the vector c(h) = ℓ(0) − ℓ(accept h) has:
* c_i > 0 if h_i > θ‖h‖, or if h is unanimous positive;
* **c_i = 0 if h is band-i⁺**;
* c_i < 0 if h_i < 0.

*Proof.* This is the splicing argument of R1 Lemma 1.1. On a band problem, changing good to silence is a weak improvement in the coarser order, and so is changing silence to good. So (G) makes each change weakly improve L_i, and the two penalties are equal. The strict claims are R1 Lemma 1.1 verbatim. ∎

*Remark.* The ties are **forced**. So the strict systems of R10a (Thm M, Prop M′) and the Σ_T systems of CSE (zero reward for all positive stakes at worlds of T) are **not** NSI_θ systems. Under BRIEF3's definition no earlier positive result transfers automatically. The task's phrase "f_i may vanish (but not be negative)" describes the lenient reading, which §7 treats separately.

Charts are as in R1 Prop 2.1. For an orientation h whose advice range contains + and 0, with c′ = ℓ(0) − ℓ(accept −h) when acceptance of −h is in the advice range, h is accepted at q iff c·q > 0 and (if − is in the advice range) c·q > c′·q. Contradiction is never optimal.

---

## 2. The band pencil and ray transport

**Lemma 1 (ray transport). PROVED.** Let h be band-i⁺ with + and 0 in its advice range. Let p ∈ int Δ, and q(s) = (1−s)δ_i + s p for s ∈ (0, 1].
* (a) If h is accepted at p (strictly, with no tie), then h is accepted at every q(s).
* (b) If neither h nor −h is accepted at p, and there is no tie at p, then h is accepted at no q(s).

*Proof.* We have c_i = 0, so c·q(s) = s·c·p. If acceptance of −h is in the advice range, c′_i < 0, because (−h)_i < 0 makes accepting −h bad at world i.
* (a) Here c·p > 0 and c·p > c′·p. Then c·q(s) = s c·p > 0, and
  c′·q(s) = (1−s)c′_i + s c′·p < s c′·p < s c·p = c·q(s).
* (b) If c·p > 0, then either c·p > c′·p and h is accepted, or c′·p > c·p > 0 and −h is accepted; equality is a tie. So c·p ≤ 0, and c·p = 0 is a tie, so c·p < 0. Hence c·q(s) < 0. ∎

So **a band-i⁺ chart is a union of rays from δ_i.** For fixed q, Lemma 1 holds for a.e. h, because ties at p are null.

**Lemma 2 (vertex pull). PROVED.** Let x ∈ C_θ(i) be a mixed orientation with + in its advice range. Then the chart R(x) contains a relative neighbourhood of δ_i in Δ.

Consequently, for every non-null set E of such x there are a non-null E′ ⊆ E and r₀ > 0 such that, for every interior q with |q − δ_i| < r₀, a.e. x ∈ E′ is accepted at q.

*Proof.*
* We have c_i(x) > 0 by Lemma 0. If acceptance of −x is in the advice range, (c − c′)_i > 0, because accepting −x is bad at world i.
* So δ_i satisfies the finitely many strict affine inequalities defining R(x); advice range {+} (every evaluable model accepts x) gives R(x) = Δ.
* Let r(x) > 0 be measurable with B(δ_i, r(x)) ∩ Δ ⊆ R(x), and take E′ = {x ∈ E : r(x) ≥ r₀}. ∎

---

## 3. The band–hull obstruction

**Theorem B. PROVED (any n ≥ 3, any norm).** Assume (H). Let:
* w ∈ ∂D∖0 with 0 < w_i < θ‖w‖ and −w ∉ cl D;
* m ∈ K with m·w = 0 (a contact point of w).

Then the set of mixed orientations x ∈ C_θ(i) with m·x < 0 whose acceptance is in the advice range is null. In particular N ∩ C_θ(i) ∩ {m·x < 0} = ∅.

*Proof.* Suppose E is a non-null set of such x.

*Step 0 (a neighbourhood of w).* Choose an open ball U ∋ w such that:
* U ⊆ N;
* every h ∈ U is mixed with 0 < φ_i(h) < θ;
* (−U) ∩ cl D = ∅, which is possible because −w ∉ cl D.

*Step 1 (transport).*
* Lemma 2 gives E′ and r₀. Fix q on (δ_i, p\*] with |q − δ_i| < r₀; q is interior.
* For a.e. h ∈ D ∩ U: h is accepted at p\* without a tie, and its advice range contains + and 0 by (LF). Lemma 1(a) gives h ∈ B_q.
* For a.e. h ∈ U∖cl D: h ∉ B_{p\*}, and −h ∉ B_{p\*} because −h ∉ D. Lemma 1(b) gives h ∉ B_q.
* So **B_q ∩ U ≈ D ∩ U.**

*Step 2 (convexity).*
* B_q ≈ D_{K_q}, an open convex cone.
* An open convex set that contains a.e. point of an open set O contains O. (Each y ∈ O is the midpoint of y ± v with both points in the set, for a.e. small v.)
* Hence D ∩ U ⊆ D_{K_q}. Also some x ∈ E′ lies in D_{K_q}.

*Step 3 (hull).*
* Take z ∈ D ∩ U close to w, and y = (1−λ)z + λx with λ = λ₀ small.
* Since m·w = 0, we can choose |z − w| small enough that y ∈ U and m·z < λ₀|m·x|/2. Then
  m·y < λ₀|m·x|/2 − λ₀|m·x| < 0,
  so y ∉ cl D ⊆ {m·h ≥ 0}.
* Thus D_{K_q} ∩ U∖cl D is a nonempty open set, hence non-null, and it lies a.e. in B_q. This contradicts Step 1. ∎

**Corollary B1 (same-face form). PROVED.** Assume (H). Suppose an exposed face F_m = {h ∈ cl D∖0 : m·h = 0} (m ∈ K) contains:
* a point w with 0 < φ_i(w) < θ and −w ∉ cl D, and
* a point w′ with φ_i(w′) > θ.

Then (H) fails.

*Proof.* We have w′ ∈ ∂D∖0 ⊆ N. The points x = w′ − s𝟙 with s > 0 small form an open subset of N ∩ C_θ(i) with m·x = −s < 0. Apply Thm B. ∎

*Remark (why strict (G) escapes).* With strict (G), c_i(h) > 0 is merely small on near-band h, so the chart tilts and transport along (δ_i, p\*] holds only on one side. NSI_θ pins the chart line to δ_i. That is the whole difference.

---

## 4. Facet crossings: T1 for every θ

**Theorem C. PROVED (n ≥ 3; Euclidean or sup norm; any θ ∈ (0, 1)).** Assume (H). Let F_m (m ∈ K, m ≫ 0) be an (n−1)-dimensional exposed face of D. Write relint for the relative interior in m^⊥. Assume −h ∉ cl D on relint F_m, which is automatic if K is full-dimensional. If relint F_m contains
* (a) a point at which i is the only positive coordinate, and
* (b) a point with h_i < 0,

then (H) fails.

For θ ≥ 1 every mixed orientation is band at every positive world. Every mixed chart is then empty at interior priors, and (H) fails trivially, since ∂D∖0 is mixed.

*Proof.* Let S = {h ∈ relint F_m : h_j < 0 for all j ≠ i}. By (a), S is nonempty and relatively open. On S, h_i > 0: otherwise m·h < 0 for m ≫ 0. The set relint F_m is connected, and φ_i takes a negative value there by (b). There are three cases.
1. *Some s ∈ S has φ_i(s) > θ.* By connectedness φ_i takes a value in (0, θ) on relint F_m. Apply Cor B1.
2. *Some s ∈ S has φ_i(s) < θ.*
   * Points h ∈ D near s are band-i⁺ and have all other coordinates negative.
   * So c(h) has c_i = 0 and c_j < 0 for j ≠ i, and c·q < 0 at every interior q.
   * Their advice ranges contain silence by (LF), so a.e. such h is rejected at p\*.
   * But D near s is a non-null set of h accepted at p\*. Contradiction.
3. *φ_i ≡ θ on S.*
   * Euclidean norm: the quadratic form (1−θ²)h_i² − θ²Σ_{j≠i}h_j² vanishes on an open subset of the hyperplane m^⊥, hence on all of m^⊥. But m^⊥ ∩ e_i^⊥ ∋ h ≠ 0 (n ≥ 3), where the form is −θ²|h|² < 0.
   * Sup norm: on S, ‖h‖ = −min_{j≠i}h_j. On an open S′ ⊆ S where a single j₀ attains the minimum, h_i + θh_{j₀} = 0. This linear identity on an open part of m^⊥ forces m ∝ e_i + θe_{j₀}, contradicting m ≫ 0 for n ≥ 3. ∎

**Corollary C1 (contamination; T1). PROVED.** Let n ≥ 3, p ∈ int Δ, ε ∈ (0,1), and K = (1−ε)p + εΔ. Then (H) fails for every θ > 0 and either norm. In particular **T1 (p = u, n = 3) is covered under NSI_θ for no θ and no ε.**

*Proof.* Let v_k = (1−ε)p + εe_k. Then v_j·h − v_k·h = ε(h_j − h_k), so
relint F_k = {h : (1−ε)p·h + εh_k = 0, h_k < h_j for all j ≠ k}.
Fix i ≠ k.
* *(a)* Take h_k = −1, h_j = −1+η for j ∉ {i,k}, and
  h_i = β = [ε/(1−ε) + p_k + (1−p_i−p_k)(1−η)]/p_i > 0.
  This point lies in relint F_k, and i is its only positive coordinate.
* *(b)* Take h_k = −1, h_i = −½, and h_j = M for j ∉ {i,k} (such j exist since n ≥ 3), with
  M = (ε/(1−ε) + p_k + p_i/2)/(1 − p_i − p_k) > 0.
  This point lies in relint F_k and has h_i < 0.
* K is full-dimensional and v_k ≫ 0. Apply Thm C. ∎

For T1 this is visible in `geometry.py`:
* On F_3, h(s) = (−1+s, b−s, −1) with b = (2+ε)/(1−ε). Here φ_2 runs from about −0.39…−0.03 up to φ_2(r₃₁).
* Sup norm: φ_2 ≡ 1 near r₃₁.
* Euclidean norm: φ_2(r₃₁) = 0.836…0.999, and the maximum lies strictly inside F_3 (case 1 for θ below the maximum; case 2 above it).

**Corollary C2 (upright triangles). PROVED (n = 3).** Let K ⊆ int Δ be a triangle in general position (no edge line through a vertex of Δ). If some edge ray of D_K has exactly one positive coordinate, (H) fails for every θ.

*Proof.*
* The edge ray r_e of edge e = [v_k, v_j] has positive coordinates exactly at the vertices of Δ on K's side of line(e). General position makes every coordinate of every edge ray nonzero.
* Let r_e have single positive coordinate i. If i were positive on the other edge rays of both F_k and F_j, then e_i would lie on K's side of all three edge lines, so e_i ∈ K, which is impossible.
* So on F_k (say) coordinate i changes sign, giving (b). Near r_e, relint F_k has the sign pattern of r_e, giving (a). Apply Thm C. ∎

**Proposition C3 (inverted triangles above θ_cap). CHECKED (sketch).** Suppose every edge ray of a general-position triangle has two positive coordinates. Then (H) can hold only in an exceptional configuration, which requires all of the following.
* At each edge ray r = cl F ∩ cl F′ with positive coordinates {i, j}:
  * i crosses on F only and j on F′ only;
  * φ_i(r) = φ_j(r) = θ, with the same θ at all three edge rays;
  * the contact vertex of F lies in cap_θ(i), and that of F′ lies in cap_θ(j).

*Sketch.*
* Each positive coordinate crosses on an adjacent facet (the C2 argument), so Cor B1 gives φ ≤ θ on that facet.
* Positivity near r (case 2 of Thm C, with two positive coordinates) forces the rest.
* The cap condition comes from the Thm Z step 2 perturbation at w₀ = r.

For the symmetric inverted triangles this is excluded by θ_inv < θ_cap at ε = .1, .3, .6, .9 (`geometry.py`).

---

## 5. Every interior full-dimensional target, for small θ

**Theorem Z. PROVED (any n ≥ 3, any norm).** Assume (H) with K ⊆ int Δ full-dimensional and K ∩ cap_θ(i) = ∅ for every i (that is, θ < θ_cap(K)). Contradiction.

*Proof.*

*Step 1 (positivity).* For a.e. h ∈ D ∩ N, some l has h_l > θ‖h‖. Otherwise c(h) ≤ 0 with a negative entry (h is mixed), so c·p\* < 0 and h is rejected at p\*, as in case 2 of Thm C.

*Step 2 (φ_i ≤ θ on ∂D∖0, for every i).*
* ∂D∖0 is connected (n ≥ 3).
* φ_i is negative somewhere on it. Separate e_i from K by a gamble g, then subtract the constant min_K g·m, which keeps g_i < 0.
* Suppose φ_i(w′) > θ somewhere. Along a path from a negative value to w′, there are band-i⁺ points w_k → w₀ with φ_i(w₀) = θ. Take t₁ = the first time φ_i ≥ θ, and t₀ = the last time before t₁ with φ_i ≤ 0.
* Choose contacts m_k ∈ K with m_k·w_k = 0, and a subsequence m_k → m\* ∈ K. Then m\*·w₀ = 0.
* Since m\* ∉ cap_θ(i), there is h ∈ C_θ(i) with m\*·h < 0. Put x = w₀ + s h. By the triangle inequality,
  x_i − θ‖x‖ ≥ s(h_i − θ‖h‖) > 0.
  Also m\*·x = s m\*·h < 0, and x ∈ N for small s.
* For large k, m_k·x < 0 on an open neighbourhood of x in N ∩ C_θ(i). Theorem B with (w_k, m_k) gives a contradiction. Note −w_k ∉ cl D because K is full-dimensional.

*Step 3.*
* Fix w ∈ ∂D∖0 and a contact μ ∈ K (μ·w = 0). Take small balls B ∋ w inside N.
* By Step 2, each convex C_θ(l) ∩ B misses ∂D, so it lies in D or misses cl D.
* By Step 1, D ∩ B is a.e. covered by those C_θ(l) ∩ B that lie in D. Since w ∈ cl(D ∩ B) for every B and there are finitely many l, some l has w ∈ cl C_θ(l) and C_θ(l) ∩ B ⊆ D ⊆ {μ·y > 0}.
* *Local to global:* suppose y′ ∈ C_θ(l) had μ·y′ < 0. Take c ∈ C_θ(l) ∩ B near w with μ·c small. Then points of [c, y′] near c lie in C_θ(l) ∩ B with μ < 0.
* So μ·y ≥ 0 on C_θ(l), i.e. μ ∈ cap_θ(l) ∩ K = ∅. Contradiction. ∎

*Reading.* At small θ, the band edge {φ_i = θ} lies close to the hyperplane {h_i = 0}, so it meets the target boundary. There Thm B forces K to contain only points of the cap. For **every** interior full-dimensional target the admissible θ (if any) satisfy θ ≥ θ_cap(K). The answer to BRIEF3 question (2) is therefore the reverse of the hoped-for one.

---

## 6. Other targets, and n ≥ 4

* **Interior segments (T3).**
  * Let K = [a, b] in general position. The face F_a = {a·h = 0, b·h > 0} is an open half-plane.
  * Pick i, j with b_i/a_i > b_j/a_j. Then h = e_i − (a_i/a_j)e_j ∈ relint F_a.
  * Band points h = z + t(e_i − (a_i/a_j)e_j) also lie in relint F_a, where z spans a^⊥ ∩ e_i^⊥ and b·z > 0.
  * −h ∉ cl D on relint F_a. So Cor B1 excludes T3 for all θ < sup_{relint F_a} φ_i (PROVED for that range). The full range is open.
* **T4 = conv{e₁, u}, a boundary-touching segment, with an interior target prior.**
  * The face F_u = {u·h = 0, h₁ > 0} contains (2, −1, −1), with φ₁ = 2/√6 ≈ 0.816 (Euclidean) or 1 (sup).
  * It also contains band points (t, 1, −1−t).
  * −h ∉ cl D because cl D ⊆ {h₁ ≥ 0}.
  * Cor B1 excludes T4 for θ < 0.816 (Euclidean) and θ < 1 (sup). PROVED.
* **Boundary-touching full-dimensional targets.**
  * Thm B and Cor B1 apply unchanged.
  * Thm Z needs K ∩ caps = ∅, which fails for targets containing vertices. Such targets, with K near e_i where it meets cap_θ(i), are not excluded by these arguments. Open.
* **Precise targets** {p\*}. Every boundary gamble has −w ∈ ∂D, so Lemma 1(b) fails: exterior band gambles may switch from −h to +h along the ray. Thm B does not apply. **Open**; no construction was attempted.
* **n = 2.**
  * Faces are rays and ∂D∖0 is disconnected, so Thm B, C and Z have no content.
  * Case 2 of Thm C still gives a necessary condition. For K = {m₁ ∈ [a, b]}, the boundary rays must be non-band at their positive coordinate, e.g. (1−a)/‖(1−a, −a)‖ > θ. Sufficiency is open.
* **n ≥ 4.** Lemmas 0–2, Thm B, Cor B1, Thm C, Cor C1 and Thm Z are written dimension-free (n ≥ 3). The contamination no-go holds for every θ in every n ≥ 3.

---

## 7. Lenient reading and the general tie-region principle

* **Lenient NSI_θ** ("good ⪯ silence allowed on band problems, strictness elsewhere"; the task's "may vanish"). This class contains every strictly guiding system. So R10a Thm M and Prop M′ (polygons converging to T1 in Hausdorff distance), CSE boxes, precise targets and all earlier positive results stand.

  **Proposition L. CHECKED.** Under the lenient reading, with (H) otherwise, Thm B's proof shows that for w, m, x as in Thm B, c_i > 0 a.e. on an exterior slab {y near w : −c < m·y < 0}. The hull of x and D near w contains that slab when w is in the relative interior of a facet. Interior-side ties add rigidity only: Lemma 1(a) transports from p\* *away* from δ_i as well. So ties cannot help near the target boundary.

  CONJECTURE: under the lenient reading, T1's status equals its strict status (open; R10b Thm PL plausibly survives, because Lemma M uses exterior strictness only).
* **General tie regions.** Replace the band by any measurable cone R_i of orientations with h_i > 0 on which good ~ silence at world i, with strictness on {h_i > 0}∖R_i. The proof of Thm B goes through verbatim. It obstructs whenever a target boundary gamble in int R_i has a contact m cut by a gamble in int({h_i > 0}∖R_i) whose acceptance is in the advice range with m·x < 0.
  * Σ_T has R_i = {h_i > 0}, with no strict side. Hence no obstruction, consistent with CSE.
  * **Partial indifference at a world (a strict/tie interface at that world) is the harmful structure.** A weakening that is to help coverage must avoid such interfaces near target boundaries. A target-independent band cannot do that.
* **Scope.** Thm B uses additivity (charts are affine minimisation diagrams). For non-additive (IB) preorders under NSI_θ nothing is claimed.

---

## 8. Designs tried, and where each fails

| design | fate | reason |
|---|---|---|
| band surgery of gauge mixtures (f_i := 0 on band-i⁺) | incoherent B_q near δ_i | Thm B; explicit witness in §9 |
| plateau K_q ≡ T1 near p\* (R10b PL crossing argument broken by NSI) | impossible | Thm B uses p\* alone, no plateau needed |
| imprecise vertex models (caps) | allowed at vertices | Thm Z: the target's band contacts must lie in caps |
| Σ_T-type zero lower slope inside bands only | not an NSI system unless ties are exact; with exact ties | Thm B / C |
| large θ for T1 | impossible | Thm C cases 1–3 cover all θ ∈ (0,1); θ ≥ 1 trivial |

---

## 9. Numerics (`n2py/`, evidence only)

* `geometry.py`:
  * T1 facet data, both norms. The Euclidean maximum of φ_2 on F_3 is interior, and φ_2 is negative near r₃₂.
  * θ_cap for T1 (the sup-norm formula is confirmed).
  * 20000 random triangles: 87% have a single-positive edge ray (Cor C2), 13% are inverted.
  * Symmetric inverted triangles: θ_inv < θ_cap, so Thm Z excludes θ_inv.
* `surgery_check.py`, `hull_check.py`, `hull_check2.py`: random midpoint and dual-hull tests of band-surgered R10a systems (hexagon, 9-gon).
  * Hexagon: defects of mass up to 0.6% at θ = .2.
  * 9-gon: about 0. This is because Thm B's failure region is a thin exterior collar, so random tests are insensitive. Not evidence of coherence.
* `witness2.py` (9-gon, θ = .05, Euclidean): constructs Thm B's objects:
  * a band-1⁺ boundary gamble w of B_u, with φ₁ = 0.025;
  * its contact m\* = (0.234, 0.531, 0.234);
  * a non-band x whose acceptance is in the advice range, with m\*·x = −0.0044.

  At q = (1−s)e₁ + s u with s ≤ 0.002: x and z (inside, near w) are accepted, while y ∈ [z, x] (beyond the facet plane, φ₁ = 0.026, rejected at u) is rejected. So B_q is non-convex exactly as predicted. For s ≥ 0.02, x is not yet accepted, consistent with Lemma 2's r₀.

  The surgered B_u itself shows a reflex kink where its facet meets the band edge (a boundary gamble with m\*·w′ < 0).

---

## 10. Recommendation (spirit of the project)

* NSI_θ as defined (forced ties) does not deliver coverage of T1 for any θ. It excludes every interior full-dimensional target for θ < θ_cap(K), and every upright triangle and every contamination class for all θ.
* The reachable nearby results are:
  * (i) the lenient reading, which keeps all strict-(G) coverage, including the R10a polygons converging to T1, but adds nothing near target boundaries (Prop L);
  * (ii) the general tie-region principle (§7), which says any acceptable indifference weakening must be *total at a world* (Σ_T-like) rather than stake-limited.
* The author should decide between:
  * (a) dropping the forced-tie clause (lenient reading), in which case T1 stays exactly the strict problem; or
  * (b) seeking a weakening without strict/tie interfaces at a single world (for instance indifference indexed by events rather than by stake size).

  Option (b) is the only route this analysis leaves open for contamination targets.
