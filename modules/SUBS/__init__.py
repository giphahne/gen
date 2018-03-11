
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


def main(f):
    
    s = f.readline().strip()
    t = f.readline().strip()

    subs = find_all(t, s)

    motifs = []
    
    for i in subs:
        motifs.append(str(i))
        
    result = " ".join(motifs)

    # print("string:\n{}\n".format(s))
    # print("motif:\n{}\n".format(t))
    print("result:\n{}".format(result))
    
    return result

        
