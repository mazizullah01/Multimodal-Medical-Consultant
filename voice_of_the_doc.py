# Step1: Create API Keys

# Step2: Create Client and send request
from deepgram import DeepgramClient
import os
from dotenv import load_dotenv
load_dotenv()

text = "Hi, my name is AI with Aziz, who r u?. I am very happy"
api_key = os.environ.get("DEEPGRAM_API_KEY")
deepgram = DeepgramClient(api_key=api_key)
audio = deepgram.speak.v1.audio.generate(
    text=text,
    model="aura-2-thalia-en",
    encoding="mp3",
)

# Step3: Save audio
from pathlib import Path

audio_file="test-output.mp3"
audio_path = Path(__file__).with_name(audio_file)
with audio_path.open("wb") as file:
    for chunk in audio:
        file.write(chunk)  

