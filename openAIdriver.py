# python file that drives the openAI test algorithm. These tests succeed if a simulted, ChatGPT conversation
# occurs within the terminal. 

from openAItest import UnifinderChatbot

msgClass = UnifinderChatbot("", "")
# msgClass.setModelPrompt("You are a helpful assistant")
# msgClass.setMessage("Give me a sleazy lawyer slogan.")

# print(msgClass.showCurrentMsgs())

msgClass.simConversation()
# print("\n" + msgClass.getResponse())

