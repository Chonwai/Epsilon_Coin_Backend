import random
from rtree import index
import rtree
import datetime
import json
from utils import utils as utils


class Blockchain:
    # This function is created
    # to create the very first
    # block and set it's hash to "0"
    def gen_coordinates(self):
        cordinates = [(random.uniform(-90, 90), random.uniform(-180, 180))
                      for _ in range(1000)]
        print("HeHe")
        print(str(len(cordinates)))
        Ridx = rtree.index.Index()
        for ind, pt in enumerate(cordinates):
            Ridx.insert(ind, (pt[0], pt[1], pt[0], pt[1]))
        return cordinates, Ridx

    def __init__(self):
        self.unconfirmed_coordinates = []
        self.chain = []
        self.create_block(proof=1, previous_hash='0',
                          unconfirmed_coordinates=self.gen_coordinates())
        self.utils = utils.Utils

    # def add_new_transaction(self):
    #     coords = [(random.uniform(-90, 90), random.uniform(-180, 180)) for _ in range(10)]
    #     self.unconfirmed_coordinates.extend(coords)

    # This function is created
    # to add further blocks
    # into the chain

    def create_block(self, proof, previous_hash, unconfirmed_coordinates):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'coordinates': unconfirmed_coordinates[0],
                 'rtree_index': unconfirmed_coordinates[1],
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    # This function is created
    # to display the previous block
    def print_previous_block(self):
        return self.chain[-1]

    # This is the function for proof of work
    # and used to successfully mine the block

    def proof_of_work(self, previous_proof):
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
            removekey(block, 'rtree_index'), sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain):
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
