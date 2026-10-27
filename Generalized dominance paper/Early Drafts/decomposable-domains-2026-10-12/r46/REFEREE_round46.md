# Referee report, round 46: PP23, PP24, PP25, PP26

22 October 2026. Independent referee. I read Brief 46 and the four notes, and checked the cited hypotheses in PP2 (Thm 6), REFEREE_PP2 (R1, R2), FF2 (Thm 4.1), and gate2d (Lemmas acyclic and sep, Prop three). I did not edit any note. My scripts are in `r9/PP27_py/`; each writes a `.out` file. I also re-ran 12 of the authors' scripts. All 12 reproduce their stored outputs byte for byte (`PP27_py/rerun_*.txt`).

**Labels.** PROVED: complete argument here or in the note, checked line by line. CHECKED: exact finite computation. NUMERICS: sampling. CONJECTURE: unproved.

---

## 0. Verdicts at a glance

| Note | Claim | Verdict |
|---|---|---|
| PP26 | Props 1.1–1.2 (rank identity, pencils) | correct |
| PP26 | Prop 1.3(a) (counterexample to "a region is one two-world problem") | correct; CHECKED independently (exact). It refutes only the one-coordinate reading. |
| PP26 | Prop 1.3(b)–(d), 1.4, 1.5 | correct |
| PP26 | Theorem V | correct |
| PP26 | Cor 2.1, 2.2 | correct |
| PP26 | Theorem M | correct; CHECKED independently (265 safe sets, 6 maximal = lexicographic, all with a veto) |
| PP26 | Prop 3.1, Theorem R (i)–(ii), direction-dependent rates | correct |
| PP26 | Theorem R (iii) | **correct with repair**: a capacity hypothesis is missing, and the "in particular" sentence overclaims |
| PP26 | Props 4.1, 4.2 | correct |
| PP26 | Theorem C, Prop 5.1 | correct; Theorem C CHECKED independently on cells |
| PP23 | Lemma 1.1, Theorem 2.1, Lemma 2.3, Cor 2.4, "room carried by Rule D" | correct |
| PP23 | Theorem 3.1, Prop 3.2 | correct |
| PP23 | Prop 3.3 | **correct, and stronger than stated.** Continuity in measure, T1 and FF2's import chain are not needed. Closed sections on one edge suffice (Theorem R46.1 below). |
| PP23 | Lemma 4.4, Theorem 4.5 | correct. One addition: Theorem 4.5 systems have no single-world ties. |
| PP23 | Props 4.6, 4.7 | **wrong as stated; correct with repair.** Counterexample: an inverted departure whose B-part hugs the e_k corner. The repair adds geometric and mass hypotheses that hold for localized departures. |
| PP23 | Prop 4.8 | correct as a cell statement. Its 25 accepted departures include B-heavy ones that the repaired Prop 4.7 forbids in the continuum, so it has no evidential weight for the continuum. |
| PP25 | Theorem A | **correct with repair**: {B_n} must be a π-system, not just a generating family |
| PP25 | Theorem B, Prop D, Lemma 5, Theorem C | correct (B and C are conditional reductions, and correct as such). (B1) must be read with "for every bounded B". |
| PP25 | Lemma 6 | correct, except its last sentence, which is an unproved gloss: **unclear** |
| PP25 | FF2 caveat on Theorem A | correct, and stronger than stated (R46.1) |
| PP24 | Lemmas 2.2, 2.4, 2.5, Theorem 2.6, Lemma 3.1, Lemma 3.4′, Theorem 3.5 | correct; Lemma 3.1 also checked by NUMERICS |
| PP24 | "PP2 Thm 6 excludes (S) for this relation and for any extension keeping one world gated" | correct. The exact hypotheses are in §4.3; they are weaker than PP24 states. |
| PP24 | §7.5 "atom escape" (not on my list; adjacent) | **wrong**: already excluded by REFEREE_PP2 R1 |

---

## 1. PP26 (regional lift)

### 1.1 Pencils and the counterexample

- **Props 1.1, 1.2: correct.** Write g = (−a, b, c) with s = b/(b+c). D_K rejects g iff a/(b+c) > max_K ψ_s. Lines with the same s meet the extended edge line {m_1 = 0} at one point outside [e_2,e_3]. So the pencil structure and the interval form are right.
- **Prop 1.3(a): correct.** CHECKED exactly (`geometry_checks.py` (1)):
  - K and K′ have identical ratio ranges [1,2] × [1,2];
  - on (−7/2, 1, 1), D_K = S and D_{K′} = B.
  - Scope: this refutes the reading "D_K|M_k is an interval of one coordinate". It does not refute the lead's rank statement, which Prop 1.1 confirms and PP24's Lemma 2.5 uses.
- **Prop 1.3(b): correct.**
  - The proof is written for the highest point; the lowest point is symmetric.
  - "Determined by the edge projections" should be read as "D_K|M_1 = D_{conv{lo,hi}}|M_1". The proof gives exactly that.
- **Prop 1.3(c): correct** (CHECKED exactly: T1 is B and the box model is S on (−776/175, 1, 1)).
- **Prop 1.3(d): correct.**
- **Prop 1.4 (median rule): correct.** Inclusion holds iff both ratio differences have one sign, i.e. iff δ_k is not strictly between the other two.
  - CHECKED on 300 exact random pairs: the ratio test and the median prediction agree in every case.
  - NUMERICS: in 220 of the 300 predicted crossings both crossing directions were sampled.
- **Prop 1.5: correct.** The endpoints are linear in t with common limit g_1, so each changes sign at most once.

### 1.2 Theorem V (veto regions kill (S)) — correct

I checked both cases line by line.

- **(V-own).**
  - The record C → X with X = (B, B, A) has pattern (I/T, W/T, I/T) at i.
  - Every pattern with I on M_i is refused, by the veto or by strict (G). So C = B a.e. on M_i, and C = V_i by Lemma 0.
  - X is then a strict world-j improvement of V_i.
- **(V-maj).**
  - The veto and strict (G) give C = A on M_f.
  - X = AAA is then a weak world-f improvement of C everywhere, and strict (G) at f forces C = X, which is incoherent.

Uses: KKM from (S) (closed sections, competitiveness on supp p at every p of the closed simplex), coherence of the selected models, and strict (G) at two worlds. Not used: transitivity, (TC), (IB), absence of ties, continuity.

One scope remark: a veto must refuse *every* record of the pattern, at every mass. The theorem says nothing about mass-sensitive rules. PP26 says so itself (§7).

### 1.3 Theorem M (mass-blind rules) — correct

- The realisability criterion is right: on each region the three entries are all T or contain both W and I. The refined 2-step pump (x followed by a partial undo, swap(x)) is a realisable triangle closed by guidance. So a safe set contains no swap pair, and every accepted realisable triangle lacks a reverse.
- I re-enumerated from scratch (`thmM_enum.py`, exact):
  - 265 safe subsets of the 12 mixed patterns;
  - the 6 maximal ones are exactly the 6 lexicographic orders;
  - 0 safe sets lack a veto region.
- This agrees with `bitlevel.out`.
- Theorem M constrains only the verdict on records that are trivial on U and region-pure. Other records can only add constraints, so the conclusions are monotone, as claimed.

### 1.4 Theorem R (linear region weights)

**Prop 3.1: correct.** With unequal weights, rescale the masses: 2w_2 m′ = w_1 m and 2w_1 m″ = w_2 m′ give m″ = m/4.

**Theorem R (i)–(ii): correct.**
- Pump lower bound: σ_i ≥ 1.
- Collatz–Wielandt:
  - the A-ward rival is refused everywhere for some m > 0 iff ρ(SB) > 1;
  - the B-ward rival is refused everywhere for some m > 0 iff ρ(S⁻¹B) < 1.
- B has a zero diagonal and positive off-diagonal entries, so it is irreducible. Strict monotonicity of the Perron root then forces S = I and ρ(B) = 1.
- NUMERICS: 3,000/3,000 (`misc_checks.py` (2)).
- The direction-dependent remark (σ^A σ^B = 1) is correct by the same computation.

**Theorem R (iii): correct with repair.**
- **The gap.** The proof needs a step set C on the untouched region M_{r′} with f(A) ≤ f(C) < f(B). The f-mass available on M_{r′} is at most cap_i(r′) := (Σ_j f_{i,r′,j}) μ(M_{r′}). That bound uses an (IB) copy whose context has rank 0 on M_{r′}, so the proof also uses (IB), which PP26 does not list.
- **Where it bites.** Theorem R's hypotheses do not bound the weights on M_{r′} from below relative to the other regions. Item (ii) constrains only f_{i,i,2} and f_{i,r,1}. So for a heavy record, f(A) > cap_i(r′) is possible, and the construction is unavailable.
  - I have no counterexample to (iii) itself; this is a gap in the proof.
- **Repair (PROVED).** (iii) holds for every accepted record supported in at most two regions with f_i(added) < cap_i(r′). It also holds for single-region records with f_i(added) < cap_i(r′) + cap_i(r″). This covers every record of small ν-mass, which is the local case that matters.
- **The "in particular" sentence.** "Every local comparison at every world is endorsed by one positive region-constant field" overclaims. Records with mixed parts in all three regions are not covered, as the Remarks themselves concede. Replace "every local comparison" with "every accepted comparison supported in at most two regions, below capacity".

### 1.5 §4 (Props 4.1, 4.2): correct

- The band construction turns any lexicographic or AND lift with fixed regional gate keys into a fixed-key weak gate.
- At a band edge, Lemma 6.1's X_c is exactly (B, B, A) or AAA. I checked all three orders.
- Prop 4.2 is a genuine strengthening: it needs no non-constancy of the key.

### 1.6 Theorem C (chain lift Λ) and Prop 5.1 — correct

**Λ's verdicts.**
- (IB): the verdict is a function of the first nontrivial region and the regional record.
- Strict (G): the first nontrivial region of a weak improvement carries a pure improvement. A pure improvement fails the gate clause (Φ < 0, or added is null).

**Acyclicity.**
- A cycle restricted to its earliest touched region is a cycle of one regional relation.
- Each regional relation is gate2d's guidance plus strong gate with a fixed key with null level sets. gate2d's window argument applies verbatim.
- The level sets of θ lie in finitely many planes {v·g = 0}, v a vertex of K_t, so they are null.

**The threshold property.**
- By Prop 1.5, on each (region, side) the membership of a step is monotone in t, with one direction per side.
- So U_side(C_t) = {key > t} or {key ≥ −t} up to null sets, with the never-switching steps and the level-3 steps placed correctly.
- The two sides of a region are complements with levels swapped, and they switch at the same time. So "threshold at one side" ⟺ "threshold at the other", for regular models.

**Competitiveness.** The regional count gives Φ_maj + Φ_min = a + b + 2c_maj + 2c_min ≥ 0:
- a regular change adds at one side exactly what it removes at the other;
- a change to contradiction adds 4 steps and removes none.

**Undominatedness.** Passing into a threshold set at both sides forces pointwise weak improvement at both sides. That is impossible for a different advice, since the rank pairs are (0,2), (1,1), (2,0), (3,3).

**Non-endorsement.** Correct: Lebesgue points of f on both sides of a smooth switching surface, with μ(R) = 2μ(Q).

**Independent check** (CHECKED, `chain_lift_cells.py`; my own implementation, not the authors'). One U direction plus 2 or 3 directions per region, exact switching times, all 4⁷ or 4¹⁰ models, 5 seeds:
- 0 competitiveness failures;
- 0 models weakly dominating a chain member;
- 0 strict or weak (G) violations;
- 0 2- or 3-cycles on pools of 350–400 models.
- Control: e_2-leg models fail (96, 32 and 49,664 uncovered rivals in three of the five seeds; in two seeds the cells happen not to separate the leg from the chain).

**Prop 5.1: correct.** gate2d's Prop (three) transfers because Λ judges a rival supported in M_k by M_k alone. Its gate failure at a side survives extra added steps (they raise the ess sup of the added set) and extra removed steps (they lower the ess inf of the removed set). The CONJECTURE (regionally nested families are at most one-dimensional) is labelled correctly.

---

## 2. PP23 (local rule)

### 2.1 Departures (Theorem 2.1, Lemma 2.3, Cor 2.4): correct

- **Lemma 1.1** is the right reduction:
  - a triangle with one guidance edge reduces to (P1);
  - one with two or three guidance edges is trivial;
  - an all-𝒜 triangle is (P2).
- **Theorem 2.1.**
  - Departures compose only on null overlaps.
  - Their composite keeps the first one's loss, so (P1) holds.
  - The closing edge of a departure triangle is a retreat, so (P2) holds vacuously.
  - CHECKED again: `departures_check.py` reproduces.
- **Lemma 2.3.**
  - q = (r|_{L∪G₁})⁻¹ is a departure with a loss on G₁, so it is accepted.
  - q·r = r|_{G₂} is a pure improvement.
  - (TC) is used, as it should be.
- **Cor 2.4.** Correct. Z is incoherent, because a coherent model differing from coherent N differs on a non-null cone (Lemma H).
- **Room carried by Rule D, flips.** Correct. The flip argument covers (P1) pairs only, and the note claims no more.

### 2.2 Ω (Theorem 3.1, Prop 3.2): correct

- The balance identity checks: s + s − 2s = 0 on M_k. A change to contradiction raises every rank, and on U the correct value is the unique 0.
- The π–λ step is valid because PP23's ψ_n include indicators of a π-system (rational boxes).
- The competitiveness argument takes n₀ minimal over all worlds, so every earlier coordinate vanishes at every world. That is what lexicographic acceptance needs.
- Prop 3.2 is the mirror argument.

### 2.3 Prop 3.3 and continuity: what follows without it

**Does FF2 Thm 4.1 need continuity?** Yes, as written. FF2's Step 2 (closed graph of q ↦ W(q)) uses continuity in measure, and Steps 3–6 depend on Step 2. Step 1 does not.

**Step 1 alone, without continuity (PROVED, FF2 Step 1).** Suppose C_q is competitive on supp q, and every accepted annulus-supported comparison out of C_q at worlds in supp q has Ω^{(0)} ≥ 0. Then C_q is a pointwise weak Bayes model of the balanced field ℓ_i = ρ_i r_i at some weight w ∈ Δ_{supp q}. The proof uses Lyapunov convexity, separation and a limit in n.
- Minor repair to Prop 3.3: integrals in this setting are taken against the Gaussian μ, so ℓ_i should be w_i r_i, not w_i r_i × density.

For the balanced field this is already decisive on the edges.

**Lemma R46.0 (PROVED; CHECKED exactly in `edge_bayes.py` (1)).** Let w ∈ [e_1, e_2]. On M_k the weighted cost of majority rank x is constant + κ_k x, with:
- κ_1 = w_2 − 2w_1;
- κ_2 = w_1 − 2w_2;
- κ_3 = w_1 + w_2 > 0.

Contradiction is never optimal, and on U the correct value is the unique optimum. Hence a coherent weak w-Bayes model is A a.e. on M_3, and:
- if κ_1 < 0, it is B on M_1, so it is V_1;
- if κ_1 > 0, it is A on M_1 and M_3, so it is V_2;
- if κ_1 = 0 (w = (1/3, 2/3, 0)), then κ_2 < 0 and it is B on M_2, so it is V_2.

At w = (1/2, 1/2, 0) there is no coherent Bayes model at all. So every C_q with q in the closed edge is V_1 or V_2.

**Theorem R46.1 (PROVED).** The following are inconsistent:
- strict (G) at worlds i and j;
- coherent C_q for q on the closed edge [e_i, e_j], competitive on supp q;
- for the single rival X := D_{[e_i,e_j]}, closed edge sections {q ∈ [e_i,e_j] : C_q ⪯_w X}, for w = i, j;
- every accepted annulus-supported comparison out of C_q, at each world in supp q, has Ω^{(0)} ≥ 0.

*Proof.*
1. By Lemma R46.0, C_q ∈ {V_i, V_j}.
2. The two closed sections cover the edge and contain e_i and e_j respectively. The edge is connected, so they meet at some q*.
3. X is S on M_i and M_j and A on M_k (CHECKED by sampling, `edge_bayes.py` (2)). So X is a strict world-j improvement of V_i and a strict world-i improvement of V_j.
4. Strict (G) refuses V_i ⪯_j X and V_j ⪯_i X, so C_{q*} can be neither. ∎

**Consequences.**
- **Prop 3.3 holds without continuity in measure, without T1 being selected, and without FF2's import chain.** Under Brief 46's (S), which has closed sections, no system whose bounded comparisons out of selected models lie in Ω, or in any subset of Ω, has a selection. Prop 3.3's status can be raised from "PROVED modulo FF2's import chain" to PROVED.
- The same applies to PP25's Theorem A rule L, whose first level is the same field.
- **What follows with neither continuity nor closed sections:** only that the selection is vertex-valued on every closed edge. In the interior, Step 1 is vacuous for this field: every regular model is weak Bayes at the uniform weight. So no contradiction follows from Step 1 alone.
- **For a general strictly guiding field,** Step 1 on an edge gives only K ⊆ [e_i, e_j] (A is strictly Bayes on M_k). The edge is then a two-world additive problem, where selections exist. So FF2's "most important open point" stays open for general fields. It is closed for Ω and L.
- **Where non-additivity must live (nearby result, PROVED).**
  - In any (S)-system, on every edge, some edge-selected model must have an accepted annulus-supported comparison at one of the edge's own worlds with Ω^{(0)} < 0.
  - Steps 2–4 of R46.1 use only C_q ∈ {V_i, V_j}. So in any (S)-system with strict (G), the selection on each closed edge is not vertex-valued, whatever the relations are.
  - A Theorem 4.5-type system (Ω-subset plus inverted departures) escapes R46.1 only if inverted departures, or other non-Ω acceptances, actually occur out of edge-selected models at the edge's worlds.

### 2.4 Lemma 4.4 and Theorem 4.5: correct

**Lemma 4.4.**
- **d·r.** Kind I forces all i-losses of d into the overlap. The losses of r are at points where b is i-correct (rank b < rank c ≤ 1 forces b correct and c = S). So in one class, r's old side equals b on all of d's i-losses there and on a non-null part of d's i-gains. Lemma 4.3 excludes this.
- **r·d.** The loss points of d force a = b (a regular, rank 2). The loss points of r force a i-correct, hence a = b again. Same contradiction.
- `entangled_check.py` reproduces.

**Theorem 4.5.** I checked every triangle type:
- guidance edge → (P1) pair, handled by Lemma 4.4 or by a disjoint union;
- a second 𝓘 edge → the third edge has a non-realizable, non-departure old side, so it must be guidance, which contradicts the kept loss;
- two 𝒞 edges → exactly (iii).

Two additions:
- **No single-world ties (PROVED).** Pairs in 𝒞 have Ω = 0 only if trivial. The inverse of a departure is never accepted. Guidance and 𝒞 cannot be mutually inverse. So each world is antisymmetric and direct (C) is vacuous.
- **Scope of "bounded".** PP23's "bounded" means supported in an annulus. Theorem 4.5(2) gives competitiveness only against annulus-supported rivals, a smaller class than PP25's "bounded set".

### 2.5 Props 4.6–4.8

**Counterexample to Props 4.6 and 4.7 as stated (PROVED).** Take k = 1, and write lines of M_1 by their edge coordinates (z_12, z_13).
- Let D^B lie on lines with z_12 ∈ (0, 1/10) and z_13 ∈ (3/10, 4/10), with ess inf z_12 = 0.
- Let D^A lie on lines in (1/2, 6/10)².
- Use radii in [1, 2], with β > α.

Then d is inverted and B-heavy, with Ω_1^{(0)}(d) = 2(α − β) < 0. Now take any x, y with x·y = d⁻¹:
- Every point of D^B carries old side B in x or in y. One of the two carries B on a piece with ess inf z_12 = 0.
- A point strictly inside the e_1-triangle of line (z_12, z_13) has m_2 < z_12. So no K ⊂ int Δ realizes that old side (`geometry_checks.py` (4)).
- So no x, y ∈ 𝒞 exist. (iii) holds for d with the full Ω covering, at every world, and d may lie in 𝓘_1 ∩ 𝓘_2 ∩ 𝓘_3.

Both conclusions (Prop 4.6's "contains x, y"; Prop 4.7's "d ∉ 𝓘_k") fail for this d.

**Repair (PROVED, by the notes' own arguments).** Add the following hypotheses on d (class k, edges toward e_j and e_l):
- (P1) ess inf_{D^B} z_kj > 0 and ess inf_{D^B} z_kl > 0, so that the B-part is realizable;
- (P2) there is ε > 0 and a non-null set of steep lines with z_kj < ess inf_{D^B} z_kj − ε and z_kl > ess sup_{D^A} z_kl + ε;
- (P3) the steep lines carry, inside an annulus, enough μ-mass to reach the needed t. For Prop 4.7 this means mass > α.

These hold whenever supp d lies on lines in a small neighbourhood of one interior line and μ(d) is small. That is the localized case Conjecture 4.9 is about.

The counterexample is harmless for room. If N = D_K, with K ⊂ int Δ, is silent on supp d, then every line of supp d meets K, so z_kj, z_kl ≥ min_K m_j, m_l > 0, and (P1) holds automatically. So corner-hugging departures never serve Theorem 4.5(4). (P2) can still fail when D^A contains lines through K that approach both e_j and e_l. In that case Props 4.6 and 4.7 are unproved, not refuted.

**Prop 4.8: correct as a cell statement; not evidence for the continuum.**
- In config `nest2` (lines (0.2, 0.2) and (0.6, 0.6) in M_1, and one M_2 line), seed 0 gives piece masses (4, 4 | 1, 3 | 5). So, for example, B on a 4-mass piece of the low line with A on the 1-mass piece of the high line is B-heavy, and it is among the "all 25 accepted".
- These lines satisfy (P1) and (P2), so in the continuum the repaired Prop 4.7 excludes such a departure at the owner world, provided the A-part is lighter than the available steep padding mass, i.e. (P3).
- The cell SAT succeeds only because the cells contain no steep padding line, as PP23's own "Omitted on cells" note says.
- So Prop 4.8 is uninformative about (iii) in the continuum. For the B-heavy part it points the wrong way.
- I did not re-run the SAT. The stored outputs are consistent with the script.

Cosmetic: the scripts call these departures "entangled", the note calls them "inverted".

---

## 3. PP25 (adversary)

**Theorem A: correct with repair.**
- Item 3 (Φ_w(r) = 0 ⇒ r trivial) needs {B_n} to be a **π-system** generating the Borel sets. A generating family is not enough.
  - CHECKED finite counterexample (`misc_checks.py` (1)): the family {12, 23, 34, 41} generates every subset of {1,2,3,4}, yet ν = (1, −1, 1, −1) vanishes on it and on the whole space.
  - Rational boxes, the note's example, are a π-system, so the repair costs nothing.
- Items 1, 2, 4 and 5 are correct. In item 4, n* is minimal over all worlds, so earlier coordinates vanish everywhere.
- The FF2 caveat is right in substance, and R46.1 strengthens it: L cannot be the local layer of any (S)-selection, continuous or not, through T1 or not.

**Theorem B: correct.**
- (B1) must be read as: for every bounded B, r|_{D∖B} is not a weak v-improvement. The note's convention gives this, but the sentence "no r has a far part that is a weak improvement" is easy to misread as the weak form.
- With that reading:
  - one bounded edge with two Guid edges → trivial far part;
  - G with Guid → contradicts (B1);
  - two G → contradicts (B2);
  - three unbounded edges with at most one G → contradicts (B1).
- **Prop D: correct.** The two G links are conic off a bounded set, so the third link is too, and Ψ_v is additive.

**Lemma 5: correct.**
- W = N[E → C] is a strict v-improvement of C, because N ≤_v C, strictly on the non-null cone {C ≠ N} ∖ E.
- Then (TC) on C ⪯ Y ⪯ W ⪯ C refuses Y ⪯_v W.

**Theorem C: correct as a conditional reduction.**
- Strictness of each domination: rec(Y, C) is not guidance by (C1) and not in G by (C2).
- Undominatedness: a G-copy into C° forces C° = N on S ∖ E and C° = y on X, which (C3) excludes. In the case where X ∩ S is non-null, conicity of {C° ≠ N} gives C° = N on S.
- No ties: (C1), (C2) and Theorem A(3).
- (TC) ⟺ (GG): Theorem B in one direction. In the other, every accepted triangle containing a G link lacks a reverse.
- All the content sits in hypotheses (C1)–(C3) and (GG). The note says so.

**Lemma 6: correct except its last sentence (unclear).**
- Correct: a.e. far point lies in two far supports; if the two G supports met only in a null set, a Guid third link would make each G far part a weak improvement; adjacent copies give the shadow N_1 = C_2.
- Unclear: "(TC) fails exactly when the cancelled part held all of one pair's compensation" is not proved. Every accepted GG triangle is already a (TC) failure, since G reverses are never accepted. The sentence describes when such a triangle *can be accepted*, with no proof. Label it heuristic.

---

## 4. PP24 (two-model family)

### 4.1 Transfer lemma and competitiveness: correct

- **Lemma 2.5.**
  - u-ward of a regular Z forces Y = Z on U and no contradiction, since the u-rank is ≤ Z's.
  - On M_{v′} (aligned) the v-rank falls below r_v(Z) ≤ r_v(T), so only T-steps are removed.
  - On M_u and M_v (opposed) it rises above r_v(Z) ≥ r_v(T), so only non-T steps are added.
  - T-anchoring separates the two: −1 > non-T keys, T-keys ≥ 0.
  - (a): a nontrivial move touches M_u, M_v or M_{v′}, and each world v ≠ u sees additions on M_u ∪ M_v.
  - (b): acceptance needs Rem_v(Y,Z) null.
- **Lemma 2.4.** Correct. In (b), null level sets make separation impossible unless one side is null.
- **Lemma 2.2.** I re-derived the window argument for the trivial verdict. The key has null level sets everywhere: exit times lie on planes, and every T-step exits before t = 1, because V_u has no world-u steps on mixed problems. So the level set {k = 1} is null.
- **Theorem 2.6 and Theorem 3.5.** Correct. Members are u-ward and threshold at u (Lemma 3.4′). C_k(δ) is phase 1 of Γ_{k+1}, so it is threshold at k + 1, and at k by the F_k keys.
- **Lemma 3.1.** NUMERICS (`geometry_checks.py` (3), 2·10⁶ Gaussian directions per value of δ):
  - at δ* and at δ*/2: 0 changes outside the claimed footprint, for each k;
  - at 1.1δ*: 108–113 changes outside it;
  - at 1.5δ*: about 2,600.
  - So the threshold is sharp, as claimed. `check_geometry.py` reproduces the exact witnesses.
- **Prop 2.7: correct.** Pieces where C is worse than T exist at every world, because C is not u-ward of T for any u. Re-adding T removes only non-T steps and adds only T-steps.

### 4.2 Hidden assumptions

None found:
- acyclicity is proved, not assumed;
- no-ties follows from it;
- the competitiveness proof uses no strict repair at every world. It splits on whether the rival is worse at u somewhere.

### 4.3 PP2 Theorem 6, and its exact hypotheses

Theorem 6, with REFEREE_PP2's R1, needs:
- **(H1)** the Gaussian three-world setting;
- **(H2′)** at one world w, with a fixed key k_w:
  - every pair (C, X) with C ≠ X is refused whenever ess inf_{T^off} k_w < ess inf_{T^on} k_w. Here C is a model selected on one of the two edges at e_w, and X is X_c or X′_c (the edge threshold models);
  - k_w(·,1) is not essentially constant on M_w;
- **(H3)** strict (G) at the other two worlds;
- **(H4)** coherent selected models, competitive on supp p at every p of the closed simplex, with closed sections for the regular rivals X_c and X′_c.

PP24's gates satisfy (H2′) at every world:
- separation with null level sets implies the strict weak gate;
- the world-u key is non-constant on M_u level-1 steps (exit times in phase 3, and F_u keys below −1).

**Why edge-selected models suffice (PROVED).** Run KKM on the edge [e_w, e_j] alone. The sections for X_c restricted to that edge are closed, they cover it (competitiveness on supp q), and they contain e_w and e_j. So they meet at an edge point q*, and Lemma 6.1 applies to C_{q*}. The edge [e_w, e_k] gives X′_c in the same way. The rest of the proof is unchanged.

So **PP24's claim is correct**, and it holds more generally than stated. An extension escapes Theorem 6 only if, at every world w, either:
- some accepted comparison *out of a model selected on an edge at e_w, into an edge threshold model* fails the fixed key's strict reverse-order test; or
- the key becomes essentially constant on that world's own-class level-1 steps.

Adding non-gated comparisons out of non-selected models does not help. Null level sets are not needed (R1).

### 4.4 PP24 §7.5 (atom escape): wrong

Collapsing world u's T-steps on M_u to an atom at key 1 leaves the non-T level-1 steps on M_u (where T = B) keyed below −1. So k_u(·,1) is not essentially constant on M_u: it takes two values, each on a non-null set.

The atom rule refuses *more* pairs, so the strict reverse-order refusal of (H2′) still holds. REFEREE_PP2 R1 then applies with c = 0: E = {T ∈ {S, A}} ∩ M_u has intermediate mass, and the strip contradiction runs unchanged.

The median step that §7.5 hopes to break is not needed (R1). REFEREE_PP2 R2 already showed that a fixed primary key survives only if it is essentially constant on *all* mixed level-1 steps. §7.5 repeats the (E2) route that REFEREE_PP2 marked wrong.

---

## 5. Hidden-assumption audit

| Assumption | Where it might hide | Finding |
|---|---|---|
| Transitivity | PP26 Thm M/R, PP23 Lemma 1.1, Thm 4.5, PP25 Thm B/C | Not used anywhere. Ω and L are transitive by construction (a property, not an assumption). |
| No single-world ties | PP23 Thm 4.5, PP25 Thm C, PP26 Thm C, PP24 Thm 3.5 | Never assumed. Absence is proved in each case, and I added it for Thm 4.5 (§2.4). |
| Continuity of the selection | PP23 Prop 3.3, PP25 Theorem A caveat (via FF2 Thm 4.1) | Used through FF2 Step 2. **Not needed** for Ω or L: closed sections on one edge suffice (R46.1). Still needed for a general field. |
| Strict repairs at every world | PP23 Cor 2.4 (N is A on all three classes); PP25 (C1); PP26 Thm R (S and A on every region); PP24 Prop 2.7 (C worse than T at every world) | Always stated as hypotheses or proved; nothing hidden. Theorem V needs strict (G) at only one second world. |
| (IB) | PP26 Thm R(iii) | Used, through a context copy, but not listed. Harmless, since it is a brief axiom. |
| Geometry of supports | PP23 Props 4.6, 4.7 | **Hidden**: steep padding, B-part bounded away from the corner, padding mass. See §2.5. |
| Capacity of the untouched region | PP26 Thm R(iii) | **Hidden**. See §1.4. |

---

## 6. What the round establishes, and nearby targets

**Firm (PROVED and refereed):**
- Local defences are cheap:
  - for every regular model: Ω and L;
  - non-additively, along chains: Λ and PP24.
- (S) is closed off for:
  - every veto lift (Theorem V);
  - every mass-blind lift (Theorem M);
  - every fixed-key gated world (PP2 Thm 6 with R1; the atom variant included);
  - every Ω- or L-endorsed edge layer (R46.1).

**The most useful new constraint is R46.1.** It moves FF2's "some world must be non-additive" from an unknown place to a known one, for the balanced field and without continuity: **the non-additive acceptances must occur out of edge-selected models, at the edge's own worlds.**

Nearby targets I would set (proposals, not results):
1. **Faces gated with edge-dependent priorities, body balanced.**
   - Interior models use Ω/L.
   - Models on the edge [e_i, e_j] use a gate2d-type gate in which world i's priority on M_i is the [e_i,e_j]-edge coordinate. World i uses a different priority for models on [e_i, e_k].
   - With one fixed key per world this is excluded by the edge form of Thm 6 (§4.3). With edge-dependent priorities (PP2's (E1)), neither R46.1 nor Thm 6 applies.
   - Obligations:
     - (IB): records into M_i ∪ M_j can have old sides that come from models on either edge at e_i, so the priority must be a function of the record;
     - (TC) has to be re-proved;
     - sections must be closed across the body/face boundary, where an integral verdict hands over to a gate verdict.
   - This is the sharpest next test.
2. **Repaired Props 4.6 and 4.7 plus Conjecture 4.9.** Restrict the room question to localized inverted departures (P1–P3). Prop 4.7 settles the B-heavy half. The A-heavy half is exactly the list-colouring question PP23 §6 poses. Cell checks must include a steep padding line, or they say nothing.
3. **PP26 (N3).** Proving that regionally nested coherent families are at most one-dimensional would close every fixed-regional-key design. Prop 1.4 already gives this for precise models.

---

## 7. Scripts (`r9/PP27_py/`)

| Script | Content | Label |
|---|---|---|
| `thmM_enum.py` | independent enumeration for Theorem M: 265 safe sets, 6 maximal = lexicographic, 0 without a veto | CHECKED (exact) |
| `edge_bayes.py` | Lemma R46.0 on a 63-point exact grid of edge weights; D_{[e1,e2]} = (S, S, A); the strict improvements used in R46.1 | CHECKED (exact) / NUMERICS (profile sampling) |
| `geometry_checks.py` | Prop 1.3 examples (exact); median rule (exact ratio test); PP24 Lemma 3.1 sharpness; corner-hugging non-realizability bound | CHECKED / NUMERICS |
| `chain_lift_cells.py` | independent implementation of Λ: competitiveness, undominatedness, strict (G), 2/3-cycles, leg control | CHECKED (cells, diagnostic) |
| `misc_checks.py` | π-system counterexample for PP25 Thm A; Theorem R covering test | CHECKED / NUMERICS |
| `rerun_*.txt` | authors' scripts re-run (PP23: 5 scripts; PP24: 2; PP25: 2; PP26: 3); all identical to stored outputs | CHECKED |
