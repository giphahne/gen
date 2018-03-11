#import json 
import math
#from itertools import groupby
#from collections import defaultdict

#from scipy import stats


def binom_f(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k == 0:
        return 1
    elif k > n: 
        return 0
    else:       
        nf = math.factorial(n)
        kf = math.factorial(k)
        n_kf = math.factorial(n-k)
        return (nf / (kf * n_kf))


def mbinom_r(n, k, memo={}):

    if (n, k) in memo:
        return memo[(n, k)]
    
    if n == k or k == 0:
        return 1

    result = mbinom_r(n - 1, k - 1, memo) + mbinom_r(n - 1, k, memo)
    memo[(n, k)] = result

    return result


def binom_r(n, k):
    if n == k or k == 0:
        return 1
    return mbinom_r(n - 1, k - 1) + mbinom_r(n - 1, k)


def find_all(sub_str, a_str):
    """
    """
    start = 0
    while True:
        start = a_str.find(sub_str, start)
        if start == -1:
            return
        yield start + 1
        start += 1

        
def prob_of_hom_rec(homr, het, homd):
    """
    IPRB
    """
    tot = homr + het + homd

    return ( ((homr * homr) - homr + (homr * het) + (het * het)/4 - het/4 )/
                             ((tot * tot) - tot) ) 
        

def expected_dom_offspring(pop_demo):
    """
    IEV
    """
    probs = [1, 1, 1, 0.75, 0.5, 0]
    offspring = [2, 2, 2, 2, 2, 2]

    expected = [j * k for j, k in zip(probs, offspring)]
    print(expected)
    expecting = [j * int(k) for j, k in zip(expected, pop_demo)]
    print(expecting)
    return sum(expecting)
    
if __name__ == "__main__":
    
    #dataset_file = "sample_data"
    dataset_file = "rosalind_iev.txt"
    
    with open(dataset_file, "r") as f:
        s = f.readline().strip().split()

    print(s)
    
    expected = expected_dom_offspring(s)
    print(expected)
    
    # print(binom_r(6, 2))
    # print(mbinom_r(6, 2))
    # print(binom_f(6, 2))

