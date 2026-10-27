# PP79. Adversary for round 60: what two generations force, the coincidence of forced verdicts on two and three rays, and attacks on PP78 (PP77 not posted)

24 October 2026. Adversary, Brief 60. One author; not refereed.

**Status.**
- §§1–2 (Task 1) are independent work.
- §3 attacks PP78 in its final form.
- **PP77 had not been posted** when this note was finished (last check 16:38). So §4 gives the attack as a list of explicit, checkable obligations, with the scripts that test them; it does not refute any specific PP77 claim.
- Relays used: REFEREE_round59 items (1)–(5), and the coordinator's PP78 relay.

**Labels.**
- PROVED: complete argument here, or a cited result used inside its hypotheses.
- CHECKED: exact rational cell computation in `r9/PP79_py/` (cells of the joint line arrangement, each split into two radial halves). LPs are solved in floating point.
- No NUMERICS. CONJECTURE / OPEN as stated.

**Axioms** (Brief 60):
- reflexivity; strict (G); (IB); (TC);
- (S): coherent selected models, undominated, competitive, closed fixed-rival acceptance sections, i.e. OPEN fixed-rival refusal sets;
- (LA); global (C), including direct (C) (no all-world tie with an incoherent model).

Every further hypothesis is named where it is used. "Endorsed" means u¹-endorsed (V_w ≥ 0 at the accepting world). V(r) := Φ(new) − Φ(old).

---

## 0. Verdict

| # | Finding | Level | Label |
|---|---|---|---|
| 1 | For EVERY dominator B₂ (any model) of EVERY radially non-conic T–B splice, B refuses Z₃ := B[D₂ ↦ B₂] at world 3 | axiom-level | PROVED |
| 2 | On 𝒮_a (L ∖ S ⊆ odd-2 sublayer) B also refuses Z₃ at 1, so **B ⪯₂ Z₃ is forced** for every dominator; on 𝒮_b, B ⪯₁ Z₃ is forced | axiom-level | PROVED; CHECKED |
| 3 | **Theorem M.** On the explicit family 𝒮_M ⊆ 𝒮_a, for EVERY coherent second defender, Z₃ is MIXED at world 1 or 3. So an essential mixed refusal exists, and its alternative defence is forced to be world 2 | axiom-level + coherence of B₂ | PROVED; CHECKED (456/456) |
| 4 | Sharpness: generic splices have mixed-free same-ray defenders; 𝒮_a has an explicit mixed-free corner-cut defender, but no mixed-free posterior | choice-level | PROVED; CHECKED |
| 5 | Section spread: an open set of selected sources around B must refuse Z₃ at 1 and 3 and accept it at 2 (generated, generally non-guidance acceptances) | axiom-level, given B not isolated | PROVED |
| 6 | Joint defeat: the same-ray pigeonhole (defeat iff an 𝒮_a and an 𝒮_b splice share a scale). Single-domination defeat with guidance counted (REFEREE59 (1)): 0 for same-ray defenders, 2 corner cuts. Not forced at axiom level | choice-level | PROVED; CHECKED |
| 7 | **Three rays (= REFEREE59's coincidence test).** Every balanced record out of T at positive distance from ∂A(T) is accepted at all worlds in any endorsed sectioned base on 𝔾. **Cor A4:** no committed model with a balanced T-piece is ever admissible beside such a base. That covers exactly the generic-order-type posteriors (30/49 CHECKED) | axiom-level given endorsement | PROVED; CHECKED |
| 8 | **PP78:** no error found inside 𝔾. Thm 4.2 survives every check of (1)–(5) in the relay. One invariant clause is used but not stated (J5) | — | checked line by line |
| 9 | **PP78 is terminal for the second generation.** Its own section device (each Γ-shape in exactly ONE closed class, so the outward world is fixed per ray) makes 𝓑 accept every null record with interior carriers on ANY TWO rays at all three worlds (Thm P2). So any committed N ∉ 𝔾 carrying such a reverse is weakly dominated by an incoherent model: band corner cuts, generic posteriors and vertex-wise models are all fatal; same-ray defenders are safe | consequence of PP78's choices | PROVED; CHECKED (`bal2_79`) |
| 10 | **𝓑 ∪ 𝔇₂ is inconsistent** for same-ray defenders of 𝒮_M splices with small F. 𝓑 defends B against Z₃ at 𝒟(V) = 1, but item 2 forces B ⋠₁ Z₃. A base usable for the milestone must withdraw these records from the V-defined class cl(A₁) and install a new world-2 class (Prop P1) | choice-level (refutes the combination, not either part) | PROVED (under (H_c)) |
| 11 | Axiom-level obstruction to the milestone | **none found** | — |

**Plain English.**
- The milestone's essential mixed refusal is forced, not optional. On 𝒮_M every coherent second defender creates one, the axioms fix its alternative (world 2), and sections spread that pattern to an open set of sources.
- PP78's base is correct but cannot host the second generation as it stands. Its classes either kill the natural second defenders (corner cuts, off-ray models) or contradict the forced refusals of the same-ray ones.
- The nearby reachable target (§5) is a base on two rays, or on 𝔾, with ONE extra record-intrinsic class: "B-side world-2 defences of T–B splice records". Its closedness is a single concrete lemma.

---

## 1. Setting

- T = C_u. B = B_{3,t} = C_(1,1,r) is the first defender. The first repair is d₁ = rec(B → X_E), a majority pure class-3 fill as in PP74 Thm 4.3 (with REFEREE59's repaired Lemma 4.2).
- L := {B ≠ T}, with odd-world sublayers and T → B patterns (PP75 Thm 3.1):
  - L⁽³⁾ = gain-A₃ ∪ lose-B₃, pattern {1,2};
  - L⁽¹⁾ = lose-A₁ ∪ gain-B₁, pattern {1};
  - L⁽²⁾ = lose-A₂ ∪ gain-B₂, pattern {2}.

  B is pointwise 3-worse than T on L.
- **Splices.** X₂(S) := T[S ↦ B], S ⊆ L, **radially non-conic** (a non-null set of rays meets both S and L ∖ S). Then X₂ is incoherent, and D₂ := {B₂ ≠ X₂} is non-conic for every conic B₂.
- **Correction sets** (PP76 Lemma 1.3, axiom-level). Every protected coherent committed N differs from X₂ on a non-null part of D₂. In particular D₂ ∩ S and D₂ ∩ (L ∖ S) are both non-null.
- **Families.**
  - 𝒮_a := {S : L ∖ S ⊆ L⁽²⁾ a.e.};
  - 𝒮_b := {S : L ∖ S ⊆ L⁽¹⁾ a.e.};
  - 𝒮_M := {L⁽¹⁾ ∪ L⁽³⁾ ∪ F : F ⊆ lose-A₂ radially non-conic} ⊆ 𝒮_a. S misses gain-B₂.
- **Forced rival.** Z₃ := B[D₂ ↦ B₂].
- **Coupled refusals over all copies:** PP76 Thm 1.1, in pointwise form (`lib79.options`). I do not use PP75 Theorem C, which REFEREE59 (2) restricts to (N1)–(N2).

---

## 2. Task 1: what the axioms force on ANY second-generation defender

**Prop 1.1 (PROVED; axiom-level).** B ⋠₃ Z₃, for every S and every dominator.

*Proof.*
1. Take the copy of d₂ with context B: B′ = Z₃ and X′ = B[D₂ ∩ (L∖S) ↦ T]. So Z₃ ⪯₃ X′ by (IB).
2. X′ differs from B on D₂ ∩ (L∖S), which is non-null by B's correction set, and there it takes T's strictly 3-better values. So X′ ⪯₃ B is strict guidance.
3. If B ⪯₃ Z₃ were accepted, (TC) on Z₃ → X′ → B → Z₃ would install B ⪯₃ X′, against strict (G). ∎

**Prop 1.2 (PROVED).** T is affected at world 3 only if B₂ = −h on all of D₂ ∩ S and D₂ ∩ S ⊆ {T = h, B = S}. So an h/S defender never affects T at 3. For H-defenders, W_T = ess-⋂_{U_T} π ⊆ {1,2} with U_T = S ∩ {B₂ = T} (PP76 Cor 1.4).

*Proof.* Thm 1.1 at T, world 3. On D₂ ∩ S, X₂ = B is strictly 3-worse than T. A point there may therefore only stay at T, and that needs B₂ ⊴₃ B; the rank table on each sublayer then gives the stated values. ∎

**Prop 1.3 (PROVED; CHECKED `mixedZ79.out` 456/456).** If S ∈ 𝒮_a, then B ⋠₁ Z₃ and B ⋠₃ Z₃, so **B ⪯₂ Z₃** is forced, for every dominator. Symmetrically, on 𝒮_b, B ⪯₁ Z₃ is forced.

*Proof.* Thm 1.1 at B, world 1, with G₁ = D₂ ∩ {B ≠ B₂} and G₂ = ∅. B is weakly 1-worse than X₂ on G₁:
- equal on S ∪ Lᶜ;
- pattern {2} on L ∖ S ⊆ L⁽²⁾.

On D₂ ∩ {B₂ = B}, B₂ = B ⊴₁ X₂ = T. Strictness holds on D₂ ∩ (L∖S). World 3 is Prop 1.1. Then use defence. ∎

**Theorem M (PROVED; CHECKED `mixed79.out`, `mixedZ79.out`).** Let S ∈ 𝒮_M and let B₂ be ANY coherent model (any credal set, in H or not) dominating X₂(S). Then Z₃ is mixed at world 1 or at world 3. So the forced refusal is not a guidance refusal, and its alternative is forced to be world 2.

*Proof.*
1. **Better at 1 and 3.** If Z₃ is not mixed at worlds 1 and 3, then, since it is refused there and weakly-worse rivals are guidance-accepted, Z₃ ⊵₁ B and Z₃ ⊵₃ B.
2. **Hence everywhere.** Off D₂, B₂ = X₂, which is B except on (L∖S) ∖ D₂ ⊆ L⁽²⁾, where B₂ = T is 1- and 3-better. So B₂ ⊵₁ B and B₂ ⊵₃ B everywhere.
3. **Only odd-2 points move.** At mixed g with sign h₁ ≠ sign h₃, no value beats another at both 1 and 3. Coherent models agree on unanimous problems. So B₂ = B off the A₂ and B₂ cells. In the A₂ cells B₂ can only gain h; in the B₂ cells it can only move toward −h.
4. **No gains in A₂.** {B₂ = h} is a convex cone that equals {B = h} on the B₁ and B₃ cells. Those cells contain B's corners c₁ = (23, −7, −7/r) and c₃ = (−7, −7, 23/r), the ends of B's vertex-2 face P₂. So ∂{B₂ = h} contains relatively open pieces of P₂, and P₂ supports {B₂ = h} globally. In the A₂ cells {B = h} is exactly P₂'s positive side, because vertex 2 binds there. So nothing is gained.
5. **Contradiction.** Hence B₂ = B off gain-B₂ ∪ (B₂-cells ∖ L). Since S ∩ gain-B₂ = ∅, D₂ ∩ S = ∅, which contradicts T's correction set. ∎

CHECKED:
- The pool has 1,034 coherent candidates: a posterior grid, same-ray points, vertex-wise rescalings, B or T with one extra vertex, and random 3–4-vertex sets.
- 456 pass (N1) and both agreement obstructions on an 𝒮_M splice.
- In all 456, Z₃ lies in B's world-1 and world-3 refusal families and is mixed at 1 or 3.

**Sharpness (PROVED; CHECKED `mixed79*.out`).**
- *Generic splices.* Same-ray B_{3,t′} (t′ < t) is mixed-free: W_B = {3} is a guidance refusal, and W_T = ∅ (30/598 passing candidates, all on the δ₃ line).
- *𝒮_a, posteriors.* No posterior is mixed-free at B. By steps 1–3, such a B₂ moves B only with pattern {1,3}, which no posterior ratio has (Pattern Lemma).
- *𝒮_a, corner cut.* The band corner cut K_B ∪ {v¹ + λv³} (λ = ½, 1, 2) removes a cap of gain-B₂ inside A(T)'s dual cone. It is mixed-free at T and B on 𝒮_a, and inadmissible on 𝒮_M, as Theorem M predicts.
- So the essential refusal is created by the family 𝒮_M, not by a restriction on defenders.

**Prop 1.5 (section spread; PROVED).** If B's index is not isolated, then refusal sets are open, so there is a neighbourhood N of B such that every selected C_p, p ∈ N, refuses Z₃ at 1 and at 3 and therefore accepts C_p ⪯₂ Z₃.

For ray neighbours C_s, s ↑ t, C_s = T on L(t) ∖ L(s). So C_s ⪯₂ Z₃ is in general **not** guidance: it is a generated acceptance on an open set of sources, and rec(C_s → Z₃) → rec(B → Z₃).

**Prop 1.6 (u¹-values for same-ray defenders; PROVED).** Take B₂ = B_{3,t′} and Q := S ∖ L(t′). Then Z₃ = B[Q ↦ T], and with q_o := mass(Q ∩ L⁽ᵒ⁾):

  V(B → Z₃) = (2q₁ − q₂ + q₃, −q₁ + 2q₂ + q₃, −q₁ − q₂ − 2q₃).

- If q₃ ≥ q₁, then V₂ ≥ 0, so the forced alternative is endorsed. (q₃ ≥ q₁ for annuli is a hypothesis here; REFEREE59 gives α/β ∈ [1.94, 2.01] for whole layers, but α = 2p/3 is false and is not used.)
- V₁ − V₂ = 3(q₁ − q₂). So for small F, world 1 is the strictly near-maximal world: this is the conflict of §3.3.

**Alternative worlds and joint defeat (PROVED; CHECKED `defeat79.out`, `single79.out`).**
- *Single domination.* With strict-guidance refusals counted (REFEREE59 (1)), one splice domination never defeats T in any family. It defeats B for 2 of 456 corner-cut candidates on 𝒮_M (also on 𝒮_a), and never for same-ray or posterior defenders. This is a constraint on the choice of B₂.
- *Same-ray pigeonhole.* If an 𝒮_a splice and an 𝒮_b splice get the same defender B_{3,τ}, then B ⋠₁ (base rule), B ⋠₂ (base rule) and B ⋠₃ (guidance): B is defeated. The exact search finds defeat iff s_a = s_b, over 16 scale pairs.
  - So a same-ray rule needs t′(𝒮_a) ∩ t′(𝒮_b) = ∅. If PP74's closed-class device is used, the closures may meet only at t, where the limit record is trivial.
  - Both scale sets must be cofinal at t, because t′(S) > sup{τ : L(τ) ⊆ S}. Alternating closed intervals accumulating at t satisfy this.
  - **A "window" rule** (every scale in a window W(S) dominates X₂(S), as in PP74 Thm 4.3) **fails**: windows of 𝒮_a and 𝒮_b splices with the same τ_S overlap, so B is defeated.
- *General pairs.* Among 625 pairs, B is jointly defeated in 29 and T in 0, and every 𝒮_a defender keeps a partner.
- **Answer.** Joint defeat is not forced by the axioms for any family chosen after commitments. It is forced for specific RULES (windows, shared scales).

**Axiom-level obstruction?** None found. Everything forced (one world at B per domination, the unique alternative world 2, its spread to a neighbourhood) can be accommodated by some choice. An obstruction would need world 2 for Z₃ to be refused at B or near B by another forced source. One further acceptance cannot do this at a limit (PP76 Prop 1.5, with REFEREE59's (CM) caveat); two can, but only through chosen coincidences.

---

## 3. Attack on PP78

### 3.1 Checks of the five relay points

1. **Layer-type lemma and Lemma 2.2: correct.** Pattern Lemma bookkeeping:
   - (k,−) points lie only in ray-k layers; (o,+) points only in the two rays other than o.
   - A null sub-record of rec(Z → W) for members on rays k ≠ m lives in odd-n, n the third world (PP62 Cor 1.2; I re-derived c₁ ≤ 0 ≤ c₃ for a strict-middle ratio).
   - The second-carrier argument is sound. "Never T" holds because (T, W) is a same-ray pair.

   **But the lemma is about members of 𝔾 only. "Dangerous" changes as soon as anything else is committed** (§3.2).
2. **Closedness under iterated limits, copies and (TC): no gap found.**
   - Step 3 of (J_G) is source-agnostic. Approximants are never null: Φ is injective on 𝔾. Null limits have exact Γ-shaped approximants, and Lemma 3.2(b) puts each shape in one class, so the limit is path-carried. Copies are absorbed because every class is a record property.
   - **One unstated clause.** Lemma 5.2 needs "(J5): every non-null non-guidance acceptance is member-carried". It is true, since 𝒟-generators are carried and section limits of rec(C_{a_n} → X) are carried by C_a, but it is not part of (J_G) as written.
3. **(TC)-installed 𝒪_{w+1} records.** Each is accepted at one world only, and no member carries it. Lemma 4.1(b) is correct: the path potential, the cyclic move pattern on S_ab, S_bc, S_ca, and ties excluded because equal coordinates mean equal members. Danger would need a later committed model carrying the reverse together with an all-world acceptance. 𝒪-records alone never give the latter, so the real danger is §3.2, not 𝒪.
4. **Defence at ray ends and at u: correct.**
   - Ends use the null defence at k (inward only).
   - At T: world 1, and T ∈ P₁.
   - Non-null rivals: 𝒟 is defined on {Σv ≥ 0} ∖ {0} (Lemma 1.0).
5. **S₃ symmetry and (2V): used correctly** (exact Γ-shapes via β_i = β_j; Pattern Lemma; λ-Bayes equality on R). (CM) is a lemma for posteriors (REFEREE59 item 3).

### 3.2 PP78's device forces two-ray coincidences

**Thm P2 (PROVED).** In 𝓑, let r be null, carried by interior members B_{k,a} and B_{m,b} of two different rays, with supp r off the moving level sets (every approximating member carries r). Then r is accepted at all three worlds.

*Proof.*
- Prop 2.1(i) (inward) gives k. The outward approximants have V = γ(e − 3e_k), an exact (k+1, k+2) tie, which 𝒟 sends to k+1. The closed section then gives k+1.
- Likewise m and m+1. For k ≠ m, {k, k+1, m, m+1} = {1, 2, 3}. ∎

More generally, any allocation that puts each outward shape in exactly one class (the device on which PP78's section proof rests) fixes an outward world out(k) ∈ {k+1, k+2} per ray. Some ray pair then covers all three worlds:
- pair (1,2) misses 3 only if out₁ = 2 and out₂ = 1;
- pair (1,3) misses 2 only if out₁ = 3 and out₃ = 1;
- these two requirements are incompatible.

PP78's elimination table (row "interior points of two rays: ⊇ {k, k′}") should read "all three".

**Cor P3 (PROVED; CHECKED `bal2_79.out`).** 𝓑 can be extended by a committed coherent N ∉ 𝔾 only if N carries the reverse of NO null record of Thm P2's kind on a non-conic support. Otherwise Y := N[supp ↦ old] has rec(Y → N) accepted at every world, so N is either dominated or tied with an incoherent model.

Exact cells, LP over cells where both rays' triples (a−, a, a+) agree and N differs:

| Candidate second defender | Fatal ray-pair configurations (of 27) |
|---|---|
| B; same-ray B_{3,t′} | 0 (PP78 Lemma 2.2 confirmed) |
| band corner cuts K_B ∪ {v¹ + v³}, K_B ∪ {v¹ + 2v³} (the mixed-free 𝒮_a defenders of §2) | 6 each (rays 1, 3) |
| generic posterior (21/20, 441/400, 1) | 16 |
| vertex-wise (B's vertex 3, T's others) | 12 |

The corner-cut witness balances, inside odd-2:
- T → B flips (S → h) on gain-B₂ outside the small layers;
- reverts h → S on gain-B₂ cells inside L₁(a) ∩ L₃(c), where the cut has made N silent.

Under an arbitrary endorsed sectioned base only the three-ray version is forced. That is Cor A4: every balanced T-record at positive distance from ∂A(T) is accepted everywhere (REFEREE59 §4.3 = my Theorem A3). It excludes exactly the generic-order-type posteriors (`balanced79.out`: 30/49) and 220/230 vertex-wise models.

### 3.3 𝓑 is inconsistent with the natural second generation

**Prop P1 (PROVED).** Let S ∈ 𝒮_a with dominator B₂, and add d₂ = rec(B₂ → X₂(S)) at all worlds to 𝓑 (PP78 Cor 5.1's construction applied to 𝔇₂). Prop 1.3 forces B ⋠₁ Z₃ and B ⋠₃ Z₃. But 𝓑 accepts B ⪯_w Z₃ at w = 𝒟(V(B → Z₃)) if that vector is non-null, and at w = 3 if it is null (null defence of a ray-3 member). So the union satisfies (TC) only if **V(B → Z₃) ≠ 0 and 𝒟(V(B → Z₃)) = 2**.

For same-ray B₂ = B_{3,t′} (Prop 1.6) assume (H_c): q₁ ≤ q₃ ≤ c·q₁. Then |V|_∞ = q₁ + q₂ + 2q₃. World 1 is the unique near-maximal world whenever 3(q₁ − q₂) > κ(q₁ + q₂ + 2q₃). This holds for every κ < ½ once q₂/q₁ is small and c < 2.5 (REFEREE59 gives a whole-layer ratio of about 2). So **𝓑 ∪ 𝔇₂ violates (TC)** for 𝒮_M splices with small F.

The other admissible defenders are fatal by Cor P3, or carry the same check. By Theorem M, every coherent defender of an 𝒮_M splice yields some Z₃, and 𝓑 must send each such Z₃ to world 2.

**What must change.** cl(A₁) is defined by V alone. Removing the records (Q : B → T) from it, while keeping their carriers B and B_{3,s} (s > t) defended at world 2, needs a new record-intrinsic class 𝒲₂ of "B-side splice records accepted at 2" that is not near-maximal at 2. Its closure under section limits followed by copying is a new lemma: by Prop 1.5 it must contain rec(C_s → Z₃) for s near t. That is exactly the audit's "withdraw and reassign", made concrete. PP78's Cor 5.1 (first generation) is unaffected.

---

## 4. Attack on PP77 (draft not available): obligations any two-generation construction must discharge

Each obligation is derived above. Each comes with a test script that runs on any proposed defender or rule.

- **O1 (Prop 1.3, Thm M).** For every 𝒮_a splice, B ⪯₂ Z₃ must be installed and world 2 must not be refused for Z₃ by another installed domination; symmetrically 𝒮_b with world 1. On 𝒮_M the refusal is mixed, whatever the defender. Test: `mixedZ79`, `defeat79`.
- **O2 (Prop 1.5).** The same acceptance at an open set of sources around B. Its class must be closed under section limits followed by copying, iterated: the REFEREE58 pattern with the transported acceptance being a generated world-2 defence.
- **O3 (Prop P1).** If the base is PP78's 𝓑 or any margin base, the base acceptance at 𝒟(V(B → Z₃)) ≠ 2 must be withdrawn record-wide, and the defence of every carrier reassigned.
- **O4 (Cor P3 / A4).** Every committed second defender must be tested against two-ray-carried null records (on 𝓑) or three-ray ones (any endorsed sectioned base on 𝔾). Corner cuts and off-ray models fail on 𝓑. Same-ray defenders pass. Test: `bal2_79`, `balanced79`.
- **O5 (D1).** A same-ray rule must keep the scales of 𝒮_a and 𝒮_b splices disjoint, including after closure; window rules fail. Single-domination defeat must be checked with guidance counted (`single79`).
- **O6 (REFEREE59 (4)).** PP74 Thm 3.2 is applied once, to 𝔇₁ ∪ 𝔇₂ over a fresh base, never recursively. Its condition (d) must be replaced by the jointly maintained refusal class of O1–O3, because Theorem M makes (d) false on 𝒮_M.
- **O7 (scope).** Conic-but-incoherent splices are outside the correction-set arguments and must be treated separately (OPEN here).

---

## 5. The nearby reachable result

The impossibility found is choice-level: 𝓑 cannot host the second generation as it stands. The nearby target I propose is:

> **𝓑′ := 𝓑 with the records Z₃(S) of 𝒮_a (resp. 𝒮_b) splices moved from cl(A₁) to a new class 𝒲₂ (resp. from cl(A₂) to 𝒲₁), with same-ray second defenders on pigeonhole-disjoint scale sets.**

Why this target:
- Same-ray defenders are the only tested family that survives both Cor P3 and Theorem M's forced pattern.
- They make every forced world-2 acceptance endorsed (Prop 1.6, under q₃ ≥ q₁).
- The single missing lemma is the closedness of 𝒲₂ ∪ 𝒲₁ ∪ 𝒦_w under section limits followed by copying.

  By Prop 1.5 these records come with Γ-shaped perturbations along the δ₃ ray. So PP78's own method (each perturbation shape in exactly one class) is the natural tool.

---

## 6. Scripts (`r9/PP79_py/`; run `python3 -I -B <script>.py > <script>.out` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `lib79.py` | exact cells with radial halves; D_K models; PP76 Thm 1.1 pointwise; mixedness | library |
| `mixed79.py` | Theorem M (456/456 on 𝒮_M); 𝒮_a and generic statistics | CHECKED |
| `mixedZ79.py` | Z₃ in both refusal families and mixed (456/456) | CHECKED |
| `mixed79b.py`, `mixed79c.py` | escaping corner cuts; explicit band corner cut | CHECKED |
| `defeat79.py` | D1 pigeonhole (defeat iff s_a = s_b); D2, 625 pairs | CHECKED |
| `single79.py` | single-domination defeat with guidance counted | CHECKED |
| `balanced79.py` | balanced T-pieces (Cor A4): posteriors capable iff generic | CHECKED |
| `bal2_79.py`, `dbg79.py` | Cor P3: fatal two-ray configurations for second defenders under 𝓑; witness | CHECKED |
