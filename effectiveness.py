import triangle
import testcases as TC
import mrs
import MetamorphicTesting as MT




"""Calculate the mutation score of a MR and a set of test cases"""
def mutation_score(killed_mutants, mutants):
    return float(len(killed_mutants)) / float(len(mutants))


def mutation_killed(mr_to_test, test_cases):
    mr = getattr(mrs, mr_to_test)()
    mutants =  ["MU_1_trisquare", "MU_2_trisquare", "MU_3_trisquare","MU_4_trisquare"]
    killed_mutants = MT.TestOneMR(mr, test_cases, mutants)
    return (killed_mutants, mutation_score(killed_mutants, mutants))

def main():
    scores = []
    for mr in mrs.LIB:
        print("{}\n".format(mr))
        (killed_mutants, mutation_score) = mutation_killed(mr, TC.testcases)
        scores.append((mr, mutation_score, killed_mutants))
    for (mr, score, list) in scores:
        print("{}: {}\n".format(mr, score))
        for mu in list:
            print("{}\t".format(mu))
        print("\n")


if __name__ =="__main__":
    main()