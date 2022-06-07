"""
Problem 5 Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from fractions import gcd
from functools import reduce

def lcm(*values):
    values = [value for value in values]
    if values:
        n  = max(values)
        m = n
        values.remove(n)
        while any( n % value for value in values ):
            n +=m
        return n
    return 0

print (reduce(lcm, range(1,21)))
