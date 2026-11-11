from google import genai
from google.genai import types

from python_ai_agent.tools import run_tool

MAX_TOOL_CALLS = 10


def _get_reply_content(response: types.GenerateContentResponse) -> types.Content:
    """Return the model's reply message, or raise if Gemini sent none."""
    if not response.candidates or response.candidates[0].content is None:
        raise RuntimeError(
            f"Gemini returned no reply (prompt_feedback ={response.prompt_feedback})"
        )
    return response.candidates[0].content


def run_agent_turn(
    client: genai.Client,
    model: str,
    config: types.GenerateContentConfig,
    history: list[types.Content],
) -> str:
    """Call Gemini and run the tools it asks for, until it answers with text."""
    tool_call_count = 0
    while True:
        response = client.models.generate_content(
            model=model, contents=history, config=config
        )
        history.append(_get_reply_content(response))
        if not response.function_calls:
            return response.text or ""
        tool_call_count += len(response.function_calls)
        if tool_call_count > MAX_TOOL_CALLS:
            raise RuntimeError(f"Stopped: more than {MAX_TOOL_CALLS} tool calls")
        response_parts: list[types.Part] = []
        for function_call in response.function_calls:
            print(f"[TOOL] : {function_call.name}({function_call.args})")
            result = run_tool(function_call.name or "", function_call.args or {})
            function_response = types.FunctionResponse(
                id=function_call.id, name=function_call.name, response=result
            )
            response_parts.append(types.Part(function_response=function_response))
        history.append(types.Content(role="user", parts=response_parts))
