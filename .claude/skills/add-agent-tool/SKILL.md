---
name: add-agent-tool
description: Use when adding a new tool to the agent (Step 3 onwards) - designing the tool's name, description and JSON Schema, writing the function, handling errors, and testing it safely.
---

# Add an agent tool

A tool = a function I write + a definition that tells the model when and how to use it. The model only *asks*; our code runs it.

## Checklist (each item goes through `approval-gate`)

1. **Purpose:** one sentence. One tool does one thing.
2. **Name:** `snake_case`, `verb_noun` (`get_current_time`, `read_file`). Same name for the Python function.
3. **Description:** written for the model — what it does, when to use it, when NOT to use it, what it returns. Good descriptions are the main way to make the model choose correctly.
4. **Input schema:** JSON Schema with types, `required` fields, and a description per field. Keep inputs few and simple.
5. **Function:** type hints, returns a string (or JSON-serialisable data). No printing secrets.
6. **Errors:** catch expected errors and return a clear error message as the tool result (so the model can recover). Don't crash the loop.
7. **Safety check:**
   - Files → only inside the configured safe folder; block `..` path traversal; read-only unless approved.
   - Shell / delete / write / network → ask Raguram for confirmation at runtime before running.
   - Large outputs → truncate.
8. **Register:** add it to the tools list the loop sends to Claude.
9. **Try it:** a prompt that should use the tool, and one that should NOT. Check the model's choice.
10. **Test:** a `pytest` test for the function itself (from Step 8, or earlier if Raguram wants).
11. **Log:** DEV_LOG entry + update `docs/TASKS.md`.

## Explain to Raguram

- Where the tool definition goes in the request, and what the `tool_use` and `tool_result` blocks look like.
- Java comparison: the definition is like an OpenAPI spec for one endpoint; the function is the controller method.
