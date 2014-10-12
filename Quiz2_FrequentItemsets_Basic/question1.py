def computeAPrioriMemorySize(N,M):
    # 1 million elements
    NUM_ELEMENTS = 1000000
    NUM_FREQ_PAIRS = 1000000
    # 4 bytes each integer
    NBYTES = 4
    freq_item_set_size = NUM_ELEMENTS * NBYTES
    triangular_matrix_approach_size = (N * (N+1) / 2 * NBYTES) + freq_item_set_size
    tabular_approach_size = (M + NUM_FREQ_PAIRS) * 3 * NBYTES + freq_item_set_size
    return [triangular_matrix_approach_size, tabular_approach_size]

# attempt 1
#for N,M,S in [ (50000,200000000,2500000000), (60000,200000000,7200000000), (50000,40000000,800000000), (40000,60000000,3200000000) ]:
#    a,b = computeAPrioriMemorySize(N,M)
#    g = min(a,b)
#    print(N,M,a,b,g,S)

# attempt 2
for N,M,S in [ (20000,80000000,1100000000), (30000,200000000,1800000000), (40000,60000000,3200000000), (100000,40000000,800000000) ]:
    a,b = computeAPrioriMemorySize(N,M)
    g = min(a,b)
    print(N,M,a,b,g,S)
