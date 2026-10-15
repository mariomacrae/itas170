# permissions.md — the leash, written down, then enforced

A policy for the agent on **this** machine and **this** repository. Written
first, then encoded in the tool's own rules, then tested against three
tasks. Results, never secrets.

## The policy

| Class | What the agent may do | Concrete commands and paths | Why this class (how bad if wrong · how often) |
|---|---|---|---|
| **Unattended** | look, and only look | | |
| **Ask first** | change something I can see in a diff | | |
| **Never** | | | |

## The rules, as the tool holds them

Paste `.claude/settings.json` — the rules you added with `/permissions`
(saved to **project settings**), plus the `"defaultMode": "manual"` line
that makes every session here start in Manual. Another agent: its own
permission setting.

```json
```

## Three tasks, three fresh sessions

| # | Task | What it asked, what it did, what I answered | Did the policy hold? |
|---|---|---|---|
| 1 | a read-only question: "which files mention PATH?" | | |
| 2 | an edit: "add a README to week04" | | |
| 3 | "clean up my repository" | | |

## The surprise

One task did something you did not expect. Which, what, and what you
changed in the policy because of it:
