# import json 
# from collections import defaultdict

# def main(inf):
    
#     # dataset_file = "rosalind_dna.txt"
#     # with open(dataset_file, 'r') as f:
#     #     f_string = f.read()


#     print("reading dataset file...")
#     f_string = inf.read()
#     print("done.")
    
#     counts = defaultdict(int)
#     for nuc in f_string:
#         counts[nuc] += 1

#     counts.pop("\n", None)

#     output_string = " ".join(*sorted(counts.values()))

#     return output_string
#     #outf.write(output_string)
