import pagerank

r = pagerank.pageRank([ [1,2], # A
                        [2],   # B
                        [0] ], # C
                      0.85)
#r = map(lambda x: 3*x, r)

print(r)
print()
print(0.95*r[1], 0.475*r[0] + 0.05*r[2])
print(r[2], r[1] + 0.575*r[0])
print(85*r[1], 0.575*r[0] + 0.15*r[2])
print(0.85*r[2], r[1] + 0.575*r[0])
#print(r[2], 0.9*r[1] + 0.475*r[0])
