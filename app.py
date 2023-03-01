import requests
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("Hello! This service provides the latest information on the prevailing exchange rates.")
    return 'Enter the base currency using a 3-letter abbreviation: e.g. /USD or /EUR'

@app.route('/<name>')
def get_rates(name):
    url = f'https://v6.exchangerate-api.com/v6/4fd53a03fff03cbb41d0e44c/latest/{name}'
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
