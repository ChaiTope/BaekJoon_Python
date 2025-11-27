import sys


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

primes = sieve(4000000)

input = sys.stdin.readline()

N = int(input)

left, right = 0, 0
current_sum = primes[0]
count = 0

while right < len(primes):
    if current_sum < N:
        right += 1
        if right == len(primes): break
        current_sum += primes[right]
    elif current_sum > N:
        current_sum -= primes[left]
        left += 1
    else:
        count += 1
        current_sum -= primes[left]
        left += 1

print(count)