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

        
def prob_off_hom_rec(homr, het, homd):
    """
    """
    tot = homr + het + homd

    return ( ((homr * homr) - homr + (homr * het) + (het * het)/4 - het/4 )/
                             ((tot * tot) - tot) ) 
        

def main(f):
    
    s = f.readline().strip().split()

    print(s)
    prob = prob_off_hom_rec(int(s[2]), int(s[1]), int(s[0])) 
    full_result = "{} {}".format(prob, 1 - prob)
    result = "{}".format(1 - prob)
    print(full_result)
    return result

    # print(binom_r(6, 2))
    # print(mbinom_r(6, 2))
    # print(binom_f(6, 2))

