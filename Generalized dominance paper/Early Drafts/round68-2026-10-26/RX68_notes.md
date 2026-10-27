# RX68: cross-paper consistency check of the two definitive manuscripts

26 October 2026. Role: RX68 (BRIEF68, verification phase, cross-paper check).

## Papers checked
- **LDG.** `Loss dominance generalized (definitive).tex` and its PDF.
  - Title in the paper: *Coherence, Dominance, and Generalized Loss*.
  - 22 pp.
  - Changes file: `WL68_changes.md`.
- **APP.** `Coherence and accuracy for sets of desirable gambles.tex` and its PDF.
  - 24 pp.
  - Changes file: `WA68_changes.md`.

## Method
- I read both `.tex` files in full.
- I grepped the PDF texts for jargon and labels.
- I checked both compile logs: no warnings, undefined references or overfull boxes.
- I compared the papers against `BRIEF68.md`, `AUDIT_r68_message.md`, both changes files, the outlines' status appendices, and the sources where needed:
  - LDG v3.3: its lemma on Zorn's lemma, and its admissibility method;
  - the covering draft;
  - the universal-coverage draft.
- I re-derived the cross-paper mathematics myself:
  - LDG Prop 7.1;
  - APP Prop 6.3;
  - the correspondence between the two rules;
  - APP Example 6.4, since LDG cites it;
  - APP Remark 4.4;
  - APP App. D Step 4, since LDG §9 cites it.

Line numbers below refer to the `.tex` files.

## Verdict in one paragraph
- **Dependence.** There is no circular dependence, and neither paper relies on deleted material.
  - LDG cites APP only for an illustration, for one existence instance, and for an attribution. No LDG proof uses APP.
  - APP does not cite LDG at all.
- **Zorn's lemma.** The Zorn-lemma argument that LDG §9 attributes to APP is present in APP App. D, with the content LDG describes.
- **The construction.** LDG Prop 7.1 and APP's ranking agree exactly. APP's rule is an instance of LDG's construction, and every LDG hypothesis is discharged by an APP result.
- **Required changes.** Several wording mismatches need fixing. The required ones are:
  1. APP calls its ranking "incomplete and intransitive" without qualification, but this is false for some admissible μ. LDG correctly says "in general".
  2. LDG describes APP's result without APP's standing qualifications.
  3. The word "cover/coverage" means two unrelated things in the two papers.
  4. APP uses "available" without defining it, and once as "available from".
  5. LDG omits the stronger-third-condition caveat that APP records as open.
  6. APP has no reciprocal pointer to LDG.
  7. One sentence each in LDG §7 and §9 could be read as routing APP through LDG's sufficient conditions.

---

## 1. Cross-references and circularity

### 1.1 LDG → APP (cited as \cite{KCM}; bibliography: "J. Konek and C. Campbell-Moore. Coherence and accuracy for sets of desirable gambles. Manuscript, 2026.")

| # | LDG location | What LDG says | What APP actually contains | Used in a proof? | Accurate? |
|---|---|---|---|---|---|
| 1 | §1, l. 52 | APP proves the improvements of Prop 7.1(c)(ii) exist for coherent sets of desirable gambles on an arbitrary set of worlds, and obtains its ranking directly, not through the conditions of §§4–5 | Thm 5.1 (repair) and Thm 6.8 | No | **Incomplete.** APP's standing qualifications are missing (see R-L2). |
| 2 | §7, l. 490 | "The ranking is acyclic, but in general it is not transitive; the companion paper gives an example on the full space of gambles in two dimensions" | Ex 6.4, with E = ℝ² and two worlds. I re-derived it: increment > 1.075δ; transitivity and completeness both fail at world 1. | Only the existence claim "in general not transitive" rests on it | Yes |
| 3 | §7, l. 490 | APP proves that every incoherent model has a coherent improvement that raises the score by a uniform margin and is available to no coherent model, and obtains its ranking as a consequence | Thm 5.1(1),(4); Thm 6.8(b) | No | Yes in substance. The qualifications are missing, and the wording is slightly off: it is the *change*, not the improvement, that is "available" (R-L2). |
| 4 | §9, l. 626 | "They do not construct a family satisfying coherent admissibility; Section 7 and the companion paper address that." | Prop 6.6 and Thm 6.8 give a single ranking under which every coherent model is undominated | No | Yes |
| 5 | §9, l. 632 | "A different method first shows, by Zorn's lemma, that every model has an undominated weak dominator, and then shows that undominated models are coherent. The companion paper uses it for one structured construction." | App. D Step 4 is Zorn's lemma on the Lyapunov-compact score range: every model on U has an undominated weak dominator. Steps 5–7 are separation, uniqueness and coherence: undominated ⇒ coherent. §8 l. 1075–1080 summarises the same two steps. | No | **Yes, same content.** See 1.3. |

### 1.2 APP → LDG
**None.** WA68 flag 5 confirms this, and grep finds no `\cite` of LDG and no mention of a companion paper.

APP is self-contained. In particular:
- APP proves its own versions of LDG Prop 7.1(a)–(c): Props 6.2, 6.6 and 6.7, and Thm 6.8.
- APP defines closure under ties itself (§6.3, requirement 3).
- APP uses "coherent admissibility" informally (§9.2) without citing LDG.

### 1.3 The Zorn-lemma argument: confirmed
The lead asked whether APP carries the Zorn-lemma admissibility argument with the content LDG attributes to it. It does.

- **Where.** APP App. D (`app:vb`, l. 1387–1505), Step 4 (l. 1420–1435).
  - Fix X₀ and let D = {y ∈ Z : y ⊴ z(X₀)}, where Z is the range of the score vector.
  - Z is compact and convex by Lyapunov's theorem (Step 3).
  - Every chain has a lower bound. The proof uses the finite intersection property of the sets cl T_γ, then argues level by level in the lexicographic order.
  - Zorn's lemma then gives a minimal element, and any model realising it is an undominated weak dominator of X₀.
- **I re-checked Step 4.**
  - The least element of finitely many chain members lies in every T_γ.
  - y^∞ ⪯ γ at level a_i, using closure.
  - If equality holds at level a_i, then a_i is constant on T_γ, so the b_i are ordered. This is correct.
- **The rest of the argument.**
  - Steps 5–7 (separation, uniqueness, coherence) supply "undominated ⇒ coherent".
  - Step 8 supplies closure under ties, dominance of incoherent models, and the undominatedness of D_K.
- **Relation to v3.3.**
  - v3.3's general Lemma `zorn` (k lexicographic levels, any compact Z) and its Prop `lexbayes` now appear in neither paper.
  - LDG §9 claims only that the *method* exists and that APP uses it for *one* structured construction. That is accurate.
  - APP App. D is a self-contained two-level specialisation.
  - No result depends on the deleted general lemma.
- **LDGO67's cross-paper requirement is met.** It said: "if the application paper keeps its veto–Brier example, it must carry the Zorn lemma and the separation step itself".

### 1.4 Circularity: none
No proof in either paper invokes a result of the other. The only LDG claim whose sole support lies in APP is the existence claim "in general not transitive". It is backed by APP Ex 6.4, which is proved in APP without LDG. So the dependency graph is acyclic.

---

## 2. Reliance on deleted material (LDG v3.3, covering draft, universal-coverage draft)

**LDG.** Clean.
- It cites no draft.
- All `\ref`s resolve, and the bibliography no longer contains CPMNote.
- The results omitted from v3.3 are not referenced anywhere:
  - Prop 4.8 (B.5–B.6);
  - the metrizable variant;
  - the relational variant of Ex 5.6;
  - the admissibility method of v3.3's "Route B", including Lemma `zorn` and Prop `lexbayes`.
- One residual external claim is unverified. §3.2 (l. 132) says that in Example 1 of SSK09 "an incoherent forecast has the same total scores at every world as a coherent one".
  - This is a cited fact, not deleted material.
  - WL68 explicitly dropped the further claim about rescaling by e^t.
  - The cited fact itself was not re-verified this round (unrefereed list, U-L10).

**APP.** Clean.
- It cites no draft.
- Every argument it needs from the covering and universal-coverage drafts is reproduced in full:
  - Lyapunov, Zorn, separation, uniqueness and coherence (App. D);
  - local freedom (App. C);
  - the measure construction (Lemma 2.2, proved in App. A and reused in §9.3).
- The two results whose full forms were dropped are not referenced:
  - the "visibility class" and Thm `cover`;
  - the nonseparable sketch, which appears only as an open question.
- One wording residue: "the classical **route** from admissibility to coherence" (l. 1075) uses a banned word (see §4).

---

## 3. Consistency of statements

### 3.1 LDG Prop 7.1 against APP's ranking (Def 6.1; Props 6.2, 6.3, 6.6, 6.7; Thm 5.1; Thm 6.8)

APP's rule is exactly LDG's construction under the following dictionary. I checked each line.

| LDG §7 | APP | Check |
|---|---|---|
| Models M_L; coherent models C ∩ M_L | Models (completion-measurable sets mod μ); coherent = a.e. equal to some D_Q. On a domain U: models on U, and coherent models on U. | ✓ |
| "the change from m′ to m"; null only if m = m′ | The change from Y to X is the pair (A, B) = (X∖Y, Y∖X), up to null sets. It is null iff X = Y a.e. | ✓ |
| "available to z": it is the change from z to some model | "Z could make it": B ⊆ Z a.e. and A ∩ Z null. Def 2.5 itself notes that the change from Z to (Z∖B) ∪ A is the change (A, B). So the two notions coincide. | ✓ The terms differ (see §4). |
| "guided by the truth at ω"; contains the null change | "guided by ω": A ⊆ {h(ω) > 0} and B ⊆ {h(ω) < 0} a.e. The null change is guided (Prop 6.2(a)). | ✓ The terms differ (see §4). |
| Real score φ_ω, larger is better | m_ω(X) = ∫_X h(ω) dμ, finite by (M1), higher is better | ✓ |
| Rule: guided, **or** available to no coherent model and φ_ω(m) > φ_ω(m′) | Def 6.1: clause (i) guided by ω, **or** clause (ii) no coherent model could make it and m_ω(X) > m_ω(Y) | ✓ identical |
| Hyp. (a), "guided changes improve the score" | Prop 6.2(b): ∫_A\|h(ω)\| + ∫_B\|h(ω)\| > 0. No (M2) is needed. | ✓ |
| Concl. (a): reflexive; acyclic; distinct models never tied at ω | Prop 6.2(a),(b) | ✓ |
| Hyp. (b), "guidance protects coherent models" | Lemma 6.5. **This needs (M2)**, specifically μ{P_S = 0} = 0; Ex B.2 shows that the condition is essential. | ✓ But APP's intro misdescribes it (see R-A6). |
| Concl. (b): no model other than c weakly dominates a coherent c | Prop 6.6, almost word for word | ✓ |
| (c)(ii): a coherent c reached by a change that is unavailable to coherent models and raises the score at every world | Thm 5.1(1) and (4), with a uniform margin | ✓ |
| (c): closure under ties; strict dominance | Thm 6.8(b),(c): uniform dominance, and the strong form of closure under ties | ✓ APP is stronger. |
| (no maximality statement) | Prop 6.3: the ranking is the largest relation with properties (1)–(3) | No conflict. LDG is silent on it (R-L4). |

**Prop 7.1 re-derived (U-L1).**
- (a) is correct. The null change is guided, so each relation is reflexive. On both branches, an accepted change between distinct models raises φ_ω. Around a cycle the scores are therefore equal, so every step is between equal models.
- (b) is correct. The change from c to a weak dominator is available to c, so it is accepted at each world only on the guided branch, and protection then gives equality.
- (c) is correct.
  - (i)⇒(ii): availability does not depend on the world. If the change is available to some coherent model, it is accepted at every world only as guidance.
  - (ii)⇒(i): (a) gives strictness, and (b) shows that coherent models are undominated, so they weakly dominate themselves.
  - Closure under ties follows from (b).
- The hypotheses are minimal for each part, as REF67_ldgo §10 required.

**APP Prop 6.3 re-derived (U-A1).**
- The ranking has property (1) by clause (i).
- It has property (2) by Prop 6.2(b).
- It has property (3) because clause (ii) excludes changes that some coherent model could make.
- Now let R have properties (1)–(3), and suppose X R Y.
  - If X = Y a.e., the change is null, hence guided.
  - Otherwise (2) gives a strict score gain.
  - If some coherent model could make the change, (3) forces it to be guided.
  - If not, clause (ii) applies.
- So R ⊆ ⪯_ω. The lead's check in BRIEF68 is correct, and the proposition is correct as stated.

### 3.2 Definitions

| Notion | LDG | APP | Consistent? |
|---|---|---|---|
| Weak dominance | c ⪯_ω m at every world (l. 62) | Same (l. 815) | ✓ |
| Dominance | Weakly dominates and not tied at every world; equivalently, ≺ at some world | Weakly dominates and ≺ at some world | ✓ (equivalent) |
| Strict dominance | ≺ at every world | Same | ✓ |
| Uniform dominance | Loss rankings only: finite losses, and a margin ε in the loss | Strict dominance **and** inf_ω(m_ω(Y) − m_ω(X)) > 0, a margin measured in the *score* rather than in the ranking | ✓ in spirit. APP should say that the margin is in the score (R-A9). |
| Undominated | No model dominates it | Same | ✓ |
| Tied | Defined only as "tied at every world" (l. 63). **"Tied at ω" is used in Prop 7.1(a) (l. 472) but never defined.** | Defined at ω (l. 691) | Minor LDG gap (R-L7) |
| Models | Abstract set; no structure | Measurable sets mod μ. LDG Remark 3.7's equivalence ∼ becomes equality, because APP builds the quotient into "model". | ✓ |
| Coherence | A class C fixed in advance | a.e. equal to D_Q; this includes Walley-coherent sets and sets coherent in the weak sense (Lemma 2.3(b)) | ✓ (instance) |
| Guidance | An abstract set of changes, "guided by the truth at ω" / "guided at ω" | "Guided by ω" (Def 2.5) | Same notion, different wording (§4) |
| Independence | Not used | Comparison depends only on the change (Prop 6.2(a); requirement (1)) | No conflict. LDG's general rule need not satisfy it, since φ_ω(m) − φ_ω(m′) need not depend only on the change. LDG makes no claim either way. |
| Finite-chain consistency | "Acyclic" (l. 472, 490): every cycle consists of equal models | "Acyclicity": no chain A₀ ⪯ … ⪯ A_k has A_k ≺ A₀, and every cycle consists of a.e.-equal models | ✓ Both use REF67_out K3's name "acyclicity" in place of the brief's "finite-chain consistency". APP's form is slightly stronger, but both forms follow from a strict score gain. |
| Disjoint additivity | Not used | Prop 6.2(c) | No conflict |
| **(C)**: closure under ties | "A model tied at every world with an undominated coherent model of L is itself an undominated coherent model of L" (l. 109) | Requirement (3), word for word in substance (l. 893). Thm 6.8(c) gives the strong form ("tied at any one world ⇒ equal"), which matches LDG Prop 7.1(a). | ✓ |
| **(W)**: the dominance conclusion | Named; central (l. 110) | **Not stated for the universal ranking.** It follows from Prop 6.6 and Thm 6.8(b), but neither the "covers" list nor Thm 6.8 states it. VB Thm 8.1(b) does state it (first sentence). | Gap (R-A5) |
| Coherent admissibility | Family-level: every coherent model is an undominated coherent model of some ranking (l. 108) | §9.2: "that coherent models remain undominated" (single ranking) | ✓ for a one-member family. APP could say so explicitly (R-A9). |
| "Covers" / "coverage" | **"Coverage"** is hypothesis (ii) of Thms 5.1 and 5.6: every prior lies in a guarantee set at a world it charges. | **"Covers K"**: the six requirements of §6.3 for a target credal set | **Collision** (R-L3 / R-A3) |
| "Domain" | "Evaluation domain" M_L (l. 58); "arbitrary domains" = algebras of events (§8.2) | A Borel set U of gambles (§6.3) | Different senses. Tolerable, but note for readers of both (optional). |
| "Score" | §7: φ_ω, **larger is better**. But Ex 5.4 (l. 349): "scores (t, 1−t) … lower being better". | Higher is better throughout | LDG is inconsistent internally, and against APP (R-L6) |

### 3.3 What the construction achieves and what it leaves open

| Point | LDG | APP | Consistent? |
|---|---|---|---|
| Representation, not independent justification | §7 l. 490: "it shows that the ranking requirements are compatible with coherence and can single it out exactly; it does not, by itself, derive coherence from independently justified comparisons of performance" | §1 l. 147–158: "compatible with coherence and can represent it exactly … does not, by itself, derive coherence from accuracy comparisons that are justified independently of coherence"; §9.1 l. 1119–1122: "can single it out" | ✓ In substance. Two issues: "represent" and "single out" alternate (minor), and **LDG's "the ranking requirements" has no referent in LDG**, since LDG never lists them (R-L5). |
| The substance lies in the existence of improvements | §7: "Its substantive mathematics is the existence of the improvements in (c)(ii)" | §1, §9.1: the repair theorem is the substantive achievement, and maximality does not replace it | ✓ |
| **The stronger third condition** | **Absent.** LDG never says that its rule's "available to a coherent model ⇒ accepted only as guidance" is a per-world, per-comparison restriction stronger than coherent admissibility, nor that its independent justification is open. | §9.2 (l. 1124–1135) and the open questions (l. 1175–1179) | **Inconsistent by omission** (R-L4) |
| What protects coherent models | Prop 7.1(b) makes protection a **separate hypothesis** on guidance | §1 l. 150–151: "Coherent models are protected **by the rule itself**". In fact protection also needs Lemma 6.5, hence (M2) with μ{P_S = 0} = 0, and Ex B.2 shows the rule alone fails without it. §9.1 l. 1115 ("Properties (1)–(3) … protect coherent models") also omits (M2). | **Inconsistent.** APP overstates (R-A6). |
| Description of APP's scope in LDG | "for coherent sets of desirable gambles on an arbitrary set of worlds" (l. 52, 490) | The gambles form a separable space with an order unit; (M1) and (M2); models mod null sets. The audit requires these in statements and introductions. | LDG omits them (R-L2) |
| Transitivity | "in general it is not transitive" (l. 490) | "The ranking is incomplete and intransitive" with no qualifier: abstract l. 58, §1 l. 123 and l. 160–161, §8 l. 1005, l. 1086–1087 | **APP is wrong as stated** (R-A1) |

**Why APP's unqualified "intransitive" is false.** APP's own measure from §2.3 is a counterexample.
- **Setup.** Take μ = δ_𝟙 + δ_{−𝟙} on E = ℝⁿ. It satisfies (M1) and (M2).
- **Models.** These are the four subsets of {𝟙, −𝟙}, and {𝟙} is the only coherent one.
- **Which changes are accepted.**
  - Every change that is not guided is either available to {𝟙}, or has zero score change. The latter applies to adding or removing both points.
  - So the ranking accepts exactly the guided changes: X∖Y ⊆ {𝟙} and Y∖X ⊆ {−𝟙}.
  - This relation is transitive.
- **Completeness.** It is still incomplete: ∅ and {𝟙, −𝟙} are incomparable. With μ = 0 the ranking is even complete.
- **Diagnosis.** Ex 6.4 shows failure for Lebesgue-equivalent μ on ℝ², not for all admissible μ.
- **What the brief asks for.** BRIEF68 asks for "generally incomplete and not transitive", and LDG has it right.

---

## 4. Terminology

| Thing | LDG term | APP term | Recommendation |
|---|---|---|---|
| A change some coherent model could carry out | "available to z" (defined, l. 464); glossed "no coherent model could make it" (l. 467) | "could make" (defined, Def 2.5). Also "available to a coherent model" in Prop 6.3(3), l. 758 and l. 1108, and "available and unavailable to" in l. 154, **all undefined in APP**. Also "available **from** a coherent model" in l. 88. | APP: add one clause to Def 2.5 ("we then also say that the change is *available to* Z"), and change l. 88 to "no coherent model could make it" (R-A2). |
| Guidance | "guided by the truth at ω" (l. 465); "guided at ω" / "guided at every world" (Prop 7.1) | "guided by ω" / "guided by every world"; "strict guidance by the truth" (l. 118) | Pick one form for both papers; "guided by the truth at ω" is clearest. Low priority. |
| KKM hypothesis vs target success | "coverage" (Thms 5.1(ii), 5.6 2(b), Cor 5.2 proof, Rem 5.8) | "covers K", "coverage of every coherent target" (§§6–9, App. C) | Rename one. Cheapest: LDG renames hypothesis (ii) to **"matching at a charged world"** (8 occurrences). APP keeps "covers", which is its headline notion. (R-L3) |
| The APP ranking | — | "the universal ranking" (l. 160, 1086, 1092, 1095), **never defined** | APP: define once ("the ranking of Definition 6.1, which we call *universal* because one ranking covers every credal set"), or replace with "the ranking of Definition 6.1" (R-A4). |
| Undominatedness | "undominated"; "coherent admissibility" (a family condition) | "admissibility" in "the classical route from admissibility to coherence" (l. 1075) means undominatedness, which is not the same as coherent admissibility | APP l. 1075: "the classical argument from undominatedness to coherence" (R-A4). This also removes the banned word "route". |
| Score | Mixed: Ex 5.4 "scores … lower being better"; §7 score, larger is better | Higher is better | LDG Ex 5.4: "losses (t, 1−t) … and (2, 2)" (R-L6) |
| Dominance conclusion (W) | Named | Unnamed and not stated for the universal ranking | APP Thm 6.8: add the clause (R-A5) |
| Repair | "coherent improvement" / "replacement" | "repair theorem", "repair" | LDG §7 may say "the companion's repair theorem" (optional; it helps the reader link the papers) |

**Jargon sweep.** I grepped both PDF texts for: certificate, record, safe, route, repair region, gate, witness, visibility, splice, v3.3, draft, round, and the labels (B), (S), (I), (CC), (GI), (GP), (SI), (RS), (TG), (TS), (FCC), (W), (C), (G), (IB), (TC), (Add), (GC), (ID) and (LF).
- **LDG:** none found.
- **APP:** one hit, "route" (l. 1075).
  - (M1)–(M3) are labelled conditions with descriptive names. The brief permits "a few named conditions with descriptive names", and I consider them acceptable.
  - Optionally, the headline statements could spell them out: Thm 5.1 "Assume μ has finite first moment and null indifference boundaries".
- **Names on theorem-like environments.** APP's Example B.1, Example B.2 and Remark B.3 open with italic titles (*Dominance need not be uniform.*, *The null boundary … is essential.*, *Replacing 𝟙.*). These act as environment names, which the brief forbids. Move each into the sentence or drop it (minor). LDG has none.

---

## 5. The three questions in LDG

- **Abstract and §1.** These separate the three questions cleanly (abstract l. 37; §1 l. 46, l. 48–50 and l. 52).
- **§7 (l. 490).** It says explicitly: "Proposition 7.1 answers the third question directly. It does not pass through Bayes choices or compact families, and nothing requires a ranking built in this way to meet their hypotheses." This meets the audit.
- **The history of (S) and certificates** is not retold anywhere.

Two sentences slightly undercut this:
1. **§7, l. 490:** "So the results of Sections 3 and 5 that use no order properties are the relevant ones."
   - Section 5's theorems rest on KKM and compactness, and their hypotheses are sufficient conditions (Q2).
   - Calling them "relevant" to a constructed ranking invites the reader to expect them to be checked.
   - Replace with: "So, of the consequences in Section 3, those that use no order properties apply (Propositions 3.1 and 3.6(a),(b)); the dominance conclusion itself comes from Proposition 7.1(c), not from Section 5." (R-L1)
2. **§9, l. 628:** "In every application they come from Bayes choices with lower semicontinuous losses."
   - In context this means §8's applications. But the paper's abstract and introduction also present the companion as an application.
   - Change to "In every application of Section 8 …" (R-L1). Remark 5.9 already says "every application in Section 8".

Neither sentence creates a dependence. Both are wording.

---

## 6. Author blocks and titles

| | LDG | APP |
|---|---|---|
| `\title` | *Coherence, Dominance, and Generalized Loss* (title case) | *Coherence and accuracy for sets of desirable gambles* (sentence case) |
| `\author` | `Jason Konek and Catrin Campbell-Moore` (renders as one line with "and") | `Jason Konek \and Catrin Campbell-Moore` (renders as two side-by-side blocks, no "and") |
| `\date` | "October 2026" | empty |
| Affiliations, e-mail, ORCID, funding acknowledgement | none | none |
| PDF metadata | pdftitle set; no pdfauthor | neither set (`hidelinks`, no `\hypersetup`) |
| File name vs title | The file is "Loss dominance generalized (definitive)", but the title is v3.3's. WL68 offers *Coherence and Dominance under General Rankings* as an alternative. | match |

Findings:
- **Authors.** The authors are the same in both papers, as the brief requires. The lead was to flag this to the author.
  - Additional fact for that flag: the source of APP's core is `Universal coverage … (draft).tex`, whose author block is **Jason Konek alone**.
  - LDG v3.3 and the covering draft list both authors.
- **Formatting.** Make the author blocks and dates typographically identical: use the same `\author` form and the same date convention.
  - Neither paper has affiliations or a funding acknowledgement. A journal submission will need both (Department of Philosophy, University of Bristol; EPIMP, Horizon Europe grant 852677).
  - Adding them is the author's decision.
- **Title casing.** The two styles differ. This is harmless, since the journal will impose its own, but if the papers are submitted as companions it is worth aligning.
- **Description of each paper in the other.**
  - LDG's description of APP has the right title, the right authors, and accurate content, except for the missing qualifications (R-L2).
  - APP does not describe LDG at all. LDG calls APP "the companion paper", but the relationship is one-way (R-A7).

---

## 7. Unrefereed items: consolidated list for the verification referees

Key:
- **N** = new mathematics;
- **G** = glue;
- **U** = copied or compressed passage that has not been re-refereed;
- **P** = new interpretive prose that makes a factual claim;
- **C** = cited fact not re-verified.

Items marked ★ are ones I found in the manuscripts that the changes files do not list.

### LDG (WL68 list, plus additions)

| # | Item | Kind | My status |
|---|---|---|---|
| U-L1 | **Prop 7.1, statement and proof** | U | **Re-derived; correct** (§3.1) |
| U-L2 | Lemma 2.2, expanded lsc-transfer proof | G | Read; correct |
| U-L3 | Thm 4.2, direct KKM proof | G | Read; correct (it is Cor 5.2 combined with Lemma 2.3) |
| U-L4 | Ex 4.4: "every hypothesis of Thm 4.3 holds except compactness" | G | Read; correct |
| U-L5 | Remark 3.7 proof | U | Re-derived; correct |
| U-L6 | Prop 6.3, case (b) | U | Not re-derived by me (outside cross-paper scope) |
| U-L7 | Ex 6.4 (SSK09 Ex 2) verification | U | Not re-derived by me |
| U-L8 | Event-forecast paragraph (§8.1), including the glue clauses | U/G | Not re-derived by me |
| U-L9 | Randomisation lines in Ex 5.5 | U | Not re-derived by me |
| U-L10 ★ | §3.2 l. 132: in SSK09 Example 1, an incoherent forecast has the same total scores at every world as a coherent one | C | Not verified against SSK09 |
| U-L11 | Thm 8.2: zero credence function as the witness m′ ∉ C | G | Read; correct |
| U-L12 ★ | §1 Q3 paragraph and §7 closing paragraph: the description of APP and the representation-vs-justification sentence | P | Checked against APP; see R-L2, R-L4, R-L5 |
| U-L13 ★ | §9 "Other methods" sentence | P | Checked against APP App. D; accurate |
| U-L14 ★ | Abstract and §1, l. 46: "the rationally permissible models are exactly the coherent ones" | P | **Overstated.** Prop 3.6 also needs coherent admissibility, and the dominance conclusion for every ranking in the family (R-L8). |
| U-L15 ★ | Footnote on nomenclature (l. 67): "With finitely many worlds, their strict dominance is ours" | C | Plausible; not verified against SSK09 or Joyce |

### APP (WA68 list, plus additions)

| # | Item | Kind | My status |
|---|---|---|---|
| U-A1 | **Prop 6.3 (maximality)** | N | **Re-derived; correct** (§3.1) |
| U-A2 | Remark 4.4, first part (balls W, W′ with Gaussian μ) | N | **Re-derived; correct.** Both coordinates of m(N) equal ∫_W(h₁+h₂) dμ > 0. D_Δ misses N, and hull(∅) = D_Δ. |
| U-A3 | Sentence that the guidance-only relation has every property of Prop 6.2 | G | Correct; it is moreover transitive |
| U-A4 | §9.2: property (3) implies coherent admissibility | G | Correct, given (M2) through Lemma 6.5. The sentence should say "under (M2)". |
| U-A5 | Ex 6.4 moved to ℝ² | G | **Re-derived; correct** (both bullets, and the 1.075δ bound) |
| U-A6 | Ex B.1 write-up (Lyapunov ball, A₀ ⊆ D_S) | G | Not re-derived by me |
| U-A7 | §9.3: mutually singular measures (D₀, D₀ + x₀, disjoint line families) | G | Re-derived; correct |
| U-A8 | μ = δ_𝟙 + δ_{−𝟙} instance (§2.3) | G | Correct (and used in R-A1) |
| U-A9 | ∂D_Q = {P_Q = 0} (Lemma 2.1(c)) | G | Correct |
| U-A10 | Prop 6.7: direct (i)⇒(iv) | G | Read; correct |
| U-A11 | Thm 8.1(b): "K\* contains p and some v_i" | G | Correct (Step 7, W₀ ≠ ∅) |
| U-A12 | §8: "U itself is dominated" | G | Correct; needs ε > 0, which holds |
| U-A13 | App. D specialised to A_i = {v_i}, especially Step 7's form of g | G | Steps 4 and 7 checked; Steps 5, 6 and 8 read |
| U-A14 | Models as completion-measurable sets (a change of definition) | G | Harmless; every notion is class-invariant |
| U-A15 ★ | §3, l. 455–457: "With finitely many worlds, Lyapunov's theorem makes the set of score vectors of ordinary acceptance sets convex and compact" | P | **False without non-atomicity.** (M2) allows atoms, for example APP's own δ_𝟙 + δ_{−𝟙}. Insert "and non-atomic μ" (R-A8). |
| U-A16 ★ | §1, l. 150–151: "Coherent models are protected by the rule itself" | P | **Overstated.** It also needs (M2) through Lemma 6.5, which Ex B.2 shows is essential (R-A6). |
| U-A17 ★ | Abstract, §1, §8: "incomplete and intransitive" | P | **False in general** (R-A1) |
| U-A18 ★ | Remark 5.2(c): no Lyapunov theorem, no non-atomicity and no full support are used | P | Correct on inspection of the proof of Thm 5.1 |
| U-A19 ★ | §9.3: "Some condition of the second kind is needed: at a world where every gamble pays 0 …" | G | Correct: only null changes are guided there, and clause (ii) never applies |
| U-A20 ★ | §9.3: "Multiplying the score at each world by a positive constant leaves the ranking unchanged" | G | Correct |
| U-A21 ★ | §1, l. 82–84: the "Brier-type" reading of the score | P | Interpretive; the displayed identity in §2.2 is correct |
| U-A22 | Bibliographic details: Aliprantis–Border Thm 6.30; Quaeghebeur chapter pages 1–27 | C | Not checked (WA68 flag 4) |

---

## 8. Ranked required changes

The order within each paper is by importance. **Required** means needed for cross-paper consistency or correctness. **Recommended** means it should be done. **Optional** is optional.

### APP (`Coherence and accuracy for sets of desirable gambles.tex`)

1. **R-A1 (Required, correctness).** Qualify "incomplete and intransitive".
   - **Where:** abstract l. 58; §1 l. 123 and l. 160–161; §8 l. 1005 and l. 1086–1087.
   - **Change to:** "in general incomplete and not transitive". Ex 6.4 should keep its own, specific claim.
   - **Why:** for μ = δ_𝟙 + δ_{−𝟙} the ranking is transitive (§3.3). BRIEF68 and LDG both say "in general".
   - **Optional addition:** note that the guidance-only relation is always transitive. This sharpens the l. 745–748 sentence.
2. **R-A2 (Required, terminology).** Define "available".
   - **Def 2.5:** after "could make this change", add "; we also say that the change is *available to* Z".
   - **l. 88:** replace "its change would never be available from a coherent model" with "no coherent model could make the change".
   - This aligns APP with LDG's defined term, which LDG glosses with APP's "could make".
3. **R-A3 (Required if LDG keeps "coverage", see R-L3).** Decide jointly with LDG. If LDG renames its hypothesis, APP needs no change.
4. **R-A4 (Required, jargon).**
   - **l. 1075:** "It is the classical route from admissibility to coherence" → "It follows the classical argument from undominatedness to coherence". This removes the banned word "route" and the clash with LDG's "coherent admissibility".
   - **"The universal ranking"** (l. 160, 1086, 1092, 1095): define it at first use, or replace it with "the ranking of Definition 6.1".
5. **R-A5 (Required, consistency with LDG's central notion).** Thm 6.8: add to (b) "In particular, every model is weakly dominated by an undominated coherent model." This is LDG's dominance conclusion (W), which VB Thm 8.1(b) already states for the contrast ranking. It follows at once from Prop 6.6 and (b).
6. **R-A6 (Required, accuracy of the achievement/limitation statement).**
   - **§1 l. 150–151:** "Coherent models are protected by the rule itself, since …" → "Coherent models are protected by the rule together with the null-boundary condition (M2): any change a coherent model could make is accepted only as guidance, and under (M2) no non-null change guided at every world is available to a coherent model."
   - **§9.1 l. 1115:** "Properties (1)–(3) … protect coherent models" → "Under (M2), properties (1)–(3) … protect coherent models".
   - **Why:** this matches LDG's treatment of protection as a separate hypothesis (Prop 7.1(b)) and APP's own Ex B.2.
7. **R-A7 (Required for companion status).** Add one non-load-bearing pointer to LDG, for example at the end of §1 "What this achieves" or in §9.1:
   > "The ranking is an instance of a general construction for arbitrary models and rankings studied in a companion paper [Konek and Campbell-Moore, *Coherence, Dominance, and Generalized Loss*], which also develops the consequences of dominance for rankings that need not be transitive. The proofs here are self-contained."
   - Keep it a citation only. Do not import any result. This preserves acyclicity of the dependency graph, because LDG cites APP only for examples and attribution.
8. **R-A8 (Required, correctness).** §3 l. 455–456: "With finitely many worlds, Lyapunov's theorem makes …" → "With finitely many worlds and a non-atomic μ, Lyapunov's theorem makes …".
9. **R-A9 (Recommended).**
   - **§6.2 l. 818:** say that uniform dominance is measured in the score ("…and inf_ω(m_ω(Y) − m_ω(X)) > 0; the margin is measured by the score").
   - **§9.2 l. 1128:** "coherent admissibility: that coherent models remain undominated" → "coherent admissibility (in the sense used for families of rankings: every coherent model is undominated)".
   - **U-A4 sentence:** add "under (M2)".
10. **R-A10 (Optional).**
    - Remove the italic lead titles of Ex B.1, Ex B.2 and Rem B.3, since the brief forbids names on environments.
    - Align the `\author`/`\date` form with LDG, and set `pdftitle`/`pdfauthor`.
    - Harmonise "represent it exactly" (§1) and "single it out" (§9.1) to one phrase shared with LDG.

### LDG (`Loss dominance generalized (definitive).tex`)

1. **R-L1 (Required, the three questions).**
   - **§7 l. 490:** replace "So the results of Sections 3 and 5 that use no order properties are the relevant ones." with "So, of the consequences in Section 3, those that use no order properties apply; the dominance conclusion itself comes from Proposition 7.1(c), not from Section 5."
   - **§9 l. 628:** "In every application they come from …" → "In every application of Section 8 they come from …".
2. **R-L2 (Required, accurate description of the companion).** At §1 l. 52 and §7 l. 490, add APP's standing qualifications. For example, in §7:
   > "For coherent sets of desirable gambles on an arbitrary set of worlds, with gambles forming a separable space that contains the constants, models identified up to null sets of a fixed measure, and that measure satisfying a finite-moment and a null-boundary condition, the companion paper~\cite{KCM} proves that every incoherent model can be replaced by a coherent one through a change available to no coherent model that raises the score at every world by a uniform margin …"
   - This also corrects "improvement … available to no coherent model" to "change … available to no coherent model".
   - In §1 a shorter clause suffices: "(for a separable space of gambles containing the constants, with models identified up to null sets)".
3. **R-L3 (Required, terminology collision).** Rename hypothesis (ii) of Thm 5.1 and (b) of Thm 5.6 from "coverage" to a term that does not clash with the companion's "covers K", for example **"matching at a charged world"**.
   - Occurrences: l. 318, 337, 340, 353 (Example 5.4), 378, 402, 405 and 408 (Remark 5.9). The figure caption (l. 221) and "open cover" (l. 280, 393) can stay.
   - Alternatively APP renames "covers", but that is its headline notion, so the LDG change is cheaper.
4. **R-L4 (Required, what is left open).** At the end of §7, after the limitation sentence, add:
   > "The companion paper shows that, for its score, this ranking is the largest relation that accepts every guided comparison, accepts comparisons between distinct models only when they raise the score, and accepts a change available to a coherent model only as guidance. The last requirement restricts individual comparisons at individual worlds and is stronger than coherent admissibility; its independent justification is open."
   - Add the corresponding item to §9 "Open questions".
   - This brings LDG in line with APP §9.2 and BRIEF68's author addition 5.
5. **R-L5 (Required, dangling referent).** §7 l. 490, "it shows that the ranking requirements are compatible with coherence": LDG never lists "the ranking requirements". Replace with "it shows that rankings guided by the truth, acyclic and closed under ties are compatible with coherence and can single it out exactly", or point to the companion's list.
6. **R-L6 (Required, terminology).** Ex 5.4 l. 349: "with scores (t, 1−t) for c_t and (2, 2) for x_t, lower being better" → "with losses (t, 1−t) … and (2, 2)", and "the score of m at ω" → "the loss of m at ω".
   - **Why:** "score" is larger-is-better in §7 and throughout APP.
7. **R-L7 (Recommended).** Define "tied at ω" in §2 (l. 63): "m and c are *tied at ω* if m ⪯_ω c and c ⪯_ω m". It is used in Prop 7.1(a).
8. **R-L8 (Recommended).** Abstract l. 37 and §1 l. 46: "the rationally permissible models are exactly the coherent ones" → add "given coherent admissibility" (Prop 3.6 needs it).
9. **R-L9 (Optional).**
   - In §7, name the companion's result: "the companion's repair theorem".
   - Unify "guided at ω" with APP's form; see §4 for the preferred choice.
   - Align the `\author`/`\date` form with APP, and add `pdfauthor`.
   - Decide the title. The file name and the paper's title differ; WL68 offers *Coherence and Dominance under General Rankings*. Whatever is chosen must match APP's citation once R-A7 is made.

### Nothing required on the following
- **Circularity:** none (§1.4).
- **Reliance on deleted material:** none (§2).
- **Statements of Prop 7.1 and APP Def 6.1, Props 6.2, 6.3, 6.6, 6.7:** these agree exactly (§3.1).
- **The Zorn-lemma argument:** it is present in APP App. D with the content LDG §9 attributes to it (§1.3).
- **Dominance nomenclature, closure under ties, acyclicity:** consistent (§3.2).
