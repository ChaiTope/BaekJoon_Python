import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())

    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])  # 비용 오름차순 정렬
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_cost = 0
max_edge = 0  # MST에 포함된 간선 중 가장 큰 가중치

for a, b, cost in edges:
    if find(a) != find(b):  # 사이클 방지
        union(a, b)
        total_cost += cost
        max_edge = max(max_edge, cost)  # MST에 포함된 간선 중 최대값 갱신

# 가장 비싼 간선 제거
print(total_cost - max_edge)
