import sys
from math import gcd

N = int(input())
res = []
for i in range(N):
    a, b = map(int, input().split())
    res.append((a*b) // gcd(a, b))

print("\n".join(map(str, res)))
sys.stdin.readline()