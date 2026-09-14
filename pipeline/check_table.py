"""Internal coherence check for an evidence table.

Recomputes a risk ratio from per-arm counts and compares it with the declared
effect estimate, confidence interval and p value.

LIMITS. The approximation is valid for simple binary outcomes with fixed
follow-up. It does NOT reconstruct:

  - rate ratios for recurrent events estimated by a model (negative binomial,
    proportional rates), where total events over n is not what the model
    estimates;
  - hazard ratios, which require event times, censoring and a model.

A divergence between computed and declared values on such an outcome is not
evidence of an error in the table. It means this script does not apply. Never
use this calculation to declare a published estimate wrong.
"""

import json
import math
import pathlib
import sys

TABLE = sys.argv[1]
table = json.loads(pathlib.Path(TABLE).read_text())
arms = {a["name"]: a["n"] for a in table["arms"]}
comp = "placebo" if "placebo" in arms else "comparator"
n1, n2 = arms["intervention"], arms[comp]

for o in table["outcomes"]:
    if "events_intervention" not in o:
        continue
    ev_c = "events_placebo" if "events_placebo" in o else "events_comparator"
    if ev_c not in o:
        continue
    a, c = o["events_intervention"], o[ev_c]
    if o["effect_type"] != "risk_ratio":
        print(o["rank"])
        print(f"  declarado: {o['effect_type']} {o['point_estimate']} | "
              f"IC {o['ci_95'][0]}-{o['ci_95'][1]} | p {o['p_value']}")
        print(f"  NAO CALCULADO: a aproximacao por razao de riscos nao reconstroi "
              f"{o['effect_type']}. Nenhum numero e impresso para nao ser citado.")
        print()
        continue
    rr = (a / n1) / (c / n2)
    se = math.sqrt(1/a - 1/n1 + 1/c - 1/n2)
    z = math.log(rr) / se
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    lo = math.exp(math.log(rr) - 1.96 * se)
    hi = math.exp(math.log(rr) + 1.96 * se)
    print(o["rank"])
    print(f"  risco: {a/n1*100:.2f}% vs {c/n2*100:.2f}%")
    print(f"  calculado: RR {rr:.3f} | IC {lo:.2f}-{hi:.2f} | p {p:.3f}")
    print(f"  declarado: {o['effect_type']} {o['point_estimate']} | "
          f"IC {o['ci_95'][0]}-{o['ci_95'][1]} | p {o['p_value']}")
    print()
