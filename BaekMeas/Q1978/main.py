import math

N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if i < 2:
        continue

    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)