"""Stage 1 — generate a lay summary from an evidence table.

    python3 pipeline/generate.py <evidence-table.json>

The output file name is derived from the table name and carries a timestamp,
so repeated runs on the same trial never overwrite each other. Each run writes
a .meta.json beside the summary with the prompt hash, the table hash, the HEAD
commit and the working tree state at execution time.
"""

import json
import pathlib
import sys
import hashlib
import subprocess
import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

MODEL = "claude-sonnet-5"
MAX_TOKENS = 8000
PROMPT = "prompts/generator.md"

if len(sys.argv) < 2:
    raise SystemExit("usage: generate.py <evidence-table.json>")
TABLE = sys.argv[1]

# evidence-table-select.json -> select
stem = pathlib.Path(TABLE).stem
slug = stem.replace("evidence-table-", "")
STAMP = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
OUT = f"runs/lay-summary-{slug}-{STAMP}.md"

load_dotenv()
client = Anthropic()

table = json.loads(pathlib.Path(TABLE).read_text())
instructions = pathlib.Path(PROMPT).read_text()

response = client.messages.create(
    model=MODEL,
    max_tokens=MAX_TOKENS,
    system=instructions,
    messages=[
        {"role": "user", "content": json.dumps(table, indent=2)}
    ],
)

blocks = [b for b in response.content if b.type == "text"]
if not blocks:
    raise SystemExit("No text block in response")
summary = "\n".join(b.text for b in blocks)

truncated = response.stop_reason == "max_tokens"

pathlib.Path("runs").mkdir(exist_ok=True)
pathlib.Path(OUT).write_text(summary)

meta = {
    "output_file": OUT,
    "table_file": TABLE,
    "prompt_file": PROMPT,
    "prompt_sha256": hashlib.sha256(instructions.encode()).hexdigest(),
    "table_sha256": hashlib.sha256(pathlib.Path(TABLE).read_bytes()).hexdigest(),
    "head_commit": subprocess.run(["git", "rev-parse", "HEAD"],
                                  capture_output=True, text=True).stdout.strip() or "unknown",
    "git_dirty": bool(subprocess.run(["git", "status", "--porcelain"],
                                     capture_output=True, text=True).stdout.strip()),
    "model_requested": MODEL,
    "model_returned": response.model,
    "max_tokens": MAX_TOKENS,
    "stop_reason": response.stop_reason,
    "truncated": truncated,
    "run_timestamp": STAMP,
    "tokens_in": response.usage.input_tokens,
    "tokens_out": response.usage.output_tokens,
}
pathlib.Path(OUT.replace(".md", ".meta.json")).write_text(json.dumps(meta, indent=2))

print(summary)
print("\n---")
print("model:", response.model)
print("tokens in/out:", response.usage.input_tokens, response.usage.output_tokens)
print("stop_reason:", response.stop_reason)
print("saved to:", OUT)
print("meta:", OUT.replace(".md", ".meta.json"))

if truncated:
    print()
    print("*** TRUNCATED: the response hit max_tokens and the summary is cut off.")
    print("*** Do not use this output. Raise MAX_TOKENS and run again.")
    raise SystemExit(1)
