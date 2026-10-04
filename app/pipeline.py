"""Consultation pipeline: STT → doctor vision → TTS (without Gradio layout)."""

import logging

import gradio as gr

from app.doctor_brain import brain_of_the_doctor
from app.doctor_voice import convert_text_to_doctor_audio
from app.patient_voice import transcribe_patient_voice
from app.ui import markup

logger = logging.getLogger(__name__)


def _attention(title, message, steps_html):
    """Show one notice and clear any previous consultation results."""
    return (
        "",
        "",
        None,
        markup.notice_html(title, message, blocked=True),
        steps_html,
    )


def _explain_failure(stage, exc):
    """Turn a pipeline failure into a short, patient-facing notice."""
    status = getattr(exc, "status_code", None)
    detail = str(exc).lower()

    if status in (401, 403) or "api key" in detail or "invalid_api_key" in detail:
        return (
            "The consultation service is not ready",
            "The app could not sign in to the analysis service. Check the API keys, then try again.",
        )
    if status == 429 or "rate limit" in detail or "too many requests" in detail:
        return (
            "Please wait a moment",
            "The consultation service is busy right now. Wait a few seconds, then analyze again.",
        )
    if stage == "voice":
        return (
            "We couldn't understand the voice note",
            "Record it again somewhere quiet, speak for a few seconds, and then analyze.",
        )
    if stage == "audio":
        return (
            "The spoken reply could not be created",
            "Your written guidance is below. Analyze again if you would like it read aloud.",
        )
    if "video" in detail or "ffmpeg" in detail or "frames" in detail:
        return (
            "This video could not be opened",
            "Use a short MP4 or MOV clip, or upload a clear photo instead.",
        )
    if status == 404 or "does not exist" in detail or "model_not_found" in detail:
        return (
            "Analysis is temporarily unavailable",
            "The consultation model could not be reached. Please try again in a moment.",
        )
    if "empty response" in detail:
        return (
            "No guidance was returned",
            "Try again with a clearer photo or a shorter video of the affected area.",
        )
    return (
        "We couldn't complete this consultation",
        "Please try again with a short voice note and a clear photo or video.",
    )


def _failure(stage, exc, patient_text, doctor_text, doctor_audio):
    logger.exception("Consultation failed during %s", stage)
    title, message = _explain_failure(stage, exc)
    produced = bool((patient_text or "").strip() or (doctor_text or "").strip())
    return (
        patient_text or "",
        doctor_text or "",
        str(doctor_audio) if doctor_audio else None,
        markup.notice_html(title, message, blocked=not produced),
        markup.STEPS_IDLE_HTML,
    )


def process_inputs(audio_filepath, image_filepath, video_filepath, progress=gr.Progress()):
    """Transcribe the concern, review the photo or video, and create the voice response."""
    if not audio_filepath:
        return _attention(
            "Voice note needed",
            "Record a short description of your skin concern, then choose Analyze Consultation.",
            markup.STEPS_IDLE_HTML,
        )
    if not image_filepath and not video_filepath:
        return _attention(
            "A photo or video is needed",
            "Add a clear photo or a short clip of the affected skin, then analyze again.",
            markup.STEPS_NEED_VISUAL_HTML,
        )

    if video_filepath and image_filepath:
        review_label = "Reviewing your photo and video"
    elif video_filepath:
        review_label = "Reviewing your skin video"
    else:
        review_label = "Reviewing your skin photo"

    patient_text = ""
    doctor_text = ""
    doctor_audio = None
    stage = "voice"
    try:
        progress(0.15, desc="Transcribing your voice note")
        patient_text = (transcribe_patient_voice(audio_filepath) or "").strip()
        if not patient_text:
            return _attention(
                "We couldn't hear a concern",
                "Record the voice note again somewhere quiet, and speak for a few seconds.",
                markup.STEPS_IDLE_HTML,
            )

        stage = "review"
        progress(0.5, desc=review_label)
        doctor_text = brain_of_the_doctor(
            patient_text=patient_text,
            image_filepath=image_filepath,
            video_filepath=video_filepath,
        )

        stage = "audio"
        progress(0.85, desc="Preparing your audio response")
        doctor_audio = convert_text_to_doctor_audio(doctor_text)
        progress(1, desc="Consultation ready")
    except Exception as exc:
        return _failure(stage, exc, patient_text, doctor_text, doctor_audio)

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
