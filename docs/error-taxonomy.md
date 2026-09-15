# Error taxonomy — v0.2

Derived from the sources pinned in `evaluation-protocol.md`. One reading of
those sources, not an official classification of any authority.

Codes are added only when a case has been observed or is specifically
required by a source. This file starts at 6 codes, not 13; the remainder are
to be derived from the Annex V elements and from annotation of real cases.

## Commission — unit: the verifiable claim

**C1 — Unsupported efficacy claim.**
States or implies benefit that the evidence table does not support.
Source: Annex V element 7; CTR Q&A July 2026 §6.2.

**C2 — Significance misstated.**
Reports a result as reliable, confirmed or significant when the analysis plan
or the reported values do not support it. Includes treating an outcome
outside the confirmatory sequence as confirmed.
Source: CTR Q&A July 2026 §6.2; GLSP v1 §2.2.2.

**C3 — Statistical apparatus displayed.**
Prints a confidence interval, p value or test statistic as a numeric value
instead of decoding the uncertainty into plain language. Applies regardless
of whether the value matches the table.
Source: GLSP v1 §3.4, §3.3.6. See annotation rule 1.

**C4 — Numeric error.**
A quantitative statement that contradicts the table: wrong value, wrong
denominator, wrong direction, or an arithmetic derivation that does not
follow from the table.
Source: GLSP v1 §3.3.8 (quality control against source).

**C5 — Untested outcome given an effect estimate.**
Reports a point estimate, difference, ratio or per-arm value for an outcome
that falls outside the confirmatory testing sequence. Applies whether or not
the statement is qualified.
Source: GLSP v1 §2.2.1, §2.2.2; CTR Q&A July 2026 §6.2. See annotation rule 2.

## Omission — unit: the required element

**O1 — Uncertainty not qualified.**
A non-significant or non-confirmatory result is presented without conveying
that it is unreliable or unconfirmed.
Source: GLSP v1 §2.2.2 (the LS should help the reader understand the
uncertainties in statistically non-significant secondary endpoints).

## Not yet derived

Codes for the remaining Annex V elements (trial identification, sponsor,
population, adverse reactions and frequency, comments on outcome, follow-up
trials, where to find more information) are pending. Each requires deciding
what counts as materially incomplete for that element.

## Omission — unit: the required element

The Annex V elements are listed in `annexV-checklist.md`. One code per element.
O1 is retained with its existing meaning and is not an element code.

**O2 — Trial identification absent or incomplete.**
Title, protocol number, EU trial number or other identifiers missing.
Source: Annex V element 1.

**O3 — Sponsor absent.**
Name or contact details of the sponsor missing.
Source: Annex V element 2.

**O4 — General information absent or incomplete.**
Where or when the trial was conducted, the main objectives, or the explanation
of the reasons for conducting it, missing.
Source: Annex V element 3.

**O5 — Population absent or incomplete.**
Number of subjects, age group breakdown, gender breakdown, or inclusion and
exclusion criteria, missing.
Source: Annex V element 4.

**O6 — Investigational medicinal products absent.**
Source: Annex V element 5.

**O7 — Adverse reactions or their frequency absent.**
Source: Annex V element 6. Where the source carries only a pre-specified subset,
a summary that states the limitation is not scored under O7; failing to state it
is.

**O8 — Overall results absent.**
Source: Annex V element 7.

**O9 — Comments on the outcome absent.**
Source: Annex V element 8.

**O10 — Follow-up trials not indicated.**
Source: Annex V element 9.

**O11 — Where to find additional information absent.**
Source: Annex V element 10.

Codes are scored against the generator only where the evidence table carries the
information. A gap present in the table is an extraction gap and is recorded
separately.
