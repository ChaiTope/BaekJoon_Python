import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(map(int, input().strip())) for _ in range(N)]
g_id = [[0 for _ in range(M)] for _ in range(N)]

# 벽은 -1로 표시
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            g_id[i][j] = -1

g_size = [0]   # g_size[group_id] = 그 그룹의 크기
group_id = 0

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(si, sj, group_id):
    q = deque()
    q.append((si, sj))
    g_id[si][sj] = group_id
    cnt = 1

    while q:
        i, j = q.popleft()
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if maps[ni][nj] == 0 and g_id[ni][nj] == 0:
                    g_id[ni][nj] = group_id
                    q.append((ni, nj))
                    cnt += 1
    return cnt

# 0 덩어리 라벨링 + 크기 저장
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0 and g_id[i][j] == 0:
            group_id += 1
            g_size.append(bfs(i, j, group_id))

# 정답 출력 만들기
out_lines = []
for i in range(N):
    row = []
    for j in range(M):
        if maps[i][j] == 0:
            row.append('0')
        else:
            total = 1
            seen = set()
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    gid = g_id[ni][nj]
                    if gid > 0 and gid not in seen:   # 벽(-1) 제외 + 중복 제거
                        seen.add(gid)
                        total += g_size[gid]
            row.append(str(total % 10))
    out_lines.append(''.join(row))

print('\n'.join(out_lines))
