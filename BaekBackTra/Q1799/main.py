import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 비숍은 같은 색 칸끼리만 서로 영향을 줌 (흑/백 분리)
cand = [[], []]  # cand[0] : (i+j)%2==0, cand[1] : (i+j)%2==1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            cand[(i + j) & 1].append((i, j))

# 대각선 점유 체크 배열
# / 대각선: i+j (0..2N-2)
# \ 대각선: i-j+(N-1) (0..2N-2)
used_sum = [False] * (2 * N - 1)
used_diff = [False] * (2 * N - 1)

def solve(cands):
    best = 0
    L = len(cands)

    def dfs(idx, cnt):
        nonlocal best

        # 가지치기: 남은 칸 다 놓아도 best 못 넘으면 컷
        if cnt + (L - idx) <= best:
            return

        if idx == L:
            if cnt > best:
                best = cnt
            return

        x, y = cands[idx]
        s = x + y
        d = x - y + (N - 1)

        # 1) 안 놓기
        dfs(idx + 1, cnt)

        # 2) 놓기 (대각선 2개가 비어있을 때만)
        if not used_sum[s] and not used_diff[d]:
            used_sum[s] = True
            used_diff[d] = True
            dfs(idx + 1, cnt + 1)
            used_sum[s] = False
            used_diff[d] = False

    dfs(0, 0)
    return best

ans = solve(cand[0]) + solve(cand[1])
print(ans)
