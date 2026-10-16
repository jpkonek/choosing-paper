# H2. Two or three worlds that fail to add up: conflict ends, the conflict digraph, and a mirrored D2

15 Oct 2026, round 17 (BRIEF15; BRIEF13 rules). Labels: **PROVED** (full proof here), **CHECKED**, **CONJECTURE**,
**NUMERICS** (scripts in `h2py/`, run with `python3 -I`; no proof depends on them). No assumption is added.
Setting and notation: write-up §§2–3, §7.7, §8.5; E1_notes §§1–2 (shadow, admissible, I_ν, dominator comparison, end,
S-positive, eventually ≥ 0 / = 0, end-protected, base); F2_notes §1. n = 3, K′ = u + s(T1 − u), U = D_{K′}, M_U,
σ_i(g) = sign g_i, E_i(X) = X △ (U ∩ {h_i > 0}). (H_U) = strict (G), (IB), (LA), (S), (C), T1 ∈ C_L on M_U.
Under (IB), world i is described by its acceptance set 𝒜_i of ternary vectors δ = 1_{E_iY} − 1_{E_iX} (X ⪯_i Y iff
δ ∈ 𝒜_i; write-up Lemma vectorform).

---

## 0. Outcome

**No cover of T1 was constructed. The attempt broke at the design of the world orders, at one identified point, and
the obstruction is a theorem in the form below.**

- **The brief's question "is the E1.4 reweighting always jointly possible?" — YES at T1-correct ends, for any number of
  protected worlds (Prop. H2.2, PROVED).** At a point where several protected worlds have T1-correct ends, their
  wishes coincide with T1's advice, so they never conflict. What does not transfer to the reweighted shadow is
  base endorsement (b), not joint heaviness. So E1.5's joint-heaviness hypothesis (h) can be weakened to (h′),
  heaviness of the *T1-correct coalition*, at no cost.
- **Requirements conflict only at T1-wrong ends ("conflict ends"), and these force a second world that fails to add
  up (Lemma H2.1(a), PROVED, no hypothesis on the other worlds).** If an end-protected world i has an end on which
  T1 errs at world i, some other world j has every bounded endorsing weight vanishing on a fixed non-null set. So
  idea (a) of the brief, where one world wants acceptance and another silence, is exactly the (R-b) case of F2 §4.3.
- **Theorem H2.3 (PROVED): E1.5 extends to ends anywhere (T1-wrong ends allowed), with heaviness only at T1-correct
  ends, unless the *conflict digraph* has a directed cycle.** The digraph has an arrow i → j when a T1-wrong end of
  world i is shadowed by a T1-correct end of world j. A cycle needs at least two worlds with T1-wrong ends, each
  shadowed by the other's correct end (a *conflict 2-cycle*), or a 3-cycle.
- **Single obstruction revealed (where the construction broke).** For a cover to escape the M0closed route with
  finitely many ends and integrable base endorsers, it must contain a conflict cycle. Along the cycle, the
  dominators C of the heavy shadow's incoherent Bayes models B_t must **exchange germs**: at every conflict end of
  the cycle, C must give the advice that T1 and B_t do *not* give (§5). Each world in the cycle must then accept a
  comparison that trades an error germ at its own T1-wrong end against an error germ at its own T1-correct end,
  both infinitely heavy for it (Lemma H2.1(b)). I could not design world orders with closed sections that accept
  these germ exchanges for a non-null set of t while keeping T1 competitive, nor prove that it is impossible.
  This is stated as Question H2.Q (§5.4).
- **New two-world fact (Theorem H2.4, PROVED; NUMERICS).** A full two-world system on M_U (every axiom, closed
  sections for every model, (C), (LF) at interior selected models) in which **neither** world adds up: D2's world 1
  and its mirror image, protected at the two opposite ends of one chain. In the full systems of the corpus that I read
  (D2.1, C2.1, ExA), some world adds up. Its ends are target-correct and its bases have jointly heavy integrable
  endorsers, so in any three-world installation it falls under E1.5/H2.3 and does not help T1 (§6). It shows that
  two non-adding-up worlds can coexist under every axiom, which (R-b) needs, but it is not a conflict cycle.

| | Statement | Label |
|---|---|---|
| H2.0 | Ends may be refined to be orthant-pure and T1-pure (correct or wrong) at their world | PROVED |
| H2.1 | (a) A T1-wrong end forces another world to fail to add up; (b) with base endorsers it is shadowed by T1-correct ends of the disagreeing worlds | PROVED |
| H2.2 | E1.4 reweighting is jointly possible at all T1-correct ends of all worlds; (b) is what fails to transfer | PROVED |
| H2.3 | E1.5 with ends anywhere and heaviness (h′) at correct ends only: contradiction unless the conflict digraph has a cycle | PROVED |
| H2.4 | Mirrored D2: a full two-world system where neither world adds up | PROVED; NUMERICS |
| H2.Q | Can a conflict cycle carry the germ exchanges with every axiom? | open |

---

## 1. Ends refined (H2.0)

Call an end S of world i **T1-correct** if μ(S_m ∩ E_i(T1)) = 0 for some m, and **T1-wrong** if
μ(S_m ∖ E_i(T1)) = 0 for some m. An end lies in an **orthant** O if μ(S_m ∖ O) = 0 for some m (O one of the six open
mixed orthants; M is their union up to null sets).

**Lemma H2.0 (PROVED).** Let world i be end-protected with a countable family 𝒮_i. Replace each S ∈ 𝒮_i by its
pieces S ∩ O ∩ E_i(T1) and S ∩ O ∖ E_i(T1) (six orthants), discarding a piece that is null at some depth. The new
family 𝒮′_i is countable, consists of orthant-pure ends that are T1-correct or T1-wrong, and world i is end-protected
with 𝒮′_i. The base comparisons (vector eventually 0 on every end) are the same for 𝒮_i and 𝒮′_i.

*Proof.* Each kept piece is decreasing, non-null at every depth, with null intersection: it is an end. If δ is
S-positive, then for every m one of the twelve pieces has {δ = 1} ∩ piece_m non-null; some piece does so for
infinitely many m, hence for all m (the pieces decrease), and that piece is kept. So δ is positive on a piece. A
discarded piece is null from some depth, so "eventually ≥ 0 (= 0) on S" is equivalent to "eventually ≥ 0 (= 0) on
every kept piece of S". ∎

From now on every end is orthant-pure and T1-correct or T1-wrong. Fix a T1-wrong end W of world i in the orthant O.
On O, T1 gives one advice (accept or reject) a.e. on W; it is wrong at i. Let
- **A(W)** := the worlds j ≠ i with σ_j = σ_i on O (T1 is also wrong at j on W);
- **V(W)** := the worlds j with σ_j ≠ σ_i on O (T1 is correct at j on W). V(W) ≠ ∅, since W ⊆ M consists of mixed
  gambles.

Fix also, for each world i, a non-null **improvement region** R⁰_i ⊆ D_{T1} on which toggling T1 (rejecting) is bad
at world i and good at both other worlds: R⁰_1 := D_{T1} ∩ (+,−,−), R⁰_2 := D_{T1} ∩ (−,+,−),
R⁰_3 := D_{T1} ∩ (−,−,+). Each is non-null (it contains a neighbourhood of a point just inside D_{T1} near the
corner ray r_23, r_31, r_12 respectively; E1.3(a)).

## 2. Conflict ends force a partner that fails to add up (H2.1)

**Lemma H2.1 (PROVED).** Assume (H_U). Let world i be end-protected with a countable family 𝒮_i, and let W ∈ 𝒮_i be
T1-wrong, in the orthant O.

**(a)** There are a world j ∈ V(W) and a non-null R ⊆ R⁰_i such that every finitely additive ν ≥ 0 on U, vanishing on
null sets and endorsing the relevant world-j comparisons out of T1, has ν(R) = 0. In particular world j does not add
up. If V(W) = {j}, then for every non-null p ⊆ W that meets W_m non-nully for every m, and every non-null
R ⊆ R⁰_i off the deep parts of the ends of world i (depths fixed in advance as in E1.3(a)), world j accepts
δ_j = 1_p − 1_R: T1 ⪯_j T1 △ (p ∪ R). (**Germ dominance**: a set touching every depth of W outweighs any R.)

**(b)** Suppose moreover that every world j ∈ V(W) is end-protected with a finite family 𝒮_j and has a density
ρ_j > 0, finite a.e., such that ρ_jμ endorses the base comparisons of world j out of T1. Then W is **shadowed**: for
every M there is m′ with
  W_{m′} ⊆ ⋃ {S_M : S a T1-correct end of some j ∈ V(W)}  (mod null).

*Proof.* Choose depths m(S) for all S ∈ 𝒮_i such that R := R⁰_i ∖ ⋃_{S ∈ 𝒮_i} S_{m(S)} is non-null (μ(⋂S_m) = 0;
a summable choice). For a non-null p ⊆ W meeting every W_m, put X := T1 △ (p ∪ R). X is regular (p ∪ R ⊆ M).
- At j ∈ A(W): on p, X gives the advice that is right at i, hence right at j; on R, toggling T1 is good at j. So X
  is better than T1 at j on a non-null set and nowhere worse, and X ≺_j T1 by strict (G). Hence T1 ⋠_j X.
- At i: δ_i = 1_R − 1_p. It is −1 on p ∩ W_m for every m, so it is not eventually ≥ 0 on W. It is +1 only on R,
  which misses S_{m(S)} for every S ∈ 𝒮_i, so it is S-positive for no S. End-protection forbids T1 ⪯_i X.
- T1 is competitive on {1,2,3}: by Theorem kkm it is tied at every world with a selected C_q, and C_q is
  competitive on supp q. So T1 ⪯_j X for some j, and by the two items j ∈ V(W). There δ_j = 1_p − 1_R, since T1 is
  right at j on p and wrong at j on R.

(a) Split the depth pieces of W into countably many pairwise disjoint sets p_1, p_2, … each meeting every W_m
non-nully (split each W_m ∖ W_{m+1} that is non-null into infinitely many non-null parts, and give p_n one part of
each). For each n some j_n ∈ V(W) accepts 1_{p_n} − 1_R. Some j occurs for infinitely many n, say n ∈ N_j. If ν
endorses world j's relevant comparisons out of T1, then ν(E_jT1) ≤ ν(E_jT1) + ν(p_n) − ν(R), i.e. ν(p_n) ≥ ν(R), for
n ∈ N_j. The p_n are disjoint and ν is bounded, so ν(R) ≤ inf_n ν(p_n) = 0. A weight positive on non-null sets
cannot vanish on R, so world j does not add up. If V(W) = {j}, j = j_n for every choice of p and R.

(b) Suppose that for some M the set W_{m′} ∖ ⋃_S S_M (S over all ends of all j ∈ V(W)) is non-null for every m′. A
T1-wrong end of j ∈ V(W) is disjoint from W mod null at large depth (on O, T1 is right at j a.e. on W and wrong at
j on that end), so the union may be taken over T1-correct ends only, which is the claim. Take p_{m′} non-null in
W_{m′} ∖ ⋃_S S_M with Σ_{m′} ρ_j(p_{m′}) < min_{j ∈ V(W)} ρ_j(R), shrinking R further so that it also misses S_M for
every S ∈ 𝒮_j, j ∈ V(W) (finitely many sets; R stays non-null for M large, since μ(⋂S_m) = 0). Put
p := ⋃_{m′} p_{m′}. For j ∈ V(W), δ_j = 1_p − 1_R vanishes on S_{M} for every S ∈ 𝒮_j: it is a base comparison
out of T1, so ρ_j(R) ≤ ρ_j(p), against the choice. The first part of the proof gives T1 ⪯_j X for some j ∈ V(W),
a contradiction. ∎

*Remarks.*
- (a) uses only (H_U) and end-protection of world i. It is the T1-wrong counterpart of E1.3(a): E1.3(a) assumed
  endorsers at the other worlds and concluded that ends are T1-correct; (a) drops the assumption and concludes that
  a T1-wrong end needs a partner that fails to add up. So T1-wrong ends live only in (R-b).
- Where the conflict ends can sit: anywhere in an orthant where T1 is wrong at i, e.g. at the collar of
  ∂U ∩ {h_i > 0} (F2.1: T1 rejects there), or inside D_{T1} ∩ {h_i < 0}.

## 3. Joint reweighting (H2.2): the answer to the brief's question

**Proposition H2.2 (PROVED).** Let ν be an admissible integrable shadow and, for each world i, let 𝒮^c_i be a
countable family of T1-correct ends of world i (any locations, any overlaps between worlds). Then the reweighting of
E1.4, ν′_i = ν_i(1 + f_i) with f_i ≥ 0 supported in the ends of 𝒮^c_i, can be done at all worlds simultaneously;
ν′ is admissible and integrable, and for every t ∈ Δ° and every S ∈ 𝒮^c_i, B^{ν′}_t is world-i-correct a.e. on S_m for
m ≥ m(S, t). Moreover ν′ satisfies

  **(h′)** for every S ∈ 𝒮^c_i: ess inf_{g ∈ S_m} ρ′_i(g) / Σ_{k ∈ W(g)} ρ′_k(g) → ∞ as m → ∞,

where W(g) is the set of worlds at which T1 errs at g (non-empty for g ∈ M).

*Proof.* At a.e. point of a T1-correct end of world i, T1's advice is right at i. If such a point lies in T1-correct
ends of several worlds, T1's advice is right at all of them, so all these worlds have the same sign there: their
"wishes" coincide with T1's advice and cannot conflict. E1.4's construction raises ρ_i only where T1 is right at i;
on such a point every world in W(g) has f_k(g) = 0 (its ends are T1-correct, so they do not contain g at depth, by
the choice of depths in E1.4), and every world k with f_k(g) > 0 is T1-right at g. Hence
t·c^{ν′}(g)σ_i(g) = Σ_{k ∉ W(g)} t_kρ′_k − Σ_{k ∈ W(g)} t_kρ_k ≥ t_iρ_i(1 + f_i) − Σ_{k∈W(g)}ρ_k, and E1.4's estimate
applies verbatim; admissibility and (h′) follow as there (each f_i raises the margin of T1's advice). ∎

So "the E1.4 reweighting is always jointly possible" is a theorem for T1-correct ends, and false only where it must
be: at a T1-wrong end of world i, raising ρ_i would reverse T1's advice and destroy admissibility. **What does not
transfer is (b):** if ρ_i endorses the base comparisons, ρ_i(1 + f_i) need not, because a base comparison is only
*eventually* 0 on the ends, at a depth depending on the comparison, while f_i charges every depth. That is route
(R-a) of F2 §4.3, not pursued here.

## 4. The conflict digraph and the extension of E1.5 (H2.3)

**Definition.** After H2.0, the **conflict digraph** Γ has vertices 1, 2, 3 and an arrow i → j (j ≠ i) iff some
T1-wrong end W ∈ 𝒮_i and some T1-correct end S ∈ 𝒮_j satisfy μ(W_m ∩ S_m) > 0 for every m. (Then j ∈ V(W), since
S is T1-correct at j while T1 is wrong at i on W.)

**Theorem H2.3 (PROVED).** Assume (H_U). Suppose each world i is end-protected with a **finite** family 𝒮_i (possibly
empty; refined by H2.0), and that there are ρ_i ∈ L¹(μ), ρ_i > 0 a.e., with
- **(b)** ρ_iμ endorses every relevant world-i comparison whose vector is eventually 0 on every S ∈ 𝒮_i;
- **(h′)** for every T1-correct S ∈ 𝒮_i: ess inf_{S_m} ρ_i / Σ_{k ∈ W(·)} ρ_k → ∞.

If Γ has no directed cycle, (H_U) is contradicted.

E1.5 is the case with no T1-wrong ends (Γ has no arrows), with (h) replaced by the weaker (h′). By H2.2, (h′) never
conflicts between worlds.

*Proof.* Let ψ := (ρ_iμ)_i.

*Step 1 (ψ is admissible).* E1.5 step 1 verbatim: it uses only (b), competitiveness and Lyapunov, and no location of
the ends. (If a regular X is strictly ψ-better than T1 at every world, let Y agree with T1 on S_m for every end S of
every world and with X elsewhere, m so large that Y is still strictly ψ-better; T1 ⪯_k Y for some k by
competitiveness, a base comparison, against (b). So ψ(T1) is weakly Pareto in the Lyapunov range, and the supporting
weight is interior.) So I_ψ is not null (E1.1(a)).

*Step 2 (shadowing).* By (b) at the worlds of V(W), Lemma H2.1(b) applies to every T1-wrong end W.

*Step 3 (where B^ψ_t is right).* Fix t ∈ Δ°. By (h′) there is m(t) such that for every T1-correct S ∈ 𝒮_j, B^ψ_t is
right at j a.e. on S_{m(t)}: there t·c^ψσ_j ≥ t_jρ_j − Σ_{k ∈ W}ρ_k > 0 (the worlds outside W(g) share σ_j). For every
T1-wrong W ∈ 𝒮_i, Step 2 with M = m(t) gives m′(t) with W_{m′(t)} covered by T1-correct ends S_{m(t)} of worlds of
V(W); there B^ψ_t is right at some j ∈ V(W), so wrong at i. Hence, for δ_i := 1_{E_iB_t} − 1_{E_iC} and any model C:
δ_i ≤ 0 a.e. deep in every T1-correct end of i, and δ_i ≥ 0 a.e. deep in every T1-wrong end of i.

*Step 4 (the walk).* Let t ∈ I_ψ (null ties, B_t incoherent) and let C ∈ C_L satisfy C ⪯_k B_t at every k
(Theorem kkm). The comparisons are relevant (B_t accepts every nonnegative gamble of U). Claim: if δ_i is not
eventually 0 on some end of world i, then there is j with i → j in Γ such that δ_j is not eventually 0 on some
T1-correct end of j.
- If δ_i is not eventually 0 on a T1-correct end E, it is −1 on non-null sets at every depth of E (Step 3), so not
  eventually ≥ 0 there. End-protection makes it S-positive for some S ∈ 𝒮_i; not a T1-correct one (δ_i ≤ 0 deep
  there), so a T1-wrong W. If E itself is T1-wrong, δ_i ≥ 0 deep in E and not eventually 0, so δ_i is E-positive.
  Either way δ_i is W-positive for a T1-wrong W ∈ 𝒮_i.
- Let D := {δ_i = 1} ∩ W: there C is right at i and B_t wrong at i, so C ≠ B_t. For each M ≥ m(t), D ∩ W_{m′(M)}
  is non-null and is covered by the finitely many sets S_M (S a T1-correct end of a world in V(W)); so some S meets
  D at depth M. One S does so for infinitely many M, hence for all M (S decreases). Let S ∈ 𝒮_j. Then
  μ(W_m ∩ S_m) > 0 for all m, so i → j. On D ∩ S_M (M ≥ m(t)), B_t is right at j and C ≠ B_t, so C is wrong at j
  and δ_j = −1. So δ_j is not eventually 0 (not even ≥ 0) on S.

Iterating the claim gives an infinite walk in the three-vertex digraph Γ, hence a directed cycle. If Γ is acyclic,
δ_k is eventually 0 on every end of every world, so every C ⪯_k B_t is a base comparison and (b) gives
ψ_k(E_kC) ≤ ψ_k(E_kB_t) for all k. Then t·ψ(C) ≤ t·ψ(B_t), and B_t is the a.e.-unique minimiser (null ties), so
C = B_t a.e., which is coherent: a contradiction with t ∈ I_ψ (E1.1(b)). ∎

*Uses:* finiteness of the 𝒮_j only in the pigeonhole of Step 4 (and of the V-worlds' families in H2.1(b)).
*Not used:* any location of the ends, E1.3, (Nest_e), the corner geometry beyond E1.1 (i.e. M0closed(a)).

**Corollary H2.3′ (PROVED).** Under the hypotheses of H2.3, a cover needs at least two worlds with T1-wrong ends, and
a directed cycle of shadowings among them: a **conflict 2-cycle** i ⇄ j (a T1-wrong end of i meets a T1-correct end
of j at every depth, and vice versa) or a 3-cycle. By H2.1(a), every world on the cycle has a partner that fails to
add up, so at least two worlds fail to add up. With finitely many ends and integrable base endorsers, this is the
precise content of route (R-b).

## 5. Conflict cycles: what a cover would have to do, and where the construction broke

### 5.1 Geometry (CHECKED)

A conflict 2-cycle between worlds 1 and 3 at the collar of ∂U (F2.1: T1 rejects there):
- end A ⊆ collar ∩ (+,+,−): T1-wrong at 1 (and at 2), T1-correct at 3;
- end B ⊆ collar ∩ (−,+,+): T1-wrong at 3 (and at 2), T1-correct at 1;
- world 1 protected at A (wrong) and B (correct); world 3 protected at B (wrong) and A (correct).
By H2.1(a) both worlds 1 and 3 fail to add up; each is germ-dominant at the end where it is T1-correct
(world 3 at A over R⁰_1, world 1 at B over R⁰_3).

Coherent models can take every germ pattern at A and B: if A and B shrink to rays r_A, r_B in the relative interiors
of two facets of ∂U, then D_{K′} = U accepts a whole neighbourhood of both (near r, U is locally the half-space
{k′·g > 0} of the facet's vertex k′ of K′, and D_K = U locally for every K ⊇ K′ with K ∩ {m·r = 0} = {k′}), T1
rejects both, P_1 accepts A and rejects B, P_3 the opposite. So nothing geometric excludes the configuration.

### 5.2 What the heavy shadow forces (PROVED, from the proof of H2.3)

Let ψ satisfy (b), (h′). Then deep in A and in B, B^ψ_t is right at the heavy T1-correct world, i.e. B_t rejects
both, exactly as T1 does. By Step 4 of H2.3, a kkm dominator C of an incoherent B_t that is not ruled out by (b)
must make δ_1 A-positive or δ_3 B-positive, and then the walk forces both: **C accepts non-null parts of A and of B
at every depth.** On those parts
- δ_1 = +1 on A-parts, −1 on B-parts (plus a base part φ_1 off the ends);
- δ_3 = −1 on A-parts, +1 on B-parts (plus φ_3);
- δ_2 = +1 on both (world 2 is right to accept on (+,+,−) and (−,+,+)).
So each of worlds 1 and 3 must accept an **exchange of an error germ at its T1-wrong end against an error germ at its
T1-correct end**, and both germs are infinitely heavy for it (germ dominance). And this must happen for every
t in a non-null subset of I_ψ, for every ψ with (b), (h′), and in fact for every admissible shadow (E1.1).

### 5.3 The attempted design and where it broke

The natural design is a germ-level copy of a two-world system. At germ level each of A, B is one binary problem:
world 1 wants (accept A, reject B), world 3 wants (reject A, accept B), world 2 wants (accept, accept), T1 gives
(reject, reject), and the dominators must give (accept, accept). For C ⪯_1 B_t and C ⪯_3 B_t, world 1 must weight its
A-germ at least as heavily as its B-germ on the exchanged pieces, and world 3 must weight its B-germ at least as
heavily as its A-germ, in both cases with the base parts φ_1, φ_3 on top.

T1 must stay competitive against Y := T1 △ (D_A ∪ D_B ∪ G), where D_A, D_B are the exchanged pieces and G is any set
of toggles good at world 2. World 2 rejects (strict (G)), so T1 ⪯_1 Y or T1 ⪯_3 Y, with
δ^Y_1 = −1_{D_A} + 1_{D_B} + γ_1 and δ^Y_3 = 1_{D_A} − 1_{D_B} + γ_3. Adding the dominator vector (transitivity is
closure of 𝒜_k under ternary sums, and the supports of γ_k and φ_k can be taken disjoint) gives

  γ_1 + φ_1 ∈ 𝒜_1  or  γ_3 + φ_3 ∈ 𝒜_3, for every admissible G. (PROVED)

These are vectors supported off every end, so a contradiction would follow from (b) if they were realised by
relevant comparisons with ψ_k(γ_k + φ_k) < 0 at both k = 1, 3 simultaneously. Choosing G = G_1 ∪ G_3 with G_1 in a
region where ρ_1 ≫ ρ_3 and G_3 where ρ_3 ≫ ρ_1 makes both ψ-values negative whenever such regions carry enough mass.
**The argument breaks at realisability:** a vector in 𝒜_k is a comparison between some pair of regular models, but
(b) speaks only of comparisons *out of selected models*; γ_k is defined relative to T1, φ_k relative to C and B_t, and
no model of C_L has the error pattern of the sum in general. Conversely, the construction breaks at the same place:
I found no world order that accepts the germ exchanges of 5.2 for a non-null set of t, closes its sections, and
leaves T1 competitive against every such Y without accepting a base vector that some selected model can realise.

### 5.4 Question H2.Q (the single obstruction, stated precisely)

> In a ranking with (H_U), finitely many ends per world and integrable base endorsers (b), (h′), can a conflict cycle
> carry the germ exchanges of 5.2, i.e. can kkm dominators of incoherent heavy-shadow Bayes models accept every
> conflict end of the cycle at every depth, for a non-null set of t?

If no, Theorem H2.3 becomes: no cover of T1 with finitely many end-protected worlds and integrable base endorsers,
in any number of protected worlds and at any end locations. That would leave only route (R-a) (bases with no integrable
endorser that can be made jointly heavy) and countably many or non-end protection. If yes, the configuration of 5.1 is
the template for a cover. I do not state a conjecture either way.

## 6. A full two-world system in which neither world adds up (H2.4)

Setting n = 2, notation of D2_notes §§1–3 (host A, uniform chain coordinate x, c_b = {x < b}, d_b = M ∖ c_b,
λ(c_b) = b, C_b coherent and regular, C_0 = P_1, C_1 = P_2, τ_f, D(f) = ∫_{N₊} f dλ, 𝒦₀, rules R⁻, R⁺, R⁰, designs
(D1)–(D4)). D2's construction uses the chain only through the coordinate x (which pushes λ|_M to Lebesgue measure)
and N₊. Put x̃ := 1 − x on M; it has the same property, and {x̃ < 1 − b} = d_b up to a null set.

**The ranking.** Fix a design 𝒢 in the coordinate x (parameters a, h₀) and a design 𝒢′ in the coordinate x̃ (parameters a′,
h₀′). 𝒜₁ is D2's world-1 acceptance set built on (x, 𝒢), and 𝒜′ is the same construction built on (x̃, 𝒢′).
- World 1: X ⪯₁ Y iff 1_{E₁Y} − 1_{E₁X} ∈ 𝒜₁ (D2's world 1).
- World 2: X ⪯₂ Y iff 1_{E₂Y} − 1_{E₂X} ∈ 𝒜′ (D2's world 1 in the coordinate x̃: its end is x → 0, its generators trade
  thin sources in d_{1−a′} for targets spread over every neighbourhood of x = 0).
- Selection p ↦ C_{p₂}.

**Theorem H2.4 (PROVED).** This ranking on M_U satisfies strict (G), (IB), (LA), (S) (competitiveness on supp p and
closed sections for every evaluable model at both worlds), (C), C_L = {C_b : b ∈ [0,1]}, (LF) at every interior C_b,
and **neither world adds up**: every finitely additive ν ≥ 0 vanishing on null sets that endorses world 1's relevant
comparisons vanishes on c_a, and every one that endorses world 2's vanishes on d_{1−a′}.

*Proof.* Put, for a model X with E₁X ∩ M = A and unanimous errors N_X (λ(N_X) = n), P := c_b ∖ A, Q := A ∖ c_b. Then
E₂X = (M ∖ A) ∪ N_X, and
- C_b ⪯₁ X ⟺ δ₁ := 1_Q − 1_P + 1_{N_X} ∈ 𝒜₁;
- C_b ⪯₂ X ⟺ δ₂ ∈ 𝒜′, with δ₂ := 1_P − 1_Q + 1_{N_X}.
1. **Per-world properties.** Lemma D2.3 (preorder, strict (G), (IB)) and Lemma D2.4 (closed sections at every model)
   are statements about one world's rule and the chain alone. They hold for world 1 as stated, and for world 2 in
   the coordinate x̃ (where E₂C_b = {x̃ < 1 − b}): its sections {b : C_b ⪯₂ X} are mirror images of closed initial segments, i.e. closed final segments
   [β, 1]. p ↦ p₂ is continuous, so the sections in p are closed.
2. **Competitiveness.** Vertices: C_0 = P_1 has E₁ = ∅ and C_0 ⪯₁ X by (G); C_1 ⪯₂ X likewise. Interior b:
   - *n = 0.* D = 0 at both worlds, rule R⁰. If λ(Q) ≥ λ(P), δ₁ ∈ 𝒦₀: it is 0 on N₊; it equals 1_Q ≥ 0 on {x ≥ b},
     which contains a neighbourhood of x = 1; its tails are ≥ 0 for t ≥ b and equal λ(Q) − λ(P ∩ [t, b)) ≥ 0 for
     t < b. So C_b ⪯₁ X. If λ(Q) < λ(P), the mirrored statement holds for δ₂ in 𝒜′: δ₂ = 1_P ≥ 0 on {x < b}, which
     contains a neighbourhood of x = 0, and its heads ∫_{x ≤ u}δ₂ dλ are ≥ 0 for u < b and equal
     λ(P) − λ(Q ∩ [b, u]) > 0 for u ≥ b. So C_b ⪯₂ X.
   - *n > 0.* D = n > 0 at both worlds, rule R⁺. World 1 rejects only if τ_{δ₁}(t) < 0 for some t ∈ [a,1]; since
     τ_{δ₁}(t) ≥ n for t ≥ b, such t < b and λ(P ∩ [t, b)) > λ(Q ∩ [t,1)) + n. World 2 rejects only if
     ∫_{x ≤ u}δ₂ + n < 0 for some u (in the mirrored window); such u ≥ b and λ(Q ∩ [b, u]) > λ(P) + n. Both together
     give λ(P) ≥ λ(P ∩ [t,b)) > λ(Q ∩ [t,1)) + n ≥ λ(Q ∩ [b,u]) + n > λ(P) + 2n, impossible. So C_b ⪯₁ X or
     C_b ⪯₂ X.
   This is (K) for every model, hence competitiveness on supp p.
3. **No weak domination of C_b.** Suppose X ⪯₁ C_b and X ⪯₂ C_b. The vectors are −δ₁ and −δ₂. D(−δ₁) = −n, so R⁻
   forces n = 0. Then −δ₁ = 1_P − 1_Q ∈ 𝒜₁ under R⁰: −δ₁ ∈ 𝒦₀ needs τ(b) = −λ(Q) ≥ 0, so Q is null; and
   −δ₁ − g_* ∈ 𝒦₀ is impossible, since near x = 1 it is ≤ −1 on Q_g ∩ {x ≥ t}, non-null by (D2). So Q is null, and
   −δ₂ = 1_Q − 1_P = −1_P is accepted at world 2, which strict (G) at world 2 (step 1) allows only if P is null.
   Hence X = C_b.
4. **C_L, (C), (LA).** As D2.1 steps 4–5: every C_b is undominated, the only model tied with C_b at both worlds is
   C_b, and by Theorem kkm every undominated model is tied at both worlds with some C_b. So U_L = C_L = {C_b}, all
   coherent.
5. **(LF).** C2.1(4), as in D2.1.
6. **Neither world adds up.** World 1: D2.1 step 7 verbatim (it uses only world 1's generator comparisons
   C_a ⪯₁ X_g, which are relevant). World 2: the mirror of the same argument, with the relevant comparisons
   C_{1−a′} ⪯₂ X′_g, X′_g regular with E₂X′_g = (d_{1−a′} ∖ P′_g) ∪ Q′_g (sources P′_g ⊆ {x̃ < a′} = d_{1−a′}). ∎

*Remarks.*
- In the full two-world systems of the corpus that I read (D2.1, C2.1, ExA), some world adds up. H2.4 has ratio
  certificates with thin sources at both worlds, not simple ones, so it does not answer (R1) (mirrored simple
  pairs). It is consistent with
  Thm RATE and Conj. NDL: φ₁(P) ≥ λ(P) by world 1's base cone alone, so (SR₁) holds and there is no doubly-light
  sequence.
- F1.2 (chain monotonicity) needs an additive partner and does not apply; each world's σ-finite endorsers are still
  monotone in x by the proof of F1.2(b), with world 2's own (K)-comparisons in place of the partner's: not checked.
- **Why it does not help T1.** Relative to any interior target C_{b*}, both ends are target-correct at their worlds,
  and the bases have integrable endorsers that are jointly heavy (world 1: w(x) nondecreasing → ∞ at 1, E1.6; world 2:
  w(1 − x)). So in any three-world installation at T1 with T1-correct ends it falls under E1.5 / H2.3 (no conflict
  arrows). To become a conflict 2-cycle, each world would need a second end at the *other* end of the chain, where it
  is target-wrong and the partner is germ-dominant (H2.1(a)); D2-type generator rules give heaviness through designed
  pairs only, not germ dominance, and §5.3 is where that extension stalled.

NUMERICS (`h2py/h2_mirrored_d2.py`, `.out`; exact integer cell model symmetric under x ↦ 1 − x, two design levels
(q = 3, 5), three scale blocks at each end, N₊ appended; "near the end" proxied by the outermost block): 0 failures in
1500 competitiveness tests at interior cuts, 1500 no-weak-domination tests, 600 + 600 strict-(G) tests, 129 + 399
transitivity triples, 40 + 40 section-shape tests (initial at world 1, final at world 2); all 40 generator comparisons
accepted at each world.

## 7. What was not done

- No three-world system was built; no selection through T1; no axiom was verified for a T1 candidate.
- Ideas (b) and (c) of the brief (cross-world certificates; holonomy constraints on facet rates) were not reached:
  §4 shows that any cross-world mechanism visible to the heavy shadow must be a conflict cycle, and §5.3 is where the
  first concrete design stalled.
- The brief's warning heuristic (end-light additive cores collapse) was not examined.
- Countably many ends per world: H2.1 holds; H2.3's pigeonhole needs finiteness (or a uniform covering).

## 8. Files (`h2py/`, run with `python3 -I`)

- `h2_mirrored_d2.py` (+ `.out`): Theorem H2.4 in an exact cell model.
