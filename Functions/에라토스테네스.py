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

# 메모리 최적화 및, 소수 자체의 배열은 필요 없을 경우
def sieve_bytearray(n):
    # 0과 1은 소수가 아니므로 0
    # 나머지는 우선 1로(소수 가정)
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0

    import math
    r = int(math.isqrt(n))  # sqrt(n)

    for i in range(2, r + 1):
        if is_prime[i]:
            # i*i부터 시작해서 i씩 증가하며 지우기
            step = i
            start = i * i
            is_prime[start: n + 1: step] = b'\x00' * (((n - start) // step) + 1)

    return is_prime