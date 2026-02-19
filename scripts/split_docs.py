#!/usr/bin/env python3
"""Split Corezoid-documentation.md into logical chunks."""

from pathlib import Path

BASE = Path(__file__).parent.parent
SRC = BASE / "references" / "Corezoid-documentation.md"
OUT = BASE / "references" / "docs"

# (start_line, end_line, filename) - end_line is exclusive
CHUNKS = [
    (1, 79, "01-introduction.md"),
    (79, 589, "02-interface.md"),
    (589, 2313, "03-core-concepts.md"),
    (2313, 2869, "04-nodes-flow.md"),
    (2869, 3751, "05-nodes-set-code.md"),
    (3751, 4857, "06-nodes-git-call.md"),
    (4857, 5468, "07-nodes-api-db.md"),
    (5468, 6158, "08-nodes-queue-copy-call.md"),
    (6158, 6826, "09-nodes-callback-modify-sum.md"),
    (6826, 7256, "10-deployment.md"),
    (7256, 7453, "11-processes-advanced.md"),
    (7453, 9124, "12-communications-orchestrator.md"),
    (9124, 9455, "13-tutorials.md"),
    (9455, 10492, "14-references.md"),
]

def main():
    content = SRC.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    OUT.mkdir(parents=True, exist_ok=True)

    for start, end, name in CHUNKS:
        chunk = "".join(lines[start - 1 : end - 1])
        out_path = OUT / name
        out_path.write_text(chunk, encoding="utf-8")
        print(f"  {name}: lines {start}-{end-1} ({len(chunk.splitlines())} lines)")

if __name__ == "__main__":
    main()
