# LEARNING — what I need to learn during the project

## Why "learn while building"

- I already know backend engineering. What's new is **Python syntax** and **a few AI ideas**. Both are small.
- Learning theory first is slow and doesn't stick. A concept clicks when I **see it in my own code**.
- So each step teaches only what that step needs (just-in-time). Nothing more.

### How learning works in each step

1. **Before coding (10–15 min):** read the "Learn" list for the step below. Claude Code explains each item with a Java comparison.
2. **While coding:** Claude Code proposes small pieces. I ask "why?" for every line I don't understand. I don't approve code I can't explain.
3. **After the step (10 min):** I explain the step back in my own words (out loud or written). Claude Code checks it.
4. **Log it:** an entry in `docs/LEARNING_LOG.md`: what I learned, Python vs Java notes, mistakes, open questions.
5. **Save the best notes** to Second Brain if they are worth keeping.

### Rules

- If I can't explain a line, it doesn't go in.
- One new idea at a time.
- Mistakes are good. Write them in the learning log.

## Already known (no prep needed)

HTTP, REST, JSON, loops, error handling, env vars/secrets, Git, Docker, testing ideas.

## What to learn per step

| Step | Python to learn | AI / agent concepts to learn |
|---|---|---|
| 0 Setup | What `uv`, `.venv`, `pyproject.toml` are (vs Maven, `pom.xml`) | API key, billing, spending limits |
| 1 One call | `import`, variables (no types needed), functions with named arguments, f-strings, `os.environ` | Messages, roles (`user`/`assistant`), `max_tokens`, tokens, `stop_reason`, response object |
| 2 Conversation | Lists and dicts, `append`, `while` loop, `input()`, `if`/`break` | Model is stateless → resend history; system prompt; context window; cost grows with history |
| 3 One tool | Functions, return values, dicts as JSON, `json` module | Tool definitions, JSON Schema, `tool_use` / `tool_result`, tool descriptions matter |
| 4 Agent loop | Loop control, functions calling functions, modules/packages, type hints, dataclasses | The agent loop, loop cap, choosing between tools |
| 5 File tool | `pathlib`, reading files, `try`/`except` (vs try/catch), custom exceptions | Safety: safe folder, path traversal, errors as tool results |
| 6 MCP | Decorators (like Java annotations), `async` basics | MCP: client/server, tools, resources, FastMCP |
| 7 Memory/RAG | Working with lists of results, simple classes | Embeddings, similarity search, retrieval, chunking |
| 8 Evals/security | `pytest` (vs JUnit), fixtures, parametrize | Evals, non-determinism, prompt injection, sandboxing |

## Python vs Java — quick reference (grows during the project)

| Java | Python | Notes |
|---|---|---|
| Maven / Gradle | `uv` | `uv add x` ≈ add a dependency |
| `pom.xml` | `pyproject.toml` | Project + dependencies |
| `~/.m2` (shared, many versions) | `.venv/` (per project) | One version per package, so each project gets its own folder. Never commit `.venv/` |
| Resolved versions / lock | `uv.lock` | Exact versions. Commit it |
| `mvn install` / `npm ci` | `uv sync` | Install everything from the lock file |
| `application-local.properties` (ignored) | `.env` (ignored) | Real secrets, loaded with `python-dotenv` |
| `application.properties` with `CHANGE_ME` | `.env.example` | Committed template, placeholders only |
| `mvn exec:java` + main class | `uv run <script>` + `[project.scripts]` | |
| `Integer.parseInt(s)` | `int(s)` | Raises `ValueError` if not a number |
| `list.get(0)` | `my_list[0]` | |
| Builder: `.model(m).contents(c)` | Keyword arguments: `model=m, contents=c` | Order doesn't matter; trailing comma allowed |
| `scanner.nextLine()` | `input("You: ")` | Returns a `str` |
| `s.trim().toLowerCase()` | `s.strip().lower()` | |
| `private static final String X = ...;` | `X = ...` (UPPER_CASE) | Constant by convention only, not enforced |
| `x != null ? x : 0` | `x or 0` | None-safe default |
| `String name = "Ram";` | `name = "Ram"` | No type needed (type hints optional: `name: str = "Ram"`) |
| `List<String>` | `list[str]` | `["a", "b"]` |
| `Map<String, Object>` | `dict` | `{"role": "user", "content": "hi"}` |
| `{ ... }` blocks | indentation | Indentation **is** the syntax |
| `try { } catch (E e) { }` | `try:` / `except E as e:` | |
| `null` | `None` | |
| `System.getenv("X")` | `os.environ["X"]` | Raises `KeyError` if missing |
| `@Annotation` | `@decorator` | Similar look, different mechanism |
| JUnit | `pytest` | |
| `this` | `self` | Written explicitly as the first method parameter |

## Learning resources (to verify / add as I go)

- Anthropic docs: https://docs.claude.com
- Python official tutorial: https://docs.python.org/3/tutorial/
- Vault pages: [[AI Agents - What Is an Agent]], [[AI Agents - Before You Start]], [[AI Agents - Learning Path]]
