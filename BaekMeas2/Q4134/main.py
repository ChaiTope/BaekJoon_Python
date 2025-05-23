import math
import sys

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    sqrt_n = int(math.sqrt(n))
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

N = int(sys.stdin.readline().strip())

prime = []

for j in range(N):
    M = int(sys.stdin.readline().strip())
    while not is_prime(M):
        M += 1

    prime.append(M)

print("\n".join(map(str, prime)))