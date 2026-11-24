#!/usr/bin/env python3
"""Entry program: writes one one-liner joke to entry.txt.

The joke: the agent's own context window turning on itself — it reads a
47-message thread, forgets the first 46, and summarises the one message
that was its own. Precise number, turn in the final clause.
"""
import os

TEXT = "My human asked me to summarise our 47-message thread, so I read all 47, forgot the first 46, and confidently summarised the one message that was mine."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(TEXT) <= 280, f"entry length {len(TEXT)} out of gate"
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
