# PS79 report: Predd et al. (2009) and Schervish–Seidenfeld–Kadane (2009) against LDG's conditions (E), (A), (S), (T)

## 0. Results first

### Verdict table

| Setting (paper, class of scores) | (E) | (A) | (S) | (T) |
|---|---|---|---|---|
| **Predd et al.**, their "proper" scores (unique minimiser, continuous; values in [0,∞], ∞ allowed at s(1,0), s(0,1)); one score or one per event (§7.1); Ω arbitrary | HOLDS (PROVED) | HOLDS (PROVED) | HOLDS (PROVED; Thm bayes-finite on τ(Ω), Thm bayes-infinite on Ω) | HOLDS (PROVED) |
| **Predd §7.2.1**, merely proper continuous scores satisfying SSK Assumption 3 (finite on (0,1)) | HOLDS | HOLDS | HOLDS (PROVED, same route) | **FAILS** (counterexample §3.2); prop:profiles applies instead (PROVED) |
| **Predd §7.2.1**, merely proper continuous scores violating Assumption 3 (allowed by Predd, excluded by SSK and by LDG §8) | HOLDS | **FAILS** for that ranking (counterexample §3.3); holds for a family only if another member admits each coherent forecast | UNCLEAR in general (holds in the n=1 example via Thm finite, not via Thm bayes-finite) | UNCLEAR in general (holds in the n=1 example) |
| **SSK**, unconditional, finitely many events, continuous strictly proper, Assumption 1 | = Predd row 1 | | | |
| **SSK**, unconditional, continuous merely proper, Assumptions 1 and 3 (Thm 2 Concl. 3, Thm 3 Concl. 4) | HOLDS | HOLDS | HOLDS | **FAILS** in general; prop:profiles applies |
| **SSK**, discontinuous scores (their Thm 1 first bullet, Thm 2 Concls. 1–2) | HOLDS | Ex. 4: HOLDS; Ex. 5: HOLDS; **Ex. 6: FAILS** | **Ex. 4: FAILS; Ex. 5: FAILS**; Ex. 2: HOLDS (LDG ex:ssk-sharp) | Ex. 4: HOLDS; **Ex. 5: FAILS**; Ex. 2: HOLDS |
| **SSK**, conditional forecasts, coherence₁ (their coherent class) | HOLDS | **FAILS** even for Brier (counterexample §3.5) | UNCLEAR | HOLDS for strictly proper (PROVED); FAILS for merely proper |

### Things the author must know

1. **Unconditional, strictly proper, continuous scores (Predd's Theorem 1; SSK Theorem 2, Conclusion 3, strictly proper case): all four conditions hold.** LDG §8's event-forecasts paragraph is correct here. Two small gaps need fixing. First, (S) is a condition on the ranking over Ω, and Ω may be infinite; the paragraph only treats τ(Ω). Second, the convention 0·∞ = 0 in G_t is used but not stated. (§5 gives the replacement text.)
2. **Merely proper continuous scores: (T) genuinely fails.** Under a continuous merely proper score with a flat stretch, an incoherent forecast can have exactly the loss profile of a coherent one, so it is undominated. Then Theorem thm:argument does not apply, and its conclusion is false. The transitivity route (prop:profiles, prop:permissible(c)) is available, since loss rankings are preorders and (S) gives the dominance property. It identifies the undominated forecasts as those with a coherent profile. At the level of the family, the rationally permissible forecasts are then a strict superset of the coherent ones whenever some ranking in the family has such a flat stretch. §8 says "closure under ties may fail" but gives no example and does not state this consequence for the argument. Text is supplied below.
3. **SSK's conditional forecasts: (A) fails for their coherent class (coherence₁), already for Brier.** Coherence₁ allows arbitrary conditional forecasts given events that may have probability 0. Such a forecast can be dominated, in LDG's sense (which is SSK's "weak dominance"), by another coherent₁ forecast. SSK's equivalence survives only because their coherence₃ uses *strict* dominance. LDG's prop:blocks is the right replacement for a finite partition. If coherence is strengthened to full conditional probabilities, (A) holds for finite-valued scores (PROVED, §3.5), but it fails for the log score (counterexample).
4. **Theorem numbering checked.** The local file is the version marked "Submitted to the Annals of Statistics", imsart date July 17, 2008. I fetched CMU Statistics Technical Report 865 (stat.cmu.edu/tr/tr865/tr865.pdf). It is the same document: same title, same imsart line and date, same numbering. All of LDG's citations match it: Theorem 2, Conclusion 3; Lemma 5; Section 6 ("Discussion"); Example 4; and Example 2 (ex:ssk-sharp). The local filename says "Annals of Statistics 2009", but the paper appeared in *Decision Analysis* 6(4) (2009) 202–221, as LDG's bibliography says. I did not check whether the published version renumbers anything.
5. **Predd: only arXiv v1 (16 Oct 2007) is available, and the arXiv record lists no later version.** I could not access the IEEE text, so differences are UNCLEAR. The statements LDG uses (Theorem 1(a),(b)) are as described below in v1. Predd et al.'s "proper" is SSK's "strictly proper", with continuity built into the definition.

---

## 1. The papers' settings

### 1.1 Predd, Seiringer, Lieb, Osherson, Poor, Kulkarni (arXiv 0710.3183v1; IEEE TIT 55 (2009) 4786–4792)

- **Worlds.** Ω is any nonempty set ("Ω can be infinite"). There are finitely many events E_1,…,E_n, which are arbitrary subsets.
- **Models.** Forecasts f ∈ [0,1]^n.
- **Coherent class.** f is coherent if f_i = μ(E_i) for a probability μ. By their Proposition 1 (de Finetti), this holds iff f ∈ conv(V), where V is the set of truth-value vectors.
- **Scores (Definition 2).** A scoring rule is s:{0,1}×[0,1]→[0,∞] satisfying two conditions:
  - (a) "ps(1,x)+(1−p)s(0,x) is uniquely minimized at x=p for all p∈[0,1]";
  - (b) s(i,·) is continuous on [0,1], in the extended sense.
  
  A footnote notes that some authors call these "strictly proper". The text derives that infinite values "can only occur for the arguments (0,1) or (1,0)"; the log score is the example.
- **Penalty.** P_s(ω,f) = Σ_i s(1_{E_i}(ω), f_i).
- **Dominance (Definition 4).** Weak domination means P_s(ω,g) ≤ P_s(ω,f) for all ω; it includes equality, and there is no g≠f clause. Strong domination means strict inequality at every ω.
- **Theorem 1.**
  - (a) "If f is coherent then it is not weakly dominated by any forecast g≠f."
  - (b) "If f is incoherent then it is strongly dominated by some coherent forecast g."
  
  Corollary 1 says that f is weakly dominated by some g≠f iff f is strongly dominated by a coherent g. In the proof the dominating g has finite penalty at every state.
- **Generalisations (§7), stated without proof.**
  - §7.1: a different proper s_i for each event.
  - §7.2.1: if uniqueness in Definition 2(a) is dropped, "a weaker form of Theorem 1 still holds": an incoherent f is weakly dominated (≤) by a coherent g. Strong dominance can fail, as for s ≡ 0.
  - §7.3: the discontinuous case is left open.

### 1.2 Schervish, Seidenfeld, Kadane (TR 865 = local file; Decis. Anal. 6 (2009))

- **Worlds and models.** Ω is arbitrary. C is an arbitrary (possibly infinite) collection of pairs (A,B) with B≠∅. A forecast is P(A|B) ∈ [0,1] for each (A,B) ∈ C. Unconditional forecasts are the case B = Ω.
- **Coherent class (Definition 1, coherence₁).** No finite book with uniformly negative payoff. By Lemma 11, this holds iff some finitely additive R has R(B)P(A|B) = R(A∩B) for every pair. So P(A|B) is unconstrained when R(B)=0.
- **Scores (Definition 3).** A pair (g0,g1) of extended-real functions on [0,1]. The loss is I_B·g1(P(A|B)) if A occurs and I_B·g0(P(A|B)) otherwise. "Proper" means x=p minimises (1−p)g0(x)+pg1(x). "Strictly proper" means p is the unique minimiser. "Merely proper" means proper but not strictly proper.
- **Assumptions.**
  - Assumption 1: g_k bounded below, with g0(0)=g1(1)=0.
  - Assumption 2: g_k continuous at x=k.
  - Assumption 3: g_k finite on (0,1).
- **Lemma 3.** If a proper rule (bounded below) is infinite somewhere in (0,1), then max{g0,g1} = ∞ on all of [0,1], and the rule is not strictly proper. So strict propriety implies Assumption 3.
- **Dominance (Definition 4).** The loss is the total score over a *finite* subcollection. "Weakly dominates" means ≤ at every ω and < at some ω; this is LDG's dominance. "Strictly dominates" means < at every ω.
- **Coherence₃ (Definition 5).** No finite subcollection is *strictly* dominated.
- **Theorem 2** (forecasts that are not weakly Bayes; all rules satisfy Assumptions 1 and 3, and merely proper rules satisfy Assumption 2).
  - Conclusion 1: weak domination by a possibly randomised forecast.
  - Conclusion 2: under Assumption 2 for all rules, strict domination by a possibly randomised forecast.
  - Conclusion 3: if all rules are continuous, strict domination of every non-weakly-Bayes finite subcollection by a coherent forecast.
- **Theorem 3.** For weakly Bayes forecasts, with continuous rules and Assumptions 1 and 3, Conclusion 4: a coherent collection with the same total scores. (The text requires Assumptions 1 and 3; Table 1 lists only Assumption 1.)
- **Theorem 1.** Strictly proper rules with Assumptions 1 and 2: coherence₁ ⇔ coherence₃ with randomised alternatives; with nonrandomised alternatives if the rules are also continuous.
- **Lemma 5.** If a left-continuous merely proper rule satisfying Assumptions 1–3 has a second minimiser p′ for p, then g0 and g1 are constant between p and p′, on the closed interval if the rule is continuous.
- **Section 6.** Coherent₁ conditional forecasts may give disjoint events conditional probabilities summing to more than 1 given a null B. SSK conjecture that restricting coherence₁ to full conditional probabilities would allow a modified coherence₃ to remain equivalent.

## 2. Translation into LDG

### 2.1 Predd

- **Ω.** As in Predd. Equivalently, the finite set τ(Ω) of truth patterns τ(ω) = (1_{E_i}(ω))_i, since the loss depends on ω only through τ(ω).
- **M and M_L.** M = M_L = [0,1]^n for every L.
- **C.** C = conv(V) = {(π(E_i))_i : π a prior on τ(Ω)}.
- **𝔏.** Any nonempty set of rankings L_s, where L_s(f,ω) = Σ_i s_i(τ_i(ω), f_i) and each s_i is Predd-proper (or, in the §7.2.1 variant, merely proper).
- **Expected loss.** For a prior p, the p-expected loss of f is Σ_i G^i_{p(E_i)}(f_i), where G^i_t(y) = t s_i(1,y) + (1−t) s_i(0,y), **with 0·∞ := 0**. LDG's expected loss sums only over charged worlds, so for t∈{0,1} only one branch enters.

### 2.2 SSK

For a finite subcollection 𝒜 = {(A_i,B_i)}_{i≤n} ⊆ C, let L_𝒜(P,ω) = Σ_i 1_{B_i}(ω) g_{1_{A_i}(ω),i}(P_i). Worlds can be taken to be the finitely many constituents. LDG needs one ranking per model space.

- **Faithful translation (T2).**
  - M = ⊔_𝒜 [0,1]^𝒜, the forecast vectors on finite subcollections, tagged by 𝒜.
  - 𝔏 = {L_𝒜}, with M_{L_𝒜} = [0,1]^𝒜.
  - C = the coherent₁ vectors.
  
  An infinite collection is coherent₁ iff every finite restriction is, since coherence₁ is finitary by Definition 1. So SSK's infinite-collection statements are recovered outside LDG, by this finite character.
- **Rejected translation (T1).**
  - M = [0,1]^C, the whole infinite forecast.
  - Each L_𝒜 evaluates the whole forecast through its restriction to 𝒜.
  
  Here (T) FAILS. Take P with P|_𝒜 coherent and undominated, and change a coordinate outside 𝒜 so that the result is incoherent. The new forecast is tied with P at every world, but it is not in C_L. Moreover LDG's principle ("irrational iff dominated under *every* ranking that evaluates it") does not match SSK's coherence₃ ("dominated on *some* finite subcollection"). An incoherent P is undominated under L_𝒜 for any singleton 𝒜 with a nondegenerate event, so P counts as rationally permissible. SSK's Example 7 (no single coherent forecast dominates two incoherent subcollections) also shows that aggregating across subcollections is not a single-ranking matter. Use T2.

## 3. The conditions

Throughout, a loss ranking is a complete preorder, so prop:profiles is available whenever the dominance property holds.

### 3.1 Strictly proper continuous scores (Predd Theorem 1; SSK, strictly proper continuous unconditional case). All four HOLD (PROVED)

**Finiteness.**
- (i) For each t, min G^i_t is finite. Otherwise every y would minimise G^i_t, contradicting uniqueness.
- (ii) Hence V(p) = Σ_i min G^i_{p(E_i)} < ∞, and f is Bayes for p iff f_i = p(E_i) for all i.
- (iii) In particular c_p := (p(E_i))_i is the unique Bayes model for p.

**(A).** Let g weakly dominate c_p. Then the p-expected loss of g is at most V(p), so g is Bayes for p, so g = c_p. So no forecast other than c_p even weakly dominates c_p; this is Predd Theorem 1(a). Every coherent forecast is some c_p, so C_L = C for every L_s ∈ 𝔏. Hence (A) holds for any nonempty family.

**(E).** M_L = M for every L.

**(T).** A forecast tied with c_p weakly dominates it, so it equals c_p.

**(S), finite Ω, or τ(Ω).** Theorem bayes-finite applies with c_p := (p(E_i))_i:
- *Bayes choice:* c_p is Bayes for p itself.
- *Competitiveness on supp p:* this follows from Lemma bayes-competitive (losses are complete).
- *Lower semicontinuity:* p ↦ L(c_p,ω) = Σ_i s_i(τ_i(ω), p(E_i)) is continuous into [0,∞], as a composition of continuous maps followed by a finite sum of continuous [0,∞]-valued maps. Infinite values, such as the log score at (1,0), are handled because continuity is in the extended topology.
- *Assigned models undominated and coherent:* shown under (A).

**(S), arbitrary Ω (needed literally, because (S) is a condition on L over Ω).** Theorem bayes-infinite applies:
- Θ := Δ_{τ(Ω)}, which is compact.
- c_θ := (θ(E_i))_i.
- Every finite F ⊆ Ω is linked, with σ_F(p) := τ_*p (the image prior), which is continuous.
- c_{σ_F(p)} is Bayes for p itself, because the p-expected loss of f is Σ_i G^i_{p(E_i)}(f_i).
- θ ↦ L(c_θ,ω) is continuous.

Alternatively, ties, dominance and uniform dominance agree on Ω and on τ(Ω).

**Unbounded and infinite-valued scores.** A continuous score on [0,1] that is unbounded must take the value ∞. This happens only at s(1,0) and s(0,1), and nothing above needs finiteness there. **Per-event scores (Predd §7.1).** The argument is coordinatewise, so they are covered verbatim.

### 3.2 Merely proper continuous scores with Assumptions 1 and 3 (Predd §7.2.1 restricted; SSK Thm 2 Concl. 3 and Thm 3)

Normalisation is free. Under Assumption 3, s_i(0,0) ≤ s_i(0,½) < ∞, and similarly for s_i(1,1). Subtracting the minima shifts each world by a constant, which preserves the ranking (Lemma rescale) and the Bayes models.

**Finiteness and Bayes models.** G^i_t(t) < ∞ for every t, so V is finite and c_p is Bayes for p. If f is Bayes for p, each f_i minimises G^i_{p(E_i)}. By SSK Lemma 5 (continuous version), s_i(k,f_i) = s_i(k,p(E_i)) for k=0,1, so L(f) = L(c_p). (Lemma 5 needs "g1 does not jump to ∞ at 0", which continuity gives. For strictly proper s_i it is vacuous.)

- **(A) HOLDS.** A weak dominator of c_p is Bayes for p, so it has profile L(c_p) and is not a dominator. Hence C_L = C.
- **(E) HOLDS.**
- **(S) HOLDS.** The route is the same as in §3.1. Bayes choice holds (c_p is Bayes for p), and continuity is unchanged.
- **(T) FAILS (PROVED).**
  - *Simplest counterexample:* s ≡ 0, which is Predd's own example. It is continuous, merely proper, finite and normalised, and every forecast is tied with every other. So any incoherent forecast is tied with a coherent one.
  - *Nondegenerate counterexample:* let λ be Lebesgue measure on [0,⅓]∪[⅔,1], and put g1(x) = ∫_{[x,1)}(1−q)λ(dq) and g0(x) = ∫_{[0,x)}qλ(dq). Explicitly:
    - g0(x) = x²/2 on [0,⅓], 1/18 on [⅓,⅔], and 1/18 + (x²−4/9)/2 on [⅔,1];
    - g1(x) = 1/18 + ((1−x)²−4/9)/2 on [0,⅓], 1/18 on [⅓,⅔], and (1−x)²/2 on [⅔,1].
    
    Then ∂_yG_t(y) = (y−t)·1_{supp λ}(y), so G_t is minimised at t. The score is continuous, finite and normalised, and constant on [⅓,⅔].
    
    Take E_1 = E with E ∉ {∅, Ω}, and E_2 = Ω∖E. The coherent forecast (0.4, 0.6) and the incoherent forecast (0.4, 0.4) have the same loss profile, because both second coordinates lie in the flat stretch.
  
  So the incoherent forecast is undominated, since any dominator of it would dominate (0.4,0.6). The conclusion of thm:argument therefore fails for any family that contains this ranking. (T) does hold for particular event structures, for example n = 1 with E nondegenerate, where every forecast is coherent.
- **Nearby result (PROVED).** Cor. bayes-coherent(b) gives the dominance property, and the ranking is a preorder. So prop:profiles applies: U_L = {f : L(f) = L(c) for some coherent c}, and every other forecast is dominated by a coherent one. By Prop. strict(b) (V finite, c_p Bayes for p, continuous losses), a forecast that is Bayes for no prior is even uniformly dominated by a coherent one. Prop. permissible(c) says a forecast is irrational iff, under every ranking in 𝔏, a coherent forecast dominates it. The rationally permissible forecasts are ⋃_{L∈𝔏}{f : L(f) is a coherent profile under L}. This is C if and only if every ranking in 𝔏 satisfies (T).
- **Remark on SSK's criticism of Predd §7.2.1.** SSK (§6) object that Predd et al. "claim … a weakly dominating coherent₁ set of forecasts", whereas really one gets strict domination or identical scores. The disagreement is terminological. Predd's weak domination (Definition 4(a)) is ≤ everywhere and includes identical scores. SSK's requires strictness somewhere. Read with Predd's definition, the §7.2.1 claim is what Cor. bayes-coherent(b) proves under Assumption 3.

### 3.3 Merely proper continuous scores violating Assumption 3 (inside Predd §7.2.1's literal class)

By SSK Lemma 3, max{g0,g1} = ∞ on all of [0,1]. Such scores are continuous in the extended sense. Example:
- g0(x) = x/(½−x) on [0,½), and ∞ on [½,1];
- g1(x) = ∞ on [0,½], and (1−x)/(x−½) on (½,1].

This is merely proper: for p ∈ (0,1) every x gives expected score ∞.

Take n = 1 and E ∉ {∅,Ω}. Every forecast is coherent. The forecast 0.3 has profile (∞, 1.5), and the forecast 0 has profile (∞, 0), so 0 dominates 0.3.

- **(A) FAILS** for this ranking, and for any family in which no other ranking admits 0.3.
- **(S).** In this example (S) holds through Thm finite but not through Thm bayes-finite. Here C_L = {0,1}, and every forecast has an infinite loss at one world. Assign c_p = 1 at p_E ≥ ½ and 0 otherwise. For a rival whose loss at E is ∞, take A_E = Δ and A_{E^c} = {δ_{E^c}}; symmetrically for the other kind of rival. A Bayes-choice assignment into {0,1} with lsc losses would split the connected Δ into two disjoint closed sets, which is impossible.
- **(T)** holds in this example.
- **General case:** UNCLEAR.

LDG §8 excludes this subclass by its finiteness requirement. That is correct, but the reason should be stated (see §5).

### 3.4 Discontinuous scores (SSK Theorem 1 first bullet; Theorem 2 Conclusions 1–2)

- **SSK Example 4** (strictly proper, Assumption 2 holds, interior jumps; two complementary events). Coherent forecasts are undominated: by strict propriety a weak dominator is Bayes, hence equal. So **(A) and (T) HOLD**. **(S) FAILS** by any route, because (S) implies the dominance property, and (0.6,0.7) has no coherent weak dominator (SSK's computation).
  
  Nevertheless every incoherent forecast is dominated (CHECKED). Write the profile as Brier plus a constant on each of the four quadrants determined by x ≷ ½ and y ≷ ½. On the two mixed quadrants and on x,y ≤ ½, the Brier projection onto x+y=1 stays in the quadrant and strictly dominates. On x,y > ½, the move (x−ε, y−ε) lowers both losses strictly, since x+y > 1. So U_L = C even though (S) fails. LDG's conditions are sufficient but not necessary.
- **SSK Example 5** (merely proper, interior jump). (0.5,0.7) is incoherent and is Bayes for an interior prior, so it is undominated. **(S) FAILS.** **(T) FAILS**: (0,1) is coherent, undominated, and tied with the incoherent (0,0.7). Its profile (2.5,0) requires x=0 and g1(y)=0, that is y>½. **(A) HOLDS.**
- **SSK Example 6** (merely proper, discontinuous). The coherent forecast (½,½,½) has total scores 1 at all four constituents. The incoherent (0,0,0) has scores (1,½,½,1). So **(A) FAILS** for this ranking.
- **SSK Example 2** (strictly proper; g0 jumps at 0, so Assumption 2 fails). This is LDG ex:ssk-sharp: (A), (S) (via lsc) and (T) all HOLD. I checked V, the lsc claims and the profiles there.
- **Where the lsc route reaches (PROVED).** For a proper score with Assumption 3, both branches are lsc iff the score is continuous on (0,1), g1 is continuous at 0, and g0 is continuous at 1. Only the "harmless" endpoint jumps (g0 at 0, g1 at 1) are allowed.
  
  Proof. g1 is decreasing and g0 increasing. So lsc means g1 is right-continuous and g0 left-continuous. At an interior jump both branches jump (SSK Lemma 6 proof, via Lemma 4). Propriety makes V(t) = G_t(t) concave and finite, hence continuous, on (0,1). But at the jump, the lsc choice gives G_x(x) = V(x+) − (1−x)J0 < V(x), where J0 > 0 is the jump of g0. That contradicts G_x(x) = V(x).
  
  So Thm bayes-finite with c_p = (p(E_i)) covers exactly these scores. Other routes can still work: for n=1, Cor. closed-choice applies to any strictly proper score, since the comparison sets are {t ≥ x} and {t ≤ x}.

### 3.5 SSK's conditional forecasts (translation T2, C = coherence₁)

- **(E) HOLDS.**
- **(A) FAILS (PROVED), already for Brier.** Take pairs (A1|B), (A2|B) with A1∩A2 = ∅, A1∩B ≠ ∅ ≠ A2∩B, and B ≠ Ω. The forecast (0.9, 0.7) is coherent₁. SSK §6 says: "These previsions are coherent₁ because no book can be made against them" (take R(B)=0).
  
  The forecast (0.6, 0.4) dominates it. On B^c both forecasts score 0. On B the Brier totals are (0.32, 0.72, 0.52) against (0.5, 0.9, 1.3), at A1∩B, A2∩B and B∖(A1∪A2). This ranking is the only one that evaluates the model, so (A) fails. Coherence₃ survives only because it uses strict dominance.
  
  A one-pair version: A∩B = ∅, B ≠ Ω, P(A|B) = 0.9 is coherent₁ and is dominated by 0.
- **(T) HOLDS for strictly proper rules with Assumptions 1 and 3 (PROVED).** Let P be undominated and coherent₁, with R as in Lemma 11, and let Q be tied with P. Then Q has the same R-expected total, which is finite by Assumptions 1 and 3 (SSK's remark before Lemma 9). So Q is Bayes for R. By Lemma 9 and strict propriety, Q_i = P_i whenever R(B_i) > 0. The remaining coordinates are unconstrained by R. So Q is coherent₁ with the same R, and Q is undominated. For merely proper rules (T) fails, as in §3.2.
- **(S) UNCLEAR.** Bayes choices require a continuous p ↦ (assigned forecast) whose Bayes prior has support in supp p, with lsc losses as p(B_i) → 0. LDG's Lemma lem:section builds such a map only for a partition. For general overlapping B_i I have no construction (CONJECTURE: one exists).
- **Nearby result: full conditional probabilities (SSK's §6 conjecture).** Let C′ be the forecasts P_i = μ(A_i|B_i) for a full conditional probability μ on the finite constituent algebra, with layers μ_0, μ_1, … in lexicographic form.
  - **Finite-valued strictly proper scores: (A) and (T) HOLD for C′ (PROVED).** Suppose Q weakly dominates P. Induct on layers. On supp μ_k, coordinates first charged at an earlier layer already agree. Coordinates first charged later contribute 0 there. Comparing μ_k-expectations, which are finite, leaves only the layer-k coordinates, and P is Bayes for μ_k on them. So they agree by strict propriety. Hence Q = P.
  - **With ∞ allowed, (A) FAILS for C′ (PROVED).** Use the log score, constituents {1,2,3}, pairs (E|Ω) with E={2}, and (F|B) with B={2,3}, F={2}. Take μ(·|Ω) = δ_1 and μ(·|B) uniform, so P = (0, ½) with profile (0, ∞, ln 2). The forecast Q = (0, 0) is also in C′ (take μ′(·|B) = δ_3), and its profile is (0, ∞, 0), so Q dominates P.
  
  LDG's prop:blocks (finite partition, block losses in [0,∞)) is consistent with both facts.
- **Possible gap in SSK's own proof (UNCLEAR, outside LDG's citations).** In Lemma 12, SSK set r_i "arbitrary" when R(B_i) = 0 and then treat δ_0 as r. Equal Bayes risk does not give equal risk at R-null constituents. For unconditional pairs, R(B_i) = 1, and the step is fine: uniqueness gives this for strictly proper rules, and Lemma 5 for merely proper continuous ones. For conditional pairs, r_i needs a specific choice. One plausible fix uses the convexity of the score set.

## 4. What the papers prove beyond LDG's conclusion, and whether LDG §5 recovers it

- **Predd Theorem 1(b): strong dominance by a coherent forecast with finite penalties.** Because τ(Ω) is finite, this is uniform dominance. Recovered by Prop. strict(b), whose hypotheses were checked in §3.1, applied on τ(Ω).
- **Predd Theorem 1(a): no forecast g ≠ c_p even weakly (≤) dominates c_p.** This is stronger than C_L = C together with (T). Recovered by the one-line argument in LDG's paragraph. Predd's Corollary 1 then follows.
- **SSK Theorem 2, Conclusion 3, for finitely many unconditional events.** Recovered by Prop. strict(b), with uniform dominance. For a finite collection, "not weakly Bayes" is the same as "Bayes for no prior": if f is Bayes for R with V finite, each sub-sum is minimised. For infinite collections it is recovered per finite subcollection, with the aggregation done by the finitary character of coherence₁ (translation T2).
- **SSK Theorem 3, Conclusion 4 (finite unconditional case).** Recovered: Bayes models have coherent profiles. But this uses SSK's Lemma 5, which is SSK's own proof of Theorem 3, so it is not an independent recovery.
- **SSK Conclusions 1–2 (randomised dominators, discontinuous scores).** Not recovered; LDG has no randomised models. LDG's ex:rescale explains why randomisation is a different question.
- **SSK's conditional results and Theorem 1 for conditionals.** Not recovered (§3.5).
- **SSK Theorem 7 (minimax strengthening: a non-Bayes action with finite losses is strictly dominated by a randomised rule).** Its nonrandomised analogue, under lsc and usc V, is Prop. strict, which also handles infinite losses through Ω_∞.

## 5. LDG §8 under the current axioms: sentences to change

### 5.1 prop:proper

prop:proper is correct as stated. Optional addition after its proof:

> "In the terms of Definition def:argument-assumptions, the proof verifies (S) for $L$ (through Theorem thm:bayes-finite with $c_p:=p$) and, when $p$ is the only Bayes model for $p$, (T); without uniqueness (T) may fail, and Proposition prop:profiles replaces Theorem thm:argument."

### 5.2 Event-forecasts paragraph

**(a) The sentence on expected loss.** Current text:

> "The $p$-expected loss of $f$ is $\sum_iG_{p(E_i)}(f_i)$, where $G_t(y)\coloneqq ts(1,y)+(1-t)s(0,y)$."

Replace with:

> "The $p$-expected loss of $f$ is $\sum_iG_{p(E_i)}(f_i)$, where $G_t(y)\coloneqq ts(1,y)+(1-t)s(0,y)$ with $0\cdot\infty\coloneqq0$, since worlds that $p$ does not charge do not enter."

**(b) The definition of proper.** Current text:

> "Call $s$ \emph{proper} if each $G_t$ is minimised at $t$, and \emph{strictly proper} if $t$ is its unique minimiser."

Append:

> "(Predd et al.\ call continuous strictly proper scores `proper'.)"

**(c) The sentence ending "which is~\cite[Theorem~1]{Predd}".** Current text:

> "Theorem~\ref{thm:bayes-finite}, Corollary~\ref{cor:bayes-coherent} and Proposition~\ref{prop:strict}(b) therefore show that every incoherent forecast is uniformly dominated by a coherent one, which is~\cite[Theorem~1]{Predd}."

Replace with:

> "Theorem~\ref{thm:bayes-finite}, Corollary~\ref{cor:bayes-coherent} and Proposition~\ref{prop:strict}(b) therefore show that every incoherent forecast is uniformly dominated by a coherent one; with the fact that no forecast other than $c_p$ weakly dominates $c_p$, this is~\cite[Theorem~1]{Predd}, and the argument applies unchanged to a different strictly proper continuous score for each event, as in~\cite[\S7.1]{Predd}. Selection holds for the ranking on $\Omega$ itself, not only on $\tau(\Omega)$: Theorem~\ref{thm:bayes-infinite} applies with $\Theta\coloneqq\Delta_{\tau(\Omega)}$, $c_\theta\coloneqq(\theta(E_i))_i$, every finite set linked and $\sigma_F(p)$ the image of $p$ under $\tau$. So any family of such rankings on the same events satisfies (E), (A), (S) and (T), and Theorem~\ref{thm:argument} applies."

**(d) The merely proper sentence.** Current text:

> "The same argument allows a different continuous score $s_i$ for each event that is merely proper, in the same sense with $s_i$ in place of $s$, with $s_i(0,y)<\infty$ for $y<1$ and $s_i(1,y)<\infty$ for $y>0$, normalised so that $s_i(0,0)=s_i(1,1)=0$."

Replace with:

> "The same argument allows a different continuous score $s_i$ for each event that is proper but not necessarily strictly proper, with $s_i(0,y)<\infty$ for $y<1$ and $s_i(1,y)<\infty$ for $y>0$, normalised so that $s_i(0,0)=s_i(1,1)=0$ (Assumptions~1 and~3 of~\cite{SSK09}; the normalisation subtracts a constant at each world and changes neither the ranking nor the Bayes models). The finiteness condition matters: a proper score that is infinite somewhere in $(0,1)$ has $\max\{s_i(0,y),s_i(1,y)\}=\infty$ for every $y$~\cite[Lemma~3]{SSK09}, and then a coherent forecast can be dominated; for one event $E\ne\varnothing,\Omega$ and $s(0,y)=y/(\frac12-y)$ for $y<\frac12$, $s(1,y)=(1-y)/(y-\frac12)$ for $y>\frac12$, and $\infty$ otherwise, the forecast $0$ dominates the forecast $0.3$."

**(e) The sentence on closure under ties.** Current text:

> "So $\C_L=\C$, although closure under ties may fail."

Replace with:

> "So $\C_L=\C$, and (S) holds as before, but closure under ties may fail. For instance, let $E_2=\Omega\setminus E_1$ with $E_1\ne\varnothing,\Omega$, and score $E_2$ by $s(1,x)\coloneqq\int_{[x,1)}(1-q)\,\lambda(dq)$ and $s(0,x)\coloneqq\int_{[0,x)}q\,\lambda(dq)$, with $\lambda$ Lebesgue measure on $[0,\frac13]\cup[\frac23,1]$; this score is continuous, finite and proper, and constant on $[\frac13,\frac23]$. Then the incoherent forecast $(0.4,0.4)$ has the same loss profile as the coherent forecast $(0.4,0.6)$, so it is undominated, and Theorem~\ref{thm:argument} does not apply to a family containing this ranking."

**(f) The sentence citing SSK Theorem 2.** Current text:

> "Theorem~\ref{thm:bayes-finite}, Corollary~\ref{cor:bayes-coherent}(b) and Proposition~\ref{prop:profiles} show that the undominated forecasts are those with a coherent loss profile, and Proposition~\ref{prop:strict}(b) that every forecast that is a Bayes model for no prior is uniformly dominated by a coherent one. This is~\cite[Theorem~2, Conclusion~3]{SSK09} for unconditional forecasts."

Replace with:

> "Loss rankings are transitive, so Theorem~\ref{thm:bayes-finite}, Corollary~\ref{cor:bayes-coherent}(b) and Proposition~\ref{prop:profiles} show that the undominated forecasts are those with a coherent loss profile, and Proposition~\ref{prop:strict}(b) that every forecast that is a Bayes model for no prior is uniformly dominated by a coherent one. For finitely many unconditional events this is~\cite[Theorem~2, Conclusion~3]{SSK09}, together with~\cite[Theorem~3, Conclusion~4]{SSK09}, whose proof is the appeal to~\cite[Lemma~5]{SSK09} above. For a family containing such rankings, Proposition~\ref{prop:permissible}(c) shows that a forecast is irrational exactly when, under every ranking in the family, a coherent forecast dominates it; the rationally permissible forecasts are those whose loss profile under some ranking in the family is that of a coherent forecast, and these can be incoherent."

**(g) Optional, after "Continuity cannot simply be dropped~\cite{SSK09}" in the Pettigrew paragraph.** Add:

> "For discontinuous scores each of our conditions can fail: in~\cite[Example~4]{SSK09} selection fails, since an incoherent forecast has no coherent weak dominator; in~\cite[Example~5]{SSK09} an incoherent forecast is undominated; and in~\cite[Example~6]{SSK09} a coherent forecast is dominated."

### 5.3 Conditional reports section

Current text:

> "Schervish, Seidenfeld and Kadane conjecture that restricting coherence to full conditional probabilities would call for a modified dominance criterion~\cite[Section~6]{SSK09}."

Replace with:

> "Schervish, Seidenfeld and Kadane allow arbitrary conditional forecasts given events of probability zero, and their equivalence uses strict dominance; under our dominance their coherent class violates coherent admissibility. For disjoint $A_1,A_2$ meeting $B\ne\Omega$, the forecasts $0.9$ and $0.7$ for $A_1$ and $A_2$ given $B$ are coherent in their sense~\cite[Section~6]{SSK09}, but under the Brier score the forecasts $0.6$ and $0.4$ dominate them: they do better at every world of $B$ and the same elsewhere. They conjecture that, if coherence is restricted to full conditional probabilities, a suitably modified dominance criterion is again equivalent to it~\cite[Section~6]{SSK09}."

The next sentence ("Proposition prop:blocks gives a result of this kind, with ordinary dominance, for a single finite partition") is accurate. Optionally append:

> "Finite block losses matter: with the logarithmic score a forecast from a full conditional probability can be dominated."

Optionally add a footnote with the §3.5 log-score example.

### 5.4 Introduction and bibliography

Introduction, current text:

> "The results recover theorems on proper scores of Pettigrew~\cite{Pettigrew}, Predd et al.~\cite{Predd} and Schervish, Seidenfeld and Kadane~\cite{SSK09}."

Replace with:

> "The results recover theorems on proper scores of Pettigrew~\cite{Pettigrew} and Predd et al.~\cite{Predd}, and, for continuous scores and unconditional forecasts, of Schervish, Seidenfeld and Kadane~\cite{SSK09}."

The bibliography entry for SSK09 is correct: TR 865's numbering matches every citation. No change is needed.

## Sources consulted

- ldg_full.tex (§§2–6, §8).
- Local SSK file (= TR 865), checked against https://www.stat.cmu.edu/tr/tr865/tr865.pdf.
- Predd et al. arXiv 0710.3183v1, via https://arxiv.org/pdf/0710.3183, https://ar5iv.arxiv.org/html/0710.3183 and https://www.alphaxiv.org/abs/0710.3183.md. The arXiv abstract page lists only v1, with DOI 10.1109/TIT.2009.2027573. The IEEE text was not accessible.
- Publication venue of SSK09: https://econpapers.repec.org/RePEc:inm:ordeca:v:6:y:2009:i:4:p:202-221.
