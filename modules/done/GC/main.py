import json 
from itertools import groupby
#from collections import defaultdict

#dataset_file = "sample_data"
dataset_file = "rosalind_gc.txt"


def ifasta(fasta_fd):
    """
    Yield tuples:
        (<header>, <sequence>)
    from fasta file.
    """
    fh = open(fasta_fd)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        # drop the ">"
        header = next(header)[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in next(faiter))
        yield header, seq


def gc_con(seq):
    return (seq.count("G") + seq.count("C")) / len(seq)


fastas = ifasta(dataset_file)
seq_gcs = {}

for seq in fastas:
    seq_gcs[seq[0]] = gc_con(seq[1])
    
print(json.dumps(seq_gcs, indent=4))

gc_max_seq = max(seq_gcs, key=seq_gcs.get)
print("\n", gc_max_seq, "\n", seq_gcs[gc_max_seq]*100, "\n")





    

