# ZipRecruiter jobs scraper Python examples

Search US and Canada jobs with the hosted [ZipRecruiter Jobs Scraper](https://apify.com/datascraperes/ziprecruiter-jobs-scraper?fpr=edudata), or use its web form. This repository provides API integration examples and selected public sample data under MIT; it does not contain the hosted Actor implementation. Links to Apify include an affiliate referral parameter.

## What this repository helps you do

- Request jobs by keyword and location using Python, JavaScript or cURL.
- Combine keyword searches in one bounded run.
- Preserve partial results and export existing results to CSV.

## Example result

The [JSON sample](data/sample-output.json) and [CSV sample](data/sample-output.csv) are a selected-field projection of an observed public listing. Listings can expire.

```json
{
  "title": "Software Engineer - AI Trainer",
  "companyName": "DataAnnotation",
  "locationDisplay": "New York, NY, United States"
}
```

## Run without code

Open the [hosted Actor](https://apify.com/datascraperes/ziprecruiter-jobs-scraper?fpr=edudata), enter keywords, select usa or canada and optionally a city, then click Start. Inspect the Dataset and export JSON, CSV or Excel. Follow the [web guide](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify currently offers $5 in monthly prepaid usage, with no credit card required. Unused credits expire each cycle. This can cover small tests while credits remain; it is not unlimited free execution. Check [current platform pricing](https://apify.com/pricing?fpr=edudata).

## Quick start for developers

Use Python 3.11+; no third-party Python packages are required. Set APIFY_API_TOKEN in your shell; never commit its value.

```bash
export APIFY_API_TOKEN="your-token"
python examples/python/collect_jobs.py
```

PowerShell: `$env:APIFY_API_TOKEN = "your-token"`. The example starts one hosted run with a 300-second platform timeout, a client watchdog and a $0.01 Actor-event cap. Platform usage is separate. It saves available rows to ziprecruiter-jobs.json and returns exit code 2 when completeness cannot be verified. A lost start acknowledgement must be reconciled before another start.

## Input example

```json
{
  "keywords": [
    "software engineer"
  ],
  "country": "usa",
  "location": "New York, NY",
  "distanceMiles": 50,
  "maxItemsPerQuery": 3,
  "maxTotalItems": 3,
  "offset": 0,
  "datePostedHours": 0,
  "jobType": "any",
  "remoteOnly": false,
  "easyApplyOnly": false,
  "descriptionFormat": "markdown",
  "includeEmails": false
}
```

See the [input reference](docs/input-reference.md). Limits are ceilings, not promised counts.

## Request examples

- [Python single run](examples/python/collect_jobs.py)
- [Python keyword batch](examples/python/batch_searches.py)
- [Existing Dataset CSV export](examples/python/export_jobs_csv.py): `python examples/python/export_jobs_csv.py DATASET_ID`
- [cURL asynchronous request](examples/curl-request.md)
- [JavaScript / Node.js 20+](examples/javascript/request.mjs): `node examples/javascript/request.mjs`

## Output fields

| Field | Meaning |
| --- | --- |
| title, companyName | Job and employer |
| locationDisplay, isRemote | Available location and remote information |
| compensation | Source salary information, when available |
| jobUrl, directJobUrl | Listing and available application link |

See the [output reference](docs/output-reference.md) for the full contract. Optional fields can be empty.

## Common use cases

Recruiting research, job-board feeds and labor-market analysis. See [workflows](docs/use-cases.md); no exhaustive-market coverage is promised.

## Search several job keywords with Python

[batch_searches.py](examples/python/batch_searches.py) requests software engineer and data analyst in New York in one run, with three jobs per keyword and six overall. Change the city or country in the sample for your own supported searches.

## Export ZipRecruiter results to CSV without another collection

[export_jobs_csv.py](examples/python/export_jobs_csv.py) reads an existing Dataset, up to 1,000 rows, and escapes spreadsheet formula prefixes. It never starts a new collection. Set your Dataset ID from the original run, not a job URL.

## FAQ

Read the [FAQ](docs/faq.md) for empty fields, partial results and example exit codes.

## Limits and pricing

The hosted Actor uses pay-per-event billing for delivered jobs. Current equivalent prices per 1,000 jobs: FREE $1.00, Bronze $0.90, Silver $0.80, Gold/Platinum/Diamond $0.75. Empty searches do not create a job event. Platform usage follows your plan; check [live Actor pricing](https://apify.com/datascraperes/ziprecruiter-jobs-scraper?fpr=edudata) before larger work.

US and Canada only. At most 50 keywords, three search pages and 60 jobs per keyword, with a global ceiling of 3,000. Public availability, filters and source responses can reduce results. The examples deliberately request three or six jobs, not the full ceiling. They do not guarantee complete source coverage.

## Hosted version

[Open ZipRecruiter Jobs Scraper on Apify](https://apify.com/datascraperes/ziprecruiter-jobs-scraper?fpr=edudata) for the web interface, hosted API and stored results.

## Responsible use

Use public job data lawfully, respect applicable terms and privacy requirements, and keep API tokens private. This repository does not provide methods for bypassing access controls.

## Support

For example issues, use [GitHub Issues](https://github.com/datacrawler-edu/ziprecruiter-jobs-scraper-python/issues). For hosted execution issues, use [Actor support](https://apify.com/datascraperes/ziprecruiter-jobs-scraper?fpr=edudata) and include the run ID with sanitized input. Never share credentials.

## License

MIT applies to the integration examples; see [LICENSE](LICENSE). Source job content retains its original rights.
