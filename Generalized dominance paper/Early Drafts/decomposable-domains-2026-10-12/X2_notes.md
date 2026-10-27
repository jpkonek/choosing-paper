# X2 — Joint two-sided comparison systems: a local extension theorem, and why no symmetric system has closed choice (round 26)

Scripts: `x2py/` — `pgeom.py` (exact geometry), `attribution_check.py`, `cycle_check.py`, `frag.py` + `scan.py` +
`run_frag.py` (exact finite fragments), each with its `.out`. The files `geom.py`, `ladder_tau.py`, `robust_inside.py`,
`wrong_blind_field.py` in `x2py/` predate this note (an earlier interrupted session). Nothing here relies on them.

Labels: PROVED (in this note, not refereed) / CHECKED (exact rational arithmetic on stated instances) / CONJECTURE /
NUMERICS. Notation as in the write-up §2. No assumption is added. Equivariance (§5) is a design choice of the
construction, and it is stated as a hypothesis wherever it is used. X3_notes.md was not in the folder when this note
was written.

---

## 0. Outcome

**No cover of T1 was constructed.** The attempt got through steps (1)–(3) of the brief, and **locally** through (4).
It fails at closed sections at the vertices, and that failure is a theorem.

1. **Selection (step 1).** I chose the **posterior family** K_p = ν(p ⊙ T1), the generalized-Bayes update of T1 by the
   likelihood vector p.
   - It is the unique selection through T1 that is equivariant under likelihood rescaling h ↦ d ⊙ h. That rescaling
     is a symmetry of the full domain and of every axiom.
   - It satisfies, automatically, every constraint that the full domain forces on any selection (Prop X2.2: precise
     vertices, edge support, vertex shrinking).
   - It has an exact description (Prop X2.6). C_p is the p-Bayes advice of a strictly guiding additive field. The one
     caution cost of an odd-favourable acceptance is attributed to the majority world with the larger p-weighted
     stake. So the whole non-additive task is to make this attribution p-dependent.
2. **Rules (steps 2–3): local extension theorem (Thm X2.7, PROVED).** The record rules are explicit, equivariant and
   balanced lexicographic, built on an invariant (Haar-type) measure. They satisfy:
   - strict (G), (IB) and closure under realizable composition;
   - competitiveness on supp p, undominatedness and absence of ties;
   - all of this for **every record bounded away from the coordinate planes, out of every coherent model, at every
     interior prior**.

   So every crossing configuration made of finitely many pieces is consistent, for every coherent selection.

   *Corollary X2.8.* Every finite whole-piece fragment of the X1/X3 type with interior priors is satisfiable. Finite
   searches without boundary or limit clauses therefore cannot certify an obstruction.
3. **The single proved obstruction (Thm X2.9).** Take the posterior selection. Assume strict (G), (IB),
   competitiveness at interior priors near e_k, and closed sections at e_k.
   - Then **no world k can have a rescaling-invariant set of accepted local records.**
   - Mechanism:
     - closed choice at e_k forces near-vertex acceptances (the vertex-domination lemma X2.2(c));
     - symmetry transports them to two interior selected models whose error sets cross on two pieces;
     - world k then accepts a swap and its reverse, plus an extra gain;
     - that is a strict guidance reversal.
   - The theorem holds for every ε and also for normalized boxes, which do have (non-symmetric) additive covers. So
     what fails is **symmetry**, not additivity.
   - In particular, the local rules of X2.7 are not the local part of any ranking with closed sections at a vertex.
4. **Also proved.**
   - The double-improvement lemma (X2.3). In any ranking with T1 ∈ C_L, **at most one world refines its wrong-advice
     charge and at most one refines its non-correct charge**. This sharpens L3.6(b)'s "at most two".
   - Vertex shrinking, d_H(K_p, e_k) → 0 (X2.2(d)).

**Nearby result (project preference).**
- Local consistency is free (X2.7).
- The cover problem on the full domain is entirely a problem about records that reach the coordinate planes, the
  "ends" that correspond to ∂Δ.
- There, the rescaling symmetry must be broken, at every world and already for local records (X2.9).
- The precise residual is Question Q_X2 (§6).

---

## 1. The full domain in record form

**Lemma X2.1 (PROVED).** Every a.e. mixed pair has a unique *majority orientation* h: two positive coordinates and one
negative. Call the index of the negative coordinate the *odd world* o(h), and let Q_o be the set of pairs with odd
world o.
- Positions: M (accept h only), S (silence), O (accept −h only), × (both).
- On Q_o, world i ≠ o ranks M < S < O < ×, and world o ranks O < S < M < ×.
- On unanimous pairs (h ≥ 0), every world ranks correct acceptance < S < wrong < ×.
- So on Q_o the two majority worlds have the same background order, and the odd world has its reverse on {M, S, O}.

*Proof.* Each sign pattern has a unique minority sign. The ranks are the background order of write-up §2, read in
this orientation. ∎

**Records.** I use the audit's transition lemma. X ⪯_i Y iff the transition record σ(X→Y) lies in A_i, where A_i
- contains the identity,
- is closed under realizable composition,
- contains every weak i-worsening,
- and contains no non-null i-improvement.

At a pair a record is either the identity or a move a → b along M–S–O–×. Two records compose iff, at every pair where
both are non-trivial, the end of the first is the start of the second.

*Ladder steps.* On Q_c, step A lies between M and S, and step B between S and O. An *O-ward* move crosses steps
towards O. It worsens both majority worlds and improves the odd world; an M-ward move does the reverse.

**Free records (PROVED).** A record out of C that weakly worsens some world i ∈ supp p everywhere satisfies (K) by (G).
At an interior prior, (K) has content only for *crossing* records, those that improve every world somewhere. Out of M
only O-ward moves exist, and out of O only M-ward moves.

Two consequences:
- A record made of M-ward moves on Q_i ∪ Q_j is a strict improvement for the third world k. So (K) needs i or j to
  accept it (pairwise sub-competitiveness).
- Moves that are O-ward on all three regions, or M-ward on all three, improve each world on one or two regions and
  worsen it on the rest. These are the crossing configurations.

---

## 2. What the full domain forces on every selection

**Proposition X2.2 (PROVED).** Take any ranking on the full domain with strict (G), and a selection that is
competitive on supp p with closed sections.

- **(a) Edge support.** If p lies in the open edge (e_i, e_j), then K_p ⊆ [e_i, e_j].
- **(b) Precise vertices.** C_{e_k} = B^k := {h : h_k > 0}.
- **(c) Vertex domination.**
  - Let P ⊆ Q_k be a cone of pairs whose closure lies in the open region, and put X_P := B^k with S on P.
  - Then there is a neighbourhood N_P of e_k such that, for every interior p ∈ N_P and every measurable F ⊆ E_k(C_p)
    (the pairs where C_p is not k-correct),
    C_p ⪯_k C_p[F → k-correct, P → S].
  - Moreover C_p is at O (k-correct) on a non-null part of P for p ∈ N_P.
- **(d) Vertex shrinking.** d_H(K_p, {e_k}) → 0 as p → e_k.

*Proof.*
- **(a)** On Q_l (l the third world), M is best for both i and j. If C_p is not at M on a non-null set, correcting
  that set gives X with X ≺_i C_p and X ≺_j C_p, against competitiveness on {i, j}. So D_{K_p} ⊇ {h_i, h_j > 0}. Let
  h_l → −∞; this gives m_l = 0 on K_p.
- **(b)** C_{e_k} ⪯_k X for every X, and B^k is the strict world-k optimum.
- **(c)**
  - On P, B^k is at O. O is wrong for both majority worlds j and l, and S is better for both. So X_P ≺_j B^k and
    X_P ≺_l B^k.
  - The sections {p : C_p ⪯_j X_P} and {p : C_p ⪯_l X_P} are closed and miss e_k. So they miss a neighbourhood N_P.
  - Competitiveness on Ω at interior p ∈ N_P gives C_p ⪯_k X_P.
  - Next compose with the pure k-worsening X_P → X_P^F. The model X_P^F carries C_p's advice on E_k(C_p) ∖ (F ∪ P)
    and agrees with X_P elsewhere. This gives C_p ⪯_k X_P^F, and X_P^F = C_p[F → correct, P → S].
  - If C_p were at M or S on almost all of P, the case F = E_k(C_p) ∖ P would give a record that is a pure
    k-improvement. It is non-null, because X_P is incoherent while C_p is coherent: the accepted set of X_P has a hole
    inside a convex cone. That contradicts strict (G).
- **(d)**
  - Fix δ > 0. Take P a small cone around h⁰ = (−δ, 1, 1), written in coordinates (k, j, l).
  - By (c), K_p ⊆ {m : m·h < 0} for some h ∈ P. This gives m_j + m_l < δ + η.
  - Hence K_p lies within O(δ) of e_k for every p ∈ N_P. ∎

(b) is L3.1(a) in the special case of the full domain, where it is immediate. (c) is the input of §6.

---

## 3. The double-improvement lemma

Let C be a selected model at an interior prior. Write O_c(C), S_c(C) and M_c(C) for the pairs of Q_c on which C is at
O, S and M respectively.

**Lemma X2.3 (PROVED).** Let the ranking satisfy strict (G), and let C be competitive on Ω. Fix distinct worlds i, j,
and let k be the third.

- **(DW)** For all non-null A ⊆ O_j(C) and B ⊆ O_i(C), put X := C[A ∪ B → S]. Then C ⪯_i X or C ⪯_j X.
- **(DW′)** For all non-null A ⊆ S_j(C) and B ⊆ S_i(C), put X := C[A ∪ B → M]. Then C ⪯_i X or C ⪯_j X.
- This applies to C = T1 in every ranking with T1 ∈ C_L.

*Proof.*
- Q_i and Q_j are majority regions for k. On both, O → S and S → M are k-improvements. So X ≺_k C by strict (G), and
  competitiveness leaves i or j.
- T1 ∈ C_L ties everywhere with a selected model (Thm kkm). It can replace that model in the selection (exact
  consistency test, closing remark). Since T1 is not edge-supported, X2.2(a) puts its prior in int Δ. ∎

What each world sees:
- In (DW), world i loses a silence step on B (its own odd region) and gains a wrong step on A. World j has the mirror
  image.
- In (DW′), world i loses a wrong step on B and gains a silence step on A.
- T1 has non-null O-, S- and M-sets in every region. For example h = (1, −.1, −.1) is accepted, and
  `x2py/scan.py` lists pieces of each kind.

**Corollary X2.4 (PROVED).** Take any ranking with strict (G), (S) and T1 ∈ C_L, on any domain with (LF) at T1. (Then
A and B can be taken near ∂D_{T1}, where (LF) makes S and M available.)

- **(a)** At most one world refines its wrong charge W_i (that is, W_i(X) < W_i(Y) ⇒ X ≺_i Y, with W_i a charge of
  i-wrong advice that is positive on non-null sets).
- **(b)** At most one world refines its non-correct charge N_i (the step-1 mass).

*Proof.*
- **(a)** In (DW), W_i(X) < W_i(T1). On A, O is i-wrong and becomes S. On B, O is i-correct, and S is not wrong. So
  X ≺_i T1. The same holds for j, and X ≺_k T1. Hence X dominates T1.
- **(b)** In (DW′), N_i(X) < N_i(T1). On A, S becomes i-correct. On B, S becomes M, which is still non-correct. Conclude
  as in (a). ∎

L3.6(b) allowed two wrong-first worlds; (a) allows one. Mixed pairs are not excluded: one W-first world and one N-first
world are compatible with (DW) and (DW′).

---

## 4. The selection: why the posterior family

**Proposition X2.5 (PROVED).** Let K_p := conv{ν(p ⊙ v_k)} = {ν(p ⊙ m) : m ∈ T1}. Then:
- K_u = T1;
- K_{e_k} = {e_k};
- K_p ⊆ [e_i, e_j] on that edge;
- p ↦ K_p is Hausdorff-continuous on Δ;
- the position of C_p at h equals the position of D_{T1} at p ⊙ h. Hence d*C_p = C_{ν(d⊙p)} for d ∈ ℝ³_{>0}, where
  d*X := d⁻¹ ⊙ X.

It is the only selection through T1 with this equivariance.

*Proof.* (p ⊙ v_k)·h = v_k·(p ⊙ h). The vertex, edge and continuity statements are immediate. For uniqueness: if
d*C_p = C_{ν(d⊙p)} and C_u = D_{T1}, then C_p = (3p)*D_{T1}. ∎

**Proposition X2.6 (attribution; PROVED, CHECKED).** Put λ := ε/c₀. Take a pair with majority orientation h and odd
world o.
- C_p is at M iff p·h + λ p_o h_o > 0.
- C_p is at O iff p·h + λ max_{j≠o} p_j h_j < 0.

Equivalently, C_p is the pointwise p-Bayes advice of the additive field with payoff losses and one caution term:
- F_i(h, M) = −h_i + λ 1[i=o] |h_o|;
- F_i(h, S) = 0;
- F_i(h, O) = h_i (1 + λ 1[i = a(h)]), with attribution a(h) = argmax_{j≠o} p_j h_j.

Every F_i is strictly guiding, whatever the attribution.

*Proof.* min_k and max_k of (p ⊙ v_k)·h ∝ p·h + λ p_k h_k are attained at k = o and at the majority argmax of p_j h_j
respectively. The guidance orders are read off the table. ∎

CHECKED: `attribution_check.out`, 20 000 random rational pairs and priors, 0 mismatches. It also checks the
equivariance identity.

So the selection is "Bayes up to one attribution". A **fixed** attribution a(h) gives an additive ranking, which
Thm gm excludes. Its Bayes models coincide with C_p only where argmax h_j = argmax p_j h_j; at p = u they coincide
everywhere, so T1 is that ranking's u-Bayes model. The non-additive task is exactly the p-dependence of a(h).

**Why this choice, against the alternatives** (the brief's item (1)).

| Family | Verdict |
|---|---|
| Bayes families of one additive field | Excluded by Thm gm. |
| Contamination families (1 − r(p)) p + r(p) Δ | By X2.2(a) and (d), r → 0 on ∂Δ, so the edges are precise (the L3.6(b) escape is available). Not equivariant, so each interior prior is a separate problem. |
| Plateau families (C_p = T1 on R) | By X2.2(a) and (d), R stays away from the vertices and the open edges. A plateau buys nothing for (K): the records out of T1 are the same at every p ∈ R. Closedness at ∂R forces {i : C_q ⪯_i X} ⊆ {i : T1 ⪯_i X} near ∂R, which is a real cost, and it breaks the symmetry. |
| Posterior family | Every forced constraint holds automatically. The symmetry reduces every interior requirement to the single prior u (Lemma X2.7a). |

Hence the posterior family was chosen.

---

## 5. The construction: equivariant joint systems

**Setting.**
- G′ := {d ∈ ℝ³_{>0} : d₁d₂d₃ = 1} acts on models by d*X = d⁻¹ ⊙ X. It preserves the full domain, null sets, sign
  patterns and the regions Q_o.
- On cone models, every scalar multiple of d acts the same way.
- An **equivariant system** has the posterior selection and world orders invariant under G′: X ⪯_i Y ⇔
  d*X ⪯_i d*Y. Equivalently, each A_i is invariant.

**Lemma X2.7a (reduction; PROVED).** In an equivariant system, (K), protection and (C) hold at every interior prior
iff they hold at u. For a fixed X, interior closedness of {p : C_p ⪯_i X} is closedness of
{d : T1 ⪯_i d⁻¹*X} in G′.

*Proof.* C_p ⪯_i X ⇔ T1 ⪯_i d⁻¹*X with d = 3p normalized, and d* acts bijectively on models. ∎

**Coordinates.**
- On each open orthant put ω(h) := (log|h₁/h₃|, log|h₂/h₃|) ∈ ℝ² and c(h) := |h₁h₂h₃|.
- G′ acts by translating ω and fixes c.
- Let ν := Leb(dω) ⊗ κ(dc), with κ a finite measure equivalent to Lebesgue (e.g. e^{−c}dc). It is G′-invariant and
  has the same null sets as μ off the coordinate planes.
- A record is **local** if, in each orthant, the ω-image of its support is relatively compact. In words, its
  supporting cones stay away from the coordinate planes. Such records have finite ν-mass. Every whole-piece record on
  cones bounded away from the planes is local.

**The rules.** For a local σ, let σ_{cs}(h) ∈ {−1, 0, 1} record an O-ward (+1) or M-ward (−1) crossing of step s at a
pair of Q_c. Let σ_U and σ_× record moves away from correct advice on unanimous pairs, and moves to ×.

- **World signs.** ε_i(c, s) = +1 if c ≠ i, and −1 if c = i.
- **Level 0.**
  m_i(σ) := Σ_{c,s} w_{ic} ε_i(c,s) ∫σ_{cs} dν + ∫σ_U dν + ∫σ_× dν,
  with w_{ii} = 2 and w_{ic} = 1 for c ≠ i.
- **Balance.** Σ_i w_{ic} ε_i(c,s) = −2 + 1 + 1 = 0. Hence Σ_i m_i(σ) = 3(∫σ_U + ∫σ_×) dν.
- **Levels n ≥ 1, common to all worlds.** A fixed sequence ψ_n:
  - the masses ∫ f_m(c) σ_{cs} dν, and likewise for U and ×;
  - then, class by class, the moments ∫ ω^α f_m(c) σ_{cs} dν;
  - f_m(c) := e^{−mc} for m ≥ 0. Their span is dense in C₀[0,∞) by Stone–Weierstrass, so together with the
    polynomials in ω they determine every finite signed measure of compact ω-support;
  - the pairs (α, m) are enumerated by |α| + m, so that every (β, m) with β < α comes before (α, m).
- **Acceptance.** World i accepts σ iff the sequence (m_i, s_i ψ₁, s_i ψ₂, …) is lexicographically ≥ 0, with
  (s₁, s₂, s₃) = (+, +, −).

**Theorem X2.7 (local extension theorem; PROVED).** Consider local records.

- **(a)** Each world's accepted set is closed under realizable composition, contains every weak i-worsening and
  contains no non-null i-improvement. So it defines a total preorder on every family of models whose pairwise records
  are local. (IB) holds by construction.
- **(b)** Each accepted set is G′-invariant.
- **(c)** Let C be any model that is correct on unanimous pairs and never gives ×; every coherent model is of this
  kind. Let σ ≠ 0 be a local record out of C. Then some world i has C ≺_i C ⊕ σ strictly. Hence:
  - (K) holds at every interior prior;
  - C ⊕ σ neither weakly dominates C nor ties it at every world;
  - so protection and (C) hold for these records.
- **(d)** In particular, every crossing configuration of finitely many pieces, out of every interior selected model of
  every coherent selection, is consistent with the axioms. The (DW)/(DW′) disjunctions of X2.3 are among them.

*Proof.*
- **(a)**
  - Realizable composition adds the vectors (σ_{cs}, σ_U, σ_×). Every level is linear. The set where the sequence is
    lexicographically ≥ 0 is therefore closed under addition.
  - A weak i-worsening has ε_i σ ≥ 0 in every class. The weights are positive and ν is equivalent to μ. So m_i ≥ 0,
    with equality only if σ = 0.
  - A non-null i-improvement has m_i < 0.
- **(b)**
  - ν is invariant, so m_i and every mass level are invariant.
  - A translation by δ changes ∫ω^α f_m σ by a combination of the ∫ω^β f_m σ with β < α (binomial expansion). These
    are earlier levels, so each level is invariant on the set where all earlier levels vanish. That set is the only
    place where the level is consulted.
- **(c)**
  - Out of such a C, σ_U ≥ 0 and σ_× ≥ 0, so Σ_i m_i ≥ 0.
  - If (m_i) ≠ 0, some m_i > 0.
  - If every m_i vanishes, all three worlds read the same sequence ψ_n up to sign. Let ψ_n be its first non-zero term.
    It exists because the masses and moments of all orders determine a signed measure of compact ω-support and finite
    κ-mass. Since the signs are not all equal, some world reads s_i ψ_n(σ) > 0.
  - In either case some world accepts σ strictly. That gives (K), and it excludes both weak domination and ties.
- **(d)** Immediate from (c). ∎

**Corollary X2.8 (PROVED).** Take any coherent selection and finitely many interior priors. Take finitely many pieces:
cones in open orthants, bounded away from the coordinate planes, on which the selected models have constant
positions. Then the exact fragment with clauses (G±), (T), (K) and (U) — the X1/X3 encoding, also on M_U — is
satisfiable.

NUMERICS agree (`run_frag.out`): 10 random 4-piece fragments for the posterior family at 7 interior priors, all SAT.

*Reading.*
- X2.7 is the locality barrier of round 12 in transition-record form. It holds on the full two-sided domain, for all
  interior selected models at once, and with an explicit invariant: balanced lexicographic levels.
- Its field is maximally degenerate. At the weight u every regular model is locally optimal, which is consistent with
  M3.10 (a cover needs blind sets).
- X2.7 cannot be extended to a full system with closed sections at a vertex, by the next theorem.

---

## 6. The single obstruction: symmetry is incompatible with closed choice at a vertex

**Theorem X2.9 (PROVED; geometry CHECKED).** Take the posterior selection on the full domain, and a ranking with
strict (G) and (IB). Assume competitiveness on Ω at interior priors near e_k, and closed sections at e_k for the
worlds j ≠ k and the models X_P = B^k ⊕ S(P). Then the set A_k ∩ {local records} is **not** G′-invariant.

In particular:
- no equivariant system satisfies these hypotheses;
- the local rules of X2.7 are not the local part of any such ranking, at any world.

The proof uses neither (C), nor (LA), nor T1 ∈ C_L.

*Proof.* Coordinates are (k, j, l), and on Q_k I write h = (−1, eˣ, eʸ) up to scale. The positions of D_{T1} are:
- O iff c₀(eˣ + eʸ − 1) + ε max(eˣ, eʸ) < 0;
- M iff c₀(eˣ + eʸ − 1) > ε;
- S otherwise.

The band S_k(T1) contains the asymptotic strip {x ≪ 0, β < eʸ < A}, with β = c₀/(c₀+ε), A = 1 + ε/c₀ and βA = 1. By the
symmetry j ↔ l it also contains the strip {y ≪ 0, β < eˣ < A}.

1. **Near-vertex local acceptances.**
   - Let P be the cone over a small box around (−1, 1, 1).
   - By X2.2(c), for p near e_k and every local F ⊆ E_k(C_p): ρ_p(F) := (F : C_p → k-correct; P : O → S) ∈ A_k.
   - C_p is at O on all of P for p near e_k, by X2.5: P is compact in the open region.
   - These records are local.
2. **Transport (invariance on local records only).**
   - For p = ν(t, 1, 1), the map h ↦ p ⊙ h, normalized into G′, carries C_p's configuration to T1's (X2.5).
   - So invariance gives ρ(F, t) := (F : T1 → k-correct; P_t : O → S) ∈ A_k for every local F ⊆ E_k(T1) and every
     t ≥ t₀. Here P_t := (t, 1, 1) ⊙ P.
   - P_t ⊆ O_k(T1) once t > 2 + ε/c₀, with a margin.
3. **Two interior selected models whose errors cross.**
   - Take t₁, t₂ ≥ t₀ and g := (1, 1/t₁, t₂) ∈ ℝ³_{>0}, acting on cones as its G′ normalization. Put Π₁ := P_{t₁} and
     Π₂ := g ⊙ P_{t₂}.
   - Π₂ is the cone over a box around (−1, 1/(t₁t₂), 1). This lies in the first strip: e^y is within 3% of 1, inside
     (β, A), and e^x is small.
   - g⁻¹ ⊙ Π₁ is the cone over a box around (−1, 1, 1/(t₁t₂)). This lies in the second strip.
   - Both are therefore in S_k(T1). Explicitly, on the whole box v_k·h = c₀(eˣ + eʸ − 1) − ε < 0, and the form of the
     larger majority coordinate is > 0. The box margins are checked in the cycle-check script.
   - So Π₂ is an error of T1 (silent) while Π₁ is k-correct for T1. Relative to C_{g·u} the roles are swapped.
4. **The cycle.**
   - Let E₁ ⊆ M_k(T1) be a cone piece disjoint from Π₁ and Π₂, e.g. around (−1, 3, 3).
   - By step 2:
     ρ₁ := ρ(Π₂ ∪ E₁, t₁) = (Π₁ : O→S, Π₂ : S→O, E₁ : M→O) ∈ A_k.
   - By step 2 with F = g⁻¹ ⊙ Π₁, transported by g:
     ρ₂ := (Π₁ : S→O, Π₂ : O→S) ∈ A_k.
   - Realize ρ₁ and then ρ₂. On Π₁ the moves are O→S→O; on Π₂ they are S→O→S; the middles match.
   - The composite record is (E₁ : M→O), a non-null pure k-improvement, since M is k-wrong on Q_k. It lies in A_k by
     transitivity. This contradicts strict (G). ∎

CHECKED: `cycle_check.out`, exact for (t₁, t₂) ∈ {(10,10), (100,37), (10³,10⁴), (10⁶,20)}, with g = (1, 1/t₁, t₂).
The script verifies:
- P_t ⊆ O_k(T1);
- both transported pieces lie in S_k(T1), certified by one form negative and one form positive on the whole box;
- E₁ ⊆ M_k(T1);
- B^k is at O on all pieces.

**Remarks.**
- **(i) What fails is symmetry, not additivity.** The proof uses three facts about the target:
  - its O-region contains the far pieces;
  - its band has two asymptotic strips;
  - the vertex models are precise.

  For a normalized box ν(∏[α_i, β_i]), the strip at x → −∞ is {α_k/β_l < eʸ < β_k/α_l}. It is non-empty unless
  α_kα_l = β_kβ_l. The same proof applies (PROVED by the same computation). Boxes do have additive covers (R10a), with
  non-invariant Gaussian penalties. So the theorem says that the problem's symmetry is never a symmetry of a solution
  with closed choice, already for boxes.
- **(ii) Relation to earlier obstructions.** Like L3.4, the failure is born at the boundary. Closed choice at e_k
  makes world k accept "a far silence outweighs any correction of C_p's errors". This is cheap near e_k, because
  C_p's errors are small there. Symmetry exports it into the interior, where it is ruinous.
- **(iii) Same mechanism without a contradiction.** Suppose bounded endorsers exist in an equivariant world k. The
  same records, with disjoint far pieces P_{t_n}, force every bounded endorser to vanish on all of T1's world-k error
  steps. That is the two-sided T1-shadow degeneracy of R21 (PROVED; subsumed by X2.9).

**What remains (Question Q_X2).** X2.7 and X2.9 together locate the problem. Every local configuration is
consistent. A cover with the posterior selection must have non-invariant local acceptance at every world. Its decisive
comparisons are those that reach the coordinate planes, where Δ's boundary lives. **Q_X2:**
- Is there a ranking with the posterior selection whose accepted local records are invariant **only along each
  edge's one-parameter subgroup**?
- Or one whose records reaching the planes are ranked by an end-level that breaks the symmetry?

X2.9 uses invariance under translations in two independent directions (along (t, 1, 1) and along g). One-parameter
invariance escapes it as stated (CONJECTURE: it still fails, through the two edges at e_k).

---

## 7. Status

| Item | Status |
|---|---|
| X2.1 record form of the full domain (majority orientation, chain, ladder) | PROVED |
| X2.2 (a) edge support, (b) precise vertices, (c) vertex domination, (d) vertex shrinking | PROVED |
| X2.3 double-improvement lemma; X2.4 at most one W-first and at most one N-first world | PROVED |
| X2.5 posterior family: properties, equivariance, uniqueness | PROVED |
| X2.6 attribution form of the posterior family | PROVED; CHECKED (20 000 exact cases) |
| X2.7a reduction to u; **X2.7 local extension theorem** (balanced Haar-lexicographic rules) | PROVED |
| X2.8 every finite whole-piece fragment with interior priors is satisfiable | PROVED; NUMERICS (10/10 SAT) |
| **X2.9 no rescaling-invariant local acceptance with closed choice at a vertex** | PROVED; geometry CHECKED |
| X2.9 for normalized boxes | PROVED (same computation) |
| Q_X2 (one-parameter invariance; symmetry-breaking end levels) | open; CONJECTURE that one-parameter invariance also fails |
| A cover of T1 on the full domain | not obtained |

**Referee priorities.**
1. X2.9, step 2. The transport uses only local records, and the normalization into G′ of h ↦ p ⊙ h is harmless
   because T1 is a cone.
2. X2.7(b). Invariance of each level on the zero set of the earlier levels, given the enumeration by |α| + m.
3. X2.2(c). The incoherence of X_P, which excludes the null record.
