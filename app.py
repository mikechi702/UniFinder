# python library imports
from flask_cors import CORS
from flask import Flask, jsonify, request

# local imports
from openAItest import UnifinderChatbot

app = Flask(__name__) # initial app setup
CORS(app)

testPrompt = "You are a helpful assistant"
testInput = ""

msgObject = UnifinderChatbot(testPrompt, testInput)
msgObject.setModelPrompt("""I want you to act as a guidance counselor
                            that helps incoming college students either choose their major
                            or choose their next university. Consider safety as an inherently high priority during your search.
                            I want you to ask one question at a time, limiting each question to one sentence.
                            After up to 4 questions, I want you to ask me if I am ready to explore some university options,
                            which should be formatted in a numbered list with short bullet-point descriptions.
                            These descriptions should be up-to-date within your capabilities. After displaying the list
                            of suggested colleges, you should ask me if I still need more help searching.""")

msgObject.setMessage("Let us begin with your first question")

@app.route('/') # base route
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET', 'POST']) # chatbot api to send to the frontend
def get_data():
    if request.method == 'GET':
        aiMessage = msgObject.makeResponse()
    elif request.method == 'POST':
        # Handling POST request with user input
        data = request.get_json()
        user_input = data.get('name')
        msgObject.setMessage(user_input)
        aiMessage = msgObject.makeResponse()

    data = {'message': aiMessage}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)