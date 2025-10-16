from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

def process_emulate():
    time.sleep(0.1)

def float_random():
    randomVar = random.uniform('1', '1000')
    jsonify({"Message": {randomVar}})


@app.route('/')
def main_page():
    process_emulate()
    return jsonify({"Message": "Main Page"})

@app.route('/data/search')
def data_search():
    process_emulate()
    return jsonify({"Result": ["item1", "item2", "item3"]})

@app.route('/data/search/complex')
def complexData_search():
    process_emulate()
    return jsonify({"result": [{"id":i,"value": random.randint(1,1000)} for i in range(5)]})

@app.route('/process', methods=['POST'])
def process():
    process_emulate()
    return jsonify({"status": "processed", "data": request.json})

if __name__ == '__main__':
    app.run(port=8000)










