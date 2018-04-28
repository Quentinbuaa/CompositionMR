import sys
import itertools
import MatrixMultiplication.MatMrs as matmrs
import MatrixMultiplication.matrixmultiplication as spm
import MatrixMultiplication.TestCases as ts
import math
import Library.Log as logger
import statistics

def pickup(num, mrs, groups):
    if not len(mrs) == len(groups):
        print("The sizes of MRs and Groups don't match!")
    combinations_index_it = itertools.combinations(range(len(mrs)), num)
    mrs_to_combine_list_list =[]
    mrs_to_combine_group_set_list =[]
    for combination in combinations_index_it:
        mrs_combination = []
        group_set = []
        for index in combination:
            mrs_combination.append(getattr(matmrs, mrs[index])())
            group_index_temp = groups[index]
            if not group_index_temp in group_set:
                group_set.append(group_index_temp)
        mrs_to_combine_list_list.append(mrs_combination)
        mrs_to_combine_group_set_list.append(group_set)
    return mrs_to_combine_list_list, mrs_to_combine_group_set_list

def AssertMRViolation(ftc_output, ftc_expected_output, message):
    d = 0.00001
    row = len(ftc_expected_output)
    col = len(ftc_expected_output[0])
    if not (row == len(ftc_output) and col == len(ftc_output[0])):
        return True
    for i in range(row):
        for j in range(col):
            if math.fabs(ftc_output[i][j] - ftc_expected_output[i][j]) >= d:
                return True
    return False

def TestOneMR(mr, testcases, mutanted_versions):
    killed_mutants= []
    for mutant_index in mutanted_versions:
        matmultiple = spm.MatrixMultiple(mutant_index)
        for (otc_A, otc_B) in testcases:
            otc_output = matmultiple.MatMul(otc_A, otc_B)
            (ftc_expected_output, ftc_A, ftc_B,matmultiple.MatMul) = mr.getExpectedFTCOutput(otc_output, otc_A, otc_B,matmultiple.MatMul)
            ftc_output = matmultiple.MatMul(ftc_A, ftc_B)
            violation = AssertMRViolation(ftc_output, ftc_expected_output, mr.getMessage())
            if violation:
                killed_mutants.append(mutant_index)
                break
    return killed_mutants


"""Calculate the mutation score of a MR and a set of test cases"""
def mutation_score(killed_mutants, mutants):
    return float(len(killed_mutants)) / float(len(mutants))


def mutation_killed(mr):
    # mutants =  ["MU_1_SparseMatMul", "MU_2_SparseMatMul", "MU_3_SparseMatMul",
    #             "MU_4_SparseMatMul","MU_5_SparseMatMul","MU_6_SparseMatMul",
    #             "MU_7_SparseMatMul","MU_8_SparseMatMul"]
    mutants = ["MU_9_SparseMatMul", "MU_2_SparseMatMul", "MU_3_SparseMatMul",
               "MU_4_SparseMatMul", "MU_5_SparseMatMul", "MU_6_SparseMatMul",
               "MU_7_SparseMatMul", "MU_8_SparseMatMul"]
    #mutants = ["SparseMatMul"]
    myTestcases = ts.TestCases().getTestCases()
    killed_mutants = TestOneMR(mr, myTestcases, mutants)
    return (killed_mutants, mutation_score(killed_mutants, mutants))


""" Assess the efficiency of compounded of num of MRs."""
def AssessCompoundedMR(num):
    scores = []
    num_of_mrs_to_compose = num
    mrs = ["MR1", "MR2", "MR3","MR4", "MR5", "MR6","MR7", "MR8", "MR9"]
    groups = ["1", "2", "2", "3","3","4", "4", "5","5"]
    #mrs = ["MR4","MR9"]
    #groups = ["3","5"]
    #mrs = ["MR1", "MR2", "MR3", "MR4", "MR5", "MR6", "MR7"]
    #groups = ["1", "2", "2", "3", "3", "4", "4"]
    mrs_to_combine_list_list, mrs_to_combine_group_set_list = pickup(num_of_mrs_to_compose, mrs, groups)
    for i in range(len(mrs_to_combine_list_list)) :
        mrs_to_combine_list = mrs_to_combine_list_list[i]
        mrs_to_combine_group_set = mrs_to_combine_group_set_list[i]
        mr = matmrs.MRComposition(mrs_to_combine_list   )
        mr.set_diversity(len(mrs_to_combine_group_set))
        mr.set_num_of_mrs(len(mrs_to_combine_list))
        (killed_mutants, mutation_score) = mutation_killed(mr)
        scores.append((mr, mutation_score, killed_mutants))
    return scores

def Statistic(scores):
    diversity_list = []
    num_list = []
    score_list=[]
    two_d_average = []
    for (mr, score, list) in scores:
        diversity_list.append(mr.get_diversity())
        num_list.append(mr.get_num_of_mrs())
        score_list.append(score)
    my_dict = dict()
    two_d_index = tuple(zip(diversity_list, num_list))
    keys = set(two_d_index)
    for key in keys:
        my_dict[key] =[]
    for i in range(len(num_list)):
        my_dict[two_d_index[i]].append(score_list[i])
    for key, value in my_dict.items():
        two_d_average.append((key[0],key[1],statistics.mean(value)))
    return two_d_average

def main():
    myLogger = logger.Logger("Without16mutants.txt")
    myLogger2 = logger.Logger("Without16mutants_average.txt")
    scores = []
    for num in range(1, 10):
        scores = scores + AssessCompoundedMR(num)

    two_d_average = Statistic(scores)

    for (mr, score, list) in scores:
        print("{}: {} : {} : {}.\n".format(mr.getMessage(),mr.get_diversity(),mr.get_num_of_mrs(), score))
        print(list)
        myLogger.LogMutationScore("{}\t{}\t{}\t{}\n".format(mr.getMessage(), mr.get_diversity(),mr.get_num_of_mrs(), score))
    for (diversity, num, average) in two_d_average:
        print("{}: {} : {}.\n".format(diversity, num, average))
        myLogger2.LogMutationScore("{}\t{}\t{}\n".format(diversity, num, average))

if __name__ == "__main__":

    main()