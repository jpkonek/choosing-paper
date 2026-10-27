# PP23. A local defence rule for every coherent model, and where room for dominations can and cannot live

22 October 2026. One reader (me); not refereed.

**Labels.** PROVED: full proof here. CHECKED: exact finite computation (rational arithmetic or SAT on finite cells). Cells check record bookkeeping only. They say nothing about (S), and nothing about continuum padding beyond the pieces present. CONJECTURE / OPEN: as stated. NUMERICS: none.

**Scripts** (`r9/PP23_py/`; run `python3 -B <script>` inside the folder; outputs in the `.out` files):

| Script | Content | Label |
|---|---|---|
| `zrule_check.py` | Theorem 3.1 and Prop 3.2 on cells, full four-value domain | CHECKED |
| `departures_check.py` | §2: lead's rule passes (TC); point-4 domination; room from mixed departures | CHECKED |
| `pumpsplit.py` | Lemma 4.2: which type-sets admit a pump split | CHECKED |
| `entangled_check.py` | Lemma 4.4 (inverted departures never pump with realizable records) | CHECKED |
| `padded_triangle.py` | Prop 4.6, exact instance | CHECKED |
| `cellsat.py`, `satrun.py`, `core_tri1.py` | SAT: coverage + (TC) + strict (G) + local dominations, radially split cells | CHECKED |
| `sat_zsubset.py` | SAT: Ω-subset covering plus inverted departures at every world (Props 4.7, 4.8) | CHECKED |

**Inputs.** Brief 46; AUDIT_local_defences (Prop 1, Cor 4); PP20 (Lemma 1.3, record algebra); AUDIT_completion (rules I–IV); DESIGN_MEMO §§5, 8.5; PP2 (Prop 3, Thm 6); gate2d; FF2 (Thm 4.1, Cor 4.3). Only Brief 46's axioms are used.

---

## 0. Verdict

1. **A complete local defence rule exists (Theorem 3.1, PROVED).** I call it the balanced lexicographic rule Ω.
   - **Definition.** World i ranks models lexicographically by countably many integrals of world-i rank. The leading integral weights world i's own minority class M_i twice.
   - **What it satisfies.**
     - Strict (G); (IB) with every common-context copy; (TC).
     - Each world is a *linear order*: there are no ties at any world, so direct (C) is never threatened.
     - Every regular model, in particular every coherent D_K for every closed convex K ⊆ Δ, is competitive against every rival, bounded or not.
   - **Ties of infima.** Verdicts are integrals, never infima, so continuum ties cannot arise.
2. **But Ω leaves no room for dominations among regular models (Prop 3.2, PROVED).** It is also endorsed by an integrable strictly guiding field. By FF2 Thm 4.1 it therefore cannot be the bounded-record part of an (S)-system with a selection that is continuous in measure through T1 (Prop 3.3).
   - **Why.** The two facts have one cause: a balance identity (§1.3) that makes every regular model Bayes for the uniform weight.
   - **Answer to the brief's last question.** Ω is a correct rule, but useless for (S) on its own.
3. **The lead's departure rule (§2).**
   - **(TC) holds** with all copies (Theorem 2.1, PROVED).
   - **It is fatal as a whole rule** (Cor 2.4, PROVED). At a world that accepts every non-improving departure, no retreat with a gain at that world can be accepted (Lemma 2.3). So, if every world uses the rule, every interior coherent model is strictly dominated by one of its own bounded partial retreats.
   - **It does carry room.** It strictly dominates "mixed departures" (S→A and S→B in one class).
4. **Where room can live (§4).**
   - **Two collapse results.** These are design screens, not axiom-level theorems:
     - a world that accepts every record with positive leading Ω-value can accept nothing with negative leading value (Lemma 4.1);
     - a "pump split" kills local domination through a record under the axioms alone (Lemma 4.2). Only 3 of the 45 relevant type-sets admit one.
   - **The positive structure.**
     - *Inverted departures:* silence replaced by A on higher lines and B on lower lines of one class, the reverse of the coherent order.
     - They never pump with records whose old side is coherent-realizable (Lemma 4.4, PROVED).
     - So they can be accepted at every world on top of any covering part drawn from Ω, giving strict local dominations, **provided** one splitting condition (iii) holds (Theorem 4.5, PROVED: (TC) ⇔ (iii)).
   - **Full Ω violates (iii)** (Prop 4.6).
   - **Every Ω-subset covering violates (iii)** for inverted departures whose B-part is heavier, at the owner world (Prop 4.7, PROVED and CHECKED).
   - **On cells, (iii) is satisfiable** with all 25 inverted departures accepted everywhere (Prop 4.8, CHECKED).
   - **Open.** Whether a measurable covering with (iii) exists for the A-heavy ones (Conjecture 4.9).
5. **Gates (§5).**
   - **Fixed-key weak gates fail local defence** of interior coherent models, without (S) or sections:
     - keys depending only on radius (and on world, level, class) always tie (Lemma 5.1);
     - gate2d-type keys fall to a two-generator rival (Lemma 5.2). These are the edge coordinates at the majority worlds with a strictly decreasing owner key.
   - **Channel-shared keys** escape every strict cheap rival and can fail only through ties (Lemma 5.3). For tier keys, coverage forces this sharing. Radial shared keys do tie.
   - **PP2 Thm 6 does not apply to Ω** (its hypothesis (H2) fails); §5.4 says which hypotheses each rule meets.

**Most important next step.** Find a covering part with property (iii) that is not additive at some world (§6), or prove Conjecture 4.9 false.

---

## 1. Setting and three tools

Setting of Brief 46: three worlds; problems g ∈ R³ modulo sign; Gaussian μ; full four-advice domain; models modulo null sets.
- On a mixed problem in M_k the values are:
  - A, the majority answer: rank 0 at the two majority worlds, 2 at k;
  - S, silence: rank 1 everywhere;
  - B, the minority answer: rank 2 at the majority worlds, 0 at k;
  - X, contradiction: rank 3 everywhere.
- On unanimous problems the ranks are correct 0 < S 1 < wrong 2 < X 3.
- A model is **regular** if it is A, S or B a.e. on mixed problems and correct a.e. on U. Every coherent D_K is regular.

A **record** r = (D, a, b) has old and new advice a ≠ b a.e. on its support D. Its rank change at world i is δ_i(g) = r_i(g, b) − r_i(g, a). Since the four values have distinct ranks at every world, δ_i ≠ 0 on D. Following PP20 §1, r is of kind **W** at i if δ_i > 0 on D, of kind **I** if δ_i < 0 on D, and of kind **M** otherwise. Composition r1·r2 exists when new₁ = old₂ on the overlap of the supports. All common-context copies of a record carry the same verdict.

A record is **bounded** if its support lies, modulo null sets, in an annulus {ρ₀ < |g| < ρ₁}. Its old side is **realizable** if some D_K with K a closed convex subset of int Δ equals a a.e. on D. This is a property of the record alone.

### 1.1 (TC) in record form

**Lemma 1.1 (PROVED; PP20 Lemma 1.3 restated).** Let each world accept weak guidance and some set 𝒜_i of kind-M records, closed under copies. Then strict (G) and (TC) hold if and only if, at each world i:

- **(P1)** no two records of 𝒜_i compose to a record of kind I at i;
- **(P2)** every triangle of 𝒜_i-records has its three reverses in 𝒜_i.

*Proof.*
- A kind-W record composed with a kind-M record has a strict worsening point (PP20 Lemma 1.2). So a non-degenerate triangle with a guidance edge has its other two edges composing to a kind-I record, which is (P1).
- A triangle with a strict guidance edge needs that edge's reverse, which is a pure improvement and is forbidden.
- The remaining triangles are all-M, which is (P2).
- (TC) is equivalent to "every accepted triangle has its reverses" (AUDIT_completion §2). ∎

### 1.2 Bounded and unbounded edges

**Lemma 1.2 (PROVED; the lead's observation 2).**
- In any triangle r1·r2·r3 = id, the number of edges with unbounded support is 0, 2 or 3.
- If the only accepted unbounded records are guidance, every accepted triangle containing a kind-M bounded edge has all three edges bounded.

*Proof.*
- supp r3 ⊆ supp r1 ∪ supp r2, and cyclically. So two bounded edges force the third to be bounded, and one bounded edge forces the other two to be unbounded together.
- In the second statement, suppose a bounded M edge has two unbounded guidance partners. Those partners compose to a kind-W record, so the bounded edge is the inverse of a kind-W record. It is then of kind I or trivial, never M. ∎

So a local rule can be checked for (TC) on bounded triangles alone. It interacts with later unbounded dominations only through triangles in which exactly one edge is bounded.

### 1.3 Region coordinates and the balance identity

On M_k a regular change moves the majority rank by s ∈ {±1, ±2} and the minority rank by −s. Call a point of a record:
- **P_k** if it moves toward B (s > 0). This is a loss at the two majority worlds and a gain at k.
- **Q_k** if it moves toward A (s < 0). This is a loss at k only.

World i loses on Q_i ∪ ⋃_{k≠i} P_k and gains on the complement. This is the lead's observation 5: on each M_k there are two players, the owner k and the pair of opponents.

Put w_i(g) = 2 if g ∈ M_i and w_i(g) = 1 otherwise (including U).

**Balance identity (PROVED).** Let a be regular at g. If b is regular, Σ_i w_i(g)(r_i(g,b) − r_i(g,a)) = 0. If b = X, or g ∈ U and b is not correct, the sum is strictly positive.

*Proof.* On M_k a regular change gives s + s − 2s = 0. A change to X raises every rank. On U, the correct value has rank 0 everywhere. ∎

Everything in §3 and the collapse results in §4 come from this identity.

---

## 2. Departures: the lead's rule, its fatal defect, and its room

A **departure** has old side S throughout its support; a **retreat** has new side S throughout; a **flip** changes one answer into another.

**Rule D.** At each world i, accept guidance at i and every departure that is not a pure improvement at i.

**Theorem 2.1 (PROVED; CHECKED).** Rule D satisfies strict (G), (IB) with all copies, and (TC).

*Proof.* Use Lemma 1.1.
- *(P1).* Two departures compose only on disjoint supports, because the second needs old side S where the first has already put an answer. The composite is their union, which keeps the first one's loss at i, so it is not of kind I.
- *(P2).* Composites of departures are departures. The closing edge of a triangle of departures is the inverse of a departure, which is a retreat and never a departure. So no triangle of departures is accepted.
- Strict (G) holds because pure improvements are refused by definition. ∎

CHECKED: `departures_check.py` finds 0 (TC) violations over all 2,197 records on two three-piece cell sets with the full four-value domain.

**Lemma 2.2 (undo lemma; PROVED).** Suppose r is accepted at i. Let O ⊆ supp r contain every i-loss of r, and let g be any pure i-improvement on fresh support (possibly trivial). If q := (r|_O)⁻¹ ∪ g is nontrivial after composition with r, then q is refused at i.

*Proof.* r·q is r on supp r ∖ O, which contains only i-gains, together with g. That composite is of kind I at i, so (P1) fails if both r and q are accepted. ∎

**Lemma 2.3 (retreats under Rule D; PROVED).** If world i accepts every non-improving departure, it accepts no retreat that has a non-null i-gain.

*Proof.*
- Let r be a retreat with i-loss set L and i-gain set G, G non-null. If L is null, r is a pure improvement and is refused anyway.
- Split G into non-null G₁ ⊔ G₂ and put q := (r|_{L∪G₁})⁻¹. Then q is a departure.
- q has an i-loss on G₁: there the old value was i-wrong, because r gains there. So q is accepted.
- q·r is r|_{G₂}, a pure i-improvement, so (P1) fails. ∎

**Corollary 2.4 (Rule D at all worlds is fatal; PROVED; CHECKED).** Let N be regular and give A on non-null sets of M₁, M₂ and M₃. This holds for every coherent D_K with K ⊂ int Δ. Then N is strictly dominated at every world by a bounded incoherent rival.

*Proof.*
- Choose bounded non-null E_k ⊆ {N = A} ∩ M_k, and let Z be N with S on E₁ ∪ E₂ ∪ E₃.
- rec(Z, N) is the departure S → A. At world i it is a loss on E_i (A is wrong at the minority world), so it is accepted at every world.
- rec(N, Z) is a retreat with an i-gain on E_i, so by Lemma 2.3 it is refused at every world.
- Z is incoherent by Lemma H. ∎

CHECKED: on cells the retreat N(A,A,A) → Z(S,S,S) is accepted at no world, and its reverse at all three.

**Room carried by Rule D (PROVED).** Let E, F ⊆ M_k be non-null bounded sets where N is silent, and let X be N with A on E and B on F.
- rec(N, X) is non-improving at every world: the owner loses on E and the opponents lose on F. So it is accepted everywhere.
- Its reverse is a retreat with gains at every world (on F at the opponents, on E at the owner), so it is refused everywhere.
- So N strictly dominates X at all three worlds. CHECKED on cells.

**Flips (PROVED).** A departure and a flip never form a (P1) pair unless the flip is itself a pure improvement.
- Departure then flip: the flip's losses must be undone inside the overlap, where it would have to turn an i-wrong answer into the i-correct one. That leaves it a pure gain.
- Flip then departure: the overlap is null, because the departure's old side is S and the flip's new side is an answer.

So flips are not the problem: retreats are. §4 shows how to keep the room above without killing retreats: restrict the non-additive departures to those whose new side cannot be the old side of any realizable retreat.

---

## 3. The balanced lexicographic rule Ω

Fix bounded measurable ψ₀ = 1, ψ₁, ψ₂, … whose indicator-type members generate the Borel sets (for example, indicators of products of rational intervals). For a record r and world i put

  Ω_i^{(n)}(r) := ∫_{supp r} w_i(g) ψ_n(g) δ_i(g) dμ(g),  Ω_i(r) := (Ω_i^{(0)}(r), Ω_i^{(1)}(r), …).

**Rule Ω.** X ⪯_i Y iff Ω_i(rec(X,Y)) ≥_lex 0, that is, the first nonzero coordinate is positive or all coordinates vanish.

**Theorem 3.1 (PROVED; CHECKED).** The relations ⪯_i satisfy the following.
- **(a)** Each ⪯_i is a linear order on models modulo null sets: reflexive, transitive, antisymmetric and total.
- **(b)** Strict (G).
- **(c)** (IB) with every common-context copy.
- **(d)** (TC).
- **(e)** For every regular N and every model Y, N ⪯_i Y at some world i. In particular every coherent D_K, for any closed convex K ⊆ Δ, is competitive against every rival, bounded or not. The rival's support may be any measurable set, of any size or shape.
- **(f)** No two distinct models tie at any world.

*Proof.*
- (c): Ω_i(r) depends only on (D, a, b).
- Ranks are bounded and μ is finite, so F_i(X) := (∫ w_i ψ_n r_i(·, X) dμ)_n is finite. Moreover Ω_i(rec(X,Y)) = F_i(Y) − F_i(X), since rank changes add under composition.
- So ⪯_i is the pullback of the lexicographic order on R^ℕ, which is a total order compatible with addition. Hence ⪯_i is reflexive, transitive and total.
- Suppose F_i(X) = F_i(Y). Then the signed measure w_i(r_i(·,Y) − r_i(·,X)) dμ vanishes on a π-system generating the Borel sets and on the whole space. By the π–λ theorem it vanishes, so r_i(·,X) = r_i(·,Y) a.e. Because ranks determine values, X = Y. This gives (a) and (f), and (d) follows from transitivity.
- (b): a nontrivial pure worsening at i has Ω_i^{(0)} > 0, and a pure improvement has Ω_i^{(0)} < 0.
- (e): Let v_i := F_i(Y) − F_i(N).
  - By the balance identity, Σ_i v_i^{(n)} = ∫ ψ_n Σ_i w_i δ_i dμ.
  - If Y has a contradiction point or a unanimous error, Σ_i v_i^{(0)} > 0, so some v_i^{(0)} > 0 and N ⪯_i Y.
  - Otherwise Σ_i v_i^{(n)} = 0 for every n. Let n₀ be the first index at which some v_i^{(n₀)} ≠ 0; it exists because Y ≠ N. At n₀ the coordinates sum to 0 and are not all zero, so some v_i^{(n₀)} > 0, while all earlier coordinates vanish. Hence v_i >_lex 0. ∎

CHECKED: `zrule_check.py` uses exact rationals on 18 instances, with up to 1,024 models of the full four-value domain each. It confirms linear orders, strict (G), competitiveness of every regular model against every model, and no regular all-world domination.

**How Ω meets the brief's requirements.**
- *Per-world and record-based:* yes.
- *Uniformity:* it comes free from (IB), as the lead's observation 1 says, and covers more than the interior family.
- *Region structure:* this is the weight 2 on M_i.
- *Ties of infima:* they do not arise. Two rivals accumulating at the same key level are separated by their integrals, so no verdict ever compares essential infima. (§5 shows that infimum-based verdicts cannot avoid ties.)

**Proposition 3.2 (no room; PROVED).** If N and Y are regular and Y ≠ N, then N ⪯_i Y fails at some world.

*Proof.* With v_i as above, Σ_i v_i = 0 coordinatewise. At the first index where some v_i is nonzero, the values sum to 0 and are not all zero, so one is negative. ∎

So under Ω no regular model, coherent or not, is dominated by another regular model. If Ω were the whole relation, every incoherent regular model would be undominated and (S) would fail. As the bounded part of a larger system, Ω forces every KKM dominator of a bounded perturbation of N to be a different model, compared through unbounded records.

**Proposition 3.3 (Ω is endorsed; PROVED, modulo FF2's import chain).**
- ℓ_i(g,v) := w_i(g) r_i(g,v) × (Gaussian density) is an integrable, strictly guiding additive field, and every Ω-acceptance at i has ∫Δℓ_i = Ω_i^{(0)} ≥ 0.
- Hence any system that uses Ω, or any subset of Ω, for the bounded comparisons out of selected models satisfies FF2's (H2) and (H3) with H_n the annuli {1/n < |g| < n}.
- By FF2 Thm 4.1 no such system has a selection that is continuous in measure, competitive on supports, and passes through T1. ∎

**Diagnosis.** The balance identity says that every regular value at every mixed point is Bayes for the uniform weight under the fields ℓ_i. This one fact gives:
- coverage of every regular model;
- the absence of regular dominations;
- endorsement.

The next section shows that, for additive-type covering parts, this is not an accident of Ω.

---

## 4. Room for dominations: what kills it, and what survives

### 4.1 Two collapse results

**Lemma 4.1 (tiny-worsening collapse; PROVED).** Suppose world i accepts every bounded record r with Ω_i^{(0)}(r) > 0. Then (G) and (TC) force every accepted bounded record to have Ω_i^{(0)} ≥ 0.

*Proof.*
- Let r = rec(N,Y) be accepted with Ω_i^{(0)}(r) = −s < 0. Then r has an i-improvement point, where Y's value has rank < 3.
- Replace Y's value by the contradictory value on a small subset E of those points, obtaining Y′. Choose E so that η := Ω_i^{(0)}(rec(Y,Y′)) ∈ (0, s). This is possible because μ is atomless.
- Then Y ⪯_i Y′ by guidance, strictly. Also Ω_i^{(0)}(rec(Y′,N)) = s − η > 0, so Y′ ⪯_i N is accepted.
- (TC) on the triangle N ⪯ Y ⪯ Y′ ⪯ N requires Y′ ⪯_i Y, the reverse of a strict guidance comparison. ∎

The same proof works for any integrable strictly guiding additive field in place of Ω^{(0)}. So **a world that contains an additive covering base can add slack only on records that are neutral for that base.**

For Ω the bases are balanced (§1.3). A domination record would therefore need Ω^{(0)} = 0 at all three worlds, and its first nonzero level would be balanced again, as in Prop 3.2. So the lexicographic levels leave no room at all. I do not claim that every additive covering base is balanced.

**Lemma 4.2 (pump splits; PROVED; any rule).** Assume (G), (IB) and (TC). Let r = (D, a, b) be bounded, and let O ⊆ D be non-null with D ∖ O non-null, such that:
- b|_O is realizable, and the coherent model realizing it is locally competitive;
- for every world i, either O consists of i-losses of r, or O contains all i-losses of r.

Then r is refused at some world.

*Proof.*
- q := (r|_O)⁻¹ has realizable old side, so it is accepted at some world i at which it is not of kind I. That means r|_O is not a pure i-worsening.
- By hypothesis O then contains every i-loss of r. So q·r = r|_{D∖O} is a nontrivial pure i-improvement.
- If r were accepted at i, (P1) would fail. ∎

**Which records does Lemma 4.2 reach?** A record that is a candidate local domination must have a loss at every world. Using the type language of §1.3, `pumpsplit.py` enumerates all 45 type-sets with this property, and all splits by type (none, part or all of each type):
- **exactly 3** type-sets admit a pump split: {P_j, P_l, Q_k}, with O = the P-parts;
- the other 42 escape it.

The SAT core in `core_tri1.out` reproduces exactly this mechanism: the cell dominations that are impossible on `tri1` are {A→S, A→S, S→A} and its permutations. So the axioms alone kill only a thin class of local dominations.

### 4.2 Inverted departures

Order the lines of M_k by inclusion of their e_k-triangles: ℓ ≤ ℓ′ iff the e_k-side of ℓ lies in that of ℓ′, that is, both edge coordinates are smaller (PP2 §3). Every coherent α-set {x ≥ 1} and β-set {x ≥ 2} is an up-set of this order, and is conic. Here x is the majority rank.

**Definition.** A bounded departure d = (D, S, b) is **inverted** if:
- b ∈ {A, B} on D ⊆ mixed problems;
- for each class k that d touches, both D_k^A := {b = A} ∩ M_k and D_k^B are non-null;
- line(g) ≤ line(g′) for a.e. g ∈ D_k^B and g′ ∈ D_k^A.

In words, B sits on lower lines and A on higher ones, the reverse of the coherent order. The case of A and B on the same rays (radial interleaving) is included.

**Lemma 4.3 (PROVED).** If line(g) ≤ line(g′) in M_k, no coherent model gives B at g and A at g′. Hence the new side of an inverted departure is not realizable on any set that meets both D_k^A and D_k^B in non-null sets.

*Proof.*
- B at g puts K strictly inside the e_k-side of line(g), and hence inside the closed e_k-side of line(g′).
- A at g′ puts K strictly on the far side of line(g′). These are incompatible.
- For the non-null version, apply this at Lebesgue points of the two sets. ∎

**Lemma 4.4 (inverted departures never pump with realizable records; PROVED; CHECKED).** Let d be an inverted departure and r a record with realizable old side. Let i be a world at which neither is a pure improvement. Then neither d·r nor r·d is of kind I at i.

*Proof.*
- *d·r.* Kind I forces the following:
  - the overlap O contains all i-losses of d;
  - r's i-losses, which are non-null because r is not a pure improvement, lie in O, at points where b is i-correct and r returns it to S;
  - r's old side on O is b.
  
  The i-losses of d are D_k^B for the classes k ≠ i (B is wrong at a majority world) and D_i^A (A is wrong at the owner). The i-correct points are D_k^A for k ≠ i and D_i^B. Take the class of a loss point of r. Then r's old side carries b on all of that class's i-loss set of d, which is non-null, and on a non-null part of its i-gain set. By Lemma 4.3 this is not realizable, a contradiction.
- *r·d.* Here r maps a → S on O and d maps S → b. Kind I forces the following:
  - d's i-losses lie in O, where the composite is a → b with b i-wrong. Since a is regular and the composite cannot be a loss, a = b there.
  - r has an i-loss somewhere, necessarily in O (outside O the composite is r itself, which must not lose). Such a loss is a point where a is i-correct.
  - At an i-loss point of d, a = b is i-wrong, so r's loss is at an i-gain point of d. There b is the i-correct value, and a must be i-correct too, so a = b.

  So r's old side equals b on all i-losses of d and on a non-null part of its i-gains. This is the same configuration as before, which Lemma 4.3 excludes. ∎

CHECKED: `entangled_check.py` examines all composable pairs on two cell sets (19,009 and 741 pairs) and finds 0 kind-I composites at a world accepting both.

### 4.3 The room reduction

Let 𝒞_i be any set of bounded records with realizable old side and Ω_i ≥_lex 0, closed under copies, such that every bounded record with realizable old side lies in 𝒞_i ∪ W_i for some i. This is a *covering subset of Ω*. Let 𝓘_i be any record-based set of inverted departures. Define

  X ⪯_i Y :⟺ rec(X,Y) ∈ W_i ∪ 𝒞_i ∪ 𝓘_i.

**Theorem 4.5 (room reduction; PROVED).**
- **(1)** Strict (G) and (IB) hold.
- **(2)** Every coherent D_K with K ⊂ int Δ is competitive against every bounded rival.
- **(3)** (TC) holds iff
  - **(iii)** for every world i, no two records x, y ∈ 𝒞_i compose to d⁻¹ with d ∈ 𝓘_i.
- **(4)** If d ∈ 𝓘₁ ∩ 𝓘₂ ∩ 𝓘₃ and N is silent on supp d, then N strictly dominates N·d at every world. N·d is incoherent and regular.

*Proof.*
- (1) holds because each piece refuses pure improvements and is record-based.
- (2): every bounded record out of an interior coherent model has realizable old side, so it is covered.
- (4): an inverted d has a loss at every world i.
  - If d touches a class k ≠ i, world i is an opponent there and loses on D_k^B.
  - If d touches only class i, world i is its owner and loses on D_i^A.

  So d ∈ ∩𝓘_i gives N ⪯_i N·d at all three worlds. The reverse of d has non-realizable old side (Lemma 4.3), so it is not in 𝒞. It is not a departure, so it is not in 𝓘. It is of kind M at every world, so it is not guidance. Hence it is refused everywhere.
- (3): apply Lemma 1.1.
  - *Inside W ∪ 𝒞.* This is a subset of the linear order Ω_i, hence acyclic: no (P1) pair and no accepted triangle.
  - *(P1) pairs involving 𝓘.* Pairs (d, x) are excluded by Lemma 4.4. Pairs (d, d′) compose to a disjoint union that keeps d's loss.
  - *Triangles with an 𝓘 edge* d, x, y, where x·y = d⁻¹:
    - If x or y is guidance, the other two edges compose to a kind-I record. This is a (P1) pair (d, ·), which Lemma 4.4 excludes.
    - Suppose x or y is in 𝓘, say x. Then x is a departure starting from d's new side, so its support misses supp d. The third edge y = (d·x)⁻¹ then has old side equal to b on supp d. That is not realizable, so y is not in 𝒞. It is not a departure, so it is guidance. But then d·x would be kind I, whereas it is a disjoint union of departures that keeps a loss. The case y ∈ 𝓘 is symmetric.
    - If x, y ∈ 𝒞_i, the reverse d⁻¹ is never accepted. So (TC) holds iff no such triangle is accepted, which is (iii).
- Covering subsets of Ω exist: the full Ω restricted to realizable-old bounded records is one, by Theorem 3.1(e). ∎

So **room through inverted perturbations is exactly a splitting condition on the covering part.** Theorem 4.5 is the precise form of "find how retreats and flips can be accepted somewhere without the pump":
- retreats and flips with realizable old side are accepted through 𝒞;
- the non-additive departures are confined to inverted ones, whose new side no realizable retreat can partly undo (Lemma 4.4);
- what remains is (iii).

**Proposition 4.6 (the full Ω violates (iii); PROVED; CHECKED).** Let d be inverted and supported in one class M_k, with Ω_i^{(0)}(d) < 0 at some world i. Then the full covering 𝒞_i = {Ω_i ≥ 0} ∩ realizable-old contains x, y with x·y = d⁻¹.

*Proof.*
- **The padding.** Take a fresh bounded non-null F ⊆ M_k, disjoint from supp d, on lines that are steep: their coordinate on the edge toward e_j is some ε below that of every B-line of d, and their coordinate toward e_l is above that of every A-line.
- **The two edges.** Let e be S → A or S → B on F. Choose the value and mass of e so that Ω_i^{(0)}(e) = t, with t strictly between −Ω_i^{(0)}(d⁻¹|_A) and Ω_i^{(0)}(d⁻¹|_B). Any real t is reachable: on F, S → A has Ω^{(0)} = +2μ(F) at the owner and −μ(F) at a majority world, and S → B the opposite.
- **The triangle.** Put x := d⁻¹|_{D^A} ∪ e and y := d⁻¹|_{D^B} ∪ e⁻¹. Then x·y = d⁻¹. Both Ω_i^{(0)}(x) and Ω_i^{(0)}(y) are positive: the interval for t is nonempty exactly because their sum is −Ω_i^{(0)}(d) > 0. The triangle P ⪯ Q ⪯ R ⪯ P runs in any context with P silent on supp d ∪ F.
- **Realizability of x's old side** (A on D^A, S on F).
  - The union of the e_k-triangles of the A-lines is a union of corner triangles. Its complement is an intersection of half-planes, hence convex.
  - Each steep line reaches that complement, because its coordinate toward e_l is larger.
  - Take a compact arc made of one point on each steep line, at positive distance from the union. Its convex hull stays in the complement, and gives K.
- **Realizability of y's old side** (B on D^B; A on F if e = S→A, B if e = S→B).
  - If e = S → B, take K near e_k, inside every B-triangle and every steep triangle.
  - If e = S → A, take a small ball near the edge toward e_j at distance between ε and the B-lines' coordinate. It lies inside every B-triangle and outside the thin steep triangles. ∎

CHECKED exactly (`padded_triangle.out`):
- Ω₂(d) = −2 at world 2, while d is non-improving at every world;
- Ω₂(x) = Ω₂(y) = 1, with both old sides realizable;
- the old side of d⁻¹ is not realizable.

This is the tiny-worsening collapse of Lemma 4.1 in triangle form.

**Proposition 4.7 (owner-world obstruction for every Ω-subset covering; PROVED; CHECKED).** Let 𝒞 be any covering subset of Ω. Let d be inverted in one class M_k and **B-heavy**: β := ∫_{D^B} dμ > α := ∫_{D^A} dμ, so that Ω_k^{(0)}(d) = 2(α − β) < 0. Then d ∉ 𝓘_k for any choice of 𝓘 satisfying (TC). So d is never a local domination in such a system.

*Proof.*
- Take e = S → A on steep F with μ(F) = φ ∈ (α, β), and x, y as in Prop 4.6. Then:
  - Ω_k^{(0)}(x) = 2(φ − α) > 0 and Ω_k^{(0)}(y) = 2(β − φ) > 0;
  - at both majority worlds Ω^{(0)}(x) = α − φ < 0 and Ω^{(0)}(y) = φ − β < 0.
- So x and y are acceptable in Ω only at k, and neither is guidance anywhere else. Coverage forces x, y ∈ 𝒞_k.
- Then (iii) at k forbids d ∈ 𝓘_k. ∎

CHECKED (`sat_zsubset.out`, config `propD`, masses 3, 1, 2): with every SAT-chosen Ω-subset covering, the one inverted departure cannot be accepted at all worlds (UNSAT). With other masses, where the inequalities fail, the problem is SAT.

**When d is A-heavy (α > β).**
- The conflicts sit at the two majority worlds, where Ω^{(0)}(d) = β − α < 0. At the owner, Ω_k^{(0)}(d) > 0.
- For a split (x, y), the values Ω_l^{(0)}(x) and Ω_l^{(0)}(y) add up to α − β > 0. So at least one of x, y is also acceptable at the other majority world, and no pair is forced onto a single world.
- Whether the infinite conflict graph can be properly list-coloured by a *measurable record-based* rule is the open point.

**Proposition 4.8 (CHECKED, cells).** Config `nest2`: two nested lines of M₁, each split radially, plus one line of M₂, with random masses. Accept all 25 inverted departures at every world. The SAT search over all record-level (P1) and (P2) clauses (1.7·10⁶ and 1.5·10⁷ of them), covering by Ω-subsets, is **SAT** for both seeds tried.

More broadly, with no restriction to Ω-subsets (`satrun.out`):
- every single candidate local domination is realizable on `one3`, `cross1`, `nest1`, `mix12` and `cyc1`;
- the only impossible ones on `tri1` are the pump-split class of Lemma 4.2;
- requiring all candidate dominations simultaneously is UNSAT everywhere.

Omitted on cells: X values and unanimous problems in the SAT runs (sub-domain only); arbitrary paddings (Prop 4.7 needs a steep third line, and it fails only once one is added); masses beyond the finitely many pieces; (S).

**Conjecture 4.9.** There is a measurable, record-based covering subset 𝒞 of Ω, and a set of A-heavy inverted departures in ∩_i 𝓘_i containing departures of every A-to-B mass ratio above 1 near a.e. point, satisfying (iii).

**Consequence if Conjecture 4.9 holds (PROVED).** The resulting local rule would not be endorsed at either majority world by any integrable strictly guiding additive field.
- Inverted departures with B-mass → 0 and fixed A-mass are accepted there.
- An endorser would need ∫_{D^B}(ℓ(B) − ℓ(S)) ≥ ∫_{D^A}(ℓ(S) − ℓ(A)). The left side tends to 0 and the right side does not.

This is the kind of world FF2 Cor 4.3 says every cover needs.

---

## 5. Gates and the tie-of-infima problem

A world uses a **weak gate** with fixed key k_i(g, j) if every accepted non-guidance record satisfies ess inf k_i(added steps) < ess inf k_i(removed steps). Ties are refused.

**Lemma 5.0 (local cheap-change criterion; PROVED; PP2 Prop 3 verbatim).** If for some c ∈ R³ each world has a non-null set of bounded c-cheap changes of N, placed on disjoint sets, then the combined bounded rival fails all three gates strictly. The proof in PP2 is per record and never uses (S).

**Lemma 5.1 (radial keys always tie; PROVED).** Suppose every key depends only on the radius, with any dependence on world, level and class: k_i(g,j) = φ_{i,j,class(g)}(|g|). Then every coherent N with non-null A-set and non-null silent set in some class M_k fails local competitiveness under weak gates.

*Proof.*
- Take P = {A-directions of N in M_k} × [ρ₀, ρ₁] and Q = {S-directions} × [ρ₀, ρ₁], and the record A → S on P and S → A on Q.
- At each world all changed steps of a given kind lie on the same class and level. Both P and Q have radial support [ρ₀, ρ₁], because μ is rotation-invariant. So every essential infimum of φ over P equals that over Q: a tie at every world.
- The record is of kind M at every world: the opponents lose on P and gain on Q, and the owner the reverse. ∎

So the radial direction, to which coherent models are blind, cannot serve as a gate key.

**Lemma 5.2 (two-generator rival; PROVED).** On M_k let a_j, a_l be the majority worlds' level-1 keys and b_k the owner's level-2 key (the α-channel keys). Suppose there are approximate-continuity points q₁, q₂, p with:
- q₁, q₂ ≰ p;
- a_j(q₁) < a_j(p) and a_l(q₂) < a_l(p);
- b_k(p) < min(b_k(q₁), b_k(q₂)).

Then the interior coherent model whose α-set is generated by q₁ and q₂ fails all three gates on the record (S → A near q₁ and q₂, A → S near p).

*Proof.*
- Realizability: take K as the segment between points of the two e_k-triangles of q₁ and q₂, chosen outside the e_k-triangle of p. The far side of a line is convex.
- The inequalities make the removed steps lowest at the majority worlds and the added step lowest at the owner. ∎

**When the hypothesis holds.** Suppose the majority keys are the two edge coordinates, a_j = z_kj and a_l = z_kl. These are the position keys gate2d uses in the two edge problems at e_k. Suppose also that the owner key b_k is continuous and strictly decreasing in the line order. Then the hypothesis holds:
- Take q₁ upper-left of q₂, and p := q₁ ∨ q₂ − (ε, ε) for small ε.
- Strict decrease gives b_k(q₁ ∨ q₂) < b_k(q_i), and continuity carries this to p.
- p remains incomparable with q₁ and q₂.

Example: q₁ = (0.1, 0.9), q₂ = (0.9, 0.1), p = (0.55, 0.55) with b_k = −(z_kj + z_kl). I have not shown the hypothesis for arbitrary monotone keys.

**Lemma 5.3 (channel-shared keys; PROVED).** Suppose that on each channel the three worlds use one common key f (majority level 1 and owner level 2 on the α-channel; majority level 2 and owner level 1 on the β-channel). Then:
- no change is c-cheap for the world with the smallest c_i, so Lemma 5.0 never applies;
- the only failures are ties.

For tier keys this sharing is *forced*. Here a tier key gives every world the same constant values: o₁, o₂ on its own class at levels 1 and 2, and p₁, p₂ on the other classes. The requirement is local defence of an interior N with A, S and B on non-null sets of every class. It forces o₂ = p₁ and o₁ = p₂.

*Proof.*
- *First claim.* A change in a channel adds and removes steps at one common key value. So a world is cheap only if every world that adds has a smaller c than it does.
- *Forcing, first pair.* Take c = (c, c, c) and consider two kinds of change:
  - S → A on another class is cheap for a majority world iff p₁ < c ≤ o₂;
  - A → S on the world's own class is cheap for the owner iff o₂ < c ≤ p₁.

  If o₂ ≠ p₁, some c makes one of these cheap for every world. Each world uses a different class, and Lemma 5.0 then defeats N.
- *Forcing, second pair.* B → S on another class is cheap iff p₂ < c ≤ o₁, and S → B on the world's own class iff o₁ < c ≤ p₂. This forces o₁ = p₂. ∎

Ties remain. For radius-dependent shared keys Lemma 5.1 applies. A general measurable shared key has not been classified (OPEN).

### 5.4 PP2 Thm 6 and the rules here

PP2 Thm 6 assumes:
- (H2): world 1 accepts every non-guidance comparison only through one fixed weak gate;
- (H4): (S) with closed sections.

For Ω and for the rule of Theorem 4.5:
- (H1) holds (the setting);
- (H3) holds: every world has strict (G);
- (H2) fails: neither rule is a gate, and both accept comparisons that fail every fixed-key gate;
- (H4), that is (S), is not claimed.

So Thm 6 says nothing about these rules.

Lemmas 5.1 and 5.2 are local relatives of Thm 6 that need neither (S) nor closed sections: local defence of the interior family alone excludes these gate families. A full classification of fixed keys (CONJECTURE: every fixed key fails) would need Lemma 5.2's hypothesis or a tie in every case. I have not proved that dichotomy.

---

## 6. Answers to the brief, and next step

| Brief item | Answer |
|---|---|
| Rule with (G), (IB), (TC) and local competitiveness for every interior coherent D_K | Rule Ω (Theorem 3.1, PROVED). It covers every regular model against every rival, with no ties. |
| Lead's departure rule and (TC) | (TC) holds (Theorem 2.1, PROVED). Run at all worlds it dominates every interior coherent model (Cor 2.4). |
| Retreats and flips without the pump | Flips never pump with departures (§2). Retreats under Rule D are blocked (Lemma 2.3). Remedy: judge retreats and flips with realizable old sides through a covering part, and keep only *inverted* departures outside it (Lemma 4.4, Theorem 4.5). |
| Region structure | The weight 2 on the owner class gives the balance identity. Inverted departures and the obstructions of §4 are classwise statements. |
| Tie of infima | Avoided by integral-lexicographic verdicts (Ω). Unavoidable for radial and line-monotone weak gates (Lemmas 5.1, 5.2). |
| Room for dominations | Ω: none (Prop 3.2), and endorsed (Prop 3.3). Additive covering bases: none off neutral records (Lemma 4.1). By the axioms alone: only the {P_j, P_l, Q_k} class is killed (Lemma 4.2). With inverted departures, room is equivalent to (iii) (Theorem 4.5). The full Ω violates (iii) (Prop 4.6). B-heavy inverted perturbations can never be dominated over an Ω-subset covering (Prop 4.7). On cells (iii) holds (Prop 4.8). Continuum A-heavy case: Conjecture 4.9. |
| Obstruction not relying on frozen comparisons | Lemma 4.2 uses only (G), (IB), (TC) and coverage, and needs no optional comparison. Props 4.6 and 4.7 and Lemma 4.1 are screens on a design class (covering inside Ω), and are labelled as such. No axiom-level obstruction to room was found; the cell evidence (Prop 4.8) suggests none exists. |

**Assessment.**
- Local defence of the entire interior family is easy: Ω.
- Room for dominations is the real constraint. Every covering mechanism built from an additive or balanced base is closed under padding, and padding splits any extra acceptance into two covered pieces (Lemma 4.1, Props 4.6 and 4.7).
- The surviving design target is a covering part that is **non-additive at the majority worlds** and **refuses at least one piece of every padded split of an A-heavy inverted retreat**.
- Such a covering part would at once:
  - give strict local dominations of inverted perturbations;
  - escape FF2's endorsement hypothesis.

**Most important next step.** Attack Conjecture 4.9 in the two-player form of a single class: owner k against two opponents with identical views, on the line order of M_k. The conflict graph in that form is explicit:
- x contains the retreat of A-points on high lines;
- y contains the retreat of B-points on low lines;
- the two padding parts are mutual inverses.

Either:
- exhibit a measurable list colouring with lists ⊆ {j, l} for the pairs where only those worlds are Ω-acceptable; or
- find an odd cycle of padded splits all confined to {j, l}. That would turn Prop 4.7 into a full Ω-subset obstruction, and show that room needs a covering part outside Ω at some world.
