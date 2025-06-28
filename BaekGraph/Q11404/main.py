import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 10**12

dist = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

# Floyd–Warshall
for k in range(1, N+1):
    for i in range(1, N+1):
        # i→k 가 불가능하면 넘어가기
        if dist[i][k] == INF:
            continue
        for j in range(1, N+1):
            # k→j 가 불가능하면 넘어가기
            if dist[k][j] == INF:
                continue
            # 경유를 통한 갱신
            new_cost = dist[i][k] + dist[k][j]
            if new_cost < dist[i][j]:
                dist[i][j] = new_cost

out = []
for i in range(1, N+1):
    row = []
    for j in range(1, N+1):
        if dist[i][j] == INF:
            row.append('0')
        else:
            row.append(str(dist[i][j]))
    out.append(' '.join(row))
print('\n'.join(out))