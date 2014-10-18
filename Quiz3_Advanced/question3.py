import numpy

def stream(ts):
    return (ts-1)%10 + 1

time=75

def count(a,t0):
    data = [ stream(x) for x in range(t0,time+1) ]
    c = 0
    for x in data:
        if x == a: c+=1
    return c

def surprise():
    data = [ stream(x) for x in range(1,time+1) ]
    counts = {}
    for x in data: counts[x] = counts.setdefault(x,0) + 1
    return sum([counts[x] ** 2 for x in counts])

second_moment = surprise()

for d in [ [25,34,47], [37,46,55], [14,35,42], [24,44,66] ]:
    values = numpy.array([ time * (2*count(stream(t),t)) for t in d ])
    print(numpy.median(values), values)

print(second_moment)
