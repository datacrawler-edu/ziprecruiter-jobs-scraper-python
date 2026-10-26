# Workflows

- Recruiting research: search a role and city, then review job and company links.
- Compare role keywords: batch_searches.py submits two terms in one bounded run. Jobs can appear in more than one query; deduplication follows Actor identity rules.
- Spreadsheet updates: export_jobs_csv.py reads up to 1,000 existing rows. It does not recollect data or infer that the source has only that many jobs.
- Salary research: compare compensation only where provided; do not infer missing pay or normalize different intervals without checking compensation metadata.
