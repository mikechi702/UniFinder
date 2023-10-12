from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello in flask"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)