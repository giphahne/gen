#import json 
from itertools import groupby
#from collections import defaultdict


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


if __name__ == "__main__":
    
    #dataset_file = "sample_data"
    dataset_file = "rosalind_subs.txt"
    
    with open(dataset_file, "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()

    subs = find_all(t, s)
    
    print("\n")            
    for i in subs:
        print(i, " ", sep="", end="")
    print("\n")        
        
