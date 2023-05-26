"""
This program returns the cartesian product of two lists received as input.
"""

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(*product(a,b))
