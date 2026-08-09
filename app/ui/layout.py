"""Gradio layout building blocks."""

import gradio as gr

from app.ui import markup


def build_layout():
    """Build centered single-page UI; returns interactive components for wiring."""
    with gr.Column(elem_classes="app-shell"):
        gr.HTML(markup.HEADER_HTML)

        with gr.Column(elem_classes="workspace"):
            steps = gr.HTML(markup.STEPS_IDLE_HTML)
            gr.HTML(markup.INPUTS_INTRO_HTML)

            with gr.Row(elem_classes="media-grid"):
                with gr.Column(elem_classes=["media-tile", "media-tile-voice"]):
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
                with gr.Column(elem_classes=["media-tile", "media-tile-image"]):
                    gr.HTML(markup.IMAGE_FIELD_HTML)
                    patient_image = gr.Image(
                        type="filepath",
                        label="Skin Image",
                        elem_classes="upload-media",
                    )
                with gr.Column(elem_classes=["media-tile", "media-tile-video"]):
                    gr.HTML(markup.VIDEO_FIELD_HTML)
                    patient_video = gr.Video(
                        label="Skin Video",
                        elem_classes=["upload-media", "video-media"],
                    )

            with gr.Row(elem_classes="actions"):
                analyze_btn = gr.Button(
                    "Analyze Consultation",
                    variant="primary",
                    elem_classes="analyze-btn",
                    scale=4,
                )
                clear_btn = gr.Button("Clear", elem_classes="clear-btn", scale=1)

            with gr.Column(elem_classes=["consult-card", "response-card"]):
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
                        autoplay=True,
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
