import sys

input = sys.stdin.readline

S = input().rstrip()
N = len(S)
INF = float('inf')

dp = [INF] * (N + 1)
dp[0] = 0

is_pal = [[False]*N for _ in range(N)]

for i in range(N):
    is_pal[i][i] = True

    if i < N-1:
        if S[i] == S[i+1]:
            is_pal[i][i+1] = True

for length in range(3, N+1):          # 길이 3..N
    for s in range(0, N-length+1):    # 시작 0..N-length
        e = s + length - 1            # 끝 인덱스
        if S[s] == S[e] and is_pal[s+1][e-1]:
            is_pal[s][e] = True

for i in range(1, N+1):
    for j in range(i):
        if is_pal[j][i-1]:
            dp[i] = min(dp[i], dp[j]+1)

print(dp[N])