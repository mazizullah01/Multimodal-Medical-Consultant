"""Launch the AI Skin Specialist Gradio app."""

from app.main import app

if __name__ == "__main__":
    app.queue().launch()
