# S1. (R4) Nestedness from (S): proof side

15 Oct 2026, round 13 (BRIEF12, task R4, proof side). Scripts: `s1py/` (run with `python3 -I`).

- **Read:** TERMFIX_RULES; write-up §§2–3, §7.7, §8.4(c), §8.5 (all); Q1, Q2, Q3 notes; Q3_referee (§4); Q12_referee
  (§§2.5, 4, 6); P4_notes Part B; P4B_referee (Lemma N0, B0, B1, DL, DR, T).
- **Labels:** PROVED / CHECKED / CONJECTURE / NUMERICS. No assumption is added to the framework. Conditional
  statements name their extra hypothesis in the statement, and that hypothesis is never claimed as derived.

---

## 0. Outcome

**Two worlds.** Conjecture Q2.N is not settled in full. What is proved:

1. **C_L is a graded linear continuum** (§2). In two worlds, two members of C_L that are tied at one world are tied
   at both (Level Lemma S1.1). Hence:
   - ⪯₁ restricted to C_L is a total preorder whose ties are double ties, and ⪯₂ is its reverse;
   - the quotient C_L/~ is a compact connected linear order, and p ↦ [C_p] is continuous onto it;
   - every model X has a closed dominator interval [l_X, u_X] in C_L/~;
   - strict escape holds without nestedness.
2. **Crossings are rigid** (§3). If two members of C_L cross, then every non-segment splice of the two is strictly
   comparable with each of them, in the same direction at both worlds. The mixed patterns (tie at one world,
   incomparability at the other) are impossible. A double tie with an incoherent splice is excluded by (C).
3. **Continuity forces nestedness** (Theorem S1.6). Suppose one world is monotonely continuous on M (for instance,
   additive with an integrable density, or (CP-a) with a countably additive credal set). Then C_L is a chain, so
   Q2.N holds, and with it the whole nested analysis of §8.5(c), Prop Q15 included.
   - The same conclusion holds under a weaker hypothesis, (MC_sel): monotone closedness, in model space, of the
     sections of members of C_L.
4. **The true residual** (§4). A non-nested two-world system must have a rigid crossing (two crossing ~-classes) or
   a tied crossing (one class with crossing members). Either way **both** worlds fail (MC_sel) on the crossing
   region, through a non-Archimedean switch.
   - If the classes are singletons, no nested selection exists for those orders, so substitute (a) of the brief is
     then false.
   - "Some nested selection with the same C_L exists" is equivalent to the existence of nested class
     representatives (Prop S1.3).

**Edges (three worlds).** (Nest_e) does **not** follow from the edge-system axioms, i.e. from everything Prop Q35
uses: Example S1.9 is a two-world edge system with strict (G), (IB), (K) and closed sections whose selection crosses.
So any derivation of (Nest_e) must use world 3, through undominatedness or (C). What is proved:

- Weak edge undominatedness (S1.10).
- Under the extra hypothesis (EU_ij), that edge-selected models are not weakly dominated at i and j by an edge test
  model with one strict:
  - the Level Lemma holds on the edge;
  - the edge classes form a continuum;
  - crossings on edges are rigid or doubly tied (S1.11).
- Under (EU_ij) plus monotone continuity at one edge world, every crossing pair can be straightened pairwise. On the
  family D_{M_{x,y}} of Prop comonotone the straightened model is again a coherent edge model D_{M_{x″,y}}
  (S1.12).
- Global straightening is a CONJECTURE (S1.13). §5.6 records exactly where the maximal-chain argument stops.

Prop Q35 and Thm Q36 use only a nested family with (K) and closed sections. They never use that the family is
selected (Remark S1.8). So straightening, not (Nest_e) itself, is the right target on edges.

| # | Statement | Label |
|---|---|---|
| S1.1 | Level Lemma (n = 2): U, V ∈ C_L, U ~₂ V ⇒ U ~₁ V (and symmetrically) | PROVED |
| S1.2 | C_L/~ is a compact linear continuum; [l_X,u_X]; strict escape in L | PROVED |
| S1.3 | Nested selection (same orders) exists ⟺ nested class representatives exist | PROVED |
| S1.4 | Crossing agreement: admissible patterns (<,<),(>,>),(~,~),(~,∥),(∥,~) | PROVED; CHECKED `patterns.py` |
| S1.5 | Crossing pairs in C_L: every non-segment splice is strict and agreeing; (~,~) only on segments | PROVED |
| S1.6 | (MC) at one world, or (MC_sel), ⇒ C_L is a chain (Q2.N) | PROVED |
| S1.7 | Q2.N for additive / (CP-a) countably additive partner; Prop Q15 etc. without (Nest) | PROVED |
| S1.8 | Q35/Q36 need only a nested family with (K) and closed sections | PROVED (inspection of the recorded proofs) |
| S1.9 | Edge-system axioms do not force nestedness | PROVED; NUMERICS `plateau_edge.py` |
| S1.10 | Weak edge undominatedness | PROVED |
| S1.11 | Under (EU_ij): edge Level Lemma, continuum, rigid-or-tied crossings | PROVED (conditional) |
| S1.12 | Under (EU_ij) + (MC) at i or j: pairwise straightening, coherent on D_{M_{x,y}} | PROVED (conditional) |
| S1.13 | Global edge straightening | CONJECTURE |
| S1.R | (S) forces (MC_sel) (hence Q2.N) | CONJECTURE |

---

## 1. Setting and notation

**Two-world setting.** The setting is n = 2 on M_U, as in §8.5(d) of the write-up.
- K′ = [α′, β′] ⊂ (0,1), M = M⁻ ⊔ M⁺, with coordinates σ on M⁻ and τ on M⁺.
- The coherent models are D_{[α,β]}, with E₁ = {σ < α} ∪ {τ ≤ β} and E₂ = M∖E₁ (Prop lattice).
- The ranking satisfies strict (G), (IB), (LA), (S) (selection p ↦ C_p, p ∈ [0,1]), and (C).

**Orders on sets.** By (G) and (IB), world i is an order on world-i error sets with de Finetti cancellation.
- For sets a, b I write a ≤_i b when world i ranks the error set a no worse than b.
- For regular models, world 2 compares world-2 error sets M∖E₁.
- ∥ denotes incomparability and ~ a tie.

**Standard facts used.**
- C₀ = P₁ and C₁ = P₂. C₀ is competitive on {1}, so E₁C₀ is null by strict (G); mirror for C₁.
- **KKM covering.** For every model X, S₁(X) := {p : C_p ⪯₁ X} and S₂(X) are closed, and S₁(X) ∪ S₂(X) = [0,1].
  This uses competitiveness at interior p and at the vertices.
- **Thm kkm.** Every undominated model is tied at every world with a selected model. With (C), every undominated
  model is in C_L, hence coherent.
- Every C ∈ C_L is competitive on {1,2}. Indeed C is tied at both worlds with some selected C_s, and s is interior
  unless C ∈ {P₁, P₂}.

**Crossing pair.** C, C′ ∈ C_L *cross* if neither error set contains the other. By Prop lattice, after relabelling:
- E₁C = m ∪ B and E₁C′ = m ∪ A;
- A = {α_C ≤ σ < α_{C′}} ⊆ M⁻ and B = {β_{C′} < τ ≤ β_C} ⊆ M⁺, both non-null;
- m = E₁C ∩ E₁C′.

For a ⊆ A and b ⊆ B, the *splice* X_{a,b} is the regular model with E₁X_{a,b} = m ∪ a ∪ (B∖b).
- So X_{∅,∅} = C and X_{A,B} = C′.
- The splice is coherent iff a is σ-initial in A ({α_C ≤ σ < α} for some α) and b is τ-final in B
  ({β < τ ≤ β_C}). Then it is the lattice point D_{[α,β]} (Prop lattice). Such (a,b) is a **segment pair**; any
  other pair is **non-segment**.

---

## 2. Two worlds: the class structure of C_L

**Lemma S1.1 (Level Lemma; PROVED).** Let U, V ∈ C_L (coherent and undominated) with U ~₂ V. Then U ~₁ V.
Symmetrically, U ~₁ V implies U ~₂ V.

*Proof.*
1. **Common section.** U ~₂ V gives S₂(U) = S₂(V) =: G. This set is closed by (S), and it contains 1.
2. **0 ∉ G unless U = V = P₁.**
   - Suppose 0 ∈ G, i.e. P₁ ⪯₂ U. The world-2 error set of P₁ is M, and U's lies inside M because U is coherent,
     hence regular.
   - Strict (G) then forces E₂U = M, so U = P₁, and likewise V = P₁.
3. **The open set O.** Otherwise O := [0,1]∖G is open and nonempty (it contains 0), and O ≠ [0,1].
   - By KKM covering for U and for V, O ⊆ S₁(U) ∩ S₁(V).
   - That intersection is closed, so cl O ⊆ S₁(U) ∩ S₁(V).
4. **A boundary point.** [0,1] is connected, so O is not closed. Take q ∈ cl O ∖ O. Then q ∈ G, so C_q ⪯₁ U,
   C_q ⪯₂ U, C_q ⪯₁ V and C_q ⪯₂ V.
5. **Conclusion.** U and V are undominated, so none of these four relations is strict. Hence C_q ~ U and C_q ~ V at
   both worlds, and U ~₁ V.

The symmetric statement uses S₁ and the vertex 1. ∎

Inputs: (S) (closed sections, KKM covering), strict (G), undominatedness. Not used: (C), (LA), (IB), coherence
(except that U is regular).

**Corollary S1.2 (PROVED).**

(a) **Linear order.** On C_L, for U, V ∈ C_L: U ⪯₁ V ⟺ V ⪯₂ U, and every pair is comparable. The ties at world 1
are exactly the ties at world 2, i.e. double ties.

*Proof.*
- Competitiveness of U and of V gives four cases: (U ⪯₁ V or U ⪯₂ V) and (V ⪯₁ U or V ⪯₂ U).
- A tie at one world is a double tie by S1.1.
- In the remaining cases one model is weakly better at world 1 and the other weakly better at world 2.
- Undominatedness makes such a trade-off strict at both worlds unless it is a double tie.

(b) **Continuum.** Let 𝓛 := C_L/~ with the order of ⪯₁, and π(p) := [C_p].
- π is onto 𝓛, by Thm kkm.
- π⁻¹ of the closed rays are the closed sets S₁(U) and S₂(U), so π is continuous for the order topology.
- Hence 𝓛 is a compact connected linear order (a linear continuum with end points [P₁] and [P₂]).

(c) **Dominator intervals.** For every model X:
- R₁(X) := {W ∈ 𝓛 : W ⪯₁ X} = π(S₁(X)) is compact. Being a down-set, it is an interval [min, u_X].
- Likewise R₂(X) = [l_X, max].
- By (KKM covering) and density, l_X ⪯ u_X. The interval [l_X, u_X] consists of the classes that weakly dominate X
  (or tie it).

(d) **Strict escape without nestedness.** If X is regular, W ∈ C_L and E₁X ⊋ E₁W (non-null difference), then
u_X ≻ W.
- Every D ∈ [l_X, u_X] has D ⪯₂ X ≺₂ W.
- Hence W ≺ D by (a), so u_X ≻ W.
- Mirror: E₁X ⊊ E₁W ⇒ l_X ≺ W.
- This is Lemma G-SE read in 𝓛.

(e) **Inclusion closedness.** For S ⊆ 𝓛 with representatives W_s:
- sup S ⪯₁ X whenever E₁X ⊇ ess∪ E₁W_s;
- inf S ⪯₂ X whenever E₁X ⊆ ess∩ E₁W_s.

These are R₁(X), R₂(X) closed. ∎

So, in two worlds, C_L is always one-dimensional in the order sense. The open question is only whether the order of
𝓛 is compatible with inclusion of error sets.

**Proposition S1.3 (PROVED).** For a fixed ranking, the following are equivalent:
- some selection satisfying (S) has nested world-1 error sets;
- one can choose one representative from each ~-class of C_L so that the chosen error sets are nested.

In particular, if two distinct classes are singletons and their members cross, every selection for that ranking is
non-nested.

*Proof.*
- **Classes must be hit.** Every selection hits every class: apply Thm kkm to the new selection, whose image lies in
  C_L.
- **Construction.** Conversely, given nested representatives r(·), put C′_p := r(π(p)).
  - C′_p ~ C_p at both worlds, so C′_p has the same sections (closed) and the same competitiveness.
  - C′_p ∈ C_L. ∎

So substitute (a) of the brief ("a nested selection with the same C_L") is equivalent to nested representatives. It
is strictly weaker than (Nest) when some class has two crossing members (§4).

---

## 3. Two worlds: crossing pairs

**Lemma S1.4 (crossing agreement; PROVED).** Let C, C′ ∈ C_L cross, with A, B, m as in §1. For a ⊆ A and b ⊆ B,
cancellation gives:

| model pair | world 1 | world 2 |
|---|---|---|
| C ⪯ X_{a,b} | b ≤₁ a | a ≤₂ b |
| X_{a,b} ⪯ C | a ≤₁ b | b ≤₂ a |

For C′ use the splice Y_{a,b} with E₁Y = m ∪ (A∖a) ∪ b:

| model pair | world 1 | world 2 |
|---|---|---|
| C′ ⪯ Y | a ≤₁ b | b ≤₂ a |
| Y ⪯ C′ | b ≤₁ a | a ≤₂ b |

Competitiveness of C against X and of C′ against Y, together with undominatedness of both, leave exactly five
patterns for the pair (relation of a, b at world 1; at world 2):

  (<,<), (>,>), (~,~), (~,∥), (∥,~).

So the two worlds agree on every strict cross comparison, and an incomparability at one world forces a tie at the
other.

*Proof:* exhaustive case analysis over the 16 combinations; CHECKED by `s1py/patterns.py` (output
`patterns.out`). ∎

**Theorem S1.5 (crossings are rigid; PROVED).** Let C, C′ ∈ C_L cross.
- (i) For every non-segment pair (a,b), the pattern is (<,<) or (>,>). That is, X_{a,b} is strictly better than C
  at one world and strictly worse at the other, and the direction is the same as the strict comparison of a and b
  at both worlds.
- (ii) For a segment pair, the pattern (~,~) is also possible. Then the lattice point X_{a,b} lies in C_L, doubly
  tied with C.

*Proof.*
- **Excluding (~,~).** For a non-segment pair, X := X_{a,b} is incoherent.
  - (~,~) means X is tied at both worlds with C ∈ C_L, so X ∈ C_L by (C). That contradicts incoherence.
- **Excluding (∥,~).** Here X ∥₁ C and X ~₂ C.
  - By KKM covering and connectedness, S₁(X) ∩ S₂(X) ≠ ∅. So some selected C_r has C_r ⪯₁ X and C_r ⪯₂ X.
    Then C_r ⪯₂ C.
  - If C_r ~₂ C, then S1.1 gives C_r ~₁ C, so C ⪯₁ C_r ⪯₁ X. This contradicts X ∥₁ C.
  - If C_r ≺₂ C, then S1.2(a) gives C ≺₁ C_r ⪯₁ X. Same contradiction.
- **Excluding (~,∥).** The mirror argument applies, with the worlds exchanged.
- **(ii)** is (C). ∎

**Definition.** World i is **monotonely continuous on M**, (MC_i), if for all measurable Y_k, Y, Z ⊆ M:
- (Y_k ↑ Y and Y_k ≤_i Z for all k) ⇒ Y ≤_i Z;
- (Y_k ↓ Y and Z ≤_i Y_k for all k) ⇒ Z ≤_i Y.

**(MC_sel)** is the weaker property: sections of members of C_L are closed along monotone chains of regular test
models. For W ∈ C_L:
- if E₁X_k ↓ E₁X and W ⪯₁ X_k for all k, then W ⪯₁ X;
- if E₁X_k ↑ E₁X and W ⪯₂ X_k for all k, then W ⪯₂ X.

**Theorem S1.6 (PROVED).** If (MC₁) or (MC₂) holds, or (MC_sel) holds, then {E₁C : C ∈ C_L} is a chain. That is,
(α, β) is comonotone along C_L, and Conjecture Q2.N holds. It suffices that the hypothesis holds for chains inside
A and inside B of a putative crossing pair.

*Proof under (MC₁).* Suppose C, C′ ∈ C_L cross, and write ◁ for "strictly smaller at both worlds".
1. **A piece a with a ◁ B.**
   - Let a_k := {s ≤ σ < s + 1/k} with α_C < s. These are non-null, non-initial in A, and a_k ↓ ∅.
   - Every pair (a_k, b) is non-segment. By S1.5 it is strict, so either b ◁ a_k or a_k ◁ b.
   - If B ◁ a_k for all k, then B ≤₁ a_k for all k, and (MC₁) gives B ≤₁ ∅, contradicting strict (G).
   - Fix a := a_k with a ◁ B.
2. **The switch.** Put b(β) := {β < τ ≤ β_C} and 𝔅 := {β : b(β) ◁ a}.
   - β_C ∈ 𝔅, since b = ∅ and ∅ ◁ a by strict (G) at both worlds.
   - β_{C′} ∉ 𝔅. 𝔅 is an up-set, since b(β) shrinks as β grows.
   - Let β* := inf 𝔅.
3. **Two limits.**
   - For β > β*, b(β) ≤₁ a, and b(β) ↑ b(β*) as β ↓ β*. So (MC₁) gives b(β*) ≤₁ a.
   - If β* = β_{C′}, this reads B ≤₁ a, against a ◁ B.
   - Otherwise, for β < β*, a ◁ b(β), so a ≤₁ b(β), and b(β) ↓ b(β*). So a ≤₁ b(β*).
4. **Contradiction.** Hence a ~₁ b(β*). But (a, b(β*)) is a non-segment pair, which S1.5(i) requires to be strict.
   ∎

*(MC₂)* gives the mirror proof. S1.5 makes the strict relations of the two worlds coincide, so the same switch is a
world-2 switch.

*Proof under (MC_sel).* Read the two limits of step 3 as sections of C.
- b(β) ≤₁ a ⟺ C ⪯₁ X_{a,b(β)}. As β ↓ β*, the error sets decrease. The world-1 half of (MC_sel) gives
  C ⪯₁ X_{a,b(β*)}.
- For β < β*, the pattern a ◁ b(β) is (<,<), so C ≺₂ X_{a,b(β)}, i.e. C ⪯₂ X_{a,b(β)}. As β ↑ β*, the error sets
  increase. The world-2 half of (MC_sel) gives C ⪯₂ X_{a,b(β*)}.
- So C weakly dominates X_{a,b(β*)} at both worlds. A strict pattern at β* is then impossible (S1.5(i)).
- Step 1 is the world-1 half applied to X_{a_k,B} = m ∪ a_k ↓ m: it would give C ⪯₁ m, but m ⊊ E₁C. ∎

**Corollary S1.7 (PROVED).**

(a) If one world is additive with an integrable density > 0 a.e., or is (CP-a) with a credal set of countably
additive measures, then (Nest) holds.
- *Why (MC) holds:* in both cases X ⪯_i Y ⟺ ∫ w_i(1_{E_iY} − 1_{E_iX}) dP ≥ 0 for all P in the credal set, with
  w_i > 0 bounded. Dominated convergence gives (MC_i).

(b) Consequently, in two worlds with such a partner world, Lemma N0 and all of §8.5(c) apply without assuming
(Nest). In particular:
- **Prop Q15:** if world 2 is additive, world 1 has no simple certificate, no certificate with vanishing targets
  and no star certificate.
- **Strict escape, DL, DR, Lemma T, LF, IS, MP** hold.
- "Any two-world counterexample needs both worlds non-additive" (Prop Q15) now holds outright, not only under
  (Nest).

(c) A two-world system that is not nested has **both** worlds failing (MC). For (CP-a) worlds in the sense of the
write-up, which allows finitely additive states, this excludes the countably additive case only.

**Failed route (recorded).** Q2's route applies G-SE to the lattice join of a crossing pair. It yields a third
selected model C_r. In 𝓛 this is the observation u_X ≻ [C], [C′] for the join, which is consistent with rigid
crossings. The progress here comes from the splices X_{a,b}, not the join, and from S1.1.

---

## 4. What survives in two worlds

By S1.2–S1.6, a non-nested two-world system satisfying every axiom must contain one of the following:

- **Rigid crossing.** Two distinct classes [C] ≺ [C′] in 𝓛 whose members cross. Then B <₁ A and B <₂ A in the
  orientation of §1.
- **Tied crossing.** One class containing two crossing members. Then A ~ B at both worlds. This is the two-world
  analogue of "a non-null tie set split in crossing ways". By S1.5(ii) every segment lattice point that is doubly
  tied with C lies in C_L.

**Necessary shape (PROVED).** In either case:
- every non-segment splice is strictly comparable with C, with the same direction at both worlds;
- for each non-initial a ⊆ A, the cross relation with the τ-final chain b(β) switches at some β* with no tie;
- (MC_sel) fails at **both** worlds along that chain: world 1 from above, world 2 from below.

**Consequences.**
- By S1.3, if the classes in a rigid crossing are singletons, the system has no nested selection at all.
  - Neither "some nested selection exists" nor "every non-nested selection can be straightened" is then available.
  - The only true statement of that kind is S1.3.
- "Non-nestedness gives a cover nothing" is not proved. A rigid crossing is a genuine pair of selected models with
  their own relevant comparisons.

**Inhabitation.** Neither case has been constructed. No example was found, and I do not claim that either can occur.

**CONJECTURE S1.R.** In two worlds on M_U, (S) forces (MC_sel). Then Q2.N follows from S1.6.
- (MC_sel) is the model-space counterpart of (S)'s closedness in the index.
- It is close to lower closedness (LC_{T₁}) of Prop Q38, and to the Villegas-type continuity of Conjecture
  villegas.
- Whether (S) forces lower closedness is already recorded as open (Q3 §5).

**Where the proof stops.**
- In the nested theory, lemma DL turns a statement about a moving test model into one about moving *selected*
  models against a fixed test model, and then uses closedness in the index.
- In a crossing, the moving test models X_{a,b(β)} are not comparable with a selected chain in that way. The classes
  of 𝓛 between [C] and [C′] can sit anywhere in the lattice, constrained only by S1.2(e).
- A proof needs either a selected chain through the crossing rectangle, or a closedness statement for test chains.

---

## 5. Edges (three worlds)

### 5.1 What (Nest_e) is used for

**Remark S1.8 (PROVED by inspection of the recorded proofs: Q3_notes §4.2 and Q3_referee §4.1).**
- Prop Q35(4), and through it Thm Q36 (a), (b), (d) and Cor Q37, use only the following inputs:
  - a family (c_b)_{b∈[0,1]} of subsets of R_ij with c₀ = ∅ and c₁ = R_ij, which is a chain;
  - (K) at every interior b;
  - closed b-sections at worlds i and j for subsets of R_ij;
  - strict (G) and cancellation.
- "N0(ii) (C_L = the path) is not used anywhere" (Q3_notes). Lemma N0's "no missing value" and continuity steps use
  only chain + closed sections + strict (G).
- So any nested **edge family** with these properties, selected or not, coherent or not, can replace the selection.
  The right target on edges is therefore **straightening**: produce such a family from the given selection.

### 5.2 The edge-system axioms do not force nestedness

**Example S1.9 (PROVED; NUMERICS `plateau_edge.py`).** Let R ≅ [0,2) with Lebesgue measure.
- **Worlds.** Worlds i and j are additive with equal densities: ψ_i(c) = μ(c) and ψ_j(c) = μ(R∖c).
- **Path.** p ↦ c_p is any path that is continuous in measure, has μ(c_p) nondecreasing, and runs from ∅ to R. For
  instance it grows to [0,½), slides to [1,1½) at constant mass, then grows to R.
- **Axioms.**
  - Every set is competitive, so (K) holds.
  - Sections {p : μ(c_p) ≤ μ(A)} are closed, since p ↦ μ(c_p) is continuous.
  - Strict (G) and (IB) hold.
- **Not nested.** c_{1/3} = [0,½) and c_{2/3} = [1,1½) are disjoint.
- **Numerics.** 300 random test sets on a 4000-cell grid: no (K) failures and no non-interval sections.
- **Two caveats.**
  - This is an edge system, not a three-world system. In three worlds these edge models would be dominated through
    world 3.
  - On M_U in two worlds the same orders violate (C).
- **Moral.** (Nest_e) cannot be derived from the inputs of Prop Q35. Any derivation must use three-world
  undominatedness or (C).
- **Not a counterexample to straightening.** A nested family exists here.

### 5.3 What three-world undominatedness gives on an edge

**Lemma S1.10 (weak edge undominatedness; PROVED).** Let p be in the open edge e_ij and let X be any model with
X ⪯_i C_p and X ⪯_j C_p. Then X ~_i C_p or X ~_j C_p.

*Proof.* Competitiveness on {i,j} gives C_p ⪯_i X or C_p ⪯_j X. ∎

So an edge test model can two-world dominate C_p only with a tie at one of the two worlds. By three-world
undominatedness, such an X is then not ⪯₃ C_p. Nothing more follows.

- Define **(EU_ij)** to mean that this never happens: no edge test model is ⪯_i and ⪯_j a member of the edge family
  with one strict.
- (EU_ij) is **not derived**.
- It holds when worlds i and j are additive with densities > 0 on R_ij (PROVED). Competitive sets are then weakly
  Pareto points of a zonoid whose generating directions have nonzero coordinates, so they are Pareto.

### 5.4 Under (EU_ij)

**Proposition S1.11 (PROVED, conditional on (EU_ij)).** Let the edge family be the edge-selected models together
with the edge test models tied with them at i and j.
- (a) Lemma S1.1 holds on e_ij. Its proof uses only edge KKM covering (from (S) and competitiveness on {i,j}),
  closed sections and (EU_ij).
- (b) S1.2 holds: a linear continuum 𝓛_e and dominator intervals.
- (c) The analogue of S1.5 holds for crossing members U, V with crossing pieces A, B ⊆ R_ij. The admissible patterns
  for all (a,b) are (<,<), (>,>) and (~,~).
  - The mixed patterns are excluded by S1.4 and the S1.5 argument.
  - (~,~) is **not** excluded: on edges there is no (C) at worlds i, j, and no coherence requirement.

Without (EU_ij), the patterns left by competitiveness alone are the nine listed in `patterns.out`, edge version.
They include (<,~) and (~,<), i.e. one-world ties with a strict comparison at the other. The two-world machinery then
does not start.

### 5.5 Pairwise straightening

**Proposition S1.12 (PROVED, conditional on (EU_ij) and (MC) at world i on R_ij).** Let U ≺ V in 𝓛_e cross, with
E_iU = m ∪ B and E_iV = m ∪ A.
- (a) Some edge test model X is doubly tied (at i and j) with U and has E_iX ⊆ E_iV. In particular X is competitive
  and satisfies (EU_ij).
- (b) Suppose U = D_{M_{x_U,y_U}} and V = D_{M_{x_V,y_V}} (Prop comonotone), with x_U > x_V and y_U < y_V. Then X
  can be taken to be the coherent edge model D_{M_{x″,y_V}} for some x″ ∈ [x_V, x_U].

*Proof.*
1. **The chain.** Take a chain a(s) ↑ A, continuous in measure. For (b), take a(s) := F(x(s))∖F(x_U), with F(x) the
   first part of the error set in Prop comonotone (ii) and x(s) decreasing from x_U to x_V. F(x) moves continuously
   in measure, since its boundary hyperplanes are null.
2. **The endpoints.** U ≺_i V means B <_i A. Also ∅ <_i B.
3. **Completeness on cross pairs.** By S1.11(c) every cross pair is strictly comparable or doubly tied, so world i is
   complete on cross pairs.
4. **The switch.** Let s* := sup{s : a(s) <_i B}. Applying (MC_i) on both sides, exactly as in S1.6, gives
   a(s*) ~_i B.
5. **The double tie.** By S1.11(c) the pattern is (~,~). Put X := m ∪ a(s*). Then X ~ U at i and j, and
   X ⊆ m ∪ A.
6. **Coherence in (b).** m ∪ a(s*) = F(x″) ∪ G(y_V). This is the error set of D_{M_{x″,y_V}}, and it is valid
   because x″ ≤ x_U ≤ y_U < y_V. ∎

The mirror version, with (MC) at world j, gives X ~ V with E_iX ⊇ E_iU.

### 5.6 Global straightening

**CONJECTURE S1.13.** Under (EU_ij) and (MC) at world i or j on R_ij, there is a nested edge family with (K) and
closed sections. By Remark S1.8, Thm Q36 (a), (b), (d) and Cor Q37 would then hold at world i without (Nest_e).

**Where the maximal-chain argument stops.**
1. **Set-up.**
   - By Zorn, take a maximal inclusion-chain 𝒞 of sets that are doubly tied with edge-selected models. It contains ∅
     and R_ij.
   - Suppose a class W is missed, and let c⁻ := ess∪{c ∈ 𝒞 : [c] ≺ W} with sup class W⁻.
2. **What is proved.**
   - **World i.** c⁻ ~_i W⁻, by S1.2(e) one way and (MC_i) along the chain the other way.
   - **World j.** W⁻ ⪯_j c⁻. If D ≺ W⁻ also had D ⪯_j c⁻, then for c ∈ 𝒞 with D ≺ [c] we would get
     [c] ≺_j D ⪯_j c⁻ ⪯_j c, a contradiction.
3. **What is missing.** The reverse inequality c⁻ ⪯_j W⁻ is not available. It is a closedness of
   {D : X ⪯_j D}, which is not a section.
   - Without it, c⁻ may fail to be doubly tied with W⁻.
   - Pairwise straightening (S1.12) then has no admissible lower end to work from.

### 5.7 Status of the edge form of (R4)

- **"(S) forces comonotone endpoints on the edge models D_{M_{x,y}}" (Prop comonotone).** Not proved. It is not
  derivable from the edge-system inputs (S1.9), and it needs world 3.
- **Proved:**
  - S1.10;
  - under (EU_ij), the classification S1.11;
  - under (EU_ij) + (MC), pairwise straightening with coherent replacements of the same family (S1.12).
- **On edges, unlike in two worlds, doubly tied crossings are not excluded by any axiom.** The (C)-type exclusion of
  S1.5 needs a tie at **all three** worlds. Edge crossings of tied type are therefore the expected genuine
  non-nested possibility. They are harmless for the edge theory exactly when straightening holds.

---

## 6. Status and next steps

**Two worlds.**
- Q2.N reduces to excluding rigid and tied crossings. Both require (MC_sel) to fail at both worlds through a
  non-Archimedean switch.
- Q2.N is proved when one world is (MC): for instance additive, or (CP-a) with a countably additive credal set.
- The rest of (R4) in two worlds is CONJECTURE S1.R.

**Edges.**
- (Nest_e) itself is the wrong target: it is not implied by the edge inputs.
- Straightening suffices (S1.8). It is proved pairwise under (EU_ij) + (MC) and is CONJECTURE globally.
- The two missing lemmas are:
  - (EU_ij) from three-world undominatedness, which S1.10 gives only up to a one-world tie;
  - the closedness of {D : X ⪯_j D} along the maximal chain (§5.6).

**Nearby reachable results, in the spirit of the project.**
1. **Interaction with (R1) and (R3).**
   - Under (MC) at one world, the two-world exclusion side is fully nested.
   - So the open two-world class is: both worlds non-(MC), with either a nested selection, in which case (R1)–(R3)
     apply, or a rigid or tied crossing.
2. **The (MC_sel) lemma.** This is S1.R, and it is the single statement that would settle two-world (R4). A route
   would be a DL-type lemma for test chains, using S1.2(e) and the continuum 𝓛.

**Files** (`s1py/`):
- `patterns.py`, `patterns.out`: exhaustive check of S1.4, and the edge pattern list of §5.4.
- `plateau_edge.py`, `plateau_edge.out`: Example S1.9.
