N, M, K = map(int, input().split())
L, J = max(N, M), min(N, M)
if J > 1:
    print(-1)
elif K == 0 and L > 2:
    print(-1)
else:
    if K == 0:
        arr = [0] * L
    else:
        arr = [(i // 2) * (K + 1) + (i % 2) for i in range(L)]

    if N == 1:
        print(*arr)
    else:
        for v in arr:
            print(v)