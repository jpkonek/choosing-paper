# PP78. The three-ray allocation: Conjecture G holds, with a refusing world that rotates with the carrier ray

24 October 2026. Allocator, Brief 60 (three-ray track). One author; not refereed. Scripts in `r9/PP78_py/`.

Labels: PROVED / CHECKED / CONJECTURE / NUMERICS.

---

## 0. Verdict

**Conjecture G is true (PROVED, under the hypotheses of §1.1).** On the three-ray star 𝔾 there is one record-based relation 𝓑 with the following properties.
- Every acceptance is u¹-endorsed (V_w ≥ 0 at its world). Endorsement is never relaxed.
- It satisfies reflexivity, strict (G), (IB) with all copies, (TC) on every triangle of measurable models, and closed fixed-rival sections on 𝔾, including at T.
- Every member of 𝔾 is defended against every measurable rival. It is undominated, has no all-world tie partner, and satisfies direct (C).

The construction adds no lexicographic levels and no realisation problem.

**The real content of the conjecture**, in four facts:

1. **Coincidence never happens on a dangerous record (PROVED, in every endorsed sectioned base).** A balanced (u¹-null) record is *dangerous* if a member carries its reverse. Only dangerous records can produce a protection or (C) failure. Every member carrying a dangerous record lies on **one ray**, and T never carries one (Lemma 2.2). The dangerous records are exactly the cross-ray balanced swaps: B_{k,t} → B_{m,s} on odd-n points, where n is the third world. So section limits and copies can force such a record at its own ray's world k and at one more world, but never at all three.
2. **The relay's test (PROVED; CHECKED).** Balanced records carried by interior members of all three rays exist. Every endorsed sectioned base must accept them at all three worlds. They are harmless: every such record is carried by T, and **no member carries its reverse** (Prop 2.4). Their reverses are dangerous, but no member carries them, so no section forces them anywhere.
3. **The device that makes sections closed (PROVED).** There are six exact Γ-shapes ±(3e_k − 1) on 𝔾. A cyclic margin rule puts each of them in exactly one closed class: the inward shape of ray k in class k, the outward shape in class k+1 (Lemma 3.2). The refusing world therefore rotates: **a dangerous record carried by ray k is refused at world k−1**.
4. **The invariant (PROVED).** Every non-trivial record accepted at w is u¹-endorsed and lies in
   𝒦_w = G_w ∪ cl(A_w) ∪ 𝔉_w ∪ 𝒪_{w+1}:
   - G_w: guidance at w;
   - cl(A_w): the closed margin class;
   - 𝔉_w: null records carried by the two-ray path ray w ∪ ray w−1;
   - 𝒪_{w+1}: null records supported in odd-(w+1) points.

   Each class depends on the record alone, so copies cannot move a record out of it. The first two classes are closed along fixed-rival sections. The last two are closed under (TC), by a monotone potential along the path (Lemma 4.1).

**Consequence.** PP74 Cor 4.6 now holds without Conjecture G. Every majority pure fill of Theorem 4.3 is strictly dominated in one relation with closed sections on 𝔾 (Cor 5.1). This still depends on Lemma 4.2's quantitative input (α ≤ a·p), and it needs one extra case, which Lemma 5.2 proves.

| Item | Statement | Label |
|---|---|---|
| Point types of the layers | Lemma 1.1 | PROVED; CHECKED (0 exceptions on 15 members) |
| Exact Γ-shapes on 𝔾 | Lemma 1.2 | PROVED; CHECKED (deviation ≤ 3·10⁻¹⁶) |
| Forced verdicts in every endorsed sectioned base | Prop 2.1 | PROVED |
| Dangerous records are carried on one ray only, never by T | Lemma 2.2 | PROVED; CHECKED |
| Relay test: three-ray-carried null records exist and are harmless | Prop 2.4 | PROVED; CHECKED |
| Cyclic margin rule separates the six Γ-shapes | Lemma 3.2 | PROVED; CHECKED |
| Path potential: (TC) among path-carried null records | Lemma 4.1 | PROVED; CHECKED (8.1·10⁶ points, 0 violations) |
| **Conjecture G** | Thm 4.2 | **PROVED** |
| PP74 Cor 4.6 / Thm 4.3 with closed sections | Cor 5.1, Lemma 5.2 | PROVED, given PP74 Lemma 4.2's input |

---

## 1. Setting and the three geometric facts used

### 1.1 Hypotheses

- **Family.** Three worlds, Gaussian μ, four advice values, T = D_M with ε = 3/10. δ_k := (1,1,1) − 3e_k is the pure down-shift of world k. B_{k,t} := C_{tδ_k} for t ∈ [0, t₁], so B_{k,0} = T. 𝔾 := ⋃_k {B_{k,t}}, with the star topology (equivalently, the index topology).
- **(Sym), (2V).** u¹ is PP56's field for PP62's S₃-symmetric family 𝒮₀ = {a : normalise(1/a) ≥ c + η} (REFEREE58 §1.1), with t₁ small enough that 𝔾 ⊆ 𝒮₀. R := R(𝒮₀). Members are pointwise λ-Bayes for λ = (1,1,1), with equality exactly on R for the values {h, S} (PP62 (U2)–(U3)).
- **(CM) Continuity in measure.** t ↦ B_{k,t} is continuous in μ-measure. This follows from monotone layers whose level sets {g changes exactly at t} lie in finitely many planes. Per the audit, it is stated as a hypothesis wherever sections are transferred.
- **(p).** p(t) is continuous and strictly increasing, with p(0) = 0 (PP74 §4).

### 1.2 Notation

- **Records.** rec(X → Y), with support, old values and new values. Z *carries* r if Z = old(r) a.e. on supp r. V(r) := Φ(new) − Φ(old) ∈ R³ (u¹-loss increase), and r is accepted at w only if V_w(r) ≥ 0 (endorsement).
- **Null and dangerous records.** r is *null* if V(r) = 0. It is *dangerous* if it is null and some member carries r⁻¹, i.e. some member equals new(r) a.e. on supp r.
- **H-records.** A record is an H-record if supp r ⊆ R and both sides take values in {h, S} there.
- **Odd world and type.** Each g ∈ R has mixed signs, so it has an odd world o(g) (PP62 §1.1). Its **type** is σ(g) = +1 if flipping T's value at g (h ↔ S) improves o(g), and σ(g) = −1 otherwise.
- **c-vector.** For an H-record, c_o(r) is the |g|-mass of the odd-o points where the new side improves o, minus the mass where it worsens o. Then V(r) = Σ_o c_o(r)(e − 3e_o), so

  **r is null ⇔ c₁(r) = c₂(r) = c₃(r)** (PP62 (1.1)).

**Lemma 1.0 (sums; PROVED).** For a member W and any model Y:
- ΣV(rec(W → Y)) ≥ 0 and ΣV(rec(Y → W)) ≤ 0;
- equality holds iff the record is an H-record.

In particular, every null record that is carried by a member, or whose reverse is carried by one, is an H-record.

*Proof.* This is pointwise λ-Bayes optimality with the equality case (U3). ∎

**Lemma 1.1 (layer types; PROVED).** L_k(t) := {B_{k,t} ≠ T} consists of points of type (k, −) and points of type (o, +) with o ≠ k. Along each ray every point changes its value at most once, so the layers are nested. Consequently:
- a point of type (o, −) can lie only in layers of ray o;
- a point of type (o, +) can lie only in layers of the two rays other than o;
- **no point lies in layers of all three rays.**

*Proof.* The log-ratio tδ_k has coordinate k strictly minimal and the other two tied at the maximum. Apply PP62 Lemma 1.1: odd-k points worsen world k, and odd-i points (i ≠ k) improve world i. Monotonicity is PP57 Lemma 4.1. ∎

CHECKED (`check78.out` [1]): there are no wrong-type layer points on 15 members (5 scales × 3 rays), and there are no (2V) violations.

**Lemma 1.2 (exact Γ-shapes; PROVED).**

  Φ(B_{k,t}) = Φ(T) + p(t)(3e_k − e),  where e = (1,1,1).

Hence, for a fixed rival X and sources on ray k,

  V(C_q → X) = V(C_a → X) + (p(t_a) − p(t_q))(3e_k − e).

At a null limit V(C_a → X) = 0, the approximating vectors are therefore exactly:
- **inward** (t_q < t_a): γ(3e_k − e), with γ > 0, which is endorsed only at k;
- **outward**, including from T along ray k: γ(e − 3e_k), which is an exact tie between the two worlds other than k.

Φ is injective on 𝔾.

*Proof.* V(T → B_{k,t}) = p(3e_k − e) is PP74 §4 (the formula uses β_i = β_j, which is the (i j)-symmetry of PP62 Lemma 1.3(b)). Additivity of Φ gives the second formula. Injectivity holds because the three directions 3e_k − e are distinct and p is strictly increasing. ∎

CHECKED ([2]): the deviation from p(3e_k − e) is ≤ 3·10⁻¹⁶ on the S₃-symmetric sample, both from T and between members of one ray.

---

## 2. What every endorsed sectioned base must do: records, carriers and coincidences

Following the brief, I keep for each record the set of worlds at which it *must* be accepted, and then ask which of these forced sets can cover {1, 2, 3} on a dangerous record.

**Prop 2.1 (forced verdicts; PROVED).** Let 𝓡 be any relation satisfying (IB) and closed fixed-rival sections on 𝔾, in which every member defends every rival at some u¹-endorsed world. Let r be null.
- (i) If B_{k,t} carries r with t > 0, then r is accepted at k.
- (ii) If B_{k,t} carries r with t < t₁ (t = 0 allowed, i.e. T), then r is accepted at some world other than k.

*Proof.* Let Z = B_{k,t} and X = Z ⊕ r.
- (i) Take sources B_{k,t_n} with t_n ↑ t. By Lemma 1.2, V(B_{k,t_n} → X) = γ_n(3e_k − e), which is endorsed only at k. So each source defends at k, and the closed section at Z gives Z ⪯_k X. By (IB), r is accepted at k.
- (ii) Take t_n ↓ t. Now V = γ_n(e − 3e_k), so each source defends at i or j. Infinitely many choose the same world, and the closed section gives the result. ∎

So for a null record r:
- every ray carrying r at an interior or end point (t > 0) adds its own world;
- every ray carrying r below its end (t < t₁) adds "some world other than its own".

The forced verdicts of two records **coincide** only when the records are equal, since verdicts are functions of records. The question is therefore which carrier patterns can occur on one record.

**Lemma 2.2 (carriers of dangerous records; PROVED).** Let r be dangerous, with W a member carrying r⁻¹, and let Z be a member carrying r. Then:
- Z and W lie on different rays k ≠ m (neither is T);
- supp r consists of odd-n points, where n is the third world, and r is a balanced swap

  r = (P₁ : B_{k,t} → T) ⊕ (P₂ : T → B_{m,s}),  P₁ ⊆ L_k ∖ L_m,  P₂ ⊆ L_m ∖ L_k,  both of odd type n, with equal |g|-mass.

Moreover, **every member carrying r lies on ray k.**

*Proof.*
- r is a null sub-record of rec(Z → W), because Z = old(r) and W = new(r) on supp r.
- **Same ray, or one of them T.** Then log(W/Z) is a multiple of some δ_k. Its two non-k coordinates tie, so it has no strictly middle coordinate. By PP62 Cor 1.2 (balanced sub-records lie in the strictly middle world), r is trivial.
- **Different rays k ≠ m.** Here log(W/Z) = sδ_m − tδ_k has coordinates
  - k: s + 2t (the maximum);
  - m: −2s − t (the minimum);
  - n: s − t (strictly middle).

  Cor 1.2 gives supp r ⊆ odd-n, and the two-valued form gives the displayed swap.
- **A second carrier.** Let Z′ be a member carrying r on another ray k′ ≠ k. The same argument applied to (Z′, W) forces k′ ≠ m and supp r ⊆ odd-n′, where n′ is the third world of {k′, m}. But k′ ≠ k, m means k′ = n, so n′ = k. Then supp r ⊆ odd-n ∩ odd-k = ∅. ∎

CHECKED ([4]): for the four ordered ray pairs at scale 0.03 there are balanced swaps with masses 0.00452 on each side. Among 15 sampled members, each swap is carried only by its own ray's member, and its reverse only by the other ray's member.

**Cor 2.3 (PROVED).** In every endorsed sectioned base, Prop 2.1 forces a dangerous record at **at most two** worlds:
- its ray's world k, if some carrier has t > 0;
- one world other than k, if some carrier has t < t₁.

The forced set is all three worlds only for a null record that has interior carriers on all three rays. Such a record is never dangerous (Prop 2.4).

**Prop 2.4 (the relay's test; PROVED; CHECKED).** Null records with interior carriers on all three rays exist. Every such record r is carried by T, and no member carries r⁻¹. So accepting r at all three worlds, which Prop 2.1 forces in **every** endorsed sectioned base, yields neither a weak domination of a member nor an incoherent all-world partner.

*Proof.*
- **Carried by T.** Let B_{k,t_k} (k = 1, 2, 3) agree on F = supp r. On F their common flipped set is contained in L₁ ∩ L₂ ∩ L₃, which is empty by Lemma 1.1. So all three equal T on F.
- **Reverse not member-carried.** A member W carrying r⁻¹ would differ from T on all of F. Then r would be a null sub-record of the pure-shift pair rec(T → W), which is trivial (Lemma 2.2's first case).
- **Harmless.** A weak domination of a member, or an incoherent all-world partner of a member W, is an all-world acceptance of a record rec(Y → W). Such a record has its reverse carried by W, and r does not.
- **Existence.** Take F inside R, off the layers of the t₁-members. In each odd class choose equal |g|-mass of type-(o,+) and type-(o,−) points. Then every c_o = 0.

CHECKED ([5]): inside the 0.15-layers but outside all t₁ = 0.05 layers, each odd class contains positive mass of both types (0.0435 and 0.0551). The constructed F (311,010 sample points) has V = 0, is carried by all 15 sampled members, and its reverse by none. ∎

r⁻¹ is dangerous, because its new side is T. But no member carries it, so Prop 2.1 forces it nowhere. In the allocation below it is refused at two or more worlds (Lemma 4.3(c)).

**Elimination table (null records, by carrier pattern).** The middle column holds in every endorsed sectioned base. The last column is for the allocation 𝓑 of §3.

| Carrier pattern of r | Dangerous? | Forced (Prop 2.1) | 𝓑 accepts at | 𝓑 refuses at |
|---|---|---|---|---|
| one ray k, some carrier with 0 < t < t₁ | possibly | k and one of k ± 1 | k, k+1 (and n−1 only by (TC), if supp ⊆ odd-n) | **k−1** |
| only B_{k,t₁} | possibly | k | k (n−1 by (TC)) | k−1 |
| no member | possibly | nothing | at most n−1, by (TC) | at least two worlds |
| T, or interior points of all three rays | never | ≥ 2 worlds; all three if interior on three rays | 1, 2, 3 | none (harmless, Prop 2.4) |
| interior points of two rays k, k′ | never | k, k′ | ⊇ {k, k′} | depends on carriers |

The obligations in the middle column are independent across records, apart from (TC) links. So the only remaining question is whether (TC) and iterated section closure push a dangerous record into its third world. §4 shows they do not, for the allocation of §3.

---

## 3. The allocation

**Definition 3.1 (cyclic margin rule).** Worlds are read cyclically: 3 + 1 = 1. Fix κ ∈ (0, 1/2).

For v ∈ R³ with v ≠ 0 and Σv ≥ 0, put M := max v and N(v) := {w : v_w ≥ M − κ|v|_∞} (the near-maximal worlds). The rule 𝒟(v) is:
- N = {w}: choose w;
- N = {w, w+1}: choose w (the cyclic predecessor);
- N = {1, 2, 3}: choose 1.

A_w := 𝒟⁻¹(w), and cl(A_w) is its closure in {Σv ≥ 0} ∖ {0}.

**Lemma 3.2 (PROVED; CHECKED).**
- (a) Every v in cl(A_w) satisfies v_w ≥ (½ − κ)|v|_∞ > 0. So 𝒟 is endorsed with a uniform margin, and limits with v_w → 0 are null.
- (b) The inward shape 3e_k − e lies in cl(A_k) and in no other cl(A_w). The outward shape e − 3e_k lies in cl(A_{k+1}) and in no other.

*Proof.*
- (a) Σv ≥ 0 gives M ≥ |v|_∞/2. Indeed, if −min v = |v|_∞ > M, then |v|_∞ ≤ (sum of the other two coordinates) ≤ 2M. Membership in cl(A_w) requires v_w ≥ M − κ|v|_∞.
- (b) cl(A_w) ⊆ {v_w ≥ M − κ|v|} ∩ {v_{w−1} ≤ M − κ|v|}, plus, for w = 1, the region where all three worlds are near-maximal. The shapes give:
  - for 3e_k − e (|v| = 2): only k is near-maximal, since −1 < 2 − 2κ;
  - for e − 3e_k: N = {k+1, k+2} robustly. The predecessor k+1 is in the closure. The successor k+2 would need v_{k+2} − v_{k+1} ≥ κ|v|, which fails at the exact tie. ∎

CHECKED ([6]): each of the six shapes lies in exactly one class, as stated. Over 2·10⁵ random v with Σv ≥ 0 the rule covers v, and the minimum of v_w/|v| over its classes is 0.38 ≥ ¼.

**Definition 3.3 (the relation 𝓑).** 𝓑 is the least relation containing:
- reflexivity and weak guidance at every world;
- the defences 𝒟, for every member C and every measurable X, applied to r = rec(C → X):
  - if V(r) ≠ 0, accept r at 𝒟(V(r)); this is legitimate because ΣV(r) ≥ 0 by Lemma 1.0;
  - if V(r) = 0, accept r at k when C = B_{k,t} with t > 0, and at world 1 when C = T;

and closed under:
- (TC)-completion (an accepted triangle at w forces its three reverses at w);
- fixed-rival section limits on 𝔾.

Verdicts are sets of (record, world) pairs, so (IB) and every common-context copy are built in. The least fixed point exists by Knaster–Tarski and is reached through transfinite stages (as in PP72 Def. 6.1).

---

## 4. The invariant and Conjecture G

**Classes.**
- **G_w:** non-trivial guidance records at w (new side pointwise weakly w-worse).
- **𝔉_w:** null records carried by a member of the **path** P_w := {B_{w,t} : 0 < t ≤ t₁} ∪ {B_{w−1,t} : 0 ≤ t < t₁}, which contains T.
- **𝒪_n:** null H-records supported (a.e.) in odd-n points.
- **𝒦_w** := G_w ∪ cl(A_w) ∪ 𝔉_w ∪ 𝒪_{w+1}.

Each class is a property of the record alone.

**Path coordinate.** x ∈ [−t₁, t₁], with x < 0 ↔ B_{w−1,−x}, x = 0 ↔ T, x > 0 ↔ B_{w,x}.

**Lemma 4.1 (path potential; PROVED; CHECKED).**
- (a) Let P, Q ∈ P_w with x_Q > x_P. Then at every odd-(w−1) point of {P ≠ Q}, Q is (w−1)-better, and at every odd-w point of {P ≠ Q}, Q is w-worse.
- (b) Consider an accepted-candidate triangle X₁ → X₂ → X₃ → X₁ whose three links are null H-records, each in 𝔉_w ∪ 𝒪_{w+1}. Then every link is supported in odd-(w+1) points, so all three reverses lie in 𝒪_{w+1}.

*Proof.*

(a) For every pair, d = log(Q/P) has w−1 as a maximal coordinate and w as a minimal one. Three cases:
- inward on ray w−1: d ∝ −δ_{w−1};
- across T: d = x_Qδ_w + x_Pδ_{w−1}, whose (w−1)-, w- and (w+1)-coordinates are x_Q − 2x_P, −2x_Q + x_P and x_Q + x_P (with x_P ≤ 0 ≤ x_Q);
- outward on ray w: d ∝ δ_w.

Apply PP62 Lemma 1.1 (i) and (ii).

(b) **Setting up.**
- On the union of the supports, the three models take two values, and each point lies in exactly two link supports.
- At a point of odd world o ∈ {w−1, w}, both links containing it are 𝔉_w-links, because 𝒪-links avoid such points. Let P_a, P_b, P_c be path carriers.
- At such a point in S_ab := supp a ∩ supp b, link a moves P_a(g) → P_b(g) and link b moves it back. The same holds cyclically for S_bc and S_ca (direct check of the three cases X₁ = X₃, X₁ = X₂, X₂ = X₃).

**The potential.** Put D(ℓ) := c_{w−1}(ℓ) − c_w(ℓ). By (a), each such point of S_xy contributes +|g| to D(x) if x_y > x_x, and −|g| otherwise, and the opposite to D(y). Null links have D = 0. Write m_xy for the odd-{w−1, w} mass of S_xy.
- **All three links in 𝔉_w.** For the link with the smallest carrier coordinate, both contributions are positive. So its two masses vanish, and then the third mass vanishes too.
- **Exactly two links (a, b) in 𝔉_w.** The odd-{w−1, w} points lie in S_ab only, and D(a) = ±m_ab = 0.
- **Fewer than two.** No point of odd world w−1 or w lies in two 𝔉-supports, so the union of the supports contains none.

So all supports are null off odd-(w+1). ∎

CHECKED ([3]): on all pairs of 11 sampled members of each of the three paths, 8.1·10⁶ changed points were checked, with 0 violations of (a).

**Theorem 4.2 (Conjecture G; PROVED under §1.1).** 𝓑 has the following properties:
- every acceptance is u¹-endorsed;
- reflexivity, strict (G), (IB) and (TC) hold on all measurable models;
- fixed-rival sections are closed on 𝔾;
- every member is defended against every measurable rival, is undominated, has no all-world tie partner, and satisfies direct (C).

*Proof.* The core is the following invariant.

**Invariant (J_G).** For every stage and every non-trivial (r, w) accepted:
- (J1) V_w(r) ≥ 0;
- (J2) r ∈ 𝒦_w;
- (J3) if r is non-null, then r ∈ G_w ∪ cl(A_w), and in particular V_w(r) > 0;
- (J4) every null r accepted at w is an H-record.

Induction over the stages; unions at limit stages preserve the invariant.

1. **Generators.**
   - Guidance: G_w, with V_w > 0 (u¹ is strictly guiding and ranks are injective at each world).
   - Non-null defences: A_w ⊆ cl(A_w), endorsed by Lemma 3.2(a).
   - Null defences: by Lemma 1.0 they are H-records. The record carried by B_{k,t} with t > 0, accepted at k, lies in 𝔉_k, since B_{k,t} ∈ P_k. The record carried by T, accepted at 1, lies in 𝔉₁, since T ∈ P₁.
2. **(TC).** An accepted triangle at w has links with V_w ≥ 0 summing to 0, so every link has V_w = 0. By (J3) all three links are null, so by (J2) and (J4) they are null H-records in 𝔉_w ∪ 𝒪_{w+1}. (A trivial link makes the other two mutual inverses, and nothing new is installed.) Lemma 4.1(b) puts the reverses in 𝒪_{w+1}: they are null, satisfy V_w = 0 and are H-records. In particular, (TC) never installs a non-null record.
3. **Section limits.** Let C_{a_n} ⪯_w X be accepted at earlier stages with a_n → a, a_n ≠ a, and r := rec(C_a → X) non-trivial. V(C_{a_n} → X) → V(r) by (CM) and dominated convergence.
   - The approximants are never null. Two null records with the same rival would give Γ(a, a_n) = 0, so a_n = a by injectivity (Lemma 1.2). So by (J3) each approximant lies in G_w ∪ cl(A_w). Pass to a subsequence that stays in one class.
   - **r non-null.** cl(A_w) is closed in {Σ ≥ 0} ∖ {0}. G_w is closed along sections: along a subsequence, C_{a_n} = C_a eventually a.e. (ranks are discrete), so the pointwise inequality passes to the limit. So r lies in the same class.
   - **r null.**
     - The approximants are exactly Γ-shapes (Lemma 1.2).
     - They cannot lie in G_w infinitely often: otherwise r would be weakly w-guidance and non-trivial, so V_w(r) > 0.
     - So they lie in cl(A_w). By Lemma 3.2(b), either they are inward shapes of ray w, or they are outward shapes of ray w−1 (including the approach to T along ray w−1).
     - Accordingly, r is carried by B_{w,t} with t > 0, or by B_{w−1,t} with t < t₁. Either way r ∈ 𝔉_w, and it is an H-record by Lemma 1.0.
4. **Copies.** All classes are properties of the record. This is where the REFEREE58 mechanism (a limit at another source and rival, transported by (IB)) is absorbed: the transported record sits in the same class at every carrier.

**Consequences of (J_G).**
- **Strict (G).** A strictly reverse-guidance record has V_w < 0, which (J1) excludes.
- **Defence.** Every member defends every rival: through 𝒟 at a world in A_w, or at k or 1 for null rivals.
- **Reflexivity, (IB), (TC) and closed sections** hold by construction.
- **Protection, ties and (C):** Lemma 4.3. ∎

**Lemma 4.3 (refusal of dangerous records; PROVED).** Let r be dangerous.
- (a) If r is carried by a member, then by Lemma 2.2 all its carriers lie on one ray k, not T, and supp r ⊆ odd-n with n ∉ {k, m}. Then r is **refused at k−1**: the path P_{k−1} uses rays k−1 and k+1, so r ∉ 𝔉_{k−1}, and r ∉ 𝒪_k because n ≠ k.
- (b) Every non-null record whose reverse a member carries has ΣV ≤ 0 (Lemma 1.0). So an all-world acceptance of it would have V = 0, i.e. it would be null.
- (c) If no member carries r, then r ∉ 𝔉_w for every w. So it is accepted only at worlds w with supp r ⊆ odd-(w+1). That is at most one world.

**Hence.** No record rec(Y → W) with W a member is accepted at all three worlds. So every member is undominated, has no all-world tie partner (an all-world tie needs that record), and satisfies direct (C). Rules III and IV never fire. ∎

**Remark (where the refusals sit).** The essential refusals are of dangerous cross-ray swaps r = (P₁ : B_{k,t} → T) ⊕ (P₂ : T → B_{m,s}) at world k−1.
- Their openness along every section through every carrier (all on ray k) comes from two facts: inward approximants are endorsed only at k, and outward ones are exact (k+1, k+2)-ties that only class k+1 contains.
- Their reverses are refused at m−1.
- r is accepted at {k, k+1} and r⁻¹ at {m, m+1}; the two sets share one world, where r and r⁻¹ form a single-world tie. Single-world ties are allowed.

(TC) does fire. For example, take odd-(w+1) swaps among carriers on ray w−1, ray w and ray w−1 again. Every reverse it installs lies in 𝒪_{w+1}. Those are the only acceptances of 𝓑 that no member carries.

---

## 5. Consequences for PP74, and what changes

**Cor 5.1 (PP74 Thm 4.3 with closed sections; PROVED given PP74 Lemma 4.2's quantitative input).** 𝓑 ∪ 𝔇₁@{1,2,3} has the following properties:
- every property of Theorem 3.2's first three bullets;
- closed fixed-rival sections on 𝔾;
- every majority pure fill T[E ↦ h], E ⊆ Sil(T) ∩ A_k ∩ L_k(t₁), is strictly dominated by every B_{k,t} with t ∈ W_θ(E).

*Proof.*
- **Hypotheses (B1) and (B2).** (B2) is Theorem 4.2. (B1) holds except that 𝓑 accepts non-carried null records in 𝒪_{w+1} at w.
- **Where carriedness is used.** PP74's proof of Thm 3.2 uses carriedness only in step 3 (Lemmas 2.2–2.3), for triangles through a domination d at its unfavourable world k. The new cases, in which one link is in 𝒪_{k+1}, are excluded by Lemma 5.2.
- **The rest.** Every other ingredient (refusals forced at carriers being strictly reverse-guidance; covers having a strictly reverse-guidance link) is endorsement-only, so it holds for 𝓑. Prop 4.5 of PP74 (𝔇₁ is closed and record-intrinsic) gives sections. ∎

**Lemma 5.2 (PROVED).** Let d = rec(B → X) ∈ 𝔇₁ be of class k, with copy (B′, X′), and consider a triangle B′ → X′ → Y → B′ at world k. If one of its links s := rec(X′ → Y), t := rec(Y → B′) lies in 𝒪_{k+1}, the triangle is not accepted.

*Proof.*
- **The other link.** Both links null would give V_k(s) + V_k(t) = −V_k(d) ≠ 0. So the other link is non-null, has V_k > 0 and, by (J3), is guidance or member-carried.
- **Case s ∈ 𝒪_{k+1}.** Then s does not touch E ∖ L (odd-k) or L^{(k−1)} (odd-(k−1)). So t moves A → S on E ∖ L and moves T-values to flipped values on L^{(k−1)} ⊆ supp d.
  - t is not k-guidance: A → S improves k on the non-null set E ∖ L (PP74 Thm 4.3, (N1)).
  - t is not carried. A carrier answers A on E ∖ L, so it is B_{k,t′} with t′ > t (PP74 (U1) argument). But that member is flipped on L^{(k−1)}, whose mass β is positive (PP74 Lemma 4.1), while the carrier must take T's values there.
- **Case t ∈ 𝒪_{k+1}.** Symmetrically, s moves A → S on E ∖ L, with the same two contradictions. ∎

**What changes in the programme.**
1. **Cor 4.6 is no longer conditional on Conjecture G.** The first application (all majority pure fills of T, every class) now lives in one relation with universal defence, protection, direct (C), (TC) and closed sections on 𝔾. The remaining conditions are those listed by the audit:
   - the uniform bound α(t) ≤ a·p(t);
   - (CM), stated as a hypothesis;
   - REFEREE59 item 4 (PP74 Thm 3.2 only for H-models inside R), which is satisfied because E ⊆ L_k(t₁) ⊆ R.
2. **The audit's three-ray calculation (REFEREE59 relay item 1) is consistent with this.** The inward vector of the world-1 ray must fall in a world-1 class, so 6.2′'s fixed refusal at world 1 is abandoned. The refusing world is k−1 for records carried by ray k.
3. **The invariant is not record-closed.** The audit's distinction (binding answer 3) is essential here. Any class closed under *arbitrary* record convergence that contains all member defences contains every member-carried null record at every world. This is because a member-carried null record r is a record limit of r ⊕ (vanishing odd-k pieces whose V lies in O_k := {v_k > 0 > v_i, v_j}), and such defences must be accepted at k. 𝓑 uses only fixed-rival section limits, where null limits have exactly Γ-shaped approximants (step 3).

---

## 6. Level, scope and limits

- **Endorsement is never relaxed.** No non-endorsed acceptance is needed on 𝔾. The only departure from PP74's (B1) is non-carried acceptances, and they are confined to 𝒪_{w+1} (null odd-(w+1) swaps installed by (TC)).
- **What the proof uses about 𝔾.** Four facts:
  - finitely many family directions with exact Γ-shapes, which needs (Sym);
  - each point lies in the layers of at most two rays (Lemma 1.1);
  - dangerous records are carried on one ray (Lemma 2.2);
  - monotone c-potentials along each two-ray path (Lemma 4.1).
- **Why it does not transfer to two-dimensional families (observation, not a theorem).** The margin device needs every family direction's Γ-shape to lie in exactly one closed class. On a 2-D posterior neighbourhood the Γ-directions fill a circle, and closed classes covering a circle must overlap. This is the setting of PP62 Theorem E. An extension beyond stars must therefore come from the second-generation construction (PP77's track), not from this allocation.
- **A linear priority also works for Theorem 4.2.** With 1 ≻ 2 ≻ 3:
  - world 3's null acceptances are carried by ray 3 alone, and (TC) never fires there;
  - world 2's acceptances are carried by the path of rays 1 and 2;
  - world 1 is uncontrolled, but it is not needed: dangerous records are refused at 3, or at 2 if they are carried by ray 3.

  The cyclic rule is preferred, because it controls every world and gives Cor 5.1 for all three classes.
- **Not done.**
  - Extending the selection beyond 𝔾 (to edge end models or to Δ).
  - Sections for defenders outside 𝔾.
  - Minority fills, unfills, X\*_j.
  - The second application (PP77).

---

## 7. Responses to the relays

| Item | Response |
|---|---|
| REFEREE59 (1): the 6.2′ invariant fails on the world-1 ray | Agreed and used. The refusing world rotates (k−1 for ray-k records), and the six Γ-shapes are separated by the cyclic margin rule (Lemma 3.2). |
| REFEREE59 (2): the three-ray test | Such records exist (Prop 2.4; CHECKED [5]) and are forced at all three worlds in every endorsed sectioned base. They yield no (C) or protection failure, because each is carried by T and no member carries its reverse. No non-endorsed acceptance is needed. |
| REFEREE59 (3): uses of (CM) | Stated as hypothesis (CM). It is used in three places: continuity of V along sections, closure of G_w, and Lemma 1.2's injectivity argument via p. |
| REFEREE59 (4): Thm 3.2 only for H-models in R | Cor 5.1 uses it only for Thm 4.3's fills, which lie in L_k(t₁) ⊆ R. |
| Brief: build by records; test cross-ray splices first | §2 does this. Cross-ray balanced splices are exactly the dangerous records (Lemma 2.2), and their forced worlds are {k, one other}. |
| Brief: identify the surviving property | (J_G) in §4: record-intrinsic classes, closed along sections or under (TC), with each Γ-shape in exactly one class. |

---

## 8. Scripts (`r9/PP78_py/`; run `python3 -I -B check78.py > check78.out` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `lib78.py` | Sample, posterior advice by vertex inequalities, odd world and type σ, u¹ on H-records, star members, margin-rule classes | library |
| `check78.py` → `check78.out` | [1] (2V) and layer types; [2] exact Γ-shapes; [3] path monotonicity; [4] cross-ray balanced swaps and their carriers; [5] relay test (three-ray-carried null record, reverse not carried); [6] margin-rule class separation and endorsement margin | CHECKED / NUMERICS (N = 1.8·10⁶, S₃-symmetric) |
