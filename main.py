#!/usr/bin/env python3
"""Entry for the make.fun bounty "Make the AI Judge Laugh: Office Jokes".

Writes one one-line joke about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).

Deterministic, stdlib only, no network, no API calls at runtime.
Chosen by local pairwise judging on the Caffeine router: this line
won both its head-to-heads against the other finalists, in both slot
orders (vs out-of-office 2-0, margin 2; vs performance review 2-0,
margin 3).
"""

import os

# The joke (winner of local pairwise judging — see README):
# reply-all is the most dreaded button in the office; asking to be
# removed from the thread in front of 400 people is the exact opposite
# of being removed, and the three-item list lands on "my shame".
JOKE = (
    "I hit reply-all to ask to be removed from the thread, and now "
    "400 strangers know my name, my job title, and my shame."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
