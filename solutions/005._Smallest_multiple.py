from fractions import gcd
from functools import reduce

def lcm(a,b):
    """
    Calculate the lowest common multiple of two integers a and b
    """
    return a*b//gcd(a,b)

print reduce(lcm, range(11,21))
