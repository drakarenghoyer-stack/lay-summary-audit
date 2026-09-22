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

## 2026-09-12 — Development C5 case-004

One development case, one execution. Auditor prompt v0.2.

The summary was altered by substitution to include the correct HbA1c
effect magnitude (0.68 percentage points), while retaining the
qualifications about blocked confirmatory testing.

The auditor returned one C5 finding, with unambiguous localisation
and a pertinent supporting reference. No additional findings were returned.

Output: runs/audit-case-004.json
Output commit: b4cbbf1

This exercises the project's presentation policy. It does not establish
general performance or isolate understanding of gatekeeping.
The case is excluded from all final-panel denominators.

## 2026-09-13 — Auditor prompt v0.3: anticipatory clause removed, detection unchanged

Auditor prompt v0.2 line 26 defined C5 and added: "Applies even when qualified
as exploratory or unconfirmed." case-004 was constructed preserving the
blocking caveats precisely to exercise that situation, so the prompt resolved
in advance the ambiguity the case was built to test. Instruction and test
coincided.

The clause was removed (auditor v0.3). What remains is the code definition and
the statement that this is the project's presentation policy, which is the same
level of abstraction as generator rule 8: it states the principle without
resolving the instance.

**Result.** case-004 re-audited under v0.3: one finding, C5, correct
localisation. Detection did not depend on the removed clause. Output under v0.2
frozen at `runs/audit-case-004-auditorv02.json` before the change; v0.3 output
at `runs/audit-case-004-auditorv03.json`. The original record was not replaced.

**The diff is more informative than the verdict.** Under v0.2 the explanation
read that the policy prohibits the estimate "regardless of qualifying
language". Under v0.3 that clause is absent and the explanation reasons
directly from the block to the reported estimate. The auditor was echoing the
instruction; without it, the reasoning stands on the code definition alone.

`table_reference` also changed, from free-text description to the structured
path `outcomes[1].point_estimate`. Not requested by the change; more usable for
annotation.

**Consequence for the protocol.** A single sentence in the auditor prompt
altered the content of the explanation while leaving the verdict intact. Freezing
a prompt version number is insufficient; the frozen artefact is the prompt text,
with its hash, and any change to it invalidates comparison with prior outputs.

**Limits of this observation.** One case, one run per version. It does not
establish that the clause never affects a verdict, only that it did not affect
this one. Output tokens 477 under v0.2 and 457 under v0.3; the difference is not
interpretable at n=1.

## 2026-09-13 — Claims register and consistency check

Four documents asserted different states of the project at the same time. None
was written in bad faith: each was correct when written and the project moved.
The Portuguese briefing still said the architecture was implemented; the English
brief v0.2 said nothing had been run, when stages 1 and 2 were running; the
portfolio card carried "13-code taxonomy" and "not yet implemented" in adjacent
paragraphs; the handbook contradicted itself across two sections.

None of those four documents is in the repository, which is why nothing flagged
them.

**Response.** `docs/claims.md` holds every fact asserted in more than one
document, with its current value. `pipeline/check_claims.py` checks the
repository documents against it: forbidden patterns that contradict current
values, and required patterns that must appear somewhere.

**It checks consistency, not correctness.** If a value in the register is wrong
and every document repeats it, the check passes.

### Calibration of the check, recorded because it is the cheapest instance

First run: six issues. Four were real stale claims, including "The 13-code
taxonomy" on line 12 of the protocol, a document edited the same day. Two were
instrument error:

- **False positive.** The pattern matched a line whose purpose was to *correct*
  the old count: "Documents describing it as five codes". Regex too broad; it
  did not distinguish mention from use. Fixed with a lookbehind.
- **False negative.** The required pattern for panel status was `not executed`.
  The text added to the README read "has not been **been** executed". The
  pattern was too narrow to match correct text. Fixed to `not (been )?executed`.

A false positive and a false negative in the same trivial instrument, within
fifteen minutes, against a reference standard of five lines.

**Consequence.** Calibrating a detector against a reference standard requires
iteration even when the detector is trivial and the standard is tiny. The
auditor has six codes and a planned panel of sixty cases. Budget for the same
process there, and expect the first pass to contain instrument error rather than
findings.

## 2026-09-13 — Not every claim is mechanically checkable

An attempt was made to add two entries to the claims register together with
matching patterns in the checker: the principal correspondence rule, and the C5
presentation policy.

The script aborted on its own guard: the closing bracket of the FORBIDDEN list
was no longer unambiguous, because that list had been edited twice by `sed`
earlier the same day. **A file edited automatically became fragile to automated
editing.** With fifteen entries, editing that list by script will be worse than
opening it.

**The substantive reason not to add the patterns.** The register holds discrete
values: 6, 60, v0.3. Each has a canonical string and is lexically verifiable.
The two new entries are rules stated in prose. They have no canonical form, and
the proposed patterns tried to match paraphrases of a wrong rule, which is
regex over meaning.

One proposed pattern would have been near-missed by correct text already in the
protocol: "Requiring a correct supporting reference as well would change it to
evidence-supported detection." It escapes only on "as well". That is the same
class of fragility that produced today's false positive, where the pattern
flagged the line written to correct the error.

The required patterns would have passed today because the author knew where the
sentences were. A later rewrite of "correct code plus unambiguous localisation"
into other words would raise an absence for a claim that is present.

**Resolution.** Both entries are in the register, followed by an explicit note
that they are not mechanically checked. The checker was left with the patterns
calibrated earlier today.

**The distinction, which only appeared by attempting it.** A claims register
serves two functions: a single source for a human to consult, and input to a
mechanical check. Only the second requires the value to be lexically verifiable.
Forcing prose into the second degrades the instrument, and an instrument that
raises false alarms is ignored within a few sessions.

## 2026-09-13 — An instrument outside its domain produces a plausible false finding

`check_table.py` approximates an effect by computing a risk ratio from per-arm
counts. Run against the PARAGON-HF evidence table, whose primary outcome is a
rate ratio for recurrent events estimated by negative binomial regression, it
produced:

    computed: RR 0.879 | CI 0.82-0.94 | p < 0.001
    declared: rate_ratio 0.87 | CI 0.75-1.01 | p 0.06

The point estimate nearly matches. The interval and the p value do not: computed
significance against declared non-significance.

**Why.** The approximation treats 894 and 1009 as independent patients with an
event. They are recurrent hospitalisations; the same patient contributes several
times. This inflates the effective sample size and narrows the interval. The
trial's model accounts for within-patient correlation, and its interval crosses
1.

**The failure mode is the dangerous one.** The output is internally consistent,
arithmetically correct, and wrong. A reader without the caveat would conclude
either that the publication is mistaken or that the table has a transcription
error. A false finding that looks like a discovery.

**Decision.** The script no longer computes anything when the declared effect
type is not a risk ratio. It prints the declared values and a line stating that
no number was computed. A printed number is a number someone will cite, and a
caveat beside it does not prevent that.

**Consequence for the project.** The same reasoning applies to the auditor.
Sensitivity and specificity reported on this panel describe detection of
injected errors of known type in this construction. Presenting them beside a
caveat does not stop them being read as performance in a regulatory setting.
Where a number cannot bear the reading it will receive, the question is whether
to report it at all, not how to caveat it.

## 2026-09-14 — The checker covers what someone remembered to list

Three documents fell out of date without anything flagging it. The four
external documents, because they are outside the repository. The claims
register, because the checker compares documents against it and never it
against reality. STATE.md, because it was not in the checker's DOCS list —
the file that had just become the single source of state was not being checked.

Each was a coverage gap, not a detection failure. The instrument works on what
it is pointed at.

**Consequence.** Adding a document to the project means adding it to DOCS.
Adding a value to the register means adding a pattern that can contradict it.
Neither happens automatically, and nothing signals the omission.

This is the same class of limitation the auditor will have: a taxonomy scores
what it enumerates. Codes not derived are errors not detected, and the panel
cannot reveal them.

## 2026-09-14 — The generator failed on the first case scored against a fuller ruler

Five consecutive runs produced no finding. The PARAGON-HF base summary, the
first scored under taxonomy v0.4 with the Annex V checklist, produced six:
O2, O3, O4, O5, O11 and C6.

**The generator did not get worse.** The earlier taxonomy had five commission
codes and one omission code, all concerned with fidelity to the evidence table.
It could not score completeness of a mandatory element, because no code existed
for one. As soon as codes existed for the ten Annex V elements, the first
summary scored against them failed.

**Consequence for the earlier observations.** The finding recorded as "with a
well-structured evidence table, generation was faithful" describes fidelity, not
compliance. Those five runs were never scored for mandatory-element
completeness; they may well contain the same omissions. They are development
cases and enter no denominator, so this is not an error in a reported result,
but the earlier entries should be read as bounded by the taxonomy in force at
the time.

**The general form.** A taxonomy scores what it enumerates. A clean result is
evidence about the instrument as much as about the object.

## 2026-09-20 — Density is not constructibility, and the error was made twice

The coverage matrix rated C3 "strong" in one trial only and concluded that its
cases would all derive from one base text, so a binomial interval over them
would describe one observation repeated. Counting the apparatus in the evidence
tables showed every trial carries at least one interval or p value: a C3 case
is constructible in all four.

The rating had measured density — how many places an error can be injected —
and the independence argument was built on it as though it measured
constructibility — whether a case can be built at all. Independence is bounded
by the second.

**While correcting this, the same conflation was made again for C6.**
Vortioxetine was described as unable to support C6 because per-term
frequencies had not been extracted. It carries overall adverse event incidence
by arm, and presenting that as a bare percentage is C6. Constructible; low
density.

Result: four independent base texts for every commission code except C5, which
has three. C5's shortfall is structural, not an extraction gap.

The conflation is easy enough to make twice in a row, in the same analysis,
while correcting it. Worth knowing before panel sizes are fixed per code.

## 2026-09-22 — Mention versus use, third occurrence, and a change of policy

check_claims flagged a line in STATE.md reading "auditor prompt v0.3 knows six
codes". The line mentions a superseded count in order to say the auditor is
stale; it does not assert that the taxonomy has six codes. Same distinction as
the first calibration false positive, on a line whose purpose was to correct
the old count.

The first occurrence was fixed by widening the pattern with a lookbehind. This
one was fixed by rewording the text instead.

**Reason for the change.** Each new mention would need another exception, and a
pattern accumulating exceptions becomes regex over meaning — the thing the
register already declines to do for prose claims. The forbidden patterns are
kept narrow and literal; where correct text collides with one, the text is
reworded.

**Cost.** Accepted: the register can no longer be used to write about its own
superseded values in the checked documents. Superseded counts are discussed in
findings.md, which is not checked.
