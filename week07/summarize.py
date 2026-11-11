# summarize.py — medians and ratios from one or many results.csv files.
#
#   python3 summarize.py results.csv
#   python3 summarize.py results/*.csv --baseline ext4
#
# For every (label, test) it prints the median of all runs found, and the
# ratio to the baseline label (default: ext4). Ratios are the honest number:
# "git is 71x slower there" travels between machines; "25 seconds" does
# not. Give it every file in the class dataset and it pools them.
# Standard library only — no uv needed.

import csv
import statistics
import sys

TESTS = ["create", "read", "git", "big200MB", "delete"]


def main():
    args = sys.argv[1:]
    baseline = "ext4"
    if "--baseline" in args:
        i = args.index("--baseline")
        baseline = args[i + 1]
        del args[i:i + 2]
    if not args:
        print("usage: python3 summarize.py results.csv [more.csv ...] [--baseline LABEL]")
        return 2
    runs = {}
    machines = set()
    for path in args:
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                runs.setdefault((r["label"], r["test"]), []).append(float(r["seconds"]))
                machines.add(r["machine"])
    labels = sorted({k[0] for k in runs}, key=lambda l: (l != baseline, l))
    print(f"{len(args)} file(s), {len(machines)} machine(s); median seconds (number of runs)")
    print(f"{'test':<10}" + "".join(f"{l:>14}" for l in labels))
    for t in TESTS:
        line = f"{t:<10}"
        for l in labels:
            xs = runs.get((l, t), [])
            line += f"{statistics.median(xs):>11.2f}({len(xs)})" if xs else f"{'-':>14}"
        print(line)
    print()
    print(f"{'test':<10}" + "".join(f"{l + ' / ' + baseline:>18}" for l in labels if l != baseline))
    for t in TESTS:
        base = runs.get((baseline, t))
        if not base:
            continue
        b = statistics.median(base)
        line = f"{t:<10}"
        for l in labels:
            if l == baseline:
                continue
            xs = runs.get((l, t))
            line += f"{statistics.median(xs) / b:>17.1f}x" if xs and b > 0 else f"{'-':>18}"
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
