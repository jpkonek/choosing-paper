# K1. The end-protected class on M_U: per-world safe tests, countable ends, and the one equivalent question

15 Oct 2026, round 19 (BRIEF16; BRIEF13 rules). Labels: **PROVED** (full proof here, from results proved and
refereed in the write-up, or re-verified here), **CHECKED**, **CONJECTURE**, **NUMERICS** (none; `k1py/` holds no
script, since no statement here rests on computation). No assumption is added.
Setting and notation: write-up §§2–3, §7.7; E1_notes §2.1 (end, S-positive, eventually ≥ 0 / = 0, end-protected,
base comparison); H1_notes §§1–3 (Φ_t, d_t, Lemma H1.0, Lemma H1.1); H2_notes §§1–4 (H2.0, T1-correct and T1-wrong
ends, V(W), R⁰_i, conflict digraph Γ); J1_notes (switched models, (Al)); H12_referee (Prop. R.1).
n = 3, U = D_{K′}, M_U, σ_k = sign h_k, E_k(X) = X △ (U ∩ {h_k > 0}).
(H_U) = strict (G), (IB), (LA), (S), (C), T1 ∈ C_L on M_U.

---

## 0. Outcome

**The class is not settled either way. The deliverable is the third option of the brief: one precise question,
K1.Q, with a proof that it is equivalent to the class question (Theorem K1.6). On the way, two exclusions are
extended from finitely many to countably many ends, which closes part (c) of the brief except along conflict
cycles that admit no aligned order.**

The class (EP∞). (H_U) holds; every world k is end-protected with a **countable** family 𝒮_k (possibly empty);
there are ρ_k ∈ L¹(μ), ρ_k > 0 a.e., with ρ_kμ endorsing every relevant world-k comparison whose vector is
eventually 0 on every S ∈ 𝒮_k (the base comparisons). A world that adds up with a countably additive weight is in
the class with 𝒮_k = ∅. A world that adds up only through a purely finitely additive weight has no integrable
endorser and is not in the class (it is case (A′) of H12 §1.7); I add nothing about it.

**New tool: per-world safe tests (Theorem K1.2, PROVED).** H1.0(c) tests all three worlds against **one** model.
That is what made the dominator's copy depth matter. It is enough to find one selected C and three models
A_1, A_2, A_3, **one per world**, such that
- C ⪯_k A_k for each k,
- A_k is **k-safe**: correct at world k a.e. deep in every end of world k (depths may differ from end to end),
- Σ_k t_k ψ_k(A_k) < m_t := min over coherent models of Σ_k t_k ψ_k.

Then every C ⪯_k A_k is base (protection, with no copy depth and no finiteness), hence endorsed, and
Σ t_kψ_k(C) < m_t, which no coherent C can do. The A_k need not be close to each other or to B_t.

**What the tool settles (PROVED).**
- **K1.3 (KKM form).** If one model X is (G)-at-least-as-good at each world k as some k-safe A_k with the cost bound,
  there is no cover. With countable families this needs only that, at some choice of depths, deep ends of different
  worlds never conflict.
- **K1.4 (countable ends, acyclic Γ).** J1.1 / Prop. R.1 (H2.3 without heaviness) hold for **countable** families.
  The pigeonhole over finitely many ends is replaced by a diagonal argument over depth assignments, after a countable
  form of the shadowing lemma H2.1(b) (Lemma K1.1).
- **K1.5 (countable ends, aligned orders).** J1.2 holds for countable families, with alignment stated end by end
  (condition (Al∞)).

**Where it stops (the single obstruction).** Via the KKM lemma, K1.2 reduces everything to a covering property of the
selection p ↦ C_p against the three fixed safe tests (Lemma K1.6(a)). A cover in the class exists **iff** some
ranking in the class has, for every admissible choice of safe tests, a selection index p that is **anti-safe**: C_p
loses at every world of supp p to that world's own safe test. Anti-safe points need two worlds of supp p whose deep
ends conflict at the chosen depths (K1.6(b)3); such conflicts persist at every depth only when the deep ends of
two worlds overlap on R_ij at every depth, as an arrow of Γ does. They are exactly what the shell exchanges of J1.5 and the germ
exchanges of H2 §5.2 amount to at the level of the selection. Competitiveness of C_p is only against **single**
models, and a single model cannot be safe at two worlds whose deep ends conflict. I could neither exclude anti-safe
points nor build a ranking with them.

| | Statement | Label |
|---|---|---|
| K1.0 | Safe closure: a comparison into a k-safe model is base (countable families) | PROVED |
| K1.1 | Shadowing of T1-wrong ends, countable families, every depth assignment | PROVED |
| K1.2 | Per-world safe tests give a contradiction | PROVED |
| K1.3 | KKM form; no cover if deep ends can be made conflict-free | PROVED |
| K1.4 | Acyclic conflict digraph ⇒ no cover, countable families | PROVED |
| K1.5 | Aligned order (Al∞) ⇒ no cover, countable families | PROVED |
| K1.6 | Cover in (EP∞) ⟺ positive answer to K1.Q (anti-safe selection points); properties of anti-safe points | PROVED |
| K1.Q | Is there a ranking with (H_U) in (EP∞) with anti-safe points for every safe triple? | open |

Relation to the brief's (a)–(c):
- **(a)** Doubly misaligned cycles are exactly the configurations in which no order is aligned. K1.6 shows that
  their survival is equivalent to K1.Q, and that what has to be decided is a property of the selection, not of the
  dominators' copy depths.
- **(b)** 3-cycles, and 2-cycles whose third world has ends, are excluded whenever some order is aligned (K1.5).
  Otherwise they fall under K1.Q.
- **(c)** Countably many ends: acyclic Γ (K1.4) and aligned orders (K1.5) are excluded, with non-uniform depths.
  The rest is K1.Q.

---

## 1. Standing facts (re-verified)

**(F1) Admissibility and a weight (PROVED; H1.1 + M0closed(a)).** Under (EP∞) let ψ := (ρ_kμ)_k. Choose depths
a_S(m) ↑ ∞ for all ends of all worlds with Σ_S μ(S_{a_S(m)}) → 0 (a summable choice; the families are countable),
and put D_m := ⋃_S S_{a_S(m)}. A comparison T1 ⪯_k Y with Y regular and Y = T1 on D_m has vector 0 on every
S_{a_S(m)}, so it is base and ρ_k-endorsed. Lemma H1.1 then makes ψ admissible. By M0closed(a) (no integrability
used) the set I_ψ := {t ∈ Δ° : Z_t null, B_t incoherent} is not null. H12 §1.3 records that H1.1 needs only
countably many ends, for exactly this summable choice.

**(F2) The gap (PROVED; H1.0(a),(b)).** Fix t ∈ I_ψ. For a regular model Y with finite costs put
T(Y) := Σ_k t_kψ_k(Y). By H1.0(b) and the referee's line (H12 §1.2), T(Y) − T(B_t) = Φ_t(Y) for every regular Y,
with all terms finite (ρ integrable). By H1.0(a), d_t := min{Φ_t(C) : C coherent} > 0 is attained. So
m_t := min{T(C) : C coherent} = T(B_t) + d_t, and T(C) ≥ m_t for every coherent C.

**(F3) Refinement (PROVED; H2.0).** Ends may be refined to be orthant-pure and T1-pure; the refined family is
countable, protection and base comparisons are unchanged. Each refined end S has a **purity depth** n_S beyond
which it lies in one orthant and is T1-correct or T1-wrong at its world.

## 2. Safe closure, and shadowing with countably many ends

A model A is **k-safe** if A is regular and there are depths (a_S)_{S∈𝒮_k} with A correct at world k a.e. on
S_{a_S} for every S ∈ 𝒮_k. If 𝒮_k = ∅, every regular model is k-safe.

**Lemma K1.0 (safe closure; PROVED).** Assume (EP∞). If C ∈ C_L and A is k-safe with C ⪯_k A, the comparison is base.

*Proof.* δ := 1_{E_kA} − 1_{E_kC} ≤ 0 a.e. on S_{a_S}, since A makes no world-k error there. So {δ = 1} ∩ S_{a_S} is
null and δ is S-positive for no S ∈ 𝒮_k. The comparison is relevant (C ∈ C_L, A regular), so end-protection makes δ
eventually ≥ 0 on every S, say on S_{b_S}. Then δ = 0 a.e. on S_{max(a_S, b_S)} for each S. ∎

No uniform depth is claimed or needed: base means "eventually 0 on each end", end by end. This is J1.0 without its
maximum over the family.

A **depth assignment** for a family 𝒯 of ends is a map M : 𝒯 → ℕ, S ↦ M_S. Assignments are ordered pointwise; a
larger assignment gives smaller sets ⋃_S S_{M_S}.

**Lemma K1.1 (shadowing, countable families; PROVED).** Assume (EP∞). Let W ∈ 𝒮_i be T1-wrong, in the orthant O,
and let 𝒯 be the set of T1-correct ends of the worlds of V(W). For every depth assignment M on 𝒯 there is m′ with

  W_{m′} ⊆ ⋃_{S ∈ 𝒯} S_{M_S}  (mod null).

*Proof.* Enlarging M only shrinks the right side, so it suffices to prove the claim for larger assignments. Enlarge
M so that M_S ≥ n_S for all S ∈ 𝒯, and extend it to all ends of all worlds by values N_E ≥ n_E with
Σ_E μ(E_{N_E}) < μ(R⁰_i)/2 over all ends E of all worlds (possible: countably many ends, each E_m ↓ a null set).
Put M_S := max(M_S, N_S) on 𝒯 and M_E := N_E elsewhere.

1. *T1-wrong ends of V(W)-worlds do not matter.* Let E be a T1-wrong end of j ∈ V(W). On O, T1 is right at j, so
   a.e. point of W_{m} (m ≥ n_W) lies outside E_j(T1), while E_{M_E} ⊆ E_j(T1) a.e. So W_m ∩ E_{M_E} is null.
2. *The set R.* R := R⁰_i ∖ ⋃_E E_{M_E} (union over all ends of all worlds) is non-null by the mass bound.
3. Suppose the claim fails for M. Then P_{m′} := W_{m′} ∖ ⋃_{S∈𝒯} S_{M_S} is non-null for every m′ ≥ n_W. Choose
   non-null p_{m′} ⊆ P_{m′} with Σ_{m′} ρ_j(p_{m′}) < min_{j∈V(W)} ρ_j(R), and p := ⋃_{m′} p_{m′}. Put
   X := T1 △ (p ∪ R); X is regular (p ∪ R ⊆ M).
4. As in H2.1 (re-verified, H12 §2.1):
   - at j ∈ A(W), X is strictly better than T1 by (G), so T1 ⋠_j X;
   - at i, δ_i = 1_R − 1_p is −1 on p ∩ W_{m′} for every m′, so not eventually ≥ 0 on W; it is +1 only on R, which
     misses every i-end at depth M_E, so it is positive on no i-end. End-protection forbids T1 ⪯_i X;
   - T1 is competitive on {1,2,3} (Theorem kkm: tied at every world with a selected C_q, competitive on supp q).
     So T1 ⪯_j X for some j ∈ V(W).
5. There δ_j = 1_p − 1_R. On every end E of j it vanishes at depth M_E: R misses E_{M_E}; p misses S_{M_S} for
   S ∈ 𝒯 by construction, and misses the T1-wrong ends at depth M_E by step 1. So the comparison is base, and
   ρ_j(R) ≤ ρ_j(p), against the choice of p. ∎

**Corollary K1.1′ (diagonal pigeonhole; PROVED).** In the situation of K1.1, let P ⊆ W meet W_m non-nully for
every m. Then some S ∈ 𝒯 has μ(P ∩ W_m ∩ S_n) > 0 for all m, n.

*Proof.* Enumerate 𝒯 = {S¹, S², …} (if 𝒯 is empty, K1.1 gives W_{m′} null for some m′, which is impossible).
Suppose each S^k has (m_k, n_k) with P ∩ W_{m_k} ∩ S^k_{n_k} null. Choose M_k ≥ n_k with
μ(S^k_{M_k}) ≤ 2^{−k−1} μ(P ∩ W_{m_k}); the right side is positive, and S^k_M ↓ a null set. K1.1 for the
assignment k ↦ M_k gives m′ with P ∩ W_{m′} ⊆ ⋃_k (P ∩ W_{m′} ∩ S^k_{M_k}) mod null.
- If m_k ≤ m′, the k-th set lies in P ∩ W_{m_k} ∩ S^k_{n_k}, which is null.
- If m_k > m′, its measure is ≤ 2^{−k−1} μ(P ∩ W_{m_k}) ≤ 2^{−k−1} μ(P ∩ W_{m′}).

So μ(P ∩ W_{m′}) ≤ ½ μ(P ∩ W_{m′}), hence μ(P ∩ W_{m′}) = 0, a contradiction. ∎

This replaces the finite pigeonhole of H2.3 Step 4 and of J1.1 ("one S does so for infinitely many M"), including
the arrow-depth adjustment of H12 §2.4: μ(W_m ∩ S_n) > 0 for all m, n is the arrow condition of Γ (it is
equivalent to μ(W_m ∩ S_m) > 0 for all m, since both sequences decrease).

**Lemma K1.0′ (the same, for vectors; PROVED).** If C ⪯_k X is relevant and δ := 1_{E_kX} − 1_{E_kC} ≤ 0 a.e. on
S_{a_S} for every S ∈ 𝒮_k (depths end by end), the comparison is base, and C = X a.e. on S_{m′_S} for some depths
m′_S ≥ a_S. *Proof:* that of K1.0; δ = 0 iff C and X give the same advice (advice on U is determined by the error
status at one world). ∎

## 3. Per-world safe tests

Fix (EP∞), ψ, t ∈ I_ψ and T, m_t as in (F2). An **admissible safe triple** is (A_1, A_2, A_3) with A_k k-safe and
T(A) := Σ_k t_kψ_k(A_k) < m_t.

**Theorem K1.2 (PROVED).** If C ∈ C_L and an admissible safe triple satisfy C ⪯_k A_k for k = 1, 2, 3, then (H_U) is
contradicted.

*Proof.* Each comparison is relevant (C ∈ C_L, A_k regular) and base by K1.0, so ψ_k(C) ≤ ψ_k(A_k) by (b), all
finite since ρ_k ∈ L¹. Hence T(C) ≤ T(A) < m_t. But C is coherent, so T(C) ≥ m_t by (F2). ∎

*Comparison with H1.0(c).* H1.0(c) is the case A_1 = A_2 = A_3 = X with Φ_t(X) < d_t. There each world must be
tested against the same model, so a dominator that copies X only down to some depth leaves the later worlds
unprotected (J1 §4.2). K1.2 lets each world have its own test, the A_k need not resemble B_t, and protection is
applied end by end with no uniform depth.

**The canonical triple.** For a depth assignment a on all ends of all worlds, with a_S ≥ n_S, put
Π^k(a) := ⋃_{S∈𝒮_k} S_{a_S}, D(a) := ⋃_k Π^k(a), and let A^a_k be B_t off D(a), correct at world k on Π^k(a), and
wrong at world k on D(a) ∖ Π^k(a). A^a_k is regular (D(a) ⊆ M and B_t ⊇ N₊ a.e.), k-safe, and
ψ_k(A^a_k) ≤ ψ_k(B_t) + ρ_k(D(a)). So T(A^a) ≤ T(B_t) + ∫_{D(a)} Σρ, and the triple is admissible as soon as
∫_{D(a)} Σ_kρ_k < d_t, which holds for all large summable assignments (absolute continuity). A^a_k is the
**k-worst** k-safe model at depths a that agrees with B_t off D(a): any such model Y satisfies Y ⪯_k A^a_k by (G).

**Corollary K1.3 (KKM form; PROVED).** If some regular X satisfies X ⪯_k A_k for every k for an admissible safe
triple, (H_U) is contradicted. In particular there is no cover in (EP∞) if, at some admissible depth assignment a,
the deep ends of different worlds never conflict: μ(Π^i(a) ∩ Π^j(a) ∩ R_ij) = 0 for all i ≠ j.

*Proof.* Theorem kkm gives a selected undominated C_p with C_p ⪯_k X ⪯_k A_k for all k; apply K1.2. For the second
statement let X be B_t off D(a), and on D(a) correct at every world k with g ∈ Π^k(a). This is consistent, since two
such worlds have the same sign a.e. on the overlap. Then X ⪯_k A^a_k by (G). ∎

This is H1.3 (second version) with countable families and with "at some depth" in place of "at every depth". It is
the case "Γ has no arrow at depth a".

## 4. Countable families: acyclic digraph and aligned orders

**Theorem K1.4 (J1.1 / Prop. R.1 for countable families; PROVED).** Assume (EP∞), with the families refined by H2.0.
Let Γ have an arrow i → l iff some T1-wrong W ∈ 𝒮_i and T1-correct S ∈ 𝒮_l have μ(W_m ∩ S_m) > 0 for every m. If Γ
has no directed cycle, (H_U) is contradicted.

*Proof.* Take an assignment a with a_S ≥ n_S and ∫_{D(a)} Σρ < d_t. Let X := T1 on D(a) and B_t off D(a). Then X is
regular, Φ_t(X) ≤ ∫_{D(a)} |t·c| ≤ ∫_{D(a)} Σρ < d_t, and all costs are finite. Theorem kkm gives a selected C with
C ⪯_k X for all k, all relevant. Put δ_k := 1_{E_kX} − 1_{E_kC}.
1. At a T1-correct end S of world k, X = T1 is k-correct on S_{a_S}, so δ_k ≤ 0 there, and δ_k is not S-positive.
2. *Step of the walk.* Suppose δ_i is not eventually 0 on some end of i. Either it is not eventually ≥ 0 on some end,
   and then end-protection makes it positive on some end; or it is ≥ 0 eventually on all ends and not eventually 0
   on some end E, and then it is E-positive. By 1 the positive end is a T1-wrong W ∈ 𝒮_i. Let P := {δ_i = 1} ∩ W_{n_W}.
   P meets every W_m, and on P, C is i-correct and X i-wrong, so C and X give different advice.
3. By K1.1′ there are l ∈ V(W) and a T1-correct S ∈ 𝒮_l with μ(P ∩ W_m ∩ S_n) > 0 for all m, n. In particular
   i → l. On P ∩ S_n with n ≥ a_S, X = T1 is l-correct and C gives the other advice, so δ_l = −1. So δ_l is not
   eventually ≥ 0 on S, and by step 2 applied to l, δ_l is positive on a T1-wrong end of l.
4. Iterating, every world reached has a non-base comparison and an outgoing arrow, so the walk never stops. In a
   3-vertex digraph an infinite walk contains a directed cycle. If Γ is acyclic, no δ_k can fail to be eventually 0
   on any end. Then all three comparisons are base and endorsed, which contradicts H1.0(c). ∎

*Uses:* K1.1 (countable shadowing), K1.1′, H2.0, H1.0, (F1). *Not used:* finiteness of the families, heaviness.

**Switched models with countable families.** Fix an order (k₁, k₂, k₃) and an assignment a as above. For
g ∈ D(a) let r(g) := min{r : g ∈ Π^{k_r}(a)}. The switched model X^a is B_t off D(a) and, at g ∈ D(a), gives the
advice correct at k_{r(g)}. Its conflict sets are Ξ^s := {g ∈ D(a) : r(g) < s, σ_{k_{r(g)}}(g) ≠ σ_{k_s}(g)}, for
s = 2, 3.

**(Al∞) at a.** For s = 2, 3 and every assignment M on ⋃_{q<s} 𝒮_{k_q}, there is an assignment J ≥ a on 𝒮_{k_s}
with (⋃_{S′∈𝒮_{k_s}} S′_{J_{S′}}) ∩ Ξ^s ⊆ ⋃_{q<s} ⋃_{S∈𝒮_{k_q}} S_{M_S} (mod null). The order is **aligned** if for
every assignment a₀ there is a ≥ a₀ at which (Al∞) holds.

For finite families and a_S = m for all S, this is J1's (Al) at m.

**Theorem K1.5 (J1.2 for countable families; PROVED).** Assume (EP∞). If some order of the worlds is aligned,
(H_U) is contradicted.

*Proof.* Choose a with (Al∞) and ∫_{D(a)}Σρ < d_t. X := X^a is near-Bayes as in K1.4. Let C be its kkm dominator.
1. X is k₁-correct on Π^{k₁}(a). By K1.0′, C ⪯_{k₁} X is base, and C = X on S_{m′_S} for all S ∈ 𝒮_{k₁}.
2. Apply (Al∞) with s = 2 and M := m′ to get J. Let g ∈ S′_{J_{S′}} ⊆ Π^{k₂}(a), so r(g) ≤ 2.
   - If X is k₂-correct at g, then δ_{k₂}(g) ≤ 0.
   - Otherwise g ∈ Ξ², so g ∈ S_{m′_S} for some S ∈ 𝒮_{k₁}. There C = X, so δ_{k₂}(g) = 0.

   So δ_{k₂} ≤ 0 on every S′_{J_{S′}}. By K1.0′ the comparison is base and C = X on S′_{m′_{S′}}.
3. The same with s = 3 and M := m′ on 𝒮_{k₁} ∪ 𝒮_{k₂}.

All three comparisons are base, so all are endorsed, which contradicts H1.0(c). ∎

**Sufficient condition (PROVED).** Let S′ ∈ 𝒮_{k_s} be T1-wrong, with every world of V(S′) that has ends placed
before k_s. Then by K1.1, for every M there is j with S′_j ⊆ ⋃_{q<s} ⋃ S_{M_S}, which is (Al∞) for the pieces of
Ξ^s inside S′. If every later end on a conflicting orthant is of this kind, or meets the earlier deep ends only in a null set at
some depth (end by end), the order is aligned. J1.3(a) and (b) follow for countable families with their hypotheses
read end by end; J1.3(c) follows when its alignment hypothesis is read with assignments in place of depths.

## 5. The equivalent question

Call p ∈ Δ **anti-safe** for an admissible safe triple A if C_p ⋠_k A_k for every k ∈ supp p.

**Theorem K1.6 (PROVED).** Assume (EP∞).

**(a) A cover forces anti-safe points.** For every tuple ρ of integrable base endorsers, every t ∈ I_ψ and every
admissible safe triple A, the selection has an anti-safe point.

*Proof.* F_k := {p ∈ Δ : C_p ⪯_k A_k} is closed by (S) (closed sections for the fixed model A_k). If no point
were anti-safe, every p would lie in F_k for some k ∈ supp p. Then Δ_S ⊆ ⋃_{k∈S} F_k for every face Δ_S, and the
KKM lemma gives p* ∈ F_1 ∩ F_2 ∩ F_3. C_{p*} ∈ C_L, so Theorem K1.2 is contradicted. ∎

**(b) Shape of anti-safe points.** Let p be anti-safe for the canonical triple A^a (admissible a). Then:
1. |supp p| ≥ 2. (At a vertex, C_{e_k} is competitive on {k}, so C_{e_k} ⪯_k A^a_k.)
2. For every regular X that agrees with B_t off D(a), the worlds k ∈ supp p with C_p ⪯_k X (at least one, by
   competitiveness) are all worlds at which X errs on a non-null part of Π^k(a). (If X is k-correct on Π^k(a), then
   X ⪯_k A^a_k by (G), and C_p ⪯_k A^a_k.)
3. supp p contains i ≠ j with μ(Π^i(a) ∩ Π^j(a) ∩ R_ij) > 0. (Otherwise the X of K1.3, built from the worlds of
   supp p only, is correct on Π^k(a) at every k ∈ supp p, against 2.)
4. If supp p = {i, j}, then C_p ⪯_j Y for every i-safe Y at depths a that agrees with B_t off D(a), and C_p ⪯_i Y
   for every such j-safe Y; and C_p ⋠_i Y, C_p ⋠_j Y′ for every such i-safe Y and j-safe Y′. (By 2, and because
   such a Y satisfies Y ⪯_i A^a_i.)

**(c) Conversely, one non-anti-safe triple is a contradiction.** If, for one ρ, one t ∈ I_ψ and one admissible safe
triple, no point of Δ is anti-safe, there is no cover. (This is (a) read backwards.)

**Question K1.Q.** Is there a ranking on M_U satisfying (H_U), in the class (EP∞), such that for every integrable
base-endorser tuple ρ, every t ∈ I_ψ and every admissible safe triple A, its selection p ↦ C_p has an anti-safe
point for A?

**Equivalence (PROVED).** A cover of T1 in the class (EP∞) exists if and only if K1.Q has a positive answer.
- ⇒ is Theorem K1.6(a).
- ⇐ holds because a ranking as in K1.Q is a ranking with (H_U) in the class, i.e. a cover in the class.

*What the equivalence says, and what it does not.* The ⇐ direction is formal. The content is (a)–(c). Every exclusion of rounds 17–19 produces one selected model whose three
comparisons are base: K1.3 does it with safe tests (a point that is not anti-safe), and H2.3, R.1, J1.1, J1.2,
K1.4, K1.5 with a single near-Bayes test whose base character is derived afterwards.
K1.Q isolates the one property a cover must have, and it is a property of the **selection** against **fixed** tests,
with no dominator and no copy depth in it. A ranking for K1.Q has to make, at selection indices with two conflicting
worlds in their support, each world lose to its own safe test while winning against the other world's. Every
configuration excluded so far (acyclic Γ; aligned orders; conflict-free depths) is excluded because one of these
losses is forced to be a win.

For the doubly misaligned 2-cycle of J1.Q (worlds i ⇄ j, world l without ends), K1.6(b) says this. At an anti-safe p
with supp p = {i, j}:
- C_p must beat at world j every model that is correct at i deep in i's ends, including the cap W around r̂;
- C_p must beat at world i every model that is correct at j deep in j's ends, including the tube S around γ;
- C_p must lose at i to every such i-safe model, and at j to every such j-safe model.

By (b)4 these comparisons are relevant. Each is either positive at an end of the winning world or a base comparison,
and the base ones are ρ-endorsed. The shell exchanges of J1.5 are the dominator-level shadow of this: in J1.5 the
dominator of the i-safe switched model wins at j by a positive comparison on a shell of S.

## 6. Why the per-world tool stops at K1.Q (what was tried)

1. **Covering through one model.** KKM needs, at each p, a world k ∈ supp p with C_p ⪯_k A_k. Competitiveness
   supplies this only through a single model X with X ⪯_k A_k at every k ∈ supp p. Through (G) that requires X to be
   correct deep in the ends of every world of supp p, which fails exactly on the conflict set
   Π^i(a) ∩ Π^j(a) ∩ R_ij (K1.6(b)3). It is non-null at every depth whenever Γ has an arrow. The per-world freedom
   removes the copy-depth problem of J1 §4.2. It does not remove the conflict set.
2. **Monotone iteration with closed sections (PROVED, not sufficient).** Let X_r be i-safe switched models whose
   i-correct part Z_r on the conflict set decreases, Z_{r+1} := Z_r minus the shell where the dominator C_{p_r} is
   j-correct, and let p_r → p*. Then X_r ⪯_i X_∞ and X_r ⪯_j X_s for r ≥ s, by (G). Closed sections give
   C_{p*} ⪯_i X_∞ and, if σ_l = σ_i on the conflict orthant, C_{p*} ⪯_l X_∞; at world j they give only
   C_{p*} ⪯_j X_s for each finite s. The two worlds pull the limit in opposite directions, so one of them always
   keeps a shell. A Zorn version fails at the same point: decreasing chains have lower bounds at i and not at j.
3. **Fixed point.** By (IB), the fixed point "C ⪯_k [C on D, B_t off D] for every k" is "C_p ∖ D ⪯_k B_t ∖ D in the
   ranking frozen on D". It would give K1.2 at once with A_k := [C_p on D, B_t off D]. Its KKM sets
   {p : C_p ⪯_k [C_p on D, B_t off D]} have a second argument that moves with p, and (S) says nothing about their
   closedness. Finite nets of the parts on D do not help, because an approximation error of small measure can still
   meet every depth of an end.
4. **Counting.** Every anti-safe comparison that is base costs at least a fixed amount of ρ-mass at its world, but
   the sources of different t may overlap. I found no use of the countable chain condition.

No construction was attempted beyond these tests. A ranking for K1.Q would need, by K1.6(b)4, a world j that ranks
selected models with i-supported indices above all i-safe models and below all j-safe ones, with closed sections in
p and with T1 competitive. I did not decide whether this is possible, and I state no conjecture.

## 7. Dependencies and scope

- **Inputs.** Theorem kkm and the KKM lemma; Theorem M0closed(a); Lemmas H1.0(a),(b) and H1.1 (refereed, H12); H2.0,
  H2.1 (refereed, H12), re-proved here in countable form as K1.1; Lyapunov (inside H1.1).
- **J1 (unrefereed).** Only its definitions and the statements of J1.0–J1.2 are used. They are re-proved here in
  countable form (K1.0′, K1.4, K1.5); J1.0's proof is checked; J1.2's proof is checked step by step in K1.5.
- **Not used.** Heaviness (h), (h′); E1.3, E1.4; (Nest_e); any edge result; finiteness of the families.
- **Outside the class.** Purely finitely additive endorsers; base endorsers that are not integrable (H12 case (D));
  protection not given by ends.
- **No NUMERICS.** `k1py/` is empty.
