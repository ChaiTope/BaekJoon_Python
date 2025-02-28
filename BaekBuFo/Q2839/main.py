N = int(input())

min_val = float('inf')

for i in range((N // 5) + 1):
    if (N - (5 * i)) % 3 == 0:
        for j in range((N // 3) + 1):
            if N - ((5 * i) + (3 * j)) == 0:
                min_val = min(min_val, i + j)

if min_val == float('inf'):
    min_val = -1
print(min_val)