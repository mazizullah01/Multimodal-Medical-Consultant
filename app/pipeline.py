"""Consultation pipeline: STT → doctor vision → TTS (no Gradio layout)."""

import gradio as gr

from app.doctor_brain import brain_of_the_doctor
from app.doctor_voice import convert_text_to_doctor_audio
from app.patient_voice import transcribe_patient_voice
from app.ui import markup


def process_inputs(audio_filepath, image_filepath, video_filepath, progress=gr.Progress()):
    """Transcribe the concern, review the image, and create the voice response."""
    if not audio_filepath:
        raise gr.Error("Please record or upload a short voice note describing your concern.")
    if not image_filepath:
        raise gr.Error("Please upload a clear photo of the affected skin area.")

    try:
        progress(0.15, desc="Transcribing your voice note")
        patient_text = transcribe_patient_voice(audio_filepath)

        progress(0.5, desc="Reviewing your skin photo")
        doctor_text = brain_of_the_doctor(
            patient_text=patient_text,
            image_filepath=image_filepath,
            video_filepath=video_filepath,
        )

        progress(0.82, desc="Preparing your audio response")
        doctor_audio = convert_text_to_doctor_audio(doctor_text)
        progress(1, desc="Consultation ready")
    except Exception as exc:
        raise gr.Error(f"We couldn't complete the consultation: {exc}") from exc

    return (
        patient_text,
        doctor_text,
        str(doctor_audio),
        markup.SUCCESS_STATUS_HTML,
        markup.STEPS_DONE_HTML,
    )


def clear_consultation():
    """Reset all consultation fields and step indicator."""
    return (
        None,
        None,
        None,
        "",
        "",
        None,
        markup.EMPTY_STATUS_HTML,
        markup.STEPS_IDLE_HTML,
    )
