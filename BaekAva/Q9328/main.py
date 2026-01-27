import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

## 탐색을 위해서 그래프 전체를 "."으로 감싸기
def tuck(graph, row, col):
    new_col, new_row = col + 2, row + 2
    padded = [["."] * new_col for _ in range(new_row)]
    for i in range(1, new_row-1):
        for j in range(1, new_col-1):
            padded[i][j] = graph[i-1][j-1]

    return padded


for i in range(T):
    N, M = map(int, input().split())
    padded_row = N + 2
    padded_col = M + 2
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0

    inputs = [list(input().rstrip()) for _ in range(N)]

    key_line = input().strip()
    keys = set() if key_line == "0" else set(key_line)

    visited = [[False] * padded_col for _ in range(padded_row)]
    waiting_doors = [[] for _ in range(26)]

    maps = tuck(inputs, N, M)

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if not (0 <= nr < padded_row and 0 <= nc < padded_col):
                continue

            if visited[nr][nc]:
                continue

            if maps[nr][nc] == ".":
                queue.append((nr, nc))
                visited[nr][nc] = True

            elif maps[nr][nc] == "*":
                continue

            elif maps[nr][nc] == "$":
                cnt += 1
                maps[nr][nc] = "."
                queue.append((nr, nc))
                visited[nr][nc] = True

            elif 'A' <= maps[nr][nc] <= 'Z':
                idx = ord(maps[nr][nc]) - ord('A')
                need_key = maps[nr][nc].lower()

                if need_key in keys:
                    queue.append((nr, nc))
                    visited[nr][nc] = True
                else:
                    waiting_doors[idx].append((nr, nc))

            elif 'a' <= maps[nr][nc] <= 'z':
                k = maps[nr][nc]
                idx = ord(k) - ord('a')
                maps[nr][nc] = "."

                if k not in keys:
                    keys.add(k)
                    for r, c in waiting_doors[idx]:
                        if not visited[r][c]:
                            visited[r][c] = True
                            queue.append((r, c))
                    waiting_doors[idx].clear()

                queue.append((nr, nc))
                visited[nr][nc] = True

    print(cnt)