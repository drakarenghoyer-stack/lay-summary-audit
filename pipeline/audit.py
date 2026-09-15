import json
import pathlib
import sys
from dotenv import load_dotenv
from anthropic import Anthropic

MODEL = "claude-sonnet-5"
if len(sys.argv) < 3:
    raise SystemExit("usage: audit.py <summary.md> <evidence-table.json>")
TABLE = sys.argv[2]
SUMMARY = sys.argv[1]
PROMPT = "prompts/auditor.md"
STAMP = __import__("datetime").datetime.now().strftime("%Y%m%dT%H%M%S")
OUT = "runs/audit-" + pathlib.Path(sys.argv[1]).stem + "-" + STAMP + ".json"

print("=== " + SUMMARY + " ===")
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
CODES = {"C1", "C2", "C3", "C4", "C5", "O1"}
problems = []
if not isinstance(findings, dict) or "findings" not in findings:
    problems.append("response is not an object with a 'findings' key")
else:
    for i, f in enumerate(findings.get("findings", [])):
        if not isinstance(f, dict):
            problems.append(f"finding {i} is not an object")
            continue
        if f.get("code") not in CODES:
            problems.append(f"finding {i}: unknown code {f.get('code')!r}")
        for k in ("quote", "explanation"):
            if not f.get(k):
                problems.append(f"finding {i}: missing {k}")

record = {
    "summary_file": SUMMARY,
    "table_file": TABLE,
    "prompt_file": PROMPT,
    "prompt_sha256": __import__("hashlib").sha256(instructions.encode()).hexdigest(),
    "head_commit": __import__("subprocess").run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True
    ).stdout.strip() or "unknown",
    "git_dirty": bool(__import__("subprocess").run(
        ["git", "status", "--porcelain"], capture_output=True, text=True
    ).stdout.strip()),
    "model_requested": MODEL,
    "model_returned": response.model,
    "max_tokens": 4000,
    "run_timestamp": STAMP,
    "tokens_in": response.usage.input_tokens,
    "tokens_out": response.usage.output_tokens,
    "schema_problems": problems,
    "raw": raw,
    "parsed": findings,
}
pathlib.Path(OUT).write_text(json.dumps(record, indent=2))
if problems:
    print("SCHEMA PROBLEMS:")
    for pr in problems:
        print("  " + pr)


for f in findings.get("findings", []):
    print(f"[{f.get('code')}] {f.get('explanation')}")
    print(f"    quote: {f.get('quote')}")
    print()

print("---")
print("findings:", len(findings.get("findings", [])))
print("tokens in/out:", response.usage.input_tokens, response.usage.output_tokens)
print("saved to:", OUT)
