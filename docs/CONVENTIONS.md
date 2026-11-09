# CONVENTIONS — naming and commits

## 1. Naming (Python standard = PEP 8)

| Thing | Style | Example | Java equivalent |
|---|---|---|---|
| Files / modules | `snake_case.py` | `claude_client.py` | `ClaudeClient.java` |
| Packages (folders) | `snake_case`, short | `agent/`, `tools/` | `com.raguram.agent` |
| Functions / methods | `snake_case`, verb first | `send_message()`, `run_tool()` | `sendMessage()` |
| Variables | `snake_case`, clear nouns | `messages`, `tool_result` | `toolResult` |
| Classes | `PascalCase` | `ClaudeClient`, `ToolRegistry` | same |
| Constants | `UPPER_SNAKE_CASE` | `MAX_TOOL_CALLS = 10` | `static final` |
| Private (internal) | leading `_` | `_build_request()` | `private` |
| Booleans | `is_` / `has_` / `should_` | `is_done`, `has_tools` | same idea |
| Env vars | `UPPER_SNAKE_CASE` | `ANTHROPIC_API_KEY`, `CLAUDE_MODEL` | same |

### Agent-specific names

| Thing | Rule | Example |
|---|---|---|
| Tool names (sent to the model) | `snake_case`, `verb_noun` | `get_current_time`, `read_file`, `search_notes` |
| Tool functions in code | same name as the tool | `def read_file(path: str) -> str:` |
| Tests | `tests/test_<module>.py`, `test_<what>_<expected>()` | `test_read_file_outside_safe_folder_is_rejected()` |
| Prompts in files | `prompts/<agent>_system.md` | `prompts/notes_agent_system.md` |

### Rules

- No abbreviations except well-known ones (`id`, `url`, `api`).
- No single-letter names except short loop counters.
- Names say **what**, not **how** (`messages`, not `msg_list_arr`).
- Type hints on every function: `def send_message(text: str) -> str:`.

## 2. Git branches

`<type>/step-NN-short-description` → `feat/step-01-first-call`, `feat/step-03-time-tool`, `fix/step-03-tool-timeout`

- `<type>` = same types as commits: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`
- `step-NN` = the step from `docs/TASKS.md` (acts like a ticket ID)
- short description = lowercase words joined with `-`

## 3. Commit messages

Format (Conventional Commits + step number):

```
<type>(step-NN): <short summary in present tense, max ~60 chars>

<optional body: what and why, wrapped at ~72 chars>
```

| Type | Use for |
|---|---|
| `feat` | New behaviour (a new tool, the loop) |
| `fix` | Bug fix |
| `refactor` | Code change with no behaviour change |
| `test` | Adding or changing tests |
| `docs` | Docs and logs only |
| `chore` | Setup, dependencies, config |

Examples:

```
chore(step-00): project setup with uv
feat(step-01): send first message to Claude and print usage
feat(step-03): add get_current_time tool
fix(step-04): stop loop after 10 tool calls
docs(step-02): add learning log for conversations
```

Rules:

- One logical change per commit.
- Commit only after Raguram approves (see `CLAUDE.md`, Rule 1).
- Never commit `.env` or any key. Check `git status` before every commit.
