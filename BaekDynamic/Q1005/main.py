import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    build = [0] + list(map(int, input().split()))  # 1번부터 N번까지 건설 시간

    graph = [[] for _ in range(N + 1)]
    indeg = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)   # X를 지어야 Y를 지을 수 있음 (단방향)
        indeg[Y] += 1

    W = int(input())         # 목표 건물

    # dp[i] = i번 건물을 완성하는 데 걸리는 최소 시간
    dp = [0] * (N + 1)

    q = deque()

    # 진입차수 0인 건물들 = 선행 조건 없이 바로 지을 수 있는 애들
    for i in range(1, N + 1):
        if indeg[i] == 0:
            dp[i] = build[i]
            q.append(i)

    # 위상 정렬 + DP
    while q:
        u = q.popleft()
        for v in graph[u]:
            # u를 통해 v를 지을 때 걸리는 시간 후보: dp[u] + build[v]
            if dp[v] < dp[u] + build[v]:
                dp[v] = dp[u] + build[v]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    print(dp[W])
