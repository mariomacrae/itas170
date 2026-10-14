# Week 01

First week of ITAS170: checking which of the term's tools are installed, and
hunting through a web server access log with `grep`, `cut`, `sort` and `uniq`,
while logging how I used an AI assistant along the way.

## Files

| File | What it is |
|---|---|
| [hunt.md](hunt.md) | Log-hunt answers: the command for each question and its result (404s, largest response, Googlebot hits, requests per date, POSTs to `wp-login.php`) |
| [access.log](access.log) | Web server access log (2,400 lines, 10–12 Sep 2026) used for the hunt |
| [LOG.md](LOG.md) | AI session log: each question I asked, what I got back, and how I verified it |
| [LOG-template.md](LOG-template.md) | Blank template for the weekly session log |
| [toolbox.sh](toolbox.sh) | Script that reports which of the term's tools (bash, git, ssh, docker, uv, ollama, claude, …) are installed |
| [toolbox.txt](toolbox.txt) | Notes file for the `toolbox.sh` output |
| [session_history.txt](session_history.txt) | Shell history from the lab session |
| [space.save](space.save) | Saved command (Zed editor install) |

## Running the toolbox check

```bash
cd week01
bash toolbox.sh
```
