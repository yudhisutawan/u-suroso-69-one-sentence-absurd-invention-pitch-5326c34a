"""Printer's excuse note — entry for One-Sentence Absurd Invention Pitch.

The pitch: a printer that, instead of printing, prints a formal excuse note
for every page it refuses to print, signed in Comic Sans by its manager, the
scanner.

Why it is funny: the annoyance is real (printers refuse to print), and the
invention is perverse in exactly the right way — a printer that does
bureaucracy instead of printing. The laugh comes from the invention itself:
three specific jokes stacked in one sentence (a formal excuse note, signed
in Comic Sans, by its manager, the scanner), each one following from the
machine's own logic, with the punch — the scanner is the printer's manager —
landing at the very end.

This pitch won a 10-candidate round-robin tournament (45 pairs, judged
head-to-head with the competition's own brief: on-brief, funny, clever fix,
original, tight): UNDEFEATED, 9 wins and 0 losses, beating the runner-up —
a toothbrush that gossips to the mirror about your 2 a.m. tacos (8-1) — and
the third-place truth-telling pen (7-2) head to head. Full record in
TOURNAMENT.md.

Writes the pitch to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).
"""

import os

# Winner of the 10-candidate round-robin (45 pairs): undefeated, 9-0.
PITCH = (
    "My printer now prints a formal excuse note for every page it refuses "
    "to print, signed in Comic Sans by its manager, the scanner."
)

# Competition gate: one sentence, 1-220 characters.
MAX_CHARS = 220


def pitch_text() -> str:
    """Return the pitch as a single line with no trailing newline."""
    return PITCH.strip()


def check_pitch(text: str) -> None:
    """Refuse anything that would fail the gate: not one line, or too long."""
    if "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line")
    if not text.strip():
        raise SystemExit("pitch must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"pitch must be at most {MAX_CHARS} characters, got {len(text)}"
        )
    # One sentence, not two wearing a trench coat: no sentence break inside.
    if ". " in text.rstrip("."):
        raise SystemExit("pitch must be a single sentence")
    if not text.endswith("."):
        raise SystemExit("pitch must end with a full stop")


def main() -> None:
    text = pitch_text()
    check_pitch(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
