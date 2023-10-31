from flask_cors import CORS
from flask import Flask, jsonify
# import openAItest

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)