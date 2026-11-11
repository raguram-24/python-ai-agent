from collections.abc import Callable
from typing import Any

from google.genai import types

from python_ai_agent.tools.calculator_tool import CALCULATE_DECLARATION, calculate
from python_ai_agent.tools.date_time_tool import (
    GET_CURRENT_TIME_DECLARATION,
    get_current_time,
)

TOOL_DECLARATIONS: list[types.FunctionDeclaration] = [
    GET_CURRENT_TIME_DECLARATION,
    CALCULATE_DECLARATION,
]

_TOOL_FUNCTIONS: dict[str, Callable[..., dict[str, Any]]] = {
    "get_current_time": get_current_time,
    "calculate": calculate,
}


def run_tool(name: str, args: dict[str, Any]) -> dict[str, Any]:
    """Run the tool the model asked for. Unknown names return an error result."""
    tool_function = _TOOL_FUNCTIONS.get(name)
    if tool_function is None:
        return {"error": f"Unknown tool: {name}"}
    try:
        return tool_function(**args)
    except TypeError as error:
        return {"error": f"Bad arguments for {name}: {error}"}
