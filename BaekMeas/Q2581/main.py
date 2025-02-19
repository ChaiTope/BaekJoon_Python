import math

M, N = int(input()), int(input())
count = []
for i in range(M, N+1):
    if i < 2:
        continue

    is_prime = True

    for j in range(2, math.isqrt(i) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        count.append(i)

if not count:
    print(-1)
else:
    print(f"{sum(count)}\n{count[0]}")