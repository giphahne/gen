import json 
from itertools import groupby
#from collections import defaultdict


def load_codon_table(codon_table_file, codons):
    """
    """
    with open(codon_table_file, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            #print(line)
            if line:
                codons[line[0]] = line
                codons[line[1]] = line


def chunks(string, n):
    """
    """
    for i in range(0, len(string), n):
        print(string[i:i+n])
        yield string[i:i+n]
    
                

if __name__ == "__main__":
    
    codon_file = "codon_table"
    
    #dataset_file = "sample_data"
    dataset_file = "rosalind_prot.txt"
    
    aas_codons = {}
    load_codon_table(codon_file, aas_codons)
    #print(json.dumps(codons, indent=4))

    with open(dataset_file, "r") as f:
        rna_string = f.read()

    codons = chunks(rna_string, 3)
    aas = []
    for codon in codons:
        if codon in aas_codons:
            aas.append(aas_codons[codon][1])
        else:
            print("read codon ({0}) not found!".format(codon))

        
    print("\n", "".join(aas).strip("*"), "\n")
        
