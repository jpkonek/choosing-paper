# R21. One reduction theorem for T1: what a cover must look like, configuration by configuration

16 Oct 2026, integrator's note (round 21). No scripts. No assumption is added. Nothing here is new mathematics
except four short elementary inferences, each marked **[new]**.

**Status tags** (one per inference):
- **[R2]**: refereed independently twice.
- **[R1]**: refereed once (the named report).
- **[Rref]**: proved inside a referee report (one reader).
- **[CH]**: CHECKED (a step-by-step reading, not a re-derivation).
- **[U]**: proved in a note but **unrefereed**. N1 and N2 Part I (round 20) are [U]: `N12_referee.md` had not appeared
  when this note was finished (11:30). Every [U] tag on N1/N2 should be updated when that report appears.
- **[new]**: proved here, unrefereed.

---

## Plain-English summary (10 lines)

1. Every axiom-satisfying cover of T1 has, at each world, either a "fair price list" (an endorser) for its trades or none.
2. If some world has none, we are in configuration **(S)**, unless both partners have honest densities. In that case M2 pushes it to (V).
3. If every world has one, the price lists give one additive field. That field makes T1 optimal at some weight p*.
4. If the field is strictly positive, M0closed kills the cover. So some world must be "blind" (zero density) on a non-null set.
5. One blind world forces p* to sit exactly at that world's vertex: configuration **(V)**, in two flavours, (V0) and (V+).
6. Two or more blind worlds give four configurations, split by where p* can sit and by whether blind sets overlap: **(P0), (PD), (E), (X)**.
7. Each configuration has one open question. For (V0) it is Q_N2. For (V+) it is a three-world lift of L2. For (P0) it is Conjecture L1.D. For (PD), (E), (X) it is the field question Q_N1, restricted.
8. On two-sided decomposable domains, M3 gives the same first two cuts: the configurations (GS) and (GL). Domains that are neither M_U nor two-sided give (GnAv).
9. Additive covers, and covers whose worlds all add up, are closed everywhere this note covers. One exception: off-M_U domains without (Av), where only additive covers are closed.
10. Branches nobody has really worked on: (S), (E), (X), (PD), and everything on general domains beyond the first cut. They are flagged in §5.

---

## 1. Setting and the case variables

**Setting A (M_U).**
- n = 3 and U = D_{K′} with K′ = u + s(T1 − u).
- M is the mixed part of U. P_k = U ∩ {g_k > 0} and E_k(X) = X △ P_k.
- Q_l is the sign class with odd world l, and R_ij = Q_i ∪ Q_j.
- J_l := Q_l ∩ E_i(T1) = Q_l ∩ E_j(T1), the joint T1-error set of i and j.
- (H_U) is: strict (G), (IB), (LA), (S) with closed sections for every model, (C), and T1 ∈ C_L, on M_U. "Covered" means (H_U) holds; (LF) is automatic on M_U.

**Setting B (general domain).**
- 𝓜 is a decomposable domain with (LF) at D_{T1}.
- (H_𝓜) is (H_U) with M_U replaced by 𝓜.
- **(Av)**: a.e. mixed pair has both acceptances in its advice range.

**Case variables, in the order the tree uses them.**
1. **(NC) at world k** (K3.1(a)): no finite nonnegative combination of relevant world-k comparison vectors is ≤ −1
   a.e. on M.
   - Endorsers exist iff (NC) holds [R1, K3_referee §1.1].
   - On general domains the ladder version is used (M3.0–M3.1) [R1, M23_referee §6.1].
   - A world failing (NC) is **strongly (M1)**. By convention its blind set is Λ_k := M (K3_referee §1.3).
2. **(RL) at world j** (M2 §1): a density ρ_j > 0 a.e., with
   - (RL-1): ψ_j(C) < ψ_j(X) ⇒ C ⪯_j X;
   - (RL-2): C ⪯_j X ⇒ ψ_j(C) ≤ ψ_j(X).

   **(RL) ⇒ (NC)** **[new]**: by (RL-2), ρ_jμ/ρ_j(M) endorses every relevant comparison.
3. **The maximal fixed point.** Under (NC) at every world, fix a maximal-support endorser tuple ν* (K3.1(c)) [R1].
   - c* := (ρ*_kσ_k)_k is its countably additive field.
   - Λ_k := {ρ*_k = 0} ∩ M is the blind set, unique mod null. V_k := M ∖ Λ_k.
   - b := #{k : Λ_k non-null}.
   - World k adds up ⇔ Λ_k is null (K3.1(c)) [R1].
4. **Where p\* is.** A* := A(c*) = {p ∈ Δ : T1 is c*-p-Bayes}.
   - A* is closed and convex [R1, M1_referee §1.2].
   - A* ≠ ∅ (L4.1.3) [R1, L4_referee §1.3].
   - Vertex criterion: e_k ∈ A* ⇔ Λ_k ⊇ E_k(T1) ∩ M (M1.1(b)) [R1, M1_referee §1.2]. This is choice-free, because Λ_k does not depend on the choice of ν*.
5. **Overlaps.** Is Λ_i ∩ Λ_j null for all i ≠ j?
6. **Countably additive endorsement.** Is V_k null, i.e. do all of world k's endorsers have zero countably additive part?
7. **Edges.** On each edge {i, j}, either (Nest_e) holds or the edge selection is non-nested.

**Location trichotomy** **[new]**, elementary. A convex subset of ∂Δ lies in one closed edge. So exactly one of the
following holds:
- **(int)** A* ∩ Δ° ≠ ∅;
- **(edge)** A* ⊆ [e_i, e_j] and A* meets the open edge (e_i, e_j);
- **(vtx)** A* = {e_i}.

---

## 2. The Reduction Theorem

> **Theorem R21.**
>
> **Part A (M_U).** Let a ranking satisfy (H_U), i.e. cover T1 on M_U. Then **exactly one** of the configurations
> (S), (V0), (V+), (P0), (PD), (E), (X) below occurs. In Branch I, which configuration occurs depends on the choice of
> maximal tuple ν* only through the location of A*, and the vertex case does not depend on it. Every other branch of
> the case tree is contradictory.
>
> **Part B (general domains).** Let a ranking satisfy (H_𝓜) on a decomposable domain 𝓜 ≠ M_U with (LF) at D_{T1}.
> Then exactly one of (GS), (GnAv-nd), (GnAv-d), (GL) occurs. The remaining branch (G0) is contradictory at the
> status given in §4.
>
> **Status of the theorem.** It is as strong as its weakest input on the route to each configuration. The weakest
> inputs are:
> - for (V0) and (V+): case (II) of L4.9 [CH]; N2.3′ and N2.7(d) [U] for the structure items;
> - for (P0) and (PD): L4.1 [R1] and N1.2 / N2.3′ [U] for the structure items;
> - for (G0): M3.9 [CH, with a fixable GAP (ii)].
>
> Each configuration's *existence* as a branch rests only on [R1]/[R2] inputs and the [new] inferences of §1. Only the
> listed *structure items* and *exclusions inside* a configuration rest on [U]/[CH].

### The configurations on M_U

Each entry gives: what defines it; its proved structure, with statuses; its single open question; and what each answer does.

**(S) A strongly (M1) world with a partner that is not (RL).**
- *Definition.* Some world fails (NC), and some partner of a failing world fails (RL).
  - This includes "two or more worlds fail (NC)", since (RL) ⇒ (NC).
- *Structure.* Almost none is known.
  - If every world still satisfies (NC_{𝔇_k ∪ 𝔗_k}), the L4.1 fixed point exists (M2.7) [R1, M23_referee §5].
  - The edge tools of N1/N2 need full (NC), so they do not apply.
  - No full system with a world failing (NC) is known.
- *Open question.* **Q_S** (= Q_M2(i), sharpened by M2.6′): is there a full system on M_U (n = 3, every axiom,
  closed sections for every model, (C); T1 ∈ C_L not required) with a world failing (NC) one of whose partners
  fails (RL)?
  - **No** closes (S).
  - **Yes** does not realise (S).

**(V) One blind world, p\* at its vertex.** World 1 is blind.
- *Definition.* (V) arises from two disjoint origins:
  - Branch I: all three worlds satisfy (NC), b = 1, A* = {e₁};
  - Branch II-a: world 1 fails (NC), worlds 2 and 3 are (RL), and Λ₁ := Λ♮ is the blind set of M2's forced-limit endorser φ*.
- *Concretely.* Worlds 2 and 3 add up (ρ*₂, ρ*₃ > 0 a.e.). The structure items (V1)–(V5) are proved in N2 §6, with the sources and statuses below.
  - **(V1)** A* = {e₁}. Λ₁ ⊋ E₁(T1) ∩ M, and Λ₁ ⊇ M ∩ {g₁ > 0} ∪ (D_{T1} ∩ {g₁ < 0}). The visible set satisfies
    V₁ ⊆ {g₁ < 0} ∖ cl D_{T1}, where T1 rejects and is world-1-correct. Sources:
    - L4.3 [R1];
    - L4.7 (equality excluded) [R1], and again by N2.6(c) [U];
    - M1.2 [R1, M1_referee §2.1].
  - **(V2)** The edge models X₁₂ = D_{K₁} and X₁₃ = D_{K₀} have world-1 errors Λ₁ ∩ R₁ⱼ. They are *selected*, with
    K₁ ∩ [e₁, e₂] = {e₂} and e₃ ∈ K₀. Sources: N2.3′ [U; its input M1.3 is R1]; M1.2 [R1].
  - **(V3)** Every edge-selected model on [e₁, e_j] has world-1 errors c ⊆ Λ₁ ∩ R₁ⱼ or c ⊇ Λ₁ ∩ R₁ⱼ (N2.2) [U].
  - **(V4)** The M1.7 exchange on [e₁, e_j] is internal to Λ₁ (N2.4, N2.5(c) with θ₀ = 1) [U; M1.7 is R1].
  - **(V5)** T1 is (2, 3)-Bayes on J₂ ∪ J₃ (N2.5′) [U].
  - *Nestedness.* Under (Nest_e) on {1, j}, Λ₁ ∩ R₁ⱼ is an initial segment of the edge chain (N1.5) [U]. Without
    it, the selections cross only inside the CA tie sets (N2.2′) [U]. Neither alternative changes the configuration.
- *Split.*
  - **(V0)** V₁ is null, i.e. Λ₁ = M: world 1 has no endorser with a nonzero countably additive part.
  - **(V+)** V₁ is non-null. Then world 1 does **not** refine its countably additive veto Φ₁(X) = ∫_{X∩V₁}ρ*₁, since
    refinement is excluded by N2.7(d) [U; its inputs L3.4 R1, M1.2 R1, L4 R1].
  - With (RL) partners, as in origin II-a, world 1 is moreover not (Loc) (H1.2) [R1, H12_referee].
- *Open question for (V0).* **Q_N2**: is there a full two-world system on M_U, next to an additive world, whose
  world 1 has no countably additive endorsing part (Λ = M)? K3.3 gives such a system with every axiom except closed
  sections [R1]; L2 reaches every blind segment c_a with a < 1 [R1].
  - **Flag.** "(V0) ⇒ Q_N2 Yes" is *not proved*, for two reasons:
    1. No edge-reduction lemma turns a three-world cover into a full two-world system. Prop. Q35 gives only edge
       order structure, and only under (Nest_e).
    2. (V)'s partners add up but need not be additive.
  - The question whose **No** provably closes (V0) is its three-world form **Q_N2⁽³⁾**: does a full three-world
    system on M_U, with worlds 2 and 3 adding up, have a world 1 with (NC) and Λ₁ = M? For origin II-a, replace (NC)
    by "φ* has Λ♮ = M".
  - **Yes** to either form does not realise (V0), because T1 ∈ C_L is still required.
- *Open question for (V+).* **Q_V+** (the T1-aimed lift of L2, Q_L2): does a full three-world system on M_U, with
  worlds 2 and 3 adding up, have a world 1 with (NC) whose blind set contains M ∩ {g₁ > 0} and whose visible set is
  non-null and contained in {g₁ < 0} ∖ cl D_{T1}?
  - **No** closes (V+), because (V1) is a proved consequence of (V+).
  - **Yes** is the shape a construction must have ("L2 on each edge at e₁"; L2 itself is the two-world edge
    picture, R1). It realises (V+) only together with T1 ∈ C_L.
  - With (RL) partners it must also be non-(Loc), against the spirit of Conjecture L2.C.

**(P0) Two or more blind worlds, p\* interior, blind sets pairwise null.**
- *Definition.* (NC) at every world, b ≥ 2, A* ∩ Δ° ≠ ∅, and Λ_i ∩ Λ_j null for all i ≠ j.
- *Structure.*
  - c* ≠ 0 a.e., so every B_q is coherent (L4.1.2 with the L4_referee clause) [R1].
  - Every Λ_i is rigid: Λ_i = (E_i(C^{ij}) ∩ R_ij) ∪ (E_i(C^{ik}) ∩ R_ik), with C^{ij}, C^{ik} **selected** edge
    or vertex models. Sources: N1.3(c) and independently N2.3′(b) [both U].
  - The field-level necessary conditions of L1.D hold [R1, L1_referee §7].
- *Open question.* **CONJECTURE L1.D**, in its rigid form: no field with (γ), pairwise-null rigid blind sets as above
  and ρ_k > 0 off Λ_k has D_{T1} Bayes at an interior weight.
  - **True** closes (P0).
  - **False** (a field counterexample) does not realise (P0); it is a template.
  - Known GAP (L1_referee §7): the "verbatim" CHECKED claim needs a world-by-world bootstrap. With one blind world this is
    Theorem L1 (Q_A: No) [R1, modulo L1.7 (GAP, fixable via L1.7⁰) and L1.C (CH)].

**(PD) Two or more blind worlds, p\* interior, some overlap.**
- *Definition.* (NC) at every world, b ≥ 2, A* ∩ Δ° ≠ ∅, and Λ_i ∩ Λ_j non-null for some i ≠ j.
- *Structure.*
  - For every ordered pair (i, j), the **edge dichotomy** holds (N1.2) [U]. Either
    - **(R)**: Λ_i ∩ R_ij is the world-i error set of a *selected* edge model; or
    - **(D)**: Λ_i ∩ Λ_j ∩ R_ij is non-null, and world j is totally null on a non-null part of it.
  - Every M1.7 exchange is of type (vis), (int_i) or (int_j) (N2.4) [U].
  - Excluded inside (PD):
    - the T1-shadow c^T (three exactly shadow-blind worlds; here A = Δ) (N1.3(a), N2.6) [U];
    - every one-sided exact shadow on an edge (N2.7(a)) [U];
    - exact shadow-blindness at one world next to a partner that sees J_j ∪ J_k (M1.11) [R1].
- *Open question.* **Q_N1[int, overlap]**: is there a field c = (ρ_kσ_k) with all of the following?
  - (γ₀);
  - B_q coherent whenever c ≠ 0 a.e.;
  - A(c) ∩ Δ° ≠ ∅;
  - some Λ_i ∩ Λ_j non-null;
  - the N1.2 dichotomy on every ordered pair, with "selected" replaced by "a coherent between model D_K with
    K ∩ [e_i, e_j] ≠ ∅ and K ⊆ co(K′ ∪ [e_i, e_j])", as in K3.7′.

  **No** closes (PD) (via L4.1 [R1] and N1.2 [U]). **Yes** does not realise (PD). By M1.1′(c) [R1], no question
  about the field alone without (N1.2) can close it.

**(E) p\* forced onto an edge.**
- *Definition.* (NC) at every world, and A* ⊆ [e_i, e_j] meets the open edge (e_i, e_j).
- *Structure.*
  - Λ_i ∩ Λ_j ⊇ J_l, which is non-null (L4.3) [R1]. Hence b ≥ 2.
  - For every p* ∈ A* on the edge, with θ₀ = p*_i/(p*_i + p*_j), c_T^{ij} := E_i(T1) ∩ R_ij is θ₀-Bayes. The edge
    tie set Z_{θ₀} ∩ R_ij is non-null (N2.5(a),(c)) [U]; the joint blind set {ρ_i = ρ_j = 0} counts as ties.
  - If θ(A*) is a non-degenerate interval, then the joint blind set Λ_i ∩ Λ_j ∩ R_ij is non-null **[new, from N2.5(a) U]**.
    - Proof: the sets Z_θ ∖ {ρ_i = ρ_j = 0} are pairwise disjoint, so only countably many are non-null.
  - If the joint blind set on R_ij is null, the ties accumulate along the R_ij-arcs of some facet (N2.5(b), N2.7(c))
    [U]. Per M1_referee §5.2 this holds **per side, possibly on different facets**, and N2's "one facet, both sides"
    wording must be corrected accordingly.
- *Open question.* **Q_N1[edge]**: Q_N1 with A(c) ⊆ [e_i, e_j] meeting the open edge, Λ_i ∩ Λ_j ⊇ J_l, and non-null edge ties at
  every θ₀ ∈ θ(A).
  - **No** closes (E).
  - **Yes** gives a template only.

**(X) p\* at a vertex, with a second blind world.**
- *Definition.* (NC) at every world, A* = {e_i}, and some Λ_j (j ≠ i) is non-null.
- *Structure.*
  - Λ_i ⊇ E_i(T1) ∩ M (M1.1(b)) [R1].
  - The N1.2 dichotomy holds on every ordered pair [U].
  - On both edges at e_i, exchanges are internal to Λ_i or have jointly blind targets (N2.5(c), θ₀ = 1) [U].
  - Λ_i = E_i(T1) ∩ M is excluded wherever a partner sees E_i(T1) ∩ R_ij (N2.6) [U].
  - M1.2 does **not** apply, because it needs ρ_j, ρ_k > 0.
- *Open question.* **Q_N1[vtx]**: Q_N1 with A(c) = {e_i} and a second non-null blind set.
  - **No** closes (X).
  - **Yes** gives a template only.

### The configurations on general (LF) domains (Part B)

**(GS)** Some world fails ladder-(NC).
- *Structure.* Nothing is known. M23_referee's CONJECTURE: M2's forced KKM transfers to the ladder when the partners have positive leading ladder densities.
- *Open question.* **Q_GS**: does any full system on an (LF) decomposable domain have a world failing ladder-(NC)?
  **No** closes (GS).

**(GL)** (Av) holds, (NC) holds at every world, and the maximal ladder field is degenerate.
- *Structure.*
  - Some ladder density vanishes on a non-null subset of the ladder (M3.10, the contrapositive of the closed branch (G0)).
  - If p* lies on an edge or at a vertex, both ladder steps are jointly blind on the joint T1-error sets of the
    worlds in supp p* (M3.4(4)) [R1].
  - At every fixed point, Σ_k p*_k(w_k − s_k) ≥ 0 a.e. on T1's silent two-sided pairs [Rref, M23_referee §6.2].
- *Open question.* **Q_M3(a)**: can the maximal ladder field of a cover on an (Av) domain be degenerate?
  **No** closes (GL).
- *Remark* **[new, sketch]**. A two-sided analogue of c^T exists at field level: ladder densities that vanish on every step at which T1's advice is not rank-0, with s ≡ 0 on T1's silent pairs and w > 0 there. Its Bayes model is T1 at every q ∈ Δ°, so (γ₀) and admissibility hold everywhere.
  - So, as with M1.1′(c), (GL) cannot be closed by the field alone. It needs ladder versions of N2.1/N1.2, and no one has written them.

**(GnAv-nd)** (Av) fails, 𝓜 ≠ M_U, (NC) holds at every world, and the M3.4 field is non-degenerate.
- *Open question.* **CONJECTURE M3.C**, with the M23_referee fix: (TS), (PC), (NS) hold without (Av), or M3.9 is proved without (Av).
  **True** closes (GnAv-nd).

**(GnAv-d)** (Av) fails, 𝓜 ≠ M_U, (NC) holds at every world, and the M3.4 field is degenerate.
- **Unaddressed.** No question sharper than the configuration itself has been formulated. See §5.

---

## 3. Proof of Part A: the case tree on M_U

Each node lists its exits. "✗" means contradictory (closed), and → names a configuration.

**Node 0: (NC) at every world?**
- **No → Node II.**
- **Yes → Node I.**

**Node II (some world fails (NC)).**
- **II-a: exactly one failing world, say 1, and worlds 2 and 3 are (RL).**
  - M2.4, M2.5 and M2.6 [R1, M23_referee §§2–4] give L4's (B1) with Λ♮ in place of Λ₁, and (γ₀).
  - M2.6′ [Rref, M23_referee §4, at the standard of L4.9 and Prop. R; case (II) CH] then says: either (H_U) is
    contradictory ✗, or p* = e₁ and Λ♮ ⊋ E₁(T1) ∩ M.
  - The second alternative is **(V)**, origin II-a. The N2 structure items transfer through N2.1′ [U]. Split by
    V♮ := M ∖ Λ♮ into (V0) / (V+).
- **II-b: otherwise.** → **(S)**. This branch is exhaustive by (RL) ⇒ (NC) **[new]**.

**Node I ((NC) at every world).** L4.1 [R1] applied to the maximal tuple ν* gives c* with (γ₀) and A* ≠ ∅.
- **I.0: b = 0.** c* is strictly signed. Then A* ⊆ Δ° (H1.1 step 4) and M0closed(a) applies (L4.1.4, Cor. L4.2)
  [R1; M0closed(a) R2] ✗.
- **I.1: b = 1, say Λ₁.**
  - The (edge) location is impossible: it would need two blind worlds on J_l (L4.3) [R1].
  - (vtx) at e_j, j ≠ 1, is impossible: it would need Λ_j ⊇ E_j(T1) ∩ M, but Λ_j is null [R1, vertex criterion].
  - **(int) ✗.** Take p* ∈ A* ∩ Δ°. Then (B1) holds with ρ*₂, ρ*₃ > 0 [R1, L4_referee §4.1]. L4.9 [R1] leaves (I₂),
    (I₃) or (II). These are disposed of as follows:
    - (I) is impossible by Prop. R [Rref, L4_referee §4.2], and independently by L1.A(a) [R1, L1_referee §8];
    - (II) is excluded at CHECKED level twice: by L4 §5.4 [CH, confirmed by own re-derivation in L4_referee §5], and
      by L1.C [CH, L1_referee §6].

    So this branch is closed **at [CH]**. Upgrading it needs the source proofs listed in L4_referee §5(d).
  - **(vtx) at e₁ → (V)**, origin I. Split by V₁ into (V0) / (V+). Within (V+), refinement of Φ₁ is excluded
    (N2.7(d)) [U].
- **I.2: b ≥ 2.** Split by the location trichotomy **[new]**:
  - (int) and all Λ_i ∩ Λ_j null → **(P0)**;
  - (int) and some overlap → **(PD)**;
  - (edge) → **(E)**. Here b ≥ 2 is automatic;
  - (vtx) → **(X)**. Here b ≥ 2 by the definition of I.2.

**Mutual exclusivity.**
- The branches are separated by:
  - the (NC) pattern (Node 0, II-a/II-b);
  - b;
  - the location of A*, which is a trichotomy;
  - the overlap test;
  - V₁ null or not.
- (V)'s two origins are disjoint by the (NC) pattern.
- The configuration is a function of ν* only through A*'s non-vertex location. b, the Λ_k and the vertex case are choice-free.

**Exhaustiveness.** Every node has exhaustive exits, so every cover lands in exactly one leaf, closed or listed. ∎

## 4. Proof of Part B (general domains)

**Node 0: ladder-(NC) at every world?**
- **No → (GS).**
- **Yes →** M3.4 [R1]: the maximal ladder tuple gives ψ* with (γ₀) and T1 Bayes at some p*.

**Node A: (Av)?**
- If 𝓜 is two-sided near ∂D_{T1}, (Av) holds for every cover (L3.1(a)) [R1, L23_referee §B.1].
- **(Av) holds.**
  - **Non-degenerate field → (G0) ✗.** This is M3.10: D1 [R1] gives p* ∉ E, and M3.6–M3.8 [R1] apply. The step needs (C2), (C3) from M3.9.
    M3.9 is [CH] with GAP (ii): Thm PL with approximate walls is only sketched, and is fixable (M23_referee §6.10).
    So (G0) is closed **at [CH], pending GAP (ii)**.
    - Additive covers are closed independently by Theorem gm [three routes, each R1].
    - Rankings that add up are closed at the same [CH] status (M3.10′, via M3.5 [R1]).
  - **Degenerate field → (GL).**
- **(Av) fails.** Then 𝓜 is not two-sided near ∂D_{T1}. If 𝓜 = M_U, use Part A. Otherwise:
  - non-degenerate field → **(GnAv-nd)**;
  - degenerate field → **(GnAv-d)**.
  - Additive covers are still excluded here (Theorem gm, any (LF) domain). Rankings that add up are **not** (§5).

Exclusivity and exhaustiveness hold as in §3. ∎

## 5. Exhaustiveness check against the brief's questions, and the unaddressed branches

| Question in the brief | Where it is decided |
|---|---|
| Does each world satisfy (NC)? | Node 0. If not, then (S), or (V) via M2 |
| (RL)? | Node II only. In Branch I, (RL) partners add facts to (V) ((V6): not (Loc)) but split nothing |
| Countably additive endorser? | V_k null or not. It splits (V) into (V0)/(V+). In (P0)–(X), V_k = ∅ is allowed and splits nothing |
| Fixed point degenerate? | b ≥ 1 in every surviving M_U leaf (b = 0 ✗). On general domains: (G0) ✗ vs (GL)/(GnAv-d) |
| Where is p*? | The location trichotomy of A* |
| Blind sets pairwise null? | Splits (int) into (P0)/(PD). Under (edge) the sets cannot be pairwise null (J_l) |
| Nested edges? | Never splits a leaf. (Nest_e) adds initial-segment structure (N1.5 [U]); non-nested edges cross only on CA ties (N2.2′ [U]) |
| (M1) worlds? | With (NC), they lie in Branch I: their certificate's negative set is blind (L4.4(a)) [R1]. Strongly (M1) worlds are in Node II |
| Sheltering, ends (H2/J1/K1) | Not separate leaves. Every such cover lies in some leaf above. Answering J1.Q / J1.Q′ / K1.Q closes only its intersection with those leaves (L4.4(c)'s "sheltering = joint blindness" is interpretive, L4_referee §3) |

**Branches nobody has addressed beyond the first cut (flagged).**
1. **(S)**: strongly (M1) worlds next to a non-(RL) partner. Only M2.7 has been done there. No full system with a world failing (NC) is known.
2. **(E)**: only N2.5 / N2.7(b),(c) [U]. No dedicated analysis of edge-forced p\* exists.
3. **(X)**: vertex p\* with a second blind world. Only the generic edge tools apply (flagged already in M1_referee §6.5).
4. **(PD)**: only N1.2, the shadow exclusions and M1.11. No analysis of doubly-blind overlaps at an interior p\*.
5. **(P0)**: L1.D is a CONJECTURE. Its proof needs the bootstrap of L1_referee §7. The rigid shapes of N1.3(c)/N2.3′ are the input that L1 §6.3 asked for, but no one has run the induction.
6. **General domains.** None of the following has been done:
   - (GS);
   - (GL): no ranking-level tool exists on two-sided domains;
   - (GnAv-nd): M3.C is open, and even rankings that add up are not excluded on these domains;
   - (GnAv-d): untouched.
7. **Fixable gaps on closed branches.**
   - I.1(int) is closed only at [CH] (case (II)).
   - (G0) is closed only at [CH], with M3.9 GAP (ii).
   - L1.7 needs L1.7⁰ (L1_referee §4).
   - N2.5(b) must be restated per side (M1_referee §5.2).
8. **Not branches, but reductions that are not proved.**
   - (V0) ⇒ Q_N2 (§2).
   - The claim in N2 §6 that (V+) "is L2 on each edge" is a description, not a theorem.

## 6. Input ledger (status of every cited result)

| Input | Use | Status |
|---|---|---|
| K3.1(a)–(c) | endorsers ⇔ (NC); localization; maximal blind set; adds up ⇔ Λ null | R1 (K3_referee) |
| Thm kkm | dominators | write-up, proved |
| L4.0, L4.1 (1–4), L4.3, L4.7, L4.9 | fixed point; boundary blindness; equality case; one-blind dichotomy | R1 (L4_referee) |
| Prop. R | (I) impossible | Rref (L4_referee §4.2) |
| L1.A(a) | (I) impossible, independently | R1 (L1_referee) |
| case (II): L4 §5.4, L1.C | (II) excluded | CH (twice) |
| M0closed(a) | b = 0 ✗ | R2 |
| M1.1(b), M1.2, M1.3, M1.6, M1.7, M1.11 | vertex criterion; (V1); face KKM; Y_k incoherent; exchange | R1 (M1_referee) |
| M2.1–M2.6; M2.6′ | Node II-a | R1; M2.6′ Rref (M23_referee) |
| M3.0–M3.8, M3.10 | Part B | R1; M3.9 CH with GAP (ii) |
| L3.1(a), L3.4, L2.1/L2.4 | (Av); veto lemma; L2 | R1 (L23_referee) |
| H1.2 | (V): not (Loc) next to (RL) partners | R1 (H12_referee) |
| D1 | p* ∉ E on general domains | R1 (D1_referee) |
| Theorem gm | additive covers, every (LF) domain | three routes, R1 each |
| N1.1–N1.7, N2.1–N2.7 | edge dichotomy, rigidity, (V2)–(V5), shadow exclusions, N2.7(d) | **U** (N12_referee pending) |
| [new] items | (RL) ⇒ (NC); location trichotomy; (E) interval ⇒ joint blindness; two-sided shadow (sketch) | this note |
