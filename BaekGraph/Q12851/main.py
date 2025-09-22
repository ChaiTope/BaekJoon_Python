import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100000

# 바로 같은 위치면 0초, 경우의 수 1
if N == K:
    print(0)
    print(1)
    sys.exit(0)

# N > K면 뒤로만 가는 게 최단(직선), 경우의 수 1
if N > K:
    print(N - K)
    print(1)
    sys.exit(0)

dist = [-1] * (MAX + 1)  # 최단 시간
cnt  = [0] * (MAX + 1)   # 최단 경로 수

q = deque([N])
dist[N] = 0
cnt[N] = 1

while q:
    x = q.popleft()

    # BFS 특성상 dist는 비내림차순. K의 최단거리 확정 후 그보다 깊은 레벨은 볼 필요 없음.
    if dist[K] != -1 and dist[x] > dist[K]:
        break

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX:
            # 처음 방문: 최단 시간 갱신 + 경로 수 승계
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                cnt[nx] = cnt[x]
                q.append(nx)
            # 같은 최단 시간으로 재도달: 경로 수 누적
            elif dist[nx] == dist[x] + 1:
                cnt[nx] += cnt[x]

print(dist[K])
print(cnt[K])
