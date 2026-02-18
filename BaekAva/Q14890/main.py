import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def can_pass(line):
    used = [False] * N  # 경사로 깔린 칸 표시(중복 방지)

    for i in range(N - 1):
        cur = line[i]
        nxt = line[i + 1]

        if cur == nxt:
            continue

        # 높이 차 2 이상이면 바로 불가
        if abs(cur - nxt) >= 2:
            return False

        # 오르막: cur -> cur+1  (뒤로 L칸 확인)
        if nxt == cur + 1:
            for k in range(i, i - L, -1):
                if k < 0:
                    return False
                if line[k] != cur:
                    return False
                if used[k]:
                    return False
                used[k] = True

        # 내리막: cur -> cur-1 (앞으로 L칸 확인)
        elif nxt == cur - 1:
            for k in range(i + 1, i + 1 + L):
                if k >= N:
                    return False
                if line[k] != nxt:
                    return False
                if used[k]:
                    return False
                used[k] = True

        else:
            return False

    return True

ans = 0

# 행 체크
for r in range(N):
    if can_pass(board[r]):
        ans += 1

# 열 체크
for c in range(N):
    col = [board[r][c] for r in range(N)]
    if can_pass(col):
        ans += 1

print(ans)