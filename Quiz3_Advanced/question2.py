import numpy
# adjacency matrix
order = [ '1' , '2', '3', '4', '5', '6' ]
index = { '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5 }
graph = {
    '1' : [ '2', '3' ],
    '2' : [ '1', '4', '6' ],
    '3' : [ '1', '4' ],
    '4' : [ '2', '3', '5' ],
    '5' : [ '4', '6' ],
    '6' : [ '2', '5' ],
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

u,s,v = numpy.linalg.svd(L)

eig2 = u[:,len(order)-2]
mean = numpy.mean(eig2)
print(mean, eig2)
print(eig2 < mean)
print(eig2 > mean)
print(eig2 == mean)
