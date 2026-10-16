# N21: T1 on adjacent decomposable domains — where (NA_w) enters, what survives, and what adjacency costs

13 Oct 2026. Task: remove (NA_w) from the N15 no-realisation theorem for T1, i.e. pass from non-adjacent (LF) decomposable domains
to all (LF) decomposable domains. Labels: **PROVED** (full proof written here), **CHECKED** (verified, proof sketched),
**CONJECTURE**, **NUMERICS**. Scripts: `n21py/`.

Refereed inputs, with status:
- N15 §§2–7 (CORRECT / CORRECT WITH REPAIR in N18); N12 Lemma 2.1, Lemma 4.3, Thm 3.1 (CORRECT in N14);
- N14 §2.3 "chart-form edge box on every (LF) decomposable domain" (PROVED in N14);
- R10b Prop V, Cor V1, V2, Lemma UVN, Lemma D, Lemma M (CORRECT in R12);
- R4 Thm A, Thm B; R1 Prop 2.1 (table of charts for each advice range), Prop 2.4, Prop 2.8, Prop 3.1, Lemma 1.5, Lemma 3.5; R11 Lemma RS.

---

## 0. Outcome

**Verdict.** (NA_w) is **not** removed in full. It is replaced by a weaker, purely local hypothesis at p\*, and the
remaining (adjacent) case is pushed into a narrow, explicitly described corner.

1. **Where non-adjacency is used (§1).** In exactly two kinds of place:
   - (U-glob) global straight levels on all of Ω (N15 Lemma 2.1 as used in Steps 0, 1, 4, and Cor PL2 inside Lemma 4.1);
   - (U-box) the box bridge, N12 Thm 3.1 item 6: the witnesses' actual charts must contain the edge prior. This is (E4).

   Everything else in N15 is local at p\*, or uses only adjacency-tolerant tools (UVN, Lemma M, chart-form box, Thm B).
2. **Adjacency-tolerant structure (§2, PROVED, every decomposable domain).**
   - N21.1: q ↦ P_{K_q}(g) is **quasi-concave** on Ω for **every** g. (Without adjacency it is also quasi-convex; this is
     the exact content of "straight levels".)
   - N21.2: wedges are confined to {q : K_q ∩ K″ = ∅}. In particular there is a ball B₁ = B(p\*, r₁) on which every
     near-facet gamble has a half-plane chart.
   - N21.3: a sector lemma for charts of pairs with advice range {+,0,−} along segments.
3. **Local theory transfers (§3, PROVED).** On every (LF) decomposable domain, the hypothesis
   - **(TS)**: for every facet F_k and τ ∈ (0,1), Ψ(·,τ) = P(·,h(τ)) takes both strict signs at points arbitrarily
     close to p\*,

   implies all of N15 Thm 4.2 (pivot chords), Thm 4.3 (no sliding edges), Prop 5.3 and §6, hence **(PC) and (NS)**.
   (TS) contains no derivative and no regularity; on non-adjacent domains N15 proves it.
4. **No WLOG reduction to two-element advice ranges (§4, PROVED).** R11 Lemma RS cannot be applied: the vertex selections C_{e_k} use −g.
   Restricting the class of evaluable models instead changes the Bayes family, and can destroy coherence (explicit n = 2 example).
5. **What adjacency costs (§5, PROVED).** Assume (PC) + (NS) at p\* (e.g. from (TS)) and a T1 realisation on any (LF)
   decomposable domain. Then for every world b:
   - every failing vertex-limit box at b (one exists for every b, NUMERICS-exact for T1) is cut by d-faces whose
     apexes lie on the segment [e_b, p\*] of the crossing chord, and which run to the edge;
   - the selection becomes **precise, equal to e_b**, at some edge prior z\*_b ∈ [e_b, e_a);
   - hence **acceptance of h is in the advice range for a.e. h with h_b > 0**.
   - Consequently **the advice range of every mixed pair contains both acceptances** (a.e.), all vertex models are precise (K_{e_b} = {e_b}),
     and interior selections near an edge prior with support S converge into Δ_S.
6. **Main theorem (N21.6, PROVED).** T1 has no realisation (integral penalties, (R1), (R2), (LF)) on any decomposable domain such
   that (TS) holds and a non-null set of mixed pairs has an advice range lacking one of the two acceptances. Without (TS): realisations must be
   of the two pinning types (E5a), (E5b) of §6. In all cases a realisation must live on a domain whose mixed pairs a.e.
   have both acceptances in their advice range, or must pin a vertex near p\* behind a wall of precise vertex priors.
7. **Residual (§6).** (E5a) single-vertex pinning near p\* shielded by priors with K_q = {v_k}; (E5b) a frozen facet;
   (E4′) the near-all-orientation cut configuration of §5. **CONJECTURE N21**: none occurs. No construction was found.

---

## 1. Setting, and the exact uses of non-adjacency

**Setting.** As in N15 §1 and R10b §1, on a general decomposable domain:
- (LF) with open N ⊇ ∂D_T∖0, shrunk so that N ∩ (−cl D_T) = ∅, N contains no h ≤ 0, and on pairs h ∈ N the advice range is
  {+,0} or {+,0,−} (R10b §1).
- K_q (q ∈ Ω) the interior credal sets, B_q ≈ D_{K_q}; P(q,g) = min_{K_q} m·g jointly continuous (R1 Prop 3.1).
- For a pair with advice range {+,0,−}: α = c·q, β = c′·q, d = c − c′; R(g) = {α>0, d>0}, R(−g) = {β>0, d<0}, silence
  S(g) = {α ≤ 0, β ≤ 0}, d-face F(g) = {d = 0, α > 0}. c, d have the strict sign of g; c′ that of −g (R1 Prop 2.1).
- **Good g**: R10b (1.1) holds (P(·,g) ≥ 0 on cl R(g) ∩ Ω, ≤ 0 on Ω ∖ cl R(g)) and R4 Thm B holds (K_p ⊆ g^⊥ on
  cl F(g) ∩ Ω). Good pairs are co-null.
- Fix a compact K″ ⊆ int T (e.g. K″ = {u}). Let N₀ ⊆ N be a closed conic neighbourhood of the closed facets of D_T
  (minus 0) so small that P_{K″} > 0 on N₀. This is possible: P_{K″} is continuous and positive on the compact set of
  normalised closed facet gambles, since K″ ⊆ int T. All gambles used below (facet gambles, their shifts h − c𝟙 with
  |c| ≤ c₀, the box witnesses, and good gambles near them) lie in N₀.

**Table of uses.** "Global" means the step uses the sign structure of P(·,g) on all of Ω.

| Step | Uses | Non-adjacency needed? |
|---|---|---|
| N15 Lemma 2.1 (exact half-planes) on Ω | (L2.1) cluster chords on Ω, i.e. (★) half-plane charts | **yes (U-glob)**; on a ball without wedges, no (N21.2) |
| N15 Lemma 2.2, 2.3 | straight levels on B(p\*, r₀) | only through r₀; replace r₀ by r₁ (N21.2) |
| N15 Step 0 (A_τ, B_τ nonempty half-planes) | UVN + Lemma 2.1 | UVN no; "half-planes" yes (U-glob) |
| N15 Step 1 via Lemma 4.1 | **Cor PL2 (no d-faces of exterior pairs meeting G)** | **yes (U-glob)**. This is the pinning step |
| N15 Step 2 (monotone) | concavity in τ; wedge inclusion at p\* | no (local), given A_τ ⊆ H⁺_τ (N21.1) |
| N15 Step 3 (continuous) | local convexity of Z_{τ₀} near p\* | no (local) |
| N15 Step 4 (crossing values) | λ⁺_τ ∩ Ω ⊆ P_τ (global) for the negative sign at e_i | **yes as written**; repaired by c-clusters (§3) |
| N15 Step 5, Thm 4.3, §5, §6 | local at p\*, cap lemma, N12 Lemma 4.3 | no |
| N12 Thm 2.4 edge box | chart form holds on every (LF) domain (N14 §2.3) | no |
| N12 Thm 3.1 item 6 (box bridge) | witness charts contain q₀ | **yes (U-box) = (NA_w) = R15 (E4)** |
| N12 Thm 3.1 items 3–5, 7 | c-clusters at p\*; algebra | no |
| R15 Lemma 6.1 Lemma FS witnesses | not used in the N12/N15 route (Thm 2.4 replaces it) | — |

So the brief's two guesses are both right in part. The box step is where (NA_w) enters, in chart form. Lemma FS
witnesses are no longer in the chain. There is a **second, independent** use: the pinning step (Cor PL2).

---

## 2. Adjacency-tolerant structure

**Lemma N21.1 (quasi-concavity; PROVED, every decomposable domain, every g ∈ ℝ³).** For every c ∈ ℝ, {q ∈ Ω : P(q,g) > c} and
{q ∈ Ω : P(q,g) ≥ c} are convex.

*Proof.*
1. Let P(q₁,g), P(q₂,g) > c, and pick c′ with c < c′ < min_i P(q_i,g). Put g′ := g − c′𝟙, so P(q_i, g′) > 0
   (level shift).
2. Good gambles are dense. Take good g″ → g′. By joint continuity, P(q_i, g″) > 0 for g″ close to g′.
3. By (1.1), P(·,g″) ≤ 0 off cl R(g″), so q_i ∈ cl R(g″). The chart R(g″) is convex (every entry of R1's table is), so
   [q₁,q₂] ⊆ cl R(g″), and (1.1) gives P(·,g″) ≥ 0 on [q₁,q₂].
4. Let g″ → g′. Then P(·,g′) ≥ 0 on [q₁,q₂], i.e. P(·,g) ≥ c′ > c there.
5. {P ≥ c} = ∩_{c̃<c} {P > c̃}. ∎

*Remark.* Without adjacency the complement {P ≤ c} is also convex (N15 Lemma 2.1, Step 3). With a wedge chart
{α>0, d>0}, its complement is not convex, and quasi-convexity fails. Quasi-concavity is therefore exactly what survives
of "straight levels".

**Corollary N21.1′ (PROVED).** Let A_τ := {Ψ(·,τ) > 0}. If A_τ ∩ B₁ = H⁺ ∩ B₁ for an open half-plane H⁺ whose boundary
passes through p\* (B₁ any ball at p\*), then A_τ ⊆ H⁺ ∩ Ω.

*Proof.* Suppose x ∈ A_τ ∖ H⁺. Since A_τ is open, we may take x with n·(x − p\*) < 0. A_τ is convex (N21.1), so it
contains conv({x} ∪ (H⁺ ∩ B₁)). That set contains points of B₁ with n·(q − p\*) < 0 arbitrarily close to p\*. ∎

**Lemma N21.2 (wedges avoid priors whose credal set meets K″; PROVED).** Let C ⊆ Ω be convex and open with
K_q ∩ K″ ≠ ∅ for all q ∈ C. Then for a.e. g ∈ N₀:
- R(−g) ∩ C = ∅ and F(g) ∩ C = ∅;
- R(g) ∩ C = {c(g)·q > 0} ∩ C.

There is r₁ > 0 such that B₁ := B(p\*, r₁) ⊆ Ω has K_q ⊇ K″ for all q ∈ B₁.

*Proof.*
1. *No acceptance of −g.* If m ∈ K_q ∩ K″, then m·g > 0, so −g ∉ D_{K_q}. Since B_q ≈ D_{K_q} for every q, the open set
   R(−g) ∩ C is a.e. disjoint from it in q, hence (Fubini, good g) null and therefore empty.
2. *No d-face.* For good g, p ∈ F(g) ∩ Ω gives K_p ⊆ g^⊥ (Thm B). But K_p ∋ m with m·g > 0.
3. *Half-plane chart.* {α > 0, d < 0} ⊆ R(−g) misses C, and {α > 0, d = 0} = F(g) misses C. So the open convex set
   {α > 0} ∩ C lies in {d > 0}, i.e. in R(g). (For advice range {+,0} the claim is the table.)
4. *The ball.* K_{p\*} = T ⊇ B(x, ρ) ∩ aff Δ for every x ∈ K″, for some ρ > 0. If d_H(K_q, T) < ρ, then K_q ⊇ K″: if
   x ∉ K_q, separate x from K_q by a line; the point of T at distance ρ from x beyond that line is at distance ≥ ρ from
   K_q. Hausdorff continuity at p\* finishes. ∎

This is R1 Lemma 3.5 with K′ replaced by an arbitrary compact K″ ⊆ int T, and with "for a.e. g ∈ U′" replaced by
"for a.e. g ∈ N₀".

**Lemma N21.3 (sector lemma; PROVED).** Let g be a pair with advice range {+,0,−}, [x,y] ⊆ Δ a segment, and x ∈ S(g). Along the
segment from x:
- once a point leaves S(g), the segment never returns to S(g);
- after leaving S(g), any passage between R(−g) and R(g) crosses cl F(g).

*Proof.* S(g) is closed and convex. If x, z ∈ S(g) and y′ ∈ (x,z), then y′ ∈ S(g). The three cells partition Δ, and
cl R(g) ∩ cl R(−g) ⊆ cl F(g) ∪ S(g). ∎ (`n21py/lemmas_check.py` (1): 908 segments starting in silence, 0 violations.)

---

## 3. The local theory transfers under (TS)

**Hypothesis (TS) (two-signedness at p\*).** For every facet F_k and every τ ∈ (0,1), p\* ∈ cl A_τ ∩ cl B_τ, where
A_τ = {Ψ(·,τ) > 0} and B_τ = {Ψ(·,τ) < 0}.

(TS) is weaker than the "both signs" clause of (DD): no limit or derivative is involved. On non-adjacent domains N15
Steps 1 and 5 prove (TS).

**Theorem N21.4 (PROVED).** On every decomposable domain with (LF), let (R1), (R2) hold with T all-facing in general position
(T1 included), and assume (TS). Then the conclusions of N15 Thm 4.2, Thm 4.3, Lemma 5.1, Prop 5.3 and §6 hold, with
Ω replaced by B₁ in every *local* statement and r₀ replaced by r₁. In particular (PC) and (NS) hold at p\* on all three
facets.

*Proof (list of edits to N15; everything not mentioned is local and unchanged).*

1. *Local straight levels.* By N21.2, for a.e. g ∈ N₀ the chart on B₁ is ∅, B₁, or a half-plane ∩ B₁. N12 Lemma 2.1
   and N15 Lemma 2.1 hold verbatim with Ω replaced by the convex set B₁. Lemma 2.3 holds with r₀ replaced by r₁: its
   proof uses only that level lines do not cross λ inside the ball.
2. *Steps 0, 1, 5 replaced by (TS).*
   - A_τ ∩ B₁ = H⁺_τ ∩ B₁ and B_τ ∩ B₁ = H⁻_τ ∩ B₁, with boundary lines λ^±_τ that do not cross in B₁.
   - (TS) puts p\* on both lines, so λ⁺_τ = λ⁻_τ =: λ_τ, and Z_τ ∩ B₁ = λ_τ ∩ B₁.
   - Globally, A_τ ⊆ H⁺_τ ∩ Ω by N21.1′.
   - UVN (adjacency-tolerant) still gives V_l ∩ Ω ⊆ A_τ for h(τ)_l > 0 and V_k ∩ Ω ⊆ B_τ. With A_τ ⊆ H⁺_τ this gives
     n_τ·(e_l − p\*) > 0 for l with h(τ)_l > 0 (a line through p\* and e_l would cut V_l ∩ Ω).
3. *Step 2 (monotone).* The inclusion A_σ ∩ A_{σ′} ⊆ A_τ (concavity in τ) is used only near p\*. Pairwise intersection on
   (0,τ_j) comes from V_j, and n_σ ≠ −n_{σ′} follows from A ⊆ H⁺. Unchanged otherwise.
4. *Step 3 (continuous).* Local. It uses (TS) in place of Step 1.
5. *Step 4: the negative vertex sign, by c-clusters.* This is the only genuinely new argument. Let h(τ)_i < 0.
   - Take good g_m → h(τ) in N₀. By N21.2, R(g_m) ∩ B₁ = {c(g_m)·q > 0} ∩ B₁. Let ĉ be a cluster of c(g_m)/|c(g_m)|.
   - By R15 Lemma C (whose proof is local on B₁), {Ψ(·,τ) > 0} ∩ B₁ ⊆ {ĉ·q > 0} and {Ψ(·,τ) < 0} ∩ B₁ ⊆ {ĉ·q < 0}.
     These are the two open half-discs of λ_τ (item 2), so the line of ĉ is λ_τ, and ĉ·q = κ n_τ·(q − p\*) with κ > 0 on
     aff Δ.
   - c(g_m)_i < 0 pointwise, so ĉ·e_i ≤ 0, i.e. n_τ·(e_i − p\*) ≤ 0.
   - *Non-constancy.* Suppose n_τ is constant on [a,b]. For q ∈ λ ∩ B₁, Ψ(q,·) = 0 on [a,b]. The cap lemma gives
     Ψ(q,·) ≤ 0 on ℝ, so λ ∩ B₁ ⊆ {Ψ(·,τ) ≤ 0} for every τ. Since A_τ ∩ B₁ is the open half-disc of λ_τ, this forces
     λ_τ = λ for all τ ∈ (0,1). Then n·(e_i − p\*) is > 0 on one side of τ_i and ≤ 0 on the other, a contradiction.
   - Continuity then gives λ_{τ_i} = line(p\*, e_i), as in N15.
   - The last clause of Thm 4.2 (every cluster chord equals λ_τ) is the c-cluster statement just proved.
6. *Thm 4.3 (no sliding).* Local. Convexity of the zero set of P(·,r) near p\* holds by item 1, since r ∈ N₀. The test
   point q ∈ B₁ and the cap lemma at q are local.
7. *§5.* Anchors q_{τ₀}(ξ) are taken with ξ < r₁/2, so they lie in B₁. Lemma 5.1 uses the strict sides of λ_τ in B₁,
   Lemma 2.3 (radius r₁) and the cap lemma at the anchor: all local. Lemma 5.2 and Prop 5.3 are unchanged.
8. *§6.* Blow-ups at p\* are local. Step 5 applies N12 Lemma 4.3 to G₂, using non-constancy (item 5). So (PC) holds.
   (NS) follows from Thm 4.3 as in N15 Thm 7.1. ∎

**Remark.** N12 Thm 3.1 items 3–5 (crossing rows λ_{ik} > 0, nonsingular Γ_k, corner equations) use only c-clusters at
p\* and (PC), (NS). So they hold on every (LF) domain under (TS). Only item 6 (the box) remains.

---

## 4. No "WLOG two-element advice range" reduction

**Proposition N21.5 (PROVED).**
- (a) Let a realisation have a non-null set E ⊆ N ∩ {g_k < 0} of pairs with advice range {+,0,−}. Let M′ be the class of
  evaluable models in M that accept −g for no g ∈ E (up to null sets), so that the advice range on E becomes {+,0}. Then C_{e_k} ∉ M′, so R11 Lemma RS does not apply.
- (b) Removing − from the advice ranges in this way (restricting the evaluable models) and keeping the penalties changes the interior Bayes family. On the modified pairs,
  B′_q = {g : α_g(q) > 0}, i.e. B_q gains {g : q ∈ R(−g) ∪ F(g), α_g(q) > 0} and loses the corresponding −g. In general
  B′_q is incoherent.
- (c) Example (n = 2). Take the precise identity system (K_t = {t}), realised on the all-model domain with data for the
  advice +, 0, − whose c-threshold is t > r/2 and whose d-threshold is t = r (r = b/(a+b) for g = (a,−b)). Restrict the evaluable models so that the advice range is {+,0} on
  pairs with r ∈ (0.4, 0.8). Then the restricted Bayes acceptance set at t ∈ (0.2, 0.4) is {r < t} ∪ (0.4, min(0.8, 2t)).
  That set is not an initial segment, so the model is incoherent.

*Proof.*
- (a) At e_k, accepting −g is good and in the advice range on E, hence best (R1 Lemma 1.5). So C_{e_k} accepts −g on E.
- (b) Read off R1's table.
- (c) Signs: the c-threshold r/2 < r = d-threshold, and the c′-threshold lies above r (the lines are concurrent), so the
  silence cell is empty and the system is the identity. In n = 2, coherent ⇔ accepted r-set is an initial segment
  (`lemmas_check.py` (3): coherent at t = 0.15, 0.5; incoherent at t = 0.25, 0.3, 0.35). ∎

So the extension cannot be obtained by restricting the domain. The adjacent case has to be argued directly. That is done in
§5.

---

## 5. What adjacency at the box witnesses costs

**Standing assumptions for this section.**
- A T1 realisation on an (LF) decomposable domain.
- (PC) + (NS) at p\* (from Thm N21.4 under (TS), or from N15 on non-adjacent domains).

By N12 Thm 3.1 items 3–5 and R15 §6 algebra, the facet data are x ∈ {x₊, x₋}. For **every** vertex b there is exactly one
a with Λ_{ab} > 1. Moreover Λ_{ab}Λ_{cb} = (v_{ac}v_{ca})/(v_{aa}v_{cc}) = β², β = (1−ε)/(1+2ε). The product identity is
algebra from R15 Thm 6.2 step 3; the per-vertex statement is reproduced exactly by `n21py/t1_lambda_per_vertex.py` for
ε ∈ {.05, .1, .3, .6, .9} at both solutions.

Fix such a pair (a,b), and let c be the third index. Let w′ ∈ F_a (w′_a < 0, the A-family) and w ∈ F_c (w_a > 0, the
B-family) be the two b-crossings. Let q₀(s) = s e_a + (1−s)e_b, with A_s → w′ and B_s → w the R15 Lemma 6.1 witnesses:
- c(A_s)·q₀ > 0 and c(B_s)·q₀ > 0, with margins, for all good gambles in small balls around them (unique clusters,
  N12 Thm 3.1 item 6);
- A_s + λB_s < 0 on {a,b} for some λ > 0.

**Theorem N21.6 (cut localisation; PROVED).** For a sequence s_m ↓ 0 there are good gambles g_m with advice range {+,0,−} (all near w′,
or all near w; call the limit crossing w\*), with apexes a_m ∈ Ω and edge points z_m ∈ [e_a, e_b], such that:
- (i) F(g_m) ∩ Ω = (a_m, z_m), and a_m lies on the α-line of g_m strictly between its edge crossing σ_m and B₁;
- (ii) a_m → a\* ∈ [e_b, p\*] ∖ B₁ (the segment of the crossing chord λ_{w\*} = line(p\*, e_b)), and z_m → z\* ∈
  [e_b, e_a). In the A-case z\* = e_b;
- (iii) K_q ⊆ ℓ_{w\*} = line(e_b, v_{k\*}) for every q ∈ [a\*, z\*] ∩ Ω, where k\* is the facet of w\*;
- (iv) there are interior priors q_m → z\* with K_{q_m} → {e_b} in the Hausdorff metric.

*Proof.*
1. *A cut exists.* By the chart-form box (N14 §2.3), for a.e. pair (A′,B′) in the witness balls, q₀ ∉ R(A′) or
   q₀ ∉ R(B′). So one family has a.e. member with q₀ ∉ R. Pick a good g = g_m in it.
   - α_g(q₀) > 0 and q₀ ∉ R(g).
   - On N there is no advice that every evaluable model gives (V1, (LF)), so the advice range is {+,0,−} and d_g(q₀) ≤ 0.
2. *Edge points.* Let V⁺ := {e_l : l ∈ P(g)} and V⁻ := {e_l : l ∈ N(g)}. α and d have the strict sign of g at
   vertices.
   - A-case (g_a < 0 < g_b, small g_b): α(e_b) > 0, d(e_b) > 0, d(q₀) ≤ 0. So the d-line meets the edge at
     z ∈ (e_b, q₀], with α(z) > 0. The α-line meets it at σ ∈ (q₀, e_a).
   - B-case (g_a > 0 > g_b): α(e_a), d(e_a) > 0, α(e_b) < 0, d(q₀) ≤ 0. So σ ∈ (e_b, q₀), z ∈ [q₀, e_a), and α(z) > 0.
   - In both cases d(σ) < 0, and z ∈ cl F(g).
3. *The apex lies in Ω.* Suppose the d-line ∩ Ω misses {α = 0}.
   - Points of the d-line near z have α > 0, so d-line ∩ Ω ⊆ {α > 0}.
   - The convex set {α ≤ 0} ∩ Ω misses the d-line, so it lies on one side of it. It contains points near some
     e_l ∈ V⁻, where d < 0. So d < 0 on {α ≤ 0} ∩ Ω.
   - As s → 0 the α-lines converge to λ_{w\*} ∋ p\*. So for small s the α-line meets B₁. Points of B₁ near it with α > 0
     have d < 0, hence lie in R(−g). This contradicts N21.2.
   - So the apex a = {α = 0 = d} lies in Ω, and F(g) ∩ Ω = (a, z).
4. *Where the apex is.*
   - By N21.2, {α > 0} ∩ B₁ ⊆ {d > 0}, so d ≥ 0 on the α-line ∩ B₁.
   - The apex is not in B₁. Thm B (closure clause) gives K_a ⊆ g^⊥, but K_q ∩ K″ ≠ ∅ with P_{K″}(g) > 0 on B₁.
   - So d > 0 on α-line ∩ B₁, while d(σ) < 0. Hence a lies strictly between σ and B₁. This is (i).
5. *Limits.*
   - σ_m → e_b, because λ_{w\*} meets [e_a,e_b] only at e_b. The α-lines converge to λ_{w\*} as lines. This gives (ii)
     for a\*.
   - In the A-case |z_m − e_b| ≤ s_m.
   - z\* ≠ e_a: otherwise d-face points near e_a would give K_{e_a} ⊆ ℓ_{w\*} (Hausdorff continuity at vertices, R10b V2).
     But e_a ∈ K_{e_a} (Prop V), and e_a ∉ line(e_b, v_{k\*}) since v_{k\*} ∈ int Δ.
6. *(iii).* Every point of [a\*, z\*] is a limit of points p_m ∈ F(g_m), where K_{p_m} ⊆ g_m^⊥. Since g_m → w\* and K is
   Hausdorff-continuous, K_q ⊆ (w\*)^⊥ ∩ Δ = ℓ_{w\*} ∩ Δ.
7. *(iv).* Take q_m ∈ F(g_m) with q_m → z\*. Every Hausdorff limit K\* of K_{q_m} satisfies K\* ⊆ ℓ_{w\*}.
   - Test gambles: h = w\* − δ𝟙 + ηe_b with 0 < δ < η, both small. Then h ∈ N, h_b = η − δ > 0, h·v_{k\*} =
     −δ + ηv_{k\*,b} < 0, and in the B-case h_a = w_a − δ > 0.
   - *If z\* = e_b:* B_{e_b} accepts a.e. h with h_b > 0 whose acceptance is in the advice range (R1 Lemma 1.5). So K_{e_b} ⊆ {m·h ≥ 0} for these h, and
     K\* = K_{e_b} by V2.
   - *If z\* ∈ relint [e_a,e_b]:* this is the B-case. These h are good at both worlds of supp z\*, so by edge forcing
     (R1 Prop 2.8, applied to non-null subsets of small balls around h, then shrinking the balls) every limit K\* at z\*
     satisfies m·h ≥ 0.
   - *Conclusion.* Write m = e_b + t(v_{k\*} − e_b) ∈ ℓ_{w\*}. Then m·h ≥ 0 iff t ≤ (η−δ)/(η(1 − v_{k\*,b})), which tends
     to 0 as η ↓ δ. Points with t < 0 leave Δ. So K\* = {e_b}. (`lemmas_check.py` (2) evaluates this bound for every
     facet/crossing of T1.) ∎

**Corollary N21.7 (advice ranges; PROVED under the standing assumptions).** Write Av for the set of orientations h whose
acceptance is in the advice range.
- (a) For every b, acceptance is in the advice range for a.e. orientation h with h_b > 0.
- (b) Hence the advice range of a.e. mixed pair contains **both** acceptances (advice ranges ⊇ {+,−}).
- (c) K_{e_b} = {e_b} for every b.
- (d) For every edge prior q₀ with support S, every limit of K_q as q → q₀ (q interior) lies in Δ_S.

*Proof.*
- (a) B_{q_m} ⊆ Av a.e., so D_{K_{q_m}} ⊆ Av a.e. Since K ↦ 1_{D_K} is continuous into L¹(μ) at the credal set {e_b}
  (R1 Prop 3.1: P_{K_m} → P_{{e_b}} uniformly on bounded sets and {h_b = 0} is null), we get {h_b > 0} ⊆ Av a.e.
- (b) Every mixed g and −g each have a positive coordinate. Apply (a) for every b; a failing box exists at every b.
- (c) B_{e_b} ≈ (Av ∩ {h_b > 0}) ∪ {h ≥ 0} = {h_b > 0} is coherent with credal set {e_b}.
- (d) R4 (K4): its only hypothesis, acceptance in the advice range for a.e. h with h_S > 0, is (a). ∎

**Theorem N21.8 (main; PROVED).** Let T be T1 (any ε ∈ (0,1)). Assume:
- any decomposable domain with (LF);
- strictly guiding additive penalties (integral, or bounded charges vanishing on null sets given interior minimisers,
  N14 Thm C2);
- (R1), (R2).

Then:
- (a) If (TS) holds, then the advice range of a.e. mixed pair contains both acceptances, all vertex models are precise, and the cut structure
  of N21.6 is present at every vertex.
- (b) In particular, **T1 has no realisation satisfying (TS) on any (LF) decomposable domain on which a non-null set of mixed
  pairs has an advice range lacking one acceptance** (e.g. any domain with a non-null set of mixed pairs with advice range
  {+,0} or {0,−} anywhere, or with an open cone of mixed orientations that no evaluable model accepts).
- (c) On domains whose pairs meeting U′ are non-adjacent, there is no realisation at all (N15, which proves (TS) there).

*Proof.*
- (a) N21.4 gives (PC) and (NS). Then N21.6 and N21.7.
- (b) Contrapositive of (a).
- (c) N15.9(a). ∎

*Scope.* §§2–3 hold for every all-facing triangle in general position. §5 needs a failing box at b and gives (a) for that
b only. For a general all-facing triangle, N12 Thm 3.1 guarantees one failing pair, hence (a) (acceptance in the advice range) for one world.

---

## 6. What remains

**(E5a) Pinning near p\* (failure of A-accumulation in (TS)).** Suppose A_τ ∩ B(p\*,ρ) = ∅ for some τ and ρ.

*Proposition N21.9 (PROVED, structure).* Then there are an open O ⊆ B(p\*,ρ), with p\* ∈ cl O, and a world j such that:
- (i) v_k ∈ K_q and Ψ(q,σ) = 0 for all q ∈ O and σ ∈ [σ₁,σ₂] (an interval containing a crossing);
- (ii) every segment from O to V_j ∩ Ω contains a prior Q with K_Q = {v_k};
- (iii) acceptance is in the advice range for a.e. h with v_k·h > 0.

*Proof.*
- (i) Take G = int({Ψ(·,σ₁) ≥ 0} ∩ {Ψ(·,σ₂) ≥ 0}), which is convex by N21.1, with p\* ∈ cl G, and O := G ∩ B(p\*,ρ).
  - On O, Ψ(·,τ) ≤ 0 by hypothesis and ≥ 0 by concavity in σ, so Ψ(·,τ) = 0.
  - Concavity with the interior zero at τ forces Ψ(q,·) ≡ 0 on [σ₁,σ₂].
  - Then v_k ∈ K_q (N12 Prop 2.5(c) argument).
- (ii) O ⊆ Γ_{v_k} ∩ α_{v_k} (R10b §1), and V_j ∩ Ω ⊆ Γ ∩ β (UVN). Apply Lemma M on int conv(O ∪ V_j) ⊆ Γ, as in
  R10b Lemma P.
- (iii) B_Q ≈ {v_k·h > 0} ⊆ Av. ∎

By N21.3, each exterior h near the crossing is silent on O and accepts −h at Q. Along (Q, e) it must cross a d-face, at
priors with K ⊆ h^⊥ ∩ W_{v_k} ⊆ B(v_k, C|h − w|) (R10b Lemma M Step 1). So (E5a) is a "precise v_k wall" between the
pinned core and e_j. I could not exclude it.

**(E5b) Frozen facet (failure of B-accumulation).** If A_τ accumulates at p\* for all τ but B_{τ₀} does not:
- the proof of N21.4 item 5 shows n_τ ≡ n on all of (0,1) (CHECKED);
- B_τ accumulates at p\* at most for τ ∈ [τ_i, τ_j]. At any other τ, accumulation would give the c-cluster sign
  contradiction of item 5 (PROVED);
- on λ ∩ B₁, v_k ∈ K_q (pinned along a segment, not on an open set; PROVED as in item 5).

Theorem PL and Lemma M need open pinned sets, so I could not exclude (E5b) either.

**(E4′) The near-all-orientation cut.** Under (TS), §5 shows that a realisation lives on a domain where the advice range of a.e. mixed pair
contains both acceptances, with:
- precise vertex models;
- edge-confined boundary limits;
- at every vertex b, cut d-faces with apexes on [e_b, p\*] and degenerate credal sets on line(e_b, v_k).

R4 §9 (identity cap) and its edge blow-up show these cuts are consistent *at the vertex scale* with the rigid facet data
x₊/x₋. That is the case a\* = e_b. So no argument local to the vertices can close (E4′). This is the same locality barrier
as R10b Prop L, now at the vertices.

**CONJECTURE N21.** None of (E5a), (E5b), (E4′) occurs in a T1 realisation. Evidence:
- each forces acceptance to be in the advice range on a large global set, and precise priors;
- R1's identity-type precise layers fail near the facets: in a chart for the advice range {+,0,−} with a silence cell of nonempty
  interior, the silence cell reaches ∂Δ (follow a recession direction of the closed convex cell; PROVED), while precise
  priors avoid silence a.e. (R4 Lemma C2);
- no construction is known.

**Next step (highest payoff).** Combine Cor N21.7(d) (edge confinement) with the chord structure. Every pivot chord
λ_τ ends at a boundary point y_τ, where every limit credal set lies in an edge face, contains the zero point of h(τ) on
that edge, and lies in {m·h(τ) ≥ 0}. This gives a "boundary edge map" that the projective chord map must respect on all
three facets at once. It is a concrete finite-dimensional consistency test for (E4′).

---

## 7. Files (`n21py/`)

| File | Purpose | Result |
|---|---|---|
| `t1_lambda_per_vertex.py` | six Λ_{ab} for T1 at x₊, x₋ (uses `../r15py` read-only) | every b has exactly one failing box; Λ_{ab}Λ_{cb}/β² = 1.000000 |
| `lemmas_check.py` | (1) sector lemma on random charts for the advice range {+,0,−}; (2) vertex-precision bound on line(e_b, v_k); (3) n = 2 restriction counterexample | (1) 0/908 violations; (2) t-bound = (η−δ)/(η(1−v_{kb})) → 0; (3) incoherent for t ∈ {.25,.3,.35} |

All NUMERICS are sanity checks. No theorem above depends on them, except that the "every b" clause of N21.7(b)
for T1 is the exact algebraic statement Λ_{ab}Λ_{cb} = β² < 1 combined with x₊² > κ (R4 G1), which the script confirms.
