ITEMS = 100
BASKETS = 100

baskets = [ [] for i in range(0,BASKETS) ]
for j in range(0,BASKETS):
    for i in range(1,i+1):
        if (j+1) % i == 0:
            baskets[j].append(i)

#for i in range(0,len(baskets)):
#    print i+1,baskets[i]

# for lhs,rhs in [ [[2,4], 8],
#                  [[4,6], 12],
#                  [[8], 16],
#                  [[1,2], 4] ]:
for lhs,rhs in [ [[2,4], 8],
                 [[3,4,5], 42],
                 [[12,18], 36],
                 [[4,10,12], 80] ]:
    lhs_counts = 0
    joint_counts = 0
    for b in baskets:
        contains_lhs = True
        for v in lhs:
            if v not in b:
                contains_lhs = False
        if contains_lhs:
            lhs_counts = lhs_counts + 1
            if rhs in b:
                joint_counts = joint_counts + 1
    print(lhs, rhs, float(joint_counts)/lhs_counts)
