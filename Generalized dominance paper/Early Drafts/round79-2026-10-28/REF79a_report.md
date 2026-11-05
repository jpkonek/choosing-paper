# REF79a: referee report on J79 (Joyce 2009) and NC79 (Nielsen 2021)

Scripts: `ref79a/jchk.py`, `ref79a/chk2.py`, `ref79a/nchk.py` (all in this folder). I re-read the paper texts (Joyce pp. 266–296 incl. Appendix; Nielsen §§2–3 and Appendices A–B) and ldg_full.tex §§2–6.1, 8.

## Summary of verdicts

**J79.** Every FAILS verdict survives: (S) fails, (T) fails for the class, and both claimed errors in Joyce are real. There are three outright errors in the report:
1. **WRONG:** the claim that the additive example (and the prop:joyce loss) has "no ties between distinct models". Both losses have such ties. The (T) verdicts still stand, because no model is tied with a *coherent* one, but four passages, including the proposed intro sentence, must change.
2. **WRONG as worded:** "(S) FAILS for N ≥ 3 (PROVED)". Only N = 3 was proved. I give a one-parameter fix of the additive example that proves it for every N ≥ 3.
3. **Inaccurate:** two readings of Joyce. His p. 267 "inadmissible" means *strictly* dominated. His p. 271 standing assumptions are ALETHIC, TRUTH-DIRECTEDNESS and ADMISSIBILITY; COHERENT ADMISSIBILITY is not among them. No verdict changes.

**NC79.** All verdicts survive. The unbounded-score gap in Nielsen is real under the standard convention 0·∞ = 0. It is slightly larger than reported: Nielsen's endorsement of B&P's (I) also fails, and his proof of Thm 4(b) has the same cancellation gap, though 4(b) itself stays true. Two sentences of the drafted cor:updating paragraph claim more than is proved under the corollary's own hypotheses (lsc only). They need a "continuous" or "lsc" qualifier.

---

## 1. J79 (Joyce 2009)

### 1(a) Joyce's exact hypotheses, and whether the counterexamples meet them — CHECKED

**Theorem 2 / 4 (pp. 287, 293).** The hypotheses are:
- TRUTH-DIRECTEDNESS;
- COHERENT ADMISSIBILITY;
- S(b,ν) finite and continuous on all of B_X = [0,1]^N.

He also has standing conditions:
- p. 266: S ≥ 0, real-valued;
- p. 271 n. 9: cell order is immaterial, i.e. invariance under permuting cells and worlds together.

**All three counterexample losses meet every hypothesis:**
- the tie loss (N = 2);
- LDG's prop:joyce loss (N = 3);
- the additive loss (N = 3).

For each one I checked: nonnegative; finite; jointly continuous; truth-directed in the p. 269 sense, which is LDG def:truth-directed; CA; and permutation-invariant. For prop:joyce: 0 truth-directedness sign violations in 20,000 random finite-difference checks; the LDG bounds are correct.

**Joyce's additive form.** It carries weights λ_n summing to 1, and EXTENSIONALITY forces λ_n = 1/N (p. 273). The examples omit the 1/N factor. This is harmless, since positive scaling preserves every condition (lem:rescale).

**Two corrections to J79 §1 (no verdict depends on either):**
- **"'Admissible' means undominated in LDG's sense" is inaccurate.** On p. 267 Joyce defines "dominated" as strict at every ν and says "Credences that are dominated this way are epistemically inadmissible". ADMISSIBILITY (also p. 267) uses weak dominance, and (ii) of Theorem 2 is called "a restatement of CA", which is the weak reading. So Joyce uses "admissible" in both senses.
  - The counterexamples refute (i) on either reading. The tie example has (0,0) not even weakly dominated. The additive example has x_a weakly dominated by nothing else. For prop:joyce, no coherent model weakly dominates x\*.
  - Suggested wording: "Joyce's 'inadmissible' is defined by strict dominance (p. 267), though Theorem 2(ii) uses the weak reading; the counterexamples refute (i) on either."
- **"Joyce assumes the first three throughout (p. 271)" is wrong as listed.** p. 271 presupposes "ALETHIC, TRUTH-DIRECTEDNESS, ADMISSIBILITY". COHERENT ADMISSIBILITY is introduced on p. 280 and is a hypothesis of Theorem 2 only.
- **Minor.** The list of Joyce's conditions omits IMMODESTY and MINIMAL COHERENCE (p. 279). IMMODESTY plus MINIMAL COHERENCE gives PROPRIETY. So the J79 sentence "Theorem 2 fails even under every 2009 condition except PROPRIETY, NORMALITY and 0/1-SYMMETRY" should read "... except PROPRIETY (and IMMODESTY, which yields it), NORMALITY and 0/1-SYMMETRY".

### 1(b) The (T)-failure example L₁ = (1−x₁+x₂)², L₂ = (1+x₁−x₂)² — all claims CHECKED

- **Truth-directed.** 1−x₁+x₂ ∈ [0,2], and squaring is strictly increasing on [0,∞). So L₁ is strictly decreasing in x₁ and strictly increasing in x₂. L₂ is symmetric.
- **Continuous, nonnegative, permutation-invariant.** L₂(x₂,x₁) = L₁(x₁,x₂).
- **Convex, not strictly.** Each L_ω is a square of an affine function.
- **CA.**
  - The profile of x is ((1−d)², (1+d)²) with d = x₁−x₂ and 1±d ≥ 0.
  - L(x) ≤ L(b) forces d ≥ d_b and d ≤ d_b, so the profiles are equal.
  - So no coherent b is dominated.
- **Every credence is tied with a coherent one.** x is tied with ((1+d)/2, (1−d)/2). Numerically, L(0,0) = L(½,½) = (1,1).
- **Consequences.**
  - Every credence is undominated.
  - (T) fails: C_L = Δ is not closed under ties.
  - Theorem 2(i) is false: (0,0) is neither strictly nor weakly dominated.
- **(S) holds via c_p := p.** The Bayes minimiser is d = p₁−p₂, so p is Bayes for p; the losses are continuous; and the assigned models are coherent and undominated.

### 1(c) The second gap, in Lemmas 2 and 2\* — PROVED genuine

Joyce's Lemma 2 (p. 295) says: "The first two possibilities [all f_n positive, all zero] entail S(p,ν_n) ≥ S(c,ν_n) for all n, which contradicts COHERENT ADMISSIBILITY". CA (p. 280) forbids ≥ everywhere *with > somewhere*, so the all-zero case contradicts nothing. Lemma 2\* has the same gap ("only the last possibility conforms").

The gap is actually reached:
- In the tie example take c = (0,0). Then b¹ = (1,0), b² = (0,1) and B⁺ = Δ.
- At p = (½,½), f ≡ 0, so M = 0 and every g_n = 0, giving G(p) = p.
- So Brouwer returns a tie, not a dominator.

**J79 §3.4(e) (Σc < 1 is sound up to ties): CHECKED.**
- b^m = c + (1−Σc)e_m are affinely independent, so λ = μ, and Lemma 1 applies to the μ_m = 0 coordinates.
- Lemma 1 is correct.
- Case 2 of Lemma 2 does yield strict dominance of p by c, which contradicts CA.
- So the outcomes are: c is strictly dominated by a coherent p, or c is tied with one.
- With (T) and C_L = C, the tie is excluded.
- A cosmetic aside: Joyce's claim that every b^m is interior is false when some c_n = 0. It is harmless, because continuity is assumed on all of B_X.

**Lemma 1\* sign for N = 2: CHECKED.** With c = (0.8, 0.7), b¹ = (0.8, 0.2). At ν² (0,1), b¹ is further from the truth in coordinate 2 and equal in coordinate 1, so f₂(b¹) > 0. Unnormalised Brier gives 0.55; with Joyce's 1/N factor it is 0.275.

### 1(d) (S) failure for the prop:joyce loss — CHECKED

| quantity | value |
|---|---|
| L(x\*), x\* = (1,1,0) | (0.337716, 0.337716, 0.717413) |
| L(½,½,0) | (0.379885, 0.379885, 0.588755) |
| grid (h = 0.0025) min over b ∈ Δ of max_{i=1,2}[L_i(b) − L_i(x\*)] | 0.04217 |

- **Competitiveness of c_p := p fails at (½,½,0).** x\* is strictly better at both worlds in supp p.
- **The decisive argument is independent of route.** Any instance of (S) gives a coherent weak dominator of x\* through thm:finite, cor:closed-choice or thm:local, and none exists. So (S) fails. PROVED.
- **Edge-prior Bayes models (my optimiser).**
  - q = 0.5: (1,1,0), with V = 0.33772 against a coherent minimum of 0.37989.
  - q = 0.6: (1, 0.79, 0), with V = 0.33579 against 0.35622.
  - q ≥ 0.75: (1,0,0).
  - This matches J79.
- **(T) holds: CHECKED.** If L(x) ≤ L(b) with b coherent, then x = b, as in LDG's proof.
- **J79's parenthetical "(no ties)" is WRONG.** (0,0,0) and (⅔,⅔,⅔) both have profile (0.448444…)³. In general, x − y = k𝟙 with Σx + Σy = 2 gives a tie. These are ties between incoherent models; (T) is unaffected.

### 1(e) The additive example s(b,1) = 3(1−b)² + 4(1−b), s(b,0) = 3b² + 2b — mostly PROVED, one claim WRONG

**PROVED (and CHECKED exactly):**
- Truth-directed: s′(·,1) ≤ −4 and s′(·,0) ≥ 2.
- Strictly convex.
- Permutation-invariant, additive and extensional.
- Unique Bayes model x_n = clip(2p_n − ⅓). The derivative is 6x + 2 − 12p_n.
- CA: b is the unique Bayes model for the interior prior b/2 + ⅙𝟙, so any weak dominator equals b. Hence (A) holds and (T) holds.
- Unique Bayes model for (½,½,0) is x_a = (⅔,⅔,0), with L(x_a) = (13/3, 13/3, 37/3). So nothing else weakly dominates x_a, coherent or not.
- Coherent margin: min over b ∈ Δ of max_ω[L(b,ω) − L(x_a,ω)] = 1/6, attained at (½,½,0), where L = (9/2, 9/2, 21/2).

**WRONG: "no two distinct models are tied".**
- Here L(x,ω) = A(x) + 7 − 12x_ω, with A(x) = Σ(3x_n² + 2x_n).
- So x − y = k𝟙 with k = ⅔(Σx − 1) gives a tie.
- Example: (7/12, 7/12, 7/12) and (1/12, 1/12, 1/12) both have profile (105/16)³, verified in exact arithmetic.
- Their midpoint (⅓,⅓,⅓) strictly dominates both, consistent with strict convexity.

**Required edits in J79:**
- Results, "What the author must know" item 2: replace "and no two distinct models are tied" with "and no credence is tied with a coherent one".
- §3.3, third bullet: delete "Any loss with no ties between distinct models. This covers prop:joyce and the additive example below". Replace it with "Any loss under which L(x) ≤ L(b), b coherent, forces x = b; this covers prop:joyce and the additive example".
- §3.4(a): change "(T) holds (no ties)" to "(T) holds (no model is tied with a coherent one)".
- §5(e) proposed intro sentence: change "under which no two models are tied" to "under which no incoherent credence is tied with a coherent one". The §5(d) paper text ("closure under ties holds") is already correct.

**WRONG as worded: "(S) FAILS for N ≥ 3 (PROVED)".**
- Both counterexamples are N = 3 only.
- The additive example does not transfer verbatim: b/2 + ⅙𝟙 sums to 1 only when N = 3.
- **Fix (PROVED; CHECKED numerically for N = 3, 4, 5, 7).** Take s(b,1) = 3(1−b)² + 2(N−1)(1−b) and s(b,0) = 3b² + 2b.
  - The unique Bayes model is x_n = clip(((2N+6)p_n − 2)/6, 0, 1).
  - Each coherent b is the unique Bayes model for the interior prior (6b+2)/(2N+6), which sums to 1.
  - At (½,½,0,…) the unique Bayes model is ((N+1)/6 ∧ 1, same, 0, …), which is incoherent.
  - The same argument applies verbatim.
  - N = 3 recovers the original.

### 1(f) Strict propriety + lsc ⇒ (E), (A), (S), (T) — PROVED

Joyce's PROPRIETY (p. 276) gives b as the unique minimiser of Exp_b over all of B_X. This is prop:proper's unique-Bayes hypothesis, so the claim follows from prop:proper:
- (E): trivial.
- (A): C_L = C.
- (S): thm:bayes-finite with c_p = p. This needs only lsc of p ↦ S(p,ω) on Δ.
- (T): uniqueness.

**Log score: CHECKED.** Joyce's log score is the additive (1/N)Σ −ln|1 − ν_n − b_n|, not the true-cell log score. It is strictly proper, and its losses are continuous into [0,∞].

**Hybrid score: CHECKED strictly proper.** For truth-probability q the expected score is (1−b) − (1−q)ln(1−b), uniquely minimised at b = q.

**prop:strict(b) for the log score.** Its proof uses continuity only at worlds in supp p, where the losses are finite. So J79's suggestion to state the "[0,∞]-continuity" reading is correct and harmless.

**§3.5 item 2 (Pexider argument): CHECKED as a sketch.**
- Gordan's step: an interior b of Δ is interior to the cube.
- For additive rules, 0/1-SYMMETRY (p. 274) means s(b,1) − s(1−b,0) = const. That gives T(1−b) = 1 − T(b), as used.

### J79 verdict table — confirmed with corrections

| | J79 verdict | Referee |
|---|---|---|
| (E) | HOLDS | CHECKED |
| (A) | HOLDS | CHECKED |
| (S) | FAILS N ≥ 3; HOLDS N = 2 | CHECKED for N = 3. N ≥ 4 was not proved in J79; proved here with the modified additive loss. N = 2 CHECKED (competitiveness at interior p by CA and completeness, at vertices by truth-directedness). |
| (T) | FAILS for the class; HOLDS for prop:joyce and the additive loss | CHECKED. The "no ties" justification is WRONG; the correct reason is "no ties with coherent models". |

J79 §5 edits (a)–(h): (a)–(d), (f), (g) and (h) are fine. (e) needs the tie wording fixed (above). In (d), the sentence "every coherent credence is undominated and closure under ties holds" is correct as drafted.

---

## 2. NC79 (Nielsen 2021)

### 2(a) (A) fails for B&P's coherent class C_BP with ≥ 2 cells, under bounded scores — PROVED

**Setup.** Take a cell E with c(E) = 0 (this needs k ≥ 2) and a probabilistic a_E with a_E(E) < 1 (possible since E ≠ Ω).

**The strategy is dominated under every bounded J in Nielsen's class.** The derivation is not circular:
- Lemma B gives C_N ⊆ U_J.
- thm:bayes-finite with lem:section's assignment, which lies in C_N, gives a C_N weak dominator.
- Lemma B excludes a tie.

**Nielsen's counterexample** is the singleton-cell case. There strict propriety at v_{ω₁} alone gives J_{ω₁}(v_{ω₁}) < J_{ω₁}(v_{ω₂}). CHECKED: Brier gives a difference of 4, as Nielsen states (profiles (7,2,2) against (3,2,2)).

**Small qualification.** For a null cell with ≥ 2 worlds the dominance uses continuity (or lsc) of J. Nielsen's own Thm 4(a) proof omits exactly this step ("exactly like Briggs and Pettigrew's proof of Lemma 4 and is omitted"). Within Nielsen's class, Continuity covers it.

### 2(b) (S) only via a smaller-support assignment — PROVED for continuous bounded J; scope note

**The obstruction argument is correct:** cell E ⊇ {ω₁,ω₂}, ω₃ ∉ E, p_ε → δ_{ω₃}, giving J_{ω₁}(x_E) ≤ J_{ω₁}(v_{ω₁}) and J_{ω₂}(x_E) ≤ J_{ω₂}(v_{ω₂}). Brier margin: min_x max(…) = ¼‖v₁ − v₂‖² = 1 > 0.

It uses **upper** limits in two places:
- J_{ω₁}(p_ε) → J_{ω₁}(δ_{ω₃});
- inf_t J_{ω₁}(t v₁ + (1−t) v₂) = J_{ω₁}(v₁).

Both require continuity, not just lsc. So:
- the claim is PROVED for Nielsen's (continuous) J;
- it is UNPROVED for the merely-lsc J of the drafted corollary (see 2(d)).

**Scope.** The claim concerns the Bayes route (thm:bayes-finite/infinite) with Bayes models for p itself. It does not exclude other assignments under thm:finite or cor:closed-choice. Report wording "(S) needs LDG's freedom…" should read "the Bayes route to (S) needs…".

**lem:section route: CHECKED.**
- ρ(Γ) = C_N.
- Block propriety follows from strict propriety at ρ_j(q).
- lsc along Γ holds by composition with continuous projections and extension by zero.

### 2(c) The unbounded-score gap — CHECKED; real under 0·∞ = 0; slightly larger than reported

**Does Nielsen allow infinite values? Yes, explicitly:** "J : Ω × C → [0,∞] … assigns a non-negative number in the extended real line", and i_ω : … → [0,∞].
- His Continuity (a limit statement) makes sense in [0,∞].
- He never fixes 0·∞.
- His Strict Propriety sum Σ c{ω} J_ω(c′) meets 0·∞ exactly when c{ω} = 0 and J_ω(c′) = ∞.

**Is the 0·∞ convention relevant? Yes, decisively.**
- Under 0·∞ = 0 (the measure-theoretic standard, and LDG's def:bayes), the additive log score satisfies all five properties. Its expectation decomposes per event A into G_{c(A)}(c′(A)), each uniquely minimised at c(A), with finite minimum.
- If 0·∞ is set to ∞ or left undefined, Strict Propriety excludes every s with s(1,0) = ∞ or s(0,1) = ∞, and the class is the bounded class.
- I'd phrase the second reading that way rather than as "0·∞ = ∞ convention", which is non-standard.
- Note also that Nielsen cites Predd et al.'s Theorem 1 as background, and Predd et al. admit [0,∞]-valued continuous s (as LDG §8 reports). So the log score is plausibly within the intended scope. Label: PROVED conditional on 0·∞ = 0.

**Does the counterexample strategy really tie with its Blackwell repair? Yes.** CHECKED numerically, with c = (0,½,½) on 2^Ω:
- J_{ω₁}(c) = ∞ (event {ω₁}: s(1,0) = ∞).
- ⟨c,a⟩, ⟨c,a′⟩ and ⟨c, zero plan⟩ all have profile (∞, 5.5452, 5.5452).

**What follows (via Lemma W, which I checked step by step):**
- ⟨c,a⟩ is undominated.
- **Thm 4(a) is false.** ⟨c,a⟩ is probabilistic, conditionalizing and not Blackwell, yet undominated.
- **Lemma 2 and Thm 3(a)(3) are false.** ⟨c, zero plan⟩ is conditionalizing and non-probabilistic on a null cell, yet undominated.
- **Additional point NC79 missed: B&P's (I) is also false under the log score.** (I) says every non-probabilistic strategy is weakly dominated by a P-C strategy, and ⟨c, zero plan⟩ is a counterexample. So Nielsen's "(a) (I) is true" fails for unbounded J.
- **Thm 4(b): the statement survives, but Nielsen's proof has the same gap.** "Weak accuracy-dominance … together with Temporal Separability, [gives] J_ω(a′) ≤ J_ω(a) for all ω" cancels J_ω(c), which may be ∞.
  - The statement survives because a strict improvement must occur at a world with finite loss.
  - Under the log score that rules out null cells, and the non-null plans are already pinned by Lemma W.
- **3(a)(1), 3(a)(2), 3(b) and 3(c) survive: CHECKED.**
  - prop:strict(b) applies to the natural assignment with a Blackwell choice on null cells.
  - V is finite.
  - L(c_p,ω) is continuous into [0,∞]: near p(E_j) = 0 the prior term J_ω(p) → ∞ dominates.
  - The losses are finite on supp p.
  - 3(c)(2) follows by transitivity, which is valid with ∞.

**Table rows for unbounded J: CHECKED.**
- C_N: (T) fails.
- C_W: all four hold. This includes mixed families; for the bounded members C_L = C_N, which is closed under ties by Lemma B.

### 2(d) The drafted cor:updating — statement and proof correct; three sentences of the follow-up paragraph need fixing

**Statement and proof: CHECKED.** The corollary meets prop:blocks' hypotheses:
- S_j finite and bounded, because J is finite on a finite Ω.
- Block propriety with unique minimisers.
- lsc along Γ.

Part (b) is valid:
- the lem:section assignment gives thm:bayes-finite with finite losses;
- prop:strict(a);
- the Bayes models for π are C_W, by the per-cell decomposition for finitely supported π.

So (a) and (b) are correct as stated.

**Paragraph after the proof:**
1. **Overclaim.** "since such a strategy is dominated under every finite strictly proper J"
   - This is proved under the corollary's hypotheses, which include lsc, or for singleton null cells.
   - Replace with: "since such a strategy is dominated under every $J$ satisfying the hypotheses of Corollary~\ref{cor:updating}".
2. **Overclaim.** "if some cell contains two worlds and $k\ge2$, no assignment of Bayes models for $p$ itself has lower semicontinuous losses"
   - The proof needs continuity, not just lsc (2(b)).
   - Replace with: "if $J$ is continuous on the probabilities, some cell contains two worlds and $k\ge2$, no assignment …".
3. **Misattribution.** "Briggs and Pettigrew's Theorem~1 counts every probabilistic conditionalizing strategy as coherent". B&P do not speak of coherence.
   - Replace with: "Briggs and Pettigrew's Theorem~1 claims that no probabilistic conditionalizing strategy is dominated (their (III)), which includes those of the second kind; taking these strategies as the coherent class, coherent admissibility fails, …".

**The log-score sentence: CORRECT.** The undominated strategies are exactly C_W, and C_N is not closed under ties. This lies outside prop:blocks, since S_j must be finite there. It is proved directly: thm:bayes-finite allows [0,∞] losses, Lemma W does the rest, and the assignment's losses are continuous into [0,∞]. Suggest adding "(by Theorem~\ref{thm:bayes-finite} directly; Proposition~\ref{prop:blocks} assumes finite block losses)".

**Optional.** After "Finiteness of $J$ cannot be dropped", add: "and then claims (I) of~\cite{BP20} and Theorem~4(a) of~\cite{Nielsen21} fail".

### NC79 verdict table — confirmed

Every cell of NC79's table is CHECKED, subject to the 0·∞ = 0 reading for the unbounded rows. NC79's "No existing sentence of §8 is made inaccurate" is CHECKED: `\cite{Nielsen}` is the 2023 Mind paper.
