# REF79b: referee report on PS79, P79 and N79

Scripts are in `refb_code/` in this folder: `flat.py`, `ex4.py`, `ex4b.py` and `misc.py`. I read the texts of SSK, Pettigrew and Nielsen locally. For Predd et al. I used arXiv v1, through WebFetch summaries of arxiv.org/pdf/0710.3183, because ar5iv returned only the text up to §4 and direct download is blocked.

## Verdicts at a glance

| # | Claim | Verdict |
|---|---|---|
| 1a | (T) fails for the continuous merely proper score that is flat on [1/3, 2/3] | **CHECKED** |
| 1b | (A) fails for a merely proper score that is infinite somewhere in (0,1) | **CHECKED** (the mathematics). The framing needs correcting: see 1b |
| 1c | SSK Example 4: every incoherent forecast is dominated, so U_L = C | **WRONG**. The forecast (1/2, 3/10) is incoherent and undominated |
| 1c | SSK Example 4: (A) and (T) hold, (S) fails | CHECKED |
| 1c | SSK Example 5: (A) holds; (S) and (T) fail | CHECKED |
| 1c | SSK Example 6: (A) fails | CHECKED. SSK's text leaves g1(1/2) undefined; the claim needs g1(1/2) = 1/4 |
| 1d | (A) fails for SSK's coherence₁ conditional forecasts under Brier; also the one-pair version and the log-score full-conditional example | CHECKED |
| 1e | SSK numbering matches LDG's citations | CHECKED against the local file (TR 865 form). Published *Decis. Anal.* numbering: UNCLEAR |
| 2 | Gap in Pettigrew's proof of Theorem 1 with infinite losses (enhanced log score, c = (0, 0, 1/2, 1)) | CHECKED. The theorem itself is true |
| 2 | All four conditions hold for Pettigrew's whole class | CHECKED |
| 3 | The lifted SSK Example 2 satisfies thm:nielsen's hypotheses exactly, and no model strictly dominates the dominated credence | CHECKED |
| 3 | LDG's sentence "Whether strict dominance holds without local boundedness remains open" is false | CHECKED under the reading "under thm:nielsen's hypotheses", which is the natural one in context. Under Nielsen's own continuity it is open only for infinite Ω. Either way the sentence must change |
| 3 | Nielsen's Theorem 2 already dropped local boundedness | CHECKED (his note 27) |

---

## 1. PS79 (Predd et al.; SSK)

### 1a. (T) fails for a flat continuous proper score: CHECKED

The score is g1(x) = ∫_{[x,1)} (1−q) λ(dq) and g0(x) = ∫_{[0,x)} q λ(dq), where λ is Lebesgue measure on [0,1/3] ∪ [2/3,1].

- **Closed forms.** The closed forms in PS79 agree with numerical integration to within 1e-16 (`flat.py`).
- **Propriety.** ∂_y G_t(y) = (y − t)·1_{supp λ}(y). So G_t is nonincreasing on [0,t] and nondecreasing on [t,1], and t is a minimiser. A grid check gives max(G_t(t) − min G_t) = 0. This is also SSK's Theorem 4 representation, with λ σ-finite.
- **Continuity, finiteness, normalisation.** The score is continuous and finite, with g0(0) = g1(1) = 0. It is constant (= 1/18) on [1/3, 2/3].
- **The tie.** Take E_1 = E and E_2 = Ω∖E, with E ∉ {∅, Ω}. The forecasts (0.4, 0.4) and (0.4, 0.6) have identical profiles (1/9, 1/9). They agree in the first coordinate, and both second coordinates lie in the flat stretch.
- **Status of the two forecasts.** (0.4, 0.6) is coherent and lies in C_L, by the Lemma 5 argument in PS79 §3.2, which I checked. (0.4, 0.4) is incoherent.

So (T) fails. The incoherent forecast is undominated: a dominator of it would dominate (0.4, 0.6). So it is rationally permissible in any family that contains this ranking.

### 1b. (A) fails for merely proper scores that are infinite in (0,1): the mathematics is CHECKED; the framing needs correcting

**The example.** g0(x) = x/(1/2 − x) on [0, 1/2) and ∞ on [1/2, 1]; g1(x) = ∞ on [0, 1/2] and (1−x)/(x − 1/2) on (1/2, 1].
- Predd's Definition 2(b) defines continuity sequentially, with values in [0,∞]. The example meets it.
- It is merely proper: G_t ≡ ∞ for t ∈ (0,1), G_0 = g0 is minimised at 0, and G_1 = g1 is minimised at 1.
- Profiles: forecast 0.3 has (∞, 1.5) and forecast 0 has (∞, 0). So 0 dominates 0.3, and both forecasts are coherent when n = 1 (`misc.py`).

**Relation to Predd's hypotheses.** The example lies inside Predd's Definition 2 with uniqueness dropped. That is all §7.2.1 changes: codomain [0,∞] and continuity are kept. However:
- §7.2.1 also asserts that "Proposition 2 still holds", with φ no longer strictly convex.
- Proposition 2 concludes that φ(x) = −x s(1,x) − (1−x) s(0,x) is real-valued and bounded.
- §7.2.2's Proposition 4 asserts boundedness of φ for *every* proper s : {0,1}×[0,1] → [0,∞].

For any proper score infinite somewhere in (0,1), SSK Lemma 3 gives max{s(0,x), s(1,x)} = ∞ for every x. So φ = −∞ on (0,1). Hence:
- Predd's "Proposition 2 still holds" in §7.2.1, and Proposition 4 as stated, are **WRONG** for this subclass. Read with care, Predd's §7 tacitly presupposes SSK's Assumption 3. (I have this from a WebFetch summary of the arXiv PDF, not from verbatim text. Check it against the PDF before citing.)
- No claim of Predd's is contradicted by the (A) failure. Predd's §7.2.1 weak-dominance claim concerns incoherent forecasts and is vacuous here.

PS79 should therefore say: "inside Predd's Definition 2 without uniqueness, but outside the class for which Predd's own §7.2 assertions (φ bounded) are true". Saying only "allowed by Predd" is not enough.

**(S) in this example: CHECKED.** Theorem thm:finite applies with c_p = 1 if p_E ≥ 1/2, and c_p = 0 otherwise. The guarantee sets are (Δ, {δ_{E^c}}) or ({δ_E}, Δ), according to which loss of the rival is infinite.

Theorem bayes-finite cannot apply. PS79's connectedness argument is correct.

Also, and PS79 does not say this, **Corollary closed-choice fails for every assignment into C_L = {0, 1}**. Consider the comparison set against 0.3 at E^c, and the one against 0.7 at E. If both were closed, then {c_p = 0} and {c_p = 1} would be complementary nonempty closed sets: competitiveness at the vertices forces both values to occur. That contradicts the connectedness of Δ. So this is a second natural instance, beside ex:two-world, in which the weakening of closed-choice to thm:finite is genuinely needed.

### 1c. SSK Examples 4–6

**Example 4: "every incoherent forecast is dominated, U_L = C" is WRONG.**

PS79's argument fails on the quadrant x, y ≤ 1/2. There the Brier projection onto x + y = 1 leaves the quadrant unless x = y. The move (x+ε, y+ε) does work in that quadrant, but only when both coordinates are < 1/2. The boundary forecasts (1/2, y) and (y, 1/2) are not covered.

Counterexample (PROVED). Take f = (1/2, 3/10). It is incoherent, with profile (0.84, 1.24). Suppose g dominates f. Check the four quadrants of g:
- *x, y ≤ 1/2:* L1 ≤ 0.84 means (1−x)² + y² ≤ 0.34. Since x ≤ 1/2, (1−x)² ≥ 1/4, so y ≤ 0.3. Summing the two constraints gives [(1−x)² + x²] + [y² + (1−y)²] ≤ 1.08. With x ≤ 1/2 and y ≤ 0.3, the left side is ≥ 0.5 + 0.58 = 1.08, with equality only at (1/2, 0.3).
- *x > 1/2 ≥ y:* L2 = 1 + x² + (1−y)² > 1.5 > 1.24.
- *x ≤ 1/2 < y:* L1 = 1 + (1−x)² + y² > 1.5 > 0.84.
- *x, y > 1/2:* L1 ≤ 0.84 forces x > 0.7. The same sum then exceeds 0.58 + 0.5 = 1.08.

So f is undominated. A grid search (`ex4.py`, `ex4b.py`) agrees. It also finds (1/2, y) undominated for y from about 0.135 up to 1/2, and symmetrically (y, 1/2).

Consequences:
- For the family {L}, the conclusion of thm:argument genuinely fails. Example 4 does **not** show that "LDG's conditions are sufficient but not necessary".
- Delete that sentence and the U_L = C claim from PS79 §3.4.
- The table entry should read: (A) holds, (S) fails, (T) holds, U_L ≠ C.
- The optional LDG sentence (g) may be strengthened: "…in [Example 4] selection fails, and indeed the incoherent forecast (1/2, 3/10) is undominated."
- (A) and (T) do hold: the score is strictly proper with V finite, so a weak dominator of c_p is c_p. **(S) FAILS**, since (S) implies the dominance property and (0.6, 0.7) has no coherent weak dominator. Both CHECKED.

**Example 5: CHECKED.**
- (0.5, 0.7) has profile (1.75, 0.25), with worlds ordered (A1, A1^c). Its expected loss under (1/2, 1/2) is 1 = V(1/2), so it is undominated. No coherent forecast has its profile, so **(S) FAILS**.
- (0, 1) and (0, 0.7) both have profile (2.5, 0), and (0, 1) ∈ C_L. So **(T) FAILS**.
- (A) HOLDS: interior c_p are undominated through the expected-loss argument, and the endpoints are undominated directly.

**Example 6: CHECKED, with one caveat.**
- (1/2, 1/2, 1/2) is coherent (R(C1) = R(C4) = 1/2) and scores 1 at all four constituents. (0, 0, 0) scores (1, 1/2, 1/2, 1). So **(A) FAILS** for {L}.
- Caveat: SSK define g1 only for x < 1/2 and x > 1/2. Their totals d_j = 1 require g1(1/2) = 1/4. Say so if the example is cited.

### 1d. Conditional forecasts: CHECKED

- **The (0.9, 0.7) example.** (0.9, 0.7) for (A1|B), (A2|B) is coherent₁: take R(B) = 0, which B ≠ Ω allows. SSK say this explicitly in §6. On (A1∩B, A2∩B, B∖(A1∪A2), B^c), its Brier profile is (0.5, 0.9, 1.3, 0), and (0.6, 0.4) has (0.32, 0.72, 0.52, 0) (`misc.py`). In translation T2 only L_𝒜 evaluates this model, so (A) fails.
- **The one-pair version.** (A∩B = ∅, P = 0.9, dominated by 0): CHECKED.
- **The log-score full-conditional example.** P = (0, 1/2) has profile (0, ∞, ln 2), and Q = (0, 0) has profile (0, ∞, 0). Q comes from the full conditional probability with μ(·|Ω) = δ_1 and μ(·|B) = δ_3. CHECKED.
- I did not check PS79's layer-induction proof for finite-valued scores or its claim about a gap in SSK's Lemma 12.

### 1e. Numbering: CHECKED against the local file

The local file is headed "Submitted to the Annals of Statistics", imsart, July 17, 2008. In it:
- Theorem 2 (Conclusions 1–3 listed in §3.3), Lemma 3, Lemma 5, Example 2 (the A2 rule g1 = x − log x), Example 4, and §6 "Discussion" with the coherent₁ (0.9, 0.7) remark and the conjecture all match LDG's uses.
- LDG's bibliography entry already says that the numbers refer to TR 865.
- I did not re-verify that the local file *is* TR 865, nor the published *Decis. Anal.* numbering: UNCLEAR.

---

## 2. P79 (Pettigrew 2022)

**The setting is confirmed from the PDF image (p. 132).**
- I : C × W → [0,∞], with a closed bracket at ∞.
- Continuity: "I(c,i) is a continuous function of c".
- Strict propriety: unique minimiser over all of C.
- p. 135 says the arguments "go through for … the Brier and enhanced log scores".

So infinite values are squarely inside his class.

**The gap: CHECKED.**
- Take W = {w1, w2} and c = (c(∅), c({1}), c({2}), c(W)) = (0, 0, 1/2, 1). Then L*(c,1) = ∞ and L*(c,2) = 1.5 + ln 2 ≈ 2.193.
- For x ∈ P with x_1 > 0, D(x,c) = ∞ − (finite) = ∞. Also D(δ2, c) = 2.193 − 2 ≈ 0.193. So Lemma 5's unique minimiser is δ2, and L*(δ2, 1) = ∞ = L*(c, 1).
- The proof of Theorem 1 infers D(w¹,c) > D(w¹,c*) from ∞ ≥ ∞ + 0.193, which is invalid.
- Lemma 5(ii) is undefined at q = δ2, since its i = 1 term is p_1(∞ − ∞).
- **An additional point.** Lemma 4(ii) uses I(w^i, i) = 0, which fails for L*: L*(w^i, i) = 2. This is harmless when the value is finite, as P79 says.

**The theorem is true: CHECKED.**
- p_ε = (ε, 1−ε) has L*(p_ε, 2) = 2 − ln(1−ε) < 2.193 for ε < 1 − e^{−0.193} ≈ 0.176, and L*(p_ε, 1) < ∞.
- In general, prop:proper's last claim through prop:strict(b) applies. I checked that prop:strict(b)'s proof works with continuity into [0,∞]: it uses continuity only at worlds in supp p, where losses are finite, and terms off the support vanish because L(c_q, ·) is finite for interior q.

**All four conditions for the whole class: CHECKED.**
- **Finiteness.** Strict propriety with |C| > 1 forces p·I(p) < ∞, reading 0·∞ = 0. That reading is needed even to make L*(p, i) finite, because of the c(∅) = 0 terms.
- **(A) and (T).** A weak dominator of p, or a model tied with p, is a Bayes model for p, so it equals p.
- **(S).** Use thm:bayes-finite with c_p = p. Continuity into [0,∞] composed with the embedding Δ → C gives lower semicontinuity.
- **(E).** Trivial.
- **No subclass fails.** P79's Theorem 2 aside, where (A) fails for an infinite-valued I and A = {(t, 1−t) : 0 < t ≤ 1/2}: CHECKED. P79's suggested text is accurate. I did not check its LSE remark.

---

## 3. N79 (Nielsen 2023)

**The lifted example meets thm:nielsen's hypotheses exactly: CHECKED.**
- Ω = {1, 2}, M_L = [0,1]^{2^Ω}, and C = {(0, t, 1−t, 1)}. The loss is L(c,1) = (1−a)² + g0(b) + e² + (1−W)² and L(c,2) = a² + g1(b) + e² + (1−W)², with values in [0,∞].
- **Quasi-strict propriety (indeed strict propriety).** E_q is the support sum; Nielsen's sup definition gives 0·∞ = 0. E_q L(m) splits into three parts, each uniquely minimised at q, as computed in ex:ssk-sharp. V is finite.
- **Lower semicontinuity.** q ↦ L(q,1) = (1−t)² + g0(1−t) drops from 1 to 0 at δ1, which lower semicontinuity allows. q ↦ L(q,2) is continuous into [0,∞].
- **Local boundedness fails**, since L(δ1, 2) = ∞.
- **The dominated credence.** m = (0, 1/2, 0, 1) is incoherent with profile (1/4, ∞), and δ1 dominates it. L(c', 1) < 1/4 forces b' = 0, hence L(c', 2) = ∞. So nothing strictly dominates m.

**On the sentence.**
- The example violates Nielsen's own continuity on P: E_{δ1} L(·) = L(·, 1) jumps at δ1. So it does not answer Nielsen's §4.2.1 question; N79 says this correctly.
- Under thm:nielsen's hypotheses, which the preceding clause of LDG's sentence is about, the sentence is **WRONG**. It is even refuted by LDG's own ex:ssk-sharp, of which this is a relabelling.
- Under Nielsen's continuity with finite Ω, prop:strict(b) gives uniform dominance without local boundedness (CHECKED), so the question is not open there either.
- It remains open only for infinite Ω under continuity.
- N79's replacement C is correct.

A shorter alternative replacement:

> "Without local boundedness strict dominance can fail under the hypotheses of Theorem~\ref{thm:nielsen}: Example~\ref{ex:ssk-sharp}, with $f=(c(\{1\}),c(\{2\}))$ and $c(\varnothing)^2+(1-c(\Omega))^2$ added at each world, is quasi-strictly proper and lower semicontinuous along $\C$, and $(0,\frac12,0,1)$ is dominated but not strictly dominated. Under Nielsen's continuity and finite $\Omega$, Proposition~\ref{prop:strict}(b) gives uniform dominance; for infinite $\Omega$ the question remains open."

**Nielsen's Theorem 2: CHECKED.** Note 27 reads: "local boundedness on P is not used. So Theorem 2 continues to hold under the weaker assumption that J is quasi-strictly proper and continuous on P." This is about coherent models being undominated. The new content in LDG is that incoherent models are dominated without local boundedness. N79 states this correctly.

**Not checked:** N79's claim that Nielsen's proof already yields uniform dominance (his eq. (9)), and its suggested lemma credits (F).

---

## Corrections required

1. **PS79 §3.4, SSK Example 4.** Delete "every incoherent forecast is dominated … U_L = C … sufficient but not necessary". Replace it with: the incoherent forecast (1/2, 3/10) is undominated; the conclusion fails for {L}.
2. **PS79 §3.3.** Reframe the subclass as lying within Predd's Definition 2 without uniqueness, but contrary to Predd's §7.2 assertion that φ stays bounded. Predd's Proposition 4 and the "Proposition 2 still holds" remark are false for these scores, which shows that they tacitly need Assumption 3. Optionally add that closed-choice also fails there, so that thm:finite is needed.
3. **PS79 Example 6.** Note SSK's undefined g1(1/2), which must be read as 1/4.
4. **LDG line 704.** Replace "Whether strict dominance holds without local boundedness remains open" as above or as in N79's text C.
5. **P79.** No corrections. Optionally note that Lemma 4(ii) also fails for L*, harmlessly.
