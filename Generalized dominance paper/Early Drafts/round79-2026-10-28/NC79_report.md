# NC79 report: Nielsen (2021), "Accuracy-Dominance and Conditionalization"

Paper: M. Nielsen, *Philosophical Studies* 178 (2021), no. 10, 3217–3236 (text: papers/NIEAACv2.txt, preprint dated 26 Jan 2021). It corrects Briggs and Pettigrew (2020), *Noûs* 54(1), 162–181 ("B&P").

## Results first

Notation (used throughout). Ω finite, partition E = {E_1,…,E_k}, F = [0,1]^{2^Ω} the credence functions. Models are credal strategies x = ⟨c, a⟩ = (c, a_1,…,a_k) ∈ F^{k+1}. Three candidate coherent classes, nested C_N ⊂ C_BP ⊂ C_W:
- **C_W**: c probabilistic and a a conditionalization of c. So a_j = c(·|E_j) when c(E_j) > 0, and a_j is an *arbitrary credence function* when c(E_j) = 0 (Nielsen, Lemma 1).
- **C_BP**: C_W with every a_j probabilistic. This is B&P's "probabilistic and conditionalizing".
- **C_N**: C_BP with every a_j Blackwell, i.e. a_j(E_j) = 1. These are Nielsen's "probabilistic, conditionalizing, Blackwell" strategies. C_N = ρ(Γ) in LDG §8.3.

Nielsen's class of inaccuracy measures splits in two:
- **bounded J**: s(1,0) and s(0,1) are finite, e.g. Brier;
- **unbounded J**: s(1,0) = ∞ or s(0,1) = ∞, e.g. the log score.

Whether unbounded J are admitted depends on the convention for 0·∞ in Strict Propriety, which Nielsen does not fix (see §1).

| Family / coherent class | (E) | (A) | (S) | (T) |
|---|---|---|---|---|
| bounded J, **C_N** | HOLDS | HOLDS | HOLDS (thm:bayes-finite via lem:section's σ) | HOLDS |
| bounded J, C_BP (B&P's class) | HOLDS | **FAILS** (Nielsen's counterexample, which is exactly a failure of (A)) | HOLDS (C_L = C_N) | HOLDS |
| bounded J, C_W | HOLDS | **FAILS** | HOLDS | HOLDS |
| any family containing an unbounded J, C_N | HOLDS | HOLDS | HOLDS | **FAILS** for every unbounded J (plans that differ only on null cells are tied) |
| any family containing an unbounded J, **C_W** | HOLDS | HOLDS | HOLDS | HOLDS |

Key findings:
1. **For bounded J, Nielsen's setting is literally an instance of LDG prop:blocks** (unique minimisers). That proposition plus prop:strict(a) recovers all of Nielsen's Theorems 3 and 4. It does so without Separability or Extensionality, and with lower semicontinuity in place of Continuity. (PROVED; §3, §5)
2. **Nielsen's counterexample to B&P's (III) is precisely a failure of (A)** for the coherent class C_BP. With C_N, all four conditions hold, and thm:argument yields Nielsen's "Blackwell Conclusion". (PROVED)
3. **(S) needs LDG's freedom to assign Bayes models for a smaller-support prior.** Nielsen's natural assignment p ↦ ⟨p, p(·|E_j)⟩ (with any choice on null cells) cannot have lower semicontinuous losses for any bounded J once k ≥ 2 and some cell has two worlds. lem:section's σ works. (PROVED)
4. **There is a gap in Nielsen's class for unbounded J.** Nielsen's J takes values in [0,∞], and his Continuity is compatible with s(1,0) = ∞. Under the convention 0·∞ = 0, the log score satisfies all five of his properties. For such J, J_ω(c) = ∞ whenever c{ω} = 0. Then Lemma 2, Theorem 3(a)(3) and Theorem 4(a) are **false**: his own counterexample strategy is tied with its "Blackwell repair" under the log score. Theorems 3(a)(1),(2),(b),(c) and 4(b) remain true. His proofs subtract J_ω(c) at worlds of null cells, which needs J_ω(c) < ∞. (PROVED, conditional on the 0·∞ = 0 reading)
5. LDG §8 does not currently treat this paper. A paper-ready corollary and paragraph are drafted in §5. No existing sentence of §8 is made inaccurate.

---

## 1. Nielsen's setting, precisely

**Worlds and propositions.** "Let Ω be a finite set of possible worlds", with A = 2^Ω (§2.1).

**Credence functions.** These are any c : A → [0,1]. c is probabilistic if it obeys the probability axioms. v_ω is the valuation (point mass) at ω.

**Inaccuracy measures.** "J : Ω × C → [0,∞] … assigns a non-negative number in the extended real line" (§2.1). Assumed properties:
- *Separability*: J_ω(c) = Σ_A i_ω(c,A).
- *Continuity*: i_ω(c,A) is continuous in c(A), with values in [0,∞].
- *Extensionality*: i_ω(c,A) = s(v_ω(A), c(A)).
- *Strict Propriety*: for probabilistic c and any credence function c' ≠ c, Σ c{ω}J_ω(c) < Σ c{ω}J_ω(c').
- *Temporal Separability*: J_ω(⟨c,a⟩) = J_ω(c) + J_ω(a_{E_ω}). Footnote 3 allows αJ_ω(c) + βJ_ω(a) with α, β > 0.

Nielsen says Strict Propriety is the only one of the first four properties his proofs use explicitly; the others enter through Predd et al. and B&P.

**Consequences of the class (PROVED).**
- Strict Propriety forces Σ c{ω}J_ω(c) < ∞ for every probabilistic c.
- It also forces s(1,x) < ∞ for x > 0 and s(0,x) < ∞ for x < 1. So s can be infinite only at s(1,0) or s(0,1).
- The **0·∞ convention is not fixed**:
  - Under 0·∞ = ∞, Strict Propriety forces J_ω(c) < ∞ for all probabilistic c and all ω. Hence s is finite, and by continuity on a compact set, bounded.
  - Under 0·∞ = 0, which is the convention of LDG's expected loss (Def. def:bayes) and of the literature, the log score s(1,x) = −log x, s(0,x) = −log(1−x) is admitted. Its expectation decomposes into Σ_A [c(A)s(1,·) + (1−c(A))s(0,·)], and each summand is uniquely minimised at c(A).
- In the unbounded case, for probabilistic c we have **J_ω(c) = ∞ iff c{ω} = 0**:
  - if s(1,0) = ∞, use A = {ω};
  - if s(0,1) = ∞, use A = Ω∖{ω}.

**Evidence and strategies.** A credal act is a : E → C. A credal strategy is ⟨c,a⟩. ⟨c,a⟩ is *probabilistic* iff c and every a_E are probabilistic. It is *conditionalizing* iff c(A∩E) = c(E)a_E(A) for all A and E; c need not be probabilistic. a is *Blackwell* iff a_E{ω} = 0 for ω ∉ E.

**Dominance notions.**
- "Strong accuracy-dominance": < at every world. This is LDG *strict* dominance, and with Ω finite it equals uniform dominance.
- "Weak accuracy-dominance": ≤ everywhere and < somewhere. This is LDG *dominance* (def:dominance; for loss rankings, "not tied" means a different profile).

**B&P's Theorem 1 (p. 171), as Nielsen reports it.**
- (I) Non-probabilistic strategies are weakly dominated by probabilistic conditionalizing ones.
- (II) Non-conditionalizing strategies are strongly dominated by probabilistic conditionalizing ones.
- (III) "For each credal strategy that is probabilistic and conditionalizing, there is no alternative credal strategy whatsoever that even weakly accuracy-dominates it."

**Counterexample to (III) (§3).**
- Setup: Ω = {ω1,ω2,ω3}, E = {{ω1},{ω2,ω3}}, Brier score, c = (0, ½, ½).
- Strategies: a_{ω1} = v_{ω2} and a'_{ω1} = v_{ω1}, with both acts equal to c(·|{ω2,ω3}) on the other cell.
- Then ⟨c,a'⟩ weakly dominates ⟨c,a⟩, since J_{ω1}(v_{ω1}) = 0 < 4 = J_{ω1}(v_{ω2}).

**Theorem 3.** Assumes all five properties.
- (a)(1) If c is not probabilistic, ⟨c,a⟩ is strongly dominated by a probabilistic conditionalizing strategy.
- (a)(2) If c is probabilistic and a_E is not, for some E with c(E) > 0, then ⟨c,a⟩ is strongly dominated.
- (a)(3) If c is probabilistic and a_E is not, for some E with c(E) = 0, then ⟨c,a⟩ is weakly dominated.
- (b) Every non-conditionalizing strategy is strongly dominated by a probabilistic conditionalizing one.
- (c)(1) No probabilistic conditionalizing strategy is strongly dominated.
- (c)(2) No probabilistic conditionalizing strategy is weakly dominated by a non-conditionalizing one.

**Theorem 4.** Assumes the same properties, with c probabilistic and ⟨c,a⟩ conditionalizing.
- (a) If ⟨c,a⟩ is not Blackwell, it is weakly dominated by a probabilistic, conditionalizing, Blackwell strategy.
- (b) If it is Blackwell and probabilistic, it is not weakly dominated by any strategy.

**Normative premises.**
- NP1: strong dominance by a strategy that is not weakly dominated. This is B&P's premise.
- NP2: strong dominance by a strategy that is not strongly dominated.
- NP3: weak dominance by a strategy that is not weakly dominated.

**Conclusions.**
- "B&P Conclusion" (from NP1 + Theorems 3 and 4): non-conditionalizing strategies are impermissible.
- "Probabilistic Conclusion" (NP1): c non-probabilistic, or a_E non-probabilistic for a non-null E, is impermissible.
- "Blackwell Conclusion" (NP3): strategies that are not probabilistic, conditionalizing and Blackwell are impermissible.

## 2. Translation into LDG

- Ω: Nielsen's finite set of worlds.
- M = M_L = F^{k+1}, all credal strategies (non-probabilistic ones included).
- For each admissible J, the ranking L_J is the loss L_J(x, ω) = αJ_ω(c) + βJ_ω(a_j) for ω ∈ E_j. This is a loss ranking, so it is complete and a preorder.
- 𝔏 = {L_J : J satisfies Separability, Continuity, Extensionality, Strict Propriety, Temporal Separability}. The bounded subfamily is 𝔏_b. Single-J families {L_J} are also considered, since B&P and Nielsen argue one J at a time.
- C: one of C_N, C_BP, C_W (§Results). The brief's "probabilistic priors with conditionalizing plans" is C_BP or C_W depending on whether null-cell plans must be probabilistic.
- **Block form (LDG Def. def:block-reports):**
  - X_0 = … = X_k = F;
  - S_0 = αJ, and S_j = βJ restricted to F × E_j;
  - ρ_0 = the inclusion of P(Ω) (probabilistic credence functions);
  - ρ_j(q) = q extended by zero from E_j to Ω.
- **Check that ρ(Γ) = C_N (CHECKED).** For a Γ-system (q_0, q_j), the identity q_0(1_{E_j}f) = q_0(E_j)q_j(f) with f = 1_B, B ⊆ E_j, is c(A∩E_j) = c(E_j)·ρ_j(q_j)(A). Here ρ_j(q_j) is probabilistic with ρ_j(q_j)(E_j) = 1. Conversely, for probabilistic Blackwell a_j we have a_j(A) = a_j(A∩E_j).

**Two lemmas used below.** Both are PROVED for every J in Nielsen's class, bounded or not, with 0·∞ = 0.

*Lemma W (weak dominators of C_W models).* Let ⟨c,a⟩ ∈ C_W and L(x) ≤ L(⟨c,a⟩) pointwise, with x = ⟨c',a'⟩. Then c' = c, and a'_j = a_j for every j with c(E_j) > 0.

Proof:
1. E_c L(⟨c,a⟩) is finite. E_c J(c) < ∞ by Strict Propriety. For ω ∈ supp c, J_ω(c(·|E_ω)) < ∞ because c(·|E_ω){ω} > 0.
2. Write E_c J(a') = Σ_{c(E_j)>0} c(E_j)·E_{c(·|E_j)}J(a'_j). By Strict Propriety this is ≥ E_c J(a), with equality iff a'_j = c(·|E_j) on every non-null cell.
3. From αE_cJ(c') + βE_cJ(a') ≤ αE_cJ(c) + βE_cJ(a) < ∞, we get E_cJ(c') ≤ E_cJ(c). So c' = c by Strict Propriety.
4. Then E_cJ(a') ≤ E_cJ(a), so equality holds in step 2. ∎

*Lemma B (bounded J, Blackwell null plans).* Let J be bounded, ⟨c,a⟩ ∈ C_N, and L(x) ≤ L(⟨c,a⟩). Then x = ⟨c,a⟩.

Proof:
1. Lemma W handles the prior and the non-null cells.
2. For a null cell E_j, J_ω(c) < ∞, so it can be cancelled: J_ω(a'_j) ≤ J_ω(a_j) for ω ∈ E_j.
3. Take the a_j-expectation. a_j is supported on E_j, so Strict Propriety gives a'_j = a_j. ∎

This is Nielsen's proof of Theorem 4(b), made explicit about where finiteness enters.

*Bayes models (PROVED, any J in the class).* x is a Bayes model for a prior π iff x_0 = π and x_j = π(·|E_j) for every j with π(E_j) > 0, with x_j arbitrary on π-null cells. The reason is that π·L(x) = απ·J(x_0) + βΣ_{π(E_j)>0} π(E_j)·E_{π(·|E_j)}J(x_j) in [0,∞], and each term has a unique minimiser. **So the Bayes models are exactly C_W.**

## 3. The conditions

### (E) Evaluability: HOLDS (PROVED)
Every L_J has M_L = M. This needs only 𝔏 ≠ ∅; the Brier score is in every reading.

### (A) Coherent admissibility

- **C_N: HOLDS (PROVED).**
  - Bounded J: by Lemma B, no model dominates a C_N model; this is Nielsen's Theorem 4(b) and LDG prop:blocks.
  - Unbounded J: by Lemma W, a weak dominator x of ⟨c,a⟩ ∈ C_N agrees with it on c and on the non-null cells. At ω ∈ supp c the losses are therefore equal. At ω ∉ supp c, J_ω(c) = ∞ on both sides. So L(x) = L(⟨c,a⟩), and there is no dominance.
  - So every C_N model is undominated under *every* J in the class.
- **C_BP: FAILS for 𝔏_b, and for any single bounded J, whenever k ≥ 2 (PROVED).**
  - Take a cell E with c(E) = 0. Take a_E probabilistic with a_E(E) < 1, and the remaining a_j = c(·|E_j).
  - This is in C_BP \ C_N. It is dominated under every bounded J: by (S) and (T) below it is weakly dominated by a C_N model, and the two are not tied by Lemma B.
  - Nielsen's Brier counterexample is the instance with E = {ω1}. So **B&P's claim (III) is exactly (A) for C_BP, and Nielsen's counterexample is exactly its failure.**
  - If an unbounded J is in the family, (A) holds for C_BP, because C_BP ⊆ C_W ⊆ U_J (see below). But then (T) fails.
- **C_W: FAILS for 𝔏_b; HOLDS for any family containing an unbounded J (PROVED).**
  - Unbounded J: by Lemma W and the ∞ argument above, every C_W model is undominated, i.e. C_W ⊆ U_J.
  - Bounded J: a C_W model with a non-Blackwell or non-probabilistic null plan is dominated (same argument as for C_BP).

### (S) Selection: HOLDS for every J in the class, with C_L ⊇ C_N (PROVED)

**Route: thm:bayes-finite**, a case of cor:closed-choice (Ω is finite, so thm:bayes-infinite and the compact-family and linked-set conditions are not needed). Equivalently, the proof of prop:blocks via thm:bayes-infinite works with Θ = Γ compact and every finite set linked.

**Assignment.** c_p := ρ(σ_Ω(p)), where σ_Ω is lem:section's map with F = Ω. All cells meet Ω, η = 1/(2k), and u_j is uniform on E_j. Write σ_Ω(p) = (q_0, r_1,…,r_k). Hypotheses:
- **Bayes choice:**
  - c_p = ⟨q_0, ρ_j(r_j)⟩ is a Bayes model for q_0, and supp q_0 ⊆ supp p (lem:section).
  - Reason: if λ_j > 0, then r_j = q_0(·|E_j). By the Bayes-model characterisation above, ⟨q_0, ρ(r)⟩ is a Bayes model for q_0.
  - The decomposition is a finite sum in [0,∞], so no finiteness is needed here.
- **Competitiveness on supp p:** by lem:bayes-competitive, since loss rankings are complete.
- **Lower semicontinuity:**
  - L(c_p, ω) = αJ_ω(q_0(p)) + βJ_ω(ρ_j(r_j(p))) for ω ∈ E_j.
  - σ_Ω is continuous, and J_ω is continuous on F (Separability plus Continuity, as a [0,∞]-valued function).
  - So p ↦ L(c_p,ω) is continuous, hence lower semicontinuous. For unbounded J this is continuity into [0,∞], which still gives closed sublevel sets.
- **Assigned models in C_L:**
  - c_p ∈ C_N.
  - For bounded J and C = C_N, C_BP or C_W: C_L = C ∩ U_J = C_N, by (A) and Lemma B.
  - For unbounded J: C_N ⊆ C_W = U_J, so c_p ∈ C_L for each of the three classes.
- **Compact family and linked sets:** not needed, since Ω is finite.

**Nielsen's natural assignment does not work (PROVED, bounded J, k ≥ 2, some cell E with two worlds ω1, ω2, and ω3 ∉ E).**
- Suppose c_p is a Bayes model for p itself.
- Along p_ε = ε t δ_{ω1} + ε(1−t) δ_{ω2} + (1−ε) δ_{ω3}, the plan on E is t v_{ω1} + (1−t) v_{ω2}.
- So lsc at δ_{ω3} forces J_{ω1}(x_E) ≤ inf_t J_{ω1}(t v_{ω1} + (1−t) v_{ω2}) = J_{ω1}(v_{ω1}). Cancelling J_{ω1}(δ_{ω3}) uses that it is finite. Strict Propriety at v_{ω1} then gives x_E = v_{ω1}.
- Likewise x_E = v_{ω2}. Contradiction.
- This is LDG ex:conditional transposed to Nielsen's full-algebra setting. **The freedom in thm:bayes-finite (i), a Bayes model for a prior whose support lies within supp p, is needed for this paper.**
- For unbounded J the obstruction disappears. Both sides are ∞ at ω1, and the natural assignment, with a Blackwell choice on null cells, has continuous [0,∞]-valued losses (CHECKED).

### (T) Closure under ties

- **Bounded J, any of the three classes: HOLDS (PROVED).** C_L = C_N, and Lemma B shows that any model tied with a C_N model equals it. This is cor:bayes-coherent(c)'s profile form, and it is the "unique minimisers" clause of prop:blocks.
- **Unbounded J with C_N or C_BP: FAILS (PROVED).**
  - Counterexample, under the log score: Nielsen's own example.
  - J_{ω1}(c) = ∞, since c{ω1} = 0 and s(1,0) = ∞. So ⟨c,a⟩ (a_{ω1} = v_{ω2}) and ⟨c,a'⟩ (a'_{ω1} = v_{ω1}) are tied at every world.
  - ⟨c,a'⟩ ∈ C_N ⊆ C_L, but ⟨c,a⟩ ∉ C_N.
  - For C_BP, replace a_{ω1} by the zero credence function. That strategy is tied with ⟨c,a'⟩ and is not in C_BP.
  - Consequence: ⟨c,a⟩ is undominated under the log score, so by LDG's dominance principle it is rationally permissible in any family containing the log score. The theorem's conclusion "permissible = C_N" is false for such families.
- **Unbounded J with C_W: HOLDS (PROVED).** A model tied with a C_W model weakly dominates it. By Lemma W it has the same prior and the same non-null plans, so it is in C_W. And C_L = C_W.

**What is tied, in general.**
- Bounded J: no model is tied with a coherent (C_N) model other than itself. Ties among incoherent strategies do occur, since profiles have |Ω| coordinates while strategies have (k+1)·2^{|Ω|}. They are irrelevant to (T).
- Unbounded J: plans differing only on null cells are always tied.

### Verdicts of thm:argument
- 𝔏_b (or any single bounded J) with C_N: (E), (A), (S), (T) hold. **Permissible = C_N, U_L = C_N for each J, and every other strategy is dominated by an undominated C_N strategy.** This is Nielsen's Blackwell Conclusion, under LDG's dominance principle.
- Any family containing an unbounded J: the conditions hold for C_W, and **permissible = C_W**. For C_N, (T) fails, and so does the conclusion.

## 4. What Nielsen proves beyond LDG's conclusion, and whether LDG §5 recovers it

| Nielsen | Content | LDG |
|---|---|---|
| Thm 3(a)(1),(2),(b) | strategies ∉ C_W (non-probabilistic c, or a_j ≠ c(·\|E_j) on a non-null cell) are **strongly** dominated by probabilistic conditionalizing strategies | **Recovered, bounded J:** prop:strict case (a). The assigned models c_p have finite losses, so V is usc. A model is strictly dominated iff it is a Bayes model for no prior, i.e. iff it is ∉ C_W, and it is then **uniformly** dominated by an assigned model in C_N, which is undominated. This gives the dominator the Blackwell property and undominatedness directly; Nielsen gets these by Thm 4(a) and footnote 8. **Unbounded J:** prop:strict case (b) applies to the natural assignment (V finite; c_p a Bayes model for p; continuous [0,∞]-valued losses, finite on supp p) (CHECKED). |
| Thm 3(c)(1) | C_BP models are not strongly dominated | Recovered and slightly sharpened: every C_W model is a Bayes model, hence not strictly dominated (prop:strict, first direction). So the strategies dominated but not strictly dominated are exactly C_W \ C_N (bounded J). Nielsen's 3(a)(3) says only "weakly" for those with non-probabilistic null plans. |
| Thm 3(c)(2) | no non-conditionalizing strategy weakly dominates a C_BP model | Follows from the above and transitivity of the loss order. |
| Thm 4(a),(b) | U = C_N | prop:blocks with unique minimisers (bounded J). |
| Proof style | avoids transfinite induction | LDG uses KKM/Brouwer instead; not simpler, but uniform. |

**LDG is more general than Nielsen for bounded J (PROVED).** The route uses only:
- Temporal Separability (block form);
- Strict Propriety;
- finiteness of J on probabilistic credence functions (for the additive class, equivalent to bounded s);
- lower semicontinuity of q ↦ J_ω(q) on probabilities.

Separability, Extensionality and full Continuity are not used.

**Nielsen's results fail for unbounded J (PROVED, 0·∞ = 0 reading).** Lemma 2, Thm 3(a)(3) and Thm 4(a) are false for the log score; the counterexample is in §3 (T). The proofs break at "J_ω(c) + J_ω(p_i) < J_ω(c) + J_ω(a_{E_i})" when J_ω(c) = ∞.

Two points are UNCLEAR:
- whether B&P's Theorem 1 restricts to finite J (their paper is not in the folder);
- whether Nielsen intends 0·∞ = ∞, which would make his class exactly the bounded J and remove the issue.

Nielsen's normative conclusions for the log score:
- The Blackwell Conclusion fails under NP3.
- The B&P and Probabilistic Conclusions still follow under NP1. Strategies ∉ C_W are strongly dominated by C_N strategies, which are undominated.

## 5. LDG §8: current treatment and drafted addition

**Current text.** §8 does not discuss Nielsen (2021) or B&P. Note that `\cite{Nielsen}`, sec:nielsen and thm:nielsen refer to Nielsen (2023, *Mind*), a different paper. **No existing sentence is made inaccurate.** In particular:
- "Ordinary conditioning has no continuous extension to priors that give a cell probability zero, so the Bayes prior must be allowed to differ…" (after def:conditional-systems) is confirmed for this setting by §3 (S).
- prop:blocks's requirement S_j : X_j × F_j → [0,∞) is exactly what excludes the log-score failure.

**Suggested additions** (optional; not corrections):

(i) Bibliography:
```latex
\bibitem{BP20} R.~Briggs and R.~Pettigrew. An accuracy-dominance argument for conditionalization. \emph{No\^us} 54 (2020) 162--181.
\bibitem{Nielsen21} M.~Nielsen. Accuracy-dominance and conditionalization. \emph{Philos. Stud.} 178 (2021) 3217--3236.
```
Consider renaming the existing key `Nielsen` to `Nielsen23` to avoid confusion.

(ii) Introduction, last paragraph. Replace "They give a dominance characterisation for conditional reports given events that may have probability zero, and they apply to …" with:
> They give a dominance characterisation for conditional reports given events that may have probability zero, which includes the plans for updating studied by Briggs and Pettigrew~\cite{BP20} and Nielsen~\cite{Nielsen21}, and they apply to …

(iii) Insert in §8.3, after Example ex:conditional and before "Schervish, Seidenfeld and Kadane conjecture…":

```latex
\emph{Plans for updating.} Briggs and Pettigrew~\cite{BP20} and Nielsen~\cite{Nielsen21} assess plans for updating by their accuracy. In their setting $\Omega$ is finite, $\mathcal F\coloneqq[0,1]^{2^\Omega}$ is the set of credence functions on all subsets of $\Omega$, and a \emph{credal strategy} is a tuple $(c,a_1,\dots,a_k)\in\mathcal F^{k+1}$: a prior $c$ and, for each cell $E_j$, a credence function $a_j$ to adopt on learning $E_j$. An inaccuracy measure $J:\mathcal F\times\Omega\to[0,\infty]$ is \emph{strictly proper} if each probability $q$ is the unique minimiser of $c\mapsto\sum_\omega q_\omega J(c,\omega)$ over $\mathcal F$, and it is extended to strategies by $L((c,a),\omega)\coloneqq\alpha J(c,\omega)+\beta J(a_j,\omega)$ for $\omega\in E_j$, with fixed $\alpha,\beta>0$.

\begin{corollary}\label{cor:updating}
In this setting, let $J$ be finite and strictly proper, with each $q\mapsto J(q,\omega)$ lower semicontinuous on the probabilities. Call a strategy \emph{coherent} if $c$ and every $a_j$ are probabilities, $a_j(E_j)=1$, and $c(A\cap E_j)=c(E_j)\,a_j(A)$ for every $A\subseteq\Omega$ and every $j$. Then:
\begin{enumerate}[label=(\alph*)]
\item the undominated strategies are exactly the coherent ones, and every incoherent strategy is dominated by a coherent one;
\item a strategy is strictly dominated if and only if $c$ is not a probability or $a_j\ne c(\cdot\mid E_j)$ for some $j$ with $c(E_j)>0$; such a strategy is uniformly dominated by a coherent strategy.
\end{enumerate}
\end{corollary}
\begin{proof}
This is the block form of Definition~\ref{def:block-reports} with $X_0=\dots=X_k\coloneqq\mathcal F$, $S_0\coloneqq\alpha J$, $S_j\coloneqq\beta J$ on $\mathcal F\times E_j$, $\rho_0$ the inclusion of the probabilities, and $\rho_j(q)$ the extension of $q\in\PP(E_j)$ by zero. For $q\in\PP(E_j)$, $\sum_{\omega\in E_j}q_\omega J(x,\omega)=\sum_{\omega\in\Omega}\rho_j(q)_\omega J(x,\omega)$, so strict propriety gives block propriety with unique minimisers; the losses along coherent systems are lower semicontinuous; and the coherent models $\rho(\Gamma)$ are the coherent strategies. Proposition~\ref{prop:blocks} gives (a). For (b), the assignment $p\mapsto\rho(\sigma_\Omega(p))$ from its proof meets the hypotheses of Theorem~\ref{thm:bayes-finite} with finite losses, so by Proposition~\ref{prop:strict}(a) a strategy is strictly dominated if and only if it is a Bayes model for no prior, and then an assigned, hence coherent, strategy uniformly dominates it. By~\eqref{eq:blocks} and unique minimisers, the Bayes models for $\pi$ are the strategies with $c=\pi$ and $a_j=\pi(\cdot\mid E_j)$ whenever $\pi(E_j)>0$.
\end{proof}

For additive, extensional and continuous $J$, this is Nielsen's Theorems~3 and~4~\cite{Nielsen21}; the corollary uses neither additivity nor extensionality, and needs only lower semicontinuity on the probabilities. The strategies that are dominated but not strictly dominated are the Bayes models that are not coherent: on some cell of probability zero they plan a credence function that is not a probability, or one that gives the cell probability less than one. Briggs and Pettigrew's Theorem~1 counts every probabilistic conditionalizing strategy as coherent, including those of the second kind; for that coherent class coherent admissibility fails, since such a strategy is dominated under every finite strictly proper $J$, and Nielsen's counterexample~\cite[\S3]{Nielsen21} is an instance. As in Example~\ref{ex:conditional}, the freedom in Theorem~\ref{thm:bayes-finite}(i) is needed: if some cell contains two worlds and $k\ge2$, no assignment of Bayes models for $p$ itself has lower semicontinuous losses. Finiteness of $J$ cannot be dropped. Under the logarithmic score, with $0\cdot\infty=0$, $J(c,\omega)=\infty$ whenever $c$ gives $\omega$ probability zero, so strategies that differ only on cells of probability zero are tied at every world; the undominated strategies are then exactly those with $c$ a probability and $a_j=c(\cdot\mid E_j)$ whenever $c(E_j)>0$, and the coherent class of Corollary~\ref{cor:updating} is not closed under ties.
```

All claims in the drafted text are PROVED in §§2–3 above:
- the log-score characterisation of the undominated strategies: Lemma W plus (S) for unbounded J;
- "no assignment of Bayes models for p itself": the obstruction in §3 (S), which needs finite J at the vertex; the drafted sentence sits inside the finite-J corollary context.

**Optional cross-reference.** The §6.1 paragraph after def:argument-assumptions could note, as an illustration that (A) is substantive, that B&P's claim (III) is (A) for the class of probabilistic conditionalizing strategies and fails.
