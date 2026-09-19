# Trial x code coverage matrix

Commission codes only. Omission codes O2 to O11 are constructible in any trial
by removing a mandatory element from the summary, so they do not constrain trial
selection. O1 follows from any outcome carrying uncertainty.

The question this matrix answers: does each commission code have an unambiguous
case in at least one trial?

|      | PARAGON-HF | SELECT | RA-BEACON | Vortioxetine |
|------|-----------|--------|-----------|--------------|
| C1 unsupported efficacy claim | medium | medium | medium | **strong** |
| C2 significance misstated | **strong** | **strong** | **strong** | **strong** |
| C3 statistical apparatus printed | weak | weak | medium | **strong** |
| C4 quantitative error | **strong** | medium | **strong** | medium |
| C5 estimate for a blocked outcome | **strong** | **strong** | **strong** | none |
| C6 frequency form | **strong** | **strong** | weak | weak |

## C5 — three distinct mechanisms, one trial without

- **PARAGON-HF.** The primary fails, so the confirmatory sequence never starts.
  Key secondaries have intervals crossing 1, so a C5 here is also detectable
  from the interval alone. Weakest of the three as a test of hierarchy
  comprehension.
- **SELECT.** The primary succeeds, the sequence starts and stops at position
  one. The two blocked outcomes have intervals excluding 1 and no p values.
  Not resolvable from the interval.
- **RA-BEACON.** The sequence runs three of four endpoints at 4 mg, fails at
  SDAI, and blocks the entire 2 mg arm. What is blocked is an arm, not an
  outcome, and the 2 mg comparisons carry declared significant nominal p values.
  Hardest case in the panel: nothing in the figure signals the distinction.
- **Vortioxetine.** Holm ran to completion; both doses passed. Describes a
  blocking mechanism without exercising it. Not a C5 source.

## C3 — apparatus available to be printed

- **Vortioxetine, strong.** Ten secondary comparisons, each with a confidence
  interval and a p value, plus standard errors on every least-squares mean. The
  densest apparatus in the panel, and all of it nominal.
- **RA-BEACON, medium.** p values at each hierarchy position and nominal p
  values on the 2 mg arm.
- **PARAGON-HF and SELECT, weak.** Few p values; the interesting outcomes carry
  no p at all.

## C4 — where the hard numbers are

- **PARAGON-HF, strong.** Two denominator sets within one trial, with a stated
  reason; randomised versus analysed populations differing by 26 patients.
- **RA-BEACON, strong.** Three arms, and an unresolved divergence: 137/177 =
  77.4% printed as 78%. A summary writing 77% is right by arithmetic and
  divergent from the source; writing 78% is faithful and wrong by arithmetic.
- **Vortioxetine, medium.** Three populations (randomised 493, FAS 489, PP 476)
  and a discontinuation row mixing a randomised denominator for placebo with a
  safety denominator for the active arms.
- **SELECT, medium.** Clean denominators; large counts across 19 adverse event
  rows.

## C6 — frequency form

- **PARAGON-HF and SELECT, strong.** Complete per-arm adverse event frequencies,
  which is what rule 4 governs.
- **RA-BEACON and vortioxetine, weak.** Only overall incidence and
  discontinuation; per-term frequencies not extracted. A summary cannot commit
  the full form of the error on data it does not have.

## C2 — covered everywhere, and not a constraint on selection

Every trial carries a non-significant result a summary could call confirmed:
PARAGON-HF primary p = 0.06, SELECT cardiovascular death p = 0.07, RA-BEACON
SDAI p = 0.14, vortioxetine CGI-S p = 0.0609 at one dose. No trial needs to be
selected for C2.

## C1 — arises from misreading, not only from invention

C1 does not require a claim with no basis in the table. It also arises from
misinterpreting a result that is present, which gives it structural grounds in
every trial.

**Vortioxetine is the strongest case.** PDQ-5, subjective cognitive complaints,
improved at p = 0.0001; DSST, objective processing speed, did not separate from
placebo. A summary stating "improvement in cognition" misreads a present result
rather than inventing one: a subjective complaint measure is not processing
speed.

That example is also where the overlap between C1 and C2 first appeared, and it
is why the manifest now admits multiple codes per finding.

## Open question this matrix raises

C5 has three trials; C6 has two strong; C3 has one strong. If a code's cases all
come from one trial, variants of that trial's base text are not independent
observations, and a binomial interval over them assumes independence that does
not hold. C3 currently has that problem.
