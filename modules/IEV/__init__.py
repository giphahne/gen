import math

from rosalind_utils import utils


def expected_dom_offspring(pop_demo):
    """
    IEV
    """
    probs = [1, 1, 1, 0.75, 0.5, 0]
    offspring = [2, 2, 2, 2, 2, 2]

    expected = [j * k for j, k in zip(probs, offspring)]
    #print(expected)
    expecting = [j * int(k) for j, k in zip(expected, pop_demo)]
    #print(expecting)
    return sum(expecting)


#if __name__ == "__main__":
def main(f):
    
    #dataset_file = "sample_data"
    #dataset_file = "rosalind_iev.txt"
    
    #with open(dataset_file, "r") as f:
    
    s = f.readline().strip().split()

    print(s)
    
    expected = expected_dom_offspring(s)
    print(expected)
    
    return str(expected)
    # print(binom_r(6, 2))
    # print(mbinom_r(6, 2))
    # print(binom_f(6, 2))

