import math
import numpy

A = [ 1, 0, 1, 0, 1, 2 ]
B = [ 1, 1, 0, 0, 1, 6 ]
C = [ 0, 1, 0, 1, 0, 2 ]

def norm2(a):
    return math.sqrt( numpy.dot(a,a) )

def cosine_distance(alpha,a,b):
    a = numpy.copy(a)
    b = numpy.copy(b)
    a[len(a)-1] -= alpha
    b[len(b)-1] -= alpha
    return math.acos( numpy.dot(a,b) / (norm2(a)*norm2(b)) )

for alpha in [ 0, 0.5, 1, 2 ]:
    print alpha,"A","B",cosine_distance(alpha, A, B)
    print alpha,"A","C",cosine_distance(alpha, A, C)
    print alpha,"B","C",cosine_distance(alpha, B, C)
