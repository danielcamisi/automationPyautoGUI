from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/characters', methods=['GET'])
def get_characters():
    response = requests.get('https://rickandmortyapi.com/api/character')
    data = response.json()
    return jsonify(data)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)