# HH1 (round 36, BRIEF28). Coverage without transitivity: the foundation, which barriers still bind, and non-triviality

18 Oct 2026. Rules of BRIEF13 and BRIEF28. Labels:
- **PROVED**: full argument written here (one reader, me; not refereed). Imports keep their recorded status.
- **CHECKED**: a step-by-step reading of a recorded result, or a standard fact with its proof sketched.
- **CONJECTURE**.
- **NUMERICS**: `hh1py/toy.py` (run `python3 -I toy.py` inside `hh1py/`; output `toy.out`). Nothing rests on it.

No assumption is added. Each extra hypothesis below belongs to a stated result and is named there.

**Conventions.** At each world i the relation ≼_i is reflexive. X ≺_i Y means X ≼_i Y and not Y ≼_i X. X ~_i Y means
both X ≼_i Y and Y ≼_i X. X ≈ Y means X ~_i Y at every world. X and Y are *incomparable at i* if neither X ≼_i Y nor Y ≼_i X.
- **(FC)**: A_0 ≼_i A_1 ≼_i … ≼_i A_k implies not A_k ≺_i A_0.
- **(TC)**: A ≼_i B ≼_i C implies not C ≺_i A. This is the case k = 2 of (FC), so (FC) implies (TC).
- **Direct (C)**: if X ≈ C for some C ∈ C_L, then X ∈ C_L.
- **Domination** (used throughout): Y *dominates* X if Y ≼_i X at every world and Y ≺_j X at some world j. Given the first
  clause, Y ≺_j X is the same as "not X ≼_j Y", so this is the same as "Y ≼ X at every world and not Y ≈ X", the form
  used in Loss Dominance Generalized v2 (LDG). Y *weakly dominates* X if Y ≼_i X at every world. Y *strictly dominates*
  X *on S* if Y ≺_i X for every i ∈ S.
- C_L := the coherent members of the domain that no member of the domain dominates. (LA) says that C_L is nonempty.
  (S) gives a selection p ↦ C_p ∈ C_L with C_p competitive on supp p and closed sections {p : C_p ≼_i X}.

---

## 0. Outcome

1. **Foundation (Proposition 1, PROVED).** For arbitrary world relations, with (LA), (S) and direct (C), the dominance
   conclusion of LDG holds model by model:
   - every model is weakly dominated by a selected, undominated, coherent C_p;
   - every undominated model is tied at every world with a selected model;
   - U_L = C_L;
   - every model outside C_L is dominated by a selected member of C_L.

   Neither (FC) nor (TC) is used, and neither is needed to make "undominated" or (LA) meaningful. The strict-dominance
   corollary of LDG (Cor. strict-ordinal) uses transitivity. It **fails under (FC)** (Example A). Under (TC) a weaker
   form survives (Proposition 1(d)).
2. **The quotient by equal profiles fails (Example B, PROVED).** It has (FC) and every other axiom. In it:
   - ≈ is not transitive, so "profiles" overlap and do not partition the models;
   - tied models compare differently with a third model;
   - a member of C_L tied with a competitive selected model is not itself competitive.

   Under (FC) one rigidity survives (Proposition 2): a model tied with a selected C_p is not strictly dominated on supp p.
3. **Dependency check (§2).** Transitivity enters the barriers in two ways only:
   - **tie transfer:** T1 ~ C_p and C_p ≼ Y give T1 ≼ Y. This makes T1 competitive (Lemma IC), and it feeds endorsement
     inequalities;
   - **composition of records:** used in CC2's threshold calculus and in the counting lemma of Three Complete Rankings.

   Tie transfer is repaired by a tie-linearisation lemma (Lemma 2.1) wherever an endorser sees all relevant comparisons.
   Composition is repaired by (TC) where a three-model chain suffices. Verdicts:

   | Barrier | Verdict |
   |---|---|
   | Theorem gm | survives. It constrains only additive rankings directly; through Q4.2 it constrains every cover |
   | M0closed(b), Q4.2 ("some world must not add up") | **survives with repair** (Lemma 2.1); no (FC) or (TC) needed |
   | L4.1 / L4.2 (Hahn–Banach endorser fixed point) | **survives with repair** (Lemma 2.1) |
   | Q3.25 (universal fixed point) | survives **when T1 is selected**. Otherwise its step (b)1 uses tie transfer at the world whose endorser sees only forced pairs, which is a gap |
   | L3.4 (vetoes cannot be paid) | **survives verbatim**; it uses no consistency condition at all |
   | FF2 Thm 4.1 | **survives verbatim** (T1 selected). GG3's Thm 4.1′ (T1 merely tied) needs transitivity; under (TC) a repaired form 4.1″ holds |
   | GG2 Thm B | **survives with repair** (lexicographic Lemma 2.1); no (FC) or (TC) needed |
   | CC2 layered core (Thm 5.6, Cor 5.7) | **fails as stated** (composition in Lemma 4.3(c)). It **survives under (TC)** for models competitive on Ω, so Cor 5.7 holds when T1 is selected. An unselected T1 is a formal gap |
   | Three Complete Rankings Cannot Cover | **survives verbatim**: a complete relation with (TC) is transitive (Lemma 3.2). It concerns the vacuous model, not T1 |

4. **Non-triviality (§3).**
   - (FC) is Suzumura consistency (CHECKED). It is equivalent to the existence of an ordering extension that keeps
     strict comparisons strict.
   - A complete relation with (TC) is already transitive. So the new freedom lives entirely in incomparabilities.
   - A per-world ordering extension keeping T1 undominated exists **iff T1 is undominated in the per-world transitive
     closures** (Proposition 3.3, PROVED). (LA) does not say this. Whether (S) forces it is open. I reduced it to
     closure-domination of one selected model by another (Lemma 3.4).
   - Coverage stays non-trivial:
     - the dominance half is intact;
     - the minimal relation, the background order, admits no competitive interior selection (Lemma 3.5);
     - the surviving barriers bind (FC) covers of T1 exactly as they bind transitive ones.

**Guidance for the constructor.** Non-transitivity can help only inside the relevant comparisons of some world, by making
that world fail to add up. Dropping composites shrinks the set of relevant comparisons, and that makes adding up
*easier*, and adding up is excluded (Q4.2 repaired). The freedom must therefore be spent on (M1)/(M2) structure that
transitive worlds cannot carry. One example: certificates that are not realisable as chains, whose shape restrictions
(N17.3) were derived from sum-closure. Realisable money pumps remain excluded by (FC) (§2.9).

---

## 1. The foundation

### 1.1 Statement

**Proposition 1 (PROVED).** Let Ω be finite, and let each ≼_i be an arbitrary binary relation on M_L. Assume (LA) and (S).
- (a) Every m ∈ M_L is weakly dominated by some selected C_p ∈ C_L.
- (b) Every undominated m ∈ M_L satisfies m ≈ C_p for some selected C_p.
- (c) Assume direct (C) as well. Then U_L = C_L, and every m ∈ M_L ∖ C_L is dominated by a selected member of C_L.
- (d) Assume (TC) at the worlds of a nonempty S ⊆ Ω, and let m′ strictly dominate m on S. Then some selected C ∈ C_L has
  C ≼_i m′ and not m ≼_i C, for every i ∈ S. If S = {i}, then C_{δ_i} ≺_i m.
- (e) For arbitrary Ω, (a)–(d) hold with (S) replaced by (I) and (S_∞) of LDG.

*Proof.*
- (a) This is LDG's argument, verbatim. Put A_i := {p ∈ Δ : C_p ≼_i m}. These sets are closed by (S). Competitiveness of
  C_p on supp p puts every p in A_i for some i ∈ supp p. The KKM lemma gives p_m ∈ ∩_i A_i. C_{p_m} ∈ C_L, and it is
  undominated by the definition of C_L.
- (b) Let c := C_{p_m}. If not m ≼_i c for some i, then c dominates m, by the definition of domination. So m ≼_i c and
  c ≼_i m at every i.
- (c) C_L ⊆ U_L by definition. If m ∈ U_L, then (b) gives m ≈ C_p ∈ C_L, and direct (C) gives m ∈ C_L. Now let
  m ∉ C_L, and let c be as in (a). If m ≈ c, direct (C) would put m in C_L. So not m ≼_j c for some j, and c dominates m.
- (d) Let Δ_S be the face of Δ spanned by S. For i ∈ S put B_i := {q ∈ Δ_S : C_q ≼_i m′}. These sets are closed (by (S),
  intersected with Δ_S). For q ∈ Δ_S we have supp q ⊆ S, so competitiveness puts q in B_i for some i ∈ supp q. The KKM
  lemma on Δ_S gives q* with C := C_{q*} ≼_i m′ for every i ∈ S. Suppose m ≼_i C for some i ∈ S. The chain m ≼_i C ≼_i m′
  and (TC) forbid m′ ≺_i m, which contradicts the hypothesis. If S = {i}, then C_{δ_i} is ideal at i, so C_{δ_i} ≼_i m.
  Together with not m ≼_i C_{δ_i}, this gives C_{δ_i} ≺_i m.
- (e) LDG's compactness argument (Cor. infinite) uses only the closedness of the sets {θ : c_θ ≼_i m}, finite
  intersections and compactness of Θ. For (d), run it over the faces Δ_{F∩S}, F ∈ 𝔉, with F ∩ S ≠ ∅. ∎

**What is used, and what is not (PROVED by inspection).**
- (a)–(c) use the following and nothing else:
  - the closedness and competitiveness in (S);
  - the definition of domination;
  - direct (C), in (c) only.
- Reflexivity is used nowhere. (S) itself demands that C_p be comparable to itself at some world of supp p.
- (FC) and (TC) are not needed to make "undominated", C_L or (LA) meaningful. Domination is defined by finitely many
  comparisons. Two models never dominate each other: that would require Y ≼ X and X ≼ Y at every world, so no strict
  comparison.
- Remark (not used): under (FC) the domination relation is acyclic. A cycle X_1, X_2, …, X_k, X_1 in which each model
  dominates the next is a chain at every world, and it contains a strict step at some world. Under (TC) alone, cycles of
  domination of length ≥ 4 are not excluded.

### 1.2 The model-level statement versus the quotient

LDG states three things through profiles, the ≈-classes:
- U_R = K, i.e. every undominated profile is a coherent profile;
- given U_R = K, U_L = C_L iff (C);
- strict dominance passes to a selected model (Cor. strict-ordinal).

All three use transitivity, as LDG's Remark rem:order says. Proposition 1 replaces them as follows:
- U_R = K becomes (b), "every undominated model is tied with a selected model", a statement about models;
- U_L = C_L is derived from direct (C), which is LDG's (C) read literally;
- Cor. strict-ordinal becomes (d).

Each replacement is necessary. Two concrete systems show it.

**Common base (both examples).**
- Two worlds. Index Δ by t := p_1, so t = 1 is δ_1 and t = 0 is δ_2.
- Selected models c_t, t ∈ [0,1], all coherent, compared by the loss (1−t, t):
  - c_s ≼_1 c_t iff s ≥ t;
  - c_s ≼_2 c_t iff s ≤ t.
- The selection is u(p) := c_{p_1}.

**Example A (strict dominance does not pass to a selected model under (FC); PROVED).**

*Models and relations.* Add two incoherent models m, m′. Put h := 1/2 and q := 1/4.
- c_t ≼_1 m iff t ≥ h; c_t ≼_2 m iff t ≤ h.
- c_t ≼_1 m′ iff t ≥ q; c_t ≼_2 m′ iff t ≤ q.
- m ≼_2 c_h.
- m′ ≼_1 m and m′ ≼_2 m.
- Reflexivity. Nothing else.

*Verification.*
- **(S).** Each section is a closed interval or empty: [u,1], [0,u], [h,1], [0,h], [q,1], [0,q]. So the sections are
  closed. Competitiveness:
  - at t = 1, c_1 ≼_1 every model;
  - at t = 0, c_0 ≼_2 every model;
  - for interior t, against m we have t ≥ h or t ≤ h, and against m′ we have t ≥ q or t ≤ q.
- **(LA).** Something ≼ c_t at both worlds must be c_t itself: m and m′ are ≼ no c_t at world 1. So every c_t is
  undominated, and C_L = {c_t}.
- **Direct (C).** m ≈ c would need m ≼_1 c, which never holds. m′ is ≼ no c_t.
- **(FC) at world 1.** No edge leaves {m, m′} except m′ → m. So every cycle lies inside the base order, which is a
  linear order.
- **(FC) at world 2.** The edges leaving {m, m′} are m → c_h and m′ → m. From c_h one reaches c_v with v ≥ h, and m only
  from c_h. The edge into m′ comes only from c_t with t ≤ q. So no cycle passes through m′. The only cycle through m
  is m → c_h → m, and both of its steps are ties.

*Claims.*
- m′ strictly dominates m at both worlds.
- c_t ≺_1 m needs t ≥ h. c_t ≺_2 m needs t ≤ h and not m ≼_2 c_t. Only t = h meets the first two conditions, and
  m ≼_2 c_h holds. So **no member of C_L strictly dominates m on Ω**, and Cor. strict-ordinal fails.
- What survives is (d): c_{1/4} ≼_i m′ and not m ≼_i c_{1/4}, at both worlds. In fact c_{1/4} ≺ m′ ≺ m at both worlds,
  while c_{1/4} and m are incomparable at world 1. That is exactly the comparison transitivity would have installed.
- m is dominated (by c_h, strictly at world 1), as (c) says.

NUMERICS (`toy.out`, grid 1/48): (FC) strict edges inside strongly connected components 0, (TC) violations 0,
competitiveness failures 0, (C) violations 0. The claims are confirmed.

**Example B (≈ is not transitive; tied models differ on third models; ties do not transfer competitiveness; PROVED).**

*Models and relations.* Add two coherent models e, e′, not selected. For x ∈ {e, e′}:
- c_t ≼_1 x iff t ≥ h; c_t ≼_2 x iff t ≤ h;
- x ≼_1 c_h and x ≼_2 c_h;
- reflexivity. Nothing else; in particular e and e′ are incomparable at both worlds.

*Verification.*
- **(S).** The sections are as for c_h, so (S) holds.
- **(LA).** Something ≼ e at both worlds must be c_h (t ≥ h and t ≤ h), and c_h ≈ e. So e is undominated. The same
  holds for e′. Every c_t stays undominated.
- **Direct (C).** The models tied with members of C_L are c_h, e and e′, all in C_L.
- **(FC).** In any cycle, replace e or e′ by c_h. This gives a cycle of the base order with the same strict steps: c_t ≼ x
  is strict iff t ≠ h, iff c_t ≼ c_h is strict. The base order has no strict cycle.

*Claims.*
- e ≈ c_h and e′ ≈ c_h, but e and e′ are not tied. So the "profiles" N(x) := {y : y ≈ x} overlap without coinciding:
  N(c_h) = {c_h, e, e′} and N(e) = {e, c_h}. They do not partition the models, so the quotient R, and the statements
  U_R = K and K ⊆ U_R, are not defined as LDG intends.
- **Tied models differ on a third model:** c_h ≼_2 c_{3/4} but not e ≼_2 c_{3/4}.
- **Ties do not transfer competitiveness:** e is not competitive on {1,2}, since neither e ≼_1 c_{3/4} nor e ≼_2 c_{3/4}.
  Yet e is tied with the competitive c_h. This is the step "ties transfer competitiveness" (R5 N1) inside Lemma IC, and
  §2 shows that it is the main channel through which transitivity enters the barriers.

NUMERICS: as for Example A, all zero. Confirmed.

**Proposition 2 (rigidity under (FC); PROVED).** Assume (FC), (S) and (LA). Let m ≈ C_p with C_p selected. Then no model
strictly dominates m on S := supp p.

*Proof.* Let d strictly dominate m on S. KKM on the face Δ_S, applied to d as in Proposition 1(d), gives a selected
C_q, q ∈ Δ_S, with C_q ≼_i d for every i ∈ S. Competitiveness of C_p on S, against C_q, gives some i ∈ S with
C_p ≼_i C_q. At that i,

  d ≼_i m ≼_i C_p ≼_i C_q ≼_i d,

and the step d ≺_i m is strict. This contradicts (FC). ∎

The cycle has four steps, so (TC) does not suffice.

Under transitivity, a model tied with a member of C_L is undominated. So LDG's equivalence "(C) iff U_L = C_L" holds in
both directions. Without transitivity only "direct (C) implies U_L = C_L" is proved (Proposition 1(c)). Proposition 2
recovers part of the converse under (FC). I have not determined whether the full converse fails under (FC). Nothing
below needs it, because direct (C) is an axiom.

---

## 2. Dependency check: which barriers still bind

### 2.0 Three tools

**Lemma 2.1 (tie linearisation; PROVED).**
- **Additive form.** Let ν_i be an additive set function (a bounded charge, a σ-finite measure, or an integral against a
  density) that endorses every relevant comparison at world i: B ∈ C_L, X regular and B ≼_i X imply ν_i(λ_i B) ≤ ν_i(λ_i X).
  Here λ_i is the error indicator or the ladder profile. Suppose B, B′ ∈ C_L and B ~_i B′. Then ν_i(λ_i B) = ν_i(λ_i B′).
  Hence, for C ∈ C_L with B ~_i C and C ≼_i Y (Y regular), ν_i(λ_i Y − λ_i B) ≥ 0, whether or not B ≼_i Y holds.
- **Lexicographic form.** Suppose instead that every comparison X ≼_i Y implies (E_i, B_i)(X) ≤_lex (E_i, B_i)(Y). Then
  ties give lex-equal values, and the same conclusion holds with ≤_lex.

*Proof.* Coherent models are regular, so B ≼_i B′ and B′ ≼_i B are both relevant comparisons. They give the two
inequalities. For the second claim, write
ν_i(λY − λB) = ν_i(λY − λC) + ν_i(λC − λB) ≥ 0 + 0. This is linearity on bounded functions. The lexicographic case is the
same, with antisymmetry of ≤_lex. ∎

The lemma uses no (FC) and no (TC). It needs the endorser to see the two tie comparisons. That holds whenever it endorses
**all** relevant comparisons, and fails for endorsers of a restricted family (§2.3).

**Lemma 2.2 (Lemma IC under (TC); PROVED).** Assume (TC). Let T ∈ C_L satisfy T ≈ C_a with C_a selected. Then:
- T is *weakly competitive* on S := supp a: for every X some i ∈ S has not X ≺_i T;
- the conclusion of R11 Lemma IC survives: supp a = Ω, for every target D_K with K ⊆ int Δ and (LF).

Full competitiveness of T on Ω does **not** follow (Example B).

*Proof.* C_a ≼_i X for some i ∈ S. Then T ≼_i C_a ≼_i X, and (TC) forbids X ≺_i T. In R11's proof of Lemma IC, the
model X built there has X ≺_i T at every i ∈ S, by strict (G). That contradicts weak competitiveness. ∎

**Lemma 3.2** below: a complete relation with (TC) is transitive. It settles every barrier stated for complete worlds.

### 2.1 Theorem gm (additive covers)

Additive rankings are transitive, so the theorem survives. Directly, it constrains only additive rankings. Its proof has
two parts:
- the necessary structure (TS)/(PC)/(NS), read off the Bayes family;
- the field contradiction: routes I1, I2, C2, and in the general form the chain D1 → M3.9 (BB2 Thm 6.1 with AUDIT_BB
  Lemma 2.0) → Q4.1 → M3.7(d)/M3.8.

The field contradiction is a statement about a strictly guiding integrable field with (γ) and D_{T1} Bayes at an interior
weight. No ranking appears in it (GG3 §8.1: "No step uses the ranking"; CHECKED here for D1, Q4.1 and CC3 Lemma 2.0).

**So gm constrains non-transitive covers exactly through the reductions that produce such a field from a ranking**:
Q4.2, M0closed(b), FF2 Thm 4.1, GG2 Thm B. Those are checked below. One consequence (PROVED from §2.2): if every world's
relevant comparisons are endorsed by some strictly guiding additive ranking with integral penalties and integrable
envelope, the cover is excluded, whether or not the worlds are transitive. Such a ranking gives a ladder weight with
positive density, so (NC) holds and the world adds up (M3.1, last clause).

### 2.2 M0closed(b) and Q4.2: "some world must not add up"

**Where transitivity enters.**
1. **R11 Lemma IC** ("ties transfer competitiveness", R5 N1). It is used in N17 Prop 2.1(α) and N13 Prop B (the route
   behind Prop M0).
2. **H1.1 step 1**: "T1 is tied with C_p, so C_p ≼_k Y for some k, and T1 ≼_k Y by transitivity". It is used in L4.1.3
   (hence L4.2, the write-up's route to M0closed(b) without N13) and in M3.4.3 (hence Q4.2, step 1 of its chain).

Nothing else at ranking level:
- M3.1 is Hahn–Banach and uses only strict (G);
- M3.3 and L4.0 (absorption) are measure theory;
- M3.4.1 ("undefeated") uses Proposition 1(a) and relevance;
- D1, M3.9 + Lemma 2.0, Q4.1, M3.7, M3.8 and M0closed(a) are field-level.

**Repair (PROVED).** In H1.1 step 1 (and M3.4.3, N17 2.1(α)), replace "T1 ≼_k Y by transitivity" by Lemma 2.1:
- C_p ≼_k Y is relevant, and the endorser ν_k sees T1 ~_k C_p in both directions;
- so ν_k(λ_k Y − λ_k T1) ≥ 0;
- if Y = T1 off the localizing set D_m, the purely finitely additive part of ν_k(λY − λT1) is ≤ 2^{−m′} for every m′, as
  before, so ∫ρ_k(λY − λT1) ≥ 0.

The rest of H1.1 (Lyapunov, separation, limit, interior) is field-level. For N17 2.1(α) with countably additive weights,
ψ_i(T) = ψ_i(C_p) ≤ ψ_i(X) at the world i where C_p ≼_i X. Here i ranges over supp p, and Lemma IC is not needed.

**Verdict.** Q4.2, M3.10, M3.10′ and M0closed(b) (both routes) **survive with this repair, for arbitrary reflexive world
relations**. No (FC) or (TC) is needed. Their status is unchanged otherwise. The hypothesis "(NC) at every world", and
"adds up", are statements about relevant comparisons, and they mean the same without transitivity.

### 2.3 L4.1 / L4.2 and Q3.25 (endorser fixed points)

- **L4.1, L4.2.** The endorser tuple ν ∈ ∏𝒩_k endorses all relevant comparisons. Step 3 (admissibility) is H1.1, repaired
  as in §2.2. Steps 1, 2 and 4 use Proposition 1(a), absorption and field arguments. **Survives with repair; no (FC) or
  (TC) needed.**
- **Q3.25.** Step (b)1 uses: "T1 ∈ C_L is competitive on Ω by Lemma IC, and (CA) gives T1 ⋠_j Y_W. So (T1, Y_W) is a
  forced pair." World 1's endorser φ* ∈ 𝒩(𝔉𝔏) endorses only forced and limit pairs, so Lemma 2.1 is not available at
  world 1. The partners are fine: they are (CA), endorsing all relevant comparisons.
  - **If T1 is selected** (T1 = C_{p*}), then T1 is competitive on supp p*, and supp p* = Ω by Lemma IC's argument with
    no tie transfer. Step (b)1 then needs no transitivity. Q3.21, Q3.22 and Q3.23 use closed sections, competitiveness
    of selected models, weak (G) and (CA) only (CHECKED). **Survives.**
  - **If T1 is only tied with C_{p*}:**
    - under (TC), T1 is weakly competitive (Lemma 2.2), but that does not make (T1, Y_W) forced;
    - running the step with C_{p*} gives admissibility of C_{p*} for c♮, not of T1.

    **Gap.** The formal escape is that T1 is tied with, but different from, its selected partner, and is incomparable at
    world 1 to its own local perturbations that the partners reject. I found nothing that excludes it.

### 2.4 L3.4 (vetoes cannot be paid)

Read step by step (L3_notes §4):
- C_{e_m} = B^m uses ideality and strict (G);
- step 1 uses refinement of Φ and closedness at world i;
- step 2 uses strict (G), closedness at j, competitiveness on {i,j} and refinement;
- step 4 uses refinement and closedness.

Each comparison is used directly. None is composed. The hypothesis "world i refines Φ" (Φ(X) < Φ(Y) ⇒ X ≺_i Y) is a
condition on single comparisons. **Survives verbatim, for arbitrary relations.** The application to VB and to ordinal
gauge limits (L3.5) concerns those transitive objects, and is unchanged.

### 2.5 FF2 Theorem 4.1, and GG3's Theorem 4.1′

- **Thm 4.1.** Its hypotheses are explicitly "any relations on models" (FF2 §4). GG3 §8.1 confirmed that no step uses the
  ranking beyond competitiveness and (H3). **Survives verbatim**, with T1 = C_{q₀} selected.
- **Thm 4.1′ / the reading of Cor 4.3** (GG3 §8.3). It replaces "T1 selected" by "T1 competitive on supp q₀", "which
  every cover gives by Theorem kkm and transitivity". That step fails without transitivity (Example B).
- **Repair under (TC), Thm 4.1″ (PROVED).** Assume (TC). Replace "T1 = C_{q₀}" by "T1 ≈ C_{q₀}". Strengthen (H3), for
  i ∈ supp q₀ and X = T1 off H_n, to

  not X ≺_i T1 ⇒ ∫(ℓ_i(X) − ℓ_i(T1)) dμ ≥ 0.

  The conclusion is unchanged.

  *Proof.* Steps 1–4 concern the selection. Step 5 is Step 1 run for T1. It needs only "every X has some i ∈ supp q₀ with
  z_i(X) ≥ 0", and that follows from weak competitiveness (Lemma 2.2) and the strengthened (H3). Step 6 is
  field-level. ∎

  This is stronger than endorsing accepted comparisons: it endorses non-reversals. That is the honest price of dropping
  tie transfer.

### 2.6 GG2 Theorem B

- Step 2 says: "T1 is tied with C_p … so by transitivity T1 is competitive on S".
- **Repair (PROVED).** Hypothesis (i) applies to every comparison, so T1 ~_k C_p gives
  (E_k, B_k)(T1) = (E_k, B_k)(C_p) (Lemma 2.1, lexicographic form). For X = T1 off H_n, some k ∈ S has C_p ≼_k X. By (i)
  and end-locality, E_k(X) = E_k(T1) = E_k(C_p), hence B_k(C_p) ≤ B_k(X), i.e. B_k(T1) ≤ B_k(X). This is what Step 2
  uses.
- Step 1 uses Proposition 1(a) and (i). Steps 3–5 are field-level.

**Survives with repair, for arbitrary relations.** Corollaries B.1 and B.2 likewise; B.1's "preorders" may be dropped.

### 2.7 CC2: the layered core (Lemma 4.3, Thm 5.6, Cor 5.7)

CC2 assumes (R0): each world is a composition-closed set of records, by the transition lemma. Transitivity is used in
Lemma 4.3 and nowhere else in §5. The Remark after Cor 5.7 says the same. Under (TC):

- **4.3(b) survives (PROVED).** Let w∘o ∈ A_k with o in Z, and w⁻¹∘o′ ∈ A_k with o′ in Z′, where Z ∩ Z′ = ∅. Realise
  X ≼_k Y := X∘w∘o ≼_k Z_ := Y∘w⁻¹∘o′ = X∘o∘o′ on the full domain. If ℓ_k(o) + ℓ_k(o′) < 0, then by (H1) the off-W record
  o∪o′ is rejected and its reverse is accepted, so Z_ ≺_k X. That contradicts (TC). Hence
  θ_k(w|Z) + θ_k(w⁻¹|Z′) ≥ 0.
- **4.3(d) survives (PROVED).** Let w be strictly k-improving, w∘o ∈ A_k and ℓ_k(o) < 0. With Y := X∘w∘o and
  Z_ := Y∘o⁻¹ = X∘w, we have X ≼_k Y ≼_k Z_ and Z_ ≺_k X, by strict (G). That contradicts (TC).
- **4.3(c) fails as proved.** It needs w∘o ∈ A and o⁻¹∘o′ ∈ A ⇒ w∘o′ ∈ A. (TC) gives only "not (w∘o′ rejected and its
  reverse accepted)". So thresholds need not be intrinsic.
- **Repair of Lemma 5.5 / Thm 5.6 (PROVED).**
  - Use region-indexed thresholds: a := −θ(w|Z_C), b^E := −θ(w′|Z_E), b^F := −θ(w′|Z_F).
  - Step 4 uses only the definition of θ(w|Z_C).
  - Step 5 uses b^E ≤ −a and b^F ≤ −a. These are 4.3(b) for the disjoint pairs (Z_C, Z_E) and (Z_C, Z_F).
  - Step 3 uses 4.3(d). (H3) bounds every region threshold.
  - Restate (H4) per region: θ(w|Z) ≠ 0 for every rich off-W region Z. Under (R0) this is equivalent to the original.

  So **Thm 5.6 survives under (TC) for every model competitive on Ω**, under (H1), (H3), (H4)_Z and (S∂). Lemmas 5.1–5.4
  use (H1), competitiveness, closedness and (G) only.
- **Cor 5.7** needs T1 competitive on Ω.
  - If T1 is selected, Lemma 2.2's argument gives supp = Ω, and **Cor 5.7 survives under (TC)**.
  - If T1 is only tied with a selected model, Lemma 5.1 still holds for T1. Off-W records are complete by (H1), so weak
    competitiveness gives ℓ_k(rec) ≥ 0 at some k. But Step 4 of Lemma 5.5 needs X ≺_k T1 at all three worlds, and an
    incomplete W-record need not deliver it. **Gap**, of the same kind as in §2.3.

### 2.8 Three Complete Rankings Cannot Cover

Its hypotheses are complete preorders with (G), (IB) and (S). It uses transitivity heavily: the transitivity of ≼_d and
≼_c, Lemma compose, the counting lemma, and Prop finite. By Lemma 3.2, a complete relation with (TC) is transitive. So
the hypothesis "complete, with (FC) or (TC)" is the old hypothesis, and **the theorem survives verbatim**.
- Its subject is the vacuous model. It does not constrain T1 directly. The write-up's T1 exclusion for complete worlds is
  only for (CP-a) worlds (Thm complete), which are transitive by construction.
- For incomplete non-transitive worlds its tools are unavailable. Lemma count needs composition. Its open problem (one or
  two incomplete worlds) is unchanged.

### 2.9 Where composition-closure itself was used (for completeness; CHECKED)

- **N17.1(b), the money pump.** It survives under (FC). If the records compose pointwise, the partial sums are realised
  by a chain X_0 ≼ X_1 ≼ … ≼ X_k. A sum that is ≤ 0 and non-zero makes X_k pointwise better, so X_k ≺ X_0 by strict (G).
  That is a strict reversal of a chain. (TC) gives this for k = 2 only.
- **N17.1(d) and N17.3**, the (M1) certificate shape restrictions (≥ 5 terms; ≥ 4 comparisons with overlapping gains).
  They use single-layer sum-closure (transitivity). They need not hold for (FC) worlds when the certificate is not
  realisable as a chain. These were restrictions, not barriers, so their loss only enlarges the search space.
- **GG3's NA-credal representation, the intersection theorem, FF1's closure classes.** They are transitive by
  construction, so they constrain only those classes, as BRIEF28 says.

---

## 3. Non-triviality

### 3.1 Suzumura consistency

**Lemma 3.1 (CHECKED; Suzumura 1976, Economica 43:381–390; Bossert–Suzumura, *Consistency, Choice, and Rationality*,
2010, Ch. 2).** For a reflexive relation R with strict part P, the following are equivalent:
1. R satisfies (FC);
2. the transitive closure T of R satisfies P ⊆ P(T);
3. R has an ordering extension: a complete preorder R* ⊇ R with P ⊆ P*.

*Proof sketch.*
- (3 ⇒ 1). A chain x_0 R … R x_k gives x_0 R* x_k, so not x_k P* x_0, and hence not x_k P x_0.
- (1 ⇒ 2). Let x P y. Then x T y. If y T x, a chain from y to x followed by x P y is a cycle with a strict step.
- (2 ⇒ 3). T is a preorder. By the Szpilrajn–Hansson extension theorem (Szpilrajn 1930; Hansson 1968, which uses the
  axiom of choice), T has an ordering extension R* with P(T) ⊆ P*. So P ⊆ P(T) ⊆ P*. ∎

A useful refinement (PROVED): **every ordering extension contains T and keeps P(T) strict.** R* is transitive and
contains R, so it contains T. If x P(T) y, then some chain from x to y has a P-step: a chain made only of ties could be
reversed, giving y T x. That step stays strict in R*, so x P* y.

**Lemma 3.2 (PROVED).** A complete relation with (TC) is transitive.

*Proof.* Let x R y, y R z and not x R z. By completeness z R x, so z P x. The chain x R y R z then violates (TC). ∎

So the freedom BRIEF28 grants exists only at worlds with incomparabilities. Every barrier proved for complete
preorders binds complete (TC) worlds unchanged.

### 3.2 Extensions that keep T1 undominated

**Proposition 3.3 (PROVED).** Let each world satisfy (FC), with transitive closure T_i. The following are equivalent:
- (i) T1 is undominated in the closures: no X has X T_i T1 at every i and X P(T_i) T1 at some i;
- (ii) there are per-world ordering extensions R*_i (complete preorders, R_i ⊆ R*_i, P_i ⊆ P*_i) in which T1 is
  undominated.

*Proof.*
- (ii ⇒ i). Every extension contains T_i and keeps P(T_i) strict (refinement of Lemma 3.1). So domination in the closures
  is domination in every extension.
- (i ⇒ ii). Fix i and put A := {X : X T_i T1}, a down-set of T_i. No T_i-comparison runs from outside A into A: if
  x T_i y and y ∈ A, then x ∈ A. Define R*_i in two steps:
  - all of A before all of A^c;
  - inside A, and inside A^c, an ordering extension of T_i restricted there (Lemma 3.1).

  This contains T_i and keeps P(T_i) strict, since cross comparisons only go from A to A^c. In R*_i, X R*_i T1 iff
  X ∈ A, and then X P*_i T1 iff X P(T_i) T1. So T1 is dominated in (R*_i) iff it is dominated in (T_i). ∎

**Is (i) automatic in an (FC) system with (LA), (S), (C)?**
- Not from the definitions. A three-model illustration (CHECKED): with z ≼_1 y ≼_1 e strictly at each step and z ~_2 e,
  e is undominated in R, since z and e are incomparable at world 1 and y and e are incomparable at world 2. But z
  dominates e in the closures. This illustration has no selection.
- Whether (S) forces (i) is **open**. The following reduction is what I proved.

**Lemma 3.4 (PROVED).** Assume (FC), (LA) and (S), and suppose that z dominates e ∈ C_L in the closures. Then there are
selected C_q, C_s with e ≈ C_s such that:
- C_q dominates C_s in the closures;
- for every i ∈ supp s with C_s ≼_i C_q, the closure relation between C_q and C_s at i is a tie;
- in particular the closure-strict world lies outside {i ∈ supp s : C_s ≼_i C_q}.

*Proof.*
- e ≈ C_s by Proposition 1(b). By Proposition 1(a), some selected C_q ≼ z at every world.
- Then C_q T_i z T_i e T_i C_s at every i. At the strict world j of z over e, C_q P(T_j) C_s: if C_s T_j C_q, then
  e T_j z, against z P(T_j) e.
- If C_s ≼_i C_q with i ∈ supp s, the cycle C_q → … → C_s → C_q at i must consist of ties, by (FC). ∎

Evidence, without a verdict:
- In two worlds I tried selections whose relations are loss-like along a frontier, including flat blocks, plateaus and
  non-monotone frontier paths. Each attempt fails by the same connectedness mechanism. A point of the selection that is a
  limit of models better at world 1 is forced by closed sections to be ≼_1 the target block. To stay undominated it must
  then tie with it. This "hub" ties C_q to C_s in the closure.
- In three worlds this mechanism could supply the closure ties at two worlds while the third supplies strictness. I have
  not built such a system.
- **CONJECTURE (labelled; not used):** in two worlds with (FC), (LA) and (S), every member of C_L is undominated in the
  closures.

Even when (i) holds, the extension is not a transitive cover:
- it keeps (G) and competitiveness, since both are preserved by adding comparisons;
- in general it loses (IB) and the closedness of sections, since the sections only grow.

So it does not reduce (FC) coverage to the transitive problem.

### 3.3 Coverage remains non-trivial

**Lemma 3.5 (PROVED).** On a decomposable domain, let the background order (pointwise world-i guidance) be the world
relations. Let C be a model such that, for every i ∈ S, the domain allows a strict world-i improvement of C's advice on a
non-null set of pairs. Then C is not competitive on S.

*Proof.* Choose disjoint non-null sets A_i (i ∈ S) with an available advice strictly better at world i than C's. Let X be
C with that advice on each A_i. At world i, X is strictly better than C on A_i, so C is not pointwise at least as good.
That is, not C ≼_i X, for every i ∈ S. ∎

T1 and every interior coherent model near it have such sets, by (LF) near ∂D_{T1}. So under (S) the comparisons cannot be
left at the (G)-minimum. Competitiveness forces comparisons that guidance does not supply, and (FC) with (IB) constrains
them. This matches SPLICING_summary's report that intersecting to the background order kills (S).

**Paragraph: why coverage of T1 under (FC) is not trivial.** The weakening leaves the dominance half intact
(Proposition 1). Incoherent models are still dominated, "undominated" is not vacuous, and C_L is exactly the undominated
class. It cannot be satisfied by withholding comparisons: Lemma 3.5 shows that (S) forces comparisons beyond guidance,
and (FC) forbids every realisable strict cycle among them. By Lemma 3.2, complete worlds gain nothing. Most importantly,
the barriers that bind T1 do not depend on transitivity:
- "every cover has a world that does not add up" (Q4.2, M0closed(b), with Lemma 2.1);
- the veto theorem L3.4;
- FF2 Thm 4.1 for selected T1 with a selection continuous in measure;
- GG2 Thm B;
- CC2's rigidity under (TC).

An (FC) cover of T1 therefore faces the same additive holonomy obstruction as before, whenever some world's relevant
comparisons are additively endorsable. The new freedom can matter only by producing a world that is not, through
non-composable (M1)/(M2) structure.

---

## 4. Status table

| # | Statement | Label |
|---|---|---|
| Prop 1(a)–(c),(e) | model-level dominance theorem for arbitrary relations, direct (C) | PROVED |
| Prop 1(d) | strict dominance under (TC): non-reversal form; singleton S strict | PROVED |
| Ex A | (FC) system with all axioms where LDG Cor. strict-ordinal fails | PROVED; NUMERICS |
| Ex B | (FC) system with all axioms: ≈ not transitive, profiles overlap, ties do not transfer competitiveness | PROVED; NUMERICS |
| Prop 2 | (FC): tied with selected C_p ⇒ not strictly dominated on supp p | PROVED |
| converse "U_L = C_L ⇒ (C)" under (FC) | not determined (not needed) | open |
| Lemma 2.1 | tie linearisation (additive and lexicographic) | PROVED |
| Lemma 2.2 | Lemma IC under (TC); weak competitiveness | PROVED |
| §2.1 | Theorem gm: survives; constrains non-transitive covers only via the reductions | CHECKED |
| §2.2 | Q4.2, M3.10, M0closed(b): survive with Lemma 2.1, arbitrary relations | PROVED (repair); rest CHECKED |
| §2.3 | L4.1/L4.2 survive (repair); Q3.25 survives for selected T1, gap otherwise | PROVED / CHECKED |
| §2.4 | L3.4 survives verbatim | CHECKED |
| §2.5 | FF2 Thm 4.1 survives verbatim; Thm 4.1″ under (TC) | CHECKED / PROVED |
| §2.6 | GG2 Thm B survives with lexicographic Lemma 2.1 | PROVED (repair) |
| §2.7 | CC2: Lemma 4.3(b),(d) and Thm 5.6 under (TC); 4.3(c) fails as proved; Cor 5.7 for selected T1 | PROVED (repair); gap for unselected T1 |
| §2.8 | Three Complete Rankings survives (Lemma 3.2) | PROVED |
| Lemma 3.1 | (FC) ⟺ Suzumura ⟺ ordering extension keeping strict comparisons; every extension contains T and keeps P(T) | CHECKED (standard) / PROVED |
| Lemma 3.2 | complete + (TC) ⇒ transitive | PROVED |
| Prop 3.3 | extension keeping T1 undominated ⟺ T1 undominated in closures | PROVED |
| Lemma 3.4 | reduction of closure-domination to selected models | PROVED |
| two-world closure-undominatedness | | CONJECTURE |
| Lemma 3.5 | background order admits no competitive interior selection | PROVED |

**Single most important open point for the constructor.** The two formal gaps (Q3.25 and CC2 Cor 5.7) have the same
escape: **T1 tied with its selected partner without being competitive**. In every barrier with a selected T1 the gap
closes. A construction that wants to use it must make T1 incomparable, at the world whose endorser sees only forced
pairs, to its own local perturbations that the partner worlds reject. Example B shows such ties exist abstractly.
Whether they are compatible with (IB) and closed sections near ∂D_{T1} is the question to test first.

## 5. Files

`hh1py/toy.py` (+ `toy.out`): grid checks of Examples A and B. NUMERICS only.
