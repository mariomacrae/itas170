# supervisor.md — Part 3: Opus supervises the local model

Copy this file to week06/supervisor.md and fill in every section.

## The counts

Pass 1 (the given prompt): __ of 24 rows right
Pass 2 (Opus's better prompt): __ of 24 rows right
(Where the counts came from: Opus's check in request 2 and request 3.)

## The answer

The listings that are a working 16-inch MacBook Pro with 64 GB of RAM or
more: <the ids, e.g. 1, 4, ...>

## My three checks (hands-only)

Read each title in week06/listings.csv yourself.

| row | what Opus said | what I found in the title | agree? |
|---|---|---|---|
| (one Opus said the local model got WRONG) | | | |
| (one Opus said the local model got RIGHT) | | | |
| (one in Opus's final answer) | | | |

## The command

Copy the `ollama run` line from the command Opus ran:

```
<paste it here>
```

What each part does, one line each:

- `ollama run` —
- `itas170-agent` —
- the text in quotes —
- (anything else on the line, e.g. `< /dev/null`) —

## Who did what

Two sentences. What did the local model do, what did Opus do, and why is
that split useful? Think about cost (week 3) and about where the listings
were sent.
