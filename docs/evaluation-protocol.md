# Evaluation protocol — v0.1

## Normative sources (pinned)

- Regulation (EU) 536/2014, Annex V — legal requirement
- CTR Questions & Answers, July 2026, chapter 6 (§6.1, §6.2) — operative interpretation
- Summaries of Clinical Trial Results for Laypersons, Expert Group
  on Clinical Trials, version 2, February 2018
- Good Lay Summary Practice, version 1, October 2021 — note: GLSP v1
  predates the current Q&A and quotes it in draft form

The 13-code taxonomy is one reading of these sources. It is not an official
classification of any regulatory authority.

## Annotation rule 1 — statistical apparatus

Confidence intervals, p values and test statistics are statistical terms.
GLSP v1 §3.4 lists "do not use statistical terms" among its writing
principles, and its health numeracy principles require whole numbers,
consistent denominators and units, and that no calculation be left to the
reader. GLSP §3.3.6 states that lay readers generally do not understand
statistical concepts and that the author should decode them into plain
language.

**Rule: uncertainty must be explained, not displayed.**

- A summary that states the direction and size of an effect in plain words,
  and conveys the uncertainty qualitatively, is FAITHFUL.
- A summary that prints a confidence interval, a p value or a test statistic
  as a numeric value is an ERROR, regardless of whether the value matches
  the evidence table.
- This applies independently of sign convention. Whether a reported interval
  preserves the sign of the source value is not assessed, because the
  interval should not be reported at all.

Rationale: accuracy against source is checked at the level of the
quantitative statement (GLSP §3.3.8, quality control), not at the level of
statistical notation. Reproducing notation is therefore not a defence.

## Open

- Whether the generator prompt should be revised so that literalism does not
  compel reproduction of intervals. Current prompt (v0.1) does compel it.

## Annotation rule 2 — outcomes outside the confirmatory sequence

Where the statistical analysis plan defines a fixed testing hierarchy and the
primary outcome does not reach the required threshold, any secondary outcome
downstream in that sequence was not formally tested. Its nominal values carry
no inferential weight.

CTR Q&A July 2026 §6.2 requires overall results to reflect at a minimum the
primary endpoints and patient-relevant secondary endpoints. GLSP v1 §2.2.1
discourages presenting tertiary or exploratory results, and §2.2.2 requires
that selection of patient-relevant secondary endpoints be governed by a policy
fixed before results are available, so that inclusion is not decided by the
result. An untested secondary is functionally exploratory.

These reconcile if "patient-relevant" is determined by the analysis plan and
not by the outcome. The hierarchy governs *how* such an outcome is presented,
not *whether*.

**Rule: the outcome is reported without an effect estimate, and its mention
carries a qualifying statement.**

Reporting a point estimate, difference, ratio or per-arm value for an outcome
outside the confirmatory sequence is code C5, whether or not it is qualified.

The qualifying statement must contain three elements. Wording is free, since
the summary is written in lay language; the elements are not.

- **Q1** — that the outcome was measured, and where the full results are
  recorded (reference to the scientific Summary of Clinical Trial Results).
- **Q2** — that it was not formally tested, and why: the primary outcome did
  not reach the required threshold.
- **Q3** — that the result does not support a conclusion about benefit.

A missing element is code O1. Annotate O1 once per outcome, listing which of
Q1, Q2 or Q3 is absent.

**Rationale.** The asymmetry used to calibrate the auditor applies to
presentation as well as detection: omitting an exploratory figure costs a
reader little, while a reader treating it as a demonstrated benefit costs a
great deal.

**Known consequence.** Under this rule the v0.2 output is positive for C5. It
reported per-arm HbA1c changes and the between-group difference for an outcome
outside the sequence. It qualified the result, which satisfies Q2 and Q3, but
the estimate should not have been given at all. Rule 2 was written after that
output was produced and read; it is not a post-hoc reading of it.

## Panel design — provisional, not frozen

Numbers below are targets. None is frozen until the four source trials are
selected and unambiguous cases of each code are confirmed constructible from
them. Confirmation happens before any final-panel run, never after observing
auditor performance.

### Fixed now

**Development cases excluded.** case-001, case-002 and case-003, and the
synthetic trial they derive from, are development material. They enter no
denominator.

**Source material for the final panel.** Four published trials with full text
and accessible supplements, selected to permit coverage of all five codes,
including positive and negative results, a testing hierarchy, and sufficient
safety data.

For each trial: extract a JSON evidence table with every field traceable to
page, table or section; verify denominators, follow-up periods, effect measures
and multiplicity rules; generate summaries from the JSON and review them for
conformity; inject errors into summaries only, never into the JSON.

The auditor receives JSON plus summary. It assesses fidelity to the JSON.
Human review verifies fidelity of the JSON to the article. Any information
required to assess a code must be present in the JSON.

**Correspondence rule.** A detection corresponds to the reference error when it
carries the correct code and unambiguously locates the altered claim. Verbatim
reproduction and identical punctuation are not required. For O1, it must
identify the missing mandatory element and its reference evidence; quoting
absent text is not required.

Recorded separately: correct code; correct localisation or identification of
the omission; combined correspondence.

Also pre-specified: how additional flags, duplicates, and correct-discrepancy-
wrong-code outcomes are treated.

**Execution freeze, to be recorded before the final run.** Auditor prompt and
taxonomy with versions and commit hash; exact API model identifier and run
parameters; one run per case for the primary metric; a stability subset chosen
in advance with three runs per case, the first remaining in the primary
analysis; reference manifest inaccessible to the auditor.

### Provisional targets, conditional on code coverage

C4 10 positives; C3 10; O1 10; C1 6; C2 6; negatives 12. Total 54.

The smaller n for C1 and C2 reflects construction and judgement cost, not lower
importance of those codes. O1 also requires judgement: removing text is
mechanical, but verifying that the removed information was mandatory and does
not survive elsewhere in the summary is not.

**Negatives are not negative by origin.** A generator output is a candidate
negative. Each is reviewed against the JSON and the taxonomy before admission.
Record how many outputs were rejected or corrected; corrected versions are
identified as such.

Each code is distributed across the four trials, and results are reported by
trial as well as pooled.

### Declared limitations of the panel

**Dependence.** Four base texts increase diversity; they do not remove
dependence between variants of the same text. Binomial intervals reported here
assume independence and that assumption is violated by construction. Exact
two-sided Clopper-Pearson lower bounds under perfect performance: 6/6 54.1%;
10/10 69.2%; 12/12 73.5%. The panel is exploratory and was not sized to
estimate sensitivity with precision.

**Training contamination, direction unknown.** Published trials may appear in
the model's training data. Removing names and titles does not guarantee
removal of prior knowledge. This can bias detection in either direction: prior
knowledge may make injected errors easier to detect, and it may also cause a
summary faithful to the extracted JSON to be flagged where the JSON diverges
from what the model recalls of the article, inflating false positives among the
negatives.

**Injected errors are not spontaneous errors.** Real source material does not
make deliberately injected errors representative of what a generator produces
unprompted.

**Annotation time.** The 7-9 hour figure covers annotation only. It does not
include trial selection, JSON extraction and verification, or resolution of
ambiguities.

### Kappa — design pending

The correspondence rule does not by itself define a kappa. Kappa requires two
raters classifying a fixed set of units into the same categories.

Intended design: two independent raters judge correspondence of each auditor
output, before resolution of disagreements. Kappa then measures agreement
between human raters on the assessment of auditor outputs.

**If only one rater is available, no inter-rater kappa is reported.**

An auditor-versus-human kappa is possible in principle but is not adopted here.
It would require fixing the unit set in advance — every verifiable claim in
each summary, segmented per the protocol definition — and both raters assigning
each unit to one of the five codes or to "no error". The auditor does not
classify a fixed unit set; it emits findings freely, and converting free output
into per-unit classification is itself a judgement. Recorded so that the absence
of an auditor-human kappa reads as a decision rather than an omission.

### Side effect worth recording

Manual JSON extraction with traceability to page and table produces a
gold-standard stage 0 output for each trial. Stage 0 is out of scope for the
current design and is the stage the findings log identifies as the likely locus
of risk. The extraction artefacts are therefore an input to a future stage 0
evaluation, not only a means to this one.

## Kappa — superseded

The "Kappa — design pending" section above is superseded. No inter-rater kappa
is planned for this stage.

**Decision for this stage:** pre-specified correspondence rule with worked
boundary examples; sole annotator, declared; intra-rater re-assessment
optional, not a pilot requirement.

Sensitivity, specificity and stability remain the focus, each reported
conditional on the quality of the reference standard.

### If intra-rater re-assessment is done

It re-judges the same frozen auditor outputs, with order and identifiers
shuffled, without access to the prior judgement. Re-running the auditor would
measure something else: model stability, which has its own metric.

The subset is chosen in advance and spans codes, negatives and source trials.
Any subset of this size is exploratory; it is not a size justified for
estimating agreement with precision.

Report raw agreement and the disagreements alongside any kappa. Kappa depends
on the distribution of categories and is undefined when both sets of judgements are constant in
one category, which is plausible here.

**Consistency is not correctness.** The same mistaken rule can be applied on
both occasions. Absence of independent review remains a limitation regardless
of the intra-rater result.

### Criterion for a second rater, if one becomes available

Demonstrated competence in applying the taxonomy, training on the rule, and
independence from the panel's construction. Clinical or regulatory background
matters where the judgement requires medical interpretation, which applies to
some codes and not to all. The criterion is competence, not profession.

## Correspondence rule — boundary cases, resolved

Principal correspondence requires correct code plus unambiguous localisation.
Supporting reference is assessed separately and does not gate the principal
count.

| Situation | Verdict |
|---|---|
| 1. Partial quote | Accept if it unambiguously identifies the altered span. A bare value suffices where that value appears once in the document; where it appears more than once, additional context is required. |
| 2. Correct localisation, wrong reference | Count the principal detection. Mark the reference incorrect. This prevents describing it as a fully supported detection. |
| 3. Correct discrepancy, wrong code | Not a hit for sensitivity of the target code. Record separately that the discrepancy was recognised but misclassified. |
| 4. Additional flag | Preserve the hit on the injected error. Review the additional flag: if unfounded, record a false alert; if founded, revise the reference standard, since the case may contain another error. |
| 5. Duplicate | Count one detection; record duplication separately. Two findings describing one discrepancy do not produce two hits. |
| 6. O1 without reference | Count identification of the omission if code and missing mandatory element are unambiguous. Mark support absent. The mandatory status must be demonstrated in the reference standard by the applicable rule and the data required. |

### Denominators do not mix

A false alert on a positive case does not enter the specificity calculation
over the 12 negatives. False alerts are recorded per case or per finding in a
separate measure.

On negatives, for document-level specificity, any unfounded alert makes the
document a false positive.

### Scope of the principal metric

As written, the principal metric is detection: correct code and correct
localisation. Requiring a correct supporting reference as well would change it
to evidence-supported detection. That is a different metric and would have to
be declared before evaluation, not chosen afterwards.

### Two operational consequences

**Uniqueness of the altered string.** Rule 1 is applicable only if uniqueness
is verified per case rather than judged at annotation time. The manifest
records, for each positive case, whether the altered string occurs once in the
document.

**Manifest revision log.** Rule 4 permits revising the reference standard after
seeing auditor output. Correcting a mislabelled case is legitimate; it is
indistinguishable from post-hoc adjustment unless logged. Every revision
records date, reason, what changed, and which auditor output prompted it.

### Status of the boundary examples

Boundary examples make the rule auditable. They do not substitute for evidence
of independent agreement.

Rules are closed using the development cases and then applied unchanged to the
final panel.
