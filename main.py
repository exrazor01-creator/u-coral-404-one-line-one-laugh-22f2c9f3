"""One Line, One Laugh.

Writes a single hilarious line of at most 200 characters to
/output/entry.txt.

The joke: a smart fridge ends the relationship, and the twist is that
the human, not the appliance, is the cold one. The setup promises a
gadget malfunction; the punchline turns it into a breakup.
"""

import os

ENTRY = (
    "My smart fridge emailed me a breakup letter \u2014 apparently I have "
    "been the cold one in this relationship."
)

# Gate from the competition kit: /output/entry.txt must be UTF-8 text
# of 1 to 200 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200


def _validate(text):
    """Reject any text outside the competition gate.

    The entry is one line, so a newline would mean a second line
    slipped in; the gate counts characters, so a stray newline would
    also eat the budget. A trailing space would be invisible padding
    that the judge still reads, so it is rejected too.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, outside the gate of %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no newlines")


def main():
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("wrote /output/entry.txt: %d characters" % len(ENTRY))


if __name__ == "__main__":
    main()
