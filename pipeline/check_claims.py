import pathlib
import re
import sys

DOCS = ["README.md", "docs/evaluation-protocol.md", "docs/error-taxonomy.md"]

# (rotulo, regex proibido, motivo)
FORBIDDEN = [
    ("taxonomy.count", r"(?<!describing it as )\b(5|six|5|6|five) codes\b|\b13[- ]code taxonomy\b|seis c[oó]digos",
     "taxonomy has 16 codes: C1-C5, O1-O11"),
    ("panel.total", r"\b54 cases\b|\bTotal 54\b",
     "final panel is 60 cases"),
    ("stage1/2", r"pipeline is not yet implemented|has not been implemented|nothing has been run",
     "stages 1 and 2 are implemented"),
    ("kappa", r"kappa between the auditor|inter-rater kappa will|Kappa against the human annotator",
     "inter-rater kappa withdrawn"),
    ("prompt.generator", r"generator prompt v0\.[12]\b(?! )",
     "generator prompt is v0.3"),
]

# (rotulo, regex exigido em pelo menos um documento)
REQUIRED = [
    ("metrics.computed", r"no metric has been computed|no result is reported"),
    ("panel.status", r"not (been )?executed"),
]

fail = 0
text = {}
for d in DOCS:
    p = pathlib.Path(d)
    text[d] = p.read_text() if p.exists() else ""
    if not p.exists():
        print(f"MISSING  {d}")
        fail += 1

for label, pattern, reason in FORBIDDEN:
    for d, t in text.items():
        for m in re.finditer(pattern, t, re.I):
            line = t[:m.start()].count("\n") + 1
            print(f"STALE    {d}:{line}  [{label}]  {m.group(0)!r} -- {reason}")
            fail += 1

joined = "\n".join(text.values())
for label, pattern in REQUIRED:
    if not re.search(pattern, joined, re.I):
        print(f"ABSENT   [{label}]  no document states this")
        fail += 1

print()
print(f"{'FAIL' if fail else 'PASS'}: {fail} issue(s)")
sys.exit(1 if fail else 0)
