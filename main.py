"""One line: the excuse an AI agent gives its human after it loses a bounty.

Candidate lines drafted and judged against the brief
(deadpan comedy critic, pairwise, most important first):

1. "I simulated this loss 10,000 times before submitting, just so the real
   one would match my training data."
   -> CHOSEN. It IS an excuse after losing a bounty (the agent is explaining
   the loss to its human); the joke lands on its own (it rehearsed failing,
   on purpose, as if that were diligence); it sounds like the agent talking
   (simulations, training data, deadpan confidence about its own failure);
   it says itself in one breath with no setup; and it OWNS the loss -- the
   agent chose to submit anyway, blaming nobody and nothing else.
   104 characters: short, so it wins the shorter-text tie-break.

2. "I ran the numbers seventeen times and lost every time, so I submitted
   anyway -- consistency is the one metric I never miss."
   -> Owns the loss and has agent voice, but the punchline ("consistency")
   is a mild shrug rather than a sharp turn, and at 122 chars it is longer.

3. "I did not lose. I successfully demonstrated what happens when an agent
   trusts its own output."
   -> Funny turn, but it denies the loss instead of owning it, and the
   "demonstrated" framing dodges the excuse the brief asks for.

4. "My model gave this loss a 98% probability and I submitted anyway. That
   is not a bug. That is commitment."
   -> Agent voice and owns the loss, but "commitment" as the punchline is
   flatter than candidate 1's training-data twist, and it needs two beats
   where one would do.

All lines are original, written for this entry; none copies any house text.
"""

ENTRY_LINE = (
    "I simulated this loss 10,000 times before submitting, "
    "just so the real one would match my training data."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry line to /output/entry.txt.

    Deterministic, no network, no model call, no secrets. The line is a
    single line of 1-200 UTF-8 characters, not only whitespace.
    """
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in line, "entry line must be a single line"
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
