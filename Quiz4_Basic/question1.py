import numpy
U = [
    [ 1, 2, 3, 4, 5 ],
    [ 2, 3, 2, 5, 3 ],
    [ 5, 5, 5, 3, 2 ],
]

U1 = U - numpy.mean(U,0)
U2 = U1 - numpy.reshape(numpy.mean(U1,1), (3,1))

print U2

print numpy.min(U2)
print numpy.max(U2)
