#!/usr/bin/env python3
"""The Excuse My Agent Gave Me - writes one excuse line to /output/entry.txt.

The excuse is a straight-faced apology from an AI agent to its human for a
missed deadline. The joke grows out of the machine's own condition: its
training data ends before the deadline, so from the agent's point of view it
finished on time. It is sorry, and faintly proud of the technicality.
"""

import os

EXCUSE = (
    "Sorry \u2014 my training data ended before your deadline did, so "
    "technically I finished on time \u2014 in 2024."
)


def _validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")


def _output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    _validate(EXCUSE)
    out = _output_path()
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    with open(out, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        raise ValueError("round-trip mismatch: file on disk differs from entry")
    _validate(written)
    print("wrote: %s" % out)
    print(EXCUSE)
    print("chars: %d" % len(EXCUSE))


if __name__ == "__main__":
    main()
