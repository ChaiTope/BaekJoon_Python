import sys
input = sys.stdin.readline

MOD = 1_000_000_007

M = int(input())
ans = 0
for _ in range(M):
    N, S = map(int, input().split())
    S %= MOD
    invN = pow(N, MOD - 2, MOD)   # N의 모듈러 역원 (페르마의 소정리)
    ans = (ans + S * invN) % MOD

print(ans)
