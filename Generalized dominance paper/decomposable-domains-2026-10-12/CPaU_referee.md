# CPaU referee report: Remark rem:CPaU and the last sentence of Remark rem:EPchords

15 Oct 2026. I am an independent referee. I did not write the remark or any of its inputs.

**Read:**
- writeup §§2–3;
- §7: sec:cp (all), sec:M0, sec:M0-residual, sec:M0-closed (Lemmas quasilin and ball, Props crosspin, chainchords and carrying, Thm M0closed, Cor M0closed, Rem midarc);
- §8 (sec:two-questions, the "remaining target", the lexicographic and non-additive items);
- N22 (§§0–2), N24 (§§0–2, 6–7), N13 (Prop B, N11.3), N11 (§§1–3), P4 Part A (§§0–4), M0_referee (headline, §§5, 7), M0_second_referee (all);
- for the hypotheses of Thm 4.1, Prop 9.2 and the status table: N25 §§0, 4, 9 and 11.

**Verdict scale:** CORRECT / CORRECT WITH REPAIR / GAP / WRONG.

**Script:** `cpauref_py/glue_check.py` (output in `glue_check.out`; run with `python3 -I`). These are discrete sanity checks of the glue: 200 random trials, 0 failures. No verdict rests on them.

---

## 0. Verdict

**Remark rem:CPaU: CORRECT WITH REPAIR.** The parallel sentence at the end of rem:EPchords gets the same verdict.

- The mathematics is right. Under (H) and (CP-a) on M_U, the field built from ψ^P meets every hypothesis of Theorem thm:M0closed(a), with the right quantifiers. The proof of thm:M0closed(a) uses nothing about the original ranking. So no (CP-a) ranking covers T1 on M_U.
- The repairs:
  - name the field;
  - cite Theorem thm:fullsupport for the existence of P;
  - spell out how (α) and (γ) translate into the form thm:M0closed(a) needs;
  - list the axioms the excluded ranking satisfies;
  - correct the logic of "(U) holds vacuously";
  - fix one corrupted `\ref` in the status line of conj:U.
- I also give a second, shorter route: on M_U every (CP-a) world adds up, so Theorem thm:M0closed(b) applies directly.

---

## 1. What Theorem thm:M0closed(a) assumes, and whether ψ^P supplies it

**Hypotheses of thm:M0closed(a)**, from the statement, the "Standing data" paragraph, and the second referee's §2 and §6.4:

- **(M-dom)** ε ∈ (0,1), 0 < s < 1, K′ = u + s(T1 − u), U = D_{K′}.
- **(M-sign)** c : U → ℝ³ is measurable and *strictly signed*: c_i(g) has the strict sign of g_i for a.e. g ∈ U. This covers all of U, including the nonnegative gambles in U. Strict signs at every g are used in Lemma quasilin(b) (q·c(g) → c_l(g) ≠ 0 as q → e_l) and in Theorem Estructure (c(g) ∝ 𝟙 is impossible).
- **(M-γ)** B_q := {q·c > 0} equals some D_{K_q} a.e., for a.e. q ∈ Δ°. Nullity of E follows by Tonelli and is not an extra hypothesis.
- **(M-α)** There are p\* ∈ Δ° and a measurable S ⊆ Z_{p\*} with D_{T1} = B_{p\*} ∪ S mod null.

**What thm:M0closed(a) does *not* assume:**
- (β) (a coherent Bayes model at every weighting): coherence of B_q at every interior q is *derived* from (γ) (Thm Estructure(d), N25 Thm 3.3).
- (δ) (coherent vertex models): vertex behaviour comes from strict signs (Lemma quasilin(b)).
- Integrability: "not used" (second referee, §6.4).
- (E_ψ), selections, Prop F step 5.

**Field for (CP-a).** Fix P ∈ ∏_i 𝒫_i^+. On M_U each pair meeting U is indexed by its orientation g ∈ U. Write ḡ := sign(g₁)g for its representative in H and a_g for the advice "accept g". Put

  c^P_i(g) := ρ_{P_i}(ḡ)·(λ_i(ḡ,0) − λ_i(ḡ,a_g)),  g ∈ U.

This is exactly the vector used in the proof of Cor residual. The remark says "the field ψ^P … is strictly signed"; strictly, it is c^P that is strictly signed (repair R1).

| Hypothesis | Supplied? | Why |
|---|---|---|
| (M-dom) | yes | The U-domain of §2.4 uses this K′ (sec:aos). |
| (M-sign) | **yes** | See §2 below. |
| (M-γ) | **yes**, for every P ∈ ∏𝒫^+ | Thm integral(c): E(P) is null, and off E(P) the ψ^P-Bayes model is a.e. unique and coherent. Off E(P) the tie set is null, so B_q is a pointwise minimiser, hence a Bayes model (integrable envelope ‖λ_i‖_∞ρ_{P_i}; R1 Lemma 1.2). By uniqueness it *is* the coherent Bayes model, so B_q = D_{K_q}. Translation of E: pairs with neither orientation in U have advice range {0} and no ties. For g ∈ U, p·ψ^P(ḡ,·) has two minimisers on {a_g, 0} iff p·c^P(g) = 0. So Z_p(P) corresponds to Z_p(c^P) under the measure-preserving bijection g ↦ ḡ (μ is symmetric), and E(P) = E(c^P). |
| (M-α) | **yes**, at p\* = p_T ∈ Δ° | Thm integral(a). T1 is ψ^P-Bayes at an *interior* p_T. Interiority is pushed by the Lemma IC model, valid on M_U (N11 Cor 3.2(d), refereed in N13; N24 §2.1). Bayes models of an integral field with integrable envelope are exactly the pointwise minimisers. On g ∈ U the pointwise minimiser accepts where p·c^P > 0, rejects where p·c^P < 0, and is free on Z_p. So D_{T1} = B_{p_T} ∪ S with S ⊆ Z_{p_T} (`glue_check.py` (3)). D_{T1} ⊆ U because K′ ⊆ T1 ⊆ Δ°. |
| P exists | **yes** | ∏𝒫_i^+ ≠ ∅ by Thm fullsupport, under (CP-a) and strict (G), both part of (H). The remark does not cite this (repair R2). One P suffices. |

**Quantifiers.**
- thm:M0closed(a) needs (M-γ) at a.e. q and (M-α) at *one* interior weighting.
- Thm integral gives (c) for every P and (a) at some p_T for every P.
- These match. (BU) at *every* q, which Cor residual needs, is not needed here; this is the whole point.

**Representative and orientation conventions.** These are consistent:
- (CP-a)(i) is stated on H with advice in {+,0,−,×};
- c^P is a function on U, carried by the bijection used in sec:CPa-def for the canonical encoding;
- N_i on M_U consists of *all* pairs meeting U, as sec:cp states explicitly.

---

## 2. Is c^P strictly signed?

**Yes, a.e. on U.**

- *Penalties.* (CP-a)(i) gives λ_i(ḡ,a) < λ_i(ḡ,b) whenever a ranks strictly better than b at world i, for a.e. ḡ. The background order is good ≺ none ≺ bad. Accepting g is good at i iff g_i > 0, and coordinate planes are null. So λ_i(ḡ,0) − λ_i(ḡ,a_g) is > 0 if g_i > 0 and < 0 if g_i < 0, for a.e. g.
- *Densities.* P_i ∈ 𝒫_i^+ means ρ_{P_i} > 0 a.e. on N_i. This is the *definition* of 𝒫_i^+ in Thm fullsupport, not a separate fact.
  - On M_U, N_i is every pair {f,−f} with f ∈ U or −f ∈ U, so ρ_{P_i}(ḡ) > 0 for a.e. g ∈ U.
  - This includes the nonnegative gambles of U, not only the mixed ones. Strict signs are needed there too, by (M-sign).
- *Hypotheses of Thm integral.* It is stated for every P ∈ ∏𝒫_i^+, so "ρ_{P_i} > 0 a.e." is exactly what membership supplies.
- *Check.* `glue_check.py` (1): random bounded rank-increasing λ and positive ρ, 1800 sign checks, 0 failures.

---

## 3. Does the proof of thm:M0closed(a) use anything about the original ranking?

**No.** I traced every input.

- **Prop chainchords** (P4 Thm 3.1/A1). P4 says it "uses only (α) and (γ): no (E_ψ), no ranking structure beyond Prop M0". "Beyond Prop M0" refers only to where (α) and (γ) come from.
  - The second referee's step table (§4.1) uses field-level facts throughout.
  - The one place that looks ranking-level is the normalisation p\* = u. P4 cites Prop generic(b) (κ⊙ψ ∈ 𝒩) for it. The writeup and the second referee instead use the field-level fact that p\*⊙c and c^σ(g) := σc(σg) preserve strict signs and (γ), move E together with p\*, and fix U and D_{T1}. That holds for any field, so c^P is covered.
- **Prop carrying, Prop crosspin, Lemmas ball and quasilin.** These are field-level. Their inputs are:
  - N25 Thm 4.1(a), (b), (d), (e), (f) and Lemma 3.1 (status "(γ)" in N25 §11);
  - Prop F steps 1–4 (status "(γ) only");
  - Lemma caps(a), Lemma UVN through Lemma quasilin(b), and Lemma signs.
- **Lemma edgebox and Prop T1.** These are N25 Prop 9.2 (status "(γ)") and the algebra of §4.
- **Thm Estructure.** Its statement asks for an *integrable* field. c^P is integrable (|c^P_i| ≤ 2‖λ_i‖_∞ρ_{P_i} ∈ L¹), so this holds whether or not integrability is really needed.
- **Not used:**
  - every (E_ψ)-dependent item: N25 Lemma 1.2, §§7–8, Prop Epsi, P4 §4.4 / Thm A3;
  - (S), (C), competitiveness and selections;
  - Prop M0 and N19 Prop R3(a).

  The ranking enters only through Thm integral(a) and (c). Inside those, (S), (C), Lemma IC and Fact 0 are used, and they are hypotheses of (H).

---

## 4. "(U) holds vacuously there"

**The logic is right; the wording is not.** Repair R5.

- (U) is a property of a *system*: some P ∈ ∏𝒫^+ has E(P) = ∅.
- What is vacuous on M_U is the *universally quantified conditional* "every (CP-a) system satisfying (H) has (U)", that is, Conj U restricted to M_U.
  - Its antecedent, (H) + (CP-a) on M_U, is unsatisfiable by the remark, because (H) includes "covers T1".
  - Likewise Cor residual is vacuous on M_U, since its hypotheses cannot be met.
- The remark bypasses (U) and Cor residual altogether. It never asks whether E(P) is empty. Thm M0closed(a) tolerates a non-empty E(P).
- The second sentence of Conj U ("on non-adjacent domains equivalent to: no (CP-a) ranking covers T1") now has both sides true on M_U. The right-hand side is the substantive theorem.
- The remark says nothing about (U) for (CP-a) systems that satisfy the axioms but do not cover T1. N24 §2.1 notes that Thm integral(b)–(d) and E(P) make sense for them.
- A side effect worth repairing (R9): several §7 statements on M_U are made under (H). These are the last sentence but one of rem:EPchords ("(U) fails exactly when every member choice P has such a chord") and Prop Ucont. They are now vacuous on M_U. To keep content, they should be stated under (H⁻) := (H) without the coverage clause. Per N24, only (α) uses coverage.

---

## 5. Scope

- **"Complete or not":** correct.
  - The M_i are arbitrary weak-* closed convex sets of null-invariant states.
  - Purely finitely additive and atomic parts are allowed.
  - No detection, separability, attainment, (UN) or (D^CA) is needed.
  - On M_U this subsumes Cor complete and Cor DCA.
- **Charges vs integrals:** correct. The charges enter only through Thm integral, which handles them by finitely many small carriers (N22 §2, N24 §2.1). The field fed to thm:M0closed(a) is integral.
- **Encodings:** any bounded measurable λ_i, strictly increasing in world-i rank a.e., not only the canonical error indicator.
- **Axioms of the excluded ranking:** strict (G), (LA), (S), (C) and T1 ∈ C_L.
  - (IB) and weak (G) are automatic under (CP-a) (Prop normalform).
  - The remark should say this (repair R4); "no ranking whose worlds are …" alone omits the axioms.
- **All three worlds (CP-a).** Mixed systems are covered by Route B below: a (CP-a) world adds up on M_U.
- **Domain:**
  - proved on the U-domain with K′ = u + s(T1 − u);
  - CHECKED for every K′ ⊆ relint T1 and every all-facing triangle in general position (inherited from thm:M0closed's scope);
  - **not established** on other non-adjacent domains (for example under (UN)), on general decomposable domains, for (CP-s), for (CP-b) with invisible desirability, or for n ≥ 4.

  On those, Conj U and Cor residual remain the live statements.

---

## 6. A second route (Route B), and the comparison

**Lemma (CP-a ⇒ adds up on M_U; PROVED here).** Let world i satisfy (CP-a) and strict (G) on M_U, and let P_i ∈ 𝒫_i^+.

Put w_i(g) := |λ_i(ḡ,a_g) − λ_i(ḡ,0)| for g ∈ U, which is > 0 a.e. Then, with W_i := U ∩ {g_i > 0} and E_i(X) the error set,

  Λ_iX = Λ_iW_i + w_i·1_{E_i(X)}  on the pairs meeting U,

and Λ_iX = Λ_iW_i on the other pairs.

*Proof.* If g_i > 0, then λ(a_g) < λ(0), and the value is λ(a_g) + w·1[g ∉ X]. If g_i < 0, the value is λ(0) + w·1[g ∈ X]. Checked in `glue_check.py` (2).

Define ν_i(A) := P_i(w_i 1_A) for A ⊆ U. Then:
- ν_i is finitely additive and vanishes on null sets;
- ν_i(A) ≥ ∫_A w_iρ_{P_i} dμ > 0 on non-null A;
- by (W), B ⪯_i X ⇒ ν_i(E_i B) ≤ ν_i(E_i X) for *all* comparisons, not only the relevant ones.

So every (CP-a) world adds up.
- The countably additive part of ν_i has density w_iρ_{P_i}: multiplying a purely finitely additive charge by a bounded function keeps it purely finitely additive.
- So the supporting field ρ^ν_i·sign(g_i) is exactly c^P.

**Consequence.** (CP-a) on M_U ⇒ (M0). Thm M0closed(b) then excludes every such ranking, and also every *mixed* system in which each world is (CP-a) or adds up.

The writeup already records the ingredient: in "The remaining target", the first bullet says a world that does not add up "is not a coherent almost-preference (Theorem fullsupport …)".

**Comparison of the routes.**
- *Route A* (the remark): Thm fullsupport + Thm integral(a), (c) + glue + thm:M0closed(a).
- *Route B*: Thm fullsupport + the Lemma above + thm:M0closed(b). It sits at the status of Prop M0: N13 Prop B, plus N19 Prop R3(a), which Route B in fact does not need, since every comparison is endorsed.
- Both rest on the same core (N13 Prop B = N22 Thm 2.1 without full support), so they are not independent.
- Route A has the better-documented status (N22 Thm 2.1 refereed in N24) and should stay primary. Route B is worth one sentence, because it places (CP-a) inside (M0) and covers mixed systems.

---

## 7. Repairs

- **R1 (precision).** Replace "the field ψ^P … is strictly signed" with: "the vector field c^P_i(g) := ρ_{P_i}(ḡ)(λ_i(ḡ,0) − λ_i(ḡ,a_g)) on U (as in the proof of Corollary residual) is strictly signed, because P_i ∈ 𝒫_i^+ gives ρ_{P_i} > 0 a.e. on N_i ⊇ {pairs meeting U} and (CP-a)(i) gives strict rank-monotonicity".
- **R2 (existence).** Add "fix P ∈ ∏𝒫_i^+, which is non-empty by Theorem fullsupport".
- **R3 (translation).** Add one sentence:
  - Bayes models of the integral field ψ^P are its pointwise minimisers, so (a) gives D_{T1} = B_{p_T} ∪ S with S ⊆ Z_{p_T}, and (c) gives B_q = D_{K_q} off the null set E(P) = E(c^P).
  - Neither (β) nor (δ) is needed.
- **R4 (axioms).** Replace "no ranking whose worlds are coherent almost-preferences over losses covers T1" with "no ranking on M_U with strict (G), (LA), (S), (C) whose worlds are all coherent almost-preferences over losses ((IB) is then automatic) has T1 ∈ C_L".
- **R5 (logic).** Replace "and (U) holds vacuously there (Conjecture U)" with: "Hence on M_U the hypotheses of Corollary residual and of Conjecture U are never met, so the conjecture holds there vacuously; its equivalent form 'no (CP-a) ranking covers T1' is what has been proved. The argument does not pass through (U): it tolerates E(P) ≠ ∅."
- **R6 (LaTeX bug).** In the status line of conj:U (lines 1209–1210), `\r` of `\ref` was turned into a line break. The source reads `Remark~` followed by a newline and `ef{rem:CPaU}`, so the PDF prints "ef{rem:CPaU}". Restore `Remark~\ref{rem:CPaU}`. No other control characters or mangled escapes were found in the file.
- **R7 (status line of rem:CPaU and table rows 107, 120).** Replace "CHECKED … not refereed" with the status in §8.
- **R8 (optional).** Add Route B (§6) as one sentence. Consider promoting the remark to a Corollary (`cor:CPaU`): it is a headline result and subsumes Cors complete and DCA on M_U.
- **R9 (optional).** Restate the coverage-free parts of §7.1–7.2 under (H⁻) (§4 above). Otherwise rem:EPchords' "(U) fails exactly when …" and Prop Ucont become vacuous on M_U.

---

## 8. The statement established, with dependencies and statuses

**Corollary (no (CP-a) cover on the U-domain).**
- *Setting.* Let ε ∈ (0,1), 0 < s < 1, K′ = u + s(T1 − u), U = D_{K′}.
- *Statement.* On M_U there is no ranking with strict (G), (LA), (S), (C) and T1 ∈ C_L in which every world is a coherent almost-preference over losses (CP-a).
- *Generality.* Here λ_i is bounded measurable and strictly rank-increasing a.e., and M_i is any weak-* closed convex set of null-invariant finitely additive states: complete or not, with purely finitely additive and atomic parts allowed. No detection, separability or attainment is assumed.
- *Mixed systems* (each world (CP-a) or adding up): excluded at the status of Thm M0closed(b), by Route B.

**Status: PROVED.**
- Every input has been refereed at least once.
- The glue (§§1–2) has had one reading (this report).
- The weakest links are Thm integral (a), (c), refereed once as assembled.

| # | Input | Status |
|---|---|---|
| D1 | Thm fullsupport (N22 Thm 1.2): ∏𝒫^+ ≠ ∅ | proved; refereed once (N24 §1, CORRECT WITH REPAIR, cosmetic) |
| D2 | Thm integral(a) (N22 Thm 2.1(α) = N11 Cor 3.2(d) + R11 Lemma IC) | proved; refereed in N13 (N11.3) and N24 §2.1 |
| D3 | Thm integral(c), with (β) behind it (N22 Thm 2.1(γ); N13 Prop B) | proved; refereed once (N24 §2.1, which re-derived N13 Prop B(β)) |
| D4 | Glue: c^P strictly signed; (M-α), (M-γ) in the form thm:M0closed(a) needs; E(P) = E(c^P) | proved here; one reader; NUMERICS sanity in `cpauref_py` |
| D5 | Thm M0closed(a) | proved; new parts read independently twice (M0_referee, M0_second_referee) |

**Not used:**
- (U), Cor residual, Thm complete, (UN), Prop Ucont;
- Thm integral(b) and (d) as hypotheses (they enter only inside the proof of (c));
- (E_ψ), Prop M0, N19 Prop R3(a), Thm ccibu, Prop F step 5;
- non-adjacency beyond M_U.

**Scope:**
- every K′ ⊆ relint T1 and every all-facing triangle in general position: CHECKED (inherited);
- other non-adjacent domains, general decomposable domains, (CP-s), (CP-b) with invisible desirability, n ≥ 4: **not established**.

---

## 9. Consequences for the write-up

**Introduction, item 3.** Reorder it to:
> On the U-domain no (CP-a) ranking covers T1, complete or not, and with arbitrary finitely additive members: the integral field of Theorem integral falls under Theorem M0closed(a) (Remark/Corollary CPaU). Equivalently, on M_U every (CP-a) world adds up. On other non-adjacent domains coverage is impossible when every world is complete (under (UN)) or strict comparisons are detected by countably additive previsions, and in general it reduces to the single property (U).

- Drop "observation of this revision, CHECKED, not refereed", and give the §8 status.
- Item 4 could add "this includes every (CP-a) ranking".

**Status table:**
- Row 120 becomes "proved; glue refereed once (CPaU_referee); inputs Thm integral (N24) and Thm M0closed(a) (two referees)".
- Row 107 becomes "open on non-adjacent domains other than M_U; on M_U its hypothesis is never met (Cor CPaU)".
- Row 106: add "on M_U superseded by Cor CPaU".

**§7.** Apply R1–R6. Under R9, rem:EPchords' structural statement should be about (H⁻) systems.

**Open-questions section (§8):**
- *Q1 answer:* change "(Remark CPaU, CHECKED)" to "(Corollary CPaU, proved; refereed once)".
- *Item on rankings that do not add up:* the sentence "for coherent almost-preferences it is (U) … on M_U both are now closed" stands, with the status updated.
- *"The remaining target":* consistent as written. Its first bullet is Route B, so the two can cross-reference.
- *Open items:* the list of what remains open for (CP-a) should read:
  - (U) / Conj U on non-adjacent domains other than M_U (including (UN) domains);
  - (CP-a) on general decomposable domains (where neither Cor residual's non-adjacency nor thm:M0closed applies);
  - the Walley-2000 variant with invisible desirability (still open; it is not (CP-a), and Route B does not reach it).
- For the coverage question on M_U, the only remaining route is unchanged: a world that is not (CP-a) and does not add up (M1/M2).
