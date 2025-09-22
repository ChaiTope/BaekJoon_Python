import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

lab = []
virus = []
empties = []

for i in range(N):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(M):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            empties.append((i, j))

def spread_virus(room, viruses, walls):
    # 벽 세우기
    for x, y in walls:
        room[x][y] = 1

    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                room[nx][ny] = 2
                q.append((nx, ny))

def count_safe(room):
    return sum(cell == 0 for row in room for cell in row)

best = 0
for walls in combinations(empties, 3):
    # 매 조합마다 복사본에서 시뮬레이션
    room = [r[:] for r in lab]
    spread_virus(room, virus, walls)
    best = max(best, count_safe(room))

print(best)
