import sys

input = sys.stdin.readline

N = int(input())
INF = float('inf')

# W[i][j]일 때, i애서 j로 가는 비용.
W = [list(map(int, input().split())) for _ in range(N)]

# dp[현재도시][방문마스크
dp = [[INF] * (1 << (N-1)) for _ in range(N)]

def dfs(curr, visited):
    if dp[curr][visited] != INF:
        return dp[curr][visited]

    if visited == ((1 << (N-1))-1):
        if W[curr][0] != 0:
            dp[curr][visited] = W[curr][0]

        return dp[curr][visited]

    for i in range(1, N):
        if not W[curr][i]:
            continue
        if visited & (1 << (i - 1)):
            continue

        dp[curr][visited] = min(dp[curr][visited], W[curr][i] + dfs(i, visited|(1<<(i-1))))

    return dp[curr][visited]

print(dfs(0, 0))