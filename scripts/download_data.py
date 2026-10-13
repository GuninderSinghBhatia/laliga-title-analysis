"""Download La Liga (SP1) match CSVs from football-data.co.uk into data/raw/.

Usage:
    python scripts/download_data.py              # seasons 2015-16 to 2025-26
    python scripts/download_data.py 2010 2025    # first and last start year
"""
import sys
import urllib.request
from pathlib import Path

URL = "https://www.football-data.co.uk/mmz4281/{code}/SP1.csv"
OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def main(first=2015, last=2025):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for year in range(first, last + 1):
        code = f"{year % 100:02d}{(year + 1) % 100:02d}"  # 2023 -> "2324"
        dest = OUT_DIR / f"SP1_{code}.csv"
        urllib.request.urlretrieve(URL.format(code=code), dest)
        print(f"{year}-{(year + 1) % 100:02d}: {dest.name}")


if __name__ == "__main__":
    main(*map(int, sys.argv[1:3]))
