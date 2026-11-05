# FS81 report: Strand 1. The finite-sequence theorem, the geometric lemma, and removing (A2)

Sources used: `AUDIT_A_finite_sequence.md`, `AUDIT_B_brief.md`, `appshort.tex` (§§2–4), `app_long.tex` (§§4–6), `ldgshort_app.tex` (§§2–4), `ldg_full_current.tex` (passages that cite the companion paper's axioms). No manuscript was modified.

Conventions. In LDG, `m ⪯_ω m'` means "m is at least as good as m' at ω". In the application, `X ⪰_ω Y` means "X is at least as good as Y at ω". Each section says which convention it uses. Throughout, "tied at every world" means each model weakly dominates the other, and "dominates" means "weakly dominates and is not tied at every world".

---

## 0. Results

| # | Claim | Label |
|---|---|---|
| 1a | The auditor's proof of the finite-sequence theorem is correct under worldwise (A3). | CHECKED |
| 1b | The exact hypothesis the theorem needs is **(TD) dominance transmission through all-world ties**: if m and m′ are tied at every world and c dominates m′, then c dominates m. For a fixed ranking, (TD) is equivalent to the theorem for all r, and also to the theorem for r = 1 alone. | PROVED |
| 1c | Hierarchy: worldwise (A3) ⇒ all-world-tie substitution (T∀) ⇒ weak-dominance substitution (W) ⇒ (TD). Every implication is strict. So **yes, substitution through all-world ties is enough**, and something weaker still is enough. Worldwise (A3) is not needed. | PROVED |
| 1d | Some hypothesis is needed. A one-world, three-model ranking (which can even be complete) breaks the theorem with r = 1. | PROVED |
| 2a | In appshort §3, undominatedness is used only to obtain (i) and (ii) of Lemma 3.4 and in the preservation step of Lemma 3.3. The constructions themselves (Lemma 3.4(i), the triple in Lemma 3.4(ii), Lemma 3.5, Lemma 3.6) use only (U1) and (U2), (M2) and (M3). | CHECKED |
| 2b | **Geometric lemma.** Under (M2) and (M3), every incoherent X has a sequence X = X₀ → … → X_r → Z with r ≤ 2. Each step X_j → X_{j+1} is a legitimate consolidation; the inclusions even hold exactly, not just a.e. The last step is a non-null change guided at every world. The proof is a three-way case split on (U1) and (U2), and the case structure is explicit. | PROVED |
| 3a | **New Theorem 4.1.** Assume (M2) and (M3). Every ranking satisfying (A1), (A4) and (TD) dominates every incoherent model, so in particular every ranking satisfying (A1), (A3) and (A4) does. The dominator is one of X₁, …, X_r, Z. | PROVED |
| 3b | (A2) is used nowhere in the new proof. It was redundant in the old proof too: there, (A2) is used only in the strictness step of Lemma 3.3, and (A3) alone gives that step by a global argument (§3.2). | PROVED |
| 3c | (A1) and (A4) alone do **not** suffice. For Ω = {1,2} with a Gaussian μ (so (M1)–(M3) hold), there is a ranking satisfying (A1) and (A4) under which an explicit incoherent model is undominated. | PROVED |
| 4 | Paper-ready statements are in §4: an LDG proposition with its lemma, the application lemmas, the revised Theorem 4.1, and the list of consequential edits. In the consistency proposition, (A2) is simply dropped. | (drafted; not inserted) |

---

## 1. The finite-sequence theorem (LDG convention)

### 1.1 Statement and proof

Let L be a ranking, r ≥ 0, and m₀, …, m_{r+1} ∈ M_L. Suppose:

- m_{j+1} weakly dominates m_j for 0 ≤ j < r;
- m_{r+1} dominates m_r.

"z weakly dominates x_r, strictly at some world" means exactly that z dominates x_r. Given weak dominance, "not tied at every world" is equivalent to "for some ω₀, not x_r ⪯_{ω₀} z".

**Theorem (PROVED).** If L satisfies (TD), then some m_k with 1 ≤ k ≤ r+1 dominates m₀. More precisely, let k be the least index k ≥ 1 such that m_k dominates m_{k−1}. Then m_k dominates m₀.

*Proof.* Such a k exists, because m_{r+1} dominates m_r. Take 1 ≤ j < k. Then m_j weakly dominates m_{j−1} but does not dominate it, so the two are tied at every world. We show by induction on i = 0, …, k−1 that m_k dominates m_{k−1−i}.

- The case i = 0 is the choice of k.
- Suppose m_k dominates m_{k−1−i}, with i < k−1. The models m_{k−2−i} and m_{k−1−i} are tied at every world. Apply (TD) with m := m_{k−2−i}, m′ := m_{k−1−i} and c := m_k: then m_k dominates m_{k−2−i}.

Taking i = k−1 gives the claim. ∎

No property of the relations is used. In particular, reflexivity, completeness, transitivity and the three-model condition are not used. Neither is the transitivity of the all-world tie relation.

**The auditor's proof (CHECKED).** The AUDIT_A argument is correct under worldwise substitution "a ∼_ω b and c ⪯_ω a ⇒ c ⪯_ω b". Its induction uses substitution in the right-hand slot only, and so does its last step: x_r ⪯_ω x₀ and x₀ ≈ z give x_r ⪯_ω z. Both uses involve only pairs that are tied at every world. So the argument already goes through under (T∀) below.

### 1.2 The exact hypothesis

Define, for a ranking L:

- **(A3)** (worldwise; the LDG transcription of the application's (A3)): if m ∼_ω m′ and c ⪯_ω m′, then c ⪯_ω m.
- **(T∀)** (substitution through all-world ties): if m and m′ are tied at every world and c ⪯_ω m′, then c ⪯_ω m.
- **(W)** (weak-dominance substitution): if m and m′ are tied at every world and c weakly dominates m′, then c weakly dominates m.
- **(TD)** (dominance transmission): if m and m′ are tied at every world and c dominates m′, then c dominates m.

**Proposition (PROVED).** For a fixed ranking L, the following are equivalent:

- (a) L satisfies (TD);
- (b) the theorem holds for every sequence, for every r;
- (c) the theorem holds for every sequence with r = 1.

*Proof.* (a) ⇒ (b) is §1.1. (b) ⇒ (c) is trivial. For (c) ⇒ (a), let m and m′ be tied at every world, and let c dominate m′. The sequence m₀ := m, m₁ := m′, m₂ := c satisfies the hypotheses with r = 1. Since m′ does not dominate m (they are tied), c dominates m. ∎

So (TD) is exactly the weakest hypothesis. The case r = 0 needs no hypothesis at all.

**Lemma (PROVED).** (A3) ⇒ (T∀) ⇒ (W) ⇒ (TD), and none of the implications reverses.

*Proof of the implications.* The first two are immediate: (T∀) is the special case of (A3) in which the tie holds at every world, and (W) is (T∀) applied at each world.

For (W) ⇒ (TD), let m and m′ be tied at every world, and let c dominate m′.

1. By (W), c weakly dominates m.
2. Suppose m also weakly dominated c, so that m and c are tied at every world.
3. m′ weakly dominates m, since m and m′ are tied.
4. Apply (W) to the tied pair (m, c) with m′ weakly dominating m: then m′ weakly dominates c.
5. So c and m′ are tied at every world, which contradicts the assumption that c dominates m′. ∎

*Strictness.* In each example, every relation is reflexive, and only the listed comparisons hold.

- **(T∀) does not imply (A3).** Two worlds ω₁, ω₂ and three models m, m′, c, with m ∼_{ω₁} m′ and c ⪯_{ω₁} m′. The only all-world ties are each model with itself, so (T∀) holds. (A3) fails at ω₁.
- **(W) does not imply (T∀).** Two worlds ω₁, ω₂. The models m and m′ are tied at both worlds, and c ⪯_{ω₁} m′.
  - Weak dominators of m′: m and m′. Weak dominators of m: m and m′. Weak dominators of c: c only. So (W) holds.
  - (T∀) fails at ω₁: c ⪯_{ω₁} m′ but not c ⪯_{ω₁} m.
- **(TD) does not imply (W).** One world. Ties m ∼ m′ and m′ ∼ c; m and c are incomparable.
  - No model dominates any other, so (TD) holds vacuously.
  - (W) fails: c weakly dominates m′, but c does not weakly dominate m. ∎

### 1.3 Some hypothesis is needed (PROVED)

Take one world and models m₀, m₁, c. The relation is reflexive, m₀ ∼ m₁, c ⪯ m₁, not m₁ ⪯ c, and there are no other comparisons.

- m₁ weakly dominates m₀, and c dominates m₁.
- Neither m₁ (tied with m₀) nor c (incomparable with m₀) dominates m₀.

Adding the tie m₀ ∼ c makes the relation complete, and the conclusion still fails. So completeness does not rescue the theorem. Both examples violate (TD), as the proposition requires.

### 1.4 Status of the "existence of a sequence" condition

Suppose m₀ is dominated by some y. Then the sequence m₀, y with r = 0 qualifies, and no hypothesis is needed for this. Under (TD), the converse holds by §1.1. So, under (TD), "every incoherent model begins such a sequence" is **equivalent** to "every incoherent model is dominated". It must therefore be *established* in an application, as §2 does for desirability, and not posited as an axiom. This agrees with AUDIT_B §1.

---

## 2. The ranking-free geometric lemma (application conventions)

Notation follows `appshort.tex`. Define:

- **(U1)**: E₊₊ \ X and X ∩ (−E₊₊) are null.
- **(U2)**: there are no x ∈ supp X and z ∈ supp(E \ X) with z − x ∈ E₊₊.

These are (i) and (ii) of appshort Lemma 3.4, and (U1) and (U2) of app_long Definition 4.4. (D_S° in app_long is E₊₊.)

### 2.1 Audit of where undominatedness enters (CHECKED)

- **Lemma 3.3** (consolidation preserves admissibility) concerns undominated models only. It is replaced by the sequence argument and is no longer needed.
- **Lemma 3.4(i).** The construction Y := (X ∪ E₊₊) \ (−E₊₊) is stated for an arbitrary model. Undominatedness enters only in the final sentence.
- **Lemma 3.4(ii).**
  - The first line, "Let X be undominated, so that it satisfies (i)", is used *only* to get μ_c(X ∩ B(d,ρ)) = μ_c(B(d,ρ)), and (U1) suffices for that.
  - The construction of (G₁, G₂, G₃) and the fact that X′ misses G₂ ⊆ E₊₊ use nothing else.
  - Undominatedness re-enters only at the final step, through Lemma 3.3.
- **Lemma 3.5** (identify) and **Lemma 3.6** (gap) assume only (i) and (ii), together with (M3) and, in 3.5(c), (M2). Neither mentions a ranking.
- **Proof of Theorem 3.1.** Undominatedness is used to obtain (i) and (ii) for X and for X′, through Lemmas 3.3 and 3.4.

So the facts the current proof takes from undominatedness are exactly these:

- X contains E₊₊ and misses −E₊₊ (that is, (U1));
- upward closure ((U2));
- tie preservation (Lemma 3.3).

The case split below replaces all three.

### 2.2 Statement

**Lemma G (consolidation sequences; PROVED).** Assume (M2) and (M3), and let X be an incoherent model. Then there are r ∈ {0,1,2} and models X₀ := X, X₁, …, X_r, Z such that:

- each X_{j+1} is a consolidation of X_j in the sense of Definition 2.5 (def:change), by a triple (G₁, G₂, G₃) of Borel sets disjoint from A_μ with G₁ ∪ G₂ ⊆ X_j and G₃ ∩ X_j = ∅ (exact inclusions);
- Z ≠ X_r, and the change from X_r to Z is guided at every world.

The cases are as follows.

- **(a)** If X violates (U1), then r = 0 and Z = (X ∪ E₊₊) \ (−E₊₊).
- **(b)** If X satisfies (U1) but not (U2), then r = 1 and X₁ is a consolidation of order c = 1.
- **(c)** If X satisfies both (U1) and (U2), then there are c ∈ {1,2} and v₁, v₂ ∈ V := supp X + E₊₊ with (v₁+v₂)/c ∉ V. In that case X₁ is a consolidation of order c that violates (U2), and:
  - if X₁ violates (U1), then r = 1;
  - otherwise X₂ is a consolidation of X₁ of order 1, as in (b), and r = 2.

### 2.3 Proof

**Step A (guided step; no measure conditions).** Let W violate (U1), and put Z := (W ∪ E₊₊) \ (−E₊₊). This is a model, since E₊₊ is open.

- Since E₊₊ ∩ (−E₊₊) = ∅, we have Z \ W = E₊₊ \ W and W \ Z = W ∩ (−E₊₊). These are exact identities.
- Every added gamble has h(ω) > 0 at every ω, and every removed gamble has h(ω) < 0 at every ω. So the change is guided at every world, and the inclusions hold exactly.
- The added and removed sets are not both null, by the violation of (U1). So Z ≠ W.

Atoms need no separate treatment: an atom in E₊₊ \ W, or in W ∩ (−E₊₊), is itself a non-null violation, and the step removes it.

**Step B (upward-closure step; uses (M3)).** Let W satisfy (U1) but not (U2). Take x ∈ supp W and z ∈ supp(E \ W) with z − x ∈ E₊₊. Put 4δ := inf_Ω(z − x) > 0, d := (z − x)/2 and ρ := δ/2.

- *Margin.* For x′ ∈ B(x,ρ), y′ ∈ B(d,ρ) and z′ ∈ B(z,ρ),

  inf_Ω(z′ − x′ − y′) ≥ inf_Ω d − 3ρ = 2δ − 3δ/2 = δ/2,

  and inf_Ω y′ ≥ 2δ − ρ > 0. Hence B(d,ρ) ⊆ E₊₊.
- *Three positive masses.*
  - μ_c(W ∩ B(x,ρ)) > 0, because x ∈ supp W.
  - μ_c(W ∩ B(d,ρ)) = μ_c(B(d,ρ)) > 0. The equality holds because B(d,ρ) ⊆ E₊₊ and E₊₊ \ W is null by (U1). The inequality is (M3).
  - μ_c(B(z,ρ) \ W) > 0, because z ∈ supp(E \ W).
- *Choice of t.* Choose 0 < t < min{μ_c(W ∩ B(x,ρ)), ½ μ_c(B(d,ρ)), μ_c(B(z,ρ) \ W)}.
- *The sets.* Apply Lemma 2.8(a) (measurefacts) three times, choosing Borel sets of μ-measure t:
  - G₁ ⊆ (W ∩ B(x,ρ)) \ A_μ;
  - G₂ ⊆ (W ∩ B(d,ρ)) \ (G₁ ∪ A_μ). This set has μ_c-measure at least μ_c(B(d,ρ)) − t > t;
  - G₃ ⊆ B(z,ρ) \ (W ∪ A_μ).
- *Legitimacy of the triple.*
  - The sets are pairwise disjoint: G₁ ∩ G₂ = ∅ by construction, and G₃ ∩ W = ∅ while G₁ ∪ G₂ ⊆ W.
  - Masses: μ(G₁) = μ(G₂) = μ(G₃) = t, with c = 1.
  - Margin: z′(ω) ≥ x′(ω) + y′(ω) + κ with κ := δ/2, for every x′ ∈ G₁, y′ ∈ G₂, z′ ∈ G₃ and every ω. This holds for the sets themselves.
  - Inclusions: G₁ ∪ G₂ ⊆ W and W ∩ G₃ = ∅ (exact).
- *Conclusion.* W′ := (W \ (G₁ ∪ G₂)) ∪ G₃ misses G₂, since G₂ ∩ G₃ = ∅. Here G₂ ⊆ E₊₊ and μ(G₂) = t > 0, so W′ violates (U1).

This is exactly the construction of appshort Lemma 3.4(ii), with "undominated" replaced by "(U1)".

**Step C (closure step; uses (M2) and (M3)).** Let W satisfy (U1) and (U2) and be incoherent.

- *Existence of v₁, v₂.* appshort Lemma 3.5 needs only (U1), (U2), (M3) and, in part (c), (M2). So does its atom paragraph: by Lemma 2.8(c), (M2) puts every atom in E₊₊ or −E₊₊, and (U1) then places it correctly. Since W is not almost coherent, Lemma 3.5(c) gives c ∈ {1,2} and v₁, v₂ ∈ V with s := (v₁+v₂)/c ∉ V.
- *Choices.* As in Lemma 3.6, choose η with B(v_i, 2η) ⊆ V, and put r := η/8, v_i′ := v_i − η1 and z₀ := s − (η/c)1. I re-checked each step of that construction.
  - B(v_i′, r) ⊆ B(v_i, η + r) ⊆ V. So μ_c(B(v_i′, r) \ W) = 0, by 3.5(a).
  - For z ∈ B(z₀, r), inf(s − z) ≥ η/c − r > 0. If z ∈ cl V, then s ∈ cl V + E₊₊ ⊆ V, which is false. So B(z₀, r) ∩ cl V = ∅, and μ_c(B(z₀, r) ∩ W) = 0, by 3.5(a).
  - *Margin.* z₀ − (v₁′ + v₂′)/c = (η/c)1. So the pointwise margin is at least η/c − r − 2r/c, which equals 5η/8 for c = 1 and η/4 for c = 2. Take κ := η/4.
  - J₀ := B(v₁′ − 3r1, r) ⊆ B(v₁, 3η/2) ⊆ V. For x ∈ B(v₁′, r) and w ∈ J₀, inf(x − w) > r > 0. Hence J₀ ∩ B(v₁′, r) = ∅.
- *Choice of t and the sets.* Choose 0 < t < min{μ_c(B(v₁′, r)), ½ μ_c(B(v₂′, r)), (1/c) μ_c(B(z₀, r)), ½ μ_c(J₀)}. All four masses are positive by (M3). Choose Borel sets avoiding A_μ:
  - G₁ ⊆ W ∩ B(v₁′, r), of measure t. This is possible because μ_c(W ∩ B(v₁′, r)) = μ_c(B(v₁′, r)) > t.
  - G₂ ⊆ (W ∩ B(v₂′, r)) \ G₁, of measure t. The available mass is at least μ_c(B(v₂′, r)) − t > t.
  - G₃ ⊆ B(z₀, r) \ W, of measure ct. The available mass is μ_c(B(z₀, r)) > ct.
- *Legitimacy.* The sets are disjoint. The masses are (t, t, ct). The margin is κ, pointwise, for the sets themselves. The inclusions are exact.
- *W₁ violates (U2).* Put W₁ := (W \ (G₁ ∪ G₂)) ∪ G₃ and J := (J₀ ∩ W) \ G₂.
  - μ_c(J) ≥ μ_c(J₀) − t > 0, and J ⊆ W₁, since J misses G₁ ⊆ B(v₁′, r).
  - Lemma 2.8(b) gives w ∈ J ∩ supp J ⊆ supp W₁ and x ∈ G₁ ∩ supp G₁. Here μ_c(G₁) = t > 0, since G₁ avoids the atoms.
  - G₁ ∩ W₁ = ∅, so x ∈ supp(E \ W₁).
  - x − w ∈ E₊₊. So W₁ violates (U2).

**Assembly.**

- *Case (a):* Step A applied to X.
- *Case (b):* Step B gives X₁ violating (U1). Then Step A applied to X₁ gives Z.
- *Case (c):* Step C gives X₁ violating (U2).
  - If X₁ violates (U1), Step A applied to X₁ gives Z, and r = 1.
  - Otherwise X₁ satisfies (U1) but not (U2). Step B gives X₂ violating (U1), Step A gives Z, and r = 2. ∎

**Where the measure conditions enter.**

- (M3) gives the positive masses in Steps B and C, and is used in Lemma 3.5(a)–(b).
- (M2) enters only in Step C, through Lemma 3.5(c): (M2) is needed for the identification {P_K = 0} = null, and for the location of atoms (Lemma 2.8(c)).
- Null sets: every triple is chosen inside actual representatives with exact inclusions, so the "a.e." clauses of def:change hold trivially.
- Atoms: they are excluded from all G_i, which Sierpiński's theorem needs, and they are handled in the guided step and in Lemma 3.5(c).

---

## 3. The new dominance theorem (application convention)

### 3.1 Statement and proof

The application-convention form of the tie hypothesis is:

**(A3′) Dominance through ties.** If Z and X are tied at every world and Y dominates Z, then Y dominates X.

**Lemma (PROVED).** (A3) implies (A3′).

*Proof.* Let Z and X be tied at every world, and let Y dominate Z.

1. Applying (A3) at each ω gives Y ⪰_ω X at every world.
2. Suppose X ⪰_ω Y at every ω, so that X and Y are tied at every world.
3. Z ⪰_ω X, since Z ∼_ω X.
4. Applying (A3) at each ω, with the tie X ∼_ω Y, gives Z ⪰_ω Y.
5. So Y does not dominate Z, which is a contradiction. Hence Y dominates X. ∎

The all-world form (A3∀) also implies (A3′), by the same proof. (A3∀) says: if Z and X are tied at every world and Y ⪰_ω Z, then Y ⪰_ω X.

**Theorem 4.1′ (PROVED).** Assume (M2) and (M3). Let a ranking satisfy (A1), (A4) and (A3′); in particular, (A1), (A3) and (A4) are enough. Then every incoherent model X is dominated by one of the models X₁, …, X_r, Z of Lemma G.

*Proof.* Put X_{r+1} := Z.

- By (A4), X_{j+1} ⪰_ω X_j for every ω and every j < r.
- By (A1), Z ≻_ω X_r at every ω. So X_{r+1} dominates X_r.
- Let k ≥ 1 be least such that X_k dominates X_{k−1}. For 1 ≤ j < k, X_j and X_{j−1} are tied at every world.
- Applying (A3′) successively to the pairs (X_{k−2}, X_{k−1}), …, (X₀, X₁) shows that X_k dominates X₀ = X. ∎

### 3.2 Where (A2) was used (PROVED)

**The new proof.** (A2) is not used.

**The old proof.** (A2) appears only in appshort Lemma 3.3, and in app_long Lemmas 4.2–4.3, for the strictness clause. It is redundant there given (A3), because the lemma above does the same job. In the old proof's terms:

- Y ⪰_ω X at every world, by (A3).
- If Y did not dominate X, then X and Y would be tied at every world.
- (A3) at ω₀, with the tie X ∼_{ω₀} Y and X′ ⪰_{ω₀} X, would give X′ ⪰_{ω₀} Y, which contradicts Y ≻_{ω₀} X′.

The old proof failed to avoid (A2) only because its argument was local: it supposed X ⪰_{ω₀} Y at one world rather than at all worlds. So the old proof also works under (A1), (A3) and (A4). In fact (A3′) is enough, restricted to the case where Z is a consolidation of X tied with it at every world. The new proof needs no more than that restricted case either.

**Elsewhere.**

- In the consistency proposition, (A2) is *verified* for the integral ranking but used by nothing.
- The repair theorem (app_long §6) does not use the ranking axioms.
- So (A2) can be dropped everywhere.

**The integral ranking.** Under the integral ranking, distinct models are never tied, so k = 1. The first model of the sequence, X₁ (or Z when r = 0), already dominates X.

### 3.3 (A1) and (A4) alone do not suffice (PROVED)

**Setting.** Ω = {1,2}, E = ℝ² with the sup norm, and μ the standard Gaussian.

- μ is atomless with positive density, so (M3) holds, and (M1) holds.
- For (M2): if P_Q(h) = 0, then h − t1 ∉ {P_Q ≥ 0} for every t > 0. So {P_Q = 0} lies in the boundary of the closed convex set {P_Q ≥ 0}. That boundary is Lebesgue-null.

**Ranking.** Define the same relation at both worlds. Y ⪰_ω X iff one of the following holds:

- (i) the change from X to Y is guided at every world;
- (ii) Y is (a.e.) a consolidation of X;
- (iii) X is (a.e.) a consolidation of Y, and the change from Y to X is not guided at every world.

Each clause depends only on a.e.-classes.

**(A4)** holds by clause (ii).

**(A1).** Let X ≠ Y with the change X → Y guided at every world: it adds A and removes B. Then Y ⪰ X by clause (i). Suppose X ⪰ Y; each clause leads to a contradiction.

- *Clause (i).* The change Y → X would be guided at every world, so A and B would lie a.e. in both {h(ω) > 0} and {h(ω) < 0}. Then A and B would be null, so X = Y.
- *Clause (ii).* X would be a consolidation of Y by some (G₁, G₂, G₃). Then A = G₁ ∪ G₂ a.e. and B = G₃ a.e. Fix ω. Since each G_i is non-null, we can choose x ∈ G₁, y ∈ G₂ and z ∈ G₃ with x(ω), y(ω) > 0 and z(ω) < 0. But z(ω) ≥ (x(ω)+y(ω))/c + κ > 0, which is impossible.
- *Clause (iii).* This requires the change X → Y not to be guided at every world, but it is.

So Y ≻_ω X at every ω.

**Every model satisfying (U1) is undominated.** Let X satisfy (U1).

- *First, a guided change from X is null.* With Ω finite, ∩_ω {h(ω) > 0} = E₊₊. So a change from X guided at every world adds a.e. only gambles in E₊₊ \ X and removes only gambles in X ∩ (−E₊₊). Both sets are null, so the change is null.
- *The consolidation change is not guided.* A consolidation change from X adds the non-null set G₃, with G₃ ∩ X null. If it were guided at every world, G₃ would lie a.e. in E₊₊ ⊆ X a.e., a contradiction.
- *Every weak dominator Y of X is tied with X.*
  - If Y ⪰ X via (i), then Y = X.
  - If via (ii), then X ⪰ Y via (iii).
  - If via (iii), then X ⪰ Y via (ii).

So no model dominates X.

**An explicit incoherent model satisfying (U1).** Take X := E₊₊ ∪ U with U := B((1,−1), 1/4).

- *(U1).* E₊₊ \ X = ∅. U ∩ (−E₊₊) = ∅, since the first coordinate of every point of U exceeds 3/4.
- *Incoherence.* Suppose X = D a.e. for some coherent D.
  - D ∩ U has positive Lebesgue measure.
  - By (D3), 2(D ∩ U) ⊆ D. This set has Lebesgue measure 4·Leb(D ∩ U) > 0.
  - 2(D ∩ U) lies in B((2,−2), 1/2), which is disjoint from X: its points have negative second coordinate and first coordinate above 5/4.
  - So D \ X is non-null, which is a contradiction.

So, under a ranking satisfying (A1) and (A4), with (M1)–(M3) holding, an incoherent model can be undominated. By Theorem 4.1′, this ranking must violate (A3′). The proof of Theorem 4.1′ therefore needs some tie hypothesis, just as the abstract theorem does.

---

## 4. Paper-ready statements (not inserted)

### 4.1 LDG: proposition (LDG convention; suggested location after Corollary `cor:coherent-assigned`, or as a short subsection of §4)

```latex
\begin{definition}\label{def:transmission}
A ranking $L$ \emph{transmits dominance through ties} if, whenever $m,m'\in\M_L$ are tied at
every world and a model $c$ dominates $m'$, then $c$ dominates $m$.
\end{definition}

\begin{proposition}[Dominance along finite sequences]\label{prop:sequences}
Let $L$ be a ranking, let $r\ge0$, and let $m_0,\dots,m_{r+1}\in\M_L$ be such that $m_{j+1}$
weakly dominates $m_j$ for $0\le j<r$ and $m_{r+1}$ dominates $m_r$. If $L$ transmits dominance
through ties, then some $m_k$ with $1\le k\le r+1$ dominates $m_0$: indeed, if $k\ge1$ is least
such that $m_k$ dominates $m_{k-1}$, then $m_k$ dominates $m_0$. Conversely, if this conclusion
holds for every such sequence with $r=1$, then $L$ transmits dominance through ties.
\end{proposition}
\begin{proof}
Such a $k$ exists, since $m_{r+1}$ dominates $m_r$. For $1\le j<k$, $m_j$ weakly dominates
$m_{j-1}$ without dominating it, so they are tied at every world (Lemma~\ref{lem:ties}). Since
$m_k$ dominates $m_{k-1}$, and $m_{j-1}$ and $m_j$ are tied at every world for $j=k-1,\dots,1$,
transmission gives in turn that $m_k$ dominates $m_{k-2},\dots,m_0$. Conversely, let $m,m'$ be
tied at every world and let $c$ dominate $m'$. The sequence $m,m',c$ satisfies the hypotheses
with $r=1$; as $m'$ does not dominate $m$, $c$ does.
\end{proof}

\begin{lemma}\label{lem:transmission}
Consider the following conditions on a ranking $L$, for all models $m,m',c$ and worlds $\omega$:
\begin{enumerate}[label=(\alph*)]
\item if $m$ and $m'$ are tied at $\omega$ and $c\preceq_\omega m'$, then $c\preceq_\omega m$;
\item if $m$ and $m'$ are tied at every world and $c\preceq_\omega m'$, then $c\preceq_\omega m$;
\item if $m$ and $m'$ are tied at every world and $c$ weakly dominates $m'$, then $c$ weakly
dominates $m$.
\end{enumerate}
Then (a) implies (b), (b) implies (c), and (c) implies that $L$ transmits dominance through ties.
\end{lemma}
\begin{proof}
The first two implications are immediate. Assume (c), let $m,m'$ be tied at every world, and let
$c$ dominate $m'$. By (c), $c$ weakly dominates $m$. If $m$ weakly dominated $c$, then $m$ and $c$
would be tied at every world; since $m'$ weakly dominates $m$, (c) would make $m'$ weakly dominate
$c$, so that $c$ and $m'$ would be tied at every world, contradicting dominance.
\end{proof}
```

Remark text (prose, to follow the lemma):

> None of the implications in Lemma~\ref{lem:transmission} reverses. Transmission cannot be dropped from Proposition~\ref{prop:sequences}. Take one world and models $m_0,m_1,c$, with each relation reflexive, $m_0$ and $m_1$ tied, and $c\preceq m_1$ but not $m_1\preceq c$. Then $c$ dominates $m_1$, and $m_1$ weakly dominates $m_0$, but neither $m_1$ nor $c$ dominates $m_0$. This remains so if $m_0$ and $c$ are also tied, which makes the relation complete. A dominated model $m_0$ always begins such a sequence, with $r=0$. So, under transmission, "$m_0$ begins such a sequence" is equivalent to "$m_0$ is dominated". The proposition is therefore an inference from comparisons established in other ways, not a new assumption. In the companion paper, the sequences are supplied by the geometry of gambles, and the comparisons by its axioms of consolidation and guidance~\cite[Theorem~4.1 and the consolidation-sequence lemma]{Konek2026}. No reflexivity, completeness, transitivity or three-model condition is used.

Consequential LDG edits (text only):

- `ldgshort_app.tex` l.244: replace "(A1)–(A4)" with "(A1), (A3) and (A4)". Add: "the proof is an application of Proposition~\ref{prop:sequences}".
- `ldg_full_current.tex`:
  - l.51 and l.548: replace "(A1)–(A4)" with "(A1), (A3) and (A4)".
  - l.548: also delete "the three-model condition".
  - l.654: delete "(A2) the three-model condition;" and renumber the list, or keep the companion paper's labels with (A2) marked as retired. Then "satisfies (A1)–(A4)" becomes "(A1), (A3), (A4)".

### 4.2 Application: lemmas replacing Lemmas 3.3–3.4

```latex
\begin{definition}[Sure-gain conditions]\label{def:U}
A model $X$ satisfies \emph{(U1)} if $\Epp\setminus X$ and $X\cap(-\Epp)$ are null, and
\emph{(U2)} if there are no $x\in\supp X$ and $z\in\supp(E\setminus X)$ with $z-x\in\Epp$.
\end{definition}

\begin{lemma}[Guided step]\label{lem:guided-step}
Let $X$ be a model violating (U1), and put $Z\coloneqq(X\cup\Epp)\setminus(-\Epp)$. Then $Z\ne X$,
and the change from $X$ to $Z$ is guided at every world.
\end{lemma}
\begin{proof}
As $\Epp\cap(-\Epp)=\varnothing$, the change adds $\Epp\setminus X$ and removes $X\cap(-\Epp)$.
Every added gamble is positive at every world and every removed gamble negative at every world, so
the change is guided at every world; as $X$ violates (U1), it is not null.
\end{proof}

\begin{lemma}[Upward-closure step]\label{lem:up-step}
Assume (M3). Let $X$ satisfy (U1) but not (U2). Then some consolidation of $X$, with $c=1$,
violates (U1).
\end{lemma}
\begin{proof}
[Text of the present proof of Lemma~\ref{lem:necessary}(ii), from ``Put $4\delta$'' to
``they define a consolidation $X'$ of $X$'', with ``by (i) and (M3)'' read as ``by (U1) and
(M3)''; then:] Since $X'\cap G_2=\varnothing$ and $G_2\subseteq\Epp$ has measure $t>0$,
$X'$ violates (U1).
\end{proof}
```

Lemmas 3.5 and 3.6 (`lem:identify`, `lem:gap`) are unchanged, except that "(i) and (ii) of Lemma~\ref{lem:necessary}" becomes "(U1) and (U2)", and "(i)" and "(ii)" inside their proofs become "(U1)" and "(U2)".

```latex
\begin{lemma}[Consolidation sequences]\label{lem:sequence}
Assume (M2) and (M3), and let $X$ be an incoherent model. There are $r\in\{0,1,2\}$ and models
$X_0\coloneqq X,X_1,\dots,X_r,Z$ such that each $X_{j+1}$ is a consolidation of $X_j$, $Z\ne X_r$,
and the change from $X_r$ to $Z$ is guided at every world. Specifically:
\begin{enumerate}[label=(\alph*)]
\item if $X$ violates (U1), one may take $r=0$;
\item if $X$ satisfies (U1) but not (U2), one may take $r=1$;
\item if $X$ satisfies (U1) and (U2), one may take $r\in\{1,2\}$, where $X_1$ is a consolidation
of order $c$ that violates (U2), with $c$ as in Lemma~\ref{lem:gap}.
\end{enumerate}
\end{lemma}
\begin{proof}
(a) Lemma~\ref{lem:guided-step}. (b) Lemma~\ref{lem:up-step} gives a consolidation $X_1$ of $X$
violating (U1); apply Lemma~\ref{lem:guided-step} to $X_1$. (c) As $X$ is incoherent,
Lemma~\ref{lem:identify}(c) gives $c\in\{1,2\}$ and $v_1,v_2\in V\coloneqq\supp X+\Epp$ with
$(v_1+v_2)/c\notin V$, and Lemma~\ref{lem:gap} gives a consolidation $X_1$ of $X$ violating (U2).
If $X_1$ violates (U1), apply Lemma~\ref{lem:guided-step} to $X_1$, with $r=1$. Otherwise $X_1$
satisfies (U1) but not (U2), and (b) applied to $X_1$ gives $X_2$ and $Z$, with $r=2$.
\end{proof}
```

Text to follow Lemma `lem:sequence`: "No ranking enters Lemmas~\ref{lem:guided-step}--\ref{lem:sequence}. They concern only the geometry of gambles and the measure."

### 4.3 Application: axioms and the revised Theorem 4.1

In Definition `def:axioms`:

- delete (A2);
- keep the labels (A1), (A3) and (A4), or renumber them;
- optionally add:

```latex
\item[(A3$'$)] \emph{Dominance through ties.} If $Z$ and $X$ are tied at every world and $Y$
dominates $Z$, then $Y$ dominates $X$.

A model that dominates $Z$ also dominates every model tied with $Z$ at every world.
```

```latex
\begin{lemma}\label{lem:A3prime}
Every ranking satisfying (A3) satisfies (A3$'$).
\end{lemma}
\begin{proof}
Let $Z$ and $X$ be tied at every world, and let $Y$ dominate $Z$. By (A3), applied at each
world, $Y\succeq_\omega X$ for every $\omega$. If also $X\succeq_\omega Y$ for every $\omega$,
then $X\sim_\omega Y$ and $Z\succeq_\omega X$ at every world, so $Z\succeq_\omega Y$ at every
world by (A3), and $Y$ does not dominate $Z$. Hence $Y$ dominates $X$.
\end{proof}

\begin{theorem}[Incoherent models are dominated]\label{thm:dominance}
Assume (M2) and (M3). Under every ranking satisfying (A1), (A3$'$) and (A4), and in particular
under every ranking satisfying (A1), (A3) and (A4), every incoherent model is dominated. Indeed,
for $X_0,\dots,X_r,Z$ as in Lemma~\ref{lem:sequence}, one of $X_1,\dots,X_r,Z$ dominates $X$.
\end{theorem}
\begin{proof}
Let $X$ be incoherent, take $X_0,\dots,X_r,Z$ from Lemma~\ref{lem:sequence}, and put
$X_{r+1}\coloneqq Z$. By (A4), $X_{j+1}\succeq_\omega X_j$ for every $\omega$ and $j<r$. By
(A1), $Z\succ_\omega X_r$ for every $\omega$, so $X_{r+1}$ dominates $X_r$. Let $k\ge1$ be least
such that $X_k$ dominates $X_{k-1}$. For $1\le j<k$, $X_j$ weakly dominates $X_{j-1}$ without
dominating it, so they are tied at every world. Applying (A3$'$) to the pairs
$(X_{k-2},X_{k-1}),\dots,(X_0,X_1)$ in turn, $X_k$ dominates $X_{k-2},\dots,X_0=X$.
\end{proof}
```

Text to follow the theorem:

> The ranking-theoretic step is an instance of~\cite[Proposition~\ref{prop:sequences}]{LDG}. Some condition on ties is needed. With $\Omega=\{1,2\}$ and a Gaussian $\mu$, let $Y\succeq_\omega X$ hold exactly when the change from $X$ to $Y$ is guided at every world, or $Y$ is a consolidation of $X$, or $X$ is a consolidation of $Y$ and the change from $Y$ to $X$ is not guided at every world. This ranking satisfies (A1) and (A4), but it leaves the incoherent model $\Epp\cup B((1,-1),1/4)$ undominated.

**Deletions.** Lemma 3.3 (`lem:consolidation`) and Lemma 3.4 (`lem:necessary`) are deleted. Lemma 3.4(i) becomes Lemma `lem:guided-step`, and Lemma 3.4(ii) becomes Lemma `lem:up-step`. The old proof of Theorem 3.1 is replaced by the proof above.

### 4.4 Consistency and the corollary

- **Prop `prop:consistent`.**
  - Statement: "satisfies (A1)–(A4)" becomes "satisfies (A1), (A3) and (A4)".
  - Proof: change the paragraph head "(A1)–(A3)" to "(A1) and (A3)", and delete its first sentence (the (A2) argument). Nothing else changes; the (A3) and (A1) arguments use only strict score increase.
  - Optional remark: since distinct models are never tied under this ranking, the first model of the sequence already dominates X.
- **Cor `cor:ldg`.** Replace "(A1)–(A4)" twice with "(A1), (A3) and (A4)", or with "(A1), (A3′) and (A4)".
- **app_long, if maintained.** Make the same edits to:
  - Lemma 4.2: the proof becomes that of Lemma `lem:A3prime`;
  - Lemma 4.3 and Corollary 4.7, whose hypotheses become (A3) and (A4);
  - Theorem 4.1, Corollary 4.10, Proposition 5.5 and Corollary 5.6.

---

## 5. Points to note

- **Which tie hypothesis to adopt in the paper.** (A3′) is the exact condition. The proof in fact uses (A3′) only when Z is a consolidation of X and tied with it at every world. (A3) is the more familiar-looking axiom, and keeping it while dropping (A2) is the smallest change to the paper. Either choice is sound.
- **Whether r ≤ 2 is ever needed.** I did not determine whether r = 2 is ever unavoidable, that is, whether some incoherent model admits no shorter sequence of this kind. Label: UNCLEAR. Nothing depends on it.
