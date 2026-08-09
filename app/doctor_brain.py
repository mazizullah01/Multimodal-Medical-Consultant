import base64
import os
import re
from io import BytesIO

from dotenv import load_dotenv
from groq import Groq
from PIL import Image


load_dotenv()


def encode_image_for_groq(filepath):
    image = Image.open(filepath)
    image.thumbnail((1024, 1024))

    buffer = BytesIO()
    image.convert("RGB").save(buffer, format="JPEG", quality=75)
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def _extract_doctor_text(message):
    """Return speakable patient-facing text from a Groq chat message."""
    content = (message.content or "").strip()
    if content:
        return content

    # Reasoning models sometimes leave content empty when the budget is used up
    # by thinking, or when only reasoning is populated.
    reasoning = getattr(message, "reasoning", None) or ""
    reasoning = reasoning.strip()
    if not reasoning:
        return ""

    # Prefer a clear final answer section if the model labeled one.
    for marker in ("Final answer:", "Patient response:", "Response:"):
        if marker.lower() in reasoning.lower():
            idx = reasoning.lower().rfind(marker.lower())
            tail = reasoning[idx + len(marker) :].strip()
            if tail:
                return tail

    # Last resort: last non-empty line of reasoning (often the spoken answer).
    lines = [line.strip() for line in reasoning.splitlines() if line.strip()]
    return lines[-1] if lines else ""


def _sanitize_for_speech(text):
    # Drop markdown/noise that confuses TTS and sounds unnatural aloud.
    text = re.sub(r"[*_`#\[\](){}]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in .env or environment")

    if not image_filepath:
        raise ValueError("Groq vision requires an image. Please upload a skin image.")

    # Groq vision does not accept video here. When the UI passes both image and
    # video, this uses the same image as the visual input and ignores the video.
    image_data = encode_image_for_groq(image_filepath)

    prompt = (
        "You are a confident, natural doctor specializing in skin care. Speak with the reassurance, clarity, and authority of a real doctor. "
        "Limit your entire response to two or three sentences maximum. "
        "If the patient has provided a video, explain that you are reviewing the uploaded image because this model cannot process video directly. "
        "Do not use any special characters, symbols, asterisks, or markdown formatting in your response because it will be converted directly to audio.\n\n"
        f"Patient text: {patient_text}"
    )

    if video_filepath:
        prompt += "\nThe patient also uploaded a video, but use the provided image as the visual reference."

    client = Groq(api_key=groq_api_key)
    # Keep enough completion budget so reasoning models still emit final content.
    create_kwargs = {
        "model": os.environ.get("GROQ_MODEL", "qwen/qwen3.6-27b"),
        "max_completion_tokens": int(os.environ.get("GROQ_MAX_TOKENS", "2048")),
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a skin care assistant. "
                    "Give general information, not a diagnosis. "
                    "Return only the response intended for the patient. "
                    "Never output analysis, reasoning, drafting notes, "
                    "self-checks, alternatives, or commentary about your instructions."
                ),
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    },
                ],
            },
        ],
    }

    # Optional for reasoning models; ignored by models that do not support it.
    reasoning_format = os.environ.get("GROQ_REASONING_FORMAT", "parsed")
    if reasoning_format:
        create_kwargs["reasoning_format"] = reasoning_format

    response = client.chat.completions.create(**create_kwargs)
    message = response.choices[0].message
    doctor_text = _sanitize_for_speech(_extract_doctor_text(message))

    if not doctor_text:
        raise ValueError(
            "The doctor model returned an empty response. "
            "Try again, or set GROQ_MODEL to a vision model that reliably returns content."
        )

    return doctor_text
