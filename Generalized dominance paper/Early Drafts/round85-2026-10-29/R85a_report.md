# R85a: referee report on the abstract theorems and logical comparisons in AUDIT_countable.md

29 October 2026. Referee R85a. The inputs were AUDIT_countable.md, AUDIT_newranking.md, AUDIT_obstruction83.md, AUDIT_handoff.md, ldgshort.tex and the round-84 summary. I did not take the audit's claims on trust. Where a claim depends on §5–§8 of the application construction, I say so: R85b checks those sections line by line.

Labels: PROVED (proved here), CHECKED (the audit's argument verified, with any repairs noted), UNCLEAR, FAILS.

---

## 0. Conflict with the author's standing instruction (flagged plainly)

The ranking in AUDIT_countable.md §5 accepts a comparison Y ≥_ω X between distinct models only if m(Y)(ω) > m(X)(ω), where m(·)(ω) is the payoff integral ∫_X g(ω) dμ. So every comparison it makes agrees strictly with the integral-score ranking. It is a subrelation of that ranking.

On 29 October the author said: stop using the integral score. It is essentially a strictly proper scoring rule, and so unsuitable for rankings meant to leave imprecise models undominated.

**So the application construction, as written, is built on exactly the score the author has ruled out.** The imprecise models are protected only because the hull clause refuses comparisons. Whenever this ranking does compare two models, it agrees with the strictly proper score.

This is not a side issue:

- The audit's own argument that the countable condition is strictly weaker than W (§9) works *because* the ranking is a subrelation of the payoff ranking. That property forces every W-assignment to consist of precise models (§4 below).
- So the note's main selling point, a ranking satisfying the countable condition but not W, comes from the very feature the author has rejected.

The abstract theorems in §§2–3 do not involve the score, and are assessed on their merits below. The verdict on the application cannot be used until R85c shows that the construction survives without the integral score.

---

## 1. The finite countable-selection theorem (§2)

**Statement as written.** Fix countably many assignments b^j : Δ_n → models, chosen before any rival is considered. For each incoherent x there must be an index j and closed sets A_i(x) ⊆ Δ_n such that:

1. b^j(p) ≥_i x on A_i(x);
2. every p lies in A_i(x) for some i in supp p;
3. at **every** point common to all the A_i(x), b^j(p) and x are not tied at every world.

The conclusion is that every incoherent x is dominated.

**Verdict: CHECKED.**

- The proof is the proof of Theorem W, applied to the index j(x). KKM (ldgshort Lemma lem:kkm) gives a common point p*. Then clause 1 gives weak dominance, and clause 3 gives that the two models are not tied at every world.
- The quantifiers are correct: "for every x there exist j and closed sets", with the b^j fixed beforehand. Clause 3 is universal over the intersection, as it must be.
- **Countability plays no role in the proof.** The same proof works for a collection of any size. Countability is there only to stop the condition from collapsing into a restatement of dominance. Section 3 below shows how weak a barrier that is.

---

## 2. The compact arbitrary-world version (§3)

**Verdict: CHECKED, with two repairs needed.**

**What holds.**

- Θ_j is compact, and the maps θ^j_F : Δ_F → Θ_j are continuous and fixed beforehand.
- So the sets (θ^j_F)^{-1}(K_ω(x)) are closed in Δ_F, and by the second clause they satisfy the KKM covering hypothesis.
- So θ^j_F(p_F) lies in every K_ω(x) with ω ∈ F. Every finite subfamily of the closed sets K_ω(x) therefore has a common point, and compactness gives a point in all of them. No Hausdorff property is needed.
- In the application (§6), Θ = S, the map θ_F(p) = Σ_ω p_ω δ_ω and the assignment q ↦ b_q are all fixed once the countable subcover is chosen, and do not depend on the rival. That requirement is met. Whether K_ω(Y) is closed is R85b's question.

**Repair (a), a quantifier.** The third clause says "at a point in every K_ω(x), the assigned model is not tied with x at every world".

- Read as "there is such a point", the clause simply asserts that some b^j_θ weakly dominates x without being tied with it. That *is* dominance, so the theorem would assume its conclusion.
- It must read "at every point of ⋂_ω K_ω(x)". The application meets this stronger version, because every point of the intersection gives a margin of at least d at every world.

**Repair (b), what the version generalises.**

- §3 asks for a continuous θ_F for *every* finite F, with the witnessing sets being inverse images.
- LDG's thm:local and handoff §4.2 ask only that for each finite G there is some F ⊇ G, a map θ_F (not necessarily continuous) and closed sets A^F_ω(x).
- So §3 is a countable version of a *special case* of thm:local. "W is the one-assignment case" holds for finitely many worlds (as §9 says) but not for the compact version as written.
- Fix: state §3 in the form used by thm:local, with closed A^F_ω(x) and θ_F(A^F_ω(x)) ⊆ K_ω(x). The proof is unchanged.

---

## 3. The logical relations

To compare the conditions precisely, write I for the incoherent models and use the following four conditions.

- **(W)** One assignment handles every x in I.
- **(σW)** The audit's countable condition: countably many fixed assignments, each x in I handled by one of them.
- **(CD)** *Countably many dominators:* there is a countable set {d_k} of models such that every x in I is dominated by some d_k.
- **(Dom)** Every x in I is dominated.

**Lemma 3.1 (PROVED). (CD) implies (σW), using constant assignments.**

- Proof: for each k let b^k(p) = d_k for every p. If d_k dominates x, take A_i(x) = Δ_n for every i.
- Clause 1 holds because d_k ≥_i x at every world. Clause 2 holds trivially. Clause 3 holds because domination rules out a tie at every world.
- In the compact version take Θ_k to be a single point.

### 3.1 W implies σW. CHECKED.

Take a collection with one member.

### 3.2 σW implies Dom. CHECKED.

This is §2 (or §3 with repair (a)).

### 3.3 Dom does not imply σW (the uncountable-pairs example). CHECKED.

Take uncountably many disjoint pairs. The relations are reflexivity plus c_t ≥ x_t at every world.

- Each c_t dominates x_t and is itself undominated.
- At the vertex e_1, clause 2 needs b^j(e_1) ≥_1 x_t. Reflexivity also permits b^j(e_1) = x_t. Even so, any fixed model stands in that relation to at most one rival, because the pairs are disjoint. So each assignment handles at most one x_t.
- The relations are transitive and C_L is closed under ties, so the example is not pathological on LDG's own axioms.

**What this example shows.** The obstruction is purely about cardinality. It needs uncountably many incoherent models whose dominators have nothing in common. It says nothing about the structure of the selection.

### 3.4 σW does not imply W, abstractly. PROVED (trivially).

- Take one world and two disjoint pairs (c_1, x_1), (c_2, x_2), with only reflexivity and c_k ≥ x_k.
- W fails, since no single model is at least as good as both x_1 and x_2.
- σW holds with two constant assignments.

So the abstract separation needs nothing like the heavy argument of §9.

### 3.5 σW does not imply W *for the §5 ranking* (§9). CHECKED, conditional on R85b. The argument depends on the payoff score.

I reconstructed §9's argument for two worlds with Gaussian μ.

1. **Each assigned model is weakly Pareto-optimal.** Suppose W holds with assignment b_p. Fix p and suppose some model Z had m(Z) strictly above m(b_p) in both coordinates.
   - Incoherent models are dense in the metric ρ: add a small bounded ball outside a coherent Z, or keep Z if it is already incoherent.
   - Since |m(Y)(ω) − m(Z)(ω)| ≤ ρ(Y, Z), there is an incoherent x ≠ b_p with m(x) still strictly above m(b_p) in both coordinates.
   - Under the §5 ranking, b_p ≥_i x with b_p ≠ x needs m(b_p)(i) > m(x)(i). So support coverage fails at p.
   - Hence m(b_p) is weakly Pareto-optimal in the range of scores.
2. **Each assigned model is precise.**
   - The range of scores is compact and convex, by Lyapunov's theorem (μ has no atoms).
   - So a weakly Pareto-optimal point maximises q·m(Z) for some q ∈ Δ_2 (separating hyperplane).
   - The maximiser of ∫_Z q(g) dμ is D_q = {g : q(g) > 0}, up to the null set {q(g) = 0}. So every b_p is a precise Bayes model D_q, vertices included.
   - This is a special case of round-84 C1 Theorem 2, which concerns rankings endorsed by an additive field.
3. **KKM forces a precise dominator.**
   - Apply W to the round-83 rival X = T ∪ E. KKM gives some b_{p*} = D_n that dominates X.
   - So D_n is at least as good as X on both payoff scores.
   - By AUDIT_obstruction83 §2, T ⊆ X ⊆ D_n. I re-checked the numbers: s(T) = κ(2/√10, 2/√10), and by Monte Carlo the admissible ratios n_1/n_2 lie in about (0.82, 1.22), inside (√(2/3), √(3/2)).
4. **The copy lemma gives a contradiction.**
   - The move X → D_n only adds gambles. Copying the same addition onto T gives a model that dominates T.
   - But the §5 ranking protects T. Contradiction.

So W fails for the §5 ranking, provided its independence and its protection of T hold (R85b).

**Two cautions.**

- This separation is a fact about one payoff-endorsed ranking, so it inherits the conflict in §0. Without the payoff score, step 1 has no counterpart, and §9 tells us nothing.
- Section 4 shows that the countable condition this ranking does satisfy is met in the most trivial way available.

---

## 4. Substance: what the countable condition really asks for

### 4.1 In the application, a constant assignment works on each neighbourhood. PROVED from the audit's own §6–§7 estimates.

Fix a consistent incoherent X, and let ε, G_ε, δ, a, r be as in §6.

- KKM applied to X itself gives a state q* in every K_ω(X). So m(b_{q*})(ω) − m(X)(ω) ≥ d = δ/2 at every world ω.
- For any Y and any world ω, |m(Y)(ω) − m(X)(ω)| ≤ ∫_{X△Y} |g(ω)| dμ ≤ ρ(X, Y). This bound holds uniformly in ω, including when there are infinitely many worlds.
- So if ρ(X, Y) < r* := min(r, δ/2), then m(b_{q*})(ω) > m(Y)(ω) at **every** world.
- The hull clause b_q∖Y ⊆ H(Y∖b_q) is proved in §6 for *every* q and every Y with ρ(X, Y) < a/2. I checked the direction of monotonicity:
  - H is increasing: Z ⊆ Z′ gives Q_{Z′} ⊆ Q_Z, hence H(Z) ⊆ H(Z′).
  - Y∖G_ε ⊆ Y∖b_q gives G_ε ⊆ H(Y∖G_ε) ⊆ H(Y∖b_q).
  - And b_q∖Y ⊆ G_ε.
  - So the step is correct, given the estimate a > 0 (which uses the trimming lemma; R85b checks this).
- Hence **the single fixed coherent model b_{q*} strictly dominates, at every world, every Y in the ρ-ball of radius r* about X.**
- §7 works the same way: with q₀ fixed, c_{q*} beats every Y with ρ(X, Y) < d₀/4 at every world. There the hull clause holds automatically, because Y∖c_q contains the inconsistent set Y∖U.

The second-countability argument of §8 then picks out countably many coherent models C_k such that every incoherent model is dominated by some C_k. That is (CD). By Lemma 3.1, σW then holds with **constant** assignments.

**Consequence.** Within each neighbourhood the KKM step does no work. It is used once, to prove that each centre X is dominated, and that dominance proof is then repackaged as the condition. The parameter q ∈ S, the maps θ_F and the closed sets K_ω(Y) can all be replaced by a single model and the whole simplex.

### 4.2 Answers to the brief's questions

**Is σW equivalent to "one assignment per open neighbourhood, plus second countability"?**

- What the audit verifies is stronger than that. It verifies *locally uniform dominance*:

  > **(LUD)** Every incoherent x has a neighbourhood U and a model d such that d dominates every incoherent model in U.

  The model d is a single dominator, not a selection mechanism.
- In a space where every open cover of I has a countable subcover (for example a separable metric space), (LUD) implies (CD), which implies σW. **PROVED.**
- The converses fail in general (PROVED):
  - *σW does not imply (CD).* Take two worlds and models c_s, x_t for s, t ∈ [0, 1], with c_s ≥_1 x_t iff s ≥ t and c_s ≥_2 x_t iff s ≤ t, and nothing else apart from reflexivity. Then W holds with b_p = c_{p_1}, A_1(x_t) = {p_1 ≥ t} and A_2(x_t) = {p_1 ≤ t}. But x_t is dominated only by c_t, so uncountably many dominators are needed. This is the only setting in which σW does more than (CD): an assignment that takes uncountably many values does real selection work.
  - *(CD) does not imply (LUD).* Take incoherent models indexed by (0, 1), with c dominating the rational ones and c′ the irrational ones. The relations ignore the topology.

**How much weaker is σW than (LUD)?** Formally it is weaker: it allows genuinely varying assignments. But the audit never uses that extra room. Its verification goes through (LUD), and so through countably many rival-chosen dominators.

**Is σW closer to the rejected rival-dependent assignment than the note suggests?** Yes.

- Handoff §3 rejects "a previously known dominator of x supplies a constant assignment and full-simplex witnessing sets", on the grounds that this repackages dominance.
- σW accepts exactly that device, provided only countably many dominators are used.
- In the application, countably many always suffice. The reason is that dominance is robust under small changes of the rival (the score moves by at most ρ, and the buffer protects the hull clause), and the model space is separable.

So, in the application, the word "countable" excludes nothing that the earlier rejection was aimed at.

**What σW adds beyond dominance in topological settings.**

> **Proposition 4.3 (PROVED).** Suppose the incoherent models I form a space in which every open cover has a countable subcover (for example a separable metric space), and suppose that for each model d, the set of incoherent models that d dominates is open in I. Then (Dom), (LUD), (CD) and σW-with-constant-assignments are equivalent. In particular, (Dom) implies σW.
>
> Proof: (Dom) together with openness gives (LUD). Then use the countable subcover and Lemma 3.1.

So, given a separable model space, σW adds to dominance only *robust openness of dominance* (or something weaker, such as (LUD)). That is a regularity property of the ranking, not a selection property.

Two remarks on how this applies:

- Under the §5 ranking the sets in Proposition 4.3 need not be open for every d, because the hull clause is not stable under small changes. That is why §6 needs its buffer. The buffer establishes openness exactly where it is needed.
- The only way σW can fail while (Dom) holds is the cardinality phenomenon of §3.3: uncountably many rivals whose dominators cannot be shared. That phenomenon cannot occur once (LUD) holds on a separable space.

**Overall.** The note says its condition is "not a restatement of dominance". That is true in the abstract. In the application, which is the only place it is verified, the condition is equivalent to "dominance, robust under small changes of the rival". The KKM selection structure that W was meant to capture plays no part in it.

---

## 5. What would change in LDG if σW were adopted

**(S).** (S) would become (S_σ): for each ranking L, a countable family of assignments (and, in the compact version, parameter spaces and maps), fixed beforehand, with each incoherent m handled by one member. Three further changes come with it.

- The present (S) requires the assigned models to lie in C_L. If that requirement is dropped, as the audit does, the theorem concludes only that incoherent models are dominated, not that they are dominated by members of C_L.
- thm:finite clause (ii) and thm:local clause 2(b) currently quantify over *every* model. They would quantify over incoherent models only, with the index chosen per rival.
- thm:local would need its own countable version, in its present form with F ⊇ G (repair (b) above).

**The disclaimer in the dominance argument.** LDG says: "it is not assumed that any incoherent model is dominated … (S) … says nothing about which other models are dominated."

- Under (S_σ) this can no longer be stated without qualification. By Lemma 3.1, (S_σ) is implied by the assumption "every incoherent model is dominated by one of countably many fixed models".
- An honest text would have to say that (S_σ) is a countable form of dominance with closed witnesses, and that in separable, robust settings it is equivalent to dominance (Proposition 4.3).
- This undermines the paper's stated contribution, namely a structural selection hypothesis that is not a dominance assumption.

**Ties.** (T) (closure under ties of C_L) would be replaced by clause 3, which excludes ties only at the intersection points.

- Theorem thm:argument steps 1–3 survive: incoherent models are dominated under every ranking, hence irrational.
- Step 6 (U_L = C_L) and Corollary cor:coherent-assigned(c) need assigned models in C_L plus (T). Without them those conclusions are lost.
- In the application this costs nothing:
  - The §5 ranking has no ties between distinct models, so (T) holds trivially.
  - The b_q are coherent, so by §5's protection claim they lie in C_L.
  - So the application could keep LDG's form "assigned models in C_L, plus (T)" and needs only the countable relaxation.

**Unchanged.** (E), (A), the dominance principle and Lemma lem:complement are unaffected.

---

## 6. Summary of verdicts

| Claim | Verdict |
|---|---|
| §2 finite countable-selection theorem | CHECKED (countability unused in the proof) |
| §3 compact version | CHECKED after repair (a), tie clause universal over the intersection, and repair (b), restate in thm:local's form |
| W implies σW | CHECKED (finitely many worlds; compact version only after repair (b)) |
| σW implies Dom | CHECKED |
| Dom does not imply σW (uncountable pairs) | CHECKED; the obstruction is purely about cardinality |
| σW does not imply W, abstractly | PROVED, by a two-pair example |
| §9: the §5 ranking fails W | CHECKED for two worlds with Gaussian μ, conditional on R85b's checks of §5. It depends on the ranking being a payoff subrelation, which conflicts with the standing instruction |
| In the application σW is met by constant assignments (via LUD and CD) | PROVED from the audit's §6–§7 estimates (subject to R85b) |
| σW in separable, robust settings is equivalent to dominance | PROVED (Proposition 4.3) |
| "Not a restatement of dominance" | Abstractly true. In the application it FAILS in substance |
| Use of the integral score | Conflicts with the author's 29 October instruction (§0) |

**Recommendation.** Do not adopt σW in LDG as a structural hypothesis distinct from dominance. In the only verified instance, it is "robust dominance plus separability", and its KKM content is idle.

If a countable relaxation is kept, a version with real content is needed. One candidate:

- each assignment must be a single continuous selection whose values do not depend on the rival, and
- the collection must be fixed before the rankings are chosen (for example, indexed by the target).

Alternatively, the selection could be required to remain genuinely non-constant. Both need fresh justification. Any application must also pass R85c's test without the integral score.
