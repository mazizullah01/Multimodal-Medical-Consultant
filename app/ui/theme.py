"""Load Gradio theme CSS and head scripts for the consultation UI."""

from pathlib import Path

_STYLES_PATH = Path(__file__).with_name("styles.css")


def load_css() -> str:
    return _STYLES_PATH.read_text(encoding="utf-8")


def load_head() -> str:
    return ""
