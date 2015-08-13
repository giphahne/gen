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
    
    seqs = []
    for seq_id, seq in utils.ifasta_file(data_file):
    #for seq_id, seq in utils.ifasta_file("CONS/rosalind_cons.txt"):
        seqs.append(seq)
        
    dna_seq = seqs[0]
    
    """
    A better way to do this would be to 'cut' the seq at 
    all stop codons, and then parallelize the search for
    open reading frame substrings, which will begin with
    start codon, within each ORF substring. (by 'cut' it
    would be better to use indexes and iterators.)
    """
    
    
    print("\ndna_seq:", dna_seq)
    rna_seq = dna_seq.replace("T", "U")
    print("\nrna_seq:", rna_seq)
    print("seq len: {0}\n".format(len(seq)))

    start_codons, stop_codons, codons = utils.load_codon_tables()

    # for stop_codon in stop_codons.keys():
    #     print("replacing {0}".format(stop_codon))
    #     rna_seq = rna_seq.replace(stop_codon, "*")
    #     print("rna_seq:", rna_seq)


    #prot_function
    prots = chain(
        utils.prots_from_trailing_rseqs(utils.orfs_from_rseq(rna_seq),
                                        stop_codons, codons),
        utils.prots_from_trailing_rseqs(
            utils.orfs_from_rseq(utils.rev_comp(rna_seq)),
            stop_codons, codons)
    )

    prots = set(prots)
        
    
    with open(output_file, "w") as f:
        for prot in prots:
            f.write(prot + "\n")
            
            
