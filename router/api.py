from flask import Flask, jsonify
from utils import utils as utils

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
        print(blockchain.chain[0]['rtree_index'])
        response = {'chain': [utils.removekey(
            i, 'rtree_index') for i in blockchain.chain], 'length': len(blockchain.chain)}
        return jsonify(response), 200
