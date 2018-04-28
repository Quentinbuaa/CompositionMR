import triangle
import math
import sys

def AssertMRViolation(ftc_output, ftc_expected_output, message):
    d = 0.00000001
    if math.fabs(ftc_output - ftc_expected_output) <= d :
        #print("OK")
        violation = False
    else:
        #print("Violation of: {}".format(message))
        violation = True
    return violation

class MR():
    def __init__(self):
        pass
    def getFTC(self, a, b, c):
        pass

    def getExpectedFTCOutput(self, otc_output):
        ftc_expected_output=otc_output
        return ftc_expected_output

    def getMessage(self):
        pass

class MR1(MR):
    def getFTC(self, a, b, c):
        return [b, a, c]
    def getMessage(self):
        return "MR1:\n IF (a',b',c') = (b, a, c)\n THEN otc_output = ftc_output\n"

class MR2(MR):
    def getFTC(self, a, b, c):
        return [a, c, b]
    def getMessage(self):
        return "MR2:\n IF (a',b',c') = (a, c, b)\n THEN otc_output = ftc_output\n"

class MR3(MR):
    def getFTC(self, a, b, c):
        return [c, b, a]
    def getMessage(self):
        return "MR3:\n IF (a',b',c') = (c, b, a)\n THEN otc_output = ftc_output\n"

class MR4(MR):
    def getFTC(self, a, b, c):
        return [2*a, 2*b, 2*c]
    def getExpectedFTCOutput(self, otc_output):
        return 4*otc_output
    def getMessage(self):
        return "MR4:\n IF (a',b',c') = (2a, 2b, 2c)\n THEN otc_output = 4 * ftc_output\n"

class MR5(MR):
    def getFTC(self, a, b, c):
        return [math.sqrt(2*math.pow(b,2)+2*math.pow(c, 2) - math.pow(a, 2)), b, c]
    def getMessage(self):
        return "MR5:\n IF (a',b',c') = (sqrt(2b*b + 2c*c - a*a), b, c)\n THEN otc_output = ftc_output\n"

class MR6(MR):
    def getFTC(self, a, b, c):
        return [a, math.sqrt(2*math.pow(a,2)+2*math.pow(c, 2) - math.pow(b, 2)), c]
    def getMessage(self):
        return "MR6:\n IF (a',b',c') = (a, sqrt(2a*a + 2c*c - b*b), b, c)\n THEN otc_output = ftc_output\n"

class MR7(MR):
    def getFTC(self, a, b, c):
        return [a, b, math.sqrt(2*math.pow(a,2)+2*math.pow(b, 2) - math.pow(c, 2))]
    def getMessage(self):
        return "MR7:\n IF (a',b',c') = (a, b, sqrt(2a*a + 2b*b - c*c))\n THEN otc_output = ftc_output\n"

class MRComposition(MR):
    def __init__(self, mr_list):
        super(MRComposition, self).__init__()
        self.mr_list = mr_list

    def getFTC(self,a, b, c):
        result = [a, b, c]
        #print(self.mr_list)
        for mr in reversed(self.mr_list):
            result = mr.getFTC(result[0], result[1], result[2])
        return result

    def getExpectedFTCOutput(self, otc_output):
        result = otc_output
        for mr in reversed(self.mr_list):
            result = mr.getExpectedFTCOutput(result)
        return result

    def getMessage(self):
        message = ""
        for mr in self.mr_list:
            message =message+mr.getMessage()
        return message

"""Return the CMR instance by given a sequence of numbers"""
def ComposeMRs(list_of_numbers):
    current_module = sys.modules[__name__]
    mrs_to_compose = ["MR"+str(i) for i in list_of_numbers]
    mrs_list = [getattr(current_module, mr_name)() for mr_name in mrs_to_compose]
    return MRComposition(mrs_list)


LIB = ["MR1", "MR2", "MR3", "MR4", "MR5", "MR6", "MR7" ]

if __name__=="__main__":
    a = 4.0
    b = 4.0
    c = 4.0
    current_module = sys.modules[__name__]
    mr_to_initial = getattr(current_module,"MR7")
    mr = mr_to_initial()
    otc = [a, b, c]
    ftc = mr.getFTC(otc[0],otc[1],otc[2])
    for func in triangle.LIB:
        method_to_call = getattr(triangle,func)
        otc_output = method_to_call(otc[0],otc[1],otc[2])
        ftc_output = method_to_call(ftc[0],ftc[1],ftc[2])
        ftc_expect_output = mr.getExpectedFTCOutput(otc_output)
        AssertMRViolation(ftc_output,ftc_expect_output,mr.getMessage())
