# A target-preserving coherent-defender extension

21 October 2026. Original, author-checked proof; not independently refereed.

## What is achieved

This note constructs an actual extension operation on rankings. It chooses coherent defenders from credal sets that are constructed from the target, rather than from a prescribed selected family. It can install an uncountable collection of repairs simultaneously.

For three worlds and an interior coherent target, the operation preserves (G), (IB), (TC), and the target's undominatedness. Starting with guidance, or with a suitably supported finite non-additivity certificate, it also gives (LA) and direct (C). Every rival in an explicitly described class is strictly dominated at all worlds by a coherent model that remains undominated. That class includes every variant allowed by one legitimate local-freedom neighbourhood of the target.

It does NOT establish (S), cover all measurable rivals, or prove that the extension can be iterated to a full system. In fact the current relation fails (S); further extendability is the unresolved issue. Those limitations are substantive and stated below.

For the strongest self-contained version, combine sections 1–5 with the target-reference base and the three concentrated posterior defenders in section 11, then apply the two-sided exposure filter of section 12. This version handles every rival preserving the guards, defends T against those rivals, and has relevant non-additivity already in comparisons starting from T. Section 7 is a separate optional application using an earlier finite certificate, not a dependency of this version.

## 1. Conventions

Work on the full measurable four-advice domain, modulo Gaussian-null sets of binary problems. Write X <=_i Y for X no worse than Y. At world i the ranks are good 0, silence 1, bad 2, contradiction 3. Ranks are used only to prove the cycle claims; the new comparison rule is defined from advice labels, not numerical rank differences.

A record d=(D,a,b) specifies the disagreement set D and the two different advice labels on it. Installing a record means accepting all its copies in all common contexts. This enforces (IB).

The target is T=D_M, where M is nonempty compact convex and contained in int Delta. Let I_i denote the ideal model at world i. All measure statements below are up to null sets.

Let R^0 satisfy (G), (IB), and (TC), and leave T undominated. Assume there is a measurable set U such that every accepted comparison of R^0 that is not a pointwise guidance comparison has its disagreement contained in U.

This is a sufficient starting condition, not an axiom being imposed on all possible rankings. Guidance itself satisfies it with U empty. Guidance plus finitely many supported exchange records is another useful starting case.

## 2. Three guard sets

Choose three disjoint compact sets of problems G_1,G_2,G_3, each of positive measure, disjoint from U. On G_k:

* world k has the minority sign;
* T gives the minority answer;
* the signs and T's acceptance are strict, uniformly on the compact set.

Such sets exist for every interior target if U is empty. Indeed, put delta=min_{m in M,k}m_k>0. A gamble with payoff L at k and -1 at the other worlds is accepted by T whenever delta*L-(1-delta)>0. Take a small compact neighbourhood of each such direction. More generally the construction applies whenever U leaves the required sets available.

Choose small convex neighbourhoods V_i of e_i in Delta such that every probability in V_i gives:

* the minority answer on G_i;
* the majority answer on G_k for k != i.

Uniform strictness on the compact guards makes this possible. V_i may be made arbitrarily small. It contains full-support probabilities and small full-dimensional credal sets, not merely e_i.

Call D_K an i-defender if K is nonempty compact convex and K subset V_i. Its advice has the specified pattern on every guard. No posterior or fixed-shape condition is imposed on K.

Define the rival class

    X_G = {X: X agrees with T on G_1 union G_2 union G_3}.

Outside those sets, a rival can be arbitrary, including incoherent, nonconic, silent, or contradictory.

## 3. The extension rule

For C=D_K an i-defender and X in X_G, call (C,X) exposed relative to T if

    mu({g: C(g) != X(g) and X(g) != T(g)}) > 0.          (E_T)

Install the record rec(C,X) at EVERY world whenever (E_T) holds. Install all common-context copies of each such record. One may install any subcollection of these records, including a chosen defender for each rival, or the entire collection.

Write R^+ for R^0 together with these comparisons.

This is a record-based rule. Equivalently, a proposed record qualifies when its old advice has an extension to some D_K with K subset V_i, its guard pattern is

    D misses G_i;
    on each G_k, k != i, D is all of G_k,
    old = majority and new = T's minority answer;

and the new advice differs from T on a non-null part of D. Outside D, complete the rival using D_K. This produces a rival in X_G. No common advice in the actual comparison is inspected.

The exposure test protects T: the new side of such a record cannot be copied into T, because it disagrees with T on part of its own disagreement set.

## 4. Why a coherent defender exists for every rival in the class

**Proposition 1.** For every X in X_G with X != T there is an exposed pair (C,X) with C an i-defender. C may be chosen to have a full-dimensional credal set contained in int Delta.

There is even a uniform finite choice of three such coherent models that works for every X.

**Construction and proof.** Choose eta>0 sufficiently small that

    eta < min_{m in M,k}m_k,
    v_i=(1-3*eta)e_i+eta*1 belongs to V_i,

and choose a small full-dimensional compact convex K_i around v_i, contained in V_i intersect int Delta intersect {m:m_i>1/2}. Put C_i=D_{K_i}.

Their agreement is subordinate to T:

    if C_1(g)=C_2(g)=C_3(g)=a, then T(g)=a.             (A)

To see this, all three cannot be silent: at a coordinate i of maximal absolute payoff, every m in K_i has m_i>1/2, so m dot g has the strict sign of g_i. If they all accept the same answer g, then every v_i dot g>0. But

    M subset conv{v_1,v_2,v_3}={m in Delta:m_i>=eta},

so T accepts g too. The opposite answer is identical; contradiction is never given by a coherent model. These statements ignore the null zero/tie sets as usual.

Now on every problem where X differs from T, (A) ensures that at least one C_i differs from X. Since there are only three C_i and the disagreement with T has positive measure, at least one i satisfies (E_T). This proves the proposition.

The uniform triple is a convenient existence proof. It is not a mandatory family: the rule permits any suitable credal set in the corresponding V_i. The defender can be chosen after seeing the rival.

## 5. The extension theorem

**Theorem 2.** Under the starting assumptions, R^+ satisfies (G), (IB), and (TC), and T remains undominated. Every i-defender that was undominated under R^0 remains undominated under R^+.

Every newly installed comparison is strict at every world. Consequently, if R^0 has no distinct models tied at all worlds, R^+ has no such ties either and direct (C) holds automatically. In particular these claims apply with guidance as the starting relation.

**Proof of (IB).** The operation explicitly installs whole record classes.

**Proof of (G).** Fix a new record labelled i and a world w. Choose k different from i and w; when w=i, choose any k != i. On G_k the old advice is the majority answer, correct at w, whereas the new advice is T's minority answer, wrong at w. Thus the record has a strict worsening at w. It can never be the reverse of a guidance comparison. Adding it preserves both halves of (G).

**Two new records cannot compose.** Suppose their labels are i and j. Choose k different from both; if i=j choose any k != i. Both records contain all of G_k, and both change the majority answer to the minority answer there. The new side of the first therefore cannot equal the old side of the second on G_k. This rules out composition in every common context, not merely at their originally named sources.

**One new record cannot participate in a three-cycle with two old comparisons.** Fix the world w and choose k as in the guidance proof. The new record strictly increases rank on G_k. Every old nonguidance record is zero there, since G_k is disjoint from U. Every old guidance comparison has nonnegative rank change there. Rank changes cannot sum to zero around an actual cycle. Hence no such three-cycle exists.

Any new violation of (TC) would contain a new accepted comparison. A cycle containing two new comparisons is impossible by noncomposition; one containing exactly one is impossible by the preceding argument. Old triples satisfy (TC). This proves (TC).

**Strictness.** The reverse of a new record is neither guidance, nor an old nonguidance record (its disagreement includes guards outside U), nor another new record (which would compose with the first). Hence it is refused at every world.

**Protection of T.** A new comparison cannot end at T by (E_T). Its incoming comparisons are unchanged. No previous dominator of T existed, and adding outgoing comparisons cannot create one.

**Protection of a defender C in V_j.** For a new record labelled i choose k != i,j, or k != i if i=j. On G_k its new side is T's minority answer, whereas C gives the majority answer. Thus no new record can end at C. An undominated defender remains so.

**Direct (C).** No new tie is created, because every new comparison is strict. Under the stated no-distinct-all-world-ties starting condition, all-world ties in R^+ are identities. This is sufficient for direct (C). Without that starting condition, preservation of direct (C) is NOT asserted: shrinking the undominated class could otherwise split an old tie class. QED.

## 6. What the theorem gives from the minimal starting ranking

Start with guidance alone. Every coherent model is initially undominated: distinct regular advice cannot improve at every world on the problems where it changes. There are no nontrivial ties.

Apply the operation using Proposition 1. Then:

* T and the constructed coherent defenders are actually undominated;
* every X in X_G other than T is strictly dominated at every world by at least one of those defenders;
* (G), (IB), (TC), (LA), and direct (C) hold on the full measurable domain.

The operation handles all such rivals simultaneously. It is not a finite-cell or finite-rival statement. It also handles modifications of arbitrarily small positive measure; their coherent dominators can be far away from the target.

### Local freedom

The guards can be chosen compact and separated from every nonzero boundary point of the target's acceptance cone. Their symmetric copies are separated from that boundary too. Therefore the open set

    N = R^3 minus the symmetric compact guard sets

contains that entire boundary. Every acceptance-set variant R with R symmetric-difference T contained in N agrees with T on the guards, and so belongs to X_G.

Thus this construction does not obtain target protection by excluding its borderline competitors. It evaluates them all, and strictly dominates every distinct one. The coherent defenders are evaluated on the full domain as well.

This does NOT mean the domain can be cut down to X_G. The defenders themselves disagree with T on the guards and would be excluded. Splice closure would also reintroduce further rivals.

## 7. Retaining a relevant finite non-additivity certificate

The extension theorem is independent of pricing. To guarantee non-additivity relevant to coherent undominated sources, it can be combined with the four-record certificate previously constructed in the audit and embedded in the posterior family by PP13.

Use only those certificate comparisons, their record copies, and guidance as R^0; do not retain the whole old multiscale ranking. Their nonguidance supports lie in four small cones U of one minority-sign class. At world 1 they have one negative cell and three positive cells; at worlds 2 and 3 the reversed records have the same cell-count pattern. The three-positive/one-negative counting argument rules out accepted two- and three-cycles. The sign-class weighted rank identity rules out domination of a regular model: three positive cells at one world would require negative cells at three locations from the other two worlds, which can supply at most two. Thus the coherent sources are initially undominated and there are no distinct ties.

The certificate says that four comparisons from coherent sources, one of them T, cannot be endorsed by any strictly positive additive weighting of the advice steps. It remains a certificate after comparisons are added, provided those sources remain undominated.

Here is a checkable protection condition for an additional source A:

    for every defender label i, some k != i has
    mu({g in G_k:A(g) != T(g)}) > 0.                    (P_A)

Under (P_A), no new record can end at A, by the same guard argument. This is sufficient; it is not declared necessary.

For contamination, the other three posterior sources in PP13 can be protected this way. Their index coordinates are pairwise distinct. For any i choose the other coordinates j,k with p_j<p_k, write r=c/(c+epsilon), and choose

    r*p_j/p_k < t < r,
    g_j=1, g_k=-t, g_i=-delta

with delta>0 sufficiently small. T accepts g, the posterior source is silent on g, and the minority world is j != i. Indeed T's lower expectation is positive while the posterior lower expectation is negative and its upper expectation positive. A small compact neighbourhood preserves these strict inequalities. It can be chosen away from the certificate cones by taking delta small.

Adjoin these finitely many patches to the corresponding G_j, and shrink the V_i as necessary. This enforces (P_A) for all three sources. Every guard still has the required sign and target advice.

Consequently the relevant finite non-additivity certificate survives with its coherent sources genuinely undominated. Its unique world-1 defences also remain unique: no new record has its disagreement confined to U, so the other worlds' refusals of these small records are unchanged.

This last application uses the earlier certificate geometry; the extension theorem and Proposition 1 do not depend on it.

## 8. Closedness: an allowed discontinuity, not a proof of (S)

The exposure condition is strict and the extended relation need not be closed as its rival varies. This is deliberate and visible.

For example, take C=I_i and rivals X_n that fill a shrinking part of T's silence with an answer wrong at i, preserving the guards. Then I_i is strictly preferred to every X_n at every world after the extension. But X_n tends to T, and the record (I_i,T) is not installed, because its exposure set is empty. At worlds w != i, (I_i,T) is mixed on the guards, so it is not guidance or an old comparison supported in U either.

This is a discontinuity with the SOURCE fixed and the RIVAL changing. It is not, by itself, a violation of (S), which requires closedness along a selected coherent family with the rival fixed.

This distinction does not establish (S). Indeed section 13 shows that the current relation fails (S), not merely that a selection has yet to be found. Whether the filtered relation admits a suitable further extension remains open. The ideal models give vertex defences by guidance, but the edge and interior selection obligations remain.

## 9. Where the operation stops

1. Rivals that alter the guard sets are not covered by the theorem. The shared guard advice is the reason the triangle proof works.
2. The operation cannot simply be repeated with the same guards: its new nonguidance records now change those guards, violating the starting support condition for another application.
3. A fresh set of guards would require a new compatibility proof. Neither transfinite induction nor taking a maximal extension supplies it.
4. The batch may dominate coherent neighbours of T as well as incoherent rivals. If a coherent model agrees with T on all guards and differs elsewhere, it is deliberately dominated. Thus preserving a rich continuous family near T is not automatic; the construction does not assume that such a family must survive.
5. The result determines protected members and some excluded members of the actual coherent undominated class. It does not identify that class completely or stipulate that it equals the defender set.

The next genuine extension problem is now concrete: can guard-changing rivals be handled without losing the shared transition that prevents composition? A proof must address that question and the fixed-rival sections, not merely choose another allocation of the same repairs.

## 10. Axiom status

With guidance as the base, or the protected finite-certificate base described above:

| Requirement | Status |
|---|---|
| Reflexivity | Preserved |
| Both halves of (G) | Proved globally |
| (IB) | Proved globally by record installation |
| (TC) | Proved globally, for arbitrary measurable models |
| Target undominated | Proved |
| Coherent chosen defenders undominated | Proved |
| (LA) | Proved |
| Direct (C) | Proved via absence of distinct all-world ties |
| Every distinct rival preserving the guards strictly dominated at every world | Proved |
| All variants in a legitimate target (LF) neighbourhood included | Proved |
| (S), defence clause on the entire simplex | Current relation fails; further extension open |
| (S), fixed-rival closed sections | No witnessing selection constructed |
| Full coverage (A) | Not established |

This is a target-preserving, variable-coherent-defender extension with a global consistency proof. It is not a covering theorem. Sections 11–13 strengthen the construction and identify a trap in installing the entire unfiltered batch.

## 11. A stronger starting relation: defend the target as well as repair its rivals

There is a useful alternative to starting with guidance or the finite certificate. Set U equal to the complement of the guards. At world i accept guidance and every record with

    old advice = T throughout D,
    D subset U,
    mu({g in D:r_i(new)>r_i(T)})>0.

Call this the target-reference relation. It uses the identity of the old advice, not just its rank increment.

**Lemma 3.** This relation satisfies (G), (IB), and has no nontrivial accepted finite cycle. T is undominated. For every X in X_G, T is no worse than X at some world.

**Proof.** A nonguidance record has a positive-measure set where it moves away from T to a strictly worse rank. At a problem in that set, subsequent guidance can only worsen the rank. Another target-reference step can apply there only after the advice has returned to T. Taking the first putative return shows it is impossible. Thus no accepted cycle can contain that record. Guidance alone has no nontrivial cycle either.

No nonguidance record can end at T, so T remains undominated. Finally, a change away from regular T cannot be pointwise better at every world. Some world has a positive-measure worsening, supplying the stated comparison. For X in X_G the support is outside the guards. QED.

This is not claimed as a new general mechanism by itself; it resembles the previously studied target-based veto constructions. Its role here is a compatible starting relation for the extension.

### Co-designing defenders that remain undominated under this stronger base

For T1 choose a large a>1 and put

    K_i = Phi_{s_i}(T), where (s_i)_i=a and (s_i)_j=1 for j!=i,
    C_i = D_{K_i}.

Only these three models are being used as potential defenders. No posterior family indexed by the whole simplex is prescribed.

For sufficiently large a:

* K_i subset V_i and all its probabilities have coordinate i greater than 1/2;
* conv(union_i K_i) contains T, since K_i contains (a,1,1)/(a+2), with a in coordinate i, and 1/(a+2)<c;
* C_i is pointwise no worse than T at world i. Multiplying just the i-th payoff by a increases the lower prevision of an i-positive gamble and decreases that of an i-negative gamble. Thus it can add correct advice or withdraw wrong advice at i, but cannot worsen the advice there.

That last property makes C_i undominated under the target-reference base. If a proposed dominator Y has any nonguidance incoming comparison Y <=_j C_i, then Y=T throughout their disagreement. At world i, C_i is pointwise no worse than T, so Y <=_i C_i cannot be a target-reference comparison. It cannot be guidance either: that would require both advice orders on the disagreement, hence identical advice there, a contradiction. If every incoming comparison is guidance, a regular coherent model cannot be dominated at all worlds. Thus C_i remains undominated.

Proposition 1's agreement argument applies to these C_i. Therefore they supply exposed defenders for every X in X_G distinct from T. Theorem 2 then preserves their undominatedness.

**Result.** With this base and these defenders, all of (G), (IB), (TC), (LA), and direct (C) hold. T is undominated and defends itself against every rival preserving the guards. Every distinct such rival is also strictly dominated, at all worlds, by an undominated coherent defender.

This repairs the previous split-cell failure for the entire guard-preserving rival class, not merely for a finite list of splits.

### Relevant non-additivity is already present

At a world i choose disjoint non-null A_n where T gives good advice, and a fixed non-null B where it gives bad advice, all outside the guards. Let X_n silence T on A_n union B. The target-reference relation strictly accepts T <=_i X_n for every n.

A finite strictly positive additive weight on the advice steps endorsing these comparisons would require

    nu(first step on A_n) >= nu(second step on B) > 0

for every n. Summing over arbitrarily many disjoint A_n contradicts finiteness of nu. This also rules out finite finitely additive endorsers. It does not rule out every unbounded or non-Archimedean representation.

These comparisons start from the actual coherent undominated target. Their non-endorsement is not confined to irrelevant comparisons elsewhere in the domain. It is an infinite obstruction, not a finite cancellation certificate.

## 12. Do not install all exposed repairs indiscriminately

The unfiltered rule has a real trap. This is important: preservation of the target and (TC) is not by itself preservation of future (S) obligations.

Take the ideal I_3 as an allowed defender in the unrestricted operation of section 3. Let Y agree with T except that it gives the majority answer on G_1 and G_2. Choose a further positive-measure set E outside the guards on which T and I_3 both give the minority-3 answer. Let X agree with I_3 except that it agrees with T on G_1,G_2 and is silent on E. It also agrees with T on G_3, so X belongs to X_G. The record d=rec(I_3,X) is exposed and is installed by the unfiltered rule.

Its old side agrees with Y on its disagreement. Copying it after T -> Y gives Z equal to T except for silence on E. At worlds 1 and 2, Z strictly improves T by guidance. Therefore (TC) forbids T <=_1 Y and T <=_2 Y once d has been installed. Guidance already forbids T <=_3 Y, because Y improves T at world 3 on both changed guards.

Thus this one optional repair blocks every defence of T against Y. This excludes an extension satisfying (S) with T selected. It also excludes a full extension with (S) and no distinct all-world ties: KKM would then force the undominated T to be selected. It does NOT exclude the separate possibility of T being an unselected all-world tie of another selected model under a more general future extension.

This is why the unrestricted batch should not be advertised as an eventual coverage construction.

### A substantive repair: two-sided exposure

Let W be the union of the guards (or a fixed larger set on which rivals agree with T). In addition to (E_T), require

    mu({g outside W:C(g)!=T(g) and X(g)!=C(g)})>0.       (E_C)

The forbidden pair above fails (E_C): away from the guards, it changes its defender only where that defender agrees with T. The additional condition rules out precisely that direct composition with a target comparison changing only W.

This filter is not asserted to resolve every remaining return comparison. However it does not cost existence of defenders in the T1 construction:

**Lemma 4.** With the three sufficiently concentrated C_i from section 11, every X in X_G distinct from T has a defender satisfying BOTH exposure conditions.

**Proof.** Proposition 1 supplies an i satisfying (E_T). If it also satisfies (E_C), stop. Otherwise X=C_i almost everywhere on the part of T's silent region where C_i is definite. This region is outside W.

Choose j!=i. On an open neighbourhood of the gamble with coordinate i equal to 1, coordinate j equal to -1 and the third coordinate 0, T is silent, C_i gives the i-answer, and C_j gives the opposite answer, provided a>1+epsilon/c. Hence X=C_i there. It follows that X differs both from T and from C_j, while C_j differs from T. The same positive-measure region witnesses both exposure conditions for j. QED.

The guard proof of Theorem 2 survives unchanged after filtering, since it held for any subcollection. Thus the stronger result of section 11 survives, together with relevant non-additivity and a new safeguard against one explicit future-defence obstruction.

The use of W larger than the guards requires that the displayed opposite-advice patches remain outside W; this holds for guard sets contained in T's strict-acceptance regions, as constructed here.

## 13. The remaining (S) failure must still be stated explicitly

Even the filtered construction is not a full system. The same Y that changes T on G_1 and G_2 is not defended by T in the current relation:

* guidance refuses world 3 and is mixed at worlds 1 and 2;
* target-reference records are confined to the complement of the guards;
* a new repair record starts with a defender's majority advice on two guards, whereas T gives the minority advice on all three.

So T <=_i Y holds at no world. Since the current relation has no distinct all-world ties, it cannot satisfy (S) through some alternative selection either: the KKM argument would require T itself to be selected.

Unlike the particular unfiltered repair in section 12, the current filtered rule has not been proved to make all future defences of Y impossible. This is the exact next issue. The result is a globally consistent partial extension, with a variable coherent defender and control of all local-freedom rivals, not a completed coverage result or a guarantee of further extensibility.
