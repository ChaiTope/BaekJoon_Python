import sys
input = sys.stdin.readline

N, M = map(int, input().split())

parent = list(range(N + 1))

def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])   # 경로 압축
    return parent[x]

for _ in range(M):
    s, a, b = map(int, input().split())

    if s == 0:
        ra = find_parent(a)
        rb = find_parent(b)
        if ra != rb:
            parent[rb] = ra   # 루트끼리 연결 (방향은 아무거나)
    else:
        print("YES" if find_parent(a) == find_parent(b) else "NO")
