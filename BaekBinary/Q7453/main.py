import sys
from collections import Counter

input = sys.stdin.readline

A, B, C, D = [], [], [], []

N = int(input())
ans = 0

for i in range(N):
    a, b, c, d = map(int, input().split())

    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

CD = []

for i in range(N):
    for j in range(N):
        CD.append(C[i] + D[j])

CD_count = Counter(CD)

for i in range(N):
    for j in range(N):
        s = A[i] + B[j]
        ans += CD_count[-s]
print(ans)