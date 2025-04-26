N = int(input())
MOD = 1_000_000_000

# 1) 초기화: 1자리 계단수 개수 세팅
dp = [[0]*10 for _ in range(N+1)]
for d in range(1, 10):
    dp[1][d] = 1

# 2) 점화식 적용: i=2부터 N까지
for i in range(2, N+1):
    # d=0,9는 따로 처리
    dp[i][0] = dp[i-1][1] % MOD
    dp[i][9] = dp[i-1][8] % MOD

    # 1~8은 공통 점화식
    for d in range(1, 9):
        dp[i][d] = (dp[i-1][d-1] + dp[i-1][d+1]) % MOD

# 3) 정답 출력
print(sum(dp[N]) % MOD)
