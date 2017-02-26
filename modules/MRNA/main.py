import json
import math
from utils import utils
from functools import reduce


if __name__ == "__main__":
    
    #dataset_file = "MRNA/sample_data"
    dataset_file = "MRNA/rosalind_mrna.txt"
    
    with open(dataset_file, "r") as f:
        aastr = f.read()

    #print("amino acid: ", aastr)
    codons = utils.load_codon_table()
    
    counts = []
    for aa in aastr:
        if aa in codons.values():
            counts.append( sum(1 for x in codons.values() if x == aa) )

    counts.append( sum(1 for x in codons.values() if x == "*") )

    print(counts)

    #total = 0
    total = reduce(lambda x, y: x * y, counts)
    print(total % 1000000)
    #for 
    #print(json.dumps(codons, indent=4))

