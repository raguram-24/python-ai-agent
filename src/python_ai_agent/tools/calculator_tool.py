from typing import Any

from google.genai import types

CALCULATE_DECLARATION = types.FunctionDeclaration(
    name="calculate",
    description=(
        "Do exact arithmetic on two numbers: add, subtract, multiply or divide. "
        "Use this for any calculation instead of doing the maths yourself. "
        "Returns the result, or an error message."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "a": types.Schema(type=types.Type.NUMBER, description="First number"),
            "b": types.Schema(type=types.Type.NUMBER, description="Second number"),
            "operation": types.Schema(
                type=types.Type.STRING,
                enum=["add", "subtract", "multiply", "divide"],
                description="Operation to apply: a <operation> b",
            ),
        },
        required=["a", "b", "operation"],
    ),
)


def calculate(a: float, b: float, operation: str) -> dict[str, Any]:
    """Apply one arithmetic operation to a and b."""
    match operation:
        case "add":
            return {"result": a + b}
        case "subtract":
            return {"result": a - b}
        case "multiply":
            return {"result": a * b}
        case "divide":
            if b == 0:
                return {"error": "Cannot divide by zero"}
            return {"result": a / b}
        case _:
            return {"error": f"Unknown operation: {operation}"}
