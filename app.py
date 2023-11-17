# python library imports
from flask_cors import CORS
from flask import Flask, jsonify, request

# local imports
from openAItest import UnifinderChatbot

app = Flask(__name__) # initial app setup
CORS(app)

@app.route('/') # base route
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET', 'POST']) # api setup to send data to the frontend
def get_data():
    if request.method == 'GET':
        # Handling GET request (assuming you want to keep the existing logic)
        aiMessage = "Start chatting."
    elif request.method == 'POST':
        # Handling POST request with user input
        data = request.get_json()
        user_input = data.get('name')  # Assuming 'name' is the key sent from the frontend
        testPrompt = "You are a helpful assistant"  # You can use the same prompt or customize it
        testInput = user_input
        msgObject = UnifinderChatbot(testPrompt, testInput)
        aiMessage = msgObject.makeResponse()

    data = {'message': aiMessage}
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True)