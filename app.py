from flask import Flask, Response
from flask import jsonify, request

import os.path


import osmnx as ox
from networkx.readwrite import json_graph

app = Flask(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)


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

    G = ox.graph_from_place('Manhattan, New York, USA', network_type='drive')

    if location is None:
        return "Error, please supply a valid location", 400
    if network_mode is None:
        return "Error, please supply a valid network_mode", 400

    ox.save_graphml(G, filename="testgraph.graphml", folder="/app")

    #jdata = json_graph.tree_data(G,root=1)
    #graphml_json = json_graph.tree_graph(jdata)
    #return jsonify(graphml_json), 200
    # return 'ok', 200
    content = get_file('testgraph.graphml')
    return Response(content, mimetype="application/xml")


# ------------------------------------------------
#               app run
# ------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',  port=5000)
