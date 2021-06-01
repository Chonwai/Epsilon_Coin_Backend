import random
from rtree import index
import rtree
import datetime
import json
from utils import utils as Utils
import hashlib
from model import TagNetwork as TagNetwork

tagNetwork = TagNetwork.TagNetwork()
Utils = Utils.Utils


class Blockchain:
    # This function is created
    # to create the very first
    # block and set it's hash to "0"
    def generateCoordinates(self, tagNetwork):
        cordinates = tagNetwork
        return cordinates

    # This function is created
    # to add further blocks
    # into the chain
    def createBlock(self, proof, previous_hash, unconfirmed_coordinates, RTree, EpsilonA):
        EpsilonA.walk()
        detectedPath = EpsilonA.detectedPathWithTags(RTree, unconfirmed_coordinates, 10)
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'tag_network': unconfirmed_coordinates,
                 'original_path': EpsilonA.path,
                 'detected_path': detectedPath,
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    # This function is created
    # to display the previous block
    def printPreviousBlock(self):
        return self.chain[-1]

    # This is the function for proof of work
    # and used to successfully mine the block

    def proofOfWork(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:3] == '000':
                check_proof = True
                print(hash_operation[:4])
            else:
                new_proof += 1

        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(
            Utils.removeKey(block, 'rtree_index'), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chainValid(self, chain):
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:3] != '000':
                return False
            previous_block = block
            block_index += 1

        return True

    def __init__(self, tagNetwork, RTree, EpsilonA):
        self.chain = []
        self.createBlock(proof=1, previous_hash='0', unconfirmed_coordinates=self.generateCoordinates(
            tagNetwork), RTree=RTree, EpsilonA=EpsilonA)
