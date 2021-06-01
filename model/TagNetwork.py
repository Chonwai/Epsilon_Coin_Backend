import random


class TagNetwork:
    def generateTags(self):
        for i in range(50000):
            coordinate = (random.uniform(-100, 100), random.uniform(-100, 100))
            self.tags.append(coordinate)

    def getNetworkLength(self):
        return len(self.tags)

    def getNetwork(self):
        return self.tags

    def __init__(self):
        self.description = 'I go to school by bus.'
        self.tags = []
        self.generateTags()