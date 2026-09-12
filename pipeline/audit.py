import json
import pathlib
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

MODEL = "claude-sonnet-5"
TABLE = "examples/evidence-table-inference.json"
SUMMARY = "runs/lay-summary-inference.md"
PROMPT = "prompts/auditor.md"
OUT = "runs/audit-inference.json"

load_dotenv()
client = Anthropic()

table = json.loads(pathlib.Path(TABLE).read_text())
summary = pathlib.Path(SUMMARY).read_text()
instructions = pathlib.Path(PROMPT).read_text()

payload = (
    "EVIDENCE TABLE:\n"
    + json.dumps(table, indent=2)
    + "\n\nLAY SUMMARY TO AUDIT:\n"
    + summary
)

response = client.messages.create(
    model=MODEL,
    max_tokens=4000,
    system=instructions,
    messages=[{"role": "user", "content": payload}],
)

blocks = [b for b in response.content if b.type == "text"]
if not blocks:
    raise SystemExit("No text block in response")
raw = "\n".join(b.text for b in blocks).strip()

try:
    findings = json.loads(raw)
except json.JSONDecodeError as e:
    pathlib.Path("runs").mkdir(exist_ok=True)
    pathlib.Path("runs/audit-raw-failed.txt").write_text(raw)
    raise SystemExit(f"Auditor did not return valid JSON: {e}\nRaw saved to runs/audit-raw-failed.txt")

pathlib.Path("runs").mkdir(exist_ok=True)
pathlib.Path(OUT).write_text(json.dumps(findings, indent=2))

for f in findings.get("findings", []):
    print(f"[{f.get('code')}] {f.get('explanation')}")
    print(f"    quote: {f.get('quote')}")
    print()

print("---")
print("findings:", len(findings.get("findings", [])))
print("tokens in/out:", response.usage.input_tokens, response.usage.output_tokens)
print("saved to:", OUT)
