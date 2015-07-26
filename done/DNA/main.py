import json 
from collections import defaultdict


dataset_file = "rosalind_dna.txt"
with open(dataset_file, 'r') as f:
    f_string = f.read()


counts = defaultdict(int)
for nuc in f_string:
    counts[nuc] += 1

counts.pop("\n", None)

print(json.dumps(counts, indent=4, sort_keys=True))
