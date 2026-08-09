"""Load Gradio theme CSS for the consultation UI."""

from pathlib import Path

_STYLES_PATH = Path(__file__).with_name("styles.css")


def load_css() -> str:
    return _STYLES_PATH.read_text(encoding="utf-8")
