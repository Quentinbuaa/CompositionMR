import triangle
import mrs
from MetamorphicTesting import *


t1 = [3.0, 4.0, 5.0]
t2 = [3.0, 3.0, 5.0]
t3 = [3.0, 4.0, 3.0]
t4 = [5.5, 3.3, 3.3]
t5 = [3.4, 3.4, 3.4]

testcases = [t1, t2, t3, t4, t5]
LIB = ["trisquare", "MU_1_trisquare", "MU_2_trisquare", "MU_3_trisquare","MU_4_trisquare"]

def main():
    #for func in triangle.LIB:
    method_to_call = getattr(triangle, LIB[1])
    #print("The current testing version is: {}\n".format(func))
    MetamorphicTesting(testcases, method_to_call)


