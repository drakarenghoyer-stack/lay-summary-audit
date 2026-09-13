# Hallucination detection in clinical trial lay summaries

A generator plus source-blinded, evidence-constrained auditor pipeline for lay summaries produced under EU CTR 536/2014, Annex V, with a defined protocol for measuring generator error rate and auditor accuracy.

> **Status — stages 1 and 2 implemented, evaluation not started.** Architecture specified. Prompts written and versioned. Evaluation protocol v0.1 with pinned normative sources and one annotation rule. Error taxonomy v0.1: 6 codes (C1-C5, O1) of an intended ~13. Stages 1 and 2 run end to end on synthetic evidence tables. **The reference standard is not annotated, so no metric has been computed and no result is reported.** Observations to date are in `docs/findings.md`, each with the n at which it was made.

The deliverable of this project is not the pipeline. It is the quantitative characterisation of the pipeline. Until the reference standard exists, that characterisation does not.

---

## Why

EU CTR 536/2014 requires sponsors to publish a lay-language summary of trial results alongside the technical report. The source material is the Clinical Study Report: hundreds to thousands of pages of statistical tables.

LLMs write these summaries fluently. The failure mode that matters is not grammatical. It is claiming efficacy the data do not support, dropping the fact that a result missed statistical significance, or reporting relative risk where absolute risk is required. In a regulatory document written for patients, that is a compliance failure and clinical misinformation at once.

This project does not ask whether an LLM can write a lay summary. It asks how often it gets this wrong, and how reliably a second system can flag that unaided.

## How

| Stage | Component | Input | Output |
|---|---|---|---|
| 0 | Extraction | CSR (PDF) | Structured JSON evidence table |
| 1 | Generator | Evidence table only | Lay summary |
| 2 | Auditor | Evidence table + generated summary | Discrepancies, classified against the taxonomy |

Neither the generator nor the auditor sees the source CSR. Both are constrained to the same structured evidence table; the auditor additionally receives the generated summary and nothing about how it was produced. It is **source-blinded and evidence-constrained**, not blinded to the generator's input.

The reason for the constraint: if both components read the raw CSR, a shared misreading would pass unflagged, and the auditor would confirm the hallucination rather than catch it. Restricting the comparison to the structured table makes any content in the summary that is absent from the table explicitly testable. Whether the auditor actually detects it is an empirical question, and the point of the evaluation.

The auditor is tuned for sensitivity over specificity. It is a screening test, not a confirmatory one: a false positive costs minutes of human review; a false negative is a false efficacy claim in a published regulatory document.

## What gets measured

**Unit of analysis.** Commission and omission errors cannot share a denominator, so two units are defined:

- **Commission** — the unit is the verifiable claim: a statement asserting something mappable to one or more fields of the evidence table. A sentence may contain several claims and is segmented accordingly.
- **Omission** — the unit is the required element: each Annex V content item expected for that trial. Positive if absent or materially incomplete.

**Metrics**, against a human-annotated reference standard: generator error rate per taxonomy code; auditor sensitivity and specificity, reported separately for commission and omission (primary); run-to-run stability under fixed input.

The design is a diagnostic accuracy study in which the index test is an LLM and the target condition is an unsupported or missing claim.

See `docs/evaluation-protocol.md` for pinned sources and annotation rules, and `docs/error-taxonomy.md` for the codes.

## Corpus

Public sources only. No identifiable patient data.

- Health Canada — Public Release of Clinical Information
- EMA CTIS public portal
- Good Lay Summary Practice (EU guidance) — one of the sources of the taxonomy

All examples currently in this repository are synthetic. No CSR content is reproduced.

## Repository layout
    
    README.md
    docs/
    evaluation-protocol.md    pinned sources, units of analysis, annotation rules
    error-taxonomy.md         the codes, with the source each derives from
    findings.md               dated observations, with n
    prompts/
    generator.md              v0.2
    auditor.md                v0.1
    pipeline/
    generate.py               stage 1
    audit.py                  stage 2
    read_table.py             read an evidence table
    check_table.py            internal consistency check of a table
    examples/
    evidence-table-commission.json
    evidence-table-inference.json

## Running it

Stage 0 is not implemented. The synthetic examples start after extraction, so stages 1 and 2 run without it:

    python3 pipeline/generate.py
    python3 pipeline/audit.py
    python3 pipeline/check_table.py examples/evidence-table-inference.json

Requires anthropic and python-dotenv, and an ANTHROPIC_API_KEY in a local .env file, which is git-ignored.

check_table.py verifies that an evidence table is internally coherent: it recomputes the risk ratio, confidence interval and p value from the per-arm counts and prints them beside the declared values. A table whose declared and computed values disagree would contaminate the evaluation with an error that is not the one being measured.

## Limitations

Read docs/findings.md and the technical brief section 7 before drawing any conclusion from this repository. In short:

- Extraction errors are invisible to the auditor. Generator and auditor inherit the same evidence table, corrupted or not. This pipeline detects generator hallucination; it does not detect extraction error. An independent check on stage 0 is necessary and is not part of the current design.
- Single annotator. Kappa measures agreement with that annotator, not against adjudicated consensus. The comparator is a reference standard, not a gold standard.
- Corpus bias. PRCI and CTIS documents are not a random sample of the literature. Error rates estimated here do not generalise automatically.
- Non-determinism. LLM output varies between runs under fixed input, in content and in response structure. The stability metric quantifies the former; the latter is an engineering constraint on batch orchestration.
- The taxonomy is an interpretation. The codes are one reading of Annex V, the CTR Q&A and the GLSP guidance, at the versions pinned in the protocol. They are not an official classification of any regulatory authority.
- Error rates are prompt-dependent. Generator prompt v0.1 compelled reproduction of confidence intervals, which GLSP asks authors to explain rather than display. Any reported rate is tied to a prompt version.

## Scope

This is a methodological portfolio exercise. It is not a validated system, it has not been submitted to any authority, and it is not intended for use on real regulatory submissions.

## Author

Karen Guimaraes Hoyer, MD - linkedin.com/in/karenguimaraeshoyer

## License

TO DECIDE. Suggested split: MIT for pipeline/, CC BY 4.0 for docs/ and prompts/.

The final panel is designed and has not been executed. Development cases are excluded from every final-panel denominator.
