import sys

N = int(input())
info = [[] for i in range(200)]
for i in range(N):
    x, y = map(str, sys.stdin.readline().strip().split())
    info[int(x)-1].append(y)

for i in range(200):
    for j in info[i]:
        print(i+1, j)