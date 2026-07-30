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

