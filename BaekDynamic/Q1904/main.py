import sys
input = sys.stdin.readline

MOD = 15746
N = int(input())

if N == 1:
    print(1)
    sys.exit()

# dp[1], dp[2]
a, b = 1, 2
for i in range(3, N+1):
    # 다음 항 구하기
    c = (a + b) % MOD
    a, b = b, c

print(b)
