target, L = map(int, input().split())

while L < 101:
    start = target - (L * (L - 1) // 2)

    if start >= 0 and start % L == 0:
        start //= L
        for i in range(start, start + L):
            print(i, end=" ")
        exit()

    L += 1

print(-1)