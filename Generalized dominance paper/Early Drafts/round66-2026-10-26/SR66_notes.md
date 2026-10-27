# SR66: referee report on the simple safe-improvement ranking (AUDIT_r66_extension §2) and the abstract construction lemma (§3) (26 Oct 2026)

Labels: PROVED (argument checked or supplied here) / CHECKED (exact computation) / CONJECTURE. Scripts are in `sr66py/`. Run `python3 -I checks.py > checks.out` from that folder; it takes about 80 seconds. `checks.out` ends in ALL PASS.

Inputs read: BRIEF66 (SR66 role); AUDIT_r66_extension §2–3 (and §4–6 for context); AUDIT_r66_message; the universal-coverage draft §2–6; REF65_hA; ES64 §1 and §3; WT65; AD65; REF65_ad; the covering paper §2 (Lemma open, Theorem 2.9, Prop lowdim) and its Lemma LF (§4.2); LDG v3.2 §1 (to see what "abstract setting" means there).

## 0. Verdict

**The Proposition is correct as stated.** I re-proved every clause in the finite-world setting of round 65 and found no error. The four specific checks also pass:
- safe ⟺ μ(A ∩ hull B) > 0, including the cases B null and Q_B = Δ;
- guidance strictly improves its own world;
- the mixed guidance/safe case of (Add);
- there are no non-trivial ties.

The auditor's correction on lower-dimensional targets is also correct.

**The abstract lemma (§3) is correct in substance, but four hypotheses are left unstated (GAP).** They are:
1. the null record must be guidance;
2. the world scores must be potentials whose differences depend only on the record;
3. "safe" must be read set-theoretically ("attacks no coherent model"), or else the model class must be decomposable;
4. guidance and safety must be invariant under null modifications.

A repaired statement is in §3. Two further points matter for LDG66.
- The lemma needs a *record structure*; LDG's bare "set of models" setting does not supply one. A Boolean algebra modulo a null ideal suffices, and no measure or topology is needed.
- Without the record structure the lemma is nearly trivial: "accept improvements only out of incoherent models" gives every conclusion except (IB) and (Add) (§3.3). So the content of the safety device is precisely that it is a *record-level* substitute for "the source model is incoherent".

**Two additions that are not in the audit (PROVED, and CHECKED on instances).**
- *(Tr) fails.* The ranking is not transitive. There is an exact instance at one world (C7). Do not claim transitivity.
- *Converse.* For this ranking, every dominance by a coherent model is strict at every world, and its record is safe. So (ID) for this ranking is *equivalent* to the strict, safe repair property: the analogue of Corollary cor:H, with no tie cases.

## 1. Verdict table

Setting throughout, unless stated otherwise:
- n ≥ 1 worlds;
- μ satisfies (M): finite, the null sets of Lebesgue measure, ∫|h| dμ < ∞;
- K′ ⊆ Δ is nonempty, compact and convex, and U = D_{K′};
- models are measurable X ⊆ U modulo null sets;
- the coherent models on U are the D_Q with K′ ⊆ Q.

Neither K′ ⊆ relint Δ nor n ≥ 2 is used anywhere except in the (LF)/coverage clause.

| # | Item | Verdict | Note / repair |
|---|---|---|---|
| P1 | Reflexivity and a.e. identification | CORRECT | The null record is in G_i. G_i, safety and d_i are invariant under null modification of A and B, so Acc_i is a set of record classes. Lemma lem:record applies. The null record is never safe: it attacks every coherent model. So it enters *only* through guidance (see L1). |
| P2 | Strict (G) | CORRECT | A non-null r ∈ G_i has d_i(r) = ∫_A\|h_i\| + ∫_B\|h_i\| > 0, because {h_i = 0} is a null hyperplane (M) and the integral is finite (first moment). r⁻¹ ∉ G_i, since otherwise A and B would be null; and d_i(r⁻¹) < 0, so r⁻¹ is not safe-accepted. |
| P3 | (IB) | CORRECT | The rule is a set of records (Lemma lem:record). No decomposability is used. |
| P4 | (TC), (FCC); no non-trivial single-world ties | CORRECT | Every accepted non-null record has d_i > 0, and d_i(r(X,Y)) = m_i(X) − m_i(Y). So X ⪯_i Y with X ≠ Y forces m_i(X) > m_i(Y). This is stronger than the deletion lemma needs: each ⪯_i is a *strict* sub-relation of Brier, together with a.e. equality. A chain gives m_i(A₀) ≥ m_i(A_k), so A_k ≺_i A₀ is impossible. A tie at one world forces both records to be null. |
| P5 | (Add), including the mixed guidance/safe case | CORRECT | See §2.3. Record form: Acc_i is closed under ⊔. Cases: (i) both in G_i, then the union is in G_i; (ii) otherwise one record, say r₁, is safe with d_i(r₁) > 0. If r₁⊔r₂ attacked a coherent C, then B₁ ⊆ B₁∪B₂ ⊆ C and A₁∩C ⊆ (A₁∪A₂)∩C is null, so r₁ would attack C. Hence the union is safe, and d_i(r₁⊔r₂) = d_i(r₁) + d_i(r₂) > 0, because d_i(r₂) ≥ 0 for every accepted r₂. CHECKED: 14 665 accepted disjoint pairs, 3 449 of them mixed. |
| P6 | Protection: no coherent model has a weak dominator except itself | CORRECT | Let Y weakly dominate a coherent C. Then r(Y,C) attacks C, so it is unsafe, so it lies in G_i at every world. Hence Y∖C ⊆ int ℝⁿ₊ ⊆ C a.e., so Y∖C is null; and C∖Y ⊆ {h ≪ 0} a.e. **Wording repair (optional):** the audit says the removed part "cannot belong to U". It is cleaner to say "no coherent model contains a gamble h ≪ 0": since C∖Y ⊆ C, it is null. This makes protection independent of the domain: it holds on any domain whose coherent models are of the form D_Q (useful for TS66). Lower-dimensional Q, and Q meeting ∂Δ, are included. CHECKED: 2 442 pairs, 1 579 of them "C ⊕ a change guided at one world". |
| P7 | Strict dominance of every incoherent model, via Theorem H | CORRECT | Theorem thm:H gives N ∈ 𝒞_U with m(N) − m(X) ≫ 0 and N ⊆ hull(X∖N). So μ((N∖X) ∩ hull(X∖N)) = μ(N∖X) > 0, the record r(N,X) is safe (item S1), and d_i > 0 at every world, so r(N,X) ∈ Acc_i for all i. r(X,N) has d_i < 0, so it is neither safe-accepted nor in G_i (guided records have d_i ≥ 0). Hence N ≺_i X at every i, and N is undominated by P6. CHECKED: the whole chain on 1 200 random incoherent two-world rivals (C6), with the safety tested from the *definition*. |
| P8 | (W), (GC), direct (C) | CORRECT | 𝒰 = 𝒞* = 𝒞_U. (GC): incoherent models are dominated. (W): coherent models weakly dominate themselves, and incoherent ones are dominated. (C) holds trivially, because a tie at even one world forces a.e. equality (P4). |
| P9 | (LF) and coverage: exactly the full-dimensional K with K′ ⊆ relint K | CORRECT | Requirements (i)–(iii) and (v) hold by P2–P8. (iv) holds iff K′ ⊆ K (Lemma lem:LF(a)) and then D_K is coherent and protected. (vi) is ranking-independent: Lemma lem:LF(b) for full-dimensional K, and lem:LF(c) / paper Prop lowdim for lower-dimensional K on the one-sided U. So the covered K are exactly the full-dimensional K with K′ ⊆ relint K, and Corollary cor:universal (universal cover on U) carries over verbatim. |
| S1 | safe ⟺ μ(A ∩ hull B) > 0, including B null and Q_B = Δ | CORRECT (on U = D_{K′}) | See §2.1. B null or B ⊆ ℝⁿ₊ a.e. ⟺ Q_B = Δ ⟺ hull B = int ℝⁿ₊. Then safe ⟺ μ(A ∩ int ℝⁿ₊) > 0, which agrees with the direct argument (every D_Q ⊇ int ℝⁿ₊, and int ℝⁿ₊ = D_Δ is coherent on U). CHECKED: 6 000 records against a brute-force attack test that does not call hull() (1 413 with B null, 922 with Q_B = Δ, 1 159 with A null, 613 null records). **Scope note for TS66:** on a two-sided domain with Q_B = ∅, the record (∅, B) is safe (vacuously), but the hull test with the convention D_∅ = ℝⁿ calls it unsafe. The correct general form is: "safe ⟺ Q_B = ∅ or μ(A ∩ hull B) > 0". |
| S2 | Guidance records strictly improve their own world | CORRECT | As in P2. It uses only that {h_i = 0} is null and that ∫\|h\| < ∞. CHECKED: 3 539 non-null guided records. |
| S3 | (Add) when one record is guidance and the other is safe | CORRECT | As in P5(ii). The guided record may itself be unsafe; this does not matter, because safety of the union needs only *one* safe part (upward closure). Its score contributes ≥ 0. |
| S4 | No non-trivial ties, so (C) is trivial | CORRECT | As in P4 and P8. In particular, the zero-score clause of AD65's plain-Brier variant is unnecessary: the simple ranking is that variant with the tie set removed. |
| L1 | Abstract lemma (§3): statement and hypotheses | **GAP** (unstated hypotheses; conclusion correct once they are added) | Missing: (a) null record ∈ G_ω (needed for reflexivity; the null record is never safe); (b) world scores are potentials s_ω on models with s_ω(X) − s_ω(Y) a function d_ω of r(X,Y) (record-based, for (IB); a potential, for (FCC) and for the score step of (Add)); (c) safety read as "attacks no coherent model", with attack defined set-theoretically. Under the reading "no coherent C and model Y with r(Y,C) = r", upward closure of safety under ⊔ needs C ⊕ r₁ ∈ ℳ, i.e. decomposability; (d) G_ω and safety are invariant under null sets. Closure of G_ω under ⊔ *is* stated, and it is needed only for (Add). Repaired statement: §3.1. |
| L2 | Abstract lemma: the setting needed in LDG | **GAP** (transplant) | LDG v3.2 §1 has abstract models with no record structure, and there (IB) and (Add) cannot even be stated. Give LDG a minimal record structure: models are elements of a Boolean algebra modulo an ideal (a measure algebra is the main example). No measure, topology or finiteness of Ω is needed. Without records the lemma is nearly trivial (§3.3). |
| L3 | Abstract lemma: needs measurability of records? | CORRECT, as qualified | Only that records are pairs of algebra elements and that the scores are finite real numbers. In the application, finiteness comes from ∫\|h\| < ∞. |
| C1 | Auditor's correction: every coherent evaluable model, lower-dimensional ones included, is undominated; what fails for lower-dimensional targets is (LF) | CORRECT | P6 covers every D_Q with K′ ⊆ Q. Precisions: (i) lower-dimensional evaluable coherent models exist iff K′ itself is not full-dimensional (every Q ⊇ K′ is full-dimensional otherwise); (ii) for lower-dimensional K with K′ ⊆ K, *exactly* requirement (vi) (LF) fails. For K′ ⊄ K, D_K is not evaluable and (iv) fails as well. The draft's Theorem thm:main(b) already implies the correct statement, so the repair is one of emphasis in the prose. CHECKED instance: K′ = K = {½} with n = 2, so U = D_K; 2 322 rivals, none dominates (C8). |
| X1 | (Tr) (not claimed) | FAILS (PROVED by an exact instance, C7) | n = 2, K′ = {½}. Take X = c, Y = a₁∪a₂ and Z = b₁∪b₂, where a₁ ⊆ hull(b) and c ⊆ hull(a₂)∖hull(b). Then X ⪯₁ Y ⪯₁ Z, but X and Z are incomparable at world 1: the composite record cancels a₁∪a₂ and is unsafe. This is consistent with (Add), because the changes overlap. UN66 and LDG66 must not claim transitivity. |
| X2 | Converse: (ID) for this ranking ⟺ strict safe repair | PROVED | If a coherent N dominates X, then r(N,X) is non-null and accepted at every world, so d_i > 0 at every world (P4). It is safe: either it is safe-accepted at some world, or it is guided at every world; in the latter case it is (A,∅) with A ⊆ int ℝⁿ₊ a.e. (its removed part lies in U ∩ {h ≪ 0} = ∅), which is safe because A is non-null. So dominance by a coherent model is always strict at every world, and Theorem H is exactly what (ID) requires. |

## 2. Proofs checked, with details

### 2.1 Safety and the hull test (S1)

Let A, B ⊆ U be disjoint and measurable. "Safe" means: no coherent C has B ⊆ C a.e. and A ∩ C null.

- (⇐) Let C = D_Q be coherent on U with B ⊆ C a.e. Lemma lem:hull(c) gives Q ⊆ Q_B, so hull(B) ⊆ C. Then μ(A ∩ C) ≥ μ(A ∩ hull B) > 0, so C is not attacked.
- (⇒) If μ(A ∩ hull B) = 0, then hull(B) is coherent on U (K′ ⊆ Q_B by lem:hull(a), which uses B ⊆ U) and contains B a.e. (lem:hull(b)). So (A,B) attacks hull(B).

**The quantifier over C may be widened** to all D_Q with Q any credal set, without changing safety: if D_Q contains B and misses A, so does D_Q ∩ U = D_{conv(Q∪K′)} (WT65 C1(c)).

**Special cases.**
- *B null:* every q satisfies the a.e. condition vacuously, so Q_B = Δ and hull B = D_Δ = int ℝⁿ₊.
- *Q_B = Δ with B non-null:* this happens iff B ⊆ ℝⁿ₊ a.e. (test with q = e_i), and then hull B = int ℝⁿ₊ again.
- *A null:* the record is unsafe, since it attacks hull(B).
- *Both null:* the null record is unsafe.

All four cases agree with a direct argument: every coherent model contains int ℝⁿ₊, and int ℝⁿ₊ is itself coherent on U because Δ ⊇ K′.

### 2.2 Guidance and the potential (S2, P2, P4)

For X, Y ∈ ℳ_U, d_i(r(X,Y)) = m_i(X∖Y) − m_i(Y∖X) = m_i(X) − m_i(Y). This is finite by the first-moment condition.

For a non-null guided r, the integrand is positive a.e. on A ∪ B, because {h_i = 0} is null, and A ∪ B is non-null. So d_i(r) > 0.

Every non-null accepted record therefore strictly raises m_i. This one fact gives all of the following:
- (TC) and (FCC);
- the absence of non-trivial single-world ties;
- (C);
- the strictness of every coherent dominance (X2).

### 2.3 (Add) (P5, S3)

At the model level: if (X△Y) ∩ (Y△Z) is null, then r(X,Z) = r(X,Y) ⊔ r(Y,Z) a.e. (draft §6.3; AD65 Lemma 1.1). So it suffices that Acc_i is closed under ⊔.
- Case 1: both records are in G_i. Then the union is in G_i.
- Case 2: otherwise one of them is not in G_i. Since it is accepted, it is safe with d_i > 0. Safety is upward closed (the Fact in AD65 / Prop prop:lex). Score increments add, and the other increment is ≥ 0.

Nothing else is needed. In particular:
- no lexicographic level is needed, because there are no tie-acceptances that could sum to zero;
- the other record may be any accepted record, safe or not.

### 2.4 Protection (P6) and the converse (X2)

The argument uses only:
- every coherent model contains int ℝⁿ₊;
- no coherent model contains an h ≪ 0;
- r(Y,C) attacks C.

So it does not use one-sidedness. This answers in the affirmative, in one line, the brief's TS66 question "is protection still free on a two-sided domain?", whenever the coherent models there are D_Q's with Q ≠ ∅ (not refereed further here).

### 2.5 Dependence on other worlds

Unlike the comparison-deleted ranking 𝐂𝐃(𝒞_U), the simple ranking at world i depends only on:
- the world-i score d_i;
- world-i guidance;
- the world-independent predicate "safe".

No moments at other worlds enter. UN66 can simplify the scope paragraph "Coherence enters the definition of the ranking" accordingly: coherence enters *only* through safety, and nothing cross-world remains.

## 3. The abstract construction lemma (L1–L3)

### 3.1 Repaired statement (PROVED)

**Setting.**
- 𝔅 is a Boolean algebra with an ideal 𝔑 of null elements. Work in 𝔅/𝔑, i.e. identify elements that differ by a null element.
- Fix u ∈ 𝔅. Models: a set ℳ of elements x ≤ u. No closure of ℳ is assumed.
- 𝒞 ⊆ ℳ is the coherent class. Ω is any nonempty set of worlds.

**Records.**
- r(x,y) := (x∖y, y∖x), with inverse (a,b)⁻¹ := (b,a). The null record is (0,0).
- For records with disjoint supports, (a₁,b₁) ⊔ (a₂,b₂) := (a₁∨a₂, b₁∨b₂).
- (a,b) **attacks** c if b ≤ c and a ∧ c = 0.
- (a,b) is **safe** if it attacks no member of 𝒞.

**Data for each world ω.**
- A set G_ω of records.
- A function s_ω: ℳ → ℝ such that s_ω(x) − s_ω(y) depends only on r(x,y). Write d_ω(r(x,y)) for this difference.

**Hypotheses.**
- (R0) (0,0) ∈ G_ω.
- (R1) If r(x,y) ∈ G_ω and x ≠ y, then s_ω(x) > s_ω(y).
- (R2) [used only for (Add)] G_ω is closed under ⊔.
- (R3) If y ∈ ℳ, c ∈ 𝒞 and r(y,c) ∈ G_ω for every ω, then y = c.
- (R4) Every x ∈ ℳ∖𝒞 has some n ∈ 𝒞 with s_ω(n) > s_ω(x) for every ω and r(n,x) safe.

**Definition.** Acc_ω := G_ω ∪ {r safe : d_ω(r) > 0}, and x ⪯_ω y :⟺ r(x,y) ∈ Acc_ω.

**Conclusions.**
- (a) Each ⪯_ω is reflexive and depends only on records, so it satisfies (IB). It satisfies strict guidance with respect to G_ω, and (TC) and (FCC). Moreover x ⪯_ω y with x ≠ y implies s_ω(x) > s_ω(y), so there are no non-trivial ties.
- (b) Under (R2), (Add) holds.
- (c) No member of 𝒞 has a weak dominator other than itself.
- (d) Every x ∉ 𝒞 is strictly dominated at every world by a member of 𝒞.
- (e) 𝒰 = 𝒞* = 𝒞; (GC), (W) and direct (C) hold.
- (f) Converse. Assume (R5): every non-null record lying in G_ω for every ω is safe. Then (ID) for this ranking implies (R4).

*Proof.*
- (a) Reflexivity is (R0). Each element of Acc_ω is a record, which gives (IB). Every accepted record with x ≠ y has d_ω > 0, by (R1) or by the definition of the safe clause. That gives (TC) and (FCC) as in P4. Strict guidance: for non-null r ∈ G_ω, d_ω(r⁻¹) = −d_ω(r) < 0, so r⁻¹ ∉ G_ω by (R1) and r⁻¹ is not safe-accepted.
- (b) As in §2.3. The Fact (if r₁ ⊔ r₂ attacks c, then r₁ attacks c) is a Boolean-algebra identity. Score additivity is the telescoping of potentials: d_ω(r(x,z)) = d_ω(r(x,y)) + d_ω(r(y,z)).
- (c) r(y,c) attacks c, so it is not safe; hence it lies in every G_ω, and (R3) applies.
- (d) The record from (R4) is accepted at every world. Its inverse has d_ω < 0, so it is neither in G_ω (by (R1)) nor safe-accepted.
- (e) As in P8.
- (f) As in X2. ∎

*Where hypotheses come from in the application.*
- (R0) and (R2) are immediate.
- (R1) is P2 and needs (M).
- (R3) is P6.
- (R4) is Theorem thm:H together with S1.
- (R5) is the observation in X2.

### 3.2 What is and is not needed (L1, L3)

- **The null record.** It must be put into G_ω (R0) or adjoined to Acc_ω explicitly. It is never safe when 𝒞 ≠ ∅, and even when 𝒞 = ∅ it has d = 0.
- **Closure of guidance under ⊔.** It is used only for (Add). If two guided records had an unguided union, (Add) could fail at that world, unless the union happens to be safe.
- **Measurability.** Records are pairs of algebra elements, and the scores must be finite reals. No σ-additivity, no measure, no topology and no finiteness of Ω are used.
- **Reading "cannot be applied".** It must be read as "attacks". Under the reading "∃ y ∈ ℳ with r(y,c) = r", the Fact needs c ⊕ r₁ ∈ ℳ, i.e. decomposability of ℳ. With the set reading, no closure of ℳ is needed, and the repair hypothesis (R4) is, if anything, stronger.
- **Potential structure.** If only the record-based increments d_ω were given, without potentials, (FCC) could fail. A record-based "score" that is not a potential difference can be cyclic.

### 3.3 Why the record layer is essential (L2)

Drop the records. Let ℳ be arbitrary and define

  x ⪯_ω y :⟺ x = y, or (y ∉ 𝒞 and s_ω(x) > s_ω(y)),

with guidance added if one is available. Then:
- reflexivity, (FCC) and the absence of non-trivial ties hold;
- protection holds, because no change out of a coherent model is ever accepted;
- given only "every incoherent x is strictly improved at every world by some coherent n" (in the application, Remark rem:H(c) or Step 1 of Theorem H, *without* the shrink), every incoherent model is strictly dominated, and (GC), (W) and (C) hold.

What fails is (IB): "y is incoherent" is not a property of the record r(x,y). It also breaks (Add).

So the safety predicate is exactly the context-free, record-level replacement for "the change starts from an incoherent model". The geometric repair theorem (hull-preserving shrink) is what makes that replacement possible.

**LDG66 should therefore:**
1. state the lemma with the record structure of §3.1;
2. say in one sentence that (IB) and (Add) are the content beyond a trivial construction.

This is a framing observation, not an error in the audit.

## 4. Exact checks (`sr66py/`, CHECKED; output `checks.out`, ALL PASS)

**Model class.** Two worlds; μ has density e^{−|h|₁}.
- Ray directions are parametrised by the L¹-unit diamond, t ∈ (−1, 3). In this parameter μ restricted to cones is Lebesgue measure in t, and m(X) = ∫_X 2·dir(t) dt.
- So cone models (finite unions of open sectors with rational ends) have exact rational measures and moments.
- Records cut sectors anywhere, so this is not an atom system.
- D_{[a,b]} = (−a, 2−b) in t; U = (−k₁, 2−k₂); the coherent models are the single intervals (L, R) with −k₁ ≤ L ≤ 0 and 1 ≤ R ≤ 2−k₂; hull(B) = (min(0, inf B), max(1, sup B)).

**Domains.** K′ ∈ {[1/3, 2/3], [1/5, 4/5], {1/2}, [0, 1/2]}. The last one meets ∂Δ.

| Check | What | Count |
|---|---|---|
| C1 | safe (brute-force attack over coherent models, not using hull) ⟺ hull test; B null; Q_B = Δ; A null; null record unsafe | 6 000 records |
| C2 | non-null guided records: d_i > 0, accepted, inverse refused | 3 539 |
| C3 | (Add) on accepted disjoint pairs; mixed guidance/safe union safe with d > 0; record composition identity | 14 665 pairs (3 449 mixed) |
| C4 | accepted comparisons with X ≠ Y strictly raise m_i; no reverse comparison | 121 192 comparisons |
| C5 | protection; includes C ⊕ (change guided at one world) | 2 442 pairs |
| C6 | Theorem H chain: hull Bayes act with strict margin found; shrink; N coherent; hull(X∖N) = hull(X); N ⊆ hull(X∖N); safe by definition; strict dominance at both worlds; Corollary cor:shrink for random N ⊆ D_{Q_τ} | 1 200 incoherent rivals |
| C7 | exact (Tr) failure at world 1 (X1) | 1 instance |
| C8 | lower-dimensional K = K′ = {½}: D_K undominated; (LF) fails at its boundary rays | 2 322 rivals |

These checks are instance checks of PROVED statements. They are not a substitute for the proofs.

## 5. Recommendations

**For UN66.**
1. Use the simple ranking as the main construction. Its proof is P1–P9; every step is one line given Theorem H, Lemma lem:hull and Lemma lem:LF.
2. State explicitly that each ⪯_i is a strict sub-relation of the Brier order together with a.e. equality, that there are no non-trivial ties, and that the ranking is not transitive (X1).
3. Add the converse X2, which mirrors Corollary cor:H with no tie cases: (ID) ⟺ every incoherent X has a coherent N with m(N) − m(X) ≫ 0 and a safe record.
4. In protection, write "no coherent model contains a gamble h ≪ 0" rather than appealing to U.
5. Scope paragraph: coherence enters only through the world-independent safety predicate; there is no cross-world dependence (§2.5).
6. Lower-dimensional statement as in C1, with precisions (i) and (ii).

**For LDG66.** Use the statement in §3.1, including (R0), the potential form of the scores, the set-theoretic attack relation, and (R2) flagged as needed only for (Add). Mention the near-trivial record-free version in one sentence (§3.3), to explain why the record structure is part of the hypotheses.

**For TS66.** Two points from this report:
- On two-sided domains the hull test must read "Q_B = ∅ or μ(A ∩ hull B) > 0" (S1).
- Protection remains free whenever the coherent models are D_Q's with nonempty Q (§2.4).

## 6. Files (`sr66py/`)

| File | Content |
|---|---|
| `cone2d.py` | exact two-world cone-model library: interval-set algebra, μ and m, guidance, hull, safety by hull test and by brute-force attack, the simple ranking |
| `checks.py` → `checks.out` | checks C1–C8; ALL PASS |
