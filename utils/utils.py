import random
import copy

class Utils:
    @staticmethod
    def removeKey(d, key):
        # shallow copy
        r = dict(d)
        r.pop(key, None)
        return r

    @staticmethod
    def calculateCenterPoint(locations=[]):
        centerX, centerY = 0, 0
        for x, y in locations:
            centerX = centerX + x
            centerY = centerY + y
            pass
        centerX = centerX / len(locations)
        centerY = centerY / len(locations)
        return [centerX, centerY]

    @staticmethod
    def randomWalk(location, dist):
        direction = random.randint(0, 7)
        if direction == 0:
            location[0] += 0
            location[1] += dist
        elif direction == 1:
            location[0] += dist
            location[1] += dist
        elif direction == 2:
            location[0] += dist
            location[1] += 0
        elif direction == 3:
            location[0] += dist
            location[1] -= dist
        elif direction == 4:
            location[0] -= 0
            location[1] -= dist
        elif direction == 5:
            location[0] -= dist
            location[1] -= dist
        elif direction == 6:
            location[0] -= dist
            location[1] -= 0
        elif direction == 7:
            location[0] -= dist
            location[1] += dist
        return location

    @staticmethod
    def insertNetworkToRTree(network, rtree):
        for ind, pt in enumerate(network):
            rtree.insertPoint(ind, pt)

    @staticmethod
    def queryNetworkLocationsByIDs(network = [], id = []):
        locations = []
        for key in id:
            locations.append(network[key])
            pass
        return locations