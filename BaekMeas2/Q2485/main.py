from math import gcd

N = int(input())

trees = [0] * N
dist = [0] * (N-1)

F = int(input())
trees[0] = F
for i in range(1, N):
    M = int(input())
    trees[i] = M
    dist[i-1] = trees[i] - trees[i - 1]

min_dis = gcd(*dist)
res = 0
if N > 2:
    for i in range(N - 1):
        res += (dist[i] - min_dis) // min_dis
else:
    res += min_dis - 1
print(res)