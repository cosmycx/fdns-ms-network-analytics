from flask import Flask

from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test/<int:post_id>')
def testing(post_id):
    return 'Got here with another endpoint! %d' % post_id

@app.route('/address/<string:textualAddress>')
def address(textualAddress):
    return 'Got here with another endpoint! %s' % textualAddress


@app.route('/latlon/<int:lat>/<int:lon>', methods=['GET'])
def latlon(lat, lon):
    response = {
        'latitude': lat,
        'longitude': lon,
    }
    return jsonify(response), 200
