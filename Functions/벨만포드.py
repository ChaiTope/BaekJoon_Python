dist[start] = 0

# N-1번 반복
for _ in range(N-1):
    for (u, v, w) in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

# 음수 사이클 체크
for (u, v, w) in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print("음수 사이클 존재")