# DD2 (round 32, BRIEF24). General closed defence covers: what they are forced to be, why the decisive lemma is a static global condition, and an obstruction to audit's plan as specified (bounded seed regions)

17 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full proof here, one reader (me), not refereed;
- **CHECKED**: exact finite computation, or a step-by-step reading of a cited statement;
- **NUMERICS**: sampled or floating point; nothing depends on it;
- **CONJECTURE**.

Scripts are in `dd2py/`. Run `python3 -I <script>.py` inside that folder; outputs are in `*.out`. No assumption is
added. Every extra hypothesis is a hypothesis of a stated result and is named where it is used.

Read: BRIEF24, AUDIT_CC_seeds, AUDIT_CC_plan, AUDIT_CC_summary, CC1, CC2 (§§0, 4), X1, Y1, AUDIT_BB, write-up §2.
DD1_notes.md appeared at the end; §5 compares.

**Setting.** Full four-advice domain, three worlds, Gaussian μ. A coherent selection p ↦ C_p (the patched posterior
family of AUDIT_CC_plan, or any other where stated), continuous in measure. Records, composition and the transition
lemma are as in X1 §1. A **defence map** assigns to every model X a triple A(X) = (A_1(X), A_2(X), A_3(X)) of subsets of Δ.
The intended reading is A_i(X) = {p : C_p ⪯_i X}.

---

## 0. Outcome

1. **The relaxation buys freedom only at the selected models (§2; PROVED).**
   - General closed defence covers are exactly (S). Each defence region is a closed **lower set** of the world-i
     preorder that the selected models induce on Δ (Lemma 2.2).
   - Two consequences follow.
     - If the selected sections are coordinate thresholds (r(C_q) = q, DD1's scheme), **every** competitor's region
       is forced to be a coordinate threshold (Cor 2.3).
     - If the index preorders are total, every region is a cut of that chain (Cor 2.4).
   - On every edge of Δ, any closed cover is forced to be a threshold anyway (Prop 2.5). In the posterior part of the
     interior it is star-shaped toward e_i.
   - So "general closed covers" means, precisely, "general index preorders on the selected models". The structural
     conditions are listed as (D0)–(D9) in §2.7. They include the seeds and a defence-map form of the coupling warning
     (Lemmas 2.8–2.10).
2. **The decisive lemma is a static global condition (Thm 3.1; PROVED).** A defence map, once fixed for every model,
   comes from a successful system iff it is closed-KKM, record-determined, and its **Horn closure is clean**. With the
   whole map fixed, there are no disjunctions, no topology left, and no limit stages. A model-by-model construction
   has genuine dead ends under any explicit local invariant. This is X1 §5, imported; the exact invariant is X1's
   plan invariant.
3. **Explicit obstruction (Thm 3.3; PROVED modulo the same imported chain as CC1 Thm 4.1).**
   - **Statement.** Whatever the worlds do on a region R of problems, only the **conic part** of R is visible to
     competitiveness at T1. Assume every world judges comparisons whose records lie off R inside a finite-seed
     countably additive envelope (CC1's class, restricted to R^c). If R is bounded up to a cone R_0, the additive
     shadow extends by radial transport through R ∖ R_0. If R_0 = ∅, T1 cannot be a selected model.
   - **Consequence.** Audit's bundles live on "small bounded neighbourhoods" R_S. For them the decisive lemma fails
     whatever compensation is used **inside** the bundles, unless the off-R comparisons leave CC1's envelope class.
   - **Intrinsic or artefact.** The obstruction is intrinsic to closed covers: it uses only competitiveness and
     continuity of the selection, so it applies to DD1's thresholds and to every relaxation. It is an artefact of
     **boundedness**.
   - **Repair.** Conic bundle regions cost nothing, since audit's Lemmas 1–4 survive verbatim (Remark 3.5). Then the
     residual is localized to the cone R_0 (Prop 3.6). CONJECTURE 3.7, supported by CC2 Cor 5.7: R_0 must surround
     ∂D_{T1}.
   - **Caveat.** DD1 Lemma 2.7, which makes seeds harmless, uses the same boundedness, so it must be re-checked
     for conic cells (§5).
4. **Explicit bundle-tracking invariant (§3.4; PROVED).** "Valued bundle worlds" form an explicit class.
   - **Definition.** World 1 integrates a superadditive value V of the *whole* bundle ladder vector over bundles,
     plus an off-R part.
   - **Properties.** The class retains the seeds at every scale and keeps bundle identity. It permits compensation
     between bundles and is transitive by construction.
   - **Static reduction.** By CC2 Thm 4.1, strict Bayes plus upper semicontinuity suffices, with no limit stages.
   - **Forced non-additivity.** The seeds force V < 0 on at least one record of an explicit conversion cycle, each of
     whose steps is priced ≥ 0 by equal-weight counting (Lemma 2.10, CHECKED exactly).
5. **Not achieved:** a full system (task 3). The lemma fails for audit's specification with bounded R_S whenever
   comparisons off R are envelope-type (Cor 3.4). The conic version is reduced to Prop 3.6 and CONJECTURE 3.7, and
   is neither proved nor refuted.
6. **Fragment check (§3.5; CHECKED).** With world 1 vetoing every R-record that the bundle relation (B) rejects, the
   forced world-2 records at the edge {1,2} never compose into a strict reversal. The same holds for world 3 at the
   edge {1,3}. This is an exhaustive search on the cell fragment. So a world-1 veto **alone** is not refuted at the
   cell level; audit's veto warning needs vetoes at several worlds.

---

## 1. Notation

- Δ(p,q) := {C_p ≠ C_q}. d_{p,q} := rec(C_p, C_q).
- S_i(p) := A_i(C_p). We write q ⊑_i p iff q ∈ S_i(p), i.e. C_q ⪯_i C_p. This is the **index preorder** at world i.
- Seeds (AUDIT_CC_seeds §2):
  - bases B_k = C_{q_k}, with q_1 = u;
  - bundle regions R_S = f_S((0,1)) and R = ⋃_S R_S;
  - the bundle ladder record d(r;t) ∈ {−1,0,1}^{21};
  - the seed competitors X_k^A, which retain B_k ⪯_1 X_k^A for every measurable A ⊆ (0,1).

---

## 2. Structural conditions on X ↦ A(X) (task 1)

### 2.1 Exact correspondence

**Theorem 2.1 (PROVED).** Fix a coherent selection C. A defence map A comes from a successful system (strict (G),
(IB), (LA), (S), (C)) with selection C if and only if all three of the following hold.

- **(D1) Closed KKM.** Each A_i(X) is closed, and every p has some i ∈ supp p with p ∈ A_i(X).
- **(D2) Record determination.** If rec(C_p, X) = rec(C_q, Y), then p ∈ A_i(X) ⟺ q ∈ A_i(Y).
  - Equivalently, A_i(X) = {p : rec(C_p,X) ∈ 𝒜_i^sel} for a set 𝒜_i^sel of records with base in the selection.
- **(D3) Horn-clean.** Let E = (E_i) be the least family of record sets with these closure properties:
  - E_i contains 𝒜_i^sel, all i-worsening records and ι;
  - E_i is closed under composition of composable records (X1 Lemma X1.1.2);
  - E is closed under protection (R4): if rec(X, C_p) ∈ E_j for every j, then rec(C_p, X) ∈ E_j for every j.

  Then E is **clean**:
  - no nontrivial i-improving record lies in E_i;
  - E_i ∩ {records with selected base} = 𝒜_i^sel, so no rejected selected comparison is derived;
  - no incoherent X has rec(C_p,X), rec(X,C_p) ∈ E_j for all j (Csel).

In that case X ⪯_i Y :⟺ rec(X,Y) ∈ E_i is a successful system. It is the least one with this defence map.

*Proof.*
- (⇒) Put 𝒜_i := {rec(X,Y) : X ⪯_i Y}. The transition lemma (X1 Thm X1.1.1) gives the composition and guidance
  properties of 𝒜_i, and (IB) gives (D2). (S) gives (D1). Undominatedness of C_p gives (R4) inside 𝒜, and (C) gives
  (Csel). Since E ⊆ 𝒜 and 𝒜 is clean, E is clean.
- (⇐)
  - E_i satisfies the four conditions of X1 Thm X1.1.1, so each ⪯_i is a preorder with strict (G) and (IB).
  - Cleanness of the selected part makes the sections exactly A_i(X). Then (D1) gives competitiveness on supp p and
    closed sections.
  - (R4) makes every C_p undominated, which gives (LA).
  - (C): by thm:kkm every undominated model ties everywhere with some C_p. A model tied with it ties with C_p, so it
    is coherent by (Csel); it is also undominated.
- This is X1 Thm X1.3.3(d),(e) with the exact plan V(p,i,X) = Δ ∖ A_i(X). ∎

### 2.2 Lower sets

**Lemma 2.2 (PROVED).** In any successful system:
- (a) each ⊑_i is a preorder on Δ, and its principal lower sets S_i(p) are closed;
- (b) each A_i(X) is a closed ⊑_i-lower set: if p ∈ A_i(X) and q ⊑_i p, then q ∈ A_i(X);
- (c) if X ⪯_i Y, then A_i(X) ⊆ A_i(Y);
- (d) e_i ∈ A_i(X) for every X, by KKM at the vertex e_i, whose support is {i}.

*Proof.* (a)–(c) are transitivity, applied as C_q ⪯_i C_p ⪯_i X and C_p ⪯_i X ⪯_i Y. Closedness is (D1) for X = C_p. ∎

**Corollary 2.3 (threshold heredity; PROVED).** Suppose S_i(p) = {q : q_i ≥ p_i} for all p, i (DD1's choice
r(C_q) = q). Then for **every** model X:
- A_i(X) = {q : q_i ≥ r_i(X)}, with r_i(X) := min{q_i : q ∈ A_i(X)};
- (D1) holds iff Σ_i r_i(X) ≤ 1. Slack is allowed, so r(X) ∈ Δ is not forced.

*Proof.*
- By Lemma 2.2(b), A_i(X) is upward closed in coordinate i. It is nonempty by (d) and compact, so the minimum is
  attained.
- **KKM ⇐.** If p_i < r_i for every i ∈ supp p, then 1 = Σ_{supp p} p_i < Σ r_i ≤ 1, which is a contradiction.
- **KKM ⇒.** If Σ r_i > 1, then p := r/Σr has p_i < r_i on supp p, so no supported world defends p. ∎

**Corollary 2.4 (total index preorders give cuts; PROVED).** Suppose ⊑_i is total. Then each A_i(X) is a closed
initial segment of the chain (Δ, ⊑_i). It is either principal, A_i(X) = S_i(p*), or a closed non-principal cut. So
X is placed at one cut of the world-i chain of selected models.

If ⊑_i is represented by a lower semicontinuous f_i (S_i(p) = {f_i ≤ f_i(p)}), then
A_i(X) ∈ {{f_i ≤ c}, {f_i < c}}. The cover is then DD1's threshold scheme after reparametrizing Δ by the "frontier
map" f = (f_1,f_2,f_3). DD1 is the case f = −id. *Proof.* Lower sets of a chain are initial segments. ∎

*Reading.* Relaxing the competitors' regions while keeping thresholds at the selected models gives **nothing**.
Every genuine relaxation is a relaxation of the selected sections S_i(p). The only freedom not of threshold type
(after a reparametrization) comes from **incomparable** pairs of selected models in some ⊑_i.

### 2.3 Guidance: vertices, edges, interior

**Proposition 2.5 (edge rigidity; PROVED; NUMERICS in `edge_chain.out`).**
- Let C be any selection that equals the posterior boundary family K⁰ on ∂Δ; the patched family does.
- On the edge [e_i, e_j], the edge models form a pointwise chain at worlds i and j: moving toward e_i improves world
  i and worsens world j, weakly everywhere and strictly somewhere.
- Hence, for every model X, A_i(X) ∩ [e_i,e_j] = {p : p_i ≥ a_i(X)} and A_j(X) ∩ [e_i,e_j] = {p : p_j ≥ a_j(X)},
  with a_i(X) + a_j(X) ≤ 1. **On ∂Δ every closed cover is a coordinate threshold** at the two edge worlds.

*Proof.*
1. For p on the edge with odds o = p_i/p_j, K⁰_p is the edge segment with odds in [o·α, o·β]. Here
   α = min_k v_{ki}/v_{kj} and β = max_k v_{ki}/v_{kj}, with 0 < α < β.
2. For a problem h on which h_i and h_j have the same sign, the advice does not depend on o.
3. For h_i > 0 > h_j: D_K accepts h iff oα > |h_j|/h_i, accepts −h iff oβ < |h_j|/h_i, and is silent otherwise. As o
   increases, the advice moves monotonically from −, through 0, to +. This is better at world i and worse at world j.
4. The case h_i < 0 < h_j is symmetric. Strictness holds because the thresholds move with o.
5. By weak (G), q closer to e_i gives q ⊑_i p. So A_i(X) ∩ edge is a closed ⊑_i-lower set of this chain (Lemma 2.2)
   containing e_i. That is a segment {p_i ≥ a}.
6. Covering the edge requires the two segments to overlap. ∎

**Corollary 2.6 (PROVED, via Y1.1).** At interior p outside the bumps' supports, the posterior i-ray from p to e_i,
q = ν(p⊙(s,1,1)) for s ≥ 1, is a straight segment, and C_q is pointwise weakly i-better than C_p there (Y1.1(a)).
Hence each A_i(X) is star-shaped toward e_i along such segments. Coordinate thresholds are a special case; so are
regions bounded by any curve that every segment to e_i crosses once.

### 2.4 Protection and (C) in index form

**Lemma 2.7 (PROVED).**
- C_p is undominated iff [X ⪯_j C_p at every j] implies p ∈ ⋂_j A_j(X). For X = C_q: q ∈ ⋂_j S_j(p) implies
  p ∈ ⋂_j S_j(q).
- For every X, ⋂_j A_j(X) ≠ ∅. This is the KKM lemma applied to (D1), i.e. Thm kkm.
- (C) is a condition only on models tied everywhere with selected ones. Ties between two selected models are
  permitted.
- For the posterior part, Y1.1′(i) (imported) excludes such ties, giving ⋂_j S_j(p) = {p}.

### 2.5 Seeds and the coupling warning

**Lemma 2.8 (seeds; PROVED).**
- q_k ∈ A_1(X_k^A) for every A, hence S_1(q_k) ⊆ A_1(X_k^A).
- Under thresholds this is exactly r_1(X_k^A) ≤ (q_k)_1 (audit), and by Cor 2.3 nothing more is implied about the
  shape of A_1(X_k^A).
- By (D2), the same holds for every transport: q ∈ A_1(Y) whenever rec(C_q,Y) = rec(B_k, X_k^A).

**Lemma 2.9 (coupling in defence form; PROVED).**
- Split (0,1) into A_1, …, A_4, and let Z_0 be the model equal to B_k on R(A_k) and to B_1 elsewhere.
- Let Z_1 be Z_0 with seed k applied on R(A_k). Let Z_1′ be Z_1 rearranged back to Z_0's advice on the six pair
  regions.
- Then **rec(Z_1, Z_1′) ∉ 𝒜_1 in every system retaining the seeds**, and so is every record with this transport.
- *Proof.*
  - The four seed transports have disjoint supports, and Z_0 agrees with B_k on R(A_k), so Z_0 ⪯_1 Z_1.
  - Z_1′ equals Z_0 except on f_∅((0,1)). There it is world-1 correct, since X_k is correct on R_∅ for every k,
    whereas Z_0 is wrong. So Z_1′ ≺_1 Z_0 by strict (G).
  - Accepting Z_1 ⪯_1 Z_1′ would give Z_0 ⪯_1 Z_1′, a strict reversal. ∎
- *Defence form.* For every selected C_p that agrees with Z_1 on the support, p ∉ A_1(C_p ⊕ rec). Generically there
  is no such p: selected models do not see the bundle partition. So the warning constrains only comparisons between
  non-selected models, through (D3). It does **not** constrain any defence region directly.

**Lemma 2.10 (conversion cycle; CHECKED exactly, `cycle_check.out`; PROVED consequence).**
- On any one bundle set, consider the chain B_1 → X_1 → B_2 → X_2 → B_3 → X_3 → B_4 → X_4 → B_1′, where B_1′ is
  B_1 corrected on the cell R_∅.
- The four seed steps are accepted. The four conversion steps X_1→B_2, X_2→B_3, X_3→B_4 and X_4→B_1′ have
  world-1 rank-change sums 1, 1, 1 and 0. So equal-weight counting prices each of them ≥ 0.
- The composite B_1 → B_1′ is a strict world-1 improvement. Hence **every** system retaining the seeds rejects at
  least one conversion at world 1, on every bundle set, in every context.
- So world 1 cannot be "count-additive with seed exceptions". In a valued world (§3.4) this reads
  Σ V(conversions) < 0.

### 2.6 (IB) transport between nearby selected models

Splice identities hold for any p, q and symmetric D ⊆ Δ(p,q). Let Y_D be C_q off D and C_p on D, and let
D′ := Δ(p,q) ∖ D. Then:
- rec(Y_D, C_p) = rec(C_q, Y_{D′}), so Y_D ⪯_i C_p ⟺ q ∈ A_i(Y_{D′});
- q ∈ A_i(Y_D) ∩ A_i(Y_{D′}) ⇒ q ⊑_i p;
- p ∈ A_i(Y_D) ∩ A_i(Y_{D′}) ⇒ p ⊑_i q (PROVED, by transitivity).

With thresholds, the finite splice cube {Y_U} over a partition of Δ(p,q) passes the splice rules. Write α_i(U) for
"switching U from q-advice to p-advice is accepted at world i", and β_i(U) for the reverse. The assignment
r(Y_U) = p if piece 1 ⊆ U, and q otherwise, satisfies:
- α_i(U) ∧ α_i(U′) ⇒ α_i(U∪U′), and the β-analogue;
- the transfer rules α_i(U∪V) ∧ β_i(V) ⇒ α_i(U), and β_i(U∪V) ∧ α_i(V) ⇒ β_i(U).

I checked these rules by hand. I did **not** check the full Horn closure of the cube, and guidance on the pieces
would further restrict the choice of piece 1. So this is evidence that splices give no cheap obstruction, not a
proof.

### 2.7 Summary of the conditions

| | condition | source |
|---|---|---|
| (D0) | A_i(X) ∋ e_i | KKM at vertices |
| (D1) | closed; KKM on supp p | (S) |
| (D2) | depends only on rec(C_p, X) (transport) | (IB) |
| (D3) | Horn closure clean (composition, (N), (R4), (Csel), agreement on selected records) | transitivity, strict (G), protection, (C) |
| (D4) | closed ⊑_i-lower sets; monotone along accepted comparisons | Lemma 2.2 |
| (D5) | thresholds at selected models ⇒ thresholds everywhere; total ⊑_i ⇒ cuts | Cor 2.3, 2.4 |
| (D6) | thresholds on every edge, at the edge worlds | Prop 2.5 |
| (D7) | star-shaped toward e_i along posterior rays (outside bumps) | Cor 2.6 |
| (D8) | S_1(q_k) ⊆ A_1(X_k^A) for all A, and transports | Lemma 2.8 |
| (D9) | rearrangement records (Lemma 2.9) and ≥ 1 conversion per cycle (Lemma 2.10) rejected at world 1 | seeds + strict (G) |

---

## 3. The assignment lemma (task 2)

### 3.1 It is a static global condition

**Theorem 3.1 (PROVED).** A system exists with selection C and retained seeds iff some single defence map A on all
models satisfies (D1), (D2), (D3) and (D8).

- **Limit stages.** None are needed: the map is fixed at once. Its literals contain every acceptance and every
  rejection out of selected models, so closed sections and competitiveness are built in.
- **Building A model by model.** Cleanness of the Horn closure passes to unions of chains, since a derivation is
  finite. But a clean partial map can be a **dead end**. An extendable partial map extends iff its literals are
  finitely satisfiable together with **some single fixed plan** for the unassigned models (X1 Thm X1.3.3, Prop.
  X1.3.2). Dead ends with clean closure exist:
  - X1.5.1 (protection detects it);
  - X1.5.4, S4 (clean even with protection in the fragment);
  - P3 Ex. 2 (closure only through the limit rule).

  These are imported, not re-derived.
- So no explicit *local* invariant is sufficient in general. Explicit invariants exist only for restricted classes:
  CC1's envelopes, CC2's valued worlds, and §3.4 below. In each, the lemma becomes a static condition on the selection.

*Proof.* Thm 2.1 together with Lemma 2.8, and X1 Thm X1.3.3 for the model-by-model version. ∎

### 3.2 The obstruction: only the conic part of a non-additive region is visible

**Theorem 3.3 (PROVED modulo CC1 Thm 4.1's imported chain: D1, M3.7(d), M3.8, M3.9 = BB2 Thm 6.1, Q4.1).**

*Hypotheses.*
- (i) On the full domain, q ↦ C_q is coherent and continuous in measure on Δ, with C_u = D_{T1}, and C_q is
  competitive on supp q for every q.
- (ii) R ⊆ H is measurable and R ⊆ R_0 ∪ B. Here R_0 is conic (h ∈ R_0 ⇒ th ∈ R_0 for all t > 0) and B is bounded.
- (iii) Each world i has the following envelope data over R^c:
  - a bounded strictly guiding penalty λ_i;
  - a set Ψ_i of bounded φ ≥ 0 on R^c, with a member φ_i^+ > 0 a.e. on R^c;
  - a finite set G_i of records on R^c, each with an (E)-witness in Ψ_i.

  Every accepted C_q ⪯_i X **with X = C_q a.e. on R** must satisfy Λ_iX − Λ_iC_q ∈ 𝒦_i ∪ ⋃_{g∈G_i}(g + 𝒦_i).

*Nothing* is assumed about comparisons whose records meet R. Closed sections, (C), the seeds, and the defence-region
shape are not used.

*Conclusions.*
- (a) For every tuple τ = (φ_i) ∈ ∏ Ψ_i and every q, some w ∈ Δ_{supp q} makes C_q a pointwise weak w-Bayes model of
  ℓ^τ = (φ_iλ_i) a.e. **off R_0**. This is not merely off R.
- (b) If R_0 is null, T1 is not a selected model, so the assumed system does not exist.

*Proof.*
1. **Off R (CC1 Thm 3.1(a), restricted).**
   - Run CC1's proof using only competitors X that agree with C_q on R. Their values z⁺(X) form a convex compact set
     (Lyapunov). Separation then gives (WB) a.e. on R^c, unless some such X has every z_i(X) < 0.
   - In that case, the shrunken X_t (Lyapunov again) have records supported off R. By (iii) they are rejected at
     every world in supp q for small t, since the seeds are finite with positive (E)-margins. This contradicts
     competitiveness.
2. **Radial transport.**
   - Let B ⊆ {|h| ≤ M} and T(h) := h + Mh/|h|. Then T is a diffeomorphism of H ∖ {0} onto {|h| > M} that preserves
     null sets both ways and keeps each h on its ray, so T(h)_1 > 0.
   - For h ∈ B ∖ R_0, the ray of h misses R_0 (R_0 is conic), and |T(h)| > M. So T(h) ∉ R.
   - Every C_q = D_{K_q} is a cone, so C_q(h) = C_q(T(h)). World ranks at h and T(h) agree, since the signs agree.
3. **The transported field.**
   - Define ℓ′_i(h,a) := φ_i(T h) λ_i(T h, a) on R ∖ R_0, and ℓ′ := ℓ^τ elsewhere. This is a bounded, strictly
     guiding additive field.
   - (WB) for ℓ′ at h ∈ R ∖ R_0 is literally (WB) for ℓ^τ at T(h) ∉ R. So the (WB) weights of ℓ′ off R_0 are those
     of step 1.
4. **When R_0 is null.**
   - ℓ′ is a global strictly guiding bounded additive field. Each C_q is weak-Bayes for it at a weight supported in
     supp q.
   - CC1 Lemmas 3.3, 3.4 and 3.4′ (closed graph from continuity; Brouwer–Browder covering) give (γ₀) and (γ) for ℓ′,
     as in CC1 Cor 3.5. That corollary's first two bullets need neither (P) nor envelopes.
   - T1 = C_u satisfies (WB) at some w. CC1 Lemma 4.2 puts w in int Δ.
   - Steps 6–8 of CC1 Thm 4.1 (D1; BB2 Thm 6.1; Q4.1/M3.8 on the full domain) give the contradiction. The tie step of
     CC1 Thm 4.1 is not needed, since T1 is itself selected. ∎

**Corollary 3.4 (audit's plan as specified; same status).** Audit's bundle regions are bounded subsets of small
bounded neighbourhoods of the cell centres. Take any extension retaining audit's seeds in which comparisons off R are
judged within finite-seed countably additive envelopes. Additive compensation off R is such a case. Then no such
extension has competitive choice through T1:
- whatever world 1 (or any world) does on R: bundle-wise (B), compensation between bundles, valued bundles, vetoes;
- with any defence regions: DD1's thresholds, general closed covers, or none at all.

**Intrinsic or artefact.** Intrinsic to closed covers: only competitiveness and continuity are used. An artefact of
two choices:
- (α) **bounded** seed regions;
- (β) envelope-type comparisons off R.

The bundles' internal non-additivity is irrelevant, because every coherent model reads a bounded region off the far
parts of its rays.

**Remark 3.5 (the free repair: conic bundle regions; PROVED by reading audit's proofs).**
- Replace each R_S by a narrow open circular cone around the centre ray h^S, inside CC1's open polyhedral cell cone.
- It keeps CC1's constant patterns. It keeps an angular distance from the coordinate planes, which is what the
  audit's repair needed. Its Gaussian measure is finite and positive, so measure isomorphisms f_S exist.
- Audit's Lemma 1 (bundle preorder), Lemma 2 (closed graph), Lemma 3 (certificates at every scale) and Lemma 4
  (undominated bases with guidance at worlds 2 and 3) never use boundedness.
- Conic bundles are therefore the correct version of the plan. Theorem 3.3 then leaves R_0 = ⋃ R_S.

**Proposition 3.6 (the residual for conic regions; PROVED).**
- Under (i)–(iii) with R_0 ≠ ∅: for every τ, the field ℓ^τ off R_0 has (γ₀) off R_0. That is, every weight t is a
  weak-Bayes weight off R_0 of some selected model (CC1 Lemma 3.4′ for the off-R_0 correspondence).
- T1 is weak-Bayes off R_0 at an interior weight (CC1 Lemma 4.2). Its open sets of problems just outside a facet
  can be chosen off cl R_0. The cone R_{34} has its centre (1, 1, −0.911) close to the facet point (1, 1, −0.875).
  But a narrow cone around that centre leaves the gambles (1, 1, −t), t ∈ (0.875, 0.9), and their neighbourhood,
  free.
- **What is not established.** The imported chain needs a global field with (γ). On R_0 the selection's charts
  (patterns of K_p vary on the cells; `patterns.out`) need not be linear in the Bayes weight, so ℓ^τ need not
  extend.

**CONJECTURE 3.7 (localization).** Under (i)–(iii), if cl R_0 misses an open conic neighbourhood of some boundary ray
in a middle arc of a facet of D_{T1}, then T1 is not selected.
- *Evidence.* CC2 Cor 5.7 proves this for a rank-weighted Brier core off R_0, with (H3) and (H4).
- *Consequence if true.* Every CC1-type cell has constant patterns for all bases, T1 included, so it avoids
  ∂D_{T1}. Retained seed cells must therefore **accumulate** conically at essentially all of ∂D_{T1}. Otherwise the
  comparisons off R must leave the envelope class: infinitely many seeds with vanishing margins, charges, or
  lexicographic levels (CC1 §5, items 1–2).

### 3.3 Why the obstruction is not visible inside the bundles

Within R nothing goes wrong. The bundle relation (B), and the valued worlds below, are transitive, closed in measure
and retain certificates at every scale. The failure is the T1 no-go **off R**, transported into R by the cone
structure of coherent models. This is why every bundle-internal repair (compensation rules, bundle bookkeeping,
choice of covers) is beside the point while R is bounded.

### 3.4 The explicit bundle-tracking invariant (for conic R)

**Definition.** Let D be the finite set of realizable bundle ladder vectors. Let V: D → [−∞, ∞) satisfy:
- (V0) V(0) = 0;
- (V1) V(d+d′) ≥ V(d) + V(d′) whenever d, d′ are composable;
- (V2) V(d) ≥ 0 for d ≥ 0, and V(d) < 0 for d ≤ 0 with d ≠ 0;
- (Vs) V(g_k) ≥ 0 for k = 1, …, 4.

Put Φ_1(r) := ∫_0^1 V(d(r;t)) dt + ℓ_1^{off}(r|_{R^c}), with ℓ_1^{off} any strictly guiding additive (or CC2-valued)
loss off R.

**Proposition 3.8 (PROVED).**
- (a) Φ_1 is a valuation in the sense of CC2 Def 4.0, so A_1 := {Φ_1 ≥ 0} is a world: transitive, strict (G), (IB).
- (b) It retains every seed: Φ_1(g_k^A) = |A|·V(g_k) ≥ 0.
- (c) Bundle identity is kept automatically: Φ_1 reads whole bundle vectors. The coupling contradiction of
  Lemma 2.9 cannot occur, by (a).
- (d) Compensation between bundles is permitted exactly where V > 0. Lemma 2.10 forces V < 0 on some conversion of
  each cycle.
- (e) An example is V_B := 0 on (B)-accepted vectors and −1 otherwise. It satisfies (V0)–(V2) and (Vs), by audit's
  Lemma 1 (two seed-type vectors never compose). It allows compensation only from off R.
- (f) With valuations Φ_2, Φ_3 of the same kind, a full system exists **if** the selection is strictly p-Bayes for
  (Φ_k) and p ↦ Φ_k(rec(C_p,X)) is upper semicontinuous (CC2 Thm 4.1; sufficiency only, the converse is not
  claimed). So inside this class the assignment lemma is replaced by a static condition, with no limit stages.

*Proof.*
- (V1) integrates over t. ℓ^{off} is additive, and records on R and R^c compose separately.
- For (e): V_B ∈ {0, −1}. (B) is composition-closed, so V_B(d+d′) = 0 when both values are 0, and the bound −2 is
  trivial otherwise. (V2) holds because (B) contains no nonzero d ≤ 0. ∎

Theorem 3.3 applies verbatim to this class when R is bounded and the off-R parts are additive. For conic R the class
is exactly where CONJECTURE 3.7 has to be decided.

### 3.5 Fragment check of the veto

Suppose world 1 judges R-records by (B) alone. Then, at an edge-{1,2} index, every R-record that (B) rejects must be
accepted at world 2.

`veto_bfs.py` (CHECKED, exhaustive) does the following:
- builds all 3^7 cell patterns with advice in {+,0,−};
- uses the 11 edge-{1,2} posterior patterns, computed exactly on a 120-grid;
- uses 17 832 forced (base, change) records and the world-2 background moves;
- computes the full transitive closure.

No pattern reaches a strictly world-2-better pattern. The same holds for edge {1,3} and world 3. The reason is
Prop 2.5: edge models form a chain, so their forced records cannot cancel each other's world-2 losses.

So a veto at world 1 alone survives edge competitiveness at the cell level. This sharpens audit §3, whose argument
uses vetoes at all worlds. It does not bear on Theorem 3.3, which is about the continuum off R.

---

## 4. Assembly (task 3)

Not possible as specified. Corollary 3.4 refutes it for bounded seed regions and envelope-type compensation off R. It
does so modulo the imported chain, whose status is that of CC1 Thm 4.1: one reading of BB2 Thm 6.1, unrefereed.

For conic seed regions:
- the structural conditions (§2.7) and the static reduction (Thm 3.1, Prop 3.8(f)) are in place;
- what is missing is a selection that is strictly p-Bayes for valued worlds through T1, with R_0 surrounding
  ∂D_{T1} (CONJECTURE 3.7);
- or comparisons off R that leave CC1's envelope class.

---

## 5. Comparison with DD1

DD1_notes.md appeared while I was finishing; I read §§0–3. Agreements, complements and one tension:

- **Same reduction.**
  - DD1 Thm 2.1(a) is my Cor 2.3 (threshold heredity).
  - DD1 Thm 2.1(c) is my Σ r_i ≤ 1. Both notes find that r ∈ Δ is not forced.
  - DD1 §3.1 is the threshold case of my Thm 2.1/3.1: the decisive lemma is a static condition on the whole map r.
- **DD1's obstruction.** DD1 found one obstruction, designated-index windows (DD1 §2.4). It lives entirely at the
  selected layer. By Cor 2.3 it cannot be removed by relaxing competitors' regions, which agrees with DD1's
  conclusion that "the relaxation was not needed".
  - Prop 2.5 adds that on ∂Δ every closed cover is a threshold anyway.
  - So the only room the relaxation adds is non-threshold index preorders at interior selected models: incomparable
    pairs in ⊑_i.
- **DD1's open sub-question and Theorem 3.3.** DD1's sharpest open question (end of §3.4) is whether small-move
  acceptance is forced to be cone-like. Theorem 3.3 does not answer it. It says what happens if the answer is yes
  **off the seed region**: then T1 fails whenever that region is bounded, whatever DD1's positions do inside it. So a
  successful threshold system must make small-move acceptance non-cone-like off R as well, or use conic seed
  regions. This is DD1's CONJECTURE (50/50) made precise as a disjunction.
- **Tension (bounded versus conic).**
  - DD1 Lemma 2.7 ("a cone contained in the bounded cells is null") uses boundedness of the cells **in favour** of
    the plan: no pair of coherent models can trigger the seed or coupling compositions.
  - Theorem 3.3 uses the same boundedness **against** it: bounded cells are invisible to competitiveness at T1.
  - With the conic repair (Remark 3.5), DD1 Lemma 2.7 must be re-proved. A difference D_K △ D_L of two coherent
    models can lie in a narrow cone only near a corner ray of one of them. So the lemma plausibly survives for cells
    that contain no corner ray of any coherent model that agrees with a base off the cell. I have not checked this.
    It is the first thing to verify in a conic version.
- **Independent of DD1.** Lemma 2.9 (coupling) and Lemma 2.10 (conversion cycle) concern non-selected comparisons.
  DD1's Lemma 2.7 shows that coherent models cannot trigger them. Both constrain the (IB)-closure, i.e. condition
  (T1)–(T3) of DD1 §3.1, not the positions r(X) directly.

## 6. Status

| Item | Statement | Label |
|---|---|---|
| 2.1 | exact correspondence: defence map ↔ successful system iff (D1)–(D3) | PROVED (via X1.1.1, X1.3.3) |
| 2.2 | regions are closed ⊑_i-lower sets; e_i ∈ A_i(X) | PROVED |
| 2.3 | selected thresholds ⇒ all regions thresholds; KKM ⟺ Σ r_i ≤ 1 | PROVED |
| 2.4 | total index preorders ⇒ cuts (frontier reparametrization) | PROVED |
| 2.5 | edge rigidity: thresholds on ∂Δ for any closed cover | PROVED; NUMERICS (`edge_chain.out`) |
| 2.6 | star-shaped toward e_i along posterior rays | PROVED (Y1.1 imported) |
| 2.7 | protection/(C) in index form; KKM point | PROVED |
| 2.6 (§) | splice cubes pass the splice rules under thresholds | CHECKED by hand (partial) |
| 2.8–2.9 | seeds; rearrangement records rejected at world 1 | PROVED |
| 2.10 | conversion cycle: one equal-weight-acceptable conversion must be rejected | CHECKED exact; PROVED |
| 3.1 | decisive lemma ⟺ static global condition; dead ends model by model | PROVED; dead-end examples imported (X1, P3) |
| **3.3** | **only the conic part of a non-additive region is visible; R_0 = ∅ ⇒ T1 not selected** | **PROVED modulo CC1 4.1's chain** |
| 3.4 | audit's bounded bundles + envelope off R: no T1 system, any covers | as 3.3 |
| 3.5 | conic bundles: audit's Lemmas 1–4 unchanged | PROVED (by reading) |
| 3.6 | residual for conic R_0: (γ₀) off R_0; T1 weak-Bayes off R_0 | PROVED |
| 3.7 | localization: R_0 must surround ∂D_{T1} | CONJECTURE (CC2 5.7 for Brier cores) |
| 3.8 | valued bundle worlds: explicit transitive class, seeds kept, static reduction | PROVED (CC2 4.1 imported) |
| 3.5 (§) | world-1 veto alone not refuted by edge chains (cell fragment) | CHECKED (exhaustive) |
| — | full system (task 3) | **not achieved** |

## 7. Files (`dd2py/`)

- `patterns.py` → `patterns.out`: exact posterior patterns on CC1's seven cell centres, by support.
- `common.py`: cells, ranks, ladders, the seed vectors g_k, and the relation (B).
- `veto_bfs.py` → `veto_bfs.out`: the exhaustive fragment check of §3.5.
- `cycle_check.py` → `cycle_check.out`: the conversion cycle of Lemma 2.10.
- `edge_chain.py` → `edge_chain.out`: sampled confirmation of the edge chain (Prop 2.5).
