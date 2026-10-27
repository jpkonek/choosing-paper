# KK4 (round 39, BRIEF31). Non-protected rate designs: protection is not what makes interior Bayes models rigid. Lexicographic Bayes models are always selected. Outside two branches the JJ2 exclusion returns; inside them the failure of protection is located, defended and tested

18 Oct 2026. Rules of BRIEF13 and BRIEF31; the corrections of AUDIT_JJ.md are adopted. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: none used.
- **CONJECTURE**: none offered.

Scripts are in `kk4py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All arithmetic is
`fractions.Fraction`.

Setting: three worlds, T1 = D_K with K = (1−ε)u + εΔ, any ε ∈ (0,1). Notation of the write-up §2, II1 §1, II2 §1 and
JJ2 §1. No assumption is added. Every extra hypothesis below is a hypothesis of the stated result, and it defines the
sub-class that result is about.

---

## 0. Outcome

**No cover of T1 was obtained.** The non-protected rate designs were analysed in the order the brief asks. One general
theorem changes the picture.

1. **Interior Bayes rigidity does not need protection (Theorem 2.4; PROVED).** Take any rate cover in the class (no
   (NT) assumed). Take any lexicographic chain of weights with an interior leading weight and an interior final weight
   on Ψ. Then the chain's pointwise minimiser is a.e. unique, coherent, and a **selected** model.
   - The proof uses lexicographic admissibility of chain minimisers (Lemma 2.2; CHECKED, `lexchain.py`), the
     transitivity-free KKM argument, and direct (C).
   - This is what JJ2 Lemma 4.1 and JJ3 Theorem 2.1 obtained from (NT). In the rate class the second level and (C) do
     the same work.
   - So the escape the brief proposes, interior Bayes models that are "NOT unique/coherent", is unavailable at the
     lexicographic level. It survives only as **non-uniqueness of the Φ-Bayes model at particular interior weights**,
     resolved differently by different chains.
2. **Where protection fails, at a definite index with an actual competitor (§3; PROVED).** There are exactly two ways
   in which a non-protected design can avoid the JJ2 setting.
   - **(CT) concurrent leading ties.** For some interior w0, a non-null set of mixed pairs has two w0·φ-minimisers.
     Then KKM for the leading preorder gives a definite index p0 and an incoherent competitor X0 (a splice of two
     selected chain models) that is **Φ-tied with C_{p0} at all three worlds** (Proposition 3.2).
   - **(BT) visible best-ties.** For some world k, on a non-null set of mixed pairs, the k-best advice is φ_k-tied
     with another advice that some admissible chain prefers. Then (NT) fails at p0 = e_k, against X0 = B^k switched to
     the tied advice (Proposition 3.3).
3. **Outside (CT) ∪ (BT) there is no rate cover (Theorem 4.1; PROVED modulo JJ2 Theorem 7.2, itself modulo the
   imported chain of Theorem gm's short route; alternatively modulo JJ3 §§3–5, ccibu and gm).** Theorem 2.4 supplies
   (W1)–(W6) of JJ2 Definition 7.1 for a normalised copy of Φ.
   - This contains JJ2 Theorem 7.4 and JJ3 Theorem 5.1 (full domain) as special cases.
   - It also excludes every non-protected design whose non-protection comes only from boundary-weight ties,
     reindexing, Ψ-broken boundary ties, or invisible ties.
   - **Exact reason:** the rigidity that kills protected designs is produced by KKM + (C) + the second level, not by
     protection.
4. **Branch (BT): the three items of the brief (§5; PROVED, CHECKED).** For an odd-world best-tie φ_o(O) = φ_o(S) on a
   non-null set Z:
   - *item 1:* (NT) fails at e_o against X0 = B^o with S on Z;
   - *item 2:* world o defends, with Φ_o = 0 < Ψ_o, and (★) holds at e_o with the weight e_o;
   - *item 3:* uniform adequacy forces every selected model with o in its support that rejects on part of Z to be
     **pointwise φ_o-optimal**. In particular this holds on a whole neighbourhood of e_o (Theorem 5.1). This is
     necessary. A plateau C_p = B^o, or (ND) near e_o, is sufficient (Proposition 5.3).
   - **Globally**, Theorem 2.4 makes the chain model lex-min(φ_o, w·φ, w′·ψ) a selected coherent D_K with K ≠ {e_o}.
     This forces the best-ties of world o to fill open cones of **both** o-odd pairs and pairs with o as a positive
     world, adjacent to the hyperplane {h_o = 0} (Proposition 5.4; CHECKED, `collar.py`). Best-ties on any smaller set
     are excluded.
5. **Branch (CT): the three items (§6; PROVED, CHECKED).**
   - The concurrent-tie set at w0 is, mod null, an open cone, and it carries a fan of selected coherent chain models
     (Proposition 6.1).
   - *Defence:* admissibility and (C) force Ψ_i(rec(C_{p0}, X0)) > 0 at some world (Lemma 2.3).
   - *Uniformity:* strict unanimity at an interior index excludes defeating sequences there (Lemma 6.2).
   - *Necessary pairwise criterion for (★) at every fan member:* Proposition 6.3. It is violated by explicit surrogate
     designs, with defeating segments computed exactly (`fan.py`, P2 and P3).
   - Single-direction ties whose normalised lower increment is essentially constant are excluded outright by (C)
     (Corollary 6.4).

**Single most important open point.** Branch (BT) with no concurrent interior ties. There the interior Φ-Bayes family is
unique, coherent, selected and Hausdorff-continuous (Corollary 2.5), exactly as in JJ2. The only defects are:
- strict-best (JJ2's (F1)) fails on the open best-tie collar of Proposition 5.4;
- the vertex limits at e_o are the collar models of Proposition 5.4, not B^o (JJ2's (W5)).

Does JJ2 Theorem 7.2, whose (F1) and (W5) uses are listed in its Table 7.2 (S3a–b, S6, S7, S8c, S11), survive this
specific weakening? A yes closes (BT) modulo the same imports as Theorem 4.1. A no identifies the exact place where a
non-protected rate cover could live.

---

## 1. Setting and the class

### 1.1 The rate class

**(H)**, the class of the brief. Each item is a defining property, not an added assumption.
- (H1) **Domain.** The full four-advice domain (§§4–6), or a decomposable domain with (LF) at D_{T1} (§§2–3). Pairs
  are indexed by majority orientation h, with advices M, S, O, ×, and best_k(h) is the world-k-best advice. B^k is the
  pointwise world-k-best model.
- (H2) **Base.** Additive penalties φ_i (leading, weakly guiding) and ψ_i (lower, strictly guiding), with an integrable
  envelope E. Costs are Φ_i, Ψ_i. For a record t: increments Φ_i(t), Ψ_i(t), and size m(t).
- (H3) **Selection.** p ↦ C_p is a map of coherent models on Δ, continuous in measure, with C_{q₀} = T1.
- (H4) **Rate rule.** For a continuous k : (0, μ(H)] → (0,∞), 𝒜_i^k = {ι} ∪ {t : Φ_i(t) ≥ 0, Ψ_i(t) + k(m(t))Φ_i(t) ≥ 0}.
  Every C_p is competitive on supp p in 𝒜^k. By AUDIT_HH_rate this is equivalent, for some k, to (RB).
- (H5) **Admissibility.** Every C_p is undominated in 𝒜^k. In particular T1 is.
- (H6) **Direct (C)** for 𝒜^k: a model tied at every world with a member of C_L belongs to C_L. Here C_L is the set of
  coherent undominated models.

A system satisfying (H) is a **rate cover**. By HH2 Prop 6.1(a)–(d) with the JJ1 §1.4 repair (PROVED there; JJ1: correct),
it is reflexive, (IB), strict (G), (FC) with ordering extension L, and has closed sections for every model. (LA) and
(LF) are then immediate. The tie structure is also known: ties of 𝒜^k are exactly lexicographic ties (JJ1 §1.3), and
every 𝒜^k-strict comparison is L-strict (JJ1 §1.2).

**Not assumed:** (NT), (U), (A1)/(A2) of II1, injectivity, strict-best, or anything about W^Φ.

### 1.2 Notation used below

- **Lexicographic base.** L_i compares (Φ_i, Ψ_i) lexicographically.
- **Weak Bayes weights.** W^Φ(p) is the set of α ∈ Δ at which C_p is pointwise weak α-Bayes for φ.
- **Leading-nonpositive records.** G(p) is the set of records z out of C_p with Φ_i(z) ≤ 0 for all i ∈ supp p.
  I^≥(z) := {i ∈ supp p : Φ_i(z) = 0 ≤ Ψ_i(z)}. (★_p) is II2 Theorem 3.1(b).
- **Leading ties at a weight.** For w ∈ Δ and a pair h, M_w(h) ⊆ A(h) is the set of minimisers of w·φ(h, ·).
- **Concurrent tie set.** T*_w := {mixed h : |M_w(h) ∩ {M, S, O}| ≥ 2}.

Two standard facts are used repeatedly.
- **(F-a)** Additive functionals on a decomposable domain with integrable envelope. A model attains the minimum of
  ∫ v·φ(h, a_X(h)) dμ iff a_X(h) is a pointwise minimiser for a.e. h. The same holds lexicographically for finitely
  many levels, by induction, because the class of pointwise minimisers of the earlier levels is itself decomposable.
- **(F-b)** Disagreement sets of coherent models. For credal sets K₁ ≠ K₂, the set of pairs where D_{K₁} and D_{K₂}
  advise differently is, mod null, a non-null **open cone**.
  - It is a cone because a_{D_K}(th) = a_{D_K}(h) for t > 0.
  - Openness up to null sets: the advice of D_K at h is decided by the signs of s_K(±h), with s_K(g) := min_K m·g.
    Off the null set {s_{K_r}(±h) = 0, r = 1, 2}, these signs are locally constant.
  - It is non-null because K ↦ D_K is injective (write-up §2).
  - The splice argument of JJ3 Theorem 2.1 step 2 rests on this.

---

## 2. Lexicographic Bayes models are selected

**Definition 2.1.** An **admissible chain** is λ = (v¹, …, v^r ; w′) such that:
- for some s ≤ r, the vectors v¹, …, v^{s−1} are in Δ and v^s ∈ int Δ;
- v^{s+1}, …, v^r ∈ ℝ³ are arbitrary;
- w′ ∈ int Δ.

At each pair let A^λ(h) be the set of advices that minimise the vector (v¹·φ(h,·), …, v^r·φ(h,·), w′·ψ(h,·))
lexicographically over A(h). A **λ-model** is a model with a_X(h) ∈ A^λ(h) a.e. λ-models exist: the pointwise choice is
measurable, and it is evaluable by Remark advicerange of the write-up.

**Lemma 2.2 (PROVED; CHECKED, `lexchain.py`).** Every λ-model B is undominated in the lexicographic base L.

*Proof.* Suppose Y L-dominates B. Then (Φ_i(Y), Ψ_i(Y)) ≤_lex (Φ_i(B), Ψ_i(B)) at every i, strictly at some i. In
particular Φ(Y) ≤ Φ(B) componentwise.

1. **The weights before s.** Suppose Y is a minimiser of the first t − 1 levels, with t < s (vacuous for t = 1).
   - Since v^t ≥ 0, v^t·Φ(Y) ≤ v^t·Φ(B).
   - By (F-a), B minimises level t among the minimisers of the earlier levels.
   - So the two values are equal, and Y also minimises level t.
2. **Level s.** The same argument gives v^s·Φ(Y) = v^s·Φ(B). Since v^s has full support and Φ(Y) ≤ Φ(B), we get
   Φ(Y) = Φ(B).
3. **Levels after s.** Every later level v^t·Φ then takes the same value on Y and on B. So Y is a minimiser of all φ-levels.
4. **The ψ-level.** With Φ(Y) = Φ(B), lexicographic domination gives Ψ_i(Y) ≤ Ψ_i(B) for all i, strictly for some i.
   Since w′ ∈ int Δ, w′·Ψ(Y) < w′·Ψ(B). This contradicts minimality of B at the last level, by (F-a). ∎

CHECKED (`lexchain.py` → `lexchain.out`). Exhaustive search over all 4⁴ models on random four-cell surrogates, with
planted concurrent ties at w0 = u and odd-world best-ties:
- 300 instances for each of five chain shapes: (w0; w′), (w0, v; w′) with v ∈ ℤ³, (e_k, w; w′), (e_k, e_j, w; w′) and
  (w; w′). In every case 0 minimisers are L-dominated.
- Controls:
  - a pure w0-minimiser with an adversarial Ψ tie-break is L-dominated in 5 of 300 instances;
  - an explicit chain (e₀, e₁; u) with no interior φ-weight has an L-dominated minimiser, while all four chains of the
    same cells with an interior φ-weight do not.

So the interior weight and the Ψ-level are both needed.

**Lemma 2.3 (PROVED).** In a rate cover, let C be a selected model and z = rec(C, X) a non-null record with Φ_i(z) = 0
at every world.
- (a) Ψ(z) is not ≤ 0 componentwise with a negative coordinate.
- (b) If Ψ(z) = 0, then X is coherent. In particular, supp z cannot be contained, mod null, in a bounded set.

Hence Ψ_i(z) > 0 for some world i, whenever X is incoherent or supp z is bounded.

*Proof.*
- **(a)** At every world, rec(X, C) has Φ_i = 0 and Ψ_i = −Ψ_i(z) ≥ 0, so it is accepted by 𝒜_i^k. At a world with
  Ψ_i(z) < 0 its reverse z has Φ_i = 0 > Ψ_i and is rejected. So X dominates C, against (H5).
- **(b)** X is lexicographically tied with C at every world, so it is 𝒜^k-tied (JJ1 §1.3). C ∈ C_L by (H5), so (H6)
  gives X ∈ C_L, and X is coherent. Two coherent models disagree on an open cone or on a null set (F-b). A non-null
  cone is not contained in a bounded set. ∎

**Theorem 2.4 (PROVED).** Let (H) hold, on any decomposable domain with (LF). For every admissible chain λ:
- the λ-model B is a.e. unique, i.e. A^λ(h) is a singleton for a.e. h;
- B is coherent;
- B = C_p a.e. for some p ∈ Δ.

*Proof.*
1. **Undominated, hence coherent.** By Lemma 2.2, B is L-undominated. An 𝒜^k-domination is an L-domination, because
   𝒜^k ⊆ L and 𝒜^k-strict comparisons are L-strict (JJ1 §1.2). So B is 𝒜^k-undominated.
   - HH1 Prop 1(c) (arbitrary relations, (LA), (S), direct (C); PROVED there, audit: sound) gives U_L = C_L.
   - So B ∈ C_L, and B is coherent. This holds for every λ-model.
2. **Uniqueness.** Suppose the set T^λ := {h : |A^λ(h)| ≥ 2} is non-null.
   - Choose measurable λ-models B₁, B₂ that differ at every h ∈ T^λ. Both are coherent by step 1, so by (F-b) they
     differ on a non-null cone G.
   - Let A := {‖h‖ < 1}, a symmetric set. The splice X := B₁ on A and B₂ off A is again a λ-model, so it is coherent.
   - JJ3 Theorem 2.1 step 2 now gives a contradiction. For a.e. (h, t) with h ∈ G ∩ A and t > 1/‖h‖, the advice of X
     at h equals its advice at th. These are B₁'s advice at h and B₂'s advice at h, which differ.
3. **Selected.** By HH1 Prop 1(b) (KKM, using closed sections and competitiveness only), B ≈ C_p at every world for
   some p.
   - Ties are lexicographic ties, so Φ(C_p) = Φ(B) and Ψ(C_p) = Ψ(B).
   - So C_p attains every level of λ at the minimal value, and by (F-a) it is a λ-model.
   - By step 2, C_p = B a.e. ∎

**Corollary 2.5 (PROVED).** Let (H) hold, and let w ∈ int Δ with T*_w null.
- (a) Every pointwise w·φ-minimiser agrees with the selected coherent model B_w := B(w; w′) a.e., except on trivial
  blind switches: unanimous pairs, and × where it is φ-tied with another advice at every world (§3). This model does not
  depend on w′.
- (b) If T*_{w′′} is null for all w′′ in a neighbourhood N ⊆ int Δ of w, then w′′ ↦ K_{w′′} is Hausdorff-continuous on N.

*Proof.*
- **(a)** Off T*_w, the minimiser among {M, S, O} is unique at mixed pairs. × is a minimiser only if it is φ-tied with
  another advice at every world, and then every chain prefers the other advice through ψ. On unanimous pairs every chain
  picks M, which is ψ-best at every world.
- **(b)** Off the null set T*_w, a strict minimiser at w stays the strict minimiser nearby, so B_{w_n} → B_w in
  measure. Then apply the injectivity argument of JJ3 Lemma 2.3(a). ∎

**Remark 2.6 (what replaces protection; the crux of the brief).**
- JJ2 Lemma 4.1 and JJ3 Theorem 2.1 derived "every interior Bayes model is unique, coherent and selected" from (NT).
  They used KKM for the leading preorder, and then (NT) to turn ties into equality.
- In the rate class the same conclusion holds for **lexicographic** Bayes models without (NT):
  - Lemma 2.2 replaces "dominating a Bayes model lowers w·Φ";
  - (C) replaces "(NT) makes ties trivial";
  - the second level breaks exactly the ties that (NT) used to forbid.
- II1 Lemma 2.5 already had coherence of L-undominated models. New here are:
  - chain models are L-undominated;
  - they are unique without (A2);
  - they are selected.
- Consequence: a non-protected design cannot make interior Bayes models non-coherent. It can only make the Φ-level
  Bayes model **non-unique** at some interior weights, the set (CT) below. There the chain models differ, all of them
  selected. Separately, it can make **vertex** limits differ from B^k, the set (BT) below.

---

## 3. Where protection fails: a definite index and an actual competitor

**Definition.** A **trivial blind switch** at h is a switch from a to b with φ(h,b) = φ(h,a) at every world while b is
worse than a in every world's rank. These occur only on unanimous pairs, and as switches to × at mixed pairs. Such a
switch has Φ = 0 and Ψ > 0 at every world, so it is accepted at every world: r_i = 0 everywhere.

**Proposition 3.1 (localisation; PROVED).** Let (NT) fail at p0 through X0 ≠ C_{p0}, and put z0 := rec(C_{p0}, X0). Then
for every α ∈ W^Φ(p0) with supp α ⊆ supp p0:
- z0 switches, a.e. on its support, only between α·φ-minimisers;
- Φ_i(z0) = 0 for every i ∈ supp α.

Consequently, if some α ∈ W^Φ(p0) ∩ Δ_{supp p0} is interior and T*_α is null, then z0 consists a.e. of trivial blind
switches. So (NT) fails at p0 only in the trivial sense, and C_{p0} defends at every world with r = 0. The same holds at
any α with supp α ⊆ supp p0 whose tie set out of C_{p0} is null; then (NT) holds outright (JJ2 Lemma 2.1).

*Proof.*
- **Increments.** α·Φ(z0) ≤ 0, because Φ_i(z0) ≤ 0 on supp p0 ⊇ supp α. The integrand α·δφ is ≥ 0 a.e., by weak
  Bayes optimality. So the integrand vanishes a.e. on supp z0, and Σ α_iΦ_i(z0) = 0 with every term ≤ 0.
- **The interior case.** Let α be interior with T*_α null.
  - At a.e. mixed pair the α-minimiser in {M, S, O} is unique.
  - × is an α-minimiser only if φ(×) = φ(a) at every world for some a, since φ(×) ≥ φ(a) componentwise and α > 0.
  - On unanimous pairs, the advices tied with the α-minimal M are tied at every world, by the same argument.
  - C_{p0} is coherent, so it never gives ×, and it gives M on unanimous pairs. So every switch in z0 is a trivial blind
    switch. ∎

*Reading.* Every actual failure of protection runs along leading ties at **every** Bayes weight of the selected model.
Only two kinds of tie can host it on a non-null set:
- ties at an interior weight, which are concurrent: (CT);
- ties at boundary weights, which are coordinate zeros of δφ, i.e. ties at one world. Among those, only best-ties
  matter for any interior chain: (BT).

The definitions make this precise.

**Definition 3.2.**
- **(CT)** There is w0 ∈ int Δ with μ(T*_{w0}) > 0.
- **(BT)** For some world k, the set Z^vis_k of mixed pairs carrying a **visible best-tie at k** is non-null. A visible
  best-tie at k is an advice b ∈ {M, S, O}, b ≠ best_k(h), with φ_k(h, b) = φ_k(h, best_k(h)), such that
  δ := φ(h, b) − φ(h, best_k(h)) has a negative coordinate or is 0.
  - Equivalently, some chain (e_k, w; w′) with w, w′ interior picks an advice other than best_k(h) at h. The
    equivalence is immediate from the lexicographic comparison. If δ = 0, then δψ has strictly mixed signs at a mixed
    pair.
  - A best-tie with δ ≥ 0, δ ≠ 0 is **invisible**: no chain with an interior weight ever picks b.

**Proposition 3.3 (the (CT) competitor; PROVED).** Let (H) hold with (CT) at w0.
- (a) There are selected coherent λ-models B₁, B₂, both w0·φ-minimisers, that differ on a non-null open cone G ⊆ T*_{w0}.
- (b) The splice X0 := B₁ on {‖h‖ < 1} and B₂ off it is an incoherent w0·φ-minimiser.
- (c) There is p0 ∈ Δ with Φ_i(C_{p0}) = Φ_i(X0) at **every** world i. So (NT) fails at p0, whatever supp p0 is, against
  the actual competitor X0 ≠ C_{p0}. Moreover C_{p0} is itself a pointwise w0·φ-minimiser.

*Proof.*
- **(a)** At h ∈ T*_{w0}, take two tied advices a ≠ b in {M, S, O}.
  - If φ(h,a) ≠ φ(h,b), the chains (w0, v; w′) and (w0, −v; w′) separate them for any v with v·(φ(h,a) − φ(h,b)) ≠ 0.
  - If φ(h,a) = φ(h,b), then ψ(h,a) − ψ(h,b) has strictly mixed signs (a mixed pair), and chains (w0; w′₁), (w0; w′₂)
    separate them.
  - For each h the set of separating chain pairs is open. Fubini over a countable dense family of chains gives two
    chains whose models differ on a non-null subset of T*_{w0}.
  - Both models are selected and coherent by Theorem 2.4, and their disagreement is an open cone G (F-b).
- **(b)** X0 is pointwise w0-minimal. If it were coherent, step 2 of Theorem 2.4's proof would give a contradiction.
- **(c)** Use the leading preorder X ≼^Φ_i Y ⟺ Φ_i(X) ≤ Φ_i(Y).
  - Every C_p is competitive for it on supp p: 𝒜^k-competitiveness implies L-competitiveness, and L-acceptance implies
    Φ_i(X) ≥ Φ_i(C_p).
  - Its sections {p : Φ_i(C_p) ≤ Φ_i(X0)} are closed, by continuity in measure.
  - KKM gives p0 with Φ_i(C_{p0}) ≤ Φ_i(X0) at every i.
  - X0 minimises w0·Φ with w0 interior, so equality holds at every i, and w0·Φ(C_{p0}) is minimal. Then (F-a) applies.
  - X0 is incoherent and C_{p0} is coherent, so they differ on a non-null set. ∎

**Proposition 3.4 (the (BT) competitor; PROVED).** Let (H) hold, with Z ⊆ Z^vis_k non-null and b(h) the tied advice.
Put X0 := B^k with b on Z. Then:
- Φ_k(X0) = Φ_k(B^k) = Φ_k(C_{e_k}), since C_{e_k} = B^k by II2 Lemma 1.2(b) on the full domain. So (NT) fails at
  p0 = e_k;
- the record has Φ_k = 0 < Ψ_k, so world k defends with r_k = 0;
- (★_{e_k}) holds with the weight e_k ∈ W^Φ(e_k).

*Proof.* B^k is pointwise φ_k-minimal by weak guidance, and b is φ_k-tied on Z. ψ_k strictly prefers best_k. ∎

**Remark 3.5.** A protected design lies in neither branch. (NT) excludes (CT) by JJ2 Lemma 4.1, and (BT) by strict-best
(II1 Prop 5.2(a)). Proposition 3.3 is the converse: (CT) forces a definite failure of (NT), with a competitor that is
leading-tied at every world.

---

## 4. Outside the two branches there is no rate cover

**Theorem 4.1 (PROVED modulo JJ2 Theorem 7.2: that theorem is PROVED there modulo the imported chain of Theorem gm's
short route, and its sign audit, Table 7.2 S8a–b, is pending referee in KK1).** On the full domain, every rate cover of
T1 satisfies (CT) or (BT).

*Proof.* Assume (H), not (CT), and not (BT).

1. **Normalisation.** Define Φ′ from Φ in three steps, in this order.
   - (i) On unanimous pairs, raise φ(S) by η(h) and φ(O) by 2η(h) at every world.
   - (ii) At every mixed pair and world k, raise φ_k of every advice in the best-tie class of best_k(h) (all of these are
     invisible, a.e., by assumption) by the same η(h).
   - (iii) Raise φ_k(h, ×) to max_{a≠×} φ_k(h, a) + |h_k| (II1 Prop 5.2(b)).

   Here η(h) ∈ (0, E(h)] is measurable and at most half of every positive gap between consecutive values of φ_k(h,·), so
   the monotonicity along each world's rank is kept. Then:
   - Φ′ is integrable and weakly guiding;
   - Φ′ is strict-best at every pair, because visible best-ties are null by assumption and the others were raised;
   - × is strictly worst.
2. **The interior Bayes family is unchanged.** Fix w ∈ int Δ.
   - Step (i): on unanimous pairs, M is the w-minimiser of Φ′ and the chain choice for Φ.
   - Step (ii): an invisible tied advice b at a mixed pair has w·δ > 0 for every interior w (δ ≥ 0, δ ≠ 0). So it was
     never a w-minimiser, and raising it changes nothing.
   - Step (iii): × is never a w-minimiser of Φ′. For Φ it is one only when it is fully φ-blind with another advice, and
     no chain picks it then.
   - Hence, since T*_w is null (not (CT)), the a.e.-unique w-minimiser of Φ′ is the selected coherent model B_w of
     Corollary 2.5.
3. **(W2), (W3), (W6).** (W2) is step 2. (W3) is Corollary 2.5(b) on N = int Δ. (W6) follows from JJ2 Lemma 4.2(c),(d),
   whose proofs use only (W2), (W3), joint measurability, Fubini and convexity (written out in JJ3 Lemma 2.4).
4. **(W5).** Strict-best of Φ′ makes B^b the unique e_b-minimiser with a positive gap, so B′_w → B^b in measure as
   w → e_b, and K_w → {e_b}. Edge-confined limits: JJ2 Lemma 4.2(b), which uses (F1) of Φ′.
5. **(W4): T1 = B_{w*} with w* interior.** By (H4), T1 = C_{q₀} is L-competitive on supp q₀. II1 Prop 3.1(a)
   (Lyapunov convexity, separation, switching; PROVED there) gives α ∈ Δ_{supp q₀} at which T1 is pointwise weak α-Bayes
   for **Φ**. I show that α is interior.
   - **α at a vertex, say e₁.** Then T1 is φ₁-optimal. Consider the open set of pairs with majority orientation near
     (−1, N, N), N > (1 + ε/c₀)/2, where T1 gives M: min_k (c₀𝟙 + εe_k)·h = c₀(2N − 1) − ε > 0. There best₁ = O, so
     φ₁(M) = φ₁(O), and δ = φ(M) − φ(O) ≤ 0 at worlds 2, 3. That is a visible best-tie on a non-null set, which is
     excluded.
   - **α on an edge, say α₃ = 0.** Take the gambles near (1, 1, −t) with t slightly above 2c₀/(c₀ + ε), where T1 is
     silent (JJ2 Lemma 4.3). Weak Bayes needs α₁c₁ + α₂c₂ ≤ 0, with c := φ(S) − φ(M) and c₁, c₂ ≥ 0.
     - If α₁, α₂ > 0, this forces c₁ = c₂ = 0. Then δ = (0, 0, c₃) with c₃ ≤ 0, a visible best-tie at world 1.
       Excluded.
     - If α is a vertex, the previous case applies.
   - So α ∈ int Δ. With T*_α null, T1 is the unique α-minimiser of Φ (Corollary 2.5(a)), hence of Φ′ (step 2).
6. **Conclusion.** Φ′ satisfies (W1)–(W6) of JJ2 Definition 7.1. JJ2 Theorem 7.2 says that T1 has no such field. ∎

**Alternative route (PROVED modulo JJ3 §§3–5 with the AUDIT_JJ repair of Lemma 4.2 step 6, ccibu and Theorem gm).**
JJ3 §§3–5 use only these conclusions about the field:
- strict-best and × strictly worst;
- for every interior w, a.e. unique coherent Bayes models;
- T1 = B_{w*} with w* interior.

Steps 1–5 supply all three. This route also gives the theorem on every decomposable (LF) domain with (Av), provided
step 5's availability of acceptance near (1, 1, −t) is taken from (LF), as in JJ3 Prop 2.5.

**Remarks.**
- **What is used.** Theorem 2.4 (hence (H4) competitiveness and closed sections, (H5), (H6)), L-competitiveness of T1,
  and the imports named. (FC), (IB), transitivity and the form of k are not used.
- **What it closes.** Every non-protected rate design whose leading field has, at every interior weight, a null
  concurrent tie set and no visible best-ties. This includes designs whose non-protection comes from:
  - reindexing, i.e. C_p certified only at weights outside Δ_{supp p};
  - ties at boundary weights, i.e. bad~silence zeros;
  - invisible best-ties;
  - Ψ-broken ties of any kind that are not concurrent in the interior.
- **The exact reason, as the brief asks.** In these designs (★) and continuity do not "force protection back". (NT)
  can genuinely fail. What returns is the consequence of protection that JJ2/JJ3 actually used: interior Bayes rigidity.
  KKM, (C) and the lexicographic admissibility of chain models (Theorem 2.4) supply it directly.

---

## 5. Branch (BT): best-ties at a vertex

Fix the odd world o. Write Z for a non-null set of o-odd pairs (h_o < 0 < h_j, h_l) with φ_o(h, O) = φ_o(h, S). Such
ties are always visible: δ = φ(S) − φ(O) is ≤ 0 at j and l, and 0 at o. If φ_o(O) = φ_o(M), weak guidance puts S in
the tie as well.

**Theorem 5.1 (PROVED; the three items of the brief).** Let (H) hold on the full domain.
- **(i) Item 1.** (NT) fails at e_o against X0 := B^o with S on Z (Proposition 3.4).
- **(ii) Item 2.** z0 := rec(B^o, X0) has Φ_o = 0, Φ_j ≤ 0, Φ_l ≤ 0, Ψ_o > 0, Ψ_j < 0, Ψ_l < 0.
  - So z0 ∈ G(q) for every q ∋ o, and I^≥(z0) = {o}.
  - At e_o world o defends, and (★_{e_o}) holds with e_o.
- **(iii) Item 3, necessity.** Suppose (RB) holds, q ∈ Δ with o ∈ supp q, and C_q gives O on a non-null part of Z.
  Then C_q is pointwise φ_o-optimal. Hence there is a neighbourhood V of e_o in Δ such that every C_q with q ∈ V is
  pointwise φ_o-optimal.

*Proof.*
- **(ii)** Direct from the ranks. S is weakly better than O at j and l in φ (weak guidance) and strictly better in ψ.
  It is tied at o in φ, and strictly worse in ψ.
- **(iii)** The step O → S is an upward step, Φ_o-blind on Z. II2 Lemma 4.0 (PROVED there: the switched record is in
  G(q) with I^≥ = {o}, so (★_q) forces e_o ∈ W^Φ(q)) gives φ_o-optimality.
  - C_{e_o} = B^o gives O on all of Z.
  - Continuity in measure gives μ(Z ∩ {C_q ≠ O}) → 0 as q → e_o. So for q near e_o, C_q gives O on a non-null part
    of Z.
  - Every q near e_o has o ∈ supp q. ∎

*Cross-index form (II2 Prop 3.2).* Take z* = z0 and X* = X0, and let p_n → e_o. Then δ_n = (Φ_o(X0) − Φ_o(C_{p_n}))⁺ = 0,
because X0 is φ_o-minimal, and γ_n = Φ_o(C_{p_n}) − min Φ_o. So any sequence of selected models near e_o that pay an
improvable φ_o-cost defeats (RB) against the **fixed** competitor X0.

CHECKED (`vertex.py` → `vertex.out`, part A): with C_{p_n} paying φ_o-cost κ_n = 1/n, the transported record has size
1 + 1/n and r = n − 1, from 1 at n = 2 to 99 999 999 at n = 10⁸. Part B: each C_{p_n} is nevertheless lexicographically
competitive on an exact 9⁴ grid (0 points better at all worlds). The failure is one of uniformity, not of lexicographic
competitiveness.

**Proposition 5.2 (best-ties at a positive world; PROVED).** Let Z′ be a non-null set of pairs with odd world j ≠ o
(o a positive world) and φ_o(M) = φ_o(b), b ∈ {S, O}. Let q have supp q ⊆ {o, j} with o ∈ supp q, and suppose C_q
gives M on a non-null part of Z′. Then (RB) forces C_q to be φ_o-optimal. So the conclusion of Theorem 5.1(iii) holds
on a neighbourhood of e_o **within the edge** [e_o, e_j].

*Proof.* The switch M → b has Φ_o = 0 < Ψ_o, and Φ_j ≤ 0 > Ψ_j: b is better than M at the odd world j. So it lies in
G(q) for supp q ⊆ {o, j}, with I^≥ = {o}. II2 Theorem 3.1(b) applies. At interior q the record has Φ_l ≥ 0 at the
other positive world, and no constraint follows. ∎

**Proposition 5.3 (item 3, sufficiency; PROVED; CHECKED, `vertex.py` parts C, D).**
- (a) **Plateau.** If C_p = B^o for all p in a neighbourhood V of e_o, then r(p, X) = 0 for every p ∈ V and every X.
  So no (RB)-defeating sequence has its limit in V.
- (b) More generally, if (ND) of II1 holds at every point of V, with o ∈ W(p) by φ_o-optimality, then no defeating
  sequence has its limit in V.

*Proof.*
- **(a)** For X ≠ B^o, Φ_o(rec(B^o, X)) ≥ 0, by weak guidance. Also Ψ_o > 0, because B^o is pointwise ψ_o-best and
  differs from X on a non-null set. Hence r_o = 0.
- **(b)** This is II1 Theorem 3.2's proof, localised: a defeating sequence with limit p* violates (ND) at p*. ∎

CHECKED: the plateau has max r = 0 over an exact grid of 83 232 records. A φ_o-optimal model silent on half of Z has
max r = 0 at sizes ≥ 1/2, 1/4 and 1/16 (exact grids). So φ_o-optimality without a plateau can also be uniformly
defended.

**Proposition 5.4 (the collar forced by Theorem 2.4; PROVED; geometry CHECKED, `collar.py`).** Let (H) hold on the
full domain, with Z^vis_o non-null.
- (a) There are w, w′ ∈ int Δ such that X := lex-min(φ_o, w·φ, w′·ψ) differs from B^o on a non-null set Dev ⊆ Z^vis_o.
  X is a selected coherent model D_K with K ≠ {e_o}, and Dev = {D_K ≠ D_{e_o}} mod null.
- (b) For every credal set K ≠ {e_o}, the set {D_K ≠ D_{e_o}} contains a non-null open cone of o-odd pairs **and** a
  non-null open cone of pairs whose odd world is some j ≠ o.
- (c) Consequently, the visible best-ties of world o fill, mod null, open cones of both kinds. Best-ties of world o
  confined to one kind of pair, or to a set containing no open cone, are impossible.
- (d) Since o-odd visible best-ties are always of the type in Theorem 5.1, Theorem 5.1(iii) and Proposition 5.2 apply
  in every design of branch (BT) at world o.

*Proof.*
- **(a)** For h ∈ Z^vis_o, the set of interior (w, w′) for which the chain deviates from best_o at h is open and
  nonempty. Fubini over a countable dense family gives (w, w′) with a non-null deviation set.
  - The chain is admissible (s = 2). By Theorem 2.4, X is selected and coherent, X = D_K.
  - B^o = D_{e_o} a.e. So Dev = {D_K ≠ D_{e_o}} mod null, and K ≠ {e_o}.
  - On Dev, X's advice minimises φ_o, so it is a best-tie, visible by construction.
- **(b)** Take m ∈ K, m ≠ e_o, and let j ≠ o with m_j > 0. Write coordinates as (j, l, o).
  - **o-odd cone.** g = (1, η, −ζ) with 0 < ζ < m_j/m_o (any ζ if m_o = 0) and small η > 0. Then m·g > 0, so D_K does
    not accept −g, while D_{e_o} does. The strict inequalities persist on a neighbourhood.
  - **j-odd cone.** g = (−1, η, ζ) with η, ζ > 0 small enough that m·g < 0. Then D_K does not accept g, while D_{e_o}
    does (g_o > 0). Again an open set.
  - Both sets are cones by homogeneity.
- **(c)** Dev ⊆ Z^vis_o. ∎

CHECKED (`collar.py` → `collar.out`): 2996 random rational credal polytopes K ≠ {e_o}, with and without e_o. In every
case both witness boxes are certified exactly. A fixed vertex m of K gives linear inequalities, and these are checked at
all 8 corners of a box. 0 failures.

**Status of branch (BT).** Every design in (BT) at a world o must have all of the following:
- (1) visible best-ties of world o on open cones of both kinds, adjacent to the hyperplane {h_o = 0}. These are the
  disagreement regions of the coherent chain models of Proposition 5.4;
- (2) every selected model near e_o, and near e_o on the edges [e_o, e_j], pointwise φ_o-optimal, and agreeing with B^o
  off the best-tie set;
- (3) uniform defence near e_o, for which (ND) on a neighbourhood suffices (a plateau is one instance);
- (4) if no concurrent interior ties are present, an interior Φ-Bayes family that is unique, coherent, selected and
  continuous (Corollary 2.5). Its vertex limits are not B^o: on Z every interior w strictly prefers S to O, because
  w·δ < 0.

Whether JJ2 Theorem 7.2 survives this precise failure of (F1) and (W5) is the open point of §0. No member of (BT)
through T1 was constructed.

---

## 6. Branch (CT): concurrent leading ties at an interior weight

**Proposition 6.1 (fans; PROVED).** Let (H) hold with (CT) at w0.
- (a) T*_{w0} is, mod null, a countable union of disagreement sets of selected coherent chain models. Hence it is a
  non-null open cone.
- (b) For every admissible chain beginning with w0, the chain model is selected and coherent. All of them agree off
  T*_{w0}.
- (c) Directional models D^v := lex-min(w0·φ, v·φ, w′·ψ), v ∈ ℝ³, are among them. So the w0-section of the Φ-Bayes
  structure is a whole family of selected coherent models, indexed by v and w′.

*Proof.*
- **(a)** By the separation step of Proposition 3.3(a), a.e. h ∈ T*_{w0} lies in the disagreement set of two chain
  models from a countable family. Each such set is an open cone contained in T*_{w0} (F-b).
- **(b), (c)** Theorem 2.4, and Corollary 2.5(a)'s argument off T*_{w0}. ∎

**Item 2 for (CT) (PROVED).** Let p0 and X0 be as in Proposition 3.3, and z0 := rec(C_{p0}, X0). Then Φ(z0) = 0, and X0
is incoherent. By Lemma 2.3, Ψ_i(z0) > 0 at some world. This needs no rate at all: admissibility and (C) alone force the
lower level to defend C_{p0} somewhere.
- (RB) requires such a world inside supp p0.
- (★_{p0}) requires a weight of W^Φ(p0) supported in I^≥(z0) = {i ∈ supp p0 : Ψ_i(z0) ≥ 0}. Since C_{p0} is a
  w0-minimiser, w0 ∈ W^Φ(p0). So (★_{p0}) is automatic when I^≥(z0) = Ω, and otherwise needs a boundary weight in
  W^Φ(p0).

**Lemma 6.2 (item 3, a local sufficient condition; PROVED).** Assume every C_p is L-competitive on supp p. Let p* ∈ int Δ,
and suppose every non-null z ∈ G(p*) has Ψ_i(z) > 0 at **every** world. Call this strict unanimity (SU_{p*}). Then no
(RB)-defeating sequence has p_n → p*.

*Proof.*
- II2 Theorem 2.1 gives a limit record z* ∈ G(p*) with m(z*) ≥ a. It also gives Ψ_i(z*) ≤ 0 at every i where
  Φ_i(t_n) ≥ 0 infinitely often.
- By (SU_{p*}), Ψ_i(z*) > 0 at every i. So for large n, Φ_i(t_n) < 0 at all three worlds.
- supp p_n = Ω eventually. So t_n is a strict lexicographic improvement at every active world, which contradicts
  L-competitiveness of C_{p_n}. ∎

For a full-support w0-minimiser, G(p*) consists exactly of the Φ-null records supported on its w0-tie set: Φ(z) ≤ 0
and w0·Φ(z) ≥ 0 force Φ(z) = 0. So (SU) is a condition on the tie set alone. II2 Prop 3.2 has no bite at interior p_n
when I = Ω, because γ_n = 0 by L-competitiveness.

**Proposition 6.3 (a necessary pairwise criterion at every fan member; PROVED; CHECKED, `fan.py`).** Let (H) hold. Let
w0 ∈ int Δ, and let T_d ⊆ T*_{w0} be non-null, with the following structure:
- at each h ∈ T_d the w0-minimisers in {M, S, O} are exactly two advices a(h), b(h), labelled measurably;
- n(h) := φ(h,b) − φ(h,a) = λ(h) d, with λ > 0 and one fixed d ≠ 0 (necessarily d ⊥ w0, with mixed signs).

Put x(h) := (ψ(h,b) − ψ(h,a))/λ(h). Let x₁, x₂ be points of the essential range of x on T_d, and w′ ∈ int Δ with
w′·x₁ > 0 > w′·x₂. Put u := x₁ − x₂ and I_u := {i : u_i ≥ 0}. Then (RB) implies that the face Δ_{I_u} meets the chord
ℓ_d := {α ∈ Δ : α·d = 0}. Equivalently, none of the following holds:
- I_u = {k} with d_k ≠ 0;
- I_u = {i, k} with d_i, d_k of the same strict sign.

*Proof.*
1. **The fan member.** Y := B(w0; w′) is selected at some p (Theorem 2.4). On T_d it gives a where w′·x > 0 and b where
   w′·x < 0.
2. **The record.** For r > 0 small, let E₁ ⊆ T_d ∩ {|x − x₁| < r} and E₂ ⊆ T_d ∩ {|x − x₂| < r} be non-null, with
   ∫_{E₁} λ = ∫_{E₂} λ =: Λ. Lyapunov allows this, since μ is non-atomic. Switch a → b on E₁ and b → a on E₂, and call
   the record z.
   - Φ(z) = Λd − Λd = 0.
   - Ψ(z) = Λ(x̄₁ − x̄₂) with |x̄_k − x_k| < r, so Ψ_i(z) has the sign of u_i wherever u_i ≠ 0.
   - Hence z ∈ G(p), m(z) > 0, and I^≥(z) ⊆ I_u.
3. **(★_p).** II2 Theorem 3.1(b) gives α ∈ W^Φ(p) with supp α ⊆ I^≥(z) ⊆ I_u.
4. **W^Φ lies on the chord.** Out of Y, switching a → b on a non-null part of T_d gives δφ = λd, so α·d ≥ 0. Switching
   b → a gives −λd, so α·d ≤ 0. Hence α ∈ ℓ_d.
5. **The faces meeting ℓ_d.** ℓ_d contains the interior point w0 and meets an edge {i, k} iff d_id_k ≤ 0, and a vertex
   e_k iff d_k = 0. ∎

CHECKED (`fan.py` → `fan.out`). Zonotope surrogates with regions of measure 1 and exact increments. In each, the fan
members realised by interior w′ are enumerated, checked to be L-undominated on an exact grid (as Theorem 2.4 requires),
and tested for (★).
- **P1** (d = (1, 0, −1), two regions with opposite tie directions). The mixed member has Φ-null records with
  Ψ = (1, 3, 2) > 0: strict unanimity, (★) holds.
- **P2** (same d, another ψ). Ψ = (−1, 3, 0) and I^≥ = {1, 2}. The face meets ℓ_d at e₁, but W^Φ(Y) excludes e₁ because
  of a third region. So (★) fails. The explicit segment of II2 Theorem 3.1(a) gives r = 31/3, 391/3, 39 991/3,
  399 999 991/3 at s = 10⁻¹, 10⁻², 10⁻⁴, 10⁻⁸, with size ≥ 9/5.
- **P3** (d = (1, 1, −2), two regions with the same tie direction and x = (4, 4, −3), (1, 1, −2)). u = (3, 3, −1) and
  I_u = {0, 1}, with d₀d₁ > 0. So the criterion of Proposition 6.3 itself fails. The segment gives r = 17, 197, 19 997,
  199 999 997 at size ≥ 9/5.

**Corollary 6.4 (single-atom concurrent ties are excluded; PROVED).** Let (H) hold with (CT) at w0, where T*_{w0} = T_d
is as in Proposition 6.3, and x is essentially constant, x = x⁰ a.e. on T_d. Then there is no rate cover.

*Proof.*
1. **The two fan members.** x⁰ has strictly mixed signs, so interior w′ with w′·x⁰ > 0 and with w′·x⁰ < 0 both exist.
   The fan members are B₁ = "a on T_d" and B₂ = "b on T_d". Both are selected and coherent.
2. **C_{p0} mixes.** Proposition 3.3(c) with this pair gives C_{p0}, a w0-minimiser with Φ(C_{p0}) = Φ(X0).
   - Then ∫_{C_{p0} = b} λ = ∫_{T_d ∖ A} λ, which lies strictly between 0 and ∫_{T_d} λ. Both T_d ∩ A and T_d ∖ A are
     non-null, because T_d is a non-null open cone (Proposition 6.1(a)).
   - So C_{p0} gives a on a non-null part of T_d and b on another.
3. **The record.** Take bounded non-null E₁ ⊆ {C_{p0} = b}, E₂ ⊆ {C_{p0} = a} with ∫_{E₁} λ = ∫_{E₂} λ. Switching both
   gives Φ = 0 and Ψ = (∫_{E₂} λ − ∫_{E₁} λ)x⁰ = 0. This is a bounded non-null lexicographic tie with a selected model,
   which contradicts Lemma 2.3(b). ∎

**Status of branch (CT).** A design in (CT) at w0 needs all of the following:
- an open cone of concurrent ties carrying a fan of selected coherent chain models;
- for every tie type and every interior w′, normalised lower increments x satisfying Proposition 6.3. If the essential
  range of x on some T_d has an interior point x*, the criterion fails (PROVED from Proposition 6.3).
  - x* has strictly mixed signs, since the essential range avoids the open orthants. So w′·x* = 0 for some interior w′.
  - Choose u with a single nonnegative coordinate k, d_k ≠ 0, and w′·u > 0, and put x₁,₂ := x* ± ρu/2 for small ρ.
  - Since Ψ is free, the designer must keep that range thin;
- x not essentially constant on any single-type tie set that is all of T*_{w0} (Corollary 6.4), and more generally no
  bounded Φ-null, Ψ-nonpositive record out of any selected model (Lemma 2.3);
- (★) at the definite index p0 of Proposition 3.3;
- uniformity, for which strict unanimity at interior indices suffices (Lemma 6.2).

The gm chain's continuity input (W3) fails here at w0 by construction, so Theorem 4.1's route does not apply. No member
through T1 was constructed, and no exclusion of the whole branch is claimed.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 2.2 | chain models (interior φ-weight, interior ψ-weight) are L-undominated | PROVED; CHECKED (`lexchain.py`, 1500 instances, controls) |
| 2.3 | no non-null Φ-null record out of a selected model is Ψ-nonpositive; bounded or incoherent lex ties excluded by (C) | PROVED |
| **2.4** | **in every rate cover, every admissible chain model is a.e. unique, coherent and selected** | **PROVED** |
| 2.5 | null concurrent ties at w ⇒ Φ-Bayes model there is the selected B_w; Hausdorff continuity on such open sets | PROVED |
| 3.1 | non-protection runs along ties at every Bayes weight | PROVED |
| 3.3 | (CT) ⇒ a definite p0 and an incoherent X0, Φ-tied with C_{p0} at all worlds | PROVED |
| 3.4 | (BT) ⇒ (NT) fails at e_k against B^k switched to the tied advice; world k defends; (★_{e_k}) | PROVED |
| **4.1** | **every rate cover of T1 on the full domain is in (CT) or (BT)** | **PROVED mod JJ2 Thm 7.2 (gm short route; Table 7.2 pending KK1); or mod JJ3 §§3–5 + ccibu + gm** |
| 5.1 | (BT) odd-world tie: items 1–3; φ_o-optimality forced near e_o | PROVED (imports II2 Lemma 4.0); CHECKED (`vertex.py` A, B) |
| 5.2 | positive-world best-ties: φ_o-optimality on the edges near e_o | PROVED |
| 5.3 | plateau / local (ND) suffices near e_o | PROVED; CHECKED (`vertex.py` C, D) |
| 5.4 | collar: best-ties of world o fill open cones of both kinds | PROVED; CHECKED (`collar.py`, 2996 cases) |
| 6.1 | concurrent tie set is an open cone carrying a fan of selected models | PROVED |
| 6.2 | strict unanimity at an interior index excludes defeating sequences there | PROVED |
| 6.3 | pairwise criterion for (★) at fan members | PROVED; CHECKED (`fan.py` P1–P3) |
| 6.4 | single-atom concurrent ties excluded by (C) | PROVED |
| — | (BT) with no concurrent ties | **open: the §0 point** |
| — | (CT) in general | **open** |
| — | cover of T1 | **not obtained** |

**Which non-protected designs remain (precisely).** Within the rate class on the full domain, these are the designs that
satisfy (CT) or (BT), and in addition:
- in (BT), the collar and φ_o-optimality structure of §5;
- in (CT), the fan, pairwise and (C) constraints of §6.

Outside the rate class nothing new is claimed: other rules, general (FC) rankings, the clone route, and non-(Av) domains
(KK3).

**Referee priorities.**
1. Lemma 2.2, step 1: the weights before the interior one must be nonnegative. Arbitrary vectors are allowed only after
   it. The ψ-weight must be interior, or the last-level ties must be null.
2. Theorem 2.4, step 2: the splice of two λ-models is a λ-model. This is decomposability of the pointwise minimiser
   class.
3. Theorem 4.1, step 5: the two exclusions of boundary weights for T1 use only "no visible best-ties", not strict-best.
4. Theorem 4.1, step 1(iii): raising invisible tied advices changes no interior minimiser set, and keeps weak guidance.
5. Proposition 5.4(a): the deviation set equals the disagreement set of D_K and D_{e_o}, and it lies inside Z^vis_o.
6. Proposition 3.1: at an interior weight with null concurrent ties, the only possible ties are trivial blind switches
   (unanimous pairs, ×), and these are defended at every world.

## 8. Files (`kk4py/`)

- `common.py`: cell surrogate, world ranks, weakly and strictly guiding penalties, lex-min, L-domination, the rate r.
- `zono.py`: zonotope surrogate (records as mass-weighted switches), exact grid scans.
- `lexchain.py` → `lexchain.out`: Lemma 2.2. Exhaustive L-domination search for five admissible chain shapes, with
  planted concurrent ties and best-ties; controls showing that the interior φ-weight and the ψ-level are needed.
- `vertex.py` → `vertex.out`: Theorem 5.1 and Proposition 5.3. The transported vertex competitor with r = n − 1;
  lexicographic competitiveness of each C_{p_n}; plateau r ≡ 0; a φ_o-optimal non-plateau model with r = 0 on grids.
- `collar.py` → `collar.out`: Proposition 5.4(b). Certified open witness boxes of both kinds for 2996 credal sets.
- `fan.py` → `fan.out`: Proposition 6.3. Fan members of three surrogate designs, their (★) status, and exact defeating
  segments for P2 and P3.
