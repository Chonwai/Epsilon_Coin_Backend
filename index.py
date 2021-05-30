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
from model import TagNetwork as TagNetwork
from utils import utils as Utils
import router.api as api


# Creating the Web
# App using flask
app = Flask(__name__)
app.debug = True

# Create the object
# of the class blockchain
TagNetwork = TagNetwork.TagNetwork()
Blockchain = Blackchain.Blockchain(TagNetwork.getNetwork())

api.init_app(app, Blockchain)
CORS(app)


# Run the flask server locally
app.run(host='127.0.0.1', port=5001)
