from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/health')
def index():
    return 'Healthly'

@app.route('/', methods=['POST']) 
def foo():
    data = request.json
    print(data)
    return jsonify(data)
