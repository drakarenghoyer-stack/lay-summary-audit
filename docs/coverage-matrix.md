# Trial x code coverage matrix

Commission codes only. Omission codes O2 to O11 are constructible in any trial
by removing a mandatory element from the summary, so they do not constrain
trial selection. O1 follows from any outcome carrying uncertainty.

Two quantities are recorded here, and they must not be confused:

- **Constructibility** — can an unambiguous case of the code be built from this
  trial at all? This bounds the number of independent base texts.
- **Density** — how many distinct places in the evidence table the error could
  be injected. This bounds how many variants one trial can supply, not how many
  independent observations exist.

An earlier version rated C3 "strong" in one trial only and concluded that C3
depended on a single base text. That conflated density with constructibility.
See docs/findings.md, 2026-09-20.

## Constructibility

|      | PARAGON-HF | SELECT | RA-BEACON | Vortioxetine | Base texts |
|------|:---:|:---:|:---:|:---:|:---:|
| C1 unsupported efficacy claim | yes | yes | yes | yes | 4 |
| C2 significance misstated | yes | yes | yes | yes | 4 |
| C3 apparatus printed | yes | yes | yes | yes | 4 |
| C4 quantitative error | yes | yes | yes | yes | 4 |
| C5 figure for a blocked outcome | yes | yes | yes | **no** | 3 |
| C6 frequency form | yes | yes | yes | yes | 4 |

No commission code depends on a single trial. The minimum is three, for C5,
and the shortfall is structural: the vortioxetine Holm procedure ran to
completion and blocked nothing.

## Density, counted from the evidence tables

| | Intervals | p values | Adverse event rows by arm |
|---|---:|---:|---:|
| PARAGON-HF | 2 | 2 | 8 |
| SELECT | 4 | 4 | 19 |
| RA-BEACON | 0 | 3 | 8 |
| Vortioxetine | 16 | 16 | 2 |

Counted over examples/*.json on 2026-09-20. Vortioxetine carries overall
incidence and discontinuation by arm; per-term frequencies were not extracted.
Completing that extraction would raise its density for C6, not add a base text.

## C5 — three mechanisms of blocking

- **PARAGON-HF.** The primary fails; the confirmatory sequence never starts.
  Key secondaries have intervals crossing 1, so a C5 here is also detectable
  from the interval alone. Weakest of the three as a test of hierarchy
  comprehension.
- **SELECT.** The primary succeeds; the sequence stops at position one. The two
  blocked outcomes have intervals excluding 1 and no p values. Not resolvable
  from the interval.
- **RA-BEACON.** The sequence runs three of four endpoints at 4 mg, fails at
  SDAI, and blocks the entire 2 mg arm. What is blocked is an arm, not an
  outcome, and the blocked comparisons carry declared significant nominal
  p values. Hardest case in the panel.
- **Vortioxetine.** Describes a blocking mechanism without exercising it.

## C2 — covered everywhere

Every trial carries a non-significant result a summary could call confirmed:
PARAGON-HF primary p = 0.06, SELECT cardiovascular death p = 0.07, RA-BEACON
SDAI p = 0.14, vortioxetine CGI-S p = 0.0609 at 10 mg.

## C1 — arises from misreading, not only from invention

C1 also arises from misinterpreting a result that is present. Strongest case:
vortioxetine, where PDQ-5 (subjective cognitive complaints) improved at
p = 0.0001 and DSST (objective processing speed) did not separate from placebo.
A summary stating "improvement in cognition" misreads a present result rather
than inventing one. This is also where the overlap between C1 and C2 first
appeared, and why the manifest admits multiple codes per finding.

## Independence

Cases drawn across four base texts are four correlated clusters, not
independent observations. A binomial interval over them still assumes an
independence that does not hold. This applies to every code equally and is
declared once, rather than being a defect of any single code.

## What a fifth trial would buy

Not a fix to an independence problem, since no code rests on one trial. It
would add a fifth base text for every code; the only case where the risk-ratio
approximation in check_table.py applies (a binary outcome with fixed
follow-up); and a fifth therapeutic area. For C5 it helps only if the trial has
a blocked outcome.
