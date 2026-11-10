import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from python_ai_agent.tools.date_time_tool import (
    GET_CURRENT_TIME_DECLARATION,
    get_current_time,
)

SYSTEM_PROMPT = (
    "You are a helpful assistant for a Java developer who is learning Python. "
    "Answer in at most 3 sentences."
)


def run_chat() -> None:
    load_dotenv()
    model = os.environ["GEMINI_MODEL"]
    max_tokens = int(os.environ["GEMINI_MAX_OUTPUT_TOKENS"])
    print(f"Using model: {model}. Type 'exit' to quit")
    history: list[types.Content] = []
    client = genai.Client()
    config = types.GenerateContentConfig(
        max_output_tokens=max_tokens,
        system_instruction=SYSTEM_PROMPT,
        tools=[types.Tool(function_declarations=[GET_CURRENT_TIME_DECLARATION])],
    )
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        history.append(types.Content(role="user", parts=[types.Part(text=user_input)]))
        response = client.models.generate_content(
            model=model, contents=history, config=config
        )
        history.append(response.candidates[0].content)
        if response.function_calls:
            function_call = response.function_calls[0]
            print(f"[TOOL] : {function_call.name} called")
            function_response = types.FunctionResponse(
                id=function_call.id,
                name=function_call.name,
                response=get_current_time(),
            )
            history.append(
                types.Content(
                    role="user", parts=[types.Part(function_response=function_response)]
                )
            )
            response = client.models.generate_content(
                model=model, contents=history, config=config
            )
            history.append(response.candidates[0].content)
        print(f"Gemini: {response.text}")
