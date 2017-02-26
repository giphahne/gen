
def main(inf):
    
    dna_string = inf.read()

    rna_string = dna_string.replace("T", "U")

    return rna_string
