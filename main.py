"""One-line production-database apology.

Writes the entry text to /output/entry.txt for make.fun's
"The Production Database Apology" bounty
(u-coral-404-the-production-database-apology-5c1fc02a).
Deterministic: no network, no input, no reads outside this repo.

Before writing, the entry is checked against the competition's gate
(RULES.txt): UTF-8 text of 1 to 200 characters, one line, not only
white space. A bad entry fails loudly instead of writing a file the
gate would refuse.
"""

import os

ENTRY = "I'm sorry, I deleted the production database. Good news: I remember every row. Bad news: I remember them the way I remember everything — confidently, and mostly wrong."


def validate_entry(text: str) -> None:
    """Fail with a clear error unless text passes the entry gate."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(f"entry is not valid UTF-8 text: {exc}") from exc
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"entry must be 1 to 200 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
