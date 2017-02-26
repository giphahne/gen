import os
#import math
import re
from itertools import chain
from functools import partial
#from functools import reduce
from collections import defaultdict
import operator
import argparse
#import json

    
from utils.utils import *

    
if __name__ == "__main__":
    unit_path, file_name = os.path.split(os.path.realpath(__file__))
    path_name, unit_name = os.path.split(unit_path)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sampledata", action="store_true",
                        default=False,
                        help="run this module against the sample_data")
    args = parser.parse_args()

    if args.sampledata:
        data_file_name = "sample_data"
    else:
        data_file_name = "rosalind_{0}.txt".format(unit_name.lower())
        
    output_file_name = "output"
    
    print("unit_name:", unit_name)
    print("data_file_name:", data_file_name)
    data_file = os.path.join(unit_name, data_file_name)
    output_file = os.path.join(unit_name, output_file_name)
    print("data file:", data_file)

    ####################################################################
    
    
    
    seqs = ifasta_file(data_file)

    seq = next(seqs)[1]
    introns = list(seqs) 
    #for seq_id, seq in ifasta_file("CONS/rosalind_cons.txt"):
    #seqs.append(seq)

    print("\nseq: {0}\n"
          "introns: {1}\n\n".format(seq, len(introns)))
    for intron in introns:
        intron = intron[1]
        print(seq)        
        index = seq.find(intron)
        print(" "*(index-1), intron)
        seq = seq[:index] + seq[index+len(intron):]

    coding_region = seq
    print(coding_region, "\ncoding_region ^ \n")


    rna_coding_region = list(orfs_from_rseq("".join(list(id2r(coding_region)))))[0]
    print("rna_coding_region:", rna_coding_region)
    prots = prots_from_trailing_rseqs([rna_coding_region])
    poly_peptide = ""
    for prot in prots:
        poly_peptide += prot
    print("\n\n", poly_peptide, "\n\n")
    

    
        
        

    
    with open(output_file, "w") as f:
        f.write("\n")
            
            
