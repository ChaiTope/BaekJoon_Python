import sys
import heapq

input = sys.stdin.readline
cnt = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def dijkstra(i, j):
    INF = float('inf')
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = board[0][0]

    pq = []
    heapq.heappush(pq, (dist[0][0], i, j))  # (거리, 정점)

    while pq:
        c, x, y = heapq.heappop(pq)
        if c > dist[x][y]:
            continue  # 이미 더 짧은 경로가 발견된 상태

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nd = c + board[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))

    return dist[N-1][N-1]

while True:
    cnt += 1
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    print("Problem "+str(cnt)+": "+str(dijkstra(0, 0)))