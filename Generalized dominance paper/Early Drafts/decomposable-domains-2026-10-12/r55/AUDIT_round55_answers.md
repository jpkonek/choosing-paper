**The limit observation is useful, but I would not adopt the proposed defaults.** They risk moving almost the entire problem into constructing the starting relation.

There are also two qualifications to the limit argument. These should be settled before the next brief.

### What the decreasing-limit argument actually gives

For a **fixed selection** \(p\mapsto C_p\), intersecting a decreasing chain of relations preserves:

- guidance and independence;
- (TC);
- closed fixed-rival sections;
- support defence, provided it holds at every stage;
- undominatedness of each model that is protected at every stage.

The finite-world defence argument works for transfinite chains too: if every world eventually refused a particular defence, finitely many stages would already witness its failure.

However:

- **Global direct (C) needs care.** A coherent model can become undominated only at the limit. Its tie partners were not necessarily constrained by (C) at earlier stages. Preservation for designated protected models does not automatically prove the global axiom.
- If stages deliberately fail (C), the limit does not repair that automatically. Every offending tie must actually be removed, and new relevant cases must be accounted for.
- None of this transfers automatically when the selection changes.

Also, **“each verdict changes only finitely often” is insufficient for closed sections**. The closed sets \([1/n,1]\) converge pointwise to \((0,1]\); each point changes membership at most once, but the limit is not closed.

### 1. The two-neighbourhood test

The intended test is more specific than your description.

Choose a nonconic swap between two interior selected models:
\[
X=C_a[F\mapsto C_b],\qquad
Y=C_b[F\mapsto C_a].
\]

Require **the same world \(w\)** to refuse
\[
C_p\preceq_w X\quad\text{throughout an open neighbourhood of }a,
\]
and
\[
C_q\preceq_w Y\quad\text{throughout an open neighbourhood of }b.
\]

At the centres, these are inverse records. Their same-world refusals deliberately escape common reweighting. Keep universal defence, protection, (G), (IB), and (TC).

This remains a rejection test—not the principal construction objective.

### 2. What may be revised?

During exploration, both acceptances and refusals may be revised. But a proof cannot simply rely on their eventually settling.

For the construction theorem, I recommend a distinction between:

- **provisional choices**, which may be revised;
- **committed comparisons and refusal neighbourhoods**, which may not.

The eventual relation must honour every commitment. Provisional relations need not themselves satisfy every axiom on every model; the commitments must remain jointly consistent and the final obligations must all be discharged.

This avoids freezing an accidental additive kernel while retaining something precise to preserve at limits.

### 3. Do not make the proposed starting relation the first theorem

Your proposed start already has closed sections, full face defence, structural axioms, and undominatedness. Finding it without an endorsing field is already most of the difficult construction.

**I do not currently have such a start.** Asking an agent to produce it would largely restate the problem.

The alternative is a partial construction whose initial commitments are modest:

- the target is assigned to a specified interior index;
- guidance is mandatory;
- independence identifies equal records;
- required face restrictions are recorded;
- target protection and defence remain explicit disjunctive obligations.

The hard theorem is then an extension theorem for these partial commitments. It must have a substantive, checkable hypothesis—not “the partial system is extendible.”

### 4. Use a partial system, not a total allocation

Choose **(b)**.

Unknown comparisons should remain genuinely unassigned. Do not interpret them as refusals, and do not fill them with an additive default.

An extension can:

- assign a coherent model at an unassigned index;
- settle previously unassigned records;
- commit a refusal neighbourhood;
- resolve a defence obligation at an available world.

Equal records are identified immediately. Any consequences for already committed comparisons must be checked before the extension is accepted.

This formulation keeps the defender variable without pretending that its comparisons are independent of previous choices.

### 5. Handle selection by commitments plus neighbourhood reservations

I would use neither unrestricted revision of the selection nor an unproved correspondence-selection principle.

Use a fixed index simplex with a **partially assigned selection**:

- once \(C_p\) is committed, it stays fixed;
- unassigned indices retain their choice of coherent model;
- a committed refusal at \((p,X,i)\) includes an open neighbourhood \(U\ni p\);
- every future assignment \(C_q\), \(q\in U\), must satisfy \(C_q\not\preceq_i X\).

Thus a refusal neighbourhood reserves obligations at indices whose models have not yet been chosen.

This directly incorporates co-design: future defenders must fit the existing neighbourhood obligations, rather than being chosen first and reconciled afterwards.

At the end, if every index and comparison has been assigned and every refusal has such a reservation, its fixed-rival refusal set is open. That supplies the section argument.

**The unproved part is whether the required extensions exist.** The reservations could exhaust the available coherent models or defending worlds. That is exactly what the constructor and adversary must investigate.

A closed-graph correspondence is not a shortcut: extracting a selection with the required comparison sections would be another substantial theorem.

### 6. Include faces from the beginning; allow transfinite methods

The simplex and all face obligations should be present from the start. Individual indices may remain unassigned, but their obligations cannot be deferred.

A transfinite construction using choice is acceptable as an existence proof. It need not be countable merely for presentational elegance.

However, a well-ordering is only bookkeeping. **The mathematical content must be the extension lemma and the preservation argument.** “Process the next rival” is not a construction until we prove that the next step can always be performed.

### 7. The first extension should test genuine choice of defender

Do not begin by repairing a balanced tie in an almost-complete starting relation that we do not possess.

Instead, test this:

> Starting with T and a small set of genuine commitments, introduce a rival that requires a new coherent defender. Choose that defender and its index jointly, establish its defence and protection obligations, and commit the refusal neighbourhoods needed at both T and the new defender—without exhausting any face-defence obligation.

The balanced-swap configuration should be an adversarial instance of this step. The defender must remain a variable; no cap, posterior, or edge restriction should be imposed unless derived.

**My recommendation is therefore a partial, commitment-based construction—not refusal-only refinement of an already nearly complete relation.** The latter has an attractive limit argument but no accessible starting point. The former exposes the real missing theorem: whether coherent defenders and open refusal reservations can always be extended together.

That theorem would be a route to coverage. Another successful local ranking, without such an extension mechanism, would not.