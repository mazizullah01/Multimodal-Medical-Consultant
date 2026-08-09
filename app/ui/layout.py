"""Gradio layout building blocks."""

import gradio as gr

from app.ui import markup


def build_layout():
    """Build UI structure; returns dict of interactive components for wiring."""
    with gr.Row(elem_classes="app-layout"):
        with gr.Column(elem_classes="sidebar", scale=0):
            gr.HTML(markup.SIDEBAR_HTML)

        with gr.Column(elem_classes="main-area"):
            gr.HTML(markup.HEADER_HTML)

            with gr.Column(elem_classes="workspace"):
                steps = gr.HTML(markup.STEPS_IDLE_HTML)

                with gr.Row(elem_classes="consult-grid"):
                    with gr.Column(elem_classes=["consult-card", "input-card"]):
                        gr.HTML(markup.PATIENT_CARD_HEAD_HTML)
                        with gr.Column(elem_classes="input-body"):
                            gr.HTML(markup.VOICE_FIELD_HTML)
                            patient_audio = gr.Audio(
                                sources=["microphone"],
                                type="filepath",
                                label="Patient Voice",
                                waveform_options=gr.WaveformOptions(
                                    waveform_color="#a9d7f1",
                                    waveform_progress_color="#087dbf",
                                    show_recording_waveform=True,
                                    show_controls=False,
                                ),
                                elem_classes="voice-recorder",
                            )
                            gr.HTML(markup.IMAGE_FIELD_HTML)
                            patient_image = gr.Image(
                                type="filepath",
                                label="Skin Image",
                                elem_classes="upload-media",
                            )
                            gr.HTML(markup.VIDEO_FIELD_HTML)
                            patient_video = gr.Video(
                                label="Skin Video",
                                elem_classes=["upload-media", "video-media"],
                            )
                        with gr.Column(elem_classes="actions"):
                            analyze_btn = gr.Button(
                                "Analyze Consultation",
                                variant="primary",
                                elem_classes="analyze-btn",
                            )
                            clear_btn = gr.Button("Clear", elem_classes="clear-btn")

                    with gr.Column(elem_classes="consult-card"):
                        gr.HTML(markup.RESPONSE_CARD_HEAD_HTML)
                        with gr.Column(elem_classes="result-body"):
                            status = gr.HTML(markup.EMPTY_STATUS_HTML)
                            transcript = gr.Textbox(
                                label="Patient transcript",
                                lines=2,
                                interactive=False,
                                elem_classes="output-box",
                            )
                            response = gr.Textbox(
                                label="Specialist guidance",
                                lines=6,
                                interactive=False,
                                elem_classes="output-box",
                            )
                            doctor_audio = gr.Audio(
                                label="Doctor voice response",
                                interactive=False,
                                elem_classes=["output-box", "audio-output"],
                            )
                            gr.HTML(markup.DISCLAIMER_HTML)

    return {
        "steps": steps,
        "patient_audio": patient_audio,
        "patient_image": patient_image,
        "patient_video": patient_video,
        "analyze_btn": analyze_btn,
        "clear_btn": clear_btn,
        "status": status,
        "transcript": transcript,
        "response": response,
        "doctor_audio": doctor_audio,
    }
