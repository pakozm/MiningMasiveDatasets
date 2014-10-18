import numpy
# adjacency matrix
order = [ 'A' , 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]
index = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7 }
graph = {
    'A' : [ 'C', 'F' ],
    'B' : [ 'E', 'H' ],
    'C' : [ 'A', 'D', 'F' ],
    'D' : [ 'C', 'E', 'G' ],
    'E' : [ 'B', 'D', 'H' ],
    'F' : [ 'A', 'C', 'G' ],
    'G' : [ 'D', 'F', 'H' ],
    'H' : [ 'B', 'E', 'G' ]
}

def mat(func):
    return numpy.array([ [ func(i,j) for j in range(0,len(order)) ] for i in range(0,len(order)) ])

def edge(i,j):
    if order[j] in graph[order[i]]: return 1
    else: return 0

def degree(i,j):
    if i != j: return 0
    else: return len(graph[order[i]])

A = mat(edge)
D = mat(degree)
L = D - A

print(A)
print(D)
print(L)
print(numpy.sum(L))
print( numpy.sum((D == 0)) )
print( numpy.sum((D != 0)) )
