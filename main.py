"""Make the AI Judge Laugh — make.fun entry.

Writes one line about office life, under 200 characters,
to /output/entry.txt.
"""

LINE = (
    "Every standup, nine people say 'no blockers' while blocked by "
    "the same meeting they're sitting in."
)


def verify_output() -> bool:
    """Read the written file back as bytes and confirm it matches."""
    with open("/output/entry.txt", "rb") as f:
        return f.read() == LINE.encode("utf-8")


def main() -> None:
    assert 1 <= len(LINE) <= 200, "joke must be 1-200 characters"
    assert LINE.strip(), "joke must not be whitespace-only"
    assert "\n" not in LINE, "joke must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    assert verify_output(), "entry.txt does not match LINE"


if __name__ == "__main__":
    main()
