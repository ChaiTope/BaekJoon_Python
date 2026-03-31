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

def kruskal(n, edges):
    parent = [i for i in range(n + 1)]
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    count = 0

    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            count += 1

            if count == n - 1:
                break

    return total_cost


N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

print(kruskal(N, edges))