import itertools
from KNN.KNNMRs import *
import KNN.TestCase as TestCase
import KNN.knn as knn
from Library.Log import LoggerDB


class MetamorphicTest():

    def __init__(self, model, cmr_num, test_case_num):
        self.mr_list = []
        self.cmr_list = []
        self.test_case_number = test_case_num
        self.mutanted_program_to_test = ["MU_1_KNN", "MU_2_KNN", "MU_3_KNN", "MU_4_KNN", "MU_5_KNN", "MU_6_KNN", "MU_7_KNN",
                                    "MU_8_KNN", "MU_9_KNN"]

        self.model = model
        self.initializeDataBase()
        self.initializeTestCases()
        self.cmr_num= cmr_num
        self.equality_count_list = []


    def getRandomInt(self, eliminate):
        result = 0
        de=10  # destiny
        for i in range(de):
            result = random.randint(-100, 100)
            if not result == eliminate:
                break
        return result

    def loadMRList(self):
        k1 = self.getRandomInt(1)
        b1 = self.getRandomInt(0)
        k2 = self.getRandomInt(1)
        b3 = self.getRandomInt(0)
        self.mr_list += [MR1(k1,b1),MR1(k2,0),MR1(1,b3)]
        #self.mr_list += [MR0(), MR1(k1,b1),MR1(k2,0),MR1(1,b3),MR3()]


    def purgeMRList(self):
        self.mr_list = []

    def initializeDataBase(self):
        self.logger = LoggerDB("knn_{}.db".format(self.test_case_number))
        self.logger.connectDB()
        if self.model =="TEST":
            self.logger.purge()
        self.logger.setLabelList(["Description","Diversity","Num","MutationScore","Equality"])

    def initializeTestCases(self):
        self.testcases = []
        for i in range(self.test_case_number):
            self.testcases.append(TestCase.TestCases().getTestCase())

    def testAllMRs(self):
        self.getCMRList(self.cmr_num)
        self.equal_count=0
        self.otc_test_case = TestCase.TestCases().getTestCase()
        for cmr in self.cmr_list:
            self.equality=0   # 1 denotes equal or higher score, 0 denotes smaller score.
            mutation_score = self.getMutationScore(cmr)
            cmr.setMutationScore(mutation_score)
            (des, div, num, score) = cmr.getInfo()
            if cmr.assessEquality():
                self.equality = 1
                self.equal_count+=1
            self.logger.insert([des, div, num, score, self.equality])
        self.logger.query()
        self.equality_count_list.append(self.equal_count)

    def getMutationScore(self, mr):
        killed_mutants = self.TestOneMR(mr)
        killed_mutants = set(killed_mutants)
        return float(len(killed_mutants))/float(len(self.mutanted_program_to_test))

    def getCMRList(self, num):
        for i in range(num):
            for candidates in itertools.combinations(self.mr_list, i+1):
                self.cmr_list.append(MRComposition(list(candidates)))

    def AssertMRViolation(self, ftc_output, ftc_expected_output):
        violate = False
        if not ftc_expected_output[0] == ftc_output[0]:
            violate = True
        return violate

    def TestOneMR(self, mr):
        killed_mutants = []
        for mu_pro_to_test_name in self.mutanted_program_to_test:
            for testcase in self.testcases:   # run n number of test cases
                knn_to_test = knn.KNNFactory(mu_pro_to_test_name).getKNN()
                otc_input = testcase
                knn_to_test.setInput(otc_input[0], otc_input[1])
                otc_output = knn_to_test.getPredications()
                (ftc_expected_output, ftc_training_set, ftc_testing_set) = mr.getExpectedFTCOutput(otc_output,
                                                                                                   otc_input[0],
                                                                                                   otc_input[1])
                knn_to_test.setInput(ftc_training_set, ftc_testing_set)
                ftc_output = knn_to_test.getPredications()
                violation = self.AssertMRViolation(ftc_expected_output, ftc_output)
                if violation:
                    killed_mutants.append(mu_pro_to_test_name)
        return killed_mutants

    def clear(self):
        self.purgeMRList()
        self.cmr_list=[]


class MTCompare(MetamorphicTest):
    def __init__(self):
        super(MTCompare, self).__init__("TEST", 1, 8000)

    def verifyCase3(self):
        mr_1 = MR1(-30.2, 10.3)
        #mr_2 = MR1(3.3, 9.4)
        mr_2 = MR5()
        ts_1 = self.TestOneMR(mr_1)
        ts_2 = self.TestOneMR(mr_2)
        ts_12 = self.TestOneMR(MRComposition([mr_1, mr_2]))
        print(list(set(ts_1)))
        print(list(set(ts_2)))
        print(list(set(ts_12)))


    def TestOneMR_with_different_test_set(self, mr):
        killed_mutants = []
        killed_test_cases = []
        for test_index in range(self.test_case_number):   # run n number of test cases
            for mu_pro_to_test_name in self.mutanted_program_to_test:
                knn_to_test = knn.KNNFactory(mu_pro_to_test_name).getKNN()
                otc_input = TestCase.TestCases().getTestCase()
                knn_to_test.setInput(otc_input[0], otc_input[1])
                otc_output = knn_to_test.getPredications()
                (ftc_expected_output, ftc_training_set, ftc_testing_set) = mr.getExpectedFTCOutput(otc_output,
                                                                                                   otc_input[0],
                                                                                                   otc_input[1])
                knn_to_test.setInput(ftc_training_set, ftc_testing_set)
                ftc_output = knn_to_test.getPredications()
                violation = self.AssertMRViolation(ftc_expected_output, ftc_output)
                if violation:
                    killed_mutants.append(mu_pro_to_test_name)
                    #killed_test_cases.append(1)
                #else:
                    #killed_test_cases.append(0)
        return killed_mutants


def Test_1():
    mt = MetamorphicTest("TEST", 3, 100)
    for i in range(1):
        print(">>>>>{}>>>>>>".format(i))
        mt.loadMRList()
        mt.testAllMRs()
        mt.clear()
    print(mt.equality_count_list)

def Test_2():
    mt = MTCompare()
    mt.verifyCase3()

if __name__ == "__main__":
    Test_2()
