---
name: explain-python-for-java
description: Use whenever showing or explaining Python code to Raguram, a Java/Spring Boot developer who is new to Python. Explains new lines in simple English with Java comparisons.
---

# Explain Python for a Java developer

Raguram knows Java, Spring Boot, TypeScript and NestJS well. He is new to Python. Teach, don't just hand over code.

## How to explain

1. **Only explain what's new.** Skip things already covered (check `docs/LEARNING_LOG.md`).
2. **Line by line for new ideas**: what the line does, in one simple sentence.
3. **Compare with Java** (or TypeScript) when it helps:

   | Python | Java |
   |---|---|
   | `client = Anthropic()` | `var client = new Anthropic();` (no `new` in Python) |

4. **Point out traps** Java developers hit:
   - Indentation is the syntax (no `{}`).
   - No `new`; `self` is explicit; `None` not `null`.
   - Mutable default arguments (`def f(items=[])`) are shared between calls.
   - `==` compares values; `is` compares identity (use `is None`).
   - Dicts use `["key"]` (raises `KeyError`) or `.get("key")` (returns `None`).
5. **Connect to AI concepts** when the line is about the agent (e.g. "this is the history we resend because the model has no memory").
6. **End with one check question**, e.g. "What happens if `.env` has no `CLAUDE_MODEL`?"

## Style

- Simple English, short sentences.
- Small examples, not big ones.
- If unsure about a library detail, say so and point to the docs. Don't guess.
