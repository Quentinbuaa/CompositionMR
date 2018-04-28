import mrs
import testcases as TC
import MetamorphicTesting as MT


ll = []
class MRComposition(mrs.MR):
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
    mrs_to_compose = ["MR"+str(i) for i in list_of_numbers]
    mrs_list = [getattr(mrs, mr_name)() for mr_name in mrs_to_compose]
    return MRComposition(mrs_list)



"""Calculate the mutation score of a MR and a set of test cases"""
def mutation_score(killed_mutants, mutants):
    return float(len(killed_mutants)) / float(len(mutants))


def mutation_killed(mr, test_cases):
    mutants =  ["MU_1_trisquare", "MU_2_trisquare", "MU_3_trisquare","MU_4_trisquare"]
    killed_mutants = MT.TestOneMR(mr, test_cases, mutants)
    return (killed_mutants, mutation_score(killed_mutants, mutants))

def runMT(mr):
    scores = []
    print("{}\n".format(mr.getMessage()))
    (killed_mutants, mutation_score) = mutation_killed(mr, TC.testcases)
    scores.append((mr, mutation_score, killed_mutants))
    for (mr, score, list) in scores:
        print("{}:                                                      {}\n".format(mr.getMessage(), score))
        ll.append(score)

        #for mu in list:
        #    print("{}\t".format(mu))
        #print("\n")

def get_list_of_number():
    #G1 = [[5, 1, 2], [5, 1, 3],[5, 2, 3], [1, 5, 6],[1, 5, 7],[1, 6, 7],
     #     [6, 1, 2], [6, 1, 3], [6, 2, 3], [2, 5, 6], [2, 5, 7], [2, 6, 7],
      #    [7, 1, 2], [7, 1, 3], [7, 2, 3], [3, 5, 6], [3, 5, 7], [3, 6, 7]]
    G1 = [[1, 2, 3],[5, 6, 7]]
    for i in G1:
            runMT(ComposeMRs(i))

def print_list_of_number():
    G1 = [[5, 1, 2], [5, 1, 3],[5, 2, 3], [1, 5, 6],[1, 5, 7],[1, 6, 7],
          [6, 1, 2], [6, 1, 3], [6, 2, 3], [2, 5, 6], [2, 5, 7], [2, 6, 7],
          [7, 1, 2], [7, 1, 3], [7, 2, 3], [3, 5, 6], [3, 5, 7], [3, 6, 7]]
    G1 = [[1, 2, 3], [5, 6, 7]]
    for i in G1:
        print(i[0], i[1], i[2])
    print(ll)

def main():
    get_list_of_number()



if __name__ == "__main__":
    main()
    print_list_of_number()