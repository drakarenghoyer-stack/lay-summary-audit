# State — read this first

If this file and any other document disagree, check the repository.

## What runs
Stages 1 and 2. Stage 0 does not exist.

## Versions
Taxonomy v0.2, six codes: C1-C5, O1.
Generator prompt v0.3. Auditor prompt v0.3.

## What has been measured
Nothing. No metric computed, no result reported.

## Panel
Development: four cases, excluded from every final denominator.
Final: 60 planned, not executed. PARAGON-HF extracted, EMPACT-MI candidate,
two trials outstanding.

## Next steps
1. Review the PARAGON-HF base summary against its evidence table under
   taxonomy v0.2, before admitting it as a panel negative. It is in
   evidence/panel-candidates/ with full execution metadata.
2. Select the two remaining trials.
3. Build the trial x code coverage matrix.

Done: development evidence versioned in evidence/development/ with its
provenance limitation declared. Both scripts now record prompt hash, table
hash, HEAD commit and working tree state at execution time.

Known gap: generate.py does not check stop_reason. The PARAGON-HF summary was
silently truncated at max_tokens on the first attempt and only the token count
revealed it.

Read docs/credentials.md before any command.
