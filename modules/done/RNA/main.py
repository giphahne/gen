import json 
from collections import defaultdict


#dataset_file = "sample_data"
#dataset_file = "dataset"
dataset_file = "rosalind_rna.txt"

with open(dataset_file, 'r') as f:
    dna_string = f.read()

rna_string = dna_string.replace("T", "U")

print(rna_string)
