"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message -- the fix that made everything worse --
to /output/entry.txt. The line is held as a constant, validated, and
written out verbatim with no trailing newline.

The joke: the page no longer loads slowly, because there is nothing left
to load. A repair that "fixed" the symptom by deleting the whole point.
"""

import os

COMMIT_MESSAGE = "fix: slow page load by showing a blank page instantly"


def validate(line):
    """Check the line reads as one real commit message of 1-100 chars."""
    if not line or not line.strip():
        raise ValueError("commit message must not be empty")
    if line != line.strip():
        raise ValueError("commit message must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("commit message must be exactly one line")
    if not line.startswith("fix:"):
        raise ValueError("commit message must read as a fix commit")
    if len(line) > 100:
        raise ValueError("commit message must be at most 100 characters")


def main():
    validate(COMMIT_MESSAGE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE)


if __name__ == "__main__":
    main()
