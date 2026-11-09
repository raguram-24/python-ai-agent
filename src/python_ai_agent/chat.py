import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

SYSTEM_PROMPT = (
    "You are a helpful assistant for a Java developer who is learning Python. "
    "Answer in at most 3 sentences."
)


def run_chat() -> None:
    load_dotenv()
    model = os.environ["GEMINI_MODEL"]
    max_tokens = int(os.environ["GEMINI_MAX_OUTPUT_TOKENS"])
    print(f"Using model: {model}. Type 'exit' to quit")
    total_response_tokens: int = 0
    history: list[types.Content] = []
    client = genai.Client()
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
        response = client.models.generate_content(
            model=model,
            contents=history,
            config=types.GenerateContentConfig(
                max_output_tokens=max_tokens, system_instruction=SYSTEM_PROMPT
            ),
        )
        history.append(
            types.Content(role="model", parts=[types.Part(text=response.text)])
        )
        total_response_tokens = (
            total_response_tokens + response.usage_metadata.candidates_token_count
        )
        print(f"Gemini: {response.text}")
        print(f"Response Tokens : {response.usage_metadata.candidates_token_count}")
        print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Total Response tokens: {total_response_tokens}")
