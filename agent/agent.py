# agent/agent.py
# The orchestrator — the only file that imports from all other modules.
# It sequences the calls and exposes clean entry points to the outside world.

from agent.image import load_from_path, load_from_bytes
from agent.prompt import build_messages
from agent.llm import call_and_parse


def run_from_path(image_path: str, instruction: str, context: str = "") -> dict:
    """
    Run the agent with an image file path.
    Use this for CLI scripts or programmatic/testing use.
    """
    base64_image, media_type = load_from_path(image_path)
    messages = build_messages(base64_image, media_type, instruction, context)
    return call_and_parse(messages)


def run_from_bytes(image_bytes: bytes, filename: str, instruction: str, context: str = "") -> dict:
    """
    Run the agent with raw image bytes.
    Use this when Streamlit passes an uploaded file directly.
    """
    base64_image, media_type = load_from_bytes(image_bytes, filename)
    messages = build_messages(base64_image, media_type, instruction, context)
    return call_and_parse(messages)