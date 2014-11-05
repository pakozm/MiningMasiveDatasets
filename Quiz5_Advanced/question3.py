import math

points = [
    (1,6),
    (3,7),
    (4,3),
    (7,7),
    (8,2),
    (9,5)
]

selection = [
    (0,0),
    (10,10)
]

def min_distance(p, selection):
    return min([ (p[0]-s[0])**2 + (p[1]-s[1])**2 for s in selection ])

for i in range(5):
    which=-1
    m=0
    for point,j in zip(points,range(len(points))):
        d = min_distance(point, selection)
        if d > m:
            m = d
            which = j
    print i,points[which]
    selection.append(points[which])
    points.pop(which)
