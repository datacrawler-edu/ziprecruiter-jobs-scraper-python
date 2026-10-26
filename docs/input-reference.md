# Input reference

`keywords` and `country` are required. Use usa or canada. The sample sets all 13 supported inputs.

| Field | Type | Meaning |
| --- | --- | --- |
| `keywords` | array | One job search phrase per item. Duplicate phrases are removed before the run. |
| `country` | string | Country used by ZipRecruiter. The public ZipRecruiter search endpoint supports the United States and Canada. |
| `location` | string | City, state, province, postal code, or other location text understood by ZipRecruiter. Leave empty for a country-wide search. |
| `distanceMiles` | integer | Distance around the location. Use 50 miles for a broad search. Range: 1 to 100 miles. |
| `maxItemsPerQuery` | integer | Maximum unique jobs collected for each keyword, up to 60 (three public result pages). This is a limit, not a guarantee of available matches. |
| `maxTotalItems` | integer | Global output limit across all keywords, up to 3,000 (50 keywords x 60). Use this to control the maximum Dataset size and spend. |
| `offset` | integer | Skip this many results for every keyword. Offset plus maxItemsPerQuery cannot exceed 60. |
| `datePostedHours` | integer | Return jobs published within this many hours. Use 0 for any age. |
| `jobType` | string | Optional ZipRecruiter employment-type filter. |
| `remoteOnly` | boolean | Return listings identified by ZipRecruiter as remote. |
| `easyApplyOnly` | boolean | Return only listings with an internal ZipApply flow. Applied locally after search; may reduce the number of returned jobs. |
| `descriptionFormat` | string | Format of the public job description in each Dataset item. |
| `includeEmails` | boolean | Extract email addresses found in public job descriptions. Disabled by default. |

Prefill is a suggested example, not a runtime default. Misspellings may yield no results or source-dependent matches; validate your keyword and location before larger runs.
