import random
from flask import Flask, jsonify, request
from utils import utils as Utils

Utils = Utils.Utils


class Controller:
    @staticmethod
    def displayChain(blockchain):
        response = {'chain': [Utils.removeKey(i, 'tag_network') for i in blockchain.chain],
                    'length': len(blockchain.chain)}
        return response

    @staticmethod
    def displaySpecifyChain(blockchain, id):
        block = list(filter(lambda x: x['index'] == id, blockchain.chain))
        response = {'chain': [Utils.removeKey(block[0], 'tag_network')],
                    'length': 1}
        return response

    @staticmethod
    def displayRidx(blockchain, RTree):
        k = request.args.get('nearest', default='6', type=int)
        nearestCoordinates = []
        target = [random.uniform(-100, 100), random.uniform(-100, 100)]
        nearestID = list(RTree.findTopKNearest(target, k))
        nearestCoordinates = [blockchain.chain[0]
                              ['tag_network'][i] for i in nearestID[1:k]]
        Utils.calculateCenterPoint(nearestCoordinates)
        response = {'traget': target, 'nearest': nearestCoordinates}
        return response

    @staticmethod
    def mineBlock(blockchain, tagNetwork, RTree, EpsilonA):
        previous_block = blockchain.printPreviousBlock()
        previous_proof = previous_block['proof']
        proof = blockchain.proofOfWork(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        unconfirmed_coordinates = tagNetwork.getNetwork()
        block = blockchain.createBlock(
            proof, previous_hash, unconfirmed_coordinates, RTree, EpsilonA)

        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']
                    }

        return response

    @staticmethod
    def validate(blockchain):
        valid = blockchain.chainValid(blockchain.chain)
        if valid:
            response = {'message': 'The Blockchain is valid.'}
        else:
            response = {'message': 'The Blockchain is not valid.'}
        return response

    @staticmethod
    def displayTags(tagNetwork):
        response = {'tag_network': tagNetwork.getNetwork()}
        return response
