import mrs
import triangle

def MetamorphicTesting(testcases, method_to_call):
    count =0
    for otc in testcases:
        count = count + 1
        violated_mrs = []
        for mr_to_initial in mrs.LIB:
            mr = getattr(mrs, mr_to_initial)()
            ftc = mr.getFTC(otc[0], otc[1], otc[2])
            otc_output = method_to_call(otc[0], otc[1], otc[2])
            ftc_output = method_to_call(ftc[0], ftc[1], ftc[2])
            ftc_expect_output = mr.getExpectedFTCOutput(otc_output)
            violation = mrs.AssertMRViolation(ftc_output, ftc_expect_output, mr.getMessage())
            if violation:
                violated_mrs.append(mr_to_initial)
        if len(violated_mrs)>0:
            print("original test case t{}:({} {} {}) violated {} MRs:\n".format(count,otc[0], otc[1], otc[2], len(violated_mrs)))
            for item in violated_mrs:
                print("{}\t",item)
            print("\n")
            violated_mrs = []


def TestOneMR(mr, testcases, mutanted_versions):
    killed_mutants= []
    for mutant in mutanted_versions:
        method_to_call = getattr(triangle, mutant)
        for otc in testcases:
            ftc = mr.getFTC(otc[0], otc[1], otc[2])
            otc_output = method_to_call(otc[0], otc[1], otc[2])
            ftc_output = method_to_call(ftc[0], ftc[1], ftc[2])
            ftc_expect_output = mr.getExpectedFTCOutput(otc_output)
            violation = mrs.AssertMRViolation(ftc_output, ftc_expect_output, mr.getMessage())
            if violation:
                killed_mutants.append(mutant)
                break
    return killed_mutants