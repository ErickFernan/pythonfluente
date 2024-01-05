from functools import reduce

def fac(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

