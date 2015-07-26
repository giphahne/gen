#import json
#import math
#from functools import reduce
import re

from utils import utils
#from utils import fetch_uniprot_record


if __name__ == "__main__":

    #prot_id_file = "MPRT/sample_data"
    prot_id_file = "MPRT/rosalind_mprt.txt"

    output_file = "MPRT/output"
    
    
    with open(prot_id_file, "r") as f:
        prot_ids = [l.strip() for l in f.readlines()]

    print(prot_ids)

    n_glycosylation_motif = r"(?=N[^P][ST][^P])"

    prots = []
    for prot_id in prot_ids:
        print("---------------------------------------"
              "\nfetching: '{0}'... ".format(prot_id))
        seq = utils.fetch_uniprot_record(prot_id)["seq"]

        motif_locs = [m.start() + 1
                     for m in re.finditer(n_glycosylation_motif, seq)]
        print("found motif at locations: ", motif_locs)
        if motif_locs:
            prots.append({
                "id": prot_id,
                "locs": [str(l) for l in motif_locs]
            })

    with open(output_file, "w") as f:
        for item in prots:
            f.write(item["id"])
            f.write("\n")
            f.write(" ".join(item["locs"]))
            f.write("\n")
        
    
    
