from flask import Flask, jsonify, make_response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/cuaca', methods=['GET'])
def cuaca():
    params = {
        'access_key': '3fa0e89892bed6f39540c3c20ba036c8',
        'query': 'Malang'
    }

    r = requests.get('http://api.weatherstack.com/current', params)
    api_response = r.json()
    
    return jsonify(api_response)

@app.route('/health', methods=['GET'])
def hello():
    return make_response("<h2>Im Alive!!<h2>", 200)

if __name__ == '__main__':
    app.run(port=5000, debug= True)
