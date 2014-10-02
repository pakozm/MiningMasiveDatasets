import pagerank

r = pagerank.pageRank([ [1,2],
                        [2],
                        [2] ], 0.7)
r = map(lambda x: 3*x, r)

print("a+b",r[0]+r[1])
print("a+c",r[0]+r[2])
print("b+c",r[1]+r[2])
