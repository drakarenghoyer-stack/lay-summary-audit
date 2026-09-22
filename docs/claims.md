# Claims register

Facts asserted in more than one document. This file is the single source; every
other document must agree with it.

**It checks consistency, not correctness.** If a value here is wrong and every
document repeats it, the check passes. Whether a value is true remains a human
judgement.

Update this file first, then propagate. Last updated: 2026-09-13.

| id | claim | current value |
|---|---|---|
| taxonomy.count | codes in the taxonomy | 17 |
| taxonomy.codes | code identifiers | C1-C6, O1-O11 |
| taxonomy.version | version of error-taxonomy.md | v0.4 |
| taxonomy.intended | eventual intended count | complete: 6 commission, 11 omission |
| panel.total | cases in the final panel | 60 |
| panel.positives | positives in the final panel | 48 |
| panel.negatives | negatives in the final panel | 12 |
| panel.status | execution status of the final panel | designed, not executed |
| dev.cases | development cases | 4 |
| prompt.generator | generator prompt version | v0.4 |
| prompt.auditor | auditor prompt version | v0.3 |
| stage0 | extraction from CSR | not implemented |
| stage1 | generator | implemented, runs on development cases |
| stage2 | auditor | implemented, runs on development cases |
| metrics.computed | any metric computed | none |
| metrics.list | planned metrics | generator error rate by code; auditor sensitivity and specificity; run-to-run stability |
| kappa | inter-rater kappa | withdrawn, sole annotator declared |
| refstandard | reference standard annotation | development cases only |
| trials.selected | published trials selected | 4 of 4 (PARAGON-HF, SELECT, NCT02389816 vortioxetine, RA-BEACON baricitinib); EMPACT-MI remains a fallback |
| extraction.complete | trials with complete extraction | 1 (PARAGON-HF) |
| provenance.recorded | fields recorded at execution time | prompt hash, table hash, HEAD commit, working tree state |
| evidence.location | where denominator-bearing output lives | evidence/, versioned; runs/ ignored for scratch |
| annotation.rules | annotation rules in the protocol | 4 |
| annotation.unit | unit of the reference standard | the finding; a finding may carry several codes |
| metrics.denominators | denominators reported | per-finding (detection) and per-code (classification), reported separately, never pooled |
| model | model identifier in scripts | claude-sonnet-5 |

| metrics.matching_rule | principal detection rule | correct target code and unequivocal localisation; supporting reference assessed separately |
| taxonomy.c5_policy | C5 presentation policy | any effect estimate for an outcome outside the confirmatory testing sequence is C5, even when qualified; nominal favourability is not required |

**Not mechanically checked.** The two entries above are rules, not values. They have no canonical string, so pattern matching over them would produce both false alarms and missed absences. They are recorded here for human reference and verified by reading.

**Adding a value here does not make it checked.** Each entry that can be
contradicted lexically needs a matching forbidden pattern in
`pipeline/check_claims.py`. Changing a value means changing that pattern too.
Nothing signals the omission.

## Documents that must agree

Inside the repository, checked mechanically:

- README.md
- docs/evaluation-protocol.md
- docs/error-taxonomy.md

Outside the repository, updated by hand when a value here changes:

- karen-portfolio.html
- technical-brief (English, current)
- briefing-tecnico (Portuguese, marked superseded 2026-09-13; not to be updated)
- caderno-projeto.pdf

Inside the repository but derived, and not mechanically checked:

- docs/annotation-rules.pdf — typeset extract of the annotation rules, the
  taxonomy, the correspondence rule and the standing decisions. Its content
  lives in docs/evaluation-protocol.md and docs/error-taxonomy.md; this file
  restates it. Regenerate whenever a rule, a code or a standing decision
  changes. check_claims.py cannot read a PDF, so nothing will flag it when it
  goes stale.
