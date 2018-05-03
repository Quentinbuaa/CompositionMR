import random


class TestCases():
    def __init__(self):
        self.dim_upper = 500
        self.dim_lower = 10
        self.split = 0.1
        self.num_of_pair_of_matrices =100

    def setUP(self,dim_lower,dim_upper):
        self.dim_upper = dim_upper
        self.dim_lower = dim_lower

    def setSize(self,size):
        self.num_of_pair_of_matrices = size

    def getSpecialTestCases(self):
        otc_A = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        otc_B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        otc_A = [[1, 7, 0, 0,0], [0, 2, 8, 0,0], [5, 0, 3, 9,0], [0, 6, 0, 4,0],[0, 6, 0, 4,0]]
        otc_B = [[1, 7, 0, 0,0], [0, 2, 8, 0,0], [5, 0, 3, 9,0], [0, 6, 0, 4,0],[0, 6, 0, 4,0]]
        otc_A = [[1, 7, 1, 7], [9, 9, 8, 0], [0, 45, 0, 9], [1, 0, -1, 4]]
        otc_B = [[1, 7, -1, 7], [0, 0, 0, 8], [5, 4, 3, 9], [0, 0, 0, 4]]
        return [(otc_A,otc_B)]


    """Return the list of test cases in tuples. 
       For multiple program input:
       The tuples' ith element corresponding to the ith input of the program.
    """
    def getTestCases(self):
        otc_A = [[1, 7, 0, 0], [0, 2, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]
        otc_B = [[0, 7, 0, 0], [0, 2, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]

        otc_A1 = [[1, 7, 0, 0], [0, 0, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]
        otc_B1 = [[0, 7, 0, 0], [0, 1, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]

        otc_A2 = [[1, 7, 1, 7], [9, 9, 8, 8], [0, 45, 3, 9], [1, 6, -1, 4]]
        otc_B2 = [[1, 7, 1, 7], [9, 9, 8, 8], [5, 4, 3, 9], [1, 6, -1, 4]]

        otc_A3 = [[0, 0, 1, 0, 0, 8, 0, 0],[0, 0, 0, 0, 0, 4, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[0, 0, -1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 100, 0], [0, -20, 0, 0, 0, 0, 0, 0]]
        otc_B3 = [[0, 0, 1, 0, 0, 8, 0, 0],[0, 0, 0, 0, 0, 4, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0],[0, 0, -1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 3, 0], [0, 0, 1, 0, 0, 0, 100, 0], [0, -20, 0, 0, 0, 0, 0, 0]]
        result = [(otc_A, otc_B), (otc_A1, otc_B1),(otc_A2,otc_B2),(otc_A3,otc_B3) ]
        return result

    def getRandomTestCases(self):
        result = []
        for i in range(self.num_of_pair_of_matrices):
            dim = random.randint(self.dim_lower,self.dim_upper)
            otc_A = []
            otc_B = []
            for row in range(dim):
                temp_A = []
                temp_B = []
                for col in range(dim):
                    if random.random() < self.split:
                        temp_A.append(random.randint(-200, 200))
                        temp_B.append(random.randint(-200,200))
                    else:
                        temp_A.append(0)
                        temp_B.append(0)
                otc_A.append(temp_A)
                otc_B.append(temp_B)
            result.append((otc_A,otc_B))
        return result
