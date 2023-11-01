import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set in the environment variables.")

modelPrompt = "You are a helpful assistant"
message = "Give me a sleazy lawyer slogan"

def setModelPrompt(inputPrompt):
    global modelPrompt
    modelPrompt = inputPrompt

def setMessage(inputMessage):
    global message
    message = inputMessage

setModelPrompt("You are a helpful assistant, but you also give your responses with a snarky and sarcastic ring")
setMessage("In one sentence, give me an apology from a fossil fuel company that ruined an ecosystem")

def getResponse():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": modelPrompt},
            {"role": "user", "content": message},
        ],
        max_tokens = 50,
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__': # bandaid fix to prevent these functions running automatixally
    getResponse()
    setModelPrompt()
    setMessage()


