

from rosalind_utils.utils import load_codon_table, chunks
       

def main(f):
    aas_codons = load_codon_table()
    
    rna_string = f.read()

    #print("rna_string:\n{}\n".format(rna_string))
    codons = chunks(rna_string, 3)
    aas = []
    for codon in codons:
        if codon in aas_codons:
            aas.append(aas_codons[codon])
        else:
            print("read codon ({0}) not found!".format(codon))

    result = "".join(aas).strip("*")
    #print("protein result:\n{}\n".format(result))

    return result
