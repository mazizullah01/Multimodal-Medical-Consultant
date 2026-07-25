# step1: install and   import dependencies 
import anthropic
from dotenv import load_dotenv
import os

# step2: Create API keys & client
load_dotenv()

api_key=os.environ.get("MINIMAX_API_KEY")
base_url="https://api.minimax.io/anthropic"

client = anthropic.Anthropic(api_key=api_key, base_url=base_url)

# step3: Create a messsage
messages = [
    {    
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "hello, what can you help me with?",
            }
        ],
    }
]

# step4: Send message

response = client.messages.create(
    model="MiniMax-M3",
    max_tokens=1000,
    messages=messages,
)

# step5: Print message

print(response)

