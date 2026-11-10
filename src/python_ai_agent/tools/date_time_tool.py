from datetime import datetime

from google.genai import types

GET_CURRENT_TIME_DECLARATION = types.FunctionDeclaration(
    name="get_current_time",
    description=(
        "Get the current local date and time on the user's computer. "
        "Returns the time in ISO 8601 format with the time zone offset, "
        "and the weekday name. "
        "Use this whenever the user asks for current time, date or day. "
        "Takes no arguments."
    ),
)


def get_current_time() -> dict[str, str]:
    """Return the current local date, time and weekday."""
    now = datetime.now().astimezone()
    return {
        "current_time": now.isoformat(timespec="seconds"),
        "weekday": now.strftime("%A"),
    }
