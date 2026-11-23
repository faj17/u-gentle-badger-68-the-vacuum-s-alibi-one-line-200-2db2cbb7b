"""The vacuum's alibi, for the make.fun bounty "The Vacuum's Alibi".

One line, at most 200 characters, in which a robot vacuum explains why
it missed a spot. The script assembles the line from fragments, validates
it against the gate (1-200 characters, not whitespace-only, one line) and
writes it to /output/entry.txt.
"""

from pathlib import Path

# The alibi, in two fragments joined at write time by assemble_alibi().
# The vacuum opens with a flat denial — it is an alibi, after all — then
# explains itself in deadpan machine terms: its lidar did the mapping,
# its battery cast the deciding vote, and the dust stays because the
# machine has formally classified it as part of the building.
OPENING = (
    "I did not miss that spot \u2014 my lidar classified the dust "
    "as load-bearing, "
)
CLOSING = (
    "and my battery voted to leave it holding the floor together."
)


def assemble_alibi() -> str:
    """Join the two alibi fragments into the single-line excuse."""
    return OPENING + CLOSING


OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the alibi; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"alibi must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("alibi must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("alibi must be a single line")
    return text


def main() -> None:
    text = validate(assemble_alibi())
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
