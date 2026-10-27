# AUDIT_fU: does any argument use "evaluable models agree on f because f ∉ U"?

14 Oct 2026. Reading used: `termfix/TERMFIX_RULES.md` (authoritative). On M_U, evaluable models agree on the choice
represented by f (all give no advice) only when f ∉ U **and** −f ∉ U. A pair {g,−g} whose H-representative g ∉ U but
−g ∈ U is inside the domain: its advice range is {0,−} in H-bookkeeping, i.e. {accept −g, no advice}.

Files checked: the write-up `writeup/The Contamination Triangle.tex` (all of §§2–7 that use M_U, the U-domain or a
decomposable domain), N9 (N9.4), N12, N13 (Prop A, Prop B), N15, N17, N19, N22, N24, N25 + referee, N26 + referee and both
scripts, N27, R1 (Lemmas 1.1–1.5, Props 2.1, 2.4, 2.5), R2 and R7 (two-world parametrisation), R11 (Lemma IC, Lemma K,
Thm W), CCIBU.tex. N14 was also spot-checked, because the write-up's Corollary `cor:coverage` rests on N14 §3(iv).
New scripts: `audit_fU_py/` (copies of `n26py/warmup.py` and `n26ref_py/check_n26_1.py`, re-run unchanged, plus a new
independent `orientation_check.py`). No other file was edited.

---

## 0. Verdict

**No step anywhere uses the false claim. Nothing NEEDS REPAIR; every result survives as stated.**

- Every argument on M_U works with a model as a measurable X ⊆ U and indexes each pair that meets U by its orientation
  in U. This includes c : U → ℝ³, B_q = {g ∈ U : q·c(g) > 0}, the tie sets Z_q ⊆ U, the error sets
  E_i(X) = X △ (U ∩ {h_i > 0}) ⊆ U, the weights ν_i and densities ρ_i "on U", the regular models, the atoms G_k ⊆ U, and
  integrals ∫_U. Each of these covers U ∩ {g₁ < 0} automatically. That part of U is non-null: for T1 it is about a
  quarter of μ(U) at s = 0.9, and it contains the whole facet F₁ (h₁ < 0 on F₁) and the box witness A ∈ relint F₁. The
  main chain uses both, so a version restricted to U ∩ H could not even be stated.
- Wherever "all evaluable models give the same advice / the penalty drops out / every model gives no advice" is
  asserted, the set meant is the set of pairs that do **not meet** U (f ∉ U and −f ∉ U). This holds in the write-up
  l. 213–215, N9.4, N14 §1 and N27 §1.5.
- Wherever (IB) or splicing is applied on M_U, the splice set is symmetrised (N25 Lemma 8.1 says so explicitly:
  A := S ∪ −S, contexts in A^c because U ∩ −U = ∅), or it is a subset of U, which is equivalent because every model lies
  in U.
- The two-world constructions handle both orientations.
  - N26.1 (and its scripts), N17.8 and N19's p₀ computation each have an explicit "+ side" r < ½ (U-orientation in H)
    and "− side" r > ½ (U-orientation −g, g₁ < 0, advice range {accept −g, no advice}).
  - r(g) = −g₂/(g₁−g₂) is invariant under g ↦ −g, so indexing by the H-representative loses nothing.
  - The N26.1 target's upper endpoint 0.625 lives entirely on the − side, and (LF) there is verified with "orientation
    −g ∈ U" (N26 l. 214).
  - R2 and R7 work on general decomposable domains with advice {+,0,−} on all mixed pairs, so the issue does not arise.
- What remains are **harmless slips of notation**. In the (CP-a) part, functions on U (Λ_iX = 1_{E_i(X)}, densities ρ_i,
  "U = N_i", c_i = ρ_i(λ_i(·,0) − λ_i(·,+))) are silently identified with functions on H, where (CP-a) is formulated
  (L^∞(H,μ)). The intended identification is the measure-preserving bijection ι : U → H ∩ (U ∪ −U), g ↦ sign(g₁)·g
  (μ is symmetric). Under ι:
  - "accept g" is advice + at ι(g) = g when g₁ > 0, and advice − at ι(g) = −g when g₁ < 0;
  - N_i on M_U is H ∩ (U ∪ −U), the pairs meeting U, **not** H ∩ U.
  No proof uses H ∩ U. One wording slip in N14 ("forced silence only off U′") reads correctly only as "on pairs with
  f ∉ U′ and −f ∉ U′".

---

## 1. Table

Verdicts: CORRECT = handles both orientations / requires f, −f ∉ U; HARMLESS SLIP = wording or notation only, the
mathematics uses the right set; NEEDS REPAIR = none found.

| File | Location | Quote (abridged) | Verdict | Repair / comment |
|---|---|---|---|---|
| write-up | l. 131 | "each pair is indexed once by its member in H … nothing depends on this convention" | CORRECT | General bookkeeping; on M_U the write-up switches to U-orientations at l. 215. |
| write-up | l. 178 (Def. LF) | "for a.e. pair with an orientation h ∈ N the advice range contains both 'accept h' and no advice" | CORRECT | Orientation language. N ⊆ U and −N ∩ U = ∅, so R △ D_T ⊆ N keeps R ⊆ U. |
| write-up | l. 203 | "On a problem on which all evaluable models give the same advice, the penalty … drops out" | CORRECT | Stated for advice ranges of size 1, not for "f ∉ U". |
| write-up | l. 210–213 | "For f with −f ∈ U the same holds with g and h swapped … For f with f,−f ∉ U, every evaluated D … no advice" | CORRECT | This is exactly the author's reading. Optionally write "f ∉ U and −f ∉ U" (§2). |
| write-up | l. 215 | "On M_U we index each pair that meets U by its orientation g ∈ U. Only the vector c(g)=ℓ(g,0)−ℓ(g,+), g ∈ U, enters … (on every other problem all evaluable models give the same advice …)" | CORRECT (wording could be sharper) | "every other problem" = pairs not meeting U. Also ℓ(g,+) for g ∈ U ∩ {g₁<0} means "accept g", i.e. ℓ(−g,−) in H-bookkeeping. Reword per §2. |
| write-up | l. 216–218 | B_q = {g ∈ U : q·c(g) > 0} | CORRECT | Over all of U. |
| write-up | l. 222, 228, 230, 239 | (CP-a) on L^∞(H,μ); "On M_U the canonical encoding is Λ_iX = 1_{E_i(X)} with E_i(X) := X △ (U ∩ {h_i>0})" | HARMLESS SLIP | E_i(X) ⊆ U while Λ_i lives on H. Add "transported to H by g ↦ sign(g₁)g". Nothing depends on it. |
| write-up | l. 242 | error set: "h ∈ U with h_i>0 that X does not accept, together with those with h_i<0 that it accepts" | CORRECT | All of U. Regular = accepts a.e. g ≥ 0 of U; −g ∉ U for g ≥ 0. |
| write-up | l. 247–248 | ν_i "on U", ρ_i > 0 a.e. on U, ψ_i = ∫_{E_i(X)}ρ_i dμ | CORRECT | |
| write-up | l. 278–295, Prop. reduction, Lemmas chords/levels/UVN/PL2/nopin, Thm pivot, Lemma edgebox (l. 533–537) | c : U → ℝ³; A, B ∈ U²; "If A+λB ∉ U this contradicts P ≤ P_{K′} ≤ 0" | CORRECT | The edge box uses only "A+λB ∉ U ⇒ P_{K′}(A+λB) ≤ 0". It needs no claim about −(A+λB). The box witness A = (−β(1+η), η, 1) ∈ U has A₁ < 0 and is used. |
| write-up | l. 409 (Lemma PL2) | "automatic on M_U, where no advice range contains both acceptances" | CORRECT | True because U ∩ −U = ∅. |
| write-up | l. 620 | "The U-domain and Cor. coverage are unaffected: they use the explicit cones U and D_{K′}" | CORRECT | |
| write-up | l. 810, 820 | N_i = problems whose advice range has ≥ 2 elements; ρ_P > 0 a.e. on N_i | CORRECT | On M_U, N_i = H ∩ (U ∪ −U). Optional parenthesis (§2). |
| write-up | l. 852 (proof of Cor. residual) | "(on M_U …) the vector c_i := ρ_{P_i}(λ_i(·,0) − λ_i(·,+))" | HARMLESS SLIP | Read as a function of the U-orientation g: c_i(g) = ρ_{P_i}(ι g)(λ_i(ι g, 0) − λ_i(ι g, a_g)), with a_g ∈ {+,−} the advice "accept g". Reword per §2. |
| write-up | l. 857 | (UN) "true on M_U with U_+ = U ∩ {g ≫ 0}" | CORRECT | g ≫ 0 has g₁ > 0, and −g ∉ U. |
| write-up | l. 917–921, 941, 948 | c_i(g) = ρ_i(g) sign(g_i), B_q, Z_q ⊆ U; V_ψ(t) = ∫_U … ; atoms G_k ⊆ U | CORRECT | Direct check: ψ_i(X) = const − ∫_X ρ_i sign(g_i) over all of U. |
| write-up | l. 995 | 𝓛₂ˢ: ψ_i = ∫_{E_i(X)} ρ_i, S_i = ∫σ_i(g, a_X(g)) | CORRECT | |
| write-up | l. 998, 1007 (Thm N26.1, proof sketch) | "For mixed g put r(g) := −g₂/(g₁−g₂) … θ … equal to t₀ on r ∈ [0.2,0.3] on one side, and strictly increasing on the other" | HARMLESS SLIP (vagueness) | r is pair-invariant (r(−g) = r(g)). "One side" = pairs whose U-orientation has g₁ > 0 (r < ½); "the other" = pairs whose U-orientation has g₁ < 0 (r > ½). "θ nondecreasing" holds on each side separately: θ drops from 0.4 to 0.1 at r = ½. Reword per §2. |
| write-up | l. 1060–1062, 1086 | permitted-tie realisation c : U → ℝ³; (X_ik) "x ∈ U with v_k·x < 0" | CORRECT | The (X_ik) witnesses near F₁ have x₁ < 0. |
| N9 | l. 102–110 (N9.4) | "On a pair {g,−g}, 'accept the orientation in U' is available iff an orientation lies in U … M_U = {X ⊆ U}"; E_i(X) = X △ P_i | CORRECT | The model of the correct reading. |
| N9 | l. 235 (Design A) | "For an orientation h ∈ U (mixed, or nonnegative)" | CORRECT | |
| N12 | l. 104–108, §1 | c : U → ℝ³; B_q ⊆ U; (R1) tie set in U | CORRECT | |
| N12 | l. 185–191 | "If g + g′ ∉ U, then P(q, g+g′) ≤ 0 for all q, because K_q ⊇ K′" | CORRECT | Uses only g+g′ ∉ U ⇒ P_{K′} ≤ 0. |
| N12 | l. 430–447 (§6 charges) | ν_i on subsets of U; splice on Y ⊆ U | CORRECT | Every model lies in U, so a splice on Y is a splice on Y ∪ −Y. |
| N13 | l. 243–262 (Prop A) | "A = C* ∩ (positive orthant) ∩ U", B ⊆ E_ω(C*) | CORRECT | |
| N13 | l. 297–330 (Prop B) | ρ_i > 0 "on non-forced problems"; "(γ) Fubini on H × Δ" | CORRECT | General domain, H-indexed; on M_U, non-forced = pairs meeting U. |
| N13 | l. 369–370 | "ν_i ~ μ on U. … accept h iff Σ_{h_i>0} p_iρ_i(h) > Σ_{h_i<0} p_iρ_i(h)" | CORRECT | h ranges over U. |
| N14 (extra) | l. 75 | "Menus are {+,0} on pairs meeting U, and forced silence otherwise" | CORRECT (old terminology) | "pairs meeting U" is right. |
| N14 (extra) | l. 311 | "Forced silence can occur only off U′" | HARMLESS SLIP | Must mean "only on pairs {f,−f} with f ∉ U′ and −f ∉ U′". Under the literal "f ∉ U′" reading it would be false for H-representatives f with −f ∈ U′. Nothing depends on it. |
| N14 (extra) | l. 299–309 (§3(iv)) | B_q ∩ U′ ≈ D_{K̂_q}; "Charts of g ∈ U′ are half-planes" | CORRECT | Orientation-based (R1 Prop 2.5). |
| N15 | l. 41–42, 149, 167, 183 | g ∈ U, I_g = {c : g − c𝟙 ∈ U, mixed} | CORRECT | Levels and chords on all of U; F₁ ⊆ {h₁ < 0} is treated like the other facets. |
| N17 | l. 9, 17–22 | M_U; P_i = U ∩ {h_i>0}; E_i(X) = X △ P_i; 𝒞 = functions on U | CORRECT | |
| N17 | l. 127 | "ten cells R_S … partitioning U" | CORRECT | |
| N17 | l. 402–410 (Prop 6.3, n = 2) | "L = {x < α′} ('accept g or silence') and R = {x > β′} ('accept −g or silence')" | CORRECT | Both orientations. Pairs with α′ < x < β′ meet neither U nor −U. |
| N19 | l. 61–65, 359–373 | 𝔚^reg: "X regular if it accepts every non-negative problem of U" | CORRECT | |
| N19 | l. 274–276 + `n19py/n2_block.py` | p₀: "the non-negative quadrant carries half of H's mass, and L ∪ R lies in the other half" | CORRECT | The script's L ∪ R includes the "accept −g" side (x > b/(1−b)). |
| N22 | l. 12–13, 28, 33 | N_i = non-forced problems; ρ_P > 0 a.e. on N_i | CORRECT | General. On M_U, N_i = H ∩ (U ∪ −U). |
| N22 | l. 232–235 | (UN) on M_U with U_+ = U ∩ {g ≫ 0} | CORRECT | |
| N22 | l. 253–257 | "w̄(g) the world-i-worst available action … ν_C(S) for S ⊆ H∖F" | CORRECT | Ranges over all available advice, so both orientations are included. |
| N22 | l. 375, 413–414 | (CP-a2) on L^∞(H,μ); "Λ_iX = 1_{E_i(X)} with E_i(X) = X △ (U ∩ {h_i > 0})" | HARMLESS SLIP | The same transport ι as in the write-up, l. 239. |
| N24 | l. 150–151 | "On M_U, put c_i(g) := ρ_i(g)(λ_i(g,0) − λ_i(g,+)). It has the strict sign of g_i a.e. on U = N_i" | HARMLESS SLIP | "U = N_i" is the identification ι. λ_i(g,+) means "accept g". The conclusion (R1)+(R2)+(LF) on all of U is correct. |
| N24 | l. 175–197 | window (Z∖F) ∩ {\|g\|<r}; (UN) on U_+∖F | CORRECT | |
| N25 | l. 14–30 | ν_i ≥ 0 on U; ψ_i = ∫_U 1_{E_i(X)}ρ_i; B_q, Z_q ⊆ U | CORRECT | |
| N25 | l. 223 | V(t) = ∫_U Σ_{g_i>0} t_iρ_i − ∫_U [t·c]₊ | CORRECT | |
| N25 | l. 488–495 (Lemma 7.1) | "Coherent models agree on unanimous problems (they accept every g ≫ 0, and g ≪ 0 ∉ U)"; worsened model on S_M ⊆ U | CORRECT | Both orientations of the unanimous pair are addressed. |
| N25 | l. 599–601 (Lemma 8.1) | "(IB) with A := (S △ S′) ∪ −(S △ S′) … contexts lie in A^c because … −(G ∪ G′) ∩ U = ∅" | CORRECT | A model case of the right handling. Confirmed in N25_referee l. 49. |
| N26 | l. 98–110 (§1.1) | "Problems are g with g₁ > 0 … The menu is {+,0} on unanimous g and on mixed g with r < ½, and {−,0} on mixed g with r > ½. A model is a triple: A ⊆ {r<½}, B ⊆ {r>½} (accept −g), W" | CORRECT | Every pair meets U here (U ∪ −U is a.e. all of ℝ²). Pairs with r > ½ have U-orientation −g with first coordinate −g₁ < 0, and they are handled through B. Error weights on the − side are "acceptance of −g errs at 1, silence errs at 2", which is X △ (U ∩ {h_i>0}) on h = −g. Verified (A3, A4 below). |
| N26 | l. 112–120 | ψ-Bayes: "accept −g on the − side iff p < θ₋(r)" | CORRECT | Recomputed from E_i: cost pρ₁ (accept) vs (1−p)ρ₂ (silence). |
| N26 | l. 210–214 | "∂D_T ∖ 0 consists of the rays r = 0.25 (orientation g ∈ U) and r = 0.625 (orientation −g ∈ U)" | CORRECT | The target's upper endpoint is carried by U ∩ {g₁<0}. |
| N26 | l. 243–244 (§2 notation) | "On M_U a model is X ⊆ U, with two actions per problem (+, 0). c_i(g) := φ_i(g,0) − φ_i(g,+)" | CORRECT | U-orientation indexing. "+" means accept the U-orientation. |
| N26 | l. 276–290 (Lemma 2.3) | "C and C′ agree off the t₀-tie set"; splice on A = D ∩ {\|g\| < R} | CORRECT | C, C′ ⊆ U, so C △ C′ ⊆ Z_{t₀} ⊆ U, and a splice on A ⊆ U equals the splice on A ∪ −A. |
| N26 | §3 (l. 303) | Z_{t₀} := {g : t₀·c(g) = 0} | CORRECT | g ∈ U. |
| N26 scripts | `n26py/warmup.py`, `n26ref_py/check_n26_1.py` | separate bins `rp` (r < ½) and `rm` (r > ½, "accept −g"), error weights r1m/r2m (acceptance errs at 1, silence at 2) | CORRECT | Both orientations. Re-run unchanged: outputs identical to the notes (§3). |
| N26 referee | §1 | "on the − side, accept −g iff p < θ₋"; β_B closed form | CORRECT | |
| N27 | l. 250–252, 266, 273, 311–313, 413–414, 464 | "Every pair with an orientation in U has menu {+,0}"; "For g ∈ U put c(g) := ℓ(g,0) − ℓ(g,+)"; (X_ik) with x ∈ U | CORRECT | U-orientation indexing. |
| R1 | l. 11–13, 80–94 (setting, Prop 2.1) | H-indexing with actions +, 0, −, ×; "Mirror images give {−} and {0,−}"; B_p = {h : p ∈ R(h)} (orientations) | CORRECT | Covers both orientations. On M_U the pairs with −g ∈ U have advice range {0,−}, which is the mirror row. |
| R1 | Lemmas 1.1–1.5 | Lemma 1.4(ii): "a non-null set Z ⊆ ℝⁿ of orientations" | CORRECT | |
| R1 | Props 2.4, 2.5 (l. 124–134) | "Av = set of orientations whose acceptance is in the menu"; "B_p ∩ U′ ≈ D_{conv(K_p ∪ K′)} … charts of h ∈ U′ unchanged" | CORRECT | Orientation-based. |
| R1 | l. 209–211 (Lemma 3.5) | "for g ∈ U′, −g ∉ B_q" | CORRECT | |
| R2, R7 | R2 l. 11, R7 l. 6 | "r(g) = −g₂/(g₁−g₂) on mixed problems (g₁ > 0 > g₂). D_[α,β] gives + if r < α, 0 …, − if r > β" | CORRECT | General domains with advice − available. No U-domain is involved. |
| R11 | l. 89–110 (Lemma IC) | "X △ T ⊆ V′ ∪ (−V′ ∩ T) ⊆ N" | CORRECT | Both orientations are explicitly tracked. |
| R11 | l. 152–230 (Lemma K, Thm W) | general decomposable domain; splice on Z ∩ {\|g\| < 1} | CORRECT | Nothing specific to M_U. |
| CCIBU.tex | l. 27–34 | L_i(X) = ∫_H ℓ_i(g, a_X(g)) dμ on a general domain | CORRECT | H-indexed with full advice; no U-domain. |

---

## 2. Sentences in the write-up to reword

No sentence is false under the correct reading. The following are the only places where the text either says, or could
be read as saying, something about "f ∉ U" or about U ∩ H. Suggested rewordings change no mathematics.

1. **l. 213** (bullet), "For $f$ with $f,-f\notin U$, every evaluated $D$ has $f,-f\notin D$ …". Correct already.
   For emphasis, write "For $f$ with $f\notin U$ **and** $-f\notin U$ …".
2. **l. 215**, "Only the vector $c(g)=\ell(g,0)-\ell(g,+)$, $g\in U$, enters comparisons between evaluable models (on
   every other problem all evaluable models give the same advice, so its penalty drops out)". Replace the parenthesis
   with: "(on every pair $\{f,-f\}$ with $f\notin U$ and $-f\notin U$ all evaluable models give no advice, so its
   penalty drops out; a pair with $-f\in U$ is not of this kind, and it enters through its orientation $-f\in U$)".
   Add after the displayed formula for $c$: "here $\ell(g,+)$ denotes the penalty for accepting $g$; for $g\in U$ with
   $g_1<0$ this is the advice $-$ at the $H$-representative $-g$".
3. **l. 215**, "The problems of the last kind remain decision problems …". Correct ("last kind" = f ∉ U and −f ∉ U).
   Optionally: "The problems with $f\notin U$ and $-f\notin U$ remain decision problems …".
4. **l. 239**, "On $\M_U$ the canonical encoding is the error indicator $\Lambda_iX=1_{E_i(X)}$ with
   $E_i(X)\coloneqq X\sd(U\cap\{h_i>0\})$." Add: "(a function on $U$, transported to $H$ by the measure-preserving
   bijection $g\mapsto\operatorname{sign}(g_1)\,g$ from $U$ onto the pairs meeting $U$; it vanishes on pairs with
   $f\notin U$ and $-f\notin U$)".
5. **l. 810**, "Let $N_i$ be the set of problems whose advice range has at least two elements …". Optionally add: "(on
   $\M_U$: the pairs $\{f,-f\}$ with $f\in U$ or $-f\in U$, not only those whose $H$-representative lies in $U$)".
6. **l. 852**, "the vector $c_i\coloneqq\rho_{P_i}(\lambda_i(\cdot,0)-\lambda_i(\cdot,+))$". Reword to: "the vector
   $c_i(g)\coloneqq\rho_{P_i}(\bar g)\bigl(\lambda_i(\bar g,0)-\lambda_i(\bar g,a_g)\bigr)$, $g\in U$, where $\bar g$
   is the $H$-representative of the pair of $g$ and $a_g\in\{+,-\}$ is the advice 'accept $g$'".
7. **l. 1007** (proof sketch of Thm N26.1), "For mixed $g$ put $r(g)\coloneqq-g_2/(g_1-g_2)$, and take
   $\rho_1=1-\theta(r)$, $\rho_2=\theta(r)$ with $\theta$ nondecreasing and equal to $t_0$ on $r\in[0.2,0.3]$ on one
   side, and strictly increasing on the other." Reword to: "For a mixed pair put $r\coloneqq-g_2/(g_1-g_2)$, which is
   the same for $g$ and $-g$. Pairs with $r<\tfrac12$ have their $U$-orientation in $H$; pairs with $r>\tfrac12$ have
   $U$-orientation $-g$ with negative first coordinate, and evaluable models may accept $-g$ there. Take
   $\rho_1=1-\theta(r)$, $\rho_2=\theta(r)$ on $U$, with $\theta$ nondecreasing on $r<\tfrac12$ and equal to $t_0$ on
   $[0.2,0.3]$, and strictly increasing on $r>\tfrac12$."

Not to be reworded: l. 203 (it concerns single-element advice ranges, not f ∉ U), l. 156, l. 178, l. 210–212, l. 728.

---

## 3. Numerics (`audit_fU_py/`, NUMERICS only)

- `warmup_copy.py` and `check_n26_1_copy.py` (unchanged copies) reproduce the notes' outputs:
  - LP gap ≤ 2.1·10⁻¹⁵;
  - 0/200 and 0/300 undominated incoherent face models;
  - V jumps from 0.8248 to 0.9252;
  - 0 KKM or section failures;
  - target cuts + 0.25, − 0.625.
- `orientation_check.py` (new, independent; output in `orientation_check.out`):
  - A1: in N26.1's setting a.e. pair meets U (0 of 2·10⁶ samples meet neither U nor −U).
  - A2: r(g) = r(−g) exactly. For mixed pairs, r > ½ ⇔ the U-orientation has g₁ < 0 (probabilities 1.000000 and
    0.000000). A quarter of all pairs (0.2498) have U-orientation outside H.
  - A3: ψ_i computed from the definition E_i(X) = X △ (U ∩ {h_i>0}) on Monte Carlo U-orientations agrees with N26's
    two-sided bin formula for six coherent models (max error 9·10⁻⁵, Monte Carlo).
  - A4: the Bayes rule derived from E_i on U-orientations agrees with N26's two-sided rule at 99 weights (0
    mismatches).
  - A5: 62.6% of the target D_[0.25,0.625]'s accepted mixed U-orientations have g₁ < 0. Bookkeeping that kept only
    H ∩ U could not represent β = 0.625.
  - B (T1, ε = 0.3, s = 0.9): μ(U) ≈ 0.351, of which μ(U ∩ {g₁<0}) ≈ 0.086. (−0.1, 1, 1) ∈ U. Facet F₁ has h₁ ≡ −1 in
    the corner-ray normalisation. The box witness A = (−0.442, 0.01, 1) ∈ U has A₁ < 0.

## 4. Summary for the author

- The concern is real in principle: U ∩ {g₁ < 0} is non-null, contains the facet F₁ and the box witness, and in n = 2
  carries the target's upper endpoint.
- No argument in the audited files treats those pairs as outside the domain or common to all models.
- The only repairs are cosmetic: the seven rewordings of §2, and the N14 l. 311 wording.
