def sieve(n):
    is_prime = [True] * (n + 1)  # 0부터 n까지 모두 True로 초기화
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):  # √N까지만 검사
        if is_prime[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수들을 False 처리
                is_prime[j] = False

    # True인 값의 인덱스(= 소수)만 리스트로 반환
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

while True:
    n = int(input())
    if n == 0:
        break
    nprime = sieve(n)
    n2prime = sieve(2 * n)
    print(len(n2prime) - len(nprime))