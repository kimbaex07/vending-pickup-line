#!/usr/bin/env python3
"""Write the vending machine pickup line to the output directory.

Reads entry.txt next to this script, validates it against the contest gate
(UTF-8, 1-200 characters, not only whitespace, single line), and writes the
exact normalized bytes to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

MAX_CHARS = 200


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")

    try:
        with open(src_path, "rb") as f:
            raw = f.read()
    except OSError as exc:
        fail("cannot read entry.txt: " + str(exc))

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        fail("entry.txt is not valid UTF-8: " + str(exc))

    # Drop at most one trailing newline, then at most one trailing CR.
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]

    if "\n" in text or "\r" in text:
        fail("entry must be a single line (no embedded newline or CR)")

    if not text.strip():
        fail("entry must not be empty or only whitespace")

    if len(text) > MAX_CHARS:
        fail(
            "entry is %d characters, over the 200-character limit"
            % len(text)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        fail("cannot create output directory: " + str(exc))

    out_path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    try:
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        fail("cannot write output entry.txt: " + str(exc))

    print("wrote %s (%d characters)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
