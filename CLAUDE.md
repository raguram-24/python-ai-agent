# CLAUDE.md — Python AI Agent (learning project)

Owner: Raguram — backend developer (Java, Spring Boot, TypeScript, NestJS, Docker, Kubernetes, AWS), **new to Python**.

Goal: learn how AI agents work by building one step by step in Python with the Gemini API (free tier). Claude may be added later behind an `LLMClient` interface.
Learning comes first. Working code is the by-product.

Read these before doing anything:

| File | What it is |
|---|---|
| `docs/TASKS.md` | The plan: steps, tasks, "done when", current status |
| `docs/LEARNING.md` | What Raguram must learn in each step (Python + AI concepts) |
| `docs/CONVENTIONS.md` | Naming rules + commit message format |
| `docs/DEV_LOG.md` | Log of every change made to the project |
| `docs/LEARNING_LOG.md` | Log of what Raguram learned in each step |

## Rule 1: never write code without approval (most important)

Raguram must approve every change before it is written. No exceptions, even for "small" changes.

1. **Explain** what you want to do and why, in simple English.
2. **Show** the exact code or change in the chat (full file, or a clear diff).
3. **Explain the new parts**: every new Python idea, with a Java comparison where it helps.
4. **Ask**: "Approve? (yes / change something / no)".
5. **Wait.** Only a clear "yes" / "approved" / "go ahead" counts. A question back is NOT approval.
6. Only then write the file, then update `docs/DEV_LOG.md`.

This applies to: code files, config (`pyproject.toml`, `.env`, `.gitignore`), installs (`uv add`), deletes, renames, and git commits.
Read-only work (reading files, explaining, running `--version`) does not need approval.

If Raguram writes the code himself, review it and explain. Don't rewrite it unless he asks.

## Rule 2: teach while building

- Use the `explain-python-for-java` skill style: explain each new line, compare it with Java.
- Never dump big code. One small piece at a time (aim for under ~30 new lines per change).
- After each step, ask Raguram to explain it back in his own words, then fill `docs/LEARNING_LOG.md`.
- If he copies something he doesn't understand, stop and explain.

## Rule 3: keep the logs

- Every approved change → one entry in `docs/DEV_LOG.md` (see the `project-logs` skill).
- Every finished step → one entry in `docs/LEARNING_LOG.md`.
- Every commit → follows the format in `docs/CONVENTIONS.md`.
- Update the status column in `docs/TASKS.md` when a task or step is done.

## Rule 4: safety

- API key lives only in `.env`. `.env` must be in `.gitignore`. Never print, log or commit the key. `.env.example` (placeholders only) is committed.
- Gemini key must stay on the **free tier** (no billing linked). Free-tier prompts may be used by Google — never send private vault notes or personal data.
- Never hard-code secrets.
- Agent tools: restrict to a safe folder, cap the loop (max 10 tool calls), confirm before any dangerous tool (shell, delete, write outside the safe folder).
- Don't guess facts like model IDs, free-tier limits or prices — say "verify" and point to the provider's docs (ai.google.dev for Gemini, docs.claude.com for Claude).

## Tech

- Python 3.12+, `uv` for env and packages (`uv add`, `uv run`).
- Packages: `google-genai`, `python-dotenv`, `anthropic` (installed, unused until Claude is added).
- Formatter / linter: Ruff. Type hints everywhere.
- Model name comes from `.env` (`GEMINI_MODEL`, currently `gemini-3.8-flash`), never hard-coded.

## Skills in this project (`.claude/skills/`)

| Skill | Use when |
|---|---|
| `approval-gate` | Before ANY change to a file, install, or commit |
| `start-build-step` | Starting a new step from `docs/TASKS.md` |
| `explain-python-for-java` | Explaining any Python code to Raguram |
| `project-logs` | Writing DEV_LOG, LEARNING_LOG entries and commit messages |
| `add-agent-tool` | Adding a new tool to the agent (Step 3 onwards) |

## Second Brain

Project notes also live in Raguram's Obsidian vault: `~/Documents/Second_Brain/wiki/projects/personal/python-ai-agent/story.md`.
Don't edit the vault from Claude Code unless Raguram asks. Never touch `raw/` in the vault.
