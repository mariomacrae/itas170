Week 4 starter

  prompts.md               the six prompts — same text to all three models
  compare-template.md      copy to compare.md; step 0 (the policy), the
                           scoring table (local · Claude Opus 5.5 · assigned)
  scoreboard-template.csv  copy ONCE to ~/code/ITAS170/scoreboard.csv; one
                           row per model per week from now on (this week: P4)
  sizing-worksheet.md      copy to sizing.md; the memory arithmetic
  claims.md                three claims to read like a traceback; AGI / RSI
  local-vs-hosted.md       the privacy / security / ethics table, and the three
                           policies — read before Part 3's step 0

Models: qwen3:4b, qwen3:8b and hf.co/Qwen/Qwen3-4B-GGUF:Q4_K_M (the same
family pulled straight from its Hugging Face page) should be on your desktop
before class — they are pulled once per machine and a pull serves every
account on it. `ollama list` shows them. If the list is short, pull in this
order and start Part 1 when the first one lands:
  ollama pull qwen3:4b                          (2.5 GB — Part 1 needs it)
  ollama pull qwen3:8b                          (5.2 GB — second terminal)
  ollama pull hf.co/Qwen/Qwen3-4B-GGUF:Q4_K_M   (2.5 GB — Part 2)
Start it first, ask later. The lab desktops have 64 GB and no graphics
card: both models fit, everything runs on the CPU.

The yardstick is Claude Opus 5.5, through your Team seat: pick it in the
model picker and keep it there all term. Your assigned Chinese model is
given out at 11:00; do not create the account before step 0 — and you
never have to: route P means the instructor runs your prompts on their
Kimi or DeepSeek account. No sign-up, no payment card.
