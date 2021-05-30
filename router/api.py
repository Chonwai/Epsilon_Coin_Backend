from flask import Flask, jsonify, request
from utils import utils as Utils
import random

Utils = Utils.Utils


def init_app(app, blockchain):
    # Display blockchain in json format
    @app.route('/chain', methods=['GET'])
    def displayChain():
        response = {'chain': [Utils.removekey(i, 'rtree_index') for i in blockchain.chain],
                    'length': len(blockchain.chain)}
        return jsonify(response), 200

    # Display ridx in json format
    @app.route('/rtree_index', methods=['GET'])
    def displayRidx():
        k = request.args.get('nearest', default='6', type=int)
        rtree = blockchain.chain[0]['rtree_index']
        targetID = blockchain.chain[0]['coordinates'][random.randint(0, 49999)]
        nearestID = list(rtree.nearest(
            (targetID[0], targetID[1], targetID[0], targetID[1]), k))
        nearestCoordinates = []
        nearestCoordinates = [blockchain.chain[0]
                              ['coordinates'][i] for i in nearestID[1:k]]
        response = {'traget': targetID, 'nearest': nearestCoordinates}
        return jsonify(response), 200

    # Mining a new block
    @app.route('/mine_block', methods=['GET'])
    def mineBlock():
        previous_block = blockchain.printPreviousBlock()
        previous_proof = previous_block['proof']
        proof = blockchain.proofOfWork(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        unconfirmed_coordinates = blockchain.generateCoordinates(blockchain.tagNetwork)
        block = blockchain.createBlock(
            proof, previous_hash, unconfirmed_coordinates)

        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'coordinates': block['coordinates'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']
                    }

        return jsonify(response), 200

    # Check validity of blockchain
    @app.route('/valid', methods=['GET'])
    def valid():
        valid = blockchain.chainValid(blockchain.chain)

        if valid:
            response = {'message': 'The Blockchain is valid.'}
        else:
            response = {'message': 'The Blockchain is not valid.'}
        return jsonify(response), 200
