# Week 04

Fourth week of ITAS170: local models versus frontier models. I ran Qwen3
locally with Ollama (CPU only, no graphics card), measured its speed in
tokens per second, worked out how much memory models of different sizes
need, and gave the same six prompts to three models — the local `qwen3:4b`,
Claude Opus 5.5 as the yardstick, and my assigned hosted model, DeepSeek V4.1
Flash — checking each answer myself before scoring it. I also read three
claims about model performance the way you would read a traceback.

## The lab, part by part

| Part | What I did | Where it is |
|---|---|---|
| 1 — Run it | Ran `qwen3:4b` with `--verbose --think=false`, captured `ollama ps`, took three eval rates (median 9.15 tokens/s), and compared load duration and thinking on vs off | `local.md` |
| 2 — Size it | Predicted memory for models from 4B to 2.4T parameters (parameters × bytes per parameter + working room), checked one row against `ollama ps`, compared the Ollama-library and Hugging Face pulls of Qwen3-4B, and read the model card | `sizing.md` (in the zip) |
| 3 — Blind comparison | Read DeepSeek's privacy policy before signing up, ran prompts P1–P6 on all three models, timed and scored each 0–2 on correct / complete / checkable, and added three P4 rows to the scoreboard | `compare.md`, `scoreboard.csv` |
| 4 — Read a claim | Five lines each on a product announcement, the Kimi K3 launch post, and a distillation report, plus AGI and RSI in my own words | `claims.md` |
| 5 — Make it yours | Route C, the desk measured: P2 with 12 lines vs a much longer prompt — prompt eval duration, and how the long prompt cost the local model its correctness | `prompt_eval_comparison.md` |

## Files

| File | What it is |
|---|---|
| [itas170-week04-handout.pdf](itas170-week04-handout.pdf) | The lab handout: parts, timings, marking |
| [prompts.md](prompts.md) | The six prompts given to every model (starter file) |
| [compare-template.md](compare-template.md) | Blank comparison table (starter file) |
| [sizing-worksheet.md](sizing-worksheet.md) | Blank memory-sizing worksheet (starter file) |
| [scoreboard-template.csv](scoreboard-template.csv) | Column headings for the course scoreboard (starter file) |
| [local-vs-hosted.md](local-vs-hosted.md) | Privacy, security and ethics trade-offs, and the three privacy policies (starter file) |
| [local.md](local.md) | Part 1 working copy |
| [compare.md](compare.md) | Part 3 working copy |
| [itas170_week04_mariomacrae/](itas170_week04_mariomacrae/) | Final hand-in: `local.md`, `compare.md`, `claims.md`, `scoreboard.csv`, `prompt_eval_comparison.md` |
| [itas170_week04_mariomacrae.zip](itas170_week04_mariomacrae.zip) | Submitted copy, which also holds `sizing.md` |

`local.md`, `compare.md` and `claims.md` were saved from a word processor, so
despite the `.md` name they are Word documents — open them in LibreOffice or
Word, not a text editor.

## Reproducing Part 1

```bash
ollama list
ollama run --verbose --think=false qwen3:4b "Explain exactly what this shell command does, option by option, in at most five lines. Do not suggest alternatives. sort -k10,10n access.log | tail -1"
ollama ps    # in a second terminal, while it answers
```
