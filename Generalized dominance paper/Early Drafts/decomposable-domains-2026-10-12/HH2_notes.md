# HH2 (round 36, BRIEF28). The principal constructive attempt under finite-chain consistency: what the weakening frees, the record-local rules it admits, and the obstruction they all meet

18 Oct 2026. Rules of BRIEF13. Labels:
- **PROVED**: full argument here (one reader, me; not refereed). Imports are named with their recorded status.
- **CHECKED**: exact rational computation with a stated script.
- **NUMERICS**: floating point or sampling. Nothing below rests on NUMERICS.
- **CONJECTURE**.

Scripts are in `hh2py/`. Run `python3 -I <script>.py` from inside that folder; outputs are in `*.out`. All verdicts
use `fractions.Fraction`.

Setting: the full four-advice domain (every measurable D ⊆ ℝ³ modulo null sets is evaluable), three worlds, T1 the
ε-contamination of u for any ε ∈ (0,1), notation of the write-up §2 and FF1 §1. Section 3 also uses VB's domain M_U.
Each world ≼_i is **reflexive** and is not assumed transitive. **(FC)** and **(TC)** are as in BRIEF28 and are kept
apart throughout. Strict (G), (IB), (LA), (S) (closed sections F_i(X) = {p : C_p ≼_i X} for every X, competitiveness
on supp p), (C) in its direct form, (LF) at T1 and T1 undominated are unchanged. No equal-profile quotient is used.
No assumption is added: every extra hypothesis below is a hypothesis of a stated result, and defines the class that
result is about.

---

## 0. Outcome

**No cover of T1 was obtained.** The attempt was carried through four designs. Each design satisfies the axioms
listed under it. Where it fails, the failure is an instance of one theorem (Theorem 5.1), which uses neither
transitivity nor (IB) nor closed sections.

1. **What (FC) frees, exactly (Prop 1.1; PROVED).** For a world given by an (IB) record set 𝒜:
   - transitivity says that the composite record ρ of every realisable chain of accepted records is accepted;
   - (FC) says only: **if ρ⁻¹ is accepted, then ρ is accepted**. (TC) says the same for chains of length 2.

   So the new freedom is to leave composites **incomparable**. It is not a failure of (IB) on composites: if ρ is
   accepted, every realisation of ρ is accepted, transported cancelled composites included. Consequences:
   - a complete world with (TC) is transitive (Cor 1.2). In particular **splicing a complete base gains nothing**:
     its splices are complete, so they are (TC) iff transitive;
   - deleting strict comparisons from an (FC) world keeps (FC) (Lemma 1.5);
   - two accepted records never compose to a strict improvement (Lemma 1.4);
   - every (FC) world has a potential (an ordering extension, not (IB)), and (IB) puts every accepted record into
     its context-uniform part (Prop 1.3).
2. **Extension theorem without transitive closure (Thm 2.1; PROVED).** Take defence points w(X) ∈ Δ, closed
   *pointed* defence cones, and caps C_p ≼_i X for p − w(X) ∈ Γ_i. Suppose every generator (worsening record or
   cap) is strictly monotone along **each of its own realisations** for an explicit lexicographic potential. Then
   the generators alone form a full system: (IB), reflexivity, strict (G), (FC), exact closed sections,
   competitiveness, (LA), (C), (LF), with every C_p undominated.
   - This is the next-best deliverable BRIEF28 asks for. It replaces EE1's monotonicity along all *closure* records
     by monotonicity along *generators*.
   - **Pointed cones are forced.** Coordinate thresholds are not pointed: their level-line ties would need a global
     strictly guiding tie-break that is constant on level lines.
   - **The four-model exchange survives.** EE1's (EX) still binds whenever the reverse selected comparison is
     accepted (Prop 2.2). EE1 Example 4.3 is a strict 3-model cycle in the threshold scheme with **no closure at
     all** (CHECKED). So (FC) does not rescue the threshold scheme. It only lets sparse (pointed) defences avoid the
     exchange.
3. **VB's failure uses no transitivity, nor anything else (Prop 3.2; PROVED, inputs CHECKED).** With VB's domain and
   selection there are **no relations whatsoever** satisfying strict (G), competitiveness and closed sections at two
   worlds. No (IB), transitivity, (C) or veto refinement is needed. The cause is the selection's jump at the
   vertices (Lemma 3.1, a general constraint on every selection).
4. **The principal constructive attempt: record-local additive ("arrow") rules (§4).**
   - **The arrow rule.** The plain posterior family is pointwise Bayes for a non-antisymmetric arrow cost, with
     friction on the arrows into O at the positive worlds (Prop 4.1; PROVED, CHECKED). The rule "accept a record iff
     its integrated arrow cost is ≥ 0" has (IB), reflexivity, strict (G), competitiveness of every C_p, closed
     sections and (LF).
   - **How it fails.** It has an explicit strict 3-model cycle, so it fails (TC) and (FC) (Prop 4.2; CHECKED). It
     also ties T1 with an incoherent model at all three worlds, so it fails (C) (Prop 4.3; CHECKED).
   - **No arrow rule can be repaired (Thm 4.4; PROVED modulo FF2's import chain).** Under (TC), every arrow cost is
     cyclically non-positive on the advices selected models use. Hence the world is endorsed by an integrable,
     strictly guiding additive penalty. FF2 Thm 4.1 then excludes every selection that is continuous in measure,
     competitive and passes through T1.
   - **Pair-indexed weightings (Thm 4.5; PROVED).** Take any rule whose verdict is a scale-invariant function of
     finitely many additive statistics of the record, for example a weighting density chosen from the record. Under
     (FC) it is endorsed by a single fixed weakly guiding field. It is excluded whenever that field can be taken
     strictly guiding (Cor 4.6). The only escape is a lexicographic acceptance cone, every endorser of which is blind.
5. **The single obstruction (Thm 5.1; PROVED modulo FF2 Thm 4.1 Steps 2–6).** Assume a selection continuous in
   measure through T1 and competitive. Then it is impossible that every world rejects small restrictions of each
   record that is improving for some fixed integrable strictly guiding field (property (Loc)). This uses no (IB),
   no transitivity, no (FC), no closed sections and no (C). Corollary 5.2 says (Loc) holds whenever the world is:
   - endorsed by such a field (FF2);
   - an arrow rule with (TC);
   - "locally arrow-linear" with (TC);
   - (FC) and (IB) with a real-valued ordering extension that is strictly differentiable, at any one model, with an
     integrable strictly guiding derivative.

   **Hence every (FC) cover through T1 with a continuous selection has a world that is non-Archimedean at
   infinitesimal scale.** Its small-record verdicts are not asymptotically linear in any arrow cost, and none of its
   ordering extensions is differentiable anywhere.
6. **What is left (§6; PROVED reduction, open core).** Start from a two-level lexicographic base. A scale-dependent
   exchange rate K(t) = k(μ(supp t)), with k → ∞ at 0, turns it into an (IB), strict-(G), (FC) world.
   - The new world has closed sections automatically (Prop 6.1). It is lexicographic at small scales, so Theorem 5.1
     does not bind, and Archimedean at large scales.
   - It is a deletion, which (FC) permits and transitivity does not. A cover follows from one missing ingredient,
     "k-competitiveness" of a continuous selection through T1 for the base.
   - GG1 Prop 3.1 still binds such worlds, so the base's leading level must charge T1 or interior selected models.

**Single most important open point.** Is there a two-level lexicographic base (Φ_i, Ψ_i)? Here Φ_i is weakly guiding
and charges the bulk near T1, and Ψ_i is strictly guiding. It needs a selection continuous in measure through T1 that
is **k-competitive** for some scale function k with k(m) → ∞ as m → 0: for every p and X, some i ∈ supp p must have
Φ_i(t) ≥ 0 and Ψ_i(t) + k(μ(supp t))Φ_i(t) ≥ 0, where t = rec(C_p, X). By Prop 6.1, Theorem 5.1 and the vertex
lemma, this is now the only kind of construction not excluded. A positive answer, with T1 protected in the base,
would be a full (FC) cover of T1.

---

## 1. Records, potentials, and what (FC) frees

### 1.1 Definitions

- **Records.** For models X, Y, rec(X,Y) is the measurable map h ↦ ι where X(h) = Y(h), and h ↦ (X(h), Y(h))
  elsewhere, modulo null sets. A *realisation* of a record t is any pair (X,Y) with rec(X,Y) = t. On the full domain
  every record has realisations: the common advice off supp t is arbitrary.
- **Chains.** Records t_1, …, t_k are *realised as a chain* by models A_0, …, A_k if rec(A_{s−1}, A_s) = t_s for every
  s. The *composite* of the chain is ρ := rec(A_0, A_k).
  - It depends only on (t_1, …, t_k). At a problem where some t_s is nontrivial, A_0(h) is the from-advice of the
    first nontrivial arrow and A_k(h) is the to-advice of the last. Elsewhere ρ(h) = ι.
  - Where the arrows cancel (A_0(h) = A_k(h) with some step nontrivial), ρ(h) = ι. Any realisation of ρ is then free
    to have any common advice there: these are the *transported cancelled composites* of FF1 §1 and EE1 §4.
- **(IB) as record sets.** On the full domain, (IB) says exactly that the verdict on (X,Y) depends only on rec(X,Y)
  (AUDIT_nonlinear_programme; FF1 §1). A world is therefore a set 𝒜_i of records with ι ∈ 𝒜_i, and
  X ≼_i Y ⟺ rec(X,Y) ∈ 𝒜_i.
- **Strict records.** r ∈ 𝒜_i is *strict* if r⁻¹ ∉ 𝒜_i. Then every realisation (X,Y) has X ≺_i Y.
- **Strict (G)** says: 𝒜_i contains every i-worsening record, and no non-null i-improving record (FF2 §1.1).
  - A record is *i-worsening* if its to-advice is weakly worse than its from-advice in world-i rank a.e.
  - It is *i-improving* if its inverse is i-worsening.
  - Every non-null i-worsening record is strict.
- **(FC):** A_0 ≼_i ⋯ ≼_i A_k ⇒ ¬(A_k ≺_i A_0).
- **(TC):** the case k = 2.

### 1.2 The exact freedom

**Proposition 1.1 (PROVED).** Let 𝒜 be an (IB) world (ι ∈ 𝒜).
- (a) 𝒜 is (FC) iff for every finite family of records of 𝒜 realised as a chain, with composite ρ: ρ⁻¹ ∈ 𝒜 ⇒ ρ ∈ 𝒜.
- (b) 𝒜 is (TC) iff the same holds for chains of two records.
- (c) ≼ is transitive iff ρ ∈ 𝒜 for every such chain.

*Proof.*
- A chain A_0 ≼ ⋯ ≼ A_k with A_k ≺ A_0 is a chain of records of 𝒜 with rec(A_k, A_0) = ρ⁻¹ ∈ 𝒜 and
  rec(A_0, A_k) = ρ ∉ 𝒜.
- Conversely, ρ⁻¹ ∈ 𝒜 and ρ ∉ 𝒜 for a realised chain give exactly such a configuration.
- (c) Transitivity installs rec(A_0, A_k) = ρ. ∎

*Reading.*
- Transitivity *installs* every composite ρ. (FC) installs ρ only when ρ⁻¹ is already accepted; otherwise ρ may stay
  incomparable.
- When ρ is accepted, (IB) accepts all its realisations, transported cancelled composites included. So the brief's
  phrase "composite comparisons need not obey independence" is true of the *ordering extension* (Prop 1.3), not of
  the world itself.

**Corollary 1.2 (PROVED).**
- (a) **Complete worlds.** If every record or its inverse lies in 𝒜, then (TC) implies transitivity.
- (b) **Splicing.** Let ≼′ be a splice of a complete base in the sense of SPLICING_summary:
  D ≼′_i D′ iff S_{D,D′}(D) ≼^H_i S_{D,D′}(D′). Then ≼′ is (TC) iff it is transitive.

  So for a complete base the author's strict 3-cycle (homothetic base) cannot be removed by passing to (FC). Only
  an incomplete base can profit.

*Proof.*
- (a) Take a 2-chain. If ρ ∉ 𝒜, completeness gives ρ⁻¹ ∈ 𝒜, and Prop 1.1(b) gives ρ ∈ 𝒜, a contradiction. So 𝒜 is
  closed under 2-step composition, and by induction under every chain.
- (b) N(D,D′) and p_{D,D′} are symmetric in D, D′, so S_{D,D′} = S_{D′,D}. A complete base therefore compares the
  two spliced models one way or the other. (IB) of ≼′ is the author's Prop (SPLICING_summary). Apply (a). ∎

**Proposition 1.3 (potentials; PROVED, importing Suzumura's extension theorem).**
- A reflexive relation ≼_i is (FC) iff it has an **ordering extension**. That is a complete preorder R_i ⊇ ≼_i with
  ≺_i ⊆ P(R_i) (Suzumura, *Economica* 1976; Bossert–Suzumura, *Consistency, Choice and Rationality*, 2010; the proof
  uses Szpilrajn's extension, hence choice).
- If moreover ≼_i is (IB), write Int(R_i) := {r : X R_i Y at every realisation (X,Y) of r}. Then:
  - every r ∈ 𝒜_i lies in Int(R_i);
  - every strict r ∈ 𝒜_i satisfies X P(R_i) Y at every realisation.
- Conversely, any complete preorder with these two properties certifies (FC).

*Proof.* The first sentence is Suzumura's theorem. An accepted record is accepted at all its realisations by (IB), and
R_i contains them. Strictness is likewise record-wise. For the converse: a chain with a strict reversal would give
A_0 R A_k P A_0. ∎

*Reading.* R_i need not be (IB). (IB) of the world forces every accepted record into the **context-uniform** part
Int(R_i): it must be R_i-monotone whatever common advice surrounds it. This is the precise sense of "potential but not
independent". It is also why smooth potentials fail (Cor 5.2(d)): for small records, Int(R) of a differentiable R is
governed by a fixed gradient field.

**Lemma 1.4 (PROVED).** Let world i have strict (G).
- Under (TC), no two records of 𝒜_i realised as a chain have a non-null i-improving composite.
- Under (FC), the same holds for chains of any length.

*Proof.* If ρ is non-null i-improving, then ρ⁻¹ is i-worsening, so ρ⁻¹ ∈ 𝒜_i and ρ ∉ 𝒜_i by strict (G). This
contradicts Prop 1.1(a) or (b). ∎

**Lemma 1.5 (PROVED).** Let 𝒜′ ⊆ 𝒜 be (IB) worlds, with 𝒜 (FC) (resp. (TC)). Suppose every strict record of 𝒜′ is
strict in 𝒜. Then 𝒜′ is (FC) (resp. (TC)). If moreover 𝒜′ contains every i-worsening record and 𝒜 has strict (G),
then 𝒜′ has strict (G).

*Proof.*
- Take a chain in 𝒜′ with ρ⁻¹ ∈ 𝒜′ and ρ ∉ 𝒜′. Then ρ⁻¹ is strict in 𝒜′, hence strict in 𝒜, so ρ ∉ 𝒜.
- But the chain lies in 𝒜, and ρ⁻¹ ∈ 𝒜, so Prop 1.1 for 𝒜 gives ρ ∈ 𝒜. This is a contradiction.
- Strict (G): 𝒜′ ⊆ 𝒜 contains no improving record. ∎

So **any record-wise deletion of strict comparisons from a transitive (IB) world with strict (G) is (FC)**, provided it
keeps the worsening records. Under transitivity such deletions are not available. Section 6 uses this.

---

## 2. An extension theorem without transitive closure

Fix an injective selection p ↦ C_p of coherent models with T1 = C_u (for example the plain posterior family; FF1
Lemma 4.2 gives injectivity). Write Σ for the selected models and τ(X) := 0 if X ∈ Σ, and 1 otherwise.

**Defence cones.** Let T := {x ∈ ℝ³ : Σx = 0}, and put φ_i(x) := x_i. Fix closed convex cones Γ_1, Γ_2, Γ_3 ⊆ T with
the following properties.
- (K1) **Pointed:** Γ_i ∩ (−Γ_i) = {0}.
- (K2) φ_i(x) = x_i > 0 for x ∈ Γ_i ∖ {0}.
- (K3) **Covering:** for all p, w ∈ Δ there is i ∈ supp p with p − w ∈ Γ_i.

*Example (PROVED).* The **argmax cones** Γ_i := {x ∈ T : x_i ≥ x_k ∀k}, with φ_i(x) := x_i.
- (K1): x, −x ∈ Γ_i force x_i = max_k x_k = min_k x_k, so x is constant, and x = 0.
- (K2): x_i = max ≥ mean = 0, with equality only if x = 0.
- (K3): if p ≠ w, the maximum of p − w is positive and is attained at some k with p_k > w_k ≥ 0. If p = w, any
  i ∈ supp p works.

**Data.**
- A *defence map* w : models → Δ with w(C_p) = p.
- Real functions G_i on models that are strictly guiding: G_i(X) < G_i(Y) whenever Y is weakly i-worse than X a.e.
  and strictly on a non-null set. Additive Brier losses will do.
- Generators at world i:
  - W_i, the i-worsening records (ι included);
  - K_i := {rec(C_p, X) : X ≠ C_p, p − w(X) ∈ Γ_i}, the caps.
- **No closure is taken:** 𝒜_i := W_i ∪ K_i.
- Potential Ψ_i(X) := (−φ_i(w(X)), τ(X), G_i(X)), ordered lexicographically.

Hypotheses:
- **(M)** every non-identity record of W_i ∪ K_i strictly increases Ψ_i along **every** realisation;
- **(E)** if a record of W_i ∪ K_i is realised by a pair (C_p, X) with X ≠ C_p, then p − w(X) ∈ Γ_i.

**Theorem 2.1 (PROVED).** Under (K1)–(K3), (M) and (E), the system 𝒜_1, 𝒜_2, 𝒜_3 has the following properties.
- (a) Reflexive, (IB), strict (G), (FC).
- (b) **Sections:** F_i(X) = {p : p − w(X) ∈ Γ_i} for X ∉ Σ, and F_i(C_q) = q + Γ_i (intersected with Δ). These are
  closed. Every C_p is competitive on supp p.
- (c) Every C_p is undominated. Every X ∉ Σ is dominated by C_{w(X)}. So U_L = C_L = Σ, and (LA) holds with T1 ∈ C_L.
- (d) No two distinct models are tied at any world, so (C) holds.
- (e) (LF) holds at T1.

*Proof.*
- **(a), (IB) and reflexivity.** 𝒜_i is a record set containing ι.
- **(a), (FC).** By (M), every non-identity accepted record strictly increases Ψ_i at every realisation. So the
  lexicographic preorder of Ψ_i is an ordering extension (Prop 1.3). There are no non-trivial ties, so it keeps
  strict parts.
- **(a), strict (G).** W_i ⊆ 𝒜_i. Suppose a non-null improving record d lay in K_i, and realise it as (X′, Y′). Then
  (M) for d gives Ψ_i(X′) < Ψ_i(Y′). But d⁻¹ ∈ W_i is realised by (Y′, X′), and (M) gives Ψ_i(Y′) < Ψ_i(X′).
- **(b), sections.** If rec(C_p, X) ∈ 𝒜_i with X ≠ C_p, then (E) gives p − w(X) ∈ Γ_i. Conversely such p are caps.
  For X = C_q, reflexivity adds q, which lies in q + Γ_i already.
- **(b), closedness and competitiveness.** w(X) + Γ_i is closed. (K3) gives competitiveness.
- **(c), protection.** Let Y ≠ C_p with Y ≼_i C_p at every i.
  - (M) at the realisation (Y, C_p) gives Ψ_i(Y) < Ψ_i(C_p). Hence w_i(Y) = φ_i(w(Y)) ≥ φ_i(p) = p_i for every i.
  - Both points lie in Δ, so w(Y) = p.
  - Then the second coordinate gives τ(Y) ≤ τ(C_p) = 0. So Y = C_q ∈ Σ with q = w(Y) = p, a contradiction.
- **(c), domination.** For X ∉ Σ, p := w(X) has p − w(X) = 0 ∈ Γ_i for all i. So C_p ≼_i X at every world, and
  X ⋠_i C_p because every non-identity accepted record is strict.
- **(d)** follows from (FC) with no ties.
- **(e)** holds on the full domain. ∎

*What is gained over EE1.*
- EE1 Thm 3.1 needs r-monotonicity along every realisation of every **closure** record. That is why it reduces to a
  clean fixed point of a lowering process (EE1 Thm 1.3), with the cascades of EE1 §4.
- (M) asks only for monotonicity along realisations of the **generators**. Nothing is lowered, nothing cascades, and
  any w with (M) and (E) is final.

*Why pointed cones.* With coordinate thresholds Γ_i = {x_i ≥ 0}, which are not pointed:
- closed sections force level-line ties C_p ~_i C_q when p_i = q_i;
- an ordering extension must then be **constant** along every realisation of every level-line record;
- that needs a global strictly guiding G_i constant on those realisations. For additive G_i this is
  G_i(C_p) = f(p_i) on all of Δ.

That is the global form of FF1 Thm 5.1, which FF1 explicitly neither claims nor needs (FF1 §5, remarks). Pointed cones
make the selected layer antisymmetric and closed, and remove this requirement.

**Proposition 2.2 (the exchange survives; PROVED, CHECKED).**
- (a) Let 𝒜_i be any (IB) world with (TC). Let records d_1, d_2 ∈ 𝒜_i be realised as a 2-chain with composite ρ,
  and suppose ρ⁻¹ ∈ 𝒜_i. Then ρ ∈ 𝒜_i.
- (b) Apply this to EE1's four-model exchange (EE1 Prop 4.2): caps rec(C_p, X), rec(C_q, Y) whose 2-chain composite
  is ρ = rec(C_s, C_z). Whenever rec(C_z, C_s) is accepted at i, so must be rec(C_s, C_z).
  - In the threshold scheme (exact sections p_i ≥ r_i(X)), z_i > s_i makes rec(C_z, C_s) a cap and rec(C_s, C_z)
    excluded. So **(EX) is necessary under (TC) with no closure taken**.
  - In Theorem 2.1 the reverse cap needs z − s ∈ Γ_i, so (EX) binds only on those configurations.

*Proof.*
- (a) is Prop 1.1(b).
- (b) EE1 Prop 4.2(a) gives the composite. An explicit 2-chain is W → W′ → W″, where W carries C_s's advice on
  D₁ ∪ D₂ and C_p's on C, and rec(W, W″) = rec(C_s, C_z).
- CHECKED on EE1 Example 4.3 (`exchange_fc.py` → `exchange_fc.out`):
  - W = (−,−,+), W′ = (+,+,+), W″ = (−,+,−);
  - rec(W,W′) = rec(C_p,X) and rec(W′,W″) = rec(C_q,Y), both world-1 caps;
  - rec(W″,W) = rec(C_z,C_s) is a cap (1/4 ≥ 1/12), while rec(C_s,C_z) is mixed and not a cap;
  - so W ≼_1 W′ ≼_1 W″ ≺_1 W, a strict 3-model cycle with no closure taken. ∎

*Reading.*
- EE1 Example 4.3 was presented as a closure phenomenon: SOM passes and the closure produces (F1). It is in fact a
  (TC) violation of the bare generators.
- So the threshold scheme does **not** become consistent by dropping transitivity. The only gain from (FC) on the
  exchange is that a sparse defence can leave rec(C_z, C_s) unaccepted.

---

## 3. VB revisited: its failure uses nothing but strict (G), competitiveness and closed sections

**Lemma 3.1 (PROVED).** Let ≼_1, ≼_2, ≼_3 be arbitrary relations on a decomposable domain, with strict (G) and a
selection competitive on supp q for every q. Let {i, j, k} = {1, 2, 3}, and suppose the sections at worlds i and k are
closed. Let X be a model with e_j ∉ F_i(X) ∪ F_k(X). Then e_j has a neighbourhood V in Δ such that:
- C_q ≼_j X for every q ∈ V;
- in particular, no C_q with q ∈ V is pointwise weakly j-worse than X and strictly j-worse on a non-null set.

*Proof.*
- F_i(X) ∪ F_k(X) is closed and misses e_j. Take V inside its complement, with V ⊆ {q_j > 0}.
- For q ∈ V, competitiveness gives some world in supp q accepting C_q ≼ X. It is not i or k, so it is j.
- The last clause is strict (G). ∎

**Proposition 3.2 (PROVED; inputs CHECKED).** Take VB's domain M_U (U = D_{K′}, K′ = u + s(T1 − u), 0 < s < 1) and VB's
selection: C_{e_j} = B^j := U ∩ {h_j > 0}, and C_q = U ∩ {q·h > 0} ∩ ⋂_m {v_m·h ≥ 0} for interior q (L3 §3). Then
**no** relations ≼_1, ≼_2, ≼_3 on M_U with this selection satisfy strict (G), competitiveness on supp q for every q,
and closed sections at two worlds.

*Proof.* Fix j, and let i, k be the two worlds with closed sections.
1. **The test set.** Let A := U ∩ {h_j > 0 > h_i, h_k} ∩ {v_i·h < 0}. It is open and non-null.
   - CHECKED (`vb_vertex.py` → `vb_vertex.out`): a point with all inequalities strict, for every ordered (i,j,k), for
     ε ∈ {1/20, 3/10, 1/2, 9/10} and s ∈ {1/4, 1/2, 9/10}.
   - Analytically, for h = (−a, 1, −b) with small b the constraints read (1−ε)σ < 3εa < σ(1−sε)/s, with
     σ = 1 − a − b. They are compatible iff s < 1.
2. **The test model.** Put X := B^j ∖ A.
   - B^j accepts A, which is i-wrong and k-wrong (h_i, h_k < 0). So X is pointwise weakly better than B^j at i and k,
     strictly on A.
   - Strict (G) gives X ≺_i B^j and X ≺_k B^j, so e_j ∉ F_i(X) ∪ F_k(X).
3. **Interior models are strictly j-worse than X.**
   - On A both reject: C_q ⊆ {v_i·h ≥ 0}.
   - Off A, X = B^j is j-best on M_U.
   - C_q differs from B^j on the non-null set P_k := U ∩ {h_i > 0, h_j > 0, v_k·h < 0}. There B^j accepts and C_q
     rejects; P_k is disjoint from A, and it is non-null by GG1 Cor 3.4, with a point CHECKED in the same script.
4. **Contradiction.** Lemma 3.1 forbids step 3 for interior q close to e_j. ∎

*Reading.*
- L3.4 (vetoes cannot be paid) needed "world i refines a paid veto". The obstruction to VB is more basic. Its interior
  selection does not converge to B^j at the vertices: it rejects the non-null one-positive set A, which B^j accepts.
- **No relation can serve that selection**, whether transitive, (FC) or neither.
- Lemma 3.1 is a constraint on **every** selection. For every non-null A ⊆ {h_j > 0 > h_i, h_k} (where B^j accepts),
  interior models near e_j must accept a non-null part of A, or be no worse at j than B^j ∖ A in some other way.
- The plain posterior family satisfies this. It is continuous in measure at the vertices, since C_q → {h_j > 0} as
  q → e_j.

*Consequence for repairs of VB.* GG1 Thm 3.3 excluded the credal repairs of VB (transitive). Prop 3.2 excludes every
repair that keeps VB's selection, whatever the relations. Any VB-like design must change the selection near the
vertices, so that interior models pay the vetoes there.

---

## 4. The principal constructive attempt: record-local additive rules

### 4.1 The arrow rule for the plain posterior family

**Notation.**
- Index pairs by the majority orientation h: either h > 0, or two positive coordinates j, l and one negative
  coordinate o (the *odd world*).
- Advice M (accept h only), S, O (accept −h only), × (both).
- λ := ε/c₀.

**Posterior advice.** For the plain posterior family C_p = {g : p⊙g ∈ D_{T1}} and mixed h:
- C_p(h) = M iff p·h + λp_o h_o > 0;
- C_p(h) = O iff p·h + λ max(p_j h_j, p_l h_l) < 0;
- C_p(h) = S otherwise.

On unanimous h, C_p(h) = M. C_p never gives ×. (Proof: the binding vertex of D_{T1} is k = o for acceptance of h,
and k = argmax_{j≠o} p_j h_j for acceptance of −h. This is the X2.6/FF2 §3 attribution.)

**Arrow costs.** For world i put c_i(h; a, b) := P_i(h, b) − P_i(h, a) + f_i(h; a, b), where:
- P_i(M) = −h_i − λ[i=o]h_o;
- P_i(S) = 0;
- P_i(O) = h_i(1 + (λ/2)[i≠o]);
- P_i(×) = (3+λ)|h_i| + λ|h_o|;
- friction f_i(h; a, O) = (λ/2)h_i[i≠o] for a ∈ {S, M}, and f_i = 0 on every other arrow;
- on unanimous h: P_i = −h_i, 0, h_i, 3h_i, and f_i = 0.

The **arrow rule** accepts a record r at world i iff κ_i(r) := ∫ c_i(h; a_r(h), b_r(h)) dμ ≥ 0, with c_i(h; a, a) := 0.

**Proposition 4.1 (PROVED; CHECKED).**
- (a) c_i has the strict sign of world-i rank change on every arrow, and an integrable envelope (|c_i| ≤ C(ε)|h|).
  Hence the arrow rule is reflexive, (IB), and has strict (G).
- (b) **Pointwise arrow-Bayes:** for every p ∈ Δ, a.e. h and every b ≠ C_p(h), Σ_i p_i c_i(h; C_p(h), b) ≥ 0. Hence
  every C_p is competitive on supp p.
- (c) Every section F_i(X) = {p : κ_i(rec(C_p, X)) ≥ 0} is closed.
- (d) (LF) holds at T1.

*Proof.*
- **(a)** Off the friction arrows, P_i is strictly increasing in world-i rank:
  - M < S < O < × at i ≠ o;
  - O < S < M < × at i = o;
  - M < S < O < × on unanimous h.

  Friction is added only on S→O and M→O at i ≠ o, which are worsening arrows there. (IB) holds because κ_i depends
  on the record alone. Strict (G) follows from the signs.
- **(b), C_p(h) = M.**
  - b = S gives p·h + λp_oh_o > 0.
  - b = O gives (p·h + λp_oh_o) + (p·h + λ(p_jh_j + p_lh_l)). Both terms are positive, since p·h > −λp_oh_o ≥ 0.
- **(b), C_p(h) = S.**
  - b = M gives −(p·h + λp_oh_o) ≥ 0.
  - b = O gives p·h + λ(p_jh_j + p_lh_l) ≥ p·h + λ max(p_jh_j, p_lh_l) ≥ 0.
- **(b), C_p(h) = O.**
  - b = S gives −p·h − (λ/2)(p_jh_j + p_lh_l) ≥ −p·h − λ max(·) > 0.
  - b = M adds −(p·h + λp_oh_o) > 0.
- **(b), the rest.** Arrows into × are positive at every world. On unanimous h every arrow out of M is positive at
  every world.
- **(b), competitiveness.** Integrate: Σ_i p_i κ_i(rec(C_p, X)) ≥ 0, so some i ∈ supp p has κ_i ≥ 0.
- **(c)** The plain family is continuous in measure on Δ (GG1 §3.3; FF2 Step 2). Along a subsequence of p_n → p the
  advice is eventually constant a.e. The integrand has an integrable envelope. So p ↦ κ_i(rec(C_p, X)) is
  continuous, and {≥ 0} is closed.
- **(d)** holds on the full domain. ∎

CHECKED (`arrow_rule.py` → `arrow_rule.out`), for ε ∈ {1/20, 3/10, 1/2, 9/10}:
- (a): 21 600 arrows on random rational h of every sign pattern, 0 failures;
- (b): 68 250 tests (p, h, b) with p ∈ Δ ∩ (1/12)ℤ³ (boundary and vertices included), 0 negative.

The friction is **forced** at every h for this family. The set {p : C_p(h) = O} is the convex wedge
{p·h + λp_jh_j < 0} ∩ {p·h + λp_lh_l < 0}, so the S/O boundary in p is kinked. An antisymmetric cost pair
c(S,O) = −c(O,S) would need it to be a line. This is FF2 §3's attribution mismatch, seen pointwise.

### 4.2 Where the arrow rule fails

**Proposition 4.2 (PROVED; CHECKED).** The arrow rule has a strict 3-model cycle at every positive world. Hence it
violates (TC), and so (FC).

*Proof.* Fix i ≠ o and a non-null bounded set S of mixed h with odd world o. On S, γ := c_i(S,O) + c_i(O,S) =
(λ/2)h_i > 0.
1. **Pieces.** Split S, by Lyapunov's theorem for the vector measure E ↦ (μ(E), ∫_E c_i(S,O), ∫_E c_i(O,S)), into
   three parts C₁, C₂, R, each carrying a third of every component. Take a non-null I ⊆ R with
   ∫_I |c_i(O,S)| < (1/3)∫_S γ.
2. **Models.** The three models agree off S and are:
   - X = (S on C₁, O on C₂ ∪ I);
   - Y = (O on C₁, S on C₂ ∪ I);
   - Z = (S on C₁, O on C₂, S on I).
3. **Values.**
   - κ_i(X→Y) = (1/3)∫_Sγ + ∫_I c_i(O,S) > 0.
   - κ_i(Y→Z) = (1/3)∫_Sγ > 0.
   - rec(X, Z) is O→S on I, a non-null i-improvement.
4. **Conclusion.** Strict (G) gives Z ≺_i X while X ≼_i Y ≼_i Z. ∎

CHECKED on an atomic surrogate, at h* = (1,1,−1), world 1, for each ε. For example, ε = 3/10 gives
κ(X→Y) = 9/28, κ(Y→Z) = 9/14, κ(Z→X) = 72/161 and κ(X→Z) = −9/28.

**Proposition 4.3 (PROVED; CHECKED).** The arrow rule also violates (C).

*Proof.* Choose a mixed h with o = 3, T1(h) = S, and Σh + (λ/2)(h_1 + h_2) < 0. Such h exist: take h_1 ≫ h_2, so that
λ max exceeds λ·mean.
1. **The model.** Let B be a small ball around h on which these strict inequalities persist. Let B′, B″ be its images
   under the cyclic coordinate permutations. Put Y := T1 with advice O on B ∪ B′ ∪ B″.
2. **Symmetry.** μ and the family of costs are permutation-equivariant. So at every world,
   - κ_i(Y→T1) = ∫_B Σ_k c_k(O,S) = −∫_B (Σh + (λ/2)(h_1+h_2)) > 0;
   - κ_i(T1→Y) = ∫_B (Σh + λ(h_1+h_2)) > 0.

   So Y is tied with T1 at all three worlds.
3. **Y is incoherent.** If Y = D_K a.e., then D_K ⊇ D_{T1} a.e., so K ⊆ T1. And D_K ∖ D_{T1} is contained in a bounded
   set. A cone that is null outside a bounded set is null (DD1 Lemma 2.7), so K = T1 and Y = T1 a.e., which it is
   not.
4. **Conclusion.** (C) fails if T1 ∈ C_L. If T1 ∉ C_L, coverage fails. ∎

CHECKED (`arrow_rule.py` (e)) at an exact mismatch point for each ε; for ε = 3/10, κ(Y→T1) = 309/280 and
κ(T1→Y) = 177/700 at every world.

### 4.3 No arrow rule can be repaired

Call a world an **arrow rule** if it accepts r iff ∫c_i(h; a_r, b_r) dμ ≥ 0, for a measurable cost c_i with the strict
sign of rank change on every arrow and an integrable envelope. Its friction may be anything.

**Theorem 4.4 (PROVED modulo FF2 Thm 4.1 Steps 2–6 and their import chain).**
- (a) If an arrow rule is (TC) at world i, then a.e. every cycle of distinct advices in {M, S, O} has non-positive
  c_i-sum.
- (b) Consequently there is a strictly guiding penalty ℓ_i with integrable envelope such that
  c_i(h; a, b) ≤ ℓ_i(h, b) − ℓ_i(h, a) for all a ∈ {M, S, O} and all b. In particular every accepted record out of a
  model that never gives × is endorsed: ∫(ℓ_i(Y) − ℓ_i(X)) ≥ 0.
- (c) No system whose three worlds are arrow rules with (TC) admits a selection continuous in measure, competitive on
  supp q for every q, and with T1 = C_{q₀}.

*Proof.*
1. **2-cycles.** Suppose γ := c(a,b) + c(b,a) > 0 on a non-null set S. One of a→b, b→a is an i-improvement. The
   construction of Prop 4.2 gives a strict 3-model cycle, which contradicts (TC); it used no property of c beyond
   this.
2. **3-cycles.** Suppose γ := c(a,b) + c(b,c) + c(c,a) > 0 on a non-null S. Let γ′ := c(a,c) + c(c,b) + c(b,a) be the
   reverse sum. Then γ + γ′ is the sum of the three 2-cycle sums, so γ′ ≤ −γ < 0 a.e. on S by step 1.
   - **Pieces.** Split S by Lyapunov into thirds C₀, C₁, C₂ for the vector measure of all six arrow densities and μ.
   - **Walks.** Over the two steps the walks are a→b→c on C₀, b→c→a on C₁ and c→a→b on C₂.
   - **Values.** Each step has value (1/3)∫_S γ > 0. The composite record has arrows a→c, b→a, c→b, so its value is
     (1/3)∫_Sγ′ < 0, and it is rejected. Its inverse has value (1/3)∫_Sγ > 0, and it is accepted.
   - This is a strict 3-model cycle, contradicting (TC).

   No other simple cycles exist on three advices.
3. **The potential.** Let g(h) be the world-i best advice. Set ℓ_i(h, a) := max over paths in {M, S, O} from g(h) to
   a of the c_i-sum. This is well defined by steps 1–2, measurable, and |ℓ_i| ≤ Σ|c_i|. Then:
   - ℓ_i(b) ≥ ℓ_i(a) + c_i(a,b) for a, b ∈ {M, S, O};
   - put ℓ_i(×) := max_a (ℓ_i(a) + c_i(a,×));
   - for a worsening arrow, c_i(a,b) > 0 gives ℓ_i(b) > ℓ_i(a). So ℓ_i is strictly guiding with × last.
4. **Endorsement.** For an accepted record r whose from-advice avoids ×,
   ∫(ℓ_i(b_r) − ℓ_i(a_r)) ≥ ∫c_i(r) ≥ 0. Selected models never give ×.
5. **(c).** Hypotheses (H1)–(H3) of FF2 Thm 4.1 hold with ℓ = (ℓ_1, ℓ_2, ℓ_3). (H3) holds for every X, not only those
   equal to C_q off H_n. FF2 Thm 4.1 gives the contradiction. Its status: CORRECT modulo D1, BB2 Thm 6.1 and
   M3.7–M3.8 (GG3 §8.1). ∎

*Reading.*
- Under (TC), friction must be sub-potential. Super-potential friction makes strict cycles (Prop 4.2). Sub-potential
  friction makes the world endorsed by one additive field, which FF2 excludes.
- The posterior family needs super-potential friction (§4.1). So **among record-local rules whose weighting depends
  on the record only pointwise (through the arrow), none works, under (TC) or (FC)**.
- Pointwise arrow-Bayes was not assumed: (c) uses only competitiveness.

### 4.4 Pair-indexed weightings that depend on the whole record

BRIEF28 suggests a weighting chosen from the record itself, for example from its disagreement region as in the
author's splicing. A large natural class makes the verdict a scale-invariant function of finitely many additive
statistics of the record.

**Definition.**
- Let φ : H × {M, S, O, ×} → ℝ^K be measurable and integrable, and put V(r) := ∫(φ(h, b_r(h)) − φ(h, a_r(h))) dμ.
- World i is a **statistics rule** if r ∈ 𝒜_i ⟺ V(r) ∈ 𝒦_i, for a set 𝒦_i ⊆ ℝ^K invariant under positive scaling.
- Example: accept iff ∫ρ_{π(r)}(ℓ_i(b_r) − ℓ_i(a_r)) ≥ 0, with ρ_π = Σ_k π_k ρ_k and an index π(r) depending
  0-homogeneously on V(r), such as a least-norm argmin like σ(v).

**Theorem 4.5 (PROVED).** Let world i be a statistics rule with strict (G) and (FC). Then there is λ ∈ ℝ^K, not
orthogonal to the span of V(all records), such that every accepted record has λ·V(r) ≥ 0. The field ℓ^λ := λ·φ is
weakly guiding at world i (≥ 0 on every worsening arrow, a.e.) and endorses every accepted record.

*Proof.*
1. **Setup.** Let R := {V(r)}. It is symmetric, since V(r⁻¹) = −V(r). Let 𝒱 := span R, and let 𝒞 be the convex cone
   generated by 𝒦_i ∩ R.
2. **Worsening records are detected.** If w is non-null and i-worsening, then V(w) ≠ 0. Otherwise V(w⁻¹) = 0 = V(ι)
   ∈ 𝒦_i, and the improving w⁻¹ would be accepted.
3. **Claim: −V(w) ∉ 𝒞.** Suppose −V(w) = Σ_{j≤k} t_j v_j with t_j > 0 and v_j = V(r_j), r_j ∈ 𝒜_i. Put T := Σ t_j.
   - **Partition.** Apply Lyapunov's partition theorem (Dvoretzky–Wald–Wolfowitz) to the non-atomic vector measure
     E ↦ (∫_E (φ(b_{r_j}) − φ(a_{r_j})) dμ)_{j≤k}. It gives disjoint P_1, …, P_k with
     V(r_j|_{P_j}) = (t_j/T)v_j. These lie in 𝒦_i (cone), so the restrictions are accepted.
   - **Chain.** They have disjoint supports, so they are realised as a chain from any model with the right
     from-advice on each P_j.
   - **Contradiction.** The composite has V = −V(w)/T. That is not in 𝒦_i, because −V(w) = V(w⁻¹) ∉ 𝒦_i. Its inverse
     has V = V(w)/T ∈ 𝒦_i. This is a strict reversal, contradicting (FC).
4. **λ exists.** So 𝒞 ≠ 𝒱. A convex set whose closure is the whole space 𝒱 is 𝒱, so cl 𝒞 is a proper closed convex
   cone. Some λ ∈ 𝒱* ∖ {0} is ≥ 0 on it.
5. **Weak guidance.** Records "a→b on E", for a worsening arrow and any E, are accepted. So λ·∫_E (φ(b) − φ(a)) ≥ 0
   for all E, and λ·(φ(h,b) − φ(h,a)) ≥ 0 a.e. ∎

**Corollary 4.6 (PROVED modulo FF2 Thm 4.1's chain).** Suppose every world is a statistics rule with (FC) whose
endorser can be chosen strictly guiding. Then no selection continuous in measure through T1 is competitive.

This holds, for instance, when the closed cone W generated by the worsening vectors is pointed and −W ∩ cl 𝒞 = {0}.
- Separate a compact base of W from the closed cone −cl 𝒞. This gives λ ≥ 0 on cl 𝒞 and λ > 0 on W ∖ {0}.
- Then λ·(φ(h,b) − φ(h,a)) vanishes on no non-null set of worsening arrows, so λ·φ is strictly guiding.

*Reading.*
- The escape left by Theorem 4.5 is **blindness of every endorser**: cl 𝒞 contains a reversed worsening direction.
- The basic case is 𝒦 = {λ·V > 0} ∪ {λ·V = 0, μ′·V ≥ 0}, which is lexicographic. Then strictness lives in a second
  statistic that the closed cone does not see. Every (FC) statistics rule is a sub-relation of such a lexicographic
  preorder.
- So pair-indexed weighting does not create new local structure under (FC). It reproduces a fixed weighting, possibly
  with lexicographic tie-breaks. This is where §6 starts.

---

## 5. The obstruction

FF2 Thm 4.1 assumed that a single integrable strictly guiding field **endorses** every local accepted comparison out
of selected models. The proof needs much less. It needs only that accepted comparisons are not **small** improvements
for that field.

**Definition ((Loc_i)).** Let ℓ_i be a strictly guiding penalty with integrable envelope, and H_n an increasing
sequence of measurable sets with ⋃H_n co-null. For a record r write Δℓ_i(r) := ℓ_i(h, b_r(h)) − ℓ_i(h, a_r(h)).

World i satisfies **(Loc_i)** if the following holds for every q with i ∈ supp q, every n, and every record r out of
C_q (that is, C_q = a_r on supp r) with supp r ⊆ H_n and ∫Δℓ_i(r) dμ < 0. There is t₀ > 0 such that r|_E ∉ 𝒜_i for
every measurable E ⊆ supp r with:
- μ(E) < t₀ μ(supp r);
- ∫_E Δℓ_i(r) ≤ (μ(E)/2μ(supp r)) ∫Δℓ_i(r).

Here r|_E is r on E and ι elsewhere.

**Theorem 5.1 (PROVED modulo FF2 Thm 4.1 Steps 2–6 and their import chain).** On the full domain with three worlds
and T1 the ε-contamination of u, let ≼_1, ≼_2, ≼_3 be any relations. Let q ↦ C_q be a selection of coherent models,
continuous in measure on Δ, competitive on supp q for every q, with T1 = C_{q₀}. Then there is no field
ℓ = (ℓ_1, ℓ_2, ℓ_3) and exhausting (H_n) for which (Loc_i) holds at every world.

*Proof.*
1. **Weak Bayes on each H_n.** Fix q, J := supp q, and n. Suppose no w ∈ Δ_J makes C_q a pointwise weak w-Bayes model
   of ℓ a.e. on H_n.
   - **Separation.** The set Z_n := {(∫Δℓ_i(rec(C_q, X)))_{i∈J} : X = C_q off H_n} is convex by Lyapunov (FF2 Step 1,
     refereed GG3 §8.1), and contains 0.
   - If Z_n missed the open negative orthant, separation and the measurable-switch argument of FF2 Step 1 would give
     such a w.
   - So some X has ∫Δℓ_i(r) < 0 for all i ∈ J, where r := rec(C_q, X).
2. **A small strict improvement.** By Lyapunov applied to E ↦ (μ(E), (∫_E Δℓ_i(r))_{i∈J}) on supp r, for every
   t ∈ (0,1) there is E_t with μ(E_t) = tμ(supp r) and ∫_{E_t} Δℓ_i(r) = t∫Δℓ_i(r) for all i ∈ J.
   - For t < min_{i∈J} t₀(i), (Loc_i) rejects r|_{E_t} at every i ∈ J.
   - So C_q is not competitive on J against C_q ⊕ r|_{E_t}. This is a contradiction.
3. **Weak Bayes everywhere.** So for every n some w_n ∈ Δ_J gives (WB) a.e. on H_n. A limit point gives (WB) a.e.,
   exactly as in FF2 Step 1. Hence W(q) ∩ Δ_{supp q} ≠ ∅ for every q, with W(q) as in FF2.
4. **Conclusion.** FF2 Steps 2–6 use only this, continuity in measure, T1 = C_{q₀}, and properties of ℓ. They give the
   contradiction. ∎

**Corollary 5.2 (PROVED, same status).** (Loc_i) holds in each of the following cases. So in each case, if every world
is of the stated kind, no such selection exists.
- (a) **Endorsement:** C_q ≼_i X ⇒ ∫(ℓ_i(X) − ℓ_i(C_q)) ≥ 0 for X = C_q off H_n. This is FF2's (H3).
- (b) **Arrow rules with (TC):** by Thm 4.4(b).
- (c) **Locally arrow-linear worlds with (IB) and (TC).**
  - *Definition.* There is a cost c_i as in §4.3 such that for every n and η > 0 there is ε > 0 with the following
    property. Every record r with supp r ⊆ H_n and μ(supp r) < ε is accepted if ∫c_i(r) ≥ ημ(supp r), and rejected
    if ∫c_i(r) ≤ −ημ(supp r).
  - *Proof.* Run the cycle constructions of Prop 4.2 and Thm 4.4 inside a subset S of {γ ≥ γ₀} ∩ H_n with μ(S) < ε.
    Their normalised margins depend only on γ₀, so they are uniform. Hence c_i is cyclically non-positive on
    {M, S, O}, and the potential ℓ_i of Thm 4.4 exists. A small restriction with normalised ℓ_i-value ≤ −η then has
    normalised c_i-value ≤ −η (since c_i ≤ Δℓ_i on arrows out of {M, S, O}), and is rejected.
- (d) **(FC) and (IB) with a differentiable ordering extension.**
  - *Definition.* Some ordering extension R_i of world i (Prop 1.3) is represented by Ψ_i : models → ℝ. There is a
    model Z_i such that for every n and η > 0 some ε > 0 has the following property. For all models X, Y with
    X △ Y ⊆ H_n and μ(X △ Z_i), μ(Y △ Z_i) < ε:
    |Ψ_i(Y) − Ψ_i(X) − ∫(ℓ_i(Y) − ℓ_i(X))| ≤ η μ(X △ Y).
  - *Proof.* Realise r|_E as (X′, X′ ⊕ r|_E) with X′ := C_q on E and Z_i elsewhere. Then Ψ_i decreases strictly for
    η < |∫Δℓ_i(r)|/(2μ(supp r)). So r|_E ∉ Int(R_i) ⊇ 𝒜_i.
  - Example: Ψ_i = G(L¹, …, L^m) with additive integrable L^k, G of class C¹, and Σ_k ∂_kG ℓ^k strictly guiding at
    one point. This covers every smooth non-additive potential.
- (e) **Statistics rules** (Thm 4.5) whose endorser is strictly guiding, by (a).

**Corollary 5.3 (what every cover needs; PROVED, same status).** Let a system with (FC) and (IB) have a selection
continuous in measure through T1 that is competitive. Then **some world i satisfies (Loc_i) for no choice of
integrable strictly guiding ℓ_i**. In particular, at that world:
- the world is not endorsed on local comparisons out of selected models by any such field (FF2 Cor 4.3);
- it is not an arrow rule, and not locally arrow-linear for any cost. Its verdicts on small records are not
  asymptotically governed by the sign of a fixed linear functional of the record;
- **no** real-valued ordering extension is strictly differentiable with an integrable strictly guiding derivative at
  **any** model;
- if it is a statistics rule, every endorser is blind (lexicographic acceptance cone).

The same holds under (TC) for the arrow and arrow-linear clauses.

*Proof.* If every world had such an ℓ_i, Theorem 5.1 would apply to (ℓ_1, ℓ_2, ℓ_3). ∎

*What is used.*
- Used: competitiveness, continuity in measure of the selection, T1 = C_{q₀}, the full domain, and FF2's import chain.
- (FC), (TC) and (IB) enter only through the corollaries that verify (Loc).
- Not used: closed sections, (C), (LA), and strict (G) of the ranking, except in Cor 5.2(b)–(d).

*Caveat (T1 tied but not selected).* GG3 §8.3 repaired FF2 for covers in which T1 is only tied with a selected C_{q₀}
(Thm 4.1′). It did so using "T1 is competitive on supp q₀", which follows from T1 ≼ C_{q₀} ≼ X **by transitivity**.
- Under (FC) one gets only ¬(X ≺_i T1), which may hold by incomparability.
- So Theorem 5.1 and Cor 5.3 are stated for selections **through** T1, which is the brief's setting (the plain
  posterior family).
- Whether an (FC) cover could exploit an unselected T1 is not examined here.

---

## 6. What is left: lexicographic at small scales, Archimedean at large scales

Corollary 5.3 forces some world to be non-Archimedean at infinitesimal scale. Theorem 4.5 shows that in the
statistics class this means a lexicographic acceptance cone. Transitive lexicographic (NA-credal) worlds lose closed
sections in every known instance: VB (L3.4), FF2's P (Cor 2.5) and D2's hull (GG3 Prop 5.4). (FC) offers a remedy that
transitivity does not: **delete** the strict lexicographic comparisons that break closedness (Lemma 1.5), with a
record-wise rule.

**Proposition 6.1 (PROVED).** Let world i have a two-level lexicographic base L_i = (Φ_i, Ψ_i): additive with
integrable densities, Φ_i weakly guiding and Ψ_i strictly guiding. For a record t write Φ_i(t), Ψ_i(t) for its
increments. Let k : (0, ∞) → (0, ∞) be continuous, and put K(t) := k(μ(supp t)). Define

  𝒜_i^k := {ι} ∪ {t : Φ_i(t) ≥ 0 and Ψ_i(t) + K(t)Φ_i(t) ≥ 0}.

Then:
- (a) 𝒜_i^k is reflexive and (IB), with strict (G).
- (b) Every strict record of 𝒜_i^k is strict in the lexicographic preorder L_i. So 𝒜_i^k is (FC) (Lemma 1.5), with
  ordering extension L_i.
- (c) Ties in 𝒜_i^k are exactly lexicographic ties (Φ_i(t) = Ψ_i(t) = 0).
- (d) If the selection is continuous in measure, every section {p : rec(C_p, X) ∈ 𝒜_i^k} is closed.
- (e) If k(m) → ∞ as m → 0, verdicts on small records are lexicographic. If k ≡ K is constant, 𝒜_i^k is the
  intersection of the two additive relations {Φ_i ≥ 0} and {Ψ_i + KΦ_i ≥ 0}. Then Ψ_i + KΦ_i is a real strictly
  guiding endorser, so FF2 Thm 4.1 (GG3 Prop 6.3) excludes it for continuous selections.

*Proof.*
- **(a)** A worsening t has Φ_i(t) ≥ 0 and Ψ_i(t) > 0, so it is accepted. An improving t has Φ_i(t) ≤ 0 and
  Ψ_i(t) < 0, so Ψ_i + KΦ_i < 0 and it is rejected. (IB) holds because acceptance is a function of the record.
- **(b)** Let t ∈ 𝒜^k with t⁻¹ ∉ 𝒜^k. If Φ_i(t) > 0, t is L-strict. If Φ_i(t) = 0, then Ψ_i(t) ≥ 0, and t⁻¹ ∈ 𝒜^k
  iff Ψ_i(t) ≤ 0. So Ψ_i(t) > 0, and t is L-strict.
- **(c)** If t, t⁻¹ ∈ 𝒜^k, then Φ_i(t) = 0 and ±Ψ_i(t) ≥ 0.
- **(d)** Let t_p := rec(C_p, X). By continuity in measure and integrability, p ↦ Φ_i(t_p) and p ↦ Ψ_i(t_p) are
  continuous, and so is p ↦ μ(supp t_p) = μ(C_p △ X).
  - **X ∉ Σ.** μ(C_p △ X) ≥ min_q μ(C_q △ X) > 0, since the selected family is compact in measure as a continuous image
    of Δ. So K(t_p) is continuous, and the section is closed.
  - **X = C_q.** K(t_p) is continuous off p = q, and q belongs to the section by reflexivity. Any limit point of the
    section other than q is a continuity point.
- **(e)** is immediate. ∎

*What this does and does not give.* Choose k with k(m) → ∞ as m → 0.
- **Theorem 5.1 does not bind.** Small records are judged lexicographically, so (Loc_i) fails whenever Φ_i is not
  blind on the relevant local records.
- **FF2 Cor 4.2 binds if Φ_i is blind on every H_n.** So Φ_i must charge the bulk near T1.
- **GG1 Prop 3.1 still binds.** Its test comparisons have Φ-increment 0 and Ψ-increment > 0, so 𝒜^k keeps them, and
  its proof transfers verbatim. Hence GG1 Thm 3.3 applies on M_U to (U2)-type bases with (P0) and (V): T1 or interior
  selected models must pay leading costs (GG1 Prop 4.1).
- **The vertex lemma (Lemma 3.1) binds every selection.** On M_U with veto-type leading levels, interior models near
  e_j must accept the vetoed one-positive sets.
- **The remaining requirement is k-competitiveness**: for every p and X, some i ∈ supp p with Φ_i(t) ≥ 0 and
  Ψ_i(t) + k(μ(supp t))Φ_i(t) ≥ 0.
  - It is stronger than lexicographic competitiveness only for records with Φ_i(t) > 0 > Ψ_i(t). There the
    exchange rate must be at least |Ψ_i(t)|/Φ_i(t).
  - The rate is allowed to grow without bound only as the record shrinks.

**Corollary 6.2 (PROVED).** Suppose the bases L_1, L_2, L_3 and a selection continuous in measure through T1 are
k-competitive for some continuous k. Suppose also that T1 is undominated in the system 𝒜^k and that (C) holds there.
Then 𝒜^k is a full cover of T1 under (FC).

Sufficient for the last two conditions: T1 undominated in the lexicographic base, and three-world lexicographic ties
with **selected** models only trivial, as in VB's vector-uniqueness argument (L3.3(b)).
- The KKM argument needs no transitivity. It shows that every undominated B in 𝒜^k satisfies C_{p\*} ≼_i B at every
  world for some p\*, and none of these comparisons is strict, so B is tied with C_{p\*} at every world.
- With trivial ties, C_L^k ⊆ Σ, and a model tied with a member of C_L^k equals it.

*Proof.*
- Prop 6.1 gives (IB), reflexivity, strict (G), (FC) and closed sections. k-competitiveness gives competitiveness.
- Domination in 𝒜^k implies domination in L, since the comparisons are a subset and strict comparisons stay strict
  (6.1(b)). So undominatedness transfers from the base.
- Ties in 𝒜^k are base ties (6.1(c)).
- (LF) holds on the full domain, or with N = U on M_U. ∎

No base meeting k-competitiveness is known. This is the open point of §0.

---

## 7. Status

| Item | Statement | Label |
|---|---|---|
| 1.1 | (FC) ⟺ "ρ⁻¹ accepted ⇒ ρ accepted" for chain composites; (TC) for 2-chains; transitivity installs ρ | PROVED |
| 1.2 | complete + (TC) ⇒ transitive; splices of complete bases gain nothing from (FC) | PROVED |
| 1.3 | (FC) ⟺ ordering extension (Suzumura); with (IB), accepted records lie in its context-uniform part Int(R) | PROVED (imports Suzumura) |
| 1.4 | no accepted chain composes to a strict improvement | PROVED |
| 1.5 | deleting strict comparisons preserves (FC)/(TC) | PROVED |
| 2.1 | **extension theorem without closure**: pointed defence cones, one-step monotone generators ⇒ full system with every axiom | PROVED |
| 2.1 remark | coordinate thresholds need a global tie-break constant on level lines (global FF1 5.1) | PROVED reduction; the global statement open |
| 2.2 | exchange survives (TC) without closure; EE1 Ex 4.3 is a strict 3-model cycle of bare generators | PROVED; CHECKED |
| 3.1 | vertex lemma for every selection (no (IB), no transitivity) | PROVED |
| 3.2 | VB's selection admits no relations at all with strict (G), competitiveness, two closed sections | PROVED; inputs CHECKED |
| 4.1 | arrow rule: (IB), strict (G), competitive, closed sections, (LF) for the plain posterior family | PROVED; CHECKED (68 250 tests) |
| 4.2 | arrow rule has strict 3-model cycles: fails (TC), (FC) | PROVED; CHECKED |
| 4.3 | arrow rule ties T1 with an incoherent model at every world: fails (C) | PROVED; CHECKED |
| 4.4 | (TC) arrow rules are endorsed by an integrable strictly guiding field; excluded for continuous selections through T1 | PROVED mod FF2 4.1 chain |
| 4.5 | (FC) statistics rules (pair-indexed weightings) are endorsed by a weakly guiding field | PROVED |
| 4.6 | … excluded when the endorser can be strictly guiding | PROVED mod FF2 chain |
| **5.1** | **local rejection by one field at every world ⇒ no continuous competitive selection through T1** | **PROVED mod FF2 4.1 Steps 2–6** |
| 5.2–5.3 | every (FC)+(IB) cover has a world with no arrow-linear local verdicts and no differentiable ordering extension anywhere | PROVED, same status |
| 6.1 | scale-dependent exchange rate on a lex base: (IB), strict (G), (FC), closed sections | PROVED |
| 6.2 | k-competitive lex base through T1 ⇒ full (FC) cover | PROVED (reduction) |
| — | existence of a k-competitive base | open (no CONJECTURE offered) |
| — | T1 cover | **not obtained** |

**Referee priorities.**
1. Thm 4.4 step 2: the 3-cycle construction under (TC). Check that the composite's arrows are a→c, b→a, c→b, and that
   the value ordering γ′ ≤ −γ follows from step 1.
2. Thm 5.1 step 2: that (Loc_i) is applied to restrictions that are proportional for all i ∈ J at once.
3. Thm 4.5 step 3: realisability of the chain from the partition (disjoint supports), and the use of the cone
   property.
4. Prop 3.2 step 3: that C_q ≠ B^j off A on a non-null set (P_k).
5. Prop 6.1(d): closedness at X = C_q, where K blows up.

## 8. Files (`hh2py/`)

- `arrow_rule.py` → `arrow_rule.out`: Prop 4.1(a),(b), the cycle sums (friction exactly on cycles through O at the
  positive worlds), Prop 4.2 (strict 3-model cycle, atomic surrogate), Prop 4.3 (three-world tie with T1). Four values
  of ε.
- `vb_vertex.py` → `vb_vertex.out`: Prop 3.2, the non-null sets A and P_k for all six (i,j,k), four ε, three s.
- `exchange_fc.py` → `exchange_fc.out`: Prop 2.2 on EE1 Example 4.3. The two caps and the reverse selected cap form a
  strict 3-model cycle at world 1, with no closure taken.
