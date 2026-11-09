---
name: start-build-step
description: Use when Raguram says "start step N", "next step", or "what's next" in this Python AI agent project. Walks through learn → plan → propose → build → explain-back → log for one step of docs/TASKS.md.
---

# Start a build step

## 1. Find the step
- Open `docs/TASKS.md`. Find the first step with status `todo` or `doing` (or the one Raguram named).
- Check the previous step is `done`. If not, say so and ask whether to finish it first.
- Set the step status to `doing` (this is a docs change, still mention it to Raguram).

## 2. Learn first (10–15 min)
- Open `docs/LEARNING.md` → the row for this step.
- Explain each Python item and AI concept briefly, with a Java comparison where it helps.
- Ask 1–2 quick check questions before coding. Don't move on until he's comfortable.

## 3. Plan
- Break the step into small tasks (use the checkboxes in `docs/TASKS.md`).
- Say which files will be touched and why. Use names from `docs/CONVENTIONS.md`.

## 4. Build, one small piece at a time
- For each piece, use the `approval-gate` skill. Never skip it.
- After each approved piece: Raguram runs it (`uv run ...`) and you explain the output together.
- Tick the checkbox in `docs/TASKS.md` when a task is done.

## 5. Explain-back
- Ask Raguram to explain the step in his own words.
- Correct gently, add what's missing.

## 6. Close the step
- `docs/LEARNING_LOG.md` entry (use `project-logs`), based on his explanation.
- `docs/DEV_LOG.md` has an entry for each change.
- Propose the commit (approval needed).
- Set step status to `done` in `docs/TASKS.md`.
- Suggest saving key notes to Second Brain (Raguram decides).

## Stay focused
If a new idea comes up mid-step, add it to "Parked ideas" in `docs/TASKS.md` and return to the current step.
