yellow = (5,10)
blue = (20,5)
instances = (
    ( ( ( 7, 8), (12, 5) ), ( (15,14), (20,10) ) ),
    ( ( ( 7,12), (12, 8) ), ( (16,19), (25,12) ) ),
    ( ( ( 3, 3), (10, 1) ), ( (15,14), (20,10) ) ),
    ( ( ( 7, 8), (12, 5) ), ( (13,10), (16, 4) ) )
)

def corners(ul,lr):
    return ( (ul[0],ul[1]), (ul[0],lr[1]), (lr[0],lr[1]), (lr[0],ul[1]) )

def distances(x, corners):
    return ( (x[0]-c[0])**2 + (x[1]-c[1])**2 for c in corners )

for instance in instances:
    yellow_corners = corners(instance[0][0], instance[0][1])
    blue_corners = corners(instance[1][0], instance[1][1])
    yellow_yellow_distances = distances(yellow, yellow_corners)
    yellow_blue_distances = distances(yellow, blue_corners)
    blue_yellow_distances = distances(blue, yellow_corners)
    blue_blue_distances = distances(blue, blue_corners)
    
    compare_yellow_blue = [ y < b for y,b in zip(yellow_yellow_distances,blue_yellow_distances) ]
    compare_blue_yelow = [ b < y for y,b in zip(yellow_blue_distances,blue_blue_distances) ]
    
    print compare_yellow_blue
    print compare_blue_yelow
