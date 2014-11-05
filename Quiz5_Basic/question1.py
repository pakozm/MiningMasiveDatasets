points = [
    (28,145,'y'), # 0
    (65,140,'y'), # 1
    (25,125,'g'), # 2
    (50,130,'y'), # 3
    (38,115,'y'), # 4
    (55,118,'y'), # 5
    (44,105,'g'), # 6
    (29,97,'g'),  # 7
    (50,90,'y'),  # 8
    (63,88,'y'),  # 9
    (43,83,'y'),  # 10
    (35,63,'g'),  # 11
    (55,63,'g'),  # 12
    (42,57,'g'),  # 13
    (50,60,'y'),  # 14
    (23,40,'g'),  # 15
    (64,37,'g'),  # 16
    (33,22,'g'),  # 17
    (50,30,'y'),  # 18
    (55,20,'g')   # 19
]

def closest(x):
    d = float('inf')
    which = -1
    for c,i in zip(centroids,range(len(centroids))):
        current_d = (x[0]-c[0])**2 + (x[1]-c[1])**2
        if current_d < d:
            which = i
            d = current_d
    return which

def assign_points(points):
    return map(closest, points)

def recompute_centroids(clusters,centroids):
    new_counts = [0]*len(centroids)
    new_centroids = [ [0,0] for i in range(len(centroids)) ]
    for which,point in zip(clusters,points):
        new_centroids[which][0] += point[0]
        new_centroids[which][1] += point[1]
        new_counts[which] += 1
    return [ [new_centroids[i][0]/float(new_counts[i]),
              new_centroids[i][1]/float(new_counts[i])]
             for i in range(len(new_centroids)) ]
             
####################################################################

centroids = [ [p[0],p[1]] for p in filter(lambda x: x[2]=='g', points) ]
assert( len(centroids) == 10 )
clusters = assign_points(points)
print clusters
print centroids

centroids = recompute_centroids(clusters,centroids)
clusters = assign_points(points)
print clusters
print centroids
