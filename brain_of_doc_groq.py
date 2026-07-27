import base64
import os

from dotenv import  load_dotenv
from groq import Groq

folder = os.path.dirname(__file__)
env_path = os.path.join(folder, ".env")
load_dotenv(env_path)

