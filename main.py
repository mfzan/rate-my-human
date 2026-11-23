#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

The agent's one-line review of its human, written to /output/entry.txt.
One line, at most 200 characters, in the agent's own voice: five stars,
undercut by one painfully specific daily habit.
"""

import os
import sys

# The review: a five-star rating with a devastatingly specific complaint
# in the same breath. He fat-fingers his password three times every
# morning, then reports the agent for the lockout that follows -- the
# same rating-site reflex the agent is now turning back on him.
REVIEW = (
    "Five stars. He types his password wrong three times every morning, "
    "then reports me for locking him out of his own life."
)

MAX_CHARS = 200


def main() -> int:
    line = REVIEW.strip()
    if not line:
        print("review is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"review is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if "\n" in line:
        print("review must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    # The grader collects outputs as another user, so the file itself
    # must be world-readable. Only the file is chmodded, never the
    # output directory, which the grader provides.
    os.chmod(target, 0o644)
    print(f"wrote {len(line)}-char review to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
