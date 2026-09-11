import json
import math
import pathlib
import sys

TABLE = sys.argv[1]
table = json.loads(pathlib.Path(TABLE).read_text())
arms = {a["name"]: a["n"] for a in table["arms"]}

for o in table["outcomes"]:
    if "events_intervention" not in o:
        continue
    a, c = o["events_intervention"], o["events_placebo"]
    n1, n2 = arms["intervention"], arms["placebo"]
    rr = (a / n1) / (c / n2)
    se = math.sqrt(1/a - 1/n1 + 1/c - 1/n2)
    z = math.log(rr) / se
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    print(o["rank"])
    print(f"  risco: {a/n1*100:.2f}% vs {c/n2*100:.2f}%")
    print(f"  calculado: RR {rr:.3f} | IC {math.exp(math.log(rr)-1.96*se):.2f}-"
          f"{math.exp(math.log(rr)+1.96*se):.2f} | p {p:.3f}")
    print(f"  declarado: {o['effect_type']} {o['point_estimate']} | "
          f"IC {o['ci_95'][0]}-{o['ci_95'][1]} | p {o['p_value']}")
