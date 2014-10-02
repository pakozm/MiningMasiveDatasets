list = [ 15, 21, 24, 30, 49 ]

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

dict = {}

for i in list:
    for p in factors(i):
        dict.setdefault(p,[]).append(i)

for k in dict:
    print(k, sum(dict[k]))
