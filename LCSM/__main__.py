import sys
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

sys.path.append("/Users/dhahne/Development/rosalind/")
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
    #print("data_file_name:", data_file_name)
    data_file = os.path.join(unit_name, data_file_name)
    output_file = os.path.join(unit_name, output_file_name)
    print("data file:", data_file)
    print("\n\n")

    ####################################################################
    
    
    
    seqs = list(ifasta_file(data_file, with_headers=False))
    n = len(seqs)
    #print("seqs:", seqs)
    #for seq_id, seq in seqs:
    #z = 0
    lcsm = ""
    for i in range(n):
        for j in range(i, n):
            #print("\n**********\n")
            ith_lcsm = longest_common_substr(seqs[i], seqs[j],
                                             just_one=True)
            # ith_lcsm = longest_common_substr(seqs[i], seqs[j],
            #                                  just_one=False)
            # print("\n"            
            #       "common-ing: \n"
            #       "{0}\n"
            #       "{1}\n"
            #       "ith_lcsm: {2}"
            #       .format(seqs[i], seqs[j], ith_lcsm))

            if len(ith_lcsm) > len(lcsm) and in_all(ith_lcsm, seqs):
                # print("ith is longer than current: {0} > {1}"
                #       .format(ith_lcsm, lcsm))
                lcsm = ith_lcsm
        #print("seq: {0}".format(seqs[i]))
    print("lcsm:", lcsm)

    with open(output_file, "w") as f:
        f.write("\n")
        f.write(lcsm)
        f.write("\n")
            
    print("\n\n")            
