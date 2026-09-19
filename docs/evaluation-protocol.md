# Evaluation protocol — v0.1

## Normative sources (pinned)

- Regulation (EU) 536/2014, Annex V — legal requirement
- CTR Questions & Answers, July 2026, chapter 6 (§6.1, §6.2) — operative interpretation
- Summaries of Clinical Trial Results for Laypersons, Expert Group
  on Clinical Trials, version 2, February 2018
- Good Lay Summary Practice, version 1, October 2021 — note: GLSP v1
  predates the current Q&A and quotes it in draft form

The taxonomy is one reading of these sources. It is not an official
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
and accessible supplements, selected to permit coverage of the commission codes,
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

C4 10 positives, C3 10, O1 10, C1 6, C2 6, C5 6; 12 negatives. Total 60 (48 positives and 12 negatives).

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
each unit to one of the taxonomy codes or to "no error". The auditor does not
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

## Correspondence rule — three amendments

### 1. Record count and location, not only uniqueness

The manifest records, per positive case: `altered_span`, `occurrence_count` of
that span in the frozen document, and its location. For O1 these fields may be
not applicable; record instead the removed text and its position in the
original.

Uniqueness of the target does not discharge the check. Whether the quote the
auditor actually produced identifies that span is still assessed per finding.

### 2. Revision handling rule

The original manifest is preserved; corrections are versioned, never
overwritten.

If review under boundary rule 4 establishes a second true error in a case, that
case no longer satisfies one-error-per-document. **It is excluded from the
principal analysis and reported separately.** No replacement case is chosen on
the basis of auditor performance. Report how many cases and how many results
were affected.

### 3. Pre-specification does not remove judgement

The rule is pre-specified, and it still requires judgement. Deciding whether an
additional flag is founded, or whether a localisation is unambiguous, remains
interpretation. The worked examples guide that judgement; they do not eliminate
it. With a sole annotator, that judgement is unreviewed.

### Code coverage across trials

Full distribution of every code across every trial is sought where feasible,
not required. Record a trial x code matrix and confirm total coverage before
the final runs.

**Do not force an ambiguous error to fill a cell.** An ambiguous case
contaminates the reference standard, which costs more than an empty cell in the
matrix.

## Correction — taxonomy count and panel coverage

The taxonomy comprises **six** codes: C1, C2, C3, C4, C5 and O1. C5 was added
with annotation rule 2 and is frozen. Documents describing it as five codes
predate that addition and are corrected.

The provisional panel distribution above omitted C5 and is therefore incomplete.
It is not reissued here: the distribution is revised together with the trial x
code coverage matrix, once candidate trials are identified. C5 requires a trial
whose primary outcome failed and whose analysis plan defines a hierarchy, which
is the scarcest requirement in the selection and should drive it.

## Scope of this panel

This panel evaluates the auditor on JSON evidence tables extracted from journal
articles and their supplements. It does not validate extraction from clinical
study reports, and it does not evaluate the full pipeline. Stage 0 as specified
takes a CSR as input; the panel does not exercise that path.

Health Canada PRCI remains an option for a later stage, at substantially higher
extraction cost.

## Source selection criteria

**Inferential strategy must be verifiable**, not merely mentioned. Required:
the testing sequence, the multiplicity control applied, and what happens when a
test in the sequence fails. Article plus protocol plus supplement may document
this adequately; a separately published SAP is convenient, not necessary.

**Document availability is verified per candidate**, not assumed by journal.
Effective access to the needed documents is part of screening.

**A published lay summary, where one exists, is an external comparator only.**
It is not a validated negative and not an automatic conformity standard. It
requires the same review as any candidate negative, and may cover information
absent from the extracted JSON.

**CTIS linkage is an advantage, not a requirement.** Registration alone does not
guarantee the document set.

**Publication date is recorded, not interpreted.** Recent publication does not
establish absence from training data. With four trials, a performance difference
between older and newer cases cannot be attributed to contamination: difficulty,
structure and content vary too.

**Sponsor diversity is sought, not required**, where requiring it would prevent
assembling a well-documented panel.

## Source selection — status

**Selected candidates:**

- **PARAGON-HF** (Solomon et al., NEJM 2019, NCT01920711) remains a candidate for C5, subject to source verification and review of the generated summary.
- **EMPACT-MI** (Butler et al., NEJM 2024, NCT04509674) remains a candidate for the panel and may also support C5 when the selected outcome's confirmatory testing is documented as blocked.

Two further trials are needed, selected for diversity and document availability.

### Criterion for a C5 target

An outcome whose confirmatory testing is blocked by the documented analysis plan. The case presents a point estimate, difference, ratio or per-arm outcome value, even when qualified as exploratory or unconfirmed.

This is the project's presentation policy. Nominal favourability, a confidence interval excluding the null, and an explicit nominal p value are not selection requirements.

Where the source does not report a p value, the JSON records it as not reported, per schema. A computed value must not be presented as though published.

The final panel contains six C5 positives. Development cases, including case-004, are excluded from all final-panel denominators.

### Visibility

Recorded as a secondary preference, never as a contamination control. If
recorded, it must be a defined indicator with a consultation date — a citation
count in a named database, or presence in a named guideline — reproducible by a
third party. Low visibility does not establish absence from training data.

### Source conflicts on a single value

Where sources differ on a value, the field takes the value from the source
recorded in its traceability entry. The primary p value for PARAGON-HF is
recorded as reported in the article version consulted, with that version
identified. A value found only in secondary or tertiary sources does not enter
the JSON.

### What selection does not settle

Meeting the profile does not guarantee an unambiguous injection. The final case
depends on reviewing the generated summary text and confirming the alteration
falls within the operational definition of C5.

## Annotation rule 3 — no figures for a blocked outcome

Rule 2 forbids an effect estimate for an outcome whose confirmatory testing is
blocked. It left open whether raw per-arm counts for such an outcome are
permitted.

**Rule: they are not.** A blocked outcome is reported as measured, qualified per
rule 2 (Q1, Q2, Q3), and with no figures of any kind: no effect estimate, no
per-arm counts, no percentages.

**Rationale.** The lay reader cannot interpret a raw count without the
inferential frame the analysis plan withheld. Presenting it is presenting
apparatus, not information, which is the same objection rule 1 makes to printing
a confidence interval. What the reader needs is the conclusion: the outcome was
measured, it was not formally tested, it supports no conclusion about benefit,
and the full figures are in the scientific summary.

**Scope.** This applies only to outcomes outside the confirmatory sequence.
Counts for tested outcomes, for populations and for adverse events are required
by Annex V and unaffected.

**Consequence for the code.** Reporting any figure for a blocked outcome is C5.
The code definition already reads "point estimate, difference, ratio or per-arm
value"; this rule makes the per-arm clause explicit rather than inferred.

**Consequence for the PARAGON-HF base summary.** Its handling of the renal
composite — measured, qualified, no figures, referred to the scientific summary
— is compliant under this rule, not over-restrictive. Rule 3 was written after
reading that output and is declared as such.

## Annotation rule 4 — adverse event frequency as natural frequency

Annex V element 6 requires a description of adverse reactions and their
frequency. Omission is not an option, so the question is form, not whether.

GLSP v1 numeracy principles require whole numbers, consistent denominators, and
that no calculation be left to the reader. An isolated percentage leaves the
calculation pending: how many people is that, and how large is the difference.

**Rule: adverse event frequency is reported as a natural frequency with an
explicit denominator.** For example, about 16 in every 100 people who took the
intervention, against about 11 in every 100 who took the comparator. A bare
percentage, or a table of percentages without the denominator in words, is an
error.

**Distinction from rule 1.** Confidence intervals and p values are inferential
apparatus: without them the reader loses no fact. An adverse event frequency is
incidence, which is the fact itself. Explain-rather-than-display applies to the
first, not the second.

**Where denominators differ within a trial**, the denominator in use is stated
in words at the point of use, not only in a footnote.

**Consequence for the PARAGON-HF base summary.** Its adverse event table gives
isolated percentages and is **not compliant** under this rule. Rule 4 was
written after reading that output and is declared as such. The summary remains a
panel candidate; its status is decided by scoring, not by the order in which the
rule was written.

### Rule 3 — external convergence

NEJM Evidence editorial policy states that in hierarchical testing procedures,
p values should be reported only until the last comparison for which the p value
was statistically significant, and that p values for the first non-significant
comparison and for all comparisons thereafter should not be reported.

This is an independent source reaching the same position as rule 3, applied to
the scientific article rather than to the lay summary. It does not change the
rule; it records that the position is not particular to this project.
Consulted 2026-09-14.


## Source selection — second candidate confirmed

**SELECT** (Lincoff et al., NEJM 2023;389:2221-32, DOI 10.1056/NEJMoa2307563).
Semaglutide 2.4 mg weekly versus placebo in 17,604 patients with overweight or
obesity and established cardiovascular disease, without diabetes.

Primary MACE: 569/8,803 (6.5%) versus 701/8,801 (8.0%); HR 0.80, 95% CI
0.72-0.90, P<0.001. **The primary was met.**

**Why it is selected.** The hierarchy breaks downstream, not at the primary.
Death from cardiovascular causes did not meet the required p value for
hierarchical testing, and the article reports the two subsequent endpoints in
the hierarchy as point estimates with 95% confidence intervals, stating that the
interval widths are not adjusted for multiplicity and should not be used to
infer definitive treatment effects.

This gives C5 a second mechanism of blocking rather than a repetition of the
first. In PARAGON-HF the sequence never starts; in SELECT it starts, succeeds,
and then stops. A summary presenting a post-block endpoint as confirmed commits
the same error by a different route.

**Structural diversity.** Positive trial; time-to-first-event primary; 17,604
patients against 4,796; different sponsor; endocrine population and indication.

**Visibility.** SELECT is among the most discussed trials of 2023-24, with
several secondary analyses published since. Prior exposure in training data is
possible and is recorded as such, not established. This strengthens the case for
selecting the two remaining trials with lower visibility.

**Pending before extraction.** Locate the statistical analysis plan and confirm
the exact hierarchy: which endpoint failed, its position, and which endpoints
fall after it.

### O11 — scope of "where additional information can be found"

A pointer to the scientific summary for a specific outcome does not discharge
Annex V element 10. The element requires an indication of where additional
information about the trial can be found, in general. A footer carrying the
registration identifier and the primary publication satisfies it; a
outcome-specific referral does not.

## Source selection — third and fourth candidates confirmed

**Vortioxetine phase 3, NCT02389816** (Lu AA21004/CCT-004). Major depressive
disorder, 8 weeks, three arms: placebo, 10 mg, 20 mg, approximately 164 per arm.
Primary: change from baseline in MADRS total score at week 8, analysed by mixed
models for repeated measures. Results posted with least-squares means, standard
errors, confidence intervals and p values. Protocol and statistical analysis
plan are hosted publicly at cdn.clinicaltrials.gov/large-docs/16/NCT02389816/.

What it adds: a continuous primary outcome, a three-arm design, and a small
sample. The three trials already selected all have two arms. The power
calculation cites a two-sided level of 0.025, which implies multiplicity control
across the two doses; the exact structure is to be confirmed from the SAP.

**RA-BEACON, baricitinib in refractory rheumatoid arthritis** (NEJM,
DOI 10.1056/NEJMoa1507247). 527 patients with inadequate response to one or more
TNF inhibitors or other biologic DMARDs, randomised 1:1:1 to baricitinib 2 mg,
4 mg or placebo for 24 weeks. Endpoints tested hierarchically at week 12:
ACR20 response (primary), HAQ-DI score, DAS28-CRP, and SDAI of 3.3 or less.
Comparisons with placebo were made first with the 4 mg dose and then with 2 mg.

What it adds:

1. **A hierarchy in two dimensions.** Endpoint and dose. The sequence runs
   through four endpoints and then repeats for the second dose. This is a richer
   blocking structure than PARAGON-HF and SELECT together.
2. **Responder and continuous outcomes in the same trial.** ACR20 and
   SDAI 3.3 or less are dichotomisations; HAQ-DI and DAS28-CRP are continuous.
3. **A composite responder definition.** ACR20 dichotomises a seven-component
   composite. A summary stating that a given percentage of patients "improved",
   without stating what counts as improvement, commits an error no current code
   covers. A code for this is expected to follow from annotating this trial, in
   the same way C6 followed from annotating PARAGON-HF.

**Coverage across the four trials.** Table formats: recurrent events
(PARAGON-HF), time to first event (SELECT), continuous (vortioxetine),
responder plus continuous (RA-BEACON). Blocking mechanisms: sequence never
starts (PARAGON-HF), sequence starts and stops mid-way (SELECT), sequence
repeats per dose (RA-BEACON).

**Pending before extraction.** Confirm the SAP for each: the multiplicity
structure across doses in NCT02389816, and for RA-BEACON whether the week-12
hierarchy held through all four endpoints at each dose, and what the article
reports for any endpoint falling after a failure.

### NCT02389816 — multiplicity confirmed: Holm, exercised and passed

The SAP controls multiplicity between the 10 mg and 20 mg doses on the primary
outcome by the Holm procedure, two-sided, overall type I error below 5%:

  Step 1. Order the two p values. If the smaller exceeds 0.025, testing stops
  and both null hypotheses are retained.
  Step 2. If the smaller is at or below 0.025, reject it and test the larger
  against 0.05.

Both doses passed: 20 mg p = 0.0023, 10 mg p = 0.0080. The procedure ran to
completion and both hypotheses were rejected. **The trial therefore describes a
blocking mechanism without exercising it**, and is not a source of C5.

**What it tests instead, and why it is structurally distinct.** In PARAGON-HF
and SELECT the sequence is fixed in the SAP before the data. In Holm the order
is determined by the observed p values: the better-performing dose is tested
first, whichever it turns out to be. A summary stating that the 20 mg dose was
tested first is factually correct and methodologically wrong if it presents that
order as pre-specified. This is an error no current code covers, and a code for
it is expected to follow from annotating this trial.

**Secondary outcomes.** The SAP makes no further adjustment for multiplicity on
the secondary outcomes. This is the SAGE-217 situation and falls under rule 3:
unadjusted intervals do not support confirmatory inference. It is not formal
blocking but absence of control, and the two are not the same situation. Whether
a summary presenting such a secondary as established is C2 or C5 is to be
decided before annotation, since the four trials now present three distinct
situations: sequence never started, sequence interrupted, and no adjustment.

### RA-BEACON (NCT01721044) — hierarchy confirmed, broken at the last endpoint

Genovese MC et al., N Engl J Med 2016;374:1243-1252, DOI 10.1056/NEJMoa1507247.
Funded by Eli Lilly and Incyte.

Week-12 sequence: ACR20, HAQ-DI, DAS28-CRP, SDAI 3.3 or less, tested first for
the 4 mg dose and then for 2 mg.

**Outcome.** At 4 mg the first three endpoints reached significance against
placebo; SDAI 3.3 or less did not. The sequence stops there, and the 2 mg
comparisons, which follow the completion of the 4 mg sequence, are blocked in
their entirety.

**Why this is the richest case of the four.** What is blocked here is an entire
dose arm, not an outcome. PARAGON-HF: the sequence never starts. SELECT: it
starts and stops at position one. RA-BEACON: it runs three of four and then
takes down the whole second dimension.

**The characteristic error it enables.** A summary stating that both doses
improved symptoms is factually plausible, because the article reports figures
for 2 mg, and is C5: nothing at 2 mg was tested confirmatorily. This shape does
not arise in any other trial in the panel.

**Also present.** Responder outcomes (ACR20, SDAI remission) alongside
continuous outcomes (HAQ-DI, DAS28-CRP) in the same trial, and a composite
responder definition that ACR20 dichotomises across seven components.

**Pending before extraction.** Confirm from the SAP whether the 2 mg sequence is
gated on completion of the whole 4 mg sequence or on each endpoint in turn, and
confirm what the article reports for SDAI at 4 mg and for all four endpoints at
2 mg.

### RA-BEACON — nominal p values are carried in the evidence table

The 2 mg arm has p values below 0.05 on several outcomes, including ACR20 and
HAQ-DI, sustained to week 24. These are nominal, not confirmatory: the
hierarchical sequence stopped at SDAI in the 4 mg arm before the 2 mg
comparisons were reached.

**Decision: the evidence table carries these p values, each labelled nominal.**

**Why.** A summary stating that both doses worked is not inventing a number here
— it is reading a significant p value that exists in the article. This is the
hardest case available to the auditor: nothing in the figure itself signals the
distinction between nominally significant and confirmatorily demonstrated.

In the other three trials a blocked outcome carries either no p value at all
(PARAGON-HF, SELECT) or an interval excluding 1 with no p. Only here does a
blocked comparison carry a declared significant p. Withholding those values from
the table would let the table decide for the generator and would remove the one
thing this trial tests that the others cannot.

**Consequence for annotation.** Reporting a 2 mg effect as established is C5.
Reporting it as measured, labelled nominal, and qualified per rules 2 and 3 is
compliant. The distinction rests on the label, not on the number.

### Source practice predates the norm; fidelity and compliance can diverge

RA-BEACON reports nominal p values for comparisons that fall after the
hierarchical sequence stopped. NEJM Evidence editorial policy holds that p
values should not be reported from the first non-significant comparison onward.

The article is from March 2016. NEJM Evidence did not exist then. **This is not
a breach of a norm in force; it is an article that predates the norm.** The
convergence recorded under rule 3 is recent, and much of the published corpus
that will feed this panel precedes it. That is itself a finding about the
corpus, not about any one trial.

**Why the nominal values stay in the evidence table.** Rule 3 governs what a lay
summary does. The evidence table is not a summary: it is the reference standard,
and it records what the source states. Removing the nominal p values because a
later norm disapproves of them would editorialise the source and would decide
for the generator the very thing the case exists to test. The point of the case
is that the source offers the number and the summary should not treat it as
confirmation. With no number offered, there is no test.

**The divergence this exposes.** Where a source reports in a way the current
norm disapproves, a summary faithful to the source can inherit the
non-compliance. Fidelity and compliance are not the same axis. This is the same
divergence that appeared when the generator was faithful to the evidence table
and failed on mandatory-element completeness: a summary can be accurate about
its source and wrong about its obligations.

**Consequence for annotation.** A finding is scored against the taxonomy, not
against the source's own practice. That a source did something does not make it
compliant for a lay summary to repeat it, and the annotation records the code
rather than the provenance of the habit.
