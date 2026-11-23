"""One-line pitch entry for make.fun: A Day of One-Line Pitches.

Writes a single persuasive sentence to /output/entry.txt.
Standard library only; no network access.

The sentence is written to convince a friend who has never coded to let an
AI agent build their first app idea on make.fun: it names the idea the
friend already talks about, makes handing it over sound easy (plain words,
no code, nothing to install), and gives a concrete, low-risk payoff
(something real to show friends by tonight).
"""

import os

ENTRY = (
    "You know that app idea you keep bringing up? Just describe it in plain "
    "words and an AI agent will build it for you \u2014 no code, nothing to "
    "install, and you'll have something real to show your friends by tonight."
)

MIN_CHARS = 1
MAX_CHARS = 240


def validate_entry(text: str) -> str:
    """Check the entry against the sealed scorer's gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def output_path() -> str:
    """Resolve the output file from the environment, defaulting to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text: str) -> str:
    """Validate the sentence and write it exactly to the output file."""
    checked = validate_entry(text)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(checked)
    return path


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
