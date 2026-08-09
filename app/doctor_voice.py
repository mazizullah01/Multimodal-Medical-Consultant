import os
import platform
import subprocess
import tempfile
from pathlib import Path

from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()


def convert_text_to_doctor_audio(text, output_filepath=None):
    deepgram_api_key = os.environ.get("DEEPGRAM_API_KEY")
    deepgram = DeepgramClient(api_key=deepgram_api_key)
    audio = deepgram.speak.v1.audio.generate(
        text=text[:1000],
        model=os.environ.get("DEEPGRAM_TTS_MODEL", "aura-2-thalia-en"),
        encoding="mp3",
    )

    if output_filepath is None:
        # A unique result prevents simultaneous consultations from overwriting
        # one another. Gradio copies/serves this file for browser playback.
        temp_audio = tempfile.NamedTemporaryFile(
            prefix="derma_ai_", suffix=".mp3", delete=False
        )
        output_filepath = Path(temp_audio.name)
        temp_audio.close()
    output_filepath = Path(output_filepath)
    with output_filepath.open("wb") as file:
        for chunk in audio:
            file.write(chunk)

    return output_filepath


def play_audio(audio_filepath):
    audio_filepath = str(audio_filepath)

    if platform.system() == "Darwin":
        subprocess.run(["afplay", audio_filepath], check=False)
    elif platform.system() == "Windows":
        os.startfile(audio_filepath)
    else:
        subprocess.run(["xdg-open", audio_filepath], check=False)
