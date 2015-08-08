#import json
#import math
#from functools import reduce
import re
import os
from collections import defaultdict

from utils import utils
#from utils import fetch_uniprot_record


if __name__ == "__main__":

    # Overlap Graphs
    unit_name = "GRPH"

    #data_file_name = "sample_data"
    data_file_name = "rosalind_{0}.txt".format(unit_name.lower())
    output_file_name = "output"

    data_file = os.path.join(unit_name, data_file_name)
    output_file = os.path.join(unit_name, output_file_name)


    heads = defaultdict(list)
    tails = defaultdict(list)

    # overlap of 'k' nts:
    k = 5
    
    for seq_id, seq in utils.ifasta_file(data_file):
        tails[seq[-k:]].append(seq_id)
        heads[seq[:k]].append(seq_id)
        
    print(heads)
    print("\n\n")
    print(tails)

    with open(output_file, "w") as f:
        
        for tail, ids in tails.items():
            print("\n", tail, ids)
            children = heads.get(tail, [])
            print("\t", children)
            for seq_id in ids:
                for child in children:
                    if child != seq_id:
                        f.write("{0} {1}\n".format(seq_id, child))
        
    
    
