import sys

input = sys.stdin.readline

MOD = 10**9+7

N, M = map(int, input().split())

K = min(N, M)

def sieve(n):
    is_prime = [True] * (n + 1)  # 0부터 n까지 모두 True로 초기화
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):  # √N까지만 검사
        if is_prime[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수들을 False 처리
                is_prime[j] = False

    # True인 값의 인덱스(= 소수)만 리스트로 반환
    return is_prime

is_prime = sieve(K)

ans = 1

for p in range(2, K+1):
    if is_prime[p]:
        # 여기서 바로 p 사용

        E_p = 0
        pk = p

        while pk <= K:
            E_p += (N // pk) * (M // pk)
            pk = pk * p

        ans = ans * pow(p, E_p, MOD) % MOD

print(ans)