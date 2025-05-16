import sys

input = sys.stdin.readline

N = int(input())
L = int(input())

vic = [[] for i in range(N+1)]

for i in range(L):
    a, b = map(int, input().split())
    vic[a].append(b)
    vic[b].append(a)

visited = [False] * (N+1)

def dfs(i):
    visited[i] = True
    for j in vic[i]:
        if not visited[j]:
            dfs(j)

dfs(1)
# 1 제외한 감염된 컴퓨터 수
print(sum(visited) - 1)