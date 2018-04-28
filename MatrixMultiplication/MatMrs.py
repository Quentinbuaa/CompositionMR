import MatrixMultiplication.matrixmultiplication as spm
import sys

class MR():

    def __init__(self):
        self.ftc_A = []
        self.ftc_B = []
        self.diversity =0
        self.num_of_mrs =0

    def set_diversity(self, diversity):
        self.diversity = diversity

    def get_diversity(self):
        return self.diversity

    def set_num_of_mrs(self, num):
        self.num_of_mrs = num

    def get_num_of_mrs(self):
        return self.num_of_mrs

    def mat_copy(self,A):
        B = []
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j])
            B.append(temp)
        return B

    def mat_transpose(self, A):
        row = len(A)
        column = len(A[0])
        B = []
        for i in range(column):
            temp = []
            for j in range(0, row):
                temp.append(A[j][i])
            B.append(temp)
        return B

    def mat_addition(self, A, B):
        C = []
        if not (len(A)==len(B) and len(A[0]) == len(B[0])):
            print("Can not compound!\n Matrix addition failure, since they do not have the same dimension.")
            sys.exit(-1)
        for i in range(len(A)):
            temp = []
            for j in range(len(A[0])):
                temp.append(A[i][j]+B[i][j])
            C.append(temp)
        return C


    """Return a square Q matrix, whose principle diagonal elements are all constant c."""
    def getQMatrix(self, dim, constant):
        Q = []
        for i in range(dim):
            temp = []
            for j in range(dim):
                if i == j:
                    temp.append(constant)
                else:
                    temp.append(0)
            Q.append(temp)
        return Q

    """Return a matrix, whose elements are all scaled with the given scalar. """
    def mat_multiple_constant(self, matrix, scalar):
        scaled_matrix = self.mat_copy(matrix)
        for i in range(len(scaled_matrix)):
            for j in range(len(scaled_matrix[0])):
                scaled_matrix[i][j] = scaled_matrix[i][j]*scalar
        return scaled_matrix


    def getIdentityMatrix(self,dim):
        I = []
        for i in range(dim):
            temp = []
            for j in range(dim):
                if i == j:
                    temp.append(1)
                else:
                    temp.append(0)
            I.append(temp)
        return I

    """Return a square matrix, which is transformed by exchanging two rows of an Identity matrix."""
    def getPMatrix(self, dim):
        if dim < 2:
            print("Cannot compound, since matrix has less than two rows!")
            sys.exit(-1)
        P = self.getIdentityMatrix(dim)
        temp = P[0]
        P[0] = P[1]
        P[1] = temp
        return P

    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        pass

class MR1(MR):

    def getExpectedFTCOutput(self, otc_output, otc_A, otc_B, program_to_test):
        self.ftc_A = self.mat_transpose(otc_B)
        self.ftc_B = self.mat_transpose(otc_A)
        ftc_expected_output = self.mat_transpose(otc_output)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR1"

class MR2(MR):

    def getExpectedFTCOutput(self, otc_output, otc_A, otc_B, program_to_test):
        P = self.getPMatrix(len(otc_A))
        self.ftc_A = program_to_test(P, otc_A)
        self.ftc_B = self.mat_copy(otc_B)
        ftc_expected_output = program_to_test(P, otc_output)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR2"

class MR3(MR):
    def getExpectedFTCOutput(self, otc_output, otc_A, otc_B, program_to_test):
        P = self.getPMatrix(len(otc_B[0]))
        self.ftc_A = self.mat_copy(otc_A)
        self.ftc_B = program_to_test(otc_B, P)
        ftc_expected_output = program_to_test(otc_output, P)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR3"

class MR4(MR):

    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        Q = self.getQMatrix(len(otc_A), 3)
        self.ftc_A = program_to_test(Q, otc_A)
        self.ftc_B = self.mat_copy(otc_B)
        ftc_expected_output = program_to_test(Q, otc_output)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR4"

class MR5(MR):

    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        Q = self.getQMatrix(len(otc_A), 4)
        self.ftc_B = program_to_test(otc_B, Q)
        self.ftc_A = self.mat_copy(otc_A)
        ftc_expected_output = program_to_test(otc_output, Q)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR5"

class MR6(MR):
    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        scalar = 6
        self.ftc_A = self.mat_multiple_constant(otc_A, scalar)
        self.ftc_B = self.mat_copy(otc_B)
        ftc_expected_output = self.mat_multiple_constant(otc_output, scalar)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR6"

class MR7(MR):
    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        scalar = 7
        self.ftc_B = self.mat_multiple_constant(otc_B, scalar)
        self.ftc_A = self.mat_copy(otc_A)
        ftc_expected_output = self.mat_multiple_constant(otc_output, scalar)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR7"


class MR8(MR):
    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        dim = len(otc_A)
        I = self.getIdentityMatrix(dim)
        self.ftc_A = self.mat_addition(otc_A, I)
        self.ftc_B = self.mat_copy(otc_B)
        ftc_expected_output = self.mat_addition(otc_output, otc_B)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)


    def getMessage(self):
        return "MR8"

class MR9(MR):
    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        dim = len(otc_B)
        I = self.getIdentityMatrix(dim)
        self.ftc_A = self.mat_copy(otc_A)
        self.ftc_B = self.mat_addition(otc_B, I)
        ftc_expected_output = self.mat_addition(otc_A, otc_output)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        return "MR9"


class MRComposition(MR):
    def __init__(self, mrs):
        super(MRComposition, self).__init__()
        self.mrs = mrs

    def getExpectedFTCOutput(self, otc_output,otc_A,otc_B, program_to_test):
        ftc_expected_output = otc_output
        self.ftc_A = otc_A
        self.ftc_B = otc_B
        for mr in self.mrs:
            (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test) = mr.getExpectedFTCOutput(ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)
        return (ftc_expected_output, self.ftc_A, self.ftc_B, program_to_test)

    def getMessage(self):
        message = ""
        for mr in self.mrs:
            message = message+".{}".format(mr.getMessage())
        return message

if __name__ == "__main__":
    otc_A = [[1, 7, 0, 0], [0, 2, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]
    otc_B = [[0, 7, 0, 0], [0, 2, 8, 0], [5, 0, 3, 9], [0, 6, 0, 4]]
    mr = MRComposition([MR8(), MR2(), MR1(), MR4(), MR5(), MR3(), MR6(), MR7(),MR9()])
    otc_output = spm.MatMul(otc_A,otc_B)
    (ftc_expected_output, ftc_A, ftc_B, spm.MatMul) = mr.getExpectedFTCOutput(otc_output, otc_A, otc_B, spm.MatMul)
    ftc_output = spm.MatMul(ftc_A, ftc_B)
    print(ftc_expected_output)
    print(ftc_output)

