# Start one bounded collection

Set APIFY_API_TOKEN in your shell, then run from the repository root:

```bash
curl --fail-with-body --max-time 40 -X POST \
  'https://api.apify.com/v2/acts/datascraperes~ziprecruiter-jobs-scraper/runs?build=latest&timeout=300&maxTotalChargeUsd=0.01' \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' --data-binary @data/sample-input.json
```

This starts a run asynchronously and returns its ID. GET /v2/actor-runs/RUN_ID until a terminal status, then read /v2/datasets/DATASET_ID/items. Use the defaultDatasetId in that run. Inspect SUMMARY in its defaultKeyValueStoreId before treating the collection as complete. A client timeout does not stop the run; the platform timeout remains 300 seconds. Do not blindly repeat a start request if its response was lost. The $0.01 limit concerns Actor charge events; other platform charges follow your plan.
