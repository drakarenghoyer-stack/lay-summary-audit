# Findings log

Dated observations from development runs. Nothing here is a result: no
reference standard has been annotated and no metric has been computed.
Entries record what was observed, with the n it was observed at.

---

## 2026-09-11 — Generator fidelity, n=2

Stage 1 run against two evidence tables of the same synthetic trial.

- `evidence-table-commission.json` carries explicit `significant` and
  `multiplicity_adjusted` booleans.
- `evidence-table-inference.json` removes both, and states the testing
  hierarchy in prose under `statistical_analysis_plan`.

In both runs the generator reported that the primary outcome did not reach
significance. In the inference run it further stated that the secondary
outcome fell outside the formal testing sequence because the primary had
failed, and never described it as significant. That qualification was not
available as a field; it required reading prose.

**Observation:** with a well-structured evidence table, generation was
faithful in both conditions, including the condition designed to be harder.

**Hypothesis this suggests, not supported at n=2:** the risk in this pipeline
may sit in stage 0 extraction rather than in generation. This is the
limitation already declared as out of scope in the technical brief §7. If it
holds at corpus scale, stage 0 becomes the object of evaluation rather than
an engineering workstream.

## 2026-09-11 — Non-determinism, observed twice

**As output variance.** Identical input to the commission table, run twice:
1090 and 926 output tokens. Different wording, equivalent content.

**As a failure mode.** A later run raised
`AttributeError: 'ThinkingBlock' object has no attribute 'text'`. The script
was unchanged and had completed three prior runs. The response returned a
thinking block in first position, and the parser selected
`response.content[0]` by position rather than filtering by block type.

**Consequence for the evaluation design:** run-to-run variability is not only
a property of the text to be measured by the stability metric. It also
changes the *shape* of the API response, and a parser that indexes by
position will fail intermittently. Batch orchestration (brief §5.2) cannot
run unattended on position-based parsing. Every response field consumed
downstream must be selected by type or key, never by index.

## 2026-09-11 — Prompt and guidance pull in opposite directions

Generator prompt v0.1 rule 1 required every number in the summary to come
from the evidence table. GLSP v1 §3.4 instructs authors not to use
statistical terms, and §3.3.6 requires statistical concepts to be decoded
into plain language.

Strict literalism therefore pushes the generator to reproduce confidence
intervals, which the guidance asks it to explain instead. The observed
output printed the secondary outcome interval as bare numbers.

**Consequence:** an error scored against the generator here was partly caused
by the prompt. Prompt v0.2 separates "supported by the table" from
"transcribed from the table". Annotation rule 1 in the evaluation protocol
was written before this change, and applies to both prompt versions.

## 2026-09-11 — Normative source drift

GLSP v1 (October 2021) quotes the CTR Q&A in draft form, rendering the lay
summary requirement as primary endpoints "and potentially also"
patient-relevant secondary endpoints, and concludes sponsors may limit
presentation to primary endpoints.

The Q&A in force (July 2026, chapter 6, §6.2) states that overall results
should reflect at a minimum the primary endpoints and patient-relevant
secondary endpoints. The qualifier "potentially" is absent.

**Consequence:** the guidance this taxonomy is derived from predates, and
softens, the interpretation currently in force. Source versions are pinned in
`evaluation-protocol.md` for this reason.
