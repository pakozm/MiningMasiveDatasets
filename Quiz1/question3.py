import pagerank

r = pagerank.pageRank([ [1,2], # A
                        [2],   # B
                        [0] ], # C
                      1.0,
                      verbose=False,
                      epsilon=1e-10)
r = map(lambda x: 3*x, r)

r5 = pagerank.pageRank([ [1,2], # A
                         [2],   # B
                         [0] ], # C
                       1.0,
                       maxIter=5,
                       verbose=False,
                       epsilon=1e-10)
r5 = map(lambda x: 3*x, r5)

r4 = pagerank.pageRank([ [1,2], # A
                         [2],   # B
                         [0] ], # C
                       1.0,
                       maxIter=4,
                       verbose=False,
                       epsilon=1e-10)
r4 = map(lambda x: 3*x, r4)

print(r)
print(r5)
print()
print("#inf",r[1], 3/5.0)
print("#inf",r[2], 4/3.0)
print("#5",r5[1], 1/2.0)
print("#5",r5[0], 13/8.0)

