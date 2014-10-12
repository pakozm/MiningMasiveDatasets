def computePYCSize(S):
    s = 10000 # support threshold
    NUM_ITEMS = 1000000
    NUM_FREQ_ITEMS = 250000 # items count >= s
    NUM_FREQ_PAIRS = 1000000 # pairs count >= s
    NBYTES = 4 # integer size
    item_counts_size = NUM_ITEMS * NBYTES
    hash_size = S - item_counts_size
    freq_items_size = NUM_FREQ_ITEMS * NBYTES
    bitmap_size = hash_size / 32
    candidate_pairs_counts_size = S - freq_items_size - bitmap_size
    num_candidate_pairs = candidate_pairs_counts_size / (3 * NBYTES)
    total_candidates = 3 * num_candidate_pairs
    P = total_candidates - NUM_FREQ_PAIRS
    return P
    
for S,P in [ [300000000,3500000000],
             [300000000,1800000000],
             [200000000,400000000],
             [300000000,750000000] ]:
    print(S,P,computePYCSize(S))
