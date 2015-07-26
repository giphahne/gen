


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

        
def prob_of_hom_rec(homr, het, homd):
    """
    """
    tot = homr + het + homd

    return ( ((homr * homr) - homr + (homr * het) + (het * het)/4 - het/4 )/
                             ((tot * tot) - tot) ) 
        
