import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set in the environment variables.")

modelPrompt = "You are a helpful assistant"
message = "I am ready. let's hear your first question"
inMessages = []

def setModelPrompt(inputPrompt):
    global modelPrompt
    modelPrompt = inputPrompt

def setMessage(inputMessage):
    global message
    message = inputMessage

def getResponse():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": modelPrompt},
            {"role": "user", "content": message},
        ],
        max_tokens = 100,
    )

    return "\nUNIFINDER: " + response['choices'][0]['message']['content'] + "\n"

def simConversation():
    setModelPrompt("""I want you to act as a guidance counselor
                    that helps incoming college students either choose their major
                    or choose their next university. Consider safety as high priority as you search.
                    I want you to ask one question at a time, limiting each question to one sentence.
                    After up to 5 questions, I want you to ask me if I am ready to explore some university options,
                    which should be formatted in a numbered list with short bullet-point descriptions.""")
    
    setMessage("Let us begin with your first question")
    print(getResponse())

    while input != "quit()":
        userMessages = input("Enter your input: ")



simConversation()

if __name__ == '__main__': # bandaid fix to prevent these functions running automatixally
    getResponse()
    setModelPrompt()
    setMessage()


