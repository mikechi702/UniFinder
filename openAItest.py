import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set in the environment variables.")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me a sleazy lawyer slogan"},
    ],
    max_tokens = 50,
)
print(response['choices'][0]['message']['content'])

# print("test123")


