import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))

    ps = [0] * (n + 1)
    for i in range(n):
        ps[i + 1] = ps[i] + A[i]

    dp = [[0] * n for _ in range(n)]
    opt = [[0] * n for _ in range(n)]

    for i in range(n):
        opt[i][i] = i

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = ps[j + 1] - ps[i]
            dp[i][j] = float('inf')

            l = opt[i][j - 1]
            r = opt[i + 1][j] if i + 1 <= j else j - 1
            r = min(r, j - 1)   # 중요

            for k in range(l, r + 1):
                val = dp[i][k] + dp[k + 1][j] + total
                if val < dp[i][j]:
                    dp[i][j] = val
                    opt[i][j] = k

    print(dp[0][n - 1])