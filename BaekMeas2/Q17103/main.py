from bisect import bisect_right


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

N = int(input())
w = []
for i in range(N):
    w.append(int(input()))
primes  = sieve(max(w))
for i in w:
    count = 0
    left, right = 0, bisect_right(primes, i) -1

    while left <= right:
        total = primes[left] + primes[right]

        if total == i:
            count += 1
            left += 1
            right -= 1
        elif total < i:
            left += 1
        else:
            right -= 1

    print(count)