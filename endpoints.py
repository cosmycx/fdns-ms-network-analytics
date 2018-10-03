from flask import Flask
from flask import jsonify, request

# Instantiate our Node
app = Flask(__name__)


@app.route('/', methods=['GET'])
def full_chain():
    response = {
        'chain': 'chain',
        'length': 20,
    }
    return jsonify(response), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)