# PP15. Guard-changing rivals: the exact block, a filtered extension, and an architecture-level obstruction

21 October 2026. Brief: guard-changing rivals for audit's guard extension (`AUDIT_guard_extension.md`). One reader (me); not refereed.

Context read: the audit note in full; DESIGN_MEMO §8.10–8.11; PP13; PP14; AUDIT_round40_brief §2. I also read `REFEREE_guard.md`, which appeared in the folder while I was working. Its F1 and F2 overlap with §2 and §6 here; the overlaps are marked.

**Labels**
- **PROVED**: the full argument is given here.
- **CHECKED**: an exact computation. It uses rational arithmetic (`fractions`) for the geometry, exhaustive enumeration of every model on a cell abstraction, and exact SAT (pysat, CaDiCaL 1.5.3) on the full line arrangement.
- **NUMERICS**, **OPEN**, **CONJECTURE**: as stated.

**Scripts** are in `PP15_py/`. Run each one inside that folder as `python3 -I -B <script>`. Outputs are in the `*.out` files.

**Nothing new is assumed.** I use T1 = ε-contamination; the guards G₁, G₂, G₃ and neighbourhoods V_i of §2 of the note; the target-reference base of §11; the co-designed defenders C_i = D_{Φ_{s_i}(T)} of §11; and the filtered repairs, i.e. exposure conditions (E_T) and (E_C) of §§3, 12. The axioms are reflexivity, both halves of (G), (IB), (TC), T undominated, defenders undominated, (LA), and direct (C).

---

## 0. Verdicts

### Task 1: the §13 rival Y = T + majority on G₁ ∪ G₂

**1a. The defences (PROVED).**
- There are exactly two possible defences: σ := rec(T, Y) = (G₁ ∪ G₂, minority → majority), accepted at world 1 or at world 2, with all its (IB) copies.
- World 3 is refused by strict (G).

**1b. Exact block (Proposition 1, PROVED).** σ at world w ∈ {1, 2} is compatible with (TC) iff the installed repairs contain no label-3 repair whose off-guard part is a pointwise strict world-w improvement. Call such a repair (3,w)-improving.
- If such a repair is installed, the violation is *forced*: its closing link is a strict-(G) refusal, so no (G) + (TC) extension accepts σ at w.
- The blocking triangle is P ⪯_w P⁺ ⪯_w P″ ≺_w P. Here P⁺ is a σ-copy of P, P″ is a repair copy of P⁺, and P″ is P with the repair's off-guard improvement.
- P is never T. This is why (E_C) does not see the block: it only excludes compositions at T.

**1c. With the whole filtered collection, both defences are blocked (PROVED; CHECKED).**
- Explicit filtered (3,1)- and (3,2)-improving repairs exist: C₃ corrected on a patch, with T on the guards.
- This agrees with REFEREE_guard F2.

**1d. The block is removable without losing defender existence (PROVED; CHECKED).**
- Filter (F₃): drop the (3,1)- and (3,2)-improving repairs.
- Every X ∈ X_G ∖ {T} keeps a doubly exposed, unfiltered defender among C₁, C₂, C₃ (Lemma 2).
- Then σ can be installed at worlds 1 and 2 with every listed axiom preserved (Theorem 3).

### Part 2: rivals that alter the guards

**2a. Cycle classification (Theorem C, PROVED).**
- Setting: guidance + target-reference base + any filtered repairs + any target-referenced records ("T-records") ρ, each accepted only at worlds w whose guard G_w it breaks.
- Every accepted 2- or 3-cycle through a non-guidance link has the same shape. It consists of:
  - one repair of label i;
  - one ρ at a world w ≠ i that converts all of the third guard G_l to the majority answer;
  - one guidance link.
- The off-guard conditions are explicit, (O1) and (O2) in §3.

**2b. A record-based extended rule with proofs (Theorem P, PROVED; CHECKED).** At world w, accept every T-record that breaks G_w and satisfies one of:
- (i) it converts neither of the other two guards fully to the majority answer; or
- (ii) off the guards its new side is weakly worse than T at w.

Add the repair filter (F*): no label-i repair whose off-guard part is a pointwise strict world-w improvement, for w ≠ i. Then:
- (G), (IB), (TC), strictness, direct (C), (LA), T undominated and the defenders undominated all hold.
- Every X_G-rival is strictly dominated at every world by an undominated defender (Lemma 4*).
- T is competitive against every guard-changing rival outside the residual class 𝒵. A rival is in 𝒵 iff:
  - it is majority a.e. on at least two guards; and
  - for every guard G_w it breaks, it is somewhere strictly better than T at w off the guards.
- Type (i) records need no filter at all beyond (E_T), (E_C).
- (F*) is exactly the price of type (ii).
- Pure guard changes and the §13 Y lie outside 𝒵.

**2c. Exact obstruction (Theorem O, PROVED; CHECKED).**
- Let X_F := T + majority answer on a T-silent open set F around (1, 1, −L₀) with 1/(1+L₀) ∈ (c, c+ε).
- The guards themselves force every 1- and 2-defender to give the majority answer on F, and every 3-defender the minority answer. So X_F's exposed defenders are 3-defenders, whatever the concentration.
- Under the target-reference base, every undominated 3-defender C is ≥₃ T pointwise.
- Then the guard-changing rival Y_C := C off F, T on F (a member of 𝒵) has **no defence by T in any extension satisfying (G) and (TC)**:
  - worlds 1, 2: forced (TC) triangle C ⪯ X_F ⪯ P₂ ≺ C;
  - world 3: strict (G).
- No rule, filter, defender allocation, nested guard system or record-dependent guard choice escapes this. It strengthens REFEREE_guard F1, whose rival can be escaped with a more concentrated defender.
- **Consequence.** No extension of the guard architecture satisfies (S) with T selected. With no distinct all-world ties, no extension satisfies (S) at all.
- **Only escape (exact).** For every θ ∈ (c, c+ε), X_F's dominator must be oriented at world 1 or 2 and silent on part of F. These are intermediate models straddling {m₃ = θ}, outside V₁ ∪ V₂ ∪ V₃.

**2d. The three suggested candidates (PROVED).**
- (i) *World-i veto.* Taken literally, it defends nothing in Task 1, because both possible defences are vetoed. Its "permission" reading is Theorem P, and its limit is Theorem O.
- (ii) *Nested guard triples.* Theorem O does not depend on how many triples there are. Rivals that change every triple also exist.
- (iii) *Record-dependent guards.* Theorem O does not depend on the guards. Shared-transition noncomposition is lost as well.

### Part 3: KKM dominators for guard-changing rivals

**3a. Two exact necessary conditions on any all-world dominator Q of a pure guard change Y (PROVED).**
- **Proposition K1 (reverse target records).** A record (D, Q, T) with D off the guards is refused at every world where Q is both better and worse than T on non-null parts of D.
- **Proposition K2 (guard-transport triangle).** rec(Q, Y) is refused at world w if:
  - Q is somewhere worse than T at w off the guards; and
  - Y is pointwise weakly better than Q at w on the guards where they differ.

**3b. Concentrated defenders fail (Corollary K3, PROVED; CHECKED).** No undominated concentrated defender, including C₁, C₂, C₃, can be installed as an all-world repair for a pure guard change that is majority a.e. on two guards.
- In particular this holds for the §13 Y.
- C₃ fails at worlds 1 and 2 (K1). C₁ and C₂ fail at world 3 (K2).

**3c. An intermediate posterior tilt passes (CHECKED on cells only).**
- Take Q_b = Φ_{(1,1,b)}(T) with b in a window (b = 44/25 at ε = 3/10, L = 5). It is silent on part of G₁ and of G₂.
- It passes K1 and K2 for the §13 Y and is undominated.
- rec(Q_b, Y) installs at all worlds with 0 violations in the exhaustive cell abstraction.
- Elsewhere in the abstraction, the concentrated defenders C_i (for rivals that are not majority a.e. on either non-i guard) together with Q_b cover the pure guard changes with 0 violations, alongside T's type-(ii) defences.

**3d. These KKM repairs conflict with the type-(i) defences (CHECKED, explicit triangle).** A continuum KKM rule is **OPEN**.

---

## 1. Setting and notation

**Advice and ranks.**
- Problems are lines g modulo sign. M_k is the class of mixed problems whose minority world is k.
- On mixed problems advice is A (majority answer), S (silence) or B (minority answer); contradiction is ⊥.
- Rank at the minority world k: B 0, S 1, A 2. At the two majority worlds: A 0, S 1, B 2. Contradiction ranks 3.
- r_w(·) is the rank at w. "X ≻_w Y at g" means r_w(X(g)) < r_w(Y(g)).

**Target and guards.**
- T = D_M with M = c𝟙 + εΔ and c = (1−ε)/3.
- Guards: G_k ⊂ M_k compact, of positive measure, with T = B strictly on G_k. W = G₁ ∪ G₂ ∪ G₃ and U = Δ-lines ∖ W.
- In the note's construction, G_k is a small cone around γ_k = L e_k − (𝟙 − e_k) with L > (1−c)/c. The exact instance is ε = 3/10, L = 5 (`s2_geometry.out`).

**Defenders.**
- An i-defender is D_K with K ⊂ V_i. On the guards it gives B on G_i and A on G_k (k ≠ i).
- The co-designed defenders are C_i = D_{K_i}, with K_i = Φ_{s_i}(M), s_i = a e_i + (𝟙 − e_i), and a large.
- C_i ≥_i T pointwise: it is never worse than T at world i.
- I use a > ((c+ε)/c)². This also gives a > 1 + ε/c (Lemma 4) and K_i ⊂ V_i ∩ {m_i > ½}. a = 20 and a = 6 are checked at ε = 3/10.

**Relations.**
- R⁰ = guidance ∪ TR. TR is the target-reference base: at world w, accept (D, T|D, N) when D ⊂ U and N is strictly worse than T at w on a non-null part of D.
- 𝓡_EC: the filtered repairs rec(C, X). Here C is an i-defender undominated in R⁰, X ∈ X_G ∖ {T}, (E_T) and (E_C) hold, and the record is installed at every world with all copies.
- The *label* of rec(C, X) is i. Its record is (G_k ∪ G_l ∪ E, (A, A, C|E), (B, B, X|E)), where {k, l} = {1,2,3} ∖ {i} and E := D ∖ W.

**Further terms.**
- A *T-record* is any record whose old side is T on its disagreement set D.
- A T-record *breaks* G_w if μ(D ∩ G_w) > 0. It *fully converts* G_l if G_l ⊂ D a.e. and its new side is A a.e. on G_l.
- A repair of label i is **(i,w)-improving** (w ≠ i) if X ≻_w C a.e. on E.
- A model Q is **w-oriented** if Q ≥_w T pointwise: Q is never worse than T at w.

**Lemma R1 (REFEREE_guard; PROVED there).** An i-defender is undominated in R⁰ iff it is w-oriented off the guards for some w. Concentrated defenders must take w = i.

---

## 2. Task 1: the §13 rival

### 2.1 The possible defences

Y agrees with T except on G₁ ∪ G₂, where it gives A. So rec(T, Y) = σ := (G₁ ∪ G₂, B, A).
- **World 3.** On M₁ and M₂, A is correct at 3. So Y strictly improves T there, and strict (G) refuses T ⪯₃ Y.
- **World 1.** σ worsens G₁ (0 → 2) and improves G₂ (2 → 0). It is mixed; world 2 is symmetric.
- **Conclusion.** Every defence of T against Y is "σ ∈ R₁" or "σ ∈ R₂".
- **(IB).** Either one means accepting every copy (P, P⁺): P is any model with B on G₁ ∪ G₂, and P⁺ is P with A there.

### 2.2 Proposition 1 (exact block; PROVED)

Let 𝓡 ⊂ 𝓡_EC be any subcollection, R = R⁰ ∪ 𝓡, and w ∈ {1, 2}.
- **(a)** If 𝓡 contains a (3,w)-improving repair, then R ∪ {σ at w} violates (TC) at w. The violation is forced, so no relation satisfying (G) and (TC) contains R ∪ {σ at w}.
- **(b)** Otherwise R ∪ {σ at w} has no accepted 2- or 3-cycle through σ. In particular it satisfies (TC).

*Proof of (a).* Let R* = rec(C, X) be (3,w)-improving, with off-guard part E.
1. Let P be any model with B on G₁ ∪ G₂ and C's advice on E.
2. P ⪯_w P⁺ is a σ-copy.
3. P⁺ agrees with C on the whole disagreement set (A on G₁ ∪ G₂, C on E). So P⁺ ⪯_w P″ is a copy of R*, where P″ := P with X on E.
4. P″ differs from P only on E, where X ≻_w C. So P″ strictly improves P at w: (G) gives P″ ⪯_w P and refuses P ⪯_w P″.
5. Hence P ⪯_w P⁺ ⪯_w P″ ≺_w P.

*Why (E_C) misses it.* P = T would force C = T on E, and then (E_C) fails for R*. So the triangle always runs in a context other than T. ∎

*Proof of (b).* Let Γ be an accepted 2- or 3-cycle at w through σ.
1. **At most one σ.** σ-links cannot be adjacent: the new side A on G₁ is not the old side B.
2. **G_w needs a repair.** σ raises the rank at w on all of G_w (B → A, 0 → 2). Returning it needs A → B on G_w. Guidance never lowers rank, TR never touches W, and σ moves B → A. So Γ contains a repair of label ≠ w.
3. **Exactly one repair.** Two repairs in a cycle of length ≤ 3 are adjacent, and Theorem 2's noncomposition forbids that.
4. **Its label is 3.** Let w′ be the other world in {1,2}. A label-w′ repair moves A → B on G₃ (0 → 2 at w). σ fixes G₃, and the third link would have to lower the rank there, which no link can do.
5. **The third link.** On W, σ and a label-3 repair are exact inverses (B → A and A → B on G₁ ∪ G₂). So the third link L is the identity on W, and L ∈ guidance ∪ TR. In either cyclic order L carries X|E to C|E.
6. **L is not TR.** TR would need X = T on E. Then X = T on all of D, so (E_T) fails.
7. **L is guidance.** Then C is weakly worse than X at w on E, i.e. the repair is (3,w)-improving. That case is excluded.
8. Guidance-only cycles are trivial. ∎

### 2.3 With the whole filtered collection both defences fail (PROVED; CHECKED)

**A (3,1)-improving filtered repair.**
- Let F₁ ⊂ M₁ ∖ W be a non-null open set where T is silent and C₃ says A. Example: near (−1, 1/10, 1), `s2_geometry.out`, region R(3,1,+).
- Put X₁ := T on W, B on F₁, C₃ elsewhere. Then X₁ ∈ X_G.
- rec(C₃, X₁) = (G₁ ∪ G₂ ∪ F₁, A, B). F₁ witnesses (E_T) (X₁ = B ≠ C₃, T) and (E_C) (C₃ = A ≠ T).
- On F₁, B is correct at world 1 and A is wrong. So the repair is (3,1)-improving.

The mirror patch on M₂ gives a (3,2)-improving repair. This is REFEREE_guard F2's record. With all of 𝓡_EC installed, T has no defence against Y in any (G) + (TC) extension.

*CHECKED* (`s4_cells.out`, E1; all 6561 models on 8 cells):
- adding σ at world 1 gives 315 (TC) violations, 162 of them forced;
- every forced violation runs through a (3,1)-improving repair, and the same holds at world 2.

### 2.4 Removing the block

**Filter (F₃).** Install no (3,1)- or (3,2)-improving repair.

**Lemma 2 (defender existence under (F₃); PROVED).** Every X ∈ X_G ∖ {T} has a defender among C₁, C₂, C₃ that is doubly exposed and not excluded by (F₃).

*Proof.* Lemma 4 of the note gives a doubly exposed C_j. If j ∈ {1,2}, or j = 3 and the repair is not excluded, we are done. Otherwise (C₃, X) is (3,w)-improving for some w ∈ {1,2}; take w = 1 (w = 2 is symmetric). Consider the region R(3,2,+), a neighbourhood of g = (δ, −1, 1) with 0 < δ < ε/c:
- T is silent. The lower prevision cδ − ε is negative and the upper cδ + ε is positive.
- C₃ accepts g, since a·c − (c+ε) > 0. This answer is correct at worlds 1 and 3, so rank 0 at world 1.
- C₂ rejects g, since (1+δ)(c+ε) − a·c < 0.

Since X ≻₁ C₃ wherever they differ off W, and C₃ already has rank 0 at world 1 here, X = C₃ = P a.e. on R(3,2,+). There X ≠ C₂, X ≠ T and C₂ ≠ T. So C₂ is doubly exposed, and (F₃) does not touch label 2.

For w = 2, use R(3,1,+) and C₁. ∎ The regions are checked exactly in `s2_geometry.out`.

**Theorem 3 (Task 1, positive; PROVED; CHECKED).** Let 𝓡 ⊂ 𝓡_EC ∩ (F₃) contain a defender for every X ∈ X_G ∖ {T} (Lemma 2). Then R⁰ ∪ 𝓡 ∪ {σ at worlds 1 and 2} satisfies the following.
- (G), (IB), (TC), with no accepted 2- or 3-cycle through σ (Proposition 1(b)).
- σ is strict. Its reverse (A → B on G₁ ∪ G₂) is mixed at worlds 1 and 2. It is not a T-record, not TR, and not a repair, because repairs have a non-null off-guard part.
- T and every defender are undominated. This is the special case ℰ = {σ} of Lemma U (§4).
- There are no new ties, so direct (C) and (LA) hold.
- T is competitive against X_G ∪ {Y}. Every X ∈ X_G ∖ {T} is strictly dominated at every world by an undominated defender.

*CHECKED* (`s4_cells.out`, E1 with (F₃)): 0 violations with σ at either world, and 0 X_G-rivals without a defender.

---

## 3. The cycle classification

**Setting.** R = R⁰ ∪ 𝓡 ∪ ℰ, where:
- 𝓡 ⊂ 𝓡_EC is arbitrary;
- ℰ = (ℰ_w)_w, and ℰ_w is a set of T-records each of which breaks G_w;
- everything is installed with all copies; ℰ_w only at world w.

**Theorem C (PROVED).** Let Γ be an accepted cycle of length 2 or 3 at world w that contains a non-guidance link. Then Γ consists of:
- exactly one repair R = rec(C, X), of label i ≠ w;
- exactly one ρ = (D, T|D, N) ∈ ℰ_w that fully converts G_l, where l ∉ {i, w};
- one guidance link (possibly the identity).

Write E = D_R ∖ W and D_U = D ∖ W. In one of the two cyclic orders, the following hold.
- **(O1)** Order R, ρ, guidance:
  - X = T and N ⪰_w C on E ∩ D_U;
  - X ≻_w C on E ∖ D_U;
  - N ≻_w T on D_U ∖ E;
  - N ∈ {S, A} on D ∩ W.
- **(O2)** Order R, guidance, ρ:
  - N = C and X ⪰_w T on E ∩ D_U;
  - X ≻_w C on E ∖ D_U;
  - N ≻_w T on D_U ∖ E;
  - N = A on D ∩ (G_w ∪ G_l), and N ∈ {S, A} on D ∩ G_i.

Conversely, if R ∈ 𝓡 and ρ ∈ ℰ_w satisfy (O1) or (O2), then R ∪ ρ ∪ guidance contains a (TC) violation at w. It is forced: the guidance link closes it strictly, because by (E_T) it is non-trivial on E ∩ {X ≠ T} ⊂ E ∖ D_U.

*Proof.* Classify Γ by the number of repairs.
1. **No repair.** Take a non-guidance link λ ∈ TR ∪ ℰ_w, and a problem g where λ raises the w-rank above r_w(T(g)). This exists: for TR by definition, for ρ ∈ ℰ_w on D ∩ G_w, where T = B has rank 0. Afterwards guidance only raises the rank, and T-records act at g only when the advice is T(g). So the advice never returns. (This is Lemma 3's argument.)
2. **Two or more repairs.** Two of them are adjacent, which Theorem 2's noncomposition forbids.
3. **One repair R (label i) and two T-links (TR or ℰ).** By (E_T), E ∩ {X ≠ T} is non-null. There the advice after R is X ≠ T, and T-links cannot move it. It never returns to C.
4. **R, TR and guidance.** Theorem 2's argument: on G_k (k ∉ {i, w}), R contributes +2 at w and the other links contribute ≥ 0.
5. **R, ρ ∈ ℰ_w and guidance.**
   - *w ≠ i.* If w = i, ρ raises the rank on part of G_i = G_w. R is the identity there and guidance cannot lower it.
   - *ρ fully converts G_l.* On G_l (l ∉ {i, w}), R moves A → B, from rank 0 to 2. Returning needs B → A on all of G_l. Guidance cannot lower rank, and S → A is also a decrease at w. So ρ itself must move B → A on all of G_l.
   - *(O1) and (O2).* Write the two cyclic orders out pointwise, as in Proposition 1(a). The context is free off D_R ∪ D, and set to T there whenever ρ must apply. This gives exactly (O1) and (O2). ∎

**Corollaries.**
- **C1.** If ρ fully converts neither non-w guard, no cycle passes through ρ, for every 𝓡 ⊂ 𝓡_EC.
- **C2.** Suppose ρ is weakly worse than T at w off the guards: N ⪯_w T on D_U. Then (O1) and (O2) both force D_U ⊂ E and X ≻_w C on all of E. In (O2), C = N ⪯_w T ⪯_w X on E ∩ D_U. So R is (i,w)-improving with i ∉ {w, l}.
  - Proposition 1 is the case ρ = σ.
- **C3 (per-record test).** For a fixed installed 𝓡, T ⪯_w Y is (TC)-compatible iff no R ∈ 𝓡 satisfies (O1) or (O2) with ρ = rec(T, Y). This is the guard version of REFEREE_guard F2's record test.

---

## 4. Theorem P: an explicit extended rule

**Rule ETR⁺.** At world w, accept (with all copies) every T-record ρ = (D, T|D, N) that breaks G_w and satisfies one of:
- **(i)** for each l ≠ w, ρ does not fully convert G_l;
- **(ii)** N ⪯_w T a.e. on D ∖ W.

**Filter (F*).** Install no (i,w)-improving repair, for any i and any w ≠ i.

**Lemma U (undominatedness; PROVED).** Let C be an i-defender that is ≥_i T pointwise. Then C is undominated in R⁰ ∪ 𝓡 ∪ ℰ for every 𝓡 ⊂ 𝓡_EC and every family ℰ of T-records accepted only at worlds whose guard they break.

*Proof.* Suppose Z ≺_w C at every w.
1. **World i.** Z ⪯_i C is not a repair copy, because repairs never end at defenders (Theorem 2). It is not a T-record copy:
   - a TR copy would need C to be worse than T at i somewhere;
   - an ℰ_i copy would need its new side C to differ from B on G_i, but C = B there.

   So Z ⪯_i C is guidance.
2. **Other worlds.** If some Z ⪯_j C is a T-record copy, then Z = T on D(Z, C). Guidance at i then gives C ⪯_i T there. Together with C ≥_i T this forces C = T on D, which is impossible. So every incoming link is guidance.
3. **Conclusion.** Z would be weakly better than the regular model C at all three worlds pointwise, and the 2/1/1 weighted rank identity excludes that. ∎

T is undominated too:
- no repair copy ends at T, by (E_T);
- no T-record copy ends at T, since its new side differs from T on D;
- so only guidance enters T.

**Lemma 4* (defender existence under (F*); PROVED, §5).** Every X ∈ X_G ∖ {T} has a doubly exposed defender among C₁, C₂, C₃ that is not (j,w)-improving for any w ≠ j.

**Theorem P (PROVED).** Let 𝓡 ⊂ 𝓡_EC ∩ (F*) contain a defender of every X ∈ X_G ∖ {T}. Let R := R⁰ ∪ 𝓡 ∪ ETR⁺. Then:
1. **(G), (IB).**
   - Every ETR⁺ record breaks G_w, so it strictly worsens at w and is never a strict improvement there.
   - Repairs satisfy (G) by Theorem 2.
   - Every rule is record-based.
2. **(TC).** There is no accepted 2- or 3-cycle through a non-guidance link.
   - Cycles through type (i) records: Corollary C1.
   - Cycles through type (ii) records: Corollary C2 and (F*).
   - Everything else: Lemma 3 and Theorem 2.
3. **Strictness and ties.**
   - The reverse of an ETR⁺ record is not guidance: T is strictly better on D ∩ G_w. It is not a T-record, and it is not a repair (its new side T would violate (E_T)).
   - So there are no new ties. Direct (C) holds via the absence of distinct all-world ties, and so does (LA).
4. **Undominatedness.** T and C₁, C₂, C₃ are undominated (Lemma U).
5. **Coverage.** Every X ∈ X_G ∖ {T} is strictly dominated at every world by an undominated defender (Lemma 4* and Theorem 2).
6. **Competitiveness.** T ⪯ Y at some world for every Y ∈ X_G (Lemma 3) and every guard-changing Y outside 𝒵.
   - *Pure guard changes are outside 𝒵.* If Y is majority a.e. on at most one guard, take w to be that guard (or any broken guard); then type (i) holds. Otherwise type (ii) holds at any broken w, because Y = T off W.
   - *Outside 𝒵 in general.* Either type (i) holds at some broken guard, or type (ii) does.

**Sharpness (PROVED).**
- (F*) is exactly the set of repairs that conflict with ETR⁺.
- If R is (i,w)-improving, the pure guard rival T + A on G_w ∪ G_l (l ∉ {i, w}) has σ_{w,l} = (G_w ∪ G_l, B, A) ∈ ETR⁺_w of type (ii). Proposition 1(a) gives the forced triangle.
- Type (i) records need no filter beyond (E_T) and (E_C).

**CHECKED** (`s4b_etrplus.out`, `s4_cells.out`; all 6561 models on 8 cells, every relation computed in full):

| configuration | (TC) violations | strict-(G) violations | T / C₁, C₂, C₃ dominated | T undefended against |
|---|---|---|---|---|
| (E_T, E_C)-repairs + ETR⁺(i) | 0 at every world | 0 | no / no | 513 (346 outside 𝒵) |
| (F*)-repairs + ETR⁺(i) + ETR⁺(ii) | 0 at every world | 0 | no / no | 167 = \|𝒵\| (0 outside 𝒵) |
| (E_T, E_C)-repairs + ETR⁻ (type (ii) only, no (F*)) | 19,843 / 19,843 / 9,407 | 0 | no / no | — |

---

## 5. Proof of Lemma 4*

Fix X ∈ X_G ∖ {T}. Write IMP(j, w) for "(C_j, X) is (j,w)-improving", i.e. X ≻_w C_j a.e. on {X ≠ C_j} ∖ W. Call C_j *valid* if it is doubly exposed and IMP(j, w) fails for both w ≠ j.

The forcing principle used throughout: if IMP(j, w) holds and C_j's answer is correct at w (rank 0) on a non-null set off W, then X = C_j a.e. there.

**Regions.** Let {j, k, w} = {1, 2, 3}. Choose δ < ε/c and η > 0 small. All regions are open, lie off W, and are checked exactly at ε = 3/10, a = 20 (`s2_geometry.out`).
- **R(j,k,+w)**, around g_j = 1, g_k = −1, g_w = δ: T = S; C_j = P, correct at j and w; C_k = N.
- **Q(j,w,k)**, around g_j = 1, g_w = η, g_k = −t with (c+ε)(1+aη)/c < t < ac/(c+ε):
  - C_j = P, which is correct at w;
  - C_w = N, which is correct at k.
  - The t-interval is non-empty because a > ((c+ε)/c)².
- **E1(j,k,w)**, around g_j = 1, g_k = −t, g_w = −η with (c+ε)/(ac) < t < c/(c+ε):
  - T = P; C_k = N, which is correct at w;
  - for η in an open interval, C_w = S.
- **E2(j,k,w)**, around (g_j, g_k, g_w) = (1, −1, η) with η < ε/(ac): T = S; C_j = P, correct at w; C_w = S.
- **E3(j,k,w)**, around (g_k, g_j, g_w) = (1, −1, η): T = S; C_k = P, correct at w; C_w = S.

**L-C. If IMP(j, w), then C_k is doubly exposed (k the third index).** On R(j,k,+w), X = P. There P ≠ C_k = N and P ≠ T = S, and C_k ≠ T.

**L-B. The cyclic case is impossible: IMP(j, w) and IMP(w, k) cannot both hold.** On Q(j,w,k), IMP(j, w) forces X = P and IMP(w, k) forces X = N.

**L-A. If IMP(j, w) and IMP(k, w), then C_w is valid.**
- *Exposure, on E1.* IMP(k, w) forces X = N. There N ≠ C_w = S, N ≠ T = P, and C_w ≠ T. So both exposures hold.
- *Not k-improving, on E2.* IMP(j, w) forces X = P, while C_w = S. P is wrong at k (g_k < 0), so X is worse than C_w at k.
- *Not j-improving, on E3.* IMP(k, w) forces X = P, while C_w = S. P is wrong at j.

**Assembly.** Suppose no C_j is valid.
1. Lemma 4 gives a doubly exposed j₀, so IMP(j₀, w₀) for some w₀ ≠ j₀. Let k₀ be the third index.
2. By L-C, k₀ is doubly exposed, so IMP(k₀, w₁) with w₁ ∈ {j₀, w₀}.
3. If w₁ = w₀, L-A makes C_{w₀} valid, a contradiction. So IMP(k₀, j₀).
4. By L-C applied to (k₀, j₀), w₀ is doubly exposed, so IMP(w₀, w₂) with w₂ ∈ {k₀, j₀}.
5. If w₂ = j₀, L-A makes C_{j₀} valid, a contradiction.
6. So w₂ = k₀. Then IMP(j₀, w₀) and IMP(w₀, k₀) hold together, which L-B forbids. ∎

**CHECKED** (`s1_lemma4star.out`).
- The full arrangement of the 15 lines generated by the vertices of M, K₁, K₂, K₃ and e₁, e₂, e₃ has 97 cells. The enumeration is exact: every vertex is perturbed in 48 directions, and 2·10⁴ random points find no new cells (`s0_cells.out`).
- I searched by exact SAT for a cell-wise rival X ≠ T with no valid defender. This is WLOG cell-wise; see the script docstring.
- The search is UNSAT for a = 20 and a = 6, for no filter, for (F₃), and for (F*).
- The cyclic case has 27 cells with empty admissible domain (`explore_cyclic.out`).

---

## 6. Theorem O: the exact obstruction

**Lemma O0 (the guards force V-separation; PROVED).** Let G_k contain the direction γ_k = L e_k − (𝟙 − e_k), with L > (1−c)/c as the note requires. Then:
- every 1- or 2-defender has m₃ < 1/(L+1) < c on its credal set;
- every 3-defender has m₃ > 1 − 2/(L+1) > c + ε.

*Proof.* An i-defender gives the majority answer on γ_k (k ≠ i) iff m·γ_k = (L+1)m_k − 1 < 0. Also 1 − 2c = c + ε. ∎ (`s2_geometry.out`: 1/6 < 7/30 < 8/15 < 2/3.)

**Construction.** Fix θ ∈ (c, c+ε), put L₀ := (1−θ)/θ and g₀ := (1, 1, −L₀), so that m·g₀ = 1 − m₃/θ.
- T is silent at g₀, because θ lies strictly inside M's m₃-range.
- Every 1- or 2-defender gives A at g₀ (it accepts g₀; A is correct at worlds 1 and 2).
- Every 3-defender gives B.
- These are strict, so they hold on a small open cone F around g₀, and F ∩ W = ∅ since T is silent there.

Put X_F := T on F^c and A on F. Then X_F ∈ X_G, and X_F strictly improves T at worlds 1 and 2.

**Lemma O1 (forced exposure; PROVED).** Suppose (IB) holds and T is undominated. If Q ⪯_w X_F strictly at every world, then Q ≠ X_F on a non-null part of F.

*Proof.* Otherwise D := D(Q, X_F) ⊂ F^c, where X_F = T. The copy of (D, Q, T) in the context Z := T with Q on D gives Z ⪯_w T at every world. Strictness transfers by (IB). So T would be dominated. ∎

In particular, X_F's exposed defenders are exactly the 3-defenders. By Lemma R1 and the patch F (where a 3-defender says B, worse than T's S at worlds 1 and 2), every 3-defender undominated in R⁰ is 3-oriented.

**Theorem O (PROVED).** Let R satisfy (G) and (TC). Suppose R contains C ⪯₁ X_F and C ⪯₂ X_F with all (IB) copies, where:
- C is 3-oriented;
- C ≠ A on a non-null part of F;
- C ≠ T off F.

Let Y_C := C on F^c and T on F. Then T ⪯_w Y_C fails at all three worlds.

If C is a guard defender, Y_C gives A on G₁ ∪ G₂, so it is guard-changing; it lies in 𝒵.

*Proof.*
- **w = 3.** C ≥₃ T everywhere. Off W this is orientation. On W, C gives A on G₁ and G₂, which is correct at 3, and B = T on G₃. So Y_C strictly improves T at world 3, and strict (G) refuses T ⪯₃ Y_C.
- **w ∈ {1, 2}.**
  1. Suppose T ⪯_w Y_C. Its record is ρ = ({C ≠ T} ∖ F, T, C).
  2. X_F = T off F, so ρ has a copy X_F ⪯_w P₂, where P₂ := C off F and A on F.
  3. Hence C ⪯_w X_F ⪯_w P₂.
  4. P₂ differs from C only on F ∩ {C ≠ A}, where A is correct at w. So P₂ strictly improves C at w, and P₂ ≺_w C by (G). This violates (TC). ∎

**Corollary O2 (PROVED).** Consider any extension of the guard architecture that repairs X_F by a guard defender, as Theorem 2's covering claim and KKM require. This covers:
- any defender pool in V₁ ∪ V₂ ∪ V₃ of any concentration;
- any filter;
- any allocation;
- any further record rule, nested guard triples, or record-dependent guards.

In every such extension that also satisfies (G) and (TC), T is non-competitive against a guard-changing rival. So (S) fails with T selected. If T is undominated and there are no distinct all-world ties, (S) fails outright, by the KKM argument of the note's §13.

**Relation to REFEREE_guard F1.**
- F1's rival X* = T + S on a set E ⊂ M₃ where C₁ and C₂ happen to be silent. E depends on a, so a more concentrated 1-defender exposes X*. This was the referee's proposed escape 1.
- F uses only V-separation, which the guards themselves force. So no pool escapes.
- The reserved-world proposal (escape 2) fails too: X_F improves T at worlds 1 and 2, yet its only exposed defenders are labelled 3.

**The exact escape (PROVED).** Let Q be an all-world dominator of X_F that is undominated in R⁰, so oriented at some world.
- If Q is 3-oriented, Theorem O applies.
- So Q must be 1- or 2-oriented. On F that means Q ∈ {S, A}, and by Lemma O1, Q = S on a non-null part of F.
- If Q is coherent, its credal set straddles a line m₃ = θ′ near θ, so it lies in none of V₁, V₂, V₃.
- Q ∉ X_G, since otherwise the note's theorem dominates it. So Q breaks a guard.
- This must happen for every θ ∈ (c, c+ε), and by symmetry for every coordinate.

So any covering extension with the target-reference base needs a *continuum of intermediate selected models*: posterior-family-like models, 1- or 2-oriented, crossing every level m₃ = θ, θ ∈ (c, c+ε). Their records have no shared full-guard transition, so Theorem 2's (TC) proof does not apply to them.

**CHECKED** (`s4_cells.out`, E4):
- X_F's only filtered exposed defender is C₃;
- adding T ⪯_w Y_{C₃} gives 21 forced (TC) violations at worlds 1 and 2, and at world 3 strict-(G) violations plus forced ones.

---

## 7. The three suggested candidates

**(i) Extended target reference with a world-i veto.**
- *Literal reading* (world i vetoes when T's minority commitment on G_i is broken): the §13 Y breaks G₁ and G₂. Both possible defences are vetoed, and world 3 is refused by (G). So the rule defends nothing in Task 1.
- *Theorem C shows the opposite logic.* Breaking G_w is what makes a T-record safe at w, because it excludes label-w repairs and supplies the first-return worsening. The danger is full conversion of the *other* guards. The correct version is ETR⁺ (Theorem P). Its limit is Theorem O.

**(ii) Nested or hierarchical guards.**
- Theorem O uses no property of the guards beyond V-separation, which holds for every level built as in §2. So it applies to every level at once.
- Also:
  - (α) Rivals that change every triple exist, so "a rival changing one triple preserves another" fails as a covering principle. AAA on every guard is an example.
  - (β) A second level's target-reference base accepts first-level guard records such as σ at any world with a worsening. That is more permissive than ETR⁻, so Proposition 1's block reappears unless the first-level repairs carry (F*).

**(iii) Guard sets depending on the record.**
- Theorem O does not mention the guards.
- Independently, record-dependent guards lose the shared full-guard transition behind Theorem 2's noncomposition. Two repairs can then compose, by PP13 §4's precision-window mechanism.

**Positive outcome.** Theorem P is the record-based rule that works: guidance + TR + (F*)-repairs + ETR⁺. It is exact in the following sense:
- type (i) is free;
- type (ii) costs exactly (F*);
- in the residual class 𝒵 the test is C3. At least the rivals Y_C of Theorem O fail it for every allocation.

Whether a cleverer allocation of repairs defends more of 𝒵 is **OPEN**. A Y ∈ 𝒵 is blocked by a forced repair rec(C, X_F) iff Y's off-guard w-gain set contains C's w-gain set over T, by (O1) and (O2). So only rivals with large gains are blocked by the forced repairs.

---

## 8. Part 3: KKM dominators for guard-changing rivals

Every guard-changing Y also needs a selected Q with Q ⪯_w Y at all w.

**Proposition K1 (PROVED).** Let R satisfy strict (G) and (TC) and contain TR at w. Let ν = (D, Q|D, T|D) with D ⊂ U. Suppose Q ≻_w T on a non-null A ⊂ D and Q ≺_w T on a non-null B ⊂ D. Then ν ∉ R_w.

*Proof.* Split B = B₁ ⊔ B₂ into non-null parts.
1. **A forced acceptance.** Cycle: (Q on D) →ν (T on D) →TR(B₁) (Q on B₁, T on D∖B₁) →TR(D∖B₁) (Q on D). (TC) applied to this 3-cycle forces the reverse of its middle link, (B₁, Q, T), into R_w.
2. **The violation.** T ⪯_w T + Q|_{A∪B₁} by TR (worse on B₁). Then ⪯_w T + Q|_A by the forced record. And T + Q|_A ≺_w T by strict (G). ∎

**Proposition K2 (PROVED).** Let Y be a pure guard change (Y = T off W) and Q any model. Let D_W := W ∩ {Q ≠ Y} ≠ ∅ and D_U := U ∩ {Q ≠ T}. If Q ≺_w T somewhere on D_U, and Y ⪰_w Q pointwise on D_W, then rec(Q, Y) ∉ R_w in any (G) + (TC) relation containing TR.

*Proof.* Q ⪯_w Y (the record), then Y ⪯_w P₂ := Y with Q on D_U (TR). P₂ differs from Q only on D_W, where it is weakly better and not equal. So P₂ ≺_w Q. ∎

**Corollary K3 (PROVED).** Let Q be a concentrated i-defender. It is oriented only at i: it is strictly worse than T at each j ≠ i on an open off-guard set (REFEREE R1). Then:
- At w ≠ i, Q must be w-better than Y somewhere on D_W. On the guards Q is w-best only on G_k (k ∉ {i, w}), where it says A.
- So rec(Q, Y) at both worlds w ≠ i requires **N_i**: Y ≠ A on non-null parts of both G_k, k ≠ i.
- If Y|W = Q|W, K1 applies instead.
- A pure guard change that is majority a.e. on two guards satisfies no N_i, so **no concentrated defender can dominate it**. For the §13 Y:
  - C₃ has Y's guard pattern, so its record with Y is a reverse target record. K1 refuses it at worlds 1 and 2.
  - C₁ and C₂ fail at world 3 by K2: Y is optimal at world 3 on the guards.

*CHECKED* (`s5_kkm_C.out`, E5, cell set C; set B in `s5_kkm_B.out` gives the same verdicts with larger counts):

| repair added at all worlds | world 1 | world 2 | world 3 |
|---|---|---|---|
| rec(C₁, Y) | 0 | 0 | 72 forced violations |
| rec(C₂, Y) | 0 | 0 | 72 forced violations |
| rec(C₃, Y) | 1,458 forced | 1,458 forced | 0 |
| rec(Q_b, Y) | 0 | 0 | 0 |

**A posterior tilt that passes (CHECKED on cells only).**
- Q_b = Φ_{(1,1,b)}(T) with b = 44/25 (ε = 3/10, L = 5).
- It is 3-oriented, and silent on part of G₁ and part of G₂ (`s2_geometry.out`, cells G1a and G2a).
- It passes K2 at worlds 1 and 2 through those silent parts, and K2 at 3 by orientation.
- It is not in X_G, and it is undominated by Lemma U's argument (ETR at 3 cannot end at it, since it gives B on G₃).

In the 8-cell abstraction with the cells where each C_i beats T at the other worlds (set C):
- the rule "rec(C_i, Y) for every pure guard change Y satisfying N_i, with Y ≠ T on part of the disagreement, and not refused by strict (G)" covers 223 of 242 pure guard changes;
- Q_b covers 15 more;
- together with ETR⁻ and the (F*)-repairs this gives **0** violations, and T, C_i and Q_b stay undominated;
- the 4 left over are the (1,3)-analogue of the §13 Y. They need the e₂-tilt, which the cell set does not represent.

**Limits of that evidence.**
- *Cell set B* (no cell where C₃ beats T at world 2): forced violations appear. These come from κ ∘ ETR compositions. The safe set C relies on the cells where C_i is strictly better than T at the other worlds.
- *Explicit conflict with type (i) defences* (`s6_kkm_conflict.out`):
  - Take Y = S on G1a, A on G2a and G3a, T elsewhere. It satisfies N₁.
  - Its repair κ = rec(C₁, Y), followed by the type-(i) ETR⁺ record that restores C₁ on G2b, G3b and O4, gives a strict world-2 improvement of C₁. So C₁ ⪯₂ Y ⪯₂ P₂ ≺₂ C₁.
  - So the concentrated KKM repairs coexist with T's type-(ii) defences on cells, but not with all type-(i) defences.
- *Note.* That T-record could be used at world 3 instead, so this is an allocation conflict, not yet a forced impossibility.

**Status of Part 3.**
- The C_i cannot be installed for rivals that are majority on two guards. This is PROVED and exact (K1–K3), and it includes the §13 Y.
- An intermediate posterior tilt passes for the §13 Y on cells. A continuum KKM rule for guard changes that keeps Theorem P's defences is **OPEN**.
- Theorem O already shows that no full (S)-system exists in this architecture. KKM for 𝒵-rivals is therefore moot there.
- Theorem O's escape route and Part 3 point the same way: **intermediate defenders**, i.e. posterior tilts that straddle guard and cut lines.

---

## 9. Summary and nearby targets

| question | answer | label |
|---|---|---|
| Defences of T against the §13 Y | σ at world 1 or 2 only | PROVED |
| Blocks | exactly the (3,w)-improving repairs; forced; (E_C) misses them (non-T context) | PROVED, CHECKED |
| Removable by a further filter keeping Lemma 4? | yes, (F₃); Lemma 2 | PROVED, CHECKED |
| Record rule for guard changes | ETR⁺ + (F*) (Theorem P); all axioms; T competitive outside 𝒵 | PROVED, CHECKED |
| Exact obstruction | Theorem O: Y_C ∈ 𝒵 undefendable in every (G) + (TC) extension of the guard architecture | PROVED, CHECKED |
| Candidates (i)–(iii) | (i) as stated fails at Y, corrected = Theorem P; (ii), (iii) do not touch Theorem O | PROVED |
| KKM by C_i for guard changes | impossible for rivals majority on two guards (incl. the §13 Y) | PROVED, CHECKED |
| KKM by another posterior tilt | intermediate e₃-tilt works for the §13 Y on cells; general rule | CHECKED (cells) / OPEN |

**Nearby reachable target (proposed).** Replace the concentrated defender pool V₁ ∪ V₂ ∪ V₃ by an intermediate family, such as the rescaled posterior family of PP13 and PP14. Every θ-cut must be straddled by a 1- or 2-oriented selected model (§6, exact escape). Two necessary design steps are now known:
- **(TC) for repairs without shared full-guard transitions.** Theorem C's structure suggests "break G_w / do not fully convert another guard" as the safe pattern.
- **A joint allocation** between T's type-(i) defences and KKM repairs (§8).

---

## 10. Scripts (`PP15_py/`)

| script → output | content | label |
|---|---|---|
| `lib15.py` | exact geometry: M, rescaled defenders, advice, ranks, arrangement cells | library |
| `s0_cells.py` → `.out` | the 97-cell line arrangement (a = 20, 6); K_i ⊂ {m_i > ½} | CHECKED |
| `s1_lemma4star.py` → `.out` | SAT: no rival without a valid defender, for no filter, (F₃), (F*) | CHECKED |
| `explore_cyclic.py` → `.out` | admissible domains under combined improvement constraints (cyclic case empty) | CHECKED |
| `s2_geometry.py` → `.out` | guards, V-separation bounds, all Lemma 4* and Theorem O regions, cell patterns incl. Q_b | CHECKED |
| `cell15.py` | exhaustive cell engine: guidance, TR, repairs with filters, ETR⁻, ETR⁺, (TC)/forced/(G)/domination checks | library |
| `s4_cells.py` → `.out` | E1 Task 1 (block, F₃); E2 Theorem P with ETR⁻; E3 necessity of (F*); E4 Theorem O | CHECKED |
| `s4b_etrplus.py` → `.out` | Theorem P with ETR⁺ = (i) ∪ (ii); undefended set = 𝒵 exactly | CHECKED |
| `s5_kkm.py` (arg `C` or `B`) → `s5_kkm_C.out`, `s5_kkm_B.out` | K1/K2 on the §13 Y; concentrated and Q_b KKM rules (cell sets C and B) | CHECKED (cells) |
| `diag_kkm.py` → `.out` | example chains for the set-B failures | diagnostic |
| `s6_kkm_conflict.py` → `.out` | explicit κ ∘ ETR⁺(i) triangle | CHECKED |

**Caveat on the cells.** The cell abstraction treats cells as atoms. It certifies the record combinatorics exactly, not the measure statements; those are proved in the text. One coverage count in `s4_cells.out` E2 (7 of 26 X_G-rivals without a defender under (F*)) is an artefact of having only three off-guard atoms. The 97-cell SAT and the proof of Lemma 4* settle coverage.

Dependencies: Python 3, numpy, pysat. Nothing is imported from other folders.
