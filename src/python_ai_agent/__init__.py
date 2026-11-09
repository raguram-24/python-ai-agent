import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main() -> None:
    load_dotenv()
    model = os.environ["GEMINI_MODEL"]
    max_tokens = int(os.environ["GEMINI_MAX_OUTPUT_TOKENS"])
    print(f"Using model: {model}")  # 50

    client = genai.Client()
    response = client.models.generate_content(
        model=model,
        contents="What is my name?",
        config=types.GenerateContentConfig(max_output_tokens=max_tokens),
    )
    print(f"Reply: {response.text}")
    print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Reply Tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Finish reason: {response.candidates[0].finish_reason}")
    print(f"Total tokens:  {response.usage_metadata.total_token_count}")
    print(f"Thinking tokens: {response.usage_metadata.thoughts_token_count}")
