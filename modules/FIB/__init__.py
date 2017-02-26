
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


def main(inf):

    s = inf.read()

    n, k = s.split(" ")
    return str(G(int(n), int(k)))


    

