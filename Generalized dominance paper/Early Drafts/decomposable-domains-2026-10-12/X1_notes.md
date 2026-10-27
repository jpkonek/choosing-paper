# X1. Joint three-world partial systems: the transition lemma, natural extension, and an exact extension theorem

16 Oct 2026 (round 26, BRIEF18). Labels: **PROVED** (full proof here), **CHECKED** (exact finite computation or verification against cited statements; the computation is reproducible), **CONJECTURE**, **NUMERICS** (sampling; no proof depends on it). Scripts are in `x1py/`; run each with `python3 -I <script>` from inside `x1py/`; outputs are in the matching `.out` files.

**Sources read.**
- BRIEF18 and AUDIT_nonlinear_programme.md (transition records, transition lemma, (K), the extension lemma to pursue).
- Write-up §2: axioms, domains, the four kinds of advice, (LF), the U-domain.
- *Coverage after Neutral Abstention* §3: Thm closure, the exact consistency test.
- *Vacuous Targets and Transfinite Construction* §5: the union lemma and the reserved-neighbourhood proposition.
- P3_notes.md: Thm 3.1 with the limit rule R5; Thm 4.1 on compactness; Example 1 (per-model reservations); Example 2 (an extendable ω-chain whose union is dead); the witnessed theorem 7.1.

**Not read.** Both literature URLs were refused by the fetch tool (provenance block):
- Miranda–Zaffalon, https://people.idsia.ch/~zaffalon/papers/2023ijar-ndt.pdf;
- De Cooman–Van Camp–De Bock, https://users.ugent.be/~jdbock/documents/GdC-2024-IJAR-paper.pdf.

I therefore use only the audit's description of them. In particular, "DVB Thm 31/Cor 32" refers to the following: finite consistency implies consistency for disjunctive assessments when the underlying closure is finitary, and fails otherwise. Nothing below depends on those papers: every finite-to-full consistency step I need is proved here directly by propositional compactness (Prop. X1.3.2).

**Setting.** As in the write-up:
- three worlds Ω = {1, 2, 3}, and in code {0, 1, 2};
- models are measurable sets modulo μ-null sets;
- the four kinds of advice are + (accept f), − (accept −f), 0 (silence) and × (contradictory);
- the world-i background order is good ≺ silence ≺ bad ≺ contradictory.

The rank rk_i(f, a) ∈ {0, 1, 2, 3} is the position of advice a in that order at f. It is defined off the null hyperplane f_i = 0, and it is injective in a.

---

## 0. Outcome

1. **The transition lemma is correct** (Thm X1.1.1, PROVED) on the full four-advice domain and on every decomposable domain with measurable advice ranges. There is no substantive gap. The audit's proviso that "every composition must be realizable" is automatically satisfied: composable realizable records are always jointly realizable (Lemma X1.1.2). Two minor corrections: condition 3 comes from weak (G), not from reflexivity; condition 4 is exactly strict (G), because rk_i(f, ·) is injective.

2. **Joint partial systems and their natural extension** are defined in §2. A partial system consists of a revisable coherent selection, world-labelled accepted and rejected record sets, unresolved (K)-disjunctions, protection (R4), the (C)-tie ban, and open reservations. The legitimate rules are identity, realizable composition, protection, and either the limit rule R5 or a plan rule. Positive linear closure is not a legitimate rule.

3. **Extension theorem (Thm X1.3.3, PROVED).** Fix the selection C, and fix a **plan** V: an open neighbourhood V(p, i, X) ∋ p for every section triple, reserved in advance. Then the invariant

   INV(L; V): Θ_C ∪ Plan(V) ∪ L is finitely satisfiable

   is explicit, finitary, and exact:
   - (a) the next (K)-disjunction can always be met at some world of supp p;
   - (b) protected coherent models stay protected;
   - (c) the invariant survives unions of chains, and the final system has closed sections, with no limit rule needed;
   - conversely, every successful system containing L satisfies INV(L; V) for its own plan.

   Fixing the plan replaces the non-finitary rule R5 by binary Horn clauses. This restores the finitary hypothesis that the audit attributes to DVB Thm 31/Cor 32. P3 Example 2 is exactly the failure of that hypothesis under R5. With a plan fixed in advance, the same bad choice is refuted at a finite stage. Corollary X1.3.5 (ultralimits under a shared plan) turns this into a construction tool.

4. **The crossing configuration** (§§4–5) has three worlds, three balls with crossing error sets, the precise (Brier) selection D_q (which covers every precise target), and interior selected models.
   - **Dead crossing triple (Thm X1.5.1, PROVED).** Three crossing trades, one at each world, have a *clean* natural extension under composition and the limit rule. Every two of them lie in a successful common-density Brier system. Yet the next competitiveness disjunction, out of the interior model D_u, **cannot be met at any world**. The reason is that the three trades already make D_u strictly dominated. Protection (R4) detects this. So "clean under composition closure" is **not** a sufficient invariant; protection must be part of the natural extension.
   - **Rigidity of minimal resolutions (Prop. X1.5.2, CHECKED exactly).** The finite crossing fragment has exactly 90 minimal models. Each is contained in a common-density Brier ranking, with positive margins verified in exact rational arithmetic for a = 1/20, 1/5, 3/10, 9/20. So INV holds with an explicit plan for every minimal resolution: crossing alone never *forces* leaving the additive class. Non-minimal models that no common-density Brier ranking contains do exist (Prop. X1.5.3, CHECKED).
   - **Is "clean natural extension *with* protection" sufficient?** In the fragment, **no**. State S4 is four records whose closure under (P), (Σ), (R4) is clean, yet the disjunction for silencing two pieces out of D_u has no admissible world (Prop. X1.5.4). The three refutations are real derivations (PROVED). Whether S4's *real* natural extension is clean is open, giving a precise dichotomy:
     - either real protection at selected models whose boundaries cross the pieces is strictly stronger than protection against whole-piece competitors;
     - or S4 is a real counterexample.

     S4 admits no certificate of the natural "one pointwise world" type (Prop. X1.5.5, PROVED). Constructions that add only (K)-resolutions never got stuck in 3000 random runs (NUMERICS).

---

## 1. The transition lemma, verified

**Records.** Let M be a decomposable domain with advice range A(f) ⊆ {+, 0, −, ×}. A **transition record** is a measurable map r on H with, for a.e. f, either r(f) = ι or r(f) = (x, y) with x ≠ y and x, y ∈ A(f). Records are taken modulo null sets. The record of an ordered pair (X, Y) of models is rec(X, Y)(f) = (a_X(f), a_Y(f)) where the advice differs, and ι otherwise. The records arising from pairs of evaluable models are exactly the realizable records. To realise r:
- put X = x and Y = y where r(f) = (x, y);
- on the set {r = ι}, fill both with a measurable selection of A(f), for example the first available value in a fixed order.

The reverse r⁻¹ swaps each pair. The pair r, s is **composable** if r(f) = (x, y) and s(f) = (y′, z) imply y = y′ a.e. where both are nontrivial. Their composite r∘s is then:
- (x, z) if x ≠ z, and ι if x = z, where both are nontrivial;
- r(f) where only r is nontrivial, and s(f) where only s is nontrivial.

The record r is **i-worsening** if rk_i(f, y) ≥ rk_i(f, x) a.e. on {r ≠ ι}, and **i-improving** if ≤ holds there.

**Lemma X1.1.2 (PROVED).** On a decomposable domain:
- (i) X ⪯ Y in a preorder satisfying (IB) depends only on rec(X, Y);
- (ii) every composable pair of realizable records r, s is realised by a triple X, Y, Z of evaluable models, with rec(X, Y) = r, rec(Y, Z) = s and rec(X, Z) = r∘s;
- (iii) rec(X, Z) = rec(X, Y)∘rec(Y, Z) for all X, Y, Z, and this pair is always composable.

*Proof.*
- (i) Let (X, Y) and (X′, Y′) have the same record r. Let A := Z ∪ −Z, where Z is the support of r (a measurable symmetric set). Off A, X agrees with Y, and X′ agrees with Y′. On A, X agrees with X′ and Y with Y′, since a common record fixes the advice on both orientations. Put F := X ∖ A and G := X′ ∖ A. Then (X, Y) = ((X∩A)∪F, (Y∩A)∪F) and (X′, Y′) = ((X∩A)∪G, (Y∩A)∪G). (IB) gives the equivalence, and all four models are the given evaluable ones.
- (ii) Define the three models pointwise.
  - Where r(f) = (x, y) and s(f) = (y, z), put X = x, Y = y, Z = z.
  - Where r(f) = (x, y) and s(f) = ι, put X = x and Y = Z = y.
  - Where r(f) = ι and s(f) = (y, z), put X = Y = y and Z = z.
  - Elsewhere, use the measurable selection.

  Every value used lies in A(f), because x, y, z each occur in a realizable record at f. The models are measurable, so they are evaluable by Remark advicerange.
- (iii) Compare pointwise. ∎

**Theorem X1.1.1 (transition lemma; PROVED).** For a world i and a set A_i of realizable records, define X ⪯_i Y :⟺ rec(X, Y) ∈ A_i. This is a preorder satisfying (IB) and strict (G) if and only if:
1. ι ∈ A_i;
2. A_i is closed under composition of composable pairs;
3. every i-worsening realizable record is in A_i;
4. no nontrivial i-improving record is in A_i.

Every preorder satisfying (IB) and strict (G) arises in this way, from A_i := {rec(X, Y) : X ⪯_i Y}.

*Proof.* (⇐)
- Reflexivity follows from 1. Transitivity follows from 2 and Lemma X1.1.2(iii). (IB) holds because the two pairs in an (IB) instance have equal records.
- Weak (G): if X is at least as good as Y at world i a.e., then rec(X, Y) is i-worsening and so lies in A_i by 3.
- Strict (G): suppose X is moreover strictly better on a non-null set. Then rec(Y, X) is i-improving, and nontrivial on that set. By 4, rec(Y, X) ∉ A_i, so not Y ⪯_i X.

(⇒)
- A_i is well defined by Lemma X1.1.2(i).
- Condition 1 is reflexivity, and condition 2 is transitivity together with Lemma X1.1.2(ii).
- Condition 3 is weak (G) (the audit cites reflexivity here; it should be weak (G)).
- Condition 4: rk_i(f, ·) is injective off a null set. So a nontrivial i-improving record r = rec(Y, X) is strictly improving on {r ≠ ι}, which is non-null, and strict (G) forbids Y ⪯_i X. ∎

**Remarks (CHECKED by direct comparison with the cited texts).**
- *On the U-domain*, the advice range on U-orientations is {+, 0}. Records are the ternary functions σ, and composability means that σ + τ is ternary. This recovers the normal form (P), (N), (Σ) of P3 §2.
- *Records are richer than rank changes.* At every f and every world, (+→0) and (0→−) have the same rank change. Yet the lemma lets A_i treat them differently, as in non-equally spaced penalties: two grades of error per world, as in M3.
- *What is not legitimate.* The lemma gives closure under composition only. It does not give closure under sums of non-composable records, or under positive multiples. This is the audit's point: posi-closure would count an error repeatedly and corresponds to no chain of models.
- *World coupling.* The same record set is evaluated at every world; the worlds differ only through rk_i. Nothing in the lemma couples worlds. All coupling enters through (K), (R4), (C) and the sections.

---

## 2. Joint partial systems and their natural extension

Fix M (the full domain or an advice-range domain). Write 𝓡 for the realizable records, and use variables x_{i,r} meaning r ∈ A_i, for i ∈ Ω and r ∈ 𝓡.

**Definition X1.2.1 (partial system).** A partial system 𝔓 = (C, L, V) consists of:
- a coherent selection p ↦ C_p ∈ M on Δ. It may be **revised** between stages. Records, and hence L, are selection-independent: only the clauses below depend on C, so a revision keeps L and changes the theory;
- a set L of world-labelled literals: accepted records x_{i,r} and rejected records ¬x_{i,r};
- a **reservation plan** V, which may be partial: for some triples t = (p, i, X), an open set V(t) ∋ p (relatively open in Δ). It means: if the comparison C_p ⪯_i X is rejected, then every comparison C_q ⪯_i X with q ∈ V(t) is rejected.

Write r_q^X := rec(C_q, X) and d_{q,p} := rec(C_q, C_p). Then r_q^X = d_{q,p}∘r_p^X, and this pair is composable.

**The clauses Θ_C** (every axiom except closed sections):
- (Bg) x_{i,r} for every i-worsening r;
- (N) ¬x_{i,r} for every nontrivial i-improving r;
- (Σ) ¬x_{i,r} ∨ ¬x_{i,s} ∨ x_{i,r∘s} for composable r, s;
- (K) ⋁_{i∈supp p} x_{i, r_p^X} for every p and X. This is the disjunctive assessment, kept unresolved;
- (R4) ⋀_j x_{j, (r_p^X)⁻¹} → x_{i, r_p^X} for every p, X, i. This is protection: X ⪯ C_p at every world forces C_p ⪯ X at every world;
- (Csel) ¬⋀_j (x_{j,r_p^X} ∧ x_{j,(r_p^X)⁻¹}) for every p and every incoherent X. This is the (C)-tie ban.

**Closed sections as open neighbourhoods of rejections.** The section {q : C_q ⪯_i X} is closed iff every rejected comparison has a neighbourhood of rejected comparisons. Two clause families express this:
- the **limit rule R5**: ⋀_k x_{i, r_{q_k}^X} → x_{i, r_p^X} whenever q_k → p. It is infinitary;
- the **plan clauses** Plan(V): ¬x_{i, r_q^X} ∨ x_{i, r_p^X} for every q ∈ V(p, i, X). They are binary Horn clauses.

By transport (P3 Lemma 2.1), rejecting r_q^X at world i rejects that record at every base point q′ ∈ Comp(r_q^X). So a reservation is a set of rejected *records*, and P3 Example 1's transport is built in.

**Definition X1.2.2 (natural extension; consistency).** The **legitimate rules** are:
- R1: identity, (Bg);
- R2: realizable composition, (Σ);
- R4: protection;
- and either R5, or the plan rule for a given V.

The rules R1–R4 are exactly the rules of *Coverage after NA* Thm closure. Its third rule, (IB)-transfer, is absorbed into records by Lemma X1.1.2(i).

For a set L⁺ of accepted world-labelled records, the **natural extension** E_V(L⁺) is the least superset of L⁺ closed under the legitimate rules. Write E_4 when the plan rule is omitted and E_5 when R5 replaces it. It exists by Knaster–Tarski.

E(L⁺) is **clean** if:
- it contains no (N)-record;
- it contains no (Csel)-tie;
- it contains no record rejected in L, either explicitly or through V.

This is the Miranda–Zaffalon pattern: a closure operator, a forbidden set, and a natural extension that exists iff the closure avoids the forbidden set. The (Csel)-tie is a forbidden *conjunction*; encode it as a rule producing ⊥.

The partial system is **K-consistent** if some clean, closed, complete assignment contains L and satisfies every (K) clause. This is the desirable-sets-of-things notion: (K) is a set of "things" of which at least one must be accepted, and a clean closed complete assignment is a conjunctive model. It is **finitely K-consistent** if this holds for every finite subset of the clauses.

**What "natural extension" does *not* include.** It includes no positive linear closure. It also makes no choice of a world for a disjunction: (K) stays an assessment, not a rule.

---

## 3. The extension theorem

**Lemma X1.3.1 (PROVED).**
- Θ_C, Plan(V) and the Horn rules R1, R2, R4 and the plan rule are finitary: each clause has at most four literals.
- R5 is not finitary. It is genuinely infinitary: P3 Example 2 gives literals {x_{1, r_{r_k}^X}}_k such that every finite subset extends to a successful system, which is a model of Θ_C ∪ R5, while the whole set together with R5 derives the (N)-outcome B_{p0} ⪯_1 X.

*Proof.* Count the literals in each clause. The second part is P3 §6.2 verbatim; there, every finite stage lies in a Brier system Ψ^{ρ_m} with the same selection. ∎

This is the phenomenon the audit attributes to DVB §2.4: under a non-finitary closure, finite consistency does not imply consistency.

**Proposition X1.3.2 (finitary consistency; PROVED).** For a fixed C and a fixed plan V, the following are equivalent:
- (i) Θ_C ∪ Plan(V) ∪ L is satisfiable;
- (ii) it is finitely satisfiable;
- (iii) the partial system is K-consistent with respect to E_V.

*Proof.* (i) ⟺ (ii) is the compactness theorem of propositional logic, for any cardinality of variables. (i) ⟺ (iii): a satisfying assignment is a clean complete assignment closed under the Horn rules and meeting every (K) clause, and conversely. ∎

**Theorem X1.3.3 (plan extension theorem; PROVED).** Fix a decomposable domain M, a coherent selection C and a plan V defined for every triple. Suppose INV(L; V) holds, that is, Θ_C ∪ Plan(V) ∪ L is finitely satisfiable. Then:
- **(a) next disjunction.** For every (p, X) there is i ∈ supp p such that INV(L ∪ {x_{i, r_p^X}}; V) holds. Moreover, for every triple t = (p, i, X), at least one of the following holds:
  - INV(L ∪ {x_{i, r_p^X}}; V);
  - INV(L ∪ {¬x_{i, r_q^X} : q ∈ V(t)}; V), that is, reject at p together with the whole reserved neighbourhood.
- **(b) protection.** Every assignment satisfying the invariant satisfies (R4). So every selected C_p, including the target, is undominated, and no incoherent model ties a selected one.
- **(c) limits.** If (L_α) is an increasing chain with INV(L_α; V) for all α, then INV(⋃_α L_α; V) holds.
- **(d) the end.** Every maximal L with INV(L; V) exists by (c) and Zorn's lemma. It is a complete assignment and defines a **successful system**: preorders satisfying strict (G), (IB), (LA), competitiveness on supp p, closed sections for every evaluable X, and (C) for every coherent undominated model.
- **(e) exactness.** Conversely, let (⪯_i) be a successful system for C containing L. Define V(p, i, X) := Δ ∖ A_i(X) if C_p ⋠_i X, and V(p, i, X) := Δ otherwise. Then INV(L; V) holds. Hence a successful system for C exists iff some plan V makes Θ_C ∪ Plan(V) finitely satisfiable.

*Proof.*
- (a) By Prop. X1.3.2 there is a model 𝔐 of Θ_C ∪ Plan(V) ∪ L. By (K) it accepts r_p^X at some i ∈ supp p, and L ∪ {x_{i,r_p^X}} ⊆ 𝔐. For the second part, take the same model 𝔐. Either it accepts r_p^X at world i, or it rejects it. In the latter case the plan clauses ¬x_{i,r_q^X} ∨ x_{i,r_p^X} make it reject r_q^X at world i for every q ∈ V(t).
- (b) (R4) and (Csel) are clauses of Θ_C.
- (c) A finite subset of the union lies in a single L_α.
- (d) Fix a maximal L. By compactness Θ_C ∪ Plan(V) ∪ L has a model 𝔐, and maximality forces L = 𝔐. Define X ⪯_i Y :⟺ rec(X, Y) ∈ A_i := {r : x_{i,r} ∈ 𝔐}. Then:
  - Theorem X1.1.1 gives preorders with strict (G) and (IB);
  - (K) gives competitiveness on supp p;
  - (R4) makes each C_p undominated, so (LA) holds;
  - closed sections: if p ∉ A_i(X), the plan clauses give V(p, i, X) ∩ A_i(X) = ∅. So the complement of each section is open (Vacuous Targets, Prop. "sufficient invariant");
  - (C): by the KKM theorem (write-up Thm kkm, which needs only (LA) and (S)), every coherent undominated B ties at every world with some selected C_p. A model tied everywhere with B ties with C_p, so by (Csel) it is coherent. It is also undominated, by the argument of P3 Thm 3.1(1).
- (e) The successful system satisfies Θ_C, since every clause is one of its axioms (R4 by undominatedness, (Csel) by (C)). It satisfies Plan(V) because sections are closed and the complement of a closed section is open. ∎

**What the theorem does and does not do.**
- It is the extension lemma requested in the brief:
  - the invariant is explicit, as finite satisfiability of a fixed finitary theory;
  - violations have **finite certificates**, namely a finite unsatisfiable subset;
  - it guarantees (a)–(c);
  - the reserved open neighbourhoods are part of the data, not a consequence of a limit rule.
- It is **exact**, so it cannot manufacture a cover where none exists. The whole difficulty is concentrated in one object, the plan V, which must be chosen with foresight.
  - *Example.* P3 Example 2 violates every plan with V(p0, 1, X) ∌ r_k for large k. Once V is fixed, the bad choice x_{1, r_{r_k}^X} with r_k ∈ V(p0, 1, X) is refuted at a finite stage, because the plan clause gives x_{1, r_{p0}^X}, which (N) forbids.
- Compared with P3 Thm 3.1, which uses a choice κ and R5: here the theory is finitary once V is fixed, so DVB-type finite-to-full consistency holds (Prop. X1.3.2). The cost is the plan.
- **Selection revision.** For a fixed plan, the theorem needs a fixed selection.
  - Making the selection a variable would require a disjunction over the continuum of coherent models available at each p. Such a disjunction is not a finite clause, so compactness is lost again.
  - A revision between stages is legitimate: L is selection-independent. INV must then be re-established for the new Θ_C.

**Corollary X1.3.4 (where plans are automatic; PROVED).** Suppose that at a triple (p, i, X) we have C_p ⪯_i C_q for all q in some neighbourhood W of p. Then every plan clause with V(p, i, X) ⊆ W is a consequence of (Σ):

x_{i,(d_{q,p})⁻¹} ∧ x_{i, r_q^X} → x_{i, r_p^X}.

So plans are needed only where C_p is not locally weakly optimal at world i along the selection. *Proof.* r_p^X = (d_{q,p})⁻¹∘r_q^X, so the clause is an instance of (Σ). ∎

**Corollary X1.3.5 (ultralimits under a shared plan; PROVED).** Let (S_α) be successful systems for the same selection C. Suppose they share a plan, in the sense of *uniform rejection*: for every triple (p, i, X) there is an open V ∋ p such that every S_α rejecting C_p ⪯_i X rejects C_q ⪯_i X for every q ∈ V. Then for every ultrafilter 𝒰 on the index set, the ultralimit

x_{i,r} := [{α : x^α_{i,r}} ∈ 𝒰]

is a successful system. The same holds if each finite subset of Θ_C ∪ Plan(V) is satisfied by 𝒰-almost all S_α, which need only be partial assignments.

*Proof.* Every clause of Θ_C ∪ Plan(V) is finite. If each disjunct fails on a set outside 𝒰, the clause fails on a set in 𝒰, a contradiction. Then apply Thm X1.3.3(d). ∎

*Remarks.*
- If the S_α are additive with weights ν_α, then by Łoś's theorem the ultralimit accepts a record at world i iff the ultraproduct weight satisfies ν*_i(r) ≥ 0. Here ν* is hyperreal-valued and positive on non-null sets. So the ultralimit is hyperreal-additive and admits no finite (M1) certificate (PROVED: a certificate would be a non-null function ≤ 0 with ν*-value ≥ 0). It need not add up with a real weight. I do not develop which case occurs.
- Uniform rejection is the precise condition under which such gluing keeps closed sections.
- For families Ψ^{ρ_n} → Ψ^ρ (giving lexicographic limits) it fails, because the gaps ψ_i(C_p) − ψ_i(X) > 0 shrink to 0. This agrees with the lexicographic failures N9.6 FC, R2 Prop 8, and R3 Thm L.
- I make no claim that a family with a shared plan exists for T1.

**Corollary X1.3.6 (the T1 problem in finitary form; PROVED from X1.3.3).**
- T1 is covered on a decomposable domain with (LF) at T1 iff there are a coherent selection C with T1 = C_{p*} and a plan V such that every finite subset of Θ_C ∪ Plan(V) is satisfiable.
- Each finite subset mentions finitely many records, base points and competitors.
- The open question is therefore the existence of a *uniform* plan compatible with all finite fragments. Neither Thm gm nor M0closed addresses fragments.

---

## 4. The crossing configuration (full advice domain, precise selection)

**Setting.**
- Fix a ∈ (0, ½) and θ := a/(1+a) < ⅓.
- Put h^{(k)} := e_k − a(𝟙 − e_k), so h^{(k)}_k = 1 and h^{(k)}_j = −a for j ≠ k.
- Let π_k := the closed ball B(h^{(k)}, δ), with 0 < δ small enough that the ball lies in the open orthant {h_k > 0, h_j < 0 (j ≠ k)}.
- So the world-j sign of every point of π_k is + iff j = k: piece π_k is "good to accept" only at world k.
- Pairs meeting the pieces are indexed by their orientation in π_k, and advice is read for that orientation.

**Selection and ranking.**
- The selection is D_q := {h : q·h > 0} (precise, coherent, continuous in measure in q).
- The Brier penalties are ℓ_j(h, a) := (rk_j(h, a) − 1)|h_j| for a ∈ {+, 0, −}, and ℓ_j(h, ×) := 2|h_j|.
- For every bounded measurable ρ > 0, the ranking Ψ^ρ_j(X) := ∫ ℓ_j(h, a_X(h)) ρ dμ with selection D_q is a **successful system** on the full domain. It covers every precise target D_p.

This is CHECKED: P3 §7 lists it among the known covers, and I re-verified each item.
- Strict (G): ℓ_j is strictly increasing in rank.
- (IB): additivity.
- The unique q-Bayes advice is sign(q·h). The values are q·ℓ(+) = −q·h, q·ℓ(−) = q·h, q·ℓ(0) = 0, and q·ℓ(×) ≥ 2|q·h|, and {q·h = 0} is null for every q ∈ Δ.
- This uniqueness gives competitiveness, undominatedness (also at boundary q) and (C).
- Dominated convergence gives closed sections.
- (LF) holds trivially on the full domain.

**Exact piece weights.** If ρ = m_k/φ on π_k, where φ is the Gaussian density, and ρ = 1 elsewhere, then

∫_{π_k} ρ |h_j| dμ = m_k·vol(π_k)·|h^{(k)}_j|,

exactly: |h_j| is linear on the ball, so it averages to its centre value. So the world-j value of a whole-piece record r is vol·Σ_k Δ_{jk}(r) m_k A_{jk}, where Δ_{jk}(r) is the rank change on π_k at world j, A_{jj} = 1, and A_{jk} = a for k ≠ j.

**Patterns.**
- D_q accepts the whole of π_k iff q·h > 0 on π_k, approximately q_k > θ. It accepts −π_k iff q·h < 0 there.
- The whole-piece patterns are s ∈ {+, −}³ ∖ {−−−}; (+++) occurs because 3θ < 1.
- The smallest support of a q with pattern s is Plus(s) := {k : s_k = +}. Every superset also occurs, including interior q.

**Crossing.** Take τ := (+→0) on all three pieces, out of the interior model D_u. At world j, the competitor gains an error on π_j and loses one on π_{j+1} and on π_{j+2}. So the error sets cross at every world.

**The fragment Γ** (`x1py/fullfrag.py`).
- Variables x_{j,r} for whole-piece records over the advice {+, 0, −}: 343 records per world, 1029 variables. The fourth advice × is omitted.
- Clauses: the instances of (Bg), (N), (Σ) and (R4), (Csel) and (K) at the realised patterns, with supports S = Plus(s) or S = Ω (interior).

**Soundness (PROVED).** Every clause of Γ is an instance of a clause of Θ_C:
- whole-piece records are realizable;
- composition of whole-piece records is the real composition;
- every competitor of a selected model obtained by changing advice on whole balls is incoherent (it is not a.e. a convex cone).

Hence a derivation of a forbidden outcome in Γ is a real derivation. In the other direction, nothing transfers: the real theory has more records, including ones that split the pieces, and more protected models, including D_q whose boundary crosses a piece.

**U-domain variant.** The earlier scripts `crossing_fragment.py`, `crossing_minimal*.py`, `dead_state_geometry.py` and `horn_states.py` treat the same configuration on M_U (T1 geometry, Brier selection B_q, records σ ∈ {−1, 0, 1}³). Their results agree with §5: 6 minimal models, all common-density witnessed; the dead triple; no one-step failure for clean states of at most 3 records, exhaustively.

---

## 5. Results on the crossing configuration

### 5.1 The dead crossing triple

Let ρ_j := (0→+) on π_j ∪ π_{j+1}, and ι elsewhere. At world j this trades a gain on π_j (good at j) for a loss on π_{j+1} (bad at j). Let L := {ρ_j accepted at world j : j = 0, 1, 2} (indices mod 3), and let X_τ := D_u with Π := π_0 ∪ π_1 ∪ π_2 silenced.

**Theorem X1.5.1 (PROVED).** Let C be any coherent selection, continuous in measure, with an interior C_u whose advice is + a.e. on Π; the precise selection D_q is an example. Then:
1. For the precise selection D_q, every two of the three trades lie in a successful common-density Brier system. With masses m_j = a², m_{j+1} = a, m_{j+2} = 1 on the pieces, ρ_j and ρ_{j+1} are both accepted. All three never are, since that would require a³ ≥ 1.
2. The natural extension E_{1,2,5}(L) (identity, composition, limit rule; no protection) is **clean**: it contains no strict reversal and no tie at all.
3. In E_{1,2,5}(L), X_τ **strictly dominates** C_u.
4. The (K)-disjunction for (u, X_τ) cannot be met at any world, in any extension of L.
5. With protection, E_4(L) is unclean. So the invariant "clean natural extension including R4" rejects L.

*Proof.*
- (1) ρ_j at world j is accepted by Ψ^ρ iff a m_{j+1} ≥ m_j, by the exact piece weights. With the stated masses, a m_{j+1} = a² = m_j, and a m_{j+2} = a ≥ a = m_{j+1}.

- (2) Let B_j be the j-worsening records. Let R_j be the records r such that:
  - (i) on π_{j+1}, r is nontrivial a.e. and r = (x→y) with x ∈ {−, 0} and y ∈ {+, ×}. (These are world-j ranks ≤ 1 and ≥ 2, since − is good on π_{j+1} at world j);
  - (ii) off π_j ∪ π_{j+1}, r is j-worsening;
  - (iii) on π_j, r is unrestricted.

  Put G_j := B_j ∪ R_j. Then:
  - G_j contains ι, all of B_j, and ρ_j.
  - G_j is closed under composition:
    - B∘B ⊆ B.
    - B∘R ⊆ R and R∘B ⊆ R: on π_{j+1}, a worsening step before r starts at rank ≤ 1, and a worsening step after r ends at rank ≥ 2. The composite is nontrivial because its start has rank ≤ 1 and its end rank ≥ 2. Condition (ii) is preserved.
    - R∘R is never composable: on the non-null set π_{j+1}, the first record ends in {+, ×} and the second starts in {−, 0}.
  - G_j contains no nontrivial j-improving record: every element of R_j raises the rank on π_{j+1}.
  - G_j contains no pair r ≠ ι with r⁻¹ also in G_j. If r ∈ R_j, then r⁻¹ starts in {+, ×} on π_{j+1}, so r⁻¹ ∉ R_j, and r⁻¹ lowers the rank there, so r⁻¹ ∉ B_j. If r, r⁻¹ ∈ B_j, then r = ι, by injectivity of the rank.
  - The sections of G_j are closed. For each fixed X, membership of rec(C_q, X) in B_j or R_j is a conjunction of conditions of the form μ{h ∈ E : advice condition on C_q(h)} = 0. These are closed in q because q ↦ C_q is continuous in measure and μ is finite.

  So (G_j)_j is closed under R1, R2 and R5 and is clean, and the least such family E_{1,2,5}(L) lies inside it.

- (3) X_τ ⪯_j C_u at every world. The chain is: X_τ, then ρ_j to accept π_j ∪ π_{j+1}, then (0→+) on π_{j+2}, which is j-worsening because π_{j+2} is bad at world j. Strictness: τ = rec(C_u, X_τ) starts at + on π_{j+1}, so τ ∉ R_j, and τ improves π_{j+1} at world j, so τ ∉ B_j. Hence τ ∉ G_j ⊇ E_{1,2,5}(L)_j for every j.

- (4) If τ is accepted at world j, compose with ρ_j:
  - on π_j and π_{j+1}: (+→0)∘(0→+) = ι;
  - on π_{j+2}: (+→0), which silences a bad acceptance at world j and so is a strict j-improvement, forbidden by (N).

- (5) By (3), X_τ ⪯_j C_u at every world. R4 then installs τ at every world, and (4) applies. ∎

*Meaning.* "Clean under composition closure" is not a sufficient invariant for (a). The obstruction is the ordinal form of the cyclic product a³ < 1. It is invisible pairwise, so pairwise or per-model tests cannot see it; P3 Example 1 is a different instance, through reservations. Protection must be part of the natural extension: undominatedness of the selected models carries information about the pending disjunctions. On M_U the same triple appears in `x1py/dead_state_geometry.py`.

### 5.2 Minimal resolutions of the crossing are additive

**Proposition X1.5.2 (CHECKED; exact).**
- Γ has exactly **90** minimal models, both for S = Ω and for S = Plus(s).
- None contains a two-way tie at any world.
- For each minimal model M and each a ∈ {1/20, 1/5, 3/10, 9/20} there are rational masses m ∈ [1, 100]³ such that every record of M has world value Σ_k Δ_{jk} m_k A_{jk} ≥ 0. This was verified in exact rational arithmetic, with positive slack on every non-background record.
- Consequently, by §4 (exact piece weights) and the Brier facts, M is contained in a successful system Ψ^{ρ_m} that covers the precise targets. Its plan satisfies INV(M; V_m) (Thm X1.3.3(e)).

Files: `exact_witness.py/.out` and `fullfrag.py/.out`.

*Meaning.* Every minimal way of resolving the crossing disjunctions can be continued by the extension theorem with an **explicit** plan. Crossing alone never forces a non-additive resolution.

### 5.3 Non-additive resolutions exist in the fragment

**Proposition X1.5.3 (CHECKED).** Γ (with S = Ω) has models that no common-density Brier ranking contains: CEGAR finds one at its third iteration, with 82 non-background records at world 0, 24 at world 1 and none at world 2 (`cegar_full.py/.out`). It is locally minimal among non-witnessed models: no single non-background record can be removed while keeping a non-witnessed model of Γ. Whether such a model extends to a real successful system is open.

### 5.4 Is a clean natural extension *with* protection sufficient?

**Proposition X1.5.4 (CHECKED for Γ; derivations PROVED in the real system).** Records are written per piece π_0, π_1, π_2, with "." for ι. Let S4 consist of:
- g = [0>+, +>0, 0>+] at world 0;
- c₂ = [0>−, −>+, 0>+] at world 2;
- c₃ = [−>+, 0>−, 0>+] at world 2;
- c₄ = [0>+, +>0, .] at world 2.

Then:
- (i) The closure of S4 under (Bg), (Σ) and (R4) in Γ is clean. Its non-background part is 18 records at world 0, none at world 1 and 26 at world 2.
- (ii) Let X := D_u with π_0 and π_2 silenced, and r := rec(D_u, X) = [+>0, ., +>0]. This is an interior, crossing comparison. Adding r at **any** world produces a forbidden outcome, by real derivations:
  - *world 1:* r is a strict 1-improvement, since π_0 and π_2 are bad at world 1. This is (N).
  - *world 0:* r∘g = [., +>0, .] silences π_1, which is bad at world 0: (N).
  - *world 2:*
    - the composites r∘c₂ = [+>−, −>+, .], then c₃∘(r∘c₂) = [., 0>+, 0>+], then that composite ∘c₄ = [0>+, ., 0>+] = r⁻¹, put r⁻¹ at world 2;
    - r⁻¹ is at world 0 as [., 0>+, .]∘g, where [., 0>+, .] is background at world 0;
    - r⁻¹ is background at world 1;
    - so X ⪯ D_u at every world, (R4) installs r at world 1, and (N) follows.

  Each step composes composable realizable records. Hence **every** system containing S4 violates competitiveness at (u, X).
- (iii) Random maximal clean states of Γ violate some (K) clause in 13 of 400 samples. The minimised stuck states have between 4 and 10 records (`maximal_states.py/.out`, `stuck_minimise.py/.out`, `trace.py/.out`).

So **in the fragment**, "clean natural extension including protection" is not a sufficient invariant. The correct invariant is K-consistency, as in Thm X1.3.3.

**Real status of S4 (open; exact dichotomy, PROVED).** By (ii), exactly one of the following holds:
- (α) The real natural extension E_4(S4) is unclean. Then real protection, either of selected models D_q whose boundaries cross the pieces or against competitors that split the pieces, derives a contradiction that whole-piece protection cannot see.
- (β) S4 is a real counterexample to "clean natural extension suffices".

**Proposition X1.5.5 (a class of real cleanliness certificates; PROVED).** Let Φ′ be the family with:
- world 1: the pointwise background order;
- worlds 0 and 2: additive Brier orders with densities κ_j(k)/φ on π_k (κ_j(k) ≥ 1) and 1 off the pieces.

Then Φ′ is closed under R1–R5 and clean if

κ_0(0) ≥ κ_2(0) and κ_2(2) ≥ κ_0(2),   (κ(1) free).

In that case every set of records contained in Φ′ has a clean real natural extension.

*Proof.*
- Φ′ contains the background orders and is composition-closed (additivity). Its sections are continuous, hence closed. A tie at world 1 forces equality, so there is no (Csel)-tie.
- For R4 it suffices that each D_q is the a.e.-unique minimiser of λ_0Φ_0 + λ_2Φ_2, with λ = (q_0, q_2), among models that are pointwise at least as good as D_q at world 1. Then a model below D_q at every world equals D_q. The case q = e_1 is trivial, since D_{e_1} is pointwise optimal at world 1.
- *Off the pieces:* this is unique q-Bayesness, minus the world-1 term, which the constraint only helps.
- *Points of a piece where D_q's advice is good at world 1:* no alternative is allowed. These are D_q = − on π_0 and π_2, and D_q = + on π_1.
- *On π_0 where D_q = +* (with − and 0 allowed; × never is): the condition is q_0κ_0(0)h_0 + q_2κ_2(0)h_2 > 0. It follows from q_0h_0 > q_1|h_1| + q_2|h_2| ≥ q_2|h_2| together with κ_0(0) ≥ κ_2(0).
- *On π_2:* symmetric, using κ_2(2) ≥ κ_0(2).
- *On π_1 where D_q = −:* − is best at worlds 0 and 2. ∎

**S4 has no Φ′ certificate (PROVED).** Membership of S4 in Φ′ requires:
- from g at world 0: κ_0(2)a ≥ κ_0(0) + κ_0(1)a, hence κ_0(2) > κ_0(0)/a;
- from c₄, c₃ and c₂ at world 2: κ_2(0) ≥ κ_2(1), 2aκ_2(0) ≥ aκ_2(1) + κ_2(2), and 2aκ_2(1) ≥ aκ_2(0) + κ_2(2). These give κ_2(2) ≤ aκ_2(0).

Then κ_2(2) ≥ κ_0(2) > κ_0(0)/a ≥ κ_2(0)/a > aκ_2(0), a contradiction. This is confirmed by LP in `s4_certificate.py/.out`.

**Searches for real counterexamples.** I enumerated the Φ′-certified states L_κ (all fragment records accepted by Φ′ at worlds 0 and 2, for 4000 samples of κ in the admissible region). None has a stuck (K) clause, for either S = Ω or S = Plus(s) (`pareto_witness*.out`).

**Constructions that add only (K)-resolutions** (NUMERICS):
- Exhaustively over clean states of at most 2 resolution literals (18,063 for S = Ω, 7,251 for S = Plus(s)), no (K) clause is unmeetable.
- In 3000 random greedy runs for each support convention, each resolving every clause by a random world whose addition keeps the Horn closure clean, no run got stuck.

Files: `greedy_stuck.py/.out`. All fragment stuck states found contain non-resolution records.

**CONJECTURE X1.C1.** In the three-piece crossing configuration with the precise selection, any state built only from (K)-resolutions whose real natural extension E_4 is clean is K-consistent.

Support:
- the greedy and exhaustive searches above;
- every minimal model is additive (Prop. X1.5.2).

Against:
- in Γ the statement fails for arbitrary states (S4).

---

## 6. What this gives, and what remains

- **The general invariant does not fail; it is exact.** INV(L; V) satisfies (a)–(c) for every partial system (Thm X1.3.3). The counterexamples of §5 concern the *weaker* invariants one might hope to use instead:
  - composition-clean (fails: Thm X1.5.1);
  - clean with protection (fails in the fragment; open in reality: Prop. X1.5.4);
  - finite consistency under R5 (fails at limits: Lemma X1.3.1).
- **The finitary issue is handled exactly.** R5 is the only non-finitary rule. A plan converts it into binary Horn clauses, so finite K-consistency equals K-consistency (Prop. X1.3.2). The price is foresight: V is fixed before the construction.
- **For one crossing configuration, before T1:** every minimal resolution comes with an explicit plan, from a common-density Brier witness (Prop. X1.5.2). The extension theorem therefore runs through the configuration for every precise target. The dead triple shows that protection is indispensable at the first crossing step.
- **The precise next problem.** Find a plan V together with a family of systems that are not all additive and satisfy uniform rejection (Cor. X1.3.5), first for the crossing configuration and then near T1. A cover of T1 exists iff some plan is compatible with all finite fragments of Θ_C (Cor. X1.3.6).
- **Two concrete sub-questions:**
  - decide the dichotomy (α)/(β) for S4. This requires real protection at D_q whose boundary crosses π_0 or π_2. A fragment with split pieces would decide it, but the direct encoding has about 10⁷ clauses;
  - decide whether the non-witnessed model of Prop. X1.5.3 extends to a real successful system.

---

## 7. Status table

| Claim | Status |
|---|---|
| X1.1.1 transition lemma (full domain; advice-range domains) | PROVED |
| X1.1.2 record invariance; composable realizable records are jointly realizable | PROVED |
| Audit wording: condition 3 comes from weak (G), not reflexivity | correction |
| U-domain normal form as a special case; (+→0) and (0→−) not identified | CHECKED |
| X1.3.1 Θ_C and Plan(V) are finitary; R5 is not (P3 Ex. 2) | PROVED |
| X1.3.2 finite K-consistency = K-consistency for a fixed plan | PROVED |
| X1.3.3 plan extension theorem (a)–(e), exact | PROVED |
| X1.3.4 plans are automatic where C_p is locally optimal at world i | PROVED |
| X1.3.5 ultralimits under uniform rejection are successful systems | PROVED |
| X1.3.6 finitary form of the T1 problem | PROVED |
| Brier system on the full domain is a successful system covering precise targets | CHECKED |
| Fragment Γ is sound for derivations of forbidden outcomes | PROVED |
| X1.5.1 dead crossing triple (composition-clean, D_u dominated, (K) unmeetable, caught by R4) | PROVED |
| X1.5.2 90 minimal models of Γ, all exactly common-density witnessed | CHECKED (exact) |
| X1.5.3 a non-witnessed model of Γ exists | CHECKED |
| X1.5.4 S4: clean in Γ but (K) unmeetable; the refutations are real | CHECKED / PROVED |
| Dichotomy (α)/(β) for S4 in the real system | PROVED; which case holds is open |
| X1.5.5 Φ′ certificates; S4 has none | PROVED |
| No stuck clause in Φ′-certified states; greedy (K)-resolution never stuck | NUMERICS |
| X1.C1 (K)-resolution states with clean E_4 are K-consistent (crossing) | CONJECTURE |

## 8. Files (`x1py/`)

**Full-domain crossing configuration**
- `fullfrag.py` / `.out`: the fragment Γ, the dead triple with and without R4, the 90 minimal models, and the witness LPs.
- `exact_witness.py` / `.out`: exact rational verification of Prop. X1.5.2.
- `cegar_full.py` / `.out`: the non-witnessed model of Prop. X1.5.3.
- `greedy_stuck.py` / `.out`: exhaustive search over small states and greedy (K)-resolution runs.
- `maximal_states.py` / `.out`: random maximal clean states and their (K) violations.
- `stuck_minimise.py` / `.out`: minimal stuck states, including S4.
- `trace.py` / `.out`: the derivations quoted in Prop. X1.5.4.
- `pareto_witness.py` / `.out`, `pareto_witness_plus.out`: the Φ′-certified search.
- `s4_certificate.py` / `.out`: S4 has no Φ′ certificate.

**U-domain variant**
- `crossing_fragment.py` / `.out`, `crossing_minimal.py` / `.out`, `crossing_minimal_show.py` / `.out`: the fragment, its 6 minimal models and their witnesses.
- `dead_state_geometry.py` / `.out`: geometry of the dead triple on M_U for T1's U, as NUMERICS.
- `horn_states.py` / `.out`: exhaustive check over clean states of at most 3 records; the dead triple with and without R4.
