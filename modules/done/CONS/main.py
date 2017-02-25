#import json
#import math
#from functools import reduce
import re
import os
from collections import defaultdict
from functools import partial
import argparse
import operator
    
from utils import utils
#from utils import fetch_uniprot_record


#def seqs_profiler(profile, *nts):
def nts_profiler(*nts, nts_set=None):
    """  """
    print(nts)
    profile_i = defaultdict(int)

    if nts_set:
        profile_i.update([(k, 0) for k in nts_set])
    
    for nt in nts:
        profile_i[nt] += 1

    print("profile_i:", profile_i)
    #profile_i
    #profile.append(curr_nts)

    return profile_i



    
if __name__ == "__main__":
    unit_name = os.path.dirname(os.path.realpath(__file__))
    
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

    data_file = os.path.join(unit_name, data_file_name)
    output_file = os.path.join(unit_name, output_file_name)
    print("data file:", data_file)
    
    seqs = []
    #for seq_id, seq in utils.ifasta_file(data_file):
    for seq_id, seq in utils.ifasta_file("CONS/rosalind_cons.txt"):
        seqs.append(seq)

    print("\n\n")
    print(seqs)

    profs = list(map(nts_profiler, *seqs))

    nts_reduction = set()
    for prof in profs:
        nts_reduction.update(prof)

    print(nts_reduction)

    full_nts_profiler = partial(nts_profiler, nts_set=nts_reduction)
    full_profs = list(map(full_nts_profiler, *seqs))
    
    print("done", "\n\n", full_profs)    

    cons_seq = ""
    for prof in full_profs:
        cons_seq += max(prof.items(), key=operator.itemgetter(1))[0]
    
    with open(output_file, "w") as f:
        f.write(cons_seq)

        for nt in sorted(nts_reduction):
            f.write("\n" + nt + ":")

            for prof in full_profs:
                f.write(" " + str(prof[nt]))
            
            
