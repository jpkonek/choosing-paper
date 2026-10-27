# T2n (round 22). Two or more worlds without strictly positive integrable endorsers: double total blindness is consistent on an edge, the field questions are all "Yes", sheltering is forced onto the blind pair, and the three-world assembly does not close

16 Oct 2026 (BRIEF13 rules; task: settle the configurations of R21 with ≥ 2 worlds lacking (CA⁺): (P0), (PD), (E),
(X) and the (S) residual). Labels: **PROVED** (full proof here, from results marked proved and refereed, each named
with its status), **CHECKED** (a step-by-step reading, not a re-derivation), **CONJECTURE**, **NUMERICS**
(`t2npy/t2n_checks.py`, run `python3 -I -B t2n_checks.py` from inside `t2npy/`; output `t2n_checks.out`; no proof
rests on it). No assumption is added; every extra hypothesis is a hypothesis of a stated result.

Notation: R21 §1 (n = 3, U = D_{K′}, K′ = u + s(T1 − u), M, N₊, P_k, E_k, σ_k, Q_l, R_ij, J_l, (H_U), (NC), Λ_k,
A*); Q3 Part I ((CA), (CA⁺), ρ^ca_k, Λ^ca_k, c♮, b♮); K3 §1 (𝒩, 𝔚, localizing families, (Loc), (Loc_int));
Q2 Part I (enlarged data D̃^k, sheltering); K1 §§2, 5 (k-safe models, anti-safe points); P1 Part I and L2 §§1–3
(two-world design: chain coordinate x, path C_b, c_b = {x < b}, d_b, λ, T, D(δ), generators g_F, selectors 𝔉).
"Totally blind" means: every bounded endorser of every localized family of relevant comparisons is purely finitely
additive on the region concerned (P1.13's conclusion).

---

## 0. Outcome

**Neither a cover nor a theorem. Both attempts were carried to the point where they stop, and both stop at the same
place: the interior of the simplex, i.e. the three-world assembly at indices whose support contains the two blind
worlds.** What is settled on the way:

1. **The negative route as proposed is false at the edge (Theorem T2n.1, Corollary T2n.2; PROVED).** P1's totally
   blind world and its mirror image form a **full two-world system in which both worlds are totally blind**
   (Λ = Λ_∞ = Λ^ca = M at both, (NC) and mode (M2) at both, both (Loc) ∖ (Loc_int)). The same system lives on the
   decomposable domain 𝓔_ij of edge models of M_U (n = 3). So "Pareto off the carriers on the edge + closed sections
   at its endpoints" cannot force a strictly positive (indeed any nonzero) countably additive endorser at either world
   of an edge: N2.1 is vacuous there (N12_referee §2.1), and every edge-local axiom holds. The new ingredient is a
   **self-protection lemma** (T2n.0): in P1's design, X ⪯₁ C_b with X regular forces E₁X ∩ d_b null, so no weak
   domination needs only strict (G) at the partner. The second step of the suggested route, link-class gluing as in
   Q1, does apply to a blind world that accepts cut moves along both of its edge chains (T2n.8), but what it yields
   is (Loc), not (CA⁺); the exclusion step Q1.24 needs two (RL-2) partners, which a world of a blind pair never has.
   So the route ends in the all-(Loc) case, i.e. in Q_W.
2. **The field-level questions of R21 for (PD), (E), (X) all have answer YES (Proposition T2n.4; PROVED, elementary).**
   Explicit fields: c ≡ 0 (and (ρσ₁·1_{M∖E₁(T1)}, 0, 0)) for Q_N1[int, overlap]; (ρσ₁, 0, 0) for Q_N1[edge];
   (0, σ₂1_{V₂}, σ₃) with a rigid edge segment Λ₂ for Q_N1[vtx]. Each satisfies (γ₀), coherence of B_q, admissibility,
   the N1.2 dichotomy with between models, and N12_referee's strengthening N2.3′(d). So R21's "No closes (PD)/(E)/(X)"
   is vacuous: **these three configurations cannot be closed by any field-level argument**; only ranking-level
   arguments remain. ((P0) is untouched: L1.D concerns pairwise-null blind sets with c ≠ 0 a.e., which these fields
   are not.)
3. **Toward the theorem, at the ranking level (Theorem T2n.3; PROVED from K3.5 [R1] and Q2.10(a) [R1]).** In an
   all-(Loc) cover with one (CA⁺) world k, the persistent sheltering of Q2.10(c) lies on R_ij for the **other two**
   worlds, for every choice of enlarged data. So all-(Loc) covers need ≥ 2 non-(CA⁺) worlds that shelter each other;
   with Q2.16 the all-(Loc) part of every multi-blind configuration that has a (CA⁺) world is exactly Q_W for that
   pair. **Q_W is not settled.**
4. **Toward the cover: the blueprint (E∗) and what is verified (§4).** Worlds 2, 3 of P1 type, world 1 (CA⁺).
   - Every **edge block exists** as a full two-world system on 𝓔_ij: P1.10 on 𝓔₁₂, 𝓔₁₃ [R1], T2n.2 on 𝓔₂₃.
   - The **three universal fixed points are degenerate exactly as required** (Prop. T2n.5; PROVED): with world 1 as
     the special world c♮ = (ρσ₁, 0, 0), A(c♮) = [e₂, e₃] (configuration (E), b♮ = 2); with world 2 (resp. 3) special,
     b♮ ≥ 1 at world 3 (resp. 2) and T1 is admissible at e₃ (resp. e₂), at no interior weight.
   - The **natural ends of the edge chains shelter each other** (Prop. T2n.7; PROVED, elementary; NUMERICS (D)): world
     2's end on its 12-chain and world 3's end on its 23-chain overlap, at every depth, in a cone around the e₃ ray
     inside (+,−,+) ∩ D_{T1}, where T1 errs at world 2 only. This is the sheltering T2n.3 demands (overlapping
     localizing families of the blind pair), at a place where T1 errs at the localizing world.
   - **Link-class gluing (T2n.8; CHECKED).** With the linear host the two edge chains of world 2 cross transversally on
     Q₂, and world 2 accepts cut moves along both; Q1.22–Q1.23 then make world 2 (Loc) with ρ₂ = ρ₁φ(x₁₂) = λψ(x₂₃) on
     Q₂. So (E∗) is all-(Loc), its ends on Q₂ act by localization, and world 1's density is fixed on R₂₃ by the two
     blind designs.
   - **Where it broke.** I could not define worlds 2, 3 at interior indices (§4.3). The single obstruction (§5) is Q_W
     for the blind pair, in the following sharpened form: the σ-finite KKM argument stops exactly at indices p with
     {2, 3} ⊆ supp p, against competitors that must be correct at 2 and at 3 on the sheltered cone. When the pair
     carries infinite minority mass on R₂₃, the obstruction is entirely on the edge [e₂, e₃] (Prop. T2n.9; PROVED): no
     model may lie below a 2-safe and a 3-safe test of finite cost at both worlds. In (E∗) the minority mass is finite
     (T2n.8), so the interior indices carry it.

| | Statement | Label |
|---|---|---|
| T2n.0 | self-protection of P1's world: X ⪯₁ C_b, X regular ⇒ E₁X ∩ d_b null | PROVED; NUMERICS (A) |
| T2n.1 | P1 ⊕ mirror-P1: full two-world system, both worlds totally blind, (NC), (M2), (Loc) ∖ (Loc_int) | PROVED; NUMERICS (B), (C) |
| T2n.2 | the same on the edge domain 𝓔_ij of M_U (n = 3); the edge axioms never force a nonzero CA endorser | PROVED |
| T2n.3 | all-(Loc) covers: a (CA⁺) world never shelters; sheltering sits on the edge of the two non-(CA⁺) worlds | PROVED |
| T2n.4 | Q_N1[int, overlap], Q_N1[edge], Q_N1[vtx] have answer YES (explicit fields) | PROVED |
| T2n.5 | universal fixed points of the blueprint (E∗): degenerate as required | PROVED |
| T2n.6 | an acceptance set containing a full half-space of an a.e.-positive finite measure is endorsed by it | PROVED |
| T2n.7 | edge-chain ends of the linear host: 12-end of world 2 meets 23-end of world 3 near the e₃ ray, at every depth | PROVED; NUMERICS (D) |
| T2n.8 | gluing at the blind world's link class: (E∗) is all-(Loc); ρ₂ = ρ₁φ(x₁₂) = λψ(x₂₃) on Q₂; finite minority mass on R₂₃ | CHECKED (reading of Q1.22–Q1.23 [R1 continuous case, Q13_referee]) |
| T2n.9 | infinite minority mass on R_ij ⇒ no model lies below an i-safe and a j-safe test of finite cost (edge reduction) | PROVED |
| Q_W (pair form) | can every admissible triple of safe tests have an anti-safe index whose support contains the sheltering pair, with closed sections? | open (= Q_W) |

---

## 1. Double total blindness in two worlds

Setting of P1 §1 (n = 2, any K′ = [α′, β′] ⊆ (0,1), C2.1 path C_b with c_b = E₁C_b ∩ M = {x < b}, λ = μ/μ(M), selection
p ↦ C_{p₂}). World 1 is P1's world 1 (§2 of P1, with its acceptance set 𝒜₁ := rules R⁻, R⁺, R⁰ over
⋃_F (g_F + T)). Its world-1 vectors are 1_{E₁Y} − 1_{E₁X}.

**Lemma T2n.0 (self-protection; PROVED, from P1.10a [R1]).** For every regular model X and every b ∈ [0,1]:
X ⪯₁ C_b ⇒ λ(E₁X ∩ d_b) = 0.

*Proof.* Write A := E₁X ∩ M, P := c_b ∖ A, Q := A ∩ d_b. The vector of X ⪯₁ C_b is δ′ = 1_{E₁C_b} − 1_{E₁X}; it vanishes
on N₊ (X regular), so D(δ′) = 0, and δ′|_M = 1_P − 1_Q. Acceptance under R⁰ gives δ′|_M = g_F + f with F ∈ 𝔉, f ∈ T.
- F ≡ ⊥: τ_f(b) = τ_{δ′}(b) = −λ(Q) ≥ 0, so Q is null.
- *Case (i): some selected level n has a block k on the line of F(n) with u_k ≥ b.* Then P ⊆ c_b ⊆ c_{u_k}, so
  τ_{δ′}(u_k) = −λ(Q ∩ {x ≥ u_k}) ≤ 0. Since g_F = 1 on ref_k, g_F ≥ 0 off S, and k ∈ I_n, P1.10a gives
  τ_{g_F}(u_k) ≥ λ(ref_k) − Θ(F, k) ≥ (16/25 − 1/25) r_k > 0. Hence τ_f(u_k) < 0, impossible.
- *Case (ii): every block on every selected line has u_k < b.* Then v_n < b for each selected n, so every selected
  source lies in Σ_n ⊆ c_{v_n} ⊆ c_b, and g_F ≥ 0 on d_b. So τ_f(b) = −λ(Q) − τ_{g_F}(b) ≤ −λ(Q), and Q is null. ∎

This is P1.10 step 4 with the last line ("then P is null", which used λ(P) ≤ λ(Q) from the additive world 2)
removed: **world 1 alone already forbids any weak improvement that errs to the right of the cut.**

**The mirror world.** Let x′ := 1 − x (it also pushes λ|_M to Lebesgue measure). World 2's errors at C_b are
d_b = {x ≥ b} = {x′ ≤ 1 − b} = c′_{1−b} (mod null). Define world 2 as P1's world 1 written in the coordinate x′ (blocks
accumulating at x′ → 1, i.e. x → 0; thin sources reaching every point; the cone T′ := {f : ∫_{x′≥t} f dλ ≥ 0 ∀t}),
acting on world-2 vectors 1_{E₂Y} − 1_{E₂X}. Every statement of P1.10a–P1.14 is a statement about λ, the chain
coordinate, the cuts c_b and the N₊ rules, so it holds for world 2 with (x, b) replaced by (x′, 1 − b); world 2's
index along the selection is 1 − p₂ = p₁.

**Theorem T2n.1 (PROVED, from P1.10–P1.14 [R1, P1_referee] and T2n.0).** The two-world ranking (world 1 = P1's world 1,
world 2 = its mirror) on M_U with selection p ↦ C_{p₂} satisfies strict (G), (IB), (LA), (S) (competitiveness on supp p,
closed sections for every model at both worlds), (C), C_L = U_L = {C_b : b ∈ [0,1]}, and (LF) at every interior C_b.
Both worlds are totally blind: for every localizing family D and every ν ∈ 𝒩(𝔚_D) of either world, ν vanishes on
every c_b, b < 1 (world 1), resp. on every d_b, b > 0 (world 2). Hence at both worlds Λ = Λ_D = Λ_∞ = Λ^ca = M, (NC)
holds, the mode is (M2), and the world is (Loc) ∖ (Loc_int).

*Proof.*
1. *Preorders, strict (G), (IB).* P1.11 for world 1; its mirror for world 2 (Lemma vectorform).
2. *Closed sections.* P1.12 for world 1 (initial segments, closed, for every model); its mirror for world 2 (final
   segments). The index map p ↦ b = p₂ is continuous.
3. *Competitiveness.* At p = e₁, C₀ = P₁ and every world-1 vector 1_{E₁X} ≥ 0 is accepted; e₂ is the mirror. For
   b ∈ (0,1) and any model X: if N_X is non-null, D(δ) > 0 at world 1 and R⁺ accepts. If X is regular, its world-1
   vector restricts on M to 1_Q − 1_P with P ⊆ c_b, Q ⊆ d_b, and its world-2 vector to 1_P − 1_Q. If λ(Q) ≥ λ(P),
   then τ_{1_Q−1_P}(t) = λ(Q ∩ {x ≥ t}) − λ(P ∩ {x ≥ t}) ≥ min(λ(Q) − λ(P), λ(Q ∩ {x ≥ t})) ≥ 0, so 1_Q − 1_P ∈ T and
   world 1 accepts. Otherwise λ(P) > λ(Q), and by the mirror computation 1_P − 1_Q ∈ T′, so world 2 accepts.
   (NUMERICS (C): 3000/3000 random cut pairs.)
4. *No weak domination; C_L; (C).* Suppose X ⪯₁ C_b and X ⪯₂ C_b. R⁻ at world 1 forces N_X null. By T2n.0, Q is null.
   The world-2 vector of X ⪯₂ C_b is then 1_{E₂C_b} − 1_{E₂X} = −1_P, which world 2 accepts only if P is null
   (strictness, P1.11 mirrored). So X = C_b. With Theorem kkm (only (LA), (S)), every undominated model is tied at both
   worlds with some C_b, hence equal to it; so U_L = C_L = {C_b}, every C_b being coherent, and (C) holds.
5. *(LF).* C2.1(4), a property of the domain and the path, as in L2.1.
6. *Blindness, (NC), (M2).* P1.13 uses only world 1's acceptance set and C_L = {C_b}: Step A uses accepted cut pairs
   (P_{n,i}, Q′) at v_n, Step B uses accepted T-moves; both are relevant since C_L = {C_b}. Its mirror holds at
   world 2. A nonzero (CA) density, normalised, would be a bounded endorser with nonzero CA part (Q3 §4 item 2), so
   Λ^ca = M at both worlds.
7. *(Loc) ∖ (Loc_int).* P1.14 uses only world 1's acceptance set (the base step and φ-neutral generators); its mirror
   at world 2. ∎

NUMERICS (A): on P1's finite cell model (`p1_cell_copy.py`, a verbatim copy), the LP relaxation of T2n.0 over 9464
selector/cut pairs (1518 feasible) has max λ(Q) = 0; positive control (C_b ⪯₁ X instead) reaches 1. (B): strictness LP,
0 over 91 selectors.

**Corollary T2n.2 (the edge form; PROVED).** Let n = 3, i ≠ j, k the third world, and let 𝓔_ij be the class of
models of M_U that equal P_i on Q_k ∩ U (the edge models of N2 Part I, with arbitrary advice on N₊). 𝓔_ij is a
decomposable domain. Take the linear edge chain C_s := U ∩ {((1−s)e_i + se_j)·g > 0} (coherent, in 𝓔_ij), for which
E_i(C_s) ∩ R_ij = {σ < s} with σ := |g_i|/(|g_i| + |g_j|) on R_ij; let λ be normalised μ on R_ij ∩ U and x := F(σ),
F the (continuous) distribution function of σ under λ. Then the construction of T2n.1, with M replaced by R_ij ∩ U,
is a two-world full system (worlds i, j) on 𝓔_ij with selection p ↦ C_{s(p)}, s(p) := p_j, in which both worlds are
totally blind on R_ij.

*Proof.* The proof of T2n.1 never uses the dimension of the gamble space: only (R_ij ∩ U, λ, x), the nested chain
{σ < s} = {x < F(s)} (mod null) and the N₊ rules. ∎

*What this does to the negative route.* Every three-world cover restricts, on 𝓔_ij, to: (a) strict (G), (IB) at worlds
i, j; (b) competitiveness of the edge-selected models on {i, j} against all of 𝓔_ij (N1.0(b)); (c) closed sections
along [e_i, e_j] for every member of 𝓔_ij. N2.1 (Pareto off the carriers), N2.2, N1.1, N1.2, N1.4–N1.6 are
consequences of (a)–(c) and K3.1. The system of T2n.2 satisfies (a)–(c) (and more: (C), C_L = chain), and in it
neither world's edge comparisons have a nonzero countably additive endorsing density, localized or not. **So no
argument that uses only (a)–(c) on one edge can force a (CA⁺), or any nonzero CA, endorser at either world of an edge
between two non-(CA⁺) worlds (PROVED, by exhibiting the model).** A negative proof must use the third world or T1.
(The link-class gluing of Q1 [R1, Q13_referee] uses only that a world accepts cut moves along two edge chains that
cross transversally on its link class; Q1.20 derives those moves from (RL-2) partners, but a blind world may accept
them by design, as both worlds of T2n.1 do. Gluing then makes the world (Loc) (Q1.23), see T2n.8. The exclusion Q1.24
goes through H1.2 and needs two integrable partners; at either world of a blind pair one partner is the other blind
world, so it does not apply. The route therefore ends in the all-(Loc) case of §3.)

---

## 2. The field questions of R21 for (PD), (E), (X) are all "Yes"

Q_N1 (N1 §7, N12_referee §1.9) and its restrictions in R21 ask for a field c = (ρ_kσ_k) (ρ_k ≥ 0 integrable) with:
(γ₀) d_t(c) = 0 for all t ∈ Δ; B_q coherent for q ∈ Δ° whenever c ≠ 0 a.e.; T1 = B_{p*} ∪ S with S ⊆ Z_{p*} for some
p*; for every ordered pair (i, j), either Λ_i ∩ R_ij = E_i(D_K) ∩ R_ij for a coherent between model D_K
(K ∩ [e_i, e_j] ≠ ∅, K ⊆ co(K′ ∪ [e_i, e_j])), or Λ_i ∩ Λ_j ∩ R_ij non-null; some Λ_k non-null. N12_referee adds:
whenever Λ_i ∩ Λ_j ∩ R_ij is null, every extreme edge θ-Bayes model E^{θ,±} of (ρ_i, ρ_j) is coherent.

**Proposition T2n.4 (PROVED).** Let ρ := 1 on M. Write C^{23}_{s₀} for the linear 23-edge model of T2n.2 with
s₀ ∈ (0,1), and Λ⁰ := E₂(C^{23}_{s₀}) ∩ R₂₃ = {σ < s₀} ∩ R₂₃.
- **(a) Q_N1[int, overlap] = Yes:** c ≡ 0. Also c = (ρσ₁·1_{M∖E₁(T1)}, 0, 0) (world 1 blind exactly on E₁(T1) ∩ M).
- **(b) Q_N1[edge] = Yes:** c = (ρσ₁, 0, 0), with A(c) = [e₂, e₃].
- **(c) Q_N1[vtx] = Yes:** c = (0, ρσ₂·1_{M∖Λ⁰}, ρσ₃), with A(c) = {e₁}, Λ₁ = M and Λ₂ = Λ⁰ non-null.

*Proof.* Throughout, P_k = D_{co(K′∪{e_k})}, P₂ ∩ P₃ and every C^{23}_s are coherent, and a t-Bayes model with all its
ties assigned arbitrarily is a minimiser, so d_t = 0 as soon as some coherent model is t-Bayes (ties free).
- **(a), c ≡ 0.** Every model is t-Bayes for every t, so (γ₀) holds (take T1); the coherence clause is vacuous;
  A(c) = Δ; every Λ_k = M, so every pair is in the second alternative and the extra clause is vacuous.
  *Second field.* For t₁ > 0 the t-Bayes models are P₁ on V₁ = M ∖ E₁(T1) and arbitrary on Λ₁ = E₁(T1) ∩ M; T1 is one
  (T1 = P₁ on V₁), so (γ₀) holds; c = 0 on Λ₁, so the coherence clause is vacuous; p·c = p₁σ₁1_{V₁} agrees in sign with
  T1 wherever it is nonzero, so A(c) = Δ ∋ interior points; Λ₂ = Λ₃ = M, so every pair is in the second alternative.
- **(b).** For t₁ > 0, B_t = P₁ (ties free), coherent; for t₁ = 0 everything ties. B_q = P₁ for q ∈ Δ°. A(c): p·c = p₁σ₁
  agrees with T1 only if p₁ = 0, so A(c) = [e₂, e₃], which meets the open edge; Λ₂ ∩ Λ₃ = M ⊇ J₁; θ(A) = [0,1] and the
  edge ties Z_θ ∩ R₂₃ = R₂₃ are non-null at every θ. Pairs: (2,3), (3,2) jointly blind; (2,1): Λ₂ ∩ R₁₂ = R₁₂ =
  E₂(P₁) ∩ R₁₂ with P₁ = D_{co(K′∪{e₁})}, a between model; (1,2): Λ₁ ∩ R₁₂ = ∅ = E₁(P₁) ∩ R₁₂; (1,3), (3,1) likewise.
  The extra clause for (1,j): e_θ = θρ₁ ≥ 0 on R₁ⱼ, so E^{θ,±} = P₁ for θ > 0, and E^{0,−} = P₁, E^{0,+} = P_j.
- **(c).** t·c = t₂σ₂1_{M∖Λ⁰} + t₃σ₃ (t₁ is irrelevant). On Q₁ worlds 2, 3 agree, Λ⁰ ⊆ R₂₃.
  - t₃ > t₂: B_t = P₃. t₂ > t₃ > 0: on R₂₃ ∖ Λ⁰ world 2 wins, on Λ⁰ world 3, so B_t equals P₂ off Λ⁰ and P₃ on Λ⁰,
    which is C^{23}_{s₀} (it errs at 2 exactly on Λ⁰ and is P₂ on Q₁). t₂ > t₃ = 0: C^{23}_{s₀} is Bayes with ties on
    Λ⁰. t₂ = t₃ > 0: P₃ is Bayes with ties on R₂₃ ∖ Λ⁰. t = e₁: all ties. So (γ₀) holds. For q ∈ Δ° with q₂ = q₃,
    B_q = C^{23}_{s₀} ∩ P₃, an intersection of two coherent cones, hence coherent (D_{K} ∩ D_{K″} = D_{co(K∪K″)}).
  - A(c) = {e₁}: for p ≠ e₁, J₁ ⊆ Q₁ ⊆ M ∖ Λ⁰ is non-null, T1 errs there at 2 and 3, and p·c has the sign of the
    2-and-3 advice there as soon as p₂ + p₃ > 0. At e₁, p·c = 0.
  - Pairs: (1,2), (1,3): Λ₁ ∩ R₁ⱼ = R₁ⱼ = E₁(P_j) ∩ R₁ⱼ (between model P_j). (2,1): Λ₁ ∩ Λ₂ ∩ R₁₂ = Λ⁰ ∩ Q₂, non-null
    (it contains the cone of points of (+,−,+) ∩ U with |g₂| small against g₃). (2,3): Λ⁰ = E₂(C^{23}_{s₀}) ∩ R₂₃,
    C^{23}_{s₀} = D_{co(K′∪{m})}, m ∈ (e₂, e₃), a between model. (3,j): Λ₃ = ∅ = E₃(P₃).
  - Extra clause, pair (2,3) (joint blindness null): e_θ = θ1_{M∖Λ⁰} − (1−θ); its extreme Bayes models are P₃
    (θ < ½, and E^{½,+}), C^{23}_{s₀} (θ ∈ (½, 1), E^{½,−}, E^{1,+}) and P₂ (E^{1,−}). Pairs (1,3), (3,1): e_θ = −(1−θ),
    giving P₃, and at θ = 1 also P₁. All coherent. ∎

**Consequence (PROVED).** R21's open questions for (PD), (E), (X) — Q_N1[int, overlap], Q_N1[edge], Q_N1[vtx] — have
answer Yes. Their "No" branches were the only proposed field-level routes, so **(PD), (E), (X) can be closed only by
ranking-level arguments.** The templates are the shapes a cover would have to realise: (a) three blind worlds, or
world 1 shadow-blind next to two totally blind worlds; (b) one (CA⁺) world next to two totally blind ones; (c) one
totally blind world, one L2-blind world (rigid segment Λ⁰), one additive world. (b) is the blueprint of §4.
(R21's (V0) question has the same feature: M1.1(c)'s field (0, σ₂, σ₃) passes every field test; this is why Q_N2 was
posed at ranking level.)

---

## 3. Sheltering is forced onto the blind pair

**Theorem T2n.3 (PROVED, from K3.5 [R1, K3_referee] and Q2.10(a) [R1, Q24_referee]).** Assume (H_U). Let world k be
(CA⁺): ρ_k ∈ L¹(M), ρ_k > 0 a.e., and ρ_kμ endorses every relevant world-k comparison. Let worlds i, j (the other two)
be (Loc), with any data, enlarged as in Q2.10(a) to (ρ_i, D̃^i), (ρ_j, D̃^j). Then μ(D̃^i_m ∩ D̃^j_m ∩ R_ij) > 0 for
every m.

*Proof.* Suppose μ(D̃^i_{m₀} ∩ D̃^j_{m₀} ∩ R_ij) = 0. Let Y° accept N₊, be i-correct on D̃^i_{m₀}, j-correct on
D̃^j_{m₀} (consistent: off R_ij worlds i and j agree, and on R_ij the overlap is null), and equal P_k elsewhere on M.
Apply K3.5 with D^k := ∅:
- (P1) at k: every relevant world-k comparison is endorsed ((CA⁺)). At l ∈ {i, j}: for m ≥ m₀, E_l(Y°) ∩ D̃^l_m = ∅,
  so a vector ≤ 0 on D̃^l_m ∖ E_l(Y°) = D̃^l_m is D̃^l-localized, and (Loc) (enlarged data are (Loc) data, Q2.10(a))
  endorses it.
- (P2): ρ_k is integrable; E_l(Y°) ⊆ M ∖ D̃^l_{m₀}, where ρ_l ≤ m₀ (Q2.10(a)), so ρ_l(E_l(Y°)) ≤ m₀μ(M).
- (P3): all densities are > 0 a.e., so c ≠ 0 a.e.

K3.5 then makes (H_U) contradictory, since all densities are strictly positive. ∎

**Reading.**
- A (CA⁺) world never takes part in sheltering. In an all-(Loc) cover the sheltering pair of Q2.10(c) consists of two
  worlds **neither of which is (CA⁺)**. With H1.2 (two (CA⁺) partners exclude a (Loc) world), every all-(Loc) cover
  has at least two non-(CA⁺) worlds, and if exactly two, they shelter each other on their common edge region.
- So the all-(Loc) part of (P0), (PD), (E), (X) is, by Q2.16 [R1], exactly **Q_W for the blind pair**; by Q2.10(d)
  [R1] every T1-wrong blow-up of ρ_i lies, off finite mass, inside D̃^j ∪ D̃^k, where D̃^k_m = {ρ_k > m} when one takes
  D^k = ∅ for the (CA⁺) world.
- Anti-safe points (K1.6(b)) for such a cover have both blind worlds in their support: with world k (CA⁺) one may
  take D^k = ∅, so the only conflict set is D̃^i ∩ D̃^j ∩ R_ij.

---

## 4. The positive attempt: blueprint (E∗), what is verified, and where it stops

**Blueprint (E∗).** World 1 additive with an integrable density ρ₁ > 0 (so (CA⁺)). Worlds 2 and 3 are P1-type: on
each of their edges the edge block of T2n.2 (edge {2,3}: P1 ⊕ mirror), resp. P1.10 on 𝓔₁₂ and 𝓔₁₃ (world 1 the
additive partner, λ := ρ₁μ normalised on the edge region, chain coordinate pushing λ to Lebesgue measure). Ends at
the chain ends of each edge chain (P1.18 [R1] forces this next to the additive world 1; on {2,3} it is the design).
A selection p ↦ C_p ∈ C_L, with C_{p₀} = T1, extending the three edge chains.

**4.1 Edge blocks (PROVED).** Each of the three edge blocks is a full two-world system on its edge domain 𝓔_ij:
P1.10 transfers to 𝓔₁ⱼ exactly as T2n.1 transfers to 𝓔₂₃ (T2n.2's proof), with λ = ρ₁μ. In each block both
non-additive worlds are totally blind on the edge region.

**Proposition T2n.5 (the universal fixed points of (E∗); PROVED, from Q3.20, Q3.25 [R1, Q13_referee]).** Let a ranking
satisfy (H_U), with world 1 (CA⁺) (density ρ₁ > 0) and Λ^ca_2 = Λ^ca_3 = M (as in (E∗), by 4.1 and Q3 §4 item 2). Then
for every choice of the (CA) densities (Q13_referee §2.6):
- **(a) World 1 special.** ρ^ca_2 = ρ^ca_3 = 0, so no pair with |S| ≥ 2 is forced; the forced-limit family consists of
  comparisons out of C_{e₁} = P₁, whose vectors are ≥ 0, so a maximal-support φ* has ρ♮₁ > 0 a.e. Hence
  c♮ = (ρ♮₁σ₁, 0, 0), b♮ = 2 and A(c♮) = [e₂, e₃]: configuration (E) of R21 at field level.
- **(b) World 2 special.** c♮ = (ρ^ca_1σ₁, ρ♮₂σ₂, 0) with ρ^ca_1 > 0 a.e. (ρ₁ is a (CA) density, so the maximal one
  has full support), and b♮ ≥ 1 (Λ^ca_3 = M). A(c♮) ⊆ [e₂, e₃] and e₃ ∈ A(c♮): for p with p₁ > 0, the non-null set
  (+,+,−) ∩ U ∖ cl D_{T1} (T1 rejects, worlds 1 and 2 prefer acceptance; it contains the gambles (1, 1, −c) with c
  slightly above 2c₀/(c₀ + ε)) has p·c♮ ≥ p₁ρ^ca_1 > 0, against admissibility; at e₃, p·c♮ = 0. So T1 is admissible
  at no interior weight. **(c) World 3 special:** the mirror, with A(c♮) ⊆ [e₂, e₃] and e₂ ∈ A(c♮).

*Proof.* Q3.25 gives (γ₀) and A(c♮) ≠ ∅ for every cover; the rest is the computation stated. Λ^ca_j = M forces
ρ^ca_j = 0 (Q3.20). ∎

So every fixed-point exclusion is inert on (E∗): b♮ ≥ 1 for each special world, and admissibility lives on the
boundary. With T2n.4(b) the field level offers no obstruction.

**4.2 Where the ends are, and why they shelter each other.** For the linear host edge chain on {i, l}
(C_s = U ∩ {((1−s)e_i + se_l)·g > 0}, s from 0 at P_i to 1 at P_l), world l errs at g ∈ R_il iff
s < |g_i|/(|g_i| + |g_l|). So the region that world l gets wrong only at models arbitrarily close to P_i — where a
P1-type world l puts its end — is

  𝔈^{il}_l(η) := {g ∈ R_il ∩ U : |g_i| < η|g_l|}   (η → 0).

**Proposition T2n.7 (PROVED; NUMERICS (D)).**
- **(a) Sheltering cone.** For every η ∈ (0,1): 𝔈^{12}_2(η) ∩ 𝔈^{23}_3(η) ⊇ H_η := {r(a, −b, 1) : r > 0, 0 < b < η,
  0 < a < ηb}, a non-null cone in Q₂ = R₁₂ ∩ R₂₃ (sign (+,−,+)). For η < c₀/(c₀ + ε) (c₀ = (1−ε)/3), H_η ⊆ U ∩ D_{T1}:
  T1 accepts there, so it errs at world 2 only. Mirror: 𝔈^{13}_3(η) ∩ 𝔈^{23}_2(η) contains the analogous cone around
  the e₂ ray in (+,+,−), where T1 errs at world 3 only.
- **(b) Unsheltered part.** For every η, W_η := {r(a, −1, c) : r > 0, 0 < a < η, κ < c < κ + 1} ⊆ 𝔈^{12}_2(η) ∩
  U ∩ D_{T1} is non-null, T1 errs on it at world 2 only, and W_η ∩ 𝔈^{23}_3(η′) = ∅ for η′ ≤ 1/(κ + 1).

*Proof.* (a) For g = (a, −b, 1): |g₁|/|g₂| = a/b < η and |g₂|/|g₃| = b < η. v_k·g = c₀(1 + a − b) + ε(a, −b, 1)_k ≥
c₀(1 − b) − εb > 0 for b < c₀/(c₀ + ε), so g ∈ D_{T1} ⊆ U (K′ ⊆ T1 gives P_{K′} ≥ P_{T1}). (b) v₂·g = c₀(a − 1 + c) − ε
> 0 iff c > 1 + ε/c₀ − a, and 1 + ε/c₀ = κ; the other two vertices give larger values. |g₂|/|g₃| = 1/c > 1/(κ+1). ∎

NUMERICS (D): for (ε, s) ∈ {(0.1, 0.9), (0.3, 0.9), (0.6, 0.5)} and η ∈ {0.1, 0.03, 0.01, 0.003}, all 20 000 sampled
points of H_η and of W_η lie in U ∩ D_{T1}.

*Reading.* The P1-type ends of the two blind worlds, placed where P1.18 forces them, **overlap** exactly where T2n.3
requires the blind pair to shelter: inside R₂₃, at every depth, on a cone where T1 errs at world 2 (H_η, inside world
3's end). No other pair of edge ends overlaps on R₂₃ (world 2's 23-end {|g₃| ≪ |g₂|} and world 3's 23-end
{|g₂| ≪ |g₃|} are disjoint; the 12-end of world 2 and the 13-end of world 3 overlap only on Q₁, where 2 and 3 agree).

**T2n.8 (gluing at the link class of a blind world; CHECKED, a reading of Q1.20–Q1.23 [R1 in the continuous case,
Q13_referee] and Q24_referee Lemma R1).** In (E∗) with the linear host chains and continuous bases, world 2 accepts:
its 12-cut moves (Q1.20: forced by the (RL-2) partner world 1, base ρ₁μ), and its 23-tail moves (the design of T2n.1
on 𝓔₂₃, base λ on R₂₃, the same λ for worlds 2 and 3, as competitiveness on the 23-edge needs). On world 2's link class
Q₂ = R₁₂ ∩ R₂₃ the two chain coordinates are monotone functions of |g₁|/|g₂| (x₁₂ → 1, world 2's 12-end, as
|g₁|/|g₂| → 0) and of |g₂|/|g₃| (x₂₃ → 1, world 2's 23-end, as |g₃|/|g₂| → 0); they cross transversally there ((TC)
holds as in Q1.26). Q1.22's proof uses only acceptance of the two families of cut moves, strict (G) and (IB), so it
applies at world 2:
- **(a)** ρ₁/λ = ψ(x₂₃)/φ(x₁₂) on Q₂ with φ, ψ nondecreasing, and every σ-finite endorser of world 2 is a multiple of
  ρ* := ρ₁φ(x₁₂) on R₁₂, λψ(x₂₃) on R₂₃; by Q1.23, ρ* endorses every comparison localized off world 2's chain ends.
  **So world 2 is (Loc), and (E∗) is all-(Loc)** (worlds 1 additive, 3 by the mirror argument on Q₃): T2n.3 and Q2.16
  apply.
- **(b)** On Q₂, ρ* = ρ₁φ(x₁₂) = λψ(x₂₃). Where x₁₂ stays away from 1 it is ≤ (sup φ)ρ₁, where x₂₃ stays away from 1
  it is ≤ (sup ψ)λ; both bounds are integrable. So on Q₂ the non-integrability of world 2 is confined to the corner
  where its two ends meet, around the e₂ ray, where T1 is right at world 2. In particular ρ* ≤ (sup ψ)λ on H_η and on
  W_η: on Q₂ the blind ends act **by localization, not by density blow-up**, and the sheltering on H_η is an overlap
  of localizing families (world 2's 12-end, world 3's 23-end), at a place where world 2's localizing set meets
  E₂(T1). (This is why K3.5′(b), the patch Y° = T1, does not apply: its (P1) fails at world 2 on D² ∩ E₂(T1).) World
  1's density is fixed on R₂₃ by the blind designs: ρ₁ = λψ(x₂₃)/φ(x₁₂) on Q₂ (and the mirror on Q₃); it must vanish
  along world 2's 12-end inside Q₂, away from the e₂ corner, at the rate 1/φ.
- **(c)** On R₂₃, min(ρ*₂, ρ*₃) = λ·min(ψ(x₂₃), ψ′(x₃₂)) up to constants, where x₃₂ is world 3's 23-chain coordinate
  (x₃₂ → 1 at world 3's 23-end, i.e. as x₂₃ → 0). Since ψ blows up only as x₂₃ → 1 and ψ′ only as x₂₃ → 0, the minimum is
  ≤ max(ψ(½), ψ′(½))·λ, so **the minority mass on R₂₃ is finite**: (E∗) is in the regime where T2n.9 does not apply.

This is a reading: Q1.22's measurable case and its transfer from (RL-2)-forced moves to designed moves were not
re-derived line by line here.

**4.3 Where the attempt stops.** The three edge blocks, the fixed points, the field and the sheltering geometry are
all consistent. What I could not do is define worlds 2 and 3 on models compared at **interior** indices p ∈ Δ°, so as
to get competitiveness of C_p on {1, 2, 3}, no domination, (C), closed sections in the 2-simplex for every model, and
T1 = C_{p₀}. Two facts fix the shape such a definition must have:

**Lemma T2n.6 (PROVED).** Let 𝒜 be a set of ternary vectors on M that contains every δ ≥ 0, no nonzero δ ≤ 0, and
δ₁ + δ₂ whenever δ₁, δ₂ ∈ 𝒜 and δ₁ + δ₂ is ternary (Lemma vectorform: the acceptance set of a preorder with strict (G),
(IB)). If 𝒜 ⊇ {δ : ∫δ dν ≥ 0} for a finite measure ν ~ μ, then every δ ∈ 𝒜 has ∫δ dν ≥ 0; so ν endorses every
comparison of that world and it is (CA⁺).

*Proof.* Let g = 1_Q − 1_P ∈ 𝒜 (P, Q disjoint) with ν(Q) < ν(P). Choose R ⊆ P with 0 < ν(R) ≤ ν(P) − ν(Q). Then
h := 1_{P∖R} − 1_Q has ν(h) ≥ 0, so h ∈ 𝒜, and g + h = −1_R is ternary, nonzero and ≤ 0, but accepted. ∎

So a blind world's acceptance set may contain a half-space only on the vectors relevant at one selected model, never
globally. In two worlds this is exactly what T and T′ do: on cut vectors at b, T = {λ(Q) ≥ λ(P)}, while globally
T = ⋂_t {τ(t) ≥ 0} is much smaller, which is what lets generator sums be blocked. The construction of T relies on the
relevant error sets {c_b} being **nested**. At interior indices of a three-world selection the error sets
E_k(C_p) are not nested (they form a 2-parameter family), and the analogue ⋂_q {ν(δ·1_{M∖E_kC_q}) ≥ 0} is strictly
smaller than the half-space on the vectors relevant at C_p (it is binding at indices q whose error set covers much of
δ⁺ and little of δ⁻). Competitiveness at C_p then needs world 1 to accept what both tail-like cones reject. I found
no pair of interior base cones for worlds 2, 3 that does this together with blocking, and I have no proof that none
exists. This is L2 §7.1 (i)–(v), with the additive partners of L2 replaced by the blind pair.

---

## 5. The single obstruction (where both attempts stop)

By T2n.3, Q2.16 [R1] and M0closed(a) [R2], the all-(Loc) part of a multi-blind configuration with a (CA⁺) world k is
contradictory iff (W) (equivalently (γ) for the σ-finite field) holds, and (W) can fail only through the sheltering
pair {i, j}. The argument that would prove (W) is K3.5's (equivalently K1.2's per-world form): for t with B_t
incoherent, take tests A_l close to B_t, l-safe (l-correct deep in D̃^l) and of finite cost, and use KKM on the closed
sets F_l := {p : C_p ⪯_l A_l} to find one selected C below all three; the comparisons are then localized, hence
endorsed, and C beats every coherent model. KKM needs at each index p a single competitor lying (G)-below the tests of
all worlds of supp p. Such a competitor exists at every p unless {i, j} ⊆ supp p, because the only set on which the
tests are forced apart is D̃^i ∩ D̃^j ∩ R_ij (this is K1.6(b)3, proved there for integrable base endorsers; here it is
a reading). So a cover must have **anti-safe indices** p ∈ (e_i, e_j) ∪ Δ° for every admissible triple. One regime can
be pinned down completely:

**Proposition T2n.9 (edge reduction under infinite minority mass; PROVED).** Let a ranking on M_U (n = 3) satisfy strict
(G) and (S). Let worlds i ≠ j be (Loc) with data (ρ_i, D^i), (ρ_j, D^j) (any data), and suppose
∫_{R_ij} min(ρ_i, ρ_j) dμ = ∞. Let A_i, A_j be regular models such that A_l is l-correct a.e. on D^l_a for some a and
ρ_l(E_lA_l) < ∞ (l = i, j). Then:
- **(a)** the closed sets F_l := {p ∈ [e_i, e_j] : C_p ⪯_l A_l} (l = i, j) do not cover [e_i, e_j];
- **(b)** no model X satisfies X ⪯_i A_i and X ⪯_j A_j;
- **(c)** in particular no single model is l-correct deep in D^l for both l = i, j with finite cost at both worlds.

*Proof.* (a) F_l is closed by (S). C_{e_i} is competitive on {i}, so C_{e_i} ⪯_i P_i and strict (G) give C_{e_i} = P_i,
which has no world-i errors; so C_{e_i} ⪯_i A_i by (G) and e_i ∈ F_i. Likewise e_j ∈ F_j. If F_i ∪ F_j = [e_i, e_j],
connectedness gives p ∈ F_i ∩ F_j; put C := C_p ∈ C_L. Each comparison C ⪯_l A_l is relevant, and its vector
1_{E_lA_l} − 1_{E_lC} is ≤ 0 on D^l_a, so it is D^l-localized and (E2) gives
ρ_l(E_lC ∖ E_lA_l) ≤ ρ_l(E_lA_l ∖ E_lC) < ∞. Hence ρ_l(E_lC) < ∞ for l = i, j. But on R_ij every model errs at exactly
one of i, j, so ∫_{R_ij} min(ρ_i, ρ_j) ≤ ρ_i(E_iC) + ρ_j(E_jC) < ∞, a contradiction. (b) If such an X existed, then
for every p ∈ [e_i, e_j] competitiveness of C_p on supp p ⊆ {i, j} against X gives l ∈ supp p with C_p ⪯_l X ⪯_l A_l,
so F_i ∪ F_j = [e_i, e_j], against (a). (c) is (b) with X = A_i = A_j. ∎

*Reading.*
- Under infinite minority mass the whole obstruction sits **on the edge** [e_i, e_j], and uses only the axioms (a)–(c)
  of §1 on 𝓔_ij plus localized endorsement: the third world and T1 play no role. With enlarged data, (c) forces
  D̃^i_a ∩ D̃^j_a ∩ R_ij non-null for every a (otherwise "l-correct on D̃^l_a, the cheaper advice elsewhere" is a model as
  in (c), of cost ≤ 3aμ(M) at each world), and puts all but finite minority mass inside every such overlap.
- Whether two worlds can satisfy (b) along a closed competitive edge selection is a **two-world question**; T2n.1 is not
  an instance (its ends are disjoint), and I did not decide it.
- (E∗) is **not** in this regime (T2n.8(c)): its minority mass on R₂₃ is finite, so its anti-safe indices must be
  interior or on the open edge, against tests that are not edge models.

> **Q_W (pair form; open).** In an all-(Loc) cover with a (CA⁺) world k whose other two worlds i, j shelter each other on
> R_ij (T2n.3), can every admissible triple of safe tests have an anti-safe index p with {i, j} ⊆ supp p, while the
> selection keeps closed sections?

- **No** closes the all-(Loc) part of (P0), (PD), (E), (X) with a (CA⁺) world: KKM then yields one selected model below
  all three tests, whose comparisons are localized and endorsed (K3.5 Step 1 / K1.2; in the σ-finite setting this is a
  reading, with the gap of H1.0 replaced by "finite cost" when every coherent model has infinite cost). Under infinite
  minority mass on R_ij a negative answer to the two-world question in T2n.9's reading already suffices.
- **Yes** is exactly what the interior design of (E∗) (§4.3) must supply; its edge blocks, fixed points, field and
  sheltering geometry are already in place (§4).

Covers with a world outside (Loc) (class (N), or worse than σ-finite) are reached neither by T2n.3 nor by T2n.9. For
them, after T2n.2 and T2n.4, no proved constraint distinguishes a blind pair from the two-world system T2n.1.

---

## 6. Status for R21, dependencies, what a referee should check, files

**For R21's configurations.**
- (PD), (E), (X): the field questions are Yes (T2n.4); closure needs ranking-level arguments. Edge-local ranking
  arguments cannot force (CA⁺) (T2n.2). Their all-(Loc) parts with a (CA⁺) world reduce to Q_W for the blind pair
  (T2n.3), and under infinite minority mass to an edge question (T2n.9). Open.
- (P0): untouched (L1.D, pairwise-null blind sets with c ≠ 0 a.e.).
- (S) residual: untouched beyond the observation that T2n.1's worlds satisfy (NC); Q_S♮ stands.
- T1 on M_U: not settled.

**Used** (status): P1.10a–P1.14 [R1, P1_referee]; L2.1–L2.3, C2.1(4) [R1, L23_referee]; Lemma vectorform, Theorem kkm
(write-up); K3.1, K3.5 [R1, K3_referee]; Q2.10(a), (c), (d), Q2.11, Q2.16 [R1, Q24_referee]; Q2.18 [CH]; Q3.20, Q3.21,
Q3.25 [R1, Q13_referee]; Q1.20–Q1.23 / Q24_referee Lemma R1 (reading in T2n.8 only); K1.2, K1.6 [R1] (reading in §5); N1.0(b), N2.1 [R1, N12_referee]; H1.2
[R1]; P1.18 [R1]; M0closed(a) [R2]; H12_referee §1.1 and R1 Prop. 3.1.

**Not used.** (C), (LF), T1 ∈ C_L in §§1–2 except where stated; any M1 result; L1.

**Referee priorities.**
1. T2n.0 case (ii): that "every block on every selected line has u_k < b" puts every selected source in c_b, and that a
   target block straddling b does not matter (only g_F ≥ 0 on d_b is used).
2. T2n.1 step 4: the order "R⁻ ⇒ N_X null ⇒ (T2n.0) Q null ⇒ (world-2 strictness) P null".
3. T2n.1 step 6: that P1.13 nowhere uses world 2 beyond C_L = {C_b}.
4. T2n.4(c): the four Bayes regimes of (0, σ₂1_{M∖Λ⁰}, σ₃), and B_q = C^{23}_{s₀} ∩ P₃ on the line q₂ = q₃.
5. T2n.3: the patch Y° and (P2) at the two (Loc) worlds.
6. T2n.5(b): the inadmissibility witness (+,+,−) ∩ U ∖ cl D_{T1} (non-null: it contains (1, 1, −c) for c slightly
   above 2c₀/(c₀ + ε)).
7. T2n.9(a): the vertex case p = e_i of the intersection point (then C = P_i, and the same count applies).
8. T2n.8: the transfer of Q1.22 from (RL-2)-forced cut moves to designed cut moves.

**Files** (`t2npy/`, run with `python3 -I -B` from inside it):
- `p1_cell_copy.py`: verbatim copy of `p1py/q_n2_common.py` (first docstring line marks it as a copy).
- `t2n_checks.py`, `t2n_checks.out`: NUMERICS (A) T2n.0 LP (9464 selector/cut pairs, max 0; positive control 1);
  (B) strictness LP (max 0); (C) competitiveness of C_b in the doubly blind system (3000/3000, exact); (D) the cones
  H_η, W_η of T2n.7 (all samples in U ∩ D_{T1}).
