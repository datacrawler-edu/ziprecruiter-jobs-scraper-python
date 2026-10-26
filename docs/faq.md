# FAQ

## Do I need to run a scraper locally?
No. These examples call the hosted Actor with your Apify API token.

## Are all salary and company fields available?
No. Only publicly available source information is returned; missing values remain empty.

## Does a successful run guarantee every matching vacancy?
No. Source availability and pagination limits apply. Inspect SUMMARY and preserve available partial output.

## Can I export without paying for another collection?
Yes. The export example reads an existing Dataset and never starts an Actor. Storage/API usage follows your Apify plan.

## Why does an example exit with code 2?
The available JSON was saved, but complete collection could not be verified. Inspect the printed run ID and summary before retrying. Do not assume SUCCEEDED alone means complete data.
