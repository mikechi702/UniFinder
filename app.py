from flask_cors import CORS
from flask import Flask, jsonify
from openAItest import setModelPrompt, setMessage, getResponse

app = Flask(__name__) # initial app setup
CORS(app)

@app.route('/') # base route
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET']) # api setup to send data to the frontend
def get_data():
    setModelPrompt("You are a helpful assistant")
    setMessage("Give me a sleazy lawyer slogan")
    aiMessage = "placeholder"
    aiMessage = getResponse()
    data = {'message': aiMessage}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)