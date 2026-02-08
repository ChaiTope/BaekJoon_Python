import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

lines = []
parent = [i for i in range(N)]

def ccw(x1, y1, x2, y2, x3, y3):
    return  x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

def intersect(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    ab1 = ccw(x1, y1, x2, y2, x3, y3)
    ab2 = ccw(x1, y1, x2, y2, x4, y4)
    cd1 = ccw(x3, y3, x4, y4, x1, y1)
    cd2 = ccw(x3, y3, x4, y4, x2, y2)

    ab = ab1 * ab2
    cd = cd1 * cd2

    if ab == 0 and cd == 0:
        A = (x1, y1)
        B = (x2, y2)
        C = (x3, y3)
        D = (x4, y4)

        if A > B: A, B = B, A
        if C > D: C, D = D, C

        return not (B < C or D < A)
    return ab <= 0 and cd <= 0

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    lines.append((x1, y1, x2, y2))

for i in range(N):
    l1 = lines[i]
    for j in range(i+1, N):
        l2 = lines[j]

        if intersect(l1, l2):
            union(i, j)

# 최종 정규화
for i in range(N):
    parent[i] = find(i)

res = Counter(parent)

print(len(res))
print(max(res.values()))