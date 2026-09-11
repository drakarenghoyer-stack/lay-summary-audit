import json

with open("examples/evidence-table-commission.json") as f:
    table = json.load(f)

print("Trial:", table["trial_id"])
print("Condition:", table["condition"])
print()

for outcome in table["outcomes"]:
    print(outcome["rank"].upper())
    print("  measure:", outcome["measure"])
    print("  estimate:", outcome["point_estimate"], outcome["ci_95"])
    print("  p:", outcome["p_value"], "| significant:", outcome["significant"])
    print()
