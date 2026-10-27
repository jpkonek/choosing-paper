# PP53. Adversary on the posterior-gate programme: the boundary, global prices, and the reduction

23 October 2026. Task PP53 of Brief 52. One reader (me); not refereed.

**Labels.** PROVED: a complete argument is given here, or a cited result is named with its status. CHECKED: an exact rational computation in `r9/PP53_py/`; every output ends ALL PASS. Floating-point LPs and MILPs only *propose* solutions; Fractions verify them. NUMERICS: none is used. CONJECTURE / OPEN: as stated.

**Inputs.** BRIEF52. AUDIT_round52, AUDIT_posterior_pairs and AUDIT_round52_answers, all binding. PP42, REFEREE_round50 (Thm R1, Lemma S), PP45, PP46, PP47 (Lemma 1.3, Thm 2.5, Thm 4.1), LEAD_selection_count, AUDIT_completion, REFEREE_PP32_penalties (Thm A, Cor A′), PP12, REFEREE_round46 (R46.1), PP38, DESIGN_MEMO §8.11 and §8.20, and FF2 Thm 4.1. During the task the coordinator relayed PP49 (the consolidated sufficiency theorem). I use PP49's conventions and treat its Theorem A as the reduction under test (§4).

**Conventions** (as in PP49 §1).
- Gates are zero-accepting gate unions (R0): a record is accepted at w if it is guidance, or if some C_b realises it and has gate value ≥ 0.
- Pair constants are written z_NM = log(c_N/c_M). On D_NM, CG2 reads z_NM ≤ log(f^M/f^N) where the move N → M worsens world w, and z_NM ≥ log(f^M/f^N) where it improves w.
- I^w_NM is the resulting closed interval of feasible z_NM.

---

## 0. Verdict

**1. The boundary is not where this programme fails.**
- **Supports are forced.** Every posterior index a has supp λ_a = supp a (Lemma 2.1; PROVED; CHECKED).
- **Every pair can be made compatible.** For every pair of indices on the closed simplex, there are fields that make both members own-Bayes, edge and vertex weights included, and that satisfy strict CG2 at all three worlds (Prop 2.2; PROVED).
- **A joint boundary module exists (Prop 2.3; CHECKED).** The module is {T, an interior model near the edge, two models on edge [e₁,e₂], one model on edge [e₁,e₃], V₁, V₂, V₃}. Its fields give:
  - strict own-Bayes, with each edge model at its edge weight;
  - strict CG2 for every pair;
  - strict CG3 for every triple. By PP49 Lemma 3.4(ii) this gives (H3), including at the three-valued points, which really occur.
- **The answer to the brief's question is yes.** At the level of finite modules, edge models can be uniquely Bayes at edge weights while compatible with nearby interior models, with T, with other edge models and with the vertices.

**2. Sections at the boundary close under PP49 Prop 4.3, which I checked. Three refinements are needed (§2.4).**
- **(a) Normalisation.** (H4)(b) should be read modulo a positive factor per index and per world. Gate verdicts do not change under such factors (PROVED). Without this reading, the raw transported field fails (H0) in the limit at every edge, because its world-3 part tends to 0.
- **(b) Degenerate limits.** A gate whose normalised limit field is degenerate breaks strict (G) at once under (R0). Replacing that gate breaks (H4)(b).
- **(c) Vertices.** With per-world normalisation, the transported design is continuous at the edges but **not at the vertices**. Its world-2 field on M₃ near e₁ depends on the direction b₃/b₂, and the dependence is not a constant factor (CHECKED). This is a failure of **a chosen design**. In general it is a stated obligation: the normalised fields must converge at each vertex.

**3. "No global prices" cannot be killed. The four-model target is achieved exactly (Thm 3.3; CHECKED).**
- **The models.** A = T together with B, C, D, at indices (11,10,9)/30, (11,11,8)/30 and (10,11,9)/30. Their credal sets pairwise overlap, so the family is two-valued.
- **What the fields deliver.** Piecewise-constant fields on the 28 point types, all of which occur, give:
  - strict pointwise own-Bayes;
  - nondegenerate strict CG2 intervals for all six pairs at all three worlds;
  - every triple passes PP47 Thm 4.1 with strict slack, so (TC) holds under (R0);
  - **no global constants at world 1** (and also at world 2). The cycle A→B→C→D→A has total upper bound −0.2 in log units.
- **A second certificate imposes λ_N = index** (which the audit does not require). It also passes.
- **Why both levers fail.**
  - The type layer is indeed a global coboundary on the closed simplex (§3.2).
  - But own-Bayes is invariant under pointwise rescaling, so it cannot pin interval positions (Lemma 3.1).
- **What escapes is exactly the freedom of the fields type by type.** Combined with PP49 Thm N, the four-model pattern is not only achievable but **necessary** at some world.

**4. Two new necessary conditions for extending the target to the whole simplex (§3.4).**
- **Width budget (Lemma 3.4; PROVED).** Take a cycle whose upper bounds sum to −Γ < 0. Every further member F that is two-valued with the cycle members must have pair intervals to them whose widths sum to at least Γ. This holds for every such F in the whole family, vertex gates at other worlds included.
- **Spectator constraints at three-valued points (Lemma 3.5; PROVED).** PP49's (H3) needs each member to compare its valuation of a step between the *other two* members' advice. Pair conditions do not supply this. Common-shape fields are exactly tight there. On triples where both rank orders occur, which happens for (T, C_b, E) at worlds 1 and 2 (CHECKED), tightness has to be broken by a deliberate humility.
- The four-model certificate is two-valued, so it does not test either condition.

**5. The reduction (PP49 Thm A): no gap found (§4).** I checked:
- strict links;
- the (TC) case split;
- the enumeration of link vectors;
- the projection proof of closed sections;
- KKM, which gives strict dominance at every world;
- competitiveness on edge supports;
- direct (C).

Two small sharpenings, both PROVED:
- (H4)(b) holds modulo normalisation, as in item 2(a).
- Given its first clause, PP49 Lemma 3.4(i) is **exact**. So at three-valued points the only open question is whether κ can be taken positive (PP49 Gap 3).

| Item | Result | Source of any failure | Label |
|---|---|---|---|
| supp λ_a = supp a forced | Lemma 2.1 | axioms (competitiveness) | PROVED; CHECKED |
| every boundary pair compatible | Prop 2.2 | — | PROVED |
| joint boundary module (edges at edge weights, vertices, three-valued points) | Prop 2.3 | — | CHECKED |
| (H4)(b) modulo normalisation; degenerate limits | Prop 2.4 | — | PROVED |
| transported fields at the boundary: (H0) at edges (raw), (H4)(b) at vertices (normalised) | Prop 2.5 | **chosen design** | PROVED; CHECKED |
| pointwise rescaling invariance; no Bayes-forced positions | Lemma 3.1 | — | PROVED |
| inconsistent cycles need a two-signed pair | Lemma 3.2 | — | PROVED |
| four-model target achieved (free λ; λ = index) | Thm 3.3 | — | CHECKED |
| width budget for every further member | Lemma 3.4 | architecture (triple-local (TC)) | PROVED |
| spectator constraints; common-shape tightness | Lemma 3.5 | architecture | PROVED; orders CHECKED |
| PP49 Thm A, Thm N | §4 | — | checked; no gap |

---

## 1. What the brief asked, and how the answers fit together

The brief poses three attacks: on the boundary, on global prices, and on the reduction. The coordinator's relay of PP49 changes their weight.
- PP49 Thm N proves, modulo FF2's import chain, that every (H0)–(H5) solution lacks a global witness at some world. So a proof that "global prices always exist" would not merely kill the four-model target. It would kill **the whole posterior gate architecture**.
- That raised the stakes of attack 2, and I pursued it to an exact answer. It fails, with an explicit certificate.
- The boundary attack also fails at the finite level. What survives from it are concrete obligations on continuity at the vertices.

The remaining risk is in the continuum, and §3.4 states the two conditions any continuum must meet.

---

## 2. The boundary

### 2.1 Supports

**Lemma 2.1 (supp λ_a = supp a; PROVED; CHECKED `boundary_supports.out`).** Every C_a that is weakly own-Bayes at some λ_a with supp λ_a ⊆ supp a (PP49 (H1), forced by PP47 Lemma 1.2) has supp λ_a = supp a.

*Proof.* For each w ∈ supp a, C_a gives, on an open cone, an answer that is correct at w only:
- for interior a, the minority answer on M_w;
- for an edge a = (a₁, a₂, 0), the answer "accept −h" on M_w, where w ∈ {1, 2}, for odds h_j/|h_w| below the strip.

If λ_{a,w} = 0, that answer is wrong at every world of supp λ_a. It is then strictly worse than silence for every strictly guiding field, which contradicts weak Bayes. Exact witnesses with strict margins exist for 8 indices: interior, all three edges, and skew points (`boundary_supports.out`).

Edge models never answer "correct only at the off-support world". So nothing forces weight there. ∎

*Consequence.* On the closed simplex the extended pair-ordering certificate D = log(a/b) (PP49 Prop 5.2) agrees, world by world, with the type-lemma vector D_w = log(λ^a_w/λ^b_w) − z_w for the coboundary choice z_ab,w = (log λ^a_w − log a_w) − (log λ^b_w − log b_w). This holds wherever these are finite. Worlds with a_w = 0 < b_w give −∞ on both sides. So the type layer of PP45 and PP46 is a **global coboundary on the closed simplex**.

### 2.2 Pairs

**Proposition 2.2 (every boundary pair can be made compatible; PROVED).** Let a ≠ b ∈ Δ, with weights as in Lemma 2.1. Then there are strictly guiding fields with integrable envelope such that:
- C_a and C_b are strict pointwise own-Bayes optima;
- the pair satisfies strict CG2 at all three worlds.

Edges, vertices and opposite answers are all included.

*Proof.*
1. **The certificate.** Take the coboundary constants of §2.1. At each disagreement type (W, R), Prop 5.2 gives w* ∈ W′ and r* ∈ R′ with D_{w*} > D_{r*}.
2. **Old side.** Choose |f^a| to put weight 1 on w*, weight s < 1 on r*, and a small weight η₀ elsewhere. Then λ^a·f^a > 0.
3. **New side.** Put b_x := λ^b_x|f^b_x| equal to e^{−D_x}(1 ± η)·a_x, choosing (1 + η) on W and (1 − η) on R. This is strict CG2 at every world with constant z.
4. **Bayes for C_b.** λ^b·f^b < 0 holds once s is close to 1 and η, η₀ are small, because e^{−D_{w*}} < e^{−D_{r*}}.
5. **Zero-weight worlds.**
   - If λ^a_x = 0 < λ^b_x, take |f^a_x| tiny; the CG2 inequality then holds at once.
   - If both weights vanish at x, set f^b_x := e^{z_x}f^a_x(1 ± η).
6. **The other advice values.** Make contradiction, and any advice absent from the type, expensive.
7. **Measurability.** The fields are |g| times constants on each type cone. ∎

*Remarks.*
- **(T, E) at the midpoint edge.** Take E = C_{(1/2,1/2,0)} and λ^E₃ = 0, so D₃ = +∞. On every disagreement of T and E, world 3 lies in W. (E answers "accept h" on M₃, and E silent or "accept −h" against T's answer on M₁ and M₂ makes world 3 worse.) So the pair (T, E) imposes **no** type constraint at all. For κ = a₁/a₂ ≠ 1, exactly one constraint appears: D₁ > D₂ if κ < 1, and the reverse if κ > 1.
- **Cited constraints.**
  - Cor A′ of REFEREE_PP32 holds for every posterior edge model: its window [κ/L, κL] always reaches an end of the band, with equality at κ = 1, which is ℓ^T's sharp case.
  - Its mechanism (Theorem A: one field endorsing both T's fills and the edge comparisons) does not pass through CG2, by the remark above.
  - PP32 Lemma 2.2 (edge KKM) holds, since the windows cover all odds.
  - R46.1 is not triggered, since posterior edge models are imprecise and so the edge selection is not vertex-valued.
  - PP38's test case D_{(1/2,1/2,0)} is a precise edge model, which this family never selects.

### 2.3 A joint boundary module, three-valued points included

**Proposition 2.3 (CHECKED `boundary_module.out`).** The module 𝓜 consists of:
- T;
- N_b = C_{(9,9,2)/20};
- E = C_{(1,1,0)/2} and E₂ = C_{(2,1,0)/3};
- F = C_{(1,0,1)/2};
- V₁, V₂, V₃.

Put μ_N := the index of N, so μ_E = (1/2, 1/2, 0) and μ_{V_i} = e_i. The superset of admissible point types is every advice vector allowed by PP49 Prop 5.2 for every disagreeing pair and by the vertices' forced advice; it has 148 types. On every one of these types there is a local potential U(g, ·), strictly increasing in rank at each world, at which **every** member's advice is the strict μ_N-optimum.

Hence the humble fields ℓ^N_w := U_w with increments scaled by (1 − η) upward and (1 + η) downward around N's own advice, for small η > 0, give the following:
- (a) strict pointwise own-Bayes at μ_N. So each edge model is Bayes at its edge weight, and each vertex at e_i.
- (b) a strict local potential for any set of gates at every point. So strict CG2 holds for every pair and PP42's strict CG3 for every triple, and PP49 Lemma 3.4(ii) gives (H3) for every ordered triple.
- (c) the 19 sampled types at which three non-vertex members give three different answers are covered. So are all 148 superset types.

*Why the superset suffices.* Actual types are a subset of the superset (Prop 5.2), so a field built on the superset is valid whichever types occur. 54 types were found by sampling, and every one of them lies in the superset.

*Scope.* The module is finite and witnessed. That is legitimate as a boundary test, and it is not offered as a construction route: by Thm N a whole-simplex solution cannot be witnessed. It shows that boundary members carry **no finite-level obstruction**. Edge models at edge weights are compatible with T, with nearby interior models, with each other on one edge, with another edge's model and with all three vertex gates. **Source of failure: none found.**

### 2.4 Limits, compactness and degeneration

**PP49 Prop 4.3 (checked).** The F_w(X) projection argument is correct.
- Realisation passes to limits by the three-term bound.
- Values pass to limits by L¹-continuity and absolute continuity.
- The projection is closed because Δ is compact.
- Remark 4.4 (no field needed at (e_w, w)) is correct: the limit record has old side V_w, so it is a weak w-worsening.

So **fixed-rival limits approaching an edge or a vertex close**, provided (H4) holds on the closed simplex.

**Proposition 2.4 (normalisation and degeneration; PROVED).**
- **(a) Normalisation.** Replace f^a_w by k_w(a)f^a_w, with k_w(a) > 0. This changes no gate verdict. It rescales the (H2) constants and replaces λ_{a,w} by λ_{a,w}/k_w(a), with the same support. (H3) is unchanged. So PP49 Thm A holds under:
  - **(H4)(b′)**: for some positive k, a ↦ k_w(a)δ^a_w is L¹-continuous on Δ.
  - Theorem N's envelope (H4)(c) should be read the same way.
- **(b) Degeneration.** Suppose that at a boundary index a the normalised limit field has a zero increment on an improving step at w, on a non-null region Z. Under (R0) that gate accepts C_a ⪯_w C_a[F ↦ better], for bounded F ⊆ Z. This violates strict (G). If the gate is given a different field instead, (H4)(b′) fails at a, and Prop 4.3 is no longer available.

**Proposition 2.5 (the transported design at the boundary; PROVED; CHECKED `transported_boundary.out`).** Take ℓ^a(g) := ℓ^T(a∘g), with ℓ^T the field of REFEREE_PP32 §3.2. C_a is its pointwise u-Bayes model, since T is ℓ^T's a.e.-unique u-Bayes model.
- **(i) Raw fields at an edge.** As a₃ → 0, the world-3 field tends to 0. The raw limit gate is degenerate, so (b) applies.
- **(ii) Normalised fields at an edge.** Normalise by a_w; the Bayes weights become ∝ a, which is consistent with Lemma 2.1. The edge limit is then |g₃|/(2d) on M₁, independent of the direction of approach (CHECKED).
- **(iii) Normalised fields at a vertex.** Near e₁ the normalised world-2 field on M₃ is ρ|g₃|F(|g₂|/(ρ|g₃|)), with ρ = b₃/b₂. This is constant along each direction but differs between directions.
  - For ρ = 1 against ρ = 100, the ratio is 23/32 at g = (1, 1, −1) and 1 at g = (1, 1/30, −1).
  - So no per-world factor reconciles the two directions, and (H4)(b′) fails at every vertex.

**Classification: chosen design.** The general obligation is **vertex coherence**. Near e_i, the normalised off-support fields must converge to one field. Direction dependence must be confined to neighbourhoods of D_{b,e_i} that vanish in measure. Nothing found makes this impossible.

**Realiser compactness and envelopes.** Δ is compact, and PP49 gates every index. Prop 4.3 needs L¹-continuity only, not a uniform envelope. A uniform envelope (H4)(c) is needed only for Theorem N. It holds for the normalised transported fields (bounded by a multiple of |g|), but those fail at the vertices.

---

## 3. No global prices

### 3.1 What a kill would mean

Under PP49 Thm N (checked in §4.2), "prices always exist" would make (H0)–(H5) unsatisfiable. So it would refute the posterior gate architecture outright. I tried the two suggested levers, and both fail for structural reasons. I then settled the question with an exact certificate.

### 3.2 The levers

**Lemma 3.1 (pointwise rescaling; PROVED).** Let h^N(g) > 0 be measurable. Replacing ℓ^N by h^N ℓ^N:
- leaves C_N's pointwise own-Bayes property unchanged, at the same weight;
- shifts every pointwise ratio log(f^M/f^N) on D_NM by log h^M − log h^N, at every world.

So Bayes conditions constrain each model's field only up to a positive function of g. They force no interval to contain any particular value, log(λ_a/λ_b)-type quantities included. The positions of the endpoints are set by the fields, type by type.

**Lever (a), D = log(a/b) as a global coboundary.** This is true (§2.1). But the type condition is an open condition with positive slack over finitely many patterns. It constrains only the *ordering* of D, and through Lemma 3.1 only up to pointwise shifts. A coboundary that *admits* a solution does not *force* one.

**Lever (b), Bayes-forced positions.** This is refuted by Lemma 3.1, and concretely by Thm 3.3. There, every coboundary choice misses some world-1 interval.

**Lemma 3.2 (cycles need a two-signed pair; PROVED).** At world w, suppose the move N → M is one-signed on D_NM. Then its only constraint is a half-line, oriented by the strict pointwise improvement order. That order is acyclic. So every inconsistent cycle of difference constraints contains a pair that is two-signed at w.

In the certificate below, the pair (A, C) is one-signed at world 3 (C/A ∝ the world-3 ray). World 3 is globally consistent.

### 3.3 The exact certificate

**Theorem 3.3 (four posterior models with no global prices; CHECKED `four_model_exact.out`).** Take ε = 3/10 and the models

  A = T = C_{(1,1,1)/3},  B = C_{(11,10,9)/30},  C = C_{(11,11,8)/30},  D = C_{(10,11,9)/30}.

The following hold.
- **(0) Two-valued.** The credal sets pairwise intersect: normalise(a/b) ∈ M for every pair. So by PP49 Lemma 1.2(a) the family is two-valued.
- **(1) Types.** Exactly 28 point types (P, R) are admitted by the pair-ordering theorem. Here P is the set of acceptors of h and R the set of worlds where h is correct. All 28 occur, each with an exact witness with strict margins, hence on a non-null open cone.
- **(2) Own-Bayes.** The fields are |g| times rational constants on each type cone, completed on all four advice values. They are strictly guiding, and each model is the **strict** pointwise optimum of its own field over all four advice values, at interior weights.
- **(3) Pairs.** All six pairs have nondegenerate CG2 intervals at all three worlds. So strict CG2 holds with positive constants, and (BR) holds.
- **(4) Triples.** Every triple at every world passes the closed cycle test with strict slack on both sides, so it is not tight. By PP47 Thm 4.1 (equivalently PP49 Lemma 3.4(iii)), (TC) holds under (R0) for the four gates and guidance.
- **(5) No global prices.** At world 1 the six intervals admit no global constants. At world 2 they again admit none. At world 3 they do.

World-1 intervals for z_NM:

| AB | AC | AD | BC | BD | CD |
|---|---|---|---|---|---|
| [−5.405, −5.355] | [0, 0.300] | [0, 0.050] | [5.355, 5.405] | [5.105, 5.405] | [−0.300, −0.250] |

Along A→B→C→D→A the upper bounds of z_AB, z_BC, z_CD and z_DA = −z_AD sum to −5.355 + 5.405 − 0.250 + 0 = −0.200 < 0. Every triangle is feasible with slack.

**Second certificate (`four_model_exact_fixlam.out`; CHECKED).** λ_N = the index of N (not required by the audit). All checks pass again, with no global constants at world 1. The field ratios are extreme (up to e^30), but finite.

*Reading.* What escapes the kill is exactly the freedom of the fields on each point type (Lemma 3.1), within the slack of the pair-ordering certificate. Nothing in own-Bayes, strict CG2 and the exact zero-accepting triangle test for four nearby posterior models forces prices. **The audit's decisive checkpoint is met at the four-model level.** It does not yet address continuity or the rest of the family; see §3.4.

### 3.4 Two necessary conditions for the continuum

**Lemma 3.4 (width budget; PROVED).** Fix w and a cycle X₁ → … → X_k → X₁ whose upper bounds satisfy Σ_i U_{X_iX_{i+1}} = −Γ < 0. Let F be any further gated member for which every triple (X_i, X_{i+1}, F) passes the closed cycle test. This is necessary for (TC) when the triple is two-valued (PP47 Thm 4.1(a); REFEREE Thm R1). Then

  Σ_i width(I^w_{X_iF}) ≥ Γ.

*Proof.*
1. Write J_i := I^w_{X_iF} = [j_i, j_i + w_i].
2. The triple test gives t_i ∈ I_{X_iX_{i+1}} ∩ (J_i − J_{i+1}).
3. Summing, −Γ ≥ Σt_i ≥ Σ(j_i − j_{i+1} − w_{i+1}) = −Σw_i. ∎

*Consequences.*
- In a whole-simplex solution, the world at which Thm N forces a deficient cycle must give **every** member F that is two-valued with the cycle a total interval width at least the deficit. This covers members near the cycle, edge members, and vertex gates at worlds other than their own.
- So the audit's "no uniform width bound" stands as an *assumption*, but some width is *forced* wherever cycles are deficient.
- One-signed partners (infinite width) are free.
- In Thm 3.3, Γ = 0.2. A fifth nearby member would need total width at least 0.2 against A, B, C, D at world 1.

**Lemma 3.5 (spectator constraints at three-valued points; PROVED; orders CHECKED `three_valued_orders.out`).** Fix w, an ordered triple o = (a, b, c), and a point g where C_a, C_b, C_c give three different advice values A, B, C with world-w ranks r(A) < r(B) < r(C). Write α_N := κ_N[ℓ^N_w(B) − ℓ^N_w(A)] and β_N := κ_N[ℓ^N_w(C) − ℓ^N_w(B)], both > 0. Then:
- PP49 Lemma 3.4(i) at g requires, for o, α_a + β_b ≤ α_c + β_c. For the reverse orientation, with its own constants, it requires α′_a + β′_a ≤ α′_b + β′_c.
- The pair conditions at g are α_a ≤ α_b, β_b ≤ β_c and α_a + β_a ≤ α_c + β_c. They imply the first condition only together with the **spectator** inequality α_a ≤ α_c. This compares C_c's valuation of the step A → B, which C_c does not make, with C_a's.
- If the three scaled fields coincide at g, both orientations are exactly 0, which is tight.
- Suppose both rank orders occur at w on non-null sets with overlapping ratio ranges β/α. Then common-shape fields give a nontrivial zero-sum selection, so (H3) fails.

*CHECKED.* For (T, C_{(9,9,2)/20}, E), both rank orders occur at worlds 1 and 2. At world 3, E is always worst.

*Proof.* Expand κ·Q_o = α_a + β_b − (α_c + β_c). For the zero selection, the scaled Q-vectors (α, β, −α−β) and (−α′, −β′, α′ + β′) with matched ratios cancel. Lyapunov matches the masses. By PP49 Lemma 3.2 the reverses are refused. ∎

*Reading.* At three-valued points (H3) is a genuinely new kind of field condition. Every boundary triple and every far triple has such points (PP49 Lemma 1.2), and the four-model certificate is two-valued, so it does not test them. These constraints are triple-local, and do not by themselves restore global prices. **Classification: architecture** (triple-local (TC) in a gate union). They are design obligations, not obstructions.

---

## 4. The reduction (PP49 Theorem A, Theorem N)

### 4.1 Theorem A, checked line by line

- **Lemma 3.2 (strict links).** Correct. One wording point: when the reverse goes through V_w's gate at w, the forward link through gate a would be a nontrivial weak w-improvement. Gate a rates that negatively. (PP49 says "guidance refuses the forward record"; the conclusion is the same.)
- **§4.2 (TC).**
  - The case split |F| ≤ 2 / |F| = 3 is exhaustive, once (e_w, w) links are reclassified as guidance and a repeated gate is allowed.
  - Lemma 3.3's "old values occur at most twice" is right.
- **Lemma 3.4, the enumeration.** I re-derived V_o(g). The four vector types P_ab, P_bc, P_ca, Q_o are exactly the pointwise link vectors; the case "X ≠ Y = Z" yields P_ca, not P_ab.
- **Lemma 3.4, exactness.** If the first clause of criterion (i) holds with κ > 0 and the second fails, a nontrivial triangle with all links 0 is accepted under (R0), and its reverses are refused (Lemma 3.2). So, **given its first clause, (i) is exact**. What remains at three-valued points is only PP49 Gap 3 (positivity of κ).
- **§4.3, competitiveness at boundary supports.** Correct with weak Bayes: some w ∈ supp λ_a ⊆ supp a has Φ ≥ 0, and (R0) accepts. Lemma 2.1 sharpens this to supp λ_a = supp a.
- **Strong undominatedness, direct (C), single-world ties.** Under strict (H2) there are no ties at any world. So direct (C) holds model by model, and zero-accepting gates create no single-world ties. Without strictness (PP49 Gap 1), PP47 Thm 2.5 shows how F2 arises.
- **Prop 4.3 and Remark 4.4.** Correct (§2.4), with (H4)(b′).
- **§4.5, KKM.** Correct. Dominance is strict at **every** world by Lemma 3.2, and the undominated class is exactly the image.

**Verdict.** The chain "own-Bayes + strict CG2 + exact triangle condition + continuity ⇒ (S) ⇒ KKM dominators" has **no gap** under (H0)–(H5).

**The true risks are in satisfying the hypotheses:**
- vertex coherence (§2.4);
- Lemma 3.4's width budget;
- Lemma 3.5's spectator constraints;
- all of them jointly with (H4) on a continuum.

### 4.2 Theorem N, checked

- Lemma 7.2(a) is immediate.
- In 7.2(b), the countable-supremum construction and the limit for gates outside Q are correct; the limit c* = 0 is harmless.
- FF2's hypotheses hold:
  - the family is continuous in measure (PP49 Lemma 1.1);
  - it is competitive on its supports;
  - T₁ = C_u;
  - endorsement on H_n = Ω.

Status: PROVED modulo FF2's import chain, as PP49 says. With Thm 3.3, this makes "no global prices at some world" both **forced** and **locally achievable**.

---

## 5. Classification

| Failure or constraint found | From the axioms | From this architecture or family | From a chosen design |
|---|---|---|---|
| Some world must lack global prices (Thm N) | yes, given the family's continuity (FF2) | | |
| supp λ_a = supp a | yes (competitiveness) | | |
| Raw transported fields degenerate at edges; normalised ones discontinuous at vertices | | | **yes** |
| Degenerate boundary limit ⇒ strict (G) fails | | yes ((R0) gate union) | |
| Width budget against every two-valued partner of a deficient cycle | | yes (triple-local (TC)) | |
| Spectator constraints; common-shape tightness at three-valued points | | yes | |
| Kill of the four-model target | not possible (Thm 3.3) | not possible | |
| Boundary pairs and the joint boundary module | none | none | none |

---

## 6. Scripts (`r9/PP53_py/`)

Run each with `python3 -I -B <script> [args] > <script>.out` inside the folder.

| Script | Content | Label |
|---|---|---|
| `lib53.py` | exact posterior advice C_a(g) = T₁(a∘g), ranks | library |
| `boundary_supports.py` | Lemma 2.1: single-correct answers at every support world, none off-support, 8 indices | CHECKED |
| `boundary_module.py` | Prop 2.3: 148 superset types (54 sampled, 19 three-valued); a strict local potential at μ = index on every type, verified in Fractions | CHECKED |
| `transported_boundary.py` | Prop 2.5: raw world-3 field → 0; normalised edge limit direction-free; vertex limits direction-dependent, non-proportional | CHECKED |
| `four_model_search.py` | Thm 3.3: MILP over the 28 types (sufficient max-form Bayes). `--fixlam` imposes λ = index. Writes the solution JSON. | proposes only |
| `four_model_exact.py` | Thm 3.3: exact verification of overlap, witnesses, strict Bayes on all four advice values, CG2, triple slack, and global infeasibility. Takes the JSON as argument; outputs `four_model_exact.out` and `four_model_exact_fixlam.out`. | CHECKED |
| `three_valued_orders.py` | Lemma 3.5: both world-w rank orders at three-valued points of (T, C_b, E) at worlds 1 and 2 | CHECKED |

**Most important next step.** Extend Thm 3.3 to a continuous two-parameter patch through T, using L¹-continuous fields on the closed simplex (normalised, vertex-coherent). The extension must meet two conditions at the deficient world:
- Lemma 3.4's width budget against every further member;
- Lemma 3.5's spectator constraints on far and boundary triples.

The four-model fields are piecewise constant on type cones. The first test is whether their per-type pattern can be made to vary continuously with the indices while the cycle deficit stays positive.
