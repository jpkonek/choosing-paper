# KK1 (round 39, BRIEF31). Referee report on the two impossibility proofs for protected weak-additive designs (JJ3 and JJ2)

18 Oct 2026. Rules of BRIEF13 and BRIEF31; the corrections of AUDIT_JJ.md are adopted. Labels:
- **PROVED**: the argument is written or re-derived here. I am the second reader of each JJ step marked PROVED below.
- **CHECKED**: an exact computation with a stated script, or a reading of a recorded result whose imports keep their recorded status.
- **CONJECTURE**: none offered.
- **NUMERICS**: none used.

No assumption is added. Each hypothesis below is a hypothesis of the result being refereed, or of a named import.

Script: `kk1py/checks.py`. Run `python3 -I checks.py` inside `kk1py/`; the output is `kk1py/checks.out`. All arithmetic is `fractions.Fraction`. The script has 0 failures. No verdict rests on it; it re-checks algebra that is proved below.

**What I read.**
- BRIEF31, AUDIT_JJ, BRIEF30, BRIEF13.
- JJ1_referee (whole), JJ2_notes (whole), JJ3_notes (whole).
- The write-up, §2 (setting, Theorem kkm, (LF)), §3 (Prop necessary, ccibu, Cor realisation), §4 (main chain), §5 (general domains: N_0, raytransfer, B1, TS, cuts, availability, TSalways, walls, apex, vertexfree, CF) and §6 (Theorem gm, inputs, the three routes, the short route, Table gmdeps).
- For the bypass questions, the following sources:
  - N21 Thm N21.6 (proof, Steps 1–7) and Cor N21.7;
  - R1 Lemmas 1.3–1.5, Thm 2.2, Props 2.1 and 2.8;
  - II1 Prop 3.1;
  - the standing-hypothesis paragraphs of N28, I2, PropD and C1.
- A keyword search, over 25 source files of the gm chain, for every invocation of (LA), (S), (C), competitiveness, Theorem kkm and R1 Lemmas 1.3–1.5 (§4.3).

---

## 0. Verdict

**JJ3 is correct, with one repair (Lemma 4.2, step 6).** The audit's repair works, and I write it out with the Fubini step in full (§2.7). Every other step of Thm 2.1, Prop 2.5, Lemmas 3.1, 3.2, 4.2, 4.3, 4.4, Thm 4.1 and Thm 5.1 holds as written.

**JJ2 is correct in everything the main theorem uses.** Its two small faults are in results that the main theorem does not need.
- Thm 3.4 needs a wording repair: "relint" must exclude singletons.
- The implication (b) ⇒ (a) in Cor 5.6 has a gap.

**S8a and S8b are correct (PROVED).** S8b needs a sharper justification of Step 3 of the cut theorem than JJ2 gives in S8c (§3.7).

**The ccibu bypass is genuine, and it is available to both notes.** The routes of Theorem gm use a cover only through:
- (BU) at every interior weight;
- T1 interior-Bayes;
- strict guidance (or, in JJ2's audit, strict-best plus weak guidance);
- (LF).

Vertex coherence and boundary coherent Bayes models follow from these (§4.2, PROVED). The reading that the chain needs nothing more is CHECKED, by its standing hypotheses and by an exhaustive keyword search of its sources (§4.3). It is not a re-derivation of the chain.

On that reading, JJ3's Theorem 5.1 needs no ccibu. JJ3's lowered field Φ′ is strictly guiding and has exactly these properties, so gm's proof applies to it directly. JJ2's Theorems 7.2 and 7.4 need no ccibu either.

**Domains.**
- JJ2's direct route (Thms 7.2, 7.4) uses the full domain. It needs both acceptances in the advice range of a.e. mixed pair, which is more than (Av).
- JJ3's route needs exactly (LF) + (Av). (Av) is used at exactly one place, Lemma 4.2 step 3.

| Item | Verdict |
|---|---|
| JJ3 Lemma 1.1, Remark 1.2 | correct |
| JJ3 Lemma 2.2, **Thm 2.1** | correct |
| JJ3 Lemma 2.3, Lemma 2.4 | correct |
| JJ3 **Prop 2.5** | correct (imports II1 Prop 3.1(a), CHECKED reading) |
| JJ3 **Lemma 3.1** | correct; CHECKED independently in part, via (A) |
| JJ3 **Lemma 3.2 (removal)**, Prop 3.3 | correct |
| JJ3 **Lemma 4.2** | **correct with repair** (step 6; §2.7) |
| JJ3 Lemma 4.3, Lemma 4.4 | correct |
| JJ3 **Thm 4.1** | correct, given repaired 4.2 |
| JJ3 **Thm 5.1** | correct modulo gm and ccibu as written; **ccibu removable** (§4) |
| JJ3 Remark 5.3 | correct |
| JJ2 **Thm 3.4** | **correct with repair** (relint convention; §3.1). Not used downstream |
| JJ2 **Lemma 4.1** | correct (independent proof of JJ3 Thm 2.1) |
| JJ2 **Lemma 4.3** | correct (same as JJ3 Prop 2.5; full domain) |
| JJ2 Lemma 5.2, **Prop 5.3 (rotation)**, Prop 5.4 | correct; the two-orientation use of 5.3 CHECKED (E) |
| JJ2 Thm 5.5 | correct; its second proof is the ccibu bypass of §4 |
| JJ2 Cor 5.6 | (a), (c) correct; **(b) ⇒ (a) has a gap** (§3.6). A side result |
| JJ2 Table 7.2, **S8a** | correct (PROVED; CHECKED (D)) |
| JJ2 Table 7.2, **S8b** | correct (PROVED; CHECKED (C)) |
| JJ2 Table 7.2, S8c | conclusion correct; its stated justification needs replacing (§3.7) |
| JJ2 Table 7.2, other rows | not re-derived (one reader: JJ2) |
| JJ2 "a cover is used only through (W1)–(W6)" | CHECKED (§4.3); for strictly guiding fields it reduces to the family form of gm |
| JJ2 Thms 7.2, 7.4 | avoid ccibu: **yes**. Need (Av) only? **No**: they use the full domain |

---

## 1. Common setting

Notation is that of JJ3 §1. A mixed pair is indexed by its majority orientation h, with positive worlds j, l and odd world o. Advices are M (accept h), S, O (accept −h) and ×.
- c = φ(S) − φ(M);
- c′ = φ(S) − φ(O);
- d = c − c′ = φ(O) − φ(M).

JJ2 writes c^g, c^{−g}, d^g for the same objects in either orientation. At w ∈ Δ, with × never minimal:
- M is the unique minimiser iff c·w > 0 and d·w > 0;
- O is the unique minimiser iff c′·w > 0 and d·w < 0;
- S is a weak minimiser iff c·w ≤ 0 and c′·w ≤ 0.

The weak minimiser set is therefore a function of the three signs of c·w, c′·w and d·w, zero included. Several proofs below use this fact.

---

## 2. JJ3, step by step

### 2.1 Lemma 1.1 and Remark 1.2. Correct (PROVED)

**(a) Strict-best.**
- B^k is the pointwise world-k-best evaluable advice. It is evaluable (Remark advicerange), and by weak guidance it minimises Φ_k.
- (NT) at e_k makes C_{e_k} the unique Φ_k-minimiser, so B^k = C_{e_k}. In particular B^k is coherent.
- Suppose a tie φ_k(h, b) = φ_k(h, best_k(h)) held on a non-null measurable set with b ∈ A(h). Switching B^k to b there gives a second minimiser, which is evaluable because the domain is decomposable. Contradiction.

**(b) × strictly worst, without loss.**
- φ_k(h, ×) is replaced by max_{a ≠ ×} φ_k(h, a) + |h_k|. This is measurable, integrable and weakly guiding.
- Coherent models never give ×: P_K(−g) ≤ −P_K(g) for every g. So Φ(C_p) is unchanged.
- Φ′ ≥ Φ pointwise, so (NT) transfers.
- A remaining equality at world k involves neither best_k nor ×. So it is S = W_k, and it requires {M, S, O} ⊆ A(h). If best_k is not available, the best available advice is strictly cheapest by (a), and no two of the remaining advices can be equal.

The signs of c, c′, d follow:
- c_j, c_l > 0 ≥ c_o;
- c′_o > 0 ≥ c′_j, c′_l;
- d_j, d_l > 0 > d_o.

Remark 1.2 is the two switching arguments, and it is correct.

### 2.2 Lemma 2.2 and Theorem 2.1. Correct (PROVED); referee priority 4

**Lemma 2.2.** The leading ranking with the given selection satisfies (LA) and (S).
- Undominatedness and competitiveness on supp p come from (NT).
- Closedness: |Φ_i(C_p) − Φ_i(C_q)| ≤ 2∫_{D(p,q)} E, where D(p, q) is the set of pairs on which C_p and C_q advise differently, and μ(D(p, q)) ≤ μ(C_p △ C_q).

Theorem kkm (valid for preorders) then gives the conclusion.

**Theorem 2.1, step 1.** Let B be w-Bayes, with w interior. A pointwise minimiser minimises w·Φ over M, because Φ is additive and M is decomposable. Hence B is undominated, since w has full support.
- Lemma 2.2 gives Φ_i(B) = Φ_i(C_p) for all i, and in particular for i ∈ supp p.
- (NT) at p then gives B = C_p a.e.

So priority 4 is fine: a tie at all three worlds gives the weak inequalities on supp p, which is exactly the antecedent of (NT).

**Step 2 (null ties).**
- The two pointwise minimisers B_1, B_2 are chosen measurably to differ at every point of T_w.
- The splice X = (B_1 ∩ A) ∪ (B_2 ∖ A), with A = {‖h‖ < 1}, is a pointwise minimiser. So X is coherent by step 1: X = D_K.
- D_K, D_{K_1}, D_{K_2} are exact cones: P_K(th) = tP_K(h).
- Let N be the union of the three null sets where X ≠ D_K and B_r ≠ D_{K_r}. The set {(h, t) : th ∈ N} is null for the product measure, since each t-section is t^{−1}N.
- So for a.e. (h, t) with h ∈ G ∩ A and t > 1/‖h‖:
  - advice of D_K at h = advice of B_1 at h = advice of D_{K_1} at h;
  - advice of D_K at th = advice of B_2 at th = advice of D_{K_2} at h;
  - and these differ on G.
- This set of (h, t) has positive measure. Contradiction.

**JJ2 Lemma 4.1, step 3** is an independent proof of the same fact, and it is also correct. A cone that is contained, modulo null sets, in {|h| < R} is null, because dilations of a non-null set are non-null.

### 2.3 Lemmas 2.3 and 2.4. Correct (PROVED)

**Lemma 2.3(a).** Off the null set T_w, the strict minimiser at w stays strict near w, since there are finitely many advices and the values are affine in the weight. This gives convergence in measure.
- Every Hausdorff cluster K′ of K_{w_n} has D_{K_{w_n}} → D_{K′} pointwise off the null set ±∂D_{K′}.
- Injectivity of K ↦ D_K then gives K′ = K_w.

**Lemma 2.3(b)** is the same argument at a boundary weight w₀ with an a.e. unique minimiser.

**Lemma 2.4(a), convexity for every gamble.** This is the key new device, and the proof is right.
- P(q_r, ·) is 1-Lipschitz in the sup norm, so P(q_r, ·) > 0 on a ball U around x.
- Theorem 2.1 holds at the three fixed weights q_1, q_2, q. So for a.e. x″ ∈ U: q_1, q_2 ∈ R(x″) ⟹ q ∈ R(x″) ⟹ P(q, x″) > 0.
- Here R(x″) is an intersection of open half-planes, so it is convex whatever the signs of the penalties.
- Density and continuity give P(q, ·) ≥ 0 on U, and the level shift gives P(q, x) > 0.

**Lemma 2.4(b).**
- Joint measurability holds.
- The x-sections are null: by Theorem 2.1 for the first set, and for the second because P(w, x + t𝟙) = P(w, x) + t, so the zero set of P(w, ·) is a graph over 𝟙^⊥.
- Fubini applies.
- Two open convex sets that agree a.e. are equal, since int cl O = O for an open convex O.

**Lemma 2.4(c).** Let z ∈ C ∖ cl O. The open set (1 − s)z + sB lies in C, misses O, and has P = 0 on it, against (b). So Z(x) ⊆ (cl O ∖ O) ∩ int Δ, which lies on the finitely many lines {w : w·(φ(x, b) − φ(x, acc)) = 0}.

### 2.4 Proposition 2.5. Correct (PROVED; import CHECKED)

**Step 1** is II1 Prop 3.1(a), which I read.
- By Lyapunov (II2 Lemma 1.1(a); JJ1 §2.1), the leading increments out of T1 = C_{q₀} over supp q₀ form a convex set.
- Competitiveness of C_{q₀}, which comes from (NT), keeps this set out of the open negative orthant.
- Separation then gives a weight α, and pointwise switching gives pointwise weak α-optimality.

**Step 2.** Take h = (1, 1, −t). Then P_{T1}(h) = 2c₀ − t(c₀ + ε), which is < 0 for t slightly above 2c₀/(c₀ + ε). Also P_{T1}(−h) = −(c₀(2 − t) + ε) < 0. So T1 is silent on an open set O′ just outside cl D_{T1}.
- (LF) makes D_{T1} ∪ O′ evaluable, so M ∈ A(h) on O′.
- By strict-best (M is best at worlds 1 and 2, and both M and S are available), α·c = α_1c_1 + α_2c_2 > 0 for every α ∈ Δ_{12}.
- So T1 is not weakly α-Bayes on the non-null set O′.

This argument also shows that supp q₀ = Ω. Theorem 2.1 then gives T1 = B_α. Here (LF) is used, and (Av) is not.

### 2.5 Lemma 3.1. Correct (PROVED; CHECKED (A))

I re-derived every case.

**(a)**
- Unanimous pair: f_M < f_S on Δ.
- z_o: {c ≤ 0} ∩ Δ = {e_o}, and c′·e_o > 0.
- z_j together with z_l: {c′ ≤ 0} ∩ Δ is the edge {w_o = 0}, where c > 0.

**(b)** With c_o < 0 < c_j, c_l and c′ = (0, c′_l, c′_o), c′_l < 0 < c′_o:
- {c ≤ 0} ∩ Δ = co{e_o, a, b};
- c′(a) > 0 and c′(e_o) > 0;
- the three sub-cases of the sign of c′(b) give ∅, {b}, or the triangle (m_h = b, s_h, t_h).

The formulas m_h = c_l/(c_l + |c_o|) and s_h = |c′_l|/(|c′_l| + c′_o) hold in the edge parameter t (the o-coordinate). §2.7 strengthens the lemma's last sentence from "near s_h" to the whole edge.

### 2.6 Lemma 3.2 and Proposition 3.3. Correct (PROVED); referee priority 5

**G and its zeros.**
- S is a weak minimiser iff G ≥ 0. The perturbed function is G_δ = G + δσ_Z, and f_M, f_O, f_× are unchanged.
- Non-essential means G < 0 on int Δ.
- On the closed simplex, G vanishes only on Σ(h): this is empty in case (a) and lies in {w_j = 0} in case (b1), where Z = {j}. So G vanishes only where σ_Z = 0, as priority 5 asks.

**Choice of δ.** Some cell vertex has σ_Z > 0 (e_j, or a vertex of Δ carrying a zero world). So the minimum −G(v)/σ_Z(v) over vertices with σ_Z(v) > 0 is finite and positive.
- Affinity on each of the two cells gives G + 2δσ_Z ≤ 0 on Δ.
- Hence G_δ ≤ −δσ_Z < 0 wherever σ_Z > 0, and G_δ = G wherever σ_Z = 0.

**Conclusion.**
- S is never a weak minimiser where anything changed, and M, O are untouched. So the minimiser sets are unchanged at **every** w ∈ Δ.
- The cap at half the gap gives best_i < S < W_i, so the field is strictly guiding.
- δ is measurable and at most E.

**Prop 3.3** follows.

### 2.7 Lemma 4.2. Correct with repair (PROVED; CHECKED (A)); referee priority 1

**Steps 1–4 are correct.**
- **Step 1.** On the edge {w_j = 0}, two distinct advices are never blind at both l and o:
  - if l and o are both positive for h, the best available advice is the same at l and o and strictly cheapest at both;
  - if exactly one of them is positive, a blind pair would need to be {S, O} (the zero at the positive world) and {S, M} (the zero at the odd world) at once;
  - × is strictly worst.

  So each pair has finitely many tie weights on the edge. Tonelli shows that T₀ := {t : the w₀(t)-tie set is null} is measurable and co-null.
- **Step 2** is Lemma 2.3(b).
- **Step 3 (confinement)** is the only use of (Av_{l,o}):
  - for a.e. g with g_l, g_o > 0, acceptance is available by (Av_{l,o});
  - it is strictly best at both l and o, so it is the unique w₀(t)-minimiser;
  - hence D_{K₀(t)} accepts a.e. such g, and K₀(t) ⊆ Δ_{lo} (test gambles near (−N, 1, 1)).
- **Step 4.** For m = (0, 1 − x, x), m·h̄ = π − x. Hence:
  - D_{K₀(t)} gives O at h iff α(t) > π(h);
  - it gives M iff β(t) < π(h);
  - it is silent otherwise.

**The gap (as stated by the audit).** Step 6 sets t₀ := max(m_h, m_{h′}) and asserts s_h, s_{h′} > t₀. From m_h < s_h and m_{h′} < s_{h′} this does not follow. The inequality m_{h′} < s_h is not implied.

`checks.py` (A′) exhibits two essential pair configurations:
- m_h = 1/5, s_h = 3/10;
- m_{h′} = 2/5, s_{h′} = 3/5.

Here t₀ = 2/5 > s_h. This refutes only the inference, not the lemma. Comparing the truncated intervals (s_h, 1) ∩ (t₀, 1) gives nothing when both s ≤ t₀.

**Repair, part 1: the pair's minimiser on the WHOLE opposite edge (PROVED).** Let h be essential (case (b2)), and parametrise the edge by w₀(t) = (1 − t)e_l + te_o, t ∈ [0, 1]. Along the edge:
- c(t) := c·w₀(t) = c_l(1 − t) + c_o t is strictly decreasing (c_l > 0 > c_o), with its zero at m_h;
- c′(t) = c′_l(1 − t) + c′_o t is strictly increasing (c′_l < 0 < c′_o), with its zero at s_h;
- d(t) = c(t) − c′(t) is strictly decreasing.

Case (b2) means m_h < s_h. Therefore:
- on (0, m_h): c > 0 and c′ < 0, so d > 0, and **M** is the unique minimiser;
- at m_h: c = 0 > c′, so M and S tie;
- on (m_h, s_h): c < 0 and c′ < 0, so **S** is the unique minimiser;
- at s_h: c < 0 = c′, so S and O tie;
- on (s_h, 1]: c′ > 0 and c < 0 (since t > s_h > m_h), so d < 0, and **O** is the unique minimiser.

So the set of t at which O is the pair's unique edge minimiser is exactly (s_h, 1]. This matches the audit's argument: c′ > 0 exactly for t > s_h; c(s_h) < 0 gives d(s_h) < 0; d(1) = d_o < 0; and linearity gives d < 0 on [s_h, 1]. For t < s_h, c′ < 0 prevents O from being a minimiser.

`checks.py` (A) tests 3000 random exact essential pairs at every breakpoint and every midpoint of the edge arrangement (a complete test), with 0 failures.

**Repair, part 2: Fubini without truncation (PROVED).** This addresses referee priority 1 in full.
1. **Measurability of the edge family.** Put w_n(t) := (1/n)e_j + (1 − 1/n)w₀(t), which is interior. The map t ↦ K_{w_n(t)} is Hausdorff-continuous (Lemma 2.3(a)). So α_n(t) := min{m_o : m ∈ K_{w_n(t)}} is continuous. On T₀, K_{w_n(t)} → K₀(t) in the Hausdorff metric (Lemma 2.3(b)), and a linear minimum is Hausdorff-continuous, so α_n(t) → α(t). Hence α is Borel on T₀.
2. **The two sets.** Put
   - F := {(t, h) ∈ T₀ × E^{j}_{l,o} : O is the unique w₀(t)-minimiser of φ(h, ·)};
   - F′ := {(t, h) ∈ T₀ × E^{j}_{l,o} : α(t) > π(h)}.

   Both are Borel: the penalties are measurable in h and affine in t, and α and π are Borel.
3. **Null h-sections.** Fix t ∈ T₀. The w₀(t)-minimiser model is a.e. unique and equals D_{K₀(t)} a.e. (Lemma 2.3(b)). By step 4, D_{K₀(t)} gives O at h iff α(t) > π(h). So the h-section of F △ F′ is null for every t ∈ T₀.
4. **Tonelli.** By Tonelli, for a.e. h ∈ E^{j}_{l,o}, the t-section of F △ F′ is null. Call this co-null set G_C ∩ E^{j}_{l,o}.
5. **Identification.** For h ∈ G_C ∩ E^{j}_{l,o}, part 1 gives F_h = (s_h, 1) ∩ T₀. Hence (s_h, 1) =_{a.e.} {t : α(t) > π(h)}.
6. **Conclusion.** If h, h′ ∈ G_C ∩ E^{j}_{l,o} have π(h) = π(h′), the right-hand sides coincide. So (s_h, 1) =_{a.e.} (s_{h′}, 1), and therefore s_h = s_{h′}. ∎

No truncation is needed. By-product: for a.e. π₀ attained by essential pairs, the superlevel set {α > π₀} is a.e. a terminal interval of the edge.

**Statement to insert** (replacing step 5 and step 6):
> *5′. For h ∈ E^{j}_{l,o}, the unique minimiser of w₀(t)·φ(h,·) is M on (0,m_h), S on (m_h,s_h) and O on (s_h,1], because c(t) decreases through 0 at m_h, c′(t) increases through 0 at s_h, and m_h<s_h. 6′. With F, F′ as above (α Borel as the limit of the continuous α_n), F △ F′ has null h-sections for every t∈T₀, hence null t-sections for a.e. h; for such h, (s_h,1) =_{a.e.} {α>π(h)}; so s_h depends only on π(h).*

### 2.8 Lemma 4.3. Correct (PROVED); referee priority 2

**Step 1.** L_{h_1} = L_{h_2}, the line through e_j and the common s. Both σ_{h_r} are open segments of L ending at s, so σ = σ_{h_1} ∩ σ_{h_2} is a non-empty open segment inside int Δ.

**Step 2 (priority 2).** Fix w ∈ σ.
- c′·w = 0, so O is not the unique minimiser at w, and w ∉ R(−h_r).
- Since h_r ∈ G_B, Lemma 2.4(b) for −h_r gives P(w, −h_r) ≤ 0.
- c·w < 0 is an open condition, so interior points w′ near w with c′·w′ > 0 have d·w′ < 0. They therefore lie in R(−h_r), where P > 0.
- Continuity gives P(w, −h_r) = 0.

This uses exactly the two facts that the priority names.

**Step 3.** f is convex and nondecreasing, with f(ρ_1) = f(ρ_2) = 0. Monotonicity alone gives f ≡ 0 on [ρ_1, ρ_2]. Danskin's formula for the right derivative then forces every maximiser m at ρ_1 to have m_j = 0, so the maximiser is P_{π₀}.

**Step 4.** m·y(a) ≥ m_j(a + ρ_1) ≥ 0 and P_{π₀}·y(a) = 0, so P(w, y(a)) = 0.

### 2.9 Lemma 4.4. Correct (PROVED)

v_k·y(a) = c₀(a + 1 − 2π₀) + εy(a)_k ≥ c₀(a + 1 − 2π₀) − επ₀ > c₀(a − 1) − ε > 0.

### 2.10 Theorem 4.1. Correct (PROVED; Jacobians CHECKED (B)); referee priority 3

**Step 1.** Both parametrisations have Jacobian λ². I computed both determinants by hand, and `checks.py` (B) confirms them exactly at 2000 rational points each. So null sets correspond in both directions.
- Π is measurable (Tonelli) and has positive length.
- A section of positive area meets two distinct values of ρ.

**Step 2.** Y is non-null. P(w, y) = 0 on σ(π₀) by homogeneity. The choice of σ(π₀) for each π₀ needs no measurability, because only one y is used.

**Step 3 (priority 3).** y is chosen outside the null sets of Lemma 2.4(b), Lemma 2.4(c) and Lemma 1.1(a). These are three null sets, so their union is null, and Y is non-null.
- T1 accepts every y ∈ Y (Lemma 4.4). Since T1 ∈ M, M ∈ A(y) for a.e. y.
- P(w*, y) = P_{T1}(y) > 0 gives w* ∈ R(y) ≠ ∅.
- best_j(y) = M, and strict-best gives a positive j-coordinate for every normal φ(y, b) − φ(y, M). So no line ℓ_b passes through e_j; lines with normal ∝ 𝟙 are empty, and the zero normal is impossible.

**Step 4.** A non-degenerate segment covered by finitely many lines lies on one of them, so L(π₀) = ℓ_b ∋ e_j. Contradiction.

### 2.11 Theorem 5.1 and Remark 5.3. Correct, modulo the stated imports (PROVED)

**Step 1** assembles Lemma 1.1(b), Thm 4.1 and Prop 3.3. Φ′ is integrable and strictly guiding, and it has the same minimiser sets as Φ at every w ∈ Δ.

**Step 2, as written,** uses ccibu to give (LA), (S), (C) for Φ′, and then Theorem gm. That is correct at the status of ccibu. §4 shows that ccibu can be dropped.

**Remark 5.3 (PROVED).** Lemma 1.1(b) preserves (i)–(iii), because Φ′ ≥ Φ with equality on coherent models:
- a model weakly better than C_p everywhere is either tied with it (so equal, by (ii)) or dominates it (excluded by (i));
- a Φ′_k-minimiser is a Φ_k-minimiser.

The rest uses only (i)–(iii).

### 2.12 Where (Av), (LF) and ccibu enter JJ3

- **(Av_{l,o}):** only in Lemma 4.2 step 3 (confinement K₀(t) ⊆ Δ_{lo}). Through Lemma 4.2 it reaches Lemma 4.3 step 1 and Thm 4.1. Nothing else uses it.
- **(LF):** in Prop 2.5 step 2, availability of M near ∂D_{T1}.
- **T1 ∈ M:** in Thm 4.1 step 3, availability of M on Y.
- **Splice closure:** in Thm 2.1 step 2, and in Remark advicerange for B^k and the switches.
- **ccibu:** only in Thm 5.1 step 2. It is removable (§4).

So JJ3 §7 is right that, on a decomposable (LF) domain, only confinement can fail without (Av). The repaired step 6 needs confinement for step 4's formula "O iff α(t) > π(h)", and §7's monotone rotation s(ρ) is exactly what replaces it.

---

## 3. JJ2, step by step

### 3.1 Theorem 3.4. Correct with repair (PROVED); referee priority 5

**(a) Confinement.** For p ∈ [e_i, e_m], switching a non-null set of gambles positive at i and m to acceptance would strictly lower Φ_i and Φ_m. This violates (NT), since C_p is coherent and gives S or O there, and acceptance is strictly best. So K_p ⊆ [e_i, e_m].

**(a) Null set.** On the edge, C_p is silent at h iff r(h) ∈ K_p. Silence on a non-null subset of Z violates Lemma 3.1: the only world of supp p ⊆ {i, m} at which g is negative is i, and it carries the zero. Correct.

**(b), (c) need a repair.** With the standard convention, relint{τ} = {τ}. Then precise points lie in N, and (c)'s contradiction "τ ∈ relint K_{p(s)} ⊆ N" would also fire at s₁ itself. In addition, N would be a union of uncountably many non-open sets, so the Lindelöf step fails.

*Repair:* define N := ⋃_p (a(p), b(p)), the union of open intervals (empty for singletons). Then:
- N is open, and is a countable union of such intervals;
- ν(N) = 0 by (a);
- the infimum argument of (c) is correct. It needs b(s₁) = τ: the set {s : b(s) > τ} is open and does not contain s₁, and b(0) = 0 < τ.

Theorem 3.4 is not used by Thms 5.5, 7.2 or 7.4.

### 3.2 Lemma 4.1. Correct (PROVED); referee priority 3

This is an independent proof of JJ3 Thm 2.1 (§2.2). The "cone modulo null sets" step holds because the disagreement set of two coherent models is an exact cone: the advice of D_K is constant on open rays.

### 3.3 Lemma 4.2(a)–(d) and Lemma 4.3. Correct (CHECKED reading; PROVED for 4.3)

- (a)–(c) are JJ3 Lemmas 2.3 and 2.4, read for the full domain.
- (b) The vertex limit uses strict-best at e_b. Edge confinement uses (F1) and full-domain availability.
- (d) is R4 Thm B in its chart form. It needs only (c) and continuity.
- Lemma 4.3 is JJ3 Prop 2.5. On the full domain the (LF) availability step is automatic.

### 3.4 Lemma 5.2 and Proposition 5.3 (removal by rotation). Correct (PROVED; CHECKED (E)); referee priority 4

**Lemma 5.2** is JJ3 Lemma 3.1 written in the orientation g = −h. The correspondence:
- JJ2's i is JJ3's j;
- JJ2's k is JJ3's l;
- JJ2's m is JJ3's o;
- JJ2's P is JJ3's m_h;
- π < 0 is case (b2).

**Prop 5.3(a)** compares x = α·c^g, y = α·c^{−g} and d. The sign of y and d is unchanged. A change in the sign of x′ = x − ty occurs only in two cases:
- **Case 1:** 0 ≤ x ≤ ty, not both zero. Then y > 0 and d < 0, before and after, so accept −g is the unique minimiser both times.
- **Case 2:** ty ≤ x ≤ 0, not both zero. This includes the case x = 0, y < 0. Then x ≤ 0 and y ≤ 0, so α is in the closed silence region. For an inactive zero that region is ∅ or {P}, where x = y = 0. So Case 2 is empty.

Because the weak minimiser set is a function of the three signs (§1), it is unchanged at every α ∈ Δ. **Priority 4 is confirmed.**

**(b)**
- The new c^g at negative worlds of g is c^g_i − tc^{−g}_i < 0, since c^{−g}_i > 0 by (F1).
- At positive worlds it is ≥ c^g_m > 0.
- c^{−g} is only rescaled.

**Using the rotation for both orientations (PROVED).** Rotate the zero of g, then the zero of −g with the new data. The second rotation acts on the once-rotated field, whose minimiser sets, and hence activity, are unchanged. After both rotations, every negative coordinate of each orientation is strictly signed:
- (1 − t)c^{−g} − t(c^g − tc^{−g}) is < 0 at the negative worlds of −g;
- it is > 0 at the positive worlds of −g.

`checks.py` (E): 400 exact pairs with an odd zero plus one or two zeros of −h. Minimiser sets were compared on the **overlay** of the old and new arrangements (a complete test), and the final field is strictly guiding. 0 failures.

**The claim "if g carries a zero, every zero of −g is inactive" is correct.**
- If g is the minority orientation, the zeros of −g are odd.
- If g is the majority orientation, g's zero is odd, and silence is never a weak minimiser.

### 3.5 Proposition 5.4 and Theorem 5.5. Correct (PROVED)

**Prop 5.4.** The interface between the unique-acceptance cell and the unique-silence cell of any field lies on that field's c-line. For the original field it contains a segment of the line through e_i, so c″^g_i = 0. The Fubini step for the second claim uses equality of open convex sets that agree a.e.

**Thm 5.5.** The first proof uses ccibu. The second ("without ccibu") is the bypass of §4.

### 3.6 Corollary 5.6. (a), (c) correct; (b) ⇒ (a) has a gap

JJ2 says: "the interior Bayes models are selected (Lemma 4.1) and have full support, so (b) implies (a)". Lemma 4.1 gives B_w = C_p for **some** p, obtained from KKM. It does not give an interior p. So (b), which constrains C_p through supp p, does not by itself prevent B_w = C_p with p on an edge missing the zero world.

Lemma 3.1 at such a p requires only that k and m are in supp p, which an edge index {k, m} satisfies. I found no argument that closes this in the abstract.

This is a side result about the brief's suggested placements. Nothing in Thms 7.2 and 7.4, or in §4 below, uses it. Repair options:
- state (b) for the index set {p : C_p = B_w for some interior w}; or
- drop (b).

### 3.7 Table 7.2, S8a and S8b (the two strict uses of strict badness). Correct (PROVED; CHECKED (C), (D)); referee priority 1

**S8a (the chart-form edge box inside Thm cuts, Step 1).** Let A′, B′ be good gambles in the witness balls, and let q₀ ∈ [e_a, e_b] lie in R(A′) ∩ R(B′), which is relatively open in the plane.
- A neighbourhood O of q₀ in int Δ has P(·, A′) > 0 and P(·, B′) > 0, by the every-weight chart identity (W6).
- For λ in the open ratio interval, g := A′ + λB′ has g_a, g_b < 0. By Fubini it can be taken good, outside the null set of (F2).
- Superadditivity of P gives P(·, g) > 0 on O, so O ⊆ R(g) ⊆ {d^g > 0}. On the full domain both acceptances are available, so R(g) = {c > 0, d > 0}.
- Hence d^g·q₀ ≥ 0.
- But d^g has the strict sign of g (F2), so d^g < 0 on the whole closed edge. Contradiction.

So (F4) is not needed. `checks.py` (D) shows that, with weak c^g, the c-version gives c·q₀ = 0 at 17 101 of the tested edge points, while d < 0 at all 63 000.

**One condition must be stated:** this needs accept −g to be in the advice range of g. That holds on the full domain, but on a general domain it would need Cor TSalways(b), which has not been audited under weak signs.

**S8b (Thm cuts Step 2). A-case: g near the b-crossing w′ ∈ F_a.**
- Veccluster (S6, which needs only weak signs plus mixedness of h) gives c(g)/|c(g)| → c_a(w′)/|c_a(w′)|.
- c_a(w′)_a = −λ_{ca}w′_c < 0, since w′_c > 0 on F_a at the b-crossing (Lemma signs) and λ_{ca} > 0.
- Hence c(g)_a < 0 strictly for g close to w′, and σ ∈ (q₀, e_a).

CHECKED exactly in (C), on the normalised facet maps, for ε ∈ {1/19, 1/7, 4/13} (x₊ = 3/2, 2, 3) and all three failing pairs.

**S8b, B-case: g near the b-crossing w ∈ F_c.** The crossing row c_c(w)_b = λ_{bc}w_b = 0 gives no strict sign at b. If c(g)_b = 0, then α vanishes on the closed edge only at e_b, so σ = e_b, and d(σ) = d_b < 0 by (F2). Then:
- z ∈ [q₀, e_a) and α(z) > 0, as in the strict case;
- step 4 has the apex strictly between σ = e_b and B₁, because d changes sign along the α-line;
- step 5 has σ_m = e_b, so trivially σ_m → e_b.

**S8c (Step 3). JJ2's justification is not right in general; the conclusion is.** Step 3 needs {α ≤ 0} ∩ int Δ to contain points near a vertex of V⁻ at which d < 0. JJ2 says "the half-neighbourhood still exists if α(e_l) = 0". That fails when α(e_l) = 0 and α > 0 at the other two vertices. Then {α ≤ 0} ∩ Δ = {e_l}, and the control in `checks.py` (C) finds no interior grid point with α ≤ 0.

The correct reason is that V⁻ always contains a vertex with **strict** α < 0:
- A-case: V⁻ = {e_a}, and c(g)_a < 0 by veccluster, as above.
- B-case: V⁻ = {e_b, e_c}. Since w_c < 0 on F_c, c_c(w)_c = −λ_{ac}w_a < 0 (w_a > 0), so veccluster gives c(g)_c < 0 strictly.

At that vertex d < 0 by (F2). CHECKED (C): 2479 exact random configurations in both cases, including 995 with c_b = 0, and 0 failures.

*Repair to S8c:* replace "the half-neighbourhood still exists if α(e_l) = 0" by "V⁻ contains e_a (A-case) or e_c (B-case), at which α < 0 strictly by Lemma veccluster and d < 0 by (F2)".

The forcing clauses of Steps 6–7 (R1 Lemma 1.5 at e_b, and R1 Prop 2.8) use only the vertex property. That property is (F1) and (F2) at positive coordinates, together with vertex coherence (W5). Correct.

The other rows of Table 7.2 (S1–S7, S9–S14) I did not re-derive. Their status is one reader (JJ2).

---

## 4. The ccibu bypass

### 4.1 What Theorem gm is used for

Theorem gm is stated for a strictly guiding additive ranking satisfying (LA), (S), (C) and covering T1. Applying it to JJ3's Φ′, or JJ2's rotated Φ′, as stated requires (LA), (S), (C) for Φ′. That is what ccibu supplies. JJ3 §8 item 6 is right that the original selection need not be (NT) for Φ′, so there is no direct (S).

The bypass is to apply gm's **proof**. That is possible if the proof uses a cover only through properties that Φ′ has without ccibu.

### 4.2 Boundary properties follow from the interior family (PROVED)

Let ℓ be strict-best and weakly guiding (in particular, strictly guiding) on a decomposable domain. Suppose that for every interior w the w-Bayes model is a.e. unique and equal to D_{K_w}.

- **(N3) Vertex models.** At e_k the pointwise minimiser B^k is a.e. unique, by strict-best. Interior B_w → B^k in measure as w → e_k, since off the null vertex-tie set the strict minimiser persists. Any Hausdorff cluster K′ of K_w then has D_{K′} = B^k a.e. So B^k is coherent, and K_w → K_{e_k}. This is R1 Lemma 1.5's conclusion without (S).
- **(N4) Boundary weights.** Let w₀ ∈ ∂Δ and let K′ be a Hausdorff cluster of K_{w_n}, with w_n → w₀ interior. Off ±∂D_{K′} and countably many null sets, the advice of D_{K_{w_n}} at h stabilises to that of D_{K′}. It is a minimiser at w_n for large n, hence a weak minimiser at w₀. D_{K′} ∈ M by closure under convergence in measure. So a coherent w₀-Bayes model exists. This is R1 Lemma 1.3(a)'s conclusion without (S).
- **(T)** is replaced by the hypothesis that T1 = B_{w*} with w* interior.

### 4.3 The cover enters the gm chain only through (N1)–(N4), (T) and (LF) (CHECKED)

**Evidence.**
1. **Write-up §5, header.** "Throughout this section the ranking is strictly guiding additive on a decomposable domain with (LF) at T, and (BU) holds at every interior prior with K_{p*}=T." The statements of Thm TS, Thm cuts and Cor availability are explicitly realisation statements.
2. **N28 §1.** The note derives from the cover exactly (BU), uniqueness of K_q, Hausdorff and joint continuity, and K_{p*} = T, and works from those. This covers Thm TSalways, apex, walls and vertexfree.
3. **I2, PropD, C1 (Theorem A).** These work at the level of the family: charts in CF form, (DL) via Prop necessary(a), and K_q.
4. **Keyword search.** I searched 25 source files of the chain (N21, N28, R10b, N12, N14_referee, N23_referee, I1, I1_referee, I2, I2_referee, C1, C1C2_referee, C2, PropD, N27, R4, R15, N15, N18, N20, R12, N28_referee, TS_second_referee, R6, R8) for (LA), (S), (C), competitiveness, Theorem kkm and R1 Lemmas 1.3–1.5. Every occurrence in the chain is one of three kinds:
   - (i) the extraction of (N1)–(N4)/(T) (R1 Thm 2.2(N), Lemmas 1.3–1.5, Prop necessary), including R4 Thm B, whose hypothesis is (N1)–(N2), and R10b Prop V and Cor V1, which use vertex coherence;
   - (ii) the converse direction, building a ranking (ccibu, R1 Thm 2.2(S)), which serves only Cor CFnone and Prop CF(⇐);
   - (iii) constructions unrelated to the chain (C2's two-world systems; R8).

This is CHECKED, not PROVED. I did not re-derive the chain. The search covers the files listed, not every archived note.

### 4.4 Family form of Theorem gm (CHECKED, at gm's recorded status)

**Theorem gm-F.** Let ε ∈ (0,1), and let M be a decomposable domain with (LF) at D_{T1}. Let ℓ be strictly guiding additive penalties on M, with integral form and an integrable envelope, such that:
- (BU) for every w ∈ int Δ, the w-Bayes model is a.e. unique and equals D_{K_w};
- (TP) T1 = B_{w*} for some w* ∈ int Δ.

Then there is no such ℓ.

*Status.* This is the proof of Theorem gm (every route; each refereed once, and the short route's Thm D unrefereed) read with the standing hypotheses of §4.3. The reading itself is one reader (KK1), CHECKED. (N3) and (N4) are supplied by §4.2.

### 4.5 Consequences

- **JJ3 Thm 5.1.** Φ′ satisfies the hypotheses of gm-F: Prop 3.3, Thm 2.1 and Prop 2.5, with (LF) a property of M. So Thm 5.1 holds **without ccibu**, at the status of gm-F.
- **JJ2 Thm 5.5, second proof:** the same argument. Correct.
- **JJ2 Thms 7.2 and 7.4: genuinely ccibu-free.** They never construct a ranking with (S) or (C). The direct route (7.2) requires, beyond §4.3, the sign audit of Table 7.2, which is exactly JJ2's (W1)–(W6) claim for weakly guiding fields. I verified S8a–c (§3.7). The rest is one reader.
- **Domain needed by 7.2 and 7.4.** They use the **full domain**, through:
  - S3b ("− is available");
  - S8a (acceptance of −(A+λB) available, so R ⊆ {d > 0});
  - (F2) wherever d is used (S12 (DL), S14).

  On a general domain the availability of both acceptances is Cor TSalways(b), which has not been audited under weak signs. So 7.2 and 7.4 are full-domain theorems. (Av) alone, which supplies only the majority acceptance, would not suffice for this route.
- **Side remark (CHECKED, conditional on gm-F).** Prop CF(⇐) produces, from a CF(T1) solution, strictly guiding penalties on the all-model domain whose interior Bayes models are unique and coherent at every q, with T1 among them. So, if gm-F is confirmed by a second reader, Cor CFnone and Theorem A for bare CF solutions lose their ccibu dependency as well. I do not change their status here.

---

## 5. Verified statements and dependencies

**Theorem KK1.1 (exclusion of protected weak-additive designs; PROVED modulo gm-F).** Let ε ∈ (0,1). Let M be the full four-advice domain, or a decomposable domain with (LF) at D_{T1} satisfying (Av): for every two-element {l, o} ⊆ Ω, acceptance of g is in A(g) for a.e. g with g_l > 0 and g_o > 0. Then there is no pair (Φ, p ↦ C_p) such that:
- Φ is additive, with an integrable envelope, and weakly guiding on M;
- p ↦ C_p maps Δ to coherent members of M, is continuous in measure, and has C_{q₀} = D_{T1};
- (NT): for every p and X ∈ M, Φ_i(X) ≤ Φ_i(C_p) for all i ∈ supp p implies X = C_p a.e.

The same holds with JJ3 Remark 5.3's (i)–(iii) in place of (NT).

*Proof chain.*
1. JJ3 Lemma 1.1, Thm 2.1, Lemmas 2.3–2.4, Prop 2.5.
2. JJ3 Lemmas 3.1–3.2 and Prop 3.3 (or JJ2 Prop 5.3, for the inactive zeros).
3. JJ3 Lemma 4.2 (with the repair of §2.7), Lemma 4.3, Lemma 4.4, Thm 4.1.
4. Hence Φ′ is strictly guiding and satisfies (BU) at every interior weight, with T1 = B′_{w*}.
5. gm-F gives the contradiction.

*Dependencies.*
- **Theorem gm**, through gm-F. Any one route suffices: the short route (collar, Thm D, Thm A), or I1, or I2/C2. Recorded status: each route refereed once, and Thm D not refereed. The gm-F reading is CHECKED (§4.3).
- **ccibu: not used.** JJ3's own Step 2 (gm as stated + ccibu) remains a valid alternative at ccibu's status.
- **(Av):** only in Lemma 4.2 step 3. It is automatic on the full domain.
- **(LF):** in Prop 2.5.
- **Other imports:** Theorem kkm (Loss Dominance Generalized v2), II1 Prop 3.1(a) with Lyapunov convexity, injectivity of K ↦ D_K.

**Theorem KK1.2 (JJ2 Thm 7.4, full domain only; PROVED modulo the imported chain of gm's short route and JJ2's Table 7.2).** On the full domain the same conclusion holds via JJ2 Thm 7.2 (no weak cover of T1).
- ccibu: not used.
- Rows S8a–S8c of Table 7.2: two readers (JJ2, KK1; S8c with the repaired justification).
- Remaining rows: one reader.

This is an independent second route on the full domain. KK1.1 does not depend on it.

**What is not affected** (BRIEF31 correction 4; AUDIT_JJ).
- Nothing here excludes T1 by the adopted axioms.
- These results close the protected subclass on the full domain and on (LF) + (Av) domains.
- The non-(Av) branch (JJ3 §7; KK3), the non-protected rate designs, general (FC) rankings and the clone route stay open.

---

## 6. Status table

| Item | Statement | Label |
|---|---|---|
| JJ3 1.1, 1.2 | strict-best; × WLOG; zero types; switching conditions | PROVED (second reading) |
| JJ3 2.2, 2.1 | KKM for leading ranking; unique, coherent, selected B_w at every interior w | PROVED (second reading) |
| JJ3 2.3, 2.4 | continuity; every-gamble convexity; every-weight charts; zero lines | PROVED (second reading) |
| JJ3 2.5 | T1 = B_{w*}, w* interior | PROVED; import II1 3.1(a) CHECKED |
| JJ3 3.1 | silence regions | PROVED (second reading); CHECKED (A) for (b2) on the edge |
| JJ3 3.2, 3.3 | removal of non-essential zeros, all w ∈ Δ | PROVED (second reading) |
| JJ3 4.2 | edge family; s_h depends only on π(h) | **PROVED with repair** (§2.7); CHECKED (A), (A′) |
| JJ3 4.3, 4.4, 4.1 | edge touching; T1 accepts y(a); essential zeros null under (Av) | PROVED (second reading); CHECKED (B) |
| JJ3 5.1, 5.3 | exclusion on full / (LF)+(Av) domains | PROVED modulo gm + ccibu as written; modulo gm-F without ccibu |
| JJ2 3.4 | edge precision | PROVED with repair (relint); unused downstream |
| JJ2 4.1, 4.3 | interior Bayes structure; T1 interior | PROVED (second reading) |
| JJ2 5.2, 5.3, 5.4 | activity; rotation removal (both orientations); active zeros intrinsic | PROVED; CHECKED (E) |
| JJ2 5.6 | brief's placements inactive | (a), (c) PROVED; (b) ⇒ (a) GAP |
| JJ2 S8a, S8b, S8c | strict badness replaced by (F2), veccluster | PROVED; CHECKED (C), (D); S8c justification repaired |
| §4.2 | vertex coherence and boundary coherent Bayes models from the interior family | PROVED |
| §4.3–4.4 | gm uses a cover only through (N1)–(N4), (T), (LF); gm-F | CHECKED (standing hypotheses + exhaustive keyword search), one reader |
| KK1.1 | no protected weak-additive design through T1 on the full domain or (LF)+(Av) domains | PROVED modulo gm-F; no ccibu |
| KK1.2 | same on the full domain via JJ2 7.2 | PROVED modulo gm short-route chain + Table 7.2 (S8a–c two readers) |

## 7. Files

`kk1py/checks.py` → `kk1py/checks.out` (0 failures):
- (A) the whole-edge minimiser structure of essential pairs, on 3000 exact pairs, at every arrangement breakpoint and midpoint;
- (A′) an exact configuration showing that JJ3's original inference in step 6 is invalid;
- (B) the two Jacobians, at 2000 rational points each;
- (C) the strict facet signs at the b-crossings for three values of ε, and N21.6 Steps 2–3 under weak signs (2479 configurations, including c_b = 0), with the control for S8c;
- (D) S8a: d < 0 on the closed edge, against the failure of the weak c-version;
- (E) the rotation applied to both orientations, with a complete overlay test, on 400 pairs.
