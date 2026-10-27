# Round 71: lead's claims to be checked (27 Oct 2026). Not refereed.

Notation as in AUDITOR_note.md: change r=(A,B); d_w(r); P(r)={w: d_w(r)>0}; H(r)= worlds guiding r; V(r)= worlds accepting r.
"Dangerous" = available to some coherent model and P(r)=Omega.
Disjoint additivity (application Prop 6.2): if X <=_w Y, Y <=_w Z and (X△Y)∩(Y△Z) null, then X <=_w Z.
With independence: if r1, r2 are accepted at w and compose disjointly, then r1⊔r2 is accepted at w.

## L1 (why the characterisation is easy)
Guidance, independence, strict score consistency and single-ranking protection each constrain one change at a time. No condition links two different changes. So the admissible rankings form a product over changes, and the maximal ones are maximal change by change. Any added condition that links changes (disjoint additivity, transitivity) breaks this.

## L2 (exact coverage criterion)
Take rankings with guidance, independence and strict score consistency. Such a ranking has undominated = coherent, with every incoherent model dominated by a coherent one, iff both of these hold:
- (a) every non-null change available to a coherent model is refused at some world;
- (b) every incoherent X has, to some coherent N, a change accepted at every world.

Sufficient for (b), given the repair theorem: (5') every change that no coherent model could make is accepted at every world where it strictly improves the score. Weaker still: such changes that improve the score at every world are accepted at every world.

The class {1,2,3,4,(5')} equals {R : R0 ⊆ R ⊆ some maximal ranking}. It contains R0 and all maximal rankings. Maximality is more than coverage needs.

## L3 (a canonical choice)
R∩ := the intersection of all maximal rankings. Then:
- V(r) = H(r) for dangerous r;
- V(r) = P(r) otherwise.

R∩ is the largest relation with guidance, strict score consistency, and:

(3') a change that some coherent model could make AND that improves the score at every world is accepted only where it is guided.

This weakens condition (3) of application Prop 6.3, which bans every non-guided change available to a coherent model. R0 ⊊ R∩ in general; e.g. in two worlds, add a set A of gambles near (2,-1) and (-1,-1), so that d = (1,-2) roughly. It is available to D_{δ_b}, accepted at a by R∩, and refused at a by R0. R∩ covers, because R0 ⊆ R∩ and R∩ satisfies (a).

Alternative characterisation: R∩ is the largest ranking satisfying 1–4 plus "neutrality". Neutrality says: a dangerous change accepted at one world where it is not guided is accepted at every world where it is not guided. Proof sketch: neutrality and protection force V(r) ∩ (non-guided worlds) = ∅ for dangerous r.

## L4 (maximality is incompatible with disjoint additivity)
Setting: Omega = {0,1,2}, E = R^3, μ with Lebesgue null sets, finite first moment, coherent model D_S = strictly positive vectors (the vacuous model).

For each ordering (x,y,z) of the three worlds, let u_{xyz} be the vector with coordinate x equal to 1, y equal to -1, and z equal to 10. Six atoms. Let A be the union of six small disjoint balls, one about each u_{xyz}, each of mass 1 (normalised). Let r = (A, ∅). Then:
- d(r) ≈ (20,20,20);
- r is available to D_S, since every gamble in A has a negative coordinate;
- H(r) = ∅;
- so r is dangerous.

For each world x, there is a split r = s ⊔ t with d_x(s), d_x(t) > 0 and both s and t failing somewhere. Take s to be all of the u_{xyz} ball, 19/20 of the u_{yxz} ball, and all of the u_{zyx} ball. Then s ≈ (10.05, -1.05, 20.5) in coordinates (x,y,z), and t ≈ (9.95, 21.05, -0.5). These are exact for point masses, robust for small balls (r71/cx.py).

So in every maximal ranking, whatever j(r) is, s and t are non-dangerous with positive increment at j(r). Both are therefore accepted at j(r), while r is refused there. Disjoint additivity fails.

Consequence: no ranking satisfying the auditor's 1–5 is disjointly additive in this setting. R∩ also fails disjoint additivity, by the same example. R0 is disjointly additive (Prop 6.2), because "no coherent model could make it" is preserved under disjoint unions.

## L5 (open)
- Is there a largest ranking satisfying 1–4, disjoint additivity, and neutrality? Is it R0? (L3 suggests not in two worlds: R∩ appears additive when |Omega| = 2. Check.)
- Explicit form of maximal additive extensions of R0 (the auditor's Zorn route, finite Omega).
- Restricted domains U closed under coherent hulls (application Cor 7.1): do L2–L3 carry over?
