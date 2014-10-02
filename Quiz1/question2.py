import pagerank

r = pagerank.pageRank([ [1,2], # A
                        [2],   # B
                        [1] ], # C
                      0.85)
r = map(lambda x: 3*x, r)

print(r)
