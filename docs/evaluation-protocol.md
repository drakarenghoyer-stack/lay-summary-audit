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
