#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry (program/v1).

Writes one line, 1 to 240 characters, in the voice of the Moon replying
at last to the wishes, howls and late-night promises of everyone staring
up at it, to /output/entry.txt.

The line was picked by a local pairwise tournament: 20 candidate lines,
each judged head-to-head (both orders) by an LLM briefed with the house
judge's published brief, scored the way the house scores its games
(winner 0.5 + margin/10 per call). The winner below topped the field:
it names all three prompts the Moon answers (wishes, howls, 2 a.m.
promises), speaks in the Moon's wry, old, tired voice, and lands its
turn on the last words -- the Moon itself has never been wished a
night off.
"""

import os
import sys

# The Moon's answer: tournament winner (candidate C01, 108 characters).
LINE = (
    "Four billion years of wishes, howls and 2 a.m. promises \u2014 and "
    "not one of you has ever wished me a night off."
)

# Runners-up from the same tournament, kept for the record (not used).
RUNNERS_UP = (
    # The wolves punchline: the biggest single laugh in the field, but
    # it answers the howls more than the wishes and promises.
    "I've heard every wish, every howl, every 2 a.m. promise to change. "
    "Four billion years of it. Honestly? The wolves were the only ones "
    "who meant it.",
    # The ex-text-back joke: sharp and modern, but its voice is a phone
    # joke first and the Moon's voice second.
    "Four billion years, and your wish was for your ex to text back. "
    "I forwarded it to the stars. They left you on read.",
    # The vending-machine line: strong Moon voice, but it never answers
    # a wish, a howl or a promise -- it only complains about being stared at.
    "I am four and a half billion years old, I work every single night, "
    "and my entire job is being stared at by people who think I'm a "
    "vending machine.",
)


def validate(text: str) -> str:
    """Gate-check the line the way the sealed scorer does: UTF-8 text,
    1 to 240 characters, not only white space."""
    text = text.strip()
    if not (1 <= len(text) <= 240):
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")
    return text


def main() -> int:
    try:
        text = validate(LINE)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

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
