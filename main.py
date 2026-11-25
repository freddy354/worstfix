import os

LINE = "fix: empty cart no longer 500s, now returns 200 with someone else's cart"

# Commit-message entries must be a single line: reject any newline/CR so a
# stray line break can never sneak into entry.txt and break the format.
assert "\n" not in LINE and "\r" not in LINE, "LINE must not contain a newline"

# Competition gate: the entry must be 1-100 characters long.
assert 1 <= len(LINE) <= 100, "LINE must be 1-100 characters"

try:
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
except OSError:
    os.makedirs("./output", exist_ok=True)
    out_path = "./output/entry.txt"

with open(out_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open(out_path, "rb") as f:
    content = f.read()
assert content == LINE.encode("utf-8"), "entry.txt does not match LINE byte-for-byte"

print(f"OK: wrote {len(LINE)} characters ({len(content)} bytes) to {out_path} (gate 1-100 chars); verified entry.txt matches LINE byte-for-byte")
