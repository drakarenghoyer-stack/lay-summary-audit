# State — read this first

If this file and any other document disagree, check the repository.

## What runs
Stages 1 and 2. Stage 0 does not exist.

## Versions
Taxonomy v0.4, seventeen codes: C1-C6 commission, O1-O11 omission.
O2-O11 map one-to-one onto the ten Annex V elements; see docs/annexV-checklist.md.
Generator prompt v0.4. Auditor prompt v0.3. Four annotation rules.

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
excluding 1, so C5 there is not resolvable from the interval alone. Third and fourth trials selected: NCT02389816 (vortioxetine, continuous MADRS,
three arms) and RA-BEACON (baricitinib, hierarchy across four endpoints and two
doses, responder plus continuous). Neither extracted yet.
NCT02389816 uses Holm between doses; both passed, so it describes a blocking
mechanism without exercising it. It is not a source of C5.
RA-BEACON (NCT01721044): the 4 mg sequence passed three of four endpoints and
failed at SDAI, blocking the entire 2 mg dose arm. What is blocked is an arm,
not an outcome: a third distinct mechanism.

## Next steps
1. Regenerate the four base summaries with generator v0.4 and review each
   against the Annex V checklist and taxonomy v0.4. Clean ones become
   negatives and injection bases.
2. Update the auditor to taxonomy v0.4. Auditor prompt v0.3 knows six codes
   (C1-C5, O1) and audit.py rejects any other as unknown. Running the panel
   now would score the auditor on eleven codes it cannot produce.
3. Fix the panel size per code, counting base texts, not injection sites:
   four for every commission code, three for C5. Settle how O2-O11 are
   sampled and how many distinct negatives each trial supplies.
4. Build the panel.

Decided: four trials. C5 proceeds with three base texts, declared. A fifth trial
may be added only before the final run, never after results are seen.

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

Read docs/credentials.md before any command.
