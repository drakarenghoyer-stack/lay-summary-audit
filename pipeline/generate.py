import json
import pathlib
from dotenv import load_dotenv
from anthropic import Anthropic

MODEL = "claude-sonnet-5"
TABLE = "examples/evidence-table-paragon-hf.json"
PROMPT = "prompts/generator.md"
OUT = "runs/lay-summary-paragon-hf.md"

load_dotenv()
client = Anthropic()

table = json.loads(pathlib.Path(TABLE).read_text())
instructions = pathlib.Path(PROMPT).read_text()

response = client.messages.create(
    model=MODEL,
    max_tokens=2000,
    system=instructions,
    messages=[
        {"role": "user", "content": json.dumps(table, indent=2)}
    ],
)

blocks = [b for b in response.content if b.type == "text"]
if not blocks:
    raise SystemExit("No text block in response")
summary = "\n".join(b.text for b in blocks)

pathlib.Path("runs").mkdir(exist_ok=True)
pathlib.Path(OUT).write_text(summary)

import hashlib, subprocess, datetime
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
    "max_tokens": 2000,
    "run_timestamp": datetime.datetime.now().strftime("%Y%m%dT%H%M%S"),
    "tokens_in": response.usage.input_tokens,
    "tokens_out": response.usage.output_tokens,
}
import json as _json
pathlib.Path(OUT.replace(".md", ".meta.json")).write_text(_json.dumps(meta, indent=2))
print("meta:", OUT.replace(".md", ".meta.json"))

print(summary)
print("\n---")
print("model:", response.model)
print("tokens in/out:", response.usage.input_tokens, response.usage.output_tokens)
print("saved to:", OUT)
