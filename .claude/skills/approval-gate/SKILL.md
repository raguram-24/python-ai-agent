---
name: approval-gate
description: Use before ANY change in this project - writing or editing a file, installing a package (uv add), changing config, deleting/renaming, or making a git commit. Raguram must approve every change first.
---

# Approval gate

Raguram's rule: **never write code without his approval.** Follow these steps every time.

## Steps

1. **Say what and why** (2–4 lines, simple English).
   - Which step from `docs/TASKS.md` this belongs to.
2. **Show the change** in the chat:
   - New file → the full file.
   - Existing file → a clear diff or the changed block with a few lines of context.
   - Command → the exact command.
   - Keep it small: aim for under ~30 new lines. Split bigger work into several approvals.
3. **Explain new ideas** using the `explain-python-for-java` skill (only the parts that are new to him).
4. **List the files** that will be created or changed.
5. **Ask exactly:** `Approve? (yes / change something / no)`
6. **Wait.**
   - Approval = a clear "yes", "approved", "go ahead", "do it".
   - A question, "looks good but…", or silence is **not** approval. Answer and ask again.
   - "Change something" → update the proposal and go back to step 2.
7. **After approval:** make exactly the approved change. Nothing extra (no "while I'm here" fixes).
8. **Log it:** add a `docs/DEV_LOG.md` entry with the `project-logs` skill.
9. **Commit only with a separate approval:** propose the commit message (format in `docs/CONVENTIONS.md`), show `git status`, wait for yes.

## Does NOT need approval

Reading files, searching, explaining, answering questions, running read-only commands (`--version`, `git status`, `uv run` of already-approved code).

## Never

- Never write a file "to save time" and ask afterwards.
- Never bundle unrelated changes into one approval.
- Never touch `.env` contents or print the API key.
