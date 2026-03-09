import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

candies = [0] + list(map(int, input().split()))  # 1-index
friends = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
group = []

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1, N + 1):
    if visited[i]:
        continue

    q = deque([i])
    visited[i] = True
    cnt = 0
    summary = 0

    while q:
        cur = q.pop()
        cnt += 1
        summary += candies[cur]

        for nxt in friends[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    group.append((cnt, summary))

cap = K - 1  # K명 이상이면 울리니까, 최대 K-1명까지
dp = [-10**18] * (cap + 1)
dp[0] = 0

for cnt, s in group:
    if cnt > cap:
        continue
    for j in range(cap, cnt - 1, -1):
        dp[j] = max(dp[j], dp[j - cnt] + s)

print(max(dp))