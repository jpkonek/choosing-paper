# GG2 (round 35, BRIEF27). The non-Archimedean intersection theorem: what transfers, what is excluded, and the one statement that remains

18 Oct 2026. Rules of BRIEF13 and BRIEF27. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: a reading of recorded results, not a re-derivation.
- **CONJECTURE**.
- **NUMERICS**: `gg2py/` (run `python3 -I vb_lex_check.py` inside it; output in `vb_lex_check.out`). Nothing below rests on it.

No assumption is added. Every extra hypothesis below is a hypothesis of a stated result, and is said to be one.

Notation follows the write-up ("The Contamination Triangle", §2): Ω = {1,2,3}, T = T1 = (1−ε)u + εΔ, D_K, P_K, the U-domain M_U with U = D_{K'}, M (mixed problems of U), N_+ (nonnegative problems of U), world-k error sets E_k(X), advice ranges A(g), (LF), (S) with closed sections for every model, C_L, KKM (write-up Thm kkm). "Δ°" is the relative interior of Δ.

---

## 0. Outcome

**The non-Archimedean intersection theorem is not proved in full. It is proved for two large subclasses, and the rest is reduced to one sharp statement about a single world under closed choice.** The reduction comes with a proof that the transfer route itself cannot close the gap: the transfer argument goes through in lexicographic form, step by step, up to its last step, and the last step (theorem gm) has no lexicographic analogue, because the VB rankings are a lexicographic realisation of T1.

What is proved:

1. **Theorem A (the Archimedean part transfers; PROVED, at the status of Q4.2).** Every NA-credal world has no finite obstruction ((NC) on its ladder, no (M1) certificate). The leading part of every member endorses every comparison of the world. Hence:
   - a world with one Archimedean member (for instance one real-valued member) adds up;
   - **the real intersection theorem holds on every (LF) decomposable domain with bounded-charge penalties too**, not only integral ones (this removes the restriction stated at the end of INTERSECTIONS_additive.md);
   - in every NA-credal cover some world has a non-null set on which the leading part of **every** member has zero countably additive density;
   - on M_U, **no NA-credal cover exists in which every world's members share one leading layer**. This includes every cover by totally preordered additive worlds with values in an arbitrary ordered abelian group (hyperreals, Hahn series, ℝ^n lexicographic).
2. **Theorem B (non-Archimedean structure at the ends is excluded; PROVED modulo the import chain of FF2 Thm 4.1 and Q4.2).** On every decomposable domain with (LF), no ranking with (LA), (S) and T1 ∈ C_L has every world contained in a lexicographic order "(end level, body)". Here the end level is any group-valued function that ignores changes inside some exhausting family of sets, the bodies are integrable strictly guiding additive penalties, and the three end levels have a joint optimum. (IB), (C) and strict (G) of the ranking are not used.
   - **Corollary B.1 answers FF2's open point for its own class.** No closure A ⊆ P of FF2's end-priority invariant, under **any** selection with closed sections (continuity in measure not assumed), satisfies (LA), (S) with T1 selected.
3. **Theorem C and Proposition C.2 (the transfer route cannot finish; PROVED; NUMERICS sanity check).** For members with finitely many countably additive layers:
   - Steps 3–6 of the 7-step proof survive in lexicographic form: some coherent model is lexicographically Bayes at every non-Archimedean weight, and T1 is lexicographically Bayes at some non-Archimedean weight;
   - but the VB field satisfies both conclusions. So no argument that uses only these conclusions can exclude NA-credal covers;
   - Step 2 fails exactly on the null sets of the leading parts (Lemma C.3), and nowhere else.
4. **Theorem D (closed choice beats finite intersections in two worlds; PROVED, input P4B Lemma N0).** Take two worlds, a nested selection, and a partner world that adds up. If world 1 is NA-credal with countably additive leading parts, world 1 adds up unless its members' blind sets are initial segments of the chain whose lengths reach the end of the chain ("end concentration"). In particular, world 1 adds up if it has finitely many members. End concentration is exactly the mechanism of Theorem D21's world.

**The residual (§6, Question Q_GG2).** On M_U with three worlds, take a ranking with strict (G), (IB) and (S). Must every NA-credal world add up?
- **Yes** proves the non-Archimedean intersection theorem on M_U (Theorem A(d) with Q4.2 / M0closed(b)).
- **No** is necessary for an NA-credal cover. By Theorems A, B and D, a counterexample world has members whose leading parts are jointly blind in the bulk, is not end-led, and is end-concentrated on every nested edge where its partner sees.

**Single most important open point: Question Q_GG2.** In words: does Theorem S21 ("a leading charge is all-or-nothing under closed choice") survive when the leading charge is replaced by a family of leading parts, one per member? Theorem D says yes in two worlds, except under end concentration. In three worlds the end-concentrated case is open.

| # | Statement | Label |
|---|---|---|
| 1.1–1.2 | ladder charge and leading part of a member (any ordered abelian group) | PROVED |
| A(a)–(c) | no finite obstruction; leading parts endorse; Archimedean member ⇒ adds up | PROVED |
| A(d), Cor A.1 | jointly blind leading parts in every NA-credal cover; real intersection theorem with charges | PROVED at Q4.2's status (M0closed(b) on M_U) |
| A(e), Cor A.2 | M_U: common leading layer ⇒ adds up; no cover by common-leading-layer worlds | PROVED (S21, two readers; M0closed(b)) |
| B | end-led envelopes with a joint end optimum are excluded, any (LF) domain | PROVED modulo D1, BB2 Thm 6.1 + Lemma 2.0, Q4.1, M3.7–M3.8 (each refereed once); on M_U modulo M0closed(a) (two readers) |
| B.1 | FF2's end-priority closures fail (S) for every selection | PROVED, same status |
| B.2 | NA-credal worlds with an end-led member (common end functional) | PROVED, same status |
| C(a),(b) | lexicographic fixed point; T1 lexicographically Bayes | PROVED |
| C.2 | VB's field is a lexicographic realisation of T1 | PROVED; NUMERICS `vb_lex_check.py` (60 000 pairs, 0 violations) |
| C.3 | exact failure of Step 2 | PROVED |
| C.4 | VB′ as the standard restriction of an internal additive system | CHECKED (from L3.3(a), L3.2) |
| D | two worlds: finite or non-end-concentrated NA-credal worlds add up | PROVED (P4B Lemma N0 imported) |
| D.1 | three-world edge version | CHECKED |
| Q_GG2 | S21 for families of leading parts, three worlds | open |

---

## 1. Setting

### 1.1 Members, ladders and ladder charges

Fix a decomposable domain 𝓜 with advice ranges A(g). For a.e. pair g ∈ H the advices in A(g) have distinct world-k ranks r_k(g, a) ∈ {0, …, |A(g)| − 1} (rank 0 is best at world k). The world-k **ladder** is Ld_k := {(g, j) : g ∈ H, 1 ≤ j ≤ |A(g)| − 1}, with μ ⊗ counting measure. The **ladder profile** of a model X is λ_k(X)(g, j) := 1[r_k(g, a_X(g)) ≥ j]. On M_U, Ld_k is (a copy of) U: one step per pair meeting U. The profile is the error indicator 1_{E_k(X)}.

A **member** of world k (BRIEF27) is a map L from evaluable models to an ordered abelian group G such that:
- L(Y) − L(X) depends only on the record rec(X, Y);
- every non-null pointwise world-k guidance improvement strictly lowers L.

World k is **NA-credal** if X ≼_k Y ⟺ L(X) ≤ L(Y) for every L ∈ Π_k, for a nonempty family Π_k of members.

**Lemma 1.1 (PROVED).** For each member L of world k there is a unique finitely additive set function ν_L on the measurable subsets of Ld_k, with values in G, such that:
- ν_L vanishes on null sets and ν_L(S) > 0 for every non-null S;
- extending ν_L additively to integer-valued simple functions, L(Y) − L(X) = ν_L(λ_k(Y)) − ν_L(λ_k(X)) for all evaluable X, Y.

*Proof.* For measurable S ⊆ Ld_k write S_j := {g : (g, j) ∈ S}. Choose evaluable models X_j and Y_j that agree off S_j, give the rank-(j−1) advice and the rank-j advice respectively on S_j, and agree elsewhere. They exist because 𝓜 is decomposable and S_j ⊆ {g : |A(g)| > j}. Put ν_L(S) := Σ_j (L(Y_j) − L(X_j)). The summand depends only on rec(X_j, Y_j), which is fixed by S_j and j. So ν_L is well defined. It is additive in disjoint pieces: realise the record on S ∪ S′ as a composite through an intermediate model, and use L(Z) − L(X) = (L(Z) − L(Y)) + (L(Y) − L(X)).
- If S_j is non-null, Y_j is a non-null guidance worsening of X_j, so L(Y_j) > L(X_j).
- For arbitrary X, Y, decompose rec(X, Y) pointwise into unit rank steps and realise them as a chain of models. The telescoping sum is ν_L(λ_k(Y)) − ν_L(λ_k(X)).
- Uniqueness: the representation determines ν_L on every set of the form S_j × {j}. ∎

### 1.2 Leading parts

**Lemma 1.2 (PROVED).** Let G be an ordered abelian group and a > 0 in G. Put:
- C(a) := {g : |g| ≤ na for some n ∈ ℕ};
- I(a) := {g : n|g| < a for every n ∈ ℕ}.

Both are convex subgroups. There is a unique order-preserving homomorphism θ_a : C(a) → ℝ with θ_a(a) = 1 and kernel I(a). Moreover, for g ∈ C(a), θ_a(g) > 0 implies g > 0, and g ≥ 0 implies θ_a(g) ≥ 0.

*Proof.* C(a)/I(a) is an Archimedean ordered group, and Hölder's theorem embeds it in ℝ, uniquely once [a] ↦ 1. If θ_a(g) > 0, then g ∉ I(a), and g is not negative; so g > 0. The second implication holds because θ_a is order-preserving. ∎

For a member L of world k, the values ν_L(f) of integer simple functions f with |f| ≤ c·1 lie in C(a_L), where a_L := ν_L(Ld_k). The **leading part** of L is the real finitely additive charge π_L := θ_{a_L} ∘ ν_L. It satisfies:
- π_L ≥ 0, π_L(Ld_k) = 1, and π_L vanishes on null sets;
- **(L1)** π_L(f) > π_L(f′) ⇒ ν_L(f) > ν_L(f′);
- **(L2)** ν_L(f) ≥ ν_L(f′) ⇒ π_L(f) ≥ π_L(f′).

On M_U, with A, B ⊆ M, the **M-leading part** is defined in the same way with a_L := ν_L(M).

By Yosida–Hewitt, π_L = ρ_L μ + π_L^p, where ρ_L ∈ L¹ and π_L^p is purely finitely additive. L is **Archimedean** if π_L(S) > 0 for every non-null S, equivalently if no non-null S has ν_L(S) ∈ I(a_L). Every real-valued member is Archimedean, by strict guidance.

The layers of L are the coefficients of ν_L in a Hahn embedding of G. Only the leading layer π_L is used in §§2–3, and no Hahn embedding is needed for it.

### 1.3 Two subclasses of members

- **FCA member** ("finitely many countably additive layers"): L(X) = ∫ ℓ(g, a_X(g)) dμ(g) ∈ ℝ^m, ordered lexicographically. The penalty ℓ is measurable with an integrable envelope, and ℓ(g, ·) is lexicographically strictly increasing in world-k rank on A(g), for a.e. g.
  - Such an L is a member: the integral of an a.e. lexicographically positive vector function over a non-null set is lexicographically positive. To see this, take the first coordinate that is not a.e. zero on the set; the earlier coordinates vanish a.e. there, so this one is ≥ 0 a.e. and not a.e. zero.
  - Its leading part is the normalised first layer.
  - The VB members (Φ_i, Ψ_i) are FCA.
- **End-local functions.** Fix an increasing sequence of symmetric measurable sets H_n (H_n = −H_n) with ⋃_n H_n co-null. A function E on evaluable models is **end-local** if E(X) = E(Y) whenever X = Y a.e. off some H_n. An example is the end level E_i of FF2 §2.1, with H_n as there.

---

## 2. The Archimedean part transfers

**Theorem A (PROVED).** Let world k be NA-credal with family Π_k.

(a) Let B_j ≼_k X_j (j = 1, …, J) be accepted comparisons and λ_j ≥ 0, with f := Σ_j λ_j (λ_k(X_j) − λ_k(B_j)) ≤ 0 a.e. on Ld_k. Then f = 0 a.e. In particular world k satisfies (NC) on its ladder and carries no (M1) certificate.

(b) For every L ∈ Π_k and all evaluable X, Y: X ≼_k Y implies π_L(λ_k(X)) ≤ π_L(λ_k(Y)). So every leading part is a bounded endorser of every comparison of world k.

(c) Suppose the sets {ρ_L > 0}, L ∈ Π_k, have co-null essential union in Ld_k. Then world k adds up: some bounded endorser of all its comparisons has countably additive density > 0 a.e. on Ld_k. This holds in particular if some member is Archimedean.

(d) Let 𝓜 have (LF) at D_T1, and let a ranking on 𝓜 satisfy strict (G), (IB), (LA), (S), (C), with T1 ∈ C_L and every world NA-credal. Then some world k has a non-null ladder blind set Λ_k, and ρ_L = 0 a.e. on Λ_k for every L ∈ Π_k.

(e) If in (d) 𝓜 = M_U, then no member of that world has an M-leading part that is a leading charge of the world on M. In particular the M-leading parts of its members are not all proportional, and Π_k is not a singleton.

*Proof.*

(a) The functions λ_k(X_j) − λ_k(B_j) take values in {−1, 0, 1} and are constant on the atoms of the finite algebra generated by their supports. Discard the null atoms. The set of λ ∈ ℝ^J_{≥0} with Σ_j λ_j(·) ≤ 0 on every remaining atom is a polyhedral cone with integer data. Suppose f is not a.e. zero. Then f < 0 on some non-null atom c. The λ in the cone with value < 0 on c form a nonempty relatively open subset of the cone, so it contains a rational point. Clearing denominators gives integers n_j ≥ 0 with F := Σ_j n_j(λ_k(X_j) − λ_k(B_j)) ≤ 0 everywhere and F ≤ −1 on c.

Fix L ∈ Π_k. Each comparison is accepted by L, so ν_L(λ_k(X_j)) − ν_L(λ_k(B_j)) ≥ 0 by Lemma 1.1, and hence ν_L(F) ≥ 0. On the other hand, ν_L is monotone on integer simple functions (a nonnegative one is a sum of indicators). So ν_L(F) ≤ ν_L(−1_c) < 0, a contradiction. Taking f ≤ −1 gives (NC). Taking f ≤ 0, not a.e. zero, gives no certificate.

(b) X ≼_k Y gives L(X) ≤ L(Y), that is ν_L(λ_k(Y)) − ν_L(λ_k(X)) ≥ 0, and (L2) gives the claim.

(c) ("Adds up" is meant on M_U in the sense of Definition addup, and elsewhere in the ladder sense of Lemma M30(c).) The essential union is attained along a countable subfamily L_1, L_2, …. Put ν := Σ_m 2^{−m} π_{L_m}. It is a bounded charge, vanishes on null sets, and endorses every comparison of world k by (b). Its countably additive density is Σ_m 2^{−m} ρ_{L_m}, which is > 0 a.e. (The purely finitely additive parts stay purely finitely additive, by the criterion in the proof of Thm K31(b).) On M_U, ν restricted to M plus μ|_{N_+} is a weight as in Definition addup(b). On a general domain, ν is a ladder endorser with a.e. positive density, so the ladder blind set of world k is null (Lemma M30(c)). If L is Archimedean, then π_L is positive on non-null sets, so ρ_L > 0 a.e. (N19 Lemma R1: remove a small carrier of π_L^p from {ρ_L = 0}), and (c) applies with the family {L}.

(d) By (a), (NC) holds at every world. By Q4.2 (BB2/CC3; PROVED at its listed status), every endorser tuple has a degenerate ladder field, so some world k has a non-null canonical blind set Λ_k (Thm K31(c) on the ladder, Lemma M30(c)). Every π_L, L ∈ Π_k, is an endorser by (b), so ρ_L = 0 a.e. on Λ_k by the defining property of Λ_k. On M_U, Thm M0closed(b) or Cor L42 may replace Q4.2.

(e) Suppose the M-leading part π of some member is a leading charge of world k on M. Then Thm S21 (strict (G), (IB), (S); two readers) makes π positive on non-null subsets of M, with ca density > 0 a.e. on M. So world k adds up, and Λ_k is null, which contradicts the choice of k.

If all members' M-leading parts equal one charge π, then π is a leading charge of the world:
- if π(B∖A) > π(A∖B), then ν_L(B∖A) > ν_L(A∖B) for every L by (L1), so A ≤_L B for every L, hence A ≼_k B;
- if A ≼_k B, then A ≤_L B, and (L2) gives π(B∖A) ≥ π(A∖B).

A singleton family is a special case. ∎

**Corollary A.1 (PROVED, at the status of Q4.2).** Let 𝓜 be decomposable with (LF) at D_T1. No ranking with strict (G), (IB), (LA), (S), (C) covers T1 if every world k is contained in the order of some real-valued strictly guiding member (X ≼_k Y ⇒ L_k(X) ≤ L_k(Y)). In particular this holds for intersections of additive rankings whose penalties are bounded charges vanishing on null sets, with no integrability and no countable dense subfamily.

*Proof.* A real member's ν_L is bounded and positive on non-null ladder sets. Normalised, it endorses world k, and by N19 Lemma R1 its density is > 0 a.e. So world k adds up, and every world adds up. (NC) holds because a strictly positive endorser exists (Thm K31(a)). Q4.2's last clause, or Thm M0closed(b) on M_U, excludes the cover. ∎

*Remark.* INTERSECTIONS_additive.md states that its 7-step argument "does NOT cover families with purely finitely additive parts". The route above does cover them, and the 7-step argument is then not needed for real intersections. Its content for the non-Archimedean question is the list of places where real values were used, and §4 settles each of those.

**Corollary A.2 (PROVED; Thm S21 two readers, Thm M0closed(b)).** On M_U there is no cover of T1 by a ranking with strict (G), (IB), (LA), (S), (C) in which every world is NA-credal with a common M-leading layer. In particular there is none in which every world is a total preorder given by one member with values in an arbitrary ordered abelian group.

This extends Thm Q36(b) (countably many charge levels) to arbitrary value groups and to intersections with a common leading layer.

---

## 3. Non-Archimedean structure at the ends is excluded

**Theorem B (PROVED, modulo the imports in Step 5).** Let 𝓜 be a decomposable domain with (LF) at D_T1. Let a ranking on 𝓜 satisfy (LA) and (S) (closed sections for every model, competitiveness on supp p), with T1 ∈ C_L. Suppose there are:
- an increasing sequence of symmetric measurable sets H_n with co-null union;
- for each world k, an end-local function E_k from evaluable models to an ordered abelian group G_k;
- for each world k, a measurable penalty b_k(g, a), strictly increasing in world-k rank on A(g) for a.e. g, with an integrable envelope; write B_k(X) := ∫ b_k(g, a_X(g)) dμ;

such that:
- **(i)** X ≼_k Y implies (E_k(X), B_k(X)) ≤_lex (E_k(Y), B_k(Y)), for every world k;
- **(ii) joint end optimum:** for some ordered abelian group G and order embeddings ι_k : G_k → G, some evaluable Y minimises X ↦ Σ_k ι_k(E_k(X)) over 𝓜.

These assumptions are inconsistent. (IB), (C), transitivity beyond the preorder property, and strict (G) of the ranking are not used.

*Proof.* Write b := (b_1, b_2, b_3) and t·B := Σ_k t_k B_k for t ∈ Δ.

**Step 1 ((γ₀) for b: at every t ∈ Δ, some coherent evaluable model is pointwise t-Bayes for b).**
- Fix t. Let B_t be a measurable pointwise minimiser of t·b(g, ·) over A(g); it is evaluable. Let Y be as in (ii), and let X_n be B_t on H_n and Y off H_n (a splice along a symmetric set, so evaluable).
- E_k(X_n) = E_k(Y) for every k, by end-locality.
- KKM gives C ∈ C_L with C ≼_k X_n at every world. By (i), E_k(C) ≤ E_k(X_n) for every k.
- By (ii), Σ_k ι_k(E_k(C)) ≥ Σ_k ι_k(E_k(Y)) = Σ_k ι_k(E_k(X_n)). In an ordered group, a ≤ a′, b ≤ b′, c ≤ c′ with one inequality strict gives a + b + c < a′ + b′ + c′. Hence E_k(C) = E_k(X_n) for every k.
- By (i) again, B_k(C) ≤ B_k(X_n) for every k, so t·B(C) ≤ t·B(X_n).
- Now t·B(X_n) − t·B(B_t) = ∫_{H_n^c} t·(b(g, a_Y) − b(g, a_{B_t})) dμ ≤ 2∫_{H_n^c} env dμ → 0, by dominated convergence.
- So inf{t·B(C) : C coherent evaluable} = min t·B. The coherent evaluable models are compact in measure (limits in measure of coherent models are coherent, Lemma H10(a) and R1 Prop 3.1, and 𝓜 is closed under convergence in measure). t·B is continuous in measure, by absolute continuity of ∫ env. So the infimum is attained by a coherent C*.
- t·B(C*) = min t·B forces C* to be pointwise t-Bayes a.e.

**Step 2 (T1 is weakly Bayes for b at some w ∈ Δ).**
- By KKM, T1 is tied at every world with some selected C_p. C_p is competitive on S := supp p, so by transitivity T1 is competitive on S.
- Fix n. For X equal to T1 a.e. off H_n, E_k(X) = E_k(T1) for every k. Some k ∈ S has T1 ≼_k X, and (i) gives B_k(T1) ≤ B_k(X).
- So the set Z_n := {(B_k(X) − B_k(T1))_{k∈S} : X = T1 off H_n} misses the open negative orthant of ℝ^S. Z_n is convex by Lyapunov's theorem (integrals over H_n of measurable selections of integrable integrands), and it contains 0.
- Separation gives w_n ∈ Δ_S with w_n·z ≥ 0 on Z_n. Switching advice on a non-null subset of H_n then shows that T1's advice minimises w_n·b(g, ·) over A(g) for a.e. g ∈ H_n.
- A limit point w of (w_n) has the same property a.e. on each H_m (the advice sets are finite), hence a.e.

This is FF2 Thm 4.1 Step 1 with C_{q₀} = T1.

**Step 3 (w ∈ Δ°).**
- Put t₀ := 2c₀/(c₀ + ε). Then h₀ := (1, 1, −t₀) lies in relint F₃, since v₃·h₀ = 0 and v₁·h₀ = v₂·h₀ = εt₀ + ε > 0.
- For t slightly above t₀, h := (1, 1, −t) has P_T1(h) = v₃·h < 0 and P_T1(−h) = −v₁·h < 0. So T1 gives no advice on the pair of h.
- A small ball O around such an h lies in the (LF) neighbourhood N, where "accept h" is available.
- On O, accepting is good at worlds 1 and 2. Strict guidance of b gives b_k(g, +) < b_k(g, 0) for k = 1, 2.
- If w₃ = 0, then w·(b(g, +) − b(g, 0)) < 0 on O ∩ H_n, a non-null set for large n. This contradicts Step 2. (The vertices e₁ and e₂ are included in this case.)
- The cyclic symmetry of T1 gives w₁, w₂ > 0 in the same way.

**Step 4 ((γ)).** For a.e. g and distinct a, a′ ∈ A(g), the vector b(g, a) − b(g, a′) has no zero coordinate (world ranks are distinct). If it is not proportional to 𝟙, its zero set in aff Δ is a line; if it is, its zero set is empty. By Tonelli, for a.e. q ∈ Δ° the q-Bayes model is a.e. unique. By Step 1 it is then coherent.

**Step 5 (contradiction).** b is a strictly guiding additive field with integral penalties and an integrable envelope. It has (γ₀) at every t ∈ Δ (Step 1) and (γ) (Step 4), and D_T1 is b-Bayes at w ∈ Δ° (Steps 2–3). Then:
- Thm D1 (refereed once) gives w ∉ E(b), so D_T1 is the a.e.-unique Bayes model at w;
- BB2 Thm 6.1 (= M3.9, with AUDIT_BB Lemma 2.0; refereed once, CC3) gives (C2) and (C3) at w;
- Q4.1 (refereed once) gives (Av);
- M3.8 with M3.7(d) (refereed once) gives a contradiction.

This is the chain of Q4.2 and of FF2 Thm 4.1 Step 6. Its standing data are properties of the field alone. On M_U, Thm M0closed(a) (strictly signed field, (γ), D_T1 Bayes at an interior weighting; two readers) gives the contradiction directly. ∎

*Relation to FF2 Thm 4.1.* FF2 uses competitiveness, continuity in measure of the selection, and endorsement of local comparisons out of selected models. Theorem B replaces continuity by closed sections, through KKM. It needs lexicographic endorsement (i) of all comparisons, plus the joint end optimum (ii), and it needs no condition on the selection beyond (S). The two results are complementary.

**Corollary B.1 (PROVED, same status).** On the full four-advice domain, let P be FF2's end-priority invariant (FF2 §2.1). Let A ⊆ P be any family of world relations that are preorders (for instance any closure in FF2's sense, with any generators (D), (K)). Then no selection makes A satisfy (LA) and (S), with closed sections for every model, while T1 ∈ C_L.

*Proof.*
- A ⊆ P gives (i), with E_i = FF2's end level and B_i = ∫F_i. E_i vanishes on records supported in FF2's H_n, which are symmetric. F_i is strictly guiding with envelope (2+λ)|h_i|.
- For (ii), take G = ℝ and ι_i = id. Then Σ_i E_i(X) = Σ_k Λ_k(Σ_i λ_i(·, a_X)) = Σ_k Λ_k(3u·F(·, a_X)/|·|). It is minimised by any pointwise minimiser of u·F, for instance T1 (FF2 Prop 2.3, step 2, with inputs (C2)–(C3) CHECKED there).
- (LF) is trivial on the full domain. ∎

*So FF2's single most important open point ("does Theorem 4.1 survive when the selection is not continuous in measure?") has a positive answer for FF2's class.* Every minimal-commitment closure under an end-priority invariant fails (S) for every selection, not only for the posterior family or for continuous selections.

**Corollary B.2 (PROVED, same status).** In Theorem A(d), suppose that for each world k there is a member L_k ∈ Π_k with values in G_k × ℝ, ordered lexicographically, of the form L_k(X) = (Λ(e_k(·, a_X(·))), ∫ b_k(g, a_X(g)) dμ). Here:
- Λ is one positive linear functional on bounded measurable functions, common to the three worlds, vanishing on every function supported in some H_n;
- e_k is bounded, measurable, and weakly increasing in world-k rank;
- b_k is as in Theorem B.

Then T1 is not covered. In words: no NA-credal cover in which each world has a member whose non-Archimedean part lives only at the ends, with a common end functional, and whose Archimedean body is integrable and strictly guiding.

*Proof.* Members contain their worlds, so (i) holds. For (ii), Σ_k E_k = Λ(Σ_k e_k(·, a_X)) is minimised by a pointwise minimiser of Σ_k e_k, which is evaluable. ∎

*What escapes Theorem B.*
- A world whose first locally visible layer (the first layer with nonzero countably additive part) is blind on a non-null set. This is non-Archimedean structure in the bulk; VB is the model case.
- End levels with no joint optimum.
- Bodies carrying purely finitely additive parts at the body scale. (Lemma L40's argument handles these when there is no end level. Combining the two needs the carriers of the end level and of the body's singular part to be compatible.)

---

## 4. Why the transfer proof cannot be completed: the bulk

### 4.1 The lexicographic fixed point

A **non-Archimedean (NA) weight** for FCA members L_1, L_2, L_3 (with m_k layers) is a finite sequence Φ = (φ_1, …, φ_s) of linear functionals on ℝ^N, N = m_1 + m_2 + m_3, which is **NA-positive**: Φ(z) ≥_lex 0 whenever z_k ≥_lex 0 for every k. (Here z = (z_1, z_2, z_3), z_k ∈ ℝ^{m_k}, and Φ(z) := (φ_a(z))_a.)

For standard data this is exactly the content of a weight with infinitesimal components in an ordered field such as ℝ((η)). For standard reals x, y and infinitesimal η > 0, x + ηy ≥ 0 iff (x, y) ≥_lex 0.

**Theorem C (PROVED).** Let a ranking on a decomposable domain satisfy (LA) and (S). Suppose each world k is contained in the order of an FCA member L_k (other members, if any, are arbitrary).

(a) For every NA-positive Φ, some C ∈ C_L is pointwise Φ-lexicographically Bayes: for a.e. g, its advice lexicographically minimises a ↦ Φ(ℓ(g, a)) over A(g), where ℓ := (ℓ_1, ℓ_2, ℓ_3).

(b) If T1 ∈ C_L, there is an NA-positive Φ* such that T1 is pointwise Φ*-lexicographically Bayes, with φ*_1(z) = Σ_k w_k z_{k,1} for some w ∈ Δ. That is, T1 is Bayes for the tuple of leading layers at w, with ties broken by the later stages.

*Proof.*

(a) Let B be a measurable pointwise lexicographic minimiser. For every evaluable X, Φ(L(X)) − Φ(L(B)) is the integral of an a.e. lexicographically nonnegative vector function, hence ≥_lex 0 (§1.3). KKM gives C ∈ C_L with C ≼_k B at every world, so L_k(C) ≤_lex L_k(B) for every k. By NA-positivity, Φ(L(C)) ≤_lex Φ(L(B)). So Φ(L(C)) = Φ(L(B)), and the integrand of the difference vanishes a.e.; that is, C is pointwise optimal.

(b) The set-up:
- As in Step 2 of Theorem B, T1 is competitive on some S ⊇ supp p with |S| ≥ 2. (|S| = 1 would make T1 world-k-best, against strict guidance of L_k.)
- Z := {L(X) − L(T1) : X evaluable} ⊆ ℝ^N is convex (Lyapunov) and contains 0.
- N^S := {z : z_k <_lex 0 for every k ∈ S} is a convex cone, and Z ∩ N^S = ∅.

The iteration: put Z_1 := Z and N_1 := N^S. While N_a ≠ ∅, take a properly separating functional φ_a (Rockafellar Thm 11.3; ri Z_a ∩ ri N_a ⊆ Z ∩ N^S = ∅), with φ_a ≥ 0 on Z_a and φ_a ≤ 0 on N_a. Then put Z_{a+1} := Z_a ∩ {φ_a = 0} and N_{a+1} := N_a ∩ {φ_a = 0}. Each step lowers dim aff(Z_a) + dim aff(N_a), so the iteration stops.
- *T1 is optimal.* For z ∈ Z: φ_1(z) ≥ 0; if it is 0, then z ∈ Z_2 and φ_2(z) ≥ 0; and so on. So Φ*(z) ≥_lex 0.
- *NA-positivity.* Let z have z_k ≥_lex 0 for all k, and φ_b(z) = 0 for b < a. Pick n₀ ∈ N_a. Then −z + δn₀ ∈ N_a for every δ > 0, because a lexicographically nonpositive vector plus a lexicographically negative one is lexicographically negative, and φ_b(−z + δn₀) = 0 for b < a. Letting δ → 0 gives φ_a(−z) ≤ 0.
- *First stage.* N^S leaves z_{k,r} (r ≥ 2) free when z_{k,1} < 0, and leaves every coordinate of k ∉ S free. So φ_1 ≤ 0 on N^S forces φ_1 = Σ_{k∈S} w_k z_{k,1} with w ≥ 0. Proper separation forces w ≠ 0.
- *Pointwise form.* As in (a). ∎

Theorem C is Theorem L41 one level down. It needs no Lemma L40, no countable dense mixture, and no Archimedean property of the value groups. **Steps 3–6 of the 7-step proof therefore survive in lexicographic form.**

### 4.2 The last step has no lexicographic analogue

**Proposition C.2 (PROVED; NUMERICS).** On M_U, take the members L_i = (Φ_i, Ψ_i), ordered lexicographically, with Φ_i(X) = ∫_{X ∩ {v_i·h<0}} |v_i·h| dμ and Ψ_i(X) = ∫_{E_i(X)} |h_i| dμ (these are the VB rankings). They are FCA, lexicographically strictly guiding, with integrable envelopes, and (LF) holds on M_U. Moreover:
1. for every NA-positive Φ, some coherent model is pointwise Φ-lexicographically Bayes;
2. D_T1 is pointwise Φ*-lexicographically Bayes for Φ* = (u·(veto layers), u·(Ψ layers)).

*Proof.* On g ∈ U, the cost of accepting minus the cost of silence is z(g) = (d_1(g), d_2(g)) with:
- d_{1,i}(g) = (v_i·g)^− ≥ 0, which is convex and positively homogeneous;
- d_{2,i}(g) = −g_i, which is linear.

*Stage functions are convex where they matter.* NA-positivity forces:
- φ_1 = Σ_i w_i d_{1,i} with w ≥ 0;
- φ_a, restricted to the stage-a tie set, to be a nonnegative combination of the coordinates current at stage a, plus arbitrary coefficients on consumed coordinates.

A consumed coordinate vanishes on every full-dimensional part of a later tie set:
- veto coordinates vanish on {Σ_{i∈supp w} w_i (v_i·g)^− = 0};
- if a stage puts positive weight β on a Ψ coordinate, its tie set {−Σ β_i g_i + Σ α_i (v_i·g)^− = 0} is null. On an open set where the signs of v_i·g are fixed, that function is linear, and it vanishes identically only if Σ β_i e_i = −Σ_{v_i·g<0} α_i v_i. Here the left side is ≥ 0 and the right side is < 0 componentwise unless both are zero.

So, up to null sets, the stage function f_a(g) := φ_a(z(g)) on the stage-a tie set T_{a−1} is a nonnegative combination of convex functions, and T_a is an intersection of T_{a−1} with half-spaces {v_i·g ≥ 0}.

*Convexity by induction from the last stage.* Let 𝒜_a be the set of g ∈ T_{a−1} with (f_a(g), f_{a+1}(g), …) ≤_lex 0 (ties accepted); 𝒜_{s+1} := T_s. Then 𝒜_a = (T_{a−1} ∩ {f_a < 0}) ∪ 𝒜_{a+1}, with 𝒜_{a+1} ⊆ T_a ⊆ T_{a−1} ∩ {f_a = 0}.
- For x with f_a(x) < 0 and y ∈ 𝒜_{a+1}: on the segment, f_a ≤ (1−τ)f_a(x) < 0 for τ < 1, and T_{a−1} is convex.
- Two points of T_{a−1} ∩ {f_a < 0}: their segment stays there, by convexity of f_a and of T_{a−1}.
- Two points of 𝒜_{a+1}: their segment stays there, by the induction hypothesis.

So 𝒜_1 is a convex cone in U (up to null sets).

*Coherence.* 𝒜_1 contains every g > 0 in U (all f_a ≤ 0 there). An open convex cone containing int ℝ³₊ and contained in U is D_K mod null, for K := {m ∈ Δ : m·g ≥ 0 on the cone}. 𝒜_1 is pointwise Φ-lexicographically Bayes (ties accepted).

*T1.* At Φ*, accept iff v_i·g ≥ 0 for all i and u·g > 0. Since u ∈ T1, this is D_T1 mod null. ∎

NUMERICS (`gg2py/vb_lex_check.py`, ε = 0.3, s = 0.5): over 300 random NA-positive weights (supports on the boundary included, arbitrary coefficients on consumed coordinates), 60 000 margin-filtered accepted pairs passed the midpoint-convexity test with 0 violations. At Φ*, the accepted set agreed with D_T1 on 4000 sampled gambles.

**Consequence (PROVED).** The conclusions of Theorem C (a coherent lexicographic Bayes model at every NA weight, T1 lexicographically Bayes at some NA weight), together with strict guidance, integrability and (LF), are satisfied by a lexicographic field. **So no argument that uses only the fixed point excludes NA-credal covers.** This is precisely why the 7-step transfer cannot be completed: its Step 7 invokes Theorem gm (no additive realisation of T1), and lexicographic realisations of T1 exist.

What excludes VB itself is closed choice at boundary priors (Thm L3.4, "vetoes cannot be paid"), and on M_U Thm S21. Both use that the world refines its leading level. An intersection world need not refine any one member's leading level, and that is the residual (§6).

### 4.3 Step 2, exactly

**Lemma C.3 (PROVED).** On M_U, let L be a member of world k whose M-leading part π_L admits infinitely many pairwise disjoint sets of positive measure. Then every bounded charge φ ≥ 0 that endorses ≤_L on subsets of M (A ≤_L B ⇒ φ(A) ≤ φ(B)) vanishes on every π_L-null set.

If instead π_L takes finitely many values, upper layers can be absorbed. For example, lex(ν⁺, λ) with a {0,1}-valued ν⁺ is endorsed by λ + λ(M)ν⁺ (P4B_referee §3).

*Proof.* Let π_L(A) = 0, and let D_1, D_2, … be disjoint with π_L(D_m) > 0. Put D′_m := D_m ∖ A, so π_L(D′_m) = π_L(D_m) > 0 = π_L(A). By (L1), ν_L(A) < ν_L(D′_m). Compare models with error sets A ∪ R and D′_m ∪ R (R disjoint): A ≤_L D′_m, so φ(A) ≤ φ(D′_m). The D′_m are disjoint and φ is bounded, so φ(D′_m) → 0 and φ(A) = 0. ∎

So the transfer's Step 2 (some real ψ registering every strict comparison) fails exactly on the null sets of the leading parts. For an intersection world it fails exactly on the joint blind set of Theorem A(d), and on no other set.

### 4.4 The internal–standard gap made precise

**Remark C.4 (CHECKED, from L3.3(a) and L3.2, both refereed once).** Fix a non-principal ultrafilter and an infinitesimal η = a/b. The internal gauge system of Prop L3.2 at stage (a, b):
- is an internal strictly guiding additive ranking satisfying every internal axiom;
- covers the internal target K_u(η), whose internal Hausdorff distance to *T1 is ≤ C(ε, K′)η;
- does not cover *T1 itself (by transfer of Thm gm).

Its restriction to standard models refines VB′ (L3.3(a)). The standard part map sends K_u(η) to T1, so T1 ∈ C_L in VB′. The standard version of (S) fails exactly at standard boundary priors (L3.3(c)).

So an NA cover would have to hide in two gaps at once:
- between "covers a target infinitesimally close to T1" and "covers T1";
- between "(S) at all internal indices" and "(S) at standard indices".

VB′ shows that the first gap alone is not enough.

### 4.5 The seven steps, one by one

| Step of INTERSECTIONS_additive.md | Non-Archimedean status |
|---|---|
| 1. countable dense mixture | not needed. Endorsers are generated by leading parts (Theorem A(b)), and countable mixtures of them are endorsers (Theorem A(c)) |
| 2. strictness transfers | **fails exactly on π_L-null sets** (Lemma C.3); for a world, exactly on its joint blind set |
| 3–4. interior Bayes models undominated, coherent, unique | survive lexicographically (Theorem C(a)); uniqueness holds off lexicographic ties |
| 5. Lyapunov plus separation | survives as iterated separation (Theorem C(b)). No completeness of the value field is needed, because standard models have standard values |
| 6. interior weight | the first stage may lie on ∂Δ (for instance configuration V gives w = e₁), and the other worlds then enter at infinitesimal order. So "T1 Bayes only at a weight with infinitesimal components" can occur |
| 7. ccibu, then gm | **no analogue**: VB is a lexicographic realisation of T1 (Proposition C.2) |

---

## 5. Closed choice against finite intersections: two worlds

**Setting for Theorem D.** Let n = 2 on M_U, and let a ranking satisfy strict (G), (IB), (LA), (S) and hypothesis (Nest): the world-1 error sets of the members of C_L form a chain. By P4B Lemma N0 (refereed):
- C_L is the selection;
- its world-1 error sets form a chain c_b, b ∈ [0,1], with μ(c_b) = bμ(M), continuous in measure;
- sections are closed in b;
- competitiveness reads (K): for every interior b and every world-1 error set A of a regular model, c_b ≤₁ A or d_b ≤₂ A^c, where d_b := M ∖ c_b.

**Theorem D (PROVED).** In this setting, assume:
- world 2 has a bounded endorser ν₂ = ρ₂μ + ν₂^p of its relevant comparisons with ρ₂ > 0 a.e. on M;
- world 1 is NA-credal, and every member L has a countably additive M-leading part π_L = ρ_L μ.

Put s_L := μ({ρ_L = 0})/μ(M). Then:

(a) {ρ_L = 0} = c_{s_L} mod null, for every L ∈ Π_1. Every member is blind exactly on an initial segment of the chain, and s_L < 1.

(b) If sup_L s_L < 1, world 1 adds up. In particular world 1 adds up whenever Π_1 is finite.

(c) Hence if world 1 does not add up, then inf_L s_L > 0 and sup_L s_L = 1: all members are blind on c_{inf s_L}, and their blind segments reach the end of the chain.

*Proof.*

(a) Fix L and an interior b, and suppose c_b ∩ {ρ_L > 0} and {ρ_L = 0} ∖ c_b are both non-null.
- Pick non-null Q ⊆ {ρ_L = 0} ∖ c_b. Then ν₂(Q) ≥ ∫_Q ρ₂ =: 2κ > 0.
- By the Yosida–Hewitt carrier property (Thm K31(b), Step 1), there is E with μ(E) arbitrarily small and ν₂^p(M ∖ E) < κ. Pick non-null P ⊆ (c_b ∩ {ρ_L > 0}) ∖ E with ∫_P ρ₂ < κ. Then ν₂(P) < 2κ ≤ ν₂(Q).
- Let A := (c_b ∖ P) ∪ Q, and let X_A be the regular model with world-1 error set A.
- *World 1.* π_L(Q) = 0 < π_L(P), so (L1) gives ν_L(A ∖ c_b) < ν_L(c_b ∖ A). So L strictly prefers X_A, and c_b ≰_1 A.
- *World 2.* If d_b ≤₂ A^c, the comparison C_b ≼₂ X_A is relevant, and ν₂ gives ν₂(M ∖ c_b) ≤ ν₂((M ∖ c_b ∖ Q) ∪ P), that is ν₂(Q) ≤ ν₂(P). That is false.
- So (K) fails at b. Hence, for every interior b, c_b ∩ {ρ_L > 0} is null or {ρ_L = 0} ⊆ c_b.

Now let b < s_L. The second alternative would give μ(c_b) ≥ s_L μ(M), so c_b ⊆ {ρ_L = 0}. Taking the union over b < s_L (the chain is continuous in measure) gives c_{s_L} ⊆ {ρ_L = 0}. The two sets have equal measure, so they are equal. And s_L < 1 because π_L(M) = 1.

(b) Put s₋ := inf_L s_L and s* := sup_L s_L < 1.
- *If s₋ = 0:* take L_m with s_{L_m} → 0. Then ν := Σ_m 2^{−m} π_{L_m} is an endorser (Theorem A(b), (c)) with density > 0 off ⋂_m c_{s_{L_m}}, a null set. So world 1 adds up.
- *If s₋ > 0:* N′ := c_{s₋} is non-null and π_L(N′) = 0 for every L, by (a).
  - Take b ∈ (s*, 1) and A := c_b ∖ N′.
  - For b′ ∈ (s*, b) and every L: π_L(A) − π_L(c_{b′}) = π_L(c_b ∖ c_{b′}) > 0, because c_b ∖ c_{b′} is a non-null subset of M ∖ c_{s_L} = {ρ_L > 0}.
  - By (L1), c_{b′} <_L A for every L, so c_{b′} ≼₁ A. **This is the step that uses the intersection form of world 1.**
  - Closed sections in b give c_b ≼₁ A. But A ⊊ c_b with c_b ∖ A = N′ non-null, so X_A ≺₁ C_b by strict (G). This is a contradiction.

(c) is (b) contraposed, together with the case s₋ = 0. ∎

*Reading.*
- Theorem D is Thm S21's mechanism run on a family of leading parts. For one member it is Cor S21(a).
- The only way an NA-credal world escapes it next to an additive partner is **end concentration**. At every index some member must be flat just below it, so the members' blind initial segments must reach arbitrarily close to the end of the chain.
- This is exactly the protected-end mechanism of Thm D21, where every bounded endorser vanishes on c_a and the generators' targets accumulate at x → 1. Whether D21's world 1 is itself NA-credal is not decided here.

**Remark D.1 (CHECKED).** In three worlds, let (Nest_e) hold on an edge e_ij, and let world j have a bounded endorser with density > 0 a.e. on R_ij. Then the proof of Theorem D applies verbatim to the **R_ij-leading parts** of the members of world i, that is, the leading parts of ν_L restricted to subsets of R_ij. Edge test models differ from edge-selected models only on R_ij, and competitiveness on {i, j} and closed sections hold at edge indices. The conclusion: either some countable mixture of R_ij-leading parts is positive a.e. on R_ij, or they are end-concentrated along the edge chain.

The first alternative does **not** make world i add up. R_ij-leading parts may sit at a deeper non-Archimedean scale than the global leading parts, and they endorse only comparisons supported in R_ij. This scale mismatch is exactly what blocks the three-world version of Theorem D.

---

## 6. The residual, and what a cover must look like

**Question Q_GG2.** Let n = 3 on M_U (more generally, a decomposable domain with (LF) at D_T1), and let a ranking satisfy strict (G), (IB) and (S). Must every NA-credal world add up?

*What each answer does.*
- **Yes** gives the non-Archimedean intersection theorem on that domain. Every world of an NA-credal cover would add up, and (NC) holds (Theorem A(a)), so Q4.2, or Thm M0closed(b) on M_U, excludes the cover.
- **No** does not by itself give a cover, but it is necessary for one (Theorem A(d)). A counterexample world must have the features below.

What is already known about Q_GG2:
- **Yes for single members and for common leading layers** on M_U (Theorem A(e), via Thm S21).
- **Yes in two worlds**, next to an additive partner under (Nest), unless the members are end-concentrated (Theorem D).
- **The fixed point cannot decide it.** Theorem C's conclusions are consistent (Proposition C.2).

**Corollary 6.1 (what an NA-credal cover must look like).** In every NA-credal cover of T1 on a decomposable domain with (LF) at D_T1 (on M_U where indicated):
1. No world has a finite obstruction, so the configurations of the reduction theorem in which a world fails (NC) (S on M_U, GS elsewhere) do not occur.
2. Some world k (the blind world):
   - its members' leading parts have zero countably additive density on a common non-null set Λ_k;
   - on M_U, no member's M-leading part is a leading charge of the world. So the leading parts genuinely vary with the member, and Π_k has at least two members with non-proportional leading parts.
3. It is not the case that every world has a member whose non-Archimedean part lives only at the ends with a common end functional and whose Archimedean body is integrable and strictly guiding. Non-Archimedean structure must sit in the bulk at some world.
4. On every edge e_ij with (Nest_e) on which the partner j has a bounded endorser with density > 0 a.e. on R_ij, the blind world's R_ij-leading parts are blind on initial segments of the edge chain. Either some countable mixture of them is positive on R_ij, or they are end-concentrated.
5. For any FCA members (one per world), T1 is lexicographically Bayes at an NA weight whose first stage is a weight w for the tuple of leading layers. The resulting lexicographic realisation may be VB-like. The leading tuple itself is degenerate, by item 2.

*Status.* PROVED at the statuses of the results used: item 1 is Theorem A(a) with Thm R21; item 2 is Theorem A(d), (e); item 3 is Corollary B.2; item 4 is Remark D.1 (CHECKED only); item 5 is Theorem C(b) and Proposition C.2.

For the FF1/FF3 programme this means: finitely separable worlds, whose ultraproduct witnesses are NA-credal members (GG3's equivalence), cover T1 only if their witnesses' standard parts are jointly blind in the bulk at some world (items 2 and 3) and end-concentrated along every nested edge where the partner sees (item 4).

**CONJECTURE (labelled as such; not used).** Item 4's end concentration is incompatible with three-world closed choice when the partner worlds add up. Heuristic: an ultralimit of end-concentrated members is a member whose leading part is purely finitely additive at the chain end. That is the end-led shape of Theorem B. But the comparisons that Theorem B's Step 1 uses are not local, and the ultralimit's body scale need not be lexicographically separated from the deviations of the leading parts, so Theorem B does not apply as it stands.

---

## 7. Imports, and what was not used

**Imports and their recorded status.**
- KKM (write-up Thm kkm), proved.
- Thm K31 (a)–(c), one reader.
- N19 Lemma R1.
- Lemma M30(c), one reader.
- Q4.2, PROVED at its listed status (BB2, CC3).
- Thm M0closed (a) and (b), (a) two readers.
- Thm S21, two readers.
- Thm D1, one reader.
- BB2 Thm 6.1 with AUDIT_BB Lemma 2.0, one full reading (CC3).
- Q4.1, one reader.
- M3.7(d) and M3.8, one reader.
- Lemma H10(a) and R1 Prop 3.1.
- FF2 §2 (definitions, Prop 2.3, with inputs CHECKED there).
- P4B Lemma N0, refereed.
- L3.2 and L3.3(a),(c), one reader.

**Not used anywhere:** (E_ψ); countable dense subfamilies; Hahn embeddings (only Hölder's theorem is used); continuity in measure of selections; nestedness (except in Theorem D, where it is a hypothesis, and Remark D.1); Thm ccibu.

**Not used in Theorem B:** (IB), (C), strict (G) of the ranking.

**Files.**
- `GG2_notes.md` (this note).
- `gg2py/vb_lex_check.py` and `gg2py/vb_lex_check.out` (NUMERICS for Proposition C.2).
