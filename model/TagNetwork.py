import random


class TagNetwork:
    def generateTags(self):
        for i in range(50000):
            cordinate = (random.uniform(-90, 90), random.uniform(-180, 180))
            self.tags.append(cordinate)

    def getNetworkLength(self):
        return len(self.tags)

    def getNetwork(self):
        return self.tags

    def __init__(self):
        self.description = 'I go to school by bus.'
        self.tags = []
        self.generateTags()