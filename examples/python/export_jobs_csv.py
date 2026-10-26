"""Export up to 1,000 existing Dataset rows without starting a collection."""
import argparse
import csv
from client import iter_items

FIELDS = ['jobId', 'title', 'companyName', 'locationDisplay', 'isRemote', 'jobUrl']


def cell(value):
    text = "" if value is None else str(value)
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("--output", default="ziprecruiter-jobs.csv")
    args = parser.parse_args()
    count = 0
    with open(args.output, "w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        for item in iter_items(args.dataset_id, maximum=1000):
            writer.writerow({key: cell(item.get(key)) for key in FIELDS})
            count += 1
    print(f"Exported {count} existing rows (maximum 1,000); completeness is not inferred.")
