import csv
import random
import sys
from decimal import *

class TestCases():
    def __init__(self):
        self.filename = 'iris.data'
        self.split = 0.5
        self.label_count = 3

        self.trainingSet = []
        self.testSet = []
        self.loadDataset()

    """
    """
    def getTestCase(self):
        return (self.trainingSet, self.testSet)

    def verifyTrainingSet(self):
        label_vector = []
        count = 0
        for row in range(len(self.trainingSet)):
            label_vector.append(self.trainingSet[row][-1])
        if not len(set(label_vector)) == self.label_count:
            self.loadDataset()
            count += 1
            if count > 9:
                print("The split number is to small")
                sys.exit(-1)


    def getDefiniteDataset(self):
        num = 120
        count = 30
        self.trainingSet = []
        with open(self.filename, 'rt') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            for x in range(len(dataset)-1):
                count += 1
                for y in range(4):
                    dataset[x][y] = Decimal(dataset[x][y])
                if count< num:
                    self.trainingSet.append(dataset[x])
            self.testSet = [dataset[num+5]]

    def loadDataset(self):
        with open(self.filename, 'rt') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            train_count= 0
            for x in range(len(dataset)-1):
                for y in range(4):
                    dataset[x][y] = Decimal(dataset[x][y])
                if random.random() <self.split:
                    self.trainingSet.append(dataset[x])
                    train_count+=1
            #self.testSet.append(dataset[train_count+5])
            self.testSet = random.sample(dataset, 1)
            self.verifyTrainingSet()

if __name__ == "__main__":
    ts = TestCases()
    ts.loadDataset()