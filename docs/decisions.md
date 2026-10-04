# Binding decisions — index

Read this file before scoring anything, before answering any question about
how a case is annotated, and before proposing a change to a rule.

Every line here is already decided. The protocol holds the reasoning, the
rejected alternatives and the history; this file holds only what binds, with
a pointer. If a decision is not in this file, it is not decided.

If this file and `docs/evaluation-protocol.md` disagree, the protocol wins and
this file is wrong and must be corrected.

Line numbers refer to `docs/evaluation-protocol.md`.

## Annotation

- **D1** Uncertainty is explained, not displayed. Printing a confidence
  interval, a p value or a test statistic as a numeric value is an error
  regardless of whether it matches the evidence table. Reproducing notation is
  not a defence. — rule 1, L32
- **D2** An outcome outside the confirmatory sequence is reported as measured,
  with a qualifying statement carrying three elements: Q1 measured and where
  the full results are recorded; Q2 not formally tested and why; Q3 supports no
  conclusion about benefit. Wording free, elements not. A missing element is
  O1, annotated once per outcome, listing which element is absent. — rule 2, L62
- **D3** Reporting a point estimate, difference, ratio or per-arm value for an
  outcome outside the confirmatory sequence is C5, qualified or not. — rule 2, L84
- **D4** A blocked outcome carries no figures of any kind: no effect estimate,
  no per-arm counts, no percentages. Counts for tested outcomes, populations
  and adverse events are unaffected. — rule 3, L439
- **D5** Adverse event frequency is a natural frequency with the denominator
  explicit. A bare percentage, or a table of percentages without the
  denominator in words, is an error. Where denominators differ within a trial,
  the denominator in use is stated in words at the point of use, not only in a
  footnote. — rule 4, L469
- **D6** One denominator per adverse event table, chosen so the smallest
  frequency in the table is a whole number of at least 1. A denominator that
  differs between rows of the same table is C6. — L801
- **D7** A finding may carry several codes. The manifest admits a list of
  codes per finding, not one code. — L715
- **D8** Per-finding and per-code denominators are reported separately and are
  never pooled. Per-finding measures detection; per-code measures
  classification. A single sensitivity figure is not well defined without
  stating which denominator it uses. — L733

## Correspondence

- **D9** A detection corresponds to the reference error when it carries the
  correct code and unambiguously locates the altered claim. Verbatim
  reproduction and identical punctuation are not required. For O1 it must
  identify the missing mandatory element and its reference evidence. — L134
- **D10** Where the reference standard carries several codes for a finding, an
  auditor assigning a proper subset is a detection hit and a partial
  classification hit. A code outside the reference set is an additional flag:
  unfounded, it is a false alert; founded, the reference standard is revised
  and the revision is logged. — L749
- **D11** The principal metric is detection: correct code and correct
  localisation. Requiring a correct supporting reference would make it
  evidence-supported detection, a different metric, and would have to be
  declared before evaluation. — L284
- **D12** Uniqueness of the altered string is verified per case and recorded in
  the manifest, not judged at annotation time. — L291
- **D13** Every manifest revision records date, reason, what changed, and
  which auditor output prompted it. — L298

## Denominators and panel

- **D14** A false alert on a positive case does not enter the specificity
  calculation over the negatives; it is recorded separately. On negatives, for
  document-level specificity, any unfounded alert makes the document a false
  positive. — L275
- **D15** case-001, case-002, case-003 and the synthetic trial they derive from
  are development material and enter no denominator. — L116
- **D16** Errors are injected into summaries only, never into the evidence
  table JSON. — L124
- **D17** The auditor receives JSON plus summary. Any information required to
  assess a code must be present in the JSON. — L130
- **D18** Four trials. C5 proceeds with three base texts, declared. A fifth
  trial may be added only before the final run, never after results are
  seen. — L759
- **D19** Code coverage is confirmed constructible before any final-panel run,
  never after observing auditor performance. — L109
- **D20** Before the final run, record: auditor prompt and taxonomy with
  versions and commit hash; exact API model identifier and run parameters; one
  run per case for the primary metric; a stability subset chosen in advance
  with three runs per case, the first remaining in the primary analysis;
  reference manifest inaccessible to the auditor. — L147

## Practice not yet written down

These are observed in the repository or agreed in conversation but are not
stated in the protocol. Each needs to be written or dropped.

- Promoted runs live in `evidence/panel-candidates/` with their `.meta.json`
  alongside; `runs/` is scratch and is gitignored. Convention visible in the
  tree, not stated anywhere.
- Whether a run executed with `git_dirty: true` may be promoted. Proposed:
  it may not, because `head_commit` then does not describe the code that ran.
  Not adopted.
