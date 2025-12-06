import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
tree = [0] * (N + 1)

def prefix_sum(x):
    res = 0
    while x > 0:
        res += tree[x]
        x -= (x & -x)
    return res

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & -i)

for i in range(1, N+1):
    update(i, arr[i])

for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(b, diff)
        continue

    ans = prefix_sum(c) - prefix_sum(b-1)
    print(ans)