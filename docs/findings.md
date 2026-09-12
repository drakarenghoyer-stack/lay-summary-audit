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

## 2026-09-11 — Platform divergence in command-line tooling

Development is on macOS (zsh, BSD userland). Two commands used while editing
project files behave differently under the GNU userland found on most Linux
systems:

- `sed -i` requires an empty argument on macOS (`sed -i '' 's/a/b/' file`).
  On GNU sed the empty argument is read as a filename and the command fails.
- `cat -A` does not exist on macOS; the equivalent is `cat -et`.

Neither affects the pipeline itself, which is Python. Both affect any shell
step used to prepare, inspect or post-process files.

**Consequence for reproducibility (brief §5.5):** a third party cloning this
repository on Linux will not reproduce shell-level steps that assume BSD
tooling. Any shell step that becomes part of the pipeline must either be
written portably or be replaced by Python. The remote host available for
future batch orchestration is Linux, so this divergence will surface there
rather than here.

Recorded because the requirement is that a third party can clone, run, and
obtain the same number. Platform-dependent tooling is a silent way to fail
that requirement.

## 2026-09-11 — Case panel v0.1: first C4 pair

Panel construction validated on one pair. case-001 is the generator v0.3 output
on the inference table, unmodified. case-002 is identical except for one value
in the adverse events table: hypoglycaemia in the intervention arm, 4.8% to
5.8%. Diff confirms a single altered line (28c28), no downstream consequence.

The value was chosen because it appears once in the summary, carries no derived
percentage or calculation, and the adjacent prose is qualitative and remains
true after the edit.

**Result.** case-001: no finding. case-002: one finding, correctly coded C4,
with an explanation naming the table value and the summary value. One true
negative, one true positive. Output tokens 9 and 95: an empty findings array
costs almost nothing, which is relevant to batch cost control.

**Verification.** case-001 was annotated by the author against the evidence
table under taxonomy v0.1 and found clean. The auditor returning zero on it
does not verify anything, since the auditor is the system under evaluation.

**Declared limitation of the panel.** Injected errors are the errors the author
could construct. Sensitivity observed on this panel describes performance
against deliberately injected errors of known type; it does not estimate
sensitivity against the errors a generator produces spontaneously. These are
different quantities and the second is the one that matters in a regulatory
setting.

## 2026-09-11 — Quote extent varies between runs

The same summary (case-002) was audited twice with an unchanged script and
prompt. Both runs returned one finding, correctly coded C4, with the same
explanation. The cited span differed: "5.8%" in the first run, the full table
row in the second. Output tokens 95 and 121.

**Consequence for the protocol:** run-to-run variability appears not only in
the verdict but in localisation. Comparing auditor output against human
annotation requires a matching rule: does a partial quote that points to the
correct span count as agreement, or is a minimum overlap required? Undecided.
Kappa cannot be computed until it is.

## 2026-09-11 — Prose C4 detected; panel v0.2

case-003 inverts the direction of a prose claim about nausea frequency:
"more often in people taking synthemide than in those taking placebo" becomes
the reverse. Target chosen as the adverse event with the largest margin
(22.4% vs 9.1%), so the altered claim is unambiguously false rather than a
matter of description. Diff confirms a single altered line (31c31); that line
is a two-sentence paragraph and only the nausea clause changed.

Detected, coded C4, with an explanation naming both table values and the
reversal. Three injected positives so far, three detections, no false
negatives; one negative, no false positive. These are development cases and
do not enter any reported denominator.

**Recorded as a property of this case, not a result:** the summary contains
an adverse events table showing 22.4% and 9.1% a few lines above the altered
prose, so the case carries an internal contradiction in addition to the
discrepancy with the source. This is one alteration manifesting twice, not two
errors, but it gives the auditor a cue a naturally occurring error might not
carry. Logged in the manifest as internal_contradiction.

**Codes do not divide by format.** A quantitative claim stated in prose and
contradicted by the table is C4, not C1. The operational definition turns on
the content of the discrepancy, not on whether it appears in digits.

## 2026-09-11 — Audit cost scales with case difficulty, not findings count

Output tokens by case: case-001 (no finding) 9; case-002 (numeric substitution)
95 and 121 across two runs; case-003 (prose inversion) 733. The stored JSON for
case-003 is one finding of roughly 80 tokens, so most of the 733 was reasoning
before the answer, not the answer.

**Consequence for batch orchestration (brief §5.2):** estimating cost per
document from the size of the visible output underestimates it, here by a
factor of about six. A panel weighted toward difficult cases costs
substantially more than the same panel of easy ones, with the same number of
findings in each.

**Testable consequence for the stability metric:** if output variability tracks
reasoning volume, difficult cases should vary more between runs than easy ones.
Two runs exist for case-002; none repeated for case-003.

## 2026-09-11 — Annotation cost measured on one case

case-002 was annotated from scratch by the author, without consulting the
manifest, against the evidence table under taxonomy v0.1. **Five minutes, one
finding**, matching the manifest. Independent reading confirms case-002 is a
single-error case.

Construction of case-003 took roughly ten minutes, with the target selection,
margin check and manifest text supplied in conversation rather than decided
alone; unassisted construction would take longer.

**Use for panel sizing.** Five minutes is a floor, not a mean. case-002 is the
easiest available case: one substituted number in a table, in a base text the
annotator had already read. C5 and O1 require reasoning about the testing
hierarchy and checking three qualification elements; different base texts
remove the familiarity advantage. Planning figure: 8 to 10 minutes per case,
putting a 50-case panel at 7 to 8 hours of annotation. Viable.

Annotation, not construction, is the cost that scales with panel size.
