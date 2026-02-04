import sys
import heapq

input = sys.stdin.readline

N = int(input())

array = list(map(int, input().split()))
M = int(input())
operations = []

for i in range(M):
    l, r, c = map(int, input().split())
    operations.append((l, r, c))

def apply(u, l, r):
    # u: tuple
    # l, r: 1-based index (문제 입력 기준)

    i = l - 1
    j = r - 1

    if i == j:
        return u

    # 튜플은 불변이라 리스트로 잠깐 바꿔서 swap
    lst = list(u)
    lst[i], lst[j] = lst[j], lst[i]
    return tuple(lst)

def dijkstra():
    start = tuple(array)
    target = tuple(sorted(array))

    if start == target:
        return 0

    dist = {start: 0}
    pq = [(0, start)]
    while pq:

        cost, u = heapq.heappop(pq)
        if cost != dist[u]:
            continue

        if u == target:
            return cost

        for l, r, c in operations:
            v = apply(u, l, r)
            if v == u:
                continue
            new_cost = cost + c

            if v not in dist or new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    return -1

print(dijkstra())