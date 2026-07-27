import base64
import os

from dotenv import  load_dotenv
from groq import Groq

folder = os.path.dirname(__file__)
env_path = os.path.join(folder, ".env")
load_dotenv(env_path)

api_key = os .environ.get("GROQ_API_KEY")
if not api_key :
    raise ValueError("Missing GROQ_API_KEY in .env or environment")

image_path = os.path.join(folder, "sample-image.jpg")
with open(image_path, "rb") as file:
    image_data = base64.b64encode(file.read()).decode("utf-8")

client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model=os.environ.get("GROQ_MODEL", "qwen/qwen3.6-27b"),
    max_completion_tokens=1000,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful medical assistant. Give general information, not a diagnosis."
        },
        {
            "role":  "user",
            "content": [
                {
                "type": "text",
                "text": "What do you see  in this image? Give general skin advice, not a diagnosis."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}",
                    },
                },
            ],
        }
    ],                 
)

print(response.choices[0].message.content)
