# Development evidence

Outputs from development runs. Development cases are excluded from every
final-panel denominator.

`runs/` remains git-ignored for scratch output. Anything that enters a
denominator lives here and is versioned.

## Provenance limitation

The prompt version used for each run is **not recorded in the output files**
for cases 001 to 003 or for the inference run. The auditor script at the time
recorded the prompt file path, not its contents or version.

Two files carry the auditor version in their filename
(`-auditorv02`, `-auditorv03`). That version is there because it was typed by
hand when the file was copied, not because the script knew it.

`audit-case-004-20260913T121038.json` is the only output written directly by
the script with execution metadata. It still does not record which prompt was
used.

This is the reason for step 2 of the plan: both scripts must record the prompt
content hash and the HEAD commit at execution time.
