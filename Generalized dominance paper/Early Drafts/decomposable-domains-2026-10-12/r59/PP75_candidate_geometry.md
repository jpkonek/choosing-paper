# PP75. Candidate geometry for repairing incoherent H-arrangements

24 October 2026. Geometer, Brief 59. One author; not refereed. Worked concurrently with PP74 (constructor) and PP76 (adversary). None of their output is used here.

**Labels.**
- PROVED: a complete argument is given here.
- CHECKED: exact rational computation in `r9/PP75_py/`; every script ends ALL PASS.
- NUMERICS: none is used.
- CONJECTURE / OPEN: as stated.

**Inputs.**
- BRIEF59 and the three round-59 audits (binding).
- DESIGN_MEMO §8.27 with its correction bullets.
- PP56 §4 (u¹, (2V), R, h); PP72 §§1–4; PP73 (Lemma 1.2, Thm 2.3, Lemma 2.4, Props 3.2–3.4); REFEREE_round57 §4 (forced pattern).
- The coordinator's relay of REFEREE_round58, used as follows:
  - the rescaling inequalities are linear in m;
  - compatibility sets with silence requirements are not convex (Prop 2.1);
  - only geometry and guidance are transported (§8);
  - pure-h fills on the **common silence** are not H-models (§6, Remark 6.3).

**What this note is not.** No relational compatibility is claimed. Everything below is a *necessary* condition on a candidate dominator, derived from:
- reflexivity, strict (G), (IB) and (TC);
- defence of committed models on their support;
- protection and direct (C).

Whether a candidate that passes these conditions can be installed is PP74's question.

---

## 0. Verdict

1. **Exact reformulation (§1–§3; PROVED, CHECKED).**
   - On R an H-model is a set A(X) ⊆ R of h-acceptances. Its world-j error set is W_j(X) = A(X) Δ I_j, where I_j = {g ∈ R : h_j > 0} is the *j-ideal*.
   - Guidance at world j is inclusion of j-error sets. Every guidance statement between H-models is a partial-compatibility statement (Lemma 1.2).
   - **Pattern Lemma (Thm 3.1).** For two posterior models C_a, C_b in the (2V) region, the set of "improvement patterns" on {C_a ≠ C_b} depends only on the **order type of b/a** (13 types). In particular, the two models are pointwise comparable at some world only on single-coordinate shifts.
2. **Necessary conditions (§4; PROVED).** For a candidate B = C_m dominating X, with a committed set 𝒦, three conditions are necessary:
   - **(N1)** B beats X somewhere at every world.
   - **(N2)** The agreement obstruction, generalised to every committed Z: B must not agree with X a.e. on Δ(Z, X).
   - **(N3)** Coupled refusals with **all** common-context copies.

   (N3) has an exact closed form (**Theorem C**), stated in two pattern sets:
   - P1 = the moves of B away from Z that X does not make;
   - P2 = the moves of X away from Z that B does not make.

   Z is left without a defence iff one of two explicit configurations, (Da_k) or (Db_k), occurs. The coupled refusal rule is the special case of (Db_k).

   CHECKED: 1,742 structured comparisons, 264 of them defeats, and 1,632 mixed fills, all against an exhaustive atom-level search, with no mismatch.
3. **The candidate correspondence (§5).** 𝒜_𝒦(X) is an explicit finite Boolean combination of membership bits in partial compatibility sets P(Y; S). Here Y ∈ {X, Z}, and the sets S are explicit pieces of Δ(Z, X) and of its complement, sorted by type. Every such set has the form "closed convex cone minus a union of open cones", which is generally non-convex.
4. **Pure-answer fills and unfills of T (§6; PROVED, CHECKED on 2,052 instances).** Take a type-homogeneous modification with pattern π, and 𝒦 = {T}. Then 𝒜 is N minus the compatibility set P(X; E) minus the following order types:
   - for π = {≠k} (fill A_k, unfill B_k): **{u, raise_k, lower_i, lower_j}**;
   - for π = {k} (fill B_k, unfill A_k): **{u, lower_k}**.

   This holds for every non-null measurable E, small or non-conic included, and 𝒜 is never empty. At rescaled sources, the same table applies to the order type of m/a (§8).
5. **Splices of two rescalings (§7).** By transport, X = C_a[A ↦ C_b] becomes a modification of T.
   - **Small or non-conic A:** a candidate must *side with the source on A* and *side with C_b somewhere in the layer*.
   - **Single-shift (loop-edge) splices:** the weaker step along the same edge is always a candidate (Prop 7.2; PROVED, CHECKED on 1,008 instances).
   - **Generic pairs:** CHECKED non-empty in all 28 tested configurations.
6. **Emptiness and the escape clause (§9).**
   - (a) **The j-ideal H-model X\*_j** (accept h on R iff h_j > 0) is incoherent. It is pointwise j-better than **every** H-model, so **no H-model at all, coherent or not, can dominate it** (PROVED). Global (C) on H therefore *forces dominators outside H*.
   - The requirement "not pointwise j-worse than X\*_j" is met by coherent credal sets outside H. Example: the posterior models C_{u∘(1+te_j)} beyond the neighbourhood. They pass (N1)–(N3) for committed T (CHECKED). **So this obstruction comes from the geometry of H and the neighbourhood, not from the axioms.**
   - (b) One defender for two rivals whose forced refusal sets cover all three worlds: **axiom-level**, for any B (the forced pattern).
   - (c) **New: joint copy-defeat** of *distinct* defenders. Two individually admissible defenders, for class-3 and class-1 fills, that agree on a set S can jointly leave T undefended. This happened for 138 of 1,974 distinct pairs (CHECKED). It is a constraint on choice, not an obstruction: every B₁ keeps a jointly admissible partner.
7. **Transport (§8; PROVED).** 𝒜_{𝒦^b}(X^b) = b∘𝒜_𝒦(X), and P(X^b; b⁻¹S) = b∘P(X; S). Theorem C's pattern sets are invariant. Measures, u¹-values, verdicts and section proofs are not transported.

| Item | Result | Label |
|---|---|---|
| Error sets; guidance = inclusion; guidance = partial compatibility | Lemmas 1.1–1.2 | PROVED |
| Structure of P(X; S); conic-mixing ⇒ empty for every coherent model | Props 2.1–2.2 | PROVED |
| Pattern Lemma | Thm 3.1 | PROVED; CHECKED (380 pairs, all 13 types) |
| (N1), (N2) for all committed Z, copy rule | Thm 4.1 | PROVED |
| Closed form of copy-defeat | Thm C (4.2) | PROVED; CHECKED (3,774 comparisons) |
| Joint copy-defeat | Thm 4.3 | PROVED; CHECKED (2,025 pairs) |
| Type-homogeneous fills and unfills: exact 𝒜, never empty | Thm 6.1, Cor 6.2 | PROVED; CHECKED |
| Naive "generic position" rule for mixed fills | — | **false** (159 of 1,632 instances wrong); Theorem C replaces it |
| Small splices: side with the source on A, with C_b in the layer | Thm 7.1 | PROVED |
| Loop-edge splices: the weaker step is a candidate | Prop 7.2 | PROVED; CHECKED |
| Generic splices non-empty | §7.3 | CHECKED (28 configurations) |
| Committed family members: forced refusals and copy exclusions | §6.4 | PROVED (base); CHECKED (copies) |
| Transport | Thm 8.1 | PROVED |
| X\*_j: no H-dominator; incoherent; escape outside H | Prop 9.1 | PROVED; CHECKED |

---

## 1. Setting and the Boolean model of H

**Setting.** The setting is BRIEF59's, with T = D_M, ε = 3/10 and c = 7/30, so that v^α = (7, 7, 7) + 9e_α (scaled by 30).

The rescaling inequalities read

  **g ∈ C_m ⟺ 7·(m·g) + 9·m_α g_α > 0 for α = 1, 2, 3.**

They are linear in m. Equivalently, C_m(g) = T(m∘g) (PP73 Lemma 1.1).

**Types and orientation.** On R the common answer h is the orientation with u·h > 0 ((2V)). Each g ∈ R has one of six types:
- **A_k:** h has one negative coordinate, k. Then h is right at the two worlds ≠ k.
- **B_k:** h has one positive coordinate, k. Then h is right only at k.

**H.** An H-model X agrees with the common advice off R and answers h or S on R. It is the set A(X) := {g ∈ R : X(g) = h}, modulo null sets.

**Lemma 1.1 (error sets; PROVED).** Put I_j := {g ∈ R : h(g)_j > 0}. At world j on R, X errs exactly on W_j(X) := A(X) Δ I_j. A single W_j determines X, and I₁ ∩ I₂ ∩ I₃ = ∅.

*Proof.* At g ∈ R the two available choices have j-ranks {0, 2} (h) and 1 (S). X errs iff it accepts h where h is j-wrong, or stays silent where h is j-right. So W_j = (A ∖ I_j) ∪ (I_j ∖ A), and A = W_j Δ I_j. On R, h is never right at all three worlds, since unanimous problems lie off R. ∎

**Lemma 1.2 (guidance = inclusion = partial compatibility; PROVED).** For H-models X and Y:
- X ⊵_j Y (pointwise weakly j-better) ⟺ W_j(X) ⊆ W_j(Y) a.e. ⟺ Y agrees with X a.e. on R ∖ W_j(X).
- In particular, **X ⊵_j C_m ⟺ m ∈ P(X; W_j(X))**: C_m repeats every j-error of X.
- **C_m ⊵_j Z ⟺ m ∈ P(Z; R ∖ W_j(Z))**: C_m keeps every j-correct choice of Z.

Distinct H-models are never tied in guidance at any world.

*Proof.* Two different choices at g have different j-ranks. So X is weakly better wherever the two differ iff the difference set avoids W_j(X), and then W_j(X) ⊆ W_j(Y). The other statements are restatements of this. ∎

So the records of H are the error-set descriptions the audit permits: errors removed and errors added. **No cancellation, additive closure or transitivity is used anywhere below.**

**Patterns.** For two H-type models P ≠ Q at g, write π(P → Q)(g) := {worlds at which Q is strictly better}. Because there are only two options, π always has size 1 or 2. The pattern is:
- {≠k} for "gain A_k" or "lose B_k";
- {k} for "lose A_k" or "gain B_k".

Reversing a move complements its pattern.

---

## 2. Compatibility sets

For X ∈ H and S ⊆ R put

  P(X; S) := {m : C_m agrees with X a.e. on S}.

Let Q(g) := {m : (m∘v^α)·h(g) > 0 for α = 1, 2, 3}. This is an open polyhedral cone, linear in m.

**Prop 2.1 (structure; PROVED).** Let ν⁺ and ν⁻ be the direction measures (radial projections) of μ restricted to S ∩ A(X) and to S ∖ A(X). Then, within the (2V) region,

  P(X; S) = {m : (m∘v^α)·h ≥ 0 for every α and every h ∈ supp ν⁺} ∖ ⋃_{h ∈ supp ν⁻} Q(h).

This is a closed convex cone minus a union of open convex cones. It is closed but **generally not convex** (relay item), and it depends on X only through supp ν⁺ and supp ν⁻.

*Proof.*
- μ ≪ Lebesgue measure, so ν^± ≪ the sphere measure, and the great circles ∂A_m are ν-null.
- "S ∩ A(X) ⊆ A_m a.e." ⟺ ν⁺(complement of A_m) = 0 ⟺ supp ν⁺ ⊆ cl A_m.
- "C_m silent a.e. on S ∖ A(X)" ⟺ ν⁻(A_m) = 0 ⟺ A_m ∩ supp ν⁻ = ∅, because A_m is open.
- Under (2V), C_m never answers −h on R. ∎

For an H-model X, P(X) := P(X; R) is a single point (mod scale) when X is posterior, and empty otherwise. Indeed, A_m = diag(1/m)·A(T) determines m through its corner directions (−7/m_α, −7/m_β, 23/m_γ). So the information is carried by the **partial** sets, as the audit said.

**Prop 2.2 (conic mixing; PROVED).** Let f(θ) be the radial fraction of S ∩ A(X) on the ray θ. If ν_S{0 < f < 1} > 0, then **no coherent model whatever** agrees with X a.e. on S. For instance, this holds when X = C[A ↦ D] with A non-conic inside {C ≠ D}.

*Proof.* Coherent models are conic, so on each ray they take a single value. If f ∈ {0, 1} for ν-a.e. θ, then S ∩ A(X) is a.e. a cone (Fubini in polar coordinates). ∎

So **non-conicity is visible to the compatibility sets only as emptiness**. The guidance conditions below see only which (type, value) atoms are non-null.

---

## 3. The Pattern Lemma

**Theorem 3.1 (PROVED; CHECKED `pattern75.py`).** Let a and b be posterior indices in the (2V) region, and r := b/a. The patterns occurring non-null in rec(C_a → C_b) are exactly:

  **{k} iff r_k > min_{i≠k} r_i;  {≠k} iff r_k < max_{i≠k} r_i.**

Their sources are {k} = lose A_k ∪ gain B_k, and {≠k} = gain A_k ∪ lose B_k. **Each pattern has two "twin" sources with the same occurrence condition, one inside A(C_a) and one inside Sil(C_a).**

*Proof.* By transport (§8), take a = u. There are two cases.
- **The A_k cell** (h_k < 0 < h_i, h_j). Vertex k binds for every m, since the vertex-i functional exceeds the vertex-k functional by 9(m_i h_i − m_k h_k) > 0. With h_k = −1:
  - T accepts iff h_i + h_j > 16/7;
  - C_m accepts iff m_i h_i + m_j h_j > 16 m_k/7.

  So "gain A_k" is non-empty iff max(m_i, m_j) > m_k, and "lose A_k" iff min(m_i, m_j) < m_k.
- **The B_k cell** (h_k > 0 > h_i, h_j). Normalise h_k = 1 and put (a, b) := (h_i, h_j) < 0. Then:
  - A(T) ∩ cell is the kite Q = conv{0, (0, −7/16), (−7/23, −7/23), (−7/16, 0)};
  - A_m ∩ cell = diag(m_k/m_i, m_k/m_j)·Q.

  The kite is mapped into itself by every coordinate contraction, and a dilation by λ > 1 moves the vertex (−7λ/16, 0) out of it. So "gain B_k" is non-empty iff max of the two factors exceeds 1 (iff m_k > min(m_i, m_j)), and "lose B_k" iff min of them is below 1.
- The patterns then follow from §1. ∎

CHECKED: 380 exact pairs, covering all 13 order types, including the twin-source assertion and (2V) on every disagreement cell.

**Corollary 3.2 (PROVED).** C_b ⊵_w C_a pointwise iff r is a single raise of w. C_b ⊴_w C_a iff r is a single lower of w. **For generic r the two models are mixed at all three worlds.** This is PP57 Lemma 4.1 together with its converse.

---

## 4. Necessary conditions

Throughout:
- B ⪯_i X is installed for i = 1, 2, 3, with X incoherent;
- 𝒦 is a set of committed models, each coherent, defended on {1, 2, 3}, protected and satisfying direct (C).

Put Δ(P, Q) := {P ≠ Q}.

**Theorem 4.1 (PROVED).**
- **(N1)** For each j, X ⋭_j B. Equivalently, m ∉ ⋃_j P(X; W_j(X)): **B must fix some error of X at every world.**
- **(N2) Generalised agreement obstruction.** For each Z ∈ 𝒦 such that Δ(Z, X) is not a.e. a cone (or, more generally, the hybrid B[Δ(Z, X) ↦ Z] is incoherent): **m ∉ P(X; Δ(Z, X))**. The audit's obstruction is the case Z = the source C (Δ = Mod(X)). With Z = D it is "endpoints repel" (PP73 Prop 3.3(b)).
- **(N3) Copy rule.** For Z ∈ 𝒦 and a non-null S ⊆ Δ(Z, B), the following holds.

  If X ▷_j B[S ↦ Z] by strict guidance, then Z ⋠_j Z[S ↦ B].

  Hence Z must defend against Z[S ↦ B] at a world j where neither X ▷_j B[S ↦ Z] nor Z[S ↦ B] ▷_j Z.
  - With S = Δ(Z, B) this is the audit's **coupled refusal rule**: X ▷_j Z ⇒ Z ⋠_j B.
  - Every model that agrees with Z on S inherits the refusal (by (IB)), so these are *all* the refusals one domination forces on Z-carried records.

*Proof.*
- (N1) is strict (G).
- (N2): if B = X a.e. on Δ(Z, X), then rec(B → X) = rec(B′ → Z) with B′ := B[Δ(Z, X) ↦ Z]. Indeed, the supports and values agree, because X = Z off Δ(Z, X).
  - So B′ ⪯_i Z for every i. Protection of Z then gives Z ⪯_i B′ for every i: an all-world tie.
  - B′ is incoherent: on a ray that meets Δ(Z, X) only partially, B′ takes both values. This contradicts direct (C).
- (N3): put Y := B[S ↦ Z]. Then rec(Y → B) = (S : Z → B) = rec(Z → Z[S ↦ B]).
  - If Z ⪯_j Z[S ↦ B], then Y ⪯_j B by (IB).
  - Together with B ⪯_j X and the guidance link X ⪯_j Y, the triangle is accepted, so (TC) installs Y ⪯_j X. That reverses strict guidance.
  - A rival W of Z carries a record of the form rec(Y′ → B) only if W = Z[S ↦ B] with S = Δ(Z, W). ∎

**Theorem C (closed form of (N3); PROVED; CHECKED `theoremC75.py`, `theoremC75b.py`, `mixed75.py`).** Let Z, B and X be two-valued (h/S) on their difference sets. Put:
- P1 := patterns of Z → B on Δ(Z, B) ∖ Δ(Z, X) (B's moves that X does not make);
- P2 := patterns of Z → X on Δ(Z, X) ∖ Δ(Z, B) (X's moves that B does not make).

For each k, write {i, j} for the two other worlds. Then:
- **(N1) ⟺ ⋃P1 ∪ ⋃{complement of p : p ∈ P2} = {1, 2, 3}.**
- **(N2) ⟺ P2 ≠ ∅.**
- **Z is defeated** (left with no admissible defence against some Z[S ↦ B], the base rule included) **iff, for some k:**
  - **(Da_k)** {≠k} ∈ P1 ⊆ {{≠k}, {i}, {j}}, k lies in every member of P2, and (P2 ≠ ∅ or P1 meets {{i}, {j}}); **or**
  - **(Db_k)** ∅ ≠ P1 ⊆ {p : k ∈ p}, P2 ⊆ {{≠k}}, and (P2 ≠ ∅ or {k} ∈ P1).

Under (N2), the parenthetical conditions are automatic: (Da_k) reads "every unshared B-move except some {≠k}-moves is k-neutral, and every unshared X-move improves k", and (Db_k) reads "every unshared B-move improves k, and every unshared X-move has pattern {≠k}".

*Proof.* Split Δ(Z, B) ∪ Δ(Z, X) into three regions:
- U₁ := Δ(Z, B) ∖ Δ(Z, X), carrying patterns P1;
- U₂ := Δ(Z, X) ∖ Δ(Z, B), carrying patterns P2;
- U₃ := the intersection, where X = B ≠ Z.

Write S = S₁ ∪ S₃ with S₁ ⊆ U₁ and S₃ ⊆ U₃. Y_S differs from X exactly on (U₁ ∖ S₁) ∪ U₂ ∪ S₃. So:
- **Refusal block at j**, X ▷_j Y_S, holds iff three things are true and the union is non-null: j ∉ p on U₁ ∖ S₁, j ∈ p for every p ∈ P2, and j ∈ p on S₃.
- **Guidance block at j**, Z[S ↦ B] ▷_j Z, holds iff S ≠ ∅ and j ∈ p on all of S.

A point of S₃ would need j ∈ p for all three j, since each world is blocked by one of the two modes. That is impossible, so S₃ = ∅.

Let G be the set of guidance-blocked worlds and R the rest. Then:
- R ⊆ ⋂P2;
- every atom of S₁ has pattern ⊇ G;
- every atom of U₁ ∖ S₁ has pattern disjoint from R.

G = ∅ forces P2 = ∅ and P1 = ∅, which is trivial. |G| = 3 is impossible. The two remaining cases are:
- G = {i, j}, R = {k}: this is (Da_k);
- G = {k}, R = {i, j}: this is (Db_k).

The parenthetical conditions are the non-nullity conditions. Atoms may be split between S₁ and its complement (they then satisfy both constraints), which is why the criterion is stated in patterns. ∎

CHECKED:
- 400 random H-type configurations;
- 1,742 structured ones (fills, unfills, mixed fills, and splices at both ends), with 264 defeats;
- 1,632 mixed fills.

In every case the closed form agrees with an independent exhaustive search over S (three states per atom, eight mode vectors). The naive rule ("excluded = {u} ∪ {lower_j : j ∈ ⋂Π} ∪ …", with Π the set of X's patterns) is **false** in 159 of the 1,632 mixed instances. The failure occurs when a piece of X lies inside C_m's own change region; Theorem C is the correct statement.

**Theorem 4.3 (joint copy-defeat; PROVED; CHECKED `joint75.py`).** Let dominations B_r ⪯ X_r, r ∈ G, be installed, and let S ⊆ ⋂_r Δ(Z, B_r) be a set on which all the B_r agree. Then rec(Z → Z[S ↦ B_r]) is the same record for every r ∈ G. So Z refuses it at every world blocked for *some* r (by Theorem 4.1(N3)) or blocked by guidance, and Z needs a world outside that union.

*Proof.* The record depends only on B_r|_S. ∎

Example. Take X₁ a small class-3 A-fill and X₂ a small class-1 A-fill of T, with B₁ and B₂ each individually admissible (§6).
- On the candidate grid, 2,025 such pairs exist.
- **All 51 same-model pairs are defeated.** This is the forced-pattern pigeonhole.
- **138 of the 1,974 distinct pairs are jointly defeated.** An example is B₁ = C_{(21/20, 1, 1)}, B₂ = C_{(441/400, 21/20, 1)}, with modes (guidance, refusal₁, refusal₂).
- Every B₁ keeps a jointly admissible B₂.

This is the precise form of "choose defenders by which joint defence options survive".

---

## 5. The candidate correspondence

**Definition.** Let N be a (2V) neighbourhood of u, 𝒦 a committed set and X a rival. Then

  𝒜_𝒦(X) := {m ∈ N : (N1), and for every Z ∈ 𝒦, (N2) and not (Da_k ∨ Db_k for any k)}.

**Explicit form (PROVED; read off from Theorem C).** Each pattern bit is a non-membership in an explicit partial compatibility set:
- [p ∈ P2(Z)] = [m ∉ P(X; Δ(Z, X)^p)], where Δ(Z, X)^p is the part of X's moves with pattern p.
- [p ∈ P1(Z)] = [m ∉ P(Z; R_Z^p ∖ Δ(Z, X))], where R_Z^p is the set where a p-move from Z is available. For p = {k}, R_Z^p is (A(Z) ∩ A_k-type) ∪ (Sil(Z) ∩ B_k-type). For p = {≠k}, it is (Sil(Z) ∩ A_k) ∪ (A(Z) ∩ B_k).

By Theorem 3.1, P1 ⊆ the pattern set of the order type of m/z. **So 𝒜_𝒦(X) is a finite Boolean combination of order-type strata (the braid arrangement m_i/z_i = m_j/z_j) and of sets "closed convex cone minus a union of open cones".** It is computable exactly from the cell arrangement of 𝒦 ∪ {X's pieces} ∪ {C_m} (`geo75.candidate_check`).

**Which committed sources must refuse C_m, and where.**
- *Base rule:* Z must refuse C_m at the worlds F(Z, X) := ⋂{patterns of Z → X}, **independently of m**.
- *Copies:* Z must refuse Z[S ↦ C_m] at R-worlds, as in Theorem C. These refusals depend on m through P1 and P2.
- *Surviving defence:* the worlds outside the blocked set. Theorem C says exactly when no such world remains.

---

## 6. Pure-answer fills (and unfills) of T

**Theorem 6.1 (PROVED; CHECKED `fills75.py`, 2,052 instances).** Let X = T ⊕ E be a modification of one type: either a fill of A_k or B_k on E ⊆ Sil(T), or an unfill on E ⊆ A(T), with E non-null and measurable (arbitrarily small or non-conic allowed). Let π be its pattern, and 𝒦 = {T}. Then

  **𝒜_T(X) = N ∖ (P(X; E) ∪ Excl_π),**

where:
- **Excl_{≠k} = {u} ∪ raise_k ∪ lower_i ∪ lower_j** (fill A_k, unfill B_k);
- **Excl_{k} = {u} ∪ lower_k** (fill B_k, unfill A_k).

Here raise_k and lower_k are the single-shift strata (two equal coordinates of m).

*Proof.*
- P2 = {π} under (N2). The pattern π has a twin source on the other side of ∂A(T) with the same occurrence condition (Thm 3.1), and that twin is disjoint from E. So **P1 = Pat(m)**, whatever E is.
- **π = {≠k}.** (N1) needs worlds i and j to be covered by Pat(m). By Thm 3.1, world i fails iff m_i ≤ min and m_j = m_k = max, i.e. m ∈ {u} ∪ lower_i.
  - (Da_l) needs l ∈ π, so l ≠ k, and Pat(m) has no pattern containing l, so m ∈ lower_l.
  - (Db_l) needs P2 = {{≠l}}, so l = k, and every pattern of m contains k, so m ∈ raise_k.
- **π = {k}.** (N1) fails iff no pattern of m contains k, i.e. m ∈ {u} ∪ lower_k. (Da_l) forces l = k and m ∈ lower_k. (Db_l) would need P2 = {{≠l}}, which is impossible.
- The P(X; E) term is (N2). ∎

**Corollary 6.2 (never empty; PROVED).** For every such X, 𝒜_T(X) contains all generic m close enough to u. As m → u, μ(E ∩ Δ(T, C_m)) → 0 by continuity in measure, so E ⊄ the moves of C_m. The natural repairer of a class-k A-fill (the lower_k ray) is admissible exactly below its **agreement threshold**, sup{t : C_{u∘(1−te_k)} is still silent on part of E}. This is PP72's τ, now derived as a necessary condition.

**Remark 6.3 (relay: common-silence fills).** If E lies in the common silence (off R), then X ∉ H. Theorem 6.1 still holds verbatim, because no H-membership was used. Moreover P(X; E) ∩ N = ∅: every C_m with m ∈ N is silent on E, so (N2) is automatic. Mixed modifications are handled by Theorem C. There P1 can lose a pattern when X covers an entire change region of C_m, which is what defeats the naive rule.

**6.4 Committed family members (PROVED for the base rule; CHECKED `family75.py`).** Let X be a small class-3 A-fill of T, and let C_c also be committed.
- **Base rule** (E not inside C_c's change region): the forced refusals are T at {1, 2}, and every member of the lower_j ray (j = 1, 2) at world j. No other member is forced, because F(C_c, X) ∋ j requires T ⊵_j C_c, which by Cor 3.2 means c ∈ lower_j. Every member keeps a world, because at most one coordinate can be raised.
- **Copies remove, in addition** (in terms of the order type of m/c):
  - for c ∈ lower₁: {lower₁, gen231};
  - for c ∈ lower₂: {lower₂, gen132};
  - for c ∈ lower₃, the natural repairer's own ray: {raise₃, gen123, gen213};
  - for c ∈ raise₁: {lower₁, raise₃, gen123, gen213}.

  (gen-abc lists the coordinates of m/c from smallest to largest.)

So committing earlier defenders thins later candidate sets in explicit chambers, not everywhere.

---

## 7. Splices between two posterior models

**7.1 Reduction.** By §8, X = C_a[A ↦ C_b] with 𝒦 ⊇ {C_a, C_b} becomes X = T[A′ ↦ C_{b/a}], where A′ = a∘A, 𝒦 ⊇ {T, D := C_{b/a}}, and C_m becomes C_{m/a}. Then:
- relative to T, X is a modification whose patterns are those of Pat(b/a) met by A′;
- relative to D, X = D[L ∖ A′ ↦ T], whose patterns are the complements of those met by L ∖ A′, where L := Δ(T, D).

**Theorem 7.1 (small or non-conic A; PROVED).** Let A′ lie inside one cell of the arrangement {T, D, C_m}, with the pattern π₀ of T → D there. (A′ may be arbitrarily small and non-conic.) Then m ∈ 𝒜_{T,D}(X) iff all of the following hold:
- **(T-side)** C_m = T a.e. on A′ (**side with the source on A**), and m/a ∉ Excl_{π₀} (Theorem 6.1);
- **(D-side)** P2(D) := patterns of D → T on (L ∖ A′) ∩ {C_m = D} is non-empty (**side with D somewhere in the layer**), and Theorem C holds for P1(D) = {complement of π₀} ∪ {patterns of D → C_m off L};
- (N1).

*Proof.* Theorem C, applied at both ends. On A′, C_m = T ≠ D, so the move D → C_m there has pattern complement(π₀). Off L, D = T. ∎

**Prop 7.2 (loop-edge splices; PROVED; CHECKED `edge75.py`, 1,008 instances, three sources, all w).** Let b = a∘(1 + te_w) be a single shift. Then **m = a∘(1 + t′e_w), with t′ below the threshold at which C_m reaches A**, is in 𝒜_{C_a, C_b}(X).

*Proof.*
- Along a single shift, each vertex functional is affine in t′ with slope v^α_w h_w, whose sign is common to the three functionals. So the change sets are nested: Δ(T, C_m) ⊆ L, and C_m = D on it.
- T-side: P1(T) = {{w}, {w, i}, {w, j}}, and P2(T) = {π₀} with π₀ in the same set. (Db_w) needs P2 ⊆ {{i, j}}, which fails. (Da_k) needs P1 ⊆ {{≠k}} ∪ singletons, which fails.
- D-side: P1(D) = {complement(π₀)} and P2(D) = {{i, j}, {i}, {j}}. Neither (Da) nor (Db) is satisfied.
- (N1) holds on both sides. ∎

So **the second application** (splices between a source and its new single-shift defender) **always has an in-family candidate** at the guidance level. It is the next smaller step along the same edge, which keeps the source's advice on A.

**7.3 Generic pairs and large A (CHECKED `splice75.py`).** The test covers:
- b ∈ {raise₁, lower₃, gen123, gen312};
- every pattern class of the layer, with A either a small piece or the whole class;
- 24 candidates each.

Admissible candidates were found in all 28 configurations (4 to 21 of 24). The exclusions follow Theorem C. Most are (N2) at T, that is, the candidate fails to side with the source on A. Large A (all of L except a small piece) is the mirror case, with T and D exchanged.

---

## 8. Transport

**Theorem 8.1 (PROVED).** For b ≫ 0 define the pullback Y^b by Y^b(g) := σ·g whenever Y(b∘g) = σ·(b∘g). Then:
- C_m^b = C_{m∘b};
- ranks are preserved, because b∘g has the sign pattern of g;
- null sets, records, (IB) copies, conicity and coherence are preserved;
- types and patterns are preserved.

Hence:
- P(X^b; b⁻¹∘S) = b∘P(X; S);
- 𝒜_{𝒦^b}(X^b) = b∘𝒜_𝒦(X);
- Theorem C's sets P1 and P2 are invariant.

In particular, **𝒜_{C_a}(C_a[E ↦ h]) = a∘𝒜_T(T[a∘E ↦ h])**. So Theorem 6.1 holds at every rescaled source, with the order type of **m/a** in place of that of m.

*Proof.* The map g ↦ b∘g is linear, invertible and sign-preserving. Then C_m(b∘g) = T(m∘b∘g). Every condition in §4 is built from pointwise ranks, null sets and records. ∎

**Not transported (relay):**
- μ, |g| and every u¹-quantity (V, Φ, balance);
- verdicts and section proofs;
- the committed set itself: 𝒦^b ≠ 𝒦 in general.

---

## 9. Emptiness and the escape clause

**Prop 9.1 (the j-ideal H-model; PROVED; CHECKED `xstar75.py`).** Let X\*_j accept h on R iff h_j > 0, and agree with the common advice off R.
- (a) W_j(X\*_j) = ∅. So X\*_j ⊵_j Y for every H-model Y, strictly if Y ≠ X\*_j. **(N1) fails for every H-model, coherent or not, and 𝒜_N(X\*_j) = ∅.** Conversely, if X ∈ H is not one of X\*_1, X\*_2, X\*_3, some H-model passes (N1): flip one error set at each world. So X\*_1, X\*_2 and X\*_3 are the only H-models that (N1) alone leaves with no H-dominator.
- (b) **X\*_j is incoherent**, under the hypothesis (thin_j): some b ∈ A(T) ∖ R has b_j < 0. This holds for every small enough N.
  - *Proof.* Take a junction q ∈ ∂A(T) with q_j = 0. R contains a neighbourhood of q, because v^α∘q is not proportional to 1, so both signs of dm move the boundary there.
  - Take a outside A(T), close to q, with 0 < a_j ≪ dist(a, ∂A(T)).
  - The segment [a, b] enters A(T) at a point c near q, and c_j < 0. Just past c the points lie in R with h_j < 0, so X\*_j is silent on an open set of positive combinations of accepted gambles.
  - CHECKED for 𝒮 = u plus its six shifts by 21/20, with an explicit rational certificate. ∎
- (c) **Incompatible requirement:** "do not be pointwise j-worse than X\*_j". **Escape:** any coherent model that improves the common advice at world j somewhere off R, or answers −h at some point of R with h_j < 0, meets it. Examples are V_j and C_{u∘(1+te_j)} beyond N.
  - CHECKED: 12 such posterior candidates (t from 1/5 to 3, plus small perturbations) pass (N1), (N2) and (N3) with all copies for committed T.
  - **Verdict: the obstruction comes from the geometry of H and the neighbourhood, not from the axioms. But it is forced that every dominator of X\*_j lies outside H.** The construction must therefore repair some H-models with models that change the common advice off R. Once such a model is committed, R grows.

**Other emptiness sources.**

| Requirement | Empty for | Escape (any coherent credal set?) | Level |
|---|---|---|---|
| One B dominating rivals whose base refusal sets F₁ ∪ F₂ ∪ … cover {1, 2, 3} for a committed Z (e.g. class-k and class-k′ fills of T) | every B | no | axiom-level (REFEREE57 §4.1; reproduced, 51/51) |
| Distinct B₁ and B₂ agreeing on S, with jointly blocked worlds covering {1, 2, 3} (Thm 4.3) | that pair | yes: another partner always survives on the grid | choice-level |
| (N1) against X\*_j | all of H, hence all of N | yes, outside H | geometry of H and the neighbourhood |
| Type-homogeneous fills and unfills, loop-edge small splices, committed ends | never (Cor 6.2, Prop 7.2) | — | — |
| Generic splices, committed ends | none found (28 configurations) | — | CHECKED only |

**OPEN.**
- Whether some incoherent H-model *other than* X\*_j has 𝒜_N(X) = ∅ with 𝒦 = {source, ends}. A candidate mechanism: X covers whole change regions of every C_m near u, so P1 loses patterns.
- The emptiness structure when the committed set is a 2-D family. Theorem C makes this a finite computation per chamber, but it was not carried out here.

---

## 10. For the constructor (PP74) and the adversary (PP76)

- **Usable invariants.** All candidate information is in the pattern sets P1 and P2 relative to each committed model (Theorem C). These sets are record-level, hence stable under (IB) copying. They are also invariant under transport.
- **Necessary defence plan.** For each Z ∈ 𝒦 and each installed domination, Z's defending world against Z[S ↦ B] must lie outside the blocked set of Theorem C. Across several installed dominations whose defenders agree on S, the blocked sets add (Thm 4.3).
- **Hand-over.**
  - Not addressed here: section closure, section closure followed by copying (the PP72 gap), and (TC) chains through two installed non-guidance acceptances.
  - The H-ideal models X\*_j are a mandatory test: their dominators lie outside H.

---

## 11. Scripts (`r9/PP75_py/`; run `python3 -I -B <script>.py > <script>.out` inside the folder)

| Script → output | Content | Label |
|---|---|---|
| `geo75.py` | exact chart cells (Fraction polygon splitting in a box containing every vertex of the arrangement); answers, ranks, patterns; checker for (N1), (N2), (N3) with copies (exhaustive over S) | — |
| `pattern75.py` → `.out` | Pattern Lemma, twin sources, (2V) on 380 pairs and all 13 order types; comparability only on single shifts | CHECKED |
| `fills75.py` → `.out` | Theorem 6.1: 24 classes × small/whole × grid, 2,052 instances | CHECKED |
| `mixed75.py` → `.out` | mixed fills: the naive rule fails (159 instances); Theorem C holds (1,632) | CHECKED |
| `theoremC75.py`, `theoremC75b.py` → `.out` | closed form against exhaustive search: 400 random and 1,742 structured comparisons (264 defeats) | CHECKED |
| `joint75.py` → `.out` | joint copy-defeat: 2,025 pairs; same-model 51/51; distinct 138; survival for every B₁ | CHECKED |
| `splice75.py` → `.out` | splices of two rescalings, 28 configurations × 24 candidates, with reasons | CHECKED |
| `edge75.py` → `.out` | Prop 7.2 at three sources (transport), 1,008 small splices | CHECKED |
| `family75.py` → `.out` | §6.4: base refusals and copy exclusions for committed ray members | CHECKED |
| `xstar75.py` → `.out` | Prop 9.1: X\*_3 strictly 3-better than every member of 𝒮; incoherence certificate; 12 escape candidates outside H | CHECKED |
