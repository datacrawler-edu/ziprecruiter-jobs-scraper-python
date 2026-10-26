"""REST integration for the hosted Actor; no collection implementation."""
import json
import os
import time
import urllib.request
from urllib.error import HTTPError

BASE = "https://api.apify.com/v2"
TERMINAL = {"SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"}


def api(path, payload=None):
    if not os.environ.get("APIFY_API_TOKEN"):
        raise RuntimeError("Set APIFY_API_TOKEN before using the API examples.")
    body = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(BASE + path, data=body, headers={
        "Authorization": "Bearer " + os.environ["APIFY_API_TOKEN"],
        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Apify API returned HTTP {exc.code}") from None


def iter_items(dataset_id, maximum=1000):
    """Read existing rows only; never start a collection."""
    if not dataset_id or not dataset_id.isalnum():
        raise ValueError("Supply the Dataset ID from your Apify run.")
    offset = 0
    while offset < maximum:
        page = api(f"/datasets/{dataset_id}/items?clean=true&offset={offset}&limit={min(100, maximum-offset)}")
        if not page:
            break
        yield from page
        offset += len(page)


def collect(payload):
    # Never automatically replay a start request with an uncertain acknowledgement.
    run = api("/acts/datascraperes~ziprecruiter-jobs-scraper/runs?build=latest&timeout=300&maxTotalChargeUsd=0.01", payload)["data"]
    print("Run ID:", run["id"], flush=True)
    deadline = time.monotonic() + 260
    while run["status"] not in TERMINAL:
        if time.monotonic() >= deadline:
            api(f"/actor-runs/{run['id']}/abort", {})
            raise RuntimeError("Watchdog requested abort; inspect the run before retrying.")
        time.sleep(2)
        run = api(f"/actor-runs/{run['id']}")["data"]
    items = list(iter_items(run["defaultDatasetId"], payload.get("maxTotalItems", 3))) if run.get("defaultDatasetId") else []
    summary = None
    try:
        summary = api(f"/key-value-stores/{run['defaultKeyValueStoreId']}/records/SUMMARY")
    except (RuntimeError, KeyError):
        pass
    complete = (run["status"] == "SUCCEEDED" and isinstance(summary, dict)
                and summary.get("status") in {"success", "empty"} and summary.get("outputItems") == len(items))
    print(json.dumps({"runId": run["id"], "status": run["status"], "complete": complete,
                      "datasetId": run.get("defaultDatasetId"), "summaryAvailable": summary is not None,
                      "summaryStatus": summary.get("status") if isinstance(summary, dict) else None}, indent=2))
    return items, complete
