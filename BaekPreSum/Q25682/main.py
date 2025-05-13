import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 1. board 초기화 (1-based 편의를 위해 N+1×M+1)
board = [[0]*(M+1) for _ in range(N+1)]

# 2. 입력 채우기
for i in range(1, N+1):
    row = input().strip()        # "BBBB...WBWBW"
    for j, ch in enumerate(row, start=1):
        board[i][j] = 1 if ch == 'B' else 0

# 3. 누적합 배열
S1 = [[0]*(M+1) for _ in range(N+1)]
S2 = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        miss1 = board[i][j] != ((i+j)&1)
        miss2 = board[i][j] != (((i+j)&1)^1)
        S1[i][j] = miss1 + S1[i-1][j] + S1[i][j-1] - S1[i-1][j-1]
        S2[i][j] = miss2 + S2[i-1][j] + S2[i][j-1] - S2[i-1][j-1]

# 4. 정답 탐색
ans = float('inf')
for i in range(1, N-K+2):
    for j in range(1, M-K+2):
        x2, y2 = i+K-1, j+K-1
        cnt1 = S1[x2][y2] - S1[i-1][y2] - S1[x2][j-1] + S1[i-1][j-1]
        cnt2 = S2[x2][y2] - S2[i-1][y2] - S2[x2][j-1] + S2[i-1][j-1]
        ans = min(ans, cnt1, cnt2)

print(ans)
