import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(E)]

edges.sort(key=lambda x: x[2])  # w(가중치) 기준 오름차순

parent = [i for i in range(V + 1)]

size = [1] * (V + 1)

# 유니온 파인드 함수
def find(x):
    # 비재귀 + 경로 압축
    root = x
    while parent[root] != root:
        root = parent[root]
    while parent[x] != root:
        parent[x], x = root, parent[x]
    return root

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

total = 0  # 가중치 합
count = 0  # 선택된 간선 개수

for u, v, w in edges:
    # 두 정점이 아직 연결되지 않았다면
    if find(u) != find(v):
        union(u, v)
        total += w
        count += 1

        # 트리는 정점 수 - 1개 간선이면 완성
        if count == V - 1:
            break

print(total)