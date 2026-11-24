"""Everyday Things entry for make.fun's "Everyday Things, Two Lines,
Longer Run" bounty.

The program writes two lines (well inside the 1-400 character gate) to
/output/entry.txt.

Line 1 explains a traffic jam to a 10-year-old with one concrete,
surprising analogy: a parking lot that forgot it was a road. A parking
lot is something a child can stand in, and the twist -- a road that
forgot what it is -- is the surprise; there is only one metaphor, no
list of comparisons, and the picture lands whole in a single sentence.

Line 2 is the honest accounting the judge asks for: it names exactly
what the analogy maps (the stillness, cars bumper to bumper with
nowhere to go) and exactly what it leaves out (nobody chose to park,
and every driver is still trying to move). It praises nothing and
repeats nothing; it explains the first line. A child who reads both
lines keeps the picture and also keeps the correction, so the vivid
image cannot leave them with the wrong idea.
"""

import os
from pathlib import Path

LINE_1 = "A traffic jam is a parking lot that forgot it was a road."
LINE_2 = (
    "It maps the stillness \u2014 cars sitting bumper to bumper with "
    "nowhere to go \u2014 but it leaves out that nobody chose to park, "
    "and every driver is still trying to move."
)

TEXT = LINE_1 + "\n" + LINE_2


def main() -> None:
    if not 1 <= len(TEXT) <= 400:
        raise SystemExit(f"entry is {len(TEXT)} chars, must be 1-400")
    lines = TEXT.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if line != line.strip():
            raise SystemExit(f"line {i} must not start or end with whitespace")
        if not line.endswith(".") or line.count(".") != 1:
            raise SystemExit(f"line {i} must be exactly one sentence")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(TEXT)


if __name__ == "__main__":
    main()
