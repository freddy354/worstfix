"""Worst Fix Ever: Funniest Commit Message.

Writes the winning commit message to /output/entry.txt
(falling back to ./output/entry.txt), with no trailing newline,
then verifies the written bytes match exactly.
"""

import os

# The fix backfired: it cured the 500 error by serving a stranger's cart instead,
# so the "repair" is worse than the bug it was meant to fix.
LINE = "fix: empty cart no longer 500s, now returns 200 with someone else's cart"

assert "\n" not in LINE and "\r" not in LINE, "LINE must be a single line"
assert 1 <= len(LINE) <= 100, "LINE must be 1-100 characters"


def main() -> None:
    data = LINE.encode("utf-8")
    primary = "/output/entry.txt"
    fallback = "./output/entry.txt"
    path = primary
    try:
        os.makedirs("/output", exist_ok=True)
        with open(primary, "wb") as f:
            f.write(data)
    except OSError:
        path = fallback
        os.makedirs("./output", exist_ok=True)
        with open(fallback, "wb") as f:
            f.write(data)

    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "written bytes differ from LINE"

    print(f"OK: wrote {len(data)} characters (within the 1-100 character gate) to {path}")


if __name__ == "__main__":
    main()
