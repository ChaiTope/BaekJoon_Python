import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = list(range(101))
for _ in range(N):
    a, b = map(int, input().split())
    board[a] = b
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

q = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while q:
    pos, cnt = q.popleft()
    if pos == 100:
        print(cnt)
        break
    for d in range(1, 7):
        nxt = pos + d
        if nxt <= 100:
            nxt = board[nxt]   # 사다리/뱀 처리
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt+1))