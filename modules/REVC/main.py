import json 
from collections import defaultdict


#dataset_file = "sample_data"
#dataset_file = "dataset"
dataset_file = "rosalind_revc.txt"

comps = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
}

def comp(nc):
    if nc == "\n":
        return ""
    return comps[nc]


with open(dataset_file, 'r') as f:
    s = f.read()

sc = ""
for nc in s:
    sc += comp(nc)

scr = sc[::-1]
    
print(scr)
