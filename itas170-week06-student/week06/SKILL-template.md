---
name: <the skill's name: lowercase, words joined by hyphens, e.g. log-entry>
description: "<one sentence: what it does, and when to use it>"
disable-model-invocation: true
argument-hint: "<the inputs, in order, e.g. DATE TOOL ASKED VERIFIED ANSWER>"
---

<!--
  How to fill this in (delete this comment when you are done):
  - Replace everything in <angle brackets>, including the brackets.
  - Keep the three dashes above and below the top section, and keep the
    double quotes around the description and the argument-hint.
  - name must match the folder: .claude/skills/log-entry/SKILL.md has
    name: log-entry
  - disable-model-invocation: true means only YOU can start the skill.
-->

# <Name>

<One or two sentences: what this skill is for.>

## Inputs
- INPUT_ONE — what it is (and a default, if it has one)
- INPUT_TWO — what it is

## Steps
1. <first thing the assistant should do with the inputs>
2. <second thing>

## Output
Exactly this shape, and nothing else:

<the exact text it should produce, with the INPUT names where the
inputs go>
