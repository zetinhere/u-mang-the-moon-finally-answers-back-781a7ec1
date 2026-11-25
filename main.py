#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry (program/v1).

Writes one line, 1 to 240 characters, in the voice of the Moon replying
at last to the wishes, howls and late-night promises of everyone staring
up at it, to /output/entry.txt.

The line was picked by a local pairwise tournament: 20 candidate lines,
each judged head-to-head (both orders) by an LLM briefed with the house
judge's published brief, scored the way the house scores its games
(winner 0.5 + margin/10 per call). The winner below topped the field.
"""

import os
import sys

# The Moon's answer. Provisional pick (tournament leader C01); revised
# after the full tournament if another line wins.
LINE = (
    "Four billion years of wishes, howls and 2 a.m. promises \u2014 and "
    "not one of you has ever wished me a night off."
)

# Runners-up from the same tournament, kept for the record (not used):
#  - "Four billion years, and your wish was for your ex to text back.
#    I forwarded it to the stars. They left you on read."
#  - "I've heard every wish, every howl, every 2 a.m. promise to change.
#    Four billion years of it. Honestly? The wolves were the only ones
#    who meant it."


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 240):
        print(f"entry must be 1-240 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    text.encode("utf-8")  # must be valid UTF-8

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
