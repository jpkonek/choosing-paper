# K3. Classifying failures of adding up: the Yosida–Hewitt route, its exact residual, and what it gives for T1

15 Oct 2026, round 19 (BRIEF16; BRIEF13 rules). Labels: **PROVED** (full proof here, from results the write-up marks
proved, each named), **CHECKED**, **CONJECTURE**, **NUMERICS** (scripts in `k3py/`, run with `python3 -I`; no proof
depends on them). No assumption is added. Setting and notation: write-up §§2–3 (Def. addup, modes M0/M1/M2), N17 §0
(acceptance sets, (NC), (NC⁺)), E1 §2.1 (ends, end-protection, base comparisons), H1 §§1–4 (localizing families,
(E1)/(E2), property (R), Φ, d_t, Lemmas H1.0, H1.1), H2 §1 (R⁰_k, A(W), V(W)), F1 §2 (chain monotonicity).
Blind sets are written Λ (not Z, which H1 uses for tie sets).

---

## 0. Outcome

**The classification asked for ("every world that does not add up is (M1), (E) or (S)") is not proved, and it is
FALSE for systems that satisfy every axiom except closedness of the sections. I did not find a full-system
counterexample either. What is PROVED is the exact form of the classification, with the residual class identified,
plus its consequences for T1.**

1. **Theorem K3.1 (the Yosida–Hewitt classification; PROVED; any n, any K′ ⊆ Δ°, only strict (G) and (IB) at the
   world in question).**
   - Hahn–Banach gives a bounded endorser at every world without a finite certificate.
   - The purely finitely additive part of any endorser is carried by a localizing family D. Off D, its countably
     additive part endorses every relevant comparison **exactly** (part (b)).
   - The route stops at one place: that countably additive part may vanish on a non-null set. Taking the best
     localization gives a canonical **non-localizable blind set** Λ_∞ ⊆ M, and an integrable ρ_∞ ≥ 0, positive
     exactly off Λ_∞, that endorses every comparison localized at a canonical family D̂.
   - (S) with an integrable density holds **iff** Λ_∞ is null. Λ_∞ is characterized by localized ratio certificates
     (part (f)).
   - So every world is (M0), (M1), (S_int) ⊆ (S), or has Λ_∞ ≠ ∅. The residual class is
     (N) := (M2) ∧ ¬(S) ⊆ {Λ_∞ ≠ ∅}.
2. **(E) adds nothing (Prop. K3.2; PROVED).** End-protection alone is vacuous (the empty family qualifies). With a
   base density it implies (S). So the classification is exactly the statement (N) = ∅.
3. **The single obstruction (Theorem K3.3; PROVED).** (N) is non-empty in a two-world system on M_U that satisfies
   every axiom except closed world-1 sections: the tilted world of Q12_referee N3, next to an additive world.
   - Its world 1 is (M2) and totally blind (Λ_∞ = M).
   - For **every** localizing family, no a.e.-finite density endorses its localized comparisons.
   - Hence any proof of the classification must use closedness of sections. By Lemma K3.4 it must use closedness
     against certificates whose positive parts do **not** pairwise meet. Protection by pairwise-meeting targets is
     the mechanism of D2, D2′_A, D2′_B and H2.4, and it is always localizable.
4. **For T1 (n = 3, (H_U)).**
   - **Theorem K3.5 (patch theorem; PROVED).**
     - It unifies H1.2, H1.3 and J1's pattern switching.
     - It extends them to a.e.-finite (σ-finite) densities at **several** worlds, which is case (ii) of BRIEF16. A
       system is excluded as soon as one regular "patch" model is correct deep in every world's localizing family,
       and every density is integrable on the patch's error set.
     - With densities allowed to vanish, the conclusion is property (γ) of the weak field.
   - **Lemma K3.6 (PROVED).** A T1-wrong blow-up of a σ-finite endorser has one of two forms. Either it is
     sheltered inside other worlds' localizing sets, or it is shadowed by a blow-up of a disagreeing, T1-correct
     world on the same set. So case (ii) survives only as sheltering or as infinite "minority mass"
     (Cor. K3.5′(c)).
   - **Theorem K3.7 (PROVED).** Next to two worlds with integrable densities endorsing all their relevant
     comparisons, the third world of a cover is (M1) or (N). In the (N) case:
     - (α) the weak field (ρ_∞σ₁, ρ₂σ₂, ρ₃σ₃) has property (γ);
     - (β) Λ_∞ is **rigid**: Λ_∞ = (E₁(C₁₂) ∩ R₁₂) ∪ (E₁(C₁₃) ∩ R₁₃) for two coherent models C₁₂ "between P₁ and P₂"
       and C₁₃ "between P₁ and P₃". This is D2's blind-set shape on both edge regions. In every open orthant it is a
       convex cone or the complement of one, and a one-parameter family of coherent splices exists;
     - (γ) T1 is admissible for this field at an interior weight, unless Λ_∞ ⊇ E₁(T1) ∩ M.

     So the (M2) part of Conjecture N17.A becomes the **additive** Question Q_A (§6): Theorem M0closed(a) for fields
     with one weakly signed component.
5. **Single open question (Q_K3, §7).** In a full system (every axiom, closed sections for every model), can a world
   have a non-null non-localizable blind set Λ_∞?
   - "No" proves the classification in its strong form (S_int).
   - "Yes, without (S)" is the counterexample, and by K3.7(β) it would have to be D2-shaped on the edge regions to be
     aimed at T1.
   - Next to an additive world in two worlds, Λ_∞ is an initial segment c_{a_∞} of the chain (Prop. K3.8; PROVED).
     The two-world form of Q_K3 there is "a_∞ = 0?" (CONJECTURE K3.C).

| | Statement | Label |
|---|---|---|
| K3.1 | (a) endorsers exist iff (NC); (b) p.f.a. parts localize, CA parts endorse off them; (c) canonical blind set Λ; (d) non-localizable blind set Λ_∞, integrable localized endorser ρ_∞; (e) (S_int) ⇔ Λ_∞ null; (f) ratio-certificate characterization | PROVED |
| K3.2 | (E) is vacuous without a density; (E) with base density ⇒ (S); classification ⇔ (N) = ∅ | PROVED |
| K3.3 | the tilted two-world system: every axiom except closed world-1 sections; world 1 ∈ (N), Λ_∞ = M | PROVED; NUMERICS |
| K3.4 | pairwise-meeting protection is localizable | PROVED |
| K3.5 | patch theorem: (γ) for weak fields; contradiction for strictly positive densities; case (ii) | PROVED |
| K3.5′ | corollaries: H1.2, H1.3, σ-finite versions; residual (R-i) sheltering / (R-ii) infinite minority mass | PROVED |
| K3.6 | T1-wrong σ-finite blow-ups are sheltered or shadowed | PROVED |
| K3.7 | one (N) world next to two integrable worlds: (γ), rigid blind set, admissibility | PROVED; NUMERICS |
| K3.8 | two worlds next to an additive world: every Λ_D is an initial segment of the chain | PROVED |
| K3.C | two worlds next to an additive world, every axiom: a_∞ = 0 | CONJECTURE |
| Q_A, Q_K3 | the two open questions | open |

---

## 1. Setting and definitions

**Standing hypotheses for §§2–4.** n ≥ 2; any credal set K′ ⊆ Δ°; U = D_{K′}; the U-domain M_U; M the mixed part of U,
N₊ its nonnegative part. A ranking on M_U whose world i has strict (G) and (IB). The other worlds and the axioms (S),
(C), (LA) are not used in §2 except to define C_L. E_i(X) = X △ P_i, and "regular" is as in Def. addup.

- **Relevant comparison vectors.** 𝔚 := 𝔚_i := {δ = 1_{E_iX} − 1_{E_iB} : B ∈ C_L, X regular, B ⪯_i X}.
  - Coherent and regular models accept a.e. h ∈ N₊ and are correct there at every world.
  - So every δ ∈ 𝔚 vanishes on N₊. Everything below lives on M.
- **Charges.** ba := bounded finitely additive set functions on the measurable subsets of M that vanish on μ-null
  sets. These are the elements of (L^∞(M, μ))*, by ν(f) = ∫ f dν.
  - **Endorsers:** 𝒩 := {ν ∈ ba : ν ≥ 0, ν(M) = 1, ν(δ) ≥ 0 for all δ ∈ 𝔚}. For a subfamily 𝔊 ⊆ 𝔚, 𝒩(𝔊) is
    defined the same way, and 𝒩(𝔊) ⊇ 𝒩.
  - **Yosida–Hewitt:** every ν ∈ ba with ν ≥ 0 is uniquely ν = ν_c + ν_p.
    - ν_c is countably additive and ≥ 0. It vanishes on null sets because ν_c ≤ ν, so ν_c = ρ_ν μ with
      0 ≤ ρ_ν ∈ L¹(M).
    - ν_p ≥ 0 is purely finitely additive: the only countably additive λ with 0 ≤ λ ≤ ν_p is 0.
    - ν_c is the largest countably additive charge below ν.
- **Modes** (Def. addup). (M0): some ν ∈ 𝒩 with ν(A) > 0 for every non-null A ⊆ M. Adding μ|_{N₊} then gives the
  weight of Def. addup(b). (M1): some finite nonnegative combination of members of 𝔚 is ≤ 0 a.e. and not a.e. 0.
  (M2): neither. (NC_𝔊) means that no finite nonnegative combination of members of 𝔊 is ≤ −1.
- **Localizing families** (H1 §1). A localizing family is a decreasing sequence D = (D_m) of measurable subsets of M
  with μ(D_m) → 0.
  - δ is **D-localized** if δ ≤ 0 a.e. on D_m for some m (hence for all larger m).
  - 𝔚_D := the D-localized members of 𝔚.
  - Write D ≤ D′ if D_m ⊆ D′_m for all m; then 𝔚_{D′} ⊆ 𝔚_D. The union (D ∪ D′)_m := D_m ∪ D′_m is localizing.
- **(S)** (H1.2's hypothesis, the brief's class). For some localizing D and some measurable ρ with 0 < ρ < ∞ a.e. on M,
  ρμ(δ⁻) ≤ ρμ(δ⁺) in [0, ∞] for every δ ∈ 𝔚_D (cancellation reading (E2)).
  - **(S_int):** the same with ρ ∈ L¹(M). For integrable ρ, (E2) is ∫ρδ dμ ≥ 0.
- **(E)** (E1 §2.1). World i is end-protected with a countable family 𝒮 of ends, possibly empty. **(E_b)** adds that
  every base comparison is (E2)-endorsed by some a.e.-finite ρ > 0. A base comparison is a relevant comparison that is
  eventually 0 on every end.
- **(N) := (M2) ∧ ¬(S).**
- **Ratio certificates.** Let 𝔊 ⊆ 𝔚, let B′ ⊆ M be non-null and c > 0. A **c-ratio certificate on B′ from 𝔊** is a
  pair (δ̂, g) with:
  - δ̂ a finite nonnegative combination of members of 𝔊;
  - g ∈ L^∞, g ≥ 0, supported in B′, ∫ g dμ = 1;
  - δ̂ ≤ c − g a.e. on M.

  In words, the combination removes one unit of μ-mass from B′ (spread as g), while its positive excess is uniformly
  at most c. D2's certificate Σ w_g g_* ≤ ε − 1_{c_a} is one, with g = 1_{c_a}/μ(c_a) and c = ε/μ(c_a).

---

## 2. The Yosida–Hewitt classification

**Theorem K3.1 (PROVED).** Under the standing hypotheses:

- **(a)** 𝒩 ≠ ∅ iff (NC_𝔚). In particular 𝒩 ≠ ∅ in modes (M0) and (M2), and 𝒩(𝔚_D) ⊇ 𝒩 ≠ ∅ for every D.
- **(b) Localization.** Let 𝔊 ⊆ 𝔚 and ν ∈ 𝒩(𝔊), ν = ρ_ν μ + ν_p. There is a localizing family D^ν with
  ν_p(M ∖ D^ν_m) ≤ 2^{−m}. For every D^ν-localized δ ∈ 𝔊, ∫ ρ_ν δ dμ ≥ 0.
- **(c) Blind set.** There is ν* ∈ 𝒩 with the following property. The set Λ := M ∖ {ρ_{ν*} > 0}, unique mod null,
  satisfies ρ_ν = 0 a.e. on Λ for every ν ∈ 𝒩: every endorser is purely finitely additive on Λ. World i adds up
  iff Λ is null. In mode (M2), Λ is non-null.
- **(d) Non-localizable blind set.** For each localizing D let Λ_D be the set of (c) for the family 𝔚_D.
  - D ↦ Λ_D is antitone, and Λ_D ⊆ Λ.
  - Λ_∞ := ess inf_D Λ_D equals Λ_{D^∞} for some localizing D^∞.
  - There are a localizing D̂ ≥ D^∞ and ρ_∞ ∈ L¹(M), ρ_∞ ≥ 0, with {ρ_∞ > 0} = M ∖ Λ_∞ a.e. and Λ_{D̂} = Λ_∞, such
    that ∫ ρ_∞ δ dμ ≥ 0 for every δ ∈ 𝔚_{D̂}.
- **(e)** (S_int) ⇔ Λ_∞ is null. In particular (S_int) ⇒ (S), and (N) ⊆ {Λ_∞ non-null}.
- **(f) Certificates.** Assume (NC_𝔚). For a non-null B ⊆ M and a localizing D, the following are equivalent:
  - (i) B ⊆ Λ_D (mod null);
  - (ii) for every non-null B′ ⊆ B and every c > 0 there is a c-ratio certificate on B′ from 𝔚_D.

  Hence B ⊆ Λ_∞ iff (ii) holds for every localizing D.

*Proof.*

- **(a)** This is N17.1(c) (IRC Thm NC(a)), on M. Directly: let 𝒦 := cone(𝔚) + L^∞_+.
  - If (NC_𝔚) holds, then −1 is not in the sup-norm closure of 𝒦. Otherwise some combination is ≤ −1 + η with
    η < 1, and rescaling gives one ≤ −1.
  - Hahn–Banach separates −1 from the closed convex cone cl 𝒦: some φ ∈ (L^∞)* has φ ≥ 0 on 𝒦 and φ(1) > 0. So
    φ ≥ 0 on L^∞_+ and on 𝔚, and φ/φ(1) ∈ 𝒩.
  - Conversely, ν ∈ 𝒩 gives ν(Σλδ) ≥ 0 > −1 = ν(−1).
- **(b)** Write π := ν_p.
  - *Step 1: for every ε > 0 there is a measurable E with μ(E) < ε and π(M ∖ E) < ε.* Put
    λ(A) := inf{π(B) + μ(A ∖ B) : B ⊆ A measurable}. This is the lattice infimum π ∧ μ in ba, a charge with
    0 ≤ λ ≤ π and λ ≤ μ. If A_n ↓ ∅, then λ(A_n) ≤ μ(A_n) → 0, so λ is countably additive. Since π is purely
    finitely additive, λ = 0. So inf_B (π(B) + μ(M ∖ B)) = 0; take E := M ∖ B for a B with π(B) + μ(M ∖ B) < ε.
  - *Step 2.* Choose E_k with μ(E_k) < 2^{−k} and π(M ∖ E_k) < 2^{−k}. Put D^ν_m := ⋃_{k≥m} E_k. Then D^ν is
    decreasing, μ(D^ν_m) < 2^{1−m}, and π(M ∖ D^ν_m) ≤ π(M ∖ E_m) < 2^{−m}.
  - *Step 3.* Let δ ∈ 𝔊 with δ ≤ 0 a.e. on D^ν_m, and let m′ ≥ m. Then δ ≤ 0 on D^ν_{m′}, and
    0 ≤ ν(δ) = ∫ρ_ν δ dμ + π(δ 1_{D^ν_{m′}}) + π(δ 1_{M∖D^ν_{m′}}) ≤ ∫ρ_ν δ dμ + 0 + 2^{−m′}.
    Letting m′ → ∞ gives ∫ρ_ν δ ≥ 0. ∎(b)
- **(c)**
  - *Two facts.*
    - (F1) A positive charge π is purely finitely additive iff Step 1 of (b) holds for it. "Only if" is Step 1.
      "If": a countably additive λ with 0 ≤ λ ≤ π vanishes on null sets, so λ = fμ. Then
      λ(M) ≤ λ(E) + π(M ∖ E) ≤ ∫_E f dμ + ε → 0 as ε → 0.
    - (F2) If ν_k ∈ 𝒩, then ν := Σ_k 2^{−k}ν_k ∈ 𝒩 (norm convergence; 𝒩 is convex and norm-closed), and
      ρ_ν = Σ 2^{−k}ρ_{ν_k}. Indeed Σ2^{−k}ρ_{ν_k}μ is countably additive. The remainder Σ2^{−k}(ν_k)_p is purely
      finitely additive by (F1): truncate the series at K with tail < ε/2, and use E := ⋃_{k≤K}E_k with
      μ(E_k) < ε/(2K) and (ν_k)_p(M ∖ E_k) < ε/2. Uniqueness of the decomposition gives the claim.
  - By (F2) the family {ρ_ν > 0}, ν ∈ 𝒩, is closed under countable unions mod null. μ(M) < ∞, so it has a largest
    element, attained by some ν*. If some ν ∈ 𝒩 had ρ_ν > 0 on a non-null part of Λ, then (ν + ν*)/2 would have a
    larger support.
  - If Λ is null, ν* + μ|_{N₊}, normalized, is positive on non-null subsets of U and endorses 𝔚 (which lives on
    M). So the world adds up.
  - Conversely, let ν be a strictly positive endorsing weight, and suppose ρ_ν = 0 on a non-null Y ⊆ M (this is N19
    Lemma R1). By Step 1 choose E_k with μ(E_k) < 2^{−k−1}μ(Y) and ν_p(M ∖ E_k) < 1/k. Then
    Y′ := Y ∖ ⋃_k E_k has μ(Y′) ≥ μ(Y)/2, and ν(Y′) = ν_p(Y′) < 1/k for all k. So ν(Y′) = 0, a contradiction.
  - In (M2) the world does not add up, so Λ is non-null.
- **(d)**
  - *Antitone.* D ≤ D′ ⇒ 𝔚_{D′} ⊆ 𝔚_D ⇒ 𝒩(𝔚_D) ⊆ 𝒩(𝔚_{D′}) ⇒ Λ_{D′} ⊆ Λ_D. Also 𝔚_D ⊆ 𝔚 gives Λ_D ⊆ Λ.
  - *Ess inf.* The family {Λ_D} is downward directed, since Λ_{D∪D′} ⊆ Λ_D ∩ Λ_{D′}. Its essential infimum is the
    intersection of a countable subfamily Λ_{D^{(k)}}.
  - *D^∞.* Choose j_k with μ(D^{(k)}_{j_k}) < 2^{−k}, and put D^∞_m := ⋃_k D^{(k)}_{m+j_k}. It is decreasing, and
    μ(D^∞_m) ≤ Σ_k μ(D^{(k)}_{m+j_k}) → 0 by dominated convergence (terms ≤ 2^{−k}). A D^∞-localized δ is
    D^{(k)}-localized for every k, so Λ_{D^∞} ⊆ Λ_{D^{(k)}} for every k, hence Λ_{D^∞} ⊆ Λ_∞. The reverse inclusion
    is the definition of Λ_∞.
  - *ρ_∞.* Apply (c) to 𝔚_{D^∞}: ν*_∞ with support M ∖ Λ_∞. Apply (b) to ν*_∞ and 𝔊 = 𝔚_{D^∞}: a family D′.
    Put D̂ := D^∞ ∪ D′ and ρ_∞ := ρ_{ν*_∞}. A D̂-localized δ ∈ 𝔚 lies in 𝔚_{D^∞} and is D′-localized, so
    ∫ρ_∞δ ≥ 0. Finally Λ_∞ ⊆ Λ_{D̂} ⊆ Λ_{D^∞} = Λ_∞.
- **(e)**
  - ⇒: an integrable ρ > 0 endorsing 𝔚_D gives ρμ/‖ρ‖₁ ∈ 𝒩(𝔚_D) with full support, so Λ_D is null and hence
    Λ_∞ is null.
  - ⇐: by (d) with ρ_∞ > 0 a.e.
- **(f)**
  - *Rates.* For ν ∈ ba₊: ν ≥ cμ|_{B′} as charges iff ρ_ν ≥ c a.e. on B′. (⇐ is trivial. ⇒: cμ|_{B′} is countably
    additive and ≤ ν, hence ≤ ν_c.)
  - So (i) holds iff there is no triple (B′ ⊆ B non-null, c > 0, ν ∈ 𝒩(𝔚_D)) with ν ≥ cμ|_{B′}. If B ⊄ Λ_D, some
    ν has ρ_ν > 0 on a non-null part of B, hence ρ_ν ≥ c on some non-null B′ ⊆ B.
  - *Duality.* Fix B′ and c. Put 𝒦′ := {δ̂ + f − cμ(f1_{B′}) + h : δ̂ ∈ cone 𝔚_D; f, h ∈ L^∞_+}, a convex cone.
    - An element ν ∈ (L^∞)* with ν(1) = 1 and ν ≥ 0 on 𝒦′ is exactly a member of 𝒩(𝔚_D) with ν ≥ cμ|_{B′}.
    - As in (a), such ν exists iff −1 ∉ cl 𝒦′.
    - −1 ∈ cl 𝒦′ iff for every η > 0 there are δ̂ and f ≥ 0 with δ̂ + f − cμ(f1_{B′}) ≤ −1 + η.
  - *(i) ⇒ (ii).* Take η < 1 and δ̂, f as above, and put s := μ(f1_{B′}).
    - If cs < 1 − η, then δ̂ ≤ −(1 − η − cs) < 0 uniformly. This contradicts (NC_{𝔚_D}), which follows from
      (NC_𝔚).
    - So s > 0. Put g := f1_{B′}/s. Then δ̂/s ≤ −f/s + c − (1 − η)/s ≤ c − g, a c-ratio certificate.
  - *(ii) ⇒ (i).* Given B′ and c, take a (c/2)-ratio certificate (δ̂, g). Every ν ∈ 𝒩(𝔚_D) with ν ≥ cμ|_{B′}
    would give 0 ≤ ν(δ̂) ≤ c/2 − ν(g) ≤ c/2 − c∫g dμ = −c/2.
  - The last sentence of (f) follows from (d): B ⊆ Λ_∞ iff B ⊆ Λ_D for every D. ∎

*Reading.*
- The natural route of the brief gives exactly (b): a purely finitely additive part always concentrates on small
  sets, and the countably additive part always endorses off them.
- The route fails at one point only: ρ_ν may vanish on a non-null set.
  - In D2 it does, with Λ = c_a. Localizing at the end of the chain repairs this: there Λ_D = ∅ and λ endorses, so
    D2 is (S_int).
  - In the tilted world (K3.3) the zero set is all of M, and no localization repairs it.
- The canonical objects are Λ_∞ (where no localized endorser has a countably additive part) and ρ_∞ (an integrable
  endorser off the canonical carrier D̂ of the purely finitely additive parts).

---

## 3. End-protection adds nothing

**Proposition K3.2 (PROVED).**
- **(a)** Every world is end-protected with the empty family 𝒮 = ∅. E1 §2.1, E1.5 and H2.3 allow empty families, and
  the second clause holds vacuously. Then every relevant comparison is a base comparison.
- **(b)** If world i is (E_b) with a countable family 𝒮, then it is (S). It is (S_int) if the base endorser is
  integrable.
- **(c)** Consequently "every world that does not add up is (M1), (E_b) or (S)" is equivalent to (N) = ∅.

*Proof.*
- (a) is by the definition.
- (b) (H1 §1). Choose depths a_S(m) ↑ ∞ with Σ_S μ(S_{a_S(m)}) → 0, and put D_m := ⋃_S S_{a_S(m)}.
  - A D-localized δ is ≤ 0 on S_{a_S(m)}, so it is S-positive for no S.
  - End-protection makes it eventually ≥ 0 on every S, hence eventually 0, so it is a base comparison and is
    endorsed.
- (c) (E_b) ⊆ (S) by (b). Worlds that add up are excluded from the statement. ∎

So the meaningful content of (E) is the base density, and the classification is the single statement "(M2) ⇒ (S)".

---

## 4. The residual class (N)

### 4.1 (N) is consistent with every axiom except closed sections

**The tilted system.**
- *Setting.* n = 2 and the Q12 setting (write-up §8.5(e)): K′ = [k₁, k₂] ⊆ (0,1), the C2.1/Q1 path C_b (b ∈ [0,1]),
  c_b = E₁C_b ∩ M with λ̄(c_b) = b, and the chain coordinate x on M. Here λ̄ = μ/μ(M), x pushes λ̄|_M to Lebesgue
  measure on [0,1), and x := 2 on N₊.
- World 2 is additive: X ⪯₂ Y iff λ̄(E₂X) ≤ λ̄(E₂Y).
- World 1 (Q12_referee N3): X ⪯₁ Y iff δ := 1_{E₁Y} − 1_{E₁X} ∈ 𝒜_tilt, where δ ∈ 𝒜_tilt iff, for some κ > 0,
  T^κ_δ(y) := ∫_{x(h)≥y} e^{κx(h)} δ dλ̄ ≥ 0 for every y ∈ [0, 2].
- Selection p ↦ C_{p₂}.

**Theorem K3.3 (PROVED).**
- **(a)** The tilted system satisfies strict (G) and (IB) at both worlds, (LA), competitiveness of every C_b on its
  support (indeed (K) for every model), (C), C_L = U_L = {C_b}, (LF) at every interior C_b, and closed world-2
  sections for every model. The world-1 sections are not closed.
- **(b)** World 1 is in mode (M2) and its non-localizable blind set is Λ_∞ = M.
- **(c)** World 1 is not (S): for every localizing D and every measurable ρ with 0 < ρ < ∞ a.e., some accepted, relevant,
  D-localized comparison has ρ(δ⁻) > ρ(δ⁺). It is not (E_b) and does not add up. So world 1 ∈ (N).

*Proof.*

- **(a)**
  - *World 1 is a ranking.*
    - For κ < κ′, the κ-cone lies inside the κ′-cone. If T^κ_δ ≥ 0 on [0,2] and ψ ≥ 0 is nondecreasing, then
      ∫_{x≥y} ψ e^{κx} δ = ψ(y)T^κ_δ(y) + ∫_{(y,2]} T^κ_δ dψ ≥ 0 (Stieltjes integration by parts on [0,2]); take
      ψ = e^{(κ′−κ)x}.
    - So 𝒜_tilt is an increasing union of convex cones, hence a convex cone. It is closed under ternary sums.
    - It contains every δ ≥ 0.
    - It contains no δ ≤ 0 with δ ≠ 0: T^κ_δ(0) = ∫ e^{κx}δ ≥ 0 forces δ = 0.
    - Lemma vectorform then gives a preorder with strict (G) and (IB).
  - *World 2* is additive with density, so strict (G) and (IB) hold.
  - *Notation.* For a model X put A := E₁X ∩ M and N := N₊ ∖ X. For a cut b put P := c_b ∖ A and Q := A ∖ c_b.
    The world-1 vector is δ₁ = 1_Q − 1_P + 1_N, and the world-2 vector is δ₂ = 1_P − 1_Q + 1_N.
  - *(K) for every model.*
    - If Q ∪ N is non-null, take y₀ with λ̄((Q ∪ N) ∩ {x ≥ y₀}) > 0 and y₀ > b (possible since Q ⊆ {x ≥ b} a.e.
      and {x = b} is null).
    - For y ≥ b, the tail T^κ_{δ₁}(y) is ≥ 0. For y < b,
      T^κ_{δ₁}(y) ≥ e^{κy₀} λ̄((Q ∪ N) ∩ {x ≥ y₀}) − e^{κb} λ̄(P) > 0 for κ large.
    - So C_b ⪯₁ X. If Q ∪ N is null, δ₂ = 1_P ≥ 0 and C_b ⪯₂ X.
    - At the vertices, C₀ = P₁ and C₁ = P₂ are handled by (G).
  - *No weak domination of C_b.* Suppose X ⪯₁ C_b and X ⪯₂ C_b.
    - The world-1 vector is −δ₁. Its tail at y = b is −∫_{x≥b} e^{κx}(1_Q + 1_N) ≥ 0 only if Q and N are null.
    - Then the world-2 vector −δ₂ = −1_P is accepted only if P is null. So X = C_b.
  - *Every other model is strictly dominated.* Put b₂ := min(1, max(0, λ̄(A) − λ̄(N))), the Q12_referee repair.
    - World 2: C_{b₂} ⪯₂ X, since λ̄(d_{b₂}) ≤ λ̄(M ∖ A) + λ̄(N).
    - World 1: the vector of C_{b₂} ⪯₁ X lies in the band (the κ → 0 limit, contained in every κ-cone). Its tails are
      ≥ 0 for y ≥ b₂, and for y < b₂ they are ≥ λ̄(A) − b₂ + λ̄(N) ≥ 0.
    - By the previous item, X ≠ C_{b₂} is not tied with C_{b₂} at both worlds, so it is strictly dominated.
    - Hence U_L = C_L = {C_b}, and (C) and (LA) hold.
  - *Other axioms.*
    - (LF) at interior C_b is C2.1(4).
    - World-2 sections {b : λ̄(d_b) ≤ λ̄(M ∖ A) + λ̄(N)} are closed.
    - World-1 sections are not closed: for Z ⊆ c_{x−η} non-null, S₁(c_x ∖ Z) = [0, x) (Q12_referee N3).
- **(b)**
  - *(M2).* The world-1 error sets c_b of C_L form a chain, so (NC⁺) holds on 𝔚 (N17 Lemma 3.1), and there is no
    finite certificate.
  - *Every bounded endorser vanishes on every c_b, b < 1.*
    - For every non-null Q ⊆ d_b, the relevant comparison C_b ⪯₁ X with E₁X = Q (X regular) is accepted by the
      (K)-argument above.
    - So ν(c_b) ≤ ν(Q). Taking disjoint non-null Q_n ⊆ d_b, ν(Q_n) → 0, so ν(c_b) = 0.
    - Hence Λ = M.
  - *Localized version.* Fix a localizing D and b ∈ (0,1). Take m with μ(D_m) < μ(d_b)/2.
    - Every non-null Q ⊆ d_b ∖ D_m gives a D-localized comparison of the same kind.
    - Disjoint such Q_n show that every ν ∈ 𝒩(𝔚_D) vanishes on c_b. So Λ_D = M for every D, and Λ_∞ = M.
- **(c)**
  - Let D and ρ be given. Fix b ∈ (0,1) and a non-null P ⊆ c_b with 0 < ρ(P) < ∞.
  - Choose m with μ(D_m) < μ(d_b)/2. Since ρ < ∞ a.e., some non-null Q ⊆ (d_b ∖ D_m) ∩ {ρ ≤ n} has
    ρ(Q) ≤ nμ(Q) < ρ(P).
  - The comparison C_b ⪯₁ X with E₁X = (c_b ∖ P) ∪ Q is accepted, relevant and D-localized (δ⁺ = Q misses D_m),
    and ρ(δ⁻) = ρ(P) > ρ(Q) = ρ(δ⁺).
  - Not (E_b), by K3.2(b). Not (M0), by (b). ∎

NUMERICS (`k3py/tilted_nonS.py`, `.out`; exact piecewise-constant data, 60-digit arithmetic):
- 300/300 cut pairs with targets of measure 10⁻⁴–10⁻² are accepted for some κ;
- for 200 random positive step densities ρ and random localizing sets of measure 0.05, an accepted, D-localized
  cut pair with ρ(P) > ρ(Q) is found every time;
- the section of c_{0.7} ∖ [0.4, 0.5) contains b = 0.6999 but not b = 0.7.

*Reading.* K3.3 is the obstruction to the classification as a theorem of the axioms other than closedness.
- Strict (G), (IB), (K) and competitiveness, (C), (LA), (LF), undominatedness, and closedness at the other world all
  hold, and world 1 is in (N).
- So **any proof that (M2) ⇒ (S) must use closed sections at the failing world.**
- Lemma DL (P4B_referee §8.1) is exactly what kills the tilted world. It is a two-world nested-chain lemma.

### 4.2 Pairwise-meeting protection is always localizable

**Lemma K3.4 (PROVED).** Let 𝔉 ⊆ 𝔚 be a family such that, for all δ, δ′ ∈ 𝔉, μ(δ⁺ ∩ δ′⁺) > 0, and
inf_{δ∈𝔉} μ(δ⁺) = 0.
- **(a)** There is a localizing T such that no member of 𝔉 is T-localized.
- **(b)** If moreover some a.e.-finite ρ > 0 (resp. integrable) and a localizing D satisfy: ρ endorses every
  D-localized member of 𝔚 ∖ 𝔉, then world i is (S) (resp. (S_int)), with localizing family D ∪ T.

*Proof.*
- (a) Pick δ_k ∈ 𝔉 with μ(δ_k⁺) < 2^{−k}, and put T_m := ⋃_{k≥m} δ_k⁺, so μ(T_m) < 2^{1−m}. Every δ ∈ 𝔉 meets
  δ_k⁺ non-nully for every k (for δ = δ_k trivially), so δ⁺ ∩ T_m is non-null for every m.
- (b) A (D ∪ T)-localized δ is D-localized and, by (a), not in 𝔉. ∎

*Consequences.*
- In D2, D2′_A, D2′_B and H2.4, the exotic comparisons are δ ≥ 1_{Q_g} near the protected end, with pairwise
  meeting targets ((D2), (D2′)). Their bases are endorsed by λ̄ or by a heavy integrable density (E1.6). So all of
  them are (S_int), by K3.4 (or directly, localizing at the end).
- The Q12 worlds (not full systems) have pairwise disjoint targets, so K3.4 does not apply to them. They are still
  (S_int), by localizing at the end: a δ ∈ 𝒢(F) has τ_δ ≥ τ_{g_F} > 0 near x = 1, so no member of 𝒢(F) is ≤ 0 near
  1, and the localized comparisons are band comparisons, which λ̄ endorses.
- More generally, in an (N) world the failure survives the deletion of any pairwise-meeting family with small
  members. By K3.1(f), for **every** localizing D there must be ratio certificates from D-localized comparisons on
  every non-null B′ ⊆ Λ_∞. Their positive parts therefore avoid any prescribed set of small measure.
- Such positive parts cannot all be drawn from one intersecting family. So an (N) world must accept comparisons
  with many pairwise disjoint small targets. Their sums are then accepted by sum closure, and this is the
  configuration that closedness penalizes in every case examined (Prop. Q13, Lemma DL). No theorem is claimed.

### 4.3 Two worlds next to an additive world

**Proposition K3.8 (PROVED).** In the setting of F1.2 (n = 2; strict (G), (IB), (LA), (S), (C); world 2 additive with
integrable density w > 0; nested selection; chain c_b; uniform coordinate x), take any localizing D and any
ν ∈ 𝒩(𝔚_D) at world 1. Then ρ := dν_c/d(wμ) equals φ∘x a.e. on M for some nondecreasing φ: [0,1) → [0, ∞). Hence
every Λ_D, and Λ_∞, is an initial segment c_a of the chain (mod null). Write Λ_∞ = c_{a_∞}. World 1 is (S_int) iff
a_∞ = 0.

*Proof.*
- By K3.1(b) applied to 𝔚_D, ρ wμ endorses exactly every (D ∪ D′)-localized relevant comparison, for some D′. Put
  D″ := D ∪ D′.
- Fix b ∈ (0,1) and c₁ < c₂ with c₁(1+ε) < c₂. Suppose c_b ∩ {ρ > c₂} and (d_b ∖ D″_m) ∩ {ρ < c₁} are both non-null.
  - Choose P, Q in them with wμ(Q) = (1+ε) wμ(P).
  - (K) at b gives C_b ⪯₁ X with E₁X = (c_b ∖ P) ∪ Q, as in F1.2. This comparison is relevant and D″-localized,
    since Q misses D″_m.
  - So ρwμ(Q) ≥ ρwμ(P), against c₁(1+ε) wμ(P) > ρwμ(Q) and ρwμ(P) ≥ c₂ wμ(P).
- Hence ess sup_{c_b} ρ ≤ ess inf_{d_b ∖ D″_m} ρ for every m. The right side decreases to ess inf_{d_b} ρ as m → ∞,
  because ⋂_m D″_m is null.
- The rest is F1.2(b) verbatim, with ρ ≥ 0 in place of ρ > 0: F(b) := ess inf_{d_b} ρ is nondecreasing, and
  ρ = F(x⁺) a.e. So {ρ > 0} is a final segment of the chain.
- The maximal support over 𝒩(𝔚_D) is a union of final segments, hence a final segment. ∎

- In D2, a_∞ = 0. In the tilted world, a_∞ = 1.
- **CONJECTURE K3.C.** Under every axiom (closed sections at both worlds), a_∞ = 0, i.e. world 1 is (S_int).
- *Evidence.*
  - By K3.1(f), a_∞ > 0 means that, for the end family D_m = d_{1−2^{−m}}, there are c-ratio certificates on every
    B′ ⊆ c_{a_∞} whose comparisons all lie in one c_t, t < 1.
  - F1.4 (PROVED) excludes every such certificate that is **chain-free**, i.e. of the form Σw1_P ≥ 1_S with
    Σw ν₂(Q) small.
  - The gap is chained certificates, in which targets of some comparisons are partly sources of others. The rounding
    of F1.4 does not handle partial overlaps.

---

## 5. T1: several worlds and σ-finite endorsers (case (ii) of BRIEF16)

From here on, n = 3, ε ∈ (0,1), K′ = u + s(T1 − u), and (H_U) holds. For measurable ρ_k ≥ 0 that are finite a.e., set
ρ_k := 1 on N₊ (this is irrelevant for relevant comparisons), c := (ρ_kσ_k)_k, B_t := {t·c > 0} and
Z_t := {t·c = 0}. Φ and d_t are as in H1 §2. **Property (γ)** means that B_t is coherent (mod null) for a.e. t ∈ Δ°.

**Theorem K3.5 (patch theorem; PROVED).** Suppose that for each world k there are a measurable ρ_k: U → [0, ∞), finite
a.e., and a localizing family D^k, and that there is a regular model Y° (the **patch**) such that:
- **(P1)** ρ_kμ endorses (E2) every relevant world-k comparison whose vector is ≤ 0 a.e. on D^k_m ∖ E_k(Y°) for some m;
- **(P2)** ∫_{E_k(Y°)} ρ_k dμ < ∞ for every k;
- **(P3)** c ≠ 0 a.e. on M.

Then c has property (γ). If moreover ρ_k > 0 a.e. for every k, then (H_U) is contradictory.

*Proof.*
- **Setup.** Put D_m := M ∩ ⋃_k (D^k_m ∪ {ρ_k > m}), a localizing family. Off D_m every ρ_k is ≤ m.
- **Step 1: if (γ) fails, there is a contradiction.**
  - By (P3) and Tonelli, Z_t is null for a.e. t ({t : t·c(g) = 0} is a line for every g with c(g) ≠ 0). So if
    (γ) fails, some t ∈ Δ° has Z_t null and B_t incoherent.
  - Let X_m := B_t on U ∖ D_m and Y° on D_m. X_m is regular, because Y° is regular and B_t ⊇ N₊.
  - *Finite costs.* E_kX_m ⊆ (E_kB_t ∖ D_m) ∪ (E_k(Y°) ∩ D_m). The first part has ρ_k-mass ≤ mμ(M), the second
    finite mass by (P2).
  - *Small Φ.* On X_m △ B_t ⊆ D_m we have |t·c| ≤ Σ_{k : X_m errs at k} t_kρ_k (H12_referee §1.2), and there X_m errs
    at k iff g ∈ E_k(Y°). So Φ(X_m) ≤ Σ_k t_k ∫_{D_m ∩ E_k(Y°)} ρ_k → 0, by (P2) and absolute continuity.
  - *Dominators.* Theorem kkm gives a coherent selected C_m with C_m ⪯_k X_m at every k. All three comparisons are
    relevant.
    - At world k the vector δ_k = 1_{E_kX_m} − 1_{E_kC_m} is ≤ 0 off E_kX_m, in particular on
      D^k_m ∖ E_k(Y°) ⊆ D_m ∖ E_kX_m.
    - So (P1) applies, and by property (R), ρ_k(E_kC_m) ≤ ρ_k(E_kX_m) < ∞.
  - *Contradiction.*
    - Lemma H1.0(b) uses only the pointwise identity Σ_k t_kρ_k(1_{E_kY} − 1_{E_kY′}) = (1_{Y′} − 1_Y)·t·c and
      finiteness, so it holds for ρ_k ≥ 0. With the H12_referee bound Φ(Y) ≤ Σ_k t_kρ_k(E_kY), it gives
      Φ(C_m) ≤ Φ(X_m).
    - Lemma H1.0(a) uses only null ties, so it gives Φ(C_m) ≥ d_t > 0.
    - This is a contradiction once Φ(X_m) < d_t.
- **Step 2: strictly positive densities.**
  - Lemma H1.1 applies with D. Every ρ_k is integrable on M ∖ D_m, and a comparison T1 ⪯_k Y with Y regular and
    Y = T1 on D_m has δ = 0 on D_m, so it is endorsed by (P1). Its steps 1–3 use only these facts, and its step 4
    (interior) uses ρ_k > 0. So T1 is admissible at some p* ∈ Δ°.
  - c is strictly signed, so Theorem M0closed(a) (which uses no integrability) says that (γ) fails. This
    contradicts Step 1. ∎

**Corollary K3.5′ (PROVED).** Assume (H_U).
- **(a) (H1.2).** Take Y° := P₁ and D² = D³ = ∅, so (P1) at worlds 2 and 3 asks for endorsement of every relevant
  comparison. Then (P2) holds if ρ₂, ρ₃ are integrable (E₁(P₁) = ∅). This recovers H1.2, with ρ₁ only a.e.-finite.
- **(b) (H1.3, σ-finite form).** Take Y° := T1.
  - Hypotheses: every ρ_k is a.e.-finite and > 0, endorses every (D^k, T1)-localized relevant comparison of world k,
    and is integrable on E_k(T1) only.
  - Conclusion: (H_U) is contradictory.
  - H1.3 needed every ρ_k integrable on M. Non-integrability is now allowed wherever T1 is correct at that world,
    in particular at every T1-correct end.
- **(c) (All worlds (S); compatible localizations).** Let every world k be (S) with (ρ_k, D^k). Suppose that, for some
  m₀:
  - **(i)** μ(D^i_{m₀} ∩ D^j_{m₀} ∩ R_ij) = 0 for all i ≠ j;
  - **(ii)** Σ_k ∫_{D^k_{m₀}} Σ_{j : σ_j ≠ σ_k} ρ_j dμ + ∫_{M ∖ ⋃_k D^k_{m₀}} min(ρ₊, ρ₋) dμ < ∞, where
    ρ_± := Σ_{k : σ_k = ±1} ρ_k.

  Then (H_U) is contradictory.

  *Proof.* Let Y° be correct at k on D^k_{m₀}; this is consistent by (i), since off R_ij worlds i and j agree. Off
  ⋃_k D^k_{m₀} let Y° accept iff ρ₋ < ρ₊, and let it accept N₊. For m ≥ m₀, E_k(Y°) ∩ D^k_m is null, so (P1) is
  D^k-localized endorsement. The sum in (ii) is Σ_k ∫_{E_k(Y°)} ρ_k. ∎

**The residual of case (ii).** If every world is (S) (σ-finite, any localizations), a cover needs, for every m₀:
- **(R-i) sheltering:** D^i_{m₀} ∩ D^j_{m₀} ∩ R_ij non-null for some i ≠ j. Two disagreeing worlds then protect a
  common region at every depth; this is H1's (B). Or:
- **(R-ii) infinite minority mass:** either two disagreeing coalitions both carry infinite mass on a common region
  off the localizing sets, or some world's density is non-integrable on the localizing set of a world that
  disagrees with it.

Lemma K3.6 shows that T1-wrong blow-ups always produce such configurations.

**Lemma K3.6 (T1-wrong blow-ups are sheltered or shadowed; PROVED).** Assume (H_U), and let every world j be (S) with
(ρ_j, D^j). Let O be an open mixed orthant and W ⊆ O ∩ E_k(T1) measurable, with V(W) := {j : σ_j ≠ σ_k on O}
(H2 §1). Then at least one of the following holds:
- **(sheltered)** for some m, ρ_k(W ∖ ⋃_{j∈V(W)} D^j_m) < ∞;
- **(shadowed)** some j ∈ V(W) has ρ_j(W ∖ D^j_m) = ∞ for every m. On W, T1 is correct at j, and j disagrees with k.

*Proof.* Suppose (sheltered) fails.
- Choose m₁ and a non-null R ⊆ R⁰_k ∖ D^k_{m₁} with all ρ_j(R) finite. R⁰_k ∖ D^k_{m₁} is non-null for large m₁,
  and we may intersect with {max_j ρ_j ≤ n}.
- Choose pairwise disjoint p_n ⊆ W ∖ ⋃_{j∈V(W)} D^j_n with ρ_k(R) < ρ_k(p_n) < ∞ and all ρ_j(p_n) finite. This is
  possible: removing finitely many sets of finite ρ_k-mass from a set of infinite ρ_k-mass leaves infinite mass, and
  ρ_k(· ∩ {ρ_k ≤ N}) increases to it.
- Put X_n := T1 △ (p_n ∪ R); it is regular.
  - *World k.* δ_k = 1_R − 1_{p_n}: T1 is correct at k on R ⊆ R⁰_k and wrong on p_n ⊆ E_k(T1). It is ≤ 0 on
    D^k_{m₁}, so it is D^k-localized. If accepted it would be endorsed, i.e. ρ_k(p_n) ≤ ρ_k(R), which is false. So
    T1 ⋠_k X_n.
  - *Worlds j ∉ V(W) ∪ {k}.* T1 errs at j on p_n (σ_j = σ_k on O), and toggling on R⁰_k is good at both worlds
    other than k. So X_n ≺_j T1 by strict (G).
  - *Competitiveness.* T1 is competitive (Theorem kkm, as in H1.1), so T1 ⪯_j X_n for some j ∈ V(W), with
    δ_j = 1_{p_n} − 1_R.
  - *Endorsement at j.* δ_j is positive only on p_n, which misses D^j_n, so it is D^j-localized. Endorsement gives
    ρ_j(R) ≤ ρ_j(p_n).
- Some j ∈ V(W) occurs for infinitely many n. For every m, ρ_j(W ∖ D^j_m) ≥ Σ_{n≥m, n∈N_j} ρ_j(p_n) = ∞, since
  ρ_j(R) > 0. ∎

*Reading.* K3.6 is the σ-finite analogue of H2.1(b): there "a T1-wrong end is shadowed by T1-correct ends". The
patch theorem fails exactly when shadowed blow-ups cannot be separated, i.e. when min(ρ_k, ρ_j) has infinite mass
on W, or when they are sheltered. J1's pattern switching (unrefereed) is the integrable, end-protected special case
of choosing a patch.

---

## 6. T1: one world in (N) next to two integrable worlds

**Lemma K3.7′ ("between" lemma; PROVED).** Let K ⊇ K′ be a credal set, and let i ≠ j. D_K agrees with P_i a.e. on the
mixed problems of U where worlds i and j agree iff K ∩ [e_i, e_j] ≠ ∅ and K ⊆ conv(K′ ∪ [e_i, e_j]).

*Proof (i = 1, j = 2).* The problems are U ∩ [(+,+,−) ∪ (−,−,+)].
- *⇐.*
  - With m* ∈ K ∩ [e₁, e₂], m*·g < 0 on (−,−,+), so D_K rejects there.
  - D_{conv(A∪B)} = D_A ∩ D_B, so D_K ⊇ D_{conv(K′∪[e₁,e₂])} = U ∩ {g₁ > 0, g₂ > 0} ⊇ U ∩ (+,+,−).
- *⇒.*
  - D_K is open on M, so an a.e. statement about an open set holds everywhere off its boundary.
  - g_L := (−1, −1, L) ∈ U for large L, since min_{K′} m₃ > 0. Rejection of g_L gives m ∈ K with
    L m₃ ≤ m₁ + m₂ ≤ 1. Let L → ∞ and use compactness: K meets [e₁, e₂].
  - If m ∈ K lies outside H := conv(K′ ∪ [e₁, e₂]), strict separation gives g with m·g < α < min_H h·g. Adding a
    multiple of 𝟏 makes α = 0. Then g ∈ D_H = U ∩ {g₁, g₂ > 0}, and P_K(g) < 0.
  - g ≥ 0 is impossible (m·g ≥ 0), so g ∈ (+,+,−) ∩ U. A neighbourhood of g is then rejected by D_K, against a.e.
    agreement with P₁. ∎

NUMERICS (`k3py/between_lemma.py`, `.out`):
- 400 random polytopes K = conv(K′ ∪ extra points) tested on 95 397 samples of U ∩ {σ₁ = σ₂}, with targeted samples
  (−1, −1, L), L ≤ e⁸;
- all 114 predicted-agreeing K agree;
- 285 of the 286 predicted-disagreeing K disagree on the sample. The remaining one has an extra point with third
  coordinate 1.1·10⁻⁵, whose disagreement needs L ≳ 9·10⁴, beyond the sampled range; this is a sampling limit, not
  a counterexample.

**Theorem K3.7 (PROVED).** Assume (H_U). Let worlds 2 and 3 have integrable ρ₂, ρ₃ > 0 a.e. that endorse all their
relevant comparisons. Then world 1 is (M1) or (N). Suppose it is not (M1). Let ρ₁ := ρ_∞ and Λ := Λ_∞ (K3.1(d)
at world 1); more generally, ρ₁ may be any integrable ρ₁ ≥ 0 that endorses exactly the D-localized relevant comparisons
for some D, with Λ := {ρ₁ = 0} ∩ M. Put c := (ρ₁σ₁, ρ₂σ₂, ρ₃σ₃). Then:

- **(α)** Λ is non-null, and c has property (γ).
- **(β) Splices.** For θ ∈ [0,1] put G_θ := {θρ₂σ₂ + (1−θ)ρ₃σ₃ > 0}, and let S_θ be the model equal to P₁ on M ∖ Λ, to
  G_θ on Λ, and accepting N₊.
  - For a.e. θ ∈ (0,1), S_θ is coherent.
  - S₁ (P₂ on Λ) and S₀ (P₃ on Λ) are coherent.
- **(β′) Rigidity.** There are coherent C₁₂ = D_{K₁} and C₁₃ = D_{K₀} in M_U with K₁ ∩ [e₁,e₂] ≠ ∅,
  K₁ ⊆ conv(K′ ∪ [e₁,e₂]), K₀ ∩ [e₁,e₃] ≠ ∅ and K₀ ⊆ conv(K′ ∪ [e₁,e₃]), such that a.e.
  Λ = (E₁(C₁₂) ∩ R₁₂) ∪ (E₁(C₁₃) ∩ R₁₃), and E₁(C₁₂) = E₁(C₁₃) on R₁₂ ∩ R₁₃ = (+,−,−) ∪ (−,+,+).
  - In every open mixed orthant O, Λ ∩ O is a.e. either D_{K_*} ∩ O (if g₁ < 0 on O) or O ∖ D_{K_*} (if g₁ > 0 on
    O), with K_* ∈ {K₁, K₀}: a convex cone, or the complement in O of one.
- **(γ) Admissibility.** If Λ ⊉ E₁(T1) ∩ M (mod null), then D_{T1} = B_{p*} ∪ S with S ⊆ Z_{p*}, for some
  p* ∈ Δ°.

*Proof.*
- **First sentence.** If world 1 is not (M1), it is (M0), (S) or (N). (M0) is excluded by M0closed(b), and (S) by
  H1.2.
- **(α).**
  - If Λ were null, ρ₁ would be an integrable a.e.-positive endorser of the D-localized comparisons, and H1.2 would
    give a contradiction.
  - (γ) is Theorem K3.5 with Y° := P₁, D¹ := D, D² = D³ = ∅. (P1) at world 1 is D-localized endorsement, since
    E₁(P₁) = ∅. (P2) holds because ρ₂, ρ₃ are integrable. (P3) holds because ρ₂ > 0.
- **(β).**
  - (s, θ) ↦ t = (1 − s, sθ, s(1 − θ)) is a C¹ bijection of (0,1)² onto Δ° with Jacobian s ≠ 0. By (α) and Fubini,
    for a.e. θ the following hold: B_{t(s,θ)} is coherent for a.e. s, and {θρ₂σ₂ + (1−θ)ρ₃σ₃ = 0} is null.
  - Fix such θ, and good s_n → 0. Pointwise a.e.:
    - on M ∖ Λ, t·c = (1 − s)ρ₁σ₁ + O(s) has the sign of σ₁;
    - on Λ, t·c = s(θρ₂σ₂ + (1−θ)ρ₃σ₃);
    - on N₊, t·c > 0.
  - So B_{t(s_n,θ)} → S_θ in measure.
  - Limits in measure of coherent models of M_U are coherent: Hausdorff compactness, H1.0(a), H12_referee §1.1. So
    S_θ is coherent.
  - As θ → 1 (resp. 0), G_θ → P₂ (resp. P₃) a.e. on Λ, so S₁ and S₀ are again limits of coherent models.
- **(β′).**
  - S₁ = D_{K₁} with K₁ ⊇ K′, since coherent models of M_U have K ⊇ K′ (H12_referee §1.1).
  - Where σ₁ = σ₂, S₁ = P₁ (on Λ, P₂ = P₁ there). Lemma K3.7′ gives the conditions on K₁.
  - On R₁₂, S₁ = P₁ off Λ and S₁ = P₂ = (U ∖ P₁) on Λ, so Λ ∩ R₁₂ = (D_{K₁} △ P₁) ∩ R₁₂ = E₁(C₁₂) ∩ R₁₂.
  - The same argument with S₀ and R₁₃ gives the C₁₃ statement.
  - On R₁₂ ∩ R₁₃ both descriptions equal Λ.
  - The orthant statement holds because P₁ ∩ O is O or ∅, and D_K ∩ O is a convex cone.
- **(γ).**
  - Run H1.1 with ρ₁ ≥ 0. Its steps 1–3 and 5 use endorsement of T1's localized out-comparisons, integrability off
    D_m, and Lyapunov, but not positivity. They give p* ∈ Δ with p*·v ≥ 0 a.e., where v_k = ±ρ_k according to T1
    being correct or wrong at k.
  - Boundary points other than e₁ are excluded as in H1.1 step 4, using ρ₂, ρ₃ > 0:
    - on the edge e₁e₂, use (−,−,+) ∩ D_{T1}: −p₁ρ₁ − p₂ρ₂ < 0;
    - on e₁e₃, use (−,+,−) ∩ D_{T1};
    - on the closed edge e₂e₃, use (+,−,−) ∩ D_{T1}: −p₂ρ₂ − p₃ρ₃ < 0.
  - p* = e₁ requires v₁ ≥ 0 a.e. on M, i.e. ρ₁ = 0 on E₁(T1) ∩ M, i.e. Λ ⊇ E₁(T1) ∩ M. ∎

NUMERICS (`k3py/splice_rigidity.py`, `.out`):
- (1) A blind set built from K₁ = conv(K′ ∪ {e₁, ½(e₁+e₂)}) and K₀ = conv(K′ ∪ {e₁, ½(e₁+e₃)}) covers 11% of the
  mixed sample. S₁ and S₀ coincide with D_{K₁} and D_{K₀} on the sample, the two descriptions agree on R₁₂ ∩ R₁₃,
  and there are 0 midpoint-convexity violations in 20 000 sums.
- (2) A slab blind set {−3 < g₂/g₁ < −1} in (+,−,+), which is not of the rigid form, gives 836 violations in 200 000
  sums for S₁. So S₁ is incoherent, as (β′) predicts.

*Reading.*
- **The blind set looks exactly like D2's.** On each of world 1's edge regions, Λ ∩ R₁ⱼ is the world-1 error set of
  a coherent model lying between P₁ and P_j. This is the shape of D2's c_a = E₁(C_a), installed on both edges at once.
- But D2's blind set is localizable and Λ_∞ is not. So the exceptional world must make a D2-shaped region
  non-localizably blind.
- The weak field c is then an integrable additive field with property (γ). It is strictly signed at worlds 2 and 3,
  vanishes at world 1 exactly on Λ, and, in case (γ), has T1 as a Bayes model at an interior weight.

**Question Q_A (additive; open).** Is there an integrable field c = (ρ₁σ₁, ρ₂σ₂, ρ₃σ₃) on U, with ρ₂, ρ₃ > 0 a.e. and
ρ₁ ≥ 0 vanishing exactly on a non-null set Λ of the form (β′), that has property (γ) and D_{T1} = B_{p*} ∪ S
(S ⊆ Z_{p*}) for some p* ∈ Δ°?
- "No" is Theorem M0closed(a) for fields with one weakly signed component. With K3.7 it would give: next to two
  integrable worlds, the third world of a cover is (M1) or has Λ_∞ ⊇ E₁(T1) ∩ M.
- M0closed(a)'s proof (Props. chainchords, carrying, crosspin) uses strict signs at every world. I have not checked
  which steps survive a zero component, so no conjecture is stated.
- The special structure ((β′), the splice family (β)) is what such a proof could exploit.

---

## 7. Assessment, the single open question, and how a counterexample would be aimed at T1

**What the attempt established.**
- The brief's route (Hahn–Banach, Yosida–Hewitt, localization) is carried out completely in K3.1.
- It proves (S) exactly when Λ_∞ is null. The residual is precisely the worlds with a non-null non-localizable blind
  set.
- (E) is absorbed (K3.2).
- No axiom other than closedness of the sections excludes the residual (K3.3).
- Case (ii) of BRIEF16 is closed except for sheltering and infinite minority mass (K3.5′(c)). T1-wrong blow-ups are
  forced into these forms (K3.6).
- For a single exceptional world, (M2) is reduced to the additive Question Q_A (K3.7).

**Where it broke.** Closedness of sections is the only remaining tool, and I found no way to use it outside
two-world nested chains.
- There, Lemma DL kills the tilted world, and F1.4 kills chain-free certificates.
- With crossing error sets (three worlds, interior selected models) there is no chain to cut.
- In two worlds the remaining gap is chained ratio certificates (CONJECTURE K3.C).

**Single open question (Q_K3).** In a full system (every axiom of BRIEF13, closed sections for every model), can some
world have a non-null non-localizable blind set Λ_∞? Equivalently (K3.1(f)), can there be a non-null B ⊆ M such that,
for every localizing D and every c > 0, every non-null B′ ⊆ B carries a c-ratio certificate made of D-localized
relevant comparisons?
- **No** ⇒ the classification holds in its strong form: every world that does not add up is (M1) or (S_int). With
  H1.2, K3.5′ and K3.7, covers of T1 would then need (M1) worlds, or sheltering, or infinite minority mass at two or
  more worlds.
- **Yes, with ¬(S)** ⇒ the classification is false, and that world is the new kind of world the brief asks for.

**How such a world would be aimed at T1** (from K3.7; every step below is a requirement, not a construction).
1. Worlds 2 and 3 additive (or with integrable full endorsers) with densities ρ₂, ρ₃.
2. Solve Q_A positively: choose Λ of the rigid form (β′) (a D2-shaped blind region on R₁₂ and on R₁₃) and ρ₁ ≥ 0
   vanishing exactly on Λ. The weak field must have property (γ) and make T1 Bayes at an interior weight.
3. Build world 1 so that its localized endorsers are exactly the multiples of ρ₁ off Λ, with Λ non-localizably blind.
   This is a closed-section version of the tilted mechanism on Λ: thin-sourced comparisons with flexible,
   disjointifiable targets, whose sums must not open any section.

If step 2 is impossible (Q_A "no"), a single exceptional world next to two integrable worlds must carry an (M1)
certificate, or be blind on all of E₁(T1) ∩ M.

**Not done.**
- No three-world system was built, and no selection through T1 was chosen.
- (M1) worlds are untouched (BRIEF16 residual (i)).
- Countably many ends (residual (iii)) are absorbed into (S) via K3.2(b) when the base has a density, and into Λ_∞
  otherwise. Nothing beyond that is claimed.

---

## 8. Dependencies and files

**Used.**
- Hahn–Banach separation in (L^∞)*; the Yosida–Hewitt decomposition; the infimum formula for π ∧ μ in ba.
- N17.1(c) and N17 Lemma 3.1.
- Theorem kkm.
- Lemmas H1.0 and H1.1 with H12_referee §§1.1–1.2.
- Theorem M0closed(a) (no integrability used) and (b).
- H1.2; F1.2 (proof of (b)); F1.4 (evidence only).
- Q12 / Q12_referee N3 (the tilted world); C2.1(4); Lemma vectorform.
- Coherent models of M_U are the D_K with K ⊇ K′ (H12_referee §1.1).

**Not used:** (Nest_e), edge results, ends beyond K3.2, E1.3, E1.4, (h), J1's results (only cited).

**Not yet refereed.**

`k3py/` (run with `python3 -I` from inside `k3py/`):
- `k3_common.py`: geometry of T1, U and D_K; samplers; midpoint-convexity test.
- `between_lemma.py` (+ `.out`): Lemma K3.7′.
- `splice_rigidity.py` (+ `.out`): Theorem K3.7(β′), positive and negative examples.
- `tilted_nonS.py` (+ `.out`): Theorem K3.3 (acceptance, failure of localized endorsement, open section).
