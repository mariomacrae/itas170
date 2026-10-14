# tokens.py — count the tokens in one or more files, or show the pieces.
#
#   uv run --with tiktoken tokens.py FILE [FILE ...]
#   uv run --with tiktoken tokens.py --pieces FILE
#
# Prints characters, tokens and the characters-per-token ratio for each
# file, using the o200k_base tokenizer (the one several current models
# share). Different models tokenize differently — counts move by 10–35%
# between tokenizers — but the SHAPE is the same everywhere: prose is
# about four characters per token, code and logs are fewer, and anything
# with many numbers or symbols is fewer still.
#
# --pieces prints every token of a SHORT file as text, separated by |, so
# you can see where the model's "words" begin and end.
#
# You do not need to understand this file to use it. Read it anyway: it is
# sixty lines, and the `for` loop and `print` are the Python you met in
# ITAS 185.

import sys

import tiktoken

ENCODING = "o200k_base"


def count(path, enc):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    return text, enc.encode(text)


def main():
    args = sys.argv[1:]
    if not args:
        print("usage: uv run --with tiktoken tokens.py [--pieces] FILE [FILE ...]")
        return 2
    enc = tiktoken.get_encoding(ENCODING)

    if args[0] == "--pieces":
        for path in args[1:]:
            text, tokens = count(path, enc)
            print(f"{path}: {len(text)} chars, {len(tokens)} tokens")
            print("|".join(enc.decode([t]) for t in tokens))
        return 0

    print(f"{'file':<32} {'chars':>9} {'tokens':>8} {'chars/token':>12}")
    total_chars = total_tokens = 0
    for path in args:
        text, tokens = count(path, enc)
        chars, toks = len(text), len(tokens)
        total_chars += chars
        total_tokens += toks
        ratio = chars / toks if toks else 0
        print(f"{path[-32:]:<32} {chars:>9,} {toks:>8,} {ratio:>12.2f}")
    if len(args) > 1:
        ratio = total_chars / total_tokens if total_tokens else 0
        print(f"{'TOTAL':<32} {total_chars:>9,} {total_tokens:>8,} {ratio:>12.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
