import json
import pathlib
from dotenv import load_dotenv
from anthropic import Anthropic

MODEL = "claude-sonnet-5"
TABLE = "examples/evidence-table-commission.json"
PROMPT = "prompts/generator.md"
OUT = "runs/lay-summary-commission.md"

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

summary = response.content[0].text

pathlib.Path("runs").mkdir(exist_ok=True)
pathlib.Path(OUT).write_text(summary)

print(summary)
print("\n---")
print("model:", response.model)
print("tokens in/out:", response.usage.input_tokens, response.usage.output_tokens)
print("saved to:", OUT)
