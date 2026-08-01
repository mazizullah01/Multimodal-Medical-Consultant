# Step1: Record audio from microphone

# dependencies: ffmpeg,  portaudio (commands available in  description)

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
