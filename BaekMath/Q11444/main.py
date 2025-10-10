import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def mat_mul(A, B):
    # 2x2 행렬 곱셈 (mod)
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD],
    ]

def mat_pow(A, n):
    # A^n (분할정복, O(log n))
    # n==0이면 항등행렬 I
    I = [[1, 0], [0, 1]]
    if n == 0:
        return I
    if n == 1:
        return A
    half = mat_pow(A, n // 2)
    sq = mat_mul(half, half)
    if n % 2 == 1:
        sq = mat_mul(sq, A)
    return sq

def fib(n):
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]           # 기본 전이 행렬
    Fn = mat_pow(F, n)              # F^n
    return Fn[0][1]                 # F(n)

N = int(input().strip())
print(fib(N))