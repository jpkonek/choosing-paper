# REF65_ad — Referee report on AD65_notes.md ((Add) as a separate normative question) (26 Oct 2026)

Labels: **PROVED** (argument checked or supplied here) / **CHECKED** (exact computation) / **CONTINUUM-EXACT** (exact computation that covers every measurable model on an atomless space partitioned into finitely many sign-homogeneous cells; method in §2.3). Scripts are in `ref65ad_py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file. None of them imports `ad65py/`: the property checker `rel.py` was written from the definitions, and it checks (IB) in the literal W62 form, quantifying over every S.

Inputs read: BRIEF65 (AD65 role), AUDIT_r65_brief, AUDIT_r65_message, AUDIT_r64_decisions, REF64_es §2 and §5, ES64 §§0–3, OR64 §1, §2 (M1) and §3.5 (𝒯), AUDIT_nontransitive, W62 §2, and AD65_notes with all of `ad65py/`.

---

## 0. Summary verdict

**The core mathematics is correct.** I checked each of the following line by line and found it correct:
- Lemma 1.1;
- Props 3.1(a)–(e), 3.2, 3.3, 3.4 and 3.5;
- Prop 4.1;
- the rigidity Lemma 4.2;
- Remark 4.3;
- Prop 5.1 and Theorem 5.2(a)–(c);
- Prop 5.4 (M1⁺) and Prop 5.5 (𝒯⁺, including transitivity).

The correction to REF64_es §5.4 is right: (Add) excludes the relations Δ(𝒩), M1 and 𝒯, but not the phenomena they were used to show.

**Three errors, all repairable.**
1. **E1 (scope overclaim, §5 Cor 5.3, §0.5 and §6.1).** "(G)+(IB)+(TC)+(Add) admits a universal cover **iff** (H)" and "cover of the reversed triangle **iff** (★) for some 𝒩 ∋ D_K" are proved only in the "if" direction.
   - The "only if" direction holds for the particular relation R_lex(all coherent). It does not hold for the framework.
   - This repeats the error that AUDIT_r65 scope correction 3 warns against.
   - The side remark "R_lex(𝒩) with D_K ∈ 𝒩 covers K iff (★) holds for 𝒩" is unproved in the "only if" direction and too strong as stated: every Bayes act is undominated in every R_lex(𝒩), so (★) for 𝒩 fails whenever 𝒩 omits a Bayes act, although a cover needs only coherent undominated models. The proved equivalence is "with undominated set exactly 𝒩".
2. **E2 (normative claim refuted, §0.4, §2.1(4) and the §4 table).** The claim "incomparability under (Add) must be content-based and scale-free" is false.
   - A **materiality threshold**, "accept guided changes, and other changes only if they improve Brier at i by at least c > 0", is world-local and purely accuracy-based.
   - It satisfies (Add), and is even **transitive**, yet it leaves every small non-guided improvement unranked (Ex T, §3.3).
   - Lemma 4.2 forbids only the opposite pattern, "trust small changes, suspend large ones".
3. **E3 (minor, Prop 3.1(f)).** The relation "only the null record" *is* reflexive. Use the empty relation to show that (Add) does not imply reflexivity.

**Gaps, each repaired here.**
- **G1 (examples realised only on finite atom algebras).** The framework's measure is atomless, so records can cut cells. I checked each example in that setting.
  - **Ex A as defined fails (TP)**, and **Ex E as defined ("(Add) closure") fails (TP)**. Both were found by refinement and proved by hand.
  - I give a repaired A, and E with the (Add)+(TP) closure. With these definitions, every example is valid in the continuum (CONTINUUM-EXACT or PROVED).
  - **Ex G** (completeness) has no canonical lift. I supply a continuum relation with G's property vector, found by SAT and verified exactly.
- **G2 (two non-implications without witnesses).** The claim "nothing else implies (Add)" needs a witness for *complete + (IB) + (TP) without (Add)*. Separately, the lattice needs *complete + (IB) + (Add) without (TP)*. AD65 has neither.
  - I supply both: a majority vote of three weighted Brier scores (Ex V, PROVED) for the first, and a SAT-found continuum relation (K*) for the second.
  - With these, the full implication lattice of AD65 §3 is established in the continuum.
- **G3.** Prop 5.4's (FCC) for M1⁺ was only CHECKED on atoms. A two-line potential proof is supplied (§4.3).
- **G4 (presentation).** Several assessments are written like theorems (§5 below):
  - "if and only if", in bold, in §0.4;
  - "ordinal shadow of separability";
  - "no exploitation argument".

  Restate them as assessments. Note also that an additive score with a non-cone acceptance rule can violate (Add): Ex H, and majority Ex V.

**Side result (Remark 4.3), stated exactly.** It is correct and needs neither (Add), (IB) nor (TC).

> Call a ranking *Brier-compatible* if, at every world i, X ⪯_i Y ⇒ m_i(X) ≥ m_i(Y). Let X be any non-Bayes model that a Brier-compatible ranking leaves undominated. This holds in particular for X = D_K in any Brier-compatible cover of a non-singleton credal set K. Then for every ε > 0 there are a world i and a record r applying to X with
> - m(r) ∈ int ℝⁿ₊ (a strict Brier improvement at every world),
> - size(r) := μ(supp r) + ∫_{supp r}|h| dμ < ε,
>
> such that X ⊕ r ⋠_i X.

Only the weak direction of Brier-compatibility is used. R_lex and Δ(𝒩) are Brier-compatible. Veto–Brier is not.

---

## 1. Verdict table

| # | Item (AD65 numbering) | Verdict | Repair / note |
|---|---|---|---|
| 1 | Lemma 1.1 (under (IB), (Add) ⟺ Acc_i closed under ⊔) | CORRECT | Uses decomposability, which is in the setting. |
| 2 | Prop 3.1(a)–(d) | CORRECT | (d) also uses decomposability, via the converse of OR64 Prop 1.2. |
| 3 | Prop 3.1(e): complete + (TC) ⇒ (Tr) ⇒ (Add) | CORRECT | |
| 4 | Prop 3.1(f): "(Add) implies neither reflexivity nor weak (G); witness: only the null record" | **ERROR** (minor) | The null-record relation is reflexive and only witnesses weak-(G) failure. Use Acc = ∅ for reflexivity. |
| 5 | Prop 3.2 (Tr ⟺ Canc; (Add) = Canc with c null; (TP) = Canc with guided 2nd step) | CORRECT | All disjointness and composability identities re-derived (§2.1). |
| 6 | Props 3.3, 3.4 (and the partition restatement) | CORRECT | The partition restatement needs (IB), not (TC). |
| 7 | Prop 3.5 ((IB) and (Add) independent) | CORRECT once A is repaired | Witnesses: A′ (§2.2) and F. |
| 8 | Ex A as defined (Br minus one record): (TP) holds | **GAP** (atom artefact) | (TP) fails when cells can be cut (refinement k = 2; proof §2.2). Repair A′: delete the (TP)-preimage closure of R plus its tie inverses (PROVED; CHECKED k = 1, 2). |
| 9 | Ex B | CORRECT | CONTINUUM-EXACT when the cells partition U. |
| 10 | Ex C, D, D′ | CORRECT | CONTINUUM-EXACT, including (TC) for D and D′ over all measurable triples. The cell descriptions are checked equal to the atom closures at k = 1, 2. |
| 11 | Ex E as defined ("(Add) closure"): (TP) holds | **GAP** | (TP) fails at refinement k = 2. With the (Add)+(TP) closure, every claim holds: CONTINUUM-EXACT, with (FCC) by the deletion lemma since every accepted non-null record is Brier-strict. |
| 12 | Ex F | CORRECT | Continuum version: Φ = m_i + κ μ(X∩a)μ(X∩c), with κμ(a) < inf_c |h_i| (PROVED; CHECKED k = 2). |
| 13 | Ex G | **GAP** (atom-only) | A continuum relation with the same vector exists (SAT + exact verification, `sat_lattice.out`, (G*)). |
| 14 | Ex H | CORRECT | Continuum version: G ∪ {r : m_i(r) ≥ 0, size(r) < ε} (PROVED, §3.2). |
| 15 | "Apart from (Tr) and complete + (TC), nothing implies (Add)" | **GAP** (no witness for complete + (IB) + (TP)) | Ex V (majority of three weighted Brier scores) is complete, (IB), (TP), strict (G), and fails (Add) (PROVED; CHECKED). |
| 16 | Summary "the only implications are those of Prop 3.1" | CORRECT after 13, 15 and (K*) | Missing witness complete + (IB) + (Add) ⇏ (TP) supplied as (K*). The full lattice is in §2.4. |
| 17 | Prop 4.1 (unanimity of additive scores ⇒ (Add)) | CORRECT | The prose gloss "separable accuracy gives (Add)" overstates it; see 23. |
| 18 | Lemma 4.2 (rigidity) | CORRECT | Lyapunov step checked: ν is finite and non-atomic, and equal k-splitting holds by induction. |
| 19 | Remark 4.3 (side result) | CORRECT | Exact statement in §0. |
| 20 | Prop 5.1 (pure guidance: transitive; protects every coherent model) | CORRECT | Protects every model containing int ℝⁿ₊ ∩ U. |
| 21 | Theorem 5.2(a)–(c) (R_lex) | CORRECT | Line-by-line in §4.2. Defender records rec(N,X) under (★) are accepted at every world and never deleted; independent atom check passes. |
| 22 | Theorem 5.2(d), Cor 5.3: "R_lex(all coherent) is a universal cover iff (H)" | CORRECT | "Universal" should carry the scope "within the fixed U = D_{K′}: every K with K′ ⊆ relint K" (AUDIT_r65 scope correction 2). |
| 23 | Cor 5.3 text, §0.5, §6.1: "(G)+(IB)+(TC)+(Add) admits a universal cover iff (H)"; "cover of the reversed triangle iff (★) for some 𝒩 ∋ D_K"; "R_lex(𝒩) covers K iff (★) for 𝒩" | **ERROR** (E1) | Replace "iff" by "if" at framework level. For R_lex(𝒩): "covers K *with undominated set exactly 𝒩* iff (★)". "Covers K" ⇒ (★) for 𝒩 is unproved and too strong (§4.2). |
| 24 | Plain-Brier variant | CORRECT | |
| 25 | Prop 5.4 (M1⁺ breaks E61's box lemma under (Add)) | CORRECT; (FCC) was GAP | Potential proof of (FCC) supplied (§4.3); CONTINUUM-EXACT check of (TC) and (Add) on OR64's cells. |
| 26 | Prop 5.5 (𝒯⁺ transitive; keeps all of 𝒯's conclusions) | CORRECT | Equivalence (i)+(ii), transitivity, strict (G) and (b)–(e) re-proved. Transitivity also CONTINUUM-EXACT at all three worlds. |
| 27 | Correction to REF64_es §5.4 | CORRECT | (Add) excludes the relations, not the phenomena. REF64_es's sentence "OR64's two (TC)-only conclusions are specific to frameworks without (Add)" is false. |
| 28 | Open item: (TP)-closure of R_lex | CORRECT as labelled | The reasoning that closure keeps (TC), (FCC), (Add), (TP) and strict dominance was checked. Protection is correctly CONJECTURE. |
| 29 | §0.4, §2.1(4), §4: "incomparability under (Add) must be content-based and scale-free"; "scale-sensitive trust violates (Add)" | **ERROR** (E2) | Counterexample Ex T (§3.3). Correct form: (Add) forbids "trust small, suspend large" (Lemma 4.2) but permits "suspend small, trust large". |
| 30 | §0.4: "Accuracy supports (Add) **if and only if** each world's verdict is an additive evaluation" | **GAP** (an assessment presented as a theorem) | Restate: Prop 4.1 gives (Add) for *unanimity (cone) acceptance* of additive evaluations. Additive scores with other acceptance rules may fail (Add) (H, V) or satisfy it (T). |
| 31 | §2.2(1): "No exploitation or money-pump argument supports it" | **GAP** (presentation) | Qualify: no sure-loss argument that does not equally target incompleteness, which the framework permits. |
| 32 | §2 balance; §6.2–6.3 recommendation | CORRECT in substance | Clearly labelled as assessment. Add Ex T and Ex V to the balance (§5). |

---

## 2. §3: logical relations

### 2.1 Proof checks

**Lemma 1.1.** For disjoint-support r₁ and r₂:
- put X = A₁∪A₂, Y = B₁∪A₂, Z = B₁∪B₂;
- then rec(X,Y) = r₁, rec(Y,Z) = r₂, X△Y = A₁∪B₁ and Y△Z = A₂∪B₂, which are disjoint;
- and rec(X,Z) = r₁⊔r₂.

Conversely, disjoint changes give records with disjoint supports and rec(X,Z) = r₁⊔r₂. ✓

**Prop 3.1.**
- (a), (b) and (e) are immediate.
- (c): (TP) with Y = X gives weak (G). ✓
- (d): composition is commutative, and every composable pair is realised in either order (decomposability). ✓
- (f) is **E3**. The relation "only the null record" accepts (∅,∅), so X ⪯ X holds and it is reflexive. A non-reflexive (Add)-relation is Acc = ∅.

**Prop 3.2.** Put c = (P₁∩N₂, N₁∩P₂), r = (P₁∖N₂, N₁∖P₂) and s = (P₂∖N₁, N₂∖P₁). I re-derived all of the following:
- r⊔c = r₁;
- s⊔c⁻¹ = r₂;
- the supports of r, s and c are pairwise disjoint. The 8 cross-intersections reduce to P₁∩P₂ = N₁∩N₂ = ∅ or to set differences;
- r₁∘r₂ = r⊔s;
- for the converse: r⊔c and s⊔c⁻¹ are composable, and their composite is r⊔s.

So (Tr) ⟺ (Canc), (Add) = (Canc) with c null (with composability, c null ⟺ (X△Y) ∩ (Y△Z) = ∅), and (TP) = (Canc) with s⊔c⁻¹ guided. ✓

"Transitivity = (Add) + cancellation" is correct in the precise sense (Tr) ⟺ (Add) ∧ (Canc with c ≠ 0).

**Props 3.3 and 3.4.**
- Suppose Z ⪯ X. If Y ≺ Z, (TC) on Z ⪯ X ⪯ Y forbids it. If X ≺ Y, (TC) on Y ⪯ Z ⪯ X forbids it. ✓
- 3.4 is immediate. ✓
- The restatement "(Add) iff every non-accepted change has a non-accepted part in every finite partition" follows from Lemma 1.1 by induction. It needs (IB) only.

### 2.2 The examples on an actual record structure (brief item: (IB) "not only abstractly")

**On the atom algebras.** `examples_ref.py` re-verifies all eight examples independently. (IB) is checked in the literal W62 form, over every S, for every record-defined example; F is the only example failing (IB), as claimed. Every property value in AD65's Table 3.6 agrees.

**On the intended setting.** μ is atomless, so a record can cut a cell, and "atom" examples are relations on a finite algebra only. Two kinds of check were made:
- **Refinement:** split each atom into k = 2 same-sign pieces and apply the same definition.
- **CONTINUUM-EXACT check** (§2.3), for the combinatorial examples.

| Ex | Stated definition in the continuum | Status |
|---|---|---|
| A | (TP) **fails** (refinement k = 2). By hand: take G₁ ⊆ x₁ small, F ⊆ G₁ non-null, and r = (A_R ∖ G₁, F) with m(r) > 0. Then r ∈ Acc, and g = (G₁, ∅) is guided and composable with r. But r∘g = (A_R, ∅) = R is refused. | **GAP → repaired A′** |
| B | Holds; needs supp R = U (cells partition U) | CONTINUUM-EXACT |
| C, D, D′ | Hold (cells partition U) | CONTINUUM-EXACT |
| E | The (Add)-closure fails (TP) (refinement k = 2) | **GAP → (Add)+(TP) closure**, CONTINUUM-EXACT |
| F | Product version holds | PROVED; CHECKED k = 2 |
| G | Not definable by lifting | **GAP → (G*)**, CONTINUUM-EXACT |
| H | Size-threshold version holds | PROVED (§3.2) |

**Repaired A′ (PROVED; CHECKED k = 1, 2 in `examples_ref.out`).**

*Definitions.*
- Let D be the least set of records that contains R = (x₁∪y₁∪x₂∪y₂, ∅) and satisfies: "r∘g ∈ D for some guided g composable with r ⇒ r ∈ D". This is the intersection of all such sets.
- Let D₂ := {t⁻¹ : t ∈ D, m_i(t) = 0}.
- Put Acc := Br_i ∖ (D ∪ D₂).

*Invariant.* Every r ∈ D adds all of Y := y₁∪y₂.
- R does.
- If r∘g adds Y, then since Y ⊆ neg_i and P_g ⊆ pos_i, we get Y ⊆ P_r∖N_g ⊆ P_r.

*Properties.*
- **(Add) fails.** r₁ = (x₁∪y₁, ∅) and r₂ = (x₂∪y₂, ∅) are accepted: they have m = 1 > 0, each misses half of Y so is not in D, and they are not ties so are not in D₂. Their union R is refused.
- **(TP).** Let r ∈ Acc and g be guided and composable with r.
  - m_i(r∘g) = m_i(r) + m_i(g) ≥ 0.
  - r∘g ∉ D, by the closure property.
  - r∘g ∈ D₂ would force m_i(g) = 0, so g is null and r∘g = r ∈ D₂, which is impossible.
- **Strict (G).** Guided records do not add Y, so they are not in D, and they are not ties.
- **Tie-symmetry and (FCC).** Tie-symmetry holds by the construction of D₂. Then (FCC) follows by the deletion lemma, and (TC) with it.

### 2.3 The CONTINUUM-EXACT method (`cellcheck.py`)

**Setting.** U is partitioned into finitely many non-null sign-homogeneous cells.

**Acceptance depends only on label sets.** For C, D, D′ (and B, E, M1⁺, 𝒯⁺, G*, K*), whether a record is accepted depends only on, for each cell, the set of labels {P, N, U} occurring with positive measure. Here P means in A, N means in B and U means untouched.

**Triples reduce to finitely many cases.** For a model triple, each point has a type in {0,1}³. Since μ is atomless, the non-null type sets per cell range over *all* non-empty subsets of the 8 types. Every label set of rec(X,Y), rec(Y,Z), rec(X,Z) and rec(Z,X) is a function of these type sets. So the following properties, each quantified over all measurable triples, reduce to a finite exhaustive enumeration:
- (TC) and (Tr);
- (Add), which excludes the types 010 and 101;
- (TP).

**Two checks of the method.** A negative control (an (Add)-violating relation) is detected. The cell descriptions agree with the atom closures at refinement k = 1, 2.

### 2.4 The full implication lattice (properties: IB, TC, FCC, Add, TP, Tr, complete; always with reflexivity and strict (G))

**Implications (all PROVED in AD65 Prop 3.1).**
- Tr ⇒ FCC ⇒ TC.
- Tr ⇒ Add.
- Tr ⇒ TP.
- complete + TC ⇒ Tr.

**No others hold.** For each property, every maximal combination of the others that does not imply it already has a continuum witness:

| Property fails | While these hold | Witness |
|---|---|---|
| IB | Tr, complete | F |
| Add | IB, TC, FCC, TP | A′ |
| Add | IB, TP, complete | **V** (new) |
| TP | IB, TC, FCC, Add | B |
| TP | IB, Add, complete | **K*** (new; SAT, CONTINUUM-EXACT) |
| TC | IB, Add, TP, complete | **G*** (continuum G) |
| FCC | IB, TC, Add, TP | D′ |
| Tr | IB, TC, FCC, Add, TP | E (with the (Add)+(TP) closure) |
| complete | everything else | pure guidance |

**Small cases are misleading** (`lattice.py`). An exhaustive census of all 16 384 strict-(G) record relations on 3 atoms *validates* two implications that are false in general:
- (TP) ⇒ (Add);
- (TC) + (TP) ⇒ (FCC).

A′, D′ and V refute them. This is why AD65's 4-atom examples are necessary. A 2-SAT search (`sat_complete_tp.py`) confirms that complete + (TP) ⇒ (Add) holds on 3 atoms and fails from 4 atoms on.

---

## 3. §4: accuracy, rigidity, Example H, the side result

### 3.1 Prop 4.1 and Lemma 4.2
Both are correct.

In Lemma 4.2:
- ν takes values in ℝ^{3n+1}, is finite because μ is finite and has a first moment, and is non-atomic because μ has a density.
- Lyapunov gives S with ν(S) = ν(A∪B)/k; recurse on the complement.
- Each piece has m(r_j) = m(r)/k ∈ C and size(r)/k < ε.
- k−1 applications of (Add) give r.

### 3.2 Example H in the continuum (PROVED)
Acc_i := G_i ∪ {r : m_i(r) ≥ 0, size(r) < ε}.
- **Sub-Brier and tie-symmetric:** size(r⁻¹) = size(r), and a non-null guided record is never a tie. So (TC) and (FCC) hold by the deletion lemma.
- Reflexivity, strict (G) and (IB) are immediate.
- **(Add) fails:** apply Lemma 4.2 to a non-guided record with m_i > 0 and size ≥ ε.
- **(TP) fails:** compose a small non-guided accepted record with a large guided one.

AD65's description "satisfies every binding axiom" should read "every binding *single-world* axiom". The cover requirements are multi-world.

### 3.3 Ex T: (Add) permits magnitude-based incomparability (refutes E2; PROVED; CHECKED `extra_examples.out`)

Acc_i := G_i ∪ {r : m_i(r) ≥ c}, with c > 0.

- **Transitive.** If both records are guided, so is their composite. Otherwise m_i(r₁∘r₂) = m_i(r₁) + m_i(r₂) ≥ c + 0.
- **Other properties.** It is reflexive and satisfies strict (G) (inverses of guided records have m_i < 0) and (IB). Being transitive, it satisfies (TC), (FCC), (Add) and (TP).
- **Incomplete.** Every non-guided record with |m_i(r)| < c is unranked in both directions.

So a world may, consistently with (Add) and even transitivity, decline to rank Brier improvements below a materiality threshold. Lemma 4.2 forbids only the converse pattern, "trust small, suspend large".

AD65's "incomparability under (Add) must be content-based and scale-free" (§0.4), its §2.1(4), and its §4 table row "scale-sensitive trust … violates (Add)" must be corrected accordingly. The correct statement is: **under (Add), the set of suspended changes is closed under coarsening of partitions in the sense of Prop 3.4, so suspension of large changes must be inherited by some part. Suspension of small changes is unconstrained.**

### 3.4 Ex V: majority over accuracy measures (PROVED; CHECKED)

**Definition.** Let s_k(r) := ∫_A w_k h_i − ∫_B w_k h_i for k = 1, 2, 3, with weights w_k > 0. Put Acc := {r : s_k(r) ≥ 0 for at least two k}.

**Properties.**
- **Complete:** if fewer than two s_k(r) are ≥ 0, then at least two s_k(r⁻¹) are > 0.
- **(TP):** s_k(r∘g) ≥ s_k(r) for guided g.
- **Strict (G)** and **(IB)** hold.
- **(Add) fails, hence (TC) fails.** With w = (5,1,1,9), (1,5,9,1), (3,3,2,2) on cells a, b (right) and c, d (wrong), r₁ = (a∪c, ∅) and r₂ = (b∪d, ∅) score (4, −8, 1) and (−8, 4, 1). Their union scores (−4, −4, 2). (TC) then fails because complete + (TC) ⇒ (Add).

Normative upshot: Prop 4.1's "imprecise accuracy respects (Add)" depends on *unanimity*. Majority aggregation of admissible scores violates it. The §4 table should say this.

### 3.5 Remark 4.3 (side result)
Correct as stated in §0. The proof:
- ES64 Lemma 5.1 gives N_π with m(N_π) − m(X) ∈ int ℝⁿ₊.
- Lemma 4.2's splitting gives sub-records r_j of rec(N_π, X). Each applies to X, with m(r_j) ∈ int ℝⁿ₊ and size(r_j) < ε.
- If all were accepted at every world, Brier-compatibility would make X ⊕ r_j ≺_i X at every i.

The proof uses no (Add), (IB) or (TC). "No non-Bayes K is covered" needs D_K to be non-Bayes, which holds for non-singleton K.

---

## 4. §5: the strengthened-framework branch

### 4.1 Prop 5.1 — CORRECT
- Transitivity of guidance: X∖Z ⊆ (X∖Y)∪(Y∖Z) ⊆ pos, and similarly for Z∖X.
- Protection: a record guided at every world has Y∖N ⊆ int ℝⁿ₊ and N∖Y ⊆ U ∩ (−int ℝⁿ₊) = ∅, and int ℝⁿ₊ ∩ U ⊆ D_Q.
- CHECKED independently (`rlex_check.out`).

### 4.2 Theorem 5.2 and Cor 5.3

**(a) — CORRECT.**
- Reflexivity: null ∈ G_i.
- Strict (G): a non-null guided g has m_i(g) > 0, so L_i(g⁻¹) <_lex 0, and g⁻¹ is not guided.
- (FCC)/(TC): every accepted record has L_i ≥_lex 0; accepted ties are null or lie in T_i, which is inverse-closed. The deletion lemma for a totally ordered score (ℝ² lex) applies.
- (Add):
  - the Fact holds: if r₁⊔r₂ attacks Z then r₁ attacks Z, so NA is upward-closed under ⊔;
  - lex-sums of terms ≥_lex 0 are ≥_lex 0, and a lex-sum equal to 0 forces both terms to be 0;
  - in the tie case, r₁⁻¹ ∈ NA by T_i, so (r₁⊔r₂)⁻¹ ∈ NA by the Fact. ✓

**(b) — CORRECT.** rec(Y,N) applies to N, so it attacks N and is not in NA. It is therefore guided at every world, hence null.

**(c) — CORRECT.**
- (⇐) Under (★), r = rec(N,X) ∈ NA has L_i(r) >_lex 0 at every i: either m_i > 0, or m_i = 0 and Σ_j m_j > 0. Also r⁻¹ ∉ Acc_i, since L_i(r⁻¹) <_lex 0 and r⁻¹ is not guided. So **the defender's comparison is accepted, strictly, at every world, and never deleted.**
- (⇒) If r ∉ NA, then r is guided at every world, so r = (N∖X, ∅) with N∖X ⊆ int ℝⁿ₊. That r attacks no member, a contradiction.
- (⇒) If r ∈ NA, then m(N) ≥ m(X). Equality would put r in T_i at every world, and then X ⪯_i N at every world.
- CHECKED independently on 12 random 7-atom systems: axioms, protection, (★) ⟺ dominated by a member, strictness at every world, defenders accepted (`rlex_check.out`).

**(d) and Cor 5.3 — CORRECT for the relation R_lex(all coherent).**
- For 𝒩 = all coherent models, rec(N,X) ∈ NA ⟺ μ((N∖X) ∩ hull(X∖N)) > 0. This holds because hull(B) = D_{Q_B} is itself coherent (K′ ⊆ Q_B since B ⊆ U) and is the least coherent model containing B.
- (⇒): if R_lex(all coherent) covers even one K, then each incoherent X is dominated by a coherent undominated model, which is a member. By (c), (★) holds at X.

**E1: the framework-level "iff" is not proved.**
- Cor 5.3's sentence "(G) + (IB) + (TC) + (Add) … admits a universal cover iff (H)", §0.5's "same universal cover, conditional on the same (H)", and §6.1's three "iff"s are fine in the "if" direction.
- The "only if" direction would require that *every* (Add)-relation cover yields (H). Nothing shows this: covers need not be Brier-compatible (veto–Brier covers exist), so dominators need not satisfy m(N) ≥ m(X).
- AUDIT_r65 scope correction 3 makes the same point for the binding framework.

**The target-specific remark is unproved, and too strong, in the "only if" direction.** The remark is "R_lex(𝒩) with D_K ∈ 𝒩 covers K iff (★) holds for 𝒩".
- For any 𝒩, every Bayes act N_π is undominated in R_lex(𝒩). Indeed, a dominator Y needs rec(Y,N_π) ∈ NA with m(Y) ≥ m(N_π), which forces π·m(Y) = π·m(N_π) and hence Y = N_π; or rec(Y,N_π) is guided everywhere, hence null.
- So (★) for 𝒩 fails at N_π whenever N_π ∉ 𝒩. A cover, however, requires only that the undominated models be coherent, and N_π is coherent. Nothing shows that "R_lex(𝒩) covers K" forces (★) for 𝒩, and the natural reading is false whenever such an R_lex(𝒩) covers K.
- **Repair:** "R_lex(𝒩) covers K *with undominated set exactly 𝒩* iff (★) for 𝒩". For 𝒩 = all coherent the two readings coincide.

**Scope of "universal".** Add "within the fixed U = D_{K′}: covers every K with K′ ⊆ relint K" (AUDIT_r65 scope correction 2).

### 4.3 Prop 5.4 (M1⁺) — CORRECT; (FCC) proof supplied

**Checked.**
- (Add): G⊔G ⊆ G; (r₀⊔g)⊔g′ = r₀⊔(g⊔g′); and two r₀-type records are never disjoint.
- Strict (G): r₀⊔g adds A ⊆ pos_j at j and E ⊆ pos_i at i, so it is never an inverse-guided record.
- (TC): the composite of r₀⊔g₁ with a guided g₂ still adds A at j, and E at i, because g₂ removes only wrong gambles. So its inverse is neither guided nor of r₀-type (it would have to add B ⊆ N_{r₁}).
- The priority region and the domination of X_i are as in OR64.

**(FCC), PROVED.** At j, put

  φ_j(X) := α·μ(X∩A) + μ(X∩B) − μ(X∩E) + m_j(X ∖ (E∪A∪B)),  with α > (μ(B)+μ(E))/μ(A).

- Every non-null guided record raises φ_j: guided records at j only add A and B, and only remove E.
- r₀⊔g raises φ_j by at least αμ(A) − μ(B) − μ(E) > 0.
- So all non-null accepted records strictly raise φ_j, and the deletion lemma gives (FCC).
- At i, use α·μ(X∩E) + μ(X∩B) − μ(X∩A) + m_i(·) with α > (μ(A)+μ(B))/μ(E).
- k is pure guidance.

CONTINUUM-EXACT re-check of (TC) and (Add) at all three worlds on OR64's 8 cells: `cellcheck.out`.

### 4.4 Prop 5.5 (𝒯⁺) — CORRECT

**The equivalence (i)+(ii).**
- A decomposition t⊔g must put the away parts in g. This forces (i).
- A non-null t that is not anti-guided supplies a right toward-move. A null t leaves a guided toward-part, which is not anti-guided.
- Conversely, take t := the toward part and g := the away part.

**Transitivity.**
- (i) is inherited, since P_c ⊆ P₁∪P₂ and N_c ⊆ N₁∪N₂.
- For (ii): a wrong toward-move in c comes from some r_k, which then has a right toward-move y.
- y is cancelled only if y ∈ N₂∩IN∩pos_w or y ∈ P₂∩OUT∩neg_w. Both are excluded by (i) for the other record.

**Strict (G).** The inverse of a guided record satisfying (i) is an all-wrong toward-move, which violates (ii).

**(b)–(e).** These reduce to: a record applying to D_K is a pure away-move, accepted iff guided; a pure toward-move is accepted iff it is not anti-guided. For (d), the toward part of rec(Y,X) with X ∈ 𝓘_w is all-wrong at w, hence null.

**Checks.** CONTINUUM-EXACT (`cellcheck.out`): reflexivity, strict (G), (TC), **(Tr)**, (Add) and (TP) at all three worlds on OR64's 9 cells. AD65's `diag.out` re-checks (b)–(e) on atoms.

**Consequence.** OR64's 𝓘-localisation holds under (G)+(IB)+transitivity. I confirm.

### 4.5 The correction to REF64_es §5.4 — CORRECT
REF64_es §5.4 is right that (Add) excludes Δ(𝒩), M1 and 𝒯 (ES64 §5.3(3) and its two direct arguments). It is wrong that "OR64's two (TC)-only conclusions are specific to frameworks without (Add)": M1⁺ and 𝒯⁺ refute that. Its "protection-for-free under (Add)?" question is answered "yes" by Prop 5.1, even under transitivity.

**One correction to AD65's own correction.** Its answer to "a cover of the reversed triangle?" is "iff (★) for some 𝒩 ∋ D_K". This should be "if" (E1).

### 4.6 The open (TP) item
The argument that (Add)+(TP) closure of R_lex keeps the relational axioms and strict dominance under (★) is correct:
- composition with a non-null guided record raises L_i strictly;
- ties in the closure are ⊔-sums of T_i-ties, whose inverses are in the closure.

Protection is correctly labelled CONJECTURE.

---

## 5. Normative assessment (§2, §0, §6): fairness and separation

**Separation.** On the whole it is good.
- §2 ends with "Balance (assessment, not a theorem)".
- The status table marks row 12 as assessment.
- §6.3 explicitly declines to propose a representation hypothesis.

Four places blur the line.
1. **§0.4 "Accuracy considerations support (Add) if and only if …"** (bold). This is an assessment phrased as a biconditional theorem, and its "if" half is not what Prop 4.1 proves.
   - Prop 4.1 needs **cone (unanimity) acceptance** of additive evaluations.
   - With the *same additive Brier score*, Ex H (trust region) and Ex V (majority of weighted Briers) violate (Add), while Ex T (threshold) satisfies it.
   - Suggested text: "Among the accuracy considerations examined, only one yields (Add): that each world accepts exactly the changes which a fixed family of additive evaluations unanimously rates non-negative (possibly together with guided changes; Prop 4.1). Additivity of the score alone does not yield it."
2. **§0.3/§2.1(1) "(Add) is the ordinal shadow of separability".** For the same reason, this is suggestive but too strong. Separability of the score is neither sufficient (H, V) nor necessary (R_lex and 𝒯⁺ satisfy (Add) without being score-based).
3. **E2 (§0.4, §2.1(4), §4).** "Scale-free" and "scale-sensitive trust violates (Add)" are refuted by Ex T. This also weakens §2.1(4) as an argument *for* (Add): (Add) does not force incomparability to be principled in any scale sense. It forbids only accumulation-type suspension.
4. **§2.2(1) "No exploitation or money-pump argument supports it".** Defensible for sure-loss arguments. Note, however, that the standard money-pump pressure on incomplete preferences (trading through incomparable options) applies to (Add)-failures as to any incompleteness. So qualify: "no pragmatic argument specific to (Add), beyond those against incompleteness itself, which the framework deliberately permits."

**Fairness.** The case for and against is balanced and accurate in substance. Two additions would make it fairer.
- **Against (Add).** Lemma 4.2 is itself the formal content of an *accumulation/sorites* objection: a world that accepts every small improvement in a cone must accept every improvement in it, however it is assembled. Someone who distrusts aggregated verdicts (Temkin-style) would reject (Add) on exactly these grounds. AD65 states the lemma but presents it only as a point for (Add).
- **For and against.** Ex T shows (Add) is compatible with a natural "materiality" view of incomparability. Ex V shows that majority-based imprecision about the accuracy measure is not.

**Nothing in §2 or §4 is stated as PROVED that is only an argument**, apart from the §0.4 biconditional (item 1) and the "must be" in item 3. The status-table rows 1–20 match their proofs, with the corrections E1–E3 and G1–G3 above.

**The recommendation (§6.2)** is that adopting (Add) "neither helps nor harms (H)" and is a free choice about separable accuracy. This is supported by Prop 5.1, Thm 5.2, Prop 5.4 and Prop 5.5, once E1 is corrected. Its tenor is consistent with AUDIT_r65: (Add) is not adopted, and the results are labelled strengthened-framework.

---

## 6. Files (`ref65ad_py/`)

| File | Content | Result |
|---|---|---|
| `rel.py` | independent property checker (literal W62 (IB) over all S; TC, FCC, Add, TP, Tr, completeness) and record closures | library |
| `examples_ref.py` → `.out` | Ex A–H re-verified on atoms; refinement k = 2; repaired A′; E with (Add) vs (Add)+(TP) closure | A naive and E-(Add) **differ** at k = 2; all others as claimed |
| `cellcheck.py` → `.out` | CONTINUUM-EXACT checks: C, D, D′; M1⁺ and 𝒯⁺ per world; negative control; agreement with atom closures | ALL AS CLAIMED |
| `cellcheck_BE.py` → `.out` | CONTINUUM-EXACT: B; E with (Add)+(TP) closure | ALL AS CLAIMED |
| `lattice.py` → `.out` | census of all 16 384 strict-(G) relations on 3 atoms; implications valid on 3 atoms | shows (TP)⇒(Add) and (TC)+(TP)⇒(FCC) hold on 3 atoms only |
| `sat_complete_tp.py`, `sat_witness.py` → `.out` | 2-SAT: complete + (TP) without (Add) | UNSAT on 3 atoms; SAT from 4 atoms |
| `sat_lattice.py` → `.out` | SAT + independent exact verification: continuum G* and K* | both exist |
| `extra_examples.py` → `.out` | Ex T (threshold: transitive, (Add), incomplete) and Ex V (majority: complete, (TP), not (Add)) | ALL AS CLAIMED |
| `rlex_check.py` → `.out` | independent R_lex(𝒩) and pure-guidance checks on 12 random 7-atom systems | ALL PASS |
