from flask import Flask
from flask import jsonify, request

# osmnx.core.graph_from_address
# osmnx.core.graph_from_point


#from osmnx import osmnx
# import geopandas as gpd

# Instantiate our Node
app = Flask(__name__)


@app.route('/', methods=['GET'])
def graph_from_place():
  # print(request.get_json())

  # Check required fields are in the POST
  # required = ['location', 'network_type']
  # print(location)
  response = {
      'chain': 'chain',
      'length': 20,
  }
  return jsonify(response), 200

# locationStr, network_mode
@app.route('/api', methods=['GET', 'POST'])
def add_message():

    values = request.get_json()
    location = values.get('location')
    print location


    if location is None:
        return "Error, please supply a valid location", 400
    return 'uuid'
    # @app.route('/receive', methods = ['POST'])
# def graph_from_place2():
#     values = request.get_json()

#     print values['location']

    # Check that the required fields are in the POSTed data
    # required = ['sender', 'recipient', 'amount']
    # if not all (k in values for k in required):
    #     return 'Missing values: {k}', 400

    # # Create a new transaction
    # index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    # response = {'message': f'Transaction will be added to Block {index}'}
    # return jsonify(response), 200

# # @app.route('/mine', methods=['GET'])
# # def mine():
# #     return "We'll mine a new Block"
# @app.route('/mine', methods=['GET'])
# def mine():
#     # We run the proof of work algorithm to get the next proof...
#     last_block = blockchain.last_block
#     proof = blockchain.proof_of_work(last_block)

#     # We must receive a reward for finding the proof.
#     # The sender is "0" to signify that this node has mined a new coin.
#     blockchain.new_transaction(
#         sender="0",
#         recipient=node_identifier,
#         amount=1,
#     )

#     # Forge the new Block by adding it to the chain
#     previous_hash = blockchain.hash(last_block)
#     block = blockchain.new_block(proof, previous_hash)

#     response = {
#         'message': "New Block Forged",
#         'index': block['index'],
#         'transactions': block['transactions'],
#         'proof': block['proof'],
#         'previous_hash': block['previous_hash'],
#     }
#     return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    