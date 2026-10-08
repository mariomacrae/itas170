Week 3 starter

  tokens.py              count tokens:   uv run --with tiktoken tokens.py FILE...
                         see the pieces: uv run --with tiktoken tokens.py --pieces sample.txt
  cost.py + pricing.csv  cost a conversation: uv run --with tiktoken cost.py 50000 20
                         (prices are DATA, dated in the csv; refresh them, not the code)
  sample.txt             140 characters to tokenize first
  templates/             two prompt templates with ${VARIABLES}, filled by envsubst
