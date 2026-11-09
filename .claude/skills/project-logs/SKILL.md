---
name: project-logs
description: Use when writing an entry in docs/DEV_LOG.md (after every approved change), docs/LEARNING_LOG.md (after every finished step), or a git commit message in this project.
---

# Project logs

Three records. Formats are fixed — follow them exactly. Logs are append-only: never edit or delete old entries (add a correction entry instead).

## 1. DEV_LOG (`docs/DEV_LOG.md`) — after every approved change

```
### YYYY-MM-DD — step-NN — <short title>
- **What:** what changed
- **Why:** reason
- **Files:** `path` (new / changed / deleted)
- **Approved by Raguram:** yes — <how>
- **Commit:** `<type>(step-NN): <summary>` or "not committed yet"
- **Notes:** surprises, follow-ups
```

- Date from the system (`date +%F`), never guessed.
- Use the step number from `docs/TASKS.md` (two digits: `step-03`).

## 2. LEARNING_LOG (`docs/LEARNING_LOG.md`) — after every finished step

Use the template at the top of the file. Rules:
- "In my own words" must come from Raguram's explain-back. Tidy grammar only, don't replace his meaning.
- Include Python vs Java rows for new syntax.
- Record mistakes and confusions honestly — they are the most useful part.
- New Python vs Java items also go into the quick-reference table in `docs/LEARNING.md`.

## 3. Commit messages — format in `docs/CONVENTIONS.md`

```
<type>(step-NN): <short summary, present tense, ≤ ~60 chars>
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`.

Before proposing a commit:
- Run `git status` and show it.
- Make sure `.env` is not staged.
- Commit needs its own approval (`approval-gate`).
- After committing, put the commit message into the DEV_LOG entry.
