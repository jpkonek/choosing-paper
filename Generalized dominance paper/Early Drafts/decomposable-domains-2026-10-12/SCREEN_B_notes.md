# SCREEN_B: exchange licensing with non-conservative rates (candidate B)

19 Oct 2026. A design screen under BRIEF_DESIGN1; it is not a results note.
- **Labels.** PROVED (a full argument is written here; one reader, me; not refereed), CHECKED (an exact rational computation, or a reading of a recorded result), CONJECTURE. No NUMERICS are used: every verdict in the scripts carries an exact certificate.
- **Scripts.** They are in `screenB_py/`. Run `python3 -I checks.py > checks.out` from that folder; it ends with `ALL CHECKS PASSED`. Every acceptance is certified by an explicit plan, and every rejection by an explicit Farkas vector. Both certificates are verified in `Fraction` arithmetic (`bmodel.verify_plan`, `bmodel.verify_farkas`). The LP solver is an exact two-phase simplex (`lpexact.py`).
- **No assumption is added.** Imports keep their recorded status.

---

## 0. Verdicts

**Headline.** With rung-decomposed types, candidate B cannot pass both (TC) and S1.
- An arbitrage cycle breaks (TC) through a **two-record pump**: X ⪯ Y ⪯ Z, with Z a pure improvement of X.
- Without an arbitrage cycle, a fixed positive potential exists. It is an additive endorser of every accepted comparison.
- The memo's minimal instance (a 4-cycle of arbitrage with no 3-cycles) therefore FAILS (TC).
- The underlying reason is **convexity**: accepted records can be added together, which is exactly what audit §3 warns against.

| Item | Verdict | Label |
|---|---|---|
| Explicit rule (§1) | given | – |
| (IB), (S7) | PASSES | PROVED |
| strict (G) | PASSES | PROVED |
| closed sections; monotone continuity (MC) | PASSES | PROVED |
| (TC), memo's instance | **FAILS**: two-record pump on 5 cells | PROVED; CHECKED |
| (TC), exact condition, rung types | TC ⟺ (N1) no cycle has rate product > 1, and (N2) every edge on a product-1 cycle has its reverse at the inverse rate | PROVED; CHECKED (random exact) |
| S1 | **FAILS whenever (TC) holds**: (N1) gives a positive potential, which is an integrable, strictly guiding additive endorser. The record-level dual gives a *fixed* finite panel of price pairs, not record-dependent potentials | PROVED |
| ties (S6) | arbitrage forces nontrivial ties. Under (TC), ties are exactly the "tight" records; equal swaps inside one type tie, so the S6 risk is the same as for additive rankings | PROVED; CHECKED |
| strict cycle lengths | under (TC): none. With arbitrage: 3-cycles that violate (TC) | PROVED; CHECKED |
| S2 | PASSES inside each connected component of E_i; there is a veto across components | PROVED |
| S3 | **not outside** the class: a finite unanimous panel of rate-adjusted judges (one-type B is LL3's margin judge) | PROVED |
| S5 | PASSES iff κ₁κ₂ ≥ 1 for the exchanges across every selected boundary point. The instance FAILS at sector boundaries; lossy self-loops fail | PROVED; CHECKED |
| Experimental target (two worlds, coherent selected models) | **impossible**: (i) for every B satisfying (TC), since there is an endorser; (ii) for every comonotone selection, including the chosen family, by LL3 Lemma B0; (iii) on M_U, for any two-world system with a B world, by Theorem MC | (i), (ii) PROVED; (iii) PROVED modulo import |
| Nearby result | certificate out of K* (selected) and a nested coherent K′, in which a cross-region exchange is K*'s only defence against a rival that world 2 rejects. The same exchanges, re-sited, form a pump | CHECKED |
| Transition types (not rung-decomposed) | pair-graph arbitrage still pumps (PROVED); the ladder triangle breaks (TC) (CHECKED). A narrow **window** exists: arbitrage only through the contradiction state keeps (TC) with no endorser, but comparisons out of coherent models cannot see it | PROVED; CHECKED |

**Overall: B is screened out.** The surviving lesson is a new screen, **S8 (convexity)**, stated in §5.

---

## 1. The rule, made explicit

**Setting (BRIEF_DESIGN1).**
- Two worlds; the full four-advice domain; problems g ∈ H = {g₁ > 0}, indexed by slope t = g₂/g₁.
- Sectors are open slope intervals, so they are cones; any type that depends only on the sector is scale-invariant. ν is the Gaussian measure of cones (angle/2π).
- World ranks:
  - unanimous sector (t > 0), both worlds: + 0, 0 1, − 2, × 3;
  - mixed sector (t < 0): world 1 ranks + 0, 0 1, − 2, × 3; world 2 ranks − 0, 0 1, + 2, × 3.
- Coherent interval models are D_[a,b] (m₁ ∈ [a,b]). On g = (1,t), D_[a,b] accepts g iff t > −α and accepts −g iff t < −β, where α = a/(1−a) and β = b/(1−b).
- The target is K* = [1/3, 2/3], so α = 1/2 and β = 2.

**Selected family (chosen).** K_s = [s − ⅔s(1−s), s + ⅔s(1−s)] for s = p₁ ∈ [0,1].
- K_{1/2} = K*, and the vertex models K₀ and K₁ are precise.
- Both endpoints are strictly increasing in s, so the family is comonotone (CHECKED).

**Items and types.**
- A record C → X is the map h ↦ (h, a_C(h), a_X(h)) on the changed set.
- At world i, a change that crosses rungs r, …, r′ (rung r lies between ranks r and r+1) is one item of size ρ_i(h)·dν per rung crossed. This is "rank steps × density".
- Its **type** (node) is n = (sector, rung). This is a sector × transition type in which E_i and κ_i see a transition only through the rungs it crosses. General transition types are treated in §2.6.
- The record has a gain vector g ∈ ℝ^N₊ (rungs crossed downwards, so X is better) and a loss vector λ ∈ ℝ^N₊.

**Rule.** World i has an exchange relation E_i ⊆ N × N and rates κ_i > 0 on E_i. An edge (n, n′) means: one unit of loss on n pays for κ_i(n, n′) units of gain on n′.
- **C ⪯_i X** ("C no worse than X") iff (g, λ)(C→X) ∈ F_i, where
  F_i := {(g, λ) : ∃ f ≥ 0 on E_i with Σ_{n′} f_{nn′} ≤ λ_n for every n, and Σ_n κ_{nn′} f_{nn′} ≥ g_{n′} for every n′}.
- In words: X's gains over C must be paid for by X's losses relative to C, with each unit of loss used at most once at its rate.
- **Strictness:** C ≺_i X iff C ⪯_i X and not X ⪯_i C. Ties are both directions.

**Instance (the memo's minimal one).**
- Sectors: U = (0,∞), S₊ = (−1/2, 0), A₂ = (−7/12, −1/2), A₁ = (−2/3, −7/12), S₀ = (−3/2, −2/3), B₂ = (−7/4, −3/2), B₁ = (−2, −7/4), S₋ = (−∞, −2).
  - A := A₁ ∪ A₂ = (−2/3, −1/2), where K* is silent and K′ := [2/5, 3/5] accepts.
  - B := B₁ ∪ B₂ = (−2, −3/2), where K* is silent and K′ accepts −g (CHECKED).
- World 1: densities ρ₁ ≡ 1, and E₁ = {self-loops at rate 1 on all 24 nodes} ∪ the 4-cycle

  (A₁,0) →¹ (B₁,1) →¹ (A₂,0) →¹ (B₂,1) →² (A₁,0).

  The rate product is 2 (arbitrage). There are no 2- or 3-cycles (CHECKED).
- World 2 (for the miniature): additive rank integral with ρ₂ ≡ 1. This is B with the complete graph and all rates 1.

---

## 2. Design checks

### 2.1 Lemma 1 (PROVED): IB, strict (G), cone structure

- F_i is a closed convex polyhedral cone (the projection of a polyhedral cone).
- F_i is monotone: if (g, λ) ∈ F_i, g′ ≤ g and λ′ ≥ λ, then (g′, λ′) ∈ F_i.
- **(IB) and (S7):** the verdict depends only on the record's type masses. It never depends on shared advice or on coherence of the base.
- **Strict (G):**
  - If X is at least as good as C a.e., the record X → C has no gains, so X ⪯ C.
  - If X is moreover strictly better on a non-null set, the record C → X has gains and no losses, and ρ_i > 0, so C ⋠ X.

### 2.2 Lemma 2 (PROVED): closed sections and (MC)

- Let ρ_i be integrable and p ↦ C_p continuous in measure. Each type mass of C_p → X changes by at most 3∫_{C_p Δ C_{p′}} ρ_i, so (g, λ)(C_p → X) is continuous in p. Since F_i is closed, {p : C_p ⪯_i X} is closed for every model X.
- The same argument with monotone convergence gives the write-up's (MC_i) for every B world.

### 2.3 Theorem 3 (exact (TC) condition, rung types; PROVED, CHECKED)

**Hypotheses.** Finite N, ρ_i > 0, every sector non-null, the full domain. Then (TC) holds at world i iff:
- **(N1)** every directed cycle of (E_i, κ_i), self-loops included, has rate product ≤ 1; and
- **(N2)** every edge (n, n′) that lies on a cycle of product exactly 1 has its reverse (n′, n) ∈ E_i, with κ(n′, n) = 1/κ(n, n′).

*(N1) is necessary: the two-record pump.*
- Take a cycle with product P > 1. If its length is odd, walk it twice.
- Colour the walk's edges alternately 1, 2. Give position t its own cell in its node's sector, with mass x_t = κ(e_t)x_{t−1}, starting from x₀ = 1.
- On position-t cells the move is high → low in the record of e_t's colour and low → high in the record of e_{t+1}'s colour. The start cell is low → high in record 1 and back in record 2. An extra cell of mass x_W − 1 at the start node moves high → low in record 2 only.
- Record c pays each of its gains through its own edges, so X ⪯ Y (record 1) and Y ⪯ Z (record 2).
- Z equals X except on the extra cell, where it is better. So Z ≺ X by strict (G), and (TC) fails.
- CHECKED:
  - on the instance: 5 cells, masses 1, 1, 1, 1 and an extra cell of mass 1;
  - on 25 random cycles of lengths 1 to 5: all 25 pumped.

*(N2) is necessary: a three-record construction.*
- Take an edge e = (n, n′) on a simple product-1 cycle of length ≥ 3. Colour e with 3 and the rest of the cycle alternately 1, 2. Masses are forced along the cycle.
- Every record pays its gains through its own edges, so X ⪯ Y ⪯ Z ⪯ X.
- X → Z is the reverse of the colour-3 record: a gain on n of mass 1 and a loss on n′ of mass κ(n, n′). It is feasible only through (n′, n), with κ(n′, n) ≥ 1/κ(n, n′). By (N1), equality must hold.
- CHECKED:
  - the conservative 4-cycle without reverses fails (TC); with exact reverses it does not;
  - 20 random tight cycles, each with one deficient reverse, all fail.

*Sufficiency.*
- By (N1) there is a potential ψ = log φ with φ_{n′}κ(n, n′) ≤ φ_n on E_i (no positive cycles, so longest paths are finite).
- Raising the weight of any single edge that lies on no product-1 cycle by a small ε keeps all cycles nonpositive. So each such edge has a potential that is strict on it. Averaging these potentials (in log space) gives one φ > 0 that is strict on every edge not lying on a product-1 cycle.
- For an accepted record with plan f:

  φ·λ − φ·g ≥ Σ_e f_e(φ_n − κ_eφ_{n′}) ≥ 0.

  So L^φ(X) := ∫ Σ_{r<rank_X(h)} φ_{(k(h),r)} ρ_i dν satisfies L^φ(C) ≤ L^φ(X).
- Suppose X ⪯ Y ⪯ Z ⪯ X. The three L^φ-differences sum to 0, so each is 0, and every inequality in the chain is tight:
  - every plan edge is tight, hence lies on a product-1 cycle;
  - every loss is used, and every gain is covered exactly.
- By (N2) the reversed plan f′_{n′n} := κ(n, n′)f_{nn′} pays the reversed record. So X ⪯ Z.
- CHECKED: in 80 random (N1)+(N2) worlds, 3172 chains X ⪯ Y ⪯ Z were tested, of which 324 have Z ⪯ X. There were no (TC) violations.

**Corollary 4 (the dichotomy; PROVED).** At every world exactly one of the following holds.
- Some cycle has rate product > 1. Then (TC) fails, through a two-record pump.
- No cycle has rate product > 1. Then a fixed φ ≫ 0 gives an integrable, strictly guiding additive loss L^φ that endorses **every** accepted comparison: S1 fails, there is no certificate of any kind, and the world adds up.

**Strict cycles (PROVED).** The tightness argument applies to cycles of any length. So under (TC), every cycle of acceptances consists of ties: there are no strict cycles. With arbitrage, the pump gives 3-cycles X ⪯ Y ⪯ Z ⪯ X with Z ≺ X.

### 2.4 Lemma 5 (the convexity pump; PROVED). This is the general form behind Corollary 4

**Statement.** Let any rule accept C ⪯_i X iff the record's rung-type mass vector lies in a polyhedral convex cone F. Then either some φ ≫ 0 endorses every accepted record, or (TC) fails.

*Proof.*
- V := {λ − g : (g, λ) ∈ F} is finitely generated. By Stiemke's alternative, either some φ ≫ 0 has φ·v ≥ 0 on V, which is an endorser, or some accepted record R has λ ≤ g, λ ≠ g.
- In the second case, use R twice. Re-site it by single-rung moves; this is legitimate because the verdict depends only on type masses.
  - Place record 2's losses on record 1's gain cells. This is possible since λ_n ≤ g_n for each node.
  - Place record 2's gains on record 1's loss cells, and put the surplus on fresh cells.
- Then X ⪯ Y ⪯ Z, and Z is a pure improvement of X. ∎

Quorum rules (LL3) escape Lemma 5 only because their acceptance set is a **union** of cones, not a convex cone.

### 2.5 Ties (S6)

- **Arbitrage forces nontrivial ties (PROVED for even cycles; CHECKED on the instance).**
  - Colour the cycle 1, 2. The record C → X uses the colour-1 exchanges, and X → C uses the colour-2 exchanges. Both are feasible iff P ≥ 1.
  - Instance: C = (+, −, +, −) and X = silence on cells of mass 2 in A₁, B₁, A₂, B₂. Then C ~₁ X.
- **Under (TC) (PROVED).** C ~_i X iff the record is L^φ-neutral and both plans use tight edges only.
  - The self-loops of rate 1, which S5 needs, make equal-ρ_i swaps inside one node ties.
  - A double tie with an incoherent swap needs ρ₁(G) = ρ₁(L) and ρ₂(G) = ρ₂(L) on the two sides of a selected boundary inside one sector.
  - Exactly as for additive rankings, this is excluded iff ρ₁/ρ₂ separates the two sides. So S6 is no worse than for additive rankings, and no better.

### 2.6 General transition types (types = sector × (old, new), not rung-decomposed)

- **The pump on the pair graph (PROVED).** Make the nodes unordered pairs {a, b} per sector. Every cycle in this graph with product > 1 pumps, by the same two-record construction: cells move a ↔ b.
- **The ladder triangle (CHECKED).** One sector at world 1, with ranks 0, 1, 2.
  - Losses 0→1 and 1→2 pay the gain 2→0, both at rate κ ∈ {1, 3/2}.
  - Three cells carry the rotations of 0 → 1 → 2 → 0, which gives X ⪯ Y ⪯ Z ⪯ X. But X → Z consists of single-rung gains that are not payable. So (TC) fails.
  - This holds with or without reverse edges 2-rung loss → 1-rung gain at rate r ≤ 2/3. If r > 2/3, the pair graph has product κr > 1 and pumps.
  - At κ = 3/2 no ladder-consistent potential exists, so (TC) fails for every choice of r.
- **CONJECTURE B.1.** For transition types on a three-state ladder, (TC) forces a ladder-consistent positive potential, as for rung types.

### 2.7 The four-state window (PROVED; CHECKED)

**Definition.** Let E consist only of edges from every one-rung loss type to the gain type × → + (3 → 0) of any sector, at rate κ ∈ (1, 3).

**Claim: (TC) holds.**
- Accepted records have only 3 → 0 gains. A 3-step pointwise loop with one 3 → 0 step therefore has at most one one-rung rise.
- So, over a 3-cycle, the paying-loss mass P is at most the gain mass G.
- Acceptance gives 3G_k ≤ κP_k for each record k. Summing, 3G ≤ κP ≤ κG, so G = 0 and the cycle is trivial.

**Claim: no endorser, but strict 4-cycles.**
- A 4-record certificate exists: a 0 → 1 → 2 → 3 → 0 loop per point, with surplus on one extra cell.
- There are strict 4-cycles and no nontrivial ties.
- The window closes exactly at κ = 3, where a 3-cycle through 0 → 1 → 3 → 0 violates (TC). CHECKED: random exact tests, the explicit 4-cycle, the certificate, and both thresholds.

**Why it is useless here (PROVED).**
- In a certificate built from comparisons out of coherent bases, no base is ever ×. An arc into × would make the pointwise level-3 tail positive. So arcs touching × never occur, and the window's exchanges are never used.
- Comparisons out of coherent models are judged by the remaining edges alone. Hence the window gives non-additivity only on comparisons that do not matter for the programme.

---

## 3. Screens

- **S1 (accounting identity). FAILS under (TC)** (Corollary 4).
  - With the instance's arbitrage, no potential exists. The LP {φ ≥ 1, κφ_{n′} ≤ φ_n} is infeasible, with the cycle as Farkas certificate (CHECKED).
  - The certificate of §4 defeats every strictly guiding additive loss (CHECKED). But then (TC) fails.
  - **Record-level dual (PROVED, Farkas).** F_i = {(g, λ) : v·g ≤ u·λ for every (u, v) in P_i}, where P_i := {u, v ≥ 0 : κ(n, n′)v_{n′} ≤ u_n on E_i}.
    - P_i is fixed. So B is the unanimity of the finitely many extreme price pairs (u, v): asymmetric judges that price gains and losses differently.
    - The duals are **not** record-dependent potentials; only which judge binds depends on the record.
    - A potential is a symmetric point (φ, φ) of P_i. Arbitrage is exactly the absence of one.
- **S2 (product obstruction). PASSES within components.**
  - Plans pair gains in one sector with losses in another; §4's defence uses this essentially (CHECKED: a region-by-region test rejects it).
  - Feasibility factorises over connected components of E_i, so the product obstruction returns across components.
- **S3 (finite statistics). Not outside the class.** With finitely many sectors, B is a function of finitely many record integrals. It is a unanimous panel of fixed rate-adjusted judges u·λ − v·g ≥ 0; a one-type B with rate r is exactly LL3's margin judge I ≤ rW. Only a continuum of types could leave the class, and Lemma 5's pump does not depend on the number of types once a single net-improving accepted record exists.
- **S5 (swap rival). Conditional.**
  - Take a small swap: G with silence → + and L with + → silence, on the two sides of a selected boundary inside nodes n_G, n_L.
  - World 1 accepts iff ρ₁(G) ≤ κ₁(n_L, n_G)ρ₁(L). World 2 accepts iff ρ₂(L) ≤ κ₂(n_G, n_L)ρ₂(G).
  - With ρ₁/ρ₂ locally constant, every small swap is defended iff κ₁κ₂ ≥ 1, and by sign alone iff κ₁κ₂ = 1 (PROVED). Lossy self-loops (κ < 1) therefore fail S5.
  - In the instance, a swap across the A₁ | A₂ boundary is defended by neither world, since E₁ has no A₂ → A₁ edge (CHECKED). A continuous selection passes every sector boundary.
  - Adding the conservative edges A₁ ↔ A₂ that repair this creates 3-cycles with the arbitrage cycle; it pumps anyway.
- **S6.** See §2.5. **S7.** PASSES (Lemma 1).

---

## 4. The experimental target in miniature

**(i) Impossible for every B that satisfies (TC) (PROVED).** Corollary 4: φ endorses every accepted comparison, and a certificate would defeat φ.

**(ii) Impossible out of selected models of any comonotone family (PROVED).**
- Two interval models cross at a world iff they are strictly nested. This is CHECKED on all 66 × 66 grid pairs; it is the lattice of write-up Prop. lattice.
- In a comonotone family the selected models are pointwise ordered at both worlds. Then LL3 Lemma B0 (certificates need two bases that cross at the world) excludes any certificate, for every strictly guiding rule. The chosen family is comonotone.

**(iii) Comonotone selection is forced (PROVED on M_U modulo import).**
- Every B world is (MC_i) (Lemma 2). By the write-up's Theorem MC (refereed once; its inputs are strict (G), (IB), (LA), (S), (C), with no (TC)), any two-world system on M_U with every axiom and one B world has a nested C_L. Then (ii) applies.
- On the full four-advice domain the transfer is not re-derived: CONJECTURE. The splice structure between nested intervals is the same, with two advice states on each of A and B.
- **This bears on audit §4 itself:** a two-world miniature needs a crossing in C_L, hence both worlds non-(MC) and without leading charges (write-up Cor. MC(b)).

**Nearby result (CHECKED, `checks.out` §6).** Use the instance, with world 2 additive. The bases are K* (selected) and the nested coherent K′ = [2/5, 3/5]. Masses are in units of a small scale s.

| record | base → rival | world-1 type masses | plan |
|---|---|---|---|
| R*₁ | K* → X₁: + on a₂ (A₂, 6), − on b₁ (B₁, 8) | gain (A₂,0) 6; loss (B₁,1) 8 | B₁ → A₂ |
| R*₂ | K* → X₂: + on a₁ (A₁, 10), − on b₂ (B₂, 5) | gain (A₁,0) 10; loss (B₂,1) 5 | B₂ → A₁ at rate 2 |
| R′₁ | K′ → silence on a₁ₓ (8 of a₁), b₁ | loss (A₁,0) 8; gain (B₁,1) 8 | A₁ → B₁ |
| R′₂ | K′ → silence on a₂, b₂ | loss (A₂,0) 6; gain (B₂,1) 5 | A₂ → B₂ |

- **All four records are accepted at world 1.** Their pointwise sum is worsening-free and nonzero: + replaces silence on a₁ \ a₁ₓ (mass 2). So it is a certificate, and no strictly guiding additive loss endorses world 1.
- **The essential defence.**
  - K* ≺₁ X₁ strictly: the reverse needs an A₂ → B₁ exchange, which E₁ lacks.
  - World 2 rejects: X₁ ≺₂ K*, with world-2 gain 8 against loss 6.
  - So K*'s only defence against X₁ is world 1's cross-region exchange B₁ → A₂. A region-by-region world 1 would reject it.
- **Convexity cost (PROVED for rung types).** Merge the K*-records of a certificate out of two crossing bases, scaled and re-sited. The merged rival is tied with K* at world 1:
  - the K′-records' merged vector is in F;
  - the reversed K*-merge has fewer gains and more losses (pointwise cancellation, node by node);
  - so it is accepted by monotonicity.
  - Hence, with an additive partner, **not every K*-record can be essential**, or the merged rival would dominate K*. Here R*₂ is defended by world 2 (K* ≺₂ X₂), and the merged rival is tied at world 1 and worse at world 2 (CHECKED).
- **But the same exchanges, re-sited out of incoherent bases, form a pump at world 1:** X ⪯₁ Y ⪯₁ Z with Z a pure improvement (CHECKED). So no full system contains this world. The arbitrage that supplies the certificate is the arbitrage that breaks (TC).

---

## 5. What survives, and the proposed shift

**The impossibility is narrow and has an exact cause: convex acceptance (Lemma 5).**
- With rung types, convexity plus a certificate gives a two-record pump.
- With transition types, loops of length 4 (only through ×) are TC-safe. But they are invisible from coherent bases (§2.7), and the three-state case is CONJECTURE B.1.

**Proposed screen S8 (convexity).**
- A rule whose acceptance region in finitely many type masses is a convex cone either adds up or violates (TC), up to CONJECTURE B.1 for multi-rung types.
- So a viable rule must refuse to add accepted patterns. This is audit §3's "two justified patterns need not justify their numerical sum".

**Nearby reachable design.** Make B non-convex: accept iff the gains can be paid under at least q of n exchange systems (E^v, κ^v), each conservative.
- Each conservative system is a margin-type judge with a potential.
- So this is the quorum/super-majority line (candidate A, LL3). It has a certificate out of crossing coherent models above LL3's spread threshold M\*, and (TC) iff the Nakamura number is ≥ 4.
- B adds nothing beyond A. Its exchange graphs are just a convenient way to specify judges whose increments vary by sector.

**For the experimental target,** combine §4(ii)–(iii) with write-up Cor. MC(b). In two worlds, at least one comparison in a certificate must come out of a coherent model that is not selected, unless both worlds lack (MC) and leading charges. The informative miniature therefore lives in three worlds, where interior selected models cross, or uses non-(MC) worlds in two worlds.

---

## 6. Status

| # | Statement | Label |
|---|---|---|
| L1, L2 | IB, strict (G), cone structure; closed sections; (MC_i) | PROVED |
| Thm 3 | (TC) ⟺ (N1) ∧ (N2) for rung types | PROVED; CHECKED (pumps 25/25, N2-failures 20/20, 3172 random chains) |
| Cor 4 | arbitrage ⟹ pump; no arbitrage ⟹ additive endorser | PROVED |
| L5 | convex cone + no endorser ⟹ two-record pump | PROVED |
| §1 instance | memo's 4-cycle fails (TC) | CHECKED |
| §2.5 | arbitrage ties; ties under (TC) | PROVED; CHECKED |
| §2.6 | pair-graph pump; ladder triangle | PROVED; CHECKED |
| B.1 | (TC) ⟹ ladder-consistent potential (three states, transition types) | CONJECTURE |
| §2.7 | four-state window: (TC), no endorser, strict 4-cycles, no ties; κ < 3 sharp; invisible from coherent bases | PROVED; CHECKED |
| S1 dual | fixed price-pair panel | PROVED |
| S5 | κ₁κ₂ ≥ 1 criterion; instance fails at sector boundaries | PROVED; CHECKED |
| §4 (i), (ii) | target impossible under (TC); impossible for comonotone selections | PROVED (B0 imported from LL3, author-proved) |
| §4 (iii) | B world forces nested C_L on M_U | PROVED modulo Thm MC (refereed once); full-domain transfer CONJECTURE |
| §4 nearby | certificate out of K*, K′ with essential cross-region defence; merged-rival tie; pump | CHECKED; tie lemma PROVED |

## Files (`screenB_py/`)

- `lpexact.py`: exact two-phase simplex.
- `bmodel.py`: cells, rung-type B worlds, plan and Farkas certificates with exact verification, interval models.
- `checks.py` → `checks.out`: §§1–11 of the checks referenced above.
