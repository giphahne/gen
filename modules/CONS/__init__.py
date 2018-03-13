from collections import defaultdict
from functools import partial
import operator
#from mmap import mmap

from rosalind_utils import utils


def nts_profiler(*nts, nts_set=None):
    """ 
    """
    profile_i = defaultdict(int)

    if nts_set:
        profile_i.update([(k, 0) for k in nts_set])
    
    for nt in nts:
        profile_i[nt] += 1

    return profile_i



def main(f):
    
    seqs = []
    for seq_id, seq in utils.ifasta_file(f):
        seqs.append(seq)

    profs = list(map(nts_profiler, *seqs))

    nts_reduction = set()
    for prof in profs:
        nts_reduction.update(prof)

    full_nts_profiler = partial(nts_profiler, nts_set=nts_reduction)
    full_profs = list(map(full_nts_profiler, *seqs))
    
    cons_seq = ""
    for prof in full_profs:
        cons_seq += max(prof.items(), key=operator.itemgetter(1))[0]


    scratch_file = "/tmp/rosalind_cons_scratchpad"

    #mm_scratch = mmap()
    with open(scratch_file, "w") as outf:
        outf.write(cons_seq)
        
        for nt in sorted(nts_reduction):
            outf.write("\n" + nt + ":")
            
            for prof in full_profs:
                outf.write(" " + str(prof[nt]))


    with open(scratch_file, "r") as outf:                
        return outf.read()
