import distances

a = [0,0]
b = [100,40]
points =[
    [56,15],
    [52,13],
    [61,8],
    [55,5],
]

for p in points:
    print p
    print distances.L1_distance(p, a), distances.L1_distance(p, b)
    print distances.L2_distance(p, a), distances.L2_distance(p, b)
    print "####################################################"
