# PP74. The H-repair operation: defender, acceptances, refusals, surviving defences

24 October 2026. Constructor, Brief 59. One author; not refereed. **The DRAFT section is posted first for PP76 and will not be changed in substance; results follow below it.**

---

## DRAFT (posted first for PP76)

**Conventions.** X ⪯_w Y: X is no worse than Y at world w. A record is r = rec(X → Y) = (supp r, old = X|supp, new = Y|supp); r⁻¹ = rec(Y → X). A model Z *carries* r if Z = old(r) a.e. on supp r; then Z ⊕ r := Z[supp r ↦ new(r)]. Verdicts are functions of (record, world), so (IB) and all common-context copies are built in. 𝒦 is the set of *committed* coherent models (each with an index plan, below); everything else is a candidate or a rival. For a world w and models Y, Z put

  Bet_w(Y, Z) := {g : Y(g) strictly w-better than Z(g)},  Weq_w(Y, Z) := complement of Bet_w(Y, Z).

**Record topology (relay item 2).** r_n → r means: the maps g ↦ (old_n(g), new_n(g)) (value ∗ off the support) converge in μ-measure. A section limit C_{a_n} → C_a (in measure) with a fixed rival gives rec(C_{a_n}, X) → rec(C_a, X). Every acceptance class below is defined by the record alone and is closed in this topology; every refusal class is defined by the record alone and is open. So neither a section limit nor an (IB) copy can move a record out of its class.

**The operation 𝒪(Σ; X).** Input: a partial system Σ (PP64 §1.2: committed acceptances, refusals with reservations, committed models with indices) satisfying the invariant of §3, and an incoherent model X of the test class (incoherent measurable splices X = C[A ↦ D] of committed C, D, including H-fills; ultimately every incoherent H-model). Output:

1. **Defender** B ∈ Cand(X), a coherent model (sought first among the rescaled models C_m; any coherent D_K is allowed — escape clause).
2. **Required acceptances:** the domination record d := rec(B → X) at all three worlds. *Nothing else is newly accepted* (see 4).
3. **Required refusals:**
   - (R0) d⁻¹ at all three worlds;
   - (R1) the coupled refusals, for every world w and every copy: every record rec(Y′ → B′), where (B′, X′) carries d and Y′ is strictly w-worse than X′ (weakly everywhere, strictly on a non-null set). In closed form (Lemma 2.2): q⁻¹ for every q with (q − d) w-worsening for the new side.
4. **Surviving defence options:** for every committed C that carries a record refused in (R1) at w (C is *affected at w*), the anchor world v_C(w) ≠ w at which B is pointwise weakly worse than C. C's defence against every refused rival C[S ↦ B] is then **weak guidance at v_C(w)**, which is already committed: no new acceptance is made. Its reservation is the guidance-robust set of §3.4.

**The rule ASR (anchored splice repair).** B is admissible for X iff:
- **(U1) agreement:** no committed model carries d⁻¹ (no C ∈ 𝒦 equals X a.e. on {B ≠ X});
- **(U2) anchoring:** every committed C that is affected at some w has an anchor world v ≠ w with B ⊴_v C (B pointwise weakly v-worse than C);
- **(U3) isolation:** at every world w at which d is not a weak-guidance record, no copy of d closes an accepted triangle, i.e. there is no accepted pair rec(X′ → Y), rec(Y → B′) (§3.2 gives the exact "two-carrier cover" form);
- **(U4) sections:** for every affected (C, w) the reservations required by C's index plan exist (§3.4).

Among admissible defenders ASR chooses one that **minimises the set of affected pairs (C, w)**: for each candidate the affected set is computed from the record alone (Lemma 2.3), and an unaffected pair costs nothing. Different rivals may receive different defenders; competing candidates are not installed.

**How the rule escapes the zero-sum obstruction.** ASR is not of the form "accept at w iff v_w(r) ≥ 0" for any score: it accepts d at every world, including the world(s) where d is u¹-unfavourable, and refuses d⁻¹ at every world, including those where d⁻¹ is u¹-favourable. The asymmetry is licensed by a property of the record, not of a score: d⁻¹ is carried by no committed model (U1), so its refusal costs no defence and no reservation. The price is (U3): d's acceptance at its unfavourable world must not close a triangle.

**Index plan.** Every committed model receives an index at which it is selected and a closed set of indices on which it defends; at the indices of affected carriers, refusals are reserved on open sets in the sense of PP64 (I6)–(I7). "No section obligation" is not used for any committed model.

---

**Addendum to the DRAFT after the relays (REFEREE_round58, PP75, PP76); recorded, not silently changed.**
- DRAFT item 4 ("nothing else is newly accepted") is **withdrawn** (PP76 §3.2 is right: extended rivals C[G₁ ↦ B][G₂ ↦ n] need non-guidance defences). In the results below these defences come from a **base relation** whose acceptance classes are record-intrinsic; the operation itself adds only the domination class 𝔇, and proves that every refusal it forces is one the base already makes.
- (U2) anchoring is **dropped as a requirement**. It is replaced by *carrier-cleanness* (Def. 3.1(d)), which is what the proofs use. Anchoring survives as a sufficient condition and as the reason ASR fails at the second application (§5).
- Admissibility now also includes PP76's second-application clauses (Def. 3.1(c), "no consecutive dominations") and joint defeat is excluded structurally (Cor 3.3).

---

## 0. Verdict

**The full deliverable is not reached. A precise part of it is, in one record-based relation, and the remaining blocks are located exactly.**

1. **A repair operation with an exact preservation theorem (Theorem 3.2; PROVED).** Take any *u¹-endorsed base* on a committed family 𝒦 (every non-guidance acceptance is carried by a committed model and has V_w ≥ 0 at its world). Add a class 𝔇 of domination records accepted at all three worlds. If 𝔇 satisfies four record-level conditions — agreement (U1), strict improvement (N1), no consecutive dominations, and carrier-cleanness at each domination's u¹-unfavourable world — then every base property survives: reflexivity, strict (G), (IB), (TC) on all triangles of measurable models, defence, protection, no all-world tie, and closed sections if the base has them and 𝔇 is closed. Every rival in 𝔇 is strictly dominated. Two dominations never jointly defeat a source.
2. **First application: every majority pure fill of T is repaired (Theorem 4.3; PROVED, one mass ratio NUMERICS).**
   - *Setting.* 𝒦 = 𝔾, the three-ray star at u: T and the pure down-shift rays C_{u+tδ_k}, 0 ≤ t ≤ t₁, k = 1, 2, 3. The base is PP56's Λ, restricted to 𝔾-carried records.
   - *Result.* In one relation 𝓡₁ satisfying reflexivity, strict (G), (IB) and (TC), every member of 𝔾 is defended against every measurable rival and protected, with no all-world tie partner. **Every fill T[E ↦ h] with E ⊆ Sil(T) ∩ A_k ∩ L_k(t₁), for every class k and every non-null measurable E however small or non-conic, is strictly dominated** by a star member chosen from a rival-dependent window.
   - *Escape from the zero-sum obstruction.* It is explicit. Each domination is accepted at its class world, where it is u¹-unfavourable, while its reverse is refused at all three worlds. These are H-models with equal total balanced loss.
3. **Sections (§4.4).** 𝔇 is a closed, record-intrinsic class (Prop 4.5, PROVED). With the Λ base, sections are not closed: Theorem Q applies, because star members on different rays have balanced swaps. **Theorem 3.2 holds for any endorsed base, so the first application inherits closed sections from any sectioned endorsed base on 𝔾** (Cor 4.6). The existence of such a base is CONJECTURE G. No axiom-level obstruction to it is known: u has no O-direction on 𝔾, and the δ_k ray has only O_k.
4. **Second application (§5).**
   - **Splice-endpoint clause (Theorem 5.1; PROVED, axiom-level).** For a splice X = C[A ↦ D] of two committed models and any dominator B″, at every world one endpoint must refuse an explicit move towards B″. Any endorsed base satisfies it automatically at the worlds where the domination is favourable. At its unfavourable world it is a real constraint.
   - **ASR's anchoring fails for T–defender splices.** No posterior, and no H-model weakly worse than the defender at its class world, is anchored (PROVED). The cell computation finds none in 949 coherent candidates, posterior and vertex-wise rescaled, on all 254 cell splices for each of two defenders (CHECKED). Defender–defender splices (B₃–B₁) all have anchored candidates (62/62, CHECKED).
   - **Without anchoring,** a posterior dominator that passes (N1), (U1) and the endpoint clause at level 0 exists for 222 of the 254 T–B₃ cell splices (NUMERICS). The other carrier conditions of Theorem 3.2 are not checked for these.
5. **Level.**
   - *Axiom-level:* nothing new beyond Theorem 5.1, which is a clause and not a contradiction.
   - *The two blocks are features of choices:* (i) the Λ base fails sections (Theorem Q, a property of Λ); (ii) carrier-cleanness at the second application is not proved. X\*_j (PP75/PP76: dominators must leave H) is outside the class treated here.

| Item | Result | Label |
|---|---|---|
| Carrier calculus: no triangle with three links carried by one model; covers | Lemma 2.1, 2.2 | PROVED |
| First-generation refusals in H, both orientations, = PP76 Thm 1.1 | Lemma 2.3 | PROVED |
| Preservation theorem for an endorsed base + 𝔇 | Thm 3.2 | PROVED |
| No joint defeat; no exhaustion | Cor 3.3 | PROVED |
| Overlap lemma for pure-shift layers | Lemma 4.1 | PROVED |
| Window lemma (over-balanced scales) | Lemma 4.2 | PROVED given α = 2p/3 (NUMERICS) |
| First application: all majority pure fills of T, one relation | Thm 4.3 | PROVED |
| 𝔇 closed and record-intrinsic; closure followed by copying | Prop 4.5 | PROVED |
| Sections inherited from a sectioned endorsed base on 𝔾 | Cor 4.6 | PROVED (conditional on CONJ G) |
| Splice-endpoint clause | Thm 5.1 | PROVED |
| No anchored dominator for T–B splices | Prop 5.2 | PROVED; CHECKED (0/254, two defenders) |
| Defender–defender splices anchored | — | CHECKED (62/62) |
| Endpoint-safe posterior dominators for T–B₃ splices | — | NUMERICS (222/254) |
| Sectioned endorsed base on the three-ray star | CONJ G | CONJECTURE |

---

## 1. Responses to the relays

| Relay item | Response |
|---|---|
| REFEREE58 (1): PP72 Thm 6.2 false | Nothing here uses it. Theorem 3.2 takes an arbitrary endorsed base as a hypothesis. Cor 4.6 needs a sectioned base, and that is CONJECTURE G, not Thm 6.2. |
| REFEREE58 (2): record-intrinsic closed classes | Adopted. Accepted classes: guidance; base classes; 𝔇_{θ,K}, which is closed (Prop 4.5). Every refusal the operation forces is in a base-refused class (Thm 3.2, step 4), so section limits and copies cannot move a record across classes. |
| REFEREE58 (3): symmetric family for u¹ | u¹ and Λ are built on PP62's 𝒮₀ = {a : normalise(1/a) ≥ c + η}, which is S₃-symmetric. 𝔾 ⊆ 𝒮₀. |
| REFEREE58 (4): zero-sum; only score escape is null-tie breaking | 𝔇 is not a score rule. Its records are non-null and u¹-unfavourable at the class world (Lemma 4.2), and they are accepted by class membership. |
| REFEREE58 (5): H; common-silence fills are not H | Theorem 4.3 takes E ⊆ L_k(t₁) ⊆ R, so every rival is an H-model. |
| REFEREE58 (6): rescaling linear in m | Used as such (`asr74.py`). Compatibility sets are not used as convex sets. |
| PP75 Theorem C, (N1)–(N3) | (N1) and (N2) are Def. 3.1(a)(b). Theorem C is the H case of Lemma 2.3. Its "all refusals" claim is correct in H, because the dual orientation coincides there (Lemma 2.3(iii)). |
| PP75 (6) / PP76 (7): X\*_j | Not in the class treated. Its dominators lie outside H, so they are not star members. OPEN here. |
| PP76 (1) extended rivals | Accepted (Addendum). They are defended by the base (Theorem L for Λ). Lemma 2.3 shows that the refusals forced on committed carriers are base-automatic in Theorem 4.3. |
| PP76 (2) refusal class not open | The forced refusals are exactly ones the base already makes (Thm 3.2, step 4). Openness is therefore a property of the base's refusal sets, i.e. part of CONJECTURE G. ASR's anchor is no longer used for sections. |
| PP76 (3) second-application clauses | Def. 3.1(a) covers every committed model, earlier defenders included. Def. 3.1(c) is "no consecutive dominations". "Not defeated by an earlier domination" follows from Cor 3.3. |
| PP76 (4) joint defeat | Impossible under Theorem 3.2's hypotheses (Cor 3.3). PP76's Example 1.7 uses complementary (o,0)/(o,1) fills on a shared layer. Theorem 4.3's classes have pairwise distinct layers, and only (o,1)-fills. |
| PP76 (5) Cor E.2 third acceptance | It concerns sectioned bases on 2-D families. It enters CONJECTURE G only where balanced swaps sit at members with an O-direction for the refusing world (§4.4). |

---

## 2. Carrier calculus

Throughout, 𝒦 is a set of coherent H-models (two values h, S on R, common advice off R). A record is *𝒦-carried* if some member of 𝒦 carries it. For a domination record d = rec(B → X) put D := supp d. Consider a triangle B′ → X′ → Y → B′ through a copy (B′, X′) = (W[D ↦ B], W[D ↦ X]), with s := rec(X′ → Y) and t := rec(Y → B′). Split D into

  P := D ∩ {Y = B},  Q := D ∩ {Y = X},  O := D ∩ {Y ∉ {X, B}},

and put D″ := {Y ≠ W} ∖ D.

**Lemma 2.1 (PROVED).**
- (i) No triangle has three links carried by one model Z.
- (ii) If s is carried by C₁ and t by C₂, then C₁ = X on P ∪ O and C₂ = X on Q. If C₂ is an H-model, then O = ∅.
- (iii) If C₁ = C₂ = Z ∈ 𝒦, then Z carries d⁻¹.

*Proof.*
- (i) Consecutive links rec(P₀ → P₁) and rec(P₁ → P₂) carried by Z force Z = P₀ ≠ P₁ and Z = P₁ at any common point. So their supports are disjoint. In a 3-cycle every pair of links is consecutive. The three supports are therefore pairwise disjoint, while the records sum to zero, so all three are empty.
- (ii) C₁ = X′ on {X′ ≠ Y} ⊇ P ∪ O, and X′ = X on D. Also C₂ = Y on {Y ≠ B′} ⊇ Q ∪ O, with Y = X on Q. On O, Y ∉ {h, S}, while C₂ ∈ H.
- (iii) By (ii), Z = X on D. ∎

**Lemma 2.2 (two-carrier covers; PROVED).** Suppose s and t are both accepted, and neither is guidance or a domination record. Then they are carried by C₁, C₂ ∈ 𝒦 with C₁ ≠ C₂ and X = C₁ on P, X = C₂ on Q, P ⊔ Q = D (a *cover* of X on D).

*Proof.* Every accepted non-guidance record is 𝒦-carried or a domination (Def. 3.1), so Lemma 2.1(ii)–(iii) applies. ∎

**Lemma 2.3 (first-generation refusals in H, both orientations; PROVED).** Let d be accepted at w and C ∈ 𝒦. Put U_C := {B = C ≠ X} (PP76's correction set).
- (i) **Into B** (the triangle's guidance link is X′ ⪯_w Y): C carries a forced refusal at w iff U_C ⊆ Up_w(C), where Up_w(C) is the set at which flipping C's value improves world w. This is PP76 Cor 1.4.
- (ii) **Out of X** (the guidance link is Y ⪯_w B′, with Y ▷_w B′): C carries a forced refusal rec(C → C[G₁ ↦ n₁][G₂ ↦ n₂]) iff C = X on Bet_w(B, X) ∩ {C ≠ B}. Here Bet_w(B, X) ⊆ G₁ ⊆ D ∩ {C = X}, n₁ ⊵_w B on G₁, and n₂ is strictly w-better than C on G₂ ⊆ D^c.
- (iii) For two-valued C, B and X, the two families of rivals coincide. So PP75's (N3) and PP76's Theorem 1.1 are exact in H. With four advice values, (ii) adds rivals with n₁ ≠ B.

*Proof.*
- (ii): if t is guidance, (TC) forces s ∉ Acc_w. Carriers of s satisfy C = X′ on {X′ ≠ Y}. Write G₁ := {X′ ≠ Y} ∩ D and G₂ := {X′ ≠ Y} ∖ D. Then Y ⊵_w B on G₁, Y = X ⊵_w B on D ∖ G₁, and Y = n₂ ⊵_w W = C on G₂, strictly there because the advice values differ. In particular Bet_w(B, X) ⊆ G₁, since X cannot be ⊵_w B where B is strictly better.
- (iii): with two values, n₁ = B on G₁, and the two sets of constraints are the same lists. ∎

---

## 3. The operation and its preservation theorem

**Definition 3.1 (admissible domination class).** Let 𝔅 be a base relation on 𝒦. 𝔇 is a set of records d = rec(B_d → X_d) with B_d ∈ 𝒦. It is *admissible* if:
- (a) **(U1)** no member of 𝒦 carries d⁻¹ (equivalently: no Z ∈ 𝒦 equals X_d a.e. on supp d);
- (b) **(N1)** at every world, B_d is strictly better than X_d somewhere;
- (c) **no consecutive dominations:** for d₁, d₂ ∈ 𝔇 (d₁ = d₂ allowed), X_{d₁} ≠ B_{d₂} on a non-null part of supp d₁ ∩ supp d₂;
- (d) **carrier-cleanness:** at every world w with V_w(d) < 0 (u¹-unfavourable),
  - every first-generation refusal of Lemma 2.3 at a carrier in 𝒦 is a record that is strictly reverse-guidance at w; and
  - every cover (Lemma 2.2) has a link that is strictly reverse-guidance at w.

**The operation 𝒪 (final form).** Given 𝔅 and 𝔇:
1. accept every d ∈ 𝔇 at all worlds;
2. refuse d⁻¹ at all worlds, and refuse every record forced by Lemma 2.3 (by (d), these are already refused);
3. keep every base acceptance.

The surviving defence options of each C ∈ 𝒦 are exactly its base defences (Cor 3.3).

**Base hypotheses.**
- (B1) Every non-guidance acceptance of 𝔅 is 𝒦-carried and u¹-endorsed at its world: V_w ≥ 0, and lex-endorsed if 𝔅 is Λ-based.
- (B2) 𝔅 satisfies reflexivity, strict (G), (IB) and (TC). Every member of 𝒦 is defended against every measurable rival, protected, and has no all-world tie partner.

**Theorem 3.2 (preservation; PROVED).** Assume (B1), (B2), and that 𝔇 is admissible and every d ∈ 𝔇 satisfies V_w(d) > 0 (lex > 0) at every world where it is not unfavourable. Let 𝓡 := 𝔅 ∪ 𝔇@{1,2,3}. Then:
- 𝓡 satisfies reflexivity, strict (G), (IB) and (TC) on every triangle of measurable models;
- every member of 𝒦 keeps its base defence against every measurable rival, is protected, and has no all-world tie partner;
- every X_d is strictly dominated by B_d;
- if 𝔅 has closed fixed-rival sections on 𝒦 and 𝔇 ∪ {∅} is closed in the record topology, then so does 𝓡.

*Proof.*
1. **(IB), reflexivity.** Every class is a set of records.
2. **Strict (G).** A strictly reverse-guidance record is never base-accepted (V_w < 0 for a strictly guiding field), and it is never in 𝔇, by (N1).
3. **(TC).** Consider an accepted triangle at w. By (c), it contains at most one domination: two dominations are consecutive in a 3-cycle, and in either order this would need X_{d₁} = B_{d₂} on the common support.
   - *No domination.* All links are base links (guidance included), and (B2) gives (TC) for them.
   - *One domination d, with w favourable for d.* The same sum argument gives a contradiction, since V_w(d) > 0.
   - *One domination d, with w unfavourable.* The other links s and t are guidance or 𝒦-carried endorsed records.
     - Both guidance: composing gives X ⊵_w B on D, contrary to (N1).
     - One guidance: the other link is a first-generation refusal (Lemma 2.3), which by (d) is strictly reverse-guidance, hence not accepted.
     - Both carried: Lemma 2.2 gives a cover, and by (d) one of its links is strictly reverse-guidance, hence not accepted.

     So no triangle through d is accepted.
4. **Defence, and the refusals forced by 𝒪.** The refusals of step 2 are base-refused:
   - at favourable worlds they have V_w < 0 (Lemma S arithmetic: V_w(t) = −V_w(d) − V_w(s) < 0 when s is guidance, and symmetrically);
   - at unfavourable worlds they are strictly reverse-guidance, by (d).

   So no base defence is withdrawn.
5. **Protection and ties.**
   - Suppose rec(Y → Z), Z ∈ 𝒦, is accepted at all worlds. If it is a domination, Z carries its reverse, contradicting (U1). Otherwise it is base-accepted at all worlds, which contradicts base protection. Mixed cases are impossible, because a record is either in 𝔇 or not.
   - d⁻¹ is refused at all worlds: it is not guidance (N1), not 𝒦-carried (U1), and not in 𝔇 (else some B_{d′} ∈ 𝒦 would carry d⁻¹).
   - So B_d strictly dominates X_d, and no new tie arises. Rules III and IV never fire.
6. **Sections.** The fixed-rival section of Z ∈ 𝒦 at w is the union of the base section and {p : rec(C_p → Z) ∈ 𝔇}. The second set is the preimage of the closed set 𝔇 ∪ {∅} under the continuous map p ↦ rec(C_p, Z). (The empty record is accepted by reflexivity.)
   - Section closure followed by copying cannot leave the classes, since membership is a property of the record.
   - So the union is closed. ∎

**Corollary 3.3 (no joint defeat, no exhaustion; PROVED).** Under Theorem 3.2's hypotheses, every refusal forced at a committed carrier by any number of installed dominations is base-refused. So the set of base-defending worlds of each C ∈ 𝒦 against each rival is unchanged. In particular, PP76's Prop 1.6 exhaustion cannot occur.

**How the operation escapes the zero-sum obstruction.** d is accepted at its unfavourable world because it belongs to 𝔇, not because of any score. The reverse d⁻¹ is refused everywhere because no committed model carries it. Theorem 3.2 shows that the cost of this asymmetry is confined to triangles through d at the unfavourable world, and that (c) and (d) close them off.

---

## 4. First application: the majority pure fills of T

**Setting.**
- u¹ and Λ are PP56's, for the symmetric (2V) family 𝒮₀.
- δ_k is the pure down-shift of world k, and B_{k,t} := C_{u+tδ_k}.
- t₁ > 0 is such that the three segments lie in 𝒮₀.
- 𝔾 := {T} ∪ {B_{k,t} : k = 1, 2, 3, 0 < t ≤ t₁}.
- L_k(t) := {B_{k,t} ≠ T}. Its odd-world-o part is L_k^{(o)}(t), and L_k(t) is non-decreasing in t (PP57 Lemma 4.1: along a pure-shift ray each point changes at most once).
- Masses are |g|-masses.
- α(t) is the mass of L_k^{(k)}(t), β(t) the mass of each L_k^{(i)}(t), i ≠ k (equal by symmetry), and p(t) = α + β. Then V(T → B_{k,t}) = p·(3e_k − (1,1,1)), i.e. (−p, −p, 2p) for k = 3 (PP73 Lemma 1.4(a)).
- For a fill X_E := T[E ↦ h] with E ⊆ Sil(T) ∩ A_k ∩ L_k(t₁), write e := mass(E).

**Lemma 4.1 (layer overlap; PROVED).** For j ≠ k, s, t ∈ (0, t₁] and the third world i:
- L_k^{(i)}(t) ∩ L_j^{(i)}(s) is non-null;
- for k fixed, L_k^{(o)}(t) is non-null for each o.

*Proof.* At odd-i points with h = A (so h_j, h_k > 0) answered by T, both shifts lower Σ_l m_l v^α_l h_l for the binding vertex α. They therefore silence the open cone {0 < Σ_l v^α_l h_l < min(t v^α_k h_k, s v^α_j h_j)} near T's α-boundary, which meets odd-i A-type points. The same estimate with one shift gives β > 0. α > 0 is Lemma 1.2(a) of PP73. ∎

**Lemma 4.2 (over-balanced window; PROVED given α = 2p/3, which is NUMERICS).** For θ ∈ (0, 1/5] and K ≥ 2, put

  W_θ(E) := {t ∈ (0, t₁] : (1 + θ)e ≤ p(t) ≤ K e and mass(E ∖ L_k(t)) ≥ θ e}.

W_θ(E) is non-empty whenever (1 + θ)e ≤ p(t₁). For t ∈ W_θ(E) and d := rec(B_{k,t} → X_E),

  V(d) = (p − e)(1 at i ≠ k, −2 at k),

which is strictly favourable at both i ≠ k and strictly unfavourable at k.

*Proof.*
- V(d) = Φ(X_E) − Φ(B) = [Φ(X_E) − Φ(T)] − [Φ(B) − Φ(T)] = e(−1, −1, 2) − (−p, −p, 2p) (for k = 3; the other classes follow by symmetry, PP72 Prop 4.2).
- p is continuous and strictly increasing from 0, so p(t₋) = (1 + θ)e for some t₋.
- Then mass(E ∩ L_k(t₋)) ≤ α(t₋) = (2/3)(1 + θ)e ≤ (1 − θ)e when θ ≤ 1/5, so t₋ ∈ W_θ(E).
- NUMERICS (`layer74.out`): β/p = 0.333 at five scales. ∎

**Theorem 4.3 (first application; PROVED, given Lemma 4.2's ratio).** Let 𝔇₁ := {rec(B_{k,t} → X_E) : k = 1, 2, 3, E as in the setting with (1 + θ)e ≤ p(t₁), t ∈ W_θ(E)}, and let 𝔅_Λ be the 𝔾-carried records with Λ_w > 0 at w, together with guidance. Then 𝓡₁ := 𝔅_Λ ∪ 𝔇₁@{1,2,3} has every property in Theorem 3.2's first three bullets. In particular, every such fill of T, of every class, is strictly dominated by every B_{k,t} with t ∈ W_θ(E), and every member of 𝔾 is defended, protected and tie-free.

*Proof.* (B1) is by construction. (B2) is PP56 Theorem L (𝔾 ⊆ 𝒮₀), restricted to 𝔾-carried records; removing acceptances of uncommitted carriers keeps acyclicity, protection and the defence of committed models. Favourability is Lemma 4.2. It remains to check Def. 3.1 for d = rec(B → X), B = B_{k,t}, X = X_E. Then D = (L ∖ E) ⊔ (E ∖ L), with L = L_k(t). On E ∖ L, B = S and X = A. On L ∖ E, X = T ≠ B.
- **(U1).** If Z = X on D, then Z = A on E ∖ L ≠ ∅. Among star members only same-class B_{k,t′} with t′ > t answer A at odd-k points that T leaves silent: other classes only lose A there (PP73 Lemma 1.2(b)). Those B_{k,t′} differ from T on all of L ⊇ L ∖ E ≠ ∅ (Lemma 4.1).
- **(N1).** At k: E ∖ L. At i ≠ k: L^{(i)} (B improves odd-i points, and E is odd-k).
- **(c).** On (L₁ ∖ E₁) ∩ (L₂ ∖ E₂) we have X₁ = T ≠ B₂. This set is non-null:
  - for the same class, the layers are nested and contain non-odd-k points;
  - for different classes, Lemma 4.1 applies.
- **(d), refusals (Lemma 2.3) at world k.** Bet_k(B, X) = E ∖ L, since B ⊴_k T everywhere.
  - *T and every other-class member C:* B = C = S on E ∖ L ⊆ U_C, and flipping S → A there worsens k. So U_C ⊄ Up_k(C), and (i) gives nothing. For (ii), C ≠ X = A on Bet_k(B, X), so it gives nothing either.
  - *Same-class t′ < t:* the same, since B_{k,t′} = S on E ∖ L.
  - *Same-class t′ > t:* refusals exist. Every rival has the form B_{k,t′}[G₁ ↦ ·][G₂ ↦ n], with G₁-values ⊵_k those of B_{k,t′} (because B_{k,t′} ⊴_k B, or by n₁ ∈ {S, k-correct} on E ∖ L), and n strictly k-better on G₂. So the rival is strictly k-better, and the forced record is strictly reverse-guidance.
- **(d), covers at world k.** By Lemma 2.1(ii) and (U1), E ∖ L must be covered by a carrier answering A there, i.e. a same-class B₂ = B_{k,t′} with t′ > t. B₂ ≠ T on L, so B₂ covers none of L ∖ E. The other carrier therefore equals T on all of L ∖ E:
  - other-class members are excluded by Lemma 4.1;
  - smaller same-class members by L_k(t′′) ∖ E ≠ ∅;
  - so the other carrier is T.

  With C₂ = T covering L ∖ E and B₂ covering E ∖ L, consider B₂'s link:
  - if B₂ carries t, then t = (E ∖ L : A → S) ⊕ (D″ : B₂ → T);
  - if B₂ carries s, then s = (E ∖ L : A → S) ⊕ (D″ : B₂ → T).

  Either way it is strictly k-improving for the new side (A → S at odd-k points; B₂ → T because B₂ ⊴_k T), hence strictly reverse-guidance.
- **Four advice values.** Intermediates Y with values −h or "contradictory" fall under O and are excluded from carried links (Lemma 2.1(ii)). Lemma 2.3(ii) with n₁ ∈ {S, −h} was covered above. ∎

**Remarks.**
1. **Zero-sum.** All the fills X_E are H-models. Each domination has V_k(d) = −2(p − e) < 0 and is accepted at k; d⁻¹ is refused at all three worlds. No score rule of the forbidden form, and no null-tie breaking, is involved.
2. **Scope.**
   - Minority fills (E of type B_k), unfills, fills outside L_k(t₁), fills of star members other than T, and X\*_j are not covered.
   - For minority fills and unfills the natural defenders are the pure up-shift rays. Joining that star to 𝔾 creates PP76 Example 1.7's shared-layer configuration across complementary classes. That has to be checked against (d) and is OPEN.
3. **Index plan.** Likelihood indexing on the three segments: p(B_{k,t}) := normalise(u + tδ_k). Every member is committed with defence on its full support. The extension to a full selection on Δ, through the edge-admissible end models of the rays, is OPEN.

### 4.4 Sections

**Prop 4.5 (𝔇₁ is closed and record-intrinsic; PROVED).** In the record topology, cl 𝔇₁ ⊆ 𝔇₁ ∪ {∅}.

*Proof.*
- A record d ∈ 𝔇₁ determines (k, t, E):
  - k from the old values;
  - t from the old side on D;
  - E ∖ L = D ∖ L;
  - E ∩ L = (L ∩ Sil(T) ∩ A_k) ∖ D.
- If d_n → r, then along a subsequence k_n = k and t_n → t* ∈ [0, t₁], and E_n converges in measure, because both pieces converge.
- The window inequalities are closed in (t, E) by continuity in measure.
- If e_n → 0, then p(t_n) ≤ K e_n → 0, so t_n → 0 and r = ∅.
- Otherwise (t*, E*) satisfies all the conditions, so r ∈ 𝔇₁. ∎

The upper bound p ≤ Ke matters. Without it, dominations of vanishing fills at a fixed scale t would accumulate at the record (L : B_t → T), which is accepted at all worlds and would make T weakly dominated. This is the record form of PP73's "endpoints repel" and of REFEREE58's counterexample mechanism. With it, every limit is trivial or admissible. Section closure followed by copying therefore stays in 𝔇₁ ∪ {∅}.

**Why the Λ base fails sections, and what replaces it.**
- Members on different rays, say u + sδ_i and u + tδ_j, have log-ratio with a strictly middle coordinate. So balanced non-conic swaps exist between them (PP62 Cor 1.2). Λ satisfies (L0⁺), so Theorem Q(ii) applies once sections are closed.
- Theorem 3.2 is base-agnostic, however.

**Corollary 4.6 (PROVED, conditional).** Let 𝔅 be any base on 𝔾 satisfying (B1) and (B2) with closed fixed-rival sections, for instance one built by REFEREE58's Theorem 6.2′ method. Then 𝔅 ∪ 𝔇₁@{1,2,3} has closed sections, and Theorem 4.3's conclusions hold, with the same proof:
- the proof of Thm 4.3 used Λ only through (B1) (endorsement), strict guiding and (B2);
- strictly reverse-guidance records are refused by any endorsed base.

**CONJECTURE G.** Such a base exists on 𝔾. Evidence:
- **Theorem E is avoidable on 𝔾.** At u, every direction in 𝔾 is a single down-shift, so its Γ has one negative coordinate and lies in no O_w. On the δ_k ray the only O-direction is inward, in O_k. So a tie rule that refuses balanced records out of the δ_k ray at a world ≠ k avoids E (Table 4.5 of PP73 applies verbatim).
- **Theorem Q is avoided** by not containing (L0⁺) (PP72 §2).
- **What is missing** is the full PP72/6.2′-type invariant proof on three rays instead of two. That proof is not given here.

---

## 5. Second application

**Theorem 5.1 (splice-endpoint clause; PROVED, axiom-level given the domination).** Let C, D be committed, let X = C[A ↦ D] be an incoherent splice, and let B″ ⪯_w X be accepted at w. Put D″ := supp rec(B″ → X), P := D″ ∩ A and Q := D″ ∖ A. Then for every F ⊆ {C ≠ D} ∖ D″, (TC) and (IB) give

  ¬[ D ⪯_w D[P ↦ B″][F ↦ C] ]  ∨  ¬[ C ⪯_w C[Q ↦ B″][F ↦ D] ],

unless X ⪯_w B″ is accepted.

*Proof.* Put Y := X[P ↦ B″] and take the copy context W with W = D on F, and W = X elsewhere off D″.
- The triangle B′ → X′ → Y′ → B′ has middle links rec(X′ → Y′) = (P : D → B″) ⊕ (F : D → C), which is carried by D, and rec(Y′ → B′) = (Q : C → B″) ⊕ (F : C → D), which is carried by C.
- (IB) identifies them with the displayed comparisons.
- (TC) would demand X′ ⪯_w B′. ∎

So at every world one endpoint refuses a move toward the new defender. Under an endorsed base the clause holds automatically wherever d″ is favourable (the two V_w values sum to −V_w(d″) < 0). It bites only at unfavourable worlds.

**Prop 5.2 (anchoring fails for T–B splices; PROVED).** Let B = B_{k,t} and X = T[S ↦ B] with S, L ∖ S non-null. Then:
- (i) B is affected at k for every dominator B″ with U_B ≠ ∅: U_B = {B″ = B ≠ X} ⊆ L ∖ S, where flipping B back to T improves k (B ⊴_k T), so U_B ⊆ Up_k(B).
- (ii) If B″ ∈ H and B″ ⊴_k B, then B″ = B on L ⊇ S, so T carries d″⁻¹ and (U1) fails.
- (iii) A posterior anchored for T at i and for B at j must have index c ∈ (u + R₊δ_i) ∩ (b + R₊δ_j), which forces c = b. Since b − u ∈ R₊δ_k lies on a δ-ray, the only decomposition sδ_i − rδ_j has (i, s, r) = (k, t, 0).

*Proof.* (i) and (ii) are Lemma 2.3 and the two-value observation that differing from B on L means reverting to T, which is k-better. (iii): the three δ's span six 60° cones. A vector on a cone boundary has only the degenerate decomposition. ∎

**CHECKED (`second74.out`).** 949 coherent candidates were tried: 49 posteriors inside or beyond (2V), 180 vertex-wise single-world down-shifts, and 720 vertex-wise mixed rescalings, i.e. K = {m_α ∘ v^α}, which is coherent and non-posterior.
- On all 254 cell splices T[S ↦ B₃] and all 254 splices T[S ↦ B₁], **none** passes (N1), (U1) and anchoring.
- On the 62 defender–defender splices B₃[S ↦ B₁], committed {T, B₃, B₁}, **all 62** have anchored candidates, posterior and vertex-wise.

**NUMERICS (`endpoint74.out`).** These use exact cells, float solid-angle masses and u¹ level 0 only.
- Every one of the 254 T[S ↦ B₃] splices has a (2V) posterior dominator passing (N1) and (U1).
- For **222** of them, some such dominator also blocks both endpoint covers (C₁, C₂) ∈ {(B, T), (T, B)} at each of its unfavourable worlds, for every F (Lyapunov interval test).
- The 32 failures all contain coarse cell 5 or the pattern {4, 6, 7}.
- Covers by other star members, and the refusal part of Def. 3.1(d), were **not** checked for these candidates.

**Status of "works twice".**
- Theorem 3.2 is the operation. Applied a second time to T–B splices, it needs a dominator satisfying Def. 3.1 relative to the enlarged 𝒦.
- Theorem 5.1 and Prop 5.2 show what is forced: a non-anchored dominator, and a refusal at an endpoint at each unfavourable world, which (d) turns into a guidance-refusal requirement.
- Numerically, the endpoint part is satisfiable for 87% of cell splices. A proof of (d) for a measurable family of T–B splices is **OPEN**. The proof of Theorem 4.3(d) used monotonicity along one ray, which a transverse dominator does not have.
- Defender–defender splices between different classes are the easy case: anchored candidates exist on every cell splice.

---

## 6. Level of the remaining blocks

| Block | Level | Reason |
|---|---|---|
| Λ base has open sections | choice (property of Λ) | Theorem Q needs (L0⁺); an endorsed base without (L0⁺) is not excluded on 𝔾 (§4.4) |
| Sectioned endorsed base on 𝔾 | CONJECTURE G | Theorem E inapplicable at u and avoidable on the rays; proof not written |
| Carrier-cleanness for T–B splices | choice (the dominator) | 222/254 endpoint-safe at level 0; transverse dominators lose ray monotonicity |
| Anchoring | choice | provably impossible for T–B splices, so ASR's (U2) is abandoned, not the operation |
| X\*_j | geometry of H (PP75/PP76) | dominators must leave H; outside 𝔾 |
| Splice-endpoint clause | axiom-level clause | it never by itself exhausts a source (one refusal per world, at one endpoint) |

No score, symmetry, fixed successor or guidance-worsening assumption is used in Theorem 3.2. Symmetry enters Theorem 4.3 only through Lemma 4.2's formula at u. Guidance-worsening of the defenders (B ⊴_k T) is used in Theorem 4.3, and its absence is exactly what blocks §5.

---

## 7. Scripts (`r9/PP74_py/`; run `python3 -I -B <script>.py > <script>.out` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `asr74.py` | library: coherent D_K by vertex lists, posterior and vertex-wise rescalings, exact cells (PP75's geo75), ASR test (N1, U1, affected pairs, anchors) | library |
| `first74.py` → `first74.out` | class-k fills of T on all unions of pool cells: admissible ray scale for 6/7 per class; the one exception is the innermost cell, which needs a smaller scale than the grid (continuum: Lemma 4.2); affected pairs exactly (T, i ≠ k), anchored at k | CHECKED |
| `layer74.py` → `layer74.out` | α, β₁, β₂, p along the δ₃ ray at five scales; β/p = 0.333 | NUMERICS |
| `second74.py` → `second74.out` | second application with ASR anchoring: T–B₃ 0/254, T–B₁ 0/254, B₃–B₁ 62/62 | CHECKED |
| `endpoint74.py` → `endpoint74.out` | endpoint clause for T–B₃ splices with (2V) posterior dominators: 254/254 pass N1+U1, 222/254 endpoint-safe | NUMERICS |
