import sys
from math import gcd
a, b = map(int, sys.stdin.readline().strip().split())

print((a*b) // gcd(a, b))