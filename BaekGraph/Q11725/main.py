import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0]*(N+1)
q = deque([1])
parent[1] = 1    # 또는 0으로 두고 안 찍어도 상관없어

while q:
    x = q.popleft()
    for y in adj[x]:
        if parent[y] == 0:      # 아직 방문 안 한 자식이면
            parent[y] = x      # x를 y의 부모로 기록
            q.append(y)

for i in range(2, N+1):
    print(parent[i])
