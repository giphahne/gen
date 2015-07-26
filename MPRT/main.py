#import json
#import math
from utils import utils
#from functools import reduce

import requests


if __name__ == "__main__":
    
    prot_id_file = "MPRT/sample_data"
    #prot_id_file = "MPRT/rosalind_mprt.txt"
    
    with open(prot_id_file, "r") as f:
        prot_ids = [l.strip() for l in f.readlines()]

    print(prot_ids)
    

