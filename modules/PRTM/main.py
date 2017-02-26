import json
import math
from utils import utils
from functools import reduce


if __name__ == "__main__":
    
    #dataset_file = "PRTM/sample_data"
    dataset_file = "PRTM/rosalind_prtm.txt"
    
    with open(dataset_file, "r") as f:
        aastr = f.read()
    
    #print("amino acid: ", aastr)
    mass_table = utils.load_aa_mass_table()
    
    masses = []
    for aa in aastr:
        if aa in mass_table.keys():
            masses.append(float(mass_table.get(aa)))
        else:
            print(aa, " -- AA. not found in table!")
        

    print("\n\n", masses, "\n\n")

    #total = 0
    #total = reduce(lambda x, y: x + y, counts)
    total = sum(masses)
    print(total)
    #for 
    #print(json.dumps(codons, indent=4))

