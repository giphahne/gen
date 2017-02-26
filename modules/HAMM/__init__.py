#import json 
#from itertools import groupby
#from collections import defaultdict


def hamm_dist(s1, s2):
    """
    """
    dist = 0
    distbool = 0
    for c1, c2 in zip(s1, s2):
        distbool += bool( (c1 != c2) )

    return distbool


def main(f):
    rna_string_one = f.readline()
    rna_string_two = f.readline()

    print(len(rna_string_one))
    result = hamm_dist(rna_string_one, rna_string_two)
    print(result)
        
    return str(result)
