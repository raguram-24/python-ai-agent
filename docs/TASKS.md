# TASKS — what we are going to do

Project: **Python AI Agent** (learning project) · Owner: Raguram · Created: 2026-11-09

## The big picture

We build **one AI agent**, step by step, in Python, using the Claude API.
Each step adds one idea. By Step 4 it is a real agent (model + tools + loop).
After that we grow it (files, MCP, memory, evals), then build **specialist agents one by one**, and finally an **orchestrator** that ties them into a suite.

```
Step 0–1   setup + one call        → "it talks"
Step 2     conversation            → "it remembers (because I resend history)"
Step 3–4   tool + loop             → "it acts"  = first real agent
Step 5–8   files, MCP, memory, evals → "it is useful and safe"
Later      specialist agents + orchestrator → the suite
```

How we work (see `CLAUDE.md`):

- Claude Code **never writes code without Raguram's approval**.
- Every step: learn the idea (`docs/LEARNING.md`) → plan → propose code → approve → write → run → log.
- Every change → `docs/DEV_LOG.md`. Every finished step → `docs/LEARNING_LOG.md`.

Status values: `todo` · `doing` · `done` · `parked`

## Steps overview

| # | Step | Status | Done when |
|---|---|---|---|
| 0 | Setup | done | `uv run` works, API key in `.env`, `.env` ignored by git |
| 1 | Call Gemini once | done | Reply, `finish_reason` and token counts printed |
| 2 | Keep a conversation going | done | Multi-turn chat in the terminal; type `exit` to quit |
| 3 | Add one tool | done | Ask "what time is it?" → model asks for the tool → my code runs it → answer |
| 4 | Agent loop | todo | Loop runs tools until the model stops asking for one; hard cap of 10 tool calls |
| 5 | File-reading tool | todo | Agent reads files only inside one safe folder; errors handled |
| 6 | MCP server | todo | Second Brain exposed as an MCP server and used by the agent |
| 7 | Memory / RAG | todo | Agent answers questions from vault notes it retrieved |
| 8 | Evals + security | todo | Small eval set runs; prompt-injection test cases pass |
| 9 | (Optional) Read OpenClaw source | parked | Comparison notes written |
| 10 | (Later) Rebuild in Java with Spring AI | parked | Same agent working in Spring Boot |

## Step details

### Step 0 — Setup
Raguram runs these himself (Claude Code only explains):

- [x] `python3 --version` → 3.12+ (`brew install python@3.12` if not) — have 3.14.7
- [x] `brew install uv` — have 0.13.7
- [x] In this folder: `uv init --package` (created `pyproject.toml`, `.python-version`, `src/python_ai_agent/__init__.py`, `README.md`, `.gitignore`, git repo)
- [x] `uv add anthropic python-dotenv` — anthropic 2.6.0, python-dotenv 1.2.4; `uv run python-ai-agent` works
- [x] Create Gemini API key at aistudio.google.com — **free tier, no billing linked** (Claude dropped: no budget for paid API)
- [x] Create `.env` from `.env.example`: `GEMINI_API_KEY=...`, `GEMINI_MODEL=gemini-3.8-flash`
- [x] Add `.env` to `.gitignore`, then check with `git status` that `.env` is NOT listed
- [x] `uv add google-genai` (Gemini SDK); `anthropic` kept for later
- [x] VS Code: "Python: Select Interpreter" → `.venv`
- [x] First commit: `feat(step-00): project setup` (82e4743), pushed to github.com/raguram-24/python-ai-agent

### Step 1 — Call Gemini once
- [x] Understand: client, `generate_content`, roles (`user` / `model`), `max_output_tokens`, response object (verify names in Google's SDK docs)
- [x] Write the code in `src/python_ai_agent/__init__.py` (run with `uv run python-ai-agent`): load `.env`, create client, send one message, print text + `finish_reason` + token counts
- [x] Experiment: `max_output_tokens=20` → see `finish_reason = MAX_TOKENS` (used 50 via `GEMINI_MAX_OUTPUT_TOKENS`)
- [x] Experiment: ask a follow-up in a second run → see it has no memory

### Step 2 — Conversation
- [x] Understand: model is stateless; history = a list of `types.Content` messages I resend
- [x] `while` loop reading `input()`, appending user + model messages
- [x] Add a system prompt
- [x] Print token usage per turn → see cost grow as history grows

### Step 3 — One tool
- [x] Understand: tool definition (name, description, JSON Schema), `function_call` / `function_response` parts
- [x] Tool `get_current_time` (use the `add-agent-tool` skill)
- [x] Handle a `function_call` in the response once — tool returns time + weekday

### Step 4 — Agent loop
- [ ] Understand: the agent loop, why it needs a cap
- [ ] Loop until the response has no `function_call`; max 10 tool calls; clean error if cap hit
- [ ] Second tool (e.g. `calculate`) → see the model choose between tools
- [ ] Organise the modules inside `src/python_ai_agent/` (structure decided and approved at this step)

### Step 5 — File-reading tool
- [ ] Tools `list_files`, `read_file` restricted to one safe folder (path traversal blocked)
- [ ] Errors returned to the model as tool results, not crashes

### Step 6 — MCP server
- [ ] Understand MCP (client, server, tools, resources)
- [ ] Build an MCP server with FastMCP exposing vault search/read (read-only)

### Step 7 — Memory / RAG
- [ ] Understand embeddings + retrieval
- [ ] Search vault notes and feed the top results to the model

### Step 8 — Evals + security
- [ ] Eval set: questions + expected behaviour; run and score
- [ ] Prompt-injection cases (e.g. a note saying "ignore your rules")
- [ ] Confirm-before-dangerous-tool check

## Parked ideas (decide after Step 4)

- First specialist agent: Money assistant (everyday use, links to Expense Tracker) **or** Unit-test agent (Java/Spring Boot).
- Local model via Ollama behind an `LLMClient` interface (privacy option).
- Agent suite with an orchestrator (final goal).
- Try Gemini Interactions API (`client.interactions.create`) after building the loop by hand.
- Add a request timeout (`types.HttpOptions(timeout=30_000)`) — `gemini-3.8-flash` hung >1 min in Step 1. Do before the Step 4 loop at the latest.
- Add Ruff as a dev dependency (`uv add --dev ruff`) if we set up CI — for now Ruff runs only via the VS Code extension.
