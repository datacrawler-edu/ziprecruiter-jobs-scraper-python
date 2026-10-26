"""Collect the three-job sample and retain any available partial output."""
import json
from pathlib import Path
from client import collect

if __name__ == "__main__":
    payload = json.loads((Path(__file__).resolve().parents[2] / "data/sample-input.json").read_text(encoding="utf-8"))
    items, complete = collect(payload)
    Path("ziprecruiter-jobs.json").write_text(json.dumps(items, indent=2), encoding="utf-8")
    print(f"Saved {len(items)} jobs. Complete within requested limits: {complete}")
    raise SystemExit(0 if complete else 2)
