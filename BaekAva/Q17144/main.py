import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
A = []
AT = AB = -1  # 공기청정기 위/아래 행
for i in range(R):
    row = list(map(int, input().split()))
    A.append(row)
    if row[0] == -1 and AT == -1:
        AT = i        # 위쪽 청정기
        AB = i + 1    # 아래쪽 청정기

dirs = ((1,0), (-1,0), (0,1), (0,-1))

# 순환 경로(한 번만 구성)
path_up = []
for y in range(1, C):                 # →
    path_up.append((AT, y))
for x in range(AT-1, -1, -1):         # ↑
    path_up.append((x, C-1))
for y in range(C-2, -1, -1):          # ←
    path_up.append((0, y))
for x in range(1, AT):                # ↓
    path_up.append((x, 0))

path_dn = []
for y in range(1, C):                 # →
    path_dn.append((AB, y))
for x in range(AB+1, R):              # ↓
    path_dn.append((x, C-1))
for y in range(C-2, -1, -1):          # ←
    path_dn.append((R-1, y))
for x in range(R-2, AB, -1):          # ↑
    path_dn.append((x, 0))

for _ in range(T):
    # 1) 확산 (동시 갱신용 add 사용)
    add = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if A[r][c] == -1 or A[r][c] < 5:
                continue
            spread = A[r][c] // 5
            cnt = 0
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                    add[nr][nc] += spread
                    cnt += 1
            add[r][c] -= spread * cnt

    # 2) 확산 결과 적용
    for r in range(R):
        for c in range(C):
            A[r][c] += add[r][c]

    # 청정기 위치 재설정(안전)
    A[AT][0] = -1
    A[AB][0] = -1

    # 3) 공기청정기 순환
    # 위쪽(반시계)
    for i in range(len(path_up)-1, 0, -1):
        r, c = path_up[i]
        pr, pc = path_up[i-1]
        A[r][c] = A[pr][pc]
    A[AT][1] = 0
    A[AT][0] = -1

    # 아래쪽(시계)
    for i in range(len(path_dn)-1, 0, -1):
        r, c = path_dn[i]
        pr, pc = path_dn[i-1]
        A[r][c] = A[pr][pc]
    A[AB][1] = 0
    A[AB][0] = -1

# 4) 합계 출력(청정기 -1 제외)
ans = 0
for r in range(R):
    for c in range(C):
        if A[r][c] > 0:
            ans += A[r][c]
print(ans)