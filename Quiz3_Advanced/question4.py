def h(x):
    return (3*x + 7) % 11

def num_trailing_zeros(x):
    s = "%04d"%(x)
    return len(s)-len(s.rstrip('0'))

print(4)

for data in [ [2,3,6,9], [2,5,7,10], [3,4,8,10], [1,3,9,10] ]:
    R = max([ num_trailing_zeros(h(x)) for x in data ])
    print(2**R)
