def computeIncidenceMatrix(outM):
    N = len(outM)
    inM = [ [] for i in range(0,N) ]
    for i in range(0,N):
        for j in outM[i]:
           inM[j].append(i)
    return inM

def computeDegree(M):
    return [ len(x) for x in M ]

# outM is an adjacency matrix
# beta is the smooth parameter (avoids "spider traps")
def pageRank(outM, beta, verbose=False, epsilon=None, maxIter=float("inf")):
    inM = computeIncidenceMatrix(outM)
    # d_in = computeDegree(outM)
    d_out = computeDegree(outM)
    EPSILON = 1e-06 if epsilon is None else epsilon
    beta = float(beta)
    N = len(outM)
    r = [1.0/N]*N
    it = 0
    if verbose:
        print("it", "r", "diff", "leak")
        print(it, r, float("inf"), 0)
    while True:
        rp = [ sum([ beta*r[i]/d_out[i] for i in inM[j] ]) for j in range(0,N) ]
        # reinsert the leaked PageRank
        S = sum(rp)
        leak = (1.0-S)/N
        rp = map(lambda rp_j: rp_j + leak, rp)
        diff = sum(map(lambda r_j,rp_j: abs(r_j - rp_j), r, rp), 0)
        r = rp
        it = it + 1
        if verbose:
            print (it, r, diff, leak)
        if diff < EPSILON:
            break
        if it >= maxIter:
            break
    return r

if __name__ == "__main__":
    r = pageRank([ [0,1],   # y
                   [0,2],   # a
                   [2] ],   # m
                 0.8) 
    print(r)
    print([7.0/33, 5.0/33, 21.0/33])
