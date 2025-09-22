import sys
input = sys.stdin.readline

INF = 10**9

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(r)]

def floyd_warshall(n, edges):
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0
    # 무방향 간선 반영 (간선 길이는 그대로; m으로 필터링하지 않음)
    for a, b, c in edges:
        if c < dist[a][b]:
            dist[a][b] = c
            dist[b][a] = c
    # FW
    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd
    return dist

dist = floyd_warshall(n, edges)

# 각 시작점 s에서 dist[s][t] <= m 인 t들의 아이템 합을 구해 최댓값
answer = 0
for s in range(1, n + 1):
    total = 0
    for t in range(1, n + 1):
        if dist[s][t] <= m:          # 자기 자신(0) 포함해서 OK
            total += items[t - 1]
    if total > answer:
        answer = total

print(answer)
