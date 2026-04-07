N = int(input())
A = sorted(map(int, input().split()))
cnt = 0
for i in range(N):
    l, r = 0, N-1
    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        s = A[l] + A[r]
        if s > A[i]:
            r -= 1
        elif s < A[i]:
            l += 1
        else:
            cnt += 1
            break

print(cnt)