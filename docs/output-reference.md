# Output reference

One Dataset row represents a job. Optional information can be null or absent. The sample is a selected-field projection of an observed public listing, not a current vacancy guarantee.

| Field | Meaning |
| --- | --- |
| `success` | Success |
| `status` | Status |
| `source` | Source |
| `searchKeyword` | Search keyword |
| `searchCountry` | Country |
| `searchLocation` | Search location |
| `jobId` | ZipRecruiter job ID |
| `jobUrl` | ZipRecruiter job URL |
| `directJobUrl` | Direct application URL |
| `title` | Job title |
| `companyName` | Company |
| `companyUrl` | Company URL |
| `companyDirectUrl` | Company website |
| `location` | Location |
| `locationDisplay` | Displayed location |
| `isRemote` | Remote |
| `jobTypes` | Job types |
| `postedDate` | Posted date |
| `description` | Description |
| `emails` | Public emails |
| `compensation` | Compensation |
| `companyIndustry` | Company industry |
| `companyAddresses` | Company addresses |
| `companyEmployees` | Company employees |
| `companyRevenue` | Company revenue |
| `companyDescription` | Company description |
| `companyLogoUrl` | Company logo |
| `scrapedAt` | Scraped at |

Completion is determined by the terminal run status and SUMMARY.status/outputItems, not the presence of rows alone. Partial output can still contain useful jobs.
