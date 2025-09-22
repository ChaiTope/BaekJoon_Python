import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 입력부터 mod 1000로 정리(선택이지만 안정적)
A = [[x % 1000 for x in row] for row in A]

def multiply(M1, M2):
    """M1 x M2 (mod 1000) -> new matrix"""
    N = len(M1)
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):           # 약간의 캐시 이점
            if M1[i][k] == 0:
                continue
            aik = M1[i][k]
            for j in range(N):
                res[i][j] = (res[i][j] + aik * M2[k][j]) % 1000
    return res

def power(M, b):
    if b == 1:
        # 기저에서 mod 보장
        return [[x % 1000 for x in row] for row in M]
    if b % 2 == 0:
        half = power(M, b // 2)
        return multiply(half, half)
    else:
        return multiply(M, power(M, b - 1))

ans = power(A, B)

for row in ans:
    print(*row)
