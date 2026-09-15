# State — read this first

If this file and any other document disagree, check the repository.

## What runs
Stages 1 and 2. Stage 0 does not exist.

## Versions
Taxonomy v0.4, seventeen codes: C1-C6 commission, O1-O11 omission.
O2-O11 map one-to-one onto the ten Annex V elements; see docs/annexV-checklist.md.
Generator prompt v0.3. Auditor prompt v0.3. Four annotation rules.

## What has been measured
Nothing. No metric computed, no result reported.

## Panel
Development: four cases, excluded from every final denominator.
Final: 60 planned, not executed. PARAGON-HF extracted and a base summary
generated; EMPACT-MI candidate; two trials outstanding.

## Next steps
1. Record the PARAGON-HF annotation under taxonomy v0.3 in the manifest, with
   the codes now applicable under rules 3 and 4. This is registration, not
   measurement: the annotator already knows where the omissions are, so it is
   declared non-blind and produces no timing figure.
2. Select the second trial, extract its evidence table, generate a base summary.
3. Annotate that one with the Annex V checklist, timed. That is the figure that
   sizes the panel; the 35 minutes from the first reading included learning the
   task and had no checklist.
4. Select the two remaining trials.
5. Build the trial x code coverage matrix, commission codes only: omission codes
   are constructible in any trial by removal.

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
