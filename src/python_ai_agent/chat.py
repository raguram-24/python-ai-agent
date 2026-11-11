import os

import httpx2
from dotenv import load_dotenv
from google import genai
from google.genai import types

from python_ai_agent.agent import run_agent_turn
from python_ai_agent.tools import TOOL_DECLARATIONS

SYSTEM_PROMPT = (
    "You are a helpful assistant for a Java developer who is learning Python. "
    "Answer in at most 3 sentences."
)
REQUEST_TIMEOUT_MS = 30_000


def run_chat() -> None:
    load_dotenv()
    model = os.environ["GEMINI_MODEL"]
    max_tokens = int(os.environ["GEMINI_MAX_OUTPUT_TOKENS"])
    print(f"Using model: {model}. Type 'exit' to quit")
    history: list[types.Content] = []
    client = genai.Client(http_options=types.HttpOptions(timeout=REQUEST_TIMEOUT_MS))
    config = types.GenerateContentConfig(
        max_output_tokens=max_tokens,
        system_instruction=SYSTEM_PROMPT,
        tools=[types.Tool(function_declarations=TOOL_DECLARATIONS)],
    )
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        turn_start = len(history)
        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
        try:
            answer = run_agent_turn(client, model, config, history)
        except (httpx2.TimeoutException, RuntimeError) as error:
            del history[turn_start:]
            print(f"Error: {error}. Please try again.")
            continue
        print(f"Gemini: {answer}")
