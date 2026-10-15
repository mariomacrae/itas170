# Week 02

Second week of ITAS170: putting the course folder under version control with
`git` (first commits, `.gitignore`, reading a diff, recovering a file with
`git restore`), setting up an SSH key for GitHub, and pushing the repository
to a remote — while logging how I used an AI assistant along the way.

## Files

| File | What it is |
|---|---|
| [gitlog.md](gitlog.md) | Git worksheet: `git status` / `git log` output from the first commit, the `.gitignore` contents, the diff and `git restore` recovery, the GitHub remote, and the history of `week01/LOG.md` |
| [ssh3.md](ssh3.md) | SSH worksheet: `~/.ssh` permissions, which key may leave the machine, GitHub's host fingerprint (checked against `api.github.com/meta`), the `ssh -T git@github.com` proof, and the `Host gh` config entry |
| [LOG_week02.md](LOG_week02.md) | AI session log: each question I asked while getting the push to GitHub working (upstream branch, wrong username, `~/.ssh` permissions), what I got back, and how I checked it |
| [ITAS170_week02_mario_macrae.zip](ITAS170_week02_mario_macrae.zip) | Submitted copy of the three files above |

## Checking the GitHub connection

```bash
ssh -T git@github.com
git remote -v
```
