# Round 52: section topology and local comparison freedom

23 October 2026. Author-checked mathematical note; not independently refereed. These results do not construct a cover of T1.

## 1. A warning against the continuous posterior-tripod route

Let C_b be the posterior family through an interior compact credal set, parameterised injectively by the closed simplex. Suppose a proposed selection is C_{f(a)}, where f:Delta -> Delta is continuous, and every selected model is competitive on supp(a) on the full measurable model domain under strict (G).

Then f preserves faces. Indeed, if K is not contained in Delta_S, choose g positive at every world in S but with min_K p.g < 0. There is an open set of such gambles: take g_i=1 on S and g_i=-L off S, and use a member of K with positive mass off S. D_K does not give the correct definite answer on that open set. Replacing its advice there by that answer strictly improves it at every world of S. This contradicts competitiveness. Thus K is contained in Delta_S. For the posterior family this says supp(f(a)) is contained in supp(a).

Every continuous face-preserving f is surjective. To see this for an interior q, put F_i={a:f_i(a)>=q_i}. These are closed. On a face Delta_S, the sum of f_i over S is 1, so some i in S has f_i(a)>=q_i. The KKM lemma gives a point in all F_i; since both vectors sum to 1, f(a)=q. Boundary points follow by compactness.

Consequently a continuous posterior selection over the whole simplex cannot omit a neighbourhood's worth of posterior models near T. In particular, it cannot take its image only in a tripod or other set that is null near T, if Theorem K excludes gating the omitted models. Reparameterising the simplex does not fix that obstruction.

Scope: this does not prohibit discontinuous selections with closed fixed-rival sections, nor other coherent families. A local tripod is not ruled out as a local module, but cannot provide the advertised continuous whole-simplex posterior completion.

## 2. A section-preserving addition lemma

Work modulo Gaussian null sets. Write d(X,Y) for the measurable set of problems where their advice differs. Coherent models are conic: their advice depends only on direction.

Let I be an ideal of measurable sets (closed under subsets and finite unions) containing no non-null conic set. Examples:

1. Sets bounded up to a null set.
2. The larger ideal of sets S such that the radial length integral int_0^infinity 1_S(r theta) dr is finite for almost every direction theta. This includes unbounded sets; it is not a fixed protected region. Gaussian and polar Lebesgue null sets agree away from the origin.

If two conic models C,D have d(C,D) in I, they are equal modulo null sets. Their disagreement is conic, so the defining property of I applies.

Therefore, for any fixed arbitrary model X, there is at most one conic model C with d(C,X) in I: two such models would differ on a subset of d(C,X) union d(D,X), which belongs to I.

**Lemma.** Let a -> C_a be a coherent selection with closed model fibres; in particular, continuity in measure suffices. Let R_i have closed fixed-rival sections along this selection. Add ANY set B_i of comparisons whose disagreement supports belong to I, and write R'_i=R_i union B_i. Then R'_i still has closed fixed-rival sections.

**Proof.** For fixed X, all added comparisons from selected models to X must start at the same conic model C, if there is one. Since B_i is a relation on models, the additional index set is either empty or the entire closed fibre {a:C_a=C}. The new section is the union of the original closed section and that closed fibre. QED.

If additions are prescribed by disagreement records, they preserve (IB). The lemma does NOT say they preserve (G), (TC), undominatedness, (C), or the defence clause of (S).

No continuity of the added verdicts as the rival varies is needed. In particular, closedness along mass paths of bounded modifications is not forced by section closedness. The lemma supplies an exact way of preserving sections while admitting discontinuous verdicts on those paths.

Important: this is an ADDITION lemma. Arbitrarily deleting comparisons at such a fibre can open a hole in a previously closed section. It is not permission to alter an existing gate relation arbitrarily.

## 3. A genuine local construction theorem

Let Q_i be any reflexive relation on the full model domain satisfying strict (G), (IB), and (TC). Define

    X R_i Y iff guidance ranks X no worse than Y at i,
                or [d(X,Y) belongs to I and X Q_i Y].

Then R_i satisfies (G), (IB), (TC), and closed fixed-rival sections along every continuous coherent selection.

**Proof of (TC).** Consider an accepted directed triangle. If two links have supports in I, the third does too, since its disagreement is contained in their union. All three links then belong to Q_i, because Q_i includes guidance, and Q_i supplies the reversed links when required. If at most one link has support in I, at least two links are guidance comparisons. Their composition makes the third link a reversal of pointwise guidance, unless the whole triangle is trivial. Strict (G) in Q_i forbids a nontrivial such reversal. The all-guidance case is immediate. Thus (TC) holds. Sections follow from section-closedness of guidance and the addition lemma.

This theorem permits genuinely nontransitive Q_i. For example, use four strictly guiding additive judges, accept a nontrivial record when at least three judges strictly favour it, and add reflexivity. This strict-vote rule has (G), (IB), and no directed triangle: each judge can support at most two edges of a strict three-cycle, whereas three accepted edges require at least nine votes and four judges can provide only eight. It can have strict four-cycles. Weak votes with ties are NOT interchangeable with this rule.

The resulting R_i is a concrete family of independent rankings with (TC) and closed sections, with no margin or continuity requirement on local verdicts. This is not a cover: universal support defence and target undominatedness have not been proved. A four-cycle by itself also does not exclude a weak additive endorser, which might tie its members.

## 4. The hard part, stated without hiding it

This does not license keeping an additive rule on all other records. Earlier tail obstructions remain relevant. Records with non-I support must also be designed, not inherited from a fixed additive field.

The ideal partitions models by X~Y iff d(X,Y) is in I. Each class contains at most one coherent model. A triangle is either:

- wholly within one class;
- across three different classes; or
- has exactly one within-class link and two cross-class links.

This is a useful decomposition of (TC), not a solution to it. The construction above solves the within-class side and section preservation for its additions. A full construction must solve the cross-class defence problem and the mixed triangles. It cannot assign separate within-class rules using the coherent representative: after a common-context substitution the class changes, so that prescription need not satisfy (IB). Rules must still depend only on records.

The next positive target should be a cross-class rule on the full posterior family that works with a discontinuous local rule, and whose fixed-rival sections are closed before local additions. Do not demand continuity as the rival varies. Test the kink triple with arbitrary measurable splits and with the local rule installed, rather than testing another additive gate at each member.

## 5. Audit cautions

- PP52 Theorem 4.1 assumes verdict closedness along rival mass paths. This is not axiom (S).
- PP52 Proposition 7.3's written proof excludes one alternate realiser M' by padding with a set E. It does not as written prove that M is the sole realiser among a continuum of other coherent models. That requires an additional argument.
- PP52 Conjecture 7.2 remains a conjecture. A summary should not treat its selective kink exclusion as proved.
- Theorem K concerns own-Bayes, strict-pair gate unions. Its proof does not exclude general disagreement-based relations.
- The local construction above is author-checked and should be independently audited before use. It supplies (G), (IB), (TC), and section closedness; it does not establish (S), (LA), (C), or coverage.
