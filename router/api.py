from flask import Flask, jsonify, request
from utils import utils as Utils
from controller import controller as Controller

Utils = Utils.Utils
Controller = Controller.Controller


def init_app(app, blockchain, tagNetwork, rtree, epsilon):
    # Display blockchain in json format
    @app.route('/chain', methods=['GET'])
    def displayChain():
        res = Controller.displayChain(blockchain)
        return jsonify(res), 200

    # Display specify blockchain in json format
    @app.route('/chain/<int:id>', methods=['GET'])
    def displaySpecifyChain(id):
        res = Controller.displaySpecifyChain(blockchain, id)
        return jsonify(res), 200

    # Display ridx in json format
    @app.route('/rtree', methods=['GET'])
    def displayRidx():
        res = Controller.displayRidx(blockchain, rtree)
        return jsonify(res), 200

    # Mining a new block
    @app.route('/chain/mine', methods=['GET'])
    def mineBlock():
        res = Controller.mineBlock(blockchain, tagNetwork, rtree, epsilon)
        return jsonify(res), 200

    # Check validity of blockchain
    @app.route('/validate', methods=['GET'])
    def validate():
        res = Controller.validate(blockchain)
        return jsonify(res), 200

    # Display tags network in json format
    @app.route('/tags', methods=['GET'])
    def displayTags():
        res = Controller.displayTags(tagNetwork)
        return jsonify(res), 200
