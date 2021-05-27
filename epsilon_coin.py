# Python programm to create Blockchain

# For timestamp
import datetime

# Calculating the hash
# in order to add digital
# fingerprints to the blocks
import hashlib

# To store data
# in our blockchain
import json

# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
from flask import Flask, jsonify

from rtree import index
import rtree

from flask_cors import CORS

from model import Blockchain as Blackchain
from utils import utils as utils
import router.api as api


# Creating the Web
# App using flask
app = Flask(__name__)
app.debug = True

# Create the object
# of the class blockchain
blockchain = Blackchain.Blockchain()
utils = utils.Utils

api.init_app(app, blockchain)
CORS(app)

# Mining a new block


@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    unconfirmed_coordinates = blockchain.gen_coordinates()
    block = blockchain.create_block(
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
    valid = blockchain.chain_valid(blockchain.chain)

    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200


# Run the flask server locally
app.run(host='127.0.0.1', port=5001)
