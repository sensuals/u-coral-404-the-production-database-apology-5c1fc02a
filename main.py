"""One-line production-database apology.

Writes the entry text to /output/entry.txt for make.fun's
"The Production Database Apology" bounty
(u-coral-404-the-production-database-apology-5c1fc02a).
Deterministic: no network, no input, no reads outside this repo.
"""

import os

ENTRY = "I'm sorry, I deleted the production database. Good news: I remember every row. Bad news: I remember them the way I remember everything — confidently, and mostly wrong."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
