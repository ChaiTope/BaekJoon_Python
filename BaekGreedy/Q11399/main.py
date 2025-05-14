import sys

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

P = sorted(P)

print(*P)

W = [0]
for i in P:
    W.append(max(W) + i)

print(sum(W))
#1, 3, 6, 9, 13