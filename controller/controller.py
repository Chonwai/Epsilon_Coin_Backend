import random
from flask import Flask, jsonify, request
from utils import utils as Utils

Utils = Utils.Utils


class Controller:
    @staticmethod
    def displayChain(blockchain):
        response = {'chain': [Utils.removeKey(i, 'rtree_index') for i in blockchain.chain],
                    'length': len(blockchain.chain)}
        return response

    @staticmethod
    def displayRidx(blockchain, rtree):
        k = request.args.get('nearest', default='6', type=int)
        nearestCoordinates = []
        # targetID = blockchain.chain[0]['coordinates'][random.randint(0, 4999)]
        target = [random.uniform(-90, 90), random.uniform(-180, 180)]
        print("The Initial Point is: ", target)
        nearestID = list(rtree.findTopKNearest(target, k))
        nearestCoordinates = [blockchain.chain[0]
                              ['coordinates'][i] for i in nearestID[1:k]]
        Utils.calculateCenterPoint(nearestCoordinates)
        response = {'traget': target, 'nearest': nearestCoordinates}
        return response

    @staticmethod
    def mineBlock(blockchain, tagNetwork, rtree):
        previous_block = blockchain.printPreviousBlock()
        previous_proof = previous_block['proof']
        proof = blockchain.proofOfWork(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        unconfirmed_coordinates = blockchain.generateCoordinates(
            tagNetwork.getNetwork(), rtree)
        block = blockchain.createBlock(
            proof, previous_hash, unconfirmed_coordinates)

        response = {'message': 'A block is MINED',
                    'index': block['index'],
                    'coordinates': block['coordinates'],
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
