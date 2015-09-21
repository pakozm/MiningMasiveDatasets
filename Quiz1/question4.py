L = [ 15, 21, 24, 30, 49 ]

def factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

D = {}

for i in L:
    for p in factors(i):
        D.setdefault(p,[]).append(i)

for k in D:
    print(k, sum(D[k]))
