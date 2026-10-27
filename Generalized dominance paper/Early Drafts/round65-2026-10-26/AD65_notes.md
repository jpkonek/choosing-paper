# AD65 — Disjoint additivity (Add) as a separate normative question (26 Oct 2026)

Labels: **PROVED** (complete argument here; not refereed) / **CHECKED** (exact, exhaustive computation on a finite atom system) / **CONJECTURE**. Scripts are in `ad65py/`; run each with `python3 -I <script>` from that folder. Each has an `.out` file, and every `.out` ends in ALL PASS.

Binding inputs: `BRIEF65.md` (role AD65), `AUDIT_r65_brief.md`, `AUDIT_r65_message.md`, `AUDIT_r64_decisions.md`. In line with them:
- (Add) is examined on its own merits. It is **not** adopted here, and nothing below is offered as a correction to the agreed question.
- Every result that assumes (Add) is in §5, the **strengthened-framework branch**, and is labelled as such.
- (S) is not reopened. Completeness and transitivity are not imposed.

---

## 0. Verdict in plain English

1. **What (Add) says.** If a world accepts each of two changes that touch disjoint sets of gambles, it accepts making both. Under (IB), (Add) is exactly the *cancellation-free part of transitivity* (Prop 3.2):
   - transitivity composes any two accepted changes, including a pair where the second undoes part of the first;
   - (Add) composes only pairs that do not interact;
   - (TP) composes only an accepted change with a guided one.

   Under (TC), the only thing (Add) forbids is that a world accepts both parts but stays **undecided** (incomparable) about the whole (Prop 3.4). For complete relations, (Add) follows from (TC).
2. **Logical relations (PROVED and CHECKED).**
   - Transitivity implies (Add), (TP) (given (G)), finite-chain consistency and (TC). Apart from transitivity, and completeness together with (TC) (which yields transitivity), nothing in the list implies (Add).
   - (Add) implies none of (IB), (TC), finite-chain consistency, (TP) or transitivity, even in combination with the others.
   - Eight exhaustively checked examples on 3–4 atoms (Table 3.6) separate all of these. Two of them:
     - Brier with **one** strict comparison deleted satisfies (IB), (TC), finite-chain consistency and (TP), but not (Add).
     - (Add), (TP), (TC) and (IB) together still allow a strict 4-cycle (Ex D′).
3. **The case for and against (§2).**
   - *For:* (Add) is the ordinal shadow of the claim that accuracy at a world is *separable*: the accuracy contributions of disjoint pieces of advice simply add up.
     - Every additive score has it, and so does every lexicographic score or unanimity of such scores (Prop 4.1).
     - So does *imprecision about which score is right*, handled by unanimity.
     - The usual objection to transitivity, that the intermediate model is a "pivot" whose contribution cancels out, does not apply, because (Add) involves no cancellation.
   - *Against:*
     - No exploitation or money-pump argument supports it. Those arguments support finite-chain consistency, which is strictly weaker (Ex A).
     - It is not implied by truth-directedness (G), by separability across contexts (IB), or by any consistency condition.
     - It rules out "holistic" evaluation, in which two harmless parts together commit the agent to something neither part does. The coherent hull itself works this way: the hull of a union can be strictly larger than the union of the hulls.
4. **What accuracy supports (§4).**
   - Accuracy considerations support (Add) **if and only if** one already holds that each world's verdict is an additive, gamble-by-gamble evaluation.
   - Dominance, guidance and consistency arguments are silent on it.
   - **Deliberate incomparability.** Under (Add), a world may be undecided about a change only if, for *every* way of splitting the change into parts, it is also undecided about (or against) at least one part. So incomparability under (Add) must be *content-based and scale-free*.
     - The "rigidity lemma" makes this precise (Lemma 4.2): a world that accepts all *small* changes in a cone must accept *all* changes in that cone.
     - Magnitude-based suspension ("trust small Brier verdicts, suspend large ones", Ex H) satisfies every binding axiom and finite-chain consistency, but violates (Add).
5. **Strengthened-framework branch (§5): (Add) does not do the excluding work it was proposed for.**
   - **Free protection survives (Add), and even transitivity (PROVED).** Pure guidance (each world accepts exactly the pointwise improvements) is a preorder at every world. It satisfies (G), (IB), (TC), finite-chain consistency, (Add) and (TP), and every coherent model has no weak dominator. Protection-for-free comes from *incompleteness*, not from dropping (Add) or transitivity.
   - **The (H)-reduction survives (Add) (PROVED, Theorem 5.2).** An (Add)-closed variant R_lex(𝒩) of ES64's deletion relation works for every family 𝒩 of coherent models. It satisfies reflexivity, a.e. ties, strict (G), (IB), (TC), finite-chain consistency and (Add). Its properties:
     - every member of 𝒩 has no weak dominator;
     - a model outside 𝒩 is dominated by a member iff ES64's (★) holds at it, and it is then dominated *strictly at every world*.

     With 𝒩 = all coherent models: **R_lex is a universal cover iff (H).** So (G) + (IB) + (TC) + (Add) admits exactly the same universal cover, conditional on exactly the same (H), as the binding framework.
   - **OR64's two "(TC)-only" diagnostic conclusions also survive (Add) (PROVED; CHECKED).**
     - The (Add)-closure M1⁺ of M1 still refutes E61's box lemma.
     - The (Add)-closure 𝒯⁺ of 𝒯 is even **transitive** at every world. It keeps all of 𝒯's conclusions: D_K is undominated, every collar trade is refused at every world, and the undominated models are D_K together with the one-world improvements 𝓘.

     REF64_es §5.4 is right that (Add) excludes the *particular* relations Δ(𝒩), M1 and 𝒯. It does not exclude what they were used to show.
6. **Recommendation.**
   - Whether to adopt (Add) can now be decided on its merits alone: adopting it changes none of the round-64 structural conclusions.
   - If the worry is that coherence-informed rankings give representation rather than independent justification, (Add) does not address it: R_lex satisfies (Add) and is just as coherence-informed.
   - A condition that did address it would have to be a *representation* condition (each world's verdicts given by an additive evaluation). That is a different and much stronger commitment, and per the audit it should not be adopted merely to exclude constructions.

---

## 1. Definitions

Setting as in ES64 §3 / BRIEF65:
- worlds i = 1,…,n;
- μ is finite, with a positive density and a finite first moment;
- U = D_{K′} ⊇ int ℝⁿ₊, with U ∩ (−ℝⁿ₊) = ∅;
- models are measurable X ⊆ U modulo null sets; coherent models are the D_Q a.e. with K′ ⊆ Q;
- m(X) := ∫_X h dμ; pos_i := {h_i > 0}, neg_i := {h_i < 0}.

**Records** (ES64 §1, OR64 §1).
- rec(X,Y) := (X∖Y, Y∖X). A record r = (A,B) is a pair of disjoint sets; it reads "accept A instead of B". Its inverse is r⁻¹ := (B,A).
- r is *guided at i* if A ⊆ pos_i and B ⊆ neg_i a.e.; G_i is the set of guided records.
- r *attacks* Z if B ⊆ Z and A ∩ Z = ∅ a.e. The *support* of r is A ∪ B.
- r₁ and r₂ are *composable* if P₁ ∩ P₂ = N₁ ∩ N₂ = ∅. Their composite is r₁∘r₂ = ((P₁∖N₂) ∪ (P₂∖N₁), (N₁∖P₂) ∪ (N₂∖P₁)), and rec(X,Z) = rec(X,Y)∘rec(Y,Z) (OR64 Prop 1.2).
- For records with disjoint supports, r₁ ⊔ r₂ := (A₁∪A₂, B₁∪B₂). This equals r₁∘r₂, with nothing cancelled.

**Conditions at one world i.** X ≺ Y means X ⪯ Y and not Y ⪯ X. "X ⪯ Y" means X is at least as good as Y.
- **(G)** strict guidance and **(IB)** independence: exactly as in W62 §2. By OR64 Prop 1.1, (IB) holds iff X ⪯_i Y ⟺ rec(X,Y) ∈ Acc_i for some set Acc_i of records.
- **(TC)** X ⪯ Y ⪯ Z ⇒ ¬(Z ≺ X).
- **(FCC)** finite-chain consistency: A₀ ⪯ A₁ ⪯ ⋯ ⪯ A_k ⇒ ¬(A_k ≺ A₀) (AUDIT_nontransitive, option 2).
- **(Tr)** transitivity: X ⪯ Y ⪯ Z ⇒ X ⪯ Z.
- **(TP)** (E61): Y ⪯ X, and X pointwise at least as good as M at i (rec(X,M) ∈ G_i, possibly null) ⇒ Y ⪯ M.
- **(Add)** (BRIEF65): X ⪯ Y, Y ⪯ Z and (X△Y) ∩ (Y△Z) = ∅ ⇒ X ⪯ Z.
- **(Canc)** (introduced here, under (IB)): if r, s, c are records with pairwise disjoint supports, and r⊔c ∈ Acc_i and s⊔c⁻¹ ∈ Acc_i, then r⊔s ∈ Acc_i.

**Lemma 1.1 ((Add) in record form; PROVED; this is REF64_es §5.4's remark).** Under (IB), (Add) holds at i iff Acc_i is closed under ⊔ (disjoint unions of records).

*Proof.*
- (⇒) Let r₁, r₂ ∈ Acc_i have disjoint supports. Put X := A₁∪A₂, Y := B₁∪A₂, Z := B₁∪B₂. Then rec(X,Y) = r₁, rec(Y,Z) = r₂ and X△Y = A₁∪B₁, Y△Z = A₂∪B₂, which are disjoint. (Add) gives rec(X,Z) = r₁⊔r₂ ∈ Acc_i.
- (⇐) If (X△Y) ∩ (Y△Z) = ∅, the two records have disjoint supports and rec(X,Z) = rec(X,Y) ⊔ rec(Y,Z). ∎

Without (IB), (Add) constrains only the given triple, and it is not a closure condition on records. Ex F below satisfies (Add) and violates (IB).

---

## 2. The case for and against (Add)

### 2.1 For
1. **Separability of accuracy.**
   - At world i, a change (A,B) alters which gambles are accepted, and its effect on accuracy at i is fixed by how right or wrong those gambles are at i.
   - When two changes touch disjoint gambles, nothing in either change alters the accuracy contribution of the other.
   - If each is no loss at i, it is hard to see on accuracy grounds alone how doing both could be something i cannot rank as no loss.
   - This is the ordinal content of the additivity of inaccuracy measures familiar from accuracy-first epistemology (inaccuracy of a state = sum of inaccuracies of its components). Every positive construction in the project has it (Prop 4.1).
2. **Path-independence without cancellation.**
   - For disjoint changes r₁, r₂, the combined change can be reached by accepted steps in *either* order: X → X⊕r₂ → Z and X → X⊕r₁ → Z. By (IB) each step is accepted in each order.
   - The composite *is* the two changes, with nothing added and later removed.
   - So the standard objection to transitivity in incomplete settings does not apply. That objection says the intermediate model may contain a "pivot" that makes both steps acceptable but is missing from the endpoint comparison. Prop 3.2 makes this exact: transitivity minus (Add) is precisely the cancelling compositions.
3. **Analogy with desirability itself.**
   - Coherent sets of desirable gambles are closed under combination: two acceptable transactions are jointly acceptable.
   - (Add) asks the same of acceptable *changes of advice* at a world, for changes on disjoint stakes.
   - Incomplete expected-utility representations (unanimity over a set of priors or utilities) have it automatically.
4. **It forces incomparability to be principled.** By Lemma 4.2, under (Add) a world may suspend judgement on a change only if the suspension survives every refinement of the change into pieces. This rules out incomparability that is merely an artefact of the *size* of a change.

### 2.2 Against
1. **No pragmatic argument.**
   - Exploitation and money-pump arguments need a strict step in a cycle of accepted moves. They support finite-chain consistency, which (by Suzumura's theorem, REF64_es §2.1) is equivalent to having an ordering extension that keeps strict comparisons.
   - An (Add)-failure in a finite-chain-consistent relation (Ex A; Δ(𝒩)) exposes no agent to a sure loss. Someone who makes the two disjoint changes in turn ends at a model they cannot rank against the start, but they never prefer the start strictly.
2. **Holism of advice.**
   - A set of desirability judgements commits the agent to more than its members: everything in its coherent hull.
   - The hull is not additive. hull(A₁ ∪ A₂) can be much larger than hull(A₁) ∪ hull(A₂), and two removals B₁ and B₂ can each leave a coherent model's commitments intact while together they do not.
   - An evaluator sensitive to what advice *commits one to* has a reason to treat the combination differently from its parts. (Add) forbids exactly this, while (IB) still allows it: (IB) concerns the common context, not the internal structure of the change.
   - Caveat: this rationale is coherence-informed. It is the kind of consideration AUDIT_r65 says gives a *representation* of coherence rather than an independent accuracy justification.
3. **It is not neutral about where incomparability may lie.** (Add) restores part of the composition requirement that the framework deliberately weakened when it moved from transitivity to (TC) (AUDIT_r65_message). It adds no consistency (Prop 3.1(e)); it only forces comparisons.
4. **It may not buy what it was proposed for.** §5 shows that (Add) excludes none of the round-64 phenomena it was meant to exclude. On the auditor's own criterion, an argument for (Add) must therefore rest on 2.1, not on its exclusions.

**Balance (assessment, not a theorem).**
- The strongest consideration for (Add) is 2.1(1)–(2): separable, cancellation-free composition.
- The strongest against it is 2.2(1): no pragmatic support beyond finite-chain consistency.
- The holistic objection 2.2(2) is real but coherence-informed.
- (Add) is a reasonable *optional strengthening* for anyone committed to separable accuracy. It is not a consequence of the agreed axioms or of accuracy as such.

---

## 3. Exact logical relations

**Prop 3.1 (implications; PROVED).** Each item holds at one world, for reflexive relations.
- (a) (Tr) ⇒ (Add). (Add) is the special case of (Tr) with disjoint changes.
- (b) (Tr) ⇒ (FCC) ⇒ (TC). By induction a chain gives A₀ ⪯ A_k, which contradicts A_k ≺ A₀. (TC) is the case k = 2.
- (c) (Tr) + weak (G) ⇒ (TP). Weak (G) gives X ⪯ M; then use (Tr). Conversely, **(TP) + reflexivity ⇒ weak (G)**: take Y = X.
- (d) Under (IB), (TP) is two-sided. Composition of records is commutative and composability is symmetric, so "X pointwise at least as good as Y, Y ⪯ M ⇒ X ⪯ M" is equivalent to (TP).
- (e) Completeness + (TC) ⇒ (Tr) (OR64 Prop 1.3) ⇒ (Add). So **(Add) has no content beyond (TC) for complete relations.** All of its content concerns incomparability.
- (f) (Add) implies neither reflexivity nor weak (G). The relation consisting only of the null record satisfies (Add).

**Prop 3.2 (transitivity = (Add) + cancellation; PROVED).** Assume (IB) on a decomposable domain. Then:
- (i) (Tr) ⟺ (Canc);
- (ii) (Add) ⟺ (Canc) restricted to c null;
- (iii) (TP) ⟺ (Canc) restricted to s⊔c⁻¹ ∈ G_i.

*Proof.*
- Let X ⪯ Y ⪯ Z, with r₁ = rec(X,Y) = (P₁,N₁) and r₂ = rec(Y,Z) = (P₂,N₂), which are composable.
- Put c := (P₁∩N₂, N₁∩P₂) (the part of r₁ that r₂ undoes), r := (P₁∖N₂, N₁∖P₂) and s := (P₂∖N₁, N₂∖P₁).
- Then r₁ = r⊔c, r₂ = s⊔c⁻¹, the supports of r, s and c are pairwise disjoint (by composability), and rec(X,Z) = r₁∘r₂ = r⊔s.
- Conversely, let r, s, c have pairwise disjoint supports.
  - Then r⊔c and s⊔c⁻¹ are composable: (P_r∪P_c) ∩ (P_s∪N_c) = ∅ and (N_r∪N_c) ∩ (N_s∪P_c) = ∅.
  - By OR64 Prop 1.2 (converse, using decomposability), they are rec(X,Y) and rec(Y,Z) for some models.
  - Their composite is r⊔s.
- This gives (i). Item (ii) is Lemma 1.1, and (iii) is the definition of (TP) in record form. ∎

So the three closure conditions are nested pieces of one principle: compose accepted changes.
- (Add) composes non-interacting changes.
- (TP) composes with a guided change, even when it cancels.
- (Tr) composes everything.

**Prop 3.3 ((TC) makes (Add) strict-additive; PROVED; (IB) not needed).** Assume (TC) and (Add), and let X ⪯ Y ⪯ Z with (X△Y) ∩ (Y△Z) = ∅. If either step is strict, then X ≺ Z.

*Proof.*
- (Add) gives X ⪯ Z. Suppose Z ⪯ X.
- If Y ≺ Z: the chain Z ⪯ X ⪯ Y and (TC) give ¬(Y ≺ Z), a contradiction.
- If X ≺ Y: the chain Y ⪯ Z ⪯ X and (TC) give ¬(X ≺ Y), a contradiction. ∎

Under (IB), applying (Add) to the inverse records shows that ties are additive too.

**Prop 3.4 (what (Add) adds to (TC); PROVED).** Assume (TC). If X ⪯ Y ⪯ Z with disjoint changes and X ⋠ Z, then X and Z are incomparable.

*Proof.* If Z ⪯ X, then Z ≺ X, contradicting (TC). ∎

So under (TC), (Add) forbids exactly one pattern: **both parts accepted, the whole left undecided.** Under (IB) this can be restated: (Add) holds iff, whenever a change is not accepted, every finite partition of it into disjoint parts has a part that is not accepted.

**Prop 3.5 ((IB) and (Add); PROVED with examples).** The two are logically independent.
- Ex A satisfies (IB) and not (Add).
- Ex F satisfies (Add), and is even complete and transitive, but not (IB).

They are different kinds of condition. (IB) is an *invariance* condition: verdicts on a change do not depend on its context. (Add) is a *closure* condition: accepted changes combine. Only together do they make (Add) a context-free closure of Acc_i under ⊔ (Lemma 1.1).

### 3.6 The separating examples (all CHECKED exhaustively at model level, `examples.out`)

All examples are at one world. Atoms are non-null cells: "+" means right to accept at this world and "−" means wrong. Where Brier values are given, they are the cell integrals m(·) at this world. Every example satisfies reflexivity and strict (G), and every example except F satisfies (IB) by construction (record relations), re-checked exhaustively.

| Ex | Construction | (TC) | (FCC) | (Add) | (TP) | (Tr) | (IB) | complete | Separates |
|---|---|---|---|---|---|---|---|---|---|
| **A** | atoms x₁(+3), y₁(−2), x₂(+4), y₂(−3); Acc = all Brier-acceptable records except R = ({x₁,y₁,x₂,y₂}, ∅) | Y | Y | **n** | Y | n | Y | n | (IB)+(TC)+(FCC)+(TP) ⇏ (Add) |
| **B** | atoms a(+3), b(−1), c(−1); Acc = G ∪ {({a,b,c}, ∅)} | Y | Y | Y | **n** | n | Y | n | (Add)+(FCC) ⇏ (TP) |
| **C** | atoms a(+), b(−), c(−); the (Add)+(TP) closure of G ∪ {({b},{c}), ({c},{a,b})} | **n** | n | Y | Y | n | Y | n | (Add)+(TP) ⇏ (TC) |
| **D** | atoms a(+), b(−), c(−); the (Add) closure of G ∪ {({a,b,c},∅), ({b},{a,c})} | Y | **n** | Y | n | n | Y | n | (Add)+(TC) ⇏ (FCC) |
| **D′** | atoms a(+), b(+), c(−), d(−); the (Add)+(TP) closure of G ∪ {({a,c},{b,d}), ({a,d},{b,c}), ({b},{a})} | Y | **n** | Y | Y | n | Y | n | (Add)+(TP)+(TC) ⇏ (FCC) |
| **E** | atoms a(+3), b(−1), c(−2); the (Add) closure of G ∪ {({b},{c}), ({a,c},∅)} | Y | Y | Y | Y | **n** | Y | n | all of (IB),(TC),(FCC),(Add),(TP) ⇏ (Tr) |
| **F** | atoms a(+1), b(+1), c(−1); X ⪯ Y iff Φ(X) ≥ Φ(Y), with Φ(X) = m(X) + ½·[a,c ∈ X] | Y | Y | Y | Y | Y | **n** | Y | (Add), even with (Tr) and completeness, ⇏ (IB) |
| **G** | atoms a(+), b(−), c(−); a complete record relation (found by exhaustive search over 729 orientations; 221 qualify) | **n** | n | Y | Y | n | Y | **Y** | completeness + (Add) + (TP) ⇏ (TC) |
| **H** | atoms as in A; Acc = G ∪ {Brier-acceptable records touching ≤ 2 atoms} ("trust region") | Y | Y | **n** | n | n | Y | n | world-local, accuracy-only suspension violates (Add) |

Witnesses, printed by the script:
- **A.** {x₁,y₁,x₂,y₂} ⪯ {x₁,y₁} ⪯ ∅, with disjoint changes, but not {x₁,y₁,x₂,y₂} ⪯ ∅.
  - *By hand:* Acc ⊆ Brier, and R is Brier-strict, so (FCC) holds by the deletion lemma (REF64_es §2.1).
  - (TP): Brier is transitive, so r∘g is Brier-acceptable. The only records r with r∘g = R for g guided are (R minus guided additions) = ({y₁,x₂,y₂},∅), ({x₁,y₁,y₂},∅) and ({y₁,y₂},∅). Their values are −1, −2 and −5, so Brier already refuses them.
- **B.** {a,b,c} ⪯ ∅ and ∅ is pointwise at least as good as {b}, yet {a,b,c} ⋠ {b}.
  - *By hand:* the extra record has full support, so ⊔ only meets null records, and G⊔G ⊆ G. Acc is a strict Brier sub-relation, so (FCC) holds.
- **C.** {b} ⪯ {c} ⪯ {a,b} and {a,b} ≺ {b}.
- **D.** ∅ ⪯ {b} ⪯ {a,c} ⪯ {a,b,c} and {a,b,c} ≺ ∅. This is a strict 4-cycle; every 3-step instance satisfies (TC).
- **D′.** {a,c} ⪯ {b,d} ⪯ {a,d} ⪯ {b,c} and {b,c} ≺ {a,c}. The generators were reduced to a minimal set by the script.
- **E.** {a,b} ⪯ {a,c} ⪯ ∅ with {a,b} and ∅ incomparable. The composite cancels c, illustrating Prop 3.2: (Add) and (TP) hold, (Canc) fails.
- **F.** {a} and {b} are tied, but {a,c} ≺ {b,c}: the same record in two contexts.
- **G.** ∅ ⪯ {a,b} ⪯ {a,c} and {a,c} ≺ ∅.
- **H.** ∅ ⪯ {y₁} ⪯ {x₁,y₁,y₂} with disjoint changes, but the union (size 3) is refused.

Search provenance (`search.out`, `search2.out`):
- Examples B–E were found by exhaustive enumeration of closures of G ∪ S with |S| ≤ 3 on 3 atoms.
- D′ was found by random search on 4–5 atoms. A pattern "(Add)+(TP)+(TC) without (FCC)" does not occur on 3 atoms, or on 4 atoms with |S| ≤ 2.
- These searches only *find* examples. Each example's properties are then established by the exhaustive model-level check.

**Summary of 3.1–3.6.**
- Among (IB), (TC), (FCC), (TP) and (Add), the only implications are those of Prop 3.1: (Tr) ⇒ everything else, given (G); (FCC) ⇒ (TC); and completeness + (TC) ⇒ (Tr).
- (Add) is independent of each of the others and of all of them jointly (A, F).
- Adding (Add) to any subset yields no new consistency (C, D, D′, G) and no transitivity (E).

---

## 4. What accuracy-based considerations do and do not support

**Prop 4.1 (separable accuracy gives (Add); PROVED).** Let (Γ, +, ≤) be an ordered abelian group; examples are ℝ, and ℝᵏ ordered lexicographically. Let S_i be any family of maps s: records → Γ that are additive on disjoint unions. Put Acc_i := G_i ∪ {r : s(r) ≥ 0 for every s ∈ S_i}. Then Acc_i satisfies (Add). The same holds without the G_i term, and for S_i = ∅.

*Proof.*
- s(r₁⊔r₂) = s(r₁) + s(r₂) ≥ 0 when both terms are ≥ 0, and G_i⊔G_i ⊆ G_i.
- Mixed case: if r₁ ∈ G_i and r₂ is unanimous, the union is unanimous provided G_i is unanimous, i.e. s ≥ 0 on G_i. This holds for every truth-directed score.
- If s ≥ 0 on G_i fails for some s ∈ S_i, drop the G_i term; then (G) must be checked separately. ∎

This covers:
- Brier and every integral score;
- lexicographic integrals, including veto–Brier;
- view-unanimity orders;
- **imprecise accuracy**: unanimity over a set of admissible truth-directed additive scores.

So *uncertainty about which accuracy measure is correct, handled cautiously, respects (Add).* It cannot be the source of deliberate incomparability of the kind (Add) forbids.

**Lemma 4.2 (rigidity; PROVED).** Assume (IB) and (Add) at world i. Let C ⊆ ℝⁿ be a cone (λC ⊆ C for λ > 0). Put size(A,B) := μ(A∪B) + ∫_{A∪B}|h| dμ. Suppose some ε > 0 is such that every record r with m(r) := m(A) − m(B) ∈ C and size(r) < ε is accepted at i. Then every record with m(r) ∈ C is accepted at i.

*Proof.*
- Fix r = (A,B) with m(r) ∈ C. The vector measure ν(S) := (∫_{S∩A} h, ∫_{S∩B} h, μ(S∩(A∪B)), ∫_{S∩(A∪B)}|h|) on subsets S of A∪B is finite and non-atomic, since μ has a density and a finite first moment.
- By Lyapunov's convexity theorem, and induction, A∪B splits into S₁,…,S_k with ν(S_j) = ν(A∪B)/k.
- Then r_j := (A∩S_j, B∩S_j) has m(r_j) = m(r)/k ∈ C and size(r_j) = size(r)/k < ε for k large, so each r_j is accepted.
- By (Add), applied k−1 times, r = ⊔ r_j is accepted. ∎

**Consequences for deliberate incomparability.** Here, "a world undecided about a combined change but decided about each part".
- If "decided" means *accepted*: under (TC) this is exactly an (Add)-failure (Prop 3.4).
- If any part is decided *against*: (Add) says nothing.
- **Scale-based** incomparability ("my Brier verdicts are trustworthy for small changes only") is world-local and accuracy-based. Ex H satisfies all the binding axioms and (FCC). Lemma 4.2 shows (Add) forbids every such scheme. Under (Add), a world that endorses small Brier-improving changes endorses all of them.
- **Content-based** incomparability is compatible with (Add), provided it is hereditary: every way of splitting a suspended change leaves a suspended (or rejected) piece. R_lex (§5) is an example.
  - Where such incomparability comes from interactions among gambles (hull, commitments), it is not grounded in world-i accuracy. At world i, each gamble's contribution to accuracy is fixed by its own payoff there.
  - Where it comes from other worlds, as in Δ(𝒩), it is cross-world. The positive constructions also use cross-world information (veto–Brier's v·h, REF64_es §5.3(2)), but only *additively*, through a fixed weight.

**What accuracy does and does not support (summary).**

| Consideration | Supports (Add)? |
|---|---|
| Truth-directedness (G): guided changes accepted, their inverses refused | No. It constrains only guided records, and G⊔G ⊆ G is automatic. |
| Separability across contexts (IB) | No (Ex A). It concerns context, not composition. |
| Pareto/dominance reasoning across worlds | No. It concerns the joint verdict, not the shape of each world's relation. |
| Consistency (TC), (FCC); exploitation arguments | No (Ex A). They support (FCC) only. |
| Additive (separable) accuracy at each world, including lexicographic and imprecise-score unanimity | **Yes** (Prop 4.1). |
| Scale-sensitive trust in accuracy verdicts | Against: these violate (Add) (Ex H, Lemma 4.2). The rationale is weak if the score is additive: distrusting the sum means distrusting the parts' common measure. |
| Holistic evaluation via commitments (coherent hull) | Against (2.2(2)). But this is coherence-informed, not accuracy-based. |

**Remark 4.3 (a necessary feature of every cover, independent of (Add); PROVED).** Call a relation *Brier-compatible* if X ⪯_i Y ⇒ m_i(X) ≥ m_i(Y).

*Claim.* If a Brier-compatible relation accepts, at every world, every record r with m(r) ∈ int ℝⁿ₊ and size(r) < ε, then every non-Bayes model is dominated. So no non-Bayes K is covered.

*Proof.*
- Let X be non-Bayes. By ES64 Lemma 5.1 (refereed CORRECT, E22) there is a Bayes act N_π with m(N_π) − m(X) ∈ int ℝⁿ₊.
- Split r := rec(N_π, X) as in Lemma 4.2. Each piece r_j applies to X, has m(r_j) ∈ int ℝⁿ₊, and is small.
- So X ⊕ r_j ⪯_i X at every i, and Brier-compatibility makes the comparison strict.
- This uses no (Add). (Add) is needed only to turn small acceptances into large ones. ∎

So in **every** Brier-compatible cover of a non-Bayes K, for every ε > 0 some world refuses some record r with m(r) ∈ int ℝⁿ₊ and size(r) < ε. Δ(𝒩) and R_lex do this; veto–Brier, which is not Brier-compatible, refuses such records through its veto. "Local accuracy dominance" is therefore not available to anyone who wants Brier-compatible coverage of non-Bayes sets, with or without (Add).

---

## 5. Strengthened-framework branch: (G) + (IB) + (TC) + (Add)

*Everything in this section assumes (Add) as an extra hypothesis. It reports a strengthened framework, not a correction to the agreed question.*

**Prop 5.1 (protection is free even under transitivity; PROVED; CHECKED on atoms, `rlex.out` last line).** Put Acc_i := G_i (pure guidance). Then at every world:
- the relation is reflexive, ties a.e.-equal models, and satisfies strict (G) and (IB);
- it is **transitive**, hence satisfies (TC), (FCC), (Add) and (TP);
- every coherent model has no weak dominator other than itself.

*Proof.*
- Transitivity: if X∖Y, Y∖Z ⊆ pos_i and Y∖X, Z∖Y ⊆ neg_i, then X∖Z ⊆ (X∖Y) ∪ (Y∖Z) ⊆ pos_i, and likewise Z∖X ⊆ neg_i.
- Strict (G): the inverse of a non-null guided record is not guided.
- Protection: if rec(Y,N) ∈ G_i for every i, then Y∖N ⊆ int ℝⁿ₊ and N∖Y ⊆ U ∩ (−int ℝⁿ₊) = ∅. Since every D_Q ⊇ int ℝⁿ₊, Y∖N is null. ∎

Pure guidance covers no target (ES64 Lemma 2.3). The point is narrower: **"protection for free" (REF64_es §5.1) is a consequence of dropping completeness.** It survives (Add), (TP) and transitivity. A non-trivial protection result must be joined to the dominance half, and that is what Theorem 5.2 does.

**Definition 5.2 (R_lex(𝒩)).** Fix a nonempty family 𝒩 of coherent models.
- NA := the records that attack no member of 𝒩. The null record is not in NA.
- For a record r, put L_i(r) := (m_i(r), Σ_j m_j(r)) ∈ ℝ², ordered lexicographically.
- Acc_i := G_i ∪ {r ∈ NA : L_i(r) >_lex 0} ∪ {r ∈ NA : r⁻¹ ∈ NA, L_i(r) = 0}.
- X ⪯_i Y :⟺ rec(X,Y) ∈ Acc_i.

In words, world i compares by Brier at i, breaking Brier ties by total Brier (Brier at the uniform prior). But it accepts a change that would carry some member of 𝒩 to a different model **only if the change is guided at i**.

ES64's Δ(𝒩) refuses such a change at *one* world. R_lex refuses it at *every* world where it is not guided, and refuses all its sub-changes too, because a sub-change of an attacking change attacks the same model. That is what makes the refusals hereditary, and hence compatible with (Add).

**Theorem 5.2 (PROVED; CHECKED on 8 atoms for 7 families, `rlex.out`).**
- (a) R_lex(𝒩) is reflexive, ties a.e.-equal models, and satisfies strict (G), (IB), (TC), (FCC) and **(Add)**.
- (b) No member of 𝒩 has a weak dominator other than itself.
- (c) For X ∉ 𝒩: X is dominated by a member of 𝒩 ⟺ (★) holds at X. That is, some N ∈ 𝒩 has m(N) ≥ m(X), m(N) ≠ m(X), and rec(N,X) attacking no member of 𝒩. In that case N dominates X strictly at every world.
- (d) Hence, if (★) holds at every X ∉ 𝒩, the undominated models are exactly 𝒩, (W) holds, and direct (C) holds in the strong form "tied at every world with a member ⇒ equal to it". If moreover D_K ∈ 𝒩, R_lex(𝒩) covers K in the sense of BRIEF64 / REF64_es §2.4, with (LF) a property of U.

*Proof.*
1. **Fact.** If r₁ ⊔ r₂ attacks Z, then r₁ and r₂ each attack Z, since B₁ ⊆ B₁∪B₂ ⊆ Z and A₁ ⊆ A₁∪A₂, which misses Z. Hence r₁ ∈ NA ⇒ r₁ ⊔ s ∈ NA for every s with disjoint support.
2. **Brier-lex compatibility and tie symmetry.** Put Φ_i(X) := (m_i(X), Σ_j m_j(X)). Then L_i(rec(X,Y)) = Φ_i(X) − Φ_i(Y).
   - Every accepted record has L_i ≥_lex 0. A non-null guided record has m_i(r) = ∫_A h_i + ∫_B |h_i| > 0.
   - If r ∈ Acc_i and L_i(r) = 0, then r is null or r ∈ T_i := {r ∈ NA : r⁻¹ ∈ NA, L_i(r) = 0}. In either case r⁻¹ ∈ Acc_i.
   - So X ≺_i Y ⇒ Φ_i(X) >_lex Φ_i(Y). A chain A₀ ⪯ ⋯ ⪯ A_k then gives Φ_i(A₀) ≥ Φ_i(A_k), and A_k ≺ A₀ would need the reverse strictly. This proves (FCC), hence (TC). It is the deletion lemma with a lexicographic score.
3. **(a), the rest.**
   - Reflexivity: the null record is guided. A.e. ties: records are taken modulo null sets. (IB): Acc_i is a set of records.
   - Strict (G): guided records are accepted; the inverse of a non-null guided record has L_i <_lex 0.
   - **(Add)** (Lemma 1.1): let r₁, r₂ ∈ Acc_i have disjoint supports.
     - If both are guided, so is r₁⊔r₂.
     - Otherwise, say r₁ ∈ NA. Then r₁⊔r₂ ∈ NA by the Fact, and L_i(r₁⊔r₂) = L_i(r₁) + L_i(r₂) ≥_lex 0.
     - If the sum is >_lex 0, the union is accepted.
     - If the sum is 0, both terms are 0. Each r_k is then null or in T_i, so (r₁⊔r₂)⁻¹ = r₁⁻¹ ⊔ r₂⁻¹ ∈ NA (by the Fact again, unless a part is null), and the union is in T_i.
4. **(b).**
   - Let Y ⪯_i N for every i, with N ∈ 𝒩. rec(Y,N) applies to N, so it attacks N and is not in NA. Hence it lies in G_i for every i.
   - Then Y∖N ⊆ int ℝⁿ₊ and N∖Y ⊆ U ∩ (−int ℝⁿ₊) = ∅.
   - Every coherent model contains int ℝⁿ₊ ∩ U, so Y = N a.e.
5. **(c) ⇐.**
   - r := rec(N,X) ∈ NA. Σ_j m_j(r) > 0 because m(N) ≥ m(X), ≠. So L_i(r) >_lex 0 at every i, and r ∈ Acc_i.
   - L_i(r⁻¹) <_lex 0, so r⁻¹ ∉ Acc_i for every i. Hence N ≺_i X at every world.
6. **(c) ⇒.** Let N ∈ 𝒩 dominate X, and r := rec(N,X).
   - *If r ∈ NA:* L_i(r) ≥_lex 0 for all i gives m(N) ≥ m(X).
     - If m(N) = m(X), every L_i(r) = 0, so r ∈ T_i at every world.
     - Then r⁻¹ ∈ Acc_i at every world, and N does not dominate X.
     - So m(N) ≠ m(X), and (★) holds.
   - *If r ∉ NA:* r is guided at every world, so r = (N∖X, ∅) with N∖X ⊆ int ℝⁿ₊ non-null. Every member of 𝒩 contains N∖X, so r attacks none of them, contradicting r ∉ NA.
7. **(d).** As in ES64 Theorem 3.2(iii)–(iv) and REF64_es §2.4, using (b) and (c). ∎

**Corollary 5.3 (the (H)-reduction survives (Add); PROVED).** Take 𝒩 = all coherent models. A coherent model contains X∖N iff it contains hull(X∖N) (REF64_es §2.5), so rec(N,X) ∈ NA ⟺ μ((N∖X) ∩ hull(X∖N)) > 0. Hence:

> **R_lex(all coherent) is a universal cover ⟺ (H).**

This is exactly the status of Δ(all coherent) in the binding framework (REF64_es E17). So **(G) + (IB) + (TC) + (Add)** — and even with (FCC) — admits a universal cover iff (H). Target-specific fallbacks carry over unchanged: R_lex(𝒩) with D_K ∈ 𝒩 covers K iff (★) holds for 𝒩.

*Remark (plain-Brier variant).* If one wants each world's relation to be a sub-relation of Brier at that world, symmetric on Brier ties, drop the lexicographic tie-break. That is, use L_i(r) := m_i(r) in Definition 5.2. Then (a) and (b) hold by the same proof, and (c) holds with (★) strengthened to m(N) > m(X) in *every* coordinate. A tie world could only be passed by the inverse being in NA, and rec(X,N) attacks N.

**Prop 5.4 (M1 survives (Add); PROVED; CHECKED on OR64's 8 atoms, `diag.out` §1).** Take OR64 Prop 2.1's sets E, A, B, R and r₀ = (E∪A, B), and put:
- Acc_i = Acc_j := G ∪ {r₀ ⊔ g : g guided at that world, with support disjoint from r₀};
- Acc_k := G_k.

Then M1⁺:
- satisfies reflexivity, a.e. ties, strict (G), (IB), (TC) and **(Add)**; (FCC) is CHECKED on atoms;
- R is still an E61 priority region at j;
- Y₀ := (X_i∖B) ∪ E ∪ A still dominates X_i.

So E61's box lemma fails under (G)+(IB)+(TC)+(Add). As OR64 found, the missing ingredient is (TP), which M1⁺ violates.

*Proof.*
- **(Add).** G⊔G ⊆ G, and (r₀⊔g)⊔g′ = r₀⊔(g⊔g′). Two records of the form r₀⊔g are never disjoint.
- **Strict (G).** At j, r₀⊔g adds A ⊆ pos_j. At i, it adds E ⊆ pos_i. So it is never the inverse of a guided record, which adds only wrong gambles.
- **(TC).** It suffices to show that, for accepted composable r₁ and r₂ with c := r₁∘r₂, c⁻¹ ∈ Acc and c ∉ Acc never happen together.
  - G∘G ⊆ G. Two records of the form r₀⊔g are not composable, since both add E∪A.
  - Take r₁ = r₀⊔g₁ and r₂ = g₂ guided. At j, c adds A, because A ⊆ pos_j and g₂ removes only neg_j gambles. So c⁻¹ removes A and is not guided.
  - Nor is c⁻¹ of the form r₀⊔g. That would need c to add B, but B lies in r₁'s removed part and g₂ cannot re-add it (composability).
  - At i the same argument works with E in place of A.
- **Priority region and domination.** As in OR64 Prop 2.1(b)–(c). A record r₀⊔g removes B ⊆ pos_j, so it never compares a model with M_R ⊆ neg_j in the required way. rec(Y₀, X_i) = r₀. ∎

**Prop 5.5 (𝒯 survives (Add), and even transitivity; PROVED; CHECKED on OR64's 9 atoms, `diag.out` §2).** Put IN := D_K and OUT := U∖D_K. Let 𝒯⁺_w be the (Add)-closure of OR64's 𝒯_w. Equivalently,

  (A,B) ∈ 𝒯⁺_w ⟺ (i) A ∩ OUT ⊆ pos_w and B ∩ IN ⊆ neg_w, and (ii) (A∩IN, B∩OUT) is null or not anti-guided at w.

In words: moves *away from* the target must be right at w, and moves *toward* the target must not be all wrong. Then at every world:
- (a) the relation is reflexive and **transitive**, and satisfies strict (G) and (IB). Hence it satisfies (TC), (FCC), (Add) and (TP).
- (b)–(e) of OR64 Prop 3.5 hold verbatim. D_K is undominated and tied with no other model. D_K strictly dominates every model that is not pointwise at least as good as D_K at some world. The undominated models are exactly D_K ∪ 𝓘. Every collar trade is refused at every world.

*Proof.*
1. **The equivalence.** Split a record into its away part (A∩OUT, B∩IN) and its toward part (A∩IN, B∩OUT).
   - A decomposition t⊔g, with t ∈ T_w ∪ {0} and g ∈ G_w, must put A∩OUT and B∩IN into g, since t ⊆ (IN, OUT). This forces (i).
   - Then t ⊇ the wrong toward-moves (A∩IN∩neg_w, B∩OUT∩pos_w), and t is not anti-guided only if (ii) holds.
   - Conversely, under (i) and (ii), take t := the toward part and g := the away part.
2. **Transitivity.** Let r₁, r₂ ∈ 𝒯⁺_w be composable, with composite c.
   - The added part of c is contained in P₁∪P₂, and its removed part in N₁∪N₂, so (i) holds for c.
   - For (ii), suppose c has a wrong toward-move, say from r₁. Then r₁ has a right toward-move y: y ∈ P₁∩IN∩pos_w or y ∈ N₁∩OUT∩neg_w.
   - y is cancelled in c only if y ∈ N₂ or y ∈ P₂, respectively. But N₂∩IN∩pos_w = ∅ and P₂∩OUT∩neg_w = ∅, by (i) for r₂.
   - So c has a right toward-move.
3. **Strict (G).** The inverse of a non-null guided record satisfies (i) only if it is a pure toward-move, all of whose moves are wrong. That violates (ii).
4. **(b)–(e).**
   - A record applying to D_K is a pure away-move. It is accepted at w iff it is guided at w, by (i).
   - A pure toward-move is accepted iff it is not anti-guided, by (ii).
   - These are exactly the facts used in OR64's proof of Prop 3.5(b), (c) and (e).
   - For (d), let X = (D_K∖N_X) ∪ A_X ∈ 𝓘_w, and let rec(Y,X) be accepted at w. Its toward part adds only N_X-gambles, which are wrong at w, and removes only A_X-gambles, which are right at w. So it has no right toward-move, and by (ii) it is null.
   - The record is then a pure away-move, so it is guided at w. Acceptance at the other worlds makes it guided there too. A record guided at every world is null, by one-sidedness and int ℝⁿ₊ ⊆ D_K. ∎

**Consequence.** OR64's localisation, "any axiom-level proof must obtain its contradiction from the coherent dominators required by the one-world improvements 𝓘", holds under (G)+(IB)+(TC)+(Add), and even under (G)+(IB)+**transitivity**. REF64_es §5.4 is correct that (Add) excludes M1 and 𝒯 *as relations*; it does not exclude the diagnostic conclusions.

**What is open in this branch.**
- **(TP).** Does (G)+(IB)+(TC)+(TP) admit a relation that protects every coherent model and reduces universal coverage to (H)?
  - Closing R_lex under (TP) and (Add) keeps (TC), (FCC), (TP), (Add) and strict dominance under (★). The reason is that composition with a guided record only increases Φ_i, and new ties arise only with a null guided record.
  - The only question is protection, which is CONJECTURE for 𝒩 = all coherent models.
  - *Atom evidence* (`rlex_tp.out`): after closure, protection survives for the coherent-like family (all D_Q restricted to atoms, Q from a grid) and for the Pareto family, but fails for 4 of the 5 arbitrary declared families. So any proof must use the structure of the coherent family.
  - This is a finite analogue only, not evidence about measurable models in general.
- **Transitivity plus coverage.** Prop 5.1 shows that transitivity is compatible with free protection; Prop 5.5 shows that it is compatible with 𝒯's localisation. Whether some transitive incomplete relation is a universal cover under (H) is open. Per AUDIT_r65, transitivity is not to be imposed.

---

## 6. Consequences for the author's decision

1. REF64_es §5.4 called (Add) "the weakest candidate that excludes every round-64 escape (Δ(𝒩), M1, 𝒯) while keeping all positive theorems". It does exclude those three relations. It excludes **none** of the three phenomena:
   - protection with the (H)-reduction (Theorem 5.2);
   - box-lemma failure (Prop 5.4);
   - 𝓘-localisation (Prop 5.5, even transitive).

   So the round-64 open question "(G)+(IB)+(TC)+(Add): protection-for-free or a cover?" is answered:
   - protection-for-free: **yes**;
   - universal cover: **iff (H)**;
   - cover of the reversed triangle: **iff (★) for some 𝒩 ∋ D_K**.

   All three statements are the same as without (Add).
2. Adopting (Add) is therefore a free choice about *separable accuracy* (§2, §4). It neither helps nor harms the main mathematical task (H).
3. If the concern is that coherence-informed acceptance gives representation, not justification, the relevant condition would have to say *how* each world's verdict is computed: for instance, an additive representation Acc_i = {r : Ψ_i(r) ∈ C_i} with Ψ_i additive. That is a representation hypothesis, much stronger than (Add) and of a different kind. In line with AUDIT_r65, I do not propose adopting it to exclude constructions; I record only that (Add) does not address the concern.

---

## 7. Status table

| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma 1.1: under (IB), (Add) ⟺ Acc_i closed under disjoint union | PROVED | §1 |
| 2 | Prop 3.1: (Tr) ⇒ (Add), (FCC) ⇒ (TC); (Tr) + weak (G) ⇒ (TP); (TP) + refl ⇒ weak (G); (TP) two-sided under (IB); complete + (TC) ⇒ (Add) | PROVED | §3 |
| 3 | **Prop 3.2: under (IB), (Tr) ⟺ (Canc); (Add) = cancellation-free (Canc); (TP) = (Canc) with a guided second step** | PROVED | §3 |
| 4 | Prop 3.3: (TC) + (Add) ⇒ strict steps make strict composites | PROVED | §3 |
| 5 | Prop 3.4: under (TC), an (Add)-failure is exactly "parts accepted, whole incomparable" | PROVED | §3 |
| 6 | Prop 3.5: (IB) and (Add) independent | PROVED; CHECKED (A, F) | §3 |
| 7 | Examples A–H (Table 3.6): every listed property and non-property | CHECKED (exhaustive, `examples.out`, ALL PASS); A and B also by hand | §3.6 |
| 8 | Ex D′: (Add) + (TP) + (TC) + (IB) + (G) without (FCC) | CHECKED | §3.6 |
| 9 | Prop 4.1: unanimity of additive (or lexicographic) scores satisfies (Add) | PROVED | §4 |
| 10 | Lemma 4.2 (rigidity): under (IB) + (Add), small acceptance in a cone ⇒ full acceptance | PROVED | §4 |
| 11 | Remark 4.3: Brier-compatible + accepts all small uniform improvements at every world ⇒ every non-Bayes model dominated (no (Add) needed) | PROVED (uses ES64 Lemma 5.1, refereed) | §4 |
| 12 | Normative balance of (Add) | Assessment (not a theorem) | §2 |
| 13 | **Prop 5.1: pure guidance is transitive and protects every coherent model** | PROVED; CHECKED | §5 |
| 14 | **Theorem 5.2: R_lex(𝒩) satisfies (G), (IB), (TC), (FCC), (Add); protects 𝒩; dominance ⟺ (★), strict at every world** | PROVED; CHECKED (8 atoms, 7 families, `rlex.out`) | §5 |
| 15 | **Cor 5.3: under (G)+(IB)+(TC)+(Add), R_lex(all coherent) is a universal cover ⟺ (H)** | PROVED | §5 |
| 16 | Plain-Brier variant: same with (★) strict in every coordinate | PROVED | §5 |
| 17 | Prop 5.4: M1⁺ ((Add)-closed) still breaks E61's box lemma | PROVED; CHECKED (`diag.out`) | §5 |
| 18 | **Prop 5.5: 𝒯⁺ is transitive and keeps all of 𝒯's conclusions** | PROVED; CHECKED (`diag.out`) | §5 |
| 19 | (TP)-closure of R_lex still protects all coherent models | CONJECTURE (atoms: yes for coherent-like and Pareto families, no for 4 of 5 arbitrary families) | §5 |
| 20 | Some transitive incomplete relation is a universal cover given (H) | OPEN | §5 |

## 8. Files

| File | Content |
|---|---|
| `ad65py/props.py` | exact single-world property checkers (refl, strict/weak (G), (IB), (TC), (FCC), (Add), (TP), (Tr), completeness) and record closures |
| `ad65py/examples.py` → `examples.out` | Examples A–H, exhaustive at model level, with witnesses; ALL PASS |
| `ad65py/search.py` → `search.out`, `search2.py` → `search2.out` | how Examples B–E and D′ were found (search only; properties re-established in `examples.out`) |
| `ad65py/rlex.py` → `rlex.out` | R_lex(𝒩) on 8 atoms, 7 families: axioms, (FCC), (Add) (exhaustive over all disjoint record pairs), protection, (★) ⟺ dominance model by model; pure guidance; ALL PASS |
| `ad65py/diag.py` → `diag.out` | M1⁺ and 𝒯⁺ on OR64's atom systems; ALL PASS |
| `ad65py/rlex_tp.py` → `rlex_tp.out` | exploratory: (TP)+(Add) closure of R_lex on atoms |
