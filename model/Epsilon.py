import random
import copy
from utils import utils as Utils 

Utils = Utils.Utils

class Epsilon:
    def __init__(self, path=[]):
        self.path = path
        self.dist = 3
        self.perviousLocation = [random.uniform(-100, 100), random.uniform(-100, 100)]

    def updatePath(self, path):
        self.path = path

    def perviousStopLocation(self, location):
        self.perviousLocation = location

    def clearPath(self):
        self.path = []

    def getPath(self):
        return self.path

    def walk(self):
        self.clearPath()
        self.path.append(copy.deepcopy(self.perviousLocation))
        for i in range(1440):
            self.perviousLocation = Utils.randomWalk(self.perviousLocation, self.dist)
            self.path.append(copy.deepcopy(self.perviousLocation))
        self.perviousLocation = self.path[-1]
        return self.path
    
    def detectedPathWithTags(self, rtree, network, k = 10):
        predictPath = []
        for location in self.path:
            item = {}
            nearestID = rtree.findTopKNearest(location, 10)
            nearestTags = Utils.queryNetworkLocationsByIDs(network, nearestID)
            detectedPoint = Utils.calculateCenterPoint(nearestTags)
            item['detected_point'] = detectedPoint
            item['nearest_tags'] = nearestTags
            predictPath.append(item)
            pass
        return predictPath
