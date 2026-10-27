# Rescaling and a global non-additive construction

21 October 2026. Author-checked proofs; not independently refereed. This is NOT a cover. It is an explicit ranking on all measurable models, followed by an exact proof that its (S) defence clause fails. The rescaling PDF was read in full. The rational geometry in section 6 was checked with exact fractions.

## 1. The rescaling note

Under the note's assumption that the target credal set M is a compact subset of int Delta,

    Q_p(g) = min_{m in M} (p*m).g/(p.m)

is coherent, and is the unique root t of P(p*(g-t1))=0. Its credal set is the posterior image M_p. The proofs in the note are correct under that assumption. The normalization does not change positive desirability:

    Q_p(g)>0 iff P(p*g)>0.

Thus it gives precisely the earlier diagonal desirable-gamble family, now with the appropriate normalized lower previsions. No division by the single number P(p) is generally valid.

For contamination, c=(1-epsilon)/3 and M=c1+epsilon Delta. This gives the posterior family discussed in the preceding audit, with imprecise edges and precise vertices. The present construction can be evaluated along this family, but does not make it competitive.

## 2. An explicit ranking, without choosing a global price field

Let H be the atomless problem space with finite Gaussian measure mu. Write r_i(X,g) in {0,1,2,3} for good, silence, bad, contradiction at world i. All null-set identifications are understood.

Choose nested finite measurable partitions P_0,P_1,... generating H modulo null sets. Each P_0 cell lies within one sign class (one minority world, or unanimous problems). Each cell is divided into two equal-measure children at the next level. In particular the largest cell measure tends to zero. The construction below uses a P_0 containing four additional specified equal-measure cells; splitting the remaining sign regions completes the partition. A standard atomless measure-space parametrization supplies the generating binary refinements.

For a record d=rec(X,Y), put

    D(d)={g:X(g)!=Y(g)},
    f_i(d,g)=r_i(Y,g)-r_i(X,g),
    Delta_i(B,d)=integral_B f_i(d,g) dmu.

Set eta_m=2^(-m)/8. Define X <=_i Y precisely when either:

1. f_i(d,g)>=0 almost everywhere (guidance); or
2. for some level m and some cell B in P_m:
   - Delta_i(A,d)>=0 for every other cell A;
   - at least three distinct cells A != B satisfy

         Delta_i(A,d) >= eta_m mu(D(d)).

For nontrivial records clause 2 permits one compartment to improve, provided at least three other compartments worsen by a definite amount. Its scale and compartments come from the disagreement; there is no fixed scalar evaluation whose sign defines the verdict. The thresholds tend to zero with refinement. This is not claimed to be a novel construction in the literature.

The use of integrals as coordinates is not itself evidence of additive representability. Section 6 gives a finite contradiction to every strictly guiding additive endorsement of the relevant comparisons.

## 3. Structural axioms

### (G), both halves

Pointwise worsening is accepted by clause 1. The reverse of a non-null pointwise worsening has no positive cell integral at any level and is not a pointwise worsening, so it is refused. Reflexivity follows as well.

### (IB)

Every ingredient depends only on the changed advice labels and their locations. Common advice outside D is unused.

### (TC), and absence of nontrivial ties

In fact no nontrivial accepted directed cycle of length two or three exists at a world.

Suppose three accepted records form an actual cycle X->Y->Z->X. Their rank increments sum to zero pointwise. If they are all guidance, they are all zero. Otherwise choose, among the nonguidance records, a certificate at the coarsest level m. That record has positive integrals on at least three P_m cells.

Every other record has negative integrals on at most one P_m cell: a guidance record has none, and a finer certificate with only one negative fine cell has at most one negative coarse cell. Two other records cannot cancel three positive cells. This contradicts the zero sum. The identical argument with one other record excludes a two-cycle. Hence (TC) holds and distinct models cannot tie at a world.

This argument uses only realizable cycles. It does not close accepted changes under arbitrary sums.

### Closed graph, hence the closed-section part of (S)

Use convergence in measure of advice labels, or equivalently the record metric rho. Rank increments are bounded, so this gives L1 convergence. At a fixed finite level the certificate conditions are closed: there are finitely many choices of the exceptional cell and the three positive cells, and all inequalities are weak. A nonzero limiting record retains positive thresholds; the zero record is guidance.

Consider certificates at levels m_n tending to infinity with f_n -> f in L1. The negative part of E[f_n | P_m_n] has integral at most 3 times the largest cell measure, which tends to zero. Also

    ||E[f_n|P_m_n]-f||_1
    <= ||f_n-f||_1 + ||E[f|P_m_n]-f||_1 -> 0.

Thus f>=0 almost everywhere. The limit is accepted by guidance. Guidance itself is closed. This proves closedness of the full relation, not merely sections.

Consequently every continuous-in-measure proposed selection, including the posterior contamination family, has closed sections for these rankings. No defence assertion is implicit here.

### Not transitive

Take four equal-measure P_0 cells, with world-i advice ranks initially (3,2,1,0). Successively change the ranks to

    (0,3,2,1), (1,0,3,2), (2,1,0,3), (3,2,1,0).

At each step the increment is a permutation of (-3,1,1,1). Each step is accepted by clause 2 at level zero, since a positive cell contributes s while eta_0 mu(D)=s/2. The reverse is refused. This is a strict four-cycle, consistent with (TC).

## 4. The actual undominated class: no stipulation

Call a model regular if it gives correct advice on unanimous problems and never contradicts itself. Every coherent model is regular.

**Proposition. Every regular model is undominated.** Indeed no distinct model is weakly better at all worlds.

Proof. On a minority-i sign class, give world i weight 2 and the other worlds weight 1. The weighted sum of advice ranks is 4 for each regular advice and 12 for contradiction. On a unanimous class, a regular model has rank zero at every world. Hence if C is regular and d=rec(X,C), the weighted sum of its rank increments is nonpositive pointwise. These weights are constant on every partition cell.

Suppose X <=_i C at all three worlds. If all three comparisons are guidance, all increments must vanish by that nonpositive weighted sum. Otherwise take the coarsest nonguidance certificate across the three worlds. At its three positive cells, at least one of the other two worlds must have a negative integral, by the weighted inequality. But each other world has negative integrals on at most one cell at that level. Contradiction.

Thus C_R is exactly the entire class of coherent models: all coherent models are undominated, and C_R is defined as the coherent undominated models. There are also many incoherent undominated regular models.

Accordingly (LA) holds. The model-by-model direct (C) holds because distinct models never tie even at a single world. This does not cure the excess of incoherent undominated models.

## 5. An exact failure of the defence clause of (S)

Let S_0 be a P_0 cell on which T1 is silent and world 1 is the minority world. Split S_0 into its two equal-measure P_1 children. Let Y agree with T1 elsewhere, give world-1-correct advice on the first child, and world-1-wrong advice on the second.

At world 1 the rank increment is -1 on one child and +1 on the other. At worlds 2 and 3 it is the negative of this.

- At level zero every cell integral is zero: no three positive cells.
- At level one there is one positive and one negative cell: still no three positive cells.
- At every later level each sign occupies at least two cells: the one-negative-cell condition fails.
- No world has a guidance comparison.

Therefore T1 <=_i Y is refused at every world. The reverse is also refused at every world. T1 cannot be a selected model at any index.

Nor can this ranking satisfy full (S) through some other selection while leaving T1 unselected: KKM would give a selected model weakly better than T1 at every world; its undominatedness and the absence of distinct ties force that selected model to equal T1, which has just been shown noncompetitive.

This is an actual failure, not an unproved condition to hand off. The construction is not a cover and not a full system under the adopted axioms.

## 6. Genuine finite non-additivity out of coherent undominated models

Here epsilon=3/10, c=7/30, and C_0=T1. Define four gamble directions:

    g_0=(3/4,-1/4,-1/4)
    g_1=(717/1000,-33/1000,-283/1000)
    g_2=(723/1000,-77/1000,-277/1000)
    g_3=(22/25,-8/25,-3/25).

All are world-1-positive and world-2/3-negative. For j=1,2,3 let K_j be the segment q_j +/- delta_j(-1,0,1), where

    q_1=(541/2000,1/20,1359/2000), delta_1=1/1000;
    q_2=(503/2000,51/400,621/1000), delta_2=1/10000;
    q_3=(129/500,69/100,13/250), delta_3=1/1000.

Let C_j=D_{K_j}. Exact rational evaluation shows C_j is silent at g_j and accepts g_l for every l != j. The lower/upper expectations, by row C_j and column g_l, are:

    C_0: (-1/60,17/60), (13/1500,463/1500), (3/1000,303/1000), (1/150,11/30)
    C_1: (39/2000,43/2000), (-1/1000,1/1000), (1/400,9/2000), (279/2000,283/2000)
    C_2: (7/5000,1/625), (11/40000,19/40000), (-1/10000,1/10000), (1059/10000,1061/10000)
    C_3: (7/1000,9/1000), (293/2000,297/2000), (59/500,3/25), (-1/1000,1/1000).

The strict margins persist on four disjoint sufficiently small open cones S_j around these directions. Take equal-measure measurable portions (or adjust cone apertures), of measure s, and include them in P_0.

Inside each S_j choose three disjoint sets E_{j,k}, k != j, each of measure s/4, leaving a quarter unused. Define Y_k from C_k by:

- replacing silence by world-1-good advice on S_k;
- replacing good advice by silence on E_{j,k} for each j != k;
- changing nothing else.

At world 1, rec(C_k,Y_k) removes one first-step error on S_k and adds one on each of the three E_{j,k}. Its cell integrals are -s on its own cell and s/4 on each other cell. Its disagreement mass is 7s/4, and s/4 > (1/8)(7s/4), so C_k <=_1 Y_k is accepted strictly.

At worlds 2 and 3 all these rank increments reverse sign. There are three negative P_0 cells; every refinement retains at least three negative cells. Hence both other worlds refuse C_k <= Y_k. Each of the four defences is indispensable. In particular one starts from T1 itself.

Let nu be any finite strictly positive charge on the world-1 good/silence error step, vanishing on null sets. Endorsing all four comparisons requires

    sum_{j!=k} nu(E_{j,k}) - nu(S_k) >= 0, for k=0,1,2,3.

Summing gives the negative of the charge of the four unused quarters, which is strictly negative. Impossible. The other advice steps do not change, so allowing separate positive penalties for every guidance step does not help. This rules out general strictly guiding additive endorsement, not just equal spacing of advice ranks or constant densities.

All sources C_k are coherent and actually undominated by section 4. These four models need not belong to the one posterior family; no such claim is made. This is a finite cancellation obstruction in a full atomless relation, not merely in an isolated seed fragment.

The same witnesses can have arbitrarily small disagreement mass: replace each S_k in the modifications by equal-measure subsets of measure t>0, split them into the same four pieces, and leave the rest unchanged. The P_0 certificate still holds with s replaced by t. The sources and the ranking remain fixed.

## 7. Status and significance

Established for this explicit ranking on the full domain:

- (G), (IB), reflexivity, (TC);
- (LA) and direct model-by-model (C);
- closed sections along the rescaled family (indeed a closed graph);
- coherent undominated sources, including T1, making indispensable non-additive defences;
- a finite certificate excluding positive additive endorsement;
- arbitrarily small disagreement witnesses.

Failed:

- the defence clause of (S), explicitly, so no full coverage theorem and no claim of class-wide (A).

The failure is excessive protection: all regular incoherent models remain undominated. No deletion-only repair can fix this particular construction: it has no ties between distinct models, so deletion cannot create strictness by breaking a tie and can only remove existing weak comparisons. Moreover deleting comparisons cannot supply T1's missing defence against the explicit rival. A successful extension must add comparisons that distinguish coherent from incoherent advice patterns while preserving (IB) and (TC). The present counting argument deliberately ignores that distinction, so it cannot itself prove such an extension.

This is a concrete new attempt and a substantial structural example, not a recommendation to let someone else finish a purported one-lemma solution. It does not resolve the original problem.

## 8. A second attempted construction, rejected explicitly

I also tried using the strictly guiding box-loss field as a common boundary scaffold for the posterior triangle family:

    loss_i(accept g)=-c g_i-epsilon min(g_i,0),
    loss_i(silence)=0,
    loss_i(accept -g)=c g_i+epsilon max(g_i,0).

This has the correct conditional edge intervals, but does not eliminate doubly explained dominating rivals. For p=u and q=(.30,.53,.17), take

    g=(.93,-.23,-.30), h=(.50,-.39,-.77).

The target accepts g and -h; C_q is silent on both. Removing those acceptances in a 6:5 mass ratio produces loss changes proportional to

    (-.0062666..., -.0562, -.0123333...).

All are negative. The signs and advice inequalities are strict, so the example extends to sufficiently small open patches with these mass ratios. Thus the tempting additive scaffold already produces a dominating rival whose reverse record is explained by another posterior model. The random search that found this pattern is in rescaling-design/splice_test.py; these displayed rational values provide a hand-checkable repair of the numerical witness.

This rejects the scaffold; it does not exclude the posterior family.
