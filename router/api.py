from flask import Flask, jsonify, request
from utils import utils as utils
import random

utils = utils.Utils


def init_app(app, blockchain):
    # Display blockchain in json format
    @app.route('/chain', methods=['GET'])
    def display_chain():
        response = {'chain': [utils.removekey(i, 'rtree_index') for i in blockchain.chain],
                    'length': len(blockchain.chain)}
        return jsonify(response), 200

    # Display ridx in json format
    @app.route('/rtree_index', methods=['GET'])
    def display_ridx():
        k = request.args.get('nearest', default = '6', type = int)
        rtree = blockchain.chain[0]['rtree_index']
        targetID = blockchain.chain[0]['coordinates'][random.randint(0, 999)]
        nearestID = list(rtree.nearest((targetID[0], targetID[1], targetID[0], targetID[1]), k))
        nearestCoordinates = []
        nearestCoordinates = [blockchain.chain[0]['coordinates'][i] for i in nearestID[1:k]]
        response = {'traget': targetID, 'nearest': nearestCoordinates}
        return jsonify(response), 200
