# State — read this first

If this file and any other document disagree, check the repository.

## What runs
Stages 1 and 2. Stage 0 does not exist.

## Versions
Taxonomy v0.4, seventeen codes: C1-C6 commission, O1-O11 omission.
O2-O11 map one-to-one onto the ten Annex V elements; see docs/annexV-checklist.md.
Generator prompt v0.3. Auditor prompt v0.3. Four annotation rules.

## What has been measured
No metric on the final panel; no result reported. Annotation cost measured:
35 minutes on the first real case, 8 minutes on the second with the Annex V
checklist. Planning figure 10 to 12 minutes per case, putting 60 cases at
10 to 12 hours.

## Panel
Development: four cases, excluded from every final denominator.
Final: 60 planned, not executed. PARAGON-HF extracted, base summary generated, annotated, not admitted.
SELECT extracted, base summary generated and annotated in 8 minutes: two
findings (C6, O11), not admitted. Its two blocked outcomes have intervals
excluding 1, so C5 there is not resolvable from the interval alone. Two trials outstanding, to be selected with lower visibility.

## Next steps
1. Select the two remaining trials, with lower visibility than PARAGON-HF and
   SELECT.
2. Build the trial x code coverage matrix, commission codes only: omission codes
   are constructible in any trial by removal.
3. Confirm the panel size against the measured annotation cost.

## Done
Development evidence versioned in evidence/development/ with its provenance
limitation declared. Both scripts record prompt hash, table hash, HEAD commit
and working tree state at execution time.

## Known gaps
generate.py does not check stop_reason. The PARAGON-HF summary was silently
truncated at max_tokens on the first attempt and only the token count revealed
it.

The PARAGON-HF base summary gives adverse event frequencies as isolated
percentages and is not compliant under rule 4.

## Outside the repository, update at the end of the day
caderno-projeto.pdf is behind: it does not carry C6, taxonomy v0.4, the
PARAGON-HF annotation with its six findings, or the finding that the generator
failed on the first case scored against a fuller taxonomy.
technical-brief.pdf says sixteen codes; it is seventeen.
karen-portfolio.html says 16 codes; it is 17.

Read docs/credentials.md before any command.
