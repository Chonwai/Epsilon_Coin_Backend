# Python programm to create Blockchain

# For timestamp
import datetime

# To store data
# in our blockchain

# Flask is for creating the web
# app and jsonify is for
# displaying the blockchain
from flask import Flask, jsonify

from flask_cors import CORS

from model import Blockchain as Blackchain
from model import TagNetwork as TagNetwork
from model import RTree as RTree
from model import Epsilon as Epsilon
from utils import utils as Utils
import router.api as api


# Creating the Web
# App using flask
app = Flask(__name__)
app.debug = True

# Create the object
# of the class blockchain
Utils = Utils.Utils
TagNetwork = TagNetwork.TagNetwork()
RTree = RTree.RTree()
EpsilonA = Epsilon.Epsilon()
Utils.insertNetworkToRTree(TagNetwork.getNetwork(), RTree)

Blockchain = Blackchain.Blockchain(TagNetwork.getNetwork(), RTree, EpsilonA)
api.init_app(app, Blockchain, TagNetwork, RTree, EpsilonA)
CORS(app)


# Run the flask server locally
app.run(host='127.0.0.1', port=5001)
