import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    edges = []
    # 도로: 양방향
    for __ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s-1, e-1, t))
        edges.append((e-1, s-1, t))
    # 웜홀: 단방향, 음수 가중치
    for __ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s-1, e-1, -t))

    # 모든 정점에서 출발하는 것처럼 0으로 초기화
    dist = [0] * N
    cycle = False

    # 벨만-포드: V번 반복했을 때도 갱신되면 음수 사이클 존재
    for i in range(N):
        updated = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
        # N번째 반복에서 갱신이 일어났다면 음수 사이클
        if i == N-1 and updated:
            cycle = True

    print("YES" if cycle else "NO")