import json 
#from collections import defaultdict

#dataset_file = "sample_data"
dataset_file = "rosalind_fib.txt"


memo={}
def G(n, k, b=1):
    """
    """

    args = (n, k, b)
    if args in memo:
        return memo[args]
    
    if n == 1 or n == 2:
        return b

    result = G(n-1, k) + k * G(n-2, k)
    memo[args] = result

    return result






with open(dataset_file, 'r') as f:
    s = f.read()

print(s)
n, k = s.split(" ")
print( G(int(n), int(k)) )


    

