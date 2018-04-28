import KNN.TestCase as TestCase
import KNN.knn as knn
import random
import sys
from decimal import *

class MR():
    def __init__(self):
        self.group_index = "NONE"
        self.index = "NONE"
        self.diversity = 1
        self.score = 0
        self.reversion_count=0
        self.initialization_complete = False


    def countReversion(self, tempList):
        for i in range(len(tempList)-1):
            for j in range(i+1, len(tempList)):
                if tempList[i] > tempList[j]:
                    self.reversion_count += 1
        self.updateIndex()

    def updateIndex(self):
        self.index+="({})".format(self.reversion_count)

    def getGroupInfo(self):
        return self.group_index


    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        return (predictions, training_set, testing_set)

    """Extract the label vector, given the sample set"""
    def getLabelVector(self,matrix):
        label_vector = []
        for row in range(len(matrix)):
            label_vector.append(matrix[row][-1])
        return label_vector

    """Extract the attribute matrix, given the sample set"""
    def getAttributeMatrix(self, matrix):
        attribute_matrix = []
        for row in range(len(matrix)):
            attribute_matrix.append(matrix[row][0:-1])
        return attribute_matrix

    """Duplicate a matrix. This could be used when the original matrix is useful and need to give it to another matrix."""
    def duplicateMatrix(self, original_matrix):
        dup_matrix = []
        for row in range(len(original_matrix)):
            temp = []
            for col in range(len(original_matrix[0])):
                temp.append(original_matrix[row][col])
            dup_matrix.append(temp)
        return dup_matrix

    """Assert whether there is only one element in the testing set. If there are more than one, then program exit."""
    def assertOneTestingSample(self, predictions):
        if not len(predictions) == 1:
            print("The testing sample is more than one!")
            sys.exit(-1)

    def getMessage(self):
        return self.index

"""MR-0: Consistence with affine transformation"""
class MR1(MR):
    def __init__(self, k, b):
        super(MR1, self).__init__()
        self.group_index="1"
        self.k = Decimal(k)
        self.b = Decimal(b)
        self.index = "MR1({},{})".format(self.k, self.b)

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        ftc_train = self.duplicateMatrix(training_set)
        ftc_test = self.duplicateMatrix(testing_set)
        for row in range(len(training_set)):
            for col in range(len(training_set[0])-1):
                ftc_train[row][col] = self.k* Decimal( training_set[row][col]) + self.b
        for row in range(len(testing_set)):
            for col in range(len(testing_set[0])-1):
                ftc_test[row][col] = self.k* Decimal(testing_set[row][col] )+ self.b
        return (predictions, ftc_train,ftc_test)

"""MR-1.1: Permutation of class labels.
    This MR is not for KNN.
"""
class MR2(MR):

    def __init__(self):
        super(MR2, self).__init__()
        self.group_index="2"
        self.index = "MR2"

    def getShuffleMap(self, labelVector):
        original_list = set(labelVector)
        shuffled_list = random.sample(original_list, len(original_list))
        shuffle_map = dict(zip(original_list, shuffled_list))
        return shuffle_map              # given a label, query the corresponding label

    def getExpectedFTCOutput(self, predictions,training_set, testing_set): # this function need to keep independent
        label_vector = self.getLabelVector(training_set)
        shuffle_map = self.getShuffleMap(label_vector)
        ftc_expected_output = []
        for i in range(len(predictions)):
            ftc_expected_output.append(shuffle_map[predictions[i]])
        for row in range(len(training_set)):
            training_set[row][-1] = shuffle_map[training_set[row][-1]]
        return (ftc_expected_output, training_set, testing_set)


"""MR-1.2: Permutation of the attribute."""
class MR3(MR):
    def __init__(self):
        super(MR3, self).__init__()
        self.group_index="3"
        self.index = "MR3"

    """ The matrix contains the label information, hence the last column should be removed"""
    def shuffleAttribute(self, original_matrix, shuffle_map):
        shuffled_matrix = self.duplicateMatrix(original_matrix)
        for row in range(len(shuffled_matrix)):
            for col in range(len(shuffled_matrix[0])-1):         # the last column, label info, is removed
                dict_value = shuffle_map[col]
                if not col == dict_value:
                    shuffled_matrix[row][col] = original_matrix[row][dict_value]
        return shuffled_matrix

    def getShuffleMap(self, training_set ):
        origin_index = list(range(len(training_set[0])-1))       # the last column, label info, is removed
        shuffle_index = random.sample(origin_index, len(origin_index))
        self.shuffle_map = dict(zip(origin_index, shuffle_index))
        self.countReversion(shuffle_index)

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        if not self.initialization_complete:
            self.getShuffleMap(training_set)
            self.initialization_complete = True
        ftc_train =  self.shuffleAttribute(training_set, self.shuffle_map)
        ftc_test = self.shuffleAttribute(testing_set, self.shuffle_map)
        return (predictions, ftc_train, ftc_test)

"""MR-3.1: Consistence with re-prediction."""
class MR4(MR):
    def __init__(self):
        super(MR4, self).__init__()
        self.group_index="4"
        self.index= "MR4"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        self.assertOneTestingSample(predictions)
        ftc_train = self.duplicateMatrix(testing_set)
        ftc_train[0][-1] = predictions[0]
        append_count = int(len(training_set)*0.8)
        ftc_train *=append_count
        ftc_train += training_set
        return (predictions, ftc_train, testing_set)


"""MR-3.2:Additional training sample. """
class MR5(MR):
    def __init__(self):
        super(MR5, self).__init__()
        self.group_index="5"
        self.index= "MR5"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        self.assertOneTestingSample(predictions)
        ftc_training_set = self.duplicateMatrix(training_set)
        for row in range(len(training_set)):
            if training_set[row][-1] == predictions[0]:
                ftc_training_set.append(training_set[row])
                break
        return (predictions, ftc_training_set, testing_set)

"""MR-4.1: Addition of classes by duplicating samples."""
class MR6(MR):
    def __init__(self):
        super(MR6, self).__init__()
        self.group_index="6"
        self.index= "MR6"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        self.assertOneTestingSample(predictions)
        ftc_training_set = self.duplicateMatrix(training_set)
        for row in range(len(training_set)):
            if not training_set[row][-1] == predictions[0]:
                ftc_training_set.append(training_set[row])
        return (predictions, ftc_training_set, testing_set)


"""MR-4.2: Addition of classes by re-labeling samples."""
class MR7(MR):
    def __init__(self):
        super(MR7, self).__init__()
        self.split = 0.67
        self.group_index="7"
        self.index= "MR7"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        self.assertOneTestingSample(predictions)
        ftc_train = self.duplicateMatrix(training_set)
        for row in range(len(ftc_train)):
            if not ftc_train[row][-1] == predictions[0]:
                if random.random() < self.split:
                    ftc_train[row][-1] = training_set[row][-1]+"_suffix"
        return (predictions, ftc_train, testing_set)


"""MR-5.1: Removal of classes."""
class MR8(MR):
    def __init__(self):
        super(MR8, self).__init__()
        self.removed_class_label = ""
        self.group_index="8"
        self.index = "MR8"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        ftc_training_set = []
        self.assertOneTestingSample(predictions)
        label_set = set(self.getLabelVector(training_set))
        for label  in label_set:
            if not label == predictions[0]:
                if self.removed_class_label == "":
                    self.removed_class_label = label
        for row in range(len(training_set)):
            if not self.removed_class_label == training_set[row][-1]:
                ftc_training_set.append(training_set[row])
        return (predictions, ftc_training_set, testing_set)


class MR9(MR):
    def __init__(self):
        super(MR9, self).__init__()
        self.split = 0.67
        self.index = "MR9"

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        ftc_training_set = []
        self.assertOneTestingSample(predictions)
        for row in range(len(training_set)):
            if predictions[0] == training_set[row][-1]:
                ftc_training_set.append(training_set[row])
            else:
                if random.random()<self.split:
                    ftc_training_set.append(training_set[row])
        return (predictions, ftc_training_set, testing_set)


class MR0(MR):
    def __init__(self):
        super(MR0, self).__init__()
        self.group_index="0"
        self.index = "MR0"

    def getSampleIndex(self, len_train):
        self.sample_index = random.sample(list(range(len_train)), len_train)
        self.countReversion(self.sample_index)

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        len_train = len(training_set)
        if not self.initialization_complete:
            self.getSampleIndex(len_train)
            self.initialization_complete = True
        ftc_train = []
        for i in range(len_train):
            ftc_train.append(training_set[i])
        return (predictions, ftc_train, testing_set)

class MRComposition(MR):
    def __init__(self, mrs):
        super(MRComposition, self).__init__()
        self.mrs = mrs

    def getDiversity(self):
        group_vector = []
        for mr in self.mrs:
            group_vector.append(mr.getGroupInfo())
        self.diversity = len(set(group_vector))
        return self.diversity

    def getMax(self):
        max = 0
        for mr in self.mrs:
            if mr.score >max:
                max = mr.score
        return max

    def assessEquality(self):
        if self.score >= self.getMax() and len(self.mrs)>1:
            return True
        else:
            return False

    def setMutationScore(self, score):
        if len(self.mrs) == 1:
            self.mrs[0].score = score
        self.score = score

    def getInfo(self):
        return (self.getMessage(), self.getDiversity(), len(self.mrs), self.score)

    def getExpectedFTCOutput(self, predictions,training_set, testing_set):
        ftc_expected_output = predictions
        ftc_training_set = training_set
        ftc_testing_set = testing_set
        for mr in self.mrs:
            (ftc_expected_output, ftc_training_set, ftc_testing_set) = mr.getExpectedFTCOutput(ftc_expected_output,ftc_training_set,ftc_testing_set)
        return (ftc_expected_output,ftc_training_set,ftc_testing_set)

    def getMessage(self):
        message = self.mrs[0].getMessage()
        for i in range(len(self.mrs)-1):
            message = message+".{}".format(self.mrs[i+1].getMessage())
        return message



def Test1():
    #mutanted_program_to_test = ["MU_1_KNN", "MU_2_KNN","MU_3_KNN", "MU_4_KNN","MU_5_KNN", "MU_6_KNN","MU_7_KNN", "MU_8_KNN","MU_9_KNN"]
    mutanted_program_to_test=["ds"]
    killed_mutants = []
    ts = TestCase.TestCases()
    #ts.getDefiniteDataset()
    for i in range(8000):
        for mu_pro_to_test_name in mutanted_program_to_test:
            knn_to_test = knn.KNNFactory(mu_pro_to_test_name).getKNN()
            mr = MRComposition([ MR1(-9.4,-55.5)])
            #otc_input = ts.getTestCase()
            otc_input = TestCase.TestCases().getTestCase()
            knn_to_test.setInput(otc_input[0], otc_input[1])
            otc_output = knn_to_test.getPredications()
            (ftc_expected_output, ftc_training_set, ftc_testing_set) = mr.getExpectedFTCOutput(otc_output, otc_input[0], otc_input[1])
            knn_to_test.setInput(ftc_training_set, ftc_testing_set)
            ftc_output = knn_to_test.getPredications()
            for i in range(len(ftc_expected_output)):
                if not (ftc_expected_output[i] == ftc_output[i]):
                    killed_mutants.append(mu_pro_to_test_name)
    for item in set(killed_mutants):
        print(item)

""" MR 1, 3, 4, 5, 7 are necessary properties for KNN.
1:
3: 2, 7
4:
5:
7:

"""
if __name__ == "__main__":
    for i in range(10):
        Test1()
