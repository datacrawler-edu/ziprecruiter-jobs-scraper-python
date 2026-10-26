"""One bounded run with two keyword searches in the same city."""
import json
from pathlib import Path
from client import collect

if __name__ == "__main__":
    payload = json.loads((Path(__file__).resolve().parents[2] / "data/sample-input.json").read_text())
    payload.update(keywords=["software engineer", "data analyst"], maxItemsPerQuery=3, maxTotalItems=6)
    items, complete = collect(payload)
    Path("ziprecruiter-batch.json").write_text(json.dumps(items, indent=2), encoding="utf-8")
    print(f"Saved {len(items)} available jobs; complete within requested limits: {complete}")
    raise SystemExit(0 if complete else 2)
