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
