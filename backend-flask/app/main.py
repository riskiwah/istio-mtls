from flask import Flask, jsonify, make_response
from flask_cors import CORS
from config import API_KEY
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/cuaca', methods=['GET'])
def cuaca():
    CITY = 'Malang'

    r = "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(CITY, API_KEY)
    api_response = requests.get(r).json()
    
    return jsonify(api_response)

@app.route('/health', methods=['GET'])
def hello():
    return make_response("<h2>Im Alive!!<h2>", 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
