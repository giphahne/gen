from itertools import groupby

import requests


def ifasta_file(fasta_fd):
    """
    Yield tuples:
        (<header>, <sequence>)
    from fasta file.

    Introduced for GC
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
    """
    Introduced for GC
    """
    return (seq.count("G") + seq.count("C")) / len(seq)


def fetch_uniprot_record(prot_id):
    """
    Introduced for MPRT
    """
    prot_url = "http://www.uniprot.org/uniprot/{0}.fasta".format(prot_id)
    prot_resp = requests.get(prot_url)
    prot_fasta = prot_resp.content.decode().split("\n")

    header = prot_fasta.pop(0)
    prot_seq = "".join(prot_fasta)
    #print("\nheader: ", header)
    #print("\nseq: ", seq)

    header = header.split(" ")
    prot_id = header.pop(0).lstrip(">")
    prot_desc = " ".join(header)

    #print("prot_id: ", prot_id)
    #print("prot_desc: ", prot_desc)
    

    #print(prot_resp.content)
    
    return {
        "id": prot_id,
        "desc": prot_desc,
        "seq": prot_seq
    }  
    

def find_motif(motif, seq):
    """
    Introduced for MPRT
    """
    pass

    

def load_codon_table(codon_table_file="utils/codon_table"):
    """
    """
    codons = {}
    
    with open(codon_table_file, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            #print(line)
            if line:
                codons[line[0]] = line[1]
                #codons[line[1]] = line

    return codons
    

def load_aa_mass_table(aa_mass_table_file="utils/aa_masses_table"):
    """
    """
    masses = {}
    
    with open(aa_mass_table_file, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            print(line)
            if line:
                masses[line[0]] = line[1]
                #masses[line[1]] = line

    return masses
    

def chunks(string, n):
    """
    """
    for i in range(0, len(string), n):
        print(string[i:i+n])
        yield string[i:i+n]
    
                
def binom_f(n, k):
    if n == k:
        return 1
    elif k == 1:
        return n
    elif k == 0:
        return 1
    elif k > n: 
        return 0
    else:       
        nf = math.factorial(n)
        kf = math.factorial(k)
        n_kf = math.factorial(n-k)
        return (nf / (kf * n_kf))


def mbinom_r(n, k, memo={}):

    if (n, k) in memo:
        return memo[(n, k)]
    
    if n == k or k == 0:
        return 1

    result = mbinom_r(n - 1, k - 1, memo) + mbinom_r(n - 1, k, memo)
    memo[(n, k)] = result

    return result


def binom_r(n, k):
    if n == k or k == 0:
        return 1
    return mbinom_r(n - 1, k - 1) + mbinom_r(n - 1, k)


def find_all(sub_str, a_str):
    """
    """
    start = 0
    while True:
        start = a_str.find(sub_str, start)
        if start == -1:
            return
        yield start + 1
        start += 1

        
def find_all_regex():
    pass

        
def prob_of_hom_rec(homr, het, homd):
    """
    """
    tot = homr + het + homd

    return ( ((homr * homr) - homr + (homr * het) + (het * het)/4 - het/4 )/
                             ((tot * tot) - tot) ) 
        
