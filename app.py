from flask import Flask
from flask import jsonify, request

import osmnx as ox

app = Flask(__name__)

# ------------------------------------------------
#               / 
# ------------------------------------------------
@app.route('/')
def index():
    return 'Street Network Analysis'

# ------------------------------------------------
#               /graph_from_address
# ------------------------------------------------
@app.route('/graph_from_address', methods=['POST'])
def graph_from_address():

    values = request.get_json()
    location = values.get('location')
    network_mode = values.get('network_mode')
    print(location)
    print(network_mode)

    if location is None:
        return "Error, please supply a valid location", 400
    if network_mode is None:
        return "Error, please supply a valid network_mode", 400
    return 'ok', 200

# ------------------------------------------------
#               /graph_from_point
# ------------------------------------------------
@app.route('/graph_from_point', methods=['POST'])
def graph_from_point():

    values = request.get_json()
    location = values.get('location')
    network_mode = values.get('network_mode')
    print(location)
    print(network_mode)

    if location is None:
        return "Error, please supply a valid location", 400
    if network_mode is None:
        return "Error, please supply a valid network_mode", 400
    return 'ok', 200

# ------------------------------------------------
#               app run
# ------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',  port=5000)
