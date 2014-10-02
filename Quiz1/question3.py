import pagerank

r = pagerank.pageRank([ [1,2], # A
                        [2],   # B
                        [1] ], # C
                      1.0,
                      verbose=True,
                      epsilon=1e-10)
r = map(lambda x: 3*x, r)

print(r)
