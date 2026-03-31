import heapq
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

def dijkstra():
    INF = float('inf')
    dist = [[INF] * M for _ in range(N)]
    dist[0][0] = 0

    pq = []
    heapq.heappush(pq, (0, 0, 0))  # (벽 부순 횟수, x, y)

    while pq:
        d, x, y = heapq.heappop(pq)

        if d > dist[x][y]:
            continue

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 핵심: 다음 칸이 벽이면 +1
                nd = d + board[nx][ny]

                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))

    return dist[N-1][M-1]

print(dijkstra())