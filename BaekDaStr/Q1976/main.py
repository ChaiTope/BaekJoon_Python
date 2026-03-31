import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
parents = [n for n in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            union(parents, i, j)

dest = list(map(int, input().split()))
group = find(parents, dest[0] - 1)

for x in dest[1:]:
    if find(parents, x - 1) != group:
        print("NO")
        break
else:
    print("YES")