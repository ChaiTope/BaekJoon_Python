import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = 10 ** 9

dist = [[INF]*N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    dist[a-1][b-1] = 1
    dist[b-1][a-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            # k를 거쳐서 i->j 가는 게 더 짧으면 갱신
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

min_sum = INF
ans = -1
for i in range(N):
    total = sum(dist[i])            # i번 사람이 다른 모든 사람까지의 합
    if total < min_sum:
        min_sum = total
        ans = i + 1                 # 1번부터 번호를 매겼으므로 +1

print(ans)