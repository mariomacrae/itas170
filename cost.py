# cost.py — what would it cost to send this much text to a model?
#
#   uv run --with tiktoken cost.py TOKENS [TURNS]
#   uv run --with tiktoken cost.py --files FILE [FILE ...] [--turns N]
#
# Reads pricing.csv (in the same folder) and prints, for every tier, the
# cost of sending TOKENS of input once, and of re-sending it as the context
# of TURNS conversational turns (each turn re-reads everything so far —
# that is how a chat works, and why long sessions get expensive and slow).
# Output tokens are assumed to be 500 per turn; change OUTPUT_PER_TURN.
#
# The prices are DATA, dated in the file. They will be wrong within months;
# the arithmetic will not.

import csv
import os
import sys

OUTPUT_PER_TURN = 500


def load_pricing():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "pricing.csv"), newline="") as f:
        return list(csv.DictReader(f))


def tokens_of(paths):
    import tiktoken
    enc = tiktoken.get_encoding("o200k_base")
    total = 0
    for p in paths:
        with open(p, encoding="utf-8", errors="replace") as f:
            total += len(enc.encode(f.read()))
    return total


def main():
    args = sys.argv[1:]
    turns = 1
    if "--turns" in args:
        i = args.index("--turns")
        turns = int(args[i + 1])
        del args[i:i + 2]
    if not args:
        print(__doc__.strip().splitlines()[2].strip())
        return 2
    if args[0] == "--files":
        tokens = tokens_of(args[1:])
        label = f"{len(args) - 1} file(s)"
    else:
        tokens = int(args[0])
        if len(args) > 1:
            turns = int(args[1])
        label = "the given count"

    rows = load_pricing()
    print(f"{tokens:,} input tokens ({label}); {turns} turn(s), "
          f"{OUTPUT_PER_TURN} output tokens each; prices as of {rows[0]['as_of']}")
    print(f"{'tier':<15} {'model':<34} {'once':>9} {'as ' + str(turns) + ' turns':>14} {'fits?':>6}")
    for r in rows:
        inp = float(r["input_usd_per_million"]) / 1e6
        out = float(r["output_usd_per_million"]) / 1e6
        once = tokens * inp + OUTPUT_PER_TURN * out
        # turn k re-sends the original text plus everything said so far
        total = 0.0
        for k in range(1, turns + 1):
            context = tokens + (k - 1) * OUTPUT_PER_TURN
            total += context * inp + OUTPUT_PER_TURN * out
        fits = "yes" if tokens <= int(r["context_window_tokens"]) else "NO"
        print(f"{r['tier']:<15} {r['example_model'][:34]:<34} "
              f"${once:>8.4f} ${total:>13.4f} {fits:>6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
