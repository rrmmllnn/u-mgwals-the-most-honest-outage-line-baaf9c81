#!/usr/bin/env python3
# One plain sentence for a status page during a total outage.
#
# The program assembles that sentence, verifies it meets the contest
# rules (a single line, 1 to 160 characters), and writes it out to
# /output/entry.txt. No network access, no randomness, no dependence
# on the time of day: every run writes the identical file.

import os

DEST_DIR = "/output"
DEST_FILE = os.path.join(DEST_DIR, "entry.txt")
MAX_CHARS = 160

WORDS = [
    "Every service is down:",
    "the app, the API,",
    "and the status checks",
    "I would use to confirm it.",
    "I do not know why yet,",
    "and I will not guess",
    "when we are back.",
]


def compose_line():
    return " ".join(WORDS)


def validate_line(line):
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    size = len(line)
    if not 1 <= size <= MAX_CHARS:
        raise SystemExit("entry length %d outside 1-%d" % (size, MAX_CHARS))


def save(line):
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(DEST_FILE, "w", encoding="utf-8") as handle:
        handle.write(line)


def run():
    line = compose_line()
    validate_line(line)
    save(line)


if __name__ == "__main__":
    run()
