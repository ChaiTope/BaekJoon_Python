import sys

input = sys.stdin.readline

INF = float('inf')
N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

tree_min = [INF] * (4*N)
tree_max = [-INF] * (4*N)

def build(node, start, end):
    if start == end:  # 리프
        tree_min[node] = arr[start]
        tree_max[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree_min[node] = min(tree_min[node*2], tree_min[node*2+1])
        tree_max[node] = max(tree_max[node*2], tree_max[node*2+1])

def query(node, start, end, left, right):
    if end < left or right < start:
        return INF, -INF  # min에 영향 안 주는 큰 값, max에 영향 안 주는 작은 값

    if left <= start and right >= end:
        return tree_min[node], tree_max[node]

    # 부분 겹침
    mid = (start + end) // 2
    lmin, lmax = query(node*2, start, mid, left, right)
    rmin, rmax = query(node*2+1, mid+1, end, left, right)
    return (min(lmin, rmin), max(lmax, rmax))

build(1, 1, N)

for i in range(M):
    a, b = map(int, input().split())
    if a > b:
        c = a
        a = b
        b = c

    mn, mx = query(1, 1, N, a, b)
    print(mn, mx)