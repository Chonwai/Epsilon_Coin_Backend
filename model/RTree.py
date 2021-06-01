from rtree import index
import rtree

class RTree:
    def __init__(self):
        self.rtree = rtree.index.Index()

    def insertPoint(self, index, point):
        self.rtree.insert(index, (point[0], point[1], point[0], point[1]))

    def findTopKNearest(self, target, k = 10):
        topKNearest = list(self.rtree.nearest(
            (target[0], target[1], target[0], target[1]), k))
        return topKNearest