# python library imports
from flask_cors import CORS
from flask import Flask, jsonify

# local imports
from openAItest import setModelPrompt, setMessage, getResponse

app = Flask(__name__) # initial app setup
CORS(app)

@app.route('/') # base route
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET']) # api setup to send data to the frontend
def get_data():
    testPrompt = "You are a helpful assistant"
    testInput = "Give me a sleazy lawyer slogan"
    aiMessage = "placeholder"
    aiMessage = getResponse(testPrompt, testInput)
    data = {'message': aiMessage}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)