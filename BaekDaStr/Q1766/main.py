import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N+1)
workbook = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    workbook[a].append(b)
    indegree[b] += 1

def topological_sort(graph):
    pq = []
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        cur = heapq.heappop(pq)  # 가장 작은 번호
        result.append(cur)

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(pq, nxt)

    print(*result)

topological_sort(workbook)