# Week 10 — First piece on a branch, merged by pull request

Monday 23 November. Final project milestone: **idea and plan agreed**.

## Before the lab

- Five minutes with the instructor in class: agree a challenging, unique idea.
- Your project repository exists on GitHub, with a first `PLAN.md` that breaks
  the idea into pieces (you edit it yourself; it is your to-do list).

## In the lab

1. **Branch.** From an up-to-date `main`, create a branch for your first piece:

   ```bash
   git switch main
   git pull
   git switch -c feature/<first-piece>
   ```

2. **Build one piece.** Plan first (Plan mode), then build and test the piece on
   the branch. Read every diff before you accept it; `git restore` is your undo.
   One piece per session, one commit per piece.

3. **Push the branch.**

   ```bash
   git push -u origin feature/<first-piece>
   ```

4. **Open a pull request** on GitHub into `main`. Describe what the piece does
   and how you checked it.

5. **Merge with "Create a merge commit"** — not "Squash and merge" — so the
   history keeps every piece. Deleting the branch after the merge is fine.

6. **Update locally.**

   ```bash
   git switch main
   git pull
   ```

7. **Write a first `SETUP.md`** — the handoff file a fresh session reads first:
   how to set the project up, run it and test it; where things live; what is
   done; what was decided and why; what is half-done and what comes next.
   No secrets in it. Have the assistant draft it, then read it and fix it.
   Your `CLAUDE.md` or `AGENTS.md` says "Read SETUP.md first."

8. **Log the session** in `LOG.md` in the course's four-line format: what I
   asked; what came back, in my words; what I verified and how; what I would
   ask differently.

## Done when

- [ ] `PLAN.md` is in the repository
- [ ] One feature branch pushed and merged into `main` through a pull request
      (visible under Pull requests → Closed), using a merge commit
- [ ] A first `SETUP.md`, and `CLAUDE.md`/`AGENTS.md` points to it
- [ ] `LOG.md` has an entry for this session

## Why branches

New features are built on a branch so `main` keeps working while the agent
experiments. The final project needs **at least two** feature branches, each
built and tested on its branch, pushed, and merged by pull request — this lab
is the first.

## Next

Mon 30 November: working core — the first important piece runs; show it in class.

Source: `week09/itas170-final-handout.pdf` (sections 3, 4 and the schedule).
