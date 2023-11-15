import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set in the environment variables.")
class UnifinderChatbot:
    def __init__(self, modelPrompt, message):
        self.message = message
        self.modelPrompt = modelPrompt
        self.messageHistory = []

    def setModelPrompt(self, inputPrompt):
        self.modelPrompt = inputPrompt

    def setMessage(self, inputMessage):
        self.message = inputMessage
    
    def showCurrentMsgs(self):
        return "Chatbot role: " + self.modelPrompt + "\nUser input: " + self.message
    
    # generates a response from the OpenAI api and returns the JSON message from it
    def makeResponse(self):
        if not self.messageHistory:
            self.messageHistory.append({"role": "system", "content": self.modelPrompt})

        self.messageHistory.append({"role": "user", "content": self.message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messageHistory,
            max_tokens = 100,
        )
        
        self.messageHistory.append(response['choices'][0]['message'])

        return "\nUNIFINDER: " + response['choices'][0]['message']['content'] + "\n"
    
    # simulates a conversation with the OpenAI API using the user input from python. Refactor later to take user input from the React
    # frontend
    def simConversation(self):
        self.setModelPrompt("""I want you to act as a guidance counselor
                                that helps incoming college students either choose their major
                                or choose their next university. Consider safety as high priority as you search.
                                I want you to ask one question at a time, limiting each question to one sentence.
                                After up to 3 questions, I want you to ask me if I am ready to explore some university options,
                                which should be formatted in a numbered list with short bullet-point descriptions.""") 
        
        self.setMessage("Let us begin with your first question")
        print(self.makeResponse())

        while input != "quit()":
            userMessages = input("User: ")
            self.setMessage(userMessages)
            print(self.makeResponse())
    

    
    # end of inputPrompts class

# if __name__ == '__main__': # bandaid fix to prevent these functions running automatically
#     getResponse("", "")
#     simConversation()


