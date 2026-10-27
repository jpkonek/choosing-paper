# Problem P1 after round 5: conditional results and the residual (working notes, 11 October 2026)

Setting: n = 3; every ranking a complete preorder with (G) and (IB); (S). Question: is V dominated? OPEN.

Written and refereed (see the note "Fineness Spreads Along Edges"): one fine world, one fine edge, or one tame world
(fine / one-sided fa loss / group primary / finite cancellation) makes V dominated; (LH) and (DH) hold at every world.

This file preserves two further rounds of working notes, each independently refereed (CORRECT, with minor fixes listed
in the reports; the reports also prove some strengthenings). They are not yet written up as a note.

1. M2 notes (+ referee report RM2). Lemma 2.1 / Cor 2.2: V dominated if one level of a three-world compensation
   ("(M2*) at one level") holds at one interior selection of edge 12. Prop 3.1: far-end compensation at the D_2 end.
   Theorem 5.6: under tail continuity (TC) of six cross-world threshold maps and meagreness of the high levels not
   crossed comparably on edges 12, 23, 31, V is dominated. RM2: the matchings in (TC) are automatic (Lemma R1);
   only high levels matter (Lemma R3, Cor R4); the claim "jumps are harmless" is false for dense jumps.
2. TC notes (+ referee report RTC). Flats and jumps (including dense jumps) of the threshold maps are heavy levels
   (Lemma 3.5); hence Theorem 5.6 holds without (TC) as a dichotomy (Thm 3.6, Cor 3.7); if all six far ends of the
   edges are local chains, V is dominated (Cor 3.10); holonomy without continuity (§4). RTC §4.8: with three
   local-chain ends, reducing six ends to three amounts to excluding three specific defect types.
Residual: a heavy level crossed only nestedly (T1), and meagreness of uncovered levels at far ends that are not
local chains (T3). Suggested next step: a far-end chain lemma ((S) + V undominated force the selections near each
vertex block to be pairwise comparable); Cor 3.10 would then settle P1.

Cross-references inside these notes (K, B, C5, LH, P1A, P1C, G3, N, J) are to earlier working notes; the refereed
content of K, B, C5, LH is written out in "Fineness Spreads Along Edges".


---
# Part 1. M2 notes
# M2_notes — (M2)/(M2*) at interior edge selections: what can be proved, what blocks it

Standing (unless stated): n = 3; all three rankings complete with (G), (IB); (S); V undominated.
Notation as in B_notes / LH_notes / K_notes (r5/SETTING5.md). Regions P_1, P_2, P_3; D_vw = P_v u P_w.
Option table (B §1 / LH §2, refereed RB5 §1, RLH §1):
 change          world 1     world 2     world 3
 o_23 on P_1     debt_1      credit_2    credit_3      ("triangle option" on P_1: bad only at 1)
 o_1  on P_1     credit_1    debt_2      debt_3
 o_13 on P_2     credit_1    debt_2      credit_3      (triangle option on P_2)
 o_2  on P_2     debt_1      credit_2    debt_3
 o_12 on P_3     credit_1    credit_2    debt_3        (triangle option on P_3)
 o_3  on P_3     debt_1      debt_2      credit_3
Pairs: "(A,T) at world k" = debt_k on A, credit_k on T; acc_k(A,T) :<=> V + debt_k(A) + cred_k(T) <=_k V
(weakly SI / weakly accepted); SI = strictly accepted; AC = not SI (by completeness V <=_k ...).
For E in F_12 (coherent undominated, competitive on {1,2}; every open-edge-12 selection is one) with
thresholds (alpha_E, beta_E) in t_12 = g_1/|g_2|: T_0(E) := P_2 n {t_12 > alpha_E} (o_13),
B_0(E) := P_1 n {t_12 < beta_E} (o_23). Interior: 0 < beta_E <= alpha_E < inf.
World-2 frame on edge 23: s := t^2_3 = |g_2|/|g_3| on D_23; world-2 frame on edge 21: t^2_1 = 1/t_12.
Deep P_3-tails: Y_c := P_3 n H^3_2(c) = P_3 n {s < 1/c} (world 3's high tail of edge 32 = world 2's low cone).
J^{(2)}[Y] := finite unions of sets Q (inside P_2) with acc_2(Q,Y) (an ideal: hereditary by (G), closed under
finite unions by definition).
Labels PROVED / PLAUSIBLE / OPEN. Written incrementally; §0 updated last.

## 0. Status summary (written last)

P1 and (M2*): OPEN. Nothing here is refereed yet. PROVED (full proofs below):
 S1 (§2, Lemma 2.1, Cor 2.2) Single-triple criterion, sharpening B Thm 3.6 + LH §7 R4: V is dominated as soon as
    for ONE E in F_12 there are non-null X_1 subset B_0(E), X_3 subset P_3, W subset T_0(E) with acc_3(X_3,X_1),
    acc_1(X_1,W) and W in J^{(2)}[X_3]. So (M2*) is needed at ONE level c = c(T), not at every level. Cor 2.3: in
    a counterexample world 2's X_3-compensable debt on T_0(E) is absorbed by X_1-credit alone (G subset N,
    N + G = N); world 1's credit on T_0(E) lives on world-2-bad sets.
 S2 (§3, Prop 3.1, Cor 3.2; idea (iv)) If the D_2-end of edge 12 is approached by interior selections C_m, then
    for every non-null X_3 subset P_3 the whole far tail D_12 n {t_12 > alpha_m} — in particular T_0(C_m) — is
    ONE X_3-good piece for world 2 for large m (no V, no completeness). This is (M2) in its strongest form, but
    at a moving selection; P1 then reduces to an explicit three-rate race (Cor 3.2(ii)).
 S3 (§4, Lemma 4.1, Prop 4.2, Rem 4.3; ideas (ii), (iii)) The only competitiveness source of world-2
    acceptances of (P_2-debt, P_3-credit) is the edge-23 XOR (competitiveness at a selection whose support contains
    world 1 never yields such an acceptance); with tail lightness it covers {s -> 0} and {s -> inf} of world 2's frame, never the
    middle of T_0(E), where the heavy germ sits. The tied full-support selection C_{p_V} gives a strict anti-TRI
    principle, with the same bundling.
 S4 (§5; idea (i)) Six tail families (one per world and edge), three exact XOR couplings, transverse lightness
    via XOR, and the two triangle 2-cycles. Prop 5.4 (holonomy rigidity): under tail continuity (TC) of the twelve
    cross-region thresholds, V undominated forces trivial holonomy H_1 = id and an unattained threshold at every
    tail level; Cor 5.5: each such level carries a heavy right debt germ of a tail family relative to an explicit
    light credit (no race: all sets fixed before the last comparison). Theorem 5.6: (TC) + "on each of the
    edges 12, 23, 31 (world 1, 2, 3 frames) the levels not crossed comparably from the worse side form a meagre
    set" => V dominated (Baire).
 S5 (§6) Updated list of necessary conditions; an order-separated valuation of the triangle options satisfies
    every constraint on triangle options I know (TRI, exact XOR, lightness of all tails in all views, (LH)/(DH),
    failure of (M2*)) but any lexicographic world order realizing it is killed by P1C Lemma 3.3; finite tie data
    cannot decide (1442 consistent assignments, script r5/m2chk/tie_orders.py).
Precise obstruction to (M2*). Every route ends in a race of lightness rates: the X_1 that world 1 accepts
against T must be lighter than T's credit, the X_3 that world 3 accepts against X_1 lighter than X_1's credit,
and T's pieces must be lighter for world 2 than X_3's credit; each available tool (tails, cones, (LH), XOR,
far-end closedness) only says "eventually lighter than a FIXED set", and nothing compares the three rates. In the
tail picture the race becomes trivial holonomy plus heavy germs at every level (Cor 5.5). No counterexample
structure was found: the natural one (order separation) has a top level and dies by P1C Lemma 3.3.
Most promising next step: remove (TC) from Theorem 5.6. A threshold map is a real monotone function, so it has
only countably many jumps; jumps are harmless for the Baire argument once Prop 5.4 is redone with monotone
correspondences (the only issue: "rectangles" in compositions at common jump points, countably many). FLATS of
the maps x -> h_{CA}(x), x -> h_{DC}(h_{CA}(x)) are the genuine residual: each flat is a single-level heavy germ
of a tail family relative to a credit band, and it produces an interval of triples with the same germ. So the
next target is: (S) excludes flats of the cross-region tail thresholds (equivalently, a world's tail debt is
never infinitely heavier at one level than another world's tail credit band), which with S4 would reduce P1 to
the meagreness of uncovered levels on three edges.

## 1. Inputs used (exact labels; refereed where stated)

(XOR) G3 Lemma 3.1 (RB5 §2 (I1)): for E in F_12, T subset T_0(E), B subset B_0(E): acc_1(B,T) or acc_2(T,B)
      (no V-hypothesis); if V is undominated and T u B non-null, not both (world 3 gains strictly).
(TRI) B Lemma 3.1 (RB5 §7: CORRECT): for non-null X_k subset P_k, not all of acc_1(X_1, X_2 u X_3),
      acc_2(X_2, X_1 u X_3), acc_3(X_3, X_1 u X_2); in particular no cyclic triple of 2-set acceptances.
(COMP) CCF §5 / (IB) + transitivity: acceptances of disjointly supported changes compose.
(Y-d), (Y-c) yardsticks at every world v (LH §2 (I1), (I2); P1A Lemmas 2.1, 2.2; RK §2.3): high tails of both
      edges at v are debt_v-lighter than any non-null set (completeness at v); low cones of both edges at v are
      credit_v-lighter than any non-null set.
(LH),(DH) LH Thm 4.1 (RLH: CORRECT WITH MINOR FIXES): at every world no non-null set is credit-null and none is
      debt-infinitesimal (V not needed).
(M1) LH 5.6(b) (RLH: CORRECT): for every non-null Z subset P_1 there is c with acc_3(Y, Z) strictly for every
      non-null Y subset Y_c.
(S_SI^i), (S_AC^i) P1A Lemma 4.2 (RK §2.4) in each world's frame.
(B3.6) B Thm 3.6 (RB5: CORRECT WITH MINOR CLARIFICATIONS) and LH 5.6(c): if for an interior E in F_12 some
      non-null T subset T_0(E) satisfies (M2*) [T in J^{(2)}[Y_c] for every c], then V is dominated.
(T2) CCF §3 (T2) (no completeness), in any world's frame: F <_j C_{q*} => C_q <=_i F for open-edge q near q*.
(END) RK §2.2 / G3 Lemma 13.1: at the boundary of {C_q = D_j} on [e_i,e_j], approaching open-edge selections have
      both world-i thresholds -> inf (mirror: -> 0 at the boundary of {C_q = D_i}).
(X2), (X2') P1A Thm 3.1 (X2) (re-checked in Thm 5.6 below) and P1A Lemma 4.1 (X2'), whose AC-pair hypothesis
      holds unconditionally by LH 5.1 (RLH: CORRECT after merging M5).
(KKMb) r2 SETTING: V undominated => V ~_k C_{p_V} at every k for some full-support p_V.
(OP) P1C Lemma 3.3 (ordinal primaries blind on a t-determining region are constant on edge models).

## 2. The flip lemma in invariance form; one triple suffices

**Lemma 2.1 (flip invariance). PROVED.** Let E in F_12, let X_1 subset B_0(E) and X_3 subset P_3 be non-null with
acc_3(X_3, X_1) [V + o_12(X_3) + o_23(X_1) <=_3 V], and let G subset T_0(E) be a finite union of sets Q_1..Q_r
with acc_2(Q_i, X_3) [V + o_13(Q_i) + o_12(X_3) <=_2 V]. Then for every W subset T_0(E):
   acc_1(X_1, W)  =>  acc_1(X_1, W \ G).
Proof. Suppose acc_1(X_1, W) and not acc_1(X_1, W \ G). Put W_0 := W \ G, W_k := W_0 u ((Q_1 u ... u Q_k) n W),
so W_r = W, and the increments R_k := W_k \ W_{k-1} subset Q_k satisfy acc_2(R_k, X_3) ((G): less debt_2).
Let k* >= 1 be least with acc_1(X_1, W_{k*}). Then not acc_1(X_1, W_{k*-1}), so (XOR, "at least one" half,
W_{k*-1} subset T_0(E), X_1 subset B_0(E)) acc_2(W_{k*-1}, X_1). Put d := o_23(X_1) + o_13(W_{k*}) + o_12(X_3)
(supports in P_1, P_2, P_3: disjoint; V + d regular).
 World 1: V + d = [V + o_23(X_1) + o_13(W_{k*})] + o_12(X_3), and o_12 on the non-null X_3 is credit_1; strict
  (G): V + d <_1 V + o_23(X_1) + o_13(W_{k*}) <=_1 V.
 World 2: V + d = [V + o_13(W_{k*-1}) + o_23(X_1)] + [o_13(R_{k*}) + o_12(X_3)]; the bracketed context is silent
  on R_{k*} u X_3, so by (IB) and acc_2(R_{k*}, X_3), V + d <=_2 V + o_13(W_{k*-1}) + o_23(X_1) <=_2 V.
 World 3: V + d = [V + o_12(X_3) + o_23(X_1)] + o_13(W_{k*}); o_13 on P_2 is credit_3; (G) and acc_3(X_3,X_1):
  V + d <=_3 V.
So V + d dominates V, contradicting V undominated. ∎
(This is the mechanism of B Lemma B.2 / B Thm 3.6 (RB5 §4, §7: CORRECT), with an arbitrary starting set W_0.)

**Corollary 2.2 (single-triple criterion; sharpening of B Thm 3.6 and of LH §7 R4). PROVED.** V is dominated as
soon as, for SOME E in F_12, some non-null X_1 subset B_0(E), X_3 subset P_3 and W subset T_0(E):
   (i) acc_3(X_3, X_1),  (ii) acc_1(X_1, W),  (iii) W in J^{(2)}[X_3].
Proof. Lemma 2.1 with G := W gives acc_1(X_1, empty), i.e. V + o_23(X_1) <=_1 V, contradicting strict (G). ∎
Relation to (M2*). If some non-null T subset T_0(E) satisfies (M2*) (T in J^{(2)}[Y_c] for EVERY c), the
criterion holds: by (LH) at world 1 there is a strictly SI pair (A, T') with T' subset T; by (Y-d) at world 1 on
edge 13 (P1A 2.1: tails on both edges) there is b with X_1 := B_0(E) n {t_13 > b} non-null and X_1 <=^1_d A,
so acc_1(X_1, T') and, by (G), acc_1(X_1, T); by (M1) there is c with acc_3(Y_c, X_1); (M2*) at this ONE c gives
(iii) with X_3 := Y_c, W := T. So the criterion needs (M2*) at a single level c = c(T), determined by T through
the chain T -> A -> b -> X_1 -> c; B Thm 3.6 asked for every level (it was written before (LH) was available,
to derive credit-nullity; with (LH) one level suffices). The criterion is strictly weaker than (M2*) also in
that X_1, X_3, W may be any sets with (i)-(iii).

**Corollary 2.3 (absorption; what a counterexample must satisfy at every E). PROVED.** Let V be undominated,
E in F_12, X_1, X_3 as in Lemma 2.1, G := J^{(2)}[X_3] n 2^{T_0(E)}, and
   N := {W subset T_0(E) : not acc_1(X_1, W)} = {W subset T_0(E) : acc_2(W, X_1)}   (XOR, both halves).
Then G subset N and N + G = N (W in N, Q in G => W u Q in N). In words: world 2's debt on any set that is
X_3-compensable in pieces is compensated by X_1 alone, and adding such debt never flips world 2's verdict on
any trade (W, X_1); dually world 1's credit on T_0(E) "lives" on world-2-bad sets: removing world-2-good sets
never flips world 1's acceptance of X_1-debt.
Proof. Let W in N, Q in G, and suppose acc_1(X_1, W u Q). Lemma 2.1 with W' := W u Q and G := Q gives
acc_1(X_1, (W u Q) \ Q); since (W u Q) \ Q subset W, (G) (more credit_1) gives acc_1(X_1, W), i.e. W not in N:
contradiction. So W u Q in N; with W := empty (empty in N: o_23(X_1) is pure debt_1) G subset N. The identity
N = {W : acc_2(W, X_1)} is XOR (at least one: E competitive on {1,2}; at most one: V undominated, X_1 non-null). ∎
Reading. In the language of the race (§3, §6): for the decreasing families X_1^n := B_0(E) n {t_13 > n},
X_3^n := Y_{c(X_1^n)}, the ideals G_n := J^{(2)}[X_3^n] and the down-sets N_n decrease, G_n subset N_n, and
(LH) at world 1 gives intersection_n N_n = {null}. A contradiction needs ONE W in G_n \ N_n: Corollary 2.3 says
this never happens; the obstruction is entirely in the relative speed at which G_n and N_n shrink.

## 3. The far end of edge 12 (idea (iv)): one-piece goodness, and the race that remains

Setting: q_e := min{q in [e_1,e_2] : C_q = D_2}. The set {q : C_q = D_2} = A_2(D_2) n [e_1,e_2] (D_2 is the
unique <=_2-minimum among regular models, strict (G)) is closed, contains e_2, not e_1 (RK §2.2), so there are
q_m in the open edge, q_m -> q_e, C_m := C_{q_m} != D_2, and beta_m -> inf (RK §2.2 / G3 13.1). Two cases:
 (a) alpha_m < inf along a subsequence (then C_m is interior: 0 < beta_m <= alpha_m < inf; this is (BR_2^{21}),
     the D_2-end of edge 12 approached with non-null world-2 debt D_12 n {t_12 > alpha_m});
 (b) C_m = E_2(beta_m) for all large m (no interior selection near q_e).

**Proposition 3.1 (far-end tails are one good piece). PROVED.** In case (a), for every non-null X_3 subset P_3
there is m_0 such that for all m >= m_0 (along the subsequence)
   V + debt_2(D_12 n {t_12 > alpha_m}) + cred_2(X_3) <_2 V;
in particular T_0(C_m) in J^{(2)}[X_3] as a single piece. No V-hypothesis, no completeness is used.
Proof. Step 1 ((S_SI^i) at world 2, P1A Lemma 4.2 in world 2's frame on [e_2,e_1]). Let Q subset D_12 n {t_12 < 1/c'}
be non-null, c' > 0. F := D_2 with its advice silenced on Q. On D_12, D_2 gives the option good at 2, i.e. debt_1,
so F <_1 D_2 = C_{q_e} (strict (G)). (T2) at q_e with the roles of 1 and 2 exchanged (q_e not in the closed
A_1(F); competitiveness of C_q, q in the open edge, on {1,2}) gives C_m <=_2 F for large m. For m with
beta_m > 1/c', world 2 sees on D_12: C_m = credit_2 on {t_12 < beta_m} (which contains Q), silence on
[beta_m, alpha_m], debt_2 on tail_m := D_12 n {t_12 > alpha_m}; F = credit_2 on D_12 \ Q, silence on Q; both give
o_12 on P_3. (IB) on the difference set Q u (D_12 n {t_12 >= beta_m}):
   V + cred_2(Q) + debt_2(tail_m) <=_2 V + cred_2(D_12 n {t_12 >= beta_m}) <_2 V
(the last by strict (G)). So (tail_m, Q) is strictly SI at world 2 for all large m.
Step 2 (credit transport at world 2). By (Y-c) at world 2 (LH §2 (I1): low cones of BOTH edges at world 2 are
credit-lighter than any non-null set; here T := X_3 subset P_3 subset D_23, and the edge-21 cone is reached by
P1A 2.2's transport) there is a > 0 with every subset of L^2_1(a) = D_12 n {t_12 > 1/a} being <=^2_c X_3. Take
Q := D_12 n {1/a < t_12 < 2/a} (non-null) and c' := a/2 in Step 1. For m large, alpha_m >= beta_m > 2/a, so
tail_m n Q = empty, and tail_m n X_3 = empty (D_12 vs P_3). With the context debt_2(tail_m) (silent on Q u X_3):
   V + debt_2(tail_m) + cred_2(X_3) <=_2 V + debt_2(tail_m) + cred_2(Q) <_2 V.
T_0(C_m) = P_2 n tail_m subset tail_m; less debt keeps the pair SI. ∎

**Corollary 3.2 (far-end criterion and the far-end race). PROVED.** Assume V undominated and case (a).
 (i) For every non-null X_3 subset P_3, every m >= m_0(X_3) and every non-null X_1 subset B_0(C_m) with
     acc_3(X_3, X_1): world 1 strictly rejects (X_1, W) for every W subset T_0(C_m), and world 2 accepts
     (T_0(C_m), X_1).
 (ii) Consequently V is dominated (contradiction) as soon as for SOME X_3, some m >= m_0(X_3) and some non-null
     X_1 subset B_0(C_m): acc_3(X_3, X_1) and acc_1(X_1, T_0(C_m)).
 (iii) For each fixed non-null Q subset P_1 n {t_12 < 1/c'}: for all large m, Q subset B_0(C_m) (beta_m -> inf)
     and acc_2(T_0(C_m), Q) (Step 1 of Prop 3.1, less debt), hence (XOR) world 1 rejects (Q, T_0(C_m)).
Proof. (i) Cor 2.2/Lemma 2.1 at E := C_m with G := T_0(C_m) (Prop 3.1), plus XOR. (ii) restates (i).
(iii) Step 1 of Prop 3.1 and XOR (at most one). ∎
Reading (the race at the far end, precisely). Order of choices in (ii): X_3 first (it may be as light as we like
for world 3), then m >= m_0(X_3), then X_1. By (iii) any X_1 with acc_1(X_1, T_0(C_m)) must leave every fixed
cone {t_12 < 1/c'} as m grows, i.e. sit in P_1 n {b_m < t_12 < beta_m} with b_m -> inf (world 1's edge-12 high
tail = world 2's low cone of edge 21; both lightness facts are consistent with this). On such sets world 3's
coordinate t^3_1 = |g_3|/g_1 is free, so world 3 sees X_1 TRANSVERSALLY: nothing known forces world 3's credit on
P_1 n {t_12 > b} n {t^3_1 in [1,2]} to stay above the debt on the fixed X_3 as b -> inf (and §5, Lemma 5.2,
shows it does become light relative to fixed sets of the edge-13 XOR region). So in a counterexample with case (a):
for every X_3 and m >= m_0(X_3), every X_1 subset B_0(C_m) whose world-3 credit covers X_3 is so large for world 2
that world 2 accepts (T_0(C_m), X_1). Three rates compete: world 1's credit on T_0(C_m) (-> 0 by (S_AC^i)),
world 3's transverse credit on world-1 tails, world 2's credit on world-3 tails; no available result orders them.
Case (b): near q_e every selection is E_2(beta) (silent, e_2 in its credal set); Lemma 2.1 is vacuous there
(T_0 empty) and the interior edge-12 selections stay away from q_e; competitiveness of E_2(beta) only gives
"at least one of worlds 1, 2 weakly rejects o_23(Z) + o_13(W)" for Z, W in its silence, with no exact XOR.
Mirror: at the D_1-end of edge 12, under (BR_1^{12}), B_0(C_m) is one good piece for world 1 relative to every
P_3-credit (same proof in world 1's frame), and the mirror of Cor 3.2 (orientation (2,1,3)) holds.

## 4. Where world-2 acceptances of (P_2-debt, P_3-credit) can come from (ideas (ii), (iii))

**Lemma 4.1 (competitiveness at a selection whose support contains world 1 never yields acc_2(Q,Y)). PROVED.**
Let C be any selection competitive on S with 1 in S (every full-support selection, every edge-12 or edge-13
selection), X regular, and suppose the competitiveness inference "X <_l C for all l in S \ {k} => C <=_k X" is
used with k = 2 and its conclusion C <=_2 X is, by (IB), the statement acc_2(Q, Y) for some Q subset P_2,
Y subset P_3 (i.e. on their difference set C gives o_13 on Q, o_12 on Y and X is silent). Then the premise fails
at l = 1, since C <_1 X (credit_1 on Q u Y). Hence such acceptances can be produced by competitiveness only at
selections with support inside {2,3}, i.e. by the edge-23 XOR [F in F_23, Q subset P_2 n {s < beta^2_F},
Y subset P_3 n {s > alpha^2_F}: acc_2(Q,Y) iff not acc_3(Y,Q)]. The other sources are closedness (the
yardstick lemmas, (S_SI^i)), (LH)/(DH) (existence statements), and composition/transitivity.
Proof. Immediate from the option table and the definition of competitiveness. ∎
[This is the precise sense in which idea (iii) fails: on P_2 worlds 1 and 3 agree, so a full-support
selection can force world 2 to REJECT moves toward o_13 that worlds 1, 3 both strictly like, but never to
ACCEPT o_13-debt against P_3-credit; and world 1 always likes o_12 on P_3 as well.]

**Proposition 4.2 (what the local sources cover). PROVED.** Let E in F_12, T subset T_0(E), c > 0.
 (a) There is b(c) < inf with T n {s > b(c)} in J^{(2)}[Y_c] as one piece ((LH) at world 2 for Y_c, then (Y-d) at
     world 2 on edge 23; completeness of world 2).
 (b) If (BR_2^{23}) holds (the D_2-end of edge 23 is approached by edge-23 selections F_m with world-2 debt
     thresholds beta^2_m > 0), there is sigma(c) > 0 with P_2 n {s < sigma(c)} in J^{(2)}[Y_c] as one piece.
 (c) The only other world-2 source of acc_2(Q, Y), Y subset Y_c, by competitiveness is the edge-23 XOR, which
     requires Q subset {s < beta^2_F} and Y subset {s > alpha^2_F}, hence Q subset {s < 1/c}: it covers no more
     than (b). So for every c the "uncovered middle" T n {sigma(c) <= s <= b(c)} is where (M2*) must be decided,
     and it exhausts T as c -> inf.
Proof. (a) (LH) gives a strictly SI pair (A, Y') at world 2 with Y' subset Y_c, A non-null; (Y-d) gives b with
every subset of H^2_3(b) <=^2_d A; for B subset T n H^2_3(b) (B n Y' = empty): V + debt_2(B) + cred_2(Y_c)
<=_2 V + debt_2(B) + cred_2(Y') <=_2 V + debt_2(A) + cred_2(Y') <_2 V.
(b) (Y-c) at world 2 for Y_c: a > 0 with every subset of L^2_1(a) <=^2_c Y_c. Q := P_2 n {|g_2| < a g_1} n
{s in (1,2)} is non-null, Q subset L^2_1(a) n D_23 n {s > 1}. (S_SI^i) at world 2 on [e_2,e_3] (P1A 4.2 in world
2's frame; RK §2.4): (D_23 n {s < beta^2_m}, Q) strictly SI for large m. Restrict the debt to
P_2 n {s < beta^2_m} (disjoint from Y_c and, for beta^2_m < 1, from Q) and replace the credit Q by Y_c (Q <=^2_c Y_c;
(IB) with that debt as context). sigma(c) := beta^2_m for such an m.
(c) Lemma 4.1 and the shape of the edge-23 XOR regions (alpha^2_F < 1/c forces beta^2_F < 1/c). ∎
[This is idea (ii) made precise: the edge opposite world 1 (edge 23, the one B Thm B.5 used) is exactly where
(M2*) lives — (M2*) is a relative fineness of world 2 on D_23, P_2 against P_3 — but its own XOR only reaches the
two ends {s -> 0}, {s -> inf} of world 2's frame, and world 2's heavy germ (B Prop 4.2 / LH 5.6(c)) sits at a
bounded level of s.]

**Remark 4.3 (the full-support selection tied with V). PROVED.** By KKMb (r2 SETTING; G3 standing) there is a
full-support index p_V with C_V := C_{p_V} ~_k V at every world k. Let d_V be C_V's advice (as a change from V)
and d' its restriction to any measurable R, d'' := the rest. For every k: acc_k(d'') <=> V <=_k V + d' (add d' in
context, (IB), and V + d_V ~_k V); symmetrically with >= in place of <=. Hence V undominated implies: for every
such d' either SOME world STRICTLY accepts d', or d' is a tie (V + d' ~_k V) at all three worlds [if no world
strictly accepts d', then V + d'' <=_k V at every k, and V + d'' does not dominate V only if all these are ties]
(a strict "anti-TRI" principle on C_V's triangle-advice set). To force world 2 one needs worlds 1 and 3 not to
strictly accept d'; since o_13 and o_12 are credit_1, d' must contain world-1 debt (o_23 on P_1, o_2 on P_2 or o_3
on P_3), so the acceptance forced on world 2 is of the bundled form acc_2(Q, Y u B) with B subset P_1 — the same bundling as
the edge-12 XOR — and it is vacuous if C_V = V (credal set Delta, allowed: F_notes Prop 6.2 in the sub-case).
This does not reach (M2*) (Lemma 4.1's obstruction, in strict form).

## 5. Idea (i): triangle trades on six tail families; XOR couplings; holonomy rigidity

Standing for §5: V undominated, and fixed interior selections E in F_12 (thresholds alpha_E, beta_E in t_12),
E' in F_13 (alpha', beta' in t_13), F in F_23 (alpha^2, beta^2 in s); they exist in a counterexample (B Cor B.6,
LH 5.8(i)). Fix bounded open intervals with closures in (0,inf): I subset (0,beta_E), I' subset (alpha_E,inf),
J subset (0,beta'), J' subset (alpha',inf), K subset (0,beta^2), K' subset (alpha^2,inf), and for x >= x_0:
  A(x)  := P_1 n {t_12 > x} n {t_13 in J}     A'(x) := P_1 n {t_13 > x} n {t_12 in I}      (o_23: debt_1)
  D(x)  := P_2 n {s > x} n {t_12 in I'}       D'(x) := P_2 n {t_12 < 1/x} n {s in K}       (o_13: debt_2)
  C(x)  := P_3 n {t_13 < 1/x} n {s in K'}     C'(x) := P_3 n {s < 1/x} n {t_13 in J'}       (o_12: debt_3)
Each is non-null (positive joint density of the two ratios on its region) and decreasing in x; x_0 is taken so
large that A(x) n A'(x') = D(x) n D'(x') = C(x) n C'(x') = empty. Each family is a tail of its owner on one edge:
A, A' are world 1's high tails of edges 12, 13; D, D' world 2's of edges 23, 21; C, C' world 3's of edges 31, 32.
Lightness (from (Y-d), (Y-c); PROVED in the cited lemmas): A is debt_1-light and credit_2-light (L^2_1), A'
debt_1/credit_3-light (L^3_1), D debt_2/credit_3-light (L^3_2), D' debt_2/credit_1-light (L^1_2), C
debt_3/credit_1-light (L^1_3), C' debt_3/credit_2-light (L^2_3). The third world sees each family TRANSVERSALLY
(its frame coordinate on that set is bounded): world 3 on A, world 2 on A', world 1 on D, world 3 on D', world 2
on C, world 1 on C'.

**Lemma 5.1 (XOR couplings). PROVED.** For all x, y >= x_0:
 (k1) acc_1(A'(x), D(y)) <=> not acc_2(D(y), A'(x))      [XOR at E: A' subset B_0(E), D subset T_0(E)];
 (k2) acc_1(A(x), C'(y)) <=> not acc_3(C'(y), A(x))      [XOR at E': A subset P_1 n {t_13 < beta'}, C' subset
                                                           P_3 n {t_13 > alpha'}; strictness witness world 2];
 (k3) acc_2(D'(x), C(y)) <=> not acc_3(C(y), D'(x))      [XOR at F: D' subset P_2 n {s < beta^2}, C subset
                                                           P_3 n {s > alpha^2}; strictness witness world 1].
Proof. G3 Lemma 3.1 (RB5 §2 (I1)) relabelled; the regions are those of the option table (checked: an edge-13
model gives o_23 on P_1 below beta' and o_12 on P_3 above alpha'; an edge-23 model gives o_13 on P_2 where
s < beta^2 and o_12 on P_3 where s > alpha^2). ∎

**Lemma 5.2 (XOR turns tail lightness into transverse lightness). PROVED.** For every fixed x >= x_0 and all
large y:  not acc_1(A'(x), D(y));  not acc_3(C'(x), A(y));  not acc_2(D'(x), C(y)).
In words: world 1's transverse credit on D(y), world 3's on A(y), world 2's on C(y) become lighter than any fixed
debt of the XOR partner family. Moreover, for every member Y of a credit family and every debt family X of the
same world, acc_k(X(x), Y) for all large x (this is what makes every h_{XY} below finite).
Proof. Last sentence: (LH) at world k for the credit Y gives a strictly SI pair (A_k, Y'), Y' subset Y; X(x) lies
in a high tail of world k, which is <^k_d A_k for large x ((Y-d)); X(x) n Y' = empty (different regions); so
V + debt_k(X(x)) + cred_k(Y) <=_k V + debt_k(X(x)) + cred_k(Y') <_k V + debt_k(A_k) + cred_k(Y') <_k V.
First display: by the last sentence acc_2(D(y), A'(x)), acc_1(A(y), C'(x)), acc_3(C(y), D'(x)) for large y; then
(k1), (k2), (k3) (the "at most one" halves) give the three rejections. ∎

**Lemma 5.3 (no tail cycles). PROVED.** Neither
 (Z1) acc_1(A(x), D(y)), acc_2(D(y), C(z)), acc_3(C(z), A(x))  for some x, y, z, nor
 (Z2) acc_1(A'(x), C'(u)), acc_3(C'(u), D'(w)), acc_2(D'(w), A'(x))  for some x, u, w.
Proof. B Lemma 3.1 (TRI), orientations (1,2,3) and (1,3,2), with X_1, X_2, X_3 the three non-null sets. ∎

Threshold functions. For a debt family X of world k and a credit family Y (from the list) put
h_{XY}(y) := inf{x >= x_0 : acc_k(X(x), Y(y))}; finite by Lemma 5.2's last sentence; {x : acc_k(X(x), Y(y))} is an
up-ray with infimum h_{XY}(y) (less debt is better), and h_{XY} is nondecreasing. The twelve used:
world 1: h_{AD}, h_{A'D}, h_{AC'}, h_{A'C'}; world 2: h_{DC}, h_{DA'}, h_{D'C}, h_{D'A'}; world 3: h_{CA}, h_{CD'},
h_{C'A}, h_{C'D'}.
Hypothesis (TC) ("tail continuity"): on a ray [x_1, inf) each of the twelve is an increasing homeomorphism onto a
ray, and the world-internal matchings agree:
  h_{A'C'} = h_{A'D} o h_{AD}^{-1} o h_{AC'},  h_{D'A'} = h_{D'C} o h_{DC}^{-1} o h_{DA'},  h_{C'D'} = h_{C'A} o h_{CA}^{-1} o h_{CD'}
(each world matches its two debt families "at equal value" through either credit family; this is automatic when
each world's debt order between its two debt families and its credit order between its two credit families are
continuous along the families, but it is ASSUMED here).

**Proposition 5.4 (holonomy rigidity). PROVED (under (TC)).** Let H_1 := h_{AD} o h_{DC} o h_{CA} and
H_2 := h_{A'C'} o h_{C'D'} o h_{D'A'}. Under (TC) and V undominated:
 (a) h_{DA'} = h_{A'D}^{-1}, h_{C'A} = h_{AC'}^{-1}, h_{CD'} = h_{D'C}^{-1}, and H_2 = Psi o H_1^{-1} o Psi^{-1} with
     Psi := h_{A'D} o h_{AD}^{-1} (on a ray);
 (b) H_1 = id on a ray (trivial holonomy around the triangle of worlds);
 (c) for every x on that ray, with z := h_{CA}(x), y := h_{DC}(z) (so h_{AD}(y) = x), at least one of
     acc_3(C(z), A(x)), acc_2(D(y), C(z)), acc_1(A(x), D(y)) fails ("unattained threshold"); likewise for (Z2).
Proof. (a) Take (k1). If x > h_{A'D}(y) then acc_1(A'(x), D(y)), so not acc_2(D(y), A'(x)), so y <= h_{DA'}(x);
if x < h_{A'D}(y) then not acc_1, so acc_2(D(y), A'(x)), so y >= h_{DA'}(x). With g := h_{A'D}^{-1}: y < g(x) =>
y <= h_{DA'}(x) and y > g(x) => y >= h_{DA'}(x); letting y -> g(x) from both sides, h_{DA'}(x) = g(x). Same for
(k2), (k3). Substituting the three matchings and the three inverse relations:
 H_2 = [h_{A'D} h_{AD}^{-1} h_{AC'}] [h_{AC'}^{-1} h_{CA}^{-1} h_{D'C}^{-1}] [h_{D'C} h_{DC}^{-1} h_{A'D}^{-1}]
     = h_{A'D} h_{AD}^{-1} h_{CA}^{-1} h_{DC}^{-1} h_{A'D}^{-1} = h_{A'D} (h_{DC} h_{CA} h_{AD})^{-1} h_{A'D}^{-1}
(composition from the right; all maps increasing homeomorphisms between rays, compositions taken on rays far
enough out), and h_{DC} h_{CA} h_{AD} = h_{AD}^{-1} H_1 h_{AD}, so H_2 = Psi H_1^{-1} Psi^{-1}.
(b) If H_1(x) < x for some x on the ray, continuity gives z > h_{CA}(x) and y > h_{DC}(z) with h_{AD}(y) < x;
then acc_3(C(z), A(x)), acc_2(D(y), C(z)), acc_1(A(x), D(y)) (each argument lies strictly inside its up-ray):
(Z1), contradicting Lemma 5.3. So H_1 >= id; likewise H_2 >= id. By (a), H_2 >= id on a ray means
H_1^{-1}(v) >= v for v on a ray, i.e. H_1 <= id there. Hence H_1 = id on a ray.
(c) At the threshold triple all three acceptances together would be (Z1). ∎

**Corollary 5.5 (every tail level carries a heavy germ). PROVED (under (TC)).** In the situation of Prop 5.4(c),
choose "extras" x'', w, u with STRICT acceptances acc_1(A'(x''), C(z)), acc_2(D'(w), A(x)), acc_3(C'(u), D(y))
(they exist: (LH) at the world for the credit set, then (Y-d) with its strict form, LH §2 (I2)). Then there is a
world k whose threshold at the triple is unattained and such that EVERY band at that threshold germ is strictly
AC against the leftover credit L_k:
  k = 1: (A(x) \ A(x'), L_1) for all x' > x,   L_1 := C'(u) u D'(w);
  k = 2: (D(y) \ D(y'), L_2) for all y' > y,   L_2 := A'(x'') u C'(u);
  k = 3: (C(z) \ C(z'), L_3) for all z' > z,   L_3 := D'(w) u A'(x'').
Proof. Otherwise every unattained world k has a band b_k at its germ with acc_k(b_k, L_k) (put b_k := empty for
attained worlds, with x' := x etc.); acceptances of smaller bands follow by (G). Let
 d := o_23(A(x) u A'(x'')) + o_13(D(y) u D'(w)) + o_12(C(z) u C'(u)).
World 1 sees debt on A(x) u A'(x''), credit on the four other sets, and V + d is the composition of the disjointly
supported accepted changes (A(x'), D(y)) [x' > x = h_{AD}(y), or attained], (b_1, L_1), (A'(x''), C(z)) [strict]:
V + d <_1 V. World 2: (D(y'), C(z)), (b_2, L_2), (D'(w), A(x)): V + d <=_2 V (strict). World 3: (C(z'), A(x)),
(b_3, L_3), (C'(u), D(y)): V + d <=_3 V. (Disjointness: the six sets are pairwise disjoint by the choice of x_0.)
So V + d dominates V. ∎
Reading. Under (TC) a counterexample needs, at EVERY level x of a ray, one world with a heavy right debt germ of
one of its tail families (A, D or C) at the corresponding level, heavy relative to a specified light credit; by
pigeonhole one world has such germs at uncountably many levels of one family (h_{AD}, h_{CA} are homeomorphisms).
Without (TC), discontinuities of the thresholds are themselves heavy germs (a flat piece of h_{XY} is a debt germ
of X heavy relative to a credit band of Y; a jump is a credit germ of Y). So in every case the triangle trades
on tails force heavy germs ON THE TAIL FAMILIES; they do not force a contradiction. The novelty relative to B/LH:
(1) the obstruction can be moved from the interior of T_0(E) (where B Prop 4.2 and LH 5.6(c) put it) to the
tails of all six edge-region pairs, where each world is light in two of the three views; (2) the race of §2/§3
disappears in Cor 5.5 — all sets there are fixed before the final comparison — but is replaced by a
germ-at-every-level requirement.
Heuristic check (PLAUSIBLE; not used). If every threshold were a power law h_{XY}(y) ~ k_{XY} y^{e_{XY}}, the three
couplings (k1)-(k3) force e_{A'D} e_{DA'} = e_{AC'} e_{C'A} = e_{D'C} e_{CD'} = 1 and the matchings force
e_{A'C'} = e_{A'D} e_{AC'}/e_{AD} etc.; then the cycle exponents Pi_1 := e_{AD} e_{DC} e_{CA} and Pi_2 satisfy
Pi_1 Pi_2 = 1, and a weighted sum of the two cycle constants vanishes identically (computed by hand; it is (a)
in logarithmic coordinates). So one of (Z1), (Z2) holds unless both are exactly borderline — the power-law
shadow of (b).


**Theorem 5.6 (tail continuity + generically comparable crossings => V dominated). PROVED.** Let n = 3, all
rankings complete with (G), (IB), (S). Suppose that for some interior E, E', F and intervals as above (TC) holds,
and that for each k the set NK_k of levels NOT covered on the edge [e_k, e_{k+1}] (indices mod 3: edges 12, 23,
31), in world k's own frame (t_12 for k = 1; s = t^2_3 for k = 2; t^3_1 = |g_3|/g_1 for k = 3), is meagre in
(0,inf). Here a level z is COVERED if some index q* of that edge has world-k debt threshold beta^{(k)}_{q*} = z and
is the limit of open-edge indices q_m with C_{q_m} >=pw_k C_{q*} (world-k-worse) and beta^{(k)}_{q_m} > z. Then V is
dominated. (By the symmetric argument — Prop 5.4(c) for (Z2) and the analogue of Cor 5.5 with the roles of the
two orientations exchanged — the same holds with the families A', D', C' and the edges 13, 21, 32.)
Proof. Suppose V undominated. Let R be the ray of Prop 5.4(b), x in R, z := h_{CA}(x), y := h_{DC}(z). By Cor 5.5
some world k is unattained at the triple and has a heavy right debt germ at the corresponding level — x for
k = 1 (bands A(x) \ A(x') subset D_12 n {x < t_12 <= x'}), y for k = 2 (bands D(y) \ D(y') subset
D_23 n {y < s <= y'}), z for k = 3 (bands C(z) \ C(z') subset D_31 n {z < t^3_1 <= z'}) — in the sense that every
band is strictly AC against L_k. By (LH) at world k there is a strictly SI pair (A_k, L'_k) with L'_k subset L_k;
if some band b were <=^k_d A_k, then V + debt_k(b) + cred_k(L_k) <=_k V + debt_k(b) + cred_k(L'_k)
<=_k V + debt_k(A_k) + cred_k(L'_k) <_k V (contexts silent on the sets compared; b misses L'_k, region reasons),
contradicting heaviness. So the right germ at that level is A_k-heavy (P1A §1 sense, restricted to a slab;
bands of the full edge band contain the slab bands, so a full band <=_d A_k would do). If the level were covered,
P1A Thm 3.1 (X2) (silent q*) or P1A Lemma 4.1 (X2') (precise q*, with the AC pair supplied unconditionally by
LH 5.1) — both in world k's frame; (X2) re-checked here: F := C_{q*} + debt(Z'), Z' a transported yardstick
<=_d A_k in the common silence, (T2) gives C_{q_m} <=_k F, and C_{q*} + debt(band) <=pw_k C_{q_m} gives
band <=_d Z' <=_d A_k — would give a band at the germ <=_d A_k. Hence the level lies in NK_k. Therefore
R subset NK_1 u y(.)^{-1}(NK_2) u z(.)^{-1}(NK_3), where x -> z(x) = h_{CA}(x) and x -> y(x) = h_{DC}(h_{CA}(x)) are
homeomorphisms between rays (TC); preimages of meagre sets under homeomorphisms are meagre, so the ray R would be
meagre, contradicting the Baire category theorem. ∎
Remarks. (1) The hypothesis on the edges fails on stretches where the threshold path jumps (jumped-over levels
form intervals of uncovered levels) or crosses an interval of levels only nestedly (K Prop 4.8); it holds on
jump-free paths that are monotone except at a meagre set of levels. The point of Theorem 5.6 is that Cor 5.5
produces heavy germs at EVERY level of a ray, so countably (even meagrely) many exceptional crossings no longer
suffice for a counterexample — in contrast to the single-germ analyses of P1A §7, K §§3-4, where one surviving
level is enough. (2) Neither hypothesis implies fineness of any world as far as I can see; (TC) is a continuity
statement about cross-region tail comparisons only (it is satisfied, for instance, in the fine case with
continuous thresholds). OPEN: whether (TC) follows from (S) + V undominated.

## 6. What a counterexample must now look like (necessary conditions; PROVED unless marked)

n = 3, complete (G)+(IB) rankings, (S), V undominated. In addition to LH 5.8 (no fine world, no fine edge, no
tame world, (LH)+(DH) everywhere, an XOR flip with a heavy germ at every two-sided edge selection):
 (N1) [Cor 2.3] at every E in F_12 and every admissible pair (X_1, X_3) (acc_3(X_3, X_1)): G(X_3) subset N(X_1)
      and N(X_1) + G(X_3) = N(X_1): world 2's X_3-compensable debt on T_0(E) is absorbed by X_1-credit alone, and
      world 1's credit on T_0(E) relevant to X_1-debt lives on world-2-bad sets. Same on every edge by relabelling.
 (N2) [Cor 3.2] if the D_2-end of edge 12 is rich (case (a)), the far-end race: for every X_3 and m >= m_0(X_3),
      world 2 accepts (T_0(C_m), X_1) for every X_1 subset B_0(C_m) with acc_3(X_3, X_1).
 (N3) [Prop 4.2, Lemma 4.1] world 2's heavy part of T_0(E) relative to Y_c lies in the "uncovered middle"
      sigma(c) <= s <= b(c), which no competitiveness source at a selection whose support contains world 1 can
      reach.
 (N4) [Prop 5.4, Cor 5.5] under tail continuity (TC): trivial holonomy H_1 = id and, at every level of a ray, a
      heavy right debt germ of one of the tail families A, D, C (and likewise of A', D', C') relative to an
      explicit light credit; without (TC), the discontinuities of the tail thresholds are heavy germs themselves.
 (N5) [§6.1 below; PROVED as stated] the heaviness cannot be "region-lexicographic": an order-separated valuation
      of the triangle options satisfies TRI, all XOR couplings, all yardstick lightness facts and violates (M2*),
      but any world realizing it has a top level blind on a t-determining region and is excluded by P1C Lemma 3.3.

6.1 The order-separated model (evidence for the shape; what kills it). PLAUSIBLE as a description, PROVED as
to the kill. Let Gamma be the Hahn group of formal series sum_n c_n omega^n (omega infinitely large, exponents
in Z bounded above, lexicographic order by the leading exponent), and give every o_{lm}-set X subset P_k (the
triangle option of region P_k) a value v(X) whose leading exponent lies in 3Z + k (region classes disjoint) and
decreases to -inf along every tail family of §5: e.g. with depth(g) := max(|log r_1(g)|, |log r_2(g)|) for the two
ratios of region P_k and shells S_j := {j <= depth < j+1}, v(X) := sum_j mu(X n S_j) omega^{3 phi(j) + k}, phi
integer-valued, strictly decreasing. Let world k accept a triangle
trade iff v(own-region debt) <= v(credit on the other two regions) in Gamma. Then: TRI holds (in any triple the
set of largest leading exponent belongs to one region; its world rejects); every XOR is exact (leading exponents
of different regions never coincide, so ties never occur); every tail family is light in all three views
(leading exponents -> -inf); (LH)/(DH) hold for triangle options; and (M2*) fails for every T (T's pieces at
bounded levels share T's exponent class, which exceeds that of any world-3-admissible X_3). [Checked by hand from
the definitions; this is not a model of the full world orders, which also rank the anti-triangle options.] It is
nevertheless excluded as soon as it is extended to a world order in which the leading coefficient at the
maximal exponent is an ordinal primary (P1C §3; this is the case for every lexicographic extension, the
maximum being attained at the innermost shells): that primary belongs to the world owning the maximal class, is
blind on the two other regions, which are t-determining for its edges, so P1C Lemma 3.3 makes it constant on
edge models, while it separates D_i from D_j. So a counterexample must have
"relative" heaviness with no top level (no coarsening of a world order into a linear order that ignores a
t-determining region), and — by C5 Thm 4.1 and P1C Lemma 2.1 — no ordered-group representation at any world.
6.2 Finite tie data cannot decide (script r5/m2chk/tie_orders.py). Encoding one member of each tail family and
each world's order on its four families as a strict total order, subject to the three XOR couplings, there are
1442 assignments avoiding both tail cycles (Z1), (Z2). So the holonomy argument of Prop 5.4 genuinely needs the
continuum of members (it is a statement about composing threshold MAPS), and at the level of finitely many tied
members nothing is forced.

## 7. Attempts that failed (with the exact reason)

(M2-F1) Idea (iii), full-support selections near an interior edge selection. On P_2 worlds 1 and 3 agree (both
 prefer o_13 > silence > o_2), so a full-support C_p can force world 2 to REJECT moves toward o_13 that worlds 1,
 3 strictly like; it can never force world 2 to ACCEPT o_13-debt against o_12-credit, because world 1 strictly
 likes both (Lemma 4.1). J Prop 1.4 (local redundancy) shows in addition that near an edge index the full-support
 neighbours may copy the edge. The tied full-support selection C_{p_V} gives a strict anti-TRI principle
 (Remark 4.3) but with the same bundling. FAILED for (M2*).
(M2-F2) Idea (ii), the edge opposite world 1 (edge 23). (M2*) is a relative fineness of world 2 on D_23, so edge
 23 is the right place, but its XOR regions force Q subset {s < beta^2_F} whenever Y subset Y_c, i.e. they reach
 only the {s -> 0} end; together with tail lightness at {s -> inf} this leaves the "middle" of T untouched
 (Prop 4.2). FAILED.
(M2-F3) Idea (iv), the far end. At the D_2-end (case (a)) T_0(C_m) is one good piece relative to ANY X_3 (Prop
 3.1) — the strongest form of (M2) one could ask for — but at the same index world 1's credit on T_0(C_m) is
 small ((S_AC^i)), and the needed X_1 must be simultaneously light for worlds 1 and 2 and heavy enough for world
 3 (Cor 3.2): a three-rate race. The own-region analogue of K's far-end transfer (the end where world 2 is in
 debt everywhere: D_1 on edge 12, D_3 on edge 23) is vacuous: world 2's debt yardsticks there lie in the partner's
 credit-light cone, so the transfer only says that world 2's heavy ultrafilter is partner-credit-heavy relative
 to a light set — which the own-region heavy shape already has. FAILED.
(M2-F4) Extremal choice of the interior selection (first interior selection along the edge; or interior
 selections approaching V_12 with beta -> 0, alpha -> inf). At such points (T1) only says that the trade
 (B_0, T_0) is worth less than every fixed credit gain at both worlds, which is consistent with small sets; no
 goodness of T_0 for world 2 relative to P_3-credit follows. FAILED.
(M2-F5) Idea (i), triangle 2-set cycles. They need no fineness at all (TRI is a direct contradiction), and
 Lemma 5.2 shows all transverse credits are light relative to fixed sets, but Prop 5.4 shows that the absence of
 both cycles forces exactly trivial holonomy rather than a contradiction; the residual is pushed into
 unattained thresholds = heavy tail germs (Cor 5.5), and finite tie data are consistent (§6.2). FAILED to
 produce a contradiction unconditionally; gave Theorem 5.6 conditionally.
(M2-F6) Baire/compactness on the race. The race of Cor 2.3 / Cor 3.2 is a comparison of monotone functions
 (f(d) > d for all d is consistent); a Baire argument needs a covering by closed sets of "good" levels, which
 exists only in the (TC) situation of Theorem 5.6. FAILED in general.
(M2-F7) Constructing the own-region heavy structure. The order-separated valuation (§6.1) satisfies every
 constraint on triangle options that I know (TRI, exact XOR on all three edges, lightness of all six tail
 families in all three views, (LH)/(DH), failure of (M2*)), but any lexicographic world order realizing it has a
 top level blind on a t-determining region and is killed by P1C Lemma 3.3; making it top-level-free while keeping
 the race lost at every scale is exactly the open problem. NOT obtained (neither a counterexample nor an
 impossibility proof).

---
# Part 2. Referee report on M2 (RM2)
# RM2 referee report on r5/M2_notes.md (§§2-6)

Referee: independent. Written incrementally; §0 (summary) is filled in last.
Verdicts: CORRECT / CORRECT WITH MINOR FIXES / GAP / WRONG.

Sources read: r5/SETTING5.md (+ r3/SETTING3.md, r3/SETTING4.md, r2/SETTING.md); r5/M2_notes.md (full, under
review); r5/B_notes.md (full) + r5/RB5_referee.md (full); r5/LH_notes.md (full) + r5/RLH_referee.md (full);
r4/P1A_notes.md (full: Lemmas 1.1-1.2, 2.1-2.2, 3.0, Thm 3.1, Lemmas 4.1-4.2, Thm 5.2, §§6, 9-11); r4/P1C_notes.md
§3 (Lemmas 3.0, 3.3, Thm 3.1), §4 (Lemma 4.1); r5/K_notes.md Prop 4.8; r4/N_notes.md Cor 2.4; r5/C5_notes.md Thm 4.1;
r5/m2chk/tie_orders.py (run).
Mechanical checks written for this report: r5/rm2chk/ (see §1).

## 0. Summary

Lemma 2.1 / Cor 2.2: CORRECT (Cor 2.3 CORRECT; minor fixes F3, F4 in the surrounding paragraphs). Prop 3.1:
CORRECT (Cor 3.2 CORRECT; F5). Prop 4.2: (a), (b) CORRECT, (c) CORRECT WITH MINOR FIXES; but Lemma 4.1's "Hence",
§0 S3 and (N3) are WRONG as worded — the note's own Prop 3.1 is a competitiveness source at a selection whose
support contains world 1 that yields world-2 acceptances of (P_2-debt, P_3-credit) at all s-levels of
T n {t_12 > alpha_m}, and (S_SI^ii) sources at world 2 reach bounded s-levels (F6, F7). Remark 4.3 CORRECT (F8).
§5: Lemmas 5.1-5.3, Prop 5.4 (under (TC)), Cor 5.5 and Theorem 5.6 CORRECT; every region, option, (IB) pattern
and composition checked mechanically (r5/rm2chk/, all pass); the Baire step is sound (closed ray, homeomorphic
level maps, meagreness hypothesised in (0,inf)). Two strengthenings, PROVED here: (TC)'s matchings are automatic
(Lemma R1), so (TC) reduces to six maps (TC6); only high levels are used (F9), and at endpoint-family far ends all
high levels are covered (Lemma R3), so Thm 5.6 yields Cor R4: under (TC6), V undominated forces a rich far end with
non-meagre uncovered high levels in each of two specified triples of vertex-ends. Item (6): the hypotheses are not
shown inconsistent with (no fine world/edge, no fa world, (LH)/(DH)) and not vacuous; (TC) fails in the only
explicit candidate (order-separated valuation: step-function thresholds). §6.1: description CORRECT, kill proved
only for top levels blind on a t-determining region ("every lexicographic extension" unproved, F12). §6.2: the
script checks only that 3 XOR equalities + 2 forbidden cycles are satisfiable for one strict (tie-free) order per
world on 4 families (1442 permutation triples = 266 distinct patterns; no lightness, no ties) (F13). The
"next step" claim that jumps are harmless for the Baire argument is false for dense jumps (F14, example §9.1).
No GAP in any proof of a numbered result. Fixes F1-F15 in §10, verdicts in §11.

## 1. Conventions and mechanical checks

Order convention (as in RK/RB5/RLH): X <=_k Y = "X at least as good as Y at world k"; X <_k Y := X <=_k Y and not
Y <=_k X. acc_k(A,T) :<=> V + debt_k(A) + cred_k(T) <=_k V. Completeness is needed exactly to turn "not acc" into
a strict rejection, and to compare two credit (or two debt) sets.
Regions in H = {g_1 > 0}: P_1 = (+,-,-), P_2 = (+,-,+), P_3 = (+,+,-). Triangle options o_23 (P_1), o_13 (P_2),
o_12 (P_3): debt at the owner world of the region, credit at the two others.

Scripts (all in r5/rm2chk/, outputs *_out.txt next to them; all ALL PASS):
 - regions.py (Monte Carlo, 2e6 points): option table; E (edge 12), E' (edge 13), F (edge 23) advice on T_0, B_0,
   the edge-13 and edge-23 XOR regions; the six families A, A', D, D', C, C' of §5: non-null, inside the XOR
   regions claimed in Lemma 5.1, pairwise disjoint for x, x' >= x_0, each a HIGH TAIL of its owner on the stated
   edge and a LOW CONE of the stated second world, transversal for the third; the Thm 5.6 bands lie in
   D_12 n {x < t_12 <= x'}, D_23 n {y < s <= y'}, D_31 n {z < t^3_1 <= z'} (and the mirror bands on edges 13, 21,
   32); Prop 3.1 Step 1: the difference set of (C_m, F) is Q u (D_12 n {t_12 >= beta_m}) with the advice pattern
   claimed (credit_2/silent on Q, silent/credit_2 on the band, debt_2/credit_2 on tail_m, o_12 on P_3 for both);
   Prop 3.1 Step 2 and Prop 4.2(b) sets non-null and inside L^2_1(a); Prop 4.2(c) (the edge-23 XOR region meets
   Y_c iff alpha^2_F < 1/c).
 - compose.py (symbolic): at each world the composition of the accepted changes used in Lemma 2.1 and in Cor 5.5
   (orientation (Z1)) and in the referee's write-out of its (Z2)-analogue (§6.6 below) reproduces exactly the
   debt/credit pattern of the dominating change d, with pairwise disjoint supports and every debt set in the
   world's own region.
 - holonomy.py: the conjugation identity of Prop 5.4(a) for random power-law maps (rel. error 3e-15), and
   H_1 = id => H_2 = id.
 - ties_analysis.py: what r5/m2chk/tie_orders.py establishes (§8.3).

## 2. Item (1): the threshold maps, (TC), "covered"

2.1 Threshold maps. For a debt family X of world k and a credit family Y of world k (i.e. Y lies in a region
other than P_k, so the triangle option on Y is credit_k), h_{XY}(y) := inf{x >= x_0 : acc_k(X(x), Y(y))}.
 - {x : acc_k(X(x),Y(y))} is an up-ray: X(x'') subset X(x) for x'' > x, and V + debt(X(x'')) + cred(Y) is
   pointwise world-k-better than V + debt(X(x)) + cred(Y) (G). Correct. Hence x > h_{XY}(y) => acc and
   x < h_{XY}(y) => not acc (used constantly; correct; nothing is said at x = h, which is the point of
   "attained/unattained").
 - h_{XY} nondecreasing: Y(y2) subset Y(y1) for y2 > y1, less credit. Correct.
 - Finiteness (Lemma 5.2, last sentence): (LH) at k gives a strict SI pair (A_k, Y'), Y' subset Y(y); X(x) lies in
   a high tail of world k ((I2)/(Y-d): tails on BOTH edges at k), so X(x) <^k_d A_0 <=^k_d A_k for large x; X(x)
   and Y' lie in different regions; A_k n Y' = empty. Chain (G), (IB) (context cred_k(Y'), silent on X(x) u A_k),
   SI pair: strict. CORRECT (uses completeness at k through (Y-d), and (LH), i.e. completeness of all worlds).
 The twelve pairs listed are exactly the (debt family, credit family) pairs with the families in the right
 regions (checked against the option table: world 1 debt A, A' in P_1; credit D (P_2), C' (P_3); world 2 debt
 D, D'; credit C (P_3), A' (P_1); world 3 debt C, C'; credit A (P_1), D' (P_2)). CORRECT.

2.2 (TC). As stated: on a ray, each of the twelve maps is an increasing homeomorphism onto a ray, and the three
world-internal matchings hold. The definition is coherent (all compositions are defined on rays far out because
increasing homeomorphisms of rays onto rays are unbounded). Two remarks, both of which STRENGTHEN Thm 5.6:

**Lemma R1 (the matchings are automatic). PROVED (referee).** Let world k be complete with (G), (IB). Let X, X' be
its two debt families and Y, Y' two credit families (pairwise in the regions of §5, so every debt set is
disjoint from every credit set). If h_{XY}, h_{XY'}, h_{X'Y} are increasing homeomorphisms between rays (on a
ray), then on a ray
   h_{X'Y'} = h_{X'Y} o h_{XY}^{-1} o h_{XY'};
in particular h_{X'Y'} is itself an increasing homeomorphism. No assumption on V.
Proof. Fix u far out; x := h_{XY'}(u), y := h_{XY}^{-1}(x), xi := h_{X'Y}(y) =: RHS(u). Let u' < u < u''; then
h_{XY'}(u') < x < h_{XY'}(u'') (strict increase).
 (i) Pick x_1 in (h_{XY'}(u'), x): acc_k(X(x_1), Y'(u')) and not acc_k(X(x_1), Y(y)) (x_1 < x = h_{XY}(y)). If
 V + cred(Y(y)) <=_k V + cred(Y'(u')), then (IB, context debt(X(x_1)), silent on Y(y) u Y'(u')) V + debt(X(x_1)) +
 cred(Y(y)) <=_k V + debt(X(x_1)) + cred(Y'(u')) <=_k V, contradiction. By completeness V + cred(Y'(u')) <_k
 V + cred(Y(y)). Hence, for every x~ with acc_k(X'(x~), Y(y)) (in particular every x~ > xi), (IB) with context
 debt(X'(x~)) gives acc_k(X'(x~), Y'(u')). So h_{X'Y'}(u') <= xi.
 (ii) Pick x_2 in (x, h_{XY'}(u'')): acc_k(X(x_2), Y(y)) and not acc_k(X(x_2), Y'(u'')); as in (i)
 V + cred(Y(y)) <_k V + cred(Y'(u'')), and acc_k(X'(x~), Y'(u'')) => acc_k(X'(x~), Y(y)); so xi <= h_{X'Y'}(u'').
 Thus h_{X'Y'}(u-) <= RHS(u) <= h_{X'Y'}(u+) for every u on the ray. RHS is continuous and strictly increasing
 and h_{X'Y'} is nondecreasing; a jump h(u_0-) < h(u_0+) would give, letting u up to u_0 and u down to u_0,
 RHS(u_0) <= h(u_0-) < h(u_0+) <= RHS(u_0). So h_{X'Y'} is continuous and equals RHS. ∎
Application. World 1 (X, X', Y, Y') = (A, A', D, C'): the first matching of (TC). World 2 (D, D', C, A'): the second,
once h_{DA'} is a homeomorphism; world 3 (C, C', A, D'): the third, once h_{C'A}, h_{CD'} are. By Prop 5.4(a)'s first
sentence (which needs only XOR and that h_{A'D}, h_{AC'}, h_{D'C} are increasing homeomorphisms; re-checked in §6.4)
h_{DA'} = h_{A'D}^{-1}, h_{C'A} = h_{AC'}^{-1}, h_{CD'} = h_{D'C}^{-1}. Hence, with V undominated, completeness and (IB):
 (TC) <=> (TC6): the six maps h_{AD}, h_{DC}, h_{CA}, h_{A'D}, h_{AC'}, h_{D'C} are increasing homeomorphisms
 between rays on a ray.
The note's parenthesis ("this is automatic when ... continuous along the families, but it is ASSUMED here")
should be replaced by Lemma R1. [FIX F1.]

2.3 "Covered" / "crossed comparably". Definition in Thm 5.6: level z is covered on edge [e_k,e_{k+1}] (world k's
frame tau_k = t_12, s = t^2_3, t^3_1 for k = 1, 2, 3) if some index q* has beta^{(k)}_{q*} = z and is a limit of
open-edge indices q_m with C_{q_m} >=pw_k C_{q*} (world-k-worse: alpha_m >= alpha*, beta_m >= beta*) and beta_m > z.
This is EXACTLY the hypothesis of P1A Thm 3.1 (X2) (silent q*) / P1A Lemma 4.1 (X2') (precise q*), transported to
world k's frame; q* is automatically in the open edge (beta = z in (0,inf) excludes D_k = (0,0), D_{k+1} =
(inf,inf)). The informal phrase "crossed comparably from the worse side" (§0, S4) means "approached", not
"passed through"; the formal definition is the one used. CORRECT.
Frames and orientation (checked, regions.py): world 2's debt region on edge 23 is LOW s (s < beta^{(2)}); the
family D(y) = P_2 n {s > y} n {t_12 in I'} is world 2's HIGH s-tail; its bands D(y) \ D(y') are bands of world
2's debt order at level y on D_23, i.e. the germ (y,+) of edge [e_2,e_3] in world 2's frame, which is what (X2) at
world 2 kills. Same for k = 1 (A, edge 12, t_12) and k = 3 (C, edge 31, t^3_1 = 1/t_13). Consistent.
"Light" (§0 S4; Cor 5.5 reading). L_1 = C'(u) u D'(w): D'(w) is credit_1-light (low cone L^1_2), but C'(u) is seen
by world 1 TRANSVERSALLY (t_13 in J') and is not shown to be credit_1-light. Wording: "an explicit credit (one
part light, one transversal)". Cosmetic. [F2]

## 3. §2 of M2: Lemma 2.1, Corollaries 2.2, 2.3

### 3.1 Lemma 2.1 (flip invariance) — CORRECT
Hypotheses actually used: E in F_12 (only for the at-least-one half of XOR); X_1 subset B_0(E) (for XOR); X_3
non-null (strictness at world 1); acc_3(X_3,X_1); pieces Q_i with acc_2(Q_i,X_3); V undominated (once, at the end).
Completeness is NOT used. X_1 need not be non-null for the lemma (if X_1 is null the conclusion is trivial).
 - W_0 := W \ G, W_k := W_0 u ((Q_1 u ... u Q_k) n W); W_r = W (G n W is covered by the Q_i). R_k := W_k \ W_{k-1}
   subset Q_k, pairwise disjoint, disjoint from W_0; acc_2(R_k, X_3) by (G) (less debt_2). CHECKED.
 - k* exists (acc_1 at W_r, not at W_0), k* >= 1; not acc_1(X_1, W_{k*-1}); W_{k*-1} subset T_0(E), X_1 subset
   B_0(E): XOR at-least-one (competitiveness of E on {1,2} against E silenced on W_{k*-1} u X_1, (IB); RB5 §2 (I1))
   gives acc_2(W_{k*-1}, X_1). No completeness, no V. CHECKED.
 - d := o_23(X_1) + o_13(W_{k*}) + o_12(X_3); supports in P_1, P_2, P_3; V + d regular.
   World 1: V + d = [V + o_23(X_1) + o_13(W_{k*})] + o_12(X_3), credit_1 on non-null X_3: strict (G), then
   acc_1(X_1, W_{k*}). World 2: the pair (V + d, V + o_13(W_{k*-1}) + o_23(X_1)) has difference set R_{k*} u X_3 with
   the advice of (V + o_13(R_{k*}) + o_12(X_3), V) (o_13 vs silence on R_{k*}, o_12 vs silence on X_3); (IB) +
   acc_2(R_{k*},X_3), then acc_2(W_{k*-1},X_1): weak. World 3: (G) (o_13 on P_2 is credit_3) and acc_3(X_3,X_1): weak.
   Pattern verified symbolically (compose.py). V + d dominates V. CORRECT.
 (The statement should list "V undominated" explicitly, or say "Standing: V undominated"; it is standing in the
 note's header. Cosmetic.)

### 3.2 Corollary 2.2 (single-triple criterion) — CORRECT
G := W in Lemma 2.1 (pieces of W may be taken inside T_0(E) by heredity of J^{(2)}[X_3]) gives acc_1(X_1, empty),
i.e. V + o_23(X_1) <=_1 V: contradicts strict (G) since X_1 is non-null (o_23 on P_1 is debt_1). So V undominated
is impossible: V is dominated. Uses V undominated only through Lemma 2.1; no completeness.
"Relation to (M2*)": re-derived. (LH) at world 1 (RLH: CORRECT) gives a strict SI pair (A,T'), T' subset T;
(Y-d) at world 1 on edge 13 (P1A 2.1, completeness at 1): D_13 n {t_13 > b} <_d A_0 <=_d A; X_1 := B_0(E) n
{t_13 > b} is non-null PROVIDED beta_E > 0 (positive joint density of (t_12,t_13) on P_1); context cred_1(T') is
silent on X_1 u A (X_1 subset P_1, T' subset P_2, A n T' = empty): acc_1(X_1,T') strictly, then acc_1(X_1,T) (G);
(M1) = LH 5.6(b) (RLH §6.6: CORRECT) gives c with acc_3(Y_c, X_1) (Y_c = P_3 n H^3_2(c) = P_3 n {s < 1/c});
(M2*) at that c gives (iii) with X_3 := Y_c, W := T. CORRECT. Fixes: (a) say "E in F_12 with beta_E > 0 (e.g.
interior)" — X_1 is null if beta_E = 0; (b) "The criterion is strictly weaker than (M2*)" — only "weaker
(implied by (M2*))" is shown; no example separates them (and in a counterexample both fail). [F3]
The comparison with B Thm 3.6 is accurate: B's proof needed every b to derive credit-nullity of T; with (LH) the
SI pair (A,T') fixes one b, hence one X_1, hence one c. CORRECT.

### 3.3 Corollary 2.3 (absorption) — CORRECT
 - empty in N: acc_1(X_1, empty) fails by strict (G) (X_1 non-null). W in N, Q in G, acc_1(X_1, W u Q) would give,
   by Lemma 2.1 with W' := W u Q subset T_0(E) and G := Q (a finite union of pieces with acc_2(.,X_3), inside
   T_0(E)), acc_1(X_1, (W u Q) \ Q), and (W u Q) \ Q subset W, so (G) (more credit_1) acc_1(X_1, W): contradiction.
   So N + G subset N and (W = empty) G subset N. CHECKED.
 - N = {W : acc_2(W,X_1)}: at-least-one (E in F_12) and at-most-one (V undominated; W u X_1 non-null because X_1 is;
   strictness witness world 3, o_13 and o_23 being credit_3). CHECKED.
 - "Reading": N_n decreasing down-sets (less debt for larger n; less credit for smaller W); G_n decreasing provided
   c(X_1^n) is chosen nondecreasing in n (possible: (M1) at X_1^{n+1} subset X_1^n can be run with any larger c,
   subsets of Y_c inherit acc_3 by (G)) — say so; intersection_n N_n = {null}: for non-null W, (LH) gives (A,T')
   with T' subset W and (Y-d) puts X_1^n <=_d A for large n, so acc_1(X_1^n, W). Correct as a reading. [F4: add
   "with c(X_1^n) nondecreasing".]

## 4. §3 of M2: Proposition 3.1, Corollary 3.2

Setting. {q in [e_1,e_2] : C_q = D_2} = A_2(D_2) n edge (D_2 is the unique <=_2-best regular model, strict (G)):
closed, contains e_2, not e_1 (RK §2.2). q_e := its point nearest e_1 is a boundary point, q_e != e_1, so open-edge
q_m -> q_e from the e_1 side with C_m != D_2 exist, and beta_m -> inf along EVERY such sequence (RK §2.2 /
G3 13.1). Case (a) (alpha_m < inf on a subsequence; then 0 < beta_m <= alpha_m < inf for large m) is (BR_2^{21})
at q_e. Case (b) as used in the "Case (b)" paragraph must be read as "for some eps > 0 every selection on the
stretch of length eps before q_e has alpha = inf" (equivalently: no sequence as in (a) exists); the note's
formulation "C_m = E_2(beta_m) for all large m" refers to one sequence and should be replaced by this. [F5]

### 4.1 Proposition 3.1 (far-end tails are one good piece) — CORRECT
Step 1. F := D_2 silenced on Q, Q subset D_12 n {t_12 < 1/c'}: on D_12, D_2 is debt_1 (regions.py), so F <_1 D_2 =
 C_{q_e} pointwise and strictly ((G), Q non-null). q_e is not in the closed A_1(F) (F <_1 C_{q_e} means not
 C_{q_e} <=_1 F); for q_m near q_e (open edge, support {1,2}) competitiveness forces C_m <=_2 F. This is (T2) with
 the roles of 1, 2 exchanged; no completeness. For beta_m > 1/c' the difference set of (C_m, F) is exactly
 Q u (D_12 n {t_12 >= beta_m}) with pattern (credit_2 | silent) on Q, (silent | credit_2) on [beta_m, alpha_m],
 (debt_2 | credit_2) on tail_m, both o_12 on P_3 (regions.py). (IB): V + cred_2(Q) + debt_2(tail_m) <=_2
 V + cred_2(D_12 n {t_12 >= beta_m}) <_2 V (strict (G); the band is non-null). So (tail_m, Q) is strictly SI.
 CHECKED.
Step 2. (Y-c) at world 2 for T := X_3 (P1A 2.2 at world 2: X_3 subset P_3 subset D_23 \ D_21, so (E1) on edge 23 and
 then the transported branch to edge 21): a > 0 with every subset of L^2_1(a) = D_12 n {t_12 > 1/a} <=^2_c X_3. No
 completeness. Q := D_12 n {1/a < t_12 < 2/a} subset L^2_1(a), c' := a/2; for large m beta_m > 2/a, so tail_m n Q
 = empty; tail_m n X_3 = empty (regions). Context debt_2(tail_m) is silent on Q u X_3: V + debt_2(tail_m) +
 cred_2(X_3) <=_2 V + debt_2(tail_m) + cred_2(Q) <_2 V. T_0(C_m) = P_2 n tail_m: (G). CHECKED.
"No V-hypothesis, no completeness is used": CORRECT (only (S), (G), (IB), competitiveness of C_m).
Remark (not an error): Prop 3.1 needs no case hypothesis for the inequality; case (a) only makes T_0(C_m)
non-null.

### 4.2 Corollary 3.2 — CORRECT
 (i) C_m in F_12 (open edge). Lemma 2.1 at E := C_m with the single piece G := T_0(C_m) (acc_2(G, X_3) by Prop 3.1,
   m >= m_0(X_3)): for W subset T_0(C_m), acc_1(X_1, W) => acc_1(X_1, empty), false (strict (G), X_1 non-null). So
   not acc_1(X_1,W); "strictly rejects" by completeness of world 1. acc_2(T_0(C_m), X_1): XOR at-least-one.
   CHECKED.
 (ii) is (i) restated. CHECKED.
 (iii) Q subset P_1 n {t_12 < 1/c'} subset B_0(C_m) once beta_m > 1/c'; Step 1 with less debt (T_0(C_m) subset
   tail_m) gives acc_2(T_0(C_m), Q) strictly; XOR at-most-one (V undominated, Q non-null): not acc_1(Q, T_0(C_m)).
   CHECKED.
 Reading paragraph: heuristic; "any X_1 with acc_1(X_1,T_0(C_m)) must leave every fixed cone" should read "cannot
 contain a fixed non-null subset Q of a fixed cone {t_12 < 1/c'} once m >= m(Q)" (by (iii) and (G)). Cosmetic.
 Case (b) paragraph: the stated consequence of competitiveness of E_2(beta) (at least one of worlds 1, 2 weakly
 rejects o_23(Z) + o_13(W) for Z, W in its silence) is correct. Mirror at the D_1-end under (BR_1^{12}): I wrote it
 out — (S_SI^i) at world 1 (P1A 4.2) gives (D_12 n {t_12 < beta_m}, Q) SI for Q subset D_12 n {t_12 > c}; (Y-c) at
 world 1 for X_3 (cone L^1_2(a)); Q := D_12 n {a/2 < t_12 < a}; then B_0(C_m) subset D_12 n {t_12 < beta_m} is one
 X_3-good piece for world 1; the mirror Lemma 2.1 (orientation (2,1,3): pieces with acc_1(Q,X_3), acc_3(X_3,T),
 XOR gives acc_1(B_{k*-1},T), d := o_13(T) + o_23(B_{k*}) + o_12(X_3) strict at 2, weak at 1 and 3) holds. CORRECT.

## 5. §4 of M2: Lemma 4.1, Proposition 4.2, Remark 4.3

### 5.1 Lemma 4.1 — statement CORRECT (trivial); its "Hence" sentence and §0 S3 / (N3) WRONG as stated
The statement: if one competitiveness inference "X <_l C for all l in S\{k} => C <=_k X" with k = 2 has as
conclusion, via (IB), literally acc_2(Q,Y) (C gives o_13 on Q, o_12 on Y, X silent there), then the premise fails
at l = 1 because o_13, o_12 are credit_1 (regions.py), so C <_1 X. Correct, and immediate.
The consequence drawn ("Hence such acceptances can be produced by competitiveness only at selections with support
inside {2,3}") and §0 S3 ("competitiveness at a selection whose support contains world 1 never yields such an
acceptance") are FALSE in the natural reading (competitiveness followed by (G)/(IB)/yardstick steps), and the
counterexample is the note's own Prop 3.1: competitiveness of C_m in F_12 (support {1,2}, containing world 1),
followed by strict (G) and the (Y-c) transport, yields acc_2(T_0(C_m), X_3) — a world-2 acceptance of (P_2-debt,
P_3-credit) — and for a fixed E it yields acc_2(T n tail_m, Y_c) for every T subset T_0(E), i.e. it reaches
T n {t_12 > alpha_{m_0(c)}} at ALL s-levels. Lemma 4.1 is true only for "one-step" conclusions, which is not what
"source" means elsewhere in the note (Prop 4.2 counts (Y-d)/(LH)- and (S_SI^i)-transported acceptances as
sources). FIX [F6]: restrict the wording to "the conclusion of a single competitiveness inference", and add Prop
3.1 to the list of sources.

### 5.2 Proposition 4.2 — (a), (b) CORRECT; (c) CORRECT only in the one-step sense; the "uncovered middle"
claim INCOMPLETE
 (a) (LH) at world 2: strict SI (A, Y'), Y' subset Y_c; (Y-d) at world 2 (completeness of 2): every subset of
   H^2_3(b) = D_23 n {s > b} is <=^2_d A; B subset T n {s > b} subset P_2 misses Y' (regions). Chain: (G) (credit
   on Y_c \ Y', context debt_2(B)), (IB) (context cred_2(Y'), silent on B u A), SI pair. CHECKED.
 (b) Under (BR_2^{23}) [boundary of {C = D_2} on [e_2,e_3] approached with beta^2_m > 0; alpha^2_m -> 0]:
   (S_SI^i) at world 2 transported (F := D_2 with credit_2 silenced on Q; F <_3 D_2 since credit_2 = debt_3 on D_23;
   (T2) gives C_m <=_2 F): (D_23 n {s < beta^2_m}, Q) strictly SI for Q subset D_23 n {s > 1}; Q := P_2 n
   {|g_2| < a g_1} n {s in (1,2)} is non-null and in L^2_1(a) (regions.py), so Q <=^2_c Y_c ((Y-c), no
   completeness); restrict the debt to P_2 n {s < beta^2_m} (disjoint from Y_c, and from Q once beta^2_m < 1);
   (IB) with that debt as context. CHECKED. No completeness, no V.
 (c) As a statement about single competitiveness inferences: the edge-23 XOR at F needs Y subset P_3 n
   {s > alpha^2_F}; Y subset Y_c = P_3 n {s < 1/c} non-null forces alpha^2_F < 1/c (regions.py), hence Q subset
   {s < beta^2_F} subset {s < 1/c}. CORRECT. But "it covers no more than (b)" is not shown: (b) covers
   {s < sigma(c)} with sigma(c) = beta^2_m for ONE m, while edge-23 XOR at selections F with beta^2_F in
   (sigma(c), 1/c) may cover parts of T n {sigma(c) <= s < 1/c} (when it returns acc_2 rather than acc_3). The
   region reached by none of (a)-(c) is T n {1/c <= s <= b(c)}, not T n {sigma(c) <= s <= b(c)}.
 The "uncovered middle ... is where (M2*) must be decided" sentence (and (N3) in §6) is incomplete in two ways:
   - in case (a) at the D_2-end of edge 12 [(BR_2^{21})], Prop 3.1 covers T n {t_12 > alpha_{m_0(c)}} as ONE piece
     at every s-level (see 5.1), so the residual is T n {sigma(c) <= s <= b(c)} n {t_12 <= alpha_{m_0(c)}};
   - closedness sources at world 2 on edge 23 also reach bounded s-levels: an (S_SI^ii) configuration (P1A 4.2: a
     silent edge-23 selection q° with beta^{2°} > 0 approached <=pw_2 with beta^2_m < beta^{2°}) gives
     (band b[beta^2_m, beta^{2°}), Z_c) strictly SI for ANY non-null credit set Z_c in the silence band away from the
     moving levels; taking Z_c := P_2 n L^2_1(a) n {s in a compact sub-interval of the silence} (non-null, <=^2_c
     Y_c by (Y-c)) gives (P_2 n band, Y_c) SI: one Y_c-good piece at bounded s-levels.
   So (c) does not support "never the middle of T_0(E)" (§0 S3) or (N3)'s "which no competitiveness source at a
   selection whose support contains world 1 can reach". FIX [F7]: state (c) as "no SINGLE competitiveness inference
   at a selection whose support contains world 1 concludes acc_2(Q,Y); the edge-23 XOR reaches only {s < 1/c}";
   delete "covers no more than (b)"; list Prop 3.1 (case (a)) and (S_SI^ii)-type sources at world 2 among the
   sources, and restate the residual accordingly.

### 5.3 Remark 4.3 (the tied full-support selection) — CORRECT (one incomplete sub-claim)
 - KKMb (r2 SETTING): V undominated => V ~_k C_{p_V} at every k, p_V full-support. CHECKED.
 - acc_k(d'') <=> V <=_k V + d': the pair (V + d' + d'', V + d') has difference set supp d'' with the advice of
   (V + d'', V) (d', d'' disjointly supported restrictions of d_V); V + d_V ~_k V; transitivity. Symmetric form
   likewise. CHECKED.
 - Dichotomy: if no world strictly accepts d', completeness gives V <=_k V + d', i.e. acc_k(d'') at every k; V + d''
   does not dominate V only if V + d'' ~_k V at every k, i.e. (symmetric form) V + d' <=_k V; so d' is a tie at
   every world. CORRECT (uses completeness and V undominated twice: KKMb and the final step).
 - Bundling claim: to force world 2, worlds 1, 3 must not strictly accept d'; d' must contain world-1 debt, which on
   C_V's advice is o_23 on P_1, o_2 on P_2 or o_3 on P_3. The note says the acceptance forced on world 2 is "of the bundled form
   acc_2(Q, Y u B) with B subset P_1"; the o_2 (credit_2 on P_2) and o_3 (debt_2 on P_3) alternatives are omitted.
   Heuristic sentence; add them. [F8] "Vacuous if C_V = V": correct (d_V = 0).

## 6. §5 of M2: tail families, XOR couplings, holonomy, Theorem 5.6

### 6.1 Set-up and the six families — CORRECT
Interior E in F_12, E' in F_13, F in F_23 exist when V is undominated (B Cor B.6, RB5: CORRECT). All region claims
re-checked mechanically (regions.py): each family is non-null; A' subset B_0(E), D subset T_0(E); A subset
P_1 n {t_13 < beta'} (E' gives o_23), C' subset P_3 n {t_13 > alpha'} (E' gives o_12); D' subset P_2 n {s < beta^2}
(F gives o_13), C subset P_3 n {s > alpha^2} (F gives o_12); x_0 > max(sup I, sup J, ...) makes A(x) n A'(x'),
D n D', C n C' empty. Owner tails, light second views and transversal third views exactly as listed. CORRECT.

### 6.2 Lemma 5.1 (XOR couplings) — CORRECT
(k1) at E (strictness witness world 3: o_13, o_23 credit_3), (k2) at E' (witness world 2: o_12 on P_3 and o_23 on P_1
are credit_2), (k3) at F (witness world 1: o_13, o_12 credit_1). Each "<=>" uses BOTH halves of XOR (at-least-one:
competitiveness of the interior selection on its edge; at-most-one: V undominated and the union non-null).
Directions of the four acceptances in each coupling checked against the option table. CORRECT.

### 6.3 Lemma 5.2 and Lemma 5.3 — CORRECT
5.2, last sentence: §2.1 above. First display: e.g. acc_2(D(y), A'(x)) for large y (last sentence at world 2,
debt family D, credit A'(x)), then (k1) at-most-one: not acc_1(A'(x), D(y)). Same for (k2) [acc_1(A(y), C'(x))]
and (k3) [acc_3(C(y), D'(x))]. CHECKED. Uses V (at-most-one), (LH), completeness ((Y-d)).
5.3: (Z1) is B Lemma 3.1 (RB5: CORRECT) in orientation (1,2,3) with X_1 = A(x), X_2 = D(y), X_3 = C(z); (Z2) in
orientation (1,3,2) with X_1 = A'(x), X_3 = C'(u), X_2 = D'(w): trades (X_1,X_3) at 1, (X_3,X_2) at 3, (X_2,X_1) at 2.
CHECKED. Uses V undominated; no completeness, no (IB).

### 6.4 Proposition 5.4 (holonomy rigidity) — CORRECT under (TC)
(a) For (k1): x > h_{A'D}(y) => acc_1(A'(x),D(y)) => not acc_2(D(y),A'(x)) => y <= h_{DA'}(x) (y outside the
 up-ray); x < h_{A'D}(y) => not acc_1 => acc_2 => y >= h_{DA'}(x). With g := h_{A'D}^{-1} (strictly increasing,
 continuous): y < g(x) => y <= h_{DA'}(x), y > g(x) => y >= h_{DA'}(x); hence h_{DA'}(x) = g(x) for every x in the
 range of h_{A'D} (y can approach g(x) from both sides inside the domain ray once x is far out). Needs only that
 h_{A'D} is an increasing homeomorphism (no hypothesis on h_{DA'}). Same for (k2), (k3). CHECKED.
 Conjugation: substituting the three matchings and inverses,
   H_2 = [h_{A'D} h_{AD}^{-1} h_{AC'}][h_{AC'}^{-1} h_{CA}^{-1} h_{D'C}^{-1}][h_{D'C} h_{DC}^{-1} h_{A'D}^{-1}]
       = h_{A'D} h_{AD}^{-1} h_{CA}^{-1} h_{DC}^{-1} h_{A'D}^{-1} = Psi H_1^{-1} Psi^{-1}, Psi = h_{A'D} h_{AD}^{-1},
 using (h_{DC} h_{CA} h_{AD})^{-1} = h_{AD}^{-1} h_{CA}^{-1} h_{DC}^{-1} and h_{DC} h_{CA} h_{AD} = h_{AD}^{-1} H_1 h_{AD}.
 CHECKED by hand and numerically (holonomy.py).
(b) H_1(x) < x: choose z slightly > h_{CA}(x), then y slightly > h_{DC}(z); by continuity h_{AD}(y) < x; the three
 parameters lie strictly inside their up-rays, so acc_3(C(z),A(x)), acc_2(D(y),C(z)), acc_1(A(x),D(y)): (Z1).
 H_2(x) < x likewise gives (Z2) (w > h_{D'A'}(x): acc_2(D'(w),A'(x)); u > h_{C'D'}(w): acc_3(C'(u),D'(w));
 x > h_{A'C'}(u): acc_1(A'(x),C'(u))). So H_1, H_2 >= id; by (a), H_2 >= id on a ray <=> H_1^{-1} >= id on the
 Psi^{-1}-image ray <=> H_1 <= id there. H_1 = id on a ray. CHECKED.
(c) Immediate from (Z1). CHECKED.
Remark: by Lemma R1 (§2.2) the three matchings in (TC) are consequences, so Prop 5.4 holds under (TC6).

### 6.5 Corollary 5.5 (a heavy germ at every tail level) — CORRECT
 - Extras: acc_1(A'(x''),C(z)) strict (C(z) subset P_3: o_12 credit_1), acc_2(D'(w),A(x)) strict (A(x) subset P_1:
   o_23 credit_2), acc_3(C'(u),D(y)) strict (D(y) subset P_2: o_13 credit_3): Lemma 5.2's last sentence with these
   credit sets (its proof works for any non-null credit set in another region). CHECKED.
 - Negation: every unattained world k has a band b_k = X(level) \ X(level') with acc_k(b_k, L_k) (completeness turns
   "not strictly AC" into acc). For the unattained world 1, x' > x = h_{AD}(y) gives acc_1(A(x'),D(y)); for an
   attained world b := empty, x' := x. The three accepted changes per world are disjointly supported and compose
   ((IB) + transitivity, one strict) to V + d: verified symbolically (compose.py), all three worlds. Disjointness of
   the six sets: x_0 choice and regions. CHECKED.
 - Hence some world is unattained and every band at its germ is strictly AC against L_k. CORRECT.
 Uses: V undominated, completeness (twice), (LH), (Y-d).

### 6.6 Theorem 5.6 — CORRECT (proof valid); hypotheses can be weakened (F1, F9)
Re-traced step by step.
 1. V undominated (reductio). (TC) gives the ray R (Prop 5.4(b)); for x in R, z := h_{CA}(x), y := h_{DC}(z),
    h_{AD}(y) = x. Cor 5.5: a world k, unattained, with every band at its germ strictly AC against L_k:
    k = 1: A(x)\A(x') subset D_12 n {x < t_12 <= x'}; k = 2: D(y)\D(y') subset D_23 n {y < s <= y'}; k = 3:
    C(z)\C(z') subset D_31 n {z < t^3_1 <= z'} (regions.py).
 2. (LH) at k: strict SI (A_k, L'_k), L'_k subset L_k. A band b <=^k_d A_k would give V + debt(b) + cred(L_k) <=_k
    V + debt(b) + cred(L'_k) [(G); L_k \ L'_k misses b] <=_k V + debt(A_k) + cred(L'_k) [(IB), context cred(L'_k)
    silent on b u A_k: b subset P_k, L'_k outside P_k, A_k n L'_k = empty] <_k V: acc_k(b, L_k), contradicting step 1.
    So no slab band at the germ is <=^k_d A_k. CHECKED.
 3. If the level (x, y or z) were covered on the edge [e_k,e_{k+1}] in world k's frame: silent q* — P1A Thm 3.1
    (X2) in world k's frame (re-derived: Lemma 3.0 gives beta_m -> z, alpha_m -> alpha* >= z + 3 delta; debt
    yardstick Z' := Z_{(z+delta,z+2delta)} <=^k_d A_k (P1A 2.1 in world k's frame, completeness at k) lies in the
    silence of C_{q*} and eventually of C_m; F := C_{q*} + debt_k(Z') is world-(k+1)-better ((1.1)), so (T2) and
    competitiveness of the open-edge C_m give C_m <=_k F; C_{q*} + debt_k(b(z,beta_m)) <=pw_k C_m; (IB), common
    context C_{q*}: b(z,beta_m) <=^k_d Z' <=^k_d A_k); precise q* — P1A Lemma 4.1 (X2') with the AC pair of LH 5.1
    (RLH: CORRECT after M5). Either way the FULL band b(z, beta_m) of D_{k,k+1} is <=^k_d A_k, hence (G) so is the
    slab band X(z) \ X(beta_m) (null boundary {tau = beta_m} ignored). Contradiction with step 2: the level is in
    NK_k. CHECKED.
 4. Baire. R subset NK_1 u y^{-1}(NK_2) u z^{-1}(NK_3), with x -> z(x) = h_{CA}(x), x -> y(x) = h_{DC}(h_{CA}(x))
    increasing homeomorphisms of R onto rays (TC). Item (5) of the brief: the levels live in (0,inf) with its usual
    topology; a meagre subset of (0,inf) meets a ray in a set meagre in that ray (a set nowhere dense in (0,inf) is
    nowhere dense in any subray: a relatively open subset of a ray contains an open interval of (0,inf));
    homeomorphisms preserve meagreness; so R is a union of three sets meagre in R. R is a closed ray of the reals,
    a complete metric space, hence not meagre in itself (Baire). CORRECT. No measurability is needed.
 5. The symmetric statement (families A', D', C', edges 13, 21, 32): H_2 = id by (a), (b); at the (Z2)-triple
    (x, w := h_{D'A'}(x), u := h_{C'D'}(w)) with h_{A'C'}(u) = x, take the strict extras acc_1(A(x~), D'(w)),
    acc_2(D(y~), C'(u)), acc_3(C(z~), A'(x)) and leftovers L_1 = D(y~) u C(z~), L_2 = A(x~) u C(z~), L_3 = A(x~) u D(y~);
    the composition is verified in compose.py; the germs are A' at x on edge 13 (t_13), D' at w on edge 21
    (t^2_1), C' at u on edge 32 (t^3_2) (regions.py). CORRECT.
Where hypotheses enter: completeness at every world (Cor 5.5, (LH), (Y-d) inside (X2), LH 5.1); (IB) at every
world; V undominated (XOR both halves, TRI, Cor 5.5); competitiveness of open-edge selections ((X2)/(X2') via (T2))
and of the three interior selections (XOR). All consistent with the theorem's statement.
Two improvements a referee should require to be stated (they are proved, not conjectured):
 (F1) (TC) may be replaced by (TC6) (Lemma R1 + Prop 5.4(a) first sentence).
 (F9) Only levels on the rays R, y(R), z(R) are used, and R may be shrunk to any subray (H_1 = id there), while y,
      z are unbounded. Hence it suffices that for each k there is M_k with NK_k n (M_k, inf) meagre ("uncovered
      HIGH levels meagre"); the hypothesis on all of (0,inf) is stronger than needed. With this form, §7 below shows
      that the hypothesis holds automatically at endpoint-family ("poor") far ends.
Remarks (1), (2) after the theorem. (1): "jumped-over levels form intervals of uncovered levels" holds only for
levels not attained (and approached from above comparably) elsewhere on the edge; reword. "jump-free paths that are
monotone except at a meagre set of levels" is heuristic. (2): the additive check is right (in an Archimedean
additive world with continuous densities, x -> P_d(X(x)) and y -> P_c(Y(y)) are continuous strictly decreasing
to 0, giving (TC)); "fine case with continuous thresholds" is accurate only with that proviso (fine fa worlds may
have charges concentrated at a level, giving jumps). [F10, cosmetic]

## 7. Item (6): are the hypotheses of Theorem 5.6 consistent with the known shape of a counterexample, or vacuous?

Known necessary shape (n = 3, complete (G)+(IB), (S), V undominated): no fine world (K Thm 3.20), no fine edge and
an interior selection on every edge (B Cor B.6), no world with local fa extensions on both edge regions (C5 Thm
4.1), (LH)/(DH) everywhere (LH Thm 4.1), XOR flips with heavy germs at every two-sided selection (LH 5.3), untied
non-clean nested jumps (N Cor 2.4). Theorem 5.6 has two hypotheses: (TC) [equivalently (TC6), §2.2] and
meagreness of uncovered levels [only HIGH levels are needed, F9].

7.1 The meagreness hypothesis is not vacuous: it holds automatically at "poor" far ends.

**Lemma R3 (endpoint-family far ends cover all high levels). PROVED (referee).** Fix a world k, the edge
[e_k,e_l] in world k's frame tau = t^k_l (debt_k below beta, credit_k above alpha; D_k = (0,0), D_l = (inf,inf)),
and let q_e be the point of the closed set {q : C_q = D_l} nearest to e_k. Suppose there is eps > 0 such that every
selection C_q with q on the stretch S of length eps before q_e (on the e_k side) has alpha_q = inf (e_l in its
credal set; C_q = E_l(beta_q)). Then there is M < inf such that every level z > M is covered (in the sense of
Thm 5.6). Only (G) at k, l and (S) are used.
Proof. On S, C_q != D_l (q_e is the nearest point), so beta_q < inf, and any two selections E_l(b), E_l(b') are
pointwise comparable. For q* in S and q_m -> q* in S, split into a <=pw_k and a >=pw_k subsequence; P1A Lemma 3.0
(comparable approaches converge; closed A_k, A_l; in world k's frame) gives beta_{q_m} -> beta_{q*}: beta is
continuous on S. Along every sequence q_m -> q_e with C_{q_m} != D_l, beta_m -> inf (RK §2.2 / G3 13.1 in world k's
frame). Let q_1 in S be the point at distance eps/2 before q_e and M := beta_{q_1}. For z > M the set
{q in [q_1, q_e) : beta_q = z} is non-empty (IVT), closed in [q_1,q_e), and bounded away from q_e, hence compact;
let q* be its point nearest q_e. On (q*, q_e) beta != z, hence (IVT, beta -> inf) beta > z. Choose q_m in (q*, q_e)
with q_m -> q*: they are open-edge indices, beta_m > z, and C_{q_m} = E_l(beta_m) >=pw_k E_l(z) = C_{q*} (more
debt_k, no credit). q* is silent (beta* = z < inf = alpha*). So z is covered. ∎
In Thm 5.6's three frames the relevant far ends are: k = 1, edge 12, end D_2 (alpha^{(1)} = inf means e_2 in the
credal set); k = 2, edge 23, end D_3 (no credit_2 on D_23, e_3 in the credal set); k = 3, edge 31, end D_1 (no
credit_3 on D_31, e_1 in the credal set). For the (Z2)-version: edge 13 end D_3, edge 21 end D_1, edge 32 end D_2.
"Poor" at q_e is the negation of richness at q_e: rich = approached by selections with alpha^{(k)} < inf, i.e.
with non-null world-l debt (this is (BR_l^{lk}) of P1A Cor 10.3 at the point q_e; for k = 1 it is case (a) of §3).

**Corollary R4. PROVED (Thm 5.6 with F9 + Lemma R3).** Let n = 3, all rankings complete with (G), (IB), (S), and
let (TC6) hold for some interior E, E', F and intervals. If the D_2-end of edge 12, the D_3-end of edge 23 and the
D_1-end of edge 31 are all poor (at the nearest points q_e as in Lemma R3), then V is dominated; likewise if the
D_3-end of edge 13, the D_1-end of edge 21 and the D_2-end of edge 32 are all poor. Equivalently: under (TC6) a
counterexample has, at one end of each of these two triples, selections accumulating at the far vertex with
non-null far-world debt, and with a NON-MEAGRE set of uncovered high levels there.
So the meagreness hypothesis is satisfied in a natural class of configurations that, as far as I can check, no
known necessary condition excludes (poor ends are local chains; P1A summary item 5 and LH Lemma 3.4 Case II treat
them without contradiction). It is a genuine restriction in the rich case: a path that, near the far vertex,
crosses all high levels only by continuous nested moves (the construction of K Prop 4.8, with amplitude -> 0 at
the vertex) has NK_k n (M,inf) = (M,inf); whether such a path is an (S)-selection with V undominated is open.

7.2 (TC) is unverified and fails in the one candidate structure.
 - No (S)-configuration with V undominated is known (that is P1 itself), so (TC) cannot be tested there. It is a
   regularity assumption on cross-region tail comparisons only; it does not imply fineness, an fa extension, or
   (BR) at any end (Remark (2) of the note is accurate), so it is not in conflict with "no fine world/edge", C5 Thm
   4.1 or (LH)/(DH) as far as I can see; nor does (TC) + V undominated contradict Cor 5.5 by an obvious argument
   (heaviness of a band relative to a FIXED credit and continuity of the thresholds are compatible in
   non-additive (IB) orders, because (IB) gives no translation invariance between the comparisons
   V + debt(b) + cred(c) vs V and V + debt(b) vs V + cred(c)).
 - In the order-separated valuation of §6.1 every h_{XY} is a STEP function (acceptance is decided by the
   integer shell index of the leading exponent), so (TC) fails there — consistent with the note's reading that
   flats/jumps of the thresholds are where a counterexample would have to live.
 - (TC) requires h_{XY} -> inf. For h_{A'D}, h_{AC'}, h_{D'C} this is forced by Lemma 5.2 (fixed debt of the XOR
   partner family is eventually rejected against deep transverse credit); for h_{AD}, h_{DC}, h_{CA} it is an extra
   assumption (a bounded h_{AD} would mean A(x) compensated by arbitrarily deep D(y), which nothing excludes).
Verdict on item (6): the hypotheses are NOT shown to be inconsistent with the known shape of a counterexample and
are not vacuous for any reason I can find; the meagreness part is automatic at poor far ends (Lemma R3), so the
real content of Theorem 5.6 is Corollary R4: (TC6) + V undominated forces richness, with non-meagre uncovered high
levels, at one far end of each triple. Whether (TC6) can hold in a counterexample is open; the only explicit
candidate violates it.

## 8. §6 of M2 (necessary conditions; order-separated valuation; the brute-force script)

### 8.1 (N1)-(N5)
 (N1) = Cor 2.3: CORRECT; "same on every edge by relabelling": correct (Lemma 2.1 is label-symmetric).
 (N2) = Cor 3.2: CORRECT (case (a)).
 (N3): first half (T n {sigma(c) <= s <= b(c)} is not in J^{(2)}[Y_c] whenever T is not, under (BR_2^{23})) is
   CORRECT (ideal property + Prop 4.2(a),(b)). Second half ("which no competitiveness source at a selection whose
   support contains world 1 can reach") is WRONG as stated: in case (a) at the D_2-end of edge 12, Prop 3.1 (a
   source at C_m in F_12) reaches T n {t_12 > alpha_{m_0(c)}} at all s-levels (§5.1-5.2). Fix as in F7.
 (N4) = Prop 5.4, Cor 5.5: CORRECT under (TC) (or (TC6)). The add-on "without (TC), the discontinuities of the tail
   thresholds are heavy germs themselves" is half right: a FLAT h_{XY} = x on [y_1,y_2] gives, by (IB), for all
   x'' < x < x' the two-sided debt band X(x'')\X(x') strictly AC against the fixed credit band Y(y_1)\Y(y_2) (a
   genuine heavy two-sided germ); a JUMP of h_{XY} at y* gives only V + cred_k(c) <_k V + debt_k(b) for the thin
   credit band c at y* and a fixed debt band b — a comparison of a pure credit change with a pure debt change,
   which is not an SI/AC statement and is not "a credit germ of Y" in the CCF sense without further argument.
   Reword. [F11]
 (N5): "PROVED as stated" overstates §6.1 (next item). [F12]

### 8.2 §6.1 the order-separated valuation — description CORRECT; "kill" PROVED only for a restricted class
Re-checked from the definitions (v(X) := sum_j mu(X n S_j) omega^{3 phi(j) + k} for X subset P_k; world k accepts a
triangle trade iff v(own-region debt) <= v(credit)):
 - TRI: three cyclic acceptances would give v(X_1) <= v(X_2) <= v(X_3) <= v(X_1), impossible (distinct exponent
   classes mod 3, values non-zero); bundled TRI likewise (the leading exponent of a union is the max). CORRECT.
 - Exact XOR for every pair of non-null sets in different regions: ties impossible. CORRECT (stronger than needed).
 - Tails: depth -> inf along each family, phi -> -inf, so v(X(x)) is eventually below any fixed non-null value, in
   every view. (LH)/(DH) for triangle options: deep tails supply the pairs. CORRECT.
 - (M2*) fails for every non-null T: T meets some shell j_0 with positive mass, so its exponent class is fixed while
   v(Y_c) has leading exponent <= 3 phi(floor(log c)) + 3 -> -inf; a finite union of pieces with v(Q) <= v(Y_c)
   must miss every shell of exponent above that of Y_c. CORRECT (the note's parenthetical "exceeds that of any
   world-3-admissible X_3" is imprecise — admissibility depends on X_1 — but the conclusion stands).
 - Consistency with the note's own results: Cor 2.2/2.3 (v additive on disjoint sets, so v(W) <= max-class
   bound < v(X_3) <= v(X_1)), Prop 3.1/Cor 3.2 (T_0(C_m) deep in P_2-depth) all hold in the valuation. Good.
 - Kill. With top level Phi := the coefficient of the maximal exponent 3 phi(0) + 3 (P_3, innermost shell), Phi is
   blind on P_1 u P_2, P_1 is t^3_1-determining on edge 31, Phi(D_1) != Phi(D_3) (o_12 vs o_3 on P_3), so P1C Lemma
   3.3 (re-read: f(q) = Phi(C_q) locally constant at every edge point, hence constant) excludes any world order in
   which Phi (suitably signed) is an ordinal primary (works at world 3 on edges 31 and 32, at world 1 on edge 13,
   at world 2 on edge 23; NOT at world 1 on edge 12 or world 2 on edge 21, where both vertex models give o_12 on
   P_3). CORRECT for that class. But "this is the case for every lexicographic extension"
   is unproved: an extension may give ANTI-triangle advice (o_1, o_2, o_3, which edge models use) exponents above
   all triangle classes, and then the top level need not be blind on a t-determining region. Restrict the claim to
   "every lexicographic extension whose top level is the maximal triangle class (or any top level blind on a
   t-determining region of an edge whose two vertex models it separates)". [F12]
 - The phrase "a counterexample must have relative heaviness with no top level" is therefore a heuristic summary.

### 8.3 §6.2 and the script r5/m2chk/tie_orders.py — what it actually verifies
Run (python3 -I): "assignments avoiding both cycles: 1442". The script enumerates, for each world, a STRICT total
order of four labels (world 1: A, A', D, C'; world 2: D, D', C, A'; world 3: C, C', A, D'), reads acc_k(X,Y) as
pos(X) < pos(Y), imposes the three XOR couplings (k1)-(k3) as equalities of two bits, and excludes the two cycles
(Z1), (Z2). That is all. My analysis (ties_analysis.py, output ties_out.txt):
 - 1442 counts PERMUTATION triples; they realize only 266 DISTINCT acceptance patterns (of the 12 cross bits that
   the constraints see); 344 patterns satisfy the XOR couplings alone, so the two cycles remove 78. "1442
   consistent assignments" overstates the multiplicity (cosmetic).
 - The encoding is a strict biorder per world (acceptance monotone in a total order) — legitimate for a complete
   (IB) world (acceptance of (X,Y) with X, Y disjoint is monotone in the debt order of X and the credit order of Y),
   but it excludes TIES, i.e. exactly the borderline/threshold situation of Prop 5.4(c) and Cor 5.5 ("attained /
   unattained"). Despite its name the script models no tie data.
 - It encodes only 4 of the 6 families per world, hence only 2 of the 16 tail TRI cycles. Extending to each world's
   full 2 x 4 biorder (146 patterns per world) with all 16 TRI cycles and the three couplings: 93340 consistent
   patterns. The order-separated single-member pattern is one of them.
 - It encodes NO lightness (Lemma 5.2), no (LH)/(DH), no thresholds, no continuity, no composition with extras
   (Cor 5.5), no bundled TRI. Lightness is the input that makes the threshold maps finite and tend to inf; with one
   member per family it has no meaning.
 Conclusion: the script verifies only that the five constraints (3 XOR equalities, 2 forbidden cycles) on one
 representative per family are satisfiable in many ways (trivially so: the order-separated pattern satisfies
 them). This is consistent with, but much weaker than, "finite tie data cannot decide"; the inference "so the
 holonomy argument genuinely needs the continuum of members" is a reasonable heuristic, not something the script
 shows. Reword §6.2 and §0 S5 accordingly. [F13]

## 9. Items (2)-(5) of the brief, collected; and the "next step" paragraph of §0

(2) (IB) applications. Lemma 2.1 world 2 (difference set R_{k*} u X_3, pattern of (V + o_13(R) + o_12(X_3), V));
 Cor 2.2 "relation" (context cred_1(T'), silent on X_1 u A); Prop 3.1 Step 1 (difference set Q u (D_12 n
 {t_12 >= beta_m}), pattern checked mechanically), Step 2 (context debt_2(tail_m), silent on Q u X_3); Prop 4.2(a)
 (contexts debt_2(B), cred_2(Y')), (b) (context debt_2(P_2 n {s < beta^2_m})); Remark 4.3 ((V + d' + d'', V + d')
 vs (V + d'', V)); Lemma 5.2 (context cred_k(Y')); Cor 5.5 (composition of disjointly supported acceptances,
 mechanically checked); Thm 5.6 step 2 (context cred_k(L'_k)) and step 3 ((X2): common context C_{q*}); Lemma R1
 (contexts debt(X(x_1)), debt(X'(x~))). In every case the two compared pairs have the same difference set and the
 same advice there, or the context is silent on the changed sets. ALL CORRECT.
(3) Competitiveness and XOR. XOR is used only at members of F_12 (E; C_m, open-edge indices), F_13 (E'), F_23 (F),
 always with the debt set in the B_0-type region and the credit set in the T_0-type region of that selection
 (regions.py). At-least-one (no V): Lemma 2.1, Cor 3.2(i), Cor 2.3 (first inclusion). At-most-one (V undominated;
 union non-null; strictness witness the third world): Cor 2.3 (identity of N), Cor 3.2(iii), Lemmas 5.1-5.2,
 Prop 5.4(a). Competitiveness of open-edge selections (via (T2)): Prop 3.1 Step 1, (S_SI^i) in Prop 4.2(b), (X2)
 in Thm 5.6. Competitiveness of full-support selections: not used (Remark 4.3 uses only KKMb ties). ALL CORRECT.
(4) Completeness and V undominated. Lemma 2.1, Cor 2.2: V once, no completeness. Cor 2.3: V. Prop 3.1: neither.
 Cor 3.2: V; completeness only for "strictly rejects". Prop 4.2(a): completeness (Y-d at 2; (LH)); (b): neither.
 Remark 4.3: V, completeness. §5: V throughout (XOR, TRI, Cor 5.5); completeness in Lemma 5.2 ((LH), (Y-d)), Cor 5.5
 (reading "not acc" as strict AC; extras), Thm 5.6 ((LH), (Y-d) in (X2), LH 5.1 in (X2')), Lemma R1. The note's
 claims "no V-hypothesis, no completeness" (Prop 3.1) and "(no race: all sets fixed before the last comparison)"
 (Cor 5.5) are accurate. CORRECT.
(5) Baire step: §6.6 step 4. CORRECT as stated (hypothesis of meagreness in (0,inf); homeomorphisms of rays).

9.1 The "Most promising next step" (§0) contains a FALSE assertion (heuristic paragraph, not a theorem; flagged
because it is proposed as the route forward). "A threshold map is a real monotone function, so it has only
countably many jumps; jumps are harmless for the Baire argument once Prop 5.4 is redone with monotone
correspondences". Countability does not make jumps harmless: if x -> z(x) is strictly increasing with jumps at a
DENSE countable set whose sizes make its image nowhere dense, then a meagre NK_3 may contain the whole image and
z^{-1}(NK_3) = R. Example: f(x) := x + sum_{n : q_n < x} 2^{-n} ((q_n) an enumeration of the rationals) is strictly
increasing, and its image misses the dense open union of the gaps (f(q_n), f(q_n) + 2^{-n}), so f(R) is nowhere
dense; with NK := f(R) (meagre) one has f^{-1}(NK) = R. So with dense jumps Theorem 5.6's Baire step fails, and
dense accumulation of jumps is exactly the behaviour the residual allows (N Cor 2.4(iii) for edge paths; nothing is
known for the h_{XY}). Also, flats are ALSO at most countably many (disjoint open intervals); what makes them
harmful is that a flat maps an interval of x to one level (non-injectivity), not their number. FIX [F14]: delete
"jumps are harmless ... (countably many)"; say that without (TC) meagreness of NK_k in (0,inf) does not control
the preimage under the level maps (dense jumps: the image can be nowhere dense; flats: non-injective), so jumps
and flats are BOTH genuine obstacles, and a replacement hypothesis must control NK_k on the image of the level map
(e.g. "the set of x whose level lies in NK_k is meagre", stated directly in the x-parameter). [With locally finite
jumps the note's claim is right: then R splits into countably many intervals on which the maps are
homeomorphisms onto intervals, plus a countable set.]

## 10. Consolidated list of fixes

 F1 (§5 (TC); Prop 5.4; Thm 5.6). The matchings are consequences (Lemma R1, §2.2: completeness + (IB) + continuity
    and strict monotonicity of the other maps), and three of the twelve maps are inverses of three others by XOR.
    Replace (TC) by (TC6): h_{AD}, h_{DC}, h_{CA}, h_{A'D}, h_{AC'}, h_{D'C} are increasing homeomorphisms between
    rays on a ray. Delete "it is ASSUMED here"; insert Lemma R1 with its proof.
 F2 (Cor 5.5; §0 S4). "relative to an explicit light credit": L_k has one light part and one transversal part
    (e.g. L_1 = C'(u) u D'(w), C'(u) transversal for world 1). Reword.
 F3 (Cor 2.2, "Relation to (M2*)"). Require beta_E > 0 (else X_1 = B_0(E) n {t_13 > b} is null). "strictly weaker
    than (M2*)" -> "weaker (implied by (M2*))".
 F4 (Cor 2.3, Reading). Choose c(X_1^n) nondecreasing in n (possible: (M1) at c persists for every larger c), so
    that G_n decreases.
 F5 (§3, case split). Define case (b) as "for some eps > 0 every selection on the stretch of length eps before q_e
    has alpha = inf" (the negation of (BR_2^{21}) at q_e), not via one sequence. Cosmetic in Cor 3.2's Reading:
    "cannot contain a fixed non-null Q subset {t_12 < 1/c'} once m >= m(Q)" instead of "must leave every fixed cone".
 F6 (Lemma 4.1 "Hence"; §0 S3). True only for the conclusion of a SINGLE competitiveness inference. With the usual
    (G)/(IB)/yardstick steps, competitiveness at edge-12 selections (support containing world 1) does produce
    world-2 acceptances of (P_2-debt, P_3-credit): Prop 3.1. Restrict the wording; list Prop 3.1 as a source.
 F7 (Prop 4.2(c), the "uncovered middle", (N3)). Delete "it covers no more than (b)" (edge-23 XOR may reach parts
    of {sigma(c) <= s < 1/c}); the region reached by none of (a)-(c) is T n {1/c <= s <= b(c)}. Add the sources
    Prop 3.1 (case (a): T n {t_12 > alpha_{m_0(c)}} at all s-levels) and (S_SI^ii) configurations of world 2 on
    edge 23 (bounded s-levels, credit yardstick taken in P_2 n L^2_1(a)). Rewrite (N3) without "no competitiveness
    source at a selection whose support contains world 1 can reach".
 F8 (Remark 4.3). The world-1 debt in d' may be o_23 on P_1, o_2 on P_2 or o_3 on P_3; list all three bundlings.
 F9 (Thm 5.6). Only high levels are used: replace "NK_k meagre in (0,inf)" by "NK_k n (M_k,inf) meagre for some M_k"
    (shrink R; y, z unbounded). Add Lemma R3 and Corollary R4 (§7): the hypothesis holds automatically at poor far
    ends, so (TC6) + V undominated forces a rich far end with non-meagre uncovered high levels in each of the two
    triples {D_2-end of 12, D_3-end of 23, D_1-end of 31}, {D_3-end of 13, D_1-end of 21, D_2-end of 32}.
 F10 (Remarks after Thm 5.6). (1): jumped-over levels are uncovered only if not covered elsewhere on the edge;
    "monotone except at a meagre set of levels" is heuristic. (2): "(TC) holds in the fine case with continuous
    thresholds" needs the continuity proviso (fine fa worlds may have level-concentrated charges).
 F11 ((N4) / Cor 5.5 Reading). A flat of h_{XY} is a two-sided debt germ strictly AC against a fixed credit band
    (correct); a jump gives only V + cred(c) <_k V + debt(b), not an SI/AC statement. Reword "a jump is a credit germ".
 F12 (§6.1; (N5); §0 S5; (M2-F7)). The P1C Lemma 3.3 kill is proved for world orders whose top level is the maximal
    triangle class (more generally, any top level blind on a t-determining region of an edge whose vertex models it
    separates); "this is the case for every lexicographic extension" is unproved (anti-triangle advice may carry
    higher exponents). Change "PROVED as stated" in (N5) accordingly.
 F13 (§6.2; §0 S5). The script checks satisfiability of 3 XOR equalities + 2 forbidden cycles for one STRICT
    (tie-free) order per world on 4 families; 1442 permutation triples = 266 distinct acceptance patterns; no
    lightness, no ties/thresholds, 2 of 16 TRI cycles (with all 16 and full 2 x 4 biorders: 93340 patterns). State
    exactly this; "the holonomy argument genuinely needs the continuum" is a heuristic reading.
 F14 (§0, Most promising next step). "jumps are harmless for the Baire argument" is false for dense jumps (a strictly
    increasing level map can have nowhere dense image; §9.1 example); flats are also countable — their harm is
    non-injectivity. Rewrite as in §9.1.
 F15 (cosmetic). Lemma 2.1: state "V undominated" in the lemma (it is standing); Prop 3.1: note that the inequality
    needs no case hypothesis (case (a) only makes T_0(C_m) non-null); §0 S1-S5 labels: Lemma 4.1's "Hence", (N3),
    (N5), §6.2 and the next-step paragraph are not PROVED in the stated form.

## 11. Verdicts

 Lemma 2.1 (flip invariance): CORRECT (no completeness; V once; XOR at-least-one at E in F_12).
 Corollary 2.2 (single-triple criterion): CORRECT; the "Relation to (M2*)" paragraph CORRECT WITH MINOR FIXES (F3).
 Corollary 2.3 (absorption): CORRECT; Reading needs F4.
 Proposition 3.1 (far-end tails are one good piece): CORRECT (no V, no completeness, as claimed).
 Corollary 3.2: CORRECT (case (b) wording F5).
 Lemma 4.1: statement CORRECT (trivial); its consequence "only edge-23 XOR can produce acc_2(P_2-debt, P_3-credit)"
   and §0 S3 WRONG as stated (counterexample: Prop 3.1).
 Proposition 4.2: (a), (b) CORRECT; (c) CORRECT WITH MINOR FIXES (true for single inferences; "covers no more than
   (b)" unproved); the "uncovered middle" conclusion and (N3) INCOMPLETE/WRONG as worded (F7).
 Remark 4.3: CORRECT (bundling list incomplete, F8).
 Lemmas 5.1, 5.2, 5.3: CORRECT. Proposition 5.4: CORRECT under (TC). Corollary 5.5: CORRECT.
 Theorem 5.6: CORRECT. Every step re-derived ((LH) -> no slab band <=_d A_k; covered level -> full band <=_d A_k by
   (X2)/(X2'); Baire on a closed ray with homeomorphic level maps). Hypotheses can and should be weakened (F1: (TC)
   -> (TC6); F9: meagreness only near inf). Item (6): hypotheses not shown inconsistent with the known shape and not
   vacuous; the meagreness part holds automatically at poor far ends (Lemma R3), giving Corollary R4; (TC) is
   untested and fails in the only explicit candidate (order-separated valuation).
 §6: (N1), (N2), (N4) CORRECT; (N3) second half WRONG as worded; (N5) overstated (F12); 6.1 description CORRECT,
   kill CORRECT for the restricted class only; 6.2/script: verifies only satisfiability of five constraints on
   single tie-free representatives (F13).
 §0 "Most promising next step": contains a false claim about jumps (F14).
 No GAP in any proof of a numbered result; no numbered result is WRONG. The errors are in interpretive sentences
 (Lemma 4.1's "Hence", Prop 4.2's "middle", (N3), (N5), the next-step paragraph).

---
# Part 3. TC notes
# TC_notes — removing (TC) and the meagreness hypothesis from M2 Theorem 5.6

Standing (unless stated): n = 3; all three rankings complete with (G), (IB); (S). "V undominated" is stated
where used (it is the reductio hypothesis throughout §§3-5). Notation of M2 §5 / RM2: interior selections
E in F_12, E' in F_13, F in F_23; intervals I, I', J, J', K, K'; the six families
  A(x)  = P_1 n {t_12 > x} n {t_13 in J}     A'(x) = P_1 n {t_13 > x} n {t_12 in I}     (o_23: debt_1)
  D(x)  = P_2 n {s > x} n {t_12 in I'}       D'(x) = P_2 n {t_12 < 1/x} n {s in K}       (o_13: debt_2)
  C(x)  = P_3 n {t_13 < 1/x} n {s in K'}     C'(x) = P_3 n {s < 1/x} n {t_13 in J'}       (o_12: debt_3)
(s = t^2_3 = |g_2|/|g_3|), x >= x_0, pairwise disjoint as in M2 §5; acc_k(X,Y) :<=> V + debt_k(X) + cred_k(Y)
<=_k V; h_XY(y) := inf{x >= x_0 : acc_k(X(x), Y(y))} (X a debt family of world k, Y a credit family of k).
Labels PROVED / PLAUSIBLE / OPEN. Written incrementally; §0 written last.

## 0. Status summary (written last)

P1 is NOT solved: (T2) is reduced to (T1); (T1) and (T3) remain OPEN in general; all three are settled when the far
ends of the edges are local chains. PROVED (full proofs in §§3-6; nothing here is refereed yet):
 S1 (Def 3.1, Lemmas 3.2-3.3) HEAVY LEVELS: a level z of world k on edge [e_k,e_l'] is heavy if two-sided P_k-bands
    at z are, for every width, strictly AC against one fixed credit set. A level covered from above AND below (P1A
    (X2)/(X2') and (X1)) is never heavy (two-sided kill, using (LH)).
 S2 (Lemma 3.4) Under (Z1) the cycle maps h_AD, h_DC, h_CA are unbounded (RM2 §7.2 had this as an assumption).
 S3 (Lemma 3.5) Every flat of one of the twelve threshold maps is a heavy level of the debt family's owner (RM2 F11);
    every JUMP of h_XY at y* is, via the XOR at E, E' or F, a heavy level y* of the OWNER of Y in its own frame.
 S4 (Thm 3.6, Cor 3.7) (TC6) holds as soon as there are no high heavy levels in any of the six frames. Hence M2 Thm 5.6
    WITHOUT (TC): if V is undominated, then either some frame carries heavy levels at arbitrarily high levels (none
    of them covered from both sides), or in each of the two triples some frame has a non-meagre set of high levels
    not covered from above.
 S5 (Lemma 3.9, Cor 3.8, Cor 3.10) At a far end that is a LOCAL CHAIN (any two selections near the vertex block are
    pointwise comparable; e.g. RM2's poor ends, or precise monotone paths) every high level is covered from both
    sides. So: if all six far ends (both vertex ends of every edge) are local chains, V is dominated. This is RM2
    Cor R4 without (TC6), at the price of six ends instead of three.
 S6 (§4: Props 4.2-4.5, Thm 4.7, Cor 4.8) Holonomy with completed graphs, no continuity: reverse cycles occur in
    boxes and need one of three specific defects of the second-triple maps (flat of h_A'D, jump of h_AC', flat of
    h_D'C), i.e. heavy levels in frames (1,3), (3,2), (2,1) (Prop 4.2 = M2 Prop 5.4(b) without (TC)); otherwise the
    balanced triples form an arc B (Prop 4.3), and at EVERY balanced triple one of six one-sided germs (right or
    left, at the levels a, b, c in frames (1,2), (2,3), (3,1)) is heavy (Prop 4.5 = M2 Cor 5.5 without (TC); left
    germs appear exactly at jumps and are moved to the owner by XOR). Every jump of f, g, k (dense or not) is a flat
    of a coordinate of B, hence a heavy level (Prop 4.4). Cor 4.8: the correct Baire statement (M2 Thm 5.6 holds
    with (TC) weakened to "f, g, k homeomorphisms at high levels + none of the three defects of Prop 4.2"); and a
    rigidity result: if two frames of a triple are doubly covered at high levels (e.g. local-chain ends) and the
    other triple has no high heavy levels, then in the third frame NO high level is covered from both sides.
 S7 (Example 4.9) In curve form, RM2's dense-jump example is a covering of the curve by the countably many flats at
    rational levels (heavy levels) and the preimage of a nowhere dense set: no category/measure/order-type argument
    along the curve can avoid excluding single heavy levels. So (T2) reduces exactly to (T1).
 S8 (Props 5.1-5.3) Anatomy of a heavy level: covered from one side => one-sidedly heavy on the other; impossible in
    a frame with a local-chain far end; at a rich far end it is also a heavy CREDIT level of the edge partner at
    the same edge level (no new kill: the same crossings are needed).
 S9 (Lemma 6.1, Prop 6.3) Uncovered = crossed only nestedly (or jumped over); path geometry alone allows a far end at
    which every high level is uncovered from both sides (K Prop 4.8 with amplitude -> 0 at the vertex).
OPEN: (T1) a heavy level at a level crossed only nestedly (single-germ problem, now confined to frames whose far
end is not a local chain); (T3) meagreness of uncovered levels at non-chain far ends; six ends -> three ends
(TC-F6).
Single most promising next step: a FAR-END CHAIN LEMMA — show that (S) + V undominated force the selections near
each vertex block of each edge to be pairwise comparable (a local chain). Everything left open lives at
non-chain far ends (Prop 5.2, Lemma 3.9), Cor 3.10 then gives P1, and near the vertex block the far-end tools
(beta -> inf (ENDS), the AC pairs (S_AC^i) with credit tails, M2 Prop 3.1, Prop 5.3) are available, unlike in the
global chain question of P1A §12. The concrete test case is the nested zigzag of Prop 6.3.

## 1. Plan and the main idea

A threshold map h_XY is a real nondecreasing function; its defects are FLATS (h constant on an interval) and
JUMPS. In world k's comparison of a debt family X with a credit family Y,
 - a flat of h_XY at value l is a jump of X's chain across a stretch of Y: world k's two-sided debt germ of X at
   level l (X's owner frame = world k's frame on X's edge) is heavier than a FIXED credit band of Y (RM2 F11);
 - a jump of h_XY at y* is a jump of Y's chain across a stretch of X: world k's two-sided credit germ of Y at y*
   is worth more than a fixed debt band of X. World k sees Y transversally, but Y lies in an XOR region, and the
   XOR at the corresponding interior selection moves this to Y's OWNER: the owner's two-sided debt germ of Y at
   level y* (in the owner's own frame) is heavier than a fixed credit set.
So both defects are the same object: a HEAVY LEVEL (Def 3.1) — a single level of a world's own edge at which
two-sided debt bands are not compensated by a fixed credit set. Heavy levels are killed by coverage of that level
from BOTH sides (Lemma 3.2), they cannot occur at local-chain far ends (Lemma 3.9), and in their absence (TC6)
holds automatically (Theorem 3.6). So (TC6) is implied by "no heavy level at high levels in the six frames" (a
hypothesis about single levels of single worlds, not about cross-world tail comparisons), and M2 Thm 5.6 becomes
a statement without (TC) (Cor 3.7). §4 redoes the holonomy with completed graphs (no continuity at all) and shows
that every jump, dense or not, of the cycle maps becomes a flat of a level coordinate along the completed holonomy
curve, hence a heavy level (Prop 4.4); this is why dense jumps are a genuine escape for any category/measure
argument along the curve (Example 4.9):
(T2) reduces to (T1). (T1) — excluding a single heavy level at a level that is not covered from both sides — is
the old single-germ problem and stays OPEN (§5). (T3) is proved at local-chain far ends and OPEN at far ends
approached nestedly (§6).

## 2. Inputs (exact labels; refereed where stated)

(XOR) G3 Lemma 3.1 (RB5 §2 (I1)), in the three forms M2 Lemma 5.1 (k1)-(k3) (RM2 §6.2 CORRECT), but for ARBITRARY
   sets in the regions, not only family members:
   at E:  for B subset B_0(E) = P_1 n {t_12 < beta_E}, T subset T_0(E) = P_2 n {t_12 > alpha_E}:
          acc_1(B,T) or acc_2(T,B), and not both if V is undominated and B u T is non-null;
   at E': for B subset P_1 n {t_13 < beta'}, T subset P_3 n {t_13 > alpha'}: acc_1(B,T) or acc_3(T,B), not both;
   at F:  for B subset P_2 n {s < beta^2}, T subset P_3 n {s > alpha^2}: acc_2(B,T) or acc_3(T,B), not both.
   (The family regions: A' subset B_0(E), D subset T_0(E); A subset P_1 n {t_13 < beta'}, C' subset
   P_3 n {t_13 > alpha'}; D' subset P_2 n {s < beta^2}, C subset P_3 n {s > alpha^2}; RM2 §6.1, regions.py.)
(TRI) B Lemma 3.1 (RB5 §7 CORRECT); M2 Lemma 5.3 (no tail cycles (Z1), (Z2); RM2 §6.3 CORRECT).
(L52) M2 Lemma 5.2 (RM2 §6.3 CORRECT): for every debt family X of world k and every non-null credit set Y of k
   (outside P_k), acc_k(X(x), Y) for all large x; hence every h_XY is finite. And (RM2 §7.2) h_A'D, h_AC', h_D'C
   are unbounded.
(YD) Lemma yard(a) of "Fineness Spreads Along Edges" (= P1A Lemma 2.1, refereed RK §2.3), at any world k and edge
   [e_k,e_l], m the third world: for every non-null A there is b < inf such that every measurable subset of the
   tail D_km n {tau^k_m > b} (and of D_kl n {tau^k_l > b}) is <=^k_d A, and for every b' >= b and every open
   interval I the set Z_I(A) := P_k n {tau^k_m > b'} n {tau^k_l in I} is non-null and <=^k_d A.
   Here tau^k_l := |g_k|/|g_l| on D_kl is world k's frame on edge kl (tau^1_2 = t_12, tau^2_3 = s, tau^3_1 = 1/t_13,
   tau^1_3 = t_13, tau^2_1 = 1/t_12, tau^3_2 = 1/s).
(LH),(DH) LH Thm 4.1 = Thm LH of the note (RLH CORRECT WITH MINOR FIXES): at every world k and every non-null R
   there is an SI pair (A,T) of world k with A non-null, T subset R; and an AC pair (A,S) with A subset R.
(X1),(X2) P1A Thm 3.1 (X1), (X2), in world k's frame (re-checked in M2 Thm 5.6 / RM2 §6.6 step 3); (X2') P1A
   Lemma 4.1 with the AC pair of LH 5.1 (RLH CORRECT after M5): the AC pair (A'',W) has A'' subset Z_I(A) (a
   subset of the tail of (YD)) at any prescribed levels I away from z.
(L30) P1A Lemma 3.0 (comparable approaches converge), any frame. (ENDS) Lemma ends of the note (RK §2.2): along
   q_m -> q_e (q_e the point of {C_q = D_l} nearest e_k) with C_{q_m} != D_l, beta^{(k)}_m -> inf.
(T56) M2 Prop 5.4, Cor 5.5, Thm 5.6 (RM2 §6.4-6.6 CORRECT), with RM2 F1 (Lemma R1: (TC) may be replaced by (TC6))
   and F9 (only levels above some M_k are used), both PROVED in RM2 §2.2, §6.6; RM2 Lemma R3 (PROVED in RM2 §7.1).
(IB-comp) Composition: by (IB) and transitivity, if (B_i, T_i), i = 1,2, are weakly SI pairs of world k with the four
   sets pairwise disjoint, then (B_1 u B_2, T_1 u T_2) is weakly SI (CCF §6; context argument). Debt comparisons
   compose likewise: B_i <=^k_d R_i (i = 1,2), all four sets pairwise disjoint => B_1 u B_2 <=^k_d R_1 u R_2.

## 3. Heavy levels; (TC6) without (TC); M2 Theorem 5.6 without (TC)

Throughout §3 "level" means a number l in (0,inf) in one of the six FRAMES (k,l') = world k on edge [e_k,e_l'],
coordinate tau := tau^k_{l'}. The owner frame of a family: A (1,2), A' (1,3), D (2,3), D' (2,1), C (3,1), C' (3,2);
the parameter x of X(x) is a level in its owner frame (X(x) = P_k n {tau > x} n {slab}).

**Definition 3.1.** Let (k,l') be a frame and z in (0,inf).
 (a) z is COVERED FROM ABOVE if some index q* of [e_k,e_l'] has beta^{(k)}_{q*} = z and is the limit of open-edge
     indices q_m with C_{q_m} >=pw_k C_{q*} and beta^{(k)}_{q_m} > z (exactly "covered" in M2 Thm 5.6; q* silent
     or precise).
 (b) z is COVERED FROM BELOW if some index q* has beta^{(k)}_{q*} = z and is the limit of indices q_m with
     C_{q_m} <=pw_k C_{q*} and beta^{(k)}_{q_m} < z (the hypothesis of P1A (X1)).
 (c) z is a HEAVY LEVEL of world k in the frame (k,l') if there is a non-null measurable gamma subset H' \ P_k such
     that for every eps > 0 the pair (P_k n {|tau - z| < eps}, gamma) is strictly AC at world k:
        V <_k V + debt_k(P_k n {|tau - z| < eps}) + cred_k(gamma).
     By (G) it suffices that this holds for some sub-band (e.g. a slab band X(z-eps)\X(z+eps)) for every eps.
 NK^+, NK^- denote the sets of levels not covered from above, resp. below.

**Lemma 3.2 (two-sided kill). PROVED.** If z is covered from above and from below in the frame (k,l'), then for
every non-null A there is eps > 0 with D_kl' n {|tau - z| < eps} <=^k_d A.
Proof. Let m be the third world. (YD) gives b such that every measurable subset of the tail
Tl := D_km n {tau^k_m > b} is <=^k_d A, and yardsticks Z_I := Z_I(A) subset Tl for every interval I.
 From below: (X1) at the index q* of (b) with yardstick Z_{(0,z/2)} (its proof needs only that the yardstick is a
 subset of debt(C_{q*}) n debt(C_{q_m}) and <=_d A; this holds for large m, since beta_m -> z by (L30)) gives,
 for large m, the left band L := D_kl' n {beta_m <= tau < z} with L <^k_d R_2 := Z_{(0,z/2)}.
 From above: if the index q* of (a) is silent (alpha* > z), (X2) with the yardstick R_1 := Z_{(z+delta,z+2delta)},
 delta := min(1,(alpha*-z)/3) (eventually in the silence of C_{q*} and C_{q_m}, by (L30)), gives the right band
 R := D_kl' n {z < tau < beta'_m} with R <=^k_d R_1. If q* is precise, (X2') with the AC pair (A'',W) of LH 5.1,
 A'' subset Z_{(z+delta,z+2delta)} (delta := 1), gives R <^k_d R_1 := A''.
 Take eps > 0 smaller than z - beta_m, beta'_m - z, delta and z/2. Then the two one-sided bands of width eps
 (subsets of L, R) are <=^k_d R_2, R_1 by (G); R_1, R_2 are disjoint subsets of Tl (different tau-levels) and
 disjoint from the band (tau-levels within eps of z; R_1 at levels > z + delta, R_2 at levels < z/2); the level set
 {tau = z} is null. By (IB-comp) the two-sided band is <=^k_d R_1 u R_2, and R_1 u R_2 subset Tl gives
 R_1 u R_2 <=^k_d A. ∎
Uses: completeness, (G), (IB) at world k ((X1) uses (T1); (YD)); (S); LH 5.1 (all worlds complete) only in the
precise case.

**Lemma 3.3 (heavy levels are not doubly covered). PROVED.** A level covered from above and from below in the
frame (k,l') is not a heavy level of world k there.
Proof. Let gamma witness heaviness. (LH) at world k gives an SI pair (A_k, gamma') with gamma' subset gamma.
Lemma 3.2 gives eps with b := P_k n {|tau - z| < eps} <=^k_d A_k. Then (context cred_k(gamma'), silent on b u A_k:
b subset P_k is disjoint from gamma', and A_k n gamma' is empty)
  V + debt(b) + cred(gamma) <=_k V + debt(b) + cred(gamma') <=_k V + debt(A_k) + cred(gamma') <_k V,
the first step by (G) (more credit on gamma \ gamma'). So (b, gamma) is SI, not strictly AC. ∎

**Lemma 3.4 (the cycle maps are unbounded). PROVED.** If V is undominated, f := h_AD, g := h_DC, k := h_CA are
unbounded. (For h_A'D, h_AC', h_D'C see (L52).)
Proof. Recall x > h_XY(y) => acc_k(X(x),Y(y)) ({x : acc} is an up-ray with infimum h_XY(y), (G)). If f <= M
everywhere: take a > M, c > k(a), b > g(c) (finite by (L52)); then acc_3(C(c),A(a)), acc_2(D(b),C(c)) and, since
a > M >= f(b), acc_1(A(a),D(b)): a (Z1) cycle, contradicting (TRI). If g <= M: b := M + 1, a > f(b), c > k(a);
then b > g(c): (Z1). If k <= M: c := M + 1 > k(a) for all a, b > g(c), a > f(b): (Z1). ∎
(This answers RM2 §7.2's remark that a bounded h_AD "is an extra assumption": it is excluded by (Z1).)

**Lemma 3.5 (flats and jumps are heavy levels). PROVED.** Let X be a debt family and Y a credit family of world
k, h := h_XY.
 (a) [flat] If h = l on a nondegenerate interval [y_1,y_2], then l is a heavy level of world k in X's owner frame,
     witnessed by gamma := Y(y)\Y(y') for any y_1 < y < y' < y_2. No V-hypothesis.
 (b) [jump] Suppose V is undominated. If h(y*-) < h(y*+) at some y* > x_0, then y* is a heavy level of the owner
     o of Y in Y's owner frame, witnessed by gamma := X*, where X* is any member far enough out of the tail family
     listed below (a debt set of world k lying in the XOR region opposite to Y's region):
       Y = D (k = 1; maps h_AD, h_A'D): X* := A'(x**) subset B_0(E), XOR at E, o = 2;
       Y = C (k = 2; maps h_DC, h_D'C): X* := D'(x**) subset P_2 n {s < beta^2}, XOR at F, o = 3;
       Y = A (k = 3; map h_CA):         X* := C'(x**) subset P_3 n {t_13 > alpha'}, XOR at E', o = 1;
       Y = C' (k = 1; map h_AC'):       X* := A(x**) subset P_1 n {t_13 < beta'}, XOR at E', o = 3.
Proof. (a) Fix y_1 < y < y' < y_2 and eps > 0 with l - eps >= x_0. Since h(y) = h(y') = l:
acc_k(X(l+eps), Y(y')) and not acc_k(X(l-eps), Y(y)); by completeness
  M := V + debt(X(l+eps)) + cred(Y(y')) <=_k V <_k V + debt(X(l-eps)) + cred(Y(y)) = M + debt(b_eps) + cred(gamma),
with b_eps := X(l-eps)\X(l+eps), gamma := Y(y)\Y(y') (non-null: positive joint density). M is silent on
b_eps u gamma, so (IB) turns M <_k M + debt(b_eps) + cred(gamma) into V <_k V + debt(b_eps) + cred(gamma).
b_eps subset P_k n {l - eps < tau <= l + eps}, gamma n P_k empty; (G) and Def 3.1(c).
(b) Take x_1 < x_2 in (h(y*-), h(y*+)) and y' < y* < y''. Then x_1 > h(y') (so acc_k(X(x_1),Y(y'))) and
x_2 < h(y'') (so not acc_k(X(x_2),Y(y''))). With N := V + debt(X(x_2)) + cred(Y(y'')), alpha := X(x_1)\X(x_2) (fixed,
non-null), delta := Y(y')\Y(y''): N + debt(alpha) + cred(delta) <=_k V <_k N, hence (IB) (N silent on alpha u delta)
V + debt(alpha) + cred(delta) <_k V: (alpha, delta) is strictly SI at world k, for all y' < y* < y''.
By (YD) at world k (alpha non-null), X* := the listed tail member with x** large is <=^k_d alpha and disjoint from
alpha and delta (A' at t_12 in I vs A at t_12 > x_0; D' far out vs D'-bands at bounded levels; etc. — in the cases
where X* and alpha belong to the same family, x** > x_2 makes X* subset X(x_2), disjoint from alpha). Then
(context cred(delta), silent on X* u alpha) V + debt(X*) + cred(delta) <=_k V + debt(alpha) + cred(delta) <_k V:
acc_k(X*, delta). X* and delta lie in the two regions of the XOR named (delta subset Y-region), so its "at most one"
half (V undominated, X* non-null) gives: not acc_o(delta, X*), i.e. (delta, X*) is strictly AC at the owner o
(completeness). delta subset P_o n {y' < tau_o <= y''} (Y(y) = P_o n {tau_o > y} n slab), so taking y', y'' within
eps of y* shows: every two-sided P_o-band at y* is strictly AC against gamma := X* (G), and X* n P_o is empty. ∎
Remarks. (i) (a) is RM2 F11's flat statement; (b) is new: RM2 F11 noted that a jump gives only a mixed comparison
(credit band versus debt band) at world k; the XOR transfer converts it into an own-frame heavy level of the owner.
(ii) In (b) the witness gamma = X* can be taken arbitrarily far out (any x** >= some x_3).

**Theorem 3.6 ((TC6) from the absence of high heavy levels). PROVED.** Let V be undominated and suppose that for
some M < inf no level z > M is heavy (for the corresponding world) in any of the six frames (1,2), (1,3), (2,3),
(2,1), (3,1), (3,2). Then each of h_AD, h_DC, h_CA, h_A'D, h_AC', h_D'C is an increasing homeomorphism of a ray
[y_0,inf) onto a ray; i.e. (TC6) holds, hence (RM2 Lemma R1) (TC) holds.
Proof. Each h is nondecreasing, finite (L52) and unbounded (Lemma 3.4, (L52)). Choose y_0 > M with h(y_0) > M.
A flat of h on a nondegenerate subinterval of [y_0,inf) has value >= h(y_0) > M and is a heavy level in X's owner
frame (Lemma 3.5(a)): excluded. A jump at y* > y_0 > M is a heavy level y* in Y's owner frame (Lemma 3.5(b)):
excluded. The frames used: flats of h_AD, h_DC, h_CA, h_A'D, h_AC', h_D'C in (1,2), (2,3), (3,1), (1,3), (1,2),
(2,1); jumps (owners of D, C, A, D, C', C) in (2,3), (3,1), (1,2), (2,3), (3,2), (3,1). So h is continuous and
strictly increasing on (y_0,inf) and unbounded: an increasing homeomorphism of [y_0 + 1, inf) onto
[h(y_0 + 1), inf). ∎

**Corollary 3.7 (M2 Theorem 5.6 without (TC)). PROVED.** Let n = 3, all rankings complete with (G), (IB), (S), and
suppose V is undominated. Then at least one of:
 (i) for every M some frame (of the six) has a heavy level z > M — and every such z is not covered from both sides
     (Lemma 3.3);
 (ii) there is k in {1,2,3} with NK^+_k n (M,inf) non-meagre for every M (frames (1,2), (2,3), (3,1)), AND there is
      k' with the same in the frames (1,3), (2,1), (3,2).
Proof. If (i) fails, Theorem 3.6 gives (TC6) on a ray, hence (TC) (RM2 Lemma R1). M2 Thm 5.6 with RM2 F9 (only
high levels) then forbids NK^+_k n (M_k,inf) meagre for all k = 1,2,3, and its symmetric form (RM2 §6.6 item 5,
families A', D', C') forbids the same on the second triple. ∎
So (TC) is replaced by a hypothesis about single levels of single worlds ("no high heavy level"), which is
automatic wherever levels are covered from both sides.

**Corollary 3.8. PROVED.** If, in each of the six frames, every level above some M is covered from above and from
below, then V is dominated.
Proof. Lemma 3.3 excludes (i) of Cor 3.7, and NK^+ n (M,inf) is empty, excluding (ii). ∎

**Lemma 3.9 (local-chain far ends cover all high levels from both sides; generalizes RM2 Lemma R3). PROVED.**
Fix a frame (k,l'), let q_e be the point of {q in [e_k,e_l'] : C_q = D_l'} nearest e_k, and suppose there is a
stretch S := (q_e - eps, q_e) (on the e_k side; eps small, so S is in the open edge) on which any two selections
are pointwise comparable (a LOCAL CHAIN at the far end; e.g. RM2's "poor" end, all C_q = E_l'(beta_q), alpha = inf).
Then there is M such that every z > M is covered from above and from below. Only (G) at k, l' and (S) are used.
Proof. On S, C_q != D_l' (q_e is the nearest point), so beta_q < inf (beta = inf forces alpha = inf, i.e. D_l').
Any sequence in S converging in S splits into a <=pw and a >=pw subsequence, so (L30) makes q -> (alpha_q,beta_q)
continuous on S; by (ENDS) beta -> inf at q_e. Fix q_1 in S, M := beta(q_1). Let z > M. The set
Z := {q in [q_1,q_e) : beta_q = z} is non-empty (IVT), closed in [q_1,q_e) and bounded away from q_e, hence
compact. Above: q* := max Z; on (q*,q_e) beta > z (IVT); q_m in (q*,q_e), q_m -> q* are comparable with q* and
have beta_m > z = beta*, so C_{q_m} >=pw C_{q*} (<=pw would force beta_m <= beta*). Below: q** := min Z > q_1; on
[q_1,q**) beta < z; q_m in [q_1,q**), q_m -> q** are comparable with q** and have beta_m < z, so C_{q_m} <=pw C_{q**}.
All q_m lie in the open edge. ∎

**Corollary 3.10. PROVED.** If each of the six far ends (frame (k,l'): the end D_l' of [e_k,e_l']; i.e. both
vertex ends of every edge) is a local chain — in particular if each is poor (only endpoint-family selections
E_l' near it) — then V is dominated. [Lemma 3.9 + Cor 3.8.] This removes (TC6) from RM2 Cor R4 at the price of
requiring all six ends instead of the three ends of one triple.
Note. By Lemma 3.3 and Lemma 3.9 a frame whose far end is a local chain has no high heavy levels; so in Cor 3.7
both alternatives point at NON-CHAIN far ends: (i) at the frame carrying the heavy levels, (ii) at one frame of
each triple (RM2 Cor R4's richness is the special case "not poor").

## 4. The completed holonomy (no continuity at all); why (T2) reduces to (T1)

Standing for §4: V undominated. f := h_AD (b -> a), g := h_DC (c -> b), k := h_CA (a -> c); finite (L52), nondecreasing,
unbounded (Lemma 3.4). For nondecreasing phi: phi(t-) := sup_{t'<t} phi(t'), phi(t+) := inf_{t'>t} phi(t');
phi^-(t) := phi(t-), phi^+(t) := phi(t+). Completed graphs (closed, each a monotone arc):
  Gamma_f := {(a,b) : f(b-) <= a <= f(b+)},  Gamma_g := {(b,c) : g(c-) <= b <= g(c+)},  Gamma_k := {(c,a) : k(a-) <= c <= k(a+)}.
(For a monotone phi and p <= q: the union of the fibres [phi(t-),phi(t+)], t in [p,q], is [phi(p-),phi(q+)]: given v
in the right side let t_0 := inf{t in [p,q] : phi(t+) >= v}; then phi(t_0+) >= v >= phi(t_0-). Used below as (U).)
(F-c) [Ferrers, credit form; completeness + (IB)]: acc_k(X,Y_1) and not acc_k(X,Y_2) => Y_2 <^k_c Y_1, hence
acc_k(X',Y_2) => acc_k(X',Y_1) for every debt set X' of world k. (F-d) likewise for debt sets.

**Lemma 4.1. PROVED.** (a) If (a,b) in Gamma_f then acc_1(A(a'),D(b')) for all a' > a, b' < b, and not
acc_1(A(a'),D(b')) for all a' < a, b' > b. Likewise for Gamma_g (world 2) and Gamma_k (world 3).
(b) [(Z1) <=> H^+ >= id] For every a: a <= H^+(a) := f^+(g^+(k(a))).
(c) [reverse cycles come in boxes] If a < H^-(a) := f^-(g^-(k(a))), then for some a_1 > a, b_- < b, c < c_+, every
point of the box Q := [a,a_1] x [b_-,b] x [c,c_+] is a REVERSE CYCLE: not acc_1(A(a'),D(b')), not acc_2(D(b'),C(c')),
not acc_3(C(c'),A(a')). Moreover b_-, c can be taken >= any prescribed bound once a is large.
Proof. (a) b' < b: f(b') <= f(b-) <= a < a', and x > f(y) => acc. a' < a, b' > b: f(b') >= f(b+) >= a > a', and
x < f(y) => not acc. (b) For c > k(a): acc_3(C(c),A(a)); for b > g(c): acc_2(D(b),C(c)); (Z1)-freeness (TRI) forces
not acc_1(A(a),D(b)), i.e. a <= f(b), for all such c, b: a <= inf_{c>k(a)} f^+(g(c)) = f^+(g^+(k(a))) (right
continuity of f^+, monotonicity of g). (c) Pick a_1 in (a, H^-(a)). By definition of H^- there are c < k(a) and
b_- < g(c) with f(b_-) > a_1; pick b in (b_-, g(c)) and c_+ in (c, k(a)). For (a',b',c') in Q: a' <= a_1 < f(b_-)
<= f(b'); b' <= b < g(c) <= g(c'); c' <= c_+ < k(a) <= k(a'). The three strict inequalities give the three
rejections. Since f(b_-) > a and f is finite on bounded sets, b_- -> inf as a -> inf; then g(c) > b_- forces c -> inf. ∎

**Proposition 4.2 (reverse cycles need heavy levels on the other triple). PROVED.** Suppose a < H^-(a) with a
large, and let Q be the box of Lemma 4.1(c). Then at least one of:
 (i) h_A'D is constant on [b_-, b] (a flat, at the value theta := h_A'D(b));
 (ii) h_AC' has a jump at psi_1 := sup{u : acc_1(A(a_1),C'(u))}, with h_AC'(psi_1-) <= a < a_1 <= h_AC'(psi_1+);
 (iii) h_D'C is constant on [c, c_+] (at the value chi := h_D'C(c)).
Hence (Lemma 3.5) there is a heavy level in frame (1,3) (at theta), (3,2) (at psi_1) or (2,1) (at chi); and theta, psi_1,
chi -> inf as a -> inf. Consequently: if for some M no level > M is heavy in the frames (1,3), (2,1), (3,2), then
H^-(a) <= a for all large a.
Proof. Route: we show that if (i)-(iii) all fail, there is a (Z2) cycle (x',u,w):
 acc_1(A'(x'),C'(u)), acc_3(C'(u),D'(w)), acc_2(D'(w),A'(x')), contradicting (TRI).
Step 1 (world 1). Let theta := h_A'D(b) (> x_0 for b large, h_A'D unbounded). Claim: some x' has
 (G1) not acc_1(A'(x'),D(b)) and A'(x') <=^1_d A(a_1).
 If not, every x' < theta (where not acc_1(A'(x'),D(b))) has A'(x') >^1_d A(a_1). For b'' in [b_-,b] we have not
 acc_1(A(a_1),D(b'')) (Q), so not acc_1(A'(x'),D(b'')) ((F-d): acc_1(A'(x'),D(b'')) and A(a_1) <=_d A'(x') would give
 acc_1(A(a_1),D(b''))); hence h_A'D(b'') >= theta for all b'' in [b_-,b], and <= theta by monotonicity: (i).
Step 2 (world 3). Claim: there are u, w with
 (G3) acc_1(A(a_1),C'(u)), acc_3(C'(u),D'(w)), acc_2(D'(w),C(c)).
 (alpha) Suppose some u has acc_1(A(a_1),C'(u)) and C'(u) <^3_d C(c_+). Let chi := h_D'C(c). If some w > chi has
 acc_3(C'(u),D'(w)), then (G3) holds (w > chi gives acc_2(D'(w),C(c))). Otherwise, for w > chi and c' in [c,c_+]:
 C'(u) <^3_d C(c_+) <=^3_d C(c') ((G)), so acc_3(C(c'),D'(w)) would give acc_3(C'(u),D'(w)); hence
 not acc_3(C(c'),D'(w)), and the "at least one" half of the XOR at F gives acc_2(D'(w),C(c')). So h_D'C(c') <= chi
 for c' in [c,c_+], and >= chi by monotonicity: (iii).
 (beta) Otherwise every u in U := {u : acc_1(A(a_1),C'(u))} has C'(u) >=^3_d C(c_+). U is a down-ray (less credit as
 u grows), non-empty for a_1 large ((L52) with Y := C'(x_0)), and bounded: for large u, acc_3(C'(u),A(a_1)) ((L52) at
 world 3), so not acc_1(A(a_1),C'(u)) (XOR at E', "at most one"). Put psi_1 := sup U < inf. For u < psi_1 and
 a' in [a,a_1]: not acc_3(C(c_+),A(a')) (Q) and C(c_+) <=^3_d C'(u) give not acc_3(C'(u),A(a')), so (XOR at E',
 "at least one") acc_1(A(a'),C'(u)): h_AC'(u) <= a. For u > psi_1: not acc_1(A(a_1),C'(u)), hence not
 acc_1(A(a'),C'(u)) for all a' <= a_1 (more debt): h_AC'(u) >= a_1. So h_AC'(psi_1-) <= a < a_1 <= h_AC'(psi_1+): (ii).
Step 3 (the cycle). With x' from (G1) and u, w from (G3):
 (P1) acc_1(A'(x'),C'(u)): from acc_1(A(a_1),C'(u)) and A'(x') <=^1_d A(a_1) (context cred(C'(u))).
 (P2) acc_2(D'(w),A'(x')): not acc_1(A'(x'),D(b)) gives (XOR at E, "at least one") acc_2(D(b),A'(x')); with
      not acc_2(D(b),C(c)) ((a_1,b,c) in Q), (F-c) gives C(c) <^2_c A'(x'); then acc_2(D'(w),C(c)) gives
      acc_2(D'(w),A'(x')).
 (P3) acc_3(C'(u),D'(w)) is in (G3).
 This is (Z2). Levels: theta = h_A'D(b) >= h_A'D(b_-) -> inf; psi_1 -> inf as a_1 -> inf (for fixed u,
 acc_1(A(a_1),C'(u)) for large a_1, (L52)); chi = h_D'C(c) -> inf since c -> inf (Lemma 4.1(c)) and h_D'C is
 unbounded (L52). The last sentence: Lemma 3.5 turns (i), (ii), (iii) into heavy levels in the frames of A' (1,3),
 of the owner of C' (3,2), of D' (2,1). ∎
Remark. Under (TC) this is M2 Prop 5.4(b)'s inequality H_1 <= id; the proof above needs no continuity: only the
three specific defects (i)-(iii) of the second-triple maps can carry a reverse cycle. (Only the "at least one"
halves of the three XORs are used, plus one "at most one" half (boundedness of U) and (TRI).)

**Proposition 4.3 (the balanced curve). PROVED.** Suppose H^-(a) <= a for all a >= a_* (e.g. by Prop 4.2). Let
 B := {(a,b,c) : a >= a_*, (a,b) in Gamma_f, (b,c) in Gamma_g, (c,a) in Gamma_k}   ("balanced triples").
Then: (a) B is closed and totally ordered by the product order; (b) its a-projection is [a_*,inf); (c) every fibre
F_a := {(b,c) : (a,b,c) in B} is a non-empty compact connected set (a point or a segment of the monotone arc
Gamma_g); (d) s := a + b + c maps B homeomorphically onto [s_*,inf); so B is an arc and its coordinates
l_1(s) = a, l_2(s) = b, l_3(s) = c are continuous, nondecreasing and unbounded; every high level of each of the
frames (1,2), (2,3), (3,1) is a value of the corresponding l_k.
Proof. (a) Closed: the three completed graphs are closed (one-sided limits are semicontinuous in the required
directions). Chain: let P = (a,b,c), P' = (a',b',c') in B with a < a'. From (c,a), (c',a') in Gamma_k: since
a < a' implies k(a+) <= k(a'-), c <= k(a+) <= k(a'-) <= c'. From (a,b), (a',b') in Gamma_f and a < a': b <= b' (if
b > b' then a >= f(b-) >= f(b'+) >= a' > a). If a = a': b < b' forces c <= c' (Gamma_g monotone: g(c-) <= b < b' <= g(c'+) excludes c > c'), and
b = b' leaves c, c' comparable trivially. So any two points are comparable. (b) Given a >= a_*, by (U) the set of b
with (b,c) in Gamma_g, (c,a) in Gamma_k for some c is [g(k(a-)-), g(k(a+)+)], and the set of a' with (a',b) in Gamma_f
for such b is [f(g(k(a-)-)-), f(g(k(a+)+)+)]. Its left end is <= f^-(g^-(k(a))) = H^-(a) <= a and its right end is
>= H^+(a) >= a (Lemma 4.1(b)); so a belongs to it, i.e. some (b,c) with (a,b,c) in B exists. (c) F_a = Gamma_g n
(Phi_f(a) x [k(a-),k(a+)]), Phi_f(a) := {b : f(b-) <= a <= f(b+)} an interval; a monotone arc meets a box in a
sub-arc (between two of its points in the box, every point of the arc is componentwise between them). (d) s is
injective on the chain B and continuous. Its image is an interval: if s_1 < t < s_2 were in s(B) with t not, let
P_- := sup{P : s(P) < t} and P_+ := inf{P : s(P) > t} (componentwise; in B by closedness, as limits of monotone
sequences in the chain); then s(P_-) < t < s(P_+) and a(P_-) = a(P_+) (if a(P_-) < a < a(P_+), the point of B over a
(by (b)) can be neither below P_- nor above P_+); so P_-, P_+ lie in one fibre, which is connected by (c): s takes
the value t on it, a contradiction. The image is unbounded (a unbounded) and closed below (the least point of the
compact fibre F_{a_*}). On {s <= S}, B is compact, so s^{-1} is continuous. Coordinates of a chain are nondecreasing
along s; a, b, c are unbounded (b -> inf because f(b+) >= a and f is finite on bounded sets; c -> inf because
g(c+) >= b). Intermediate values give the last claim. ∎

**Proposition 4.4 (flats of the curve are heavy levels). PROVED.** In the situation of Prop 4.3:
 l_1 is constant (= a*) on a nondegenerate s-interval  <=>  F_{a*} is not a point  <=>  f is constant (= a*) on a
 nondegenerate interval, or k jumps at a*;
and likewise l_2 (at b*: g constant = b*, or f jumps at b*) and l_3 (at c*: k constant = c*, or g jumps at c*).
Every such flat level is a heavy level: of world 1 in (1,2) at a*, of world 2 in (2,3) at b*, of world 3 in (3,1)
at c* (Lemma 3.5: flat of h_AD / jump of h_CA (owner of A = 1); flat of h_DC / jump of h_AD (owner of D = 2);
flat of h_CA / jump of h_DC (owner of C = 3)).
Proof. First equivalence: s is a homeomorphism and l_1 is the a-coordinate. If F_{a*} contains (b_1,c_1) != (b_2,c_2)
with b_1 < b_2: f(b-) <= a* <= f(b+) at b_1, b_2 gives f = a* on (b_1,b_2). If b_1 = b_2 and c_1 < c_2:
k(a*-) <= c_1 < c_2 <= k(a*+), a jump. Conversely, if f = a* on a maximal (b_1,b_2), points of B with a < a* have
b <= b_1 and points with a > a* have b >= b_2, so by continuity of l_2 and l_1 the fibre F_{a*} contains points
with b = b_1 and b = b_2; if k jumps at a*, F_{a*} contains points with c = k(a*-) and c = k(a*+) by the same
argument. l_2, l_3 likewise. ∎
So every jump of the cycle maps f, g, k — isolated or dense — is a flat of another coordinate of the balanced curve,
and both kinds of defects are heavy levels. Whether jumps are dense is irrelevant; what matters is whether the
(countably many) flat levels are covered (Cor 4.8, Example 4.9).

**Proposition 4.5 (M2 Cor 5.5 without continuity: six one-sided alternatives). PROVED.** Let (a,b,c) in B with
a, b, c large. Choose a'', u, w with STRICT acceptances acc_1(A'(a''),C(c)), acc_2(D'(w),A(a)), acc_3(C'(u),D(b))
(M2 Cor 5.5; RM2 §6.5), L_1 := C'(u) u D'(w), L_2 := A'(a'') u C'(u), L_3 := D'(w) u A'(a''), and split each
L_k = L_k^1 u L_k^2 into disjoint non-null parts. Then there are tail members X_1 := A'(x_1) (subset B_0(E)),
X_2 := D'(x_2) (subset P_2 n {s < beta^2}), X_3 := C'(x_3) (subset P_3 n {t_13 > alpha'}), depending only on L_1^2,
L_2^2, L_3^2, such that at least one of the following holds:
 (1+) for all a_1 > a: (A(a)\A(a_1), L_1^1) is strictly AC at world 1;      [right germ, frame (1,2), level a]
 (1-) for all a_1 < a: (A(a_1)\A(a), X_3) is strictly AC at world 1;       [left germ, frame (1,2), level a]
 (2+) for all b_1 > b: (D(b)\D(b_1), L_2^1) is strictly AC at world 2;      [right germ, (2,3), level b]
 (2-) for all b_1 < b: (D(b_1)\D(b), X_1) is strictly AC at world 2;       [left germ, (2,3), level b]
 (3+) for all c_1 > c: (C(c)\C(c_1), L_3^1) is strictly AC at world 3;      [right germ, (3,1), level c]
 (3-) for all c_1 < c: (C(c_1)\C(c), X_2) is strictly AC at world 3.       [left germ, (3,1), level c]
More precisely, world 1's failure gives (1+) or (2-), world 2's gives (2+) or (3-), world 3's gives (3+) or (1-);
and if a >= f(b) (e.g. f continuous at b), world 1's failure gives (1+) with L_1 in place of L_1^1 (similarly
b >= g(c) for world 2, c >= k(a) for world 3). Under (TC) this is exactly M2 Cor 5.5.
Proof. Let d := o_23(A(a) u A'(a'')) + o_13(D(b) u D'(w)) + o_12(C(c) u C'(u)) (six pairwise disjoint sets). Say
Fix_1 holds if there are a_1 >= a, b_1 <= b with acc_1(A(a_1),D(b_1)) and
  V + debt_1(alpha) + cred_1(L_1) <=_1 V + cred_1(delta),  alpha := A(a)\A(a_1), delta := D(b_1)\D(b);
Fix_2, Fix_3 analogously (world 2: D(b), C(c), L_2; world 3: C(c), A(a), L_3). If Fix_1: the models
V + debt(A(a)) + cred(D(b)) + cred(L_1) and V + debt(A(a_1)) + cred(D(b_1)) agree off alpha u delta u L_1, where they
are N + debt(alpha) + cred(L_1) and N + cred(delta) with N := V + debt(A(a_1)) + cred(D(b)) silent there; (IB) and Fix_1
give V + debt(A(a)) + cred(D(b)) + cred(L_1) <=_1 V + debt(A(a_1)) + cred(D(b_1)) <=_1 V, and adding the strict extra
(A'(a''),C(c)) (context silent on A'(a'') u C(c)) gives V + d <_1 V. Same at worlds 2, 3 (extras (D'(w),A(a)),
(C'(u),D(b)); the credit/debt roles of the six sets at each world are those of M2 Cor 5.5, checked in RM2
compose.py). So not all of Fix_1, Fix_2, Fix_3 hold (V undominated). By completeness, not Fix_1 means: for all
admissible (a_1,b_1), V + cred(delta) <_1 V + debt(alpha) + cred(L_1).
 World 1 fails. If (1+) fails, some a_1 > a has (alpha, L_1^1) weakly SI. For every b_1 < b, f(b_1) <= f(b-) <= a < a_1
 ((a,b) in Gamma_f), so acc_1(A(a_1),D(b_1)), and not Fix_1 gives
   V + cred(delta) <_1 V + debt(alpha) + cred(L_1^1) + cred(L_1^2) <=_1 V + cred(L_1^2)
 ((IB), context cred(L_1^2)): L_1^2 <^1_c delta for all b_1 < b. Transfer: (LH) at world 1 gives an SI pair
 (A*,L*) with L* subset L_1^2; by (YD) choose X_1 := A'(x_1), x_1 large, with X_1 <=^1_d A* (A' is world 1's high
 tail on edge 13) — X_1 subset P_1 is disjoint from L_1 subset P_2 u P_3 and from delta subset P_2. Then
   V + debt(X_1) + cred(delta) <_1 V + debt(X_1) + cred(L_1^2) <=_1 V + debt(X_1) + cred(L*) <=_1 V + debt(A*) + cred(L*) <_1 V,
 so acc_1(X_1,delta) for all b_1 < b; X_1 subset B_0(E), delta subset T_0(E); the XOR at E ("at most one") gives not
 acc_2(delta,X_1): (2-). If a >= f(b): for every a_1 > a, acc_1(A(a_1),D(b)), so b_1 := b (delta empty) is admissible
 and not Fix_1 reads V <_1 V + debt(alpha) + cred(L_1): (1+) with L_1.
 World 2 fails: as for world 1 with (D,C,L_2,(b,c) in Gamma_g); the transfer uses (LH) at world 2, X_2 := D'(x_2)
 (world 2's high tail on edge 21; disjoint from L_2 subset P_1 u P_3 and from C-bands) and the XOR at F
 (X_2 subset P_2 n {s < beta^2}, C-bands subset P_3 n {s > alpha^2}): (2+) or (3-).
 World 3 fails: (C,A,L_3,(c,a) in Gamma_k), X_3 := C'(x_3) (world 3's high tail on edge 32; disjoint from
 L_3 subset P_1 u P_2 and from A-bands), XOR at E' (A-bands subset P_1 n {t_13 < beta'}, X_3 subset
 P_3 n {t_13 > alpha'}): (3+) or (1-). ∎

**Lemma 4.6 (one-sided kills). PROVED.** In frame (k,l'), if z is covered from above, then for every non-null
credit set gamma (gamma n P_k empty) some right band P_k n {z < tau < z + eps} makes a weakly (indeed strictly)
SI pair with gamma; if z is covered from below, the same for some left band. Hence (1+), (2+), (3+) fail when
a, b, c respectively are covered from above, and (1-), (2-), (3-) fail when they are covered from below.
Proof. The one-sided halves of the proof of Lemma 3.2 give, for A_k from (LH) at world k with an SI pair
(A_k, gamma') (gamma' subset gamma), a one-sided band <=^k_d A_k; conclude as in Lemma 3.3. ∎

**Theorem 4.7 (holonomy without (TC)). PROVED.** Let n = 3, all rankings complete with (G), (IB), (S), V
undominated, and suppose that for some M no level > M is heavy in the frames (1,3), (2,1), (3,2). Then the balanced
curve B exists on a ray (Props 4.2, 4.3), and for every large s at least one of l_1(s), l_2(s), l_3(s) is NOT
covered from both sides in its frame ((1,2), (2,3), (3,1) respectively).
Proof. Prop 4.5 at the balanced triple B(s), and Lemma 4.6. ∎
**Corollary 4.8 (consequences). PROVED.** In the situation of Theorem 4.7, let G_k be the set of levels > M of the
frame (1,2), (2,3), (3,1) (k = 1,2,3) covered from both sides, and N_k := (M,inf) \ G_k.
 (a) The sets l_k^{-1}(G_k) (k = 1,2,3) have no common point at high s; equivalently [s_*,inf) = U_k l_k^{-1}(N_k).
 (b) If two of the three frames have all levels > M covered from both sides (e.g. their far ends are local chains,
     Lemma 3.9), then there is M' such that in the third frame NO level > M' is covered from both sides. [Choose
     s_M with l_j(s) > M for all j and all s >= s_M, and M' := max_j l_j(s_M). A level z > M' of the third frame is
     l_k(s) for some s >= s_M (Prop 4.3(d)); at B(s) the other two levels are > M, hence in G; Theorem 4.7.]
 (c) If each N_k is meagre and contains no flat value of l_k, then V is dominated. [Lemma below + Baire.]
 (d) Since flat values of l_k are heavy levels (Prop 4.4) and heavy levels lie in N_k (Lemma 3.3), the condition
     in (c) says: N_k meagre and l_k without flats at levels > M, i.e. f, g, k continuous and strictly increasing at
     high levels. In that case every balanced triple has a = f(b), b = g(c), c = k(a), so only (1+), (2+), (3+) occur
     in Prop 4.5, and the same argument needs only NK^+_k meagre: this is M2 Thm 5.6 with (TC) weakened to
     "f, g, k homeomorphisms at high levels, and none of the three defects (i)-(iii) of Prop 4.2" (no hypothesis on
     the other defects of h_A'D, h_AC', h_D'C, and no matchings).
 Lemma (preimages). If l: [s_*,inf) -> R is continuous and nondecreasing and N = U_i N_i is meagre (N_i nowhere
 dense) and contains no flat value of l, then l^{-1}(N) is meagre. Proof: let G be the union of the interiors of the
 flat intervals of l and K its (closed) complement. l^{-1}(N) n G is empty. K_i := l^{-1}(cl N_i) n K is closed; if it
 contained an interval J, l(J) would be an interval inside the nowhere dense cl N_i, so l would be constant on J and
 int J subset G, contradicting J subset K. So l^{-1}(N) subset U_i K_i is meagre. ∎
 Proof of (c): by the Lemma, U_k l_k^{-1}(N_k) is meagre in [s_*,inf), contradicting (a) and Baire. ∎

**Example 4.9 (dense jumps defeat every argument that uses only (a) of Cor 4.8 and the size of N_k). PROVED.**
Take (RM2 §9.1) an enumeration (q_n) of the rationals in (1,inf), kappa(a) := a + sum_{n : q_n < a} 2^{-n} (strictly
increasing, jumps 2^{-n} at q_n), and the arc Gamma_kappa = {(c,a) : kappa(a-) <= c <= kappa(a+)} parametrized by
s = a + c. Along it the a-coordinate is flat exactly at the levels q_n (where c runs over the gap
[kappa(q_n), kappa(q_n) + 2^{-n}]), and at every other point c = kappa(a) with a irrational. Let N_1 := Q (countable)
and N_3 := [kappa(1),inf) minus the union G of the open gaps (kappa(q_n), kappa(q_n) + 2^{-n}). G is dense (between
c_1 < c_2 on the arc with a-coordinates a_1 < a_2 lies the whole gap of any q_n in (a_1,a_2); if a_1 = a_2 then
(c_1,c_2) lies in a gap), so N_3 is nowhere dense; and every point of the arc has a in N_1 or c in N_3. So the
covering U_k l_k^{-1}(N_k) = everything is compatible with meagre N_k when k = h_CA has dense jumps; the
offending part is the open dense set of a-flats, i.e. the countably many heavy levels q_n of world 1 (Prop 4.4),
each of which must then be uncovered from some side (Lemma 3.3). This is the precise sense of RM2 F14: dense jumps
are not harmful as jumps but as heavy levels; removing them requires excluding single heavy levels — (T1).

Answer to (T2). PROVED: with completed graphs the holonomy survives without any continuity (Prop 4.2, Prop 4.3,
Prop 4.5, Theorem 4.7); jumps of the cycle maps, dense or not, become flats of the curve coordinates, i.e. heavy
levels (Prop 4.4); Cor 4.8(c) is the correct Baire statement ("no flat at an uncovered level" replaces
"homeomorphism"), and Example 4.9 shows that no category or measure argument along the curve can dispense with
excluding heavy levels at uncovered levels. So (T2) reduces to (T1).

## 5. (T1): heavy levels — what is forced, what survives

By §§3-4 every defect that obstructs the Baire argument (flats, jumps, dense jumps, the reverse-cycle defects of
Prop 4.2) is a heavy level (Def 3.1(c)) in one of the six frames, at a high level. (T1) is therefore: exclude a
heavy level of world k at a high level z of the frame (k,l'). The flat of RM2 F11 is the special case "heavy
relative to a fat credit band of a cross-world tail family".

**Proposition 5.1 (one-sided reduction). PROVED.** Let z be a heavy level of world k in frame (k,l') with witness
gamma. (a) If z is covered from above, then for every split gamma = gamma_1 u gamma_2 into disjoint non-null parts,
every LEFT band P_k n {z - eps < tau < z} is strictly AC against gamma_1 (all eps > 0). (b) If z is covered from
below, the same for RIGHT bands. (c) z is not covered from both sides (Lemma 3.3).
Proof. (a) (LH) at world k gives an SI pair (A_2, gamma_2') with gamma_2' subset gamma_2; Lemma 4.6 gives eps_0 with
every right band R_eps (eps <= eps_0) making (R_eps, gamma_2) weakly SI. If (L_eps, gamma_1) were weakly SI for some
eps <= eps_0 (L_eps the left band), then (IB-comp) (L_eps, R_eps, gamma_1, gamma_2 pairwise disjoint) makes
(L_eps u R_eps, gamma) weakly SI, i.e. the two-sided band (up to the null set {tau = z}) is not strictly AC against
gamma: contradiction. For eps > eps_0 use (G). (b) Mirror. ∎

**Proposition 5.2 (where heavy levels can sit). PROVED.** A frame whose far end is a local chain (Lemma 3.9) has
no heavy level above some M (Lemma 3.9 + Lemma 3.3). In particular, in a counterexample to P1, high heavy levels
can only sit in frames whose far end is NOT a local chain (every stretch before the vertex block contains two
strictly nested selections).

**Proposition 5.3 (a heavy debt level is a heavy credit level of the edge partner at a rich far end). PROVED.**
Work in frame (1,2) (relabel for the others). Let z be a heavy level of world 1 with witness gamma, and suppose
the D_2-end of [e_1,e_2] is rich: q_m -> q_e (the point of {C = D_2} nearest e_1) with C_m := C_{q_m} having
alpha_m < inf. Then there is m_0 such that for all m >= m_0, all non-null T subset T_0(C_m) = P_2 n {t_12 > alpha_m}
and all eps in (0, beta_m - z):
 (i) acc_2(T, b_eps), where b_eps := P_1 n {|t_12 - z| < eps}  (world 2 accepts T-debt against b_eps-credit);
 (ii) for some non-null S (depending on m): S <=^2_c b_eps for every eps > 0 — world 2's credit order has, at the
      same edge level (1/z in its frame (2,1)), a two-sided germ heavy relative to S.
Proof. (LH) at world 1: SI pair (A*, gamma*) with gamma* subset gamma. (YD): A'' := Z_I(A*) with I a bounded
interval, so A'' subset D_12 n {t_12 < c} for some c, A'' <=_d A*. Lemma SAC of the note ((S_AC^i), P1A Lemma 4.2)
at q_e: for m >= m_0 and every non-null W subset D_12 n {t_12 > alpha_m}, (A'',W) is strictly AC. For non-null
T subset T_0(C_m): V + debt(A'') + cred(gamma*) <=_1 V + debt(A*) + cred(gamma*) <_1 V <_1 V + debt(A'') + cred(T)
(contexts silent: A'' subset P_1 misses gamma and T), so (IB, context debt(A'')) T <^1_c gamma* <=^1_c gamma. Hence
V <_1 V + debt(b_eps) + cred(gamma) <=_1 V + debt(b_eps) + cred(T): world 1 rejects (b_eps, T). For eps < beta_m - z,
b_eps subset B_0(C_m) = P_1 n {t_12 < beta_m}, and the XOR at C_m ("at least one" half; C_m is an open-edge-12
selection) gives (i). (ii): (DH) at world 2 for T_0(C_m) (non-null since alpha_m < inf) gives an AC pair (T',S)
with T' subset T_0(C_m); with (i) for T', V + debt(T') + cred(b_eps) <=_2 V <=_2 V + debt(T') + cred(S), and (IB)
(context debt(T'), silent on b_eps u S) gives S <=^2_c b_eps; larger eps by (G). ∎
Reading. The partner's credit germ in (ii) is killed by exactly the crossings that kill world 1's debt germ (in
world 2's frame, (X3)/(X4) at level 1/z are (X2)/(X1) at level z in world 1's frame), so Prop 5.3 gives no new
kill; it shows that heavy levels come in edge pairs (debt-heavy for one edge world, credit-heavy for the other),
as P1A Cor 6.4 did for heavy ultrafilters at silent selections, now at the rich far end without silence.

**5.4 The surviving configuration (necessary conditions; PROVED as a list).** In a counterexample to P1, by
Cor 3.7 either (A) some frame carries heavy levels at arbitrarily high levels, or (B) the second alternative of
Cor 3.7 holds. In case (A), each such heavy level z of world k in frame (k,l'):
 1. is not covered from both sides; if covered from one side, it is one-sidedly heavy on the other side relative
    to almost all of its witness (Prop 5.1);
 2. sits in a frame whose far end is not a local chain (Prop 5.2);
 3. if that far end is rich, is also a heavy credit level of the edge partner l' (Prop 5.3);
 4. is crossed, from the uncovered side, only by nested moves or nested jumps (Lemma 6.1 below; this is the gap
    (M1)/(M2) of K §4.4);
 5. arises, if it comes from a defect of the six maps, as in Lemma 3.5 / Prop 4.2 / Prop 4.4, with witness a fixed
    fat band of a cross-world tail family (flats) or a fixed deep tail member X* (jumps).
Status of (T1): OPEN. A single heavy level is compatible with completeness, (G), (IB) at a single world (K Example
5.2: an exact finitely additive loss with a germ charge has a heavy level), so (T1) is not an order-theoretic
statement; it needs (S) non-locally — exactly the single-germ problem of P1A §7.2 / K §4.4, now localized to
nested far ends (item 2) and to levels crossed only nestedly (item 4).

## 6. (T3): meagreness of uncovered high levels

**Lemma 6.1 (what "uncovered" means). PROVED.** In frame (k,l'), z in (0,inf) is NOT covered from above iff no
index q* with beta*_{q*} = z is the limit of indices q_m that are pointwise comparable with q* and have beta_m > z;
NOT covered from below iff no such q* is a limit of comparable q_m with beta_m < z. (Levels z not attained as a
debt threshold at all are uncovered from both sides.)
Proof. If C_{q_m} is comparable with C_{q*} and beta_m > z = beta*, then C_{q_m} <=pw C_{q*} is impossible
(it needs beta_m <= beta*), so C_{q_m} >=pw C_{q*}; q* is in the open edge (beta* in (0,inf) excludes the vertex
models), hence so are q_m for large m. Symmetrically from below. ∎
So NK^+ (NK^-) is the set of levels crossed from above (below) only by NESTED approaches (continuous nested moves
or nested jumps, P1A §6, G3 13.3) or never attained.

**Proposition 6.2 (local chains; refines RM2 Lemma R3). PROVED.** = Lemma 3.9: at a far end that is a local chain,
NK^+ and NK^- contain no level above some M. A poor end (RM2) is a local chain; so is, e.g., an end approached by
precise selections (z_q, z_q) with z_q increasing (rich, alpha < inf). So the dichotomy relevant to (T3) is
CHAIN versus NESTED at the far end, not poor versus rich (RM2 Cor R4 used poor).

**Proposition 6.3 (path geometry allows a nested far end with every high level uncovered). PROVED (geometry
only).** There is a continuous path q -> (alpha_q, beta_q), q in [0,1), in {0 <= beta <= alpha <= inf}, from
(0,0) and tending to (inf,inf) as q -> 1, such that for some M every point with beta_q > M has a punctured
neighbourhood consisting of points strictly nested with it. For such a path every level > M is attained and is
uncovered from both sides (Lemma 6.1).
Proof. K Prop 4.8's coordinates: phi := arctan(alpha) + arctan(beta) in [0,pi], psi := arctan(alpha) -
arctan(beta), admissible region 0 <= psi <= min(phi, pi - phi); strictly nested iff |d psi| > |d phi|. Fix
x_1 in (0,pi/2) and x_j increasing to pi; on [x_j, x_{j+1}] let psi be the triangle wave of slope +-2, zeros at the
grid points of mesh h_j, peak height h_j, where h_j <= min(x_1, (pi - x_{j+1})/2) and (x_{j+1} - x_j)/h_j is an
integer; psi := 0 on [0,x_1]. Then psi <= h_j <= pi - phi on [x_j,x_{j+1}] and psi <= phi near x_1 (h_j <= x_1),
so the path is admissible; psi -> 0 and phi -> pi give alpha, beta -> inf. Every point with phi > x_1 lies on one or
two linear pieces of slope +-2 (at grid points and at the x_j the neighbouring pieces also have slope +-2), so all
nearby points are strictly nested with it. Points with phi <= x_1 have beta <= tan(x_1/2) =: M. ∎
Status of (T3): PROVED at local-chain far ends (Prop 6.2). OPEN at nested far ends: no result known to me excludes
an (S)-selection whose edge path near a far vertex is a nested zigzag as in Prop 6.3 (with V undominated). The
cleaner statement that (T3) reduces to: for each of the six frames, the high levels crossed from above (for
Cor 3.7: only from above is needed) only nestedly form a meagre set. By Cor 4.8(b), in the presence of two chain
far ends of a triple (and no high heavy levels on the other triple, e.g. three chain far ends there), every high
level of the third frame is crossed only nestedly from at least one side: so in the most constrained case (T3)
asks to exclude (a one-sided version of) the configuration of Prop 6.3.

## 7. Attempts that failed (with the exact reason)

(TC-F1) Baire in the original parameter with dense jumps (M2 §0 "next step"): false (RM2 F14); in curve form
 Example 4.9 shows why: the jumps of k become flats of the a-coordinate at countably many levels, which cover an
 open dense set of curve parameters. Any replacement of Baire category by Lebesgue measure or by an order-type
 count fails for the same reason (a flat level carries a curve interval of positive length and of second
 category). FAILED; replaced by Cor 4.8(c) (flats at uncovered levels must be excluded separately).
(TC-F2) Killing a heavy level through the second edge shadow of a P_1-germ (K Lemma 4.3: an ultrafilter containing
 P_1 sits at germ points of both edges at world 1, e.g. the A-bands at level a on edge 12 also sit on edge 13 at
 some level in the closure of J). This needs IDEAL heaviness (no band in J_{A*} for some A*), while Cor 5.5 /
 Prop 4.5 / Def 3.1 give single-comparison heaviness relative to a fixed credit set gamma. Turning one into the
 other would need one A* lying <=_d below the debt parts of infinitely many SI pairs with disjoint credit parts
 inside gamma (to absorb finite covers with an unbounded number of pieces); nothing provides it. FAILED.
(TC-F3) K's far-end technique (Thm 3.13) without a fine partner: its two branches are P1A Cor 6.4 (silent
 selections) and Prop 3.12 (precise selections), both of which need world j's extension Lam_j to make the germ
 pieces credit-light for world j. Without Lam_j the same moves give Prop 5.3: the heaviness is transferred to world
 j's credit at the same edge level, where the same crossings would be needed to kill it. FAILED.
(TC-F4) Triangle trade with the heavy band as one side: with (M1) (LH 5.6(b)) world 3 accepts (Y_{c(eps)}, b_eps)
 and by Prop 5.3 world 2 accepts (T, b_eps); (TRI) in orientation (1,3,2) then forces world 1 to reject
 (b_eps, T u Y_{c(eps)}). This is consistent with transversal lightness (M2 Lemma 5.2: world 1's credit on deep
 P_3-tails is light relative to fixed debts), because c(eps) -> inf as eps -> 0. FAILED (a race again).
(TC-F5) Counting heavy levels relative to a fixed credit set: in non-additive (G)+(IB) orders (e.g. lexicographic
 or Hahn-series valued) uncountably many disjoint bands can each be strictly AC against the same fixed gamma; no
 finite-additivity bound is available in a counterexample (no group primary, C5 Thm 4.1). So "heavy levels relative
 to fixed L_k are few" cannot be used to beat the Baire obstruction. FAILED.
(TC-F6) Three ends instead of six. With the three far ends of the first triple local chains, f, g, k are
 homeomorphisms at high levels (no heavy levels in (1,2), (2,3), (3,1)), H^+ = H^- = H >= id, but H <= id needs the
 second-triple conditions of Prop 4.2 (no flat of h_A'D, no jump of h_AC', no flat of h_D'C); these are heavy
 levels in (1,3), (3,2), (2,1) and are not controlled by the first triple. I found no route that uses only the
 first triple (all three Z2-construction routes need members of A', C', D' in prescribed gaps of the scales).
 FAILED; Cor 3.10 needs all six ends.
(TC-F7) (T3) by closedness of sections along the far-end approach (the technique of RM2 Lemma R3): the proof needs
 continuity of beta on a stretch before q_e, which holds exactly for local chains (Lemma 3.9); at a nested far end
 closedness only gives the instances with the WRONG limit model (K Prop 4.1, gap (M2) of K §4.4), and continuous
 nested moves give nothing local (K Prop 4.7). FAILED.
(TC-F8) Linking at nested crossings (P1A Lemma 6.2): a heavy right debt germ at beta* of a continuous SE crossing
 forces a heavy left credit germ at alpha*; in a nested zigzag the alpha-levels are also crossed only nestedly
 (Prop 6.3's path is nested at every point), so the credit germs are not killed either. FAILED.

---
# Part 4. Referee report on TC (RTC)
# RTC referee report on r5/TC_notes.md (§§3-6)

Referee: independent. Written incrementally; §0 (summary) is filled in last.
Verdicts: CORRECT / CORRECT WITH MINOR FIXES / GAP / WRONG.

## 0. Summary

Every numbered result of §§3-6 was re-derived line by line; no GAP, nothing WRONG in a numbered statement.
 - Def 3.1 consistent; Lemma 3.2 CORRECT WITH MINOR FIXES (precise case: the AC pair's credit levels K must be fixed
   above z and away from I, F1); Lemma 3.3 CORRECT.
 - Lemma 3.4 CORRECT (Z1 excludes bounded f, g, k).
 - Lemma 3.5 CORRECT. The jump transfer is right, and the sign pattern was checked row by row (world k accepts
   (X*,delta); the XOR at E/F/E' then makes the owner o strictly reject (delta,X*); witness X* lies outside P_o; the
   level sits in Y's owner frame). In fact the jump gives a genuine SI pair at world k, so RM2 F11's "mixed
   comparison" was too pessimistic (F4). The table covers 4 of the 6 credit families; the two missing rows
   (Y = A', D') are true and were verified (F5).
 - Thm 3.6 CORRECT WITH MINOR FIXES (M >= x_0, F6). Cor 3.7, Cor 3.8 CORRECT.
 - Lemma 3.9 CORRECT (generalizes RM2 Lemma R3, now from both sides).
 - Cor 3.10 CORRECT: it needs only the standing hypotheses plus six local-chain far ends; (TC) is derived before M2
   Thm 5.6 is applied.
 - §4: Lemma 4.1 (label "<=>" should be "=>", F9), Props 4.2-4.5, Lemma 4.6, Thm 4.7 CORRECT. The monotone-map facts
   ((U), closed completed graphs, chain, fibres, s-homeomorphism, flats <-> jumps) are all verified.
 - Cor 4.8 CORRECT WITH MINOR FIXES. By its own (d), the hypothesis of (c) is equivalent to "f, g, k
   homeomorphisms", so the "no flat at an uncovered level replaces homeomorphism" reading is misleading (F13).
 - Example 4.9 is right for category, but its N_3 has infinite Lebesgue measure. So the "measure" claims (S7,
   TC-F1) are not shown; a pure-jump kappa repairs this (F14).
 - §§5-6 CORRECT (F15, F16 cosmetic).
 - Nearby sharper result, PROVED here from the note's results (§4.8, Cor R): if the three far ends of ONE triple are
   local chains, V undominated forces flats of h_A'D, jumps of h_AC' or flats of h_D'C at arbitrarily high levels.
   So "six ends -> three ends" is exactly the exclusion of these three defect types.
Fixes F1-F16 in §7, verdicts in §8. Scripts: r5/rtcchk/ (all ALL PASS).

Sources read: r5/SETTING5.md; r5/TC_notes.md (full, under review); r5/M2_notes.md (full) + r5/RM2_referee.md (full:
Lemma R1, F9, F11, F14, Lemma R3, Cor R4, §9.1 dense-jump example); "Fineness Spreads Along Edges" (tex: §§1-2 in
full - (T1), (T2), lem:ends, lem:E12, lem:yard, lem:SAC, thm:SIAC; lem:XOR; thm:LH, cor:relLH, cor:LHcons);
r4/P1A_notes.md §§1-5 (Lemma 3.0, Thm 3.1 (X1)-(X5), Lemmas 4.1-4.2); r5/K_notes.md Prop 4.8, Example 5.2;
r5/RLH_referee.md §6.1 (LH 5.1, M5).
Mechanical checks written for this report: r5/rtcchk/ (outputs *_out.txt; all ALL PASS):
 - tc_regions.py (Monte Carlo, 3e6 points): option table; advice of E, E', F, C_m on the XOR regions; the three
   XOR structures (debt regions, strictness witness); the six families: non-null, owner frames
   X(x) = P_k n {tau > x} n slab, bands X(x_1)\X(x_2) subset P_k n {x_1 < tau <= x_2}, inside their XOR regions,
   disjoint at x_0; Lemma 3.5(b) table row by row (X* subset P_k in a high tail of world k, X* and delta in the
   two regions of the named XOR, debt/credit roles at k and at the owner o, third world credit on both, owner
   frame), INCLUDING the two rows the note omits (Y = A', Y = D'); X* disjoint from every alpha-band; Theorem 3.6
   frame list; Prop 4.2 XOR uses and the (Z2) orientation; Prop 4.5 transfers; Prop 5.3 regions.
 - tc_ib.py (symbolic): every (IB)/(G) step of Lemmas 3.3, 3.5(a),(b), Prop 4.2, Prop 4.5 (Fix_k decompositions
   M_1 = N + debt(alpha) + cred(L), M_2 = N + cred(delta), V + d = M_1 + extra, at all three worlds, and the
   transfer chain), Prop 5.1 (IB-comp), Prop 5.3: same difference set and same advice, or (G) pointwise.
 - tc_monotone.py: (U); the limit identity of Lemma 4.1(b) and the end inequalities of Prop 4.3(b) on random
   monotone functions with jumps and flats (exact rationals); Example 4.9 (truncated) incl. a pure-jump variant;
   Prop 6.3's zigzag path (admissibility, strict nestedness of nearby points).

## 1. Conventions

X <=_k Y: X at least as good as Y at world k; acc_k(X,Y) :<=> V + debt_k(X) + cred_k(Y) <=_k V (weakly SI);
strictly AC := V <_k V + debt_k(X) + cred_k(Y). Completeness is what turns "not acc" into "strictly AC", and makes
two debt (credit) sets comparable. Regions P_1 = (+,-,-), P_2 = (+,-,+), P_3 = (+,+,-) in H; the triangle option
of P_x is debt at x and credit at the two other worlds (re-checked, tc_regions.py). Frame (k,l') = world k on
[e_k,e_l'], tau = tau^k_{l'} = |g_k|/|g_l'| on D_kl'; an edge model (alpha,beta) in frame (k,l') is
(1/beta,1/alpha) in frame (l',k) (checked numerically).
XOR (lem:XOR of the note, relabelled): at an open-edge selection S on [e_v,e_w], for ARBITRARY B in S's debt_v
region and T in its debt_w region: acc_v(B,T) or acc_w(T,B) (competitiveness of S on {v,w} + (IB); no V); not both
if V is undominated and B u T non-null (third world gains strictly). The TC_notes §2 form "for arbitrary sets in
the regions" is exactly the lemma. Regions: E: B_0(E) (1) / T_0(E) (2); E': P_1 n {t_13 < beta'} (1) /
P_3 n {t_13 > alpha'} (3); F: P_2 n {s < beta^2} (2) / P_3 n {s > alpha^2} (3). Families: A', D at E; A, C' at E';
D', C at F (all checked).

## 2. Item (1)+(2): Definition 3.1 and Lemmas 3.2-3.3

### 2.1 Definition 3.1 — CORRECT (consistent with its uses)
(a) "covered from above" is verbatim M2 Thm 5.6's "covered" in frame (k,l') (q* automatically in the open edge
since beta* = z in (0,inf)). (b) "covered from below" is the hypothesis of P1A (X1); (b) does not require the q_m
in the open edge, correctly ((X1) uses (T1), not (T2)); they are in the open edge anyway for large m. (c) heavy
level: one FIXED credit set gamma subset H' \ P_k, every two-sided P_k-band strictly AC against it; the sub-band
remark is (G) (more debt is worse). Used consistently: Lemma 3.5 produces P_k-slab sub-bands (owner frames checked,
tc_regions.py), Lemma 3.3 kills P_k-bands, Prop 4.5/Lemma 4.6/Prop 5.1 speak of ONE-sided germs and never call
them heavy levels. NK^+, NK^- are per frame (Cor 3.7 writes NK^+_k for the frame (k,k+1) resp. (k,k-1); fine).

### 2.2 Lemma 3.2 (two-sided kill) — CORRECT WITH MINOR FIXES
Re-derived. (YD) = lem:yard(a) in world k's frame: for n = 3, D_1j n D_1k = P_1, so Z_I(A) = P_k n {tau^k_m > b'}
n {tau^k_{l'} in I}, every subset of Tl := D_km n {tau^k_m > b} is <=^k_d A (tail <_d A_0 <=_d A, then (G)).
 - Below: P1A (X1) with Z := Z_{(0,z/2)}. Its proof needs Z in debt(C_{q*}) (levels < z = beta*) and in debt(C_m)
   (beta_m -> z by (L30), so beta_m > z/2 eventually), Z disjoint from b_m = b[beta_m,z), Y := C_{q*} with Z
   silenced, (T1) (completeness at k), C_m <=_k N + debt(Z) ((G): C_m silent or credit on b_m), N + debt(b_m)
   <=pw Y (they differ only on (max(alpha_m,z), alpha*], N credit, Y silent). All hold. L <^k_d R_2. CHECKED.
 - Above, silent q*: (X2) with Z' := Z_{(z+delta,z+2delta)}, delta = min(1,(alpha*-z)/3) (also covers alpha* = inf):
   Z' lies in (z, alpha*) and, since alpha_m >= alpha*, beta_m -> z, in the silence of C_m eventually; F := C_{q*} +
   debt(Z') is l'-better (swap: debt_k = cred_l' on D_kl'; strict (G) at l'); (T2) at the open-edge q_m; C_{q*} +
   debt(b(z,beta_m)) <=pw C_m. R <=^k_d R_1. CHECKED.
 - Above, precise q*: (X2') with cor:LHcons(a) (= LH 5.1, RLH §6.1). The proof of cor:LHcons(a) gives A'' subset
   Z_I(A) subset Tl, I = (z+1,z+2), and W subset P_k n {tau in K}. FIX F1: the note does not fix K; (X2') needs
   W subset D_kl' n {tau > z + eta} and W disjoint from A'': say "K := (z+3,z+4), eta := 3" (any K above z+eta,
   disjoint from I). Also say that the tail parameter b' of Z_I(A) is the b of (YD) for the same A (so A'' subset Tl).
 - Assembly: eps < min(z - beta_m, beta'_m - z, delta, z/2): the one-sided D_kl'-bands lie in L, R; R_1 (levels in
   (z+delta, z+2delta) or (z+1,z+2)), R_2 (levels < z/2) and the two bands are pairwise disjoint; {tau = z} null.
   (IB-comp) for debt comparisons (checked: two (IB) steps with contexts V + debt(B_2), V + debt(R_1)), then
   R_1 u R_2 subset Tl. CHECKED.
 "Uses" line: add (G) at l' ((X2), (X2'), (T2)) and (G) at all worlds (lem:yard); otherwise accurate. [F2,
 cosmetic]

### 2.3 Lemma 3.3 — CORRECT
(LH) (thm:LH(i), all worlds complete, no V) gives (A_k, gamma') SI with gamma' subset gamma. b := P_k-band <=_d
D_kl'-band <=^k_d A_k ((G) + Lemma 3.2). Chain: (G) (credit on gamma \ gamma'), (IB) with context cred(gamma'),
silent on b u A_k (b subset P_k, gamma' subset H' \ P_k, A_k n gamma' empty; b and A_k may overlap - allowed),
then SI. Pattern checked (tc_ib.py). So (b, gamma) is SI, not strictly AC. No completeness needed beyond Lemma 3.2.

## 3. Lemmas 3.4, 3.5; Theorem 3.6; Corollaries 3.7, 3.8; Lemma 3.9; Corollary 3.10

### 3.1 Lemma 3.4 — CORRECT
x > h_XY(y) => acc (up-ray, (G)). The three cases produce (Z1) = acc_1(A(a),D(b)), acc_2(D(b),C(c)),
acc_3(C(c),A(a)) exactly as written (checked each inequality: a > M >= f(b); b > M >= g(c); c = M+1 > M >= k(a)).
(TRI) (B Lemma 3.1, RB5 CORRECT; V undominated) excludes it. Trivial fix: take all parameters >= x_0 (e.g.
a > max(M, x_0), b := max(M+1, x_0)). Uses V (TRI) and finiteness (L52) (completeness, (LH)).

### 3.2 Lemma 3.5(a) (flat) — CORRECT (one-line fix)
acc_k(X(l+eps),Y(y')) and not acc_k(X(l-eps),Y(y)); completeness gives M <=_k V <_k M + debt(b_eps) + cred(gamma);
M is silent on b_eps u gamma; (IB) (pattern checked at all three worlds). b_eps subset P_k n {l-eps < tau <= l+eps}
(owner-frame band, checked), gamma = Y(y)\Y(y') non-null and outside P_k; gamma does not depend on eps. Uses
completeness and (IB) at k only; no V (correct). FIX F3: require l > x_0 (X(l - eps) must be a member of the
family, i.e. l - eps >= x_0 for some eps); at the uses (Thm 3.6, Prop 4.2, Prop 4.4) the values are > M >= x_0
once M >= x_0 is imposed.

### 3.3 Lemma 3.5(b) (jump) — CORRECT; item (5): sign pattern verified explicitly
Step at world k. x_1 < x_2 in (h(y*-), h(y*+)), y' < y* < y'': x_1 > h(y') gives acc_k(X(x_1),Y(y')); x_2 < h(y'')
gives not acc_k(X(x_2),Y(y'')), strict by completeness: V <_k N := V + debt(X(x_2)) + cred(Y(y'')). With
alpha := X(x_1)\X(x_2), delta := Y(y')\Y(y''): V + debt(X(x_1)) + cred(Y(y')) = N + debt(alpha) + cred(delta)
<=_k V <_k N; N silent on alpha u delta; (IB): (alpha, delta) strictly SI at world k. (Checked symbolically.)
Remark on the note's Remark (i): what world k gives at a jump is NOT a mere "mixed comparison" (RM2 F11's
description): it is a genuine strictly SI pair (fixed debt band alpha, thin credit band delta at y*), i.e. a
transversal heavy CREDIT germ of world k at y*; the derivation is the exact mirror of (a) (acc at (more debt, more
credit), rejection at (less, less)). RM2 F11 was too pessimistic; the note's own proof shows this. Reword Remark (i)
accordingly [F4, cosmetic].
Transfer. (YD) at world k for the non-null alpha: the listed X* = X'(x**) lies in a high tail of world k
(A' on edge 13, D' on edge 21, C' on edge 32, A on edge 12; checked), so X* <=^k_d alpha for x** large; X* subset
P_k is disjoint from delta subset P_o and from alpha (other family: x_0-disjointness; same family: x** > x_2;
checked for all alpha-bands). (IB) with context cred(delta): acc_k(X*, delta) (strict).
XOR, row by row (tc_regions.py, tc_ib.py: one change o(X*) + o(delta), read at k as (X*,delta), at o as (delta,X*),
credit at the third world on both):
  Y = D  (k=1): X* = A'(x**) in B_0(E) (debt_1 region), delta in T_0(E) (debt_2 region); XOR at E: acc_1(X*,delta)
                => not acc_2(delta,X*) => (delta,X*) strictly AC at o = 2; delta subset P_2 n {y' < s <= y''}:
                frame (2,3). Witness X* subset P_1. CORRECT.
  Y = C  (k=2): X* = D'(x**) in P_2 n {s < beta^2}, delta in P_3 n {s > alpha^2}; XOR at F: acc_2(X*,delta) =>
                not acc_3(delta,X*); o = 3, delta subset P_3 n {y' < t^3_1 <= y''}: frame (3,1). CORRECT.
  Y = A  (k=3): X* = C'(x**) in P_3 n {t_13 > alpha'}, delta in P_1 n {t_13 < beta'}; XOR at E': acc_3(X*,delta)
                => not acc_1(delta,X*); o = 1, frame (1,2). CORRECT.
  Y = C' (k=1): X* = A(x**) in P_1 n {t_13 < beta'}, delta in P_3 n {t_13 > alpha'}; XOR at E': acc_1(X*,delta)
                => not acc_3(delta,X*); o = 3, delta subset P_3 n {y' < t^3_2 <= y''}: frame (3,2). CORRECT.
The "at most one" half is used each time (V undominated, X* non-null); completeness at o turns "not acc_o" into
strict AC. Taking y', y'' within eps of y* gives every two-sided P_o-band at y* strictly AC against the fixed
gamma := X* (X* depends only on alpha, i.e. on x_1, x_2). CORRECT.
Scope [F5]: the statement is for an arbitrary credit family Y, and §0 S3 says "every JUMP of h_XY", but the table
lists only Y in {D, C, A, C'}. The two missing rows are true and were checked (tc_regions.py):
  Y = A' (k=2; maps h_DA', h_D'A'): X* := D(x**) subset T_0(E), XOR at E (acc_2(X*,delta) => not acc_1(delta,X*)),
         o = 1, frame (1,3);
  Y = D' (k=3; maps h_CD', h_C'D'): X* := C(x**) subset P_3 n {s > alpha^2}, XOR at F, o = 2, frame (2,1).
Add them (or restrict the statement and S3 to the four listed Y; only those are used).

### 3.4 Theorem 3.6 — CORRECT WITH MINOR FIXES
Each map nondecreasing, finite (L52), unbounded (Lemma 3.4 for f, g, k; RM2 §7.2 / M2 Lemma 5.2 for h_A'D, h_AC',
h_D'C - these use the "at most one" XOR halves, V undominated). Frames (checked, tc_regions.py): flats of h_AD, h_DC,
h_CA, h_A'D, h_AC', h_D'C in (1,2), (2,3), (3,1), (1,3), (1,2), (2,1); jumps (owners of D, C, A, D, C', C) in (2,3),
(3,1), (1,2), (2,3), (3,2), (3,1) - exactly as stated; all six frames occur. For nondecreasing h, h(y*-) = h(y*+)
forces continuity at y*; no flat on [y_0,inf) forces strict increase; with unboundedness, h is an increasing
homeomorphism of [y_0+1,inf) onto [h(y_0+1),inf). (TC6) => (TC) is RM2 Lemma R1 + M2 Prop 5.4(a) first sentence
(RM2 §2.2, re-read: needs completeness, (IB), XOR both halves). FIX F6: impose M >= x_0 (needed by Lemma 3.5(a),
F3, and Lemma 3.5(b)'s y* > x_0); say "ray [y_0+1,inf)" in the statement.

### 3.5 Corollaries 3.7, 3.8 — CORRECT
3.7: negation of (i) is the hypothesis of Thm 3.6; then (TC6) for the given E, E', F, intervals, hence (TC); M2 Thm
5.6 with F9 (hypothesis "NK_k n (M_k,inf) meagre for each k", NK_k = TC's NK^+ in frames (1,2),(2,3),(3,1)) and its
symmetric form (RM2 §6.6 item 5; frames (1,3),(2,1),(3,2)) give (ii) as the conjunction of two contrapositives. The
parenthesis in (i) is Lemma 3.3. 3.8: immediate. Both CORRECT.

### 3.6 Lemma 3.9 — CORRECT
On S, C_q != D_l' and beta = inf forces alpha = inf, i.e. D_l': so beta < inf on S. For q_m -> q* in S, each C_m
is comparable with C_{q*}; (L30) (P1A Lemma 3.0, re-read: only (G) and closed A_k, A_l') applies to the <=pw and the
>=pw subsequences, so beta (and alpha) is continuous on S into [0,inf]. (ENDS) = lem:ends(a) gives beta -> inf at
q_e along any sequence. Z is non-empty (IVT), closed in [q_1,q_e), bounded away from q_e: compact. Above: q* = max Z,
beta > z on (q*,q_e) (else IVT gives a zero beyond q*); comparable q_m with beta_m > z are >=pw (<=pw would force
beta_m <= beta*). Below: q** = min Z > q_1 (beta(q_1) = M < z), beta < z on [q_1,q**), comparable q_m are <=pw. All
in the open edge. Only (G) at k, l' and (S) are used: correct.

### 3.7 Corollary 3.10 — CORRECT; item (6)
Chain of inferences, each re-checked: six local-chain far ends => (Lemma 3.9, take M := max of six) every level > M
covered from both sides in all six frames => (Lemma 3.3) no heavy level > M in any frame => (Thm 3.6, V undominated)
(TC6) => (RM2 Lemma R1) (TC) => (M2 Thm 5.6 with F9; NK^+ n (M,inf) empty) V dominated, contradicting the
reductio hypothesis. Hypotheses actually used: n = 3; all three rankings complete with (G) and (IB) (completeness at
every world through (LH), (YD), LH 5.1, Lemma R1, M2 Cor 5.5); (S); V undominated only as the reductio hypothesis
(interior E, E', F exist by B Cor B.6; XOR; TRI). No (TC6), no meagreness hypothesis. Nothing else is hidden; the
statement should repeat the standing hypotheses [F7, cosmetic]. Relation to RM2: Lemma 3.9 strictly generalizes
RM2 Lemma R3 (poor => local chain; R3 gave only "covered from above"); Cor 3.10 trades (TC6) for three more far
ends. The combination with M2 Thm 5.6 is correct: Thm 5.6 is applied only after (TC) has been DERIVED (Thm 3.6),
for the same interior selections and intervals.
A nearby sharper statement is available from the note's own §4 (not stated there; see §4.8 below): local chains at
the three far ends of ONE triple already force the second triple to carry, at arbitrarily high levels, one of the
three specific defects of Prop 4.2.

## 4. §4: completed holonomy (items (3), (7))

### 4.1 Preliminaries — CORRECT
Completed graphs: Gamma_f is closed because b -> f(b+) is upper and b -> f(b-) lower semicontinuous (if b_n -> b,
limsup f(b_n+) <= f(b+) and liminf f(b_n-) >= f(b-), checking b_n > b, b_n < b separately); each is a closed
connected chain in the product order (a monotone arc, with horizontal pieces at flats and vertical pieces at
jumps). (U): for v in [phi(p-), phi(q+)], t_0 := inf{t : phi(t+) >= v} satisfies phi(t_0+) >= v (right continuity
of phi^+) and phi(t_0-) <= v (phi(t+) < v for t < t_0); the reverse inclusion is monotonicity. CORRECT (also
tested, tc_monotone.py). (F-c)/(F-d): if Y_1 <=_c Y_2 then (IB, context debt(X), X disjoint from Y_1 u Y_2)
acc_k(X,Y_1) => acc_k(X,Y_2); contrapositive + completeness gives Y_2 <_c Y_1; the "hence" is (IB) with context
debt(X'). Needs X, X' disjoint from Y_1 u Y_2 (true for all uses: different regions). CORRECT.
Notation clash [F8, cosmetic]: k denotes both h_CA and a world index (Lemma 4.6, Thm 4.7); rename the map.

### 4.2 Lemma 4.1 — CORRECT (label overclaims)
(a) CHECKED. (b) a <= inf_{c > k(a)} inf_{b > g(c)} f(b) = inf_{c > k(a)} f^+(g(c)) = f^+(g^+(k(a))) by
monotonicity and right continuity of f^+ (tested numerically). The bracket "[(Z1) <=> H^+ >= id]" claims an
equivalence; only "(Z1)-freeness => H^+ >= id" is proved (and the converse is false at attained thresholds: a
(Z1) cycle at (a,b,c) only gives a >= f(b), b >= g(c), c >= k(a)). FIX F9: replace "<=>" by "=>".
(c) From a_1 < H^-(a) = sup_{b < g^-(k(a))} f(b): b_- < g^-(k(a)) with f(b_-) > a_1, then c < k(a) with g(c) > b_-;
b in (b_-, g(c)), c_+ in (c, k(a)); the three strict inequalities a' <= a_1 < f(b_-) <= f(b'), b' <= b < g(c) <=
g(c'), c' <= c_+ < k(a) <= k(a') give the three rejections (x < h(y) => not acc). b_- >= inf{b : f(b) > a} -> inf
uniformly in the choice, then c -> inf. CORRECT.

### 4.3 Proposition 4.2 — CORRECT
Re-derived step by step; every (IB) step checked symbolically and every XOR region mechanically (tc_ib.py,
tc_regions.py).
 Step 1: negation of (G1) + completeness: A'(x') >_d A(a_1) for all x' in [x_0, theta); (IB, context
  cred(D(b''))) turns acc_1(A'(x'),D(b'')) into acc_1(A(a_1),D(b'')), excluded on [b_-,b] by Q; hence
  h_A'D >= theta on [b_-,b] and <= theta by monotonicity: (i). (If theta = x_0 the same conclusion holds
  vacuously; theta -> inf removes this case.)
 Step 2(alpha): C'(u) <_d C(c_+) <=_d C(c') ((G)); not acc_3(C(c'),D'(w)) for w > chi; XOR at F, at least one
  (D'(w) in the debt_2 region, C(c') in the debt_3 region): acc_2(D'(w),C(c')); so h_D'C = chi on [c,c_+]: (iii).
 Step 2(beta): U is a down-set; non-empty for a_1 > h_AC'(x_0); bounded because acc_3(C'(u),A(a_1)) for large u
  (L52 at world 3) and the "at most one" half of the XOR at E'. For u < psi_1: (IB) + Q + XOR at E', at least one:
  h_AC'(u) <= a; for u > psi_1: h_AC'(u) >= a_1. So h_AC'(psi_1-) <= a < a_1 <= h_AC'(psi_1+): (ii).
 Step 3: (P1) (IB, context cred(C'(u))); (P2) XOR at E, at least one, then (F-c) with X = D(b), Y_1 = A'(x'),
  Y_2 = C(c), X' = D'(w); (P3) from (G3). Orientation (1,3,2) of (TRI): acc_1(A',C'), acc_3(C',D'), acc_2(D',A')
  = (Z2). CHECKED.
 Levels: theta >= h_A'D(b_-), b_- -> inf; chi = h_D'C(c), c -> inf; psi_1 >= sup{u : h_AC'(u) < a} -> inf; all
 uniform in the choices, so "no heavy level > M in (1,3),(2,1),(3,2) => H^- <= id on a ray" follows (Lemma 3.5(a)
 for (i), (iii); 3.5(b), row Y = C', for (ii); frames (1,3), (2,1), (3,2) CHECKED).
 Remark after the proof [F10, cosmetic]: besides the boundedness of U, the "at most one" halves also enter through
 the unboundedness of h_A'D, h_D'C (theta, chi -> inf; M2 Lemma 5.2) and through Lemma 3.5(b) for (ii).

### 4.4 Proposition 4.3 — CORRECT
(a) closedness: §4.1. Chain: a < a' gives c <= k(a+) <= k(a'-) <= c' and b <= b' (else a >= f(b-) >= f(b'+) >= a');
a = a', b < b' gives c <= c' (else g(c'+) <= g(c-) <= b < b' <= g(c'+)); so B is totally ordered, and P <= P'
componentwise whenever comparable. (b) by (U) twice: the a'-set is [f(p-), f(q+)], p = g(k(a-)-), q = g(k(a+)+);
f(p-) <= f(g(k(a)-)-) = H^-(a) <= a and f(q+) >= f(g(k(a)+)+) = H^+(a) >= a (inequalities tested numerically).
(c) F_a = Gamma_g n (Phi_f(a) x [k(a-),k(a+)]); Phi_f(a) is a closed interval (down-set n up-set), bounded since f
is unbounded; a monotone arc meets a box in a connected piece. (d) sup/inf of the down-/up-set of a chain are limits
of monotone sequences, hence in B; the argument that a(P_-) = a(P_+) is right (a point over an intermediate a would
have to be both > P_- and < P_+ in s), and the fibre's connectedness gives s = t: contradiction. Compactness of
{s <= S} gives continuity of s^{-1}. CORRECT. Wording [F11, cosmetic]: "a point or a segment" -> "a point or a
sub-arc" (the fibre can contain a corner of Gamma_g); take a_* so large that all fibres stay away from x_0 (f(x_0-),
k(x_0-) are undefined).

### 4.5 Proposition 4.4 — CORRECT (item (7): flats vs jumps)
Two distinct fibre points: different b => f = a* on the open b-interval; same b, different c => k(a*-) < k(a*+).
Converse: points with a < a* have b <= b_1 (else f(b-) >= a*), points with a > a* have b >= b_2; continuity of the
coordinates along s and Phi_f(a*) subset [b_1,b_2] put points with b = b_1 and b = b_2 in F_{a*}. Jump of k at a*:
points with a < a* have c <= k(a*-), with a > a* have c >= k(a*+). l_2, l_3 likewise (checked: two points of the
b*-fibre with c_1 < c_2 give g = b* on (c_1,c_2), with equal c and a_1 < a_2 give f(b*-) < f(b*+); l_3 analogous).
The attributions are right (flat of h_AD at a*: Lemma 3.5(a), X = A, frame (1,2); jump of h_CA at a*: 3.5(b), Y = A,
owner 1, frame (1,2); flat of h_DC / jump of h_AD: frame (2,3); flat of h_CA / jump of h_DC: frame (3,1)).
Minor: the converse needs a* > a_* (points on both sides) [part of F11].

### 4.6 Proposition 4.5 — CORRECT (the key holonomy step; item (3))
 - Extras: strict acceptances from (L52) (any non-null credit set in another region), sets pairwise disjoint
   (x_0, regions).
 - Fix_k => domination: at each world, M_1 = N + debt(alpha) + cred(L_k), M_2 = N + cred(delta), N silent on
   alpha u delta u L_k, so Fix_k is exactly (IB) applied to M_1 <=_k M_2; then M_2 <=_k V by the acceptance, and
   V + d = M_1 + (strict extra) with M_1 silent on the extra's support. Checked symbolically at all three worlds,
   including that the three worlds evaluate the same d (tc_ib.py). Hence not all Fix_k (V undominated).
 - World 1 fails: (a,b) in Gamma_f gives f(b_1) <= f(b-) <= a < a_1 for b_1 < b, so (a_1,b_1) is admissible; not
   Fix_1 (completeness) + weak SI of (alpha, L_1^1) + (IB, context cred(L_1^2)) give L_1^2 <^1_c delta. Transfer:
   (LH) at world 1 for L_1^2 -> (A*, L*); (YD) -> X_1 = A'(x_1) <=_d A*; chain (IB)-(G)-(IB)-SI checked; so
   acc_1(X_1, delta) strictly; X_1 in B_0(E), delta in T_0(E); XOR at E, AT MOST ONE (V undominated): not
   acc_2(delta, X_1); completeness at 2: (2-). X_1 depends only on L_1^2 (through A*), not on b_1. The case
   a >= f(b) (b_1 := b admissible) gives (1+) with the full L_1. CORRECT.
 - World 2 (X_2 = D'(x_2), XOR at F, at most one: acc_2(X_2,delta) => not acc_3(delta,X_2): (3-)); world 3
   (X_3 = C'(x_3), XOR at E': acc_3(X_3,delta) => not acc_1(delta,X_3): (1-)). Regions and roles checked
   (tc_regions.py "Prop 4.5 transfers"). CORRECT.
 Observations (no fix needed): only the LEFT inequalities f(b-) <= a, g(c-) <= b, k(a-) <= c of the balanced triple
 are used; the left germs (2-), (3-), (1-) can arise only when a < f(b) (resp. b < g(c), c < k(a)), i.e. at a jump
 of f at b (f(b-) <= a < f(b)) etc. — so §0 S6's "left germs appear exactly at jumps" should read "only at jumps"
 [F12, cosmetic]. "Under (TC) this is exactly M2 Cor 5.5": accurate up to the attained/unattained bookkeeping.

### 4.7 Lemma 4.6, Theorem 4.7 — CORRECT
Lemma 4.6: the one-sided halves of Lemma 3.2 give a right (left) D_kl'-band <=^k_d R_1 (R_2) <=^k_d A_k, with A_k from
(LH) for gamma; the chain of Lemma 3.3 makes the band SI with gamma; (1+) uses gamma = L_1^1, (1-) gamma = X_3, etc.
(all outside the band's region, checked). Thm 4.7: Prop 4.2 -> H^- <= id on a ray -> Prop 4.3 -> Prop 4.5 at B(s)
-> Lemma 4.6. CORRECT.

### 4.8 Corollary 4.8 — CORRECT WITH MINOR FIXES; interpretation of (c) misleading
(a) correct at high s ([s_1,inf) with all l_k(s) > M; not [s_*,inf)). (b) correct; s_M must also exceed the
threshold of "large s" in Thm 4.7. (c) Lemma (preimages): correct (l^{-1}(N) misses the open set G of flat
interiors; each K_i = l^{-1}(cl N_i) n K is closed and contains no interval, else l would be constant on it and
int J subset G). Baire on a closed ray: correct. (d) correct: flat values > M of l_k are heavy levels (Prop 4.4 +
Lemma 3.5), heavy levels are in N_k (Lemma 3.3); with f, g, k homeomorphisms every balanced triple has a = f(b),
b = g(c), c = k(a), Prop 4.5 then gives (1+), (2+) or (3+) with the full L_k, Lemma 4.6 kills them at levels
covered from above, and l_k are homeomorphisms, so NK^+_k meagre suffices.
Interpretation [F13]: by (d) itself, the hypothesis of (c) ("N_k meagre and free of flat values of l_k") is
EQUIVALENT to "N_k meagre and f, g, k increasing homeomorphisms at high levels". So (c) does not weaken
"homeomorphism", and the sentence of "Answer to (T2)" ("no flat at an uncovered level" replaces "homeomorphism")
is misleading. The genuine gain of §4 over Thm 3.6 is (d): only f, g, k (first triple) plus the THREE specific
defects (i)-(iii) of Prop 4.2 on the second triple, and only NK^+.
Nearby sharper statement (PROVED here from the note's results; suggested addition as Cor 4.8(e)):
 **Cor R (one triple of local-chain ends).** Standing hypotheses. If the far ends of the frames (1,2), (2,3), (3,1)
 are local chains and V is undominated, then H^-(a) > a for arbitrarily large a; hence (Prop 4.2) at arbitrarily
 high levels one of: a flat of h_A'D (heavy level in (1,3)), a jump of h_AC' (heavy level in (3,2)), a flat of
 h_D'C (heavy level in (2,1)). In particular V is dominated as soon as, in addition, h_A'D and h_D'C have no flats and
 h_AC' has no jumps at high levels (e.g. if the far ends of (1,3), (3,2), (2,1) are local chains: Cor 3.10).
 Proof. Lemma 3.9 at the three ends: every level > M_0 of (1,2), (2,3), (3,1) is covered from both sides; Lemma 3.3:
 no heavy level > M_0 there; Lemma 3.5 (frames listed in Thm 3.6): f, g, k have no flats with value > M_0 and no
 jumps at arguments > M_0, so they are increasing homeomorphisms on a ray. If H^-(a) <= a for all large a, Prop 4.3
 makes B the set of exact threshold triples, and Prop 4.5 + Lemma 4.6 give a level of B(s) not covered from above,
 contradicting Lemma 3.9. So H^- > id at arbitrarily large a, and Prop 4.2 applies with theta, psi_1, chi -> inf. ∎
 This makes (TC-F6) precise: going from six ends to three is EXACTLY the exclusion of the three defect types
 (i)-(iii) at high levels — nothing else about the second triple is needed.

### 4.9 Example 4.9 — CORRECT for category; the "measure" claim is not supported as written
Checked: kappa is strictly increasing, left continuous, jumps 2^{-n} at q_n; the arc's a-coordinate is flat exactly
over the closed gaps; G (open gaps) is dense (between two arc points with a_1 < a_2 lies the gap of any q_n in
(a_1,a_2)); every arc point has a in Q or c = kappa(a), a irrational, which lies in no open gap (tc_monotone.py).
To be a balanced curve of the §4 type one may take f = id, g := the (continuous) generalized inverse of kappa,
k := kappa: then Gamma_g is the transpose of Gamma_kappa, H^- = H^+ = id, and B = {(a,a,c) : (c,a) in Gamma_kappa}
(state this; otherwise the example is an arc, not a B) [F14a].
But N_3 = [kappa(1),inf) \ G has INFINITE Lebesgue measure (on a in [1,3] it has measure 2: kappa adds the
identity; tc_monotone.py). So the example does not show that a Lebesgue-measure argument fails, contrary to §0 S7
("no category/measure/order-type argument") and (TC-F1) ("Any replacement of Baire category by Lebesgue measure ...
fails for the same reason"). Repair (checked numerically): use a PURE-JUMP kappa, kappa(a) := sum_{q_n < a} w_n
with w_n > 0 and sum_{q_n in (j,j+1]} w_n = 1 for every j (finite, strictly increasing, unbounded); then the open
gaps have full measure, so N_3 = kappa(irrationals) is nowhere dense AND Lebesgue-null, and N_1 = Q is null. With
this kappa every statement of the example holds and also defeats measure arguments. [F14b]

### 4.10 "Answer to (T2)" — interpretive; correct after F13, F14b
The mathematical content (Props 4.2-4.5, Thm 4.7, Cor 4.8) is correct. "(T2) reduces to (T1)" is accurate in the
sense that every defect is a heavy level (Lemma 3.5, Prop 4.4) and that, with (T1) settled, Thm 3.6 already gives
(TC6) — §4 is then not needed; §4's independent value is Cor 4.8(d) and Cor R above.

## 5. §§5-6 (briefly)

Prop 5.1 — CORRECT. Lemma 4.6 for gamma_2 gives eps_0 with every right band (eps <= eps_0) weakly SI with gamma_2
((G) for smaller bands); a weakly SI left band with gamma_1 would compose ((IB-comp), pattern checked) to a weakly SI
two-sided band (up to {tau = z}) against gamma, contradicting heaviness; eps > eps_0 by (G). (b) mirror; (c) Lemma 3.3.
(The extra (LH) sentence at the start of the proof is redundant: Lemma 4.6 contains it.)
Prop 5.2 — CORRECT (Lemma 3.9 + Lemma 3.3; two edge selections are pointwise incomparable iff strictly nested).
Prop 5.3 — CORRECT (one wording fix). (LH) at 1 -> (A*, gamma*); A'' := Z_I(A*) bounded in t_12; lem:SAC (re-read:
needs alpha_m < inf, gives (A'',W) strictly AC for all non-null W in the far tail, m >= m_0) — uniform in T; the
(IB) steps (contexts cred(gamma*), debt(A''), debt(b_eps)) checked; b_eps subset B_0(C_m) for eps < beta_m - z
(beta_m -> inf by lem:ends); XOR at the open-edge C_m, "at least one" (no V): (i). (ii): (DH) at world 2 for T_0(C_m),
(i) for T', (IB) with context debt(T'): S <=^2_c b_eps. Wording [F15]: "S <=_c b_eps" is a weak inequality; to state
credit-heaviness of the germ (no band <=_c a fixed set) take a non-null proper S' subset S (strict (G): S' <_c S <=_c
b_eps). The "Reading" is right: under (alpha,beta) -> (1/beta,1/alpha) and the reversal of <=pw between the two
edge worlds, (X3)/(X4) of world 2 at 1/z are the (X2)/(X1) configurations of world 1 at z.
5.4 — CORRECT as a list of necessary conditions; item 4 should add "or not attained/jumped over" (Lemma 6.1's own
parenthesis) [F16, cosmetic].
Lemma 6.1 — CORRECT. Prop 6.2 — CORRECT (= Lemma 3.9; precise monotone paths are local chains).
Prop 6.3 — CORRECT (geometry only). Coordinates as in K Prop 4.8 (strict nesting <=> dA dB < 0 <=> |dpsi| > |dphi|;
admissible region <=> 0 <= B <= A <= pi/2). Admissibility: psi <= h_j <= x_1 <= phi and psi <= h_j <= (pi - x_{j+1})/2
<= pi - phi on [x_j,x_{j+1}]; psi = 0 at all x_j (integer number of periods), so the path is continuous; psi -> 0,
phi -> pi give alpha, beta -> inf. A point with beta > M = tan(x_1/2) has phi > x_1, and a small neighbourhood lies on
one or two pieces of slope +-2. Tested numerically (tc_monotone.py). Uncovered from both sides by Lemma 6.1, if the
path is injective in q (it is: phi strictly increasing).
§6 closing paragraph and §7: interpretive; (TC-F1)'s measure clause needs F14b; (TC-F6) is made exact by Cor R (§4.8).

## 6. Items (3), (4) collected

(3) XOR / competitiveness. All XORs are at open-edge selections: E in F_12, E' in F_13, F in F_23 (interior), C_m
in F_12 (Prop 5.3); competitiveness of open-edge q_m via (T2) inside (X2), (X2') (Lemma 3.2, Lemma 4.6). "At least
one" (no V): Prop 4.2 (P2) at E, (alpha) at F, (beta) at E'; Prop 5.3 at C_m. "At most one" (V undominated, union
non-null, third world strict): Lemma 3.5(b) (E, F, E', E' — and E, F for the two added rows), Prop 4.2 boundedness of U
at E', Prop 4.5 transfers at E, F, E', and through (L52)/M2 Lemma 5.2 (unboundedness of h_A'D, h_AC', h_D'C). In every
use the debt set is in the debt region of the world whose acceptance is asserted (tc_regions.py). ALL CORRECT.
(4) Completeness: Lemma 3.2 ((T1) in (X1), (YD), LH 5.1 in the precise case), Lemma 3.3 ((LH)), Lemma 3.5 (strict
rejection at k; strict AC at o; (YD)), (F-c)/(F-d), Prop 4.2, Prop 4.5 ("not Fix" read strictly), Lemma R1, M2 Thm
5.6. Not used: Lemma 3.9 (only (G) at k, l', (S)), Lemma 3.4 beyond (L52), Prop 6.3. V undominated: Lemma 3.4 (TRI),
Lemma 3.5(b), Thm 3.6 (via 3.4, 3.5(b), L52), Prop 4.2 (TRI, XOR), Prop 4.5 (domination, XOR); not in Lemmas 3.2,
3.3, 3.5(a), 3.9, Props 4.3, 4.4 (as order facts), 5.1, 5.3(i)-(ii). The note's own "uses" claims are accurate
(Lemma 3.2's list should add (G) at l' and at all worlds, F2).

## 7. Consolidated list of fixes

 F1 (Lemma 3.2, precise case). Fix the credit levels of the AC pair of cor:LHcons(a): K := (z+3, z+4) (any K above
    z + eta, disjoint from I = (z+1,z+2)), eta := 3; and build Z_I(A) with the b of (YD) for the same A, so that
    A'' subset Tl.
 F2 (Lemma 3.2 "Uses"). Add (G) at l' ((X2), (X2'), (T2)) and (G) at every world (lem:yard).
 F3 (Lemma 3.5(a)). Require l > x_0.
 F4 (Lemma 3.5, Remark (i)). A jump gives at world k a genuine strictly SI pair (fixed debt band alpha in the gap,
    thin credit band delta at y*) — a transversal credit germ — not a "mixed comparison"; RM2 F11's description was
    too weak. Reword.
 F5 (Lemma 3.5(b) table; §0 S3). Add the rows Y = A' (k = 2, X* = D(x**) subset T_0(E), XOR at E, o = 1, frame (1,3))
    and Y = D' (k = 3, X* = C(x**) subset P_3 n {s > alpha^2}, XOR at F, o = 2, frame (2,1)) — both verified — or
    restrict the statement and S3 to the four listed credit families.
 F6 (Thm 3.6). Impose M >= x_0; state the conclusion on [y_0+1, inf).
 F7 (Cor 3.10). Repeat the standing hypotheses (n = 3, complete (G)+(IB) at all worlds, (S)); V enters only as the
    reductio hypothesis.
 F8 (§4). Rename the map k := h_CA (clash with the world index k in Lemma 4.6, Thm 4.7, Cor 4.8).
 F9 (Lemma 4.1(b)). "[(Z1) <=> H^+ >= id]" -> "[(Z1)-freeness => H^+ >= id]".
 F10 (Remark after Prop 4.2). The "at most one" halves are used also via unboundedness of h_A'D, h_D'C (theta,
    chi -> inf) and in Lemma 3.5(b) for (ii).
 F11 (Props 4.3, 4.4). "a point or a segment" -> "a point or a sub-arc"; a_* (and a*, b*, c* in Prop 4.4) large, so
    that fibres avoid x_0 and points of B exist on both sides of the flat level.
 F12 (§0 S6). "left germs appear exactly at jumps" -> "only at jumps".
 F13 (Cor 4.8(c), "Answer to (T2)", §0 S6). By (d), (c)'s hypothesis is equivalent to "N_k meagre and f, g, k
    homeomorphisms at high levels"; delete "'no flat at an uncovered level' replaces 'homeomorphism'"; present (d)
    as the statement and add Cor R (§4.8) as (e). Cor 4.8(a): "[s_1,inf)", s_1 large; (b): s_M also beyond Thm 4.7's
    threshold.
 F14 (Example 4.9; §0 S7; (TC-F1)). (a) Realize the arc as a balanced curve: f = id, g = generalized inverse of
    kappa, k = kappa. (b) The given kappa leaves N_3 of infinite Lebesgue measure, so the "measure" claims are not
    shown; use a pure-jump kappa (w_n > 0, sum over each (j,j+1] equal to 1): then N_3 and N_1 are null and nowhere
    dense (resp. countable), and all claims hold.
 F15 (Prop 5.3(ii)). Weak inequality S <=_c b_eps; for credit-heaviness use a proper non-null S' subset S.
 F16 (5.4 item 4). Add "or not attained (jumped over)".

## 8. Verdicts

 Definition 3.1: CORRECT (consistent use throughout).
 Lemma 3.2: CORRECT WITH MINOR FIXES (F1, F2). Lemma 3.3: CORRECT.
 Lemma 3.4: CORRECT (parameters >= x_0, trivial).
 Lemma 3.5: (a) CORRECT (F3); (b) CORRECT — sign pattern verified row by row (k accepts (X*,delta) => owner o
   strictly rejects (delta,X*), witness X* outside P_o, level in Y's owner frame); table incomplete w.r.t. the stated
   generality (F5, both missing rows verified); Remark (i) reworded (F4).
 Theorem 3.6: CORRECT WITH MINOR FIXES (F6). Corollary 3.7: CORRECT. Corollary 3.8: CORRECT.
 Lemma 3.9: CORRECT (generalizes RM2 Lemma R3, adds "from below"; only (G) at k, l' and (S)).
 Corollary 3.10: CORRECT (F7 cosmetic); needs exactly n = 3, complete (G)+(IB) rankings, (S), six local-chain far
   ends; combines correctly with M2 Thm 5.6 (applied after (TC) is derived) and RM2 Lemmas R1, R3, F9.
 Lemma 4.1: CORRECT (F9). Proposition 4.2: CORRECT (F10). Proposition 4.3: CORRECT (F11). Proposition 4.4: CORRECT
   (F11). Proposition 4.5: CORRECT. Lemma 4.6: CORRECT. Theorem 4.7: CORRECT. Corollary 4.8: CORRECT WITH MINOR FIXES
   (F13: (c) is not a weakening of "homeomorphism"; (d) is the real statement). Added: Cor R (§4.8), PROVED here.
 Example 4.9: CORRECT for Baire category; the measure claims are NOT supported as written (F14b gives the repair).
 Props 5.1, 5.2: CORRECT. Prop 5.3: CORRECT (F15). 5.4: CORRECT as a list (F16). Lemma 6.1, Props 6.2, 6.3: CORRECT.
 No GAP and nothing WRONG in any numbered result; the errors are in interpretive sentences (Cor 4.8(c)'s reading,
 the measure clauses of S7/(TC-F1), S6 "exactly") and in the scope of Lemma 3.5(b)'s table.
