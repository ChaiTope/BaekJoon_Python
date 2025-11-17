# Platinum 4

## 문제
N과 M 이 주어졌을 때, GCD(1, 1) × GCD(1, 2) × ... × GCD(1, M) × GCD(2, 1) × GCD(2, 2) × ... × GCD(2, M) × ... × GCD(N, 1) × GCD(N, 2) × ... × GCD(N, M)을 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N, M ≤ 15,000,000)

## 출력
첫째 줄에 곱을 109+7로 나눈 나머지를 출력한다.

## Thinking!!
O(NM log N) << 이거론 절대 안되고,

ans * (p ** E_p % MOD) % MOD << 이것도 pow 써야함.

### [True] 대신 bytearray 사용 예시.
    def sieve_bytearray(n):
        # 0과 1은 소수가 아니므로 0
        # 나머지는 우선 1로(소수 가정)
        is_prime = bytearray([1]) * (n + 1)
        is_prime[0] = is_prime[1] = 0
    
        import math
        r = int(math.isqrt(n))   # sqrt(n)
    
        for i in range(2, r + 1):
            if is_prime[i]:
                # i*i부터 시작해서 i씩 증가하며 지우기
                step = i
                start = i * i
                is_prime[start : n+1 : step] = b'\x00' * (((n - start) // step) + 1)
    
        return is_prime
