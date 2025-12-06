import sys

input = sys.stdin.readline

mod = 10**9+7
INF = float('inf')
N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

tree = [1] * (4*N)   # 곱의 항등원은 1

def build(node, start, end):
    if start == end:
        tree[node] = arr[start] % mod
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1]) % mod


def query(node, start, end, left, right):
    if end < left or right < start:
        return 1  # 곱의 항등원

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = query(node*2, start, mid, left, right)
    r = query(node*2+1, mid+1, end, left, right)
    return (l * r) % mod

def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return

    if start == end:
        tree[node] = val % mod
        return

    mid = (start + end) // 2
    update(node*2, start, mid, idx, val)
    update(node*2+1, mid+1, end, idx, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % mod


build(1, 1, N)

for i in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
        continue

    print(query(1, 1, N, b, c))