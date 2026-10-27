# J1. Conflict cycles on M_U: the germ exchanges of H2.Q are impossible whenever the cycle can be "switched"; the one surviving configuration

15 Oct 2026, round 17 (BRIEF15; BRIEF13 rules). Labels: **PROVED** (full proof here, from results marked proved in
the write-up or re-verified here), **CHECKED**, **CONJECTURE**, **NUMERICS** (none used). No assumption is added.
Setting and notation: write-up §§2–3, §7.7; E1_notes §§1–2 (end, S-positive, eventually ≥ 0 / = 0, end-protected,
base comparison, shadow, admissible, I_ψ); H1_notes §§1–2 (Φ, d_t, Lemma H1.0, Lemma H1.1); H2_notes §§1–4 (H2.0
refinement, T1-correct / T1-wrong ends, V(W), conflict digraph Γ, H2.1). n = 3, K′ = u + s(T1 − u), U = D_{K′}, M_U,
σ_k = sign h_k, E_k(X) = X △ (U ∩ {h_k > 0}); (H_U) = strict (G), (IB), (LA), (S), (C), T1 ∈ C_L on M_U.

---

## 0. Outcome

**No cover of T1 was constructed. H2.Q is answered NEGATIVELY for every conflict cycle whose ends can be put in an
"aligned order" (Theorem J1.2, PROVED). This includes H2's own template (§5.1), and every configuration in which
ends of different worlds are, orthant by orthant, either eventually disjoint or germ-equal. The construction
broke at one point, stated below. Step (2) of the brief (installation in a three-world ranking) was not reached.**

**The new tool: pattern switching (PROVED).** H2.3 tests the dominators of the *Bayes model* B_t. That model is fixed
by the shadow, and at a conflict end it is wrong at one of the two worlds whatever the shadow is. I test instead
the dominators of a *near-Bayes model* X_m:
- X_m equals B_t off the deep parts D_m of all ends;
- on D_m, X_m may carry **any advice pattern we like**.

Because the base endorsers are integrable, Φ(X_m) ≤ ∫_{D_m} Σρ_k → 0 for every pattern. So Lemma H1.0(c) still
applies: some dominator comparison into X_m is unendorsed, hence (by (b)) not a base comparison. Two choices of
pattern give the two results.
- **J1.1 (PROVED).** Pattern = T1 on D_m. This gives H2.3 **without** the heaviness hypothesis (h′): the
  conflict-digraph walk needs no end-heavy shadow.
- **J1.2 (PROVED).** Pattern = "the first world in a fixed order whose end contains the point is right". End-protection
  then forces the dominator to copy X_m deep in the ends of the first world. That makes the second world's comparison
  base, then the third's. All three comparisons are then base and endorsed, which contradicts H1.0(c). The one
  hypothesis is **alignment** (Al): deep in a later world's end, within a fixed depth of an earlier world's
  conflicting end, one is deep in the earlier world's ends.

**Answer to H2.Q.**
- In H2's template (§5.1), A and B are common ends of worlds 1 and 3. Take the pattern "world 1 right": accept on A,
  reject on B.
  - World 1's dominator comparison is ≤ 0 on both of its ends, so end-protection makes it eventually 0. The
    dominator therefore agrees with X_m deep in A and B.
  - Then world 3's comparison is eventually 0 on A and B as well, and world 2's is base.
  - All three comparisons are endorsed, which contradicts H1.0(c).
  - **The germ exchanges of H2 §5.2 cannot be carried, for any t ∈ I_ψ.**
- More generally, no conflict cycle survives if one of its arrows is aligned (Cor. J1.3).

**The single obstruction (where the attempt broke).** A cover with finitely many end-protected worlds and integrable
base endorsers must contain a **doubly misaligned** conflict cycle. In a 2-cycle i ⇄ j this means the following,
for **both** arrows.
- The T1-correct end S of j that shelters the T1-wrong end W of i (H2.1(b): W ⊑ S) is germ-strictly larger than W in
  the shell sense: for some m, the points of S at every depth include points of W_m that are shallow in W.
- Model picture: W is a conic tube shrinking to a ray r, and S is a tube shrinking to a curve of directions through r
  (§4).
- The dominators must then make the exchanges in these **shells**, not at the ends.

I could neither construct world orders that do this with closed sections, nor exclude it. Pattern switching fails
there for a precise reason (§4.2): the depth to which end-protection forces the dominator to copy X_m depends on the
dominator.

| | Statement | Label |
|---|---|---|
| J1.0 | Closure lemma: ≤ 0 deep on all own ends ⇒ dominator copies X deep there | PROVED |
| J1.1 | H2.3 holds without (h′) | PROVED |
| J1.2 | Pattern switching: no cover if some order of worlds is aligned | PROVED |
| J1.3 | (a) H2 §5.1 template; (b) germ-equal-or-disjoint ends; (c) 2-cycles with one aligned arrow: all excluded | PROVED |
| J1.4 | Misaligned arrows exist as configurations of ends (ray inside a curve) | CHECKED |
| J1.Q | Doubly misaligned cycles: carry the exchanges, or not? | open |

---

## 1. Standing hypotheses and the near-Bayes models

**(J)** (H_U) holds. Each world k is end-protected with a **finite** family 𝒮_k of ends, possibly empty, refined by
H2.0 so that every end is orthant-pure and either T1-correct or T1-wrong at its world. There are ρ_k ∈ L¹(μ),
ρ_k > 0 a.e., such that ρ_kμ endorses every relevant world-k comparison whose vector is eventually 0 on every
S ∈ 𝒮_k (**base** comparisons; hypothesis (b) of E1.5 / H2.3). An empty family means that every relevant comparison
is base.

No heaviness is assumed. Put ψ := (ρ_kμ)_k, c := ρσ, Π^k_m := ⋃_{S∈𝒮_k} S_m and D_m := ⋃_k Π^k_m. Then
μ(D_m) → 0, since the families are finite and each S_m ↓ a null set in a finite measure space.

**Step A (ψ is admissible; PROVED).** Use Lemma H1.1 with the localizing family D_m. Let T1 ⪯_k Y be a comparison
with Y regular and Y = T1 on D_m. It is relevant (T1 ∈ C_L), and its vector vanishes on D_m ⊇ S_m for every
S ∈ 𝒮_k, so it is base and ρ_k-endorsed. The ρ_k are integrable.

I re-verified H1.1's proof (H1 is unrefereed):
- Step 1 uses only competitiveness of T1 via Theorem kkm, and endorsement.
- Step 2 uses Lyapunov on M ∖ D_m.
- Steps 3–5 take the limit, prove interiority (the (−,−,+) part of D_{T1} near r₁₂ is non-null and eventually
  outside D_m) and conclude.

All correct. Equivalently, this is E1.5 step 1 verbatim.

**Step B (a weight in I_ψ; PROVED).** Each {t : t·c(g) = 0} is a line, so by Tonelli Z_t is null for a.e. t. If B_t
were coherent for a.e. t, the field c would have (γ). Together with admissibility, Theorem M0closed(a) excludes
this, and (a) uses no integrability. Fix t ∈ I_ψ: ties are null and B_t is incoherent. By H1.0(a),
d_t := inf{Φ(C) : C coherent} > 0, with Φ(Y) := ∫_{Y△B_t} |t·c| dμ.

I re-verified H1.0(a) as well: coherent models are D_K with K ⊇ K′, compact in measure; Φ is lower semicontinuous by
Fatou along a.e.-convergent subsequences; the minimiser C* differs from B_t non-nully; and |t·c| > 0 a.e.

**Step C (near-Bayes models; PROVED).** Let X be any model with X = B_t on U ∖ D_m, and with any advice on D_m.
- X is regular: D_m ⊆ M, and B_t ⊇ N₊ a.e. (on N₊ every σ_k = +, so t·c > 0).
- Φ(X) ≤ ∫_{D_m} |t·c| ≤ ∫_{D_m} Σ_k ρ_k → 0 as m → ∞.
- ψ_k(E_kX) < ∞ for all k.

Fix m with ∫_{D_m} Σρ_k < d_t. Theorem kkm gives a selected, undominated, hence coherent C ∈ C_L with C ⪯_k X for
k = 1, 2, 3, and all three comparisons are relevant. By Lemma H1.0(c), **not all three are endorsed**, so by (b)
**at least one is not base**.

## 2. The closure lemma and heaviness-free H2.3

For a comparison C ⪯_k X write δ_k := 1_{E_kX} − 1_{E_kC}. Then δ_k(g) = 0 iff C and X give the same advice at g,
since on U the advice is determined by the error status at any one world.

**Lemma J1.0 (closure; PROVED).** Assume (J). Let C ⪯_k X be a relevant comparison, and suppose that for every
S ∈ 𝒮_k there is a depth a_S with δ_k ≤ 0 a.e. on S_{a_S}. Then there is a depth m′ with C = X a.e. on Π^k_{m′}.

*Proof.*
- {δ_k = 1} ∩ S_{a_S} is null, so δ_k is S-positive for no S ∈ 𝒮_k.
- End-protection then makes δ_k eventually ≥ 0 on every S ∈ 𝒮_k, i.e. ≥ 0 a.e. on S_{b_S}.
- So δ_k = 0 a.e. on S_{max(a_S, b_S)}. Take m′ := max_S max(a_S, b_S); the family is finite. ∎

Sufficient condition: X is world-k-correct a.e. on S_{a_S}. Then 1_{E_kX} = 0 there, so δ_k ≤ 0.

**Theorem J1.1 (H2.3 without (h′); PROVED).** Assume (J). If the conflict digraph Γ (H2 §4) has no directed cycle,
then (H_U) is contradicted.

*Proof.* Take X := B_t off D_m and X := T1 on D_m, and let C be as in Step C.
- At every T1-correct end S of world k, X is k-correct on S_m. So δ_k ≤ 0 there, and δ_k is not S-positive.
- **Walk.** Suppose δ_i is not eventually 0 on some end of world i.
  - End-protection makes δ_i W-positive for some W ∈ 𝒮_i: if δ_i is not eventually ≥ 0 on an end, some end is
    positive; if it is ≥ 0 but not = 0, that end itself is positive.
  - By the first point, W is T1-wrong at i. On P := {δ_i = 1} ∩ W, C is i-correct, i.e. it gives the advice opposite
    to T1.
  - By H2.1(b) (hypotheses: every world end-protected with a finite family and with a base endorser; re-verified, see
    §5), for every M there is j(M) with W_{j(M)} ⊆ ⋃{S_M : S a T1-correct end of a world of V(W)}.
  - P meets every W_j non-nully, and the covering family is finite. So some T1-correct end S of some l ∈ V(W) meets P
    at every depth M.
  - On P ∩ S_M, X = T1 is l-correct and C, which gives the opposite advice, is l-wrong, so δ_l = −1.
  - Hence δ_l is not eventually ≥ 0 on S, and S is T1-correct. As before, δ_l is then W′-positive for a T1-wrong
    W′ ∈ 𝒮_l, and i → l in Γ.
- Iterating gives an infinite walk, hence a directed cycle, in the 3-vertex digraph Γ.
- If Γ is acyclic, every δ_k is eventually 0 on every own end, so all three comparisons are base and endorsed. This
  contradicts Step C. ∎

So **(h′) and the E1.4/H2.2 reweighting are unnecessary**. Integrability of the base endorsers already lets one move
the tested model off B_t on the ends.

## 3. Pattern switching

Fix an order (k₁, k₂, k₃) of the worlds. For g ∈ D_m let r_m(g) := min{r : g ∈ Π^{k_r}_m}. Define the **switched
model**:
- X_m := B_t on U ∖ D_m;
- at g ∈ D_m, X_m gives the advice that is correct at world k_{r_m(g)}.

X_m is a near-Bayes model as in Step C. For s = 2, 3 let the **conflict set** be
B^s_m := {g ∈ D_m : r_m(g) < s, σ_{k_{r_m(g)}}(g) ≠ σ_{k_s}(g)}: the points where X_m follows an earlier world whose
sign differs from that of k_s.

**Definition (aligned order).** The order is **aligned** if, for infinitely many m, the following holds for s = 2, 3
and every M:

  (Al)  there is j with Π^{k_s}_j ∩ B^s_m ⊆ ⋃_{q<s} Π^{k_q}_M (mod null).

In words: going deep into a later world's ends, inside a fixed-depth conflicting end of an earlier world, takes one
arbitrarily deep into the earlier worlds' ends.

**Theorem J1.2 (pattern switching; PROVED).** Assume (J). If some order of the worlds is aligned, (H_U) is
contradicted.

*Proof.* Take m as in (Al) with ∫_{D_m} Σρ_k < d_t, the switched model X := X_m, and C as in Step C.
1. **World k₁.** X is k₁-correct on Π^{k₁}_m, because r_m = 1 there. By J1.0 there is m′₁ with C = X a.e. on
   Π^{k₁}_{m′₁}.
2. **World k₂.** Let M := m′₁ and take j from (Al) with s = 2. Let g ∈ Π^{k₂}_j ⊆ Π^{k₂}_m.
   - If r_m(g) = 2, X is k₂-correct at g, so δ_{k₂}(g) ≤ 0.
   - If r_m(g) = 1 and σ_{k₁}(g) = σ_{k₂}(g), X is k₂-correct at g, so δ_{k₂}(g) ≤ 0.
   - Otherwise g ∈ B²_m, so by (Al) g ∈ Π^{k₁}_{m′₁} (a.e.). There C = X, so δ_{k₂}(g) = 0.

   So δ_{k₂} ≤ 0 a.e. on Π^{k₂}_j. By J1.0 there is m′₂ with C = X a.e. on Π^{k₂}_{m′₂}.
3. **World k₃.** The same argument with M := max(m′₁, m′₂) and s = 3 gives C = X a.e. on Π^{k₃}_{m′₃}.
4. **Conclusion.** For each k, δ_k = 0 a.e. on S_{m′} for every S ∈ 𝒮_k. So all three dominator comparisons are base,
   hence endorsed by (b), which contradicts Step C (Lemma H1.0(c)). ∎

*Uses:* (b) and integrability (Step C); finiteness of the families (J1.0 and μ(D_m) → 0); end-protection (J1.0);
Theorem kkm; M0closed(a) (Step B); H1.1 (Step A).
*Not used:* heaviness, H2.2, the location of the ends, T1-correctness of the ends, E1.3, (Nest_e).

**Pairwise sufficient condition (PROVED).** (Al) holds for s at all large m if, for every r < s and every pair of ends
S ∈ 𝒮_{k_r}, S′ ∈ 𝒮_{k_s} lying in a common orthant O on which σ_{k_r} ≠ σ_{k_s}, one of the following holds:
- **(i)** S, S′ are eventually disjoint, i.e. μ(S_{j₀} ∩ S′_{j₀}) = 0 for some j₀;
- **(ii)** S′ is shadowed by the earlier worlds: ∀M ∃j with S′_j ⊆ ⋃_{q<s} Π^{k_q}_M;
- **(iii)** S′ ∩ S_m is shadowed by the earlier worlds for every m: ∀m, M ∃j with S′_j ∩ S_m ⊆ ⋃_{q<s} Π^{k_q}_M.

*Proof.* Take m beyond every orthant-purity depth and every j₀ of (i). Then a point of Π^{k_s}_j ∩ B^s_m (j ≥ m) lies
in S′_j ∩ S_m for one of finitely many such pairs (S, S′); pairs in different orthants are disjoint at these depths.
In case (i) this set is null; in cases (ii) and (iii) it lies in ⋃_{q<s} Π^{k_q}_M for large j. ∎

(ii) is supplied by H2.1(b) for T1-wrong ends whose rescuers come earlier. Let S′ be T1-wrong at k_s with every world
of V(S′) that has ends placed before k_s. Then S′_j ⊆ ⋃{T_M : T a T1-correct end of a world of V(S′)} for large j,
so (ii) holds. A world of V(S′) with an empty family contributes nothing to the covering, so it may come anywhere in
the order.

**Corollary J1.3 (PROVED).** Assume (J). Each of the following configurations is contradictory (no cover of T1).
- **(a) H2's template (§5.1).** Worlds 1 and 3 have the common ends A, B, and 𝒮₂ ⊆ {A, B}.
  - Take the order (1, 3, 2). Every later end is an end of world 1, so S′_j ⊆ S′_M ⊆ Π¹_M for j ≥ M, which is (ii).
  - Concretely: the switched model accepts deep A and rejects deep B (world 1 right). The dominator must copy it
    deep in A and B, and then all three comparisons are base. **The germ exchanges of H2 §5.2 are impossible.**
- **(b) Germ-equal or disjoint ends.** For any two ends of different worlds in a common orthant with conflicting
  signs, either (i) holds, or each is shadowed by the other (S′ ⊑ S and S ⊑ S′). Then every order is aligned, with
  any number of conflict cycles.
- **(c) A 2-cycle with one aligned arrow.** Say Γ has a 2-cycle i ⇄ j, the third world l has 𝒮_l = ∅ (for instance
  additive, or adding up with an integrable density), and the arrow i → j is **aligned**: every T1-correct end S′ of j
  and every T1-wrong end W of i that lie in a common orthant satisfy ∀m, M ∃n with S′_n ∩ W_m ⊆ Π^i_M. Take the order
  (i, j, l), and check the pairs (S ∈ 𝒮_i, S′ ∈ 𝒮_j) on conflicting orthants.
  - If S′ is T1-wrong at j, then V(S′) ⊆ {i, l} and 𝒮_l = ∅, so (ii) holds by H2.1(b).
  - If S′ is T1-correct at j, then T1 is wrong at i on O, so S is a T1-wrong end of i and the hypothesis is (iii).

  The l-step is vacuous.

*Proof.* Theorem J1.2 with the pairwise condition. ∎

**Consequences for H2.** H2.Q asks whether a conflict cycle can carry the germ exchanges of H2 §5.2. For every
configuration in J1.3 the answer is **no**: not merely for a non-null set of t, but for every t ∈ I_ψ. In
particular the template of H2 §5.1, the only concrete conflict-cycle design in the corpus, is closed. Theorem H2.3
holds for every aligned configuration, with or without cycles, and with (h′) dropped (J1.1).

## 4. What survives, and where the construction broke

### 4.1 The surviving configuration

By J1.2, a cover under (J) needs **every** order of the worlds to violate (Al). Take the simplest case of J1.3(c):
a 2-cycle i ⇄ j next to a world with no ends. It survives only if **both arrows are misaligned**.
- Arrow i → j is misaligned if some T1-wrong end W of i and some T1-correct end S of j in a common orthant, with
  W ⊑ S (H2.1(b)), satisfy: for some m, S ∩ W_m is not shadowed by Π^i.
- This means that, at every depth of S, a non-null set of points of W_m stays outside some fixed Π^i_M, i.e. is
  shallow in i's ends.

**Example J1.4 (CHECKED; configurations of sets, no ranking).** Let O be a mixed orthant, r̂ a direction in O, and γ
an arc of directions in O with r̂ in its relative interior. Put:
- W_m := the cone over the spherical cap of radius θ_m around r̂;
- S_n := the cone over the θ_n-tube around γ, with θ_m ↓ 0.

Then:
- both are ends, and W_n ⊆ S_n, so W ⊑ S;
- for M with θ_M < θ_m, the set S_n ∩ W_m ∖ W_M contains the cone over {directions within θ_n of γ, at angular
  distance in (θ_M, θ_m) from r̂}, which is non-null for every n;
- so S ∩ W_m ⋢ W, and if W is i's only end in O, the arrow is misaligned.

With two such pairs (one per arrow, e.g. in the orthants (+,+,−) and (−,+,+) of H2 §5.1), the configuration
escapes J1.2. Nothing about rankings is claimed.

**Proposition J1.5 (what the dominators must do in the surviving case; PROVED).** Assume (J), and the situation of
J1.3(c) without the alignment hypothesis. Take the order (i, j, l), m large, the switched model X, and its kkm
dominator C (Step C).
- **(1)** C = X a.e. on Π^i_{m′} for some m′, and world l's comparison is base.
- **(2)** World j's comparison C ⪯_j X is **not** base. It is positive on some **T1-correct** end S′ of j. Deep in S′,
  its positive set lies in the **shells** ⋃_W (W_m ∖ W_{m′}) of T1-wrong ends W of i in the orthant of S′. There C
  gives j's advice, against X's i-advice.
- So the exchanges that H2 §5.2 located "at the ends" must happen in shells of world i's T1-wrong ends that stay at
  bounded depth in W while going to every depth in S′. The same holds with i and j interchanged, under the order
  (j, i, l).

*Proof.*
- (1) is Step 1 of J1.2. 𝒮_l = ∅ makes every l-comparison base.
- If C ⪯_j X were also base, Step C would be contradicted. So by end-protection (as in the walk of J1.1) δ_j is
  S′-positive for some S′ ∈ 𝒮_j, and {δ_j = 1} lies where X is j-wrong.
- **If S′ is T1-wrong at j:** then V(S′) ⊆ {i, l}, and H2.1(b) gives S′_n ⊆ Π^i_{m′} for large n. There C = X, so
  δ_j = 0 deep in S′, a contradiction. Hence S′ is T1-correct at j.
- **Where δ_j = 1 deep in S′:** X is j-wrong only at points with r_m = i and σ_i ≠ σ_j, i.e. in Π^i_m on S′'s
  orthant. The ends of i there are T1-wrong (T1 is right at j there). Points of Π^i_{m′} are excluded by (1). ∎

### 4.2 Why pattern switching stops there (the single obstruction)

In J1.2 the dominator copies X only down to a depth m′ = m′(C) that is not controlled in advance (J1.0 gives
existence only). For a misaligned arrow, the shell S′ ∩ (W_m ∖ W_{m′}) is S′-stationary, i.e. it meets every S′_n
non-nully, **for every** m′. So C can take j's advice there at every depth of S′. That is a protected,
S′-positive comparison at world j, which (b) does not constrain. Reversing the order moves the same problem to the
other arrow.

Three repairs were tried, and each fails at a stated point:
- **(α) Refining ends.** S′ ∖ W is not a decreasing family. With "positive infinitely often / eventually ≥ 0 for all
  large n" on non-decreasing pieces, world j is still end-protected, but the positive set is again confined to the
  same shell, so nothing is gained.
- **(β) Depth-blended priority.** Give each point to the world whose end it is deeper in. Then world i's own
  comparison can be W-positive near r̂, where both ends are deep, and the first step of the closure is lost.
- **(γ) Re-choosing X after seeing C.** Let X* := X, but j-correct on the shell W_m ∖ W_{m′} (inside S′).
  - X ⪯_i X* by (G), and likewise at l if σ_l = σ_i on O. So C ⪯_i X* (and C ⪯_l X*) by transitivity, and these are
    base.
  - The comparison C ⪯_j X* would be base too. But C ⪯_j X does not imply it, because (G) gives X* ⪯_j X, the wrong
    direction for transitivity.
  - Taking the dominator of X* instead restarts the regress with a new uncontrolled depth.

**Question J1.Q (open; I state no conjecture).** Assume (J). Can a **doubly misaligned** conflict cycle carry the shell
exchanges of J1.5 at every t ∈ I_ψ for every integrable admissible ψ, under every axiom? Strict (G), (IB),
transitivity, closed sections for every model, and competitiveness of T1 must all hold.
- If **no**, then no cover of T1 on M_U has finitely many end-protected worlds with integrable base endorsers, at any
  end locations. That is the big negative result of brief task (1).
- If **yes**, Example J1.4 is the geometric template: a cap inside a tube, twice, in two conflicting orthants.

## 5. Re-verifications and dependencies

**Re-verified here (H1 and H2 are unrefereed; only what is used):**
- H1.0(a) and (c): steps as in Step B. (b) is the pointwise identity
  (1_{Y△B_t} − 1_{Y′△B_t})|t·c| = (1_{Y′} − 1_Y)t·c, integrated with all terms finite for integrable ρ.
- H1.1, with D_m containing the deep ends (Step A).
- H2.0: refinement into orthant-pure and T1-pure pieces preserves end-protection and base comparisons. The
  pigeonhole works because pieces decrease, and discarded pieces are null from some depth.
- H2.1(b), as used in J1.1 and in the pairwise condition (ii). It needs:
  - every world of V(W) end-protected with a finite family and a base endorser;
  - the probe X = T1 △ (p ∪ R), with p ⊆ ⋃_{m′} (W_{m′} ∖ ⋃ S_M) and R ⊆ R⁰_i off the deep ends;
  - competitiveness of T1, via Theorem kkm;
  - that δ_j = 1_p − 1_R vanishes on S_M for every end S of every j ∈ V(W). This needs p ⊆ O, i.e. starting p beyond
    W's orthant-purity depth. H2 leaves this implicit; it is harmless.

**External inputs:**
- Theorem kkm.
- Theorem M0closed(a): proved, refereed twice, no integrability.
- Lyapunov.
- Write-up Prop. reduction (a) and R1 Prop. 3.1, via H1.0(a).

**Not used:** (h), (h′), E1.4, H2.2, H2.3's heavy-shadow Step 3, E1.3, (Nest_e), any edge result, (E_ψ).

## 6. What was not done

- **Brief task (2) (installation, every axiom, the L3 shadow check) was not reached.** There is nothing to install:
  - the template of H2 §5.1 is closed (J1.3(a));
  - the surviving doubly misaligned configuration (J1.Q) has no world orders yet.
- **Countably many ends.** J1.0 takes a maximum over the family, and μ(D_m) → 0 needs summable depths. With countably
  many ends, the depths m′_S are not uniform, and (Al) would have to be required end by end with only finitely many
  earlier ends meeting each later end deeply. This is not proved.
- **Non-integrable base endorsers** (route (R-a) of F2, (A) and (C) of H1 §6) are untouched. Step C needs
  ∫_{D_m} Σρ_k → 0.
- No scripts: no NUMERICS were needed, and `j1py/` was not created.
