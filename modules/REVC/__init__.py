

#dataset_file = "sample_data"
#dataset_file = "dataset"
dataset_file = "rosalind_revc.txt"

def main(inf):

    comps = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    def comp(nc):
        if nc == "\n":
            return ""
        return comps[nc]


    s = inf.read()

    sc = ""
    for nc in s:
        sc += comp(nc)

    scr = sc[::-1]

    return scr
