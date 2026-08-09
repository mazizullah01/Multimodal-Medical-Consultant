"""Build and wire the Gradio consultation app."""

import gradio as gr

from app.ui.layout import build_layout
from app.ui.theme import load_css


def build_app(process_inputs, clear_consultation):
    """Create the Blocks app with soft-clinical UI and bound callbacks."""
    with gr.Blocks(css=load_css(), title="AI Skin Specialist") as demo:
        components = build_layout()

        components["analyze_btn"].click(
            fn=process_inputs,
            inputs=[
                components["patient_audio"],
                components["patient_image"],
                components["patient_video"],
            ],
            outputs=[
                components["transcript"],
                components["response"],
                components["doctor_audio"],
                components["status"],
                components["steps"],
            ],
        )
        components["clear_btn"].click(
            fn=clear_consultation,
            inputs=[],
            outputs=[
                components["patient_audio"],
                components["patient_image"],
                components["patient_video"],
                components["transcript"],
                components["response"],
                components["doctor_audio"],
                components["status"],
                components["steps"],
            ],
            queue=False,
        )

    return demo
