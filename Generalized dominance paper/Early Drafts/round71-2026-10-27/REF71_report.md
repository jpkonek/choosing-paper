# REF71 report (27 Oct 2026)

Referee for: AUDITOR_note.md, LEAD_claims.md L1-L4 (and the L5 two-world aside), checked against app.tex
(Def 2.x change, Lemma 6.5 `lem:guidedeverywhere`, Prop 6.2 `prop:structure`, Prop 6.3 `prop:maximal`, Prop 6.6 `prop:protect`,
covers-K in Sec 6.3, Thm 6.8 `thm:main`, Cor 7.1 `cor:domains`, Thm 5.1 `thm:repair`).
Script: `ref71_check.py` (exact arithmetic for L4; also reruns cx.py's numbers).

## Verdicts (one line each)

| # | Claim | Verdict |
|---|---|---|
| A1 | Exact protection equivalence (auditor) | **PROVED**. It needs only independence, reflexivity and strict score consistency, and it uses the paper's own dominance notions. |
| A2 | Maximal rankings = {V=P off dangerous; V=Ω\{j(r)}, j(r)∉H(r) on dangerous} | **PROVED** |
| A3 | Existence for arbitrary Ω; chain-union warning | **PROVED**. AC is needed only to well-order Ω, and no AC is needed for countable Ω. The chain warning is correct. |
| A4 | Null-set invariance of V, P, H, availability | **CHECKED** |
| A5 | H(r)≠Ω for dangerous r | **PROVED**. It follows from Lemma 6.5 under μ{P_S=0}=0 plus separability and an order unit (or Rem `rem:orderunit`). It holds for every non-null change available to a coherent model, not only for dangerous ones. |
| A6 | Coverage theorem for maximal rankings (all clauses) | **PROVED** under (M1),(M2). (M3) is not needed. |
| A7 | Sandwich class R0 ⊆ R ⊆ Rmax (reflexive, independent) covers | **PROVED** |
| A8 | Finite-Ω Zorn route to maximal additive protecting extensions | **PROVED**. A nearby result also holds for arbitrary Ω (see §A8). |
| L1 | Product structure | **CHECKED**, with one wording fix (E3) |
| L2 | (a)+(b) is an exact criterion; (5') suffices; class equality | Criterion and sufficiency **PROVED**. The class equality is **WRONG as literally stated** because the right-hand side must be restricted to independent relations (E1). With that fix it is **PROVED**. |
| L3 | R∩ formula; largest with (3'); neutrality characterisation; R0 ⊊ R∩ example; R∩ covers | **PROVED** (all parts) |
| L4 | No maximal ranking (and not R∩) is disjointly additive | **PROVED**. The arithmetic is exact. The "exact for point masses" wording is wrong, and the 19/20 split is unnecessary (E2, E4). |
| L5 aside | R∩ is disjointly additive when \|Ω\|=2 | **PROVED** (bonus, §L5) |
| Q5 | Carry-over to U closed under coherent hulls | **PROVED**. Everything restricts. Coverage of K on U holds iff D_K⊆U a.e. and local freedom holds, exactly as in Cor 7.1(d). |

No mathematical error affects the main conclusions. The errors are E1–E4 below.

---

## 0. Translation of the axioms (used throughout)

The paper's coverage definition gives independence as follows: whether X⪯_ω Y holds depends only on the change from Y to X, taken modulo null sets.
Any pair r=(A,B) of a.e.-classes with μ(A∩B)=0 is realised as a change, by taking Y=B and X=A.
So an independent ranking is the same thing as a map r ↦ V(r) ⊆ Ω.
Inclusion of rankings, as relations, is coordinatewise inclusion of the V(r).

Write r⁻¹=(B,A), d_ω(r)=m_ω(A)−m_ω(B), P(r)={d>0} and H(r)={ω: r guided by ω}.

- **Reflexivity** says that V(null change)=Ω. Since models are identified a.e., a.e.-equal models are then tied.
- **Strict score consistency** says that V(r)⊆P(r) for every non-null r.
- **Strict guidance** says that for non-null r and ω∈H(r), ω∈V(r) and ω∉V(r⁻¹).
  Prop 6.2(b) gives H(r)⊆P(r), so d_ω(r⁻¹)<0 there, and score consistency already forbids ω∈V(r⁻¹).
  So, *given score consistency*, strict guidance is exactly H(r)⊆V(r).
  Without score consistency it links r and r⁻¹ (see E3).
- **Dominance.** The paper (Sec 6.2) uses three notions:
  - weak dominance means Y⪯_ω X at every world;
  - dominance means weak dominance plus Y≺_ω X at some world;
  - undominated means not dominated.

  Under the three axioms above:
  - if Y=X a.e., they are tied everywhere, so Y does not dominate X;
  - if Y≠X a.e., weak dominance means ω∈V(X→Y) for all ω, so d_ω>0 everywhere, so the reverse is refused everywhere, so the dominance is strict at every world.

  Hence weak dominance by a distinct model, dominance and strict dominance coincide. This is the analogue of Prop `prop:strict` (i)–(iii), with (iv) replaced by "X→Y accepted at every world".

## A1. Exact protection equivalence

**Claim.** Assume independence, reflexivity and strict score consistency. Every coherent model is undominated iff V(r)≠Ω for every non-null r available to some coherent model.

**Proof.**

(⇐) Suppose coherent C is dominated by Y. By §0, Y≠C a.e. and V(C→Y)=Ω. The change C→Y adds Y∖C, which misses C, and removes C∖Y⊆C. So C itself can make it (Def. of change), and it is non-null. This contradicts the condition.

(⇒) Suppose r=(A,B) is non-null, available to a coherent model Z, and V(r)=Ω. Put Y=(Z∖B)∪A. The change Z→Y is r a.e. (Def. of change, using B⊆Z a.e. and μ(A∩Z)=0). So Y⪯_ω Z at every ω, and Y≠Z a.e. By §0, Y strictly dominates Z.

∎

Strict guidance is not used. The restriction to non-null r is necessary because reflexivity forces V(null)=Ω. The equivalence also holds verbatim on any domain U, with "coherent model on U" and changes between models on U, since Y⊆U whenever Z,A⊆U.

## A5. H(r)≠Ω: what Lemma 6.5 gives, and under which hypotheses

Lemma 6.5 assumes μ{P_S=0}=0 and the standing setting. Suppose a change (A,B) is guided by every world. The lemma then gives A⊆D_S a.e. and B⊆{sup h≤0} a.e. Every D_Q contains D_S and meets {sup h≤0} in the empty set.

Uncountable Ω is handled through the countable Ω₀ of Lemma `lem:states`(f), which uses separability of E. It also uses 𝟙∈E, through P_S=inf h. Under Rem `rem:orderunit` (order unit e), the transfer map preserves guidance and the D_Q, so the lemma transfers.

Now let r be non-null, available to D_Q, and guided everywhere. Then A⊆D_Q a.e. and μ(A∩D_Q)=0, so A is null. Likewise B⊆D_Q a.e. and B∩D_Q is null, so B is null. This is a contradiction.

So **H(r)≠Ω for every non-null change available to a coherent model**. This is the auditor's claim, with "dangerous" not needed. (M1) is needed only to define P(r). (M3) is not used.

## A4. Null-set invariance

- A change is a pair of a.e.-classes.
- m(A) depends only on the a.e.-class of A, so d_ω and P(r) are invariant.
- Guidance is defined with "a.e." at each ω, so H(r) is invariant. Different worlds may have different null exceptions; that is harmless for H as a set of worlds, and Lemma 6.5 deals with it when all worlds are needed.
- Availability is defined a.e., and coherence is a property of a.e.-classes. So "available to a coherent model" and "dangerous" are invariant.
- V(r) is invariant by independence. The auditor's remark that "choices are made on classes" is just independence.

CHECKED.

## A2. Characterisation of maximal rankings

By §0, the rankings satisfying 1–4 are exactly the maps V with:
- V(null)=Ω;
- for non-null r, H(r)⊆V(r)⊆P(r);
- by A1, V(r)≠Ω whenever r is available to a coherent model.

Every constraint concerns one r. The set of admissible rankings is therefore the product over r of the admissible sets 𝒜(r):

- **r not available to any coherent model:** 𝒜(r)={V: H⊆V⊆P}. Its maximum is P.
- **r available to a coherent model, P≠Ω:** the same set, because V⊆P≠Ω. Its maximum is P.
- **r dangerous:** 𝒜(r)={V: H⊆V⊊Ω}. Its maximal elements are exactly Ω∖{j} with j∉H(r). This set is nonempty by A5.
  - Each Ω∖{j} is maximal, since the only strictly larger subset is Ω.
  - Any V∈𝒜(r) with two missing worlds j≠j′ is strictly contained in V∪{j′}∈𝒜(r).
  - j∈H is impossible, because H⊆V.

In a product of posets, an element is maximal iff each coordinate is maximal.
- If one coordinate is not maximal, enlarge that coordinate alone.
- If every coordinate is maximal, any larger element agrees in each coordinate.

This is exactly the auditor's formula, together with V(null)=Ω. **PROVED.**

The auditor's necessity and sufficiency arguments are this proof in words and are correct. One point they do not mention: adding ω to V(r) with d_ω(r)>0 cannot break strict guidance of r⁻¹, because ω∈H(r⁻¹) would force d_ω(r)<0.

## A3. Existence and the chain warning

**Existence.** Well-order Ω (AC) and let j(r)=min(Ω∖H(r)). This is the only use of choice, and no choice is needed for countable Ω. The maximal ranking then exists outright. **PROVED.**

**Chain warning.** Take countable Ω={ω₁,ω₂,…} and a dangerous r. The stages V_n(r)=Ω∖{ω_k: k≥n} each satisfy 1–4 on this coordinate, with the other coordinates fixed at R0. The chain increases, but its union has V(r)=Ω. So Zorn over 1–4 fails in infinite Ω. In finite Ω every increasing chain of subsets stabilises, so the warning does not apply there. **CHECKED.**

## A6. Coverage theorem for maximal rankings

**Setting.** U=E, (M1) and (M2). (M3) is not needed. Any credal set K is the target.

**R0 ⊆ Rmax.**
- If r is not available to a coherent model, V0(r)=P(r)=Vmax(r).
- If r is available to a coherent model, V0(r)=H(r)⊆Vmax(r), since j(r)∉H(r).

R0 itself is the paper's ranking: its V0(r) is H∪P for unavailable r and H for available r, and H⊆P.

**Repair.** Let X be incoherent. Thm 5.1(1),(4) gives a coherent N with d_ω(X→N)≥η>0 at every ω, by a change that no coherent model could make. So this change is not dangerous, and Vmax=P=Ω on it. N≠X a.e., because coherence is a property of classes. By §0, N strictly dominates X, and the margin η makes the dominance uniform.

**Clause-by-clause check of "covers K" (Sec 6.3):**
1. *Strict guidance:* from H⊆V together with score consistency (§0).
   *Independence:* by construction.
   *Finite-chain consistency:* a chain A₀⪯…⪯A_k gives m(A₀)≥…≥m(A_k). Equalities occur only on a.e.-equal steps, by score consistency and reflexivity. Now A_k≺A₀ requires A_k≠A₀ a.e., since a.e.-equal models are tied. That gives m(A_k)>m(A₀), a contradiction.
2. *Global coherence:* incoherent X is dominated by its repair N.
3. *Closure under ties:* distinct models are never tied, since a tie would need d>0 and d<0. So a model tied everywhere with an undominated coherent model equals it a.e.
4. (4a) holds trivially on E. (4b): D_K is undominated by A1.
5. *Incoherent-model dominance:* N dominates X uniformly, and N is undominated by A1.
6. *Local freedom:* E is open.

The analogues of Thm 6.8(b)–(d) also hold:
- (b) uniform dominance by the repair;
- (c) every model is weakly dominated by an undominated coherent model;
- (d) no coherent model has a weak dominator other than itself, and there are no ties between distinct models.

The bijection in (a) needs (M3), exactly as in the paper. **PROVED.**

## A7. Sandwich class

Let R be independent with R0⊆R⊆Rmax.
- Reflexivity holds because R⊇R0.
- Guidance holds because H⊆V0⊆V.
- Score consistency holds because V⊆Vmax⊆P.
- Protection holds because V⊆Vmax, and Vmax≠Ω on non-null changes available to a coherent model.
- Repairs are inherited from R0.

Coverage follows as in A6. **PROVED.**

Independence must be assumed explicitly. Without it, R still has guidance, score consistency, protection and repairs, but it fails requirement (1). The auditor states this; L2 omits it (E1).

## A8. Additive extensions

**Finite Ω (the auditor's route).** Consider the class of independent rankings ⊇R0 with 1–4 and disjoint additivity. It contains R0 (Prop 6.2). It is closed under unions of chains:
- every condition except protection is finitary;
- additivity: if x∈V_i(s) and x∈V_k(t), then both hold at the later stage, which is additive, so x∈V(r);
- protection: an increasing chain of subsets of a finite Ω has a largest member, so the union of the V(r) is that member, which is ≠Ω.

Zorn applies. Every maximal element contains R0 and satisfies 1–4, so it covers. **PROVED.**

**Nearby result for arbitrary Ω (new, PROVED).** Fix any selection j(r)∉H(r) on dangerous r. Let 𝒞_j be the class of independent, additive rankings R⊇R0 with 1–3 and j(r)∉V_R(r) for all dangerous r.
- R0∈𝒞_j, because V0(r)=H(r) on dangerous r.
- 𝒞_j is closed under chain unions, since the refusal at a fixed world survives unions.
- Every member satisfies protection and contains R0, so it covers.

So for every Ω and every j, maximal j-respecting additive extensions of R0 exist and cover. What remains open in infinite Ω is whether some such element is maximal among *all* additive rankings with 1–4.

## L1. Product structure

Correct once score consistency is in force. Then guidance is H⊆V per change (§0), protection is per change (A1), and finite-chain consistency is automatic. Without score consistency, strict guidance couples r and r⁻¹ (E3).

Disjoint additivity is genuinely non-local: it couples r with each of its splits s⊔t. Transitivity is also non-local, coupling the changes Z→Y, Y→X and Z→X. **CHECKED.**

## L2. Exact coverage criterion

Rankings here are reflexive and independent, with strict guidance and score consistency. **Claim:** "undominated = coherent, and every incoherent model is dominated by a coherent model" ⇔ (a)+(b).

**Proof.**
- (a) is protection, by A1.
- Under §0, "X is dominated by coherent N" ⇔ V(X→N)=Ω, which is (b).
- If (a) holds, the coherent dominator is undominated. So (a)+(b) gives every clause of "covers every K" on E (A6 argument).
- Conversely, covering every K forces all D_K to be undominated, which gives (a), and (5) gives (b).

So (a)+(b) is exactly "one ranking covers every credal set" on E. For a *single* K, (a) is not necessary. **PROVED.**

**(5') suffices.** The repair change is unavailable to coherent models and has P=Ω, so (5') accepts it everywhere. So does the weaker form that only covers unavailable changes with P=Ω. **PROVED.**

**Class equality.**

(⊆) Let R satisfy 1–4 and (5'). Then:
- V=P on changes not available to a coherent model;
- H⊆V⊆P elsewhere;
- V≠Ω on dangerous changes.

So V⊇V0. For each dangerous r, choose j(r)∈Ω∖V(r); this lies outside H(r). Then V⊆V_{max,j}. Choice is used here, as in A3.

(⊇) This is A7, and it needs R independent.

As written, "{R : R0 ⊆ R ⊆ some maximal ranking}" includes non-independent relations, which fail axiom 2. **WRONG as stated; correct with "independent R"** (E1).

## L3. R∩

**Formula.** By the product structure, each j∈Ω∖H(r) is realised by some maximal ranking. So V∩(r)=⋂_{j∉H(r)}(Ω∖{j})=H(r) on dangerous r, and V∩(r)=P(r) elsewhere, with Ω on null changes. **PROVED.**

**Largest relation with guidance, score consistency and (3').**
- R∩ has these properties.
- Let R have them, and suppose X R Y at ω. If X=Y a.e., this is in R∩. Otherwise ω∈P by score consistency, and if the change is dangerous, ω∈H by (3'). So the triple is in R∩.

As in Prop 6.3, neither independence nor guidance is needed for containment. R∩ also satisfies protection: on dangerous r, V=H≠Ω by A5; on other non-null changes available to a coherent model, V=P≠Ω. **PROVED.**

**Neutrality characterisation.** Let R satisfy 1–4 and neutrality, and let r be dangerous. If some ω∈V(r)∖H(r), neutrality gives V(r)⊇Ω∖H(r). With H⊆V this means V=Ω, contradicting protection. So V(r)=H(r), and R⊆R∩. R∩ satisfies neutrality vacuously. **PROVED.**

Philosophical note: under protection, neutrality is just (3') restated. It is not an independent motivation.

**R0 ⊊ R∩ example.** Take Ω={a,b}. Let A be two equal-mass small balls about (2,−1) and (−1,−1), and r=(A,∅).
- d≈(1,−2), so P={a}.
- A⊆{h_b<0}, so D_{δ_b}={h_b>0} can make r.
- The ball about (−1,−1) lies in {h_a<0}, so r is not guided at a.
- R∩ accepts r at a, because r is not dangerous. R0 refuses it, because r is available to a coherent model and not guided.

**R∩ covers**, by L2: R0⊆R∩ gives (b), and protection gives (a). **PROVED.**

## L4. Maximality is incompatible with disjoint additivity

**Composition.** Under independence, the Prop 6.2(c) clause is equivalent to the lead's restatement. Let r₁=(A₁,B₁) and r₂=(A₂,B₂) have supports disjoint mod null. Put Z=B₁∪B₂, Y=A₁∪B₂ and X=A₁∪A₂. Then:
- Z→Y is r₁ and Y→X is r₂;
- X△Y=A₂∪B₂ and Y△Z=A₁∪B₁, so their intersection is null;
- Z→X is (A₁∪A₂, B₁∪B₂).

For L4 itself, Z=∅, Y=the s-set, X=A.

**The vacuous model.** D_S={h: min_i h_i>0}, the strictly positive vectors. It is coherent, with Q=S=Δ₃.

**Arithmetic (exact; `ref71_check.py`).**
- Σu=(20,20,20).
- The lead's split (x,y,z) gives s=(201/20, −21/20, 41/2) and t=(199/20, 421/20, −1/2). This matches cx.py for all six (x,y,z).
- With weight λ on the u_{yxz} piece, s=(11−λ, λ−2, 11+10λ) and t=(9+λ, 22−λ, 9−10λ). These work exactly for λ∈(9/10,1].
- **λ=1 needs no splitting of any ball:** s={u_{xyz},u_{yxz},u_{zyx}} has sum (10,−1,21), and t=the other three has sum (10,21,−1). The margin is 1.

**Small balls.** Choose ε<1/3. Pick concentric balls of a common measure δ about the six points, as in Ex `ex:intransitive`, and rescale scores by 1/δ, which preserves signs.

The barycentre of any measurable piece of a ball lies in the closed ball. So each piece's normalised score is within ε of its centre in sup norm, and each of s, t is within 3ε of its point-mass value.

Then:
- the balls are disjoint, since the centres are ≥2 apart;
- every gamble has a coordinate in (−1−ε, −1+ε), so A∩D_S=∅ and r is available to D_S;
- every world has two balls with h_ω≈−1, so H(r)=∅;
- d(r)>0 everywhere, so r is dangerous;
- s fails at y and t fails at z, so neither is dangerous;
- both have d_x>0.

The lead's 19/20 version is also robust, for ε<0.16; it needs a sub-ball of measure 19δ/20.

**Conclusion.** Let R be any ranking with 1–4 and V=P on non-dangerous changes. This includes every maximal ranking and R∩. By protection, V(r)≠Ω, so some j refuses r. Use the split at x=j: s and t are accepted at j and r is refused there. So disjoint additivity fails.

R0 is additive (Prop 6.2(c), via Lemma `lem:join`: if the union is available to a coherent model, so is each part). **PROVED.**

**Sharper reading.** Any additive ranking with 1–4 must, at each world x, refuse one of the two non-dangerous changes s_x, t_x, even though both improve the score at x. So additivity plus protection forces refusals that protection alone does not.

## L5 aside: R∩ is additive when |Ω|=2

**Lemma.** Take E=ℝ², (M2), and a non-null change guided by a and available to D_Q. Then d_b<0.

*Proof.* Work on B⊆{h_a<0}∩D_Q a.e. Pick q∈Q. Then q≠δ_a, because h_a<0 and q·h>0. So q_b>0 and q_b h_b > −q_a h_a ≥ 0, hence h_b>0.

Now work on A⊆{h_a>0}∖D_Q a.e. There P_Q(h)≤0, so q·h≤0 for some q∈Q. Again q≠δ_a, so q_b h_b ≤ −q_a h_a < 0, hence h_b<0.

So m_b(A)≤0≤m_b(B), with one inequality strict, and d_b<0. ∎

Hence, in two worlds, H(r)=∅ for every dangerous r, and V∩(r)=∅ on dangerous r.

**Additivity.** Let s,t be disjoint and accepted at a, and let r=s⊔t.
- If r is not dangerous: d_a(r)=d_a(s)+d_a(t)>0, so a∈P(r)=V∩(r).
- If r is dangerous: s and t are available to a coherent model by Lemma `lem:join`. Neither is dangerous, since dangerous changes have V∩=∅. Both have d_a>0 and P≠Ω, so d_b(s)≤0 and d_b(t)≤0. Then d_b(r)≤0, a contradiction.

**PROVED.** So for |Ω|=2:
- R∩ is an additive covering ranking that strictly contains R0;
- R∩ is the largest ranking with 1–4, neutrality and additivity, which answers L5's first question for two worlds: it is R∩, not R0;
- for |Ω|=3, L4 shows that R∩ is not additive.

## Q5. Restricted domains U closed under coherent hulls (Cor 7.1)

Changes are now pairs (A,B) with A,B⊆U a.e., and all are realised by models on U.

By Cor 7.1(a), "available to a coherent model on U" equals "available to a coherent model" for such changes. So "dangerous" and the R0 test are the restrictions of those on E. A5 does not involve U.

Consequences:
- **A1** holds on U (see the note after A1's proof).
- **A2 and A3** hold verbatim over the changes inside U. Rmax^U is exactly the set of restrictions of the Rmax, and R∩^U=R∩|_U.
- **L2(b) and (5')** use the repair N⊆U a.e. (Cor 7.1(b)), and the change X→N is between models on U.

So L2 and L3 carry over verbatim, with "coherent model on U" in place of "coherent model". The auditor's theorem also carries over, with two exceptions.

**What changes.** (4a) and (6) are no longer automatic.
- Every ranking in the sandwich class on U (in particular every maximal ranking and R∩) covers K iff D_K⊆U a.e. and local freedom holds at D_K. This is the same answer as Cor 7.1(d), since (4b) follows from protection once D_K⊆U.
- The R0⊊R∩ example and L4 need the relevant balls to lie in U. For instance, both work in U=D_{K′} with K′={uniform}, since p·u=10/3>0.

**If U is not closed under coherent hulls,** A1 and the characterisation still hold relative to coherent models on U. But the repair may leave U, so (b) can fail. This is not treated here.

---

## Errors and corrected statements

- **E1 (L2, class equality).** Corrected statement: "the class {1,2,3,4,(5′)} equals the set of *independent* relations R with R0⊆R⊆Rmax for some maximal Rmax". The ⊆ direction uses choice.
- **E2 (L4, "exact for point masses").** Point masses are not admissible: they violate the Lebesgue-null-set hypothesis and (M2). An atom also cannot be split 19/20 : 1/20 as a set. The fractional computation in cx.py is only the limit of the ball construction.
  Corrected statement: use the whole-ball split s={u_{xyz},u_{yxz},u_{zyx}} with sums (10,−1,21) and (10,21,−1). This is exact in the limit and robust for ε<1/3. Alternatively keep 19/20 with a sub-ball, robust for ε<0.16.
- **E3 (L1).** "No condition links two different changes" is false for strict guidance in isolation, since it links r and r⁻¹.
  Corrected statement: "given strict score consistency, guidance, independence and protection are per-change constraints".
- **E4 (L4, wording).** "Each of mass 1" cannot be imposed on a given μ. Choose concentric balls of equal measure δ (Ex `ex:intransitive`) and rescale by 1/δ. Equal masses are in any case inessential at margin 1 with small ε.
- **Minor (auditor).** "H(r)≠Ω for dangerous r" holds for all non-null changes available to a coherent model. Its hypotheses are μ{P_S=0}=0, separability and an order unit (Rem `rem:orderunit`). It needs neither (M1) nor (M3).
- **Minor (auditor).** AC is used only to well-order Ω (A3).
