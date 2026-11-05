# RD78 referee report: the dominance argument (Short §3, handout §3, Full §6.1)

## Verdict

**Accept after five small required fixes.** The theorem and its proof are correct. I re-derived every step, and each cited result gives exactly what the step uses. The UPDATE's (E), (A), (S), (T) are stated as specified. Prop prop:family is gone from Short and Full; in the handout it is wrapped in `comment`. Numbering is in sync. The author's handout edits are preserved. All three files compile cleanly.

The required fixes:
- two sentences that claim more than is true ("(S) asks only…" and "proved from coherent admissibility…");
- a logical gap in the (P1)–(P3),(C) summary;
- one false sentence in the full paper (the applications);
- one under-stated example (the (S) example).

There is also one handout figure fix.

## What I checked

**Proof, step by step (identical in all three documents).**
1. Step 1 is correct.
   - (S) puts every assigned model c_p or c_θ in C_L, and C_L ⊆ M_L.
   - Under a fixed L, "model" ranges over M_L, so the hypotheses of Thm 2.2/2.4 and Cor 2.3 quantify over M_L.
   - Thm 2.2 gives a pmf whose assigned model weakly dominates m. Cor 2.3 reduces to it. Thm 2.4 gives θ* with c_θ* weakly dominating m.
2. Step 2 is correct. Lemma 1.7(b) needs a weakly dominating m, a ∈ C_L, m ∉ C_L and L closed under ties, and all four are available.
3. Step 3 is correct.
   - Steps 1–2 hold for every L with m ∈ M_L, so "evaluates" is respected.
   - Lemma 3.2 (the equivalence) needs no (E). (E) is needed only for "dominated under at least one ranking".
4. Step 4 is correct: C_L ⊆ M_L ∩ U_L.
5. Step 5 is correct.
6. Step 6 is correct. (S) gives 𝒜 ⊆ C_L, and with (T) these are the hypotheses of Cor 2.5(c).
   - Cor 2.5(c)'s proof uses only Lemma 1.7(a),(b). The argument does not use Cor 2.5(a).
   - Lemma 1.7(c) enters only indirectly; see recommendation R1.

**Other claims, all verified:**
- The remark that (E) is used only for the last claim is true. Without (E), unevaluated incoherent models are vacuously irrational and not permissible, which is consistent with (C).
- "Steps 1 and 6 use (S) only through weak domination by C_L" is true.
- "No property of the relations" is true.

**(T) example (all three): correct.** One world; a ⪯ a, a ⪯ m, m ⪯ a, m ⪯ m. Then:
- U_L = {a, m} and C_L = {a};
- (E) holds, and (A) holds;
- (S) holds via Cor 2.3 with c_δ = a, which is competitive, and the comparison sets are all of Δ, so closed;
- (T) fails, and m is permissible.

**(S) example (Full, Ex 3.6): mathematically correct, but under-stated.** Take 𝔏 = {L} with M = M_L. Then:
- (E) holds, and (A) holds because every e_n is undominated;
- (T) holds because no two distinct models are tied;
- x is undominated.

(S) fails because Thm 2.4 would give a weak dominator of x in C_L = {e_n}, and no e_n weakly dominates x, since L(e_n, n+1) > 1. The text says neither that (E), (A) hold for the singleton family nor the last clause. See Fix 4.

**The Full paper's claim that the Bayes theorems are cases of Cor 2.3 / Thm 2.4: correct.** The paper's own remarks after Cor 4.3 and Thm 4.6 verify it.

**Cross-references.** I checked the Full paper's abstract, intro ¶2, the "dominance argument" paragraph of the intro, the Def 2.9 sentence, Def 2.11, inventory items (2), (4) and (6), §6 intro, §6.2 intro, the remark after Prop 6.9, §7, and Scope. All are accurate except Fix 3 and Fix 5 below, plus R2. No mention of prop:family or "premise (i)" remains.

**Numbering.** The Short paper's .aux gives:
- Def 3.1, Lem 3.2, Def 3.3, Thm 3.4;
- Props 3.5, 3.6, 3.7;
- §1–2 unchanged, with Lem 1.7, Thm 2.2, Cor 2.3, Thm 2.4, Cor 2.5.

Every hard-coded number in handout §3 matches, including those in the figure captions and in the proof headings.

The Full paper's .aux gives:
- Def 6.1, Lem 6.2, Def 6.3, Thm 6.4;
- Prop 6.5, Ex 6.6, Prop 6.7, Ex 6.8, Prop 6.9.

**Handout diff against handout_user1529.tex.**
- Lines 1–373 (title, §1–2, removed figures, comment blocks, % lines, the commented-out Lemma 1.7(c)) are byte-identical.
- In §3, the author's `%The equivalence …` line, the in-box `%Each incoherent model …` edit and the `%Proposition 3.3 does not prove …` paragraph are all kept verbatim.
- The old Prop 3.3 box is inside `\begin{comment}`.
- I found no unintended change.
- Additions that exist only as source comments:
  - a `%` line with the KCM sentence;
  - a `%` note "Former Proposition 3.3, superseded…".

**Compilation.** I compiled all three in r77/RD78_build/ with pdflatex ×3. There are 0 errors, 0 warnings, 0 undefined references and 0 overfull or underfull boxes. Page counts: Short 6 pp, Full 30 pp, handout 7 pp.

## Required fixes

### 1. Short §3 and Full §6.1: the "Second" point of "Three things are not assumed" is wrong as stated

"(S) asks only that the assigned models perform at least as well as each model…" is false. (S) also requires that the assigned models be **undominated coherent models**, which is a dominance condition, and it requires the closedness and compactness conditions. "(T) concerns ties, not dominance" hides what (T) does say about incoherent models.

**Short, replace:**
```
Second, it is not assumed that any incoherent model is dominated. Condition (A) concerns coherent models only; (S) asks only that the assigned models perform at least as well as each model at the worlds specified in the hypotheses of those theorems; and (T) concerns ties, not dominance. That every incoherent model is dominated, and so irrational, is proved in Theorem~\ref{thm:argument}.
```
**with:**
```
Second, it is not assumed that any incoherent model is dominated. Condition (A) concerns coherent models only. Condition (S) concerns the assigned models: they must be undominated coherent models and must meet the conditions of one of the theorems of Section~\ref{sec:general}, which compare them with each model at particular worlds; it says nothing about which other models are dominated. Condition (T) concerns ties: it implies that no incoherent model is tied at every world with an undominated coherent model, but not that any incoherent model is dominated. That every incoherent model is dominated, and so irrational, is proved in Theorem~\ref{thm:argument}.
```

**Full, replace:**
```
Condition (A) concerns coherent models only; (S) asks only that the assigned models perform at least as well as each model at the worlds specified by the guarantee and serving conditions; and (T) concerns ties, not dominance.
```
**with:**
```
Condition (A) concerns coherent models only. Condition (S) concerns the assigned models: they must be undominated coherent models and must meet the guarantee and serving conditions of one of the theorems of Section~\ref{sec:general}, which compare them with each model at particular worlds; it says nothing about which other models are dominated. Condition (T) concerns ties: it implies that no incoherent model is tied at every world with an undominated coherent model, but not that any incoherent model is dominated.
```

### 2. All three: (P2) is stated one way only, so (C)'s "exactly" does not follow

From the conditionals "dominated everywhere ⇒ irrational" and "undominated somewhere ⇒ permissible", together with (P3), we get only "incoherent ⇒ irrational" and "coherent ⇒ permissible". Nothing excludes an incoherent model also being permissible. The argument needs the definitional "exactly when", which gives disjointness (Lemma 3.2).

**Short and Full, replace:**
```
\item \emph{Dominance principle} (Definition~\ref{def:permissibility}). A model dominated under every ranking in $\Lf$ that evaluates it is irrational. A model undominated under some ranking in $\Lf$ that evaluates it is rationally permissible.
```
**with:**
```
\item \emph{Dominance principle} (Definition~\ref{def:permissibility}). A model is irrational exactly when it is dominated under every ranking in $\Lf$ that evaluates it, and rationally permissible exactly when it is undominated under some ranking in $\Lf$ that evaluates it; so no model is both (Lemma~\ref{lem:complement}).
```
**Handout:** make the same replacement, with `(Definition 3.1)` and `(Lemma 3.2)` hard-coded.

### 3. Full §6 intro: wrong attribution to coherent admissibility

"it is proved, from coherent admissibility and the other assumptions" is misleading. Steps 1–3 never use (A). The dominance of incoherent models comes from (S) and (T) alone; (A) is used only in step 4.

**Replace:**
```
That incoherent models are dominated is not assumed: it is proved, from coherent admissibility and the other assumptions, using the results of Section~\ref{sec:general}.
```
**with:**
```
That incoherent models are dominated is not assumed: it is proved from selection and closure under ties, using the results of Section~\ref{sec:general}; coherent admissibility is used only to show that the coherent models are rationally permissible.
```

**Note for the author, plainly stated.** The brief says coherent admissibility is used to prove that incoherent models are irrational. In this argument it is not. The ranking-level admissibility built into (S) does that work: the assigned models must be undominated coherent models, which is the analogue of the old (LA). (T) does the rest. This is not a defect of the theorem, but the prose should say what the proof actually uses.

### 4. Full §6.1: state the (S) example fully

**Replace:**
```
Neither (S) nor (T) can be dropped. In Example~\ref{ex:main} the ranking is closed under ties and every coherent model is undominated, yet the incoherent model $x$ is undominated; under any family containing that ranking, $x$ is rationally permissible. Here (S) fails, since Theorem~\ref{thm:local} would make $x$ weakly dominated by an undominated coherent model.
```
**with:**
```
Neither (S) nor (T) can be dropped. For (S), let $\Lf$ consist of the ranking of Example~\ref{ex:main} alone. It evaluates every model, every coherent model is undominated, and distinct models are never tied, so (E), (A) and (T) hold. Yet the incoherent model $x$ is undominated, so it is rationally permissible. Here (S) fails: by Theorem~\ref{thm:local} it would make $x$ weakly dominated by some $e_n$, and no $e_n$ weakly dominates $x$.
```

### 5. Full §6.1: "the applications in Section 8 verify it" is false for §8.5

For the loss of Proposition 8.13 (prop:joyce), no coherent credence weakly dominates x*, so (S) fails there.

**Replace:**
```
the applications in Section~\ref{sec:apps} verify it in this form for the rankings they consider.
```
**with:**
```
the applications in Sections~\ref{sec:proper}--\ref{sec:conditional} and Proposition~\ref{prop:countable} verify it in this form for the rankings they consider; for the loss of Proposition~\ref{prop:joyce} it fails, since no coherent credence weakly dominates $x^*$.
```

### 6. Handout Figure 5: step marker ④ sits outside 𝒞

The marker ④ is placed in 𝓜 \ 𝒞, at the lower left. Step 4 concerns coherent models, so this placement is misleading. I tested the fix below: it compiles cleanly and the marker sits beside the label "𝒞 = …", with no overlap.

**Replace:** `\node at (0.5,0.9) {\stp{4}};`
**with:** `\node at (5.75,0.25) {\stp{4}};`

## Recommendations (not required)

**R1. Lemma 1.7(b) is proved via (c), in the Short and Full papers.**
The UPDATE says not to rely on 1.7(c). Step 2 cites (b), and (b)'s proof there reads "This is (c) with 𝒜 := C_L". This is harmless in the handout, where the author has commented out the proofs, but in the papers it is an indirect reliance on (c). Give (b) its own proof.

In the Short paper, replace:
```
(c) Since $m\notin\mathcal A$, $m$ is not tied at every world with $a$. (b) This is (c) with $\mathcal A\coloneqq\C_L$.
```
with:
```
(b) Since $L$ is closed under ties, $a\in\C_L$ and $m\notin\C_L$, $m$ is not tied at every world with $a$. (c) Likewise, since $\mathcal A$ is closed under ties and $m\notin\mathcal A$, $m$ is not tied at every world with $a$.
```
The Full paper's proof needs the same change: there the line reads "(c) Since … so $a$ dominates $m$. (b) This is (c) with …".

**R2. Full §7: the parenthetical is ambiguous.**
In "Proposition 6.9 except part (c), whose last claim is…", the word "whose" can be read as referring to part (c). Replace it with:
```
(Lemma~\ref{lem:complement}, Proposition~\ref{prop:conclusion}, and Proposition~\ref{prop:permissible} except part~(c); the last claim of Proposition~\ref{prop:permissible} is the conclusion of Theorem~\ref{thm:argument} with the dominance property in place of (S))
```

**R3. A choice for the author.**
In the old handout Prop 3.3, the author commented out "Each incoherent model is dominated under at least one ranking in 𝔏". Theorem 3.4 now restates this as its last sentence, in all three documents. If the author's edit reflects a preference, drop that sentence from Thm 3.4 / 6.4 and step 3's "(E): …" clause, everywhere and consistently. (E) would then appear only in Lemma 3.2.

**R4. The KCM sentence in the handout.**
It exists only as a `%` line, because the author had commented out the KCM paragraph. That was the right call given the UPDATE. The author should confirm.
