import random
import copy
from utils import utils as Utils 

Utils = Utils.Utils

class Epsilon:
    def __init__(self, path=[]):
        self.path = path
        self.dist = 1
        self.perviousLocation = [random.uniform(-90, 90), random.uniform(-180, 180)]

    def updatePath(self, path):
        self.path = path

    def perviousStopLocation(self, location):
        self.perviousLocation = location

    def clearPath(self):
        self.path = []

    def getPath(self):
        print(self.path)
        return self.path

    def walk(self):
        self.clearPath()
        self.path.append(copy.deepcopy(self.perviousLocation))
        for i in range(1440):
            self.perviousLocation = Utils.randomWalk(self.perviousLocation, self.dist)
            self.path.append(copy.deepcopy(self.perviousLocation))
        self.perviousLocation = self.path[-1]
        return self.path
