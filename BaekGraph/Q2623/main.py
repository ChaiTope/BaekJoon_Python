import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N + 1)
stage = [[] for _ in range(N + 1)]

for _ in range(M):
    singers = list(map(int, input().split()[1:]))

    for i in range(len(singers)-1):
        stage[singers[i]].append(singers[i+1])
        indegree[singers[i+1]] += 1

def topological_sort(graph):
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        result.append(cur)

        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    if len(result) != N:
        print(0)
    else:
        for x in result:
            print(x)

topological_sort(stage)